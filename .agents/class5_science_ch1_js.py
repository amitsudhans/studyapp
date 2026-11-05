"""
Interactive JavaScript for Class 5 Science Chapter 1: Water - The Essence of Life
Features sentence-by-sentence Web Speech API with Indian Male voice priority, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure clean Unicode.
"""

JS_CODE = '''
// Science Chapter 1 Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis Engine (Sentence-by-Sentence Queue with Indian Male Voice Selection)
let isSpeaking = false;
let currentSpeakingSlide = null;
let speechQueue = [];
let speechIndex = 0;
let selectedMaleVoice = null;

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

function getIndianMaleVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const explicitIndianMale = [
        'prabhat', 'rishi', 'ravi', 'madhav', 'pradeep', 'karan', 'amit', 'anil',
        'ajay', 'deepak', 'mohan', 'hemant', 'aravind', 'arun', 'madhur'
    ];

    const inVoices = voices.filter(v =>
        (v.lang && (v.lang.toLowerCase() === 'en-in' || v.lang.toLowerCase().startsWith('en_in') || v.lang.toLowerCase() === 'hi-in')) ||
        (v.name && v.name.toLowerCase().includes('india'))
    );

    for (const mk of explicitIndianMale) {
        const match = inVoices.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemaleVoice(v));
        if (match) return match;
    }

    const inMale = inVoices.find(v => (v.name || '').toLowerCase().includes('male') && !isFemaleVoice(v));
    if (inMale) return inMale;

    const anyInNonFemale = inVoices.find(v => !isFemaleVoice(v) && !(v.name || '').toLowerCase().includes('google indian english'));
    if (anyInNonFemale) return anyInNonFemale;

    const enVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
    const generalMaleKeywords = ['male', 'david', 'mark', 'george', 'daniel', 'guy', 'stefan', 'oliver', 'arthur', 'james', 'richard', 'brian', 'sean', 'alex', 'fred', 'neil'];
    for (const mk of generalMaleKeywords) {
        const match = enVoices.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemaleVoice(v));
        if (match) return match;
    }

    const nonFemale = enVoices.find(v => !isFemaleVoice(v));
    if (nonFemale) return nonFemale;

    return inVoices[0] || voices[0] || null;
}

if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        selectedMaleVoice = getIndianMaleVoice();
    };
    selectedMaleVoice = getIndianMaleVoice();
}

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
    utterance.pitch = 0.88; // Deep, resonant Indian baritone male tone

    if (!selectedMaleVoice) {
        selectedMaleVoice = getIndianMaleVoice();
    }
    if (selectedMaleVoice) {
        utterance.voice = selectedMaleVoice;
    }

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

    // Split text into natural sentences
    const sentences = fullText.match(/[^.!?]+[.!?]+/g) || [fullText];
    speechQueue = sentences.map(s => s.trim()).filter(s => s.length > 0);
    speechIndex = 0;
    isSpeaking = true;
    currentSpeakingSlide = slideNo;

    updateAllAudioButtons();
    speakNextSentence();
}

function toggleCurrentSlideLecture() {
    if (currentSlide > 16) {
        alert("Mastery challenges are interactive exercises and do not have an audio lecture.");
        return;
    }
    const textElem = document.getElementById(`slide-spoken-text-${currentSlide}`);
    if (textElem) {
        startLectureSpeech(textElem.textContent, currentSlide);
    }
}

function updateAllAudioButtons() {
    for (let i = 1; i <= 16; i++) {
        const btn = document.getElementById(`slide-audio-btn-${i}`);
        const badge = document.getElementById(`slide-audio-badge-${i}`);
        if (btn) {
            if (isSpeaking && currentSpeakingSlide === i) {
                btn.innerHTML = '<span>⏹</span><span>Pause Lecture</span>';
                btn.className = "px-3 py-1.5 rounded-xl bg-amber-500/20 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm";
                if (badge) {
                    badge.textContent = "Speaking...";
                    badge.className = "px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30 animate-pulse";
                }
            } else {
                btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
                btn.className = "px-3 py-1.5 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 text-xs font-bold flex items-center space-x-1.5 border border-indigo-500/30 transition shadow-sm";
                if (badge) {
                    badge.textContent = "Audio Lecture Ready";
                    badge.className = "px-2 py-0.5 rounded text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
                }
            }
        }
    }

    const globalBtn = document.getElementById('globalAudioBtn');
    if (globalBtn) {
        if (isSpeaking) {
            globalBtn.innerHTML = '<span>⏹</span><span>Pause Audio</span>';
            globalBtn.className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500/20 text-amber-300 hover:bg-amber-500/30 border border-amber-500/30 flex items-center space-x-1.5 transition";
        } else {
            globalBtn.innerHTML = '<span>🔊</span><span>Listen to Lecture</span>';
            globalBtn.className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/30 border border-indigo-500/30 flex items-center space-x-1.5 transition";
        }
    }
}

// Slide Navigation
function goToSlide(slideNo) {
    if (slideNo < 1 || slideNo > totalSlides) return;
    stopSpeech();

    // Hide all slides
    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) el.style.display = 'none';
    }

    // Show target slide
    const target = document.getElementById(`slide-${slideNo}`);
    if (target) {
        target.style.display = 'block';
    }

    currentSlide = slideNo;

    // Update Counter & Select
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${currentSlide} / ${totalSlides}`;

    const select = document.getElementById('slideSelect');
    if (select) select.value = currentSlide;

    // Prev / Next button states
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        prevBtn.style.opacity = (currentSlide === 1) ? '0.4' : '1';
    }

    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
    }
}

// Checkpoint Feedback
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const fb = document.getElementById(`cp-feedback-${cpId}`);
    if (!fb) return;

    if (selectedIdx === correctIdx) {
        fb.className = "p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-200 space-y-1";
        fb.innerHTML = `<div><strong>✓ Correct!</strong></div><div>${explanation}</div>`;
    } else {
        fb.className = "p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-xs text-rose-200 space-y-1";
        fb.innerHTML = `<div><strong>✗ Incorrect. Try reviewing the principle.</strong></div><div>${explanation}</div>`;
    }
    fb.classList.remove('hidden');
}

// Mastery Quiz Selection & Feedback
function selectQuizOption(qId, selectedIdx, correctIdx, title, question, explanation) {
    const fb = document.getElementById(`q-fb-${qId}`);
    const solBtn = document.getElementById(`q-sol-btn-${qId}`);
    if (!fb) return;

    if (selectedIdx === correctIdx) {
        fb.className = "p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-200 space-y-1";
        fb.innerHTML = `<div><strong>✓ Correct!</strong></div><div>${explanation}</div>`;
    } else {
        fb.className = "p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-xs text-rose-200 space-y-1";
        fb.innerHTML = `<div><strong>✗ Incorrect.</strong></div><div>${explanation}</div>`;
    }
    fb.classList.remove('hidden');

    if (solBtn) {
        solBtn.classList.remove('hidden');
        solBtn.classList.add('inline-flex');
    }
}

// Solution Modal Handlers
function openSolutionModal(title, question, solutionHtml) {
    const modal = document.getElementById('solutionModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalQuestion = document.getElementById('modalQuestion');
    const modalSolution = document.getElementById('modalSolution');

    if (modal && modalTitle && modalQuestion && modalSolution) {
        modalTitle.textContent = title;
        modalQuestion.innerHTML = question;
        modalSolution.innerHTML = solutionHtml;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    }
}

// ==================== 16 Bespoke Simulator Logic Handlers ====================

// Sim 1: Rain Window & Global Water Distribution
function inspectWaterFraction(fraction) {
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');
    const oceanBar = document.getElementById('sim1-ocean-bar');
    const freshBar = document.getElementById('sim1-fresh-bar');
    const drinkBar = document.getElementById('sim1-drink-bar');

    if (fraction === 'ocean') {
        if (badge) badge.textContent = "Focus: Oceans & Seas (~97%)";
        if (oceanBar) oceanBar.setAttribute('stroke-width', '3');
        if (freshBar) freshBar.setAttribute('stroke-width', '1');
        if (drinkBar) drinkBar.setAttribute('stroke-width', '1');
        if (desc) desc.innerHTML = "<strong>Saline Ocean Water:</strong> Covers most of the planet with dissolved mineral salts (35g/L). Drinking it causes dehydration and cannot be used for farming.";
    } else if (fraction === 'glacier') {
        if (badge) badge.textContent = "Focus: Frozen Glaciers (~2%)";
        if (oceanBar) oceanBar.setAttribute('stroke-width', '1');
        if (freshBar) freshBar.setAttribute('stroke-width', '3');
        if (drinkBar) drinkBar.setAttribute('stroke-width', '1');
        if (desc) desc.innerHTML = "<strong>Frozen Polar Caps & Glaciers:</strong> Accounts for over two-thirds of all freshwater, held in Antarctica, Greenland, and Himalayan peaks out of direct human reach.";
    } else if (fraction === 'usable') {
        if (badge) badge.textContent = "Focus: Accessible Freshwater (<1%)";
        if (oceanBar) oceanBar.setAttribute('stroke-width', '1');
        if (freshBar) freshBar.setAttribute('stroke-width', '1');
        if (drinkBar) drinkBar.setAttribute('stroke-width', '3');
        if (desc) desc.innerHTML = "<strong>Accessible Liquid Freshwater:</strong> Less than 1% of Earth's water is readily available in rivers, lakes, ponds, and shallow aquifers to support 8 billion humans and wildlife!";
    }
}

// Sim 2: Three States of Water
function setWaterState(state) {
    const badge = document.getElementById('sim2-badge');
    const ice = document.getElementById('sim2-ice');
    const liquid = document.getElementById('sim2-liquid');
    const steam = document.getElementById('sim2-steam');
    const flame = document.getElementById('sim2-flame');
    const mercury = document.getElementById('sim2-thermo-mercury');
    const tempLabel = document.getElementById('sim2-temp-label');
    const desc = document.getElementById('sim2-desc');

    if (state === 'solid') {
        if (ice) ice.style.display = 'block';
        if (liquid) liquid.style.display = 'none';
        if (steam) steam.style.display = 'none';
        if (flame) flame.setAttribute('opacity', '0');
        if (mercury) { mercury.setAttribute('y', '135'); mercury.setAttribute('height', '25'); }
        if (tempLabel) tempLabel.textContent = "-10°C";
        if (badge) badge.textContent = "State: Solid Ice (-10°C)";
        if (desc) desc.innerHTML = "<strong>Solid Ice:</strong> Below 0°C, water molecules lock into an orderly hexagonal lattice, holding a fixed rigid shape and definite volume.";
    } else if (state === 'liquid') {
        if (ice) ice.style.display = 'none';
        if (liquid) liquid.style.display = 'block';
        if (steam) steam.style.display = 'none';
        if (flame) flame.setAttribute('opacity', '0');
        if (mercury) { mercury.setAttribute('y', '95'); mercury.setAttribute('height', '65'); }
        if (tempLabel) tempLabel.textContent = "25°C";
        if (badge) badge.textContent = "State: Liquid Water (25°C)";
        if (desc) desc.innerHTML = "<strong>Liquid Water:</strong> Between 0°C and 100°C, water flows freely, taking the shape of its container while maintaining a definite volume.";
    } else if (state === 'gas') {
        if (ice) ice.style.display = 'none';
        if (liquid) liquid.style.display = 'none';
        if (steam) steam.style.display = 'block';
        if (flame) flame.setAttribute('opacity', '1');
        if (mercury) { mercury.setAttribute('y', '35'); mercury.setAttribute('height', '125'); }
        if (tempLabel) tempLabel.textContent = "100°C";
        if (badge) badge.textContent = "State: Gaseous Steam (100°C)";
        if (desc) desc.innerHTML = "<strong>Gaseous Steam / Vapour:</strong> At 100°C, thermal energy breaks intermolecular bonds completely. Molecules disperse rapidly to fill any available volume.";
    }
}

// Sim 3: State Shifters & Phase Transitions
function triggerTransition(action) {
    const badge = document.getElementById('sim3-badge');
    const infoText = document.getElementById('sim3-info-text');
    const desc = document.getElementById('sim3-desc');

    if (action === 'melt') {
        if (badge) badge.textContent = "Phase Shift: Melting (Solid ➔ Liquid)";
        if (infoText) infoText.textContent = "Ice absorbs latent heat of fusion at 0°C to melt into liquid water.";
        if (desc) desc.innerHTML = "<strong>Melting:</strong> Adding thermal energy causes rigid crystalline bonds in ice to break, allowing molecules to slide freely past each other.";
    } else if (action === 'evap') {
        if (badge) badge.textContent = "Phase Shift: Evaporation (Liquid ➔ Gas)";
        if (infoText) infoText.textContent = "Water absorbs heat, turning into high-energy gaseous water vapour.";
        if (desc) desc.innerHTML = "<strong>Evaporation:</strong> Thermal energy overcomes surface tension, launching water molecules into the air as invisible vapour.";
    } else if (action === 'cond') {
        if (badge) badge.textContent = "Phase Shift: Condensation (Gas ➔ Liquid)";
        if (infoText) infoText.textContent = "Cooling slows vapour molecules down, forming liquid droplets.";
        if (desc) desc.innerHTML = "<strong>Condensation:</strong> When warm vapour contacts cold air or a cool surface, it loses kinetic energy and clusters into liquid dew drops and clouds.";
    } else if (action === 'freeze') {
        if (badge) badge.textContent = "Phase Shift: Freezing (Liquid ➔ Solid)";
        if (infoText) infoText.textContent = "Removing heat below 0°C locks water molecules into solid ice crystals.";
        if (desc) desc.innerHTML = "<strong>Freezing / Solidification:</strong> Continued cooling removes kinetic agitation until molecules lock into an orderly hexagonal lattice.";
    }
}

// Sim 4: Steel Tumbler Condensation Experiment
function toggleIceGlass(mode) {
    const badge = document.getElementById('sim4-badge');
    const beads = document.getElementById('sim4-outer-beads');
    const desc = document.getElementById('sim4-desc');

    if (mode === 'ice') {
        if (beads) beads.style.display = 'block';
        if (badge) badge.textContent = "Contents: Chilled Ice Water (4°C)";
        if (desc) desc.innerHTML = "<strong>Condensation Proved:</strong> The cold metal exterior chills surrounding room air below its saturation dew point. Invisible vapour condenses into liquid beads on the outside.";
    } else {
        if (beads) beads.style.display = 'none';
        if (badge) badge.textContent = "Contents: Lukewarm Water (30°C)";
        if (desc) desc.innerHTML = "<strong>No Condensation:</strong> Because the metal surface is warm, adjacent room air is not cooled, so water vapour remains gaseous and no droplets form.";
    }
}

// Sim 5: Miniature Bag Sunbeam Water Cycle
function animateBagSolar(mode) {
    const badge = document.getElementById('sim5-badge');
    const vapour = document.getElementById('sim5-rising-vapour');
    const rain = document.getElementById('sim5-mini-rain');
    const desc = document.getElementById('sim5-desc');

    if (mode === 'evaporate') {
        if (vapour) vapour.style.opacity = '1';
        if (rain) rain.style.opacity = '0.3';
        if (badge) badge.textContent = "Solar Action: Vapour Rising ⬆";
        if (desc) desc.innerHTML = "<strong>Evaporation in Bag:</strong> Radiant sunlight heats water in the cup, causing water molecules to vaporize and rise into the closed humid air of the bag.";
    } else {
        if (vapour) vapour.style.opacity = '0.4';
        if (rain) rain.style.opacity = '1';
        if (badge) badge.textContent = "Gravity Action: Mini-Rain Trickling ⬇";
        if (desc) desc.innerHTML = "<strong>Condensation & Rain:</strong> Vapour touches the cooler upper bag wall, condenses into heavy liquid drops, and gravity pulls them downward as miniature rainfall!";
    }
}

// Sim 6: Grand Water Cycle
function highlightCycleStep(step) {
    const badge = document.getElementById('sim6-badge');
    const desc = document.getElementById('sim6-desc');

    if (step === 'evap') {
        if (badge) badge.textContent = "Stage 1: Evaporation & Transpiration";
        if (desc) desc.innerHTML = "<strong>Solar Lift:</strong> Heat from the Sun evaporates ocean water while plant leaves transpire moisture, lifting invisible water vapour into the sky.";
    } else if (step === 'cond') {
        if (badge) badge.textContent = "Stage 2: Condensation & Clouds";
        if (desc) desc.innerHTML = "<strong>Cloud Formation:</strong> Rising vapour cools at high altitudes and condenses around microscopic dust particles into vast white clouds.";
    } else if (step === 'precip') {
        if (badge) badge.textContent = "Stage 3: Precipitation (Rain/Snow)";
        if (desc) desc.innerHTML = "<strong>Precipitation:</strong> When cloud droplets merge and become too heavy to remain suspended in updrafts, gravity pulls them down as rain, snow, or hail.";
    } else if (step === 'runoff') {
        if (badge) badge.textContent = "Stage 4: Runoff & Aquifer Infiltration";
        if (desc) desc.innerHTML = "<strong>Return to Source:</strong> Rainwater flows through streams and rivers back to the sea, while a vital portion infiltrates soil to recharge groundwater.";
    }
}

// Sim 7: Earth's Sponge Infiltration
function simulateRainfallSeepage() {
    const badge = document.getElementById('sim7-badge');
    const wt = document.getElementById('sim7-water-table');
    const aquifer = document.getElementById('sim7-aquifer');
    const desc = document.getElementById('sim7-desc');

    if (wt) wt.setAttribute('y1', '85');
    if (wt) wt.setAttribute('y2', '85');
    if (aquifer) aquifer.setAttribute('opacity', '0.75');

    if (badge) badge.textContent = "Water Table: Rising with Infiltration";
    if (desc) desc.innerHTML = "<strong>Natural Groundwater Recharge:</strong> Rainwater percolates through porous soil and gravel filters, filling underground pore spaces and elevating the water table.";
}

function pumpAquiferWater() {
    const badge = document.getElementById('sim7-badge');
    const wt = document.getElementById('sim7-water-table');
    const aquifer = document.getElementById('sim7-aquifer');
    const desc = document.getElementById('sim7-desc');

    if (wt) wt.setAttribute('y1', '115');
    if (wt) wt.setAttribute('y2', '115');
    if (aquifer) aquifer.setAttribute('opacity', '0.3');

    if (badge) badge.textContent = "Water Table: Dropping from Over-Extraction";
    if (desc) desc.innerHTML = "<strong>Aquifer Depletion:</strong> Pumping water out faster than monsoon rainfall can recharge it causes the water table to drop, leaving shallow wells dry.";
}

// Sim 8: Dug Well vs Handpump
function operateWellBucket() {
    const bucket = document.getElementById('sim8-bucket');
    const badge = document.getElementById('sim8-badge');
    const desc = document.getElementById('sim8-desc');

    if (bucket) {
        bucket.setAttribute('y', '30');
        setTimeout(() => { bucket.setAttribute('y', '70'); }, 1200);
    }
    if (badge) badge.textContent = "Well: Pulley Raising Water Bucket";
    if (desc) desc.innerHTML = "<strong>Open Dug Well:</strong> A pulley (charkhi) redirects the downward pull of the rope, making it easy to hoist heavy buckets of clean water from the water table.";
}

function operateHandpump() {
    const lever = document.getElementById('sim8-lever');
    const stream = document.getElementById('sim8-pump-water');
    const badge = document.getElementById('sim8-badge');
    const desc = document.getElementById('sim8-desc');

    if (lever) {
        lever.setAttribute('y2', '20');
        setTimeout(() => { lever.setAttribute('y2', '5'); }, 600);
    }
    if (stream) {
        stream.setAttribute('opacity', '1');
        setTimeout(() => { stream.setAttribute('opacity', '0'); }, 1200);
    }

    if (badge) badge.textContent = "Handpump: Suction Cylinder Delivering Water";
    if (desc) desc.innerHTML = "<strong>Handpump Mechanics:</strong> The lever drives a piston rod inside a sealed casing pipe. Check valves hold water column pressure, pumping groundwater into the bucket.";
}

// Sim 9: Paved vs Green Recharge Comparison
function setSurfaceComparison(mode) {
    const badge = document.getElementById('sim9-badge');
    const desc = document.getElementById('sim9-desc');

    if (mode === 'paved') {
        if (badge) badge.textContent = "Mode: Paved Concrete City (Flooding)";
        if (desc) desc.innerHTML = "<strong>Impervious Concrete Seal:</strong> Asphalt roads and cemented pavements block infiltration. Rainwater turns into 90% surface runoff, causing urban flash floods while local aquifers dry up.";
    } else {
        if (badge) badge.textContent = "Mode: Natural Green Soil & Soak Pit (Recharge)";
        if (desc) desc.innerHTML = "<strong>Eco-Friendly Infiltration:</strong> Open soils, tree root networks, and gravel soak pits absorb rain, allowing up to 70% of precipitation to recharge deep groundwater.";
    }
}

// Sim 10: Surface Water Reservoirs
function selectSurfaceBody(body) {
    const badge = document.getElementById('sim10-badge');
    const desc = document.getElementById('sim10-desc');

    if (body === 'river') {
        if (badge) badge.textContent = "Selected: Perennial Himalayan River (Nadi)";
        if (desc) desc.innerHTML = "<strong>Perennial River:</strong> Snow and glacial meltwater from Himalayan ranges keep rivers like the Ganga flowing 365 days a year, transporting rich alluvial silt to farms.";
    } else if (body === 'lake') {
        if (badge) badge.textContent = "Selected: Natural Freshwater Lake (Jheel)";
        if (desc) desc.innerHTML = "<strong>Freshwater Lake:</strong> Deep natural depression storing millions of liters of pristine water, stabilizing regional microclimate and supporting fisheries.";
    } else if (body === 'pond') {
        if (badge) badge.textContent = "Selected: Village Community Pond (Talab)";
        if (desc) desc.innerHTML = "<strong>Village Pond:</strong> Traditional shallow catchment capturing seasonal monsoon runoff, crucial for livestock hydration and maintaining surrounding open wells.";
    }
}

// Sim 11: Activity 6 Crumpled Paper River Contours
function sprayMountainMist() {
    const spray = document.getElementById('sim11-spray');
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');

    if (spray) {
        spray.setAttribute('opacity', '1');
        setTimeout(() => { spray.setAttribute('opacity', '0.4'); }, 800);
    }
    if (badge) badge.textContent = "Mist Sprayed: Mountain Runoff Initiated";
    if (desc) desc.innerHTML = "<strong>Gravity Seeking Lowest Path:</strong> Water droplets coalesce on high ridges and immediately seek the lowest path downhill through creases, modeling natural stream formation.";
}

function washDownSeeds() {
    const seeds = document.getElementById('sim11-seeds');
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');

    if (seeds) {
        seeds.style.transition = 'transform 1s ease';
        seeds.setAttribute('transform', 'translate(-10, 15)');
    }
    if (badge) badge.textContent = "Sediment Transport: Silt Carried to Plains";
    if (desc) desc.innerHTML = "<strong>Sediment Deposition:</strong> Rushing water carries seeds down into valleys just as real rivers erode mountain minerals and deposit fertile alluvial silt onto agricultural plains.";
}

// Sim 12: Freshwater Pond Biodiversity Layers
function inspectPondZone(zone) {
    const badge = document.getElementById('sim12-badge');
    const desc = document.getElementById('sim12-desc');

    if (zone === 'surface') {
        if (badge) badge.textContent = "Zone: Pond Surface (Lotus & Strider)";
        if (desc) desc.innerHTML = "<strong>Surface Zone:</strong> Abundant sunlight allows floating lotus leaves and water hyacinths to photosynthesize, while water striders skim across the surface tension skin.";
    } else if (zone === 'midwater') {
        if (badge) badge.textContent = "Zone: Mid-Water Column (Fish & Hydrilla)";
        if (desc) desc.innerHTML = "<strong>Mid-Water Column:</strong> Fish swim among submerged oxygenating weeds (Hydrilla), extracting dissolved oxygen through crimson gills.";
    } else if (zone === 'shore') {
        if (badge) badge.textContent = "Zone: Shoreline & Shallows (Pond Heron)";
        if (desc) desc.innerHTML = "<strong>Shoreline Zone:</strong> Long-legged wading birds like the pond heron stalk shallow mud silently, spearing passing fish with sharp dagger beaks.";
    }
}

// Sim 13: Aquatic Plant Adaptations
function selectPlantSpecimen(specimen) {
    const badge = document.getElementById('sim13-badge');
    const lotus = document.getElementById('sim13-specimen-lotus');
    const hyacinth = document.getElementById('sim13-specimen-hyacinth');
    const desc = document.getElementById('sim13-desc');

    if (specimen === 'lotus') {
        if (lotus) lotus.style.display = 'block';
        if (hyacinth) hyacinth.style.display = 'none';
        if (badge) badge.textContent = "Specimen: Lotus Leaf (Waxy Coating)";
        if (desc) desc.innerHTML = "<strong>Lotus Effect:</strong> A superhydrophobic waxy coating prevents rotting by making water roll off in clean beads. Stomata are located only on the top surface facing the air.";
    } else {
        if (lotus) lotus.style.display = 'none';
        if (hyacinth) hyacinth.style.display = 'block';
        if (badge) badge.textContent = "Specimen: Hyacinth Petiole (Aerenchyma)";
        if (desc) desc.innerHTML = "<strong>Buoyant Aerenchyma:</strong> Swollen leaf petioles are packed with honeycomb air cavities that reduce plant density, functioning like natural life jackets to keep the plant afloat.";
    }
}

// Sim 14: Aquatic Animal Adaptations
function selectAnimalSpecimen(animal) {
    const badge = document.getElementById('sim14-badge');
    const fish = document.getElementById('sim14-art-fish');
    const scorpion = document.getElementById('sim14-art-scorpion');
    const desc = document.getElementById('sim14-desc');

    if (animal === 'fish') {
        if (fish) fish.style.display = 'block';
        if (scorpion) scorpion.style.display = 'none';
        if (badge) badge.textContent = "Animal: Streamlined Fish (Gills & Fins)";
        if (desc) desc.innerHTML = "<strong>Fish Hydrodynamics:</strong> Spindle-shaped body minimizes water drag; caudal fins propel forward, and crimson gills extract dissolved oxygen directly from water.";
    } else {
        if (fish) fish.style.display = 'none';
        if (scorpion) scorpion.style.display = 'block';
        if (badge) badge.textContent = "Animal: Water Scorpion Snorkel Tube";
        if (desc) desc.innerHTML = "<strong>Insect Snorkel Tube:</strong> The water scorpion lurks underwater among weeds, extending a long caudal breathing siphon to the surface to breathe atmospheric oxygen!";
    }
}

// Sim 15: River Food Chain
function simulatePollutionImpact(isPolluted) {
    const badge = document.getElementById('sim15-badge');
    const statusText = document.getElementById('sim15-chain-status');
    const desc = document.getElementById('sim15-desc');

    if (!isPolluted) {
        if (badge) {
            badge.textContent = "Ecosystem: Healthy Balance";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (statusText) {
            statusText.textContent = "Energy flows smoothly from solar-powered algae to apex herons.";
            statusText.setAttribute('fill', '#a7f3d0');
        }
        if (desc) desc.innerHTML = "<strong>Ecological Balance:</strong> Clean water allows microscopic algae to thrive on sunlight, nourishing insect larvae, which feed fish, which sustain apex herons.";
    } else {
        if (badge) {
            badge.textContent = "Ecosystem: Pollution Collapse";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (statusText) {
            statusText.textContent = "Toxic poisons destroy algae ➔ Entire food chain starves!";
            statusText.setAttribute('fill', '#fca5a5');
        }
        if (desc) desc.innerHTML = "<strong>Food Web Collapse:</strong> Chemical runoff kills algae and aquatic insects. Deprived of prey, fish perish, and water birds abandon the dead river.";
    }
}

// Sim 16: Drought Impact & Water Conservation Meter
function toggleConservationView(view) {
    const badge = document.getElementById('sim16-badge');
    const drought = document.getElementById('sim16-scene-drought');
    const wise = document.getElementById('sim16-scene-waterwise');
    const savings = document.getElementById('sim16-savings-text');
    const desc = document.getElementById('sim16-desc');

    if (view === 'wise') {
        if (drought) drought.style.display = 'none';
        if (wise) wise.style.display = 'block';
        if (badge) {
            badge.textContent = "Action: Water Guardian (Conserving)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (savings) savings.textContent = "Daily Conservation Savings: ~15 to 50 Liters per Household";
        if (desc) desc.innerHTML = "<strong>Water Stewardship:</strong> Simple actions—turning off taps while brushing, repairing leaks, and routing rooftop rainwater into soak pits—save thousands of liters every year.";
    } else {
        if (drought) drought.style.display = 'block';
        if (wise) wise.style.display = 'none';
        if (badge) {
            badge.textContent = "Warning: Drought Devastation (Sookha)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (savings) savings.textContent = "Zero Inflow: Aquifers Dried Up & Farmland Parched";
        if (desc) desc.innerHTML = "<strong>Drought Emergency:</strong> Consecutive monsoon failures deplete reservoirs, lower the water table, crack fertile topsoil, and trigger severe community famine.";
    }
}

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
    if ('speechSynthesis' in window) {
        selectedMaleVoice = getIndianMaleVoice();
    }
});
'''


"""
Interactive JavaScript module for NCERT Class 5 Science Chapter 2: Journey of a River
Features:
- Sentence-by-sentence Web Speech API with Indian Male voice priority (pitch: 0.88, rate: 0.95)
- Zero lecturer names
- Slide switcher with terminal slide notice ("You have reached the last slide of this chapter.")
- In-slide checkpoints (2 per slide on slides 1-16)
- 40 Mastery Challenge questions with solution modal
- 16 interactive SVG/HTML simulators
Zero raw LaTeX. Pure clean Unicode.
"""

JS_CODE = '''
// Science Chapter 2 Interactive JavaScript
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
        startLectureSpeech(textElem.textContent.trim(), currentSlide);
    }
}

function updateAllAudioButtons() {
    for (let i = 1; i <= 16; i++) {
        const btn = document.getElementById(`slide-audio-btn-${i}`);
        const badge = document.getElementById(`slide-audio-badge-${i}`);
        if (btn) {
            if (isSpeaking && currentSpeakingSlide === i) {
                btn.innerHTML = '<span>⏸</span><span>Pause Lecture</span>';
                btn.className = 'px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm';
                if (badge) {
                    badge.textContent = 'Speaking...';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30 animate-pulse';
                }
            } else {
                btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
                btn.className = 'px-3 py-1.5 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 text-xs font-bold flex items-center space-x-1.5 border border-indigo-500/30 transition shadow-sm';
                if (badge) {
                    badge.textContent = 'Audio Lecture Ready';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
                }
            }
        }
    }

    const globalBtn = document.getElementById('globalSpeechBtn');
    if (globalBtn) {
        if (isSpeaking) {
            globalBtn.innerHTML = '<span>⏸</span><span>Pause Lecture</span>';
            globalBtn.className = 'px-3 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm';
        } else {
            globalBtn.innerHTML = '<span>▶</span><span>Play Slide Audio</span>';
            globalBtn.className = 'px-3 py-2 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 text-xs font-bold flex items-center space-x-1.5 border border-indigo-500/30 transition shadow-sm';
        }
    }
}

// Slide Navigation
function showSlide(n) {
    if (n < 1 || n > totalSlides) return;
    stopSpeech();

    for (let i = 1; i <= totalSlides; i++) {
        const slide = document.getElementById(`slide-${i}`);
        if (slide) {
            slide.style.display = (i === n) ? 'block' : 'none';
        }
    }

    currentSlide = n;

    // Update Jump Select
    const jumpSelect = document.getElementById('slideJumpSelect');
    if (jumpSelect) jumpSelect.value = n;

    // Update Header Counter
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${n} / ${totalSlides}`;

    // Update Progress Bar
    const progressBar = document.getElementById('slideProgressBar');
    if (progressBar) {
        const pct = ((n - 1) / (totalSlides - 1)) * 100;
        progressBar.style.width = `${pct}%`;
    }

    // Previous Button state
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.disabled = (n === 1);
        if (n === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }

    // Next Button & Terminal Slide Notice
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (n === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.classList.add('hidden');
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

function goToSlide(n) {
    showSlide(parseInt(n, 10));
}

// Formative Checkpoint Handler
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const fb = document.getElementById(`cp-feedback-${cpId}`);
    if (!fb) return;

    fb.classList.remove('hidden');
    if (selectedIdx === correctIdx) {
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 text-xs flex items-start space-x-2">
                <span class="text-base font-bold shrink-0">✓</span>
                <div>
                    <strong class="font-bold">Correct!</strong> ${explanation}
                </div>
            </div>
        `;
    } else {
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-rose-300 text-xs flex items-start space-x-2">
                <span class="text-base font-bold shrink-0">✕</span>
                <div>
                    <strong class="font-bold">Incorrect.</strong> ${explanation}
                </div>
            </div>
        `;
    }
}

// Mastery Quiz Option Handler
function selectQuizOption(qId, selectedIdx, answerIdx, title, question, explanation) {
    const card = document.getElementById(`q-card-${qId}`);
    const fb = document.getElementById(`q-fb-${qId}`);
    const solBtn = document.getElementById(`q-sol-btn-${qId}`);
    if (!card || !fb) return;

    const optButtons = card.querySelectorAll('.quiz-opt-btn');
    optButtons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === answerIdx) {
            btn.classList.remove('bg-slate-900', 'hover:bg-slate-800', 'border-slate-800');
            btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx && selectedIdx !== answerIdx) {
            btn.classList.remove('bg-slate-900', 'hover:bg-slate-800', 'border-slate-800');
            btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200');
        } else {
            btn.classList.add('opacity-50');
        }
    });

    fb.classList.remove('hidden');
    if (selectedIdx === answerIdx) {
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-emerald-950/50 border border-emerald-500/30 text-emerald-300 text-xs flex items-start space-x-2">
                <span class="font-bold text-sm shrink-0">✓ Correct!</span>
                <span>${explanation}</span>
            </div>
        `;
    } else {
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-rose-950/50 border border-rose-500/30 text-rose-300 text-xs flex items-start space-x-2">
                <span class="font-bold text-sm shrink-0">✕ Incorrect.</span>
                <span>${explanation}</span>
            </div>
        `;
    }

    if (solBtn) {
        solBtn.classList.remove('hidden');
        solBtn.classList.add('inline-flex');
    }
}

// Solution Modal
function openSolutionModal(title, question, solutionHtml) {
    const modal = document.getElementById('solutionModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalQuestion = document.getElementById('modalQuestion');
    const modalBody = document.getElementById('modalBody');

    if (modal && modalTitle && modalQuestion && modalBody) {
        modalTitle.textContent = title;
        modalQuestion.innerHTML = `<strong>Question:</strong> ${question}`;
        modalBody.innerHTML = solutionHtml;
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }
}

// ==========================================
// 16 Bespoke Interactive Simulator Handlers
// ==========================================

// Sim 1: Godavari River Source & Course
function navigateGodavariCourse(stage) {
    const boat = document.getElementById('sim1-boat');
    const badge = document.getElementById('sim1-badge');
    const distText = document.getElementById('sim1-distance-text');
    const desc = document.getElementById('sim1-desc');

    if (stage === 'source') {
        if (boat) boat.setAttribute('transform', 'translate(50, 70)');
        if (badge) {
            badge.textContent = 'Brahmagiri Origin (0 km)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
        }
        if (distText) distText.textContent = '0 km (Source)';
        if (desc) desc.textContent = 'Brahmagiri Hills at Trimbakeshwar in the Western Ghats (Maharashtra). Pure, bubbling freshwater springs emerging at ~1,000 m elevation.';
    } else {
        if (boat) boat.setAttribute('transform', 'translate(320, 140)');
        if (badge) {
            badge.textContent = 'Bay of Bengal Mouth (1,465 km)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (distText) distText.textContent = '1,465 km (Mouth)';
        if (desc) desc.textContent = 'After journeying 1,465 km across Maharashtra, Telangana, and Andhra Pradesh, the mighty Godavari splits into delta distributaries and empties into the Bay of Bengal.';
    }
}

// Sim 2: Tributaries & Sangam Confluence
let activeTributaries = { manjira: true, indravati: false, sabari: false };
function toggleTributary(trib) {
    activeTributaries[trib] = !activeTributaries[trib];
    const elem = document.getElementById(`sim2-trib-${trib}`);
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (elem) {
        elem.setAttribute('opacity', activeTributaries[trib] ? '1' : '0.2');
        elem.setAttribute('stroke-width', activeTributaries[trib] ? '4' : '2');
    }

    const count = Object.values(activeTributaries).filter(Boolean).length;
    if (badge) {
        badge.textContent = `${count} Tributaries Flowing`;
        badge.className = count > 1 ? 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : 'px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
    }

    if (trib === 'manjira') {
        if (desc) desc.textContent = activeTributaries.manjira ? 'Manjira River (Right Bank, 724 km) actively pours water from Maharashtra and Karnataka into the main Godavari trunk.' : 'Manjira tributary flow throttled.';
    } else if (trib === 'indravati') {
        if (desc) desc.textContent = activeTributaries.indravati ? 'Indravati River (Left Bank, 535 km) joins through dense Bastar forests with immense volume, dramatically swelling the main river.' : 'Indravati tributary flow throttled.';
    } else if (trib === 'sabari') {
        if (desc) desc.textContent = activeTributaries.sabari ? 'Sabari River (Left Bank, 418 km) merges near Kunavaram, draining the southern slopes of the Eastern Ghats.' : 'Sabari tributary flow throttled.';
    }
}

// Sim 3: Perennial vs Seasonal River Flow
function setRiverSeason(season) {
    const badge = document.getElementById('sim3-badge');
    const perWater = document.getElementById('sim3-perennial-water');
    const seaBed = document.getElementById('sim3-seasonal-bed');
    const seaStatus = document.getElementById('sim3-seasonal-status');
    const desc = document.getElementById('sim3-desc');

    if (season === 'summer') {
        if (badge) {
            badge.textContent = 'Summer Season (May)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (perWater) perWater.setAttribute('opacity', '0.75');
        if (seaBed) seaBed.setAttribute('opacity', '0.9');
        if (seaStatus) seaStatus.textContent = 'Status: Dry Cracked Sandbed';
        if (desc) desc.textContent = 'In peak summer, perennial rivers like the Godavari maintain baseflow fed by deep groundwater and Western Ghat springs, while seasonal streams dry up completely.';
    } else {
        if (badge) {
            badge.textContent = 'Monsoon Season (August)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (perWater) perWater.setAttribute('opacity', '1');
        if (seaBed) seaBed.setAttribute('opacity', '0.1');
        if (seaStatus) seaStatus.textContent = 'Status: Rushing Full Torrent';
        if (desc) desc.textContent = 'During the southwest monsoon, torrential rains swell both perennial rivers and seasonal channels into surging, muddy highways carrying rich sediments.';
    }
}

// Sim 4: Riparian Wildlife & Forest Corridor
function selectRiverCreature(species) {
    const badge = document.getElementById('sim4-badge');
    const desc = document.getElementById('sim4-desc');

    const speciesData = {
        tiger: {
            name: 'Royal Bengal Tiger',
            badgeClass: 'bg-orange-500/20 text-orange-300 border-orange-500/30',
            info: 'Apex predator prowling the moist deciduous and bamboo riverine forests along the Godavari basin, hunting barking deer and wild boar.'
        },
        deer: {
            name: 'Barking Deer (Muntjac)',
            badgeClass: 'bg-amber-500/20 text-amber-300 border-amber-500/30',
            info: 'Small, solitary herbivore grazing on riverbank foliage; emits loud barking alarm calls when predators like tigers or leopards approach.'
        },
        gecko: {
            name: 'Indian Golden Gecko',
            badgeClass: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30',
            info: 'Rare, endemic golden-hued reptile clinging to rocky granite boulders, ravines, and cavernous cliffs flanking the Eastern Ghats river gorge.'
        },
        sandalwood: {
            name: 'Red Sandalwood (Pterocarpus santalinus)',
            badgeClass: 'bg-rose-500/20 text-rose-300 border-rose-500/30',
            info: 'Highly prized medicinal and aromatic tree endemic to the dry hilly terrain and rocky river valleys of the Eastern Ghats.'
        }
    };

    const item = speciesData[species] || speciesData.tiger;
    if (badge) {
        badge.textContent = item.name;
        badge.className = `px-2 py-0.5 rounded text-[10px] font-bold ${item.badgeClass} border`;
    }
    if (desc) desc.textContent = item.info;
}

// Sim 5: Coringa Mangrove Estuary & Tidal Roots
function setMangroveTide(tide) {
    const badge = document.getElementById('sim5-badge');
    const roots = document.getElementById('sim5-pneumatophores');
    const water = document.getElementById('sim5-tide-water');
    const desc = document.getElementById('sim5-desc');

    if (tide === 'low') {
        if (badge) {
            badge.textContent = 'Low Tide (Roots Exposed)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30';
        }
        if (water) {
            water.setAttribute('y', '160');
            water.setAttribute('height', '50');
            water.setAttribute('opacity', '0.5');
        }
        if (roots) roots.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'At low tide, salty seawater recedes, revealing thousands of pencil-like vertical breathing roots (pneumatophores) that absorb atmospheric oxygen in waterlogged mud.';
    } else {
        if (badge) {
            badge.textContent = 'High Tide (Delta Inundated)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (water) {
            water.setAttribute('y', '90');
            water.setAttribute('height', '120');
            water.setAttribute('opacity', '0.85');
        }
        if (roots) roots.setAttribute('opacity', '0.4');
        if (desc) desc.textContent = 'At high tide, brackish tides flood the estuary. The dense network of stilt roots acts as a natural shock-absorber against cyclones, storm surges, and coastal erosion.';
    }
}

// Sim 6: Civilization Lifeline (Multi-Sector Use)
function selectWaterService(svc) {
    const badge = document.getElementById('sim6-badge');
    const desc = document.getElementById('sim6-desc');

    const svcData = {
        domestic: {
            name: 'Domestic: Drinking & Towns',
            badgeClass: 'bg-sky-500/20 text-sky-300 border-sky-500/30',
            info: 'Godavari supplies tap drinking water, cooking, and sanitation needs to over 70 million residents across Nashik, Nanded, Nizamabad, and Rajahmundry.'
        },
        farming: {
            name: 'Farming: Irrigation Canals',
            badgeClass: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30',
            info: 'Network of canal barrages irrigates over 2.6 million hectares of fertile paddy, sugarcane, cotton, and oilseed fields in the delta.'
        },
        industry: {
            name: 'Industry: Power & Factories',
            badgeClass: 'bg-amber-500/20 text-amber-300 border-amber-500/30',
            info: 'Thermal power cooling, textile mills, paper plants, and food processing facilities draw industrial process water from the river.'
        }
    };

    const item = svcData[svc] || svcData.domestic;
    if (badge) {
        badge.textContent = item.name;
        badge.className = `px-2 py-0.5 rounded text-[10px] font-bold ${item.badgeClass} border`;
    }
    if (desc) desc.textContent = item.info;
}

// Sim 7: Livelihoods & Ecotourism at Papi Hills
function setLivelihoodMode(mode) {
    const badge = document.getElementById('sim7-badge');
    const ecoBoat = document.getElementById('sim7-eco-boat');
    const fishBoat = document.getElementById('sim7-fish-boat');
    const desc = document.getElementById('sim7-desc');

    if (mode === 'tour') {
        if (badge) {
            badge.textContent = 'Ecotourism (Papi Hills Gorge)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (ecoBoat) ecoBoat.setAttribute('opacity', '1');
        if (fishBoat) fishBoat.setAttribute('opacity', '0.3');
        if (desc) desc.textContent = 'Tourists enjoy scenic river cruises between majestic forested hilltops. Responsible ecotourism provides local livelihood while enforcing zero-plastic and zero-pollution rules.';
    } else {
        if (badge) {
            badge.textContent = 'Artisanal River Fishery';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (ecoBoat) ecoBoat.setAttribute('opacity', '0.3');
        if (fishBoat) fishBoat.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Traditional fishermen cast hand-woven nets at dawn, harvesting freshwater carp, catfish, and migrating hilsa to support their families and coastal fish markets.';
    }
}

// Sim 8: Hydroelectric Dam & Reservoirs
let turbinesSpinning = true;
function toggleDamTurbines(generate) {
    turbinesSpinning = generate;
    const badge = document.getElementById('sim8-badge');
    const turbine = document.getElementById('sim8-turbine');
    const desc = document.getElementById('sim8-desc');

    if (generate) {
        if (badge) {
            badge.textContent = 'Hydroelectricity: Generating';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (turbine) turbine.classList.add('animate-spin');
        if (desc) desc.textContent = 'Water drops through penstocks under high hydrostatic pressure, spinning turbine generator blades to create clean electricity before exiting into downstream canals.';
    } else {
        if (badge) {
            badge.textContent = 'Turbines Idled / Sluice Closed';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30';
        }
        if (turbine) turbine.classList.remove('animate-spin');
        if (desc) desc.textContent = 'Sluice gates shut; stored water conserved in reservoir for critical dry-season agricultural irrigation and city tap water reserves.';
    }
}

// Sim 9: Dam Trade-Offs & Submergence
function setReservoirLevel(level) {
    const badge = document.getElementById('sim9-badge');
    const water = document.getElementById('sim9-reservoir-water');
    const forest = document.getElementById('sim9-forest');
    const village = document.getElementById('sim9-village');
    const desc = document.getElementById('sim9-desc');

    if (level === 'high') {
        if (badge) {
            badge.textContent = 'Full Reservoir: Upstream Submergence';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (water) {
            water.setAttribute('y', '50');
            water.setAttribute('height', '130');
            water.setAttribute('fill', '#0284c7');
        }
        if (forest) forest.setAttribute('opacity', '0.25');
        if (village) village.setAttribute('opacity', '0.2');
        if (desc) desc.textContent = 'High dam impoundment provides massive water security and electricity, but drowns thousands of hectares of biodiversity-rich forests and displaces tribal communities.';
    } else {
        if (badge) {
            badge.textContent = 'Natural River Valley / Low Storage';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (water) {
            water.setAttribute('y', '120');
            water.setAttribute('height', '60');
            water.setAttribute('fill', '#0ea5e9');
        }
        if (forest) forest.setAttribute('opacity', '1');
        if (village) village.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Natural valley preserved with ancient forests and intact riverside villages, but without storage there is little flood buffer or summer irrigation security.';
    }
}

// Sim 10: River Pollution & Sewage Cleanup
function cleanseRiver(clean) {
    const badge = document.getElementById('sim10-badge');
    const water = document.getElementById('sim10-water');
    const statusText = document.getElementById('sim10-water-status');
    const trash = document.getElementById('sim10-plastic-trash');
    const desc = document.getElementById('sim10-desc');

    if (clean) {
        if (badge) {
            badge.textContent = 'STP Operating: Pure River';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (water) water.setAttribute('fill', '#0284c7');
        if (statusText) statusText.textContent = 'Water: Treated & Oxygen-Rich (Safe)';
        if (trash) trash.style.display = 'none';
        if (desc) desc.textContent = 'Operating Sewage Treatment Plants (STPs) and enforcing zero industrial discharge keeps the river healthy, transparent, and hospitable for aquatic life.';
    } else {
        if (badge) {
            badge.textContent = 'Raw Untreated Sewage & Trash';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (water) water.setAttribute('fill', '#713f12');
        if (statusText) statusText.textContent = 'Water: Murky, Anoxic & Contaminated';
        if (trash) trash.style.display = 'inline';
        if (desc) desc.textContent = 'Dumping untreated city drains, chemical effluents, and plastic garbage severely depletes dissolved oxygen and turns sparkling river waters foul and toxic.';
    }
}

// Sim 11: Fertilizer Runoff & Algal Bloom
function toggleEutrophication(bloom) {
    const badge = document.getElementById('sim11-badge');
    const greenMat = document.getElementById('sim11-green-mat');
    const deadFish = document.getElementById('sim11-dead-fish');
    const desc = document.getElementById('sim11-desc');

    if (bloom) {
        if (badge) {
            badge.textContent = 'Green Blanket: Eutrophication';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (greenMat) greenMat.setAttribute('opacity', '0.9');
        if (deadFish) deadFish.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Excess synthetic chemical fertilizers wash into rivers. Algae reproduce uncontrollably forming a thick green blanket, cutting off sunlight and suffocating fish.';
    } else {
        if (badge) {
            badge.textContent = 'Balanced Nutrient Stream';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (greenMat) greenMat.setAttribute('opacity', '0.05');
        if (deadFish) deadFish.setAttribute('opacity', '0.05');
        if (desc) desc.textContent = 'Natural riparian buffer plants filter out runoff; sunlight penetrates deep water, supporting balanced aquatic vegetation and healthy swimming fish.';
    }
}

// Sim 12: Monsoon River Flood Dynamics
function triggerFloodStage(stage) {
    const badge = document.getElementById('sim12-badge');
    const floodWater = document.getElementById('sim12-flood-water');
    const floodLabel = document.getElementById('sim12-flood-label');
    const desc = document.getElementById('sim12-desc');

    if (stage === 'normal') {
        if (badge) {
            badge.textContent = 'Normal River Flow';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (floodWater) {
            floodWater.setAttribute('y', '140');
            floodWater.setAttribute('height', '50');
            floodWater.setAttribute('fill', '#0284c7');
        }
        if (floodLabel) floodLabel.textContent = 'Water safely contained within banks';
        if (desc) desc.textContent = 'The natural river channel easily accommodates everyday discharge. Floodplain farms remain dry and safe.';
    } else {
        if (badge) {
            badge.textContent = 'Cloudburst: Flood Inundation';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (floodWater) {
            floodWater.setAttribute('y', '60');
            floodWater.setAttribute('height', '130');
            floodWater.setAttribute('fill', '#991b1b');
        }
        if (floodLabel) floodLabel.textContent = 'Deluge overtopping natural riverbanks!';
        if (desc) desc.textContent = 'Intense monsoon downpours exceed channel capacity; floodwaters burst over embankments, submerging floodplains, low-lying homes, and standing crops.';
    }
}

// Sim 13: Forest Shield vs Deforested Runoff
function compareCatchment(type) {
    const badge = document.getElementById('sim13-badge');
    const trees = document.getElementById('sim13-forest-trees');
    const desc = document.getElementById('sim13-desc');

    if (type === 'forest') {
        if (badge) {
            badge.textContent = 'Forested Catchment (Natural Shield)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (trees) trees.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Dense tree canopies intercept falling raindrops while deep root systems anchor topsoil, absorbing rainwater like a gigantic sponge and recharging aquifers.';
    } else {
        if (badge) {
            badge.textContent = 'Deforested Catchment (Muddy Flash Flood)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (trees) trees.setAttribute('opacity', '0.15');
        if (desc) desc.textContent = 'Without tree cover, rain hammers bare hillsides. Water rushes instantly into riverbeds as sudden muddy flash floods, stripping valuable topsoil and silting reservoirs.';
    }
}

// Sim 14: Flood Safety Protocol Station
function setFloodSafetyPhase(phase) {
    const badge = document.getElementById('sim14-badge');
    const title = document.getElementById('sim14-step-title');
    const p1 = document.getElementById('sim14-step-p1');
    const p2 = document.getElementById('sim14-step-p2');
    const p3 = document.getElementById('sim14-step-p3');
    const desc = document.getElementById('sim14-desc');

    if (phase === 'before') {
        if (badge) {
            badge.textContent = 'Phase 1: Before Flood Warning';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (title) title.textContent = 'Preparation & Early Warnings';
        if (p1) p1.textContent = '1. Monitor radio, TV, and meteorological flood alerts.';
        if (p2) p2.textContent = '2. Assemble emergency kit (torch, dry rations, medicines, clean water).';
        if (p3) p3.textContent = '3. Identify designated highland evacuation shelters.';
        if (desc) desc.textContent = 'Advance preparedness saves lives. Keep battery-powered radios and essential documents in waterproof containers before waters rise.';
    } else if (phase === 'during') {
        if (badge) {
            badge.textContent = 'Phase 2: During Flood Deluge';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (title) title.textContent = 'Immediate Survival & Safe Evacuation';
        if (p1) p1.textContent = '1. Turn off main power switches and gas cylinders immediately.';
        if (p2) p2.textContent = '2. Move to higher floors or designated relief centers.';
        if (p3) p3.textContent = '3. Never walk, swim, or drive through moving floodwaters.';
        if (desc) desc.textContent = 'Just 15 cm of moving floodwater can knock an adult down, and 60 cm can carry away a car. Avoid swollen streams and stay away from snapped electric cables.';
    } else {
        if (badge) {
            badge.textContent = 'Phase 3: After Waters Recede';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (title) title.textContent = 'Recovery, Sanitation & Disease Prevention';
        if (p1) p1.textContent = '1. Return home only after official safety clearance is declared.';
        if (p2) p2.textContent = '2. Drink strictly boiled or chlorine-disinfected water.';
        if (p3) p3.textContent = '3. Clean sludge and disinfect surroundings to prevent cholera and malaria.';
        if (desc) desc.textContent = 'Post-flood contamination poses severe waterborne epidemic risks. Always boil drinking water vigorously and clear debris carefully.';
    }
}

// Sim 15: Chennai 2019 Day Zero: Jaldoot Water Train
function dispatchWaterTrain() {
    const badge = document.getElementById('sim15-badge');
    const train = document.getElementById('sim15-water-train');
    const status = document.getElementById('sim15-train-status');
    const desc = document.getElementById('sim15-desc');

    if (badge) {
        badge.textContent = 'Jaldoot Express Dispatched';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
    }
    if (train) {
        train.setAttribute('transform', 'translate(100, 110)');
    }
    if (status) status.textContent = 'Delivering 2.5 Million Liters from Jolarpettai (216 km)';
    if (desc) desc.textContent = 'In July 2019, Indian Railways deployed special 50-wagon "Jaldoot" water trains, transporting 2.5 million liters per trip across 216 km to rescue parched Chennai.';
}

function inspectDayZero() {
    const badge = document.getElementById('sim15-badge');
    const status = document.getElementById('sim15-train-status');
    const desc = document.getElementById('sim15-desc');

    if (badge) {
        badge.textContent = 'Chennai Day Zero: Reservoirs Dry';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
    }
    if (status) status.textContent = 'All 4 Reservoirs Dried to 1% Storage Capacity';
    if (desc) desc.textContent = 'Chembarambakkam, Poondi, Red Hills, and Sholavaram reservoirs dried up due to consecutive failed monsoons and unmanaged groundwater extraction.';
}

// Sim 16: Automated Water ATM & Conservation Meter
function operateWaterATM() {
    const badge = document.getElementById('sim16-badge');
    const screen = document.getElementById('sim16-atm-screen');
    const stream = document.getElementById('sim16-atm-stream');
    const desc = document.getElementById('sim16-desc');

    if (badge) {
        badge.textContent = 'Water ATM: Dispensing 20 Liters';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
    }
    if (screen) screen.textContent = 'Dispensing 20L...';
    if (stream) stream.setAttribute('opacity', '1');
    if (desc) desc.textContent = 'Card/coin-operated Water ATMs dispense clean, RO-purified drinking water in water-stressed villages at just 30 paise per liter, eliminating disease and middleman extortion.';
}

function calculatePledgeSavings() {
    const badge = document.getElementById('sim16-badge');
    const screen = document.getElementById('sim16-atm-screen');
    const stream = document.getElementById('sim16-atm-stream');
    const desc = document.getElementById('sim16-desc');

    if (badge) {
        badge.textContent = 'Daily Water Savings Pledge';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (screen) screen.textContent = 'Saved: 80 L/Day!';
    if (stream) stream.setAttribute('opacity', '0');
    if (desc) desc.textContent = 'Simple actions yield huge results: Turn off tap while brushing (-10 L) + Bucket bath over shower (-40 L) + Prompt leak repairs (-30 L) = 80 Liters fresh water saved every day!';
}

// Keyboard Navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        prevSlide();
    } else if (e.key === 'Escape') {
        closeSolutionModal();
    }
});

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
});
'''


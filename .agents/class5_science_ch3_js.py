"""
Interactive JavaScript module for NCERT Class 5 Science Chapter 3: The Mystery of Food
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
// Science Chapter 3 Interactive JavaScript
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
                btn.className = 'px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm';
                if (badge) {
                    badge.textContent = 'Audio Lecture Ready';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30';
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
            globalBtn.className = 'px-3 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm';
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

// Sim 1: Tiffin Box Inspection
function setTiffinState(state) {
    const badge = document.getElementById('sim1-badge');
    const mold = document.getElementById('sim1-mold');
    const freshGarnish = document.getElementById('sim1-fresh-garnish');
    const food = document.getElementById('sim1-food');
    const desc = document.getElementById('sim1-desc');

    if (state === 'spoiled') {
        if (badge) {
            badge.textContent = '3 Days Later: Spoiled';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (food) food.setAttribute('fill', '#78350f');
        if (mold) mold.setAttribute('opacity', '1');
        if (freshGarnish) freshGarnish.setAttribute('opacity', '0');
        if (desc) desc.textContent = 'Foul sour odor escapes as the forgotten box opens. The uttapam is covered with fuzzy greenish mold colonies and black spore patches.';
    } else {
        if (badge) {
            badge.textContent = 'Freshly Steamed Uttapam';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (food) food.setAttribute('fill', '#d97706');
        if (mold) mold.setAttribute('opacity', '0');
        if (freshGarnish) freshGarnish.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Freshly cooked uttapam smells savory and fragrant with tomatoes and coriander. No molds or bacteria have settled yet!';
    }
}

// Sim 2: Microscope Magnification Lens
function setMicroscopeZoom(level) {
    const badge = document.getElementById('sim2-badge');
    const v1 = document.getElementById('sim2-view-1x');
    const v100 = document.getElementById('sim2-view-100x');
    const v1000 = document.getElementById('sim2-view-1000x');
    const desc = document.getElementById('sim2-desc');

    if (level === '1x') {
        if (badge) {
            badge.textContent = 'Zoom: 1x (Naked Eye)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-500/20 text-slate-300 border border-slate-500/30';
        }
        if (v1) v1.setAttribute('opacity', '1');
        if (v100) v100.setAttribute('opacity', '0');
        if (v1000) v1000.setAttribute('opacity', '0');
        if (desc) desc.textContent = 'To the naked eye, mold appears only as fuzzy greenish-black velvety patches on the surface of bread or uttapam.';
    } else if (level === '100x') {
        if (badge) {
            badge.textContent = 'Zoom: 100x (Fungal Hyphae)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30';
        }
        if (v1) v1.setAttribute('opacity', '0');
        if (v100) v100.setAttribute('opacity', '1');
        if (v1000) v1000.setAttribute('opacity', '0');
        if (desc) desc.textContent = 'Under 100x magnification, the fuzz reveals a dense branching network of microscopic living fungal threads called hyphae.';
    } else {
        if (badge) {
            badge.textContent = 'Zoom: 1,000x (Sporangium & Spores)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (v1) v1.setAttribute('opacity', '0');
        if (v100) v100.setAttribute('opacity', '0');
        if (v1000) v1000.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'At 1,000x high power, round spore heads (sporangia) burst open, releasing thousands of buoyant microscopic spores into the air!';
    }
}

// Sim 3: Microbial Habitat Explorer
function selectHabitat(habitat) {
    const badge = document.getElementById('sim3-badge');
    const desc = document.getElementById('sim3-desc');

    const habitatData = {
        air: {
            title: 'Habitat: Open Air',
            badgeClass: 'bg-sky-500/20 text-sky-300 border-sky-500/30',
            text: 'Air contains millions of microscopic airborne mold spores and bacterial cells riding on the gentlest breeze, ready to land on open food.'
        },
        soil: {
            title: 'Habitat: Fertile Soil',
            badgeClass: 'bg-amber-500/20 text-amber-300 border-amber-500/30',
            text: 'A single gram of garden soil houses billions of bacteria and fungal hyphae that decompose organic leaf litter and recycle soil minerals.'
        },
        water: {
            title: 'Habitat: Fresh Water',
            badgeClass: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/30',
            text: 'Natural freshwater bodies contain aquatic bacteria and microscopic algae forming the primary energy base of freshwater food chains.'
        },
        gut: {
            title: 'Habitat: Human Gut',
            badgeClass: 'bg-indigo-500/20 text-indigo-300 border-indigo-500/30',
            text: 'Finding #1: Over 100 trillion beneficial symbiotic bacteria live inside our intestines, digesting fibers, producing Vitamin K, and training immunity!'
        }
    };

    const item = habitatData[habitat] || habitatData.gut;
    if (badge) {
        badge.textContent = item.title;
        badge.className = `px-2 py-0.5 rounded text-[10px] font-bold ${item.badgeClass} border`;
    }
    if (desc) desc.textContent = item.text;
}

// Sim 4: Microbial Growth Triad Simulator
let growthTriad = { moisture: true, temp: true, air: true };
function toggleGrowthFactor(factor) {
    growthTriad[factor] = !growthTriad[factor];
    const badge = document.getElementById('sim4-badge');
    const colonies = document.getElementById('sim4-colonies');
    const mText = document.getElementById('sim4-moist-text');
    const tText = document.getElementById('sim4-temp-text');
    const aText = document.getElementById('sim4-air-text');
    const desc = document.getElementById('sim4-desc');

    if (mText) mText.textContent = `Moist: ${growthTriad.moisture ? 'YES' : 'DRY'}`;
    if (tText) tText.textContent = `Warm: ${growthTriad.temp ? '30°C' : '4°C'}`;
    if (aText) aText.textContent = `Air: ${growthTriad.air ? 'YES' : 'SEALED'}`;

    const count = Object.values(growthTriad).filter(Boolean).length;
    if (count === 3) {
        if (badge) {
            badge.textContent = 'Growth: Rapid Multiplication';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (colonies) colonies.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'All three essentials (Moisture + Warmth + Air) are present! Bacteria double every 20 minutes, rapidly spoiling food.';
    } else if (count === 2) {
        if (badge) {
            badge.textContent = 'Growth: Severely Retarded';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (colonies) colonies.setAttribute('opacity', '0.4');
        if (desc) desc.textContent = 'One essential factor removed! Microbial reproduction is drastically suppressed, slowing spoilage down.';
    } else {
        if (badge) {
            badge.textContent = 'Growth: Completely Halted';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (colonies) colonies.setAttribute('opacity', '0.05');
        if (desc) desc.textContent = 'Finding #2: When moisture, warmth, or air are eliminated, microbes cannot reproduce at all! Food remains preserved.';
    }
}

// Sim 5: Solar Dehydration Yard
function setDryingDay(day) {
    const badge = document.getElementById('sim5-badge');
    const c1 = document.getElementById('chilli-1');
    const c2 = document.getElementById('chilli-2');
    const c3 = document.getElementById('chilli-3');
    const vapor = document.getElementById('sim5-vapor');
    const pct = document.getElementById('sim5-moist-pct');
    const desc = document.getElementById('sim5-desc');

    if (day === 1) {
        if (badge) {
            badge.textContent = 'Day 1: 85% Moisture';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-500/20 text-slate-300 border border-slate-500/30';
        }
        if (c1) c1.setAttribute('stroke-width', '12');
        if (c2) c2.setAttribute('stroke-width', '11');
        if (c3) c3.setAttribute('stroke-width', '10');
        if (vapor) vapor.setAttribute('opacity', '0.9');
        if (pct) {
            pct.textContent = '85% (Juicy)';
            pct.setAttribute('fill', '#38bdf8');
        }
        if (desc) desc.textContent = 'Day 1: Freshly harvested chillies contain 85% cellular water, making them highly vulnerable to mold if left in damp air.';
    } else if (day === 3) {
        if (badge) {
            badge.textContent = 'Day 3: 40% Moisture';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (c1) c1.setAttribute('stroke-width', '8');
        if (c2) c2.setAttribute('stroke-width', '7');
        if (c3) c3.setAttribute('stroke-width', '7');
        if (vapor) vapor.setAttribute('opacity', '0.5');
        if (pct) {
            pct.textContent = '40% (Wilting)';
            pct.setAttribute('fill', '#f59e0b');
        }
        if (desc) desc.textContent = 'Day 3: Continuous solar heat evaporates free cellular water. The chillies shrivel, wrinkle, and lose over half their weight.';
    } else {
        if (badge) {
            badge.textContent = 'Day 5: 8% Moisture (Dry)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (c1) c1.setAttribute('stroke-width', '5');
        if (c2) c2.setAttribute('stroke-width', '4');
        if (c3) c3.setAttribute('stroke-width', '4');
        if (vapor) vapor.setAttribute('opacity', '0');
        if (pct) {
            pct.textContent = '8% (Crisp Dry)';
            pct.setAttribute('fill', '#10b981');
        }
        if (desc) desc.textContent = 'Finding #3: Moisture drops below 10%! Without water, microbial enzymes cannot function. The crisp red chillies can now be stored for a year!';
    }
}

// Sim 6: Grandmother's Pickle Jar
function setPickleOil(hasOil) {
    const badge = document.getElementById('sim6-badge');
    const oilLayer = document.getElementById('sim6-oil-layer');
    const oilLabel = document.getElementById('sim6-oil-label');
    const mold = document.getElementById('sim6-mold');
    const desc = document.getElementById('sim6-desc');

    if (hasOil) {
        if (badge) {
            badge.textContent = 'Oil Seal: 100% Sealed';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (oilLayer) oilLayer.setAttribute('opacity', '0.85');
        if (oilLabel) oilLabel.textContent = 'Mustard Oil Barrier';
        if (mold) mold.setAttribute('opacity', '0');
        if (desc) desc.textContent = 'Finding #4: Thick mustard oil floats on top, completely cutting off atmospheric oxygen so molds cannot respire or germinate!';
    } else {
        if (badge) {
            badge.textContent = 'Oil Removed: Oxygen Infiltrates';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (oilLayer) oilLayer.setAttribute('opacity', '0.1');
        if (oilLabel) oilLabel.textContent = 'No Oil Barrier!';
        if (mold) mold.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Without the protective oil layer, air and oxygen contact the mango pieces. Airborne mold spores germinate, rapidly spoiling the top pieces!';
    }
}

// Sim 7: Temperature Danger Zone Meter
function setTempZone(zone) {
    const badge = document.getElementById('sim7-badge');
    const pointer = document.getElementById('sim7-pointer');
    const statusText = document.getElementById('sim7-status-text');
    const desc = document.getElementById('sim7-desc');

    if (zone === 'fridge') {
        if (badge) {
            badge.textContent = 'Refrigerator: 4°C';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (pointer) pointer.setAttribute('points', '60,110 50,130 70,130');
        if (statusText) {
            statusText.textContent = 'Bacterial Growth: Sluggish / Sleeping';
            statusText.setAttribute('fill', '#38bdf8');
        }
        if (desc) desc.textContent = 'Finding #5: In the refrigerator at 4°C, enzymes slow down dramatically. Bacteria cannot multiply fast enough to spoil milk for several days.';
    } else if (zone === 'room') {
        if (badge) {
            badge.textContent = 'Danger Zone: 30°C';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (pointer) pointer.setAttribute('points', '165,110 155,130 175,130');
        if (statusText) {
            statusText.textContent = 'Bacterial Growth: Doubling Every 20 Mins!';
            statusText.setAttribute('fill', '#f87171');
        }
        if (desc) desc.textContent = 'Room temperature (20-45°C) is the danger zone! Warmth stimulates rapid enzyme activity, causing food spoilage in hours.';
    } else {
        if (badge) {
            badge.textContent = 'Boiling Sterilization: 100°C';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (pointer) pointer.setAttribute('points', '275,110 265,130 285,130');
        if (statusText) {
            statusText.textContent = 'Bacteria: Destroyed by Rolling Heat';
            statusText.setAttribute('fill', '#fb923c');
        }
        if (desc) desc.textContent = 'Boiling milk to 100°C destroys active vegetative bacteria and pasteurizes it, making it clean and safe.';
    }
}

// Sim 8: Pantry Preservation Vault
function selectPreserveVault(method) {
    const badge = document.getElementById('sim8-badge');
    const content = document.getElementById('sim8-content');
    const desc = document.getElementById('sim8-desc');

    if (method === 'sugar') {
        if (badge) {
            badge.textContent = 'Method: Sugar Murabba';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (content) {
            content.innerHTML = `
                <circle cx="150" cy="95" r="22" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
                <circle cx="210" cy="95" r="22" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
                <circle cx="180" cy="125" r="20" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
                <rect x="95" y="70" width="170" height="90" rx="10" fill="#facc15" opacity="0.35"/>
                <text x="180" y="60" text-anchor="middle" font-size="10" fill="#fde047" font-weight="bold">Thick Sugar Syrup (Osmosis)</text>
            `;
        }
        if (desc) desc.textContent = 'Finding #6: High sugar syrup locks water tightly through osmotic pressure, starving bacteria of moisture and preserving amla murabba for months.';
    } else if (method === 'salt') {
        if (badge) {
            badge.textContent = 'Method: Salt Brine (Lemons)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (content) {
            content.innerHTML = `
                <circle cx="150" cy="105" r="20" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
                <circle cx="210" cy="105" r="20" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
                <circle cx="180" cy="135" r="18" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
                <rect x="95" y="80" width="170" height="80" rx="10" fill="#38bdf8" opacity="0.25"/>
                <text x="180" y="60" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">Salt Brine (Dehydrates Microbes)</text>
            `;
        }
        if (desc) desc.textContent = 'Heavy salt draws out water from microbial cells through osmosis. Shriveled bacterial cells become dormant, keeping lemons crisp.';
    } else if (method === 'spices') {
        if (badge) {
            badge.textContent = 'Method: Antimicrobial Spices';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (content) {
            content.innerHTML = `
                <circle cx="140" cy="100" r="8" fill="#1e293b" stroke="#64748b"/>
                <circle cx="160" cy="115" r="7" fill="#1e293b" stroke="#64748b"/>
                <circle cx="200" cy="105" r="8" fill="#1e293b" stroke="#64748b"/>
                <circle cx="220" cy="120" r="7" fill="#1e293b" stroke="#64748b"/>
                <rect x="170" y="80" width="20" height="40" rx="4" fill="#eab308" opacity="0.8"/>
                <text x="180" y="60" text-anchor="middle" font-size="10" fill="#34d399" font-weight="bold">Pepper & Turmeric (Bioactive Oils)</text>
            `;
        }
        if (desc) desc.textContent = 'Black pepper contains piperine, and turmeric contains curcumin. These natural essential oils destroy bacterial membranes and suppress mold.';
    } else {
        if (badge) {
            badge.textContent = 'Method: Vacuum Packaging';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
        }
        if (content) {
            content.innerHTML = `
                <rect x="120" y="65" width="120" height="85" rx="8" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
                <text x="180" y="105" text-anchor="middle" font-size="12" fill="#c7d2fe" font-weight="bold">0% OXYGEN</text>
                <text x="180" y="125" text-anchor="middle" font-size="8" fill="#94a3b8">Vacuum Sealed Pouch</text>
                <text x="180" y="55" text-anchor="middle" font-size="10" fill="#818cf8" font-weight="bold">Hermetic Vacuum (Air Extracted)</text>
            `;
        }
        if (desc) desc.textContent = 'Factory machines extract all atmospheric oxygen and seal foil packets, preventing aerobic molds and stopping fats from turning rancid.';
    }
}

// Sim 9: Idli Batter Fermentation Lab
function setBatterState(state) {
    const badge = document.getElementById('sim9-badge');
    const batter = document.getElementById('sim9-batter');
    const bubbles = document.getElementById('sim9-bubbles');
    const desc = document.getElementById('sim9-desc');

    if (state === 'unfermented') {
        if (badge) {
            badge.textContent = 'Evening: Freshly Ground Flat';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-500/20 text-slate-300 border border-slate-500/30';
        }
        if (batter) batter.setAttribute('d', 'M 115 130 Q 180 120 245 130 Q 255 160 180 160 Q 105 160 115 130 Z');
        if (bubbles) bubbles.setAttribute('opacity', '0');
        if (desc) desc.textContent = 'Evening: Freshly ground rice and urad dal batter sits flat and dense at the bottom of the bowl. No fermentation has occurred yet.';
    } else {
        if (badge) {
            badge.textContent = 'Morning: Fermented & Fluffy';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (batter) batter.setAttribute('d', 'M 106 90 Q 180 70 254 90 Q 260 160 180 160 Q 100 160 106 90 Z');
        if (bubbles) bubbles.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Finding #7: Beneficial airborne yeasts and lactic acid bacteria ferment batter starches, releasing CO2 gas bubbles that expand it into light, fluffy idlis!';
    }
}

// Sim 10: Digestive Gut Microbiome
function setGutState(state) {
    const badge = document.getElementById('sim10-badge');
    const bad = document.getElementById('sim10-bad-microbes');
    const good = document.getElementById('sim10-good-microbes');
    const desc = document.getElementById('sim10-desc');

    if (state === 'upset') {
        if (badge) {
            badge.textContent = 'Fair Food: Indigestion & Cramps';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (bad) bad.setAttribute('opacity', '1');
        if (good) good.setAttribute('opacity', '0.2');
        if (desc) desc.textContent = 'Finding #8: Uncovered fair snacks brought harmful pathogenic bacteria that disrupt normal digestion, triggering cramps and indigestion.';
    } else {
        if (badge) {
            badge.textContent = 'Buttermilk Remedy: Gut Restored';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (bad) bad.setAttribute('opacity', '0.05');
        if (good) good.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Fresh buttermilk supplies billions of helpful Lactobacillus bacteria that outcompete harmful germs, neutralizing stomach acid and restoring calm.';
    }
}

// Sim 11: Vegetable Quality Inspector
function setProduceQuality(quality) {
    const badge = document.getElementById('sim11-badge');
    const gloss = document.getElementById('sim11-gloss');
    const defect = document.getElementById('sim11-defect');
    const desc = document.getElementById('sim11-desc');

    if (quality === 'fresh') {
        if (badge) {
            badge.textContent = 'Tomato: Fresh & Firm (Select)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (gloss) gloss.setAttribute('opacity', '0.8');
        if (defect) defect.setAttribute('opacity', '0');
        if (desc) desc.textContent = "Grandfather Thatha's rule: Look for taut, glossy skin and firm texture. Avoid bruises or punctures that let spoilage microbes inside!";
    } else {
        if (badge) {
            badge.textContent = 'Tomato: Bruised & Moldy (Reject)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (gloss) gloss.setAttribute('opacity', '0.1');
        if (defect) defect.setAttribute('opacity', '0.9');
        if (desc) desc.textContent = 'Deep bruise and puncture detected! Punctures break the protective outer skin, allowing spoilage bacteria and mold hyphae to decompose the inner pulp.';
    }
}

// Sim 12: Seasonal Harvest Calendar
function setSeasonCalendar(season) {
    const badge = document.getElementById('sim12-badge');
    const emoji = document.getElementById('sim12-fruit-emoji');
    const text = document.getElementById('sim12-fruit-text');
    const desc = document.getElementById('sim12-desc');

    if (season === 'summer') {
        if (badge) {
            badge.textContent = 'Summer Harvest (May-June)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (emoji) emoji.textContent = '🥭';
        if (text) text.textContent = 'Mango & Lychee';
        if (desc) desc.textContent = 'Finding #9: Summer brings juicy regional mangoes and lychees, providing natural sugars, water, and cooling nutrients without artificial ripening!';
    } else if (season === 'winter') {
        if (badge) {
            badge.textContent = 'Winter Harvest (Dec-Jan)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30';
        }
        if (emoji) emoji.textContent = '🥕';
        if (text) text.textContent = 'Carrot, Guava & Orange';
        if (desc) desc.textContent = 'Winter yields crisp red carrots, sweet guavas, and amla packed with Vitamin C to fortify our immune system during cold weather.';
    } else {
        if (badge) {
            badge.textContent = 'Monsoon Harvest (July-Aug)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (emoji) emoji.textContent = '🫐';
        if (text) text.textContent = 'Jamun & Corn (Bhutta)';
        if (desc) desc.textContent = 'Monsoon brings sweet roasted corn on the cob and purple jamuns rich in minerals and digestive-friendly astringents.';
    }
}

// Sim 13: Human Dental Arch
function selectTeethGroup(group) {
    const badge = document.getElementById('sim13-badge');
    const toolIcon = document.getElementById('sim13-tool-icon');
    const toolDesc = document.getElementById('sim13-tool-desc');
    const desc = document.getElementById('sim13-desc');

    if (group === 'incisors') {
        if (badge) {
            badge.textContent = 'Incisors (8 Teeth): Cutting';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30';
        }
        if (toolIcon) toolIcon.textContent = '✂️';
        if (toolDesc) toolDesc.textContent = 'Chisel Action: Cutting & Slicing';
        if (desc) desc.textContent = 'Finding #11: 8 front incisors have sharp, horizontal chisel edges designed specifically for cutting and biting off food portions.';
    } else if (group === 'canines') {
        if (badge) {
            badge.textContent = 'Canines (4 Teeth): Tearing';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (toolIcon) toolIcon.textContent = '🗡️';
        if (toolDesc) toolDesc.textContent = 'Dagger Action: Piercing & Tearing';
        if (desc) desc.textContent = '4 pointed canines beside incisors act like sharp daggers, specialized for piercing and tearing tough, fibrous food items.';
    } else if (group === 'premolars') {
        if (badge) {
            badge.textContent = 'Premolars (8 Teeth): Crushing';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (toolIcon) toolIcon.textContent = '🔨';
        if (toolDesc) toolDesc.textContent = 'Hammer Action: Holding & Crushing';
        if (desc) desc.textContent = '8 broad premolars with dual cusps hold and crush food chunks into smaller, manageable fragments.';
    } else {
        if (badge) {
            badge.textContent = 'Molars (12 Teeth): Grinding';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
        }
        if (toolIcon) toolIcon.textContent = '⚙️';
        if (toolDesc) toolDesc.textContent = 'Millstone Action: Pulverizing to Paste';
        if (desc) desc.textContent = '12 large back molars have broad, bumpy occlusal surfaces that grind food into a fine, smooth paste before swallowing.';
    }
}

// Sim 14: Salivary Amylase Starch Digestion
function setChewTimer(sec) {
    const badge = document.getElementById('sim14-badge');
    const banner = document.getElementById('sim14-taste-banner');
    const desc = document.getElementById('sim14-desc');

    if (sec === 0) {
        if (badge) {
            badge.textContent = 'Chewing: 0 Seconds';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-500/20 text-slate-300 border border-slate-500/30';
        }
        if (banner) banner.textContent = 'Solid Food: Tasteless Starch';
        if (desc) desc.textContent = 'At 0 seconds, a piece of boiled rice or chapati consists of long, complex starch molecules that taste plain and bland.';
    } else if (sec === 30) {
        if (badge) {
            badge.textContent = 'Chewing: 30 Seconds';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (banner) banner.textContent = 'Enzymes Cutting Starch Chains';
        if (desc) desc.textContent = 'Finding #10: Salivary amylase mixes with crushed food, slicing long starch polymers into shorter dextrin molecules.';
    } else {
        if (badge) {
            badge.textContent = 'Chewing: 60 Seconds (Sweet!)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (banner) banner.textContent = 'Sweet Maltose Sugar Released!';
        if (desc) desc.textContent = 'After 60 seconds of thorough chewing, starch converts into simple sweet maltose sugar! Saliva lubricates food into a smooth bolus.';
    }
}

// Sim 15: Dental Cavity Defense Station
function setDentalAction(action) {
    const badge = document.getElementById('sim15-badge');
    const enamel = document.getElementById('sim15-enamel');
    const cavity = document.getElementById('sim15-cavity');
    const desc = document.getElementById('sim15-desc');

    if (action === 'brush') {
        if (badge) {
            badge.textContent = 'Healthy Enamel Shield';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (enamel) enamel.setAttribute('fill', '#f8fafc');
        if (cavity) cavity.setAttribute('opacity', '0');
        if (desc) desc.textContent = 'Finding #12: Brushing twice daily flushes away bacterial plaque before microbes can ferment sugars into enamel-dissolving acid!';
    } else {
        if (badge) {
            badge.textContent = 'Acid Attack: Cavity Forming!';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (enamel) enamel.setAttribute('fill', '#fef3c7');
        if (cavity) cavity.setAttribute('opacity', '1');
        if (desc) desc.textContent = 'Trapped sugary food particles feed oral bacteria. The bacteria excrete lactic acid, which dissolves calcium enamel and carves a painful cavity hole!';
    }
}

// Sim 16: Throat Crossroads & Epiglottis Valve
function setThroatAction(action) {
    const badge = document.getElementById('sim16-badge');
    const epiglottis = document.getElementById('sim16-epiglottis');
    const bolus = document.getElementById('sim16-bolus');
    const desc = document.getElementById('sim16-desc');

    if (action === 'swallow') {
        if (badge) {
            badge.textContent = 'Safe Swallowing: Windpipe Sealed';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (epiglottis) {
            epiglottis.setAttribute('x1', '165');
            epiglottis.setAttribute('y1', '75');
            epiglottis.setAttribute('x2', '135');
            epiglottis.setAttribute('y2', '95');
            epiglottis.setAttribute('stroke', '#10b981');
        }
        if (bolus) {
            bolus.setAttribute('cx', '212');
            bolus.setAttribute('cy', '110');
            bolus.setAttribute('fill', '#d97706');
        }
        if (desc) desc.textContent = 'Finding #13: When you swallow calmly, the muscular epiglottis folds down to seal the windpipe, guiding food smoothly into the esophagus!';
    } else {
        if (badge) {
            badge.textContent = 'Talking: Windpipe Open (Choking!)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        }
        if (epiglottis) {
            epiglottis.setAttribute('x1', '165');
            epiglottis.setAttribute('y1', '75');
            epiglottis.setAttribute('x2', '165');
            epiglottis.setAttribute('y2', '55');
            epiglottis.setAttribute('stroke', '#ef4444');
        }
        if (bolus) {
            bolus.setAttribute('cx', '147');
            bolus.setAttribute('cy', '110');
            bolus.setAttribute('fill', '#ef4444');
        }
        if (desc) desc.textContent = 'DANGER! Talking forces the epiglottis upright for voice airflow. Food slips down into the open windpipe, triggering violent emergency coughing!';
    }
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


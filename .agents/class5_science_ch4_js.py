"""
Interactive JavaScript module for NCERT Class 5 Science Chapter 4: Our School - A Happy Place
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
// Science Chapter 4 Interactive JavaScript
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
                btn.className = 'px-3 py-1.5 rounded-xl bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 text-xs font-bold flex items-center space-x-1.5 border border-emerald-500/30 transition shadow-sm';
                if (badge) {
                    badge.textContent = 'Audio Lecture Ready';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
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
            globalBtn.className = 'px-3 py-2 rounded-xl bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 text-xs font-bold flex items-center space-x-1.5 border border-emerald-500/30 transition shadow-sm';
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

// Sim 1: Green Campus Explorer
function selectCampusZone(zone) {
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');

    const zoneData = {
        solar: {
            title: "Zone: Solar Rooftop (Clean Power)",
            badgeClass: "bg-sky-500/20 text-sky-300 border-sky-500/30",
            text: "Rooftop solar photovoltaic cells convert Indian sunshine into clean electricity, powering computer labs and classroom fans without burning coal!"
        },
        compost: {
            title: "Zone: Organic Compost Yard",
            badgeClass: "bg-amber-500/20 text-amber-300 border-amber-500/30",
            text: "Canteen vegetable scraps, fruit skins, and dry leaves decompose naturally into dark, organic manure that enriches campus flowerbeds."
        },
        rainwater: {
            title: "Zone: Rainwater Recharge Pit",
            badgeClass: "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
            text: "Clean monsoon rainwater from terrace gutters filters through sand and gravel pits to replenish the underground water table beneath the school!"
        },
        trees: {
            title: "Zone: Native Neem Canopy",
            badgeClass: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
            text: "Indigenous neem and peepal trees filter airborne dust, provide cool shade that lowers classroom temperatures by 5°C, and shelter nesting birds."
        }
    };

    const item = zoneData[zone] || zoneData.trees;
    if (badge) {
        badge.textContent = item.title;
        badge.className = `px-2 py-0.5 rounded text-[10px] font-bold ${item.badgeClass} border`;
    }
    if (desc) desc.textContent = item.text;
}

// Sim 2: Student Explorer Brigades
function selectExplorerTeam(team) {
    const badge = document.getElementById('sim2-badge');
    const icon = document.getElementById('sim2-center-icon');
    const desc = document.getElementById('sim2-desc');

    const teamData = {
        water: {
            icon: "💧",
            title: "Active: Water Watchers",
            badgeClass: "bg-sky-500/20 text-sky-300 border-sky-500/30",
            text: "Water Watchers: Inspect taps, washrooms, and water coolers to detect drips, report worn washers, and ensure drinking water is never wasted."
        },
        electricity: {
            icon: "⚡",
            title: "Active: Electricity Savers",
            badgeClass: "bg-amber-500/20 text-amber-300 border-amber-500/30",
            text: "Electricity Savers: Patrol corridors during recess and assembly to switch off idle fans, tube lights, and monitors in empty classrooms."
        },
        waste: {
            icon: "🗑️",
            title: "Active: Waste Warriors",
            badgeClass: "bg-rose-500/20 text-rose-300 border-rose-500/30",
            text: "Waste Warriors: Inspect dustbins, teach proper separation into green and blue bins, and monitor campus compost pits."
        },
        green: {
            icon: "🌳",
            title: "Active: Green Guardians",
            badgeClass: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
            text: "Green Guardians: Plant indigenous trees, water flowerbeds, monitor butterfly gardens, and record visiting bird species."
        },
        traffic: {
            icon: "🚶",
            title: "Active: Traffic Trackers",
            badgeClass: "bg-indigo-500/20 text-indigo-300 border-indigo-500/30",
            text: "Traffic Trackers: Audit school gate safety during morning drop-off, verify 20 km/h speed limits, and promote safe crosswalk habits."
        }
    };

    const item = teamData[team] || teamData.water;
    if (badge) {
        badge.textContent = item.title;
        badge.className = `px-2 py-0.5 rounded text-[10px] font-bold ${item.badgeClass} border`;
    }
    if (icon) icon.textContent = item.icon;
    if (desc) desc.textContent = item.text;
}

// Sim 3: Dual-Bin Waste Sorter
let wasteIndex = 0;
const wasteItems = [
    { name: "Banana Peel", icon: "🍌", type: "green", desc: "Correct! Banana peels are organic wet waste that decomposes into nutrient-rich compost." },
    { name: "Scrap Exam Paper", icon: "📄", type: "blue", desc: "Correct! Dry paper belongs in the blue bin to be sent to paper recycling mills." },
    { name: "Apple Core", icon: "🍎", type: "green", desc: "Correct! Leftover fruit pieces are biodegradable and belong in the green wet bin." },
    { name: "Empty Cardboard Box", icon: "📦", type: "blue", desc: "Correct! Cardboard cartons are dry recyclables that can be re-pulped into new books." }
];

function sortItemToBin(selectedBin) {
    const item = wasteItems[wasteIndex];
    const badge = document.getElementById('sim3-badge');
    const itemIcon = document.getElementById('sim3-item-icon');
    const itemName = document.getElementById('sim3-item-name');
    const desc = document.getElementById('sim3-desc');

    if (selectedBin === item.type) {
        if (badge) {
            badge.textContent = "Sorted Correctly! ✓";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) desc.textContent = item.desc;
    } else {
        if (badge) {
            badge.textContent = "Wrong Bin! Contamination!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (desc) desc.textContent = "Contamination Warning: Never mix wet food with dry paper! Wet scraps make paper soggy and impossible to recycle.";
    }

    wasteIndex = (wasteIndex + 1) % wasteItems.length;
    const nextItem = wasteItems[wasteIndex];
    setTimeout(() => {
        if (itemIcon) itemIcon.textContent = nextItem.icon;
        if (itemName) itemName.textContent = nextItem.name;
    }, 600);
}

// Sim 4: Recycling & Dignity of Labour
function triggerGratitudeAction(action) {
    const badge = document.getElementById('sim4-badge');
    const desc = document.getElementById('sim4-desc');

    if (action === 'thank') {
        if (badge) {
            badge.textContent = "Respect: Greeted Cleaning Staff!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) desc.textContent = "Dignity of Labour: Greeting housekeeping and sanitation staff with polite appreciation acknowledges their indispensable role in maintaining campus health!";
    } else {
        if (badge) {
            badge.textContent = "Cleaned Personal Desk!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
        }
        if (desc) desc.textContent = "Personal Stewardship: Cleaning up your own tiffin crumbs and disposing of pencil shavings in the bin shows true respect for campus staff.";
    }
}

// Sim 5: Passive Thermal Cooling Model
function setCoolingMode(mode) {
    const badge = document.getElementById('sim5-badge');
    const roof = document.getElementById('sim5-roof');
    const label = document.getElementById('sim5-roof-label');
    const winLeft = document.getElementById('sim5-win-left');
    const winRight = document.getElementById('sim5-win-right');
    const breeze = document.getElementById('sim5-breeze');
    const tempText = document.getElementById('sim5-temp-text');
    const desc = document.getElementById('sim5-desc');

    if (mode === 'cool') {
        if (badge) {
            badge.textContent = "Cool Roof: 28°C (Breezy)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
        }
        if (roof) {
            roof.setAttribute('fill', '#f8fafc');
            roof.setAttribute('stroke', '#cbd5e1');
        }
        if (label) {
            label.textContent = "WHITE REFLECTIVE ROOF (85% REFLECTED)";
            label.setAttribute('fill', '#475569');
        }
        if (winLeft) winLeft.setAttribute('opacity', '0.8');
        if (winRight) winRight.setAttribute('opacity', '0.8');
        if (breeze) breeze.setAttribute('opacity', '1');
        if (tempText) {
            tempText.textContent = "28°C";
            tempText.setAttribute('fill', '#38bdf8');
        }
        if (desc) desc.textContent = "Passive Cooling Physics: Reflective white roof bounces 85% of solar rays away, while cross-ventilation flushes out hot indoor air!";
    } else {
        if (badge) {
            badge.textContent = "Dark Roof: 38°C (Stifling Hot)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (roof) {
            roof.setAttribute('fill', '#0f172a');
            roof.setAttribute('stroke', '#334155');
        }
        if (label) {
            label.textContent = "DARK TAR ROOF (ABSORBS 90% HEAT)";
            label.setAttribute('fill', '#f87171');
        }
        if (winLeft) winLeft.setAttribute('opacity', '0.2');
        if (winRight) winRight.setAttribute('opacity', '0.2');
        if (breeze) breeze.setAttribute('opacity', '0');
        if (tempText) {
            tempText.textContent = "38°C";
            tempText.setAttribute('fill', '#ef4444');
        }
        if (desc) desc.textContent = "Thermal Trap: Dark tar roofs absorb solar heat like a furnace, while closed windows trap hot air, driving room temperature up to 38°C!";
    }
}

// Sim 6: Leaking Tap Accumulator
function setTapRepair(repaired) {
    const badge = document.getElementById('sim6-badge');
    const drips = document.getElementById('sim6-drips');
    const waterLevel = document.getElementById('sim6-water-level');
    const volText = document.getElementById('sim6-volume-text');
    const desc = document.getElementById('sim6-desc');

    if (repaired) {
        if (badge) {
            badge.textContent = "Repaired: 0 Liters Wasted!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (drips) drips.setAttribute('opacity', '0');
        if (waterLevel) waterLevel.setAttribute('height', '5');
        if (volText) {
            volText.textContent = "0.0 Liters";
            volText.setAttribute('fill', '#10b981');
        }
        if (desc) desc.textContent = "Leak Fixed! A new 5-rupee rubber washer seals the valve tightly, conserving over 10,000 liters of pure drinking water every year.";
    } else {
        if (badge) {
            badge.textContent = "Dripping: 30 L / Day";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (drips) drips.setAttribute('opacity', '1');
        if (waterLevel) waterLevel.setAttribute('height', '28');
        if (volText) {
            volText.textContent = "30.2 Liters";
            volText.setAttribute('fill', '#f59e0b');
        }
        if (desc) desc.textContent = "Shocking Math: A single tap dripping once per second loses over 30 liters daily. Report leaks to school plumbers promptly!";
    }
}

// Sim 7: Canopy Thermometer Probe
function setProbeLocation(loc) {
    const badge = document.getElementById('sim7-badge');
    const probe = document.getElementById('sim7-probe');
    const mercury = document.getElementById('sim7-mercury');
    const desc = document.getElementById('sim7-desc');

    if (loc === 'asphalt') {
        if (badge) {
            badge.textContent = "Asphalt Court: 43°C (Scorching)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (probe) probe.setAttribute('transform', 'translate(95, 120)');
        if (mercury) {
            mercury.setAttribute('y', '-30');
            mercury.setAttribute('height', '38');
        }
        if (desc) desc.textContent = "Dark asphalt basketball courts absorb solar energy and radiate intense heat, reaching a scorching 43°C under direct afternoon sun.";
    } else {
        if (badge) {
            badge.textContent = "Neem Canopy: 34°C (Gentle Shade)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (probe) probe.setAttribute('transform', 'translate(265, 120)');
        if (mercury) {
            mercury.setAttribute('y', '-15');
            mercury.setAttribute('height', '23');
        }
        if (desc) desc.textContent = "Microclimate Science: Physical tree shade blocks radiant heat while foliar transpiration evaporates moisture, dropping temperature by 9°C!";
    }
}

// Sim 8: Butterfly Habitat Designer
function toggleGardenPlot(plot) {
    const badge = document.getElementById('sim8-badge');
    const host = document.getElementById('sim8-host-group');
    const butterfly = document.getElementById('sim8-butterfly');
    const desc = document.getElementById('sim8-desc');

    if (plot === 'both') {
        if (badge) {
            badge.textContent = "Complete Habitat: Nectar + Host";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (host) host.setAttribute('opacity', '1');
        if (butterfly) butterfly.setAttribute('opacity', '1');
        if (desc) desc.textContent = "Biodiversity Secret: Adult butterflies sip sweet nectar, but females lay eggs only on specific host leaves like curry leaves for baby caterpillars to hatch!";
    } else {
        if (badge) {
            badge.textContent = "Nectar Only: No Egg Laying";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (host) host.setAttribute('opacity', '0.2');
        if (butterfly) butterfly.setAttribute('opacity', '0.5');
        if (desc) desc.textContent = "Without host plants, adult butterflies visit briefly for sweet nectar but cannot breed or lay eggs, preventing new generations from flourishing.";
    }
}

// Sim 9: School Zone Traffic Calmer
function setSchoolSpeed(speed) {
    const badge = document.getElementById('sim9-badge');
    const van = document.getElementById('sim9-van');
    const brakeLine = document.getElementById('sim9-brake-line');
    const brakeText = document.getElementById('sim9-brake-text');
    const desc = document.getElementById('sim9-desc');

    if (speed === 20) {
        if (badge) {
            badge.textContent = "Speed: 20 km/h (Safe Zone)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (van) van.setAttribute('transform', 'translate(60, 115)');
        if (brakeLine) {
            brakeLine.setAttribute('x2', '120');
            brakeLine.setAttribute('stroke', '#10b981');
        }
        if (brakeText) {
            brakeText.textContent = "Stop in 6m (Safe)";
            brakeText.setAttribute('fill', '#10b981');
        }
        if (desc) desc.textContent = "Stopping Physics: At 20 km/h, a driver can brake and stop completely within 6 meters, preventing collisions with crossing students.";
    } else {
        if (badge) {
            badge.textContent = "Hazard: 50 km/h (Excessive Speed)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (van) van.setAttribute('transform', 'translate(130, 115)');
        if (brakeLine) {
            brakeLine.setAttribute('x2', '240');
            brakeLine.setAttribute('stroke', '#ef4444');
        }
        if (brakeText) {
            brakeText.textContent = "Skids 25m! (DANGER)";
            brakeText.setAttribute('fill', '#ef4444');
        }
        if (desc) desc.textContent = "Severe Danger: At 50 km/h, vehicle momentum requires 25 meters to stop, endangering students crossing at school gates!";
    }
}

// Sim 10: Traffic Signboard Decrypter
function selectTrafficSign(type) {
    const badge = document.getElementById('sim10-badge');
    const display = document.getElementById('sim10-sign-display');
    const desc = document.getElementById('sim10-desc');

    if (type === 'mandatory') {
        if (badge) {
            badge.textContent = "Mandatory: Red Circle / Stop";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (display) {
            display.innerHTML = `
                <polygon points="150,40 210,40 235,65 235,105 210,130 150,130 125,105 125,65" fill="#dc2626" stroke="#f8fafc" stroke-width="4"/>
                <text x="180" y="92" text-anchor="middle" font-size="18" fill="#ffffff" font-weight="extrabold">STOP</text>
            `;
        }
        if (desc) desc.textContent = "Mandatory Signs: Circular red signs give direct legal orders. Drivers must come to a complete halt before proceeding.";
    } else if (type === 'cautionary') {
        if (badge) {
            badge.textContent = "Cautionary: Triangular Warning";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (display) {
            display.innerHTML = `
                <polygon points="180,35 240,125 120,125" fill="#fef08a" stroke="#dc2626" stroke-width="6"/>
                <text x="180" y="100" text-anchor="middle" font-size="20">🚸</text>
                <text x="180" y="118" text-anchor="middle" font-size="7" fill="#1e293b" font-weight="bold">SCHOOL AHEAD</text>
            `;
        }
        if (desc) desc.textContent = "Cautionary Signs: Triangular signs with red borders warn drivers of upcoming hazards ahead, such as children crossing near a school gate.";
    } else {
        if (badge) {
            badge.textContent = "Informatory: Blue Rectangle";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30";
        }
        if (display) {
            display.innerHTML = `
                <rect x="135" y="45" width="90" height="75" rx="6" fill="#0284c7" stroke="#ffffff" stroke-width="3"/>
                <text x="180" y="85" text-anchor="middle" font-size="22">🚌</text>
                <text x="180" y="108" text-anchor="middle" font-size="8" fill="#ffffff" font-weight="bold">BUS STOP</text>
            `;
        }
        if (desc) desc.textContent = "Informatory Signs: Blue rectangular signboards provide helpful navigation, designating public bus stops, hospitals, and pedestrian crossing facilities.";
    }
}

// Sim 11: Fire Evacuation Floorplan
function triggerDrillStep(step) {
    const badge = document.getElementById('sim11-badge');
    const students = document.getElementById('sim11-students');
    const desc = document.getElementById('sim11-desc');

    if (step === 'evacuate') {
        if (badge) {
            badge.textContent = "Alarm: Single-File Evacuation";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
        }
        if (students) students.setAttribute('opacity', '0.7');
        if (desc) desc.textContent = "Leave bags behind! Form a quiet single line and walk briskly down staircases holding the handrails without running or pushing.";
    } else {
        if (badge) {
            badge.textContent = "Muster Point: 100% Accounted";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (students) students.setAttribute('opacity', '1');
        if (desc) desc.textContent = "Assembly Roll Call: All students stand in their class line on the open sports ground while teachers verify attendance to ensure complete safety.";
    }
}

// Sim 12: Low-Smoke Crawl Simulator
function setSmokePosture(posture) {
    const badge = document.getElementById('sim12-badge');
    const student = document.getElementById('sim12-student');
    const desc = document.getElementById('sim12-desc');

    if (posture === 'crawl') {
        if (badge) {
            badge.textContent = "Action: Crawl on Hands & Knees";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (student) student.setAttribute('transform', 'translate(100, 130)');
        if (desc) desc.textContent = "Thermal Buoyancy Physics: Hot toxic gases rise toward the ceiling. Crawling on hands and knees keeps your nose in the coolest, oxygen-rich air layer!";
    } else {
        if (badge) {
            badge.textContent = "DANGER: Standing in Toxic Smoke!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (student) student.setAttribute('transform', 'translate(100, 70)');
        if (desc) desc.textContent = "Severe Inhalation Danger! Walking upright forces you to breathe scorching toxic fumes and carbon monoxide gas trapped near the ceiling!";
    }
}

// Sim 13: Campus Kindness & Civility
function setDeskEtiquette(mode) {
    const badge = document.getElementById('sim13-badge');
    const content = document.getElementById('sim13-desk-content');
    const desc = document.getElementById('sim13-desc');

    if (mode === 'clean') {
        if (badge) {
            badge.textContent = "Happiness Index: 100%";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (content) {
            content.innerHTML = `
                <rect x="140" y="85" width="80" height="45" rx="2" fill="#f8fafc"/>
                <line x1="180" y1="85" x2="180" y2="130" stroke="#cbd5e1"/>
                <text x="180" y="105" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="bold">CLEAN DESK</text>
                <text x="180" y="120" text-anchor="middle" font-size="7" fill="#64748b">Respect Shared Property</text>
            `;
        }
        if (desc) desc.textContent = "Public Stewardship: Taking turns in line and keeping wooden desks clean preserves school heritage for younger students and builds mutual respect!";
    } else {
        if (badge) {
            badge.textContent = "Happiness Index: 30% (Damaged)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (content) {
            content.innerHTML = `
                <path d="M 120 95 Q 160 110 240 90 M 130 115 L 210 110" stroke="#ef4444" stroke-width="2" fill="none"/>
                <text x="180" y="105" text-anchor="middle" font-size="8" fill="#f87171" font-weight="bold">SCRIBBLED GRAFFITI</text>
                <text x="180" y="120" text-anchor="middle" font-size="7" fill="#fca5a5">Damaging Public Property</text>
            `;
        }
        if (desc) desc.textContent = "Scribbling on shared furniture damages school property and creates a neglected atmosphere. Respect shared classroom treasures!";
    }
}

// Sim 14: Universal Accessibility Station
function setAccessibilityFeature(feat) {
    const badge = document.getElementById('sim14-badge');
    const ramp = document.getElementById('sim14-ramp');
    const tactile = document.getElementById('sim14-tactile');
    const wheelchair = document.getElementById('sim14-wheelchair');
    const desc = document.getElementById('sim14-desc');

    if (feat === 'ramp') {
        if (badge) {
            badge.textContent = "Accessible: Gentle Ramp (1:12)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
        }
        if (ramp) ramp.setAttribute('opacity', '1');
        if (tactile) tactile.setAttribute('opacity', '1');
        if (wheelchair) wheelchair.setAttribute('opacity', '1');
        if (desc) desc.textContent = "Universal Design: A gentle 1:12 slope ramp with handrails and yellow tactile floor tiles ensures that friends using wheelchairs or canes navigate freely!";
    } else {
        if (badge) {
            badge.textContent = "Barrier: Steep Stairs (Blocked)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (ramp) ramp.setAttribute('opacity', '0.1');
        if (tactile) tactile.setAttribute('opacity', '0.1');
        if (wheelchair) wheelchair.setAttribute('opacity', '0.3');
        if (desc) desc.textContent = "Physical Barrier: Without an entrance ramp, friends using wheelchairs or recovering from leg injuries cannot enter classrooms independently.";
    }
}

// Sim 15: Classroom Power Switchboard
function setPowerState(state) {
    const badge = document.getElementById('sim15-badge');
    const fan = document.getElementById('sim15-fan');
    const needle = document.getElementById('sim15-meter-needle');
    const wattText = document.getElementById('sim15-watt-text');
    const desc = document.getElementById('sim15-desc');

    if (state === 'save') {
        if (badge) {
            badge.textContent = "Daylight Mode: Fans & Lights Off";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (fan) fan.classList.remove('animate-spin');
        if (needle) needle.setAttribute('x2', '245');
        if (wattText) {
            wattText.textContent = "0 W (Idle)";
            wattText.setAttribute('fill', '#10b981');
        }
        if (desc) desc.textContent = "Energy Conservation: Daylight harvesting uses free solar light. Turning off fans during recess reduces coal burning and prevents air pollution!";
    } else {
        if (badge) {
            badge.textContent = "Wasting Power: Empty Room ON";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (fan) fan.classList.add('animate-spin');
        if (needle) needle.setAttribute('x2', '275');
        if (wattText) {
            wattText.textContent = "450 W (Wasted)";
            wattText.setAttribute('fill', '#f59e0b');
        }
        if (desc) desc.textContent = "Unnecessary Wastage: Fans and lights left spinning in an empty room during lunch waste hundreds of watt-hours of electrical energy.";
    }
}

// Sim 16: The Campus Happiness Tree
let happinessLeaves = 150;
function addHappinessLeaf(category) {
    happinessLeaves++;
    const badge = document.getElementById('sim16-badge');
    const count = document.getElementById('sim16-leaf-count');
    const desc = document.getElementById('sim16-desc');

    if (count) count.textContent = `${happinessLeaves} Pledges & Kind Acts!`;

    if (category === 'eco') {
        if (badge) {
            badge.textContent = "Eco Leaf Added: Water Saved!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) desc.textContent = "Eco Pledge Added: 'I turned off the leaking tap firmly and planted a marigold seedling in the butterfly garden!'";
    } else if (category === 'kind') {
        if (badge) {
            badge.textContent = "Kindness Leaf: Shared with Peer!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (desc) desc.textContent = "Kindness Act Added: 'I shared my colored pencils with a classmate and invited a new friend to join our playground game.'";
    } else {
        if (badge) {
            badge.textContent = "Gratitude Leaf: Thanked Staff!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) desc.textContent = "Gratitude Note Added: 'Thank you to our school bus driver uncle for driving us safely home every single afternoon!'";
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


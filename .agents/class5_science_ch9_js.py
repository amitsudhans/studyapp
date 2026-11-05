"""
Interactive JavaScript Engine for NCERT Class 5 Science Chapter 9: Rhythms of Nature
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
    const inNonFemale = inVoices.find(v => !isFemaleVoice(v));
    if (inNonFemale) return inNonFemale;

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
                badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500 text-slate-950';
                btn.innerHTML = '<span>❚❚</span> <span>Pause Lecture</span>';
                btn.className = 'px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 text-xs font-bold flex items-center space-x-1.5 transition shadow-sm';
            } else {
                badge.textContent = 'Audio Lecture Ready';
                badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30';
                btn.innerHTML = '<span>▶</span> <span>Listen to Full Lecture</span>';
                btn.className = 'px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm';
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
// 16 BESPOKE SIMULATORS FOR CHAPTER 9
// ==========================================

// SIM 1: Nature's Clock (Time Scales of Change)
function setSim1Scale(scale) {
    const canvas = document.getElementById('sim1StageCanvas');
    const title = document.getElementById('sim1ScaleTitle');
    const status = document.getElementById('sim1Status');
    if (!canvas || !title) return;

    if (scale === 'seconds') {
        title.textContent = "Seconds Scale";
        canvas.innerHTML = `
            <circle cx="200" cy="120" r="28" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
            <ellipse cx="200" cy="120" rx="18" ry="12" fill="#0f172a"/>
            <circle cx="200" cy="120" r="5" fill="#38bdf8"/>
            <circle cx="200" cy="120" r="45" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6">
                <animate attributeName="r" values="35;65;35" dur="1.5s" repeatCount="indefinite"/>
            </circle>
            <text x="200" y="185" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Rapid Change: Blinking Eye (0.3 Seconds)</text>
        `;
        if (status) status.innerHTML = "<strong>Seconds Scale:</strong> A ball bounces instantly, an eye blinks in 0.3 seconds, and a lightning bolt flashes across the sky in a split second.";
    } else if (scale === 'hours') {
        title.textContent = "Hours Scale";
        canvas.innerHTML = `
            <circle cx="200" cy="65" r="24" fill="#fbbf24" opacity="0.9"/>
            <line x1="80" y1="180" x2="320" y2="180" stroke="#475569" stroke-width="2"/>
            <rect x="195" y="120" width="10" height="60" fill="#0284c7" rx="2"/>
            <polygon points="195,180 280,180 195,183" fill="#0f172a" opacity="0.7"/>
            <text x="200" y="210" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Moderate Change: Flagpole Shadow Crawls (12 Hours)</text>
        `;
        if (status) status.innerHTML = "<strong>Hours Scale:</strong> The Sun rises, reaches overhead at noon, and sets in the evening while shadows change length and angle across 12 hours.";
    } else if (scale === 'years') {
        title.textContent = "Years Scale";
        canvas.innerHTML = `
            <rect x="60" y="190" width="280" height="20" fill="#3f2e1a" opacity="0.8"/>
            <path d="M190,190 Q195,140 185,110 Q180,95 160,85" stroke="#78350f" stroke-width="9" fill="none"/>
            <path d="M190,130 Q220,110 235,90" stroke="#78350f" stroke-width="5" fill="none"/>
            <circle cx="150" cy="75" r="38" fill="#15803d" opacity="0.9"/>
            <circle cx="230" cy="80" r="32" fill="#16a34a" opacity="0.9"/>
            <circle cx="190" cy="60" r="40" fill="#22c55e" opacity="0.85"/>
            <text x="200" y="222" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Slow Change: Sapling Grows into Tree (5 Years)</text>
        `;
        if (status) status.innerHTML = "<strong>Years Scale:</strong> Saba and Aparna grow taller, teeth fall and replace, and tiny mango seeds grow into fruit-bearing shade trees across multiple years.";
    }
}

// SIM 2: Day and Night (Torch & Globe Activity 1)
let sim2TorchOn = true;
let sim2GlobeAngle = 0;
function toggleTorchBeam() {
    sim2TorchOn = !sim2TorchOn;
    const beam = document.getElementById('torchBeam');
    const dayHemisphere = document.getElementById('globeDaySide');
    const beamText = document.getElementById('beamStatusText');
    const status = document.getElementById('sim2Status');

    if (beam) beam.setAttribute('opacity', sim2TorchOn ? '0.35' : '0');
    if (dayHemisphere) dayHemisphere.setAttribute('opacity', sim2TorchOn ? '0.9' : '0.2');
    if (beamText) beamText.textContent = sim2TorchOn ? 'Torch: Shining Light' : 'Torch: Switched Off';

    if (status) {
        status.innerHTML = sim2TorchOn
            ? "<strong>Activity 1:</strong> The stationary torch illuminates exactly half of the globe facing it (Day), while the opposite half remains in darkness (Night)."
            : "<strong>Torch Off:</strong> Without light from the Sun, all parts of Earth would remain cold and dark!";
    }
}

function rotateGlobeStep() {
    sim2GlobeAngle = (sim2GlobeAngle + 45) % 360;
    const marker = document.getElementById('indiaPinMarker');
    const indiaStatus = document.getElementById('indiaDayNightText');
    const status = document.getElementById('sim2Status');

    if (marker) {
        const xPos = 240 + Math.sin(sim2GlobeAngle * Math.PI / 180) * 45;
        const yPos = 120 + Math.cos(sim2GlobeAngle * Math.PI / 180) * 12;
        marker.setAttribute('transform', `translate(${xPos}, ${yPos})`);
    }

    const isDay = (sim2GlobeAngle < 90 || sim2GlobeAngle > 270);
    if (indiaStatus) {
        indiaStatus.textContent = isDay ? "India: Experiencing Day" : "India: Experiencing Night";
        indiaStatus.setAttribute('fill', isDay ? '#fef08a' : '#94a3b8');
    }

    if (status) {
        status.innerHTML = isDay
            ? "<strong>Earth Rotates West-to-East:</strong> India turns toward the Sun and experiences bright daylight!"
            : "<strong>Earth Rotates West-to-East:</strong> India turns away from the Sun into Earth's own shadow, experiencing night!";
    }
}

// SIM 3: Earth's Spin & Solar Tracker
function setSolarHour(hour) {
    const sunOrb = document.getElementById('sim3SunOrb');
    const shadowLine = document.getElementById('poleShadow');
    const dialTime = document.getElementById('dialClockTime');
    const status = document.getElementById('sim3Status');

    if (hour === 6) {
        if (sunOrb) sunOrb.setAttribute('transform', 'translate(80, 140)');
        if (shadowLine) {
            shadowLine.setAttribute('x1', '200');
            shadowLine.setAttribute('y1', '180');
            shadowLine.setAttribute('x2', '310');
            shadowLine.setAttribute('y2', '180');
        }
        if (dialTime) dialTime.textContent = "06:00 AM (Sunrise in East)";
        if (status) status.innerHTML = "<strong>06:00 AM (Morning):</strong> Sun rises in the East due to Earth's eastward spin. The low Sun casts a very long shadow stretching toward the West.";
    } else if (hour === 12) {
        if (sunOrb) sunOrb.setAttribute('transform', 'translate(200, 45)');
        if (shadowLine) {
            shadowLine.setAttribute('x1', '200');
            shadowLine.setAttribute('y1', '180');
            shadowLine.setAttribute('x2', '215');
            shadowLine.setAttribute('y2', '180');
        }
        if (dialTime) dialTime.textContent = "12:00 PM (Noon Overhead)";
        if (status) status.innerHTML = "<strong>12:00 PM (Noon):</strong> The Sun is high directly overhead. Rays strike almost vertically, casting the shortest shadow of the entire day.";
    } else if (hour === 18) {
        if (sunOrb) sunOrb.setAttribute('transform', 'translate(320, 140)');
        if (shadowLine) {
            shadowLine.setAttribute('x1', '200');
            shadowLine.setAttribute('y1', '180');
            shadowLine.setAttribute('x2', '90');
            shadowLine.setAttribute('y2', '180');
        }
        if (dialTime) dialTime.textContent = "06:00 PM (Sunset in West)";
        if (status) status.innerHTML = "<strong>06:00 PM (Evening):</strong> The Sun descends in the West. As the angle drops, the flagpole casts a long shadow stretching toward the East.";
    }
}

// SIM 4: Classroom Seasons' Journal Explorer
function setSeasonsQuarter(quarter) {
    const canvas = document.getElementById('journalStageCanvas');
    const tag = document.getElementById('quarterCardText');
    const status = document.getElementById('sim4Status');
    if (!canvas || !tag) return;

    if (quarter === 'q1') {
        tag.textContent = "Q1: April–June (Peak Summer)";
        canvas.innerHTML = `
            <circle cx="200" cy="50" r="30" fill="#f59e0b" opacity="0.9"/>
            <path d="M120,180 Q160,110 200,105 Q240,110 280,180 Z" fill="#65a30d" opacity="0.85"/>
            <circle cx="170" cy="130" r="8" fill="#fbbf24"/>
            <circle cx="220" cy="125" r="8" fill="#f59e0b"/>
            <circle cx="195" cy="145" r="8" fill="#fbbf24"/>
            <text x="200" y="210" fill="#fed7aa" font-size="10" font-weight="bold" text-anchor="middle">Sweltering Heat, Dry Ground, Ripe Golden Mangoes</text>
        `;
        if (status) status.innerHTML = "<strong>April–June:</strong> Intense solar heat, hot dry winds (Loo), tree leaves dusty, schools close for summer vacation, and sweet mangoes ripen.";
    } else if (quarter === 'q2') {
        tag.textContent = "Q2: July–September (Monsoon Rains)";
        canvas.innerHTML = `
            <ellipse cx="200" cy="45" rx="80" ry="25" fill="#475569" opacity="0.9"/>
            <line x1="160" y1="75" x2="150" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
            <line x1="200" y1="75" x2="190" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
            <line x1="240" y1="75" x2="230" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
            <rect x="80" y="160" width="240" height="30" fill="#0284c7" opacity="0.5"/>
            <text x="200" y="210" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">Dark Nimbus Clouds, Rain Puddles, Lush Green Shoots</text>
        `;
        if (status) status.innerHTML = "<strong>July–September:</strong> Monsoon winds bring heavy downpours, dry earth transforms into vibrant green carpet, and ponds fill with water.";
    } else if (quarter === 'q3') {
        tag.textContent = "Q3: October–December (Autumn & Pre-Winter)";
        canvas.innerHTML = `
            <circle cx="300" cy="50" r="22" fill="#fef08a" opacity="0.85"/>
            <path d="M120,190 Q130,130 115,90" stroke="#84cc16" stroke-width="2.5" fill="none"/>
            <ellipse cx="115" cy="85" rx="7" ry="22" fill="#ffffff"/>
            <path d="M150,190 Q160,125 145,85" stroke="#84cc16" stroke-width="2.5" fill="none"/>
            <ellipse cx="145" cy="80" rx="7" ry="22" fill="#ffffff"/>
            <text x="200" y="210" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Clear Blue Skies, White Kaash Grass, Golden Paddy Fields</text>
        `;
        if (status) status.innerHTML = "<strong>October–December:</strong> Rain clouds vanish leaving sapphire skies. Kaash reeds bloom white, mornings become misty with dew, and paddy crops turn gold.";
    } else if (quarter === 'q4') {
        tag.textContent = "Q4: January–March (Winter & Early Spring)";
        canvas.innerHTML = `
            <polygon points="120,180 180,80 240,180" fill="#334155" opacity="0.6"/>
            <polygon points="150,130 180,80 210,130" fill="#f8fafc" opacity="0.95"/>
            <path d="M280,180 Q285,130 275,100" stroke="#78350f" stroke-width="4" fill="none"/>
            <circle cx="270" cy="95" r="5" fill="#f97316"/>
            <circle cx="285" cy="90" r="5" fill="#ea580c"/>
            <text x="200" y="210" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">Cold Crisp Mornings, Woollen Sweaters, Early Spring Blossoms</text>
        `;
        if (status) status.innerHTML = "<strong>January–March:</strong> Cold chilly days with bonfires and woollens give way to warming sunshine and bright orange Palash flowers in late February.";
    }
}

// SIM 5: Five Ecological Themes Dashboard
function selectTheme(theme) {
    const title = document.getElementById('sim5ThemeTitle');
    const desc = document.getElementById('sim5ThemeDesc');
    const status = document.getElementById('sim5Status');

    if (theme === 'flora') {
        if (title) title.textContent = "Theme 1: Plant Life & Vegetation";
        if (desc) desc.textContent = "Observing leaf shedding in winter, flowering in spring, lush canopy in monsoon, and ripe crops in harvest.";
        if (status) status.innerHTML = "<strong>Flora Theme:</strong> Plants time their leaf budding, flowering, fruit setting, and seed dispersal to match changing heat and rainfall patterns.";
    } else if (theme === 'fauna') {
        if (title) title.textContent = "Theme 2: Birds, Insects & Animals";
        if (desc) desc.textContent = "Noticing Asian Koel singing in mango groves, migratory Siberian cranes arriving in winter, and bullfrogs croaking in rain.";
        if (status) status.innerHTML = "<strong>Fauna Theme:</strong> Animals respond to seasons: birds migrate thousands of miles, bees forage nectar during spring, and bears/snakes hibernate in cold.";
    } else if (theme === 'air') {
        if (title) title.textContent = "Theme 3: Air, Wind & Humidity";
        if (desc) desc.textContent = "Tracking scorching dusty Loo winds in summer, moisture-laden southwest monsoon winds, and chilly dry northern breezes.";
        if (status) status.innerHTML = "<strong>Air Theme:</strong> Wind direction and moisture dictate daily comfort: dry and dusty in May, drenched in July, and calm and crisp in November.";
    } else if (theme === 'sun') {
        if (title) title.textContent = "Theme 4: Sun, Insolation & Heat";
        if (desc) desc.textContent = "Measuring day length (long in summer, short in winter) and intensity of solar heat reaching Earth's surface.";
        if (status) status.innerHTML = "<strong>Sun Theme:</strong> The Sun's midday elevation changes throughout the year, altering the angle and intensity of thermal energy received.";
    } else if (theme === 'human') {
        if (title) title.textContent = "Theme 5: Water Bodies & Human Habits";
        if (desc) desc.textContent = "Observing drying wells in summer, overflowing rivers in monsoon, changing clothing from cotton to wool, and seasonal foods.";
        if (status) status.innerHTML = "<strong>Human Theme:</strong> Humans adapt routines, farm cycles (Kharif, Rabi, Zaid), and celebrate festivals to synchronize with nature's rhythms.";
    }
}

// SIM 6: Vasanta Spring Garden & Koel Song
function bloomPalashFlowers() {
    const palashGroup = document.getElementById('palashFlowersGroup');
    const status = document.getElementById('sim6Status');

    if (palashGroup) {
        palashGroup.classList.toggle('opacity-100');
    }
    if (status) {
        status.innerHTML = "<span class='text-amber-400 font-bold'>Flame of the Forest in Bloom:</span> Fiery orange Palash flowers burst open across deciduous forests, signalling Vasanta Ritu and natural Holi colours!";
    }
}

function playKoelCall() {
    const status = document.getElementById('sim6Status');
    if (status) {
        status.innerHTML = "<span class='text-emerald-400 font-bold'>Asian Koel's Melodious Call:</span> 'Koo-oo, Koo-oo!' The male Asian Koel calls from deep inside mango groves as fresh green leaves and sweet blossoms unfold!";
    }
}

// SIM 7: Grishma Heatwave & Hydration Station
function blowLooWind() {
    const looGraphic = document.getElementById('looWindGusts');
    const status = document.getElementById('sim7Status');

    if (looGraphic) {
        looGraphic.setAttribute('stroke', '#ea580c');
        looGraphic.setAttribute('stroke-width', '3');
        setTimeout(() => {
            looGraphic.setAttribute('stroke', '#f97316');
            looGraphic.setAttribute('stroke-width', '1.5');
        }, 1200);
    }
    if (status) {
        status.innerHTML = "<span class='text-rose-400 font-bold'>Hot Loo Wind Alert:</span> Blistering dry winds blow across Northern and Western India. Stay indoors during afternoon hours to prevent heat stroke!";
    }
}

function drinkCoolingPanna() {
    const status = document.getElementById('sim7Status');
    if (status) {
        status.innerHTML = "<span class='text-amber-300 font-bold'>Hydration Boost:</span> You drank cold Aam Panna and sweet watermelon juice! Rich in electrolytes and vitamin C, cooling drinks keep the body balanced during Grishma.";
    }
}

// SIM 8: Varsha Monsoon Rain Simulator
let isMonsoonRaining = true;
function toggleMonsoonRain() {
    isMonsoonRaining = !isMonsoonRaining;
    const rain = document.getElementById('monsoonRainDrops');
    const status = document.getElementById('sim8Status');

    if (rain) rain.setAttribute('opacity', isMonsoonRaining ? '0.7' : '0');
    if (status) {
        status.innerHTML = isMonsoonRaining
            ? "<strong>Rain Downpour:</strong> Cool raindrops hit warm dry soil, creating the magical sweet aroma of Petrichor! Ponds fill and nature turns emerald green."
            : "<strong>Rainbreak (Cloudy):</strong> The showers pause, leaving humid air, bubbling streams, and sparkling wet leaves.";
    }
}

function triggerFrogCroak() {
    const frog = document.getElementById('monsoonFrog');
    const status = document.getElementById('sim8Status');

    if (frog) {
        frog.setAttribute('transform', 'translate(180, 172) scale(1.1)');
        setTimeout(() => {
            frog.setAttribute('transform', 'translate(180, 180) scale(1)');
        }, 500);
    }
    if (status) {
        status.innerHTML = "<span class='text-lime-400 font-bold'>Bullfrog Chorus:</span> 'Croak-croak-croak!' Bullfrogs rejoice in rain puddles as their breeding season begins during Varsha.";
    }
}

// SIM 9: Sharad Autumn Riverbank & Kash Grass
function swayKaashGrass() {
    const reeds = document.getElementById('kaashReedsLeft');
    const status = document.getElementById('sim9Status');

    if (reeds) {
        reeds.setAttribute('transform', 'skewX(12)');
        setTimeout(() => {
            reeds.setAttribute('transform', 'skewX(-8)');
            setTimeout(() => reeds.setAttribute('transform', 'skewX(0)'), 400);
        }, 400);
    }
    if (status) {
        status.innerHTML = "<span class='text-sky-300 font-bold'>Kaash Reeds Swaying:</span> Silvery white plumes wave along riverbanks beneath deep blue autumn skies, welcoming festive celebrations!";
    }
}

function bloomShiuliFlowers() {
    const fallen = document.getElementById('fallenFlowers');
    const status = document.getElementById('sim9Status');

    if (fallen) {
        fallen.setAttribute('opacity', '1');
    }
    if (status) {
        status.innerHTML = "<span class='text-amber-300 font-bold'>Shiuli (Parijat) Night Bloom:</span> Intensely fragrant white flowers with bright coral-orange stalks bloom under the moonlight and gently carpet the ground at dawn.";
    }
}

// SIM 10: Hemant Pre-Winter Dew & Golden Harvest
function sparkleDewdrops() {
    const dew = document.getElementById('condensingDew');
    const status = document.getElementById('sim10Status');

    if (dew) {
        dew.setAttribute('fill', '#67e8f9');
        dew.setAttribute('stroke-width', '3');
        setTimeout(() => {
            dew.setAttribute('fill', '#38bdf8');
            dew.setAttribute('stroke-width', '1.5');
        }, 800);
    }
    if (status) {
        status.innerHTML = "<span class='text-cyan-300 font-bold'>Dewdrop Condensation:</span> As chilly night air cools, water vapour condenses into sparkling liquid jewels resting on grass tips.";
    }
}

function tasteTilGurSweet() {
    const status = document.getElementById('sim10Status');
    if (status) {
        status.innerHTML = "<span class='text-amber-400 font-bold'>Traditional Warmth:</span> Til (sesame seeds) and Gur (jaggery) provide essential healthy fats and warmth to nourish the body as winter approaches.";
    }
}

// SIM 11: Shishir Winter Chill & Immunity Pantry
function stokeWinterBonfire() {
    const status = document.getElementById('sim11Status');
    if (status) {
        status.innerHTML = "<span class='text-orange-400 font-bold'>Bonfire Roaring:</span> Families gather around glowing evening fires to stay warm and share folk stories during cold winter nights.";
    }
}

function inspectImmunityFoods() {
    const status = document.getElementById('sim11Status');
    if (status) {
        status.innerHTML = "<span class='text-emerald-300 font-bold'>Winter Immunity:</span> Sarson ka Saag (mustard greens), Amla (rich in Vitamin C), and juicy oranges strengthen immune defense against cold weather ailments.";
    }
}

// SIM 12: Pan-India Regional Climatic Contrasts
function selectRegion(reg) {
    const title = document.getElementById('regCardTitle');
    const d1 = document.getElementById('regCardDesc1');
    const d2 = document.getElementById('regCardDesc2');
    const d3 = document.getElementById('regCardDesc3');
    const status = document.getElementById('sim12Status');

    if (reg === 'kashmir') {
        if (title) title.textContent = "Kashmir Himalayas";
        if (d1) d1.textContent = "• Sub-zero snowy winter";
        if (d2) d2.textContent = "• Pheran & Kangri fire pot";
        if (d3) d3.textContent = "• Insulated timber homes";
        if (status) status.innerHTML = "<strong>Kashmir & Ladakh:</strong> Chilly mountain winters freeze lakes. People wear woollen Pherans with Kangri pots (charcoal braziers) underneath for portable warmth!";
    } else if (reg === 'rajasthan') {
        if (title) title.textContent = "Rajasthan Thar Desert";
        if (d1) d1.textContent = "• Blistering summer 48°C";
        if (d2) d2.textContent = "• Thick mud insulating walls";
        if (d3) d3.textContent = "• Night-time rapid cooling";
        if (status) status.innerHTML = "<strong>Thar Desert (Rajasthan):</strong> Extreme temperature swings! Sand heats up rapidly during daytime and cools down fast at night. Thick mud walls keep homes cool in day and warm at night.";
    } else if (reg === 'meghalaya') {
        if (title) title.textContent = "Meghalaya (Mawsynram)";
        if (d1) d1.textContent = "• Wettest place on Earth";
        if (d2) d2.textContent = "• Over 11,800 mm rain/year";
        if (d3) d3.textContent = "• Knup bamboo-leaf umbrellas";
        if (status) status.innerHTML = "<strong>Mawsynram (Meghalaya):</strong> World-record rainfall! Locals weave full-body turtle-shell shaped rain-shields called 'Knups' from bamboo and palm leaves to work in heavy downpours.";
    } else if (reg === 'kerala') {
        if (title) title.textContent = "Kerala Coastal Tropics";
        if (d1) d1.textContent = "• Warm humid climate year-round";
        if (d2) d2.textContent = "• Breathable airy cottons";
        if (d3) d3.textContent = "• Twin monsoons (June & Oct)";
        if (status) status.innerHTML = "<strong>Kerala & Coastal South:</strong> The nearby Arabian Sea prevents extreme cold. Temperatures stay moderate (25–32°C), and people wear light cottons year-round.";
    }
}

// SIM 13: Agricultural Cropping Triad (Kharif, Rabi, Zaid)
function selectCropPattern(pattern) {
    const graphic = document.getElementById('cropStageGraphic');
    const title = document.getElementById('cropTitle');
    const timing = document.getElementById('cropTiming');
    const status = document.getElementById('sim13Status');

    if (pattern === 'kharif') {
        if (title) title.textContent = "Kharif Season";
        if (timing) timing.textContent = "Sown: June | Harvest: Oct";
        if (graphic) {
            graphic.innerHTML = `
                <circle cx="200" cy="40" r="22" fill="#475569"/>
                <circle cx="225" cy="35" r="26" fill="#64748b"/>
                <circle cx="175" cy="40" r="20" fill="#475569"/>
                <rect x="50" y="150" width="300" height="20" fill="#0284c7" opacity="0.4"/>
                <path d="M120,165 Q110,120 95,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M120,165 Q130,115 145,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M200,165 Q190,115 175,90" stroke="#16a34a" stroke-width="3" fill="none"/>
                <path d="M200,165 Q210,110 225,90" stroke="#16a34a" stroke-width="3" fill="none"/>
                <path d="M280,165 Q270,120 255,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M280,165 Q290,115 305,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <text x="200" y="195" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Kharif: Water-Hungry Paddy & Cotton</text>
            `;
        }
        if (status) status.innerHTML = "<strong>Kharif Crops:</strong> Planted with monsoon onset (June–July) and harvested in autumn (Sept–Oct). Examples: Rice (paddy), maize, soybean, and cotton.";
    } else if (pattern === 'rabi') {
        if (title) title.textContent = "Rabi Season";
        if (timing) timing.textContent = "Sown: Oct–Nov | Harvest: Mar–Apr";
        if (graphic) {
            graphic.innerHTML = `
                <circle cx="200" cy="40" r="20" fill="#fef08a" opacity="0.8"/>
                <path d="M120,165 Q120,120 120,80" stroke="#eab308" stroke-width="3" fill="none"/>
                <path d="M200,165 Q200,115 200,75" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M280,165 Q280,120 280,80" stroke="#eab308" stroke-width="3" fill="none"/>
                <circle cx="160" cy="110" r="7" fill="#fde047"/>
                <circle cx="240" cy="110" r="7" fill="#fde047"/>
                <text x="200" y="195" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Rabi: Golden Wheat, Mustard & Green Gram</text>
            `;
        }
        if (status) status.innerHTML = "<strong>Rabi Crops:</strong> Planted in post-monsoon chill (Oct–Nov) and harvested in spring (March–April). Examples: Wheat, barley, mustard, and chickpeas (gram).";
    } else if (pattern === 'zaid') {
        if (title) title.textContent = "Zaid Season";
        if (timing) timing.textContent = "Sown: March | Harvest: June";
        if (graphic) {
            graphic.innerHTML = `
                <circle cx="200" cy="40" r="28" fill="#f59e0b" opacity="0.9"/>
                <path d="M80,160 Q200,130 320,160" stroke="#22c55e" stroke-width="3.5" fill="none"/>
                <ellipse cx="150" cy="155" rx="18" ry="14" fill="#15803d" stroke="#166534" stroke-width="2"/>
                <line x1="140" y1="145" x2="140" y2="165" stroke="#4ade80" stroke-width="1.5"/>
                <line x1="150" y1="143" x2="150" y2="167" stroke="#4ade80" stroke-width="1.5"/>
                <line x1="160" y1="145" x2="160" y2="165" stroke="#4ade80" stroke-width="1.5"/>
                <ellipse cx="250" cy="158" rx="14" ry="7" fill="#84cc16"/>
                <text x="200" y="195" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Zaid: Refreshing Watermelon, Cucumber & Muskmelon</text>
            `;
        }
        if (status) status.innerHTML = "<strong>Zaid Crops:</strong> Short summer gap season (March–June) growing refreshing, high-water fruits and vegetables like watermelon, cucumber, and bitter gourd.";
    }
}

// SIM 14: Pan-Indian Harvest Festival Wheel
function displayFestival(fest) {
    const graphic = document.getElementById('festGraphic');
    const name = document.getElementById('festName');
    const region = document.getElementById('festRegion');
    const custom = document.getElementById('festCustom');
    const status = document.getElementById('sim14Status');

    if (fest === 'sankranti') {
        if (name) name.textContent = "Makar Sankranti";
        if (region) region.textContent = "Across India (January)";
        if (custom) custom.textContent = "Flying Kites & Til-Gur";
        if (graphic) {
            graphic.innerHTML = `
                <polygon points="67,25 90,50 67,75 44,50" fill="#ef4444" stroke="#fbbf24" stroke-width="1.5"/>
                <line x1="67" y1="25" x2="67" y2="75" stroke="#ffffff" stroke-width="1"/>
                <line x1="44" y1="50" x2="90" y2="50" stroke="#ffffff" stroke-width="1"/>
            `;
        }
        if (status) status.innerHTML = "<strong>Makar Sankranti:</strong> Marks the Sun's northward movement (Uttarayana). Celebrated with colorful kite flying, sesame chikki, and thanking nature for winter grains.";
    } else if (fest === 'pongal') {
        if (name) name.textContent = "Thai Pongal";
        if (region) region.textContent = "Tamil Nadu (January)";
        if (custom) custom.textContent = "Boiling Sweet Rice & Cane";
        if (graphic) {
            graphic.innerHTML = `
                <ellipse cx="67" cy="65" rx="20" ry="14" fill="#b45309" stroke="#78350f" stroke-width="1.5"/>
                <path d="M52,58 Q67,45 82,58 Z" fill="#ffffff"/>
                <text x="67" y="48" fill="#fef08a" font-size="7" font-weight="bold" text-anchor="middle">"Pongalo Pongal!"</text>
            `;
        }
        if (status) status.innerHTML = "<strong>Pongal:</strong> A four-day thanksgiving festival in Tamil Nadu where fresh harvested rice and jaggery are boiled in clay pots until it overflows, shouting 'Pongalo Pongal!'";
    } else if (fest === 'lohri') {
        if (name) name.textContent = "Lohri Festival";
        if (region) region.textContent = "Punjab & North India (Jan)";
        if (custom) custom.textContent = "Bonfires, Rewari & Bhangra";
        if (graphic) {
            graphic.innerHTML = `
                <line x1="50" y1="75" x2="84" y2="65" stroke="#78350f" stroke-width="4"/>
                <line x1="50" y1="65" x2="84" y2="75" stroke="#78350f" stroke-width="4"/>
                <path d="M67,70 Q55,40 67,25 Q79,40 67,70 Z" fill="#f97316"/>
                <circle cx="67" cy="55" r="6" fill="#fde047"/>
            `;
        }
        if (status) status.innerHTML = "<strong>Lohri:</strong> Marks the end of winter chill and the ripening of Rabi crops. Families circle bonfires, offering peanuts, sesame, and puffed rice while dancing to drum beats.";
    } else if (fest === 'bihu') {
        if (name) name.textContent = "Magh Bihu (Bhogali)";
        if (region) region.textContent = "Assam (January)";
        if (custom) custom.textContent = "Bhelaghar & Pitha Feasts";
        if (graphic) {
            graphic.innerHTML = `
                <polygon points="67,30 45,60 89,60" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
                <rect x="52" y="60" width="30" height="25" fill="#a16207"/>
                <rect x="62" y="70" width="10" height="15" fill="#451a03"/>
            `;
        }
        if (status) status.innerHTML = "<strong>Magh Bihu:</strong> Assam's feast of plenty after harvesting paddy. Communities build tall thatched huts called Bhelaghar and Meji, enjoying traditional rice cakes (Pitha).";
    }
}

// SIM 15: Ritucharya Seasonal Lifestyle Matcher
function setLifestyleMode(mode) {
    const charTorso = document.getElementById('charTorso');
    const status = document.getElementById('sim15Status');

    if (mode === 'summer') {
        if (charTorso) {
            charTorso.setAttribute('fill', '#ffffff');
            charTorso.setAttribute('stroke', '#38bdf8');
        }
        if (status) {
            status.innerHTML = "<strong>Grishma (Summer Adaptation):</strong> Wear light, loose, white cotton clothes that reflect heat and absorb perspiration. Sip cooling buttermilk and rest during midday heat!";
        }
    } else if (mode === 'winter') {
        if (charTorso) {
            charTorso.setAttribute('fill', '#dc2626');
            charTorso.setAttribute('stroke', '#991b1b');
        }
        if (status) {
            status.innerHTML = "<strong>Shishir (Winter Adaptation):</strong> Wear layered woollens that trap warm air pockets. Eat nourishing warm meals with bajra roti, pure ghee, sesame, and ginger!";
        }
    }
}

// SIM 16: Nature's Harmony (The Eternal Cycle of Seasons)
let currentCosmicSeason = 1;
const seasonNames = [
    "Vasanta (Spring - Blossom & Growth)",
    "Grishma (Summer - Sun Energy & Heat)",
    "Varsha (Monsoon - Life-Giving Water)",
    "Sharad (Autumn - Clear Sapphire Skies)",
    "Hemant (Pre-Winter - Dew & Harvest)",
    "Shishir (Winter - Rest & Resilience)"
];
let cosmicAutoTimer = null;

function jumpToSeasonCycle(idx) {
    currentCosmicSeason = idx;
    const tag = document.getElementById('seasonCycleName');
    const mandala = document.getElementById('cosmicMandala');
    const status = document.getElementById('sim16Status');

    if (tag) tag.textContent = seasonNames[idx - 1];
    if (mandala) {
        const rot = (idx - 1) * 60;
        mandala.setAttribute('transform', `translate(200, 120) rotate(${rot})`);
    }
    if (status) {
        status.innerHTML = `<strong>Season ${idx} of 6: ${seasonNames[idx - 1]}</strong> - Every season plays an irreplaceable role in maintaining life on Earth!`;
    }
}

function stepNextSeasonCycle() {
    currentCosmicSeason = (currentCosmicSeason % 6) + 1;
    jumpToSeasonCycle(currentCosmicSeason);
}

function toggleSeasonalAutoSpin() {
    const status = document.getElementById('sim16Status');
    if (cosmicAutoTimer) {
        clearInterval(cosmicAutoTimer);
        cosmicAutoTimer = null;
        if (status) status.innerHTML = "<strong>Auto-Spin Paused:</strong> Use the step button or click nodes to explore each season manually.";
    } else {
        cosmicAutoTimer = setInterval(stepNextSeasonCycle, 1500);
        if (status) status.innerHTML = "<span class='text-purple-300 font-bold'>Cosmic Wheel Revolving:</span> Witnessing the eternal unbroken rhythm of nature across the six seasons!";
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

"""
Interactive JavaScript Engine for NCERT Class 5 Science Chapter 8: Clothes - How Things are Made
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

// =========================================================================
// 16 BESPOKE SIMULATOR INTERACTIVE ENGINES
// =========================================================================

// SIM 1: Baya Weaver Nest
function setSim1Stage(stage) {
    const lbl = document.getElementById('sim1StageLabel');
    const exp = document.getElementById('sim1Explanation');
    const tube = document.getElementById('nestTubeGroup');
    const body = document.getElementById('nestBody');
    const bird = document.getElementById('bayaBird');

    if (stage === 1) {
        if (lbl) lbl.textContent = "Stage 1: Suspended Loop";
        if (tube) tube.style.opacity = '0.1';
        if (body) body.style.opacity = '0.3';
        if (bird) bird.setAttribute('transform', 'translate(170, 45)');
        if (exp) exp.innerHTML = "<strong>Stage 1:</strong> The male baya weaver secures strong grass fibres to a drooping branch, fashioning a sturdy vertical suspension ring.";
    } else if (stage === 2) {
        if (lbl) lbl.textContent = "Stage 2: Interlaced Chamber";
        if (tube) tube.style.opacity = '0.2';
        if (body) body.style.opacity = '0.85';
        if (bird) bird.setAttribute('transform', 'translate(230, 95)');
        if (exp) exp.innerHTML = "<strong>Stage 2:</strong> By weaving crosswise ribbons over and under the vertical strands, it forms a rounded central egg pouch.";
    } else if (stage === 3) {
        if (lbl) lbl.textContent = "Stage 3: Downward Entrance Tube";
        if (tube) tube.style.opacity = '1';
        if (body) body.style.opacity = '1';
        if (bird) bird.setAttribute('transform', 'translate(225, 175)');
        if (exp) exp.innerHTML = "<strong>Stage 3:</strong> A long vertical woven cylinder is added to the bottom, allowing the birds to enter while locking out tree snakes and crows!";
    }
}

// SIM 2: Warp and Weft Loom Grid
let sim2RowsWoven = 3;
function stepSim2Weave() {
    const weftGroup = document.getElementById('sim2WeftGroup');
    const shuttle = document.getElementById('sim2Shuttle');
    const status = document.getElementById('sim2Status');

    if (!weftGroup) return;

    sim2RowsWoven++;
    const yPos = 60 + (sim2RowsWoven - 1) * 22;

    if (yPos > 200) {
        if (status) status.innerHTML = "<span class='text-emerald-400 font-bold'>Fabric Complete:</span> The loom grid is densely woven! Press 'Reset Loom' to weave again.";
        return;
    }

    const newPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    newPath.setAttribute('d', `M 70,${yPos} L 320,${yPos}`);
    newPath.setAttribute('stroke', sim2RowsWoven % 2 === 0 ? '#f59e0b' : '#ea580c');
    newPath.setAttribute('stroke-width', '5');
    newPath.setAttribute('stroke-linecap', 'round');
    newPath.setAttribute('stroke-dasharray', '15,15');
    if (sim2RowsWoven % 2 === 0) {
        newPath.setAttribute('stroke-dashoffset', '15');
    }
    weftGroup.appendChild(newPath);

    if (shuttle) {
        shuttle.setAttribute('transform', `translate(210, ${yPos})`);
    }

    if (status) {
        status.innerHTML = `<strong>Row ${sim2RowsWoven} inserted:</strong> Shuttle moved through shed, trapping warp threads with alternating over-under tension!`;
    }
}

function resetSim2Loom() {
    sim2RowsWoven = 0;
    const weftGroup = document.getElementById('sim2WeftGroup');
    const shuttle = document.getElementById('sim2Shuttle');
    const status = document.getElementById('sim2Status');
    if (weftGroup) weftGroup.innerHTML = '';
    if (shuttle) shuttle.setAttribute('transform', 'translate(100, 60)');
    if (status) status.innerHTML = "Loom reset. Click 'Throw Shuttle' to begin inserting weft rows over and under the vertical blue warp threads.";
}

// SIM 3: Handloom Heritage Atlas
function selectHandloom(region) {
    const title = document.getElementById('swatchTitle');
    const origin = document.getElementById('swatchOrigin');
    const fibre = document.getElementById('swatchFibre');
    const feature = document.getElementById('swatchFeature');
    const details = document.getElementById('sim3Details');

    if (region === 'kanjeevaram') {
        if (title) title.textContent = "Kanjeevaram";
        if (origin) origin.textContent = "Kanchipuram, Tamil Nadu";
        if (fibre) fibre.textContent = "Mulberry Silk + Zari";
        if (feature) feature.textContent = "Interlocking Temple Borders";
        if (details) details.innerHTML = "<strong>Kanjeevaram (Tamil Nadu):</strong> Woven on traditional pit looms with 3 shuttle weavers joining vibrant body silk with gold-wrapped zari temple borders.";
    } else if (region === 'pashmina') {
        if (title) title.textContent = "Pashmina";
        if (origin) origin.textContent = "Ladakh / Kashmir";
        if (fibre) fibre.textContent = "Changthangi Goat Down";
        if (feature) feature.textContent = "Ultra-fine 12-micron warmth";
        if (details) details.innerHTML = "<strong>Pashmina (Kashmir):</strong> Combed gently from mountain goats at -40 °C, spun by Kashmiri artisans on delicate taklis and woven into feather-light warm shawls.";
    } else if (region === 'ikat') {
        if (title) title.textContent = "Ikat (Bandha)";
        if (origin) origin.textContent = "Odisha & Gujarat";
        if (fibre) fibre.textContent = "Tie-Dyed Cotton / Silk";
        if (feature) feature.textContent = "Soft feathered geometric motifs";
        if (details) details.innerHTML = "<strong>Ikat (Odisha / Gujarat):</strong> Yarn bundles are tied and dyed with mathematical precision BEFORE weaving, creating soft feathered patterns as threads interlock.";
    }
}

// SIM 4: Charkha Spinning
let charkhaAngle = 0;
function updateCharkhaSpeed(val) {
    const speed = parseInt(val, 10);
    const speedText = document.getElementById('speedDisplay');
    const wheel = document.getElementById('charkhaWheel');
    const gauge = document.getElementById('gaugeBar');
    const gaugeText = document.getElementById('gaugeText');
    const status = document.getElementById('sim4Status');

    if (speedText) speedText.textContent = `${speed} rpm`;

    if (wheel) {
        charkhaAngle += speed * 2;
        wheel.setAttribute('transform', `translate(115, 120) rotate(${charkhaAngle})`);
    }

    const tensile = Math.min(100, Math.round(speed * 0.95 + 10));
    if (gauge) gauge.setAttribute('width', `${tensile * 1.1}`);
    if (gaugeText) gaugeText.textContent = `${tensile}% Tensile`;

    if (status) {
        if (speed === 0) {
            status.innerHTML = "<span class='text-slate-400'>Wheel motionless:</span> Without spinning, cotton sliver fibres slide apart under the slightest pull.";
        } else if (speed < 40) {
            status.innerHTML = "<span class='text-amber-400'>Gentle twist:</span> Fibres are starting to align, generating moderate friction.";
        } else {
            status.innerHTML = "<span class='text-emerald-400 font-bold'>Optimal twist:</span> High-speed friction packs fibres into a strong, unbreakable yarn ready for the loom!";
        }
    }
}

// SIM 5: Natural Fibre Micro-Lab
function viewFibre(type) {
    const view = document.getElementById('microscopeFibreView');
    const name = document.getElementById('fibreNameTag');
    const origin = document.getElementById('fibreOriginTag');
    const exp = document.getElementById('sim5Explanation');

    if (!view) return;

    if (type === 'cotton') {
        view.innerHTML = `
            <path d="M 125,60 Q 155,90 145,120 Q 135,150 165,180" stroke="#f8fafc" stroke-width="14" stroke-linecap="round" fill="none"/>
            <path d="M 125,60 Q 155,90 145,120 Q 135,150 165,180" stroke="#cbd5e1" stroke-width="4" stroke-dasharray="10,8" fill="none"/>
            <path d="M 235,60 Q 255,90 245,130 Q 235,160 265,180" stroke="#f8fafc" stroke-width="12" stroke-linecap="round" fill="none"/>
        `;
        if (name) name.textContent = "Cotton Fibre";
        if (origin) origin.textContent = "Plant Seed Pod (Cellulose)";
        if (exp) exp.innerHTML = "<strong>Cotton:</strong> Twisted hollow ribbon structure (convolutions) allows natural air flow and absorbs body perspiration.";
    } else if (type === 'linen') {
        view.innerHTML = `
            <line x1="150" y1="50" x2="150" y2="190" stroke="#e2e8f0" stroke-width="12" stroke-linecap="round"/>
            <line x1="144" y1="80" x2="156" y2="80" stroke="#94a3b8" stroke-width="3"/>
            <line x1="144" y1="120" x2="156" y2="120" stroke="#94a3b8" stroke-width="3"/>
            <line x1="144" y1="160" x2="156" y2="160" stroke="#94a3b8" stroke-width="3"/>
            <line x1="240" y1="50" x2="240" y2="190" stroke="#e2e8f0" stroke-width="10" stroke-linecap="round"/>
        `;
        if (name) name.textContent = "Linen / Flax";
        if (origin) origin.textContent = "Plant Stem Bast (Cellulose)";
        if (exp) exp.innerHTML = "<strong>Linen (Flax):</strong> Straight, smooth polygonal fibres with bamboo-like cross-nodes. Extremely strong and cool against the skin.";
    } else if (type === 'wool') {
        view.innerHTML = `
            <path d="M 150,55 Q 170,85 140,115 Q 165,145 145,185" stroke="#fef08a" stroke-width="15" stroke-linecap="round" fill="none"/>
            <path d="M 142,75 L 158,75 M 138,105 L 154,105 M 144,135 L 160,135 M 140,165 L 156,165" stroke="#ca8a04" stroke-width="2.5"/>
            <path d="M 235,55 Q 215,95 240,135 Q 220,165 240,185" stroke="#fef08a" stroke-width="13" stroke-linecap="round" fill="none"/>
        `;
        if (name) name.textContent = "Wool Fibre";
        if (origin) origin.textContent = "Sheep Fleece (Keratin Protein)";
        if (exp) exp.innerHTML = "<strong>Wool:</strong> Wavy crimped fibres coated in microscopic scales trap millions of dead-air pockets, providing superb thermal insulation.";
    } else if (type === 'silk') {
        view.innerHTML = `
            <path d="M 140,50 Q 150,120 140,190" stroke="#fde047" stroke-width="8" stroke-linecap="round" fill="none"/>
            <path d="M 170,50 Q 160,120 170,190" stroke="#ffffff" stroke-width="7" stroke-linecap="round" fill="none"/>
            <polygon points="230,80 250,70 240,150 220,160" fill="#fef9c3" stroke="#facc15" stroke-width="1.5"/>
        `;
        if (name) name.textContent = "Mulberry Silk";
        if (origin) origin.textContent = "Caterpillar Cocoon (Fibroin Protein)";
        if (exp) exp.innerHTML = "<strong>Silk:</strong> Smooth triangular prism cross-section refracts incoming light at different angles, creating its celebrated natural pearl lustre.";
    }
}

// SIM 6: Silkworm Metamorphosis
function setSilkStage(stage) {
    const canvas = document.getElementById('silkwormStageCanvas');
    const title = document.getElementById('silkStageTitle');
    const len = document.getElementById('filamentLengthText');
    const desc = document.getElementById('sim6Description');

    if (!canvas) return;

    if (stage === 1) {
        canvas.innerHTML = `
            <ellipse cx="200" cy="140" rx="90" ry="50" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
            <circle cx="180" cy="130" r="4" fill="#fef08a" stroke="#ca8a04"/>
            <circle cx="190" cy="135" r="4" fill="#fef08a" stroke="#ca8a04"/>
            <circle cx="205" cy="132" r="4" fill="#fef08a" stroke="#ca8a04"/>
            <circle cx="215" cy="138" r="4" fill="#fef08a" stroke="#ca8a04"/>
            <circle cx="195" cy="145" r="4" fill="#fef08a" stroke="#ca8a04"/>
        `;
        if (title) title.textContent = "1. Silkworm Eggs";
        if (len) len.textContent = "0 Metres";
        if (desc) desc.innerHTML = "<strong>Stage 1 (Egg):</strong> Female silk moth lays 300 to 500 tiny eggs on fresh mulberry leaves, each no larger than a pinhead.";
    } else if (stage === 2) {
        canvas.innerHTML = `
            <path d="M 60,190 Q 200,60 340,190 Q 200,240 60,190" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
            <g id="caterpillarBody" transform="translate(130, 115)">
                <circle cx="20" cy="20" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="42" cy="22" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="64" cy="20" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="86" cy="18" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="108" cy="15" r="12" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="112" cy="13" r="2.5" fill="#0f172a"/>
            </g>
        `;
        if (title) title.textContent = "2. Voracious Larva";
        if (len) len.textContent = "Growing";
        if (desc) desc.innerHTML = "<strong>Stage 2 (Larva):</strong> The caterpillar feeds day and night on chopped mulberry leaves, molting 4 times as it grows 10,000 times heavier!";
    } else if (stage === 3) {
        canvas.innerHTML = `
            <ellipse cx="200" cy="120" rx="45" ry="60" fill="#fef08a" stroke="#eab308" stroke-width="3"/>
            <path d="M 170,90 Q 200,70 230,90 Q 240,120 230,150 Q 200,170 170,150 Q 160,120 170,90" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,4"/>
            <path d="M 230,90 Q 280,60 310,35" stroke="#facc15" stroke-width="2" stroke-dasharray="3,2"/>
        `;
        if (title) title.textContent = "3. Silk Cocoon";
        if (len) len.textContent = "Up to 1,000 Metres";
        if (desc) desc.innerHTML = "<strong>Stage 3 (Pupa):</strong> Moving its head in figure-8s, the caterpillar spins a continuous silk thread up to 1 kilometre long around itself.";
    } else if (stage === 4) {
        canvas.innerHTML = `
            <ellipse cx="200" cy="130" rx="15" ry="28" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
            <line x1="195" y1="105" x2="185" y2="85" stroke="#ca8a04" stroke-width="2"/>
            <line x1="205" y1="105" x2="215" y2="85" stroke="#ca8a04" stroke-width="2"/>
            <path d="M 190,120 Q 130,80 120,130 Q 160,150 190,135 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <path d="M 210,120 Q 270,80 280,130 Q 240,150 210,135 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
        `;
        if (title) title.textContent = "4. Adult Silk Moth";
        if (len) len.textContent = "New Generation";
        if (desc) desc.innerHTML = "<strong>Stage 4 (Adult Moth):</strong> The moth emerges to mate and lay eggs, continuing nature's miraculous life cycle.";
    }
}

// SIM 7: Thermal Safety Duel
function testSafetyReaction(type) {
    const status = document.getElementById('sim7Status');
    if (!status) return;

    if (type === 'cotton') {
        status.innerHTML = "<span class='text-emerald-400 font-bold'>Natural Cotton:</span> Chars cleanly into harmless powdery ash. It does NOT melt or drip, making it safe to wear in kitchens and laboratories.";
    } else {
        status.innerHTML = "<span class='text-rose-400 font-bold'>Synthetic Polyester:</span> Melts into hot viscous molten plastic that sticks tightly to human skin. NEVER wear synthetic clothes near open fire or firecrackers!";
    }
}

// SIM 8: Common Tailorbird Leaf Stitcher
let tailorbirdStitchCount = 5;
function addTailorbirdStitch() {
    tailorbirdStitchCount++;
    const status = document.getElementById('sim8Status');
    if (status) {
        status.innerHTML = `<span class='text-lime-400 font-bold'>Stitch ${tailorbirdStitchCount} completed:</span> Punctured leaf eyelet, pulled spider-silk strand, and knotted exterior rivet securely!`;
    }
}

function resetTailorbirdStitches() {
    tailorbirdStitchCount = 0;
    const status = document.getElementById('sim8Status');
    if (status) {
        status.innerHTML = "Fresh green leaves positioned. Click 'Pierce Eyelet & Thread Stitch' to start sewing.";
    }
}

// SIM 9: Running Stitch Master
let runningStitchStep = 4;
function advanceRunningStitch() {
    runningStitchStep++;
    const countText = document.getElementById('stitchCountText');
    const needle = document.getElementById('activeNeedle');
    const status = document.getElementById('sim9Status');

    if (countText) countText.textContent = `Stitch ${runningStitchStep}: In-Out Rhythm`;
    if (needle) {
        const yOffset = 165 + (runningStitchStep - 4) * 10;
        needle.setAttribute('transform', `translate(190, ${Math.min(210, yOffset)})`);
    }

    if (status) {
        status.innerHTML = `<span class='text-teal-400 font-bold'>Running Stitch ${runningStitchStep}:</span> Needle drives down through both layers and emerges on the other side, locking tailor scraps firmly!`;
    }
}

function resetRunningStitch() {
    runningStitchStep = 0;
    const countText = document.getElementById('stitchCountText');
    const status = document.getElementById('sim9Status');
    if (countText) countText.textContent = "Ready to Stitch";
    if (status) status.innerHTML = "Fabric layers aligned. Click 'Drive Needle' to sew the running stitch seam.";
}

// SIM 10: Chikankari & Banjara Mirror Studio
function switchCraftMode(mode) {
    const canvas = document.getElementById('craftStudioContent');
    const tag = document.getElementById('craftStudioTag');
    const desc = document.getElementById('sim10Description');

    if (!canvas) return;

    if (mode === 'chikankari') {
        if (tag) tag.textContent = "CHIKANKARI MODE";
        canvas.innerHTML = `
            <rect x="70" y="25" width="260" height="190" rx="8" fill="#1e293b" stroke="#e2e8f0" stroke-width="1.5"/>
            <rect x="75" y="30" width="250" height="180" rx="6" fill="#f8fafc" opacity="0.15"/>
            <path d="M 200,60 C 160,80 160,140 200,165 C 240,140 240,80 200,60 Z" fill="#ffffff" opacity="0.3" stroke="#ffffff" stroke-width="2"/>
            <path d="M 180,90 L 220,110 M 180,110 L 220,90 M 180,110 L 220,130 M 180,130 L 220,110" stroke="#f8fafc" stroke-width="2.5" opacity="0.6"/>
            <circle cx="200" cy="110" r="3" fill="#ffffff"/>
            <circle cx="200" cy="125" r="3" fill="#ffffff"/>
            <text x="200" y="195" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Lucknow Chikankari: Bakhiya Shadow Work</text>
        `;
        if (desc) desc.innerHTML = "<strong>Bakhiya (Shadow Stitch):</strong> Crisscross herringbone stitches worked on the reverse of sheer muslin create a softly shaded silhouette on the front.";
    } else {
        if (tag) tag.textContent = "BANJARA MODE";
        canvas.innerHTML = `
            <rect x="70" y="25" width="260" height="190" rx="8" fill="#991b1b" stroke="#f59e0b" stroke-width="2"/>
            <circle cx="200" cy="115" r="32" fill="#e2e8f0" stroke="#facc15" stroke-width="4"/>
            <circle cx="200" cy="115" r="28" fill="#38bdf8" opacity="0.35"/>
            <line x1="200" y1="83" x2="200" y2="75" stroke="#fef08a" stroke-width="3"/>
            <line x1="200" y1="147" x2="200" y2="155" stroke="#fef08a" stroke-width="3"/>
            <line x1="168" y1="115" x2="160" y2="115" stroke="#fef08a" stroke-width="3"/>
            <line x1="232" y1="115" x2="240" y2="115" stroke="#fef08a" stroke-width="3"/>
            <text x="200" y="195" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Banjara Mirror Work: Shisha Embroidery</text>
        `;
        if (desc) desc.innerHTML = "<strong>Banjara Mirror Work:</strong> Artisans securely encase circular glass mirrors inside tight buttonhole stitches to reflect the desert sun and ward off evil spirits.";
    }
}

// SIM 11: Kantha Quilt & Gota Patti
function switchSim11(mode) {
    const canvas = document.getElementById('sim11Canvas');
    const status = document.getElementById('sim11Status');
    if (!canvas) return;

    if (mode === 'kantha') {
        canvas.innerHTML = `
            <rect x="50" y="40" width="200" height="150" fill="#dc2626" opacity="0.3" transform="rotate(-3 150 115)"/>
            <rect x="50" y="40" width="200" height="150" fill="#2563eb" opacity="0.4" transform="rotate(2 150 115)"/>
            <rect x="50" y="40" width="200" height="150" fill="#f59e0b" opacity="0.5"/>
            <path d="M 60,60 Q 150,55 240,60 M 60,75 Q 150,70 240,75 M 60,90 Q 150,85 240,90 M 60,105 Q 150,100 240,105 M 60,120 Q 150,115 240,120 M 60,135 Q 150,130 240,135 M 60,150 Q 150,145 240,150" stroke="#fef08a" stroke-width="1.8" stroke-dasharray="5,4" fill="none"/>
            <path d="M 150,115 C 135,95 165,95 150,115 Z" fill="#ffffff" stroke="#e11d48" stroke-width="1.5"/>
        `;
        if (status) status.innerHTML = "<strong>Kantha (Bengal / Odisha):</strong> Thousands of tiny running stitches hold 4 to 6 worn sarees together, creating cozy, breathable ripple-textured quilts.";
    } else {
        canvas.innerHTML = `
            <rect x="50" y="40" width="200" height="150" fill="#881337" stroke="#e11d48" stroke-width="2"/>
            <polygon points="150,70 170,100 150,130 130,100" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
            <polygon points="110,115 130,135 110,155 90,135" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
            <polygon points="190,115 210,135 190,155 170,135" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
            <circle cx="150" cy="100" r="6" fill="#ea580c"/>
        `;
        if (status) status.innerHTML = "<strong>Gota Patti (Rajasthan):</strong> Metallic ribbons (gota) folded into delicate flower petals (patti) and stitched down onto vibrant silks.";
    }
}

// SIM 12: Phulkari & Toda Shawl
function switchSim12(mode) {
    const canvas = document.getElementById('sim12Canvas');
    const tag = document.getElementById('sim12ModeTag');
    const status = document.getElementById('sim12Status');
    if (!canvas) return;

    if (mode === 'phulkari') {
        if (tag) tag.textContent = "PHULKARI";
        canvas.innerHTML = `
            <rect x="60" y="25" width="280" height="190" rx="8" fill="#451a03" stroke="#78350f" stroke-width="2"/>
            <polygon points="200,60 250,120 200,180 150,120" fill="#f59e0b" stroke="#ea580c" stroke-width="2"/>
            <polygon points="200,80 230,120 200,160 170,120" fill="#e11d48" stroke="#be123c" stroke-width="1.5"/>
            <text x="200" y="200" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Punjab Phulkari: Reverse Darning Stitch (Bagh)</text>
        `;
        if (status) status.innerHTML = "<strong>Phulkari (Punjab):</strong> Embroidered with bright silk floss (pat) from the reverse side of coarse khaddar cotton.";
    } else {
        if (tag) tag.textContent = "TODA SHAWL";
        canvas.innerHTML = `
            <rect x="60" y="25" width="280" height="190" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
            <rect x="80" y="50" width="240" height="20" fill="#dc2626"/>
            <rect x="80" y="75" width="240" height="20" fill="#0f172a"/>
            <polygon points="170,140 200,105 230,140" fill="#dc2626"/>
            <polygon points="180,140 200,115 220,140" fill="#0f172a"/>
            <text x="200" y="195" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Nilgiri Toda: Red & Black Geometric Pukhoor</text>
        `;
        if (status) status.innerHTML = "<strong>Toda Shawl (Nilgiris, Tamil Nadu):</strong> Sacred counted-thread geometric bands celebrating wild buffalo horns on coarse unbleached white cotton.";
    }
}

// SIM 13: Kashmiri Kashida & Meghalaya Khneng
function switchSim13(mode) {
    const canvas = document.getElementById('sim13Canvas');
    const tag = document.getElementById('sim13ModeTag');
    const status = document.getElementById('sim13Status');
    if (!canvas) return;

    if (mode === 'kashida') {
        if (tag) tag.textContent = "KASHIDA";
        canvas.innerHTML = `
            <rect x="60" y="25" width="280" height="190" rx="8" fill="#1e1b4b" stroke="#4338ca" stroke-width="2"/>
            <path d="M 200,60 C 190,80 160,85 155,105 C 170,115 160,135 150,150 C 170,150 185,160 195,175 C 200,165 205,165 205,175 C 215,160 230,150 250,150 C 240,135 230,115 245,105 C 240,85 210,80 200,60 Z" fill="#b45309" stroke="#f59e0b" stroke-width="2.5"/>
            <line x1="200" y1="65" x2="200" y2="175" stroke="#fef08a" stroke-width="2"/>
            <text x="200" y="200" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Kashmiri Kashida: Chinar Autumn Leaf Motif</text>
        `;
        if (status) status.innerHTML = "<strong>Kashida (Kashmir):</strong> Uses fine chain stitches to depict autumnal chinar leaves, saffron blossoms, and singing nightingales.";
    } else {
        if (tag) tag.textContent = "KHNENG";
        canvas.innerHTML = `
            <rect x="60" y="25" width="280" height="190" rx="8" fill="#fef3c7" stroke="#ca8a04" stroke-width="2"/>
            <line x1="100" y1="120" x2="300" y2="120" stroke="#0f172a" stroke-width="3"/>
            <line x1="130" y1="120" x2="115" y2="90" stroke="#0f172a" stroke-width="2"/>
            <line x1="130" y1="120" x2="115" y2="150" stroke="#0f172a" stroke-width="2"/>
            <line x1="170" y1="120" x2="155" y2="90" stroke="#0f172a" stroke-width="2"/>
            <line x1="170" y1="120" x2="155" y2="150" stroke="#0f172a" stroke-width="2"/>
            <line x1="210" y1="120" x2="195" y2="90" stroke="#0f172a" stroke-width="2"/>
            <line x1="210" y1="120" x2="195" y2="150" stroke="#0f172a" stroke-width="2"/>
            <line x1="250" y1="120" x2="235" y2="90" stroke="#0f172a" stroke-width="2"/>
            <line x1="250" y1="120" x2="235" y2="150" stroke="#0f172a" stroke-width="2"/>
            <text x="200" y="195" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle">Meghalaya Khneng: River Fish-Bone Stitch on Eri Silk</text>
        `;
        if (status) status.innerHTML = "<strong>Khneng (Mustoh, Meghalaya):</strong> Delicate fish-bone embroidery worked in black thread on handspun Eri peace silk.";
    }
}

// SIM 14: Circular Textile Upcycling
function setUpcycleStage(stage) {
    const name = document.getElementById('upcycleStageName');
    const exp = document.getElementById('sim14Explanation');

    if (stage === 1) {
        if (name) name.textContent = "1. New Garment";
        if (exp) exp.innerHTML = "<strong>Stage 1 (New):</strong> Tailored festive kurta worn proudly for school and family celebrations.";
    } else if (stage === 2) {
        if (name) name.textContent = "2. Sibling Hand-Me-Down";
        if (exp) exp.innerHTML = "<strong>Stage 2 (Hand-Me-Down):</strong> Outgrown clothes are passed lovingly to younger siblings or cousins.";
    } else if (stage === 3) {
        if (name) name.textContent = "3. Godhari Quilt / Toy";
        if (exp) exp.innerHTML = "<strong>Stage 3 (Repurposed):</strong> Faded, softened cloth is quilted into cozy blankets, cradle sheets, or fabric dolls.";
    } else if (stage === 4) {
        if (name) name.textContent = "4. Kitchen Duster / Mop";
        if (exp) exp.innerHTML = "<strong>Stage 4 (Cleaning):</strong> Worn scraps serve as absorbent dusting cloths and floor cleaning mops.";
    } else if (stage === 5) {
        if (name) name.textContent = "5. Soil Compost";
        if (exp) exp.innerHTML = "<strong>Stage 5 (Compost):</strong> 100% natural cotton cellulose decomposes completely in garden compost, nourishing new soil!";
    }
}

// SIM 15: Forensic Flame Burn Test
function burnSample(sample) {
    const name = document.getElementById('burnSampleName');
    const odor = document.getElementById('burnOdorText');
    const ash = document.getElementById('burnAshText');
    const verdict = document.getElementById('burnVerdict');
    const status = document.getElementById('sim15Status');

    if (sample === 'cotton') {
        if (name) name.textContent = "Cotton Sample";
        if (odor) odor.textContent = "Odor: Burning paper / leaves";
        if (ash) ash.textContent = "Ash: Soft, fluffy grey ash";
        if (verdict) {
            verdict.textContent = "Natural Plant Cellulose";
            verdict.style.color = '#38bdf8';
        }
        if (status) status.innerHTML = "<strong>Cotton:</strong> Burns with a steady yellow flame, smells like paper (cellulose), and leaves soft powdery grey ash.";
    } else if (sample === 'wool') {
        if (name) name.textContent = "Wool / Silk Sample";
        if (odor) odor.textContent = "Odor: Singed hair / feathers";
        if (ash) ash.textContent = "Ash: Dark, crushable bead";
        if (verdict) {
            verdict.textContent = "Natural Animal Protein";
            verdict.style.color = '#fbbf24';
        }
        if (status) status.innerHTML = "<strong>Wool / Silk:</strong> Burns slowly and self-extinguishes. Emits a burning hair odor (sulfur protein) and leaves a crushable black bead.";
    } else if (sample === 'polyester') {
        if (name) name.textContent = "Polyester Sample";
        if (odor) odor.textContent = "Odor: Sweet chemical / plastic";
        if (ash) ash.textContent = "Ash: Hard, uncrushable plastic bead";
        if (verdict) {
            verdict.textContent = "Petrochemical Synthetic Polymer";
            verdict.style.color = '#f87171';
        }
        if (status) status.innerHTML = "<strong>Polyester:</strong> Melts into bubbling liquid with black chemical smoke, hardening into an uncrushable plastic bead.";
    }
}

// SIM 16: Textile Guardian Workshop
function mendButton() {
    const btn = document.getElementById('looseButton');
    const status = document.getElementById('sim16Status');

    if (btn) {
        const circle = btn.querySelector('circle');
        if (circle) circle.setAttribute('stroke', '#22c55e');
    }
    if (status) {
        status.innerHTML = "<span class='text-emerald-400 font-bold'>Button Mended:</span> You secured the button with crosswise locking stitches! Extending a garment's life saves thousands of litres of water.";
    }
}

function pledgeGuardian() {
    const status = document.getElementById('sim16Status');
    if (status) {
        status.innerHTML = "<span class='text-amber-400 font-bold'>Textile Guardian Certified:</span> You pledged to care for clothes, mend small tears, practice upcycling, and honour India's handloom artisans!";
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

"""
Interactive JavaScript Engine for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I
Enhanced with Strict Male Teacher Voice priority, female voice filtering, Voice Selector UI,
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
let speechKeepAliveTimer = null;

// Comprehensive Female Filter Keywords (Strictly excludes all female voices)
const femaleKeywords = [
    'female', 'woman', 'girl', 'lady', 'zira', 'jenny', 'aria', 'samantha', 'victoria',
    'karen', 'susan', 'neerja', 'heera', 'hazel', 'catherine', 'linda', 'eva', 'ava',
    'siri', 'cortana', 'swara', 'veena', 'priya', 'kalpana', 'shruti', 'sunita',
    'aditi', 'anjali', 'geeta', 'roshni', 'meera', 'rekha', 'rani', 'kavya', 'leena',
    'shreya', 'deepa', 'ananya', 'google indian english', 'google us english',
    'google uk english female', 'google हिन्दी', 'en-in-x-enc', 'en-in-x-cxx'
];

function isFemaleVoice(v) {
    if (!v) return false;
    const name = (v.name || '').toLowerCase();
    const id = (v.voiceURI || '').toLowerCase();
    return femaleKeywords.some(fk => name.includes(fk) || id.includes(fk));
}

// Strict Male Voice Identifier
function isStrictlyMaleVoice(v) {
    if (!v) return false;
    if (isFemaleVoice(v)) return false;

    const name = (v.name || '').toLowerCase();
    const id = (v.voiceURI || '').toLowerCase();

    const maleKeywords = [
        'male', 'prabhat', 'rishi', 'ravi', 'madhav', 'pradeep', 'karan',
        'amit', 'anil', 'ajay', 'deepak', 'mohan', 'hemant', 'aravind', 'arun',
        'madhur', 'david', 'mark', 'george', 'guy', 'james', 'richard', 'charles',
        'oliver', 'alex', 'daniel', 'fred', 'tom', 'lee', 'reed', 'nathan',
        'en-in-x-end', 'en-in-x-ene', 'en-us-x-sfg'
    ];

    return maleKeywords.some(mk => name.includes(mk) || id.includes(mk));
}

function isIndianMaleVoice(v) {
    if (!v || !isStrictlyMaleVoice(v)) return false;
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    const isIndian = lang.includes('en-in') || lang.includes('en_in') || lang.includes('hi-in') || name.includes('india');

    const explicitIndianMale = [
        'prabhat', 'rishi', 'ravi', 'madhav', 'pradeep', 'karan', 'amit', 'anil',
        'ajay', 'deepak', 'mohan', 'hemant', 'aravind', 'arun', 'madhur'
    ];

    return isIndian && (explicitIndianMale.some(mk => name.includes(mk)) || name.includes('male'));
}

// Dedicated Male Voice Selector with Indian Priority
function getBestMaleVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    // 1. Priority 1: Verified Indian Male voice (Prabhat, Rishi, Ravi, etc.)
    for (const v of voices) {
        if (isIndianMaleVoice(v)) return v;
    }

    // 2. Priority 2: Google UK English Male (The best built-in desktop male voice in Google Chrome)
    const googleMale = voices.find(v => {
        const name = (v.name || '').toLowerCase();
        return name.includes('google') && name.includes('male') && !isFemaleVoice(v);
    });
    if (googleMale) return googleMale;

    // 3. Priority 3: Any explicit male voice (David, Mark, Guy, Alex, Daniel, Oliver, etc.)
    const anyMale = voices.find(v => isStrictlyMaleVoice(v));
    if (anyMale) return anyMale;

    // 4. Priority 4: Any voice that explicitly contains 'male' in name or id
    const maleGeneric = voices.find(v => {
        const name = (v.name || '').toLowerCase();
        const id = (v.voiceURI || '').toLowerCase();
        return (name.includes('male') || id.includes('male')) && !isFemaleVoice(v);
    });
    if (maleGeneric) return maleGeneric;

    // 5. Priority 5: Any non-female English voice
    const nonFemaleEn = voices.find(v => {
        const lang = (v.lang || '').toLowerCase();
        return lang.startsWith('en') && !isFemaleVoice(v);
    });
    if (nonFemaleEn) return nonFemaleEn;

    // 6. Absolute Fallback
    return voices[0];
}

// Populate Voice Selector in header
function populateVoiceList() {
    const voiceSelect = document.getElementById('voiceSelect');
    if (!voiceSelect || !('speechSynthesis' in window)) return;

    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return;

    voiceSelect.innerHTML = '';

    if (!selectedMaleVoice || isFemaleVoice(selectedMaleVoice)) {
        selectedMaleVoice = getBestMaleVoice();
    }

    // Sort: Indian Male first, then other Male voices, then remaining
    const sortedVoices = [...voices].sort((a, b) => {
        const aIndM = isIndianMaleVoice(a);
        const bIndM = isIndianMaleVoice(b);
        if (aIndM && !bIndM) return -1;
        if (!aIndM && bIndM) return 1;

        const aMale = isStrictlyMaleVoice(a);
        const bMale = isStrictlyMaleVoice(b);
        if (aMale && !bMale) return -1;
        if (!aMale && bMale) return 1;

        const aFem = isFemaleVoice(a);
        const bFem = isFemaleVoice(b);
        if (!aFem && bFem) return -1;
        if (aFem && !bFem) return 1;

        return 0;
    });

    sortedVoices.forEach((v) => {
        const opt = document.createElement('option');
        const origIdx = voices.indexOf(v);
        opt.value = origIdx;

        const isIndM = isIndianMaleVoice(v);
        const isMale = isStrictlyMaleVoice(v);
        const isFem = isFemaleVoice(v);

        let label = v.name;
        if (isIndM) {
            label = `🇮🇳 [Indian Male Teacher] ${v.name}`;
        } else if (isMale) {
            label = `👨 [Male Teacher] ${v.name}`;
        } else if (isFem) {
            label = `👩 [Female] ${v.name}`;
        } else {
            label = `🎙️ ${v.name}`;
        }

        if (v === selectedMaleVoice) {
            opt.selected = true;
            label += ' ★ Selected';
        }

        opt.textContent = label;
        voiceSelect.appendChild(opt);
    });
}

function onVoiceChange(val) {
    if (!('speechSynthesis' in window)) return;
    const voices = window.speechSynthesis.getVoices();
    const idx = parseInt(val, 10);
    if (voices[idx]) {
        selectedMaleVoice = voices[idx];
        if (isSpeaking && currentSlideSpeaking) {
            const txtEl = document.getElementById(`slide-spoken-text-${currentSlideSpeaking}`);
            if (txtEl) {
                stopLectureSpeech();
                startLectureSpeech(txtEl.textContent, currentSlideSpeaking);
            }
        }
    }
}

// Clean text for speech synthesis (strip markdown, HTML, keep pure spoken words)
function cleanTextForSpeech(text) {
    return text
        .replace(/<[^>]*>/g, ' ')
        .replace(/\*\*/g, '')
        .replace(/\*/g, '')
        .replace(/#/g, '')
        .replace(/—/g, ', ')
        .replace(/–/g, ', ')
        .replace(/×/g, ' multiplied by ')
        .replace(/÷/g, ' divided by ')
        .replace(/&times;/g, ' multiplied by ')
        .replace(/&divide;/g, ' divided by ')
        .replace(/&ge;/g, ' is greater than or equal to ')
        .replace(/&le;/g, ' is less than or equal to ')
        .replace(/&rarr;/g, ' leads to ')
        .replace(/\s+/g, ' ')
        .trim();
}

// Spoken Lecture Controller
function startLectureSpeech(rawText, slideNo) {
    if (!('speechSynthesis' in window)) {
        alert("Speech synthesis is not supported in this browser.");
        return;
    }

    if (isSpeaking && currentSlideSpeaking === slideNo) {
        stopLectureSpeech();
        return;
    }

    stopLectureSpeech();

    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) {
        window.speechSynthesis.onvoiceschanged = () => {
            selectedMaleVoice = getBestMaleVoice();
            populateVoiceList();
            startLectureSpeech(rawText, slideNo);
        };
        return;
    }

    // Guarantee that selected voice is locked to male
    if (!selectedMaleVoice || isFemaleVoice(selectedMaleVoice)) {
        selectedMaleVoice = getBestMaleVoice();
        populateVoiceList();
    }

    const clean = cleanTextForSpeech(rawText);
    if (!clean) return;

    const rawSentences = clean.match(/[^.!?]+[.!?]+(\s|$)|[^.!?]+$/g) || [clean];
    speechQueue = rawSentences.map(s => s.trim()).filter(s => s.length > 0);
    speechQueueIndex = 0;
    isSpeaking = true;
    currentSlideSpeaking = slideNo;

    updateAudioButtonUI(slideNo, true);

    // Chrome keep-alive timer for long full-lecture playback
    if (speechKeepAliveTimer) clearInterval(speechKeepAliveTimer);
    speechKeepAliveTimer = setInterval(() => {
        if (window.speechSynthesis && window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        } else {
            clearInterval(speechKeepAliveTimer);
        }
    }, 10000);

    playNextSpeechChunk();
}

function playNextSpeechChunk() {
    if (!isSpeaking || speechQueueIndex >= speechQueue.length) {
        stopLectureSpeech();
        return;
    }

    const chunk = speechQueue[speechQueueIndex];
    speechQueueIndex++;

    const utt = new SpeechSynthesisUtterance(chunk);

    if (!selectedMaleVoice || isFemaleVoice(selectedMaleVoice)) {
        selectedMaleVoice = getBestMaleVoice();
    }

    if (selectedMaleVoice) {
        utt.voice = selectedMaleVoice;
    }

    // Acoustic male teacher calibration
    const isMale = isStrictlyMaleVoice(selectedMaleVoice);
    if (isMale) {
        utt.pitch = 0.85; // Warm, dignified baritone male teacher delivery
        utt.rate = 0.94;
    } else {
        // Deep pitch transformation if an unverified voice is ever encountered
        utt.pitch = 0.55;
        utt.rate = 0.90;
    }

    utt.onend = () => {
        if (isSpeaking) {
            playNextSpeechChunk();
        }
    };

    utt.onerror = () => {
        if (isSpeaking) {
            playNextSpeechChunk();
        }
    };

    window.speechSynthesis.speak(utt);
}

function stopLectureSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    if (speechKeepAliveTimer) {
        clearInterval(speechKeepAliveTimer);
        speechKeepAliveTimer = null;
    }
    if (currentSlideSpeaking) {
        updateAudioButtonUI(currentSlideSpeaking, false);
    }
    isSpeaking = false;
    currentSlideSpeaking = null;
    speechQueue = [];
    speechQueueIndex = 0;
}

function updateAudioButtonUI(slideNo, playing) {
    const btn = document.getElementById(`slide-audio-btn-${slideNo}`);
    const badge = document.getElementById(`slide-audio-badge-${slideNo}`);
    const globalBtn = document.getElementById('globalSpeechBtn');

    if (btn) {
        if (playing) {
            btn.innerHTML = '<span>⏹</span><span>Stop Full Lecture</span>';
            btn.className = 'px-3 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold flex items-center space-x-1.5 transition shadow-sm';
        } else {
            btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
            btn.className = 'px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm';
        }
    }

    if (badge) {
        if (playing) {
            badge.textContent = 'Male Teacher Speaking...';
            badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 animate-pulse';
        } else {
            badge.textContent = 'Male Audio Lecture Ready';
            badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
    }

    if (globalBtn) {
        if (playing) {
            globalBtn.innerHTML = '<span>⏹</span><span>Stop Audio</span>';
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-600 text-white hover:bg-rose-500 flex items-center space-x-1.5 transition shadow';
        } else {
            globalBtn.innerHTML = '<span>▶</span><span>Play Slide Audio</span>';
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500/20 text-amber-300 hover:bg-amber-500/30 border border-amber-500/30 flex items-center space-x-1.5 transition';
        }
    }
}

function toggleCurrentSlideLecture() {
    const txtEl = document.getElementById(`slide-spoken-text-${currentSlide}`);
    if (txtEl) {
        startLectureSpeech(txtEl.textContent, currentSlide);
    }
}

// Slide Navigation
function showSlide(n) {
    stopLectureSpeech();

    if (n < 1) n = 1;
    if (n > totalSlides) n = totalSlides;

    currentSlide = n;

    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) el.style.display = (i === n) ? 'block' : 'none';
    }

    // Update Progress Bar & Counter
    const progBar = document.getElementById('slideProgressBar');
    if (progBar) progBar.style.width = `${(n / totalSlides) * 100}%`;

    const countDisp = document.getElementById('slideCounterDisplay');
    if (countDisp) countDisp.textContent = `Slide ${n} of ${totalSlides}`;

    const jumpSel = document.getElementById('slideJumpSelect');
    if (jumpSel) jumpSel.value = n;

    // Prev / Next button states
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) prevBtn.disabled = (n === 1);

    if (n === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'inline-flex';
            nextBtn.disabled = false;
        }
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

function jumpToSlide(n) {
    showSlide(parseInt(n, 10));
}

// Formative Checkpoints
function checkCheckpoint(cpId, optIdx, correctIdx, explanation) {
    const fbEl = document.getElementById(`cp-feedback-${cpId}`);
    if (!fbEl) return;

    fbEl.classList.remove('hidden');
    if (optIdx === correctIdx) {
        fbEl.className = 'p-3 rounded-xl bg-emerald-950/70 border border-emerald-500/40 text-xs text-emerald-200 mt-2';
        fbEl.innerHTML = `<strong>Correct! &check;</strong> ${explanation}`;
    } else {
        fbEl.className = 'p-3 rounded-xl bg-rose-950/70 border border-rose-500/40 text-xs text-rose-200 mt-2';
        fbEl.innerHTML = `<strong>Not quite.</strong> ${explanation}`;
    }
}

// Mastery Quiz Options
function selectQuizOption(qId, optIdx, correctIdx, title, question, explanation) {
    const fbEl = document.getElementById(`q-fb-${qId}`);
    const solBtn = document.getElementById(`q-sol-btn-${qId}`);

    if (fbEl) {
        fbEl.classList.remove('hidden');
        if (optIdx === correctIdx) {
            fbEl.className = 'p-3 rounded-xl bg-emerald-950/80 border border-emerald-500/50 text-xs text-emerald-200 mt-2';
            fbEl.innerHTML = `<strong>Correct! &check;</strong> ${explanation}`;
        } else {
            fbEl.className = 'p-3 rounded-xl bg-rose-950/80 border border-rose-500/50 text-xs text-rose-200 mt-2';
            fbEl.innerHTML = `<strong>Incorrect.</strong> ${explanation}`;
        }
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
    const modalQ = document.getElementById('modalQuestion');
    const modalSol = document.getElementById('modalSolution') || document.getElementById('modalBody');

    if (modalTitle) modalTitle.textContent = title;
    if (modalQ) modalQ.innerHTML = question;
    if (modalSol) modalSol.innerHTML = solutionHtml;

    if (modal) {
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

// ==========================================
// BESPOKE 16 SIMULATOR ENGINES (Class 5 Maths)
// ==========================================

// SIM 1: We the Travellers (Transport Speeds)
function setTransportMode(mode) {
    const needle = document.getElementById('speedoNeedle');
    const speedText = document.getElementById('sim1SpeedText');
    const descText = document.getElementById('sim1DescText');
    const statusText = document.getElementById('sim1Status');

    let angle = -60;
    let speed = "4 km/h";
    let desc = "Walking (Ancient Era)";
    let explanation = "Walking at 4 km/h: An 800 km journey across states would take 200 hours of continuous walking!";

    if (mode === 'cart') {
        angle = -30;
        speed = "5 km/h";
        desc = "Bullock Cart (Agricultural Era)";
        explanation = "Bullock Cart at 5 km/h: Revolutionized trade and cargo transport, covering roughly 30 to 40 km per day.";
    } else if (mode === 'train') {
        angle = 20;
        speed = "120 km/h";
        desc = "Express Train (Industrial / Modern)";
        explanation = "Express Train at 120 km/h: Covers 600 km in just 5 hours, connecting distant cities seamlessly!";
    } else if (mode === 'rocket') {
        angle = 60;
        speed = "28,000 km/h";
        desc = "Spacecraft (Space Era)";
        explanation = "Spacecraft at 28,000 km/h (Orbital Speed): Can circle the entire Earth in about 90 minutes!";
    }

    if (needle) needle.setAttribute('transform', `rotate(${angle} 150 150)`);
    if (speedText) speedText.textContent = speed;
    if (descText) descText.textContent = desc;
    if (statusText) statusText.innerHTML = `<strong>Transport Insight:</strong> ${explanation}`;
}

// SIM 2: Ten Thousand (Base-10 Visual Counter)
let thousandsCount = 0;
function addThousandBlock() {
    if (thousandsCount < 10) {
        thousandsCount++;
        renderThousandBlocks();
    }
}

function resetThousandBlocks() {
    thousandsCount = 0;
    renderThousandBlocks();
}

function jumpToTenThousand() {
    thousandsCount = 10;
    renderThousandBlocks();
}

function renderThousandBlocks() {
    const grid = document.getElementById('thousandBlocksGrid');
    const countVal = document.getElementById('thousandCountVal');
    const status = document.getElementById('sim2Status');

    if (countVal) countVal.textContent = (thousandsCount * 1000).toLocaleString('en-IN');

    if (grid) {
        grid.innerHTML = '';
        for (let i = 0; i < 10; i++) {
            const block = document.createElement('div');
            block.className = `p-2 rounded-lg border text-center text-[10px] font-bold font-mono transition-all duration-300 ${
                i < thousandsCount 
                    ? 'bg-amber-500/20 border-amber-500/50 text-amber-300 scale-100' 
                    : 'bg-slate-900 border-slate-800 text-slate-600 scale-95 opacity-50'
            }`;
            block.innerHTML = `<span>1,000</span><br><span class="text-[8px] text-slate-400">#${i + 1}</span>`;
            grid.appendChild(block);
        }
    }

    if (status) {
        if (thousandsCount === 10) {
            status.innerHTML = "<strong>Milestone Reached!</strong> 10 Thousands bundle together to create <strong>1 Ten Thousand (10,000)</strong>, opening the 5th place value column: TTh!";
        } else {
            status.innerHTML = `Current count: <strong>${thousandsCount} Thousand${thousandsCount !== 1 ? 's' : ''}</strong> = <strong>${(thousandsCount * 1000).toLocaleString('en-IN')}</strong>. Keep adding to reach 10,000!`;
        }
    }
}

// SIM 3: Place Value (Indian Place Value Spike Abacus)
let abacusState = { tth: 3, th: 4, h: 2, t: 8, o: 5 };

function incrementAbacusSpike(spike) {
    if (abacusState[spike] !== undefined) {
        abacusState[spike] = (abacusState[spike] + 1) % 10;
        renderAbacus();
    }
}

function renderAbacus() {
    const spikes = ['tth', 'th', 'h', 't', 'o'];
    spikes.forEach(s => {
        const valEl = document.getElementById(`abacus-${s}-val`);
        const beadsCont = document.getElementById(`abacus-${s}-beads`);
        const count = abacusState[s];

        if (valEl) valEl.textContent = count;
        if (beadsCont) {
            beadsCont.innerHTML = '';
            for (let b = 0; b < count; b++) {
                const bead = document.createElement('div');
                bead.className = "w-6 h-3 rounded-full bg-amber-400 border border-amber-300 shadow-sm";
                beadsCont.appendChild(bead);
            }
        }
    });

    const standardVal = abacusState.tth * 10000 + abacusState.th * 1000 + abacusState.h * 100 + abacusState.t * 10 + abacusState.o;
    const stdEl = document.getElementById('abacusStandardForm');
    const expEl = document.getElementById('abacusExpandedForm');

    if (stdEl) stdEl.textContent = standardVal.toLocaleString('en-IN');
    if (expEl) expEl.textContent = `${abacusState.tth * 10000} + ${abacusState.th * 1000} + ${abacusState.h * 100} + ${abacusState.t * 10} + ${abacusState.o}`;
}

// SIM 4: Writing Numbers (Indian Comma Formatter)
function setExampleNumber(numStr) {
    const thousandsPart = numStr.slice(0, 2);
    const onesPart = numStr.slice(2);

    const thPeriodEl = document.getElementById('thPeriodDisplay');
    const onesPeriodEl = document.getElementById('onesPeriodDisplay');
    const formattedEl = document.getElementById('formattedNumDisplay');
    const wordsEl = document.getElementById('numWordsDisplay');

    if (thPeriodEl) thPeriodEl.textContent = thousandsPart;
    if (onesPeriodEl) onesPeriodEl.textContent = onesPart;
    if (formattedEl) formattedEl.textContent = `${thousandsPart},${onesPart}`;

    let words = "";
    if (numStr === '48215') words = "Forty-eight thousand two hundred fifteen";
    else if (numStr === '70008') words = "Seventy thousand eight";
    else if (numStr === '99999') words = "Ninety-nine thousand nine hundred ninety-nine (Largest 5-digit number)";

    if (wordsEl) wordsEl.textContent = words;
}

// SIM 5: Ordering Numbers (Vehicle Odometer Sorter)
let odometerVehicles = [
    { name: "Family Car", reading: 34500, id: "car" },
    { name: "School Bus", reading: 78200, id: "bus" },
    { name: "Delivery Van", reading: 12900, id: "van" },
    { name: "Highway Truck", reading: 95400, id: "truck" }
];

function sortOdometers(order) {
    if (order === 'ascending') {
        odometerVehicles.sort((a, b) => a.reading - b.reading);
    } else {
        odometerVehicles.sort((a, b) => b.reading - a.reading);
    }

    const container = document.getElementById('odometerList');
    if (container) {
        container.innerHTML = '';
        odometerVehicles.forEach((v, idx) => {
            const card = document.createElement('div');
            card.className = "flex items-center justify-between p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs";
            card.innerHTML = `
                <div class="flex items-center space-x-2">
                    <span class="w-5 h-5 rounded-full bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-[10px]">${idx + 1}</span>
                    <span class="font-semibold text-white">${v.name}</span>
                </div>
                <span class="font-mono font-bold text-amber-400">${v.reading.toLocaleString('en-IN')} km</span>
            `;
            container.appendChild(card);
        });
    }

    const status = document.getElementById('sim5Status');
    if (status) {
        status.innerHTML = `Sorted in <strong>${order.toUpperCase()}</strong> order by comparing the highest place value (Ten Thousands) first!`;
    }
}

// SIM 6: Digit Swap (Number Shifter Lab)
let currentDigits = [2, 5, 4, 8, 0];
const originalSwapVal = 25480;

function swapDigits(i, j) {
    const temp = currentDigits[i];
    currentDigits[i] = currentDigits[j];
    currentDigits[j] = temp;
    updateSwapUI();
}

function resetSwapDigits() {
    currentDigits = [2, 5, 4, 8, 0];
    updateSwapUI();
}

function updateSwapUI() {
    const tilesCont = document.getElementById('digitTilesCont');
    if (tilesCont) {
        tilesCont.innerHTML = '';
        currentDigits.forEach((d) => {
            const t = document.createElement('div');
            t.className = "p-3 bg-amber-950/60 border border-amber-500/40 rounded-xl text-center font-mono font-bold text-lg text-amber-300";
            t.textContent = d;
            tilesCont.appendChild(t);
        });
    }

    const currentVal = currentDigits[0] * 10000 + currentDigits[1] * 1000 + currentDigits[2] * 100 + currentDigits[3] * 10 + currentDigits[4];
    const valEl = document.getElementById('swapCurrentVal');
    const diffEl = document.getElementById('swapDiffVal');

    if (valEl) valEl.textContent = currentVal.toLocaleString('en-IN');
    if (diffEl) {
        const diff = currentVal - originalSwapVal;
        if (diff > 0) {
            diffEl.className = "text-xs font-bold text-emerald-400";
            diffEl.textContent = `Increased by +${diff.toLocaleString('en-IN')}`;
        } else if (diff < 0) {
            diffEl.className = "text-xs font-bold text-rose-400";
            diffEl.textContent = `Decreased by ${diff.toLocaleString('en-IN')}`;
        } else {
            diffEl.className = "text-xs font-bold text-slate-400";
            diffEl.textContent = "Original value (25,480)";
        }
    }
}

// SIM 7: Nearest Tens (Rabbit & Carrot Number Line)
function setRabbitPosition(pos) {
    const rabbit = document.getElementById('rabbitToken');
    const valText = document.getElementById('rabbitCurrentVal');
    const resultText = document.getElementById('rabbitResultText');

    let xPos = 50 + (pos - 40) * 30;
    if (rabbit) rabbit.setAttribute('cx', xPos);
    if (valText) valText.textContent = `Position: ${pos}`;

    if (resultText) {
        const onesDigit = pos % 10;
        if (onesDigit >= 5) {
            resultText.innerHTML = `Ones digit is <strong>${onesDigit} (&ge; 5)</strong> &rarr; Hops UP to <strong>50</strong>!`;
        } else {
            resultText.innerHTML = `Ones digit is <strong>${onesDigit} (&lt; 5)</strong> &rarr; Hops DOWN to <strong>40</strong>!`;
        }
    }
}

// SIM 8: Nearest Hundreds (Highway Milestone Marker)
function setHighwayDistance(dist) {
    const car = document.getElementById('milestoneCar');
    const resText = document.getElementById('milestoneResultText');
    const verdText = document.getElementById('milestoneVerdictText');

    let x = 50 + ((dist - 300) / 100) * 300;
    if (car) car.setAttribute('transform', `translate(${x - 200}, 0)`);

    const tensDigit = Math.floor((dist % 100) / 10);
    if (resText) resText.textContent = `${dist} km: Tens digit is ${tensDigit} (${tensDigit >= 5 ? '≥ 5' : '< 5'})`;
    if (verdText) {
        if (tensDigit >= 5) {
            verdText.textContent = "Rounds UP to 400 km";
            verdText.setAttribute('fill', '#34d399');
        } else {
            verdText.textContent = "Rounds DOWN to 300 km";
            verdText.setAttribute('fill', '#38bdf8');
        }
    }
}

// SIM 9: Nearest Thousands (Dual-Rounding Milestone Analyzer)
function setRoundingNum(num) {
    const slider = document.getElementById('roundSlider');
    if (slider) slider.value = num;
    updateDualRounding(num);
}

function updateDualRounding(val) {
    const num = parseInt(val, 10);
    const disp = document.getElementById('currentRoundVal');
    const res100 = document.getElementById('resRound100');
    const exp100 = document.getElementById('expRound100');
    const res1000 = document.getElementById('resRound1000');
    const exp1000 = document.getElementById('expRound1000');
    const banner = document.getElementById('dualRoundBanner');

    if (disp) disp.textContent = num.toLocaleString('en-IN');

    const rounded100 = Math.round(num / 100) * 100;
    const tens = Math.floor((num % 100) / 10);
    if (res100) res100.textContent = rounded100.toLocaleString('en-IN');
    if (exp100) exp100.innerHTML = `Tens digit ${tens} ${tens >= 5 ? '&ge; 5 &rarr; Round up' : '&lt; 5 &rarr; Round down'} to ${rounded100.toLocaleString('en-IN')}`;

    const rounded1000 = Math.round(num / 1000) * 1000;
    const hundreds = Math.floor((num % 1000) / 100);
    if (res1000) res1000.textContent = rounded1000.toLocaleString('en-IN');
    if (exp1000) exp1000.innerHTML = `Hundreds digit ${hundreds} ${hundreds >= 5 ? '&ge; 5 &rarr; Round up' : '&lt; 5 &rarr; Round down'} to ${rounded1000.toLocaleString('en-IN')}`;

    if (banner) {
        if (rounded100 === rounded1000) {
            banner.className = "p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-xl text-center text-xs text-emerald-300 font-medium";
            banner.innerHTML = `Awesome match! Both roundings land on <strong>${rounded100.toLocaleString('en-IN')}</strong>!`;
        } else {
            banner.className = "p-3 bg-amber-950/60 border border-amber-500/40 rounded-xl text-center text-xs text-amber-300 font-medium";
            banner.innerHTML = `Different milestones: Nearest 100 is <strong>${rounded100.toLocaleString('en-IN')}</strong>, whereas Nearest 1,000 is <strong>${rounded1000.toLocaleString('en-IN')}</strong>.`;
        }
    }
}

// SIM 10: Transport Speeds (Distance = Speed × Time)
let currentVehicleSpeed = 120;
let currentVehicleName = "Train";

function setSpeedVehicle(type, speed) {
    currentVehicleSpeed = speed;
    if (type === 'walk') currentVehicleName = "Walking";
    else if (type === 'train') currentVehicleName = "Express Train";
    else if (type === 'flight') currentVehicleName = "Aeroplane";
    else if (type === 'rocket') currentVehicleName = "Spacecraft";

    const nameEl = document.getElementById('selectedVehicleName');
    const speedEl = document.getElementById('selectedVehicleSpeed');
    if (nameEl) nameEl.textContent = currentVehicleName;
    if (speedEl) speedEl.textContent = `${speed.toLocaleString('en-IN')} km/h`;

    const slider = document.getElementById('timeSlider');
    const hours = slider ? parseInt(slider.value, 10) : 4;
    updateSpeedCalc(hours);
}

function updateSpeedCalc(hours) {
    const h = parseInt(hours, 10);
    const hoursDisp = document.getElementById('hoursVal');
    const distDisp = document.getElementById('totalDistDisplay');
    const formDisp = document.getElementById('distFormulaDisplay');

    if (hoursDisp) hoursDisp.textContent = `${h} hour${h > 1 ? 's' : ''}`;

    const totalDist = currentVehicleSpeed * h;
    if (distDisp) distDisp.textContent = `${totalDist.toLocaleString('en-IN')} km`;
    if (formDisp) formDisp.textContent = `${currentVehicleSpeed.toLocaleString('en-IN')} km/h × ${h} h = ${totalDist.toLocaleString('en-IN')} km`;
}

// SIM 11: Trip Planning (School Trip Fleet Dispatcher)
function updateTripFleet(headcount) {
    const count = parseInt(headcount, 10);
    const countDisp = document.getElementById('tripHeadcount');
    if (countDisp) countDisp.textContent = `${count} Passengers`;

    const buses = Math.floor(count / 50);
    const remainder = count % 50;
    const vans = remainder > 0 ? Math.ceil(remainder / 15) : 0;

    const busCountEl = document.getElementById('bus50Count');
    const busSeatsEl = document.getElementById('bus50Seats');
    const vanCountEl = document.getElementById('van15Count');
    const vanSeatsEl = document.getElementById('van15Seats');
    const totalSeatsEl = document.getElementById('totalSeatsBooked');
    const emptySeatsEl = document.getElementById('emptySeatsCount');

    if (busCountEl) busCountEl.textContent = `${buses} Bus${buses !== 1 ? 'es' : ''}`;
    if (busSeatsEl) busSeatsEl.textContent = `Carries ${buses * 50} passengers`;

    if (vanCountEl) vanCountEl.textContent = `${vans} Van${vans !== 1 ? 's' : ''}`;
    if (vanSeatsEl) vanSeatsEl.textContent = `Carries remaining ${remainder} (${vans * 15} capacity)`;

    const totalCap = buses * 50 + vans * 15;
    if (totalSeatsEl) totalSeatsEl.textContent = `${totalCap} seats`;
    if (emptySeatsEl) emptySeatsEl.textContent = `${totalCap - count} empty seats`;
}

// SIM 12: Real-World Numbers Context
function setContextNumber(key, val, title, breakdown) {
    const tEl = document.getElementById('contextTitle');
    const nEl = document.getElementById('contextNum');
    const wEl = document.getElementById('contextWords');

    if (tEl) tEl.textContent = title;
    if (nEl) nEl.textContent = val.toLocaleString('en-IN');

    let words = "";
    if (key === 'book') words = "Eighteen thousand four hundred fifty";
    else if (key === 'stadium') words = "Forty-two thousand five hundred";
    else if (key === 'forest') words = "Twenty-five thousand six hundred eighty";
    else if (key === 'town') words = "Sixty-eight thousand nine hundred";
    if (wEl) wEl.textContent = words;

    const bCont = document.getElementById('contextBreakdown');
    if (bCont) {
        const str = String(val).padStart(5, '0');
        const digits = str.split('').map(Number);
        bCont.innerHTML = `
            <div class="bg-teal-950/60 p-2 rounded border border-teal-500/30"><div class="text-[10px] text-teal-400">TTh</div><div class="font-bold text-white text-base">${digits[0]}</div><div class="text-[9px] text-slate-400">${(digits[0] * 10000).toLocaleString('en-IN')}</div></div>
            <div class="bg-cyan-950/60 p-2 rounded border border-cyan-500/30"><div class="text-[10px] text-cyan-400">Th</div><div class="font-bold text-white text-base">${digits[1]}</div><div class="text-[9px] text-slate-400">${(digits[1] * 1000).toLocaleString('en-IN')}</div></div>
            <div class="bg-blue-950/60 p-2 rounded border border-blue-500/30"><div class="text-[10px] text-blue-400">H</div><div class="font-bold text-white text-base">${digits[2]}</div><div class="text-[9px] text-slate-400">${digits[2] * 100}</div></div>
            <div class="bg-indigo-950/60 p-2 rounded border border-indigo-500/30"><div class="text-[10px] text-indigo-400">T</div><div class="font-bold text-white text-base">${digits[3]}</div><div class="text-[9px] text-slate-400">${digits[3] * 10}</div></div>
            <div class="bg-violet-950/60 p-2 rounded border border-violet-500/30"><div class="text-[10px] text-violet-400">O</div><div class="font-bold text-white text-base">${digits[4]}</div><div class="text-[9px] text-slate-400">${digits[4]}</div></div>
        `;
    }
}

// SIM 13: River Crossing Puzzle
let riverState = {
    boatBank: 'left',
    cargo: null,
    left: ['lion', 'sheep', 'grass'],
    right: []
};

function updateRiverUI() {
    const leftCont = document.getElementById('leftBankItems');
    const rightCont = document.getElementById('rightBankItems');
    const boatDisp = document.getElementById('boatDisplay');
    const status = document.getElementById('riverGameStatus');

    const icons = { lion: '🦁 Lion', sheep: '🐑 Sheep', grass: '🌾 Grass' };

    if (leftCont) {
        leftCont.innerHTML = riverState.left.map(i => `<span class="px-2 py-1 bg-amber-900/60 border border-amber-600/40 rounded text-amber-200 text-xs">${icons[i]}</span>`).join('') || '<span class="text-slate-500 italic text-[11px]">Empty</span>';
    }

    if (rightCont) {
        rightCont.innerHTML = riverState.right.map(i => `<span class="px-2 py-1 bg-teal-900/60 border border-teal-600/40 rounded text-teal-200 text-xs">${icons[i]}</span>`).join('') || '<span class="text-slate-500 italic text-[11px]">None yet</span>';
    }

    if (boatDisp) {
        boatDisp.innerHTML = `
            <div class="text-[11px] text-amber-300 font-semibold">🚣 Boatman (${riverState.boatBank === 'left' ? 'Left Bank' : 'Right Bank'})</div>
            <div id="boatCargo" class="text-xs text-slate-300 mt-0.5">${riverState.cargo ? icons[riverState.cargo] : 'Empty'}</div>
        `;
    }

    const bankWithItems = (riverState.boatBank === 'left') ? riverState.right : riverState.left;
    if (bankWithItems.includes('lion') && bankWithItems.includes('sheep')) {
        if (status) status.innerHTML = "<span class='text-rose-400 font-bold'>DANGER!</span> The Lion is alone with the Sheep and ate it! Click Reset to try again.";
        return false;
    }
    if (bankWithItems.includes('sheep') && bankWithItems.includes('grass')) {
        if (status) status.innerHTML = "<span class='text-rose-400 font-bold'>DANGER!</span> The Sheep is alone with the Grass and ate it! Click Reset to try again.";
        return false;
    }

    if (riverState.right.length === 3) {
        if (status) status.innerHTML = "<span class='text-emerald-400 font-bold'>CONGRATULATIONS! 🎉</span> All three reached the right bank safely!";
        return true;
    }

    if (status) status.textContent = `Boat is on the ${riverState.boatBank} bank. ${riverState.cargo ? `Loaded: ${icons[riverState.cargo]}` : 'Ready to load.'}`;
    return true;
}

function riverLoad(item) {
    const currentBankList = riverState.boatBank === 'left' ? riverState.left : riverState.right;
    if (riverState.cargo === item) {
        riverState.cargo = null;
        currentBankList.push(item);
    } else if (!riverState.cargo && currentBankList.includes(item)) {
        const idx = currentBankList.indexOf(item);
        currentBankList.splice(idx, 1);
        riverState.cargo = item;
    }
    updateRiverUI();
}

function riverRowBoat() {
    riverState.boatBank = (riverState.boatBank === 'left') ? 'right' : 'left';
    if (riverState.cargo) {
        if (riverState.boatBank === 'right') {
            riverState.right.push(riverState.cargo);
        } else {
            riverState.left.push(riverState.cargo);
        }
        riverState.cargo = null;
    }
    updateRiverUI();
}

function riverReset() {
    riverState = { boatBank: 'left', cargo: null, left: ['lion', 'sheep', 'grass'], right: [] };
    updateRiverUI();
}

function riverAutoSolve() {
    riverReset();
    const steps = [
        "1. Boatman takes Sheep across &rarr; Left: Lion, Grass; Right: Sheep",
        "2. Boatman returns empty &rarr; Left: Lion, Grass",
        "3. Boatman takes Lion across &rarr; Right: Lion, Sheep",
        "4. Boatman brings Sheep BACK &rarr; Left: Sheep, Grass",
        "5. Boatman takes Grass across &rarr; Right: Lion, Grass",
        "6. Boatman returns empty &rarr; Left: Sheep",
        "7. Boatman takes Sheep across &rarr; Right: Lion, Sheep, Grass &check;"
    ];
    const status = document.getElementById('riverGameStatus');
    if (status) {
        status.innerHTML = `<div class='text-left space-y-1 text-sky-300'><strong>Winning 7-Step Sequence:</strong><br>${steps.join('<br>')}</div>`;
    }
}

// SIM 14: Pebble Game (Strategic Nim - Multiple of 4)
let pebblesRemaining = 15;

function renderPebbles() {
    const disp = document.getElementById('pebbleCountDisplay');
    const cont = document.getElementById('pebblesContainer');
    if (disp) disp.textContent = pebblesRemaining;

    if (cont) {
        cont.innerHTML = '';
        for (let i = 0; i < pebblesRemaining; i++) {
            const p = document.createElement('div');
            p.className = "w-6 h-6 rounded-full bg-gradient-to-br from-amber-300 to-amber-600 border border-amber-200 shadow flex items-center justify-center text-[10px] font-bold text-slate-900";
            p.textContent = i + 1;
            cont.appendChild(p);
        }
    }
}

function playerTakePebbles(count) {
    const status = document.getElementById('pebbleGameStatus');
    if (pebblesRemaining < count) {
        if (status) status.textContent = `Only ${pebblesRemaining} pebble(s) left!`;
        return;
    }

    pebblesRemaining -= count;
    renderPebbles();

    if (pebblesRemaining === 0) {
        if (status) status.innerHTML = "<strong class='text-emerald-400'>You took the last pebble and WON! 🎉</strong>";
        return;
    }

    if (status) status.textContent = "AI Friend is thinking...";
    setTimeout(() => {
        let aiTake = pebblesRemaining % 4;
        if (aiTake === 0) aiTake = 1;

        pebblesRemaining -= aiTake;
        renderPebbles();

        if (pebblesRemaining === 0) {
            if (status) status.innerHTML = "<strong class='text-rose-400'>AI took the last pebble and won!</strong> Reset and try the multiple-of-4 strategy!";
        } else {
            if (status) status.innerHTML = `AI took <strong>${aiTake}</strong> pebble(s). <strong>${pebblesRemaining}</strong> left. Your turn! (Target leaving a multiple of 4!)`;
        }
    }, 600);
}

function resetPebblesGame() {
    pebblesRemaining = 15;
    renderPebbles();
    const status = document.getElementById('pebbleGameStatus');
    if (status) status.textContent = "Your turn! Pick 1, 2, or 3 pebbles.";
}

// SIM 15: Magic 9 Digit-Difference Engine
function calcDigitDiff() {
    const a = parseInt(document.getElementById('digitASelect').value, 10);
    const b = parseInt(document.getElementById('digitBSelect').value, 10);

    const num1 = a * 10 + b;
    const num2 = b * 10 + a;
    const diff = Math.abs(num1 - num2);
    const digitDiff = Math.abs(a - b);

    const eqEl = document.getElementById('diffEquation');
    const mulEl = document.getElementById('diffMultiple');
    const proofEl = document.getElementById('diffProof');

    if (eqEl) eqEl.textContent = `${num1} − ${num2} = ${diff}`;
    if (mulEl) mulEl.textContent = `${diff} = 9 × ${digitDiff}`;
    if (proofEl) proofEl.textContent = `Notice: 9 × (${a} − ${b}) = 9 × ${digitDiff} = ${diff}!`;
}

// SIM 16: King's Horses Stable Trick
function setStableConfig(type) {
    const cells = {
        TL: document.getElementById('valTL'),
        TM: document.getElementById('valTM'),
        TR: document.getElementById('valTR'),
        ML: document.getElementById('valML'),
        MR: document.getElementById('valMR'),
        BL: document.getElementById('valBL'),
        BM: document.getElementById('valBM'),
        BR: document.getElementById('valBR'),
    };

    let vals = { TL: 0, TM: 5, TR: 0, ML: 5, MR: 5, BL: 0, BM: 5, BR: 0 };
    if (type === 'stolen_18') {
        vals = { TL: 1, TM: 3, TR: 1, ML: 4, MR: 4, BL: 0, BM: 5, BR: 0 };
    } else if (type === 'stolen_16') {
        vals = { TL: 1, TM: 3, TR: 1, ML: 3, MR: 3, BL: 1, BM: 3, BR: 1 };
    }

    Object.keys(cells).forEach(k => {
        if (cells[k]) cells[k].textContent = vals[k];
    });

    const topSum = vals.TL + vals.TM + vals.TR;
    const botSum = vals.BL + vals.BM + vals.BR;
    const leftSum = vals.TL + vals.ML + vals.BL;
    const rightSum = vals.TR + vals.MR + vals.BR;

    const topEl = document.getElementById('sumTop');
    const botEl = document.getElementById('sumBottom');
    const leftEl = document.getElementById('sumLeft');
    const rightEl = document.getElementById('sumRight');

    if (topEl) topEl.textContent = `${topSum} horses ✓`;
    if (botEl) botEl.textContent = `${botSum} horses ✓`;
    if (leftEl) leftEl.textContent = `${leftSum} horses ✓`;
    if (rightEl) rightEl.textContent = `${rightSum} horses ✓`;
}

// Document Ready Initialization
document.addEventListener('DOMContentLoaded', () => {
    showSlide(1);

    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            selectedMaleVoice = getBestMaleVoice();
            populateVoiceList();
        };
        selectedMaleVoice = getBestMaleVoice();
        populateVoiceList();
    }

    // Initialize Simulator Initial States
    renderThousandBlocks();
    renderAbacus();
    renderPebbles();
    updateSwapUI();

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

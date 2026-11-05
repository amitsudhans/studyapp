"""
Interactive JavaScript Engine for NCERT Class 5 Mathematics Chapter 2: Fractions
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

    const progBar = document.getElementById('slideProgressBar');
    if (progBar) progBar.style.width = `${(n / totalSlides) * 100}%`;

    const countDisp = document.getElementById('slideCounterDisplay');
    if (countDisp) countDisp.textContent = `Slide ${n} of ${totalSlides}`;

    const jumpSel = document.getElementById('slideJumpSelect');
    if (jumpSel) jumpSel.value = n;

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
// BESPOKE 16 SIMULATORS (Class 5 Maths Ch 2)
// ==========================================

// SIM 1: Equal Wholes (Paratha Sizer)
function setParathaSizes(smallWeight, largeWeight) {
    const pSmall = document.getElementById('parathaSmall');
    const pLarge = document.getElementById('parathaLarge');
    const wSmall = document.getElementById('weightSmall');
    const wLarge = document.getElementById('weightLarge');
    const status = document.getElementById('sim1Status');

    if (wSmall) wSmall.textContent = `${smallWeight / 2} grams of food`;
    if (wLarge) wLarge.textContent = `${largeWeight / 2} grams of food`;

    if (smallWeight === largeWeight) {
        if (pSmall) { pSmall.className = "relative w-28 h-28 rounded-full bg-amber-700/60 border-2 border-emerald-500 flex items-center justify-center overflow-hidden transition-all duration-300"; }
        if (pLarge) { pLarge.className = "relative w-28 h-28 rounded-full bg-amber-700/60 border-2 border-emerald-500 flex items-center justify-center overflow-hidden transition-all duration-300"; }
        if (status) {
            status.innerHTML = "<strong>Fair Comparison!</strong> Both parathas are identical (200g each), so 1/2 = 100g for both! Wholes are identical &check;";
        }
    } else {
        if (pSmall) { pSmall.className = "relative w-24 h-24 rounded-full bg-amber-700/60 border-2 border-amber-500/80 flex items-center justify-center overflow-hidden transition-all duration-300"; }
        if (pLarge) { pLarge.className = "relative w-36 h-36 rounded-full bg-amber-700/60 border-2 border-sky-400 flex items-center justify-center overflow-hidden transition-all duration-300"; }
        if (status) {
            status.innerHTML = "Both eat 1/2 of their paratha, but 150g is <strong>3 times more</strong> than 50g! Wholes must be identical to compare fractions fairly.";
        }
    }
}

// SIM 2: Square Grid Painter
let activeGridType = 'A';
let currentShadedCount = 0;
let totalGridSquares = 16;

function switchGrid(type) {
    activeGridType = type;
    const btnA = document.getElementById('tabGridA');
    const btnB = document.getElementById('tabGridB');
    const btnC = document.getElementById('tabGridC');

    if (btnA) btnA.className = type === 'A' ? "px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white" : "px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300";
    if (btnB) btnB.className = type === 'B' ? "px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white" : "px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300";
    if (btnC) btnC.className = type === 'C' ? "px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white" : "px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300";

    if (type === 'A') totalGridSquares = 16;
    else if (type === 'B') totalGridSquares = 24;
    else if (type === 'C') totalGridSquares = 36;

    currentShadedCount = 0;
    renderGrid();
}

function renderGrid() {
    const canvas = document.getElementById('gridCanvas');
    const countDisp = document.getElementById('shadedCountDisplay');
    const totalDisp = document.getElementById('totalSquaresDisplay');
    const fracDisp = document.getElementById('gridFractionDisplay');

    if (countDisp) countDisp.textContent = currentShadedCount;
    if (totalDisp) totalDisp.textContent = totalGridSquares;

    let cols = 4;
    if (activeGridType === 'B') cols = 6;
    else if (activeGridType === 'C') cols = 6;

    if (canvas) {
        canvas.style.gridTemplateColumns = `repeat(${cols}, minmax(0, 1fr))`;
        canvas.innerHTML = '';
        for (let i = 0; i < totalGridSquares; i++) {
            const sq = document.createElement('div');
            const isShaded = i < currentShadedCount;
            sq.className = `w-7 h-7 rounded border transition cursor-pointer flex items-center justify-center text-[10px] font-bold ${
                isShaded ? 'bg-indigo-500 border-indigo-400 text-white' : 'bg-slate-900 border-slate-800 text-slate-600 hover:border-slate-700'
            }`;
            sq.textContent = i + 1;
            sq.onclick = () => {
                currentShadedCount = isShaded ? i : i + 1;
                renderGrid();
            };
            canvas.appendChild(sq);
        }
    }

    if (fracDisp) {
        if (currentShadedCount === 0) {
            fracDisp.textContent = `0/${totalGridSquares} = 0`;
        } else {
            // Simplify fraction
            const gcd = (a, b) => b ? gcd(b, a % b) : a;
            const div = gcd(currentShadedCount, totalGridSquares);
            const simNum = currentShadedCount / div;
            const simDen = totalGridSquares / div;
            fracDisp.textContent = `${currentShadedCount}/${totalGridSquares}${div > 1 ? ` = ${simNum}/${simDen}` : ''}`;
        }
    }
}

function presetShade(count) {
    currentShadedCount = count;
    renderGrid();
}

function clearGridShading() {
    currentShadedCount = 0;
    renderGrid();
}

// SIM 3: Fraction Strip Kit
let kitPieces = [];

function addKitPiece(label, percent, styleClass) {
    const currentTotal = kitPieces.reduce((acc, p) => acc + p.percent, 0);
    if (currentTotal + percent > 100.01) {
        alert("Adding this piece would overflow the whole strip! Reset or choose a smaller piece.");
        return;
    }

    kitPieces.push({ label, percent, styleClass });
    renderKit();
}

function renderKit() {
    const bench = document.getElementById('kitWorkbench');
    const fillDisp = document.getElementById('kitFillPercent');
    const status = document.getElementById('kitStatusText');

    const total = kitPieces.reduce((acc, p) => acc + p.percent, 0);

    if (fillDisp) fillDisp.textContent = `${total.toFixed(1)}% Filled`;

    if (bench) {
        bench.innerHTML = '';
        kitPieces.forEach((p) => {
            const el = document.createElement('div');
            el.style.width = `${p.percent}%`;
            el.className = `h-full ${p.styleClass} border-r flex items-center justify-center font-mono font-bold text-xs truncate transition-all`;
            el.textContent = p.label;
            bench.appendChild(el);
        });
    }

    if (status) {
        if (Math.abs(total - 100) < 0.1) {
            status.innerHTML = "<strong class='text-emerald-400'>Perfect Whole Reached! &check;</strong> Your assembled pieces equal exactly 100% (1 Whole Strip)!";
        } else {
            status.textContent = `Current total: ${total.toFixed(1)}%. Keep adding pieces to reach 100%!`;
        }
    }
}

function resetKit() {
    kitPieces = [];
    renderKit();
}

// SIM 4: Piece Relations Bench
function highlightRelation(rel) {
    const status = document.getElementById('benchRelationStatus');
    const h1 = document.getElementById('benchHalf1');
    const f1 = document.getElementById('benchFourth1');
    const f2 = document.getElementById('benchFourth2');
    const e1 = document.getElementById('benchEighth1');
    const e2 = document.getElementById('benchEighth2');
    const e3 = document.getElementById('benchEighth3');
    const e4 = document.getElementById('benchEighth4');

    // Reset styles
    [h1, f1, f2, e1, e2, e3, e4].forEach(el => {
        if (el) el.classList.remove('ring-2', 'ring-amber-400', 'bg-amber-500/40');
    });

    if (rel === 'two_fourths') {
        if (h1) h1.classList.add('ring-2', 'ring-amber-400');
        if (f1) f1.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500/40');
        if (f2) f2.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500/40');
        if (status) status.innerHTML = "<strong>Verified:</strong> Exactly <strong>two 1/4 pieces</strong> match the length of <strong>one 1/2 piece</strong> (2/4 = 1/2)!";
    } else if (rel === 'four_eighths') {
        if (h1) h1.classList.add('ring-2', 'ring-amber-400');
        [e1, e2, e3, e4].forEach(el => { if (el) el.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500/40'); });
        if (status) status.innerHTML = "<strong>Verified:</strong> Exactly <strong>four 1/8 pieces</strong> equal <strong>one 1/2 piece</strong> (4/8 = 1/2)!";
    } else if (rel === 'two_eighths') {
        if (f1) f1.classList.add('ring-2', 'ring-amber-400');
        if (e1) e1.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500/40');
        if (e2) e2.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500/40');
        if (status) status.innerHTML = "<strong>Verified:</strong> Exactly <strong>two 1/8 pieces</strong> equal <strong>one 1/4 piece</strong> (2/8 = 1/4)!";
    }
}

// SIM 5: Whole-Building Puzzle Box
let wholeBuildTwelfths = 0;
let wholeBuildSteps = [];

function addWholeBuildPart(twelfths, label) {
    if (wholeBuildTwelfths + twelfths > 12) {
        alert("That piece would exceed 1 Whole! Click reset to try another combination.");
        return;
    }

    wholeBuildTwelfths += twelfths;
    wholeBuildSteps.push(label);
    renderWholeBuild();
}

function renderWholeBuild() {
    const progBar = document.getElementById('wholeBuildProgressBar');
    const progText = document.getElementById('wholeBuildProgressText');
    const status = document.getElementById('wholeBuildStatus');

    const pct = (wholeBuildTwelfths / 12) * 100;
    if (progBar) progBar.style.width = `${pct}%`;
    if (progText) progText.textContent = `${wholeBuildTwelfths} / 12 (${pct.toFixed(0)}%)`;

    if (status) {
        if (wholeBuildTwelfths === 12) {
            status.innerHTML = `<strong class='text-emerald-400'>1 Whole Completed! 🎉</strong> Recipe: ${wholeBuildSteps.join(' + ')} = 12/12 = 1!`;
        } else {
            status.textContent = `Current pieces: ${wholeBuildSteps.join(' + ') || 'None'}. Still need ${(12 - wholeBuildTwelfths)}/12 to complete 1 Whole!`;
        }
    }
}

function resetWholeBuild() {
    wholeBuildTwelfths = 0;
    wholeBuildSteps = [];
    renderWholeBuild();
}

// SIM 6: Equivalent Fractions Slicer
function setEquivRows(rows) {
    const box = document.getElementById('equivSliceBox');
    const txt = document.getElementById('equivFractionText');
    const formula = document.getElementById('equivSliceFormula');

    let total = 3 * rows;
    let shaded = 1 * rows;

    if (box) {
        box.innerHTML = '';
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < 3; c++) {
                const cell = document.createElement('div');
                const isShaded = (c === 0);
                cell.className = `border-r border-b border-slate-600 transition ${isShaded ? 'bg-cyan-500/40' : 'bg-transparent'}`;
                box.appendChild(cell);
            }
        }
    }

    if (txt) txt.textContent = `${shaded}/${total}`;
    if (formula) formula.textContent = `${shaded} shaded rectangles out of ${total} total rectangles (Same Area as 1/3!)`;
}

// SIM 7: Equivalence Scale
function setScalePair(leftFrac, rightFrac, missingVal, missingType, mult) {
    const lEl = document.getElementById('scaleFracLeft');
    const rEl = document.getElementById('scaleFracRight');
    const expEl = document.getElementById('scaleExplanation');
    const banner = document.getElementById('scaleResultBanner');

    if (lEl) lEl.textContent = leftFrac;
    if (rEl) rEl.textContent = rightFrac;

    if (expEl) {
        if (missingType === 'num') {
            expEl.innerHTML = `Multiplier: &times; ${mult}. So top number is: ${leftFrac.split('/')[0]} &times; ${mult} = <strong class="text-amber-400">${missingVal}</strong>!`;
        } else {
            expEl.innerHTML = `Multiplier: &times; ${mult}. So bottom number is: ${leftFrac.split('/')[1]} &times; ${mult} = <strong class="text-amber-400">${missingVal}</strong>!`;
        }
    }

    if (banner) {
        banner.innerHTML = `Equivalence verified! <strong>${leftFrac} = ${rightFrac.replace('?', missingVal)}</strong> &check;`;
    }
}

// SIM 8: Same Denominator Chikki Slices
function setChikkiComparison(aarav, meera, den) {
    const numA = document.getElementById('numAaravDisplay');
    const numM = document.getElementById('numMeeraDisplay');
    const barA = document.getElementById('barAarav');
    const barM = document.getElementById('barMeera');
    const resDisp = document.getElementById('chikkiInequalityDisplay');

    if (numA) numA.textContent = aarav;
    if (numM) numM.textContent = meera;

    if (barA) barA.style.width = `${(aarav / den) * 100}%`;
    if (barM) barM.style.width = `${(meera / den) * 100}%`;

    if (resDisp) {
        if (aarav < meera) {
            resDisp.innerHTML = `${aarav}/${den} &lt; ${meera}/${den} (Meera has more chikki!)`;
        } else if (aarav > meera) {
            resDisp.innerHTML = `${aarav}/${den} &gt; ${meera}/${den} (Aarav has more chikki!)`;
        } else {
            resDisp.innerHTML = `${aarav}/${den} = ${meera}/${den} (Both have equal shares!)`;
        }
    }
}

// SIM 9: Same Numerator Slice Comparator
function setSameNumCompare(num, den1, den2) {
    const disp = document.getElementById('sameNumResultDisplay');
    if (disp) {
        const val1 = num / den1;
        const val2 = num / den2;
        if (val1 < val2) {
            disp.innerHTML = `${num}/${den1} &lt; ${num}/${den2} (Since 1/${den1} &lt; 1/${den2}, ${num} slices of 1/${den2} is greater!)`;
        } else if (val1 > val2) {
            disp.innerHTML = `${num}/${den1} &gt; ${num}/${den2} (Since 1/${den1} &gt; 1/${den2}, ${num} slices of 1/${den1} is greater!)`;
        } else {
            disp.innerHTML = `${num}/${den1} = ${num}/${den2} (Equal values)`;
        }
    }
}

// SIM 10: Improper Paratha Bundler
function setImproperSlices(slices, den) {
    const countDisp = document.getElementById('improperCountDisplay');
    const cont = document.getElementById('parathaBundleContainer');
    const mixedDisp = document.getElementById('mixedNumberDisplay');

    if (countDisp) countDisp.textContent = `${slices} slices (${slices}/${den})`;

    const wholes = Math.floor(slices / den);
    const remainder = slices % den;

    if (cont) {
        cont.innerHTML = '';
        for (let w = 0; w < wholes; w++) {
            const wholeCircle = document.createElement('div');
            wholeCircle.className = "w-14 h-14 rounded-full bg-amber-500/30 border-2 border-amber-400 flex items-center justify-center text-xs font-bold text-amber-200";
            wholeCircle.textContent = "1 Whole";
            cont.appendChild(wholeCircle);
        }

        if (remainder > 0) {
            const remCircle = document.createElement('div');
            remCircle.className = "w-14 h-14 rounded-full bg-slate-800 border-2 border-dashed border-sky-400 flex items-center justify-center text-xs font-bold text-sky-300";
            remCircle.textContent = `${remainder}/${den}`;
            cont.appendChild(remCircle);
        }
    }

    if (mixedDisp) {
        if (remainder === 0) {
            mixedDisp.textContent = `${slices}/${den} = ${wholes} Whole${wholes > 1 ? 's' : ''}`;
        } else {
            mixedDisp.textContent = `${slices}/${den} = ${wholes} Whole${wholes > 1 ? 's' : ''} and ${remainder}/${den} (${wholes} ${remainder}/${den})`;
        }
    }
}

// SIM 11: Number Line Mixed Number Plotter
function plotOnLine(num, den, improperStr, mixedStr, xPos) {
    const pin = document.getElementById('linePlotPin');
    const label = document.getElementById('pinLabel');
    const mixedText = document.getElementById('plotMixedText');

    if (pin) pin.setAttribute('transform', `translate(${xPos}, 0)`);
    if (label) label.textContent = improperStr;
    if (mixedText) mixedText.textContent = `${improperStr} = ${mixedStr}`;
}

// SIM 12: Benchmark 1 Balance Scale
function setBenchmark1(fracA, fracB, op) {
    const aEl = document.getElementById('benchAFraction');
    const bEl = document.getElementById('benchBFraction');
    const aV = document.getElementById('benchAVerdict');
    const bV = document.getElementById('benchBVerdict');
    const res = document.getElementById('benchmarkComparisonResult');

    if (aEl) aEl.textContent = fracA;
    if (bEl) bEl.textContent = fracB;

    const parseF = (f) => {
        const [n, d] = f.split('/').map(Number);
        return n / d;
    };

    const valA = parseF(fracA);
    const valB = parseF(fracB);

    if (aV) aV.textContent = valA < 1 ? "< 1 (Proper)" : "> 1 (Improper)";
    if (bV) bV.textContent = valB < 1 ? "< 1 (Proper)" : "> 1 (Improper)";

    if (res) {
        res.innerHTML = `Conclusion: <strong>${fracA} ${op} ${fracB}</strong> verified via Benchmark 1!`;
    }
}

// SIM 13: Benchmark 1/2 Gauge
function testHalfBenchmark(num, den, fracStr) {
    const fEl = document.getElementById('halfGaugeFraction');
    const bEl = document.getElementById('halfGaugeBadge');

    if (fEl) fEl.textContent = fracStr;

    const halfDen = den / 2;
    if (bEl) {
        if (num > halfDen) {
            bEl.className = "p-2.5 bg-emerald-950/60 border border-emerald-500/40 rounded-lg text-xs font-bold text-emerald-300";
            bEl.textContent = `Verdict: ${fracStr} is GREATER THAN 1/2 (> 1/2)`;
        } else if (num < halfDen) {
            bEl.className = "p-2.5 bg-rose-950/60 border border-rose-500/40 rounded-lg text-xs font-bold text-rose-300";
            bEl.textContent = `Verdict: ${fracStr} is LESS THAN 1/2 (< 1/2)`;
        } else {
            bEl.className = "p-2.5 bg-blue-950/60 border border-blue-500/40 rounded-lg text-xs font-bold text-blue-300";
            bEl.textContent = `Verdict: ${fracStr} is EXACTLY EQUAL to 1/2 (= 1/2)`;
        }
    }
}

// SIM 14: Ant Parade Ruler March
function setAntCount(count) {
    const track = document.getElementById('antTrack');
    const countDisp = document.getElementById('antCountDisplay');
    const lengthDisp = document.getElementById('antTotalLength');

    if (countDisp) countDisp.textContent = `${count} ants`;

    const totalCm = count * 0.25;
    if (lengthDisp) lengthDisp.textContent = `${count} × 1/4 = ${totalCm} cm`;

    if (track) {
        track.innerHTML = '';
        for (let i = 0; i < count; i++) {
            const ant = document.createElement('span');
            ant.className = "text-xs px-1 py-0.5 bg-amber-950/70 border border-amber-600/40 rounded text-amber-300 font-mono";
            ant.textContent = "🐜 1/4";
            track.appendChild(ant);
        }
    }
}

// SIM 15: Family Riddle Deduction Tree
function revealRiddleStep(step) {
    const s1 = document.getElementById('riddleStep1');
    const s2 = document.getElementById('riddleStep2');
    const s3 = document.getElementById('riddleStep3');
    const banner = document.getElementById('riddleSolutionBanner');

    if (step >= 1 && s1) s1.className = "p-2.5 rounded-lg bg-purple-950/70 border border-purple-500/60 transition";
    if (step >= 2 && s2) s2.className = "p-2.5 rounded-lg bg-purple-950/70 border border-purple-500/60 transition";
    if (step >= 3 && s3) {
        s3.className = "p-2.5 rounded-lg bg-emerald-950/70 border border-emerald-500/60 transition";
        if (banner) banner.classList.remove('hidden');
    }
}

function resetRiddleSteps() {
    const s1 = document.getElementById('riddleStep1');
    const s2 = document.getElementById('riddleStep2');
    const s3 = document.getElementById('riddleStep3');
    const banner = document.getElementById('riddleSolutionBanner');

    if (s1) s1.className = "p-2.5 rounded-lg bg-slate-950 border border-slate-800 transition";
    if (s2) s2.className = "p-2.5 rounded-lg bg-slate-950 border border-slate-800 transition";
    if (s3) s3.className = "p-2.5 rounded-lg bg-slate-950 border border-slate-800 transition";
    if (banner) banner.classList.add('hidden');
}

// SIM 16: All-in-One Fraction Laboratory
function updateLabFraction() {
    const numSlider = document.getElementById('labNumSlider');
    const denSlider = document.getElementById('labDenSlider');
    const numVal = document.getElementById('labNumVal');
    const denVal = document.getElementById('labDenVal');
    const fracDisp = document.getElementById('labFractionDisplay');
    const typeDisp = document.getElementById('labTypeDisplay');
    const halfDisp = document.getElementById('labHalfStatus');
    const barFill = document.getElementById('labBarFill');

    const num = parseInt(numSlider.value, 10);
    const den = parseInt(denSlider.value, 10);

    if (numVal) numVal.textContent = num;
    if (denVal) denVal.textContent = den;
    if (fracDisp) fracDisp.textContent = `${num} / ${den}`;

    if (typeDisp) {
        if (num < den) typeDisp.textContent = "Type: Proper Fraction (< 1)";
        else if (num === den) typeDisp.textContent = "Type: Exactly 1 Whole (= 1)";
        else typeDisp.textContent = `Type: Improper Fraction (> 1) = ${Math.floor(num / den)} ${num % den}/${den}`;
    }

    if (halfDisp) {
        const half = den / 2;
        if (num > half) halfDisp.textContent = `Comparison to 1/2: ${num}/${den} > 1/2`;
        else if (num < half) halfDisp.textContent = `Comparison to 1/2: ${num}/${den} < 1/2`;
        else halfDisp.textContent = `Comparison to 1/2: ${num}/${den} = 1/2`;
    }

    if (barFill) {
        const pct = Math.min((num / den) * 100, 100);
        barFill.style.width = `${pct}%`;
    }
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

    // Initialize Simulator States
    renderGrid();
    renderKit();
    setImproperSlices(5, 2);
    setAntCount(16);
    updateLabFraction();

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


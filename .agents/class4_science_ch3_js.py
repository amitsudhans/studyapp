# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 3: Nature Trail
Compiled JS Engine String
"""

JS_ENGINE = '''
// ============================================================================
// State Management & Audio Setup
// ============================================================================
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;

// Audio SFX Synthesizer
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playSuccessSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1);
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2);
        
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        
        osc.start(now);
        osc.stop(now + 0.35);
    } catch(e) {}
}

function playErrorSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(146.83, now + 0.2);
        
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
        
        osc.start(now);
        osc.stop(now + 0.25);
    } catch(e) {}
}

function playClickSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        gain.gain.setValueAtTime(0.06, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        
        osc.start(now);
        osc.stop(now + 0.08);
    } catch(e) {}
}

// ============================================================================
// Indian English Male Teacher Voice Engine
// ============================================================================
const femaleTerms = [
    'female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'victoria', 
    'kavya', 'priya', 'swara', 'veena', 'neerja', 'heera', 'ananya', 'aditi',
    'sangeeta', 'vani', 'maya', 'shravani', 'shruti', 'alva', 'karen', 'moira', 'tessa'
];

function selectIndianMaleVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const maleIndianNames = ['prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'karan', 'mohan', 'deepak', 'kumar'];
    for (const name of maleIndianNames) {
        const found = voices.find(v => {
            const vName = v.name.toLowerCase();
            const isFemale = femaleTerms.some(f => vName.includes(f));
            return !isFemale && vName.includes(name);
        });
        if (found) return found;
    }

    const anyIndian = voices.find(v => {
        const vName = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => vName.includes(f));
        return !isFemale && lang.includes('en-in');
    });
    if (anyIndian) return anyIndian;

    const globalMaleNames = ['google uk english male', 'microsoft david', 'microsoft mark', 'microsoft george', 'daniel', 'oliver', 'alex'];
    for (const name of globalMaleNames) {
        const found = voices.find(v => {
            const vName = v.name.toLowerCase();
            const isFemale = femaleTerms.some(f => vName.includes(f));
            return !isFemale && vName.includes(name);
        });
        if (found) return found;
    }

    const fallback = voices.find(v => {
        const vName = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => vName.includes(f));
        return !isFemale && lang.startsWith('en');
    });
    return fallback || voices[0];
}

function stopAudioLecture() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    clearInterval(keepAliveTimer);
    isSpeaking = false;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (playing) {
        btn.classList.add('bg-rose-600', 'text-white', 'animate-pulse');
        btn.classList.remove('bg-emerald-600');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8 7a1 1 0 00-1 1v4a1 1 0 001 1h4a1 1 0 001-1V8a1 1 0 00-1-1H8z" clip-rule="evenodd"></path></svg>
            Stop Audio
        `;
    } else {
        btn.classList.remove('bg-rose-600', 'animate-pulse');
        btn.classList.add('bg-emerald-600', 'text-white');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
            Audio Lecture
        `;
    }
}

function playAudioLecture() {
    if (!('speechSynthesis' in window)) {
        alert('Web Speech API is not supported in this browser.');
        return;
    }
    
    if (isSpeaking) {
        stopAudioLecture();
        return;
    }
    
    const slide = SLIDES.find(s => s.id === currentSlide);
    if (!slide || !slide.speech || slide.speech.trim() === '') {
        return;
    }
    
    window.speechSynthesis.cancel();
    clearInterval(keepAliveTimer);
    
    currentUtterance = new SpeechSynthesisUtterance(slide.speech);
    currentUtterance.pitch = 0.85; // Low pitch male educator
    currentUtterance.rate = 0.94;  // Measured classroom tempo
    
    const voice = selectIndianMaleVoice();
    if (voice) {
        currentUtterance.voice = voice;
        currentUtterance.lang = voice.lang || 'en-IN';
    }
    
    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioButtonUI(true);
    };
    
    currentUtterance.onend = () => {
        stopAudioLecture();
    };
    
    currentUtterance.onerror = (e) => {
        console.warn('Speech error:', e);
        stopAudioLecture();
    };
    
    window.speechSynthesis.speak(currentUtterance);
    
    // Chrome keep-alive watchdog timer
    keepAliveTimer = setInterval(() => {
        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        }
    }, 9000);
}

// ============================================================================
// Slide Navigation & Terminal Slide Invariant
// ============================================================================
function showSlide(num) {
    if (num < 1 || num > totalSlides) return;
    stopAudioLecture();
    
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));
    
    const target = document.getElementById(`slide-${num}`);
    if (target) {
        target.classList.remove('hidden');
    }
    
    currentSlide = num;
    const curNumEl = document.getElementById('currentSlideNum');
    if (curNumEl) curNumEl.innerText = currentSlide;
    
    const progressPct = (currentSlide / totalSlides) * 100;
    const pbar = document.getElementById('chapterProgressBar');
    if (pbar) pbar.style.width = `${progressPct}%`;
    
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
            prevBtn.disabled = true;
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
            prevBtn.disabled = false;
        }
    }
    
    // Terminal Slide Invariant (Strict Rule for Slide 20)
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }
    
    // Hide audio button on challenge slides (17-20)
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.classList.add('hidden');
        } else {
            audioBtn.classList.remove('hidden');
        }
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
    initSimulatorForSlide(currentSlide);
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        playClickSfx();
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        playClickSfx();
        showSlide(currentSlide - 1);
    }
}

// ============================================================================
// Checkpoint & Challenge Quiz Verification Handlers
// ============================================================================
function checkCheckpoint(slideId, cpIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints || !slide.checkpoints[cpIdx]) return;
    
    const cp = slide.checkpoints[cpIdx];
    const fb = document.getElementById(`cp-fb-${slideId}-${cpIdx}`);
    const btns = document.querySelectorAll(`.cp-btn-${slideId}-${cpIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = cp.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${cp.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Not quite.</strong> ${cp.exp}`;
    }
}

function checkQuiz(slideId, qIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const fb = document.getElementById(`qz-fb-${slideId}-${qIdx}`);
    const solBtn = document.getElementById(`qz-sol-btn-${slideId}-${qIdx}`);
    const btns = document.querySelectorAll(`.qz-btn-${slideId}-${qIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = qz.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${qz.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Not quite.</strong> ${qz.exp}`;
    }
    
    if (solBtn) {
        solBtn.classList.remove('hidden');
    }
}

function showSolutionModal(slideId, qIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('modalQuestionTitle');
    const content = document.getElementById('modalSolutionContent');
    
    if (modal && title && content) {
        playClickSfx();
        title.innerText = `Question ${qIdx + 1}: ${qz.q}`;
        content.innerHTML = qz.sol;
        modal.classList.remove('hidden');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

function toggleHint(slideId, qIdx) {
    const hintEl = document.getElementById(`qz-hint-${slideId}-${qIdx}`);
    if (hintEl) {
        playClickSfx();
        hintEl.classList.toggle('hidden');
    }
}

// ============================================================================
// Simulator Handlers (Slides 1 to 16)
// ============================================================================

// --- Sim 1: Pachmarhi Biosphere Explorer ---
const pachmarhiSpots = {
    cliffs: {
        title: "Sandstone Cliffs",
        desc: "Towering prehistoric rock shelters in the Satpura range shelter ancient cave art and provide safe roosts for eagles and vultures.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <polygon points="20,90 70,20 120,90" fill="#78350f"/>
            <polygon points="90,90 150,15 210,90" fill="#92400e"/>
            <polygon points="180,90 230,35 280,90" fill="#b45309"/>
            <circle cx="150" cy="12" r="3" fill="#cbd5e1"/>
            <path d="M145,14 Q150,10 155,14" stroke="#f8fafc" stroke-width="1.5" fill="none"/>
            <text x="160" y="93" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Satpura Sandstone Escarpments</text>
        </svg>`
    },
    waterfall: {
        title: "Duchess Falls",
        desc: "Perennial mountain cascades tumble over rocky ravines, providing fresh drinking water and humid microclimates for ferns and mosses.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="30" y="10" width="80" height="80" fill="#334155"/>
            <rect x="210" y="10" width="80" height="80" fill="#334155"/>
            <!-- Waterfall cascade -->
            <rect x="110" y="10" width="100" height="65" fill="#38bdf8" opacity="0.8"/>
            <line x1="125" y1="10" x2="125" y2="75" stroke="#ffffff" stroke-width="2" stroke-dasharray="8,4"/>
            <line x1="145" y1="10" x2="145" y2="75" stroke="#ffffff" stroke-width="2" stroke-dasharray="10,5"/>
            <line x1="165" y1="10" x2="165" y2="75" stroke="#ffffff" stroke-width="2" stroke-dasharray="6,3"/>
            <line x1="185" y1="10" x2="185" y2="75" stroke="#ffffff" stroke-width="2" stroke-dasharray="8,4"/>
            <ellipse cx="160" cy="80" rx="60" ry="12" fill="#0284c7"/>
            <text x="160" y="95" fill="#bae6fd" font-size="8" font-weight="bold" text-anchor="middle">Crystal Stream Pool</text>
        </svg>`
    },
    canopy: {
        title: "Teak & Sal Forest Canopy",
        desc: "Towering deciduous trees form a dense green shield, filtering sunlight and nurturing diverse epiphytes, mushrooms, and climbing vines.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Trunks -->
            <rect x="65" y="45" width="10" height="45" fill="#78350f"/><rect x="155" y="40" width="12" height="50" fill="#78350f"/><rect x="245" y="45" width="10" height="45" fill="#78350f"/>
            <!-- Canopies -->
            <circle cx="70" cy="35" r="28" fill="#15803d" opacity="0.9"/>
            <circle cx="161" cy="30" r="34" fill="#16a34a" opacity="0.95"/>
            <circle cx="250" cy="35" r="28" fill="#15803d" opacity="0.9"/>
            <text x="160" y="93" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Primary Teak & Sal Canopy</text>
        </svg>`
    },
    dhoopgarh: {
        title: "Dhoopgarh Peak (1,352 m)",
        desc: "The highest summit in Madhya Pradesh and the Satpura range, offering panoramic vistas of sunrise, sunset, and endless forest ridges.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Golden Rising Sun -->
            <circle cx="160" cy="35" r="22" fill="#f59e0b"/>
            <polygon points="30,90 160,28 290,90" fill="#1e293b"/>
            <polygon points="120,90 160,35 200,90" fill="#334155"/>
            <text x="160" y="75" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Highest Satpura Summit: 1,352 m</text>
        </svg>`
    }
};

function selectPachmarhiSpot(spot) {
    const data = pachmarhiSpots[spot];
    if (!data) return;
    playClickSfx();
    
    ['cliffs', 'waterfall', 'canopy', 'dhoopgarh'].forEach(k => {
        const btn = document.getElementById(`pbe-btn-${k}`);
        if (!btn) return;
        if (k === spot) {
            btn.className = "p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('pbe-visual-box');
    const iBox = document.getElementById('pbe-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-emerald-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 2: Forest Safety & Etiquette ---
const forestRules = {
    silence: {
        title: "Keep Quiet & Walk Softly",
        desc: "Speak in soft murmurs so wild animals are not startled into flight. Quiet observation rewards naturalists with intimate glimpses of wildlife.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="80" y="30" width="160" height="40" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
            <text x="160" y="47" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">SOUND LEVEL: &lt; 40 dB</text>
            <text x="160" y="60" fill="#4ade80" font-size="7" text-anchor="middle">Safe, Whisper-Quiet Trail Walking</text>
        </svg>`
    },
    nofeed: {
        title: "Do Not Feed Wild Animals",
        desc: "Human snacks contain salt, processed sugars, and artificial chemicals that cause digestive sickness and turn animals into aggressive beggars.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="50" r="28" fill="#fee2e2" stroke="#ef4444" stroke-width="4"/>
            <line x1="140" y1="32" x2="180" y2="68" stroke="#ef4444" stroke-width="4"/>
            <text x="160" y="55" fill="#b91c1c" font-size="16" font-weight="bold" text-anchor="middle">🍞</text>
            <text x="160" y="90" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">No Human Food For Wildlife</text>
        </svg>`
    },
    noplastic: {
        title: "No Polythene or Plastic Bags",
        desc: "Plastic litter never decomposes. Wild herbivores accidentally ingest plastic bags smelling of food, leading to fatal digestive blockages.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="50" r="28" fill="#fee2e2" stroke="#dc2626" stroke-width="4"/>
            <line x1="140" y1="32" x2="180" y2="68" stroke="#dc2626" stroke-width="4"/>
            <text x="160" y="55" fill="#991b1b" font-size="16" font-weight="bold" text-anchor="middle">🛍️</text>
            <text x="160" y="90" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Zero Single-Use Plastic Zone</text>
        </svg>`
    },
    trail: {
        title: "Stay on Marked Paths",
        desc: "Straying off trail crushes fragile seedlings, disturbs hidden bird nests in bushes, and risks stepping on camouflaged vipers or thorny vines.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Path between grass -->
            <rect x="20" y="20" width="280" height="60" fill="#14532d"/>
            <polygon points="120,80 145,20 175,20 200,80" fill="#78350f"/>
            <text x="160" y="55" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">MARKED HIKING TRAIL</text>
        </svg>`
    }
};

function selectForestRule(rule) {
    const data = forestRules[rule];
    if (!data) return;
    playClickSfx();
    
    ['silence', 'nofeed', 'noplastic', 'trail'].forEach(k => {
        const btn = document.getElementById(`fse-btn-${k}`);
        if (!btn) return;
        if (k === rule) {
            btn.className = "p-2.5 rounded-xl border border-amber-500 bg-amber-950/40 text-amber-300 font-bold ring-2 ring-amber-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('fse-visual-box');
    const iBox = document.getElementById('fse-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-amber-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 3: Forest Wildlife Classifier ---
const animalStrata = {
    terrestrial: {
        title: "Terrestrial Dwellers (Forest Floor)",
        desc: "Spotted deer (chital), sambar, and wild boars graze along the leaf-strewn forest floor, alert to nearby feline predators.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="10" y="65" width="300" height="25" fill="#334155"/>
            <!-- Spotted Deer Silhouette -->
            <ellipse cx="140" cy="55" rx="22" ry="14" fill="#d97706"/>
            <circle cx="170" cy="42" r="8" fill="#d97706"/>
            <!-- Antlers -->
            <line x1="172" y1="36" x2="180" y2="22" stroke="#78350f" stroke-width="2"/>
            <line x1="178" y1="28" x2="185" y2="28" stroke="#78350f" stroke-width="2"/>
            <!-- Legs -->
            <line x1="125" y1="65" x2="125" y2="85" stroke="#b45309" stroke-width="3"/><line x1="155" y1="65" x2="155" y2="85" stroke="#b45309" stroke-width="3"/>
            <!-- White Spots -->
            <circle cx="132" cy="52" r="1.5" fill="#f8fafc"/><circle cx="142" cy="54" r="1.5" fill="#f8fafc"/><circle cx="150" cy="51" r="1.5" fill="#f8fafc"/>
            <text x="160" y="93" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Herbivore Ground Forager</text>
        </svg>`
    },
    arboreal: {
        title: "Arboreal Inhabitants (Canopy Layer)",
        desc: "Gray langurs and Indian giant squirrels navigate treetops with strong leaping limbs and balancing tails, feeding on tender buds and fruits.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Tree Branch -->
            <rect x="20" y="55" width="280" height="12" rx="4" fill="#78350f"/>
            <!-- Monkey perched on branch -->
            <ellipse cx="150" cy="42" rx="14" ry="18" fill="#94a3b8"/>
            <circle cx="150" cy="22" r="8" fill="#0f172a"/>
            <!-- Long tail looping down -->
            <path d="M140,50 Q130,75 145,85 Q155,90 150,80" fill="none" stroke="#64748b" stroke-width="3"/>
            <text x="160" y="94" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Canopy Tree Climber</text>
        </svg>`
    },
    aerial: {
        title: "Aerial Navigators (Sky Layer)",
        desc: "Raptor eagles, hornbills, and swifts rule the skies with aerodynamic feathers, pneumatic hollow bones, and exceptional long-distance vision.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Eagle soaring -->
            <path d="M90,40 Q160,20 230,40 Q160,55 90,40 Z" fill="#78350f"/>
            <circle cx="160" cy="42" r="6" fill="#fef08a"/>
            <polygon points="158,42 162,42 160,49" fill="#f59e0b"/>
            <text x="160" y="85" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Thermal Soaring Predator</text>
        </svg>`
    },
    aquatic: {
        title: "Aquatic Specialists (Streams & Ponds)",
        desc: "Gharials, river fish, freshwater turtles, and frogs inhabit forest rivers with streamlined bodies, webbed flippers, and gills.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="20" y="30" width="280" height="50" rx="8" fill="#0284c7" opacity="0.8"/>
            <!-- Fish swimming -->
            <ellipse cx="140" cy="55" rx="20" ry="10" fill="#f59e0b"/>
            <polygon points="120,55 105,45 105,65" fill="#d97706"/>
            <!-- Turtle -->
            <ellipse cx="210" cy="55" rx="14" ry="10" fill="#15803d"/>
            <circle cx="228" cy="55" r="4" fill="#16a34a"/>
            <text x="160" y="93" fill="#bae6fd" font-size="8" font-weight="bold" text-anchor="middle">Freshwater Wetland Specialists</text>
        </svg>`
    }
};

function selectAnimalStratum(stratum) {
    const data = animalStrata[stratum];
    if (!data) return;
    playClickSfx();
    
    ['terrestrial', 'arboreal', 'aerial', 'aquatic'].forEach(k => {
        const btn = document.getElementById(`fwc-btn-${k}`);
        if (!btn) return;
        if (k === stratum) {
            btn.className = "p-2.5 rounded-xl border border-cyan-500 bg-cyan-950/40 text-cyan-300 font-bold ring-2 ring-cyan-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('fwc-visual-box');
    const iBox = document.getElementById('fwc-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-cyan-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 4: Unique Creature Features ---
const uniqueCreatures = {
    elephant: {
        title: "Asian Elephant Trunk",
        desc: "Contains over 40,000 muscle units and zero bones, allowing the elephant to uproot trees or gently pick up a tiny blade of grass.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="120" cy="40" r="22" fill="#64748b"/>
            <circle cx="110" cy="35" r="3" fill="#0f172a"/>
            <!-- Long Curved Trunk -->
            <path d="M125,50 C125,85 170,85 175,65 C175,55 165,55 165,65" fill="none" stroke="#475569" stroke-width="12" stroke-linecap="round"/>
            <text x="210" y="55" fill="#93c5fd" font-size="8" font-weight="bold">40,000+ Muscle Units</text>
        </svg>`
    },
    squirrel: {
        title: "Indian Giant Squirrel (Pachmarhi)",
        desc: "Measuring up to a meter long, its magnificent multi-colored maroon fur coat and two-foot bushy tail provide critical balance for 6-meter leaps.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Body -->
            <ellipse cx="120" cy="50" rx="22" ry="14" fill="#881337"/>
            <circle cx="140" cy="42" r="8" fill="#9f1239"/>
            <!-- Huge Bushy Tail arching overhead -->
            <path d="M100,55 C70,20 85,-5 125,10 C145,20 150,30 140,40" fill="none" stroke="#4c0519" stroke-width="14" stroke-linecap="round"/>
            <text x="210" y="55" fill="#fda4af" font-size="8" font-weight="bold">2-Foot Balancing Tail</text>
        </svg>`
    },
    monkey: {
        title: "Spectacled Monkey (Tripura)",
        desc: "Features prominent white ocular fur rings around its eyes and a specialized multi-chambered stomach to ferment and digest tough forest leaves.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="45" r="22" fill="#334155"/>
            <!-- White fur spectacles around eyes -->
            <circle cx="152" cy="42" r="8" fill="#f8fafc"/>
            <circle cx="168" cy="42" r="8" fill="#f8fafc"/>
            <circle cx="152" cy="42" r="4" fill="#0f172a"/>
            <circle cx="168" cy="42" r="4" fill="#0f172a"/>
            <text x="160" y="85" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">White Ocular Fur Rings</text>
        </svg>`
    }
};

function selectUniqueCreature(creature) {
    const data = uniqueCreatures[creature];
    if (!data) return;
    playClickSfx();
    
    ['elephant', 'squirrel', 'monkey'].forEach(k => {
        const btn = document.getElementById(`ucf-btn-${k}`);
        if (!btn) return;
        if (k === creature) {
            btn.className = "p-2.5 rounded-xl border border-purple-500 bg-purple-950/40 text-purple-300 font-bold ring-2 ring-purple-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('ucf-visual-box');
    const iBox = document.getElementById('ucf-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-purple-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 5: Pugmarks & Lookalikes ---
const trackComparators = {
    tiger: {
        title: "Tiger Pugmark (Feline)",
        desc: "Round paw print with four distinct toe pads and NO visible claws. Big cats retract their sharp claws into sheaths while walking.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Main Heel Pad -->
            <path d="M145,55 C135,70 185,70 175,55 C170,48 150,48 145,55 Z" fill="#d97706"/>
            <!-- 4 Rounded Toe Pads -->
            <ellipse cx="138" cy="40" rx="6" ry="8" fill="#d97706"/>
            <ellipse cx="152" cy="32" rx="6" ry="8" fill="#d97706"/>
            <ellipse cx="168" cy="32" rx="6" ry="8" fill="#d97706"/>
            <ellipse cx="182" cy="40" rx="6" ry="8" fill="#d97706"/>
            <text x="160" y="85" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">Retracted Claws (Smooth Print)</text>
        </svg>`
    },
    wolf: {
        title: "Canine Track (Wolf / Jackal)",
        desc: "Oval paw print with four toe pads and sharp, visible claw impressions. Canines have non-retractable claws that provide running traction.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <path d="M148,58 C140,70 180,70 172,58 C168,52 152,52 148,58 Z" fill="#64748b"/>
            <ellipse cx="145" cy="45" rx="5" ry="7" fill="#64748b"/>
            <ellipse cx="155" cy="38" rx="5" ry="7" fill="#64748b"/>
            <ellipse cx="165" cy="38" rx="5" ry="7" fill="#64748b"/>
            <ellipse cx="175" cy="45" rx="5" ry="7" fill="#64748b"/>
            <!-- Sharp Claw marks -->
            <line x1="145" y1="38" x2="145" y2="30" stroke="#0f172a" stroke-width="2"/>
            <line x1="155" y1="31" x2="155" y2="23" stroke="#0f172a" stroke-width="2"/>
            <line x1="165" y1="31" x2="165" y2="23" stroke="#0f172a" stroke-width="2"/>
            <line x1="175" y1="38" x2="175" y2="30" stroke="#0f172a" stroke-width="2"/>
            <text x="160" y="85" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Non-Retractable Claws Visible</text>
        </svg>`
    },
    croc: {
        title: "Crocodile vs Alligator",
        desc: "Crocodiles have narrow, pointed V-shaped snouts with visible lower teeth. Alligators feature broader, rounded U-shaped snouts.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Croc V-snout -->
            <polygon points="60,70 90,20 120,70" fill="#15803d"/>
            <text x="90" y="85" fill="#86efac" font-size="7" font-weight="bold" text-anchor="middle">Crocodile: V-Snout</text>
            <text x="160" y="55" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">vs</text>
            <!-- Alligator U-snout -->
            <path d="M200,70 C200,20 260,20 260,70 Z" fill="#166534"/>
            <text x="230" y="85" fill="#86efac" font-size="7" font-weight="bold" text-anchor="middle">Alligator: U-Snout</text>
        </svg>`
    },
    dove: {
        title: "Pigeon vs Dove",
        desc: "Pigeons are larger with darker iridescent neck plumage. Doves are smaller with delicate pastel grays, whites, and soft cooing calls.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Pigeon -->
            <ellipse cx="90" cy="50" rx="20" ry="14" fill="#475569"/>
            <circle cx="108" cy="42" r="7" fill="#065f46"/>
            <text x="90" y="80" fill="#94a3b8" font-size="7" font-weight="bold" text-anchor="middle">Pigeon: Larger & Darker</text>
            <!-- Dove -->
            <ellipse cx="230" cy="52" rx="16" ry="11" fill="#cbd5e1"/>
            <circle cx="244" cy="46" r="5" fill="#e2e8f0"/>
            <text x="230" y="80" fill="#f8fafc" font-size="7" font-weight="bold" text-anchor="middle">Dove: Petite & Pastel Gray</text>
        </svg>`
    }
};

function selectTrackComparator(comp) {
    const data = trackComparators[comp];
    if (!data) return;
    playClickSfx();
    
    ['tiger', 'wolf', 'croc', 'dove'].forEach(k => {
        const btn = document.getElementById(`pml-btn-${k}`);
        if (!btn) return;
        if (k === comp) {
            btn.className = "p-2.5 rounded-xl border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('pml-visual-box');
    const iBox = document.getElementById('pml-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-orange-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 6: Remarkable Bird Traits ---
const avianFeatures = {
    hornbill: {
        title: "Malabar Pied Hornbill",
        desc: "Features a massive casque atop its curved beak that acts as an acoustic sound resonator. The female seals herself in a tree hole to protect eggs.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="120" cy="45" r="16" fill="#0f172a"/>
            <!-- Curved Beak with Casque -->
            <path d="M135,42 Q175,48 185,60 Q155,58 135,52 Z" fill="#fef08a" stroke="#ca8a04"/>
            <!-- Hollow Casque on top -->
            <path d="M135,35 Q170,30 180,48 Q155,42 135,40 Z" fill="#eab308"/>
            <text x="215" y="52" fill="#fde047" font-size="8" font-weight="bold">Resonating Acoustic Casque</text>
        </svg>`
    },
    peacock: {
        title: "Indian Peacock Ocelli",
        desc: "The peacock displays elongated tail coverts adorned with multi-colored iridescent circular eye-spots (ocelli) to attract peahens during courtship.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Fanned feather display -->
            <circle cx="160" cy="50" r="32" fill="#065f46" opacity="0.6"/>
            <!-- Ocelli (eyespot) -->
            <circle cx="140" cy="38" r="8" fill="#0284c7"/><circle cx="140" cy="38" r="4" fill="#1e1b4b"/>
            <circle cx="160" cy="30" r="8" fill="#0284c7"/><circle cx="160" cy="30" r="4" fill="#1e1b4b"/>
            <circle cx="180" cy="38" r="8" fill="#0284c7"/><circle cx="180" cy="38" r="4" fill="#1e1b4b"/>
            <text x="160" y="90" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Courtship Ocelli Eyespots</text>
        </svg>`
    },
    owl: {
        title: "Barn Owl Night Vision & Sound Disc",
        desc: "Heart-shaped facial discs funnel faint sounds to asymmetric ears, while fringed velvet-edged wing feathers enable completely silent flight.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Heart-shaped facial disc -->
            <circle cx="150" cy="45" r="18" fill="#f8fafc"/>
            <circle cx="170" cy="45" r="18" fill="#f8fafc"/>
            <circle cx="150" cy="45" r="5" fill="#0f172a"/><circle cx="170" cy="45" r="5" fill="#0f172a"/>
            <polygon points="158,50 162,50 160,58" fill="#f59e0b"/>
            <text x="160" y="85" fill="#e2e8f0" font-size="8" font-weight="bold" text-anchor="middle">Acoustic Sound Funnel & Silent Wings</text>
        </svg>`
    }
};

function selectAvianFeature(bird) {
    const data = avianFeatures[bird];
    if (!data) return;
    playClickSfx();
    
    ['hornbill', 'peacock', 'owl'].forEach(k => {
        const btn = document.getElementById(`rbt-btn-${k}`);
        if (!btn) return;
        if (k === bird) {
            btn.className = "p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('rbt-visual-box');
    const iBox = document.getElementById('rbt-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-teal-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 7: Beaks, Claws & Diet Matcher ---
const beakClawData = {
    eagle: {
        title: "Raptor Eagle",
        desc: "Razor-sharp hooked beak tears prey, while muscular curved talons lock onto snakes and rodents with lethal grip force.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Hooked Beak -->
            <path d="M70,35 Q100,35 105,55 Q95,45 80,45 Z" fill="#f59e0b"/>
            <text x="85" y="70" fill="#fbbf24" font-size="7" font-weight="bold" text-anchor="middle">Hooked Beak</text>
            <!-- Curved Talons -->
            <path d="M220,30 Q225,50 215,65 M225,30 Q235,50 230,68 M230,30 Q245,50 245,65" stroke="#f59e0b" stroke-width="3" fill="none"/>
            <text x="230" y="80" fill="#fbbf24" font-size="7" font-weight="bold" text-anchor="middle">Grasping Talons</text>
        </svg>`
    },
    sunbird: {
        title: "Purple Sunbird",
        desc: "Slender down-curved beak acts like a drinking straw, with a long tubular tongue sipping nectar deep inside forest blossoms.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="90" cy="45" r="14" fill="#3b0764"/>
            <!-- Slender curved probe -->
            <path d="M102,42 Q150,48 165,65" fill="none" stroke="#f43f5e" stroke-width="2.5"/>
            <!-- Flower -->
            <circle cx="175" cy="70" r="10" fill="#f43f5e"/>
            <text x="160" y="90" fill="#fda4af" font-size="8" font-weight="bold" text-anchor="middle">Tubular Nectar Straw</text>
        </svg>`
    },
    woodpecker: {
        title: "Woodpecker",
        desc: "Stout chisel-like beak hammers into dead tree trunks for wood-boring grubs. 2+2 zygodactyl climbing toes clamp securely to vertical bark.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Tree trunk -->
            <rect x="170" y="10" width="16" height="80" fill="#78350f"/>
            <!-- Chisel Beak -->
            <polygon points="120,40 170,45 120,50" fill="#64748b"/>
            <!-- Zygodactyl Toes -->
            <text x="110" y="80" fill="#93c5fd" font-size="7" font-weight="bold">Zygodactyl Feet (2+2)</text>
        </svg>`
    },
    duck: {
        title: "Pond Duck",
        desc: "Broad, flat bill lined with comb-like lamellae strainers that filter edible seeds and insect larvae from muddy water.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="120" cy="45" rx="16" ry="12" fill="#15803d"/>
            <!-- Flat Bill with comb-like lamellae -->
            <rect x="135" y="40" width="40" height="12" rx="4" fill="#eab308"/>
            <line x1="140" y1="46" x2="170" y2="46" stroke="#78350f" stroke-width="1.5" stroke-dasharray="3,2"/>
            <text x="160" y="80" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Lamellae Strainer Filter</text>
        </svg>`
    }
};

function selectBeakAndClaw(bird) {
    const data = beakClawData[bird];
    if (!data) return;
    playClickSfx();
    
    ['eagle', 'sunbird', 'woodpecker', 'duck'].forEach(k => {
        const btn = document.getElementById(`bcd-btn-${k}`);
        if (!btn) return;
        if (k === bird) {
            btn.className = "p-2.5 rounded-xl border border-blue-500 bg-blue-950/40 text-blue-300 font-bold ring-2 ring-blue-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('bcd-visual-box');
    const iBox = document.getElementById('bcd-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-blue-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 8: Interactive Bird Diary ---
const diarySightings = {
    flycatcher: {
        title: "Asian Paradise Flycatcher (Dudhraj)",
        desc: "Observed in Mahua canopy at 08:30 AM. Male with long white ribbon tail catching moths mid-air. Melodious territorial song recorded.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="50" y="15" width="220" height="70" rx="4" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
            <text x="65" y="32" fill="#a5b4fc" font-size="8" font-weight="bold">FIELD NOTE: Asian Paradise Flycatcher</text>
            <text x="65" y="46" fill="#cbd5e1" font-size="7">Time: 08:30 AM | Canopy: Mahua Tree | Tail: White Ribbon (30 cm)</text>
            <text x="65" y="58" fill="#4ade80" font-size="7">Behavior: Aerial sallying for moths | Call: Flute-like whistle</text>
            <text x="65" y="72" fill="#fbbf24" font-size="7">Status: State Bird of Madhya Pradesh</text>
        </svg>`
    },
    barbet: {
        title: "Coppersmith Barbet",
        desc: "Observed tapping tree hollow at 10:15 AM. Bright red forehead and yellow throat. Monotonous, metallic 'tuk... tuk... tuk' call like a copper smith.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="50" y="15" width="220" height="70" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
            <text x="65" y="32" fill="#6ee7b7" font-size="8" font-weight="bold">FIELD NOTE: Coppersmith Barbet</text>
            <text x="65" y="46" fill="#cbd5e1" font-size="7">Time: 10:15 AM | Habitat: Dead Fig Trunk | Crest: Crimson Red</text>
            <text x="65" y="58" fill="#4ade80" font-size="7">Behavior: Excavating nest hole | Call: Metallic 'Tuk-Tuk' rhythm</text>
            <text x="65" y="72" fill="#fbbf24" font-size="7">Diet: Wild figs and insect grubs</text>
        </svg>`
    },
    kingfisher: {
        title: "Pied Kingfisher",
        desc: "Observed hovering over river pool at 02:40 PM. Black and white plumage. Hovering motionless before high-speed vertical dive to catch fish.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="50" y="15" width="220" height="70" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="65" y="32" fill="#7dd3fc" font-size="8" font-weight="bold">FIELD NOTE: Pied Kingfisher</text>
            <text x="65" y="46" fill="#cbd5e1" font-size="7">Time: 02:40 PM | Habitat: River Sandbar | Plumage: Pied (B&W)</text>
            <text x="65" y="58" fill="#4ade80" font-size="7">Behavior: Mid-air hovering dive | Beak: Stiletto dagger</text>
            <text x="65" y="72" fill="#fbbf24" font-size="7">Diet: Small river minnows</text>
        </svg>`
    }
};

function selectDiarySighting(sighting) {
    const data = diarySightings[sighting];
    if (!data) return;
    playClickSfx();
    
    ['flycatcher', 'barbet', 'kingfisher'].forEach(k => {
        const btn = document.getElementById(`ibd-btn-${k}`);
        if (!btn) return;
        if (k === sighting) {
            btn.className = "p-2.5 rounded-xl border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('ibd-visual-box');
    const iBox = document.getElementById('ibd-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-indigo-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 9: Aquatic Life Adaptations ---
const aquaticSpecies = {
    fish: {
        title: "River Fish (Streamlined Body)",
        desc: "Tapered streamlined body reduces water resistance, steering fins provide balance, and gills extract dissolved oxygen directly from water currents.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="150" cy="50" rx="35" ry="16" fill="#38bdf8"/>
            <polygon points="115,50 85,35 85,65" fill="#0284c7"/>
            <circle cx="172" cy="46" r="3" fill="#0f172a"/>
            <!-- Gills arc -->
            <path d="M160,40 Q155,50 160,60" fill="none" stroke="#0284c7" stroke-width="2"/>
            <text x="160" y="85" fill="#7dd3fc" font-size="8" font-weight="bold" text-anchor="middle">Streamlined Hydrodynamic Spindle</text>
        </svg>`
    },
    gharial: {
        title: "Gharial (Fish-Hunting Specialist)",
        desc: "Uniquely narrow, elongated snout lined with over 100 needle-sharp interlocking teeth cuts through water with minimal resistance to seize fish.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="80" y="42" width="70" height="18" rx="4" fill="#15803d"/>
            <!-- Narrow long snout -->
            <line x1="150" y1="51" x2="240" y2="51" stroke="#166534" stroke-width="4"/>
            <circle cx="242" cy="51" r="3" fill="#14532d"/>
            <text x="160" y="85" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Slender Low-Drag Snout</text>
        </svg>`
    },
    turtle: {
        title: "Freshwater River Turtle",
        desc: "Hard bony carapace shell fused to ribs protects internal organs. Webbed feet act like swimming flippers and claws dig nesting pits in sand.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="26" ry="18" fill="#78350f" stroke="#ca8a04" stroke-width="2"/>
            <circle cx="192" cy="50" r="7" fill="#16a34a"/>
            <text x="160" y="85" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Protective Bony Carapace Shell</text>
        </svg>`
    },
    frog: {
        title: "Indian Bullfrog (Amphibian Dual Life)",
        desc: "Aquatic tadpoles breathe through gills and swim with tails. Adult frogs develop powerful leaping hind legs and absorb oxygen through moist skin.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="22" ry="16" fill="#16a34a"/>
            <circle cx="174" cy="40" r="5" fill="#eab308"/><circle cx="174" cy="40" r="2" fill="#0f172a"/>
            <path d="M142,55 Q125,75 140,82" stroke="#15803d" stroke-width="4" fill="none"/>
            <text x="160" y="93" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Moist Gas-Exchange Skin & Jumping Legs</text>
        </svg>`
    }
};

function selectAquaticSpecies(species) {
    const data = aquaticSpecies[species];
    if (!data) return;
    playClickSfx();
    
    ['fish', 'gharial', 'turtle', 'frog'].forEach(k => {
        const btn = document.getElementById(`ala-btn-${k}`);
        if (!btn) return;
        if (k === species) {
            btn.className = "p-2.5 rounded-xl border border-sky-500 bg-sky-950/40 text-sky-300 font-bold ring-2 ring-sky-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('ala-visual-box');
    const iBox = document.getElementById('ala-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-sky-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 10: Hexapod Insect Anatomy ---
const insectFeatures = {
    mantis: {
        title: "Praying Mantis",
        desc: "Cryptic green camouflage matches foliage, while spiny raptorial front legs snap forward in milliseconds to snare insect prey.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Body -->
            <line x1="120" y1="65" x2="190" y2="40" stroke="#16a34a" stroke-width="8" stroke-linecap="round"/>
            <circle cx="195" cy="38" r="7" fill="#22c55e"/>
            <!-- Folded raptorial front legs -->
            <path d="M192,42 L205,25 L215,35" stroke="#15803d" stroke-width="3" fill="none"/>
            <text x="160" y="85" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Spiny Raptorial Forelegs</text>
        </svg>`
    },
    beetle: {
        title: "Beetle Elytra (Wing Shields)",
        desc: "Heavily sclerotized armor-like forewings (elytra) protect delicate transparent flying wings and soft abdomen beneath from predators.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="22" ry="26" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
            <line x1="160" y1="24" x2="160" y2="76" stroke="#f59e0b" stroke-width="2"/>
            <text x="160" y="92" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">Hardened Protective Elytra</text>
        </svg>`
    },
    bee: {
        title: "Honeybee Pollen Baskets",
        desc: "Workers collect golden pollen grains in specialized corbiculae (pollen baskets) on their hind legs, pollinating forest trees in return.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Striped abdomen -->
            <ellipse cx="160" cy="50" rx="20" ry="14" fill="#eab308"/>
            <line x1="150" y1="36" x2="150" y2="64" stroke="#0f172a" stroke-width="3"/>
            <line x1="165" y1="36" x2="165" y2="64" stroke="#0f172a" stroke-width="3"/>
            <!-- Pollen Basket -->
            <circle cx="145" cy="62" r="5" fill="#fbbf24"/>
            <text x="160" y="85" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Corbicula Pollen Basket</text>
        </svg>`
    },
    anatomy: {
        title: "Insect Anatomy: 3 Parts & 6 Legs",
        desc: "All insects share 3 distinct body segments (head, thorax, abdomen) and exactly three pairs of jointed walking legs (6 legs).",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Head -->
            <circle cx="110" cy="50" r="12" fill="#0284c7"/>
            <text x="110" y="53" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">HEAD</text>
            <!-- Thorax -->
            <ellipse cx="155" cy="50" rx="18" ry="15" fill="#0ea5e9"/>
            <text x="155" y="53" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">THORAX</text>
            <!-- Abdomen -->
            <ellipse cx="215" cy="50" rx="26" ry="16" fill="#38bdf8"/>
            <text x="215" y="53" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">ABDOMEN</text>
            <!-- 6 legs attached to thorax -->
            <line x1="145" y1="65" x2="135" y2="82" stroke="#0284c7" stroke-width="2"/>
            <line x1="155" y1="65" x2="155" y2="84" stroke="#0284c7" stroke-width="2"/>
            <line x1="165" y1="65" x2="175" y2="82" stroke="#0284c7" stroke-width="2"/>
            <text x="160" y="95" fill="#7dd3fc" font-size="7" font-weight="bold" text-anchor="middle">3 Pairs of Jointed Legs</text>
        </svg>`
    }
};

function selectInsectFeature(feature) {
    const data = insectFeatures[feature];
    if (!data) return;
    playClickSfx();
    
    ['mantis', 'beetle', 'bee', 'anatomy'].forEach(k => {
        const btn = document.getElementById(`hia-btn-${k}`);
        if (!btn) return;
        if (k === feature) {
            btn.className = "p-2.5 rounded-xl border border-lime-500 bg-lime-950/40 text-lime-300 font-bold ring-2 ring-lime-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('hia-visual-box');
    const iBox = document.getElementById('hia-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-lime-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 11: Botanical Leaf Shapes ---
const leafSpecimens = {
    peepal: {
        title: "Peepal Leaf (Heart with Drip-Tip)",
        desc: "Heart-shaped leaf with an elongated, slender drip-tip that sheds heavy monsoon raindrops rapidly to prevent fungal infections.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Peepal outline with long tip -->
            <path d="M160,20 C185,25 200,50 180,68 C165,80 160,92 160,95 C160,92 155,80 140,68 C120,50 135,25 160,20 Z" fill="#22c55e"/>
            <line x1="160" y1="20" x2="160" y2="95" stroke="#15803d" stroke-width="1.5"/>
            <text x="210" y="55" fill="#86efac" font-size="8" font-weight="bold">Elongated Drip-Tip</text>
        </svg>`
    },
    teak: {
        title: "Teak Leaf (Broad & Sandpaper Rough)",
        desc: "Massive oval leaves nearly a meter long, equipped with coarse sandpaper-like surfaces and prominent ridges to resist insect bites.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="45" ry="32" fill="#15803d"/>
            <line x1="160" y1="18" x2="160" y2="82" stroke="#14532d" stroke-width="3"/>
            <line x1="160" y1="35" x2="195" y2="45" stroke="#14532d" stroke-width="2"/>
            <line x1="160" y1="35" x2="125" y2="45" stroke="#14532d" stroke-width="2"/>
            <text x="160" y="94" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Large Rough Surface Blade</text>
        </svg>`
    },
    pine: {
        title: "Pine Needle (Slender with Waxy Cuticle)",
        desc: "Slender needle-like leaves with low surface area and thick waxy coatings that drastically reduce water loss in dry, windy mountain air.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <line x1="130" y1="80" x2="155" y2="20" stroke="#16a34a" stroke-width="3"/>
            <line x1="145" y1="80" x2="160" y2="15" stroke="#15803d" stroke-width="3"/>
            <line x1="160" y1="80" x2="165" y2="20" stroke="#16a34a" stroke-width="3"/>
            <text x="160" y="93" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Slender Evaporation-Resistant Needles</text>
        </svg>`
    },
    lemon: {
        title: "Wild Citrus (Aromatic Essential Oils)",
        desc: "Oval leaves embedded with translucent volatile oil glands that release fresh citrus fragrance when crushed, warding off herbivores.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="30" ry="20" fill="#84cc16"/>
            <!-- Oil gland spots -->
            <circle cx="150" cy="45" r="1.5" fill="#fef08a"/><circle cx="165" cy="48" r="1.5" fill="#fef08a"/><circle cx="155" cy="56" r="1.5" fill="#fef08a"/>
            <text x="160" y="85" fill="#d9f99d" font-size="8" font-weight="bold" text-anchor="middle">Volatile Insect-Deterring Oil Glands</text>
        </svg>`
    }
};

function selectLeafSpecimen(leaf) {
    const data = leafSpecimens[leaf];
    if (!data) return;
    playClickSfx();
    
    ['peepal', 'teak', 'pine', 'lemon'].forEach(k => {
        const btn = document.getElementById(`bls-btn-${k}`);
        if (!btn) return;
        if (k === leaf) {
            btn.className = "p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('bls-visual-box');
    const iBox = document.getElementById('bls-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-emerald-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 12: Leaf Vein Architecture ---
function selectVenationPattern(pattern) {
    const vBox = document.getElementById('lvp-visual-box');
    const iBox = document.getElementById('lvp-info-box');
    playClickSfx();
    
    const btnR = document.getElementById('lvp-btn-reticulate');
    const btnP = document.getElementById('lvp-btn-parallel');
    
    if (pattern === 'reticulate') {
        if (btnR) btnR.className = "p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex items-center justify-center gap-2";
        if (btnP) btnP.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex items-center justify-center gap-2";
        
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <ellipse cx="160" cy="50" rx="35" ry="24" fill="#059669"/>
                    <!-- Midrib -->
                    <line x1="160" y1="26" x2="160" y2="74" stroke="#fef08a" stroke-width="2.5"/>
                    <!-- Branching net-like veins -->
                    <line x1="160" y1="36" x2="185" y2="42" stroke="#fef08a" stroke-width="1.5"/><line x1="160" y1="36" x2="135" y2="42" stroke="#fef08a" stroke-width="1.5"/>
                    <line x1="160" y1="50" x2="190" y2="56" stroke="#fef08a" stroke-width="1.5"/><line x1="160" y1="50" x2="130" y2="56" stroke="#fef08a" stroke-width="1.5"/>
                    <line x1="160" y1="64" x2="182" y2="68" stroke="#fef08a" stroke-width="1.5"/><line x1="160" y1="64" x2="138" y2="68" stroke="#fef08a" stroke-width="1.5"/>
                    <text x="160" y="93" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Reticulate (Net-Like) Dicot Venation</text>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-teal-400">Reticulate Venation (Dicot):</strong> Prominent central midrib with branching lateral veins forming an interconnected mesh. Found in Mango, Peepal, and Banyan.`;
        }
    } else {
        if (btnR) btnR.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex items-center justify-center gap-2";
        if (btnP) btnP.className = "p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex items-center justify-center gap-2";
        
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <rect x="130" y="15" width="60" height="70" rx="8" fill="#15803d"/>
                    <!-- Parallel straight lines -->
                    <line x1="140" y1="15" x2="140" y2="85" stroke="#fef08a" stroke-width="2"/>
                    <line x1="150" y1="15" x2="150" y2="85" stroke="#fef08a" stroke-width="2"/>
                    <line x1="160" y1="15" x2="160" y2="85" stroke="#fef08a" stroke-width="2.5"/>
                    <line x1="170" y1="15" x2="170" y2="85" stroke="#fef08a" stroke-width="2"/>
                    <line x1="180" y1="15" x2="180" y2="85" stroke="#fef08a" stroke-width="2"/>
                    <text x="160" y="95" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Parallel (Straight) Monocot Venation</text>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-teal-400">Parallel Venation (Monocot):</strong> Veins run side by side in straight parallel lines along the length of the blade. Characteristic of Grasses, Bamboo, Maize, and Banana.`;
        }
    }
}

// --- Sim 13: Leaf Crayon Rubbing Studio ---
let crayonStepIndex = 1;
const crayonSteps = [
    {
        num: 1,
        title: "Step 1: Place Leaf Rough Side Up",
        desc: "Select a freshly fallen leaf and place its rough lower surface facing upward. Raised veins create friction for clear impressions.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="110" y="30" width="100" height="40" fill="#334155"/>
            <!-- Leaf rough side up -->
            <ellipse cx="160" cy="50" rx="30" ry="16" fill="#15803d"/>
            <line x1="160" y1="34" x2="160" y2="66" stroke="#ca8a04" stroke-width="3"/>
            <text x="160" y="85" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Vein Ridges Facing Upward</text>
        </svg>`
    },
    {
        num: 2,
        title: "Step 2: Lay Plain Paper Sheet Over Leaf",
        desc: "Place a sheet of plain white paper over the leaf. Keep your fingers completely steady so the paper does not slip or blur.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- White paper covering leaf -->
            <rect x="100" y="20" width="120" height="60" rx="3" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
            <ellipse cx="160" cy="50" rx="30" ry="16" fill="none" stroke="#cbd5e1" stroke-dasharray="4,4"/>
            <text x="160" y="88" fill="#94a3b8" font-size="8" font-weight="bold" text-anchor="middle">Paper Held Steady Over Leaf</text>
        </svg>`
    },
    {
        num: 3,
        title: "Step 3: Rub Wax Crayon Sideways",
        desc: "Hold an unwrapped crayon flat on its broad side. Rub firmly across the paper using even, smooth sideways strokes.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="100" y="20" width="120" height="60" rx="3" fill="#f8fafc"/>
            <!-- Crayon held horizontally -->
            <rect x="135" y="42" width="50" height="12" rx="3" fill="#ea580c"/>
            <line x1="120" y1="58" x2="200" y2="58" stroke="#fdba74" stroke-width="4" stroke-linecap="round"/>
            <text x="160" y="88" fill="#fb923c" font-size="8" font-weight="bold" text-anchor="middle">Firm Sideways Crayon Pressure</text>
        </svg>`
    },
    {
        num: 4,
        title: "Step 4: Botanical Autograph Revealed!",
        desc: "The raised midrib and branching veins appear in vibrant wax relief. Label with the tree species name and venation type for your herbarium!",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="100" y="20" width="120" height="60" rx="3" fill="#f8fafc" stroke="#ea580c" stroke-width="2"/>
            <!-- Completed Rubbing Skeleton -->
            <path d="M160,25 C180,30 190,50 175,65 C160,75 160,78 160,78 C160,78 160,75 145,65 C130,50 140,30 160,25 Z" fill="none" stroke="#c2410c" stroke-width="2"/>
            <line x1="160" y1="25" x2="160" y2="78" stroke="#c2410c" stroke-width="2"/>
            <text x="160" y="93" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Autograph Print Complete!</text>
        </svg>`
    }
];

function renderCrayonStep(idx) {
    const data = crayonSteps[idx - 1];
    if (!data) return;
    const lbl = document.getElementById('lcr-step-label');
    const vBox = document.getElementById('lcr-visual-box');
    const iBox = document.getElementById('lcr-info-box');
    if (lbl) lbl.innerText = data.title;
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-amber-400">${data.title}:</strong> ${data.desc}`;
}

function nextCrayonStep() {
    playClickSfx();
    crayonStepIndex = crayonStepIndex < 4 ? crayonStepIndex + 1 : 1;
    renderCrayonStep(crayonStepIndex);
}

function prevCrayonStep() {
    playClickSfx();
    crayonStepIndex = crayonStepIndex > 1 ? crayonStepIndex - 1 : 4;
    renderCrayonStep(crayonStepIndex);
}

// --- Sim 14: Web Of Life Yarn Game ---
const webNodes = {
    sun: {
        title: "Radiant Solar Energy",
        desc: "Sunlight provides the essential energy for green plants to manufacture food via photosynthesis, sustaining the entire food web.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="50" r="24" fill="#f59e0b"/>
            <line x1="160" y1="15" x2="160" y2="8" stroke="#f59e0b" stroke-width="3"/>
            <line x1="160" y1="85" x2="160" y2="92" stroke="#f59e0b" stroke-width="3"/>
            <text x="160" y="54" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">SOLAR ENGINE</text>
        </svg>`
    },
    plant: {
        title: "Primary Producer (Green Grass & Trees)",
        desc: "Plants convert solar energy and water into energy-rich glucose and oxygen, providing food and shelter for all herbivores.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <line x1="160" y1="85" x2="160" y2="35" stroke="#16a34a" stroke-width="5"/>
            <circle cx="145" cy="40" r="14" fill="#22c55e"/><circle cx="175" cy="40" r="14" fill="#22c55e"/>
            <text x="160" y="94" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Autotrophic Biomass</text>
        </svg>`
    },
    deer: {
        title: "Primary Consumer (Herbivore Deer)",
        desc: "Spotted deer graze on tender leaves and grass, transferring chemical energy from plants upward into the animal kingdom.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="24" ry="16" fill="#d97706"/>
            <circle cx="188" cy="38" r="8" fill="#d97706"/>
            <text x="160" y="85" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Herbivore Energy Link</text>
        </svg>`
    },
    tiger: {
        title: "Apex Predator (Tiger)",
        desc: "Tigers prey upon deer, regulating herbivore populations to prevent destructive overgrazing and maintain healthy forest regeneration.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="50" rx="28" ry="18" fill="#ea580c"/>
            <line x1="150" y1="36" x2="150" y2="64" stroke="#0f172a" stroke-width="3"/>
            <line x1="165" y1="36" x2="165" y2="64" stroke="#0f172a" stroke-width="3"/>
            <text x="160" y="85" fill="#fdba74" font-size="8" font-weight="bold" text-anchor="middle">Top Trophic Regulator</text>
        </svg>`
    },
    fungi: {
        title: "Decomposers (Fungi & Earthworms)",
        desc: "Fungi break down dead leaves, fallen branches, and animal remains, returning vital minerals back into the soil for plants to reuse.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Mushrooms -->
            <rect x="156" y="50" width="8" height="25" fill="#e2e8f0"/>
            <path d="M140,50 C140,25 180,25 180,50 Z" fill="#ef4444"/>
            <circle cx="152" cy="40" r="2.5" fill="#f8fafc"/><circle cx="168" cy="40" r="2.5" fill="#f8fafc"/>
            <text x="160" y="90" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Mineral Nutrient Recycler</text>
        </svg>`
    }
};

function connectWebNode(node) {
    const data = webNodes[node];
    if (!data) return;
    playClickSfx();
    
    ['sun', 'plant', 'deer', 'tiger', 'fungi'].forEach(k => {
        const btn = document.getElementById(`wol-btn-${k}`);
        if (!btn) return;
        if (k === node) {
            btn.className = "p-2 rounded-lg border border-yellow-500 bg-yellow-950/40 text-yellow-300 font-bold ring-2 ring-yellow-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('wol-visual-box');
    const iBox = document.getElementById('wol-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-yellow-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 15: Ecosystem Disruption Lab ---
function triggerDisruption(scenario) {
    const vBox = document.getElementById('edl-visual-box');
    const iBox = document.getElementById('edl-info-box');
    playClickSfx();
    
    const btnB = document.getElementById('edl-btn-balanced');
    const btnD = document.getElementById('edl-btn-deforest');
    const btnT = document.getElementById('edl-btn-notiger');
    
    if (scenario === 'balanced') {
        if (btnB) btnB.className = "p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1";
        if (btnD) btnD.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        if (btnT) btnT.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <rect x="20" y="70" width="280" height="20" fill="#15803d"/>
                    <circle cx="60" cy="45" r="18" fill="#22c55e"/><rect x="57" y="60" width="6" height="15" fill="#78350f"/>
                    <circle cx="160" cy="50" r="14" fill="#d97706"/>
                    <circle cx="260" cy="48" r="16" fill="#ea580c"/>
                    <text x="160" y="85" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">✓ Trophic Harmony: Canopy ⇄ Herbivores ⇄ Apex Predators</text>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-emerald-400">Balanced Ecosystem:</strong> Intact canopies nourish herbivores, predators regulate grazing numbers, and decomposers recycle soil nutrients smoothly.`;
        }
    } else if (scenario === 'deforest') {
        if (btnB) btnB.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        if (btnD) btnD.className = "p-2.5 rounded-xl border border-rose-500 bg-rose-950/40 text-rose-300 font-bold ring-2 ring-rose-500 transition-all flex flex-col items-center gap-1";
        if (btnT) btnT.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        
        playErrorSfx();
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <rect x="20" y="70" width="280" height="20" fill="#78350f"/>
                    <!-- Cut Tree Stump -->
                    <rect x="55" y="65" width="16" height="10" fill="#451a03"/>
                    <text x="160" y="45" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">⚠️ HABITAT COLLAPSE</text>
                    <text x="160" y="62" fill="#fca5a5" font-size="7" text-anchor="middle">No leaves for herbivores • Severe topsoil erosion into rivers</text>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-rose-400">Trees Destroyed:</strong> Caterpillars lose food, songbirds starve, monsoon rains wash topsoil into rivers, suffocating fish populations!`;
        }
    } else {
        if (btnB) btnB.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        if (btnD) btnD.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        if (btnT) btnT.className = "p-2.5 rounded-xl border border-amber-500 bg-amber-950/40 text-amber-300 font-bold ring-2 ring-amber-500 transition-all flex flex-col items-center gap-1";
        
        playErrorSfx();
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <rect x="20" y="70" width="280" height="20" fill="#ca8a04"/>
                    <!-- Swarm of Deer -->
                    <circle cx="80" cy="55" r="10" fill="#d97706"/><circle cx="130" cy="55" r="10" fill="#d97706"/><circle cx="180" cy="55" r="10" fill="#d97706"/><circle cx="230" cy="55" r="10" fill="#d97706"/>
                    <text x="160" y="32" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">HERBIVORE OVERGRAZING</text>
                    <text x="160" y="85" fill="#fef08a" font-size="7" text-anchor="middle">All young tree saplings eaten • Forest fails to regenerate</text>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-amber-400">Predator Removed:</strong> Deer herds multiply unchecked, eating every young sapling and grass blade until the forest floor becomes a barren dust bowl.`;
        }
    }
}

// --- Sim 16: State Nature Symbols ---
const stateSymbols = {
    animal: {
        title: "State Animal - Barasingha (Swamp Deer)",
        desc: "The swamp deer of Madhya Pradesh features twelve-tined antlers. Successfully conserved in Kanha and Satpura national parks.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="150" cy="55" rx="26" ry="16" fill="#d97706"/>
            <circle cx="182" cy="42" r="10" fill="#b45309"/>
            <!-- 12-tined Antlers -->
            <path d="M185,35 L195,15 M188,26 L198,24 M190,20 L200,16 M182,35 L175,15 M180,26 L170,24" stroke="#78350f" stroke-width="2.5"/>
            <text x="160" y="90" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">12-Tined Antlered Swamp Deer</text>
        </svg>`
    },
    bird: {
        title: "State Bird - Asian Paradise Flycatcher (Dudhraj)",
        desc: "Adult males sport brilliant white plumage, crested black heads, and two elongated 30 cm ribbon-like tail feathers that stream gracefully in flight.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="120" cy="42" r="10" fill="#0f172a"/>
            <ellipse cx="140" cy="48" rx="18" ry="10" fill="#f8fafc"/>
            <!-- Streaming white ribbon tail -->
            <path d="M158,50 Q210,65 260,50" stroke="#f8fafc" stroke-width="3" fill="none"/>
            <path d="M158,52 Q210,75 260,65" stroke="#f8fafc" stroke-width="2" fill="none"/>
            <text x="160" y="90" fill="#c7d2fe" font-size="8" font-weight="bold" text-anchor="middle">Streaming Ribbon Tail Feathers</text>
        </svg>`
    },
    tree: {
        title: "State Tree - Sacred Banyan (Ficus benghalensis)",
        desc: "Expansive canopy supported by descending aerial prop roots, providing sheltering shade and sacred community council grounds.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="155" y="45" width="14" height="40" fill="#78350f"/>
            <!-- Aerial roots -->
            <line x1="125" y1="45" x2="125" y2="85" stroke="#92400e" stroke-width="2.5"/>
            <line x1="195" y1="45" x2="195" y2="85" stroke="#92400e" stroke-width="2.5"/>
            <ellipse cx="162" cy="35" rx="55" ry="24" fill="#15803d"/>
            <text x="160" y="94" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Wide Canopy & Aerial Prop Roots</text>
        </svg>`
    },
    origami: {
        title: "Origami Turtle Craft Studio",
        desc: "Fold a square paper sheet into a freshwater river turtle! Decorate the shell with geometric scutes and write your personal nature conservation pledge.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <!-- Origami Turtle Outline -->
            <polygon points="160,25 185,45 185,75 160,90 135,75 135,45" fill="#16a34a" stroke="#fef08a" stroke-width="2"/>
            <polygon points="135,45 115,35 125,55" fill="#15803d"/>
            <polygon points="185,45 205,35 195,55" fill="#15803d"/>
            <circle cx="160" cy="20" r="5" fill="#22c55e"/>
            <text x="160" y="60" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">PLEDGE: SAVE WILDLIFE</text>
        </svg>`
    }
};

function selectStateSymbol(symbol) {
    const data = stateSymbols[symbol];
    if (!data) return;
    playClickSfx();
    
    ['animal', 'bird', 'tree', 'origami'].forEach(k => {
        const btn = document.getElementById(`sns-btn-${k}`);
        if (!btn) return;
        if (k === symbol) {
            btn.className = "p-2.5 rounded-xl border border-violet-500 bg-violet-950/40 text-violet-300 font-bold ring-2 ring-violet-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('sns-visual-box');
    const iBox = document.getElementById('sns-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-violet-400">${data.title}:</strong> ${data.desc}`;
}

// ============================================================================
// Simulator Initialization Dispatcher
// ============================================================================
function initSimulatorForSlide(slideNum) {
    if (slideNum === 1) selectPachmarhiSpot('cliffs');
    if (slideNum === 2) selectForestRule('silence');
    if (slideNum === 3) selectAnimalStratum('terrestrial');
    if (slideNum === 4) selectUniqueCreature('elephant');
    if (slideNum === 5) selectTrackComparator('tiger');
    if (slideNum === 6) selectAvianFeature('hornbill');
    if (slideNum === 7) selectBeakAndClaw('eagle');
    if (slideNum === 8) selectDiarySighting('flycatcher');
    if (slideNum === 9) selectAquaticSpecies('fish');
    if (slideNum === 10) selectInsectFeature('mantis');
    if (slideNum === 11) selectLeafSpecimen('peepal');
    if (slideNum === 12) selectVenationPattern('reticulate');
    if (slideNum === 13) renderCrayonStep(1);
    if (slideNum === 14) connectWebNode('sun');
    if (slideNum === 15) triggerDisruption('balanced');
    if (slideNum === 16) selectStateSymbol('animal');
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            // Voices pre-loaded
        };
    }
});
'''

# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 2: Exploring Our Neighbourhood
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

// --- Sim 1: Neighbourhood Route Explorer ---
const routeWaypoints = {
    school: {
        title: "School Gate",
        desc: "Students begin their homeward walk safely on marked pedestrian footpaths, staying attentive to surrounding road traffic and bicycle bells.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="10" y="20" width="80" height="60" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
            <polygon points="50,5 15,20 85,20" fill="#3b82f6"/>
            <text x="50" y="48" fill="#93c5fd" font-size="9" font-weight="bold" text-anchor="middle">SCHOOL</text>
            <rect x="42" y="55" width="16" height="25" fill="#0f172a"/>
            <rect x="90" y="60" width="220" height="25" fill="#334155"/>
            <line x1="90" y1="72" x2="310" y2="72" stroke="#64748b" stroke-width="2" stroke-dasharray="8,6"/>
            <circle cx="120" cy="55" r="7" fill="#fbbf24"/>
            <line x1="120" y1="62" x2="120" y2="75" stroke="#fbbf24" stroke-width="3"/>
            <text x="120" y="92" fill="#94a3b8" font-size="8" text-anchor="middle">Student Walking</text>
        </svg>`
    },
    market: {
        title: "Produce Market",
        desc: "Local vegetable and fruit vendors arrange colorful carts along the street, supplying fresh food to neighbourhood families.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="10" y="50" width="300" height="35" fill="#334155"/>
            <polygon points="40,25 90,25 95,40 35,40" fill="#f97316"/>
            <rect x="40" y="40" width="50" height="30" fill="#7c2d12"/>
            <circle cx="50" cy="50" r="4" fill="#ef4444"/><circle cx="65" cy="50" r="4" fill="#84cc16"/><circle cx="80" cy="50" r="4" fill="#eab308"/>
            <text x="65" y="80" fill="#fdba74" font-size="8" font-weight="bold" text-anchor="middle">Fruit & Veggie Cart</text>
            <polygon points="130,25 180,25 185,40 125,40" fill="#10b981"/>
            <rect x="130" y="40" width="50" height="30" fill="#064e3b"/>
            <text x="155" y="80" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Bakery & Grains</text>
        </svg>`
    },
    crossing: {
        title: "Zebra Crossing",
        desc: "Marked white stripes on the road indicate safe pedestrian crossing points. Always look left and right before stepping forward.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="10" y="25" width="300" height="55" fill="#1e293b"/>
            <rect x="110" y="30" width="12" height="45" fill="#f8fafc"/>
            <rect x="130" y="30" width="12" height="45" fill="#f8fafc"/>
            <rect x="150" y="30" width="12" height="45" fill="#f8fafc"/>
            <rect x="170" y="30" width="12" height="45" fill="#f8fafc"/>
            <rect x="190" y="30" width="12" height="45" fill="#f8fafc"/>
            <rect x="250" y="10" width="14" height="40" rx="3" fill="#0f172a" stroke="#475569"/>
            <circle cx="257" cy="18" r="4" fill="#ef4444"/>
            <circle cx="257" cy="30" r="4" fill="#334155"/>
            <circle cx="257" cy="42" r="4" fill="#22c55e"/>
            <text x="257" y="60" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">WALK</text>
        </svg>`
    },
    busstop: {
        title: "Bus Stop",
        desc: "A sheltered commuter waiting point with route schedules and benches, connecting neighbours across the entire city.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <line x1="40" y1="20" x2="110" y2="20" stroke="#0284c7" stroke-width="5"/>
            <line x1="45" y1="20" x2="45" y2="80" stroke="#64748b" stroke-width="3"/>
            <line x1="105" y1="20" x2="105" y2="80" stroke="#64748b" stroke-width="3"/>
            <rect x="50" y="55" width="50" height="8" rx="2" fill="#0369a1"/>
            <text x="75" y="35" fill="#7dd3fc" font-size="7" font-weight="bold" text-anchor="middle">BUS STOP</text>
            <rect x="150" y="30" width="110" height="45" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <rect x="160" y="38" width="20" height="15" rx="2" fill="#bae6fd"/>
            <rect x="190" y="38" width="20" height="15" rx="2" fill="#bae6fd"/>
            <rect x="220" y="38" width="20" height="15" rx="2" fill="#bae6fd"/>
            <circle cx="175" cy="75" r="7" fill="#0f172a"/><circle cx="235" cy="75" r="7" fill="#0f172a"/>
        </svg>`
    }
};

function selectRouteWaypoint(wp) {
    const data = routeWaypoints[wp];
    if (!data) return;
    playClickSfx();
    
    ['school', 'market', 'crossing', 'busstop'].forEach(k => {
        const btn = document.getElementById(`nre-btn-${k}`);
        if (!btn) return;
        if (k === wp) {
            btn.className = "p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('nre-visual-box');
    const iBox = document.getElementById('nre-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-emerald-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 2: Communication Timeline ---
const commEras = {
    ancient: {
        title: "Drums & Smoke Signals",
        desc: "Ancient acoustic drumbeats and high smoke plumes transmitted alerts across hills and valleys before electrical wires were invented.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <polygon points="40,80 70,30 100,80" fill="#475569"/>
            <circle cx="70" cy="22" r="5" fill="#94a3b8" opacity="0.8"/>
            <circle cx="75" cy="14" r="7" fill="#cbd5e1" opacity="0.6"/>
            <circle cx="80" cy="6" r="9" fill="#e2e8f0" opacity="0.4"/>
            <ellipse cx="200" cy="50" rx="20" ry="8" fill="#78350f" stroke="#d97706" stroke-width="2"/>
            <rect x="180" y="50" width="40" height="25" fill="#92400e"/>
            <ellipse cx="200" cy="75" rx="20" ry="8" fill="#78350f"/>
            <line x1="170" y1="40" x2="190" y2="48" stroke="#d97706" stroke-width="2"/>
            <text x="200" y="93" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle">Acoustic Drum Wave</text>
        </svg>`
    },
    pigeon: {
        title: "Homing Pigeon Messenger",
        desc: "Trained homing pigeons used natural geomagnetic navigation to carry lightweight rolled scrolls tied securely to their legs.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <path d="M120,50 Q140,25 170,45 Q200,25 220,50 Q180,60 160,55 Z" fill="#94a3b8"/>
            <circle cx="125" cy="48" r="4" fill="#cbd5e1"/>
            <polygon points="115,48 122,46 122,50" fill="#f59e0b"/>
            <rect x="158" y="57" width="12" height="6" rx="2" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>
            <text x="164" y="75" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Parchment Scroll</text>
        </svg>`
    },
    postal: {
        title: "Postal Letters & Red Postboxes",
        desc: "Organized postal networks allowed citizens to write letters, affix postage stamps, and send mail worldwide via sorting offices.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="60" y="30" width="30" height="50" rx="8" fill="#dc2626" stroke="#991b1b" stroke-width="2"/>
            <rect x="65" y="40" width="20" height="4" fill="#0f172a"/>
            <text x="75" y="65" fill="#ffffff" font-size="6" font-weight="bold" text-anchor="middle">MAIL</text>
            <rect x="150" y="35" width="70" height="45" rx="3" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
            <polygon points="150,35 185,58 220,35" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
            <rect x="202" y="38" width="12" height="14" fill="#f43f5e" stroke="#881337" stroke-width="1"/>
            <text x="185" y="72" fill="#475569" font-size="6" text-anchor="middle">PIN: 110001</text>
        </svg>`
    },
    telecom: {
        title: "Landline Telephone",
        desc: "Landline telephones transmitted analog voice signals along metal wires, enabling real-time spoken conversations across thousands of kilometers.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="120" y="45" width="80" height="35" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <circle cx="160" cy="62" r="14" fill="#334155"/>
            <circle cx="160" cy="62" r="6" fill="#f8fafc"/>
            <path d="M105,35 Q160,20 215,35" stroke="#0f172a" stroke-width="10" stroke-linecap="round"/>
            <circle cx="108" cy="35" r="8" fill="#334155"/>
            <circle cx="212" cy="35" r="8" fill="#334155"/>
            <text x="160" y="92" fill="#94a3b8" font-size="8" text-anchor="middle">Copper Cable Audio</text>
        </svg>`
    },
    digital: {
        title: "Digital Satellites & Smartphones",
        desc: "Modern digital telecommunications use space satellites and wireless fiber networks to stream voice, video, and text instantly across the globe.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="50" y="15" width="20" height="15" fill="#38bdf8"/>
            <line x1="30" y1="22" x2="50" y2="22" stroke="#e0f2fe" stroke-width="3"/>
            <line x1="70" y1="22" x2="90" y2="22" stroke="#e0f2fe" stroke-width="3"/>
            <path d="M75,35 Q120,40 180,50" stroke="#38bdf8" stroke-dasharray="3,3" fill="none"/>
            <rect x="190" y="25" width="35" height="60" rx="5" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
            <rect x="193" y="30" width="29" height="48" fill="#164e63"/>
            <circle cx="207.5" cy="81" r="2" fill="#06b6d4"/>
            <text x="240" y="55" fill="#67e8f9" font-size="8" font-weight="bold">Instant Video & Chat</text>
        </svg>`
    }
};

function selectCommEra(era) {
    const data = commEras[era];
    if (!data) return;
    playClickSfx();
    
    ['ancient', 'pigeon', 'postal', 'telecom', 'digital'].forEach(k => {
        const btn = document.getElementById(`ctl-btn-${k}`);
        if (!btn) return;
        if (k === era) {
            btn.className = "p-2 rounded-lg border border-cyan-500 bg-cyan-950/40 text-cyan-300 font-bold ring-2 ring-cyan-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('ctl-visual-box');
    const iBox = document.getElementById('ctl-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-cyan-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 3: Postal Mail Journey ---
let postalStepIndex = 1;
const postalSteps = [
    {
        num: 1,
        title: "Step 1: Posting in Letterbox",
        desc: "The sender addresses an envelope with a six-digit PIN code, affixes a postage stamp, and drops it into the neighborhood red letterbox.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="130" y="25" width="36" height="60" rx="8" fill="#dc2626" stroke="#991b1b" stroke-width="2"/>
            <rect x="136" y="36" width="24" height="4" fill="#0f172a"/>
            <rect x="140" y="20" width="16" height="12" fill="#f8fafc" stroke="#94a3b8"/>
            <text x="148" y="93" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Street Postbox</text>
        </svg>`
    },
    {
        num: 2,
        title: "Step 2: Mail Van Collection",
        desc: "At scheduled clearance hours, a postal carrier empties the letterbox into a mail sack and transports it to the central sorting hub.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="90" y="30" width="120" height="45" rx="6" fill="#dc2626" stroke="#991b1b" stroke-width="2"/>
            <polygon points="210,45 230,55 230,75 210,75" fill="#dc2626"/>
            <rect x="110" y="40" width="30" height="20" fill="#991b1b"/>
            <text x="125" y="53" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">INDIA POST</text>
            <circle cx="120" cy="75" r="8" fill="#0f172a"/><circle cx="195" cy="75" r="8" fill="#0f172a"/>
        </svg>`
    },
    {
        num: 3,
        title: "Step 3: Central Sorting Hub",
        desc: "At the sorting center, postal workers date-stamp each envelope and categorize mail using the six-digit Postal Index Number (PIN code).",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="60" y="20" width="200" height="60" fill="#1e293b" stroke="#475569"/>
            <line x1="110" y1="20" x2="110" y2="80" stroke="#475569"/>
            <line x1="160" y1="20" x2="160" y2="80" stroke="#475569"/>
            <line x1="210" y1="20" x2="210" y2="80" stroke="#475569"/>
            <line x1="60" y1="50" x2="260" y2="50" stroke="#475569"/>
            <text x="85" y="40" fill="#f87171" font-size="7" text-anchor="middle">Zone 1</text>
            <text x="135" y="40" fill="#f87171" font-size="7" text-anchor="middle">Zone 2</text>
            <text x="185" y="40" fill="#f87171" font-size="7" text-anchor="middle">Zone 3</text>
            <text x="235" y="40" fill="#f87171" font-size="7" text-anchor="middle">Zone 4</text>
        </svg>`
    },
    {
        num: 4,
        title: "Step 4: Intercity Mail Transit",
        desc: "Sorted sacks travel on dedicated mail trains, long-distance postal buses, or air cargo carriers to destination cities.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="70" y="35" width="80" height="40" rx="4" fill="#b91c1c"/>
            <rect x="155" y="40" width="85" height="35" rx="3" fill="#991b1b"/>
            <text x="195" y="60" fill="#fecaca" font-size="7" font-weight="bold" text-anchor="middle">MAIL EXPRESS</text>
            <line x1="30" y1="78" x2="290" y2="78" stroke="#64748b" stroke-width="4"/>
            <circle cx="90" cy="75" r="7" fill="#0f172a"/><circle cx="130" cy="75" r="7" fill="#0f172a"/>
            <circle cx="175" cy="75" r="7" fill="#0f172a"/><circle cx="220" cy="75" r="7" fill="#0f172a"/>
        </svg>`
    },
    {
        num: 5,
        title: "Step 5: Doorstep Delivery",
        desc: "The local mail carrier organizes letters by street order and delivers envelopes directly to home mailboxes and residents.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="50" y="30" width="70" height="50" fill="#1e293b" stroke="#64748b"/>
            <polygon points="50,30 85,15 120,30" fill="#f43f5e"/>
            <circle cx="180" cy="35" r="7" fill="#fca5a5"/>
            <line x1="180" y1="42" x2="180" y2="65" stroke="#fca5a5" stroke-width="3"/>
            <rect x="185" y="48" width="12" height="15" rx="2" fill="#78350f"/>
            <line x1="180" y1="65" x2="175" y2="82" stroke="#fca5a5" stroke-width="2"/>
            <line x1="180" y1="65" x2="185" y2="82" stroke="#fca5a5" stroke-width="2"/>
            <text x="180" y="93" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Delivered Successfully!</text>
        </svg>`
    }
];

function renderPostalStep(idx) {
    const data = postalSteps[idx - 1];
    if (!data) return;
    const lbl = document.getElementById('pmj-step-label');
    const vBox = document.getElementById('pmj-visual-box');
    const iBox = document.getElementById('pmj-info-box');
    if (lbl) lbl.innerText = data.title;
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-rose-400">${data.title}:</strong> ${data.desc}`;
}

function nextPostalStep() {
    playClickSfx();
    postalStepIndex = postalStepIndex < 5 ? postalStepIndex + 1 : 1;
    renderPostalStep(postalStepIndex);
}

function prevPostalStep() {
    playClickSfx();
    postalStepIndex = postalStepIndex > 1 ? postalStepIndex - 1 : 5;
    renderPostalStep(postalStepIndex);
}

// --- Sim 4: Modern Urban Transit ---
const transitModes = {
    ground: {
        title: "Surface Road Traffic",
        desc: "Ground-level intersections experience long queues at red signals, vehicle idling, slower travel times, and concentrated exhaust fumes.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="10" y="55" width="300" height="35" fill="#334155"/>
            <rect x="40" y="62" width="40" height="18" rx="3" fill="#ef4444"/>
            <circle cx="50" cy="80" r="4" fill="#0f172a"/><circle cx="70" cy="80" r="4" fill="#0f172a"/>
            <rect x="95" y="62" width="40" height="18" rx="3" fill="#f59e0b"/>
            <circle cx="105" cy="80" r="4" fill="#0f172a"/><circle cx="125" cy="80" r="4" fill="#0f172a"/>
            <rect x="180" y="30" width="10" height="35" fill="#0f172a"/>
            <circle cx="185" cy="38" r="4" fill="#ef4444"/>
            <text x="235" y="50" fill="#f87171" font-size="8" font-weight="bold">Heavy Traffic Jam</text>
        </svg>`
    },
    flyover: {
        title: "Elevated Flyover",
        desc: "Soars above busy road crossroads, allowing vehicles to bypass ground signals without stopping, saving fuel and eliminating traffic bottlenecks.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="10" y="65" width="300" height="25" fill="#1e293b"/>
            <rect x="80" y="35" width="12" height="35" fill="#64748b"/>
            <rect x="220" y="35" width="12" height="35" fill="#64748b"/>
            <rect x="10" y="25" width="300" height="14" rx="2" fill="#3b82f6"/>
            <rect x="130" y="15" width="40" height="12" rx="3" fill="#93c5fd"/>
            <circle cx="140" cy="27" r="3" fill="#1e3a8a"/><circle cx="160" cy="27" r="3" fill="#1e3a8a"/>
            <text x="160" y="55" fill="#60a5fa" font-size="8" font-weight="bold" text-anchor="middle">Smooth Overhead Bypass</text>
        </svg>`
    },
    metro: {
        title: "Electric Metro Rail",
        desc: "Carries hundreds of commuters simultaneously on dedicated elevated tracks with zero tailpipe emissions, making city travel clean, punctual, and rapid.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="70" y="40" width="16" height="40" fill="#475569"/>
            <rect x="230" y="40" width="16" height="40" fill="#475569"/>
            <line x1="10" y1="40" x2="310" y2="40" stroke="#0ea5e9" stroke-width="4"/>
            <rect x="85" y="20" width="150" height="22" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <rect x="95" y="24" width="20" height="12" rx="2" fill="#e0f2fe"/>
            <rect x="125" y="24" width="20" height="12" rx="2" fill="#e0f2fe"/>
            <rect x="155" y="24" width="20" height="12" rx="2" fill="#e0f2fe"/>
            <rect x="185" y="24" width="20" height="12" rx="2" fill="#e0f2fe"/>
            <text x="160" y="75" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Zero Emission Transit (400+ Pass.)</text>
        </svg>`
    }
};

function selectTransitMode(mode) {
    const data = transitModes[mode];
    if (!data) return;
    playClickSfx();
    
    ['ground', 'flyover', 'metro'].forEach(k => {
        const btn = document.getElementById(`mut-btn-${k}`);
        if (!btn) return;
        if (k === mode) {
            btn.className = "p-2.5 rounded-xl border border-blue-500 bg-blue-950/40 text-blue-300 font-bold ring-2 ring-blue-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('mut-visual-box');
    const iBox = document.getElementById('mut-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-blue-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 5: Green Infrastructure Balancer ---
let ecoTreeCount = 4;
function updateEcoDisplay() {
    const tCountEl = document.getElementById('gib-tree-count');
    const scoreEl = document.getElementById('gib-eco-score');
    const vBox = document.getElementById('gib-visual-box');
    const iBox = document.getElementById('gib-info-box');
    
    const pct = Math.min(100, ecoTreeCount * 20);
    if (tCountEl) tCountEl.innerText = ecoTreeCount;
    if (scoreEl) scoreEl.innerText = `${pct}%`;
    
    let treesSvg = '';
    const spacing = 280 / (ecoTreeCount + 1);
    for (let i = 1; i <= ecoTreeCount; i++) {
        const cx = 20 + i * spacing;
        treesSvg += `
            <rect x="${cx - 2}" y="55" width="4" height="25" fill="#78350f"/>
            <circle cx="${cx}" cy="45" r="14" fill="#22c55e" opacity="0.9"/>
            <circle cx="${cx - 6}" cy="48" r="10" fill="#16a34a"/>
            <circle cx="${cx + 6}" cy="48" r="10" fill="#15803d"/>
        `;
    }
    
    if (vBox) {
        vBox.innerHTML = `
            <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                <rect x="10" y="75" width="300" height="20" fill="#334155"/>
                <rect x="10" y="70" width="300" height="6" fill="#0284c7" stroke="#38bdf8" stroke-width="0.5"/>
                ${treesSvg}
            </svg>
        `;
    }
    if (iBox) {
        if (pct >= 100) {
            iBox.innerHTML = `<strong class="text-emerald-400">Optimal Eco-Balance Achieved!</strong> ${ecoTreeCount} native trees planted along avenues provide abundant shade, absorb vehicle exhaust, and house singing songbirds.`;
        } else {
            iBox.innerHTML = `<strong class="text-lime-400">Compensatory Planting:</strong> When road widening trims mature trees, planting multiple native avenue trees (Neem, Peepal, Banyan) restores wildlife habitat and purifies air.`;
        }
    }
}

function addSapling() {
    if (ecoTreeCount < 6) {
        playSuccessSfx();
        ecoTreeCount++;
        updateEcoDisplay();
    }
}

function resetEcoBalance() {
    playClickSfx();
    ecoTreeCount = 2;
    updateEcoDisplay();
}

// --- Sim 6: Community Health Clinic ---
const clinicSections = {
    eye: {
        title: "Community Eye Check-up Camp",
        desc: "Specialists test visual acuity with Snellen charts, check intraocular pressure, and provide free corrective spectacles for schoolchildren and elders.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="60" y="15" width="55" height="70" rx="3" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
            <text x="87.5" y="32" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">E</text>
            <text x="87.5" y="46" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">F P</text>
            <text x="87.5" y="58" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">T O Z</text>
            <text x="87.5" y="68" fill="#0f172a" font-size="5" font-weight="bold" text-anchor="middle">L P E D</text>
            <circle cx="180" cy="50" r="16" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <circle cx="225" cy="50" r="16" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <line x1="196" y1="50" x2="209" y2="50" stroke="#38bdf8" stroke-width="3"/>
            <text x="202.5" y="85" fill="#7dd3fc" font-size="8" font-weight="bold" text-anchor="middle">Corrective Spectacles</text>
        </svg>`
    },
    vaccine: {
        title: "Immunization Station",
        desc: "Routine vaccinations protect infants and growing children from dangerous infectious diseases including polio, measles, and hepatitis.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="90" y="30" width="25" height="45" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
            <rect x="94" y="24" width="17" height="6" fill="#64748b"/>
            <rect x="92" y="42" width="21" height="16" fill="#0284c7"/>
            <text x="102" y="53" fill="#ffffff" font-size="5" font-weight="bold" text-anchor="middle">POLIO</text>
            <line x1="160" y1="55" x2="220" y2="55" stroke="#cbd5e1" stroke-width="8"/>
            <line x1="220" y1="55" x2="240" y2="55" stroke="#94a3b8" stroke-width="2"/>
            <text x="160" y="85" fill="#2dd4bf" font-size="8" font-weight="bold" text-anchor="middle">Safe Childhood Protection</text>
        </svg>`
    },
    opd: {
        title: "Doctor OPD Clinic",
        desc: "Physicians conduct clinical examinations, listen to heartbeats through stethoscopes, and prescribe medicines for recovery.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <path d="M120,25 C120,60 160,60 160,25" fill="none" stroke="#38bdf8" stroke-width="4"/>
            <circle cx="120" cy="25" r="4" fill="#64748b"/><circle cx="160" cy="25" r="4" fill="#64748b"/>
            <line x1="140" y1="46" x2="140" y2="70" stroke="#38bdf8" stroke-width="3"/>
            <circle cx="140" cy="74" r="8" fill="#64748b" stroke="#38bdf8" stroke-width="2"/>
            <text x="215" y="52" fill="#7dd3fc" font-size="8" font-weight="bold">Clinical Diagnosis</text>
        </svg>`
    },
    pharma: {
        title: "Dispensary Pharmacy",
        desc: "Pharmacists dispense correct medications, verifying doctor prescriptions and explaining dosage instructions carefully to patients.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="90" y="30" width="30" height="45" rx="4" fill="#a7f3d0" stroke="#059669" stroke-width="2"/>
            <rect x="98" y="24" width="14" height="6" fill="#047857"/>
            <rect x="150" y="30" width="55" height="40" rx="3" fill="#f8fafc" stroke="#94a3b8"/>
            <circle cx="162" cy="40" r="5" fill="#f59e0b"/><circle cx="177" cy="40" r="5" fill="#f59e0b"/><circle cx="192" cy="40" r="5" fill="#f59e0b"/>
            <circle cx="162" cy="58" r="5" fill="#ef4444"/><circle cx="177" cy="58" r="5" fill="#ef4444"/><circle cx="192" cy="58" r="5" fill="#ef4444"/>
            <text x="145" y="85" fill="#34d399" font-size="8" font-weight="bold" text-anchor="middle">Prescription Dispensed</text>
        </svg>`
    }
};

function selectClinicSection(sec) {
    const data = clinicSections[sec];
    if (!data) return;
    playClickSfx();
    
    ['eye', 'vaccine', 'opd', 'pharma'].forEach(k => {
        const btn = document.getElementById(`chc-btn-${k}`);
        if (!btn) return;
        if (k === sec) {
            btn.className = "p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('chc-visual-box');
    const iBox = document.getElementById('chc-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-teal-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 7: Medical Roles Explorer ---
const medicalRoles = {
    doc: {
        title: "Physician / Doctor",
        desc: "Listens to chest and heart sounds using a stethoscope, identifies the illness through careful clinical diagnosis, and prescribes treatment.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="35" r="14" fill="#fed7aa"/>
            <path d="M135,80 C135,55 185,55 185,80" fill="#f8fafc"/>
            <path d="M148,45 C148,65 172,65 172,45" fill="none" stroke="#0284c7" stroke-width="3"/>
            <circle cx="160" cy="68" r="4" fill="#64748b"/>
            <text x="160" y="94" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Doctor Diagnosing</text>
        </svg>`
    },
    nurse: {
        title: "Staff Nurse",
        desc: "Provides continuous compassionate bedside care, dresses wounds, administers prescribed injections, and monitors recovery vitals.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="35" r="14" fill="#fed7aa"/>
            <polygon points="150,22 170,22 165,15 155,15" fill="#f8fafc"/>
            <rect x="158" y="16" width="4" height="4" fill="#ef4444"/>
            <path d="M135,80 C135,55 185,55 185,80" fill="#e0f2fe"/>
            <text x="160" y="94" fill="#7dd3fc" font-size="8" font-weight="bold" text-anchor="middle">Nurse Monitoring Vitals</text>
        </svg>`
    },
    lab: {
        title: "Laboratory Technician",
        desc: "Examines blood and body fluid specimens under high-magnification optical microscopes to identify bacteria, parasites, and cell counts.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="135" y="70" width="50" height="8" rx="2" fill="#475569"/>
            <line x1="160" y1="70" x2="160" y2="35" stroke="#64748b" stroke-width="6"/>
            <line x1="160" y1="35" x2="140" y2="25" stroke="#94a3b8" stroke-width="5"/>
            <rect x="145" y="55" width="30" height="4" fill="#f8fafc"/>
            <text x="160" y="92" fill="#c7d2fe" font-size="8" font-weight="bold" text-anchor="middle">Microscopic Diagnostic Analysis</text>
        </svg>`
    },
    pharm: {
        title: "Hospital Pharmacist",
        desc: "Ensures accurate medicine dispensing, verifies dosages against medical guidelines, and instructs patients on dosage schedules.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="160" cy="65" rx="22" ry="12" fill="#334155" stroke="#64748b" stroke-width="2"/>
            <path d="M138,65 C138,82 182,82 182,65" fill="#1e293b"/>
            <line x1="150" y1="35" x2="165" y2="65" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
            <text x="160" y="94" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Pharmacist Compounding Care</text>
        </svg>`
    }
};

function selectMedicalRole(role) {
    const data = medicalRoles[role];
    if (!data) return;
    playClickSfx();
    
    ['doc', 'nurse', 'lab', 'pharm'].forEach(k => {
        const btn = document.getElementById(`mre-btn-${k}`);
        if (!btn) return;
        if (k === role) {
            btn.className = "p-2.5 rounded-xl border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('mre-visual-box');
    const iBox = document.getElementById('mre-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-indigo-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 8: Virtual ATM & Bank Vault ---
let atmBalance = 12500;
function doAtmAction(action) {
    const vBox = document.getElementById('atm-visual-box');
    const iBox = document.getElementById('atm-info-box');
    playClickSfx();
    
    ['balance', 'withdraw', 'deposit'].forEach(k => {
        const btn = document.getElementById(`atm-btn-${k}`);
        if (!btn) return;
        if (k === action) {
            btn.className = "p-2.5 rounded-xl border border-amber-500 bg-amber-950/40 text-amber-300 font-bold ring-2 ring-amber-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    if (action === 'withdraw') {
        if (atmBalance >= 500) {
            playSuccessSfx();
            atmBalance -= 500;
        }
    } else if (action === 'deposit') {
        playSuccessSfx();
        atmBalance += 1000;
    }
    
    if (vBox) {
        vBox.innerHTML = `
            <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                <rect x="70" y="10" width="180" height="80" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                <rect x="85" y="20" width="100" height="40" rx="3" fill="#0f172a" stroke="#059669" stroke-width="1.5"/>
                <text x="135" y="35" fill="#34d399" font-size="7" font-weight="bold" text-anchor="middle">BANK SAVINGS SECURE</text>
                <text x="135" y="48" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">₹${atmBalance.toLocaleString('en-IN')}</text>
                <rect x="195" y="20" width="45" height="40" rx="2" fill="#334155"/>
                <rect x="85" y="68" width="100" height="10" rx="2" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
                <rect x="110" y="71" width="50" height="4" fill="#22c55e"/>
            </svg>
        `;
    }
    
    if (iBox) {
        if (action === 'withdraw') {
            iBox.innerHTML = `<strong class="text-amber-400">Cash Withdrawn:</strong> Dispensed ₹500 from secure ATM cash slot. Updated balance: ₹${atmBalance.toLocaleString('en-IN')}.`;
        } else if (action === 'deposit') {
            iBox.innerHTML = `<strong class="text-emerald-400">Cash Deposited:</strong> Credited ₹1,000 to bank savings account. Updated balance: ₹${atmBalance.toLocaleString('en-IN')}.`;
        } else {
            iBox.innerHTML = `<strong class="text-amber-400">Account Inquiry:</strong> Verified with secret 4-digit PIN. Current Savings Balance: ₹${atmBalance.toLocaleString('en-IN')}. Banks safeguard funds and pay interest on deposits.`;
        }
    }
}

// --- Sim 9: Evolution of Money Exhibit ---
const moneyStages = {
    commodity: {
        title: "Commodity Trade",
        desc: "Early farming communities exchanged cattle, sheep, wheat grains, and salt blocks directly before coins existed.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="70" y="35" width="45" height="45" rx="6" fill="#78350f" stroke="#d97706" stroke-width="2"/>
            <text x="92.5" y="60" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">WHEAT</text>
            <text x="160" y="60" fill="#cbd5e1" font-size="16" font-weight="bold">⇄</text>
            <rect x="195" y="40" width="50" height="30" rx="4" fill="#d97706"/>
            <circle cx="250" cy="45" r="8" fill="#d97706"/>
            <text x="160" y="92" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Perishable Commodity Barter</text>
        </svg>`
    },
    shell: {
        title: "Cowrie Shells",
        desc: "Rare sea shells were collected and used as lightweight, durable, and recognizable decorative currency across ancient trade routes.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <ellipse cx="120" cy="50" rx="18" ry="24" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <line x1="120" y1="32" x2="120" y2="68" stroke="#78350f" stroke-width="3"/>
            <ellipse cx="170" cy="50" rx="18" ry="24" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <line x1="170" y1="32" x2="170" y2="68" stroke="#78350f" stroke-width="3"/>
            <text x="145" y="92" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Ancient Cowrie Currency</text>
        </svg>`
    },
    coin: {
        title: "Stamped Metal Coins",
        desc: "Ancient rulers minted copper, silver, and gold coins stamped with royal emblems, guaranteeing weight and legal purchasing value.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="130" cy="50" r="22" fill="#eab308" stroke="#ca8a04" stroke-width="3"/>
            <circle cx="130" cy="50" r="16" fill="none" stroke="#78350f" stroke-width="1.5"/>
            <text x="130" y="54" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">👑</text>
            <circle cx="190" cy="50" r="20" fill="#94a3b8" stroke="#64748b" stroke-width="3"/>
            <text x="190" y="54" fill="#1e293b" font-size="8" font-weight="bold" text-anchor="middle">SILVER</text>
        </svg>`
    },
    paper: {
        title: "Standardized Paper Notes",
        desc: "Sovereign reserve banks issue standardized paper currency notes with security watermarks, serial numbers, and legal tender promises.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="90" y="25" width="140" height="55" rx="4" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>
            <circle cx="120" cy="52" r="14" fill="#93c5fd"/>
            <text x="120" y="56" fill="#1e3a8a" font-size="10" font-weight="bold" text-anchor="middle">₹</text>
            <text x="180" y="45" fill="#1e3a8a" font-size="9" font-weight="bold">₹100</text>
            <text x="180" y="62" fill="#1e40af" font-size="6">LEGAL TENDER</text>
        </svg>`
    },
    digital: {
        title: "Digital UPI & Mobile Banking",
        desc: "Money travels invisibly through secure bank computer networks, QR codes, and phone apps, enabling instant cashless payments.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="135" y="15" width="50" height="70" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
            <rect x="142" y="25" width="36" height="36" fill="#f8fafc"/>
            <rect x="146" y="29" width="10" height="10" fill="#0f172a"/>
            <rect x="164" y="29" width="10" height="10" fill="#0f172a"/>
            <rect x="146" y="47" width="10" height="10" fill="#0f172a"/>
            <text x="160" y="93" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Instant Digital UPI Payment</text>
        </svg>`
    }
};

function selectMoneyStage(stage) {
    const data = moneyStages[stage];
    if (!data) return;
    playClickSfx();
    
    ['commodity', 'shell', 'coin', 'paper', 'digital'].forEach(k => {
        const btn = document.getElementById(`eom-btn-${k}`);
        if (!btn) return;
        if (k === stage) {
            btn.className = "p-2 rounded-lg border border-yellow-500 bg-yellow-950/40 text-yellow-300 font-bold ring-2 ring-yellow-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('eom-visual-box');
    const iBox = document.getElementById('eom-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-yellow-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 10: Barter vs Money Simulator ---
function selectTradeMode(mode) {
    const vBox = document.getElementById('bvm-visual-box');
    const iBox = document.getElementById('bvm-info-box');
    playClickSfx();
    
    const btnB = document.getElementById('bvm-btn-barter');
    const btnM = document.getElementById('bvm-btn-money');
    
    if (mode === 'barter') {
        if (btnB) btnB.className = "p-2.5 rounded-xl border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500 transition-all flex items-center justify-center gap-2";
        if (btnM) btnM.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex items-center justify-center gap-2";
        
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <circle cx="70" cy="40" r="12" fill="#fed7aa"/>
                    <rect x="55" y="55" width="30" height="25" fill="#ea580c"/>
                    <text x="70" y="90" fill="#fdba74" font-size="8" text-anchor="middle">Potter (Has Pots)</text>
                    <text x="160" y="45" fill="#ef4444" font-size="18" font-weight="bold" text-anchor="middle">❌ MISMATCH</text>
                    <text x="160" y="65" fill="#fca5a5" font-size="7" text-anchor="middle">Seller wants cloth, not pots!</text>
                    <circle cx="250" cy="40" r="12" fill="#fed7aa"/>
                    <rect x="235" y="55" width="30" height="25" fill="#16a34a"/>
                    <text x="250" y="90" fill="#86efac" font-size="8" text-anchor="middle">Fruit Seller (Has Mangoes)</text>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-orange-400">Barter Bottleneck:</strong> The potter has pots and desires mangoes, but the fruit seller needs cloth! Trade fails without a double coincidence of wants.`;
        }
    } else {
        if (btnB) btnB.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex items-center justify-center gap-2";
        if (btnM) btnM.className = "p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex items-center justify-center gap-2";
        
        if (vBox) {
            vBox.innerHTML = `
                <svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
                    <circle cx="70" cy="40" r="12" fill="#fed7aa"/>
                    <rect x="55" y="55" width="30" height="25" fill="#ea580c"/>
                    <circle cx="160" cy="45" r="16" fill="#22c55e" stroke="#15803d" stroke-width="2"/>
                    <text x="160" y="51" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">₹</text>
                    <text x="160" y="75" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Instant Fair Trade!</text>
                    <circle cx="250" cy="40" r="12" fill="#fed7aa"/>
                    <rect x="235" y="55" width="30" height="25" fill="#16a34a"/>
                </svg>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-emerald-400">Money Unlocks Trade:</strong> Potter sells pots for ₹100, then buys mangoes for ₹40. Standard currency is universally accepted, solving all barter dilemmas!`;
        }
    }
}

// --- Sim 11: Passbook & Budget Planner ---
function selectBudgetTab(tab) {
    const vBox = document.getElementById('pab-visual-box');
    const iBox = document.getElementById('pab-info-box');
    playClickSfx();
    
    const btnP = document.getElementById('pab-btn-passbook');
    const btnB = document.getElementById('pab-btn-budget');
    
    if (tab === 'passbook') {
        if (btnP) btnP.className = "p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all";
        if (btnB) btnB.className = "p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all";
        
        if (vBox) {
            vBox.innerHTML = `
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-slate-700 text-emerald-400">
                            <th class="p-1">Date</th>
                            <th class="p-1">Particulars</th>
                            <th class="p-1">Withdrawal (-)</th>
                            <th class="p-1">Deposit (+)</th>
                            <th class="p-1">Balance</th>
                        </tr>
                    </thead>
                    <tbody class="text-slate-300 divide-y divide-slate-800">
                        <tr><td class="p-1">01/10</td><td>Opening Balance</td><td>-</td><td>-</td><td class="font-bold text-white">₹10,000</td></tr>
                        <tr><td class="p-1">05/10</td><td>Monthly Salary</td><td>-</td><td class="text-emerald-400 font-bold">+₹15,000</td><td class="font-bold text-white">₹25,000</td></tr>
                        <tr><td class="p-1">10/10</td><td>Grocery Purchase</td><td class="text-rose-400 font-bold">-₹3,500</td><td>-</td><td class="font-bold text-white">₹21,500</td></tr>
                        <tr><td class="p-1">15/10</td><td>School Books Fee</td><td class="text-rose-400 font-bold">-₹1,200</td><td>-</td><td class="font-bold text-white">₹20,300</td></tr>
                    </tbody>
                </table>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-emerald-400">Passbook Ledger:</strong> Shows transaction dates, withdrawal (debit), deposit (credit), and running balance. Prudent budgeters prioritize essentials over luxuries.`;
        }
    } else {
        if (btnP) btnP.className = "p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all";
        if (btnB) btnB.className = "p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all";
        
        if (vBox) {
            vBox.innerHTML = `
                <div class="w-full grid grid-cols-3 gap-3 text-center text-xs p-2">
                    <div class="bg-blue-950/60 p-3 rounded-xl border border-blue-600">
                        <div class="text-xl font-bold text-blue-400">60%</div>
                        <div class="font-bold text-white">Essential Needs</div>
                        <div class="text-[10px] text-blue-300">Food, Water, School, Medicines</div>
                    </div>
                    <div class="bg-emerald-950/60 p-3 rounded-xl border border-emerald-600">
                        <div class="text-xl font-bold text-emerald-400">25%</div>
                        <div class="font-bold text-white">Future Savings</div>
                        <div class="text-[10px] text-emerald-300">Bank Deposit, Emergency Fund</div>
                    </div>
                    <div class="bg-purple-950/60 p-3 rounded-xl border border-purple-600">
                        <div class="text-xl font-bold text-purple-400">15%</div>
                        <div class="font-bold text-white">Optional Wants</div>
                        <div class="text-[10px] text-purple-300">Hobbies, Toys, Celebrations</div>
                    </div>
                </div>
            `;
        }
        if (iBox) {
            iBox.innerHTML = `<strong class="text-emerald-400">Sensible 60-25-15 Budget Rule:</strong> Fund essential survival and education needs first, set aside 25% for emergency bank savings, and keep discretionary wants under control.`;
        }
    }
}

// --- Sim 12: Essential Public Services Hub ---
const publicServices = {
    police: {
        title: "Police Station (Dial 112)",
        desc: "Protects citizens, investigates crimes, maintains neighbourhood order, and assists vulnerable residents during emergencies.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="120" y="20" width="80" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="160,25 175,35 168,55 152,55 145,35" fill="#0284c7"/>
            <text x="160" y="45" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">★</text>
            <text x="160" y="90" fill="#7dd3fc" font-size="8" font-weight="bold" text-anchor="middle">Police Emergency: 112</text>
        </svg>`
    },
    fire: {
        title: "Fire Station (Dial 101)",
        desc: "Deploys brave firefighters, high-pressure water cannons, and extendable ladders to extinguish fires and rescue endangered citizens.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="90" y="30" width="120" height="45" rx="6" fill="#dc2626" stroke="#ef4444" stroke-width="2"/>
            <line x1="100" y1="25" x2="190" y2="25" stroke="#cbd5e1" stroke-width="3"/>
            <line x1="100" y1="20" x2="190" y2="20" stroke="#cbd5e1" stroke-width="3"/>
            <circle cx="120" cy="75" r="7" fill="#0f172a"/><circle cx="185" cy="75" r="7" fill="#0f172a"/>
            <text x="160" y="92" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Fire Emergency: 101</text>
        </svg>`
    },
    hospital: {
        title: "Civil Hospital (Dial 102)",
        desc: "Operates 24/7 trauma emergency care, ambulance transport, maternity wards, and outpatient clinics for neighbourhood healing.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="110" y="20" width="100" height="55" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
            <rect x="155" y="32" width="10" height="26" fill="#ef4444"/>
            <rect x="147" y="40" width="26" height="10" fill="#ef4444"/>
            <text x="160" y="90" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Hospital Ambulance: 102</text>
        </svg>`
    },
    library: {
        title: "Public Community Library",
        desc: "Provides free access to educational books, encyclopedias, quiet reading halls, and newspapers to promote literacy for all ages.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="100" y="25" width="120" height="50" rx="4" fill="#065f46" stroke="#34d399" stroke-width="2"/>
            <path d="M140,40 Q160,35 180,40" stroke="#f8fafc" stroke-width="3" fill="none"/>
            <path d="M140,55 Q160,50 180,55" stroke="#f8fafc" stroke-width="3" fill="none"/>
            <line x1="160" y1="36" x2="160" y2="58" stroke="#f8fafc" stroke-width="2"/>
            <text x="160" y="90" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Free Community Learning</text>
        </svg>`
    }
};

function selectPublicService(srv) {
    const data = publicServices[srv];
    if (!data) return;
    playClickSfx();
    
    ['police', 'fire', 'hospital', 'library'].forEach(k => {
        const btn = document.getElementById(`eps-btn-${k}`);
        if (!btn) return;
        if (k === srv) {
            btn.className = "p-2 rounded-xl border border-sky-500 bg-sky-950/40 text-sky-300 font-bold ring-2 ring-sky-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('eps-visual-box');
    const iBox = document.getElementById('eps-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-sky-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 13: Sun & Cardinal Directions ---
const compassOrientations = {
    east: {
        title: "Facing East (Morning Sunrise)",
        desc: "Early morning rising sun is ahead. Your back points West, your left hand points North, and your right hand points South!",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="270" cy="50" r="18" fill="#f59e0b"/>
            <line x1="270" y1="24" x2="270" y2="18" stroke="#f59e0b" stroke-width="3"/>
            <line x1="270" y1="76" x2="270" y2="82" stroke="#f59e0b" stroke-width="3"/>
            <circle cx="130" cy="50" r="10" fill="#fed7aa"/>
            <line x1="130" y1="30" x2="130" y2="70" stroke="#f43f5e" stroke-width="4"/>
            <text x="130" y="22" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">NORTH (Left Arm)</text>
            <text x="130" y="86" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">SOUTH (Right Arm)</text>
            <text x="60" y="54" fill="#a78bfa" font-size="8" font-weight="bold" text-anchor="middle">WEST (Back)</text>
            <text x="210" y="54" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">EAST (Ahead)</text>
        </svg>`
    },
    west: {
        title: "Facing West (Evening Sunset)",
        desc: "Facing the setting sun in the West: East is behind you, your right arm points North, and your left arm points South.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="50" cy="50" r="18" fill="#ea580c"/>
            <circle cx="190" cy="50" r="10" fill="#fed7aa"/>
            <line x1="190" y1="30" x2="190" y2="70" stroke="#f43f5e" stroke-width="4"/>
            <text x="190" y="22" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">NORTH (Right Arm)</text>
            <text x="190" y="86" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">SOUTH (Left Arm)</text>
            <text x="110" y="54" fill="#ea580c" font-size="8" font-weight="bold" text-anchor="middle">WEST (Ahead)</text>
            <text x="260" y="54" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">EAST (Back)</text>
        </svg>`
    },
    north: {
        title: "Facing North (Standard Map View)",
        desc: "Facing North: South is directly behind your back, East is toward your right hand, and West is toward your left hand.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="50" r="10" fill="#fed7aa"/>
            <line x1="130" y1="50" x2="190" y2="50" stroke="#f43f5e" stroke-width="4"/>
            <text x="160" y="20" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">▲ NORTH (Ahead / Map Top)</text>
            <text x="160" y="85" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">▼ SOUTH (Behind)</text>
            <text x="95" y="54" fill="#a78bfa" font-size="8" font-weight="bold" text-anchor="middle">WEST (Left)</text>
            <text x="225" y="54" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">EAST (Right)</text>
        </svg>`
    },
    south: {
        title: "Facing South",
        desc: "Facing South: North is directly behind you, East is toward your left hand, and West is toward your right hand.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="50" r="10" fill="#fed7aa"/>
            <line x1="130" y1="50" x2="190" y2="50" stroke="#f43f5e" stroke-width="4"/>
            <text x="160" y="20" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">▲ NORTH (Behind)</text>
            <text x="160" y="85" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">▼ SOUTH (Ahead / Map Bottom)</text>
            <text x="95" y="54" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">EAST (Left)</text>
            <text x="225" y="54" fill="#a78bfa" font-size="8" font-weight="bold" text-anchor="middle">WEST (Right)</text>
        </svg>`
    }
};

function orientCompass(dir) {
    const data = compassOrientations[dir];
    if (!data) return;
    playClickSfx();
    
    ['east', 'west', 'north', 'south'].forEach(k => {
        const btn = document.getElementById(`scd-btn-${k}`);
        if (!btn) return;
        if (k === dir) {
            btn.className = "p-2 rounded-xl border border-fuchsia-500 bg-fuchsia-950/40 text-fuchsia-300 font-bold ring-2 ring-fuchsia-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('scd-visual-box');
    const iBox = document.getElementById('scd-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-fuchsia-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 14: Neighbourhood Map Navigator ---
const mapBuildings = {
    hospital: {
        title: "Route to Hospital (North)",
        desc: "From the central School landmark, walk North (upward on map) along Main Avenue for 200 metres. The hospital is on the left.",
        pathColor: "#ef4444"
    },
    library: {
        title: "Route to Library (East)",
        desc: "From School, head East (rightward on map) past the clock tower. The Public Library stands on the northern side of Reading Lane.",
        pathColor: "#3b82f6"
    },
    park: {
        title: "Route to Park (South)",
        desc: "From School, walk South (downward on map) across the pedestrian crossing to reach the Green Community Park.",
        pathColor: "#22c55e"
    },
    postoffice: {
        title: "Route to Post Office (West)",
        desc: "From School, walk West (leftward on map) along Market Road. The red Post Office is situated beside the bus terminus.",
        pathColor: "#f43f5e"
    }
};

function navigateToBuilding(dest) {
    const data = mapBuildings[dest];
    if (!data) return;
    playClickSfx();
    
    ['hospital', 'library', 'park', 'postoffice'].forEach(k => {
        const btn = document.getElementById(`nmn-btn-${k}`);
        if (!btn) return;
        if (k === dest) {
            btn.className = "p-2 rounded-xl border border-violet-500 bg-violet-950/40 text-violet-300 font-bold ring-2 ring-violet-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('nmn-visual-box');
    const iBox = document.getElementById('nmn-info-box');
    
    if (vBox) {
        vBox.innerHTML = `
            <svg viewBox="0 0 320 120" class="w-full max-h-[120px]">
                <line x1="160" y1="10" x2="160" y2="110" stroke="#334155" stroke-width="20"/>
                <line x1="20" y1="60" x2="300" y2="60" stroke="#334155" stroke-width="20"/>
                <rect x="145" y="45" width="30" height="30" rx="4" fill="#f59e0b"/>
                <text x="160" y="63" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">🏫 SCHOOL</text>
                <rect x="145" y="8" width="30" height="20" rx="3" fill="#ef4444"/>
                <text x="160" y="21" fill="#ffffff" font-size="6" font-weight="bold" text-anchor="middle">🏥 HOSPITAL</text>
                <rect x="260" y="48" width="36" height="24" rx="3" fill="#0284c7"/>
                <text x="278" y="63" fill="#ffffff" font-size="6" font-weight="bold" text-anchor="middle">📚 LIBRARY</text>
                <rect x="145" y="90" width="30" height="22" rx="3" fill="#16a34a"/>
                <text x="160" y="104" fill="#ffffff" font-size="6" font-weight="bold" text-anchor="middle">🌳 PARK</text>
                <rect x="25" y="48" width="38" height="24" rx="3" fill="#dc2626"/>
                <text x="44" y="63" fill="#ffffff" font-size="5" font-weight="bold" text-anchor="middle">📮 POST OFF.</text>
                <circle cx="295" cy="20" r="12" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
                <text x="295" y="23" fill="#a78bfa" font-size="8" font-weight="bold" text-anchor="middle">N ▲</text>
            </svg>
        `;
    }
    
    if (iBox) {
        iBox.innerHTML = `<strong class="text-violet-400">${data.title}:</strong> ${data.desc}`;
    }
}

// --- Sim 15: Frontline Heroes Tribute ---
const frontlineHeroes = {
    sanitation: {
        title: "Sanitation Worker",
        desc: "Arrives at dawn to sweep streets, clear refuse bins, and sanitize lanes, preventing dangerous disease vectors and keeping our neighbourhood clean.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="35" r="14" fill="#fed7aa"/>
            <rect x="145" y="52" width="30" height="30" fill="#059669"/>
            <line x1="175" y1="40" x2="195" y2="85" stroke="#78350f" stroke-width="3"/>
            <polygon points="190,80 205,80 200,92 185,92" fill="#ca8a04"/>
            <text x="160" y="94" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Street Sanitation & Hygiene</text>
        </svg>`
    },
    medical: {
        title: "Doctors & Nursing Heroes",
        desc: "Provide selfless round-the-clock medical treatment, emergency resuscitation, and comforting care to patients during health crises.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="130" cy="35" r="12" fill="#fed7aa"/>
            <rect x="118" y="50" width="24" height="32" fill="#0284c7"/>
            <circle cx="190" cy="35" r="12" fill="#fed7aa"/>
            <rect x="178" y="50" width="24" height="32" fill="#f8fafc"/>
            <text x="160" y="94" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Emergency Medical Team</text>
        </svg>`
    },
    grocery: {
        title: "Grocery & Food Vendors",
        desc: "Keep markets stocked with fresh vegetables, milk, grains, and clean drinking water so families have daily nourishment.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="35" r="14" fill="#fed7aa"/>
            <rect x="145" y="52" width="30" height="30" fill="#d97706"/>
            <rect x="180" y="55" width="35" height="25" fill="#78350f" stroke="#b45309"/>
            <circle cx="190" cy="62" r="4" fill="#ef4444"/><circle cx="202" cy="62" r="4" fill="#84cc16"/>
            <text x="160" y="94" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Essential Food Supply</text>
        </svg>`
    },
    utility: {
        title: "Public Utility Linemen",
        desc: "Work through heavy rains and storms to repair electrical power grids, clear blocked storm drains, and restore drinking water pipelines.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <circle cx="160" cy="35" r="14" fill="#fed7aa"/>
            <polygon points="144,25 176,25 170,18 150,18" fill="#eab308"/>
            <rect x="145" y="52" width="30" height="30" fill="#0284c7"/>
            <line x1="180" y1="50" x2="195" y2="70" stroke="#94a3b8" stroke-width="4"/>
            <text x="160" y="94" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Power & Water Grid Maintenance</text>
        </svg>`
    }
};

function selectFrontlineHero(hero) {
    const data = frontlineHeroes[hero];
    if (!data) return;
    playClickSfx();
    
    ['sanitation', 'medical', 'grocery', 'utility'].forEach(k => {
        const btn = document.getElementById(`fht-btn-${k}`);
        if (!btn) return;
        if (k === hero) {
            btn.className = "p-2.5 rounded-xl border border-pink-500 bg-pink-950/40 text-pink-300 font-bold ring-2 ring-pink-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('fht-visual-box');
    const iBox = document.getElementById('fht-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-pink-400">${data.title}:</strong> ${data.desc}`;
}

// --- Sim 16: Emergency Vehicle Dispatcher ---
const dispatchVehicles = {
    fire: {
        title: "Fire Engine Dispatched (Dial 101)",
        desc: "Red truck equipped with water hoses, foam extinguishers, and hydraulic ladders races to the scene to protect lives and property.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="70" y="30" width="160" height="45" rx="6" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
            <circle cx="100" cy="75" r="8" fill="#0f172a"/><circle cx="185" cy="75" r="8" fill="#0f172a"/>
            <polygon points="140,24 150,15 160,24" fill="#fbbf24"/>
            <text x="150" y="55" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">FIRE RESCUE 101</text>
        </svg>`
    },
    ambulance: {
        title: "Emergency Ambulance Dispatched (Dial 102)",
        desc: "Life-support vehicle carrying oxygen cylinders, patient stretchers, and paramedics provides first aid en route to hospital.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="80" y="30" width="140" height="45" rx="6" fill="#f8fafc" stroke="#dc2626" stroke-width="2"/>
            <rect x="145" y="40" width="10" height="24" fill="#dc2626"/>
            <rect x="138" y="47" width="24" height="10" fill="#dc2626"/>
            <circle cx="110" cy="75" r="8" fill="#0f172a"/><circle cx="185" cy="75" r="8" fill="#0f172a"/>
            <text x="150" y="93" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Ambulance Life Support (102)</text>
        </svg>`
    },
    police: {
        title: "Police Patrol Car Dispatched (Dial 112)",
        desc: "Vigilant police patrol vehicle with two-way communications and siren reaches neighbourhood streets to secure safety.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="90" y="35" width="120" height="38" rx="6" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
            <polygon points="145,26 155,18 165,26" fill="#ef4444"/>
            <circle cx="115" cy="73" r="8" fill="#0f172a"/><circle cx="185" cy="73" r="8" fill="#0f172a"/>
            <text x="150" y="57" fill="#93c5fd" font-size="9" font-weight="bold" text-anchor="middle">POLICE 112</text>
        </svg>`
    },
    bookmobile: {
        title: "Mobile Library Bookmobile",
        desc: "Specialized municipal van fitted with book lending shelves brings stories, encyclopedias, and science books directly to residential alleys.",
        svg: `<svg viewBox="0 0 320 100" class="w-full max-h-[110px]">
            <rect x="80" y="30" width="140" height="45" rx="6" fill="#047857" stroke="#34d399" stroke-width="2"/>
            <rect x="100" y="38" width="60" height="25" fill="#f8fafc"/>
            <line x1="110" y1="42" x2="110" y2="58" stroke="#1e293b" stroke-width="2"/>
            <line x1="120" y1="42" x2="120" y2="58" stroke="#b91c1c" stroke-width="2"/>
            <line x1="130" y1="42" x2="130" y2="58" stroke="#0284c7" stroke-width="2"/>
            <circle cx="105" cy="75" r="8" fill="#0f172a"/><circle cx="185" cy="75" r="8" fill="#0f172a"/>
            <text x="150" y="93" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Community Bookmobile</text>
        </svg>`
    }
};

function dispatchEmergencyVehicle(vtype) {
    const data = dispatchVehicles[vtype];
    if (!data) return;
    playClickSfx();
    
    ['fire', 'ambulance', 'police', 'bookmobile'].forEach(k => {
        const btn = document.getElementById(`evd-btn-${k}`);
        if (!btn) return;
        if (k === vtype) {
            btn.className = "p-2.5 rounded-xl border border-red-500 bg-red-950/40 text-red-300 font-bold ring-2 ring-red-500 transition-all flex flex-col items-center gap-1";
        } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1";
        }
    });
    
    const vBox = document.getElementById('evd-visual-box');
    const iBox = document.getElementById('evd-info-box');
    if (vBox) vBox.innerHTML = data.svg;
    if (iBox) iBox.innerHTML = `<strong class="text-red-400">${data.title}:</strong> ${data.desc}`;
}

// ============================================================================
// Simulator Initialization Dispatcher
// ============================================================================
function initSimulatorForSlide(slideNum) {
    if (slideNum === 1) selectRouteWaypoint('school');
    if (slideNum === 2) selectCommEra('ancient');
    if (slideNum === 3) renderPostalStep(1);
    if (slideNum === 4) selectTransitMode('flyover');
    if (slideNum === 5) updateEcoDisplay();
    if (slideNum === 6) selectClinicSection('eye');
    if (slideNum === 7) selectMedicalRole('doc');
    if (slideNum === 8) doAtmAction('balance');
    if (slideNum === 9) selectMoneyStage('commodity');
    if (slideNum === 10) selectTradeMode('barter');
    if (slideNum === 11) selectBudgetTab('passbook');
    if (slideNum === 12) selectPublicService('police');
    if (slideNum === 13) orientCompass('east');
    if (slideNum === 14) navigateToBuilding('hospital');
    if (slideNum === 15) selectFrontlineHero('sanitation');
    if (slideNum === 16) dispatchEmergencyVehicle('fire');
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

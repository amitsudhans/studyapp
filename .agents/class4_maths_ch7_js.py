# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 7 JavaScript Engine"""

js_code = r'''
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
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1); // E5
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2); // G5
        
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
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        
        osc.start(now);
        osc.stop(now + 0.08);
    } catch(e) {}
}

// ============================================================================
// Indian English Male Teacher Narration Engine
// ============================================================================
function selectIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;
    
    const femaleTerms = ['female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera', 'kavya'];
    const malePreferred = ['microsoft prabhat', 'rishi', 'microsoft ravi', 'pradeep', 'madhav', 'karan', 'mohan', 'google uk english male', 'microsoft david', 'microsoft mark', 'alex'];
    
    // 1. Look for prioritized Indian Male voices
    for (const pref of malePreferred) {
        const found = voices.find(v => {
            const name = v.name.toLowerCase();
            const lang = v.lang.toLowerCase();
            const isFemale = femaleTerms.some(f => name.includes(f));
            return !isFemale && (name.includes(pref) || (lang.includes('en-in') && name.includes(pref)));
        });
        if (found) return found;
    }
    
    // 2. Any Indian English non-female voice
    const anyIndian = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.includes('en-in');
    });
    if (anyIndian) return anyIndian;
    
    // 3. Any English non-female fallback
    const fallback = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.startsWith('en');
    });
    return fallback || voices[0];
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
    if (!slide || currentSlide > 16) {
        alert('Classroom lecture is only available on Slides 1 to 16.');
        return;
    }
    
    const lectureText = slide.speech || slide.lecture;
    if (!lectureText) return;
    
    window.speechSynthesis.cancel();
    clearInterval(keepAliveTimer);
    
    currentUtterance = new SpeechSynthesisUtterance(lectureText);
    currentUtterance.rate = 0.94;
    currentUtterance.pitch = 0.85;
    
    const voices = window.speechSynthesis.getVoices();
    const chosenVoice = selectIndianMaleVoice(voices);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    
    // Chrome keep-alive watchdog
    keepAliveTimer = setInterval(() => {
        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        } else {
            clearInterval(keepAliveTimer);
        }
    }, 10000);
    
    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioButtonUI(true);
    };
    
    currentUtterance.onend = () => {
        isSpeaking = false;
        clearInterval(keepAliveTimer);
        updateAudioButtonUI(false);
    };
    
    currentUtterance.onerror = () => {
        isSpeaking = false;
        clearInterval(keepAliveTimer);
        updateAudioButtonUI(false);
    };
    
    window.speechSynthesis.speak(currentUtterance);
}

function stopAudioLecture() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    clearInterval(keepAliveTimer);
    isSpeaking = false;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(speaking) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (speaking) {
        btn.innerHTML = `
            <svg class="w-4 h-4 text-rose-400 animate-pulse" fill="currentColor" viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>
            <span class="text-xs font-bold text-rose-300">Stop Lecture</span>
        `;
        btn.classList.add('border-rose-500/50', 'bg-rose-500/10');
    } else {
        btn.innerHTML = `
            <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span class="text-xs font-bold text-emerald-300">Listen Teacher Lecture</span>
        `;
        btn.classList.remove('border-rose-500/50', 'bg-rose-500/10');
    }
}

// Preload voices
if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
    };
}

// ============================================================================
// Slide Navigation & Terminal Slide Invariant
// ============================================================================
function showSlide(num) {
    if (num < 1 || num > totalSlides) return;
    stopAudioLecture();
    
    // Hide all slides
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));
    
    // Show current slide
    const target = document.getElementById(`slide-${num}`);
    if (target) {
        target.classList.remove('hidden');
    }
    
    currentSlide = num;
    const curNumEl = document.getElementById('currentSlideNum');
    if (curNumEl) curNumEl.innerText = currentSlide;
    
    // Progress bar
    const progressPct = ((currentSlide) / totalSlides) * 100;
    const pbar = document.getElementById('chapterProgressBar');
    if (pbar) pbar.style.width = `${progressPct}%`;
    
    // Previous button state
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
    
    // Initialize slide-specific simulators if needed
    initSlideSimulator(currentSlide);
    window.scrollTo({ top: 0, behavior: 'smooth' });
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
// Checkpoint Validation
// ============================================================================
function checkCheckpoint(slideId, cpIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints || !slide.checkpoints[cpIdx]) return;
    
    const cp = slide.checkpoints[cpIdx];
    const fb = document.getElementById(`cp-fb-${slideId}-${cpIdx}`);
    const btns = document.querySelectorAll(`.cp-btn-${slideId}-${cpIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = (cp.ans !== undefined) ? cp.ans : cp.answer;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        btns[optIdx].classList.remove('bg-emerald-600/30');
        btns[optIdx].classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        fb.innerHTML = `
            <div class="p-2.5 rounded-xl bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 text-xs font-semibold flex items-start gap-2">
                <span>✅</span> <span><strong>Correct!</strong> ${cp.exp || cp.explanation}</span>
            </div>
        `;
    } else {
        playErrorSfx();
        btns[optIdx].classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        fb.innerHTML = `
            <div class="p-2.5 rounded-xl bg-rose-500/15 border border-rose-500/40 text-rose-300 text-xs font-semibold flex items-start gap-2">
                <span>❌</span> <span><strong>Try Again!</strong> ${cp.exp || cp.explanation}</span>
            </div>
        `;
    }
    fb.classList.remove('hidden');
}

// ============================================================================
// Mastery Quiz & Pop-up Solution Modal
// ============================================================================
function selectQuizOption(qId, optIdx) {
    let qData = null;
    for (const s of SLIDES) {
        if (s.quiz) {
            const found = s.quiz.find(item => item.id === qId);
            if (found) {
                qData = found;
                break;
            }
        }
    }
    if (!qData) return;
    
    const fb = document.getElementById(`quiz-fb-${qId}`);
    const btns = document.querySelectorAll(`.quiz-opt-btn-${qId}`);
    if (!fb || !btns) return;
    
    const correctIdx = (qData.ans !== undefined) ? qData.ans : qData.answer;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        btns[optIdx].classList.remove('bg-emerald-600/30');
        btns[optIdx].classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 text-xs font-semibold flex flex-col gap-2">
                <div class="flex items-center justify-between">
                    <span>✅ Correct! ${qData.exp || ''}</span>
                    <button onclick="openSolutionModal(${qId})" class="px-2.5 py-1 rounded bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-[11px] transition shadow">View Solution</button>
                </div>
            </div>
        `;
    } else {
        playErrorSfx();
        btns[optIdx].classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-rose-500/15 border border-rose-500/40 text-rose-300 text-xs font-semibold flex flex-col gap-2">
                <div class="flex items-center justify-between">
                    <span>❌ Not quite! ${qData.exp || ''}</span>
                    <button onclick="openSolutionModal(${qId})" class="px-2.5 py-1 rounded bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-[11px] transition shadow">View Solution</button>
                </div>
            </div>
        `;
    }
    fb.classList.remove('hidden');
}

function openSolutionModal(qId) {
    let qData = null;
    for (const s of SLIDES) {
        if (s.quiz) {
            const found = s.quiz.find(item => item.id === qId);
            if (found) {
                qData = found;
                break;
            }
        }
    }
    if (!qData) return;
    
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionModalTitle');
    const content = document.getElementById('solutionModalContent');
    if (!modal || !title || !content) return;
    
    title.innerHTML = `<span>💡</span> Question ${qId} Detailed Solution`;
    content.innerHTML = `
        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm font-semibold text-slate-200">
            ${qData.q}
        </div>
        <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300 font-medium">
            <strong>Hint:</strong> ${qData.hint || 'Carefully note the numbers and place value columns.'}
        </div>
        <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Step-by-Step Derivation</h4>
            ${qData.sol || makeDefaultSol(qData)}
        </div>
    `;
    modal.classList.remove('hidden');
    playClickSfx();
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
    playClickSfx();
}

function makeDefaultSol(qData) {
    const correctIdx = (qData.ans !== undefined) ? qData.ans : qData.answer;
    const correctOpt = qData.options[correctIdx];
    return `
        <ol class="space-y-1.5 list-none pl-0">
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 1:</span> Understand the question requirements and note given numbers.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 2:</span> Apply the appropriate addition or subtraction regrouping rule.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 3:</span> Conclude that the correct answer is <strong>${correctOpt}</strong>.</li>
        </ol>
    `;
}

// ============================================================================
// Interactive Simulator Handlers (Simulators 1 to 16)
// ============================================================================

// Simulator 1: Village Field Trip Logistics
function setTripMetric(metric) {
    playClickSfx();
    const group = document.getElementById('tripDisplayGroup');
    const desc = document.getElementById('tripDesc');
    if (!group || !desc) return;

    document.querySelectorAll('.trip-btn').forEach(b => {
        b.className = 'trip-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-trip-${metric}`);
    if (btn) btn.className = 'trip-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';

    if (metric === 'time') {
        group.innerHTML = `
            <circle cx="110" cy="85" r="45" fill="#022c22" stroke="#34d399" stroke-width="2"/>
            <line x1="110" y1="85" x2="110" y2="52" stroke="#34d399" stroke-width="3" stroke-linecap="round"/>
            <line x1="110" y1="85" x2="85" y2="105" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
            <circle cx="110" cy="85" r="4" fill="#fbbf24"/>
            <text x="110" y="145" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">Departure: 7:00 AM</text>

            <path d="M 175 85 L 210 85" stroke="#38bdf8" stroke-width="3" stroke-dasharray="3 3"/>
            <text x="195" y="75" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">9 Hours</text>

            <circle cx="260" cy="85" r="35" fill="#022c22" stroke="#f59e0b" stroke-width="2"/>
            <line x1="260" y1="85" x2="260" y2="60" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="260" y1="85" x2="285" y2="100" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
            <circle cx="260" cy="85" r="3" fill="#ffffff"/>
            <text x="260" y="135" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Arrival: 4:00 PM</text>
        `;
        desc.innerHTML = 'From 7:00 AM to 12:00 noon (5h) + 12:00 noon to 4:00 PM (4h) = <span class="text-emerald-400 font-bold">9 Hours Travel Time</span>.';
    } else if (metric === 'pop') {
        group.innerHTML = `
            <rect x="50" y="45" width="110" height="80" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
            <text x="105" y="75" fill="#ffffff" font-size="20" font-weight="black" text-anchor="middle">77</text>
            <text x="105" y="100" fill="#a5b4fc" font-size="10" font-weight="bold" text-anchor="middle">Village Families</text>

            <rect x="200" y="45" width="110" height="80" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
            <text x="255" y="75" fill="#ffffff" font-size="20" font-weight="black" text-anchor="middle">414</text>
            <text x="255" y="100" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Total Residents</text>
        `;
        desc.innerHTML = '414 people living in 77 families = about <span class="text-emerald-400 font-bold">5 to 6 persons per household</span> on average.';
    } else if (metric === 'ticket') {
        group.innerHTML = `
            <rect x="80" y="45" width="200" height="80" rx="8" fill="#431407" stroke="#ea580c" stroke-width="2"/>
            <text x="180" y="72" fill="#fdba74" font-size="11" font-weight="bold" text-anchor="middle">Ticket Price: ₹500 / Child</text>
            <text x="180" y="98" fill="#fef08a" font-size="15" font-weight="black" text-anchor="middle">3 Children = 3 × 500 = ₹1,500</text>
        `;
        desc.innerHTML = 'Budgeting for 3 children: 500 + 500 + 500 = <span class="text-orange-400 font-bold">₹1,500 Total Tickets Cost</span>.';
    }
}

// Simulator 2: Market Cart Unit Pricing
let currentCartPrice = 95;
let currentCartItem = 'beans';
let currentCartQty = 2;

function selectCartItem(item) {
    playClickSfx();
    currentCartItem = item;
    const icon = document.getElementById('cartProduceIcon');
    const label = document.getElementById('cartProduceLabel');
    if (!icon || !label) return;

    document.querySelectorAll('.cart-btn').forEach(b => {
        b.className = 'cart-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-item-${item}`);
    if (btn) btn.className = 'cart-btn px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs shadow transition';

    if (item === 'beans') { currentCartPrice = 95; icon.innerText = '🫘'; label.innerText = 'Green Beans'; }
    else if (item === 'potato') { currentCartPrice = 37; icon.innerText = '🥔'; label.innerText = 'Potatoes'; }
    else if (item === 'onion') { currentCartPrice = 32; icon.innerText = '🧅'; label.innerText = 'Onions'; }
    else if (item === 'radish') { currentCartPrice = 23; icon.innerText = '🥕'; label.innerText = 'Radishes'; }

    updateCartCalc();
}

function setCartQty(qty) {
    playClickSfx();
    currentCartQty = qty;
    document.querySelectorAll('.qty-btn').forEach((b, idx) => {
        if (idx + 1 === qty) {
            b.className = 'qty-btn px-2.5 py-1 rounded bg-amber-500 text-slate-950 text-xs font-bold shadow';
        } else {
            b.className = 'qty-btn px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700';
        }
    });
    updateCartCalc();
}

function updateCartCalc() {
    const math = document.getElementById('cartMathText');
    const total = document.getElementById('cartTotalText');
    const desc = document.getElementById('cartDesc');
    if (!math || !total || !desc) return;

    const cost = currentCartPrice * currentCartQty;
    math.innerText = `${currentCartQty} kg × ₹${currentCartPrice}`;
    total.innerText = `= ₹${cost}`;
    desc.innerHTML = `${currentCartQty} kg of ${currentCartItem} at ₹${currentCartPrice}/kg: <span class="text-amber-400 font-bold">= ₹${cost}</span>.`;
}

// Simulator 3: Total Cost Combinations
function setBasketCombo(combo) {
    playClickSfx();
    const group = document.getElementById('receiptRowsGroup');
    const desc = document.getElementById('basketComboDesc');
    if (!group || !desc) return;

    document.querySelectorAll('.combo-btn').forEach(b => {
        b.className = 'combo-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'combo-btn px-3 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition';

    if (combo === 'standard') {
        group.innerHTML = `
            <text x="60" y="45" fill="#94a3b8" font-size="10" font-weight="bold">ITEM DESCRIPTION</text>
            <text x="300" y="45" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="end">PRICE</text>
            <line x1="60" y1="52" x2="300" y2="52" stroke="#475569" stroke-width="1"/>
            <text x="60" y="70" fill="#f8fafc" font-size="11">1 kg Onions</text>
            <text x="300" y="70" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="end">₹32</text>
            <text x="60" y="90" fill="#f8fafc" font-size="11">2 kg Potatoes (2 × ₹37)</text>
            <text x="300" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="end">₹74</text>
            <line x1="60" y1="102" x2="300" y2="102" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="60" y="125" fill="#38bdf8" font-size="13" font-weight="extrabold">TOTAL AMOUNT</text>
            <text x="300" y="125" fill="#38bdf8" font-size="15" font-weight="black" text-anchor="end">₹106</text>
        `;
        desc.innerHTML = 'Subtotal for potatoes: 37 + 37 = ₹74. Adding onions: 74 + 32 = <span class="text-cyan-400 font-bold">₹106</span>.';
    } else if (combo === 'target163') {
        group.innerHTML = `
            <text x="60" y="45" fill="#94a3b8" font-size="10" font-weight="bold">ITEM DESCRIPTION</text>
            <text x="300" y="45" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="end">PRICE</text>
            <line x1="60" y1="52" x2="300" y2="52" stroke="#475569" stroke-width="1"/>
            <text x="60" y="66" fill="#f8fafc" font-size="10">1 kg Green Beans</text>
            <text x="300" y="66" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="end">₹95</text>
            <text x="60" y="82" fill="#f8fafc" font-size="10">1 kg Onions</text>
            <text x="300" y="82" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="end">₹32</text>
            <text x="60" y="98" fill="#f8fafc" font-size="10">1 kg Fresh Produce</text>
            <text x="300" y="98" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="end">₹36</text>
            <line x1="60" y1="106" x2="300" y2="106" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="60" y="125" fill="#34d399" font-size="13" font-weight="extrabold">TARGET ₹163</text>
            <text x="300" y="125" fill="#34d399" font-size="15" font-weight="black" text-anchor="end">₹163</text>
        `;
        desc.innerHTML = 'Target ₹163 assembled: 95 + 32 = 127; 127 + 36 = <span class="text-emerald-400 font-bold">₹163 exact match</span>!';
    } else if (combo === 'fruits') {
        group.innerHTML = `
            <text x="60" y="45" fill="#94a3b8" font-size="10" font-weight="bold">ITEM DESCRIPTION</text>
            <text x="300" y="45" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="end">PRICE</text>
            <line x1="60" y1="52" x2="300" y2="52" stroke="#475569" stroke-width="1"/>
            <text x="60" y="70" fill="#f8fafc" font-size="11">1 kg Ripe Bananas</text>
            <text x="300" y="70" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="end">₹55</text>
            <text x="60" y="90" fill="#f8fafc" font-size="11">1 kg Sweet Papaya</text>
            <text x="300" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="end">₹65</text>
            <line x1="60" y1="102" x2="300" y2="102" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="60" y="125" fill="#f59e0b" font-size="13" font-weight="extrabold">TOTAL AMOUNT</text>
            <text x="300" y="125" fill="#f59e0b" font-size="15" font-weight="black" text-anchor="end">₹120</text>
        `;
        desc.innerHTML = 'Bananas (₹55) + Papaya (₹65) = <span class="text-amber-400 font-bold">₹120</span>.';
    }
}

// Simulator 4: Grocery Balance Math
function setBalanceScenario(bill, paid) {
    playClickSfx();
    const summary = document.getElementById('balanceMathSummary');
    const desc = document.getElementById('balanceDesc');
    if (!summary || !desc) return;

    document.querySelectorAll('.bal-btn').forEach(b => {
        b.className = 'bal-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'bal-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold text-xs shadow transition';

    const change = paid - bill;
    summary.innerText = `Paid ₹${paid} - Bill ₹${bill} = Change ₹${change}`;
    desc.innerHTML = `Customer tenders ₹${paid} for ₹${bill} bill. Cashier returns <span class="text-indigo-400 font-bold">₹${change} change</span>.`;
}

// Simulator 5: Orange Purchase Tenders
function setOrangeTender(note) {
    playClickSfx();
    const noteVal = document.getElementById('tenderNoteVal');
    const changeVal = document.getElementById('tenderChangeVal');
    const eq = document.getElementById('tenderEquationText');
    const desc = document.getElementById('orangeTenderDesc');
    if (!noteVal || !changeVal || !eq || !desc) return;

    document.querySelectorAll('.tender-btn').forEach(b => {
        b.className = 'tender-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'tender-btn px-2.5 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow transition';

    const change = note - 42;
    noteVal.innerText = `₹${note} Note`;
    changeVal.innerText = `Change: ₹${change}`;
    eq.innerText = `₹${note} - ₹42 = ₹${change}`;
    desc.innerHTML = `Paying with ₹${note}: <span class="text-orange-400 font-bold">₹${note} - ₹42 = ₹${change}</span> balance returned.`;
}

// Simulator 6: Triangle Magic Sums
function setMagicTriangle(target) {
    playClickSfx();
    const top = document.getElementById('nodeTop');
    const left = document.getElementById('nodeLeft');
    const right = document.getElementById('nodeRight');
    const mLeft = document.getElementById('nodeMidLeft');
    const mRight = document.getElementById('nodeMidRight');
    const mBot = document.getElementById('nodeMidBottom');
    const desc = document.getElementById('magicTriangleDesc');
    if (!top || !left || !right || !mLeft || !mRight || !mBot || !desc) return;

    document.querySelectorAll('.magic-btn').forEach(b => {
        b.className = 'magic-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'magic-btn px-3 py-1.5 rounded-xl bg-pink-600 text-white font-bold text-xs shadow transition';

    if (target === 9) {
        top.innerText = '1'; left.innerText = '2'; right.innerText = '3';
        mLeft.innerText = '6'; mRight.innerText = '5'; mBot.innerText = '4';
        desc.innerHTML = 'Side 1: 1 + 6 + 2 = 9. Side 2: 1 + 5 + 3 = 9. Side 3: 2 + 4 + 3 = <span class="text-pink-400 font-bold">9</span>!';
    } else if (target === 10) {
        top.innerText = '1'; left.innerText = '3'; right.innerText = '5';
        mLeft.innerText = '6'; mRight.innerText = '4'; mBot.innerText = '2';
        desc.innerHTML = 'Side 1: 1 + 6 + 3 = 10. Side 2: 1 + 4 + 5 = 10. Side 3: 3 + 2 + 5 = <span class="text-pink-400 font-bold">10</span>!';
    } else if (target === 12) {
        top.innerText = '4'; left.innerText = '5'; right.innerText = '6';
        mLeft.innerText = '3'; mRight.innerText = '2'; mBot.innerText = '1';
        desc.innerHTML = 'Side 1: 4 + 3 + 5 = 12. Side 2: 4 + 2 + 6 = 12. Side 3: 5 + 1 + 6 = <span class="text-pink-400 font-bold">12</span>!';
    }
}

// Simulator 7: Base Ten Addition
function setBaseTenStep(step) {
    playClickSfx();
    const group = document.getElementById('dienesBlocksGroup');
    const desc = document.getElementById('baseTenDesc');
    if (!group || !desc) return;

    document.querySelectorAll('.dienes-btn').forEach(b => {
        b.className = 'dienes-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'dienes-btn px-3.5 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs shadow transition';

    if (step === 'unbundled') {
        group.innerHTML = `
            <rect x="42" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="57" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
            <rect x="72" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="87" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
            <rect x="110" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="125" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
            <text x="100" y="152" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">4 Tens + 2 Tens = 6 Tens</text>

            <rect x="205" y="55" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="220" y="55" width="12" height="12" fill="#f59e0b" rx="2"/>
            <rect x="235" y="55" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="250" y="55" width="12" height="12" fill="#f59e0b" rx="2"/>
            <rect x="265" y="55" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="280" y="55" width="12" height="12" fill="#f59e0b" rx="2"/>
            <rect x="295" y="55" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="310" y="55" width="12" height="12" fill="#f59e0b" rx="2"/>
            <rect x="205" y="75" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="220" y="75" width="12" height="12" fill="#f59e0b" rx="2"/>
            <rect x="235" y="75" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="250" y="75" width="12" height="12" fill="#f59e0b" rx="2"/>
            <rect x="265" y="75" width="12" height="12" fill="#f59e0b" rx="2"/><rect x="280" y="75" width="12" height="12" fill="#f59e0b" rx="2"/>
            <text x="260" y="152" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">8 + 6 = 14 Ones</text>
        `;
        desc.innerHTML = 'Combining 8 Ones and 6 Ones produces <span class="text-amber-400 font-bold">14 Ones</span>, which exceeds 9 and must be regrouped!';
    } else {
        group.innerHTML = `
            <rect x="42" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="57" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
            <rect x="72" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="87" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
            <rect x="102" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="117" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
            <rect x="132" y="55" width="10" height="85" fill="#10b981" rx="2" stroke="#34d399" stroke-width="1"/>
            <text x="100" y="152" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">7 Tens = 70</text>

            <rect x="225" y="65" width="14" height="14" fill="#f59e0b" rx="2"/><rect x="250" y="65" width="14" height="14" fill="#f59e0b" rx="2"/>
            <rect x="225" y="90" width="14" height="14" fill="#f59e0b" rx="2"/><rect x="250" y="90" width="14" height="14" fill="#f59e0b" rx="2"/>
            <text x="260" y="152" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">4 Ones = 4</text>
        `;
        desc.innerHTML = '10 of the 14 single cubes bundle into <span class="text-emerald-400 font-bold">1 new Ten rod</span>, leaving 4 single cubes. Total = <span class="text-teal-400 font-bold">74</span>.';
    }
}

// Simulator 8: Field Trip Attendance Addition
function setAdditionProblem(prob) {
    playClickSfx();
    const group = document.getElementById('colAddTextGroup');
    const desc = document.getElementById('colAddDesc');
    if (!group || !desc) return;

    document.querySelectorAll('.add-prob-btn').forEach(b => {
        b.className = 'add-prob-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'add-prob-btn px-3 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow transition';

    if (prob === 'teachers') {
        group.innerHTML = `
            <text x="175" y="40" fill="#f59e0b" font-size="12" font-weight="black" text-anchor="middle">¹</text>
            <text x="145" y="65" fill="#94a3b8" font-size="16" font-weight="bold">T</text>
            <text x="185" y="65" fill="#94a3b8" font-size="16" font-weight="bold">O</text>
            <text x="145" y="90" fill="#ffffff" font-size="18" font-weight="bold">2</text>
            <text x="185" y="90" fill="#ffffff" font-size="18" font-weight="bold">4</text>
            <text x="115" y="115" fill="#38bdf8" font-size="18" font-weight="black">+</text>
            <text x="145" y="115" fill="#ffffff" font-size="18" font-weight="bold">2</text>
            <text x="185" y="115" fill="#ffffff" font-size="18" font-weight="bold">8</text>
            <line x1="110" y1="125" x2="210" y2="125" stroke="#64748b" stroke-width="2"/>
            <text x="145" y="148" fill="#34d399" font-size="20" font-weight="black">5</text>
            <text x="185" y="148" fill="#34d399" font-size="20" font-weight="black">2</text>
        `;
        desc.innerHTML = 'Ones: 4 + 8 = 12 (write 2, carry 1). Tens: 1 + 2 + 2 = <span class="text-blue-400 font-bold">5 Tens</span>. Total = <span class="text-emerald-400 font-bold">52 Staff</span>.';
    } else {
        group.innerHTML = `
            <text x="145" y="40" fill="#f59e0b" font-size="11" font-weight="black" text-anchor="middle">¹</text>
            <text x="175" y="40" fill="#f59e0b" font-size="11" font-weight="black" text-anchor="middle">¹</text>
            <text x="115" y="65" fill="#94a3b8" font-size="14" font-weight="bold">H</text>
            <text x="145" y="65" fill="#94a3b8" font-size="14" font-weight="bold">T</text>
            <text x="175" y="65" fill="#94a3b8" font-size="14" font-weight="bold">O</text>
            <text x="115" y="90" fill="#ffffff" font-size="17" font-weight="bold">4</text>
            <text x="145" y="90" fill="#ffffff" font-size="17" font-weight="bold">3</text>
            <text x="175" y="90" fill="#ffffff" font-size="17" font-weight="bold">8</text>
            <text x="90" y="115" fill="#38bdf8" font-size="17" font-weight="black">+</text>
            <text x="115" y="115" fill="#ffffff" font-size="17" font-weight="bold">4</text>
            <text x="145" y="115" fill="#ffffff" font-size="17" font-weight="bold">7</text>
            <text x="175" y="115" fill="#ffffff" font-size="17" font-weight="bold">6</text>
            <line x1="85" y1="125" x2="200" y2="125" stroke="#64748b" stroke-width="2"/>
            <text x="115" y="148" fill="#34d399" font-size="19" font-weight="black">9</text>
            <text x="145" y="148" fill="#34d399" font-size="19" font-weight="black">1</text>
            <text x="175" y="148" fill="#34d399" font-size="19" font-weight="black">4</text>
        `;
        desc.innerHTML = '8+6=14 (carry 1); 1+3+7=11 (carry 1); 1+4+4=9 Hundreds -> <span class="text-emerald-400 font-bold">914 Students Total</span>.';
    }
}

// Simulator 9: Traditional Snack Expenses
function setSnackExpenseMode(mode) {
    playClickSfx();
    const icon = document.getElementById('snackIcon');
    const label = document.getElementById('snackLabel');
    const subLabel = document.getElementById('snackSubLabel');
    const math = document.getElementById('snackMathGroup');
    const desc = document.getElementById('snackExpenseDesc');
    if (!icon || !label || !subLabel || !math || !desc) return;

    document.querySelectorAll('.snack-btn').forEach(b => {
        b.className = 'snack-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'snack-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';

    if (mode === 'pusaw') {
        icon.innerText = '🥮';
        label.innerText = 'Khasi Red Rice Cake';
        subLabel.innerText = '₹38 Cake + ₹16 Tea';
        math.innerHTML = `
            <text x="250" y="50" fill="#f59e0b" font-size="12" font-weight="black" text-anchor="middle">¹ (carry)</text>
            <text x="225" y="75" fill="#ffffff" font-size="16" font-weight="bold">38</text>
            <text x="200" y="98" fill="#38bdf8" font-size="16" font-weight="black">+</text>
            <text x="225" y="98" fill="#ffffff" font-size="16" font-weight="bold">16</text>
            <line x1="200" y1="108" x2="270" y2="108" stroke="#64748b" stroke-width="2"/>
            <text x="225" y="132" fill="#34d399" font-size="19" font-weight="black">₹54</text>
        `;
        desc.innerHTML = '8 + 6 = 14 (write 4, carry 1 Ten); 1 + 3 + 1 = 5 Tens. Total bill: <span class="text-emerald-400 font-bold">₹54</span>.';
    } else {
        icon.innerText = '🪙';
        label.innerText = 'Piggy Bank Savings';
        subLabel.innerText = '₹185 Jar + ₹125 Pouch';
        math.innerHTML = `
            <text x="235" y="48" fill="#f59e0b" font-size="10" font-weight="black">¹</text>
            <text x="255" y="48" fill="#f59e0b" font-size="10" font-weight="black">¹</text>
            <text x="215" y="75" fill="#ffffff" font-size="16" font-weight="bold">185</text>
            <text x="195" y="98" fill="#38bdf8" font-size="16" font-weight="black">+</text>
            <text x="215" y="98" fill="#ffffff" font-size="16" font-weight="bold">125</text>
            <line x1="195" y1="108" x2="280" y2="108" stroke="#64748b" stroke-width="2"/>
            <text x="215" y="132" fill="#34d399" font-size="19" font-weight="black">₹310</text>
        `;
        desc.innerHTML = '5+5=10 (carry 1); 1+8+2=11 (carry 1); 1+1+1=3 Hundreds. Total savings: <span class="text-emerald-400 font-bold">₹310</span>.';
    }
}

// Simulator 10: Snack Choice Differences
function setSnackDiffStep(step) {
    playClickSfx();
    const colGroup = document.getElementById('snackDiffColGroup');
    const desc = document.getElementById('snackDiffDesc');
    if (!colGroup || !desc) return;

    document.querySelectorAll('.diff-btn').forEach(b => {
        b.className = 'diff-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'diff-btn px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs shadow transition';

    if (step === 'problem') {
        colGroup.innerHTML = `
            <text x="250" y="68" fill="#ffffff" font-size="18" font-weight="bold">8</text>
            <text x="280" y="68" fill="#ffffff" font-size="18" font-weight="bold">3</text>
            <text x="232" y="92" fill="#ef4444" font-size="18" font-weight="black">-</text>
            <text x="250" y="92" fill="#ffffff" font-size="18" font-weight="bold">4</text>
            <text x="280" y="92" fill="#ffffff" font-size="18" font-weight="bold">6</text>
            <line x1="230" y1="104" x2="310" y2="104" stroke="#64748b" stroke-width="2"/>
            <text x="260" y="130" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">3 < 6 (Need Borrow)</text>
        `;
        desc.innerHTML = 'Cannot subtract 6 from 3. We must borrow 1 Ten from the 8 Tens to make 13 Ones.';
    } else {
        colGroup.innerHTML = `
            <text x="250" y="42" fill="#f59e0b" font-size="11" font-weight="extrabold">⁷</text>
            <text x="280" y="42" fill="#f59e0b" font-size="11" font-weight="extrabold">¹³</text>
            <text x="250" y="68" fill="#ffffff" font-size="18" font-weight="bold">8</text>
            <text x="280" y="68" fill="#ffffff" font-size="18" font-weight="bold">3</text>
            <text x="232" y="92" fill="#ef4444" font-size="18" font-weight="black">-</text>
            <text x="250" y="92" fill="#ffffff" font-size="18" font-weight="bold">4</text>
            <text x="280" y="92" fill="#ffffff" font-size="18" font-weight="bold">6</text>
            <line x1="230" y1="104" x2="310" y2="104" stroke="#64748b" stroke-width="2"/>
            <text x="250" y="130" fill="#34d399" font-size="20" font-weight="black">3</text>
            <text x="280" y="130" fill="#34d399" font-size="20" font-weight="black">7</text>
        `;
        desc.innerHTML = '13 - 6 = 7 Ones; 7 - 4 = 3 Tens. Difference = <span class="text-amber-400 font-bold">37 students</span>.';
    }
}

// Simulator 11: Regrouping In Subtraction
function setSubStep(step) {
    playClickSfx();
    const textGroup = document.getElementById('colSubTextGroup');
    const desc = document.getElementById('colSubDesc');
    if (!textGroup || !desc) return;

    document.querySelectorAll('.substep-btn').forEach(b => {
        b.className = 'substep-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'substep-btn px-2.5 py-1.5 rounded-xl bg-red-500 text-white font-bold text-xs shadow transition';

    if (step === 1) {
        textGroup.innerHTML = `
            <text x="135" y="38" fill="#64748b" font-size="11" font-weight="bold">H</text>
            <text x="175" y="38" fill="#64748b" font-size="11" font-weight="bold">T</text>
            <text x="215" y="38" fill="#64748b" font-size="11" font-weight="bold">O</text>
            <text x="175" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹</text>
            <text x="215" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹⁴</text>
            <text x="135" y="80" fill="#ffffff" font-size="18" font-weight="bold">3</text>
            <text x="175" y="80" fill="#ffffff" font-size="18" font-weight="bold">2</text>
            <text x="215" y="80" fill="#ffffff" font-size="18" font-weight="bold">4</text>
            <text x="105" y="105" fill="#ef4444" font-size="18" font-weight="black">-</text>
            <text x="135" y="105" fill="#ffffff" font-size="18" font-weight="bold">1</text>
            <text x="175" y="105" fill="#ffffff" font-size="18" font-weight="bold">7</text>
            <text x="215" y="105" fill="#ffffff" font-size="18" font-weight="bold">6</text>
            <line x1="105" y1="116" x2="245" y2="116" stroke="#64748b" stroke-width="2"/>
            <text x="215" y="142" fill="#34d399" font-size="20" font-weight="black">8</text>
        `;
        desc.innerHTML = 'Step 1: 4 cannot subtract 6. Borrow 1 Ten -> 14 - 6 = <span class="text-emerald-400 font-bold">8 Ones</span>.';
    } else if (step === 2) {
        textGroup.innerHTML = `
            <text x="135" y="38" fill="#64748b" font-size="11" font-weight="bold">H</text>
            <text x="175" y="38" fill="#64748b" font-size="11" font-weight="bold">T</text>
            <text x="215" y="38" fill="#64748b" font-size="11" font-weight="bold">O</text>
            <text x="135" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">²</text>
            <text x="175" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹¹</text>
            <text x="215" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹⁴</text>
            <text x="135" y="80" fill="#ffffff" font-size="18" font-weight="bold">3</text>
            <text x="175" y="80" fill="#ffffff" font-size="18" font-weight="bold">2</text>
            <text x="215" y="80" fill="#ffffff" font-size="18" font-weight="bold">4</text>
            <text x="105" y="105" fill="#ef4444" font-size="18" font-weight="black">-</text>
            <text x="135" y="105" fill="#ffffff" font-size="18" font-weight="bold">1</text>
            <text x="175" y="105" fill="#ffffff" font-size="18" font-weight="bold">7</text>
            <text x="215" y="105" fill="#ffffff" font-size="18" font-weight="bold">6</text>
            <line x1="105" y1="116" x2="245" y2="116" stroke="#64748b" stroke-width="2"/>
            <text x="175" y="142" fill="#34d399" font-size="20" font-weight="black">4</text>
            <text x="215" y="142" fill="#34d399" font-size="20" font-weight="black">8</text>
        `;
        desc.innerHTML = 'Step 2: 1 Ten cannot subtract 7 Tens. Borrow 1 Hundred -> 11 - 7 = <span class="text-emerald-400 font-bold">4 Tens</span>.';
    } else {
        textGroup.innerHTML = `
            <text x="135" y="38" fill="#64748b" font-size="11" font-weight="bold">H</text>
            <text x="175" y="38" fill="#64748b" font-size="11" font-weight="bold">T</text>
            <text x="215" y="38" fill="#64748b" font-size="11" font-weight="bold">O</text>
            <text x="135" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">²</text>
            <text x="175" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹¹</text>
            <text x="215" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹⁴</text>
            <text x="135" y="80" fill="#ffffff" font-size="18" font-weight="bold">3</text>
            <text x="175" y="80" fill="#ffffff" font-size="18" font-weight="bold">2</text>
            <text x="215" y="80" fill="#ffffff" font-size="18" font-weight="bold">4</text>
            <text x="105" y="105" fill="#ef4444" font-size="18" font-weight="black">-</text>
            <text x="135" y="105" fill="#ffffff" font-size="18" font-weight="bold">1</text>
            <text x="175" y="105" fill="#ffffff" font-size="18" font-weight="bold">7</text>
            <text x="215" y="105" fill="#ffffff" font-size="18" font-weight="bold">6</text>
            <line x1="105" y1="116" x2="245" y2="116" stroke="#64748b" stroke-width="2"/>
            <text x="135" y="142" fill="#34d399" font-size="20" font-weight="black">1</text>
            <text x="175" y="142" fill="#34d399" font-size="20" font-weight="black">4</text>
            <text x="215" y="142" fill="#34d399" font-size="20" font-weight="black">8</text>
        `;
        desc.innerHTML = 'Hundreds: 2 - 1 = 1 Hundred. Complete difference = <span class="text-red-400 font-bold">148</span>.';
    }
}

// Simulator 12: Travel Spend Balances
function setSpendMode(mode) {
    playClickSfx();
    const init = document.getElementById('spendInitVal');
    const rem = document.getElementById('spendRemVal');
    const res = document.getElementById('spendResultVal');
    const desc = document.getElementById('spendDesc');
    if (!init || !rem || !res || !desc) return;

    document.querySelectorAll('.spend-btn').forEach(b => {
        b.className = 'spend-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'spend-btn px-3 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow transition';

    if (mode === 'wallet') {
        init.innerText = '₹310';
        rem.innerText = '₹179';
        res.innerText = '₹131';
        desc.innerHTML = 'Initial ₹310 - Remaining ₹179 = <span class="text-purple-400 font-bold">₹131 Total Money Spent</span>.';
    } else {
        init.innerText = '520 kg';
        rem.innerText = '415 kg';
        res.innerText = '105 kg';
        desc.innerHTML = 'Last year 520 kg - This year 415 kg = <span class="text-purple-400 font-bold">105 kg Harvest Decrease</span>.';
    }
}

// Simulator 13: Train Passenger Tracking
function setTrainStation(st) {
    playClickSfx();
    const train = document.getElementById('trainGraphic');
    const stName = document.getElementById('trainStationName');
    const occ = document.getElementById('trainOccupancyVal');
    const detail = document.getElementById('trainFlowDetail');
    const desc = document.getElementById('trainTrackDesc');
    if (!train || !stName || !occ || !detail || !desc) return;

    document.querySelectorAll('.st-btn').forEach(b => {
        b.className = 'st-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'st-btn px-2.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition';

    if (st === 1) {
        train.setAttribute('transform', 'translate(30, 0)');
        stName.innerText = 'Departure: New Delhi';
        occ.innerText = '642 Passengers';
        detail.innerText = 'Initial departures count';
        desc.innerHTML = 'Departing New Delhi: <span class="text-cyan-400 font-bold">642 passengers</span> on board.';
    } else if (st === 2) {
        train.setAttribute('transform', 'translate(100, 0)');
        stName.innerText = 'Junction 1: Dadri';
        occ.innerText = '671 Passengers';
        detail.innerText = 'Alight: 85 | Board: 114';
        desc.innerHTML = 'Dadri Junction: 642 - 85 = 557; 557 + 114 = <span class="text-cyan-400 font-bold">671 passengers</span>.';
    } else if (st === 3) {
        train.setAttribute('transform', 'translate(170, 0)');
        stName.innerText = 'Junction 2: Ghaziabad';
        occ.innerText = '637 Passengers';
        detail.innerText = 'Alight: 96 | Board: 62';
        desc.innerHTML = 'Ghaziabad Junction: 671 - 96 = 575; 575 + 62 = <span class="text-cyan-400 font-bold">637 passengers</span>.';
    } else {
        train.setAttribute('transform', 'translate(240, 0)');
        stName.innerText = 'Arrival: Aligarh';
        occ.innerText = '592 Passengers';
        detail.innerText = 'Alight: 45 | Final terminal';
        desc.innerHTML = 'Aligarh Terminal: 637 - 45 = <span class="text-cyan-400 font-bold">592 passengers</span> arriving.';
    }
}

// Simulator 14: Mental Math Shortcuts
function setMentalShortcut(strat) {
    playClickSfx();
    const orig = document.getElementById('mentalOriginalText');
    const s1 = document.getElementById('mentalStep1');
    const s2 = document.getElementById('mentalStep2');
    const desc = document.getElementById('mentalDesc');
    if (!orig || !s1 || !s2 || !desc) return;

    document.querySelectorAll('.short-btn').forEach(b => {
        b.className = 'short-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'short-btn px-3 py-1.5 rounded-xl bg-yellow-500 text-slate-950 font-bold text-xs shadow transition';

    if (strat === 'add99') {
        orig.innerText = 'Problem: 356 + 99';
        s1.innerText = 'Step 1: 356 + 100 = 456';
        s2.innerText = 'Step 2: 456 - 1 = 455!';
        desc.innerHTML = '99 is (100 - 1). Add 100 to get 456, then subtract 1 = <span class="text-yellow-400 font-bold">455</span>!';
    } else if (strat === 'sub49') {
        orig.innerText = 'Problem: 280 - 49';
        s1.innerText = 'Step 1: 280 - 50 = 230';
        s2.innerText = 'Step 2: 230 + 1 = 231!';
        desc.innerHTML = '49 is (50 - 1). Subtract 50 to get 230, then add back 1 = <span class="text-yellow-400 font-bold">231</span>!';
    } else {
        orig.innerText = 'Problem: 45 + 32';
        s1.innerText = 'Tens: 40 + 30 = 70';
        s2.innerText = 'Ones: 5 + 2 = 7 -> 77!';
        desc.innerHTML = 'Expanded strategy: Add Tens (40+30=70) and Ones (5+2=7) = <span class="text-yellow-400 font-bold">77</span>!';
    }
}

// Simulator 15: Target Number Decompositions
function setTargetDecomp(eq) {
    playClickSfx();
    const central = document.getElementById('targetCentralNum');
    const pA = document.getElementById('partAVal');
    const pB = document.getElementById('partBVal');
    const op = document.getElementById('decompOp');
    const desc = document.getElementById('targetDecompDesc');
    if (!central || !pA || !pB || !op || !desc) return;

    document.querySelectorAll('.decomp-btn').forEach(b => {
        b.className = 'decomp-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'decomp-btn px-2.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow transition';

    if (eq === 'sum856_a') {
        central.innerText = '856'; pA.innerText = '500'; pB.innerText = '356'; op.innerText = '+';
        desc.innerHTML = '500 + 356 = <span class="text-blue-400 font-bold">856</span>. Clean place value decomposition!';
    } else if (eq === 'sum856_b') {
        central.innerText = '856'; pA.innerText = '700'; pB.innerText = '156'; op.innerText = '+';
        desc.innerHTML = '700 + 156 = <span class="text-blue-400 font-bold">856</span>. Multiple addend pairs match the target sum!';
    } else if (eq === 'diff563_a') {
        central.innerText = '563'; pA.innerText = '763'; pB.innerText = '200'; op.innerText = '-';
        desc.innerHTML = '763 - 200 = <span class="text-blue-400 font-bold">563</span>. Subtraction target difference!';
    } else {
        central.innerText = '563'; pA.innerText = '863'; pB.innerText = '300'; op.innerText = '-';
        desc.innerHTML = '863 - 300 = <span class="text-blue-400 font-bold">563</span>. Invariant difference principle!';
    }
}

// Simulator 16: Number Pair Hunt Grid
function setGridHunt(mode) {
    playClickSfx();
    const title = document.getElementById('gridReadoutTitle');
    const nums = document.getElementById('gridReadoutNums');
    const res = document.getElementById('gridReadoutResult');
    const tag = document.getElementById('gridReadoutTag');
    const desc = document.getElementById('gridHuntDesc');
    const c87 = document.getElementById('cell87');
    const c94 = document.getElementById('cell94');
    const c52 = document.getElementById('cell52');
    const c55 = document.getElementById('cell55');
    if (!title || !nums || !res || !tag || !desc) return;

    document.querySelectorAll('.hunt-btn').forEach(b => {
        b.className = 'hunt-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'hunt-btn px-2.5 py-1.5 rounded-xl bg-green-500 text-slate-950 font-bold text-xs shadow transition';

    if (c87) c87.setAttribute('fill', '#1e293b');
    if (c94) c94.setAttribute('fill', '#1e293b');
    if (c52) c52.setAttribute('fill', '#1e293b');
    if (c55) c55.setAttribute('fill', '#1e293b');

    if (mode === 'max_sum') {
        if (c87) c87.setAttribute('fill', '#15803d');
        if (c94) c94.setAttribute('fill', '#15803d');
        title.innerText = 'Adjacent Pair';
        nums.innerText = '87 + 94';
        res.innerText = '= 181';
        tag.innerText = 'Greatest Adjacent Sum';
        desc.innerHTML = 'Neighboring cells 87 and 94 yield the <span class="text-green-400 font-bold">greatest sum = 181</span>!';
    } else if (mode === 'min_diff') {
        if (c52) c52.setAttribute('fill', '#0284c7');
        if (c55) c55.setAttribute('fill', '#0284c7');
        title.innerText = 'Adjacent Pair';
        nums.innerText = '55 - 52';
        res.innerText = '= 3';
        tag.innerText = 'Smallest Adjacent Diff';
        desc.innerHTML = 'Neighboring cells 55 and 52 yield the <span class="text-cyan-400 font-bold">smallest difference = 3</span>!';
    } else {
        title.innerText = 'Missing Digit';
        nums.innerText = '3 _ 5 + 142';
        res.innerText = 'Digit = 5';
        tag.innerText = '355 + 142 = 497';
        desc.innerHTML = 'In Tens place: 9 - 4 = <span class="text-green-400 font-bold">5</span> (Equation: 355 + 142 = 497).';
    }
}

// Initializer helper for each slide
function initSlideSimulator(slideId) {
    if (slideId === 1) setTripMetric('time');
    else if (slideId === 2) selectCartItem('beans');
    else if (slideId === 3) setBasketCombo('standard');
    else if (slideId === 4) setBalanceScenario(64, 100);
    else if (slideId === 5) setOrangeTender(50);
    else if (slideId === 6) setMagicTriangle(9);
    else if (slideId === 7) setBaseTenStep('bundled');
    else if (slideId === 8) setAdditionProblem('teachers');
    else if (slideId === 9) setSnackExpenseMode('pusaw');
    else if (slideId === 10) setSnackDiffStep('borrowed');
    else if (slideId === 11) setSubStep(3);
    else if (slideId === 12) setSpendMode('wallet');
    else if (slideId === 13) setTrainStation(1);
    else if (slideId === 14) setMentalShortcut('add99');
    else if (slideId === 15) setTargetDecomp('sum856_a');
    else if (slideId === 16) setGridHunt('max_sum');
}

// Document ready bootstrap
document.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
});
'''

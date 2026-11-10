
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
        
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.05);
        
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.06);
        
        osc.start(now);
        osc.stop(now + 0.06);
    } catch(e) {}
}

// ============================================================================
// Indian English Male Teacher Voice Engine
// ============================================================================
function selectIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;
    
    const femaleTerms = ['female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera', 'kavya'];
    const malePreferred = ['microsoft prabhat', 'rishi', 'microsoft ravi', 'pradeep', 'madhav', 'karan', 'mohan', 'google uk english male', 'microsoft david', 'microsoft mark', 'alex'];
    
    for (const pref of malePreferred) {
        const found = voices.find(v => {
            const name = v.name.toLowerCase();
            const lang = v.lang.toLowerCase();
            const isFemale = femaleTerms.some(f => name.includes(f));
            return !isFemale && (name.includes(pref) || (lang.includes('en-in') && name.includes(pref)));
        });
        if (found) return found;
    }
    
    const anyIndian = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.includes('en-in');
    });
    if (anyIndian) return anyIndian;
    
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
    if (!slide || !slide.speech || slide.speech.trim() === '') {
        return;
    }
    
    window.speechSynthesis.cancel();
    clearInterval(keepAliveTimer);
    
    currentUtterance = new SpeechSynthesisUtterance(slide.speech);
    currentUtterance.pitch = 0.85;
    currentUtterance.rate = 0.94;
    
    const voices = window.speechSynthesis.getVoices();
    const chosenVoice = selectIndianMaleVoice(voices);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    
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

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (playing) {
        btn.classList.add('bg-rose-600', 'text-white', 'animate-pulse');
        btn.classList.remove('bg-indigo-600');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8 7a1 1 0 00-1 1v4a1 1 0 001 1h4a1 1 0 001-1V8a1 1 0 00-1-1H8z" clip-rule="evenodd"></path></svg>
            Stop Audio
        `;
    } else {
        btn.classList.remove('bg-rose-600', 'animate-pulse');
        btn.classList.add('bg-indigo-600', 'text-white');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
            Audio Lecture
        `;
    }
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

    // Audio button visibility for non-speech slides (slides 17 to 20)
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.classList.add('hidden');
        } else {
            audioBtn.classList.remove('hidden');
        }
    }
    
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

// ============================================================================
// Quiz Validation & Solution Modals
// ============================================================================
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
// Simulator 1: Leap Year Timeline Explorer
// ============================================================================
function updateLeapSim(year) {
    const yr = parseInt(year);
    const yrVal = document.getElementById('leap-year-val');
    const badge = document.getElementById('leap-badge');
    const divMath = document.getElementById('leap-div-math');
    const remText = document.getElementById('leap-rem-text');
    const febDays = document.getElementById('leap-feb-days');
    const febSub = document.getElementById('leap-feb-sub');
    const totalDays = document.getElementById('leap-total-days');
    const bdayStatus = document.getElementById('leap-bday-status');
    const slider = document.getElementById('leap-slider');
    
    if (slider) slider.value = yr;
    if (yrVal) yrVal.innerText = yr;
    
    const isLeap = (yr % 4 === 0) && (yr % 100 !== 0 || yr % 400 === 0);
    const quotient = Math.floor(yr / 4);
    const remainder = yr % 4;
    
    if (divMath) divMath.innerText = `${yr} ÷ 4 = ${quotient}`;
    
    if (isLeap) {
        if (badge) {
            badge.className = 'px-2.5 py-1 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            badge.innerText = 'LEAP YEAR (366 Days)';
        }
        if (remText) {
            remText.className = 'text-[10px] text-emerald-400 font-medium';
            remText.innerText = 'Remainder 0 (Divisible)';
        }
        if (febDays) febDays.innerText = '29 Days';
        if (febSub) febSub.innerText = '+1 Leap Day Added';
        if (totalDays) totalDays.innerText = '366 Days';
        if (bdayStatus) {
            bdayStatus.className = 'text-emerald-300 font-bold text-xs mt-1';
            bdayStatus.innerText = 'Official Date!';
        }
    } else {
        if (badge) {
            badge.className = 'px-2.5 py-1 rounded-full text-[11px] font-bold bg-slate-700/50 text-slate-300 border border-slate-600';
            badge.innerText = 'ORDINARY YEAR (365 Days)';
        }
        if (remText) {
            remText.className = 'text-[10px] text-amber-400 font-medium';
            remText.innerText = `Remainder ${remainder} (Not Divisible)`;
        }
        if (febDays) febDays.innerText = '28 Days';
        if (febSub) febSub.innerText = 'Standard Month';
        if (totalDays) totalDays.innerText = '365 Days';
        if (bdayStatus) {
            bdayStatus.className = 'text-amber-300 font-bold text-xs mt-1';
            bdayStatus.innerText = 'Observed March 1st';
        }
    }
}

// ============================================================================
// Simulator 2: Universal Date Formats Math
// ============================================================================
const monthNames = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

function populateDateSelectors() {
    const ddSelect = document.getElementById('date-dd');
    if (!ddSelect) return;
    ddSelect.innerHTML = '';
    for (let i = 1; i <= 31; i++) {
        const val = i < 10 ? '0' + i : '' + i;
        const opt = document.createElement('option');
        opt.value = i;
        opt.innerText = val;
        if (i === 15) opt.selected = true;
        ddSelect.appendChild(opt);
    }
}

function renderDateFormatSim() {
    const dd = parseInt(document.getElementById('date-dd').value);
    const mm = parseInt(document.getElementById('date-mm').value);
    const yyyy = parseInt(document.getElementById('date-yyyy').value);
    
    const ddStr = dd < 10 ? '0' + dd : '' + dd;
    const mmStr = mm < 10 ? '0' + mm : '' + mm;
    const yyyyStr = '' + yyyy;
    
    const outNum = document.getElementById('date-out-num');
    const outWords = document.getElementById('date-out-words');
    const outDd = document.getElementById('out-dd');
    const outMm = document.getElementById('out-mm');
    const outYy = document.getElementById('out-yy');
    
    if (outNum) outNum.innerText = `${ddStr}/${mmStr}/${yyyyStr}`;
    if (outWords) outWords.innerText = `${dd} ${monthNames[mm]} ${yyyy}`;
    if (outDd) outDd.innerText = ddStr;
    if (outMm) outMm.innerText = mmStr;
    if (outYy) outYy.innerText = yyyyStr;
}

function setDatePreset(d, m, y, context) {
    const ddEl = document.getElementById('date-dd');
    const mmEl = document.getElementById('date-mm');
    const yyEl = document.getElementById('date-yyyy');
    const noteEl = document.getElementById('date-context-note');
    
    if (ddEl) ddEl.value = d;
    if (mmEl) mmEl.value = m;
    if (yyEl) yyEl.value = y;
    if (noteEl) noteEl.innerText = context;
    renderDateFormatSim();
}

// ============================================================================
// Simulator 3: Packaging Expiry Dates Inspector
// ============================================================================
const expiryCatalog = {
    biscuit: {
        name: 'Nutri-Bake Digestive Biscuits',
        mfg: '10/01/2024',
        mfgDate: new Date(2024, 0, 10),
        lifeStr: '6 Months from MFG',
        exp: '10/07/2024',
        expDate: new Date(2024, 6, 10),
        expl: 'Manufacturing Month: <strong>January (01)</strong>. Adding 6 months: 01 + 6 = <strong>July (07)</strong>. Expiry Date = 10 July 2024.'
    },
    milk: {
        name: 'Pure Dairy Toned Milk Pouch',
        mfg: '12/03/2024',
        mfgDate: new Date(2024, 2, 12),
        lifeStr: '3 Days from Packing',
        exp: '15/03/2024',
        expDate: new Date(2024, 2, 15),
        expl: 'Manufacturing Day: <strong>12 March</strong>. Adding 3 days: 12 + 3 = <strong>15 March</strong>. Fresh dairy spoils quickly!'
    },
    jam: {
        name: 'Mixed Fruit Preserve Jam',
        mfg: '01/02/2024',
        mfgDate: new Date(2024, 1, 1),
        lifeStr: '12 Months (1 Year)',
        exp: '01/02/2025',
        expDate: new Date(2025, 1, 1),
        expl: 'Manufacturing Date: <strong>1 February 2024</strong>. Adding 12 months (1 year): <strong>1 February 2025</strong>.'
    },
    syrup: {
        name: 'Herbal Cough Syrup Bottle',
        mfg: '10/2023',
        mfgDate: new Date(2023, 9, 1),
        lifeStr: '24 Months (2 Years)',
        exp: '10/2025',
        expDate: new Date(2025, 9, 31),
        expl: 'Manufacturing: <strong>October 2023</strong>. Adding 2 years: 2023 + 2 = <strong>October 2025</strong>.'
    }
};

let currentExpKey = 'biscuit';

function selectExpiryProduct(key) {
    currentExpKey = key;
    ['biscuit', 'milk', 'jam', 'syrup'].forEach(k => {
        const tab = document.getElementById(`exp-tab-${k}`);
        if (!tab) return;
        if (k === key) {
            tab.className = 'p-2 rounded-xl border bg-amber-600/20 border-amber-500 text-amber-300 font-bold text-center transition';
        } else {
            tab.className = 'p-2 rounded-xl border border-slate-800 bg-slate-950/60 text-slate-400 text-center transition hover:text-white';
        }
    });
    
    const prod = expiryCatalog[key];
    document.getElementById('exp-prod-name').innerText = prod.name;
    document.getElementById('exp-mfg-str').innerText = prod.mfg;
    document.getElementById('exp-life-str').innerText = prod.lifeStr;
    document.getElementById('exp-target-str').innerText = prod.exp;
    auditExpiryProduct();
}

function auditExpiryProduct() {
    const prod = expiryCatalog[currentExpKey];
    const inp = document.getElementById('exp-inspect-date');
    const pill = document.getElementById('exp-status-pill');
    const expl = document.getElementById('exp-calc-expl');
    
    if (!inp || !pill || !expl) return;
    const inspectDate = new Date(inp.value);
    
    if (inspectDate <= prod.expDate) {
        pill.className = 'px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        pill.innerText = 'SAFE TO EAT (Fresh)';
        expl.innerHTML = `${prod.expl} Inspection date is prior to expiration, so this food item is completely fresh and safe to eat.`;
    } else {
        pill.className = 'px-3 py-1 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        pill.innerText = 'EXPIRED! DO NOT CONSUME';
        expl.innerHTML = `${prod.expl} <span class='text-rose-400 font-bold'>Warning:</span> Inspection date is past the expiry date. Consuming expired items carries health risks.`;
    }
}

// ============================================================================
// Simulator 4: Community Lunar Calendars
// ============================================================================
function updateLunarSim(day) {
    const d = parseInt(day);
    const slider = document.getElementById('lunar-slider');
    const dayVal = document.getElementById('lunar-day-val');
    const pctVal = document.getElementById('lunar-cycle-pct');
    const pakshaTag = document.getElementById('lunar-paksha-tag');
    const tithiTitle = document.getElementById('lunar-tithi-title');
    const descText = document.getElementById('lunar-desc-text');
    const moonPath = document.getElementById('moon-phase-path');
    
    if (slider) slider.value = d;
    if (dayVal) dayVal.innerText = d;
    
    let pct = 0;
    if (d <= 15) {
        pct = Math.round(((d - 1) / 14) * 100);
    } else {
        pct = Math.round(((30 - d) / 15) * 100);
    }
    if (pctVal) pctVal.innerText = `${pct}% Illuminated`;
    
    // Moon phase visual path calculation
    if (moonPath) {
        if (d === 1 || d === 30) {
            moonPath.setAttribute('d', 'M 50 50 Z'); // Invisible
        } else if (d === 15) {
            moonPath.setAttribute('d', 'M 50 5 A 45 45 0 0 1 50 95 A 45 45 0 0 1 50 5'); // Full circle
        } else if (d < 15) {
            // Waxing: right side lit
            const k = (d / 15) * 2 - 1; // -1 to 1
            const curve = 45 * k;
            moonPath.setAttribute('d', `M 50 5 A 45 45 0 0 1 50 95 A ${Math.abs(curve)} 45 0 0 ${curve > 0 ? 0 : 1} 50 5`);
        } else {
            // Waning: left side lit
            const k = ((d - 15) / 15) * 2 - 1;
            const curve = 45 * k;
            moonPath.setAttribute('d', `M 50 5 A 45 45 0 0 0 50 95 A ${Math.abs(curve)} 45 0 0 ${curve > 0 ? 1 : 0} 50 5`);
        }
    }
    
    if (d <= 15) {
        if (pakshaTag) {
            pakshaTag.className = 'text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30';
            pakshaTag.innerText = 'Shukla Paksha (Waxing Bright Fortnight)';
        }
        if (d === 1) {
            if (tithiTitle) tithiTitle.innerText = 'Tithi 1: Pratipada (New Moon Onset)';
            if (descText) descText.innerText = 'The moon begins its waxing journey. A faint silver crescent emerges in the western sky.';
        } else if (d === 15) {
            if (tithiTitle) tithiTitle.innerText = 'Tithi 15: Purnima (Full Moon)';
            if (descText) descText.innerText = 'The glowing moon is fully round and luminous. Many Indian festivals like Raksha Bandhan and Guru Purnima fall on Purnima.';
        } else {
            if (tithiTitle) tithiTitle.innerText = `Tithi ${d}: Waxing Moon (${pct}%)`;
            if (descText) descText.innerText = 'The illuminated area expands every single night leading toward the full moon night.';
        }
    } else {
        if (pakshaTag) {
            pakshaTag.className = 'text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
            pakshaTag.innerText = 'Krishna Paksha (Waning Dark Fortnight)';
        }
        if (d === 30) {
            if (tithiTitle) tithiTitle.innerText = 'Tithi 30: Amavasya (New Moon Night)';
            if (descText) descText.innerText = 'The Moon is completely dark from Earth. The night of deep darkness celebrated with lamps on Diwali.';
        } else {
            if (tithiTitle) tithiTitle.innerText = `Tithi ${d}: Waning Moon (${pct}%)`;
            if (descText) descText.innerText = 'The moon shrinks gradually each night, heading towards Amavasya.';
        }
    }
}

// ============================================================================
// Simulator 5: Daily Routine Wheel
// ============================================================================
function renderRoutineSvg() {
    const svg = document.getElementById('routine-svg');
    if (!svg) return;
    
    // Sectors: Sleep 8h (120 deg), Study 6h (90 deg), Play 3h (45 deg), Routine 7h (105 deg)
    const sectors = [
        { hours: 8, color: '#6366f1' }, // Sleep
        { hours: 6, color: '#10b981' }, // Study
        { hours: 3, color: '#f59e0b' }, // Play
        { hours: 7, color: '#f43f5e' }  // Meals/Hobbies
    ];
    
    let currentAngle = 0;
    let pathsHtml = '';
    
    sectors.forEach(s => {
        const sweep = (s.hours / 24) * 360;
        const startRad = (currentAngle * Math.PI) / 180;
        const endRad = ((currentAngle + sweep) * Math.PI) / 180;
        
        const x1 = 100 + 80 * Math.cos(startRad);
        const y1 = 100 + 80 * Math.sin(startRad);
        const x2 = 100 + 80 * Math.cos(endRad);
        const y2 = 100 + 80 * Math.sin(endRad);
        
        const largeArc = sweep > 180 ? 1 : 0;
        const d = `M 100 100 L ${x1} ${y1} A 80 80 0 ${largeArc} 1 ${x2} ${y2} Z`;
        pathsHtml += `<path d="${d}" fill="${s.color}" fill-opacity="0.8" stroke="#0f172a" stroke-width="2"/>`;
        currentAngle += sweep;
    });
    
    // Inner cutout ring
    pathsHtml += '<circle cx="100" cy="100" r="45" fill="#0f172a"/>';
    svg.innerHTML = pathsHtml;
}

// ============================================================================
// Simulator 6: Twelve Hour Clocks
// ============================================================================
function setTwelveHourSim(h, m, meridiem, note) {
    const hourHand = document.getElementById('sim6-hour-hand');
    const minHand = document.getElementById('sim6-min-hand');
    const digTime = document.getElementById('sim6-digital-time');
    const badge = document.getElementById('sim6-meridian-badge');
    const noteEl = document.getElementById('sim6-desc-note');
    const skyBox = document.getElementById('sky-box');
    
    const hAngle = ((h % 12) + m / 60) * 30;
    const mAngle = m * 6;
    
    if (hourHand) {
        hourHand.setAttribute('transform', `rotate(${hAngle} 50 50)`);
    }
    if (minHand) {
        minHand.setAttribute('transform', `rotate(${mAngle} 50 50)`);
    }
    
    const hStr = h < 10 ? '0' + h : '' + h;
    const mStr = m < 10 ? '0' + m : '' + m;
    if (digTime) digTime.innerText = `${hStr}:${mStr} ${meridiem}`;
    
    if (badge) {
        if (meridiem === 'AM') {
            badge.className = 'inline-block px-3 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
            badge.innerText = 'AM (Ante Meridiem — Before Midday)';
        } else {
            badge.className = 'inline-block px-3 py-1 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
            badge.innerText = 'PM (Post Meridiem — After Midday)';
        }
    }
    
    if (noteEl) noteEl.innerText = note;
    
    if (skyBox) {
        if (meridiem === 'AM' && h >= 6 && h <= 11) {
            skyBox.className = 'relative rounded-xl p-5 border border-amber-700/60 overflow-hidden transition-colors duration-700 bg-gradient-to-b from-amber-900 to-indigo-950 flex flex-col sm:flex-row items-center justify-around gap-4';
        } else if (h === 12 && meridiem === 'PM') {
            skyBox.className = 'relative rounded-xl p-5 border border-sky-600 overflow-hidden transition-colors duration-700 bg-gradient-to-b from-sky-800 to-blue-950 flex flex-col sm:flex-row items-center justify-around gap-4';
        } else if (meridiem === 'PM' && h >= 1 && h <= 6) {
            skyBox.className = 'relative rounded-xl p-5 border border-orange-700/60 overflow-hidden transition-colors duration-700 bg-gradient-to-b from-orange-950 to-indigo-950 flex flex-col sm:flex-row items-center justify-around gap-4';
        } else {
            skyBox.className = 'relative rounded-xl p-5 border border-slate-700 overflow-hidden transition-colors duration-700 bg-gradient-to-b from-slate-950 to-indigo-950 flex flex-col sm:flex-row items-center justify-around gap-4';
        }
    }
}

// ============================================================================
// Simulator 7: Digital Clock Formats
// ============================================================================
let convMeridiem = 'PM';

function toggleConverterMeridiem() {
    convMeridiem = convMeridiem === 'AM' ? 'PM' : 'AM';
    const btn = document.getElementById('conv-meridiem-btn');
    if (btn) btn.innerText = convMeridiem;
    runClockConverter();
}

function setConvPreset(h, m, mer) {
    document.getElementById('conv-hh').value = h;
    document.getElementById('conv-mm').value = m;
    convMeridiem = mer;
    const btn = document.getElementById('conv-meridiem-btn');
    if (btn) btn.innerText = convMeridiem;
    runClockConverter();
}

function runClockConverter() {
    const hh = parseInt(document.getElementById('conv-hh').value) || 12;
    const mm = parseInt(document.getElementById('conv-mm').value) || 0;
    
    const h12Str = hh < 10 ? '0' + hh : '' + hh;
    const mStr = mm < 10 ? '0' + mm : '' + mm;
    
    document.getElementById('conv-12h-str').innerText = `${h12Str}:${mStr} ${convMeridiem}`;
    
    let h24 = hh;
    let mathRule = '';
    
    if (convMeridiem === 'AM') {
        if (hh === 12) {
            h24 = 0;
            mathRule = 'Midnight Rule: 12:00 AM becomes 00:00 hours';
        } else {
            mathRule = `Morning AM: Same hours (${hh} hours)`;
        }
    } else {
        if (hh === 12) {
            h24 = 12;
            mathRule = 'Noon Rule: 12:00 PM remains 12:00 hours';
        } else {
            h24 = hh + 12;
            mathRule = `PM Rule: Add 12 to hours (${hh} + 12 = ${h24})`;
        }
    }
    
    const h24Str = h24 < 10 ? '0' + h24 : '' + h24;
    document.getElementById('conv-math-rule').innerText = mathRule;
    document.getElementById('conv-24h-str').innerText = `${h24Str}:${mStr} Hours`;
}

// ============================================================================
// Simulator 9: Fractions Of Time
// ============================================================================
function setFractionSim(frac, label, mins, eq, degText, angle) {
    const badge = document.getElementById('frac-badge');
    const title = document.getElementById('frac-title');
    const eqStr = document.getElementById('frac-eq-str');
    const degStr = document.getElementById('frac-deg-str');
    const minHand = document.getElementById('frac-min-hand');
    const wedge = document.getElementById('frac-wedge-path');
    
    if (badge) badge.innerText = label;
    if (title) title.innerText = `${mins} Minutes`;
    if (eqStr) eqStr.innerText = `Equation: ${eq}`;
    if (degStr) degStr.innerText = `Angle: ${degText}`;
    
    if (minHand) {
        minHand.setAttribute('transform', `rotate(${angle} 50 50)`);
    }
    
    if (wedge) {
        if (angle === 360) {
            wedge.setAttribute('d', 'M 50 50 L 50 8 A 42 42 0 1 1 49.99 8 Z');
        } else {
            const rad = ((angle - 90) * Math.PI) / 180;
            const x = 50 + 42 * Math.cos(rad);
            const y = 50 + 42 * Math.sin(rad);
            const largeArc = angle > 180 ? 1 : 0;
            wedge.setAttribute('d', `M 50 50 L 50 8 A 42 42 0 ${largeArc} 1 ${x} ${y} Z`);
        }
    }
}

// ============================================================================
// Simulator 10: Clock Reading Errors
// ============================================================================
const diagCases = {
    1: {
        wrong: '"The minute hand points to 7, so the time is 3:07."',
        wrongWhy: 'Reading the clock face digit literally as minutes instead of multiplying by 5.',
        right: '"Actual Time: 3:35 (7 × 5 = 35 minutes)"',
        rightWhy: 'Each number from 1 to 12 marks a 5-minute interval: 7 × 5 = 35 minutes elapsed.',
        tip: 'Teacher Diagnostic Tip: The minute hand traces sixty 1-minute steps. Always multiply the pointed digit by 5!'
    },
    2: {
        wrong: '"The hour hand is close to 6 and minute hand is at 10, so it is 6:50."',
        wrongWhy: 'Assuming the hour hand belongs to 6 because it has almost moved there.',
        right: '"Actual Time: 5:50 (Ten minutes to 6:00)"',
        rightWhy: 'The hour hand only reaches 6 when the minute hand completes its full revolution to 12. At :50 it is still hour 5.',
        tip: 'Teacher Diagnostic Tip: An hour hand past halfway is anticipating the next hour, but has not arrived yet!'
    },
    3: {
        wrong: '"At four o\'clock, the time is written as 4:12."',
        wrongWhy: 'Confusing the minute hand pointing up at the number 12 with 12 minutes.',
        right: '"Actual Time: 4:00 (Zero minutes into the new hour)"',
        rightWhy: 'The 12 at the top of the dial indicates 00 minutes (a fresh hour completion).',
        tip: 'Teacher Diagnostic Tip: The number 12 represents both the 60-minute cycle end and 00-minute fresh start.'
    }
};

function selectDiagCase(caseNum) {
    [1, 2, 3].forEach(c => {
        const btn = document.getElementById(`diag-btn-${c}`);
        if (!btn) return;
        if (c === caseNum) {
            btn.className = 'p-2.5 rounded-xl border bg-red-600/20 border-red-500 text-red-300 font-bold text-left transition';
        } else {
            btn.className = 'p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-left transition hover:text-white';
        }
    });
    
    const d = diagCases[caseNum];
    document.getElementById('diag-wrong-text').innerText = d.wrong;
    document.getElementById('diag-wrong-reason').innerText = d.wrongWhy;
    document.getElementById('diag-right-text').innerText = d.right;
    document.getElementById('diag-right-reason').innerText = d.rightWhy;
    document.getElementById('diag-tip-box').innerHTML = `<strong>${d.tip.split(':')[0]}:</strong> ${d.tip.split(':')[1]}`;
}

// ============================================================================
// Simulator 12: Railway Time Schedules
// ============================================================================
const trainData = {
    rajdhani: {
        name: 'New Delhi - Mumbai Central Rajdhani',
        dep: '20:15',
        arr: '08:45',
        steps: 'Phase 1: 20:15 to 24:00 = 3h 45m. Phase 2: 00:00 to 08:45 = 8h 45m.<br>Total Duration: 3h 45m + 8h 45m = 11h 90m = <strong class="text-white">12 Hours 30 Minutes</strong>.'
    },
    vande: {
        name: 'New Delhi - Varanasi Vande Bharat',
        dep: '06:00',
        arr: '14:00',
        steps: 'Daytime Journey: 06:00 to 14:00.<br>Duration: 14:00 - 06:00 = <strong class="text-white">8 Hours 00 Minutes</strong>.'
    },
    mail: {
        name: 'Howrah - Kalka Mail',
        dep: '21:55',
        arr: '04:35',
        steps: 'Phase 1: 21:55 to 24:00 = 2h 05m. Phase 2: 00:00 to 04:35 = 4h 35m.<br>Total Duration: 2h 05m + 4h 35m = <strong class="text-white">6 Hours 40 Minutes</strong>.'
    }
};

function selectTrainSchedule(trainId) {
    ['rajdhani', 'vande', 'mail'].forEach(t => {
        const btn = document.getElementById(`train-btn-${t}`);
        if (!btn) return;
        if (t === trainId) {
            btn.className = 'p-2 rounded-xl border bg-blue-600/20 border-blue-500 text-blue-300 font-bold text-center transition';
        } else {
            btn.className = 'p-2 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-center transition hover:text-white';
        }
    });
    
    const tr = trainData[trainId];
    document.getElementById('train-name-tag').innerText = tr.name;
    document.getElementById('train-dep-str').innerText = tr.dep;
    document.getElementById('train-arr-str').innerText = tr.arr;
    document.getElementById('train-calc-steps').innerHTML = tr.steps;
}

// ============================================================================
// Simulator 13: Shelf Life Inspection Audit
// ============================================================================
const auditItems = [
    { name: '🍞 Whole Wheat Bread', mfg: '01/04/2025', life: '5 Days', exp: '06/04/2025', expDate: new Date(2025, 3, 6) },
    { name: '🧀 Processed Cheese', mfg: '15/01/2025', life: '90 Days', exp: '15/04/2025', expDate: new Date(2025, 3, 15) },
    { name: '🥛 UHT Milk Carton', mfg: '10/11/2024', life: '6 Months', exp: '10/05/2025', expDate: new Date(2025, 4, 10) },
    { name: '🍯 Organic Wild Honey', mfg: '01/01/2024', life: '24 Months', exp: '01/01/2026', expDate: new Date(2026, 0, 1) }
];

function runShelfLifeAudit() {
    const input = document.getElementById('audit-date-input');
    const tbody = document.getElementById('shelf-audit-tbody');
    if (!input || !tbody) return;
    
    const auditDate = new Date(input.value);
    tbody.innerHTML = '';
    
    auditItems.forEach(item => {
        const isSafe = auditDate <= item.expDate;
        const verdictHtml = isSafe
            ? '<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">PASSED (FRESH)</span>'
            : '<span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">REJECTED (EXPIRED)</span>';
            
        const row = document.createElement('tr');
        row.className = 'border-b border-slate-800/60 hover:bg-slate-800/30 transition';
        row.innerHTML = `
            <td class="py-2.5 px-2 text-white font-medium">${item.name}</td>
            <td class="py-2.5 px-2 text-slate-400">${item.mfg}</td>
            <td class="py-2.5 px-2 text-slate-300">${item.life}</td>
            <td class="py-2.5 px-2 text-amber-400 font-bold">${item.exp}</td>
            <td class="py-2.5 px-2">${verdictHtml}</td>
        `;
        tbody.appendChild(row);
    });
}

// ============================================================================
// Simulator 14: Days And Weeks Modular Cycle
// ============================================================================
function runCalendarJumps() {
    const container = document.getElementById('cal-grid-cells');
    if (!container) return;
    
    container.innerHTML = '';
    const sundays = [3, 10, 17, 24, 31];
    
    for (let day = 1; day <= 31; day++) {
        const cell = document.createElement('div');
        const isSun = sundays.includes(day);
        
        if (isSun) {
            cell.className = 'py-2 rounded-lg bg-emerald-600/40 border border-emerald-500 text-emerald-200 font-bold text-center ring-1 ring-emerald-400 animate-pulse';
            cell.innerText = `${day} ★`;
        } else {
            cell.className = 'py-2 rounded-lg bg-slate-900 border border-slate-800/80 text-slate-400 text-center';
            cell.innerText = `${day}`;
        }
        container.appendChild(cell);
    }
}

// ============================================================================
// Simulator 15: Century Leap Rules
// ============================================================================
function testCenturyYear(yr) {
    const val = parseInt(yr);
    const centVal = document.getElementById('cent-val');
    const badge = document.getElementById('cent-status-pill');
    const chk1 = document.getElementById('cent-chk1-math');
    const chk2Math = document.getElementById('cent-chk2-math');
    const chk2Res = document.getElementById('cent-chk2-res');
    
    if (centVal) centVal.innerText = val;
    
    const div4 = val / 4;
    if (chk1) chk1.innerText = `${val} ÷ 4 = ${div4} (R 0)`;
    
    const div400 = Math.floor(val / 400);
    const rem400 = val % 400;
    
    if (chk2Math) chk2Math.innerText = `${val} ÷ 400 = ${div400} (R ${rem400})`;
    
    if (rem400 === 0) {
        if (badge) {
            badge.className = 'px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            badge.innerText = 'LEAP CENTURY (366 Days)';
        }
        if (chk2Res) {
            chk2Res.className = 'text-[11px] text-emerald-400';
            chk2Res.innerText = 'Divisible by 400! February has 29 days.';
        }
    } else {
        if (badge) {
            badge.className = 'px-2.5 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
            badge.innerText = 'ORDINARY CENTURY (365 Days)';
        }
        if (chk2Res) {
            chk2Res.className = 'text-[11px] text-amber-400';
            chk2Res.innerText = `Not divisible by 400 (R ${rem400})! February has 28 days.`;
        }
    }
}

// ============================================================================
// Simulator 16: Time Arithmetic Logic
// ============================================================================
function setTimeArithMode(mode) {
    const btnAdd = document.getElementById('arith-mode-add');
    const btnSub = document.getElementById('arith-mode-sub');
    const op = document.getElementById('arith-op');
    const r1h = document.getElementById('arith-r1-h');
    const r1m = document.getElementById('arith-r1-m');
    const r2h = document.getElementById('arith-r2-h');
    const r2m = document.getElementById('arith-r2-m');
    const resh = document.getElementById('arith-res-h');
    const resm = document.getElementById('arith-res-m');
    const subh = document.getElementById('arith-sub-h');
    const subm = document.getElementById('arith-sub-m');
    const expl = document.getElementById('arith-step-expl');
    
    if (mode === 'add') {
        if (btnAdd) btnAdd.className = 'px-4 py-1.5 rounded-xl bg-emerald-600 text-white font-bold transition';
        if (btnSub) btnSub.className = 'px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition';
        if (op) op.innerText = '+';
        if (r1h) r1h.innerText = '3 hr';
        if (r1m) r1m.innerText = '45 min';
        if (r2h) r2h.innerText = '2 hr';
        if (r2m) r2m.innerText = '35 min';
        if (resh) resh.innerText = '6 hr';
        if (resm) resm.innerText = '20 min';
        if (subh) subh.innerText = '(3 + 2 + 1)';
        if (subm) subm.innerText = '(80m - 60m)';
        if (expl) expl.innerHTML = 'Minutes: 45 + 35 = 80 min. Since 80 ≥ 60, regroup 60 min into +1 hour. Remaining minutes = 80 - 60 = 20 min. Hours: 3 + 2 + 1 = 6 hours. Final Result = <strong>6 Hours 20 Minutes</strong>.';
    } else {
        if (btnAdd) btnAdd.className = 'px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition';
        if (btnSub) btnSub.className = 'px-4 py-1.5 rounded-xl bg-emerald-600 text-white font-bold transition';
        if (op) op.innerText = '−';
        if (r1h) r1h.innerText = '5 hr';
        if (r1m) r1m.innerText = '15 min';
        if (r2h) r2h.innerText = '2 hr';
        if (r2m) r2m.innerText = '40 min';
        if (resh) resh.innerText = '2 hr';
        if (resm) resm.innerText = '35 min';
        if (subh) subh.innerText = '(4 - 2)';
        if (subm) subm.innerText = '(75m - 40m)';
        if (expl) expl.innerHTML = 'Minutes: Cannot subtract 40 from 15. Borrow 1 hour (60 min) from 5 hr: hours become 4, minutes become 15 + 60 = 75 min. Minutes: 75 - 40 = 35 min. Hours: 4 - 2 = 2 hr. Final Result = <strong>2 Hours 35 Minutes</strong>.';
    }
}

// ============================================================================
// DOM Ready Lifecycle Initialization
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
    // Populate Speech API voices
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            window.speechSynthesis.getVoices();
        };
    }
    
    // Initialize active simulators
    updateLeapSim(2024);
    populateDateSelectors();
    renderDateFormatSim();
    selectExpiryProduct('biscuit');
    updateLunarSim(15);
    renderRoutineSvg();
    setTwelveHourSim(7, 0, 'AM', 'Morning activities between midnight and 12:00 noon.');
    runClockConverter();
    setFractionSim(0.25, '1/4 Hour (Quarter Past)', 15, '1/4 × 60 min = 15 min', '90° arc on dial', 90);
    selectDiagCase(1);
    selectTrainSchedule('rajdhani');
    runShelfLifeAudit();
    runCalendarJumps();
    testCenturyYear(2000);
    setTimeArithMode('add');
    
    showSlide(1);
});

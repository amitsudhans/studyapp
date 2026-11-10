
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
// Simulator 1: Mystery Matrix Puzzle
// ============================================================================
function checkMysteryMatrix() {
    const r1 = parseInt(document.getElementById('mm-row-1').value) || 0;
    const r2 = parseInt(document.getElementById('mm-row-2').value) || 0;
    const r3 = parseInt(document.getElementById('mm-row-3').value) || 0;
    const c1 = parseInt(document.getElementById('mm-col-1').value) || 0;
    const c2 = parseInt(document.getElementById('mm-col-2').value) || 0;
    const c3 = parseInt(document.getElementById('mm-col-3').value) || 0;
    
    const matrix = [
        [r1 * c1, r1 * c2, r1 * c3],
        [r2 * c1, r2 * c2, r2 * c3],
        [r3 * c1, r3 * c2, r3 * c3]
    ];
    
    for (let r = 1; r <= 3; r++) {
        for (let c = 1; c <= 3; c++) {
            const el = document.getElementById(`mm-c-${r}-${c}`);
            if (el) el.innerText = matrix[r-1][c-1];
        }
    }
    
    const status = document.getElementById('mm-status');
    if (status) {
        status.className = 'text-center text-xs p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-800/60 text-emerald-300 font-medium';
        status.innerHTML = `All 9 matrix cells updated: Row multipliers <strong>[${r1}, ${r2}, ${r3}]</strong> × Column multipliers <strong>[${c1}, ${c2}, ${c3}]</strong>!`;
    }
}

function resetMysteryMatrix(preset) {
    if (preset === 1) {
        document.getElementById('mm-row-1').value = 8;
        document.getElementById('mm-row-2').value = 5;
        document.getElementById('mm-row-3').value = 7;
        document.getElementById('mm-col-1').value = 3;
        document.getElementById('mm-col-2').value = 4;
        document.getElementById('mm-col-3').value = 6;
    } else {
        document.getElementById('mm-row-1').value = 6;
        document.getElementById('mm-row-2').value = 9;
        document.getElementById('mm-row-3').value = 4;
        document.getElementById('mm-col-1').value = 5;
        document.getElementById('mm-col-2').value = 7;
        document.getElementById('mm-col-3').value = 8;
    }
    checkMysteryMatrix();
}

// ============================================================================
// Simulator 2: Visualizing Tens Bundles
// ============================================================================
function updateTensSim(val) {
    const count = parseInt(val);
    const countEl = document.getElementById('tens-count-val');
    const labelEl = document.getElementById('tens-place-label');
    const formulaEl = document.getElementById('tens-math-formula');
    const container = document.getElementById('tens-rods-container');
    
    if (countEl) countEl.innerText = count;
    const total = count * 10;
    
    if (labelEl) {
        if (count === 10) {
            labelEl.className = 'px-2.5 py-1 rounded-full text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
            labelEl.innerText = '10 Tens = 1 Hundred Flat (100)';
        } else {
            labelEl.className = 'px-2.5 py-1 rounded-full text-[11px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
            labelEl.innerText = `${count} Tens = ${total}`;
        }
    }
    
    if (container) {
        container.innerHTML = '';
        if (count === 10) {
            // Render a 10x10 Hundred Flat grid
            container.innerHTML = `
                <div class="p-2 rounded-lg bg-amber-950/60 border border-amber-600/80 flex flex-col items-center">
                    <div class="grid grid-cols-10 gap-0.5 w-32 h-32 bg-amber-900/40 p-1 border border-amber-500/50 rounded">
                        ${Array(100).fill('<div class="w-full h-full bg-amber-400 rounded-[1px]"></div>').join('')}
                    </div>
                    <span class="text-[10px] text-amber-300 font-bold mt-1">100 Flat Unit</span>
                </div>
            `;
        } else {
            // Render Base-Ten Rods
            for (let i = 0; i < count; i++) {
                const rod = document.createElement('div');
                rod.className = 'flex flex-col items-center bg-cyan-950/60 p-1 border border-cyan-500/50 rounded';
                rod.innerHTML = `
                    <div class="flex flex-col gap-0.5 w-3 h-20 bg-cyan-900/40 p-0.5 border border-cyan-400/40 rounded">
                        ${Array(10).fill('<div class="w-full h-1.5 bg-cyan-400 rounded-[0.5px]"></div>').join('')}
                    </div>
                    <span class="text-[8px] text-cyan-300 font-mono mt-0.5">10</span>
                `;
                container.appendChild(rod);
            }
        }
    }
    
    if (formulaEl) {
        formulaEl.innerHTML = `Calculation: <strong>${count} × 10 = ${total} Units</strong> (${count} Tens rods combined)`;
    }
}

// ============================================================================
// Simulator 3: Constructing Table Arrays
// ============================================================================
function renderTableArraySim(val) {
    const n = parseInt(val) || 6;
    const t10 = n * 10;
    const t5 = n * 5;
    const total = t10 + t5;
    
    const m10 = document.getElementById('table-math-10');
    const m5 = document.getElementById('table-math-5');
    const addStr = document.getElementById('table-add-str');
    const resStr = document.getElementById('table-res-str');
    
    if (m10) m10.innerText = `${n} × 10 = ${t10}`;
    if (m5) m5.innerText = `${n} × 5 = ${t5}`;
    if (addStr) addStr.innerText = `${t10} + ${t5} = ${total}`;
    if (resStr) resStr.innerText = `${n} × 15 = ${total}`;
}

// ============================================================================
// Simulator 4: Comparing Number Tables
// ============================================================================
function renderTableComparison() {
    const tbody = document.getElementById('comp-table-body');
    if (!tbody) return;
    tbody.innerHTML = '';
    
    for (let i = 1; i <= 10; i++) {
        const p5 = i * 5;
        const p15 = i * 15;
        const row = document.createElement('tr');
        row.className = 'hover:bg-slate-800/30 transition';
        row.innerHTML = `
            <td class="py-1 px-2 text-slate-400 font-bold">${i}</td>
            <td class="py-1 px-2 text-pink-300 font-bold">${p5}</td>
            <td class="py-1 px-2 text-cyan-300 font-bold">${p15}</td>
            <td class="py-1 px-2 text-amber-300 font-mono text-[11px]">${p15} ÷ ${p5} = 3×</td>
        `;
        tbody.appendChild(row);
    }
}

// ============================================================================
// Simulator 5: Halving And Doubling
// ============================================================================
function setHalvingProblem(a, b) {
    const halfB = b / 2;
    const baseProd = a * halfB;
    const finalProd = baseProd * 2;
    
    document.getElementById('hd-step-1').innerText = `Half of ${b} is ${halfB}`;
    document.getElementById('hd-step-2').innerText = `${a} × ${halfB} = ${baseProd}`;
    document.getElementById('hd-step-3').innerText = `${baseProd} × 2 = ${finalProd}`;
    document.getElementById('hd-summary-note').innerHTML = `Exact Solution: <strong>${a} × ${b} = ${finalProd}</strong> (computed via doubling ${baseProd})`;
}

// ============================================================================
// Simulator 6: Scaling Decade Multiples
// ============================================================================
function setDecadePreset(f1, f2) {
    document.getElementById('dec-f1').value = f1;
    document.getElementById('dec-f2').value = f2;
    runDecadeScalingSim();
}

function runDecadeScalingSim() {
    const f1 = parseInt(document.getElementById('dec-f1').value) || 12;
    const f2 = parseInt(document.getElementById('dec-f2').value) || 20;
    
    const tensFactor = f2 / 10;
    const step1 = f1 * tensFactor;
    const total = step1 * 10;
    
    document.getElementById('dec-breakdown-str').innerText = `${f1} × ${f2} = ${f1} × ${tensFactor} × 10`;
    document.getElementById('dec-step1-res').innerText = `${f1} × ${tensFactor} = ${step1}`;
    document.getElementById('dec-step2-res').innerText = `${step1} × 10 = ${total}`;
}

// ============================================================================
// Simulator 7: Transport Museum Fleet Math
// ============================================================================
function calcMuseumFleet() {
    const count = parseInt(document.getElementById('museum-tram-count').value) || 1;
    const total = count * 32;
    document.getElementById('museum-fleet-res').innerText = `${count} Trams × 32 seats per tram = ${total} Total Passenger Capacity`;
}

// ============================================================================
// Simulator 10: Multiplication & Division Drill
// ============================================================================
function setDrillMode(mode) {
    const btnMult = document.getElementById('drill-btn-mult');
    const btnDiv = document.getElementById('drill-btn-div');
    const container = document.getElementById('drill-container');
    const vBox = document.getElementById('drill-verification-box');
    
    if (mode === 'mult') {
        if (btnMult) btnMult.className = 'px-4 py-1.5 rounded-xl bg-emerald-600 text-white font-bold transition';
        if (btnDiv) btnDiv.className = 'px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition';
        
        container.innerHTML = `
            <div class="w-56 space-y-1 text-right">
                <div class="text-slate-400 font-bold">24</div>
                <div class="flex justify-between items-center border-b-2 border-slate-700 pb-1">
                    <span class="text-emerald-400 font-black">×</span>
                    <span class="font-bold text-white">36</span>
                </div>
                <div class="text-cyan-300">144 <span class="text-[10px] text-slate-500">(24 × 6)</span></div>
                <div class="text-cyan-300">+ 720 <span class="text-[10px] text-slate-500">(24 × 30)</span></div>
                <div class="border-t-2 border-slate-700 pt-1 text-base font-black text-emerald-400">864</div>
            </div>
        `;
        if (vBox) vBox.innerHTML = 'Multiplication Result: <strong>24 × 36 = 864</strong> (144 ones partial product + 720 tens partial product)';
    } else {
        if (btnMult) btnMult.className = 'px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition';
        if (btnDiv) btnDiv.className = 'px-4 py-1.5 rounded-xl bg-emerald-600 text-white font-bold transition';
        
        container.innerHTML = `
            <div class="w-64 space-y-1">
                <div class="text-right text-emerald-400 font-bold text-sm">Quotient: 59</div>
                <div class="flex items-center border-t-2 border-slate-700 pt-1">
                    <span class="w-12 text-orange-400 font-bold">8 )</span>
                    <span class="font-bold text-white text-sm">478</span>
                </div>
                <div class="text-right text-slate-400">- 400 <span class="text-[10px] text-slate-500">(8 × 50)</span></div>
                <div class="border-t border-slate-700 text-right text-white">78</div>
                <div class="text-right text-slate-400">- 72 <span class="text-[10px] text-slate-500">(8 × 9)</span></div>
                <div class="border-t border-slate-700 text-right text-amber-400 font-bold">Remainder: 6</div>
            </div>
        `;
        if (vBox) vBox.innerHTML = 'Verification Check: <strong>(8 × 59) + 6 = 472 + 6 = 478</strong> (Dividend matches perfectly!)';
    }
}

// ============================================================================
// Simulator 11: Hundreds Scaling Patterns
// ============================================================================
function setHundredsProblem(a, b) {
    const total = a * b;
    document.getElementById('h-prob-str').innerText = `${a} × ${b}`;
    
    // Determine trailing zeroes
    let zCount = 0;
    if (a % 10 === 0) zCount++;
    if (b % 100 === 0) zCount += 2;
    else if (b % 10 === 0) zCount++;
    
    document.getElementById('h-zero-count-badge').innerText = `${zCount} Trailing Zeroes`;
    
    // Single digit part
    const aBase = (a % 10 === 0) ? a / 10 : a;
    const bBase = (b % 100 === 0) ? b / 100 : (b % 10 === 0 ? b / 10 : b);
    const baseProd = aBase * bBase;
    
    document.getElementById('h-step1-res').innerText = `${aBase} × ${bBase} = ${baseProd}`;
    document.getElementById('h-step2-res').innerText = `${a} × ${b} = ${total.toLocaleString()}`;
}

// ============================================================================
// Simulator 12: Dividing Tens & Hundreds
// ============================================================================
const packCases = {
    1: { eq: '750 ÷ 10', badge: 'Exact Packaging (R 0)', quot: '75 Sacks', rem: '0 kg Leftover' },
    2: { eq: '2,400 ÷ 100', badge: 'Exact Bulk Crates (R 0)', quot: '24 Crates', rem: '0 kg Leftover' },
    3: { eq: '846 ÷ 100', badge: 'Remainder Packaging', quot: '8 Crates', rem: '46 kg Leftover' }
};

function setPackCase(caseNum) {
    [1, 2, 3].forEach(c => {
        const btn = document.getElementById(`pack-btn-${c}`);
        if (!btn) return;
        if (c === caseNum) {
            btn.className = 'p-2.5 rounded-xl border bg-teal-600/20 border-teal-500 text-teal-300 font-bold text-left transition';
        } else {
            btn.className = 'p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-left transition hover:text-white';
        }
    });
    
    const d = packCases[caseNum];
    document.getElementById('pack-eq-str').innerText = d.eq;
    document.getElementById('pack-status-badge').innerText = d.badge;
    document.getElementById('pack-quot-res').innerText = d.quot;
    document.getElementById('pack-rem-res').innerText = d.rem;
}

// ============================================================================
// Simulator 14: Multiplication Pattern Discovery
// ============================================================================
function setPatternMode(mode) {
    const btnN = document.getElementById('pat-btn-nines');
    const btnE = document.getElementById('pat-btn-elevens');
    const card = document.getElementById('pat-demo-card');
    if (!card) return;
    
    if (mode === 'nines') {
        if (btnN) btnN.className = 'px-3.5 py-1.5 rounded-xl bg-rose-600 text-white font-bold transition';
        if (btnE) btnE.className = 'px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition';
        
        card.innerHTML = `
            <div class="text-rose-400 font-bold mb-2">Digital Roots of the Times-9 Table:</div>
            <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 text-center text-xs">
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 1 = 09<br><span class="text-emerald-400">0 + 9 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 2 = 18<br><span class="text-emerald-400">1 + 8 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 3 = 27<br><span class="text-emerald-400">2 + 7 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 4 = 36<br><span class="text-emerald-400">3 + 6 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 5 = 45<br><span class="text-emerald-400">4 + 5 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 6 = 54<br><span class="text-emerald-400">5 + 4 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 7 = 63<br><span class="text-emerald-400">6 + 3 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 8 = 72<br><span class="text-emerald-400">7 + 2 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 9 = 81<br><span class="text-emerald-400">8 + 1 = 9</span></div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800">9 × 10 = 90<br><span class="text-emerald-400">9 + 0 = 9</span></div>
            </div>
            <div class="text-[11px] text-slate-300 mt-2 bg-slate-900 p-2 rounded">Invariant: Adding the digits of any multiple of 9 always yields 9!</div>
        `;
    } else {
        if (btnN) btnN.className = 'px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition';
        if (btnE) btnE.className = 'px-3.5 py-1.5 rounded-xl bg-rose-600 text-white font-bold transition';
        
        card.innerHTML = `
            <div class="text-rose-400 font-bold mb-2">The 11s Split-Sum Insertion Shortcut:</div>
            <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800 flex justify-between items-center">
                    <span>25 × 11:</span>
                    <span>Split 2 and 5, insert (2 + 5 = 7) in center → <strong class="text-emerald-300 text-sm">275</strong></span>
                </div>
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800 flex justify-between items-center">
                    <span>34 × 11:</span>
                    <span>Split 3 and 4, insert (3 + 4 = 7) in center → <strong class="text-emerald-300 text-sm">374</strong></span>
                </div>
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800 flex justify-between items-center">
                    <span>52 × 11:</span>
                    <span>Split 5 and 2, insert (5 + 2 = 7) in center → <strong class="text-emerald-300 text-sm">572</strong></span>
                </div>
            </div>
        `;
    }
}

// ============================================================================
// Simulator 15: Fleet Capacity Matching
// ============================================================================
function recalcFleetCapacity() {
    const bikes = parseInt(document.getElementById('fl-bike-n').value) || 0;
    const autos = parseInt(document.getElementById('fl-auto-n').value) || 0;
    const cars = parseInt(document.getElementById('fl-car-n').value) || 0;
    const buses = parseInt(document.getElementById('fl-bus-n').value) || 0;
    
    const bTot = bikes * 1;
    const aTot = autos * 3;
    const cTot = cars * 5;
    const busTot = buses * 20;
    const grand = bTot + aTot + cTot + busTot;
    
    document.getElementById('fl-bike-tot').innerText = bTot;
    document.getElementById('fl-auto-tot').innerText = aTot;
    document.getElementById('fl-car-tot').innerText = cTot;
    document.getElementById('fl-bus-tot').innerText = busTot;
    document.getElementById('fl-grand-total').innerText = `${grand} Passengers`;
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
    checkMysteryMatrix();
    updateTensSim(4);
    renderTableArraySim(6);
    renderTableComparison();
    setHalvingProblem(3, 14);
    runDecadeScalingSim();
    calcMuseumFleet();
    setDrillMode('mult');
    setHundredsProblem(80, 50);
    setPackCase(1);
    setPatternMode('nines');
    recalcFleetCapacity();
    
    showSlide(1);
});

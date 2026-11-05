# -*- coding: utf-8 -*-
"""
JavaScript engine for NCERT Class 5 Mathematics - Chapter 6: The Dairy Farm
"""

js_code = '''
// State variables
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let watchdogInterval = null;
let currentAudioText = "";

// Voice configuration
let selectedVoice = null;
let availableVoices = [];

// Sound effects using Web Audio API
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSound(type) {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    const now = audioCtx.currentTime;

    if (type === 'correct') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.2);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
        osc.start(now);
        osc.stop(now + 0.25);
    } else if (type === 'incorrect') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(260, now);
        osc.frequency.exponentialRampToValueAtTime(130, now + 0.25);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
        osc.start(now);
        osc.stop(now + 0.3);
    } else if (type === 'click') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600, now);
        gain.gain.setValueAtTime(0.1, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
    }
}

// Pure Indian Male Voices Filter
function isIndianMaleVoice(v) {
    const name = v.name.toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    const femaleKeywords = [
        'female', 'woman', 'girl', 'lady', 'zira', 'aria', 'jenny', 'heera',
        'neerja', 'priya', 'swara', 'veena', 'google us english',
        'google indian english', 'google uk english female', 'google हिन्दी'
    ];
    if (femaleKeywords.some(kw => name.includes(kw))) return false;

    const indianMaleKeywords = ['prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'karan', 'mohan'];
    if (indianMaleKeywords.some(kw => name.includes(kw))) return true;

    if ((lang.includes('en-in') || lang.includes('en_in')) && !femaleKeywords.some(kw => name.includes(kw))) {
        if (name.includes('male') || !name.includes('google')) return true;
    }
    return false;
}

function isGeneralMaleVoice(v) {
    const name = v.name.toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    const femaleKeywords = [
        'female', 'woman', 'girl', 'lady', 'zira', 'aria', 'jenny', 'heera',
        'neerja', 'priya', 'swara', 'veena', 'google us english',
        'google indian english', 'google uk english female', 'google हिन्दी'
    ];
    if (femaleKeywords.some(kw => name.includes(kw))) return false;

    if (name.includes('uk english male') || name.includes('male') || name.includes('david') || name.includes('mark') || name.includes('alex') || name.includes('daniel')) {
        return true;
    }
    return false;
}

function initVoices() {
    if (!('speechSynthesis' in window)) return;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return;

    availableVoices = voices;
    const voiceSelect = document.getElementById('voiceSelect');
    if (voiceSelect) {
        voiceSelect.innerHTML = '';
    }

    let indianMale = voices.find(isIndianMaleVoice);
    let ukMale = voices.find(v => v.name.toLowerCase().includes('google uk english male'));
    let generalMale = voices.find(isGeneralMaleVoice);

    if (indianMale) {
        selectedVoice = indianMale;
    } else if (ukMale) {
        selectedVoice = ukMale;
    } else if (generalMale) {
        selectedVoice = generalMale;
    } else {
        selectedVoice = voices[0];
    }

    voices.forEach((v, idx) => {
        const isInd = isIndianMaleVoice(v);
        const isGenMale = isGeneralMaleVoice(v);
        const option = document.createElement('option');
        option.value = idx;
        let badge = '';
        if (isInd) badge = ' 🇮🇳 [Indian Male Teacher]';
        else if (isGenMale) badge = ' 👨 [Male Teacher]';
        option.textContent = `${v.name} (${v.lang})${badge}`;

        if (v === selectedVoice) {
            option.selected = true;
        }
        if (voiceSelect) {
            voiceSelect.appendChild(option);
        }
    });
}

function onVoiceChange(selectElem) {
    const idx = parseInt(selectElem.value, 10);
    if (availableVoices[idx]) {
        selectedVoice = availableVoices[idx];
        if (isSpeaking) {
            stopSpeech();
            speakLecture();
        }
    }
}

function speakLecture() {
    if (!('speechSynthesis' in window)) {
        alert('Web Speech API is not supported in this browser.');
        return;
    }

    if (isSpeaking) {
        stopSpeech();
        return;
    }

    const slideData = allSlidesData.find(s => s.id === currentSlide);
    if (!slideData || !slideData.lecture) return;

    currentAudioText = slideData.lecture;
    window.speechSynthesis.cancel();

    currentUtterance = new SpeechSynthesisUtterance(currentAudioText);
    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
    }

    const isInd = selectedVoice && isIndianMaleVoice(selectedVoice);
    const isMale = selectedVoice && isGeneralMaleVoice(selectedVoice);
    if (isInd || isMale) {
        currentUtterance.pitch = 0.85;
        currentUtterance.rate = 0.94;
    } else {
        currentUtterance.pitch = 0.55;
        currentUtterance.rate = 0.92;
    }

    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioButton(true);
        startWatchdog();
    };

    currentUtterance.onend = () => {
        isSpeaking = false;
        updateAudioButton(false);
        stopWatchdog();
    };

    currentUtterance.onerror = (e) => {
        console.error('TTS error:', e);
        isSpeaking = false;
        updateAudioButton(false);
        stopWatchdog();
    };

    window.speechSynthesis.speak(currentUtterance);
}

function stopSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    updateAudioButton(false);
    stopWatchdog();
}

function startWatchdog() {
    stopWatchdog();
    watchdogInterval = setInterval(() => {
        if (isSpeaking && 'speechSynthesis' in window) {
            if (window.speechSynthesis.paused) {
                window.speechSynthesis.resume();
            } else if (!window.speechSynthesis.speaking) {
                isSpeaking = false;
                updateAudioButton(false);
                stopWatchdog();
            }
        }
    }, 10000);
}

function stopWatchdog() {
    if (watchdogInterval) {
        clearInterval(watchdogInterval);
        watchdogInterval = null;
    }
}

function updateAudioButton(active) {
    const btn = document.getElementById('audioBtn');
    if (!btn) return;
    if (active) {
        btn.innerHTML = '<span>⏹️</span><span>Stop Lecture</span>';
        btn.classList.add('bg-rose-600', 'hover:bg-rose-500');
        btn.classList.remove('bg-emerald-600', 'hover:bg-emerald-500');
    } else {
        btn.innerHTML = '<span>🔊</span><span>Listen Lecture</span>';
        btn.classList.remove('bg-rose-600', 'hover:bg-rose-500');
        btn.classList.add('bg-emerald-600', 'hover:bg-emerald-500');
    }
}

// Slide Navigation
function goToSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;
    stopSpeech();

    document.querySelectorAll('.slide-card').forEach(el => {
        el.classList.add('hidden');
    });

    const target = document.getElementById(`slide-${slideNum}`);
    if (target) {
        target.classList.remove('hidden');
    }

    currentSlide = slideNum;
    updateNavUI();
    playSound('click');

    // Initialize slide-specific simulator
    initSimulatorForSlide(slideNum);
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
    }
}

function updateNavUI() {
    const curSpan = document.getElementById('curSlideNum');
    if (curSpan) curSpan.textContent = currentSlide;

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
    }

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.style.display = 'none';
    }

    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
        const pct = (currentSlide / totalSlides) * 100;
        progressBar.style.width = `${pct}%`;
    }

    const audioBtn = document.getElementById('audioBtn');
    const slideData = allSlidesData.find(s => s.id === currentSlide);
    if (audioBtn) {
        if (slideData && slideData.lecture) {
            audioBtn.style.display = 'inline-flex';
        } else {
            audioBtn.style.display = 'none';
        }
    }
}

// Formative Checkpoint Handling
function checkCheckpoint(qIndex, optIndex, correctIndex, explanation) {
    const container = document.getElementById(`cp_${currentSlide}_${qIndex}`);
    if (!container) return;

    const btns = container.querySelectorAll('.cp-opt-btn');
    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIndex) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-300');
        } else if (idx === optIndex && idx !== correctIndex) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-300');
        }
    });

    const expBox = document.getElementById(`cp_exp_${currentSlide}_${qIndex}`);
    if (expBox) {
        expBox.classList.remove('hidden');
        if (optIndex === correctIndex) {
            expBox.innerHTML = `<span class="text-emerald-400 font-bold">✓ Correct!</span> ${explanation}`;
            playSound('correct');
        } else {
            expBox.innerHTML = `<span class="text-rose-400 font-bold">✗ Keep trying!</span> ${explanation}`;
            playSound('incorrect');
        }
    }
}

// Mastery Quiz Handling
function answerQuiz(qId, selectedIdx, correctIdx) {
    const container = document.getElementById(`quiz_q_${qId}`);
    if (!container) return;

    const btns = container.querySelectorAll('.quiz-opt-btn');
    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-300');
        } else if (idx === selectedIdx && idx !== correctIdx) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-300');
        }
    });

    const solBtn = document.getElementById(`quiz_sol_btn_${qId}`);
    if (solBtn) {
        solBtn.classList.remove('hidden');
    }

    if (selectedIdx === correctIdx) {
        playSound('correct');
    } else {
        playSound('incorrect');
    }
}

function showSolutionModal(qId, title, solutionHtml) {
    const modal = document.getElementById('solutionModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');

    if (modal && modalTitle && modalBody) {
        modalTitle.textContent = title;
        modalBody.innerHTML = solutionHtml;
        modal.classList.remove('hidden');
        playSound('click');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
        playSound('click');
    }
}

// ==========================================
// 16 Bespoke Simulator Logic Implementations
// ==========================================

function initSimulatorForSlide(slideNum) {
    switch (slideNum) {
        case 1: updateSim1Array(); break;
        case 2: setSim2Mode('3x2'); break;
        case 3: runSim3Shift(); break;
        case 4: setSim4Factor(18); break;
        case 5: updateSim5View(); break;
        case 6: updateSim6(); break;
        case 7: setSim7Mode('auditorium'); break;
        case 8: updateSim8(); break;
        case 9: updateSim9(); break;
        case 10: updateSim10(); break;
        case 11: setSim11Problem(453, 13); break;
        case 12: setSim12Bug(1); break;
        case 13: setSim13Deriv('double_b'); break;
        case 14: updateSim14(); break;
        case 15: setSim15Mode('repunits'); break;
        case 16: setSim16Tab('algebra'); break;
    }
}

// Sim 1: Shape Decrypter & Pouch Array
function setSim1Puzzle(c_sq, tri_prod, sq_prod) {
    const c_val = Math.round(Math.sqrt(c_sq));
    const tri_val = tri_prod / c_val;
    const sq_val = sq_prod / tri_val;

    document.getElementById('sim1_circ_sq').textContent = c_sq;
    document.getElementById('sim1_circ_val').textContent = c_val;
    document.getElementById('sim1_tri_prod').textContent = tri_prod;
    document.getElementById('sim1_tri_val').textContent = tri_val;
    document.getElementById('sim1_sq_prod').textContent = sq_prod;
    document.getElementById('sim1_sq_val').textContent = sq_val;
    playSound('click');
}

function updateSim1Array() {
    const rows = parseInt(document.getElementById('sim1_rows')?.value || 6, 10);
    const cols = parseInt(document.getElementById('sim1_cols')?.value || 5, 10);
    const trays = parseInt(document.getElementById('sim1_trays')?.value || 4, 10);

    const rowsVal = document.getElementById('sim1_rows_val');
    const colsVal = document.getElementById('sim1_cols_val');
    const traysVal = document.getElementById('sim1_trays_val');
    if (rowsVal) rowsVal.textContent = rows;
    if (colsVal) colsVal.textContent = cols;
    if (traysVal) traysVal.textContent = trays;

    const perTray = rows * cols;
    const total = trays * perTray;

    const tally = document.getElementById('sim1_tray_tally');
    if (tally) tally.textContent = `${trays} Trays × (${rows} × ${cols}) = ${total} Pouches`;

    const summary = document.getElementById('sim1_summary');
    if (summary) summary.textContent = `1 Tray = ${rows} × ${cols} = ${perTray} pouches | ${trays} Trays = ${total} total pouches`;

    const svg = document.getElementById('sim1_svg');
    if (svg) {
        svg.innerHTML = '';
        // Draw 1 sample tray with rows x cols pouches
        const startX = 20, startY = 15;
        const pW = 340 / cols;
        const pH = 110 / rows;

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                rect.setAttribute('x', startX + c * pW + 2);
                rect.setAttribute('y', startY + r * pH + 2);
                rect.setAttribute('width', Math.max(pW - 4, 4));
                rect.setAttribute('height', Math.max(pH - 4, 4));
                rect.setAttribute('rx', '3');
                rect.setAttribute('fill', '#0284c7');
                rect.setAttribute('stroke', '#38bdf8');
                rect.setAttribute('stroke-width', '1');
                svg.appendChild(rect);
            }
        }
    }
}

// Sim 2: Commutative Property & Zero
function setSim2Mode(mode) {
    const display = document.getElementById('sim2_display');
    const explanation = document.getElementById('sim2_explanation');
    const formula = document.getElementById('sim2_formula');
    const b3x2 = document.getElementById('sim2_btn_3x2');
    const b2x3 = document.getElementById('sim2_btn_2x3');
    const bzero = document.getElementById('sim2_btn_zero');

    b3x2?.classList.replace('bg-indigo-600', 'bg-slate-700');
    b2x3?.classList.replace('bg-indigo-600', 'bg-slate-700');
    bzero?.classList.replace('bg-indigo-600', 'bg-slate-700');

    if (!display || !explanation || !formula) return;
    display.innerHTML = '';

    if (mode === '3x2') {
        b3x2?.classList.replace('bg-slate-700', 'bg-indigo-600');
        formula.textContent = '3 Groups of 2 = 3 × 2 = 6';
        explanation.textContent = '3 crates with 2 bottles each = 3 × 2 = 6 bottles';
        for (let i = 1; i <= 3; i++) {
            const crate = document.createElement('div');
            crate.className = 'p-3 bg-slate-900 border border-indigo-500/40 rounded-xl flex items-center gap-2';
            crate.innerHTML = `<span class="text-[10px] text-indigo-400 font-bold block">Crate ${i}:</span>
                               <span class="text-xl">🥛</span><span class="text-xl">🥛</span>`;
            display.appendChild(crate);
        }
    } else if (mode === '2x3') {
        b2x3?.classList.replace('bg-slate-700', 'bg-indigo-600');
        formula.textContent = '2 Groups of 3 = 2 × 3 = 6';
        explanation.textContent = '2 crates with 3 bottles each = 2 × 3 = 6 bottles';
        for (let i = 1; i <= 2; i++) {
            const crate = document.createElement('div');
            crate.className = 'p-3 bg-slate-900 border border-cyan-500/40 rounded-xl flex items-center gap-2';
            crate.innerHTML = `<span class="text-[10px] text-cyan-400 font-bold block">Crate ${i}:</span>
                               <span class="text-xl">🥛</span><span class="text-xl">🥛</span><span class="text-xl">🥛</span>`;
            display.appendChild(crate);
        }
    } else if (mode === 'zero') {
        bzero?.classList.replace('bg-slate-700', 'bg-indigo-600');
        formula.textContent = '4 Groups of 0 = 4 × 0 = 0';
        explanation.textContent = '4 empty crates with 0 bottles each = 4 × 0 = 0 bottles';
        for (let i = 1; i <= 4; i++) {
            const crate = document.createElement('div');
            crate.className = 'p-3 bg-slate-900 border border-rose-500/40 rounded-xl flex items-center gap-2';
            crate.innerHTML = `<span class="text-[10px] text-rose-400 font-bold block">Crate ${i}:</span>
                               <span class="text-xs text-slate-500 italic">Empty (0)</span>`;
            display.appendChild(crate);
        }
    }
    playSound('click');
}

// Sim 3: Place Value Shift Machine
let sim3Multiplier = 10;
function setSim3Mult(m) {
    sim3Multiplier = m;
    [1, 10, 100, 1000].forEach(val => {
        const btn = document.getElementById(`sim3_m${val}`);
        if (btn) {
            if (val === m) btn.className = 'px-2.5 py-1 bg-cyan-600 rounded font-mono font-bold text-xs';
            else btn.className = 'px-2.5 py-1 bg-slate-700 rounded font-mono font-bold text-xs';
        }
    });
    runSim3Shift();
    playSound('click');
}

function runSim3Shift() {
    const input = parseInt(document.getElementById('sim3_input')?.value || 34, 10);
    const prod = input * sim3Multiplier;

    const s = prod.toString().padStart(5, ' ');
    const tth = s[0] === ' ' ? '-' : s[0];
    const th = s[1] === ' ' ? '-' : s[1];
    const h = s[2] === ' ' ? '-' : s[2];
    const t = s[3] === ' ' ? '-' : s[3];
    const o = s[4] === ' ' ? '-' : s[4];

    document.getElementById('sim3_tth').textContent = tth;
    document.getElementById('sim3_th').textContent = th;
    document.getElementById('sim3_h').textContent = h;
    document.getElementById('sim3_t').textContent = t;
    document.getElementById('sim3_o').textContent = o;

    const shiftCount = Math.log10(sim3Multiplier);
    const text = document.getElementById('sim3_text');
    if (text) {
        if (sim3Multiplier === 1) {
            text.textContent = `${input} × 1 = ${prod} (Identity rule: value unchanged)`;
        } else {
            text.textContent = `${input} × ${sim3Multiplier.toLocaleString()} = ${prod.toLocaleString()} (digits shifted ${shiftCount} place(s) left; ${shiftCount} trailing zero(s) appended)`;
        }
    }
}

// Sim 4: 3-Way Strategy Comparator
function setSim4Factor(f) {
    [18, 24, 36].forEach(val => {
        const btn = document.getElementById(`sim4_f${val}`);
        if (btn) {
            btn.className = (val === f) ? 'px-2.5 py-1 bg-teal-600 rounded font-mono font-bold' : 'px-2.5 py-1 bg-slate-700 rounded font-mono font-bold';
        }
    });

    const prod = f * 5;
    document.getElementById('sim4_target').textContent = `Target: ${f} × 5 = ${prod}`;
    document.getElementById('sim4_final').textContent = prod;

    // Halving & Doubling
    const half = f / 2;
    document.getElementById('sim4_hd_1').textContent = `• ${f} ÷ 2 = ${half}`;
    document.getElementById('sim4_hd_2').textContent = `• 5 × 2 = 10`;
    document.getElementById('sim4_hd_res').textContent = `➔ ${half} × 10 = ${prod}`;

    // Partitioning
    const tens = Math.floor(f / 10) * 10;
    const ones = f % 10;
    document.getElementById('sim4_pt_1').textContent = `• ${tens} × 5 = ${tens * 5}`;
    document.getElementById('sim4_pt_2').textContent = `• ${ones} × 5 = ${ones * 5}`;
    document.getElementById('sim4_pt_res').textContent = `➔ ${tens * 5} + ${ones * 5} = ${prod}`;

    // Compensation
    const nextTen = Math.ceil(f / 10) * 10;
    const diff = nextTen - f;
    document.getElementById('sim4_cp_1').textContent = `• ${nextTen} × 5 = ${nextTen * 5}`;
    document.getElementById('sim4_cp_2').textContent = `• - (${diff} × 5) = -${diff * 5}`;
    document.getElementById('sim4_cp_res').textContent = `➔ ${nextTen * 5} - ${diff * 5} = ${prod}`;

    playSound('click');
}

// Sim 5: Rectangle Slice & Paste Area Model
let sim5Width = 25;
let sim5Height = 16;
let sim5Step = 0; // 0 = original, 1 = halved/doubled

function setSim5Preset(h, w) {
    sim5Height = h;
    sim5Width = w;
    sim5Step = 0;
    [1, 2, 3].forEach(idx => {
        const btn = document.getElementById(`sim5_p${idx}`);
        if (btn) btn.className = 'px-2.5 py-1 bg-slate-700 rounded font-mono font-bold';
    });
    const map = { '16_25': 1, '24_50': 2, '28_25': 3 };
    const key = `${h}_${w}`;
    if (map[key]) {
        document.getElementById(`sim5_p${map[key]}`).className = 'px-2.5 py-1 bg-emerald-600 rounded font-mono font-bold';
    }
    updateSim5View();
    playSound('click');
}

function toggleSim5Slice() {
    sim5Step = (sim5Step === 0) ? 1 : 0;
    updateSim5View();
    playSound('correct');
}

function updateSim5View() {
    const area = sim5Height * sim5Width;
    document.getElementById('sim5_dim').textContent = `${sim5Height} × ${sim5Width} = ${area} m²`;

    const svg = document.getElementById('sim5_svg');
    const stepText = document.getElementById('sim5_step_text');
    if (!svg || !stepText) return;
    svg.innerHTML = '';

    if (sim5Step === 0) {
        stepText.textContent = `Original: Height ${sim5Height} m × Width ${sim5Width} m = ${area} m²`;
        // Draw single rectangle
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', '100');
        rect.setAttribute('y', '20');
        rect.setAttribute('width', '180');
        rect.setAttribute('height', '90');
        rect.setAttribute('fill', '#059669');
        rect.setAttribute('stroke', '#34d399');
        rect.setAttribute('stroke-width', '2');
        rect.setAttribute('rx', '6');
        svg.appendChild(rect);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', '190');
        text.setAttribute('y', '70');
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', '#ecfdf5');
        text.setAttribute('font-size', '14');
        text.setAttribute('font-weight', 'bold');
        text.textContent = `${sim5Height} m × ${sim5Width} m = ${area} m²`;
        svg.appendChild(text);
    } else {
        const newH = sim5Height / 2;
        const newW = sim5Width * 2;
        stepText.textContent = `Sliced & Doubled: Height ${newH} m × Width ${newW} m = ${area} m² (Friendly Multiplier!)`;

        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', '40');
        rect.setAttribute('y', '45');
        rect.setAttribute('width', '300');
        rect.setAttribute('height', '45');
        rect.setAttribute('fill', '#0284c7');
        rect.setAttribute('stroke', '#38bdf8');
        rect.setAttribute('stroke-width', '2');
        rect.setAttribute('rx', '6');
        svg.appendChild(rect);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', '190');
        text.setAttribute('y', '72');
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', '#f0f9ff');
        text.setAttribute('font-size', '14');
        text.setAttribute('font-weight', 'bold');
        text.textContent = `${newH} m × ${newW} m = ${area} m²`;
        svg.appendChild(text);
    }
}

// Sim 6: Nearest Multiple Compensation
function updateSim6() {
    const m = parseInt(document.getElementById('sim6_m')?.value || 4, 10);
    const t = parseInt(document.getElementById('sim6_t')?.value || 19, 10);

    document.getElementById('sim6_m_val').textContent = m;
    document.getElementById('sim6_t_val').textContent = t;

    const roundTen = Math.round(t / 10) * 10;
    const diff = roundTen - t;
    const roundProd = m * roundTen;
    const adjust = m * Math.abs(diff);
    const finalProd = m * t;

    document.getElementById('sim6_preview').textContent = `${m} × ${t} = ${finalProd}`;
    document.getElementById('sim6_round_calc').textContent = `${m} × ${roundTen} = ${roundProd}`;

    const sign = (diff > 0) ? '-' : '+';
    document.getElementById('sim6_adjust_calc').textContent = `${sign} (${m} × ${Math.abs(diff)}) = ${sign}${adjust}`;
    document.getElementById('sim6_final_calc').textContent = `${roundProd} ${sign} ${adjust} = ${finalProd}`;

    const svg = document.getElementById('sim6_svg');
    if (svg) {
        svg.innerHTML = '';
        // Base bar
        const baseBar = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        baseBar.setAttribute('x', '20');
        baseBar.setAttribute('y', '15');
        baseBar.setAttribute('width', '280');
        baseBar.setAttribute('height', '30');
        baseBar.setAttribute('fill', '#4f46e5');
        baseBar.setAttribute('rx', '4');
        svg.appendChild(baseBar);

        // Adjustment strip
        const adjStrip = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        adjStrip.setAttribute('x', (diff > 0) ? '260' : '300');
        adjStrip.setAttribute('y', '15');
        adjStrip.setAttribute('width', '40');
        adjStrip.setAttribute('height', '30');
        adjStrip.setAttribute('fill', (diff > 0) ? '#e11d48' : '#10b981');
        adjStrip.setAttribute('rx', '4');
        svg.appendChild(adjStrip);

        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        label.setAttribute('x', '150');
        label.setAttribute('y', '35');
        label.setAttribute('fill', '#ffffff');
        label.setAttribute('font-size', '12');
        label.setAttribute('font-weight', 'bold');
        label.setAttribute('text-anchor', 'middle');
        label.textContent = `Base: ${roundProd} | Adjust: ${sign}${adjust}`;
        svg.appendChild(label);
    }
}

// Sim 7: Real-World Scenario Multiplier
let sim7CurrentMode = 'auditorium';
function setSim7Mode(mode) {
    sim7CurrentMode = mode;
    ['aud', 'milk', 'kurta'].forEach(m => {
        const btn = document.getElementById(`sim7_m_${m}`);
        if (btn) {
            btn.className = (m === (mode === 'auditorium' ? 'aud' : mode)) ? 'px-3 py-1 bg-indigo-600 rounded text-xs font-bold' : 'px-3 py-1 bg-slate-700 rounded text-xs font-bold';
        }
    });

    const controls = document.getElementById('sim7_controls');
    const title = document.getElementById('sim7_mode_title');
    if (!controls || !title) return;

    if (mode === 'auditorium') {
        title.textContent = 'Auditorium Seating';
        controls.innerHTML = `
            <div>
                <div class="flex justify-between items-center mb-1">
                    <span>Rows: <strong id="sim7_v1" class="text-indigo-400">24</strong></span>
                </div>
                <input type="range" id="sim7_r1" min="10" max="30" value="24" oninput="updateSim7()" class="w-full accent-indigo-400">
            </div>
            <div>
                <div class="flex justify-between items-center mb-1">
                    <span>Seats per Row: <strong id="sim7_v2" class="text-cyan-400">18</strong></span>
                </div>
                <input type="range" id="sim7_r2" min="10" max="25" value="18" oninput="updateSim7()" class="w-full accent-cyan-400">
            </div>
        `;
    } else if (mode === 'milk') {
        title.textContent = 'Milk Herd Production';
        controls.innerHTML = `
            <div>
                <div class="flex justify-between items-center mb-1">
                    <span>Cows in Herd: <strong id="sim7_v1" class="text-indigo-400">14</strong></span>
                </div>
                <input type="range" id="sim7_r1" min="5" max="30" value="14" oninput="updateSim7()" class="w-full accent-indigo-400">
            </div>
            <div>
                <div class="flex justify-between items-center mb-1">
                    <span>Daily Yield per Cow (L): <strong id="sim7_v2" class="text-cyan-400">12</strong></span>
                </div>
                <input type="range" id="sim7_r2" min="5" max="20" value="12" oninput="updateSim7()" class="w-full accent-cyan-400">
            </div>
        `;
    } else if (mode === 'kurta') {
        title.textContent = 'Kurta Uniform Cloth Scaling';
        controls.innerHTML = `
            <div>
                <div class="flex justify-between items-center mb-1">
                    <span>Staff Kurtas: <strong id="sim7_v1" class="text-indigo-400">8</strong></span>
                </div>
                <input type="range" id="sim7_r1" min="1" max="15" value="8" oninput="updateSim7()" class="w-full accent-indigo-400">
            </div>
            <div class="p-2 bg-slate-900 rounded font-mono text-[11px] text-slate-300 flex items-center">
                <span>Each Kurta requires <strong>2 m 25 cm</strong></span>
            </div>
        `;
    }
    updateSim7();
    playSound('click');
}

function updateSim7() {
    const v1 = parseInt(document.getElementById('sim7_r1')?.value || 10, 10);
    const v2 = parseInt(document.getElementById('sim7_r2')?.value || 10, 10);
    const lbl1 = document.getElementById('sim7_v1');
    const lbl2 = document.getElementById('sim7_v2');
    if (lbl1) lbl1.textContent = v1;
    if (lbl2) lbl2.textContent = v2;

    const calc = document.getElementById('sim7_calculation');
    const sub = document.getElementById('sim7_subtext');

    if (sim7CurrentMode === 'auditorium') {
        const total = v1 * v2;
        if (calc) calc.textContent = `${v1} rows × ${v2} seats = ${total} seats`;
        if (sub) sub.textContent = `${v1} × (${Math.round(v2/10)*10} - ${Math.round(v2/10)*10 - v2}) = ${total}`;
    } else if (sim7CurrentMode === 'milk') {
        const daily = v1 * v2;
        const weekly = daily * 7;
        if (calc) calc.textContent = `${v1} cows × ${v2} L/day = ${daily} L/day`;
        if (sub) sub.textContent = `Weekly Herd Yield = ${daily} L × 7 days = ${weekly} litres`;
    } else if (sim7CurrentMode === 'kurta') {
        const totalCm = v1 * 225;
        const m = Math.floor(totalCm / 100);
        const cm = totalCm % 100;
        if (calc) calc.textContent = `${v1} Kurtas × 2 m 25 cm = ${m} m ${cm > 0 ? cm + ' cm' : ''}`;
        if (sub) sub.textContent = `Metres: ${v1} × 2 = ${v1*2} m | Centimetres: ${v1} × 25 = ${v1*25} cm = ${Math.floor(v1*25/100)} m ${ (v1*25)%100 } cm`;
    }
}

// Sim 8: Compost Savings
function updateSim8() {
    const waste = parseInt(document.getElementById('sim8_waste')?.value || 350, 10);
    const cost = parseInt(document.getElementById('sim8_cost')?.value || 120, 10);

    document.getElementById('sim8_waste_val').textContent = `${waste} g`;
    document.getElementById('sim8_cost_val').textContent = `₹ ${cost}`;

    const mWasteG = waste * 30;
    const yWasteG = waste * 365;
    const mWasteKg = (mWasteG / 1000).toFixed(1);
    const yWasteKg = (yWasteG / 1000).toFixed(1);

    // Yield ~ 1 5kg bag per 5kg organic matter
    const bags = Math.floor(yWasteG / 5000);
    const savings = bags * cost;

    document.getElementById('sim8_m_waste').textContent = `${mWasteKg} kg`;
    document.getElementById('sim8_y_waste').textContent = `${yWasteKg} kg`;
    document.getElementById('sim8_bags').textContent = `${bags} bags`;
    document.getElementById('sim8_savings').textContent = `₹ ${savings.toLocaleString()}`;
}

// Sim 9: 2×2 Box Method Grid Builder
function setSim9Preset(n1, n2) {
    document.getElementById('sim9_n1').value = n1;
    document.getElementById('sim9_n2').value = n2;
    updateSim9();
    playSound('click');
}

function updateSim9() {
    const n1 = parseInt(document.getElementById('sim9_n1')?.value || 69, 10);
    const n2 = parseInt(document.getElementById('sim9_n2')?.value || 45, 10);

    const t1 = Math.floor(n1 / 10) * 10;
    const o1 = n1 % 10;
    const t2 = Math.floor(n2 / 10) * 10;
    const o2 = n2 % 10;

    const c1 = t1 * t2;
    const c2 = o1 * t2;
    const c3 = t1 * o2;
    const c4 = o1 * o2;

    const row1 = c1 + c2;
    const row2 = c3 + c4;
    const total = row1 + row2;

    document.getElementById('sim9_summary_top').textContent = `${n1} × ${n2} = ${total.toLocaleString()}`;
    document.getElementById('sim9_t1').textContent = t1;
    document.getElementById('sim9_o1').textContent = o1;
    document.getElementById('sim9_t2').textContent = t2;
    document.getElementById('sim9_o2').textContent = o2;

    document.getElementById('sim9_c1_lbl').textContent = `${t1} × ${t2}`;
    document.getElementById('sim9_c1').textContent = c1.toLocaleString();
    document.getElementById('sim9_c2_lbl').textContent = `${o1} × ${t2}`;
    document.getElementById('sim9_c2').textContent = c2.toLocaleString();
    document.getElementById('sim9_c3_lbl').textContent = `${t1} × ${o2}`;
    document.getElementById('sim9_c3').textContent = c3.toLocaleString();
    document.getElementById('sim9_c4_lbl').textContent = `${o1} × ${o2}`;
    document.getElementById('sim9_c4').textContent = c4.toLocaleString();

    document.getElementById('sim9_row1_sum').textContent = `Row 1: ${row1.toLocaleString()}`;
    document.getElementById('sim9_row2_sum').textContent = `Row 2: ${row2.toLocaleString()}`;
    document.getElementById('sim9_grand_total').textContent = total.toLocaleString();
}

// Sim 10: Cricket Scoreboard
function updateSim10() {
    const f = parseInt(document.getElementById('sim10_f')?.value || 14, 10);
    const s = parseInt(document.getElementById('sim10_s')?.value || 8, 10);
    const o = parseInt(document.getElementById('sim10_1')?.value || 32, 10);

    const rF = f * 4;
    const rS = s * 6;
    const rO = o * 1;
    const total = rF + rS + rO;

    document.getElementById('sim10_f_val').textContent = f;
    document.getElementById('sim10_s_val').textContent = s;
    document.getElementById('sim10_1_val').textContent = o;

    document.getElementById('sim10_f_runs').textContent = rF;
    document.getElementById('sim10_s_runs').textContent = rS;
    document.getElementById('sim10_1_runs').textContent = rO;

    document.getElementById('sim10_summary_stat').textContent = `${total} Total Runs`;
    document.getElementById('sim10_eq').textContent = `${rF} + ${rS} + ${rO}`;
    document.getElementById('sim10_total').textContent = `${total} Runs Scored!`;
}

// Sim 11: Standard Column Stepper
let sim11N1 = 453;
let sim11N2 = 13;
let sim11CurrentStep = 0;

function setSim11Problem(n1, n2) {
    sim11N1 = n1;
    sim11N2 = n2;
    sim11CurrentStep = 0;
    ['p1', 'p2', 'p3'].forEach(p => {
        const btn = document.getElementById(`sim11_${p}`);
        if (btn) btn.className = 'px-2.5 py-1 bg-slate-700 rounded font-mono font-bold';
    });
    if (n1 === 453) document.getElementById('sim11_p1').className = 'px-2.5 py-1 bg-indigo-600 rounded font-mono font-bold';
    else if (n1 === 324) document.getElementById('sim11_p2').className = 'px-2.5 py-1 bg-indigo-600 rounded font-mono font-bold';
    else if (n1 === 574) document.getElementById('sim11_p3').className = 'px-2.5 py-1 bg-indigo-600 rounded font-mono font-bold';

    renderSim11();
    playSound('click');
}

function nextSim11Step() {
    const maxSteps = (sim11N2 >= 100) ? 4 : 3;
    sim11CurrentStep = (sim11CurrentStep + 1) % (maxSteps + 1);
    renderSim11();
    playSound('correct');
}

function renderSim11() {
    const box = document.getElementById('sim11_calc_box');
    const exp = document.getElementById('sim11_explanation');
    const tag = document.getElementById('sim11_step_tag');
    if (!box || !exp || !tag) return;

    const maxSteps = (sim11N2 >= 100) ? 4 : 3;
    tag.textContent = `Step ${sim11CurrentStep} of ${maxSteps}`;

    const ones2 = sim11N2 % 10;
    const tens2 = Math.floor((sim11N2 % 100) / 10);
    const hundreds2 = Math.floor(sim11N2 / 100);

    const p1 = sim11N1 * ones2;
    const p2 = sim11N1 * tens2 * 10;
    const p3 = hundreds2 > 0 ? (sim11N1 * hundreds2 * 100) : 0;
    const total = sim11N1 * sim11N2;

    let html = `
        <div class="text-slate-400 font-bold">${sim11N1}</div>
        <div class="text-slate-400 font-bold">× &nbsp;${sim11N2}</div>
        <div class="border-b border-slate-700 my-1"></div>
    `;

    if (sim11CurrentStep === 0) {
        exp.textContent = `Set up: Multiply ${sim11N1} by each place-value digit of ${sim11N2}.`;
    } else if (sim11CurrentStep === 1) {
        html += `<div class="text-cyan-300 font-bold">${p1} <span class="text-[10px] text-slate-400">(${sim11N1} × ${ones2})</span></div>`;
        exp.textContent = `Step 1: Multiply by the ones digit ${ones2}: ${sim11N1} × ${ones2} = ${p1}.`;
    } else if (sim11CurrentStep === 2) {
        html += `<div class="text-cyan-300">${p1}</div>`;
        html += `<div class="text-amber-300 font-bold">+ ${p2} <span class="text-[10px] text-amber-400 font-semibold">(tens zero!)</span></div>`;
        exp.textContent = `Step 2: Multiply by tens digit ${tens2} (value ${tens2 * 10}). Note the zero in units column!`;
    } else if (sim11CurrentStep === 3) {
        html += `<div class="text-cyan-300">${p1}</div>`;
        html += `<div class="text-amber-300">+ ${p2}</div>`;
        if (hundreds2 > 0) {
            html += `<div class="text-purple-300 font-bold">+ ${p3} <span class="text-[10px] text-purple-400">(hundreds zeros!)</span></div>`;
            exp.textContent = `Step 3: Multiply by hundreds digit ${hundreds2} (value ${hundreds2 * 100}). Note two zero placeholders!`;
        } else {
            html += `<div class="border-b border-slate-700 my-1"></div>`;
            html += `<div class="text-emerald-400 font-bold text-base">${total}</div>`;
            exp.textContent = `Step 3: Sum the partial products: ${p1} + ${p2} = ${total}!`;
        }
    } else if (sim11CurrentStep === 4) {
        html += `<div class="text-cyan-300">${p1}</div>`;
        html += `<div class="text-amber-300">+ ${p2}</div>`;
        html += `<div class="text-purple-300">+ ${p3}</div>`;
        html += `<div class="border-b border-slate-700 my-1"></div>`;
        html += `<div class="text-emerald-400 font-bold text-base">${total}</div>`;
        exp.textContent = `Step 4: Sum all partial products: ${p1} + ${p2} + ${p3} = ${total}!`;
    }

    box.innerHTML = html;
}

// Sim 12: Bug Hunter
function setSim12Bug(bugId) {
    [1, 2, 3].forEach(b => {
        const btn = document.getElementById(`sim12_b${b}`);
        if (btn) btn.className = (b === bugId) ? 'px-3 py-1 bg-rose-600 rounded text-xs font-bold' : 'px-3 py-1 bg-slate-700 rounded text-xs font-bold';
    });

    const wBox = document.getElementById('sim12_wrong_box');
    const rBox = document.getElementById('sim12_right_box');
    const fDesc = document.getElementById('sim12_flaw_desc');
    const rDesc = document.getElementById('sim12_fix_desc');

    if (!wBox || !rBox) return;

    if (bugId === 1) {
        wBox.innerHTML = `
            <p class="text-slate-400">54 × 23</p>
            <p class="text-slate-300">&nbsp; 162</p>
            <p class="text-rose-400 font-bold">+ 108 ❌ Missing 0</p>
            <div class="border-b border-slate-700"></div>
            <p class="text-rose-400 font-bold">&nbsp; 270 ❌</p>
        `;
        fDesc.textContent = 'Flaw: The second partial product omitted the place value zero for 20, treating it as 2.';

        rBox.innerHTML = `
            <p class="text-slate-400">54 × 23</p>
            <p class="text-slate-300">&nbsp; 162 (54 × 3)</p>
            <p class="text-emerald-400 font-bold">+ 1080 ✓ (54 × 20)</p>
            <div class="border-b border-slate-700"></div>
            <p class="text-emerald-400 font-bold">&nbsp; 1242 ✓</p>
        `;
        rDesc.textContent = 'Fix: Insert the tens zero placeholder: 54 × 20 = 1,080. Correct sum = 1,242.';
    } else if (bugId === 2) {
        wBox.innerHTML = `
            <p class="text-slate-400">47 × 3 (carry 2)</p>
            <p class="text-rose-400 font-bold">• (4 + 2) × 3 = 6 × 3 = 18</p>
            <p class="text-rose-400 font-bold">• Recorded: 181 ❌</p>
        `;
        fDesc.textContent = 'Flaw: Added the carried 2 to the tens digit 4 BEFORE multiplying by 3!';

        rBox.innerHTML = `
            <p class="text-slate-400">47 × 3 (carry 2)</p>
            <p class="text-emerald-400 font-bold">• (4 × 3) + 2 = 12 + 2 = 14</p>
            <p class="text-emerald-400 font-bold">• Correct: 141 ✓</p>
        `;
        rDesc.textContent = 'Fix: Multiply place value first (4 × 3 = 12), then add carried 2 (12 + 2 = 14).';
    } else if (bugId === 3) {
        wBox.innerHTML = `
            <p class="text-slate-400">38 × 42</p>
            <p class="text-slate-300">&nbsp; &nbsp;76 (38 × 2)</p>
            <p class="text-rose-400 font-bold">+ 152 ❌ Shifted wrong</p>
            <div class="border-b border-slate-700"></div>
            <p class="text-rose-400 font-bold">&nbsp; 228 ❌</p>
        `;
        fDesc.textContent = 'Flaw: Multiplied 38 by 4 instead of 40 (4 tens = 1,520). Estimate: 40 × 40 = 1,600!';

        rBox.innerHTML = `
            <p class="text-slate-400">38 × 42</p>
            <p class="text-slate-300">&nbsp; &nbsp; 76 (38 × 2)</p>
            <p class="text-emerald-400 font-bold">+ 1520 ✓ (38 × 40)</p>
            <div class="border-b border-slate-700"></div>
            <p class="text-emerald-400 font-bold">&nbsp; 1596 ✓</p>
        `;
        rDesc.textContent = 'Fix: 38 × 40 = 1,520. Correct sum = 76 + 1,520 = 1,596.';
    }
    playSound('click');
}

// Sim 13: Derivative Facts Tree
function setSim13Deriv(type) {
    ['db', 'da', 'p1', 'm1', 't10'].forEach(t => {
        const btn = document.getElementById(`sim13_btn_${t}`);
        if (btn) btn.className = 'px-2.5 py-1 bg-slate-700 rounded text-xs font-mono font-bold';
    });

    const deriv = document.getElementById('sim13_derivation');
    const res = document.getElementById('sim13_result');

    if (type === 'double_b') {
        document.getElementById('sim13_btn_db').className = 'px-2.5 py-1 bg-teal-600 rounded text-xs font-mono font-bold';
        deriv.textContent = '17 × 46 = 17 × (23 × 2) = 391 × 2';
        res.textContent = '= 782';
    } else if (type === 'double_a') {
        document.getElementById('sim13_btn_da').className = 'px-2.5 py-1 bg-teal-600 rounded text-xs font-mono font-bold';
        deriv.textContent = '34 × 23 = (17 × 2) × 23 = 391 × 2';
        res.textContent = '= 782';
    } else if (type === 'plus_1') {
        document.getElementById('sim13_btn_p1').className = 'px-2.5 py-1 bg-teal-600 rounded text-xs font-mono font-bold';
        deriv.textContent = '17 × 24 = (17 × 23) + 17 = 391 + 17';
        res.textContent = '= 408';
    } else if (type === 'minus_1') {
        document.getElementById('sim13_btn_m1').className = 'px-2.5 py-1 bg-teal-600 rounded text-xs font-mono font-bold';
        deriv.textContent = '17 × 22 = (17 × 23) - 17 = 391 - 17';
        res.textContent = '= 374';
    } else if (type === 'times_10') {
        document.getElementById('sim13_btn_t10').className = 'px-2.5 py-1 bg-teal-600 rounded text-xs font-mono font-bold';
        deriv.textContent = '170 × 23 = (17 × 10) × 23 = 391 × 10';
        res.textContent = '= 3,910';
    }
    playSound('correct');
}

// Sim 14: King's Reward Growth Race
function updateSim14() {
    const day = parseInt(document.getElementById('sim14_day')?.value || 7, 10);
    document.getElementById('sim14_d_val').textContent = day;
    document.getElementById('sim14_day_lbl').textContent = `Day ${day} Comparison`;

    // Choice A: ₹ 100k daily
    const totA = day * 100000;

    // Choice B: 2 on day 1, doubling daily
    const dayB = Math.pow(2, day);
    const totB = Math.pow(2, day + 1) - 2;

    // Choice C: 1 on day 1, multiplying by 5 daily
    const dayC = Math.pow(5, day - 1);
    const totC = (Math.pow(5, day) - 1) / 4;

    document.getElementById('sim14_tot_a').textContent = `Total: ₹ ${totA.toLocaleString()}`;
    document.getElementById('sim14_day_b').textContent = `Today: ${dayB.toLocaleString()} coins`;
    document.getElementById('sim14_tot_b').textContent = `Total: ${totB.toLocaleString()} coins`;
    document.getElementById('sim14_day_c').textContent = `Today: ${dayC.toLocaleString()} coins`;
    document.getElementById('sim14_tot_c').textContent = `Total: ${totC.toLocaleString()} coins`;

    const verdict = document.getElementById('sim14_verdict');
    if (day <= 7) {
        verdict.textContent = `At Day ${day}: Choice A is currently ahead with ₹ ${totA.toLocaleString()}!`;
    } else {
        verdict.textContent = `At Day ${day}: Choice C explodes into the stratosphere with ${totC.toLocaleString()} coins! Multiplicative compounding triumphs!`;
    }

    const svg = document.getElementById('sim14_svg');
    if (svg) {
        svg.innerHTML = '';
        const maxVal = Math.max(totA, totC);
        const wA = Math.max(10, Math.min(320, (totA / maxVal) * 320));
        const wC = Math.max(10, Math.min(320, (totC / maxVal) * 320));

        // Bar A
        const bA = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        bA.setAttribute('x', '20');
        bA.setAttribute('y', '15');
        bA.setAttribute('width', wA);
        bA.setAttribute('height', '18');
        bA.setAttribute('fill', '#059669');
        bA.setAttribute('rx', '3');
        svg.appendChild(bA);

        // Bar C
        const bC = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        bC.setAttribute('x', '20');
        bC.setAttribute('y', '42');
        bC.setAttribute('width', wC);
        bC.setAttribute('height', '18');
        bC.setAttribute('fill', '#d97706');
        bC.setAttribute('rx', '3');
        svg.appendChild(bC);
    }
}

// Sim 15: Palindromic & 9s Patterns
function setSim15Mode(mode) {
    const content = document.getElementById('sim15_content');
    const bRep = document.getElementById('sim15_m_rep');
    const bNine = document.getElementById('sim15_m_nine');

    bRep.className = (mode === 'repunits') ? 'px-3 py-1 bg-indigo-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    bNine.className = (mode === 'nines') ? 'px-3 py-1 bg-indigo-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';

    if (!content) return;

    if (mode === 'repunits') {
        content.innerHTML = `
            <div class="space-y-1">
                <p>1 × 1 = <strong class="text-emerald-400">1</strong></p>
                <p>11 × 11 = <strong class="text-emerald-400">121</strong></p>
                <p>111 × 111 = <strong class="text-emerald-400">12321</strong></p>
                <p>1111 × 1111 = <strong class="text-emerald-400">1234321</strong></p>
                <p>11111 × 11111 = <strong class="text-emerald-400">123454321</strong></p>
                <p>111111 × 111111 = <strong class="text-emerald-400">12345654321</strong></p>
                <p>1111111 × 1111111 = <strong class="text-emerald-400">1234567654321</strong></p>
            </div>
        `;
    } else if (mode === 'nines') {
        content.innerHTML = `
            <div class="space-y-1">
                <p>1 × 9 + 2 = <strong class="text-amber-400">11</strong></p>
                <p>12 × 9 + 3 = <strong class="text-amber-400">111</strong></p>
                <p>123 × 9 + 4 = <strong class="text-amber-400">1111</strong></p>
                <p>1234 × 9 + 5 = <strong class="text-amber-400">11111</strong></p>
                <p>12345 × 9 + 6 = <strong class="text-amber-400">111111</strong></p>
                <p>123456 × 9 + 7 = <strong class="text-amber-400">1111111</strong></p>
                <p>1234567 × 9 + 8 = <strong class="text-amber-400">11111111</strong></p>
            </div>
        `;
    }
    playSound('click');
}

// Sim 16: Algebraic Bridge & Tournament Ledger
function setSim16Tab(tab) {
    const body = document.getElementById('sim16_body');
    const bAlg = document.getElementById('sim16_t_alg');
    const bTour = document.getElementById('sim16_t_tour');

    bAlg.className = (tab === 'algebra') ? 'px-3 py-1 bg-teal-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    bTour.className = (tab === 'tournament') ? 'px-3 py-1 bg-teal-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';

    if (!body) return;

    if (tab === 'algebra') {
        body.innerHTML = `
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span>Base Number (n): <strong id="sim16_n_val" class="text-amber-400">67</strong></span>
                    <input type="range" id="sim16_n" min="20" max="90" value="67" oninput="updateSim16Alg()" class="w-48 accent-amber-400">
                </div>
                <div class="p-3 bg-slate-900 rounded-lg space-y-1 font-mono text-center">
                    <p class="text-slate-400">Base Square: n² = <strong id="sim16_sq" class="text-slate-200">67 × 67 = 4,489</strong></p>
                    <p class="text-emerald-400 font-bold text-sm" id="sim16_next">n × (n + 1) = 4,489 + 67 = 4,556</p>
                    <p class="text-cyan-400 font-bold text-sm" id="sim16_prev">n × (n - 1) = 4,489 - 67 = 4,422</p>
                </div>
            </div>
        `;
        updateSim16Alg();
    } else if (tab === 'tournament') {
        body.innerHTML = `
            <div class="space-y-2">
                <div class="flex justify-between items-center">
                    <span>Teams (18 players/team): <strong id="sim16_t_val" class="text-cyan-400">16</strong></span>
                    <input type="range" id="sim16_tm" min="8" max="24" value="16" oninput="updateSim16Tour()" class="w-32 accent-cyan-400">
                </div>
                <div class="flex justify-between items-center">
                    <span>Spectator Tickets Sold (₹ 65 each): <strong id="sim16_tk_val" class="text-amber-400">450</strong></span>
                    <input type="range" id="sim16_tk" min="100" max="800" step="50" value="450" oninput="updateSim16Tour()" class="w-32 accent-amber-400">
                </div>
                <div class="p-3 bg-slate-900 rounded-lg space-y-1 font-mono text-center pt-2">
                    <p>Total Athletes: <strong id="sim16_ath" class="text-cyan-300">288 players</strong></p>
                    <p>Ticket Sales: <strong id="sim16_rev" class="text-amber-300">₹ 29,250</strong></p>
                    <p>Expenses: ₹ 12,000</p>
                    <p class="text-emerald-400 font-bold text-sm pt-1 border-t border-slate-700">Net Tournament Profit: <span id="sim16_net">₹ 17,250</span></p>
                </div>
            </div>
        `;
        updateSim16Tour();
    }
    playSound('click');
}

function updateSim16Alg() {
    const n = parseInt(document.getElementById('sim16_n')?.value || 67, 10);
    document.getElementById('sim16_n_val').textContent = n;

    const sq = n * n;
    const nextProd = sq + n;
    const prevProd = sq - n;

    document.getElementById('sim16_sq').textContent = `${n} × ${n} = ${sq.toLocaleString()}`;
    document.getElementById('sim16_next').textContent = `${n} × ${n + 1} = ${sq.toLocaleString()} + ${n} = ${nextProd.toLocaleString()}`;
    document.getElementById('sim16_prev').textContent = `${n} × ${n - 1} = ${sq.toLocaleString()} - ${n} = ${prevProd.toLocaleString()}`;
}

function updateSim16Tour() {
    const tm = parseInt(document.getElementById('sim16_tm')?.value || 16, 10);
    const tk = parseInt(document.getElementById('sim16_tk')?.value || 450, 10);

    document.getElementById('sim16_t_val').textContent = tm;
    document.getElementById('sim16_tk_val').textContent = tk;

    const ath = tm * 18;
    const rev = tk * 65;
    const net = rev - 12000;

    document.getElementById('sim16_ath').textContent = `${ath} players`;
    document.getElementById('sim16_rev').textContent = `₹ ${rev.toLocaleString()}`;
    document.getElementById('sim16_net').textContent = `₹ ${net.toLocaleString()}`;
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    initVoices();
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = initVoices;
    }
    goToSlide(1);

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') nextSlide();
        else if (e.key === 'ArrowLeft') prevSlide();
        else if (e.key === 'Escape') closeSolutionModal();
    });
});
'''


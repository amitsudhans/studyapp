# -*- coding: utf-8 -*-
"""
JavaScript engine for NCERT Class 5 Mathematics - Chapter 7: Shapes and Patterns
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
        case 1: setSim1Weave('plain'); break;
        case 2: setSim2Tile('square'); break;
        case 3: setSim3Mode('pentagon'); break;
        case 4: setSim4Type('equilateral'); break;
        case 5: updateSim5(); break;
        case 6: updateSim6(); break;
        case 7: setSim7Shape('square'); break;
        case 8: setSim8Riddle(1); break;
        case 9: setSim9Step(1); break;
        case 10: updateSim10(); break;
        case 11: setSim11Preset('star5'); break;
        case 12: setSim12Net('cross'); break;
        case 13: setSim13Filter(3); break;
        case 14: resetSim14(); break;
        case 15: setSim15Solid('icosa'); break;
        case 16: setSim16Model('square'); break;
    }
}

// Sim 1: Paper Weaving Simulator
function setSim1Weave(mode) {
    ['plain', 'twill', 'basket'].forEach(m => {
        const btn = document.getElementById(`sim1_b_${m}`);
        if (btn) btn.className = (m === mode) ? 'px-3 py-1 bg-indigo-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    });

    const modeLabel = document.getElementById('sim1_weave_mode');
    const desc = document.getElementById('sim1_desc');
    const svg = document.getElementById('sim1_svg');
    if (!svg) return;
    svg.innerHTML = '';

    const cols = 8, rows = 6;
    const w = 300 / cols, h = 150 / rows;
    const startX = 10, startY = 15;

    if (mode === 'plain') {
        if (modeLabel) modeLabel.textContent = 'Plain Weave (1 Over, 1 Under)';
        if (desc) desc.textContent = 'Row 1: Over-Under-Over-Under | Row 2: Under-Over-Under-Over (Interlocking Tension)';
    } else if (mode === 'twill') {
        if (modeLabel) modeLabel.textContent = 'Twill Weave (2 Over, 1 Under)';
        if (desc) desc.textContent = 'Each row shifts 1 step to the right, generating a dynamic diagonal chevron texture.';
    } else if (mode === 'basket') {
        if (modeLabel) modeLabel.textContent = 'Basket Weave (2 Over, 2 Under)';
        if (desc) desc.textContent = 'Pairs of rows and columns alternate, creating bold checkerboard fabric blocks.';
    }

    // Draw background warp (cream paper vertical strips)
    for (let c = 0; c < cols; c++) {
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', startX + c * w);
        rect.setAttribute('y', startY);
        rect.setAttribute('width', w - 4);
        rect.setAttribute('height', rows * h);
        rect.setAttribute('fill', '#fde68a'); // amber-200
        rect.setAttribute('rx', '2');
        svg.appendChild(rect);
    }

    // Draw weft (horizontal colored strips)
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            let isOver = false;
            if (mode === 'plain') {
                isOver = ((r + c) % 2 === 0);
            } else if (mode === 'twill') {
                isOver = ((r + c) % 3 !== 0);
            } else if (mode === 'basket') {
                const br = Math.floor(r / 2);
                const bc = Math.floor(c / 2);
                isOver = ((br + bc) % 2 === 0);
            }

            if (isOver) {
                const patch = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                patch.setAttribute('x', startX + c * w - 1);
                patch.setAttribute('y', startY + r * h);
                patch.setAttribute('width', w - 2);
                patch.setAttribute('height', h - 3);
                patch.setAttribute('fill', r % 2 === 0 ? '#4f46e5' : '#0284c7');
                patch.setAttribute('rx', '2');
                svg.appendChild(patch);
            }
        }
    }
    playSound('click');
}

// Sim 2: 360° Vertex Tessellation Tester
let sim2CurrentShape = 'square';
let sim2TilesCount = 0;
function setSim2Tile(shape) {
    sim2CurrentShape = shape;
    sim2TilesCount = 0;
    ['sq', 'tri', 'hex'].forEach(s => {
        const btn = document.getElementById(`sim2_b_${s}`);
        if (btn) btn.className = (s === (shape === 'square' ? 'sq' : (shape === 'triangle' ? 'tri' : 'hex'))) ? 'px-3 py-1 bg-emerald-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    });
    renderSim2();
    playSound('click');
}

function addSim2Tile() {
    const angleMap = { square: 90, triangle: 60, hexagon: 120 };
    const maxMap = { square: 4, triangle: 6, hexagon: 3 };
    const maxTiles = maxMap[sim2CurrentShape];

    if (sim2TilesCount < maxTiles) {
        sim2TilesCount++;
        renderSim2();
        playSound('click');
    } else {
        sim2TilesCount = 1;
        renderSim2();
        playSound('click');
    }
}

function renderSim2() {
    const angleMap = { square: 90, triangle: 60, hexagon: 120 };
    const maxMap = { square: 4, triangle: 6, hexagon: 3 };
    const step = angleMap[sim2CurrentShape];
    const total = sim2TilesCount * step;

    document.getElementById('sim2_angle_dial').textContent = `Current Angle: ${total}° / 360°`;
    const res = document.getElementById('sim2_result');
    const svg = document.getElementById('sim2_svg');
    if (!svg) return;
    svg.innerHTML = '';

    if (total === 360) {
        res.innerHTML = `<span class="text-emerald-400 font-bold">✓ 360° Completed!</span> Exactly ${sim2TilesCount} ${sim2CurrentShape}s tile the plane with ZERO gaps!`;
        playSound('correct');
    } else {
        res.innerHTML = `Placed ${sim2TilesCount} tile(s) (${total}°). Gap remaining: <strong class="text-cyan-300">${360 - total}°</strong>.`;
    }

    // Draw central vertex point
    const cx = 120, cy = 90;
    const centerDot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    centerDot.setAttribute('cx', cx);
    centerDot.setAttribute('cy', cy);
    centerDot.setAttribute('r', '4');
    centerDot.setAttribute('fill', '#f59e0b');

    // Draw tiles as sectors or polygons around center
    for (let i = 0; i < sim2TilesCount; i++) {
        const startA = (i * step) * (Math.PI / 180);
        const endA = ((i + 1) * step) * (Math.PI / 180);
        const r = 60;

        const x1 = cx + r * Math.cos(startA);
        const y1 = cy + r * Math.sin(startA);
        const x2 = cx + r * Math.cos(endA);
        const y2 = cy + r * Math.sin(endA);

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', `M ${cx},${cy} L ${x1},${y1} A ${r},${r} 0 0 1 ${x2},${y2} Z`);
        path.setAttribute('fill', '#059669');
        path.setAttribute('stroke', '#34d399');
        path.setAttribute('stroke-width', '2');
        svg.appendChild(path);
    }
    svg.appendChild(centerDot);
}

// Sim 3: Pentagon Gap vs Octagon-Square
function setSim3Mode(mode) {
    const bPent = document.getElementById('sim3_b_pent');
    const bOct = document.getElementById('sim3_b_oct');
    bPent.className = (mode === 'pentagon') ? 'px-3 py-1 bg-rose-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    bOct.className = (mode === 'octsq') ? 'px-3 py-1 bg-rose-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';

    const svg = document.getElementById('sim3_svg');
    const text = document.getElementById('sim3_text');
    if (!svg || !text) return;
    svg.innerHTML = '';

    const cx = 130, cy = 85;

    if (mode === 'pentagon') {
        text.innerHTML = `3 × 108° = 324°. <span class="text-rose-400 font-bold">Angle Gap = 36°</span> (Too narrow for a 4th pentagon ➔ Overlap!)`;
        // 3 sectors of 108 deg
        for (let i = 0; i < 3; i++) {
            const startA = (i * 108) * (Math.PI / 180);
            const endA = ((i + 1) * 108) * (Math.PI / 180);
            const r = 55;
            const x1 = cx + r * Math.cos(startA);
            const y1 = cy + r * Math.sin(startA);
            const x2 = cx + r * Math.cos(endA);
            const y2 = cy + r * Math.sin(endA);

            const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            path.setAttribute('d', `M ${cx},${cy} L ${x1},${y1} A ${r},${r} 0 0 1 ${x2},${y2} Z`);
            path.setAttribute('fill', '#e11d48');
            path.setAttribute('stroke', '#fda4af');
            path.setAttribute('stroke-width', '1.5');
            svg.appendChild(path);
        }
        // Gap indicator
        const gapPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        const gStart = 324 * (Math.PI / 180);
        const gEnd = 360 * (Math.PI / 180);
        const gx1 = cx + 55 * Math.cos(gStart);
        const gy1 = cy + 55 * Math.sin(gStart);
        const gx2 = cx + 55 * Math.cos(gEnd);
        const gy2 = cy + 55 * Math.sin(gEnd);
        gapPath.setAttribute('d', `M ${cx},${cy} L ${gx1},${gy1} A 55,55 0 0 1 ${gx2},${gy2} Z`);
        gapPath.setAttribute('fill', 'rgba(251, 191, 36, 0.4)');
        gapPath.setAttribute('stroke', '#fbbf24');
        gapPath.setAttribute('stroke-dasharray', '3,3');
        svg.appendChild(gapPath);
    } else {
        text.innerHTML = `2 Octagons (135° + 135° = 270°) + 1 Square (90°) = <span class="text-emerald-400 font-bold">360° Perfect Fit!</span>`;
        // 2 octagons of 135
        for (let i = 0; i < 2; i++) {
            const startA = (i * 135) * (Math.PI / 180);
            const endA = ((i + 1) * 135) * (Math.PI / 180);
            const r = 55;
            const x1 = cx + r * Math.cos(startA);
            const y1 = cy + r * Math.sin(startA);
            const x2 = cx + r * Math.cos(endA);
            const y2 = cy + r * Math.sin(endA);

            const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            path.setAttribute('d', `M ${cx},${cy} L ${x1},${y1} A ${r},${r} 0 0 1 ${x2},${y2} Z`);
            path.setAttribute('fill', '#4f46e5');
            path.setAttribute('stroke', '#a5b4fc');
            path.setAttribute('stroke-width', '1.5');
            svg.appendChild(path);
        }
        // 1 square of 90
        const startA = 270 * (Math.PI / 180);
        const endA = 360 * (Math.PI / 180);
        const r = 55;
        const x1 = cx + r * Math.cos(startA);
        const y1 = cy + r * Math.sin(startA);
        const x2 = cx + r * Math.cos(endA);
        const y2 = cy + r * Math.sin(endA);

        const sqPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        sqPath.setAttribute('d', `M ${cx},${cy} L ${x1},${y1} A ${r},${r} 0 0 1 ${x2},${y2} Z`);
        sqPath.setAttribute('fill', '#0284c7');
        sqPath.setAttribute('stroke', '#38bdf8');
        sqPath.setAttribute('stroke-width', '2');
        svg.appendChild(sqPath);
    }
    playSound('click');
}

// Sim 4: Triangle Classifier & Rhombus Dissection
let sim4RhombusActive = false;
function setSim4Type(type) {
    sim4RhombusActive = false;
    ['eq', 'iso', 'sca'].forEach(t => {
        const btn = document.getElementById(`sim4_b_${t}`);
        if (btn) btn.className = (t === (type === 'equilateral' ? 'eq' : (type === 'isosceles' ? 'iso' : 'sca'))) ? 'px-3 py-1 bg-cyan-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    });
    document.getElementById('sim4_b_rhomb').className = 'px-3 py-1 bg-slate-700 rounded font-bold';

    const svg = document.getElementById('sim4_svg');
    const text = document.getElementById('sim4_text');
    if (!svg || !text) return;
    svg.innerHTML = '';

    if (type === 'equilateral') {
        text.textContent = 'Equilateral: 3 equal sides (8 cm each), 3 equal angles (60° each), 3 lines of symmetry.';
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', '130,25 70,130 190,130');
        poly.setAttribute('fill', '#0284c7');
        poly.setAttribute('stroke', '#38bdf8');
        poly.setAttribute('stroke-width', '2');
        svg.appendChild(poly);
    } else if (type === 'isosceles') {
        text.textContent = 'Isosceles: 2 equal sides, 2 equal base angles (70° each). Folding along dashed axis matches edges!';
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', '130,15 85,135 175,135');
        poly.setAttribute('fill', '#059669');
        poly.setAttribute('stroke', '#34d399');
        poly.setAttribute('stroke-width', '2');
        svg.appendChild(poly);

        const symLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        symLine.setAttribute('x1', '130'); symLine.setAttribute('y1', '15');
        symLine.setAttribute('x2', '130'); symLine.setAttribute('y2', '135');
        symLine.setAttribute('stroke', '#f59e0b');
        symLine.setAttribute('stroke-width', '2');
        symLine.setAttribute('stroke-dasharray', '4,4');
        svg.appendChild(symLine);
    } else if (type === 'scalene') {
        text.textContent = 'Scalene: All 3 sides are unequal (5 cm, 7 cm, 9 cm). All 3 angles are unequal (40°, 60°, 80°).';
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', '90,25 50,135 210,120');
        poly.setAttribute('fill', '#e11d48');
        poly.setAttribute('stroke', '#fda4af');
        poly.setAttribute('stroke-width', '2');
        svg.appendChild(poly);
    }
    playSound('click');
}

function toggleSim4Rhombus() {
    sim4RhombusActive = true;
    ['eq', 'iso', 'sca'].forEach(t => {
        document.getElementById(`sim4_b_${t}`).className = 'px-3 py-1 bg-slate-700 rounded font-bold';
    });
    document.getElementById('sim4_b_rhomb').className = 'px-3 py-1 bg-amber-600 rounded font-bold';

    const svg = document.getElementById('sim4_svg');
    const text = document.getElementById('sim4_text');
    if (!svg || !text) return;
    svg.innerHTML = '';

    text.textContent = 'Rhombus Dissection: Perpendicular diagonals divide the rhombus into 4 identical right-angled triangles!';

    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', '130,20 210,80 130,140 50,80');
    poly.setAttribute('fill', 'rgba(217, 119, 6, 0.4)');
    poly.setAttribute('stroke', '#f59e0b');
    poly.setAttribute('stroke-width', '2');
    svg.appendChild(poly);

    // Diagonals
    const d1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    d1.setAttribute('x1', '130'); d1.setAttribute('y1', '20');
    d1.setAttribute('x2', '130'); d1.setAttribute('y2', '140');
    d1.setAttribute('stroke', '#38bdf8'); d1.setAttribute('stroke-width', '2');
    svg.appendChild(d1);

    const d2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    d2.setAttribute('x1', '50'); d2.setAttribute('y1', '80');
    d2.setAttribute('x2', '210'); d2.setAttribute('y2', '80');
    d2.setAttribute('stroke', '#38bdf8'); d2.setAttribute('stroke-width', '2');
    svg.appendChild(d2);

    playSound('correct');
}

// Sim 5: Kite Geometry
function updateSim5() {
    const topW = parseInt(document.getElementById('sim5_top')?.value || 6, 10);
    const tailW = parseInt(document.getElementById('sim5_tail')?.value || 14, 10);

    document.getElementById('sim5_top_val').textContent = `${topW} cm`;
    document.getElementById('sim5_tail_val').textContent = `${tailW} cm`;

    const svg = document.getElementById('sim5_svg');
    if (!svg) return;
    svg.innerHTML = '';

    const cx = 130, topY = 20;
    const crossY = topY + topW * 6;
    const bottomY = crossY + tailW * 5;
    const spanX = topW * 7;

    const kitePoly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    kitePoly.setAttribute('points', `${cx},${topY} ${cx + spanX},${crossY} ${cx},${bottomY} ${cx - spanX},${crossY}`);
    kitePoly.setAttribute('fill', 'rgba(245, 158, 11, 0.3)');
    kitePoly.setAttribute('stroke', '#f59e0b');
    kitePoly.setAttribute('stroke-width', '2');
    svg.appendChild(kitePoly);

    // Diagonals
    const dVert = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    dVert.setAttribute('x1', cx); dVert.setAttribute('y1', topY);
    dVert.setAttribute('x2', cx); dVert.setAttribute('y2', bottomY);
    dVert.setAttribute('stroke', '#38bdf8'); dVert.setAttribute('stroke-width', '2');
    svg.appendChild(dVert);

    const dHoriz = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    dHoriz.setAttribute('x1', cx - spanX); dHoriz.setAttribute('y1', crossY);
    dHoriz.setAttribute('x2', cx + spanX); dHoriz.setAttribute('y2', crossY);
    dHoriz.setAttribute('stroke', '#38bdf8'); dHoriz.setAttribute('stroke-width', '2');
    svg.appendChild(dHoriz);
}

// Sim 6: Quadrilateral Morphing Machine
function updateSim6() {
    const ang = parseInt(document.getElementById('sim6_ang')?.value || 65, 10);
    const rat = parseInt(document.getElementById('sim6_rat')?.value || 15, 10) / 10;

    document.getElementById('sim6_ang_val').textContent = `${ang}°`;
    document.getElementById('sim6_rat_val').textContent = `${rat.toFixed(1)} : 1`;

    const nameLbl = document.getElementById('sim6_shape_name');
    const ruleLbl = document.getElementById('sim6_rule');
    const isRight = (ang === 90);
    const isEqual = (rat === 1.0);

    let shapeName = '';
    let explanation = '';
    if (!isRight && !isEqual) {
        shapeName = 'Parallelogram';
        explanation = 'Opposite sides equal, opposite angles equal, diagonals unequal.';
    } else if (!isRight && isEqual) {
        shapeName = 'Rhombus';
        explanation = 'All 4 sides equal, diagonals cross at perpendicular 90° right angles.';
    } else if (isRight && !isEqual) {
        shapeName = 'Rectangle';
        explanation = 'Opposite sides equal, 4 right angles (90°), equal diagonals.';
    } else if (isRight && isEqual) {
        shapeName = 'Square';
        explanation = 'King of Quadrilaterals: 4 equal sides, 4 right angles, equal perpendicular diagonals!';
    }

    if (nameLbl) nameLbl.textContent = shapeName;
    if (ruleLbl) ruleLbl.textContent = `${shapeName}: ${explanation}`;

    const svg = document.getElementById('sim6_svg');
    if (!svg) return;
    svg.innerHTML = '';

    const cx = 130, cy = 70;
    const h = 50;
    const w = h * rat;
    const rad = ang * (Math.PI / 180);
    const dx = h / Math.tan(rad);

    const p1x = cx - w/2 - dx/2; const p1y = cy + h/2;
    const p2x = cx + w/2 - dx/2; const p2y = cy + h/2;
    const p3x = cx + w/2 + dx/2; const p3y = cy - h/2;
    const p4x = cx - w/2 + dx/2; const p4y = cy - h/2;

    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${p1x},${p1y} ${p2x},${p2y} ${p3x},${p3y} ${p4x},${p4y}`);
    poly.setAttribute('fill', isRight ? (isEqual ? '#059669' : '#0284c7') : (isEqual ? '#d97706' : '#4f46e5'));
    poly.setAttribute('stroke', '#ffffff');
    poly.setAttribute('stroke-width', '2');
    svg.appendChild(poly);
}

// Sim 7: Tangram Dissection Sandbox
function setSim7Shape(mode) {
    ['sq', 'ssq', 'mtri', 'para'].forEach(m => {
        const btn = document.getElementById(`sim7_b_${m}`);
        if (btn) btn.className = (m === (mode === 'square' ? 'sq' : (mode === 'small_sq' ? 'ssq' : (mode === 'med_tri' ? 'mtri' : 'para')))) ? 'px-3 py-1 bg-violet-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    });

    const svg = document.getElementById('sim7_svg');
    const desc = document.getElementById('sim7_desc');
    if (!svg || !desc) return;
    svg.innerHTML = '';

    if (mode === 'square') {
        desc.textContent = '7 Tans combine into 1 Big Square with zero overlaps and zero gaps (Conservation of Area).';
        // Draw 7 pieces of standard tangram
        const bg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        bg.setAttribute('x', '40'); bg.setAttribute('y', '20'); bg.setAttribute('width', '120'); bg.setAttribute('height', '120');
        bg.setAttribute('fill', '#1e1b4b'); bg.setAttribute('stroke', '#818cf8'); bg.setAttribute('stroke-width', '2');
        svg.appendChild(bg);

        // Piece lines
        const lines = [
            ['40', '20', '160', '140'],
            ['40', '140', '100', '80'],
            ['100', '80', '160', '80'],
            ['100', '80', '100', '140'],
            ['130', '50', '130', '110']
        ];
        lines.forEach(l => {
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', l[0]); line.setAttribute('y1', l[1]);
            line.setAttribute('x2', l[2]); line.setAttribute('y2', l[3]);
            line.setAttribute('stroke', '#38bdf8'); line.setAttribute('stroke-width', '2');
            svg.appendChild(line);
        });
    } else if (mode === 'small_sq') {
        desc.textContent = '2 Small Triangles joined along their hypotenuse form the small square!';
        const poly1 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly1.setAttribute('points', '70,50 130,50 70,110');
        poly1.setAttribute('fill', '#e11d48'); poly1.setAttribute('stroke', '#fda4af'); poly1.setAttribute('stroke-width', '2');
        svg.appendChild(poly1);

        const poly2 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly2.setAttribute('points', '130,50 130,110 70,110');
        poly2.setAttribute('fill', '#0284c7'); poly2.setAttribute('stroke', '#38bdf8'); poly2.setAttribute('stroke-width', '2');
        svg.appendChild(poly2);
    } else if (mode === 'med_tri') {
        desc.textContent = '2 Small Triangles joined along matching legs form the medium triangle!';
        const poly1 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly1.setAttribute('points', '100,30 100,110 40,110');
        poly1.setAttribute('fill', '#e11d48'); poly1.setAttribute('stroke', '#fda4af'); poly1.setAttribute('stroke-width', '2');
        svg.appendChild(poly1);

        const poly2 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly2.setAttribute('points', '100,30 160,110 100,110');
        poly2.setAttribute('fill', '#059669'); poly2.setAttribute('stroke', '#34d399'); poly2.setAttribute('stroke-width', '2');
        svg.appendChild(poly2);
    } else if (mode === 'para') {
        desc.textContent = '2 Small Triangles joined along reversed legs form the parallelogram!';
        const poly1 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly1.setAttribute('points', '50,50 110,50 70,110');
        poly1.setAttribute('fill', '#d97706'); poly1.setAttribute('stroke', '#fbbf24'); poly1.setAttribute('stroke-width', '2');
        svg.appendChild(poly1);

        const poly2 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly2.setAttribute('points', '110,50 130,110 70,110');
        poly2.setAttribute('fill', '#4f46e5'); poly2.setAttribute('stroke', '#a5b4fc'); poly2.setAttribute('stroke-width', '2');
        svg.appendChild(poly2);
    }
    playSound('click');
}

// Sim 8: Which Shape Am I?
let sim8CurrentRiddle = 1;
const sim8Riddles = {
    1: { clue: '"I have 4 equal sides, 4 right angles, and equal diagonals."', ans: 'Square' },
    2: { clue: '"I have 4 sides. Opposite sides are equal, all angles are 90°, and diagonals are equal."', ans: 'Rectangle' },
    3: { clue: '"I have 4 equal sides, opposite angles are equal, but NO right angles."', ans: 'Rhombus' },
    4: { clue: '"Adjacent pairs of sides are equal, diagonals meet at 90°, exactly 1 line of symmetry."', ans: 'Kite' }
};

function setSim8Riddle(num) {
    sim8CurrentRiddle = num;
    [1, 2, 3, 4].forEach(n => {
        const btn = document.getElementById(`sim8_b_r${n}`);
        if (btn) btn.className = (n === num) ? 'px-2.5 py-1 bg-rose-600 rounded font-bold' : 'px-2.5 py-1 bg-slate-700 rounded font-bold';
    });
    document.getElementById('sim8_riddle_tag').textContent = `Riddle ${num} of 4`;
    document.getElementById('sim8_clue_box').textContent = sim8Riddles[num].clue;
    document.getElementById('sim8_feedback').textContent = '';
    playSound('click');
}

function guessSim8(shape) {
    const correct = sim8Riddles[sim8CurrentRiddle].ans;
    const fb = document.getElementById('sim8_feedback');
    if (shape === correct) {
        fb.innerHTML = `<span class="text-emerald-400">✓ Correct!</span> You deduced the <strong>${correct}</strong>!`;
        playSound('correct');
    } else {
        fb.innerHTML = `<span class="text-rose-400">✗ Not quite.</span> Re-read the clues and test again!`;
        playSound('incorrect');
    }
}

// Sim 9: Origami Kite Step Folder
function setSim9Step(step) {
    [1, 2, 3, 4].forEach(s => {
        const btn = document.getElementById(`sim9_b_s${s}`);
        if (btn) btn.className = (s === step) ? 'px-2.5 py-1 bg-amber-600 rounded font-bold' : 'px-2.5 py-1 bg-slate-700 rounded font-bold';
    });

    const tag = document.getElementById('sim9_step_tag');
    const desc = document.getElementById('sim9_desc');
    const svg = document.getElementById('sim9_svg');
    if (!svg || !tag || !desc) return;
    svg.innerHTML = '';

    const cx = 120, cy = 90;

    if (step === 1) {
        tag.textContent = 'Step 1: Square Paper';
        desc.textContent = 'Start with a square sheet of paper with 4 equal sides and 90° right angles.';
        const sq = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        sq.setAttribute('x', '60'); sq.setAttribute('y', '30'); sq.setAttribute('width', '120'); sq.setAttribute('height', '120');
        sq.setAttribute('fill', '#d97706'); sq.setAttribute('stroke', '#fbbf24'); sq.setAttribute('stroke-width', '2');
        svg.appendChild(sq);
    } else if (step === 2) {
        tag.textContent = 'Step 2: Diagonal Crease';
        desc.textContent = 'Fold diagonally corner-to-corner and unfold to create the central symmetry axis.';
        const sq = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        sq.setAttribute('x', '60'); sq.setAttribute('y', '30'); sq.setAttribute('width', '120'); sq.setAttribute('height', '120');
        sq.setAttribute('fill', '#d97706'); sq.setAttribute('stroke', '#fbbf24'); sq.setAttribute('stroke-width', '2');
        svg.appendChild(sq);

        const d = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        d.setAttribute('x1', '60'); d.setAttribute('y1', '30');
        d.setAttribute('x2', '180'); d.setAttribute('y2', '150');
        d.setAttribute('stroke', '#38bdf8'); d.setAttribute('stroke-width', '2'); d.setAttribute('stroke-dasharray', '4,4');
        svg.appendChild(d);
    } else if (step === 3) {
        tag.textContent = 'Step 3: Left Wing Fold';
        desc.textContent = 'Fold top-left edge flush along the diagonal crease to create the first kite wing.';
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', '60,30 180,30 180,150 120,90');
        poly.setAttribute('fill', '#d97706'); poly.setAttribute('stroke', '#fbbf24'); poly.setAttribute('stroke-width', '2');
        svg.appendChild(poly);
    } else if (step === 4) {
        tag.textContent = 'Step 4: Right Wing Fold (Complete Kite!)';
        desc.textContent = 'Both edges folded along the diagonal crease: 2 pairs of adjacent equal sides meet at 90°!';
        const kite = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        kite.setAttribute('points', '120,15 165,80 120,165 75,80');
        kite.setAttribute('fill', '#059669'); kite.setAttribute('stroke', '#34d399'); kite.setAttribute('stroke-width', '2');
        svg.appendChild(kite);

        // Struts
        const l1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        l1.setAttribute('x1', '120'); l1.setAttribute('y1', '15'); l1.setAttribute('x2', '120'); l1.setAttribute('y2', '165');
        l1.setAttribute('stroke', '#ffffff'); l1.setAttribute('stroke-width', '1.5');
        svg.appendChild(l1);

        const l2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        l2.setAttribute('x1', '75'); l2.setAttribute('y1', '80'); l2.setAttribute('x2', '165'); l2.setAttribute('y2', '80');
        l2.setAttribute('stroke', '#ffffff'); l2.setAttribute('stroke-width', '1.5');
        svg.appendChild(l2);
    }
    playSound('click');
}

// Sim 10: Inscribed Quadrilateral Constructor
function setSim10Angle(ang) {
    document.getElementById('sim10_ang').value = ang;
    updateSim10();
    playSound('correct');
}

function updateSim10() {
    const ang = parseInt(document.getElementById('sim10_ang')?.value || 60, 10);
    document.getElementById('sim10_ang_val').textContent = `${ang}°`;

    const tag = document.getElementById('sim10_inscribed_tag');
    const desc = document.getElementById('sim10_desc');
    const isSquare = (ang === 90);

    if (tag) tag.textContent = isSquare ? 'Inscribed Square (90°)' : 'Inscribed Rectangle';
    if (desc) desc.textContent = isSquare ? 'At 90°: Equal diameters cross perpendicularly ➔ Perfect Square!' : `At ${ang}°: Equal diameters bisecting at centre ➔ Rectangle!`;

    const svg = document.getElementById('sim10_svg');
    if (!svg) return;
    svg.innerHTML = '';

    const cx = 120, cy = 90, r = 65;

    // Draw circle
    const circ = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circ.setAttribute('cx', cx); circ.setAttribute('cy', cy); circ.setAttribute('r', r);
    circ.setAttribute('fill', 'none'); circ.setAttribute('stroke', '#334155'); circ.setAttribute('stroke-width', '2');
    svg.appendChild(circ);

    // Diameters
    const a1 = 0;
    const a2 = (180 - ang) * (Math.PI / 180);

    const x1 = cx + r * Math.cos(a1); const y1 = cy - r * Math.sin(a1);
    const x2 = cx - r * Math.cos(a1); const y2 = cy + r * Math.sin(a1);
    const x3 = cx + r * Math.cos(a2); const y3 = cy - r * Math.sin(a2);
    const x4 = cx - r * Math.cos(a2); const y4 = cy + r * Math.sin(a2);

    // Inscribed quad
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${x1},${y1} ${x3},${y3} ${x2},${y2} ${x4},${y4}`);
    poly.setAttribute('fill', isSquare ? 'rgba(5, 150, 105, 0.4)' : 'rgba(2, 132, 199, 0.3)');
    poly.setAttribute('stroke', isSquare ? '#34d399' : '#38bdf8');
    poly.setAttribute('stroke-width', '2');
    svg.appendChild(poly);

    // Diameter lines
    const d1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    d1.setAttribute('x1', x1); d1.setAttribute('y1', y1); d1.setAttribute('x2', x2); d1.setAttribute('y2', y2);
    d1.setAttribute('stroke', '#f59e0b'); d1.setAttribute('stroke-width', '1.5');
    svg.appendChild(d1);

    const d2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    d2.setAttribute('x1', x3); d2.setAttribute('y1', y3); d2.setAttribute('x2', x4); d2.setAttribute('y2', y4);
    d2.setAttribute('stroke', '#f59e0b'); d2.setAttribute('stroke-width', '1.5');
    svg.appendChild(d2);
}

// Sim 11: 24-Point String Art Designer
let sim11Mode = 'jump';
function setSim11Preset(preset) {
    if (preset === 'star5') {
        sim11Mode = 'jump';
        document.getElementById('sim11_k').value = 5;
    } else if (preset === 'star7') {
        sim11Mode = 'jump';
        document.getElementById('sim11_k').value = 7;
    } else if (preset === 'cardioid') {
        sim11Mode = 'cardioid';
    }
    updateSim11();
    playSound('click');
}

function updateSim11() {
    const k = parseInt(document.getElementById('sim11_k')?.value || 5, 10);
    document.getElementById('sim11_k_val').textContent = k;
    const ruleTag = document.getElementById('sim11_rule_tag');
    if (ruleTag) {
        ruleTag.textContent = (sim11Mode === 'cardioid') ? 'Caustic: n ➔ 2n (mod 24)' : `Step Jump: +${k}`;
    }

    const svg = document.getElementById('sim11_svg');
    if (!svg) return;
    svg.innerHTML = '';

    const cx = 120, cy = 100, r = 80;
    const nPts = 24;
    const pts = [];

    for (let i = 0; i < nPts; i++) {
        const a = (i * (360 / nPts) - 90) * (Math.PI / 180);
        pts.push({ x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) });
    }

    // Outer circle
    const circ = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circ.setAttribute('cx', cx); circ.setAttribute('cy', cy); circ.setAttribute('r', r);
    circ.setAttribute('fill', 'none'); circ.setAttribute('stroke', '#334155'); circ.setAttribute('stroke-width', '1');
    svg.appendChild(circ);

    // Chords
    if (sim11Mode === 'jump') {
        for (let i = 0; i < nPts; i++) {
            const next = (i + k) % nPts;
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', pts[i].x); line.setAttribute('y1', pts[i].y);
            line.setAttribute('x2', pts[next].x); line.setAttribute('y2', pts[next].y);
            line.setAttribute('stroke', '#818cf8'); line.setAttribute('stroke-width', '1.2');
            svg.appendChild(line);
        }
    } else {
        for (let i = 0; i < nPts; i++) {
            const next = (2 * i) % nPts;
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', pts[i].x); line.setAttribute('y1', pts[i].y);
            line.setAttribute('x2', pts[next].x); line.setAttribute('y2', pts[next].y);
            line.setAttribute('stroke', '#f43f5e'); line.setAttribute('stroke-width', '1.2');
            svg.appendChild(line);
        }
    }

    // Dots
    pts.forEach(p => {
        const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        dot.setAttribute('cx', p.x); dot.setAttribute('cy', p.y); dot.setAttribute('r', '2.5');
        dot.setAttribute('fill', '#fde047');
        svg.appendChild(dot);
    });
}

// Sim 12: 3D Cube Net Unfolder
function setSim12Net(type) {
    ['cross', 'stair', 'znet', 'illegal'].forEach(t => {
        const btn = document.getElementById(`sim12_b_${t}`);
        if (btn) btn.className = (t === type) ? (type === 'illegal' ? 'px-2.5 py-1 bg-rose-600 rounded font-bold' : 'px-2.5 py-1 bg-indigo-600 rounded font-bold') : 'px-2.5 py-1 bg-slate-700 rounded font-bold';
    });

    const tag = document.getElementById('sim12_net_tag');
    const desc = document.getElementById('sim12_desc');
    const svg = document.getElementById('sim12_svg');
    if (!svg || !tag || !desc) return;
    svg.innerHTML = '';

    const s = 30; // square size
    let squares = [];

    if (type === 'cross') {
        tag.textContent = 'Latin Cross (T-Net)';
        desc.textContent = 'Valid Net: 4 squares in central trunk with top and bottom side flaps. Folds cleanly!';
        squares = [[1, 0], [1, 1], [0, 1], [2, 1], [1, 2], [1, 3]];
    } else if (type === 'stair') {
        tag.textContent = 'Staircase Net';
        desc.textContent = 'Valid Net: Staggered squares fold without collisions into opposite faces.';
        squares = [[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 3]];
    } else if (type === 'znet') {
        tag.textContent = 'Z-Net (3-3 Shift)';
        desc.textContent = 'Valid Net: A 3-square row connected to another 3-square row offset by 1.';
        squares = [[0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1]];
    } else if (type === 'illegal') {
        tag.textContent = '6-in-a-Line (Illegal Net!)';
        desc.textContent = 'FAILS: Wraps around 4 sides; leaves top/bottom open and two squares overlap!';
        squares = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1]];
    }

    const ox = 30, oy = 25;
    squares.forEach(sq => {
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', ox + sq[0] * s);
        rect.setAttribute('y', oy + sq[1] * s);
        rect.setAttribute('width', s);
        rect.setAttribute('height', s);
        rect.setAttribute('fill', type === 'illegal' ? '#e11d48' : '#4f46e5');
        rect.setAttribute('stroke', '#ffffff');
        rect.setAttribute('stroke-width', '1.5');
        svg.appendChild(rect);
    });
    playSound('click');
}

// Sim 13: 3×3×3 Painted Cube Dissector
function setSim13Filter(faces) {
    [0, 1, 2, 3].forEach(f => {
        const btn = document.getElementById(`sim13_b_${f}`);
        if (btn) btn.className = (f === faces) ? 'p-2 bg-rose-600 rounded-lg font-bold' : 'p-2 bg-slate-700 rounded-lg font-bold';
    });

    const desc = document.getElementById('sim13_desc');
    const svg = document.getElementById('sim13_svg');
    if (!svg || !desc) return;
    svg.innerHTML = '';

    if (faces === 3) {
        desc.textContent = '8 Corner Cubes: Located at the 8 outer corners, exposed on 3 faces.';
    } else if (faces === 2) {
        desc.textContent = '12 Edge Cubes: 1 in the middle of each of the 12 edges, exposed on 2 faces.';
    } else if (faces === 1) {
        desc.textContent = '6 Face-Center Cubes: 1 in the middle of each of the 6 faces, exposed on 1 face.';
    } else if (faces === 0) {
        desc.textContent = '1 Core Cube: Completely buried inside the center, receives 0 paint.';
    }

    // Render 3D isometric representation of 3x3x3 cube
    const cx = 120, cy = 80;
    const s = 18; // isometric unit
    const uX = Math.cos(Math.PI / 6) * s;
    const uY = Math.sin(Math.PI / 6) * s;

    for (let z = -1; z <= 1; z++) {
        for (let y = -1; y <= 1; y++) {
            for (let x = -1; x <= 1; x++) {
                let paintedCount = 0;
                if (Math.abs(x) === 1) paintedCount++;
                if (Math.abs(y) === 1) paintedCount++;
                if (Math.abs(z) === 1) paintedCount++;

                const isMatch = (paintedCount === faces);
                const isoX = cx + (x - y) * uX;
                const isoY = cy + (x + y) * uY - z * s * 1.1;

                const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                dot.setAttribute('cx', isoX);
                dot.setAttribute('cy', isoY);
                dot.setAttribute('r', isMatch ? '6' : '3');
                dot.setAttribute('fill', isMatch ? '#f43f5e' : '#334155');
                dot.setAttribute('stroke', isMatch ? '#ffffff' : 'none');
                dot.setAttribute('stroke-width', '1.5');
                svg.appendChild(dot);
            }
        }
    }
    playSound('click');
}

// Sim 14: Linear Shape Pedestal Puzzle
let sim14Order = ['⭕', '🔺', '⬡', '🟦', '▭'];
function resetSim14() {
    sim14Order = ['⭕', '🔺', '⬡', '🟦', '▭'];
    updateSim14Display();
}

function swapSim14(posA, posB) {
    const temp = sim14Order[posA - 1];
    sim14Order[posA - 1] = sim14Order[posB - 1];
    sim14Order[posB - 1] = temp;
    updateSim14Display();
    playSound('click');
}

function updateSim14Display() {
    for (let i = 1; i <= 5; i++) {
        const el = document.getElementById(`sim14_slot_${i}`);
        if (el) el.textContent = sim14Order[i - 1];
    }
    document.getElementById('sim14_feedback').textContent = '';
}

function checkSim14() {
    const isCenterHex = (sim14Order[2] === '⬡');
    const isFirstCircle = (sim14Order[0] === '⭕');
    const isSquareBetween = (sim14Order[3] === '🟦' && sim14Order[1] === '🔺' && sim14Order[4] === '▭') ||
                            (sim14Order[3] === '🟦' && sim14Order[4] === '🔺' && sim14Order[1] === '▭');

    const fb = document.getElementById('sim14_feedback');
    if (isCenterHex && isFirstCircle && isSquareBetween) {
        fb.innerHTML = '<span class="text-emerald-400 font-bold">✓ Perfect Deduction!</span> Circle at 1, Hexagon at 3, Square between Triangle and Rectangle!';
        playSound('correct');
    } else {
        fb.innerHTML = '<span class="text-rose-400 font-bold">✗ Clues not fully satisfied!</span> Check the positions and try again.';
        playSound('incorrect');
    }
}

// Sim 15: Platonic Solids Dual Explorer
function setSim15Solid(type) {
    document.getElementById('sim15_b_ico').className = (type === 'icosa') ? 'px-3 py-1 bg-indigo-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';
    document.getElementById('sim15_b_dod').className = (type === 'dodeca') ? 'px-3 py-1 bg-indigo-600 rounded font-bold' : 'px-3 py-1 bg-slate-700 rounded font-bold';

    const stats = document.getElementById('sim15_stats');
    const svg = document.getElementById('sim15_svg');
    if (!svg || !stats) return;
    svg.innerHTML = '';

    const cx = 120, cy = 80;

    if (type === 'icosa') {
        stats.innerHTML = 'Faces: 20 (Equilateral Triangles) | Vertices: 12 | Edges: 30 ➔ <span class="text-emerald-400 font-bold">12 - 30 + 20 = 2</span> ✓';
        // Draw icosahedron projection
        const r = 50;
        const pts = [];
        for (let i = 0; i < 5; i++) {
            const a = (i * 72 - 90) * (Math.PI / 180);
            pts.push({ x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) });
        }
        for (let i = 0; i < 5; i++) {
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', cx); line.setAttribute('y1', cy);
            line.setAttribute('x2', pts[i].x); line.setAttribute('y2', pts[i].y);
            line.setAttribute('stroke', '#38bdf8'); line.setAttribute('stroke-width', '2');
            svg.appendChild(line);

            const next = (i + 1) % 5;
            const edge = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            edge.setAttribute('x1', pts[i].x); edge.setAttribute('y1', pts[i].y);
            edge.setAttribute('x2', pts[next].x); edge.setAttribute('y2', pts[next].y);
            edge.setAttribute('stroke', '#818cf8'); edge.setAttribute('stroke-width', '2');
            svg.appendChild(edge);
        }
    } else {
        stats.innerHTML = 'Faces: 12 (Regular Pentagons) | Vertices: 20 | Edges: 30 ➔ <span class="text-emerald-400 font-bold">20 - 30 + 12 = 2</span> ✓';
        // Draw dodecahedron projection
        const r1 = 55, r2 = 30;
        const outer = [], inner = [];
        for (let i = 0; i < 5; i++) {
            const a = (i * 72 - 90) * (Math.PI / 180);
            outer.push({ x: cx + r1 * Math.cos(a), y: cy + r1 * Math.sin(a) });
            inner.push({ x: cx + r2 * Math.cos(a), y: cy + r2 * Math.sin(a) });
        }
        for (let i = 0; i < 5; i++) {
            const next = (i + 1) % 5;
            const eOut = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            eOut.setAttribute('x1', outer[i].x); eOut.setAttribute('y1', outer[i].y);
            eOut.setAttribute('x2', outer[next].x); eOut.setAttribute('y2', outer[next].y);
            eOut.setAttribute('stroke', '#f59e0b'); eOut.setAttribute('stroke-width', '2');
            svg.appendChild(eOut);

            const eIn = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            eIn.setAttribute('x1', inner[i].x); eIn.setAttribute('y1', inner[i].y);
            eIn.setAttribute('x2', inner[next].x); eIn.setAttribute('y2', inner[next].y);
            eIn.setAttribute('stroke', '#fbbf24'); eIn.setAttribute('stroke-width', '2');
            svg.appendChild(eIn);

            const spoke = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            spoke.setAttribute('x1', inner[i].x); spoke.setAttribute('y1', inner[i].y);
            spoke.setAttribute('x2', outer[i].x); spoke.setAttribute('y2', outer[i].y);
            spoke.setAttribute('stroke', '#a5b4fc'); spoke.setAttribute('stroke-width', '1.5');
            svg.appendChild(spoke);
        }
    }
    playSound('click');
}

// Sim 16: Straw & Clay Skeletal Stability Tester
let sim16CurrentModel = 'square';
let sim16ForceApplied = false;
function setSim16Model(model) {
    sim16CurrentModel = model;
    sim16ForceApplied = false;
    ['sq', 'tri', 'tetra'].forEach(m => {
        const btn = document.getElementById(`sim16_b_${m}`);
        if (btn) btn.className = (m === (model === 'square' ? 'sq' : (model === 'triangulated' ? 'tri' : 'tetra'))) ? 'px-2.5 py-1 bg-teal-600 rounded font-bold' : 'px-2.5 py-1 bg-slate-700 rounded font-bold';
    });

    renderSim16();
    playSound('click');
}

function applySim16Force() {
    sim16ForceApplied = true;
    renderSim16();
    if (sim16CurrentModel === 'square') playSound('incorrect');
    else playSound('correct');
}

function renderSim16() {
    const desc = document.getElementById('sim16_desc');
    const tag = document.getElementById('sim16_model_tag');
    const svg = document.getElementById('sim16_svg');
    if (!svg) return;
    svg.innerHTML = '';

    const cx = 120, cy = 80;

    if (sim16CurrentModel === 'square') {
        tag.textContent = 'Unbraced Square (4 Straws)';
        if (!sim16ForceApplied) {
            desc.textContent = 'Unbraced Square: Push with lateral force to test rigidity.';
            drawStrawSquare(cx, cy, 0);
        } else {
            desc.innerHTML = '<span class="text-rose-400 font-bold">Wobbled into a Rhombus!</span> 4-sided frames lack rigidity and deform under load.';
            drawStrawSquare(cx, cy, 25); // 25px slant
        }
    } else if (sim16CurrentModel === 'triangulated') {
        tag.textContent = 'Triangulated Frame (5 Straws)';
        if (!sim16ForceApplied) {
            desc.textContent = 'Diagonal straw added: Test with force.';
            drawStrawTriangulated(cx, cy, 0);
        } else {
            desc.innerHTML = '<span class="text-emerald-400 font-bold">Rock Solid!</span> Diagonal bracing creates two rigid triangles that cannot deform!';
            drawStrawTriangulated(cx, cy, 0);
        }
    } else if (sim16CurrentModel === 'tetra') {
        tag.textContent = '3D Tetrahedron (6 Straws, 4 Clay Balls)';
        desc.innerHTML = '<span class="text-emerald-400 font-bold">Inherently Rigid!</span> 4 triangular faces lock every angle in 3 dimensions.';
        drawStrawTetra(cx, cy);
    }
}

function drawStrawSquare(cx, cy, slant) {
    const svg = document.getElementById('sim16_svg');
    const w = 70, h = 70;
    const p1 = { x: cx - w/2 - slant, y: cy + h/2 };
    const p2 = { x: cx + w/2 - slant, y: cy + h/2 };
    const p3 = { x: cx + w/2 + slant, y: cy - h/2 };
    const p4 = { x: cx - w/2 + slant, y: cy - h/2 };

    const pts = [p1, p2, p3, p4];
    for (let i = 0; i < 4; i++) {
        const next = (i + 1) % 4;
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', pts[i].x); line.setAttribute('y1', pts[i].y);
        line.setAttribute('x2', pts[next].x); line.setAttribute('y2', pts[next].y);
        line.setAttribute('stroke', '#38bdf8'); line.setAttribute('stroke-width', '4');
        svg.appendChild(line);
    }
    pts.forEach(p => {
        const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        c.setAttribute('cx', p.x); c.setAttribute('cy', p.y); c.setAttribute('r', '6');
        c.setAttribute('fill', '#f59e0b');
        svg.appendChild(c);
    });
}

function drawStrawTriangulated(cx, cy, slant) {
    drawStrawSquare(cx, cy, slant);
    const svg = document.getElementById('sim16_svg');
    const w = 70, h = 70;
    const diag = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    diag.setAttribute('x1', cx - w/2 - slant); diag.setAttribute('y1', cy + h/2);
    diag.setAttribute('x2', cx + w/2 + slant); diag.setAttribute('y2', cy - h/2);
    diag.setAttribute('stroke', '#10b981'); diag.setAttribute('stroke-width', '4');
    svg.appendChild(diag);
}

function drawStrawTetra(cx, cy) {
    const svg = document.getElementById('sim16_svg');
    const p1 = { x: cx, y: cy - 40 };
    const p2 = { x: cx - 50, y: cy + 35 };
    const p3 = { x: cx + 50, y: cy + 35 };
    const p4 = { x: cx, y: cy + 10 };

    const edges = [[p1, p2], [p1, p3], [p1, p4], [p2, p3], [p2, p4], [p3, p4]];
    edges.forEach(e => {
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', e[0].x); line.setAttribute('y1', e[0].y);
        line.setAttribute('x2', e[1].x); line.setAttribute('y2', e[1].y);
        line.setAttribute('stroke', '#14b8a6'); line.setAttribute('stroke-width', '3');
        svg.appendChild(line);
    });
    [p1, p2, p3, p4].forEach(p => {
        const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        c.setAttribute('cx', p.x); c.setAttribute('cy', p.y); c.setAttribute('r', '6');
        c.setAttribute('fill', '#f59e0b');
        svg.appendChild(c);
    });
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


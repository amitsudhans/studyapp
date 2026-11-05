# -*- coding: utf-8 -*-
"""JavaScript Engine for Class 5 Maths Chapter 13: Animal Jumps"""

js_code = """
// State Variables
let currentSlide = 0;
let synth = window.speechSynthesis;
let currentUtterance = null;
let keepAliveTimer = null;
let userPreferredVoice = null;
let quizScores = { 17: {}, 18: {}, 19: {}, 20: {} };

// Simulators State
let sim1CurrentInput = 7;
let sim2CurrentRows = 1;
let sim2CurrentCols = 12;
let sim3CurrentNum = 16;
let sim4CurrentNum = 13;
let sim5RabbitPos = 0;
let sim5FrogPos = 0;
let sim6SpiderPos = 0;
let sim6GrassPos = 0;
let sim7Pair = [4, 6];
let sim8Timer = null;
let sim9Step = 2;
let sim11Mode = 'composite';
let sim12Pair = [12, 16];
let sim13CurrentTest = 1;
let sim14Challenge = 'hunt';
let sim15CurrentFilter = 'all';

// Audio Context for Sound Effects
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

function playSound(type) {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (type === 'correct') {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(523.25, now);
            osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1);
            osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2);
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
            osc.start(now);
            osc.stop(now + 0.35);
        } else if (type === 'incorrect') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(220, now);
            osc.frequency.exponentialRampToValueAtTime(164.81, now + 0.18);
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        } else if (type === 'click') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(440, now);
            gain.gain.setValueAtTime(0.05, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
            osc.start(now);
            osc.stop(now + 0.05);
        } else if (type === 'jump') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(300, now);
            osc.frequency.exponentialRampToValueAtTime(600, now + 0.08);
            gain.gain.setValueAtTime(0.1, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
            osc.start(now);
            osc.stop(now + 0.12);
        }
    } catch (e) {
        // Audio might be restricted until user interaction
    }
}

// Indian Male Teacher Voice Priority & Calibration
function isIndianMaleVoice(v) {
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    const female = ['female', 'zira', 'susan', 'hazel', 'geeta', 'kalpana', 'priya', 'neerja', 'heera', 'swara', 'veena', 'woman', 'girl', 'lady', 'aria', 'jenny', 'samantha'];
    if (female.some(f => name.includes(f))) return false;
    if (lang.includes('en-in') || lang.includes('hi-in') || name.includes('india') || name.includes('indian')) {
        if (name.includes('prabhat') || name.includes('rishi') || name.includes('ravi') || name.includes('pradeep') || name.includes('madhav') || name.includes('karan') || name.includes('mohan') || name.includes('male')) {
            return true;
        }
        if (lang.includes('en-in')) return true;
    }
    return false;
}

function isMaleVoice(v) {
    const name = (v.name || '').toLowerCase();
    const female = ['female', 'zira', 'susan', 'hazel', 'geeta', 'kalpana', 'priya', 'neerja', 'heera', 'swara', 'veena', 'woman', 'girl', 'lady', 'aria', 'jenny', 'samantha'];
    if (female.some(f => name.includes(f))) return false;
    return (name.includes('male') || name.includes('david') || name.includes('mark') || name.includes('george') || name.includes('alex') || name.includes('guy') || name.includes('uk english male'));
}

function populateVoiceList() {
    if (!synth) return;
    const voices = synth.getVoices();
    const voiceSelect = document.getElementById('voiceSelect');
    if (!voiceSelect) return;

    voiceSelect.innerHTML = '';

    let indianMale = null;
    let anyMale = null;

    voices.forEach((v) => {
        const opt = document.createElement('option');
        opt.value = v.name;
        opt.textContent = `${v.name} (${v.lang})`;

        if (isIndianMaleVoice(v)) {
            opt.textContent = `🇮🇳 [Indian Male Teacher] ${v.name}`;
            if (!indianMale) indianMale = v;
        } else if (isMaleVoice(v)) {
            opt.textContent = `👨 [Male Teacher] ${v.name}`;
            if (!anyMale) anyMale = v;
        }

        voiceSelect.appendChild(opt);
    });

    if (userPreferredVoice) {
        voiceSelect.value = userPreferredVoice.name;
    } else if (indianMale) {
        voiceSelect.value = indianMale.name;
        userPreferredVoice = indianMale;
    } else if (anyMale) {
        voiceSelect.value = anyMale.name;
        userPreferredVoice = anyMale;
    }
}

if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = populateVoiceList;
}

function speakCurrentSlide() {
    if (!synth) return;
    synth.cancel();
    if (keepAliveTimer) clearInterval(keepAliveTimer);

    if (currentSlide >= 16) {
        return; // Mastery quizzes have no spoken lecture
    }

    const slide = slidesData[currentSlide];
    if (!slide || !slide.lecture) return;

    currentUtterance = new SpeechSynthesisUtterance(slide.lecture);

    const voiceSelect = document.getElementById('voiceSelect');
    if (voiceSelect && voiceSelect.value) {
        const voices = synth.getVoices();
        const selected = voices.find(v => v.name === voiceSelect.value);
        if (selected) currentUtterance.voice = selected;
    } else if (userPreferredVoice) {
        currentUtterance.voice = userPreferredVoice;
    }

    currentUtterance.rate = 0.94;
    currentUtterance.pitch = 0.85;

    const playBtn = document.getElementById('audioPlayBtn');
    if (playBtn) playBtn.innerHTML = '⏸️ Pause';

    currentUtterance.onend = () => {
        if (playBtn) playBtn.innerHTML = '🔊 Speak';
        if (keepAliveTimer) clearInterval(keepAliveTimer);
    };

    currentUtterance.onerror = () => {
        if (playBtn) playBtn.innerHTML = '🔊 Speak';
        if (keepAliveTimer) clearInterval(keepAliveTimer);
    };

    synth.speak(currentUtterance);

    // Keep-alive watchdog timer
    keepAliveTimer = setInterval(() => {
        if (!synth.speaking) {
            clearInterval(keepAliveTimer);
        } else {
            synth.pause();
            synth.resume();
        }
    }, 10000);
}

function toggleAudio() {
    if (!synth) return;
    if (synth.speaking && !synth.paused) {
        synth.pause();
        const playBtn = document.getElementById('audioPlayBtn');
        if (playBtn) playBtn.innerHTML = '▶️ Resume';
    } else if (synth.paused) {
        synth.resume();
        const playBtn = document.getElementById('audioPlayBtn');
        if (playBtn) playBtn.innerHTML = '⏸️ Pause';
    } else {
        speakCurrentSlide();
    }
}

// Navigation
function goToSlide(idx) {
    if (idx < 0 || idx >= slidesData.length) return;
    currentSlide = idx;

    if (synth) synth.cancel();
    const playBtn = document.getElementById('audioPlayBtn');
    if (playBtn) playBtn.innerHTML = '🔊 Speak';

    renderSlide();
}

function nextSlide() {
    if (currentSlide < slidesData.length - 1) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 0) {
        goToSlide(currentSlide - 1);
    }
}

function renderSlide() {
    const slide = slidesData[currentSlide];
    const container = document.getElementById('slideContent');
    const titleEl = document.getElementById('slideTitle');
    const taglineEl = document.getElementById('slideTagline');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    const progressEl = document.getElementById('progressBar');
    const numEl = document.getElementById('slideNum');

    if (titleEl) titleEl.textContent = `${slide.id}. ${slide.title}`;
    if (taglineEl) taglineEl.textContent = slide.tagline;
    if (numEl) numEl.textContent = `Slide ${slide.id} of ${slidesData.length}`;
    if (progressEl) progressEl.style.width = `${((currentSlide + 1) / slidesData.length) * 100}%`;

    if (prevBtn) prevBtn.disabled = currentSlide === 0;

    // Terminal slide invariant
    if (currentSlide === slidesData.length - 1) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.style.display = 'none';
    }

    // Render Slide Content
    if (currentSlide < 16) {
        let simHtml = simulatorsHtml[slide.id] || '';
        let checkpointsHtml = '';
        if (slide.checkpoints && slide.checkpoints.length > 0) {
            checkpointsHtml = `
            <div class="mt-4 pt-4 border-t border-slate-700/60">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                    <span>⚡ Formative Checkpoints</span>
                </h4>
                <div class="grid grid-cols-1 gap-3">
                    ${slide.checkpoints.map((cp, cIdx) => `
                        <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/80 text-xs">
                            <p class="font-semibold text-slate-200 mb-2">${cIdx + 1}. ${cp.question}</p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 mb-2">
                                ${cp.options.map((opt, oIdx) => `
                                    <button onclick="checkAnswer(${currentSlide}, ${cIdx}, ${oIdx})" id="cp_${currentSlide}_${cIdx}_${oIdx}" class="text-left px-2.5 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
                                        ${opt}
                                    </button>
                                `).join('')}
                            </div>
                            <div id="cp_feedback_${currentSlide}_${cIdx}" class="hidden p-2 rounded text-[11px] font-mono"></div>
                        </div>
                    `).join('')}
                </div>
            </div>`;
        }

        container.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 h-full">
            <div class="lg:col-span-6 flex flex-col justify-between overflow-y-auto pr-1">
                <div>
                    ${slide.content_html}
                </div>
                ${checkpointsHtml}
            </div>
            <div class="lg:col-span-6 bg-slate-950/70 p-4 rounded-2xl border border-slate-800 flex flex-col justify-between shadow-inner">
                ${simHtml}
            </div>
        </div>`;

        // Initialize Simulator
        initSimulator(slide.id);
    } else {
        // Quiz Slide (Slides 17 to 20)
        let questionsHtml = `
        <div class="space-y-4 max-w-4xl mx-auto">
            <div class="p-3 bg-gradient-to-r from-amber-900/40 via-purple-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl text-center">
                <h3 class="font-bold text-amber-300 text-sm uppercase tracking-wider">${slide.title}: ${slide.tagline}</h3>
                <p class="text-xs text-slate-300 mt-1">Answer all 10 questions to achieve mastery badge for this chapter.</p>
            </div>
            <div class="space-y-3">
                ${slide.questions.map((q, qIdx) => `
                    <div class="p-3.5 bg-slate-900/90 rounded-xl border border-slate-700 text-xs">
                        <div class="flex justify-between items-start gap-2 mb-2">
                            <span class="font-bold text-slate-200">Q${qIdx + 1}. ${q.question}</span>
                            <button onclick="openSolutionModal(${slide.id}, ${qIdx})" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 hover:bg-indigo-500/30 transition shrink-0">💡 Solution</button>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                            ${q.options.map((opt, oIdx) => `
                                <button onclick="selectQuizAnswer(${slide.id}, ${qIdx}, ${oIdx})" id="quiz_${slide.id}_${qIdx}_${oIdx}" class="text-left px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
                                    ${opt}
                                </button>
                            `).join('')}
                        </div>
                        <div id="quiz_feedback_${slide.id}_${qIdx}" class="hidden p-2 rounded text-[11px] font-mono"></div>
                    </div>
                `).join('')}
            </div>
        </div>`;

        container.innerHTML = questionsHtml;
    }
}

// Checkpoint Answer Checker
function checkAnswer(slideIdx, cpIdx, selectedIdx) {
    const slide = slidesData[slideIdx];
    const cp = slide.checkpoints[cpIdx];
    const fbEl = document.getElementById(`cp_feedback_${slideIdx}_${cpIdx}`);
    if (!fbEl) return;

    cp.options.forEach((_, oIdx) => {
        const btn = document.getElementById(`cp_${slideIdx}_${cpIdx}_${oIdx}`);
        if (btn) {
            btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
            if (oIdx === cp.answer) {
                btn.classList.add('bg-emerald-600/60', 'text-white', 'border-emerald-500');
            }
        }
    });

    const chosenBtn = document.getElementById(`cp_${slideIdx}_${cpIdx}_${selectedIdx}`);

    fbEl.classList.remove('hidden', 'bg-emerald-950/80', 'text-emerald-300', 'border-emerald-500/40', 'bg-rose-950/80', 'text-rose-300', 'border-rose-500/40');

    if (selectedIdx === cp.answer) {
        playSound('correct');
        if (chosenBtn) chosenBtn.classList.add('bg-emerald-600', 'text-white');
        fbEl.classList.add('bg-emerald-950/80', 'text-emerald-300', 'border', 'border-emerald-500/40');
        fbEl.innerHTML = `<strong>✓ Correct!</strong> ${cp.explanation}`;
    } else {
        playSound('incorrect');
        if (chosenBtn) chosenBtn.classList.add('bg-rose-600', 'text-white');
        fbEl.classList.add('bg-rose-950/80', 'text-rose-300', 'border', 'border-rose-500/40');
        fbEl.innerHTML = `<strong>✗ Incorrect.</strong> ${cp.hint} <span class="block mt-1 text-[10px] text-slate-400">${cp.explanation}</span>`;
    }
}

// Quiz Answer Selection
function selectQuizAnswer(slideId, qIdx, selectedIdx) {
    const slide = slidesData.find(s => s.id === slideId);
    if (!slide || !slide.questions) return;
    const q = slide.questions[qIdx];
    const fbEl = document.getElementById(`quiz_feedback_${slideId}_${qIdx}`);
    if (!fbEl) return;

    q.options.forEach((_, oIdx) => {
        const btn = document.getElementById(`quiz_${slideId}_${qIdx}_${oIdx}`);
        if (btn) {
            btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white');
            if (oIdx === q.answer) {
                btn.classList.add('bg-emerald-600/60', 'text-white');
            }
        }
    });

    const chosenBtn = document.getElementById(`quiz_${slideId}_${qIdx}_${selectedIdx}`);

    fbEl.classList.remove('hidden', 'bg-emerald-950/80', 'text-emerald-300', 'border-emerald-500/40', 'bg-rose-950/80', 'text-rose-300', 'border-rose-500/40');

    if (selectedIdx === q.answer) {
        playSound('correct');
        if (chosenBtn) chosenBtn.classList.add('bg-emerald-600', 'text-white');
        fbEl.classList.add('bg-emerald-950/80', 'text-emerald-300', 'border', 'border-emerald-500/40');
        fbEl.innerHTML = `<strong>✓ Correct!</strong> ${q.explanation}`;
        quizScores[slideId][qIdx] = true;
    } else {
        playSound('incorrect');
        if (chosenBtn) chosenBtn.classList.add('bg-rose-600', 'text-white');
        fbEl.classList.add('bg-rose-950/80', 'text-rose-300', 'border', 'border-rose-500/40');
        fbEl.innerHTML = `<strong>✗ Incorrect.</strong> ${q.hint}`;
        quizScores[slideId][qIdx] = false;
    }
}

// Modal for Quiz Solutions
function openSolutionModal(slideId, qIdx) {
    const slide = slidesData.find(s => s.id === slideId);
    if (!slide || !slide.questions) return;
    const q = slide.questions[qIdx];

    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionTitle');
    const content = document.getElementById('solutionContent');

    if (title) title.textContent = `Solution: Question ${qIdx + 1} (${slide.title})`;
    if (content) {
        content.innerHTML = `
        <div class="space-y-3 font-mono text-xs">
            <div class="p-2.5 rounded bg-slate-900 border border-slate-700 text-slate-200">
                <span class="text-amber-400 font-bold block mb-1">Question:</span>
                ${q.question}
            </div>
            <div class="p-2.5 rounded bg-emerald-950/60 border border-emerald-500/40 text-emerald-300">
                <span class="text-amber-300 font-bold block mb-1">Correct Answer:</span>
                ${q.options[q.answer]}
            </div>
            <div class="p-2.5 rounded bg-slate-900 border border-slate-700 text-slate-300 leading-relaxed">
                <span class="text-cyan-300 font-bold block mb-1">Step-by-Step Mathematical Derivation:</span>
                ${q.solution_html || q.explanation}
            </div>
        </div>`;
    }

    if (modal) modal.classList.remove('hidden');
    playSound('click');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// Initialize Simulators
function initSimulator(simId) {
    switch(simId) {
        case 1: sim1Init(); break;
        case 2: sim2Init(); break;
        case 3: sim3Init(); break;
        case 4: sim4Init(); break;
        case 5: sim5Init(); break;
        case 6: sim6Init(); break;
        case 7: sim7Init(); break;
        case 8: sim8Init(); break;
        case 9: sim9Init(); break;
        case 10: sim10Init(); break;
        case 11: sim11Init(); break;
        case 12: sim12Init(); break;
        case 13: sim13Init(); break;
        case 14: sim14Init(); break;
        case 15: sim15Init(); break;
        case 16: sim16Init(); break;
    }
}

// SIM 1: Multiplier Magic Box
function sim1Init() {
    sim1SetInput(7);
}

function sim1SetInput(n) {
    sim1CurrentInput = n;
    [7, 9, 12, 15, 18].forEach(x => {
        const b = document.getElementById(`sim1_btn_${x}`);
        if (b) {
            b.className = (x === n) ? 'px-2.5 py-1 rounded bg-purple-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const token = document.getElementById('sim1_token');
    const tokenTxt = document.getElementById('sim1_token_txt');
    const calcEl = document.getElementById('sim1_calc');
    const outEl = document.getElementById('sim1_out_val');
    const relEl = document.getElementById('sim1_rel');

    if (token) token.setAttribute('cy', '25');
    if (tokenTxt) {
        tokenTxt.setAttribute('y', '29');
        tokenTxt.textContent = n;
    }

    const res = n * 4;
    if (calcEl) calcEl.textContent = `${n} × 4 = ${res}`;
    if (outEl) outEl.textContent = res;
    if (relEl) relEl.textContent = `${res} is a multiple of ${n} and 4.`;
    playSound('click');
}

function sim1DropToken() {
    const token = document.getElementById('sim1_token');
    const tokenTxt = document.getElementById('sim1_token_txt');
    const btn = document.getElementById('sim1_drop_btn');
    if (!token || !btn) return;

    btn.disabled = true;
    playSound('jump');

    let pos = 25;
    const interval = setInterval(() => {
        pos += 6;
        token.setAttribute('cy', pos);
        if (tokenTxt) tokenTxt.setAttribute('y', pos + 4);

        if (pos >= 135) {
            clearInterval(interval);
            tokenTxt.textContent = sim1CurrentInput * 4;
            token.setAttribute('fill', '#f59e0b');
            playSound('correct');
            setTimeout(() => {
                token.setAttribute('cy', '25');
                token.setAttribute('fill', '#10b981');
                tokenTxt.setAttribute('y', '29');
                tokenTxt.textContent = sim1CurrentInput;
                btn.disabled = false;
            }, 1200);
        }
    }, 40);
}

// SIM 2: Factor Rectangle Studio
function sim2Init() {
    sim2SetArray(1, 12);
}

function sim2SetArray(r, c) {
    sim2CurrentRows = r;
    sim2CurrentCols = c;

    ['1_12', '2_6', '3_4'].forEach(id => {
        const b = document.getElementById(`sim2_btn_${id}`);
        if (b) {
            b.className = (id === `${r}_${c}`) ? 'px-2.5 py-1 rounded bg-cyan-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const grid = document.getElementById('sim2_grid');
    const desc = document.getElementById('sim2_desc');
    if (!grid) return;

    grid.innerHTML = '';
    const tileSize = 14;
    const pad = 2;
    const startX = 100 - (c * (tileSize + pad)) / 2;
    const startY = 60 - (r * (tileSize + pad)) / 2;

    for (let row = 0; row < r; row++) {
        for (let col = 0; col < c; col++) {
            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('x', startX + col * (tileSize + pad));
            rect.setAttribute('y', startY + row * (tileSize + pad));
            rect.setAttribute('width', tileSize);
            rect.setAttribute('height', tileSize);
            rect.setAttribute('rx', '2');
            rect.setAttribute('fill', '#06b6d4');
            rect.setAttribute('stroke', '#38bdf8');
            rect.setAttribute('stroke-width', '1');
            grid.appendChild(rect);
        }
    }

    if (desc) desc.textContent = `${r} Row(s) of ${c} Tiles (${r} × ${c} = 12)`;
    playSound('click');
}

// SIM 3: Array Configurations Lab
function sim3Init() {
    sim3SetNumber(16);
}

function sim3SetNumber(n) {
    sim3CurrentNum = n;
    [10, 16, 25, 13].forEach(x => {
        const b = document.getElementById(`sim3_btn_${x}`);
        if (b) {
            b.className = (x === n) ? 'px-2 py-1 rounded bg-emerald-600 text-white font-bold' : 'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const badge = document.getElementById('sim3_badge');
    const title = document.getElementById('sim3_title');
    const pairs = document.getElementById('sim3_pairs');
    const nature = document.getElementById('sim3_nature');
    const insight = document.getElementById('sim3_insight');
    const g = document.getElementById('sim3_tiles');
    if (!g) return;

    g.innerHTML = '';

    let rows = 1, cols = n;
    if (n === 16) { rows = 4; cols = 4; }
    else if (n === 25) { rows = 5; cols = 5; }
    else if (n === 10) { rows = 2; cols = 5; }
    else if (n === 13) { rows = 1; cols = 13; }

    const tileSize = (n === 13) ? 10 : 16;
    const startX = 80 - (cols * tileSize) / 2;
    const startY = 60 - (rows * tileSize) / 2;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('x', startX + c * tileSize);
            rect.setAttribute('y', startY + r * tileSize);
            rect.setAttribute('width', tileSize - 2);
            rect.setAttribute('height', tileSize - 2);
            rect.setAttribute('rx', '2');
            rect.setAttribute('fill', n === 13 ? '#a855f7' : (rows === cols ? '#10b981' : '#f59e0b'));
            g.appendChild(rect);
        }
    }

    if (n === 16) {
        if (badge) badge.textContent = 'Square Array!';
        if (title) title.textContent = '16 Tiles: 4 × 4 Square';
        if (pairs) pairs.textContent = 'Pairs: 1×16, 2×8, 4×4';
        if (nature) nature.textContent = 'Factors: {1, 2, 4, 8, 16} (5 Factors)';
        if (insight) insight.textContent = 'Identical factor (4×4) yields a perfect square!';
    } else if (n === 25) {
        if (badge) badge.textContent = 'Square Array!';
        if (title) title.textContent = '25 Tiles: 5 × 5 Square';
        if (pairs) pairs.textContent = 'Pairs: 1×25, 5×5';
        if (nature) nature.textContent = 'Factors: {1, 5, 25} (3 Factors)';
        if (insight) insight.textContent = 'Odd number of factors confirms perfect square!';
    } else if (n === 10) {
        if (badge) badge.textContent = 'Composite';
        if (title) title.textContent = '10 Tiles: 2 × 5 Array';
        if (pairs) pairs.textContent = 'Pairs: 1×10, 2×5';
        if (nature) nature.textContent = 'Factors: {1, 2, 5, 10} (4 Factors)';
        if (insight) insight.textContent = 'Even number of factors (paired rect dimensions).';
    } else if (n === 13) {
        if (badge) badge.textContent = 'Prime Number!';
        if (title) title.textContent = '13 Tiles: 1 × 13 Line Only';
        if (pairs) pairs.textContent = 'Pair: 1×13 only';
        if (nature) nature.textContent = 'Factors: {1, 13} (2 Factors)';
        if (insight) insight.textContent = 'Cannot form multiple rows without leftover tiles.';
    }
    playSound('click');
}

// SIM 4: Prime & Composite Sieve
function sim4Init() {
    sim4TestNumber(13);
}

function sim4TestNumber(n) {
    sim4CurrentNum = n;
    [2, 9, 13, 14, 24, 37, 1].forEach(x => {
        const b = document.getElementById(`sim4_btn_${x}`);
        if (b) {
            b.className = (x === n) ? 'px-2 py-1 rounded bg-emerald-600 text-white font-bold' : 'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const badge = document.getElementById('sim4_badge');
    const numEl = document.getElementById('sim4_num');
    const countEl = document.getElementById('sim4_count');
    const listEl = document.getElementById('sim4_factor_list');
    const desc = document.getElementById('sim4_desc');
    const sub = document.getElementById('sim4_sub');
    const geom = document.getElementById('sim4_geom');

    if (numEl) numEl.textContent = n;

    let factors = [];
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) factors.push(i);
    }

    if (countEl) countEl.textContent = factors.length;
    if (listEl) listEl.textContent = `Factors: {${factors.join(', ')}}`;

    if (n === 1) {
        if (badge) {
            badge.textContent = 'NEITHER PRIME NOR COMPOSITE';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-500/20 text-slate-300 border border-slate-500/30';
        }
        if (desc) desc.textContent = 'Unique Special Number (Only 1 Factor)';
        if (sub) sub.textContent = 'Prime numbers require exactly 2 distinct factors.';
        if (geom) geom.textContent = 'Single unit square point.';
    } else if (factors.length === 2) {
        if (badge) {
            badge.textContent = 'PRIME NUMBER';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (desc) desc.textContent = `Prime Number (Exactly 2 Factors)`;
        if (sub) sub.textContent = `Divisible only by 1 and ${n}.`;
        if (geom) geom.textContent = `Forms only a 1 × ${n} single straight line.`;
    } else {
        if (badge) {
            badge.textContent = 'COMPOSITE NUMBER';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
        }
        if (desc) desc.textContent = `Composite Number (${factors.length} Factors)`;
        if (sub) sub.textContent = `Can be divided by numbers other than 1 and ${n}.`;
        if (geom) geom.textContent = `Forms multiple complete rectangular arrays.`;
    }
    playSound('click');
}

// SIM 5: Rabbit & Frog Jumps
function sim5Init() {
    sim5Reset();
}

function sim5Reset() {
    sim5RabbitPos = 0;
    sim5FrogPos = 0;
    const rPos = document.getElementById('sim5_r_pos');
    const fPos = document.getElementById('sim5_f_pos');
    const overlap = document.getElementById('sim5_overlap');
    const rCircle = document.getElementById('sim5_rabbit_pos');
    const fCircle = document.getElementById('sim5_frog_pos');
    const rArcs = document.getElementById('sim5_rabbit_arcs');
    const fArcs = document.getElementById('sim5_frog_arcs');
    const ticks = document.getElementById('sim5_ticks');

    if (rPos) rPos.textContent = '0';
    if (fPos) fPos.textContent = '0';
    if (overlap) overlap.textContent = '0';
    if (rCircle) rCircle.setAttribute('cx', '10');
    if (fCircle) fCircle.setAttribute('cx', '10');
    if (rArcs) rArcs.innerHTML = '';
    if (fArcs) fArcs.innerHTML = '';

    if (ticks) {
        ticks.innerHTML = '';
        for (let i = 0; i <= 24; i++) {
            const x = 10 + i * 12.5;
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', x);
            line.setAttribute('y1', 77);
            line.setAttribute('x2', x);
            line.setAttribute('y2', 83);
            line.setAttribute('stroke', (i % 6 === 0) ? '#38bdf8' : '#475569');
            ticks.appendChild(line);

            if (i % 3 === 0) {
                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', x);
                text.setAttribute('y', 95);
                text.setAttribute('text-anchor', 'middle');
                text.setAttribute('font-size', '7');
                text.setAttribute('fill', (i % 12 === 0 && i > 0) ? '#facc15' : '#94a3b8');
                text.setAttribute('font-weight', (i % 12 === 0) ? 'bold' : 'normal');
                text.textContent = i;
                ticks.appendChild(text);
            }
        }
    }
}

function sim5NextStep() {
    if (sim5RabbitPos >= 24 && sim5FrogPos >= 24) {
        sim5Reset();
        return;
    }

    const prevR = sim5RabbitPos;
    const prevF = sim5FrogPos;
    sim5RabbitPos = Math.min(24, sim5RabbitPos + 4);
    sim5FrogPos = Math.min(24, sim5FrogPos + 3);

    const rCircle = document.getElementById('sim5_rabbit_pos');
    const fCircle = document.getElementById('sim5_frog_pos');
    const rArcs = document.getElementById('sim5_rabbit_arcs');
    const fArcs = document.getElementById('sim5_frog_arcs');
    const rPos = document.getElementById('sim5_r_pos');
    const fPos = document.getElementById('sim5_f_pos');
    const overlap = document.getElementById('sim5_overlap');

    const xR1 = 10 + prevR * 12.5;
    const xR2 = 10 + sim5RabbitPos * 12.5;
    const xF1 = 10 + prevF * 12.5;
    const xF2 = 10 + sim5FrogPos * 12.5;

    if (rCircle) rCircle.setAttribute('cx', xR2);
    if (fCircle) fCircle.setAttribute('cx', xF2);

    if (rArcs && sim5RabbitPos > prevR) {
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        const midX = (xR1 + xR2) / 2;
        path.setAttribute('d', `M ${xR1} 80 Q ${midX} 35 ${xR2} 80`);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', '#f59e0b');
        path.setAttribute('stroke-width', '2');
        rArcs.appendChild(path);
    }

    if (fArcs && sim5FrogPos > prevF) {
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        const midX = (xF1 + xF2) / 2;
        path.setAttribute('d', `M ${xF1} 80 Q ${midX} 50 ${xF2} 80`);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', '#10b981');
        path.setAttribute('stroke-width', '1.5');
        path.setAttribute('stroke-dasharray', '3,2');
        fArcs.appendChild(path);
    }

    if (rPos) rPos.textContent = sim5RabbitPos;
    if (fPos) fPos.textContent = sim5FrogPos;

    let shared = [];
    for (let i = 1; i <= Math.min(sim5RabbitPos, sim5FrogPos); i++) {
        if (i % 12 === 0) shared.push(i);
    }
    if (overlap) overlap.textContent = shared.length > 0 ? shared.join(', ') : 'None yet';

    playSound('jump');
}

// SIM 6: Spider & Grasshopper
function sim6Init() {
    sim6Reset();
}

function sim6Reset() {
    sim6SpiderPos = 0;
    sim6GrassPos = 0;
    const sPos = document.getElementById('sim6_s_pos');
    const gPos = document.getElementById('sim6_g_pos');
    const sCircle = document.getElementById('sim6_spider_pos');
    const gCircle = document.getElementById('sim6_grass_pos');
    const sArcs = document.getElementById('sim6_spider_arcs');
    const gArcs = document.getElementById('sim6_grass_arcs');
    const ticks = document.getElementById('sim6_ticks');

    if (sPos) sPos.textContent = '0';
    if (gPos) gPos.textContent = '0';
    if (sCircle) sCircle.setAttribute('cx', '10');
    if (gCircle) gCircle.setAttribute('cx', '10');
    if (sArcs) sArcs.innerHTML = '';
    if (gArcs) gArcs.innerHTML = '';

    if (ticks) {
        ticks.innerHTML = '';
        for (let i = 0; i <= 24; i++) {
            const x = 10 + i * 12.5;
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', x);
            line.setAttribute('y1', 77);
            line.setAttribute('x2', x);
            line.setAttribute('y2', 83);
            line.setAttribute('stroke', (i % 6 === 0) ? '#06b6d4' : '#475569');
            ticks.appendChild(line);

            if (i % 6 === 0) {
                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', x);
                text.setAttribute('y', 95);
                text.setAttribute('text-anchor', 'middle');
                text.setAttribute('font-size', '8');
                text.setAttribute('fill', '#38bdf8');
                text.setAttribute('font-weight', 'bold');
                text.textContent = i;
                ticks.appendChild(text);
            }
        }
    }
}

function sim6Step() {
    if (sim6SpiderPos >= 24 && sim6GrassPos >= 24) {
        sim6Reset();
        return;
    }

    const prevS = sim6SpiderPos;
    const prevG = sim6GrassPos;
    sim6SpiderPos = Math.min(24, sim6SpiderPos + 3);
    sim6GrassPos = Math.min(24, sim6GrassPos + 6);

    const sCircle = document.getElementById('sim6_spider_pos');
    const gCircle = document.getElementById('sim6_grass_pos');
    const sArcs = document.getElementById('sim6_spider_arcs');
    const gArcs = document.getElementById('sim6_grass_arcs');
    const sPos = document.getElementById('sim6_s_pos');
    const gPos = document.getElementById('sim6_g_pos');

    const xS1 = 10 + prevS * 12.5;
    const xS2 = 10 + sim6SpiderPos * 12.5;
    const xG1 = 10 + prevG * 12.5;
    const xG2 = 10 + sim6GrassPos * 12.5;

    if (sCircle) sCircle.setAttribute('cx', xS2);
    if (gCircle) gCircle.setAttribute('cx', xG2);

    if (sArcs && sim6SpiderPos > prevS) {
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        const midX = (xS1 + xS2) / 2;
        path.setAttribute('d', `M ${xS1} 80 Q ${midX} 55 ${xS2} 80`);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', '#a855f7');
        path.setAttribute('stroke-width', '1.5');
        sArcs.appendChild(path);
    }

    if (gArcs && sim6GrassPos > prevG) {
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        const midX = (xG1 + xG2) / 2;
        path.setAttribute('d', `M ${xG1} 80 Q ${midX} 35 ${xG2} 80`);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', '#06b6d4');
        path.setAttribute('stroke-width', '2.5');
        gArcs.appendChild(path);
    }

    if (sPos) sPos.textContent = sim6SpiderPos;
    if (gPos) gPos.textContent = sim6GrassPos;
    playSound('jump');
}

// SIM 7: Multiples Practice
function sim7Init() {
    sim7SelectPair(4, 6);
}

function sim7SelectPair(a, b) {
    sim7Pair = [a, b];
    ['4_6', '8_12', '6_8', '9_12'].forEach(id => {
        const btn = document.getElementById(`sim7_btn_${id}`);
        if (btn) {
            btn.className = (id === `${a}_${b}`) ? 'px-2.5 py-1 rounded bg-indigo-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const l1 = document.getElementById('sim7_m1_label');
    const l2 = document.getElementById('sim7_m2_label');
    const list1 = document.getElementById('sim7_m1_list');
    const list2 = document.getElementById('sim7_m2_list');
    const lcmEl = document.getElementById('sim7_lcm');
    const badge = document.getElementById('sim7_badge');

    let m1 = [], m2 = [];
    for (let i = 1; i <= 8; i++) m1.push(a * i);
    for (let i = 1; i <= 8; i++) m2.push(b * i);

    let lcm = 1;
    for (let i = 1; i <= a * b; i++) {
        if (i % a === 0 && i % b === 0) {
            lcm = i;
            break;
        }
    }

    if (l1) l1.textContent = `Multiples of ${a}:`;
    if (l2) l2.textContent = `Multiples of ${b}:`;
    if (list1) list1.textContent = m1.join(', ') + '...';
    if (list2) list2.textContent = m2.join(', ') + '...';
    if (lcmEl) lcmEl.textContent = lcm;
    if (badge) badge.textContent = `LCM: ${lcm}`;
    playSound('click');
}

// SIM 8: Cobbled Road Race
function sim8Init() {
    sim8Reset();
}

function sim8Reset() {
    if (sim8Timer) clearInterval(sim8Timer);
    const r1 = document.getElementById('sim8_r1');
    const r2 = document.getElementById('sim8_r2');
    const t1 = document.getElementById('sim8_t1_txt');
    const t2 = document.getElementById('sim8_t2_txt');
    const res = document.getElementById('sim8_result');
    const btn = document.getElementById('sim8_btn_race');

    if (r1) r1.setAttribute('cx', '20');
    if (r2) r2.setAttribute('cx', '20');
    if (t1) t1.textContent = 'Tile 0 (0 leaps)';
    if (t2) t2.textContent = 'Tile 0 (0 leaps)';
    if (res) res.textContent = 'Click Start to see who reaches tile 64!';
    if (btn) btn.disabled = false;
}

function sim8RunRace() {
    const btn = document.getElementById('sim8_btn_race');
    if (btn) btn.disabled = true;

    const r1 = document.getElementById('sim8_r1');
    const r2 = document.getElementById('sim8_r2');
    const t1 = document.getElementById('sim8_t1_txt');
    const t2 = document.getElementById('sim8_t2_txt');
    const res = document.getElementById('sim8_result');

    let stepA = 0;
    let stepB = 0;

    sim8Timer = setInterval(() => {
        if (stepA < 16) stepA++;
        if (stepB < 11) stepB++;

        const posA = stepA * 4;
        const posB = stepB * 6;

        // Map tile 0-66 to cx 20-288
        const cxA = 20 + (posA / 64) * 260;
        const cxB = 20 + (posB / 64) * 260;

        if (r1) r1.setAttribute('cx', Math.min(280, cxA));
        if (r2) r2.setAttribute('cx', Math.min(288, cxB));

        if (t1) t1.textContent = `Tile ${posA} (${stepA} leaps)`;
        if (t2) t2.textContent = `Tile ${posB} (${stepB} leaps)`;

        playSound('jump');

        if (stepA === 16 && stepB === 11) {
            clearInterval(sim8Timer);
            if (res) {
                res.innerHTML = `<strong>🏆 Racer A Wins!</strong> Landed exactly on tile 64 in 16 leaps.<br><span class="text-rose-400 font-normal">Racer B hit 60, then 66 (Overshot 64)!</span>`;
            }
            playSound('correct');
            if (btn) btn.disabled = false;
        }
    }, 200);
}

// SIM 9: Jungle Trail
function sim9Init() {
    sim9SetStep(2);
}

function sim9SetStep(step) {
    sim9Step = step;
    [2, 3, 5, 10].forEach(s => {
        const b = document.getElementById(`sim9_btn_${s}`);
        if (b) {
            b.className = (s === step) ? 'px-2.5 py-1 rounded bg-emerald-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const badge = document.getElementById('sim9_badge');
    const countEl = document.getElementById('sim9_count');
    const grid = document.getElementById('sim9_stones_grid');
    const summary = document.getElementById('sim9_summary');

    if (badge) badge.textContent = `Step Size: ${step}`;

    let stones = [];
    for (let i = 0; i <= 50; i += step) {
        stones.push(i);
    }

    if (countEl) countEl.textContent = `${stones.length} Stones`;
    if (grid) {
        grid.innerHTML = stones.map(st => `
            <span class="px-1.5 py-0.5 rounded bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 font-bold">
                ${st}
            </span>
        `).join('');
    }

    if (summary) {
        summary.textContent = `${step} divides all of these numbers completely with zero remainder.`;
    }
    playSound('click');
}

// SIM 10: Common Factors Finder
function sim10Init() {
    sim10Highlight('all');
}

function sim10Highlight(mode) {
    ['all', 'common', 'hcf'].forEach(m => {
        const b = document.getElementById(`sim10_btn_${m}`);
        if (b) {
            b.className = (m === mode) ? 'px-2.5 py-1 rounded bg-cyan-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const cf1 = document.getElementById('sim10_cf1');
    const cf2 = document.getElementById('sim10_cf2');
    const cf4 = document.getElementById('sim10_cf4');
    const resHcf = document.getElementById('sim10_res_hcf');

    if (mode === 'hcf') {
        if (cf1) cf1.setAttribute('fill', '#475569');
        if (cf2) cf2.setAttribute('fill', '#475569');
        if (cf4) cf4.setAttribute('fill', '#facc15');
        if (cf4) cf4.setAttribute('font-size', '14');
        playSound('correct');
    } else if (mode === 'common') {
        if (cf1) cf1.setAttribute('fill', '#34d399');
        if (cf2) cf2.setAttribute('fill', '#34d399');
        if (cf4) cf4.setAttribute('fill', '#34d399');
        if (cf4) cf4.setAttribute('font-size', '10');
        playSound('click');
    } else {
        if (cf1) cf1.setAttribute('fill', '#34d399');
        if (cf2) cf2.setAttribute('fill', '#34d399');
        if (cf4) cf4.setAttribute('fill', '#facc15');
        if (cf4) cf4.setAttribute('font-size', '10');
        playSound('click');
    }
}

// SIM 11: Consecutive & Composite Pairs
function sim11Init() {
    sim11SetMode('composite');
}

function sim11SetMode(m) {
    sim11Mode = m;
    const bComp = document.getElementById('sim11_btn_comp');
    const bCons = document.getElementById('sim11_btn_cons');
    const badge = document.getElementById('sim11_badge');
    const t1 = document.getElementById('sim11_title1');
    const t2 = document.getElementById('sim11_title2');
    const f1 = document.getElementById('sim11_f1');
    const f2 = document.getElementById('sim11_f2');
    const lbl = document.getElementById('sim11_common_label');
    const res = document.getElementById('sim11_result');

    if (m === 'composite') {
        if (bComp) bComp.className = 'flex-1 py-1.5 rounded-lg bg-purple-600 text-white font-bold';
        if (bCons) bCons.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-200 font-bold';
        if (badge) badge.textContent = 'Pair: 24 & 36';
        if (t1) t1.textContent = 'Factors of 24:';
        if (f1) f1.textContent = '{1, 2, 3, 4, 6, 8, 12, 24}';
        if (t2) t2.textContent = 'Factors of 36:';
        if (f2) f2.textContent = '{1, 2, 3, 4, 6, 9, 12, 18, 36}';
        if (lbl) lbl.textContent = 'Shared Factors (6 factors):';
        if (res) res.textContent = '{1, 2, 3, 4, 6, 12} (HCF: 12)';
    } else {
        if (bComp) bComp.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-200 font-bold';
        if (bCons) bCons.className = 'flex-1 py-1.5 rounded-lg bg-purple-600 text-white font-bold';
        if (badge) badge.textContent = 'Consecutive: 12 & 13';
        if (t1) t1.textContent = 'Factors of 12:';
        if (f1) f1.textContent = '{1, 2, 3, 4, 6, 12}';
        if (t2) t2.textContent = 'Factors of 13:';
        if (f2) f2.textContent = '{1, 13}';
        if (lbl) lbl.textContent = 'Consecutive Rule:';
        if (res) res.textContent = '{1} Only! (Co-prime)';
    }
    playSound('click');
}

// SIM 12: Common Factor Practice Matrix
function sim12Init() {
    sim12SetPair(12, 16);
}

function sim12SetPair(a, b) {
    sim12Pair = [a, b];
    ['12_16', '2_9', '9_21'].forEach(id => {
        const btn = document.getElementById(`sim12_btn_${id}`);
        if (btn) {
            btn.className = (id === `${a}_${b}`) ? 'px-2.5 py-1 rounded bg-teal-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const lbl1 = document.getElementById('sim12_n1_lbl');
    const lbl2 = document.getElementById('sim12_n2_lbl');
    const f1 = document.getElementById('sim12_n1_f');
    const f2 = document.getElementById('sim12_n2_f');
    const cf = document.getElementById('sim12_cf');
    const hcf = document.getElementById('sim12_hcf');

    let fa = [], fb = [];
    for (let i = 1; i <= a; i++) if (a % i === 0) fa.push(i);
    for (let i = 1; i <= b; i++) if (b % i === 0) fb.push(i);

    let common = fa.filter(x => fb.includes(x));
    let maxFactor = Math.max(...common);

    if (lbl1) lbl1.textContent = `Number ${a}`;
    if (lbl2) lbl2.textContent = `Number ${b}`;
    if (f1) f1.textContent = `{${fa.join(', ')}}`;
    if (f2) f2.textContent = `{${fb.join(', ')}}`;
    if (cf) cf.textContent = `{${common.join(', ')}}`;
    if (hcf) hcf.textContent = maxFactor;
    playSound('click');
}

// SIM 13: Divisibility Truth Tester
function sim13Init() {
    sim13Test(1);
}

function sim13Test(idx) {
    sim13CurrentTest = idx;
    [1, 2, 3, 4].forEach(i => {
        const b = document.getElementById(`sim13_btn_${i}`);
        if (b) {
            b.className = (i === idx) ? 'px-2 py-1 rounded bg-amber-600 text-white font-bold text-left truncate' : 'px-2 py-1 rounded bg-slate-800 text-slate-200 font-bold text-left truncate';
        }
    });

    const stmt = document.getElementById('sim13_statement');
    const verd = document.getElementById('sim13_verdict');
    const proof = document.getElementById('sim13_proof');

    if (idx === 1) {
        if (stmt) stmt.textContent = '"Factors of even numbers must be even."';
        if (verd) {
            verd.textContent = 'FALSE';
            verd.className = 'px-2 py-0.5 rounded font-bold text-rose-400 bg-rose-950/80 border border-rose-500/30';
        }
        if (proof) proof.textContent = 'Counterexample: 10 is even, but its factors include 1 and 5 (odd)!';
    } else if (idx === 2) {
        if (stmt) stmt.textContent = '"Multiples of odd numbers cannot be even."';
        if (verd) {
            verd.textContent = 'FALSE';
            verd.className = 'px-2 py-0.5 rounded font-bold text-rose-400 bg-rose-950/80 border border-rose-500/30';
        }
        if (proof) proof.textContent = 'Counterexample: 3 × 2 = 6, which is even. Odd × Even = Even!';
    } else if (idx === 3) {
        if (stmt) stmt.textContent = '"Factors of odd numbers cannot be even."';
        if (verd) {
            verd.textContent = 'TRUE';
            verd.className = 'px-2 py-0.5 rounded font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/30';
        }
        if (proof) proof.textContent = 'Proof: If an odd number had an even factor, it would be divisible by 2, making it even!';
    } else if (idx === 4) {
        if (stmt) stmt.textContent = '"Any two consecutive numbers share only factor 1."';
        if (verd) {
            verd.textContent = 'TRUE';
            verd.className = 'px-2 py-0.5 rounded font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/30';
        }
        if (proof) proof.textContent = 'Proof: Consecutive numbers differ by 1. No number > 1 can divide both.';
    }
    playSound('click');
}

// SIM 14: Jungle Story Navigator
function sim14Init() {
    sim14SetChallenge('hunt');
}

function sim14SetChallenge(ch) {
    sim14Challenge = ch;
    const bHunt = document.getElementById('sim14_btn_hunt');
    const bPath = document.getElementById('sim14_btn_path');
    const vHunt = document.getElementById('sim14_hunt_view');
    const vPath = document.getElementById('sim14_path_view');
    const badge = document.getElementById('sim14_badge');

    if (ch === 'hunt') {
        if (bHunt) bHunt.className = 'flex-1 py-1.5 rounded-lg bg-cyan-600 text-white font-bold';
        if (bPath) bPath.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-200 font-bold';
        if (vHunt) vHunt.classList.remove('hidden');
        if (vPath) vPath.classList.add('hidden');
        if (badge) badge.textContent = 'Hunting Cycle';
    } else {
        if (bHunt) bHunt.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-200 font-bold';
        if (bPath) bPath.className = 'flex-1 py-1.5 rounded-lg bg-cyan-600 text-white font-bold';
        if (vHunt) vHunt.classList.add('hidden');
        if (vPath) vPath.classList.remove('hidden');
        if (badge) badge.textContent = 'Safe Den Path';
    }
    playSound('click');
}

// SIM 15: Divisibility Venn Sorter
function sim15Init() {
    sim15Filter('all');
}

function sim15Filter(f) {
    sim15CurrentFilter = f;
    ['all', '2only', '5only', 'both'].forEach(k => {
        const b = document.getElementById(`sim15_btn_${k}`);
        if (b) {
            b.className = (k === f) ? 'px-2.5 py-1 rounded bg-purple-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const l2 = document.getElementById('sim15_list_2');
    const l5 = document.getElementById('sim15_list_5');
    const lb = document.getElementById('sim15_list_both');

    if (l2 && l5 && lb) {
        l2.style.opacity = (f === 'all' || f === '2only') ? '1' : '0.2';
        l5.style.opacity = (f === 'all' || f === '5only') ? '1' : '0.2';
        lb.style.opacity = (f === 'all' || f === 'both') ? '1' : '0.2';
    }
    playSound('click');
}

// SIM 16: Grand Master Synthesis
function sim16Init() {
    sim16Compute();
}

function sim16Compute() {
    const aInput = document.getElementById('sim16_a');
    const bInput = document.getElementById('sim16_b');
    const hcfEl = document.getElementById('sim16_hcf');
    const lcmEl = document.getElementById('sim16_lcm');
    const faEl = document.getElementById('sim16_fa');
    const fbEl = document.getElementById('sim16_fb');

    let a = parseInt(aInput ? aInput.value : 12) || 12;
    let b = parseInt(bInput ? bInput.value : 18) || 18;

    a = Math.max(1, Math.min(50, a));
    b = Math.max(1, Math.min(50, b));

    let fa = [], fb = [];
    for (let i = 1; i <= a; i++) if (a % i === 0) fa.push(i);
    for (let i = 1; i <= b; i++) if (b % i === 0) fb.push(i);

    let hcf = 1;
    for (let i = 1; i <= Math.min(a, b); i++) {
        if (a % i === 0 && b % i === 0) hcf = i;
    }

    let lcm = (a * b) / hcf;

    if (hcfEl) hcfEl.textContent = `HCF = ${hcf}`;
    if (lcmEl) lcmEl.textContent = `LCM = ${lcm}`;
    if (faEl) faEl.textContent = fa.join(', ');
    if (fbEl) fbEl.textContent = fb.join(', ');
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    populateVoiceList();
    renderSlide();
});
"""

if __name__ == '__main__':
    with open('.agents/class5_maths_ch13_js.js', 'w') as f:
        f.write(js_code)
    print("class5_maths_ch13_js.js written successfully!")

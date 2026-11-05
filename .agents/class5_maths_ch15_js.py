# -*- coding: utf-8 -*-
"""JavaScript Engine for Class 5 Maths Chapter 15: Data Through Pictures"""

js_code = '''
// State Variables
let currentSlide = 0;
let synth = window.speechSynthesis;
let currentUtterance = null;
let keepAliveTimer = null;
let userPreferredVoice = null;
let quizScores = { 17: {}, 18: {}, 19: {}, 20: {} };

// Simulators Internal State
let sim1CurrentFilter = 'all';
let sim2CurrentStep = 0;
let sim5CurrentScale = 10;
let sim7CurrentScale = 6;
let sim8ActiveCat = 'sleep';
let sim14Reduction = 0;

// Raw survey dataset (35 responses)
const sim1Dataset = [
    { cat: 'half', val: '½ hr' }, { cat: 'one', val: '1 hr' }, { cat: 'one_half', val: '1½ hrs' },
    { cat: 'one', val: '1 hr' }, { cat: 'two', val: '2 hrs' }, { cat: 'more', val: '> 2 hrs' },
    { cat: 'one', val: '1 hr' }, { cat: 'half', val: '½ hr' }, { cat: 'one', val: '1 hr' },
    { cat: 'one_half', val: '1½ hrs' }, { cat: 'two', val: '2 hrs' }, { cat: 'one', val: '1 hr' },
    { cat: 'half', val: '½ hr' }, { cat: 'one', val: '1 hr' }, { cat: 'one_half', val: '1½ hrs' },
    { cat: 'two', val: '2 hrs' }, { cat: 'more', val: '> 2 hrs' }, { cat: 'one', val: '1 hr' },
    { cat: 'one_half', val: '1½ hrs' }, { cat: 'half', val: '½ hr' }, { cat: 'one', val: '1 hr' },
    { cat: 'two', val: '2 hrs' }, { cat: 'one', val: '1 hr' }, { cat: 'one_half', val: '1½ hrs' },
    { cat: 'more', val: '> 2 hrs' }, { cat: 'one', val: '1 hr' }, { cat: 'half', val: '½ hr' },
    { cat: 'one', val: '1 hr' }, { cat: 'one_half', val: '1½ hrs' }, { cat: 'two', val: '2 hrs' },
    { cat: 'one', val: '1 hr' }, { cat: 'one_half', val: '1½ hrs' }, { cat: 'more', val: '> 2 hrs' },
    { cat: 'two', val: '2 hrs' }, { cat: 'one_half', val: '1½ hrs' }
];

// Audio Context for Interactive Sound Effects
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
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
            gain.gain.setValueAtTime(0.06, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
            osc.start(now);
            osc.stop(now + 0.05);
        } else if (type === 'tally') {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(350, now);
            osc.frequency.exponentialRampToValueAtTime(500, now + 0.08);
            gain.gain.setValueAtTime(0.08, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
            osc.start(now);
            osc.stop(now + 0.1);
        }
    } catch (e) {
        // Audio policy restriction
    }
}

// Indian Male Teacher Voice Priority & Strict Filtering
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

if (window.speechSynthesis && speechSynthesis.onvoiceschanged !== undefined) {
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

    // Keep-alive watchdog timer (10s ping)
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

// Slide Navigation
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

// Master Slide Renderer
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

    // Terminal slide invariant for Slide 20
    if (currentSlide === slidesData.length - 1) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.style.display = 'none';
    }

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

// Solution Modal
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
    playSound('click');
}

// Simulator Initializer
function initSimulator(id) {
    if (id === 1) sim1Filter('all');
    else if (id === 2) sim2ShowAll();
    else if (id === 3) sim3Subgroup('le1');
    else if (id === 4) sim4Inspect('toys');
    else if (id === 5) sim5SetScale(10);
    else if (id === 6) sim6Inspect('mon');
    else if (id === 7) sim7ToggleScale(6);
    else if (id === 8) sim8Select('sleep');
    else if (id === 9) sim9Highlight('sleep');
    else if (id === 10) sim10Update();
    else if (id === 11) sim11Measure('A');
    else if (id === 12) sim12Compare('max_min');
    else if (id === 13) sim13SelectDay('thu');
    else if (id === 14) sim14SetReduction(0);
    else if (id === 15) sim15CheckStatement(1);
    else if (id === 16) sim16SelectSolid('icosa');
}

// SIMULATOR 1: Raw Survey Field Notebook
function sim1Filter(cat) {
    playSound('click');
    sim1CurrentFilter = cat;
    const grid = document.getElementById('sim1_grid');
    const badge = document.getElementById('sim1_badge');
    const countEl = document.getElementById('sim1_count');
    const descEl = document.getElementById('sim1_desc');

    ['all', 'half', 'one', 'one_half', 'two', 'more'].forEach(c => {
        const b = document.getElementById(`sim1_btn_${c}`);
        if (b) {
            b.classList.remove('bg-amber-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim1_btn_${cat}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-amber-600', 'text-white', 'font-bold');
    }

    if (!grid) return;
    grid.innerHTML = '';

    let matchCount = 0;
    sim1Dataset.forEach((item, idx) => {
        const isMatch = (cat === 'all' || item.cat === cat);
        if (isMatch) matchCount++;
        const tag = document.createElement('span');
        tag.className = `px-2 py-1 rounded border font-mono transition-all ${isMatch ? 'bg-amber-500/20 text-amber-200 border-amber-500/40 font-bold scale-105' : 'bg-slate-900 text-slate-500 border-slate-800 opacity-40'}`;
        tag.textContent = `#${idx + 1}: ${item.val}`;
        grid.appendChild(tag);
    });

    if (badge) badge.textContent = `${matchCount} / 35 Friends`;
    if (countEl) countEl.textContent = `${matchCount} Matching Entries`;
    if (descEl) {
        if (cat === 'all') descEl.textContent = 'Raw data reflects initial unorganized survey notes before mathematical tallying.';
        else descEl.textContent = `Filtered category contains ${matchCount} out of 35 surveyed friends.`;
    }
}

// SIMULATOR 2: Frequency Distribution Table Builder
const sim2Data = [
    { name: '½ hour', tally: '<s>||||</s>', freq: 5 },
    { name: '1 hour', tally: '<s>||||</s> <s>||||</s> ||', freq: 12 },
    { name: '1½ hours', tally: '<s>||||</s> |||', freq: 8 },
    { name: '2 hours', tally: '<s>||||</s> |', freq: 6 },
    { name: '> 2 hours', tally: '||||', freq: 4 }
];

function sim2ShowAll() {
    playSound('correct');
    for (let i = 0; i < 5; i++) {
        const tEl = document.getElementById(`sim2_tally_${i}`);
        const fEl = document.getElementById(`sim2_freq_${i}`);
        if (tEl) tEl.innerHTML = sim2Data[i].tally;
        if (fEl) fEl.textContent = sim2Data[i].freq;
    }
}

function sim2StepTally() {
    playSound('tally');
    sim2CurrentStep = (sim2CurrentStep + 1) % 6;
    for (let i = 0; i < 5; i++) {
        const tEl = document.getElementById(`sim2_tally_${i}`);
        const fEl = document.getElementById(`sim2_freq_${i}`);
        if (i < sim2CurrentStep) {
            if (tEl) tEl.innerHTML = sim2Data[i].tally;
            if (fEl) fEl.textContent = sim2Data[i].freq;
        } else {
            if (tEl) tEl.innerHTML = '<span class="text-slate-600">...</span>';
            if (fEl) fEl.textContent = '-';
        }
    }
}

// SIMULATOR 3: TV Survey Subgroup Calculator
function sim3Subgroup(mode) {
    playSound('click');
    const title = document.getElementById('sim3_calc_title');
    const math = document.getElementById('sim3_calc_math');
    const desc = document.getElementById('sim3_calc_desc');
    const barLe = document.getElementById('sim3_bar_le');
    const barGt = document.getElementById('sim3_bar_gt');

    ['le1', 'gt1', 'gt2'].forEach(m => {
        const b = document.getElementById(`sim3_btn_${m}`);
        if (b) {
            b.classList.remove('bg-sky-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim3_btn_${mode}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-sky-600', 'text-white', 'font-bold');
    }

    if (mode === 'le1') {
        if (title) title.textContent = 'Subgroup: 1 Hour or Less';
        if (math) math.textContent = '5 (½ hr) + 12 (1 hr) = 17 Children';
        if (desc) desc.textContent = '17 out of 35 children (48.6%) adhere to healthy daily screen time recommendations.';
        if (barLe) barLe.style.width = '48.6%';
        if (barGt) barGt.style.width = '51.4%';
    } else if (mode === 'gt1') {
        if (title) title.textContent = 'Subgroup: More than 1 Hour';
        if (math) math.textContent = '8 (1½ hrs) + 6 (2 hrs) + 4 (>2 hrs) = 18 Children';
        if (desc) desc.textContent = '18 out of 35 children (51.4%) exceed recommended daily leisure screen time.';
        if (barLe) barLe.style.width = '48.6%';
        if (barGt) barGt.style.width = '51.4%';
    } else if (mode === 'gt2') {
        if (title) title.textContent = 'Subgroup: More than 2 Hours (Extreme)';
        if (math) math.textContent = '4 Children (>2 hrs)';
        if (desc) desc.textContent = '4 out of 35 children (11.4%) watch excessive television exceeding two hours daily.';
        if (barLe) barLe.style.width = '88.6%';
        if (barGt) barGt.style.width = '11.4%';
    }
}

// SIMULATOR 4: Toy Shop Stock Pictograph
function sim4Inspect(cat) {
    playSound('click');
    ['toys', 'games', 'sports'].forEach(c => {
        const r = document.getElementById(`sim4_row_${c}`);
        const b = document.getElementById(`sim4_btn_${c}`);
        if (r) {
            if (c === cat) {
                r.classList.add('border-amber-500/50', 'opacity-100');
                r.classList.remove('opacity-60');
            } else {
                r.classList.remove('border-amber-500/50', 'opacity-100');
                r.classList.add('opacity-60');
            }
        }
        if (b) {
            if (c === cat) {
                b.classList.remove('bg-slate-800');
                b.classList.add('bg-amber-600', 'text-white', 'font-bold');
            } else {
                b.classList.remove('bg-amber-600', 'text-white', 'font-bold');
                b.classList.add('bg-slate-800');
            }
        }
    });
}

// SIMULATOR 5: Custom Scale Transformer
function sim5SetScale(scale) {
    playSound('click');
    sim5CurrentScale = scale;
    const badge = document.getElementById('sim5_badge');
    const dispToys = document.getElementById('sim5_disp_toys');
    const dispGames = document.getElementById('sim5_disp_games');
    const dispSports = document.getElementById('sim5_disp_sports');
    const totalIcons = document.getElementById('sim5_total_icons');

    [5, 10, 2].forEach(s => {
        const b = document.getElementById(`sim5_btn_${s}`);
        if (b) {
            b.classList.remove('bg-teal-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim5_btn_${scale}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-teal-600', 'text-white', 'font-bold');
    }

    if (badge) badge.textContent = `Scale: 1 = ${scale}`;

    const nToys = 20 / scale;
    const nGames = 30 / scale;
    const nSports = 40 / scale;
    const sum = nToys + nGames + nSports;

    if (dispToys) dispToys.textContent = `${'⭐'.repeat(nToys)} (${nToys} Icons)`;
    if (dispGames) dispGames.textContent = `${'⭐'.repeat(nGames)} (${nGames} Icons)`;
    if (dispSports) dispSports.textContent = `${'⭐'.repeat(nSports)} (${nSports} Icons)`;
    if (totalIcons) totalIcons.textContent = `${nToys} + ${nGames} + ${nSports} = ${sum} Icons Total`;
}

// SIMULATOR 6: Two-Wheeler Roadside Traffic Tally
function sim6Inspect(day) {
    playSound('click');
    ['mon', 'wed', 'fri'].forEach(d => {
        const r = document.getElementById(`sim6_row_${d}`);
        const b = document.getElementById(`sim6_btn_${d}`);
        if (r) {
            if (d === day) {
                r.classList.add('border-indigo-500/50', 'opacity-100');
                r.classList.remove('opacity-60');
            } else {
                r.classList.remove('border-indigo-500/50', 'opacity-100');
                r.classList.add('opacity-60');
            }
        }
        if (b) {
            if (d === day) {
                b.classList.remove('bg-slate-800');
                b.classList.add('bg-indigo-600', 'text-white', 'font-bold');
            } else {
                b.classList.remove('bg-indigo-600', 'text-white', 'font-bold');
                b.classList.add('bg-slate-800');
            }
        }
    });
}

// SIMULATOR 7: Fractional Pictograph Re-scaling (Scale = 6)
function sim7ToggleScale(sc) {
    playSound('click');
    sim7CurrentScale = sc;
    const btn6 = document.getElementById('sim7_btn_scale6');
    const btn3 = document.getElementById('sim7_btn_scale3');
    const badge = document.getElementById('sim7_badge');
    const monIcons = document.getElementById('sim7_mon_icons');
    const wedIcons = document.getElementById('sim7_wed_icons');
    const friIcons = document.getElementById('sim7_fri_icons');
    const monMath = document.getElementById('sim7_mon_math');
    const wedMath = document.getElementById('sim7_wed_math');
    const friMath = document.getElementById('sim7_fri_math');

    if (sc === 6) {
        if (btn6) { btn6.classList.add('bg-sky-600', 'text-white', 'font-bold'); btn6.classList.remove('bg-slate-800'); }
        if (btn3) { btn3.classList.add('bg-slate-800'); btn3.classList.remove('bg-sky-600', 'text-white', 'font-bold'); }
        if (badge) badge.textContent = 'Full = 6 | Half = 3';
        if (monIcons) monIcons.textContent = '🛵🛵 🛺 (2½ Icons)';
        if (monMath) monMath.textContent = '6 + 6 + 3 = 15';
        if (wedIcons) wedIcons.textContent = '🛵 🛺 (1½ Icons)';
        if (wedMath) wedMath.textContent = '6 + 3 = 9';
        if (friIcons) friIcons.textContent = '🛵🛵🛵🛵 (4 Icons)';
        if (friMath) friMath.textContent = '6 × 4 = 24';
    } else {
        if (btn3) { btn3.classList.add('bg-sky-600', 'text-white', 'font-bold'); btn3.classList.remove('bg-slate-800'); }
        if (btn6) { btn6.classList.add('bg-slate-800'); btn6.classList.remove('bg-sky-600', 'text-white', 'font-bold'); }
        if (badge) badge.textContent = '1 Icon = 3 Vehicles';
        if (monIcons) monIcons.textContent = '🛵🛵🛵🛵🛵 (5 Icons)';
        if (monMath) monMath.textContent = '5 × 3 = 15';
        if (wedIcons) wedIcons.textContent = '🛵🛵🛵 (3 Icons)';
        if (wedMath) wedMath.textContent = '3 × 3 = 9';
        if (friIcons) friIcons.textContent = '🛵🛵🛵🛵🛵🛵🛵🛵 (8 Icons)';
        if (friMath) friMath.textContent = '8 × 3 = 24';
    }
}

// SIMULATOR 8: 24-Hour Icon Daily Schedule
const sim8Routines = {
    sleep: { name: '🛏️ Restful Sleep', hours: 8, icon: '🛏️', fraction: '8 / 24 = 1/3 of Day', color: 'text-indigo-400 bg-indigo-500/20' },
    school: { name: '🏫 School & Assembly', hours: 6, icon: '🏫', fraction: '6 / 24 = 1/4 of Day', color: 'text-amber-400 bg-amber-500/20' },
    study: { name: '📖 Focused Self-Study', hours: 2, icon: '📖', fraction: '2 / 24 = 1/12 of Day', color: 'text-cyan-400 bg-cyan-500/20' },
    play: { name: '⚽ Meals & Recreation', hours: 4, icon: '⚽', fraction: '4 / 24 = 1/6 of Day', color: 'text-emerald-400 bg-emerald-500/20' },
    other: { name: '⏳ Personal Care & Routines', hours: 4, icon: '⏳', fraction: '4 / 24 = 1/6 of Day', color: 'text-rose-400 bg-rose-500/20' }
};

function sim8Select(cat) {
    playSound('click');
    sim8ActiveCat = cat;
    const nameEl = document.getElementById('sim8_active_name');
    const fracEl = document.getElementById('sim8_fraction');
    const grid = document.getElementById('sim8_blocks_grid');

    ['sleep', 'school', 'study', 'play', 'other'].forEach(c => {
        const b = document.getElementById(`sim8_btn_${c}`);
        if (b) {
            b.classList.remove('bg-indigo-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim8_btn_${cat}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-indigo-600', 'text-white', 'font-bold');
    }

    const data = sim8Routines[cat];
    if (nameEl) nameEl.textContent = `${data.name} (${data.hours} Hours)`;
    if (fracEl) fracEl.textContent = data.fraction;

    if (!grid) return;
    grid.innerHTML = '';
    
    // Total 24 hours schedule
    const scheduleArray = [
        ...Array(8).fill('sleep'),
        ...Array(6).fill('school'),
        ...Array(2).fill('study'),
        ...Array(4).fill('play'),
        ...Array(4).fill('other')
    ];

    scheduleArray.forEach((type, hIdx) => {
        const box = document.createElement('div');
        const isActive = (type === cat);
        const itemData = sim8Routines[type];
        box.className = `p-1 rounded text-xs border transition-all ${isActive ? `${itemData.color} border-white/50 font-bold scale-105` : 'bg-slate-900 text-slate-500 border-slate-800 opacity-40'}`;
        box.textContent = `${hIdx + 1}h ${itemData.icon}`;
        grid.appendChild(box);
    });
}

// SIMULATOR 9: Routine Bar Graph
function sim9Highlight(act) {
    playSound('click');
    ['sleep', 'school', 'study', 'play', 'other'].forEach(a => {
        const bar = document.getElementById(`sim9_bar_${a}`);
        const btn = document.getElementById(`sim9_btn_${a}`);
        if (bar) {
            bar.setAttribute('opacity', a === act ? '1' : '0.35');
        }
        if (btn) {
            if (a === act) {
                btn.classList.add('bg-indigo-600', 'text-white', 'font-bold');
                btn.classList.remove('bg-slate-800');
            } else {
                btn.classList.remove('bg-indigo-600', 'text-white', 'font-bold');
                btn.classList.add('bg-slate-800');
            }
        }
    });

    const title = document.getElementById('sim9_act_title');
    const hours = document.getElementById('sim9_act_hours');
    const desc = document.getElementById('sim9_act_desc');

    if (act === 'sleep') {
        if (title) title.textContent = '🛏️ Restful Sleep';
        if (hours) hours.textContent = 'Height: 8 Hours';
        if (desc) desc.textContent = 'Occupies 8 out of 24 daily hours (1/3 of the full day). Tallest bar on the chart.';
    } else if (act === 'school') {
        if (title) title.textContent = '🏫 School & Assembly';
        if (hours) hours.textContent = 'Height: 6 Hours';
        if (desc) desc.textContent = 'Classroom learning from morning to afternoon.';
    } else if (act === 'study') {
        if (title) title.textContent = '📖 Focused Self-Study';
        if (hours) hours.textContent = 'Height: 2 Hours (Shortest)';
        if (desc) desc.textContent = 'Home study and revision tasks.';
    } else if (act === 'play') {
        if (title) title.textContent = '⚽ Meals & Play';
        if (hours) hours.textContent = 'Height: 4 Hours';
        if (desc) desc.textContent = 'Nourishment and active outdoor games.';
    } else if (act === 'other') {
        if (title) title.textContent = '⏳ Other Daily Routines';
        if (hours) hours.textContent = 'Height: 4 Hours';
        if (desc) desc.textContent = 'Commute, dressing, family conversations.';
    }
}

// SIMULATOR 10: Schedule Balance & Equity Analyzer
function sim10Update() {
    const sSleep = document.getElementById('sim10_slider_sleep');
    const sStudy = document.getElementById('sim10_slider_study');
    if (!sSleep || !sStudy) return;

    const sleep = parseInt(sSleep.value, 10);
    const study = parseInt(sStudy.value, 10);
    const school = 6;
    const edu = school + study;
    const playAndOther = 24 - (sleep + edu);

    const txtSleep = document.getElementById('sim10_sleep_txt');
    const txtStudy = document.getElementById('sim10_study_txt');
    const dispSleep = document.getElementById('sim10_disp_sleep');
    const dispEdu = document.getElementById('sim10_disp_edu');
    const dispPlay = document.getElementById('sim10_disp_play');
    const status = document.getElementById('sim10_balance_status');
    const desc = document.getElementById('sim10_balance_desc');

    if (txtSleep) txtSleep.textContent = `${sleep}h`;
    if (txtStudy) txtStudy.textContent = `${study}h`;
    if (dispSleep) dispSleep.textContent = `${sleep} Hours`;
    if (dispEdu) dispEdu.textContent = `${edu} Hours (6+${study})`;
    if (dispPlay) dispPlay.textContent = `${playAndOther} Hours`;

    if (status && desc) {
        if (sleep === 8 && edu === 8 && playAndOther === 8) {
            status.textContent = '✓ Perfectly Balanced Three-Part Day (8-8-8)';
            status.className = 'text-emerald-400 font-bold block mb-0.5';
            desc.textContent = '1/3 of the day is allocated to sleep, 1/3 to education, and 1/3 to recreation and living.';
        } else if (playAndOther < 6) {
            status.textContent = '⚠️ Tight Schedule Alert: Low Free Time';
            status.className = 'text-rose-400 font-bold block mb-0.5';
            desc.textContent = `Only ${playAndOther} hours remaining for meals and relaxation!`;
        } else {
            status.textContent = '⚖️ Custom Schedule Balance';
            status.className = 'text-sky-400 font-bold block mb-0.5';
            desc.textContent = `Sum: ${sleep}h Sleep + ${edu}h Education + ${playAndOther}h Life = 24 Hours.`;
        }
    }
}

// SIMULATOR 11: Paper Strip Finger Measuring Lab
const sim11Data = {
    A: { name: 'Friend A', len: 4.5, heightPx: 90, y: 40 },
    B: { name: 'Friend B', len: 5.0, heightPx: 100, y: 30 },
    C: { name: 'Friend C', len: 5.8, heightPx: 116, y: 14 },
    D: { name: 'Friend D', len: 4.2, heightPx: 84, y: 46 }
};

function sim11Measure(friend) {
    playSound('click');
    ['A', 'B', 'C', 'D'].forEach(f => {
        const b = document.getElementById(`sim11_btn_${f.toLowerCase()}`);
        if (b) {
            b.classList.remove('bg-teal-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim11_btn_${friend.toLowerCase()}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-teal-600', 'text-white', 'font-bold');
    }

    const data = sim11Data[friend];
    const strip = document.getElementById('sim11_strip');
    const cutLine = document.getElementById('sim11_cut_line');
    const label = document.getElementById('sim11_label');
    const nameEl = document.getElementById('sim11_friend_name');
    const lenDisp = document.getElementById('sim11_len_disp');

    if (strip) {
        strip.setAttribute('y', data.y);
        strip.setAttribute('height', data.heightPx);
    }
    if (cutLine) {
        cutLine.setAttribute('y1', data.y);
        cutLine.setAttribute('y2', data.y);
    }
    if (label) {
        label.setAttribute('y', data.y - 5);
        label.textContent = `${data.len} cm`;
    }
    if (nameEl) nameEl.textContent = `${data.name} Measurement`;
    if (lenDisp) lenDisp.textContent = `Index Finger: ${data.len} cm`;
}

// SIMULATOR 12: Physical Strip Bar Graph Canvas
function sim12Compare(mode) {
    playSound('click');
    const rangeLine = document.getElementById('sim12_range_line');
    const title = document.getElementById('sim12_comp_title');
    const math = document.getElementById('sim12_comp_math');
    const desc = document.getElementById('sim12_comp_desc');
    const btnDiff = document.getElementById('sim12_btn_diff');
    const btnAll = document.getElementById('sim12_btn_all');

    if (mode === 'max_min') {
        if (btnDiff) { btnDiff.classList.add('bg-emerald-600', 'text-white'); btnDiff.classList.remove('bg-slate-800'); }
        if (btnAll) { btnAll.classList.add('bg-slate-800'); btnAll.classList.remove('bg-emerald-600', 'text-white'); }
        if (rangeLine) rangeLine.setAttribute('opacity', '1');
        if (title) title.textContent = 'Spread Across Measured Cohort';
        if (math) math.textContent = 'Range = 5.8 - 4.2 = 1.6 cm';
        if (desc) desc.textContent = 'Friend C possesses the longest finger (5.8 cm), while Friend D has the shortest (4.2 cm).';
    } else {
        if (btnAll) { btnAll.classList.add('bg-emerald-600', 'text-white'); btnAll.classList.remove('bg-slate-800'); }
        if (btnDiff) { btnDiff.classList.add('bg-slate-800'); btnDiff.classList.remove('bg-emerald-600', 'text-white'); }
        if (rangeLine) rangeLine.setAttribute('opacity', '0.2');
        if (title) title.textContent = 'All 4 Pasted Paper Strips';
        if (math) math.textContent = 'D: 4.2 | A: 4.5 | B: 5.0 | C: 5.8 cm';
        if (desc) desc.textContent = 'Notice that every strip starts precisely at Baseline = 0 cm for valid visual comparison.';
    }
}

// SIMULATOR 13: Canteen Food Waste Notice Board
const sim13Data = {
    mon: { day: 'Monday: Sandwich Day', waste: '4 kg', desc: 'Moderate waste recorded from crusts and packaging.' },
    tue: { day: 'Tuesday: Paratha Day', waste: '7 kg', desc: 'Elevated waste due to rich filling portions.' },
    wed: { day: 'Wednesday: Khichdi Day', waste: '3 kg (Lowest)', desc: 'Lowest waste of the week; high student approval.' },
    thu: { day: 'Thursday: Puri-Sabzi Day', waste: '8 kg (Peak Waste)', desc: 'Highest waste of the week. Oily portion adjustment needed.' },
    fri: { day: 'Friday: Idli-Sambar Day', waste: '5 kg', desc: 'Average waste level across the cafeteria.' }
};

function sim13SelectDay(day) {
    playSound('click');
    ['mon', 'tue', 'wed', 'thu', 'fri'].forEach(d => {
        const bar = document.getElementById(`sim13_bar_${d}`);
        const btn = document.getElementById(`sim13_btn_${d}`);
        if (bar) {
            bar.setAttribute('opacity', d === day ? '1' : '0.35');
        }
        if (btn) {
            if (d === day) {
                btn.classList.add('bg-rose-600', 'text-white', 'font-bold');
                btn.classList.remove('bg-slate-800');
            } else {
                btn.classList.remove('bg-rose-600', 'text-white', 'font-bold');
                btn.classList.add('bg-slate-800');
            }
        }
    });

    const info = sim13Data[day];
    const nameEl = document.getElementById('sim13_day_name');
    const wasteEl = document.getElementById('sim13_day_waste');
    const descEl = document.getElementById('sim13_day_desc');

    if (nameEl) nameEl.textContent = info.day;
    if (wasteEl) wasteEl.textContent = `Plate Waste: ${info.waste}`;
    if (descEl) descEl.textContent = info.desc;
}

// SIMULATOR 14: Food Waste Meal Saver Calculator
function sim14SetReduction(percent) {
    playSound('click');
    sim14Reduction = percent;
    [0, 25, 50].forEach(p => {
        const b = document.getElementById(`sim14_btn_${p}`);
        if (b) {
            b.classList.remove('bg-rose-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim14_btn_${percent}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-rose-600', 'text-white', 'font-bold');
    }

    const baseline = 27.0;
    const currentWaste = baseline * (1 - percent / 100);
    const wastedMeals = Math.round(currentWaste * 3);
    const savedMeals = Math.round((baseline - currentWaste) * 3);

    const wasteEl = document.getElementById('sim14_waste_kg');
    const mealsEl = document.getElementById('sim14_meals_wasted');
    const impactEl = document.getElementById('sim14_impact_txt');

    if (wasteEl) wasteEl.textContent = `${currentWaste.toFixed(1)} kg`;
    if (mealsEl) mealsEl.textContent = `${wastedMeals} Child Meals`;
    if (impactEl) {
        if (percent === 0) {
            impactEl.textContent = 'At baseline, 27 kg of discarded food equals 81 meals that could have fed children. Reducing waste saves resources and protects the environment.';
        } else {
            impactEl.textContent = `With a ${percent}% reduction, the canteen saves ${(baseline - currentWaste).toFixed(1)} kg of food, preserving ${savedMeals} wholesome child meals every week!`;
        }
    }
}

// SIMULATOR 15: Courtyard Picture Logic Checker
const sim15Claims = {
    1: { claim: 'Claim 1: "Exactly 5 children are wearing caps."', verdict: 'Verdict: TRUE ✓ (Visual Count = 5)', proof: 'Careful scanning reveals 5 cap wearers among the 12 children in the courtyard.' },
    2: { claim: 'Claim 2: "More children are wearing glasses than backpacks."', verdict: 'Verdict: FALSE ✗ (Glasses: 4, Backpacks: 6)', proof: 'Since 4 is less than 6, the claim that glasses exceed backpacks is mathematically false.' },
    3: { claim: 'Claim 3: "3 children are wearing both a cap and glasses."', verdict: 'Verdict: FALSE ✗ (Overlap Count = 2)', proof: 'Only 2 students simultaneously wear both accessories.' }
};

function sim15CheckStatement(num) {
    playSound('click');
    [1, 2, 3].forEach(n => {
        const b = document.getElementById(`sim15_btn_s${n}`);
        if (b) {
            b.classList.remove('bg-cyan-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const activeBtn = document.getElementById(`sim15_btn_s${num}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800');
        activeBtn.classList.add('bg-cyan-600', 'text-white', 'font-bold');
    }

    const c = sim15Claims[num];
    const claimEl = document.getElementById('sim15_claim_txt');
    const verdictEl = document.getElementById('sim15_verdict');
    const proofEl = document.getElementById('sim15_proof');

    if (claimEl) claimEl.textContent = c.claim;
    if (verdictEl) verdictEl.textContent = c.verdict;
    if (proofEl) proofEl.textContent = c.proof;
}

// SIMULATOR 16: Regular Polyhedral Nets Explorer
function sim16SelectSolid(solid) {
    playSound('click');
    const btnI = document.getElementById('sim16_btn_icosa');
    const btnD = document.getElementById('sim16_btn_dodeca');
    const badge = document.getElementById('sim16_badge');
    const solidName = document.getElementById('sim16_solid_name');
    const props = document.getElementById('sim16_props');
    const caption = document.getElementById('sim16_net_caption');

    if (solid === 'icosa') {
        if (btnI) { btnI.classList.add('bg-violet-600', 'text-white', 'font-bold'); btnI.classList.remove('bg-slate-800'); }
        if (btnD) { btnD.classList.add('bg-slate-800'); btnD.classList.remove('bg-violet-600', 'text-white', 'font-bold'); }
        if (badge) badge.textContent = 'Icosahedron (20)';
        if (solidName) solidName.textContent = '🔷 Regular Icosahedron';
        if (props) {
            props.innerHTML = `
            <div>• Faces (F): 20 Equilateral Triangles</div>
            <div>• Vertices (V): 12 Corners</div>
            <div>• Edges (E): 30 Creased Lines</div>`;
        }
        if (caption) caption.textContent = '20 Equilateral Triangles';
    } else {
        if (btnD) { btnD.classList.add('bg-violet-600', 'text-white', 'font-bold'); btnD.classList.remove('bg-slate-800'); }
        if (btnI) { btnI.classList.add('bg-slate-800'); btnI.classList.remove('bg-violet-600', 'text-white', 'font-bold'); }
        if (badge) badge.textContent = 'Dodecahedron (12)';
        if (solidName) solidName.textContent = '⬟ Regular Dodecahedron';
        if (props) {
            props.innerHTML = `
            <div>• Faces (F): 12 Regular Pentagons</div>
            <div>• Vertices (V): 20 Corners</div>
            <div>• Edges (E): 30 Creased Lines</div>`;
        }
        if (caption) caption.textContent = '12 Regular Pentagons';
    }
}

// Window Onload Initialization
window.addEventListener('DOMContentLoaded', () => {
    populateVoiceList();
    renderSlide();
});
'''

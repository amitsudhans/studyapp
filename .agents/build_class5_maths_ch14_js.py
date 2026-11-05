# -*- coding: utf-8 -*-
"""JavaScript Engine Builder for Chapter 14: Maps and Locations"""

js_code = """
// State Variables
let currentSlide = 0;
let synth = window.speechSynthesis;
let currentUtterance = null;
let keepAliveTimer = null;
let userPreferredVoice = null;
let quizScores = { 17: {}, 18: {}, 19: {}, 20: {} };

// Simulators Internal State
let sim1AnimTimer = null;
let sim1Step = 0;
let sim6Angle = 0;
let sim7StopIdx = 0;
let sim12Step = 0;

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
        } else if (type === 'fly') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(320, now);
            osc.frequency.exponentialRampToValueAtTime(640, now + 0.15);
            gain.gain.setValueAtTime(0.1, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
            osc.start(now);
            osc.stop(now + 0.2);
        } else if (type === 'turn') {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(280, now);
            osc.frequency.exponentialRampToValueAtTime(380, now + 0.08);
            gain.gain.setValueAtTime(0.08, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
            osc.start(now);
            osc.stop(now + 0.1);
        }
    } catch (e) {
        // Audio might be blocked before first user click
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
    if (id === 1) sim1Reset();
    else if (id === 2) sim2Face('east');
    else if (id === 3) sim3Reset();
    else if (id === 4) sim4Reset();
    else if (id === 5) sim5Inspect('window');
    else if (id === 6) sim6Reset();
    else if (id === 7) sim7Reset();
    else if (id === 8) sim8SelectRoute('r1');
    else if (id === 9) sim9FilterLine('all');
    else if (id === 10) sim10SelectRoute('A');
    else if (id === 11) sim11Highlight('building');
    else if (id === 12) sim12Reset();
    else if (id === 13) sim13SelectFood('laddoo');
    else if (id === 14) sim14ShowRoute('EN');
    else if (id === 15) sim15Update();
    else if (id === 16) sim16Plot('panda');
}

// SIMULATOR 1: Siberian Crane Migration
function sim1AnimateFlight() {
    if (sim1AnimTimer) clearInterval(sim1AnimTimer);
    const crane = document.getElementById('sim1_crane');
    const distEl = document.getElementById('sim1_dist');
    const btn = document.getElementById('sim1_fly_btn');
    if (btn) btn.disabled = true;

    playSound('fly');
    sim1Step = 0;
    const totalSteps = 40;
    // Quadratic bezier curve from (50, 25) via (120, 70) to (100, 135)
    sim1AnimTimer = setInterval(() => {
        sim1Step++;
        const t = sim1Step / totalSteps;
        const x = (1 - t) * (1 - t) * 50 + 2 * (1 - t) * t * 120 + t * t * 100;
        const y = (1 - t) * (1 - t) * 25 + 2 * (1 - t) * t * 70 + t * t * 135;
        if (crane) crane.setAttribute('transform', `translate(${x}, ${y})`);
        const km = Math.round(t * 5200);
        if (distEl) distEl.textContent = `${km.toLocaleString()} km / 5,200 km`;

        if (sim1Step >= totalSteps) {
            clearInterval(sim1AnimTimer);
            if (btn) {
                btn.disabled = false;
                btn.textContent = 'Arrived at Bharatpur! (Fly Again)';
            }
        }
    }, 40);
}

function sim1Reset() {
    if (sim1AnimTimer) clearInterval(sim1AnimTimer);
    const crane = document.getElementById('sim1_crane');
    const distEl = document.getElementById('sim1_dist');
    const btn = document.getElementById('sim1_fly_btn');
    if (crane) crane.setAttribute('transform', 'translate(50, 25)');
    if (distEl) distEl.textContent = '0 km / 5,200 km';
    if (btn) {
        btn.disabled = false;
        btn.textContent = 'Start Southward Flight ➔';
    }
}

// SIMULATOR 2: Sun & Cardinal Directions
function sim2Face(dir) {
    playSound('turn');
    const badge = document.getElementById('sim2_badge');
    const pointer = document.getElementById('sim2_pointer');
    const frontEl = document.getElementById('sim2_front');
    const leftEl = document.getElementById('sim2_left');
    const rightEl = document.getElementById('sim2_right');
    const backEl = document.getElementById('sim2_back');

    ['east', 'north', 'west', 'south'].forEach(d => {
        const b = document.getElementById(`sim2_btn_${d}`);
        if (b) {
            b.classList.remove('bg-amber-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800', 'text-slate-200');
        }
    });
    const activeBtn = document.getElementById(`sim2_btn_${dir}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800', 'text-slate-200');
        activeBtn.classList.add('bg-amber-600', 'text-white', 'font-bold');
    }

    if (dir === 'east') {
        if (badge) badge.textContent = 'Facing East (Sun)';
        if (pointer) pointer.setAttribute('transform', 'rotate(90, 90, 70)');
        if (frontEl) frontEl.textContent = 'East (Rising Sun)';
        if (leftEl) leftEl.textContent = 'North';
        if (rightEl) rightEl.textContent = 'South';
        if (backEl) backEl.textContent = 'West (Setting Sun)';
    } else if (dir === 'north') {
        if (badge) badge.textContent = 'Facing North';
        if (pointer) pointer.setAttribute('transform', 'rotate(0, 90, 70)');
        if (frontEl) frontEl.textContent = 'North';
        if (leftEl) leftEl.textContent = 'West';
        if (rightEl) rightEl.textContent = 'East';
        if (backEl) backEl.textContent = 'South';
    } else if (dir === 'west') {
        if (badge) badge.textContent = 'Facing West';
        if (pointer) pointer.setAttribute('transform', 'rotate(270, 90, 70)');
        if (frontEl) frontEl.textContent = 'West (Setting Sun)';
        if (leftEl) leftEl.textContent = 'South';
        if (rightEl) rightEl.textContent = 'North';
        if (backEl) backEl.textContent = 'East (Rising Sun)';
    } else if (dir === 'south') {
        if (badge) badge.textContent = 'Facing South';
        if (pointer) pointer.setAttribute('transform', 'rotate(180, 90, 70)');
        if (frontEl) frontEl.textContent = 'South';
        if (leftEl) leftEl.textContent = 'East';
        if (rightEl) rightEl.textContent = 'West';
        if (backEl) backEl.textContent = 'North';
    }
}

// SIMULATOR 3: Four Little Chicks Flight
function sim3FlyChicks() {
    playSound('fly');
    const c1 = document.getElementById('sim3_c1'); // North
    const c2 = document.getElementById('sim3_c2'); // East
    const c3 = document.getElementById('sim3_c3'); // South
    const c4 = document.getElementById('sim3_c4'); // West

    if (c1) { c1.setAttribute('cx', '80'); c1.setAttribute('cy', '25'); }
    if (c2) { c2.setAttribute('cx', '135'); c2.setAttribute('cy', '70'); }
    if (c3) { c3.setAttribute('cx', '80'); c3.setAttribute('cy', '115'); }
    if (c4) { c4.setAttribute('cx', '25'); c4.setAttribute('cy', '70'); }
}

function sim3Reset() {
    playSound('click');
    const c1 = document.getElementById('sim3_c1');
    const c2 = document.getElementById('sim3_c2');
    const c3 = document.getElementById('sim3_c3');
    const c4 = document.getElementById('sim3_c4');
    [c1, c2, c3, c4].forEach(c => {
        if (c) {
            c.setAttribute('cx', '80');
            c.setAttribute('cy', '70');
        }
    });
}

// SIMULATOR 4: Campsite Legend Reading
function sim4ColorTents() {
    playSound('correct');
    const tw = document.getElementById('sim4_t_west');
    const tl = document.getElementById('sim4_t_lake');
    const tn = document.getElementById('sim4_t_north');
    const ts = document.getElementById('sim4_t_south');

    if (tw) tw.setAttribute('fill', '#3b82f6'); // Blue
    if (tl) tl.setAttribute('fill', '#10b981'); // Green
    if (tn) tn.setAttribute('fill', '#a855f7'); // Purple
    if (ts) ts.setAttribute('fill', '#eab308'); // Yellow
}

function sim4AddEastTent() {
    playSound('correct');
    const te = document.getElementById('sim4_t_east');
    if (te) te.setAttribute('opacity', '1');
}

function sim4Reset() {
    playSound('click');
    const tw = document.getElementById('sim4_t_west');
    const tl = document.getElementById('sim4_t_lake');
    const tn = document.getElementById('sim4_t_north');
    const ts = document.getElementById('sim4_t_south');
    const te = document.getElementById('sim4_t_east');

    if (tw) tw.setAttribute('fill', '#475569');
    if (tl) tl.setAttribute('fill', '#475569');
    if (tn) tn.setAttribute('fill', '#475569');
    if (ts) ts.setAttribute('fill', '#475569');
    if (te) te.setAttribute('opacity', '0');
}

// SIMULATOR 5: Room Layout Map
function sim5Inspect(item) {
    playSound('click');
    const title = document.getElementById('sim5_item_title');
    const card = document.getElementById('sim5_cardinal');
    const rel = document.getElementById('sim5_relative');

    ['window', 'bed', 'door', 'cupboard'].forEach(i => {
        const b = document.getElementById(`sim5_btn_${i}`);
        if (b) {
            b.classList.remove('bg-cyan-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800', 'text-slate-200');
        }
    });
    const active = document.getElementById(`sim5_btn_${item}`);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-200');
        active.classList.add('bg-cyan-600', 'text-white', 'font-bold');
    }

    if (item === 'window') {
        if (title) title.textContent = 'Window on Northern Wall';
        if (card) card.textContent = 'Cardinal Direction: North';
        if (rel) rel.textContent = 'Relative to Observer: Straight Ahead (Front)';
    } else if (item === 'bed') {
        if (title) title.textContent = 'Bed along Eastern Wall';
        if (card) card.textContent = 'Cardinal Direction: East';
        if (rel) rel.textContent = 'Relative to Observer: To the Right Hand';
    } else if (item === 'door') {
        if (title) title.textContent = 'Entrance Door on Southern Wall';
        if (card) card.textContent = 'Cardinal Direction: South';
        if (rel) rel.textContent = 'Relative to Observer: Behind Back';
    } else if (item === 'cupboard') {
        if (title) title.textContent = 'Cupboard along Western Wall';
        if (card) card.textContent = 'Cardinal Direction: West';
        if (rel) rel.textContent = 'Relative to Observer: To the Left Hand';
    }
}

// SIMULATOR 6: Relative Directions vs Fixed Cardinal
function sim6Turn(delta) {
    playSound('turn');
    sim6Angle = (sim6Angle + delta) % 360;
    if (sim6Angle < 0) sim6Angle += 360;

    const avatar = document.getElementById('sim6_avatar');
    if (avatar) avatar.setAttribute('transform', `rotate(${sim6Angle}, 80, 70)`);

    const badge = document.getElementById('sim6_heading_txt');
    const fEl = document.getElementById('sim6_facing');
    const rEl = document.getElementById('sim6_right');
    const lEl = document.getElementById('sim6_left');

    const directions = [
        { deg: 0, face: 'North', right: 'East', left: 'West' },
        { deg: 90, face: 'East', right: 'South', left: 'North' },
        { deg: 180, face: 'South', right: 'West', left: 'East' },
        { deg: 270, face: 'West', right: 'North', left: 'South' }
    ];
    const curr = directions.find(d => d.deg === sim6Angle) || directions[0];

    if (badge) badge.textContent = `Facing: ${curr.face} (${sim6Angle}°)`;
    if (fEl) fEl.textContent = curr.face;
    if (rEl) rEl.textContent = curr.right;
    if (lEl) lEl.textContent = curr.left;
}

function sim6Reset() {
    sim6Angle = 0;
    sim6Turn(0);
}

// SIMULATOR 7: School Bus Route Navigator
const sim7Stops = [
    { name: 'Depot (Start)', x: 20, y: 85, desc: 'Bus starts at Central Bus Depot facing North.' },
    { name: 'Stop 1 (Turn Right onto MG Road)', x: 90, y: 85, desc: 'Bus drives East along Station Road to Stop 1.' },
    { name: 'Stop 2 (Turn Left onto School Lane)', x: 90, y: 35, desc: 'Bus turns North onto MG Road to reach Stop 2.' },
    { name: 'Stop 3 (Turn Right onto Ring Road)', x: 200, y: 35, desc: 'Bus turns East onto School Lane reaching Stop 3.' },
    { name: 'Zoo Highway (Final Destination)', x: 290, y: 35, desc: 'Bus reaches Zoo Highway terminus safely!' }
];

function sim7Step() {
    playSound('click');
    sim7StopIdx = (sim7StopIdx + 1) % sim7Stops.length;
    const st = sim7Stops[sim7StopIdx];
    const bus = document.getElementById('sim7_bus');
    const status = document.getElementById('sim7_status');
    const log = document.getElementById('sim7_log');

    if (bus) bus.setAttribute('transform', `translate(${st.x}, ${st.y})`);
    if (status) status.textContent = st.name;
    if (log) log.textContent = st.desc;
}

function sim7Reset() {
    sim7StopIdx = 0;
    const st = sim7Stops[0];
    const bus = document.getElementById('sim7_bus');
    const status = document.getElementById('sim7_status');
    const log = document.getElementById('sim7_log');

    if (bus) bus.setAttribute('transform', `translate(${st.x}, ${st.y})`);
    if (status) status.textContent = 'At Depot';
    if (log) log.textContent = 'Bus ready at Depot. Click Next to depart!';
}

// SIMULATOR 8: Manhattan Grid Distance Calculator
function sim8SelectRoute(key) {
    playSound('click');
    const path = document.getElementById('sim8_path');
    const title = document.getElementById('sim8_route_title');
    const dist = document.getElementById('sim8_dist_calc');
    const eff = document.getElementById('sim8_efficiency');

    ['r1', 'r2', 'r3', 'r4'].forEach(k => {
        const b = document.getElementById(`sim8_btn_${k}`);
        if (b) {
            b.classList.remove('bg-indigo-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800', 'text-slate-200');
        }
    });
    const active = document.getElementById(`sim8_btn_${key}`);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-200');
        active.classList.add('bg-indigo-600', 'text-white', 'font-bold');
    }

    if (key === 'r1') {
        if (path) path.setAttribute('d', 'M 20 110 L 140 110 L 140 20');
        if (title) title.textContent = 'Route 1: 3 East + 4 North';
        if (dist) dist.textContent = 'Total Distance = 3 + 4 = 7 Blocks';
        if (eff) eff.textContent = 'Minimal Manhattan grid distance without backtracking.';
    } else if (key === 'r2') {
        if (path) path.setAttribute('d', 'M 20 110 L 20 20 L 140 20');
        if (title) title.textContent = 'Route 2: 4 North + 3 East';
        if (dist) dist.textContent = 'Total Distance = 4 + 3 = 7 Blocks';
        if (eff) eff.textContent = 'Identical minimal distance (7 blocks) moving strictly North then East.';
    } else if (key === 'r3') {
        if (path) path.setAttribute('d', 'M 20 110 L 60 110 L 60 65 L 100 65 L 100 20 L 140 20');
        if (title) title.textContent = 'Route 3: Staircase Zig-Zag';
        if (dist) dist.textContent = 'Total Distance = 1E + 2N + 1E + 2N + 1E = 7 Blocks';
        if (eff) eff.textContent = 'Still minimal 7 blocks because all steps head East and North!';
    } else if (key === 'r4') {
        if (path) path.setAttribute('d', 'M 20 110 L 20 130 L 140 130 L 140 20');
        if (title) title.textContent = 'Route 4: Backtracking Detour';
        if (dist) dist.textContent = 'Total Distance = 1 South + 3 East + 5 North = 9 Blocks';
        if (eff) eff.textContent = 'Wasteful detour! Backtracking South increases journey length by 2 blocks.';
    }
}

// SIMULATOR 9: Delhi Metro Network Map
function sim9FilterLine(line) {
    playSound('click');
    const red = document.getElementById('sim9_line_red');
    const yellow = document.getElementById('sim9_line_yellow');
    const blue = document.getElementById('sim9_line_blue');
    const violet = document.getElementById('sim9_line_violet');
    const status = document.getElementById('sim9_status');
    const title = document.getElementById('sim9_info_title');
    const desc = document.getElementById('sim9_info_desc');

    ['all', 'yellow', 'blue', 'red', 'hubs'].forEach(l => {
        const b = document.getElementById(`sim9_btn_${l}`);
        if (b) {
            b.classList.remove('bg-amber-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const active = document.getElementById(`sim9_btn_${line}`);
    if (active) {
        active.classList.remove('bg-slate-800');
        active.classList.add('bg-amber-600', 'text-white', 'font-bold');
    }

    if (line === 'all') {
        if (red) red.setAttribute('opacity', '1');
        if (yellow) yellow.setAttribute('opacity', '1');
        if (blue) blue.setAttribute('opacity', '1');
        if (violet) violet.setAttribute('opacity', '0.8');
        if (status) status.textContent = 'All 4 Lines Visible';
        if (title) title.textContent = 'Delhi Metro Network Map';
        if (desc) desc.textContent = 'Schematic maps use straight 90° and 45° angle lines rather than realistic curved geography for instant readability.';
    } else if (line === 'yellow') {
        if (red) red.setAttribute('opacity', '0.15');
        if (yellow) yellow.setAttribute('opacity', '1');
        if (blue) blue.setAttribute('opacity', '0.15');
        if (violet) violet.setAttribute('opacity', '0.15');
        if (status) status.textContent = 'Yellow Line: North-South';
        if (title) title.textContent = 'Yellow Line (Samaypur Badli ➔ Millenium City)';
        if (desc) desc.textContent = 'Runs vertically from North to South, connecting Kashmere Gate, Rajiv Chowk, and Qutb Minar.';
    } else if (line === 'blue') {
        if (red) red.setAttribute('opacity', '0.15');
        if (yellow) yellow.setAttribute('opacity', '0.15');
        if (blue) blue.setAttribute('opacity', '1');
        if (violet) violet.setAttribute('opacity', '0.15');
        if (status) status.textContent = 'Blue Line: East-West';
        if (title) title.textContent = 'Blue Line (Dwarka ➔ Vaishali / Noida)';
        if (desc) desc.textContent = 'Traverses East-West across central Delhi, connecting Rajiv Chowk, Mandi House, and Supreme Court.';
    } else if (line === 'red') {
        if (red) red.setAttribute('opacity', '1');
        if (yellow) yellow.setAttribute('opacity', '0.15');
        if (blue) blue.setAttribute('opacity', '0.15');
        if (violet) violet.setAttribute('opacity', '0.15');
        if (status) status.textContent = 'Red Line: Rithala ➔ Ghaziabad';
        if (title) title.textContent = 'Red Line (Northern Cross-Corridor)';
        if (desc) desc.textContent = 'First line constructed, intersecting Yellow and Violet lines at Kashmere Gate hub.';
    } else if (line === 'hubs') {
        if (red) red.setAttribute('opacity', '0.4');
        if (yellow) yellow.setAttribute('opacity', '0.4');
        if (blue) blue.setAttribute('opacity', '0.4');
        if (violet) violet.setAttribute('opacity', '0.4');
        if (status) status.textContent = 'Key Interchange Hubs';
        if (title) title.textContent = 'Interchange Transfer Stations';
        if (desc) desc.textContent = 'Rajiv Chowk (Yellow + Blue) & Kashmere Gate (Red + Yellow + Violet) permit switching trains without exiting!';
    }
}

// SIMULATOR 10: Metro Route Optimizer
function sim10SelectRoute(rt) {
    playSound('click');
    const pa = document.getElementById('sim10_path_a');
    const pa2 = document.getElementById('sim10_path_a2');
    const pb = document.getElementById('sim10_path_b');
    const btnA = document.getElementById('sim10_btn_a');
    const btnB = document.getElementById('sim10_btn_b');
    const title = document.getElementById('sim10_route_title');
    const breakdown = document.getElementById('sim10_breakdown');
    const metrics = document.getElementById('sim10_metrics');

    if (rt === 'A') {
        if (btnA) { btnA.classList.add('bg-sky-600', 'text-white'); btnA.classList.remove('bg-slate-800'); }
        if (btnB) { btnB.classList.add('bg-slate-800', 'text-slate-200'); btnB.classList.remove('bg-sky-600'); }
        if (pa) pa.setAttribute('opacity', '1');
        if (pa2) pa2.setAttribute('opacity', '1');
        if (pb) pb.setAttribute('opacity', '0.1');
        if (title) title.textContent = 'Route A: Optimal 1-Interchange';
        if (breakdown) {
            breakdown.innerHTML = `
            <div>• Yellow Line: Qutb Minar ➔ Rajiv Chowk (14 stops)</div>
            <div>• Interchange 1: Switch at Rajiv Chowk to Blue Line</div>
            <div>• Blue Line: Rajiv Chowk ➔ Supreme Court (2 stops)</div>`;
        }
        if (metrics) metrics.textContent = '16 Stops | 1 Transfer';
    } else {
        if (btnB) { btnB.classList.add('bg-sky-600', 'text-white'); btnB.classList.remove('bg-slate-800'); }
        if (btnA) { btnA.classList.add('bg-slate-800', 'text-slate-200'); btnA.classList.remove('bg-sky-600'); }
        if (pa) pa.setAttribute('opacity', '0.1');
        if (pa2) pa2.setAttribute('opacity', '0.1');
        if (pb) pb.setAttribute('opacity', '1');
        if (title) title.textContent = 'Route B: Double Transfer Alternate';
        if (breakdown) {
            breakdown.innerHTML = `
            <div>• Yellow Line: Qutb Minar ➔ Hauz Khas (4 stops)</div>
            <div>• Interchange 1: Transfer to Magenta Line (10 stops)</div>
            <div>• Interchange 2: Transfer to Blue Line (2 stops)</div>`;
        }
        if (metrics) metrics.textContent = '16 Stops | 2 Transfers (Slower)';
    }
}

// SIMULATOR 11: School Map Symbols & Legend
function sim11Highlight(sym) {
    playSound('click');
    const bld = document.getElementById('sim11_sym_building');
    const gt = document.getElementById('sim11_sym_gate');
    const tk = document.getElementById('sim11_sym_tank');
    const gd = document.getElementById('sim11_sym_garden');
    const bc = document.getElementById('sim11_sym_bench');
    const name = document.getElementById('sim11_legend_name');
    const desc = document.getElementById('sim11_legend_desc');
    const stat = document.getElementById('sim11_feat_stat');

    ['building', 'gate', 'tank', 'garden', 'bench', 'all'].forEach(s => {
        const b = document.getElementById(`sim11_btn_${s}`);
        if (b) {
            b.classList.remove('bg-indigo-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const active = document.getElementById(`sim11_btn_${sym}`);
    if (active) {
        active.classList.remove('bg-slate-800');
        active.classList.add('bg-indigo-600', 'text-white', 'font-bold');
    }

    // Reset opacities
    [bld, gt, tk, gd, bc].forEach(el => { if (el) el.setAttribute('opacity', sym === 'all' ? '1' : '0.25'); });

    if (sym === 'building') {
        if (bld) bld.setAttribute('opacity', '1');
        if (name) name.textContent = 'Main Building Symbol';
        if (desc) desc.textContent = 'Depicted as a bold violet rectangle labeled at the school center.';
        if (stat) stat.textContent = 'Main School Building (Purple)';
    } else if (sym === 'gate') {
        if (gt) gt.setAttribute('opacity', '1');
        if (name) name.textContent = 'Main Entrance Gate';
        if (desc) desc.textContent = 'Gold rectangular opening along the southern boundary wall.';
        if (stat) stat.textContent = 'Entrance Gate (South)';
    } else if (sym === 'tank') {
        if (tk) tk.setAttribute('opacity', '1');
        if (name) name.textContent = 'Overhead Water Tank';
        if (desc) desc.textContent = 'Cyan circular glyph placed in the north-eastern corner for easy fire and water access.';
        if (stat) stat.textContent = 'Water Tank (North-East)';
    } else if (sym === 'garden') {
        if (gd) gd.setAttribute('opacity', '1');
        if (name) name.textContent = 'Botanical Garden & Trees';
        if (desc) desc.textContent = 'Green patch with clustered canopy symbols in the south-western lawn.';
        if (stat) stat.textContent = 'Garden & Trees (South-West)';
    } else if (sym === 'bench') {
        if (bc) bc.setAttribute('opacity', '1');
        if (name) name.textContent = 'Outdoor Seating Benches';
        if (desc) desc.textContent = 'Magenta bar pairs situated along the eastern walkway path.';
        if (stat) stat.textContent = 'Benches along East Path';
    } else if (sym === 'all') {
        if (name) name.textContent = 'Standardized School Map Legend';
        if (desc) desc.textContent = 'All symbols calibrated for instant universal navigation across the campus.';
        if (stat) stat.textContent = 'All Campus Features Active';
    }
}

// SIMULATOR 12: Island Treasure Hunt Navigation
function sim12NextStep() {
    sim12Step++;
    playSound('turn');

    const l1 = document.getElementById('sim12_line1');
    const l2 = document.getElementById('sim12_line2');
    const l3 = document.getElementById('sim12_line3');
    const chest = document.getElementById('sim12_chest');
    const marker = document.getElementById('sim12_marker');
    const btn = document.getElementById('sim12_step_btn');
    const badge = document.getElementById('sim12_badge');
    const title = document.getElementById('sim12_clue_title');
    const desc = document.getElementById('sim12_clue_desc');
    const paces = document.getElementById('sim12_paces');

    if (sim12Step === 1) {
        if (l1) l1.setAttribute('opacity', '1');
        if (marker) { marker.setAttribute('cx', '130'); marker.setAttribute('cy', '130'); }
        if (badge) badge.textContent = 'Step 1 of 3';
        if (btn) btn.textContent = 'Walk Step 2 (North 40 Paces) ➔';
        if (title) title.textContent = 'Clue 2: The Sun Dial';
        if (desc) desc.textContent = 'From the Old Well, turn 90° left to face North. Walk 40 paces straight to the Sun Dial.';
        if (paces) paces.textContent = '30 Paces';
    } else if (sim12Step === 2) {
        if (l2) l2.setAttribute('opacity', '1');
        if (marker) { marker.setAttribute('cx', '130'); marker.setAttribute('cy', '50'); }
        if (badge) badge.textContent = 'Step 2 of 3';
        if (btn) btn.textContent = 'Walk Step 3 (West 20 Paces) ➔';
        if (title) title.textContent = 'Clue 3: The Hollow Oak';
        if (desc) desc.textContent = 'From the Sun Dial, turn 90° left to face West. Walk 20 paces to find the buried chest!';
        if (paces) paces.textContent = '70 Paces';
    } else if (sim12Step === 3) {
        if (l3) l3.setAttribute('opacity', '1');
        if (chest) chest.setAttribute('opacity', '1');
        if (marker) { marker.setAttribute('cx', '70'); marker.setAttribute('cy', '50'); }
        if (badge) badge.textContent = 'Treasure Found! 🏆';
        if (btn) { btn.textContent = 'Treasure Discovered!'; btn.disabled = true; }
        if (title) title.textContent = 'Treasure Uncovered!';
        if (desc) desc.textContent = 'You have reached the buried chest! Total steps: 30 East + 40 North + 20 West = 90 Paces.';
        if (paces) paces.textContent = '90 Paces';
        playSound('correct');
    }
}

function sim12Reset() {
    playSound('click');
    sim12Step = 0;
    const l1 = document.getElementById('sim12_line1');
    const l2 = document.getElementById('sim12_line2');
    const l3 = document.getElementById('sim12_line3');
    const chest = document.getElementById('sim12_chest');
    const marker = document.getElementById('sim12_marker');
    const btn = document.getElementById('sim12_step_btn');
    const badge = document.getElementById('sim12_badge');
    const title = document.getElementById('sim12_clue_title');
    const desc = document.getElementById('sim12_clue_desc');
    const paces = document.getElementById('sim12_paces');

    if (l1) l1.setAttribute('opacity', '0.2');
    if (l2) l2.setAttribute('opacity', '0.2');
    if (l3) l3.setAttribute('opacity', '0.2');
    if (chest) chest.setAttribute('opacity', '0.3');
    if (marker) { marker.setAttribute('cx', '40'); marker.setAttribute('cy', '130'); }
    if (badge) badge.textContent = 'Step 0 of 3';
    if (btn) { btn.textContent = 'Walk Step 1 (East 30 Paces) ➔'; btn.disabled = false; }
    if (title) title.textContent = 'Clue 1: Departure';
    if (desc) desc.textContent = 'Face the rising Sun and walk 30 paces East from the Great Banyan Tree to reach the Old Stone Well.';
    if (paces) paces.textContent = '0 Paces';
}

// SIMULATOR 13: Anthill Grid Crawling Lab
function sim13SelectFood(food) {
    playSound('click');
    const path = document.getElementById('sim13_path');
    const ant = document.getElementById('sim13_ant');
    const title = document.getElementById('sim13_target_title');
    const steps = document.getElementById('sim13_calc_steps');
    const total = document.getElementById('sim13_total_dist');

    ['laddoo', 'bread', 'sugar', 'apple'].forEach(f => {
        const b = document.getElementById(`sim13_btn_${f}`);
        if (b) {
            b.classList.remove('bg-orange-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const active = document.getElementById(`sim13_btn_${food}`);
    if (active) {
        active.classList.remove('bg-slate-800');
        active.classList.add('bg-orange-600', 'text-white', 'font-bold');
    }

    if (food === 'laddoo') {
        // (2, 3) -> svg (60, 80)
        if (path) path.setAttribute('d', 'M 20 140 L 60 140 L 60 80');
        if (ant) { ant.setAttribute('cx', '60'); ant.setAttribute('cy', '80'); }
        if (title) title.textContent = 'Target: Sweet Laddoo (2, 3)';
        if (steps) steps.innerHTML = '<div>• Horizontal East: 2 cm</div><div>• Vertical North: 3 cm</div><div>• Coordinates: (2, 3)</div>';
        if (total) total.textContent = '2 + 3 = 5 cm';
    } else if (food === 'bread') {
        // (5, 4) -> svg (120, 60)
        if (path) path.setAttribute('d', 'M 20 140 L 120 140 L 120 60');
        if (ant) { ant.setAttribute('cx', '120'); ant.setAttribute('cy', '60'); }
        if (title) title.textContent = 'Target: Bread Crumb (5, 4)';
        if (steps) steps.innerHTML = '<div>• Horizontal East: 5 cm</div><div>• Vertical North: 4 cm</div><div>• Coordinates: (5, 4)</div>';
        if (total) total.textContent = '5 + 4 = 9 cm';
    } else if (food === 'sugar') {
        // (6, 5) -> svg (140, 40)
        if (path) path.setAttribute('d', 'M 20 140 L 140 140 L 140 40');
        if (ant) { ant.setAttribute('cx', '140'); ant.setAttribute('cy', '40'); }
        if (title) title.textContent = 'Target: Sugar Cube (6, 5)';
        if (steps) steps.innerHTML = '<div>• Horizontal East: 6 cm</div><div>• Vertical North: 5 cm</div><div>• Coordinates: (6, 5)</div>';
        if (total) total.textContent = '6 + 5 = 11 cm';
    } else if (food === 'apple') {
        // (1, 5) -> svg (40, 40)
        if (path) path.setAttribute('d', 'M 20 140 L 40 140 L 40 40');
        if (ant) { ant.setAttribute('cx', '40'); ant.setAttribute('cy', '40'); }
        if (title) title.textContent = 'Target: Apple Slice (1, 5)';
        if (steps) steps.innerHTML = '<div>• Horizontal East: 1 cm</div><div>• Vertical North: 5 cm</div><div>• Coordinates: (1, 5)</div>';
        if (total) total.textContent = '1 + 5 = 6 cm';
    }
}

// SIMULATOR 14: Shortest Grid Path Comparison
function sim14ShowRoute(rt) {
    playSound('click');
    const ren = document.getElementById('sim14_route_en');
    const rne = document.getElementById('sim14_route_ne');
    const rstair = document.getElementById('sim14_route_stair');
    const rback = document.getElementById('sim14_route_back');
    const name = document.getElementById('sim14_route_name');
    const formula = document.getElementById('sim14_formula');
    const badge = document.getElementById('sim14_len_badge');

    ['en', 'ne', 'stair', 'back'].forEach(k => {
        const b = document.getElementById(`sim14_btn_${k}`);
        if (b) {
            b.classList.remove('bg-teal-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });

    [ren, rne, rstair, rback].forEach(p => { if (p) p.setAttribute('opacity', '0.15'); });

    if (rt === 'EN') {
        const b = document.getElementById('sim14_btn_en');
        if (b) { b.classList.remove('bg-slate-800'); b.classList.add('bg-teal-600', 'text-white', 'font-bold'); }
        if (ren) ren.setAttribute('opacity', '1');
        if (name) name.textContent = 'Route 1: 5 East + 4 North';
        if (formula) formula.textContent = 'Total distance = 5 cm (East) + 4 cm (North) = 9 cm. Minimal shortest path.';
        if (badge) { badge.textContent = '9 cm (Optimal)'; badge.className = 'text-emerald-400 font-bold'; }
    } else if (rt === 'NE') {
        const b = document.getElementById('sim14_btn_ne');
        if (b) { b.classList.remove('bg-slate-800'); b.classList.add('bg-teal-600', 'text-white', 'font-bold'); }
        if (rne) rne.setAttribute('opacity', '1');
        if (name) name.textContent = 'Route 2: 4 North + 5 East';
        if (formula) formula.textContent = 'Total distance = 4 cm (North) + 5 cm (East) = 9 cm. Equal shortest minimal length.';
        if (badge) { badge.textContent = '9 cm (Optimal)'; badge.className = 'text-emerald-400 font-bold'; }
    } else if (rt === 'stair') {
        const b = document.getElementById('sim14_btn_stair');
        if (b) { b.classList.remove('bg-slate-800'); b.classList.add('bg-teal-600', 'text-white', 'font-bold'); }
        if (rstair) rstair.setAttribute('opacity', '1');
        if (name) name.textContent = 'Route 3: Staircase Stepping';
        if (formula) formula.textContent = 'Total distance = 2E + 2N + 2E + 2N + 1E = 9 cm. Still strictly minimal!';
        if (badge) { badge.textContent = '9 cm (Optimal)'; badge.className = 'text-emerald-400 font-bold'; }
    } else if (rt === 'back') {
        const b = document.getElementById('sim14_btn_back');
        if (b) { b.classList.remove('bg-slate-800'); b.classList.add('bg-rose-600', 'text-white', 'font-bold'); }
        if (rback) rback.setAttribute('opacity', '1');
        if (name) name.textContent = 'Route 4: Backtracking Detour';
        if (formula) formula.textContent = 'Total distance = 3E + 3N - 2W + 1N + 4E = 13 cm. Backtracking West wastes 4 cm!';
        if (badge) { badge.textContent = '13 cm (Suboptimal)'; badge.className = 'text-rose-400 font-bold'; }
    }
}

// SIMULATOR 15: 2D Coordinate Grid Studio
function sim15Update() {
    const sx = document.getElementById('sim15_slider_x');
    const sy = document.getElementById('sim15_slider_y');
    if (!sx || !sy) return;

    const x = parseInt(sx.value, 10);
    const y = parseInt(sy.value, 10);

    const xVal = document.getElementById('sim15_x_val');
    const yVal = document.getElementById('sim15_y_val');
    const badge = document.getElementById('sim15_badge');
    const pair = document.getElementById('sim15_pair_display');
    const desc = document.getElementById('sim15_pair_desc');

    if (xVal) xVal.textContent = x;
    if (yVal) yVal.textContent = y;
    if (badge) badge.textContent = `Active: (${x}, ${y})`;
    if (pair) pair.textContent = `(${x}, ${y})`;
    if (desc) desc.textContent = `Walk ${x} units right along the horizontal X-axis, then ${y} units up along the vertical Y-axis.`;

    // SVG projection: origin (20, 140), 10px per unit
    const svgX = 20 + x * 10;
    const svgY = 140 - y * 10;

    const px = document.getElementById('sim15_proj_x');
    const py = document.getElementById('sim15_proj_y');
    const pt = document.getElementById('sim15_pt');

    if (px) {
        px.setAttribute('x1', svgX);
        px.setAttribute('y1', '140');
        px.setAttribute('x2', svgX);
        px.setAttribute('y2', svgY);
    }
    if (py) {
        py.setAttribute('x1', '20');
        py.setAttribute('y1', svgY);
        py.setAttribute('x2', svgX);
        py.setAttribute('y2', svgY);
    }
    if (pt) {
        pt.setAttribute('cx', svgX);
        pt.setAttribute('cy', svgY);
    }
}

// SIMULATOR 16: Zoo Animal Coordinate Plotting Master
const sim16Animals = {
    panda: { name: '🐼 Panda Enclosure', x: 1, y: 1, color: '#f8fafc', desc: 'Located 1 unit East along the horizontal column and 1 unit North along the vertical row.' },
    tortoise: { name: '🐢 Tortoise Enclosure', x: 4, y: 1, color: '#10b981', desc: 'Located 4 units East along the horizontal column and 1 unit North along the vertical row.' },
    deer: { name: '🦌 Deer Meadow', x: 8, y: 3, color: '#f59e0b', desc: 'Located 8 units East along the horizontal column and 3 units North along the vertical row.' },
    croc: { name: '🐊 Crocodile Pond', x: 7, y: 6, color: '#06b6d4', desc: 'Located 7 units East along the horizontal column and 6 units North along the vertical row.' },
    lion: { name: '🦁 Lion Den', x: 3, y: 10, color: '#f43f5e', desc: 'Located 3 units East along the horizontal column and 10 units North along the vertical row.' },
    elephant: { name: '🐘 Elephant Sanctuary', x: 11, y: 11, color: '#6366f1', desc: 'Located 11 units East along the horizontal column and 11 units North along the vertical row.' }
};

function sim16Plot(animal) {
    playSound('click');
    const badge = document.getElementById('sim16_badge');
    const nameEl = document.getElementById('sim16_animal_name');
    const coordEl = document.getElementById('sim16_coord_display');
    const descEl = document.getElementById('sim16_plot_desc');
    const statEl = document.getElementById('sim16_status_text');
    const lx = document.getElementById('sim16_line_x');
    const ly = document.getElementById('sim16_line_y');

    ['panda', 'tortoise', 'deer', 'croc', 'lion', 'elephant', 'all'].forEach(a => {
        const b = document.getElementById(`sim16_btn_${a}`);
        if (b) {
            b.classList.remove('bg-emerald-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-800');
        }
    });
    const active = document.getElementById(`sim16_btn_${animal}`);
    if (active) {
        active.classList.remove('bg-slate-800');
        active.classList.add('bg-emerald-600', 'text-white', 'font-bold');
    }

    if (animal === 'all') {
        if (badge) badge.textContent = 'All 6 Animals Active';
        if (nameEl) nameEl.textContent = 'All Zoo Enclosures';
        if (coordEl) coordEl.textContent = '6 Animals Plotted on (X, Y) Grid';
        if (descEl) descEl.textContent = 'Observe the positions of all enclosures relative to origin (0, 0) at the zoo main gate.';
        if (statEl) statEl.textContent = 'All Animals Shown';
        if (lx) lx.setAttribute('opacity', '0');
        if (ly) ly.setAttribute('opacity', '0');
        return;
    }

    const data = sim16Animals[animal];
    if (!data) return;

    if (badge) badge.textContent = `Coordinates: (${data.x}, ${data.y})`;
    if (nameEl) nameEl.textContent = data.name;
    if (coordEl) coordEl.textContent = `Coordinates: (${data.x}, ${data.y})`;
    if (descEl) descEl.textContent = data.desc;
    if (statEl) statEl.textContent = `Plotted at (${data.x}, ${data.y})`;

    const svgX = 20 + data.x * 10;
    const svgY = 140 - data.y * 10;

    if (lx) {
        lx.setAttribute('opacity', '1');
        lx.setAttribute('x1', svgX);
        lx.setAttribute('y1', '140');
        lx.setAttribute('x2', svgX);
        lx.setAttribute('y2', svgY);
    }
    if (ly) {
        ly.setAttribute('opacity', '1');
        ly.setAttribute('x1', '20');
        ly.setAttribute('y1', svgY);
        ly.setAttribute('x2', svgX);
        ly.setAttribute('y2', svgY);
    }
}

// Window Onload Initialization
window.addEventListener('DOMContentLoaded', () => {
    populateVoiceList();
    renderSlide();
});
"""

with open('.agents/class5_maths_ch14_js.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

with open('.agents/class5_maths_ch14_js.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""JavaScript Engine for Class 5 Maths Chapter 14: Maps and Locations"""\n\n')
    f.write(f"js_code = '''{js_code}'''\n")

print("Successfully written class5_maths_ch14_js.js and class5_maths_ch14_js.py!")


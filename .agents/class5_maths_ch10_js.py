# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 10: Symmetrical Designs
JavaScript Engine: TTS, Slide Navigation, Checkpoints, Modal Solutions & 16 Simulators
"""

js_code = """
// State Variables
let currentSlide = 0;
let synth = window.speechSynthesis;
let currentUtterance = null;
let keepAliveTimer = null;
let userPreferredVoice = null;
let quizScores = { 17: {}, 18: {}, 19: {}, 20: {} };

// Simulators State
let sim1Folded = false;
let sim1CurrentMotif = 'butterfly';
let sim2CurrentLetter = 'A';
let sim2State = 'folded';
let sim4Mode = 'single';
let sim4Folded = false;
let sim5CurrentStep = 1;
let sim5SpinAngle = 0;
let sim5SpinTimer = null;
let sim6CurrentAngle = 0;
let sim7CurrentShape = 'square';
let sim8CurrentLetter = 'S';
let sim8Transformed = false;
let sim10CurrentNum = '808';
let sim10Flipped = false;
let sim12Grid = Array(4).fill(0).map(() => Array(4).fill(0));
let sim13Detached = false;
let sim13Angle = 0;
let sim14Color = '#38bdf8';
let sim14Count = 0;
let sim15Step = 1;
let sim16Type = 'okra';
let sim16Angle = 0;

// TTS Voice Functions
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
    return name.includes('male') || name.includes('david') || name.includes('george') || name.includes('mark') || name.includes('alex') || name.includes('guy') || name.includes('prabhat') || name.includes('ravi');
}

function getBestVoice() {
    if (!synth) return null;
    const voices = synth.getVoices() || [];
    if (userPreferredVoice) {
        const found = voices.find(v => v.name === userPreferredVoice);
        if (found) return found;
    }
    // 1. Indian Male
    const inMale = voices.find(v => isIndianMaleVoice(v));
    if (inMale) return inMale;
    // 2. Any Indian English non-female
    const inAny = voices.find(v => (v.lang || '').toLowerCase().includes('en-in') && !v.name.toLowerCase().includes('female'));
    if (inAny) return inAny;
    // 3. Fallback General Male
    const male = voices.find(v => isMaleVoice(v));
    if (male) return male;
    // 4. Default
    return voices[0] || null;
}

function populateVoiceList() {
    if (!synth) return;
    const voiceSelect = document.getElementById('voiceSelect');
    if (!voiceSelect) return;
    const voices = synth.getVoices() || [];
    voiceSelect.innerHTML = '';

    voices.forEach((v) => {
        const opt = document.createElement('option');
        opt.value = v.name;
        let badge = '';
        if (isIndianMaleVoice(v)) badge = ' 🇮🇳 [Indian Male Teacher]';
        else if (isMaleVoice(v)) badge = ' 👨 [Male Teacher]';
        else badge = ` (${v.lang})`;
        opt.textContent = `${v.name}${badge}`;
        voiceSelect.appendChild(opt);
    });

    const best = getBestVoice();
    if (best) voiceSelect.value = best.name;
}

function onVoiceChange() {
    const voiceSelect = document.getElementById('voiceSelect');
    if (voiceSelect) {
        userPreferredVoice = voiceSelect.value;
        if (synth && synth.speaking) {
            synth.cancel();
            playCurrentLecture();
        }
    }
}

function startKeepAlive() {
    if (keepAliveTimer) clearInterval(keepAliveTimer);
    keepAliveTimer = setInterval(() => {
        if (synth && synth.speaking) {
            synth.pause();
            synth.resume();
        }
    }, 10000);
}

function playCurrentLecture() {
    if (!synth) return;
    synth.cancel();

    const slide = slidesData[currentSlide];
    if (!slide || !slide.lecture) return;

    // Do NOT speak exercises or checkpoints!
    const textToSpeak = slide.lecture;

    currentUtterance = new SpeechSynthesisUtterance(textToSpeak);
    const voice = getBestVoice();
    if (voice) currentUtterance.voice = voice;

    // Acoustic Calibration: pitch = 0.85, rate = 0.94; fail-safe clamp 0.55 if not strictly male
    const isStrictlyMale = voice && (isIndianMaleVoice(voice) || isMaleVoice(voice));
    currentUtterance.pitch = isStrictlyMale ? 0.85 : 0.55;
    currentUtterance.rate = 0.94;

    const btn = document.getElementById('audioBtn');
    if (btn) btn.innerHTML = '<span>🔊</span> Pause Lecture';

    currentUtterance.onend = () => {
        if (btn) btn.innerHTML = '<span>🔊</span> Listen to Lecture';
    };
    currentUtterance.onerror = () => {
        if (btn) btn.innerHTML = '<span>🔊</span> Listen to Lecture';
    };

    synth.speak(currentUtterance);
    startKeepAlive();
}

function toggleAudio() {
    if (!synth) return;
    if (synth.speaking) {
        if (synth.paused) {
            synth.resume();
            const btn = document.getElementById('audioBtn');
            if (btn) btn.innerHTML = '<span>🔊</span> Pause Lecture';
        } else {
            synth.pause();
            const btn = document.getElementById('audioBtn');
            if (btn) btn.innerHTML = '<span>▶️</span> Resume Lecture';
        }
    } else {
        playCurrentLecture();
    }
}

// Slide Navigation
function showSlide(index) {
    if (index < 0 || index >= slidesData.length) return;
    currentSlide = index;

    if (synth && synth.speaking) synth.cancel();
    const btn = document.getElementById('audioBtn');
    if (btn) btn.innerHTML = '<span>🔊</span> Listen to Lecture';

    // Update Progress and Counter
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `Slide ${currentSlide + 1} of ${slidesData.length}`;
    const pbar = document.getElementById('progressBar');
    if (pbar) pbar.style.width = `${((currentSlide + 1) / slidesData.length) * 100}%`;

    // Terminal Slide Invariant (Slide 20)
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) prevBtn.disabled = (currentSlide === 0);

    if (currentSlide === slidesData.length - 1) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) {
            lastNotice.style.display = 'block';
            lastNotice.textContent = 'You have reached the last slide of this chapter.';
        }
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'inline-flex';
            nextBtn.disabled = false;
        }
        if (lastNotice) lastNotice.style.display = 'none';
    }

    // Render Slide Content
    const slide = slidesData[currentSlide];
    const titleEl = document.getElementById('slideTitle');
    const tagEl = document.getElementById('slideTagline');
    const theoryEl = document.getElementById('theoryContainer');
    const simEl = document.getElementById('simulatorContainer');
    const checkEl = document.getElementById('checkpointContainer');

    if (titleEl) titleEl.textContent = slide.title;
    if (tagEl) tagEl.textContent = slide.tagline;
    if (theoryEl) theoryEl.innerHTML = slide.content_html || '';

    // Simulator or Challenge Quiz Deck
    if (currentSlide < 16) {
        if (theoryEl) theoryEl.className = 'lg:col-span-7 space-y-4';
        if (simEl) {
            simEl.style.display = 'block';
            simEl.innerHTML = simulatorsHtml[currentSlide + 1] || '';
            initSimulator(currentSlide + 1);
        }
        if (checkEl) {
            checkEl.style.display = 'block';
            renderCheckpoints(slide.checkpoints || []);
        }
    } else {
        // Quiz Slides (17 to 20)
        if (theoryEl) {
            theoryEl.className = 'lg:col-span-12 space-y-4';
        }
        if (simEl) simEl.style.display = 'none';
        if (checkEl) {
            checkEl.style.display = 'block';
            renderQuizChallenge(slide.id, slide.questions || []);
        }
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < slidesData.length - 1) {
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 0) {
        showSlide(currentSlide - 1);
    }
}

// Formative Checkpoints Renderer (Slides 1 to 16)
function renderCheckpoints(checkpoints) {
    const checkEl = document.getElementById('checkpointContainer');
    if (!checkEl) return;
    if (!checkpoints || checkpoints.length === 0) {
        checkEl.innerHTML = '';
        return;
    }

    let html = `<div class="mt-4 pt-3 border-t border-slate-700/80">
        <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
            <span>📝</span> Formative Knowledge Checkpoints
        </h4>
        <div class="space-y-3">`;

    checkpoints.forEach((cp, idx) => {
        html += `
        <div id="cp_${cp.id}" class="p-3 rounded-xl bg-slate-800/60 border border-slate-700 text-xs">
            <p class="font-semibold text-slate-200 mb-2">${idx + 1}. ${cp.question}</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 mb-2">
                ${cp.options.map((opt, optIdx) => `
                    <button onclick="handleCheckpoint('${cp.id}', ${optIdx}, ${cp.answer})" class="cp-opt-${cp.id} p-2 rounded-lg bg-slate-900/80 hover:bg-slate-700 text-slate-300 border border-slate-700/80 text-left transition-all">
                        <span class="font-bold text-slate-400 mr-1">${String.fromCharCode(65 + optIdx)}.</span> ${opt}
                    </button>
                `).join('')}
            </div>
            <div id="cp_fb_${cp.id}" class="hidden p-2 rounded-lg text-[11px] leading-relaxed"></div>
        </div>`;
    });

    html += `</div></div>`;
    checkEl.innerHTML = html;
}

function handleCheckpoint(cpId, selected, correct) {
    const btns = document.querySelectorAll(`.cp-opt-${cpId}`);
    btns.forEach((b, idx) => {
        b.disabled = true;
        if (idx === correct) {
            b.classList.remove('bg-slate-900/80');
            b.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200', 'font-bold');
        } else if (idx === selected) {
            b.classList.remove('bg-slate-900/80');
            b.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200');
        }
    });

    const fb = document.getElementById(`cp_fb_${cpId}`);
    if (!fb) return;
    fb.classList.remove('hidden');

    const slide = slidesData[currentSlide];
    const cp = (slide.checkpoints || []).find(c => c.id === cpId);
    if (!cp) return;

    if (selected === correct) {
        fb.className = 'mt-2 p-2.5 rounded-lg bg-emerald-950/80 border border-emerald-500/50 text-emerald-200 text-[11px]';
        fb.innerHTML = `<strong>✅ Correct!</strong> ${cp.explanation}`;
    } else {
        fb.className = 'mt-2 p-2.5 rounded-lg bg-amber-950/80 border border-amber-500/50 text-amber-200 text-[11px]';
        fb.innerHTML = `<strong>💡 Hint & Explanation:</strong> ${cp.explanation}`;
    }
}

// Mastery Quiz Challenge Renderer (Slides 17 to 20)
function renderQuizChallenge(slideId, questions) {
    const checkEl = document.getElementById('checkpointContainer');
    if (!checkEl) return;

    let html = `
    <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700">
        <div class="flex items-center justify-between border-b border-slate-700 pb-2 mb-3">
            <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider flex items-center gap-2">
                <span>🏆</span> Mastery Assessment (10 Questions)
            </h4>
            <div id="quizScore_${slideId}" class="px-2.5 py-1 rounded bg-slate-800 text-xs font-mono font-bold text-cyan-300 border border-slate-700">
                Score: 0 / 10
            </div>
        </div>
        <div class="space-y-4">`;

    questions.forEach((q, idx) => {
        html += `
        <div id="card_${q.id}" class="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700 text-xs">
            <div class="flex items-start justify-between gap-2 mb-2">
                <span class="font-bold text-slate-200 text-sm">${idx + 1}. ${q.question}</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                ${q.options.map((opt, oIdx) => `
                    <button onclick="answerQuiz('${slideId}', '${q.id}', ${oIdx}, ${q.answer})" class="q-opt-${q.id} p-2 rounded-lg bg-slate-900 hover:bg-slate-700 text-slate-300 border border-slate-700 text-left transition-all">
                        <span class="font-bold text-slate-400 mr-1">${String.fromCharCode(65 + oIdx)}.</span> ${opt}
                    </button>
                `).join('')}
            </div>
            <div class="flex items-center justify-between pt-1">
                <div id="q_fb_${q.id}" class="hidden text-[11px] font-semibold"></div>
                <button onclick="openSolutionModal('${q.id}')" class="px-2 py-1 rounded bg-indigo-950/60 hover:bg-indigo-900 text-indigo-300 border border-indigo-700/60 text-[11px] font-medium flex items-center gap-1">
                    <span>🔍</span> View Step-by-Step Solution
                </button>
            </div>
        </div>`;
    });

    html += `</div></div>`;
    checkEl.innerHTML = html;
}

function answerQuiz(slideId, qId, selected, correct) {
    const btns = document.querySelectorAll(`.q-opt-${qId}`);
    btns.forEach((b, idx) => {
        b.disabled = true;
        if (idx === correct) {
            b.classList.remove('bg-slate-900');
            b.classList.add('bg-emerald-950', 'border-emerald-500', 'text-emerald-200', 'font-bold');
        } else if (idx === selected) {
            b.classList.remove('bg-slate-900');
            b.classList.add('bg-rose-950', 'border-rose-500', 'text-rose-200');
        }
    });

    const isCorrect = (selected === correct);
    quizScores[slideId] = quizScores[slideId] || {};
    quizScores[slideId][qId] = isCorrect ? 1 : 0;

    const scoreCount = Object.values(quizScores[slideId]).reduce((a, b) => a + b, 0);
    const scoreEl = document.getElementById(`quizScore_${slideId}`);
    if (scoreEl) scoreEl.textContent = `Score: ${scoreCount} / 10`;

    const fb = document.getElementById(`q_fb_${qId}`);
    if (fb) {
        fb.classList.remove('hidden');
        if (isCorrect) {
            fb.className = 'text-[11px] font-bold text-emerald-400';
            fb.textContent = '✅ Correct!';
        } else {
            fb.className = 'text-[11px] font-bold text-rose-400';
            fb.textContent = '❌ Incorrect';
        }
    }
}

// Modal Solution Dialog
function openSolutionModal(qId) {
    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    if (!modal || !body) return;

    let targetQ = null;
    slidesData.forEach(s => {
        if (s.questions) {
            const found = s.questions.find(q => q.id === qId);
            if (found) targetQ = found;
        }
    });

    if (!targetQ) return;

    body.innerHTML = `
    <div class="space-y-3 text-xs">
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
            <span class="text-[10px] text-amber-400 uppercase font-bold tracking-wider block mb-1">Question</span>
            <p class="font-semibold text-slate-200">${targetQ.question}</p>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-700">
            <span class="text-[10px] text-cyan-400 uppercase font-bold tracking-wider block mb-1">Step-by-Step Mathematical Explanation</span>
            ${targetQ.solution_html || `<p class="text-slate-300">${targetQ.explanation}</p>`}
        </div>
    </div>`;

    modal.classList.remove('hidden');
    modal.classList.add('flex');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.remove('flex');
        modal.classList.add('hidden');
    }
}

// ----------------- 16 SIMULATOR ENGINES -----------------

function initSimulator(num) {
    switch (num) {
        case 1: sim1Select('butterfly'); break;
        case 2: sim2Choose('A'); break;
        case 3: sim3Inspect('A'); break;
        case 4: sim4SetMode('single'); break;
        case 5: sim5Step(1); break;
        case 6: sim6RotateTo(0); break;
        case 7: sim7Select('square'); break;
        case 8: sim8Select('S'); break;
        case 9: sim9Inspect('8'); break;
        case 10: sim10Set('808'); break;
        case 11: sim11Update(); break;
        case 12: sim12Reset('checker'); break;
        case 13: sim13Init(); break;
        case 14: sim14SetDye('#38bdf8', 'Indigo Blue'); break;
        case 15: sim15Reset(); break;
        case 16: sim16SetVeg('okra'); break;
    }
}

// Sim 1: Mirror Reflection Studio
function sim1Select(motif) {
    sim1CurrentMotif = motif;
    sim1Folded = false;
    sim1Render();
}

function sim1ToggleFold() {
    sim1Folded = !sim1Folded;
    const btn = document.getElementById('sim1_fold_btn');
    if (btn) btn.textContent = sim1Folded ? '📖 Unfold Paper' : '📖 Fold Paper in Half';
    sim1Render();
}

function sim1Render() {
    const leftEl = document.getElementById('sim1_left_shape');
    const rightEl = document.getElementById('sim1_right_shape');
    const descEl = document.getElementById('sim1_desc');
    if (!leftEl || !rightEl) return;

    let leftPath = '', rightPath = '';
    if (sim1CurrentMotif === 'butterfly') {
        leftPath = '<path d="M100,80 Q60,30 30,50 Q20,90 60,95 Q40,130 70,135 Q90,120 100,85 Z" fill="#38bdf8" opacity="0.85"/>';
        rightPath = '<path d="M100,80 Q140,30 170,50 Q180,90 140,95 Q160,130 130,135 Q110,120 100,85 Z" fill="#38bdf8" opacity="0.85"/>';
        if (descEl) descEl.textContent = 'Left wing reflects across the vertical fold into an identical right wing.';
    } else if (sim1CurrentMotif === 'heart') {
        leftPath = '<path d="M100,135 C50,110 40,65 65,45 C85,30 100,60 100,60 Z" fill="#f43f5e" opacity="0.85"/>';
        rightPath = '<path d="M100,135 C150,110 160,65 135,45 C115,30 100,60 100,60 Z" fill="#f43f5e" opacity="0.85"/>';
        if (descEl) descEl.textContent = 'Left curve of the festive heart reflects perfectly into the right lobe.';
    } else if (sim1CurrentMotif === 'leaf') {
        leftPath = '<path d="M100,140 Q40,90 70,30 Q90,20 100,20 Z" fill="#10b981" opacity="0.85"/>';
        rightPath = '<path d="M100,140 Q160,90 130,30 Q110,20 100,20 Z" fill="#10b981" opacity="0.85"/>';
        if (descEl) descEl.textContent = 'Peepal leaf margins mirror each other along the central midrib vein.';
    } else {
        // Star
        leftPath = '<polygon points="100,25 75,70 100,80 75,90 100,135" fill="#fbbf24"/>';
        rightPath = '<polygon points="100,25 125,70 100,80 125,90 100,135" fill="#fbbf24"/>';
        if (descEl) descEl.textContent = '4-point star vertices mirror across the central vertical axis.';
    }

    leftEl.innerHTML = leftPath;
    if (sim1Folded) {
        rightEl.innerHTML = '';
    } else {
        rightEl.innerHTML = rightPath;
    }
}

// Sim 2: Letter Cutting Simulator
function sim2Choose(letter) {
    sim2CurrentLetter = letter;
    const bA = document.getElementById('sim2_btn_a');
    const bH = document.getElementById('sim2_btn_h');
    const badge = document.getElementById('sim2_badge');
    const tTitle = document.getElementById('sim2_steps_title');
    const tDesc = document.getElementById('sim2_steps_desc');

    if (letter === 'A') {
        if (bA) { bA.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold'; }
        if (bH) { bH.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold'; }
        if (badge) { badge.textContent = '1 Fold (Letter A)'; }
        if (tTitle) tTitle.textContent = 'Letter A (Single Fold):';
        if (tDesc) tDesc.textContent = 'Fold paper once vertically. Cut outer leg angle and inner triangular notch along the fold. Unfold to reveal symmetrical Letter A!';
    } else {
        if (bH) { bH.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold'; }
        if (bA) { bA.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold'; }
        if (badge) { badge.textContent = '2 Folds (Letter H)'; }
        if (tTitle) tTitle.textContent = 'Letter H (Double Fold into Quarters):';
        if (tDesc) tDesc.textContent = 'Fold vertically, then fold horizontally (4 layers). Cut a small corner rectangle notch. Unfolding reveals complete Letter H with 2 symmetry lines!';
    }
    sim2Render(false);
}

function sim2Animate() {
    sim2Render(true);
}

function sim2Render(unfolded) {
    const svg = document.getElementById('sim2_svg');
    if (!svg) return;

    if (sim2CurrentLetter === 'A') {
        if (!unfolded) {
            svg.innerHTML = `
            <rect x="100" y="20" width="70" height="120" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
            <path d="M100,20 L150,140 L130,140 L100,70 Z" fill="#f59e0b" opacity="0.9"/>
            <polygon points="100,70 120,110 100,110" fill="#0f172a"/>
            <text x="95" y="80" text-anchor="end" font-size="9" fill="#f59e0b" font-weight="bold">Fold</text>`;
        } else {
            svg.innerHTML = `
            <rect x="30" y="20" width="140" height="120" fill="#1e293b" stroke="#475569" stroke-width="1"/>
            <line x1="100" y1="15" x2="100" y2="145" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.5"/>
            <!-- Complete Unfolded Letter A -->
            <path d="M100,20 L150,140 L130,140 L115,105 L85,105 L70,140 L50,140 Z" fill="#f59e0b"/>
            <polygon points="100,50 112,90 88,90" fill="#1e293b"/>
            <text x="100" y="155" text-anchor="middle" font-size="9" fill="#34d399" font-weight="bold">Unfolded Letter A (1 Vertical Line)</text>`;
        }
    } else {
        // Letter H
        if (!unfolded) {
            svg.innerHTML = `
            <rect x="100" y="80" width="60" height="60" fill="#334155" stroke="#06b6d4" stroke-width="2"/>
            <rect x="100" y="80" width="25" height="60" fill="#06b6d4" opacity="0.9"/>
            <rect x="100" y="80" width="60" height="20" fill="#06b6d4" opacity="0.9"/>
            <rect x="125" y="100" width="35" height="40" fill="#0f172a"/>
            <text x="95" y="90" text-anchor="end" font-size="8" fill="#06b6d4">Folds</text>`;
        } else {
            svg.innerHTML = `
            <rect x="40" y="20" width="120" height="120" fill="#1e293b" stroke="#475569" stroke-width="1"/>
            <line x1="100" y1="15" x2="100" y2="145" stroke="#06b6d4" stroke-dasharray="3,3" stroke-width="1.5"/>
            <line x1="35" y1="80" x2="165" y2="80" stroke="#06b6d4" stroke-dasharray="3,3" stroke-width="1.5"/>
            <!-- Complete Unfolded Letter H -->
            <path d="M55,30 L80,30 L80,68 L120,68 L120,30 L145,30 L145,130 L120,130 L120,92 L80,92 L80,130 L55,130 Z" fill="#06b6d4"/>
            <text x="100" y="155" text-anchor="middle" font-size="9" fill="#34d399" font-weight="bold">Unfolded Letter H (2 Axes: V + H)</text>`;
        }
    }
}

// Sim 3: Alphabet Symmetry Inspector
const sim3Data = {
    'A': { lines: '1 (Vertical)', type: 'Vertical Only', color: '#f59e0b', path: 'M40,110 L80,30 L120,110 L100,110 L90,90 L70,90 L60,110 Z M75,75 L85,75 L80,55 Z', v: true, h: false, note: 'Vertical axis cuts apex and crossbar cleanly.' },
    'B': { lines: '1 (Horizontal)', type: 'Horizontal Only', color: '#06b6d4', path: 'M50,30 L95,30 Q115,30 115,55 Q115,70 95,70 L95,70 Q120,70 120,95 Q120,110 95,110 L50,110 Z M68,46 L68,60 L90,60 Q98,60 98,53 Q98,46 90,46 Z M68,78 L68,96 L92,96 Q102,96 102,87 Q102,78 92,78 Z', v: false, h: true, note: 'Horizontal line splits top loop and bottom loop.' },
    'C': { lines: '1 (Horizontal)', type: 'Horizontal Only', color: '#06b6d4', path: 'M115,45 Q70,25 55,70 Q45,95 70,110 Q95,115 115,95 L105,85 Q85,100 70,90 Q60,80 70,55 Q80,40 105,55 Z', v: false, h: true, note: 'Horizontal axis mirrors top curve into bottom curve.' },
    'D': { lines: '1 (Horizontal)', type: 'Horizontal Only', color: '#06b6d4', path: 'M50,30 L85,30 Q120,30 120,70 Q120,110 85,110 L50,110 Z M68,48 L68,92 L85,92 Q102,92 102,70 Q102,48 85,48 Z', v: false, h: true, note: 'Horizontal axis cuts across the middle curved arc.' },
    'E': { lines: '1 (Horizontal)', type: 'Horizontal Only', color: '#06b6d4', path: 'M50,30 L115,30 L115,48 L70,48 L70,62 L105,62 L105,78 L70,78 L70,92 L115,92 L115,110 L50,110 Z', v: false, h: true, note: 'Horizontal line runs straight through the middle arm.' },
    'H': { lines: '2 (Vertical & Horizontal)', type: 'Both (V + H)', color: '#10b981', path: 'M50,30 L70,30 L70,62 L110,62 L110,30 L130,30 L130,110 L110,110 L110,78 L70,78 L70,110 L50,110 Z', v: true, h: true, note: 'Has both vertical line between pillars and horizontal line along crossbar.' },
    'I': { lines: '2 (Vertical & Horizontal)', type: 'Both (V + H)', color: '#10b981', path: 'M55,30 L105,30 L105,48 L90,48 L90,92 L105,92 L105,110 L55,110 L55,92 L70,92 L70,48 L55,48 Z', v: true, h: true, note: 'Symmetrical across both axes when drawn with serif caps.' },
    'M': { lines: '1 (Vertical)', type: 'Vertical Only', color: '#f59e0b', path: 'M45,110 L45,30 L80,75 L115,30 L115,110 L98,110 L98,58 L80,82 L62,58 L62,110 Z', v: true, h: false, note: 'Vertical line passes through the central dip V.' },
    'N': { lines: '0 (None)', type: 'No Reflection', color: '#f43f5e', path: 'M50,110 L50,30 L70,30 L105,85 L105,30 L125,30 L125,110 L105,110 L70,55 L70,110 Z', v: false, h: false, note: 'Diagonal stroke slopes in reverse when flipped. 0 mirror lines!' },
    'O': { lines: '2+ (Vertical, Horizontal & Diagonal)', type: 'Both (V + H)', color: '#10b981', path: 'M80,30 Q50,30 50,70 Q50,110 80,110 Q110,110 110,70 Q110,30 80,30 Z M80,48 Q94,48 94,70 Q94,92 80,92 Q66,92 66,70 Q66,48 80,48 Z', v: true, h: true, note: 'Oval has 2 lines of symmetry; perfect circle has infinite.' },
    'S': { lines: '0 (None)', type: 'No Reflection', color: '#f43f5e', path: 'M110,48 Q110,32 80,32 Q55,32 55,52 Q55,65 80,72 Q115,80 115,95 Q115,110 80,110 Q50,110 50,90 L68,88 Q68,95 80,95 Q95,95 95,88 Q95,80 75,75 Q40,65 40,50 Q40,32 80,32 Q125,32 125,48 Z', v: false, h: false, note: 'Flipping turns S backwards. Zero reflection lines (has rotation!).' },
    'T': { lines: '1 (Vertical)', type: 'Vertical Only', color: '#f59e0b', path: 'M45,30 L115,30 L115,48 L90,48 L90,110 L70,110 L70,48 L45,48 Z', v: true, h: false, note: 'Vertical line runs down the stem from the center of the crossbar.' },
    'V': { lines: '1 (Vertical)', type: 'Vertical Only', color: '#f59e0b', path: 'M45,30 L65,30 L80,90 L95,30 L115,30 L90,110 L70,110 Z', v: true, h: false, note: 'Vertical line bisects the lower vertex and spreads evenly.' },
    'X': { lines: '2 (Vertical & Horizontal)', type: 'Both (V + H)', color: '#10b981', path: 'M45,30 L70,70 L45,110 L68,110 L80,90 L92,110 L115,110 L90,70 L115,30 L92,30 L80,50 L68,30 Z', v: true, h: true, note: 'Crossing diagonal arms create vertical, horizontal (and diagonal) lines.' },
    'Y': { lines: '1 (Vertical)', type: 'Vertical Only', color: '#f59e0b', path: 'M45,30 L65,30 L80,65 L95,30 L115,30 L90,72 L90,110 L70,110 L70,72 Z', v: true, h: false, note: 'Vertical line bisects the upper V and stem.' },
    'Z': { lines: '0 (None)', type: 'No Reflection', color: '#f43f5e', path: 'M50,30 L110,30 L110,48 L75,92 L110,92 L110,110 L50,110 L50,92 L85,48 L50,48 Z', v: false, h: false, note: 'Flipping inverts slant direction. Zero reflection lines.' }
};

function sim3Inspect(letter) {
    const data = sim3Data[letter] || sim3Data['A'];
    const svg = document.getElementById('sim3_svg');
    const letEl = document.getElementById('sim3_letter');
    const catEl = document.getElementById('sim3_cat');
    const linesEl = document.getElementById('sim3_lines');
    const noteEl = document.getElementById('sim3_note');

    if (letEl) letEl.textContent = `Letter ${letter}`;
    if (catEl) {
        catEl.textContent = data.type;
        if (data.type.includes('Both')) catEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        else if (data.type.includes('No')) catEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
        else catEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
    }
    if (linesEl) linesEl.textContent = `Lines of Symmetry: ${data.lines}`;
    if (noteEl) noteEl.textContent = data.note;

    if (svg) {
        let vLine = data.v ? '<line x1="80" y1="10" x2="80" y2="130" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>' : '';
        let hLine = data.h ? '<line x1="20" y1="70" x2="140" y2="70" stroke="#06b6d4" stroke-width="2" stroke-dasharray="3,3"/>' : '';
        svg.innerHTML = `
        <path d="${data.path}" fill="${data.color}" opacity="0.85"/>
        ${vLine}
        ${hLine}`;
    }
}

// Sim 4: Festive Diya Cutout Workshop
function sim4SetMode(mode) {
    sim4Mode = mode;
    sim4Folded = false;
    const bS = document.getElementById('sim4_single_btn');
    const bG = document.getElementById('sim4_garland_btn');
    const status = document.getElementById('sim4_status');
    const desc = document.getElementById('sim4_desc');

    if (mode === 'single') {
        if (bS) bS.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold';
        if (bG) bG.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold';
        if (status) status.textContent = 'Single Diya';
        if (desc) desc.textContent = 'The base and flame tip touch the folded edge so the cutout unfolds as one united piece.';
    } else {
        if (bG) bG.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold';
        if (bS) bS.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold';
        if (status) status.textContent = 'Accordion Garland';
        if (desc) desc.textContent = 'Pleat folds allow outer rims to touch adjoining leaves, unfolding into a continuous chain of diyas holding hands!';
    }
    sim4Render();
}

function sim4ToggleFold() {
    sim4Folded = !sim4Folded;
    sim4Render();
}

function sim4Render() {
    const svg = document.getElementById('sim4_svg');
    if (!svg) return;

    if (sim4Mode === 'single') {
        if (sim4Folded) {
            svg.innerHTML = `
            <rect x="100" y="20" width="70" height="100" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
            <!-- Half Diya along fold -->
            <path d="M100,75 C130,75 140,105 100,105 Z" fill="#d97706"/>
            <path d="M100,45 C115,55 115,70 100,75 Z" fill="#fbbf24"/>
            <text x="95" y="65" text-anchor="end" font-size="8" fill="#f59e0b">Fold Spine</text>`;
        } else {
            svg.innerHTML = `
            <line x1="100" y1="15" x2="100" y2="125" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.5"/>
            <!-- Full Diya -->
            <path d="M60,105 C60,75 140,75 140,105 C140,115 60,115 60,105 Z" fill="#d97706"/>
            <!-- Diya Flame -->
            <path d="M100,35 C115,55 115,75 100,75 C85,75 85,55 100,35 Z" fill="#fbbf24"/>
            <text x="100" y="132" text-anchor="middle" font-size="9" fill="#10b981" font-weight="bold">Unfolded Symmetrical Diya</text>`;
        }
    } else {
        // Garland
        if (sim4Folded) {
            svg.innerHTML = `
            <rect x="80" y="30" width="40" height="80" fill="#334155" stroke="#475569"/>
            <text x="100" y="75" text-anchor="middle" font-size="10" fill="#f59e0b">Pleated Layers</text>`;
        } else {
            svg.innerHTML = `
            <g transform="translate(10, 20) scale(0.6)">
                <!-- Diya 1 -->
                <path d="M60,105 C60,75 140,75 140,105 Z" fill="#d97706"/>
                <path d="M100,35 C115,55 115,75 100,75 C85,75 85,55 100,35 Z" fill="#fbbf24"/>
                <!-- Diya 2 -->
                <path d="M140,105 C140,75 220,75 220,105 Z" fill="#d97706"/>
                <path d="M180,35 C195,55 195,75 180,75 C165,75 165,55 180,35 Z" fill="#fbbf24"/>
                <!-- Diya 3 -->
                <path d="M220,105 C220,75 300,75 300,105 Z" fill="#d97706"/>
                <path d="M260,35 C275,55 275,75 260,75 C245,75 245,55 260,35 Z" fill="#fbbf24"/>
            </g>
            <text x="100" y="125" text-anchor="middle" font-size="9" fill="#10b981" font-weight="bold">Continuous Garland of Connected Diyas</text>`;
        }
    }
}

// Sim 5: Paper Firki Construction
function sim5Step(step) {
    sim5CurrentStep = step;
    const badge = document.getElementById('sim5_stage_badge');
    const titleEl = document.getElementById('sim5_instruction_title');
    const descEl = document.getElementById('sim5_instruction_desc');
    const spinCtrl = document.getElementById('sim5_spin_control');

    const btns = document.querySelectorAll('.sim5-step-btn');
    btns.forEach((b, idx) => {
        if (idx + 1 === step) b.className = 'sim5-step-btn px-2 py-1 rounded bg-amber-600 text-white font-bold';
        else b.className = 'sim5-step-btn px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold';
    });

    if (spinCtrl) spinCtrl.className = (step === 4) ? 'block mt-2' : 'hidden';

    if (step === 1) {
        if (badge) badge.textContent = 'Step 1: Crease';
        if (titleEl) titleEl.textContent = 'Step 1: Diagonal Creases';
        if (descEl) descEl.textContent = 'Fold square sheet diagonally both ways to locate central pin intersection.';
    } else if (step === 2) {
        if (badge) badge.textContent = 'Step 2: Slit';
        if (titleEl) titleEl.textContent = 'Step 2: Slit 4 Diagonals';
        if (descEl) descEl.textContent = 'Cut from each corner halfway towards center along diagonal creases.';
    } else if (step === 3) {
        if (badge) badge.textContent = 'Step 3: Bend Tips';
        if (titleEl) titleEl.textContent = 'Step 3: Curve Alternate Tips';
        if (descEl) descEl.textContent = 'Gently bring 4 alternate corner tips to the center hub without creasing.';
    } else {
        if (badge) badge.textContent = 'Step 4: Spin!';
        if (titleEl) titleEl.textContent = 'Step 4: Mount Pin & Spin';
        if (descEl) descEl.textContent = 'Pin blades through central hub to stick. Move wind slider to watch it spin!';
        sim5StartSpin();
    }
    sim5Render();
}

function sim5StartSpin() {
    if (sim5SpinTimer) clearInterval(sim5SpinTimer);
    sim5SpinTimer = setInterval(() => {
        if (sim5CurrentStep === 4) {
            const speed = parseInt(document.getElementById('sim5_speed')?.value || '50');
            sim5SpinAngle = (sim5SpinAngle + (speed * 0.15)) % 360;
            const firkiG = document.getElementById('sim5_spin_group');
            if (firkiG) firkiG.setAttribute('transform', `rotate(${sim5SpinAngle}, 80, 80)`);
        }
    }, 30);
}

function sim5UpdateSpeed() {
    // dynamically handled by interval
}

function sim5Render() {
    const svg = document.getElementById('sim5_svg');
    if (!svg) return;

    if (sim5CurrentStep === 1) {
        svg.innerHTML = `
        <rect x="20" y="20" width="120" height="120" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <line x1="20" y1="20" x2="140" y2="140" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.5"/>
        <line x1="140" y1="20" x2="20" y2="140" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.5"/>
        <circle cx="80" cy="80" r="4" fill="#ef4444"/>`;
    } else if (sim5CurrentStep === 2) {
        svg.innerHTML = `
        <rect x="20" y="20" width="120" height="120" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <!-- Slit lines -->
        <line x1="20" y1="20" x2="55" y2="55" stroke="#ef4444" stroke-width="2.5"/>
        <line x1="140" y1="20" x2="105" y2="55" stroke="#ef4444" stroke-width="2.5"/>
        <line x1="140" y1="140" x2="105" y2="105" stroke="#ef4444" stroke-width="2.5"/>
        <line x1="20" y1="140" x2="55" y2="105" stroke="#ef4444" stroke-width="2.5"/>
        <circle cx="80" cy="80" r="4" fill="#f59e0b"/>
        <text x="80" y="95" text-anchor="middle" font-size="8" fill="#f59e0b">Center Hub</text>`;
    } else if (sim5CurrentStep === 3) {
        svg.innerHTML = `
        <!-- Alternate corners bent -->
        <polygon points="80,80 80,20 50,40" fill="#38bdf8"/>
        <polygon points="80,80 140,80 120,50" fill="#fbbf24"/>
        <polygon points="80,80 80,140 110,120" fill="#34d399"/>
        <polygon points="80,80 20,80 40,110" fill="#a855f7"/>
        <circle cx="80" cy="80" r="5" fill="#f8fafc"/>`;
    } else {
        svg.innerHTML = `
        <rect x="78" y="80" width="4" height="75" fill="#854d0e"/>
        <g id="sim5_spin_group" transform="rotate(${sim5SpinAngle}, 80, 80)">
            <polygon points="80,80 80,20 50,40" fill="#38bdf8"/>
            <polygon points="80,80 140,80 120,50" fill="#fbbf24"/>
            <polygon points="80,80 80,140 110,120" fill="#34d399"/>
            <polygon points="80,80 20,80 40,110" fill="#a855f7"/>
            <circle cx="80" cy="80" r="5" fill="#f8fafc"/>
        </g>`;
    }
}

// Sim 6: 4-Quadrant Turn Tracker
function sim6RotateTo(angle) {
    sim6CurrentAngle = angle;
    const firki = document.getElementById('sim6_firki');
    const badge = document.getElementById('sim6_angle_badge');
    const aText = document.getElementById('sim6_angle_text');
    const dPos = document.getElementById('sim6_dot_pos');

    if (firki) firki.setAttribute('transform', `rotate(${angle}, 80, 80)`);

    const effective = angle % 360;
    if (badge) badge.textContent = `${angle}° (${effective === 0 ? 'Start' : effective === 90 ? '1/4 Turn' : effective === 180 ? '1/2 Turn' : '3/4 Turn'})`;
    if (aText) aText.textContent = `${angle}° (${effective === 0 ? 'Start / Full Turn' : effective + '°'})`;

    if (dPos) {
        if (effective === 0) dPos.textContent = "Top (12 o'clock)";
        else if (effective === 90) dPos.textContent = "Right (3 o'clock)";
        else if (effective === 180) dPos.textContent = "Bottom (6 o'clock)";
        else if (effective === 270) dPos.textContent = "Left (9 o'clock)";
    }
}

// Sim 7: Rotational Symmetry Tester
const sim7Shapes = {
    square: {
        order: 4,
        steps: [0, 90, 180, 270, 360],
        desc: 'Square matches its outline at 90°, 180°, 270°, 360° (Order 4).',
        svg: '<rect x="45" y="45" width="70" height="70" fill="#38bdf8" opacity="0.85"/>',
        ghost: '<rect x="45" y="45" width="70" height="70" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2"/>'
    },
    triangle: {
        order: 3,
        steps: [0, 120, 240, 360],
        desc: 'Equilateral triangle matches at 120°, 240°, 360° (Order 3).',
        svg: '<polygon points="80,35 125,115 35,115" fill="#fbbf24" opacity="0.85"/>',
        ghost: '<polygon points="80,35 125,115 35,115" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2"/>'
    },
    rectangle: {
        order: 2,
        steps: [0, 180, 360],
        desc: 'Rectangle matches at 180° and 360° (Order 2). Stands tall at 90°!',
        svg: '<rect x="30" y="55" width="100" height="50" fill="#34d399" opacity="0.85"/>',
        ghost: '<rect x="30" y="55" width="100" height="50" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2"/>'
    },
    hexagon: {
        order: 6,
        steps: [0, 60, 120, 180, 240, 300, 360],
        desc: 'Regular hexagon matches every 60° (Order 6).',
        svg: '<polygon points="80,35 115,55 115,105 80,125 45,105 45,55" fill="#a855f7" opacity="0.85"/>',
        ghost: '<polygon points="80,35 115,55 115,105 80,125 45,105 45,55" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2"/>'
    },
    scalene: {
        order: 1,
        steps: [0, 360],
        desc: 'Scalene triangle only matches at 360°. Order 1 (No rotational symmetry).',
        svg: '<polygon points="50,40 130,90 40,120" fill="#f43f5e" opacity="0.85"/>',
        ghost: '<polygon points="50,40 130,90 40,120" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2"/>'
    }
};

function sim7Select(shapeKey) {
    sim7CurrentShape = shapeKey;
    const slider = document.getElementById('sim7_slider');
    if (slider) slider.value = 0;
    const badge = document.getElementById('sim7_order_badge');
    if (badge) badge.textContent = `Order ${sim7Shapes[shapeKey].order} (${shapeKey.toUpperCase()})`;
    sim7Rotate();
}

function sim7Rotate() {
    const deg = parseInt(document.getElementById('sim7_slider')?.value || '0');
    const shape = sim7Shapes[sim7CurrentShape];
    const ghostEl = document.getElementById('sim7_ghost');
    const shapeEl = document.getElementById('sim7_shape');
    const degVal = document.getElementById('sim7_deg_val');
    const statusEl = document.getElementById('sim7_match_status');
    const detEl = document.getElementById('sim7_details');

    if (ghostEl) ghostEl.innerHTML = shape.ghost;
    if (shapeEl) {
        shapeEl.innerHTML = shape.svg;
        shapeEl.setAttribute('transform', `rotate(${deg}, 80, 80)`);
    }
    if (degVal) degVal.textContent = `${deg}°`;
    if (detEl) detEl.textContent = shape.desc;

    const isMatch = shape.steps.some(s => Math.abs(s - deg) <= 4);
    if (statusEl) {
        if (isMatch) {
            statusEl.className = 'text-emerald-400 font-bold';
            statusEl.textContent = `✅ Matches Outline! (At ${deg}°)`;
        } else {
            statusEl.className = 'text-amber-400 font-bold';
            statusEl.textContent = `⏳ Out of Alignment (${deg}°)`;
        }
    }
}

// Sim 8: Flip vs Turn Tracing Station
function sim8Select(letter) {
    sim8CurrentLetter = letter;
    sim8Transformed = false;
    const badge = document.getElementById('sim8_badge');
    if (badge) {
        if (letter === 'S' || letter === 'N') badge.textContent = `Letter ${letter} (Rotation Only)`;
        else if (letter === 'H') badge.textContent = `Letter ${letter} (Both Flip & Turn)`;
        else badge.textContent = `Letter ${letter} (Flip Only)`;
    }
    sim8Render('none');
}

function sim8Action(action) {
    sim8Render(action);
}

function sim8Render(action) {
    const svg = document.getElementById('sim8_svg');
    const res = document.getElementById('sim8_result');
    if (!svg) return;

    const letter = sim8CurrentLetter;
    let path = (sim3Data[letter] || sim3Data['A']).path;

    if (action === 'none') {
        svg.innerHTML = `
        <path d="${path}" fill="#64748b" opacity="0.4"/>
        <path d="${path}" fill="#38bdf8"/>`;
        if (res) res.textContent = `Original Letter ${letter} ready. Test Flip vs Turn.`;
    } else if (action === 'flip') {
        // Horizontal flip across vertical mirror line x=80
        svg.innerHTML = `
        <path d="${path}" fill="#64748b" opacity="0.3"/>
        <g transform="translate(160, 0) scale(-1, 1)">
            <path d="${path}" fill="#f59e0b" opacity="0.9"/>
        </g>`;
        if (letter === 'H' || letter === 'A') {
            if (res) res.innerHTML = `<span class="text-emerald-400 font-bold">✅ Reflection Match!</span> Letter ${letter} coincides with its mirror image.`;
        } else {
            if (res) res.innerHTML = `<span class="text-rose-400 font-bold">❌ Flip Mismatch!</span> Letter ${letter} inverts backwards (Fails line symmetry).`;
        }
    } else {
        // 180° Turn around (80, 70)
        svg.innerHTML = `
        <path d="${path}" fill="#64748b" opacity="0.3"/>
        <g transform="rotate(180, 80, 70)">
            <path d="${path}" fill="#10b981" opacity="0.9"/>
        </g>`;
        if (letter === 'H' || letter === 'S' || letter === 'N') {
            if (res) res.innerHTML = `<span class="text-emerald-400 font-bold">✅ 180° Turn Match!</span> Letter ${letter} matches its outline (Rotational Order 2).`;
        } else {
            if (res) res.innerHTML = `<span class="text-rose-400 font-bold">❌ Turn Mismatch!</span> Letter ${letter} stands upside-down (Fails 180° rotation).`;
        }
    }
}

// Sim 9: Digit Symmetry Lab
const sim9Data = {
    '0': { ref: '2 lines (V + H)', rot: 'Invariant (Order 2)', color: '#10b981', note: 'Oval matches when folded both ways and upside down.' },
    '1': { ref: '2 lines (straight bar |)', rot: 'Invariant (Order 2)', color: '#10b981', note: 'Simple straight stroke matches across both axes.' },
    '2': { ref: '0 (None)', rot: 'No (Inverts)', color: '#f43f5e', note: 'Has neither reflection nor rotational symmetry.' },
    '3': { ref: '1 line (Horizontal)', rot: 'No (Loops face left)', color: '#06b6d4', note: 'Horizontal fold matches top arc with bottom arc.' },
    '4': { ref: '0 (None)', rot: 'No', color: '#f43f5e', note: 'Asymmetrical cross-arm.' },
    '5': { ref: '0 (None)', rot: 'No', color: '#f43f5e', note: 'Has neither reflection nor rotational symmetry.' },
    '6': { ref: '0 (None)', rot: 'Transforms into 9!', color: '#a855f7', note: 'Rotating 6 by 180° yields digit 9 (Rotational Pair).' },
    '7': { ref: '0 (None)', rot: 'No', color: '#f43f5e', note: 'Asymmetrical diagonal arm.' },
    '8': { ref: '2 lines (V + H)', rot: 'Invariant (Order 2)', color: '#10b981', note: 'Both reflection axes and 180° rotational invariance.' },
    '9': { ref: '0 (None)', rot: 'Transforms into 6!', color: '#a855f7', note: 'Rotating 9 by 180° yields digit 6 (Rotational Pair).' }
};

function sim9Inspect(digit) {
    const d = sim9Data[digit] || sim9Data['8'];
    const nameEl = document.getElementById('sim9_digit_name');
    const badge = document.getElementById('sim9_badge');
    const refEl = document.getElementById('sim9_ref_text');
    const rotEl = document.getElementById('sim9_rot_text');
    const noteEl = document.getElementById('sim9_note');
    const svg = document.getElementById('sim9_svg');

    if (nameEl) nameEl.textContent = digit;
    if (badge) badge.textContent = `Digit ${digit}`;
    if (refEl) refEl.textContent = `Reflection: ${d.ref}`;
    if (rotEl) rotEl.textContent = `180° Rotation: ${d.rot}`;
    if (noteEl) noteEl.textContent = d.note;

    if (svg) {
        svg.innerHTML = `
        <text x="80" y="90" text-anchor="middle" font-size="70" font-family="monospace" font-weight="bold" fill="${d.color}">${digit}</text>
        <line x1="80" y1="10" x2="80" y2="130" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.5"/>
        <line x1="20" y1="70" x2="140" y2="70" stroke="#06b6d4" stroke-dasharray="3,3" stroke-width="1.5"/>`;
    }
}

// Sim 10: Rotational Number Generator
function sim10Set(num) {
    sim10CurrentNum = num;
    sim10Flipped = false;

    const upEl = document.getElementById('sim10_upright');
    const rotEl = document.getElementById('sim10_rotated');
    const verdEl = document.getElementById('sim10_verdict');
    const anEl = document.getElementById('sim10_analysis');
    const status = document.getElementById('sim10_status');

    if (upEl) upEl.textContent = num;
    if (rotEl) rotEl.textContent = num;

    const invariants = ['88', '69', '181', '808', '1001', '8888', '6996', '96'];
    const isValid = invariants.includes(num);

    if (status) {
        status.textContent = isValid ? 'Invariant!' : 'Fails!';
        status.className = isValid ? 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
    }

    if (verdEl) {
        verdEl.textContent = isValid ? '✅ Rotational Invariant!' : '❌ Not Invariant';
        verdEl.className = isValid ? 'text-emerald-400 font-bold block mb-1' : 'text-rose-400 font-bold block mb-1';
    }

    if (anEl) {
        if (num === '69') anEl.textContent = '6 turns into 9 on right, 9 turns into 6 on left: Recreates 69!';
        else if (isValid) anEl.textContent = `Reading ${num} upside down gives exactly ${num}.`;
        else anEl.textContent = `${num} upside down does not form a valid identical number.`;
    }
}

function sim10FlipCard() {
    sim10Flipped = !sim10Flipped;
    const rotEl = document.getElementById('sim10_rotated');
    if (rotEl) {
        rotEl.style.transform = sim10Flipped ? 'rotate(0deg)' : 'rotate(180deg)';
    }
}

// Sim 11: Symmetrical Design Modifier
function sim11Update() {
    const motif = document.getElementById('sim11_motif')?.value || 'triangle';
    const mode = document.getElementById('sim11_mode')?.value || 'order4';
    const canvas = document.getElementById('sim11_canvas');
    const desc = document.getElementById('sim11_rule_desc');
    const badge = document.getElementById('sim11_symmetry_type');

    if (!canvas) return;

    let baseShape = '';
    if (motif === 'triangle') baseShape = '<polygon points="50,50 65,30 65,50" fill="#38bdf8"/>';
    else if (motif === 'circle') baseShape = '<circle cx="55" cy="45" r="12" fill="#fbbf24"/>';
    else baseShape = '<polygon points="55,35 59,47 71,47 62,54 65,65 55,58 45,65 48,54 39,47 51,47" fill="#f43f5e"/>';

    if (mode === 'order4') {
        if (badge) badge.textContent = '1/4 Turn (Order 4)';
        if (desc) desc.textContent = '4 copies placed at 90° intervals around center.';
        canvas.innerHTML = `
        <g transform="rotate(0, 80, 80)">${baseShape}</g>
        <g transform="rotate(90, 80, 80)">${baseShape}</g>
        <g transform="rotate(180, 80, 80)">${baseShape}</g>
        <g transform="rotate(270, 80, 80)">${baseShape}</g>`;
    } else {
        if (badge) badge.textContent = '1/2 Turn (Order 2)';
        if (desc) desc.textContent = '2 copies placed diametrically opposite (180° turn).';
        canvas.innerHTML = `
        <g transform="rotate(0, 80, 80)">${baseShape}</g>
        <g transform="rotate(180, 80, 80)">${baseShape}</g>`;
    }
}

// Sim 12: 4-Quadrant Grid Coloring Studio
function sim12Reset(type) {
    sim12Grid = Array(4).fill(0).map(() => Array(4).fill(0));
    if (type === 'checker') {
        sim12Toggle(0, 1);
        sim12Toggle(1, 2);
    } else if (type === 'cross') {
        sim12Toggle(1, 1);
        sim12Toggle(1, 2);
    }
    sim12Render();
}

function sim12Clear() {
    sim12Grid = Array(4).fill(0).map(() => Array(4).fill(0));
    sim12Render();
}

function sim12Toggle(r, c) {
    const newVal = sim12Grid[r][c] === 1 ? 0 : 1;
    // Rotate (r, c) 4 times by 90°:
    // (r, c) ➔ (c, 3-r) ➔ (3-r, 3-c) ➔ (3-c, r)
    sim12Grid[r][c] = newVal;
    sim12Grid[c][3 - r] = newVal;
    sim12Grid[3 - r][3 - c] = newVal;
    sim12Grid[3 - c][r] = newVal;
    sim12Render();
}

function sim12Render() {
    const gridEl = document.getElementById('sim12_grid');
    if (!gridEl) return;
    gridEl.innerHTML = '';

    for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
            const btn = document.createElement('button');
            const val = sim12Grid[r][c];
            btn.className = `w-7 h-7 rounded border transition-all ${val === 1 ? 'bg-amber-400 border-amber-300' : 'bg-slate-800 border-slate-700 hover:bg-slate-700'}`;
            btn.onclick = () => sim12Toggle(r, c);
            gridEl.appendChild(btn);
        }
    }
}

let sim12SpinDeg = 0;
function sim12SpinTest() {
    sim12SpinDeg = (sim12SpinDeg + 90) % 360;
    const gridEl = document.getElementById('sim12_grid');
    if (gridEl) {
        gridEl.style.transform = `rotate(${sim12SpinDeg}deg)`;
        gridEl.style.transition = 'transform 0.5s ease';
    }
}

// Sim 13: Composite Polygon Star Builder
function sim13Init() {
    sim13Detached = false;
    sim13Angle = 0;
    sim13Render();
}

function sim13ToggleTriangles() {
    sim13Detached = !sim13Detached;
    const btn = document.getElementById('sim13_toggle_btn');
    if (btn) btn.textContent = sim13Detached ? 'Attach Triangles' : 'Detach Triangles';
    sim13Render();
}

function sim13RotateStar() {
    sim13Angle = (sim13Angle + 90) % 360;
    const g = document.getElementById('sim13_group');
    if (g) g.setAttribute('transform', `rotate(${sim13Angle}, 80, 80)`);
}

function sim13Render() {
    const op = sim13Detached ? '0' : '1';
    ['sim13_t_top', 'sim13_t_right', 'sim13_t_bottom', 'sim13_t_left'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.setAttribute('opacity', op);
    });
}

// Sim 14: Rajasthani Wood Block Printing Press
function sim14SetDye(color, name) {
    sim14Color = color;
    const badge = document.getElementById('sim14_dye_badge');
    if (badge) badge.textContent = name;
}

function sim14Stamp() {
    const fabric = document.getElementById('sim14_fabric');
    if (!fabric) return;
    sim14Count++;

    const div = document.createElement('div');
    div.className = 'w-10 h-10 rounded border border-slate-700 flex items-center justify-center shrink-0 shadow animate-pulse';
    div.innerHTML = `
    <svg viewBox="0 0 40 40" class="w-8 h-8">
        <path d="M20,5 Q32,15 28,30 Q20,38 12,30 Q8,15 20,5 Z" fill="${sim14Color}"/>
        <circle cx="20" cy="22" r="3" fill="#ffffff"/>
    </svg>`;
    fabric.appendChild(div);

    const countEl = document.getElementById('sim14_count');
    if (countEl) countEl.textContent = `Stamped: ${sim14Count} blocks`;
}

function sim14Clear() {
    sim14Count = 0;
    const fabric = document.getElementById('sim14_fabric');
    if (fabric) fabric.innerHTML = '';
    const countEl = document.getElementById('sim14_count');
    if (countEl) countEl.textContent = 'Stamped: 0 blocks';
}

// Sim 15: 4-Step Rotational Block Rosette
function sim15Reset() {
    sim15Step = 1;
    for (let i = 1; i <= 4; i++) {
        const q = document.getElementById(`sim15_q${i}`);
        if (q) q.setAttribute('opacity', '0');
    }
    const badge = document.getElementById('sim15_step_badge');
    const desc = document.getElementById('sim15_desc');
    const msg = document.getElementById('sim15_symmetry_msg');

    if (badge) badge.textContent = 'Step 1 of 4';
    if (desc) desc.textContent = 'Ready to stamp Quadrant 1 (0°).';
    if (msg) msg.textContent = 'Click button to stamp first quarter!';
}

function sim15StampNext() {
    const q = document.getElementById(`sim15_q${sim15Step}`);
    if (q) {
        const rot = (sim15Step - 1) * 90;
        q.setAttribute('transform', `rotate(${rot}, 80, 80)`);
        q.setAttribute('opacity', '1');
        q.innerHTML = '<path d="M80,80 L80,25 Q45,25 45,55 Q45,80 80,80 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>';
    }

    const badge = document.getElementById('sim15_step_badge');
    const desc = document.getElementById('sim15_desc');
    const msg = document.getElementById('sim15_symmetry_msg');

    if (sim15Step === 4) {
        if (badge) badge.textContent = 'Complete! (Order 4)';
        if (desc) desc.textContent = 'All 4 quadrants stamped: 0°, 90°, 180°, 270°.';
        if (msg) msg.textContent = '🎉 Full circular rosette achieved with order 4 rotational symmetry!';
    } else {
        sim15Step++;
        if (badge) badge.textContent = `Step ${sim15Step} of 4`;
        if (desc) desc.textContent = `Quadrant ${sim15Step} stamped at ${(sim15Step - 1) * 90}°.`;
    }
}

// Sim 16: Botanical Vegetable Stamping Studio
function sim16SetVeg(type) {
    sim16Type = type;
    sim16Angle = 0;
    const badge = document.getElementById('sim16_stamp_badge');
    const desc = document.getElementById('sim16_desc');
    const ang = document.getElementById('sim16_angle');

    if (type === 'okra') {
        if (badge) badge.textContent = 'Okra (Order 5)';
        if (desc) desc.textContent = 'Okra cross-section has 5 seed pods forming a 5-pointed star.';
        if (ang) ang.textContent = 'Rotational Angle: 72° (360° ÷ 5)';
    } else if (type === 'onion') {
        if (badge) badge.textContent = 'Onion (Concentric)';
        if (desc) desc.textContent = 'Concentric circular rings radiate outward with continuous reflection symmetry.';
        if (ang) ang.textContent = 'Rotational Angle: Continuous (Infinite order)';
    } else {
        if (badge) badge.textContent = 'Potato (Order 3)';
        if (desc) desc.textContent = 'Carved equilateral triangle stamp matches every 120°.';
        if (ang) ang.textContent = 'Rotational Angle: 120° (360° ÷ 3)';
    }
    sim16Render();
}

function sim16RotateStamp() {
    const step = sim16Type === 'okra' ? 72 : sim16Type === 'onion' ? 45 : 120;
    sim16Angle = (sim16Angle + step) % 360;
    const g = document.getElementById('sim16_group');
    if (g) g.setAttribute('transform', `rotate(${sim16Angle}, 80, 80)`);
}

function sim16Render() {
    const svg = document.getElementById('sim16_svg');
    if (!svg) return;

    if (sim16Type === 'okra') {
        svg.innerHTML = `
        <g id="sim16_group" transform="rotate(${sim16Angle}, 80, 80)" class="transition-transform duration-500">
            <!-- 5-pointed star pentagon -->
            <polygon points="80,25 96,65 137,68 105,95 116,135 80,112 44,135 55,95 23,68 64,65" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <!-- 5 seed dots -->
            <circle cx="80" cy="55" r="4" fill="#fef08a"/>
            <circle cx="102" cy="72" r="4" fill="#fef08a"/>
            <circle cx="94" cy="98" r="4" fill="#fef08a"/>
            <circle cx="66" cy="98" r="4" fill="#fef08a"/>
            <circle cx="58" cy="72" r="4" fill="#fef08a"/>
            <circle cx="80" cy="80" r="6" fill="#047857"/>
        </g>`;
    } else if (sim16Type === 'onion') {
        svg.innerHTML = `
        <g id="sim16_group" transform="rotate(${sim16Angle}, 80, 80)">
            <circle cx="80" cy="80" r="55" fill="none" stroke="#c084fc" stroke-width="4"/>
            <circle cx="80" cy="80" r="42" fill="none" stroke="#a855f7" stroke-width="3"/>
            <circle cx="80" cy="80" r="28" fill="none" stroke="#9333ea" stroke-width="3"/>
            <circle cx="80" cy="80" r="15" fill="none" stroke="#7e22ce" stroke-width="3"/>
            <circle cx="80" cy="80" r="5" fill="#581c87"/>
        </g>`;
    } else {
        svg.innerHTML = `
        <g id="sim16_group" transform="rotate(${sim16Angle}, 80, 80)" class="transition-transform duration-500">
            <polygon points="80,30 130,120 30,120" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
            <circle cx="80" cy="85" r="8" fill="#78350f"/>
        </g>`;
    }
}

// Initializer
document.addEventListener('DOMContentLoaded', () => {
    if (synth) {
        populateVoiceList();
        if (synth.onvoiceschanged !== undefined) {
            synth.onvoiceschanged = populateVoiceList;
        }
    }
    showSlide(0);
});
"""

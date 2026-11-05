# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 9: Coconut Farm
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
let sim4Mode = 'cycle';
let sim7Method = 'susie';
let sim12Step = 0;
const sim12Steps = [
    { title: "Step 1: Divide Tens", desc: "Divide 7 into 43. 7 × 6 = 42. Quotient tens digit is 6.", active: "d", bracket: "<span class='text-amber-400 font-bold'>&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;</span><br>&nbsp;&nbsp;______<br>7 ) 435<br>&nbsp;&nbsp;&nbsp;&nbsp;42<br>&nbsp;&nbsp;------<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1" },
    { title: "Step 2: Multiply & Subtract", desc: "6 × 7 = 42. Subtract 42 from 43 to get remainder 1.", active: "m", bracket: "<span class='text-amber-400 font-bold'>&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;</span><br>&nbsp;&nbsp;______<br>7 ) 435<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class='text-cyan-400 font-bold'>42</span><br>&nbsp;&nbsp;------<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class='text-emerald-400 font-bold'>1</span>" },
    { title: "Step 3: Bring Down Ones", desc: "Bring down the next digit 5 alongside remainder 1 to form 15.", active: "b", bracket: "<span class='text-amber-400 font-bold'>&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;</span><br>&nbsp;&nbsp;______<br>7 ) 43<span class='text-amber-300 font-bold'>5</span><br>&nbsp;&nbsp;&nbsp;&nbsp;42<br>&nbsp;&nbsp;------<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<span class='text-amber-300 font-bold'>5</span>" },
    { title: "Step 4: Divide Again", desc: "Divide 7 into 15. 7 × 2 = 14. Quotient ones digit is 2. Final remainder is 1.", active: "s", bracket: "<span class='text-amber-400 font-bold'>&nbsp;&nbsp;&nbsp;&nbsp;62</span><br>&nbsp;&nbsp;______<br>7 ) 435<br>&nbsp;&nbsp;&nbsp;&nbsp;42<br>&nbsp;&nbsp;------<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;14<br>&nbsp;&nbsp;------<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class='text-rose-400 font-bold'>1</span> (Rem)" }
];

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

    // Terminal Slide Invariant
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
        case 1: sim1Update(); break;
        case 2: sim2Set(9, 8); break;
        case 3: sim3Set(4200, 70); break;
        case 4: sim4SetMode('cycle'); break;
        case 5: sim5Set(1248, 6, 'add', 1200, 48); break;
        case 6: sim6Update(); break;
        case 7: sim7SetMethod('susie'); break;
        case 8: sim8Update(); break;
        case 9: sim9Update(); break;
        case 10: sim10Update(); break;
        case 11: sim11Set(9913, 23); break;
        case 12: sim12Reset(); break;
        case 13: sim13Set(3005, 5); break;
        case 14: sim14Update(); break;
        case 15: break;
        case 16: break;
    }
}

// Simulator 1: Coconut Grid
function sim1Update() {
    const rows = parseInt(document.getElementById('sim1_rows_input')?.value || '6');
    const cols = parseInt(document.getElementById('sim1_cols_input')?.value || '8');
    const total = rows * cols;

    const rVal = document.getElementById('sim1_rows_val');
    const cVal = document.getElementById('sim1_cols_val');
    const nEl = document.getElementById('sim1_n');
    const mEl = document.getElementById('sim1_mult');
    const d1El = document.getElementById('sim1_div1');
    const d2El = document.getElementById('sim1_div2');
    const gridEl = document.getElementById('sim1_grid');

    if (rVal) rVal.textContent = rows;
    if (cVal) cVal.textContent = cols;
    if (nEl) nEl.textContent = total;
    if (mEl) mEl.textContent = `${rows} × ${cols} = ${total}`;
    if (d1El) d1El.textContent = `${total} ÷ ${rows} = ${cols}`;
    if (d2El) d2El.textContent = `${total} ÷ ${cols} = ${rows}`;

    if (gridEl) {
        gridEl.style.gridTemplateColumns = `repeat(${cols}, minmax(0, 1fr))`;
        let html = '';
        for (let i = 0; i < total; i++) {
            html += `<span class="flex items-center justify-center text-sm p-0.5 bg-slate-800 rounded border border-slate-700">🥥</span>`;
        }
        gridEl.innerHTML = html;
    }
}

// Simulator 2: Fact Triangle
function sim2Set(a, b) {
    const prod = a * b;
    const pEl = document.getElementById('sim2_peak');
    const lEl = document.getElementById('sim2_left');
    const rEl = document.getElementById('sim2_right');
    const spProd = document.getElementById('sim2_stat_prod');
    const spDiv1 = document.getElementById('sim2_stat_div1');
    const spDiv2 = document.getElementById('sim2_stat_div2');

    if (pEl) pEl.textContent = prod;
    if (lEl) lEl.textContent = a;
    if (rEl) rEl.textContent = b;
    if (spProd) spProd.textContent = `${a} × ${b} = ${prod}`;
    if (spDiv1) spDiv1.textContent = `${prod} ÷ ${a} = ${b}`;
    if (spDiv2) spDiv2.textContent = `${prod} ÷ ${b} = ${a}`;
}

// Simulator 3: Trailing Zero Striking
let sim3CurrentNum = 4200;
let sim3CurrentDen = 70;

function sim3Set(num, den) {
    sim3CurrentNum = num;
    sim3CurrentDen = den;
    const ans = Math.floor(num / den);

    const nEl = document.getElementById('sim3_num');
    const dEl = document.getElementById('sim3_den');
    const aEl = document.getElementById('sim3_ans');
    const exp = document.getElementById('sim3_explanation');

    if (nEl) nEl.innerHTML = num.toLocaleString();
    if (dEl) dEl.innerHTML = den.toLocaleString();
    if (aEl) aEl.textContent = ans;

    let zeroesDen = 0;
    let tempD = den;
    while (tempD % 10 === 0 && tempD > 0) {
        zeroesDen++;
        tempD /= 10;
    }

    if (exp) {
        exp.textContent = `Divisor has ${zeroesDen} trailing zero(s). Strike ${zeroesDen} zero(s) from both numbers to calculate mental quotient!`;
    }
}

function sim3Animate() {
    let nStr = sim3CurrentNum.toString();
    let dStr = sim3CurrentDen.toString();

    let zeros = 0;
    while (nStr.endsWith('0') && dStr.endsWith('0')) {
        zeros++;
        nStr = nStr.slice(0, -1);
        dStr = dStr.slice(0, -1);
    }

    const nEl = document.getElementById('sim3_num');
    const dEl = document.getElementById('sim3_den');
    const exp = document.getElementById('sim3_explanation');

    if (zeros > 0) {
        const nKept = sim3CurrentNum.toString().slice(0, -zeros);
        const dKept = sim3CurrentDen.toString().slice(0, -zeros);
        const zerosStruck = '0'.repeat(zeros);

        if (nEl) nEl.innerHTML = `${nKept}<span class="line-through text-rose-500 font-bold opacity-75">${zerosStruck}</span>`;
        if (dEl) dEl.innerHTML = `${dKept}<span class="line-through text-rose-500 font-bold opacity-75">${zerosStruck}</span>`;
        if (exp) exp.textContent = `Struck ${zeros} matching zero(s): Simplified to ${nKept} ÷ ${dKept} = ${Math.floor(sim3CurrentNum / sim3CurrentDen)}!`;
    }
}

// Simulator 4: Rate & Bonus
function sim4SetMode(mode) {
    sim4Mode = mode;
    const bC = document.getElementById('sim4_mode_cycle');
    const bB = document.getElementById('sim4_mode_bonus');
    const cDiv = document.getElementById('sim4_controls');

    if (mode === 'cycle') {
        if (bC) { bC.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold'; }
        if (bB) { bB.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold'; }
        if (cDiv) {
            cDiv.innerHTML = `
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Total Distance:</span>
                        <span id="sim4_dist_val" class="text-amber-400 font-mono font-bold">400 km</span>
                    </label>
                    <input id="sim4_dist_in" type="range" min="100" max="1000" value="400" step="50" oninput="sim4CalcCycle()" class="w-full accent-amber-400">
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Tour Days:</span>
                        <span id="sim4_days_val" class="text-cyan-400 font-mono font-bold">5 days</span>
                    </label>
                    <input id="sim4_days_in" type="range" min="2" max="10" value="5" step="1" oninput="sim4CalcCycle()" class="w-full accent-cyan-400">
                </div>
            </div>`;
        }
        sim4CalcCycle();
    } else {
        if (bB) { bB.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold'; }
        if (bC) { bC.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold'; }
        if (cDiv) {
            cDiv.innerHTML = `
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Bonus Pool:</span>
                        <span id="sim4_pool_val" class="text-amber-400 font-mono font-bold">₹3,600</span>
                    </label>
                    <input id="sim4_pool_in" type="range" min="1000" max="12000" value="3600" step="200" oninput="sim4CalcBonus()" class="w-full accent-amber-400">
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Workers:</span>
                        <span id="sim4_work_val" class="text-cyan-400 font-mono font-bold">6 workers</span>
                    </label>
                    <input id="sim4_work_in" type="range" min="2" max="12" value="6" step="1" oninput="sim4CalcBonus()" class="w-full accent-cyan-400">
                </div>
            </div>`;
        }
        sim4CalcBonus();
    }
}

function sim4CalcCycle() {
    const dist = parseInt(document.getElementById('sim4_dist_in')?.value || '400');
    const days = parseInt(document.getElementById('sim4_days_in')?.value || '5');
    const rate = Math.floor(dist / days);
    const rem = dist % days;

    const dVal = document.getElementById('sim4_dist_val');
    const dayVal = document.getElementById('sim4_days_val');
    const fEl = document.getElementById('sim4_formula');
    const cEl = document.getElementById('sim4_calculation');
    const dtEl = document.getElementById('sim4_detail');

    if (dVal) dVal.textContent = `${dist} km`;
    if (dayVal) dayVal.textContent = `${days} days`;
    if (fEl) fEl.textContent = 'Daily Rate = Total Distance ÷ Number of Days';
    if (cEl) cEl.textContent = `${dist} km ÷ ${days} days = ${rate} km/day ${rem > 0 ? '(+ ' + rem + ' km extra)' : ''}`;
    if (dtEl) dtEl.textContent = `The rally cyclists pedal an equal distance of ${rate} km each day.`;
}

function sim4CalcBonus() {
    const pool = parseInt(document.getElementById('sim4_pool_in')?.value || '3600');
    const workers = parseInt(document.getElementById('sim4_work_in')?.value || '6');
    const perWorker = Math.floor(pool / workers);
    const rem = pool % workers;

    const pVal = document.getElementById('sim4_pool_val');
    const wVal = document.getElementById('sim4_work_val');
    const fEl = document.getElementById('sim4_formula');
    const cEl = document.getElementById('sim4_calculation');
    const dtEl = document.getElementById('sim4_detail');

    if (pVal) pVal.textContent = `₹${pool.toLocaleString()}`;
    if (wVal) wVal.textContent = `${workers} workers`;
    if (fEl) fEl.textContent = 'Bonus per Worker = Total Pool ÷ Number of Workers';
    if (cEl) cEl.textContent = `₹${pool.toLocaleString()} ÷ ${workers} = ₹${perWorker.toLocaleString()} each`;
    if (dtEl) dtEl.textContent = `Each coconut farm worker receives exactly ₹${perWorker.toLocaleString()} bonus.`;
}

// Simulator 5: Convenient Splitting
function sim5Set(orig, div, type, p1, p2) {
    const oEl = document.getElementById('sim5_orig');
    const sEl = document.getElementById('sim5_split');
    const rEl = document.getElementById('sim5_result');
    const stEl = document.getElementById('sim5_steps');

    const q1 = Math.floor(p1 / div);
    const q2 = Math.floor(p2 / div);

    if (oEl) oEl.textContent = `${orig.toLocaleString()} ÷ ${div}`;

    if (type === 'add') {
        const sumQ = q1 + q2;
        if (sEl) sEl.textContent = `(${p1.toLocaleString()} + ${p2.toLocaleString()}) ÷ ${div}`;
        if (rEl) rEl.textContent = `${q1} + ${q2} = ${sumQ}`;
        if (stEl) {
            stEl.innerHTML = `
            <div>Step 1: ${p1.toLocaleString()} ÷ ${div} = ${q1}</div>
            <div>Step 2: ${p2.toLocaleString()} ÷ ${div} = ${q2}</div>
            <div class="text-emerald-400 font-bold">Sum of Quotients: ${q1} + ${q2} = ${sumQ}</div>`;
        }
    } else {
        const diffQ = q1 - q2;
        if (sEl) sEl.textContent = `(${p1.toLocaleString()} - ${p2.toLocaleString()}) ÷ ${div}`;
        if (rEl) rEl.textContent = `${q1} - ${q2} = ${diffQ}`;
        if (stEl) {
            stEl.innerHTML = `
            <div>Step 1: ${p1.toLocaleString()} ÷ ${div} = ${q1}</div>
            <div>Step 2: ${p2.toLocaleString()} ÷ ${div} = ${q2}</div>
            <div class="text-emerald-400 font-bold">Difference of Quotients: ${q1} - ${q2} = ${diffQ}</div>`;
        }
    }
}

// Simulator 6: Repeated Halving
function sim6Update() {
    const div = parseInt(document.getElementById('sim6_divisor')?.value || '4');
    const num = parseInt(document.getElementById('sim6_number')?.value || '256');

    const stDiv = document.getElementById('sim6_stages');
    const sumEl = document.getElementById('sim6_summary');

    const h1 = num / 2;
    const h2 = h1 / 2;

    if (div === 4) {
        if (stDiv) {
            stDiv.innerHTML = `
            <div class="p-2 rounded bg-slate-800 text-center"><span class="text-[10px] text-slate-400">Start</span><div class="text-cyan-300 font-bold">${num}</div></div>
            <span class="text-amber-400 font-bold">➔ ÷2 ➔</span>
            <div class="p-2 rounded bg-slate-800 text-center"><span class="text-[10px] text-slate-400">Half 1</span><div class="text-amber-300 font-bold">${h1}</div></div>
            <span class="text-amber-400 font-bold">➔ ÷2 ➔</span>
            <div class="p-2 rounded bg-emerald-950/60 border border-emerald-800/50 text-center"><span class="text-[10px] text-emerald-400">Final (÷4)</span><div class="text-emerald-300 font-bold text-sm">${h2}</div></div>`;
        }
        if (sumEl) sumEl.textContent = `${num} ÷ 4 = ${h2} (Halved twice: ${num} ➔ ${h1} ➔ ${h2})`;
    } else {
        const h3 = h2 / 2;
        if (stDiv) {
            stDiv.innerHTML = `
            <div class="p-1.5 rounded bg-slate-800 text-center"><span class="text-[9px] text-slate-400">Start</span><div class="text-cyan-300 font-bold">${num}</div></div>
            <span class="text-amber-400">➔</span>
            <div class="p-1.5 rounded bg-slate-800 text-center"><span class="text-[9px] text-slate-400">Half 1</span><div class="text-amber-300 font-bold">${h1}</div></div>
            <span class="text-amber-400">➔</span>
            <div class="p-1.5 rounded bg-slate-800 text-center"><span class="text-[9px] text-slate-400">Half 2</span><div class="text-amber-300 font-bold">${h2}</div></div>
            <span class="text-amber-400">➔</span>
            <div class="p-1.5 rounded bg-emerald-950/60 border border-emerald-800/50 text-center"><span class="text-[9px] text-emerald-400">Final (÷8)</span><div class="text-emerald-300 font-bold text-sm">${h3}</div></div>`;
        }
        if (sumEl) sumEl.textContent = `${num} ÷ 8 = ${h3} (Halved thrice: ${num} ➔ ${h1} ➔ ${h2} ➔ ${h3})`;
    }
}

// Simulator 7: Partial Quotients
function sim7SetMethod(method) {
    sim7Method = method;
    const bSusie = document.getElementById('sim7_tab_susie');
    const bSunitha = document.getElementById('sim7_tab_sunitha');
    const tbody = document.getElementById('sim7_table_body');

    if (method === 'susie') {
        if (bSusie) bSusie.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold';
        if (bSunitha) bSunitha.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold';
        if (tbody) {
            tbody.innerHTML = `
            <tr><td class="p-1.5">1</td><td class="p-1.5 text-cyan-300 font-bold">+ 20</td><td class="p-1.5">6 × 20 = 120</td><td class="p-1.5">582 - 120 = 462</td></tr>
            <tr><td class="p-1.5">2</td><td class="p-1.5 text-cyan-300 font-bold">+ 20</td><td class="p-1.5">6 × 20 = 120</td><td class="p-1.5">462 - 120 = 342</td></tr>
            <tr><td class="p-1.5">3</td><td class="p-1.5 text-cyan-300 font-bold">+ 50</td><td class="p-1.5">6 × 50 = 300</td><td class="p-1.5">342 - 300 = 42</td></tr>
            <tr><td class="p-1.5">4</td><td class="p-1.5 text-cyan-300 font-bold">+ 7</td><td class="p-1.5">6 × 7 = 42</td><td class="p-1.5">42 - 42 = 0</td></tr>`;
        }
    } else {
        if (bSunitha) bSunitha.className = 'px-3 py-1 rounded bg-amber-600 text-white font-bold';
        if (bSusie) bSusie.className = 'px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold';
        if (tbody) {
            tbody.innerHTML = `
            <tr><td class="p-1.5">1</td><td class="p-1.5 text-emerald-400 font-bold">+ 90 (Giant Leap!)</td><td class="p-1.5">6 × 90 = 540</td><td class="p-1.5">582 - 540 = 42</td></tr>
            <tr><td class="p-1.5">2</td><td class="p-1.5 text-emerald-400 font-bold">+ 7</td><td class="p-1.5">6 × 7 = 42</td><td class="p-1.5">42 - 42 = 0</td></tr>`;
        }
    }
}

// Simulator 8: Division Algorithm
function sim8Update() {
    const n = parseInt(document.getElementById('sim8_n_input')?.value || '47');
    const d = parseInt(document.getElementById('sim8_d_input')?.value || '6');

    const q = Math.floor(n / d);
    const r = n % d;

    const nVal = document.getElementById('sim8_n_val');
    const dVal = document.getElementById('sim8_d_val');
    const qEl = document.getElementById('sim8_q');
    const rEl = document.getElementById('sim8_r');
    const cEl = document.getElementById('sim8_cond');
    const eqEl = document.getElementById('sim8_eqn');
    const vBadge = document.getElementById('sim8_validity');

    if (nVal) nVal.textContent = n;
    if (dVal) dVal.textContent = d;
    if (qEl) qEl.textContent = q;
    if (rEl) rEl.textContent = r;

    if (r < d) {
        if (cEl) cEl.textContent = `${r} < ${d} (Pass)`;
        if (vBadge) {
            vBadge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            vBadge.textContent = 'R < D Verified';
        }
    } else {
        if (cEl) cEl.textContent = `${r} ≥ ${d} (Violated!)`;
        if (vBadge) {
            vBadge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
            vBadge.textContent = 'Invalid Remainder';
        }
    }

    if (eqEl) eqEl.textContent = `${n} = ${d} × ${q} + ${r}`;
}

// Simulator 9: Fleet Allocator
function sim9Update() {
    const students = parseInt(document.getElementById('sim9_students_input')?.value || '248');
    const cap = parseInt(document.getElementById('sim9_capacity_input')?.value || '50');

    const full = Math.floor(students / cap);
    const rem = students % cap;
    const totalBuses = Math.ceil(students / cap);

    const sVal = document.getElementById('sim9_students_val');
    const cVal = document.getElementById('sim9_capacity_val');
    const fEl = document.getElementById('sim9_full');
    const rEl = document.getElementById('sim9_rem');
    const tbEl = document.getElementById('sim9_total_buses');
    const exp = document.getElementById('sim9_explanation');

    if (sVal) sVal.textContent = students;
    if (cVal) cVal.textContent = cap;
    if (fEl) fEl.textContent = full;
    if (rEl) rEl.textContent = rem;
    if (tbEl) tbEl.textContent = totalBuses;

    if (exp) {
        if (rem === 0) {
            exp.textContent = `${students} ÷ ${cap} = exactly ${full} buses needed (0 leftover children).`;
        } else {
            exp.textContent = `${students} ÷ ${cap} = ${full} full buses with ${rem} leftover kids. An extra 1 bus is required, making ${totalBuses} buses total!`;
        }
    }
}

// Simulator 10: Coconut Oil Extraction
function sim10Update() {
    const nuts = parseInt(document.getElementById('sim10_nuts_input')?.value || '4376');
    const price = parseInt(document.getElementById('sim10_price_input')?.value || '240');

    const litres = Math.floor(nuts / 8);
    const revenue = litres * price;

    const nVal = document.getElementById('sim10_nuts_val');
    const pVal = document.getElementById('sim10_price_val');
    const lEl = document.getElementById('sim10_litres');
    const revEl = document.getElementById('sim10_revenue');
    const bd = document.getElementById('sim10_breakdown');

    if (nVal) nVal.textContent = nuts.toLocaleString();
    if (pVal) pVal.textContent = `₹${price}`;
    if (lEl) lEl.textContent = `${litres.toLocaleString()} L`;
    if (revEl) revEl.textContent = `₹${revenue.toLocaleString()}`;
    if (bd) bd.textContent = `${nuts.toLocaleString()} nuts ÷ 8 = ${litres.toLocaleString()} Litres. ${litres.toLocaleString()} L × ₹${price} = ₹${revenue.toLocaleString()} revenue!`;
}

// Simulator 11: Two-Digit Divisors
function sim11Set(num, den) {
    const exEl = document.getElementById('sim11_exact');
    const estEl = document.getElementById('sim11_est');
    const stepsEl = document.getElementById('sim11_steps');

    const roundedDen = Math.round(den / 10) * 10;
    const roundedNum = Math.round(num / 1000) * 1000;
    const estQuotient = Math.round(roundedNum / roundedDen);

    const quot = Math.floor(num / den);
    const rem = num % den;

    if (exEl) exEl.textContent = `${num.toLocaleString()} ÷ ${den}`;
    if (estEl) estEl.textContent = `Round ${den} to ${roundedDen}: Estimate ≈ ${estQuotient}`;

    if (stepsEl) {
        stepsEl.innerHTML = `
        <div>1. Trial divisor rounded to nearest 10: ${den} ➔ ${roundedDen}</div>
        <div>2. Long division calculation: ${num.toLocaleString()} ÷ ${den}</div>
        <div class="text-emerald-400 font-bold">Exact Quotient: ${quot.toLocaleString()} with Remainder ${rem}</div>
        <div class="text-slate-400 text-[10px]">Verification: (${den} × ${quot.toLocaleString()}) + ${rem} = ${num.toLocaleString()}</div>`;
    }
}

// Simulator 12: 4-Step Long Division
function sim12Next() {
    if (sim12Step < sim12Steps.length - 1) {
        sim12Step++;
        sim12Render();
    }
}

function sim12Prev() {
    if (sim12Step > 0) {
        sim12Step--;
        sim12Render();
    }
}

function sim12Reset() {
    sim12Step = 0;
    sim12Render();
}

function sim12Render() {
    const s = sim12Steps[sim12Step];
    const bEl = document.getElementById('sim12_bracket');
    const tEl = document.getElementById('sim12_action_title');
    const dEl = document.getElementById('sim12_action_desc');
    const badge = document.getElementById('sim12_step_badge');

    if (bEl) bEl.innerHTML = s.bracket;
    if (tEl) tEl.textContent = s.title;
    if (dEl) dEl.textContent = s.desc;
    if (badge) badge.textContent = `Step ${sim12Step + 1} of 4`;

    const bD = document.getElementById('sim12_badge_d');
    const bM = document.getElementById('sim12_badge_m');
    const bS = document.getElementById('sim12_badge_s');
    const bB = document.getElementById('sim12_badge_b');

    const allBadges = [bD, bM, bS, bB];
    const keys = ['d', 'm', 's', 'b'];

    allBadges.forEach((b, idx) => {
        if (!b) return;
        if (keys[idx] === s.active) {
            b.className = 'p-1 px-2 rounded bg-indigo-600 text-white font-bold shadow';
        } else {
            b.className = 'p-1 px-2 rounded bg-slate-800 text-slate-400';
        }
    });
}

// Simulator 13: Zero Quotient Trap Detective
function sim13Set(n, d) {
    const wrongQuot = Math.floor(n / d).toString().replace(/0/g, '') || '0';
    const rightQuot = Math.floor(n / d);

    const wEl = document.getElementById('sim13_wrong');
    const rEl = document.getElementById('sim13_right');

    if (wEl) {
        wEl.innerHTML = `
        Skipping 0 gives incorrect quotient: <span class="text-rose-400 font-bold">${wrongQuot}</span>.<br>
        Check: ${wrongQuot} × ${d} = ${parseInt(wrongQuot) * d} (Off by ${(n - parseInt(wrongQuot) * d).toLocaleString()}!)`;
    }

    if (rEl) {
        rEl.innerHTML = `
        Correct place-value quotient: <span class="text-emerald-400 font-bold">${rightQuot}</span>.<br>
        Check: ${rightQuot} × ${d} = ${rightQuot * d} (Exact match!)`;
    }
}

// Simulator 14: Workshop Bottleneck
function sim14Update() {
    const panels = parseInt(document.getElementById('sim14_panels')?.value || '120');
    const clips = parseInt(document.getElementById('sim14_clips')?.value || '200');
    const screws = parseInt(document.getElementById('sim14_screws')?.value || '480');

    const capP = Math.floor(panels / 4);
    const capC = Math.floor(clips / 8);
    const capS = Math.floor(screws / 16);

    const cpEl = document.getElementById('sim14_cap_panels');
    const ccEl = document.getElementById('sim14_cap_clips');
    const csEl = document.getElementById('sim14_cap_screws');
    const sumEl = document.getElementById('sim14_summary');
    const bnBadge = document.getElementById('sim14_bottleneck');

    if (cpEl) cpEl.textContent = `${capP} Crates`;
    if (ccEl) ccEl.textContent = `${capC} Crates`;
    if (csEl) csEl.textContent = `${capS} Crates`;

    const minCap = Math.min(capP, capC, capS);
    let limiting = '';
    if (minCap === capP) limiting = 'Panels';
    else if (minCap === capC) limiting = 'Clips';
    else limiting = 'Screws';

    if (bnBadge) bnBadge.textContent = `Bottleneck: ${limiting}`;
    if (sumEl) sumEl.textContent = `Maximum finished crates possible = ${minCap} crates (limited by ${limiting}).`;
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

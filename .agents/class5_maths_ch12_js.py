# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 12: Racing Seconds
JavaScript Engine: Indian Male Teacher Voice Priority, Slide Navigation,
Checkpoints, Quiz Modal Solutions & 16 Bespoke Simulators
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
let sim5Timer = null;
let sim6CurrentSec = 0;
let sim8TimerInterval = null;
let sim8TimeLeft = 60;
let sim8CurrentFeat = 'pushups';

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
        const cpKey = cp.id || (`cp_${currentSlide + 1}_${idx}`);
        html += `
        <div id="cp_${cpKey}" class="p-3 rounded-xl bg-slate-800/60 border border-slate-700 text-xs">
            <p class="font-semibold text-slate-200 mb-2">${idx + 1}. ${cp.question}</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 mb-2">
                ${cp.options.map((opt, optIdx) => `
                    <button onclick="handleCheckpoint('${cpKey}', ${optIdx}, ${cp.answer})" class="cp-opt-${cpKey} p-2 rounded-lg bg-slate-900/80 hover:bg-slate-700 text-slate-300 border border-slate-700/80 text-left transition-all">
                        <span class="font-bold text-slate-400 mr-1">${String.fromCharCode(65 + optIdx)}.</span> ${opt}
                    </button>
                `).join('')}
            </div>
            <div id="cp_fb_${cpKey}" class="hidden p-2 rounded-lg text-[11px] leading-relaxed"></div>
        </div>`;
    });

    html += `</div></div>`;
    checkEl.innerHTML = html;
}

function handleCheckpoint(cpKey, selected, correct) {
    const btns = document.querySelectorAll(`.cp-opt-${cpKey}`);
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

    const fb = document.getElementById(`cp_fb_${cpKey}`);
    if (!fb) return;
    fb.classList.remove('hidden');

    const slide = slidesData[currentSlide];
    const cp = (slide.checkpoints || []).find((c, idx) => (c.id === cpKey || `cp_${currentSlide + 1}_${idx}` === cpKey));
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

function openSolutionModal(qId) {
    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    if (!modal || !body) return;

    let targetQ = null;
    slidesData.forEach(s => {
        if (s.questions) {
            const found = s.questions.find(q => q.id == qId);
            if (found) targetQ = found;
        }
    });

    if (!targetQ) return;

    body.innerHTML = `
        <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700 mb-3">
            <div class="font-bold text-slate-200 text-xs mb-1.5">Question:</div>
            <div class="text-slate-300 text-xs">${targetQ.question}</div>
        </div>
        <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 mb-3">
            <div class="font-bold text-emerald-400 text-xs mb-1">Correct Answer:</div>
            <div class="text-emerald-200 font-bold text-xs">
                ${String.fromCharCode(65 + targetQ.answer)}. ${targetQ.options[targetQ.answer]}
            </div>
        </div>
        <div class="p-3 rounded-xl bg-slate-800/60 border border-slate-700 text-xs space-y-2">
            <div class="font-bold text-amber-400 mb-1">Step-by-Step Mathematical Explanation:</div>
            ${targetQ.solution_html || `<p class="text-slate-300">${targetQ.explanation}</p>`}
        </div>
    `;

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

// -------------------------------------------------------------
// Simulator Initializations & Handlers (Simulators 1 to 16)
// -------------------------------------------------------------
function initSimulator(simId) {
    switch (simId) {
        case 1: sim1Update(); break;
        case 2: sim2Select(1); break;
        case 3: sim3Highlight('all'); break;
        case 4: sim4Update(); break;
        case 5: sim5ResetRace(); break;
        case 6: sim6InitHashes(); break;
        case 7: sim7Test('blink'); break;
        case 8: sim8SelectFeat('pushups'); break;
        case 9: sim9Select('skip'); break;
        case 10: sim10Select('kitchen'); break;
        case 11: sim11Set(30); break;
        case 12: sim12Update(); break;
        case 13: sim13Update(); break;
        case 14: sim14Preset(320); break;
        case 15: sim15Select('picnic'); break;
        case 16: sim16Highlight('lunch'); break;
    }
}

// SIM 1: Yoga Elapsed Time Calculator
function sim1Update() {
    const startEl = document.getElementById('sim1_start');
    const endEl = document.getElementById('sim1_end');
    if (!startEl || !endEl) return;

    const startM = parseInt(startEl.value, 10);
    const endM = parseInt(endEl.value, 10);

    const startVal = document.getElementById('sim1_start_val');
    const endVal = document.getElementById('sim1_end_val');
    if (startVal) startVal.textContent = `06:${startM < 10 ? '0' + startM : startM} a.m.`;
    if (endVal) endVal.textContent = `07:${endM < 10 ? '0' + endM : endM} a.m.`;

    const step1M = 60 - startM;
    const totalM = step1M + endM;

    const step1El = document.getElementById('sim1_step1');
    const step2El = document.getElementById('sim1_step2');
    const resTotEl = document.getElementById('sim1_res_tot');
    if (step1El) step1El.textContent = `Step 1: 06:${startM < 10 ? '0' + startM : startM} ➔ 07:00 = ${step1M} min`;
    if (step2El) step2El.textContent = `Step 2: 07:00 ➔ 07:${endM < 10 ? '0' + endM : endM} = ${endM} min`;
    if (resTotEl) resTotEl.textContent = `${totalM} minutes`;

    // Rotate clock minute hand to finish time
    const minHand = document.getElementById('sim1_min_hand');
    const hourHand = document.getElementById('sim1_hour_hand');
    if (minHand && hourHand) {
        const minAngle = endM * 6; // 6 deg per min
        const minRad = (minAngle - 90) * Math.PI / 180;
        minHand.setAttribute('x2', 100 + 40 * Math.cos(minRad));
        minHand.setAttribute('y2', 80 + 40 * Math.sin(minRad));

        const hourAngle = (7 * 30) + (endM * 0.5);
        const hourRad = (hourAngle - 90) * Math.PI / 180;
        hourHand.setAttribute('x2', 100 + 28 * Math.cos(hourRad));
        hourHand.setAttribute('y2', 80 + 28 * Math.sin(hourRad));
    }
}

// SIM 2: Interval Duration Studio
function sim2Select(presetId) {
    [1, 2, 3].forEach(id => {
        const btn = document.getElementById(`sim2_btn_${id}`);
        if (btn) {
            btn.className = (id === presetId) ?
                'px-2 py-1 rounded bg-cyan-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const lblStart = document.getElementById('sim2_lbl_start');
    const lblEnd = document.getElementById('sim2_lbl_end');
    const jumpTxt = document.getElementById('sim2_jump_txt');
    const typeEl = document.getElementById('sim2_type');
    const mathEl = document.getElementById('sim2_math');
    const resEl = document.getElementById('sim2_res');

    if (presetId === 1) {
        if (lblStart) lblStart.textContent = '01:15 p.m.';
        if (lblEnd) lblEnd.textContent = '01:42 p.m.';
        if (jumpTxt) jumpTxt.textContent = '+27 min';
        if (typeEl) typeEl.textContent = 'Category: Same Hour Gap';
        if (mathEl) mathEl.textContent = 'Subtract minutes: 42 − 15 = 27 min';
        if (resEl) resEl.textContent = '27 minutes';
    } else if (presetId === 2) {
        if (lblStart) lblStart.textContent = '03:18 p.m.';
        if (lblEnd) lblEnd.textContent = '08:18 p.m.';
        if (jumpTxt) jumpTxt.textContent = '+5 Hours';
        if (typeEl) typeEl.textContent = 'Category: Same Minute Gap';
        if (mathEl) mathEl.textContent = 'Subtract hours: 8 − 3 = 5 hours';
        if (resEl) resEl.textContent = '5 hours';
    } else if (presetId === 3) {
        if (lblStart) lblStart.textContent = '09:15 a.m.';
        if (lblEnd) lblEnd.textContent = '11:30 a.m.';
        if (jumpTxt) jumpTxt.textContent = '+2h 15m';
        if (typeEl) typeEl.textContent = 'Category: Mixed Interval (Hours & Minutes)';
        if (mathEl) mathEl.textContent = '09:15 ➔ 11:15 (2 hr) + 15 min = 2 hr 15 min';
        if (resEl) resEl.textContent = '2 hours 15 minutes';
    }
}

// SIM 3: Painting Duration Ranker
function sim3Highlight(painter) {
    ['all', 'student3', 'student1', 'student2', 'student4'].forEach(p => {
        const btn = document.getElementById(`sim3_btn_${p}`);
        if (btn) {
            btn.className = (painter === p) ?
                'px-2 py-1 rounded bg-indigo-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const descEl = document.getElementById('sim3_desc');
    const diffEl = document.getElementById('sim3_diff');

    if (painter === 'student3') {
        if (descEl) descEl.textContent = '★ Student 3 (Rank 1): 1 hr 30 min = 90 min (Longest!)';
        if (diffEl) diffEl.textContent = '90 − 40 = 50 min longer than Student 4';
    } else if (painter === 'student1') {
        if (descEl) descEl.textContent = 'Student 1 (Rank 2): 1 hr 15 min = 75 min';
        if (diffEl) diffEl.textContent = '75 − 50 = 25 min longer than Student 2';
    } else if (painter === 'student2') {
        if (descEl) descEl.textContent = 'Student 2 (Rank 3): 50 min';
        if (diffEl) diffEl.textContent = '50 − 40 = 10 min longer than Student 4';
    } else if (painter === 'student4') {
        if (descEl) descEl.textContent = '⚡ Student 4 (Rank 4): 40 min (Least Time Taken!)';
        if (diffEl) diffEl.textContent = 'Fastest artist to finish artwork!';
    } else {
        if (descEl) descEl.textContent = 'Longest: Student 3 (90 min) • Shortest: Student 4 (40 min)';
        if (diffEl) diffEl.textContent = 'Spread: 90 − 40 = 50 minutes';
    }
}

// SIM 4: 12-Hour vs 24-Hour Railway Clock
function sim4Update() {
    const hrEl = document.getElementById('sim4_hr');
    if (!hrEl) return;
    const h24 = parseInt(hrEl.value, 10);
    const m = 30;

    const hrVal = document.getElementById('sim4_hr_val');
    const disp24 = document.getElementById('sim4_disp_24');
    const disp12 = document.getElementById('sim4_disp_12');
    const ruleEl = document.getElementById('sim4_rule');
    const statusEl = document.getElementById('sim4_status');

    const str24 = `${h24 < 10 ? '0' + h24 : h24}:${m}`;
    if (hrVal) hrVal.textContent = `${str24} Hours`;
    if (disp24) disp24.textContent = str24;

    let h12 = h24 % 12;
    if (h12 === 0) h12 = 12;
    const period = h24 >= 12 ? 'p.m.' : 'a.m.';
    const str12 = `${h12 < 10 ? '0' + h12 : h12}:${m} ${period}`;
    if (disp12) disp12.textContent = str12;

    if (h24 >= 12) {
        if (ruleEl) ruleEl.textContent = `P.M. time: ${h12} + 12 = ${h24}:${m} hours`;
        if (statusEl) {
            statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
            statusEl.textContent = 'Afternoon / Evening';
        }
    } else {
        if (ruleEl) ruleEl.textContent = `A.M. morning time: hours remain identical (${h24}:${m})`;
        if (statusEl) {
            statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
            statusEl.textContent = 'Morning';
        }
    }
}

// SIM 5: 200m School Race Stopwatch
function sim5StartRace() {
    sim5ResetRace();
    const r1 = document.getElementById('sim5_racer1');
    const r2 = document.getElementById('sim5_racer2');
    const r3 = document.getElementById('sim5_racer3');
    const statusEl = document.getElementById('sim5_status');
    const btn = document.getElementById('sim5_race_btn');
    if (btn) btn.disabled = true;

    if (statusEl) {
        statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        statusEl.textContent = 'Race in Progress!';
    }

    let t = 0;
    sim5Timer = setInterval(() => {
        t += 0.05;
        // Runner A finishes in 2.14s simulation scale
        const p1 = Math.min(160, 30 + (t / 2.14) * 130);
        const p2 = Math.min(160, 30 + (t / 2.18) * 130);
        const p3 = Math.min(160, 30 + (t / 2.22) * 130);

        if (r1) r1.setAttribute('cx', p1);
        if (r2) r2.setAttribute('cx', p2);
        if (r3) r3.setAttribute('cx', p3);

        if (t >= 2.25) {
            clearInterval(sim5Timer);
            if (btn) btn.disabled = false;
            if (statusEl) statusEl.textContent = 'Runner A Wins by 4 Seconds!';
        }
    }, 50);
}

function sim5ResetRace() {
    if (sim5Timer) clearInterval(sim5Timer);
    const r1 = document.getElementById('sim5_racer1');
    const r2 = document.getElementById('sim5_racer2');
    const r3 = document.getElementById('sim5_racer3');
    const statusEl = document.getElementById('sim5_status');
    const btn = document.getElementById('sim5_race_btn');
    if (btn) btn.disabled = false;

    if (r1) r1.setAttribute('cx', 30);
    if (r2) r2.setAttribute('cx', 30);
    if (r3) r3.setAttribute('cx', 30);
    if (statusEl) statusEl.textContent = 'Ready at Starting Line';
}

// SIM 6: Seconds Precision & Sweep Studio
function sim6InitHashes() {
    const hashes = document.getElementById('sim6_hashes');
    if (!hashes) return;
    let h = '';
    for (let i = 0; i < 60; i++) {
        const a = (i * 6 - 90) * Math.PI / 180;
        const r1 = (i % 5 === 0) ? 52 : 55;
        const r2 = 58;
        const x1 = 100 + r1 * Math.cos(a);
        const y1 = 80 + r1 * Math.sin(a);
        const x2 = 100 + r2 * Math.cos(a);
        const y2 = 80 + r2 * Math.sin(a);
        h += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${i%5===0 ? '#94a3b8' : '#475569'}" stroke-width="${i%5===0 ? 1.5 : 0.75}"/>`;
    }
    hashes.innerHTML = h;
}

function sim6Sweep(sec) {
    sim6CurrentSec = sec;
    const secVal = document.getElementById('sim6_sec_val');
    const degVal = document.getElementById('sim6_deg_val');
    const descEl = document.getElementById('sim6_desc');
    const secHand = document.getElementById('sim6_sec_hand');
    const minHand = document.getElementById('sim6_min_hand');

    const angle = sec * 6; // 6 deg per second
    if (secVal) secVal.textContent = `${sec} sec`;
    if (degVal) degVal.textContent = `${angle}°`;

    if (secHand) {
        const rad = (angle - 90) * Math.PI / 180;
        secHand.setAttribute('x2', 100 + 50 * Math.cos(rad));
        secHand.setAttribute('y2', 80 + 50 * Math.sin(rad));
    }

    if (sec === 60) {
        if (minHand) {
            // Click minute hand forward by 6 deg
            const minRad = (6 - 90) * Math.PI / 180;
            minHand.setAttribute('x2', 100 + 40 * Math.cos(minRad));
            minHand.setAttribute('y2', 80 + 40 * Math.sin(minRad));
        }
        if (descEl) descEl.textContent = '🎉 Full 60s Circuit complete! Minute hand stepped forward by exactly 1 tick!';
    } else {
        if (descEl) descEl.textContent = `${sec} seconds represents ${angle}° of angular rotation on the circular clock.`;
    }
}

// SIM 7: Time Unit Estimation Classifier
function sim7Test(act) {
    ['blink', 'switch', 'teeth', 'count', 'lunch'].forEach(a => {
        const btn = document.getElementById(`sim7_btn_${a}`);
        if (btn) {
            btn.className = (act === a) ?
                'px-2 py-1 rounded bg-teal-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const icon = document.getElementById('sim7_icon');
    const title = document.getElementById('sim7_title');
    const badge = document.getElementById('sim7_badge');
    const reason = document.getElementById('sim7_reason');

    if (act === 'blink') {
        if (icon) icon.textContent = '👀';
        if (title) title.textContent = 'Blinking Eyelids';
        if (badge) {
            badge.className = 'inline-block px-2 py-0.5 rounded text-xs font-bold font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
            badge.textContent = 'Takes Seconds (~0.3 sec)';
        }
        if (reason) reason.textContent = 'Instant involuntary muscle reflex completed in a fraction of a second.';
    } else if (act === 'switch') {
        if (icon) icon.textContent = '💡';
        if (title) title.textContent = 'Flipping Light Switch';
        if (badge) {
            badge.className = 'inline-block px-2 py-0.5 rounded text-xs font-bold font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
            badge.textContent = 'Takes Seconds (~1 sec)';
        }
        if (reason) reason.textContent = 'Quick mechanical finger press happens in 1 single second.';
    } else if (act === 'teeth') {
        if (icon) icon.textContent = '🪥';
        if (title) title.textContent = 'Brushing Teeth Thoroughly';
        if (badge) {
            badge.className = 'inline-block px-2 py-0.5 rounded text-xs font-bold font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30';
            badge.textContent = 'Takes Minutes (2 to 3 min)';
        }
        if (reason) reason.textContent = 'Dental hygiene requires circular brushing over 120 to 180 seconds.';
    } else if (act === 'count') {
        if (icon) icon.textContent = '🔢';
        if (title) title.textContent = 'Counting Out Loud (1 to 20)';
        if (badge) {
            badge.className = 'inline-block px-2 py-0.5 rounded text-xs font-bold font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
            badge.textContent = 'Takes Seconds (~15 sec)';
        }
        if (reason) reason.textContent = 'Speaking 20 steady numbers takes roughly 15 seconds.';
    } else if (act === 'lunch') {
        if (icon) icon.textContent = '🍲';
        if (title) title.textContent = 'Eating Afternoon Lunch';
        if (badge) {
            badge.className = 'inline-block px-2 py-0.5 rounded text-xs font-bold font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30';
            badge.textContent = 'Takes Minutes (20 to 30 min)';
        }
        if (reason) reason.textContent = 'Chewing and enjoying a full meal spans 20 to 30 minutes.';
    }
}

// SIM 8: One-Minute Challenge Simulator
function sim8SelectFeat(feat) {
    sim8CurrentFeat = feat;
    ['pushups', 'balloons', 'breaths', 'hops'].forEach(f => {
        const btn = document.getElementById(`sim8_btn_${f}`);
        if (btn) {
            btn.className = (feat === f) ?
                'px-2 py-1 rounded bg-rose-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const est = document.getElementById('sim8_est');
    const act = document.getElementById('sim8_act');
    const obs = document.getElementById('sim8_obs');

    if (feat === 'pushups') {
        if (est) est.textContent = '30 push-ups';
        if (act) act.textContent = '15 to 22 reps';
        if (obs) obs.textContent = 'Muscular fatigue slows repetition pace over 60 seconds.';
    } else if (feat === 'balloons') {
        if (est) est.textContent = '5 balloons';
        if (act) act.textContent = '2 to 3 balloons';
        if (obs) obs.textContent = 'Tying balloon knots requires delicate fine motor time.';
    } else if (feat === 'breaths') {
        if (est) est.textContent = '30 breaths';
        if (act) act.textContent = '16 to 20 breaths';
        if (obs) obs.textContent = 'Healthy resting breathing rhythm maintains this steady rate.';
    } else if (feat === 'hops') {
        if (est) est.textContent = '50 hops';
        if (act) act.textContent = '60 to 85 hops';
        if (obs) obs.textContent = 'Fast spring rhythm exceeds pre-activity estimate!';
    }
}

function sim8StartTimer() {
    sim8ResetTimer();
    const btn = document.getElementById('sim8_timer_btn');
    if (btn) btn.disabled = true;

    sim8TimerInterval = setInterval(() => {
        sim8TimeLeft--;
        const timer = document.getElementById('sim8_timer');
        if (timer) timer.textContent = `${sim8TimeLeft}s`;

        if (sim8TimeLeft <= 0) {
            clearInterval(sim8TimerInterval);
            if (btn) btn.disabled = false;
            if (timer) timer.textContent = 'Done! 60s';
        }
    }, 1000);
}

function sim8ResetTimer() {
    if (sim8TimerInterval) clearInterval(sim8TimerInterval);
    sim8TimeLeft = 60;
    const timer = document.getElementById('sim8_timer');
    const btn = document.getElementById('sim8_timer_btn');
    if (timer) timer.textContent = '60s';
    if (btn) btn.disabled = false;
}

// SIM 9: Micro-Interval Stopwatch
function sim9Select(task) {
    ['skip', 'word', 'sprint'].forEach(t => {
        const btn = document.getElementById(`sim9_btn_${t}`);
        if (btn) {
            btn.className = (task === t) ?
                'px-2 py-1 rounded bg-blue-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const disp = document.getElementById('sim9_disp');
    const frac = document.getElementById('sim9_frac');
    const title = document.getElementById('sim9_title');
    const perf = document.getElementById('sim9_perf');

    if (task === 'skip') {
        if (disp) disp.textContent = '10.0s';
        if (frac) frac.textContent = '1/6th of a Minute';
        if (title) title.textContent = '10-Second Rope Skipping';
        if (perf) perf.textContent = 'Achieved: 18 rapid rope skips!';
    } else if (task === 'word') {
        if (disp) disp.textContent = '5.4s';
        if (frac) frac.textContent = '1/11th of a Minute';
        if (title) title.textContent = 'Writing "FRIEND"';
        if (perf) perf.textContent = 'Neat cursive 6-letter handwriting complete.';
    } else if (task === 'sprint') {
        if (disp) disp.textContent = '18.2s';
        if (frac) frac.textContent = 'Almost 1/3rd of a Minute';
        if (title) title.textContent = '100m Athletics Track Sprint';
        if (perf) perf.textContent = 'Crossed finish line at top speed!';
    }
}

// SIM 10: Analog Seconds Hand Reader
function sim10Select(task) {
    ['kitchen', 'paper', 'dish'].forEach(t => {
        const btn = document.getElementById(`sim10_btn_${t}`);
        if (btn) {
            btn.className = (task === t) ?
                'px-2 py-1 rounded bg-purple-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const handA = document.getElementById('sim10_hand_a');
    const handB = document.getElementById('sim10_hand_b');
    const gapEl = document.getElementById('sim10_gap');
    const resEl = document.getElementById('sim10_res');

    if (task === 'kitchen') {
        // 12 to 4
        if (handA) { handA.setAttribute('x2', 50); handA.setAttribute('y2', 15); }
        if (handB) { handB.setAttribute('x2', 80); handB.setAttribute('y2', 68); }
        if (gapEl) gapEl.textContent = 'Hand moved: 12 ➔ 4 (4 gaps)';
        if (resEl) resEl.textContent = '4 × 5 = 20 seconds';
    } else if (task === 'paper') {
        // 2 to 5
        if (handA) { handA.setAttribute('x2', 75); handA.setAttribute('y2', 35); }
        if (handB) { handB.setAttribute('x2', 68); handB.setAttribute('y2', 80); }
        if (gapEl) gapEl.textContent = 'Hand moved: 2 (10s) ➔ 5 (25s)';
        if (resEl) resEl.textContent = '25 − 10 = 15 seconds';
    } else if (task === 'dish') {
        // 12 to 7
        if (handA) { handA.setAttribute('x2', 50); handA.setAttribute('y2', 15); }
        if (handB) { handB.setAttribute('x2', 32); handB.setAttribute('y2', 80); }
        if (gapEl) gapEl.textContent = 'Hand moved: 12 (0s) ➔ 7 (35s)';
        if (resEl) resEl.textContent = '7 × 5 = 35 seconds';
    }
}

// SIM 11: Seconds Hand Drawing Studio
function sim11Set(sec) {
    [20, 30, 40, 60].forEach(s => {
        const btn = document.getElementById(`sim11_btn_${s}`);
        if (btn) {
            btn.className = (sec === s) ?
                'px-2 py-1 rounded bg-emerald-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const hand = document.getElementById('sim11_hand');
    const calc = document.getElementById('sim11_calc');
    const orient = document.getElementById('sim11_orient');

    const numeral = sec === 60 ? 12 : (sec / 5);
    const angle = (numeral * 30 - 90) * Math.PI / 180;

    if (hand) {
        hand.setAttribute('x2', 100 + 50 * Math.cos(angle));
        hand.setAttribute('y2', 80 + 50 * Math.sin(angle));
    }

    if (calc) calc.textContent = `Target Numeral = ${sec} ÷ 5 = ${numeral}`;
    if (orient) {
        if (sec === 20) orient.textContent = 'Points at numeral 4';
        else if (sec === 30) orient.textContent = 'Points straight down at 6 (Half Turn)';
        else if (sec === 40) orient.textContent = 'Points at numeral 8';
        else if (sec === 60) orient.textContent = 'Full 360° circuit back to numeral 12!';
    }
}

// SIM 12: Hours To Minutes Multiplier
function sim12Update() {
    const hrEl = document.getElementById('sim12_hr');
    const minEl = document.getElementById('sim12_min');
    if (!hrEl || !minEl) return;

    const h = parseInt(hrEl.value, 10);
    const m = parseInt(minEl.value, 10);

    const hrVal = document.getElementById('sim12_hr_val');
    const minVal = document.getElementById('sim12_min_val');
    if (hrVal) hrVal.textContent = `${h} hr`;
    if (minVal) minVal.textContent = `${m} min`;

    const total = (h * 60) + m;
    const resTot = document.getElementById('sim12_res_tot');
    const sub = document.getElementById('sim12_sub');
    const inv = document.getElementById('sim12_inv');

    if (resTot) resTot.textContent = `${total} min`;
    if (sub) sub.textContent = `${h} × 60 + ${m} = ${total} min`;
    if (inv) inv.textContent = `${total} ÷ 60 = ${h} hr remainder ${m} min`;
}

// SIM 13: Double Number Line (Hours & Minutes)
function sim13Update() {
    const cursor = document.getElementById('sim13_cursor');
    if (!cursor) return;
    const totalMin = parseInt(cursor.value, 10);

    const curVal = document.getElementById('sim13_cur_val');
    const h = Math.floor(totalMin / 60);
    const m = totalMin % 60;
    if (curVal) curVal.textContent = `${h} hr ${m} min (${totalMin} min)`;

    const resTop = document.getElementById('sim13_res_top');
    const resBot = document.getElementById('sim13_res_bot');
    if (resTop) resTop.textContent = `Top Scale: ${h} hr ${m} min`;
    if (resBot) resBot.textContent = `Bottom Scale: ${totalMin} minutes`;

    // Move SVG cursor
    const line = document.getElementById('sim13_cursor_line');
    const ptTop = document.getElementById('sim13_pt_top');
    const ptBot = document.getElementById('sim13_pt_bot');
    const xPos = 20 + (totalMin / 300) * 160;

    if (line) { line.setAttribute('x1', xPos); line.setAttribute('x2', xPos); }
    if (ptTop) ptTop.setAttribute('cx', xPos);
    if (ptBot) ptBot.setAttribute('cx', xPos);
}

// SIM 14: Double Number Line (Minutes & Seconds)
function sim14Preset(sec) {
    [320, 150, 250].forEach(s => {
        const btn = document.getElementById(`sim14_btn_${s}`);
        if (btn) {
            btn.className = (sec === s) ?
                'px-2.5 py-1 rounded bg-cyan-600 text-white font-semibold' :
                'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const dispSec = document.getElementById('sim14_disp_sec');
    const dispMin = document.getElementById('sim14_disp_min');
    const mathEl = document.getElementById('sim14_math');

    const m = Math.floor(sec / 60);
    const s = sec % 60;

    if (dispSec) dispSec.textContent = `${sec} Seconds`;
    if (dispMin) dispMin.textContent = `${m} min ${s} sec`;
    if (mathEl) mathEl.textContent = `${sec} ÷ 60 = ${m} with remainder ${s}`;
}

// SIM 15: Elapsed Time Word Problem Solver
function sim15Select(scen) {
    ['picnic', 'homework', 'movie'].forEach(s => {
        const btn = document.getElementById(`sim15_btn_${s}`);
        if (btn) {
            btn.className = (scen === s) ?
                'px-2 py-1 rounded bg-amber-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const lbl1 = document.getElementById('sim15_lbl_1');
    const lbl2 = document.getElementById('sim15_lbl_2');
    const lbl3 = document.getElementById('sim15_lbl_3');
    const title = document.getElementById('sim15_title');
    const steps = document.getElementById('sim15_steps');
    const res = document.getElementById('sim15_res');

    if (scen === 'picnic') {
        if (lbl1) lbl1.textContent = '08:30 a.m.';
        if (lbl2) lbl2.textContent = '09:30 a.m.';
        if (lbl3) lbl3.textContent = '10:15 a.m.';
        if (title) title.textContent = 'Bus Journey (1 hr 45 min)';
        if (steps) steps.textContent = '08:30 + 1 hr = 09:30 ➔ + 45 min = 10:15 a.m.';
        if (res) res.textContent = '10:15 a.m.';
    } else if (scen === 'homework') {
        if (lbl1) lbl1.textContent = '04:15 p.m.';
        if (lbl2) lbl2.textContent = '05:15 p.m.';
        if (lbl3) lbl3.textContent = '05:40 p.m.';
        if (title) title.textContent = 'Homework Duration';
        if (steps) steps.textContent = '04:15 ➔ 05:15 (1 hr) + 25 min = 1 hr 25 min';
        if (res) res.textContent = '1 hr 25 min';
    } else if (scen === 'movie') {
        if (lbl1) lbl1.textContent = '02:45 p.m.';
        if (lbl2) lbl2.textContent = '03:00 p.m.';
        if (lbl3) lbl3.textContent = '05:00 p.m.';
        if (title) title.textContent = 'Movie Duration (2 hr 15 min)';
        if (steps) steps.textContent = '02:45 + 15 min = 03:00 ➔ + 2 hr = 05:00 p.m.';
        if (res) res.textContent = '05:00 p.m.';
    }
}

// SIM 16: Daily Time Schedules Planner
function sim16Highlight(evt) {
    ['assembly', 'lunch', 'sports', 'all'].forEach(e => {
        const btn = document.getElementById(`sim16_btn_${e}`);
        if (btn) {
            btn.className = (evt === e) ?
                'px-2 py-1 rounded bg-emerald-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const title = document.getElementById('sim16_title');
    const time = document.getElementById('sim16_time');

    if (evt === 'assembly') {
        if (title) title.textContent = 'Morning Assembly';
        if (time) time.textContent = '08:00 a.m. ➔ 08:25 a.m. (25 minutes)';
    } else if (evt === 'lunch') {
        if (title) title.textContent = 'Lunch Recess Duration';
        if (time) time.textContent = '12:15 p.m. + 40 min = 12:55 p.m.';
    } else if (evt === 'sports') {
        if (title) title.textContent = 'Sprint Training (High Precision)';
        if (time) time.textContent = '03:45 p.m. ➔ Track Sprint timed at 20.4 seconds!';
    } else {
        if (title) title.textContent = 'Full Day Overview';
        if (time) time.textContent = '08:00 a.m. to 05:00 p.m. seamlessly managed across hours, minutes, and seconds.';
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    if (synth) {
        populateVoiceList();
        if (synth.onvoiceschanged !== undefined) {
            synth.onvoiceschanged = populateVoiceList;
        }
    }
    showSlide(0);
});
"""

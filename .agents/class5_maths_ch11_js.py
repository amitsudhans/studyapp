# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 11: Grandmother's Quilt
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
let sim2CurrentShape = 'triangle';
let sim3TargetP = 26;
let sim4CurrentShape = 'squares';
let sim5CurrentUnit = 'books';
let sim6Layers = { whole: true, half: true, more: true };
let sim7CurrentHand = 'adrit';
let sim8CurrentLeaf = 'peepal';
let sim9CurrentConfig = 'strip';
let sim14CurrentObj = 'floor';
let sim16Mode = 'linear';
let sim16Tiles = [{x: 4, y: 3}];
let sim16LastRoll = 3;

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
        case 2: sim2Update(); break;
        case 3: sim3Update(); break;
        case 4: sim4Set(sim4CurrentShape); break;
        case 5: sim5Set(sim5CurrentUnit); break;
        case 6: sim6Render(); break;
        case 7: sim7Select(sim7CurrentHand); break;
        case 8: sim8Select(sim8CurrentLeaf); break;
        case 9: sim9Select(sim9CurrentConfig); break;
        case 10: sim10Update(); break;
        case 11: sim11Update(); break;
        case 12: sim12Update(); break;
        case 13: sim13Update(); break;
        case 14: sim14Select(sim14CurrentObj); break;
        case 15: sim15Update(); break;
        case 16: sim16Render(); break;
    }
}

// SIM 1: Quilt Lace Border Calculator
function sim1Update() {
    const lenEl = document.getElementById('sim1_len');
    const brdEl = document.getElementById('sim1_brd');
    if (!lenEl || !brdEl) return;

    const L = parseFloat(lenEl.value);
    const B = parseFloat(brdEl.value);

    const lenVal = document.getElementById('sim1_len_val');
    const brdVal = document.getElementById('sim1_brd_val');
    if (lenVal) lenVal.textContent = `${L.toFixed(1)} m`;
    if (brdVal) brdVal.textContent = `${B.toFixed(1)} m`;

    const P = 2 * (L + B);
    const cost = P * 15;

    const calcEl = document.getElementById('sim1_calc');
    const resPEl = document.getElementById('sim1_res_p');
    const resCostEl = document.getElementById('sim1_res_cost');
    if (calcEl) calcEl.textContent = `P = 2 × (${L.toFixed(1)} + ${B.toFixed(1)}) = ${P.toFixed(1)} m`;
    if (resPEl) resPEl.textContent = `${P.toFixed(1)} m`;
    if (resCostEl) resCostEl.textContent = `₹${Math.round(cost)}`;

    const topLbl = document.getElementById('sim1_top_lbl');
    const sideLbl = document.getElementById('sim1_side_lbl');
    if (topLbl) topLbl.textContent = `L = ${L.toFixed(1)} m`;
    if (sideLbl) sideLbl.textContent = `B = ${B.toFixed(1)} m`;

    const rect = document.getElementById('sim1_rect');
    const patches = document.getElementById('sim1_patches');
    if (rect && patches) {
        const svgW = 160;
        const svgH = 110;
        const scaleW = (L / 4.0) * svgW;
        const scaleH = (B / 3.0) * svgH;
        const startX = 110 - scaleW / 2;
        const startY = 80 - scaleH / 2;

        rect.setAttribute('x', startX);
        rect.setAttribute('y', startY);
        rect.setAttribute('width', scaleW);
        rect.setAttribute('height', scaleH);

        // Render patchwork grid inside
        const cols = Math.max(2, Math.round(L * 2));
        const rows = Math.max(2, Math.round(B * 2));
        const cellW = scaleW / cols;
        const cellH = scaleH / rows;

        const colors = ['#f43f5e', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#06b6d4'];
        let patchHtml = '';
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                const color = colors[(r * cols + c) % colors.length];
                patchHtml += `<rect x="${startX + c * cellW}" y="${startY + r * cellH}" width="${cellW}" height="${cellH}" fill="${color}" fill-opacity="0.35" stroke="#ffffff" stroke-width="0.75" stroke-opacity="0.4"/>`;
            }
        }
        patches.innerHTML = patchHtml;
    }
}

// SIM 2: Regular Polygon Perimeter Studio
function sim2SetShape(shape) {
    sim2CurrentShape = shape;
    ['tri', 'sq', 'pen', 'hex', 'oct'].forEach(s => {
        const btn = document.getElementById(`sim2_btn_${s}`);
        if (btn) {
            btn.className = (shape.startsWith(s)) ?
                'px-2 py-1 rounded bg-indigo-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });
    sim2Update();
}

function sim2Update() {
    const sideEl = document.getElementById('sim2_side');
    if (!sideEl) return;
    const s = parseInt(sideEl.value, 10);
    const sideVal = document.getElementById('sim2_side_val');
    if (sideVal) sideVal.textContent = `${s} cm`;

    let n = 3;
    let name = 'Equilateral Triangle';
    if (sim2CurrentShape === 'square') { n = 4; name = 'Square'; }
    else if (sim2CurrentShape === 'pentagon') { n = 5; name = 'Regular Pentagon'; }
    else if (sim2CurrentShape === 'hexagon') { n = 6; name = 'Regular Hexagon'; }
    else if (sim2CurrentShape === 'octagon') { n = 8; name = 'Regular Octagon'; }

    const P = n * s;
    const calcEl = document.getElementById('sim2_calc');
    const resPEl = document.getElementById('sim2_res_p');
    if (calcEl) calcEl.textContent = `P = ${n} × ${s} = ${P} cm`;
    if (resPEl) resPEl.textContent = `${P} cm`;

    // Render regular polygon vertices in SVG
    const poly = document.getElementById('sim2_poly');
    const lbl = document.getElementById('sim2_poly_lbl');
    if (poly) {
        const cx = 100, cy = 75, r = 50;
        let points = [];
        for (let i = 0; i < n; i++) {
            const angle = (i * 2 * Math.PI / n) - (Math.PI / 2);
            const px = cx + r * Math.cos(angle);
            const py = cy + r * Math.sin(angle);
            points.push(`${px.toFixed(1)},${py.toFixed(1)}`);
        }
        poly.setAttribute('points', points.join(' '));
    }
    if (lbl) lbl.textContent = `s = ${s} cm (${name})`;
}

// SIM 3: Fixed Perimeter Rectangle Generator
function sim3SetP(targetP) {
    sim3TargetP = targetP;
    const btn26 = document.getElementById('sim3_btn_26');
    const btn18 = document.getElementById('sim3_btn_18');
    const lenEl = document.getElementById('sim3_len');

    if (targetP === 26) {
        if (btn26) btn26.className = 'px-2.5 py-1 rounded bg-indigo-600 text-white font-semibold';
        if (btn18) btn18.className = 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        if (lenEl) { lenEl.max = 12; lenEl.value = 8; }
    } else {
        if (btn18) btn18.className = 'px-2.5 py-1 rounded bg-indigo-600 text-white font-semibold';
        if (btn26) btn26.className = 'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        if (lenEl) { lenEl.max = 8; lenEl.value = 6; }
    }
    sim3Update();
}

function sim3Update() {
    const lenEl = document.getElementById('sim3_len');
    if (!lenEl) return;
    const L = parseInt(lenEl.value, 10);
    const halfP = sim3TargetP / 2;
    const B = halfP - L;

    const lenVal = document.getElementById('sim3_len_val');
    if (lenVal) lenVal.textContent = `${L} cm`;

    const area = L * B;
    const P = 2 * (L + B);

    const calcEl = document.getElementById('sim3_calc');
    const resPEl = document.getElementById('sim3_res_p');
    const resAEl = document.getElementById('sim3_res_a');
    if (calcEl) calcEl.textContent = `L = ${L} cm, B = ${B} cm (Sum = ${L+B} cm)`;
    if (resPEl) resPEl.textContent = `2 × (${L} + ${B}) = ${P} cm`;
    if (resAEl) resAEl.textContent = `${L} × ${B} = ${area} cm²`;

    const rect = document.getElementById('sim3_rect');
    const topLbl = document.getElementById('sim3_top_lbl');
    const sideLbl = document.getElementById('sim3_side_lbl');
    const areaLbl = document.getElementById('sim3_area_lbl');

    if (rect) {
        const scaleW = Math.max(20, L * 12);
        const scaleH = Math.max(15, B * 12);
        const startX = 100 - scaleW / 2;
        const startY = 80 - scaleH / 2;
        rect.setAttribute('x', startX);
        rect.setAttribute('y', startY);
        rect.setAttribute('width', scaleW);
        rect.setAttribute('height', scaleH);

        if (topLbl) {
            topLbl.setAttribute('x', 100);
            topLbl.setAttribute('y', Math.max(12, startY - 6));
            topLbl.textContent = `L = ${L} cm`;
        }
        if (sideLbl) {
            sideLbl.setAttribute('x', Math.max(12, startX - 8));
            sideLbl.setAttribute('y', 80);
            sideLbl.textContent = `B = ${B} cm`;
        }
        if (areaLbl) {
            areaLbl.setAttribute('x', 100);
            areaLbl.setAttribute('y', 84);
            areaLbl.textContent = `${area} cm²`;
        }
    }
}

// SIM 4: Tessellation Lab
function sim4Set(shape) {
    sim4CurrentShape = shape;
    ['sq', 'tri', 'hex', 'cir'].forEach(s => {
        const btn = document.getElementById(`sim4_btn_${s}`);
        if (btn) {
            btn.className = (shape.startsWith(s)) ?
                'px-2 py-1 rounded bg-emerald-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const grid = document.getElementById('sim4_grid');
    const descEl = document.getElementById('sim4_desc');
    const gapsEl = document.getElementById('sim4_gaps');
    const statusEl = document.getElementById('sim4_status');
    if (!grid) return;

    let html = '';
    if (shape === 'squares') {
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 5; c++) {
                html += `<rect x="${25 + c * 30}" y="${20 + r * 30}" width="30" height="30" fill="#047857" stroke="#34d399" stroke-width="1.5"/>`;
            }
        }
        if (descEl) descEl.textContent = 'Squares tile edge-to-edge seamlessly with zero empty gaps!';
        if (gapsEl) gapsEl.textContent = '0% (Completely Covered)';
        if (statusEl) {
            statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            statusEl.textContent = 'Seamless Tessellation';
        }
    } else if (shape === 'triangles') {
        const w = 34, h = 28;
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 5; c++) {
                const x = 20 + c * w;
                const y = 20 + r * h;
                html += `<polygon points="${x},${y+h} ${x+w/2},${y} ${x+w},${y+h}" fill="#0d9488" stroke="#2dd4bf" stroke-width="1.2"/>`;
                html += `<polygon points="${x+w/2},${y} ${x+w},${y+h} ${x+w*1.5},${y}" fill="#0f766e" stroke="#2dd4bf" stroke-width="1.2"/>`;
            }
        }
        if (descEl) descEl.textContent = 'Equilateral triangles interlock edge-to-edge with 0% gap space!';
        if (gapsEl) gapsEl.textContent = '0% (Seamless Tiling)';
        if (statusEl) {
            statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30';
            statusEl.textContent = 'Seamless Tessellation';
        }
    } else if (shape === 'hexagons') {
        const r = 16;
        for (let row = 0; row < 4; row++) {
            for (let col = 0; col < 5; col++) {
                const cx = 35 + col * 28 + (row % 2 ? 14 : 0);
                const cy = 30 + row * 24;
                let pts = [];
                for (let i = 0; i < 6; i++) {
                    const a = i * Math.PI / 3;
                    pts.push(`${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a)).toFixed(1)}`);
                }
                html += `<polygon points="${pts.join(' ')}" fill="#0284c7" stroke="#38bdf8" stroke-width="1.2"/>`;
            }
        }
        if (descEl) descEl.textContent = 'Hexagons form a perfect honeycomb lattice with zero gaps!';
        if (gapsEl) gapsEl.textContent = '0% (Honeycomb Lattice)';
        if (statusEl) {
            statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30';
            statusEl.textContent = 'Seamless Tessellation';
        }
    } else if (shape === 'circles') {
        const r = 15;
        for (let row = 0; row < 4; row++) {
            for (let col = 0; col < 5; col++) {
                const cx = 40 + col * 30;
                const cy = 35 + row * 30;
                html += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#9333ea" stroke="#c084fc" stroke-width="1.5"/>`;
                if (row < 3 && col < 4) {
                    html += `<circle cx="${cx + 15}" cy="${cy + 15}" r="4" fill="#f43f5e" opacity="0.8"/>`;
                }
            }
        }
        if (descEl) descEl.textContent = 'Circles leave unfilled diamond voids (red dots)! Circles cannot tile a plane!';
        if (gapsEl) gapsEl.textContent = '~21.5% Empty Voids (Gaps!)';
        if (statusEl) {
            statusEl.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';
            statusEl.textContent = 'Fails Tessellation (Gaps)';
        }
    }
    grid.innerHTML = html;
}

// SIM 5: Non-Standard Desk Covering Studio
function sim5Set(unit) {
    sim5CurrentUnit = unit;
    ['books', 'boxes', 'tri'].forEach(u => {
        const btn = document.getElementById(`sim5_btn_${u}`);
        if (btn) {
            btn.className = (unit.startsWith(u)) ?
                'px-2 py-1 rounded bg-amber-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const items = document.getElementById('sim5_items');
    const descEl = document.getElementById('sim5_desc');
    const ruleEl = document.getElementById('sim5_rule');
    if (!items) return;

    let html = '';
    if (unit === 'books') {
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 6; c++) {
                html += `<rect x="${24 + c * 25.5}" y="${24 + r * 28}" width="23.5" height="26" rx="2" fill="#d97706" stroke="#fcd34d" stroke-width="1"/>`;
                html += `<text x="${24 + c * 25.5 + 11.5}" y="${24 + r * 28 + 16}" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Book</text>`;
            }
        }
        if (descEl) descEl.textContent = '24 Mathematics textbooks (6 × 4) completely cover the desk surface.';
        if (ruleEl) ruleEl.textContent = 'Area = 24 Textbooks';
    } else if (unit === 'boxes') {
        for (let r = 0; r < 5; r++) {
            for (let c = 0; c < 8; c++) {
                html += `<rect x="${23 + c * 19}" y="${23 + r * 22.5}" width="17.5" height="20.5" rx="2" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>`;
            }
        }
        if (descEl) descEl.textContent = '40 Pencil boxes (8 × 5) cover the exact same desk surface.';
        if (ruleEl) ruleEl.textContent = 'Area = 40 Pencil Boxes';
    } else if (unit === 'triangles') {
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 6; c++) {
                const x = 24 + c * 25.5;
                const y = 24 + r * 28;
                html += `<polygon points="${x},${y} ${x+24},${y} ${x+24},${y+26}" fill="#10b981" stroke="#34d399" stroke-width="0.75"/>`;
                html += `<polygon points="${x},${y} ${x},${y+26} ${x+24},${y+26}" fill="#059669" stroke="#34d399" stroke-width="0.75"/>`;
            }
        }
        if (descEl) descEl.textContent = '48 Half-triangles join in pairs to form 24 full square units.';
        if (ruleEl) ruleEl.textContent = '2 Half-Triangles = 1 Unit Square';
    }
    items.innerHTML = html;
}

// SIM 6: 1 cm² Grid Overlay Tool
function sim6Toggle(layer) {
    sim6Layers[layer] = !sim6Layers[layer];
    const btn = document.getElementById(layer === 'whole' ? 'sim6_btn_w' : (layer === 'half' ? 'sim6_btn_h' : 'sim6_btn_m'));
    if (btn) {
        btn.classList.toggle('opacity-50', !sim6Layers[layer]);
    }
    sim6Render();
}

function sim6Render() {
    const gridLines = document.getElementById('sim6_grid_lines');
    const markers = document.getElementById('sim6_markers');
    if (!gridLines || !markers) return;

    // Draw coordinate grid lines
    let gl = '';
    for (let x = 20; x <= 180; x += 16) {
        gl += `<line x1="${x}" y1="20" x2="${x}" y2="140" stroke="#334155" stroke-width="0.75"/>`;
    }
    for (let y = 20; y <= 140; y += 16) {
        gl += `<line x1="20" y1="${y}" x2="180" y2="${y}" stroke="#334155" stroke-width="0.75"/>`;
    }
    gridLines.innerHTML = gl;

    let mHtml = '';
    // Whole squares (teal)
    const wholeCells = [
        [4,3], [5,3], [6,3], [7,3],
        [4,4], [5,4], [6,4], [7,4],
        [4,5], [5,5], [6,5], [7,5]
    ];
    if (sim6Layers.whole) {
        wholeCells.forEach(([c, r]) => {
            mHtml += `<rect x="${20 + c * 16}" y="${20 + r * 16}" width="16" height="16" fill="#14b8a6" fill-opacity="0.6" stroke="#2dd4bf" stroke-width="0.5"/>`;
        });
    }

    // Half squares (cyan)
    const halfCells = [
        [3,3], [8,3], [3,5], [8,5], [5,2], [6,6]
    ];
    if (sim6Layers.half) {
        halfCells.forEach(([c, r]) => {
            mHtml += `<rect x="${20 + c * 16}" y="${20 + r * 16}" width="16" height="16" fill="#06b6d4" fill-opacity="0.6" stroke="#22d3ee" stroke-width="0.5"/>`;
        });
    }

    // More than half squares (indigo)
    const moreCells = [
        [4,2], [7,2], [4,6], [7,6]
    ];
    if (sim6Layers.more) {
        moreCells.forEach(([c, r]) => {
            mHtml += `<rect x="${20 + c * 16}" y="${20 + r * 16}" width="16" height="16" fill="#6366f1" fill-opacity="0.6" stroke="#818cf8" stroke-width="0.5"/>`;
        });
    }
    markers.innerHTML = mHtml;

    const wCount = sim6Layers.whole ? 12 : 0;
    const hCount = sim6Layers.half ? 6 : 0;
    const mCount = sim6Layers.more ? 4 : 0;
    const total = wCount + (hCount * 0.5) + mCount;

    const resA = document.getElementById('sim6_res_a');
    if (resA) resA.textContent = `${total.toFixed(1)} cm²`;
}

// SIM 7: Palm Tracing Simulator
function sim7Select(who) {
    sim7CurrentHand = who;
    ['adrit', 'preetha', 'dadi'].forEach(w => {
        const btn = document.getElementById(`sim7_btn_${w}`);
        if (btn) {
            btn.className = (who === w) ?
                'px-2.5 py-1 rounded bg-rose-600 text-white font-semibold' :
                'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const handPath = document.getElementById('sim7_hand');
    const descEl = document.getElementById('sim7_desc');
    const compEl = document.getElementById('sim7_comp');
    const grid = document.getElementById('sim7_grid');
    if (!handPath || !grid) return;

    // Grid background
    let gl = '';
    for (let x = 20; x <= 180; x += 15) {
        gl += `<line x1="${x}" y1="15" x2="${x}" y2="145" stroke="#334155" stroke-width="0.6"/>`;
    }
    for (let y = 15; y <= 145; y += 15) {
        gl += `<line x1="20" y1="${y}" x2="180" y2="${y}" stroke="#334155" stroke-width="0.6"/>`;
    }
    grid.innerHTML = gl;

    if (who === 'adrit') {
        handPath.setAttribute('d', 'M 75,135 C 65,115 50,95 45,75 C 42,65 52,60 56,70 C 60,50 68,45 74,58 C 78,35 88,35 90,55 C 95,45 105,48 104,65 C 112,65 118,75 110,95 C 105,115 95,135 75,135 Z');
        if (descEl) descEl.textContent = "Adrit's palm covers 52 square centimetres on the 1 cm grid.";
        if (compEl) compEl.textContent = 'Adrit > Preetha (+6 cm²)';
    } else if (who === 'preetha') {
        handPath.setAttribute('d', 'M 78,135 C 70,118 55,100 52,82 C 49,72 58,68 62,77 C 65,60 72,55 77,66 C 81,48 89,48 91,65 C 95,57 103,58 102,72 C 108,72 114,80 108,98 C 103,115 94,135 78,135 Z');
        if (descEl) descEl.textContent = "Preetha's palm covers 46 square centimetres on the 1 cm grid.";
        if (compEl) compEl.textContent = 'Preetha < Adrit (-6 cm²)';
    } else if (who === 'dadi') {
        handPath.setAttribute('d', 'M 70,140 C 58,115 40,90 35,68 C 30,55 42,50 48,62 C 52,40 62,35 70,50 C 75,25 88,25 92,48 C 98,35 110,40 108,58 C 118,60 125,72 118,95 C 112,120 98,140 70,140 Z');
        if (descEl) descEl.textContent = "Grandmother's palm covers 72 square centimetres on the 1 cm grid.";
        if (compEl) compEl.textContent = 'Grandmother > Children (+20 cm²)';
    }
}

// SIM 8: Garden Leaf Surface Ranker
function sim8Select(leaf) {
    sim8CurrentLeaf = leaf;
    ['cor', 'neem', 'mango', 'peepal'].forEach(l => {
        const btn = document.getElementById(`sim8_btn_${l}`);
        if (btn) {
            btn.className = (leaf.startsWith(l)) ?
                'px-2 py-1 rounded bg-emerald-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const leafPath = document.getElementById('sim8_leaf');
    const descEl = document.getElementById('sim8_desc');
    const rankEl = document.getElementById('sim8_rank');
    const grid = document.getElementById('sim8_grid');
    if (!leafPath || !grid) return;

    // Grid lines
    let gl = '';
    for (let x = 20; x <= 180; x += 15) {
        gl += `<line x1="${x}" y1="15" x2="${x}" y2="145" stroke="#334155" stroke-width="0.6"/>`;
    }
    for (let y = 15; y <= 145; y += 15) {
        gl += `<line x1="20" y1="${y}" x2="180" y2="${y}" stroke="#334155" stroke-width="0.6"/>`;
    }
    grid.innerHTML = gl;

    if (leaf === 'coriander') {
        leafPath.setAttribute('d', 'M 95,95 C 90,85 88,78 95,70 C 98,65 105,65 106,72 C 112,78 108,88 95,95 Z');
        if (descEl) descEl.textContent = 'Tiny coriander leaflet covers only ~3 cm² of surface area.';
        if (rankEl) rankEl.textContent = 'Smallest (Rank 1 of 4)';
    } else if (leaf === 'neem') {
        leafPath.setAttribute('d', 'M 100,120 C 85,95 85,65 100,45 C 115,65 115,95 100,120 Z');
        if (descEl) descEl.textContent = 'Slender neem leaflet spans ~8 cm² of surface area.';
        if (rankEl) rankEl.textContent = 'Small (Rank 2 of 4)';
    } else if (leaf === 'mango') {
        leafPath.setAttribute('d', 'M 100,135 C 75,100 70,55 100,25 C 130,55 125,100 100,135 Z');
        if (descEl) descEl.textContent = 'Elongated mango leaf covers ~32 cm² of surface area.';
        if (rankEl) rankEl.textContent = 'Medium (Rank 3 of 4)';
    } else if (leaf === 'peepal') {
        leafPath.setAttribute('d', 'M 100,140 C 60,110 45,70 80,40 C 95,25 100,15 100,15 C 100,15 105,25 120,40 C 155,70 140,110 100,140 Z');
        if (descEl) descEl.textContent = 'Broad heart-shaped peepal leaf covers ~70 cm² of surface area.';
        if (rankEl) rankEl.textContent = 'Largest (Rank 4 of 4)';
    }
}

// SIM 9: Same Area, Different Perimeter Studio
function sim9Select(config) {
    sim9CurrentConfig = config;
    ['strip', 'mid', 'compact'].forEach(c => {
        const btn = document.getElementById(`sim9_btn_${c}`);
        if (btn) {
            btn.className = (config === c) ?
                'px-2.5 py-1 rounded bg-amber-600 text-white font-semibold' :
                'px-2.5 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const tiles = document.getElementById('sim9_tiles');
    const dimEl = document.getElementById('sim9_dim');
    const pEl = document.getElementById('sim9_p');
    if (!tiles) return;

    let html = '';
    if (config === 'strip') {
        // 1 × 12
        for (let i = 0; i < 12; i++) {
            html += `<rect x="${20 + i * 13}" y="70" width="13" height="20" fill="#d97706" stroke="#fbbf24" stroke-width="1"/>`;
        }
        if (dimEl) dimEl.textContent = 'Dimensions: 1 cm × 12 cm';
        if (pEl) pEl.textContent = '2 × (1 + 12) = 26 cm (Maximum!)';
    } else if (config === 'mid') {
        // 2 × 6
        for (let r = 0; r < 2; r++) {
            for (let c = 0; c < 6; c++) {
                html += `<rect x="${40 + c * 20}" y="${55 + r * 25}" width="20" height="25" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>`;
            }
        }
        if (dimEl) dimEl.textContent = 'Dimensions: 2 cm × 6 cm';
        if (pEl) pEl.textContent = '2 × (2 + 6) = 16 cm (Moderate)';
    } else if (config === 'compact') {
        // 3 × 4
        for (let r = 0; r < 3; r++) {
            for (let c = 0; c < 4; c++) {
                html += `<rect x="${55 + c * 22}" y="${45 + r * 22}" width="22" height="22" fill="#059669" stroke="#34d399" stroke-width="1"/>`;
            }
        }
        if (dimEl) dimEl.textContent = 'Dimensions: 3 cm × 4 cm';
        if (pEl) pEl.textContent = '2 × (3 + 4) = 14 cm (Minimum!)';
    }
    tiles.innerHTML = html;
}

// SIM 10: Same Perimeter, Different Area Studio
function sim10Update() {
    const lenEl = document.getElementById('sim10_len');
    if (!lenEl) return;
    const L = parseInt(lenEl.value, 10);
    const B = 12 - L;
    const area = L * B;

    const lenVal = document.getElementById('sim10_len_val');
    if (lenVal) lenVal.textContent = `${L} cm`;

    const dimsEl = document.getElementById('sim10_dims');
    const resAEl = document.getElementById('sim10_res_a');
    if (dimsEl) dimsEl.textContent = `Dimensions: ${L} cm × ${B} cm`;
    if (resAEl) {
        if (L === 6) resAEl.textContent = `${area} cm² (★ Max Area! Square)`;
        else resAEl.textContent = `${area} cm²`;
    }

    const rect = document.getElementById('sim10_rect');
    const lblL = document.getElementById('sim10_lbl_l');
    const lblB = document.getElementById('sim10_lbl_b');
    const lblA = document.getElementById('sim10_lbl_a');

    if (rect) {
        const scaleW = Math.max(16, L * 13);
        const scaleH = Math.max(16, B * 13);
        const startX = 100 - scaleW / 2;
        const startY = 80 - scaleH / 2;
        rect.setAttribute('x', startX);
        rect.setAttribute('y', startY);
        rect.setAttribute('width', scaleW);
        rect.setAttribute('height', scaleH);

        if (lblL) {
            lblL.setAttribute('x', 100);
            lblL.setAttribute('y', Math.max(14, startY - 6));
            lblL.textContent = `L = ${L} cm`;
        }
        if (lblB) {
            lblB.setAttribute('x', Math.max(12, startX - 8));
            lblB.setAttribute('y', 80);
            lblB.textContent = `B = ${B} cm`;
        }
        if (lblA) {
            lblA.setAttribute('x', 100);
            lblA.setAttribute('y', 84);
            lblA.textContent = `${area} cm²`;
        }
    }
}

// SIM 11: Row-Column Array Multiplier
function sim11Update() {
    const rowsEl = document.getElementById('sim11_rows');
    const colsEl = document.getElementById('sim11_cols');
    if (!rowsEl || !colsEl) return;

    const R = parseInt(rowsEl.value, 10);
    const C = parseInt(colsEl.value, 10);

    const rowVal = document.getElementById('sim11_row_val');
    const colVal = document.getElementById('sim11_col_val');
    if (rowVal) rowVal.textContent = R;
    if (colVal) colVal.textContent = C;

    const total = R * C;
    const calcEl = document.getElementById('sim11_calc');
    const resTotEl = document.getElementById('sim11_res_tot');
    if (calcEl) calcEl.textContent = `${R} Rows × ${C} Columns = ${total} cm²`;
    if (resTotEl) resTotEl.textContent = `${total} Squares`;

    const grid = document.getElementById('sim11_grid');
    if (!grid) return;

    const tileW = Math.min(22, 140 / C);
    const tileH = Math.min(22, 100 / R);
    const startX = 100 - (C * tileW) / 2;
    const startY = 80 - (R * tileH) / 2;

    let html = '';
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            html += `<rect x="${startX + c * tileW}" y="${startY + r * tileH}" width="${tileW}" height="${tileH}" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.2"/>`;
        }
    }
    grid.innerHTML = html;
}

// SIM 12: Rectangle Dimensions & Formula Lab
function sim12Update() {
    const lenEl = document.getElementById('sim12_len');
    const brdEl = document.getElementById('sim12_brd');
    if (!lenEl || !brdEl) return;

    const L = parseInt(lenEl.value, 10);
    const B = parseInt(brdEl.value, 10);

    const lenVal = document.getElementById('sim12_len_val');
    const brdVal = document.getElementById('sim12_brd_val');
    if (lenVal) lenVal.textContent = `${L} cm`;
    if (brdVal) brdVal.textContent = `${B} cm`;

    const area = L * B;
    const P = 2 * (L + B);

    const resA = document.getElementById('sim12_res_a');
    const resP = document.getElementById('sim12_res_p');
    if (resA) resA.textContent = `Area = ${L} × ${B} = ${area} cm²`;
    if (resP) resP.textContent = `P = 2 × (${L} + ${B}) = ${P} cm`;

    const rect = document.getElementById('sim12_rect');
    const topLbl = document.getElementById('sim12_top_lbl');
    const sideLbl = document.getElementById('sim12_side_lbl');
    const areaLbl = document.getElementById('sim12_area_lbl');

    if (rect) {
        const scaleW = Math.max(20, L * 12);
        const scaleH = Math.max(15, B * 12);
        const startX = 100 - scaleW / 2;
        const startY = 80 - scaleH / 2;
        rect.setAttribute('x', startX);
        rect.setAttribute('y', startY);
        rect.setAttribute('width', scaleW);
        rect.setAttribute('height', scaleH);

        if (topLbl) {
            topLbl.setAttribute('x', 100);
            topLbl.setAttribute('y', Math.max(12, startY - 6));
            topLbl.textContent = `L = ${L} cm`;
        }
        if (sideLbl) {
            sideLbl.setAttribute('x', Math.max(12, startX - 8));
            sideLbl.setAttribute('y', 80);
            sideLbl.textContent = `B = ${B} cm`;
        }
        if (areaLbl) {
            areaLbl.setAttribute('x', 100);
            areaLbl.setAttribute('y', 84);
            areaLbl.textContent = `${area} cm²`;
        }
    }
}

// SIM 13: Square Area & Perimeter Benchmarker
function sim13Update() {
    const sideEl = document.getElementById('sim13_side');
    if (!sideEl) return;
    const s = parseInt(sideEl.value, 10);

    const sideVal = document.getElementById('sim13_side_val');
    if (sideVal) sideVal.textContent = `${s} cm`;

    const area = s * s;
    const P = 4 * s;

    const resA = document.getElementById('sim13_res_a');
    const resP = document.getElementById('sim13_res_p');
    if (resA) resA.textContent = `${s} × ${s} = ${area} cm²`;
    if (resP) resP.textContent = `4 × ${s} = ${P} cm`;

    const sq = document.getElementById('sim13_sq');
    const topLbl = document.getElementById('sim13_top_lbl');
    const innerLbl = document.getElementById('sim13_inner_lbl');

    if (sq) {
        const size = Math.max(20, s * 10);
        const startX = 100 - size / 2;
        const startY = 80 - size / 2;
        sq.setAttribute('x', startX);
        sq.setAttribute('y', startY);
        sq.setAttribute('width', size);
        sq.setAttribute('height', size);

        if (topLbl) {
            topLbl.setAttribute('x', 100);
            topLbl.setAttribute('y', Math.max(12, startY - 6));
            topLbl.textContent = `s = ${s} cm`;
        }
        if (innerLbl) {
            innerLbl.setAttribute('x', 100);
            innerLbl.setAttribute('y', 84);
            innerLbl.textContent = `${area} cm²`;
        }
    }
}

// SIM 14: Classroom & Object Dimension Auditor
function sim14Select(obj) {
    sim14CurrentObj = obj;
    ['floor', 'board', 'book', 'ludo'].forEach(o => {
        const btn = document.getElementById(`sim14_btn_${o}`);
        if (btn) {
            btn.className = (obj === o) ?
                'px-2 py-1 rounded bg-purple-600 text-white font-semibold' :
                'px-2 py-1 rounded bg-slate-800 text-slate-200';
        }
    });

    const titleEl = document.getElementById('sim14_lbl_title');
    const dimsEl = document.getElementById('sim14_lbl_dims');
    const unitEl = document.getElementById('sim14_unit');
    const pEl = document.getElementById('sim14_p');
    const aEl = document.getElementById('sim14_a');
    const useEl = document.getElementById('sim14_use');

    if (obj === 'floor') {
        if (titleEl) titleEl.textContent = 'Classroom Floor';
        if (dimsEl) dimsEl.textContent = '8 m × 6 m';
        if (unitEl) unitEl.textContent = 'Standard Unit: Metres & Square Metres (m²)';
        if (pEl) pEl.textContent = 'Perimeter (Skirting): 2 × (8 + 6) = 28 m';
        if (aEl) aEl.textContent = 'Area (Tiling): 8 × 6 = 48 m²';
        if (useEl) useEl.textContent = 'Application: Tiles or carpets are bought by square metres.';
    } else if (obj === 'board') {
        if (titleEl) titleEl.textContent = 'School Blackboard';
        if (dimsEl) dimsEl.textContent = '3 m × 1.5 m';
        if (unitEl) unitEl.textContent = 'Standard Unit: Metres & Square Metres (m²)';
        if (pEl) pEl.textContent = 'Perimeter (Border Frame): 2 × (3 + 1.5) = 9 m';
        if (aEl) aEl.textContent = 'Area (Paint Surface): 3 × 1.5 = 4.5 m²';
        if (useEl) useEl.textContent = 'Application: Blackboard paint is calculated by surface area.';
    } else if (obj === 'book') {
        if (titleEl) titleEl.textContent = 'Notebook Cover';
        if (dimsEl) dimsEl.textContent = '20 cm × 15 cm';
        if (unitEl) unitEl.textContent = 'Standard Unit: Centimetres & Square Centimetres (cm²)';
        if (pEl) pEl.textContent = 'Perimeter: 2 × (20 + 15) = 70 cm';
        if (aEl) aEl.textContent = 'Area: 20 × 15 = 300 cm²';
        if (useEl) useEl.textContent = 'Application: Brown covering paper needs 300 cm² surface coverage.';
    } else if (obj === 'ludo') {
        if (titleEl) titleEl.textContent = 'Square Ludo Board';
        if (dimsEl) dimsEl.textContent = '40 cm × 40 cm';
        if (unitEl) unitEl.textContent = 'Standard Unit: Centimetres & Square Centimetres (cm²)';
        if (pEl) pEl.textContent = 'Perimeter: 4 × 40 = 160 cm';
        if (aEl) aEl.textContent = 'Area: 40 × 40 = 1,600 cm²';
        if (useEl) useEl.textContent = 'Application: Game board layout is divided into 4 colored zones.';
    }
}

// SIM 15: Missing Dimension Solver
function sim15Update() {
    const areaEl = document.getElementById('sim15_area');
    const lenEl = document.getElementById('sim15_len');
    if (!areaEl || !lenEl) return;

    const A = parseInt(areaEl.value, 10);
    const L = parseInt(lenEl.value, 10);
    const B = (A / L);

    const areaVal = document.getElementById('sim15_area_val');
    const lenVal = document.getElementById('sim15_len_val');
    if (areaVal) areaVal.textContent = `${A} m²`;
    if (lenVal) lenVal.textContent = `${L} m`;

    const calcEl = document.getElementById('sim15_calc');
    const resBEl = document.getElementById('sim15_res_b');
    if (calcEl) calcEl.textContent = `B = ${A} ÷ ${L} = ${B.toFixed(1)} m`;
    if (resBEl) resBEl.textContent = `${B.toFixed(1)} m`;

    const rect = document.getElementById('sim15_rect');
    const topLbl = document.getElementById('sim15_top_lbl');
    const sideLbl = document.getElementById('sim15_side_lbl');
    const innerLbl = document.getElementById('sim15_inner_lbl');

    if (rect) {
        const scaleW = Math.max(20, Math.min(140, L * 10));
        const scaleH = Math.max(15, Math.min(100, B * 10));
        const startX = 100 - scaleW / 2;
        const startY = 80 - scaleH / 2;
        rect.setAttribute('x', startX);
        rect.setAttribute('y', startY);
        rect.setAttribute('width', scaleW);
        rect.setAttribute('height', scaleH);

        if (topLbl) {
            topLbl.setAttribute('x', 100);
            topLbl.setAttribute('y', Math.max(12, startY - 6));
            topLbl.textContent = `L = ${L} m`;
        }
        if (sideLbl) {
            sideLbl.setAttribute('x', Math.max(12, startX - 8));
            sideLbl.setAttribute('y', 80);
            sideLbl.textContent = `B = ${B.toFixed(1)} m`;
        }
        if (innerLbl) {
            innerLbl.setAttribute('x', 100);
            innerLbl.setAttribute('y', 84);
            innerLbl.textContent = `${A} m²`;
        }
    }
}

// SIM 16: Perimeter Building Dice Game
function sim16SetMode(mode) {
    sim16Mode = mode;
    const btnLin = document.getElementById('sim16_btn_lin');
    const btnCor = document.getElementById('sim16_btn_cor');
    if (btnLin) {
        btnLin.className = (mode === 'linear') ?
            'px-2 py-1 rounded bg-indigo-600 text-white font-semibold' :
            'px-2 py-1 rounded bg-slate-800 text-slate-200';
    }
    if (btnCor) {
        btnCor.className = (mode === 'corner') ?
            'px-2 py-1 rounded bg-indigo-600 text-white font-semibold' :
            'px-2 py-1 rounded bg-slate-800 text-slate-200';
    }
}

function sim16Roll() {
    const roll = Math.floor(Math.random() * 6) + 1;
    sim16LastRoll = roll;
    const dieVal = document.getElementById('sim16_die_val');
    if (dieVal) dieVal.textContent = roll;

    // Add 'roll' tiles based on mode
    for (let i = 0; i < roll; i++) {
        if (sim16Tiles.length >= 25) break;
        if (sim16Mode === 'linear') {
            const last = sim16Tiles[sim16Tiles.length - 1];
            // Extend to the right or snake down
            if (last.x < 8) sim16Tiles.push({ x: last.x + 1, y: last.y });
            else sim16Tiles.push({ x: 2, y: last.y + 1 });
        } else {
            // Corner placement: attach next to an existing tile with at least 1-2 neighbors
            const last = sim16Tiles[sim16Tiles.length - 1];
            if (last.y < 5) sim16Tiles.push({ x: last.x, y: last.y + 1 });
            else sim16Tiles.push({ x: Math.max(1, last.x - 1), y: last.y });
        }
    }

    sim16Render();
}

function sim16Reset() {
    sim16Tiles = [{ x: 4, y: 3 }];
    sim16LastRoll = 1;
    const dieVal = document.getElementById('sim16_die_val');
    if (dieVal) dieVal.textContent = '1';
    sim16Render();
}

function sim16CalculatePerimeter() {
    // Count exposed edges of all tiles
    const tileSet = new Set(sim16Tiles.map(t => `${t.x},${t.y}`));
    let exposed = 0;
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    sim16Tiles.forEach(t => {
        dirs.forEach(([dx, dy]) => {
            if (!tileSet.has(`${t.x + dx},${t.y + dy}`)) {
                exposed++;
            }
        });
    });
    return exposed;
}

function sim16Render() {
    const grid = document.getElementById('sim16_grid');
    const pEl = document.getElementById('sim16_p');
    const tilesCntEl = document.getElementById('sim16_tiles_cnt');
    const msgEl = document.getElementById('sim16_msg');
    if (!grid) return;

    const P = sim16CalculatePerimeter();
    if (pEl) pEl.textContent = `P = ${P} units`;
    if (tilesCntEl) tilesCntEl.textContent = `${sim16Tiles.length} Tiles (Area = ${sim16Tiles.length})`;

    if (msgEl) {
        if (P === 24) {
            msgEl.className = 'text-emerald-400 font-bold';
            msgEl.textContent = '🎉 VICTORY! Exact perimeter 24 reached!';
        } else if (P < 24) {
            msgEl.className = 'text-cyan-400 font-bold';
            msgEl.textContent = `Game In Progress: Need ${24 - P} more perimeter units!`;
        } else {
            msgEl.className = 'text-rose-400 font-bold';
            msgEl.textContent = `Overshot: Perimeter is ${P} (>24). Reset to try again!`;
        }
    }

    // Draw 10x8 grid in SVG
    const tileW = 16;
    let html = '';
    for (let x = 0; x < 10; x++) {
        for (let y = 0; y < 8; y++) {
            html += `<rect x="${20 + x * tileW}" y="${16 + y * tileW}" width="${tileW}" height="${tileW}" fill="#0f172a" stroke="#1e293b" stroke-width="0.75"/>`;
        }
    }

    // Draw active tiles
    sim16Tiles.forEach(t => {
        html += `<rect x="${20 + t.x * tileW}" y="${16 + t.y * tileW}" width="${tileW}" height="${tileW}" fill="#f59e0b" stroke="#fef08a" stroke-width="1.5" rx="1.5"/>`;
    });

    grid.innerHTML = html;
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

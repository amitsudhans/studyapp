# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 8: Weight and Capacity
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
let sim1Current = 'rice';
let sim5Items = {};
let sim6State = { elephant: false, stones: 0 };
let sim7Step = 0, sim7Data = { kg1: 45, g1: 750, kg2: 38, g2: 650, name1: 'Basmati Rice', name2: 'Wheat Flour' };
let sim8Step = 0, sim8Data = { kg1: 50, g1: 200, kg2: 27, g2: 650 };
let sim12State = { vol: 260, angle: 'eye' };
let sim13Total = 0;
let sim14Total = 0;

// TTS Voice Functions
function isIndianMaleVoice(v) {
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    const female = ['female', 'zira', 'susan', 'hazel', 'geeta', 'kalpana', 'priya', 'neerja', 'heera', 'swara', 'veena', 'woman', 'girl', 'lady'];
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
    // 2. Any Indian English
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
        if (simEl) simEl.style.display = 'none';
        if (checkEl) {
            checkEl.style.display = 'block';
            renderQuizChallenge(slide.id, slide.questions || []);
        }
    }
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

// Formative Checkpoint Renderer (Slides 1 to 16)
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

function initSimulator(id) {
    switch (id) {
        case 1: sim1Select('rice'); break;
        case 2: sim2Update(1.0); break;
        case 3: sim3Calc(); break;
        case 4: sim4Compare(); break;
        case 5: sim5Reset(); break;
        case 6: sim6Reset(); break;
        case 7: sim7Preset(45, 750, 38, 650); break;
        case 8: sim8Preset(50, 200, 27, 650); break;
        case 9: sim9Scale(4); break;
        case 10: sim10Divide(); sim10Scrap(); break;
        case 11: sim11Select('glass'); break;
        case 12: sim12Update(260); break;
        case 13: sim13Reset(); break;
        case 14: sim14Reset(); break;
        case 15: sim15Select(); break;
        case 16: sim16Scenario('juice'); break;
    }
}

// Sim 1
function sim1Select(item) {
    sim1Current = item;
    const items = {
        almirah: { name: 'Steel Almirah', icon: '🚪', kg: 80, g: 80000, angle: 144, ok: true, note: '✅ Reasonable: A solid steel wardrobe typically weighs 70 to 90 kg.' },
        bed: { name: 'Wooden Bed', icon: '🛏️', kg: 40, g: 40000, angle: 72, ok: true, note: '✅ Reasonable: A single wooden cot weighs around 35 to 45 kg.' },
        rice: { name: 'Basmati Rice Sack', icon: '🌾', kg: 25, g: 25000, angle: 45, ok: true, note: '✅ Reasonable: Standard wholesale grocery bags are packed in 25 kg sacks.' },
        sofa: { name: 'Living Room Sofa', icon: '🛋️', kg: 35, g: 35000, angle: 63, ok: true, note: '✅ Reasonable: A padded 2-seater couch weighs approximately 35 kg.' },
        water: { name: 'Water Bottle (1 L)', icon: '💧', kg: 1, g: 1000, angle: 10, ok: true, note: '✅ Reasonable: 1 litre of pure drinking water has a mass of exactly 1,000 g (1 kg).' },
        bucket: { name: 'Empty Bucket', icon: '🪣', kg: 0.85, g: 850, angle: 8, ok: true, note: '✅ Reasonable: A lightweight plastic bathroom bucket is under 1 kg.' },
        fridge: { name: 'Refrigerator', icon: '🧊', kg: 60, g: 60000, angle: 108, ok: true, note: '✅ Reasonable: A family refrigerator contains heavy compressor coils, weighing ~60 kg.' },
        absurd: { name: 'Water Bottle?!', icon: '⚠️', kg: 50, g: 50000, angle: 90, ok: false, note: '❌ Completely Absurd: A school water bottle cannot weigh 50 kg (the weight of an adult)!' }
    };

    const d = items[item] || items.rice;
    const iconEl = document.getElementById('sim1_item_icon');
    if (iconEl) iconEl.innerHTML = `<text x="0" y="0" text-anchor="middle" font-size="28">${d.icon}</text>`;

    const needle = document.getElementById('sim1_needle');
    if (needle) {
        const rad = (d.angle - 90) * (Math.PI / 180);
        const x2 = 100 + 20 * Math.cos(rad);
        const y2 = 130 + 20 * Math.sin(rad);
        needle.setAttribute('x2', x2);
        needle.setAttribute('y2', y2);
    }

    const dig = document.getElementById('sim1_digital');
    if (dig) dig.textContent = `${d.kg.toFixed(2)} kg`;
    const gr = document.getElementById('sim1_grams');
    if (gr) gr.textContent = `= ${d.g.toLocaleString()} g`;

    const verd = document.getElementById('sim1_verdict');
    if (verd) {
        verd.className = d.ok ? 'p-2.5 rounded-lg bg-emerald-950/60 border border-emerald-700/60 text-[11px] text-emerald-200' : 'p-2.5 rounded-lg bg-rose-950/60 border border-rose-700/60 text-[11px] text-rose-200';
        verd.innerHTML = d.note;
    }
}

// Sim 2
function sim2Set(val) {
    const s = document.getElementById('sim2_slider');
    if (s) {
        s.value = val;
        sim2Update(val);
    }
}

function sim2Update(val) {
    const dispVal = document.getElementById('sim2_slider_val');
    if (dispVal) dispVal.textContent = `${val.toFixed(2)} kg`;

    const grams = Math.round(val * 1000);
    const disp = document.getElementById('sim2_display');
    if (disp) disp.textContent = `${val.toFixed(2)} kg = ${grams.toLocaleString()} g`;

    // Map 0 -> 40, 3 -> 420 (range 380)
    const x = 40 + (val / 3) * 380;
    const cursor = document.getElementById('sim2_cursor');
    const dt = document.getElementById('sim2_dot_top');
    const db = document.getElementById('sim2_dot_bot');

    if (cursor) {
        cursor.setAttribute('x1', x);
        cursor.setAttribute('x2', x);
    }
    if (dt) dt.setAttribute('cx', x);
    if (db) db.setAttribute('cx', x);
}

// Sim 3
function sim3Preset(kg, g) {
    const kEl = document.getElementById('sim3_kg');
    const gEl = document.getElementById('sim3_g');
    if (kEl) kEl.value = kg;
    if (gEl) gEl.value = g;
    sim3Calc();
}

function sim3Calc() {
    const kg = parseInt(document.getElementById('sim3_kg')?.value || '0', 10);
    const g = parseInt(document.getElementById('sim3_g')?.value || '0', 10);

    const s1 = document.getElementById('sim3_step1');
    const s2 = document.getElementById('sim3_step2');
    const tot = document.getElementById('sim3_total');
    const warn = document.getElementById('sim3_warning');

    const kgInG = kg * 1000;
    const padG = g.toString().padStart(3, '0');
    const totalG = kgInG + g;

    if (s1) s1.textContent = `${kg} × 1,000 = ${kgInG.toLocaleString()} g`;
    if (s2) s2.textContent = `+ ${padG} g`;
    if (tot) tot.textContent = `${totalG.toLocaleString()} g`;

    if (warn) {
        if (g < 100) {
            warn.className = 'p-2 rounded-lg bg-amber-950/50 border border-amber-700/50 text-[11px] text-amber-200 leading-tight';
            warn.innerHTML = `⚠️ <strong>Leading Zero Alert:</strong> ${g} g has no hundreds, so write as <strong>${padG}</strong>. Total is ${totalG.toLocaleString()} g!`;
        } else {
            warn.className = 'p-2 rounded-lg bg-emerald-950/50 border border-emerald-700/50 text-[11px] text-emerald-200 leading-tight';
            warn.innerHTML = `✅ <strong>Correct Format:</strong> ${kg} kg + ${g} g = ${totalG.toLocaleString()} g.`;
        }
    }
}

// Sim 4
function sim4Compare() {
    const lVal = parseInt(document.getElementById('sim4_left')?.value || '3200', 10);
    const rVal = parseInt(document.getElementById('sim4_right')?.value || '2500', 10);

    const icons = { 3200: '🍉', 2500: '🍎', 1800: '🍍', 1250: '🥭' };
    const il = document.getElementById('sim4_icon_l');
    const ir = document.getElementById('sim4_icon_r');
    if (il) il.textContent = icons[lVal] || '🍉';
    if (ir) ir.textContent = icons[rVal] || '🍎';

    const beam = document.getElementById('sim4_beam');
    let deg = 0;
    if (lVal > rVal) deg = -7;
    else if (lVal < rVal) deg = 7;
    if (beam) beam.setAttribute('transform', `rotate(${deg}, 140, 70)`);

    const stat = document.getElementById('sim4_statement');
    if (stat) {
        if (lVal > rVal) {
            stat.className = 'p-2 rounded bg-slate-950 font-mono text-center font-bold text-xs text-amber-300 w-full mt-1';
            stat.textContent = `${lVal.toLocaleString()} g > ${rVal.toLocaleString()} g (Left is heavier by ${(lVal - rVal).toLocaleString()} g)`;
        } else if (lVal < rVal) {
            stat.className = 'p-2 rounded bg-slate-950 font-mono text-center font-bold text-xs text-cyan-300 w-full mt-1';
            stat.textContent = `${lVal.toLocaleString()} g < ${rVal.toLocaleString()} g (Right is heavier by ${(rVal - lVal).toLocaleString()} g)`;
        } else {
            stat.className = 'p-2 rounded bg-slate-950 font-mono text-center font-bold text-xs text-emerald-400 w-full mt-1';
            stat.textContent = `${lVal.toLocaleString()} g = ${rVal.toLocaleString()} g (Both pans are balanced!)`;
        }
    }
}

// Sim 5
function sim5Toggle(id) {
    const items = {
        1: { name: 'Ant', mg: 5 },
        2: { name: 'Salt', mg: 1 },
        3: { name: 'Pill', mg: 500 },
        4: { name: 'Feather', mg: 15 },
        5: { name: 'Ring', mg: 4000 },
        6: { name: 'Sugar', mg: 5000 }
    };

    sim5Items[id] = !sim5Items[id];
    const btn = document.getElementById(`sim5_b${id}`);
    if (btn) {
        if (sim5Items[id]) {
            btn.classList.add('bg-emerald-800', 'border-emerald-500', 'font-bold');
        } else {
            btn.classList.remove('bg-emerald-800', 'border-emerald-500', 'font-bold');
        }
    }

    let totMg = 0;
    let listNames = [];
    Object.keys(sim5Items).forEach(k => {
        if (sim5Items[k]) {
            totMg += items[k].mg;
            listNames.push(items[k].name);
        }
    });

    const dMg = document.getElementById('sim5_display_mg');
    const dG = document.getElementById('sim5_display_g');
    const notes = document.getElementById('sim5_notes');

    if (dMg) dMg.textContent = `${totMg.toLocaleString()} mg`;
    if (dG) dG.textContent = `= ${(totMg / 1000).toFixed(3)} g`;

    if (notes) {
        if (listNames.length === 0) {
            notes.textContent = 'Pan is empty. Click any item above to weigh it on the micro-scale!';
        } else {
            notes.textContent = `Weighing: ${listNames.join(', ')} (Total: ${totMg} mg).`;
        }
    }
}

function sim5Reset() {
    sim5Items = {};
    for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`sim5_b${i}`);
        if (btn) btn.classList.remove('bg-emerald-800', 'border-emerald-500', 'font-bold');
    }
    const dMg = document.getElementById('sim5_display_mg');
    const dG = document.getElementById('sim5_display_g');
    const notes = document.getElementById('sim5_notes');
    if (dMg) dMg.textContent = '0 mg';
    if (dG) dG.textContent = '= 0.000 g';
    if (notes) notes.textContent = 'Pan is empty. Click any item above to weigh it on the micro-scale!';
}

// Sim 6
function sim6ToggleElephant() {
    sim6State.elephant = !sim6State.elephant;
    const btn = document.getElementById('sim6_btn_ele');
    const cargo = document.getElementById('sim6_cargo_icon');
    const boat = document.getElementById('sim6_boat');

    if (sim6State.elephant) {
        if (btn) btn.textContent = 'Remove Elephant';
        if (cargo) cargo.textContent = '🐘';
        if (boat) boat.setAttribute('transform', 'translate(0, 15)');
        sim6UpdateReadouts(4000);
    } else {
        if (btn) btn.textContent = 'Load Elephant';
        if (cargo) cargo.textContent = sim6State.stones > 0 ? '🪨' : '⛵';
        const sink = Math.min(15, (sim6State.stones * 50 / 4000) * 15);
        if (boat) boat.setAttribute('transform', `translate(0, ${sink})`);
        sim6UpdateReadouts(sim6State.stones * 50);
    }
}

function sim6AddStones(n) {
    if (sim6State.elephant) {
        sim6ToggleElephant();
    }
    sim6State.stones += n;
    const cargo = document.getElementById('sim6_cargo_icon');
    if (cargo) cargo.textContent = '🪨';

    const totKg = sim6State.stones * 50;
    const sink = Math.min(15, (totKg / 4000) * 15);
    const boat = document.getElementById('sim6_boat');
    if (boat) boat.setAttribute('transform', `translate(0, ${sink})`);

    sim6UpdateReadouts(totKg);
}

function sim6UpdateReadouts(kg) {
    const elKg = document.getElementById('sim6_kg');
    const elQ = document.getElementById('sim6_q');
    const elT = document.getElementById('sim6_t');

    if (elKg) elKg.textContent = `${kg.toLocaleString()} kg`;
    if (elQ) elQ.textContent = `${(kg / 100).toFixed(1)} q`;
    if (elT) elT.textContent = `${(kg / 1000).toFixed(2)} t`;
}

function sim6Reset() {
    sim6State = { elephant: false, stones: 0 };
    const btn = document.getElementById('sim6_btn_ele');
    if (btn) btn.textContent = 'Load Elephant';
    const cargo = document.getElementById('sim6_cargo_icon');
    if (cargo) cargo.textContent = '⛵';
    const boat = document.getElementById('sim6_boat');
    if (boat) boat.setAttribute('transform', 'translate(0, 0)');
    sim6UpdateReadouts(0);
}

// Sim 7
function sim7Preset(kg1, g1, kg2, g2) {
    sim7Step = 0;
    sim7Data = { kg1, g1, kg2, g2, name1: (kg1 === 45 ? 'Basmati Rice' : 'Potatoes'), name2: (kg1 === 45 ? 'Wheat Flour' : 'Potatoes Evg') };

    document.getElementById('sim7_name1').textContent = sim7Data.name1;
    document.getElementById('sim7_name2').textContent = sim7Data.name2;
    document.getElementById('sim7_kg1').textContent = kg1;
    document.getElementById('sim7_g1').textContent = g1;
    document.getElementById('sim7_kg2').textContent = kg2;
    document.getElementById('sim7_g2').textContent = g2;

    document.getElementById('sim7_carry_kg').textContent = '-';
    document.getElementById('sim7_tot_kg').textContent = '-';
    document.getElementById('sim7_tot_g').textContent = '-';
    document.getElementById('sim7_expl').textContent = "Click 'Execute Next Step' to start adding grams first!";
}

function sim7NextStep() {
    sim7Step++;
    const gSum = sim7Data.g1 + sim7Data.g2;
    const carry = Math.floor(gSum / 1000);
    const gRem = gSum % 1000;
    const kgSum = sim7Data.kg1 + sim7Data.kg2 + carry;

    if (sim7Step === 1) {
        document.getElementById('sim7_tot_g').textContent = gRem.toString().padStart(3, '0');
        if (carry > 0) {
            document.getElementById('sim7_carry_kg').textContent = `(+${carry})`;
            document.getElementById('sim7_expl').innerHTML = `<strong>Step 1 (Grams):</strong> ${sim7Data.g1} + ${sim7Data.g2} = ${gSum} g. Regroup: ${carry * 1000} g = ${carry} kg carry-over. ${gRem} g remains.`;
        } else {
            document.getElementById('sim7_expl').innerHTML = `<strong>Step 1 (Grams):</strong> ${sim7Data.g1} + ${sim7Data.g2} = ${gSum} g. No regrouping needed.`;
        }
    } else if (sim7Step >= 2) {
        document.getElementById('sim7_tot_kg').textContent = `${kgSum} kg`;
        document.getElementById('sim7_expl').innerHTML = `<strong>Step 2 (Kilograms):</strong> ${sim7Data.kg1} + ${sim7Data.kg2} + ${carry} (carry) = <strong>${kgSum} kg</strong>. Final Total: <strong>${kgSum} kg ${gRem} g</strong>!`;
        sim7Step = 0;
    }
}

// Sim 8
function sim8Preset(kg1, g1, kg2, g2) {
    sim8Step = 0;
    sim8Data = { kg1, g1, kg2, g2 };

    document.getElementById('sim8_kg1').textContent = kg1;
    document.getElementById('sim8_g1').textContent = g1;
    document.getElementById('sim8_kg2').textContent = `- ${kg2}`;
    document.getElementById('sim8_g2').textContent = `- ${g2}`;

    document.getElementById('sim8_borrow_kg').textContent = '-';
    document.getElementById('sim8_borrow_g').textContent = '-';
    document.getElementById('sim8_tot_kg').textContent = '-';
    document.getElementById('sim8_tot_g').textContent = '-';
    document.getElementById('sim8_expl').textContent = "Click 'Execute Next Step' to see 1 kg borrowed and converted to +1,000 g!";
}

function sim8NextStep() {
    sim8Step++;
    const needBorrow = sim8Data.g1 < sim8Data.g2;
    const bKg = needBorrow ? sim8Data.kg1 - 1 : sim8Data.kg1;
    const bG = needBorrow ? sim8Data.g1 + 1000 : sim8Data.g1;
    const gDiff = bG - sim8Data.g2;
    const kgDiff = bKg - sim8Data.kg2;

    if (sim8Step === 1) {
        if (needBorrow) {
            document.getElementById('sim8_borrow_kg').textContent = bKg;
            document.getElementById('sim8_borrow_g').textContent = `(${bG})`;
            document.getElementById('sim8_expl').innerHTML = `<strong>Step 1 (Borrowing):</strong> Cannot subtract ${sim8Data.g2} from ${sim8Data.g1}. Borrow 1 kg (1,000 g) from ${sim8Data.kg1} kg ➔ ${bKg} kg and ${sim8Data.g1} + 1,000 = <strong>${bG} g</strong>.`;
        } else {
            document.getElementById('sim8_expl').innerHTML = `<strong>Step 1:</strong> ${sim8Data.g1} ≥ ${sim8Data.g2}, so no borrowing required.`;
        }
    } else if (sim8Step >= 2) {
        document.getElementById('sim8_tot_g').textContent = `${gDiff} g`;
        document.getElementById('sim8_tot_kg').textContent = `${kgDiff} kg`;
        document.getElementById('sim8_expl').innerHTML = `<strong>Step 2 (Subtraction):</strong> Grams: ${bG} - ${sim8Data.g2} = ${gDiff} g. Kilograms: ${bKg} - ${sim8Data.kg2} = ${kgDiff} kg. Result = <strong>${kgDiff} kg ${gDiff} g</strong>!`;
        sim8Step = 0;
    }
}

// Sim 9
function sim9Scale(n) {
    const btns = document.querySelectorAll('.sim9-btn');
    btns.forEach((b, idx) => {
        if (idx + 1 === n) {
            b.className = 'sim9-btn flex-1 py-1 rounded bg-cyan-700 font-bold text-slate-950 border border-cyan-600';
        } else {
            b.className = 'sim9-btn flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700';
        }
    });

    const kgPart = n * 2;
    const gPart = n * 350;
    const carry = Math.floor(gPart / 1000);
    const gRem = gPart % 1000;
    const totKg = kgPart + carry;

    const totalGrams = n * 2350;

    document.getElementById('sim9_m1_kg').textContent = `${n} × 2 kg = ${kgPart} kg`;
    document.getElementById('sim9_m1_g').textContent = `${n} × 350 g = ${gPart.toLocaleString()} g`;
    document.getElementById('sim9_m2_calc').textContent = `2,350 g × ${n} = ${totalGrams.toLocaleString()} g`;
    document.getElementById('sim9_final').textContent = `${totKg} kg ${gRem} g`;
}

// Sim 10
function sim10Divide() {
    const parts = parseInt(document.getElementById('sim10_parts')?.value || '6', 10);
    const perG = Math.round(7500 / parts);
    const kg = Math.floor(perG / 1000);
    const g = perG % 1000;

    document.getElementById('sim10_res_div').textContent = `${perG.toLocaleString()} g per packet`;
    document.getElementById('sim10_res_unit').textContent = `${kg} kg ${g} g`;
}

function sim10Scrap() {
    const rate = parseInt(document.getElementById('sim10_scrap')?.value || '28', 10);
    const kg = parseInt(document.getElementById('sim10_kg_slider')?.value || '5', 10);

    const valEl = document.getElementById('sim10_kg_val');
    if (valEl) valEl.textContent = `${kg} kg`;

    const cash = kg * rate;
    const cashEl = document.getElementById('sim10_cash');
    if (cashEl) cashEl.textContent = `${kg} kg × ₹${rate} = ₹${cash.toLocaleString()}`;
}

// Sim 11
function sim11Select(item) {
    const data = {
        spoon: { icon: '🥄', name: 'Medicine Spoon', cap: '5 mL', bar: '1%', rel: '200 spoons make 1 litre (1,000 mL).' },
        cup: { icon: '☕', name: 'Chai Tea Cup', cap: '150 mL', bar: '15%', rel: 'About 6.6 cups make 1 litre.' },
        glass: { icon: '🥛', name: 'Standard Drinking Glass', cap: '250 mL (1/4 Litre)', bar: '25%', rel: '4 glasses make exactly 1 full litre (1,000 mL).' },
        carton: { icon: '🧃', name: 'Juice Tetra-Pack', cap: '1,000 mL (1 Litre)', bar: '100%', rel: '1 litre equals exactly 1,000 millilitres.' },
        bucket: { icon: '🪣', name: 'Bath Bucket', cap: '18 Litres', bar: '100%', rel: '18 litres = 18,000 millilitres (72 glasses of water).' },
        tank: { icon: '🏠', name: 'Rooftop Storage Tank', cap: '750 Litres', bar: '100%', rel: '750 litres = 750,000 millilitres (fills 41 buckets).' }
    };

    const d = data[item] || data.glass;
    document.getElementById('sim11_icon').textContent = d.icon;
    document.getElementById('sim11_name').textContent = d.name;
    document.getElementById('sim11_cap').textContent = d.cap;
    document.getElementById('sim11_bar').style.width = d.bar;
    document.getElementById('sim11_rel').textContent = d.rel;
}

// Sim 12
function sim12Angle(mode) {
    sim12State.angle = mode;
    sim12Update(sim12State.vol);
}

function sim12Update(val) {
    sim12State.vol = val;
    document.getElementById('sim12_val').textContent = `${val} mL`;

    // Map 0 to 500 mL -> y from 110 to 10 (height 100)
    const yTop = 110 - (val / 500) * 100;
    const h = 118 - yTop;

    const liq = document.getElementById('sim12_liquid');
    const men = document.getElementById('sim12_meniscus');
    const eye = document.getElementById('sim12_eye_icon');

    if (liq) {
        liq.setAttribute('y', yTop);
        liq.setAttribute('height', h);
    }
    if (men) {
        men.setAttribute('d', `M 27 ${yTop} Q 50 ${yTop + 4} 73 ${yTop}`);
    }

    let eyeY = yTop + 4;
    let reading = val;
    let note = '';

    if (sim12State.angle === 'high') {
        eyeY = yTop - 15;
        reading = val + 15;
        note = 'Looking down from above causes parallax: apparent level looks higher (~' + reading + ' mL).';
    } else if (sim12State.angle === 'low') {
        eyeY = yTop + 18;
        reading = val - 15;
        note = 'Looking up from below causes parallax: apparent level looks lower (~' + reading + ' mL).';
    } else {
        note = 'Eye aligned horizontally with the bottom of the meniscus: zero parallax error!';
    }

    if (eye) eye.setAttribute('y', eyeY);

    const rEl = document.getElementById('sim12_reading');
    const nEl = document.getElementById('sim12_note');
    if (rEl) {
        rEl.textContent = `${reading} mL ${sim12State.angle === 'eye' ? '(Accurate)' : '(Parallax Error)'}`;
        rEl.className = sim12State.angle === 'eye' ? 'text-base font-bold text-emerald-400' : 'text-base font-bold text-rose-400';
    }
    if (nEl) nEl.textContent = note;
}

// Sim 13
function sim13Add(ml) {
    sim13Total += ml;
    const l = Math.floor(sim13Total / 1000);
    const remMl = sim13Total % 1000;

    document.getElementById('sim13_tot_ml').textContent = `${sim13Total.toLocaleString()} mL`;
    document.getElementById('sim13_tot_l').textContent = `= ${l} L ${remMl} mL`;
    document.getElementById('sim13_breakdown').textContent = `Khayal chacha poured: ${l} whole litre(s) and ${remMl} mL into the milk can.`;
}

function sim13Reset() {
    sim13Total = 0;
    document.getElementById('sim13_tot_ml').textContent = '0 mL';
    document.getElementById('sim13_tot_l').textContent = '= 0 L 0 mL';
    document.getElementById('sim13_breakdown').textContent = 'Click ladles above to measure milk for a customer order!';
}

// Sim 14
function sim14Add(ml) {
    sim14Total = Math.min(3000, sim14Total + ml);
    const pct = Math.min(100, (sim14Total / 2500) * 100);

    const txt = document.getElementById('sim14_text');
    const bar = document.getElementById('sim14_bar');
    const msg = document.getElementById('sim14_msg');
    const status = document.getElementById('sim14_goal_status');

    if (txt) txt.textContent = `${sim14Total} / 2,500 mL (${(sim14Total / 1000).toFixed(2)} L)`;
    if (bar) bar.style.width = `${pct}%`;

    if (sim14Total >= 2500) {
        if (status) {
            status.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            status.textContent = 'Goal Met! 🎉';
        }
        if (msg) msg.textContent = `Aarav reached ${sim14Total} mL! Daily hydration requirement of 2.5 L is successfully fulfilled.`;
    } else {
        if (status) {
            status.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
            status.textContent = 'In Progress';
        }
        if (msg) msg.textContent = `Aarav drank ${sim14Total} mL. He needs ${(2500 - sim14Total)} mL more to meet his daily goal.`;
    }
}

function sim14Reset() {
    sim14Total = 0;
    document.getElementById('sim14_text').textContent = '0 / 2,500 mL (0.00 L)';
    document.getElementById('sim14_bar').style.width = '0%';
    document.getElementById('sim14_goal_status').className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
    document.getElementById('sim14_goal_status').textContent = 'In Progress';
    document.getElementById('sim14_msg').textContent = "Aarav hasn't started drinking water yet today. Click an activity above!";
}

// Sim 15
function sim15Select() {
    const tank = parseFloat(document.getElementById('sim15_veh')?.value || '45');
    const currInput = document.getElementById('sim15_curr');
    if (currInput) {
        currInput.max = tank;
        currInput.value = (tank * 0.3).toFixed(1);
    }
    sim15Calc();
}

function sim15Calc() {
    const tank = parseFloat(document.getElementById('sim15_veh')?.value || '45');
    let curr = parseFloat(document.getElementById('sim15_curr')?.value || '0');
    if (curr > tank) curr = tank;

    const needed = tank - curr;
    const l = Math.floor(needed);
    const ml = Math.round((needed - l) * 1000);
    const cost = Math.round(needed * 96);

    const nEl = document.getElementById('sim15_needed');
    const cEl = document.getElementById('sim15_cost');
    const eEl = document.getElementById('sim15_expl');

    if (nEl) nEl.textContent = `${l} L ${ml} mL`;
    if (cEl) cEl.textContent = `₹${cost.toLocaleString()}`;
    if (eEl) eEl.textContent = `Tank Capacity: ${tank} L - Current: ${curr} L = ${l} L ${ml} mL needed to fill.`;
}

// Sim 16
function sim16Scenario(type) {
    if (type === 'juice') {
        document.getElementById('sim16_step1').textContent = '10 L = 10,000 mL';
        document.getElementById('sim16_step2').textContent = '10,000 ÷ 200 = 50 Cups';
        document.getElementById('sim16_step3').textContent = '50 × ₹15 = ₹750';
        document.getElementById('sim16_note').textContent = '10 L divided into 200 mL cups yields 50 cups. Selling at ₹15 per cup earns ₹750.';
    } else {
        document.getElementById('sim16_step1').textContent = '15 L = 15,000 mL';
        document.getElementById('sim16_step2').textContent = '15,000 ÷ 750 = 20 Bottles';
        document.getElementById('sim16_step3').textContent = '20 × ₹130 = ₹2,600';
        document.getElementById('sim16_note').textContent = '15 L divided into 750 mL bottles yields 20 bottles. Selling at ₹130 per bottle earns ₹2,600.';
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


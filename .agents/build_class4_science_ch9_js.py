# -*- coding: utf-8 -*-
"""
Build Class 4 Science Chapter 9 JavaScript Engine
Generates .agents/class4_science_ch9_js.js and .agents/class4_science_ch9_js.py
Equipped with Pure Indian Male Teacher Sound Engine (Speaking All Text).
"""

import os

js_code = r'''
// =========================================================================
// PURE INDIAN MALE TEACHER SOUND ENGINE & SLIDE ORCHESTRATION
// NCERT Class 4 Science - Chapter 9: Different Lands, Different Lives
// =========================================================================

let currentSlide = 1;
const totalSlides = 20;
let isAudioPlaying = false;
let currentUtterance = null;
let synth = window.speechSynthesis;
let selectedVoice = null;
let allVoices = [];

// Audio Context for Chimes & Acoustics
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

// Live High/Low Feedback Chimes
function playSuccessChime() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc1 = ctx.createOscillator();
        const osc2 = ctx.createOscillator();
        const gain = ctx.createGain();

        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(523.25, now); // C5
        osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.15); // E5

        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(659.25, now);
        osc2.frequency.exponentialRampToValueAtTime(783.99, now + 0.15); // G5

        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(ctx.destination);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.35);
        osc2.stop(now + 0.35);
    } catch(e) {
        console.warn("Audio chime unsupported:", e);
    }
}

function playErrorChime() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now); // A3
        osc.frequency.exponentialRampToValueAtTime(146.83, now + 0.25); // D3

        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.3);
    } catch(e) {
        console.warn("Audio chime unsupported:", e);
    }
}

function playAcousticWoodClick() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'square';
        osc.frequency.setValueAtTime(800, now);
        osc.frequency.exponentialRampToValueAtTime(120, now + 0.06);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.08);
    } catch(e) {
        console.warn("Wood click unsupported:", e);
    }
}

// Voice Filtering & Selection
const femaleBlockList = [
    'female', 'woman', 'girl', 'zira', 'kavya', 'kalpana', 'veena',
    'siri', 'samantha', 'victoria', 'karen', 'moira', 'tessa', 'fiona',
    'helena', 'catherine', 'monica', 'paulina', 'lucia', 'sara', 'anna'
];

function isIndianMaleVoice(v) {
    const name = v.name.toLowerCase();
    const lang = v.lang.toLowerCase();

    for (let f of femaleBlockList) {
        if (name.includes(f)) return false;
    }

    const indianMaleKeywords = ['prabhat', 'rishi', 'ravi', 'madhav', 'hemant', 'amit', 'neerja', 'ahp', 'cxx'];
    for (let k of indianMaleKeywords) {
        if (name.includes(k)) return true;
    }

    if (lang.includes('en-in') || lang.includes('hi-in') || lang.includes('ta-in') || lang.includes('mr-in')) {
        return !name.includes('female');
    }

    return false;
}

function initSpeechEngine() {
    if (!synth) return;

    function populateVoices() {
        allVoices = synth.getVoices();
        const voiceSelect = document.getElementById('voiceSelect');
        if (!voiceSelect) return;

        voiceSelect.innerHTML = '';
        let indianMaleVoices = [];
        let otherMaleVoices = [];

        allVoices.forEach((v, index) => {
            const nameLower = v.name.toLowerCase();
            let isFemale = femaleBlockList.some(f => nameLower.includes(f));
            if (isFemale) return;

            if (isIndianMaleVoice(v)) {
                indianMaleVoices.push({ voice: v, index: index });
            } else if (nameLower.includes('male') || nameLower.includes('david') || nameLower.includes('george')) {
                otherMaleVoices.push({ voice: v, index: index });
            }
        });

        const sortedCandidates = [...indianMaleVoices, ...otherMaleVoices];

        if (sortedCandidates.length === 0) {
            allVoices.forEach((v, index) => {
                if (!femaleBlockList.some(f => v.name.toLowerCase().includes(f))) {
                    sortedCandidates.push({ voice: v, index: index });
                }
            });
        }

        sortedCandidates.forEach(item => {
            const opt = document.createElement('option');
            opt.value = item.index;
            opt.textContent = `${item.voice.name} (${item.voice.lang})${isIndianMaleVoice(item.voice) ? ' 🇮🇳 Pure Indian Male' : ' 👨 Male'}`;
            voiceSelect.appendChild(opt);
        });

        if (sortedCandidates.length > 0) {
            selectedVoice = sortedCandidates[0].voice;
            voiceSelect.value = sortedCandidates[0].index;
        }
    }

    populateVoices();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populateVoices;
    }
}

function onVoiceChange() {
    const voiceSelect = document.getElementById('voiceSelect');
    if (!voiceSelect || !allVoices) return;
    const idx = parseInt(voiceSelect.value);
    if (!isNaN(idx) && allVoices[idx]) {
        selectedVoice = allVoices[idx];
        if (isAudioPlaying) {
            speakLecture();
        }
    }
}

function toggleAudio() {
    if (isAudioPlaying) {
        stopSpeaking();
    } else {
        speakLecture();
    }
}

function stopSpeaking() {
    if (synth) {
        synth.cancel();
    }
    isAudioPlaying = false;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    const icon = document.getElementById('audioPlayIcon');
    const label = document.getElementById('audioButtonText');
    if (!btn || !icon || !label) return;

    if (playing) {
        btn.classList.remove('bg-cyan-600', 'hover:bg-cyan-500');
        btn.classList.add('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        icon.textContent = '⏹️';
        label.textContent = 'Pause Lecture';
    } else {
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        btn.classList.add('bg-cyan-600', 'hover:bg-cyan-500');
        icon.textContent = '🔊';
        label.textContent = 'Teacher Sound Lecture';
    }
}

function speakLecture() {
    if (!synth) return;
    stopSpeaking();

    const currentSlideData = window.slideCurriculumData.find(s => s.id === currentSlide);
    if (!currentSlideData || !currentSlideData.speech) return;

    const speechText = currentSlideData.speech;
    currentUtterance = new SpeechSynthesisUtterance(speechText);

    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
    }
    currentUtterance.rate = 0.90;
    currentUtterance.pitch = 0.88;

    currentUtterance.onstart = () => {
        isAudioPlaying = true;
        updateAudioButtonUI(true);
    };

    currentUtterance.onend = () => {
        isAudioPlaying = false;
        updateAudioButtonUI(false);
    };

    currentUtterance.onerror = (e) => {
        console.warn("Speech synthesis error:", e);
        isAudioPlaying = false;
        updateAudioButtonUI(false);
    };

    synth.speak(currentUtterance);
}

function speakText(text) {
    if (!synth) return;
    synth.cancel();

    const u = new SpeechSynthesisUtterance(text);
    if (selectedVoice) {
        u.voice = selectedVoice;
    }
    u.rate = 0.90;
    u.pitch = 0.88;
    synth.speak(u);
}

// Slide Navigation
function showSlide(n) {
    stopSpeaking();

    if (n < 1) n = 1;
    if (n > totalSlides) n = totalSlides;
    currentSlide = n;

    for (let i = 1; i <= totalSlides; i++) {
        const slideEl = document.getElementById(`slide-${i}`);
        if (slideEl) {
            if (i === currentSlide) {
                slideEl.classList.remove('hidden');
            } else {
                slideEl.classList.add('hidden');
            }
        }
    }

    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${currentSlide} / ${totalSlides}`;

    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
        const pct = (currentSlide / totalSlides) * 100;
        progressBar.style.width = `${pct}%`;
    }

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    const audioControls = document.getElementById('audioControls');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }

    // Terminal Invariant on Slide 20
    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    // Hide auto-speech bar on challenge quiz slides (17-20)
    if (currentSlide >= 17) {
        if (audioControls) audioControls.classList.add('opacity-0', 'pointer-events-none');
    } else {
        if (audioControls) audioControls.classList.remove('opacity-0', 'pointer-events-none');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        showSlide(currentSlide - 1);
    }
}

// In-slide Concept Checkpoint Handler
function checkAnswer(slideId, cpIdx, optIdx, correctAns) {
    const card = document.getElementById(`cp-${slideId}-${cpIdx}`);
    if (!card) return;

    const buttons = card.querySelectorAll('.checkpoint-opt-btn');
    const feedbackBox = document.getElementById(`fb-${slideId}-${cpIdx}`);

    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        const optVal = btn.getAttribute('data-opt-val');
        if (optVal === correctAns) {
            btn.classList.remove('bg-slate-900', 'border-slate-800');
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === optIdx && optVal !== correctAns) {
            btn.classList.remove('bg-slate-900', 'border-slate-800');
            btn.classList.add('bg-red-600/30', 'border-red-500', 'text-red-200');
        }
    });

    const isCorrect = buttons[optIdx].getAttribute('data-opt-val') === correctAns;
    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        const expl = feedbackBox.getAttribute('data-explanation') || '';
        if (isCorrect) {
            playSuccessChime();
            feedbackBox.className = 'mt-3 p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-xs text-emerald-300';
            feedbackBox.innerHTML = `<b>✓ Correct!</b> ${expl}`;
        } else {
            playErrorChime();
            feedbackBox.className = 'mt-3 p-3 rounded-xl bg-red-500/10 border border-red-500/30 text-xs text-red-300';
            feedbackBox.innerHTML = `<b>✗ Re-examine Concept:</b> ${expl}`;
        }
    }
}

// Challenge Quiz Answer Handler (Slides 17-20)
function checkQuizAnswer(qid, selectedOpt, correctAns) {
    const container = document.getElementById(`quiz-q-${qid}`);
    if (!container) return;

    const buttons = container.querySelectorAll('.quiz-opt-btn');
    const fbBox = document.getElementById(`quiz-fb-${qid}`);

    buttons.forEach(btn => {
        btn.disabled = true;
        const val = btn.getAttribute('data-opt-val');
        if (val === correctAns) {
            btn.classList.remove('bg-slate-900', 'border-slate-800');
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500', 'text-emerald-200');
        } else if (val === selectedOpt && val !== correctAns) {
            btn.classList.remove('bg-slate-900', 'border-slate-800');
            btn.classList.add('bg-red-600/30', 'border-red-500', 'text-red-200');
        }
    });

    if (fbBox) {
        fbBox.classList.remove('hidden');
        const expl = fbBox.getAttribute('data-explanation') || '';
        if (selectedOpt === correctAns) {
            playSuccessChime();
            fbBox.className = 'mt-2 p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-xs text-emerald-300';
            fbBox.innerHTML = `<b>✓ Correct!</b> ${expl}`;
        } else {
            playErrorChime();
            fbBox.className = 'mt-2 p-2.5 rounded-xl bg-red-500/10 border border-red-500/30 text-xs text-red-300';
            fbBox.innerHTML = `<b>✗ Not Quite:</b> ${expl}`;
        }
    }
}

// 3-Step Scientific Solution Modal
function showSolutionModal(qid) {
    let questionObj = null;
    for (let s of window.slideCurriculumData) {
        if (s.questions) {
            const found = s.questions.find(q => q.id === qid);
            if (found) {
                questionObj = found;
                break;
            }
        }
    }

    if (!questionObj) return;

    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const contentEl = document.getElementById('modalContent');
    if (!modal || !titleEl || !contentEl) return;

    titleEl.textContent = `Scientific Solution Walkthrough: ${questionObj.q}`;
    
    let stepsHtml = questionObj.solution_steps.map((step, idx) => `
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 flex items-start gap-3">
            <span class="w-6 h-6 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs shrink-0">${idx + 1}</span>
            <p class="text-xs text-slate-300 leading-relaxed">${step}</p>
        </div>
    `).join('');

    contentEl.innerHTML = `
        <div class="space-y-3">
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-xs text-emerald-300 font-semibold">
                Correct Answer: <b>${questionObj.ans}</b>
            </div>
            <div class="space-y-2">
                ${stepsHtml}
            </div>
        </div>
    `;

    modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// =========================================================================
// BESPOKE SIMULATOR INTERACTIVE CONTROLLERS (Simulators 1 to 16)
// =========================================================================

// Simulator 1: Diverse Indian Landforms
const landformData = {
    plains: {
        title: "🌾 Northern Agricultural Plains",
        badge: "Punjab Basin",
        desc: "Expansive flat lowlands formed by Himalayan river silt deposits. Ideal for intensive farming of wheat and rice with extensive canal networks.",
        soil: "Very High (Alluvial)",
        soilPct: "95%",
        rain: "Moderate (650 mm)",
        rainPct: "60%",
        flat: "Level Flatland (180 m)",
        flatPct: "90%",
        adapt: "Tractor-plowed large fields, draft cattle, canal irrigation networks, and wheat granaries."
    },
    desert: {
        title: "🏜️ Thar Desert",
        badge: "Western Arid Zone",
        desc: "Extreme arid environment with rolling sand dunes, intense daytime heat, scarce rainfall, and dramatic diurnal temperature shifts.",
        soil: "Coarse Sandy Dunes",
        soilPct: "20%",
        rain: "Extremely Scarce (<150 mm)",
        rainPct: "15%",
        flat: "Shifting Dunes (150-300 m)",
        flatPct: "50%",
        adapt: "Underground rainwater tankas, padded-foot camels, multi-fold cotton turbans, and thick mud houses."
    },
    coast: {
        title: "🏖️ Puri Coastal Seashore",
        badge: "Bay of Bengal Shore",
        desc: "Dynamic marine boundary characterized by rhythmic ocean tides, saline breezes, golden sand beaches, and frequent tropical cyclones.",
        soil: "Saline Beach Sand & Silt",
        soilPct: "45%",
        rain: "Heavy Monsoon (1,400 mm)",
        rainPct: "85%",
        flat: "Sea Level (0-15 m)",
        flatPct: "95%",
        adapt: "Artisanal catamaran fishing, deep palm tree roots stabilizing dunes, and elevated cyclone shelters."
    },
    mountains: {
        title: "🏔️ Eastern Himalayas (Sikkim)",
        badge: "Highland Alpine Zone",
        desc: "Rugged vertical relief featuring snow-clad peaks including Mount Kangchenjunga (8,586 m), steep river gorges, and alpine forests.",
        soil: "Rocky Thin Hill Soil",
        soilPct: "35%",
        rain: "High Precipitation (2,500 mm)",
        rainPct: "95%",
        flat: "Steep Slopes (1,500-8,586 m)",
        flatPct: "10%",
        adapt: "Stepped hillside terrace farming, warm woollen bakhus, domestic yaks, and steeply pitched wooden roofs."
    }
};

function selectLandform(type) {
    const data = landformData[type];
    if (!data) return;

    document.getElementById('lfDetailTitle').textContent = data.title;
    document.getElementById('lfDetailBadge').textContent = data.badge;
    document.getElementById('lfDetailDesc').textContent = data.desc;
    document.getElementById('lfSoilVal').textContent = data.soil;
    document.getElementById('lfSoilBar').style.width = data.soilPct;
    document.getElementById('lfRainVal').textContent = data.rain;
    document.getElementById('lfRainBar').style.width = data.rainPct;
    document.getElementById('lfFlatVal').textContent = data.flat;
    document.getElementById('lfFlatBar').style.width = data.flatPct;
    document.getElementById('lfAdaptText').textContent = data.adapt;

    // Highlight button
    document.querySelectorAll('.landform-btn').forEach(btn => {
        btn.classList.remove('ring-2', 'ring-white');
    });
    const activeBtn = document.getElementById(`lf-btn-${type}`);
    if (activeBtn) activeBtn.classList.add('ring-2', 'ring-white');

    playSuccessChime();
}

// Simulator 2: Fertile Agricultural Plains
let tractorX = 60;
function drivePlainsTractor() {
    const tractor = document.getElementById('tractorSvgGroup');
    if (!tractor) return;
    tractorX = (tractorX + 60) % 360;
    tractor.setAttribute('transform', `translate(${tractorX}, 135)`);
    playAcousticWoodClick();
}

function setPlainsSeason(season) {
    const statusText = document.getElementById('plainsStatusText');
    const cropName = document.getElementById('plainsCropName');
    const btnRabi = document.getElementById('btnPlainsRabi');
    const btnKharif = document.getElementById('btnPlainsKharif');

    if (season === 'rabi') {
        btnRabi.className = 'px-3 py-1 rounded-xl bg-amber-500 text-slate-950 text-xs font-bold transition';
        btnKharif.className = 'px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white text-xs font-bold transition';
        if (statusText) statusText.textContent = "🌾 Active Season: Rabi (Winter Wheat & Mustard)";
        if (cropName) cropName.textContent = "Golden Wheat (Kanak)";
    } else {
        btnKharif.className = 'px-3 py-1 rounded-xl bg-emerald-500 text-slate-950 text-xs font-bold transition';
        btnRabi.className = 'px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white text-xs font-bold transition';
        if (statusText) statusText.textContent = "🌧️ Active Season: Kharif (Monsoon Rice Paddies)";
        if (cropName) cropName.textContent = "Paddy Rice (Dhan)";
    }
    playSuccessChime();
}

function toggleTubeWell() {
    const dot = document.getElementById('waterSprayDot');
    if (!dot) return;
    dot.classList.toggle('hidden');
    playAcousticWoodClick();
}

// Simulator 3: Plains Harvest Cuisine
const thaliFoods = { roti: true, saag: true, makhan: true, lassi: true };
function toggleThaliFood(item) {
    thaliFoods[item] = !thaliFoods[item];
    const el = document.getElementById(`thaliItem${item.charAt(0).toUpperCase() + item.slice(1)}`);
    if (el) {
        if (thaliFoods[item]) {
            el.classList.remove('opacity-20');
        } else {
            el.classList.add('opacity-20');
        }
    }
    updateThaliNutrition();
    playAcousticWoodClick();
}

function resetPlainsThali() {
    thaliFoods.roti = true;
    thaliFoods.saag = true;
    thaliFoods.makhan = true;
    thaliFoods.lassi = true;
    ['Roti', 'Saag', 'Makhan', 'Lassi'].forEach(name => {
        const el = document.getElementById(`thaliItem${name}`);
        if (el) el.classList.remove('opacity-20');
    });
    updateThaliNutrition();
    playSuccessChime();
}

function updateThaliNutrition() {
    let carbs = 0, vitamins = 0, probio = 0;
    if (thaliFoods.roti) carbs += 55;
    if (thaliFoods.saag) { vitamins += 65; carbs += 15; }
    if (thaliFoods.makhan) { carbs += 10; }
    if (thaliFoods.lassi) { probio += 85; vitamins += 20; }

    document.getElementById('nutriCarbs').textContent = `${carbs}%`;
    document.getElementById('barCarbs').style.width = `${carbs}%`;
    document.getElementById('nutriVitamins').textContent = `${vitamins}%`;
    document.getElementById('barVitamins').style.width = `${vitamins}%`;
    document.getElementById('nutriProbiotics').textContent = `${probio}%`;
    document.getElementById('barProbiotics').style.width = `${probio}%`;
}

// Simulator 4: Golden Temple Langar
let langarMeals = 104250;
function operateRotiMachine() {
    langarMeals += 50;
    const countEl = document.getElementById('langarCount');
    if (countEl) countEl.textContent = langarMeals.toLocaleString();
    playAcousticWoodClick();
}

function stirDalCauldron() {
    langarMeals += 25;
    const countEl = document.getElementById('langarCount');
    if (countEl) countEl.textContent = langarMeals.toLocaleString();
    playSuccessChime();
}

// Simulator 5: Arid Desert Ecosystem
function toggleDesertFeature(feat) {
    const camel = document.getElementById('desertCamelSvg');
    const khejri = document.getElementById('desertKhejriSvg');
    const title = document.getElementById('desFeatureTitle');
    const desc = document.getElementById('desFeatureDesc');
    const press = document.getElementById('desPressureVal');
    const transp = document.getElementById('desTranspVal');
    const adapt = document.getElementById('desAdaptVal');

    if (feat === 'camel') {
        if (camel) camel.classList.remove('hidden');
        if (khejri) khejri.classList.add('hidden');
        if (title) title.textContent = "🐪 Camel (Ship of the Desert)";
        if (desc) desc.textContent = "Wide padded feet spread the camel's body mass over a large area, preventing sinking in loose dunes. The hump stores fat that metabolizes into energy and water.";
        if (press) press.textContent = "Low (Wide cushioned footpad)";
        if (transp) transp.textContent = "Minimal (Retains bodily water)";
        if (adapt) adapt.textContent = "Fat metabolism & double eyelashes";
    } else if (feat === 'khejri') {
        if (camel) camel.classList.add('hidden');
        if (khejri) khejri.classList.remove('hidden');
        if (title) title.textContent = "🌳 Khejri Tree (Desert Lifeline)";
        if (desc) desc.textContent = "Sends deep vertical taproots up to 30 metres subterranean to access hidden groundwater, providing shade and protein-rich sangri pods.";
        if (press) press.textContent = "Firm subterranean anchoring";
        if (transp) transp.textContent = "Very Low (Small waxy leaflets)";
        if (adapt) adapt.textContent = "30-metre taproot & edible pods";
    } else {
        if (camel) camel.classList.remove('hidden');
        if (khejri) khejri.classList.remove('hidden');
        if (title) title.textContent = "🌵 Xerophytic Spines vs Leaves";
        if (desc) desc.textContent = "Leaves are modified into sharp spines to minimize transpiration water loss and deter thirsty desert animals from chewing the succulent green stem.";
        if (press) press.textContent = "N/A";
        if (transp) transp.textContent = "Near Zero Transpiration";
        if (adapt) adapt.textContent = "Spines reduce transpiration";
    }
    playSuccessChime();
}

// Simulator 6: Desert Culture Attire
function playKhartalSound() {
    playAcousticWoodClick();
    setTimeout(playAcousticWoodClick, 100);
    setTimeout(playAcousticWoodClick, 220);
}

const bandhiniPalettes = [
    'from-red-600 via-amber-500 to-pink-600',
    'from-emerald-600 via-teal-500 to-cyan-600',
    'from-indigo-600 via-purple-500 to-rose-600'
];
let bPaletteIdx = 0;
function cycleBandhiniPattern() {
    bPaletteIdx = (bPaletteIdx + 1) % bandhiniPalettes.length;
    playSuccessChime();
}

// Simulator 7: Desert Water Tankas
function triggerTankaRain() {
    const rain = document.getElementById('tankaRainGroup');
    const water = document.getElementById('tankaWaterRect');
    const text = document.getElementById('tankaWaterText');
    if (!rain || !water) return;

    rain.classList.remove('hidden');
    water.setAttribute('height', '95');
    water.setAttribute('y', '128');
    if (text) text.textContent = "Water: 25,000 Litres (Full!)";
    playSuccessChime();

    setTimeout(() => {
        rain.classList.add('hidden');
    }, 2500);
}

// Simulator 8: Golden Sandstone Fort
function updateFortSun(val) {
    const shadeBox = document.getElementById('fortAlleyShade');
    if (!shadeBox) return;
    const opacity = 0.3 + (val / 100) * 0.4;
    shadeBox.style.backgroundColor = `rgba(0,0,0,${opacity})`;
}

// Simulator 9: Puri Coastal Seashore
function triggerPuriTide(type) {
    const ocean = document.getElementById('puriOceanPath');
    const status = document.getElementById('puriWaveStatus');
    if (!ocean) return;

    if (type === 'high') {
        ocean.setAttribute('d', 'M0,80 Q125,65 250,80 T500,75 L500,175 Q350,185 180,175 L0,180 Z');
        if (status) status.textContent = "🌊 Wave State: High Tide Breakers (Roots Anchoring Dunes)";
        playSuccessChime();
    } else {
        ocean.setAttribute('d', 'M0,95 Q125,85 250,95 T500,90 L500,150 Q350,165 180,155 L0,160 Z');
        if (status) status.textContent = "🏖️ Wave State: Calm Low Tide (Smooth Sandy Beach)";
        playAcousticWoodClick();
    }
}

// Simulator 10: Marine Coastal Biodiversity
function animateTurtleNesting() {
    const status = document.getElementById('turtleStatusText');
    const eggs = document.getElementById('turtleEggCount');
    if (status) status.textContent = "Mother turtle has laid ~100 eggs in the flask-shaped pit, covered the nest with moist sand, and navigated back to sea.";
    if (eggs) eggs.textContent = "Eggs: 115 incubated";
    playSuccessChime();
}

let beachLightsOn = false;
function toggleBeachLights() {
    beachLightsOn = !beachLightsOn;
    const btn = document.getElementById('btnLightToggle');
    const warning = document.getElementById('lightWarningBox');
    if (beachLightsOn) {
        if (btn) btn.className = 'px-2.5 py-1 text-xs rounded-lg bg-yellow-500 text-slate-950 font-bold transition';
        if (warning) {
            warning.className = 'p-2 rounded bg-red-950/80 border border-red-500 text-[11px] text-red-200';
            warning.innerHTML = "⚠️ <b>DANGER!</b> Bright lights active. Newly hatched baby turtles are disoriented away from the ocean.";
        }
        playErrorChime();
    } else {
        if (btn) btn.className = 'px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 text-yellow-300 font-semibold transition';
        if (warning) {
            warning.className = 'p-2 rounded bg-slate-900 border border-slate-800 text-[11px] text-slate-400';
            warning.textContent = "Natural Moon Horizon: Safe navigation into the open sea. Keep beach lights OFF!";
        }
        playSuccessChime();
    }
}

// Simulator 11: Coastal Chariot Heritage
let chariotMoved = false;
function pullChariotRopes() {
    const chariot = document.getElementById('chariotGroup');
    const status = document.getElementById('chariotMoveStatus');
    if (!chariot) return;

    chariotMoved = !chariotMoved;
    if (chariotMoved) {
        chariot.setAttribute('transform', 'translate(80, 20)');
        if (status) status.textContent = "Chariot Rolling on 16 Wooden Wheels! (Grand Road)";
        playSuccessChime();
    } else {
        chariot.setAttribute('transform', 'translate(180, 20)');
        if (status) status.textContent = "Chariot Stationary at Bada Danda (Grand Road)";
        playAcousticWoodClick();
    }
}

// Simulator 12: Cyclone Early Warning
function triggerCycloneRadarSweep() {
    playAcousticWoodClick();
}

function evacuateToShelter() {
    const badge = document.getElementById('evacStatusBadge');
    const log = document.getElementById('evacLogText');
    if (badge) badge.textContent = "Safe: 100% Evacuated (Zero Casualties)";
    if (log) log.textContent = "All 48 village hamlets safely transferred to elevated concrete cyclone shelters with solar power and potable water.";
    playSuccessChime();
}

// Simulator 13: Himalayan Mountain Landforms
let alpineSunrise = false;
function toggleKangchenjungaSun() {
    alpineSunrise = !alpineSunrise;
    const sky = document.getElementById('alpineSkyRect');
    const glacier = document.getElementById('peakSnowGlacier');
    const status = document.getElementById('mountainSunStatus');
    const btn = document.getElementById('btnSunToggle');

    if (alpineSunrise) {
        if (sky) sky.setAttribute('fill', '#475569');
        if (glacier) glacier.setAttribute('fill', '#fde047');
        if (status) status.textContent = "Current Time: Sunrise (Golden Alpenglow illuminating Kangchenjunga Glaciers)";
        if (btn) btn.textContent = "🌙 Return to Dusk";
        playSuccessChime();
    } else {
        if (sky) sky.setAttribute('fill', '#0f172a');
        if (glacier) glacier.setAttribute('fill', '#ffffff');
        if (status) status.textContent = "Current Time: Dawn (First Light Striking Glaciers)";
        if (btn) btn.textContent = "🌅 Sunrise Alpenglow";
        playAcousticWoodClick();
    }
}

// Simulator 14: Mountain Lifestyle Warmth
function feedHotThukpa() {
    const meter = document.getElementById('thukpaEnergyMeter');
    if (meter) {
        meter.textContent = "Metabolic Heat Active: Core Temperature Restored (+300 kcal)";
        meter.className = "text-[10px] text-emerald-300 font-bold text-center";
    }
    playSuccessChime();
}

// Simulator 15: Mountain Flora Festivals
function triggerRoofSnow() {
    const snow = document.getElementById('roofSnowPolygon');
    const status = document.getElementById('roofSnowStatus');
    if (snow) {
        snow.classList.add('opacity-0', 'transition-opacity', 'duration-500');
        setTimeout(() => snow.classList.remove('opacity-0'), 2000);
    }
    if (status) status.textContent = "Snow slid off pitched roof under gravity! Zero roof accumulation.";
    playSuccessChime();
}

let chaamAngle = 0;
function spinChaamDancer() {
    const mask = document.getElementById('chaamMaskIcon');
    if (!mask) return;
    chaamAngle += 360;
    mask.style.transform = `rotate(${chaamAngle}deg)`;
    playSuccessChime();
}

// Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);
});
'''.strip()

# Write JS file
js_path = os.path.join('.agents', 'class4_science_ch9_js.js')
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_code)

# Write Python module file
py_path = os.path.join('.agents', 'class4_science_ch9_js.py')
with open(py_path, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Complete JavaScript engine for Class 4 Science Chapter 9."""\n\n')
    f.write(f"complete_js = {repr(js_code)}\n")

print(f"Generated {js_path} and {py_path} successfully!")


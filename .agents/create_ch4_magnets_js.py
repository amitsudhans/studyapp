import re
import sys

def verify_no_latex(text, context=""):
    matches = re.findall(r'\\[a-zA-Z]+', text)
    if matches:
        print(f"ERROR: Raw LaTeX found in {context}: {matches[:10]}")
        sys.exit(1)

js_content = """
// Global state
let currentSlide = 1;
const totalSlides = 20;
let isAudioPlaying = false;
let audioUtterance = null;
let currentSentenceIndex = 0;
let speechSentences = [];
let audioSynth = window.speechSynthesis;

// Audio tone synthesizer for checkpoints
const audioCtx = (typeof AudioContext !== 'undefined' || typeof webkitAudioContext !== 'undefined') ? new (window.AudioContext || window.webkitAudioContext)() : null;

function playAudioTone(freq, type, duration) {
    if (!audioCtx) return;
    try {
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
    } catch(e) {}
}

function playSuccessTone() {
    playAudioTone(523.25, 'sine', 0.15); // C5
    setTimeout(() => playAudioTone(659.25, 'sine', 0.25), 120); // E5
}

function playErrorTone() {
    playAudioTone(311.13, 'sawtooth', 0.2); // Eb4
    setTimeout(() => playAudioTone(277.18, 'sawtooth', 0.25), 150); // Db4
}

// Sentence-by-sentence Web Speech API Lecture Engine
function cleanSpokenSentence(text) {
    if (!text) return '';
    return text.split(' ').filter(Boolean).join(' ');
}

function prepareSpeechQueue(slideId) {
    speechSentences = [];
    currentSentenceIndex = 0;
    const slideData = SLIDES_DATA.find(s => s.id === slideId);
    if (!slideData || !slideData.spoken_text) return;

    const rawText = slideData.spoken_text;
    const rawSentences = rawText.match(/[^.!?]+[.!?]+/g) || [rawText];
    rawSentences.forEach(s => {
        const cleaned = cleanSpokenSentence(s);
        if (cleaned.length > 2) {
            speechSentences.push(cleaned);
        }
    });
}

function speakNextSentence() {
    if (!isAudioPlaying || currentSentenceIndex >= speechSentences.length) {
        stopSpeech();
        return;
    }
    const sentence = speechSentences[currentSentenceIndex];
    audioUtterance = new SpeechSynthesisUtterance(sentence);
    audioUtterance.rate = 0.95;
    audioUtterance.pitch = 1.0;

    audioUtterance.onend = () => {
        currentSentenceIndex++;
        if (isAudioPlaying) {
            speakNextSentence();
        }
    };
    audioUtterance.onerror = () => {
        currentSentenceIndex++;
        if (isAudioPlaying) {
            speakNextSentence();
        }
    };

    updateAudioStatus(`Speaking sentence ${currentSentenceIndex + 1} of ${speechSentences.length}...`);
    audioSynth.speak(audioUtterance);
}

function toggleLectureAudio() {
    if (isAudioPlaying) {
        stopSpeech();
    } else {
        startSpeech();
    }
}

function startSpeech() {
    if (!audioSynth) {
        alert("Speech synthesis is not supported in this browser.");
        return;
    }
    audioSynth.cancel();
    isAudioPlaying = true;
    prepareSpeechQueue(currentSlide);
    if (speechSentences.length === 0) {
        updateAudioStatus("No spoken lecture for this slide.");
        isAudioPlaying = false;
        return;
    }
    updateAudioButtons(true);
    speakNextSentence();
}

function stopSpeech() {
    isAudioPlaying = false;
    if (audioSynth) {
        audioSynth.cancel();
    }
    updateAudioButtons(false);
    updateAudioStatus("Audio paused / ready");
}

function updateAudioButtons(isPlaying) {
    const globalBtn = document.getElementById('globalAudioBtn');
    const slideBtn = document.getElementById(`slideAudioBtn_${currentSlide}`);
    const text = isPlaying ? "⏸ Pause Lecture" : "🔊 Listen to Lecture";
    if (globalBtn) globalBtn.innerHTML = `<span>${isPlaying ? '⏸' : '🔊'}</span> ${text}`;
    if (slideBtn) slideBtn.innerHTML = `<span>${isPlaying ? '⏸' : '▶'}</span> ${isPlaying ? 'Pause Lecture' : 'Listen to Full Lecture'}`;
}

function updateAudioStatus(msg) {
    const el = document.getElementById('audioStatusText');
    if (el) el.textContent = msg;
}

// Slide Navigation
function goToSlide(n) {
    if (n < 1 || n > totalSlides) return;
    stopSpeech();

    // Hide old slide
    const oldSlide = document.getElementById(`slide-${currentSlide}`);
    if (oldSlide) oldSlide.classList.add('hidden');

    const oldThumb = document.getElementById(`thumb-${currentSlide}`);
    if (oldThumb) oldThumb.classList.remove('ring-2', 'ring-amber-400', 'bg-amber-500/20');

    currentSlide = n;

    // Show new slide
    const newSlide = document.getElementById(`slide-${currentSlide}`);
    if (newSlide) newSlide.classList.remove('hidden');

    const newThumb = document.getElementById(`thumb-${currentSlide}`);
    if (newThumb) newThumb.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500/20');

    // Update Counter & Progress Bar
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${currentSlide} / ${totalSlides}`;

    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
        const pct = (currentSlide / totalSlides) * 100;
        progressBar.style.width = `${pct}%`;
    }

    // Update Prev / Next Buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = currentSlide === 1;
        prevBtn.classList.toggle('opacity-50', currentSlide === 1);
        prevBtn.classList.toggle('cursor-not-allowed', currentSlide === 1);
    }

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'flex';
            nextBtn.disabled = false;
        }
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    // Auto initialize simulators if needed
    initSlideSim(currentSlide);
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

// Checkpoint handler
function handleCheckpoint(slideId, cpIdx, selectedOptIdx, correctOptIdx) {
    const container = document.getElementById(`cp_${slideId}_${cpIdx}`);
    if (!container) return;
    const buttons = container.querySelectorAll('.cp-btn');
    const feedbackBox = document.getElementById(`cp_fb_${slideId}_${cpIdx}`);

    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-700', 'border-slate-700');
        if (idx === correctOptIdx) {
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedOptIdx) {
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-200');
        } else {
            btn.classList.add('opacity-40');
        }
    });

    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        if (selectedOptIdx === correctOptIdx) {
            playSuccessTone();
            feedbackBox.classList.add('bg-emerald-950/60', 'border-emerald-500/40', 'text-emerald-300');
        } else {
            playErrorTone();
            feedbackBox.classList.add('bg-rose-950/60', 'border-rose-500/40', 'text-rose-300');
        }
    }
}

// Quiz challenge handler
function handleQuizSelect(qId, selectedOpt, correctOpt) {
    const card = document.getElementById(`quiz_card_${qId}`);
    if (!card) return;
    const btns = card.querySelectorAll('.quiz-opt-btn');
    const fb = document.getElementById(`quiz_fb_${qId}`);
    const solBtn = document.getElementById(`quiz_sol_btn_${qId}`);

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctOpt) {
            btn.classList.add('bg-emerald-900/70', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedOpt) {
            btn.classList.add('bg-rose-900/70', 'border-rose-500', 'text-rose-200');
        } else {
            btn.classList.add('opacity-40');
        }
    });

    if (fb) {
        fb.classList.remove('hidden');
        if (selectedOpt === correctOpt) {
            playSuccessTone();
            fb.innerHTML = "<span class='text-emerald-400 font-bold'>✓ Correct!</span> Excellent scientific deduction.";
        } else {
            playErrorTone();
            fb.innerHTML = "<span class='text-rose-400 font-bold'>✗ Incorrect.</span> Review the study solution.";
        }
    }
    if (solBtn) solBtn.classList.remove('hidden');
}

// Modal Solution handler
function openSolutionModal(qId) {
    const qData = QUIZ_DATA.find(q => q.id === qId);
    if (!qData) return;
    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('modalBody');
    const title = document.getElementById('modalTitle');

    if (title) title.textContent = `Question ${qData.id} • Step-by-Step Solution`;
    if (body) {
        body.innerHTML = `
            <div class="mb-3 text-slate-200 font-medium">${qData.question}</div>
            <div class="p-3 bg-slate-900 rounded-lg border border-slate-700">${qData.solution_html}</div>
        `;
    }
    if (modal) modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// ==========================================
// SIMULATOR CONTROLLERS
// ==========================================
function initSlideSim(slideNum) {
    if (slideNum === 2) setSim2Magnet('bar');
    if (slideNum === 6) initSim6();
}

// Sim 1: Weather toggle
let sim1Stormy = false;
function toggleSim1Weather() {
    sim1Stormy = !sim1Stormy;
    const clouds = document.getElementById('sim1Clouds');
    const stars = document.getElementById('sim1Stars');
    const needle = document.getElementById('sim1CompassNeedle');
    const status = document.getElementById('sim1StatusText');
    const btn = document.getElementById('toggleWeatherBtn');

    if (sim1Stormy) {
        if (clouds) clouds.classList.remove('opacity-0');
        if (stars) stars.classList.add('opacity-0');
        if (needle) needle.style.transform = 'rotate(-25deg)';
        setTimeout(() => { if (needle) needle.style.transform = 'rotate(0deg)'; }, 400);
        if (status) status.innerHTML = "<strong class='text-amber-400'>Storm!</strong> Compass needle points North. Navigation safe!";
        if (btn) btn.textContent = "Clear Sky ☀️";
    } else {
        if (clouds) clouds.classList.add('opacity-0');
        if (stars) stars.classList.remove('opacity-0');
        if (status) status.textContent = "Stars visible. Ship steering North.";
        if (btn) btn.textContent = "Toggle Storm Clouds";
    }
}

// Sim 2: Magnet shapes
function setSim2Magnet(type) {
    const display = document.getElementById('sim2Display');
    const desc = document.getElementById('sim2Description');
    const btns = ['btnMagBar', 'btnMagHorse', 'btnMagRing', 'btnMagNeedle'];
    btns.forEach(b => {
        const el = document.getElementById(b);
        if (el) {
            el.classList.remove('bg-sky-600', 'text-white');
            el.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    if (type === 'bar') {
        const b = document.getElementById('btnMagBar');
        if (b) { b.classList.add('bg-sky-600', 'text-white'); b.classList.remove('bg-slate-800'); }
        if (display) {
            display.innerHTML = `
                <div class="flex rounded-lg overflow-hidden shadow-2xl border-2 border-slate-600">
                    <div class="w-28 h-12 bg-red-600 flex items-center justify-center font-bold text-white text-base shadow-inner">N</div>
                    <div class="w-28 h-12 bg-blue-600 flex items-center justify-center font-bold text-white text-base shadow-inner">S</div>
                </div>
            `;
        }
        if (desc) desc.textContent = "Bar Magnet: Straight rectangular bar with North and South poles at opposite ends.";
    } else if (type === 'horseshoe') {
        const b = document.getElementById('btnMagHorse');
        if (b) { b.classList.add('bg-sky-600', 'text-white'); b.classList.remove('bg-slate-800'); }
        if (display) {
            display.innerHTML = `
                <div class="w-24 h-28 border-8 border-red-600 border-b-0 rounded-t-full relative flex justify-between items-end p-1">
                    <div class="w-6 h-8 bg-red-600 -ml-2 text-white font-bold text-xs flex items-center justify-center rounded-b">N</div>
                    <div class="w-6 h-8 bg-blue-600 -mr-2 text-white font-bold text-xs flex items-center justify-center rounded-b">S</div>
                </div>
            `;
        }
        if (desc) desc.textContent = "Horseshoe Magnet: U-shaped bar bringing North and South poles side by side to focus intense lifting power.";
    } else if (type === 'ring') {
        const b = document.getElementById('btnMagRing');
        if (b) { b.classList.add('bg-sky-600', 'text-white'); b.classList.remove('bg-slate-800'); }
        if (display) {
            display.innerHTML = `
                <div class="w-24 h-24 rounded-full border-8 border-slate-700 bg-slate-900 relative flex items-center justify-center shadow-2xl">
                    <div class="w-10 h-10 rounded-full border-4 border-slate-800 bg-slate-950"></div>
                    <span class="absolute top-1 text-[10px] text-red-400 font-bold">Top Face: N</span>
                    <span class="absolute bottom-1 text-[10px] text-blue-400 font-bold">Bottom Face: S</span>
                </div>
            `;
        }
        if (desc) desc.textContent = "Ring Magnet: Circular disc with opposite poles located on flat top and bottom faces. Used in speakers.";
    } else if (type === 'needle') {
        const b = document.getElementById('btnMagNeedle');
        if (b) { b.classList.add('bg-sky-600', 'text-white'); b.classList.remove('bg-slate-800'); }
        if (display) {
            display.innerHTML = `
                <div class="w-40 h-8 flex items-center justify-center relative">
                    <div class="w-0 h-0 border-y-8 border-y-transparent border-r-[70px] border-r-red-600"></div>
                    <div class="w-3 h-3 rounded-full bg-amber-400 border border-slate-950 z-10 -mx-1.5"></div>
                    <div class="w-0 h-0 border-y-8 border-y-transparent border-l-[70px] border-l-blue-600"></div>
                </div>
            `;
        }
        if (desc) desc.textContent = "Compass Needle: Tapered magnetized steel blade balanced on a low-friction jewel pivot.";
    }
}

// Sim 3: Magnetic tester
function testSim3Material(mat) {
    const box = document.getElementById('sim3ResultBox');
    if (!box) return;
    if (mat === 'iron') {
        playSuccessTone();
        box.innerHTML = "<span class='text-emerald-400 font-bold'>🧲 SNAP! Iron Nail:</span> Strongly magnetic! Ferromagnetic domains snap directly onto the magnet.";
    } else if (mat === 'steel') {
        playSuccessTone();
        box.innerHTML = "<span class='text-emerald-400 font-bold'>🧲 SNAP! Steel Clip:</span> Strongly magnetic! Steel is an iron-carbon alloy that clings tightly.";
    } else if (mat === 'nickel') {
        playSuccessTone();
        box.innerHTML = "<span class='text-emerald-400 font-bold'>🧲 SNAP! Nickel Bolt:</span> Strongly magnetic! Nickel is a natural ferromagnetic metal.";
    } else if (mat === 'wood') {
        playErrorTone();
        box.innerHTML = "<span class='text-rose-400 font-bold'>Zero Attraction: Wooden Pencil.</span> Wood is organic cellulose, completely non-magnetic.";
    } else if (mat === 'copper') {
        playErrorTone();
        box.innerHTML = "<span class='text-rose-400 font-bold'>Zero Attraction: Copper Coin.</span> Copper is non-ferrous and does not stick to magnets.";
    } else if (mat === 'plastic') {
        playErrorTone();
        box.innerHTML = "<span class='text-rose-400 font-bold'>Zero Attraction: Plastic Scale.</span> Synthetic plastic polymers are completely non-magnetic.";
    }
}

// Sim 4: Crane electromagnet
let sim4On = false;
function toggleSim4Electromagnet() {
    sim4On = !sim4On;
    const btn = document.getElementById('sim4CraneBtn');
    const head = document.getElementById('sim4CraneHead');
    const iron = document.getElementById('scrapIron');
    const steel = document.getElementById('scrapSteel');
    const status = document.getElementById('sim4Status');

    if (sim4On) {
        playSuccessTone();
        if (btn) { btn.textContent = "Turn Electromagnet OFF"; btn.classList.replace('bg-amber-600', 'bg-rose-600'); }
        if (head) {
            head.textContent = "⚡ ELECTROMAGNET (ON)";
            head.classList.replace('bg-slate-700', 'bg-amber-600');
            head.classList.replace('border-slate-500', 'border-amber-300');
        }
        if (iron) iron.style.transform = 'translateY(-60px)';
        if (steel) steel.style.transform = 'translateY(-60px)';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>MAGNETIC SEPARATION:</strong> Iron scrap & steel cars stick to crane! Non-magnetic aluminium cans and plastic remain behind.";
    } else {
        if (btn) { btn.textContent = "Turn Electromagnet ON"; btn.classList.replace('bg-rose-600', 'bg-amber-600'); }
        if (head) {
            head.textContent = "🧲 CRANE HEAD (OFF)";
            head.classList.replace('bg-amber-600', 'bg-slate-700');
            head.classList.replace('border-amber-300', 'border-slate-500');
        }
        if (iron) iron.style.transform = 'translateY(0px)';
        if (steel) steel.style.transform = 'translateY(0px)';
        if (status) status.textContent = "Electromagnet turned OFF. Scrap dropped into transport bin.";
    }
}

// Sim 5: Filings sprinkle
let sim5Sprinkled = false;
function sprinkleSim5Filings() {
    sim5Sprinkled = !sim5Sprinkled;
    const container = document.getElementById('sim5FilingsContainer');
    const status = document.getElementById('sim5Status');
    if (container) {
        if (sim5Sprinkled) {
            playSuccessTone();
            container.classList.remove('opacity-0');
            if (status) status.innerHTML = "<strong class='text-cyan-400'>Observation:</strong> Filings cluster densely at the North and South poles! The middle zone is nearly empty.";
        } else {
            container.classList.add('opacity-0');
            if (status) status.textContent = "Clean bar magnet. Click 'Sprinkle Iron Filings' to test pole strength.";
        }
    }
}

// Sim 6: Dipole Slicer
let sim6Stage = 1;
function initSim6() {
    sim6Stage = 1;
    renderSim6();
}

function cutSim6Magnet() {
    if (sim6Stage === 1) {
        sim6Stage = 2;
        playSuccessTone();
    } else if (sim6Stage === 2) {
        sim6Stage = 4;
        playSuccessTone();
    } else {
        sim6Stage = 1;
    }
    renderSim6();
}

function renderSim6() {
    const container = document.getElementById('sim6MagnetsContainer');
    const btn = document.getElementById('sim6CutBtn');
    const status = document.getElementById('sim6Status');
    if (!container) return;

    if (sim6Stage === 1) {
        container.innerHTML = `
            <div class="flex rounded overflow-hidden shadow-lg border border-slate-600">
                <div class="w-32 h-10 bg-red-600 text-white font-bold flex items-center justify-center">N</div>
                <div class="w-32 h-10 bg-blue-600 text-white font-bold flex items-center justify-center">S</div>
            </div>
        `;
        if (btn) btn.textContent = "Cut Magnet in Half ✂️";
        if (status) status.textContent = "1 Whole Magnet. Can you isolate the North pole?";
    } else if (sim6Stage === 2) {
        container.innerHTML = `
            <div class="flex gap-4">
                <div class="flex rounded overflow-hidden shadow-md border border-slate-600">
                    <div class="w-16 h-8 bg-red-600 text-white font-bold text-xs flex items-center justify-center">N</div>
                    <div class="w-16 h-8 bg-blue-600 text-white font-bold text-xs flex items-center justify-center">S</div>
                </div>
                <div class="flex rounded overflow-hidden shadow-md border border-slate-600">
                    <div class="w-16 h-8 bg-red-600 text-white font-bold text-xs flex items-center justify-center">N</div>
                    <div class="w-16 h-8 bg-blue-600 text-white font-bold text-xs flex items-center justify-center">S</div>
                </div>
            </div>
        `;
        if (btn) btn.textContent = "Cut into 4 Pieces ✂️";
        if (status) status.innerHTML = "<strong class='text-violet-400'>Two Complete Magnets!</strong> New opposite poles instantly formed at the cut!";
    } else if (sim6Stage === 4) {
        container.innerHTML = `
            <div class="grid grid-cols-2 gap-2">
                <div class="flex rounded overflow-hidden border border-slate-600">
                    <div class="w-10 h-6 bg-red-600 text-[10px] text-white font-bold flex items-center justify-center">N</div>
                    <div class="w-10 h-6 bg-blue-600 text-[10px] text-white font-bold flex items-center justify-center">S</div>
                </div>
                <div class="flex rounded overflow-hidden border border-slate-600">
                    <div class="w-10 h-6 bg-red-600 text-[10px] text-white font-bold flex items-center justify-center">N</div>
                    <div class="w-10 h-6 bg-blue-600 text-[10px] text-white font-bold flex items-center justify-center">S</div>
                </div>
                <div class="flex rounded overflow-hidden border border-slate-600">
                    <div class="w-10 h-6 bg-red-600 text-[10px] text-white font-bold flex items-center justify-center">N</div>
                    <div class="w-10 h-6 bg-blue-600 text-[10px] text-white font-bold flex items-center justify-center">S</div>
                </div>
                <div class="flex rounded overflow-hidden border border-slate-600">
                    <div class="w-10 h-6 bg-red-600 text-[10px] text-white font-bold flex items-center justify-center">N</div>
                    <div class="w-10 h-6 bg-blue-600 text-[10px] text-white font-bold flex items-center justify-center">S</div>
                </div>
            </div>
        `;
        if (btn) btn.textContent = "Reset Magnet 🔄";
        if (status) status.innerHTML = "<strong class='text-fuchsia-400'>Four Complete Magnets!</strong> Monopoles are impossible. Poles always come in pairs!";
    }
}

// Sim 7: Spinning suspended magnet
let sim7Angle = 0;
function spinSim7Magnet() {
    playSuccessTone();
    const mag = document.getElementById('sim7Magnet');
    const status = document.getElementById('sim7Status');
    const randomAngle = Math.floor(Math.random() * 360) + 720;
    if (mag) {
        mag.style.transform = `rotate(${randomAngle}deg)`;
        if (status) status.textContent = "Oscillating freely against air resistance...";
        setTimeout(() => {
            mag.style.transform = 'rotate(0deg)';
            if (status) status.innerHTML = "<strong class='text-teal-400'>DIRECTIVE PROPERTY:</strong> The magnet settles firmly along the North-South line!";
        }, 1200);
    }
}

// Sim 8: Earth's Dipole
let sim8Visible = true;
function toggleSim8Poles() {
    sim8Visible = !sim8Visible;
    const dip = document.getElementById('sim8Dipole');
    const status = document.getElementById('sim8Status');
    if (dip) {
        dip.style.opacity = sim8Visible ? '0.9' : '0.1';
        if (status) {
            status.innerHTML = sim8Visible ?
                "Earth's geodynamo creates an internal magnet with <strong>magnetic South near geographic North</strong>!" :
                "Magnetic dipole hidden. Earth's molten core convection generates this field.";
        }
    }
}

// Sim 9: Compass dial rotation
function rotateSim9Compass(deg) {
    const dial = document.getElementById('sim9Dial');
    const disp = document.getElementById('sim9AngleDisplay');
    if (dial) dial.style.transform = `rotate(${deg}deg)`;
    if (disp) {
        let heading = 'North';
        if (deg >= 45 && deg < 135) heading = 'East';
        else if (deg >= 135 && deg < 225) heading = 'South';
        else if (deg >= 225 && deg < 315) heading = 'West';
        disp.textContent = `Dial: ${deg}° (${heading})`;
    }
}

// Sim 10: Matsya-Yantra oil float
function stirSim10Oil() {
    playSuccessTone();
    const fish = document.getElementById('sim10Fish');
    const status = document.getElementById('sim10Status');
    if (fish) {
        fish.style.transform = 'rotate(180deg)';
        if (status) status.textContent = "Oil swirling... Viscous fluid dampens sudden wave shocks.";
        setTimeout(() => {
            fish.style.transform = 'rotate(0deg)';
            if (status) status.innerHTML = "<strong class='text-amber-400'>Ancient Matsya-Yantra:</strong> Frictionless oil flotation aligns the fish head North!";
        }, 1200);
    }
}

// Sim 11: Single-touch magnetize needle
let sim11Strokes = 0;
function performSim11Stroke() {
    sim11Strokes++;
    const counter = document.getElementById('sim11StrokeCounter');
    const needle = document.getElementById('sim11Needle');
    const status = document.getElementById('sim11Status');
    const magnet = document.getElementById('sim11Magnet');

    playSuccessTone();
    if (magnet) {
        magnet.style.transform = 'translateX(60px)';
        setTimeout(() => { magnet.style.transform = 'translateX(0px)'; }, 250);
    }

    if (counter) counter.textContent = `Strokes: ${sim11Strokes} / 30`;

    if (sim11Strokes >= 30) {
        if (needle) {
            needle.classList.remove('bg-slate-400');
            needle.classList.add('bg-gradient-to-r', 'from-red-500', 'to-blue-500');
        }
        if (status) status.innerHTML = "<strong class='text-emerald-400'>SUCCESS!</strong> The needle is now magnetized! Push through cork and float in water.";
    } else {
        if (status) status.textContent = `Keep stroking in the exact same direction! (${30 - sim11Strokes} strokes remaining)`;
    }
}

// Sim 12: Pencil rollers attraction vs repulsion
let sim12Flipped = false;
function flipSim12HandMagnet() {
    sim12Flipped = !sim12Flipped;
    const handLeft = document.getElementById('sim12HandLeft');
    const handRight = document.getElementById('sim12HandRight');
    const roller = document.getElementById('sim12RollerMagnet');
    const status = document.getElementById('sim12Status');

    if (sim12Flipped) {
        // S faces S (Like poles repel)
        playErrorTone();
        if (handLeft) { handLeft.textContent = 'S'; handLeft.classList.replace('bg-red-600', 'bg-blue-600'); }
        if (handRight) { handRight.textContent = 'N'; handRight.classList.replace('bg-blue-600', 'bg-red-600'); }
        if (roller) roller.style.transform = 'translateX(-40px)';
        if (status) status.innerHTML = "<strong class='text-rose-400'>REPULSION!</strong> Like poles face each other (S faces S): The roller magnet is pushed backwards!";
    } else {
        // S faces N (Unlike poles attract)
        playSuccessTone();
        if (handLeft) { handLeft.textContent = 'N'; handLeft.classList.replace('bg-blue-600', 'bg-red-600'); }
        if (handRight) { handRight.textContent = 'S'; handRight.classList.replace('bg-red-600', 'bg-blue-600'); }
        if (roller) roller.style.transform = 'translateX(30px)';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>ATTRACTION!</strong> Unlike poles face each other (S faces N): The roller magnet rolls eagerly forward!";
    }
}

// Sim 13: Mystery Bar Tester
function testSim13Bar(bar) {
    const label = document.getElementById('sim13MysteryLabel');
    const visual = document.getElementById('sim13BarVisual');
    const status = document.getElementById('sim13Status');
    const container = document.getElementById('sim13MysteryBar');

    if (bar === 'barA') {
        // Bar A is soft iron (attracts on both ends)
        playSuccessTone();
        if (label) label.textContent = "Testing Bar A (Mystery)";
        if (visual) visual.innerHTML = "<span class='text-emerald-400'>Attracts N</span> | <span class='text-emerald-400'>Attracts S</span>";
        if (container) container.style.transform = 'translateX(-20px)';
        if (status) status.innerHTML = "<strong class='text-amber-400'>Result for Bar A:</strong> Both ends attract the North pole. Zero repulsion! Bar A is an <em>ordinary unmagnetized iron bar</em>.";
    } else {
        // Bar B is a permanent magnet (repels on one end)
        playErrorTone();
        if (label) label.textContent = "Testing Bar B (Mystery)";
        if (visual) visual.innerHTML = "<span class='text-rose-400'>REPELS N</span> | <span class='text-emerald-400'>Attracts S</span>";
        if (container) container.style.transform = 'translateX(30px)';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>Result for Bar B:</strong> Repulsion observed on End 1! <em>Bar B is the TRUE MAGNET! Repulsion is the only sure test!</em>";
    }
}

// Sim 14: Action through barriers
function setSim14Barrier(type) {
    const vis = document.getElementById('sim14BarrierVisual');
    if (!vis) return;
    if (type === 'cardboard') {
        vis.textContent = "Cardboard Sheet";
        vis.className = "w-full h-4 bg-amber-700/80 rounded border border-amber-600 text-[10px] text-center font-bold text-amber-200";
    } else if (type === 'glass') {
        vis.textContent = "Transparent Glass Plate";
        vis.className = "w-full h-4 bg-cyan-700/50 rounded border border-cyan-400 text-[10px] text-center font-bold text-cyan-200";
    } else if (type === 'water') {
        vis.textContent = "Water Tumbler Barrier";
        vis.className = "w-full h-4 bg-blue-700/60 rounded border border-blue-400 text-[10px] text-center font-bold text-blue-200";
    }
}

function moveSim14Magnet(val) {
    const mag = document.getElementById('sim14Magnet');
    const clip = document.getElementById('sim14Clip');
    if (mag) mag.style.transform = `translateX(${val}px)`;
    if (clip) clip.style.transform = `translateX(${val}px)`;
}

// Sim 15: Storage Reset
function resetSim15Storage() {
    playSuccessTone();
    const status = document.getElementById('sim15Status');
    if (status) status.innerHTML = "<strong class='text-emerald-400'>STORAGE VERIFIED:</strong> Magnets stored in pairs with unlike poles opposite, wooden spacer inside, and soft iron keepers across ends.";
}

// Sim 16: Maglev Levitation
let sim16Levitated = false;
function toggleSim16Maglev() {
    sim16Levitated = !sim16Levitated;
    const btn = document.getElementById('sim16MaglevBtn');
    const train = document.getElementById('sim16Train');
    const gap = document.getElementById('sim16Gap');
    const spd = document.getElementById('sim16Speed');
    const status = document.getElementById('sim16Status');

    if (sim16Levitated) {
        playSuccessTone();
        if (btn) { btn.textContent = "Cut Levitation Power"; btn.classList.replace('bg-purple-600', 'bg-rose-600'); }
        if (train) train.style.transform = 'translateY(-15px)';
        if (gap) gap.textContent = "15 mm (Floating on magnetic repulsion)";
        if (spd) spd.textContent = "505 km/h (Frictionless cruise!)";
        if (status) status.innerHTML = "<strong class='text-purple-400'>LEVITATION ACTIVE:</strong> Like poles repel, floating the 40-tonne train. Zero wheel friction allows speeds over 500 km/h!";
    } else {
        if (btn) { btn.textContent = "Activate Levitation"; btn.classList.replace('bg-rose-600', 'bg-purple-600'); }
        if (train) train.style.transform = 'translateY(0px)';
        if (gap) gap.textContent = "0 mm (Resting on track)";
        if (spd) spd.textContent = "0 km/h";
        if (status) status.textContent = "Train is resting mechanically on the track. Activate electromagnets to achieve magnetic levitation!";
    }
}

// Keyboard shortcuts for slide navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        prevSlide();
    } else if (e.key === 'Escape') {
        closeSolutionModal();
    }
});
"""

verify_no_latex(js_content, "JavaScript Controller")
print("Verified JS controller with zero raw LaTeX.")

with open('.agents/class6_science_ch4_js.py', 'w') as f:
    f.write('"""\nJavaScript Controllers for NCERT Class 6 Science - Chapter 4\n"""\n\nJS_CODE = ' + repr(js_content) + '\n')

print("Created .agents/class6_science_ch4_js.py successfully!")

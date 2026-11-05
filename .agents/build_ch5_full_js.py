import re
import sys

js_code = """
// Science Chapter 5 Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis Engine (Sentence-by-Sentence Queue to prevent browser timeout)
let isSpeaking = false;
let currentSpeakingSlide = null;
let speechQueue = [];
let speechIndex = 0;

function stopSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    currentSpeakingSlide = null;
    speechQueue = [];
    speechIndex = 0;
    updateAllAudioButtons();
}

function speakNextSentence() {
    if (!isSpeaking || speechIndex >= speechQueue.length) {
        stopSpeech();
        return;
    }
    const text = speechQueue[speechIndex];
    speechIndex++;

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.95;
    utterance.pitch = 1.0;

    utterance.onend = () => {
        if (isSpeaking) {
            speakNextSentence();
        }
    };
    utterance.onerror = (e) => {
        console.warn("Speech error, advancing to next sentence:", e);
        if (isSpeaking) {
            speakNextSentence();
        }
    };

    window.speechSynthesis.speak(utterance);
}

function startLectureSpeech(fullText, slideNo) {
    if (!('speechSynthesis' in window)) {
        alert("Text-to-speech is not supported in this browser.");
        return;
    }

    if (isSpeaking && currentSpeakingSlide === slideNo) {
        stopSpeech();
        return;
    }

    stopSpeech();

    // Clean text and split by sentences
    const cleanText = fullText.replace(/<[^>]+>/g, ' ').split(' ').filter(Boolean).join(' ').trim();
    const rawSentences = cleanText.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [cleanText];
    speechQueue = rawSentences.map(s => s.trim()).filter(s => s.length > 0);

    if (speechQueue.length === 0) return;

    isSpeaking = true;
    currentSpeakingSlide = slideNo;
    speechIndex = 0;

    updateAllAudioButtons();
    speakNextSentence();
}

function toggleCurrentSlideLecture() {
    if (currentSlide > 16) {
        alert("This slide contains interactive mastery exercises for self-study and practice.");
        return;
    }
    const slideDataEl = document.getElementById(`slide-spoken-text-${currentSlide}`);
    if (slideDataEl) {
        const textToSpeak = slideDataEl.textContent.trim();
        startLectureSpeech(textToSpeak, currentSlide);
    }
}

function updateAllAudioButtons() {
    // Global Header Button
    const globalBtn = document.getElementById('globalAudioBtn');
    if (globalBtn) {
        if (isSpeaking) {
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 flex items-center space-x-1.5 animate-pulse transition';
            globalBtn.innerHTML = '<span>⏹</span><span>Stop Lecture</span>';
        } else {
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/30 border border-indigo-500/30 flex items-center space-x-1.5 transition';
            globalBtn.innerHTML = '<span>🔊</span><span>Listen to Lecture</span>';
        }
    }

    // Per-slide buttons
    for (let i = 1; i <= 16; i++) {
        const btn = document.getElementById(`slide-audio-btn-${i}`);
        const badge = document.getElementById(`slide-audio-badge-${i}`);
        if (btn) {
            if (isSpeaking && currentSpeakingSlide === i) {
                btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 flex items-center space-x-1.5 animate-pulse transition';
                btn.innerHTML = '<span>⏹</span><span>Stop Audio</span>';
                if (badge) {
                    badge.textContent = 'Speaking Lecture...';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30';
                }
            } else {
                btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 border border-indigo-500/30 flex items-center space-x-1.5 transition';
                btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
                if (badge) {
                    badge.textContent = 'Audio Lecture Ready';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
                }
            }
        }
    }
}

// Navigation
function updateSlideDisplay() {
    stopSpeech();

    for (let i = 1; i <= totalSlides; i++) {
        const slide = document.getElementById(`slide-${i}`);
        if (slide) {
            slide.style.display = (i === currentSlide) ? 'block' : 'none';
        }
    }

    // Update Counter & Progress
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${currentSlide} / ${totalSlides}`;

    const progress = document.getElementById('progressBar');
    if (progress) progress.style.width = `${(currentSlide / totalSlides) * 100}%`;

    // Update Buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        prevBtn.style.opacity = (currentSlide === 1) ? '0.4' : '1';
        prevBtn.style.cursor = (currentSlide === 1) ? 'not-allowed' : 'pointer';
    }

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.style.display = 'block';
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'flex';
            nextBtn.disabled = false;
        }
        if (lastNotice) lastNotice.style.display = 'none';
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        currentSlide++;
        updateSlideDisplay();
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        currentSlide--;
        updateSlideDisplay();
    }
}

function goToSlide(n) {
    if (n >= 1 && n <= totalSlides) {
        currentSlide = n;
        updateSlideDisplay();
    }
}

// Checkpoint Feedback Handler
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const badge = document.getElementById(`cp-badge-${cpId}`);
    const fb = document.getElementById(`cp-feedback-${cpId}`);
    if (!fb) return;

    const isCorrect = (selectedIdx === correctIdx);
    if (badge) {
        badge.textContent = isCorrect ? 'Solved Correctly' : 'Try Again';
        badge.className = isCorrect ?
            'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' :
            'px-2 py-0.5 rounded text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30';
    }

    fb.className = isCorrect ?
        'p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/30 text-xs text-emerald-200 mt-2 space-y-1' :
        'p-3 rounded-xl bg-rose-950/60 border border-rose-500/30 text-xs text-rose-200 mt-2 space-y-1';
    
    fb.innerHTML = `
        <div class="font-bold flex items-center space-x-1.5">
            <span>${isCorrect ? '✓ Correct!' : '✗ Not Quite.'}</span>
        </div>
        <p class="leading-relaxed">${explanation}</p>
    `;
    fb.style.display = 'block';
}

// Quiz Option Selection Handler
function selectQuizOption(qId, selectedLetter, correctLetter, title, question, solution) {
    const optionsContainer = document.getElementById(`q-options-${qId}`);
    const feedbackEl = document.getElementById(`q-feedback-${qId}`);
    const solBtn = document.getElementById(`q-sol-btn-${qId}`);

    if (optionsContainer) {
        const buttons = optionsContainer.querySelectorAll('button');
        buttons.forEach(btn => {
            btn.disabled = true;
            btn.classList.add('opacity-75');
            if (btn.textContent.trim().startsWith(correctLetter)) {
                btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-950/50 text-xs sm:text-sm text-emerald-200 font-semibold transition';
            } else if (btn.textContent.trim().startsWith(selectedLetter) && selectedLetter !== correctLetter) {
                btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-950/50 text-xs sm:text-sm text-rose-200 font-semibold transition';
            }
        });
    }

    if (feedbackEl) {
        const isCorrect = (selectedLetter === correctLetter);
        feedbackEl.className = isCorrect ?
            'p-3 rounded-xl bg-emerald-950/50 border border-emerald-500/30 text-xs text-emerald-200' :
            'p-3 rounded-xl bg-rose-950/50 border border-rose-500/30 text-xs text-rose-200';
        feedbackEl.innerHTML = `
            <div class="font-bold">${isCorrect ? '✓ Correct!' : '✗ Incorrect.'}</div>
            <div>The correct answer is Option ${correctLetter}. Review the step-by-step solution below.</div>
        `;
        feedbackEl.style.display = 'block';
    }

    if (solBtn) {
        solBtn.style.display = 'inline-flex';
    }
}

// Solution Modal
function openSolutionModal(title, question, correctAnswer, explanation) {
    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const questionEl = document.getElementById('modalQuestion');
    const answerEl = document.getElementById('modalAnswer');
    const explanationEl = document.getElementById('modalExplanation');

    if (titleEl) titleEl.textContent = title;
    if (questionEl) questionEl.innerHTML = question;
    if (answerEl) answerEl.innerHTML = `Correct Answer: ${correctAnswer}`;
    if (explanationEl) explanationEl.innerHTML = explanation;

    if (modal) modal.style.display = 'flex';
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// -------------------------------------------------------------
// Simulator 1: Tailor Shop Tool Switcher
// -------------------------------------------------------------
let sim1UsingTape = false;
function toggleSim1Tool() {
    sim1UsingTape = !sim1UsingTape;
    const btn = document.getElementById('sim1ModeBtn');
    const visual = document.getElementById('sim1ToolVisual');
    const status = document.getElementById('sim1Status');

    if (sim1UsingTape) {
        if (btn) btn.textContent = "Switch to Char Angula";
        if (visual) {
            visual.innerHTML = `
                <div class="w-64 h-6 bg-yellow-400 rounded border border-yellow-600 flex items-center justify-between px-2 text-slate-900 font-mono text-[10px] font-bold shadow">
                    <span>0 cm</span>
                    <span>15</span>
                    <span>30</span>
                    <span class="text-red-700 font-black">45.0 cm (Exact!)</span>
                </div>
            `;
        }
        if (status) status.innerHTML = "<strong class='text-emerald-400'>Calibrated Measuring Tape:</strong> Uniform millimetre divisions measure exactly <strong>45.0 cm</strong> for every tailor!";
    } else {
        if (btn) btn.textContent = "Switch to Flexible Tape";
        if (visual) {
            visual.innerHTML = `
                <div class="flex gap-2">
                    <span class="px-2 py-1 bg-amber-800/80 rounded border border-amber-600 text-[10px] text-amber-200 font-bold">4 fingers (~7cm)</span>
                    <span class="px-2 py-1 bg-amber-800/80 rounded border border-amber-600 text-[10px] text-amber-200 font-bold">4 fingers</span>
                    <span class="px-2 py-1 bg-amber-800/80 rounded border border-amber-600 text-[10px] text-amber-200 font-bold">4 fingers</span>
                    <span class="px-2 py-1 bg-amber-800/80 rounded border border-amber-600 text-[10px] text-amber-200 font-bold">~6.4 blocks?</span>
                </div>
            `;
        }
        if (status) status.innerHTML = "Using <strong>Char Angula</strong> (four fingers). Width varies by hand size! Click switch to test tailor's tape.";
    }
}

// -------------------------------------------------------------
// Simulator 2: Activity 5.1 Handspans
// -------------------------------------------------------------
function setSim2Student(type) {
    const btns = ['btnStudTall', 'btnStudMed', 'btnStudShort'];
    btns.forEach(b => {
        const el = document.getElementById(b);
        if (el) {
            el.className = 'px-2 py-1 bg-slate-800 text-slate-300 text-xs font-bold rounded border border-slate-700';
        }
    });

    const container = document.getElementById('sim2HandsContainer');
    const status = document.getElementById('sim2Status');

    let count = 6;
    let spanSize = 20;
    let name = "Tall Student (20 cm span)";

    if (type === 'tall') {
        const b = document.getElementById('btnStudTall');
        if (b) b.className = 'px-2 py-1 bg-sky-600 text-white text-xs font-bold rounded shadow';
        count = 6;
        spanSize = 20;
        name = "Tall Student (20 cm span)";
    } else if (type === 'med') {
        const b = document.getElementById('btnStudMed');
        if (b) b.className = 'px-2 py-1 bg-sky-600 text-white text-xs font-bold rounded shadow';
        count = 8;
        spanSize = 15;
        name = "Medium Student (15 cm span)";
    } else if (type === 'short') {
        const b = document.getElementById('btnStudShort');
        if (b) b.className = 'px-2 py-1 bg-sky-600 text-white text-xs font-bold rounded shadow';
        count = 10;
        spanSize = 12;
        name = "Small Student (12 cm span)";
    }

    if (container) {
        let hands = '';
        for (let i = 1; i <= count; i++) {
            hands += `<span class="px-2 py-1 bg-sky-900/60 rounded border border-sky-500/40 text-[10px] text-sky-200 font-bold shrink-0">✋ ${i}</span>`;
        }
        container.innerHTML = hands;
    }

    if (status) {
        status.innerHTML = `${name}: Desk of 120 cm measures <strong>${count} handspans</strong> (${count} x ${spanSize} cm = 120 cm). Body units are non-standard!`;
    }
}

// -------------------------------------------------------------
// Simulator 3: Lothal Ivory Scale Zoom
// -------------------------------------------------------------
let sim3Zoomed = false;
function toggleSim3Zoom() {
    sim3Zoomed = !sim3Zoomed;
    const btn = document.getElementById('sim3ZoomBtn');
    const scale = document.getElementById('sim3ScaleGraphic');
    const status = document.getElementById('sim3Status');

    if (sim3Zoomed) {
        if (btn) btn.textContent = "Reset Scale View 🔍";
        if (scale) scale.style.transform = 'scale(1.4)';
        if (status) status.innerHTML = "<strong class='text-amber-400'>1.7 mm Precision:</strong> Bronze Age Harappan engineers used 1.7 mm divisions to align city streets and dockyards!";
    } else {
        if (btn) btn.textContent = "Zoom 1.7 mm Divisions 🔍";
        if (scale) scale.style.transform = 'scale(1.0)';
        if (status) status.textContent = "Lothal ivory scale: Precision divisions of ~1.7 mm prove Harappan standard calibration.";
    }
}

// -------------------------------------------------------------
// Simulator 5: Metric Multiples Zoom
// -------------------------------------------------------------
function setSim5Zoom(val) {
    const disp = document.getElementById('sim5ScaleDisplay');
    const graphic = document.getElementById('sim5ZoomGraphic');
    const status = document.getElementById('sim5Status');

    if (val == 1) {
        if (disp) disp.textContent = "Scale: Millimetre (mm)";
        if (graphic) graphic.innerHTML = "<span class='text-3xl'>✏️</span><span class='text-xs font-mono text-emerald-300 font-bold mt-1'>Pencil Lead Tip: ~1 mm (0.1 cm)</span>";
        if (status) status.textContent = "Millimetre (mm): 1 cm = 10 mm. Smallest mark on school ruler.";
    } else if (val == 2) {
        if (disp) disp.textContent = "Scale: Centimetre (cm)";
        if (graphic) graphic.innerHTML = "<span class='text-3xl'>📏</span><span class='text-xs font-mono text-sky-300 font-bold mt-1'>15-cm School Ruler (1 cm = 10 mm)</span>";
        if (status) status.textContent = "Centimetre (cm): 1 m = 100 cm. Ideal for textbooks, pens, and shoes.";
    } else if (val == 3) {
        if (disp) disp.textContent = "Scale: Metre (m)";
        if (graphic) graphic.innerHTML = "<span class='text-3xl'>🚪</span><span class='text-xs font-mono text-indigo-300 font-bold mt-1'>Door Height: ~2 m (200 cm)</span>";
        if (status) status.textContent = "Metre (m): Base SI unit of length. Used for room walls and fabric.";
    } else if (val == 4) {
        if (disp) disp.textContent = "Scale: Kilometre (km)";
        if (graphic) graphic.innerHTML = "<span class='text-3xl'>🛣️</span><span class='text-xs font-mono text-amber-300 font-bold mt-1'>National Highway: 1 km = 1,000 m</span>";
        if (status) status.textContent = "Kilometre (km): 1 km = 1,000 m. Used for highway milestones and travel.";
    }
}

// -------------------------------------------------------------
// Simulator 6: Tool Matcher
// -------------------------------------------------------------
function testSim6Tool(obj) {
    const box = document.getElementById('sim6ResultBox');
    if (!box) return;

    if (obj === 'pencil') {
        box.innerHTML = `
            <div class="text-2xl mb-1">✏️ ➡️ 📏</div>
            <strong class="text-emerald-400">Match: 15-cm Plastic Ruler</strong>
            <p class="mt-1 text-slate-300">Pencil is small, rigid, and straight. A 15-cm ruler provides instant sub-millimetre accuracy.</p>
        `;
    } else if (obj === 'tree') {
        box.innerHTML = `
            <div class="text-2xl mb-1">🌳 ➡️ 🎗️</div>
            <strong class="text-emerald-400">Match: Flexible Tailor's Tape</strong>
            <p class="mt-1 text-slate-300">Tree trunks are curved. A flexible vinyl/fiberglass tape hugs the bark circumference without snapping!</p>
        `;
    } else if (obj === 'cloth') {
        box.innerHTML = `
            <div class="text-2xl mb-1">🧵 ➡️ 🥢</div>
            <strong class="text-emerald-400">Match: 1-Metre Rigid Steel Rod</strong>
            <p class="mt-1 text-slate-300">Cloth merchants use a stiff 1-metre steel rod to rapidly unroll and measure fabric reams without wrinkles.</p>
        `;
    } else if (obj === 'track') {
        box.innerHTML = `
            <div class="text-2xl mb-1">🏃 ➡️ 🛞</div>
            <strong class="text-emerald-400">Match: 50-Metre Surveyor Tape / Measuring Wheel</strong>
            <p class="mt-1 text-slate-300">Long ground distances require a heavy-duty 50-metre coiled tape or calibrated rolling surveyor wheel.</p>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 7: Parallax Angle
// -------------------------------------------------------------
function setSim7Angle(pos) {
    const ray = document.getElementById('sim7EyeRay');
    const status = document.getElementById('sim7Status');
    const btnA = document.getElementById('btnAngleA');
    const btnB = document.getElementById('btnAngleB');
    const btnC = document.getElementById('btnAngleC');

    [btnA, btnB, btnC].forEach(b => {
        if (b) b.className = 'px-2 py-1 bg-slate-800 text-slate-300 text-xs font-bold rounded border border-slate-700';
    });

    if (pos === 'A') {
        if (btnA) btnA.className = 'px-2 py-1 bg-rose-600 text-white text-xs font-bold rounded shadow';
        if (ray) ray.style.transform = 'translateX(-50px) rotate(20deg)';
        if (status) {
            status.className = 'mt-2 text-xs text-center text-rose-300 font-bold';
            status.textContent = "Position A (Left Angle): Parallax error! Skewed reading: 6.8 cm (Appears too long).";
        }
    } else if (pos === 'B') {
        if (btnB) btnB.className = 'px-2 py-1 bg-emerald-600 text-white text-xs font-bold rounded shadow';
        if (ray) ray.style.transform = 'translateX(0px) rotate(0deg)';
        if (status) {
            status.className = 'mt-2 text-xs text-center text-emerald-300 font-bold';
            status.textContent = "Position B: Eye directly perpendicular at 90°. True Reading: 6.5 cm (Zero Parallax!).";
        }
    } else if (pos === 'C') {
        if (btnC) btnC.className = 'px-2 py-1 bg-rose-600 text-white text-xs font-bold rounded shadow';
        if (ray) ray.style.transform = 'translateX(50px) rotate(-20deg)';
        if (status) {
            status.className = 'mt-2 text-xs text-center text-rose-300 font-bold';
            status.textContent = "Position C (Right Angle): Parallax error! Skewed reading: 6.2 cm (Appears too short).";
        }
    }
}

// -------------------------------------------------------------
// Simulator 9: Tactile Scale
// -------------------------------------------------------------
let sim9Tactile = false;
function toggleSim9Tactile() {
    sim9Tactile = !sim9Tactile;
    const btn = document.getElementById('sim9TactileBtn');
    const visual = document.getElementById('sim9ScaleVisual');
    const status = document.getElementById('sim9Status');

    if (sim9Tactile) {
        if (btn) btn.textContent = "Show Standard Scale 📏";
        if (visual) {
            visual.className = 'w-64 h-12 bg-amber-900/60 rounded border border-amber-500 flex items-center justify-around text-xs font-mono text-amber-300 font-bold';
            visual.innerHTML = '<span>⠼⠁ (1)</span><span>⠼⠃ (2)</span><span>⠼⠉ (3)</span><span>⠼⠙ (4)</span><span>⠼⠑ (5)</span>';
        }
        if (status) status.innerHTML = "<strong class='text-purple-400'>Tactile Scale Active:</strong> Embossed Braille dots and raised tactile notches enable visually challenged students to measure by touch!";
    } else {
        if (btn) btn.textContent = "Show Tactile Braille Scale 🦯";
        if (visual) {
            visual.className = 'w-64 h-12 bg-slate-800 rounded border border-slate-600 flex items-center justify-around text-xs font-mono';
            visual.innerHTML = '<span>1 cm</span><span>2 cm</span><span>3 cm</span><span>4 cm</span><span>5 cm</span>';
        }
        if (status) status.textContent = "Symbols never take plural 's' or trailing periods. Tactile scales use embossed dots for touch.";
    }
}

// -------------------------------------------------------------
// Simulator 10: Curved Thread
// -------------------------------------------------------------
let sim10Straight = false;
function straightenSim10Thread() {
    sim10Straight = !sim10Straight;
    const btn = document.getElementById('sim10ThreadBtn');
    const disp = document.getElementById('sim10Display');
    const status = document.getElementById('sim10Status');

    if (sim10Straight) {
        if (btn) btn.textContent = "Place Thread on Curved Line 〰️";
        if (disp) {
            disp.innerHTML = `
                <div class="flex flex-col items-center gap-2">
                    <div class="w-72 h-1 bg-teal-400 rounded-full shadow-[0_0_8px_#2dd4bf]"></div>
                    <div class="w-72 h-8 bg-slate-800 rounded border border-slate-600 flex items-center justify-between px-2 text-[10px] font-mono text-slate-300">
                        <span>0 cm</span><span>5 cm</span><span>10 cm</span><span>15 cm</span><span class="text-teal-300 font-bold">18.5 cm</span>
                    </div>
                </div>
            `;
        }
        if (status) status.innerHTML = "<strong class='text-teal-400'>Straightened Length:</strong> The thread measures exactly <strong>18.5 cm</strong> against the scale!";
    } else {
        if (btn) btn.textContent = "Straighten Thread on Scale 📏";
        initSim10();
        if (status) status.textContent = "Thread conforms to the winding curved line from A to B. Click to straighten across the centimetre ruler!";
    }
}

function initSim10() {
    const disp = document.getElementById('sim10Display');
    if (disp) {
        disp.innerHTML = `
            <svg width="280" height="90" viewBox="0 0 280 90">
                <path d="M 20 45 Q 80 10, 140 45 T 260 45" fill="none" stroke="#2dd4bf" stroke-width="4" stroke-dasharray="6,3"/>
                <circle cx="20" cy="45" r="5" fill="#f59e0b"/>
                <text x="15" y="30" fill="#f59e0b" font-size="11" font-weight="bold">Point A</text>
                <circle cx="260" cy="45" r="5" fill="#f59e0b"/>
                <text x="245" y="30" fill="#f59e0b" font-size="11" font-weight="bold">Point B</text>
            </svg>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 11: Highway Reference Point
// -------------------------------------------------------------
let sim11OriginDelhi = true;
function toggleSim11Origin() {
    sim11OriginDelhi = !sim11OriginDelhi;
    const btn = document.getElementById('sim11OriginBtn');
    const stone = document.getElementById('sim11Milestone');
    const status = document.getElementById('sim11Status');

    if (sim11OriginDelhi) {
        if (btn) btn.textContent = "Change Reference Origin";
        if (stone) stone.innerHTML = "<span>DELHI</span><span class='text-xs'>120 km</span>";
        if (status) status.innerHTML = "Reference Point: <strong>Delhi</strong>. The milestone indicates the car is 120 km from Delhi.";
    } else {
        if (btn) btn.textContent = "Reference: Delhi (Reset)";
        if (stone) stone.innerHTML = "<span>CHANDIGARH</span><span class='text-xs'>130 km</span>";
        if (status) status.innerHTML = "Reference Point: <strong>Chandigarh</strong>. Distance = 250 - 120 = <strong>130 km</strong> remaining to Chandigarh!";
    }
}

// -------------------------------------------------------------
// Simulator 12: Rest vs Motion Classroom
// -------------------------------------------------------------
function testSim12Object(obj) {
    const box = document.getElementById('sim12ResultBox');
    if (!box) return;

    if (obj === 'board') {
        box.innerHTML = `
            <div class="text-3xl mb-1">🏫</div>
            <strong class="text-emerald-400 font-bold text-sm">Blackboard: State of Rest</strong>
            <p class="mt-1 text-slate-300">Its position coordinates relative to the classroom walls and floor do NOT change over time.</p>
        `;
    } else if (obj === 'student') {
        box.innerHTML = `
            <div class="text-3xl mb-1">🚶</div>
            <strong class="text-sky-400 font-bold text-sm">Walking Student: State of Motion</strong>
            <p class="mt-1 text-slate-300">The student's distance from the door and teacher's desk continuously changes as seconds tick by.</p>
        `;
    } else if (obj === 'clock') {
        box.innerHTML = `
            <div class="text-3xl mb-1">⏰</div>
            <strong class="text-purple-400 font-bold text-sm">Clock Hands: Circular & Periodic Motion</strong>
            <p class="mt-1 text-slate-300">The hand rotates around the central pin, changing its directional position continuously over time.</p>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 13: Moving Bus Paradox
// -------------------------------------------------------------
let sim13Outside = false;
function toggleSim13Observer() {
    sim13Outside = !sim13Outside;
    const btn = document.getElementById('sim13ObsBtn');
    const status = document.getElementById('sim13Status');

    if (sim13Outside) {
        if (btn) btn.textContent = "Switch to Inside Passenger View 🚌";
        renderSim13Outside();
        if (status) status.innerHTML = "<strong class='text-amber-400'>Roadside Observer View:</strong> The bus and passengers are speeding past trees at <strong>60 km/h (In Motion!)</strong>.";
    } else {
        if (btn) btn.textContent = "Switch to Roadside Observer 🌲";
        renderSim13Inside();
        if (status) status.innerHTML = "Inside Bus View: Deepa and friend sit side by side. <strong>Relative Speed = 0 km/h (At Rest!).</strong>";
    }
}

function renderSim13Inside() {
    const scene = document.getElementById('sim13Scene');
    if (scene) {
        scene.innerHTML = `
            <div class="w-64 h-24 bg-indigo-950/80 rounded-xl border border-indigo-500/40 p-2 flex items-center justify-around">
                <div class="flex flex-col items-center">
                    <span class="text-2xl">👧</span>
                    <span class="text-[10px] text-indigo-300 font-bold">Deepa</span>
                </div>
                <div class="text-[10px] font-mono font-bold text-emerald-400 bg-slate-900 px-2 py-1 rounded">
                    Distance = 0.5 m (Constant!)
                </div>
                <div class="flex flex-col items-center">
                    <span class="text-2xl">👦</span>
                    <span class="text-[10px] text-indigo-300 font-bold">Friend</span>
                </div>
            </div>
        `;
    }
}

function renderSim13Outside() {
    const scene = document.getElementById('sim13Scene');
    if (scene) {
        scene.innerHTML = `
            <div class="w-full flex items-center justify-between px-6">
                <span class="text-3xl">🌲</span>
                <div class="flex items-center gap-2 bg-purple-900/60 p-2 rounded-lg border border-purple-500/40">
                    <span class="text-3xl animate-pulse">🚌</span>
                    <span class="text-xs font-bold text-amber-300">60 km/h ➡️</span>
                </div>
                <span class="text-2xl">🧍 (Bystander)</span>
            </div>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 14: Linear Motion
// -------------------------------------------------------------
function dropSim14Mango() {
    const mango = document.getElementById('sim14Mango');
    const status = document.getElementById('sim14Status');
    if (mango) {
        mango.style.transform = 'translateY(70px)';
        if (status) status.innerHTML = "<strong class='text-cyan-400'>Linear Motion:</strong> Mango dropped straight down in a 1D vertical straight line with zero deviation!";
        setTimeout(() => {
            mango.style.transform = 'translateY(0px)';
        }, 1500);
    }
}

// -------------------------------------------------------------
// Simulator 15: Circular Motion
// -------------------------------------------------------------
let sim15Rot = 0;
function spinSim15String() {
    sim15Rot += 360;
    const arm = document.getElementById('sim15StoneArm');
    const status = document.getElementById('sim15Status');
    if (arm) {
        arm.style.transform = `rotate(${sim15Rot}deg)`;
        if (status) status.innerHTML = "<strong class='text-emerald-400'>Circular Motion:</strong> The stone revolves along the circle. Radial distance to the hand remains strictly constant!";
    }
}

// -------------------------------------------------------------
// Simulator 16: Pendulum
// -------------------------------------------------------------
let sim16Swinging = false;
function swingSim16Pendulum() {
    const arm = document.getElementById('sim16PendulumArm');
    const status = document.getElementById('sim16Status');
    if (arm) {
        arm.style.transform = 'rotate(30deg)';
        setTimeout(() => {
            arm.style.transform = 'rotate(-30deg)';
        }, 400);
        setTimeout(() => {
            arm.style.transform = 'rotate(0deg)';
            if (status) status.innerHTML = "<strong class='text-purple-400'>Oscillatory & Periodic Motion:</strong> Bob swings to-and-fro across the mean position in equal time periods!";
        }, 800);
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    toggleSim1Tool();
    setSim2Student('tall');
    setSim5Zoom(2);
    initSim10();
    renderSim13Inside();

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
"""

matches = re.findall(r'\\[a-zA-Z]+', js_code)
if matches:
    print("Found LaTeX:", set(matches))
    sys.exit(1)

with open('.agents/class6_science_ch5_js.py', 'w') as f:
    f.write('"""\nJavaScript Code for Class 6 Science Chapter 5 Interactive Lab\n"""\n\nJS_CODE = ' + repr(js_code) + '\n')

print("Updated .agents/class6_science_ch5_js.py successfully!")

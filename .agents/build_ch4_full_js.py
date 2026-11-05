import re
import sys

js_code = """
// Science Chapter 4 Interactive JavaScript
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
// Simulator 1: Maritime Weather & Compass
// -------------------------------------------------------------
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

// -------------------------------------------------------------
// Simulator 2: Magnet Shapes
// -------------------------------------------------------------
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

// -------------------------------------------------------------
// Simulator 3: Magnetic Tester
// -------------------------------------------------------------
function testSim3Material(mat) {
    const box = document.getElementById('sim3ResultBox');
    if (!box) return;
    if (mat === 'iron') {
        box.innerHTML = "<span class='text-emerald-400 font-bold'>🧲 SNAP! Iron Nail:</span> Strongly magnetic! Ferromagnetic domains snap directly onto the magnet.";
    } else if (mat === 'steel') {
        box.innerHTML = "<span class='text-emerald-400 font-bold'>🧲 SNAP! Steel Clip:</span> Strongly magnetic! Steel is an iron-carbon alloy that clings tightly.";
    } else if (mat === 'nickel') {
        box.innerHTML = "<span class='text-emerald-400 font-bold'>🧲 SNAP! Nickel Bolt:</span> Strongly magnetic! Nickel is a natural ferromagnetic metal.";
    } else if (mat === 'wood') {
        box.innerHTML = "<span class='text-rose-400 font-bold'>Zero Attraction: Wooden Pencil.</span> Wood is organic cellulose, completely non-magnetic.";
    } else if (mat === 'copper') {
        box.innerHTML = "<span class='text-rose-400 font-bold'>Zero Attraction: Copper Coin.</span> Copper is non-ferrous and does not stick to magnets.";
    } else if (mat === 'plastic') {
        box.innerHTML = "<span class='text-rose-400 font-bold'>Zero Attraction: Plastic Scale.</span> Synthetic plastic polymers are completely non-magnetic.";
    }
}

// -------------------------------------------------------------
// Simulator 4: Crane Electromagnet
// -------------------------------------------------------------
let sim4On = false;
function toggleSim4Electromagnet() {
    sim4On = !sim4On;
    const btn = document.getElementById('sim4CraneBtn');
    const head = document.getElementById('sim4CraneHead');
    const iron = document.getElementById('scrapIron');
    const steel = document.getElementById('scrapSteel');
    const status = document.getElementById('sim4Status');

    if (sim4On) {
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

// -------------------------------------------------------------
// Simulator 5: Iron Filings Field Pattern
// -------------------------------------------------------------
let sim5Sprinkled = false;
function sprinkleSim5Filings() {
    sim5Sprinkled = !sim5Sprinkled;
    const container = document.getElementById('sim5FilingsContainer');
    const status = document.getElementById('sim5Status');
    if (container) {
        if (sim5Sprinkled) {
            container.classList.remove('opacity-0');
            if (status) status.innerHTML = "<strong class='text-cyan-400'>Observation:</strong> Filings cluster densely at the North and South poles! The middle zone is nearly empty.";
        } else {
            container.classList.add('opacity-0');
            if (status) status.textContent = "Clean bar magnet. Click 'Sprinkle Iron Filings' to test pole strength.";
        }
    }
}

// -------------------------------------------------------------
// Simulator 6: Dipole Slicer
// -------------------------------------------------------------
let sim6Stage = 1;
function initSim6() {
    sim6Stage = 1;
    renderSim6();
}

function cutSim6Magnet() {
    if (sim6Stage === 1) {
        sim6Stage = 2;
    } else if (sim6Stage === 2) {
        sim6Stage = 4;
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

// -------------------------------------------------------------
// Simulator 7: Suspended Magnet
// -------------------------------------------------------------
function spinSim7Magnet() {
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

// -------------------------------------------------------------
// Simulator 8: Earth's Dipole
// -------------------------------------------------------------
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

// -------------------------------------------------------------
// Simulator 9: 360° Compass
// -------------------------------------------------------------
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

// -------------------------------------------------------------
// Simulator 10: Matsya-Yantra
// -------------------------------------------------------------
function stirSim10Oil() {
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

// -------------------------------------------------------------
// Simulator 11: Single-Touch Needle Magnetizer
// -------------------------------------------------------------
let sim11Strokes = 0;
function performSim11Stroke() {
    sim11Strokes++;
    const counter = document.getElementById('sim11StrokeCounter');
    const needle = document.getElementById('sim11Needle');
    const status = document.getElementById('sim11Status');
    const magnet = document.getElementById('sim11Magnet');

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

// -------------------------------------------------------------
// Simulator 12: Pencil Rollers
// -------------------------------------------------------------
let sim12Flipped = false;
function flipSim12HandMagnet() {
    sim12Flipped = !sim12Flipped;
    const handLeft = document.getElementById('sim12HandLeft');
    const handRight = document.getElementById('sim12HandRight');
    const roller = document.getElementById('sim12RollerMagnet');
    const status = document.getElementById('sim12Status');

    if (sim12Flipped) {
        if (handLeft) { handLeft.textContent = 'S'; handLeft.classList.replace('bg-red-600', 'bg-blue-600'); }
        if (handRight) { handRight.textContent = 'N'; handRight.classList.replace('bg-blue-600', 'bg-red-600'); }
        if (roller) roller.style.transform = 'translateX(-40px)';
        if (status) status.innerHTML = "<strong class='text-rose-400'>REPULSION!</strong> Like poles face each other (S faces S): The roller magnet is pushed backwards!";
    } else {
        if (handLeft) { handLeft.textContent = 'N'; handLeft.classList.replace('bg-blue-600', 'bg-red-600'); }
        if (handRight) { handRight.textContent = 'S'; handRight.classList.replace('bg-red-600', 'bg-blue-600'); }
        if (roller) roller.style.transform = 'translateX(30px)';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>ATTRACTION!</strong> Unlike poles face each other (S faces N): The roller magnet rolls eagerly forward!";
    }
}

// -------------------------------------------------------------
// Simulator 13: Mystery Bar Tester
// -------------------------------------------------------------
function testSim13Bar(bar) {
    const label = document.getElementById('sim13MysteryLabel');
    const visual = document.getElementById('sim13BarVisual');
    const status = document.getElementById('sim13Status');
    const container = document.getElementById('sim13MysteryBar');

    if (bar === 'barA') {
        if (label) label.textContent = "Testing Bar A (Mystery)";
        if (visual) visual.innerHTML = "<span class='text-emerald-400'>Attracts N</span> | <span class='text-emerald-400'>Attracts S</span>";
        if (container) container.style.transform = 'translateX(-20px)';
        if (status) status.innerHTML = "<strong class='text-amber-400'>Result for Bar A:</strong> Both ends attract the North pole. Zero repulsion! Bar A is an <em>ordinary unmagnetized iron bar</em>.";
    } else {
        if (label) label.textContent = "Testing Bar B (Mystery)";
        if (visual) visual.innerHTML = "<span class='text-rose-400'>REPELS N</span> | <span class='text-emerald-400'>Attracts S</span>";
        if (container) container.style.transform = 'translateX(30px)';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>Result for Bar B:</strong> Repulsion observed on End 1! <em>Bar B is the TRUE MAGNET! Repulsion is the only sure test!</em>";
    }
}

// -------------------------------------------------------------
// Simulator 14: Barriers
// -------------------------------------------------------------
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

// -------------------------------------------------------------
// Simulator 15: Storage
// -------------------------------------------------------------
function resetSim15Storage() {
    const status = document.getElementById('sim15Status');
    if (status) status.innerHTML = "<strong class='text-emerald-400'>STORAGE VERIFIED:</strong> Magnets stored in pairs with unlike poles opposite, wooden spacer inside, and soft iron keepers across ends.";
}

// -------------------------------------------------------------
// Simulator 16: Maglev
// -------------------------------------------------------------
let sim16Levitated = false;
function toggleSim16Maglev() {
    sim16Levitated = !sim16Levitated;
    const btn = document.getElementById('sim16MaglevBtn');
    const train = document.getElementById('sim16Train');
    const gap = document.getElementById('sim16Gap');
    const spd = document.getElementById('sim16Speed');
    const status = document.getElementById('sim16Status');

    if (sim16Levitated) {
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

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    setSim2Magnet('bar');
    initSim6();

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

with open('.agents/class6_science_ch4_js.py', 'w') as f:
    f.write('"""\nJavaScript Code for Class 6 Science Chapter 4 Interactive Lab\n"""\n\nJS_CODE = ' + repr(js_code) + '\n')

print("Updated .agents/class6_science_ch4_js.py successfully!")

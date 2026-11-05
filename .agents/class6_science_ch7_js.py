"""
Interactive JavaScript for Class 6 Science Chapter 7: Temperature and its Measurement
Handles sentence-by-sentence Web Speech API, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure Unicode.
"""

JS_CODE = '''
// Science Chapter 7 Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis Engine (Sentence-by-Sentence Queue with Male Voice Selection)
let isSpeaking = false;
let currentSpeakingSlide = null;
let speechQueue = [];
let speechIndex = 0;
let selectedMaleVoice = null;

function getMaleVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const enVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
    const pool = enVoices.length > 0 ? enVoices : voices;

    const femaleKeywords = ['female', 'zira', 'jenny', 'aria', 'samantha', 'victoria', 'karen', 'susan', 'neerja', 'heera', 'hazel', 'catherine', 'linda', 'eva', 'ava', 'siri'];
    const isFemale = (v) => {
        const name = (v.name || '').toLowerCase();
        return femaleKeywords.some(fk => name.includes(fk));
    };

    const maleKeywords = ['male', 'david', 'mark', 'george', 'daniel', 'guy', 'stefan', 'oliver', 'rishi', 'arthur', 'james', 'richard', 'brian', 'sean', 'alex', 'fred', 'ravi', 'neil'];

    // 1. Try finding an English voice explicitly matching male names/keywords and not female
    for (const mk of maleKeywords) {
        const match = pool.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemale(v));
        if (match) return match;
    }

    // 2. Try finding any English voice with gender === 'male'
    const genderMatch = pool.find(v => v.gender === 'male' || (v.name && v.name.toLowerCase().includes('male')));
    if (genderMatch) return genderMatch;

    // 3. Try finding any non-female English voice from standard providers
    const naturalMale = pool.find(v => {
        const name = (v.name || '').toLowerCase();
        return (name.includes('google') || name.includes('microsoft') || name.includes('natural')) && !isFemale(v);
    });
    if (naturalMale) return naturalMale;

    // 4. Any voice that is not in the female list
    const nonFemale = pool.find(v => !isFemale(v));
    if (nonFemale) return nonFemale;

    return pool[0] || null;
}

if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        selectedMaleVoice = getMaleVoice();
    };
    selectedMaleVoice = getMaleVoice();
}

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
    utterance.pitch = 0.88; // Deep, clear baritone male pitch

    if (!selectedMaleVoice) {
        selectedMaleVoice = getMaleVoice();
    }
    if (selectedMaleVoice) {
        utterance.voice = selectedMaleVoice;
    }

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

// Slide Navigation
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

    // Update Control Buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    const select = document.getElementById('slideSelect');
    if (select) select.value = currentSlide;

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
        <div class="flex items-center space-x-1.5 font-bold ${isCorrect ? 'text-emerald-400' : 'text-rose-400'}">
            <span>${isCorrect ? '✓ Correct Answer!' : '✕ Not Quite'}</span>
        </div>
        <p class="mt-1 leading-relaxed text-slate-300">${explanation}</p>
    `;
    fb.style.display = 'block';
}

// Quiz Selection Handler
function selectQuizOption(qId, selectedOpt, correctOpt, title, question, solution) {
    const fb = document.getElementById(`q-feedback-${qId}`);
    const solBtn = document.getElementById(`q-sol-btn-${qId}`);
    const optsContainer = document.getElementById(`q-options-${qId}`);

    if (optsContainer) {
        const buttons = optsContainer.getElementsByTagName('button');
        for (let btn of buttons) {
            btn.disabled = true;
            btn.classList.remove('hover:bg-slate-700', 'bg-slate-800/60');
            const btnOpt = btn.textContent.trim().charAt(0);
            if (btnOpt === correctOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500/60 bg-emerald-950/50 text-xs sm:text-sm text-emerald-200 font-semibold';
            } else if (btnOpt === selectedOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500/60 bg-rose-950/50 text-xs sm:text-sm text-rose-200 font-semibold';
            } else {
                btn.className = 'w-full text-left p-3 rounded-xl border border-slate-800 bg-slate-900/40 text-xs sm:text-sm text-slate-500';
            }
        }
    }

    if (fb) {
        const isCorrect = (selectedOpt === correctOpt);
        fb.className = isCorrect ?
            'p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-200 mt-2' :
            'p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-xs text-rose-200 mt-2';
        fb.innerHTML = `
            <div class="font-bold flex items-center space-x-2">
                <span>${isCorrect ? '🎉 Correct!' : '⚠️ Incorrect Choice'}</span>
            </div>
            <p class="mt-1 text-slate-300 leading-relaxed">
                ${isCorrect ? 'Outstanding scientific reasoning!' : `The correct option is <strong>${correctOpt}</strong>.`}
            </p>
        `;
        fb.style.display = 'block';
    }

    if (solBtn) {
        solBtn.style.display = 'inline-flex';
    }
}

// Pop-up Solution Modal
function openSolutionModal(title, question, answer, explanation) {
    const modal = document.getElementById('solutionModal');
    if (!modal) return;

    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalQuestion').innerHTML = `<strong>Question:</strong> ${question}`;
    document.getElementById('modalAnswer').innerHTML = `<strong>Correct Answer:</strong> ${answer}`;
    document.getElementById('modalExplanation').innerHTML = `<strong>Step-by-Step Explanation:</strong><br>${explanation}`;

    modal.style.display = 'flex';
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// -------------------------------------------------------------
// Simulator 1: Touch vs Digital Probe Comparator
// -------------------------------------------------------------
function testSim1Method(method) {
    const badge = document.getElementById('sim1ModeBadge');
    const summary = document.getElementById('sim1Summary');
    const cardHand = document.getElementById('sim1Card-hand');
    const cardTool = document.getElementById('sim1Card-tool');

    if (method === 'hand') {
        if (badge) {
            badge.textContent = 'Subjective Sensation';
            badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
        if (cardHand) cardHand.className = 'p-3.5 rounded-xl bg-slate-800/90 border-2 border-amber-500 transition space-y-2';
        if (cardTool) cardTool.className = 'p-3.5 rounded-xl bg-slate-800/40 border border-slate-700/60 opacity-60 transition space-y-2';
        if (summary) summary.innerHTML = "<strong class='text-amber-300'>Subjective Sensation:</strong> Hand touch depends entirely on the temperature of your own palm. If your fingers are cold, normal skin feels feverish!";
    } else {
        if (badge) {
            badge.textContent = 'Objective Measurement';
            badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        }
        if (cardTool) cardTool.className = 'p-3.5 rounded-xl bg-slate-800/90 border-2 border-emerald-500 transition space-y-2';
        if (cardHand) cardHand.className = 'p-3.5 rounded-xl bg-slate-800/40 border border-slate-700/60 opacity-60 transition space-y-2';
        if (summary) summary.innerHTML = "<strong class='text-emerald-400'>Scientific Objective Measurement:</strong> The calibrated electronic thermistor records 37.0°C (98.6°F) with zero human observer bias.";
    }
}

// -------------------------------------------------------------
// Simulator 2: The Three-Bowl Paradox (Activity 7.1)
// -------------------------------------------------------------
let sim2Step = 0;

function runSim2Step1() {
    sim2Step = 1;
    const badge = document.getElementById('sim2StateBadge');
    const btn1 = document.getElementById('sim2Btn1');
    const btn2 = document.getElementById('sim2Btn2');
    const feedback = document.getElementById('sim2Feedback');
    const bowlA = document.getElementById('sim2BowlA');
    const bowlC = document.getElementById('sim2BowlC');
    const leftLbl = document.getElementById('sim2LeftHandLabel');
    const rightLbl = document.getElementById('sim2RightHandLabel');

    if (badge) {
        badge.textContent = 'Hands Adapting in Bowls A & C';
        badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 animate-pulse';
    }
    if (bowlA) bowlA.classList.add('ring-4', 'ring-rose-500');
    if (bowlC) bowlC.classList.add('ring-4', 'ring-cyan-500');
    if (leftLbl) { leftLbl.textContent = 'Left Hand in Warm Water (40°C)'; leftLbl.className = 'text-[10px] text-rose-300 mt-1 font-bold'; }
    if (rightLbl) { rightLbl.textContent = 'Right Hand in Cold Water (5°C)'; rightLbl.className = 'text-[10px] text-cyan-300 mt-1 font-bold'; }

    if (btn1) { btn1.disabled = true; btn1.className = 'p-2.5 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs cursor-not-allowed'; }
    if (btn2) { btn2.disabled = false; btn2.className = 'p-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-lg transition animate-bounce'; }

    if (feedback) {
        feedback.innerHTML = "Hands have been immersed for 2 minutes and thermally adapted. Now click <strong>Step 2</strong> to plunge both hands into Bowl B!";
    }
}

function runSim2Step2() {
    sim2Step = 2;
    const badge = document.getElementById('sim2StateBadge');
    const btn2 = document.getElementById('sim2Btn2');
    const feedback = document.getElementById('sim2Feedback');
    const bowlA = document.getElementById('sim2BowlA');
    const bowlB = document.getElementById('sim2BowlB');
    const bowlC = document.getElementById('sim2BowlC');
    const leftLbl = document.getElementById('sim2LeftHandLabel');
    const rightLbl = document.getElementById('sim2RightHandLabel');

    if (bowlA) bowlA.classList.remove('ring-4', 'ring-rose-500');
    if (bowlC) bowlC.classList.remove('ring-4', 'ring-cyan-500');
    if (bowlB) bowlB.classList.add('ring-4', 'ring-emerald-500');

    if (leftLbl) { leftLbl.textContent = 'Left Hand (feels COLD!) ❄️'; leftLbl.className = 'text-[10px] text-cyan-400 mt-1 font-extrabold'; }
    if (rightLbl) { rightLbl.textContent = 'Right Hand (feels WARM!) 🔥'; rightLbl.className = 'text-[10px] text-rose-400 mt-1 font-extrabold'; }

    if (badge) {
        badge.textContent = 'Sensory Paradox Confirmed!';
        badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }

    if (btn2) { btn2.disabled = true; btn2.className = 'p-2.5 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs cursor-not-allowed'; }

    if (feedback) {
        feedback.innerHTML = "<strong class='text-amber-400'>The Sensory Paradox:</strong> To the left hand, the 22°C tap water feels cold (losing heat). To the right hand, the exact same water feels warm (gaining heat)! Proving that touch cannot serve as a reliable scientific measure.";
    }
}

// -------------------------------------------------------------
// Simulator 3: Molecular Kinetic Speed & Thermal Motion
// -------------------------------------------------------------
let sim3Particles = [];
function initSim3Particles() {
    sim3Particles = [];
    for (let i = 0; i < 20; i++) {
        sim3Particles.push({
            x: 20 + Math.random() * 300,
            y: 20 + Math.random() * 110,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2
        });
    }
    renderSim3Svg(25);
}

function updateSim3Temp(temp) {
    const badge = document.getElementById('sim3TempBadge');
    const label = document.getElementById('sim3SliderLabel');
    const insight = document.getElementById('sim3Insight');
    const t = parseInt(temp, 10);

    if (badge) badge.textContent = `${t} °C`;
    if (label) {
        if (t <= 5) label.textContent = `${t} °C (Near Freezing)`;
        else if (t >= 95) label.textContent = `${t} °C (Boiling Point)`;
        else if (t >= 35 && t <= 40) label.textContent = `${t} °C (Human Body Range)`;
        else label.textContent = `${t} °C`;
    }

    if (insight) {
        if (t < 15) {
            insight.innerHTML = `<strong class='text-cyan-300'>Low Temperature (${t}°C):</strong> Sluggish molecular motion. Particles have low average kinetic energy.`;
        } else if (t > 75) {
            insight.innerHTML = `<strong class='text-rose-400'>High Temperature (${t}°C):</strong> Violent, rapid collisions! High molecular kinetic energy directly manifests as elevated temperature.`;
        } else {
            insight.innerHTML = `Moderate kinetic vibration at ${t}°C. Temperature is the statistical average kinetic energy of molecular agitation.`;
        }
    }

    renderSim3Svg(t);
}

function renderSim3Svg(temp) {
    const svg = document.getElementById('sim3ParticleBox');
    if (!svg) return;

    const speedFactor = 0.5 + (temp / 100) * 3;
    let circlesHtml = '';

    sim3Particles.forEach((p, idx) => {
        p.x += p.vx * speedFactor;
        p.y += p.vy * speedFactor;

        if (p.x < 15 || p.x > 325) p.vx *= -1;
        if (p.y < 15 || p.y > 135) p.vy *= -1;

        const color = temp > 70 ? '#f43f5e' : (temp < 15 ? '#38bdf8' : '#fbbf24');
        circlesHtml += `<circle cx="${p.x}" cy="${p.y}" r="4" fill="${color}" opacity="0.8"/>`;
    });

    svg.innerHTML = `
        <rect x="5" y="5" width="330" height="140" rx="8" fill="none" stroke="#475569" stroke-width="1.5"/>
        ${circlesHtml}
    `;
}

// -------------------------------------------------------------
// Simulator 4: Digital Clinical Thermometer Inspector
// -------------------------------------------------------------
const sim4PartInfo = {
    tip: {
        title: "Probe Tip (Thermistor Sensor)",
        desc: "Made of non-reactive stainless steel enclosing an electronic thermistor. Its electrical resistance changes instantly and predictably with body heat."
    },
    lcd: {
        title: "Liquid Crystal Display (LCD)",
        desc: "Displays the calculated temperature digitally in sharp decimal figures (e.g., 37.0°C). Eliminates human misinterpretation of glass capillaries."
    },
    btn: {
        title: "Power & Memory Button",
        desc: "Switches on the device, initiates a screen self-check, displays the previous stored fever reading, and resets to 'Lo °C'."
    },
    battery: {
        title: "Button Cell Battery Compartment",
        desc: "Holds a long-lasting, safe 1.5 V alkaline button battery (LR41) powering the microchip for thousands of readings."
    }
};

function inspectSim4Part(part) {
    const details = document.getElementById('sim4Details');
    const d = sim4PartInfo[part];
    if (details && d) {
        details.innerHTML = `
            <span class="font-bold text-cyan-300 block">${d.title}:</span>
            <p class="text-slate-300 leading-relaxed">${d.desc}</p>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 5: Non-Contact Infrared Scanner
// -------------------------------------------------------------
function triggerSim5Scan() {
    const beamLine = document.getElementById('sim5BeamLine');
    const beamArrow = document.getElementById('sim5BeamArrow');
    const scanText = document.getElementById('sim5ScanText');
    const gunDisplay = document.getElementById('sim5GunDisplay');
    const status = document.getElementById('sim5Status');

    if (beamLine) beamLine.setAttribute('opacity', '1');
    if (beamArrow) beamArrow.setAttribute('opacity', '1');
    if (scanText) scanText.style.opacity = '1';
    if (gunDisplay) gunDisplay.textContent = 'Scanning...';

    setTimeout(() => {
        if (gunDisplay) gunDisplay.textContent = '36.8 °C';
        if (beamLine) beamLine.setAttribute('opacity', '0');
        if (beamArrow) beamArrow.setAttribute('opacity', '0');
        if (scanText) scanText.style.opacity = '0';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>Scan Complete (0.5 s):</strong> Normal temperature 36.8°C recorded via temporal artery thermal emission. Zero physical contact, zero contamination risk!";
    }, 600);
}

// -------------------------------------------------------------
// Simulator 6: Clinical Measuring Step Simulator (Activity 7.2)
// -------------------------------------------------------------
let sim6CurStep = 1;
const sim6Steps = [
    {
        num: 1,
        title: "Step 1: Sanitize Probe Tip",
        icon: "🧼",
        desc: "Wipe the metal sensor probe thoroughly with an alcohol swab or wash with clean water and antiseptic solution to neutralize oral pathogens."
    },
    {
        num: 2,
        title: "Step 2: Power On & Check 'Lo'",
        icon: "⏻",
        desc: "Press the power button. Confirm the self-test and ensure 'Lo °C' appears on the LCD, verifying readiness for measurement."
    },
    {
        num: 3,
        title: "Step 3: Correct Placement",
        icon: "👅",
        desc: "Place the metal tip firmly under the tongue with mouth closed (or deep into the center of the armpit for infants/elderly)."
    },
    {
        num: 4,
        title: "Step 4: Wait for Beeper Alert",
        icon: "⏱️",
        desc: "Hold still for approximately 60 seconds until the internal thermistor stabilizes and sounds consecutive beeps: 'Beep-Beep-Beep!'"
    },
    {
        num: 5,
        title: "Step 5: Record Reading & Disinfect",
        icon: "📝",
        desc: "Read the clear digital numbers (e.g. 37.0°C), power off to save battery, and wipe the probe with antiseptic before storing in its case."
    }
];

function renderSim6Step() {
    const s = sim6Steps[sim6CurStep - 1];
    const badge = document.getElementById('sim6StepBadge');
    const graphic = document.getElementById('sim6StepGraphic');
    const prevBtn = document.getElementById('sim6PrevBtn');
    const nextBtn = document.getElementById('sim6NextBtn');
    const dots = document.getElementById('sim6Dots');

    if (badge) badge.textContent = `Step ${s.num} of 5`;
    if (graphic) {
        graphic.innerHTML = `
            <span class="text-3xl">${s.icon}</span>
            <span class="text-sm font-bold text-white block">${s.title}</span>
            <p class="text-xs text-slate-300 max-w-sm leading-relaxed">${s.desc}</p>
        `;
    }

    if (prevBtn) {
        prevBtn.disabled = (sim6CurStep === 1);
        prevBtn.className = (sim6CurStep === 1) ?
            'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-500 text-xs font-bold transition cursor-not-allowed' :
            'px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition';
    }

    if (nextBtn) {
        nextBtn.textContent = (sim6CurStep === 5) ? 'Restart Steps ↺' : 'Next Step →';
    }

    if (dots) {
        dots.innerHTML = sim6Steps.map(step => `
            <span class="w-2 h-2 rounded-full ${step.num === sim6CurStep ? 'bg-indigo-500 ring-2 ring-indigo-300' : 'bg-slate-700'}"></span>
        `).join('');
    }
}

function nextSim6Step() {
    if (sim6CurStep < 5) sim6CurStep++;
    else sim6CurStep = 1;
    renderSim6Step();
}

function prevSim6Step() {
    if (sim6CurStep > 1) {
        sim6CurStep--;
        renderSim6Step();
    }
}

// -------------------------------------------------------------
// Simulator 7: Circadian Body Temperature Rhythm
// -------------------------------------------------------------
function updateSim7Time(hour) {
    const h = parseInt(hour, 10);
    const badge = document.getElementById('sim7TimeBadge');
    const sliderTime = document.getElementById('sim7SliderTime');
    const tempDisp = document.getElementById('sim7TempDisplay');
    const phaseLbl = document.getElementById('sim7PhaseLabel');
    const point = document.getElementById('sim7Point');
    const insight = document.getElementById('sim7Insight');

    const formattedTime = (h < 12 ? (h === 0 ? '12:00 AM' : `${h}:00 AM`) : (h === 12 ? '12:00 PM' : `${h - 12}:00 PM`));
    if (sliderTime) sliderTime.textContent = formattedTime;
    if (badge) badge.textContent = `${formattedTime}`;

    // Circadian calculation
    const rad = ((h - 6) / 24) * 2 * Math.PI;
    const temp = (36.85 + Math.sin(rad - 0.5) * 0.45).toFixed(1);
    if (tempDisp) tempDisp.textContent = `${temp} °C`;

    if (point) {
        const cx = 20 + (h / 24) * 200;
        const cy = 95 - Math.sin(rad - 0.5) * 40;
        point.setAttribute('cx', cx);
        point.setAttribute('cy', cy);
    }

    if (phaseLbl) {
        if (h >= 4 && h <= 8) phaseLbl.textContent = 'Morning Nadir (Lowest)';
        else if (h >= 14 && h <= 18) phaseLbl.textContent = 'Afternoon Peak (Highest)';
        else phaseLbl.textContent = 'Metabolic Baseline';
    }

    if (insight) {
        insight.innerHTML = `At <strong>${formattedTime}</strong>, baseline body temperature is roughly <strong>${temp}°C</strong>. Normal human temperature is a healthy dynamic range, not an unmoving single number.`;
    }
}

// -------------------------------------------------------------
// Simulator 8: Triple Scale Converter
// -------------------------------------------------------------
function updateSim8Scales(celsiusVal) {
    const c = parseFloat(celsiusVal);
    const f = ((c * 9 / 5) + 32).toFixed(1);
    const k = (c + 273.15).toFixed(2);

    const elC = document.getElementById('sim8ValC');
    const elF = document.getElementById('sim8ValF');
    const elK = document.getElementById('sim8ValK');
    const presetLabel = document.getElementById('sim8PresetLabel');

    if (elC) elC.textContent = `${c.toFixed(1)} °C`;
    if (elF) elF.textContent = `${f} °F`;
    if (elK) elK.textContent = `${k} K`;

    if (presetLabel) {
        if (Math.abs(c - 0) < 1) presetLabel.textContent = "Melting Ice / Freezing Water";
        else if (Math.abs(c - 37) < 1) presetLabel.textContent = "Normal Human Body Temperature";
        else if (Math.abs(c - 100) < 1) presetLabel.textContent = "Boiling Point of Pure Water";
        else presetLabel.textContent = `Intermediate Thermal State (${c}°C)`;
    }
}

function setSim8Preset(celsius) {
    const slider = document.getElementById('sim8Slider');
    if (slider) slider.value = celsius;
    updateSim8Scales(celsius);
}

// -------------------------------------------------------------
// Simulator 10: Least Count Calculator
// -------------------------------------------------------------
function setSim10Divisions(divCount) {
    ['10', '5', '50'].forEach(d => {
        const btn = document.getElementById(`sim10Btn-${d}`);
        if (btn) {
            btn.className = (parseInt(d, 10) === divCount) ?
                'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs' :
                'p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs';
        }
    });

    const badge = document.getElementById('sim10LcBadge');
    const calc = document.getElementById('sim10Calculation');
    const svg = document.getElementById('sim10SvgScale');
    const lc = (10 / divCount).toFixed(1);

    if (badge) badge.textContent = `Least Count: ${lc} °C`;
    if (calc) calc.innerHTML = `Calculation: 10°C major span ÷ ${divCount} subdivisions = <strong>${lc} °C per division mark</strong>.`;

    if (svg) {
        let ticks = '';
        const step = 200 / divCount;
        for (let i = 0; i <= divCount; i++) {
            const x = 50 + i * step;
            const h = (i === 0 || i === divCount) ? 24 : (i % 5 === 0 ? 18 : 10);
            ticks += `<line x1="${x}" y1="45" x2="${x}" y2="${45 - h}" stroke="#38bdf8" stroke-width="1.5"/>`;
        }
        svg.innerHTML = `
            <rect x="30" y="45" width="240" height="16" fill="#334155" rx="3"/>
            ${ticks}
            <text x="50" y="75" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">20°C</text>
            <text x="250" y="75" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">30°C</text>
            <text x="150" y="20" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">10°C Major Span</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 11: Parallax Alignment Gauge
// -------------------------------------------------------------
function setSim11Pos(pos) {
    ['A', 'B', 'C'].forEach(p => {
        const btn = document.getElementById(`sim11Btn-${p}`);
        if (btn) {
            btn.className = (p === pos) ?
                'px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-bold transition text-left shadow-lg' :
                'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 font-semibold transition text-left';
        }
    });

    const badge = document.getElementById('sim11AccuracyBadge');
    const reading = document.getElementById('sim11Reading');
    const status = document.getElementById('sim11Status');
    const exp = document.getElementById('sim11Explanation');

    if (pos === 'A') {
        if (badge) { badge.textContent = 'Position A: High Parallax Error'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30'; }
        if (reading) reading.textContent = '42.0 °C';
        if (status) { status.textContent = 'Over-estimated (+2°C)'; status.className = 'text-[10px] font-bold text-rose-400 block mt-1'; }
        if (exp) exp.innerHTML = "Looking downward from above projects the liquid meniscus higher against the background glass scale, causing an artificial +2°C error.";
    } else if (pos === 'C') {
        if (badge) { badge.textContent = 'Position C: Low Parallax Error'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30'; }
        if (reading) reading.textContent = '38.0 °C';
        if (status) { status.textContent = 'Under-estimated (-2°C)'; status.className = 'text-[10px] font-bold text-rose-400 block mt-1'; }
        if (exp) exp.innerHTML = "Looking upward from below projects the liquid meniscus lower against the scale, causing an artificial -2°C error.";
    } else {
        if (badge) { badge.textContent = 'Position B: 90° Perpendicular (Correct)'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'; }
        if (reading) reading.textContent = '40.0 °C';
        if (status) { status.textContent = 'True Temperature'; status.className = 'text-[10px] font-bold text-emerald-400 block mt-1'; }
        if (exp) exp.innerHTML = "Position B: The observer's eye is aligned at the exact horizontal level of the liquid meniscus. Parallax error is completely eliminated.";
    }
}

// -------------------------------------------------------------
// Simulator 12: In-Liquid vs Out-of-Liquid Drop
// -------------------------------------------------------------
function liftSim12Thermometer() {
    const thermo = document.getElementById('sim12ThermoUnit');
    const col = document.getElementById('sim12Column');
    const readout = document.getElementById('sim12Readout');
    const badge = document.getElementById('sim12Badge');
    const state = document.getElementById('sim12State');

    if (thermo) thermo.style.transform = 'translateY(-30px)';
    if (col) col.style.height = '20%';
    if (readout) readout.textContent = '26.0 °C';
    if (badge) { badge.textContent = 'Lifted into Cooler Room Air'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30'; }
    if (state) { state.textContent = 'Corrupted! Dropped in Air'; state.className = 'text-[10px] text-rose-400 font-bold block mt-1 animate-pulse'; }
}

function immerseSim12Thermometer() {
    const thermo = document.getElementById('sim12ThermoUnit');
    const col = document.getElementById('sim12Column');
    const readout = document.getElementById('sim12Readout');
    const badge = document.getElementById('sim12Badge');
    const state = document.getElementById('sim12State');

    if (thermo) thermo.style.transform = 'translateY(0px)';
    if (col) col.style.height = '75%';
    if (readout) readout.textContent = '80.0 °C';
    if (badge) { badge.textContent = 'Immersed in Hot Water'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'; }
    if (state) { state.textContent = 'Accurate In-Liquid Reading'; state.className = 'text-[10px] text-emerald-400 font-bold block mt-1'; }
}

// -------------------------------------------------------------
// Simulator 13: Ice Melting Phase Plateau (Activity 7.5)
// -------------------------------------------------------------
let sim13Heating = false;
function toggleSim13Heating() {
    sim13Heating = !sim13Heating;
    const btn = document.getElementById('sim13HeatBtn');
    const text = document.getElementById('sim13Text');
    const line = document.getElementById('sim13PlateauLine');

    if (sim13Heating) {
        if (btn) { btn.textContent = '🔥 Room Heat Pouring In... (Temp Stays at 0.0°C!)'; btn.className = 'w-full py-2 rounded-xl bg-rose-600 text-white font-bold text-xs shadow-lg animate-pulse'; }
        if (line) line.classList.add('stroke-amber-400');
        if (text) text.innerHTML = "<strong class='text-amber-400'>Latent Heat Action:</strong> Even as heat energy streams in, the thermometer stays firmly locked at 0.0°C! The energy is breaking ice crystal bonds, not raising kinetic temperature.";
    } else {
        if (btn) { btn.textContent = '🔥 Apply Continuous Room Heat'; btn.className = 'w-full py-2 rounded-xl bg-cyan-600 text-white font-bold text-xs shadow-lg transition'; }
        if (line) line.classList.remove('stroke-amber-400');
        if (text) text.innerHTML = "Heat from the room is absorbed as latent heat of fusion. Temperature remains locked at 0°C until the final ice crystal liquefies.";
    }
}

// -------------------------------------------------------------
// Simulator 14: Boiling Water Phase Plateau (Activity 7.6)
// -------------------------------------------------------------
function boostSim14Flame() {
    const temp = document.getElementById('sim14Temp');
    const insight = document.getElementById('sim14Insight');
    const btn = document.getElementById('sim14BoostBtn');

    if (btn) btn.className = 'flex-1 py-2 rounded-xl bg-rose-700 text-white font-bold text-xs shadow-lg animate-pulse';
    if (temp) temp.textContent = '100.0 °C';
    if (insight) {
        insight.innerHTML = "<strong class='text-rose-400'>Maximum Flame Test:</strong> The burner flame is blazing at 1000°C, yet the boiling water stays strictly at <strong>100.0°C</strong>! All extra heat rapidly converts water into steam (latent heat of vaporization).";
    }
}

function resetSim14() {
    const btn = document.getElementById('sim14BoostBtn');
    const insight = document.getElementById('sim14Insight');
    if (btn) btn.className = 'flex-1 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-lg transition';
    if (insight) insight.innerHTML = "Even with maximum burner power, open water cannot exceed 100°C. Extra heat becomes latent heat of vaporization.";
}

// -------------------------------------------------------------
// Simulator 16: Anna Mani Meteorological Station
// -------------------------------------------------------------
const sim16Tools = {
    ozone: {
        title: "The Indian Ozonesonde",
        desc: "Designed and standardized by Anna Mani at IMD Pune. Carried by high-altitude sounding balloons to measure stratospheric ozone layers up to 35 km altitude.",
        svg: `
            <svg width="200" height="120" viewBox="0 0 200 120">
                <circle cx="100" cy="40" r="28" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <line x1="100" y1="68" x2="100" y2="90" stroke="#94a3b8" stroke-width="1.5"/>
                <rect x="85" y="90" width="30" height="22" rx="3" fill="#3b82f6" stroke="#1d4ed8"/>
                <text x="100" y="104" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Sonde</text>
            </svg>
        `
    },
    solar: {
        title: "National Solar Radiation Pyranometer",
        desc: "Anna Mani established India's first network of solar radiation monitoring stations, providing the empirical solar mapping that guides modern mega-solar parks.",
        svg: `
            <svg width="200" height="120" viewBox="0 0 200 120">
                <circle cx="100" cy="65" r="30" fill="rgba(250, 204, 21, 0.2)" stroke="#facc15" stroke-width="2"/>
                <ellipse cx="100" cy="75" rx="40" ry="12" fill="#334155"/>
                <polygon points="100,20 95,35 105,35" fill="#facc15"/>
                <polygon points="65,40 78,48 72,55" fill="#facc15"/>
                <polygon points="135,40 122,48 128,55" fill="#facc15"/>
            </svg>
        `
    },
    wind: {
        title: "Cup Anemometer & Wind Vane Network",
        desc: "Anna Mani installed over 700 wind-monitoring towers across India to survey wind velocities, establishing the scientific foundation of India's wind energy sector.",
        svg: `
            <svg width="200" height="120" viewBox="0 0 200 120">
                <rect x="98" y="40" width="4" height="70" fill="#64748b"/>
                <circle cx="100" cy="40" r="5" fill="#38bdf8"/>
                <line x1="60" y1="40" x2="140" y2="40" stroke="#38bdf8" stroke-width="3"/>
                <path d="M 60,35 A 10,10 0 0,0 60,45 Z" fill="#ef4444"/>
                <path d="M 140,35 A 10,10 0 0,1 140,45 Z" fill="#ef4444"/>
            </svg>
        `
    }
};

function selectSim16Tool(tool) {
    ['ozone', 'solar', 'wind'].forEach(t => {
        const btn = document.getElementById(`sim16Btn-${t}`);
        if (btn) {
            btn.className = (t === tool) ?
                'p-2 rounded-xl bg-indigo-600 text-white font-bold text-xs' :
                'p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs';
        }
    });

    const d = sim16Tools[tool];
    const display = document.getElementById('sim16Display');
    const notes = document.getElementById('sim16Notes');

    if (display) display.innerHTML = d.svg;
    if (notes) notes.innerHTML = `<strong>${d.title}:</strong> ${d.desc}`;
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    testSim1Method('tool');
    initSim3Particles();
    renderSim6Step();
    updateSim7Time(6);
    updateSim8Scales(37);
    setSim10Divisions(10);
    setSim11Pos('B');
    immerseSim12Thermometer();
    selectSim16Tool('ozone');

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''


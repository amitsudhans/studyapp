"""
Interactive JavaScript for Class 6 Science Chapter 11: Nature's Treasures
Features sentence-by-sentence Web Speech API with Indian Male voice priority, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure clean Unicode.
"""

JS_CODE = '''
// Science Chapter 11 Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis Engine (Sentence-by-Sentence Queue with Indian Male Voice Selection)
let isSpeaking = false;
let currentSpeakingSlide = null;
let speechQueue = [];
let speechIndex = 0;
let selectedMaleVoice = null;

function getIndianMaleVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const femaleKeywords = ['female', 'zira', 'jenny', 'aria', 'samantha', 'victoria', 'karen', 'susan', 'neerja', 'heera', 'hazel', 'catherine', 'linda', 'eva', 'ava', 'siri', 'swara', 'veena'];
    const isFemale = (v) => {
        const name = (v.name || '').toLowerCase();
        return femaleKeywords.some(fk => name.includes(fk));
    };

    const indianMaleKeywords = ['rishi', 'ravi', 'pradeep', 'madhav', 'en-in', 'hindi', 'india'];
    const generalMaleKeywords = ['male', 'david', 'mark', 'george', 'daniel', 'guy', 'stefan', 'oliver', 'arthur', 'james', 'richard', 'brian', 'sean', 'alex', 'fred', 'neil'];

    // 1. Prioritize Indian English male voices
    const inVoices = voices.filter(v => (v.lang && (v.lang.toLowerCase() === 'en-in' || v.lang.toLowerCase().startsWith('en_in'))) || (v.name && v.name.toLowerCase().includes('india')));
    for (const mk of indianMaleKeywords) {
        const match = inVoices.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemale(v));
        if (match) return match;
    }
    const anyInMale = inVoices.find(v => !isFemale(v));
    if (anyInMale) return anyInMale;

    // 2. English male voices
    const enVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
    for (const mk of generalMaleKeywords) {
        const match = enVoices.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemale(v));
        if (match) return match;
    }

    // 3. Any English voice with male gender or non-female
    const maleGender = enVoices.find(v => v.gender === 'male' && !isFemale(v));
    if (maleGender) return maleGender;

    const nonFemale = enVoices.find(v => !isFemale(v));
    if (nonFemale) return nonFemale;

    return voices[0] || null;
}

if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        selectedMaleVoice = getIndianMaleVoice();
    };
    selectedMaleVoice = getIndianMaleVoice();
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
    utterance.pitch = 0.88; // Deep, resonant Indian baritone male tone

    if (!selectedMaleVoice) {
        selectedMaleVoice = getIndianMaleVoice();
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

    // Split text into natural sentences
    const sentences = fullText.match(/[^.!?]+[.!?]+/g) || [fullText];
    speechQueue = sentences.map(s => s.trim()).filter(s => s.length > 0);
    speechIndex = 0;
    isSpeaking = true;
    currentSpeakingSlide = slideNo;

    updateAllAudioButtons();
    speakNextSentence();
}

function toggleCurrentSlideLecture() {
    if (currentSlide > 16) {
        alert("Mastery challenges are interactive exercises and do not have an audio lecture.");
        return;
    }
    const textElem = document.getElementById(`slide-spoken-text-${currentSlide}`);
    if (textElem) {
        startLectureSpeech(textElem.textContent, currentSlide);
    }
}

function updateAllAudioButtons() {
    for (let i = 1; i <= 16; i++) {
        const btn = document.getElementById(`slide-audio-btn-${i}`);
        const badge = document.getElementById(`slide-audio-badge-${i}`);
        if (btn) {
            if (isSpeaking && currentSpeakingSlide === i) {
                btn.innerHTML = '<span>⏹</span><span>Pause Lecture</span>';
                btn.className = "px-3 py-1.5 rounded-xl bg-amber-500/20 text-amber-300 text-xs font-bold flex items-center space-x-1.5 border border-amber-500/30 transition shadow-sm";
                if (badge) {
                    badge.textContent = "Speaking...";
                    badge.className = "px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30 animate-pulse";
                }
            } else {
                btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
                btn.className = "px-3 py-1.5 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 text-xs font-bold flex items-center space-x-1.5 border border-indigo-500/30 transition shadow-sm";
                if (badge) {
                    badge.textContent = "Audio Lecture Ready";
                    badge.className = "px-2 py-0.5 rounded text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
                }
            }
        }
    }

    const globalBtn = document.getElementById('globalAudioBtn');
    if (globalBtn) {
        if (isSpeaking) {
            globalBtn.innerHTML = '<span>⏹</span><span>Pause Audio</span>';
            globalBtn.className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500/20 text-amber-300 hover:bg-amber-500/30 border border-amber-500/30 flex items-center space-x-1.5 transition";
        } else {
            globalBtn.innerHTML = '<span>🔊</span><span>Listen to Lecture</span>';
            globalBtn.className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/30 border border-indigo-500/30 flex items-center space-x-1.5 transition";
        }
    }
}

// Slide Navigation
function goToSlide(slideNo) {
    if (slideNo < 1 || slideNo > totalSlides) return;
    stopSpeech();

    // Hide all slides
    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) el.style.display = 'none';
    }

    // Show target slide
    const target = document.getElementById(`slide-${slideNo}`);
    if (target) {
        target.style.display = 'block';
    }

    currentSlide = slideNo;

    // Update Counter & Select
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${currentSlide} / ${totalSlides}`;

    const select = document.getElementById('slideSelect');
    if (select) select.value = currentSlide;

    // Prev / Next button states
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        prevBtn.style.opacity = (currentSlide === 1) ? '0.4' : '1';
    }

    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
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

// Checkpoint Feedback
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const fb = document.getElementById(`cp-feedback-${cpId}`);
    if (!fb) return;

    if (selectedIdx === correctIdx) {
        fb.className = "p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-200 space-y-1";
        fb.innerHTML = `<div><strong>✓ Correct!</strong></div><div>${explanation}</div>`;
    } else {
        fb.className = "p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-xs text-rose-200 space-y-1";
        fb.innerHTML = `<div><strong>✗ Incorrect. Try reviewing the principle.</strong></div><div>${explanation}</div>`;
    }
    fb.classList.remove('hidden');
}

// Mastery Quiz Selection & Feedback
function selectQuizOption(qId, selectedIdx, correctIdx, title, question, explanation) {
    const fb = document.getElementById(`q-fb-${qId}`);
    const solBtn = document.getElementById(`q-sol-btn-${qId}`);
    if (!fb) return;

    if (selectedIdx === correctIdx) {
        fb.className = "p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-200 space-y-1";
        fb.innerHTML = `<div><strong>✓ Correct!</strong></div><div>${explanation}</div>`;
    } else {
        fb.className = "p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-xs text-rose-200 space-y-1";
        fb.innerHTML = `<div><strong>✗ Incorrect.</strong></div><div>${explanation}</div>`;
    }
    fb.classList.remove('hidden');

    if (solBtn) {
        solBtn.classList.remove('hidden');
        solBtn.classList.add('inline-flex');
    }
}

// Solution Modal Handlers
function openSolutionModal(title, question, solutionHtml) {
    const modal = document.getElementById('solutionModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalQuestion = document.getElementById('modalQuestion');
    const modalSolution = document.getElementById('modalSolution');

    if (modal && modalTitle && modalQuestion && modalSolution) {
        modalTitle.textContent = title;
        modalQuestion.innerHTML = question;
        modalSolution.innerHTML = solutionHtml;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    }
}

// Simulator Event Handlers

// Sim 1: Nature's Treasury
function inspectGift(gift) {
    const focusText = document.getElementById('sim1-focus-text');
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');

    if (gift === 'air') {
        if (focusText) focusText.textContent = "Gift: Pure Mountain Air";
        if (badge) badge.textContent = "Bounty: 78% N₂ + 21% O₂";
        if (desc) desc.innerHTML = "<strong>Fresh Air:</strong> Mountain forests continually replenish atmospheric oxygen and filter particulate dust.";
    } else if (gift === 'water') {
        if (focusText) focusText.textContent = "Gift: Sweet Spring Water";
        if (badge) badge.textContent = "Bounty: Natural Aquifers";
        if (desc) desc.innerHTML = "<strong>Sweet Water:</strong> Forest soils act as giant sponges, purifying monsoon rainwater into perennial crystal streams.";
    } else if (gift === 'soil') {
        if (focusText) focusText.textContent = "Gift: Fertile Topsoil";
        if (badge) badge.textContent = "Bounty: Humus & Minerals";
        if (desc) desc.innerHTML = "<strong>Fertile Soil:</strong> Centimeter by centimeter, centuries of rock weathering and decaying leaf mulch produce living topsoil.";
    } else if (gift === 'sun') {
        if (focusText) focusText.textContent = "Gift: Radiant Solar Light";
        if (badge) badge.textContent = "Bounty: Primary Energy";
        if (desc) desc.innerHTML = "<strong>Sunlight:</strong> Powers green photosynthesis in the dense forest canopy, sustaining all herbivores and predators.";
    }
}

// Sim 2: Breath Hold & Saturation
let breathInterval = null;
let breathSeconds = 0;
let isHoldingBreath = false;

function toggleHoldBreath() {
    const btn = document.getElementById('sim2-btn');
    const lungL = document.getElementById('sim2-lung-l');
    const lungR = document.getElementById('sim2-lung-r');
    const o2Bar = document.getElementById('sim2-o2-bar');
    const o2Val = document.getElementById('sim2-o2-val');
    const timer = document.getElementById('sim2-timer');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (!isHoldingBreath) {
        isHoldingBreath = true;
        breathSeconds = 0;
        if (btn) btn.textContent = "🛑 Stop & Inhale (Gasp for Air)";
        if (badge) {
            badge.textContent = "Holding Breath: Hypoxia Alert!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse";
        }
        if (lungL) lungL.style.fill = "#9333ea";
        if (lungR) lungR.style.fill = "#9333ea";

        breathInterval = setInterval(() => {
            breathSeconds += 2;
            if (timer) timer.textContent = `${breathSeconds}s`;

            const sat = Math.max(75, 99 - Math.floor(breathSeconds * 0.8));
            if (o2Val) o2Val.textContent = `${sat}%`;
            if (o2Bar) {
                const height = Math.max(10, Math.floor((sat / 100) * 70));
                o2Bar.setAttribute('height', height);
            }

            if (breathSeconds >= 35) {
                if (desc) {
                    desc.innerHTML = "<strong class='text-rose-400'>Biological Limit Reached:</strong> Brainstem forces diaphragm contraction to resume immediate oxygen intake!";
                }
            }
        }, 500);
    } else {
        resetBreathing();
    }
}

function resetBreathing() {
    clearInterval(breathInterval);
    isHoldingBreath = false;
    breathSeconds = 0;

    const btn = document.getElementById('sim2-btn');
    const lungL = document.getElementById('sim2-lung-l');
    const lungR = document.getElementById('sim2-lung-r');
    const o2Bar = document.getElementById('sim2-o2-bar');
    const o2Val = document.getElementById('sim2-o2-val');
    const timer = document.getElementById('sim2-timer');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (btn) btn.textContent = "🫁 Hold Breath (Pinch Nostrils)";
    if (timer) timer.textContent = "0s";
    if (o2Val) o2Val.textContent = "99%";
    if (o2Bar) o2Bar.setAttribute('height', '70');
    if (lungL) lungL.style.fill = "#f43f5e";
    if (lungR) lungR.style.fill = "#f43f5e";
    if (badge) {
        badge.textContent = "Breathing Normal";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
    }
    if (desc) {
        desc.innerHTML = "Click <strong>Hold Breath</strong>: blood oxygen saturation rapidly drops, triggering an overwhelming biological urge to breathe within 30-40 seconds!";
    }
}

// Sim 3: Atmospheric Gas Mixture
function isolateGas(gas) {
    const badge = document.getElementById('sim3-badge');
    const desc = document.getElementById('sim3-desc');

    if (gas === 'nitrogen') {
        if (badge) badge.textContent = "Isolate: Nitrogen (78%)";
        if (desc) desc.innerHTML = "<strong>Nitrogen (78%):</strong> Moderates burning, dilutes oxygen, and is fixed by soil microbes into amino acids and proteins.";
    } else if (gas === 'oxygen') {
        if (badge) badge.textContent = "Isolate: Oxygen (21%)";
        if (desc) desc.innerHTML = "<strong>Oxygen (21%):</strong> Required for cellular respiration in living organisms and supports fuel combustion.";
    } else if (gas === 'co2') {
        if (badge) badge.textContent = "Isolate: Carbon Dioxide (0.04%)";
        if (desc) desc.innerHTML = "<strong>Carbon Dioxide (0.04%):</strong> Absorbed by plant chloroplasts during photosynthesis to produce glucose and emit oxygen.";
    }
}

// Sim 4: Wind Speed & Power
function setWindSpeed(val) {
    const speed = parseInt(val, 10);
    const speedVal = document.getElementById('sim4-speed-val');
    const badge = document.getElementById('sim4-badge');
    const power = document.getElementById('sim4-power');
    const blades = document.getElementById('sim4-blades');
    const firki = document.getElementById('sim4-firki');

    if (speedVal) speedVal.textContent = `${speed} km/h`;
    if (badge) badge.textContent = `Wind Speed: ${speed} km/h`;

    const watts = Math.floor(speed * speed * 1.8);
    if (power) power.textContent = `Output: ${watts} kW`;

    const animDuration = (speed === 0) ? '0s' : `${Math.max(0.3, 3 - (speed / 20))}s`;
    if (blades) blades.style.animationDuration = animDuration;
    if (firki) firki.style.animationDuration = `${Math.max(0.15, 1.5 - (speed / 30))}s`;
}

// Sim 5: 10-Liter Bucket Analogy
function highlightWaterFraction(fraction) {
    const badge = document.getElementById('sim5-badge');
    const desc = document.getElementById('sim5-desc');

    if (fraction === 'all') {
        if (badge) badge.textContent = "10L Bucket: Saline Oceans (97.5%)";
        if (desc) desc.innerHTML = "<strong>Saline Oceans (97.5%):</strong> Contains 35 grams of salt per liter. Direct human consumption or crop irrigation causes fatal dehydration.";
    } else if (fraction === 'fresh') {
        if (badge) badge.textContent = "250mL Cup: Total Freshwater (2.5%)";
        if (desc) desc.innerHTML = "<strong>Total Freshwater (2.5%):</strong> Most is locked in polar ice caps (~69%) or buried deep in underground aquifers (~30%).";
    } else if (fraction === 'drop') {
        if (badge) badge.textContent = "1 Drop: Usable Freshwater (< 1%)";
        if (desc) desc.innerHTML = "<strong>Accessible Surface Water:</strong> Rivers, lakes, and freshwater streams constitute barely one drop of the 10-liter bucket!";
    }
}

// Sim 6: Leaky Tap Repair
function repairTap(isRepaired) {
    const stream = document.getElementById('sim6-water-stream');
    const valve = document.getElementById('sim6-valve');
    const liters = document.getElementById('sim6-liters');
    const cost = document.getElementById('sim6-cost');
    const action = document.getElementById('sim6-action');
    const badge = document.getElementById('sim6-badge');
    const desc = document.getElementById('sim6-desc');

    if (isRepaired) {
        if (stream) stream.style.display = 'none';
        if (valve) valve.style.transform = "rotate(90deg)";
        if (liters) {
            liters.textContent = "0 L/day";
            liters.style.color = "#4ade80";
        }
        if (cost) cost.textContent = "10,950 L Saved / year!";
        if (action) {
            action.textContent = "✓ Washer Replaced!";
            action.style.color = "#4ade80";
        }
        if (badge) {
            badge.textContent = "Tap Sealed: 0 Waste";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Water Conserved:</strong> Fixing a single leaking tap washer preserves thousands of liters of treated freshwater annually.";
        }
    } else {
        if (stream) stream.style.display = 'block';
        if (valve) valve.style.transform = "rotate(0deg)";
        if (liters) {
            liters.textContent = "30 L/day";
            liters.style.color = "#f43f5e";
        }
        if (cost) cost.textContent = "10,950 L / year";
        if (action) {
            action.textContent = "Fix washer now!";
            action.style.color = "#f59e0b";
        }
        if (badge) {
            badge.textContent = "Tap Leaking: Wasting Water";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (desc) {
            desc.innerHTML = "A faucet dripping once per second squanders over 30 liters daily. Fixing leaky washers saves over 10,000 liters every year!";
        }
    }
}

// Sim 7: Traditional Stepwell (Bawadi / Vav)
function setStepwellSeason(season) {
    const water = document.getElementById('sim7-water');
    const rain = document.getElementById('sim7-rain');
    const badge = document.getElementById('sim7-badge');
    const desc = document.getElementById('sim7-desc');

    if (season === 'monsoon') {
        if (water) {
            water.setAttribute('y', '60');
            water.setAttribute('height', '120');
        }
        if (rain) rain.style.opacity = '1';
        if (badge) {
            badge.textContent = "Season: Monsoon Refill";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Monsoon Inflow:</strong> Stone tiers funnel heavy rains into the central shaft, recharging subterranean aquifers for miles around.";
        }
    } else {
        if (water) {
            water.setAttribute('y', '135');
            water.setAttribute('height', '45');
        }
        if (rain) rain.style.opacity = '0';
        if (badge) {
            badge.textContent = "Season: Summer Drought";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Summer Access:</strong> Communities descend stone steps to reach cool subterranean water stored from the previous monsoon.";
        }
    }
}

// Sim 8: Solar Engine
function toggleSolarEngine(isActive) {
    const sun = document.getElementById('sim8-sun');
    const rays = document.getElementById('sim8-rays');
    const badge = document.getElementById('sim8-badge');
    const desc = document.getElementById('sim8-desc');

    if (isActive) {
        if (sun) sun.setAttribute('fill', '#f59e0b');
        if (rays) rays.style.opacity = '0.8';
        if (badge) {
            badge.textContent = "Solar Drive: Maximum";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Solar Powerhouse:</strong> Sunlight drives ocean evaporation, powers atmospheric wind convection, and fuels green photosynthesis.";
        }
    } else {
        if (sun) sun.setAttribute('fill', '#334155');
        if (rays) rays.style.opacity = '0';
        if (badge) {
            badge.textContent = "Solar Drive: Zero (Freeze)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300";
        }
        if (desc) {
            desc.innerHTML = "<strong>Absolute Cold:</strong> Without solar radiation, planetary temperatures drop to -270°C, oceans freeze solid, and all food production ceases.";
        }
    }
}

// Sim 9: Solar PV vs Cooker
function setSolarTech(tech) {
    const pv = document.getElementById('sim9-pv-group');
    const cooker = document.getElementById('sim9-cooker-group');
    const badge = document.getElementById('sim9-badge');
    const desc = document.getElementById('sim9-desc');

    if (tech === 'pv') {
        if (pv) pv.style.opacity = '1';
        if (cooker) cooker.style.opacity = '0';
        if (badge) badge.textContent = "Mode: Solar PV Panel";
        if (desc) desc.textContent = "Silicon semiconductor cells convert sunlight photons directly into clean electrical current for homes and pumps.";
    } else {
        if (pv) pv.style.opacity = '0';
        if (cooker) cooker.style.opacity = '1';
        if (badge) badge.textContent = "Mode: Solar Box Cooker";
        if (desc) desc.textContent = "Black-painted insulated interior and glass lid create a miniature greenhouse, heating pots to 120°C–140°C with zero firewood or smoke.";
    }
}

// Sim 10: Forest Humus Recycling
function triggerLeafFall() {
    const litter = document.getElementById('sim10-leaf-litter');
    const badge = document.getElementById('sim10-badge');
    const desc = document.getElementById('sim10-desc');

    if (litter) litter.style.transform = "translateY(2px)";
    if (badge) badge.textContent = "Humus Formation Active";
    if (desc) desc.innerHTML = "<strong>Natural Nutrient Cycle:</strong> Fallen foliage decomposes into rich, dark humus, replenishing soil nitrates and minerals naturally.";
}

function toggleDeforestation(isDeforested) {
    const badge = document.getElementById('sim10-badge');
    const desc = document.getElementById('sim10-desc');

    if (isDeforested) {
        if (badge) {
            badge.textContent = "Deforestation Hazard!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse";
        }
        if (desc) {
            desc.innerHTML = "<strong>Erosion Crisis:</strong> Clear-cutting trees destroys the root anchor, triggering fatal mudslides and washing away precious topsoil.";
        }
    }
}

// Sim 11: Chipko Movement
function setChipkoMode(mode) {
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');
    const protester = document.getElementById('sim11-protester');

    if (mode === 'hug') {
        if (protester) protester.style.opacity = '1';
        if (badge) badge.textContent = "Action: Hugging the Ash Tree";
        if (desc) desc.textContent = "Gaura Devi and village women shielded forest trees with their bodies, forcing commercial contractors to withdraw their axes.";
    } else {
        if (protester) protester.style.opacity = '0.5';
        if (badge) badge.textContent = "Festival: Van Mahotsav Planting";
        if (desc) desc.textContent = "During the first week of July, millions of young saplings are planted across India to catch seasonal monsoon rains.";
    }
}

// Sim 12: Earthworm Soil
function toggleEarthworm(isBurrowing) {
    const worm = document.getElementById('sim12-worm-group');
    const badge = document.getElementById('sim12-badge');
    const desc = document.getElementById('sim12-desc');

    if (isBurrowing) {
        if (worm) worm.style.opacity = '1';
        if (badge) badge.textContent = "Aeration: Active Burrowing";
        if (desc) desc.innerHTML = "<strong>Farmer's Ally:</strong> Earthworms tunnel subterranean air channels and enrich the soil with fertile vermicompost.";
    } else {
        if (worm) worm.style.opacity = '0';
        if (badge) badge.textContent = "Soil: Compacted";
        if (desc) desc.innerHTML = "Without earthworms, soil becomes dense and compacted, restricting root respiration and water drainage.";
    }
}

// Sim 13: Mineral to Metal
function setMetalSample(sample) {
    const orePoly = document.getElementById('sim13-ore-poly');
    const oreLabel = document.getElementById('sim13-ore-label');
    const ingotRect = document.getElementById('sim13-ingot-rect');
    const metalLabel = document.getElementById('sim13-metal-label');
    const badge = document.getElementById('sim13-badge');
    const desc = document.getElementById('sim13-desc');

    if (sample === 'aluminium') {
        if (orePoly) orePoly.setAttribute('fill', '#b45309');
        if (oreLabel) oreLabel.textContent = "Bauxite Ore";
        if (ingotRect) ingotRect.setAttribute('fill', '#cbd5e1');
        if (metalLabel) metalLabel.textContent = "Aluminium Ingot";
        if (badge) badge.textContent = "Display: Bauxite ➔ Aluminium";
        if (desc) desc.textContent = "Hydrated aluminium oxide (bauxite) is refined into lightweight, rust-resistant aluminium metal for aircraft and utensils.";
    } else if (sample === 'iron') {
        if (orePoly) orePoly.setAttribute('fill', '#881337');
        if (oreLabel) oreLabel.textContent = "Haematite Ore";
        if (ingotRect) ingotRect.setAttribute('fill', '#475569');
        if (metalLabel) metalLabel.textContent = "Structural Steel/Iron";
        if (badge) badge.textContent = "Display: Haematite ➔ Iron";
        if (desc) desc.textContent = "Iron oxide ore (haematite) is smelted with coke in blast furnaces to produce structural steel for bridges and buildings.";
    } else if (sample === 'copper') {
        if (orePoly) orePoly.setAttribute('fill', '#713f12');
        if (oreLabel) oreLabel.textContent = "Chalcopyrite Ore";
        if (ingotRect) ingotRect.setAttribute('fill', '#f97316');
        if (metalLabel) metalLabel.textContent = "Copper Wiring";
        if (badge) badge.textContent = "Display: Chalcopyrite ➔ Copper";
        if (desc) desc.textContent = "Copper sulfide ores are smelted into highly conductive copper for city electric power grids and motor windings.";
    }
}

// Sim 14: Fossil Fuel Era
function setFossilEra(era) {
    const badge = document.getElementById('sim14-badge');
    const desc = document.getElementById('sim14-desc');

    if (era === 'prehistoric') {
        if (badge) badge.textContent = "Era: 300 Million Years Ago";
        if (desc) desc.innerHTML = "<strong>Prehistoric Swamp Forests:</strong> Giant ferns and marine plankton died and settled beneath stagnant anaerobic mud.";
    } else {
        if (badge) badge.textContent = "Era: Modern Hydrocarbon Trap";
        if (desc) desc.innerHTML = "<strong>Buried Reservoirs:</strong> Hundreds of millions of years of geothermal heat compressed organic biomass into coal, oil, and gas.";
    }
}

// Sim 15: Resource Classifier
function testResource(res) {
    const badge = document.getElementById('sim15-badge');
    const desc = document.getElementById('sim15-desc');

    if (res === 'sun') {
        if (badge) badge.textContent = "Sunlight: 100% Renewable";
        if (desc) desc.innerHTML = "<strong class='text-emerald-400'>Renewable:</strong> Continuous thermonuclear fusion ensures sunlight remains an inexhaustible natural treasure.";
    } else if (res === 'petrol') {
        if (badge) badge.textContent = "Petroleum: Non-Renewable";
        if (desc) desc.innerHTML = "<strong class='text-rose-400'>Non-Renewable:</strong> Takes 300 million years to form; current extraction will permanently deplete known reserves.";
    } else if (res === 'forest') {
        if (badge) badge.textContent = "Forests: Conditionally Renewable";
        if (desc) desc.innerHTML = "<strong class='text-emerald-400'>Renewable:</strong> Trees naturally regenerate via seed dispersal, provided logging rates do not exceed replanting.";
    }
}

// Sim 16: Balance Scale (Need vs Greed)
function setBalanceState(state) {
    const beam = document.getElementById('sim16-beam');
    const badge = document.getElementById('sim16-badge');
    const desc = document.getElementById('sim16-desc');

    if (state === 'need') {
        if (beam) beam.style.transform = "rotate(0deg)";
        if (badge) {
            badge.textContent = "Mode: Sustainable Need";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Gandhian Harmony:</strong> Resource consumption balances within Earth's regenerative limits, preserving nature's treasures for posterity.";
        }
    } else {
        if (beam) beam.style.transform = "rotate(18deg)";
        if (badge) {
            badge.textContent = "Mode: Over-Exploitation (Greed)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong class='text-rose-400'>Depletion Crisis:</strong> Excessive greed, wastefulness, and pollution overwhelm Earth's ecological capacity, triggering resource collapse.";
        }
    }
}

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
    if ('speechSynthesis' in window) {
        selectedMaleVoice = getIndianMaleVoice();
    }
});
'''


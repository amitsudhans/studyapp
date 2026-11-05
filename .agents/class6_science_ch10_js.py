"""
Interactive JavaScript for Class 6 Science Chapter 10: Living Creatures: Exploring their Characteristics
Features sentence-by-sentence Web Speech API with Indian Male voice priority, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure clean Unicode.
"""

JS_CODE = '''
// Science Chapter 10 Interactive JavaScript
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

// Sim 1: Snail Shell vs Living Snail
function setSnailState(state) {
    const body = document.getElementById('sim1-snail-body');
    const badge = document.getElementById('sim1-badge');
    const svgText = document.getElementById('sim1-svg-text');
    const desc = document.getElementById('sim1-desc');

    if (state === 'living') {
        if (body) body.style.opacity = '1';
        if (badge) {
            badge.textContent = "Viewing: Living Snail";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (svgText) {
            svgText.textContent = "Living Snail: Gliding & Sensing";
            svgText.setAttribute('fill', '#4ade80');
        }
        if (desc) {
            desc.innerHTML = "<strong>Living Snail:</strong> Soft muscular foot expands, tentacles perceive light and vibrations, and slime trail facilitates forward locomotion.";
        }
    } else {
        if (body) body.style.opacity = '0';
        if (badge) {
            badge.textContent = "Viewing: Empty Shell";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300";
        }
        if (svgText) {
            svgText.textContent = "Empty Shell: Lifeless";
            svgText.setAttribute('fill', '#94a3b8');
        }
        if (desc) {
            desc.innerHTML = "<strong>Empty Shell:</strong> Lacking living tissue, this calcium structure undergoes no metabolism, respiration, growth, or reproduction.";
        }
    }
}

// Sim 2: Drosera Sundew Trap
let droseraTrapped = false;
function triggerDroseraTrap() {
    const fly = document.getElementById('sim2-fly');
    const leftT = document.getElementById('tentacles-left');
    const rightT = document.getElementById('tentacles-right');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (fly) fly.style.transform = "translate(160px, 95px) rotate(15deg)";
    if (leftT) leftT.style.transform = "rotate(35deg)";
    if (rightT) rightT.style.transform = "rotate(-35deg)";

    if (badge) {
        badge.textContent = "Prey Trapped!";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse";
    }
    if (desc) {
        desc.innerHTML = "<strong>Thigmonasty:</strong> The insect's struggles trigger sensory hairs, causing glandular tentacles to bend inwards and secrete digestive enzymes.";
    }
    droseraTrapped = true;
}

function resetDroseraTrap() {
    const fly = document.getElementById('sim2-fly');
    const leftT = document.getElementById('tentacles-left');
    const rightT = document.getElementById('tentacles-right');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (fly) fly.style.transform = "translate(160px, 20px) rotate(0deg)";
    if (leftT) leftT.style.transform = "rotate(0deg)";
    if (rightT) rightT.style.transform = "rotate(0deg)";

    if (badge) {
        badge.textContent = "Trap Primed";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
    }
    if (desc) {
        desc.innerHTML = "Click <strong>Insect Lands</strong> to see the fly adhere to sticky glandular mucilage, triggering rapid inward curling of sensory tentacles.";
    }
    droseraTrapped = false;
}

// Sim 3: Stoma Simulator
function setStomaState(isOpen) {
    const pore = document.getElementById('stoma-pore');
    const leftG = document.getElementById('guard-left');
    const rightG = document.getElementById('guard-right');
    const arrows = document.getElementById('gas-arrows');
    const status = document.getElementById('sim3-status');
    const desc = document.getElementById('sim3-desc');

    if (isOpen) {
        if (pore) pore.setAttribute('rx', '18');
        if (leftG) leftG.setAttribute('d', 'M 160,35 C 110,40 100,160 160,165 C 130,140 130,60 160,35 Z');
        if (rightG) rightG.setAttribute('d', 'M 160,35 C 210,40 220,160 160,165 C 190,140 190,60 160,35 Z');
        if (arrows) arrows.style.opacity = '1';
        if (status) {
            status.textContent = "Day: Stoma Open";
            status.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Turgid Guard Cells:</strong> High turgor curves guard cells outward, opening the stoma for active oxygen and carbon dioxide diffusion.";
        }
    } else {
        if (pore) pore.setAttribute('rx', '2');
        if (leftG) leftG.setAttribute('d', 'M 160,35 C 135,40 135,160 160,165 C 150,140 150,60 160,35 Z');
        if (rightG) rightG.setAttribute('d', 'M 160,35 C 185,40 185,160 160,165 C 170,140 170,60 160,35 Z');
        if (arrows) arrows.style.opacity = '0';
        if (status) {
            status.textContent = "Night: Stoma Closed";
            status.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300";
        }
        if (desc) {
            desc.innerHTML = "<strong>Flaccid Guard Cells:</strong> Loss of water pressure causes guard cells to straighten, closing the stoma to preserve internal moisture.";
        }
    }
}

// Sim 4: Guttation
function toggleGuttation(isActive) {
    const droplets = document.getElementById('sim4-droplets');
    const badge = document.getElementById('sim4-badge');
    const desc = document.getElementById('sim4-desc');

    if (isActive) {
        if (droplets) droplets.style.opacity = '1';
        if (badge) {
            badge.textContent = "Early Dawn: Guttation Active";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Hydathode Exudation:</strong> Night root pressure forces xylem sap out as guttation droplets containing dissolved mineral wastes.";
        }
    } else {
        if (droplets) droplets.style.opacity = '0';
        if (badge) {
            badge.textContent = "Midday: Transpiration Dominates";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Midday Sunlight:</strong> High ambient heat accelerates transpiration, evaporating water before liquid droplets can accumulate.";
        }
    }
}

// Sim 5: Mimosa Touch-Me-Not
let mimosaFolded = false;
function touchMimosa() {
    const branch = document.getElementById('sim5-branch');
    const badge = document.getElementById('sim5-badge');
    const desc = document.getElementById('sim5-desc');
    const pulvinus = document.getElementById('sim5-pulvinus');

    if (branch) branch.style.transform = "rotate(38deg)";
    if (pulvinus) pulvinus.setAttribute('ry', '3'); // Deflated pulvinus

    const pairs = document.querySelectorAll('.mimosa-pair');
    pairs.forEach(p => {
        p.style.transform = "scaleY(0.2)";
    });

    if (badge) {
        badge.textContent = "Stimulus: Leaflets Folded";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
    }
    if (desc) {
        desc.innerHTML = "<strong>Thigmonasty:</strong> Mechanical stimulus caused instantaneous potassium and water efflux from the lower pulvinus, collapsing leaflet turgor!";
    }
    mimosaFolded = true;
}

function recoverMimosa() {
    const branch = document.getElementById('sim5-branch');
    const badge = document.getElementById('sim5-badge');
    const desc = document.getElementById('sim5-desc');
    const pulvinus = document.getElementById('sim5-pulvinus');

    if (branch) branch.style.transform = "rotate(0deg)";
    if (pulvinus) pulvinus.setAttribute('ry', '6'); // Inflated pulvinus

    const pairs = document.querySelectorAll('.mimosa-pair');
    pairs.forEach(p => {
        p.style.transform = "scaleY(1)";
    });

    if (badge) {
        badge.textContent = "Turgor Restored";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
    }
    if (desc) {
        desc.innerHTML = "<strong>Turgor Recovery:</strong> Over 10-15 minutes, pulvinus cells reabsorb water and potassium, reopening the leaflets to catch sunlight.";
    }
    mimosaFolded = false;
}

// Sim 6: Reproduction Modes
function setReproMode(mode) {
    const pIcon = document.getElementById('sim6-p-icon');
    const pLabel = document.getElementById('sim6-p-label');
    const vIcon = document.getElementById('sim6-v-icon');
    const vLabel = document.getElementById('sim6-v-label');
    const cIcon = document.getElementById('sim6-c-icon');
    const cLabel = document.getElementById('sim6-c-label');
    const badge = document.getElementById('sim6-badge');
    const desc = document.getElementById('sim6-desc');

    if (mode === 'plant') {
        if (pIcon) pIcon.textContent = "🌳";
        if (pLabel) pLabel.textContent = "Parent Tree";
        if (vIcon) vIcon.textContent = "🌰";
        if (vLabel) vLabel.textContent = "Seed in Pod";
        if (cIcon) cIcon.textContent = "🌱";
        if (cLabel) cLabel.textContent = "Sapling";
        if (badge) badge.textContent = "Mode: Seed to Plant";
        if (desc) desc.textContent = "Flowering trees produce seeds inside fruits that disperse and germinate into new daughter plants.";
    } else if (mode === 'bird') {
        if (pIcon) pIcon.textContent = "🦅";
        if (pLabel) pLabel.textContent = "Parent Bird";
        if (vIcon) vIcon.textContent = "🥚";
        if (vLabel) vLabel.textContent = "Incubated Egg";
        if (cIcon) cIcon.textContent = "🐣";
        if (cLabel) cLabel.textContent = "Hatched Chick";
        if (badge) badge.textContent = "Mode: Oviparous (Eggs)";
        if (desc) desc.textContent = "Birds lay fertilized, hard-shelled eggs in nests, keeping them warm until chicks hatch.";
    } else if (mode === 'mammal') {
        if (pIcon) pIcon.textContent = "🐘";
        if (pLabel) pLabel.textContent = "Mother Elephant";
        if (vIcon) vIcon.textContent = "🍼";
        if (vLabel) vLabel.textContent = "Gestation";
        if (cIcon) cIcon.textContent = "🐘";
        if (cLabel) cLabel.textContent = "Elephant Calf";
        if (badge) badge.textContent = "Mode: Viviparous (Live Birth)";
        if (desc) desc.textContent = "Mammals nourish embryos internally and give birth to live offspring, nursing them with milk.";
    }
}

// Sim 7: Activity 10.2 Seed Germination Chamber
const sim7State = { water: false, air: true, temp: false };
function toggleSim7Condition(cond) {
    sim7State[cond] = !sim7State[cond];

    const btn = document.getElementById(`sim7-btn-${cond}`);
    if (btn) {
        const icons = { water: '💧 Water', air: '💨 Air', temp: '🌡️ Warmth' };
        if (sim7State[cond]) {
            btn.innerHTML = `${icons[cond]}: ON`;
            btn.className = "p-1.5 rounded-lg bg-emerald-950 border border-emerald-500/50 text-[11px] font-bold text-emerald-300";
        } else {
            btn.innerHTML = `${icons[cond]}: OFF`;
            btn.className = "p-1.5 rounded-lg bg-slate-900 border border-slate-700 text-[11px] font-bold text-slate-300";
        }
    }

    const waterLayer = document.getElementById('sim7-water-layer');
    if (waterLayer) {
        waterLayer.style.opacity = sim7State.water ? '0.4' : '0';
    }

    const radicle = document.getElementById('sim7-radicle');
    const plumule = document.getElementById('sim7-plumule');
    const badge = document.getElementById('sim7-status-badge');
    const overlay = document.getElementById('sim7-overlay-text');
    const desc = document.getElementById('sim7-desc');

    if (sim7State.water && sim7State.air && sim7State.temp) {
        if (radicle) radicle.style.opacity = '1';
        if (plumule) plumule.style.opacity = '1';
        if (badge) {
            badge.textContent = "Germination Complete!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (overlay) {
            overlay.textContent = "✓ Ideal Conditions: Seed Sprouted!";
            overlay.setAttribute('fill', '#4ade80');
        }
        if (desc) {
            desc.innerHTML = "<strong>Success:</strong> Moisture softened the coat, oxygen powered respiration, and warmth drove enzymatic cell division!";
        }
    } else {
        if (radicle) radicle.style.opacity = '0';
        if (plumule) plumule.style.opacity = '0';
        if (badge) {
            badge.textContent = "Conditions Incomplete";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        let missing = [];
        if (!sim7State.water) missing.push("Water");
        if (!sim7State.air) missing.push("Air");
        if (!sim7State.temp) missing.push("Warmth");
        if (overlay) {
            overlay.textContent = `Missing: ${missing.join(', ')}`;
            overlay.setAttribute('fill', '#f59e0b');
        }
        if (desc) {
            desc.innerHTML = `<strong>Dormant:</strong> Seed cannot sprout without ${missing.join(' and ')}. Toggle all 3 switches to ON.`;
        }
    }
}

// Sim 8: Imbibition
function soakSeed(isSoaked) {
    const water = document.getElementById('sim8-water-fill');
    const seed = document.getElementById('sim8-seed-scale');
    const crack = document.getElementById('sim8-crack');
    const badge = document.getElementById('sim8-badge');
    const desc = document.getElementById('sim8-desc');

    if (isSoaked) {
        if (water) water.style.opacity = '0.6';
        if (seed) seed.setAttribute('transform', 'translate(160, 140) scale(1.4)');
        if (crack) crack.style.opacity = '1';
        if (badge) {
            badge.textContent = "Swollen Seed (Testa Split)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Imbibition Success:</strong> Seed absorbs water through its micropyle, swells by 40-50%, softens the tough testa, and allows the radicle to push out.";
        }
    } else {
        if (water) water.style.opacity = '0.1';
        if (seed) seed.setAttribute('transform', 'translate(160, 140) scale(1)');
        if (crack) crack.style.opacity = '0';
        if (badge) {
            badge.textContent = "Dry Dormant Seed";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300";
        }
        if (desc) {
            desc.innerHTML = "<strong>Dry Seed:</strong> Hydrophilic colloids remain dehydrated; seed coat is tough and impermeable, keeping embryo asleep.";
        }
    }
}

// Sim 9: Soil Aeration vs Waterlogging
function setSoilAeration(isAerated) {
    const flood = document.getElementById('sim9-flood');
    const bubbles = document.getElementById('sim9-air-bubbles');
    const badge = document.getElementById('sim9-badge');
    const desc = document.getElementById('sim9-desc');

    if (isAerated) {
        if (flood) flood.style.opacity = '0';
        if (bubbles) bubbles.style.opacity = '1';
        if (badge) {
            badge.textContent = "Soil Well-Aerated";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Aerobic Health:</strong> Soil micro-pores supply abundant atmospheric oxygen to root tips for energetic nutrient absorption.";
        }
    } else {
        if (flood) flood.style.opacity = '0.7';
        if (bubbles) bubbles.style.opacity = '0';
        if (badge) {
            badge.textContent = "Waterlogged: Hypoxia Hazard";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse";
        }
        if (desc) {
            desc.innerHTML = "<strong>Hypoxia Suffocation:</strong> Water displaces trapped air in pores. Roots are deprived of oxygen, leading to root rot and seedling death.";
        }
    }
}

// Sim 10: Light vs Dark
function setLightEnvironment(isLit) {
    const bg = document.getElementById('sim10-bg');
    const sun = document.getElementById('sim10-sun');
    const stem = document.getElementById('sim10-stem');
    const leaves = document.getElementById('sim10-leaves');
    const leafL = document.getElementById('sim10-leaf-l');
    const leafR = document.getElementById('sim10-leaf-r');
    const badge = document.getElementById('sim10-badge');
    const desc = document.getElementById('sim10-desc');

    if (isLit) {
        if (bg) bg.setAttribute('fill', '#0f172a');
        if (sun) sun.style.opacity = '1';
        if (stem) {
            stem.setAttribute('d', 'M 160,145 Q 160,110 160,85');
            stem.setAttribute('stroke', '#16a34a');
        }
        if (leaves) leaves.setAttribute('transform', 'translate(160, 85)');
        if (leafL) {
            leafL.setAttribute('fill', '#22c55e');
            leafL.setAttribute('rx', '14');
        }
        if (leafR) {
            leafR.setAttribute('fill', '#22c55e');
            leafR.setAttribute('rx', '14');
        }
        if (badge) {
            badge.textContent = "Sunlit Window: Healthy";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Photomorphogenesis:</strong> Sunlight activates chlorophyll pigments, producing broad, vibrant green leaves and sturdy stems.";
        }
    } else {
        if (bg) bg.setAttribute('fill', '#020617');
        if (sun) sun.style.opacity = '0';
        if (stem) {
            stem.setAttribute('d', 'M 160,145 Q 155,90 160,40');
            stem.setAttribute('stroke', '#fef08a');
        }
        if (leaves) leaves.setAttribute('transform', 'translate(160, 40)');
        if (leafL) {
            leafL.setAttribute('fill', '#fef9c3');
            leafL.setAttribute('rx', '6');
        }
        if (leafR) {
            leafR.setAttribute('fill', '#fef9c3');
            leafR.setAttribute('rx', '6');
        }
        if (badge) {
            badge.textContent = "Darkness: Etiolated";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300";
        }
        if (desc) {
            desc.innerHTML = "<strong>Etiolation:</strong> Deprived of light, the shoot grows abnormally tall, thin, and pale yellow, unable to photosynthesize.";
        }
    }
}

// Sim 11: Tropisms
function tiltPlantPot(isTilted) {
    const group = document.getElementById('sim11-plant-group');
    const root = document.getElementById('sim11-root');
    const shoot = document.getElementById('sim11-shoot');
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');

    if (isTilted) {
        if (group) group.style.transform = "rotate(-90deg)";
        if (root) root.setAttribute('d', 'M 160,160 Q 180,180 205,185'); // Curving down towards earth
        if (shoot) shoot.setAttribute('d', 'M 160,120 Q 140,80 115,50'); // Curving up towards sky
        if (badge) {
            badge.textContent = "Pot Tilted: Tropisms Active";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Activity 10.3 Observed:</strong> Roots curve down towards gravity (+ geotropism), while the shoot bends upwards toward light (+ phototropism).";
        }
    } else {
        if (group) group.style.transform = "rotate(0deg)";
        if (root) root.setAttribute('d', 'M 160,160 Q 160,180 160,195');
        if (shoot) shoot.setAttribute('d', 'M 160,120 Q 160,80 160,50');
        if (badge) {
            badge.textContent = "Orientation: Upright";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300";
        }
        if (desc) {
            desc.innerHTML = "Upright seedling displays standard vertical gravitropic root anchoring and phototropic shoot elevation.";
        }
    }
}

// Sim 12: J.C. Bose Crescograph
function applyBoseStimulus(type) {
    const wave = document.getElementById('sim12-trace-wave');
    const needle = document.getElementById('sim12-needle');
    const status = document.getElementById('sim12-status');
    const desc = document.getElementById('sim12-desc');

    if (type === 'electric') {
        if (wave) wave.setAttribute('d', 'M 20,100 Q 40,30 60,160 T 100,50 T 140,140 T 180,70 L 200,100');
        if (needle) needle.style.transform = "rotate(65deg)";
        if (status) {
            status.textContent = "Electrical Spike Detected!";
            status.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 animate-pulse";
        }
        if (desc) {
            desc.innerHTML = "<strong>Action Potential:</strong> Bose proved plants transmit electrical impulses identical to animal motor nerves when stimulated!";
        }
    } else if (type === 'anesthetic') {
        if (wave) wave.setAttribute('d', 'M 20,100 L 200,100'); // Flatline
        if (needle) needle.style.transform = "rotate(-40deg)";
        if (status) {
            status.textContent = "Anesthetic: Growth Suspended";
            status.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Chloroform Stupor:</strong> Chloroform quenches plant electrical activity; reviving with fresh air restores normal vitality!";
        }
    } else {
        if (wave) wave.setAttribute('d', 'M 20,100 Q 50,90 80,100 T 140,100 T 200,100');
        if (needle) needle.style.transform = "rotate(15deg)";
        if (status) {
            status.textContent = "Magnification: 10,000×";
            status.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
        }
        if (desc) {
            desc.innerHTML = "J.C. Bose's crescograph records rhythmic micron pulsations during healthy, uninhibited plant cellular elongation.";
        }
    }
}

// Sim 13: Plant Life Cycle Wheel
let plantCycleStep = 1;
const plantCycleData = [
    { title: "1. Seed in Soil", icon: "🌰", desc: "Dormant embryo awaits moisture and warmth inside a protective seed coat." },
    { title: "2. Sprouting Seedling", icon: "🌱", desc: "Radicle roots anchor downward; plumule emerges to unfurl primary leaves." },
    { title: "3. Vegetative Growth", icon: "🌿", desc: "Vigorous stems and lush foliage expand via active daytime photosynthesis." },
    { title: "4. Blossoming Flowers", icon: "🌸", desc: "Bright blooms display male stamens and female carpels for pollination." },
    { title: "5. Fruits & Seed Pods", icon: "🫛", desc: "Fertilization yields seed-bearing pods and juicy fruits nourishing new embryos." },
    { title: "6. Seed Dispersal", icon: "💨", desc: "Wind, water, and animals scatter seeds far from the parent, renewing life." }
];

function stepPlantCycle(dir) {
    plantCycleStep += dir;
    if (plantCycleStep < 1) plantCycleStep = 6;
    if (plantCycleStep > 6) plantCycleStep = 1;

    const data = plantCycleData[plantCycleStep - 1];
    const icon = document.getElementById('sim13-icon');
    const title = document.getElementById('sim13-title');
    const badge = document.getElementById('sim13-badge');
    const desc = document.getElementById('sim13-desc');

    if (icon) icon.textContent = data.icon;
    if (title) title.textContent = data.title;
    if (badge) badge.textContent = `Stage ${plantCycleStep}: ${data.title}`;
    if (desc) desc.textContent = data.desc;

    for (let i = 1; i <= 6; i++) {
        const dot = document.getElementById(`dot-${i}`);
        if (dot) {
            dot.setAttribute('fill', (i === plantCycleStep) ? '#6366f1' : '#334155');
            dot.setAttribute('r', (i === plantCycleStep) ? '7' : '5');
        }
    }
}

// Sim 14: Mosquito Vector Control
function sprayKeroseneFilm(isSprayed) {
    const oil = document.getElementById('sim14-oil-film');
    const larva = document.getElementById('sim14-larva');
    const air = document.getElementById('sim14-air');
    const badge = document.getElementById('sim14-badge');
    const desc = document.getElementById('sim14-desc');

    if (isSprayed) {
        if (oil) oil.style.opacity = '0.9';
        if (larva) larva.setAttribute('transform', 'translate(160, 80) rotate(45)');
        if (air) air.style.opacity = '0';
        if (badge) {
            badge.textContent = "Siphons Suffocated!";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) {
            desc.innerHTML = "<strong>Suffocation Barrier:</strong> Oil lowers surface tension and physically seals breathing siphons. Wrigglers and pupae suffocate within minutes!";
        }
    } else {
        if (oil) oil.style.opacity = '0';
        if (larva) larva.setAttribute('transform', 'translate(160, 40) rotate(0)');
        if (air) air.style.opacity = '1';
        if (badge) {
            badge.textContent = "Larvae Breathing: Normal";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (desc) {
            desc.innerHTML = "Wrigglers hang suspended from surface tension, breathing atmospheric oxygen through open siphons.";
        }
    }
}

// Sim 15: Silk Moth Metamorphosis
function setSilkStage(stage) {
    const caterpillar = document.getElementById('sim15-caterpillar');
    const cocoon = document.getElementById('sim15-cocoon');
    const moth = document.getElementById('sim15-moth');
    const badge = document.getElementById('sim15-badge');
    const desc = document.getElementById('sim15-desc');

    if (caterpillar) caterpillar.style.opacity = '0';
    if (cocoon) cocoon.style.opacity = '0';
    if (moth) moth.style.opacity = '0';

    if (stage === 'larva') {
        if (caterpillar) caterpillar.style.opacity = '1';
        if (badge) badge.textContent = "Stage: Silkworm Larva";
        if (desc) desc.textContent = "Caterpillars feed continuously on fresh mulberry leaves, storing amino acids for silk synthesis.";
    } else if (stage === 'cocoon') {
        if (cocoon) cocoon.style.opacity = '1';
        if (badge) badge.textContent = "Stage: Spun Cocoon";
        if (desc) desc.textContent = "Mature silkworm spins a continuous 1,000-meter fibroin silk filament around itself to form a cocoon.";
    } else if (stage === 'moth') {
        if (moth) moth.style.opacity = '1';
        if (badge) badge.textContent = "Stage: Adult Silk Moth";
        if (desc) desc.textContent = "Pupa metamorphoses inside the cocoon and emerges as a winged adult silk moth to reproduce.";
    }
}

// Sim 16: Frog Metamorphosis Timeline
function setFrogStage(stage) {
    const spawn = document.getElementById('sim16-spawn');
    const tadpole = document.getElementById('sim16-tadpole');
    const froglet = document.getElementById('sim16-froglet');
    const adult = document.getElementById('sim16-adult');
    const badge = document.getElementById('sim16-badge');
    const desc = document.getElementById('sim16-desc');

    if (spawn) spawn.style.opacity = '0';
    if (tadpole) tadpole.style.opacity = '0';
    if (froglet) froglet.style.opacity = '0';
    if (adult) adult.style.opacity = '0';

    if (stage === 1) {
        if (spawn) spawn.style.opacity = '1';
        if (badge) badge.textContent = "Stage 1: Jelly Spawn";
        if (desc) desc.textContent = "Clumps of eggs surrounded by protective clear jelly float safely in pond water.";
    } else if (stage === 2) {
        if (tadpole) tadpole.style.opacity = '1';
        if (badge) badge.textContent = "Stage 2: Aquatic Tadpole";
        if (desc) desc.textContent = "Swimming herbivore with a finned tail, breathing dissolved oxygen through gills.";
    } else if (stage === 3) {
        if (froglet) froglet.style.opacity = '1';
        if (badge) badge.textContent = "Stage 3: Froglet";
        if (desc) desc.textContent = "Legs sprout, lungs develop, and tail tissues are broken down and reabsorbed into the body.";
    } else if (stage === 4) {
        if (adult) adult.style.opacity = '1';
        if (badge) badge.textContent = "Stage 4: Adult Frog";
        if (desc) desc.textContent = "Tailless, carnivorous amphibian leaping on land, breathing through lungs and moist skin.";
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


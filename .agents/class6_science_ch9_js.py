"""
Interactive JavaScript for Class 6 Science Chapter 9: Methods of Separation in Everyday Life
Features sentence-by-sentence Web Speech API with Indian Male voice priority, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure Unicode.
"""

JS_CODE = '''
// Science Chapter 9 Interactive JavaScript
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

    // Clean text and split into sentences
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
        const el = document.getElementById(`slide-${i}`);
        if (el) {
            el.style.display = (i === currentSlide) ? 'block' : 'none';
        }
    }

    const counter = document.getElementById('slideCounter');
    if (counter) {
        counter.textContent = `${currentSlide} / ${totalSlides}`;
    }

    const select = document.getElementById('slideSelect');
    if (select) {
        select.value = currentSlide.toString();
    }

    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }

    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastSlideNotice) lastSlideNotice.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastSlideNotice) lastSlideNotice.style.display = 'none';
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

// Checkpoint Verification
function checkCheckpoint(cpId, selectedOpt, correctOpt, explanation) {
    const feedbackBox = document.getElementById(`cp-feedback-${cpId}`);
    if (!feedbackBox) return;

    if (selectedOpt === correctOpt) {
        feedbackBox.className = "mt-3 p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs";
        feedbackBox.innerHTML = `<strong>Correct!</strong> ${explanation}`;
    } else {
        feedbackBox.className = "mt-3 p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs";
        feedbackBox.innerHTML = `<strong>Not quite right.</strong> Review the concept explanation and observe the physical properties carefully.`;
    }
    feedbackBox.style.display = "block";
}

// Solution Modal
function openSolutionModal(title, questionText, solutionHtml) {
    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const questionEl = document.getElementById('modalQuestion');
    const solEl = document.getElementById('modalSolution');

    if (modal && titleEl && questionEl && solEl) {
        titleEl.textContent = title;
        questionEl.innerHTML = `<strong>Question:</strong> ${questionText}`;
        solEl.innerHTML = solutionHtml;
        modal.style.display = 'flex';
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Quiz Option Selection
function selectQuizOption(qId, selectedOpt, correctOpt, title, questionText, explanation) {
    const container = document.getElementById(`q-card-${qId}`);
    if (!container) return;

    const optButtons = container.querySelectorAll('.quiz-opt-btn');
    optButtons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctOpt) {
            btn.className = "quiz-opt-btn w-full text-left p-3 rounded-xl text-xs font-medium border bg-emerald-950/60 border-emerald-500 text-emerald-200";
        } else if (idx === selectedOpt && selectedOpt !== correctOpt) {
            btn.className = "quiz-opt-btn w-full text-left p-3 rounded-xl text-xs font-medium border bg-rose-950/60 border-rose-500 text-rose-200";
        } else {
            btn.className = "quiz-opt-btn w-full text-left p-3 rounded-xl text-xs font-medium border bg-slate-900 border-slate-800 text-slate-400 opacity-60";
        }
    });

    const fb = document.getElementById(`q-fb-${qId}`);
    if (fb) {
        if (selectedOpt === correctOpt) {
            fb.className = "p-3 rounded-xl text-xs bg-emerald-950/40 border border-emerald-500/40 text-emerald-300";
            fb.innerHTML = `<strong>Correct!</strong> ${explanation}`;
        } else {
            fb.className = "p-3 rounded-xl text-xs bg-rose-950/40 border border-rose-500/40 text-rose-300";
            fb.innerHTML = `<strong>Incorrect.</strong> ${explanation}`;
        }
        fb.style.display = "block";
    }

    const solBtn = document.getElementById(`q-sol-btn-${qId}`);
    if (solBtn) {
        solBtn.style.display = "inline-flex";
    }
}

// ==========================================
// SIMULATOR 1: Separation Purpose
// ==========================================
function sim1RemoveStones() {
    const stones = document.getElementById('sim1-stones');
    if (stones) stones.style.opacity = '0';
    const badge = document.getElementById('sim1-badge');
    if (badge) badge.textContent = 'Harmful Stones Removed';
    const status = document.getElementById('sim1-status');
    if (status) status.innerHTML = "<strong class='text-rose-400'>1. Harmful Impurities Extracted:</strong> Stones picked out to protect teeth and health.";
}

function sim1RemoveHusk() {
    const husk = document.getElementById('sim1-husk');
    if (husk) husk.style.opacity = '0';
    const badge = document.getElementById('sim1-badge');
    if (badge) badge.textContent = 'Clean Wheat Grain Ready';
    const status = document.getElementById('sim1-status');
    if (status) status.innerHTML = "<strong class='text-amber-400'>2. Non-Useful Chaff Discarded:</strong> Papery husk blown away to leave clean, edible grain.";
}

function sim1Reset() {
    const stones = document.getElementById('sim1-stones');
    const husk = document.getElementById('sim1-husk');
    const badge = document.getElementById('sim1-badge');
    const status = document.getElementById('sim1-status');
    if (stones) stones.style.opacity = '1';
    if (husk) husk.style.opacity = '1';
    if (badge) badge.textContent = 'Raw Mixture';
    if (status) status.textContent = 'Raw mixture contains wheat grains, dangerous gravel stones, and fibrous husk.';
}

// ==========================================
// SIMULATOR 2: Handpicking
// ==========================================
let sim2PebblesLeft = 4;
function sim2PickPebble(n) {
    const p = document.getElementById(`pebble-${n}`);
    if (p && p.style.display !== 'none') {
        p.style.display = 'none';
        sim2PebblesLeft--;
        const cnt = document.getElementById('sim2-counter');
        const st = document.getElementById('sim2-status');
        if (cnt) cnt.textContent = `Pebbles Left: ${sim2PebblesLeft} / 4`;
        if (st) {
            if (sim2PebblesLeft === 0) {
                st.innerHTML = "<strong class='text-emerald-400'>100% Clean!</strong> All gravel stones picked out. Rice is ready for cooking!";
            } else {
                st.textContent = `Picked out pebble #${n}! ${sim2PebblesLeft} remaining on plate.`;
            }
        }
    }
}

function sim2Reset() {
    sim2PebblesLeft = 4;
    for (let i = 1; i <= 4; i++) {
        const p = document.getElementById(`pebble-${i}`);
        if (p) p.style.display = 'block';
    }
    const cnt = document.getElementById('sim2-counter');
    const st = document.getElementById('sim2-status');
    if (cnt) cnt.textContent = 'Pebbles Left: 4 / 4';
    if (st) st.textContent = 'Click individual stones to handpick them.';
}

// ==========================================
// SIMULATOR 3: Threshing
// ==========================================
let sim3Strikes = 0;
function sim3Strike() {
    sim3Strikes++;
    const sheaf = document.getElementById('sim3-sheaf');
    const pile = document.getElementById('sim3-grain-pile');
    const counter = document.getElementById('sim3-strike-count');
    const msg = document.getElementById('sim3-msg');

    if (sheaf) {
        sheaf.style.transform = 'rotate(20deg)';
        setTimeout(() => {
            sheaf.style.transform = 'rotate(-30deg)';
        }, 150);
    }
    if (pile) pile.style.opacity = '1';
    if (counter) counter.textContent = `Strikes: ${sim3Strikes}`;
    if (msg) msg.innerHTML = `<strong class='text-amber-300'>Strike #${sim3Strikes}:</strong> Inertia dislodges golden grains cascading onto the ground!`;
}

// ==========================================
// SIMULATOR 4: Auto Thresher
// ==========================================
function sim4UpdateSpeed(val) {
    const badge = document.getElementById('sim4-rpm-badge');
    const text = document.getElementById('sim4-rate-val');
    const drum = document.getElementById('sim4-drum');
    if (badge) badge.textContent = `Drum: ${val} RPM`;
    const rate = Math.round(val / 20);
    if (text) text.textContent = `Processing: ${rate} Quintals/hr`;
    if (drum) {
        drum.style.stroke = val > 1000 ? '#f43f5e' : '#38bdf8';
    }
}

// ==========================================
// SIMULATOR 5: Winnowing
// ==========================================
function sim5ChangeWind(val) {
    const badge = document.getElementById('sim5-wind-badge');
    const text = document.getElementById('sim5-wind-text');
    const husk = document.getElementById('sim5-husk-falling');
    if (badge) badge.textContent = `Wind: ${val} km/h`;
    if (text) {
        if (val < 10) text.textContent = 'Light Air (Husk barely drifts)';
        else if (val < 25) text.textContent = `Moderate Breeze (${val} km/h - Optimal)`;
        else text.textContent = `Strong Gale (${val} km/h - Grains may blow!)`;
    }
    if (husk) {
        const offset = (val - 18) * 3;
        husk.style.transform = `translateX(${offset}px)`;
    }
}

// ==========================================
// SIMULATOR 6: Sieving
// ==========================================
let sim6CurrentMode = 'flour';
function sim6SetMode(mode) {
    sim6CurrentMode = mode;
    const btnF = document.getElementById('sim6-btn-flour');
    const btnS = document.getElementById('sim6-btn-sand');
    const topL = document.getElementById('sim6-top-label');
    const botL = document.getElementById('sim6-bottom-label');

    if (mode === 'flour') {
        if (btnF) btnF.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-600 text-white';
        if (btnS) btnS.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300';
        if (topL) topL.textContent = 'Retained: Wheat Bran (Choker)';
        if (botL) botL.textContent = 'Passed: Fine Flour Powder';
    } else {
        if (btnS) btnS.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-600 text-white';
        if (btnF) btnF.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300';
        if (topL) topL.textContent = 'Retained: Coarse Pebbles & Gravel';
        if (botL) botL.textContent = 'Passed: Smooth Construction Sand';
    }
}

function sim6Shake() {
    const sieve = document.getElementById('sim6-sieve');
    if (sieve) {
        sieve.style.transform = 'translateX(8px)';
        setTimeout(() => { sieve.style.transform = 'translateX(-8px)'; }, 50);
        setTimeout(() => { sieve.style.transform = 'translateX(0px)'; }, 100);
    }
}

// ==========================================
// SIMULATOR 7: Coastal Salt Pans
// ==========================================
function sim7SetDay(day) {
    const badge = document.getElementById('sim7-salinity-badge');
    const daysVal = document.getElementById('sim7-days-val');
    const water = document.getElementById('sim7-water-layer');
    const crust = document.getElementById('sim7-salt-crust');
    const label = document.getElementById('sim7-salt-label');

    const h = 55 - (day - 1) * 11;
    if (water) water.setAttribute('height', Math.max(0, h));
    if (crust) crust.style.opacity = (day * 0.2).toString();

    if (day == 1) {
        if (badge) badge.textContent = 'Salinity: 3.5% (Seawater)';
        if (daysVal) daysVal.textContent = 'Day 1 (Fresh Seawater Intake)';
        if (label) label.style.opacity = '0';
    } else if (day == 3) {
        if (badge) badge.textContent = 'Salinity: 12% (Concentrated Brine)';
        if (daysVal) daysVal.textContent = 'Day 3 (Significant Solar Evaporation)';
        if (label) label.style.opacity = '0';
    } else if (day >= 5) {
        if (badge) badge.textContent = 'Salinity: Saturated (Solid Salt Crust)';
        if (daysVal) daysVal.textContent = 'Day 5 (100% Water Evaporated!)';
        if (label) label.style.opacity = '1';
    }
}

// ==========================================
// SIMULATOR 8: China Dish Evaporation
// ==========================================
let sim8Burning = false;
function sim8ToggleBurner() {
    sim8Burning = !sim8Burning;
    const flame = document.getElementById('sim8-flame');
    const steam = document.getElementById('sim8-steam');
    const liquid = document.getElementById('sim8-liquid');
    const residue = document.getElementById('sim8-residue');
    const state = document.getElementById('sim8-burner-state');
    const btn = document.getElementById('sim8-btn');
    const info = document.getElementById('sim8-info');

    if (sim8Burning) {
        if (flame) flame.style.opacity = '1';
        if (steam) steam.style.opacity = '1';
        if (state) {
            state.textContent = 'Burner: ON (100°C Boiling)';
            state.className = 'text-xs font-bold text-amber-400';
        }
        if (btn) btn.textContent = '⏹ Extinguish Flame';
        if (info) info.textContent = 'Water is rapidly evaporating into steam...';

        setTimeout(() => {
            if (sim8Burning) {
                if (liquid) liquid.style.opacity = '0';
                if (residue) residue.style.opacity = '1';
                if (info) info.innerHTML = "<strong class='text-white'>Evaporation Complete:</strong> Dry white salt crystals (NaCl) remain in the dish!";
            }
        }, 1200);
    } else {
        if (flame) flame.style.opacity = '0';
        if (steam) steam.style.opacity = '0';
        if (liquid) liquid.style.opacity = '1';
        if (residue) residue.style.opacity = '0';
        if (state) {
            state.textContent = 'Burner: OFF';
            state.className = 'text-xs font-bold text-slate-400';
        }
        if (btn) btn.textContent = '🔥 Ignite Burner';
        if (info) info.textContent = 'Click to boil water and crystallize white salt.';
    }
}

// ==========================================
// SIMULATOR 9: Sedimentation Settling
// ==========================================
function sim9SetTime(mins) {
    const badge = document.getElementById('sim9-time-badge');
    const val = document.getElementById('sim9-clarity-val');
    const water = document.getElementById('sim9-water');
    const sed = document.getElementById('sim9-sediment');
    const label = document.getElementById('sim9-sed-label');

    if (badge) badge.textContent = `Time: ${mins} mins`;
    const clarity = Math.round((mins / 20) * 100);
    if (val) val.textContent = `${clarity}% Clarified`;

    if (water) {
        const opacity = 0.8 - (clarity / 100) * 0.45;
        water.setAttribute('opacity', opacity.toString());
        if (mins >= 15) water.setAttribute('fill', '#0284c7');
        else water.setAttribute('fill', '#78350f');
    }
    if (sed) sed.setAttribute('opacity', (0.3 + (clarity / 100) * 0.7).toString());
    if (label) label.style.opacity = mins > 5 ? '1' : '0';
}

// ==========================================
// SIMULATOR 10: Decantation Tilt
// ==========================================
function sim10SetTilt(angle) {
    const badge = document.getElementById('sim10-angle-badge');
    const msg = document.getElementById('sim10-status-msg');
    const beaker = document.getElementById('sim10-tilt-beaker');
    const stream = document.getElementById('sim10-stream');
    const recv = document.getElementById('sim10-recv-liquid');

    if (badge) badge.textContent = `Tilt: ${angle}°`;
    if (beaker) beaker.style.transform = `rotate(${angle}deg)`;

    if (angle > 15 && angle <= 45) {
        if (stream) stream.style.opacity = '1';
        if (recv) recv.setAttribute('height', (8 + (angle - 15) * 0.8).toString());
        if (msg) {
            msg.textContent = 'Smooth Pouring (Sediment Stable)';
            msg.className = 'text-emerald-400 font-bold';
        }
    } else if (angle > 45) {
        if (stream) {
            stream.style.opacity = '1';
            stream.setAttribute('stroke', '#78350f');
        }
        if (msg) {
            msg.textContent = 'Warning: Over-tilt! Sediment stirs up into pour!';
            msg.className = 'text-rose-400 font-bold';
        }
    } else {
        if (stream) stream.style.opacity = '0';
        if (msg) {
            msg.textContent = 'Stable';
            msg.className = 'text-slate-400 font-bold';
        }
    }
}

// ==========================================
// SIMULATOR 11: Filter Cone Folding
// ==========================================
function sim11Step(n) {
    const shape = document.getElementById('sim11-shape');
    const badge = document.getElementById('sim11-step-badge');
    const cap = document.getElementById('sim11-caption');

    if (n === 1) {
        if (shape) shape.setAttribute('d', ''); // Reset
        if (badge) badge.textContent = 'Step 1: Circle';
        if (cap) cap.textContent = 'Flat Circular Filter Paper (110 mm diameter)';
    } else if (n === 2) {
        if (badge) badge.textContent = 'Step 2: Semicircle';
        if (cap) cap.textContent = 'Folded precisely in half across diameter';
    } else if (n === 3) {
        if (badge) badge.textContent = 'Step 3: Quadrant (Quarter)';
        if (cap) cap.textContent = 'Folded once more into a 90° quadrant wedge';
    } else if (n === 4) {
        if (badge) badge.textContent = 'Step 4: 60° Hollow Cone';
        if (cap) cap.textContent = 'Open 3 layers on one side and 1 layer on the other: 60° Cone ready for funnel!';
    }
}

// ==========================================
// SIMULATOR 12: Funnel Filtration Lab
// ==========================================
function sim12StartFilter() {
    const res = document.getElementById('sim12-residue');
    const resL = document.getElementById('sim12-res-label');
    const fil = document.getElementById('sim12-filtrate');
    const filL = document.getElementById('sim12-fil-label');
    const drop = document.getElementById('sim12-drop');
    const badge = document.getElementById('sim12-filtrate-badge');
    const info = document.getElementById('sim12-info');

    if (drop) {
        drop.style.opacity = '1';
        drop.style.transition = 'transform 0.4s ease-in';
        drop.style.transform = 'translateY(30px)';
    }

    setTimeout(() => {
        if (res) res.style.opacity = '1';
        if (resL) resL.style.opacity = '1';
        if (fil) fil.style.opacity = '0.7';
        if (filL) filL.style.opacity = '1';
        if (badge) badge.textContent = 'Filtrate: 50 mL (Pure)';
        if (info) info.innerHTML = "<strong class='text-emerald-400'>Filtration Succeeded:</strong> Insoluble mud trapped as residue; pristine filtrate collected below!";
    }, 500);
}

// ==========================================
// SIMULATOR 13: Curd Churning (Mathni)
// ==========================================
let sim13Butter = 0;
function sim13Churn() {
    sim13Butter += 25;
    const mathni = document.getElementById('sim13-mathni');
    const butter = document.getElementById('sim13-butter-blobs');
    const badge = document.getElementById('sim13-butter-badge');
    const status = document.getElementById('sim13-status');

    if (mathni) {
        mathni.style.transform = 'rotate(15deg)';
        setTimeout(() => { mathni.style.transform = 'rotate(-15deg)'; }, 60);
        setTimeout(() => { mathni.style.transform = 'rotate(0deg)'; }, 120);
    }

    if (butter) butter.style.opacity = '1';
    if (badge) badge.textContent = `Butter: ${sim13Butter} g`;
    if (status) status.innerHTML = "<strong class='text-amber-300'>Lipid Coalescence:</strong> Rapid spinning ruptures fat globules; lighter butter floats buoyantly over buttermilk!";
}

// ==========================================
// SIMULATOR 14: Magnetic Wand
// ==========================================
let sim14Picked = 0;
function sim14HoverMagnet() {
    const magnet = document.getElementById('sim14-magnet');
    if (magnet) magnet.style.transform = 'translate(160, 65)';

    setTimeout(() => {
        for (let i = 1; i <= 5; i++) {
            const nail = document.getElementById(`nail-${i}`);
            if (nail) {
                nail.style.transition = 'transform 0.2s ease-out';
                nail.style.transform = 'translateY(-35px)';
            }
        }
        sim14Picked = 5;
        const b = document.getElementById('sim14-pins-badge');
        if (b) b.textContent = 'Iron Nails Retrieved: 5 / 5';
    }, 250);
}

function sim14Reset() {
    const magnet = document.getElementById('sim14-magnet');
    if (magnet) magnet.style.transform = 'translate(160, 25)';
    for (let i = 1; i <= 5; i++) {
        const nail = document.getElementById(`nail-${i}`);
        if (nail) nail.style.transform = 'translateY(0px)';
    }
    sim14Picked = 0;
    const b = document.getElementById('sim14-pins-badge');
    if (b) b.textContent = 'Iron Nails Retrieved: 0 / 5';
}

// ==========================================
// SIMULATOR 15: Scrap Crane
// ==========================================
function sim15PowerOn() {
    const glow = document.getElementById('sim15-glow');
    const scrap = document.getElementById('sim15-clinging-iron');
    const badge = document.getElementById('sim15-power-badge');
    if (glow) glow.style.opacity = '1';
    if (scrap) scrap.style.opacity = '1';
    if (badge) {
        badge.textContent = 'Current: ON (5000 A Magnetized)';
        badge.className = 'text-xs font-bold text-emerald-400 font-mono';
    }
}

function sim15PowerOff() {
    const glow = document.getElementById('sim15-glow');
    const scrap = document.getElementById('sim15-clinging-iron');
    const badge = document.getElementById('sim15-power-badge');
    if (glow) glow.style.opacity = '0';
    if (scrap) scrap.style.opacity = '0';
    if (badge) {
        badge.textContent = 'Current: OFF (Released)';
        badge.className = 'text-xs font-bold text-rose-400 font-mono';
    }
}

// ==========================================
// SIMULATOR 16: Multi-Step Pipeline
// ==========================================
let sim16Stage = 1;
function sim16Advance() {
    sim16Stage = (sim16Stage % 3) + 1;
    const badge = document.getElementById('sim16-stage-badge');
    const status = document.getElementById('sim16-status');
    const b1 = document.getElementById('sim16-box1');
    const b2 = document.getElementById('sim16-box2');
    const b3 = document.getElementById('sim16-box3');

    if (badge) badge.textContent = `Stage: ${sim16Stage} / 3`;

    if (sim16Stage === 1) {
        if (b1) b1.style.opacity = '1';
        if (b2) b2.style.opacity = '0.4';
        if (b3) b3.style.opacity = '0.4';
        if (status) status.textContent = 'Stage 1: Adding water dissolves soluble salt into solution.';
    } else if (sim16Stage === 2) {
        if (b1) b1.style.opacity = '0.4';
        if (b2) b2.style.opacity = '1';
        if (b3) b3.style.opacity = '0.4';
        if (status) status.innerHTML = "<strong class='text-amber-400'>Stage 2:</strong> Filtration traps insoluble sand as residue; salt solution flows through!";
    } else if (sim16Stage === 3) {
        if (b1) b1.style.opacity = '0.4';
        if (b2) b2.style.opacity = '0.4';
        if (b3) b3.style.opacity = '1';
        if (status) status.innerHTML = "<strong class='text-emerald-400'>Stage 3:</strong> Evaporation boils off water and condenses pure water; dry salt remains!";
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''


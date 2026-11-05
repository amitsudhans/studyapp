"""
Interactive JavaScript for Class 6 Science Chapter 12: Beyond Earth
Features sentence-by-sentence Web Speech API with Indian Male voice priority, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure clean Unicode.
"""

JS_CODE = '''
// Science Chapter 12 Interactive JavaScript
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

// ==================== 16 Bespoke Simulator Handlers ====================

// Sim 1: Caravan Navigator
function navigateCaravan(dir) {
    const badge = document.getElementById('sim1-badge');
    const headingText = document.getElementById('sim1-heading-text');
    const caravan = document.getElementById('sim1-caravan');
    const navLine = document.getElementById('sim1-nav-line');
    const desc = document.getElementById('sim1-desc');

    if (dir === 'north') {
        if (badge) badge.textContent = "Heading: True North (000°)";
        if (headingText) headingText.textContent = "Compass: 000° N";
        if (caravan) caravan.setAttribute('transform', 'translate(140, 165)');
        if (navLine) {
            navLine.setAttribute('x2', '160');
            navLine.setAttribute('stroke', '#38bdf8');
        }
        if (desc) desc.innerHTML = "<strong>North Alignment:</strong> Moving directly toward the Pole Star maintains a constant true north bearing without drift.";
    } else if (dir === 'east') {
        if (badge) badge.textContent = "Heading: East (090°)";
        if (headingText) headingText.textContent = "Compass: 090° E";
        if (caravan) caravan.setAttribute('transform', 'translate(200, 165)');
        if (navLine) {
            navLine.setAttribute('x2', '220');
            navLine.setAttribute('stroke', '#ca8a04');
        }
        if (desc) desc.innerHTML = "<strong>East Heading:</strong> Caravan turns perpendicular to the right of the Pole Star, maintaining Polaris strictly on their left shoulder.";
    } else if (dir === 'west') {
        if (badge) badge.textContent = "Heading: West (270°)";
        if (headingText) headingText.textContent = "Compass: 270° W";
        if (caravan) caravan.setAttribute('transform', 'translate(80, 165)');
        if (navLine) {
            navLine.setAttribute('x2', '100');
            navLine.setAttribute('stroke', '#ca8a04');
        }
        if (desc) desc.innerHTML = "<strong>West Heading:</strong> Caravan keeps Polaris constantly on their right shoulder to journey toward western Himalayan passes.";
    }
}

// Sim 2: Constellation Sky Map
function toggleConstellationView(mode) {
    const badge = document.getElementById('sim2-badge');
    const iau = document.getElementById('sim2-iau-boundaries');
    const lines = document.getElementById('sim2-lines');
    const desc = document.getElementById('sim2-desc');

    if (mode === 'all') {
        if (iau) iau.style.display = 'inline';
        if (lines) lines.style.display = 'inline';
        if (badge) badge.textContent = "Mode: 88 IAU Official Boundaries";
        if (desc) desc.innerHTML = "<strong>IAU Sky Sectors:</strong> Like national borders on Earth, the International Astronomical Union mapped 88 contiguous regions covering every square degree of the sky.";
    } else if (mode === 'figures') {
        if (iau) iau.style.display = 'none';
        if (lines) lines.style.display = 'inline';
        if (badge) badge.textContent = "Mode: Constellation Stick Figures";
        if (desc) desc.innerHTML = "<strong>Pattern Recognition:</strong> Connect-the-dot stick figures historically helped navigators memorize constellations like Ursa Major and Orion.";
    } else if (mode === 'stars') {
        if (iau) iau.style.display = 'none';
        if (lines) lines.style.display = 'none';
        if (badge) badge.textContent = "Mode: Unadorned Star Field";
        if (desc) desc.innerHTML = "<strong>Pristine Star Field:</strong> Without boundary lines, stars appear as scattered pinpoints of light at widely varying cosmic distances.";
    }
}

// Sim 3: Orion the Hunter & Sirius Pointer
function highlightTarget(target) {
    const badge = document.getElementById('sim3-badge');
    const siriusRay = document.getElementById('sim3-sirius-ray');
    const taurusRay = document.getElementById('sim3-taurus-ray');
    const desc = document.getElementById('sim3-desc');

    if (target === 'sirius') {
        if (siriusRay) {
            siriusRay.setAttribute('stroke-width', '3');
            siriusRay.setAttribute('opacity', '1');
        }
        if (taurusRay) {
            taurusRay.setAttribute('stroke-width', '1');
            taurusRay.setAttribute('opacity', '0.3');
        }
        if (badge) badge.textContent = "Target: Sirius (Canis Major)";
        if (desc) desc.innerHTML = "<strong>Locating Sirius:</strong> An imaginary line drawn south-east through the three belt stars leads straight to Sirius, the brightest star in the night sky.";
    } else {
        if (siriusRay) {
            siriusRay.setAttribute('stroke-width', '1');
            siriusRay.setAttribute('opacity', '0.3');
        }
        if (taurusRay) {
            taurusRay.setAttribute('stroke-width', '3');
            taurusRay.setAttribute('opacity', '1');
        }
        if (badge) badge.textContent = "Target: Aldebaran (Taurus)";
        if (desc) desc.innerHTML = "<strong>Locating Aldebaran (Rohiṇī):</strong> Extending the belt line upward and to the right points to the reddish giant star Aldebaran in the constellation Taurus.";
    }
}

// Sim 4: Pole Star Pointer (5x Gap Rule)
let isRotated = false;
function measurePoleStar(mode) {
    const badge = document.getElementById('sim4-badge');
    const ray = document.getElementById('sim4-ray');
    const dipper = document.getElementById('sim4-dipper');
    const desc = document.getElementById('sim4-desc');

    if (mode === 'extend') {
        if (ray) {
            ray.setAttribute('stroke', '#22d3ee');
            ray.setAttribute('stroke-width', '3');
        }
        if (badge) badge.textContent = "Rule: 5x Pointer Gap Measured";
        if (desc) desc.innerHTML = "<strong>5× Distance Rule:</strong> Distance between Merak and Dubhe multiplied by 5 gives the exact distance to Polaris (Dhruva Tārā).";
    } else if (mode === 'rotate') {
        isRotated = !isRotated;
        if (dipper) {
            dipper.style.transition = 'transform 1s ease';
            dipper.style.transformOrigin = '120px 35px';
            dipper.style.transform = isRotated ? 'rotate(45deg)' : 'rotate(0deg)';
        }
        if (badge) badge.textContent = isRotated ? "Earth Spin: Polaris Remains Stationary" : "Sky Angle: Normal Northern View";
        if (desc) desc.innerHTML = "<strong>Stationary North Anchor:</strong> As Earth rotates beneath the stars, constellations appear to circle counter-clockwise around the stationary Pole Star.";
    }
}

// Sim 5: Urban Light Pollution vs Hanle
function updateLightPollution(val) {
    const sky = document.getElementById('sim5-sky');
    const mw = document.getElementById('sim5-milkyway');
    const faintStars = document.getElementById('sim5-faint-stars');
    const lamp = document.getElementById('sim5-lamp');
    const hanle = document.getElementById('sim5-hanle');
    const badge = document.getElementById('sim5-badge');
    const countText = document.getElementById('sim5-visibility-text');
    const desc = document.getElementById('sim5-desc');

    const pct = val / 100;

    if (sky) {
        const r = Math.round(51 - 49 * pct);
        const g = Math.round(65 - 59 * pct);
        const b = Math.round(85 - 62 * pct);
        sky.setAttribute('fill', `rgb(${r}, ${g}, ${b})`);
    }

    if (mw) mw.setAttribute('opacity', (0.05 + 0.65 * pct).toFixed(2));
    if (faintStars) faintStars.setAttribute('opacity', (0.1 + 0.9 * pct).toFixed(2));

    if (lamp) lamp.setAttribute('opacity', (1 - pct).toFixed(2));
    if (hanle) hanle.setAttribute('opacity', pct.toFixed(2));

    if (pct > 0.7) {
        if (badge) {
            badge.textContent = "Hanle Dark Sky Reserve (Bortle 1)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (countText) countText.textContent = "Visible Stars: 3,000+ & Milky Way Core";
        if (desc) desc.innerHTML = "<strong>Pristine High-Altitude Darkness:</strong> Hanle's elevation of 4,500m above sea level with minimal humidity and zero light pollution provides world-class astronomical transparency.";
    } else if (pct > 0.3) {
        if (badge) {
            badge.textContent = "Suburban Skies (Bortle 4-5)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (countText) countText.textContent = "Visible Stars: ~300 to 500";
        if (desc) desc.innerHTML = "<strong>Moderate Skyglow:</strong> Major constellations are clear, but the faint dust lanes of the Milky Way remain washed out.";
    } else {
        if (badge) {
            badge.textContent = "Urban Skyglow (Bortle 8-9)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (countText) countText.textContent = "Visible Stars: ~20 to 50";
        if (desc) desc.innerHTML = "<strong>Severe Light Pollution:</strong> Over-illuminated streets scatter glare across atmospheric aerosols, hiding 99% of celestial bodies.";
    }
}

// Sim 6: Stargazing Night Vision Flashlight
function setTorchMode(mode) {
    const beam = document.getElementById('sim6-beam');
    const filter = document.getElementById('sim6-filter');
    const badge = document.getElementById('sim6-badge');
    const starfield = document.getElementById('sim6-starfield');
    const desc = document.getElementById('sim6-desc');

    if (mode === 'red') {
        if (beam) beam.setAttribute('fill', '#ef4444');
        if (filter) filter.setAttribute('fill', '#ef4444');
        if (starfield) starfield.setAttribute('opacity', '1');
        if (badge) {
            badge.textContent = "Light: Red Cellophane (Preserves Vision)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (desc) desc.innerHTML = "<strong>Red Light Protection:</strong> Red wavelengths don't bleach the rhodopsin photopigment in human retinal rod cells, keeping pupil dilation sensitive to distant stars.";
    } else {
        if (beam) beam.setAttribute('fill', '#ffffff');
        if (filter) filter.setAttribute('fill', '#ffffff');
        if (starfield) starfield.setAttribute('opacity', '0.2');
        if (badge) {
            badge.textContent = "Light: White Glare (Night Blindness)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (desc) desc.innerHTML = "<strong>Pupil Constriction:</strong> White light triggers rapid constriction of the iris and bleaches rhodopsin, resetting night adaptation and blinding you to faint stars for 20 minutes.";
    }
}

// Sim 7: Solar Transit Time
function firePhotonAnimation() {
    const photon = document.getElementById('sim7-photon');
    const timerText = document.getElementById('sim7-timer-text');
    const badge = document.getElementById('sim7-badge');
    const desc = document.getElementById('sim7-desc');

    if (badge) badge.textContent = "Solar Transit: 1 AU in 8m 20s";
    if (timerText) timerText.textContent = "Photon Traversing 1 AU...";

    if (photon) {
        photon.setAttribute('cx', '75');
        let pos = 75;
        const interval = setInterval(() => {
            pos += 6;
            if (pos >= 255) {
                pos = 255;
                clearInterval(interval);
                if (timerText) timerText.textContent = "Transit Complete: 8m 20s (499 sec)";
                if (desc) desc.innerHTML = "<strong>Speed of Light:</strong> Traveling at 300,000 km/s, solar photons take 499 seconds (approx 8 min 20 sec) to cross the 149.6 million kilometer gap to Earth.";
            }
            photon.setAttribute('cx', pos.toString());
        }, 30);
    }
}

function compareProxima() {
    const timerText = document.getElementById('sim7-timer-text');
    const badge = document.getElementById('sim7-badge');
    const desc = document.getElementById('sim7-desc');

    if (badge) badge.textContent = "Proxima Centauri: 4.24 Light-Years";
    if (timerText) timerText.textContent = "Distance: ~40 Trillion km";
    if (desc) desc.innerHTML = "<strong>Interstellar Scale:</strong> While the Sun's light arrives in 8 minutes, the very next closest star system (Alpha Centauri / Proxima Centauri) is so far that its light takes 4.24 years to reach us.";
}

// Sim 8: Inner Terrestrial Planets
const rockyData = {
    mercury: {
        badge: "Planet: Mercury (Cratered Core)",
        title: "Mercury: Temp -180°C to +430°C | No Atmosphere",
        sub: "Closest planet to Sun (0.39 AU); 88-day orbit; heavily cratered metallic surface; 0 moons."
    },
    venus: {
        badge: "Planet: Venus (Runaway Greenhouse)",
        title: "Venus: Temp +465°C | 96% CO2 Atmosphere",
        sub: "Hottest planet in solar system; thick sulfuric acid cloud deck; rotates backward (retrograde); 0 moons."
    },
    earth: {
        badge: "Planet: Earth (Blue Oasis of Life)",
        title: "Earth: Temp 15°C | 78% N2, 21% O2 Atmosphere",
        sub: "Only known world with liquid surface oceans and life; magnetic shield; 1 natural satellite (Moon)."
    },
    mars: {
        badge: "Planet: Mars (Red Planet)",
        title: "Mars: Temp -65°C | Thin CO2 Atmosphere",
        sub: "Iron oxide dust causes reddish hue; home to Olympus Mons volcano and polar ice caps; 2 small moons."
    }
};

function selectRockyPlanet(p) {
    const badge = document.getElementById('sim8-badge');
    const line1 = document.getElementById('sim8-data-line1');
    const line2 = document.getElementById('sim8-data-line2');
    const desc = document.getElementById('sim8-desc');

    const data = rockyData[p];
    if (badge) badge.textContent = data.badge;
    if (line1) line1.textContent = data.title;
    if (line2) line2.textContent = data.sub;
    if (desc) desc.innerHTML = `<strong>${p.toUpperCase()}:</strong> Solid, rocky crust with a metallic core. Terrestrial planets are dense and rocky because intense solar wind in the early solar system blew light gases away.`;
}

// Sim 9: Outer Giants
const giantData = {
    jupiter: {
        badge: "Jupiter: Gas Giant King",
        title: "Jupiter: Gas Giant of Hydrogen & Helium",
        detail: "Mass exceeds all other 7 planets combined; Great Red Spot anticyclone raging 300+ yrs; 95 known moons."
    },
    saturn: {
        badge: "Saturn: Spectacular Rings",
        title: "Saturn: Icy Ring Wonder",
        detail: "Thousands of ringlets made of water-ice and rock chunks; lowest density of all planets (would float on water); 146 moons."
    },
    uranus: {
        badge: "Uranus: Sideways Ice Giant",
        title: "Uranus: 98° Extreme Axial Tilt",
        detail: "Rotates virtually on its side, rolling like a bowling ball along its orbit; pale blue-green methane atmosphere."
    },
    neptune: {
        badge: "Neptune: Supersonic Wind World",
        title: "Neptune: Outermost Known Giant (30 AU)",
        detail: "Deep azure blue methane atmosphere; fastest winds in solar system exceeding 2,000 km/h; takes 165 Earth years to orbit."
    }
};

function selectGiant(g) {
    const badge = document.getElementById('sim9-badge');
    const title = document.getElementById('sim9-data-title');
    const detail = document.getElementById('sim9-data-detail');
    const desc = document.getElementById('sim9-desc');

    const d = giantData[g];
    if (badge) badge.textContent = d.badge;
    if (title) title.textContent = d.title;
    if (detail) detail.textContent = d.detail;
    if (desc) desc.innerHTML = `<strong>${g.toUpperCase()}:</strong> Far from solar heat, volatile gases condensed into colossal gas and ice envelopes with extensive satellite and ring families.`;
}

// Sim 10: IAU Planetary Criteria
function testIAUObject(obj) {
    const badge = document.getElementById('sim10-badge');
    const body = document.getElementById('sim10-target-body');
    const heart = document.getElementById('sim10-heart');
    const nameLabel = document.getElementById('sim10-name-label');
    const chk3 = document.getElementById('sim10-chk3');
    const chk3Icon = document.getElementById('sim10-chk3-icon');
    const sub3 = document.getElementById('sim10-c3-sub');
    const verdict = document.getElementById('sim10-verdict');
    const desc = document.getElementById('sim10-desc');

    if (obj === 'earth') {
        if (badge) {
            badge.textContent = "Classification: Major Planet (Earth)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        }
        if (body) {
            body.setAttribute('fill', '#0284c7');
            body.setAttribute('stroke', '#38bdf8');
        }
        if (heart) heart.style.display = 'none';
        if (nameLabel) nameLabel.textContent = "Earth";
        if (chk3) chk3.setAttribute('fill', '#10b981');
        if (chk3Icon) chk3Icon.textContent = "✓";
        if (sub3) {
            sub3.textContent = "Cleared orbit of debris";
            sub3.className = "text-[7px] text-emerald-400";
        }
        if (verdict) verdict.textContent = "Earth meets ALL 3 criteria ➔ Full Classical Planet";
        if (desc) desc.innerHTML = "<strong>Major Planet Status:</strong> Earth's dominant gravity cleared all rival planetesimals along its orbital path, fulfilling every criterion.";
    } else {
        if (badge) {
            badge.textContent = "Classification: Dwarf Planet (Pluto)";
            badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        }
        if (body) {
            body.setAttribute('fill', '#a8a29e');
            body.setAttribute('stroke', '#e7e5e4');
        }
        if (heart) heart.style.display = 'inline';
        if (nameLabel) nameLabel.textContent = "Pluto";
        if (chk3) chk3.setAttribute('fill', '#ef4444');
        if (chk3Icon) chk3Icon.textContent = "✗";
        if (sub3) {
            sub3.textContent = "Shares orbit with Kuiper belt";
            sub3.className = "text-[7px] text-rose-400";
        }
        if (verdict) verdict.textContent = "Pluto meets 2 of 3 criteria ➔ Classified as Dwarf Planet";
        if (desc) desc.innerHTML = "<strong>Dwarf Planet:</strong> Pluto orbits the Sun and is spherical, but its mass is dwarfed by the thousands of icy objects sharing its orbit in the Kuiper Belt.";
    }
}

// Sim 11: Twinkle vs Steady Disk
function inspectLightSource(src) {
    const badge = document.getElementById('sim11-badge');
    const srcDot = document.getElementById('sim11-src-dot');
    const srcName = document.getElementById('sim11-src-name');
    const beamPath = document.getElementById('sim11-beam-path');
    const signal = document.getElementById('sim11-signal');
    const statusText = document.getElementById('sim11-status-text');
    const desc = document.getElementById('sim11-desc');

    if (src === 'star') {
        if (badge) badge.textContent = "Target: Distant Star (Point Source)";
        if (srcDot) {
            srcDot.setAttribute('r', '3');
            srcDot.setAttribute('fill', '#ffffff');
        }
        if (srcName) srcName.textContent = "Single Point Source";
        if (beamPath) beamPath.setAttribute('d', 'M 40,100 L 120,95 Q 160,115 200,90 L 270,100');
        if (signal) {
            signal.setAttribute('d', 'M 30,175 Q 45,155 60,180 T 90,160 T 120,182 T 150,158 T 180,180 T 210,160 T 240,180 T 270,165');
            signal.setAttribute('stroke', '#f59e0b');
        }
        if (statusText) statusText.textContent = "Narrow Ray Severely Deviated ➔ Intense Twinkling";
        if (desc) desc.innerHTML = "<strong>Point Source Twinkles:</strong> Starlight passes through shifting layers of warmer and colder air, refracting erratically to cause twinkling (scintillation).";
    } else {
        if (badge) badge.textContent = "Target: Nearby Planet (Extended Disk)";
        if (srcDot) {
            srcDot.setAttribute('r', '9');
            srcDot.setAttribute('fill', '#f59e0b');
        }
        if (srcName) srcName.textContent = "Extended Disk Source";
        if (beamPath) beamPath.setAttribute('d', 'M 40,95 L 120,96 Q 160,102 200,98 L 270,98 M 40,105 L 120,104 Q 160,98 200,102 L 270,102');
        if (signal) {
            signal.setAttribute('d', 'M 30,170 L 270,170');
            signal.setAttribute('stroke', '#10b981');
        }
        if (statusText) statusText.textContent = "Multi-Point Fluctuations Average Out ➔ Steady Glow";
        if (desc) desc.innerHTML = "<strong>Steady Planetary Disk:</strong> As an extended disk made of millions of light rays, when one point flickers brighter another flickers dimmer, averaging into a rock-steady shine.";
    }
}

// Sim 12: Lunar Orbit & Craters
let orbitAngle = 0;
function simulateOrbitStep() {
    orbitAngle = (orbitAngle + 45) % 360;
    const moonNode = document.getElementById('sim12-moon-node');
    const faceArrow = document.getElementById('sim12-face-arrow');
    const badge = document.getElementById('sim12-badge');
    const desc = document.getElementById('sim12-desc');

    const rad = orbitAngle * Math.PI / 180;
    const x = 160 + 100 * Math.cos(rad);
    const y = 100 + 60 * Math.sin(rad);

    if (moonNode) {
        moonNode.setAttribute('transform', `translate(${x.toFixed(1)}, ${y.toFixed(1)})`);
    }

    const angleToEarth = Math.atan2(100 - y, 160 - x);
    const ax = 14 * Math.cos(angleToEarth);
    const ay = 14 * Math.sin(angleToEarth);

    if (faceArrow) {
        faceArrow.setAttribute('x1', '0');
        faceArrow.setAttribute('y1', '0');
        faceArrow.setAttribute('x2', ax.toFixed(1));
        faceArrow.setAttribute('y2', ay.toFixed(1));
    }

    if (badge) badge.textContent = `Orbit Angle: ${orbitAngle}° (Tidally Locked)`;
    if (desc) desc.innerHTML = "<strong>Synchronous Rotation:</strong> Notice the red marker continuously points inward toward Earth. The Moon spins on its axis exactly once per orbit (~27.3 days).";
}

function impactMeteorite() {
    const desc = document.getElementById('sim12-desc');
    const title = document.getElementById('sim12-crater-title');
    if (title) title.textContent = "Meteorite Impact Preserved Permanently!";
    if (desc) desc.innerHTML = "<strong>Preservation Without Erosion:</strong> Unlike Earth where rain, wind, and vegetation erase craters, the Moon's airless vacuum keeps impact craters unchanged for billions of years.";
}

// Sim 13: Chandrayaan-3 South Pole
function drivePragyanRover() {
    const rover = document.getElementById('sim13-pragyan');
    const imprint = document.getElementById('sim13-imprint');
    const badge = document.getElementById('sim13-badge');
    const desc = document.getElementById('sim13-desc');

    if (rover) {
        rover.style.transition = 'transform 1s ease';
        rover.setAttribute('transform', 'translate(205, 150)');
    }
    if (imprint) imprint.setAttribute('opacity', '1');
    if (badge) badge.textContent = "Pragyan Rover: Rolling on Lunar Regolith";
    if (desc) desc.innerHTML = "<strong>Pragyan Exploration:</strong> The 26 kg 6-wheel rover rolled down Vikram's ramp, using laser-induced breakdown spectroscopy to analyze lunar elemental composition.";
}

function scanWaterIce() {
    const badge = document.getElementById('sim13-badge');
    const desc = document.getElementById('sim13-desc');

    if (badge) badge.textContent = "Radar Scan: Subsurface Water Ice Confirmed";
    if (desc) desc.innerHTML = "<strong>Permanently Shadowed Craters:</strong> South pole crater depths never receive direct sunlight, preserving water ice molecules discovered by India's Chandrayaan missions.";
}

// Sim 14: Asteroid Belt & Gravitational Dynamics
function highlightCeres() {
    const badge = document.getElementById('sim14-badge');
    const statusLine = document.getElementById('sim14-status-line');
    const desc = document.getElementById('sim14-desc');

    if (badge) badge.textContent = "Focus: Ceres (~940 km Diameter)";
    if (statusLine) statusLine.textContent = "Ceres: Largest asteroid and only dwarf planet inside Neptune's orbit";
    if (desc) desc.innerHTML = "<strong>Ceres Discovery:</strong> Discovered in 1801, Ceres contains roughly one-third of the entire Asteroid Belt's total mass and has a rocky core surrounded by an icy mantle.";
}

function stirJupiterGravity() {
    const badge = document.getElementById('sim14-badge');
    const statusLine = document.getElementById('sim14-status-line');
    const debris = document.getElementById('sim14-debris');
    const desc = document.getElementById('sim14-desc');

    if (debris) {
        debris.style.transition = 'transform 0.5s ease';
        debris.style.transformOrigin = '160px 100px';
        debris.style.transform = 'rotate(20deg)';
        setTimeout(() => { debris.style.transform = 'rotate(0deg)'; }, 500);
    }

    if (badge) badge.textContent = "Jupiter Orbital Resonance Active";
    if (statusLine) statusLine.textContent = "Gravitational tugs speed up collisions, smashing debris apart";
    if (desc) desc.innerHTML = "<strong>Kirkwood Gaps & Disruption:</strong> Jupiter's orbital resonance regularly gave passing planetesimals high velocity kicks, causing destructive collisions instead of coalescence.";
}

// Sim 15: Comet Anatomy & Sublimation
function orbitCometNearSun() {
    const comet = document.getElementById('sim15-comet');
    const ionTail = document.getElementById('sim15-ion-tail');
    const dustTail = document.getElementById('sim15-dust-tail');
    const badge = document.getElementById('sim15-badge');
    const desc = document.getElementById('sim15-desc');

    if (comet) {
        comet.setAttribute('transform', 'translate(130, 100)');
    }
    if (ionTail) {
        ionTail.setAttribute('points', '0,0 160,-22 155,-10');
        ionTail.setAttribute('opacity', '0.9');
    }
    if (dustTail) {
        dustTail.setAttribute('d', 'M 0,0 Q 80,20 150,50 L 145,62 Q 70,25 0,0 Z');
        dustTail.setAttribute('opacity', '0.85');
    }

    if (badge) badge.textContent = "Perihelion: Maximum Sublimation & Tail Length";
    if (desc) desc.innerHTML = "<strong>Tail Growth Near Sun:</strong> As solar radiation heats the nucleus, ices vaporize rapidly. Solar wind blows lightweight ions straight back, while photon pressure pushes heavier dust into a curving tail.";
}

function showHalleyPeriod() {
    const badge = document.getElementById('sim15-badge');
    const halleyText = document.getElementById('sim15-halley-text');
    const desc = document.getElementById('sim15-desc');

    if (badge) badge.textContent = "Halley's Comet: 76-Year Elliptical Orbit";
    if (halleyText) halleyText.textContent = "Last seen: 1986 | Next visible from Earth: mid-2061";
    if (desc) desc.innerHTML = "<strong>Periodic Comet:</strong> Edmond Halley calculated that comets observed in 1531, 1607, and 1682 were the same object returning every 75-76 years in an elongated orbit stretching past Neptune.";
}

// Sim 16: Milky Way (Akasha Ganga) & Cosmic Address
function pinpointSunLocation() {
    const badge = document.getElementById('sim16-badge');
    const address = document.getElementById('sim16-address');
    const desc = document.getElementById('sim16-desc');

    if (badge) badge.textContent = "Sun Position: Orion-Cygnus Arm (~26,000 ly)";
    if (address) address.textContent = "Earth ➔ Solar System ➔ Orion Arm ➔ Milky Way (Akasha Ganga)";
    if (desc) desc.innerHTML = "<strong>Our Galactic Home:</strong> We live roughly two-thirds of the way out from the galactic center, orbiting the core at 220 km/s in a cosmic year lasting 230 million Earth years.";
}

function scanExoplanets() {
    const badge = document.getElementById('sim16-badge');
    const address = document.getElementById('sim16-address');
    const desc = document.getElementById('sim16-desc');

    if (badge) badge.textContent = "Exoplanet Survey: 5,500+ Confirmed Worlds";
    if (address) address.textContent = "Goldilocks Zone: Distance where liquid water can pool";
    if (desc) desc.innerHTML = "<strong>Beyond Our Solar System:</strong> Space telescopes like Kepler and James Webb have proven that almost every star in the Milky Way hosts planets, many inside the habitable zone!";
}

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
    if ('speechSynthesis' in window) {
        selectedMaleVoice = getIndianMaleVoice();
    }
});
'''

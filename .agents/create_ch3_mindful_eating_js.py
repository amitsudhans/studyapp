"""
Script to generate .agents/class6_science_ch3_js.py containing the interactive JavaScript
for NCERT Class 6 Science Chapter 3: Mindful Eating: A Path to a Healthy Body.
"""

js_body = r'''
// Science Chapter 3 Interactive JavaScript
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

    // Clean text and split by sentences (periods, exclamation, question marks)
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
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-500/20 text-emerald-300 hover:bg-emerald-500/30 border border-emerald-500/30 flex items-center space-x-1.5 transition';
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
                btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30 flex items-center space-x-1.5 transition';
                btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
                if (badge) {
                    badge.textContent = 'Audio Lecture Ready';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
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
    const indicator = document.getElementById('slideIndicator');
    if (indicator) {
        indicator.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    }
    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
        progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;
    }
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
    }
    if (nextBtn) {
        if (currentSlide === totalSlides) {
            nextBtn.style.display = 'none';
        } else {
            nextBtn.style.display = 'inline-flex';
        }
    }
    if (lastSlideNotice) {
        lastSlideNotice.style.display = (currentSlide === totalSlides) ? 'block' : 'none';
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
function checkCheckpoint(cpId, selectedOption, correctOption, explanation) {
    const feedbackEl = document.getElementById(`cp-feedback-${cpId}`);
    const badgeEl = document.getElementById(`cp-badge-${cpId}`);
    if (!feedbackEl) return;

    if (selectedOption === correctOption) {
        feedbackEl.className = 'mt-3 p-3 rounded-lg text-sm bg-emerald-950/40 border border-emerald-500/50 text-emerald-300';
        feedbackEl.innerHTML = `<strong>Correct!</strong> ` + explanation;
        if (badgeEl) {
            badgeEl.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
            badgeEl.textContent = 'Solved';
        }
    } else {
        feedbackEl.className = 'mt-3 p-3 rounded-lg text-sm bg-rose-950/40 border border-rose-500/50 text-rose-300';
        feedbackEl.innerHTML = `<strong>Try again:</strong> Re-read the nutritional principle or biochemical mechanism carefully!`;
    }
    feedbackEl.style.display = 'block';
}

// Solution Modal
function openSolutionModal(title, question, correctAnswer, explanation) {
    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const questionEl = document.getElementById('modalQuestion');
    const answerEl = document.getElementById('modalAnswer');
    const explanationEl = document.getElementById('modalExplanation');

    if (modal && titleEl && questionEl && answerEl && explanationEl) {
        titleEl.textContent = title;
        questionEl.innerHTML = `<strong>Question:</strong> ${question}`;
        answerEl.innerHTML = `<strong>Correct Answer:</strong> ${correctAnswer}`;
        explanationEl.innerHTML = `<strong>Detailed Step-by-Step Solution:</strong><br>${explanation}`;
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
    const btnContainer = document.getElementById(`q-options-${qId}`);
    const feedbackBox = document.getElementById(`q-feedback-${qId}`);
    const solutionBtn = document.getElementById(`q-sol-btn-${qId}`);

    if (btnContainer) {
        const buttons = btnContainer.querySelectorAll('button');
        buttons.forEach((btn, index) => {
            const optLetter = String.fromCharCode(65 + index);
            btn.disabled = true;
            if (optLetter === correctOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-950/60 border border-emerald-500/60 text-emerald-300 shadow-sm';
            } else if (optLetter === selectedOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl text-xs sm:text-sm font-semibold bg-rose-950/60 border border-rose-500/60 text-rose-300 shadow-sm';
            } else {
                btn.className = 'w-full text-left p-3 rounded-xl text-xs sm:text-sm font-medium bg-slate-900/40 border border-slate-800/80 text-slate-500 opacity-60';
            }
        });
    }

    if (feedbackBox) {
        feedbackBox.style.display = 'block';
        if (selectedOpt === correctOpt) {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-xs sm:text-sm bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
            feedbackBox.innerHTML = `<strong>Correct! (${correctOpt})</strong> Outstanding nutritional understanding!`;
        } else {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-xs sm:text-sm bg-rose-950/40 border border-rose-500/40 text-rose-300';
            feedbackBox.innerHTML = `<strong>Incorrect (${selectedOpt}).</strong> The correct answer is <strong>${correctOpt}</strong>.`;
        }
    }

    if (solutionBtn) {
        solutionBtn.style.display = 'inline-flex';
    }
}

// -------------------------------------------------------------
// Simulator 1: The Biological Power Plant
// -------------------------------------------------------------
function setSim1Function(func) {
    ['energy', 'growth', 'defense', 'brain'].forEach(k => {
        const btn = document.getElementById(`sim1-btn-${k}`);
        if (btn) {
            btn.className = (k === func) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim1-svg');
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');

    if (func === 'energy') {
        badge.textContent = "Cellular Energy & Movement";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20";
        desc.innerHTML = "Carbohydrates and fats are converted into glucose and ATP, fueling heartbeat, continuous breathing, body warmth, and vigorous muscle locomotion.";
        svg.innerHTML = `
            <circle cx="225" cy="85" r="45" fill="#f59e0b" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
            <text x="225" y="80" fill="#fef08a" font-size="14" font-weight="bold" text-anchor="middle">Metabolic Engine</text>
            <text x="225" y="98" fill="#fcd34d" font-size="10" text-anchor="middle">Glucose → ATP Energy</text>
            <path d="M140,85 Q180,60 180,85" stroke="#f59e0b" stroke-width="3" fill="none"/>
            <path d="M310,85 Q270,110 270,85" stroke="#f59e0b" stroke-width="3" fill="none"/>
            <text x="225" y="160" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Carbs & Fats Provide Daily Metabolic Power</text>
        `;
    } else if (func === 'growth') {
        badge.textContent = "Tissue Growth & Wound Repair";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20";
        desc.innerHTML = "Proteins supply amino acids to assemble new muscle fibers, lengthen bones during puberty, and mend damaged skin cells when you scrape a knee.";
        svg.innerHTML = `
            <rect x="175" y="45" width="100" height="80" rx="10" fill="#065f46" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
            <text x="225" y="80" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="middle">Cellular Growth</text>
            <text x="225" y="98" fill="#6ee7b7" font-size="10" text-anchor="middle">Amino Acid Chains</text>
            <line x1="120" y1="85" x2="175" y2="85" stroke="#10b981" stroke-width="3"/>
            <line x1="275" y1="85" x2="330" y2="85" stroke="#10b981" stroke-width="3"/>
            <text x="225" y="160" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Proteins Rebuild and Expand Every Tissue</text>
        `;
    } else if (func === 'defense') {
        badge.textContent = "Immune Defense Shield";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-500/10 text-sky-400 border border-sky-500/20";
        desc.innerHTML = "Vitamins (A, C, D) and minerals (Zinc, Iron) arm circulating white blood cells and antibodies, destroying bacteria and viral invaders.";
        svg.innerHTML = `
            <polygon points="225,35 275,65 260,125 225,145 190,125 175,65" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
            <text x="225" y="85" fill="#bae6fd" font-size="13" font-weight="bold" text-anchor="middle">Immune Shield</text>
            <text x="225" y="105" fill="#7dd3fc" font-size="10" text-anchor="middle">Vitamins & Minerals</text>
            <text x="225" y="165" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Micro-nutrients Guard Against Pathogens</text>
        `;
    } else {
        badge.textContent = "Brain & Cognitive Sharpness";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-purple-500/10 text-purple-400 border border-purple-500/20";
        desc.innerHTML = "Glucose from carbohydrates powers brain neurons, while Iodine, B-complex vitamins, and Iron ensure rapid nerve conduction and memory retention.";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="50" ry="35" fill="#6b21a8" fill-opacity="0.3" stroke="#c084fc" stroke-width="2"/>
            <text x="225" y="80" fill="#f3e8ff" font-size="13" font-weight="bold" text-anchor="middle">Neural Matrix</text>
            <text x="225" y="98" fill="#d8b4fe" font-size="10" text-anchor="middle">Focus & Memory</text>
            <text x="225" y="160" fill="#e9d5ff" font-size="11" font-weight="bold" text-anchor="middle">Optimal Brain Function Demands Steady Nutrition</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 2: India's Regional Thali Explorer
// -------------------------------------------------------------
function setSim2Region(region) {
    ['punjab', 'karnataka', 'manipur'].forEach(k => {
        const btn = document.getElementById(`sim2-btn-${k}`);
        if (btn) {
            btn.className = (k === region) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim2-svg');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (region === 'punjab') {
        badge.textContent = "Punjab (North Alluvial Plains)";
        desc.innerHTML = "<strong>Punjab Thali:</strong> Fertile alluvial soil and chilly winters favor mustard greens (Sarson da saag), corn flatbread (Makki di roti), and churned white butter (Makhan). Packed with Iron, Vitamin A, and energy!";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="70" ry="50" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b" stroke-width="3"/>
            <!-- Corn flatbread -->
            <circle cx="195" cy="80" r="26" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
            <text x="195" y="84" fill="#713f12" font-size="9" font-weight="bold" text-anchor="middle">Makki Roti</text>
            <!-- Mustard Greens Bowl -->
            <circle cx="255" cy="80" r="24" fill="#14532d" stroke="#16a34a" stroke-width="2"/>
            <text x="255" y="84" fill="#a7f3d0" font-size="9" font-weight="bold" text-anchor="middle">Sarson Saag</text>
            <text x="225" y="160" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Rich in Iron, Plant Fiber & Healthy Lipids</text>
        `;
    } else if (region === 'karnataka') {
        badge.textContent = "Karnataka (Deccan Semi-Arid)";
        desc.innerHTML = "<strong>Karnataka Thali:</strong> Red rain-fed soils produce drought-hardy millets. Steamed Finger Millet balls (<em>Ragi mudde</em>) served with lentil vegetable <em>Sambar</em> provide tremendous Calcium and protein.";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="70" ry="50" fill="#831843" fill-opacity="0.3" stroke="#ec4899" stroke-width="3"/>
            <!-- Ragi Mudde Ball -->
            <circle cx="195" cy="80" r="24" fill="#4c0519" stroke="#9d174d" stroke-width="2"/>
            <text x="195" y="84" fill="#fbcfe8" font-size="9" font-weight="bold" text-anchor="middle">Ragi Mudde</text>
            <!-- Sambar Bowl -->
            <circle cx="255" cy="80" r="24" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
            <text x="255" y="84" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">Dal Sambar</text>
            <text x="225" y="160" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="middle">Superlative Natural Calcium (344 mg) & Protein</text>
        `;
    } else {
        badge.textContent = "Manipur (Northeastern Hills)";
        desc.innerHTML = "<strong>Manipur Thali:</strong> Lush hills and streams yield fermented seasonal vegetables and bamboo shoots (<em>Uttis</em>) mashed with herbs and chili (<em>Eromba</em>), delivering probiotics, vitamins, and minerals.";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="70" ry="50" fill="#065f46" fill-opacity="0.3" stroke="#10b981" stroke-width="3"/>
            <!-- Eromba bowl -->
            <circle cx="195" cy="80" r="24" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
            <text x="195" y="84" fill="#dcfce7" font-size="9" font-weight="bold" text-anchor="middle">Eromba</text>
            <!-- Uttis bowl -->
            <circle cx="255" cy="80" r="24" fill="#3f6212" stroke="#84cc16" stroke-width="2"/>
            <text x="255" y="84" fill="#ecfccb" font-size="9" font-weight="bold" text-anchor="middle">Uttis Shoot</text>
            <text x="225" y="160" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Natural Probiotics & Delicate Forest Micro-nutrients</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 3: Kitchen Evolution Timeline
// -------------------------------------------------------------
function setSim3Era(era) {
    ['chulha', 'silbatta', 'gas', 'blender'].forEach(k => {
        const btn = document.getElementById(`sim3-btn-${k}`);
        if (btn) {
            btn.className = (k === era) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim3-svg');
    const badge = document.getElementById('sim3-badge');
    const desc = document.getElementById('sim3-desc');

    if (era === 'chulha') {
        badge.textContent = "Clay Chulha (Firewood/Dung)";
        desc.innerHTML = "Traditional earthenware cooking over slow wood fire created distinctive flavors, but emitted dense indoor smoke (particulate matter) that affected women's respiratory health.";
        svg.innerHTML = `
            <!-- Mud Chulha horseshoe -->
            <path d="M180,130 C180,60 270,60 270,130" stroke="#78350f" stroke-width="16" fill="none"/>
            <!-- Flame -->
            <polygon points="225,120 215,85 225,60 235,85" fill="#f97316"/>
            <polygon points="225,115 220,90 225,75 230,90" fill="#fde047"/>
            <!-- Smoke plumes -->
            <circle cx="215" cy="40" r="10" fill="#64748b" fill-opacity="0.4"/>
            <circle cx="235" cy="25" r="14" fill="#64748b" fill-opacity="0.3"/>
            <text x="225" y="165" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Earthen Slow Cooking with Firewood Smoke</text>
        `;
    } else if (era === 'silbatta') {
        badge.textContent = "Sil-Batta (Manual Granite Grinder)";
        desc.innerHTML = "Heavy flat granite stone and cylindrical pestle crushed spices, garlic, and fresh herbs by hand. Friction released natural aromatic oils while retaining coarse dietary fiber.";
        svg.innerHTML = `
            <!-- Flat stone slab -->
            <rect x="150" y="80" width="150" height="40" rx="6" fill="#334155" stroke="#64748b" stroke-width="2"/>
            <!-- Roller stone (batta) -->
            <ellipse cx="225" cy="80" rx="30" ry="12" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
            <!-- Ground spice paste -->
            <ellipse cx="225" cy="90" rx="20" ry="5" fill="#d97706"/>
            <text x="225" y="165" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Manual Stone Crushing Retained Essential Aromatic Oils</text>
        `;
    } else if (era === 'gas') {
        badge.textContent = "Modern LPG & Induction Stoves";
        desc.innerHTML = "Smokeless blue LPG flame and electromagnetic induction provide precise, instant thermal control, protecting lungs from indoor pollution and ensuring uniform cooking.";
        svg.innerHTML = `
            <!-- Modern stove base -->
            <rect x="160" y="90" width="130" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <!-- Clean blue gas burner ring -->
            <circle cx="225" cy="90" r="18" fill="none" stroke="#0ea5e9" stroke-width="4"/>
            <circle cx="225" cy="90" r="8" fill="#38bdf8"/>
            <text x="225" y="165" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Smokeless, Clean Thermal Heat Control</text>
        `;
    } else {
        badge.textContent = "High-Speed Electric Mixer-Grinder";
        desc.innerHTML = "High-velocity stainless steel rotating blades pulverize wet and dry spices into fine purees in seconds, saving tremendous kitchen time and physical labor.";
        svg.innerHTML = `
            <!-- Motor base -->
            <rect x="185" y="95" width="80" height="45" rx="8" fill="#334155" stroke="#64748b"/>
            <!-- Stainless Steel Jar -->
            <polygon points="195,95 255,95 250,45 200,45" fill="#94a3b8" stroke="#cbd5e1" stroke-width="2"/>
            <!-- Rotating blade inside jar -->
            <line x1="210" y1="85" x2="240" y2="85" stroke="#f59e0b" stroke-width="3"/>
            <text x="225" y="165" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Instant Motorized Homogenization & Time Efficiency</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 4: Carbohydrate Fuel Meter
// -------------------------------------------------------------
function setSim4Carb(carb) {
    ['starch', 'wholegrain', 'sugar'].forEach(k => {
        const btn = document.getElementById(`sim4-btn-${k}`);
        if (btn) {
            btn.className = (k === carb) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim4-svg');
    const badge = document.getElementById('sim4-badge');
    const desc = document.getElementById('sim4-desc');

    if (carb === 'starch') {
        badge.textContent = "Complex Starch (Potato/Rice)";
        desc.innerHTML = "Complex starch chains are cleaved gradually by amylase enzymes, delivering a <strong>steady, prolonged energy release</strong> over several hours without fatigue.";
        svg.innerHTML = `
            <!-- Axis lines -->
            <line x1="60" y1="130" x2="400" y2="130" stroke="#475569" stroke-width="2"/>
            <line x1="60" y1="30" x2="60" y2="130" stroke="#475569" stroke-width="2"/>
            <!-- Smooth steady energy curve -->
            <path d="M60,130 Q160,50 380,80" stroke="#f59e0b" stroke-width="4" fill="none"/>
            <text x="380" y="70" fill="#fde68a" font-size="10">Steady Fuel</text>
            <text x="225" y="165" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Sustained Blood Glucose: Ideal for Long Study & Activity</text>
        `;
    } else if (carb === 'wholegrain') {
        badge.textContent = "Whole Grains (Wheat/Millets)";
        desc.innerHTML = "Intact outer bran and germ slow down digestion even further, providing <strong>maximum sustained stamina</strong> and vital B-vitamins for active school days.";
        svg.innerHTML = `
            <line x1="60" y1="130" x2="400" y2="130" stroke="#475569" stroke-width="2"/>
            <line x1="60" y1="30" x2="60" y2="130" stroke="#475569" stroke-width="2"/>
            <!-- Optimal plateau curve -->
            <path d="M60,130 Q120,65 240,65 Q340,65 390,95" stroke="#10b981" stroke-width="4" fill="none"/>
            <text x="240" y="55" fill="#a7f3d0" font-size="10" text-anchor="middle">Long Plateau</text>
            <text x="225" y="165" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Fiber-Rich Carbohydrates Prevent Energy Dips</text>
        `;
    } else {
        badge.textContent = "Refined Sugar (Candy/Soda)";
        desc.innerHTML = "Simple sugars enter blood in minutes, causing a violent <strong>glucose spike followed by a steep crash</strong> that leaves you tired, moody, and craving more snacks!";
        svg.innerHTML = `
            <line x1="60" y1="130" x2="400" y2="130" stroke="#475569" stroke-width="2"/>
            <line x1="60" y1="30" x2="60" y2="130" stroke="#475569" stroke-width="2"/>
            <!-- Sharp spike and crash -->
            <path d="M60,130 Q120,20 160,40 Q200,125 380,128" stroke="#ef4444" stroke-width="4" fill="none"/>
            <text x="160" y="30" fill="#fca5a5" font-size="10">Spike & Crash!</text>
            <text x="225" y="165" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Sudden Energy High Followed by Severe Fatigue & Cravings</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 5: Fats Energy Density Vault
// -------------------------------------------------------------
function setSim5Fat(fat) {
    ['density', 'insulation', 'vitamins'].forEach(k => {
        const btn = document.getElementById(`sim5-btn-${k}`);
        if (btn) {
            btn.className = (k === fat) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim5-svg');
    const badge = document.getElementById('sim5-badge');
    const desc = document.getElementById('sim5-desc');

    if (fat === 'density') {
        badge.textContent = "Calorie Vault (9 kcal vs 4 kcal)";
        desc.innerHTML = "Fats are nature's most compact energy storage! 1 gram of fat yields <strong>9 kcal</strong>, while 1 gram of carb or protein yields only <strong>4 kcal</strong>.";
        svg.innerHTML = `
            <!-- Balance scale beam -->
            <line x1="120" y1="75" x2="330" y2="75" stroke="#94a3b8" stroke-width="4"/>
            <polygon points="225,75 215,115 235,115" fill="#64748b"/>
            <!-- 1g Fat Box -->
            <rect x="100" y="80" width="60" height="40" rx="6" fill="#f59e0b"/>
            <text x="130" y="105" fill="#713f12" font-size="10" font-weight="bold" text-anchor="middle">1g Fat = 9 kcal</text>
            <!-- 1g Carb Box -->
            <rect x="290" y="40" width="60" height="35" rx="6" fill="#0284c7"/>
            <text x="320" y="62" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">1g Carb = 4 kcal</text>
            <text x="225" y="165" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Fats Pack Over Double the Energy of Carbohydrates</text>
        `;
    } else if (fat === 'insulation') {
        badge.textContent = "Thermal Insulation & Organ Cushion";
        desc.innerHTML = "Subcutaneous adipose fat beneath our skin traps metabolic heat like an internal thermal blanket, shielding muscles and internal organs from cold shock.";
        svg.innerHTML = `
            <rect x="150" y="40" width="150" height="20" fill="#f43f5e" rx="4"/>
            <text x="225" y="55" fill="#ffffff" font-size="9" text-anchor="middle">Skin Epidermis</text>
            <rect x="150" y="65" width="150" height="35" fill="#fbbf24" rx="4"/>
            <text x="225" y="87" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle">Subcutaneous Fat Layer</text>
            <rect x="150" y="105" width="150" height="25" fill="#991b1b" rx="4"/>
            <text x="225" y="122" fill="#fecaca" font-size="9" text-anchor="middle">Core Muscle Tissue</text>
            <text x="225" y="165" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Thermal Blanket Preserves Internal Body Heat</text>
        `;
    } else {
        badge.textContent = "Fat-Soluble Vitamin Carrier";
        desc.innerHTML = "Vitamins A, D, E, and K are fat-soluble. Without healthy dietary lipids in your meals, your digestive tract cannot absorb these critical protective vitamins!";
        svg.innerHTML = `
            <circle cx="225" cy="85" r="45" fill="#d97706" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
            <text x="225" y="80" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">Lipid Droplet</text>
            <text x="225" y="98" fill="#fef08a" font-size="10" text-anchor="middle">Carrying Vit A, D, E, K</text>
            <text x="225" y="165" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Essential Vehicle for Vitamin Absorption</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 6: Protein Muscle & Growth Builder
// -------------------------------------------------------------
function setSim6Protein(prot) {
    ['soyabean', 'pulses', 'repair'].forEach(k => {
        const btn = document.getElementById(`sim6-btn-${k}`);
        if (btn) {
            btn.className = (k === prot) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim6-svg');
    const badge = document.getElementById('sim6-badge');
    const desc = document.getElementById('sim6-desc');

    if (prot === 'soyabean') {
        badge.textContent = "Soyabean: Plant Protein King";
        desc.innerHTML = "Soyabean contains an astounding <strong>36% to 40% protein by weight</strong>—far higher than wheat, rice, or eggs! It provides all essential amino acids for growth.";
        svg.innerHTML = `
            <!-- Percentage bar -->
            <rect x="80" y="65" width="290" height="35" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <rect x="80" y="65" width="200" height="35" rx="8" fill="#10b981"/>
            <text x="180" y="88" fill="#022c22" font-size="12" font-weight="bold" text-anchor="middle">Soyabean: ~40% Pure Protein</text>
            <text x="330" y="88" fill="#94a3b8" font-size="10" text-anchor="middle">Other Nutrients</text>
            <text x="225" y="155" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Unequaled Champion of Plant-Based Body Building</text>
        `;
    } else if (prot === 'pulses') {
        badge.textContent = "Pulses, Paneer & Milk";
        desc.innerHTML = "Daily Indian staples like moong dal, chana, toor dal, and fresh paneer deliver complete protein profiles when paired with whole grains like rice or roti!";
        svg.innerHTML = `
            <circle cx="170" cy="85" r="35" fill="#b45309" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
            <text x="170" y="90" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Dals (22%)</text>
            <circle cx="280" cy="85" r="35" fill="#047857" fill-opacity="0.4" stroke="#10b981" stroke-width="2"/>
            <text x="280" y="90" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Paneer (18%)</text>
            <line x1="205" y1="85" x2="245" y2="85" stroke="#38bdf8" stroke-width="3"/>
            <text x="225" y="155" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Dal + Roti = Complete Essential Amino Acid Profile</text>
        `;
    } else {
        badge.textContent = "Muscle Fiber Healing in Action";
        desc.innerHTML = "When muscle fibers experience micro-tears during sports or daily play, circulating amino acids link together like bricks to repair and strengthen the muscle.";
        svg.innerHTML = `
            <!-- Muscle strands with healing bridge -->
            <line x1="80" y1="80" x2="180" y2="80" stroke="#f43f5e" stroke-width="8" stroke-linecap="round"/>
            <line x1="270" y1="80" x2="370" y2="80" stroke="#f43f5e" stroke-width="8" stroke-linecap="round"/>
            <!-- Amino acid bridge -->
            <rect x="185" y="70" width="80" height="20" rx="6" fill="#10b981"/>
            <text x="225" y="85" fill="#022c22" font-size="9" font-weight="bold" text-anchor="middle">Amino Acids Repair</text>
            <text x="225" y="155" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Active Muscle Hypertrophy and Cellular Recovery</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 7: The Vitamin Protective Shield
// -------------------------------------------------------------
function setSim7Vitamin(vit) {
    ['A', 'B', 'C', 'D'].forEach(k => {
        const btn = document.getElementById(`sim7-btn-${k}`);
        if (btn) {
            btn.className = (k === vit) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim7-svg');
    const badge = document.getElementById('sim7-badge');
    const desc = document.getElementById('sim7-desc');

    if (vit === 'A') {
        badge.textContent = "Vitamin A (Sharp Eyesight & Skin)";
        desc.innerHTML = "Found in carrots, papayas, and mangoes. Essential for synthesizing the retina photopigment <em>rhodopsin</em>, preventing night blindness and keeping skin healthy.";
        svg.innerHTML = `
            <!-- Eye drawing -->
            <ellipse cx="225" cy="80" rx="45" ry="25" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
            <circle cx="225" cy="80" r="14" fill="#0284c7"/>
            <circle cx="225" cy="80" r="6" fill="#0f172a"/>
            <text x="225" y="155" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Protects Retina Rod Cells for Twilight Vision</text>
        `;
    } else if (vit === 'B') {
        badge.textContent = "Vitamin B1 (Nerve & Heart Function)";
        desc.innerHTML = "Found in whole grains and legumes. Acts as a co-enzyme in cellular respiration, facilitating electrical nerve impulses and maintaining healthy cardiac muscles.";
        svg.innerHTML = `
            <!-- Nerve neuron impulse -->
            <circle cx="160" cy="80" r="16" fill="#6366f1"/>
            <line x1="176" y1="80" x2="290" y2="80" stroke="#818cf8" stroke-width="4"/>
            <circle cx="290" cy="80" r="12" fill="#a855f7"/>
            <text x="225" y="155" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">Fuels Fast Nerve Signals and Cellular Respiration</text>
        `;
    } else if (vit === 'C') {
        badge.textContent = "Vitamin C (Infection Defense & Gums)";
        desc.innerHTML = "Found in Indian gooseberry (Amla) and lemons. Powerful antioxidant that heals bleeding gums, synthesizes collagen, and empowers white blood cells to fight infections.";
        svg.innerHTML = `
            <!-- Glowing citrus defense shield -->
            <circle cx="225" cy="80" r="35" fill="#f59e0b" stroke="#eab308" stroke-width="3"/>
            <text x="225" y="85" fill="#713f12" font-size="11" font-weight="bold" text-anchor="middle">Amla Power</text>
            <text x="225" y="155" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Heals Gums, Mends Wounds, and Destroys Microbes</text>
        `;
    } else {
        badge.textContent = "Vitamin D (Morning Sunlight & Bones)";
        desc.innerHTML = "Synthesized naturally in skin by gentle morning sunshine! Promotes intestinal calcium absorption, preventing soft bone rickets and strengthening teeth.";
        svg.innerHTML = `
            <!-- Sun rays touching bone -->
            <circle cx="150" cy="75" r="22" fill="#f59e0b"/>
            <line x1="175" y1="75" x2="270" y2="75" stroke="#fde047" stroke-width="3" stroke-dasharray="4,4"/>
            <rect x="270" y="60" width="30" height="30" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
            <text x="285" y="80" fill="#334155" font-size="9" font-weight="bold" text-anchor="middle">Bone</text>
            <text x="225" y="155" fill="#bae6fd" font-size="11" font-weight="bold" text-anchor="middle">Sunlight Exposure Drives Bone Mineralization</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 8: Mineral Core Trio
// -------------------------------------------------------------
function setSim8Mineral(min) {
    ['calcium', 'iodine', 'iron'].forEach(k => {
        const btn = document.getElementById(`sim8-btn-${k}`);
        if (btn) {
            btn.className = (k === min) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim8-svg');
    const badge = document.getElementById('sim8-badge');
    const desc = document.getElementById('sim8-desc');

    if (min === 'calcium') {
        badge.textContent = "Calcium (Skeletal Framework)";
        desc.innerHTML = "Present in milk, paneer, and ragi. Formulates calcium hydroxyapatite crystals that give human bones rigidity and allow teeth to chew tough foods safely.";
        svg.innerHTML = `
            <rect x="180" y="55" width="90" height="50" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
            <text x="225" y="85" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">Dense Bone</text>
            <text x="225" y="155" fill="#f1f5f9" font-size="11" font-weight="bold" text-anchor="middle">Prevents Fractures and Strengthens Enamel</text>
        `;
    } else if (min === 'iodine') {
        badge.textContent = "Iodine (Thyroid Gland in Neck)";
        desc.innerHTML = "Present in iodised table salt. Enables the thyroid gland to produce thyroxine hormone, regulating metabolic rate, height growth, and mental acuity in children.";
        svg.innerHTML = `
            <!-- Butterfly shaped thyroid in neck -->
            <path d="M190,65 C175,80 180,105 200,95 C215,85 225,85 225,85 C225,85 235,85 250,95 C270,105 275,80 260,65 Z" fill="#991b1b" stroke="#f87171" stroke-width="2"/>
            <text x="225" y="85" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Thyroid</text>
            <text x="225" y="155" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Prevents Neck Goitre and Protects Mental Development</text>
        `;
    } else {
        badge.textContent = "Iron (Red Blood Hemoglobin)";
        desc.innerHTML = "Present in jaggery, spinach, and dates. Forms the central binding atom in hemoglobin, catching oxygen in lungs and releasing it into active tissues.";
        svg.innerHTML = `
            <!-- Red blood cell disc -->
            <ellipse cx="225" cy="80" rx="40" ry="24" fill="#dc2626" stroke="#ef4444" stroke-width="2"/>
            <circle cx="225" cy="80" r="10" fill="#991b1b"/>
            <text x="225" y="84" fill="#fef2f2" font-size="10" font-weight="bold" text-anchor="middle">O2</text>
            <text x="225" y="155" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Oxygen Carrier: Prevents Chronic Anemic Fatigue</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 9: Fiber & Water Motility Simulator
// -------------------------------------------------------------
function setSim9Mode(mode) {
    const isFiber = (mode === 'fiber');
    document.getElementById('sim9-btn-fiber').className = isFiber ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim9-btn-water').className = !isFiber ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim9-svg');
    const badge = document.getElementById('sim9-badge');
    const desc = document.getElementById('sim9-desc');

    if (isFiber) {
        badge.textContent = "Roughage: Smooth Bowel Peristalsis";
        desc.innerHTML = "Plant cellulose fiber absorbs water and expands softly inside the colon, stimulating muscular peristalsis that sweeps out digestive waste and prevents constipation.";
        svg.innerHTML = `
            <!-- Colon channel with soft bulk moving smoothly -->
            <path d="M120,80 Q225,50 330,80" stroke="#10b981" stroke-width="24" fill="none" stroke-linecap="round"/>
            <circle cx="200" cy="72" r="8" fill="#14532d"/>
            <circle cx="230" cy="70" r="9" fill="#14532d"/>
            <circle cx="260" cy="72" r="8" fill="#14532d"/>
            <text x="225" y="155" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Adds Healthy Bulk for Regular, Painless Bowel Evacuation</text>
        `;
    } else {
        badge.textContent = "Water: Toxin Solvation & Renal Clearance";
        desc.innerHTML = "Water dissolves urea, mineral salts, and cellular toxins. Kidneys filter blood continuously, excreting dissolved wastes via urine and regulating core temperature via sweat.";
        svg.innerHTML = `
            <!-- Kidney bean shape with fluid filtration stream -->
            <path d="M180,60 C180,40 240,40 240,65 C240,85 220,85 220,105 C220,125 180,125 180,100 Z" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
            <line x1="220" y1="105" x2="270" y2="125" stroke="#7dd3fc" stroke-width="4" stroke-linecap="round"/>
            <text x="225" y="155" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Kidneys Filter 180 Liters of Fluid Daily with Water</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 10: Starch Iodine Lab
// -------------------------------------------------------------
function runSim10Test(sample) {
    ['potato', 'rice', 'butter'].forEach(k => {
        const btn = document.getElementById(`sim10-btn-${k}`);
        if (btn) {
            btn.className = (k === sample) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim10-svg');
    const badge = document.getElementById('sim10-badge');
    const desc = document.getElementById('sim10-desc');

    if (sample === 'potato') {
        badge.textContent = "Positive Result: Intense Blue-Black!";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
        desc.innerHTML = "When yellowish-brown dilute iodine touches the raw potato slice, it reacts with amylose starch coils, forming an <strong>instant deep blue-black stain</strong> (+ Positive).";
        svg.innerHTML = `
            <!-- Potato slice -->
            <ellipse cx="225" cy="95" rx="65" ry="40" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
            <!-- Blue black reaction patch -->
            <ellipse cx="225" cy="95" rx="35" ry="20" fill="#1e1b4b" stroke="#312e81" stroke-width="2"/>
            <!-- Dropper above -->
            <rect x="222" y="25" width="6" height="35" fill="#94a3b8"/>
            <circle cx="225" cy="65" r="3" fill="#1e1b4b"/>
            <text x="225" y="165" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Conclusive Positive Confirmation of Starch</text>
        `;
    } else if (sample === 'rice') {
        badge.textContent = "Positive Result: Intense Blue-Black!";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
        desc.innerHTML = "Boiled rice is rich in gelatinized starch. Two drops of dilute iodine solution instantly turn the grains a <strong>striking blue-black color</strong> (+ Positive).";
        svg.innerHTML = `
            <ellipse cx="225" cy="95" rx="60" ry="35" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
            <ellipse cx="225" cy="95" rx="30" ry="18" fill="#172554"/>
            <text x="225" y="165" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Abundant Cereal Starch Confirmed</text>
        `;
    } else {
        badge.textContent = "Negative Result: Stays Light Brown";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        desc.innerHTML = "Butter contains pure lipids and zero carbohydrates. The iodine solution retains its original <strong>yellow-brown tint with no blue-black change</strong> (− Negative).";
        svg.innerHTML = `
            <rect x="180" y="70" width="90" height="45" rx="6" fill="#fef08a" stroke="#facc15" stroke-width="2"/>
            <!-- Light brown iodine droplet remaining unchanged -->
            <ellipse cx="225" cy="92" rx="14" ry="8" fill="#b45309"/>
            <text x="225" y="165" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">No Blue-Black Color Shift (Zero Starch in Lipids)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 11: Fat Translucent Paper Lab
// -------------------------------------------------------------
function runSim11Test(sample) {
    ['peanut', 'butter', 'water'].forEach(k => {
        const btn = document.getElementById(`sim11-btn-${k}`);
        if (btn) {
            btn.className = (k === sample) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim11-svg');
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');

    if (sample === 'peanut' || sample === 'butter') {
        badge.textContent = "Positive Result: Translucent Greasy Patch!";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        desc.innerHTML = `When ${sample === 'peanut' ? 'crushed groundnut' : 'butter'} is pressed on white paper and dried, an oily spot remains. Light passes partially through, creating a <strong>translucent patch</strong> (+ Positive).`;
        svg.innerHTML = `
            <!-- White paper sheet -->
            <rect x="145" y="30" width="160" height="110" rx="4" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
            <!-- Translucent greasy circular patch letting light through -->
            <circle cx="225" cy="85" r="28" fill="#fef08a" fill-opacity="0.8" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="225" y="88" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">Oily Patch</text>
            <text x="225" y="165" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Persistent Translucency Confirms Dietary Fat</text>
        `;
    } else {
        badge.textContent = "Negative Result: Water Dries Completely Opaque";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30";
        desc.innerHTML = "A water drop makes paper wet initially, but after evaporation in air, the paper returns to being completely dry and <strong>opaque</strong> (− Negative for fat).";
        svg.innerHTML = `
            <rect x="145" y="30" width="160" height="110" rx="4" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
            <text x="225" y="88" fill="#64748b" font-size="10" text-anchor="middle">Paper Dries Dry & Opaque</text>
            <text x="225" y="165" fill="#bae6fd" font-size="11" font-weight="bold" text-anchor="middle">Water Evaporates Completely with Zero Residue</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 12: Protein Biuret Lab
// -------------------------------------------------------------
function runSim12Step(sample) {
    ['dal', 'soya', 'sugar'].forEach(k => {
        const btn = document.getElementById(`sim12-btn-${k}`);
        if (btn) {
            btn.className = (k === sample) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim12-svg');
    const badge = document.getElementById('sim12-badge');
    const desc = document.getElementById('sim12-desc');

    if (sample === 'dal' || sample === 'soya') {
        badge.textContent = "Positive Result: Vivid Royal Violet!";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30";
        desc.innerHTML = `Adding 2 drops of blue copper sulfate and 10 drops of caustic soda to mashed ${sample === 'dal' ? 'boiled dal' : 'soaked soyabean'} turns the liquid into a <strong>royal violet/purple color</strong> (+ Positive).`;
        svg.innerHTML = `
            <!-- Test tube contour -->
            <rect x="205" y="30" width="40" height="95" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
            <!-- Violet protein solution inside tube -->
            <rect x="207" y="65" width="36" height="58" rx="6" fill="#7e22ce"/>
            <text x="225" y="100" fill="#f3e8ff" font-size="10" font-weight="bold" text-anchor="middle">Violet</text>
            <text x="225" y="165" fill="#d8b4fe" font-size="11" font-weight="bold" text-anchor="middle">Peptide Bonds Yield Distinct Violet Color</text>
        `;
    } else {
        badge.textContent = "Negative Result: Stays Light Blue";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        desc.innerHTML = "Sugar syrup has zero peptide bonds. The liquid remains a pale blue from unreacted copper sulfate with <strong>no violet color change</strong> (− Negative).";
        svg.innerHTML = `
            <rect x="205" y="30" width="40" height="95" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
            <rect x="207" y="65" width="36" height="58" rx="6" fill="#0284c7" fill-opacity="0.6"/>
            <text x="225" y="100" fill="#e0f2fe" font-size="9" text-anchor="middle">Light Blue</text>
            <text x="225" y="165" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">No Violet Color Formed (Carbohydrates Lack Peptide Bonds)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 13: The Balanced Thali Architect
// -------------------------------------------------------------
function setSim13Diet(diet) {
    ['balanced', 'junk', 'fortified'].forEach(k => {
        const btn = document.getElementById(`sim13-btn-${k}`);
        if (btn) {
            btn.className = (k === diet) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim13-svg');
    const badge = document.getElementById('sim13-badge');
    const desc = document.getElementById('sim13-desc');

    if (diet === 'balanced') {
        badge.textContent = "Optimal Balanced Indian Thali";
        desc.innerHTML = "<strong>Harmonious Proportions:</strong> 50% Vegetables & Fruits (Vitamins/Roughage), 25% Whole Grains (Energy Carbs), 20% Dals/Paneer (Proteins), and 5% Healthy Oils/Curd (Fats).";
        svg.innerHTML = `
            <!-- Thali plate circle -->
            <circle cx="225" cy="85" r="55" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
            <!-- Roti & Rice wedge -->
            <path d="M225,85 L225,30 A55,55 0 0,1 280,85 Z" fill="#f59e0b"/>
            <!-- Dal bowl -->
            <path d="M225,85 L280,85 A55,55 0 0,1 225,140 Z" fill="#0284c7"/>
            <!-- Vegetables & Salad half -->
            <path d="M225,85 L225,140 A55,55 0 0,1 225,30 Z" fill="#15803d"/>
            <text x="225" y="165" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Complete Harmony: Growth, Energy, and Disease Defense</text>
        `;
    } else if (diet === 'junk') {
        badge.textContent = "Junk Food (Empty Calorie Trap)";
        desc.innerHTML = "<strong>Imbalanced Trap:</strong> 85% Refined Sugars, Sodium & Saturated Fat, but virtually 0% Fiber, Proteins, or Vitamins. Promotes childhood obesity and metabolic sluggishness.";
        svg.innerHTML = `
            <circle cx="225" cy="85" r="55" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
            <!-- Imbalanced red/yellow wedge -->
            <path d="M225,85 L225,30 A55,55 0 1,1 180,120 Z" fill="#dc2626"/>
            <text x="225" y="90" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Excess Fat/Sugar</text>
            <text x="225" y="165" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Lacks Micronutrients and Causes Chronic Nutritional Deficiencies</text>
        `;
    } else {
        badge.textContent = "Fortified Staples (+F Logo)";
        desc.innerHTML = "Staple foods scientifically enriched with micronutrients (Iodised salt, Vitamin A & D milk, Iron wheat flour) under FSSAI standards to eradicate hidden hunger.";
        svg.innerHTML = `
            <!-- Blue +F logo badge -->
            <rect x="185" y="50" width="80" height="70" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <text x="225" y="85" fill="#ffffff" font-size="22" font-weight="bold" text-anchor="middle">+F</text>
            <text x="225" y="105" fill="#bae6fd" font-size="9" text-anchor="middle">FSSAI Fortified</text>
            <text x="225" y="165" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Targeted Elimination of Anemia, Goitre & Rickets</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 14: Millet Super Grain Harvest
// -------------------------------------------------------------
function setSim14Millet(millet) {
    ['ragi', 'bajra', 'jowar', 'water'].forEach(k => {
        const btn = document.getElementById(`sim14-btn-${k}`);
        if (btn) {
            btn.className = (k === millet) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim14-svg');
    const badge = document.getElementById('sim14-badge');
    const desc = document.getElementById('sim14-desc');

    if (millet === 'ragi') {
        badge.textContent = "Ragi (Finger Millet) - Calcium King";
        desc.innerHTML = "Contains a staggering <strong>344 mg of Calcium per 100g</strong> (over 30 times more than polished rice), plus abundant dietary fiber that prevents diabetes.";
        svg.innerHTML = `
            <circle cx="225" cy="80" r="40" fill="#831843" fill-opacity="0.4" stroke="#ec4899" stroke-width="2"/>
            <text x="225" y="75" fill="#fbcfe8" font-size="13" font-weight="bold" text-anchor="middle">Ragi</text>
            <text x="225" y="95" fill="#f472b6" font-size="10" text-anchor="middle">344 mg Calcium</text>
            <text x="225" y="155" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="middle">Superior Bone Mineralization & High Dietary Fiber</text>
        `;
    } else if (millet === 'bajra') {
        badge.textContent = "Bajra (Pearl Millet) - Iron Dynamo";
        desc.innerHTML = "Rich in dietary Iron (8 mg/100g) and phosphorus. Provides long-lasting metabolic warmth and prevents iron-deficiency anemia in desert and arid zones.";
        svg.innerHTML = `
            <circle cx="225" cy="80" r="40" fill="#b45309" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
            <text x="225" y="75" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">Bajra</text>
            <text x="225" y="95" fill="#fde047" font-size="10" text-anchor="middle">8 mg Iron (Fe)</text>
            <text x="225" y="155" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Combats Anemia and Delivers Dense Warmth</text>
        `;
    } else if (millet === 'jowar') {
        badge.textContent = "Jowar (Sorghum) - Antioxidant Rich";
        desc.innerHTML = "Gluten-free cereal packed with polyphenolic antioxidants and complex resistant starches that protect heart health and ensure smooth digestion.";
        svg.innerHTML = `
            <circle cx="225" cy="80" r="40" fill="#065f46" fill-opacity="0.4" stroke="#10b981" stroke-width="2"/>
            <text x="225" y="75" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="middle">Jowar</text>
            <text x="225" y="95" fill="#6ee7b7" font-size="10" text-anchor="middle">Gluten-Free Fiber</text>
            <text x="225" y="155" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Heart-Friendly Antioxidants & Metabolic Regulation</text>
        `;
    } else {
        badge.textContent = "Water Footprint: Rice vs Millets";
        desc.innerHTML = "1 kg of polished white rice requires up to <strong>4,000 liters of water</strong>, whereas hardy millets need only <strong>300–400 liters</strong> to produce the same grain!";
        svg.innerHTML = `
            <!-- Water tank rice -->
            <rect x="100" y="45" width="80" height="70" fill="#0284c7" fill-opacity="0.6"/>
            <text x="140" y="85" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Rice: 4,000 L</text>
            <!-- Water tank millet -->
            <rect x="270" y="95" width="80" height="20" fill="#10b981" fill-opacity="0.8"/>
            <text x="310" y="110" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Millet: 400 L</text>
            <text x="225" y="155" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Millets Save 90% of Agricultural Irrigation Water</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 15: Food Miles & Carbon Footprint
// -------------------------------------------------------------
function setSim15Miles(miles) {
    const isLocal = (miles === 'local');
    document.getElementById('sim15-btn-local').className = isLocal ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim15-btn-imported').className = !isLocal ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim15-svg');
    const badge = document.getElementById('sim15-badge');
    const desc = document.getElementById('sim15-desc');

    if (isLocal) {
        badge.textContent = "Local Produce (15 km) - Ultra Low Carbon";
        desc.innerHTML = "Harvested yesterday at a nearby farm. Reaches your plate with <strong>near-zero transport emissions</strong>, maximum natural Vitamin C content, and no synthetic waxing.";
        svg.innerHTML = `
            <line x1="120" y1="85" x2="330" y2="85" stroke="#10b981" stroke-width="4"/>
            <!-- Farm icon -->
            <circle cx="120" cy="85" r="16" fill="#047857"/>
            <text x="120" y="89" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">Farm</text>
            <!-- Plate icon -->
            <circle cx="330" cy="85" r="16" fill="#047857"/>
            <text x="330" y="89" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">Plate</text>
            <!-- Delivery tractor -->
            <rect x="210" y="70" width="30" height="15" rx="3" fill="#10b981"/>
            <text x="225" y="60" fill="#a7f3d0" font-size="10" text-anchor="middle">15 km (0.01 kg CO2)</text>
            <text x="225" y="155" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Peak Freshness, High Vitamin Retention & Local Farmer Support</text>
        `;
    } else {
        badge.textContent = "Imported Produce (8,000 km) - High Pollution";
        desc.innerHTML = "Flown and shipped across continents. Requires refrigerated cold chains, burns thousands of liters of fossil fuel, and fruit is picked green and artificially ripened.";
        svg.innerHTML = `
            <line x1="80" y1="85" x2="370" y2="85" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/>
            <circle cx="80" cy="85" r="16" fill="#991b1b"/>
            <text x="80" y="89" fill="#fecaca" font-size="8" text-anchor="middle">Origin</text>
            <circle cx="370" cy="85" r="16" fill="#991b1b"/>
            <text x="370" y="89" fill="#fecaca" font-size="8" text-anchor="middle">Plate</text>
            <!-- Cargo airplane icon -->
            <polygon points="225,65 240,75 225,85 220,78 210,80 215,75 210,70" fill="#f87171"/>
            <text x="225" y="55" fill="#fca5a5" font-size="10" text-anchor="middle">8,000 km (12.4 kg CO2)</text>
            <text x="225" y="155" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Heavy Carbon Footprint & Chemical Preservative Coating</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 16: Nutrition Science Pioneers
// -------------------------------------------------------------
function setSim16Hero(hero) {
    ['lind', 'goitre', 'gopalan'].forEach(k => {
        const btn = document.getElementById(`sim16-btn-${k}`);
        if (btn) {
            btn.className = (k === hero) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim16-svg');
    const badge = document.getElementById('sim16-badge');
    const desc = document.getElementById('sim16-desc');

    if (hero === 'lind') {
        badge.textContent = "Dr. James Lind (1746 - Scurvy Cure)";
        desc.innerHTML = "Aboard the warship <em>HMS Salisbury</em>, Dr. Lind conducted history's first controlled clinical trial, proving that fresh citrus fruits cured sailors dying of scurvy.";
        svg.innerHTML = `
            <rect x="130" y="35" width="190" height="90" rx="10" fill="#0369a1" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
            <text x="225" y="65" fill="#bae6fd" font-size="13" font-weight="bold" text-anchor="middle">Dr. James Lind (1746)</text>
            <text x="225" y="85" fill="#7dd3fc" font-size="10" text-anchor="middle">Controlled Clinical Trial</text>
            <text x="225" y="105" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Proved Citrus Fruits Cure Scurvy</text>
            <text x="225" y="155" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Birth of Controlled Evidence-Based Nutritional Medicine</text>
        `;
    } else if (hero === 'goitre') {
        badge.textContent = "Agariya Salt Community & Goitre Resolution";
        desc.innerHTML = "Iodine deficiency in Himalayan soils caused rampant goitre. Universal salt iodisation, powered by traditional salt harvesters in Kutch, eradicated endemic goitre nationwide.";
        svg.innerHTML = `
            <rect x="130" y="35" width="190" height="90" rx="10" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
            <text x="225" y="65" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">Agariya Salt Harvesters</text>
            <text x="225" y="85" fill="#fcd34d" font-size="10" text-anchor="middle">Little Rann of Kutch</text>
            <text x="225" y="105" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Nationwide Iodised Salt Supply</text>
            <text x="225" y="155" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Grassroots Salt Producers Defeated Himalayan Goitre</text>
        `;
    } else {
        badge.textContent = "Dr. C. Gopalan (1918-2019) - NIN Founder";
        desc.innerHTML = "The Father of Indian Nutrition Research! Analyzed 500+ indigenous foods, founded the National Nutrition Monitoring Bureau, and provided the scientific impetus for school Mid-Day Meals.";
        svg.innerHTML = `
            <rect x="130" y="35" width="190" height="90" rx="10" fill="#065f46" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
            <text x="225" y="65" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="middle">Dr. Coluthur Gopalan</text>
            <text x="225" y="85" fill="#6ee7b7" font-size="10" text-anchor="middle">National Institute of Nutrition</text>
            <text x="225" y="105" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Inspiration for School Mid-Day Meals</text>
            <text x="225" y="155" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Nourishing Over 100 Million Indian Children Daily</text>
        `;
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    setSim1Function('energy');
    setSim2Region('punjab');
    setSim3Era('chulha');
    setSim4Carb('starch');
    setSim5Fat('density');
    setSim6Protein('soyabean');
    setSim7Vitamin('A');
    setSim8Mineral('calcium');
    setSim9Mode('fiber');
    runSim10Test('potato');
    runSim11Test('peanut');
    runSim12Step('dal');
    setSim13Diet('balanced');
    setSim14Millet('ragi');
    setSim15Miles('local');
    setSim16Hero('lind');

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''

with open(".agents/class6_science_ch3_js.py", "w", encoding="utf-8") as f:
    f.write('"""\nJavaScript Code for Class 6 Science Chapter 3 Interactive Lab\n"""\n\n')
    f.write('JS_CODE = ' + repr(js_body) + '\n')

print("Generated .agents/class6_science_ch3_js.py successfully.")


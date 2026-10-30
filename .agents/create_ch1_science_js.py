import re

js_code = r'''
// Science Chapter 1 Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis
let isSpeaking = false;
function speakMentor(text) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    if (isSpeaking) {
        isSpeaking = false;
        return;
    }
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.95;
    utterance.pitch = 1.0;
    utterance.onend = () => { isSpeaking = false; };
    utterance.onerror = () => { isSpeaking = false; };
    isSpeaking = true;
    window.speechSynthesis.speak(utterance);
}

// Navigation
function updateSlideDisplay() {
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
        feedbackEl.innerHTML = `<strong>Try again:</strong> Think about the scientific observation or test involved!`;
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
        buttons.forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === correctOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl border text-sm font-medium transition bg-emerald-500/20 border-emerald-400 text-emerald-200';
            } else if (idx === selectedOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl border text-sm font-medium transition bg-rose-500/20 border-rose-400 text-rose-200';
            } else {
                btn.className = 'w-full text-left p-3 rounded-xl border text-sm font-medium transition bg-slate-800/40 border-slate-700/60 text-slate-400 opacity-60';
            }
        });
    }

    if (feedbackBox) {
        feedbackBox.style.display = 'block';
        if (selectedOpt === correctOpt) {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-sm bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
            feedbackBox.innerHTML = `<strong>Great job!</strong> ${explanation}`;
        } else {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-sm bg-rose-950/40 border border-rose-500/40 text-rose-300';
            feedbackBox.innerHTML = `<strong>Incorrect.</strong> Click "View Step-by-Step Solution" below for full breakdown.`;
        }
    }

    if (solutionBtn) {
        solutionBtn.style.display = 'inline-flex';
    }
}

// -------------------------------------------------------------
// Simulator 1: Spark of Curiosity
// -------------------------------------------------------------
function setSim1Target(key) {
    ['sea', 'leaf', 'sky'].forEach(k => {
        const btn = document.getElementById(`sim1-btn-${k}`);
        if (btn) {
            btn.className = (k === key) ?
                'px-3 py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim1-svg');
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');

    if (key === 'sea') {
        badge.textContent = "The Blue Sea (Raman Effect)";
        desc.innerHTML = "In 1921, Dr. C.V. Raman asked: <em>'Why is the Mediterranean Sea so intensely blue?'</em> By investigating how water molecules scatter light, he discovered the Raman Effect and won the Nobel Prize!";
        svg.innerHTML = `
            <rect x="30" y="80" width="390" height="80" fill="#0284c7" fill-opacity="0.5" rx="6"/>
            <!-- Sunlight ray -->
            <line x1="60" y1="20" x2="180" y2="100" stroke="#f59e0b" stroke-width="3"/>
            <text x="60" y="15" fill="#f59e0b" font-size="11" font-weight="bold">White Sunlight</text>
            <!-- Water molecule -->
            <circle cx="180" cy="100" r="14" fill="#38bdf8"/>
            <text x="180" y="104" fill="#0f172a" font-size="10" text-anchor="middle" font-weight="bold">H₂O</text>
            <!-- Scattered Blue Light -->
            <line x1="180" y1="100" x2="320" y2="40" stroke="#60a5fa" stroke-width="3" stroke-dasharray="4,2"/>
            <line x1="180" y1="100" x2="340" y2="90" stroke="#60a5fa" stroke-width="3" stroke-dasharray="4,2"/>
            <line x1="180" y1="100" x2="310" y2="140" stroke="#60a5fa" stroke-width="3" stroke-dasharray="4,2"/>
            <text x="350" y="85" fill="#93c5fd" font-size="11" font-weight="bold">Scattered Blue Photons</text>
        `;
    } else if (key === 'leaf') {
        badge.textContent = "Green Leaf (Photosynthesis)";
        desc.innerHTML = "Why are leaves green? Inside plant cells, microscopic green chloroplasts contain chlorophyll, absorbing red and blue light to convert water and carbon dioxide into sugar and life-giving oxygen!";
        svg.innerHTML = `
            <path d="M70,120 Q180,20 370,60 Q260,170 70,120 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
            <line x1="70" y1="120" x2="370" y2="60" stroke="#4ade80" stroke-width="2"/>
            <!-- Chloroplast bubbles -->
            <circle cx="200" cy="80" r="10" fill="#22c55e"/>
            <circle cx="250" cy="100" r="8" fill="#22c55e"/>
            <circle cx="160" cy="105" r="9" fill="#22c55e"/>
            <text x="220" y="55" fill="#86efac" font-size="11" font-weight="bold">Chloroplasts at Work</text>
            <text x="250" y="145" fill="#f8fafc" font-size="10">Light + CO₂ + H₂O → Food + Oxygen (O₂)</text>
        `;
    } else {
        badge.textContent = "Night Sky (Nuclear Furnaces)";
        desc.innerHTML = "Why do stars twinkle? Stars are colossal nuclear engines millions of kilometers away, fusing hydrogen into helium and radiating light across the cosmos through our shimmering atmosphere.";
        svg.innerHTML = `
            <rect x="30" y="20" width="390" height="140" fill="#090d16" rx="8"/>
            <!-- Stars -->
            <circle cx="100" cy="50" r="3" fill="#f8fafc"/>
            <circle cx="220" cy="40" r="4" fill="#fde047"/>
            <circle cx="340" cy="70" r="3" fill="#67e8f9"/>
            <circle cx="160" cy="110" r="2.5" fill="#f8fafc"/>
            <circle cx="280" cy="120" r="3.5" fill="#f472b6"/>
            <!-- Large Telescope -->
            <line x1="70" y1="140" x2="160" y2="80" stroke="#94a3b8" stroke-width="6"/>
            <line x1="70" y1="140" x2="50" y2="155" stroke="#64748b" stroke-width="3"/>
            <line x1="70" y1="140" x2="90" y2="155" stroke="#64748b" stroke-width="3"/>
            <text x="230" y="85" fill="#cbd5e1" font-size="11" font-weight="bold">Trillions of Cosmic Stars Twinkling</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 2: Science Everywhere
// -------------------------------------------------------------
function setSim2Domain(dom) {
    ['kitchen', 'forest', 'ocean', 'space'].forEach(d => {
        const btn = document.getElementById(`sim2-btn-${d}`);
        if (btn) {
            btn.className = (d === dom) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim2-svg');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (dom === 'kitchen') {
        badge.textContent = "Kitchen Science (Thermodynamics & Chemistry)";
        desc.innerHTML = "Pressure cookers raise water boiling points above 100 °C to cook lentils faster; yeast ferments idli batter releasing CO₂ gas bubbles that make it fluffy!";
        svg.innerHTML = `
            <!-- Pressure Cooker -->
            <rect x="160" y="70" width="120" height="90" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
            <line x1="220" y1="70" x2="220" y2="45" stroke="#cbd5e1" stroke-width="4"/>
            <rect x="210" y="38" width="20" height="10" fill="#f59e0b"/>
            <!-- Steam Whistle -->
            <path d="M220,38 Q210,15 200,20 M220,38 Q235,15 245,20" stroke="#e2e8f0" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
            <text x="260" y="30" fill="#f59e0b" font-size="10" font-weight="bold">Steam Whistle!</text>
            <!-- Stove Flame -->
            <path d="M170,165 Q180,180 190,165 Q200,180 210,165 Q220,180 230,165 Q240,180 250,165 Q260,180 270,165" stroke="#f97316" stroke-width="4" fill="none"/>
        `;
    } else if (dom === 'forest') {
        badge.textContent = "Forest Ecology (Nutrient Cycles)";
        desc.innerHTML = "Fallen leaves decompose into dark fertile humus with help from fungi and earthworms, feeding the root systems of towering teak trees.";
        svg.innerHTML = `
            <!-- Tree Trunk and Foliage -->
            <rect x="210" y="90" width="30" height="80" fill="#78350f"/>
            <circle cx="225" cy="70" r="50" fill="#15803d" opacity="0.8"/>
            <circle cx="190" cy="80" r="35" fill="#16a34a" opacity="0.7"/>
            <circle cx="260" cy="80" r="35" fill="#16a34a" opacity="0.7"/>
            <!-- Soil and Earthworm -->
            <line x1="60" y1="170" x2="390" y2="170" stroke="#854d0e" stroke-width="6"/>
            <path d="M120,175 Q135,165 150,175" stroke="#f472b6" stroke-width="3" fill="none"/>
            <text x="145" y="160" fill="#fca5a5" font-size="10">Earthworm aerating soil</text>
        `;
    } else if (dom === 'ocean') {
        badge.textContent = "Ocean Depths (Bioluminescence)";
        desc.innerHTML = "In the dark abyss 3,000 meters deep where sunlight never penetrates, deep-sea anglerfish create their own glowing light through chemical bioluminescence to lure prey!";
        svg.innerHTML = `
            <rect x="50" y="20" width="350" height="150" fill="#032b43" rx="8"/>
            <!-- Deep sea fish -->
            <path d="M260,100 Q200,60 170,100 Q200,140 260,100 Z" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
            <polygon points="260,100 290,80 290,120" fill="#0ea5e9"/>
            <!-- Glowing Angler lure -->
            <path d="M170,95 Q140,50 160,40" stroke="#94a3b8" stroke-width="2" fill="none"/>
            <circle cx="160" cy="40" r="7" fill="#38bdf8" filter="drop-shadow(0 0 6px #38bdf8)"/>
            <text x="210" y="45" fill="#7dd3fc" font-size="10" font-weight="bold">Bioluminescent Lure</text>
        `;
    } else {
        badge.textContent = "Cosmos (Galaxies & Telescopes)";
        desc.innerHTML = "Space telescopes orbit Earth above atmospheric distortion to capture ultraviolet, infrared, and visible light from galaxies born billions of years ago.";
        svg.innerHTML = `
            <rect x="50" y="20" width="350" height="150" fill="#020617" rx="8"/>
            <!-- Swirling galaxy -->
            <ellipse cx="225" cy="95" rx="80" ry="35" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="8,4" transform="rotate(-20 225 95)"/>
            <ellipse cx="225" cy="95" rx="40" ry="15" fill="none" stroke="#ec4899" stroke-width="2" transform="rotate(-20 225 95)"/>
            <circle cx="225" cy="95" r="8" fill="#fbbf24"/>
            <text x="225" y="150" fill="#cbd5e1" font-size="10" text-anchor="middle">Spiral Galaxy with Billions of Solar Systems</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 3: The Infinite Jigsaw
// -------------------------------------------------------------
let sim3Count = 3;

function addSim3Piece() {
    if (sim3Count < 6) {
        sim3Count++;
        renderSim3();
    }
}

function resetSim3Puzzle() {
    sim3Count = 3;
    renderSim3();
}

function renderSim3() {
    const board = document.getElementById('sim3-puzzle-board');
    const badge = document.getElementById('sim3-badge');
    const status = document.getElementById('sim3-status');
    const addBtn = document.getElementById('sim3-add-btn');

    badge.textContent = `Pieces: ${sim3Count} of 6`;

    const pieceLabels = [
        "1. Earth Spherical (Greeks/India)",
        "2. Heliocentric Orbit (Copernicus)",
        "3. Gravity (Newton)",
        "4. Evolution (Darwin)",
        "5. Relativity & Light (Einstein)",
        "6. Quantum & DNA (Modern Science)"
    ];

    let html = '';
    for (let i = 0; i < 6; i++) {
        if (i < sim3Count) {
            html += `
                <div class="rounded-lg p-2 bg-gradient-to-br from-indigo-900 to-cyan-900 border border-cyan-400 text-cyan-200 text-[10px] font-bold flex items-center justify-center text-center shadow">
                    ${pieceLabels[i]}
                </div>
            `;
        } else {
            html += `
                <div class="rounded-lg p-2 bg-slate-950/40 border border-dashed border-slate-700 text-slate-600 text-[10px] flex items-center justify-center text-center">
                    ? Unmapped Frontier
                </div>
            `;
        }
    }
    board.innerHTML = html;

    if (sim3Count === 6) {
        addBtn.disabled = true;
        addBtn.className = 'w-1/2 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-500 cursor-not-allowed';
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Discovery Frontier Expanded!</span> Notice how each piece connected with and refined the previous ones. The puzzle continues infinitely!`;
    } else {
        addBtn.disabled = false;
        addBtn.className = 'w-1/2 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-indigo-600 text-white transition';
        status.textContent = `Click "Discover New Evidence" to place the next piece into our understanding of the universe.`;
    }
}

// -------------------------------------------------------------
// Simulator 4: Earth's Living Quilt
// -------------------------------------------------------------
function setSim4Habitat(hab) {
    ['desert', 'mountain', 'mangrove', 'reef'].forEach(h => {
        const btn = document.getElementById(`sim4-btn-${h}`);
        if (btn) {
            btn.className = (h === hab) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim4-svg');
    const title = document.getElementById('sim4-habitat-title');
    const desc = document.getElementById('sim4-desc');

    if (hab === 'desert') {
        title.textContent = "Thar Desert (Hot & Arid)";
        desc.innerHTML = "<strong>Adaptations:</strong> Cacti store gallons of water in succulent stems; camels have broad padded feet to walk on burning dunes and long eyelashes to block sandstorms.";
        svg.innerHTML = `
            <rect x="40" y="110" width="370" height="70" fill="#d97706" fill-opacity="0.3"/>
            <!-- Sun -->
            <circle cx="370" cy="50" r="25" fill="#f59e0b"/>
            <!-- Cactus -->
            <rect x="180" y="70" width="18" height="70" rx="6" fill="#15803d"/>
            <path d="M165,95 L180,95 M165,95 L165,80" stroke="#15803d" stroke-width="8" stroke-linecap="round" fill="none"/>
            <path d="M198,105 L213,105 M213,105 L213,90" stroke="#15803d" stroke-width="8" stroke-linecap="round" fill="none"/>
            <text x="190" y="160" fill="#fef3c7" font-size="11" text-anchor="middle" font-weight="bold">Water-Storing Cactus</text>
        `;
    } else if (hab === 'mountain') {
        title.textContent = "Himalayan Peaks (Cold & Snowy)";
        desc.innerHTML = "<strong>Adaptations:</strong> Snow leopards have thick insulating spotted coats and broad paws acting like snowshoes; pine trees have conical shapes allowing heavy snow to slide off effortlessly.";
        svg.innerHTML = `
            <!-- Snowy Mountain peaks -->
            <polygon points="80,160 170,50 260,160" fill="#475569"/>
            <polygon points="140,85 170,50 200,85" fill="#f8fafc"/>
            <polygon points="200,160 290,65 380,160" fill="#334155"/>
            <polygon points="260,100 290,65 320,100" fill="#f8fafc"/>
            <!-- Pine tree -->
            <polygon points="110,160 125,120 140,160" fill="#166534"/>
            <polygon points="115,135 125,105 135,135" fill="#166534"/>
            <text x="230" y="175" fill="#cbd5e1" font-size="11" text-anchor="middle" font-weight="bold">Conical Snow-Shedding Pines</text>
        `;
    } else if (hab === 'mangrove') {
        title.textContent = "Sundarbans Mangroves (Tidal Saline Wetlands)";
        desc.innerHTML = "<strong>Adaptations:</strong> Pneumatophores (breathing roots) grow upwards out of oxygen-poor tidal mud into the air to breathe during low tides!";
        svg.innerHTML = `
            <!-- Mud and water -->
            <rect x="40" y="120" width="370" height="50" fill="#451a03" opacity="0.6"/>
            <line x1="40" y1="120" x2="410" y2="120" stroke="#0284c7" stroke-width="3"/>
            <!-- Mangrove Trunk -->
            <rect x="215" y="40" width="20" height="80" fill="#78350f"/>
            <circle cx="225" cy="40" r="35" fill="#15803d"/>
            <!-- Breathing roots sticking up -->
            <line x1="160" y1="140" x2="160" y2="105" stroke="#78350f" stroke-width="4"/>
            <line x1="180" y1="140" x2="180" y2="100" stroke="#78350f" stroke-width="4"/>
            <line x1="270" y1="140" x2="270" y2="105" stroke="#78350f" stroke-width="4"/>
            <line x1="290" y1="140" x2="290" y2="95" stroke="#78350f" stroke-width="4"/>
            <text x="225" y="160" fill="#fde68a" font-size="10" text-anchor="middle">Breathing Roots (Pneumatophores)</text>
        `;
    } else {
        title.textContent = "Andaman Coral Reefs (Marine Biodiversity)";
        desc.innerHTML = "<strong>Adaptations:</strong> Clownfish produce a special mucus skin coat that protects them from deadly sea anemone stings, living in safe mutual symbiosis.";
        svg.innerHTML = `
            <rect x="40" y="20" width="370" height="150" fill="#0369a1" fill-opacity="0.3" rx="8"/>
            <!-- Corals -->
            <path d="M100,160 Q110,120 120,160 M120,160 Q130,110 140,160 M140,160 Q150,130 160,160" stroke="#f43f5e" stroke-width="6" fill="none"/>
            <path d="M280,160 Q290,115 300,160 M300,160 Q315,100 330,160" stroke="#a855f7" stroke-width="8" fill="none"/>
            <!-- Clownfish -->
            <ellipse cx="220" cy="90" rx="20" ry="12" fill="#ea580c"/>
            <polygon points="240,90 255,80 255,100" fill="#ea580c"/>
            <rect x="215" y="78" width="4" height="24" fill="#ffffff"/>
            <text x="225" y="125" fill="#fed7aa" font-size="11" text-anchor="middle" font-weight="bold">Clownfish in Anemone Shelter</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 5: Miracles of Growth
// -------------------------------------------------------------
let sim5Mode = 'plant';

function setSim5Mode(mode) {
    sim5Mode = mode;
    document.getElementById('sim5-btn-plant').className = (mode === 'plant') ?
        'py-2 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim5-btn-butterfly').className = (mode === 'butterfly') ?
        'py-2 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    updateSim5();
}

function updateSim5() {
    const stage = parseInt(document.getElementById('sim5-slider').value, 10);
    document.getElementById('sim5-slider-val').textContent = `Step ${stage}`;
    document.getElementById('sim5-stage-badge').textContent = `Stage ${stage} of 4`;

    const svg = document.getElementById('sim5-svg');
    const desc = document.getElementById('sim5-desc');

    if (sim5Mode === 'plant') {
        const plantStages = [
            "<strong>Stage 1 (Dormant Seed):</strong> The seed rests in warm moist soil, absorbing water through its seed coat.",
            "<strong>Stage 2 (Radicle Emergence):</strong> The seed coat cracks; the first primary root (radicle) grows downward anchoring in soil.",
            "<strong>Stage 3 (Shoot & Cotyledons):</strong> The green shoot pushes upward toward sunlight, spreading its initial seed leaves.",
            "<strong>Stage 4 (Mature Flowering Plant):</strong> True leaves, strong stem, and radiant flowers appear ready to produce seeds for the next generation!"
        ];
        desc.innerHTML = plantStages[stage - 1];

        // Render Plant SVG Stages
        let plantSvg = '';
        if (stage === 1) {
            plantSvg = `
                <line x1="50" y1="120" x2="400" y2="120" stroke="#854d0e" stroke-width="4"/>
                <ellipse cx="225" cy="135" rx="10" ry="7" fill="#78350f"/>
                <text x="225" y="160" fill="#d97706" font-size="11" text-anchor="middle">Moist Seed in Soil</text>
            `;
        } else if (stage === 2) {
            plantSvg = `
                <line x1="50" y1="120" x2="400" y2="120" stroke="#854d0e" stroke-width="4"/>
                <ellipse cx="225" cy="135" rx="10" ry="7" fill="#78350f"/>
                <path d="M225,142 Q220,165 230,175" stroke="#fef08a" stroke-width="3" fill="none"/>
                <text x="225" y="110" fill="#a3e635" font-size="10" text-anchor="middle">Radicle (Root) Sprouting Downward</text>
            `;
        } else if (stage === 3) {
            plantSvg = `
                <line x1="50" y1="120" x2="400" y2="120" stroke="#854d0e" stroke-width="4"/>
                <path d="M225,120 Q225,95 225,80" stroke="#22c55e" stroke-width="4" fill="none"/>
                <ellipse cx="215" cy="75" rx="10" ry="5" fill="#22c55e" transform="rotate(-30 215 75)"/>
                <ellipse cx="235" cy="75" rx="10" ry="5" fill="#22c55e" transform="rotate(30 235 75)"/>
                <!-- Roots below -->
                <path d="M225,120 Q220,150 210,170 M225,120 Q230,150 240,170" stroke="#fef08a" stroke-width="2" fill="none"/>
                <text x="225" y="60" fill="#4ade80" font-size="11" text-anchor="middle" font-weight="bold">First Green Shoot</text>
            `;
        } else {
            plantSvg = `
                <line x1="50" y1="120" x2="400" y2="120" stroke="#854d0e" stroke-width="4"/>
                <line x1="225" y1="120" x2="225" y2="45" stroke="#15803d" stroke-width="5"/>
                <ellipse cx="205" cy="80" rx="16" ry="8" fill="#16a34a" transform="rotate(-25 205 80)"/>
                <ellipse cx="245" cy="65" rx="16" ry="8" fill="#16a34a" transform="rotate(25 245 65)"/>
                <!-- Flower -->
                <circle cx="225" cy="40" r="14" fill="#fbbf24"/>
                <circle cx="215" cy="30" r="9" fill="#f43f5e"/>
                <circle cx="235" cy="30" r="9" fill="#f43f5e"/>
                <circle cx="215" cy="50" r="9" fill="#f43f5e"/>
                <circle cx="235" cy="50" r="9" fill="#f43f5e"/>
                <text x="225" y="20" fill="#fde047" font-size="11" text-anchor="middle" font-weight="bold">Flowering Plant with Seeds!</text>
            `;
        }
        svg.innerHTML = plantSvg;
    } else {
        const bflyStages = [
            "<strong>Stage 1 (Egg):</strong> A tiny oval pearl-like egg laid carefully on the underside of a fresh green leaf.",
            "<strong>Stage 2 (Caterpillar):</strong> The ravenous larva eats its eggshell and munches leaves continuously to store energy.",
            "<strong>Stage 3 (Chrysalis / Pupa):</strong> Inside a hardened silky cocoon, cellular metamorphosis re-engineers the body plan.",
            "<strong>Stage 4 (Adult Butterfly):</strong> A splendid butterfly emerges, expands colorful wings with hemolymph, and takes flight!"
        ];
        desc.innerHTML = bflyStages[stage - 1];

        let bflySvg = '';
        if (stage === 1) {
            bflySvg = `
                <path d="M120,130 Q225,50 330,130" stroke="#16a34a" stroke-width="12" fill="none"/>
                <ellipse cx="225" cy="85" rx="8" ry="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <text x="225" y="65" fill="#fef08a" font-size="11" text-anchor="middle" font-weight="bold">Butterfly Egg on Leaf</text>
            `;
        } else if (stage === 2) {
            bflySvg = `
                <line x1="80" y1="120" x2="370" y2="120" stroke="#15803d" stroke-width="8"/>
                <!-- Caterpillar body segments -->
                <circle cx="180" cy="110" r="10" fill="#84cc16"/>
                <circle cx="195" cy="110" r="10" fill="#65a30d"/>
                <circle cx="210" cy="110" r="10" fill="#84cc16"/>
                <circle cx="225" cy="110" r="10" fill="#65a30d"/>
                <circle cx="240" cy="110" r="10" fill="#84cc16"/>
                <circle cx="255" cy="110" r="10" fill="#65a30d"/>
                <circle cx="270" cy="106" r="11" fill="#4d7c0f"/>
                <text x="225" y="80" fill="#bef264" font-size="11" text-anchor="middle" font-weight="bold">Leaf-Eating Caterpillar (Larva)</text>
            `;
        } else if (stage === 3) {
            bflySvg = `
                <!-- Twig -->
                <line x1="120" y1="40" x2="330" y2="40" stroke="#78350f" stroke-width="6"/>
                <!-- Chrysalis hanging -->
                <line x1="225" y1="40" x2="225" y2="60" stroke="#a1a1aa" stroke-width="2"/>
                <path d="M225,60 C205,80 210,130 225,145 C240,130 245,80 225,60 Z" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                <text x="225" y="165" fill="#86efac" font-size="11" text-anchor="middle" font-weight="bold">Metamorphosis Inside Chrysalis (Pupa)</text>
            `;
        } else {
            bflySvg = `
                <!-- Butterfly wings -->
                <g transform="translate(225, 95)">
                    <path d="M0,-10 Q-50,-70 -80,-30 Q-90,20 0,0 Z" fill="#ea580c" stroke="#fed7aa" stroke-width="2"/>
                    <path d="M0,-10 Q50,-70 80,-30 Q90,20 0,0 Z" fill="#ea580c" stroke="#fed7aa" stroke-width="2"/>
                    <path d="M0,0 Q-60,30 -40,65 Q-10,50 0,0 Z" fill="#f97316"/>
                    <path d="M0,0 Q60,30 40,65 Q10,50 0,0 Z" fill="#f97316"/>
                    <!-- Body -->
                    <ellipse cx="0" cy="0" rx="4" ry="25" fill="#1e293b"/>
                    <line x1="-2" y1="-25" x2="-12" y2="-40" stroke="#f8fafc" stroke-width="1.5"/>
                    <line x1="2" y1="-25" x2="12" y2="-40" stroke="#f8fafc" stroke-width="1.5"/>
                </g>
                <text x="225" y="25" fill="#fdba74" font-size="12" text-anchor="middle" font-weight="bold">Winged Adult Butterfly Emerges!</text>
            `;
        }
        svg.innerHTML = bflySvg;
    }
}

// -------------------------------------------------------------
// Simulator 6: Cuisines & Nutrients
// -------------------------------------------------------------
let sim6Selected = { carbs: false, protein: false, vitamins: false };

function toggleSim6Food(cat) {
    sim6Selected[cat] = !sim6Selected[cat];
    const btn = document.getElementById(`sim6-btn-${cat}`);
    if (btn) {
        btn.className = sim6Selected[cat] ?
            'py-2 rounded-xl text-xs font-semibold bg-emerald-500 text-slate-950 transition' :
            'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    }
    renderSim6();
}

function renderSim6() {
    const plate = document.getElementById('sim6-plate');
    const badge = document.getElementById('sim6-health-badge');
    const status = document.getElementById('sim6-status');

    let itemsHtml = '';
    let count = 0;

    if (sim6Selected.carbs) {
        count++;
        itemsHtml += `<div class="absolute top-6 left-12 w-14 h-14 rounded-full bg-amber-500 text-slate-950 font-bold flex flex-col items-center justify-center text-[10px] shadow border border-amber-300"><span>🌾</span><span>Carbs</span></div>`;
    }
    if (sim6Selected.protein) {
        count++;
        itemsHtml += `<div class="absolute top-6 right-12 w-14 h-14 rounded-full bg-orange-500 text-white font-bold flex flex-col items-center justify-center text-[10px] shadow border border-orange-300"><span>🥣</span><span>Protein</span></div>`;
    }
    if (sim6Selected.vitamins) {
        count++;
        itemsHtml += `<div class="absolute bottom-6 w-16 h-16 rounded-full bg-emerald-500 text-slate-950 font-bold flex flex-col items-center justify-center text-[10px] shadow border border-emerald-300"><span>🥬</span><span>Vitamins</span></div>`;
    }

    if (count === 0) {
        itemsHtml = `<span class="text-slate-500 text-xs italic text-center">Empty Thali Plate.<br>Select items below to balance!</span>`;
    }

    plate.innerHTML = itemsHtml;

    if (count === 3) {
        badge.textContent = "100% Balanced Thali!";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Perfect Nutritional Balance!</span> Energy from Carbs + Muscle Repair from Proteins + Immunity from Vitamins & Minerals.`;
    } else {
        badge.textContent = `${count} of 3 Nutrients Added`;
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        status.textContent = `A healthy body needs all 3 pillars: Energy givers (Carbs), Body builders (Protein), and Protectors (Vitamins).`;
    }
}

// -------------------------------------------------------------
// Simulator 7: The Journey of Water
// -------------------------------------------------------------
function triggerSim7Phase(phase) {
    ['evap', 'cond', 'rain'].forEach(p => {
        const btn = document.getElementById(`sim7-btn-${p}`);
        if (btn) {
            btn.className = (p === phase) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim7-svg');
    const badge = document.getElementById('sim7-badge');
    const desc = document.getElementById('sim7-desc');

    if (phase === 'evap') {
        badge.textContent = "Phase 1: Solar Evaporation";
        desc.innerHTML = "Sunlight heats the ocean. Kinetic energy frees water molecules from liquid bounds, ascending into the atmosphere as invisible water vapor.";
        svg.innerHTML = `
            <!-- Ocean -->
            <rect x="30" y="130" width="390" height="45" fill="#0284c7" fill-opacity="0.5" rx="4"/>
            <!-- Sun -->
            <circle cx="80" cy="45" r="22" fill="#f59e0b"/>
            <!-- Rising vapor arrows -->
            <path d="M160,120 Q150,90 160,70" stroke="#38bdf8" stroke-width="2.5" fill="none" stroke-dasharray="4,2"/>
            <path d="M220,120 Q210,90 220,70" stroke="#38bdf8" stroke-width="2.5" fill="none" stroke-dasharray="4,2"/>
            <path d="M280,120 Q270,90 280,70" stroke="#38bdf8" stroke-width="2.5" fill="none" stroke-dasharray="4,2"/>
            <text x="220" y="55" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Rising Water Vapor</text>
            <text x="220" y="155" fill="#e0f2fe" font-size="11" text-anchor="middle">Warmed Ocean Water</text>
        `;
    } else if (phase === 'cond') {
        badge.textContent = "Phase 2: Cloud Condensation";
        desc.innerHTML = "As water vapor reaches cooler altitudes, it condenses around microscopic dust particles into trillions of suspended water droplets: <strong>Clouds</strong>!";
        svg.innerHTML = `
            <rect x="30" y="130" width="390" height="45" fill="#0284c7" fill-opacity="0.5" rx="4"/>
            <!-- Cloud cluster -->
            <g transform="translate(200, 50)">
                <circle cx="0" cy="0" r="28" fill="#e2e8f0"/>
                <circle cx="-25" cy="8" r="22" fill="#e2e8f0"/>
                <circle cx="25" cy="8" r="22" fill="#e2e8f0"/>
                <circle cx="-12" cy="16" r="20" fill="#e2e8f0"/>
                <circle cx="15" cy="16" r="20" fill="#e2e8f0"/>
            </g>
            <text x="200" y="110" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">Cold Upper Atmosphere Condensation</text>
        `;
    } else {
        badge.textContent = "Phase 3: Rain Precipitation";
        desc.innerHTML = "Droplets merge, become too heavy for rising updrafts to support, and plunge downward as life-giving precipitation (monsoon rain).";
        svg.innerHTML = `
            <rect x="30" y="130" width="390" height="45" fill="#0284c7" fill-opacity="0.5" rx="4"/>
            <!-- Dark rain cloud -->
            <g transform="translate(200, 45)">
                <circle cx="0" cy="0" r="28" fill="#64748b"/>
                <circle cx="-25" cy="8" r="22" fill="#64748b"/>
                <circle cx="25" cy="8" r="22" fill="#64748b"/>
            </g>
            <!-- Falling raindrops -->
            <line x1="160" y1="85" x2="150" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4"/>
            <line x1="190" y1="85" x2="180" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4"/>
            <line x1="220" y1="85" x2="210" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4"/>
            <line x1="250" y1="85" x2="240" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4"/>
            <text x="200" y="155" fill="#e0f2fe" font-size="11" text-anchor="middle" font-weight="bold">Precipitation Returns Water to Earth!</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 8: Three States of Matter
// -------------------------------------------------------------
function updateSim8() {
    const temp = parseInt(document.getElementById('sim8-temp').value, 10);
    document.getElementById('sim8-temp-val').textContent = `${temp} °C`;
    const badge = document.getElementById('sim8-state-badge');
    const desc = document.getElementById('sim8-desc');
    const svg = document.getElementById('sim8-svg');

    if (temp <= 0) {
        badge.textContent = `Solid Ice (${temp} °C)`;
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30";
        desc.innerHTML = "<strong>Solid Phase:</strong> Below 0 °C, low thermal kinetic energy locks H₂O molecules into a rigid hexagonal crystalline grid.";
        svg.innerHTML = `
            <rect x="145" y="30" width="160" height="110" rx="8" fill="#1e3a8a" fill-opacity="0.4" stroke="#60a5fa" stroke-width="2"/>
            <!-- Rigid grid dots -->
            <g fill="#93c5fd">
                <circle cx="175" cy="55" r="7"/><circle cx="210" cy="55" r="7"/><circle cx="245" cy="55" r="7"/><circle cx="280" cy="55" r="7"/>
                <circle cx="175" cy="85" r="7"/><circle cx="210" cy="85" r="7"/><circle cx="245" cy="85" r="7"/><circle cx="280" cy="85" r="7"/>
                <circle cx="175" cy="115" r="7"/><circle cx="210" cy="115" r="7"/><circle cx="245" cy="115" r="7"/><circle cx="280" cy="115" r="7"/>
            </g>
            <text x="225" y="160" fill="#bfdbfe" font-size="11" text-anchor="middle" font-weight="bold">Rigid Ice Lattice (Fixed Volume & Shape)</text>
        `;
    } else if (temp < 100) {
        badge.textContent = `Liquid Water (${temp} °C)`;
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
        desc.innerHTML = "<strong>Liquid Phase:</strong> Between 0 °C and 100 °C, molecules slide past each other freely, flowing into whatever container holds them.";
        svg.innerHTML = `
            <path d="M140,40 L140,130 Q225,145 310,130 L310,40" stroke="#94a3b8" stroke-width="2" fill="none"/>
            <rect x="142" y="70" width="166" height="60" fill="#0284c7" fill-opacity="0.3"/>
            <!-- Free flowing molecules -->
            <g fill="#38bdf8">
                <circle cx="170" cy="85" r="6"/><circle cx="205" cy="95" r="6"/><circle cx="240" cy="80" r="6"/><circle cx="275" cy="90" r="6"/>
                <circle cx="185" cy="115" r="6"/><circle cx="225" cy="110" r="6"/><circle cx="265" cy="118" r="6"/>
            </g>
            <text x="225" y="160" fill="#7dd3fc" font-size="11" text-anchor="middle" font-weight="bold">Fluid State (Fixed Volume, Takes Container Shape)</text>
        `;
    } else {
        badge.textContent = `Gaseous Steam (${temp} °C)`;
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        desc.innerHTML = "<strong>Gas Phase:</strong> At 100 °C and above, rapid kinetic motion completely overcomes intermolecular forces. Steam expands vigorously to fill any space!";
        svg.innerHTML = `
            <rect x="120" y="25" width="210" height="120" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>
            <!-- Fast bouncing gas molecules with velocity ticks -->
            <g fill="#fde047" stroke="#f59e0b" stroke-width="1.5">
                <circle cx="150" cy="50" r="5"/><line x1="150" y1="50" x2="165" y2="40"/>
                <circle cx="230" cy="40" r="5"/><line x1="230" y1="40" x2="245" y2="55"/>
                <circle cx="290" cy="65" r="5"/><line x1="290" y1="65" x2="275" y2="55"/>
                <circle cx="170" cy="100" r="5"/><line x1="170" y1="100" x2="160" y2="115"/>
                <circle cx="260" cy="110" r="5"/><line x1="260" y1="110" x2="280" y2="100"/>
            </g>
            <text x="225" y="165" fill="#fde047" font-size="11" text-anchor="middle" font-weight="bold">High-Energy Vapor (No Fixed Shape or Volume)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 9: Hot or Cold?
// -------------------------------------------------------------
function setSim9Step(step) {
    document.getElementById('sim9-btn-step1').className = (step === 1) ?
        'py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition' :
        'py-2.5 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim9-btn-step2').className = (step === 2) ?
        'py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition' :
        'py-2.5 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim9-svg');
    const badge = document.getElementById('sim9-badge');
    const exp = document.getElementById('sim9-explanation');

    if (step === 1) {
        badge.textContent = "Step 1: Extreme Conditioning";
        exp.innerHTML = "Left hand is immersed in ice-cold water (5 °C); right hand is immersed in hot water (45 °C) for one minute. Thermal receptors adapt to these contrasting baselines.";
        svg.innerHTML = `
            <!-- Left Bowl (Ice Cold) -->
            <rect x="70" y="60" width="120" height="80" rx="10" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
            <text x="130" y="95" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Ice-Cold (5 °C)</text>
            <text x="130" y="115" fill="#94a3b8" font-size="10" text-anchor="middle">Left Hand Here</text>
            
            <!-- Right Bowl (Hot) -->
            <rect x="260" y="60" width="120" height="80" rx="10" fill="#e11d48" fill-opacity="0.3" stroke="#f43f5e" stroke-width="2"/>
            <text x="320" y="95" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">Warm / Hot (45 °C)</text>
            <text x="320" y="115" fill="#94a3b8" font-size="10" text-anchor="middle">Right Hand Here</text>
        `;
    } else {
        badge.textContent = "Step 2: Sensory Contradiction";
        exp.innerHTML = "<strong>The Great Illusion!</strong> Both hands are placed into the SAME bowl of lukewarm water (25 °C). The cold left hand feels warm, while the warm right hand feels cold! Touch is subjective; only calibrated thermometers tell absolute truth!";
        svg.innerHTML = `
            <!-- Center Lukewarm Bowl -->
            <rect x="145" y="40" width="160" height="100" rx="12" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="2"/>
            <text x="225" y="80" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Lukewarm Water (25 °C)</text>
            <text x="175" y="110" fill="#38bdf8" font-size="10" font-weight="bold">Left feels: WARM!</text>
            <text x="275" y="110" fill="#f43f5e" font-size="10" font-weight="bold">Right feels: COLD!</text>
            <text x="225" y="160" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Contradictory Sensation in the Exact Same Water!</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 10: Sorting Materials
// -------------------------------------------------------------
const sim10Data = {
    iron: { title: "Iron Nail (Ferrous Metal)", magnetic: true, conductor: true, desc: "Strongly attracted to magnets; conducts electric circuit lighting the bulb." },
    copper: { title: "Copper Coin (Non-ferrous Metal)", magnetic: false, conductor: true, desc: "Not attracted to magnets, but an excellent electrical conductor lighting the bulb brightly." },
    plastic: { title: "Plastic Ruler (Polymer)", magnetic: false, conductor: false, desc: "Completely non-magnetic and an electrical insulator (bulb stays dark)." },
    wood: { title: "Wooden Stick (Organic)", magnetic: false, conductor: false, desc: "Non-magnetic and an electrical insulator (bulb stays dark)." }
};

function testSim10Material(mat) {
    ['iron', 'copper', 'plastic', 'wood'].forEach(m => {
        const btn = document.getElementById(`sim10-btn-${m}`);
        if (btn) {
            btn.className = (m === mat) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const data = sim10Data[mat];
    document.getElementById('sim10-mat-title').textContent = data.title;
    document.getElementById('sim10-status').innerHTML = data.desc;

    const svg = document.getElementById('sim10-svg');
    svg.innerHTML = `
        <!-- Magnet Test on Left -->
        <g transform="translate(100, 90)">
            <rect x="-40" y="-15" width="40" height="30" fill="#dc2626" rx="3"/>
            <text x="-20" y="4" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">N</text>
            <rect x="0" y="-15" width="40" height="30" fill="#2563eb" rx="3"/>
            <text x="20" y="4" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">S</text>
            <text x="0" y="35" fill="${data.magnetic ? '#34d399' : '#f87171'}" font-size="11" font-weight="bold" text-anchor="middle">
                ${data.magnetic ? 'Attracted to Magnet (Yes)' : 'Non-Magnetic (No)'}
            </text>
        </g>
        
        <!-- Electric Circuit on Right -->
        <g transform="translate(320, 90)">
            <circle cx="0" cy="-25" r="16" fill="${data.conductor ? '#fef08a' : '#334155'}" stroke="${data.conductor ? '#f59e0b' : '#64748b'}" stroke-width="2"/>
            <text x="0" y="-20" font-size="14" text-anchor="middle">${data.conductor ? '💡' : '⚫'}</text>
            <text x="0" y="35" fill="${data.conductor ? '#34d399' : '#f87171'}" font-size="11" font-weight="bold" text-anchor="middle">
                ${data.conductor ? 'Electrical Conductor (Bulb ON)' : 'Insulator (Bulb OFF)'}
            </text>
        </g>
    `;
}

// -------------------------------------------------------------
// Simulator 11: Celestial Wonders
// -------------------------------------------------------------
let sim11OrbitAngle = 0;
let sim11Interval = null;

function renderSim11() {
    const svg = document.getElementById('sim11-svg');
    const rad = (sim11OrbitAngle * Math.PI) / 180;
    const earthX = 225 + 130 * Math.cos(rad);
    const earthY = 95 + 50 * Math.sin(rad);

    // Moon orbiting Earth
    const moonRad = rad * 4;
    const moonX = earthX + 26 * Math.cos(moonRad);
    const moonY = earthY + 14 * Math.sin(moonRad);

    svg.innerHTML = `
        <!-- Cosmic Stars background -->
        <rect x="30" y="20" width="390" height="150" fill="#030712" rx="8"/>
        <circle cx="60" cy="40" r="1.5" fill="#f8fafc"/>
        <circle cx="180" cy="30" r="1.5" fill="#f8fafc"/>
        <circle cx="360" cy="45" r="1.5" fill="#f8fafc"/>
        <circle cx="390" cy="130" r="1.5" fill="#f8fafc"/>
        <circle cx="80" cy="150" r="1.5" fill="#f8fafc"/>
        
        <!-- Earth Orbit Ellipse -->
        <ellipse cx="225" cy="95" rx="130" ry="50" fill="none" stroke="#334155" stroke-dasharray="4,4"/>
        
        <!-- Central Sun -->
        <circle cx="225" cy="95" r="24" fill="#f59e0b" filter="drop-shadow(0 0 10px #f59e0b)"/>
        <text x="225" y="99" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Sun ☀️</text>
        
        <!-- Earth -->
        <circle cx="${earthX}" cy="${earthY}" r="9" fill="#0284c7"/>
        <text x="${earthX}" y="${earthY - 14}" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Earth</text>
        
        <!-- Moon -->
        <circle cx="${moonX}" cy="${moonY}" r="3.5" fill="#f8fafc"/>
    `;
}

function toggleSim11Orbit() {
    const btn = document.getElementById('sim11-orbit-btn');
    if (sim11Interval) {
        clearInterval(sim11Interval);
        sim11Interval = null;
        if (btn) btn.textContent = "Resume Cosmic Orbit";
    } else {
        sim11Interval = setInterval(() => {
            sim11OrbitAngle = (sim11OrbitAngle + 2) % 360;
            renderSim11();
        }, 40);
        if (btn) btn.textContent = "Pause Cosmic Orbit";
    }
}

// -------------------------------------------------------------
// Simulator 12: The Scientific Method
// -------------------------------------------------------------
function setSim12Action(act) {
    ['ink', 'scribble', 'restore'].forEach(a => {
        const btn = document.getElementById(`sim12-btn-${a}`);
        if (btn) {
            btn.className = (a === act || (a === 'ink' && act === 'check_ink')) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim12-svg');
    const badge = document.getElementById('sim12-step-badge');
    const desc = document.getElementById('sim12-desc');

    if (act === 'check_ink') {
        badge.textContent = "Test 1: Unscrew Pen Barrel";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        desc.innerHTML = "<strong>Hypothesis 1 ('Out of ink') Refuted!</strong> The transparent tube shows plenty of blue ink inside. The problem must be dried ink clogging the tiny ball at the point.";
        svg.innerHTML = `
            <!-- Refill tube with blue ink column -->
            <rect x="80" y="75" width="280" height="15" rx="3" fill="#334155" stroke="#94a3b8"/>
            <rect x="80" y="75" width="180" height="15" rx="3" fill="#2563eb"/>
            <polygon points="70,82.5 80,75 80,90" fill="#94a3b8"/>
            <circle cx="68" cy="82.5" r="3" fill="#cbd5e1"/>
            <text x="220" y="115" fill="#60a5fa" font-size="11" text-anchor="middle" font-weight="bold">Refill is 60% Full of Blue Ink!</text>
        `;
    } else if (act === 'scribble') {
        badge.textContent = "Test 2: Loosening Clog";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
        desc.innerHTML = "<strong>Hypothesis 2 Tested:</strong> Scribbling firmly on rough paper or gently warming the metal tip loosens the dry ink clot around the rolling ball bearing.";
        svg.innerHTML = `
            <!-- Rough paper with friction strokes -->
            <rect x="120" y="30" width="210" height="120" fill="#f8fafc" rx="6"/>
            <!-- Scribble lines -->
            <path d="M150,60 Q170,90 190,60 Q210,100 230,70 Q250,90 270,75" stroke="#94a3b8" stroke-width="2" fill="none"/>
            <text x="225" y="130" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Friction Rolling the Ballpoint</text>
        `;
    } else {
        badge.textContent = "Verdict: Fresh Ink Flows!";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        desc.innerHTML = "<strong>Problem Solved Scientifically!</strong> Smooth blue ink writes effortlessly across the page. Evidence-based troubleshooting beats random guessing!";
        svg.innerHTML = `
            <rect x="120" y="30" width="210" height="120" fill="#f8fafc" rx="6"/>
            <path d="M140,75 C170,60 190,100 230,70 S280,90 300,75" stroke="#2563eb" stroke-width="3" fill="none"/>
            <text x="225" y="125" fill="#1e40af" font-size="13" font-weight="bold" text-anchor="middle">Science in Action! ✨</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 13: Observe & Question
// -------------------------------------------------------------
function setSim13Case(c) {
    ['rainbow', 'rust', 'firefly'].forEach(k => {
        const btn = document.getElementById(`sim13-btn-${k}`);
        if (btn) {
            btn.className = (k === c) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim13-svg');
    const badge = document.getElementById('sim13-badge');
    const qBox = document.getElementById('sim13-question-box');

    if (c === 'rainbow') {
        badge.textContent = "Observation: Rainbow in Sky";
        qBox.innerHTML = "<strong>Question:</strong> <em>'Why does sunlight split into 7 distinct colors only when rain falls in front of the sun?'</em><br>→ Leads to refraction & dispersion theory of optics!";
        svg.innerHTML = `
            <!-- Rainbow Arcs -->
            <path d="M70,140 Q225,20 380,140" stroke="#ef4444" stroke-width="5" fill="none"/>
            <path d="M75,140 Q225,30 375,140" stroke="#f97316" stroke-width="5" fill="none"/>
            <path d="M80,140 Q225,40 370,140" stroke="#eab308" stroke-width="5" fill="none"/>
            <path d="M85,140 Q225,50 365,140" stroke="#22c55e" stroke-width="5" fill="none"/>
            <path d="M90,140 Q225,60 360,140" stroke="#06b6d4" stroke-width="5" fill="none"/>
            <path d="M95,140 Q225,70 355,140" stroke="#3b82f6" stroke-width="5" fill="none"/>
            <path d="M100,140 Q225,80 350,140" stroke="#a855f7" stroke-width="5" fill="none"/>
        `;
    } else if (c === 'rust') {
        badge.textContent = "Observation: Rust on Iron Gate";
        qBox.innerHTML = "<strong>Question:</strong> <em>'Why does shiny grey iron turn to flaky brown powder outdoors, but stays shiny inside dry paint?'</em><br>→ Leads to chemical oxidation theory (Iron + Oxygen + Water)!";
        svg.innerHTML = `
            <!-- Half clean iron, half rusted -->
            <rect x="100" y="40" width="120" height="100" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
            <text x="160" y="95" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Dry Shiny Iron</text>
            
            <rect x="230" y="40" width="120" height="100" fill="#9a3412" stroke="#ea580c" stroke-width="2"/>
            <text x="290" y="95" fill="#ffedd5" font-size="11" font-weight="bold" text-anchor="middle">Rusted Powder</text>
        `;
    } else {
        badge.textContent = "Observation: Firefly Light";
        qBox.innerHTML = "<strong>Question:</strong> <em>'How can an insect glow brightly in the dark without producing burning heat like a campfire?'</em><br>→ Leads to cold biochemical luminescence discoveries!";
        svg.innerHTML = `
            <rect x="50" y="20" width="350" height="140" fill="#020617" rx="8"/>
            <!-- Firefly body -->
            <ellipse cx="225" cy="85" rx="20" ry="12" fill="#334155"/>
            <!-- Glowing abdomen -->
            <circle cx="205" cy="85" r="14" fill="#a3e635" filter="drop-shadow(0 0 8px #a3e635)"/>
            <text x="225" y="130" fill="#d9f99d" font-size="11" font-weight="bold" text-anchor="middle">Cold Chemical Luminescence</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 14: Hypothesize & Test
// -------------------------------------------------------------
let sim14Advanced = false;

function runSim14Days() {
    sim14Advanced = !sim14Advanced;
    const btn = document.getElementById('sim14-run-btn');
    const svg = document.getElementById('sim14-svg');
    const res = document.getElementById('sim14-result');

    if (sim14Advanced) {
        btn.textContent = "Reset to Day 1";
        res.innerHTML = "<strong>After 7 Days:</strong> Pot A (Sunlight) grew to 20 cm with rich green leaves. Pot B (Dark) only grew 5 cm and turned pale yellow. <em>Fair test proves: Sunlight is essential for vigorous plant growth!</em>";
        svg.innerHTML = `
            <!-- Pot A (Sunlight) -> Tall green -->
            <rect x="90" y="120" width="60" height="40" fill="#b45309" rx="3"/>
            <line x1="120" y1="120" x2="120" y2="40" stroke="#16a34a" stroke-width="4"/>
            <circle cx="105" cy="65" r="12" fill="#22c55e"/>
            <circle cx="135" cy="55" r="12" fill="#22c55e"/>
            <circle cx="120" cy="35" r="10" fill="#22c55e"/>
            <text x="120" y="175" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Pot A: 20 cm Tall</text>
            
            <!-- Pot B (Dark) -> Stunted yellow -->
            <rect x="290" y="120" width="60" height="40" fill="#b45309" rx="3"/>
            <line x1="320" y1="120" x2="320" y2="95" stroke="#ca8a04" stroke-width="3"/>
            <circle cx="310" cy="100" r="6" fill="#fef08a"/>
            <circle cx="330" cy="98" r="6" fill="#fef08a"/>
            <text x="320" y="175" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Pot B: 5 cm Stunted</text>
        `;
    } else {
        btn.textContent = "Advance Time (7 Days)";
        res.textContent = "Both seeds start at equal height (2 cm). Click Advance to observe the single variable effect of sunlight over 7 days.";
        svg.innerHTML = `
            <!-- Pot A (Day 1) -->
            <rect x="90" y="120" width="60" height="40" fill="#b45309" rx="3"/>
            <line x1="120" y1="120" x2="120" y2="105" stroke="#16a34a" stroke-width="3"/>
            <text x="120" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">Pot A: Day 1 (2 cm)</text>
            
            <!-- Pot B (Day 1) -->
            <rect x="290" y="120" width="60" height="40" fill="#b45309" rx="3"/>
            <line x1="320" y1="120" x2="320" y2="105" stroke="#16a34a" stroke-width="3"/>
            <text x="320" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">Pot B: Day 1 (2 cm)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 15: Analyze & Conclude
// -------------------------------------------------------------
function setSim15Scenario(scen) {
    document.getElementById('sim15-btn-sup').className = (scen === 'support') ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim15-btn-ref').className = (scen === 'refute') ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim15-svg');
    const badge = document.getElementById('sim15-verdict-badge');
    const desc = document.getElementById('sim15-desc');

    if (scen === 'support') {
        badge.textContent = "Hypothesis Supported (Verified)";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        desc.innerHTML = "The measured experimental results match the predicted trend! The hypothesis is supported and can now be published for peer review and replication.";
        svg.innerHTML = `
            <line x1="60" y1="140" x2="380" y2="140" stroke="#64748b" stroke-width="2"/>
            <line x1="60" y1="140" x2="60" y2="20" stroke="#64748b" stroke-width="2"/>
            <!-- Bar 1 (Expected) -->
            <rect x="120" y="45" width="60" height="95" fill="#0284c7" rx="3"/>
            <text x="150" y="40" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Predicted (20cm)</text>
            <!-- Bar 2 (Actual Measured) -->
            <rect x="240" y="48" width="60" height="92" fill="#10b981" rx="3"/>
            <text x="270" y="40" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Measured (19.6cm)</text>
            <text x="220" y="165" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Match Confirmed! Hypothesis Supported</text>
        `;
    } else {
        badge.textContent = "Hypothesis Refuted (Self-Correction)";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
        desc.innerHTML = "The data directly contradicts the hypothesis! This is not a failure — it proves what does NOT happen, pointing researchers toward a new, improved hypothesis.";
        svg.innerHTML = `
            <line x1="60" y1="140" x2="380" y2="140" stroke="#64748b" stroke-width="2"/>
            <line x1="60" y1="140" x2="60" y2="20" stroke="#64748b" stroke-width="2"/>
            <!-- Bar 1 (Expected) -->
            <rect x="120" y="45" width="60" height="95" fill="#0284c7" rx="3"/>
            <text x="150" y="40" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Predicted (20cm)</text>
            <!-- Bar 2 (Actual Measured -> Tiny) -->
            <rect x="240" y="115" width="60" height="25" fill="#f43f5e" rx="3"/>
            <text x="270" y="105" fill="#fb7185" font-size="10" font-weight="bold" text-anchor="middle">Measured (4cm)</text>
            <text x="220" y="165" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Hypothesis Refuted! Formulate New Guess</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 16: Everyday Scientists
// -------------------------------------------------------------
function setSim16Role(role) {
    ['mech', 'cook', 'elec'].forEach(r => {
        const btn = document.getElementById(`sim16-btn-${r}`);
        if (btn) {
            btn.className = (r === role || (r === 'mech' && role === 'mechanic') || (r === 'elec' && role === 'electrician')) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim16-svg');
    const title = document.getElementById('sim16-role-title');
    const desc = document.getElementById('sim16-desc');

    if (role === 'mechanic') {
        title.textContent = "Bicycle Mechanic (Finding Punctures)";
        desc.innerHTML = "The mechanic immerses an inflated black rubber tube into a basin of water. When air bubbles stream upward from a single point, physics reveals the exact invisible puncture hole!";
        svg.innerHTML = `
            <!-- Water basin -->
            <ellipse cx="225" cy="140" rx="140" ry="35" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
            <!-- Submerged Tyre tube -->
            <path d="M140,135 Q225,160 310,135" stroke="#1e293b" stroke-width="14" fill="none" stroke-linecap="round"/>
            <!-- Escaping air bubbles -->
            <circle cx="210" cy="125" r="4" fill="#e0f2fe"/>
            <circle cx="205" cy="100" r="5" fill="#e0f2fe"/>
            <circle cx="212" cy="75" r="6" fill="#e0f2fe"/>
            <text x="210" y="55" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Air Bubbles Pinpoint Puncture!</text>
        `;
    } else if (role === 'cook') {
        title.textContent = "Master Cook (Pressure Regulation)";
        desc.innerHTML = "When liquid sputters out of the weight valve, the cook diagnoses: <em>'The heat is causing violent boiling that overwhelms headspace!'</em> They reduce the burner flame to steady cooking.";
        svg.innerHTML = `
            <rect x="170" y="60" width="110" height="80" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
            <rect x="215" y="45" width="20" height="15" fill="#f59e0b"/>
            <!-- Flame controlled -->
            <path d="M190,150 Q200,160 210,150 Q220,160 230,150 Q240,160 250,150" stroke="#f97316" stroke-width="4" fill="none"/>
            <text x="225" y="30" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Flame Turned to Simmer</text>
            <text x="225" y="175" fill="#cbd5e1" font-size="10" text-anchor="middle">Optimal Thermodynamic Balance</text>
        `;
    } else {
        title.textContent = "Electrician (Circuit Diagnosis)";
        desc.innerHTML = "When a room goes dark, the electrician doesn't smash the bulb. They use a multimeter tester to verify whether voltage reaches the socket, systematically diagnosing the broken path.";
        svg.innerHTML = `
            <!-- Circuit battery and wires -->
            <rect x="80" y="70" width="60" height="35" rx="4" fill="#334155" stroke="#64748b"/>
            <text x="110" y="92" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Battery</text>
            <!-- Wire to switch -->
            <line x1="140" y1="87" x2="210" y2="87" stroke="#22c55e" stroke-width="3"/>
            <!-- Switch -->
            <circle cx="210" cy="87" r="4" fill="#f59e0b"/>
            <line x1="210" y1="87" x2="245" y2="70" stroke="#f59e0b" stroke-width="3"/>
            <circle cx="250" cy="87" r="4" fill="#f59e0b"/>
            <!-- Wire to bulb -->
            <line x1="250" y1="87" x2="320" y2="87" stroke="#22c55e" stroke-width="3"/>
            <circle cx="335" cy="87" r="14" fill="#475569" stroke="#94a3b8"/>
            <text x="225" y="145" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Open Switch Detected: Complete the Path!</text>
        `;
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    setSim1Target('sea');
    setSim2Domain('kitchen');
    renderSim3();
    setSim4Habitat('desert');
    updateSim5();
    renderSim6();
    triggerSim7Phase('evap');
    updateSim8();
    setSim9Step(1);
    testSim10Material('iron');
    renderSim11();
    setSim12Action('check_ink');
    setSim13Case('rainbow');
    runSim14Days();
    setSim15Scenario('support');
    setSim16Role('mechanic');

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''

# Verify zero raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')
matches = raw_latex_pattern.findall(js_code)
if matches:
    print("WARNING: Found potential raw LaTeX in JS code:", set(matches))
else:
    print("VERIFIED PASS: Zero raw LaTeX in JS code!")

with open(".agents/class6_science_ch1_js.py", "w", encoding="utf-8") as f:
    f.write('"""\nJavaScript Code for Class 6 Science Chapter 1 Interactive Lab\n"""\n\n')
    f.write('JS_CODE = ' + repr(js_code) + '\n')

print("Successfully wrote .agents/class6_science_ch1_js.py")

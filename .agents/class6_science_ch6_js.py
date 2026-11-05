"""
Interactive JavaScript for Class 6 Science Chapter 6: Materials Around Us
Handles sentence-by-sentence Web Speech API, slide switcher, 16 simulators, checkpoints, and 40 quiz questions.
Zero raw LaTeX. Pure Unicode.
"""

JS_CODE = '''
// Science Chapter 6 Interactive JavaScript
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
// Simulator 1: Object Anatomy Disassembler
// -------------------------------------------------------------
const sim1Data = {
    pen: {
        title: "Retractable Ballpoint Pen",
        svg: `
            <svg width="300" height="120" viewBox="0 0 300 120">
                <!-- Plastic Barrel -->
                <rect x="50" y="45" width="160" height="25" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
                <text x="130" y="62" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Plastic Barrel</text>
                <!-- Metal Tip -->
                <polygon points="50,45 20,57.5 50,70" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                <circle cx="18" cy="57.5" r="3" fill="#64748b"/>
                <text x="35" y="52" fill="#fbbf24" font-size="7" font-weight="bold">Brass</text>
                <!-- Steel Clip -->
                <path d="M 190,45 L 190,30 L 130,30 L 130,35" fill="none" stroke="#94a3b8" stroke-width="3"/>
                <text x="160" y="25" fill="#cbd5e1" font-size="8" font-weight="bold">Steel Clip</text>
                <!-- Push Button -->
                <rect x="210" y="50" width="25" height="15" rx="2" fill="#ef4444"/>
                <!-- Internal Ink Tube -->
                <line x1="25" y1="57.5" x2="200" y2="57.5" stroke="#1e1b4b" stroke-width="3" stroke-dasharray="3,2"/>
            </svg>
        `,
        parts: [
            { name: "Outer Barrel & Grip", material: "Synthetic Polymer (Plastic)", role: "Lightweight, ergonomic, non-conductive casing" },
            { name: "Writing Ball Point", material: "Tungsten Carbide / Brass", role: "Ultra-hard, wear-resistant spherical roller" },
            { name: "Retractable Spring & Clip", material: "High-Tensile Stainless Steel", role: "Elastic recoil mechanism and pocket anchor" },
            { name: "Writing Core", material: "Viscous Dye Solution (Liquid Ink)", role: "Evenly flowing marking fluid" }
        ]
    },
    pencil: {
        title: "Standard Graphite Pencil",
        svg: `
            <svg width="300" height="120" viewBox="0 0 300 120">
                <!-- Wood Shaft -->
                <polygon points="50,50 20,60 50,70" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
                <polygon points="20,60 10,60 25,56" fill="#334155"/>
                <rect x="50" y="50" width="160" height="20" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <text x="130" y="64" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">Cedar Wood Body</text>
                <!-- Ferrule -->
                <rect x="210" y="49" width="20" height="22" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
                <!-- Eraser -->
                <rect x="230" y="51" width="25" height="18" rx="2" fill="#f43f5e"/>
                <text x="242" y="63" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Eraser</text>
            </svg>
        `,
        parts: [
            { name: "Casing Slats", material: "Soft Incense-Cedar Wood", role: "Protects core, easy to sharpen with blade" },
            { name: "Writing Core", material: "Compressed Graphite & Clay", role: "Leaves friction-deposited carbon marks on paper" },
            { name: "Ferrule Collar", material: "Aluminium Metal", role: "Clamps the eraser securely to the wood shaft" },
            { name: "Eraser Tip", material: "Vulcanized Rubber / Polymer", role: "Frictional abrasion to lift graphite without tearing paper" }
        ]
    },
    scissors: {
        title: "Craft Tailor Scissors",
        svg: `
            <svg width="300" height="120" viewBox="0 0 300 120">
                <!-- Steel Blades -->
                <polygon points="40,35 170,55 170,60 40,45" fill="#cbd5e1" stroke="#64748b" stroke-width="1.5"/>
                <polygon points="40,85 170,65 170,60 40,75" fill="#94a3b8" stroke="#64748b" stroke-width="1.5"/>
                <circle cx="165" cy="60" r="5" fill="#334155" stroke="#cbd5e1" stroke-width="1.5"/>
                <!-- Plastic Handles -->
                <ellipse cx="225" cy="40" rx="35" ry="18" fill="#e11d48" stroke="#9f1239" stroke-width="2"/>
                <ellipse cx="225" cy="40" rx="20" ry="9" fill="#020617"/>
                <ellipse cx="225" cy="80" rx="35" ry="18" fill="#e11d48" stroke="#9f1239" stroke-width="2"/>
                <ellipse cx="225" cy="80" rx="20" ry="9" fill="#020617"/>
            </svg>
        `,
        parts: [
            { name: "Cutting Blades", material: "Hardened Stainless Steel", role: "Retains sharp shearing edge, resists corrosion" },
            { name: "Pivot Screw", material: "High-Tensile Brass / Steel", role: "Maintains optimal shear tension between blades" },
            { name: "Finger Bows & Grips", material: "Molded Thermoplastic (Polypropylene)", role: "Cushions hand pressure during forceful cutting" }
        ]
    },
    bottle: {
        title: "Vacuum Insulated Flask",
        svg: `
            <svg width="300" height="120" viewBox="0 0 300 120">
                <!-- Double Wall Flask Body -->
                <rect x="70" y="30" width="130" height="60" rx="10" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
                <rect x="80" y="38" width="110" height="44" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2"/>
                <text x="135" y="64" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Vacuum Chamber</text>
                <!-- Cap -->
                <rect x="200" y="42" width="30" height="36" rx="4" fill="#059669" stroke="#047857" stroke-width="2"/>
                <!-- Silicone Seal -->
                <rect x="195" y="48" width="6" height="24" rx="2" fill="#f43f5e"/>
            </svg>
        `,
        parts: [
            { name: "Inner & Outer Flask Walls", material: "Food-Grade Stainless Steel (18/8)", role: "Unbreakable, hygienic, prevents flavor absorption" },
            { name: "Vacuum Gap", material: "Empty Space (Absence of Matter)", role: "Eliminates heat transfer by conduction & convection" },
            { name: "Threaded Stopper", material: "BPA-Free Polypropylene Plastic", role: "Lightweight thermal insulation for top opening" },
            { name: "Sealing Gasket Ring", material: "Flexible Food-Grade Silicone", role: "Elastic, waterproof seal to prevent liquid leaks" }
        ]
    }
};

function selectSim1Object(type) {
    ['pen', 'pencil', 'scissors', 'bottle'].forEach(t => {
        const btn = document.getElementById(`sim1Btn-${t}`);
        if (btn) {
            btn.className = (t === type) ?
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white transition' :
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const data = sim1Data[type];
    const stage = document.getElementById('sim1Stage');
    const details = document.getElementById('sim1Details');

    if (stage) stage.innerHTML = data.svg;
    if (details) {
        details.innerHTML = `
            <div class="flex items-center justify-between mb-1">
                <span class="font-bold text-indigo-300">${data.title}</span>
                <span class="text-[10px] text-slate-400 font-semibold">${data.parts.length} Distinct Materials</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                ${data.parts.map(p => `
                    <div class="p-2 rounded bg-slate-900/80 border border-slate-800">
                        <span class="font-bold text-white block text-[11px]">${p.name}</span>
                        <span class="text-emerald-400 font-mono block text-[10px]">${p.material}</span>
                        <span class="text-slate-400 text-[10px]">${p.role}</span>
                    </div>
                `).join('')}
            </div>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 2: Harappan Terracotta Kiln Simulator
// -------------------------------------------------------------
function setSim2Stage(stage) {
    const potBody = document.getElementById('sim2PotBody');
    const motifs = document.getElementById('sim2Motifs');
    const label = document.getElementById('sim2PotLabel');
    const badge = document.getElementById('sim2StatusBadge');
    const glow = document.getElementById('sim2FireGlow');
    const exp = document.getElementById('sim2Explanation');

    if (stage === 'raw') {
        if (potBody) potBody.setAttribute('fill', '#78716c');
        if (motifs) motifs.setAttribute('opacity', '0');
        if (label) { label.textContent = 'Soft Wet Clay (Raw Mud)'; label.className = 'text-xs font-bold text-stone-400 mt-2'; }
        if (badge) { badge.textContent = 'Raw River Clay'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20'; }
        if (glow) glow.style.opacity = '0';
        if (exp) exp.innerHTML = 'Raw river clay is malleable and plastic when moist. It dissolves into slurry if exposed to rain.';
    } else if (stage === 'fire') {
        if (potBody) potBody.setAttribute('fill', '#f97316');
        if (motifs) motifs.setAttribute('opacity', '0.4');
        if (label) { label.textContent = 'Kiln Firing at 850°C! 🔥'; label.className = 'text-xs font-bold text-orange-400 mt-2 animate-pulse'; }
        if (badge) { badge.textContent = 'High-Temp Firing (850°C)'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-orange-500/20 text-orange-300 border border-orange-500/30 animate-pulse'; }
        if (glow) glow.style.opacity = '1';
        if (exp) exp.innerHTML = 'Intense kiln heat permanently expels bound water molecules and fuses silicate minerals into a vitreous ceramic bond.';
    } else if (stage === 'cool') {
        if (potBody) potBody.setAttribute('fill', '#c2410c');
        if (motifs) motifs.setAttribute('opacity', '1');
        if (label) { label.textContent = 'Durable Harappan Terracotta Artifact ✨'; label.className = 'text-xs font-bold text-amber-400 mt-2'; }
        if (badge) { badge.textContent = 'Baked Terracotta (Harappan Red)'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'; }
        if (glow) glow.style.opacity = '0';
        if (exp) exp.innerHTML = 'Permanent transformation! The terracotta is now rock-hard, insoluble in water, and decorated with traditional black geometric slips.';
    }
}

// -------------------------------------------------------------
// Simulator 3: Material Substitution Lab
// -------------------------------------------------------------
const sim3Materials = {
    glass: {
        name: "Transparent Borosilicate Glass",
        svg: `
            <svg width="100" height="110" viewBox="0 0 100 110">
                <polygon points="20,15 80,15 70,95 30,95" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="2"/>
                <ellipse cx="50" cy="15" rx="30" ry="6" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="1.5"/>
                <line x1="35" y1="30" x2="65" y2="30" stroke="#bae6fd" stroke-width="2" stroke-linecap="round"/>
            </svg>
        `,
        transparency: { label: "100% (Transparent)", width: "100%", color: "bg-cyan-500" },
        durability: { label: "Low (Brittle Fragile)", width: "25%", color: "bg-rose-500" },
        thermal: { label: "Moderate Conduction", width: "50%", color: "bg-amber-500" }
    },
    steel: {
        name: "18/8 Stainless Steel Tumbler",
        svg: `
            <svg width="100" height="110" viewBox="0 0 100 110">
                <polygon points="20,15 80,15 70,95 30,95" fill="url(#steelGrad)" stroke="#94a3b8" stroke-width="2"/>
                <ellipse cx="50" cy="15" rx="30" ry="6" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
                <defs>
                    <linearGradient id="steelGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#475569"/>
                        <stop offset="50%" stop-color="#cbd5e1"/>
                        <stop offset="100%" stop-color="#334155"/>
                    </linearGradient>
                </defs>
            </svg>
        `,
        transparency: { label: "0% (Completely Opaque)", width: "0%", color: "bg-slate-600" },
        durability: { label: "100% (Shatterproof Tough)", width: "100%", color: "bg-emerald-500" },
        thermal: { label: "Very High Conduction", width: "95%", color: "bg-rose-500" }
    },
    clay: {
        name: "Unglazed Earthen Kulhad",
        svg: `
            <svg width="100" height="110" viewBox="0 0 100 110">
                <polygon points="22,20 78,20 68,95 32,95" fill="#9a3412" stroke="#7c2d12" stroke-width="2"/>
                <ellipse cx="50" cy="20" rx="28" ry="6" fill="#b45309" stroke="#7c2d12" stroke-width="1.5"/>
            </svg>
        `,
        transparency: { label: "0% (Opaque)", width: "0%", color: "bg-slate-600" },
        durability: { label: "Moderate (Porcelain Fragile)", width: "40%", color: "bg-amber-500" },
        thermal: { label: "Natural Evaporative Cooling", width: "30%", color: "bg-cyan-500" }
    },
    plastic: {
        name: "Polypropylene Plastic Tumbler",
        svg: `
            <svg width="100" height="110" viewBox="0 0 100 110">
                <polygon points="20,15 80,15 70,95 30,95" fill="#ec4899" stroke="#be185d" stroke-width="2"/>
                <ellipse cx="50" cy="15" rx="30" ry="6" fill="#f472b6" stroke="#be185d" stroke-width="1.5"/>
            </svg>
        `,
        transparency: { label: "Translucent (Colored)", width: "50%", color: "bg-pink-500" },
        durability: { label: "High (Impact Resistant)", width: "85%", color: "bg-emerald-500" },
        thermal: { label: "Low (Thermal Insulator)", width: "20%", color: "bg-blue-500" }
    }
};

function setSim3Material(mat) {
    ['glass', 'steel', 'clay', 'plastic'].forEach(m => {
        const btn = document.getElementById(`sim3Btn-${m}`);
        if (btn) {
            btn.className = (m === mat) ?
                'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs transition' :
                'p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition';
        }
    });

    const d = sim3Materials[mat];
    const graphic = document.getElementById('sim3CupGraphic');
    const nameEl = document.getElementById('sim3MaterialName');

    if (graphic) graphic.innerHTML = d.svg;
    if (nameEl) nameEl.textContent = d.name;

    const tVal = document.getElementById('sim3ValTransparency');
    const tBar = document.getElementById('sim3BarTransparency');
    if (tVal) tVal.textContent = d.transparency.label;
    if (tBar) { tBar.style.width = d.transparency.width; tBar.className = `${d.transparency.color} h-2 rounded-full`; }

    const dVal = document.getElementById('sim3ValDurability');
    const dBar = document.getElementById('sim3BarDurability');
    if (dVal) dVal.textContent = d.durability.label;
    if (dBar) { dBar.style.width = d.durability.width; dBar.className = `${d.durability.color} h-2 rounded-full`; }

    const thVal = document.getElementById('sim3ValThermal');
    const thBar = document.getElementById('sim3BarThermal');
    if (thVal) thVal.textContent = d.thermal.label;
    if (thBar) { thBar.style.width = d.thermal.width; thBar.className = `${d.thermal.color} h-2 rounded-full`; }
}

// -------------------------------------------------------------
// Simulator 4: Material Tree Explorer
// -------------------------------------------------------------
const sim4Data = {
    wood: {
        summary: "Wood possesses high tensile strength along its grain and easy workability, enabling objects from structural furniture to aerodynamic cricket bats.",
        items: [
            { icon: "🪑", name: "Chair / Desk", reason: "Compressive load bearing" },
            { icon: "🏏", name: "Cricket Bat", reason: "Willow grain elastic rebound" },
            { icon: "🚪", name: "Door Panel", reason: "Acoustic and thermal insulation" },
            { icon: "✏️", name: "Pencil Slat", reason: "Easy sharpening with blade" },
            { icon: "🚣", name: "Canoe / Boat", reason: "Less dense than water (floats!)" }
        ]
    },
    steel: {
        summary: "Iron & Steel provide extraordinary tensile strength and magnetic permeability, serving as the backbone of heavy infrastructure.",
        items: [
            { icon: "🥄", name: "Spoon / Fork", reason: "Non-toxic food hygiene" },
            { icon: "🌉", name: "Bridge Girders", reason: "Withstands mega-ton stresses" },
            { icon: "🧲", name: "Electromagnet", reason: "Ferromagnetic core alignment" },
            { icon: "🪡", name: "Sewing Needle", reason: "Ultra-fine rigid sharpness" },
            { icon: "🚂", name: "Railway Track", reason: "Resists extreme rolling wear" }
        ]
    },
    plastic: {
        summary: "Synthetic polymers can be molded into virtually any 3D geometry, provide electrical insulation, and resist atmospheric corrosion.",
        items: [
            { icon: "🪥", name: "Toothbrush", reason: "Molded handle + nylon bristles" },
            { icon: "🪣", name: "Water Bucket", reason: "Lightweight, impermeable" },
            { icon: "🔌", name: "Cable Sheath", reason: "High electrical insulation" },
            { icon: "🧱", name: "Toy Blocks", reason: "Precision dimensional snap" },
            { icon: "🧴", name: "Soap Dispenser", reason: "Chemical resistance" }
        ]
    },
    cotton: {
        summary: "Natural cotton cellulose fibers have soft texture, high moisture absorbency, and hypoallergenic comfort against human skin.",
        items: [
            { icon: "👕", name: "Summer Shirt", reason: "Absorbs sweat, breathable" },
            { icon: "🩹", name: "Medical Bandage", reason: "Soft, sterile wound dressing" },
            { icon: "🛏️", name: "Bed Mattress", reason: "Compressible plush cushioning" },
            { icon: "🧵", name: "Sewing Thread", reason: "High tensile twisted fiber" },
            { icon: "👜", name: "Shopping Bag", reason: "Biodegradable eco-tote" }
        ]
    }
};

function setSim4Tree(mat) {
    ['wood', 'steel', 'plastic', 'cotton'].forEach(m => {
        const btn = document.getElementById(`sim4Btn-${m}`);
        if (btn) {
            btn.className = (m === mat) ?
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 text-white transition' :
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const d = sim4Data[mat];
    const canvas = document.getElementById('sim4Canvas');
    const summary = document.getElementById('sim4Summary');

    if (canvas) {
        canvas.innerHTML = `
            <div class="flex items-center justify-around w-full">
                ${d.items.map(item => `
                    <div class="flex flex-col items-center p-2 rounded-xl bg-slate-900 border border-slate-800 shadow-md transform hover:scale-105 transition w-24 text-center">
                        <span class="text-2xl mb-1">${item.icon}</span>
                        <span class="text-[11px] font-bold text-white block truncate w-full">${item.name}</span>
                        <span class="text-[9px] text-emerald-400 mt-1 leading-tight">${item.reason}</span>
                    </div>
                `).join('')}
            </div>
        `;
    }
    if (summary) summary.textContent = d.summary;
}

// -------------------------------------------------------------
// Simulator 5: Interactive Sorting Station
// -------------------------------------------------------------
const sim5Items = [
    { id: 1, name: "Tennis Ball 🎾", type: "spherical" },
    { id: 2, name: "Textbook 📚", type: "non-spherical" },
    { id: 3, name: "Glass Marble 🔮", type: "spherical" },
    { id: 4, name: "Wooden Ruler 📏", type: "non-spherical" },
    { id: 5, name: "Fresh Orange 🍊", type: "spherical" },
    { id: 6, name: "Pencil Carton 📦", type: "non-spherical" }
];
let sim5Selected = null;
let sim5SortedCount = 0;
let sim5State = {};

function resetSim5() {
    sim5Selected = null;
    sim5SortedCount = 0;
    sim5State = {};
    renderSim5();
}

function renderSim5() {
    const pool = document.getElementById('sim5ItemPool');
    const sBin = document.getElementById('sim5SphericalItems');
    const nsBin = document.getElementById('sim5NonSphericalItems');
    const score = document.getElementById('sim5ScoreBadge');
    const prompt = document.getElementById('sim5Prompt');

    if (score) score.textContent = `${sim5SortedCount} / 6 Sorted`;

    if (pool) {
        pool.innerHTML = sim5Items.filter(it => !sim5State[it.id]).map(it => `
            <button onclick="selectSim5Item(${it.id})" class="px-2.5 py-1.5 rounded-lg text-xs font-semibold ${sim5Selected === it.id ? 'bg-amber-500 text-slate-950 font-bold ring-2 ring-white' : 'bg-slate-800 text-slate-200 hover:bg-slate-700'} border border-slate-700 transition">
                ${it.name}
            </button>
        `).join('');
    }

    if (sBin) {
        sBin.innerHTML = sim5Items.filter(it => sim5State[it.id] === 'spherical').map(it => `
            <span class="px-2 py-1 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-[10px] font-bold">
                ${it.name}
            </span>
        `).join('');
    }

    if (nsBin) {
        nsBin.innerHTML = sim5Items.filter(it => sim5State[it.id] === 'non-spherical').map(it => `
            <span class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[10px] font-bold">
                ${it.name}
            </span>
        `).join('');
    }

    if (prompt) {
        if (sim5SortedCount === 6) {
            prompt.innerHTML = "<strong class='text-emerald-400'>🎉 Perfect Classification! All 6 items grouped accurately by geometrical shape.</strong>";
        } else if (sim5Selected) {
            const item = sim5Items.find(i => i.id === sim5Selected);
            prompt.innerHTML = `Selected <strong>${item.name}</strong>. Now click the correct destination bin below!`;
        } else {
            prompt.innerHTML = "Click any object in the pool above, then click the correct destination bin.";
        }
    }
}

function selectSim5Item(id) {
    sim5Selected = id;
    renderSim5();
}

function dropSim5Item(targetBin) {
    if (!sim5Selected) return;
    const item = sim5Items.find(i => i.id === sim5Selected);
    if (item.type === targetBin) {
        sim5State[item.id] = targetBin;
        sim5SortedCount++;
        sim5Selected = null;
    } else {
        alert(`Incorrect bin! ${item.name} is ${item.type === 'spherical' ? 'spherical' : 'non-spherical'}.`);
    }
    renderSim5();
}

// -------------------------------------------------------------
// Simulator 6: The Tumbler & Bounce Lab
// -------------------------------------------------------------
let sim6Mode = 'tumbler';
function setSim6Mode(mode) {
    sim6Mode = mode;
    const btnT = document.getElementById('sim6Mode-tumbler');
    const btnB = document.getElementById('sim6Mode-bounce');
    if (btnT) btnT.className = (mode === 'tumbler') ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    if (btnB) btnB.className = (mode === 'bounce') ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    renderSim6();
}

function renderSim6() {
    const ws = document.getElementById('sim6Workspace');
    const ctrl = document.getElementById('sim6Controls');
    const fb = document.getElementById('sim6Feedback');

    if (sim6Mode === 'tumbler') {
        if (ws) {
            ws.innerHTML = `
                <div id="sim6TumblerStage" class="flex items-center justify-around w-full">
                    <!-- Cloth Tumbler -->
                    <div class="flex flex-col items-center">
                        <div id="clothCup" class="w-16 h-24 border-2 border-dashed border-amber-400 bg-amber-900/30 rounded-b-xl relative flex items-center justify-center">
                            <span class="text-[9px] text-amber-300 font-bold">Cloth Cup</span>
                            <div id="clothDrips" class="absolute -bottom-8 flex flex-col items-center opacity-0 transition-opacity">
                                <span class="text-xs text-cyan-400">💧 💧 💧</span>
                                <span class="text-[9px] text-rose-400 font-bold">LEAKING!</span>
                            </div>
                        </div>
                        <span class="text-[10px] text-slate-400 mt-2">Woven Cotton Fabric</span>
                    </div>
                    <!-- Steel Tumbler -->
                    <div class="flex flex-col items-center">
                        <div id="steelCup" class="w-16 h-24 border-2 border-slate-400 bg-slate-700/60 rounded-b-xl relative flex items-center justify-center overflow-hidden">
                            <span class="text-[9px] text-slate-200 font-bold">Steel Cup</span>
                            <div id="steelWater" class="absolute bottom-0 w-full bg-cyan-500/60 h-0 transition-all duration-500"></div>
                        </div>
                        <span class="text-[10px] text-slate-400 mt-2">Solid Stainless Steel</span>
                    </div>
                </div>
            `;
        }
        if (ctrl) {
            ctrl.innerHTML = `
                <button onclick="pourSim6Water()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-lg transition">
                    💧 Pour 250 mL Water into Both Tumblers
                </button>
                <button onclick="resetSim6Tumbler()" class="text-xs text-slate-400 hover:text-white underline">Empty</button>
            `;
        }
        if (fb) fb.innerHTML = "Woven cloth contains microscopic pores between fibers. Pour water to test impermeability.";
    } else {
        if (ws) {
            ws.innerHTML = `
                <div class="flex items-end justify-around w-full h-36 border-b-2 border-slate-700 pb-1">
                    <div class="flex flex-col items-center">
                        <div id="tennisBall" class="w-8 h-8 rounded-full bg-lime-400 flex items-center justify-center text-xs font-bold text-slate-900 shadow-lg transform transition-transform duration-500">🎾</div>
                        <span class="text-[9px] text-lime-400 mt-2">Tennis Ball</span>
                    </div>
                    <div class="flex flex-col items-center">
                        <div id="cricketBall" class="w-8 h-8 rounded-full bg-red-700 border border-amber-300 flex items-center justify-center text-xs font-bold text-white shadow-lg transform transition-transform duration-500">🏏</div>
                        <span class="text-[9px] text-red-400 mt-2">Cricket Ball</span>
                    </div>
                    <div class="flex flex-col items-center">
                        <div id="foamBall" class="w-8 h-8 rounded-full bg-sky-400 flex items-center justify-center text-xs font-bold text-slate-900 shadow-lg transform transition-transform duration-500">🧽</div>
                        <span class="text-[9px] text-sky-400 mt-2">Foam Ball</span>
                    </div>
                </div>
            `;
        }
        if (ctrl) {
            ctrl.innerHTML = `
                <button onclick="dropSim6Balls()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-lg transition">
                    ⬇️ Drop from 1 Metre Height
                </button>
                <span class="text-xs text-slate-400">Compare Elastic Rebounds</span>
            `;
        }
        if (fb) fb.innerHTML = "Different sports demand different material dynamics: hollow pressurized rubber rebounds high, wound leather is dense, and sponge absorbs shock.";
    }
}

function pourSim6Water() {
    const drips = document.getElementById('clothDrips');
    const water = document.getElementById('steelWater');
    const fb = document.getElementById('sim6Feedback');

    if (drips) drips.style.opacity = '1';
    if (water) water.style.height = '75%';
    if (fb) fb.innerHTML = "<strong class='text-rose-400'>Failure vs Success:</strong> Water pours straight through the porous cloth fibers. The stainless steel vessel retains 100% of the liquid safely!";
}

function resetSim6Tumbler() {
    const drips = document.getElementById('clothDrips');
    const water = document.getElementById('steelWater');
    if (drips) drips.style.opacity = '0';
    if (water) water.style.height = '0%';
}

function dropSim6Balls() {
    const tb = document.getElementById('tennisBall');
    const cb = document.getElementById('cricketBall');
    const fb = document.getElementById('foamBall');
    const feed = document.getElementById('sim6Feedback');

    if (tb) {
        tb.style.transform = 'translateY(-70px)';
        setTimeout(() => { tb.style.transform = 'translateY(0px)'; }, 500);
    }
    if (cb) {
        cb.style.transform = 'translateY(-30px)';
        setTimeout(() => { cb.style.transform = 'translateY(0px)'; }, 500);
    }
    if (fb) {
        fb.style.transform = 'translateY(-5px)';
        setTimeout(() => { fb.style.transform = 'translateY(0px)'; }, 500);
    }

    if (feed) {
        feed.innerHTML = "<strong class='text-amber-400'>Rebound Analysis:</strong> Tennis ball (vulcanized rubber) bounces 70 cm; cricket ball (cork + leather) bounces 30 cm; foam ball (polyurethane) absorbs energy and bounces only 5 cm.";
    }
}

// -------------------------------------------------------------
// Simulator 7: Fresh Cut & Lustre Polish Station
// -------------------------------------------------------------
let sim7Metal = 'copper';
const sim7Colors = {
    copper: { tarnish: "#78350f", fresh: "#f59e0b", name: "Copper Rod (Cu)" },
    iron: { tarnish: "#451a03", fresh: "#94a3b8", name: "Iron Rod (Fe)" },
    aluminium: { tarnish: "#475569", fresh: "#f1f5f9", name: "Aluminium Pipe (Al)" }
};

function setSim7Sample(sample) {
    sim7Metal = sample;
    ['copper', 'iron', 'aluminium'].forEach(m => {
        const btn = document.getElementById(`sim7Btn-${m}`);
        if (btn) {
            btn.className = (m === sample) ?
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 text-white transition' :
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });
    resetSim7Rod();
}

function renderSim7Graphic(isCut) {
    const graphic = document.getElementById('sim7RodGraphic');
    const d = sim7Colors[sim7Metal];
    if (!graphic) return;

    if (!isCut) {
        graphic.innerHTML = `
            <svg width="280" height="70" viewBox="0 0 280 70">
                <rect x="20" y="20" width="240" height="30" rx="6" fill="${d.tarnish}" stroke="#1e293b" stroke-width="2"/>
                <text x="140" y="38" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">Tarnished / Oxidized Surface</text>
            </svg>
        `;
    } else {
        graphic.innerHTML = `
            <svg width="280" height="70" viewBox="0 0 280 70">
                <!-- Left Piece -->
                <rect x="20" y="20" width="110" height="30" rx="4" fill="${d.tarnish}"/>
                <!-- Right Piece -->
                <rect x="150" y="20" width="110" height="30" rx="4" fill="${d.tarnish}"/>
                <!-- Gleaming Fresh Cut Faces -->
                <rect x="126" y="18" width="6" height="34" rx="2" fill="${d.fresh}" stroke="#ffffff" stroke-width="1.5" class="animate-pulse"/>
                <rect x="148" y="18" width="6" height="34" rx="2" fill="${d.fresh}" stroke="#ffffff" stroke-width="1.5" class="animate-pulse"/>
                <text x="140" y="62" fill="${d.fresh}" font-size="9" font-weight="bold" text-anchor="middle">Freshly Exposed Metallic Lustre! ✨</text>
            </svg>
        `;
    }
}

function cutSim7Rod() {
    renderSim7Graphic(true);
    const sparkles = document.getElementById('sim7Sparkles');
    const badge = document.getElementById('sim7Badge');
    const status = document.getElementById('sim7Status');
    const d = sim7Colors[sim7Metal];

    if (sparkles) { sparkles.style.opacity = '1'; setTimeout(() => { sparkles.style.opacity = '0'; }, 1000); }
    if (badge) { badge.textContent = 'Fresh Cut Lustre Exposed'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'; }
    if (status) status.innerHTML = `<strong class='text-amber-300'>Diagnostic Proof:</strong> The hacksaw cut slices past the microscopic oxide patina, exposing pure metallic atoms with high specular reflectivity (${d.name})!`;
}

function sandpaperSim7Rod() {
    cutSim7Rod();
}

function resetSim7Rod() {
    renderSim7Graphic(false);
    const badge = document.getElementById('sim7Badge');
    const status = document.getElementById('sim7Status');
    if (badge) { badge.textContent = 'Tarnished Outer Layer'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/20'; }
    if (status) status.innerHTML = "Atmospheric oxygen and humidity have tarnished the outer atoms. Slicing reveals pristine lustre.";
}

// -------------------------------------------------------------
// Simulator 8: Light Reflection Analyzer
// -------------------------------------------------------------
function setSim8Material(mat) {
    ['gold', 'wood', 'varnish'].forEach(m => {
        const btn = document.getElementById(`sim8Btn-${m}`);
        if (btn) {
            btn.className = (m === mat) ?
                'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs' :
                'p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs';
        }
    });

    const svg = document.getElementById('sim8Svg');
    const badge = document.getElementById('sim8ModeBadge');
    const exp = document.getElementById('sim8Explanation');
    if (!svg) return;

    if (mat === 'gold') {
        if (badge) { badge.textContent = 'Specular Reflection'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30'; }
        if (exp) exp.textContent = "Gold has dense, free-electron planes that bounce incoming light in an orderly, single specular beam (true metallic lustre).";
        svg.innerHTML = `
            <!-- Torch -->
            <rect x="20" y="20" width="40" height="20" rx="3" fill="#334155"/>
            <!-- Incident Beam -->
            <line x1="60" y1="30" x2="170" y2="100" stroke="#facc15" stroke-width="4"/>
            <!-- Sample -->
            <rect x="130" y="100" width="80" height="15" rx="2" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
            <text x="170" y="125" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">Gold Leaf (Metal)</text>
            <!-- Specular Reflected Beam -->
            <line x1="170" y1="100" x2="280" y2="30" stroke="#facc15" stroke-width="4" stroke-dasharray="0"/>
            <polygon points="280,30 270,36 276,43" fill="#facc15"/>
        `;
    } else if (mat === 'wood') {
        if (badge) { badge.textContent = 'Diffuse Scattering (Dull)'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-slate-500/20 text-slate-300 border border-slate-500/30'; }
        if (exp) exp.textContent = "Rough cellular cellulose fibers in untreated wood scatter incident light randomly in all directions, appearing matte and dull.";
        svg.innerHTML = `
            <rect x="20" y="20" width="40" height="20" rx="3" fill="#334155"/>
            <line x1="60" y1="30" x2="170" y2="100" stroke="#facc15" stroke-width="4"/>
            <rect x="130" y="100" width="80" height="15" rx="2" fill="#78350f" stroke="#451a03" stroke-width="2"/>
            <text x="170" y="125" fill="#d6d3d1" font-size="9" font-weight="bold" text-anchor="middle">Rough Wood (Non-Lustrous)</text>
            <!-- Scattered Rays -->
            <line x1="170" y1="100" x2="210" y2="40" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="2,2"/>
            <line x1="170" y1="100" x2="250" y2="55" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="2,2"/>
            <line x1="170" y1="100" x2="130" y2="40" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="2,2"/>
            <line x1="170" y1="100" x2="170" y2="30" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="2,2"/>
        `;
    } else {
        if (badge) { badge.textContent = 'Artificial Varnish Gloss'; badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30'; }
        if (exp) exp.textContent = "A synthetic resin varnish coats the wood with a glass-smooth surface. The gloss is an artificial surface layer, not intrinsic material lustre.";
        svg.innerHTML = `
            <rect x="20" y="20" width="40" height="20" rx="3" fill="#334155"/>
            <line x1="60" y1="30" x2="170" y2="100" stroke="#facc15" stroke-width="4"/>
            <rect x="130" y="102" width="80" height="13" rx="2" fill="#78350f"/>
            <!-- Clear Varnish Film -->
            <rect x="130" y="98" width="80" height="4" rx="1" fill="#38bdf8" opacity="0.8"/>
            <text x="170" y="125" fill="#7dd3fc" font-size="9" font-weight="bold" text-anchor="middle">Varnished Tabletop</text>
            <line x1="170" y1="100" x2="280" y2="30" stroke="#facc15" stroke-width="3"/>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 9: Hardness Compression & Scratch Gauge
// -------------------------------------------------------------
let sim9Sample = 'sponge';
const sim9Data = {
    sponge: { name: "Bath Sponge", comp: "85% (High)", scratch: "Punctured instantly", soft: true, height: 40 },
    wax: { name: "Candle Wax", comp: "20% (Low)", scratch: "Deep white gouge", soft: true, height: 35 },
    wood: { name: "Pine Wood", comp: "3% (Very Low)", scratch: "Shallow indent line", soft: false, height: 35 },
    iron: { name: "Iron Plate", comp: "0% (Zero Compressible)", scratch: "Nail tip deflects (no scratch!)", soft: false, height: 35 }
};

function setSim9Sample(sample) {
    sim9Sample = sample;
    ['sponge', 'wax', 'wood', 'iron'].forEach(s => {
        const btn = document.getElementById(`sim9Btn-${s}`);
        if (btn) {
            btn.className = (s === sample) ?
                'p-1.5 rounded-lg bg-indigo-600 text-white font-bold text-xs' :
                'p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs';
        }
    });

    const d = sim9Data[sample];
    const badge = document.getElementById(`sim9Badge`);
    const compVal = document.getElementById(`sim9CompVal`);
    const scratchVal = document.getElementById(`sim9ScratchVal`);
    const graphic = document.getElementById('sim9StageGraphic');

    if (badge) {
        badge.textContent = d.soft ? 'Soft Material' : 'Hard Material';
        badge.className = d.soft ?
            'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20' :
            'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/20';
    }
    if (compVal) compVal.textContent = d.comp;
    if (scratchVal) scratchVal.textContent = d.scratch;

    if (graphic) {
        graphic.innerHTML = `
            <div id="sim9Piston" class="w-20 h-6 bg-slate-700 border-2 border-slate-500 rounded-t flex items-center justify-center text-[8px] font-mono text-slate-300 transition-all duration-300">
                50 N Press
            </div>
            <div id="sim9Block" style="height: ${d.height}px;" class="w-24 ${sample === 'sponge' ? 'bg-amber-400' : (sample === 'wax' ? 'bg-amber-100' : (sample === 'wood' ? 'bg-amber-800' : 'bg-slate-400'))} rounded-b border border-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-900 transition-all duration-300">
                ${d.name}
            </div>
        `;
    }
}

function applySim9Pressure() {
    const block = document.getElementById('sim9Block');
    const piston = document.getElementById('sim9Piston');
    if (!block || !piston) return;

    if (sim9Sample === 'sponge') {
        block.style.height = '10px';
        piston.style.transform = 'translateY(25px)';
        setTimeout(() => { block.style.height = '40px'; piston.style.transform = 'translateY(0px)'; }, 1000);
    } else if (sim9Sample === 'wax') {
        block.style.height = '28px';
        piston.style.transform = 'translateY(7px)';
        setTimeout(() => { block.style.height = '35px'; piston.style.transform = 'translateY(0px)'; }, 1000);
    } else {
        piston.style.transform = 'translateY(2px)';
        setTimeout(() => { piston.style.transform = 'translateY(0px)'; }, 500);
    }
}

function scratchSim9Nail() {
    const block = document.getElementById('sim9Block');
    if (!block) return;
    block.classList.add('ring-2', 'ring-rose-500');
    setTimeout(() => { block.classList.remove('ring-2', 'ring-rose-500'); }, 700);
}

// -------------------------------------------------------------
// Simulator 10: Optical Transmission Bench (Transparent)
// -------------------------------------------------------------
function setSim10Medium(med) {
    ['glass', 'water', 'cellophane'].forEach(m => {
        const btn = document.getElementById(`sim10Btn-${m}`);
        if (btn) {
            btn.className = (m === med) ?
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-cyan-600 text-white' :
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300';
        }
    });

    const barrier = document.getElementById('sim10Barrier');
    if (!barrier) return;
    if (med === 'glass') {
        barrier.innerHTML = '<span class="text-[9px] text-cyan-300 font-bold rotate-90 whitespace-nowrap">Clear Glass</span>';
        barrier.className = 'w-16 h-32 rounded-lg border-2 border-cyan-400/60 bg-cyan-400/10 backdrop-blur-[0px] flex items-center justify-center relative shadow-lg shadow-cyan-500/10 transition-all';
    } else if (med === 'water') {
        barrier.innerHTML = '<span class="text-[9px] text-sky-300 font-bold rotate-90 whitespace-nowrap">Clean Water</span>';
        barrier.className = 'w-20 h-32 rounded-lg border-2 border-sky-400/60 bg-sky-500/20 backdrop-blur-[0px] flex items-center justify-center relative shadow-lg shadow-sky-500/10 transition-all';
    } else {
        barrier.innerHTML = '<span class="text-[9px] text-emerald-300 font-bold rotate-90 whitespace-nowrap">Cellophane</span>';
        barrier.className = 'w-10 h-32 rounded-lg border border-emerald-400/50 bg-emerald-400/10 backdrop-blur-[0px] flex items-center justify-center relative transition-all';
    }
}

// -------------------------------------------------------------
// Simulator 11: Shadow Formation & Opaque Blocker
// -------------------------------------------------------------
function setSim11Blocker(blocker) {
    ['cardboard', 'wood', 'metal'].forEach(b => {
        const btn = document.getElementById(`sim11Btn-${b}`);
        if (btn) {
            btn.className = (b === blocker) ?
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-rose-600 text-white' :
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300';
        }
    });

    const barrier = document.getElementById('sim11Barrier');
    if (!barrier) return;
    if (blocker === 'cardboard') {
        barrier.className = 'w-12 h-32 rounded bg-amber-900 border border-amber-700 shadow-2xl flex items-center justify-center';
        barrier.innerHTML = '<span class="text-[9px] text-white font-bold rotate-90 whitespace-nowrap">Cardboard</span>';
    } else if (blocker === 'wood') {
        barrier.className = 'w-16 h-32 rounded bg-amber-950 border border-amber-800 shadow-2xl flex items-center justify-center';
        barrier.innerHTML = '<span class="text-[9px] text-amber-200 font-bold rotate-90 whitespace-nowrap">Thick Wood</span>';
    } else {
        barrier.className = 'w-10 h-32 rounded bg-slate-600 border border-slate-400 shadow-2xl flex items-center justify-center';
        barrier.innerHTML = '<span class="text-[9px] text-white font-bold rotate-90 whitespace-nowrap">Steel Sheet</span>';
    }
}

// -------------------------------------------------------------
// Simulator 12: Frosted Diffuser & Oil Spot (Translucent)
// -------------------------------------------------------------
function setSim12Material(mat) {
    ['butter', 'frosted', 'oilspot'].forEach(m => {
        const btn = document.getElementById(`sim12Btn-${m}`);
        if (btn) {
            btn.className = (m === mat) ?
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 text-white' :
                'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300';
        }
    });

    const sheet = document.getElementById('sim12Sheet');
    const label = document.getElementById('sim12SheetLabel');
    const target = document.getElementById('sim12Target');
    const slider = document.getElementById('sim12Slider');

    if (mat === 'butter') {
        if (label) label.textContent = 'Butter Paper';
        if (sheet) sheet.className = 'w-20 h-32 rounded-lg bg-amber-100/20 border-2 border-amber-300/40 backdrop-blur-md flex items-center justify-center transition-all';
        if (target) { target.style.filter = 'blur(4px)'; target.style.opacity = '0.6'; }
        if (slider) slider.value = 5;
    } else if (mat === 'frosted') {
        if (label) label.textContent = 'Frosted Glass';
        if (sheet) sheet.className = 'w-20 h-32 rounded-lg bg-sky-200/20 border-2 border-sky-300/40 backdrop-blur-lg flex items-center justify-center transition-all';
        if (target) { target.style.filter = 'blur(6px)'; target.style.opacity = '0.5'; }
        if (slider) slider.value = 7;
    } else {
        if (label) label.textContent = 'Oily Paper Spot';
        if (sheet) sheet.className = 'w-20 h-32 rounded-lg bg-yellow-400/30 border-2 border-dashed border-amber-400 flex items-center justify-center transition-all';
        if (target) { target.style.filter = 'blur(3px)'; target.style.opacity = '0.75'; }
        if (slider) slider.value = 4;
    }
}

function adjustSim12Blur(val) {
    const target = document.getElementById('sim12Target');
    const scatterVal = document.getElementById('sim12ScatterVal');
    if (target) {
        target.style.filter = `blur(${val}px)`;
        target.style.opacity = `${Math.max(0.2, 1 - val * 0.08)}`;
    }
    if (scatterVal) {
        scatterVal.textContent = val > 7 ? 'Heavy Scattering (Very Hazy)' : (val > 3 ? 'Medium (Blurry)' : 'Light Scattering');
    }
}

// -------------------------------------------------------------
// Simulator 13: Beaker Dissolution Lab
// -------------------------------------------------------------
let sim13Solute = 'sugar';
const sim13Data = {
    sugar: { name: "Sugar Crystals", soluble: true, sediment: "Zero (Completely Dissolved)", mix: "Clear Homogeneous Solution", color: "rgba(56, 189, 248, 0.2)" },
    salt: { name: "Table Salt", soluble: true, sediment: "Zero (Dissolved Ions)", mix: "Clear Transparent Saline", color: "rgba(56, 189, 248, 0.2)" },
    sand: { name: "River Sand", soluble: false, sediment: "Heavy Bottom Sediment", mix: "Insoluble Suspension (Clears)", color: "rgba(180, 83, 9, 0.4)" },
    chalk: { name: "Chalk Powder", soluble: false, sediment: "Cloudy White Sediment", mix: "Milky Insoluble Suspension", color: "rgba(241, 245, 249, 0.5)" }
};

function setSim13Solute(solute) {
    sim13Solute = solute;
    ['sugar', 'salt', 'sand', 'chalk'].forEach(s => {
        const btn = document.getElementById(`sim13Btn-${s}`);
        if (btn) {
            btn.className = (s === solute) ?
                'p-1.5 rounded-lg bg-emerald-600 text-white font-bold text-xs' :
                'p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs';
        }
    });

    renderSim13Graphic(false);
}

function renderSim13Graphic(isStirred) {
    const d = sim13Data[sim13Solute];
    const graphic = document.getElementById('sim13BeakerGraphic');
    const badge = document.getElementById('sim13StatusBadge');
    const mixType = document.getElementById('sim13MixType');
    const sedVal = document.getElementById('sim13SedimentVal');

    if (badge) {
        badge.textContent = d.soluble ? 'Soluble Substance' : 'Insoluble Substance';
        badge.className = d.soluble ?
            'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20' :
            'px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/20';
    }

    if (mixType) mixType.textContent = isStirred ? d.mix : 'Water + Added Powder';
    if (sedVal) sedVal.textContent = isStirred ? d.sediment : 'Untested';

    if (graphic) {
        graphic.innerHTML = `
            <svg width="110" height="130" viewBox="0 0 110 130">
                <!-- Beaker Body -->
                <rect x="15" y="20" width="80" height="100" rx="4" fill="none" stroke="#64748b" stroke-width="2"/>
                <polygon points="15,20 10,15 25,20" fill="#64748b"/>
                <!-- Liquid Fill -->
                <rect x="17" y="50" width="76" height="68" fill="${isStirred ? (d.soluble ? 'rgba(56, 189, 248, 0.25)' : d.color) : 'rgba(56, 189, 248, 0.2)'}"/>
                <line x1="17" y1="50" x2="93" y2="50" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Particles or Sediment -->
                ${isStirred ? (
                    d.soluble ? `
                        <!-- Tiny invisible dissolved molecules -->
                        <circle cx="50" cy="80" r="1" fill="#ffffff" opacity="0.1"/>
                    ` : `
                        <!-- Bottom Sediment -->
                        <ellipse cx="55" cy="115" rx="35" ry="4" fill="${sim13Solute === 'sand' ? '#92400e' : '#cbd5e1'}"/>
                    `
                ) : `
                    <!-- Powder clump sitting on bottom -->
                    <ellipse cx="55" cy="114" rx="20" ry="4" fill="#f8fafc"/>
                `}
            </svg>
        `;
    }
}

function stirSim13() {
    renderSim13Graphic(true);
}

// -------------------------------------------------------------
// Simulator 14: Liquid Stratification & ORS Formulator
// -------------------------------------------------------------
let sim14Mode = 'miscible';
let sim14Sugar = 0;
let sim14Salt = 0;

function setSim14Mode(mode) {
    sim14Mode = mode;
    const btnM = document.getElementById('sim14Mode-miscible');
    const btnO = document.getElementById('sim14Mode-ors');
    if (btnM) btnM.className = (mode === 'miscible') ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    if (btnO) btnO.className = (mode === 'ors') ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    renderSim14();
}

function renderSim14() {
    const ws = document.getElementById('sim14Workspace');
    const ctrl = document.getElementById('sim14Controls');
    const fb = document.getElementById('sim14Feedback');

    if (sim14Mode === 'miscible') {
        if (ws) {
            ws.innerHTML = `
                <!-- Test Tube 1: Water + Vinegar -->
                <div class="flex flex-col items-center">
                    <div class="w-10 h-28 border-2 border-slate-600 bg-cyan-500/20 rounded-b-xl flex items-center justify-center relative overflow-hidden">
                        <span class="text-[8px] text-cyan-300 font-bold rotate-90">Uniform Solution</span>
                    </div>
                    <span class="text-[10px] text-emerald-400 font-bold mt-1">Water + Vinegar</span>
                    <span class="text-[9px] text-slate-400">Miscible (1 Phase)</span>
                </div>

                <!-- Test Tube 2: Water + Oil -->
                <div class="flex flex-col items-center">
                    <div class="w-10 h-28 border-2 border-slate-600 rounded-b-xl flex flex-col justify-between overflow-hidden">
                        <div class="h-10 bg-amber-500/80 flex items-center justify-center text-[7px] font-bold text-slate-900 border-b border-amber-600">Oil Layer</div>
                        <div class="h-18 bg-cyan-500/30 flex items-center justify-center text-[7px] font-bold text-cyan-300">Water Layer</div>
                    </div>
                    <span class="text-[10px] text-rose-400 font-bold mt-1">Water + Mustard Oil</span>
                    <span class="text-[9px] text-slate-400">Immiscible (2 Layers)</span>
                </div>
            `;
        }
        if (ctrl) {
            ctrl.innerHTML = `
                <div class="flex justify-between items-center text-xs">
                    <span class="text-slate-300">Density & Polarity Rule: Oil is non-polar and less dense, floating on top.</span>
                </div>
            `;
        }
        if (fb) fb.innerHTML = "Vinegar and water form hydrogen bonds and mix completely. Oil and water refuse to mix and stratify into two distinct layers.";
    } else {
        if (ws) {
            ws.innerHTML = `
                <div class="flex items-center justify-around w-full">
                    <div class="flex flex-col items-center">
                        <span class="text-2xl">💧</span>
                        <span class="text-[10px] font-bold text-white">1 Litre Clean Water</span>
                    </div>
                    <div class="space-y-1 text-center">
                        <span class="text-xs text-amber-300 font-mono font-bold block">Sugar: ${sim14Sugar} / 6 Spoons</span>
                        <span class="text-xs text-cyan-300 font-mono font-bold block">Salt: ${sim14Salt} / 0.5 Spoon</span>
                    </div>
                    <div id="orsStatus" class="p-2 rounded-lg bg-slate-800 border border-slate-700 text-center">
                        <span class="text-[10px] text-slate-400 block">Formulation:</span>
                        <span class="text-xs font-bold ${sim14Sugar === 6 && sim14Salt === 0.5 ? 'text-emerald-400' : 'text-amber-400'}">${sim14Sugar === 6 && sim14Salt === 0.5 ? 'Perfect Life-Saving ORS! ✅' : 'Incomplete Ratio'}</span>
                    </div>
                </div>
            `;
        }
        if (ctrl) {
            ctrl.innerHTML = `
                <div class="flex space-x-2">
                    <button onclick="addSim14ORS('sugar')" class="flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs">+1 Spoon Sugar</button>
                    <button onclick="addSim14ORS('salt')" class="flex-1 py-1.5 rounded-lg bg-cyan-600 text-white font-bold text-xs">+0.5 Spoon Salt</button>
                    <button onclick="resetSim14ORS()" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 text-xs">Reset</button>
                </div>
            `;
        }
        if (fb) fb.innerHTML = "Life-saving ORS recipe: 1 Litre boiled & cooled clean water + 6 level teaspoons sugar + 1/2 level teaspoon table salt.";
    }
}

function addSim14ORS(type) {
    if (type === 'sugar' && sim14Sugar < 6) sim14Sugar++;
    if (type === 'salt' && sim14Salt < 0.5) sim14Salt += 0.5;
    renderSim14();
}

function resetSim14ORS() {
    sim14Sugar = 0;
    sim14Salt = 0;
    renderSim14();
}

// -------------------------------------------------------------
// Simulator 15: Dual-Pan Balance & Water Displacement Lab
// -------------------------------------------------------------
let sim15Tool = 'balance';
function setSim15Tool(tool) {
    sim15Tool = tool;
    const btnB = document.getElementById('sim15Tool-balance');
    const btnV = document.getElementById('sim15Tool-volume');
    if (btnB) btnB.className = (tool === 'balance') ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    if (btnV) btnV.className = (tool === 'volume') ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    renderSim15();
}

function renderSim15() {
    const stage = document.getElementById('sim15Stage');
    const ctrl = document.getElementById('sim15Controls');
    const ins = document.getElementById('sim15Insight');

    if (sim15Tool === 'balance') {
        if (stage) {
            stage.innerHTML = `
                <div class="flex flex-col items-center">
                    <!-- Dual-Pan Balance Graphic -->
                    <svg width="240" height="110" viewBox="0 0 240 110">
                        <!-- Central Pillar -->
                        <rect x="115" y="20" width="10" height="70" fill="#64748b"/>
                        <polygon points="120,90 90,105 150,105" fill="#475569"/>
                        <!-- Beam (Tilted toward right sand pan) -->
                        <line id="sim15Beam" x1="40" y1="35" x2="200" y2="45" stroke="#cbd5e1" stroke-width="4"/>
                        <circle cx="120" cy="40" r="4" fill="#38bdf8"/>
                        <!-- Left Pan (Cotton) -->
                        <line x1="40" y1="35" x2="40" y2="60" stroke="#94a3b8" stroke-width="1.5"/>
                        <ellipse cx="40" cy="65" rx="20" ry="4" fill="#475569"/>
                        <circle cx="40" cy="58" r="8" fill="#f8fafc"/>
                        <text x="40" y="80" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Cotton (10 g)</text>
                        <!-- Right Pan (Sand) -->
                        <line x1="200" y1="45" x2="200" y2="75" stroke="#94a3b8" stroke-width="1.5"/>
                        <ellipse cx="200" cy="80" rx="20" ry="4" fill="#475569"/>
                        <circle cx="200" cy="73" r="8" fill="#b45309"/>
                        <text x="200" y="95" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">Sand (200 g)</text>
                    </svg>
                </div>
            `;
        }
        if (ctrl) {
            ctrl.innerHTML = `
                <span class="text-xs font-bold text-amber-300">Equal Volume Cups (100 mL each)</span>
                <span class="text-xs font-mono text-emerald-400">Mass: Sand (200 g) &gt; Cotton (10 g)</span>
            `;
        }
        if (ins) ins.innerHTML = "Even though both cups have an identical volume of 100 mL, the sand cup contains 20 times more mass because sand particles are densely packed.";
    } else {
        if (stage) {
            stage.innerHTML = `
                <div class="flex items-center justify-around w-full">
                    <!-- Graduated Cylinder -->
                    <div class="flex items-center space-x-4">
                        <svg width="80" height="120" viewBox="0 0 80 120">
                            <rect x="25" y="10" width="30" height="100" rx="3" fill="none" stroke="#64748b" stroke-width="2"/>
                            <!-- Water Column -->
                            <rect id="sim15WaterCol" x="27" y="60" width="26" height="48" fill="rgba(56, 189, 248, 0.4)"/>
                            <line id="sim15Meniscus" x1="27" y1="60" x2="53" y2="60" stroke="#38bdf8" stroke-width="2"/>
                            <!-- Markings -->
                            <line x1="50" y1="35" x2="55" y2="35" stroke="#cbd5e1" stroke-width="1"/>
                            <text x="58" y="38" fill="#cbd5e1" font-size="7">75 mL</text>
                            <line x1="50" y1="60" x2="55" y2="60" stroke="#cbd5e1" stroke-width="1"/>
                            <text x="58" y="63" fill="#cbd5e1" font-size="7">50 mL</text>
                            <!-- Stone Pebble -->
                            <circle id="sim15Stone" cx="40" cy="95" r="7" fill="#64748b" opacity="0"/>
                        </svg>
                        <div class="space-y-1 text-xs">
                            <div class="text-slate-300">Initial Water = <span class="font-bold text-white">50 mL</span></div>
                            <div class="text-slate-300">Final Water = <span id="sim15FinalVol" class="font-bold text-cyan-400">50 mL</span></div>
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800 text-emerald-400 font-bold">
                                Stone Volume = <span id="sim15DiffVol">0 mL</span>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }
        if (ctrl) {
            ctrl.innerHTML = `
                <button onclick="submergeSim15Stone()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-lg transition">
                    🪨 Submerge Stone in Water
                </button>
                <button onclick="resetSim15Stone()" class="text-xs text-slate-400 hover:text-white underline">Reset</button>
            `;
        }
        if (ins) ins.innerHTML = "Water displacement principle: Submerging an irregular object displaces a water volume exactly equal to the object's three-dimensional space.";
    }
}

function submergeSim15Stone() {
    const col = document.getElementById('sim15WaterCol');
    const men = document.getElementById('sim15Meniscus');
    const stone = document.getElementById('sim15Stone');
    const fv = document.getElementById('sim15FinalVol');
    const dv = document.getElementById('sim15DiffVol');

    if (stone) stone.style.opacity = '1';
    if (col) { col.setAttribute('y', '35'); col.setAttribute('height', '73'); }
    if (men) { men.setAttribute('y1', '35'); men.setAttribute('y2', '35'); }
    if (fv) fv.textContent = '75 mL';
    if (dv) dv.textContent = '25 mL (25 cm³)';
}

function resetSim15Stone() {
    const col = document.getElementById('sim15WaterCol');
    const men = document.getElementById('sim15Meniscus');
    const stone = document.getElementById('sim15Stone');
    const fv = document.getElementById('sim15FinalVol');
    const dv = document.getElementById('sim15DiffVol');

    if (stone) stone.style.opacity = '0';
    if (col) { col.setAttribute('y', '60'); col.setAttribute('height', '48'); }
    if (men) { men.setAttribute('y1', '60'); men.setAttribute('y2', '60'); }
    if (fv) fv.textContent = '50 mL';
    if (dv) dv.textContent = '0 mL';
}

// -------------------------------------------------------------
// Simulator 16: Matter Classifier & Ayurvedic Gunas Matrix
// -------------------------------------------------------------
let sim16Tab = 'matter';
const sim16Items = [
    { name: "Pebble 🪨", matter: true },
    { name: "Sunlight ☀️", matter: false },
    { name: "Water 💧", matter: true },
    { name: "Bird Chirp 🎶", matter: false },
    { name: "Air Balloon 🎈", matter: true },
    { name: "Shadow 👤", matter: false }
];
let sim16Results = {};

const sim16Gunas = [
    { sanskrit: "Guru / Laghu", english: "Heavy vs Light" },
    { sanskrit: "Sheeta / Ushna", english: "Cold vs Hot" },
    { sanskrit: "Snigdha / Ruksha", english: "Oily vs Dry" },
    { sanskrit: "Mridu / Kathina", english: "Soft vs Hard" },
    { sanskrit: "Sthira / Sara", english: "Stable vs Mobile" }
];

function setSim16Tab(tab) {
    sim16Tab = tab;
    const btnM = document.getElementById('sim16Tab-matter');
    const btnG = document.getElementById('sim16Tab-gunas');
    if (btnM) btnM.className = (tab === 'matter') ? 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    if (btnG) btnG.className = (tab === 'gunas') ? 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white';
    renderSim16();
}

function renderSim16() {
    const ws = document.getElementById('sim16Workspace');
    const bb = document.getElementById('sim16BottomBar');

    if (sim16Tab === 'matter') {
        if (ws) {
            ws.innerHTML = `
                <div class="grid grid-cols-2 gap-2">
                    ${sim16Items.map((it, idx) => `
                        <div class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between text-xs">
                            <span class="font-bold text-white">${it.name}</span>
                            <div class="space-x-1">
                                <button onclick="checkSim16Matter(${idx}, true)" class="px-2 py-0.5 rounded text-[10px] font-bold ${sim16Results[idx] === 'correct' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">Matter</button>
                                <button onclick="checkSim16Matter(${idx}, false)" class="px-2 py-0.5 rounded text-[10px] font-bold ${sim16Results[idx] === 'correct-energy' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">Energy / Idea</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
            `;
        }
        if (bb) {
            bb.innerHTML = `
                <span class="text-slate-400">Classify all items: Does it have mass and occupy volume?</span>
            `;
        }
    } else {
        if (ws) {
            ws.innerHTML = `
                <div class="space-y-1.5">
                    <span class="text-[11px] font-bold text-amber-300 block">Ashtanga Hridaya: 20 Fundamental Physical Gunas (10 Dual Pairs)</span>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                        ${sim16Gunas.map(g => `
                            <div class="p-2 rounded bg-slate-900/90 border border-slate-800 flex items-center justify-between">
                                <span class="font-mono font-bold text-emerald-400">${g.sanskrit}</span>
                                <span class="text-slate-300 text-[11px]">${g.english}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }
        if (bb) {
            bb.innerHTML = `
                <span class="text-amber-300 italic">Ancient Indian medical taxonomy anticipated binary physical categorization.</span>
            `;
        }
    }
}

function checkSim16Matter(idx, chosenMatter) {
    const item = sim16Items[idx];
    if (item.matter === chosenMatter) {
        sim16Results[idx] = chosenMatter ? 'correct' : 'correct-energy';
    } else {
        alert(`${item.name} is ${item.matter ? 'MATTER (it has mass and occupies space!)' : 'NOT matter (it is a form of energy or absence of light without mass/volume).'}`);
    }
    renderSim16();
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    selectSim1Object('pen');
    setSim2Stage('raw');
    setSim3Material('glass');
    setSim4Tree('wood');
    resetSim5();
    renderSim6();
    renderSim7Graphic(false);
    setSim8Material('gold');
    setSim9Sample('sponge');
    setSim10Medium('glass');
    setSim11Blocker('cardboard');
    setSim12Material('butter');
    setSim13Solute('sugar');
    renderSim14();
    renderSim15();
    renderSim16();

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''


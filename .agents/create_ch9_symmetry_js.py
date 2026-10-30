import re

js_code = r'''
// Symmetry Chapter Interactive JavaScript
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
        feedbackEl.innerHTML = `<strong>Try again:</strong> That option is not quite right. Review the geometric properties above!`;
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
// Simulator 1: Nature's Balance
// -------------------------------------------------------------
const sim1Data = {
    butterfly: {
        title: "Monarch Butterfly (Bilateral Symmetry)",
        desc: "The butterfly exhibits bilateral symmetry. A single vertical line down the body divides it into exact mirror left and right wings.",
        symText: "1 Vertical Line of Symmetry • 0 Rotational Symmetry",
        svg: `<svg viewBox="0 0 300 240" class="w-full h-56 mx-auto">
            <line x1="150" y1="20" x2="150" y2="220" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4" />
            <!-- Left Wing -->
            <path d="M150,70 Q70,20 40,80 Q20,130 90,160 Q130,170 150,130 Z" fill="#f97316" fill-opacity="0.75" stroke="#ea580c" stroke-width="2"/>
            <path d="M150,130 Q80,160 70,190 Q90,220 130,200 Q145,180 150,150 Z" fill="#fb923c" fill-opacity="0.7" stroke="#ea580c" stroke-width="2"/>
            <!-- Right Wing (Mirrored) -->
            <path d="M150,70 Q230,20 260,80 Q280,130 210,160 Q170,170 150,130 Z" fill="#f97316" fill-opacity="0.75" stroke="#ea580c" stroke-width="2"/>
            <path d="M150,130 Q220,160 230,190 Q210,220 170,200 Q155,180 150,150 Z" fill="#fb923c" fill-opacity="0.7" stroke="#ea580c" stroke-width="2"/>
            <!-- Body -->
            <ellipse cx="150" cy="110" rx="8" ry="45" fill="#1e293b" stroke="#f8fafc" stroke-width="1.5"/>
            <circle cx="150" cy="60" r="10" fill="#1e293b" stroke="#f8fafc" stroke-width="1.5"/>
            <!-- Antennae -->
            <path d="M148,52 Q130,30 120,35" stroke="#f8fafc" stroke-width="2" fill="none"/>
            <path d="M152,52 Q170,30 180,35" stroke="#f8fafc" stroke-width="2" fill="none"/>
            <text x="150" y="235" fill="#f59e0b" font-size="12" text-anchor="middle" font-weight="bold">Axis of Symmetry</text>
        </svg>`
    },
    flower: {
        title: "5-Petal Flower (Radial & Reflectional)",
        desc: "Each petal is spaced at 72° (360° ÷ 5). It possesses 5 lines of symmetry and rotational symmetry of order 5.",
        symText: "5 Lines of Symmetry • Rotational Order 5 (72° angle)",
        svg: `<svg viewBox="0 0 300 240" class="w-full h-56 mx-auto">
            <g transform="translate(150,120)">
                <!-- 5 Lines of symmetry -->
                <line x1="0" y1="-100" x2="0" y2="100" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" />
                <line x1="-95" y1="-31" x2="95" y2="31" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" />
                <line x1="-59" y1="81" x2="59" y2="-81" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" />
                <!-- Petals -->
                <circle cx="0" cy="-55" r="30" fill="#ec4899" fill-opacity="0.6" stroke="#db2777" stroke-width="2"/>
                <circle cx="52" cy="-17" r="30" fill="#ec4899" fill-opacity="0.6" stroke="#db2777" stroke-width="2"/>
                <circle cx="32" cy="45" r="30" fill="#ec4899" fill-opacity="0.6" stroke="#db2777" stroke-width="2"/>
                <circle cx="-32" cy="45" r="30" fill="#ec4899" fill-opacity="0.6" stroke="#db2777" stroke-width="2"/>
                <circle cx="-52" cy="-17" r="30" fill="#ec4899" fill-opacity="0.6" stroke="#db2777" stroke-width="2"/>
                <!-- Center Core -->
                <circle cx="0" cy="0" r="22" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
            </g>
        </svg>`
    },
    snowflake: {
        title: "Kepler's 6-Fold Snowflake",
        desc: "Johannes Kepler described how hexagonal ice crystals exhibit exact 6-fold radial symmetry with 6 lines of symmetry.",
        symText: "6 Lines of Symmetry • Rotational Order 6 (60° angle)",
        svg: `<svg viewBox="0 0 300 240" class="w-full h-56 mx-auto">
            <g transform="translate(150,120)" stroke="#67e8f9" stroke-width="2.5" stroke-linecap="round">
                <!-- 6 main branches -->
                <line x1="0" y1="-85" x2="0" y2="85" />
                <line x1="-73.6" y1="-42.5" x2="73.6" y2="42.5" />
                <line x1="-73.6" y1="42.5" x2="73.6" y2="-42.5" />
                <!-- Sub branches on vertical -->
                <path d="M-20,-50 L0,-65 L20,-50 M-20,50 L0,65 L20,50" fill="none"/>
                <path d="M-15,-30 L0,-40 L15,-30 M-15,30 L0,40 L15,30" fill="none"/>
                <!-- Center crystal -->
                <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" fill="#0891b2" fill-opacity="0.5" stroke="#a5f3fc" stroke-width="1.5"/>
            </g>
        </svg>`
    },
    tajmahal: {
        title: "Taj Mahal, Agra (Architectural Symmetry)",
        desc: "A worldwide masterclass in bilateral symmetry: the central dome, minarets, and arched iwans mirror perfectly across the vertical axis.",
        symText: "1 Vertical Line of Symmetry • Pure Bilateral Equilibrium",
        svg: `<svg viewBox="0 0 300 240" class="w-full h-56 mx-auto">
            <line x1="150" y1="10" x2="150" y2="230" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4" />
            <!-- Base Plinth -->
            <rect x="50" y="190" width="200" height="25" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
            <!-- Main Mausoleum Building -->
            <rect x="80" y="110" width="140" height="80" fill="#475569" stroke="#cbd5e1" stroke-width="1.5"/>
            <!-- Main Dome -->
            <path d="M120,110 C120,60 135,45 150,35 C165,45 180,60 180,110 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
            <!-- Finial -->
            <line x1="150" y1="35" x2="150" y2="15" stroke="#f59e0b" stroke-width="2"/>
            <!-- Side Chattris -->
            <path d="M90,110 C90,85 97,75 105,70 C113,75 120,85 120,110 Z" fill="#cbd5e1"/>
            <path d="M180,110 C180,85 187,75 195,70 C203,75 210,85 210,110 Z" fill="#cbd5e1"/>
            <!-- Central Arch -->
            <path d="M130,190 L130,140 Q150,120 170,140 L170,190 Z" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
            <!-- Left & Right Minarets -->
            <rect x="40" y="70" width="12" height="120" fill="#64748b"/>
            <rect x="248" y="70" width="12" height="120" fill="#64748b"/>
        </svg>`
    },
    cloud: {
        title: "Drifting Cumulus Cloud (Asymmetrical)",
        desc: "Unlike living flowers or engineered monuments, clouds form irregularly through turbulent air. No line of symmetry or rotational center exists.",
        symText: "0 Lines of Symmetry • 0 Rotational Symmetry (Asymmetric)",
        svg: `<svg viewBox="0 0 300 240" class="w-full h-56 mx-auto">
            <path d="M50,150 Q40,110 80,100 Q100,60 150,75 Q190,50 230,85 Q270,105 255,145 Q265,180 220,180 Q190,195 150,180 Q100,190 70,175 Q40,170 50,150 Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
            <text x="150" y="215" fill="#f87171" font-size="12" text-anchor="middle" font-weight="bold">No Mirror Line • Asymmetric</text>
        </svg>`
    }
};

function selectSim1(key) {
    const data = sim1Data[key];
    if (!data) return;
    document.getElementById('sim1-display').innerHTML = data.svg;
    document.getElementById('sim1-title').textContent = data.title;
    document.getElementById('sim1-desc').textContent = data.desc;
    document.getElementById('sim1-badge').textContent = data.symText;

    const btns = document.querySelectorAll('.sim1-btn');
    btns.forEach(b => {
        b.className = b.getAttribute('data-key') === key ?
            'sim1-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
            'sim1-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    });
}

// -------------------------------------------------------------
// Simulator 2: Line of Symmetry
// -------------------------------------------------------------
let sim2Folded = false;
let sim2Angle = 90;

function updateSim2() {
    const svg = document.getElementById('sim2-svg');
    const status = document.getElementById('sim2-status');
    const angle = parseInt(document.getElementById('sim2-angle').value, 10);
    sim2Angle = angle;
    document.getElementById('sim2-angle-val').textContent = `${angle}°`;

    const rad = (angle * Math.PI) / 180;
    const x1 = 150 - 110 * Math.cos(rad);
    const y1 = 120 - 110 * Math.sin(rad);
    const x2 = 150 + 110 * Math.cos(rad);
    const y2 = 120 + 110 * Math.sin(rad);

    let html = `
        <!-- Heart Shape -->
        <g id="sim2-shape">
            <path d="M150,190 C100,150 60,110 60,70 A45,45 0 0,1 150,70 A45,45 0 0,1 240,70 C240,110 200,150 150,190 Z" 
                  fill="${sim2Folded ? '#818cf8' : '#ec4899'}" fill-opacity="0.6" stroke="#db2777" stroke-width="2"/>
        </g>
        <!-- Cutting / Folding Line -->
        <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/>
        <circle cx="150" cy="120" r="4" fill="#38bdf8" />
    `;

    if (sim2Folded) {
        if (angle === 90) {
            html += `<text x="150" y="215" fill="#34d399" font-size="12" text-anchor="middle" font-weight="bold">Perfect Overlap! Exact Line of Symmetry</text>`;
            status.innerHTML = `<span class="text-emerald-400 font-semibold">Match!</span> At 90° (vertical), left half mirrors right half precisely. Both halves coincide completely.`;
        } else {
            html += `<text x="150" y="215" fill="#f87171" font-size="12" text-anchor="middle" font-weight="bold">Mismatch! Edges poke out</text>`;
            status.innerHTML = `<span class="text-rose-400 font-semibold">Does not coincide:</span> At ${angle}°, folding along this line causes parts to jut out. It is NOT a line of symmetry.`;
        }
    } else {
        status.textContent = `Adjust line angle and click "Fold Along Line" to test mirror overlap.`;
    }

    svg.innerHTML = html;
}

function toggleSim2Fold() {
    sim2Folded = !sim2Folded;
    const btn = document.getElementById('sim2-fold-btn');
    if (btn) btn.textContent = sim2Folded ? "Unfold Paper" : "Fold Along Line";
    updateSim2();
}

function resetSim2() {
    sim2Folded = false;
    document.getElementById('sim2-angle').value = 90;
    const btn = document.getElementById('sim2-fold-btn');
    if (btn) btn.textContent = "Fold Along Line";
    updateSim2();
}

// -------------------------------------------------------------
// Simulator 3: Squares vs Rectangles
// -------------------------------------------------------------
let sim3Shape = 'square';
let sim3Fold = 'none';

function setSim3Shape(shape) {
    sim3Shape = shape;
    sim3Fold = 'none';
    const sBtn = document.getElementById('sim3-btn-square');
    const rBtn = document.getElementById('sim3-btn-rect');
    if (shape === 'square') {
        sBtn.className = 'px-4 py-1.5 rounded-lg text-xs font-semibold bg-cyan-500 text-slate-950';
        rBtn.className = 'px-4 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300';
    } else {
        sBtn.className = 'px-4 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300';
        rBtn.className = 'px-4 py-1.5 rounded-lg text-xs font-semibold bg-cyan-500 text-slate-950';
    }
    renderSim3();
}

function setSim3Fold(fold) {
    sim3Fold = fold;
    renderSim3();
}

function renderSim3() {
    const svg = document.getElementById('sim3-svg');
    const status = document.getElementById('sim3-status');
    const isSquare = (sim3Shape === 'square');
    const w = isSquare ? 140 : 180;
    const h = isSquare ? 140 : 100;
    const x = 150 - w / 2;
    const y = 120 - h / 2;

    let lineSvg = '';
    let matchText = '';
    let isMatch = false;

    if (sim3Fold === 'v') {
        lineSvg = `<line x1="150" y1="${y - 15}" x2="150" y2="${y + h + 15}" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4"/>`;
        matchText = 'Vertical Fold: Left half exactly overlaps right half.';
        isMatch = true;
    } else if (sim3Fold === 'h') {
        lineSvg = `<line x1="${x - 15}" y1="120" x2="${x + w + 15}" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4"/>`;
        matchText = 'Horizontal Fold: Top half exactly overlaps bottom half.';
        isMatch = true;
    } else if (sim3Fold === 'd1') {
        lineSvg = `<line x1="${x - 10}" y1="${y - 10}" x2="${x + w + 10}" y2="${y + h + 10}" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5,4"/>`;
        if (isSquare) {
            matchText = 'Diagonal 1 (Square): Perfect overlap! Both triangular halves coincide.';
            isMatch = true;
        } else {
            matchText = 'Diagonal 1 (Rectangle): MISMATCH! Corners jut out into empty air. NOT a line of symmetry!';
            isMatch = false;
        }
    } else if (sim3Fold === 'd2') {
        lineSvg = `<line x1="${x + w + 10}" y1="${y - 10}" x2="${x - 10}" y2="${y + h + 10}" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5,4"/>`;
        if (isSquare) {
            matchText = 'Diagonal 2 (Square): Perfect overlap! All sides and angles align.';
            isMatch = true;
        } else {
            matchText = 'Diagonal 2 (Rectangle): MISMATCH! A non-square rectangle diagonal is NEVER a line of symmetry.';
            isMatch = false;
        }
    }

    svg.innerHTML = `
        <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#3b82f6" fill-opacity="0.25" stroke="#60a5fa" stroke-width="2" rx="4"/>
        <text x="150" y="${y + h / 2 + 5}" fill="#94a3b8" font-size="12" text-anchor="middle">${isSquare ? 'Square (4 Lines)' : 'Rectangle (2 Lines)'}</text>
        ${lineSvg}
    `;

    if (sim3Fold === 'none') {
        status.innerHTML = `<span class="text-slate-400">Click a fold line below to test mirror overlap.</span>`;
    } else if (isMatch) {
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Valid Axis of Symmetry:</span> ${matchText}`;
    } else {
        status.innerHTML = `<span class="text-rose-400 font-semibold">Invalid Fold:</span> ${matchText}`;
    }
}

// -------------------------------------------------------------
// Simulator 4: Polygons & Snowflakes
// -------------------------------------------------------------
function renderSim4() {
    const sides = parseInt(document.getElementById('sim4-sides').value, 10);
    const countEl = document.getElementById('sim4-sides-count');
    const badgeEl = document.getElementById('sim4-badge');
    const svg = document.getElementById('sim4-svg');

    countEl.textContent = `${sides} Sides`;
    badgeEl.textContent = `Lines of Symmetry: ${sides} • Rotational Order: ${sides}`;

    const r = 85;
    const cx = 150;
    const cy = 120;
    let pts = [];
    for (let i = 0; i < sides; i++) {
        const theta = (2 * Math.PI * i) / sides - Math.PI / 2;
        pts.push(`${cx + r * Math.cos(theta)},${cy + r * Math.sin(theta)}`);
    }

    let axesSvg = '';
    for (let i = 0; i < sides; i++) {
        const theta = (Math.PI * i) / sides - Math.PI / 2;
        const x1 = cx - (r + 15) * Math.cos(theta);
        const y1 = cy - (r + 15) * Math.sin(theta);
        const x2 = cx + (r + 15) * Math.cos(theta);
        const y2 = cy + (r + 15) * Math.sin(theta);
        axesSvg += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>`;
    }

    svg.innerHTML = `
        <polygon points="${pts.join(' ')}" fill="#6366f1" fill-opacity="0.3" stroke="#818cf8" stroke-width="2.5" />
        ${axesSvg}
        <circle cx="${cx}" cy="${cy}" r="3.5" fill="#f59e0b"/>
    `;
}

// -------------------------------------------------------------
// Simulator 5: Mirror Reflections
// -------------------------------------------------------------
let sim5Px = 90;
let sim5Py = 80;

function renderSim5() {
    const svg = document.getElementById('sim5-svg');
    const mirrorX = 150;
    const reflectedX = 2 * mirrorX - sim5Px;
    const dist = Math.abs(mirrorX - sim5Px);

    svg.innerHTML = `
        <!-- Mirror Line -->
        <line x1="${mirrorX}" y1="20" x2="${mirrorX}" y2="220" stroke="#38bdf8" stroke-width="3" />
        <text x="${mirrorX}" y="15" fill="#38bdf8" font-size="11" text-anchor="middle" font-weight="bold">Mirror Line M</text>
        
        <!-- Connecting Line PP' -->
        <line x1="${sim5Px}" y1="${sim5Py}" x2="${reflectedX}" y2="${sim5Py}" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
        
        <!-- Right Angle Marker -->
        <rect x="${mirrorX - 10}" y="${sim5Py - 10}" width="10" height="10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
        
        <!-- Point P -->
        <circle cx="${sim5Px}" cy="${sim5Py}" r="7" fill="#10b981" stroke="#ecfdf5" stroke-width="2" class="cursor-pointer"/>
        <text x="${sim5Px - 14}" y="${sim5Py - 10}" fill="#34d399" font-size="12" font-weight="bold">P (${sim5Px}, ${sim5Py})</text>
        
        <!-- Midpoint M0 -->
        <circle cx="${mirrorX}" cy="${sim5Py}" r="4" fill="#f59e0b"/>
        
        <!-- Point P' (Reflected) -->
        <circle cx="${reflectedX}" cy="${sim5Py}" r="7" fill="#a855f7" stroke="#faf5ff" stroke-width="2"/>
        <text x="${reflectedX + 14}" y="${sim5Py - 10}" fill="#c084fc" font-size="12" font-weight="bold">P' (${reflectedX}, ${sim5Py})</text>
        
        <!-- Distance Labels -->
        <text x="${(sim5Px + mirrorX) / 2}" y="${sim5Py + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">d = ${dist}px</text>
        <text x="${(reflectedX + mirrorX) / 2}" y="${sim5Py + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">d = ${dist}px</text>
    `;

    document.getElementById('sim5-info').textContent = `Distance PM = ${dist}px | Distance P'M = ${dist}px | Segment PP' ⟂ Mirror Line`;
}

function handleSim5Click(e) {
    const svg = document.getElementById('sim5-svg');
    const rect = svg.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;
    const scaleX = 300 / rect.width;
    const scaleY = 240 / rect.height;
    const svgX = Math.round(clickX * scaleX);
    const svgY = Math.round(clickY * scaleY);

    if (svgX < 140 && svgX > 20 && svgY > 30 && svgY < 210) {
        sim5Px = svgX;
        sim5Py = svgY;
        renderSim5();
    }
}

// -------------------------------------------------------------
// Simulator 6: Ink Blot Patterns
// -------------------------------------------------------------
let sim6Blots = [
    { x: 90, y: 70, r: 8, col: '#f43f5e' },
    { x: 120, y: 120, r: 12, col: '#06b6d4' },
    { x: 70, y: 150, r: 10, col: '#8b5cf6' }
];
let sim6Folded = false;

function renderSim6() {
    const svg = document.getElementById('sim6-svg');
    let blotSvg = '';

    sim6Blots.forEach(b => {
        blotSvg += `<circle cx="${b.x}" cy="${b.y}" r="${b.r}" fill="${b.col}" opacity="0.85"/>`;
        if (sim6Folded) {
            const rx = 300 - b.x;
            blotSvg += `<circle cx="${rx}" cy="${b.y}" r="${b.r}" fill="${b.col}" opacity="0.85"/>`;
        }
    });

    svg.innerHTML = `
        <!-- Paper Outline -->
        <rect x="20" y="20" width="260" height="200" fill="#1e293b" stroke="#475569" stroke-width="2" rx="6"/>
        <!-- Fold crease -->
        <line x1="150" y1="20" x2="150" y2="220" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,4"/>
        <text x="85" y="40" fill="#94a3b8" font-size="11" text-anchor="middle">Left Half (Drop Ink)</text>
        <text x="215" y="40" fill="#94a3b8" font-size="11" text-anchor="middle">Right Half</text>
        ${blotSvg}
    `;

    const status = document.getElementById('sim6-status');
    if (sim6Folded) {
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Crease Unfolded:</span> Symmetrical twin blots created! The crease is the perpendicular bisector between each original and mirrored blot.`;
    } else {
        status.innerHTML = `<span class="text-slate-400">Click on left paper half to add ink drops, then fold.</span>`;
    }
}

function handleSim6Click(e) {
    if (sim6Folded) return;
    const svg = document.getElementById('sim6-svg');
    const rect = svg.getBoundingClientRect();
    const clickX = (e.clientX - rect.left) * (300 / rect.width);
    const clickY = (e.clientY - rect.top) * (240 / rect.height);

    if (clickX >= 35 && clickX <= 140 && clickY >= 35 && clickY <= 205) {
        const colors = ['#f43f5e', '#06b6d4', '#8b5cf6', '#10b981', '#f59e0b', '#ec4899'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        const r = Math.floor(Math.random() * 8) + 6;
        sim6Blots.push({ x: Math.round(clickX), y: Math.round(clickY), r, col: randomColor });
        renderSim6();
    }
}

function toggleSim6Fold() {
    sim6Folded = !sim6Folded;
    const btn = document.getElementById('sim6-fold-btn');
    if (btn) btn.textContent = sim6Folded ? "Clear & Reset Paper" : "Fold & Press Paper";
    if (!sim6Folded) {
        sim6Blots = [];
    }
    renderSim6();
}

// -------------------------------------------------------------
// Simulator 7: Paper Folding & Cuts
// -------------------------------------------------------------
let sim7Folds = 2; // 1, 2, 4
let sim7Cut = 'triangle';
let sim7Unfolded = false;

function setSim7Folds(n) {
    sim7Folds = n;
    sim7Unfolded = false;
    renderSim7();
}

function setSim7Cut(shape) {
    sim7Cut = shape;
    sim7Unfolded = false;
    renderSim7();
}

function toggleSim7Unfold() {
    sim7Unfolded = !sim7Unfolded;
    const btn = document.getElementById('sim7-btn-unfold');
    if (btn) btn.textContent = sim7Unfolded ? "Fold Again" : "Unfold Paper";
    renderSim7();
}

function renderSim7() {
    const svg = document.getElementById('sim7-svg');
    const status = document.getElementById('sim7-status');

    let cutCount = sim7Folds === 1 ? 2 : (sim7Folds === 2 ? 4 : 8);

    if (!sim7Unfolded) {
        svg.innerHTML = `
            <rect x="75" y="45" width="150" height="150" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
            <text x="150" y="115" fill="#f8fafc" font-size="12" text-anchor="middle">Folded Sheet (${sim7Folds} Folds)</text>
            <polygon points="150,45 165,70 135,70" fill="#ef4444"/>
            <text x="150" y="85" fill="#fca5a5" font-size="10" text-anchor="middle">Notch Cut</text>
        `;
        status.textContent = `Paper folded with ${sim7Folds} fold(s). Click "Unfold Paper" to observe symmetrical cut-outs.`;
    } else {
        let cutsSvg = '';
        if (cutCount === 2) {
            cutsSvg = `<polygon points="150,45 160,65 140,65" fill="#ef4444"/><polygon points="150,195 160,175 140,175" fill="#ef4444"/>`;
        } else if (cutCount === 4) {
            cutsSvg = `
                <polygon points="150,45 160,65 140,65" fill="#ef4444"/>
                <polygon points="150,195 160,175 140,175" fill="#ef4444"/>
                <polygon points="75,120 95,110 95,130" fill="#ef4444"/>
                <polygon points="225,120 205,110 205,130" fill="#ef4444"/>
            `;
        } else {
            cutsSvg = `
                <polygon points="150,45 160,65 140,65" fill="#ef4444"/>
                <polygon points="150,195 160,175 140,175" fill="#ef4444"/>
                <polygon points="75,120 95,110 95,130" fill="#ef4444"/>
                <polygon points="225,120 205,110 205,130" fill="#ef4444"/>
                <circle cx="100" cy="70" r="10" fill="#ef4444"/>
                <circle cx="200" cy="70" r="10" fill="#ef4444"/>
                <circle cx="100" cy="170" r="10" fill="#ef4444"/>
                <circle cx="200" cy="170" r="10" fill="#ef4444"/>
            `;
        }
        svg.innerHTML = `
            <rect x="75" y="45" width="150" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <line x1="150" y1="45" x2="150" y2="195" stroke="#94a3b8" stroke-dasharray="4,4"/>
            <line x1="75" y1="120" x2="225" y2="120" stroke="#94a3b8" stroke-dasharray="4,4"/>
            ${cutsSvg}
        `;
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Kirigami Pattern:</span> ${cutCount} identical cut-outs generated! Each fold crease acts as an axis of mirror symmetry.`;
    }
}

// -------------------------------------------------------------
// Simulator 8: The Punching Game
// -------------------------------------------------------------
let sim8Holes = [{ x: 105, y: 95 }];
let sim8Unfolded = false;

function renderSim8() {
    const svg = document.getElementById('sim8-svg');
    const status = document.getElementById('sim8-status');

    let holesSvg = '';
    sim8Holes.forEach(h => {
        holesSvg += `<circle cx="${h.x}" cy="${h.y}" r="6" fill="#f43f5e" stroke="#fff" stroke-width="1.5"/>`;
        if (sim8Unfolded) {
            const mirroredX = 300 - h.x;
            holesSvg += `<circle cx="${mirroredX}" cy="${h.y}" r="6" fill="#f43f5e" stroke="#fff" stroke-width="1.5"/>`;
            holesSvg += `<line x1="${h.x}" y1="${h.y}" x2="${mirroredX}" y2="${h.y}" stroke="#94a3b8" stroke-dasharray="3,3"/>`;
        }
    });

    svg.innerHTML = `
        <rect x="30" y="30" width="240" height="180" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="4"/>
        <line x1="150" y1="30" x2="150" y2="210" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,4"/>
        <text x="150" y="25" fill="#38bdf8" font-size="11" text-anchor="middle">Fold Line (Crease)</text>
        ${holesSvg}
    `;

    if (sim8Unfolded) {
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Unfolded:</span> For every punch hole, its partner appears symmetrically across the crease. The crease is the perpendicular bisector between paired holes!`;
    } else {
        status.innerHTML = `<span class="text-slate-400">Click on left paper half to punch a hole, then click Unfold.</span>`;
    }
}

function handleSim8Click(e) {
    if (sim8Unfolded) return;
    const svg = document.getElementById('sim8-svg');
    const rect = svg.getBoundingClientRect();
    const clickX = (e.clientX - rect.left) * (300 / rect.width);
    const clickY = (e.clientY - rect.top) * (240 / rect.height);

    if (clickX >= 40 && clickX <= 140 && clickY >= 40 && clickY <= 200) {
        sim8Holes.push({ x: Math.round(clickX), y: Math.round(clickY) });
        renderSim8();
    }
}

function toggleSim8Unfold() {
    sim8Unfolded = !sim8Unfolded;
    const btn = document.getElementById('sim8-btn-unfold');
    if (btn) btn.textContent = sim8Unfolded ? "Reset Punch" : "Unfold Paper";
    if (!sim8Unfolded) {
        sim8Holes = [{ x: 105, y: 95 }];
    }
    renderSim8();
}

// -------------------------------------------------------------
// Simulator 9: Rotational Center
// -------------------------------------------------------------
function renderSim9() {
    const angle = parseInt(document.getElementById('sim9-angle').value, 10);
    document.getElementById('sim9-angle-val').textContent = `${angle}°`;
    const showCenter = document.getElementById('sim9-center-check').checked;
    const svg = document.getElementById('sim9-svg');

    svg.innerHTML = `
        <!-- Reference Ghost -->
        <g transform="translate(150,120)" opacity="0.2">
            <path d="M0,0 L0,-65 L25,-40 Z" fill="#64748b"/>
            <path d="M0,0 L65,0 L40,25 Z" fill="#64748b"/>
            <path d="M0,0 L0,65 L-25,40 Z" fill="#64748b"/>
            <path d="M0,0 L-65,0 L-40,-25 Z" fill="#64748b"/>
        </g>
        <!-- Rotating Pinwheel -->
        <g transform="translate(150,120) rotate(${angle})">
            <path d="M0,0 L0,-65 L25,-40 Z" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
            <path d="M0,0 L65,0 L40,25 Z" fill="#3b82f6" stroke="#93c5fd" stroke-width="1.5"/>
            <path d="M0,0 L0,65 L-25,40 Z" fill="#10b981" stroke="#86efac" stroke-width="1.5"/>
            <path d="M0,0 L-65,0 L-40,-25 Z" fill="#f59e0b" stroke="#fde68a" stroke-width="1.5"/>
        </g>
        ${showCenter ? '<circle cx="150" cy="120" r="6" fill="#f8fafc" stroke="#dc2626" stroke-width="2"/><text x="150" y="140" fill="#f8fafc" font-size="11" text-anchor="middle" font-weight="bold">Center of Rotation (Fixed Point)</text>' : ''}
    `;

    const status = document.getElementById('sim9-status');
    if (angle % 90 === 0) {
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Perfect Alignment (${angle}°):</span> The pinwheel coincides exactly with its original footprint!`;
    } else {
        status.innerHTML = `<span class="text-slate-400">Rotated by ${angle}°. Notice that the fixed center point never changes position during rotation.</span>`;
    }
}

// -------------------------------------------------------------
// Simulator 10: Angle of Symmetry
// -------------------------------------------------------------
let sim10Shape = 'square'; // tri, square, pent, hex

function setSim10Shape(shape) {
    sim10Shape = shape;
    document.getElementById('sim10-angle').value = 0;
    renderSim10();
}

function renderSim10() {
    const angle = parseInt(document.getElementById('sim10-angle').value, 10);
    document.getElementById('sim10-angle-val').textContent = `${angle}°`;
    const svg = document.getElementById('sim10-svg');
    const status = document.getElementById('sim10-status');

    let sides = 4;
    let symAngle = 90;
    if (sim10Shape === 'tri') { sides = 3; symAngle = 120; }
    else if (sim10Shape === 'square') { sides = 4; symAngle = 90; }
    else if (sim10Shape === 'pent') { sides = 5; symAngle = 72; }
    else if (sim10Shape === 'hex') { sides = 6; symAngle = 60; }

    const r = 70;
    let pts = [];
    for (let i = 0; i < sides; i++) {
        const theta = (2 * Math.PI * i) / sides - Math.PI / 2;
        pts.push(`${r * Math.cos(theta)},${r * Math.sin(theta)}`);
    }
    const ptStr = pts.join(' ');

    const isMatch = (angle % symAngle === 0);

    svg.innerHTML = `
        <!-- Ghost Original Outline -->
        <g transform="translate(150,120)" opacity="0.3">
            <polygon points="${ptStr}" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4"/>
        </g>
        <!-- Rotated Polygon -->
        <g transform="translate(150,120) rotate(${angle})">
            <polygon points="${ptStr}" fill="#8b5cf6" fill-opacity="0.5" stroke="#a78bfa" stroke-width="2.5"/>
            <!-- Top vertex marker to track spin -->
            <circle cx="0" cy="${-r}" r="5" fill="#f59e0b"/>
        </g>
        <circle cx="150" cy="120" r="4" fill="#f8fafc"/>
    `;

    if (isMatch && angle > 0) {
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Coincidence Match (${angle}°)!</span> Matches initial shape. Smallest non-zero angle = ${symAngle}°. Order = 360° ÷ ${symAngle}° = ${360 / symAngle}.`;
    } else if (angle === 0) {
        status.innerHTML = `<span class="text-slate-400">At 0° (Starting position). Drag slider to find angles where the shape looks identical.</span>`;
    } else {
        status.innerHTML = `<span class="text-slate-400">Rotated ${angle}°. Not currently matching original orientation. (Next match at ${Math.ceil(angle / symAngle) * symAngle}°).</span>`;
    }
}

// -------------------------------------------------------------
// Simulator 11: Radial Windmills
// -------------------------------------------------------------
let sim11Blades = 4;
let sim11SpinAngle = 0;
let sim11Interval = null;

function setSim11Blades(n) {
    sim11Blades = n;
    renderSim11();
}

function renderSim11() {
    const svg = document.getElementById('sim11-svg');
    const badge = document.getElementById('sim11-badge');
    const symAngle = 360 / sim11Blades;
    badge.textContent = `Blades: ${sim11Blades} • Angle of Rotation: 360° ÷ ${sim11Blades} = ${symAngle}° • Order: ${sim11Blades}`;

    let bladesSvg = '';
    const r = 70;
    for (let i = 0; i < sim11Blades; i++) {
        const deg = (360 / sim11Blades) * i;
        bladesSvg += `
            <g transform="rotate(${deg})">
                <path d="M0,0 Q-15,-35 0,-${r} Q15,-35 0,0" fill="#06b6d4" fill-opacity="0.7" stroke="#22d3ee" stroke-width="1.5"/>
                <circle cx="0" cy="-${r}" r="4" fill="#f59e0b"/>
            </g>
        `;
    }

    svg.innerHTML = `
        <g transform="translate(150,120) rotate(${sim11SpinAngle})">
            ${bladesSvg}
            <circle cx="0" cy="0" r="8" fill="#1e293b" stroke="#f8fafc" stroke-width="2"/>
        </g>
    `;
}

function toggleSim11Spin() {
    const btn = document.getElementById('sim11-spin-btn');
    if (sim11Interval) {
        clearInterval(sim11Interval);
        sim11Interval = null;
        if (btn) btn.textContent = "Start Spin";
    } else {
        sim11Interval = setInterval(() => {
            sim11SpinAngle = (sim11SpinAngle + 3) % 360;
            renderSim11();
        }, 30);
        if (btn) btn.textContent = "Stop Spin";
    }
}

// -------------------------------------------------------------
// Simulator 12: Order of Rotation
// -------------------------------------------------------------
let sim12Shape = 'square';
let sim12Step = 0;

function setSim12Shape(shape) {
    sim12Shape = shape;
    sim12Step = 0;
    renderSim12();
}

function nextSim12Step() {
    const maxSteps = (sim12Shape === 'tri') ? 3 : (sim12Shape === 'square' ? 4 : (sim12Shape === 'rect' ? 2 : 6));
    sim12Step = (sim12Step + 1) % (maxSteps + 1);
    renderSim12();
}

function renderSim12() {
    const svg = document.getElementById('sim12-svg');
    const info = document.getElementById('sim12-info');
    let maxSteps = 4;
    let stepAngle = 90;

    if (sim12Shape === 'tri') { maxSteps = 3; stepAngle = 120; }
    else if (sim12Shape === 'rect') { maxSteps = 2; stepAngle = 180; }
    else if (sim12Shape === 'square') { maxSteps = 4; stepAngle = 90; }
    else if (sim12Shape === 'hex') { maxSteps = 6; stepAngle = 60; }

    const curAngle = sim12Step * stepAngle;
    const r = 65;

    let shapeSvg = '';
    if (sim12Shape === 'rect') {
        shapeSvg = `<rect x="-65" y="-35" width="130" height="70" rx="4" fill="#ec4899" fill-opacity="0.4" stroke="#f472b6" stroke-width="2"/>`;
    } else {
        let pts = [];
        for (let i = 0; i < maxSteps; i++) {
            const th = (2 * Math.PI * i) / maxSteps - Math.PI / 2;
            pts.push(`${r * Math.cos(th)},${r * Math.sin(th)}`);
        }
        shapeSvg = `<polygon points="${pts.join(' ')}" fill="#8b5cf6" fill-opacity="0.4" stroke="#a78bfa" stroke-width="2"/>`;
    }

    svg.innerHTML = `
        <g transform="translate(150,120) rotate(${curAngle})">
            ${shapeSvg}
            <circle cx="0" cy="-45" r="5" fill="#f59e0b"/>
            <text x="0" y="-55" fill="#f59e0b" font-size="10" text-anchor="middle" font-weight="bold">Vertex A</text>
        </g>
        <circle cx="150" cy="120" r="4" fill="#f8fafc"/>
    `;

    info.innerHTML = `Rotation: <strong>${curAngle}°</strong> (Step ${sim12Step} of ${maxSteps}) | Matches Found in 360° turn: <strong>${sim12Step === 0 ? 1 : sim12Step}</strong> / Total Order = <strong>${maxSteps}</strong>`;
}

// -------------------------------------------------------------
// Simulator 13: Symmetries of a Circle
// -------------------------------------------------------------
let sim13Diameters = 6;
let sim13Angle = 0;
let sim13Spinning = false;
let sim13Interval = null;

function renderSim13() {
    const count = parseInt(document.getElementById('sim13-slider').value, 10);
    sim13Diameters = count;
    document.getElementById('sim13-count-val').textContent = `${count} Lines`;

    const svg = document.getElementById('sim13-svg');
    const r = 80;
    let linesSvg = '';

    for (let i = 0; i < count; i++) {
        const rad = (Math.PI * i) / count;
        const x1 = 150 - r * Math.cos(rad);
        const y1 = 120 - r * Math.sin(rad);
        const x2 = 150 + r * Math.cos(rad);
        const y2 = 120 + r * Math.sin(rad);
        linesSvg += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>`;
    }

    svg.innerHTML = `
        <g transform="translate(150,120) rotate(${sim13Angle}) translate(-150,-120)">
            <circle cx="150" cy="120" r="${r}" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2.5"/>
            ${linesSvg}
            <circle cx="150" cy="${120 - r}" r="4" fill="#f59e0b"/>
        </g>
        <circle cx="150" cy="120" r="4" fill="#f8fafc"/>
    `;
}

function toggleSim13Spin() {
    const btn = document.getElementById('sim13-spin-btn');
    if (sim13Spinning) {
        clearInterval(sim13Interval);
        sim13Spinning = false;
        if (btn) btn.textContent = "Rotate Continuously";
    } else {
        sim13Interval = setInterval(() => {
            sim13Angle = (sim13Angle + 2) % 360;
            renderSim13();
        }, 30);
        sim13Spinning = true;
        if (btn) btn.textContent = "Pause Rotation";
    }
}

// -------------------------------------------------------------
// Simulator 14: Tile Symmetry Studio
// -------------------------------------------------------------
let sim14Mode = 4; // 1, 2, 4 axes

function setSim14Mode(mode) {
    sim14Mode = mode;
    renderSim14();
}

function renderSim14() {
    const svg = document.getElementById('sim14-svg');
    const badge = document.getElementById('sim14-badge');
    badge.textContent = `Tessellation Mode: ${sim14Mode} Symmetry Axes`;

    svg.innerHTML = `
        <rect x="50" y="20" width="200" height="200" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
        <!-- 4 Sub-tiles -->
        <g transform="translate(100,70)">
            <circle cx="-20" cy="-20" r="15" fill="#f43f5e" opacity="0.8"/>
            <path d="M-40,0 Q-20,20 0,0" fill="none" stroke="#38bdf8" stroke-width="2"/>
        </g>
        <g transform="translate(200,70) scale(-1, 1)">
            <circle cx="-20" cy="-20" r="15" fill="#f43f5e" opacity="0.8"/>
            <path d="M-40,0 Q-20,20 0,0" fill="none" stroke="#38bdf8" stroke-width="2"/>
        </g>
        <g transform="translate(100,170) scale(1, -1)">
            <circle cx="-20" cy="-20" r="15" fill="#f43f5e" opacity="0.8"/>
            <path d="M-40,0 Q-20,20 0,0" fill="none" stroke="#38bdf8" stroke-width="2"/>
        </g>
        <g transform="translate(200,170) scale(-1, -1)">
            <circle cx="-20" cy="-20" r="15" fill="#f43f5e" opacity="0.8"/>
            <path d="M-40,0 Q-20,20 0,0" fill="none" stroke="#38bdf8" stroke-width="2"/>
        </g>
        <!-- Division lines -->
        <line x1="150" y1="20" x2="150" y2="220" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
        <line x1="50" y1="120" x2="250" y2="120" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
    `;
}

// -------------------------------------------------------------
// Simulator 15: The Symmetry Grid Game (6x6)
// -------------------------------------------------------------
let sim15Grid = Array(6).fill(null).map(() => Array(6).fill(0)); // 0: empty, 1: P1, 2: P2
let sim15Moves = 0;

function renderSim15() {
    const container = document.getElementById('sim15-grid-board');
    if (!container) return;

    let html = '';
    for (let r = 0; r < 6; r++) {
        for (let c = 0; c < 6; c++) {
            const val = sim15Grid[r][c];
            let cellContent = '';
            if (val === 1) {
                cellContent = '<div class="w-6 h-6 rounded-full bg-emerald-500 shadow-md"></div>';
            } else if (val === 2) {
                cellContent = '<div class="w-6 h-6 rounded-full bg-purple-500 shadow-md"></div>';
            }
            html += `
                <div onclick="playSim15Cell(${r}, ${c})" 
                     class="w-8 h-8 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 flex items-center justify-center cursor-pointer transition">
                    ${cellContent}
                </div>
            `;
        }
    }
    container.innerHTML = html;
}

function playSim15Cell(r, c) {
    if (sim15Grid[r][c] !== 0) return;

    // Player 1 Move
    sim15Grid[r][c] = 1;
    sim15Moves++;

    // Player 2 Point-Reflection Strategy (180° rotation around center)
    // Center is between indices (2.5, 2.5) -> (5 - r, 5 - c)
    const p2R = 5 - r;
    const p2C = 5 - c;

    setTimeout(() => {
        if (sim15Grid[p2R][p2C] === 0) {
            sim15Grid[p2R][p2C] = 2;
            sim15Moves++;
        }
        renderSim15();
        const status = document.getElementById('sim15-status');
        status.innerHTML = `<span class="text-purple-400 font-semibold">Player 2 Counter-Move (${p2R + 1}, ${p2C + 1}):</span> Player 2 mirrors Player 1 across the central point (180° rotation)! Because the 6×6 board is centrally symmetric, Player 2 is GUARANTEED to always have a vacant mirror cell and win!`;
    }, 250);

    renderSim15();
}

function resetSim15() {
    sim15Grid = Array(6).fill(null).map(() => Array(6).fill(0));
    sim15Moves = 0;
    renderSim15();
    const status = document.getElementById('sim15-status');
    if (status) {
        status.textContent = "Click any vacant square to place Player 1's piece (Green). Watch Player 2's unbeatable 180° rotational mirror response (Purple)!";
    }
}

// -------------------------------------------------------------
// Simulator 16: The Symmetry Matrix
// -------------------------------------------------------------
const sim16MatrixData = {
    square: { quad: "both", name: "Square", text: "Square: 4 Lines of Symmetry AND Rotational Symmetry of Order 4 (90°)." },
    pinwheel: { quad: "rot_only", name: "Paper Pinwheel", text: "Paper Pinwheel: 0 Lines of Reflection Symmetry, but Rotational Symmetry of Order 4 (90°)." },
    isoc_tri: { quad: "line_only", name: "Isosceles Triangle", text: "Isosceles Triangle: 1 Line of Symmetry, but NO non-trivial rotational symmetry (Order 1)." },
    scalene_tri: { quad: "neither", name: "Scalene Triangle", text: "Scalene Triangle: 0 Lines of Symmetry AND 0 Rotational Symmetry (Order 1 only)." },
    rect: { quad: "both", name: "Rectangle", text: "Rectangle: 2 Lines of Symmetry AND Rotational Symmetry of Order 2 (180°)." },
    letter_z: { quad: "rot_only", name: "Letter 'Z'", text: "Letter 'Z': 0 Reflection lines (folding fails), but looks identical when turned 180° (Order 2)." },
    kite: { quad: "line_only", name: "Kite", text: "Kite: 1 Line of Symmetry down the main diagonal, but 0 Rotational Symmetry (Order 1)." },
    cloud: { quad: "neither", name: "Cloud Shape", text: "Cloud: Asymmetrical. 0 Reflection lines and 0 Rotational Symmetry." }
};

function selectSim16(key) {
    const item = sim16MatrixData[key];
    if (!item) return;

    const display = document.getElementById('sim16-display');
    display.innerHTML = `<strong>${item.name} Selected:</strong> ${item.text}`;

    ['quad-both', 'quad-rot_only', 'quad-line_only', 'quad-neither'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.classList.remove('ring-2', 'ring-cyan-400');
    });

    const activeEl = document.getElementById(`quad-${item.quad}`);
    if (activeEl) {
        activeEl.classList.add('ring-2', 'ring-cyan-400');
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    selectSim1('butterfly');
    updateSim2();
    renderSim3();
    renderSim4();
    renderSim5();
    renderSim6();
    renderSim7();
    renderSim8();
    renderSim9();
    renderSim10();
    renderSim11();
    renderSim12();
    renderSim13();
    renderSim14();
    renderSim15();
    selectSim16('square');

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

with open(".agents/class6_math_symmetry_js.py", "w", encoding="utf-8") as f:
    f.write('"""\nJavaScript Code for Class 6 Math Chapter 9 Symmetry Interactive Lab\n"""\n\n')
    f.write('JS_CODE = ' + repr(js_code) + '\n')

print("Successfully wrote .agents/class6_math_symmetry_js.py")

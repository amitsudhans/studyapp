"""NCERT Class 6 Mathematics Chapter 4: Data Handling and Presentation JavaScript Module."""

INTERACTIVE_JS = """
// State & Navigation
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis
let isMuted = false;
let currentUtterance = null;

function toggleAudio() {
    isMuted = !isMuted;
    const btn = document.getElementById('muteBtn');
    if (isMuted) {
        if (window.speechSynthesis) window.speechSynthesis.cancel();
        if (btn) btn.innerHTML = '🔇';
    } else {
        if (btn) btn.innerHTML = '🔊';
        speakSlide(currentSlide);
    }
}

function speakSlide(slideNum) {
    if (isMuted || !('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const slideElem = document.getElementById(`slide-${slideNum}`);
    if (!slideElem) return;
    const summaryElem = slideElem.querySelector('.slide-summary');
    if (!summaryElem) return;
    const text = summaryElem.innerText;
    currentUtterance = new SpeechSynthesisUtterance(text);
    currentUtterance.rate = 1.0;
    currentUtterance.pitch = 1.0;
    window.speechSynthesis.speak(currentUtterance);
}

function goToSlide(n) {
    if (n < 1 || n > totalSlides) return;
    
    // Hide current
    const curr = document.getElementById(`slide-${currentSlide}`);
    if (curr) curr.classList.add('hidden');
    
    currentSlide = n;
    
    // Show target
    const target = document.getElementById(`slide-${currentSlide}`);
    if (target) target.classList.remove('hidden');
    
    // Update counter & progress
    const counter = document.getElementById('slideCounter');
    if (counter) counter.innerText = `${currentSlide} / ${totalSlides}`;
    
    const progress = document.getElementById('progressBar');
    if (progress) progress.style.width = `${(currentSlide / totalSlides) * 100}%`;
    
    // Update nav buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);
    
    // Terminal Slide Constraint
    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) {
            lastNotice.style.display = 'block';
            lastNotice.innerText = 'You have reached the last slide of this chapter.';
        }
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.style.display = 'none';
    }
    
    // Speak narration
    speakSlide(currentSlide);
    
    // Trigger slide-specific sim setups
    if (currentSlide === 1) renderSportsSurvey();
    else if (currentSlide === 2) updateTallySim(14);
    else if (currentSlide === 3) toggleShoeSort(false);
    else if (currentSlide === 4) setPictoScale(10);
    else if (currentSlide === 5) setPartialTarget(25);
    else if (currentSlide === 6) setVBarDataset('sports');
    else if (currentSlide === 7) initReaderSim();
    else if (currentSlide === 8) setDraftProtocolStep(1);
    else if (currentSlide === 9) loadCaseStudy('sweets');
    else if (currentSlide === 10) setOrientation('vertical');
    else if (currentSlide === 12) toggleMisleadGraph('honest');
    else if (currentSlide === 14) testScaleChoice('optimal');
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

// In-Slide Checkpoints
function checkAnswer(cpId, selectedOption, correctIndex, explanation) {
    const cpContainer = document.getElementById(cpId);
    if (!cpContainer) return;
    
    const buttons = cpContainer.querySelectorAll('.option-btn');
    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIndex) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedOption) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-200');
        }
    });
    
    const feedbackBox = cpContainer.querySelector('.checkpoint-feedback');
    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        if (selectedOption === correctIndex) {
            feedbackBox.innerHTML = `
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-emerald-300 text-xs mt-2">
                    <strong class="font-bold">✓ Correct!</strong> ${explanation}
                </div>`;
        } else {
            feedbackBox.innerHTML = `
                <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30 text-rose-300 text-xs mt-2">
                    <strong class="font-bold">✗ Not Quite.</strong> ${explanation}
                </div>`;
        }
    }
}

// Quiz Selection & Solution Modal
const quizState = {};

function selectQuizOption(qId, selectedIdx, correctIdx) {
    quizState[qId] = selectedIdx;
    const qCard = document.getElementById(`quiz-q-${qId}`);
    if (!qCard) return;
    
    const btns = qCard.querySelectorAll('.quiz-option-btn');
    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-200');
        }
    });
    
    const solBtn = qCard.querySelector('.view-solution-btn');
    if (solBtn) solBtn.classList.remove('hidden');
}

function openSolution(qId) {
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionTitle');
    const body = document.getElementById('solutionBody');
    if (!modal || !title || !body) return;
    
    const questionObj = QUIZ_QUESTIONS_MAP[qId];
    if (!questionObj) return;
    
    title.innerText = `Question ${qId} • Step-by-Step Solution`;
    const letters = ['A', 'B', 'C', 'D'];
    const correctLetter = letters[questionObj.correct];
    const correctText = questionObj.options[questionObj.correct];
    
    body.innerHTML = `
        <div class="space-y-3 text-slate-200 text-xs sm:text-sm">
            <div class="p-3 rounded-lg bg-slate-900 border border-slate-700">
                <span class="text-slate-400 font-bold block mb-1">Question Prompt:</span>
                <p class="font-medium text-slate-100">${questionObj.question}</p>
            </div>
            <div class="p-3 rounded-lg bg-emerald-950/50 border border-emerald-500/40 text-emerald-200">
                <span class="font-bold text-emerald-400 block mb-1">Correct Answer:</span>
                <p class="font-bold">${correctLetter}. ${correctText}</p>
            </div>
            <div class="p-3 rounded-lg bg-amber-950/30 border border-amber-500/30 text-amber-200">
                <span class="font-bold text-amber-300 block mb-1">Mastery Explanation:</span>
                <p class="leading-relaxed text-slate-300">${questionObj.explanation}</p>
            </div>
        </div>
    `;
    modal.style.display = 'flex';
}

function closeSolution() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// -------------------------------------------------------------
// Interactive Simulators Handlers
// -------------------------------------------------------------

// Sim 1: Sports Survey Voting
const sportsSurveyData = {
    'Cricket': 12,
    'Football': 8,
    'Badminton': 5
};

function castSportVote(sport) {
    if (sportsSurveyData[sport] !== undefined) {
        sportsSurveyData[sport]++;
        renderSportsSurvey();
    }
}

function resetSportsSurvey() {
    sportsSurveyData['Cricket'] = 12;
    sportsSurveyData['Football'] = 8;
    sportsSurveyData['Badminton'] = 5;
    renderSportsSurvey();
}

function renderSportsSurvey() {
    const container = document.getElementById('sportsVoteBars');
    const badge = document.getElementById('surveyTotalBadge');
    if (!container) return;
    
    const total = sportsSurveyData['Cricket'] + sportsSurveyData['Football'] + sportsSurveyData['Badminton'];
    if (badge) badge.innerText = `Total Class Sample: ${total} Students`;
    
    const maxVal = Math.max(15, Math.max(...Object.values(sportsSurveyData)));
    const colors = {
        'Cricket': { bar: 'bg-amber-500', text: 'text-amber-300' },
        'Football': { bar: 'bg-cyan-500', text: 'text-cyan-300' },
        'Badminton': { bar: 'bg-emerald-500', text: 'text-emerald-300' }
    };
    
    let html = '';
    for (const [sport, count] of Object.entries(sportsSurveyData)) {
        const pct = Math.round((count / maxVal) * 100);
        html += `
            <div>
                <div class="flex justify-between text-xs mb-1">
                    <span class="font-semibold ${colors[sport].text}">${sport}</span>
                    <span class="font-mono text-slate-300">${count} votes (${Math.round((count/total)*100)}%)</span>
                </div>
                <div class="w-full bg-slate-900 rounded-full h-3 border border-slate-700/80 overflow-hidden">
                    <div class="${colors[sport].bar} h-3 rounded-full transition-all duration-300" style="width: ${pct}%"></div>
                </div>
            </div>
        `;
    }
    container.innerHTML = html;
}

// Sim 2: Tally Bundler Slider
function updateTallySim(val) {
    const sliderVal = document.getElementById('tallySliderVal');
    const countBadge = document.getElementById('tallyCountBadge');
    const display = document.getElementById('tallyDisplay');
    const slider = document.getElementById('tallySlider');
    
    if (sliderVal) sliderVal.innerText = val;
    if (slider && parseInt(slider.value) !== val) slider.value = val;
    if (countBadge) countBadge.innerText = `Total Count: ${val}`;
    
    if (!display) return;
    
    const bundles = Math.floor(val / 5);
    const remainder = val % 5;
    
    let bundlesHtml = '';
    for (let b = 0; b < bundles; b++) {
        bundlesHtml += `
            <div class="flex items-center justify-center p-2 rounded-lg bg-slate-900 border border-amber-500/40 relative w-14 h-16 shadow-inner">
                <svg class="w-full h-full" viewBox="0 0 50 60">
                    <line x1="10" y1="10" x2="10" y2="50" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                    <line x1="18" y1="10" x2="18" y2="50" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                    <line x1="26" y1="10" x2="26" y2="50" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                    <line x1="34" y1="10" x2="34" y2="50" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                    <line x1="6" y1="48" x2="38" y2="12" stroke="#ef4444" stroke-width="4.5" stroke-linecap="round"/>
                </svg>
                <span class="absolute -bottom-2 text-[9px] font-mono text-amber-400 font-bold bg-slate-950 px-1 rounded border border-amber-900">5</span>
            </div>
        `;
    }
    
    if (remainder > 0) {
        let singleLines = '';
        const xStarts = [12, 20, 28, 36];
        for (let r = 0; r < remainder; r++) {
            singleLines += `<line x1="${xStarts[r]}" y1="10" x2="${xStarts[r]}" y2="50" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>`;
        }
        bundlesHtml += `
            <div class="flex items-center justify-center p-2 rounded-lg bg-slate-900 border border-cyan-500/40 relative w-14 h-16 shadow-inner">
                <svg class="w-full h-full" viewBox="0 0 50 60">
                    ${singleLines}
                </svg>
                <span class="absolute -bottom-2 text-[9px] font-mono text-cyan-400 font-bold bg-slate-950 px-1 rounded border border-cyan-900">${remainder}</span>
            </div>
        `;
    }
    
    display.innerHTML = bundlesHtml;
}

// Sim 3: Shoe Size Sorter
const rawShoeSizes = [5, 4, 7, 5, 6, 4, 5, 8, 6, 5, 7, 6, 5];
const sortedShoeSizes = [4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8];

function toggleShoeSort(isSorted) {
    const list = document.getElementById('shoeSizesList');
    const badge = document.getElementById('sortStatusBadge');
    const summary = document.getElementById('shoeStatsSummary');
    if (!list) return;
    
    const data = isSorted ? sortedShoeSizes : rawShoeSizes;
    if (badge) {
        badge.innerText = isSorted ? 'Sorted Ascending (Ready for Tally)' : 'Raw Unsorted Survey Data';
        badge.className = isSorted ? 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40' : 'font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40';
    }
    
    let html = '';
    data.forEach(val => {
        const isMode = (val === 5);
        const bg = isSorted ? (isMode ? 'bg-amber-500/30 text-amber-300 border-amber-400' : 'bg-slate-800 text-slate-200 border-slate-700') : 'bg-slate-800 text-slate-200 border-slate-700';
        html += `<span class="px-2.5 py-1.5 rounded-lg border font-mono font-bold text-xs ${bg}">${val}</span>`;
    });
    list.innerHTML = html;
    
    if (summary) {
        if (isSorted) {
            summary.innerHTML = `
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Smallest</span>
                        <span class="font-bold text-cyan-300 font-mono text-sm">Size 4</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Largest</span>
                        <span class="font-bold text-rose-300 font-mono text-sm">Size 8</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Spread Range</span>
                        <span class="font-bold text-violet-300 font-mono text-sm">8 − 4 = 4</span>
                    </div>
                    <div class="p-2 rounded bg-amber-950/40 border border-amber-500/40">
                        <span class="text-amber-300 block text-[10px]">Mode (Peak)</span>
                        <span class="font-bold text-amber-400 font-mono text-sm">Size 5 (Freq: 5)</span>
                    </div>
                </div>
            `;
        } else {
            summary.innerHTML = `
                <p class="text-slate-400 text-xs italic">
                    Unsorted order makes it difficult to quickly spot the smallest shoe size, highest shoe size, or the most popular size without counting one by one.
                </p>
            `;
        }
    }
}

// Sim 4: Pictograph Scaler
const pictographData = [
    { mode: 'School Bus', count: 40, icon: '🚌' },
    { mode: 'Bicycle', count: 30, icon: '🚲' },
    { mode: 'Walking', count: 20, icon: '🚶' },
    { mode: 'Family Car', count: 10, icon: '🚗' }
];

function setPictoScale(scale) {
    const badge = document.getElementById('pictoKeyBadge');
    const container = document.getElementById('pictographRows');
    if (badge) badge.innerText = `Key Scale: 1 Icon = ${scale} Students`;
    if (!container) return;
    
    let html = '';
    pictographData.forEach(item => {
        const fullIcons = Math.floor(item.count / scale);
        const rem = item.count % scale;
        let iconsHtml = '';
        for (let i = 0; i < fullIcons; i++) {
            iconsHtml += `<span class="text-xl sm:text-2xl" title="${scale} students">${item.icon}</span>`;
        }
        if (rem > 0) {
            iconsHtml += `<span class="text-sm opacity-60 font-bold bg-slate-800 px-1 py-0.5 rounded border border-slate-700 text-amber-300" title="${rem} students">½</span>`;
        }
        
        html += `
            <div class="flex items-center justify-between p-2 rounded-lg bg-slate-900 border border-slate-800 text-xs">
                <span class="font-bold text-slate-300 w-24 shrink-0">${item.mode}</span>
                <div class="flex items-center gap-1.5 flex-wrap flex-1 px-2">
                    ${iconsHtml}
                </div>
                <span class="font-mono text-slate-400 w-16 text-right font-bold shrink-0">${item.count} total</span>
            </div>
        `;
    });
    container.innerHTML = html;
}

// Sim 5: Partial Symbols
function setPartialTarget(num) {
    const badge = document.getElementById('partialSymbolBadge');
    const iconContainer = document.getElementById('partialStarIcons');
    const textContainer = document.getElementById('partialExplainText');
    if (badge) badge.innerText = `Display Target: ${num} Items`;
    
    const full = Math.floor(num / 10);
    const rem = num % 10;
    
    let icons = '';
    for (let i = 0; i < full; i++) {
        icons += `<span class="text-3xl sm:text-4xl">⭐</span>`;
    }
    if (rem >= 5) {
        icons += `
            <div class="relative inline-flex items-center justify-center w-8 h-8 overflow-hidden">
                <span class="text-3xl sm:text-4xl absolute -left-1">⭐</span>
                <div class="absolute right-0 top-0 bottom-0 w-4 bg-slate-950/80 backdrop-blur-[1px] border-l border-amber-400/50"></div>
            </div>
        `;
    }
    if (iconContainer) iconContainer.innerHTML = icons;
    
    if (textContainer) {
        if (rem === 5) {
            textContainer.innerHTML = `
                <p class="text-emerald-300 font-medium">
                    ✓ Clean fit: <strong>${full} full stars</strong> (${full} × 10 = ${full*10}) + <strong>1 half star</strong> (5 items) = <strong>${num} items</strong>.
                </p>
            `;
        } else if (rem === 0) {
            textContainer.innerHTML = `
                <p class="text-cyan-300 font-medium">
                    ✓ Clean exact multiple: <strong>${full} full stars</strong> (${full} × 10 = ${num} items). No fractional symbols needed!
                </p>
            `;
        } else {
            textContainer.innerHTML = `
                <p class="text-amber-300 font-medium">
                    ⚠️ Fractional limitation: ${rem} is not half of 10. Representing ${rem} with a partial symbol is subjective and hard to read accurately!
                </p>
            `;
        }
    }
}

// Sim 6: Vertical Bar Chart Switcher
const barDatasets = {
    'sports': {
        name: 'Class Sports Preferences',
        unit: 'Students',
        scale: 5,
        max: 30,
        items: [
            { label: 'Cricket', val: 26, color: '#f59e0b' },
            { label: 'Football', val: 18, color: '#06b6d4' },
            { label: 'Tennis', val: 12, color: '#10b981' },
            { label: 'Badminton', val: 22, color: '#8b5cf6' }
        ]
    },
    'fruits': {
        name: 'Weekly Fruit Carts Sold',
        unit: 'Kg',
        scale: 10,
        max: 60,
        items: [
            { label: 'Apple', val: 45, color: '#ef4444' },
            { label: 'Mango', val: 58, color: '#f59e0b' },
            { label: 'Banana', val: 32, color: '#eab308' },
            { label: 'Orange', val: 24, color: '#f97316' }
        ]
    },
    'traffic': {
        name: 'Vehicles Crossing Junction',
        unit: 'Vehicles',
        scale: 20,
        max: 100,
        items: [
            { label: '8 AM', val: 75, color: '#3b82f6' },
            { label: '9 AM', val: 96, color: '#8b5cf6' },
            { label: '10 AM', val: 62, color: '#06b6d4' },
            { label: '11 AM', val: 38, color: '#10b981' }
        ]
    }
};

function setVBarDataset(type) {
    const data = barDatasets[type] || barDatasets['sports'];
    const badge = document.getElementById('barGraphScaleBadge');
    const grid = document.getElementById('vBarGridGroup');
    const bars = document.getElementById('vBarsGroup');
    
    if (badge) badge.innerText = `${data.name} (1 unit length = ${data.scale} ${data.unit})`;
    if (!grid || !bars) return;
    
    // Y-axis spans from Y=190 (value 0) to Y=30 (value max)
    const yOrigin = 190;
    const yTop = 30;
    const hRange = yOrigin - yTop; // 160px
    
    // Build Grid lines
    let gridLines = '';
    const numTicks = 5;
    for (let i = 0; i <= numTicks; i++) {
        const val = Math.round((data.max / numTicks) * i);
        const y = yOrigin - (i / numTicks) * hRange;
        gridLines += `
            <line x1="50" y1="${y}" x2="380" y2="${y}" stroke="#334155" stroke-dasharray="2,2" stroke-width="1"/>
            <text x="42" y="${y + 4}" fill="#94a3b8" font-size="10" text-anchor="end" font-family="monospace">${val}</text>
        `;
    }
    grid.innerHTML = gridLines;
    
    // Build Bars
    let barsHtml = '';
    const barWidth = 44;
    const spacing = (330 - (data.items.length * barWidth)) / (data.items.length + 1);
    
    data.items.forEach((item, idx) => {
        const x = 55 + spacing + idx * (barWidth + spacing);
        const barHeight = (item.val / data.max) * hRange;
        const y = yOrigin - barHeight;
        
        barsHtml += `
            <g class="transition-all duration-300">
                <rect x="${x}" y="${y}" width="${barWidth}" height="${barHeight}" rx="4" fill="${item.color}" fill-opacity="0.85" stroke="${item.color}" stroke-width="1.5"/>
                <text x="${x + barWidth / 2}" y="${y - 6}" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">${item.val}</text>
                <text x="${x + barWidth / 2}" y="206" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle">${item.label}</text>
            </g>
        `;
    });
    bars.innerHTML = barsHtml;
}

// Sim 7: Reader Crosshair
function initReaderSim() {
    const barsGroup = document.getElementById('readerBarsGroup');
    const crosshair = document.getElementById('readerCrosshairLine');
    const readout = document.getElementById('crosshairReadout');
    if (!barsGroup || !crosshair || !readout) return;
    
    const items = [
        { label: 'Morning Peak (8-9 AM)', val: 85, color: '#f59e0b', x: 75 },
        { label: 'Mid-Morning (9-10 AM)', val: 65, color: '#06b6d4', x: 155 },
        { label: 'Noon Lull (12-1 PM)', val: 35, color: '#10b981', x: 235 },
        { label: 'Evening Rush (5-6 PM)', val: 92, color: '#ec4899', x: 315 }
    ];
    
    const yOrigin = 200;
    const hRange = 160;
    const maxVal = 100;
    
    let html = '';
    items.forEach(item => {
        const h = (item.val / maxVal) * hRange;
        const y = yOrigin - h;
        html += `
            <rect class="cursor-pointer hover:brightness-125 transition-all"
                  data-label="${item.label}" data-val="${item.val}" data-y="${y}"
                  x="${item.x}" y="${y}" width="50" height="${h}" rx="4"
                  fill="${item.color}" fill-opacity="0.8" stroke="${item.color}" stroke-width="1.5"/>
            <text x="${item.x + 25}" y="${y - 6}" fill="#f1f5f9" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">${item.val}</text>
            <text x="${item.x + 25}" y="216" fill="#94a3b8" font-size="9" text-anchor="middle">${item.label.split(' ')[0]}</text>
        `;
    });
    barsGroup.innerHTML = html;
    
    const rects = barsGroup.querySelectorAll('rect');
    rects.forEach(r => {
        r.addEventListener('mouseenter', (e) => {
            const y = e.target.getAttribute('data-y');
            const val = e.target.getAttribute('data-val');
            const label = e.target.getAttribute('data-label');
            crosshair.setAttribute('y1', y);
            crosshair.setAttribute('y2', y);
            crosshair.setAttribute('opacity', '1');
            readout.innerText = `${label} = ${val} vehicles`;
        });
        r.addEventListener('mouseleave', () => {
            crosshair.setAttribute('opacity', '0');
            readout.innerText = 'Hover over any bar to read';
        });
    });
}

// Sim 8: Drafting Protocol Step-by-Step
function setDraftProtocolStep(step) {
    const badge = document.getElementById('draftingStepBadge');
    const axes = document.getElementById('draftStepAxes');
    const scale = document.getElementById('draftStepScale');
    const cats = document.getElementById('draftStepCategories');
    const bars = document.getElementById('draftStepBars');
    
    const descriptions = [
        'Step 1 of 4: Draw Perpendicular Axes (Horizontal X & Vertical Y meeting at Origin 0)',
        'Step 2 of 4: Choose Scale (e.g. 1 unit = 10 runs) & Mark Equal Tick Marks along Y',
        'Step 3 of 4: Mark Categories along Horizontal Axis with Uniform Equal Gaps',
        'Step 4 of 4: Draw Bars with Equal Width & Heights Equal to Frequencies'
    ];
    
    if (badge) badge.innerText = descriptions[step - 1];
    
    if (axes) axes.style.opacity = step >= 1 ? '1' : '0.1';
    if (scale) scale.style.opacity = step >= 2 ? '1' : '0';
    if (cats) cats.style.opacity = step >= 3 ? '1' : '0';
    if (bars) bars.style.opacity = step >= 4 ? '1' : '0';
}

// Sim 9: Real-World Case Studies
const caseStudies = {
    'sweets': {
        title: 'Sweet Preferences in Grade 6',
        yAxis: 'Number of Students',
        scale: '1 cm = 2 Students',
        bars: [
            { label: 'Jalebi', val: 12, max: 16, color: '#f59e0b' },
            { label: 'Laddoo', val: 15, max: 16, color: '#eab308' },
            { label: 'Rasgulla', val: 9, max: 16, color: '#06b6d4' },
            { label: 'Barfi', val: 6, max: 16, color: '#ec4899' }
        ]
    },
    'cricket': {
        title: 'Runs Scored in 5 Consecutive Overs',
        yAxis: 'Runs Scored',
        scale: '1 cm = 5 Runs',
        bars: [
            { label: 'Over 1', val: 4, max: 20, color: '#3b82f6' },
            { label: 'Over 2', val: 11, max: 20, color: '#10b981' },
            { label: 'Over 3', val: 6, max: 20, color: '#6366f1' },
            { label: 'Over 4', val: 18, max: 20, color: '#ef4444' },
            { label: 'Over 5', val: 9, max: 20, color: '#8b5cf6' }
        ]
    },
    'budget': {
        title: 'Family Monthly Budget Allocation',
        yAxis: 'Percentage of Income (%)',
        scale: '1 cm = 10%',
        bars: [
            { label: 'Food', val: 35, max: 50, color: '#10b981' },
            { label: 'Rent', val: 25, max: 50, color: '#3b82f6' },
            { label: 'Education', val: 15, max: 50, color: '#f59e0b' },
            { label: 'Savings', val: 20, max: 50, color: '#8b5cf6' },
            { label: 'Misc', val: 5, max: 50, color: '#ec4899' }
        ]
    }
};

function loadCaseStudy(studyKey) {
    const data = caseStudies[studyKey] || caseStudies['sweets'];
    const badge = document.getElementById('caseTitleBadge');
    const container = document.getElementById('caseBarsGroup');
    if (badge) badge.innerText = `${data.title} • Scale: ${data.scale}`;
    if (!container) return;
    
    const yOrigin = 190;
    const hRange = 150;
    const barWidth = Math.floor(280 / data.bars.length) - 12;
    
    let html = '';
    data.bars.forEach((b, idx) => {
        const x = 60 + idx * (barWidth + 12);
        const h = (b.val / b.max) * hRange;
        const y = yOrigin - h;
        html += `
            <g class="transition-all duration-300">
                <rect x="${x}" y="${y}" width="${barWidth}" height="${h}" rx="4" fill="${b.color}" fill-opacity="0.85" stroke="${b.color}" stroke-width="1.5"/>
                <text x="${x + barWidth/2}" y="${y - 5}" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">${b.val}</text>
                <text x="${x + barWidth/2}" y="206" fill="#cbd5e1" font-size="9" font-weight="600" text-anchor="middle">${b.label}</text>
            </g>
        `;
    });
    container.innerHTML = html;
}

// Sim 10: Orientation Switcher (Vertical Columns vs Horizontal Bars)
function setOrientation(mode) {
    const badge = document.getElementById('orientationBadge');
    const group = document.getElementById('orientGraphGroup');
    if (!group) return;
    
    if (mode === 'vertical') {
        if (badge) badge.innerText = 'Vertical Columns: Natural for Heights Rising Skyward';
        const peaks = [
            { name: 'Everest', val: 8848, color: '#38bdf8' },
            { name: 'K2', val: 8611, color: '#818cf8' },
            { name: 'Kanchen.', val: 8586, color: '#c084fc' }
        ];
        let html = '';
        peaks.forEach((p, idx) => {
            const x = 90 + idx * 85;
            const h = (p.val / 9000) * 150;
            const y = 190 - h;
            html += `
                <rect x="${x}" y="${y}" width="48" height="${h}" rx="4" fill="${p.color}" fill-opacity="0.85" stroke="${p.color}" stroke-width="1.5"/>
                <text x="${x + 24}" y="${y - 6}" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">${p.val}m</text>
                <text x="${x + 24}" y="206" fill="#cbd5e1" font-size="10" text-anchor="middle">${p.name}</text>
            `;
        });
        group.innerHTML = html;
    } else {
        if (badge) badge.innerText = 'Horizontal Bars: Natural for Long River Lengths & Text Labels';
        const rivers = [
            { name: 'Ganga', val: 2525, color: '#06b6d4' },
            { name: 'Godavari', val: 1465, color: '#3b82f6' },
            { name: 'Krishna', val: 1400, color: '#6366f1' },
            { name: 'Yamuna', val: 1376, color: '#10b981' }
        ];
        let html = '';
        rivers.forEach((r, idx) => {
            const y = 45 + idx * 38;
            const w = (r.val / 3000) * 230;
            html += `
                <text x="80" y="${y + 14}" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="end">${r.name}</text>
                <rect x="90" y="${y}" width="${w}" height="22" rx="4" fill="${r.color}" fill-opacity="0.85" stroke="${r.color}" stroke-width="1.5"/>
                <text x="${90 + w + 8}" y="${y + 15}" fill="#f8fafc" font-size="10" font-weight="bold" font-family="monospace">${r.val} km</text>
            `;
        });
        group.innerHTML = html;
    }
}

// Sim 12: Misleading Graph Toggle (Truncated Baseline vs True Zero)
function toggleMisleadGraph(mode) {
    const badge = document.getElementById('misleadBadge');
    const group = document.getElementById('misleadGraphGroup');
    if (!group) return;
    
    // Product A = 100, Product B = 104
    if (mode === 'deceptive') {
        if (badge) {
            badge.innerText = '⚠️ Deceptive: Baseline starts at 98! Bar B looks 300% taller than Bar A';
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
        // Baseline 98, Range 98-106 (diff 8)
        const hA = ((100 - 98) / 8) * 150; // 37.5px
        const hB = ((104 - 98) / 8) * 150; // 112.5px (3x height!)
        group.innerHTML = `
            <line x1="60" y1="190" x2="350" y2="190" stroke="#f43f5e" stroke-width="2"/>
            <text x="52" y="194" fill="#f43f5e" font-size="10" text-anchor="end" font-weight="bold">98</text>
            <text x="52" y="44" fill="#94a3b8" font-size="10" text-anchor="end">106</text>
            
            <rect x="110" y="${190 - hA}" width="60" height="${hA}" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="140" y="${190 - hA - 6}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">100</text>
            <text x="140" y="206" fill="#cbd5e1" font-size="10" text-anchor="middle">Company X</text>
            
            <rect x="220" y="${190 - hB}" width="60" height="${hB}" rx="4" fill="#e11d48" stroke="#fb7185" stroke-width="1.5"/>
            <text x="250" y="${190 - hB - 6}" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">104</text>
            <text x="250" y="206" fill="#cbd5e1" font-size="10" text-anchor="middle">Company Y</text>
            
            <text x="200" y="30" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">DISPROPORTIONATE: Difference of only 4 units exaggerated!</text>
        `;
    } else {
        if (badge) {
            badge.innerText = '✓ Honest: Baseline starts strictly at 0. Both heights reflect real ratio';
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        // Baseline 0, Range 0-120
        const hA = (100 / 120) * 150; // 125px
        const hB = (104 / 120) * 150; // 130px
        group.innerHTML = `
            <line x1="60" y1="190" x2="350" y2="190" stroke="#10b981" stroke-width="2"/>
            <text x="52" y="194" fill="#10b981" font-size="10" text-anchor="end" font-weight="bold">0</text>
            <text x="52" y="44" fill="#94a3b8" font-size="10" text-anchor="end">120</text>
            
            <rect x="110" y="${190 - hA}" width="60" height="${hA}" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="140" y="${190 - hA - 6}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">100</text>
            <text x="140" y="206" fill="#cbd5e1" font-size="10" text-anchor="middle">Company X</text>
            
            <rect x="220" y="${190 - hB}" width="60" height="${hB}" rx="4" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
            <text x="250" y="${190 - hB - 6}" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">104</text>
            <text x="250" y="206" fill="#cbd5e1" font-size="10" text-anchor="middle">Company Y</text>
            
            <text x="200" y="30" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">HONEST: Proper proportional comparison (104 vs 100 is almost equal)</text>
        `;
    }
}

// Sim 14: Scale Choice Laboratory
function testScaleChoice(choice) {
    const badge = document.getElementById('scaleFeedbackBadge');
    const group = document.getElementById('scaleSelectGraphGroup');
    if (!group) return;
    
    // Values: 20, 50, 35, 75
    const values = [20, 50, 35, 75];
    const labels = ['Cat A', 'Cat B', 'Cat C', 'Cat D'];
    
    if (choice === 'small') {
        if (badge) {
            badge.innerText = 'Scale = 2 (Too Small): 75 runs needs 37.5 units! Bars shoot off the page!';
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
        let html = '';
        values.forEach((v, idx) => {
            const x = 90 + idx * 65;
            const h = v * 3.5; // shoots way past 160px!
            const y = Math.max(10, 190 - h);
            const clampedH = Math.min(185, h);
            html += `
                <rect x="${x}" y="${y}" width="42" height="${clampedH}" rx="4" fill="#ef4444" fill-opacity="0.8" stroke="#f87171" stroke-width="1.5"/>
                <text x="${x + 21}" y="${y - 4}" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">OVERFLOW!</text>
                <text x="${x + 21}" y="206" fill="#cbd5e1" font-size="9" text-anchor="middle">${labels[idx]}</text>
            `;
        });
        group.innerHTML = html;
    } else if (choice === 'optimal') {
        if (badge) {
            badge.innerText = 'Scale = 10 (Optimal): Tallest bar (75) is 7.5 units tall. Perfect fit & readable!';
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        let html = '';
        values.forEach((v, idx) => {
            const x = 90 + idx * 65;
            const h = (v / 80) * 150;
            const y = 190 - h;
            html += `
                <rect x="${x}" y="${y}" width="42" height="${h}" rx="4" fill="#10b981" fill-opacity="0.8" stroke="#34d399" stroke-width="1.5"/>
                <text x="${x + 21}" y="${y - 5}" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">${v}</text>
                <text x="${x + 21}" y="206" fill="#cbd5e1" font-size="9" text-anchor="middle">${labels[idx]}</text>
            `;
        });
        group.innerHTML = html;
    } else {
        if (badge) {
            badge.innerText = 'Scale = 50 (Too Large): Bars are flattened to the ground. Differences invisible!';
            badge.className = 'font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40';
        }
        let html = '';
        values.forEach((v, idx) => {
            const x = 90 + idx * 65;
            const h = (v / 200) * 150; // max height is ~50px
            const y = 190 - h;
            html += `
                <rect x="${x}" y="${y}" width="42" height="${h}" rx="4" fill="#f59e0b" fill-opacity="0.8" stroke="#fbbf24" stroke-width="1.5"/>
                <text x="${x + 21}" y="${y - 4}" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">${v}</text>
                <text x="${x + 21}" y="206" fill="#cbd5e1" font-size="9" text-anchor="middle">${labels[idx]}</text>
            `;
        });
        group.innerHTML = html;
    }
}

// Keyboard navigation & modal close
window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') nextSlide();
    else if (e.key === 'ArrowLeft') prevSlide();
    else if (e.key === 'Escape') closeSolution();
});

// Click outside modal to close
window.addEventListener('click', (e) => {
    const modal = document.getElementById('solutionModal');
    if (modal && e.target === modal) {
        closeSolution();
    }
});
"""

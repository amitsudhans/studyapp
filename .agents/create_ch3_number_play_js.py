import sys

def generate_js():
    js_content = """
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
    if (currentSlide === 1) setFriendsPattern('pyramid');
    else if (currentSlide === 2) setSupercellPreset('max5');
    else if (currentSlide === 3) setNumberLineScale(10);
    else if (currentSlide === 5) renderDetectiveGrid();
    else if (currentSlide === 7) runReverseAndAdd(57);
    else if (currentSlide === 8) runKaprekarRoutine(3524);
    else if (currentSlide === 11) setGaussRange(10);
    else if (currentSlide === 12) runCollatzGraph(7);
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

// Sim 1: Line of Friends
function setFriendsPattern(type) {
    const group = document.getElementById('friendsGroup');
    const badge = document.getElementById('friendsStatusBadge');
    if (!group) return;
    
    let heights = [100, 130, 170, 140, 110]; // pyramid
    if (type === 'valley') heights = [160, 120, 90, 130, 170];
    else if (type === 'ascending') heights = [80, 105, 130, 155, 180];
    
    group.innerHTML = '';
    const xPositions = [60, 130, 200, 270, 340];
    
    for (let i = 0; i < 5; i++) {
        const h = heights[i];
        const x = xPositions[i];
        const y = 200 - h;
        
        // Count taller neighbors
        let tallerCount = 0;
        if (i > 0 && heights[i - 1] > h) tallerCount++;
        if (i < 4 && heights[i + 1] > h) tallerCount++;
        
        // Bar
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', x - 18);
        rect.setAttribute('y', y);
        rect.setAttribute('width', '36');
        rect.setAttribute('height', h);
        rect.setAttribute('rx', '6');
        rect.setAttribute('fill', '#0284c7');
        rect.setAttribute('fill-opacity', '0.7');
        rect.setAttribute('stroke', '#38bdf8');
        rect.setAttribute('stroke-width', '2');
        group.appendChild(rect);
        
        // Head
        const head = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        head.setAttribute('cx', x);
        head.setAttribute('cy', y - 10);
        head.setAttribute('r', '8');
        head.setAttribute('fill', '#fbbf24');
        group.appendChild(head);
        
        // Reported clue badge
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', x);
        text.setAttribute('y', y + 25);
        text.setAttribute('fill', '#ffffff');
        text.setAttribute('font-size', '13');
        text.setAttribute('font-weight', 'bold');
        text.setAttribute('text-anchor', 'middle');
        text.textContent = `"${tallerCount}"`;
        group.appendChild(text);
        
        // Label
        const lbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        lbl.setAttribute('x', x);
        lbl.setAttribute('y', '218');
        lbl.setAttribute('fill', '#94a3b8');
        lbl.setAttribute('font-size', '10');
        lbl.setAttribute('text-anchor', 'middle');
        lbl.textContent = `P${i + 1}`;
        group.appendChild(lbl);
    }
    if (badge) badge.innerText = `Pattern: ${type.toUpperCase()} • Quoted: Taller Neighbors`;
}

// Sim 2: Supercells
let currentGrid = [
    [9, 2, 8],
    [3, 7, 1],
    [6, 4, 5]
];

function setSupercellPreset(preset) {
    if (preset === 'max5') {
        currentGrid = [
            [9, 1, 8],
            [2, 7, 3],
            [6, 4, 5]
        ];
    } else {
        const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].sort(() => Math.random() - 0.5);
        currentGrid = [
            [nums[0], nums[1], nums[2]],
            [nums[3], nums[4], nums[5]],
            [nums[6], nums[7], nums[8]]
        ];
    }
    renderSupercellGrid();
}

function renderSupercellGrid() {
    const container = document.getElementById('gridSupercellContainer');
    const badge = document.getElementById('supercellCountBadge');
    if (!container) return;
    
    container.innerHTML = '';
    let supercellCount = 0;
    
    for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 3; c++) {
            const val = currentGrid[r][c];
            // Check neighbors
            let isSuper = true;
            if (r > 0 && currentGrid[r - 1][c] >= val) isSuper = false;
            if (r < 2 && currentGrid[r + 1][c] >= val) isSuper = false;
            if (c > 0 && currentGrid[r][c - 1] >= val) isSuper = false;
            if (c < 2 && currentGrid[r][c + 1] >= val) isSuper = false;
            
            if (isSuper) supercellCount++;
            
            const cell = document.createElement('div');
            cell.className = `flex flex-col items-center justify-center rounded-xl font-mono font-bold text-lg border transition-all ${
                isSuper 
                ? 'bg-amber-500/20 text-amber-300 border-amber-500/60 shadow-lg shadow-amber-500/30' 
                : 'bg-slate-900/80 text-slate-400 border-slate-800'
            }`;
            cell.innerHTML = `
                <span>${val}</span>
                ${isSuper ? '<span class="text-[9px] uppercase tracking-tighter text-amber-400 font-sans">SUPER</span>' : ''}
            `;
            container.appendChild(cell);
        }
    }
    if (badge) badge.innerText = `Supercells Found: ${supercellCount}`;
}

// Sim 3: Number Line Scale
function setNumberLineScale(step) {
    const group = document.getElementById('numLineTicksGroup');
    const badge = document.getElementById('numLineStepBadge');
    const mystery = document.getElementById('mysteryLabel');
    const mysteryPt = document.getElementById('mysteryPt');
    if (!group) return;
    
    group.innerHTML = '';
    const totalTicks = 7;
    const startX = 60, gap = 45;
    
    for (let i = 0; i < totalTicks; i++) {
        const x = startX + i * gap;
        const val = i * step;
        
        const tick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        tick.setAttribute('x1', x);
        tick.setAttribute('y1', '110');
        tick.setAttribute('x2', x);
        tick.setAttribute('y2', '130');
        tick.setAttribute('stroke', '#38bdf8');
        tick.setAttribute('stroke-width', '2');
        group.appendChild(tick);
        
        if (i !== 4) { // keep 4th mystery
            const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            txt.setAttribute('x', x);
            txt.setAttribute('y', '150');
            txt.setAttribute('fill', '#cbd5e1');
            txt.setAttribute('font-size', '11');
            txt.setAttribute('font-weight', 'bold');
            txt.setAttribute('font-family', 'monospace');
            txt.setAttribute('text-anchor', 'middle');
            txt.textContent = val;
            group.appendChild(txt);
        }
    }
    
    const targetVal = 4 * step;
    if (mystery) mystery.textContent = `? = ${targetVal}`;
    if (mysteryPt) mysteryPt.setAttribute('cx', startX + 4 * gap);
    if (badge) badge.innerText = `Step Size = +${step} • 4th Step = ${targetVal}`;
}

// Sim 4: Digit Counts
function setDigitCountSim(d) {
    const formula = document.getElementById('digitCountFormula');
    const range = document.getElementById('digitCountRange');
    const badge = document.getElementById('digitCountBadge');
    const bar = document.getElementById('digitCountBar');
    if (!formula) return;
    
    const power = d - 1;
    const count = 9 * Math.pow(10, power);
    const minVal = Math.pow(10, power);
    const maxVal = Math.pow(10, d) - 1;
    
    formula.innerText = `9 × 10^${power} = ${count.toLocaleString()}`;
    range.innerText = `Range: ${minVal.toLocaleString()} to ${maxVal.toLocaleString()} (${maxVal} − ${minVal} + 1 = ${count.toLocaleString()})`;
    if (badge) badge.innerText = `${d} Digits: ${count.toLocaleString()} Numbers`;
    if (bar) bar.style.width = `${d * 20}%`;
}

// Sim 5: Digit Detective
function renderDetectiveGrid() {
    const container = document.getElementById('detectiveDisplay');
    if (!container || container.children.length > 0) return;
    
    for (let i = 1; i <= 100; i++) {
        const span = document.createElement('span');
        span.id = `chart-num-${i}`;
        span.className = 'p-1 rounded bg-slate-900 border border-slate-800 transition-colors';
        span.textContent = i;
        container.appendChild(span);
    }
}

function highlightDigitInChart(d) {
    renderDetectiveGrid();
    const badge = document.getElementById('detectiveBadge');
    let count = 0;
    
    for (let i = 1; i <= 100; i++) {
        const span = document.getElementById(`chart-num-${i}`);
        if (!span) continue;
        const s = i.toString();
        const matches = (s.match(new RegExp(d, 'g')) || []).length;
        if (matches > 0) {
            count += matches;
            span.className = 'p-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500 font-bold';
        } else {
            span.className = 'p-1 rounded bg-slate-900 text-slate-500 border border-slate-800';
        }
    }
    if (badge) badge.innerText = `Digit '${d}' appears: ${count} times (1–100)`;
}

function highlightDigitSumInChart(sum) {
    renderDetectiveGrid();
    const badge = document.getElementById('detectiveBadge');
    let count = 0;
    
    for (let i = 1; i <= 100; i++) {
        const span = document.getElementById(`chart-num-${i}`);
        if (!span) continue;
        const dSum = i.toString().split('').reduce((acc, c) => acc + parseInt(c), 0);
        if (dSum === sum) {
            count++;
            span.className = 'p-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500 font-bold';
        } else {
            span.className = 'p-1 rounded bg-slate-900 text-slate-500 border border-slate-800';
        }
    }
    if (badge) badge.innerText = `Numbers with Digit Sum = ${sum}: ${count} numbers found`;
}

// Sim 6: Palindrome Mirror
function testPalindromeInput(str) {
    const orig = document.getElementById('palOriginal');
    const rev = document.getElementById('palReversed');
    const badge = document.getElementById('palMirrorBadge');
    const verdict = document.getElementById('palVerdictText');
    if (!orig || !rev) return;
    
    const reversedStr = str.split('').reverse().join('');
    orig.innerText = str;
    rev.innerText = reversedStr;
    
    if (str === reversedStr) {
        if (badge) badge.innerText = `${str} is a Palindrome!`;
        if (verdict) {
            verdict.innerText = '✓ Reads identically in both directions!';
            verdict.className = 'mt-4 text-xs font-bold text-emerald-400 font-mono';
        }
    } else {
        if (badge) badge.innerText = `${str} is NOT a Palindrome`;
        if (verdict) {
            verdict.innerText = `✗ ${str} ≠ ${reversedStr} (Reversal differs)`;
            verdict.className = 'mt-4 text-xs font-bold text-rose-400 font-mono';
        }
    }
}

// Sim 7: Reverse-and-Add Machine
function runReverseAndAdd(startNum) {
    const container = document.getElementById('revAddStepsContainer');
    const badge = document.getElementById('revAddStepsBadge');
    if (!container) return;
    
    container.innerHTML = '';
    let curr = startNum;
    let step = 0;
    const maxSteps = 8;
    
    while (step < maxSteps) {
        step++;
        const rev = parseInt(curr.toString().split('').reverse().join(''));
        const sum = curr + rev;
        const isPal = (sum.toString() === sum.toString().split('').reverse().join(''));
        
        const row = document.createElement('div');
        row.className = `p-2 rounded-lg border flex items-center justify-between ${
            isPal ? 'bg-emerald-950/60 border-emerald-500/60 text-emerald-200' : 'bg-slate-950/60 border-slate-800'
        }`;
        row.innerHTML = `
            <span>Step ${step}: ${curr} + ${rev} = <strong class="text-amber-300">${sum}</strong></span>
            <span>${isPal ? '✓ PALINDROME!' : 'Repeat →'}</span>
        `;
        container.appendChild(row);
        
        if (isPal) {
            if (badge) badge.innerText = `Reached Palindrome in ${step} Step${step > 1 ? 's' : ''}!`;
            return;
        }
        curr = sum;
    }
    if (badge) badge.innerText = `Stopped after ${maxSteps} steps`;
}

// Sim 8: Kaprekar's Routine
function runKaprekarRoutine(startNum) {
    const container = document.getElementById('kaprekarStepsContainer');
    const badge = document.getElementById('kaprekarStepsBadge');
    if (!container) return;
    
    container.innerHTML = '';
    let curr = startNum;
    let step = 0;
    
    while (step < 7) {
        step++;
        let digits = curr.toString().padStart(4, '0').split('');
        let desc = parseInt([...digits].sort((a, b) => b - a).join(''));
        let asc = parseInt([...digits].sort((a, b) => a - b).join(''));
        let diff = desc - asc;
        
        const row = document.createElement('div');
        row.className = `p-2 rounded-lg border flex items-center justify-between ${
            diff === 6174 ? 'bg-cyan-950/60 border-cyan-500/60 text-cyan-200 font-bold' : 'bg-slate-950/60 border-slate-800'
        }`;
        row.innerHTML = `
            <span>Step ${step}: ${desc} − ${String(asc).padStart(4, '0')} = <strong class="text-amber-300">${diff}</strong></span>
            <span>${diff === 6174 ? '🎯 6174 REACHED!' : 'Continue'}</span>
        `;
        container.appendChild(row);
        
        if (diff === 6174) {
            if (badge) badge.innerText = `Reached 6174 in ${step} Step${step > 1 ? 's' : ''}!`;
            return;
        }
        curr = diff;
    }
}

// Sim 9: Clock
function setClockDisplay(timeStr, label) {
    const disp = document.getElementById('digitalClockDisplay');
    const badge = document.getElementById('clockTypeBadge');
    const detail = document.getElementById('clockDetailsText');
    if (!disp) return;
    
    disp.innerText = timeStr;
    if (badge) badge.innerText = `${label}: ${timeStr}`;
    if (detail) detail.innerText = `Display mode: ${label} • Symmetrical beauty`;
}

// Sim 10: Mental Target
function setMentalTarget(tgt, expr) {
    const expElem = document.getElementById('mentalMathExpr');
    const badge = document.getElementById('targetStatusBadge');
    if (expElem) expElem.innerText = expr;
    if (badge) badge.innerText = `Target = ${tgt}`;
}

// Sim 11: Gauss Rainbow
function setGaussRange(n) {
    const arcGroup = document.getElementById('gaussArcsGroup');
    const numGroup = document.getElementById('gaussNumbersGroup');
    const badge = document.getElementById('gaussSumBadge');
    if (!arcGroup || !numGroup) return;
    
    arcGroup.innerHTML = '';
    numGroup.innerHTML = '';
    
    const count = n;
    const pairSum = count + 1;
    const totalPairs = count / 2;
    const totalSum = totalPairs * pairSum;
    
    const startX = 40;
    const gap = (400 - 80) / (count - 1);
    
    for (let i = 1; i <= count; i++) {
        const x = startX + (i - 1) * gap;
        const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        txt.setAttribute('x', x);
        txt.setAttribute('y', '200');
        txt.setAttribute('fill', '#e2e8f0');
        txt.setAttribute('font-size', '11');
        txt.setAttribute('font-weight', 'bold');
        txt.setAttribute('font-family', 'monospace');
        txt.setAttribute('text-anchor', 'middle');
        txt.textContent = i;
        numGroup.appendChild(txt);
    }
    
    const colors = ['#f59e0b', '#06b6d4', '#10b981', '#a855f7', '#ec4899'];
    for (let i = 1; i <= totalPairs; i++) {
        const x1 = startX + (i - 1) * gap;
        const x2 = startX + (count - i) * gap;
        const midX = (x1 + x2) / 2;
        const h = 40 + (totalPairs - i) * 20;
        
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', `M ${x1} 185 Q ${midX} ${185 - h} ${x2} 185`);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', colors[(i - 1) % colors.length]);
        path.setAttribute('stroke-width', '2');
        path.setAttribute('stroke-opacity', '0.7');
        arcGroup.appendChild(path);
    }
    
    if (badge) badge.innerText = `Sum 1 to ${n} = ${totalPairs} × ${pairSum} = ${totalSum}`;
}

// Sim 12: Collatz Graph
function runCollatzGraph(startN) {
    const path = document.getElementById('collatzPath');
    const dots = document.getElementById('collatzDotsGroup');
    const badge = document.getElementById('collatzPeakBadge');
    if (!path || !dots) return;
    
    dots.innerHTML = '';
    let curr = startN;
    const seq = [curr];
    while (curr !== 1 && seq.length < 30) {
        if (curr % 2 === 0) curr = curr / 2;
        else curr = 3 * curr + 1;
        seq.push(curr);
    }
    
    const maxVal = Math.max(...seq);
    const startX = 35, endX = 370;
    const startY = 205, endY = 40;
    const xStep = (endX - startX) / (seq.length - 1);
    
    let d = '';
    for (let i = 0; i < seq.length; i++) {
        const x = startX + i * xStep;
        const y = startY - ((seq[i] - 1) / (maxVal - 1 || 1)) * (startY - endY);
        if (i === 0) d += `M ${x} ${y}`;
        else d += ` L ${x} ${y}`;
        
        const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        dot.setAttribute('cx', x);
        dot.setAttribute('cy', y);
        dot.setAttribute('r', '3.5');
        dot.setAttribute('fill', '#38bdf8');
        dots.appendChild(dot);
    }
    path.setAttribute('d', d);
    if (badge) badge.innerText = `Start ${startN}: Peak ${maxVal}, Steps ${seq.length - 1}`;
}

// Sim 13: Estimation
function setEstimationScenario(type) {
    const title = document.getElementById('estScenarioTitle');
    const formula = document.getElementById('estFormulaText');
    const comp = document.getElementById('estComparisonText');
    const badge = document.getElementById('estContextBadge');
    
    if (type === 'steps') {
        if (title) title.innerText = 'How many steps do you take in 1 year?';
        if (formula) formula.innerText = '8,000 steps/day × 365 days ≈ 3,000,000 steps';
        if (comp) comp.innerText = 'Distance: 3,000,000 × 0.6 m ≈ 1,800 kilometers!';
        if (badge) badge.innerText = 'Daily Steps Estimation';
    } else if (type === 'heartbeats') {
        if (title) title.innerText = 'How many heartbeats in a single day?';
        if (formula) formula.innerText = '70 bpm × 60 min × 24 hr ≈ 100,000 beats/day';
        if (comp) comp.innerText = 'In 1 Year: 100,000 × 365 ≈ 36.5 Million beats!';
        if (badge) badge.innerText = 'Heartbeats Estimation';
    } else if (type === 'books') {
        if (title) title.innerText = 'Total cost of 19 books at ₹48 each?';
        if (formula) formula.innerText = 'Round: 20 books × ₹50 = ₹1,000';
        if (comp) comp.innerText = 'Exact is ₹912 (Estimation is within 10%!)';
        if (badge) badge.innerText = 'Book Purchasing Estimation';
    }
}

// Sim 14: Game of 21
let game21Total = 0;
function playGame21Move(num) {
    if (game21Total >= 20) return;
    game21Total += num;
    updateGame21Display();
    
    if (game21Total >= 20) {
        document.getElementById('game21AdviceText').innerText = '🎉 Target 20 hit! Opponent is forced to say 21!';
        return;
    }
    
    // Opponent AI responds
    setTimeout(() => {
        let aiMove = 1;
        const targetMultiples = [4, 8, 12, 16, 20];
        const nextMilestone = targetMultiples.find(m => m > game21Total);
        if (nextMilestone) {
            const diff = nextMilestone - game21Total;
            if (diff >= 1 && diff <= 3) aiMove = diff;
            else aiMove = 1;
        }
        game21Total += aiMove;
        updateGame21Display();
    }, 600);
}

function updateGame21Display() {
    const numDisp = document.getElementById('game21CurrentNumber');
    const badge = document.getElementById('game21TurnBadge');
    const advice = document.getElementById('game21AdviceText');
    if (numDisp) numDisp.innerText = game21Total;
    if (badge) badge.innerText = `Current Total: ${game21Total}`;
    if (advice && game21Total < 20) {
        advice.innerText = `Total is ${game21Total}. Add 1, 2, or 3 to aim for next multiple of 4!`;
    }
}

function resetGame21() {
    game21Total = 0;
    updateGame21Display();
    const advice = document.getElementById('game21AdviceText');
    if (advice) advice.innerText = 'Your Turn: Pick 1, 2, or 3 numbers!';
}

// Sim 15: Race to 99
let race99Total = 0;
function playRace99Move(num) {
    if (race99Total >= 99) return;
    race99Total += num;
    updateRace99Display();
    
    if (race99Total >= 99) {
        document.getElementById('race99ScoreBadge').innerText = '🎉 99 Reached! You Win!';
        return;
    }
    
    // Opponent AI responds
    setTimeout(() => {
        const milestones = [11, 22, 33, 44, 55, 66, 77, 88, 99];
        const nextTarget = milestones.find(m => m > race99Total);
        let aiAdd = 5;
        if (nextTarget) {
            const diff = nextTarget - race99Total;
            if (diff >= 1 && diff <= 10) aiAdd = diff;
            else aiAdd = 1;
        }
        race99Total += aiAdd;
        updateRace99Display();
    }, 600);
}

function updateRace99Display() {
    const disp = document.getElementById('race99CurrentTotal');
    const bar = document.getElementById('race99Progress');
    const badge = document.getElementById('race99ScoreBadge');
    if (disp) disp.innerText = `${race99Total} / 99`;
    if (bar) bar.style.width = `${Math.min(100, (race99Total / 99) * 100)}%`;
    if (badge) badge.innerText = `Current Score: ${race99Total}`;
}

function resetRace99() {
    race99Total = 0;
    updateRace99Display();
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

    code = f'''"""NCERT Class 6 Mathematics Chapter 3: Number Play JavaScript Module."""

INTERACTIVE_JS = """{js_content}"""
'''

    # Strict check for zero raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in JavaScript module!")

    # Check for surrogates
    clean_chars = [ch for ch in code if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_code = ''.join(clean_chars)

    with open(".agents/class6_math_number_play_js.py", "w", encoding="utf-8") as f:
        f.write(clean_code)

    print("Successfully generated .agents/class6_math_number_play_js.py.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in JS module!")

if __name__ == "__main__":
    generate_js()

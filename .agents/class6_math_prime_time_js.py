"""NCERT Class 6 Mathematics Chapter 5: Prime Time JavaScript Module."""

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
    if (currentSlide === 1) updateIdliVadaDisplay();
    else if (currentSlide === 2) setVennPair(4, 6);
    else if (currentSlide === 3) setJumpTarget(18);
    else if (currentSlide === 4) testPerfectNumber(6);
    else if (currentSlide === 5) packFigs(7);
    else if (currentSlide === 6) initSieveGrid();
    else if (currentSlide === 7) selectTwinPair(11, 13);
    else if (currentSlide === 8) testVaultPair(4, 9);
    else if (currentSlide === 9) setThreadStep(3);
    else if (currentSlide === 10) setTheoPair(5, 7);
    else if (currentSlide === 11) buildFactorTree(56);
    else if (currentSlide === 12) setDnaTarget(36);
    else if (currentSlide === 13) testPantryDivisor(14);
    else if (currentSlide === 14) scanNumber(3480);
    else if (currentSlide === 15) scan48Number(7536);
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

// Sim 1: Idli-Vada Game Simulator
let idliVadaCount = 1;

function updateIdliVadaDisplay() {
    const numDisplay = document.getElementById('idliVadaNum');
    const textDisplay = document.getElementById('idliVadaCallText');
    const badge = document.getElementById('idliVadaCallBadge');
    if (!numDisplay || !textDisplay) return;
    
    numDisplay.innerText = idliVadaCount;
    
    const is3 = (idliVadaCount % 3 === 0);
    const is5 = (idliVadaCount % 5 === 0);
    
    if (is3 && is5) {
        textDisplay.innerHTML = '<span class="text-emerald-300 font-black text-lg">🥟🥞 IDLI-VADA!</span>';
        textDisplay.className = 'text-base font-bold py-1 px-4 rounded-xl bg-emerald-950/80 border border-emerald-500/60 min-h-[36px] flex items-center justify-center animate-pulse';
        if (badge) badge.innerText = `Call: IDLI-VADA (${idliVadaCount} ÷ 15)`;
    } else if (is3) {
        textDisplay.innerHTML = '<span class="text-amber-300 font-black">🥟 IDLI! (Multiple of 3)</span>';
        textDisplay.className = 'text-base font-bold py-1 px-4 rounded-xl bg-amber-950/70 border border-amber-500/50 min-h-[36px] flex items-center justify-center';
        if (badge) badge.innerText = `Call: IDLI (${idliVadaCount} ÷ 3)`;
    } else if (is5) {
        textDisplay.innerHTML = '<span class="text-cyan-300 font-black">🥞 VADA! (Multiple of 5)</span>';
        textDisplay.className = 'text-base font-bold py-1 px-4 rounded-xl bg-cyan-950/70 border border-cyan-500/50 min-h-[36px] flex items-center justify-center';
        if (badge) badge.innerText = `Call: VADA (${idliVadaCount} ÷ 5)`;
    } else {
        textDisplay.innerHTML = `<span class="text-slate-300 font-mono">Regular Count: ${idliVadaCount}</span>`;
        textDisplay.className = 'text-base font-bold text-slate-300 py-1 px-4 rounded-xl bg-slate-900/80 border border-slate-800 min-h-[36px] flex items-center justify-center';
        if (badge) badge.innerText = `Call: Say Number (${idliVadaCount})`;
    }
}

function stepIdliVada(step) {
    idliVadaCount += step;
    updateIdliVadaDisplay();
}

function jumpToNextIdliVada() {
    idliVadaCount += (15 - (idliVadaCount % 15));
    if (idliVadaCount % 15 !== 0) idliVadaCount = 15;
    updateIdliVadaDisplay();
}

function resetIdliVada() {
    idliVadaCount = 1;
    updateIdliVadaDisplay();
}

// Sim 2: Overlapping Circles (Venn Diagram)
function gcd(a, b) {
    while (b) {
        let t = b;
        b = a % b;
        a = t;
    }
    return a;
}

function lcm(a, b) {
    return (a * b) / gcd(a, b);
}

function setVennPair(a, b) {
    const badge = document.getElementById('venmLcmBadge');
    const labelA = document.getElementById('vennLabelA');
    const labelB = document.getElementById('vennLabelB');
    const numbersGroup = document.getElementById('vennNumbersGroup');
    if (!numbersGroup) return;
    
    const theLcm = lcm(a, b);
    if (badge) badge.innerText = `LCM(${a}, ${b}) = ${theLcm}`;
    if (labelA) labelA.innerText = `Multiples of ${a}`;
    if (labelB) labelB.innerText = `Multiples of ${b}`;
    
    let html = '';
    
    // Left circle exclusive (multiples of a but not b, up to 48)
    let leftCount = 0;
    for (let m = a; m <= 48 && leftCount < 4; m += a) {
        if (m % b !== 0) {
            const y = 70 + leftCount * 22;
            html += `<text x="110" y="${y}" fill="#38bdf8" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">${m}</text>`;
            leftCount++;
        }
    }
    
    // Right circle exclusive (multiples of b but not a, up to 48)
    let rightCount = 0;
    for (let m = b; m <= 48 && rightCount < 4; m += b) {
        if (m % a !== 0) {
            const y = 70 + rightCount * 22;
            html += `<text x="270" y="${y}" fill="#fbbf24" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">${m}</text>`;
            rightCount++;
        }
    }
    
    // Overlap center (multiples of both)
    let centerCount = 0;
    for (let m = theLcm; m <= 100 && centerCount < 3; m += theLcm) {
        const y = 80 + centerCount * 25;
        html += `
            <text x="190" y="${y}" fill="#34d399" font-size="13" font-weight="black" font-family="monospace" text-anchor="middle">${m}</text>
        `;
        centerCount++;
    }
    
    numbersGroup.innerHTML = html;
}

// Sim 3: Jump Jackpot (Factor Jumping Game)
let currentJumpTarget = 18;

function setJumpTarget(t) {
    currentJumpTarget = t;
    const badge = document.getElementById('jumpFeedbackBadge');
    const factorsList = document.getElementById('jumpFactorsList');
    if (badge) badge.innerText = `Target: ${t} • Choose Jump Size`;
    
    // Calculate factors
    const fArr = [];
    for (let i = 1; i <= t; i++) {
        if (t % i === 0) fArr.push(i);
    }
    if (factorsList) factorsList.innerText = fArr.join(', ');
    
    drawJumpLine(0);
}

function drawJumpLine(jumpStep) {
    const ticksGroup = document.getElementById('jumpTicksGroup');
    const arcsGroup = document.getElementById('jumpArcsGroup');
    if (!ticksGroup || !arcsGroup) return;
    
    const xStart = 30;
    const xEnd = 350;
    const t = currentJumpTarget;
    
    // Draw Ticks
    let ticksHtml = '';
    for (let i = 0; i <= t; i++) {
        const x = xStart + (i / t) * (xEnd - xStart);
        const isMajor = (i === 0 || i === t || (t <= 20) || (i % 5 === 0));
        ticksHtml += `
            <line x1="${x}" y1="75" x2="${x}" y2="${isMajor ? '85' : '80'}" stroke="#94a3b8" stroke-width="1.5"/>
            ${isMajor ? `<text x="${x}" y="95" fill="#cbd5e1" font-size="9" text-anchor="middle" font-family="monospace">${i}</text>` : ''}
        `;
    }
    // Highlight Target
    ticksHtml += `
        <circle cx="${xEnd}" cy="80" r="4" fill="#f59e0b"/>
        <text x="${xEnd}" y="65" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">TARGET</text>
    `;
    ticksGroup.innerHTML = ticksHtml;
    
    // Draw Arcs
    if (jumpStep <= 0) {
        arcsGroup.innerHTML = '';
        return;
    }
    
    let arcsHtml = '';
    let currentX = 0;
    let stepCount = 0;
    const isFactor = (t % jumpStep === 0);
    const strokeColor = isFactor ? '#10b981' : '#f43f5e';
    
    while (currentX < t) {
        const nextX = currentX + jumpStep;
        const x1 = xStart + (currentX / t) * (xEnd - xStart);
        const x2 = xStart + (Math.min(nextX, t * 1.1) / t) * (xEnd - xStart);
        const midX = (x1 + x2) / 2;
        const arcHeight = Math.min(45, 10 + jumpStep * 2.5);
        const yTop = 80 - arcHeight;
        
        arcsHtml += `
            <path d="M ${x1} 80 Q ${midX} ${yTop} ${x2} 80" fill="none" stroke="${strokeColor}" stroke-width="2" stroke-linecap="round"/>
        `;
        currentX = nextX;
        stepCount++;
        if (stepCount > 25) break;
    }
    arcsGroup.innerHTML = arcsHtml;
}

function executeJump(step) {
    const badge = document.getElementById('jumpFeedbackBadge');
    const isFactor = (currentJumpTarget % step === 0);
    drawJumpLine(step);
    
    if (isFactor) {
        if (badge) {
            badge.innerText = `🎉 JACKPOT! Step ${step} divides ${currentJumpTarget} exactly (${step} × ${currentJumpTarget/step})!`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
    } else {
        const rem = currentJumpTarget % step;
        if (badge) {
            badge.innerText = `💥 OVERSHOT! Step ${step} misses target (leaves remainder ${rem})!`;
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
    }
}

// Sim 4: Perfect Number Divisor Scale
function testPerfectNumber(n) {
    const badge = document.getElementById('perfectScaleBadge');
    const formulaDisplay = document.getElementById('perfectFormulaDisplay');
    const numVal = document.getElementById('perfectNumberVal');
    const sumVal = document.getElementById('perfectSumVal');
    const totalVal = document.getElementById('perfectTotalVal');
    const statusText = document.getElementById('perfectStatusText');
    
    const propFactors = [];
    for (let i = 1; i < n; i++) {
        if (n % i === 0) propFactors.push(i);
    }
    const sumProp = propFactors.reduce((acc, c) => acc + c, 0);
    const sumAll = sumProp + n;
    
    if (numVal) numVal.innerText = n;
    if (sumVal) sumVal.innerText = sumProp;
    if (totalVal) totalVal.innerText = `${sumAll} (${sumAll === 2*n ? '2 × ' + n : '≠ 2 × ' + n})`;
    
    if (formulaDisplay) formulaDisplay.innerText = `Proper Divisors: ${propFactors.join(' + ')} = ${sumProp}`;
    
    if (sumProp === n) {
        if (badge) {
            badge.innerText = `N = ${n} • PERFECT NUMBER`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        if (statusText) statusText.innerHTML = '⭐ Perfect Harmony: Sum of proper factors exactly equals the number itself!';
        statusText.className = 'mt-3 text-xs text-emerald-300 font-medium';
    } else if (sumProp > n) {
        if (badge) {
            badge.innerText = `N = ${n} • ABUNDANT NUMBER`;
            badge.className = 'font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40';
        }
        if (statusText) statusText.innerHTML = `Divisor sum (${sumProp}) exceeds ${n} (Abundant number).`;
        statusText.className = 'mt-3 text-xs text-cyan-300 font-medium';
    } else {
        if (badge) {
            badge.innerText = `N = ${n} • DEFICIENT NUMBER`;
            badge.className = 'font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40';
        }
        if (statusText) statusText.innerHTML = `Divisor sum (${sumProp}) falls short of ${n} (Deficient number).`;
        statusText.className = 'mt-3 text-xs text-amber-300 font-medium';
    }
}

// Sim 5: Rectangular Array Fig Packer
function packFigs(n) {
    const badge = document.getElementById('figPackBadge');
    const container = document.getElementById('figGridContainer');
    const explain = document.getElementById('figExplainText');
    if (!container) return;
    
    const factorPairs = [];
    for (let r = 1; r <= Math.sqrt(n); r++) {
        if (n % r === 0) {
            factorPairs.push({ rows: r, cols: n / r });
        }
    }
    
    let html = '';
    factorPairs.forEach(pair => {
        let dotsHtml = '';
        for (let r = 0; r < pair.rows; r++) {
            dotsHtml += '<div class="flex gap-1">';
            for (let c = 0; c < pair.cols; c++) {
                dotsHtml += '<span class="w-3.5 h-3.5 rounded-full bg-amber-400 shadow-sm inline-block"></span>';
            }
            dotsHtml += '</div>';
        }
        html += `
            <div class="flex flex-col items-center p-2 rounded-xl bg-slate-900 border border-slate-700">
                <span class="text-[10px] font-mono text-slate-400 mb-1.5">${pair.rows} × ${pair.cols} Grid</span>
                <div class="space-y-1">${dotsHtml}</div>
            </div>
        `;
    });
    container.innerHTML = html;
    
    if (n === 1) {
        if (badge) {
            badge.innerText = '1 Fig: NEITHER PRIME NOR COMPOSITE';
            badge.className = 'font-mono text-slate-300 bg-slate-800 px-2 py-0.5 rounded border border-slate-700';
        }
        if (explain) explain.innerText = 'Only 1 dot. Fails the requirement of having two distinct factors. Neither prime nor composite.';
    } else if (factorPairs.length === 1 && factorPairs[0].rows === 1) {
        if (badge) {
            badge.innerText = `${n} Figs: PRIME NUMBER`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        if (explain) explain.innerText = `Only 1 arrangement possible (1 × ${n}). ${n} has exactly two factors (1 and ${n}). Prime!`;
    } else {
        if (badge) {
            badge.innerText = `${n} Figs: COMPOSITE NUMBER`;
            badge.className = 'font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40';
        }
        if (explain) explain.innerText = `Multiple rectangular arrangements possible! ${n} has more than two factors. Composite!`;
    }
}

// Sim 6: Sieve of Eratosthenes Interactive Grid (1 to 100)
let sieveStep = 0;
const primeSet100 = new Set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]);

function initSieveGrid() {
    sieveStep = 0;
    renderSieveState();
}

function advanceSieve() {
    if (sieveStep < 5) sieveStep++;
    renderSieveState();
}

function revealAllPrimes() {
    sieveStep = 5;
    renderSieveState();
}

function resetSieve() {
    sieveStep = 0;
    renderSieveState();
}

function renderSieveState() {
    const grid = document.getElementById('sieveGrid');
    const badge = document.getElementById('sieveStepBadge');
    if (!grid) return;
    
    const descriptions = [
        'Step 0: Grid 1 to 100',
        'Step 1: Cross out 1 (Neither)',
        'Step 2: Circle 2, cross multiples of 2',
        'Step 3: Circle 3, cross multiples of 3',
        'Step 4: Circle 5, cross multiples of 5',
        'Step 5: Circle 7, all 25 Primes revealed!'
    ];
    if (badge) badge.innerText = descriptions[sieveStep];
    
    let html = '';
    for (let i = 1; i <= 100; i++) {
        let cls = 'bg-slate-900 border border-slate-800 text-slate-300 rounded p-1';
        
        if (i === 1 && sieveStep >= 1) {
            cls = 'bg-slate-950 text-slate-600 line-through rounded p-1 border border-slate-900';
        } else if (i === 2 && sieveStep >= 2) {
            cls = 'bg-amber-500 text-slate-950 font-bold rounded p-1 shadow-md';
        } else if (i % 2 === 0 && sieveStep >= 2) {
            cls = 'bg-slate-950/80 text-slate-600 line-through rounded p-1';
        } else if (i === 3 && sieveStep >= 3) {
            cls = 'bg-amber-500 text-slate-950 font-bold rounded p-1 shadow-md';
        } else if (i % 3 === 0 && sieveStep >= 3) {
            cls = 'bg-slate-950/80 text-slate-600 line-through rounded p-1';
        } else if (i === 5 && sieveStep >= 4) {
            cls = 'bg-amber-500 text-slate-950 font-bold rounded p-1 shadow-md';
        } else if (i % 5 === 0 && sieveStep >= 4) {
            cls = 'bg-slate-950/80 text-slate-600 line-through rounded p-1';
        } else if (i === 7 && sieveStep >= 5) {
            cls = 'bg-amber-500 text-slate-950 font-bold rounded p-1 shadow-md';
        } else if (i % 7 === 0 && sieveStep >= 5) {
            cls = 'bg-slate-950/80 text-slate-600 line-through rounded p-1';
        } else if (sieveStep === 5 && primeSet100.has(i)) {
            cls = 'bg-emerald-500 text-slate-950 font-bold rounded p-1 shadow-md';
        }
        
        html += `<div class="${cls}">${i}</div>`;
    }
    grid.innerHTML = html;
}

// Sim 7: Twin Prime Detector & Explorer
function selectTwinPair(p1, p2) {
    const badge = document.getElementById('twinFeedbackBadge');
    const p1Box = document.getElementById('twinP1');
    const p2Box = document.getElementById('twinP2');
    const midBox = document.getElementById('twinMiddleEven');
    const explain = document.getElementById('twinExplainBox');
    
    if (badge) badge.innerText = `Selected: (${p1}, ${p2})`;
    if (p1Box) p1Box.querySelector('.text-xl').innerText = p1;
    if (p2Box) p2Box.querySelector('.text-xl').innerText = p2;
    
    const mid = (p1 + p2) / 2;
    const isMid6 = (mid % 6 === 0);
    if (midBox) midBox.innerText = `Mid: ${mid} ${isMid6 ? '(÷ 6)' : ''}`;
    
    const sophie1 = (2 * p1 + 1);
    const isSophiePrime = primeSet100.has(sophie1);
    
    if (explain) {
        explain.innerHTML = `
            Twin primes have difference 2 (${p2} − ${p1} = 2). Sandwiched even number is <strong>${mid}</strong>${isMid6 ? ' (divisible by 6!)' : ''}.<br>
            <span class="text-cyan-300">Sophie Germain Test for ${p1}: 2(${p1}) + 1 = <strong>${sophie1}</strong> (${isSophiePrime ? 'Prime! ✓' : 'Composite'}).</span>
        `;
    }
}

// Sim 8: Co-prime Lock & Key Vault
function testVaultPair(a, b) {
    const badge = document.getElementById('vaultStatusBadge');
    const numA = document.getElementById('vaultNumA');
    const numB = document.getElementById('vaultNumB');
    const factorsA = document.getElementById('vaultFactorsA');
    const factorsB = document.getElementById('vaultFactorsB');
    const graphic = document.getElementById('vaultGraphic');
    const msg = document.getElementById('vaultMessage');
    
    const fA = [];
    for (let i = 1; i <= a; i++) if (a % i === 0) fA.push(i);
    const fB = [];
    for (let i = 1; i <= b; i++) if (b % i === 0) fB.push(i);
    
    if (numA) numA.innerText = `Number A: ${a}`;
    if (numB) numB.innerText = `Number B: ${b}`;
    if (factorsA) factorsA.innerText = `{${fA.join(', ')}}`;
    if (factorsB) factorsB.innerText = `{${fB.join(', ')}}`;
    
    const common = fA.filter(x => fB.includes(x));
    const isCoPrime = (common.length === 1 && common[0] === 1);
    
    if (isCoPrime) {
        if (badge) {
            badge.innerText = `HCF(${a}, ${b}) = 1 • UNLOCKED`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        if (graphic) graphic.innerText = '🔓';
        if (msg) {
            msg.innerText = `Common factor is ONLY {1}. Both numbers are CO-PRIME!`;
            msg.className = 'text-xs text-emerald-300 font-medium';
        }
    } else {
        if (badge) {
            badge.innerText = `HCF(${a}, ${b}) = ${common[common.length-1]} • LOCKED`;
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
        if (graphic) graphic.innerText = '🔒';
        if (msg) {
            msg.innerText = `Shared factors: {${common.join(', ')}}. NOT co-prime!`;
            msg.className = 'text-xs text-rose-300 font-medium';
        }
    }
}

// Sim 9: Circular Thread-Art Peg Star Simulator
function setThreadStep(k) {
    const badge = document.getElementById('threadStarBadge');
    const linesGroup = document.getElementById('threadLinesGroup');
    const pegsGroup = document.getElementById('threadPegsGroup');
    if (!linesGroup || !pegsGroup) return;
    
    const N = 8;
    const g = gcd(N, k);
    const isCoPrime = (g === 1);
    
    if (badge) {
        if (isCoPrime) {
            badge.innerText = `N = ${N}, Step = ${k} (Continuous Star!)`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        } else {
            badge.innerText = `N = ${N}, Step = ${k} (Sub-loop: ${N/g} pegs)`;
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
    }
    
    const cx = 110, cy = 110, r = 80;
    const pegCoords = [];
    for (let i = 0; i < N; i++) {
        const angle = (i / N) * 2 * Math.PI - Math.PI / 2;
        pegCoords.push({
            x: cx + r * Math.cos(angle),
            y: cy + r * Math.sin(angle)
        });
    }
    
    // Draw Pegs
    let pegsHtml = '';
    pegCoords.forEach((pt, idx) => {
        pegsHtml += `
            <circle cx="${pt.x}" cy="${pt.y}" r="5" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
            <text x="${pt.x + (pt.x > cx ? 12 : -12)}" y="${pt.y + 4}" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">${idx}</text>
        `;
    });
    pegsGroup.innerHTML = pegsHtml;
    
    // Draw Thread
    let linesHtml = '';
    const strokeColor = isCoPrime ? '#10b981' : '#f43f5e';
    
    let visited = 0;
    let curr = 0;
    while (visited < N) {
        const nxt = (curr + k) % N;
        const p1 = pegCoords[curr];
        const p2 = pegCoords[nxt];
        linesHtml += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${strokeColor}" stroke-width="2" stroke-linecap="round"/>`;
        curr = nxt;
        visited++;
        if (curr === 0) break;
    }
    linesGroup.innerHTML = linesHtml;
}

// Sim 10: Co-prime LCM & Product Calculator
function setTheoPair(a, b) {
    const badge = document.getElementById('lcmTheoremBadge');
    const hcfVal = document.getElementById('theoHcfVal');
    const lcmVal = document.getElementById('theoLcmVal');
    const prodVal = document.getElementById('theoProdVal');
    const eq = document.getElementById('theoEquation');
    const tag = document.getElementById('theoCoPrimeTag');
    
    const g = gcd(a, b);
    const l = (a * b) / g;
    const prod = a * b;
    const isCoPrime = (g === 1);
    
    if (hcfVal) hcfVal.innerText = g;
    if (lcmVal) lcmVal.innerText = l;
    if (prodVal) prodVal.innerText = prod;
    if (eq) eq.innerText = `${g} × ${l} = ${a} × ${b} (= ${prod})`;
    
    if (badge) badge.innerText = `LCM(${a}, ${b}) = ${l} (HCF = ${g})`;
    
    if (tag) {
        if (isCoPrime) {
            tag.innerText = `✓ Co-prime (HCF = 1): LCM is exactly the direct product a × b!`;
            tag.className = 'mt-2 text-xs text-emerald-400 font-bold';
        } else {
            tag.innerText = `⚠️ Shared factor ${g} (HCF > 1): LCM (${l}) is less than product (${prod})!`;
            tag.className = 'mt-2 text-xs text-amber-400 font-bold';
        }
    }
}

// Sim 11: Interactive Factor Tree Builder
function buildFactorTree(n) {
    const badge = document.getElementById('factorTreeBadge');
    const linesGroup = document.getElementById('treeLinesGroup');
    const nodesGroup = document.getElementById('treeNodesGroup');
    if (!linesGroup || !nodesGroup) return;
    
    // Preset factor trees
    const treeDefs = {
        56: {
            root: 56,
            exp: '56 = 2³ × 7',
            nodes: [
                { id: '56', val: 56, x: 160, y: 30, prime: false },
                { id: '7', val: 7, x: 90, y: 80, prime: true, parent: '56' },
                { id: '8', val: 8, x: 230, y: 80, prime: false, parent: '56' },
                { id: '2a', val: 2, x: 180, y: 130, prime: true, parent: '8' },
                { id: '4', val: 4, x: 270, y: 130, prime: false, parent: '8' },
                { id: '2b', val: 2, x: 240, y: 180, prime: true, parent: '4' },
                { id: '2c', val: 2, x: 300, y: 180, prime: true, parent: '4' }
            ]
        },
        72: {
            root: 72,
            exp: '72 = 2³ × 3²',
            nodes: [
                { id: '72', val: 72, x: 160, y: 30, prime: false },
                { id: '8', val: 8, x: 90, y: 80, prime: false, parent: '72' },
                { id: '9', val: 9, x: 230, y: 80, prime: false, parent: '72' },
                { id: '2a', val: 2, x: 50, y: 130, prime: true, parent: '8' },
                { id: '4', val: 4, x: 120, y: 130, prime: false, parent: '8' },
                { id: '3a', val: 3, x: 200, y: 130, prime: true, parent: '9' },
                { id: '3b', val: 3, x: 260, y: 130, prime: true, parent: '9' },
                { id: '2b', val: 2, x: 90, y: 180, prime: true, parent: '4' },
                { id: '2c', val: 2, x: 140, y: 180, prime: true, parent: '4' }
            ]
        },
        84: {
            root: 84,
            exp: '84 = 2² × 3 × 7',
            nodes: [
                { id: '84', val: 84, x: 160, y: 30, prime: false },
                { id: '4', val: 4, x: 90, y: 80, prime: false, parent: '84' },
                { id: '21', val: 21, x: 230, y: 80, prime: false, parent: '84' },
                { id: '2a', val: 2, x: 60, y: 140, prime: true, parent: '4' },
                { id: '2b', val: 2, x: 120, y: 140, prime: true, parent: '4' },
                { id: '3', val: 3, x: 200, y: 140, prime: true, parent: '21' },
                { id: '7', val: 7, x: 260, y: 140, prime: true, parent: '21' }
            ]
        },
        60: {
            root: 60,
            exp: '60 = 2² × 3 × 5',
            nodes: [
                { id: '60', val: 60, x: 160, y: 30, prime: false },
                { id: '6', val: 6, x: 90, y: 80, prime: false, parent: '60' },
                { id: '10', val: 10, x: 230, y: 80, prime: false, parent: '60' },
                { id: '2a', val: 2, x: 60, y: 140, prime: true, parent: '6' },
                { id: '3', val: 3, x: 120, y: 140, prime: true, parent: '6' },
                { id: '2b', val: 2, x: 200, y: 140, prime: true, parent: '10' },
                { id: '5', val: 5, x: 260, y: 140, prime: true, parent: '10' }
            ]
        }
    };
    
    const tree = treeDefs[n] || treeDefs[56];
    if (badge) badge.innerText = tree.exp;
    
    let linesHtml = '';
    let nodesHtml = '';
    
    const nodeMap = {};
    tree.nodes.forEach(nd => { nodeMap[nd.id] = nd; });
    
    tree.nodes.forEach(nd => {
        if (nd.parent && nodeMap[nd.parent]) {
            const p = nodeMap[nd.parent];
            linesHtml += `<line x1="${p.x}" y1="${p.y}" x2="${nd.x}" y2="${nd.y}" stroke="#475569" stroke-width="1.5"/>`;
        }
        
        const fill = nd.prime ? '#10b981' : '#334155';
        const stroke = nd.prime ? '#34d399' : '#64748b';
        const textFill = nd.prime ? '#042f2e' : '#f1f5f9';
        
        nodesHtml += `
            <circle cx="${nd.x}" cy="${nd.y}" r="14" fill="${fill}" stroke="${stroke}" stroke-width="2"/>
            <text x="${nd.x}" y="${nd.y + 4}" fill="${textFill}" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">${nd.val}</text>
        `;
    });
    
    linesGroup.innerHTML = linesHtml;
    nodesGroup.innerHTML = nodesHtml;
}

// Sim 12: Fundamental Theorem DNA Sorter
let currentDnaTarget = 36;
let currentDnaBeads = [2, 2, 3, 3];

function setDnaTarget(n) {
    currentDnaTarget = n;
    const badge = document.getElementById('dnaNumBadge');
    if (badge) badge.innerText = `Target: ${n}`;
    
    if (n === 36) currentDnaBeads = [2, 2, 3, 3];
    else if (n === 90) currentDnaBeads = [2, 3, 3, 5];
    else if (n === 60) currentDnaBeads = [2, 2, 3, 5];
    
    renderDnaBeads();
}

function shuffleDnaBeads() {
    for (let i = currentDnaBeads.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [currentDnaBeads[i], currentDnaBeads[j]] = [currentDnaBeads[j], currentDnaBeads[i]];
    }
    renderDnaBeads();
}

function renderDnaBeads() {
    const row = document.getElementById('dnaBeadsRow');
    const result = document.getElementById('dnaProductResult');
    if (!row) return;
    
    let html = '';
    currentDnaBeads.forEach(b => {
        html += `
            <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-amber-500 to-yellow-300 text-slate-950 font-black font-mono flex items-center justify-center text-sm shadow-md border border-amber-200">
                ${b}
            </div>
        `;
    });
    row.innerHTML = html;
    
    const prodStr = currentDnaBeads.join(' × ');
    if (result) result.innerText = `${prodStr} = ${currentDnaTarget}`;
}

// Sim 13: Factor Pantry Divisibility Tester
function testPantryDivisor(b) {
    const badge = document.getElementById('pantryResultBadge');
    const divLabel = document.getElementById('pantryDivisorLabel');
    const divFactorsBox = document.getElementById('pantryFactorsB');
    const explain = document.getElementById('pantryStatusExplanation');
    
    if (divLabel) divLabel.innerText = b;
    if (!divFactorsBox) return;
    
    // Target A = 84 = [2, 2, 3, 7]
    const bFactorsMap = {
        14: { factors: [2, 7], div: true, exp: "✓ Both '2' and '7' are inside 84! Exactly divisible (84 ÷ 14 = 6)." },
        12: { factors: [2, 2, 3], div: true, exp: "✓ Two '2's and one '3' are inside 84! Exactly divisible (84 ÷ 12 = 7)." },
        8: { factors: [2, 2, 2], div: false, exp: "✗ 8 needs three '2's, but 84 only has two '2's! Missing one '2'." },
        15: { factors: [3, 5], div: false, exp: "✗ 15 needs '5', but 84 has no factor of 5! Not divisible." }
    };
    
    const item = bFactorsMap[b] || bFactorsMap[14];
    
    let html = '';
    item.factors.forEach(f => {
        html += `<span class="px-2 py-0.5 rounded bg-slate-800 text-cyan-300 font-bold">${f}</span>`;
    });
    divFactorsBox.innerHTML = html;
    
    if (badge) {
        if (item.div) {
            badge.innerText = `84 is divisible by ${b} (✓)`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        } else {
            badge.innerText = `84 is NOT divisible by ${b} (✗)`;
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
    }
    
    if (explain) {
        explain.innerText = item.exp;
        explain.className = item.div ? 'text-emerald-300 text-center font-medium' : 'text-rose-300 text-center font-medium';
    }
}

// Sim 14: Last Digit Divisibility Scanner (2, 5, 10)
function scanNumber(num) {
    const badge = document.getElementById('scannerInputBadge');
    const pfx = document.getElementById('scanPrefix');
    const last = document.getElementById('scanLastDigit');
    const r2 = document.getElementById('rule2Result');
    const r5 = document.getElementById('rule5Result');
    const r10 = document.getElementById('rule10Result');
    
    const str = num.toString();
    const lastDigit = parseInt(str.slice(-1));
    const prefixStr = str.slice(0, -1);
    
    if (badge) badge.innerText = `Number: ${num.toLocaleString()}`;
    if (pfx) pfx.innerText = prefixStr;
    if (last) last.innerText = lastDigit;
    
    const is2 = (lastDigit % 2 === 0);
    const is5 = (lastDigit === 0 || lastDigit === 5);
    const is10 = (lastDigit === 0);
    
    if (r2) {
        r2.innerText = is2 ? '✓ Yes' : '✗ No';
        r2.className = is2 ? 'font-bold text-emerald-400 text-sm mt-0.5' : 'font-bold text-rose-400 text-sm mt-0.5';
    }
    if (r5) {
        r5.innerText = is5 ? '✓ Yes' : '✗ No';
        r5.className = is5 ? 'font-bold text-emerald-400 text-sm mt-0.5' : 'font-bold text-rose-400 text-sm mt-0.5';
    }
    if (r10) {
        r10.innerText = is10 ? '✓ Yes' : '✗ No';
        r10.className = is10 ? 'font-bold text-emerald-400 text-sm mt-0.5' : 'font-bold text-rose-400 text-sm mt-0.5';
    }
}

// Sim 15: Last 2 & 3 Digits Scanner (4 & 8)
function scan48Number(num) {
    const badge = document.getElementById('scan48Badge');
    const pfx = document.getElementById('scan48Thousands');
    const last2 = document.getElementById('scan48Last2');
    const t4 = document.getElementById('scan4Text');
    const r4 = document.getElementById('scan4Result');
    const t8 = document.getElementById('scan8Text');
    const r8 = document.getElementById('scan8Result');
    
    const str = num.toString();
    const l2 = parseInt(str.slice(-2));
    const l3 = parseInt(str.slice(-3));
    
    if (badge) badge.innerText = `Testing: ${num.toLocaleString()}`;
    if (pfx) pfx.innerText = str.slice(0, -2);
    if (last2) last2.innerText = str.slice(-2);
    
    const is4 = (l2 % 4 === 0);
    const is8 = (l3 % 8 === 0);
    
    if (t4) t4.innerText = `Last 2 digits: ${l2}`;
    if (r4) {
        r4.innerText = is4 ? `${l2} ÷ 4 = ${l2/4} (Divisible! ✓)` : `${l2} ÷ 4 leaves remainder ${l2%4} (✗)`;
        r4.className = is4 ? 'font-bold text-emerald-400 mt-1 block' : 'font-bold text-rose-400 mt-1 block';
    }
    
    if (t8) t8.innerText = `Last 3 digits: ${l3}`;
    if (r8) {
        r8.innerText = is8 ? `${l3} ÷ 8 = ${l3/8} (Divisible! ✓)` : `${l3} ÷ 8 leaves remainder ${l3%8} (✗)`;
        r8.className = is8 ? 'font-bold text-emerald-400 mt-1 block' : 'font-bold text-rose-400 mt-1 block';
    }
}

// Sim 16: Prime Cross-Product Grid Puzzle
function checkPuzzle() {
    const c1 = parseInt(document.getElementById('puz_r1c1')?.value);
    const c2 = parseInt(document.getElementById('puz_r1c2')?.value);
    const c3 = parseInt(document.getElementById('puz_r2c1')?.value);
    const c4 = parseInt(document.getElementById('puz_r2c2')?.value);
    const feedback = document.getElementById('puzzleFeedbackText');
    const badge = document.getElementById('puzzleStatusBadge');
    
    if (c1 === 3 && c2 === 5 && c3 === 2 && c4 === 7) {
        if (badge) {
            badge.innerText = '🎉 PUZZLE SOLVED! All Products Match!';
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        if (feedback) feedback.innerHTML = '<span class="text-emerald-300 font-bold">✓ Row 1: 3×5=15 • Row 2: 2×7=14 • Col 1: 3×2=6 • Col 2: 5×7=35!</span>';
    }
}

function solvePrimePuzzle() {
    const r1c1 = document.getElementById('puz_r1c1');
    const r1c2 = document.getElementById('puz_r1c2');
    const r2c1 = document.getElementById('puz_r2c1');
    const r2c2 = document.getElementById('puz_r2c2');
    
    if (r1c1) r1c1.value = 3;
    if (r1c2) r1c2.value = 5;
    if (r2c1) r2c1.value = 2;
    if (r2c2) r2c2.value = 7;
    
    checkPuzzle();
}

function resetPrimePuzzle() {
    const r1c2 = document.getElementById('puz_r1c2');
    const r2c1 = document.getElementById('puz_r2c1');
    const r2c2 = document.getElementById('puz_r2c2');
    const feedback = document.getElementById('puzzleFeedbackText');
    const badge = document.getElementById('puzzleStatusBadge');
    
    if (r1c2) r1c2.value = '';
    if (r2c1) r2c1.value = '';
    if (r2c2) r2c2.value = '';
    
    if (badge) {
        badge.innerText = 'Fill 4 Cells with Primes';
        badge.className = 'font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40';
    }
    if (feedback) feedback.innerText = 'Hint: R1C1 must divide Row 1 (15) and Col 1 (6) → HCF(15, 6) = 3!';
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

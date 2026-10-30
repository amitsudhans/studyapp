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
    
    // Re-trigger simulator animations if needed
    if (currentSlide === 12) setWheelDivision(4);
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

// Sim 1: Point
function setSimPoint(x, y, name) {
    const circle = document.getElementById('pointCircle');
    const label = document.getElementById('pointLabel');
    const crossH = document.getElementById('crossH');
    const crossV = document.getElementById('crossV');
    const badge = document.getElementById('pointCoordinates');
    if (!circle || !label) return;
    
    circle.setAttribute('cx', x);
    circle.setAttribute('cy', y);
    label.setAttribute('x', x + 12);
    label.setAttribute('y', y - 5);
    label.textContent = `Point ${name}`;
    
    if (crossH) { crossH.setAttribute('y1', y); crossH.setAttribute('y2', y); }
    if (crossV) { crossV.setAttribute('x1', x); crossV.setAttribute('x2', x); }
    if (badge) badge.innerText = `Point ${name} at (${x}, ${y})`;
}

// Sim 2: Line Segment
function updateSegmentSim(val) {
    const lengthPx = parseInt(val);
    const line = document.getElementById('segmentLine');
    const ptB = document.getElementById('segPtB');
    const txtB = document.getElementById('segTextB');
    const curved = document.getElementById('curvedPath');
    const badge = document.getElementById('segmentLengthBadge');
    const sliderVal = document.getElementById('segSliderVal');
    if (!line || !ptB) return;
    
    const startX = 80;
    const endX = startX + lengthPx;
    line.setAttribute('x2', endX);
    ptB.setAttribute('cx', endX);
    if (txtB) txtB.setAttribute('x', endX - 5);
    
    if (curved) {
        const midX = (startX + endX) / 2;
        curved.setAttribute('d', `M ${startX} 120 Q ${midX} 40 ${endX} 120`);
    }
    
    const cm = (lengthPx / 40).toFixed(1);
    if (badge) badge.innerText = `Length AB = ${cm} cm`;
    if (sliderVal) sliderVal.innerText = `${lengthPx} px (${cm} cm)`;
}

// Sim 3: The Line
function rotateSimLine(deg) {
    const line = document.getElementById('infiniteLine');
    if (!line) return;
    line.setAttribute('transform', `rotate(${deg}, 200, 120)`);
}

// Sim 4: Ray
function setRayDirection(dir) {
    const ray = document.getElementById('simRayLine');
    const originPt = document.getElementById('rayOriginPt');
    const originTxt = document.getElementById('rayOriginTxt');
    const dirPt = document.getElementById('rayDirPt');
    const dirTxt = document.getElementById('rayDirTxt');
    const badge = document.getElementById('rayLabelBadge');
    const cone = document.getElementById('torchCone');
    if (!ray) return;
    
    if (dir === 'right') {
        ray.setAttribute('x1', 80);
        ray.setAttribute('x2', 380);
        if (originPt) originPt.setAttribute('cx', 80);
        if (originTxt) { originTxt.setAttribute('x', 55); originTxt.textContent = 'A (Start)'; }
        if (dirPt) dirPt.setAttribute('cx', 240);
        if (dirTxt) { dirTxt.setAttribute('x', 235); dirTxt.textContent = 'P'; }
        if (cone) cone.setAttribute('points', '80,120 380,50 380,190');
        if (badge) badge.innerText = 'Ray AP (Start at A)';
    } else {
        ray.setAttribute('x1', 320);
        ray.setAttribute('x2', 20);
        if (originPt) originPt.setAttribute('cx', 320);
        if (originTxt) { originTxt.setAttribute('x', 325); originTxt.textContent = 'P (Start)'; }
        if (dirPt) dirPt.setAttribute('cx', 160);
        if (dirTxt) { dirTxt.setAttribute('x', 155); dirTxt.textContent = 'A'; }
        if (cone) cone.setAttribute('points', '320,120 20,50 20,190');
        if (badge) badge.innerText = 'Ray PA (Start at P)';
    }
}

// Sim 5: Primitives Sieve
function highlightPrimitive(type) {
    const p = document.getElementById('gPoint');
    const s = document.getElementById('gSegment');
    const l = document.getElementById('gLine');
    const r = document.getElementById('gRay');
    const badge = document.getElementById('sieveSelected');
    
    const setOpacity = (elem, val) => { if (elem) elem.style.opacity = val; };
    
    if (type === 'all') {
        setOpacity(p, '1'); setOpacity(s, '1'); setOpacity(l, '1'); setOpacity(r, '1');
        if (badge) badge.innerText = 'Showing: All 4 Primitives';
    } else if (type === 'seg') {
        setOpacity(p, '0.15'); setOpacity(s, '1'); setOpacity(l, '0.15'); setOpacity(r, '0.15');
        if (badge) badge.innerText = 'Focus: Line Segment (2 Ends, Measurable)';
    } else if (type === 'line') {
        setOpacity(p, '0.15'); setOpacity(s, '0.15'); setOpacity(l, '1'); setOpacity(r, '0.15');
        if (badge) badge.innerText = 'Focus: Line (0 Ends, Infinite)';
    } else if (type === 'ray') {
        setOpacity(p, '0.15'); setOpacity(s, '0.15'); setOpacity(l, '0.15'); setOpacity(r, '1');
        if (badge) badge.innerText = 'Focus: Ray (1 End, Semi-infinite)';
    }
}

// Sim 6: Angle & Vertex
function updateAngleSim(deg) {
    const rad = (parseInt(deg) * Math.PI) / 180;
    const vX = 120, vY = 180;
    const len = 170;
    const endX = vX + len * Math.cos(rad);
    const endY = vY - len * Math.sin(rad);
    
    const arm2 = document.getElementById('angleArm2');
    const ptE = document.getElementById('ptE');
    const txtE = document.getElementById('txtE');
    const arc = document.getElementById('angleArc');
    const degTxt = document.getElementById('angleDegreesTxt');
    const sliderVal = document.getElementById('angleSliderVal');
    const interior = document.getElementById('angleInterior');
    
    if (arm2) { arm2.setAttribute('x2', endX); arm2.setAttribute('y2', endY); }
    if (ptE) { ptE.setAttribute('cx', vX + 130 * Math.cos(rad)); ptE.setAttribute('cy', vY - 130 * Math.sin(rad)); }
    if (txtE) { txtE.setAttribute('x', vX + 130 * Math.cos(rad) + 10); txtE.setAttribute('y', vY - 130 * Math.sin(rad) - 5); }
    
    const arcR = 50;
    const arcEndX = vX + arcR * Math.cos(rad);
    const arcEndY = vY - arcR * Math.sin(rad);
    if (arc) {
        arc.setAttribute('d', `M ${vX + arcR} ${vY} A ${arcR} ${arcR} 0 0 0 ${arcEndX} ${arcEndY}`);
    }
    if (interior) {
        const intR = 100;
        const intEndX = vX + intR * Math.cos(rad);
        const intEndY = vY - intR * Math.sin(rad);
        interior.setAttribute('d', `M ${vX} ${vY} L ${vX + intR} ${vY} A ${intR} ${intR} 0 0 0 ${intEndX} ${intEndY} Z`);
    }
    
    if (degTxt) {
        const midRad = rad / 2;
        degTxt.setAttribute('x', vX + 65 * Math.cos(midRad));
        degTxt.setAttribute('y', vY - 65 * Math.sin(midRad));
        degTxt.textContent = `${deg}°`;
    }
    if (sliderVal) sliderVal.innerText = `${deg}°`;
}

// Sim 7: Invariance
function updateArmLengthSim(len) {
    const lengthPx = parseInt(len);
    const baseLine = document.getElementById('invBaseLine');
    const rotLine = document.getElementById('invRotLine');
    const armTxt = document.getElementById('armLengthTxt');
    if (!baseLine || !rotLine) return;
    
    const rad = (40 * Math.PI) / 180;
    baseLine.setAttribute('x2', 100 + lengthPx);
    rotLine.setAttribute('x2', 100 + lengthPx * Math.cos(rad));
    rotLine.setAttribute('y2', 180 - lengthPx * Math.sin(rad));
    if (armTxt) armTxt.innerText = `${lengthPx} px (Measure still 40°)`;
}

// Sim 8: Superimposition
function superimposeAngles(isOverlay) {
    const movable = document.getElementById('movableAngle');
    const verdict = document.getElementById('superVerdict');
    const badge = document.getElementById('superResultBadge');
    if (!movable) return;
    
    if (isOverlay) {
        movable.setAttribute('transform', 'translate(160, 0)');
        if (verdict) verdict.style.opacity = '1';
        if (badge) badge.innerText = 'Overlay: Arm BA inside ∠DEF (∠ABC < ∠DEF)';
    } else {
        movable.setAttribute('transform', 'translate(0, 0)');
        if (verdict) verdict.style.opacity = '0';
        if (badge) badge.innerText = 'Status: Separate Angles';
    }
}

// Sim 10: Slit
function updateSlitSim(val) {
    const deg = parseInt(val);
    const left = document.getElementById('strawLeft');
    const right = document.getElementById('strawRight');
    const status = document.getElementById('slitPassStatus');
    const valBadge = document.getElementById('strawAngleVal');
    const angleTxt = document.getElementById('strawAngleTxt');
    if (!left || !right) return;
    
    const halfRad = ((deg / 2) * Math.PI) / 180;
    const len = 120;
    const vX = 200, vY = 180;
    
    left.setAttribute('x2', vX - len * Math.sin(halfRad));
    left.setAttribute('y2', vY - len * Math.cos(halfRad));
    right.setAttribute('x2', vX + len * Math.sin(halfRad));
    right.setAttribute('y2', vY - len * Math.cos(halfRad));
    
    if (angleTxt) angleTxt.textContent = `Straw Opening: ${deg}°`;
    
    if (deg <= 40) {
        if (status) {
            status.innerText = 'Status: Fits Smoothly!';
            status.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
        if (valBadge) valBadge.innerText = `${deg}° (Passes)`;
    } else {
        if (status) {
            status.innerText = 'Status: Jams! (Angle Too Wide)';
            status.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
        if (valBadge) valBadge.innerText = `${deg}° (Jams)`;
    }
}

// Sim 11: Straight & Right Angle Bisector
function toggleBisector(mode) {
    const ray = document.getElementById('bisectRay');
    const badge = document.getElementById('bisectBadge');
    if (!ray) return;
    
    if (mode === 'straight') {
        ray.style.opacity = '0.15';
        if (badge) badge.innerText = 'Straight Angle: Exactly 180°';
    } else {
        ray.style.opacity = '1';
        if (badge) badge.innerText = 'Two Right Angles: 90° ⊥ 90°';
    }
}

// Sim 12: 360 Wheel
function setWheelDivision(parts) {
    const group = document.getElementById('wheelSlicesGroup');
    const badge = document.getElementById('divWheelBadge');
    if (!group) return;
    
    group.innerHTML = '';
    const sliceAngle = 360 / parts;
    const colors = ['#f59e0b', '#06b6d4', '#10b981', '#a855f7', '#ec4899', '#3b82f6'];
    
    for (let i = 0; i < parts; i++) {
        const startRad = ((i * sliceAngle) * Math.PI) / 180;
        const endRad = (((i + 1) * sliceAngle) * Math.PI) / 180;
        const r = 90;
        const x1 = 200 + r * Math.cos(startRad);
        const y1 = 120 + r * Math.sin(startRad);
        const x2 = 200 + r * Math.cos(endRad);
        const y2 = 120 + r * Math.sin(endRad);
        const largeArc = sliceAngle > 180 ? 1 : 0;
        
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', `M 200 120 L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`);
        path.setAttribute('fill', colors[i % colors.length]);
        path.setAttribute('fill-opacity', '0.45');
        path.setAttribute('stroke', '#0f172a');
        path.setAttribute('stroke-width', '2');
        group.appendChild(path);
    }
    if (badge) badge.innerText = `1/${parts} of 360° = ${sliceAngle}° (Clean Whole Number)`;
}

// Sim 13: Protractor
function updateProtractorSim(val) {
    const deg = parseInt(val);
    const rad = (deg * Math.PI) / 180;
    const arm = document.getElementById('protArm');
    const badge = document.getElementById('protractorReadout');
    const sliderVal = document.getElementById('protAngleVal');
    if (!arm) return;
    
    const r = 140;
    const endX = 200 + r * Math.cos(rad);
    const endY = 190 - r * Math.sin(rad);
    arm.setAttribute('x2', endX);
    arm.setAttribute('y2', endY);
    
    if (badge) badge.innerText = `Inner: ${deg}° | Outer: ${180 - deg}°`;
    if (sliderVal) sliderVal.innerText = `${deg}°`;
}

// Sim 14: Step Drafter
function setDraftStep(step) {
    const s2 = document.getElementById('draftStep2');
    const s3 = document.getElementById('draftStep3');
    const s4 = document.getElementById('draftStep4');
    const badge = document.getElementById('draftStepBadge');
    
    const setOp = (elem, val) => { if (elem) elem.style.opacity = val; };
    
    if (step === 1) {
        setOp(s2, '0'); setOp(s3, '0'); setOp(s4, '0');
        if (badge) badge.innerText = 'Step 1: Draw Reference Ray IT';
    } else if (step === 2) {
        setOp(s2, '1'); setOp(s3, '0'); setOp(s4, '0');
        if (badge) badge.innerText = 'Step 2: Center Protractor at Vertex I';
    } else if (step === 3) {
        setOp(s2, '1'); setOp(s3, '1'); setOp(s4, '0');
        if (badge) badge.innerText = 'Step 3: Mark Point N at 30°';
    } else if (step === 4) {
        setOp(s2, '0.2'); setOp(s3, '1'); setOp(s4, '1');
        if (badge) badge.innerText = 'Step 4: Draw Ray IN (∠TIN = 30°)';
    }
}

// Sim 15: Classifier
function updateClassifierSim(val) {
    const deg = parseInt(val);
    const rad = (deg * Math.PI) / 180;
    const arm = document.getElementById('classArm');
    const arc = document.getElementById('classArc');
    const text = document.getElementById('classAngleText');
    const badge = document.getElementById('classTypeBadge');
    const sliderVal = document.getElementById('classAngleSliderVal');
    if (!arm) return;
    
    const vX = 180, vY = 180, r = 120;
    const endX = vX + r * Math.cos(rad);
    const endY = vY - r * Math.sin(rad);
    arm.setAttribute('x2', endX);
    arm.setAttribute('y2', endY);
    
    const arcR = 45;
    const arcX = vX + arcR * Math.cos(rad);
    const arcY = vY - arcR * Math.sin(rad);
    if (arc) arc.setAttribute('d', `M ${vX + arcR} ${vY} A ${arcR} ${arcR} 0 0 0 ${arcX} ${arcY}`);
    
    if (text) {
        const midRad = rad / 2;
        text.setAttribute('x', vX + 65 * Math.cos(midRad));
        text.setAttribute('y', vY - 65 * Math.sin(midRad));
        text.textContent = `${deg}°`;
    }
    if (sliderVal) sliderVal.innerText = `${deg}°`;
    
    if (deg < 90) {
        if (badge) {
            badge.innerText = `Acute Angle (${deg}° < 90°)`;
            badge.className = 'font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40';
        }
    } else if (deg === 90) {
        if (badge) {
            badge.innerText = 'Right Angle (Exactly 90° ∟)';
            badge.className = 'font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40';
        }
    } else {
        if (badge) {
            badge.innerText = `Obtuse Angle (90° < ${deg}° < 180°)`;
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
    }
}

// Sim 16: Reflex
function updateReflexSim(val) {
    const deg = parseInt(val);
    const rad = (deg * Math.PI) / 180;
    const arm = document.getElementById('reflexArm');
    const arc = document.getElementById('reflexArc');
    const text = document.getElementById('reflexDegreeText');
    const inner = document.getElementById('innerComplementText');
    const badge = document.getElementById('reflexTypeBadge');
    const sliderVal = document.getElementById('reflexSliderVal');
    if (!arm) return;
    
    const vX = 200, vY = 120, r = 110;
    const endX = vX + r * Math.cos(rad);
    const endY = vY - r * Math.sin(rad);
    arm.setAttribute('x2', endX);
    arm.setAttribute('y2', endY);
    
    const arcR = 40;
    const arcX = vX + arcR * Math.cos(rad);
    const arcY = vY - arcR * Math.sin(rad);
    if (arc) {
        arc.setAttribute('d', `M ${vX + arcR} ${vY} A ${arcR} ${arcR} 0 1 1 ${arcX} ${arcY}`);
    }
    
    if (text) text.textContent = `${deg}°`;
    if (inner) inner.textContent = `Inner: ${360 - deg}°`;
    if (sliderVal) sliderVal.innerText = `${deg}° (${deg === 180 ? 'Straight' : deg === 360 ? 'Complete Turn' : 'Reflex'})`;
    
    if (badge) {
        if (deg === 180) {
            badge.innerText = 'Straight Angle: 180°';
            badge.className = 'font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40';
        } else if (deg === 360) {
            badge.innerText = 'Complete Angle: 360°';
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        } else {
            badge.innerText = `Reflex Angle: ${deg}° (180° < θ < 360°)`;
            badge.className = 'font-mono text-violet-300 bg-violet-950/60 px-2 py-0.5 rounded border border-violet-800/40';
        }
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

// Setup click on point canvas
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('pointCanvasContainer');
    if (canvas) {
        canvas.addEventListener('click', (e) => {
            const rect = canvas.getBoundingClientRect();
            const x = Math.round(((e.clientX - rect.left) / rect.width) * 400);
            const y = Math.round(((e.clientY - rect.top) / rect.height) * 240);
            setSimPoint(x, y, 'P');
        });
    }
});
"""

    code = f'''"""NCERT Class 6 Mathematics Chapter 2: Lines and Angles JavaScript Module."""

INTERACTIVE_JS = """{js_content}"""
'''

    # Strict check for zero raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in JavaScript module!")

    with open(".agents/class6_math_lines_angles_js.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully generated .agents/class6_math_lines_angles_js.py.")
    print("VERIFIED PASS: Zero raw LaTeX in JS module!")

if __name__ == "__main__":
    generate_js()

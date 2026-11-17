# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 8: Heredity
Interactive Canvas & Simulator JavaScript Handlers (Slides 1 to 16)
"""

SIMULATOR_JS = '''
// Helper: Draw rounded rectangle
function drawRoundedRect(ctx, x, y, width, height, radius, fill, stroke) {
    ctx.beginPath();
    ctx.moveTo(x + radius, y);
    ctx.lineTo(x + width - radius, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
    ctx.lineTo(x + width, y + height - radius);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
    ctx.lineTo(x + radius, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
    ctx.lineTo(x, y + radius);
    ctx.quadraticCurveTo(x, y, x + radius, y);
    ctx.closePath();
    if (fill) ctx.fill();
    if (stroke) ctx.stroke();
}

// ==========================================
// SIMULATOR 1: Accumulation of Variation
// ==========================================
let slide1State = { mode: 'asexual', gen: 1 };

function initSlide1() {
    setSlide1Mode('asexual');
}

function setSlide1Mode(mode) {
    slide1State.mode = mode;
    slide1State.gen = 1;
    const btnA = document.getElementById('btnSlide1Asexual');
    const btnS = document.getElementById('btnSlide1Sexual');
    if (btnA && btnS) {
        if (mode === 'asexual') {
            btnA.className = 'px-3 py-1.5 rounded-xl bg-cyan-600 text-white text-xs font-semibold shadow-md transition-all';
            btnS.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        } else {
            btnS.className = 'px-3 py-1.5 rounded-xl bg-cyan-600 text-white text-xs font-semibold shadow-md transition-all';
            btnA.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        }
    }
    updateSlide1();
}

function stepSlide1Gen() {
    if (slide1State.gen < 3) slide1State.gen++;
    else slide1State.gen = 1;
    updateSlide1();
}

function resetSlide1() {
    slide1State.gen = 1;
    updateSlide1();
}

function updateSlide1() {
    const canvas = document.getElementById('slide1Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;
    const badge = document.getElementById('slide1GenBadge');
    if (badge) badge.textContent = `Gen ${slide1State.gen}`;
    const status = document.getElementById('slide1Status');

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    if (slide1State.mode === 'asexual') {
        // Asexual Tree: 1 -> 2 -> 4
        if (status) status.innerHTML = `<span class="text-cyan-400 font-bold">Asexual Reproduction:</span> Generation ${slide1State.gen} of clonal division. Bacteria or sugarcane plants divide with minimal copying inaccuracies; individuals share almost identical basic body design.`;

        // Gen 1: 1 parent at top
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.roundRect(w * 0.5 - 25, 30, 50, 30, 8);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Original', w * 0.5, 50);

        if (slide1State.gen >= 2) {
            // Lines to Gen 2
            ctx.strokeStyle = '#38bdf8';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(w * 0.5, 60);
            ctx.lineTo(w * 0.3, 110);
            ctx.moveTo(w * 0.5, 60);
            ctx.lineTo(w * 0.7, 110);
            ctx.stroke();

            // Gen 2 individuals
            ctx.fillStyle = '#0284c7';
            ctx.beginPath();
            ctx.roundRect(w * 0.3 - 25, 110, 50, 30, 8);
            ctx.fill();
            ctx.fillStyle = '#ffffff';
            ctx.fillText('Clone A', w * 0.3, 130);

            // Clone B with slight mutation (green dot)
            ctx.fillStyle = '#0ea5e9';
            ctx.beginPath();
            ctx.roundRect(w * 0.7 - 25, 110, 50, 30, 8);
            ctx.fill();
            ctx.fillStyle = '#10b981';
            ctx.beginPath();
            ctx.arc(w * 0.7 + 15, 118, 4, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = '#ffffff';
            ctx.fillText('Variant 1', w * 0.7, 130);
        }

        if (slide1State.gen >= 3) {
            // Lines to Gen 3
            ctx.strokeStyle = '#38bdf8';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(w * 0.3, 140);
            ctx.lineTo(w * 0.18, 200);
            ctx.moveTo(w * 0.3, 140);
            ctx.lineTo(w * 0.42, 200);
            ctx.moveTo(w * 0.7, 140);
            ctx.lineTo(w * 0.58, 200);
            ctx.moveTo(w * 0.7, 140);
            ctx.lineTo(w * 0.82, 200);
            ctx.stroke();

            const nodes = [
                { x: w * 0.18, label: 'Clone A1', col: '#0284c7', dot: null },
                { x: w * 0.42, label: 'Variant 2', col: '#0284c7', dot: '#f59e0b' },
                { x: w * 0.58, label: 'Variant 1a', col: '#0ea5e9', dot: '#10b981' },
                { x: w * 0.82, label: 'Variant 1b', col: '#0ea5e9', dot: '#ec4899' }
            ];

            nodes.forEach(n => {
                ctx.fillStyle = n.col;
                ctx.beginPath();
                ctx.roundRect(n.x - 28, 200, 56, 32, 8);
                ctx.fill();
                if (n.dot) {
                    ctx.fillStyle = n.dot;
                    ctx.beginPath();
                    ctx.arc(n.x + 18, 208, 4, 0, Math.PI * 2);
                    ctx.fill();
                }
                ctx.fillStyle = '#ffffff';
                ctx.fillText(n.label, n.x, 220);
            });
        }

        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px sans-serif';
        ctx.fillText('Subtle differences accumulate slowly over generations (DNA replication errors).', w * 0.5, h - 25);

    } else {
        // Sexual Reproduction Tree (2 parents -> diverse offspring)
        if (status) status.innerHTML = `<span class="text-cyan-400 font-bold">Sexual Reproduction:</span> Generation ${slide1State.gen}. Two distinct parental genomes combine via meiotic reduction and gametic fertilization, creating immense phenotypic and genotypic diversity!`;

        // Parents
        ctx.fillStyle = '#3b82f6';
        ctx.beginPath();
        ctx.roundRect(w * 0.35 - 30, 30, 60, 32, 8);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Parent A', w * 0.35, 50);

        ctx.fillStyle = '#ec4899';
        ctx.beginPath();
        ctx.roundRect(w * 0.65 - 30, 30, 60, 32, 8);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Parent B', w * 0.65, 50);

        if (slide1State.gen >= 2) {
            ctx.strokeStyle = '#a855f7';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(w * 0.35, 62);
            ctx.lineTo(w * 0.5, 95);
            ctx.moveTo(w * 0.65, 62);
            ctx.lineTo(w * 0.5, 95);
            ctx.lineTo(w * 0.5, 120);
            ctx.stroke();

            // 3 diverse offspring
            const off = [
                { x: w * 0.25, label: 'Offspring 1', col: '#8b5cf6' },
                { x: w * 0.5, label: 'Offspring 2', col: '#06b6d4' },
                { x: w * 0.75, label: 'Offspring 3', col: '#f59e0b' }
            ];

            ctx.beginPath();
            ctx.moveTo(w * 0.5, 120);
            ctx.lineTo(w * 0.25, 140);
            ctx.moveTo(w * 0.5, 120);
            ctx.lineTo(w * 0.5, 140);
            ctx.moveTo(w * 0.5, 120);
            ctx.lineTo(w * 0.75, 140);
            ctx.stroke();

            off.forEach(o => {
                ctx.fillStyle = o.col;
                ctx.beginPath();
                ctx.roundRect(o.x - 35, 140, 70, 32, 8);
                ctx.fill();
                ctx.fillStyle = '#ffffff';
                ctx.fillText(o.label, o.x, 160);
            });
        }

        if (slide1State.gen >= 3) {
            ctx.fillStyle = '#10b981';
            ctx.font = 'bold 12px sans-serif';
            ctx.fillText('Exponential Allelic Diversity & Novel Combinations in Gen 3!', w * 0.5, 230);

            // Diverse dots
            const colors = ['#f43f5e', '#8b5cf6', '#06b6d4', '#10b981', '#f59e0b', '#ec4899', '#6366f1', '#14b8a6'];
            for (let i = 0; i < 16; i++) {
                const rx = 100 + i * 26;
                ctx.fillStyle = colors[i % colors.length];
                ctx.beginPath();
                ctx.arc(rx, 265, 8, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px sans-serif';
        ctx.fillText('Sexual reproduction yields high diversity, equipping populations for environmental change.', w * 0.5, h - 25);
    }
}

// ==========================================
// SIMULATOR 2: DNA Replication Fidelity
// ==========================================
let slide2State = { fidelity: 2, replicated: false, mismatches: 0 };

function initSlide2() {
    setSlide2Fidelity(2);
}

function setSlide2Fidelity(val) {
    slide2State.fidelity = parseInt(val);
    drawSlide2();
}

function replicateSlide2DNA() {
    slide2State.replicated = true;
    slide2State.mismatches = slide2State.fidelity === 1 ? 0 : (slide2State.fidelity === 2 ? 1 : 3);
    const mSpan = document.getElementById('slide2Errors');
    if (mSpan) mSpan.textContent = slide2State.mismatches;
    drawSlide2();
}

function drawSlide2() {
    const canvas = document.getElementById('slide2Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText("Parental DNA Template Strand (5' to 3')", 40, 45);

    const basesParent = ['A','T','G','C','T','A','A','G','C','T','G','C'];
    const basesComp =   ['T','A','C','G','A','T','T','C','G','A','C','G'];

    // Draw parent strand
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(40, 80);
    ctx.lineTo(w - 40, 80);
    ctx.stroke();

    for (let i = 0; i < basesParent.length; i++) {
        const x = 60 + i * 42;
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(x - 14, 65, 28, 30, 6);
        ctx.fill();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px monospace';
        ctx.textAlign = 'center';
        ctx.fillText(basesParent[i], x, 85);
    }

    if (slide2State.replicated) {
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText('Synthesized Daughter Strand with DNA Polymerase', 40, 160);

        ctx.strokeStyle = '#6366f1';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(40, 200);
        ctx.lineTo(w - 40, 200);
        ctx.stroke();

        const errorIndices = slide2State.mismatches === 0 ? [] : (slide2State.mismatches === 1 ? [4] : [2, 7, 10]);

        for (let i = 0; i < basesComp.length; i++) {
            const x = 60 + i * 42;
            const isError = errorIndices.includes(i);
            const base = isError ? (basesComp[i] === 'A' ? 'C' : 'G') : basesComp[i];

            ctx.fillStyle = isError ? '#ef4444' : '#10b981';
            ctx.beginPath();
            ctx.roundRect(x - 14, 185, 28, 30, 6);
            ctx.fill();

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 12px monospace';
            ctx.textAlign = 'center';
            ctx.fillText(base, x, 205);

            // Hydrogen bond lines
            ctx.strokeStyle = isError ? '#f87171' : '#64748b';
            ctx.lineWidth = 1.5;
            ctx.setLineDash([2, 2]);
            ctx.beginPath();
            ctx.moveTo(x, 95);
            ctx.lineTo(x, 185);
            ctx.stroke();
            ctx.setLineDash([]);
        }

        ctx.fillStyle = slide2State.mismatches > 0 ? '#f59e0b' : '#34d399';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        if (slide2State.mismatches > 0) {
            ctx.fillText(`⚡ Replication Inaccuracy: ${slide2State.mismatches} mismatched nucleotide base pairs introduce genetic variation.`, w * 0.5, h - 35);
        } else {
            ctx.fillText('✓ Perfect complementary base-pairing (Adenine-Thymine, Guanine-Cytosine).', w * 0.5, h - 35);
        }
    } else {
        ctx.fillStyle = '#94a3b8';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Click "Replicate DNA Fork" to synthesize the complementary daughter strand.', w * 0.5, 200);
    }
}

// ==========================================
// SIMULATOR 3: Environmental Selection
// ==========================================
let slide3State = { temp: 30, heatShock: false, normal: 45, resistant: 5 };

function initSlide3() {
    resetSlide3Culture();
}

function resetSlide3Culture() {
    slide3State = { temp: 30, heatShock: false, normal: 45, resistant: 5 };
    const slider = document.getElementById('slide3TempSlider');
    if (slider) slider.value = 30;
    updateSlide3();
}

function setSlide3Temp(val) {
    slide3State.temp = parseInt(val);
    if (slide3State.temp >= 55) {
        slide3State.normal = Math.max(0, 45 - Math.floor((slide3State.temp - 50) * 2));
        slide3State.resistant = 5 + Math.floor((slide3State.temp - 50) * 1.5);
    } else {
        slide3State.normal = 45;
        slide3State.resistant = 5;
    }
    updateSlide3();
}

function applySlide3HeatWave() {
    slide3State.temp = 65;
    const slider = document.getElementById('slide3TempSlider');
    if (slider) slider.value = 65;
    slide3State.heatShock = true;
    slide3State.normal = 4;
    slide3State.resistant = 28;
    updateSlide3();
}

function updateSlide3() {
    const canvas = document.getElementById('slide3Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    const tDisp = document.getElementById('slide3TempDisplay');
    if (tDisp) tDisp.textContent = `${slide3State.temp}°C`;
    const nCount = document.getElementById('slide3NormalCount');
    if (nCount) nCount.textContent = slide3State.normal;
    const rCount = document.getElementById('slide3ResistantCount');
    if (rCount) rCount.textContent = slide3State.resistant;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Petri Dish Circle
    const cX = w * 0.5, cY = h * 0.5 - 10, radius = 120;
    ctx.fillStyle = slide3State.temp > 50 ? '#271216' : '#0b1d28';
    ctx.beginPath();
    ctx.arc(cX, cY, radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = slide3State.temp > 50 ? '#f43f5e' : '#38bdf8';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Draw normal bacteria (green rods)
    ctx.fillStyle = '#10b981';
    for (let i = 0; i < slide3State.normal; i++) {
        const ang = (i * 2.39996) % (Math.PI * 2);
        const dist = 15 + ((i * 37) % (radius - 25));
        const bx = cX + Math.cos(ang) * dist;
        const by = cY + Math.sin(ang) * dist;

        ctx.save();
        ctx.translate(bx, by);
        ctx.rotate(ang);
        ctx.beginPath();
        ctx.roundRect(-7, -3, 14, 6, 3);
        ctx.fill();
        ctx.restore();
    }

    // Draw heat-resistant bacteria (red/rose rods)
    ctx.fillStyle = '#f43f5e';
    for (let i = 0; i < slide3State.resistant; i++) {
        const ang = (i * 1.618) % (Math.PI * 2);
        const dist = 20 + ((i * 43) % (radius - 30));
        const bx = cX + Math.cos(ang) * dist;
        const by = cY + Math.sin(ang) * dist;

        ctx.save();
        ctx.translate(bx, by);
        ctx.rotate(ang + 0.5);
        ctx.beginPath();
        ctx.roundRect(-8, -4, 16, 8, 4);
        ctx.fill();
        ctx.restore();
    }

    // Environmental condition text
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`Water Temperature: ${slide3State.temp}°C`, cX, h - 25);
}

// ==========================================
// SIMULATOR 4: Parental Genetic Contribution
// ==========================================
let slide4State = { trait: 'height', fused: false };

function initSlide4() {
    setSlide4Trait('height');
}

function setSlide4Trait(trait) {
    slide4State.trait = trait;
    slide4State.fused = false;
    drawSlide4();
}

function fuseSlide4Gametes() {
    slide4State.fused = true;
    drawSlide4();
}

function drawSlide4() {
    const canvas = document.getElementById('slide4Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const traitNames = {
        height: { m: 'T (Tall)', f: 't (Short)', res: 'Tt (Tall Offspring)' },
        seed: { m: 'R (Round)', f: 'r (Wrinkled)', res: 'Rr (Round Seed)' },
        earlobe: { m: 'E (Free)', f: 'e (Attached)', res: 'Ee (Free Earlobe)' }
    };
    const tInfo = traitNames[slide4State.trait] || traitNames.height;

    // Maternal Gamete (Ovum)
    ctx.fillStyle = '#ec4899';
    ctx.beginPath();
    ctx.arc(w * 0.25, 120, 45, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Maternal Ovum', w * 0.25, 115);
    ctx.font = '11px sans-serif';
    ctx.fillText('23 Chromosomes (n)', w * 0.25, 135);
    ctx.fillStyle = '#fbcfe8';
    ctx.font = 'bold 13px monospace';
    ctx.fillText(`Allele: ${tInfo.m.split(' ')[0]}`, w * 0.25, 185);

    // Paternal Gamete (Sperm)
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath();
    ctx.arc(w * 0.75, 120, 30, 0, Math.PI * 2);
    ctx.fill();
    // Sperm tail
    ctx.strokeStyle = '#60a5fa';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(w * 0.75 + 30, 120);
    ctx.quadraticCurveTo(w * 0.75 + 60, 105, w * 0.75 + 80, 135);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Paternal Sperm', w * 0.75, 115);
    ctx.font = '11px sans-serif';
    ctx.fillText('23 Chromosomes (n)', w * 0.75, 135);
    ctx.fillStyle = '#bfdbfe';
    ctx.font = 'bold 13px monospace';
    ctx.fillText(`Allele: ${tInfo.f.split(' ')[0]}`, w * 0.75, 185);

    if (slide4State.fused) {
        // Zygote in center
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(w * 0.5, 220, 50, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Diploid Zygote (2n)', w * 0.5, 215);
        ctx.font = '10px sans-serif';
        ctx.fillText('46 Chromosomes (23 Pairs)', w * 0.5, 230);
        ctx.fillStyle = '#a7f3d0';
        ctx.font = 'bold 12px monospace';
        ctx.fillText(tInfo.res, w * 0.5, 250);

        ctx.fillStyle = '#34d399';
        ctx.font = '11px sans-serif';
        ctx.fillText('Fertilization restores the diploid number with equal genetic contributions!', w * 0.5, h - 20);
    } else {
        ctx.fillStyle = '#94a3b8';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Click "Fuse Gametes (Fertilization)" to unite the maternal and paternal alleles.', w * 0.5, 250);
    }
}

// ==========================================
// SIMULATOR 5: Earlobe Survey (Activity 8.1)
// ==========================================
let slide5State = { total: 40, free: 30, attached: 10 };

function initSlide5() {
    sampleSlide5Earlobes(40);
}

function sampleSlide5Earlobes(n) {
    slide5State.total = n;
    // ~75% dominant free earlobe
    slide5State.free = Math.round(n * 0.75);
    slide5State.attached = n - slide5State.free;

    const t = document.getElementById('slide5Total');
    const f = document.getElementById('slide5Free');
    const a = document.getElementById('slide5Attached');
    if (t) t.textContent = slide5State.total;
    if (f) f.textContent = `${slide5State.free} (75%)`;
    if (a) a.textContent = `${slide5State.attached} (25%)`;

    drawSlide5();
}

function drawSlide5() {
    const canvas = document.getElementById('slide5Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Two diagrams: Free Earlobe vs Attached Earlobe
    // Left: Free Earlobe Diagram
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(50, 40, 220, 180, 12);
    ctx.fill();

    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 4;
    ctx.beginPath();
    // Ear contour free
    ctx.moveTo(130, 70);
    ctx.bezierCurveTo(190, 70, 200, 140, 160, 170);
    ctx.bezierCurveTo(145, 185, 120, 175, 120, 150); // Free hanging lobe
    ctx.stroke();

    ctx.fillStyle = '#f59e0b';
    ctx.font = 'bold 13px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Free Earlobe (Dominant)', 160, 205);

    // Right: Attached Earlobe Diagram
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 270, 40, 220, 180, 12);
    ctx.fill();

    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    // Ear contour attached directly to head
    ctx.moveTo(w - 190, 70);
    ctx.bezierCurveTo(w - 130, 70, w - 120, 140, w - 150, 165);
    ctx.lineTo(w - 170, 165); // Fused straight to cheek
    ctx.stroke();

    ctx.fillStyle = '#cbd5e1';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText('Attached Earlobe (Recessive)', w - 160, 205);

    // Bar chart comparison
    const maxBarH = 60;
    const freeBarH = (slide5State.free / slide5State.total) * maxBarH;
    const attBarH = (slide5State.attached / slide5State.total) * maxBarH;

    ctx.fillStyle = '#f59e0b';
    ctx.fillRect(140, h - 30 - freeBarH, 40, freeBarH);
    ctx.fillStyle = '#94a3b8';
    ctx.fillRect(w - 180, h - 30 - attBarH, 40, attBarH);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText(`75% (EE or Ee)`, 160, h - 35 - freeBarH);
    ctx.fillText(`25% (ee)`, w - 160, h - 35 - attBarH);
}

// ==========================================
// SIMULATOR 6: Mendel Pea Breeding Bench
// ==========================================
let slide6State = { trait: 'height', pollinated: false };

function initSlide6() {
    setSlide6PeaTrait('height');
}

function setSlide6PeaTrait(t) {
    slide6State.trait = t;
    slide6State.pollinated = false;
    drawSlide6();
}

function pollinateSlide6Peas() {
    slide6State.pollinated = true;
    drawSlide6();
}

function drawSlide6() {
    const canvas = document.getElementById('slide6Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const traits = {
        height: { name: 'Plant Height', dom: 'Tall Stem (TT)', rec: 'Dwarf Stem (tt)', domCol: '#10b981', recCol: '#64748b' },
        seed_shape: { name: 'Seed Shape', dom: 'Round Seed (RR)', rec: 'Wrinkled Seed (rr)', domCol: '#fbbf24', recCol: '#d97706' },
        seed_color: { name: 'Seed Color', dom: 'Yellow Seed (YY)', rec: 'Green Seed (yy)', domCol: '#fde047', recCol: '#22c55e' },
        flower_color: { name: 'Flower Color', dom: 'Violet Flower (WW)', rec: 'White Flower (ww)', domCol: '#a855f7', recCol: '#f8fafc' },
        pod_shape: { name: 'Pod Shape', dom: 'Inflated Pod (II)', rec: 'Constricted Pod (ii)', domCol: '#16a34a', recCol: '#ca8a04' }
    };

    const cur = traits[slide6State.trait] || traits.height;

    // Flower 1: Maternal Stigma
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(60, 45, 200, 190, 12);
    ctx.fill();

    ctx.fillStyle = cur.domCol;
    ctx.font = 'bold 13px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Dominant Parent', 160, 75);
    ctx.font = '11px sans-serif';
    ctx.fillStyle = '#cbd5e1';
    ctx.fillText(cur.dom, 160, 95);

    // Draw visual representation
    if (slide6State.trait === 'height') {
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(160, 200);
        ctx.lineTo(160, 115);
        ctx.stroke();
    } else {
        ctx.fillStyle = cur.domCol;
        ctx.beginPath();
        ctx.arc(160, 160, 28, 0, Math.PI * 2);
        ctx.fill();
    }

    // Flower 2: Paternal Anther
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 260, 45, 200, 190, 12);
    ctx.fill();

    ctx.fillStyle = '#cbd5e1';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText('Recessive Parent', w - 160, 75);
    ctx.font = '11px sans-serif';
    ctx.fillText(cur.rec, w - 160, 95);

    if (slide6State.trait === 'height') {
        ctx.strokeStyle = '#64748b';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(w - 160, 200);
        ctx.lineTo(w - 160, 155); // Short
        ctx.stroke();
    } else {
        ctx.fillStyle = cur.recCol;
        ctx.beginPath();
        ctx.arc(w - 160, 160, 20, 0, Math.PI * 2);
        ctx.fill();
    }

    if (slide6State.pollinated) {
        // Pollination Brush animation line
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(w - 160, 120);
        ctx.quadraticCurveTo(w * 0.5, 80, 160, 120);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#fef08a';
        ctx.beginPath();
        ctx.arc(w * 0.5, 95, 6, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#34d399';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('✓ Cross-Pollination Complete: Pollen dusted on emasculated stigma.', w * 0.5, h - 35);
    } else {
        ctx.fillStyle = '#94a3b8';
        ctx.font = '12px sans-serif';
        ctx.fillText('Click "Cross-Pollinate Flowers" to transfer pollen.', w * 0.5, h - 35);
    }
}

// ==========================================
// SIMULATOR 7: Monohybrid Cross Dynamics
// ==========================================
let slide7State = { stage: 'P' };

function initSlide7() {
    setSlide7Stage('P');
}

function setSlide7Stage(st) {
    slide7State.stage = st;
    const btnP = document.getElementById('btnSlide7P');
    const btnF1 = document.getElementById('btnSlide7F1');
    const btnF2 = document.getElementById('btnSlide7F2');

    [btnP, btnF1, btnF2].forEach(b => {
        if (b) b.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    });
    if (st === 'P' && btnP) btnP.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold';
    if (st === 'F1' && btnF1) btnF1.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold';
    if (st === 'F2' && btnF2) btnF2.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold';

    const curGen = document.getElementById('slide7CurrentGen');
    const tCount = document.getElementById('slide7TallCount');
    const sCount = document.getElementById('slide7ShortCount');

    if (st === 'P') {
        if (curGen) curGen.textContent = 'Parental (TT × tt)';
        if (tCount) tCount.textContent = 'Pure Tall (TT)';
        if (sCount) sCount.textContent = 'Pure Short (tt)';
    } else if (st === 'F1') {
        if (curGen) curGen.textContent = 'F1 Progeny (Tt)';
        if (tCount) tCount.textContent = '100% Tall';
        if (sCount) sCount.textContent = '0% Short';
    } else {
        if (curGen) curGen.textContent = 'F2 Generation (Selfing)';
        if (tCount) tCount.textContent = '75% (3 Tall)';
        if (sCount) sCount.textContent = '25% (1 Short)';
    }

    drawSlide7();
}

function drawSlide7() {
    const canvas = document.getElementById('slide7Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    if (slide7State.stage === 'P') {
        // Parental: Pure TT tall (left) and Pure tt short (right)
        ctx.fillStyle = '#10b981';
        ctx.font = 'bold 13px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Pure Tall Parent (TT)', w * 0.3, 50);

        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.moveTo(w * 0.3, 220);
        ctx.lineTo(w * 0.3, 80); // Tall stem
        ctx.stroke();

        ctx.fillStyle = '#94a3b8';
        ctx.fillText('Pure Short Parent (tt)', w * 0.7, 50);

        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.moveTo(w * 0.7, 220);
        ctx.lineTo(w * 0.7, 160); // Short stem
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = '12px sans-serif';
        ctx.fillText('Cross-pollination between homozygous tall and dwarf lines.', w * 0.5, h - 25);

    } else if (slide7State.stage === 'F1') {
        // F1: 100% Tall (Tt)
        ctx.fillStyle = '#10b981';
        ctx.font = 'bold 14px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('All F1 Progeny are TALL (Genotype: Tt)', w * 0.5, 45);

        // 4 tall plants
        for (let i = 0; i < 4; i++) {
            const px = 120 + i * 120;
            ctx.strokeStyle = '#10b981';
            ctx.lineWidth = 7;
            ctx.beginPath();
            ctx.moveTo(px, 220);
            ctx.lineTo(px, 80);
            ctx.stroke();

            ctx.fillStyle = '#34d399';
            ctx.font = 'bold 11px monospace';
            ctx.fillText('Tt', px, 70);
        }

        ctx.fillStyle = '#a7f3d0';
        ctx.font = '12px sans-serif';
        ctx.fillText('Zero dwarf plants appear in F1. Tallness completely dominates shortness!', w * 0.5, h - 25);

    } else {
        // F2: 3 Tall : 1 Dwarf
        ctx.fillStyle = '#a855f7';
        ctx.font = 'bold 14px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('F2 Generation: 3 Tall : 1 Short (3:1 Phenotypic Ratio)', w * 0.5, 40);

        const plants = [
            { x: 100, tall: true, geno: 'TT' },
            { x: 220, tall: true, geno: 'Tt' },
            { x: 340, tall: true, geno: 'Tt' },
            { x: 460, tall: false, geno: 'tt' }
        ];

        plants.forEach(p => {
            ctx.strokeStyle = p.tall ? '#10b981' : '#f43f5e';
            ctx.lineWidth = 7;
            ctx.beginPath();
            ctx.moveTo(p.x, 220);
            ctx.lineTo(p.x, p.tall ? 80 : 160);
            ctx.stroke();

            ctx.fillStyle = p.tall ? '#34d399' : '#f87171';
            ctx.font = 'bold 11px monospace';
            ctx.fillText(p.geno, p.x, p.tall ? 70 : 150);
            ctx.font = '10px sans-serif';
            ctx.fillText(p.tall ? 'Tall' : 'Dwarf', p.x, 240);
        });

        ctx.fillStyle = '#e9d5ff';
        ctx.font = '12px sans-serif';
        ctx.fillText('The hidden recessive dwarf trait cleanly reappears in 25% of offspring!', w * 0.5, h - 25);
    }
}

// ==========================================
// SIMULATOR 8: Punnett Square Calculator
// ==========================================
let slide8State = { cross: 'Tt_Tt' };

function initSlide8() {
    updateSlide8Cross('Tt_Tt');
}

function updateSlide8Cross(c) {
    slide8State.cross = c;
    const pRat = document.getElementById('slide8PhenoRatio');
    const gRat = document.getElementById('slide8GenoRatio');

    if (c === 'Tt_Tt') {
        if (pRat) pRat.textContent = '3 Tall : 1 Dwarf (75% vs 25%)';
        if (gRat) gRat.textContent = '1 TT : 2 Tt : 1 tt (25% : 50% : 25%)';
    } else if (c === 'TT_tt') {
        if (pRat) pRat.textContent = '100% Tall (0% Dwarf)';
        if (gRat) gRat.textContent = '100% Tt (Heterozygous)';
    } else {
        if (pRat) pRat.textContent = '1 Tall : 1 Dwarf (50% vs 50%)';
        if (gRat) gRat.textContent = '1 Tt : 1 tt (50% vs 50%)';
    }

    drawSlide8();
}

function drawSlide8() {
    const canvas = document.getElementById('slide8Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const configs = {
        Tt_Tt: { g1: ['T', 't'], g2: ['T', 't'], cells: [['TT', true], ['Tt', true], ['Tt', true], ['tt', false]] },
        TT_tt: { g1: ['T', 'T'], g2: ['t', 't'], cells: [['Tt', true], ['Tt', true], ['Tt', true], ['Tt', true]] },
        Tt_tt: { g1: ['T', 't'], g2: ['t', 't'], cells: [['Tt', true], ['tt', false], ['Tt', true], ['tt', false]] }
    };
    const cur = configs[slide8State.cross] || configs.Tt_Tt;

    // Draw 2x2 Punnett Grid in center
    const sX = w * 0.5 - 90, sY = 60, cellSize = 80;

    // Gamete labels top
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 15px monospace';
    ctx.textAlign = 'center';
    ctx.fillText(cur.g1[0], sX + cellSize * 0.5, sY - 12);
    ctx.fillText(cur.g1[1], sX + cellSize * 1.5, sY - 12);

    // Gamete labels left
    ctx.fillStyle = '#ec4899';
    ctx.fillText(cur.g2[0], sX - 25, sY + cellSize * 0.5 + 5);
    ctx.fillText(cur.g2[1], sX - 25, sY + cellSize * 1.5 + 5);

    // Grid cells
    for (let r = 0; r < 2; r++) {
        for (let c = 0; c < 2; c++) {
            const idx = r * 2 + c;
            const [geno, isTall] = cur.cells[idx];
            const cellX = sX + c * cellSize;
            const cellY = sY + r * cellSize;

            ctx.fillStyle = isTall ? '#064e3b' : '#7f1d1d';
            ctx.fillRect(cellX, cellY, cellSize, cellSize);

            ctx.strokeStyle = '#334155';
            ctx.lineWidth = 2;
            ctx.strokeRect(cellX, cellY, cellSize, cellSize);

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 16px monospace';
            ctx.fillText(geno, cellX + cellSize * 0.5, cellY + cellSize * 0.45);

            ctx.fillStyle = isTall ? '#6ee7b7' : '#fca5a5';
            ctx.font = '11px sans-serif';
            ctx.fillText(isTall ? 'Tall' : 'Dwarf', cellX + cellSize * 0.5, cellY + cellSize * 0.75);
        }
    }

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Green = Dominant Tall phenotype; Red = Recessive Dwarf phenotype.', w * 0.5, h - 25);
}

// ==========================================
// SIMULATOR 9: Dihybrid Cross Assortment
// ==========================================
let slide9State = { crossed: false };

function initSlide9() {
    slide9State.crossed = false;
    drawSlide9();
}

function crossSlide9Parents() {
    slide9State.crossed = true;
    drawSlide9();
}

function drawSlide9() {
    const canvas = document.getElementById('slide9Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Parent 1: Round Yellow (RRYY)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(50, 40, 220, 140, 12);
    ctx.fill();

    // Round Yellow seed circle
    ctx.fillStyle = '#fbbf24';
    ctx.beginPath();
    ctx.arc(160, 95, 30, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Round Yellow Parent', 160, 145);
    ctx.fillStyle = '#fde68a';
    ctx.font = 'bold 12px monospace';
    ctx.fillText('Genotype: RRYY (Gamete: RY)', 160, 165);

    // Parent 2: Wrinkled Green (rryy)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 270, 40, 220, 140, 12);
    ctx.fill();

    // Wrinkled green seed
    ctx.fillStyle = '#15803d';
    ctx.beginPath();
    // bumpy path
    ctx.arc(w - 160, 95, 24, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Wrinkled Green Parent', w - 160, 145);
    ctx.fillStyle = '#86efac';
    ctx.font = 'bold 12px monospace';
    ctx.fillText('Genotype: rryy (Gamete: ry)', w - 160, 165);

    if (slide9State.crossed) {
        // Arrow to F1
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(160, 180);
        ctx.lineTo(w * 0.5, 215);
        ctx.moveTo(w - 160, 180);
        ctx.lineTo(w * 0.5, 215);
        ctx.stroke();

        // F1 seed
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(w * 0.5, 245, 26, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('F1 Generation: 100% Round Yellow Seeds', w * 0.5, 290);
        ctx.fillStyle = '#fde68a';
        ctx.font = 'bold 12px monospace';
        ctx.fillText('Genotype: RrYy (All Heterozygous Dihybrids)', w * 0.5, 310);
    } else {
        ctx.fillStyle = '#94a3b8';
        ctx.font = '12px sans-serif';
        ctx.fillText('Click "Perform Dihybrid Cross" to fertilize and observe the F1 generation.', w * 0.5, 250);
    }
}

// ==========================================
// SIMULATOR 10: Law of Independent Assortment
// ==========================================
let slide10State = { filter: 'all' };

function initSlide10() {
    filterSlide10Seeds('all');
}

function filterSlide10Seeds(filter) {
    slide10State.filter = filter;
    const btnAll = document.getElementById('btnSlide10All');
    const btnPar = document.getElementById('btnSlide10Parental');
    const btnRec = document.getElementById('btnSlide10Recomb');

    [btnAll, btnPar, btnRec].forEach(b => {
        if (b) b.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    });
    if (filter === 'all' && btnAll) btnAll.className = 'px-2.5 py-1 rounded-lg bg-indigo-600 text-white text-xs font-semibold';
    if (filter === 'parental' && btnPar) btnPar.className = 'px-2.5 py-1 rounded-lg bg-indigo-600 text-white text-xs font-semibold';
    if (filter === 'recombinant' && btnRec) btnRec.className = 'px-2.5 py-1 rounded-lg bg-indigo-600 text-white text-xs font-semibold';

    drawSlide10();
}

function drawSlide10() {
    const canvas = document.getElementById('slide10Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const gametes = ['RY', 'Ry', 'rY', 'ry'];
    const phenotypes = [
        // row 0 (RY)
        ['RY', 'RY', 'RY', 'RY'],
        // row 1 (Ry)
        ['RY', 'RG', 'RY', 'RG'],
        // row 2 (rY)
        ['RY', 'RY', 'WY', 'WY'],
        // row 3 (ry)
        ['RY', 'RG', 'WY', 'WG']
    ];

    const sX = w * 0.5 - 120, sY = 40, cellSize = 55;

    // Gametes top
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 12px monospace';
    ctx.textAlign = 'center';
    for (let c = 0; c < 4; c++) {
        ctx.fillText(gametes[c], sX + c * cellSize + cellSize * 0.5, sY - 10);
    }
    // Gametes left
    ctx.fillStyle = '#ec4899';
    for (let r = 0; r < 4; r++) {
        ctx.fillText(gametes[r], sX - 25, sY + r * cellSize + cellSize * 0.5 + 4);
    }

    const typeColors = {
        RY: { bg: '#b45309', fill: '#fde047', txt: 'Round Yellow' },
        RG: { bg: '#047857', fill: '#86efac', txt: 'Round Green' },
        WY: { bg: '#854d0e', fill: '#fef08a', txt: 'Wrinkled Yellow' },
        WG: { bg: '#1e3a8a', fill: '#22c55e', txt: 'Wrinkled Green' }
    };

    for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
            const type = phenotypes[r][c];
            const isParental = (type === 'RY' || type === 'WG');
            const isRecomb = (type === 'RG' || type === 'WY');

            let opacity = 1.0;
            if (slide10State.filter === 'parental' && !isParental) opacity = 0.2;
            if (slide10State.filter === 'recombinant' && !isRecomb) opacity = 0.2;

            ctx.globalAlpha = opacity;
            const cX = sX + c * cellSize;
            const cY = sY + r * cellSize;

            ctx.fillStyle = typeColors[type].bg;
            ctx.fillRect(cX, cY, cellSize, cellSize);

            ctx.strokeStyle = '#1e293b';
            ctx.lineWidth = 1.5;
            ctx.strokeRect(cX, cY, cellSize, cellSize);

            // Mini seed circle
            ctx.fillStyle = typeColors[type].fill;
            ctx.beginPath();
            ctx.arc(cX + cellSize * 0.5, cY + cellSize * 0.45, 12, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 9px monospace';
            ctx.fillText(type, cX + cellSize * 0.5, cY + cellSize * 0.85);
            ctx.globalAlpha = 1.0;
        }
    }

    ctx.fillStyle = '#cbd5e1';
    ctx.font = '11px sans-serif';
    ctx.fillText('Mendelian Ratio: 9 Round Yellow : 3 Round Green : 3 Wrinkled Yellow : 1 Wrinkled Green (9:3:3:1)', w * 0.5, h - 20);
}

// ==========================================
// SIMULATOR 11: Gene Expression Mechanism
// ==========================================
let slide11State = { mutated: false, transcribed: false };

function initSlide11() {
    slide11State = { mutated: false, transcribed: false };
    drawSlide11();
}

function toggleSlide11Mutation() {
    slide11State.mutated = !slide11State.mutated;
    const btn = document.getElementById('btnSlide11Mut');
    const dCode = document.getElementById('slide11DNACode');
    const rCode = document.getElementById('slide11RNACode');
    const pStat = document.getElementById('slide11ProteinStatus');

    if (slide11State.mutated) {
        if (btn) btn.className = 'px-3 py-1.5 rounded-xl bg-amber-600 text-white text-xs font-semibold shadow-md transition-all';
        if (dCode) dCode.textContent = 'TAC-GTC-TTA-ACT (Mutated)';
        if (rCode) rCode.textContent = 'AUG-CAG-AAU-UGA';
        if (pStat) {
            pStat.textContent = 'Less Efficient Enzyme (20%)';
            pStat.className = 'text-xs font-bold text-amber-400';
        }
    } else {
        if (btn) btn.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (dCode) dCode.textContent = 'TAC-GGC-TTA-ACT';
        if (rCode) rCode.textContent = 'AUG-CCG-AAU-UGA';
        if (pStat) {
            pStat.textContent = 'Active Enzyme (100%)';
            pStat.className = 'text-xs font-bold text-emerald-400';
        }
    }
    drawSlide11();
}

function transcribeSlide11Gene() {
    slide11State.transcribed = true;
    drawSlide11();
}

function drawSlide11() {
    const canvas = document.getElementById('slide11Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Step 1: Cellular DNA (Gene Segment)
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('1. Nuclear DNA (Gene Segment)', 50, 45);

    ctx.strokeStyle = slide11State.mutated ? '#f59e0b' : '#0284c7';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(50, 70);
    ctx.lineTo(w - 50, 70);
    ctx.stroke();

    const dnaStr = slide11State.mutated ? 'T A C   G T C   T T A   A C T' : 'T A C   G G C   T T A   A C T';
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 13px monospace';
    ctx.fillText(dnaStr, 60, 65);

    // Step 2: mRNA Transcript
    ctx.fillStyle = '#10b981';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('2. Messenger RNA (Transcription)', 50, 130);

    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(50, 155);
    ctx.lineTo(w - 50, 155);
    ctx.stroke();
    ctx.setLineDash([]);

    const rnaStr = slide11State.mutated ? 'A U G   C A G   A A U   U G A' : 'A U G   C C G   A A U   U G A';
    ctx.fillStyle = '#a7f3d0';
    ctx.font = 'bold 13px monospace';
    ctx.fillText(rnaStr, 60, 150);

    // Step 3: Protein / Enzyme
    ctx.fillStyle = '#ec4899';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('3. Functional Protein / Enzyme (Translation on Ribosome)', 50, 215);

    // Folded enzyme shape
    ctx.fillStyle = slide11State.mutated ? '#f59e0b' : '#8b5cf6';
    ctx.beginPath();
    ctx.roundRect(w * 0.5 - 70, 230, 140, 50, 16);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(slide11State.mutated ? 'Altered Enzyme (Less Active)' : 'Active Growth Enzyme', w * 0.5, 260);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Genes provide the code for enzymes that control cellular biochemical pathways.', w * 0.5, h - 20);
}

// ==========================================
// SIMULATOR 12: Enzymes & Hormone Control
// ==========================================
let slide12State = { eff: 100 };

function initSlide12() {
    setSlide12EnzymeLevel(100);
}

function setSlide12EnzymeLevel(val) {
    slide12State.eff = parseInt(val);
    const slider = document.getElementById('slide12Slider');
    if (slider) slider.value = val;
    updateSlide12();
}

function setSlide12EnzymeSlider(val) {
    slide12State.eff = parseInt(val);
    updateSlide12();
}

function updateSlide12() {
    const disp = document.getElementById('slide12EffDisplay');
    const horm = document.getElementById('slide12HormoneLevel');
    const pheno = document.getElementById('slide12Phenotype');
    const status = document.getElementById('slide12Status');

    if (disp) disp.textContent = `${slide12State.eff}%`;
    if (horm) {
        if (slide12State.eff >= 60) {
            horm.textContent = `High (${slide12State.eff} ppm)`;
            horm.className = 'text-emerald-400 font-bold';
        } else {
            horm.textContent = `Low (${slide12State.eff} ppm)`;
            horm.className = 'text-rose-400 font-bold';
        }
    }
    if (pheno) {
        pheno.textContent = slide12State.eff >= 50 ? 'Tall Plant (Normal)' : 'Dwarf Plant (Stunted)';
        pheno.className = slide12State.eff >= 50 ? 'text-emerald-400 font-bold' : 'text-amber-400 font-bold';
    }

    drawSlide12();
}

function drawSlide12() {
    const canvas = document.getElementById('slide12Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Left side: Biochemical Pathway (Enzyme -> Hormone)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(40, 40, 240, 220, 12);
    ctx.fill();

    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Biochemical Hormone Factory', 160, 65);

    // Substrate box
    ctx.fillStyle = '#334155';
    ctx.roundRect(60, 90, 80, 35, 6);
    ctx.fill();
    ctx.fillStyle = '#cbd5e1';
    ctx.font = '10px sans-serif';
    ctx.fillText('Precursor', 100, 112);

    // Arrow with Enzyme
    ctx.strokeStyle = slide12State.eff >= 50 ? '#10b981' : '#f59e0b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(145, 107);
    ctx.lineTo(185, 107);
    ctx.stroke();

    ctx.fillStyle = '#fde047';
    ctx.font = 'bold 10px sans-serif';
    ctx.fillText(`Enzyme (${slide12State.eff}%)`, 165, 95);

    // Growth Hormone Box
    ctx.fillStyle = slide12State.eff >= 50 ? '#065f46' : '#7f1d1d';
    ctx.roundRect(190, 90, 80, 35, 6);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 10px sans-serif';
    ctx.fillText('Auxin / Hormone', 230, 112);

    // Hormone emission dots
    const dotCount = Math.floor(slide12State.eff / 8);
    ctx.fillStyle = '#34d399';
    for (let i = 0; i < dotCount; i++) {
        const dx = 80 + (i * 27) % 160;
        const dy = 150 + (i * 17) % 80;
        ctx.beginPath();
        ctx.arc(dx, dy, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    // Right side: Pea Plant Growth
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 280, 40, 240, 220, 12);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Plant Phenotypic Height', w - 160, 65);

    // Soil line
    ctx.strokeStyle = '#78350f';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(w - 260, 220);
    ctx.lineTo(w - 60, 220);
    ctx.stroke();

    // Stem height proportional to enzyme efficiency (80px dwarf to 160px tall)
    const stemH = 50 + (slide12State.eff / 100) * 110;
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.moveTo(w - 160, 220);
    ctx.lineTo(w - 160, 220 - stemH);
    ctx.stroke();

    // Leaves at top
    ctx.fillStyle = '#4ade80';
    ctx.beginPath();
    ctx.ellipse(w - 180, 220 - stemH + 10, 18, 8, -0.4, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.ellipse(w - 140, 220 - stemH + 10, 18, 8, 0.4, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText(slide12State.eff >= 50 ? 'Tall Plant (High Hormone)' : 'Dwarf Plant (Low Hormone)', w - 160, h - 25);
}

// ==========================================
// SIMULATOR 13: Chromosomal Basis of Heredity
// ==========================================
let slide13State = { meiotic: false, fertilized: false };

function initSlide13() {
    slide13State = { meiotic: false, fertilized: false };
    drawSlide13();
}

function runSlide13Meiosis() {
    slide13State.meiotic = true;
    slide13State.fertilized = false;
    const gBadge = document.getElementById('slide13GametePloidy');
    if (gBadge) gBadge.textContent = 'Haploid (n = 1 of each pair)';
    drawSlide13();
}

function fuseSlide13Gametes() {
    slide13State.fertilized = true;
    const zBadge = document.getElementById('slide13ZygotePloidy');
    if (zBadge) zBadge.textContent = 'Restored Diploid (2n = 2 pairs)';
    drawSlide13();
}

function drawSlide13() {
    const canvas = document.getElementById('slide13Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Initial Diploid Somatic Cell (Left)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(40, 45, 170, 220, 12);
    ctx.fill();

    ctx.fillStyle = '#a855f7';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Diploid Cell (2n)', 125, 70);
    ctx.font = '10px sans-serif';
    ctx.fillStyle = '#cbd5e1';
    ctx.fillText('Homologous Pairs', 125, 88);

    // Pair 1: Chromosome 1A (blue) & 1B (pink)
    ctx.fillStyle = '#38bdf8';
    ctx.roundRect(90, 110, 16, 60, 4);
    ctx.fill();
    ctx.fillStyle = '#ec4899';
    ctx.roundRect(112, 110, 16, 60, 4);
    ctx.fill();

    // Pair 2: Chromosome 2A (green) & 2B (amber)
    ctx.fillStyle = '#10b981';
    ctx.roundRect(138, 125, 14, 45, 4);
    ctx.fill();
    ctx.fillStyle = '#f59e0b';
    ctx.roundRect(156, 125, 14, 45, 4);
    ctx.fill();

    if (slide13State.meiotic) {
        // Center: 4 Haploid Gametes
        ctx.fillStyle = '#0284c7';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Meiosis: 4 Haploid Gametes (n)', w * 0.5, 45);

        const gameteConfigs = [
            { x: w * 0.42, y: 80, c1: '#38bdf8', c2: '#10b981' },
            { x: w * 0.58, y: 80, c1: '#38bdf8', c2: '#f59e0b' },
            { x: w * 0.42, y: 175, c1: '#ec4899', c2: '#10b981' },
            { x: w * 0.58, y: 175, c1: '#ec4899', c2: '#f59e0b' }
        ];

        gameteConfigs.forEach(g => {
            ctx.fillStyle = '#0f172a';
            ctx.beginPath();
            ctx.arc(g.x, g.y + 35, 30, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = '#334155';
            ctx.stroke();

            // 1 from pair 1, 1 from pair 2
            ctx.fillStyle = g.c1;
            ctx.roundRect(g.x - 12, g.y + 15, 10, 38, 3);
            ctx.fill();
            ctx.fillStyle = g.c2;
            ctx.roundRect(g.x + 2, g.y + 22, 10, 30, 3);
            ctx.fill();
        });
    }

    if (slide13State.fertilized) {
        // Right: Restored Zygote
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(w - 190, 45, 160, 220, 12);
        ctx.fill();

        ctx.fillStyle = '#34d399';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Restored Zygote (2n)', w - 110, 70);
        ctx.font = '10px sans-serif';
        ctx.fillStyle = '#cbd5e1';
        ctx.fillText('Fusion Restores Pairs', w - 110, 88);

        // Reunited homologous pairs
        ctx.fillStyle = '#38bdf8';
        ctx.roundRect(w - 145, 110, 14, 55, 3);
        ctx.fill();
        ctx.fillStyle = '#ec4899';
        ctx.roundRect(w - 128, 110, 14, 55, 3);
        ctx.fill();

        ctx.fillStyle = '#10b981';
        ctx.roundRect(w - 105, 125, 12, 40, 3);
        ctx.fill();
        ctx.fillStyle = '#f59e0b';
        ctx.roundRect(w - 90, 125, 12, 40, 3);
        ctx.fill();
    }

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Meiosis ensures each gamete receives only one chromosome from each homologous pair.', w * 0.5, h - 20);
}

// ==========================================
// SIMULATOR 14: Sex Determination Cues
// ==========================================
let slide14State = { species: 'reptile', temp: 29 };

function initSlide14() {
    setSlide14Species('reptile');
}

function setSlide14Species(sp) {
    slide14State.species = sp;
    const ctrl = document.getElementById('slide14ControlArea');
    if (ctrl) {
        if (sp === 'reptile') {
            ctrl.innerHTML = `
                <div>
                    <label class="block text-xs font-medium text-slate-400 mb-1">Nest Incubation Temperature: <span id="slide14TempDisplay" class="text-amber-400 font-bold">${slide14State.temp}°C</span></label>
                    <input type="range" id="slide14TempSlider" min="24" max="34" value="${slide14State.temp}" oninput="setSlide14Temp(this.value)" class="w-full accent-amber-500 cursor-pointer">
                </div>
                <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    <span>Determined Sex: <strong id="slide14SexOutput" class="text-cyan-400">Mixed</strong></span>
                    <span>Mechanism: <strong class="text-white">Environmental Cue</strong></span>
                </div>
            `;
        } else if (sp === 'snail') {
            ctrl.innerHTML = `
                <div class="flex items-center gap-2">
                    <button onclick="toggleSlide14Snail()" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-semibold">Change Snail Sex</button>
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    Mechanism: <strong class="text-white">Sequential Hermaphroditism (Flexible Non-Genetic)</strong>
                </div>
            `;
        } else {
            ctrl.innerHTML = `
                <div class="flex items-center gap-2">
                    <span class="text-xs text-slate-300">Human Genetic Sex Determination: XX (Female) / XY (Male)</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    Mechanism: <strong class="text-white">Strictly Genetic at Fertilization</strong>
                </div>
            `;
        }
    }
    updateSlide14();
}

function setSlide14Temp(t) {
    slide14State.temp = parseInt(t);
    const disp = document.getElementById('slide14TempDisplay');
    const out = document.getElementById('slide14SexOutput');
    if (disp) disp.textContent = `${slide14State.temp}°C`;

    if (out) {
        if (slide14State.temp <= 27) out.textContent = '100% Male (Cooler Nest)';
        else if (slide14State.temp >= 31) out.textContent = '100% Female (Warmer Nest)';
        else out.textContent = 'Mixed (50% Male / 50% Female)';
    }
    drawSlide14();
}

function toggleSlide14Snail() {
    drawSlide14();
}

function updateSlide14() {
    drawSlide14();
}

function drawSlide14() {
    const canvas = document.getElementById('slide14Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    if (slide14State.species === 'reptile') {
        // Turtle / Lizard Temperature Curve
        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 13px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Reptilian Temperature-Dependent Sex Determination', w * 0.5, 40);

        // Thermometer / Nest Graphic
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(80, 65, w - 160, 160, 12);
        ctx.fill();

        // Temperature Bar
        const barW = w - 240;
        const grad = ctx.createLinearGradient(120, 0, 120 + barW, 0);
        grad.addColorStop(0, '#38bdf8'); // cool = male
        grad.addColorStop(0.5, '#a855f7');
        grad.addColorStop(1, '#f43f5e'); // warm = female

        ctx.fillStyle = grad;
        ctx.roundRect(120, 100, barW, 25, 6);
        ctx.fill();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('< 28°C: All Males 🐢', 160, 145);

        ctx.fillStyle = '#f43f5e';
        ctx.fillText('> 31°C: All Females 🐢', w - 180, 145);

        // Marker for current temp
        const markerX = 120 + ((slide14State.temp - 24) / 10) * barW;
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.moveTo(markerX, 90);
        ctx.lineTo(markerX - 8, 75);
        ctx.lineTo(markerX + 8, 75);
        ctx.closePath();
        ctx.fill();

        ctx.font = 'bold 13px sans-serif';
        ctx.fillText(`${slide14State.temp}°C`, markerX, 68);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px sans-serif';
        ctx.fillText('Environmental temperature controls enzyme activity (aromatase) that determines embryo sex.', w * 0.5, h - 25);

    } else if (slide14State.species === 'snail') {
        // Snail Diagram
        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 13px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Garden Snail: Flexible Sex Reversal', w * 0.5, 45);

        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(w * 0.5 - 120, 75, 240, 140, 16);
        ctx.fill();

        // Draw snail shell swirl
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.arc(w * 0.5, 140, 35, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Hermaphroditic Mollusk 🐌', w * 0.5, 195);

        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px sans-serif';
        ctx.fillText('Snails can change sex during their lifetime, demonstrating sex is not genetically fixed.', w * 0.5, h - 25);

    } else {
        // Humans
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 13px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Humans: Strictly Genetic Sex Determination at Fertilization', w * 0.5, 45);

        ctx.fillStyle = '#ec4899';
        ctx.font = 'bold 14px sans-serif';
        ctx.fillText('Female: 44 Autosomes + XX', w * 0.35, 120);

        ctx.fillStyle = '#3b82f6';
        ctx.fillText('Male: 44 Autosomes + XY', w * 0.65, 120);

        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px sans-serif';
        ctx.fillText('Environmental cues play zero role in human sex determination.', w * 0.5, h - 25);
    }
}

// ==========================================
// SIMULATOR 15: Human Karyotype (23 Pairs)
// ==========================================
let slide15State = { sex: 'female' };

function initSlide15() {
    setSlide15Karyotype('female');
}

function setSlide15Karyotype(sex) {
    slide15State.sex = sex;
    const btnF = document.getElementById('btnSlide15Female');
    const btnM = document.getElementById('btnSlide15Male');
    const sBadge = document.getElementById('slide15SexPairBadge');
    const gBadge = document.getElementById('slide15GameteBadge');

    if (sex === 'female') {
        if (btnF) btnF.className = 'px-3 py-1.5 rounded-xl bg-pink-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnM) btnM.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (sBadge) {
            sBadge.textContent = 'XX (Homogametic)';
            sBadge.className = 'text-xs font-bold text-pink-400';
        }
        if (gBadge) gBadge.textContent = '100% X-bearing Ova';
    } else {
        if (btnM) btnM.className = 'px-3 py-1.5 rounded-xl bg-blue-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnF) btnF.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (sBadge) {
            sBadge.textContent = 'XY (Heterogametic)';
            sBadge.className = 'text-xs font-bold text-blue-400';
        }
        if (gBadge) gBadge.textContent = '50% X / 50% Y Sperm';
    }

    drawSlide15();
}

function drawSlide15() {
    const canvas = document.getElementById('slide15Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Title
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(`Human Karyotype: 22 Autosomal Pairs + Pair 23 (${slide15State.sex.toUpperCase()})`, 40, 35);

    // Draw 22 autosomal chromosome pairs in a 4x6 grid on left
    const startX = 40, startY = 55;
    for (let i = 0; i < 22; i++) {
        const col = i % 8;
        const row = Math.floor(i / 8);
        const px = startX + col * 44;
        const py = startY + row * 45;

        // Pair of bars
        ctx.fillStyle = '#64748b';
        const barH = 26 - row * 3;
        ctx.roundRect(px, py, 6, barH, 2);
        ctx.fill();
        ctx.roundRect(px + 8, py, 6, barH, 2);
        ctx.fill();

        ctx.fillStyle = '#94a3b8';
        ctx.font = '9px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`${i + 1}`, px + 7, py + barH + 11);
    }

    // Pair 23 Spotlight Box (Right side)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 180, 50, 140, 180, 12);
    ctx.fill();

    ctx.strokeStyle = slide15State.sex === 'female' ? '#ec4899' : '#3b82f6';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Pair 23: Sex Chromosomes', w - 110, 75);

    if (slide15State.sex === 'female') {
        // Two full-size X chromosomes (pink)
        ctx.fillStyle = '#ec4899';
        ctx.roundRect(w - 135, 95, 16, 75, 4);
        ctx.fill();
        ctx.roundRect(w - 100, 95, 16, 75, 4);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('X', w - 127, 190);
        ctx.fillText('X', w - 92, 190);
    } else {
        // One normal X and one shorter Y (blue)
        ctx.fillStyle = '#38bdf8';
        ctx.roundRect(w - 135, 95, 16, 75, 4); // Full X
        ctx.fill();

        ctx.fillStyle = '#f43f5e';
        ctx.roundRect(w - 100, 125, 14, 45, 4); // Short Y
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('X', w - 127, 190);
        ctx.fillText('Y', w - 93, 190);
    }

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('The Y chromosome is significantly smaller than the X chromosome and triggers male development.', w * 0.5, h - 25);
}

// ==========================================
// SIMULATOR 16: Sex Inheritance Probability
// ==========================================
let slide16State = { total: 0, girls: 0, boys: 0 };

function initSlide16() {
    resetSlide16Stats();
}

function resetSlide16Stats() {
    slide16State = { total: 0, girls: 0, boys: 0 };
    updateSlide16UI();
    drawSlide16();
}

function simulateSlide16Birth(n) {
    for (let i = 0; i < n; i++) {
        slide16State.total++;
        if (Math.random() < 0.5) {
            slide16State.girls++;
        } else {
            slide16State.boys++;
        }
    }
    updateSlide16UI();
    drawSlide16();
}

function simulateSlide16Batch(n) {
    simulateSlide16Birth(n);
}

function updateSlide16UI() {
    const t = document.getElementById('slide16TotalCount');
    const g = document.getElementById('slide16GirlCount');
    const b = document.getElementById('slide16BoyCount');

    if (t) t.textContent = slide16State.total;
    if (g) {
        const pct = slide16State.total > 0 ? ((slide16State.girls / slide16State.total) * 100).toFixed(1) : '50.0';
        g.textContent = `${slide16State.girls} (${pct}%)`;
    }
    if (b) {
        const pct = slide16State.total > 0 ? ((slide16State.boys / slide16State.total) * 100).toFixed(1) : '50.0';
        b.textContent = `${slide16State.boys} (${pct}%)`;
    }
}

function drawSlide16() {
    const canvas = document.getElementById('slide16Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Left side: 2x2 Sex Determination Punnett Square
    const sX = 80, sY = 55, cellSize = 65;

    // Mother Gametes Top
    ctx.fillStyle = '#ec4899';
    ctx.font = 'bold 14px monospace';
    ctx.textAlign = 'center';
    ctx.fillText('X (Mom)', sX + cellSize * 0.5, sY - 12);
    ctx.fillText('X (Mom)', sX + cellSize * 1.5, sY - 12);

    // Father Gametes Left
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('X (Dad)', sX - 35, sY + cellSize * 0.5 + 5);
    ctx.fillText('Y (Dad)', sX - 35, sY + cellSize * 1.5 + 5);

    // Grid: Row 0 (X sperm) -> XX, XX (Girls)
    // Grid: Row 1 (Y sperm) -> XY, XY (Boys)
    const gridData = [
        [['XX (Girl)', '#ec4899', '#831843'], ['XX (Girl)', '#ec4899', '#831843']],
        [['XY (Boy)', '#38bdf8', '#1e3a8a'], ['XY (Boy)', '#38bdf8', '#1e3a8a']]
    ];

    for (let r = 0; r < 2; r++) {
        for (let c = 0; c < 2; c++) {
            const [txt, col, bg] = gridData[r][c];
            const cX = sX + c * cellSize;
            const cY = sY + r * cellSize;

            ctx.fillStyle = bg;
            ctx.fillRect(cX, cY, cellSize, cellSize);

            ctx.strokeStyle = '#334155';
            ctx.strokeRect(cX, cY, cellSize, cellSize);

            ctx.fillStyle = col;
            ctx.font = 'bold 12px sans-serif';
            ctx.fillText(txt, cX + cellSize * 0.5, cY + cellSize * 0.55);
        }
    }

    // Right side: Real-time Probability Bar Graph
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 280, 40, 240, 180, 12);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Statistical Distribution (50:50 Odds)', w - 160, 65);

    const maxBarH = 90;
    const gH = slide16State.total > 0 ? (slide16State.girls / slide16State.total) * maxBarH : 45;
    const bH = slide16State.total > 0 ? (slide16State.boys / slide16State.total) * maxBarH : 45;

    // Girl Bar
    ctx.fillStyle = '#ec4899';
    ctx.fillRect(w - 230, 180 - gH, 45, gH);
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('XX 👧', w - 208, 198);

    // Boy Bar
    ctx.fillStyle = '#38bdf8';
    ctx.fillRect(w - 140, 180 - bH, 45, bH);
    ctx.fillText('XY 👦', w - 118, 198);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Every pregnancy is an independent event with equal 50% probability for a boy or girl.', w * 0.5, h - 25);
}
'''

if __name__ == "__main__":
    print("SIMULATOR_JS length:", len(SIMULATOR_JS))

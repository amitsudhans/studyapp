# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 7: How do Organisms Reproduce?
Interactive Canvas & Simulator JavaScript Handlers
"""

SIMULATOR_JS = '''
// ==========================================
// SIMULATOR 1: Reproduction Biological Purpose
// ==========================================
let slide1State = { mode: 'continuity' };

function initSlide1() {
    setSlide1Scenario('continuity');
}

function setSlide1Scenario(mode) {
    slide1State.mode = mode;
    const canvas = document.getElementById('slide1Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide1Status');

    drawSlide1(ctx, canvas.width, canvas.height, mode);

    if (mode === 'extinction') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">No Reproduction (Extinction):</span> A solitary organism lives its natural lifespan, but when it dies, its entire species lineage disappears permanently from the ecological niche.';
    } else {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Continuous Reproduction (Species Survival):</span> Through reproduction, mature organisms continually generate offspring, maintaining population density and ensuring species visibility across generations.';
    }
}

function drawSlide1(ctx, w, h, mode) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    if (mode === 'extinction') {
        // Solitary organism timeline -> extinction
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(60, h * 0.5);
        ctx.lineTo(w - 60, h * 0.5);
        ctx.stroke();
        ctx.setLineDash([]);

        // Generation 1: Single individual
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(120, h * 0.5, 20, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Solitary Parent', 80, h * 0.5 + 40);

        // Generation 2: Aging
        ctx.fillStyle = '#64748b';
        ctx.beginPath();
        ctx.arc(280, h * 0.5, 18, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('Aging Organism', 240, h * 0.5 + 40);

        // Generation 3: Death / Extinction
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(460, h * 0.5, 8, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(445, h * 0.5 - 15);
        ctx.lineTo(475, h * 0.5 + 15);
        ctx.moveTo(475, h * 0.5 - 15);
        ctx.lineTo(445, h * 0.5 + 15);
        ctx.stroke();

        ctx.fillStyle = '#f87171';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('PERMANENT EXTINCTION (0 Individuals)', 340, h * 0.5 + 40);

    } else {
        // Continuous reproduction branching tree
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;

        const startX = 80, startY = h * 0.5;

        // Parent
        ctx.fillStyle = '#34d399';
        ctx.beginPath();
        ctx.arc(startX, startY, 20, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Generation 1', startX - 35, startY - 30);

        // Branch to Gen 2
        const g2X = 260;
        ctx.beginPath();
        ctx.moveTo(startX + 20, startY);
        ctx.lineTo(g2X - 16, startY - 60);
        ctx.moveTo(startX + 20, startY);
        ctx.lineTo(g2X - 16, startY + 60);
        ctx.stroke();

        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(g2X, startY - 60, 16, 0, Math.PI * 2);
        ctx.arc(g2X, startY + 60, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Generation 2 (Offspring)', g2X - 55, 35);

        // Branch to Gen 3
        const g3X = 460;
        const g3Ys = [startY - 90, startY - 30, startY + 30, startY + 90];
        ctx.beginPath();
        ctx.moveTo(g2X + 16, startY - 60);
        ctx.lineTo(g3X - 14, g3Ys[0]);
        ctx.moveTo(g2X + 16, startY - 60);
        ctx.lineTo(g3X - 14, g3Ys[1]);
        ctx.moveTo(g2X + 16, startY + 60);
        ctx.lineTo(g3X - 14, g3Ys[2]);
        ctx.moveTo(g2X + 16, startY + 60);
        ctx.lineTo(g3X - 14, g3Ys[3]);
        ctx.stroke();

        ctx.fillStyle = '#059669';
        g3Ys.forEach(y => {
            ctx.beginPath();
            ctx.arc(g3X, y, 14, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#4ade80';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Generation 3 (Stable Population Expansion)', g3X - 110, h - 25);
    }
}

// ==========================================
// SIMULATOR 2: DNA Replication Blueprint
// ==========================================
let slide2Progress = 0;
let slide2Anim = null;
let slide2Active = false;

function initSlide2() {
    resetSlide2();
}

function resetSlide2() {
    slide2Active = false;
    slide2Progress = 0;
    if (slide2Anim) cancelAnimationFrame(slide2Anim);
    const canvas = document.getElementById('slide2Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide2(ctx, canvas.width, canvas.height, 0);
    const status = document.getElementById('slide2Status');
    if (status) status.innerHTML = 'Single parent cell with DNA double helix. Click <b>"Duplicate DNA & Cell"</b> to observe replication and division.';
}

function triggerSlide2Replication() {
    if (slide2Active) return;
    slide2Active = true;
    slide2Progress = 0;
    const canvas = document.getElementById('slide2Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide2Status');

    function animate() {
        slide2Progress += 0.015;
        drawSlide2(ctx, canvas.width, canvas.height, slide2Progress);

        if (slide2Progress < 0.3) {
            if (status) status.innerHTML = '<span class="text-amber-400 font-bold">1. Biochemical DNA Unwinding:</span> Replication enzymes duplicate genetic strands, occasionally introducing subtle base-pair variations.';
        } else if (slide2Progress < 0.7) {
            if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">2. Cellular Apparatus Synthesis:</span> Fresh cytoplasm, enzyme complexes, and mitochondria organelles are synthesized simultaneously.';
        } else if (slide2Progress <= 1.0) {
            if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">3. Cytokinesis & Separation:</span> Two viable daughter cells form, each equipped with its own DNA copy and complete metabolic apparatus.';
        }

        if (slide2Progress < 1.0) {
            slide2Anim = requestAnimationFrame(animate);
        } else {
            slide2Active = false;
        }
    }
    animate();
}

function drawSlide2(ctx, w, h, p) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060c18';
    ctx.fillRect(0, 0, w, h);

    const midY = h * 0.5;

    if (p < 0.6) {
        // Single cell expanding and elongating
        const cellW = 120 + 80 * (p / 0.6);
        const cellH = 100;
        const cX = w * 0.5;

        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(cX - cellW / 2, midY - cellH / 2, cellW, cellH, 30);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.stroke();

        // DNA Double Helix strands
        const strandDist = 30 * (p / 0.6);
        drawDnaStrand(ctx, cX - strandDist, midY, 60, '#38bdf8');
        if (p > 0.15) {
            drawDnaStrand(ctx, cX + strandDist, midY, 60, '#f59e0b');
        }

        ctx.fillStyle = '#94a3b8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Replicating Parent Cell & Organelles', cX - 100, midY - 65);

    } else {
        // Cell cleaved into two daughter cells
        const sepP = (p - 0.6) / 0.4;
        const c1X = w * 0.5 - 50 - sepP * 70;
        const c2X = w * 0.5 + 50 + sepP * 70;

        // Daughter Cell 1
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(c1X - 60, midY - 50, 120, 100, 24);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.stroke();
        drawDnaStrand(ctx, c1X, midY, 50, '#38bdf8');

        // Daughter Cell 2 (Subtle Variation in color)
        ctx.beginPath();
        ctx.roundRect(c2X - 60, midY - 50, 120, 100, 24);
        ctx.fill();
        ctx.strokeStyle = '#10b981';
        ctx.stroke();
        drawDnaStrand(ctx, c2X, midY, 50, '#34d399');

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Daughter Cell 1', c1X - 45, midY + 70);

        ctx.fillStyle = '#34d399';
        ctx.fillText('Daughter Cell 2 (Subtle Variation)', c2X - 85, midY + 70);
    }
}

function drawDnaStrand(ctx, x, y, len, color) {
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.beginPath();
    for (let dy = -len / 2; dy <= len / 2; dy += 6) {
        const dx = Math.sin(dy * 0.15) * 12;
        if (dy === -len / 2) ctx.moveTo(x + dx, y + dy);
        else ctx.lineTo(x + dx, y + dy);
    }
    ctx.stroke();

    ctx.strokeStyle = '#e2e8f0';
    ctx.lineWidth = 1.5;
    for (let dy = -len / 2; dy <= len / 2; dy += 12) {
        const dx = Math.sin(dy * 0.15) * 12;
        ctx.beginPath();
        ctx.moveTo(x - dx, y + dy);
        ctx.lineTo(x + dx, y + dy);
        ctx.stroke();
    }
}

// ==========================================
// SIMULATOR 3: Evolutionary Variation Importance
// ==========================================
let slide3Temp = 'normal';

function initSlide3() {
    setSlide3Temp('normal');
}

function setSlide3Temp(temp) {
    slide3Temp = temp;
    const canvas = document.getElementById('slide3Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide3Status');

    drawSlide3(ctx, canvas.width, canvas.height, temp);

    if (temp === 'normal') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Normal Pond (25°C):</span> Both standard temperate bacteria (cyan) and rare heat-resistant mutant variants (amber) flourish comfortably in the stable niche.';
    } else {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Thermal Shock (45°C):</span> Elevated temperature denatures proteins in standard bacteria, causing mass mortality. Only pre-existing heat-resistant variants survive and replenish the colony.';
    }
}

function drawSlide3(ctx, w, h, temp) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = (temp === 'normal') ? '#081426' : '#2b0b0e';
    ctx.fillRect(0, 0, w, h);

    // Pond outline
    ctx.strokeStyle = (temp === 'normal') ? '#0284c7' : '#e11d48';
    ctx.lineWidth = 4;
    ctx.strokeRect(30, 30, w - 60, h - 60);

    ctx.fillStyle = (temp === 'normal') ? '#38bdf8' : '#f43f5e';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText(temp === 'normal' ? 'Temperate Pond Basin (Water Temperature: 25°C)' : 'Thermal Shock Influx (Water Temperature: 45°C)', 45, 55);

    // Bacteria population
    const totalBact = 28;
    for (let i = 0; i < totalBact; i++) {
        const bx = 60 + ((i * 73) % (w - 120));
        const by = 80 + ((i * 47) % (h - 140));
        const isResistant = (i % 7 === 0); // ~14% are heat-resistant

        if (temp === 'normal') {
            // All alive
            ctx.fillStyle = isResistant ? '#f59e0b' : '#38bdf8';
            ctx.beginPath();
            ctx.ellipse(bx, by, 12, 6, i * 0.3, 0, Math.PI * 2);
            ctx.fill();
        } else {
            // Thermal shock: standard bacteria dead (ghostly gray cross), resistant thriving
            if (isResistant) {
                ctx.fillStyle = '#f59e0b';
                ctx.beginPath();
                ctx.ellipse(bx, by, 14, 7, i * 0.3, 0, Math.PI * 2);
                ctx.fill();
                // Glow
                ctx.strokeStyle = '#fef08a';
                ctx.lineWidth = 1.5;
                ctx.stroke();
            } else {
                ctx.strokeStyle = '#475569';
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                ctx.moveTo(bx - 6, by - 6);
                ctx.lineTo(bx + 6, by + 6);
                ctx.moveTo(bx + 6, by - 6);
                ctx.lineTo(bx - 6, by + 6);
                ctx.stroke();
            }
        }
    }

    // Legend
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('● Standard Temperate Bacteria', 50, h - 45);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('● Heat-Resistant Variant (Pre-existing DNA Variation)', 260, h - 45);
}

// ==========================================
// SIMULATOR 4: Cellular Fission Modes
// ==========================================
let slide4Mode = 'amoeba';

function initSlide4() {
    setSlide4Mode('amoeba');
}

function setSlide4Mode(mode) {
    slide4Mode = mode;
    const canvas = document.getElementById('slide4Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide4Status');

    drawSlide4(ctx, canvas.width, canvas.height, mode);

    if (mode === 'amoeba') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Amoeba Binary Fission:</span> Irregular cell outline without fixed polarity. Nucleus elongates and splits, followed by cytokinesis furrowing across any arbitrary geometric plane.';
    } else if (mode === 'leishmania') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Leishmania Binary Fission:</span> Elongated organism causing Kala-azar. Possesses a whip-like flagellum; binary fission occurs strictly along a definite longitudinal axis.';
    } else {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Plasmodium Multiple Fission:</span> Malarial parasite encysts within red blood cells. The nucleus divides repeatedly into dozens of daughter nuclei, bursting the cyst simultaneously.';
    }
}

function drawSlide4(ctx, w, h, mode) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060d1b';
    ctx.fillRect(0, 0, w, h);

    const midY = h * 0.5;

    if (mode === 'amoeba') {
        // Step 1: Parent Amoeba
        drawAmoebaCell(ctx, 110, midY, 32, '#059669', '#34d399');
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('1. Mature Amoeba', 65, midY + 65);

        // Arrow
        drawArrow(ctx, 160, midY, 210, midY);

        // Step 2: Nuclear elongation & cleavage furrow (Any plane)
        drawConstrictedAmoeba(ctx, 270, midY);
        ctx.fillText('2. Cleavage (Any Plane)', 210, midY + 65);

        drawArrow(ctx, 330, midY, 380, midY);

        // Step 3: Two daughter amoebae
        drawAmoebaCell(ctx, 440, midY - 25, 20, '#059669', '#34d399');
        drawAmoebaCell(ctx, 440, midY + 25, 20, '#059669', '#34d399');
        ctx.fillText('3. Two Daughter Cells', 385, midY + 65);

    } else if (mode === 'leishmania') {
        // Leishmania with whip-like flagellum
        // Step 1: Single Leishmania
        drawLeishmaniaCell(ctx, 120, midY, 0);
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('1. Whip-like Flagellum', 70, midY + 70);

        drawArrow(ctx, 175, midY, 230, midY);

        // Step 2: Longitudinal cleavage furrow
        drawLeishmaniaDividing(ctx, 290, midY);
        ctx.fillText('2. Longitudinal Splitting', 230, midY + 70);

        drawArrow(ctx, 350, midY, 405, midY);

        // Step 3: Two separate flagellated daughter cells
        drawLeishmaniaCell(ctx, 450, midY - 28, -0.2);
        drawLeishmaniaCell(ctx, 470, midY + 28, 0.2);
        ctx.fillText('3. Two Daughter Organisms', 390, midY + 70);

    } else {
        // Plasmodium Multiple Fission
        const cX = w * 0.45;

        // Cyst Wall
        ctx.strokeStyle = '#d97706';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.arc(cX, midY, 65, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = 'rgba(217, 119, 6, 0.15)';
        ctx.fill();

        // Numerous daughter nuclei
        for (let a = 0; a < Math.PI * 2; a += 0.35) {
            const r = 20 + ((a * 23) % 35);
            const nx = cX + Math.cos(a) * r;
            const ny = midY + Math.sin(a) * r;

            ctx.fillStyle = '#fbbf24';
            ctx.beginPath();
            ctx.arc(nx, ny, 5, 0, Math.PI * 2);
            ctx.fill();
        }

        ctx.fillStyle = '#fde68a';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Protective Cyst Capsule', cX - 65, midY - 80);
        ctx.fillText('Multiple Daughter Merozoites Dividing Simultaneously', cX - 140, midY + 95);
    }
}

function drawAmoebaCell(ctx, x, y, r, stroke, fill) {
    ctx.fillStyle = fill;
    ctx.strokeStyle = stroke;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.bezierCurveTo(x + r, y - r * 0.8, x + r * 0.2, y - r, x, y - r);
    ctx.bezierCurveTo(x - r * 0.6, y - r, x - r, y - r * 0.3, x - r, y);
    ctx.bezierCurveTo(x - r, y + r * 0.7, x - r * 0.3, y + r, x, y + r);
    ctx.bezierCurveTo(x + r * 0.5, y + r, x + r, y + r * 0.5, x + r, y);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    // Nucleus
    ctx.fillStyle = '#1e3a8a';
    ctx.beginPath();
    ctx.arc(x, y, r * 0.3, 0, Math.PI * 2);
    ctx.fill();
}

function drawConstrictedAmoeba(ctx, x, y) {
    ctx.fillStyle = '#34d399';
    ctx.strokeStyle = '#059669';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(x - 20, y, 22, 28, 0, 0, Math.PI * 2);
    ctx.ellipse(x + 20, y, 22, 28, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Elongated dividing nuclei
    ctx.fillStyle = '#1e3a8a';
    ctx.beginPath();
    ctx.arc(x - 20, y, 7, 0, Math.PI * 2);
    ctx.arc(x + 20, y, 7, 0, Math.PI * 2);
    ctx.fill();
}

function drawLeishmaniaCell(ctx, x, y, angle) {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(angle);

    // Elongated body
    ctx.fillStyle = '#38bdf8';
    ctx.strokeStyle = '#0284c7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(0, 0, 32, 10, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Nucleus
    ctx.fillStyle = '#1e3a8a';
    ctx.beginPath();
    ctx.arc(-5, 0, 5, 0, Math.PI * 2);
    ctx.fill();

    // Whip flagellum
    ctx.strokeStyle = '#e0f2fe';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(32, 0);
    ctx.quadraticCurveTo(55, -15, 75, 5);
    ctx.stroke();

    ctx.restore();
}

function drawLeishmaniaDividing(ctx, x, y) {
    // Longitudinal splitting body
    ctx.fillStyle = '#38bdf8';
    ctx.strokeStyle = '#0284c7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(0 + x, -8 + y, 32, 8, 0, 0, Math.PI * 2);
    ctx.ellipse(0 + x, 8 + y, 32, 8, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Two flagella
    ctx.strokeStyle = '#e0f2fe';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(32 + x, -8 + y);
    ctx.quadraticCurveTo(55 + x, -20 + y, 70 + x, -5 + y);
    ctx.moveTo(32 + x, 8 + y);
    ctx.quadraticCurveTo(55 + x, 20 + y, 70 + x, 5 + y);
    ctx.stroke();
}

function drawArrow(ctx, x1, y1, x2, y2) {
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.lineTo(x2 - 6, y2 - 4);
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - 6, y2 + 4);
    ctx.stroke();
}

// ==========================================
// SIMULATOR 5: Budding Fragmentation Regeneration
// ==========================================
let slide5Type = 'yeast';

function initSlide5() {
    setSlide5Type('yeast');
}

function setSlide5Type(type) {
    slide5Type = type;
    const canvas = document.getElementById('slide5Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide5Status');

    drawSlide5(ctx, canvas.width, canvas.height, type);

    if (type === 'yeast') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Yeast Budding:</span> A small cellular outgrowth forms on the parent cell wall, receives a daughter nucleus, and detaches to live independently.';
    } else if (type === 'spirogyra') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Spirogyra Fragmentation:</span> Simple filamentous green alga breaks into smaller fragments upon reaching maturity, each fragment elongating into a complete new filament.';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Planaria Regeneration:</span> When cut into segments, specialized proliferating stem cells divide and differentiate into missing organs to rebuild whole worms.';
    }
}

function drawSlide5(ctx, w, h, type) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060f1e';
    ctx.fillRect(0, 0, w, h);

    const midY = h * 0.5;

    if (type === 'yeast') {
        // Parent cell with bud chain
        const cX = w * 0.4;
        ctx.fillStyle = '#d97706';
        ctx.beginPath();
        ctx.arc(cX, midY, 40, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Bud 1
        ctx.beginPath();
        ctx.arc(cX + 55, midY - 20, 24, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Bud 2
        ctx.beginPath();
        ctx.arc(cX + 90, midY - 35, 15, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#fef08a';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Parent Yeast Cell', cX - 45, midY + 65);
        ctx.fillText('Detachable Bud Chain', cX + 45, midY + 25);

    } else if (type === 'spirogyra') {
        // Long filament breaking into 2 fragments
        const startX = 60;
        const filW = 180;

        // Fragment 1
        drawSpirogyraSegment(ctx, startX, midY - 30, filW);
        // Fragment 2
        drawSpirogyraSegment(ctx, startX + filW + 50, midY - 30, filW);

        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(startX + filW + 25, midY - 50);
        ctx.lineTo(startX + filW + 25, midY + 40);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#86efac';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Fragment 1 (Elongates via mitosis)', startX + 15, midY + 45);
        ctx.fillText('Fragment 2 (Elongates via mitosis)', startX + filW + 65, midY + 45);

    } else {
        // Planaria Regeneration: Cut into 3 pieces, forming 3 complete worms
        const cX = 100;
        ctx.fillStyle = '#06b6d4';
        ctx.beginPath();
        ctx.ellipse(cX, midY, 20, 50, 0, 0, Math.PI * 2);
        ctx.fill();

        // Cut lines
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(cX - 30, midY - 15);
        ctx.lineTo(cX + 30, midY - 15);
        ctx.moveTo(cX - 30, midY + 15);
        ctx.lineTo(cX + 30, midY + 15);
        ctx.stroke();

        drawArrow(ctx, 150, midY, 220, midY);

        // 3 regenerated Planaria
        const pXs = [320, 390, 460];
        pXs.forEach((px, idx) => {
            ctx.fillStyle = '#06b6d4';
            ctx.beginPath();
            ctx.ellipse(px, midY, 15, 40, 0, 0, Math.PI * 2);
            ctx.fill();
            // Eyespots
            ctx.fillStyle = '#0f172a';
            ctx.beginPath();
            ctx.arc(px - 4, midY - 25, 2, 0, Math.PI * 2);
            ctx.arc(px + 4, midY - 25, 2, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Cut into 3 Segments', 50, midY + 75);
        ctx.fillText('3 Fully Regenerated Planaria', 300, midY + 75);
    }
}

function drawSpirogyraSegment(ctx, x, y, len) {
    ctx.strokeStyle = '#15803d';
    ctx.lineWidth = 3;
    ctx.strokeRect(x, y, len, 50);

    ctx.fillStyle = 'rgba(34, 197, 94, 0.15)';
    ctx.fillRect(x, y, len, 50);

    // Spiral ribbon chloroplast
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 4;
    ctx.beginPath();
    for (let dx = 0; dx < len; dx += 10) {
        const dy = 25 + Math.sin(dx * 0.1) * 18;
        if (dx === 0) ctx.moveTo(x + dx, y + dy);
        else ctx.lineTo(x + dx, y + dy);
    }
    ctx.stroke();
}

// ==========================================
// SIMULATOR 6: Vegetative Propagation Techniques
// ==========================================
let slide6Veg = 'bryophyllum';

function initSlide6() {
    setSlide6Veg('bryophyllum');
}

function setSlide6Veg(veg) {
    slide6Veg = veg;
    const canvas = document.getElementById('slide6Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide6Status');

    drawSlide6(ctx, canvas.width, canvas.height, veg);

    if (veg === 'bryophyllum') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Bryophyllum Leaf Margin:</span> Scalloped notches develop adventitious buds. When leaves detach and touch moist soil, these sprout roots and grow into new plants.';
    } else if (veg === 'potato') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Potato Tuber Eyes:</span> Underground stem tubers possess surface notches (eyes) with dormant buds that sprout vigorous green shoots in moisture.';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Tissue Culture (Micropropagation):</span> Shoot tip explant placed in nutrient medium -> forms undifferentiated callus -> hormone treatment differentiates disease-free plantlets.';
    }
}

function drawSlide6(ctx, w, h, veg) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#071220';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;
    const midY = h * 0.5;

    if (veg === 'bryophyllum') {
        // Large succulent leaf with notched plantlets
        ctx.fillStyle = '#166534';
        ctx.beginPath();
        ctx.ellipse(midX, midY, 130, 80, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Notches and mini plantlets
        const angles = [-2.2, -1.8, -1.2, -0.6, 0.6, 1.2, 1.8, 2.2];
        angles.forEach(a => {
            const bx = midX + Math.cos(a) * 130;
            const by = midY + Math.sin(a) * 80;

            // Mini plantlet leaves
            ctx.fillStyle = '#86efac';
            ctx.beginPath();
            ctx.ellipse(bx, by - 12, 8, 4, 0.3, 0, Math.PI * 2);
            ctx.ellipse(bx, by - 18, 8, 4, -0.3, 0, Math.PI * 2);
            ctx.fill();

            // Roots
            ctx.strokeStyle = '#fef08a';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(bx, by);
            ctx.lineTo(bx - 6, by + 12);
            ctx.moveTo(bx, by);
            ctx.lineTo(bx + 6, by + 12);
            ctx.stroke();
        });

        ctx.fillStyle = '#86efac';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Bryophyllum Leaf Margin Notches Bearing Plantlets', midX - 160, 45);

    } else if (veg === 'potato') {
        // Potato tuber with eyes sprouting shoots
        ctx.fillStyle = '#854d0e';
        ctx.beginPath();
        ctx.ellipse(midX, midY, 120, 70, 0.1, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ca8a04';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Eyes with sprouts
        const eyes = [
            { x: midX - 60, y: midY - 20 },
            { x: midX + 40, y: midY - 30 },
            { x: midX - 10, y: midY + 25 },
            { x: midX + 70, y: midY + 15 }
        ];

        eyes.forEach(e => {
            ctx.fillStyle = '#451a03';
            ctx.beginPath();
            ctx.ellipse(e.x, e.y, 10, 5, 0.2, 0, Math.PI * 2);
            ctx.fill();

            // Sprouting green shoot
            ctx.strokeStyle = '#22c55e';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(e.x, e.y);
            ctx.quadraticCurveTo(e.x - 8, e.y - 25, e.x, e.y - 35);
            ctx.stroke();

            ctx.fillStyle = '#4ade80';
            ctx.beginPath();
            ctx.arc(e.x, e.y - 35, 4, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#fde68a';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Potato Tuber "Eyes" (Vegetative Buds Sprouting)', midX - 140, 45);

    } else {
        // Tissue culture progression: Test tube explant -> Callus -> Plantlet
        // Step 1: Explant
        drawCultureVial(ctx, 110, midY, 'Shoot Explant');
        drawArrow(ctx, 160, midY, 210, midY);

        // Step 2: Callus
        drawCultureVial(ctx, 270, midY, 'Callus Mass');
        drawArrow(ctx, 320, midY, 370, midY);

        // Step 3: Differentiated Plantlet
        drawCultureVial(ctx, 430, midY, 'Plantlet');

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Micropropagation (Sterile Tissue Culture in Lab)', 130, 45);
    }
}

function drawCultureVial(ctx, x, y, label) {
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(x - 20, y - 45, 40, 90);

    // Nutrient jelly
    ctx.fillStyle = 'rgba(6, 182, 212, 0.2)';
    ctx.fillRect(x - 18, y + 10, 36, 33);

    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText(label, x - 35, y + 65);
}

// ==========================================
// SIMULATOR 7: Rhizopus Spore Formation
// ==========================================
let slide7Ruptured = false;

function initSlide7() {
    resetSlide7();
}

function resetSlide7() {
    slide7Ruptured = false;
    const canvas = document.getElementById('slide7Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide7(ctx, canvas.width, canvas.height, false);
    const status = document.getElementById('slide7Status');
    if (status) status.innerHTML = 'Intact Rhizopus bread mould sporangia capsules. Click <b>"Rupture & Disperse Spores"</b> to release spores into air.';
}

function triggerSlide7Rupture() {
    slide7Ruptured = true;
    const canvas = document.getElementById('slide7Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide7(ctx, canvas.width, canvas.height, true);
    const status = document.getElementById('slide7Status');
    if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Spore Dispersal:</span> Sporangium wall bursts, releasing hundreds of thick-walled microscopic spores into ambient air currents.';
}

function drawSlide7(ctx, w, h, ruptured) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#090e1a';
    ctx.fillRect(0, 0, w, h);

    const breadY = h * 0.78;

    // Bread substrate
    ctx.fillStyle = '#78350f';
    ctx.fillRect(40, breadY, w - 80, 50);
    ctx.fillStyle = '#d97706';
    ctx.font = '11px sans-serif';
    ctx.fillText('Moist Bread Substrate', 55, breadY + 30);

    // Horizontal Hyphae (Mycelium)
    ctx.strokeStyle = '#e2e8f0';
    ctx.lineWidth = 2;
    for (let x = 60; x < w - 80; x += 30) {
        ctx.beginPath();
        ctx.moveTo(x, breadY);
        ctx.lineTo(x + 25, breadY - 6);
        ctx.stroke();
    }

    // Erect Stalks
    const stalks = [150, 300, 450];
    stalks.forEach(sx => {
        ctx.strokeStyle = '#cbd5e1';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(sx, breadY);
        ctx.lineTo(sx, breadY - 110);
        ctx.stroke();

        const knobY = breadY - 110;

        if (ruptured) {
            // Burst open sporangium
            ctx.strokeStyle = '#f59e0b';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(sx, knobY, 22, 0.4, Math.PI * 1.6);
            ctx.stroke();

            // Dispersed spores floating
            ctx.fillStyle = '#fbbf24';
            for (let i = 0; i < 18; i++) {
                const spX = sx - 40 + ((i * 37) % 80);
                const spY = knobY - 50 + ((i * 29) % 65);
                ctx.beginPath();
                ctx.arc(spX, spY, 3, 0, Math.PI * 2);
                ctx.fill();
            }
        } else {
            // Intact globular sporangium
            ctx.fillStyle = '#1e293b';
            ctx.beginPath();
            ctx.arc(sx, knobY, 24, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = '#64748b';
            ctx.lineWidth = 3;
            ctx.stroke();

            ctx.fillStyle = '#94a3b8';
            ctx.font = 'bold 10px sans-serif';
            ctx.fillText('Sporangium', sx - 28, knobY - 32);
        }
    });

    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText(ruptured ? 'Ruptured Sporangia Discharging Thick-Walled Spores' : 'Aerial Hyphae with Intact Globular Sporangia', 130, 35);
}

// ==========================================
// SIMULATOR 8: Sexual Reproduction Logic
// ==========================================
let slide8Stage = 'meiosis';

function initSlide8() {
    setSlide8Stage('meiosis');
}

function setSlide8Stage(stage) {
    slide8Stage = stage;
    const canvas = document.getElementById('slide8Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide8Status');

    drawSlide8(ctx, canvas.width, canvas.height, stage);

    if (stage === 'meiosis') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Meiotic Halving (2n → n):</span> In gonads, germ-cells undergo reduction division, halving chromosome count so each gamete carries only one set (n=23 in humans).';
    } else {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Fertilization (n + n → 2n):</span> Motile sperm (n) fuses with nutrient ovum (n), precisely restoring the species diploid chromosome count (2n=46) in the zygote.';
    }
}

function drawSlide8(ctx, w, h, stage) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060d1b';
    ctx.fillRect(0, 0, w, h);

    const midY = h * 0.5;

    if (stage === 'meiosis') {
        // Diploid Parent Cell -> Haploid Gametes
        // Male Germ Cell (2n = 46)
        ctx.fillStyle = '#1e3a8a';
        ctx.beginPath();
        ctx.arc(120, midY - 45, 30, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Parent (2n)', 90, midY - 40);

        drawArrow(ctx, 160, midY - 45, 230, midY - 45);

        // Sperm (n = 23)
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(270, midY - 45, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('Sperm (n)', 245, midY - 40);

        // Female Germ Cell (2n = 46)
        ctx.fillStyle = '#831843';
        ctx.beginPath();
        ctx.arc(120, midY + 45, 30, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('Parent (2n)', 90, midY + 50);

        drawArrow(ctx, 160, midY + 45, 230, midY + 45);

        // Ovum (n = 23)
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(270, midY + 45, 22, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('Ovum (n)', 248, midY + 50);

        ctx.fillStyle = '#fde68a';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Meiosis (Reduction Division: 2n → n)', 170, 35);

    } else {
        // Fertilization: Sperm (n) + Ovum (n) -> Zygote (2n)
        // Sperm entering Ovum
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(140, midY, 12, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('Sperm (n=23)', 95, midY - 20);

        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(260, midY, 35, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Ovum (n=23)', 230, midY - 45);

        drawArrow(ctx, 310, midY, 370, midY);

        // Zygote (2n = 46)
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(440, midY, 40, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#4ade80';
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Zygote (2n=46)', 400, midY + 5);

        ctx.fillStyle = '#86efac';
        ctx.fillText('Diploid Number Restored', 380, midY + 65);
    }
}

// ==========================================
// SIMULATOR 9: Flower Anatomy Structure
// ==========================================
let slide9Whorl = 'all';

function initSlide9() {
    setSlide9Whorl('all');
}

function setSlide9Whorl(whorl) {
    slide9Whorl = whorl;
    const canvas = document.getElementById('slide9Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide9Status');

    drawSlide9(ctx, canvas.width, canvas.height, whorl);

    if (whorl === 'stamen') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Male Stamen (Androecium):</span> Slender filament supporting terminal bilobed anther, which produces thousands of yellow pollen grains containing male germ-cells.';
    } else if (whorl === 'carpel') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Female Carpel/Pistil (Gynoecium):</span> Terminal sticky stigma, slender style, and basal swollen ovary enclosing ovules, each housing an egg cell.';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Complete Flower Anatomy:</span> Four concentric whorls: Calyx (green sepals), Corolla (colored petals), Androecium (stamens), and Gynoecium (carpels).';
    }
}

function drawSlide9(ctx, w, h, whorl) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#07101e';
    ctx.fillRect(0, 0, w, h);

    const cX = w * 0.5;
    const baseY = h * 0.8;

    // Stem & Receptacle
    ctx.fillStyle = '#15803d';
    ctx.fillRect(cX - 8, baseY, 16, 50);
    ctx.beginPath();
    ctx.ellipse(cX, baseY, 35, 14, 0, 0, Math.PI * 2);
    ctx.fill();

    // Petals (Corolla)
    const showCorolla = (whorl === 'all');
    if (showCorolla) {
        ctx.fillStyle = 'rgba(236, 72, 153, 0.4)';
        ctx.beginPath();
        ctx.ellipse(cX - 90, baseY - 90, 50, 75, -0.4, 0, Math.PI * 2);
        ctx.ellipse(cX + 90, baseY - 90, 50, 75, 0.4, 0, Math.PI * 2);
        ctx.fill();
    }

    // Carpel (Pistil) - Center
    const showCarpel = (whorl === 'all' || whorl === 'carpel');
    if (showCarpel) {
        // Ovary
        ctx.fillStyle = '#166534';
        ctx.beginPath();
        ctx.ellipse(cX, baseY - 35, 30, 24, 0, 0, Math.PI * 2);
        ctx.fill();

        // Ovule inside ovary
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(cX, baseY - 35, 9, 0, Math.PI * 2);
        ctx.fill();

        // Style
        ctx.fillStyle = '#15803d';
        ctx.fillRect(cX - 6, baseY - 120, 12, 90);

        // Stigma (Sticky top)
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.ellipse(cX, baseY - 125, 18, 9, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fda4af';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Stigma (Sticky)', cX + 22, baseY - 125);
        ctx.fillText('Style', cX + 12, baseY - 75);
        ctx.fillText('Ovary with Ovule', cX + 35, baseY - 30);
    }

    // Stamens (Male)
    const showStamen = (whorl === 'all' || whorl === 'stamen');
    if (showStamen) {
        [-50, 50].forEach(sx => {
            ctx.strokeStyle = '#e2e8f0';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(cX + sx * 0.5, baseY - 20);
            ctx.quadraticCurveTo(cX + sx * 1.2, baseY - 70, cX + sx, baseY - 110);
            ctx.stroke();

            // Anther head
            ctx.fillStyle = '#eab308';
            ctx.beginPath();
            ctx.ellipse(cX + sx, baseY - 115, 10, 6, 0.3, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#facc15';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Anther (Pollen)', cX - 115, baseY - 115);
        ctx.fillText('Filament', cX - 95, baseY - 70);
    }
}

// ==========================================
// SIMULATOR 10: Plant Pollination Fertilization
// ==========================================
let slide10Anim = null;
let slide10P = 0;
let slide10Active = false;

function initSlide10() {
    resetSlide10();
}

function resetSlide10() {
    slide10Active = false;
    slide10P = 0;
    if (slide10Anim) cancelAnimationFrame(slide10Anim);
    const canvas = document.getElementById('slide10Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide10(ctx, canvas.width, canvas.height, 0);
    const status = document.getElementById('slide10Status');
    if (status) status.innerHTML = 'Pollen grain resting on stigma. Click <b>"Germinate Pollen Tube"</b> to trigger chemotropic growth down the style.';
}

function triggerSlide10Tube() {
    if (slide10Active) return;
    slide10Active = true;
    slide10P = 0;
    const canvas = document.getElementById('slide10Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide10Status');

    function animate() {
        slide10P += 0.012;
        drawSlide10(ctx, canvas.width, canvas.height, slide10P);

        if (slide10P < 0.4) {
            if (status) status.innerHTML = '<span class="text-amber-400 font-bold">1. Stigmatic Germination:</span> Pollen grain absorbs moisture and generates a pollen tube penetrating stigmatic tissue.';
        } else if (slide10P < 0.8) {
            if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">2. Chemotropic Elongation:</span> The pollen tube extends down through the style guided by chemical gradients from the ovary.';
        } else if (slide10P <= 1.0) {
            if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">3. Gamete Fusion & Fertilization:</span> Male germ-cells discharge into the ovule, fertilizing the egg to form the diploid zygote.';
        }

        if (slide10P < 1.0) {
            slide10Anim = requestAnimationFrame(animate);
        } else {
            slide10Active = false;
        }
    }
    animate();
}

function drawSlide10(ctx, w, h, p) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060d1b';
    ctx.fillRect(0, 0, w, h);

    const cX = w * 0.5;
    const topY = 60;
    const botY = h * 0.75;

    // Carpel outline
    ctx.fillStyle = '#14532d';
    // Style
    ctx.fillRect(cX - 10, topY + 15, 20, botY - topY - 15);

    // Stigma
    ctx.beginPath();
    ctx.ellipse(cX, topY + 15, 24, 10, 0, 0, Math.PI * 2);
    ctx.fill();

    // Ovary
    ctx.beginPath();
    ctx.ellipse(cX, botY, 45, 35, 0, 0, Math.PI * 2);
    ctx.fill();

    // Ovule inside
    ctx.fillStyle = '#854d0e';
    ctx.beginPath();
    ctx.ellipse(cX, botY, 20, 16, 0, 0, Math.PI * 2);
    ctx.fill();

    // Egg cell
    ctx.fillStyle = '#f43f5e';
    ctx.beginPath();
    ctx.arc(cX, botY + 4, 6, 0, Math.PI * 2);
    ctx.fill();

    // Pollen Grain on Stigma
    ctx.fillStyle = '#eab308';
    ctx.beginPath();
    ctx.arc(cX - 4, topY + 8, 7, 0, Math.PI * 2);
    ctx.fill();

    // Pollen Tube Growth
    if (p > 0) {
        const curY = topY + 15 + (botY - (topY + 15)) * Math.min(1, p);
        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(cX - 4, topY + 12);
        ctx.lineTo(cX, curY);
        ctx.stroke();

        // Male gamete moving down
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(cX, curY - 4, 3, 0, Math.PI * 2);
        ctx.fill();
    }

    ctx.fillStyle = '#fde047';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Pollen Grain', cX + 15, topY + 12);
    ctx.fillText('Pollen Tube', cX + 15, topY + 80);
    ctx.fillText('Egg Cell (Ovule)', cX + 30, botY + 5);
}

// ==========================================
// SIMULATOR 11: Seed Development Germination
// ==========================================
let slide11View = 'anatomy';

function initSlide11() {
    setSlide11View('anatomy');
}

function setSlide11View(view) {
    slide11View = view;
    const canvas = document.getElementById('slide11Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide11Status');

    drawSlide11(ctx, canvas.width, canvas.height, view);

    if (view === 'anatomy') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Internal Seed Anatomy:</span> Dicot seed opened up showing food-storing cotyledons, embryonic plumule (future shoot), and embryonic radicle (future root).';
    } else {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Active Germination:</span> In moisture and warmth, radicle elongates downward (+geotropism) into soil while plumule extends upward (-geotropism) with foliage.';
    }
}

function drawSlide11(ctx, w, h, view) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#09101d';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    if (view === 'anatomy') {
        // Dissected bean seed halves
        ctx.fillStyle = '#ca8a04';
        // Left cotyledon
        ctx.beginPath();
        ctx.ellipse(midX - 45, h * 0.5, 45, 65, 0.2, 0, Math.PI * 2);
        ctx.fill();
        // Right cotyledon
        ctx.beginPath();
        ctx.ellipse(midX + 45, h * 0.5, 45, 65, -0.2, 0, Math.PI * 2);
        ctx.fill();

        // Embryo axis in center
        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 6;
        ctx.beginPath();
        // Radicle down
        ctx.moveTo(midX, h * 0.5);
        ctx.quadraticCurveTo(midX + 15, h * 0.5 + 20, midX + 8, h * 0.5 + 45);
        // Plumule up
        ctx.moveTo(midX, h * 0.5);
        ctx.quadraticCurveTo(midX - 15, h * 0.5 - 20, midX - 8, h * 0.5 - 45);
        ctx.stroke();

        ctx.fillStyle = '#86efac';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Plumule (Future Shoot)', midX - 160, h * 0.5 - 45);
        ctx.fillText('Radicle (Future Root)', midX + 25, h * 0.5 + 50);
        ctx.fillStyle = '#fef08a';
        ctx.fillText('Cotyledons (Food Stores)', midX - 85, h * 0.5 + 95);

    } else {
        // Germinating seedling in soil
        const soilY = h * 0.55;
        ctx.fillStyle = '#3e2723';
        ctx.fillRect(40, soilY, w - 80, h - soilY - 20);

        // Seed in soil
        ctx.fillStyle = '#854d0e';
        ctx.beginPath();
        ctx.ellipse(midX, soilY + 25, 18, 12, 0, 0, Math.PI * 2);
        ctx.fill();

        // Radicle growing DOWN
        ctx.strokeStyle = '#fef08a';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(midX, soilY + 30);
        ctx.lineTo(midX, soilY + 70);
        ctx.stroke();

        // Plumule growing UP
        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(midX, soilY + 15);
        ctx.lineTo(midX, soilY - 55);
        ctx.stroke();

        // Leaves at top
        ctx.fillStyle = '#4ade80';
        ctx.beginPath();
        ctx.ellipse(midX - 12, soilY - 55, 12, 6, -0.4, 0, Math.PI * 2);
        ctx.ellipse(midX + 12, soilY - 55, 12, 6, 0.4, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#4ade80';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Plumule: Aerial Shoot & Leaves', midX + 20, soilY - 50);
        ctx.fillStyle = '#fef08a';
        ctx.fillText('Radicle: Subterranean Root System', midX + 20, soilY + 65);
    }
}

// ==========================================
// SIMULATOR 12: Human Puberty Changes
// ==========================================
let slide12Sex = 'male';

function initSlide12() {
    setSlide12Sex('male');
}

function setSlide12Sex(sex) {
    slide12Sex = sex;
    const canvas = document.getElementById('slide12Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide12Status');

    drawSlide12(ctx, canvas.width, canvas.height, sex);

    if (sex === 'male') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Male Pubertal Adaptations:</span> Driven by testicular testosterone: facial hair growth, deepening voice (larynx enlargement), broader shoulders, and spermatogenesis onset.';
    } else {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Female Pubertal Adaptations:</span> Driven by ovarian estrogen: breast enlargement, pelvic widening for childbearing, and commencement of monthly menstruation.';
    }
}

function drawSlide12(ctx, w, h, sex) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060d1b';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    // Pituitary master gland at top
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(midX, 45, 16, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#fde68a';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Pituitary Gland (LH & FSH Signals)', midX - 85, 20);

    // Endocrine signal line
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(midX, 61);
    ctx.lineTo(midX, 110);
    ctx.stroke();

    if (sex === 'male') {
        // Testes & Testosterone
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.roundRect(midX - 70, 110, 140, 45, 10);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Testes: TESTOSTERONE', midX - 60, 137);

        // Traits
        const traits = [
            '• Facial beard & mustache hair',
            '• Larynx enlargement & voice cracking',
            '• Increased skeletal muscle mass',
            '• Penis enlargement & sperm production'
        ];
        ctx.fillStyle = '#93c5fd';
        ctx.font = '11px sans-serif';
        traits.forEach((t, i) => {
            ctx.fillText(t, midX - 100, 185 + i * 24);
        });

    } else {
        // Ovaries & Estrogen
        ctx.fillStyle = '#db2777';
        ctx.beginPath();
        ctx.roundRect(midX - 70, 110, 140, 45, 10);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Ovaries: ESTROGEN', midX - 55, 137);

        // Traits
        const traits = [
            '• Breast enlargement & areola pigmentation',
            '• Widening of hips & pelvis for childbearing',
            '• Onset of monthly menstrual bleeding cycles',
            '• Maturation and cyclic release of mature ova'
        ];
        ctx.fillStyle = '#f472b6';
        ctx.font = '11px sans-serif';
        traits.forEach((t, i) => {
            ctx.fillText(t, midX - 120, 185 + i * 24);
        });
    }
}

// ==========================================
// SIMULATOR 13: Male Reproductive Anatomy
// ==========================================
let slide13View = 'tract';

function initSlide13() {
    setSlide13View('tract');
}

function setSlide13View(view) {
    slide13View = view;
    const canvas = document.getElementById('slide13Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide13Status');

    drawSlide13(ctx, canvas.width, canvas.height, view);

    if (view === 'tract') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Male Reproductive Duct System:</span> Testes inside cooler scrotum (2–2.5°C lower) -> Vas deferens -> Prostate & Seminal vesicles (nutrition/fluid) -> Urethra.';
    } else {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Sperm Cell Architecture:</span> Head containing condensed genetic DNA, middle piece packed with energy-providing mitochondria, and long flagellar tail for motility.';
    }
}

function drawSlide13(ctx, w, h, view) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060d1b';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    if (view === 'tract') {
        // Scrotum & Testes
        ctx.fillStyle = '#1e3a8a';
        ctx.beginPath();
        ctx.ellipse(140, h * 0.65, 28, 35, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Testis in Scrotum (34.5°C)', 80, h * 0.65 + 50);

        // Vas deferens ascending and looping
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(140, h * 0.65 - 35);
        ctx.quadraticCurveTo(150, 70, 260, 70);
        ctx.quadraticCurveTo(340, 70, 340, 140);
        ctx.stroke();

        ctx.fillStyle = '#fde68a';
        ctx.fillText('Vas Deferens (Sperm Duct)', 160, 60);

        // Prostate & Seminal vesicles
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.ellipse(340, 140, 18, 14, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('Prostate & Seminal Vesicles (Fluids)', 280, 175);

        // Urethra through penis
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.moveTo(340, 154);
        ctx.lineTo(w - 70, 154);
        ctx.stroke();

        ctx.fillStyle = '#38bdf8';
        ctx.fillText('Urethra (Common Passage)', w - 180, 140);

    } else {
        // Sperm Microscopic Structure
        const sX = 120;
        const sY = h * 0.5;

        // Head (Condensed DNA)
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.ellipse(sX, sY, 28, 18, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Acrosome cap
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(sX + 18, sY, 9, -Math.PI / 2, Math.PI / 2);
        ctx.fill();

        // Middle piece (Mitochondria)
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(sX - 45, sY - 8, 20, 16);

        // Flagellar Tail
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(sX - 45, sY);
        for (let dx = -45; dx >= -280; dx -= 15) {
            const dy = Math.sin(dx * 0.08) * 14;
            ctx.lineTo(sX + dx, sY + dy);
        }
        ctx.stroke();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Head: Genetic Material (DNA)', sX - 20, sY - 30);
        ctx.fillStyle = '#fde68a';
        ctx.fillText('Middle Piece (Mitochondria Energy)', sX - 90, sY + 35);
        ctx.fillStyle = '#cbd5e1';
        ctx.fillText('Tail: Motility (Whiplash Swimming)', 180, sY + 65);
    }
}

// ==========================================
// SIMULATOR 14: Female Reproductive Anatomy
// ==========================================
let slide14Ovulated = false;

function initSlide14() {
    resetSlide14();
}

function resetSlide14() {
    slide14Ovulated = false;
    const canvas = document.getElementById('slide14Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide14(ctx, canvas.width, canvas.height, false);
    const status = document.getElementById('slide14Status');
    if (status) status.innerHTML = 'Resting female reproductive tract. Click <b>"Trigger Ovulation"</b> to release an ovum into the fallopian tube.';
}

function triggerSlide14Ovulation() {
    slide14Ovulated = true;
    const canvas = document.getElementById('slide14Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide14(ctx, canvas.width, canvas.height, true);
    const status = document.getElementById('slide14Status');
    if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Ovulation Occurred:</span> Ovary discharges a mature egg, swept by fallopian tube fimbriae into the ampulla (the site of fertilization).';
}

function drawSlide14(ctx, w, h, ovulated) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#080d1b';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    // Muscular Uterus (inverted pear shape)
    ctx.fillStyle = '#9d174d';
    ctx.beginPath();
    ctx.moveTo(midX - 50, 110);
    ctx.lineTo(midX + 50, 110);
    ctx.lineTo(midX + 18, 210);
    ctx.lineTo(midX - 18, 210);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = '#f472b6';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Uterus', midX - 18, 160);

    // Cervix & Vagina below
    ctx.fillStyle = '#831843';
    ctx.fillRect(midX - 14, 210, 28, 45);

    // Fallopian Tubes extending laterally
    ctx.strokeStyle = '#db2777';
    ctx.lineWidth = 6;
    ctx.beginPath();
    // Left tube
    ctx.moveTo(midX - 45, 115);
    ctx.quadraticCurveTo(midX - 140, 80, midX - 160, 130);
    // Right tube
    ctx.moveTo(midX + 45, 115);
    ctx.quadraticCurveTo(midX + 140, 80, midX + 160, 130);
    ctx.stroke();

    // Ovaries
    ctx.fillStyle = '#be185d';
    ctx.beginPath();
    ctx.ellipse(midX - 170, 150, 20, 14, 0, 0, Math.PI * 2);
    ctx.ellipse(midX + 170, 150, 20, 14, 0, 0, Math.PI * 2);
    ctx.fill();

    // Released Egg
    if (ovulated) {
        ctx.fillStyle = '#fef08a';
        ctx.beginPath();
        ctx.arc(midX - 110, 95, 7, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fde047';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Ovum in Fallopian Tube (Site of Fertilization)', 80, 65);
    }

    ctx.fillStyle = '#f472b6';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Ovary', midX - 215, 155);
    ctx.fillText('Ovary', midX + 180, 155);
    ctx.fillText('Fallopian Tube', midX + 110, 70);
    ctx.fillText('Vaginal Canal', midX - 35, 275);
}

// ==========================================
// SIMULATOR 15: Implantation Placenta Gestation
// ==========================================
let slide15View = 'implant';

function initSlide15() {
    setSlide15View('implant');
}

function setSlide15View(view) {
    slide15View = view;
    const canvas = document.getElementById('slide15Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide15Status');

    drawSlide15(ctx, canvas.width, canvas.height, view);

    if (view === 'implant') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Uterine Implantation:</span> The cleaving blastocyst embeds deeply into the spongy, blood-rich uterine endometrium.';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Placental Villi Exchange:</span> Finger-like embryonic villi bathe in maternal blood spaces, diffusing glucose and O₂ to the fetus while removing urea and CO₂.';
    }
}

function drawSlide15(ctx, w, h, view) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#070d1a';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    if (view === 'implant') {
        // Uterine wall lining
        ctx.fillStyle = '#831843';
        ctx.fillRect(60, 60, w - 120, 80);

        // Blood vessels in uterine wall
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 3;
        for (let x = 80; x < w - 80; x += 30) {
            ctx.beginPath();
            ctx.moveTo(x, 60);
            ctx.lineTo(x + 10, 130);
            ctx.stroke();
        }

        // Blastocyst embedding
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(midX, 135, 25, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Thickened Vascular Endometrium', 80, 85);
        ctx.fillText('Implanted Blastocyst (Embryo)', midX - 75, 185);

    } else {
        // Placenta Villi structure
        // Maternal Blood Pool
        ctx.fillStyle = 'rgba(239, 68, 68, 0.25)';
        ctx.fillRect(60, 60, w - 120, 90);

        ctx.fillStyle = '#f87171';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Maternal Blood Pool (Oxygen & Glucose Rich)', 80, 80);

        // Embryonic Villi projecting downwards into pool
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 6;
        for (let x = 120; x < w - 100; x += 60) {
            ctx.beginPath();
            ctx.moveTo(x, 150);
            ctx.lineTo(x, 95);
            ctx.stroke();

            // Villi branch
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(x, 120);
            ctx.lineTo(x - 14, 105);
            ctx.moveTo(x, 120);
            ctx.lineTo(x + 14, 105);
            ctx.stroke();
            ctx.lineWidth = 6;
        }

        ctx.fillStyle = '#38bdf8';
        ctx.fillText('Embryonic Villi (Enormous Exchange Surface)', 120, 185);

        // Gas & Waste exchange arrows
        ctx.fillStyle = '#4ade80';
        ctx.font = '10px sans-serif';
        ctx.fillText('O₂ & Nutrients → Fetus', 140, 220);
        ctx.fillStyle = '#fb923c';
        ctx.fillText('CO₂ & Urea → Mother', 320, 220);
    }
}

// ==========================================
// SIMULATOR 16: Menstruation Contraceptive Methods
// ==========================================
let slide16Mode = 'menstrual';

function initSlide16() {
    setSlide16Mode('menstrual');
}

function setSlide16Mode(mode) {
    slide16Mode = mode;
    const canvas = document.getElementById('slide16Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide16Status');

    drawSlide16(ctx, canvas.width, canvas.height, mode);

    if (mode === 'menstrual') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">28-Day Menstrual Cycle:</span> Days 1–5: Menstrual discharge; Days 6–13: Follicular wall thickening; Day 14: Ovulation; Days 15–28: Secretory phase awaiting fertilization.';
    } else {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Contraceptive Methods:</span> Barrier (condoms, STD protection), Hormonal (pills suppress ovulation), IUD (Copper-T blocks implantation), Surgical (vasectomy/tubectomy permanent sterilization).';
    }
}

function drawSlide16(ctx, w, h, mode) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#070d1a';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    if (mode === 'menstrual') {
        // 28-day Circular Cycle Wheel
        const cY = h * 0.5;
        const rad = 80;

        // Days 1-5 (Menstruation - Red)
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 14;
        ctx.beginPath();
        ctx.arc(midX, cY, rad, -Math.PI / 2, -Math.PI / 2 + (5 / 28) * Math.PI * 2);
        ctx.stroke();

        // Days 6-13 (Proliferation - Green)
        ctx.strokeStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(midX, cY, rad, -Math.PI / 2 + (5 / 28) * Math.PI * 2, -Math.PI / 2 + (13 / 28) * Math.PI * 2);
        ctx.stroke();

        // Day 14 (Ovulation - Amber)
        ctx.strokeStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(midX, cY, rad, -Math.PI / 2 + (13 / 28) * Math.PI * 2, -Math.PI / 2 + (15 / 28) * Math.PI * 2);
        ctx.stroke();

        // Days 15-28 (Secretory - Blue)
        ctx.strokeStyle = '#0284c7';
        ctx.beginPath();
        ctx.arc(midX, cY, rad, -Math.PI / 2 + (15 / 28) * Math.PI * 2, Math.PI * 1.5);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('28 Days Cycle', midX - 35, cY + 4);

        ctx.fillStyle = '#ef4444';
        ctx.fillText('Days 1–5: Menstruation', 45, 60);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText('Day 14: Ovulation', w - 160, 60);
        ctx.fillStyle = '#10b981';
        ctx.fillText('Days 6–13: Follicular', 45, h - 35);
        ctx.fillStyle = '#38bdf8';
        ctx.fillText('Days 15–28: Secretory', w - 160, h - 35);

    } else {
        // Contraceptive 4 Quadrants
        const quads = [
            { title: '1. Mechanical Barriers', desc: 'Condoms / Diaphragms: Block sperm entry & protect against STDs (HIV)', col: '#10b981', x: 50, y: 50 },
            { title: '2. Chemical / Hormonal', desc: 'Oral contraceptive pills: Alter hormonal balance to inhibit ovulation', col: '#0284c7', x: midX + 20, y: 50 },
            { title: '3. Intrauterine Devices', desc: 'Loop / Copper-T: Placed in uterus to prevent blastocyst implantation', col: '#f59e0b', x: 50, y: 145 },
            { title: '4. Surgical Sterilization', desc: 'Vasectomy (male vas deferens) / Tubectomy (female fallopian tubes)', col: '#ec4899', x: midX + 20, y: 145 }
        ];

        quads.forEach(q => {
            ctx.fillStyle = '#1e293b';
            ctx.beginPath();
            ctx.roundRect(q.x, q.y, midX - 60, 75, 8);
            ctx.fill();

            ctx.fillStyle = q.col;
            ctx.font = 'bold 11px sans-serif';
            ctx.fillText(q.title, q.x + 12, q.y + 24);

            ctx.fillStyle = '#cbd5e1';
            ctx.font = '10px sans-serif';
            ctx.fillText(q.desc.slice(0, 40), q.x + 12, q.y + 44);
            ctx.fillText(q.desc.slice(40), q.x + 12, q.y + 58);
        });
    }
}
'''

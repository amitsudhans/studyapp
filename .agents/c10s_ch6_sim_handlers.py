# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 6: Control and Coordination
Interactive Canvas & Simulator JavaScript Handlers
"""

SIMULATOR_JS = '''
// ==========================================
// SIMULATOR 1: Movement Environmental Response
// ==========================================
let slide1State = { mode: 'seed', animFrame: null, progress: 0 };

function initSlide1() {
    setSlide1Movement('seed');
}

function setSlide1Movement(mode) {
    slide1State.mode = mode;
    slide1State.progress = 0;
    const canvas = document.getElementById('slide1Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide1Status');

    if (slide1State.animFrame) cancelAnimationFrame(slide1State.animFrame);

    if (mode === 'seed') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Growth-Dependent Movement:</span> Germinating seed radicle moves downward into soil while plumule shoots upward, breaking through soil particles toward light.';
    } else if (mode === 'cat') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Non-Growth Locomotor Movement:</span> Cat sprinting rapidly toward prey or fleeing danger — fast, voluntary, and does not alter permanent body dimensions.';
    } else if (mode === 'whisper') {
        if (status) status.innerHTML = '<span class="text-purple-400 font-bold">Precision Coordination:</span> Whispering quietly in a classroom — fine motor control balancing auditory communication with environmental restraint.';
    }

    function animate() {
        slide1State.progress = Math.min(1, slide1State.progress + 0.02);
        drawSlide1(ctx, canvas.width, canvas.height, slide1State.mode, slide1State.progress);
        if (slide1State.progress < 1) {
            slide1State.animFrame = requestAnimationFrame(animate);
        }
    }
    animate();
}

function drawSlide1(ctx, w, h, mode, p) {
    ctx.clearRect(0, 0, w, h);

    // Background gradient
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, '#0f172a');
    grad.addColorStop(1, '#020617');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    if (mode === 'seed') {
        // Soil line
        const soilY = h * 0.55;
        ctx.fillStyle = '#3f2e18';
        ctx.fillRect(0, soilY, w, h - soilY);

        ctx.strokeStyle = '#604323';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(0, soilY);
        ctx.lineTo(w, soilY);
        ctx.stroke();

        ctx.fillStyle = '#a17238';
        ctx.font = '11px sans-serif';
        ctx.fillText('SOIL HORIZON', 15, soilY + 20);

        // Seed Body
        const seedX = w * 0.5;
        const seedY = soilY + 40;
        ctx.fillStyle = '#854d0e';
        ctx.beginPath();
        ctx.ellipse(seedX, seedY, 16, 12, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ca8a04';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Radicle (Root growing down)
        ctx.strokeStyle = '#fef08a';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(seedX, seedY + 10);
        ctx.quadraticCurveTo(seedX - 10, seedY + 30 * p, seedX, seedY + 60 * p);
        ctx.stroke();

        // Secondary roots
        if (p > 0.5) {
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(seedX - 5, seedY + 35);
            ctx.lineTo(seedX - 25 * p, seedY + 45 * p);
            ctx.moveTo(seedX + 5, seedY + 45);
            ctx.lineTo(seedX + 25 * p, seedY + 55 * p);
            ctx.stroke();
        }

        // Plumule (Shoot pushing up)
        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(seedX, seedY - 10);
        const shootTipY = seedY - (70 * p);
        ctx.quadraticCurveTo(seedX + 15, (seedY + shootTipY) / 2, seedX, shootTipY);
        ctx.stroke();

        // Leaves at plumule tip
        if (shootTipY < soilY) {
            ctx.fillStyle = '#4ade80';
            ctx.beginPath();
            ctx.ellipse(seedX - 12, shootTipY - 5, 10, 5, -0.4, 0, Math.PI * 2);
            ctx.ellipse(seedX + 12, shootTipY - 5, 10, 5, 0.4, 0, Math.PI * 2);
            ctx.fill();
        }

        // Sun
        ctx.fillStyle = '#facc15';
        ctx.beginPath();
        ctx.arc(w - 50, 45, 22, 0, Math.PI * 2);
        ctx.fill();

        // Labels
        ctx.fillStyle = '#86efac';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Plumule (Shoot: +Phototropism)', seedX + 20, shootTipY + 15);
        ctx.fillStyle = '#fef08a';
        ctx.fillText('Radicle (Root: +Geotropism)', seedX + 20, seedY + 50);

    } else if (mode === 'cat') {
        // Ground line
        const groundY = h * 0.75;
        ctx.strokeStyle = '#334155';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, groundY);
        ctx.lineTo(w, groundY);
        ctx.stroke();

        // Cat running across
        const catX = 60 + (w - 180) * p;
        const catY = groundY - 30;

        // Mouse target
        ctx.fillStyle = '#94a3b8';
        ctx.beginPath();
        ctx.ellipse(w - 50, groundY - 10, 14, 8, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px sans-serif';
        ctx.fillText('Target (Prey)', w - 85, groundY - 25);

        // Cat Body
        ctx.fillStyle = '#f97316';
        ctx.beginPath();
        ctx.ellipse(catX, catY, 32, 16, 0, 0, Math.PI * 2);
        ctx.fill();

        // Cat Head
        ctx.beginPath();
        ctx.arc(catX + 32, catY - 10, 14, 0, Math.PI * 2);
        ctx.fill();

        // Ears
        ctx.beginPath();
        ctx.moveTo(catX + 28, catY - 22);
        ctx.lineTo(catX + 34, catY - 32);
        ctx.lineTo(catX + 40, catY - 22);
        ctx.fill();

        // Legs (animated stride)
        ctx.strokeStyle = '#ea580c';
        ctx.lineWidth = 4;
        const legPhase = Math.sin(p * 20);
        ctx.beginPath();
        ctx.moveTo(catX - 18, catY + 10);
        ctx.lineTo(catX - 25 + legPhase * 15, groundY);
        ctx.moveTo(catX - 10, catY + 10);
        ctx.lineTo(catX - 5 - legPhase * 15, groundY);
        ctx.moveTo(catX + 15, catY + 10);
        ctx.lineTo(catX + 10 + legPhase * 15, groundY);
        ctx.moveTo(catX + 25, catY + 10);
        ctx.lineTo(catX + 32 - legPhase * 15, groundY);
        ctx.stroke();

        // Speed motion streaks
        ctx.strokeStyle = 'rgba(249, 115, 22, 0.4)';
        ctx.lineWidth = 2;
        for (let i = 0; i < 3; i++) {
            ctx.beginPath();
            ctx.moveTo(catX - 60 - i * 15, catY - 10 + i * 12);
            ctx.lineTo(catX - 20, catY - 10 + i * 12);
            ctx.stroke();
        }

        ctx.fillStyle = '#fdba74';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('High-Speed Locomotion (Non-Growth Response)', catX - 60, catY - 50);

    } else if (mode === 'whisper') {
        // Classroom scene
        const deskY = h * 0.7;
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(80, deskY, 340, 20);

        // Student 1 (whispering)
        const s1X = 140;
        const s1Y = deskY - 50;
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(s1X, s1Y, 20, 0, Math.PI * 2);
        ctx.fill();

        // Student 2 (listening)
        const s2X = 360;
        const s2Y = deskY - 50;
        ctx.fillStyle = '#a855f7';
        ctx.beginPath();
        ctx.arc(s2X, s2Y, 20, 0, Math.PI * 2);
        ctx.fill();

        // Sound waves traveling quietly
        ctx.strokeStyle = `rgba(56, 189, 248, ${1 - p * 0.5})`;
        ctx.lineWidth = 2;
        for (let i = 1; i <= 3; i++) {
            const waveX = s1X + 30 + (s2X - s1X - 60) * p * (i / 3);
            ctx.beginPath();
            ctx.arc(waveX, s1Y, 15 * i * 0.4, -Math.PI / 3, Math.PI / 3);
            ctx.stroke();
        }

        // Whispering text cloud
        ctx.fillStyle = '#93c5fd';
        ctx.font = '11px monospace';
        ctx.fillText('"psst... check question 4"', s1X + 40, s1Y - 20);

        ctx.fillStyle = '#f1f5f9';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Speaker (Fine Motor Vocal Cord Control)', s1X - 50, deskY + 45);
        ctx.fillText('Listener (Auditory Receptors)', s2X - 50, deskY + 45);
    }
}

// ==========================================
// SIMULATOR 2: Neuron Synaptic Transmission
// ==========================================
let slide2Anim = null;
let slide2Progress = 0;
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
    if (status) status.innerHTML = 'Neuron at resting potential (-70mV). Click <b>"Fire Action Potential"</b> to trigger wave.';
}

function triggerSlide2Impulse() {
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
            if (status) status.innerHTML = '<span class="text-amber-400 font-bold">1. Dendritic Tip Detection:</span> Receptor acquires stimulus, triggering initial electrical impulse at cyton.';
        } else if (slide2Progress < 0.7) {
            if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">2. Axonal Conduction:</span> Voltage-gated Na⁺/K⁺ depolarization wave surges rapidly along axon fiber.';
        } else if (slide2Progress <= 1.0) {
            if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">3. Synaptic Cleft Neurotransmission:</span> Axon terminal releases neurotransmitters across microscopic 20nm gap to activate next dendrite.';
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

    // Dark backdrop
    ctx.fillStyle = '#090d16';
    ctx.fillRect(0, 0, w, h);

    const cytonX = 90;
    const cytonY = h * 0.5;
    const axonStartX = 120;
    const axonEndX = 330;
    const synX = 380;

    // --- 1. PRE-SYNAPTIC NEURON ---
    // Cyton (Soma)
    ctx.fillStyle = '#1e3a8a';
    ctx.beginPath();
    ctx.arc(cytonX, cytonY, 28, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Nucleus
    ctx.fillStyle = '#60a5fa';
    ctx.beginPath();
    ctx.arc(cytonX, cytonY, 10, 0, Math.PI * 2);
    ctx.fill();

    // Dendrites branching from cyton
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    const dendrites = [
        { x: cytonX - 50, y: cytonY - 35 },
        { x: cytonX - 60, y: cytonY },
        { x: cytonX - 50, y: cytonY + 35 },
        { x: cytonX - 25, y: cytonY - 45 },
        { x: cytonX - 25, y: cytonY + 45 }
    ];
    dendrites.forEach(d => {
        ctx.beginPath();
        ctx.moveTo(cytonX, cytonY);
        ctx.lineTo(d.x, d.y);
        ctx.stroke();
    });

    // Axon Cylinder
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.moveTo(axonStartX, cytonY);
    ctx.lineTo(axonEndX, cytonY);
    ctx.stroke();

    // Myelin Sheath segments
    ctx.fillStyle = '#0284c7';
    for (let x = axonStartX + 10; x < axonEndX - 20; x += 38) {
        ctx.beginPath();
        ctx.roundRect(x, cytonY - 10, 26, 20, 6);
        ctx.fill();
    }

    // Axon Terminals & Boutons
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(axonEndX, cytonY);
    ctx.lineTo(axonEndX + 30, cytonY - 20);
    ctx.moveTo(axonEndX, cytonY);
    ctx.lineTo(axonEndX + 30, cytonY + 20);
    ctx.stroke();

    // Bouton knobs
    ctx.fillStyle = '#2563eb';
    ctx.beginPath();
    ctx.arc(axonEndX + 34, cytonY - 20, 9, 0, Math.PI * 2);
    ctx.arc(axonEndX + 34, cytonY + 20, 9, 0, Math.PI * 2);
    ctx.fill();

    // --- 2. POST-SYNAPTIC DENDRITE ---
    ctx.fillStyle = '#14532d';
    ctx.beginPath();
    ctx.arc(synX + 50, cytonY, 35, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.strokeStyle = '#4ade80';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(synX + 15, cytonY - 20);
    ctx.lineTo(synX + 40, cytonY - 10);
    ctx.moveTo(synX + 15, cytonY + 20);
    ctx.lineTo(synX + 40, cytonY + 10);
    ctx.stroke();

    // --- 3. ELECTRICAL IMPULSE WAVE ---
    if (p > 0 && p <= 0.7) {
        const impX = 40 + (axonEndX + 30 - 40) * (p / 0.7);
        const glow = ctx.createRadialGradient(impX, cytonY, 0, impX, cytonY, 20);
        glow.addColorStop(0, '#fef08a');
        glow.addColorStop(0.5, '#eab308');
        glow.addColorStop(1, 'transparent');
        ctx.fillStyle = glow;
        ctx.beginPath();
        ctx.arc(impX, cytonY, 20, 0, Math.PI * 2);
        ctx.fill();

        // Sparkle sparks
        ctx.fillStyle = '#ffffff';
        for (let i = 0; i < 4; i++) {
            const sx = impX + (Math.random() - 0.5) * 20;
            const sy = cytonY + (Math.random() - 0.5) * 20;
            ctx.fillRect(sx, sy, 3, 3);
        }
    }

    // --- 4. SYNAPTIC NEUROTRANSMITTER VESICLES ---
    if (p > 0.7) {
        const transP = (p - 0.7) / 0.3;
        ctx.fillStyle = '#f43f5e';
        for (let i = 0; i < 14; i++) {
            const startX = axonEndX + 34;
            const startY = cytonY - 20 + (i % 2 === 0 ? 0 : 40);
            const targetX = synX + 15;
            const currentX = startX + (targetX - startX) * Math.min(1, transP * (1 + (i % 5) * 0.15));
            const currentY = startY + (Math.sin(i * 1.5) * 12);
            ctx.beginPath();
            ctx.arc(currentX, currentY, 3, 0, Math.PI * 2);
            ctx.fill();
        }

        // Postsynaptic activation glow
        if (transP > 0.6) {
            ctx.fillStyle = 'rgba(74, 222, 128, 0.4)';
            ctx.beginPath();
            ctx.arc(synX + 50, cytonY, 40, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // LABELS
    ctx.fillStyle = '#93c5fd';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Dendrite Tip', 25, cytonY - 45);
    ctx.fillText('Cell Body (Cyton)', cytonX - 40, cytonY + 45);
    ctx.fillText('Axon Fiber', axonStartX + 50, cytonY - 18);
    ctx.fillText('Axon Terminal', axonEndX - 10, cytonY + 42);

    ctx.fillStyle = '#f43f5e';
    ctx.fillText('Synapse (20nm gap)', synX - 25, cytonY - 35);
    ctx.fillStyle = '#86efac';
    ctx.fillText('Next Dendrite', synX + 25, cytonY + 45);
}

// ==========================================
// SIMULATOR 3: Spinal Reflex Arc
// ==========================================
let slide3Anim = null;
let slide3Progress = 0;
let slide3Active = false;

function initSlide3() {
    resetSlide3();
}

function resetSlide3() {
    slide3Active = false;
    slide3Progress = 0;
    if (slide3Anim) cancelAnimationFrame(slide3Anim);
    const canvas = document.getElementById('slide3Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide3(ctx, canvas.width, canvas.height, 0);
    const status = document.getElementById('slide3Status');
    if (status) status.innerHTML = 'Resting reflex loop. Click <b>"Touch Hot Pan"</b> to observe the spinal reflex arc bypass slow brain processing.';
}

function triggerSlide3Reflex() {
    if (slide3Active) return;
    slide3Active = true;
    slide3Progress = 0;
    const canvas = document.getElementById('slide3Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide3Status');

    function animate() {
        slide3Progress += 0.012;
        drawSlide3(ctx, canvas.width, canvas.height, slide3Progress);

        if (slide3Progress < 0.25) {
            if (status) status.innerHTML = '<span class="text-rose-400 font-bold">1. Stimulus & Receptors:</span> Heat from pan stimulates thermo-receptors and pain receptors in fingertips.';
        } else if (slide3Progress < 0.5) {
            if (status) status.innerHTML = '<span class="text-amber-400 font-bold">2. Sensory Afferent Pathway:</span> Impulse races through sensory neuron entering spinal cord dorsal root.';
        } else if (slide3Progress < 0.75) {
            if (status) status.innerHTML = '<span class="text-purple-400 font-bold">3. Relay Neuron in Spinal Cord:</span> Direct connection triggers motor neuron while sending delayed branch copy to brain.';
        } else if (slide3Progress <= 1.0) {
            if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">4. Motor Efferent & Effector:</span> Motor neuron fires; arm biceps contract instantly pulling hand safely away from heat.';
        }

        if (slide3Progress < 1.0) {
            slide3Anim = requestAnimationFrame(animate);
        } else {
            slide3Active = false;
        }
    }
    animate();
}

function drawSlide3(ctx, w, h, p) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0b1120';
    ctx.fillRect(0, 0, w, h);

    // Positions
    const panX = 60, panY = h * 0.75;
    const handX = 75, handY = (p > 0.8) ? panY - 50 : panY - 15;
    const spinalX = 380, spinalY = h * 0.45;
    const brainX = 380, brainY = 50;

    // --- HOT PAN ---
    ctx.fillStyle = '#475569';
    ctx.fillRect(panX - 40, panY, 80, 16);
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.ellipse(panX, panY, 35, 10, 0, 0, Math.PI * 2);
    ctx.fill();

    // Heat flames
    ctx.fillStyle = 'rgba(239, 68, 68, 0.7)';
    for (let i = -2; i <= 2; i++) {
        ctx.beginPath();
        ctx.moveTo(panX + i * 12, panY - 2);
        ctx.lineTo(panX + i * 12 + 4, panY - 18 - Math.abs(i) * 3);
        ctx.lineTo(panX + i * 12 + 8, panY - 2);
        ctx.fill();
    }

    // --- HAND & ARM ---
    ctx.fillStyle = '#fbcfe8';
    ctx.beginPath();
    ctx.ellipse(handX, handY, 18, 12, 0.3, 0, Math.PI * 2);
    ctx.fill();

    // Arm muscle (Biceps effector)
    const armX = 150, armY = handY - 40;
    ctx.fillStyle = (p > 0.8) ? '#dc2626' : '#7f1d1d';
    ctx.beginPath();
    ctx.ellipse(armX, armY, (p > 0.8) ? 30 : 25, (p > 0.8) ? 18 : 12, -0.4, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#f87171';
    ctx.lineWidth = 2;
    ctx.stroke();

    // --- SPINAL CORD CROSS SECTION ---
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.ellipse(spinalX, spinalY, 55, 65, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Butterfly Gray Matter
    ctx.fillStyle = '#475569';
    ctx.beginPath();
    ctx.moveTo(spinalX - 25, spinalY - 25);
    ctx.quadraticCurveTo(spinalX, spinalY, spinalX - 25, spinalY + 25);
    ctx.quadraticCurveTo(spinalX + 15, spinalY, spinalX + 25, spinalY + 25);
    ctx.quadraticCurveTo(spinalX, spinalY, spinalX + 25, spinalY - 25);
    ctx.closePath();
    ctx.fill();

    // --- BRAIN BOX (Higher Center) ---
    ctx.fillStyle = '#312e81';
    ctx.beginPath();
    ctx.roundRect(brainX - 45, brainY - 20, 90, 40, 10);
    ctx.fill();
    ctx.strokeStyle = '#6366f1';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.fillStyle = '#c7d2fe';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Brain (Slow)', brainX - 32, brainY + 4);

    // --- PATHWAYS ---
    // 1. Sensory Pathway (Red/Amber)
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(handX, handY);
    ctx.quadraticCurveTo(240, handY - 60, spinalX - 20, spinalY - 15);
    ctx.stroke();

    // 2. Relay Neuron in Spinal Cord
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(spinalX - 20, spinalY - 15);
    ctx.lineTo(spinalX + 5, spinalY);
    ctx.lineTo(spinalX - 20, spinalY + 15);
    ctx.stroke();

    // 3. Motor Pathway (Green)
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(spinalX - 20, spinalY + 15);
    ctx.quadraticCurveTo(240, handY + 20, armX + 10, armY + 10);
    ctx.stroke();

    // 4. Delay Path to Brain (Dashed)
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(spinalX, spinalY - 25);
    ctx.lineTo(brainX, brainY + 20);
    ctx.stroke();
    ctx.setLineDash([]);

    // --- PULSING SIGNALS ---
    if (p > 0 && p < 0.45) {
        // Sensory impulse moving toward spinal cord
        const t = p / 0.45;
        const curX = handX + (spinalX - 20 - handX) * t;
        const curY = handY + (spinalY - 15 - handY) * t - Math.sin(t * Math.PI) * 40;
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(curX, curY, 6, 0, Math.PI * 2);
        ctx.fill();
    } else if (p >= 0.45 && p < 0.65) {
        // Relay neuron activation
        ctx.fillStyle = '#c084fc';
        ctx.beginPath();
        ctx.arc(spinalX + 5, spinalY, 8, 0, Math.PI * 2);
        ctx.fill();
    } else if (p >= 0.65 && p <= 1.0) {
        // Motor impulse traveling to muscle
        const t = (p - 0.65) / 0.35;
        const curX = (spinalX - 20) + (armX + 10 - (spinalX - 20)) * t;
        const curY = (spinalY + 15) + (armY + 10 - (spinalY + 15)) * t + Math.sin(t * Math.PI) * 20;
        ctx.fillStyle = '#34d399';
        ctx.beginPath();
        ctx.arc(curX, curY, 6, 0, Math.PI * 2);
        ctx.fill();
    }

    // Delayed signal to brain
    if (p > 0.5) {
        const bp = (p - 0.5) / 0.5;
        const curY = (spinalY - 25) + (brainY + 20 - (spinalY - 25)) * bp;
        ctx.fillStyle = '#818cf8';
        ctx.beginPath();
        ctx.arc(brainX, curY, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    // LABELS
    ctx.fillStyle = '#fbbf24';
    ctx.font = '11px sans-serif';
    ctx.fillText('Sensory Neuron (Afferent)', 160, handY - 60);

    ctx.fillStyle = '#34d399';
    ctx.fillText('Motor Neuron (Efferent)', 165, handY + 30);

    ctx.fillStyle = '#f87171';
    ctx.fillText('Effector: Biceps Muscle', armX - 40, armY - 25);

    ctx.fillStyle = '#cbd5e1';
    ctx.fillText('Spinal Cord (Reflex Center)', spinalX - 60, spinalY + 80);
}

// ==========================================
// SIMULATOR 4: Human Brain Anatomy
// ==========================================
let slide4Region = 'all';

function initSlide4() {
    setSlide4BrainRegion('all');
}

function setSlide4BrainRegion(region) {
    slide4Region = region;
    const canvas = document.getElementById('slide4Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide4Status');

    drawSlide4(ctx, canvas.width, canvas.height, region);

    if (region === 'forebrain') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Fore-Brain (Cerebrum):</span> Largest thinking center. Contains sensory receiving areas, association areas (memory/reasoning), motor control centers, and hunger satiety center.';
    } else if (region === 'midbrain') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Mid-Brain:</span> Connects fore-brain to hind-brain. Governs involuntary reflex movements of eyes, pupil size, head, and auditory orientation.';
    } else if (region === 'hindbrain') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Hind-Brain (Pons, Medulla, Cerebellum):</span> Cerebellum coordinates posture and balance; Medulla controls vital involuntary functions (blood pressure, salivation, vomiting).';
    } else {
        if (status) status.innerHTML = '<span class="text-indigo-400 font-bold">Complete Brain Architecture:</span> Protected inside the bony cranium and bathed in cerebrospinal fluid (CSF).';
    }
}

function drawSlide4(ctx, w, h, region) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#030712';
    ctx.fillRect(0, 0, w, h);

    const cx = w * 0.45;
    const cy = h * 0.48;

    // --- CRANIUM (Bony Skull Box) ---
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 10;
    ctx.beginPath();
    ctx.arc(cx, cy - 20, 115, Math.PI * 0.75, Math.PI * 2.25);
    ctx.stroke();

    // Cranium Label
    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Cranium (Skull Box)', cx - 55, cy - 145);

    // --- FORE-BRAIN (CEREBRUM) ---
    const isFore = (region === 'all' || region === 'forebrain');
    ctx.fillStyle = isFore ? '#ca8a04' : '#451a03';
    ctx.beginPath();
    ctx.moveTo(cx - 85, cy);
    ctx.bezierCurveTo(cx - 90, cy - 110, cx + 70, cy - 120, cx + 80, cy - 20);
    ctx.bezierCurveTo(cx + 85, cy + 20, cx + 20, cy + 30, cx - 10, cy + 10);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = isFore ? '#fef08a' : '#78350f';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Cerebrum Sulci & Gyri (folds)
    ctx.strokeStyle = isFore ? '#fef9c3' : '#92400e';
    ctx.lineWidth = 1.5;
    for (let i = 0; i < 5; i++) {
        ctx.beginPath();
        ctx.arc(cx - 40 + i * 25, cy - 50 + (i % 2) * 15, 20, 0.2, Math.PI * 0.9);
        ctx.stroke();
    }

    // --- MID-BRAIN ---
    const isMid = (region === 'all' || region === 'midbrain');
    ctx.fillStyle = isMid ? '#0284c7' : '#082f49';
    ctx.beginPath();
    ctx.arc(cx - 5, cy + 20, 18, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = isMid ? '#38bdf8' : '#0369a1';
    ctx.lineWidth = 2;
    ctx.stroke();

    // --- HIND-BRAIN ---
    const isHind = (region === 'all' || region === 'hindbrain');

    // Cerebellum (tree-like folia structure at posterior base)
    ctx.fillStyle = isHind ? '#15803d' : '#052e16';
    ctx.beginPath();
    ctx.ellipse(cx + 60, cy + 45, 30, 22, -0.3, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = isHind ? '#4ade80' : '#166534';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Pons (bulge below midbrain)
    ctx.fillStyle = isHind ? '#16a34a' : '#052e16';
    ctx.beginPath();
    ctx.arc(cx - 15, cy + 45, 14, 0, Math.PI * 2);
    ctx.fill();

    // Medulla Oblongata (tapering downwards)
    ctx.fillStyle = isHind ? '#22c55e' : '#14532d';
    ctx.beginPath();
    ctx.moveTo(cx - 25, cy + 55);
    ctx.lineTo(cx - 5, cy + 55);
    ctx.lineTo(cx - 10, cy + 95);
    ctx.lineTo(cx - 20, cy + 95);
    ctx.closePath();
    ctx.fill();

    // Spinal Cord Continuation
    ctx.fillStyle = '#64748b';
    ctx.fillRect(cx - 20, cy + 95, 10, 45);

    // --- LABELS & HIGHLIGHT CALLOUTS ---
    ctx.font = 'bold 12px sans-serif';

    if (isFore) {
        ctx.fillStyle = '#fef08a';
        ctx.fillText('FORE-BRAIN (Cerebrum)', cx - 75, cy - 65);
        ctx.font = '10px sans-serif';
        ctx.fillText('• Sensory & Motor Areas', cx - 75, cy - 48);
        ctx.fillText('• Hunger Satiety Center', cx - 75, cy - 35);
    }

    if (isMid) {
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('MID-BRAIN', cx - 80, cy + 22);
    }

    if (isHind) {
        ctx.fillStyle = '#4ade80';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Cerebellum (Balance)', cx + 70, cy + 80);
        ctx.fillText('Pons', cx - 60, cy + 50);
        ctx.fillText('Medulla (Vitals)', cx - 95, cy + 75);
    }

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Spinal Cord', cx - 80, cy + 120);
}

// ==========================================
// SIMULATOR 5: Voluntary Involuntary Coordination
// ==========================================
let slide5Mode = 'cerebellum';

function initSlide5() {
    setSlide5Type('cerebellum');
}

function setSlide5Type(mode) {
    slide5Mode = mode;
    const canvas = document.getElementById('slide5Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide5Status');

    drawSlide5(ctx, canvas.width, canvas.height, mode);

    if (mode === 'cerebellum') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Cerebellar Precision:</span> Coordinates equilibrium, balance, and fine motor timing (e.g. riding a bicycle, walking straight along a chalk line, picking up a pen).';
    } else if (mode === 'medulla') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Medullary Involuntary Control:</span> Automatically sustains life via autonomous autonomic centers regulating blood pressure, peristalsis, salivation, and vomiting.';
    } else if (mode === 'cerebrum') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Cerebral Voluntary Action:</span> Conscious decision-making, planning, language articulation, and deliberate arm/leg movement commands.';
    }
}

function drawSlide5(ctx, w, h, mode) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    if (mode === 'cerebellum') {
        // Bicycle Rider Balance simulation
        const groundY = h * 0.72;
        ctx.strokeStyle = '#334155';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, groundY);
        ctx.lineTo(w, groundY);
        ctx.stroke();

        // Bicycle Wheels
        const bX = w * 0.5;
        const bY = groundY - 30;
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(bX - 50, bY, 24, 0, Math.PI * 2);
        ctx.arc(bX + 50, bY, 24, 0, Math.PI * 2);
        ctx.stroke();

        // Spokes
        for (let a = 0; a < Math.PI * 2; a += Math.PI / 3) {
            ctx.beginPath();
            ctx.moveTo(bX - 50, bY);
            ctx.lineTo(bX - 50 + Math.cos(a) * 24, bY + Math.sin(a) * 24);
            ctx.moveTo(bX + 50, bY);
            ctx.lineTo(bX + 50 + Math.cos(a) * 24, bY + Math.sin(a) * 24);
            ctx.stroke();
        }

        // Frame
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(bX - 50, bY);
        ctx.lineTo(bX - 10, bY);
        ctx.lineTo(bX + 25, bY - 35);
        ctx.lineTo(bX - 20, bY - 35);
        ctx.closePath();
        ctx.stroke();

        // Rider
        ctx.fillStyle = '#34d399';
        ctx.beginPath();
        ctx.arc(bX - 5, bY - 70, 14, 0, Math.PI * 2);
        ctx.fill();

        // Posture alignment line (Equilibrium)
        ctx.strokeStyle = '#4ade80';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(bX, 20);
        ctx.lineTo(bX, groundY);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#4ade80';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Posture & Dynamic Equilibrium (Cerebellum)', 110, 40);

    } else if (mode === 'medulla') {
        // Heart & Blood Vessel & Stomach
        const midX = w * 0.5;

        // Heart beating outline
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.moveTo(midX, 90);
        ctx.bezierCurveTo(midX + 35, 60, midX + 60, 100, midX, 145);
        ctx.bezierCurveTo(midX - 60, 100, midX - 35, 60, midX, 90);
        ctx.fill();

        // Pulse waves around heart
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(midX, 105, 50, 0, Math.PI * 2);
        ctx.stroke();

        // Blood pressure & autonomic readouts
        ctx.fillStyle = '#fca5a5';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Blood Pressure: 120/80 mmHg', midX - 85, 175);
        ctx.fillText('Peristalsis & Salivation Active', midX - 80, 200);
        ctx.fillText('Vomiting / Swallowing Centers', midX - 85, 225);

        ctx.fillStyle = '#f87171';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Involuntary Autonomous Control (Medulla Oblongata)', 70, 35);

    } else if (mode === 'cerebrum') {
        // Decision making node map
        const cx = w * 0.5;
        const cy = h * 0.5;

        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(cx, cy, 32, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#0f172a';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('THINKING', cx - 26, cy + 4);

        const nodes = [
            { label: 'Voluntary Motion', x: cx - 120, y: cy - 40, col: '#38bdf8' },
            { label: 'Hunger Satiety', x: cx + 120, y: cy - 40, col: '#fb923c' },
            { label: 'Sensory Perception', x: cx - 110, y: cy + 50, col: '#a78bfa' },
            { label: 'Memory / Reason', x: cx + 110, y: cy + 50, col: '#34d399' }
        ];

        nodes.forEach(n => {
            ctx.strokeStyle = '#64748b';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(cx, cy);
            ctx.lineTo(n.x, n.y);
            ctx.stroke();

            ctx.fillStyle = n.col;
            ctx.beginPath();
            ctx.arc(n.x, n.y, 20, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = '#f8fafc';
            ctx.font = '10px sans-serif';
            ctx.fillText(n.label, n.x - 40, n.y + 32);
        });

        ctx.fillStyle = '#fef08a';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Conscious Voluntary Processing (Fore-Brain Cerebrum)', 65, 35);
    }
}

// ==========================================
// SIMULATOR 6: Nervous Tissue Protection
// ==========================================
let slide6View = 'skull';

function initSlide6() {
    setSlide6View('skull');
}

function setSlide6View(view) {
    slide6View = view;
    const canvas = document.getElementById('slide6Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide6Status');

    drawSlide6(ctx, canvas.width, canvas.height, view);

    if (view === 'skull') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Cranium & CSF Cushion:</span> The brain is enclosed in a bony skull box (cranium) inside a fluid-filled balloon of cerebrospinal fluid that absorbs mechanical shocks. The spinal cord is shielded inside the vertebral column.';
    } else {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Neuromuscular Junction:</span> Motor nerve impulse stimulates muscle cells, triggering actin and myosin proteins to change conformation and slide together, causing cellular shortening.';
    }
}

function drawSlide6(ctx, w, h, view) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0b1329';
    ctx.fillRect(0, 0, w, h);

    if (view === 'skull') {
        const cx = w * 0.5;
        const cy = h * 0.5;

        // Outer Bone (Cranium)
        ctx.fillStyle = '#64748b';
        ctx.beginPath();
        ctx.arc(cx, cy - 10, 110, 0, Math.PI * 2);
        ctx.fill();

        // CSF fluid layer (Cushion balloon)
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.arc(cx, cy - 10, 96, 0, Math.PI * 2);
        ctx.fill();

        // Brain Tissue
        ctx.fillStyle = '#ea580c';
        ctx.beginPath();
        ctx.arc(cx, cy - 10, 78, 0, Math.PI * 2);
        ctx.fill();

        // Brain folds
        ctx.strokeStyle = '#fdba74';
        ctx.lineWidth = 3;
        for (let i = -2; i <= 2; i++) {
            ctx.beginPath();
            ctx.arc(cx + i * 25, cy - 20, 20, 0.4, Math.PI * 0.8);
            ctx.stroke();
        }

        // Labels
        ctx.fillStyle = '#e2e8f0';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('1. Bony Cranium (Hard Skull)', 20, 40);

        ctx.fillStyle = '#38bdf8';
        ctx.fillText('2. Cerebrospinal Fluid (CSF Shock Absorber)', 20, 65);

        ctx.fillStyle = '#fdba74';
        ctx.fillText('3. Delicate Neural Brain Tissue', 20, 90);

        // Vertebral column illustration at bottom
        ctx.fillStyle = '#94a3b8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Vertebral Column (Backbone) encases Spinal Cord below', 80, h - 20);

    } else {
        // Neuromuscular Junction & Sliding Filaments
        const startX = 60;
        const nmjY = 90;

        // Nerve Terminal
        ctx.fillStyle = '#3b82f6';
        ctx.beginPath();
        ctx.ellipse(w * 0.5, nmjY, 40, 22, 0, 0, Math.PI * 2);
        ctx.fill();

        // Synaptic Vesicles
        ctx.fillStyle = '#f43f5e';
        for (let i = 0; i < 8; i++) {
            ctx.beginPath();
            ctx.arc(w * 0.5 - 25 + i * 7, nmjY + 10, 3, 0, Math.PI * 2);
            ctx.fill();
        }

        // Muscle Fiber Membrane (Sarcolemma)
        ctx.strokeStyle = '#ec4899';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(40, nmjY + 30);
        ctx.lineTo(w - 40, nmjY + 30);
        ctx.stroke();

        // Actin & Myosin Filaments
        const filY = nmjY + 70;
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(50, filY, w - 100, 65);

        // Thick Myosin filaments (red)
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(130, filY + 22);
        ctx.lineTo(w - 130, filY + 22);
        ctx.moveTo(130, filY + 44);
        ctx.lineTo(w - 130, filY + 44);
        ctx.stroke();

        // Thin Actin filaments (cyan) sliding inward
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(70, filY + 22);
        ctx.lineTo(190, filY + 22);
        ctx.moveTo(w - 70, filY + 22);
        ctx.lineTo(w - 190, filY + 22);
        ctx.moveTo(70, filY + 44);
        ctx.lineTo(190, filY + 44);
        ctx.moveTo(w - 70, filY + 44);
        ctx.lineTo(w - 190, filY + 44);
        ctx.stroke();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Motor Axon Terminal', w * 0.5 - 55, nmjY - 10);

        ctx.fillStyle = '#f43f5e';
        ctx.fillText('Neurotransmitter Release', w * 0.5 - 65, nmjY + 25);

        ctx.fillStyle = '#06b6d4';
        ctx.fillText('Actin Filaments (Sliding Inward)', 70, filY + 80);

        ctx.fillStyle = '#ef4444';
        ctx.fillText('Myosin Thick Filaments (Shortening Muscle)', 230, filY + 80);
    }
}

// ==========================================
// SIMULATOR 7: Plant Nastic Movements
// ==========================================
let slide7Collapsed = false;

function initSlide7() {
    resetSlide7();
}

function resetSlide7() {
    slide7Collapsed = false;
    const canvas = document.getElementById('slide7Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide7(ctx, canvas.width, canvas.height, false);
    const status = document.getElementById('slide7Status');
    if (status) status.innerHTML = 'Intact <i>Mimosa pudica</i> plant. Leaves are turgid and fully spread. Click <b>"Touch Leaflet"</b> to trigger water efflux.';
}

function touchSlide7Leaf() {
    slide7Collapsed = true;
    const canvas = document.getElementById('slide7Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide7(ctx, canvas.width, canvas.height, true);
    const status = document.getElementById('slide7Status');
    if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Thigmonastic Response:</span> Touch generates electrical-chemical signal; pulvinus cells lose potassium and water rapidly, losing turgor pressure and causing petiole/leaflets to droop instantly.';
}

function drawSlide7(ctx, w, h, collapsed) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#05131e';
    ctx.fillRect(0, 0, w, h);

    const stemX = 80;
    const baseY = h * 0.75;

    // Main Stem
    ctx.strokeStyle = '#15803d';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(stemX, h);
    ctx.lineTo(stemX, baseY - 50);
    ctx.stroke();

    // Pulvinus (Swollen leaf base)
    const pulvX = stemX + 5;
    const pulvY = baseY - 20;
    ctx.fillStyle = collapsed ? '#854d0e' : '#4ade80';
    ctx.beginPath();
    ctx.ellipse(pulvX + 10, pulvY, 14, collapsed ? 7 : 12, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Petiole Rachis
    const petioleAngle = collapsed ? 0.6 : -0.3;
    const petioleLen = 170;
    const endX = pulvX + Math.cos(petioleAngle) * petioleLen;
    const endY = pulvY + Math.sin(petioleAngle) * petioleLen;

    ctx.strokeStyle = '#16a34a';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(pulvX + 18, pulvY);
    ctx.lineTo(endX, endY);
    ctx.stroke();

    // Leaflets along rachis
    for (let i = 1; i <= 6; i++) {
        const f = i / 7;
        const lx = (pulvX + 18) + (endX - (pulvX + 18)) * f;
        const ly = pulvY + (endY - pulvY) * f;

        ctx.fillStyle = collapsed ? '#65a30d' : '#22c55e';

        if (collapsed) {
            // Folded closed leaflets
            ctx.beginPath();
            ctx.ellipse(lx, ly + 6, 12, 3, 0.8, 0, Math.PI * 2);
            ctx.fill();
        } else {
            // Wide open paired leaflets
            ctx.beginPath();
            ctx.ellipse(lx - 8, ly - 14, 14, 5, -0.6, 0, Math.PI * 2);
            ctx.ellipse(lx + 8, ly + 14, 14, 5, 0.6, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Touch indicator icon if collapsed
    if (collapsed) {
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(endX - 20, endY - 15, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('⚡', endX - 25, endY - 11);
    }

    // LABELS
    ctx.fillStyle = '#86efac';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Pulvinus (Turgor Motor Organ)', pulvX + 15, pulvY - 20);

    ctx.fillStyle = '#e2e8f0';
    ctx.font = '11px sans-serif';
    ctx.fillText(collapsed ? 'Collapsed: Water leaves pulvinus cells' : 'Turgid: High water pressure keeps leaves erect', 140, 45);
}

// ==========================================
// SIMULATOR 8: Plant Directional Tropisms
// ==========================================
let slide8Trop = 'thigmo';

function initSlide8() {
    setSlide8Tropism('thigmo');
}

function setSlide8Tropism(trop) {
    slide8Trop = trop;
    const canvas = document.getElementById('slide8Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide8Status');

    drawSlide8(ctx, canvas.width, canvas.height, trop);

    if (trop === 'thigmo') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Thigmotropism (Pea Tendril):</span> Cells in contact with support wire grow slower; cells on free outer side elongate rapidly, causing tendril to coil tightly around support.';
    } else if (trop === 'geo') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Geotropism (Gravity Response):</span> Roots exhibit positive geotropism (bend downward toward gravity pull); shoots exhibit negative geotropism (bend upward away from gravity).';
    } else if (trop === 'chemo') {
        if (status) status.innerHTML = '<span class="text-purple-400 font-bold">Chemotropism (Pollen Tube):</span> Pollen grain on stigma germinates pollen tube that navigates accurately down style toward ovule driven by chemical attractants.';
    }
}

function drawSlide8(ctx, w, h, trop) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060e1a';
    ctx.fillRect(0, 0, w, h);

    if (trop === 'thigmo') {
        // Vertical support stick
        const poleX = w * 0.55;
        ctx.fillStyle = '#78350f';
        ctx.fillRect(poleX - 6, 30, 12, h - 50);

        ctx.fillStyle = '#d97706';
        ctx.font = '11px sans-serif';
        ctx.fillText('Solid Support Pole', poleX + 15, 50);

        // Pea Tendril coiling around pole
        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(60, h - 50);
        ctx.quadraticCurveTo(140, h - 70, poleX - 6, h * 0.6);

        // Coils
        for (let y = h * 0.6; y > 80; y -= 24) {
            ctx.bezierCurveTo(poleX + 18, y - 6, poleX + 18, y - 18, poleX - 6, y - 24);
        }
        ctx.stroke();

        ctx.fillStyle = '#4ade80';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Pea Tendril Contact (Differential Elongation)', 50, 40);

    } else if (trop === 'geo') {
        // Horizontal Seedling showing Geotropic curvature
        const midX = w * 0.45;
        const midY = h * 0.5;

        // Seed
        ctx.fillStyle = '#854d0e';
        ctx.beginPath();
        ctx.ellipse(midX, midY, 18, 12, 0, 0, Math.PI * 2);
        ctx.fill();

        // Shoot bending UP (-ve Geotropism)
        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(midX + 15, midY);
        ctx.quadraticCurveTo(midX + 60, midY, midX + 65, midY - 70);
        ctx.stroke();

        // Shoot leaves
        ctx.fillStyle = '#4ade80';
        ctx.beginPath();
        ctx.ellipse(midX + 65, midY - 75, 12, 6, 0.3, 0, Math.PI * 2);
        ctx.fill();

        // Root bending DOWN (+ve Geotropism)
        ctx.strokeStyle = '#fef08a';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(midX - 15, midY);
        ctx.quadraticCurveTo(midX - 60, midY, midX - 65, midY + 70);
        ctx.stroke();

        // Gravity arrow
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(w - 60, 60);
        ctx.lineTo(w - 60, 140);
        ctx.lineTo(w - 66, 130);
        ctx.moveTo(w - 60, 140);
        ctx.lineTo(w - 54, 130);
        ctx.stroke();

        ctx.fillStyle = '#38bdf8';
        ctx.font = '10px sans-serif';
        ctx.fillText('Gravity (g)', w - 85, 160);

        ctx.fillStyle = '#86efac';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Shoot: Negative Geotropism', midX + 30, midY - 85);

        ctx.fillStyle = '#fef08a';
        ctx.fillText('Root: Positive Geotropism', midX - 140, midY + 80);

    } else if (trop === 'chemo') {
        // Carpel / Pistil structure
        const cX = w * 0.5;

        // Stigma (top)
        ctx.fillStyle = '#15803d';
        ctx.beginPath();
        ctx.arc(cX, 45, 20, 0, Math.PI * 2);
        ctx.fill();

        // Style (neck)
        ctx.fillStyle = '#166534';
        ctx.fillRect(cX - 12, 45, 24, 110);

        // Ovary (swollen base)
        ctx.beginPath();
        ctx.arc(cX, 185, 45, 0, Math.PI * 2);
        ctx.fill();

        // Ovule inside ovary
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(cX, 185, 18, 0, Math.PI * 2);
        ctx.fill();

        // Pollen Grain on Stigma
        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(cX - 6, 32, 6, 0, Math.PI * 2);
        ctx.fill();

        // Pollen Tube growing down style to ovule
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(cX - 6, 38);
        ctx.quadraticCurveTo(cX - 4, 100, cX - 6, 175);
        ctx.lineTo(cX, 185);
        ctx.stroke();

        ctx.fillStyle = '#fde68a';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Pollen Tube Growth', cX + 25, 95);
        ctx.fillText('Chemo-attractants in Ovule', cX + 55, 185);
    }
}

// ==========================================
// SIMULATOR 9: Phototropism Auxin Mechanism
// ==========================================
let slide9Light = 'unilateral';

function initSlide9() {
    setSlide9Light('unilateral');
}

function setSlide9Light(mode) {
    slide9Light = mode;
    const canvas = document.getElementById('slide9Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide9Status');

    drawSlide9(ctx, canvas.width, canvas.height, mode);

    if (mode === 'unilateral') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Unilateral Sunlight:</span> Auxin synthesized at tip diffuses toward shaded side. Higher auxin concentration on dark flank stimulates cell elongation, bending stem toward light.';
    } else if (mode === 'overhead') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Uniform Overhead Sunlight:</span> Auxin diffuses evenly down all sides of stem; symmetrical cell elongation produces straight vertical growth.';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Dark / Symmetrical:</span> In absence of directional light cue, uniform diffusion maintains upright vertical orientation.';
    }
}

function drawSlide9(ctx, w, h, mode) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#06101e';
    ctx.fillRect(0, 0, w, h);

    const stemBaseX = w * 0.45;
    const stemBaseY = h * 0.85;

    // Sun Position
    if (mode === 'unilateral') {
        // Sun on the right
        ctx.fillStyle = '#facc15';
        ctx.beginPath();
        ctx.arc(w - 55, 55, 26, 0, Math.PI * 2);
        ctx.fill();

        // Rays
        ctx.strokeStyle = 'rgba(250, 204, 21, 0.4)';
        ctx.lineWidth = 2;
        for (let a = 0; a < 6; a++) {
            ctx.beginPath();
            ctx.moveTo(w - 55, 55);
            ctx.lineTo(w - 110 - a * 15, 60 + a * 20);
            ctx.stroke();
        }

        ctx.fillStyle = '#fde047';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Directional Sunlight', w - 120, 30);

        // Bent Stem toward Sun
        ctx.strokeStyle = '#15803d';
        ctx.lineWidth = 22;
        ctx.beginPath();
        ctx.moveTo(stemBaseX, stemBaseY);
        ctx.quadraticCurveTo(stemBaseX, stemBaseY - 80, stemBaseX + 70, stemBaseY - 140);
        ctx.stroke();

        // Auxin dots (concentrated on SHADED left side!)
        ctx.fillStyle = '#f43f5e';
        const dots = [
            { x: stemBaseX - 10, y: stemBaseY - 30 },
            { x: stemBaseX - 12, y: stemBaseY - 60 },
            { x: stemBaseX - 5, y: stemBaseY - 90 },
            { x: stemBaseX + 20, y: stemBaseY - 115 },
            { x: stemBaseX + 45, y: stemBaseY - 135 }
        ];
        dots.forEach(d => {
            ctx.beginPath();
            ctx.arc(d.x, d.y, 4, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#f43f5e';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Auxin migrates to shaded side', stemBaseX - 140, stemBaseY - 90);
        ctx.fillText('(Causes faster elongation)', stemBaseX - 140, stemBaseY - 75);

    } else {
        // Overhead Sun
        ctx.fillStyle = '#facc15';
        ctx.beginPath();
        ctx.arc(stemBaseX, 40, 24, 0, Math.PI * 2);
        ctx.fill();

        // Straight Upright Stem
        ctx.strokeStyle = '#15803d';
        ctx.lineWidth = 22;
        ctx.beginPath();
        ctx.moveTo(stemBaseX, stemBaseY);
        ctx.lineTo(stemBaseX, stemBaseY - 130);
        ctx.stroke();

        // Symmetrical Auxin dots
        ctx.fillStyle = '#f43f5e';
        for (let y = stemBaseY - 20; y > stemBaseY - 120; y -= 20) {
            ctx.beginPath();
            ctx.arc(stemBaseX - 7, y, 4, 0, Math.PI * 2);
            ctx.arc(stemBaseX + 7, y, 4, 0, Math.PI * 2);
            ctx.fill();
        }

        ctx.fillStyle = '#86efac';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Uniform Auxin Distribution (Straight Growth)', stemBaseX - 110, stemBaseY + 25);
    }
}

// ==========================================
// SIMULATOR 10: Plant Phytohormone Quartet
// ==========================================
let slide10Hormone = 'auxin';

function initSlide10() {
    setSlide10Hormone('auxin');
}

function setSlide10Hormone(hormone) {
    slide10Hormone = hormone;
    const canvas = document.getElementById('slide10Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide10Status');

    drawSlide10(ctx, canvas.width, canvas.height, hormone);

    if (hormone === 'auxin') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Auxin:</span> Synthesized at shoot tips. Promotes cell elongation, apical dominance, and phototropic/geotropic differential curvature.';
    } else if (hormone === 'gibberellin') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Gibberellins:</span> Stimulate stem internode elongation, breaking dwarfism and promoting seed germination.';
    } else if (hormone === 'cytokinin') {
        if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Cytokinins:</span> Promote rapid cytokinesis (cell division); present in high concentrations in growing fruits and seeds.';
    } else if (hormone === 'aba') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Abscisic Acid (ABA):</span> Primary growth inhibitor. Triggers stomatal closure during drought and causes wilting and leaf senescence.';
    }
}

function drawSlide10(ctx, w, h, hormone) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    // Plant Stem in background
    ctx.strokeStyle = '#1e3a1e';
    ctx.lineWidth = 14;
    ctx.beginPath();
    ctx.moveTo(midX, h - 30);
    ctx.lineTo(midX, 60);
    ctx.stroke();

    if (hormone === 'auxin') {
        // Highlight Tip
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(midX, 60, 18, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fda4af';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Shoot Tip Synthesis (Auxin)', midX + 30, 65);
        ctx.font = '11px sans-serif';
        ctx.fillText('• Cell Enlargement & Elongation', midX + 30, 85);
        ctx.fillText('• Apical Dominance', midX + 30, 102);

    } else if (hormone === 'gibberellin') {
        // Highlight internodes
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.moveTo(midX, 110);
        ctx.lineTo(midX, 180);
        ctx.stroke();

        ctx.fillStyle = '#fde68a';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Internode Elongation (Gibberellin)', midX + 30, 140);
        ctx.font = '11px sans-serif';
        ctx.fillText('• Overcomes genetic dwarfism', midX + 30, 160);
        ctx.fillText('• Promotes seed germination', midX + 30, 178);

    } else if (hormone === 'cytokinin') {
        // Developing fruit/seed node
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.ellipse(midX - 35, 120, 24, 18, 0.2, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#6ee7b7';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Rapid Cell Division (Cytokinin)', midX + 30, 115);
        ctx.font = '11px sans-serif';
        ctx.fillText('• High concentration in seeds & fruits', midX + 30, 135);
        ctx.fillText('• Delays leaf aging (senescence)', midX + 30, 153);

    } else if (hormone === 'aba') {
        // Wilting Leaf (Yellowed & drooping)
        ctx.fillStyle = '#ca8a04';
        ctx.beginPath();
        ctx.ellipse(midX + 45, 160, 30, 12, 0.6, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fef08a';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Growth Inhibitor (Abscisic Acid)', midX - 190, 150);
        ctx.font = '11px sans-serif';
        ctx.fillText('• Closes stomata during drought stress', midX - 190, 170);
        ctx.fillText('• Causes wilting and leaf fall', midX - 190, 188);
    }
}

// ==========================================
// SIMULATOR 11: Animal Endocrine System
// ==========================================
let slide11Mode = 'hormone';

function initSlide11() {
    setSlide11Mode('hormone');
}

function setSlide11Mode(mode) {
    slide11Mode = mode;
    const canvas = document.getElementById('slide11Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide11Status');

    drawSlide11(ctx, canvas.width, canvas.height, mode);

    if (mode === 'hormone') {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Endocrine System:</span> Ductless glands secrete hormones directly into the bloodstream; circulatory system carries molecules systemically to reach every cell equipped with specific receptors.';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Nervous System:</span> High-speed electrical action potentials confined strictly to wired axonal pathways; requires refractory recovery reset period.';
    }
}

function drawSlide11(ctx, w, h, mode) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#080d1a';
    ctx.fillRect(0, 0, w, h);

    if (mode === 'hormone') {
        // Blood Vessel Pipe
        const pipeY = h * 0.5;
        ctx.fillStyle = '#881337';
        ctx.fillRect(40, pipeY - 24, w - 80, 48);

        // Gland Cell Secreting
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(75, pipeY - 55, 20, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fda4af';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Endocrine Gland', 30, pipeY - 82);

        // Hormone molecules floating in blood
        ctx.fillStyle = '#fbbf24';
        for (let x = 90; x < w - 90; x += 35) {
            ctx.beginPath();
            ctx.arc(x, pipeY - 8 + (x % 3) * 6, 4, 0, Math.PI * 2);
            ctx.fill();
        }

        // Target Cell with Receptor
        ctx.fillStyle = '#1e3a8a';
        ctx.beginPath();
        ctx.arc(w - 75, pipeY + 55, 22, 0, Math.PI * 2);
        ctx.fill();

        // Specific receptor cup
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(w - 75, pipeY + 33, 8, Math.PI, 0);
        ctx.stroke();

        ctx.fillStyle = '#93c5fd';
        ctx.fillText('Target Cell Receptor', w - 130, pipeY + 95);

        ctx.fillStyle = '#fbbf24';
        ctx.fillText('Bloodstream Circulation (Systemic Hormone Delivery)', 85, 35);

    } else {
        // Nerve Wire
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(60, h * 0.5);
        ctx.lineTo(w - 60, h * 0.5);
        ctx.stroke();

        // Point to point impulses
        ctx.fillStyle = '#fef08a';
        for (let x = 120; x < w - 100; x += 70) {
            ctx.beginPath();
            ctx.arc(x, h * 0.5, 6, 0, Math.PI * 2);
            ctx.fill();
        }

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Point-to-Point Electrical Innervation (Strictly Wired)', 85, 45);
    }
}

// ==========================================
// SIMULATOR 12: Adrenaline Emergency Response
// ==========================================
let slide12Active = false;

function initSlide12() {
    resetSlide12();
}

function resetSlide12() {
    slide12Active = false;
    const canvas = document.getElementById('slide12Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide12(ctx, canvas.width, canvas.height, false);
    const status = document.getElementById('slide12Status');
    if (status) status.innerHTML = 'Normal basal resting state. Click <b>"Trigger Adrenaline Rush"</b> to activate fight-or-flight cardiovascular adaptations.';
}

function triggerSlide12Adrenaline() {
    slide12Active = true;
    const canvas = document.getElementById('slide12Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide12(ctx, canvas.width, canvas.height, true);
    const status = document.getElementById('slide12Status');
    if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Fight-or-Flight Response:</span> Adrenal glands release adrenaline directly into bloodstream — accelerates heart rate, diverts blood from skin/digestive tract to skeletal muscles, quickens breathing, and releases glucose.';
}

function drawSlide12(ctx, w, h, active) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#080d19';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    // Adrenal Gland atop Kidney
    ctx.fillStyle = '#854d0e';
    ctx.beginPath();
    ctx.ellipse(80, 130, 24, 38, 0.1, 0, Math.PI * 2);
    ctx.fill();

    // Adrenal Cap
    ctx.fillStyle = active ? '#ef4444' : '#ca8a04';
    ctx.beginPath();
    ctx.moveTo(60, 95);
    ctx.lineTo(80, 75);
    ctx.lineTo(100, 95);
    ctx.closePath();
    ctx.fill();

    ctx.fillStyle = '#fde047';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Adrenal Gland', 45, 68);

    // Dynamic metrics
    const heartBpm = active ? '145 BPM (Surging)' : '72 BPM (Resting)';
    const respRate = active ? '28 Breaths/min (Diaphragm rapid)' : '14 Breaths/min (Normal)';
    const bloodFlow = active ? 'Diverted to Skeletal Muscles (Skin constricted)' : 'Normal distribution to digestive system';

    ctx.fillStyle = active ? '#ef4444' : '#38bdf8';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText('Heart Rate: ' + heartBpm, 170, 85);

    ctx.fillStyle = active ? '#fb923c' : '#818cf8';
    ctx.fillText('Respiration: ' + respRate, 170, 120);

    ctx.fillStyle = active ? '#4ade80' : '#94a3b8';
    ctx.fillText('Blood Circulation: ' + bloodFlow, 170, 155);

    ctx.fillStyle = active ? '#facc15' : '#64748b';
    ctx.fillText(active ? 'Liver: High Glycogenolysis -> Blood Glucose Surge' : 'Liver: Basal Glycogen storage', 170, 190);
}

// ==========================================
// SIMULATOR 13: Thyroid Pituitary Hormones
// ==========================================
let slide13Gland = 'thyroid';

function initSlide13() {
    setSlide13Gland('thyroid');
}

function setSlide13Gland(gland) {
    slide13Gland = gland;
    const canvas = document.getElementById('slide13Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide13Status');

    drawSlide13(ctx, canvas.width, canvas.height, gland);

    if (gland === 'thyroid') {
        if (status) status.innerHTML = '<span class="text-amber-400 font-bold">Thyroid Gland (Thyroxin):</span> Regulates carbohydrate, protein, and fat metabolism for balanced growth. Requires dietary iodine; deficiency causes goitre (enlarged neck).';
    } else {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Pituitary Gland (Growth Hormone):</span> Located at the base of the brain ("master gland"). Deficiency in childhood causes dwarfism; excess secretion causes gigantism.';
    }
}

function drawSlide13(ctx, w, h, gland) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060d18';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    if (gland === 'thyroid') {
        // Neck outline
        ctx.strokeStyle = '#334155';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(midX - 70, 30);
        ctx.lineTo(midX - 50, 160);
        ctx.moveTo(midX + 70, 30);
        ctx.lineTo(midX + 50, 160);
        ctx.stroke();

        // Butterfly Thyroid Gland across trachea
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.ellipse(midX - 25, 95, 20, 30, -0.2, 0, Math.PI * 2);
        ctx.ellipse(midX + 25, 95, 20, 30, 0.2, 0, Math.PI * 2);
        ctx.fill();

        // Isthmus bridge
        ctx.fillRect(midX - 15, 90, 30, 12);

        ctx.fillStyle = '#fde047';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Thyroid Gland in Neck', midX - 60, 45);

        ctx.fillStyle = '#38bdf8';
        ctx.font = '11px sans-serif';
        ctx.fillText('Hormone: Thyroxin | Essential Nutrient: Dietary Iodine', midX - 140, 190);
        ctx.fillText('Deficiency Sign: Swollen neck goitre', midX - 95, 210);

    } else {
        // Pituitary Gland at Brain Base
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.arc(midX, 70, 45, 0, Math.PI * 2);
        ctx.fill();

        // Infundibulum stalk & Pituitary lobes
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.ellipse(midX - 8, 125, 12, 14, 0, 0, Math.PI * 2);
        ctx.ellipse(midX + 8, 125, 12, 14, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fde047';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Pituitary Gland ("Master Gland")', midX - 85, 30);

        ctx.fillStyle = '#4ade80';
        ctx.font = '11px sans-serif';
        ctx.fillText('Hormone: Growth Hormone (GH)', midX - 85, 175);
        ctx.fillText('Deficiency: Dwarfism | Excess: Gigantism', midX - 105, 195);
    }
}

// ==========================================
// SIMULATOR 14: Gonadal Puberty Hormones
// ==========================================
let slide14Gonad = 'male';

function initSlide14() {
    setSlide14Gonad('male');
}

function setSlide14Gonad(gonad) {
    slide14Gonad = gonad;
    const canvas = document.getElementById('slide14Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('slide14Status');

    drawSlide14(ctx, canvas.width, canvas.height, gonad);

    if (gonad === 'male') {
        if (status) status.innerHTML = '<span class="text-cyan-400 font-bold">Male (Testes & Testosterone):</span> Located in the scrotum; drives spermatogenesis and secondary sexual traits at puberty (facial hair, deeper voice, increased muscle mass).';
    } else {
        if (status) status.innerHTML = '<span class="text-rose-400 font-bold">Female (Ovaries & Oestrogen/Progesterone):</span> Located in the lower abdomen; regulates oogenesis, secondary sexual traits (mammary gland development), and the 28-day menstrual cycle.';
    }
}

function drawSlide14(ctx, w, h, gonad) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060e1b';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    if (gonad === 'male') {
        // Testes
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.ellipse(midX - 25, 100, 22, 28, 0, 0, Math.PI * 2);
        ctx.ellipse(midX + 25, 100, 22, 28, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Testes: Hormone Testosterone', midX - 95, 45);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px sans-serif';
        ctx.fillText('• Sperm production (spermatogenesis)', midX - 110, 160);
        ctx.fillText('• Deepening voice pitch', midX - 110, 180);
        ctx.fillText('• Facial & body hair development', midX - 110, 200);

    } else {
        // Ovaries & Uterus outline
        ctx.fillStyle = '#db2777';
        ctx.beginPath();
        ctx.ellipse(midX - 60, 100, 18, 14, -0.2, 0, Math.PI * 2);
        ctx.ellipse(midX + 60, 100, 18, 14, 0.2, 0, Math.PI * 2);
        ctx.fill();

        // Uterus
        ctx.fillStyle = '#9d174d';
        ctx.beginPath();
        ctx.moveTo(midX - 35, 80);
        ctx.lineTo(midX + 35, 80);
        ctx.lineTo(midX, 135);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#f472b6';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Ovaries: Oestrogen & Progesterone', midX - 110, 45);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px sans-serif';
        ctx.fillText('• Egg maturation & ovulation', midX - 110, 160);
        ctx.fillText('• 28-day menstrual cycle regulation', midX - 110, 180);
        ctx.fillText('• Breast & hip development', midX - 110, 200);
    }
}

// ==========================================
// SIMULATOR 15: Pancreas Insulin Feedback
// ==========================================
let slide15Active = false;

function initSlide15() {
    resetSlide15();
}

function resetSlide15() {
    slide15Active = false;
    const canvas = document.getElementById('slide15Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide15(ctx, canvas.width, canvas.height, false);
    const status = document.getElementById('slide15Status');
    if (status) status.innerHTML = 'Blood glucose at normal baseline (~90 mg/dL). Click <b>"Eat Carbohydrate Meal"</b> to observe closed-loop negative feedback.';
}

function triggerSlide15Meal() {
    slide15Active = true;
    const canvas = document.getElementById('slide15Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    drawSlide15(ctx, canvas.width, canvas.height, true);
    const status = document.getElementById('slide15Status');
    if (status) status.innerHTML = '<span class="text-emerald-400 font-bold">Negative Feedback Loop:</span> 1. High blood sugar detected by pancreas β-cells -> 2. Insulin secreted -> 3. Target cells absorb glucose & store as glycogen -> 4. Blood sugar falls back to normal -> 5. Insulin secretion stops.';
}

function drawSlide15(ctx, w, h, active) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#060c18';
    ctx.fillRect(0, 0, w, h);

    const midX = w * 0.5;

    // Closed Loop Feedback Flow
    // Step 1: Glucose Level
    ctx.fillStyle = active ? '#ef4444' : '#10b981';
    ctx.beginPath();
    ctx.roundRect(40, 40, 170, 45, 8);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText(active ? '1. High Blood Glucose' : '1. Normal Blood Glucose', 50, 60);
    ctx.font = '10px sans-serif';
    ctx.fillText(active ? '(160 mg/dL - Meal Eaten)' : '(90 mg/dL - Fasting)', 50, 75);

    // Arrow to Pancreas
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(210, 62);
    ctx.lineTo(w - 190, 62);
    ctx.stroke();

    // Step 2: Pancreas Islets
    ctx.fillStyle = '#ca8a04';
    ctx.beginPath();
    ctx.roundRect(w - 180, 40, 140, 45, 8);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('2. Pancreas β-Cells', w - 170, 60);
    ctx.font = '10px sans-serif';
    ctx.fillText(active ? 'Secrete INSULIN' : 'Insulin Idle', w - 170, 75);

    // Arrow Down
    ctx.beginPath();
    ctx.moveTo(w - 110, 85);
    ctx.lineTo(w - 110, 135);
    ctx.stroke();

    // Step 3: Target Cells (Liver / Muscle)
    ctx.fillStyle = '#0369a1';
    ctx.beginPath();
    ctx.roundRect(w - 190, 135, 160, 45, 8);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('3. Liver & Muscle Cells', w - 180, 155);
    ctx.font = '10px sans-serif';
    ctx.fillText(active ? 'Glucose -> Glycogen' : 'Basal Uptake', w - 180, 170);

    // Arrow back to Baseline
    ctx.beginPath();
    ctx.moveTo(w - 190, 158);
    ctx.lineTo(135, 158);
    ctx.lineTo(135, 85);
    ctx.stroke();

    ctx.fillStyle = '#4ade80';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('4. Negative Feedback: Blood Glucose falls, shutting off insulin', 60, 215);
}

// ==========================================
// SIMULATOR 16: Coordination System Integration
// ==========================================
function initSlide16() {
    filterSlide16('all');
}

function filterSlide16(mode) {
    const table = document.getElementById('slide16Table');
    if (!table) return;
    const rows = table.querySelectorAll('tr[data-sys]');
    rows.forEach(r => {
        if (mode === 'all') {
            r.style.display = '';
            r.style.opacity = '1';
        } else if (r.getAttribute('data-sys') === mode) {
            r.style.display = '';
            r.style.opacity = '1';
        } else {
            r.style.opacity = '0.25';
        }
    });
}
'''

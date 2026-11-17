# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 9: Light - Reflection and Refraction
Interactive Canvas & Simulator JavaScript Handlers (Slides 1 to 16)
"""

SIMULATOR_JS = '''
// ==========================================
// SIMULATOR 1: Light Nature & Duality
// ==========================================
let slide1State = { mode: 'ray', scale: 1 };

function initSlide1() {
    setSlide1Mode('ray');
}

function setSlide1Mode(mode) {
    slide1State.mode = mode;
    slide1State.scale = mode === 'ray' ? 1 : 2;
    const btnR = document.getElementById('btnSlide1Ray');
    const btnD = document.getElementById('btnSlide1Diff');
    const sld = document.getElementById('slide1ScaleSlider');
    const sDisp = document.getElementById('slide1ScaleDisplay');
    const model = document.getElementById('slide1Model');
    const shadow = document.getElementById('slide1Shadow');

    if (mode === 'ray') {
        if (btnR) btnR.className = 'px-3 py-1.5 rounded-xl bg-amber-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnD) btnD.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (sld) sld.value = 1;
        if (sDisp) sDisp.textContent = 'Macroscopic (5 cm)';
        if (model) model.textContent = 'Straight Ray Lines';
        if (shadow) shadow.textContent = 'Sharp Boundary';
    } else {
        if (btnD) btnD.className = 'px-3 py-1.5 rounded-xl bg-amber-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnR) btnR.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (sld) sld.value = 2;
        if (sDisp) sDisp.textContent = 'Microscopic (500 nm)';
        if (model) model.textContent = 'Wavefront Bending';
        if (shadow) shadow.textContent = 'Diffraction Fringes';
    }
    drawSlide1();
}

function setSlide1Scale(val) {
    if (val === '1') setSlide1Mode('ray');
    else setSlide1Mode('diffraction');
}

function drawSlide1() {
    const canvas = document.getElementById('slide1Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    if (slide1State.mode === 'ray') {
        // Macroscopic ray optics: Light source -> Opaque obstacle -> Sharp shadow
        // Source
        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(60, h * 0.5, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Source', 60, h * 0.5 + 32);

        // Opaque Obstacle
        const obsX = w * 0.45, obsH = 100;
        ctx.fillStyle = '#475569';
        ctx.fillRect(obsX, h * 0.5 - obsH * 0.5, 20, obsH);
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Obstacle (5 cm)', obsX + 10, h * 0.5 + obsH * 0.5 + 20);

        // Rays
        ctx.strokeStyle = '#fde047';
        ctx.lineWidth = 2;
        // Upper ray
        ctx.beginPath();
        ctx.moveTo(60, h * 0.5);
        ctx.lineTo(obsX, h * 0.5 - obsH * 0.5);
        ctx.lineTo(w - 50, h * 0.5 - 130);
        ctx.stroke();

        // Lower ray
        ctx.beginPath();
        ctx.moveTo(60, h * 0.5);
        ctx.lineTo(obsX, h * 0.5 + obsH * 0.5);
        ctx.lineTo(w - 50, h * 0.5 + 130);
        ctx.stroke();

        // Screen
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(w - 50, 40);
        ctx.lineTo(w - 50, h - 40);
        ctx.stroke();

        // Sharp Shadow on Screen
        ctx.strokeStyle = '#020617';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.moveTo(w - 50, h * 0.5 - 128);
        ctx.lineTo(w - 50, h * 0.5 + 128);
        ctx.stroke();

        ctx.fillStyle = '#ef4444';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Sharp Geometric Shadow', w - 120, h * 0.5);

    } else {
        // Wave diffraction: Wavefronts bending into shadow around tiny obstacle
        const slitX = w * 0.4;

        // Incoming plane waves
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        for (let x = 60; x < slitX; x += 30) {
            ctx.beginPath();
            ctx.moveTo(x, 60);
            ctx.lineTo(x, h - 60);
            ctx.stroke();
        }

        // Tiny obstacle (500 nm)
        ctx.fillStyle = '#cbd5e1';
        ctx.fillRect(slitX, h * 0.5 - 15, 12, 30);
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Tiny Edge (500 nm)', slitX + 6, h * 0.5 + 40);

        // Curved diffracted wavelets
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        for (let r = 25; r < 200; r += 28) {
            ctx.beginPath();
            ctx.arc(slitX + 12, h * 0.5 - 15, r, -Math.PI * 0.35, Math.PI * 0.35);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(slitX + 12, h * 0.5 + 15, r, -Math.PI * 0.35, Math.PI * 0.35);
            ctx.stroke();
        }

        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Diffraction: Waves bend into geometric shadow region', w * 0.75, h * 0.5);
    }
}

// ==========================================
// SIMULATOR 2: Laws of Reflection
// ==========================================
let slide2State = { angle: 45, lateral: false };

function initSlide2() {
    setSlide2Angle(45);
}

function setSlide2Angle(ang) {
    slide2State.angle = parseInt(ang);
    const aDisp = document.getElementById('slide2AngleDisplay');
    const rDisp = document.getElementById('slide2AngleR');
    if (aDisp) aDisp.textContent = `${slide2State.angle}°`;
    if (rDisp) rDisp.textContent = `${slide2State.angle}°`;
    drawSlide2();
}

function toggleSlide2Lateral() {
    slide2State.lateral = !slide2State.lateral;
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

    const mY = h * 0.7, pX = w * 0.5;

    // Mirror horizontal line
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(60, mY);
    ctx.lineTo(w - 60, mY);
    ctx.stroke();

    // Mirror hatching on bottom
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1.5;
    for (let x = 60; x <= w - 60; x += 15) {
        ctx.beginPath();
        ctx.moveTo(x, mY);
        ctx.lineTo(x - 8, mY + 12);
        ctx.stroke();
    }

    // Normal line
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(pX, mY);
    ctx.lineTo(pX, mY - 170);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Normal (N)', pX, mY - 180);

    // Calculate incident & reflected rays
    const rad = (slide2State.angle * Math.PI) / 180;
    const rayLen = 160;
    const incX = pX - Math.sin(rad) * rayLen;
    const incY = mY - Math.cos(rad) * rayLen;
    const refX = pX + Math.sin(rad) * rayLen;
    const refY = mY - Math.cos(rad) * rayLen;

    // Incident Ray (yellow)
    ctx.strokeStyle = '#fde047';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(incX, incY);
    ctx.lineTo(pX, mY);
    ctx.stroke();

    ctx.fillStyle = '#fde047';
    ctx.fillText(`Incident Ray (i = ${slide2State.angle}°)`, incX, incY - 10);

    // Reflected Ray (emerald)
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(pX, mY);
    ctx.lineTo(refX, refY);
    ctx.stroke();

    ctx.fillStyle = '#10b981';
    ctx.fillText(`Reflected Ray (r = ${slide2State.angle}°)`, refX, refY - 10);

    // Angle arcs
    ctx.strokeStyle = '#fde047';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(pX, mY, 40, -Math.PI / 2 - rad, -Math.PI / 2);
    ctx.stroke();

    ctx.strokeStyle = '#10b981';
    ctx.beginPath();
    ctx.arc(pX, mY, 40, -Math.PI / 2, -Math.PI / 2 + rad);
    ctx.stroke();

    if (slide2State.lateral) {
        // Lateral Inversion Demo
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(80, 40, 160, 60, 8);
        ctx.fill();
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 18px monospace';
        ctx.fillText('AMBULANCE', 160, 75);

        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(w - 240, 40, 160, 60, 8);
        ctx.fill();
        ctx.fillStyle = '#f43f5e';
        ctx.fillText('ƎƆИA⅃UБMA', w - 160, 75);
    }
}

// ==========================================
// SIMULATOR 3: Spherical Mirror Anatomy
// ==========================================
let slide3State = { type: 'concave', R: 30 };

function initSlide3() {
    setSlide3Type('concave');
}

function setSlide3Type(t) {
    slide3State.type = t;
    const btnC = document.getElementById('btnSlide3Concave');
    const btnV = document.getElementById('btnSlide3Convex');
    const fPos = document.getElementById('slide3FPos');

    if (t === 'concave') {
        if (btnC) btnC.className = 'px-3 py-1.5 rounded-xl bg-cyan-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnV) btnV.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (fPos) fPos.textContent = 'In Front of Mirror (Real)';
    } else {
        if (btnV) btnV.className = 'px-3 py-1.5 rounded-xl bg-cyan-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnC) btnC.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (fPos) fPos.textContent = 'Behind Mirror (Virtual)';
    }
    updateSlide3();
}

function setSlide3R(val) {
    slide3State.R = parseInt(val);
    const rDisp = document.getElementById('slide3RDisplay');
    const fDisp = document.getElementById('slide3FDisplay');
    if (rDisp) rDisp.textContent = `${slide3State.R} cm`;
    if (fDisp) fDisp.textContent = `${(slide3State.R / 2).toFixed(1)} cm`;
    updateSlide3();
}

function updateSlide3() {
    const canvas = document.getElementById('slide3Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const pX = w * 0.65, pY = h * 0.5;
    const scale = 5;
    const rPix = slide3State.R * scale;
    const fPix = rPix * 0.5;

    // Principal Axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(40, pY);
    ctx.lineTo(w - 40, pY);
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Principal Axis', 50, pY - 12);

    if (slide3State.type === 'concave') {
        // Concave Mirror (curves inward facing left)
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.arc(pX - rPix + rPix, pY, rPix, Math.PI - 0.5, Math.PI + 0.5);
        ctx.stroke();

        // Pole P
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(pX, pY, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('P (Pole)', pX + 10, pY + 18);

        // Focus F
        const fX = pX - fPix;
        ctx.fillStyle = '#34d399';
        ctx.beginPath();
        ctx.arc(fX, pY, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('F (Focus)', fX - 15, pY + 22);

        // Center C
        const cX = pX - rPix;
        ctx.fillStyle = '#a855f7';
        ctx.beginPath();
        ctx.arc(cX, pY, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('C (Center)', cX - 15, pY + 22);

        // Incoming parallel rays converging at F
        ctx.strokeStyle = '#fde047';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(60, pY - 60);
        ctx.lineTo(pX - 5, pY - 60);
        ctx.lineTo(fX, pY);
        ctx.moveTo(60, pY + 60);
        ctx.lineTo(pX - 5, pY + 60);
        ctx.lineTo(fX, pY);
        ctx.stroke();

    } else {
        // Convex Mirror (curves outward facing left)
        const mX = w * 0.35;
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.arc(mX + rPix, pY, rPix, Math.PI - 0.5, Math.PI + 0.5);
        ctx.stroke();

        // Pole P
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(mX, pY, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('P (Pole)', mX - 45, pY + 18);

        // Focus F behind
        const fX = mX + fPix;
        ctx.fillStyle = '#34d399';
        ctx.beginPath();
        ctx.arc(fX, pY, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('F (Virtual Focus)', fX - 30, pY + 22);

        // Center C behind
        const cX = mX + rPix;
        ctx.fillStyle = '#a855f7';
        ctx.beginPath();
        ctx.arc(cX, pY, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('C', cX - 5, pY + 22);
    }

    ctx.fillStyle = '#cbd5e1';
    ctx.textAlign = 'center';
    ctx.fillText(`Verification: R = ${slide3State.R} cm = 2f = 2 × ${(slide3State.R / 2).toFixed(1)} cm`, w * 0.5, h - 25);
}

// ==========================================
// SIMULATOR 4: 4 Standard Ray Tracing Rules
// ==========================================
let slide4State = { rayIdx: 1 };

function initSlide4() {
    setSlide4Ray(1);
}

function setSlide4Ray(idx) {
    slide4State.rayIdx = idx;
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnSlide4Ray${i}`);
        if (btn) {
            btn.className = (i === idx)
                ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold'
                : 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
        }
    }
    const desc = document.getElementById('slide4RuleDesc');
    const descriptions = [
        '',
        'Rule 1: A ray parallel to the principal axis passes through the principal focus F after reflection.',
        'Rule 2: A ray passing through the principal focus F reflects outward parallel to the principal axis.',
        'Rule 3: A ray passing through the center of curvature C strikes normally (i = 0) and retraces its own path.',
        'Rule 4: A ray incident obliquely at the pole P reflects symmetrically with an equal angle (i = r).'
    ];
    if (desc) desc.textContent = descriptions[idx];
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

    const pX = w * 0.75, pY = h * 0.5;
    const fX = pX - 100, cX = pX - 200;

    // Principal Axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(50, pY);
    ctx.lineTo(w - 50, pY);
    ctx.stroke();

    // Concave mirror curve
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.arc(cX + 200, pY, 200, Math.PI - 0.45, Math.PI + 0.45);
    ctx.stroke();

    // Landmarks
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(pX, pY, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillText('P', pX + 10, pY + 15);

    ctx.fillStyle = '#34d399';
    ctx.beginPath();
    ctx.arc(fX, pY, 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillText('F', fX - 5, pY + 18);

    ctx.fillStyle = '#a855f7';
    ctx.beginPath();
    ctx.arc(cX, pY, 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillText('C', cX - 5, pY + 18);

    // Dynamic Ray based on rule
    ctx.lineWidth = 3;
    if (slide4State.rayIdx === 1) {
        // Parallel -> F
        ctx.strokeStyle = '#fde047';
        ctx.beginPath();
        ctx.moveTo(80, pY - 70);
        ctx.lineTo(pX - 5, pY - 70);
        ctx.stroke();

        ctx.strokeStyle = '#10b981';
        ctx.beginPath();
        ctx.moveTo(pX - 5, pY - 70);
        ctx.lineTo(fX - 80, pY + 70);
        ctx.stroke();

    } else if (slide4State.rayIdx === 2) {
        // Through F -> Parallel
        ctx.strokeStyle = '#fde047';
        ctx.beginPath();
        ctx.moveTo(cX - 20, pY - 70);
        ctx.lineTo(pX - 5, pY + 70);
        ctx.stroke();

        ctx.strokeStyle = '#10b981';
        ctx.beginPath();
        ctx.moveTo(pX - 5, pY + 70);
        ctx.lineTo(80, pY + 70);
        ctx.stroke();

    } else if (slide4State.rayIdx === 3) {
        // Through C -> Retraces
        ctx.strokeStyle = '#ec4899';
        ctx.beginPath();
        ctx.moveTo(cX - 50, pY - 75);
        ctx.lineTo(pX - 15, pY - 25);
        ctx.stroke();

        ctx.fillStyle = '#ec4899';
        ctx.fillText('Retraces along normal (i = 0°)', cX, pY - 90);

    } else {
        // Oblique at P
        ctx.strokeStyle = '#fde047';
        ctx.beginPath();
        ctx.moveTo(cX - 30, pY - 80);
        ctx.lineTo(pX, pY);
        ctx.stroke();

        ctx.strokeStyle = '#10b981';
        ctx.beginPath();
        ctx.moveTo(pX, pY);
        ctx.lineTo(cX - 30, pY + 80);
        ctx.stroke();
    }
}

// ==========================================
// SIMULATOR 5: Concave Mirror 6 Positions
// ==========================================
let slide5State = { preset: 'beyondC' };

function initSlide5() {
    setSlide5Preset('beyondC');
}

function setSlide5Preset(p) {
    slide5State.preset = p;
    const oPos = document.getElementById('slide5ObjPos');
    const iPos = document.getElementById('slide5ImgPos');
    const iSize = document.getElementById('slide5ImgSize');
    const iNat = document.getElementById('slide5ImgNature');

    const config = {
        beyondC: { o: 'Beyond C', i: 'Between F and C', s: 'Diminished', n: 'Real & Inverted', oX: 300, oH: 60, iX: 160, iH: -35 },
        atC: { o: 'At C', i: 'At C', s: 'Same Size', n: 'Real & Inverted', oX: 240, oH: 50, iX: 240, iH: -50 },
        betweenCF: { o: 'Between C & F', i: 'Beyond C', s: 'Enlarged', n: 'Real & Inverted', oX: 180, oH: 40, iX: 320, iH: -70 },
        atF: { o: 'At F', i: 'At Infinity', s: 'Highly Enlarged', n: 'Real & Inverted', oX: 120, oH: 40, iX: 500, iH: -120 },
        betweenPF: { o: 'Between P & F', i: 'Behind Mirror', s: 'Magnified', n: 'Virtual & Erect', oX: 60, oH: 35, iX: -80, iH: 75 },
        infinity: { o: 'At Infinity', i: 'At F', s: 'Point-Sized', n: 'Real & Inverted', oX: 450, oH: 80, iX: 120, iH: -5 }
    };
    const c = config[p] || config.beyondC;

    if (oPos) oPos.textContent = c.o;
    if (iPos) iPos.textContent = c.i;
    if (iSize) iSize.textContent = c.s;
    if (iNat) iNat.textContent = c.n;

    drawSlide5(c);
}

function drawSlide5(c) {
    const canvas = document.getElementById('slide5Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const pX = w * 0.75, pY = h * 0.55;
    const fX = pX - 120, cX = pX - 240;

    // Principal Axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(30, pY);
    ctx.lineTo(w - 30, pY);
    ctx.stroke();

    // Mirror
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.arc(pX, pY, 240, Math.PI - 0.45, Math.PI + 0.45);
    ctx.stroke();

    // Landmarks
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('P', pX + 12, pY + 15);
    ctx.fillText('F', fX, pY + 18);
    ctx.fillText('C', cX, pY + 18);

    // Draw Object Arrow (teal)
    const objX = pX - c.oX;
    ctx.strokeStyle = '#2dd4bf';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(objX, pY);
    ctx.lineTo(objX, pY - c.oH);
    ctx.stroke();
    // Arrow head
    ctx.fillStyle = '#2dd4bf';
    ctx.beginPath();
    ctx.moveTo(objX, pY - c.oH - 8);
    ctx.lineTo(objX - 6, pY - c.oH);
    ctx.lineTo(objX + 6, pY - c.oH);
    ctx.fill();

    ctx.fillText('Object', objX, pY - c.oH - 12);

    // Draw Image Arrow (rose if real inverted, emerald if virtual erect)
    const imgX = pX - c.iX;
    const isVirtual = c.iH > 0;
    ctx.strokeStyle = isVirtual ? '#34d399' : '#f43f5e';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(imgX, pY);
    ctx.lineTo(imgX, pY - c.iH);
    ctx.stroke();

    ctx.fillStyle = isVirtual ? '#34d399' : '#f43f5e';
    ctx.fillText(isVirtual ? 'Virtual Image' : 'Real Image', imgX, pY - c.iH + (isVirtual ? -12 : 20));
}

// ==========================================
// SIMULATOR 6: Concave Mirror Applications
// ==========================================
let slide6State = { app: 'headlight' };

function initSlide6() {
    setSlide6App('headlight');
}

function setSlide6App(app) {
    slide6State.app = app;
    const btnH = document.getElementById('btnSlide6Headlight');
    const btnD = document.getElementById('btnSlide6Dentist');
    const btnS = document.getElementById('btnSlide6Solar');
    const status = document.getElementById('slide6Status');

    [btnH, btnD, btnS].forEach(b => {
        if (b) b.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    });
    if (app === 'headlight' && btnH) btnH.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-white text-xs font-semibold';
    if (app === 'dentist' && btnD) btnD.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-white text-xs font-semibold';
    if (app === 'solar' && btnS) btnS.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-white text-xs font-semibold';

    if (status) {
        if (app === 'headlight') status.textContent = 'Vehicle Headlights & Torches: High-intensity bulb at focus F produces a powerful, long-range parallel beam of light.';
        else if (app === 'dentist') status.textContent = 'Dentist / Shaving Mirror: Placing tooth/face between pole P and focus F produces an erect, highly magnified virtual view.';
        else status.textContent = 'Solar Furnace: Parallel solar rays from infinity reflect and converge at focus F, generating intense thermal heat to melt metals.';
    }
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

    if (slide6State.app === 'headlight') {
        // Headlight: Bulb at Focus F -> Parallel rays forward
        const mX = 140, mY = h * 0.5;
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.arc(mX - 80, mY, 120, -Math.PI * 0.35, Math.PI * 0.35);
        ctx.stroke();

        // Bulb at F
        ctx.fillStyle = '#fde047';
        ctx.beginPath();
        ctx.arc(mX - 20, mY, 12, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Bulb at F', mX - 20, mY + 28);

        // Parallel beams
        ctx.strokeStyle = '#fef08a';
        ctx.lineWidth = 3;
        for (let y = mY - 60; y <= mY + 60; y += 30) {
            ctx.beginPath();
            ctx.moveTo(mX, y);
            ctx.lineTo(w - 60, y);
            ctx.stroke();
        }

        ctx.fillStyle = '#fde047';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('Powerful Parallel Beam for Long-Range Driving', w * 0.65, mY - 80);

    } else if (slide6State.app === 'dentist') {
        // Dentist mirror magnifying tooth
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(80, 50, 200, 180, 12);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Tooth in Patient Mouth (u < f)', 180, 80);

        // Small tooth
        ctx.fillStyle = '#cbd5e1';
        ctx.fillRect(165, 120, 30, 45);

        // Magnified view in concave mirror
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(w - 280, 50, 200, 180, 12);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.fillStyle = '#34d399';
        ctx.fillText('Dentist View: Magnified Tooth', w - 180, 80);

        // Big tooth
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(w - 215, 105, 70, 95);

    } else {
        // Solar furnace
        const fX = w * 0.45, fY = h * 0.5;

        // Big concave reflector
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.arc(fX + 160, fY, 200, Math.PI - 0.45, Math.PI + 0.45);
        ctx.stroke();

        // Sunlight parallel rays
        ctx.strokeStyle = '#fde047';
        ctx.lineWidth = 2;
        for (let y = fY - 80; y <= fY + 80; y += 40) {
            ctx.beginPath();
            ctx.moveTo(60, y);
            ctx.lineTo(fX + 15, y);
            ctx.lineTo(fX, fY);
            ctx.stroke();
        }

        // Crucible melting at F
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(fX, fY, 15, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fca5a5';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Thermal Crucible (>2500°C)', fX, fY + 35);
    }
}

// ==========================================
// SIMULATOR 7: Convex Mirror Field of View
// ==========================================
let slide7State = { dist: 25, compareFov: false };

function initSlide7() {
    setSlide7Dist(25);
}

function setSlide7Dist(d) {
    slide7State.dist = parseInt(d);
    const dDisp = document.getElementById('slide7DistDisplay');
    if (dDisp) dDisp.textContent = `${slide7State.dist} m`;
    drawSlide7();
}

function toggleSlide7FieldOfView() {
    slide7State.compareFov = !slide7State.compareFov;
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

    const mX = w * 0.4, mY = h * 0.5;

    // Convex Mirror (curves outward toward left)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.arc(mX + 100, mY, 120, Math.PI - 0.5, Math.PI + 0.5);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Convex Mirror', mX, mY - 90);

    // Trailing car on left
    const carX = Math.max(70, mX - slide7State.dist * 5);
    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(carX - 25, mY - 20, 50, 40);
    ctx.fillStyle = '#ffffff';
    ctx.fillText('Car', carX, mY + 35);

    // Diminished virtual image inside mirror
    const imgX = mX + 25;
    ctx.fillStyle = '#60a5fa';
    ctx.fillRect(imgX - 8, mY - 7, 16, 14);
    ctx.fillStyle = '#a7f3d0';
    ctx.font = 'bold 10px sans-serif';
    ctx.fillText('Diminished (Erect)', imgX, mY + 25);

    if (slide7State.compareFov) {
        // Field of view cone
        ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
        ctx.beginPath();
        ctx.moveTo(mX, mY);
        ctx.lineTo(60, mY - 120);
        ctx.lineTo(60, mY + 120);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Wide Field of View (>90° Range)', 140, mY - 110);
    }
}

// ==========================================
// SIMULATOR 8: Cartesian Sign Convention
// ==========================================
let slide8State = { mirror: 'concave' };

function initSlide8() {
    setSlide8Mirror('concave');
}

function setSlide8Mirror(m) {
    slide8State.mirror = m;
    const btnC = document.getElementById('btnSlide8Concave');
    const btnV = document.getElementById('btnSlide8Convex');
    const fSign = document.getElementById('slide8FocalSign');

    if (m === 'concave') {
        if (btnC) btnC.className = 'px-2.5 py-1 rounded-lg bg-purple-600 text-white text-xs font-semibold';
        if (btnV) btnV.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
        if (fSign) fSign.textContent = 'Negative (-f)';
    } else {
        if (btnV) btnV.className = 'px-2.5 py-1 rounded-lg bg-purple-600 text-white text-xs font-semibold';
        if (btnC) btnC.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
        if (fSign) fSign.textContent = 'Positive (+f)';
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

    const oX = w * 0.5, oY = h * 0.5;

    // X and Y Coordinate Axes
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    // Horizontal X-axis
    ctx.beginPath();
    ctx.moveTo(50, oY);
    ctx.lineTo(w - 50, oY);
    ctx.stroke();

    // Vertical Y-axis
    ctx.beginPath();
    ctx.moveTo(oX, 40);
    ctx.lineTo(oX, h - 40);
    ctx.stroke();

    // Origin (Pole P)
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Pole P (Origin 0,0)', oX, oY + 20);

    // Direction indicators
    ctx.fillStyle = '#f43f5e';
    ctx.fillText('Left of P: Distances Negative (-x)', oX - 140, oY - 15);
    ctx.fillStyle = '#10b981';
    ctx.fillText('Right of P: Distances Positive (+x)', oX + 140, oY - 15);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText('Above Axis: Positive (+y)', oX - 80, 60);
    ctx.fillText('Below Axis: Negative (-y)', oX - 80, h - 60);

    // Mirror curve at origin
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 5;
    ctx.beginPath();
    if (slide8State.mirror === 'concave') {
        ctx.arc(oX, oY, 100, Math.PI - 0.4, Math.PI + 0.4);
    } else {
        ctx.arc(oX + 100, oY, 100, Math.PI - 0.4, Math.PI + 0.4);
    }
    ctx.stroke();
}

// ==========================================
// SIMULATOR 9: Mirror Formula & Magnification
// ==========================================
let slide9State = { u: -5.0, f: 1.5, isConcave: false };

function initSlide9() {
    loadSlide9Example('ex91');
}

function loadSlide9Example(ex) {
    const btn1 = document.getElementById('btnSlide9Ex1');
    const btn2 = document.getElementById('btnSlide9Ex2');

    if (ex === 'ex91') {
        slide9State = { u: -5.0, f: 1.5, isConcave: false };
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg bg-blue-600 text-white text-xs font-semibold';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    } else {
        slide9State = { u: -25.0, f: -15.0, isConcave: true };
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg bg-blue-600 text-white text-xs font-semibold';
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    }
    updateSlide9();
}

function updateSlide9() {
    const u = slide9State.u, f = slide9State.f;
    // 1/v = 1/f - 1/u
    const invV = (1 / f) - (1 / u);
    const v = 1 / invV;
    const m = -v / u;

    const uEl = document.getElementById('slide9UVal');
    const fEl = document.getElementById('slide9FVal');
    const vEl = document.getElementById('slide9VVal');
    const mEl = document.getElementById('slide9MVal');

    const unit = slide9State.isConcave ? 'cm' : 'm';
    if (uEl) uEl.textContent = `${u.toFixed(2)} ${unit}`;
    if (fEl) fEl.textContent = `${f > 0 ? '+' : ''}${f.toFixed(2)} ${unit}`;
    if (vEl) vEl.textContent = `${v > 0 ? '+' : ''}${v.toFixed(2)} ${unit}`;
    if (mEl) mEl.textContent = `${m > 0 ? '+' : ''}${m.toFixed(2)} (${m > 0 ? 'Virtual' : 'Real'})`;

    drawSlide9(u, f, v, m);
}

function drawSlide9(u, f, v, m) {
    const canvas = document.getElementById('slide9Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const mX = w * 0.5, mY = h * 0.55;

    // Principal Axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(50, mY);
    ctx.lineTo(w - 50, mY);
    ctx.stroke();

    // Mirror at center
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.arc(mX + (slide9State.isConcave ? 0 : 60), mY, 120, Math.PI - 0.45, Math.PI + 0.45);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Mirror (Pole P)', mX, mY + 25);

    // Visual arrows for Object & Image
    ctx.fillStyle = '#2dd4bf';
    ctx.fillText(`Object (u = ${u.toFixed(1)})`, mX - 120, mY - 80);
    ctx.strokeStyle = '#2dd4bf';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(mX - 120, mY);
    ctx.lineTo(mX - 120, mY - 60);
    ctx.stroke();

    ctx.fillStyle = v > 0 ? '#34d399' : '#f43f5e';
    ctx.fillText(`Image (v = ${v.toFixed(1)}, m = ${m.toFixed(2)})`, mX + (v > 0 ? 100 : -180), mY - 80);
    ctx.strokeStyle = v > 0 ? '#34d399' : '#f43f5e';
    ctx.beginPath();
    ctx.moveTo(mX + (v > 0 ? 100 : -180), mY);
    ctx.lineTo(mX + (v > 0 ? 100 : -180), mY - (v > 0 ? 30 : -60));
    ctx.stroke();
}

// ==========================================
// SIMULATOR 10: Refraction & Optical Illusions
// ==========================================
let slide10State = { demo: 'pencil' };

function initSlide10() {
    setSlide10Demo('pencil');
}

function setSlide10Demo(demo) {
    slide10State.demo = demo;
    const btnP = document.getElementById('btnSlide10Pencil');
    const btnC = document.getElementById('btnSlide10Coin');
    const btnT = document.getElementById('btnSlide10Tank');

    [btnP, btnC, btnT].forEach(b => {
        if (b) b.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    });
    if (demo === 'pencil' && btnP) btnP.className = 'px-2.5 py-1 rounded-lg bg-cyan-600 text-white text-xs font-semibold';
    if (demo === 'coin' && btnC) btnC.className = 'px-2.5 py-1 rounded-lg bg-cyan-600 text-white text-xs font-semibold';
    if (demo === 'tank' && btnT) btnT.className = 'px-2.5 py-1 rounded-lg bg-cyan-600 text-white text-xs font-semibold';

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

    if (slide10State.demo === 'pencil') {
        // Tumbler with bent pencil
        const bX = w * 0.5 - 70, bY = 70, bW = 140, bH = 200;

        // Water fill
        ctx.fillStyle = 'rgba(56, 189, 248, 0.2)';
        ctx.fillRect(bX, bY + 60, bW, bH - 60);

        // Glass boundary
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.strokeRect(bX, bY, bW, bH);

        // Pencil in air (straight)
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.moveTo(bX + 30, bY - 20);
        ctx.lineTo(bX + 70, bY + 60);
        ctx.stroke();

        // Pencil in water (bent shift)
        ctx.beginPath();
        ctx.moveTo(bX + 85, bY + 60);
        ctx.lineTo(bX + 115, bY + bH - 20);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Apparent Bending at Water Surface Line', w * 0.5, h - 25);

    } else if (slide10State.demo === 'coin') {
        // Bowl with reappearing coin
        const bowlX = w * 0.5, bowlY = h * 0.6;
        ctx.fillStyle = 'rgba(56, 189, 248, 0.25)';
        ctx.beginPath();
        ctx.arc(bowlX, bowlY, 100, 0, Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#cbd5e1';
        ctx.lineWidth = 4;
        ctx.stroke();

        // Coin at bottom
        ctx.fillStyle = '#fde047';
        ctx.beginPath();
        ctx.arc(bowlX - 40, bowlY + 60, 12, 0, Math.PI * 2);
        ctx.fill();

        // Virtual apparent coin higher up
        ctx.fillStyle = 'rgba(253, 224, 71, 0.6)';
        ctx.beginPath();
        ctx.arc(bowlX - 25, bowlY + 25, 12, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Refraction bends rays into observer line of sight (Activity 9.8)', w * 0.5, h - 25);

    } else {
        // Raised water tank floor
        ctx.fillStyle = 'rgba(56, 189, 248, 0.2)';
        ctx.fillRect(80, 80, w - 160, 160);

        // Real bottom
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(80, 240);
        ctx.lineTo(w - 80, 240);
        ctx.stroke();

        // Apparent raised bottom
        ctx.strokeStyle = '#38bdf8';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(80, 190);
        ctx.lineTo(w - 80, 190);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Apparent Depth = Real Depth / n (Floor Appears Raised)', w * 0.5, 175);
    }
}

// ==========================================
// SIMULATOR 11: Glass Slab Lateral Shift
// ==========================================
let slide11State = { angle: 45 };

function initSlide11() {
    setSlide11Angle(45);
}

function setSlide11Angle(ang) {
    slide11State.angle = parseInt(ang);
    const aDisp = document.getElementById('slide11AngleDisp');
    const eDisp = document.getElementById('slide11Emerg');
    if (aDisp) aDisp.textContent = `${slide11State.angle}°`;
    if (eDisp) eDisp.textContent = `${slide11State.angle}° (e = i)`;
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

    // Glass Slab
    const sX = 100, sY = 110, sW = w - 200, sH = 120;
    ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
    ctx.fillRect(sX, sY, sW, sH);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(sX, sY, sW, sH);

    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'right';
    ctx.fillText('Glass Slab (n = 1.5)', sX + sW - 15, sY + 25);

    // Angles
    const iRad = (slide11State.angle * Math.PI) / 180;
    const rRad = Math.asin(Math.sin(iRad) / 1.5); // Snell's Law

    const p1X = w * 0.4, p1Y = sY;
    const rayLen = 90;
    const incX = p1X - Math.sin(iRad) * rayLen;
    const incY = p1Y - Math.cos(iRad) * rayLen;

    const p2X = p1X + Math.tan(rRad) * sH;
    const p2Y = sY + sH;

    const emX = p2X + Math.sin(iRad) * rayLen;
    const emY = p2Y + Math.cos(iRad) * rayLen;

    // Normal at top
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(p1X, p1Y - 40);
    ctx.lineTo(p1X, p1Y + 40);
    ctx.stroke();

    // Normal at bottom
    ctx.beginPath();
    ctx.moveTo(p2X, p2Y - 40);
    ctx.lineTo(p2X, p2Y + 40);
    ctx.stroke();
    ctx.setLineDash([]);

    // Incident Ray (yellow)
    ctx.strokeStyle = '#fde047';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(incX, incY);
    ctx.lineTo(p1X, p1Y);
    ctx.stroke();

    // Refracted Ray inside slab (cyan)
    ctx.strokeStyle = '#38bdf8';
    ctx.beginPath();
    ctx.moveTo(p1X, p1Y);
    ctx.lineTo(p2X, p2Y);
    ctx.stroke();

    // Emergent Ray (emerald)
    ctx.strokeStyle = '#10b981';
    ctx.beginPath();
    ctx.moveTo(p2X, p2Y);
    ctx.lineTo(emX, emY);
    ctx.stroke();

    // Undeviated original path dotted
    ctx.strokeStyle = '#fde047';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([2, 4]);
    ctx.beginPath();
    ctx.moveTo(p1X, p1Y);
    ctx.lineTo(p1X + Math.sin(iRad) * 210, p1Y + Math.cos(iRad) * 210);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#10b981';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Emergent Ray is Parallel to Incident Ray (Lateral Shift d)', w * 0.5, h - 25);
}

// ==========================================
// SIMULATOR 12: Refractive Index & Kerosene
// ==========================================
let slide12State = { med: 'water' };

function initSlide12() {
    setSlide12Medium('water');
}

function setSlide12Medium(m) {
    slide12State.med = m;
    const indices = { water: 1.33, kerosene: 1.44, glass: 1.52, diamond: 2.42 };
    const n = indices[m] || 1.33;
    const v = (3.0 / n).toFixed(2);

    const iDisp = document.getElementById('slide12IndexDisp');
    const sDisp = document.getElementById('slide12SpeedDisp');
    const dDisp = document.getElementById('slide12DensityDisp');

    if (iDisp) iDisp.textContent = n.toFixed(2);
    if (sDisp) sDisp.textContent = `${v} × 10⁸ m/s`;
    if (dDisp) dDisp.textContent = n >= 1.5 ? 'Very High' : (n >= 1.4 ? 'High' : 'Moderate');

    drawSlide12(n, v);
}

function drawSlide12(n, v) {
    const canvas = document.getElementById('slide12Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Kerosene vs Water Density Demo Box
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(60, 45, 220, 210, 12);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('The Kerosene Paradox', 170, 70);

    // Beaker layers: Kerosene on top (yellow), Water on bottom (blue)
    ctx.fillStyle = 'rgba(250, 204, 21, 0.4)';
    ctx.fillRect(80, 100, 180, 60); // Kerosene
    ctx.fillStyle = '#fef08a';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Kerosene: n = 1.44 (Optically Denser)', 170, 135);
    ctx.font = '10px sans-serif';
    ctx.fillText('Mass Density: 0.8 g/cm³ (Floats)', 170, 150);

    ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
    ctx.fillRect(80, 160, 180, 70); // Water
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Water: n = 1.33 (Optically Rarer)', 170, 195);
    ctx.font = '10px sans-serif';
    ctx.fillText('Mass Density: 1.0 g/cm³ (Heavier)', 170, 210);

    // Right side: Speedometer graphic
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 280, 45, 220, 210, 12);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Light Velocity Gauge (c / n)', w - 170, 70);

    // Speed bar
    const barW = 160;
    const filledW = (v / 3.0) * barW;
    ctx.fillStyle = '#334155';
    ctx.fillRect(w - 250, 130, barW, 25);

    ctx.fillStyle = '#10b981';
    ctx.fillRect(w - 250, 130, filledW, 25);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px monospace';
    ctx.fillText(`${v} × 10⁸ m/s`, w - 170, 147);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('Higher Refractive Index -> Slower Propagation Speed', w * 0.5, h - 25);
}

// ==========================================
// SIMULATOR 13: Spherical Lens Geometry
// ==========================================
let slide13State = { lens: 'convex' };

function initSlide13() {
    setSlide13Lens('convex');
}

function setSlide13Lens(l) {
    slide13State.lens = l;
    const btnX = document.getElementById('btnSlide13Convex');
    const btnV = document.getElementById('btnSlide13Concave');
    const prof = document.getElementById('slide13Profile');
    const act = document.getElementById('slide13Action');

    if (l === 'convex') {
        if (btnX) btnX.className = 'px-3 py-1.5 rounded-xl bg-teal-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnV) btnV.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (prof) prof.textContent = 'Thicker in Middle';
        if (act) act.textContent = 'Converges at F2';
    } else {
        if (btnV) btnV.className = 'px-3 py-1.5 rounded-xl bg-teal-600 text-white text-xs font-semibold shadow-md transition-all';
        if (btnX) btnX.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all';
        if (prof) prof.textContent = 'Thinner in Middle';
        if (act) act.textContent = 'Diverges from F1';
    }
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

    const oX = w * 0.5, oY = h * 0.5;

    // Principal Axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(40, oY);
    ctx.lineTo(w - 40, oY);
    ctx.stroke();

    // Foci landmarks
    const fPix = 120;
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('O', oX, oY + 18);
    ctx.fillText('F1', oX - fPix, oY + 18);
    ctx.fillText('2F1', oX - fPix * 2, oY + 18);
    ctx.fillText('F2', oX + fPix, oY + 18);
    ctx.fillText('2F2', oX + fPix * 2, oY + 18);

    if (slide13State.lens === 'convex') {
        // Double convex lens (bulges outwards)
        ctx.fillStyle = 'rgba(45, 212, 191, 0.25)';
        ctx.strokeStyle = '#2dd4bf';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.ellipse(oX, oY, 24, 90, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Converging rays
        ctx.strokeStyle = '#fde047';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(60, oY - 50);
        ctx.lineTo(oX, oY - 50);
        ctx.lineTo(oX + fPix, oY);
        ctx.moveTo(60, oY + 50);
        ctx.lineTo(oX, oY + 50);
        ctx.lineTo(oX + fPix, oY);
        ctx.stroke();

    } else {
        // Double concave lens (thinner middle)
        ctx.fillStyle = 'rgba(56, 189, 248, 0.25)';
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(oX - 16, oY - 90);
        ctx.quadraticCurveTo(oX - 4, oY, oX - 16, oY + 90);
        ctx.lineTo(oX + 16, oY + 90);
        ctx.quadraticCurveTo(oX + 4, oY, oX + 16, oY - 90);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Diverging rays
        ctx.strokeStyle = '#fde047';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(60, oY - 50);
        ctx.lineTo(oX, oY - 50);
        ctx.lineTo(w - 60, oY - 95);
        ctx.moveTo(60, oY + 50);
        ctx.lineTo(oX, oY + 50);
        ctx.lineTo(w - 60, oY + 95);
        ctx.stroke();
    }
}

// ==========================================
// SIMULATOR 14: Convex Lens 6 Scenarios
// ==========================================
let slide14State = { preset: 'beyond2F' };

function initSlide14() {
    setSlide14Preset('beyond2F');
}

function setSlide14Preset(p) {
    slide14State.preset = p;
    const oPos = document.getElementById('slide14ObjPos');
    const iPos = document.getElementById('slide14ImgPos');
    const iSize = document.getElementById('slide14ImgSize');
    const iNat = document.getElementById('slide14ImgNature');

    const config = {
        beyond2F: { o: 'Beyond 2F1', i: 'Between F2 & 2F2', s: 'Diminished', n: 'Real & Inverted', oX: 240, oH: 60, iX: -150, iH: -38 },
        at2F: { o: 'At 2F1', i: 'At 2F2', s: 'Same Size', n: 'Real & Inverted', oX: 200, oH: 50, iX: -200, iH: -50 },
        betweenF2F: { o: 'Between F1 & 2F1', i: 'Beyond 2F2', s: 'Enlarged', n: 'Real & Inverted', oX: 150, oH: 40, iX: -260, iH: -70 },
        atF: { o: 'At F1', i: 'At Infinity', s: 'Highly Enlarged', n: 'Real & Inverted', oX: 100, oH: 40, iX: -450, iH: -120 },
        betweenOF: { o: 'Between O & F1', i: 'Same Side (Virtual)', s: 'Magnified', n: 'Virtual & Erect', oX: 50, oH: 30, iX: 140, iH: 80 },
        concave: { o: 'Any Position', i: 'Between O & F1', s: 'Diminished', n: 'Virtual & Erect', oX: 180, oH: 50, iX: 60, iH: 22 }
    };
    const c = config[p] || config.beyond2F;

    if (oPos) oPos.textContent = c.o;
    if (iPos) iPos.textContent = c.i;
    if (iSize) iSize.textContent = c.s;
    if (iNat) iNat.textContent = c.n;

    drawSlide14(c);
}

function drawSlide14(c) {
    const canvas = document.getElementById('slide14Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const oX = w * 0.5, oY = h * 0.55;
    const fPix = 100;

    // Principal Axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(30, oY);
    ctx.lineTo(w - 30, oY);
    ctx.stroke();

    // Convex lens outline
    ctx.fillStyle = 'rgba(16, 185, 129, 0.2)';
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.ellipse(oX, oY, 20, 85, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Landmarks
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('O', oX, oY + 16);
    ctx.fillText('F1', oX - fPix, oY + 16);
    ctx.fillText('2F1', oX - fPix * 2, oY + 16);
    ctx.fillText('F2', oX + fPix, oY + 16);
    ctx.fillText('2F2', oX + fPix * 2, oY + 16);

    // Object Arrow
    const objX = oX - c.oX;
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(objX, oY);
    ctx.lineTo(objX, oY - c.oH);
    ctx.stroke();

    ctx.fillStyle = '#38bdf8';
    ctx.fillText('Object', objX, oY - c.oH - 8);

    // Image Arrow
    const imgX = oX - c.iX;
    const isVirtual = c.iH > 0;
    ctx.strokeStyle = isVirtual ? '#34d399' : '#f43f5e';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(imgX, oY);
    ctx.lineTo(imgX, oY - c.iH);
    ctx.stroke();

    ctx.fillStyle = isVirtual ? '#34d399' : '#f43f5e';
    ctx.fillText(isVirtual ? 'Virtual Image' : 'Real Image', imgX, oY - c.iH + (isVirtual ? -8 : 16));
}

// ==========================================
// SIMULATOR 15: Lens Formula & Magnification
// ==========================================
let slide15State = { u: -30.0, f: -15.0, isConcave: true };

function initSlide15() {
    loadSlide15Example('ex93');
}

function loadSlide15Example(ex) {
    const btn1 = document.getElementById('btnSlide15Ex3');
    const btn2 = document.getElementById('btnSlide15Ex4');

    if (ex === 'ex93') {
        slide15State = { u: -30.0, f: -15.0, isConcave: true };
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    } else {
        slide15State = { u: -15.0, f: 10.0, isConcave: false };
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold';
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700';
    }
    updateSlide15();
}

function updateSlide15() {
    const u = slide15State.u, f = slide15State.f;
    // 1/v = 1/f + 1/u
    const invV = (1 / f) + (1 / u);
    const v = 1 / invV;
    const m = v / u; // For lens, m = +v/u

    const uEl = document.getElementById('slide15UVal');
    const fEl = document.getElementById('slide15FVal');
    const vEl = document.getElementById('slide15VVal');
    const mEl = document.getElementById('slide15MVal');

    if (uEl) uEl.textContent = `${u.toFixed(1)} cm`;
    if (fEl) fEl.textContent = `${f > 0 ? '+' : ''}${f.toFixed(1)} cm`;
    if (vEl) vEl.textContent = `${v > 0 ? '+' : ''}${v.toFixed(1)} cm`;
    if (mEl) mEl.textContent = `${m > 0 ? '+' : ''}${m.toFixed(2)} (${m > 0 ? 'Virtual' : 'Real'})`;

    drawSlide15(u, f, v, m);
}

function drawSlide15(u, f, v, m) {
    const canvas = document.getElementById('slide15Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    const oX = w * 0.5, oY = h * 0.55;

    // Principal axis
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(40, oY);
    ctx.lineTo(w - 40, oY);
    ctx.stroke();

    // Lens outline
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.ellipse(oX, oY, 18, 80, 0, 0, Math.PI * 2);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Lens Center (O)', oX, oY + 20);

    // Object and image markers
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Object (u = ${u.toFixed(1)} cm)`, oX - 120, oY - 70);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(oX - 120, oY);
    ctx.lineTo(oX - 120, oY - 50);
    ctx.stroke();

    ctx.fillStyle = v > 0 ? '#10b981' : '#a7f3d0';
    ctx.fillText(`Image (v = ${v.toFixed(1)} cm, m = ${m.toFixed(2)})`, oX + (v > 0 ? 120 : -60), oY - 70);
    ctx.strokeStyle = v > 0 ? '#10b981' : '#a7f3d0';
    ctx.beginPath();
    ctx.moveTo(oX + (v > 0 ? 120 : -60), oY);
    ctx.lineTo(oX + (v > 0 ? 120 : -60), oY - (v > 0 ? -70 : 25));
    ctx.stroke();
}

// ==========================================
// SIMULATOR 16: Lens Power & Combinations
// ==========================================
let slide16State = { focalM: 0.5 };

function initSlide16() {
    setSlide16FocalSlider(50);
}

function setSlide16EyeType(t) {
    const sld = document.getElementById('slide16Slider');
    if (t === 'hypermetropia') {
        if (sld) sld.value = 50;
        setSlide16FocalSlider(50);
    } else {
        if (sld) sld.value = 40;
        setSlide16FocalSlider(-40);
    }
}

function setSlide16FocalSlider(val) {
    const fCm = parseInt(val);
    const fM = fCm / 100.0;
    slide16State.focalM = fM;

    const p = (1 / fM).toFixed(2);
    const fDisp = document.getElementById('slide16FDisplay');
    const pDisp = document.getElementById('slide16PowerDisp');
    const tDisp = document.getElementById('slide16TypeDisp');

    if (fDisp) fDisp.textContent = `${fM > 0 ? '+' : ''}${fM.toFixed(2)} m (${fCm > 0 ? '+' : ''}${fCm} cm)`;
    if (pDisp) pDisp.textContent = `${p > 0 ? '+' : ''}${p} D`;
    if (tDisp) tDisp.textContent = fM > 0 ? 'Convex (Converging)' : 'Concave (Diverging)';

    drawSlide16(fM, p);
}

function drawSlide16(fM, p) {
    const canvas = document.getElementById('slide16Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a101d';
    ctx.fillRect(0, 0, w, h);

    // Eyeglass Frame Graphic
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(80, 50, 200, 180, 16);
    ctx.fill();
    ctx.strokeStyle = '#2dd4bf';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Eyewear Prescription', 180, 80);

    ctx.fillStyle = '#2dd4bf';
    ctx.font = 'bold 22px monospace';
    ctx.fillText(`${p > 0 ? '+' : ''}${p} D`, 180, 130);

    ctx.fillStyle = '#cbd5e1';
    ctx.font = '11px sans-serif';
    ctx.fillText(fM > 0 ? 'Corrects Hypermetropia (Farsightedness)' : 'Corrects Myopia (Nearsightedness)', 180, 165);

    // Lens Combination Box (Right side)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(w - 280, 50, 200, 180, 16);
    ctx.fill();
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('Lens Combination Formula', w - 180, 80);

    ctx.fillStyle = '#a855f7';
    ctx.font = 'bold 16px monospace';
    ctx.fillText('P = P1 + P2 + P3', w - 180, 125);

    ctx.fillStyle = '#cbd5e1';
    ctx.font = '11px sans-serif';
    ctx.fillText('Example: (+3.5 D) + (-1.5 D) = +2.0 D', w - 180, 160);
    ctx.fillText('Maximizes optical instrument sharpness', w - 180, 180);
}
'''

if __name__ == "__main__":
    print("SIMULATOR_JS length:", len(SIMULATOR_JS))

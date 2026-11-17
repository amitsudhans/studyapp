
// Chapter 12: Magnetic Effects of Electric Current - Simulators Engine

let sim1AnimHandle = null;
let sim2AnimHandle = null;

function initSimulator(id) {
    if (sim1AnimHandle) { cancelAnimationFrame(sim1AnimHandle); sim1AnimHandle = null; }
    if (sim2AnimHandle) { cancelAnimationFrame(sim2AnimHandle); sim2AnimHandle = null; }

    switch(id) {
        case 1: sim1Init(); break;
        case 2: sim2Init(); break;
        case 3: sim3Init(); break;
        case 4: sim4Init(); break;
        case 5: sim5Init(); break;
        case 6: sim6Init(); break;
        case 7: sim7Init(); break;
        case 8: sim8Init(); break;
        case 9: sim9Init(); break;
        case 10: sim10Init(); break;
        case 11: sim11Init(); break;
        case 12: sim12Init(); break;
        case 13: sim13Init(); break;
        case 14: sim14Init(); break;
        case 15: sim15Init(); break;
        case 16: sim16Init(); break;
    }
}

// -------------------------------------------------------------
// Simulator 1: Oersted Compass Deflection Lab
// -------------------------------------------------------------
let sim1SwitchClosed = true;

function sim1ToggleSwitch() {
    sim1SwitchClosed = !sim1SwitchClosed;
    const btn = document.getElementById('sim1_btn_switch');
    if (btn) {
        btn.textContent = sim1SwitchClosed ? 'Current: ON (Closed)' : 'Current: OFF (Open)';
        btn.className = sim1SwitchClosed ? 'px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold' : 'px-3 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim1Update();
}

function sim1Init() {
    sim1Update();
}

function sim1Update() {
    const canvas = document.getElementById('sim1_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const iVal = parseFloat(document.getElementById('sim1_i_slider')?.value || 2.5);
    const dMm = parseFloat(document.getElementById('sim1_d_slider')?.value || 25);
    document.getElementById('sim1_i_txt').textContent = `${iVal.toFixed(1)} A`;
    document.getElementById('sim1_d_txt').textContent = `${dMm} mm`;

    // B = mu0 * I / (2 * pi * r), mu0 / 2pi = 2e-7
    const rM = dMm / 1000;
    const bWire = sim1SwitchClosed ? (2e-7 * iVal / rM) : 0;
    const bEarth = 3.5e-5; // 35 microTesla
    // Deflection angle tan theta = B_wire / B_earth
    const thetaRad = Math.atan(bWire / bEarth);
    const thetaDeg = (thetaRad * 180 / Math.PI);

    document.getElementById('sim1_val_angle').textContent = sim1SwitchClosed ? `${thetaDeg.toFixed(1)}° East` : '0.0° (Undeflected)';
    document.getElementById('sim1_val_b').textContent = `${(bWire * 1e5).toFixed(2)} × 10⁻⁵ T`;

    // Draw workbench
    const cx = w / 2;
    const cy = h / 2;

    // Geographic North-South guide line
    ctx.strokeStyle = 'rgba(100, 116, 139, 0.3)';
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(cx, 25); ctx.lineTo(cx, h - 25);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Geographic North', cx - 40, 20);
    ctx.fillText('Geographic South', cx - 40, h - 10);

    // Thick Copper Wire (AB) along North-South
    const wireX = cx;
    ctx.strokeStyle = '#b45309';
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.moveTo(wireX, 35);
    ctx.lineTo(wireX, h - 35);
    ctx.stroke();

    // Wire Core Highlight
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(wireX, 35); ctx.lineTo(wireX, h - 35);
    ctx.stroke();

    // Current Direction Arrows (flowing South to North)
    if (sim1SwitchClosed) {
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText(`Current I = ${iVal.toFixed(1)} A ↑`, wireX + 15, 60);

        // Arrowheads along wire
        for (let ay of [80, 130, 180]) {
            ctx.beginPath();
            ctx.moveTo(wireX, ay - 8);
            ctx.lineTo(wireX - 6, ay + 6);
            ctx.lineTo(wireX + 6, ay + 6);
            ctx.closePath();
            ctx.fill();
        }
    }

    // Compass Needle under or near the wire
    const compassX = cx + (dMm * 1.5);
    const compassY = cy;
    const compassR = 48;

    // Compass casing
    ctx.beginPath();
    ctx.arc(compassX, compassY, compassR, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    // Compass dial markings
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('N', compassX - 4, compassY - compassR + 14);
    ctx.fillText('S', compassX - 4, compassY + compassR - 6);
    ctx.fillText('W', compassX - compassR + 6, compassY + 4);
    ctx.fillText('E', compassX + compassR - 14, compassY + 4);

    // Pivoted Needle (Rotated by thetaDeg)
    ctx.save();
    ctx.translate(compassX, compassY);
    ctx.rotate((sim1SwitchClosed ? -thetaRad : 0)); // Deflect toward East

    // North half (Red)
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(-5, -6);
    ctx.lineTo(0, -compassR + 8);
    ctx.lineTo(5, -6);
    ctx.closePath();
    ctx.fillStyle = '#ef4444';
    ctx.fill();

    // South half (Silver/White)
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(-5, 6);
    ctx.lineTo(0, compassR - 8);
    ctx.lineTo(5, 6);
    ctx.closePath();
    ctx.fillStyle = '#cbd5e1';
    ctx.fill();

    // Pivot center dot
    ctx.beginPath();
    ctx.arc(0, 0, 4, 0, Math.PI * 2);
    ctx.fillStyle = '#f59e0b';
    ctx.fill();

    ctx.restore();

    // Description text
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = sim1SwitchClosed ? '#10b981' : '#f43f5e';
    ctx.fillText(sim1SwitchClosed ? '⚡ Magnetic Torque Active: Needle deflected toward East' : '○ Circuit Open: Needle aligned with Earth geomagnetic field', 40, h - 25);
}

// -------------------------------------------------------------
// Simulator 2: Bar Magnet & Iron Filings Pattern
// -------------------------------------------------------------
let sim2Filings = [];
let sim2Taps = 3;

function sim2Init() {
    sim2ResetFilings();
}

function sim2ResetFilings() {
    sim2Filings = [];
    sim2Taps = 0;
    const canvas = document.getElementById('sim2_canvas');
    const w = canvas ? canvas.width : 600;
    const h = canvas ? canvas.height : 260;

    for (let i = 0; i < 280; i++) {
        sim2Filings.push({
            x: 60 + Math.random() * (w - 120),
            y: 35 + Math.random() * (h - 70),
            angle: Math.random() * Math.PI,
            length: 8 + Math.random() * 6
        });
    }
    sim2Update();
}

function sim2TapBoard() {
    sim2Taps = Math.min(8, sim2Taps + 1);
    sim2Update();
}

function sim2Update() {
    const canvas = document.getElementById('sim2_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const magStrength = parseInt(document.getElementById('sim2_str_slider')?.value || 3);
    const orderPct = Math.min(100, sim2Taps * 15 + 10);
    document.getElementById('sim2_val_order').textContent = `${orderPct}% Aligned`;

    const cx = w / 2;
    const cy = h / 2;
    const magW = 140;
    const magH = 34;

    // Pole locations (North on Left, South on Right)
    const poleNX = cx - magW / 2 + 10;
    const poleNY = cy;
    const poleSX = cx + magW / 2 - 10;
    const poleSY = cy;

    // Draw Cardboard Background
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(40, 20, w - 80, h - 40);
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.strokeRect(40, 20, w - 80, h - 40);

    // Draw Iron Filings
    ctx.lineWidth = 1.5;
    sim2Filings.forEach(f => {
        // Calculate true dipole field angle at filing position (x, y)
        const rxN = f.x - poleNX;
        const ryN = f.y - poleNY;
        const rN3 = Math.pow(rxN*rxN + ryN*ryN, 1.5) || 1;

        const rxS = f.x - poleSX;
        const ryS = f.y - poleSY;
        const rS3 = Math.pow(rxS*rxS + ryS*ryS, 1.5) || 1;

        // B = B_North - B_South
        const bx = (rxN / rN3) - (rxS / rS3);
        const by = (ryN / rN3) - (ryS / rS3);
        const idealAngle = Math.atan2(by, bx);

        // Blend angle based on tap count
        const blend = Math.min(1, sim2Taps * 0.18);
        const currentAngle = f.angle * (1 - blend) + idealAngle * blend;

        // Draw filing needle
        const dx = Math.cos(currentAngle) * (f.length / 2);
        const dy = Math.sin(currentAngle) * (f.length / 2);

        ctx.strokeStyle = `rgba(226, 232, 240, ${0.4 + blend * 0.5})`;
        ctx.beginPath();
        ctx.moveTo(f.x - dx, f.y - dy);
        ctx.lineTo(f.x + dx, f.y + dy);
        ctx.stroke();
    });

    // Draw Bar Magnet in Center
    // North Pole (Red)
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(cx - magW/2, cy - magH/2, magW/2, magH);
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('N', cx - magW/2 + 25, cy + 5);

    // South Pole (Blue)
    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(cx, cy - magH/2, magW/2, magH);
    ctx.fillStyle = '#ffffff';
    ctx.fillText('S', cx + magW/2 - 35, cy + 5);

    // Magnet Border
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 2;
    ctx.strokeRect(cx - magW/2, cy - magH/2, magW, magH);
}

// -------------------------------------------------------------
// Simulator 3: Compass Step-by-Step Field Line Tracer
// -------------------------------------------------------------
let sim3Step = 3;
let sim3Line = 2;

function sim3StepForward() {
    sim3Step = (sim3Step + 1) % 9;
    sim3Update();
}

function sim3ResetTracing() {
    sim3Step = 0;
    sim3Update();
}

function sim3ChangeLine() {
    sim3Line = parseInt(document.getElementById('sim3_line_select')?.value || 2);
    sim3Step = 0;
    sim3Update();
}

function sim3Init() {
    sim3Update();
}

function sim3Update() {
    const canvas = document.getElementById('sim3_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    document.getElementById('sim3_val_progress').textContent = `Step ${sim3Step} / 8`;

    const cx = w / 2;
    const cy = h / 2;
    const magW = 140;
    const magH = 34;

    // Define 8 discrete waypoints for selected trajectory
    const trajectories = {
        1: [ // Upper tight loop
            {x: cx - 60, y: cy - 25, angle: -1.9},
            {x: cx - 45, y: cy - 65, angle: -1.3},
            {x: cx - 20, y: cy - 85, angle: -0.6},
            {x: cx, y: cy - 90, angle: 0.0},
            {x: cx + 20, y: cy - 85, angle: 0.6},
            {x: cx + 45, y: cy - 65, angle: 1.3},
            {x: cx + 60, y: cy - 25, angle: 1.9},
            {x: cx + 65, y: cy, angle: 3.14}
        ],
        2: [ // Central wide loop
            {x: cx - 65, y: cy - 15, angle: -2.3},
            {x: cx - 75, y: cy - 70, angle: -1.4},
            {x: cx - 35, y: cy - 105, angle: -0.5},
            {x: cx, y: cy - 110, angle: 0.0},
            {x: cx + 35, y: cy - 105, angle: 0.5},
            {x: cx + 75, y: cy - 70, angle: 1.4},
            {x: cx + 65, y: cy - 15, angle: 2.3},
            {x: cx + 65, y: cy, angle: 3.14}
        ],
        3: [ // Lower tight loop
            {x: cx - 60, y: cy + 25, angle: 1.9},
            {x: cx - 45, y: cy + 65, angle: 1.3},
            {x: cx - 20, y: cy + 85, angle: 0.6},
            {x: cx, y: cy + 90, angle: 0.0},
            {x: cx + 20, y: cy + 85, angle: -0.6},
            {x: cx + 45, y: cy + 65, angle: -1.3},
            {x: cx + 60, y: cy + 25, angle: -1.9},
            {x: cx + 65, y: cy, angle: 3.14}
        ]
    };

    const pts = trajectories[sim3Line];

    // Draw Bar Magnet
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(cx - magW/2, cy - magH/2, magW/2, magH);
    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(cx, cy - magH/2, magW/2, magH);
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 2;
    ctx.strokeRect(cx - magW/2, cy - magH/2, magW, magH);
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('N', cx - magW/2 + 25, cy + 5);
    ctx.fillText('S', cx + magW/2 - 35, cy + 5);

    // Draw traced curve up to current step
    if (sim3Step > 0) {
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(cx - magW/2, cy);
        for (let s = 0; s < Math.min(sim3Step, pts.length); s++) {
            ctx.lineTo(pts[s].x, pts[s].y);
        }
        ctx.stroke();

        // Pencil guide dots
        for (let s = 0; s < Math.min(sim3Step, pts.length); s++) {
            ctx.beginPath();
            ctx.arc(pts[s].x, pts[s].y, 4, 0, Math.PI * 2);
            ctx.fillStyle = '#f59e0b';
            ctx.fill();
        }
    }

    // Draw plotting compass at active step
    if (sim3Step > 0 && sim3Step <= pts.length) {
        const cp = pts[sim3Step - 1];
        const cR = 20;

        ctx.beginPath();
        ctx.arc(cp.x, cp.y, cR, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.save();
        ctx.translate(cp.x, cp.y);
        ctx.rotate(cp.angle);

        // Compass red arrow tip (North)
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.moveTo(0, 0); ctx.lineTo(-3, -3); ctx.lineTo(cR - 3, 0); ctx.lineTo(-3, 3);
        ctx.fill();

        // Compass silver back tip (South)
        ctx.fillStyle = '#cbd5e1';
        ctx.beginPath();
        ctx.moveTo(0, 0); ctx.lineTo(3, -3); ctx.lineTo(-cR + 3, 0); ctx.lineTo(3, 3);
        ctx.fill();

        ctx.restore();
    }
}

// -------------------------------------------------------------
// Simulator 4: Magnetic Field Vector & Non-Intersection Proof
// -------------------------------------------------------------
let sim4ParadoxMode = false;

function sim4TestIntersection() {
    sim4ParadoxMode = !sim4ParadoxMode;
    const btn = document.getElementById('sim4_btn_intersect');
    if (btn) {
        btn.textContent = sim4ParadoxMode ? 'Clear Paradox Simulation' : 'Simulate Intersection Paradox';
        btn.className = sim4ParadoxMode ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold' : 'px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim4Update();
}

function sim4Init() {
    sim4Update();
}

function sim4Update() {
    const canvas = document.getElementById('sim4_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const px = parseInt(document.getElementById('sim4_px_slider')?.value || 280);
    const py = parseInt(document.getElementById('sim4_py_slider')?.value || 65);

    const cx = w / 2;
    const cy = h / 2 + 30;
    const magW = 140;
    const magH = 34;

    // Draw Bar Magnet
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(cx - magW/2, cy - magH/2, magW/2, magH);
    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(cx, cy - magH/2, magW/2, magH);
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 2;
    ctx.strokeRect(cx - magW/2, cy - magH/2, magW, magH);
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('N', cx - magW/2 + 25, cy + 5);
    ctx.fillText('S', cx + magW/2 - 35, cy + 5);

    // Family of continuous smooth field lines
    const lineRadii = [45, 75, 110];
    ctx.lineWidth = 2;
    lineRadii.forEach(r => {
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.beginPath();
        ctx.ellipse(cx, cy, magW/2 + r * 0.7, r, 0, Math.PI, 0, false);
        ctx.stroke();

        ctx.beginPath();
        ctx.ellipse(cx, cy, magW/2 + r * 0.7, r, 0, 0, Math.PI, false);
        ctx.stroke();
    });

    if (sim4ParadoxMode) {
        // Draw artificial crossing lines intersecting at (px, py)
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(px - 70, py - 40); ctx.lineTo(px + 70, py + 40);
        ctx.moveTo(px - 70, py + 40); ctx.lineTo(px + 70, py - 40);
        ctx.stroke();

        // Dual needle confusion
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(px, py, 22, 0, Math.PI * 2);
        ctx.fill();

        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.fillText('⚡ Paradox! Needles point both ↗ and ↘ simultaneously!', 80, 25);
    } else {
        // Normal Probe at (px, py)
        // Tangent vector
        const dx = px - cx;
        const dy = py - cy;
        const tangentAngle = Math.atan2(dx, -dy);

        ctx.beginPath();
        ctx.arc(px, py, 20, 0, Math.PI * 2);
        ctx.fillStyle = '#0f172a';
        ctx.fill();
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Tangent Arrow
        ctx.save();
        ctx.translate(px, py);
        ctx.rotate(tangentAngle);
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(-16, 0); ctx.lineTo(16, 0); ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(16, 0); ctx.lineTo(8, -5); ctx.lineTo(8, 5); ctx.fillStyle = '#10b981'; ctx.fill();
        ctx.restore();

        ctx.font = '10px Inter, sans-serif';
        ctx.fillStyle = '#10b981';
        ctx.fillText('Unique Tangent Vector', px - 55, py - 26);
    }
}

// -------------------------------------------------------------
// Simulator 5: Current Reversal & Polarity Deflection Lab
// -------------------------------------------------------------
let sim5Direction = 'N_S';
let sim5KeyClosed = true;

function sim5SetDirection(dir) {
    sim5Direction = dir;
    const btnNS = document.getElementById('sim5_btn_n_s');
    const btnSN = document.getElementById('sim5_btn_s_n');
    if (dir === 'N_S') {
        if (btnNS) btnNS.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnSN) btnSN.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim5_val_flow').textContent = 'North to South';
        document.getElementById('sim5_val_deflect').textContent = 'Deflects toward EAST';
    } else {
        if (btnSN) btnSN.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnNS) btnNS.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim5_val_flow').textContent = 'South to North';
        document.getElementById('sim5_val_deflect').textContent = 'Deflects toward WEST';
    }
    sim5Update();
}

function sim5ToggleKey() {
    sim5KeyClosed = !sim5KeyClosed;
    const btn = document.getElementById('sim5_btn_key');
    if (btn) {
        btn.textContent = sim5KeyClosed ? 'Key Closed' : 'Key Open';
        btn.className = sim5KeyClosed ? 'px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold' : 'px-3 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim5Update();
}

function sim5Init() {
    sim5Update();
}

function sim5Update() {
    const canvas = document.getElementById('sim5_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h / 2;

    // Overhead Wire (horizontal along screen)
    ctx.strokeStyle = '#b45309';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(80, cy); ctx.lineTo(w - 80, cy);
    ctx.stroke();

    // Compass resting under the wire
    const compR = 45;
    ctx.beginPath();
    ctx.arc(cx, cy + 45, compR, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    // Deflection logic
    let angleRad = 0;
    if (sim5KeyClosed) {
        angleRad = (sim5Direction === 'N_S') ? 0.65 : -0.65;
    }

    ctx.save();
    ctx.translate(cx, cy + 45);
    ctx.rotate(angleRad);

    // Needle North (Red)
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.moveTo(0, 0); ctx.lineTo(-4, 5); ctx.lineTo(0, -compR + 8); ctx.lineTo(4, 5);
    ctx.fill();

    // Needle South (Silver)
    ctx.fillStyle = '#cbd5e1';
    ctx.beginPath();
    ctx.moveTo(0, 0); ctx.lineTo(-4, -5); ctx.lineTo(0, compR - 8); ctx.lineTo(4, -5);
    ctx.fill();

    ctx.restore();

    // Arrow along wire
    if (sim5KeyClosed) {
        ctx.fillStyle = '#38bdf8';
        const arrX = (sim5Direction === 'N_S') ? cx + 60 : cx - 60;
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText(sim5Direction === 'N_S' ? 'Current → (North to South)' : '← Current (South to North)', cx - 80, cy - 15);
    }
}

// -------------------------------------------------------------
// Simulator 6: Straight Wire Concentric Rings Field
// -------------------------------------------------------------
function sim6Init() {
    sim6Update();
}

function sim6Update() {
    const canvas = document.getElementById('sim6_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const iVal = parseFloat(document.getElementById('sim6_i_slider')?.value || 4);
    const rCm = parseFloat(document.getElementById('sim6_r_slider')?.value || 3);
    document.getElementById('sim6_i_txt').textContent = `${iVal.toFixed(1)} A`;
    document.getElementById('sim6_r_txt').textContent = `${rCm.toFixed(1)} cm`;

    // B = 2e-7 * I / (r / 100)
    const bT = (2e-7 * iVal / (rCm / 100));
    document.getElementById('sim6_val_b').textContent = `${(bT * 1e5).toFixed(2)} × 10⁻⁵ T`;

    const cx = w / 2;
    const cy = h / 2;

    // Concentric circles representing magnetic field
    const radii = [30, 60, 95, 135];
    radii.forEach(rad => {
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        ctx.arc(cx, cy, rad, 0, Math.PI * 2);
        ctx.stroke();

        // Direction arrows on concentric circles (Right-hand rule: anticlockwise if current OUT)
        for (let a of [0, Math.PI/2, Math.PI, 3*Math.PI/2]) {
            const ax = cx + Math.cos(a) * rad;
            const ay = cy + Math.sin(a) * rad;
            ctx.fillStyle = '#38bdf8';
            ctx.beginPath();
            ctx.arc(ax, ay, 3, 0, Math.PI * 2);
            ctx.fill();
        }
    });

    // Central Wire Cross-Section (Current coming OUT OF PAGE: dot)
    ctx.beginPath();
    ctx.arc(cx, cy, 14, 0, Math.PI * 2);
    ctx.fillStyle = '#b45309';
    ctx.fill();
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(cx, cy, 4, 0, Math.PI * 2);
    ctx.fillStyle = '#ffffff';
    ctx.fill();

    // Compass placed at chosen radius rCm
    const compPx = cx + (rCm * 18);
    const compPy = cy;
    ctx.beginPath();
    ctx.arc(compPx, compPy, 18, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Tangent needle pointing vertically UP (counter-clockwise)
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.moveTo(compPx, compPy); ctx.lineTo(compPx - 3, compPy + 3); ctx.lineTo(compPx, compPy - 14); ctx.lineTo(compPx + 3, compPy + 3);
    ctx.fill();

    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText(`r = ${rCm} cm`, compPx - 15, compPy + 28);
}

// -------------------------------------------------------------
// Simulator 7: Right-Hand Thumb Rule 3D Visualizer
// -------------------------------------------------------------
let sim7View = 'east';

function sim7SetView(v) {
    sim7View = v;
    const btnE = document.getElementById('sim7_btn_east');
    const btnW = document.getElementById('sim7_btn_west');
    if (v === 'east') {
        if (btnE) btnE.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnW) btnW.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim7_val_circ').textContent = 'Clockwise';
    } else {
        if (btnW) btnW.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnE) btnE.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim7_val_circ').textContent = 'Counter-Clockwise';
    }
    sim7Update();
}

function sim7Init() {
    sim7Update();
}

function sim7Update() {
    const canvas = document.getElementById('sim7_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h / 2;

    // Observer End View circular diagram
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(cx, cy, 75, 0, Math.PI * 2);
    ctx.stroke();

    // Central Conductor wire cross section
    ctx.beginPath();
    ctx.arc(cx, cy, 18, 0, Math.PI * 2);
    ctx.fillStyle = '#b45309';
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.stroke();

    if (sim7View === 'east') {
        // Current going away (into page from East to West: cross X)
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(cx - 7, cy - 7); ctx.lineTo(cx + 7, cy + 7);
        ctx.moveTo(cx + 7, cy - 7); ctx.lineTo(cx - 7, cy + 7);
        ctx.stroke();

        // Circulating arrows: Clockwise
        ctx.font = '12px Inter, sans-serif';
        ctx.fillStyle = '#fbbf24';
        ctx.fillText('Circulation: CLOCKWISE', cx - 65, 30);
        ctx.fillStyle = '#10b981';
        ctx.fillText('Directly Below: Points NORTH (→)', cx - 85, cy + 105);
        ctx.fillText('Directly Above: Points SOUTH (←)', cx - 85, cy - 90);
    } else {
        // View from West: Current coming towards observer (dot •)
        ctx.beginPath();
        ctx.arc(cx, cy, 5, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.fill();

        ctx.font = '12px Inter, sans-serif';
        ctx.fillStyle = '#fbbf24';
        ctx.fillText('Circulation: COUNTER-CLOCKWISE', cx - 85, 30);
    }
}

// -------------------------------------------------------------
// Simulator 8: Circular Loop Magnetic Field
// -------------------------------------------------------------
let sim8Sense = 'cw';

function sim8SetSense(s) {
    sim8Sense = s;
    const btnCW = document.getElementById('sim8_btn_cw');
    const btnCCW = document.getElementById('sim8_btn_ccw');
    if (s === 'cw') {
        if (btnCW) btnCW.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnCCW) btnCCW.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim8_val_pole').textContent = 'South Pole (Clock rule)';
        document.getElementById('sim8_val_dir').textContent = 'Into the Screen (⊗)';
    } else {
        if (btnCCW) btnCCW.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnCW) btnCW.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim8_val_pole').textContent = 'North Pole (Anti-clock rule)';
        document.getElementById('sim8_val_dir').textContent = 'Out of the Screen (⊙)';
    }
    sim8Update();
}

function sim8Init() {
    sim8Update();
}

function sim8Update() {
    const canvas = document.getElementById('sim8_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h / 2;

    // Draw Circular Wire Loop in perspective ellipse
    ctx.strokeStyle = '#b45309';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.ellipse(cx, cy, 140, 60, 0, 0, Math.PI * 2);
    ctx.stroke();

    // Central Field Line: Straight and perpendicular
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(cx, cy - 80); ctx.lineTo(cx, cy + 80);
    ctx.stroke();

    // Arrowhead on central line
    ctx.fillStyle = '#ef4444';
    if (sim8Sense === 'cw') {
        // Downward / into
        ctx.beginPath();
        ctx.moveTo(cx, cy + 85); ctx.lineTo(cx - 7, cy + 70); ctx.lineTo(cx + 7, cy + 70);
        ctx.fill();
    } else {
        // Upward / out
        ctx.beginPath();
        ctx.moveTo(cx, cy - 85); ctx.lineTo(cx - 7, cy - 70); ctx.lineTo(cx + 7, cy - 70);
        ctx.fill();
    }

    // Expanding field loops on left and right segments
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
    ctx.lineWidth = 1.5;
    for (let r of [25, 45, 70]) {
        ctx.beginPath();
        ctx.ellipse(cx - 140, cy, r, r * 0.8, 0, 0, Math.PI * 2);
        ctx.stroke();

        ctx.beginPath();
        ctx.ellipse(cx + 140, cy, r, r * 0.8, 0, 0, Math.PI * 2);
        ctx.stroke();
    }

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText('Central Field Lines: Straight & Parallel', cx - 100, h - 15);
}

// -------------------------------------------------------------
// Simulator 9: Multi-Turn Coil Superposition Analyzer
// -------------------------------------------------------------
function sim9Init() {
    sim9Update();
}

function sim9Update() {
    const canvas = document.getElementById('sim9_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const n = parseInt(document.getElementById('sim9_n_slider')?.value || 5);
    const i = parseFloat(document.getElementById('sim9_i_slider')?.value || 2.0);
    document.getElementById('sim9_n_txt').textContent = `${n} Turns`;
    document.getElementById('sim9_i_txt').textContent = `${i.toFixed(1)} A`;

    const b1 = (2e-7 * Math.PI * i / 0.1); // R = 10 cm
    const bTot = n * b1;

    document.getElementById('sim9_val_btot').textContent = `${(bTot * 1e5).toFixed(2)} × 10⁻⁵ T`;
    document.getElementById('sim9_val_b1').textContent = `${(b1 * 1e5).toFixed(2)} × 10⁻⁵ T`;
    document.getElementById('sim9_val_mult').textContent = `${n}× Amplification`;

    const cx = w / 2;
    const cy = h / 2;

    // Draw multi-turn windings
    for (let t = 0; t < n; t++) {
        const offset = (t - n/2) * 4;
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.ellipse(cx + offset, cy, 100, 50, 0, 0, Math.PI * 2);
        ctx.stroke();
    }

    // Dense straight parallel field vectors at center
    const numLines = Math.min(15, n * 2);
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    for (let l = 0; l < numLines; l++) {
        const lx = cx - 40 + (l * 80 / (numLines - 1 || 1));
        ctx.beginPath();
        ctx.moveTo(lx, cy - 60); ctx.lineTo(lx, cy + 60);
        ctx.stroke();
    }

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText(`B_total = n · B₁ = ${n} × ${(b1*1e5).toFixed(2)} = ${(bTot*1e5).toFixed(2)} × 10⁻⁵ T`, 140, h - 18);
}

// -------------------------------------------------------------
// Simulator 10: Solenoid Uniform Field Studio
// -------------------------------------------------------------
let sim10Polarity = 'L_N';

function sim10ToggleCurrent() {
    sim10Polarity = (sim10Polarity === 'L_N') ? 'L_S' : 'L_N';
    const btn = document.getElementById('sim10_btn_toggle');
    if (btn) {
        btn.textContent = (sim10Polarity === 'L_N') ? 'Left: North / Right: South' : 'Left: South / Right: North';
    }
    sim10Update();
}

function sim10Init() {
    sim10Update();
}

function sim10Update() {
    const canvas = document.getElementById('sim10_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const turns = parseInt(document.getElementById('sim10_density_slider')?.value || 12);
    document.getElementById('sim10_density_txt').textContent = `${turns} Turns`;

    const cx = w / 2;
    const cy = h / 2;
    const solW = 240;
    const solH = 60;

    // External field loops (Bar magnet exterior)
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)';
    ctx.lineWidth = 2;
    for (let r of [50, 85, 120]) {
        ctx.beginPath();
        ctx.ellipse(cx, cy, solW/2 + r * 0.4, r, 0, Math.PI, 0, false);
        ctx.stroke();
        ctx.beginPath();
        ctx.ellipse(cx, cy, solW/2 + r * 0.4, r, 0, 0, Math.PI, false);
        ctx.stroke();
    }

    // Inside core: Perfectly straight, parallel, uniform lines
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2.5;
    for (let row of [-18, -6, 6, 18]) {
        ctx.beginPath();
        ctx.moveTo(cx - solW/2 + 10, cy + row);
        ctx.lineTo(cx + solW/2 - 10, cy + row);
        ctx.stroke();

        // Arrowheads inside pointing toward North
        const arrX = cx;
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        if (sim10Polarity === 'L_N') {
            // Pointing Left
            ctx.moveTo(arrX - 10, cy + row); ctx.lineTo(arrX, cy + row - 4); ctx.lineTo(arrX, cy + row + 4);
        } else {
            // Pointing Right
            ctx.moveTo(arrX + 10, cy + row); ctx.lineTo(arrX, cy + row - 4); ctx.lineTo(arrX, cy + row + 4);
        }
        ctx.fill();
    }

    // Solenoid helical coils
    for (let t = 0; t < turns; t++) {
        const tx = cx - solW/2 + 15 + t * ((solW - 30) / (turns - 1));
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.ellipse(tx, cy, 6, solH/2, 0, 0, Math.PI * 2);
        ctx.stroke();
    }

    // Pole labels
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = (sim10Polarity === 'L_N') ? '#ef4444' : '#3b82f6';
    ctx.fillText((sim10Polarity === 'L_N') ? 'NORTH' : 'SOUTH', cx - solW/2 - 75, cy + 5);

    ctx.fillStyle = (sim10Polarity === 'L_N') ? '#3b82f6' : '#ef4444';
    ctx.fillText((sim10Polarity === 'L_N') ? 'SOUTH' : 'NORTH', cx + solW/2 + 15, cy + 5);
}

// -------------------------------------------------------------
// Simulator 11: Electromagnet Soft Iron Core Inducer
// -------------------------------------------------------------
let sim11Powered = true;

function sim11TogglePower() {
    sim11Powered = !sim11Powered;
    const btn = document.getElementById('sim11_btn_power');
    if (btn) {
        btn.textContent = sim11Powered ? 'Power: ENERGIZED' : 'Power: OFF (Open)';
        btn.className = sim11Powered ? 'px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold' : 'px-3 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim11Update();
}

function sim11Init() {
    sim11Update();
}

function sim11Update() {
    const canvas = document.getElementById('sim11_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const core = document.getElementById('sim11_core_select')?.value || 'soft_iron';
    const cx = w / 2;
    const cy = h / 2;

    let pinsHeld = 0;
    if (sim11Powered) {
        pinsHeld = (core === 'soft_iron') ? 45 : (core === 'steel') ? 30 : 5;
    } else {
        pinsHeld = (core === 'steel') ? 25 : 0; // Steel retains permanent magnetism
    }

    document.getElementById('sim11_val_lift').textContent = `${pinsHeld} Steel Pins Held`;
    document.getElementById('sim11_val_resid').textContent = (core === 'steel') ? 'High (Permanent Magnet)' : 'Zero (Demagnetized)';

    // Core rod
    if (core !== 'air') {
        ctx.fillStyle = (core === 'soft_iron') ? '#94a3b8' : '#475569';
        ctx.fillRect(cx - 120, cy - 20, 240, 40);
        ctx.strokeStyle = '#f8fafc';
        ctx.lineWidth = 2;
        ctx.strokeRect(cx - 120, cy - 20, 240, 40);

        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#0f172a';
        ctx.fillText(core === 'soft_iron' ? 'Soft Iron Core (High μ)' : 'Steel Core (Retentive)', cx - 60, cy + 4);
    }

    // Solenoid winding around core
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 4;
    for (let k = 0; k < 10; k++) {
        const kx = cx - 95 + k * 21;
        ctx.beginPath();
        ctx.ellipse(kx, cy, 7, 32, 0, 0, Math.PI * 2);
        ctx.stroke();
    }

    // Steel Pins attracted to pole
    if (pinsHeld > 0) {
        ctx.strokeStyle = '#cbd5e1';
        ctx.lineWidth = 2;
        for (let p = 0; p < Math.min(20, pinsHeld); p++) {
            const px = cx + 120 + (p % 4) * 6;
            const py = cy - 25 + p * 3;
            ctx.beginPath();
            ctx.moveTo(px, py); ctx.lineTo(px + 18, py + 12);
            ctx.stroke();
        }
    }
}

// -------------------------------------------------------------
// Simulator 12: Kicking Aluminium Rod Experiment
// -------------------------------------------------------------
let sim12CurrentForward = true;
let sim12MagnetUpward = true;

function sim12ToggleCurrent() {
    sim12CurrentForward = !sim12CurrentForward;
    const btn = document.getElementById('sim12_btn_curr');
    if (btn) {
        btn.textContent = sim12CurrentForward ? 'B → A (Forward)' : 'A → B (Reverse)';
    }
    sim12Update();
}

function sim12ToggleMagnet() {
    sim12MagnetUpward = !sim12MagnetUpward;
    const btn = document.getElementById('sim12_btn_mag');
    if (btn) {
        btn.textContent = sim12MagnetUpward ? 'Bottom N / Top S (Upward B)' : 'Bottom S / Top N (Downward B)';
    }
    sim12Update();
}

function sim12Init() {
    sim12Update();
}

function sim12Update() {
    const canvas = document.getElementById('sim12_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const theta = parseInt(document.getElementById('sim12_theta_slider')?.value || 90);
    document.getElementById('sim12_theta_txt').textContent = `${theta}°`;

    const cx = w / 2;
    const cy = h / 2;

    // Determine kick direction: Fleming Left Hand Rule
    // Current Forward (in), Field Up -> Thumb Left
    let kickLeft = true;
    if (!sim12CurrentForward && sim12MagnetUpward) kickLeft = false;
    else if (sim12CurrentForward && !sim12MagnetUpward) kickLeft = false;
    else if (!sim12CurrentForward && !sim12MagnetUpward) kickLeft = true;

    const sinVal = Math.sin(theta * Math.PI / 180);
    const displacementPx = (kickLeft ? -35 : 35) * sinVal;

    document.getElementById('sim12_val_force').textContent = (theta === 0) ? 'Zero Force (No Kick)' : (kickLeft ? 'Displaces to the LEFT' : 'Displaces to the RIGHT');
    document.getElementById('sim12_val_scaling').textContent = `${(sinVal * 100).toFixed(0)}% at ${theta}°`;

    // Draw Horseshoe Magnet Poles
    // Top Pole
    ctx.fillStyle = sim12MagnetUpward ? '#3b82f6' : '#ef4444';
    ctx.fillRect(cx - 50, cy - 90, 100, 35);
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText(sim12MagnetUpward ? 'S Pole' : 'N Pole', cx - 22, cy - 68);

    // Bottom Pole
    ctx.fillStyle = sim12MagnetUpward ? '#ef4444' : '#3b82f6';
    ctx.fillRect(cx - 50, cy + 55, 100, 35);
    ctx.fillStyle = '#ffffff';
    ctx.fillText(sim12MagnetUpward ? 'N Pole' : 'S Pole', cx - 22, cy + 77);

    // Magnetic field vectors (Green)
    ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
    ctx.lineWidth = 2;
    for (let x = -30; x <= 30; x += 30) {
        ctx.beginPath();
        ctx.moveTo(cx + x, cy + 50); ctx.lineTo(cx + x, cy - 50);
        ctx.stroke();
    }

    // Suspended Aluminium Rod AB
    const rodX = cx + displacementPx;
    ctx.fillStyle = '#cbd5e1';
    ctx.fillRect(rodX - 6, cy - 35, 12, 70);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(rodX - 6, cy - 35, 12, 70);

    // Suspension wires
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cx - 40, 20); ctx.lineTo(rodX, cy - 35);
    ctx.moveTo(cx + 40, 20); ctx.lineTo(rodX, cy + 35);
    ctx.stroke();

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText('A', rodX - 18, cy - 25);
    ctx.fillText('B', rodX - 18, cy + 30);
}

// -------------------------------------------------------------
// Simulator 13: Fleming's Left-Hand Rule Workbench
// -------------------------------------------------------------
let sim13ParticleX = 80;

function sim13FireParticle() {
    sim13ParticleX = 80;
    sim13Update();
}

function sim13Init() {
    sim13Update();
}

function sim13Update() {
    const canvas = document.getElementById('sim13_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const scenario = document.getElementById('sim13_scenario_select')?.value || 'ex12_2';
    const cx = w / 2;
    const cy = h / 2;

    // Draw Orthogonal Triad Axes representing Fleming Left Hand
    // Forefinger (Field): Y-axis UP or DOWN
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - 80);
    ctx.stroke();
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('Forefinger: Magnetic Field B ↓', cx + 10, cy - 70);

    // Middle finger (Current): X-axis LEFT
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(cx, cy); ctx.lineTo(cx - 100, cy);
    ctx.stroke();
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Middle: Current I ←', cx - 120, cy - 10);

    // Thumb (Force): 3D into page ⊗
    ctx.beginPath();
    ctx.arc(cx, cy, 24, 0, Math.PI * 2);
    ctx.fillStyle = '#ef4444';
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Cross for INTO PAGE
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(cx - 10, cy - 10); ctx.lineTo(cx + 10, cy + 10);
    ctx.moveTo(cx + 10, cy - 10); ctx.lineTo(cx - 10, cy + 10);
    ctx.stroke();

    ctx.fillStyle = '#ef4444';
    ctx.fillText('Thumb: Force F INTO PAGE (⊗)', cx - 75, cy + 45);
}

// -------------------------------------------------------------
// Simulator 14: Biomagnetism & Diagnostic MRI Studio
// -------------------------------------------------------------
let sim14Organ = 'brain';
let sim14RfActive = false;

function sim14SetOrgan(org) {
    sim14Organ = org;
    const btnB = document.getElementById('sim14_btn_brain');
    const btnH = document.getElementById('sim14_btn_heart');
    if (org === 'brain') {
        if (btnB) btnB.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnH) btnH.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
    } else {
        if (btnH) btnH.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnB) btnB.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
    }
    sim14Update();
}

function sim14PulseRF() {
    sim14RfActive = true;
    sim14Update();
    setTimeout(() => {
        sim14RfActive = false;
        sim14Update();
    }, 1500);
}

function sim14Init() {
    sim14Update();
}

function sim14Update() {
    const canvas = document.getElementById('sim14_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h / 2;

    // MRI Scanner Bore Casing
    ctx.beginPath();
    ctx.arc(cx, cy, 110, 0, Math.PI * 2);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 8;
    ctx.stroke();

    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(cx, cy, 105, 0, Math.PI * 2);
    ctx.fill();

    // Organ illustration inside bore
    if (sim14Organ === 'brain') {
        // Brain lobes
        ctx.fillStyle = '#a855f7';
        ctx.beginPath();
        ctx.arc(cx - 20, cy - 10, 35, 0, Math.PI * 2);
        ctx.arc(cx + 20, cy - 10, 35, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#f8fafc';
        ctx.fillText('Cerebral Cortex (Dense Synaptic Currents)', cx - 110, cy + 50);
    } else {
        // Heart
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(cx - 20, cy - 15, 25, 0, Math.PI * 2);
        ctx.arc(cx + 20, cy - 15, 25, 0, Math.PI * 2);
        ctx.moveTo(cx - 38, cy - 5); ctx.lineTo(cx, cy + 45); ctx.lineTo(cx + 38, cy - 5);
        ctx.fill();
        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#f8fafc';
        ctx.fillText('Cardiac Myocyte Action Potentials', cx - 90, cy + 60);
    }

    // RF excitation wave if active
    if (sim14RfActive) {
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 3;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.arc(cx, cy, 80, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#fbbf24';
        ctx.fillText('⚡ RF Radio Pulse Emitting Tissue Echo Signal', cx - 110, 35);
    }
}

// -------------------------------------------------------------
// Simulator 15: Domestic 220V AC Electrical Installation
// -------------------------------------------------------------
let sim15Loads = { lamp: true, fan: true, geyser: true };
let sim15MainClosed = true;

function sim15ToggleLoad(load) {
    sim15Loads[load] = !sim15Loads[load];
    const btn = document.getElementById(`sim15_btn_${load}`);
    if (btn) {
        const name = (load === 'lamp') ? '5A Lamp' : (load === 'fan') ? '5A Fan' : '15A Geyser';
        btn.textContent = `${name}: ${sim15Loads[load] ? 'ON' : 'OFF'}`;
        btn.className = sim15Loads[load] ? 'px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold' : 'px-2 py-0.5 rounded bg-rose-700 text-white text-[11px] font-bold';
    }
    sim15Update();
}

function sim15ToggleMain() {
    sim15MainClosed = !sim15MainClosed;
    const btn = document.getElementById('sim15_btn_main');
    if (btn) {
        btn.textContent = sim15MainClosed ? 'Main: CLOSED' : 'Main: OPEN';
        btn.className = sim15MainClosed ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold' : 'px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim15Update();
}

function sim15Init() {
    sim15Update();
}

function sim15Update() {
    const canvas = document.getElementById('sim15_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Current calc
    let totalI = 0;
    if (sim15MainClosed) {
        if (sim15Loads.lamp) totalI += 0.25;
        if (sim15Loads.fan) totalI += 0.35;
        if (sim15Loads.geyser) totalI += 9.50;
    }

    document.getElementById('sim15_val_current').textContent = `${totalI.toFixed(2)} A`;

    // Draw Three Bus Conductors
    // 1. Green Earth Wire (Top)
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 3.5;
    ctx.beginPath();
    ctx.moveTo(60, 40); ctx.lineTo(w - 60, 40);
    ctx.stroke();

    // 2. Red Live Wire (Middle)
    ctx.strokeStyle = sim15MainClosed ? '#ef4444' : '#64748b';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(60, 80); ctx.lineTo(w - 60, 80);
    ctx.stroke();

    // 3. Black Neutral Wire (Bottom)
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 3.5;
    ctx.beginPath();
    ctx.moveTo(60, 120); ctx.lineTo(w - 60, 120);
    ctx.stroke();

    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#22c55e'; ctx.fillText('Earth Wire (Green)', 65, 32);
    ctx.fillStyle = '#ef4444'; ctx.fillText('Live Wire (Red, 220V)', 65, 74);
    ctx.fillStyle = '#94a3b8'; ctx.fillText('Neutral Wire (Black, 0V)', 65, 136);

    // 3 Appliances in Parallel
    const apps = [
        { key: 'lamp', name: 'Bulb (50W)', x: 180, circuit: '5A' },
        { key: 'fan', name: 'Fan (75W)', x: 300, circuit: '5A' },
        { key: 'geyser', name: 'Geyser (2kW)', x: 440, circuit: '15A' }
    ];

    apps.forEach(app => {
        const isOn = sim15MainClosed && sim15Loads[app.key];
        ctx.strokeStyle = isOn ? '#ef4444' : '#64748b';
        ctx.lineWidth = 2;
        // Drops from Live & Neutral
        ctx.beginPath();
        ctx.moveTo(app.x, 80); ctx.lineTo(app.x, 160);
        ctx.moveTo(app.x + 20, 120); ctx.lineTo(app.x + 20, 160);
        ctx.stroke();

        // Appliance block
        ctx.fillStyle = isOn ? '#0f172a' : '#1e293b';
        ctx.fillRect(app.x - 15, 160, 50, 45);
        ctx.strokeStyle = isOn ? '#10b981' : '#64748b';
        ctx.lineWidth = 2;
        ctx.strokeRect(app.x - 15, 160, 50, 45);

        ctx.font = '10px Inter, sans-serif';
        ctx.fillStyle = isOn ? '#10b981' : '#64748b';
        ctx.fillText(app.name, app.x - 15, 220);
        ctx.fillText(app.circuit, app.x, 185);
    });
}

// -------------------------------------------------------------
// Simulator 16: Earth Wire & Fuse Safety Meltdown Lab
// -------------------------------------------------------------
let sim16EarthConnected = true;
let sim16FaultType = 'none';

function sim16ToggleEarth() {
    sim16EarthConnected = !sim16EarthConnected;
    const btn = document.getElementById('sim16_btn_earth');
    if (btn) {
        btn.textContent = sim16EarthConnected ? 'Earth Connected (Safe)' : 'Earth Broken (DANGEROUS)';
        btn.className = sim16EarthConnected ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold' : 'px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim16Update();
}

function sim16SimulateInsulationLeak() {
    sim16FaultType = 'leakage';
    sim16Update();
}

function sim16TriggerShortCircuit() {
    sim16FaultType = 'short';
    sim16Update();
}

function sim16ResetSystem() {
    sim16FaultType = 'none';
    sim16Update();
}

function sim16Init() {
    sim16Update();
}

function sim16Update() {
    const canvas = document.getElementById('sim16_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const isFuseBlown = (sim16FaultType === 'short');
    const isChassisLive = (sim16FaultType === 'leakage' && !sim16EarthConnected && !isFuseBlown);

    document.getElementById('sim16_val_chassis').textContent = isChassisLive ? '220 V DANGER (Live Chassis)' : '0 V (Safe Earth Discharge)';
    document.getElementById('sim16_val_chassis').className = isChassisLive ? 'text-rose-400 font-bold text-sm' : 'text-emerald-400 font-bold text-sm';

    document.getElementById('sim16_val_fuse').textContent = isFuseBlown ? 'MELTED (Overcurrent Break)' : 'Conducting Intact';
    document.getElementById('sim16_val_fuse').className = isFuseBlown ? 'text-rose-400 font-bold text-sm' : 'text-emerald-400 font-bold text-sm';

    document.getElementById('sim16_val_shock').textContent = isChassisLive ? 'FATAL SHOCK RISK!' : 'Safe to Touch';
    document.getElementById('sim16_val_shock').className = isChassisLive ? 'text-rose-400 font-bold text-sm' : 'text-emerald-400 font-bold text-sm';

    const cx = w / 2;
    const cy = h / 2;

    // Metal Appliance (Electric Iron / Heater)
    ctx.fillStyle = isChassisLive ? '#7f1d1d' : '#1e293b';
    ctx.fillRect(cx - 60, cy - 40, 120, 80);
    ctx.strokeStyle = isChassisLive ? '#ef4444' : '#10b981';
    ctx.lineWidth = 3;
    ctx.strokeRect(cx - 60, cy - 40, 120, 80);

    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('Metallic Chassis', cx - 45, cy + 5);

    // Fuse in Live Wire
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(120, cy - 45, 60, 25);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(120, cy - 45, 60, 25);

    ctx.strokeStyle = isFuseBlown ? '#f43f5e' : '#ef4444';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(60, cy - 32);
    ctx.lineTo(120, cy - 32);
    if (!isFuseBlown) {
        ctx.lineTo(180, cy - 32);
    }
    ctx.lineTo(cx - 60, cy - 32);
    ctx.stroke();

    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = isFuseBlown ? '#f43f5e' : '#10b981';
    ctx.fillText(isFuseBlown ? 'Fuse MELTED!' : 'Safety Fuse (Intact)', 105, cy - 52);

    // Earth wire lead
    ctx.strokeStyle = sim16EarthConnected ? '#22c55e' : '#64748b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(cx + 60, cy);
    ctx.lineTo(cx + 140, cy);
    ctx.lineTo(cx + 140, h - 35);
    ctx.stroke();

    // Ground symbol
    ctx.beginPath();
    ctx.moveTo(cx + 120, h - 35); ctx.lineTo(cx + 160, h - 35);
    ctx.moveTo(cx + 128, h - 28); ctx.lineTo(cx + 152, h - 28);
    ctx.moveTo(cx + 135, h - 21); ctx.lineTo(cx + 145, h - 21);
    ctx.stroke();

    ctx.fillStyle = '#22c55e';
    ctx.fillText(sim16EarthConnected ? 'Earth Ground Plate' : 'Earth Disconnected', cx + 100, h - 8);
}

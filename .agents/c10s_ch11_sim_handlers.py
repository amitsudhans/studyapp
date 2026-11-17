# -*- coding: utf-8 -*-
"""Class 10 Science Chapter 11 Simulator JavaScript Handlers"""

SIMULATOR_JS = """
// Chapter 11: Electricity - Simulators Engine

// Global animation timer handles
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
// Simulator 1: Electric Charge & Drift Velocity Studio
// -------------------------------------------------------------
let sim1FieldOn = true;
let sim1Electrons = [];

function sim1ToggleField() {
    sim1FieldOn = !sim1FieldOn;
    const btn = document.getElementById('sim1_btn_toggle');
    if (btn) {
        btn.textContent = sim1FieldOn ? 'Field: ON' : 'Field: OFF';
        btn.className = sim1FieldOn ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold' : 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-medium';
    }
    sim1Update();
}

function sim1Init() {
    sim1Electrons = [];
    for (let i = 0; i < 40; i++) {
        sim1Electrons.push({
            x: 50 + Math.random() * 500,
            y: 70 + Math.random() * 120,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2
        });
    }
    sim1Loop();
}

function sim1Update() {
    const q = parseFloat(document.getElementById('sim1_charge_slider')?.value || 5.0);
    const t = parseFloat(document.getElementById('sim1_time_slider')?.value || 2.0);
    document.getElementById('sim1_charge_txt').textContent = `${q.toFixed(1)} C`;
    document.getElementById('sim1_time_txt').textContent = `${t.toFixed(1)} s`;

    const i = (q / t).toFixed(2);
    document.getElementById('sim1_val_current').textContent = sim1FieldOn ? `${i} A` : '0.00 A';

    const numElectrons = ((q / 1.6e-19) / 1e19).toFixed(2);
    document.getElementById('sim1_val_electrons').textContent = `${numElectrons} × 10¹⁹`;
    document.getElementById('sim1_val_drift').textContent = sim1FieldOn ? 'Right → Left (- to +)' : 'Random Thermal (Net Zero)';
    document.getElementById('sim1_val_conventional').textContent = sim1FieldOn ? 'Left → Right (+ to -)' : 'Zero Net Flow';
}

function sim1Loop() {
    const canvas = document.getElementById('sim1_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Draw cylindrical conductor wire
    const wireX = 60;
    const wireY = 55;
    const wireW = w - 120;
    const wireH = 150;

    // Copper wire body
    const grad = ctx.createLinearGradient(0, wireY, 0, wireY + wireH);
    grad.addColorStop(0, 'rgba(180, 83, 9, 0.25)');
    grad.addColorStop(0.5, 'rgba(217, 119, 6, 0.45)');
    grad.addColorStop(1, 'rgba(180, 83, 9, 0.25)');
    ctx.fillStyle = grad;
    ctx.fillRect(wireX, wireY, wireW, wireH);

    ctx.strokeStyle = '#b45309';
    ctx.lineWidth = 3;
    ctx.strokeRect(wireX, wireY, wireW, wireH);

    // Conductor Terminals (+ on left, - on right)
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(wireX - 15, wireY, 15, wireH);
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('+', wireX - 12, wireY + wireH/2 + 6);

    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(wireX + wireW, wireY, 15, wireH);
    ctx.fillStyle = '#ffffff';
    ctx.fillText('−', wireX + wireW + 3, wireY + wireH/2 + 6);

    // Electric field vectors (arrows pointing left to right)
    if (sim1FieldOn) {
        ctx.strokeStyle = 'rgba(245, 158, 11, 0.35)';
        ctx.fillStyle = 'rgba(245, 158, 11, 0.35)';
        ctx.lineWidth = 2;
        for (let row of [wireY + 30, wireY + 75, wireY + 120]) {
            ctx.beginPath();
            ctx.moveTo(wireX + 30, row);
            ctx.lineTo(wireX + wireW - 30, row);
            ctx.stroke();
            // Arrowhead
            ctx.beginPath();
            ctx.moveTo(wireX + wireW - 25, row);
            ctx.lineTo(wireX + wireW - 35, row - 5);
            ctx.lineTo(wireX + wireW - 35, row + 5);
            ctx.fill();
        }
        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#f59e0b';
        ctx.fillText('Electric Field E →', wireX + 40, wireY + 20);
        ctx.fillStyle = '#10b981';
        ctx.fillText('Conventional Current (I) Direction →', wireX + 180, wireY + 20);
        ctx.fillStyle = '#38bdf8';
        ctx.fillText('← Electron Drift Velocity (v_d)', wireX + wireW - 190, wireY + wireH + 20);
    }

    // Update and draw electron particles
    const driftSpeed = sim1FieldOn ? -1.8 : 0;
    sim1Electrons.forEach(e => {
        e.x += e.vx + driftSpeed;
        e.y += e.vy;

        // Bounce within wire bounds
        if (e.x < wireX + 8) e.x = wireX + wireW - 10;
        if (e.x > wireX + wireW - 8) e.x = wireX + 10;
        if (e.y < wireY + 10 || e.y > wireY + wireH - 10) e.vy = -e.vy;

        // Random jitter
        e.vx += (Math.random() - 0.5) * 0.4;
        e.vy += (Math.random() - 0.5) * 0.4;
        e.vx = Math.max(-2, Math.min(2, e.vx));
        e.vy = Math.max(-2, Math.min(2, e.vy));

        // Draw electron (blue circle with minus)
        ctx.beginPath();
        ctx.arc(e.x, e.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#38bdf8';
        ctx.fill();
        ctx.fillStyle = '#0f172a';
        ctx.font = 'bold 9px Inter, sans-serif';
        ctx.fillText('−', e.x - 3, e.y + 3);
    });

    sim1AnimHandle = requestAnimationFrame(sim1Loop);
}

// -------------------------------------------------------------
// Simulator 2: Circuit & In-Line Ammeter Laboratory
// -------------------------------------------------------------
let sim2KeyClosed = true;

function sim2ToggleKey() {
    sim2KeyClosed = !sim2KeyClosed;
    const btn = document.getElementById('sim2_btn_key');
    if (btn) {
        btn.textContent = sim2KeyClosed ? 'Plug Inserted (Closed)' : 'Key Removed (Open)';
        btn.className = sim2KeyClosed ? 'px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold' : 'px-3 py-1 rounded-lg bg-rose-600 text-white font-bold';
    }
    sim2Update();
}

function sim2Init() {
    sim2Update();
}

function sim2Update() {
    const canvas = document.getElementById('sim2_canvas');
    if (!canvas) return;\n    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const v = parseFloat(document.getElementById('sim2_cell_select')?.value || 3.0);
    const r = parseFloat(document.getElementById('sim2_res_slider')?.value || 10);
    document.getElementById('sim2_res_txt').textContent = `${r} Ω`;

    const i = sim2KeyClosed ? (v / r) : 0;
    const power = (i * i * r).toFixed(2);

    document.getElementById('sim2_val_state').textContent = sim2KeyClosed ? 'Closed & Continuous' : 'Open (Broken Circuit)';
    document.getElementById('sim2_val_ammeter').textContent = `${i.toFixed(3)} A (${(i * 1000).toFixed(0)} mA)`;
    document.getElementById('sim2_val_glow').textContent = sim2KeyClosed ? `${power} W (Glowing)` : '0.0 W (Dark)';

    // Circuit Loop Coordinates
    const x1 = 80, y1 = 40;
    const x2 = w - 80, y2 = h - 40;

    // Draw Wire Loop
    ctx.strokeStyle = sim2KeyClosed ? '#38bdf8' : '#64748b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y1);
    ctx.lineTo(x2, y2);
    ctx.lineTo(x1, y2);
    ctx.closePath();
    ctx.stroke();

    // Top: Battery (Left)
    const batX = 180;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(batX - 25, y1 - 15, 50, 30);
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 4;
    // Long line (+)
    ctx.beginPath();
    ctx.moveTo(batX - 10, y1 - 16);
    ctx.lineTo(batX - 10, y1 + 16);
    ctx.stroke();
    // Short thick line (-)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(batX + 8, y1 - 10);
    ctx.lineTo(batX + 8, y1 + 10);
    ctx.stroke();
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText(`${v} V Battery`, batX - 28, y1 - 22);

    // Top: Plug Key (Right)
    const keyX = 420;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(keyX - 25, y1 - 15, 50, 30);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(keyX - 20, y1 - 10, 40, 20);
    if (sim2KeyClosed) {
        ctx.beginPath();
        ctx.arc(keyX, y1, 5, 0, Math.PI * 2);
        ctx.fillStyle = '#10b981';
        ctx.fill();
        ctx.fillStyle = '#10b981';
        ctx.fillText('Key (•) Closed', keyX - 32, y1 - 18);
    } else {
        ctx.fillStyle = '#f43f5e';
        ctx.fillText('Key ( ) Open', keyX - 28, y1 - 18);
    }

    // Right: Electric Bulb
    const bulbY = (y1 + y2) / 2;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(x2 - 25, bulbY - 25, 50, 50);
    ctx.beginPath();
    ctx.arc(x2, bulbY, 20, 0, Math.PI * 2);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.fillStyle = (sim2KeyClosed && i > 0) ? 'rgba(251, 191, 36, 0.45)' : 'rgba(100, 116, 139, 0.1)';
    ctx.fill();
    ctx.stroke();
    // Filament loop
    ctx.beginPath();
    ctx.arc(x2, bulbY + 5, 8, Math.PI, 0, false);
    ctx.strokeStyle = (sim2KeyClosed && i > 0) ? '#fef08a' : '#94a3b8';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Bulb (${r}Ω)`, x2 - 25, bulbY + 35);

    // Bottom: Ammeter (In Series)
    const ammX = (x1 + x2) / 2;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(ammX - 35, y2 - 35, 70, 70);
    ctx.beginPath();
    ctx.arc(ammX, y2, 28, 0, Math.PI * 2);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fill();
    ctx.stroke();
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('A', ammX - 6, y2 - 4);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`${i.toFixed(2)} A`, ammX - 16, y2 + 14);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Ammeter (Series)', ammX - 42, y2 + 42);

    // Current flow direction arrows if closed
    if (sim2KeyClosed && i > 0) {
        ctx.fillStyle = '#38bdf8';
        // Top wire (conventional left to right)
        ctx.beginPath();
        ctx.moveTo(300, y1);
        ctx.lineTo(290, y1 - 5);
        ctx.lineTo(290, y1 + 5);
        ctx.fill();
        // Right wire (down)
        ctx.beginPath();
        ctx.moveTo(x2, 100);
        ctx.lineTo(x2 - 5, 90);
        ctx.lineTo(x2 + 5, 90);
        ctx.fill();
    }
}

// -------------------------------------------------------------
// Simulator 3: Electric Potential Difference & Voltmeter Studio
// -------------------------------------------------------------
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

    const work = parseFloat(document.getElementById('sim3_work_slider')?.value || 24);
    const q = parseFloat(document.getElementById('sim3_charge_slider')?.value || 2);
    const tap = document.getElementById('sim3_tap_select')?.value || 'parallel';

    document.getElementById('sim3_work_txt').textContent = `${work} J`;
    document.getElementById('sim3_charge_txt').textContent = `${q.toFixed(1)} C`;

    const v = (work / q).toFixed(1);
    document.getElementById('sim3_val_voltage').textContent = `${v} V`;
    document.getElementById('sim3_val_status').textContent = (tap === 'parallel') ? 'Correct Parallel Hookup' : 'Fault: High R Blocks Current';
    document.getElementById('sim3_val_status').className = (tap === 'parallel') ? 'text-emerald-400 font-bold text-sm' : 'text-rose-400 font-bold text-sm';

    // Main circuit wire
    const startX = 60;
    const endX = w - 60;
    const midY = 150;

    // Resistor component between A and B
    const ptA = 220;
    const ptB = 380;

    // Main wire
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(startX, midY);
    ctx.lineTo(ptA, midY);
    ctx.stroke();

    // Resistor zigzag
    ctx.beginPath();
    ctx.moveTo(ptA, midY);
    const numZigs = 6;
    const zigW = (ptB - ptA) / numZigs;
    for (let k = 0; k < numZigs; k++) {
        const zx = ptA + k * zigW + zigW / 2;
        const zy = midY + (k % 2 === 0 ? -15 : 15);
        ctx.lineTo(zx, zy);
    }
    ctx.lineTo(ptB, midY);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.strokeStyle = '#38bdf8';
    ctx.beginPath();
    ctx.moveTo(ptB, midY);
    ctx.lineTo(endX, midY);
    ctx.stroke();

    // Points A and B nodes
    ctx.beginPath();
    ctx.arc(ptA, midY, 6, 0, Math.PI * 2);
    ctx.arc(ptB, midY, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#ef4444';
    ctx.fill();

    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText('Point A', ptA - 20, midY + 24);
    ctx.fillText('Point B', ptB - 20, midY + 24);

    if (tap === 'parallel') {
        // Parallel voltmeter loop arched above
        const vmX = (ptA + ptB) / 2;
        const vmY = 60;

        ctx.strokeStyle = '#a855f7';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(ptA, midY);
        ctx.lineTo(ptA, vmY);
        ctx.lineTo(vmX - 25, vmY);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(ptB, midY);
        ctx.lineTo(ptB, vmY);
        ctx.lineTo(vmX + 25, vmY);
        ctx.stroke();

        // Voltmeter dial
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(vmX - 28, vmY - 28, 56, 56);
        ctx.beginPath();
        ctx.arc(vmX, vmY, 26, 0, Math.PI * 2);
        ctx.strokeStyle = '#a855f7';
        ctx.lineWidth = 2.5;
        ctx.fillStyle = 'rgba(168, 85, 247, 0.15)';
        ctx.fill();
        ctx.stroke();

        ctx.font = 'bold 16px Inter, sans-serif';
        ctx.fillStyle = '#a855f7';
        ctx.fillText('V', vmX - 6, vmY - 3);
        ctx.font = '10px Inter, sans-serif';
        ctx.fillStyle = '#38bdf8';
        ctx.fillText(`${v} V`, vmX - 14, vmY + 14);

        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#10b981';
        ctx.fillText(`Work done W = ${work} J transporting Q = ${q.toFixed(1)} C`, vmX - 120, h - 35);
        ctx.fillText(`Potential Difference V = W / Q = ${v} Volts`, vmX - 100, h - 18);
    } else {
        // Series error warning
        ctx.font = '12px Inter, sans-serif';
        ctx.fillStyle = '#f43f5e';
        ctx.fillText('⚠ ERROR: Voltmeter connected in SERIES! Very high resistance chokes entire current.', 80, 70);
    }
}

// -------------------------------------------------------------
// Simulator 4: Circuit Diagram Symbol Workbench
// -------------------------------------------------------------
const sim4Symbols = [
    'cell', 'battery', 'open_key', 'closed_key', 'wire_joint',
    'wire_cross', 'bulb', 'resistor', 'rheostat', 'ammeter', 'voltmeter'
];

function sim4CycleNext() {
    const sel = document.getElementById('sim4_sym_select');
    if (!sel) return;
    let idx = sim4Symbols.indexOf(sel.value);
    idx = (idx + 1) % sim4Symbols.length;
    sel.value = sim4Symbols[idx];
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

    const sym = document.getElementById('sim4_sym_select')?.value || 'cell';
    const cx = w / 2;
    const cy = h / 2;

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;

    switch(sym) {
        case 'cell':
            document.getElementById('sim4_val_name').textContent = 'Electric Cell';
            document.getElementById('sim4_val_role').textContent = 'Source of electromotive potential';
            document.getElementById('sim4_val_polarity').textContent = 'Long line (+), Short thick line (−)';
            // Leads
            ctx.beginPath();
            ctx.moveTo(cx - 80, cy); ctx.lineTo(cx - 15, cy);
            ctx.moveTo(cx + 15, cy); ctx.lineTo(cx + 80, cy);
            ctx.stroke();
            // Long thin (+)
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(cx - 15, cy - 40); ctx.lineTo(cx - 15, cy + 40);
            ctx.stroke();
            // Short thick (-)
            ctx.strokeStyle = '#38bdf8';
            ctx.lineWidth = 7;
            ctx.beginPath();
            ctx.moveTo(cx + 15, cy - 25); ctx.lineTo(cx + 15, cy + 25);
            ctx.stroke();
            ctx.font = 'bold 14px Inter, sans-serif';
            ctx.fillStyle = '#ef4444'; ctx.fillText('+', cx - 35, cy - 10);
            ctx.fillStyle = '#38bdf8'; ctx.fillText('−', cx + 30, cy - 10);
            break;

        case 'battery':
            document.getElementById('sim4_val_name').textContent = 'Battery (Cells in Series)';
            document.getElementById('sim4_val_role').textContent = 'Multiple cells providing higher cumulative voltage';
            document.getElementById('sim4_val_polarity').textContent = 'Alternating long (+) and short (−) plates';
            ctx.beginPath();
            ctx.moveTo(cx - 110, cy); ctx.lineTo(cx - 60, cy);
            ctx.moveTo(cx + 60, cy); ctx.lineTo(cx + 110, cy);
            ctx.stroke();
            for (let b = 0; b < 3; b++) {
                const bx = cx - 40 + b * 40;
                ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
                ctx.beginPath(); ctx.moveTo(bx - 10, cy - 35); ctx.lineTo(bx - 10, cy + 35); ctx.stroke();
                ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 6;
                ctx.beginPath(); ctx.moveTo(bx + 10, cy - 20); ctx.lineTo(bx + 10, cy + 20); ctx.stroke();
            }
            break;

        case 'open_key':
            document.getElementById('sim4_val_name').textContent = 'Plug Key (Open Switch)';
            document.getElementById('sim4_val_role').textContent = 'Breaks circuit; current ceases to flow';
            document.getElementById('sim4_val_polarity').textContent = 'Parentheses without central dot ( )';
            ctx.beginPath();
            ctx.moveTo(cx - 90, cy); ctx.lineTo(cx - 35, cy);
            ctx.moveTo(cx + 35, cy); ctx.lineTo(cx + 90, cy);
            ctx.stroke();
            ctx.font = '36px Inter, sans-serif';
            ctx.fillStyle = '#f43f5e';
            ctx.fillText('(   )', cx - 25, cy + 12);
            break;

        case 'closed_key':
            document.getElementById('sim4_val_name').textContent = 'Plug Key (Closed Switch)';
            document.getElementById('sim4_val_role').textContent = 'Completes circuit; enables continuous current';
            document.getElementById('sim4_val_polarity').textContent = 'Parentheses with central plug dot ( • )';
            ctx.beginPath();
            ctx.moveTo(cx - 90, cy); ctx.lineTo(cx - 35, cy);
            ctx.moveTo(cx + 35, cy); ctx.lineTo(cx + 90, cy);
            ctx.stroke();
            ctx.font = '36px Inter, sans-serif';
            ctx.fillStyle = '#10b981';
            ctx.fillText('( • )', cx - 28, cy + 12);
            break;

        case 'wire_joint':
            document.getElementById('sim4_val_name').textContent = 'A Wire Joint';
            document.getElementById('sim4_val_role').textContent = 'Electrical T-junction branching current';
            document.getElementById('sim4_val_polarity').textContent = 'Solid filled contact dot at intersection';
            ctx.beginPath();
            ctx.moveTo(cx - 100, cy); ctx.lineTo(cx + 100, cy);
            ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - 70);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(cx, cy, 7, 0, Math.PI * 2);
            ctx.fillStyle = '#10b981';
            ctx.fill();
            break;

        case 'wire_cross':
            document.getElementById('sim4_val_name').textContent = 'Wire Crossing without Joint';
            document.getElementById('sim4_val_role').textContent = 'Two insulated conductors crossing without contact';
            document.getElementById('sim4_val_polarity').textContent = 'Semicircular bridge jumping over wire';
            ctx.beginPath();
            ctx.moveTo(cx - 100, cy); ctx.lineTo(cx + 100, cy);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(cx, cy - 70); ctx.lineTo(cx, cy - 16);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(cx, cy, 16, -Math.PI/2, Math.PI/2, true);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(cx, cy + 16); ctx.lineTo(cx, cy + 70);
            ctx.stroke();
            break;

        case 'bulb':
            document.getElementById('sim4_val_name').textContent = 'Electric Bulb';
            document.getElementById('sim4_val_role').textContent = 'Converts electrical energy to light and heat';
            document.getElementById('sim4_val_polarity').textContent = 'Loop / curly filament inside circle';
            ctx.beginPath();
            ctx.moveTo(cx - 90, cy); ctx.lineTo(cx - 30, cy);
            ctx.moveTo(cx + 30, cy); ctx.lineTo(cx + 90, cy);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(cx, cy, 30, 0, Math.PI * 2);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(cx - 8, cy, 12, Math.PI, 0, false);
            ctx.arc(cx + 8, cy, 12, Math.PI, 0, false);
            ctx.strokeStyle = '#f59e0b';
            ctx.stroke();
            break;

        case 'resistor':
            document.getElementById('sim4_val_name').textContent = 'Fixed Resistor';
            document.getElementById('sim4_val_role').textContent = 'Provides constant, calibrated electrical resistance';
            document.getElementById('sim4_val_polarity').textContent = 'Symmetrical zigzag teeth line';
            ctx.beginPath();
            ctx.moveTo(cx - 100, cy); ctx.lineTo(cx - 50, cy);
            for (let i = 0; i < 5; i++) {
                ctx.lineTo(cx - 40 + i * 20, cy + (i % 2 === 0 ? -20 : 20));
            }
            ctx.lineTo(cx + 50, cy);
            ctx.lineTo(cx + 100, cy);
            ctx.strokeStyle = '#f59e0b';
            ctx.stroke();
            break;

        case 'rheostat':
            document.getElementById('sim4_val_name').textContent = 'Rheostat (Variable Resistor)';
            document.getElementById('sim4_val_role').textContent = 'Regulates current magnitude without changing voltage';
            document.getElementById('sim4_val_polarity').textContent = 'Zigzag line with diagonal slider arrow';
            ctx.beginPath();
            ctx.moveTo(cx - 100, cy); ctx.lineTo(cx - 50, cy);
            for (let i = 0; i < 5; i++) {
                ctx.lineTo(cx - 40 + i * 20, cy + (i % 2 === 0 ? -20 : 20));
            }
            ctx.lineTo(cx + 50, cy); ctx.lineTo(cx + 100, cy);
            ctx.strokeStyle = '#f59e0b';
            ctx.stroke();
            // Diagonal Arrow
            ctx.strokeStyle = '#38bdf8';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(cx - 30, cy + 40); ctx.lineTo(cx + 30, cy - 40);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(cx + 35, cy - 45); ctx.lineTo(cx + 20, cy - 40); ctx.lineTo(cx + 28, cy - 25);
            ctx.fillStyle = '#38bdf8'; ctx.fill();
            break;

        case 'ammeter':
            document.getElementById('sim4_val_name').textContent = 'Ammeter (Current Gauge)';
            document.getElementById('sim4_val_role').textContent = 'Measures electric current; connected in series';
            document.getElementById('sim4_val_polarity').textContent = 'Circle with "A", + and − terminals';
            ctx.beginPath();
            ctx.moveTo(cx - 90, cy); ctx.lineTo(cx - 30, cy);
            ctx.moveTo(cx + 30, cy); ctx.lineTo(cx + 90, cy);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(cx, cy, 30, 0, Math.PI * 2);
            ctx.stroke();
            ctx.font = 'bold 24px Inter, sans-serif';
            ctx.fillStyle = '#38bdf8';
            ctx.fillText('A', cx - 8, cy + 8);
            ctx.font = '12px Inter, sans-serif';
            ctx.fillStyle = '#ef4444'; ctx.fillText('+', cx - 45, cy - 10);
            ctx.fillStyle = '#38bdf8'; ctx.fillText('−', cx + 35, cy - 10);
            break;

        case 'voltmeter':
            document.getElementById('sim4_val_name').textContent = 'Voltmeter (Potential Gauge)';
            document.getElementById('sim4_val_role').textContent = 'Measures potential difference; connected in parallel';
            document.getElementById('sim4_val_polarity').textContent = 'Circle with "V", + and − terminals';
            ctx.beginPath();
            ctx.moveTo(cx - 90, cy); ctx.lineTo(cx - 30, cy);
            ctx.moveTo(cx + 30, cy); ctx.lineTo(cx + 90, cy);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(cx, cy, 30, 0, Math.PI * 2);
            ctx.stroke();
            ctx.font = 'bold 24px Inter, sans-serif';
            ctx.fillStyle = '#a855f7';
            ctx.fillText('V', cx - 8, cy + 8);
            ctx.font = '12px Inter, sans-serif';
            ctx.fillStyle = '#ef4444'; ctx.fillText('+', cx - 45, cy - 10);
            ctx.fillStyle = '#38bdf8'; ctx.fillText('−', cx + 35, cy - 10);
            break;
    }
}

// -------------------------------------------------------------
// Simulator 5: Ohm's Law Activity 11.1 Verification
// -------------------------------------------------------------
let sim5Cells = 1;

function sim5SetCells(c) {
    sim5Cells = c;
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`sim5_btn_c${i}`);
        if (btn) {
            btn.className = (i === c) ? 'px-2.5 py-0.5 rounded text-xs bg-amber-600 text-slate-950 font-bold' : 'px-2.5 py-0.5 rounded text-xs text-slate-300';
        }
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

    const r = parseFloat(document.getElementById('sim5_res_slider')?.value || 10);
    document.getElementById('sim5_res_txt').textContent = `${r} Ω`;

    const v = sim5Cells * 1.5;
    const i = v / r;

    document.getElementById('sim5_val_voltage').textContent = `${v.toFixed(2)} V`;
    document.getElementById('sim5_val_current').textContent = `${i.toFixed(2)} A`;
    document.getElementById('sim5_val_ratio').textContent = `${(v / i).toFixed(2)} Ω`;

    // Circuit layout
    const x1 = 90, y1 = 45;
    const x2 = w - 90, y2 = h - 45;

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);

    // Top: Battery bank
    for (let c = 0; c < sim5Cells; c++) {
        const bx = 160 + c * 40;
        ctx.fillStyle = '#ef4444'; ctx.fillRect(bx - 6, y1 - 15, 3, 30);
        ctx.fillStyle = '#38bdf8'; ctx.fillRect(bx + 6, y1 - 10, 6, 20);
    }
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText(`${sim5Cells} × 1.5V = ${v.toFixed(1)}V`, 150, y1 - 22);

    // Bottom: Nichrome wire XY
    const nx1 = 200;
    const nx2 = 380;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(nx1, y2 - 10, nx2 - nx1, 20);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(nx1, y2);
    ctx.lineTo(nx2, y2);
    ctx.stroke();

    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444'; ctx.fillText('X', nx1 - 15, y2 + 5);
    ctx.fillStyle = '#38bdf8'; ctx.fillText('Y', nx2 + 8, y2 + 5);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Nichrome Wire (${r}Ω)`, 240, y2 + 25);

    // Voltmeter across XY
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(nx1, y2); ctx.lineTo(nx1, y2 - 50); ctx.lineTo(260, y2 - 50);
    ctx.moveTo(nx2, y2); ctx.lineTo(nx2, y2 - 50); ctx.lineTo(320, y2 - 50);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(290, y2 - 50, 20, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.stroke();
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('V', 285, y2 - 46);

    // Ammeter on right leg
    ctx.beginPath();
    ctx.arc(x2, (y1 + y2)/2, 20, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('A', x2 - 5, (y1 + y2)/2 + 4);
}

// -------------------------------------------------------------
// Simulator 6: V-I Characteristic Graph & Slope Studio
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

    const wireType = document.getElementById('sim6_wire_select')?.value || 'iron';
    const v = parseFloat(document.getElementById('sim6_v_slider')?.value || 6.0);
    document.getElementById('sim6_v_txt').textContent = `${v.toFixed(1)} V`;

    let r = 10;
    if (wireType === 'copper') r = 2;
    else if (wireType === 'nichrome') r = 25;

    const i = v / r;
    document.getElementById('sim6_val_v').textContent = `${v.toFixed(1)} V`;
    document.getElementById('sim6_val_i').textContent = `${i.toFixed(2)} A`;
    document.getElementById('sim6_val_slope').textContent = `${r.toFixed(1)} Ω`;

    // Draw V-I Cartesian axes
    const ox = 70;
    const oy = h - 45;
    const gw = w - 120;
    const gh = h - 80;

    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(ox, oy); ctx.lineTo(ox + gw, oy); // X-axis (Current I)
    ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - gh); // Y-axis (Potential V)
    ctx.stroke();

    // Axis labels
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('Current I (Amperes) →', ox + gw - 120, oy + 30);
    ctx.save();
    ctx.translate(ox - 35, oy - gh + 70);
    ctx.rotate(-Math.PI/2);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Potential V (Volts) →', 0, 0);
    ctx.restore();

    // Max scales: V_max = 12V, I_max = 6A
    const vMax = 12.0;
    const iMax = 6.0;

    // Grid marks
    ctx.strokeStyle = 'rgba(100, 116, 139, 0.2)';
    ctx.setLineDash([3, 3]);
    for (let k = 1; k <= 5; k++) {
        // Vertical grid lines
        const gx = ox + (k / 5) * (gw - 20);
        ctx.beginPath(); ctx.moveTo(gx, oy); ctx.lineTo(gx, oy - gh); ctx.stroke();
        // Horizontal grid lines
        const gy = oy - (k / 5) * (gh - 10);
        ctx.beginPath(); ctx.moveTo(ox, gy); ctx.lineTo(ox + gw, gy); ctx.stroke();
    }
    ctx.setLineDash([]);

    // Plot theoretical straight line: V = I * R => y = (V/vMax)*gh, x = (I/iMax)*gw
    const endI = Math.min(iMax, vMax / r);
    const endV = endI * r;
    const plotX = ox + (endI / iMax) * (gw - 20);
    const plotY = oy - (endV / vMax) * (gh - 10);

    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(ox, oy);
    ctx.lineTo(plotX, plotY);
    ctx.stroke();

    // Current operating point
    const currX = ox + (i / iMax) * (gw - 20);
    const currY = oy - (v / vMax) * (gh - 10);

    ctx.beginPath();
    ctx.arc(currX, currY, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#ef4444';
    ctx.fill();

    // Slope triangle (ΔV / ΔI)
    ctx.strokeStyle = 'rgba(239, 68, 68, 0.6)';
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(currX, currY);
    ctx.lineTo(currX, oy);
    ctx.lineTo(ox, oy);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText(`Slope = ΔV / ΔI = R = ${r} Ω (Ohmic)`, plotX - 110, plotY - 10);
}

// -------------------------------------------------------------
// Simulator 7: Resistance Geometric Factors (l, A, Material)
// -------------------------------------------------------------
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

    const mat = document.getElementById('sim7_mat_select')?.value || 'nichrome';
    const len = parseFloat(document.getElementById('sim7_len_slider')?.value || 1.0);
    const area = parseFloat(document.getElementById('sim7_area_slider')?.value || 0.5);

    document.getElementById('sim7_len_txt').textContent = `${len.toFixed(1)} m`;
    document.getElementById('sim7_area_txt').textContent = `${area.toFixed(1)} mm²`;

    // ρ in 10^-8 Ω·m
    let rho = 100.0;
    if (mat === 'copper') rho = 1.62;
    else if (mat === 'aluminium') rho = 2.63;
    else if (mat === 'iron') rho = 10.0;

    // R = rho * l / A (scaled for demonstration)
    const r = (rho * len / (area * 25)).toFixed(2);
    const i = (3.0 / Math.max(0.1, r)).toFixed(2);

    document.getElementById('sim7_val_r').textContent = `${r} Ω`;
    document.getElementById('sim7_val_current').textContent = `${i} A`;

    // Draw Wire visualization with length and area
    const startX = 60;
    const centerY = h / 2;
    const wireLengthPx = 60 + len * 70;
    const wireThicknessPx = 10 + area * 24;

    // Conductor cylinder
    const grad = ctx.createLinearGradient(0, centerY - wireThicknessPx/2, 0, centerY + wireThicknessPx/2);
    if (mat === 'copper') {
        grad.addColorStop(0, '#b45309'); grad.addColorStop(0.5, '#f59e0b'); grad.addColorStop(1, '#b45309');
    } else if (mat === 'aluminium') {
        grad.addColorStop(0, '#64748b'); grad.addColorStop(0.5, '#cbd5e1'); grad.addColorStop(1, '#64748b');
    } else if (mat === 'iron') {
        grad.addColorStop(0, '#334155'); grad.addColorStop(0.5, '#94a3b8'); grad.addColorStop(1, '#334155');
    } else {
        grad.addColorStop(0, '#78350f'); grad.addColorStop(0.5, '#d97706'); grad.addColorStop(1, '#78350f');
    }

    ctx.fillStyle = grad;
    ctx.fillRect(startX, centerY - wireThicknessPx/2, wireLengthPx, wireThicknessPx);
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(startX, centerY - wireThicknessPx/2, wireLengthPx, wireThicknessPx);

    // Cross-section ellipse at end
    ctx.beginPath();
    ctx.ellipse(startX + wireLengthPx, centerY, 8, wireThicknessPx/2, 0, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.stroke();

    // Dimensional arrows
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Length l = ${len.toFixed(1)} m`, startX + wireLengthPx / 2 - 40, centerY - wireThicknessPx/2 - 15);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Area A = ${area.toFixed(1)} mm²`, startX + wireLengthPx + 15, centerY + 4);

    ctx.fillStyle = '#10b981';
    ctx.fillText(`R = ρ · (l / A) = ${r} Ω`, startX, h - 25);
}

// -------------------------------------------------------------
// Simulator 8: Electrical Resistivity Spectrum Analyzer
// -------------------------------------------------------------
let sim8Category = 'conductor';
let sim8HeatOn = true;

function sim8SetCat(cat) {
    sim8Category = cat;
    for (let c of ['conductor', 'alloy', 'insulator']) {
        const btn = document.getElementById(`sim8_btn_${c === 'conductor' ? 'cat1' : c === 'alloy' ? 'cat2' : 'cat3'}`);
        if (btn) {
            btn.className = (c === cat) ? 'px-2.5 py-0.5 rounded text-xs bg-amber-600 text-slate-950 font-bold' : 'px-2.5 py-0.5 rounded text-xs text-slate-300';
        }
    }
    sim8Update();
}

function sim8ToggleHeat() {
    sim8HeatOn = !sim8HeatOn;
    const btn = document.getElementById('sim8_btn_heat');
    if (btn) {
        btn.textContent = sim8HeatOn ? 'Oxidation Stress: ON' : 'Oxidation Stress: OFF';
        btn.className = sim8HeatOn ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold' : 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-medium';
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

    if (sim8Category === 'conductor') {
        document.getElementById('sim8_val_range').textContent = '1.6 × 10⁻⁸ to 10 × 10⁻⁸ Ω·m';
        document.getElementById('sim8_val_oxid').textContent = 'Oxidizes at high temp';
        document.getElementById('sim8_val_app').textContent = 'Transmission Cables (Cu, Al)';
    } else if (sim8Category === 'alloy') {
        document.getElementById('sim8_val_range').textContent = '44 × 10⁻⁸ to 100 × 10⁻⁸ Ω·m';
        document.getElementById('sim8_val_oxid').textContent = 'Does NOT oxidize / burn easily';
        document.getElementById('sim8_val_app').textContent = 'Heating Elements (Nichrome)';
    } else {
        document.getElementById('sim8_val_range').textContent = '10¹² to 10¹⁷ Ω·m';
        document.getElementById('sim8_val_oxid').textContent = 'Zero Conduction (Breakdown)';
        document.getElementById('sim8_val_app').textContent = 'Safety Insulation (Glass, Rubber)';
    }

    // Draw logarithmic spectrum bar
    const barX = 60;
    const barY = 80;
    const barW = w - 120;
    const barH = 50;

    const grad = ctx.createLinearGradient(barX, 0, barX + barW, 0);
    grad.addColorStop(0, '#10b981');    // Conductors
    grad.addColorStop(0.35, '#f59e0b'); // Alloys
    grad.addColorStop(0.8, '#ef4444');  // Insulators
    ctx.fillStyle = grad;
    ctx.fillRect(barX, barY, barW, barH);
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 2;
    ctx.strokeRect(barX, barY, barW, barH);

    // Labels across spectrum
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('Conductors (10⁻⁸)', barX + 10, barY + 30);
    ctx.fillText('Alloys (10⁻⁶)', barX + barW * 0.35, barY + 30);
    ctx.fillText('Insulators (10¹² to 10¹⁷ Ω·m)', barX + barW * 0.65, barY + 30);

    // Indicator pointer for current selection
    let pointerX = barX + 50;
    if (sim8Category === 'alloy') pointerX = barX + barW * 0.42;
    else if (sim8Category === 'insulator') pointerX = barX + barW * 0.85;

    ctx.beginPath();
    ctx.moveTo(pointerX, barY + barH + 5);
    ctx.lineTo(pointerX - 10, barY + barH + 20);
    ctx.lineTo(pointerX + 10, barY + barH + 20);
    ctx.closePath();
    ctx.fillStyle = '#38bdf8';
    ctx.fill();

    // Heating element illustration
    ctx.font = '12px Inter, sans-serif';
    if (sim8Category === 'alloy' && sim8HeatOn) {
        ctx.fillStyle = '#fbbf24';
        ctx.fillText('🔥 Nichrome ribbon at red heat (~800°C): Maintains structural integrity without burning!', barX, h - 35);
    } else {
        ctx.fillStyle = '#94a3b8';
        ctx.fillText('Select category and toggle heating test to examine oxidation stability.', barX, h - 35);
    }
}

// -------------------------------------------------------------
// Simulator 9: Series Resistors & Ammeter Position Lab
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

    const pos = document.getElementById('sim9_pos_select')?.value || 'between_r1_r2';
    const v = parseFloat(document.getElementById('sim9_v_slider')?.value || 6);
    document.getElementById('sim9_v_txt').textContent = `${v} V`;

    const r1 = 2, r2 = 4, r3 = 6;
    const rs = r1 + r2 + r3;
    const i = v / rs;

    document.getElementById('sim9_val_i').textContent = `${i.toFixed(3)} A`;
    document.getElementById('sim9_val_rtot').textContent = `${rs.toFixed(1)} Ω (2+4+6)`;

    // Series loop coordinates
    const x1 = 80, y1 = 50;
    const x2 = w - 80, y2 = h - 50;

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);

    // Top: Battery
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(w/2 - 30, y1 - 15, 60, 30);
    ctx.fillStyle = '#ef4444'; ctx.fillRect(w/2 - 10, y1 - 15, 3, 30);
    ctx.fillStyle = '#38bdf8'; ctx.fillRect(w/2 + 6, y1 - 10, 6, 20);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText(`${v}V Battery`, w/2 - 25, y1 - 22);

    // Bottom wire: 3 Series Resistors R1, R2, R3
    const rx1 = 150, rx2 = 280, rx3 = 410;
    const rW = 70;

    // Resistor 1
    ctx.fillStyle = '#0f172a'; ctx.fillRect(rx1, y2 - 10, rW, 20);
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3;
    ctx.strokeRect(rx1, y2 - 8, rW, 16);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b'; ctx.fillText('R1 = 2Ω', rx1 + 15, y2 + 4);

    // Resistor 2
    ctx.fillStyle = '#0f172a'; ctx.fillRect(rx2, y2 - 10, rW, 20);
    ctx.strokeRect(rx2, y2 - 8, rW, 16);
    ctx.fillText('R2 = 4Ω', rx2 + 15, y2 + 4);

    // Resistor 3
    ctx.fillStyle = '#0f172a'; ctx.fillRect(rx3, y2 - 10, rW, 20);
    ctx.strokeRect(rx3, y2 - 8, rW, 16);
    ctx.fillText('R3 = 6Ω', rx3 + 15, y2 + 4);

    // Ammeter placement based on selection
    let ax = x1;
    let ay = (y1 + y2) / 2;
    if (pos === 'before_r1') { ax = 115; ay = y2; }
    else if (pos === 'between_r1_r2') { ax = (rx1 + rW + rx2) / 2; ay = y2; }
    else if (pos === 'between_r2_r3') { ax = (rx2 + rW + rx3) / 2; ay = y2; }
    else if (pos === 'after_r3') { ax = x2; ay = (y1 + y2) / 2; }

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(ax - 20, ay - 20, 40, 40);
    ctx.beginPath();
    ctx.arc(ax, ay, 18, 0, Math.PI * 2);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('A', ax - 4, ay - 2);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillText(`${i.toFixed(2)}A`, ax - 12, ay + 10);
}

// -------------------------------------------------------------
// Simulator 10: Series Circuit Analysis & Voltage Drops
// -------------------------------------------------------------
let sim10Preset = 'three_r';

function sim10UpdatePreset() {
    sim10Preset = document.getElementById('sim10_preset_select')?.value || 'three_r';
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

    const probe = document.getElementById('sim10_probe_select')?.value || 'total';

    let vTot = 10.0;
    let r1 = 2.0, r2 = 3.0, r3 = 5.0;

    if (sim10Preset === 'ex11_7') {
        vTot = 6.0;
        r1 = 20.0; // lamp
        r2 = 4.0;  // conductor
        r3 = 0.0;
    }

    const rs = r1 + r2 + r3;
    const i = vTot / rs;
    const v1 = i * r1;
    const v2 = i * r2;
    const v3 = i * r3;

    document.getElementById('sim10_val_rs').textContent = `${rs.toFixed(1)} Ω`;
    document.getElementById('sim10_val_i').textContent = `${i.toFixed(2)} A`;

    let vProbeVal = vTot;
    if (probe === 'v1') vProbeVal = v1;
    else if (probe === 'v2') vProbeVal = v2;
    else if (probe === 'v3') vProbeVal = v3;

    document.getElementById('sim10_val_vprobe').textContent = `${vProbeVal.toFixed(2)} V`;

    // Circuit layout
    const x1 = 80, y1 = 45;
    const x2 = w - 80, y2 = h - 45;

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);

    // Top: Battery
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText(`${vTot.toFixed(1)} V Supply`, w/2 - 35, y1 - 15);

    // Bottom Resistors
    const rx1 = 160, rx2 = 280, rx3 = 400;
    const rw = 75;

    // Resistor 1
    ctx.fillStyle = '#0f172a'; ctx.fillRect(rx1, y2 - 12, rw, 24);
    ctx.strokeStyle = '#f59e0b'; ctx.strokeRect(rx1, y2 - 10, rw, 20);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(sim10Preset === 'ex11_7' ? 'Lamp 20Ω' : 'R1 = 2Ω', rx1 + 10, y2 + 4);

    // Resistor 2
    ctx.fillStyle = '#0f172a'; ctx.fillRect(rx2, y2 - 12, rw, 24);
    ctx.strokeRect(rx2, y2 - 10, rw, 20);
    ctx.fillText(sim10Preset === 'ex11_7' ? 'Wire 4Ω' : 'R2 = 3Ω', rx2 + 10, y2 + 4);

    if (sim10Preset !== 'ex11_7') {
        // Resistor 3
        ctx.fillStyle = '#0f172a'; ctx.fillRect(rx3, y2 - 12, rw, 24);
        ctx.strokeRect(rx3, y2 - 10, rw, 20);
        ctx.fillText('R3 = 5Ω', rx3 + 10, y2 + 4);
    }

    // Voltmeter Probes based on probe selection
    let pxA = rx1, pxB = rx1 + rw;
    if (probe === 'total') { pxA = rx1; pxB = (sim10Preset === 'ex11_7') ? rx2 + rw : rx3 + rw; }
    else if (probe === 'v1') { pxA = rx1; pxB = rx1 + rw; }
    else if (probe === 'v2') { pxA = rx2; pxB = rx2 + rw; }
    else if (probe === 'v3') { pxA = rx3; pxB = rx3 + rw; }

    const vmX = (pxA + pxB) / 2;
    const vmY = y2 - 60;

    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(pxA, y2); ctx.lineTo(pxA, vmY); ctx.lineTo(vmX - 20, vmY);
    ctx.moveTo(pxB, y2); ctx.lineTo(pxB, vmY); ctx.lineTo(vmX + 20, vmY);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(vmX, vmY, 18, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a'; ctx.fill(); ctx.stroke();
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('V', vmX - 4, vmY - 2);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillText(`${vProbeVal.toFixed(1)}V`, vmX - 11, vmY + 10);
}

// -------------------------------------------------------------
// Simulator 11: Parallel Resistor Network & Current Branching
// -------------------------------------------------------------
let sim11Branches = [true, true, true];

function sim11ToggleBranch(b) {
    sim11Branches[b - 1] = !sim11Branches[b - 1];
    const btn = document.getElementById(`sim11_btn_b${b}`);
    if (btn) {
        btn.textContent = `R${b}: ${sim11Branches[b - 1] ? 'ON' : 'OFF'}`;
        btn.className = sim11Branches[b - 1] ? 'px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold' : 'px-2 py-0.5 rounded bg-rose-700 text-white text-[11px] font-bold';
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

    const v = parseFloat(document.getElementById('sim11_v_slider')?.value || 12);
    document.getElementById('sim11_v_txt').textContent = `${v} V`;

    const r1 = 6.0, r2 = 12.0, r3 = 20.0;
    const i1 = sim11Branches[0] ? (v / r1) : 0;
    const i2 = sim11Branches[1] ? (v / r2) : 0;
    const i3 = sim11Branches[2] ? (v / r3) : 0;
    const iTot = i1 + i2 + i3;

    // Equivalent Rp
    let invRp = 0;
    if (sim11Branches[0]) invRp += 1 / r1;
    if (sim11Branches[1]) invRp += 1 / r2;
    if (sim11Branches[2]) invRp += 1 / r3;
    const rp = invRp > 0 ? (1 / invRp) : 0;

    document.getElementById('sim11_val_rp').textContent = rp > 0 ? `${rp.toFixed(2)} Ω` : '∞ (All OFF)';
    document.getElementById('sim11_val_itot').textContent = `${iTot.toFixed(2)} A`;
    document.getElementById('sim11_val_ibranches').textContent = `${i1.toFixed(1)}A, ${i2.toFixed(1)}A, ${i3.toFixed(1)}A`;
    document.getElementById('sim11_val_vbranch').textContent = `Uniform ${v.toFixed(1)} V`;

    // Circuit with 3 vertical branches
    const leftX = 140;
    const rightX = w - 140;
    const topY = 40;
    const bottomY = h - 40;

    // Main bus rails
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(60, topY, w - 120, bottomY - topY);

    // 3 parallel branches
    const branchYs = [75, 130, 185];
    const rs = [r1, r2, r3];

    for (let b = 0; b < 3; b++) {
        const by = branchYs[b];
        ctx.strokeStyle = sim11Branches[b] ? '#38bdf8' : '#64748b';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(leftX, by); ctx.lineTo(rightX, by);
        ctx.stroke();

        // Resistor box in branch
        const rx = (leftX + rightX) / 2 - 35;
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(rx, by - 12, 70, 24);
        ctx.strokeStyle = '#f59e0b';
        ctx.strokeRect(rx, by - 10, 70, 20);

        ctx.font = '10px Inter, sans-serif';
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`R${b+1}=${rs[b]}Ω`, rx + 12, by + 4);

        // Branch Current label
        const cur = (b === 0 ? i1 : b === 1 ? i2 : i3);
        ctx.fillStyle = sim11Branches[b] ? '#10b981' : '#f43f5e';
        ctx.fillText(`I${b+1} = ${cur.toFixed(2)} A`, rightX + 10, by + 4);
    }

    // Bus current
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Total Bus Current I = ${iTot.toFixed(2)} A`, 70, topY - 12);
}

// -------------------------------------------------------------
// Simulator 12: Domestic Parallel vs Series Wiring Lab
// -------------------------------------------------------------
let sim12Topology = 'parallel';
let sim12Bulb1Blown = false;

function sim12SetTopology(t) {
    sim12Topology = t;
    const btnP = document.getElementById('sim12_btn_parallel');
    const btnS = document.getElementById('sim12_btn_series');
    if (t === 'parallel') {
        if (btnP) btnP.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnS) btnS.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim12_val_voltstatus').textContent = 'Each gets full 220 V';
    } else {
        if (btnS) btnS.className = 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold';
        if (btnP) btnP.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium';
        document.getElementById('sim12_val_voltstatus').textContent = 'Divided voltage (Loads underpowered)';
    }
    sim12Update();
}

function sim12ToggleFault() {
    sim12Bulb1Blown = !sim12Bulb1Blown;
    const btn = document.getElementById('sim12_btn_fault');
    if (btn) {
        btn.textContent = sim12Bulb1Blown ? 'Restore Bulb 1' : 'Blow Bulb 1';
        btn.className = sim12Bulb1Blown ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold' : 'px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold';
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

    const app1Ok = !sim12Bulb1Blown;
    const app2Ok = (sim12Topology === 'parallel') ? true : app1Ok;
    const app3Ok = (sim12Topology === 'parallel') ? true : app1Ok;

    document.getElementById('sim12_val_app1').textContent = app1Ok ? 'Operating Normal (50W)' : 'BLOWN / FAULTY (Open)';
    document.getElementById('sim12_val_app1').className = app1Ok ? 'text-amber-400 font-bold text-sm' : 'text-rose-400 font-bold text-sm';
    document.getElementById('sim12_val_app2').textContent = app2Ok ? 'Operating Normal (75W)' : 'STOPPED (Series break)';
    document.getElementById('sim12_val_app2').className = app2Ok ? 'text-teal-400 font-bold text-sm' : 'text-rose-400 font-bold text-sm';
    document.getElementById('sim12_val_app3').textContent = app3Ok ? 'Operating Normal (1500W)' : 'STOPPED (Series break)';
    document.getElementById('sim12_val_app3').className = app3Ok ? 'text-cyan-400 font-bold text-sm' : 'text-rose-400 font-bold text-sm';

    // Visual schematic
    const cx = w / 2;
    ctx.font = '12px Inter, sans-serif';

    if (sim12Topology === 'parallel') {
        // Parallel bus bars
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(100, 45); ctx.lineTo(w - 100, 45);
        ctx.moveTo(100, h - 45); ctx.lineTo(w - 100, h - 45);
        ctx.stroke();

        const xPos = [160, cx, w - 160];
        const names = ['Bulb (50W)', 'Ceiling Fan (75W)', 'Heater (1500W)'];
        const states = [app1Ok, app2Ok, app3Ok];

        for (let i = 0; i < 3; i++) {
            const xp = xPos[i];
            ctx.strokeStyle = states[i] ? '#38bdf8' : '#64748b';
            ctx.beginPath();
            ctx.moveTo(xp, 45); ctx.lineTo(xp, h - 45);
            ctx.stroke();

            // Appliance circle
            ctx.beginPath();
            ctx.arc(xp, h/2, 24, 0, Math.PI * 2);
            ctx.fillStyle = states[i] ? '#0f172a' : '#1e293b';
            ctx.fill();
            ctx.strokeStyle = states[i] ? '#10b981' : '#f43f5e';
            ctx.lineWidth = 2.5;
            ctx.stroke();

            ctx.fillStyle = states[i] ? '#10b981' : '#f43f5e';
            ctx.font = '10px Inter, sans-serif';
            ctx.fillText(names[i], xp - 35, h/2 + 40);
            ctx.fillText(states[i] ? '220 V (Active)' : 'DISCONNECTED', xp - 32, h/2 - 32);
        }
    } else {
        // Series single loop
        ctx.strokeStyle = (app1Ok && app2Ok && app3Ok) ? '#38bdf8' : '#64748b';
        ctx.lineWidth = 3;
        ctx.strokeRect(100, 50, w - 200, h - 100);

        const xPos = [180, cx, w - 180];
        const names = ['Bulb 1', 'Bulb 2', 'Bulb 3'];
        const states = [app1Ok, app2Ok, app3Ok];

        for (let i = 0; i < 3; i++) {
            const xp = xPos[i];
            ctx.fillStyle = '#0f172a';
            ctx.fillRect(xp - 25, h - 65, 50, 30);
            ctx.beginPath();
            ctx.arc(xp, h - 50, 18, 0, Math.PI * 2);
            ctx.fillStyle = states[i] ? '#10b981' : '#f43f5e';
            ctx.strokeStyle = '#f8fafc';
            ctx.fill(); ctx.stroke();
            ctx.font = '10px Inter, sans-serif';
            ctx.fillText(names[i], xp - 15, h - 20);
        }
    }
}

// -------------------------------------------------------------
// Simulator 13: Joule's Heating Law Calorimeter Studio
// -------------------------------------------------------------
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

    const i = parseFloat(document.getElementById('sim13_i_slider')?.value || 2.0);
    const r = parseFloat(document.getElementById('sim13_r_slider')?.value || 10.0);
    const t = parseFloat(document.getElementById('sim13_t_slider')?.value || 20.0);

    document.getElementById('sim13_i_txt').textContent = `${i.toFixed(1)} A`;
    document.getElementById('sim13_r_txt').textContent = `${r.toFixed(0)} Ω`;
    document.getElementById('sim13_t_txt').textContent = `${t.toFixed(0)} s`;

    // H = I^2 * R * t
    const power = i * i * r;
    const heatJ = power * t;
    // Assume 50g water (c = 4.18 J/g K), dT = H / (m * c)
    const deltaT = (heatJ / (50 * 4.184)).toFixed(1);

    document.getElementById('sim13_val_heat').textContent = `${heatJ.toFixed(0)} J (${(heatJ / 1000).toFixed(2)} kJ)`;
    document.getElementById('sim13_val_temp').textContent = `+${deltaT} °C`;
    document.getElementById('sim13_val_power').textContent = `${power.toFixed(1)} W (J/s)`;

    // Draw Calorimeter vessel
    const calX = w / 2 - 80;
    const calY = 45;
    const calW = 160;
    const calH = 160;

    // Outer insulated vessel
    ctx.fillStyle = '#334155';
    ctx.fillRect(calX - 10, calY - 5, calW + 20, calH + 10);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(calX - 10, calY - 5, calW + 20, calH + 10);

    // Inner water container
    const waterLevel = Math.min(calH - 20, 100 + parseFloat(deltaT) * 1.5);
    ctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
    ctx.fillRect(calX, calY + calH - waterLevel, calW, waterLevel);

    // Heating resistance coil (nichrome spiral)
    const coilY = calY + calH - 40;
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(calX + 25, calY);
    ctx.lineTo(calX + 25, coilY);
    // Spiral
    for (let s = 0; s < 6; s++) {
        ctx.arc(calX + 45 + s * 14, coilY, 7, 0, Math.PI, false);
    }
    ctx.lineTo(calX + calW - 25, calY);
    ctx.stroke();

    // Thermometer
    const thX = calX + 35;
    ctx.fillStyle = '#f8fafc';
    ctx.fillRect(thX - 3, calY - 15, 6, calH - 10);
    ctx.fillStyle = '#f43f5e';
    ctx.fillRect(thX - 2, calY + 20, 4, calH - 45);

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f43f5e';
    ctx.fillText(`ΔT = +${deltaT} °C`, thX + 12, calY + 25);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Heating Coil (${r}Ω)`, calX + 25, calY + calH + 20);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`H = I²·R·t = (${i}A)² × ${r}Ω × ${t}s = ${heatJ.toFixed(0)} J`, 100, h - 12);
}

// -------------------------------------------------------------
// Simulator 14: Thermal Appliance & Bulb Filament Studio
// -------------------------------------------------------------
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

    const app = document.getElementById('sim14_app_select')?.value || 'bulb';
    const pPct = parseInt(document.getElementById('sim14_power_slider')?.value || 80);
    document.getElementById('sim14_power_txt').textContent = `${pPct}%`;

    const cx = w / 2;
    const cy = h / 2;

    if (app === 'bulb') {
        document.getElementById('sim14_val_temp').textContent = `${(1500 + pPct * 15)} °C (Glowing)`;
        document.getElementById('sim14_val_gas').textContent = 'Inactive Nitrogen & Argon';
        document.getElementById('sim14_val_cord').textContent = 'Low R Copper: Cool (~30°C)';
        document.getElementById('sim14_val_mp').textContent = '3380 °C (Tungsten MP)';

        // Glass bulb globe
        ctx.beginPath();
        ctx.arc(cx, cy - 15, 65, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(251, 191, 36, ${0.1 + (pPct / 100) * 0.4})`;
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Bulb base
        ctx.fillStyle = '#64748b';
        ctx.fillRect(cx - 20, cy + 45, 40, 35);

        // Tungsten filament support wires
        ctx.strokeStyle = '#cbd5e1';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(cx - 15, cy + 45); ctx.lineTo(cx - 15, cy - 10);
        ctx.moveTo(cx + 15, cy + 45); ctx.lineTo(cx + 15, cy - 10);
        ctx.stroke();

        // Coiled-coil Tungsten filament
        ctx.strokeStyle = (pPct > 40) ? '#fef08a' : '#f59e0b';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(cx - 15, cy - 10);
        ctx.quadraticCurveTo(cx, cy - 35, cx + 15, cy - 10);
        ctx.stroke();

        // Radiating heat waves
        ctx.strokeStyle = `rgba(245, 158, 11, ${(pPct / 100) * 0.6})`;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.arc(cx, cy - 15, 85, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#fef08a';
        ctx.fillText('White-Hot Tungsten Filament (3380°C MP)', cx - 110, cy - 85);
        ctx.fillStyle = '#38bdf8';
        ctx.fillText('Sealed with Chemically Inactive N₂ / Ar Gas', cx - 110, h - 15);
    } else {
        // Laundry Iron / Toaster
        document.getElementById('sim14_val_temp').textContent = `${(180 + pPct * 3.5).toFixed(0)} °C`;
        document.getElementById('sim14_val_gas').textContent = 'Mica Sheet Encapsulation';
        document.getElementById('sim14_val_cord').textContent = 'Lead Cord: Remains Room Temp';
        document.getElementById('sim14_val_mp').textContent = 'High Resistivity Nichrome';

        ctx.fillStyle = '#334155';
        ctx.beginPath();
        ctx.moveTo(cx - 120, cy + 40);
        ctx.lineTo(cx + 100, cy + 40);
        ctx.lineTo(cx + 140, cy);
        ctx.lineTo(cx - 120, cy);
        ctx.closePath();
        ctx.fill();
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Glowing nichrome ribbon inside
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 4;
        ctx.beginPath();
        for (let k = 0; k < 8; k++) {
            ctx.lineTo(cx - 100 + k * 28, cy + 10 + (k % 2 === 0 ? 0 : 20));
        }
        ctx.stroke();

        ctx.font = '11px Inter, sans-serif';
        ctx.fillStyle = '#f43f5e';
        ctx.fillText('Nichrome Ribbon Element (Embedded in Mica)', cx - 120, cy - 15);
    }
}

// -------------------------------------------------------------
// Simulator 15: Electric Fuse Safety & Meltdown Simulator
// -------------------------------------------------------------
let sim15Melted = false;

function sim15TriggerSurge() {
    const slider = document.getElementById('sim15_load_slider');
    if (slider) slider.value = 11.5;
    sim15Update();
}

function sim15ResetFuse() {
    sim15Melted = false;
    const slider = document.getElementById('sim15_load_slider');
    if (slider) slider.value = 4.5;
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

    const fuseRating = parseFloat(document.getElementById('sim15_fuse_select')?.value || 5);
    const loadI = parseFloat(document.getElementById('sim15_load_slider')?.value || 4.5);
    document.getElementById('sim15_load_txt').textContent = `${loadI.toFixed(1)} A`;

    if (loadI > fuseRating) {
        sim15Melted = true;
    }

    if (sim15Melted) {
        document.getElementById('sim15_val_status').textContent = 'MELTED & BLOWN (Circuit Broken)';
        document.getElementById('sim15_val_status').className = 'text-rose-400 font-bold text-sm';
        document.getElementById('sim15_val_app').textContent = 'SAFE (Saved from Burnout)';
        document.getElementById('sim15_val_app').className = 'text-emerald-400 font-bold text-sm';
    } else {
        document.getElementById('sim15_val_status').textContent = `Intact (Carrying ${loadI}A / ${fuseRating}A)`;
        document.getElementById('sim15_val_status').className = 'text-emerald-400 font-bold text-sm';
        document.getElementById('sim15_val_app').textContent = 'Normal Power Delivery';
        document.getElementById('sim15_val_app').className = 'text-amber-400 font-bold text-sm';
    }

    // Live wire bus through fuse to appliance
    const liveY = 90;
    const fuseX = 220;
    const fuseW = 100;

    // Incoming Live wire (Red)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(50, liveY);
    ctx.lineTo(fuseX, liveY);
    ctx.stroke();

    // Fuse Cartridge
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(fuseX, liveY - 20, fuseW, 40);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(fuseX, liveY - 20, fuseW, 40);

    // Fuse wire inside
    if (!sim15Melted) {
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(fuseX, liveY);
        ctx.lineTo(fuseX + fuseW, liveY);
        ctx.stroke();
    } else {
        // Broken melted wire
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(fuseX, liveY);
        ctx.lineTo(fuseX + 35, liveY);
        ctx.moveTo(fuseX + fuseW - 35, liveY);
        ctx.lineTo(fuseX + fuseW, liveY);
        ctx.stroke();

        // Spark / Melt puff
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(fuseX + fuseW/2, liveY, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(fuseX + fuseW/2, liveY, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    // Wire to appliance
    ctx.strokeStyle = sim15Melted ? '#64748b' : '#ef4444';
    ctx.beginPath();
    ctx.moveTo(fuseX + fuseW, liveY);
    ctx.lineTo(w - 120, liveY);
    ctx.stroke();

    // Expensive Appliance Box
    const appX = w - 120;
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(appX, liveY - 35, 70, 70);
    ctx.strokeStyle = sim15Melted ? '#64748b' : '#10b981';
    ctx.lineWidth = 2.5;
    ctx.strokeRect(appX, liveY - 35, 70, 70);

    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText('Appliance', appX + 12, liveY);
    ctx.fillStyle = sim15Melted ? '#94a3b8' : '#10b981';
    ctx.fillText(sim15Melted ? 'Power: 0W' : 'Power: 1kW', appX + 8, liveY + 16);

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Fuse Cartridge (${fuseRating} A Rating)`, fuseX - 10, liveY - 28);
    ctx.fillStyle = sim15Melted ? '#f43f5e' : '#10b981';
    ctx.fillText(sim15Melted ? '⚡ CURRENT SURGE! Fuse melted; Appliance spared from fire!' : '✓ Safe load within fuse threshold rating.', 80, h - 25);
}

// -------------------------------------------------------------
// Simulator 16: Electric Power & Commercial Energy Meter
// -------------------------------------------------------------
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

    const powerW = parseFloat(document.getElementById('sim16_power_slider')?.value || 400);
    const hours = parseFloat(document.getElementById('sim16_hours_slider')?.value || 8);
    const rate = parseFloat(document.getElementById('sim16_tariff_slider')?.value || 5.0);

    document.getElementById('sim16_power_txt').textContent = `${powerW} W`;
    document.getElementById('sim16_hours_txt').textContent = `${hours} hrs/day`;
    document.getElementById('sim16_tariff_txt').textContent = `₹${rate.toFixed(1)} / unit`;

    // Energy calculations
    const dailyKwh = (powerW * hours) / 1000;
    const monthlyKwh = dailyKwh * 30;
    const monthlyBill = monthlyKwh * rate;

    document.getElementById('sim16_val_daily').textContent = `${dailyKwh.toFixed(2)} kWh (Units)`;
    document.getElementById('sim16_val_monthly').textContent = `${monthlyKwh.toFixed(1)} kWh (Units)`;
    document.getElementById('sim16_val_bill').textContent = `₹ ${monthlyBill.toFixed(2)}`;

    // Digital Energy Meter Dashboard Visual
    const meterX = w / 2 - 140;
    const meterY = 30;
    const meterW = 280;
    const meterH = 175;

    // Meter outer casing
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(meterX, meterY, meterW, meterH);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(meterX, meterY, meterW, meterH);

    // Digital LCD display window
    ctx.fillStyle = '#022c22';
    ctx.fillRect(meterX + 25, meterY + 25, meterW - 50, 65);
    ctx.strokeStyle = '#059669';
    ctx.lineWidth = 2;
    ctx.strokeRect(meterX + 25, meterY + 25, meterW - 50, 65);

    // Digital 7-segment style text
    ctx.font = 'bold 26px "Courier New", monospace';
    ctx.fillStyle = '#34d399';
    ctx.fillText(`${monthlyKwh.toFixed(1).padStart(6, '0')} kWh`, meterX + 45, meterY + 65);

    // Blinking pulse LED
    ctx.beginPath();
    ctx.arc(meterX + 45, meterY + 115, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#ef4444';
    ctx.fill();

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Cal Pulse: 3200 imp/kWh', meterX + 60, meterY + 118);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Active Load: ${powerW} W @ 220 V`, meterX + 45, meterY + 145);
    ctx.fillStyle = '#10b981';
    ctx.fillText(`30-Day Cost: ₹${monthlyBill.toFixed(2)} (@ ₹${rate}/unit)`, meterX + 45, meterY + 165);
}
"""

with open(".agents/c10s_ch11_sim_handlers.js", "w", encoding="utf-8") as f:
    f.write(SIMULATOR_JS)

print("Saved .agents/c10s_ch11_sim_handlers.js successfully!")

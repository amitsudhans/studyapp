# -*- coding: utf-8 -*-
SIMULATOR_JS = """
// ==========================================
// SIMULATOR 1: Molecular Movement & Repair
// ==========================================
let s1RepairActive = false;
let s1Order = 100;
let s1Particles = [];
let s1AnimId = null;

function initSlide1() {
    const canvas = document.getElementById('s1Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    s1Particles = [];
    for (let i = 0; i < 35; i++) {
        s1Particles.push({
            x: 60 + Math.random() * 360,
            y: 40 + Math.random() * 120,
            vx: (Math.random() - 0.5) * 1.5,
            vy: (Math.random() - 0.5) * 1.5,
            radius: 3.5 + Math.random() * 2.5,
            color: '#10b981'
        });
    }
    if (s1AnimId) cancelAnimationFrame(s1AnimId);
    animateSlide1();
}

function animateSlide1() {
    const canvas = document.getElementById('s1Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw cellular border
    ctx.strokeStyle = s1RepairActive ? '#10b981' : '#f59e0b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.roundRect(40, 20, 400, 160, 20);
    ctx.stroke();

    // Degradation or repair logic
    if (s1RepairActive) {
        if (s1Order < 100) s1Order += 0.4;
    } else {
        if (s1Order > 45) s1Order -= 0.15;
    }

    const orderEl = document.getElementById('s1OrderVal');
    const stateEl = document.getElementById('s1StateVal');
    if (orderEl) orderEl.textContent = Math.round(s1Order) + '%';
    if (stateEl) {
        if (s1Order > 80) {
            stateEl.textContent = 'Living & Maintained';
            stateEl.className = 'font-bold text-emerald-400';
        } else if (s1Order > 60) {
            stateEl.textContent = 'Degrading (Wear)';
            stateEl.className = 'font-bold text-amber-400';
        } else {
            stateEl.textContent = 'Critical Breakdown!';
            stateEl.className = 'font-bold text-rose-400';
        }
    }

    // Move & draw molecular particles
    s1Particles.forEach(p => {
        p.x += p.vx * (s1RepairActive ? 1.4 : 0.6);
        p.y += p.vy * (s1RepairActive ? 1.4 : 0.6);
        if (p.x < 50 || p.x > 430) p.vx *= -1;
        if (p.y < 30 || p.y > 170) p.vy *= -1;

        ctx.fillStyle = s1RepairActive ? '#34d399' : '#fbbf24';
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
    });

    // Draw connecting repair lines if active
    if (s1RepairActive) {
        ctx.strokeStyle = 'rgba(52, 211, 153, 0.25)';
        ctx.lineWidth = 1;
        for (let i = 0; i < s1Particles.length; i += 3) {
            for (let j = i + 1; j < s1Particles.length; j += 4) {
                const dist = Math.hypot(s1Particles[i].x - s1Particles[j].x, s1Particles[i].y - s1Particles[j].y);
                if (dist < 60) {
                    ctx.beginPath();
                    ctx.moveTo(s1Particles[i].x, s1Particles[i].y);
                    ctx.lineTo(s1Particles[j].x, s1Particles[j].y);
                    ctx.stroke();
                }
            }
        }
    }

    s1AnimId = requestAnimationFrame(animateSlide1);
}

function toggleSlide1Repair() {
    s1RepairActive = !s1RepairActive;
    const btn = document.getElementById('s1RepairBtn');
    const badge = document.getElementById('s1StatusBadge');
    if (btn) {
        btn.textContent = s1RepairActive ? 'Active Molecular Repair (ON)' : 'Enable Active Repair';
        btn.className = s1RepairActive
            ? 'px-3 py-1.5 rounded-xl bg-orange-600 hover:bg-orange-500 text-slate-950 font-bold text-xs transition-all animate-pulse'
            : 'px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs transition-all';
    }
    if (badge) {
        badge.textContent = s1RepairActive ? 'Active Maintenance: Repairing Tissues' : 'Degradation: Natural Wear';
        badge.className = s1RepairActive
            ? 'absolute top-5 right-5 px-2.5 py-1 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
            : 'absolute top-5 right-5 px-2.5 py-1 rounded-full text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40';
    }
}

function resetSlide1Sim() {
    s1RepairActive = false;
    s1Order = 100;
    const btn = document.getElementById('s1RepairBtn');
    if (btn) {
        btn.textContent = 'Enable Active Repair';
        btn.className = 'px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs transition-all';
    }
    initSlide1();
}

// ==========================================
// SIMULATOR 2: Single-Celled vs Multicellular Diffusion
// ==========================================
let s2Mode = 'unicellular';

function initSlide2() {
    drawSlide2();
}

function setSlide2Mode(mode) {
    s2Mode = mode;
    const btnUni = document.getElementById('s2BtnUni');
    const btnMulti = document.getElementById('s2BtnMulti');
    const desc = document.getElementById('s2Description');

    if (mode === 'unicellular') {
        if (btnUni) btnUni.className = 'px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all';
        if (btnMulti) btnMulti.className = 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
        if (desc) {
            desc.innerHTML = `
                <span class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider block">Direct Diffusion (Amoeba)</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    In unicellular Amoeba, the entire plasma membrane touches the aquatic medium. Gases, nutrients, and wastes diffuse in fractions of a second across microscopic distances.
                </p>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <div class="flex justify-between text-[11px]"><span class="text-slate-400">Diffusion Distance:</span><span class="font-mono text-emerald-400">&lt; 50 μm</span></div>
                    <div class="flex justify-between text-[11px]"><span class="text-slate-400">Oxygen Transit Time:</span><span class="font-mono text-emerald-400">0.02 seconds</span></div>
                </div>
            `;
        }
    } else {
        if (btnUni) btnUni.className = 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
        if (btnMulti) btnMulti.className = 'px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all';
        if (desc) {
            desc.innerHTML = `
                <span class="font-bold text-rose-400 uppercase text-[10px] tracking-wider block">Multicellular Diffusion Inadequacy</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Internal body cells are deeply buried beneath millions of tissue layers. Simple diffusion from the skin surface would take over 3 years for oxygen to reach the human big toe!
                </p>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <div class="flex justify-between text-[11px]"><span class="text-slate-400">Tissue Distance:</span><span class="font-mono text-rose-400">&gt; 1 meter</span></div>
                    <div class="flex justify-between text-[11px]"><span class="text-slate-400">Diffusion Transit Time:</span><span class="font-mono text-rose-400">~ 3 Years (Fatal!)</span></div>
                    <div class="text-[10px] text-amber-300 font-semibold mt-1">Specialized vascular heart & blood circulation mandatory!</div>
                </div>
            `;
        }
    }
    drawSlide2();
}

function drawSlide2() {
    const canvas = document.getElementById('s2Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (s2Mode === 'unicellular') {
        // Draw single amoeba with diffusion arrows
        ctx.fillStyle = '#0f766e';
        ctx.beginPath();
        ctx.ellipse(180, 100, 70, 50, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#2dd4bf';
        ctx.lineWidth = 2.5;
        ctx.stroke();

        ctx.fillStyle = '#ccfbf1';
        ctx.font = 'bold 12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Amoeba (Single Cell)', 180, 105);

        // Surrounding water and diffusion arrows
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        const angles = [0, Math.PI/3, 2*Math.PI/3, Math.PI, 4*Math.PI/3, 5*Math.PI/3];
        angles.forEach(a => {
            const x1 = 180 + Math.cos(a) * 95;
            const y1 = 100 + Math.sin(a) * 75;
            const x2 = 180 + Math.cos(a) * 72;
            const y2 = 100 + Math.sin(a) * 52;
            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.stroke();
        });
        ctx.fillStyle = '#38bdf8';
        ctx.font = '10px sans-serif';
        ctx.fillText('O2 Inflow (Direct Diffusion)', 180, 175);
    } else {
        // Draw multilayer tissue block
        for (let row = 0; row < 4; row++) {
            for (let col = 0; col < 6; col++) {
                const x = 70 + col * 40;
                const y = 40 + row * 30;
                const isDeep = row >= 2;
                ctx.fillStyle = isDeep ? '#334155' : '#1e293b';
                ctx.strokeStyle = isDeep ? '#f43f5e' : '#64748b';
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                ctx.roundRect(x, y, 36, 26, 6);
                ctx.fill();
                ctx.stroke();
            }
        }
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('External Environment (Skin Surface)', 180, 25);

        ctx.fillStyle = '#f43f5e';
        ctx.fillText('Deep Internal Cells (Oxygen Starved without Blood)', 180, 185);
    }
}

// ==========================================
// SIMULATOR 3: Photosynthesis Master Events
// ==========================================
let s3Phase = 1;
const s3Phases = [
    { title: "1. Solar Photon Absorption", desc: "Chlorophyll thylakoid pigments absorb light energy across blue and red wavelengths.", color: "#10b981" },
    { title: "2. Photolysis of Water", desc: "Light energy splits 12 H2O into 24 H+ ions, 24 electrons, and 6 O2 molecules released into air.", color: "#06b6d4" },
    { title: "3. Carbon Dioxide Reduction", desc: "Assimilatory chemical energy (ATP/NADPH) reduces 6 CO2 into 1 glucose molecule (C6H12O6).", color: "#f59e0b" }
];

function initSlide3() {
    drawSlide3();
}

function stepSlide3Event() {
    s3Phase = (s3Phase % 3) + 1;
    const p = s3Phases[s3Phase - 1];
    const titleEl = document.getElementById('s3PhaseTitle');
    const descEl = document.getElementById('s3PhaseDesc');
    if (titleEl) titleEl.textContent = p.title;
    if (descEl) descEl.textContent = p.desc;
    drawSlide3();
}

function drawSlide3() {
    const canvas = document.getElementById('s3Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw chloroplast disc
    ctx.fillStyle = '#064e3b';
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.ellipse(240, 100, 180, 75, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#a7f3d0';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Chloroplast (Thylakoids & Stroma)', 240, 45);

    if (s3Phase === 1) {
        // Sun rays hitting chloroplast
        ctx.fillStyle = '#fde047';
        ctx.beginPath();
        ctx.arc(80, 50, 22, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(105, 60);
        ctx.lineTo(180, 90);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('☀️ Solar Photons Absorbed', 240, 110);
    } else if (s3Phase === 2) {
        // Water photolysis
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 13px font-mono';
        ctx.fillText('12 H2O  ➔  24 H⁺  +  6 O2 ↑  +  24 e⁻', 240, 105);
        ctx.fillStyle = '#67e8f9';
        ctx.font = '11px sans-serif';
        ctx.fillText('(Photolysis: Splitting of Water)', 240, 130);
    } else if (s3Phase === 3) {
        // CO2 reduction to Glucose
        ctx.fillStyle = '#fbbf24';
        ctx.font = 'bold 13px font-mono';
        ctx.fillText('6 CO2  +  Hydrogen Energy  ➔  C6H12O6 (Glucose)', 240, 105);
        ctx.fillStyle = '#fde68a';
        ctx.font = '11px sans-serif';
        ctx.fillText('Stored internally as Insoluble Starch', 240, 130);
    }
}

// ==========================================
// SIMULATOR 4: Activity 5.1 Variegated Leaf
// ==========================================
let s4Step = 1;

function initSlide4() {
    drawSlide4();
}

function stepSlide4Activity() {
    s4Step = (s4Step % 4) + 1;
    updateSlide4UI();
    drawSlide4();
}

function resetSlide4Activity() {
    s4Step = 1;
    updateSlide4UI();
    drawSlide4();
}

function updateSlide4UI() {
    const badge = document.getElementById('s4StepBadge');
    const title = document.getElementById('s4StepTitle');
    const desc = document.getElementById('s4StepDesc');
    const outBox = document.getElementById('s4OutcomeBox');

    const steps = [
        {
            badge: "Stage 1 of 4",
            title: "Step 1: De-starching in Dark",
            desc: "Potted money plant kept in darkness for 3 days. Cells consume all pre-existing starch reserves via respiration."
        },
        {
            badge: "Stage 2 of 4",
            title: "Step 2: 6 Hours in Bright Sunlight",
            desc: "Plant exposed to sunlight. Green patches containing chlorophyll synthesize brand-new starch molecules."
        },
        {
            badge: "Stage 3 of 4",
            title: "Step 3: Boiling Alcohol Water Bath",
            desc: "Leaf boiled in alcohol within a safe hot water bath to dissolve out green chlorophyll, bleaching leaf pale white."
        },
        {
            badge: "Stage 4 of 4",
            title: "Step 4: Iodine Solution Dip",
            desc: "Bleached leaf dipped in dilute iodine. ONLY previously green patches turn deep blue-black! White areas remain pale yellow."
        }
    ];

    const s = steps[s4Step - 1];
    if (badge) badge.textContent = s.badge;
    if (title) title.textContent = s.title;
    if (desc) desc.textContent = s.desc;
    if (outBox) {
        outBox.innerHTML = s4Step === 4
            ? '<strong class="text-amber-400 block mb-0.5">Definitive Conclusion:</strong> Blue-black iodine staining occurs strictly in green zones, proving chlorophyll is indispensable for starch formation.'
            : '<strong class="text-white block mb-0.5">Key Observation:</strong> Follow the stages to isolate and test chlorophyll-dependent carbohydrate synthesis.';
    }
}

function drawSlide4() {
    const canvas = document.getElementById('s4Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw leaf shape
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(180, 30);
    ctx.bezierCurveTo(260, 60, 260, 140, 180, 175);
    ctx.bezierCurveTo(100, 140, 100, 60, 180, 30);

    if (s4Step === 1 || s4Step === 2) {
        // Variegated: White base with green center
        ctx.fillStyle = '#fef08a';
        ctx.fill();
        ctx.clip();

        ctx.fillStyle = '#15803d';
        ctx.beginPath();
        ctx.ellipse(180, 100, 38, 55, 0, 0, Math.PI * 2);
        ctx.fill();
    } else if (s4Step === 3) {
        // Bleached in alcohol: completely pale white
        ctx.fillStyle = '#f8fafc';
        ctx.fill();
    } else if (s4Step === 4) {
        // Iodine stained: center blue-black, outer pale brown
        ctx.fillStyle = '#fef3c7';
        ctx.fill();
        ctx.clip();

        ctx.fillStyle = '#1e1b4b'; // deep blue-black
        ctx.beginPath();
        ctx.ellipse(180, 100, 38, 55, 0, 0, Math.PI * 2);
        ctx.fill();
    }
    ctx.restore();

    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(180, 30);
    ctx.bezierCurveTo(260, 60, 260, 140, 180, 175);
    ctx.bezierCurveTo(100, 140, 100, 60, 180, 30);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    if (s4Step === 1) ctx.fillText('De-starched Leaf (No Starch)', 180, 190);
    else if (s4Step === 2) ctx.fillText('Photosynthesizing in Light', 180, 190);
    else if (s4Step === 3) ctx.fillText('Bleached Leaf (Chlorophyll Removed)', 180, 190);
    else if (s4Step === 4) ctx.fillText('Iodine Blue-Black (Starch Confirmed)', 180, 190);
}

// ==========================================
// SIMULATOR 5: Guard Cells & KOH Bell Jar
// ==========================================
let s5Tab = 'stoma';
let s5Turgor = 80;

function initSlide5() {
    drawSlide5();
}

function setSlide5Tab(tab) {
    s5Tab = tab;
    const tabStoma = document.getElementById('s5TabStoma');
    const tabKOH = document.getElementById('s5TabKOH');
    const controls = document.getElementById('s5Controls');

    if (tab === 'stoma') {
        if (tabStoma) tabStoma.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all';
        if (tabKOH) tabKOH.className = 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
        if (controls) {
            controls.innerHTML = `
                <div>
                    <div class="flex justify-between text-xs mb-1">
                        <span class="text-slate-400">Guard Cell Water Inflow (Turgor):</span>
                        <span id="s5TurgorVal" class="font-mono text-emerald-400 font-bold">Turgid (Open Pore)</span>
                    </div>
                    <input type="range" id="s5TurgorSlider" min="0" max="100" value="${s5Turgor}" oninput="updateSlide5Stoma(this.value)" class="w-full accent-emerald-500">
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    <strong class="text-amber-400">Hydraulic Mechanism:</strong> Water inflow swells guard cells; thin outer walls bow out, pulling thick inner concave walls apart to open the pore. Water loss collapses them closed.
                </div>
            `;
        }
    } else {
        if (tabStoma) tabStoma.className = 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
        if (tabKOH) tabKOH.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all';
        if (controls) {
            controls.innerHTML = `
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-300 space-y-2">
                    <strong class="text-cyan-400 block">Activity 5.2: Potassium Hydroxide (KOH) Proof</strong>
                    <p>Plant A is enclosed with KOH watch-glass (absorbs all atmospheric CO2). Plant B has normal air.</p>
                    <div class="grid grid-cols-2 gap-2 text-center mt-2">
                        <div class="p-1.5 rounded bg-slate-950 border border-rose-500/50">
                            <span class="text-rose-400 font-bold block text-[10px]">Bell Jar A (with KOH)</span>
                            <span class="text-slate-400 text-[10px]">Starch Test: NEGATIVE</span>
                        </div>
                        <div class="p-1.5 rounded bg-slate-950 border border-emerald-500/50">
                            <span class="text-emerald-400 font-bold block text-[10px]">Bell Jar B (Control)</span>
                            <span class="text-emerald-300 text-[10px]">Starch Test: POSITIVE ✓</span>
                        </div>
                    </div>
                </div>
            `;
        }
    }
    drawSlide5();
}

function updateSlide5Stoma(val) {
    s5Turgor = parseInt(val);
    const label = document.getElementById('s5TurgorVal');
    if (label) {
        if (s5Turgor > 60) label.textContent = 'Turgid (Open Pore)';
        else if (s5Turgor > 30) label.textContent = 'Partially Open';
        else label.textContent = 'Flaccid (Closed Pore)';
    }
    drawSlide5();
}

function drawSlide5() {
    const canvas = document.getElementById('s5Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (s5Tab === 'stoma') {
        const gap = (s5Turgor / 100) * 22; // pore gap

        // Left guard cell
        ctx.fillStyle = '#059669';
        ctx.strokeStyle = '#34d399';
        ctx.lineWidth = 2.5;

        ctx.beginPath();
        ctx.ellipse(180 - gap - 25, 100, 24, 60, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Right guard cell
        ctx.beginPath();
        ctx.ellipse(180 + gap + 25, 100, 24, 60, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Stomatal aperture (pore)
        ctx.fillStyle = gap > 4 ? '#022c22' : '#064e3b';
        ctx.beginPath();
        ctx.ellipse(180, 100, gap, 45, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(gap > 4 ? 'Stomatal Pore OPEN (Gas Exchange)' : 'Stomatal Pore CLOSED (Water Conserved)', 180, 185);
    } else {
        // Draw two bell jars
        // Jar A
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.roundRect(50, 40, 110, 120, 20);
        ctx.stroke();
        ctx.fillStyle = '#10b981';
        ctx.fillRect(95, 110, 20, 40); // small plant
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(65, 140, 25, 8); // watch glass KOH
        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Jar A (+ KOH)', 105, 175);

        // Jar B
        ctx.strokeStyle = '#38bdf8';
        ctx.beginPath();
        ctx.roundRect(200, 40, 110, 120, 20);
        ctx.stroke();
        ctx.fillStyle = '#10b981';
        ctx.fillRect(245, 110, 20, 40); // plant
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Jar B (Normal Air)', 255, 175);
    }
}

// ==========================================
// SIMULATOR 6: Heterotrophic Modes
// ==========================================
let s6Mode = 'saprophyte';

function initSlide6() {
    drawSlide6();
}

function setSlide6Mode(mode) {
    s6Mode = mode;
    const btnS = document.getElementById('s6BtnSapro');
    const btnH = document.getElementById('s6BtnHolo');
    const btnP = document.getElementById('s6BtnPara');
    const title = document.getElementById('s6Title');
    const desc = document.getElementById('s6Desc');
    const dig = document.getElementById('s6DigVal');
    const host = document.getElementById('s6HostVal');
    const ex = document.getElementById('s6ExVal');

    btnS.className = mode === 'saprophyte' ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnH.className = mode === 'holozoic' ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnP.className = mode === 'parasite' ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (mode === 'saprophyte') {
        title.textContent = 'Saprophytic Nutrition (Bread Mould / Mushrooms)';
        desc.textContent = 'Fungi secrete digestive enzymes externally onto dead organic matter, breaking polymers down into soluble molecules before absorbing them across hyphal walls.';
        dig.textContent = 'External';
        host.textContent = 'Dead Decay';
        ex.textContent = 'Rhizopus';
    } else if (mode === 'holozoic') {
        title.textContent = 'Holozoic Nutrition (Humans, Animals, Amoeba)';
        desc.textContent = 'Organisms ingest whole complex food items into the internal body, followed by mechanical mastication, internal enzymatic digestion, and absorption.';
        dig.textContent = 'Internal';
        host.textContent = 'Whole Food';
        ex.textContent = 'Humans / Amoeba';
    } else {
        title.textContent = 'Parasitic Nutrition (Cuscuta / Amar-bel, Ticks)';
        desc.textContent = 'Parasites derive continuous nourishment directly from a living host plant or animal without killing it immediately, using specialized absorptive haustoria.';
        dig.textContent = 'Host Derived';
        host.textContent = 'Living Host';
        ex.textContent = 'Cuscuta / Leeches';
    }
    drawSlide6();
}

function drawSlide6() {
    const canvas = document.getElementById('s6Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s6Mode === 'saprophyte') {
        // Draw bread substrate & fungal hyphae
        ctx.fillStyle = '#78350f';
        ctx.fillRect(80, 130, 200, 40); // bread slice

        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(130, 130); ctx.lineTo(130, 70);
        ctx.moveTo(180, 130); ctx.lineTo(180, 60);
        ctx.moveTo(230, 130); ctx.lineTo(230, 75);
        ctx.stroke();

        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(130, 65, 12, 0, Math.PI * 2);
        ctx.arc(180, 55, 14, 0, Math.PI * 2);
        ctx.arc(230, 70, 11, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fde68a';
        ctx.font = '10px sans-serif';
        ctx.fillText('External Enzymes Dissolving Bread Substrate', 180, 185);
    } else if (s6Mode === 'holozoic') {
        ctx.fillStyle = '#1e3a8a';
        ctx.beginPath();
        ctx.roundRect(120, 40, 120, 120, 25);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(180, 100, 18, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Ingested Food', 180, 105);
        ctx.font = '10px sans-serif';
        ctx.fillText('Internal Enzymatic Breakdown', 180, 185);
    } else {
        // Cuscuta coiled on host stem
        ctx.fillStyle = '#15803d';
        ctx.fillRect(160, 30, 40, 140); // host green stem

        ctx.strokeStyle = '#eab308';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(140, 50); ctx.lineTo(210, 80);
        ctx.moveTo(140, 90); ctx.lineTo(210, 120);
        ctx.moveTo(140, 130); ctx.lineTo(210, 150);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Yellow Cuscuta Haustoria Sucking Host Sap', 180, 185);
    }
}

// ==========================================
// SIMULATOR 7: Amoeba Phagocytosis vs Paramoecium
// ==========================================
let s7Organism = 'amoeba';
let s7Engulfed = false;

function initSlide7() {
    drawSlide7();
}

function toggleSlide7Organism() {
    s7Organism = s7Organism === 'amoeba' ? 'paramoecium' : 'amoeba';
    s7Engulfed = false;
    const btnT = document.getElementById('s7ToggleBtn');
    const title = document.getElementById('s7OrganismTitle');
    const desc = document.getElementById('s7OrganismDesc');
    const app = document.getElementById('s7Apparatus');

    if (s7Organism === 'amoeba') {
        btnT.textContent = 'Switch to Paramoecium';
        title.textContent = 'Amoeba Phagocytosis (Figure 5.5)';
        desc.textContent = 'Temporary finger-like pseudopodia extend and fuse around food, forming an internal food vacuole where hydrolytic enzymes digest polymers into soluble nutrients.';
        app.textContent = 'Pseudopodia (Any Site)';
    } else {
        btnT.textContent = 'Switch to Amoeba';
        title.textContent = 'Paramoecium Ciliary Wave Feeding';
        desc.textContent = 'Paramoecium maintains a definite slipper shape. Rhythmic wave-like beating of thousands of surface cilia sweeps food particles toward a fixed oral cytostome groove.';
        app.textContent = 'Cilia to Oral Groove';
    }
    drawSlide7();
}

function triggerSlide7Engulf() {
    s7Engulfed = !s7Engulfed;
    drawSlide7();
}

function drawSlide7() {
    const canvas = document.getElementById('s7Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s7Organism === 'amoeba') {
        // Amoeba body
        ctx.fillStyle = '#0d9488';
        ctx.strokeStyle = '#2dd4bf';
        ctx.lineWidth = 3;

        ctx.beginPath();
        if (!s7Engulfed) {
            // Pseudopodia opening like arms
            ctx.moveTo(120, 100);
            ctx.bezierCurveTo(100, 40, 170, 30, 200, 60); // top arm
            ctx.bezierCurveTo(180, 80, 160, 100, 180, 120); // mouth indentation
            ctx.bezierCurveTo(170, 160, 100, 150, 120, 100); // bottom arm
            ctx.fill();
            ctx.stroke();

            // Food particle outside
            ctx.fillStyle = '#f43f5e';
            ctx.beginPath();
            ctx.arc(220, 100, 9, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = '#ffffff';
            ctx.font = '10px sans-serif';
            ctx.fillText('Food Particle Outside', 180, 185);
        } else {
            // Food engulfed into food vacuole
            ctx.ellipse(180, 100, 75, 55, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();

            // Food vacuole inside
            ctx.fillStyle = '#042f2e';
            ctx.beginPath();
            ctx.arc(180, 100, 22, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = '#facc15';
            ctx.lineWidth = 2;
            ctx.stroke();

            ctx.fillStyle = '#f43f5e';
            ctx.beginPath();
            ctx.arc(180, 100, 8, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = '#ffffff';
            ctx.font = '10px sans-serif';
            ctx.fillText('Enzymatic Digestion in Food Vacuole', 180, 185);
        }
    } else {
        // Paramoecium slipper shape with cilia
        ctx.fillStyle = '#0284c7';
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;

        ctx.beginPath();
        ctx.ellipse(180, 100, 85, 42, -0.15, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Oral groove
        ctx.fillStyle = '#0c4a6e';
        ctx.beginPath();
        ctx.ellipse(195, 100, 16, 26, 0.4, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Oral Groove (Cytostome)', 195, 105);
        ctx.fillText('Surface Cilia Wave Currents', 180, 185);
    }
}

// ==========================================
// SIMULATOR 8: Buccal Cavity, Saliva & Peristalsis
// ==========================================
let s8BolusY = 40;
let s8Anim = null;

function initSlide8() {
    drawSlide8();
}

function triggerSlide8Peristalsis() {
    s8BolusY = 40;
    if (s8Anim) cancelAnimationFrame(s8Anim);
    animateSlide8();
}

function animateSlide8() {
    s8BolusY += 2.5;
    drawSlide8();
    if (s8BolusY < 160) {
        s8Anim = requestAnimationFrame(animateSlide8);
    }
}

function drawSlide8() {
    const canvas = document.getElementById('s8Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw oesophagus tube with muscular constriction wave
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 4;

    // Left muscular wall
    ctx.beginPath();
    ctx.moveTo(140, 20);
    for (let y = 20; y <= 180; y += 10) {
        const bulge = Math.abs(y - s8BolusY) < 20 ? 12 : 0;
        ctx.lineTo(140 - bulge, y);
    }
    ctx.stroke();

    // Right muscular wall
    ctx.beginPath();
    ctx.moveTo(220, 20);
    for (let y = 20; y <= 180; y += 10) {
        const bulge = Math.abs(y - s8BolusY) < 20 ? 12 : 0;
        ctx.lineTo(220 + bulge, y);
    }
    ctx.stroke();

    // Food bolus moving downward
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.ellipse(180, s8BolusY, 16, 20, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = '10px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Peristaltic Wave Propelling Bolus', 180, 192);
}

// ==========================================
// SIMULATOR 9: Gastric, Bile & Intestinal Villi
// ==========================================
let s9Section = 'stomach';

function initSlide9() {
    drawSlide9();
}

function setSlide9Section(sec) {
    s9Section = sec;
    const btnS = document.getElementById('s9BtnStomach');
    const btnB = document.getElementById('s9BtnBile');
    const btnV = document.getElementById('s9BtnVilli');
    const title = document.getElementById('s9Title');
    const desc = document.getElementById('s9Desc');

    btnS.className = sec === 'stomach' ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnB.className = sec === 'bile' ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnV.className = sec === 'villi' ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (sec === 'stomach') {
        title.textContent = 'Stomach: HCl, Pepsin & Mucus';
        desc.textContent = 'Gastric glands secrete HCl (creates acidic pH 2 and kills bacteria), pepsin (digests proteins), and mucus (shields gastric lining from acid corrosion).';
    } else if (sec === 'bile') {
        title.textContent = 'Liver Bile Juice & Pancreas Secretions';
        desc.textContent = 'Alkaline bile salts neutralize stomach acid and emulsify large insoluble lipid droplets into microscopic globules for pancreatic lipase.';
    } else {
        title.textContent = 'Microscopic Intestinal Villi Absorption';
        desc.textContent = 'Millions of vascularized finger-like villi maximize surface area (> 30 m²). Capillaries absorb glucose and amino acids; lacteals absorb digested fats.';
    }
    drawSlide9();
}

function drawSlide9() {
    const canvas = document.getElementById('s9Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s9Section === 'stomach') {
        // Draw stomach organ
        ctx.fillStyle = '#881337';
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.ellipse(180, 100, 75, 50, -0.2, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#fecdd3';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Gastric Lumen (pH 1.5 - 2.0)', 180, 95);
        ctx.font = '10px sans-serif';
        ctx.fillText('HCl + Pepsin + Mucus Layer', 180, 115);
    } else if (s9Section === 'bile') {
        // Large lipid droplet vs emulsified droplets
        ctx.fillStyle = '#eab308';
        ctx.beginPath();
        ctx.arc(100, 100, 35, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Large Fat', 100, 100);

        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(150, 100); ctx.lineTo(190, 100);
        ctx.stroke();

        // Emulsified tiny droplets
        for (let i = 0; i < 9; i++) {
            const rx = 220 + (i % 3) * 22;
            const ry = 80 + Math.floor(i / 3) * 22;
            ctx.fillStyle = '#facc15';
            ctx.beginPath();
            ctx.arc(rx, ry, 7, 0, Math.PI * 2);
            ctx.fill();
        }
        ctx.fillStyle = '#a7f3d0';
        ctx.fillText('Emulsified Micelles (High Area)', 240, 160);
    } else {
        // Microscopic Villi fingers
        ctx.fillStyle = '#fb7185';
        ctx.strokeStyle = '#fda4af';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(60, 160);
        for (let i = 0; i < 5; i++) {
            const x = 80 + i * 50;
            ctx.lineTo(x, 40);
            ctx.arc(x + 15, 40, 15, Math.PI, 0, false);
            ctx.lineTo(x + 30, 160);
        }
        ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Intestinal Villi with Capillary Blood Vessels', 180, 185);
    }
}

// ==========================================
// SIMULATOR 10: Glucose Breakdown Pathways
// ==========================================
let s10Pathway = 'aerobic';

function initSlide10() {
    drawSlide10();
}

function setSlide10Pathway(pw) {
    s10Pathway = pw;
    const btnA = document.getElementById('s10BtnAero');
    const btnM = document.getElementById('s10BtnMuscle');
    const btnY = document.getElementById('s10BtnYeast');
    const title = document.getElementById('s10Title');
    const desc = document.getElementById('s10Desc');
    const out = document.getElementById('s10EnergyOut');

    btnA.className = pw === 'aerobic' ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnM.className = pw === 'muscle' ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnY.className = pw === 'yeast' ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (pw === 'aerobic') {
        title.textContent = 'Aerobic Respiration in Mitochondria';
        desc.textContent = 'In the presence of oxygen, 3-carbon pyruvate is oxidized completely inside mitochondria into carbon dioxide, water, and 38 ATP molecules.';
        out.textContent = '38 ATP (~30.5 kJ/mol per ATP)';
    } else if (pw === 'muscle') {
        title.textContent = 'Lack of Oxygen in Human Muscle Cells';
        desc.textContent = 'During sudden strenuous exertion, cellular oxygen runs short; pyruvate is converted into 3-carbon lactic acid, causing acute muscle cramps.';
        out.textContent = '2 ATP + Lactic Acid (Cramps)';
    } else {
        title.textContent = 'Anaerobic Yeast Fermentation (Absence of O2)';
        desc.textContent = 'In the total absence of oxygen, yeast converts pyruvate into 2-carbon ethanol, carbon dioxide, and modest energy.';
        out.textContent = '2 ATP + Ethanol + CO2';
    }
    drawSlide10();
}

function drawSlide10() {
    const canvas = document.getElementById('s10Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';

    // Step 1: Glucose box
    ctx.fillStyle = '#1e293b';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(20, 75, 80, 50, 8);
    ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Glucose', 60, 96);
    ctx.font = '9.5px sans-serif';
    ctx.fillText('(6-Carbon)', 60, 112);

    // Arrow to Pyruvate
    ctx.strokeStyle = '#94a3b8';
    ctx.beginPath();
    ctx.moveTo(100, 100); ctx.lineTo(135, 100); ctx.stroke();

    // Step 2: Pyruvate box
    ctx.fillStyle = '#1e293b';
    ctx.strokeStyle = '#f59e0b';
    ctx.beginPath();
    ctx.roundRect(135, 75, 80, 50, 8);
    ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('Pyruvate', 175, 96);
    ctx.font = '9.5px sans-serif';
    ctx.fillText('(3-Carbon)', 175, 112);

    // Arrow to chosen pathway outcome
    ctx.beginPath();
    ctx.moveTo(215, 100); ctx.lineTo(250, 100); ctx.stroke();

    // Step 3: Pathway Outcome
    ctx.beginPath();
    ctx.roundRect(250, 60, 100, 80, 10);

    if (s10Pathway === 'aerobic') {
        ctx.fillStyle = '#064e3b';
        ctx.strokeStyle = '#10b981';
        ctx.fill(); ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10.5px sans-serif';
        ctx.fillText('Mitochondria', 300, 85);
        ctx.fillText('CO2 + H2O', 300, 105);
        ctx.fillStyle = '#34d399';
        ctx.fillText('+ 38 ATP', 300, 125);
    } else if (s10Pathway === 'muscle') {
        ctx.fillStyle = '#881337';
        ctx.strokeStyle = '#f43f5e';
        ctx.fill(); ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10.5px sans-serif';
        ctx.fillText('Muscle Cells', 300, 85);
        ctx.fillText('Lactic Acid', 300, 105);
        ctx.fillStyle = '#fb7185';
        ctx.fillText('+ Muscle Cramps', 300, 125);
    } else {
        ctx.fillStyle = '#78350f';
        ctx.strokeStyle = '#f59e0b';
        ctx.fill(); ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10.5px sans-serif';
        ctx.fillText('Yeast Cell', 300, 85);
        ctx.fillText('Ethanol + CO2', 300, 105);
        ctx.fillStyle = '#fde68a';
        ctx.fillText('+ 2 ATP', 300, 125);
    }
}

// ==========================================
// SIMULATOR 11: Gas Exchange: Plants vs Fish Gills
// ==========================================
let s11View = 'day';

function initSlide11() {
    drawSlide11();
}

function setSlide11View(view) {
    s11View = view;
    const btnD = document.getElementById('s11BtnDay');
    const btnN = document.getElementById('s11BtnNight');
    const btnF = document.getElementById('s11BtnFish');
    const title = document.getElementById('s11Title');
    const desc = document.getElementById('s11Desc');

    btnD.className = view === 'day' ? 'px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnN.className = view === 'night' ? 'px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnF.className = view === 'fish' ? 'px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (view === 'day') {
        title.textContent = 'Plant Daylight Gas Exchange';
        desc.textContent = 'Photosynthesis operates at high speed, consuming all respiratory CO2 internally and releasing large volumes of surplus oxygen through stomata into the air.';
    } else if (view === 'night') {
        title.textContent = 'Plant Nighttime Gas Exchange';
        desc.textContent = 'In darkness, photosynthesis completely stops while cellular respiration continues; carbon dioxide elimination is the primary net gas exchange.';
    } else {
        title.textContent = 'Aquatic Fish Gill Counter-Current Extraction';
        desc.textContent = 'Dissolved oxygen in water is low. Fishes rapidly pump water through mouth and across vascular gill filaments to extract oxygen into blood.';
    }
    drawSlide11();
}

function drawSlide11() {
    const canvas = document.getElementById('s11Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s11View === 'day') {
        // Bright sun + green leaf releasing O2
        ctx.fillStyle = '#fde047';
        ctx.beginPath(); ctx.arc(70, 50, 18, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = '#15803d';
        ctx.beginPath();
        ctx.ellipse(180, 100, 60, 35, -0.2, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(180, 80); ctx.lineTo(180, 40); ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('↑ Oxygen Gas (O2) Released', 180, 30);
    } else if (s11View === 'night') {
        // Dark moon + leaf releasing CO2
        ctx.fillStyle = '#94a3b8';
        ctx.beginPath(); ctx.arc(70, 50, 16, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = '#064e3b';
        ctx.beginPath();
        ctx.ellipse(180, 100, 60, 35, -0.2, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(180, 80); ctx.lineTo(180, 40); ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('↑ Carbon Dioxide (CO2) Released', 180, 30);
    } else {
        // Fish with gills
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.ellipse(180, 100, 75, 45, 0, 0, Math.PI * 2);
        ctx.fill();

        // Gills slits
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 3;
        for (let i = 0; i < 4; i++) {
            ctx.beginPath();
            ctx.arc(150 + i * 8, 100, 22, -0.5, 0.5);
            ctx.stroke();
        }
        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Vascularized Gill Filaments', 180, 185);
    }
}

// ==========================================
// SIMULATOR 12: Human Respiratory System & Alveoli
// ==========================================
let s12Inhaling = false;

function initSlide12() {
    drawSlide12();
}

function toggleSlide12Breath() {
    s12Inhaling = !s12Inhaling;
    const btn = document.getElementById('s12BreathBtn');
    const badge = document.getElementById('s12PhaseBadge');
    const desc = document.getElementById('s12PhaseDesc');

    if (s12Inhaling) {
        btn.textContent = 'Exhale (Relax Chest)';
        badge.textContent = 'Inhaling: Chest Expands';
        badge.className = 'px-2.5 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300';
        desc.textContent = 'Diaphragm flattens downward, intercostal muscles lift ribs outward, thoracic volume expands, drawing air into alveoli.';
    } else {
        btn.textContent = 'Inhale (Expand Chest)';
        badge.textContent = 'Exhaling / Resting';
        badge.className = 'px-2.5 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300';
        desc.textContent = 'Diaphragm relaxes into a dome shape, chest cavity contracts, expelling air while lungs retain vital residual volume.';
    }
    drawSlide12();
}

function drawSlide12() {
    const canvas = document.getElementById('s12Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';

    // Trachea with rings
    ctx.fillStyle = '#334155';
    ctx.fillRect(165, 20, 30, 45);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    for (let y = 25; y < 65; y += 8) {
        ctx.strokeRect(165, y, 30, 4);
    }

    // Lungs (expand if inhaling)
    const lungW = s12Inhaling ? 55 : 42;
    const lungH = s12Inhaling ? 80 : 68;

    ctx.fillStyle = '#f43f5e';
    // Left lung
    ctx.beginPath();
    ctx.ellipse(135, 105, lungW, lungH, 0.15, 0, Math.PI * 2);
    ctx.fill();

    // Right lung
    ctx.beginPath();
    ctx.ellipse(225, 105, lungW, lungH, -0.15, 0, Math.PI * 2);
    ctx.fill();

    // Diaphragm
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    if (s12Inhaling) {
        // Flattened
        ctx.moveTo(80, 165); ctx.lineTo(280, 165);
    } else {
        // Curved dome
        ctx.moveTo(80, 165);
        ctx.quadraticCurveTo(180, 140, 280, 165);
    }
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = '10px sans-serif';
    ctx.fillText(s12Inhaling ? 'Flattened Diaphragm (Air Inrush)' : 'Dome-Shaped Relaxed Diaphragm', 180, 185);
}

// ==========================================
// SIMULATOR 13: 4-Chambered Human Heart
// ==========================================
let s13Step = 1;

function initSlide13() {
    drawSlide13();
}

function stepSlide13Heart() {
    s13Step = (s13Step % 3) + 1;
    const badge = document.getElementById('s13PhaseBadge');
    const title = document.getElementById('s13Title');
    const desc = document.getElementById('s13Desc');

    if (s13Step === 1) {
        badge.textContent = 'Phase 1: Atrial Filling';
        title.textContent = 'Atria Receive Inflowing Blood';
        desc.textContent = 'Right atrium collects deoxygenated blood from vena cava; left atrium collects oxygenated blood from pulmonary veins.';
    } else if (s13Step === 2) {
        badge.textContent = 'Phase 2: Ventricular Filling';
        title.textContent = 'Tricuspid & Bicuspid Valves Open';
        desc.textContent = 'Atria contract, forcing blood through atrioventricular valves into the relaxed right and left ventricles.';
    } else {
        badge.textContent = 'Phase 3: Ventricular Systole';
        title.textContent = 'Ventricles Pump into Aorta & Lungs';
        desc.textContent = 'Thick-walled ventricles contract powerfully, pumping blood into pulmonary artery (to lungs) and systemic aorta (to body).';
    }
    drawSlide13();
}

function drawSlide13() {
    const canvas = document.getElementById('s13Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Heart 4 chambers box
    const cx = 180, cy = 100;

    // Right Atrium (blue deoxygenated)
    ctx.fillStyle = '#1e3a8a';
    ctx.fillRect(cx - 70, cy - 60, 65, 55);

    // Left Atrium (red oxygenated)
    ctx.fillStyle = '#881337';
    ctx.fillRect(cx + 5, cy - 60, 65, 55);

    // Right Ventricle (blue)
    ctx.fillStyle = '#172554';
    ctx.fillRect(cx - 70, cy + 5, 65, 65);

    // Left Ventricle (thick red wall)
    ctx.fillStyle = '#4c0519';
    ctx.fillRect(cx + 5, cy + 5, 65, 65);

    // Ventricular septum & walls
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 3;
    ctx.strokeRect(cx - 70, cy - 60, 140, 130);
    ctx.beginPath();
    ctx.moveTo(cx, cy - 60); ctx.lineTo(cx, cy + 70); // vertical septum
    ctx.moveTo(cx - 70, cy); ctx.lineTo(cx + 70, cy); // horizontal valve line
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 10px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Right Atrium', cx - 38, cy - 30);
    ctx.fillText('Left Atrium', cx + 38, cy - 30);
    ctx.fillText('Right Ventricle', cx - 38, cy + 40);
    ctx.fillText('Left Ventricle', cx + 38, cy + 40);

    // Text at bottom
    ctx.font = '10px sans-serif';
    ctx.fillText('4 Chambers: Complete Separation of Arterial & Venous Blood', 180, 185);
}

// ==========================================
// SIMULATOR 14: Double Circulation & Vessels
// ==========================================
let s14View = 'circuit';

function initSlide14() {
    drawSlide14();
}

function setSlide14View(view) {
    s14View = view;
    const btnC = document.getElementById('s14BtnCircuit');
    const btnV = document.getElementById('s14BtnVessels');
    const btnP = document.getElementById('s14BtnClot');
    const title = document.getElementById('s14Title');
    const desc = document.getElementById('s14Desc');

    btnC.className = view === 'circuit' ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnV.className = view === 'vessels' ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnP.className = view === 'clot' ? 'px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (view === 'circuit') {
        title.textContent = 'Vertebrate Double Circulation';
        desc.textContent = 'Blood passes through the heart twice per complete body circuit: once through the pulmonary circuit (to lungs) and once through the systemic circuit (to body).';
    } else if (view === 'vessels') {
        title.textContent = 'Artery vs Vein Wall Specialization';
        desc.textContent = 'Arteries have thick elastic muscular walls to handle surging systolic pressure without valves; veins have thin walls and one-way valves.';
    } else {
        title.textContent = 'Platelet Clotting & Lymph Drainage';
        desc.textContent = 'Platelets aggregate at injury sites, weaving fibrin networks to seal vascular leaks. Leaked intercellular fluid drains as lymph into lymphatic capillaries.';
    }
    drawSlide14();
}

function drawSlide14() {
    const canvas = document.getElementById('s14Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s14View === 'circuit') {
        // Pulmonary loop (top) and Systemic loop (bottom)
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.ellipse(180, 60, 80, 30, 0, 0, Math.PI * 2);
        ctx.stroke();

        ctx.strokeStyle = '#f43f5e';
        ctx.beginPath();
        ctx.ellipse(180, 140, 80, 30, 0, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Lungs (Pulmonary Circuit)', 180, 65);
        ctx.fillText('Heart Pump', 180, 105);
        ctx.fillText('Body Organs (Systemic Circuit)', 180, 145);
    } else if (s14View === 'vessels') {
        // Artery cross section (thick wall)
        ctx.fillStyle = '#e11d48';
        ctx.beginPath(); ctx.arc(100, 100, 40, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#0f172a';
        ctx.beginPath(); ctx.arc(100, 100, 18, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px sans-serif';
        ctx.fillText('Artery (Thick Wall)', 100, 160);

        // Vein cross section (thin wall with valve)
        ctx.fillStyle = '#0284c7';
        ctx.beginPath(); ctx.arc(260, 100, 40, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#0f172a';
        ctx.beginPath(); ctx.arc(260, 100, 30, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.fillText('Vein (Thin Wall + Valve)', 260, 160);
    } else {
        // Platelet plug
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 4;
        ctx.strokeRect(60, 60, 240, 80);

        ctx.fillStyle = '#f59e0b';
        for (let i = 0; i < 14; i++) {
            ctx.beginPath();
            ctx.arc(160 + (Math.random() - 0.5) * 40, 100 + (Math.random() - 0.5) * 30, 4.5, 0, Math.PI * 2);
            ctx.fill();
        }
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('Platelet Fibrin Clot Sealing Vascular Leak', 180, 175);
    }
}

// ==========================================
// SIMULATOR 15: Plant Xylem & Phloem Transport
// ==========================================
let s15System = 'xylem';

function initSlide15() {
    drawSlide15();
}

function setSlide15System(sys) {
    s15System = sys;
    const btnX = document.getElementById('s15BtnXylem');
    const btnP = document.getElementById('s15BtnPhloem');
    const title = document.getElementById('s15Title');
    const desc = document.getElementById('s15Desc');

    btnX.className = sys === 'xylem' ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnP.className = sys === 'phloem' ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (sys === 'xylem') {
        title.textContent = 'Xylem Water Ascent (Transpiration Pull)';
        desc.textContent = 'Daytime water evaporation from stomata generates negative suction tension that pulls continuous water columns upward through tracheids and vessel elements to tall treetops.';
    } else {
        title.textContent = 'Phloem Bidirectional Translocation';
        desc.textContent = 'Companion cells actively load sucrose into sieve tubes using ATP energy. Osmotic water inflow generates high pressure that drives sap toward lower-pressure storage tissues.';
    }
    drawSlide15();
}

function drawSlide15() {
    const canvas = document.getElementById('s15Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s15System === 'xylem') {
        // Vertical xylem conduit with upward arrows
        ctx.fillStyle = '#1e293b';
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.strokeRect(140, 20, 80, 150);

        // Upward water column arrows
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 2.5;
        for (let y = 140; y >= 40; y -= 30) {
            ctx.beginPath();
            ctx.moveTo(180, y); ctx.lineTo(180, y - 18);
            ctx.lineTo(175, y - 12);
            ctx.moveTo(180, y - 18); ctx.lineTo(185, y - 12);
            ctx.stroke();
        }
        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Transpiration Pull (Unidirectional Ascent)', 180, 185);
    } else {
        // Phloem sieve tube with bidirectional arrows
        ctx.fillStyle = '#1e293b';
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;
        ctx.strokeRect(140, 20, 80, 150);

        // Perforated sieve plates
        ctx.strokeStyle = '#64748b';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(140, 60); ctx.lineTo(220, 60);
        ctx.moveTo(140, 130); ctx.lineTo(220, 130);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#f59e0b';
        ctx.beginPath(); ctx.arc(180, 95, 12, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 9px sans-serif';
        ctx.fillText('ATP', 180, 98);

        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Bidirectional Translocation (Sieve Tubes)', 180, 185);
    }
}

// ==========================================
// SIMULATOR 16: Human Nephron & Plant Excretion
// ==========================================
let s16Tab = 'nephron';

function initSlide16() {
    drawSlide16();
}

function setSlide16Tab(tab) {
    s16Tab = tab;
    const btnN = document.getElementById('s16BtnNephron');
    const btnD = document.getElementById('s16BtnDialysis');
    const btnP = document.getElementById('s16BtnPlant');
    const title = document.getElementById('s16Title');
    const desc = document.getElementById('s16Desc');

    btnN.className = tab === 'nephron' ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnD.className = tab === 'dialysis' ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';
    btnP.className = tab === 'plant' ? 'px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all' : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all';

    if (tab === 'nephron') {
        title.textContent = "Nephron: Glomerulus & Tubule (Figure 5.14)";
        desc.textContent = "High blood pressure forces 180 L of initial filtrate into Bowman's capsule daily. The long coiled tubule reabsorbs >99% of water, glucose, and salts, leaving 1-2 L of concentrated urine.";
    } else if (tab === 'dialysis') {
        title.textContent = 'Artificial Kidney (Hemodialysis Machine)';
        desc.textContent = 'Patient blood passes through semipermeable cellophane tubes immersed in dialysing fluid. Nitrogenous urea diffuses out into dialysate without tubular reabsorption.';
    } else {
        title.textContent = 'Plant Excretory Strategies';
        desc.textContent = 'Plants store metabolic wastes in cellular vacuoles, shed old senescent leaves, deposit gums and resins in old xylem, or exude wastes into surrounding soil.';
    }
    drawSlide16();
}

function drawSlide16() {
    const canvas = document.getElementById('s16Canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.textAlign = 'center';
    if (s16Tab === 'nephron') {
        // Bowman's cup & coiled tubule
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(100, 80, 25, 0.5, 2.5 * Math.PI);
        ctx.stroke();

        // Glomerulus tuft inside
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(100, 80, 14, 0, Math.PI * 2);
        ctx.fill();

        // Convoluted tubule leading to collecting duct
        ctx.beginPath();
        ctx.moveTo(125, 80);
        ctx.bezierCurveTo(150, 40, 180, 120, 210, 80);
        ctx.bezierCurveTo(240, 40, 260, 130, 290, 80);
        ctx.lineTo(290, 160); // collecting duct
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px sans-serif';
        ctx.fillText('Glomerulus (Ultrafiltration)', 100, 125);
        ctx.fillText('Tubular Selective Reabsorption (> 99%)', 210, 35);
        ctx.fillText('Urine (1-2 L)', 290, 175);
    } else if (s16Tab === 'dialysis') {
        // Dialyzer tank with coiled tubes
        ctx.fillStyle = '#0f172a';
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.strokeRect(60, 40, 240, 110);

        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(80, 60); ctx.lineTo(280, 60);
        ctx.moveTo(280, 95); ctx.lineTo(80, 95);
        ctx.moveTo(80, 130); ctx.lineTo(280, 130);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Semipermeable Tubes in Dialysing Fluid (No Reabsorption)', 180, 175);
    } else {
        // Plant showing leaf shedding & resin in old xylem
        ctx.fillStyle = '#78350f';
        ctx.fillRect(160, 50, 40, 110); // trunk

        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(175, 75, 12, 45); // resin in old xylem

        ctx.fillStyle = '#ca8a04';
        ctx.beginPath();
        ctx.ellipse(120, 120, 20, 12, -0.4, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Fallen Yellow Leaves & Resins in Old Xylem', 180, 185);
    }
}
"""

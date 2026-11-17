
// ==========================================
// SIMULATOR MASTER DISPATCHER & LOGIC (CH 13)
// ==========================================

let simAnimFrames = {};

function cancelSimAnim(slideId) {
    if (simAnimFrames[slideId]) {
        cancelAnimationFrame(simAnimFrames[slideId]);
        simAnimFrames[slideId] = null;
    }
}

function initSimulator(slideId) {
    cancelSimAnim(slideId);

    if (slideId === 1) initSim1();
    else if (slideId === 2) initSim2();
    else if (slideId === 3) initSim3();
    else if (slideId === 4) initSim4();
    else if (slideId === 5) initSim5();
    else if (slideId === 6) initSim6();
    else if (slideId === 7) initSim7();
    else if (slideId === 8) initSim8();
    else if (slideId === 9) initSim9();
    else if (slideId === 10) initSim10();
    else if (slideId === 11) initSim11();
    else if (slideId === 12) initSim12();
    else if (slideId === 13) initSim13();
    else if (slideId === 14) initSim14();
    else if (slideId === 15) initSim15();
    else if (slideId === 16) initSim16();
}

// ------------------------------------------
// SIMULATOR 1: Ecosystem Biotic & Abiotic Balance
// ------------------------------------------
let sim1State = { rain: 100, temp: 25, deerX: [80, 220, 360], deerDir: [1, -1, 1], eagleX: 50 };

function initSim1() {
    sim1Update();
    sim1Loop();
}

function sim1Update() {
    const rain = parseInt(document.getElementById('sim1_rain_slider')?.value || 100);
    const temp = parseInt(document.getElementById('sim1_temp_slider')?.value || 25);
    sim1State.rain = rain;
    sim1State.temp = temp;

    const rainTxt = document.getElementById('sim1_rain_txt');
    if (rainTxt) rainTxt.textContent = `${rain} cm`;
    const tempTxt = document.getElementById('sim1_temp_txt');
    if (tempTxt) tempTxt.textContent = `${temp}°C`;

    let biome = 'Temperate Forest';
    let biomass = 7800;
    let herbivores = 45;
    let stability = 92;

    if (rain < 40 && temp > 30) {
        biome = 'Arid Desert';
        biomass = 450;
        herbivores = 8;
        stability = 65;
    } else if (rain > 150 && temp > 22) {
        biome = 'Tropical Rainforest';
        biomass = 14500;
        herbivores = 85;
        stability = 98;
    } else if (rain >= 40 && rain <= 80) {
        biome = 'Grassland Savanna';
        biomass = 3200;
        herbivores = 60;
        stability = 88;
    } else if (temp < 10) {
        biome = 'Boreal Taiga';
        biomass = 4200;
        herbivores = 20;
        stability = 75;
    }

    const bEl = document.getElementById('sim1_val_biome');
    if (bEl) bEl.textContent = biome;
    const bmEl = document.getElementById('sim1_val_biomass');
    if (bmEl) bmEl.textContent = `${biomass.toLocaleString()} kg/ha`;
    const hEl = document.getElementById('sim1_val_herbivores');
    if (hEl) hEl.textContent = `${herbivores} deer/km²`;
    const sEl = document.getElementById('sim1_val_stability');
    if (sEl) sEl.textContent = `Balanced (${stability}%)`;
}

function sim1Reset() {
    const rEl = document.getElementById('sim1_rain_slider');
    if (rEl) rEl.value = 100;
    const tEl = document.getElementById('sim1_temp_slider');
    if (tEl) tEl.value = 25;
    sim1Update();
}

function sim1Loop() {
    const canvas = document.getElementById('sim1_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const skyGrad = ctx.createLinearGradient(0, 0, 0, h * 0.6);
    if (sim1State.temp > 35) {
        skyGrad.addColorStop(0, '#78350f');
        skyGrad.addColorStop(1, '#fed7aa');
    } else if (sim1State.temp < 12) {
        skyGrad.addColorStop(0, '#1e293b');
        skyGrad.addColorStop(1, '#94a3b8');
    } else {
        skyGrad.addColorStop(0, '#0369a1');
        skyGrad.addColorStop(1, '#bae6fd');
    }
    ctx.fillStyle = skyGrad;
    ctx.fillRect(0, 0, w, h * 0.65);

    ctx.beginPath();
    ctx.arc(w - 70, 50, 28, 0, Math.PI * 2);
    ctx.fillStyle = '#fef08a';
    ctx.shadowColor = '#eab308';
    ctx.shadowBlur = 20;
    ctx.fill();
    ctx.shadowBlur = 0;

    const hillGrad = ctx.createLinearGradient(0, h * 0.5, 0, h);
    if (sim1State.rain < 40) {
        hillGrad.addColorStop(0, '#d97706');
        hillGrad.addColorStop(1, '#78350f');
    } else {
        hillGrad.addColorStop(0, '#15803d');
        hillGrad.addColorStop(1, '#14532d');
    }

    ctx.beginPath();
    ctx.moveTo(0, h * 0.65);
    ctx.bezierCurveTo(w * 0.25, h * 0.55, w * 0.5, h * 0.7, w, h * 0.6);
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.closePath();
    ctx.fillStyle = hillGrad;
    ctx.fill();

    const treeCount = Math.floor(sim1State.rain / 18);
    for (let i = 0; i < treeCount; i++) {
        const tx = 30 + i * (w / (treeCount + 1));
        const ty = h * 0.62 + Math.sin(i * 1.5) * 12;
        const th = 30 + (sim1State.rain / 200) * 35;

        ctx.fillStyle = '#78350f';
        ctx.fillRect(tx - 3, ty, 6, th * 0.4);

        ctx.beginPath();
        ctx.arc(tx, ty - th * 0.2, th * 0.4, 0, Math.PI * 2);
        ctx.fillStyle = sim1State.rain < 40 ? '#b45309' : (sim1State.temp < 12 ? '#1e3a1e' : '#22c55e');
        ctx.fill();
    }

    for (let i = 0; i < sim1State.deerX.length; i++) {
        sim1State.deerX[i] += sim1State.deerDir[i] * 0.4;
        if (sim1State.deerX[i] > w - 40) sim1State.deerDir[i] = -1;
        if (sim1State.deerX[i] < 40) sim1State.deerDir[i] = 1;

        const dx = sim1State.deerX[i];
        const dy = h * 0.82 + (i % 2) * 15;

        ctx.font = '18px sans-serif';
        ctx.fillText('🦌', dx, dy);
    }

    sim1State.eagleX = (sim1State.eagleX + 0.8) % (w + 40);
    ctx.font = '16px sans-serif';
    ctx.fillText('🦅', sim1State.eagleX - 20, 60 + Math.sin(sim1State.eagleX * 0.03) * 10);

    simAnimFrames[1] = requestAnimationFrame(sim1Loop);
}

// ------------------------------------------
// SIMULATOR 2: Artificial Aquarium Studio (Activity 13.1)
// ------------------------------------------
let sim2State = {
    aeratorOn: true,
    fishCount: 6,
    wastePpm: 0.15,
    o2Level: 8.2,
    bubbles: [],
    fishList: []
};

function initSim2() {
    sim2State.bubbles = [];
    for (let i = 0; i < 30; i++) {
        sim2State.bubbles.push({
            x: 80 + Math.random() * 40,
            y: Math.random() * 240,
            r: 2 + Math.random() * 4,
            speed: 1 + Math.random() * 2
        });
    }

    sim2State.fishList = [];
    for (let i = 0; i < 15; i++) {
        sim2State.fishList.push({
            x: 100 + Math.random() * 400,
            y: 50 + Math.random() * 160,
            vx: (Math.random() - 0.5) * 1.5,
            vy: (Math.random() - 0.5) * 0.6,
            icon: ['🐠', '🐟', '🐡'][i % 3]
        });
    }

    sim2Update();
    sim2Loop();
}

function sim2ToggleAerator() {
    sim2State.aeratorOn = !sim2State.aeratorOn;
    const btn = document.getElementById('sim2_btn_aerator');
    if (btn) {
        if (sim2State.aeratorOn) {
            btn.className = 'px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold';
            btn.textContent = 'Aerator: ON 🫧';
        } else {
            btn.className = 'px-3 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold';
            btn.textContent = 'Aerator: OFF ⛔';
        }
    }
    sim2Update();
}

function sim2FeedFish() {
    sim2State.wastePpm += 0.25;
    playSuccessChime();
    sim2Update();
}

function sim2CleanTank() {
    sim2State.wastePpm = 0.05;
    playSuccessChime();
    sim2Update();
}

function sim2Update() {
    const fCount = parseInt(document.getElementById('sim2_fish_slider')?.value || 6);
    sim2State.fishCount = fCount;

    const fTxt = document.getElementById('sim2_fish_txt');
    if (fTxt) fTxt.textContent = `${fCount} Fish`;

    if (sim2State.aeratorOn) {
        sim2State.o2Level = Math.max(5.0, 9.2 - fCount * 0.18);
    } else {
        sim2State.o2Level = Math.max(1.8, 5.0 - fCount * 0.35);
    }

    const o2El = document.getElementById('sim2_val_o2');
    if (o2El) {
        const desc = sim2State.o2Level > 6.0 ? 'Optimal' : (sim2State.o2Level > 4.0 ? 'Moderate' : 'Hypoxic Danger');
        o2El.textContent = `${sim2State.o2Level.toFixed(1)} mg/L (${desc})`;
        o2El.className = sim2State.o2Level > 5.0 ? 'text-emerald-400 font-bold text-sm' : 'text-rose-400 font-bold text-sm';
    }

    const wEl = document.getElementById('sim2_val_waste');
    if (wEl) {
        const desc = sim2State.wastePpm < 0.5 ? 'Safe' : (sim2State.wastePpm < 1.0 ? 'Polluted' : 'Lethal Ammonia');
        wEl.textContent = `${sim2State.wastePpm.toFixed(2)} ppm (${desc})`;
        wEl.className = sim2State.wastePpm < 0.5 ? 'text-amber-400 font-bold text-sm' : 'text-rose-400 font-bold text-sm';
    }

    const sEl = document.getElementById('sim2_val_status');
    if (sEl) {
        if (!sim2State.aeratorOn && sim2State.o2Level < 3.5) {
            sEl.textContent = 'Fish Suffocation Warning!';
            sEl.className = 'text-rose-500 font-bold text-sm';
        } else if (sim2State.wastePpm > 0.8) {
            sEl.textContent = 'Requires Water Change 🧼';
            sEl.className = 'text-amber-400 font-bold text-sm';
        } else {
            sEl.textContent = 'Healthy Aquarium';
            sEl.className = 'text-cyan-400 font-bold text-sm';
        }
    }
}

function sim2Loop() {
    const canvas = document.getElementById('sim2_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const waterGrad = ctx.createLinearGradient(0, 20, 0, h - 20);
    if (sim2State.wastePpm > 0.8) {
        waterGrad.addColorStop(0, '#1e293b');
        waterGrad.addColorStop(1, '#064e3b');
    } else {
        waterGrad.addColorStop(0, '#0284c7');
        waterGrad.addColorStop(1, '#082f49');
    }
    ctx.fillStyle = waterGrad;
    ctx.fillRect(10, 20, w - 20, h - 40);

    ctx.lineWidth = 4;
    ctx.strokeStyle = '#38bdf8';
    ctx.strokeRect(10, 20, w - 20, h - 40);

    ctx.fillStyle = '#78350f';
    ctx.fillRect(10, h - 35, w - 20, 15);

    ctx.fillStyle = '#64748b';
    ctx.fillRect(80, h - 45, 40, 10);

    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 3;
    for (let x = w - 120; x < w - 40; x += 25) {
        ctx.beginPath();
        ctx.moveTo(x, h - 35);
        ctx.quadraticCurveTo(x + 15 * Math.sin(Date.now() * 0.002 + x), h - 90, x, h - 140);
        ctx.stroke();
    }

    if (sim2State.aeratorOn) {
        ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
        for (let b of sim2State.bubbles) {
            b.y -= b.speed;
            if (b.y < 30) b.y = h - 45;
            b.x += Math.sin(b.y * 0.08) * 0.5;

            ctx.beginPath();
            ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    const activeFish = sim2State.fishList.slice(0, sim2State.fishCount);
    for (let f of activeFish) {
        f.x += f.vx;
        f.y += f.vy;

        if (f.x < 30 || f.x > w - 50) f.vx *= -1;
        if (f.y < 40 || f.y > h - 60) f.vy *= -1;

        ctx.font = '24px sans-serif';
        ctx.save();
        ctx.translate(f.x, f.y);
        if (f.vx < 0) ctx.scale(-1, 1);
        ctx.fillText(f.icon, 0, 0);
        ctx.restore();
    }

    simAnimFrames[2] = requestAnimationFrame(sim2Loop);
}

// ------------------------------------------
// SIMULATOR 3: Ecological Trophic Roles Lab
// ------------------------------------------
function initSim3() {
    sim3Update();
}

function sim3Update() {
    const organism = document.getElementById('sim3_sel_organism')?.value || 'producer';
    const sunlight = parseInt(document.getElementById('sim3_sun_slider')?.value || 80);
    const sunTxt = document.getElementById('sim3_sun_txt');
    if (sunTxt) sunTxt.textContent = `${sunlight}%`;

    const canvas = document.getElementById('sim3_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    let mode = 'Photoautotrophic';
    let source = 'Solar Photons + CO₂';
    let chloro = 'Active Chloroplasts';
    let rank = 'Trophic Level 1';

    if (organism === 'producer') {
        mode = 'Photoautotrophic';
        source = 'Solar Photons + CO₂';
        chloro = 'Active Chloroplasts';
        rank = 'Trophic Level 1';

        ctx.fillStyle = '#fef08a';
        ctx.beginPath();
        ctx.arc(100, 60, 30, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#eab308';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(130, 80);
        ctx.lineTo(w * 0.5, h * 0.5);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.font = '80px sans-serif';
        ctx.fillText('🌿', w * 0.5 - 40, h * 0.7);

        ctx.fillStyle = '#38bdf8';
        ctx.font = '13px monospace';
        ctx.fillText('6 CO₂ + 6 H₂O + Light ➔ C₆H₁₂O₆ + 6 O₂', w * 0.5 - 130, h * 0.88);

    } else if (organism === 'herbivore') {
        mode = 'Holozoic Herbivore';
        source = 'Plant Cellulose Biomass';
        chloro = 'Zero (Heterotroph)';
        rank = 'Trophic Level 2';

        ctx.font = '60px sans-serif';
        ctx.fillText('🌾', 120, h * 0.65);
        ctx.fillText('➔', 220, h * 0.6);
        ctx.fillText('🦗', 300, h * 0.65);

        ctx.fillStyle = '#34d399';
        ctx.font = '13px monospace';
        ctx.fillText('Ingesting producer foliage -> Primary Consumer', w * 0.5 - 140, h * 0.88);

    } else if (organism === 'carnivore') {
        mode = 'Holozoic Carnivore';
        source = 'Animal Herbivore Tissues';
        chloro = 'Zero (Heterotroph)';
        rank = 'Trophic Level 3';

        ctx.font = '60px sans-serif';
        ctx.fillText('🦗', 120, h * 0.65);
        ctx.fillText('➔', 220, h * 0.6);
        ctx.fillText('🐸', 300, h * 0.65);

        ctx.fillStyle = '#38bdf8';
        ctx.font = '13px monospace';
        ctx.fillText('Preying upon primary herbivores -> Secondary Consumer', w * 0.5 - 160, h * 0.88);

    } else if (organism === 'parasite') {
        mode = 'Ectoparasitic Fluid Feeding';
        source = 'Host Plant Vascular Sap';
        chloro = 'Zero (Non-photosynthetic)';
        rank = 'Specialized Heterotroph';

        ctx.font = '70px sans-serif';
        ctx.fillText('🌳', 160, h * 0.65);

        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(170, h * 0.35);
        ctx.bezierCurveTo(230, h * 0.45, 170, h * 0.55, 210, h * 0.65);
        ctx.stroke();

        ctx.fillStyle = '#facc15';
        ctx.font = '13px monospace';
        ctx.fillText('Cuscuta (Amarbel) Haustoria sucking host sap', w * 0.5 - 130, h * 0.88);
    }

    const mEl = document.getElementById('sim3_val_mode');
    if (mEl) mEl.textContent = mode;
    const sEl = document.getElementById('sim3_val_source');
    if (sEl) sEl.textContent = source;
    const cEl = document.getElementById('sim3_val_chloro');
    if (cEl) cEl.textContent = chloro;
    const rEl = document.getElementById('sim3_val_rank');
    if (rEl) rEl.textContent = rank;
}

// ------------------------------------------
// SIMULATOR 4: Decomposer Mineralization Engine
// ------------------------------------------
let sim4State = { enzymes: true, waste: 50, micro: 3 };

function initSim4() {
    sim4Update();
}

function sim4ToggleEnzymes() {
    sim4State.enzymes = !sim4State.enzymes;
    const btn = document.getElementById('sim4_btn_enz');
    if (btn) {
        btn.textContent = sim4State.enzymes ? 'Enzymes: ON' : 'Enzymes: OFF';
        btn.className = sim4State.enzymes ? 'px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold' : 'px-2.5 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold';
    }
    sim4Update();
}

function sim4Update() {
    sim4State.waste = parseInt(document.getElementById('sim4_waste_slider')?.value || 50);
    sim4State.micro = parseInt(document.getElementById('sim4_micro_slider')?.value || 3);

    const wTxt = document.getElementById('sim4_waste_txt');
    if (wTxt) wTxt.textContent = `${sim4State.waste} kg`;
    const mTxt = document.getElementById('sim4_micro_txt');
    if (mTxt) mTxt.textContent = `${sim4State.micro}× Density`;

    const canvas = document.getElementById('sim4_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const soilGrad = ctx.createLinearGradient(0, 80, 0, h);
    soilGrad.addColorStop(0, '#78350f');
    soilGrad.addColorStop(1, '#451a03');
    ctx.fillStyle = soilGrad;
    ctx.fillRect(0, 80, w, h - 80);

    ctx.strokeStyle = '#fef08a';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(w * 0.75, 40);
    ctx.lineTo(w * 0.75, 120);
    ctx.lineTo(w * 0.65, 180);
    ctx.moveTo(w * 0.75, 120);
    ctx.lineTo(w * 0.85, 200);
    ctx.stroke();

    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(w * 0.75, 80);
    ctx.lineTo(w * 0.75, 20);
    ctx.stroke();
    ctx.font = '28px sans-serif';
    ctx.fillText('🌱', w * 0.75 - 14, 25);

    ctx.font = '24px sans-serif';
    ctx.fillText('🍂 🪵 🦴 💩', 40, 75);

    ctx.fillStyle = '#38bdf8';
    for (let i = 0; i < sim4State.micro * 15; i++) {
        const mx = 60 + (i * 27) % 300;
        const my = 100 + (i * 17) % 120;
        ctx.beginPath();
        ctx.arc(mx, my, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    if (sim4State.enzymes) {
        ctx.fillStyle = '#f59e0b';
        ctx.font = '12px monospace';
        ctx.fillText('NO₃⁻', 180, 140);
        ctx.fillText('PO₄³⁻', 240, 160);
        ctx.fillText('K⁺', 320, 130);

        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(340, 130);
        ctx.lineTo(w * 0.75, 160);
        ctx.stroke();
        ctx.setLineDash([]);
    }

    const rate = sim4State.enzymes ? (sim4State.micro * 1.6).toFixed(1) : '0.0';
    const npk = sim4State.enzymes ? (sim4State.micro * 110 + sim4State.waste * 1.5).toFixed(0) : '35';

    const rEl = document.getElementById('sim4_val_rate');
    if (rEl) rEl.textContent = `${rate} kg/day`;
    const nEl = document.getElementById('sim4_val_npk');
    if (nEl) nEl.textContent = `${npk} mg/kg`;
    const hEl = document.getElementById('sim4_val_humus');
    if (hEl) hEl.textContent = sim4State.enzymes ? 'Rich Humus (6.2%)' : 'Depleted (0.8%)';
    const sEl = document.getElementById('sim4_val_status');
    if (sEl) sEl.textContent = sim4State.enzymes ? 'Actively Replenished' : 'Nutrient Locked!';
}

// ------------------------------------------
// SIMULATOR 5: 4-Tier Food Chain Simulator
// ------------------------------------------
let sim5Disrupted = false;

function initSim5() {
    sim5UpdateChain();
}

function sim5ToggleDisruption() {
    sim5Disrupted = !sim5Disrupted;
    const btn = document.getElementById('sim5_btn_disrupt');
    if (btn) {
        btn.textContent = sim5Disrupted ? 'Restore Food Chain 🔄' : 'Remove Intermediate Tier ⚡';
        btn.className = sim5Disrupted ? 'px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold' : 'px-3 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold';
    }
    if (sim5Disrupted) playErrorBuzz();
    else playSuccessChime();
    sim5UpdateChain();
}

function sim5UpdateChain() {
    const chain = document.getElementById('sim5_sel_chain')?.value || 'grassland';
    const canvas = document.getElementById('sim5_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    let icons = ['🌿 Grass', '🦗 Insect', '🐸 Frog', '🐍 Snake', '🦅 Hawk'];
    if (chain === 'forest') {
        icons = ['🌳 Forest Tree', '🦌 Herbivore Deer', '🐅 Apex Tiger'];
    } else if (chain === 'pond') {
        icons = ['🦠 Phytoplankton', '🦐 Zooplankton', '🐟 Small Fish', '🦩 Crane Bird'];
    }

    const n = icons.length;
    const step = (w - 60) / n;

    for (let i = 0; i < n; i++) {
        const x = 30 + i * step + step * 0.5;
        const y = h * 0.5;

        const isDisruptedTier = (sim5Disrupted && i === Math.floor(n / 2));

        ctx.fillStyle = isDisruptedTier ? '#e11d48' : '#1e293b';
        ctx.strokeStyle = isDisruptedTier ? '#fda4af' : '#38bdf8';
        ctx.lineWidth = 2;

        ctx.beginPath();
        ctx.roundRect(x - 45, y - 40, 90, 80, 12);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#f8fafc';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(icons[i], x, y + 5);

        if (isDisruptedTier) {
            ctx.strokeStyle = '#f43f5e';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(x - 35, y - 30);
            ctx.lineTo(x + 35, y + 30);
            ctx.moveTo(x + 35, y - 30);
            ctx.lineTo(x - 35, y + 30);
            ctx.stroke();
        }

        if (i < n - 1) {
            const nextX = 30 + (i + 1) * step + step * 0.5;
            ctx.strokeStyle = isDisruptedTier ? '#94a3b8' : '#34d399';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(x + 45, y);
            ctx.lineTo(nextX - 45, y);
            ctx.stroke();

            ctx.fillStyle = isDisruptedTier ? '#94a3b8' : '#34d399';
            ctx.beginPath();
            ctx.moveTo(nextX - 45, y);
            ctx.lineTo(nextX - 55, y - 5);
            ctx.lineTo(nextX - 55, y + 5);
            ctx.fill();
        }
    }
    ctx.textAlign = 'start';

    const t1El = document.getElementById('sim5_val_t1');
    const t2El = document.getElementById('sim5_val_t2');
    const t3El = document.getElementById('sim5_val_t3');
    const t4El = document.getElementById('sim5_val_t4');

    if (sim5Disrupted) {
        if (t1El) t1El.textContent = 'Overgrazed / Collapsing';
        if (t2El) t2El.textContent = 'Uncontrolled Outbreak';
        if (t3El) t3El.textContent = 'EXTIRPATED (0)';
        if (t4El) t4El.textContent = 'Starving to Death';
    } else {
        if (t1El) t1El.textContent = 'Healthy Abundance';
        if (t2El) t2El.textContent = 'Regulated Herbivory';
        if (t3El) t3El.textContent = 'Active Predation';
        if (t4El) t4El.textContent = 'Sustained Population';
    }
}

// ------------------------------------------
// SIMULATOR 6: Solar Energy 1% Photochemical Capture
// ------------------------------------------
function initSim6() {
    sim6Update();
}

function sim6Update() {
    const solar = parseInt(document.getElementById('sim6_solar_slider')?.value || 1000000);
    const canopy = parseInt(document.getElementById('sim6_canopy_slider')?.value || 100);

    const sTxt = document.getElementById('sim6_solar_txt');
    if (sTxt) sTxt.textContent = `${solar.toLocaleString()} J`;
    const cTxt = document.getElementById('sim6_canopy_txt');
    if (cTxt) cTxt.textContent = `${canopy}%`;

    const captured = Math.round(solar * 0.01 * (canopy / 100));
    const lost = solar - captured;

    const capEl = document.getElementById('sim6_val_captured');
    if (capEl) capEl.textContent = `${captured.toLocaleString()} J`;
    const lostEl = document.getElementById('sim6_val_lost');
    if (lostEl) lostEl.textContent = `${lost.toLocaleString()} J`;

    const canvas = document.getElementById('sim6_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = '#fef08a';
    ctx.shadowColor = '#eab308';
    ctx.shadowBlur = 25;
    ctx.beginPath();
    ctx.arc(80, 70, 35, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    ctx.fillStyle = '#ca8a04';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText('SUN 100%', 52, 74);

    ctx.fillStyle = '#15803d';
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.ellipse(w * 0.6, h * 0.6, 120, 60, Math.PI * 0.1, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(115, 70);
    ctx.lineTo(w * 0.55, h * 0.45);
    ctx.lineTo(w * 0.85, 40);
    ctx.stroke();

    ctx.fillStyle = '#f43f5e';
    ctx.font = '12px monospace';
    ctx.fillText('99% Reflected / Heat / Transpiration', w * 0.45, 35);

    ctx.strokeStyle = '#4ade80';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(115, 80);
    ctx.lineTo(w * 0.6, h * 0.6);
    ctx.stroke();

    ctx.fillStyle = '#4ade80';
    ctx.font = 'bold 13px monospace';
    ctx.fillText(`1% Captured = ${captured.toLocaleString()} J`, w * 0.5, h * 0.85);
}

// ------------------------------------------
// SIMULATOR 7: Lindeman 10% Trophic Energy Pyramid
// ------------------------------------------
function initSim7() {
    sim7Update();
}

function sim7Update() {
    const e1 = parseInt(document.getElementById('sim7_energy_slider')?.value || 10000);

    const eTxt = document.getElementById('sim7_energy_txt');
    if (eTxt) eTxt.textContent = `${e1.toLocaleString()} J`;

    const e2 = Math.round(e1 * 0.10);
    const e3 = Math.round(e2 * 0.10);
    const e4 = Math.round(e3 * 0.10);
    const heat = e1 - e4;

    const t2El = document.getElementById('sim7_val_t2');
    if (t2El) t2El.textContent = `${e2.toLocaleString()} J (10%)`;
    const t3El = document.getElementById('sim7_val_t3');
    if (t3El) t3El.textContent = `${e3.toLocaleString()} J (1%)`;
    const t4El = document.getElementById('sim7_val_t4');
    if (t4El) t4El.textContent = `${e4.toLocaleString()} J (0.1%)`;
    const hEl = document.getElementById('sim7_val_heat');
    if (hEl) hEl.textContent = `${heat.toLocaleString()} J Lost`;

    const canvas = document.getElementById('sim7_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const levels = [
        { label: `T1: Producers (${e1.toLocaleString()} J)`, val: e1, color: '#16a34a', w: 420 },
        { label: `T2: Herbivores (${e2.toLocaleString()} J)`, val: e2, color: '#0d9488', w: 300 },
        { label: `T3: Carnivores (${e3.toLocaleString()} J)`, val: e3, color: '#0284c7', w: 180 },
        { label: `T4: Apex (${e4.toLocaleString()} J)`, val: e4, color: '#eab308', w: 80 }
    ];

    const th = 40;
    const startY = h - 50;

    for (let i = 0; i < levels.length; i++) {
        const lvl = levels[i];
        const y = startY - i * (th + 10);
        const lw = lvl.w;
        const x = (w - lw) / 2;

        ctx.fillStyle = lvl.color;
        ctx.beginPath();
        ctx.roundRect(x, y, lw, th, 8);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(lvl.label, w * 0.5, y + 24);

        if (i < levels.length - 1) {
            ctx.fillStyle = '#f43f5e';
            ctx.font = '10px monospace';
            ctx.textAlign = 'left';
            ctx.fillText(`🔥 90% lost`, x + lw + 12, y + 24);
        }
    }
    ctx.textAlign = 'start';
}

// ------------------------------------------
// SIMULATOR 8: Interconnected Food Web Graph
// ------------------------------------------
let sim8Shock = 'none';

function initSim8() {
    sim8Draw();
}

function sim8ApplyShock() {
    sim8Shock = document.getElementById('sim8_sel_shock')?.value || 'none';
    if (sim8Shock !== 'none') playErrorBuzz();
    else playSuccessChime();
    sim8Draw();
}

function sim8ResetWeb() {
    const sEl = document.getElementById('sim8_sel_shock');
    if (sEl) sEl.value = 'none';
    sim8Shock = 'none';
    sim8Draw();
}

function sim8Draw() {
    const canvas = document.getElementById('sim8_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const nodes = {
        grass: { x: 80, y: 200, name: '🌿 Grass', dead: false },
        shrub: { x: 80, y: 80, name: '🌱 Shrub', dead: false },
        insect: { x: 230, y: 70, name: '🦗 Insect', dead: sim8Shock === 'insect_blight' },
        mouse: { x: 230, y: 150, name: '🐁 Mouse', dead: sim8Shock === 'rodent_decline' },
        rabbit: { x: 230, y: 220, name: '🐇 Rabbit', dead: false },
        frog: { x: 380, y: 80, name: '🐸 Frog', dead: sim8Shock === 'frog_decline' },
        snake: { x: 380, y: 180, name: '🐍 Snake', dead: false },
        hawk: { x: 520, y: 130, name: '🦅 Hawk', dead: false }
    };

    const links = [
        ['grass', 'rabbit'],
        ['grass', 'mouse'],
        ['shrub', 'insect'],
        ['shrub', 'rabbit'],
        ['insect', 'frog'],
        ['mouse', 'snake'],
        ['frog', 'snake'],
        ['rabbit', 'hawk'],
        ['snake', 'hawk'],
        ['mouse', 'hawk']
    ];

    for (let [from, to] of links) {
        const n1 = nodes[from];
        const n2 = nodes[to];

        ctx.lineWidth = 2;
        if (n1.dead || n2.dead) {
            ctx.strokeStyle = '#475569';
            ctx.setLineDash([4, 4]);
        } else {
            ctx.strokeStyle = '#22c55e';
            ctx.setLineDash([]);
        }

        ctx.beginPath();
        ctx.moveTo(n1.x, n1.y);
        ctx.lineTo(n2.x, n2.y);
        ctx.stroke();
        ctx.setLineDash([]);
    }

    for (let key in nodes) {
        const n = nodes[key];
        ctx.fillStyle = n.dead ? '#be123c' : '#0f172a';
        ctx.strokeStyle = n.dead ? '#fda4af' : '#38bdf8';
        ctx.lineWidth = 2;

        ctx.beginPath();
        ctx.roundRect(n.x - 35, n.y - 18, 70, 36, 8);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = '10px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(n.name, n.x, n.y + 4);
    }
    ctx.textAlign = 'start';

    const shiftEl = document.getElementById('sim8_val_shift');
    const casEl = document.getElementById('sim8_val_cascade');
    if (sim8Shock !== 'none') {
        if (shiftEl) shiftEl.textContent = 'Predators switched to alternative prey';
        if (casEl) casEl.textContent = 'Shock Buffered by Web Links';
    } else {
        if (shiftEl) shiftEl.textContent = 'Balanced across all links';
        if (casEl) casEl.textContent = 'Zero Disruption';
    }
}

// ------------------------------------------
// SIMULATOR 9: Unidirectional Energy Flow vs Cycles
// ------------------------------------------
function initSim9() {
    sim9Update();
}

function sim9Update() {
    const mode = document.getElementById('sim9_sel_mode')?.value || 'both';
    const solar = parseInt(document.getElementById('sim9_solar_slider')?.value || 100);
    const sTxt = document.getElementById('sim9_solar_txt');
    if (sTxt) sTxt.textContent = `${solar}%`;

    const canvas = document.getElementById('sim9_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    if (mode === 'energy' || mode === 'both') {
        // Linear One-Way Flow on top half
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('ENERGY: Strictly Unidirectional One-Way Flow', 30, 30);

        const eSteps = ['☀️ Sun', '🌿 Plants', '🦌 Deer', '🐅 Tiger', '🔥 Heat'];
        for (let i = 0; i < eSteps.length; i++) {
            const x = 50 + i * 115;
            const y = 65;

            ctx.fillStyle = (i === 4) ? '#f43f5e' : '#1e293b';
            ctx.strokeStyle = (i === 4) ? '#fda4af' : '#eab308';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(x - 40, y - 18, 80, 36, 8);
            ctx.fill();
            ctx.stroke();

            ctx.fillStyle = '#ffffff';
            ctx.font = '11px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(eSteps[i], x, y + 5);

            if (i < eSteps.length - 1) {
                ctx.strokeStyle = '#eab308';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(x + 40, y);
                ctx.lineTo(x + 75, y);
                ctx.stroke();
            }
        }
        ctx.textAlign = 'start';
    }

    if (mode === 'nutrients' || mode === 'both') {
        // Cyclic Loop on bottom half
        const cy = (mode === 'both') ? h * 0.72 : h * 0.5;
        const cx = w * 0.5;
        const r = 60;

        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('MINERAL NUTRIENTS (N, P, K): Closed Biogeochemical Cycle', 30, (mode === 'both') ? h * 0.45 : 30);

        ctx.strokeStyle = '#22c55e';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();

        const nSteps = [
            { label: 'Soil NPK', angle: 0 },
            { label: 'Plant Roots', angle: Math.PI * 0.5 },
            { label: 'Animals', angle: Math.PI },
            { label: 'Decomposers', angle: Math.PI * 1.5 }
        ];

        for (let ns of nSteps) {
            const nx = cx + Math.cos(ns.angle) * r;
            const ny = cy + Math.sin(ns.angle) * r;

            ctx.fillStyle = '#0f172a';
            ctx.strokeStyle = '#34d399';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(nx - 40, ny - 14, 80, 28, 6);
            ctx.fill();
            ctx.stroke();

            ctx.fillStyle = '#34d399';
            ctx.font = '10px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(ns.label, nx, ny + 4);
        }
        ctx.textAlign = 'start';
    }
}

// ------------------------------------------
// SIMULATOR 10: Biological Toxic Magnification
// ------------------------------------------
function initSim10() {
    sim10Update();
}

function sim10Update() {
    const baseToxin = parseInt(document.getElementById('sim10_toxin_slider')?.value || 2) * 0.01;
    const tTxt = document.getElementById('sim10_toxin_txt');
    if (tTxt) tTxt.textContent = `${baseToxin.toFixed(2)} ppb`;

    const canvas = document.getElementById('sim10_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const levels = [
        { name: '💧 Water', val: `${baseToxin.toFixed(2)} ppb`, ppm: baseToxin * 0.001, color: '#38bdf8', dots: 2 },
        { name: '🦠 Plankton', val: `${(baseToxin * 20).toFixed(2)} ppm`, ppm: baseToxin * 20, color: '#34d399', dots: 10 },
        { name: '🐟 Small Fish', val: `${(baseToxin * 250).toFixed(1)} ppm`, ppm: baseToxin * 250, color: '#fbbf24', dots: 30 },
        { name: '🦈 Large Fish', val: `${(baseToxin * 1000).toFixed(0)} ppm`, ppm: baseToxin * 1000, color: '#fb923c', dots: 70 },
        { name: '🧍 Human / Hawk', val: `${(baseToxin * 12500).toFixed(0)} ppm`, ppm: baseToxin * 12500, color: '#f43f5e', dots: 150 }
    ];

    const stepW = (w - 60) / levels.length;

    for (let i = 0; i < levels.length; i++) {
        const lvl = levels[i];
        const barH = 35 + i * 38;
        const x = 30 + i * stepW + 10;
        const y = h - 40 - barH;

        ctx.fillStyle = lvl.color;
        ctx.beginPath();
        ctx.roundRect(x, y, stepW - 20, barH, 8);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(lvl.name, x + (stepW - 20) * 0.5, h - 20);

        ctx.font = 'bold 10px monospace';
        ctx.fillStyle = '#fecdd3';
        ctx.fillText(lvl.val, x + (stepW - 20) * 0.5, y - 8);

        // Toxic red dots inside bar
        ctx.fillStyle = '#ef4444';
        for (let d = 0; d < Math.min(lvl.dots, 60); d++) {
            const rx = x + 6 + (d * 11) % (stepW - 32);
            const ry = y + 8 + Math.floor(d / 4) * 8;
            if (ry < h - 45) {
                ctx.beginPath();
                ctx.arc(rx, ry, 2.5, 0, Math.PI * 2);
                ctx.fill();
            }
        }
    }
    ctx.textAlign = 'start';
}

// ------------------------------------------
// SIMULATOR 11: Pesticide Surface Wash vs Systemic Residue
// ------------------------------------------
let sim11State = { treatment: 'raw' };

function initSim11() {
    sim11ApplyTreatment();
}

function sim11ApplyTreatment() {
    sim11State.treatment = document.getElementById('sim11_sel_treatment')?.value || 'raw';
    sim11Draw();
}

function sim11Reset() {
    const tEl = document.getElementById('sim11_sel_treatment');
    if (tEl) tEl.value = 'raw';
    sim11State.treatment = 'raw';
    sim11Draw();
}

function sim11Draw() {
    const canvas = document.getElementById('sim11_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const cx = w * 0.5;
    const cy = h * 0.5;

    // Outer vegetable skin (Tomato)
    ctx.fillStyle = '#dc2626';
    ctx.beginPath();
    ctx.arc(cx, cy, 75, 0, Math.PI * 2);
    ctx.fill();

    // Inner vascular edible pulp
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(cx, cy, 62, 0, Math.PI * 2);
    ctx.fill();

    // Vascular Seed Pockets
    ctx.fillStyle = '#b91c1c';
    ctx.beginPath();
    ctx.ellipse(cx - 25, cy - 15, 18, 10, 0.4, 0, Math.PI * 2);
    ctx.ellipse(cx + 25, cy - 15, 18, 10, -0.4, 0, Math.PI * 2);
    ctx.ellipse(cx, cy + 28, 20, 12, 0, 0, Math.PI * 2);
    ctx.fill();

    let surfaceRemain = 100;
    let systemicRemain = 100;

    if (sim11State.treatment === 'tap_water') {
        surfaceRemain = 25;
        systemicRemain = 100;
    } else if (sim11State.treatment === 'salt_soak') {
        surfaceRemain = 10;
        systemicRemain = 95;
    } else if (sim11State.treatment === 'peeled') {
        surfaceRemain = 0;
        systemicRemain = 85;
    }

    // Draw Surface Pesticide Dots (Yellow)
    const surfCount = Math.floor(surfaceRemain * 0.35);
    ctx.fillStyle = '#facc15';
    for (let i = 0; i < surfCount; i++) {
        const angle = (i / surfCount) * Math.PI * 2;
        const px = cx + Math.cos(angle) * 72;
        const py = cy + Math.sin(angle) * 72;
        ctx.beginPath();
        ctx.arc(px, py, 3, 0, Math.PI * 2);
        ctx.fill();
    }

    // Draw Internal Systemic Pesticide Dots (Purple)
    const sysCount = Math.floor(systemicRemain * 0.25);
    ctx.fillStyle = '#c084fc';
    for (let i = 0; i < sysCount; i++) {
        const angle = i * 2.3;
        const dist = 15 + (i * 9) % 45;
        const px = cx + Math.cos(angle) * dist;
        const py = cy + Math.sin(angle) * dist;
        ctx.beginPath();
        ctx.arc(px, py, 3, 0, Math.PI * 2);
        ctx.fill();
    }

    // Annotations
    ctx.fillStyle = '#facc15';
    ctx.font = '11px sans-serif';
    ctx.fillText(`Surface Spray: ${surfaceRemain}%`, 30, 60);

    ctx.fillStyle = '#c084fc';
    ctx.fillText(`Systemic Absorbed Residue: ${systemicRemain}%`, 30, 90);

    const sEl = document.getElementById('sim11_val_surface');
    if (sEl) sEl.textContent = `${surfaceRemain}% Remaining`;
    const sysEl = document.getElementById('sim11_val_systemic');
    if (sysEl) sysEl.textContent = `${systemicRemain}% Embedded`;
    const dEl = document.getElementById('sim11_val_decon');
    if (dEl) dEl.textContent = `${100 - Math.round((surfaceRemain + systemicRemain) / 2)}% Cleared`;
    const safEl = document.getElementById('sim11_val_safety');
    if (safEl) {
        if (systemicRemain > 80) {
            safEl.textContent = 'Systemic Hazard Remains!';
            safEl.className = 'text-rose-500 font-bold text-sm';
        } else {
            safEl.textContent = 'Partially Reduced';
            safEl.className = 'text-amber-400 font-bold text-sm';
        }
    }
}

// ------------------------------------------
// SIMULATOR 12: Two-Step Ozone Photochemical Synthesis
// ------------------------------------------
let sim12Step = 1;

function initSim12() {
    sim12Update();
}

function sim12TriggerPhoton() {
    sim12Step = (sim12Step === 1) ? 2 : 1;
    playSuccessChime();
    sim12Update();
}

function sim12Update() {
    const uv = parseInt(document.getElementById('sim12_uv_slider')?.value || 70);
    const alt = parseInt(document.getElementById('sim12_alt_slider')?.value || 25);

    const uvTxt = document.getElementById('sim12_uv_txt');
    if (uvTxt) uvTxt.textContent = `${uv}% UV`;
    const altTxt = document.getElementById('sim12_alt_txt');
    if (altTxt) altTxt.textContent = `${alt} km`;

    const canvas = document.getElementById('sim12_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    if (sim12Step === 1) {
        // Step 1: O2 + UV -> O + O
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('STEP 1: High-Energy UV Photolysis (O₂ + UV ➔ O + O)', 30, 30);

        // O2 Molecule
        ctx.fillStyle = '#0ea5e9';
        ctx.beginPath();
        ctx.arc(150, h * 0.5, 24, 0, Math.PI * 2);
        ctx.arc(186, h * 0.5, 24, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 14px sans-serif';
        ctx.fillText('O', 144, h * 0.5 + 5);
        ctx.fillText('O', 180, h * 0.5 + 5);

        // Incoming UV Ray
        ctx.strokeStyle = '#f43f5e';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(30, 40);
        ctx.lineTo(168, h * 0.5);
        ctx.stroke();

        ctx.fillStyle = '#f43f5e';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('⚡ UV Photon', 80, 80);

        // Arrow
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(240, h * 0.5);
        ctx.lineTo(320, h * 0.5);
        ctx.stroke();

        // 2 Free Nascent O Atoms
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(380, h * 0.38, 22, 0, Math.PI * 2);
        ctx.arc(460, h * 0.62, 22, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.fillText('O', 374, h * 0.38 + 5);
        ctx.fillText('O', 454, h * 0.62 + 5);

    } else {
        // Step 2: O + O2 -> O3
        ctx.fillStyle = '#34d399';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText('STEP 2: Ozone Synthesis (O + O₂ ➔ O₃ Triatomic Molecule)', 30, 30);

        // Nascent O
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(120, h * 0.5, 22, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 14px sans-serif';
        ctx.fillText('O', 114, h * 0.5 + 5);

        ctx.fillStyle = '#f8fafc';
        ctx.fillText('+', 170, h * 0.5 + 5);

        // O2 Molecule
        ctx.fillStyle = '#0ea5e9';
        ctx.beginPath();
        ctx.arc(220, h * 0.5, 22, 0, Math.PI * 2);
        ctx.arc(254, h * 0.5, 22, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.fillText('O', 214, h * 0.5 + 5);
        ctx.fillText('O', 248, h * 0.5 + 5);

        // Arrow
        ctx.strokeStyle = '#34d399';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(300, h * 0.5);
        ctx.lineTo(370, h * 0.5);
        ctx.stroke();

        // Triatomic Ozone O3 Molecule (Bent structure)
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(440, h * 0.42, 22, 0, Math.PI * 2);
        ctx.arc(474, h * 0.62, 22, 0, Math.PI * 2);
        ctx.arc(412, h * 0.62, 22, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.fillText('O', 434, h * 0.42 + 5);
        ctx.fillText('O', 468, h * 0.62 + 5);
        ctx.fillText('O', 406, h * 0.62 + 5);

        ctx.fillStyle = '#10b981';
        ctx.font = 'bold 14px sans-serif';
        ctx.fillText('Ozone (O₃)', 410, h * 0.88);
    }
}

// ------------------------------------------
// SIMULATOR 13: CFC Catalytic Ozone Depletion
// ------------------------------------------
let sim13Montreal = true;

function initSim13() {
    sim13Update();
}

function sim13ToggleMontreal() {
    sim13Montreal = !sim13Montreal;
    const btn = document.getElementById('sim13_btn_protocol');
    if (btn) {
        btn.textContent = sim13Montreal ? 'Montreal Protocol: ACTIVE 📜' : 'Montreal Protocol: INACTIVE ⛔';
        btn.className = sim13Montreal ? 'px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold' : 'px-3 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold';
    }
    sim13Update();
}

function sim13Update() {
    const year = parseInt(document.getElementById('sim13_year_slider')?.value || 1987);
    const yTxt = document.getElementById('sim13_year_txt');
    if (yTxt) yTxt.textContent = year;

    let cfcPpt = 550;
    let holeArea = 24.5;

    if (sim13Montreal) {
        if (year <= 1995) {
            cfcPpt = 300 + (year - 1980) * 20;
            holeArea = 10 + (year - 1980) * 1.0;
        } else {
            cfcPpt = Math.max(120, 600 - (year - 1995) * 8);
            holeArea = Math.max(2.0, 25 - (year - 1995) * 0.45);
        }
    } else {
        cfcPpt = 300 + (year - 1980) * 35;
        holeArea = Math.min(45, 10 + (year - 1980) * 0.8);
    }

    const cfcEl = document.getElementById('sim13_val_cfc');
    if (cfcEl) cfcEl.textContent = `${cfcPpt} ppt`;
    const holeEl = document.getElementById('sim13_val_hole');
    if (holeEl) holeEl.textContent = `${holeArea.toFixed(1)} Million km²`;

    const canvas = document.getElementById('sim13_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    // Globe Antarctica View
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(w * 0.5, h * 0.5, 90, 0, Math.PI * 2);
    ctx.fill();

    // Antarctica Continent
    ctx.fillStyle = '#e2e8f0';
    ctx.beginPath();
    ctx.arc(w * 0.5, h * 0.5, 50, 0, Math.PI * 2);
    ctx.fill();

    // Ozone Hole (Purple/Violet thinning overlay)
    const holeRadius = Math.min(85, (holeArea / 28) * 65);
    const holeGrad = ctx.createRadialGradient(w * 0.5, h * 0.5, 10, w * 0.5, h * 0.5, holeRadius);
    holeGrad.addColorStop(0, 'rgba(147, 51, 234, 0.85)');
    holeGrad.addColorStop(1, 'rgba(147, 51, 234, 0.1)');

    ctx.fillStyle = holeGrad;
    ctx.beginPath();
    ctx.arc(w * 0.5, h * 0.5, holeRadius, 0, Math.PI * 2);
    ctx.fill();

    // Cl Catalytic Cycle Reaction Formula Box
    ctx.fillStyle = '#1e293b';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.roundRect(20, 20, 200, 70, 8);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#38bdf8';
    ctx.font = '10px monospace';
    ctx.fillText('Cl• + O₃ ➔ ClO• + O₂', 30, 42);
    ctx.fillText('ClO• + O ➔ Cl• + O₂', 30, 60);
    ctx.fillStyle = '#f43f5e';
    ctx.fillText('1 Cl destroys 100k O₃', 30, 78);
}

// ------------------------------------------
// SIMULATOR 14: Substrate Enzyme Specificity
// ------------------------------------------
function initSim14() {
    sim14Update();
}

function sim14BurySample() {
    playSuccessChime();
    sim14Update();
}

function sim14Update() {
    const mat = document.getElementById('sim14_sel_material')?.value || 'cellulose';

    const canvas = document.getElementById('sim14_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const bEl = document.getElementById('sim14_val_bond');
    const fEl = document.getElementById('sim14_val_fit');
    const hlEl = document.getElementById('sim14_val_halflife');
    const clEl = document.getElementById('sim14_val_class');

    if (mat === 'cellulose') {
        if (bEl) bEl.textContent = 'β-1,4 Glycosidic Link';
        if (fEl) fEl.textContent = 'Perfect Lock-and-Key';
        if (hlEl) hlEl.textContent = '3 to 6 Weeks';
        if (clEl) clEl.textContent = '100% Biodegradable';

        // Bacterial Enzyme with Active Site Cleft
        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.arc(150, h * 0.5, 55, 0, Math.PI * 2);
        ctx.fill();

        // Triangular Active Site Cleft
        ctx.fillStyle = '#030712';
        ctx.beginPath();
        ctx.moveTo(180, h * 0.45);
        ctx.lineTo(205, h * 0.5);
        ctx.lineTo(180, h * 0.55);
        ctx.closePath();
        ctx.fill();

        // Matching Triangular Substrate Key
        ctx.fillStyle = '#22c55e';
        ctx.beginPath();
        ctx.moveTo(215, h * 0.45);
        ctx.lineTo(190, h * 0.5);
        ctx.lineTo(215, h * 0.55);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#22c55e';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Cellulose Natural Substrate', 230, h * 0.5 + 4);

        ctx.fillStyle = '#38bdf8';
        ctx.font = '12px monospace';
        ctx.fillText('Enzyme Active Site Cleaves β-Glycosidic Bond', 100, h * 0.85);

    } else if (mat === 'plastic') {
        if (bEl) bEl.textContent = 'Synthetic C–C Backbone';
        if (fEl) fEl.textContent = 'Zero Fit / Mismatched';
        if (hlEl) hlEl.textContent = '400+ Years';
        if (clEl) clEl.textContent = 'Non-Biodegradable';

        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.arc(150, h * 0.5, 55, 0, Math.PI * 2);
        ctx.fill();

        // Triangular Cleft
        ctx.fillStyle = '#030712';
        ctx.beginPath();
        ctx.moveTo(180, h * 0.45);
        ctx.lineTo(205, h * 0.5);
        ctx.lineTo(180, h * 0.55);
        ctx.closePath();
        ctx.fill();

        // Rigid Square Mismatched Plastic Block
        ctx.fillStyle = '#f43f5e';
        ctx.fillRect(215, h * 0.42, 35, 35);

        ctx.fillStyle = '#f43f5e';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Synthetic Polyethylene Block (NO FIT!)', 260, h * 0.5 + 4);

        ctx.fillStyle = '#f87171';
        ctx.font = '12px monospace';
        ctx.fillText('Bacteria possess zero enzymes to break synthetic C-C bonds', 80, h * 0.85);
    }
}

// ------------------------------------------
// SIMULATOR 15: Municipal Source Segregation Mini-Game
// ------------------------------------------
let sim15Items = [
    { name: '🍌 Banana Peels', type: 'green' },
    { name: '🥤 Plastic Bottle', type: 'blue' },
    { name: '🥫 Aluminium Can', type: 'blue' },
    { name: '🥬 Kitchen Vegetable Waste', type: 'green' },
    { name: '📦 Cardboard Packaging', type: 'blue' }
];
let sim15Idx = 0;
let sim15Score = 0;

function initSim15() {
    sim15Update();
}

function sim15SortItem(bin) {
    const curr = sim15Items[sim15Idx];
    if (bin === curr.type) {
        sim15Score++;
        playSuccessChime();
    } else {
        playErrorBuzz();
    }
    sim15Idx = (sim15Idx + 1) % sim15Items.length;
    sim15Update();
}

function sim15Update() {
    const item = sim15Items[sim15Idx];
    const nEl = document.getElementById('sim15_item_name');
    if (nEl) nEl.textContent = item.name;

    const canvas = document.getElementById('sim15_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    // Green Bin (Left)
    ctx.fillStyle = '#16a34a';
    ctx.beginPath();
    ctx.roundRect(80, 70, 140, 150, 16);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 14px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('🟢 GREEN BIN', 150, 110);
    ctx.font = '11px sans-serif';
    ctx.fillText('Wet / Biodegradable', 150, 135);
    ctx.fillText('Compost & Biogas', 150, 160);

    // Blue Bin (Right)
    ctx.fillStyle = '#0284c7';
    ctx.beginPath();
    ctx.roundRect(w - 220, 70, 140, 150, 16);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.fillText('🔵 BLUE BIN', w - 150, 110);
    ctx.font = '11px sans-serif';
    ctx.fillText('Dry / Non-Biodegradable', w - 150, 135);
    ctx.fillText('Mechanical Recycling', w - 150, 160);

    // Current Floating Item in center
    ctx.fillStyle = '#0f172a';
    ctx.strokeStyle = '#eab308';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.roundRect(w * 0.5 - 70, 80, 140, 60, 12);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#fef08a';
    ctx.font = 'bold 12px sans-serif';
    ctx.fillText(item.name, w * 0.5, 115);

    ctx.textAlign = 'start';
}

// ------------------------------------------
// SIMULATOR 16: Railway Beverage Container Lifecycle
// ------------------------------------------
function initSim16() {
    sim16Update();
}

function sim16Update() {
    const cup = document.getElementById('sim16_sel_cup')?.value || 'glass';
    const demand = parseInt(document.getElementById('sim16_demand_slider')?.value || 5);
    const dTxt = document.getElementById('sim16_demand_txt');
    if (dTxt) dTxt.textContent = `${demand} Million/day`;

    const canvas = document.getElementById('sim16_canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    const hyEl = document.getElementById('sim16_val_hygiene');
    const topEl = document.getElementById('sim16_val_topsoil');
    const decEl = document.getElementById('sim16_val_decomp');
    const susEl = document.getElementById('sim16_val_sustain');

    if (cup === 'glass') {
        if (hyEl) hyEl.textContent = 'Poor (Washing Risk)';
        if (topEl) topEl.textContent = '0 Tons Mined';
        if (decEl) decEl.textContent = '1 Million Years';
        if (susEl) susEl.textContent = 'Moderate (Washing Water)';

        ctx.font = '80px sans-serif';
        ctx.fillText('🥛', w * 0.5 - 40, h * 0.55);
        ctx.fillStyle = '#f43f5e';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Reusable Glass: Heavy water consumption & unhygienic on-train washing', w * 0.5, h * 0.8);

    } else if (cup === 'plastic') {
        if (hyEl) hyEl.textContent = 'High Hygiene';
        if (topEl) topEl.textContent = '0 Tons Mined';
        if (decEl) decEl.textContent = '400+ Years';
        if (susEl) susEl.textContent = 'Hazardous (Choked Culverts)';

        ctx.font = '80px sans-serif';
        ctx.fillText('🥤', w * 0.5 - 40, h * 0.55);
        ctx.fillStyle = '#f43f5e';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Plastic/Styrofoam: Non-biodegradable litter choked rail culverts', w * 0.5, h * 0.8);

    } else if (cup === 'kulhad') {
        if (hyEl) hyEl.textContent = 'High Hygiene';
        if (topEl) topEl.textContent = `${(demand * 1200).toLocaleString()} Tons Soil Lost`;
        if (decEl) decEl.textContent = 'Instant (Natural Clay)';
        if (susEl) susEl.textContent = 'Severe Topsoil Depletion';

        ctx.font = '80px sans-serif';
        ctx.fillText('🏺', w * 0.5 - 40, h * 0.55);
        ctx.fillStyle = '#f59e0b';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Clay Kulhads: Stripped millions of tons of fertile agricultural topsoil', w * 0.5, h * 0.8);

    } else if (cup === 'paper') {
        if (hyEl) hyEl.textContent = 'Optimal Hygiene';
        if (topEl) topEl.textContent = '0 Tons Soil Lost';
        if (decEl) decEl.textContent = '2 to 6 Months';
        if (susEl) susEl.textContent = 'Best Ecological Choice';

        ctx.font = '80px sans-serif';
        ctx.fillText('☕', w * 0.5 - 40, h * 0.55);
        ctx.fillStyle = '#10b981';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Paper Cups: Renewable plant pulp, biodegradable, preserves topsoil', w * 0.5, h * 0.8);
    }
    ctx.textAlign = 'start';
}

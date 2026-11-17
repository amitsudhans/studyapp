"""Interactive Simulation JavaScript Handlers for Class 10 Science Chapter 3: Metals and Non-metals
"""

SIMULATOR_JS = '''
// ==========================================
// SIMULATOR 1: Physical Properties of Metals
// ==========================================
function setSim1Mode(mode) {
    document.getElementById('sim1LustreView').classList.toggle('hidden', mode !== 'lustre');
    document.getElementById('sim1HammerView').classList.toggle('hidden', mode !== 'hammer');
    document.getElementById('sim1ThermalView').classList.toggle('hidden', mode !== 'thermal');

    document.getElementById('sim1BtnLustre').className = mode === 'lustre' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim1BtnHammer').className = mode === 'hammer' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim1BtnThermal').className = mode === 'thermal' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function rubSandpaper() {
    const sp = document.getElementById('sim1Sandpaper');
    const strip = document.getElementById('sim1MetalStrip');
    const label = document.getElementById('sim1StripText');
    const sparkles = document.getElementById('sim1Sparkles');
    const msg = document.getElementById('sim1LustreMsg');

    sp.setAttribute('opacity', '1');
    setTimeout(() => {
        strip.setAttribute('fill', '#fde047');
        strip.setAttribute('stroke', '#eab308');
        label.textContent = 'Polished Pure Metal (Shiny Lustre!)';
        label.setAttribute('fill', '#854d0e');
        sparkles.setAttribute('opacity', '1');
        msg.innerHTML = '<strong class="text-amber-400">Activity 3.1:</strong> Rubbing removes outer oxide tarnish, revealing pure metallic lustre underneath!';
        sp.setAttribute('opacity', '0');
    }, 600);
}

function resetLustre() {
    const strip = document.getElementById('sim1MetalStrip');
    const label = document.getElementById('sim1StripText');
    const sparkles = document.getElementById('sim1Sparkles');
    const msg = document.getElementById('sim1LustreMsg');

    strip.setAttribute('fill', '#64748b');
    strip.setAttribute('stroke', '#475569');
    label.textContent = 'Dull / Oxidised Surface';
    label.setAttribute('fill', '#cbd5e1');
    sparkles.setAttribute('opacity', '0');
    msg.textContent = 'Metals in pure state have a shiny surface known as metallic lustre.';
}

function testKnife(metal) {
    const knife = document.getElementById('sim1Knife');
    const block = document.getElementById('sim1SampleBlock');
    const cut = document.getElementById('sim1CutBlock');
    const label = document.getElementById('sim1SampleLabel');
    const msg = document.getElementById('sim1KnifeMsg');

    if (metal === 'iron') {
        block.setAttribute('fill', '#94a3b8');
        block.setAttribute('width', '110');
        cut.setAttribute('opacity', '0');
        label.textContent = 'Iron (Hard)';
        knife.setAttribute('transform', 'translate(85, 20)');
        setTimeout(() => {
            knife.setAttribute('transform', 'translate(85, 10)');
            msg.innerHTML = '<span class="text-rose-400 font-bold">Knife bounces off!</span> Iron is exceptionally hard and cannot be cut with a domestic knife.';
        }, 300);
    } else {
        block.setAttribute('fill', '#fde047');
        block.setAttribute('width', '55');
        cut.setAttribute('fill', '#fde047');
        label.textContent = 'Sodium';
        knife.setAttribute('transform', 'translate(85, 45)');
        setTimeout(() => {
            cut.setAttribute('opacity', '1');
            cut.setAttribute('transform', 'translate(10, 0)');
            knife.setAttribute('transform', 'translate(85, 10)');
            msg.innerHTML = '<span class="text-emerald-400 font-bold">Clean cut!</span> Sodium is an alkali metal so soft it slices like cold butter!';
        }, 400);
    }
}

function strikeHammer() {
    const hammer = document.getElementById('sim1HammerTool');
    const metal = document.getElementById('sim1HammerMetal');
    const msg = document.getElementById('sim1HammerMsg');

    hammer.setAttribute('transform', 'translate(85, 45)');
    setTimeout(() => {
        metal.setAttribute('width', '100');
        metal.setAttribute('x', '50');
        metal.setAttribute('height', '4');
        metal.setAttribute('y', '76');
        hammer.setAttribute('transform', 'translate(85, 15)');
        msg.innerHTML = '<span class="text-amber-400 font-bold">Malleability demonstrated!</span> The metal deforms into a broad thin sheet without shattering.';
    }, 250);
}

function drawWire() {
    const pellet = document.getElementById('sim1GoldPellet');
    const wire = document.getElementById('sim1GoldWire');
    const label = document.getElementById('sim1WireLengthText');
    const msg = document.getElementById('sim1DuctileMsg');

    pellet.setAttribute('r', '4');
    wire.setAttribute('x2', '160');
    label.setAttribute('opacity', '1');
    msg.innerHTML = '<span class="text-amber-300 font-bold">Maximal Ductility:</span> 1 gram of gold can be drawn out into a continuous wire 2 kilometres in length!';
}

function heatThermalWire() {
    const flame = document.getElementById('sim1BurnerFlame');
    const pin = document.getElementById('sim1WaxPin');
    const msg = document.getElementById('sim1ThermalMsg');

    flame.setAttribute('opacity', '1');
    setTimeout(() => {
        pin.setAttribute('transform', 'translate(150, 75)');
        msg.innerHTML = '<span class="text-emerald-400 font-bold">Wax melted — Pin dropped!</span> Heat conducted along the metal rod to the wax attachment point (Ag & Cu are best conductors).';
    }, 700);
}

function testCircuit(mat) {
    const clip = document.getElementById('sim1TestClip');
    const bulb = document.getElementById('sim1Bulb');
    const glow = document.getElementById('sim1BulbGlow');
    const clipText = document.getElementById('sim1ClipText');
    const msg = document.getElementById('sim1CircuitMsg');

    if (mat === 'copper') {
        clip.setAttribute('stroke', '#f97316');
        clip.setAttribute('stroke-dasharray', '0');
        clipText.textContent = 'Copper';
        bulb.setAttribute('fill', '#fde047');
        glow.setAttribute('opacity', '0.7');
        msg.innerHTML = '<span class="text-emerald-400 font-bold">Circuit Closed!</span> Copper has free delocalised electrons that conduct electricity; bulb glows brightly.';
    } else if (mat === 'pvc') {
        clip.setAttribute('stroke', '#cbd5e1');
        clip.setAttribute('stroke-dasharray', '2 2');
        clipText.textContent = 'PVC Plastic';
        bulb.setAttribute('fill', '#475569');
        glow.setAttribute('opacity', '0.05');
        msg.innerHTML = '<span class="text-rose-400 font-bold">Circuit Open!</span> Polyvinylchloride (PVC) is an electrical insulator; no current flows and the bulb stays dark.';
    } else if (mat === 'graphite') {
        clip.setAttribute('stroke', '#818cf8');
        clip.setAttribute('stroke-dasharray', '0');
        clipText.textContent = 'Graphite Rod';
        bulb.setAttribute('fill', '#fde047');
        glow.setAttribute('opacity', '0.5');
        msg.innerHTML = '<span class="text-indigo-400 font-bold">Non-metal Exception!</span> Graphite has delocalised pi electrons in hexagonal planes, conducting electricity!';
    }
}

// ==========================================
// SIMULATOR 2: Physical Exceptions
// ==========================================
function setSim2Tab(tab) {
    document.getElementById('sim2ViewHg').classList.toggle('hidden', tab !== 'mercury');
    document.getElementById('sim2ViewPalm').classList.toggle('hidden', tab !== 'palmMelt');
    document.getElementById('sim2ViewAllo').classList.toggle('hidden', tab !== 'allotropes');

    document.getElementById('sim2TabHg').className = tab === 'mercury' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim2TabPalm').className = tab === 'palmMelt' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim2TabAllo').className = tab === 'allotropes' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function meltOnPalm() {
    const cube = document.getElementById('sim2GaCube');
    const puddle = document.getElementById('sim2GaPuddle');

    cube.setAttribute('transform', 'scale(0.2)');
    cube.setAttribute('opacity', '0');
    puddle.setAttribute('opacity', '1');
}

function resetPalm() {
    const cube = document.getElementById('sim2GaCube');
    const puddle = document.getElementById('sim2GaPuddle');

    cube.setAttribute('transform', 'scale(1)');
    cube.setAttribute('opacity', '1');
    puddle.setAttribute('opacity', '0');
}

// ==========================================
// SIMULATOR 3: Combustion & Oxide Testing
// ==========================================
let currentCombustElement = null;

function burnMetal(elem) {
    currentCombustElement = elem;
    const sample = document.getElementById('sim3Sample');
    const flame = document.getElementById('sim3Flame');
    const ash = document.getElementById('sim3Ash');
    const title = document.getElementById('sim3StageTitle');
    const ctext = document.getElementById('sim3CombustText');
    const btn = document.getElementById('sim3LitmusBtn');

    ['Mg', 'S', 'Cu'].forEach(e => {
        const b = document.getElementById('sim3Btn' + e);
        if (b) b.className = (e.toLowerCase() === elem) ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    });

    flame.setAttribute('opacity', '1');

    if (elem === 'mg') {
        sample.setAttribute('fill', '#ffffff');
        title.textContent = 'Burning Magnesium Ribbon';
        ctext.innerHTML = '<span class="text-amber-300 font-bold">Dazzling White Flame!</span> 2Mg + O2 → 2MgO (white powder collected in watch glass).';
        setTimeout(() => {
            ash.setAttribute('opacity', '1');
            ash.setAttribute('fill', '#f8fafc');
            btn.disabled = false;
            btn.className = 'px-3 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/40 text-xs font-bold';
        }, 600);
    } else if (elem === 's') {
        sample.setAttribute('fill', '#eab308');
        title.textContent = 'Burning Sulphur Powder';
        ctext.innerHTML = '<span class="text-sky-300 font-bold">Blue Flame & Pungent SO2 Gas!</span> S + O2 → SO2 gas.';
        setTimeout(() => {
            ash.setAttribute('opacity', '0');
            btn.disabled = false;
            btn.className = 'px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold';
        }, 600);
    } else if (elem === 'cu') {
        sample.setAttribute('fill', '#1e293b');
        title.textContent = 'Heating Copper Metal';
        ctext.innerHTML = '<span class="text-slate-300 font-bold">Black Coating Forms!</span> 2Cu + O2 → 2CuO (Black copper(II) oxide layer on surface).';
        btn.disabled = true;
        btn.className = 'px-3 py-1 rounded bg-slate-800 text-slate-500 text-xs font-bold';
    }
}

function testOxideLitmus() {
    const strip = document.getElementById('sim3LitmusStrip');
    const sol = document.getElementById('sim3SolWater');
    const res = document.getElementById('sim3LitmusResult');

    if (currentCombustElement === 'mg') {
        sol.setAttribute('fill', '#a855f7');
        strip.setAttribute('fill', '#3b82f6');
        res.innerHTML = '<strong class="text-cyan-400">Basic Metal Oxide:</strong> MgO + H2O → Mg(OH)2. Alkaline solution turns red litmus BLUE!';
    } else if (currentCombustElement === 's') {
        sol.setAttribute('fill', '#ef4444');
        strip.setAttribute('fill', '#ef4444');
        res.innerHTML = '<strong class="text-rose-400">Acidic Non-metal Oxide:</strong> SO2 + H2O → H2SO3 (sulphurous acid). Turns blue litmus RED!';
    }
}

// ==========================================
// SIMULATOR 4: Amphoteric Oxides & Anodising
// ==========================================
function setSim4Tab(tab) {
    document.getElementById('sim4ViewAmpho').classList.toggle('hidden', tab !== 'ampho');
    document.getElementById('sim4ViewAnodise').classList.toggle('hidden', tab !== 'anodise');

    document.getElementById('sim4TabAmpho').className = tab === 'ampho' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim4TabAnod').className = tab === 'anodise' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function reactAmpho(type) {
    if (type === 'acid') {
        const dot = document.getElementById('sim4Al2O3Acid');
        const msg = document.getElementById('sim4AcidMsg');
        dot.setAttribute('transform', 'scale(0.1)');
        dot.setAttribute('opacity', '0');
        msg.innerHTML = '<span class="text-emerald-400 font-bold">Al2O3 Dissolved!</span> Al2O3 + 6HCl → 2AlCl3 + 3H2O (Acts as a Base, neutralising acid).';
    } else {
        const dot = document.getElementById('sim4Al2O3Base');
        const msg = document.getElementById('sim4BaseMsg');
        dot.setAttribute('transform', 'scale(0.1)');
        dot.setAttribute('opacity', '0');
        msg.innerHTML = '<span class="text-emerald-400 font-bold">Al2O3 Dissolved!</span> Al2O3 + 2NaOH → 2NaAlO2 (Sodium Aluminate) + H2O (Acts as an Acid, neutralising base).';
    }
}

function startAnodising() {
    const layer = document.getElementById('sim4OxideLayer');
    const btn = document.getElementById('sim4DyeBtn');
    const msg = document.getElementById('sim4AnodiseMsg');

    layer.setAttribute('stroke-width', '4');
    msg.innerHTML = '<strong class="text-amber-400">Oxide Layer Thickened!</strong> Oxygen liberated at the aluminium anode builds a uniform, non-porous Al2O3 barrier.';
    btn.disabled = false;
    btn.className = 'px-3 py-1 rounded bg-purple-600/30 hover:bg-purple-600/50 text-purple-200 border border-purple-500/40 text-xs font-bold';
}

function dyeAnodised() {
    const layer = document.getElementById('sim4OxideLayer');
    const msg = document.getElementById('sim4AnodiseMsg');
    layer.setAttribute('stroke', '#a855f7');
    msg.innerHTML = '<strong class="text-purple-300">Dyed Anodised Coating:</strong> Porous oxide film absorbs bright organic dye, giving cookware durable, corrosion-proof finishes!';
}

// ==========================================
// SIMULATOR 5: Metals Reacting with Water
// ==========================================
function setSim5Mode(mode) {
    document.getElementById('sim5ColdView').classList.toggle('hidden', mode !== 'cold');
    document.getElementById('sim5HotView').classList.toggle('hidden', mode !== 'hot');
    document.getElementById('sim5SteamView').classList.toggle('hidden', mode !== 'steam');

    document.getElementById('sim5BtnCold').className = mode === 'cold' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim5BtnHot').className = mode === 'hot' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim5BtnSteam').className = mode === 'steam' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function testWater(metal) {
    const sample = document.getElementById('sim5Sample');
    const vigor = document.getElementById('sim5Vigor');
    const msg = document.getElementById('sim5ColdMsg');

    if (metal === 'na') {
        sample.setAttribute('cx', '90');
        sample.setAttribute('cy', '60');
        sample.setAttribute('fill', '#fde047');
        vigor.setAttribute('opacity', '1');
        msg.innerHTML = '<span class="text-amber-400 font-bold">Violent Reaction!</span> 2Na + 2H2O → 2NaOH + H2 + Heat. Sodium darts on surface and catches fire immediately!';
    } else if (metal === 'ca') {
        sample.setAttribute('cx', '90');
        sample.setAttribute('cy', '65');
        sample.setAttribute('fill', '#cbd5e1');
        vigor.setAttribute('opacity', '0.5');
        msg.innerHTML = '<span class="text-sky-300 font-bold">Calcium floats!</span> Ca + 2H2O → Ca(OH)2 + H2. Bubbles of hydrogen stick to calcium, buoying it to the surface.';
    } else if (metal === 'cu') {
        sample.setAttribute('cx', '90');
        sample.setAttribute('cy', '100');
        sample.setAttribute('fill', '#b45309');
        vigor.setAttribute('opacity', '0');
        msg.innerHTML = '<span class="text-slate-400 font-bold">No reaction!</span> Copper sits inertly at the bottom; does not react with cold or hot water.';
    }
}

function reactMgHot() {
    const mg = document.getElementById('sim5MgPiece');
    const msg = document.getElementById('sim5HotMsg');
    mg.setAttribute('y', '50');
    msg.innerHTML = '<span class="text-amber-300 font-bold">Mg floats in hot water!</span> Mg + 2H2O(hot) → Mg(OH)2 + H2. Hydrogen gas bubbles stick to metal surface, causing it to float.';
}

function passSteam() {
    const bubbles = document.getElementById('sim5SteamBubbles');
    const fe = document.getElementById('sim5SteamFe');
    const msg = document.getElementById('sim5SteamMsg');

    fe.setAttribute('fill', '#1e293b');
    bubbles.setAttribute('opacity', '1');
    msg.innerHTML = '<span class="text-cyan-400 font-bold">Hydrogen Gas Collected!</span> 3Fe + 4H2O(steam) → Fe3O4 (magnetic oxide) + 4H2 ↑.';
}

// ==========================================
// SIMULATOR 6: Metals with Acids & Aqua Regia
// ==========================================
function setSim6Tab(tab) {
    document.getElementById('sim6HClView').classList.toggle('hidden', tab !== 'hcl');
    document.getElementById('sim6AquaView').classList.toggle('hidden', tab !== 'aqua');

    document.getElementById('sim6TabHCl').className = tab === 'hcl' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim6TabAqua').className = tab === 'aqua' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function startAcidBubbles() {
    document.getElementById('sim6B1').setAttribute('opacity', '1');
    document.getElementById('sim6B2').setAttribute('opacity', '1');
    document.getElementById('sim6B3').setAttribute('opacity', '1');
    document.getElementById('sim6B4').setAttribute('opacity', '1');
}

function dissolveGold() {
    const leaf = document.getElementById('sim6GoldLeaf');
    const liq = document.getElementById('sim6AquaLiquid');
    const msg = document.getElementById('sim6AquaMsg');

    leaf.setAttribute('transform', 'scale(0.1)');
    leaf.setAttribute('opacity', '0');
    liq.setAttribute('fill', '#ca8a04');
    msg.innerHTML = '<span class="text-yellow-400 font-bold">Gold Dissolved!</span> Fresh 3:1 conc. HCl + conc. HNO3 yields nascent chlorine, producing soluble chloroauric acid HAuCl4.';
}

// ==========================================
// SIMULATOR 7: Metal Displacement Reactions
// ==========================================
function runDisplacementA() {
    const sol = document.getElementById('sim7SolutionA');
    const nail = document.getElementById('sim7NailA');
    const msg = document.getElementById('sim7MsgA');

    sol.setAttribute('fill', '#10b981');
    sol.setAttribute('fill-opacity', '0.25');
    nail.setAttribute('fill', '#b45309');
    nail.setAttribute('stroke', '#78350f');
    msg.innerHTML = '<strong class="text-emerald-400">Displacement Occurred!</strong> Fe + CuSO4(blue) → FeSO4(pale green) + Cu(reddish-brown coating on iron nail).';
}

function runDisplacementB() {
    const msg = document.getElementById('sim7MsgB');
    msg.innerHTML = '<strong class="text-rose-400">No Reaction!</strong> Copper is less reactive than iron and cannot displace Fe²⁺ ions from solution.';
}

// ==========================================
// SIMULATOR 8: Reactivity Series Duel
// ==========================================
function testDuel() {
    const aVal = parseInt(document.getElementById('sim8MetalA').value);
    const bVal = parseInt(document.getElementById('sim8SaltB').value);
    const outcome = document.getElementById('sim8DuelOutcome');

    const mAName = document.getElementById('sim8MetalA').options[document.getElementById('sim8MetalA').selectedIndex].text;
    const sBName = document.getElementById('sim8SaltB').options[document.getElementById('sim8SaltB').selectedIndex].text;

    if (aVal > bVal) {
        outcome.className = 'p-2 bg-emerald-950/80 rounded border border-emerald-500/80 text-xs text-emerald-300';
        outcome.innerHTML = `<strong>Reaction Occurs!</strong> ${mAName} is higher in the reactivity series and successfully displaces metal from ${sBName}!`;
    } else if (aVal === bVal) {
        outcome.className = 'p-2 bg-slate-900 rounded border border-slate-700 text-xs text-slate-400';
        outcome.innerHTML = `<strong>Identical Metal:</strong> No chemical displacement occurs between identical species.`;
    } else {
        outcome.className = 'p-2 bg-rose-950/80 rounded border border-rose-500/80 text-xs text-rose-300';
        outcome.innerHTML = `<strong>No Reaction!</strong> ${mAName} is lower in the reactivity series and cannot displace metal from ${sBName}.`;
    }
}

// ==========================================
// SIMULATOR 9: Ionic Bond Formation
// ==========================================
function setSim9Compound(comp) {
    document.getElementById('sim9NaClView').classList.toggle('hidden', comp !== 'nacl');
    document.getElementById('sim9MgCl2View').classList.toggle('hidden', comp !== 'mgcl2');

    document.getElementById('sim9BtnNaCl').className = comp === 'nacl' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim9BtnMgCl2').className = comp === 'mgcl2' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function transferElectronNaCl() {
    const e = document.getElementById('sim9NaValence');
    const naState = document.getElementById('sim9NaState');
    const clState = document.getElementById('sim9ClState');
    const hole = document.getElementById('sim9ClHole');
    const msg = document.getElementById('sim9Msg');

    e.setAttribute('cx', '180');
    setTimeout(() => {
        hole.setAttribute('fill', '#fbbf24');
        hole.setAttribute('stroke', '#d97706');
        naState.innerHTML = '<strong class="text-amber-400">Na⁺ Cation (2,8)</strong>';
        clState.innerHTML = '<strong class="text-emerald-400">Cl⁻ Anion (2,8,8)</strong>';
        msg.innerHTML = '<strong class="text-emerald-400">Stable Octets Achieved!</strong> Electrostatic attraction binds Na⁺ and Cl⁻ into ionic NaCl crystal lattice.';
    }, 600);
}

function resetSim9() {
    const e = document.getElementById('sim9NaValence');
    const naState = document.getElementById('sim9NaState');
    const clState = document.getElementById('sim9ClState');
    const hole = document.getElementById('sim9ClHole');
    const msg = document.getElementById('sim9Msg');

    e.setAttribute('cx', '55');
    hole.setAttribute('fill', 'none');
    hole.setAttribute('stroke', '#34d399');
    naState.textContent = 'Na Atom (2,8,1)';
    clState.textContent = 'Cl Atom (2,8,7)';
    msg.textContent = 'Complete transfer of valence electrons yields stable noble gas octets and powerful electrostatic attraction.';
}

// ==========================================
// SIMULATOR 10: Properties of Ionic Compounds
// ==========================================
function setSim10Mode(mode) {
    document.getElementById('sim10BrittleView').classList.toggle('hidden', mode !== 'brittle');
    document.getElementById('sim10MeltView').classList.toggle('hidden', mode !== 'melting');
    document.getElementById('sim10ConductView').classList.toggle('hidden', mode !== 'conduct');

    document.getElementById('sim10BtnBrittle').className = mode === 'brittle' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim10BtnMelt').className = mode === 'melting' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim10BtnConduct').className = mode === 'conduct' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function strikeIonicCrystal() {
    const top = document.getElementById('sim10TopLayer');
    const hammer = document.getElementById('sim10Hammer');
    const msg = document.getElementById('sim10BrittleMsg');

    hammer.setAttribute('transform', 'translate(140, 25)');
    setTimeout(() => {
        top.setAttribute('transform', 'translate(30, -5)');
        msg.innerHTML = '<span class="text-rose-400 font-bold">Crystal Cleaved!</span> Layer shift aligned like charges (+ next to +, - next to -). Electrostatic repulsion shattered the crystal.';
        hammer.setAttribute('transform', 'translate(140, 5)');
    }, 250);
}

function testConductivity(state) {
    const bulb = document.getElementById('sim10Bulb');
    const liq = document.getElementById('sim10Liq');
    const msg = document.getElementById('sim10ConductMsg');

    if (state === 'solid') {
        liq.setAttribute('fill-opacity', '0.05');
        bulb.setAttribute('fill', '#334155');
        msg.innerHTML = '<strong class="text-rose-400">Solid Ionic Salt:</strong> Ions are locked in rigid crystal lattice positions; no mobile charge carriers; does not conduct electricity.';
    } else {
        liq.setAttribute('fill-opacity', '0.4');
        bulb.setAttribute('fill', '#fde047');
        msg.innerHTML = '<strong class="text-emerald-400">Aqueous / Molten Salt:</strong> Lattice dissociates into mobile hydrated cations and anions that migrate to electrodes, conducting current freely!';
    }
}

// ==========================================
// SIMULATOR 12: Low Reactivity Metallurgy
// ==========================================
function setSim12Ore(ore) {
    document.getElementById('sim12HgView').classList.toggle('hidden', ore !== 'cinnabar');
    document.getElementById('sim12CuView').classList.toggle('hidden', ore !== 'copper');

    document.getElementById('sim12BtnHg').className = ore === 'cinnabar' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim12BtnCu').className = ore === 'copper' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function roastCinnabar() {
    const msg = document.getElementById('sim12HgMsg');
    msg.innerHTML = '<strong class="text-emerald-400">Thermal Extraction Complete!</strong> 2HgS + 3O2 → 2HgO + 2SO2. Then 2HgO(heat) → 2Hg(liquid droplets) + O2 gas!';
}

// ==========================================
// SIMULATOR 13: Moderate Reactivity Metallurgy
// ==========================================
function setSim13Tab(tab) {
    document.getElementById('sim13ViewRoast').classList.toggle('hidden', tab !== 'roast');
    document.getElementById('sim13ViewThermit').classList.toggle('hidden', tab !== 'thermit');

    document.getElementById('sim13TabRoast').className = tab === 'roast' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim13TabThermit').className = tab === 'thermit' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function igniteThermit() {
    const spark = document.getElementById('sim13ThermitSpark');
    const stream = document.getElementById('sim13IronStream');
    const weld = document.getElementById('sim13Weld');
    const msg = document.getElementById('sim13ThermitMsg');

    spark.setAttribute('fill', '#ffffff');
    setTimeout(() => {
        stream.setAttribute('opacity', '1');
        setTimeout(() => {
            weld.setAttribute('opacity', '1');
            stream.setAttribute('opacity', '0');
            msg.innerHTML = '<strong class="text-orange-400">Thermit Weld Complete!</strong> Molten iron (>3000°C) poured into railway joint gap, fusing the rails seamlessly on-site!';
        }, 500);
    }, 400);
}

// ==========================================
// SIMULATOR 14: Electrolytic Metal Extraction
// ==========================================
function electrolyseMoltenNaCl() {
    const na = document.getElementById('sim14NaMetal');
    const cl = document.getElementById('sim14ClGas');
    const msg = document.getElementById('sim14Msg');

    na.setAttribute('opacity', '1');
    cl.setAttribute('opacity', '1');
    msg.innerHTML = '<strong class="text-emerald-400">Electrolysis Active!</strong> Na⁺ + e⁻ → Na(l) deposited at cathode. 2Cl⁻ → Cl2(g) evolved at anode.';
}

// ==========================================
// SIMULATOR 15: Electrolytic Refining of Copper
// ==========================================
function refineCopper() {
    const anode = document.getElementById('sim15Anode');
    const cathode = document.getElementById('sim15Cathode');
    const mud = document.getElementById('sim15Mud');
    const label = document.getElementById('sim15MudLabel');
    const msg = document.getElementById('sim15Msg');

    anode.setAttribute('width', '8');
    anode.setAttribute('fill', '#78350f');
    cathode.setAttribute('width', '22');
    mud.setAttribute('opacity', '1');
    label.setAttribute('opacity', '1');
    msg.innerHTML = '<strong class="text-emerald-400">Refining Complete!</strong> Cathode grew to 99.99% pure copper. Insoluble gold and silver settled as precious anode mud!';
}

function resetRefining() {
    const anode = document.getElementById('sim15Anode');
    const cathode = document.getElementById('sim15Cathode');
    const mud = document.getElementById('sim15Mud');
    const label = document.getElementById('sim15MudLabel');
    const msg = document.getElementById('sim15Msg');

    anode.setAttribute('width', '22');
    anode.setAttribute('fill', '#b45309');
    cathode.setAttribute('width', '8');
    mud.setAttribute('opacity', '0');
    label.setAttribute('opacity', '0');
    msg.textContent = 'Pure Cu transfers from dissolving anode to growing cathode. Precious insoluble metals settle as anode mud.';
}

// ==========================================
// SIMULATOR 16: Corrosion Testing & Alloys
// ==========================================
function setSim16Tab(tab) {
    document.getElementById('sim16TubesView').classList.toggle('hidden', tab !== 'tubes');
    document.getElementById('sim16AlloysView').classList.toggle('hidden', tab !== 'alloys');

    document.getElementById('sim16TabTubes').className = tab === 'tubes' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim16TabAlloys').className = tab === 'alloys' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function incubateRust() {
    const nailA = document.getElementById('sim16NailA');
    const resA = document.getElementById('sim16ResA');

    nailA.setAttribute('fill', '#b45309');
    nailA.setAttribute('stroke', '#78350f');
    resA.innerHTML = '<span class="text-rose-400 font-bold">Rusted (Fe2O3·xH2O)</span>';
}
'''

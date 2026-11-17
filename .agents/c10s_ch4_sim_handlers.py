"""Interactive Simulation JavaScript Handlers for Class 10 Science Chapter 4: Carbon and its Compounds
"""

SIMULATOR_JS = '''
// ==========================================
// SIMULATOR 1: Carbon Ubiquity & Properties
// ==========================================
function setSim1Mode(mode) {
    document.getElementById('sim1SortView').classList.toggle('hidden', mode !== 'sort');
    document.getElementById('sim1ConstView').classList.toggle('hidden', mode !== 'constants');
    document.getElementById('sim1CircuitView').classList.toggle('hidden', mode !== 'circuit');

    document.getElementById('sim1BtnSort').className = mode === 'sort' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim1BtnConst').className = mode === 'constants' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim1BtnCircuit').className = mode === 'circuit' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function testSim1Conduct(type) {
    const bulb = document.getElementById('sim1Bulb');
    const liq = document.getElementById('sim1Liq');
    const msg = document.getElementById('sim1ConductMsg');

    if (type === 'ionic') {
        liq.setAttribute('fill-opacity', '0.4');
        bulb.setAttribute('fill', '#fde047');
        msg.innerHTML = '<strong class="text-emerald-400">Ionic NaCl:</strong> Dissociates into free mobile Na⁺ and Cl⁻ ions, conducting electricity and lighting the bulb brightly!';
    } else {
        liq.setAttribute('fill-opacity', '0.15');
        bulb.setAttribute('fill', '#334155');
        msg.innerHTML = '<strong class="text-amber-400">Covalent Carbon Compound:</strong> Covalent molecules do not form free mobile ions; behaves as an electrical insulator and the bulb stays dark.';
    }
}

// ==========================================
// SIMULATOR 2: Valency Dilemma
// ==========================================
function testC4Minus() {
    const msg = document.getElementById('sim2C4MinusMsg');
    msg.innerHTML = '<span class="text-rose-400 font-bold">Unstable!</span> 6 positive protons in the small carbon nucleus cannot hold 10 orbital electrons due to massive inter-electron repulsion.';
}

function testC4Plus() {
    const msg = document.getElementById('sim2C4PlusMsg');
    msg.innerHTML = '<span class="text-rose-400 font-bold">Energy Prohibitive!</span> Removing four successive electrons requires immense cumulative ionisation energy, leaving an unstable naked nucleus.';
}

function testCovalentSharing() {
    const msg = document.getElementById('sim2CovalentMsg');
    msg.innerHTML = '<span class="text-emerald-400 font-bold">Perfect Stability!</span> By sharing 4 valence electron pairs, carbon achieves the noble gas configuration of neon (2,8) without creating destabilising electrical charges.';
}

// ==========================================
// SIMULATOR 3: Covalent Bonds
// ==========================================
function setSim3Molecule(mol) {
    document.getElementById('sim3H2View').classList.toggle('hidden', mol !== 'h2');
    document.getElementById('sim3O2View').classList.toggle('hidden', mol !== 'o2');
    document.getElementById('sim3N2View').classList.toggle('hidden', mol !== 'n2');
    document.getElementById('sim3S8View').classList.toggle('hidden', mol !== 's8');

    document.getElementById('sim3BtnH2').className = mol === 'h2' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim3BtnO2').className = mol === 'o2' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim3BtnN2').className = mol === 'n2' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim3BtnS8').className = mol === 's8' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

// ==========================================
// SIMULATOR 4: Carbon Allotropes
// ==========================================
function setSim4Allotrope(allo) {
    document.getElementById('sim4DiaView').classList.toggle('hidden', allo !== 'diamond');
    document.getElementById('sim4GphView').classList.toggle('hidden', allo !== 'graphite');
    document.getElementById('sim4FulView').classList.toggle('hidden', allo !== 'fullerene');

    document.getElementById('sim4BtnDia').className = allo === 'diamond' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim4BtnGph').className = allo === 'graphite' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim4BtnFul').className = allo === 'fullerene' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

// ==========================================
// SIMULATOR 5: Carbon Versatility Framework
// ==========================================
function setSim5Framework(fw) {
    const visual = document.getElementById('sim5FrameworkVisual');
    const desc = document.getElementById('sim5FrameworkDesc');

    document.getElementById('sim5BtnStr').className = fw === 'straight' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim5BtnBrn').className = fw === 'branched' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim5BtnRng').className = fw === 'ring' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';

    if (fw === 'straight') {
        visual.textContent = '– C – C – C – C – C –';
        desc.textContent = 'Straight chain: Continuous unbranched catenated carbon backbone.';
    } else if (fw === 'branched') {
        visual.innerHTML = '– C – C(–C) – C – C –';
        desc.textContent = 'Branched framework: Carbon atoms branch off the main parent chain, creating structural isomers.';
    } else {
        visual.textContent = '[ C – C – C – C – C – C ] (Closed Ring)';
        desc.textContent = 'Closed cyclic ring: Carbon atoms loop and bond end-to-end (e.g., cyclohexane, benzene).';
    }
}

// ==========================================
// SIMULATOR 6: Wöhler Urea Synthesis
// ==========================================
function heatWöhlerTube() {
    const flame = document.getElementById('sim6Flame');
    const crystals = document.getElementById('sim6Crystals');
    const status = document.getElementById('sim6Status');

    flame.setAttribute('opacity', '1');
    setTimeout(() => {
        crystals.setAttribute('fill', '#ffffff');
        status.innerHTML = '<span class="text-emerald-400 font-bold">Urea Formed!</span> NH4CNO (inorganic ammonium cyanate) rearranged upon heating into NH2CONH2 (organic urea), disproving vitalism!';
    }, 600);
}

// ==========================================
// SIMULATOR 7: Bromine Water Test
// ==========================================
function testBromine(hc) {
    const liquid = document.getElementById('sim7BrLiquid');
    const title = document.getElementById('sim7Title');
    const desc = document.getElementById('sim7Desc');
    const eq = document.getElementById('sim7Eq');

    document.getElementById('sim7BtnEthane').className = hc === 'ethane' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim7BtnEthene').className = hc === 'ethene' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';

    if (hc === 'ethane') {
        liquid.setAttribute('fill', '#b91c1c');
        title.textContent = 'Saturated Alkane: Ethane (C2H6)';
        desc.textContent = 'No double bond. Bromine water remains reddish-brown; no addition reaction occurs.';
        eq.textContent = 'C2H6 + Br2 → No reaction (in dark)';
    } else {
        liquid.setAttribute('fill', '#38bdf8');
        liquid.setAttribute('fill-opacity', '0.15');
        title.textContent = 'Unsaturated Alkene: Ethene (C2H4)';
        desc.innerHTML = '<strong class="text-emerald-400">Decolourised!</strong> Reddish-brown bromine water turns colourless as bromine adds across the reactive double bond.';
        eq.textContent = 'CH2=CH2 + Br2 → CH2Br–CH2Br (1,2-dibromoethane)';
    }
}

// ==========================================
// SIMULATOR 8: Chains, Branches & Rings
// ==========================================
function setSim8Model(model) {
    const box = document.getElementById('sim8FormulaBox');
    const desc = document.getElementById('sim8Desc');

    document.getElementById('sim8BtnNBut').className = model === 'nbutane' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim8BtnIso').className = model === 'isobutane' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim8BtnBen').className = model === 'benzene' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';

    if (model === 'nbutane') {
        box.textContent = 'CH3 – CH2 – CH2 – CH3';
        desc.textContent = 'n-Butane: Continuous straight 4-carbon chain (Formula C4H10, bp 273 K / 0°C).';
    } else if (model === 'isobutane') {
        box.textContent = 'CH3 – CH(CH3) – CH3';
        desc.textContent = 'Isobutane (2-methylpropane): Branched 4-carbon chain (Formula C4H10, bp 261 K / -12°C).';
    } else {
        box.textContent = 'C6H6 (Planar Hexagonal Ring with 3 Alternating C=C Double Bonds)';
        desc.textContent = 'Benzene: Unsaturated aromatic cyclic hydrocarbon with exceptional resonance stability.';
    }
}

// ==========================================
// SIMULATOR 9: Functional Groups
// ==========================================
function setSim9Group(grp) {
    const formula = document.getElementById('sim9FormulaDisplay');
    const name = document.getElementById('sim9NameDisplay');
    const desc = document.getElementById('sim9DescDisplay');

    ['halo', 'alcohol', 'aldehyde', 'ketone', 'acid'].forEach(g => {
        const btn = document.getElementById('sim9Btn' + g.charAt(0).toUpperCase() + g.slice(1, 3));
    });

    if (grp === 'halo') {
        formula.textContent = 'CH3 – CH2 – Cl';
        name.textContent = 'Chloroethane (Haloalkane Family)';
        desc.textContent = 'Heteroatom chlorine replaces hydrogen, conferring distinct haloalkane properties.';
    } else if (grp === 'alcohol') {
        formula.textContent = 'CH3 – CH2 – OH';
        name.textContent = 'Ethanol (Alcohol Family, -OH)';
        desc.textContent = 'Hydroxyl group (-OH) enables hydrogen bonding and characteristic alcohol reactions.';
    } else if (grp === 'aldehyde') {
        formula.textContent = 'CH3 – CHO';
        name.textContent = 'Ethanal (Aldehyde Family, -CHO)';
        desc.textContent = 'Terminal carbonyl group (-CHO) with carbon bonded to oxygen and hydrogen.';
    } else if (grp === 'ketone') {
        formula.textContent = 'CH3 – CO – CH3';
        name.textContent = 'Propanone (Ketone Family, >C=O)';
        desc.textContent = 'Internal carbonyl group (>C=O) positioned between two carbon atoms.';
    } else if (grp === 'acid') {
        formula.textContent = 'CH3 – COOH';
        name.textContent = 'Ethanoic Acid (Carboxylic Acid Family, -COOH)';
        desc.textContent = 'Carboxyl group (-COOH) confers acidic properties, reacting with bases and carbonates.';
    }
}

// ==========================================
// SIMULATOR 11: IUPAC Naming Machine
// ==========================================
function updateIUPAC() {
    const n = parseInt(document.getElementById('sim11Chain').value);
    const func = document.getElementById('sim11Func').value;
    const outName = document.getElementById('sim11OutputName');
    const outFormula = document.getElementById('sim11FormulaText');

    const roots = ['', 'Meth', 'Eth', 'Prop', 'But', 'Pent', 'Hex'];
    const r = roots[n];

    if (func === 'alkane') {
        outName.textContent = r + 'ane';
        outFormula.textContent = `C${n}H${2*n+2}`;
    } else if (func === 'alkene') {
        if (n < 2) {
            outName.textContent = 'Alkenes require ≥ 2 carbons!';
            outFormula.textContent = '–';
        } else {
            outName.textContent = r + 'ene';
            outFormula.textContent = `C${n}H${2*n}`;
        }
    } else if (func === 'alkyne') {
        if (n < 2) {
            outName.textContent = 'Alkynes require ≥ 2 carbons!';
            outFormula.textContent = '–';
        } else {
            outName.textContent = r + 'yne';
            outFormula.textContent = `C${n}H${2*n-2}`;
        }
    } else if (func === 'alcohol') {
        outName.textContent = r + 'an-1-ol';
        outFormula.textContent = `C${n}H${2*n+1}OH`;
    } else if (func === 'aldehyde') {
        outName.textContent = r + 'anal';
        outFormula.textContent = `C${n-1}H${2*n-1}CHO`;
    } else if (func === 'ketone') {
        if (n < 3) {
            outName.textContent = 'Ketones require ≥ 3 carbons!';
            outFormula.textContent = '–';
        } else {
            outName.textContent = r + 'an-2-one';
            outFormula.textContent = `C${n}H${2*n}O`;
        }
    } else if (func === 'acid') {
        outName.textContent = r + 'anoic acid';
        outFormula.textContent = `C${n-1}H${2*n-1}COOH`;
    } else if (func === 'chloro') {
        outName.textContent = 'Chloro' + r.toLowerCase() + 'ane';
        outFormula.textContent = `C${n}H${2*n+1}Cl`;
    }
}

// ==========================================
// SIMULATOR 12: Combustion Flame
// ==========================================
function setSim12Vent(isOpen) {
    const vent = document.getElementById('sim12VentHole');
    const outer = document.getElementById('sim12OuterFlame');
    const inner = document.getElementById('sim12InnerFlame');
    const soot = document.getElementById('sim12Soot');
    const title = document.getElementById('sim12FlameTitle');
    const desc = document.getElementById('sim12FlameDesc');

    document.getElementById('sim12BtnOpen').className = isOpen ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim12BtnClosed').className = !isOpen ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';

    if (isOpen) {
        vent.setAttribute('fill', '#0f172a');
        outer.setAttribute('fill', '#38bdf8');
        inner.setAttribute('fill', '#67e8f9');
        soot.setAttribute('opacity', '0');
        title.textContent = 'Complete Combustion: Clean Blue Flame';
        desc.textContent = 'Adequate oxygen allows saturated gas to burn completely without forming soot.';
    } else {
        vent.setAttribute('fill', '#475569');
        outer.setAttribute('fill', '#f59e0b');
        inner.setAttribute('fill', '#ef4444');
        soot.setAttribute('opacity', '1');
        title.innerHTML = '<span class="text-amber-400 font-bold">Incomplete Combustion: Yellow Sooty Flame</span>';
        desc.textContent = 'Insufficient oxygen results in unburnt carbon particles depositing as black soot on cooking pots.';
    }
}

// ==========================================
// SIMULATOR 13: Oxidation of Alcohol
// ==========================================
function oxidiseAlcohol() {
    const liq = document.getElementById('sim13Liquid');
    const status = document.getElementById('sim13Status');

    liq.setAttribute('fill', '#f8fafc');
    liq.setAttribute('fill-opacity', '0.2');
    status.innerHTML = '<strong class="text-emerald-400">Oxidation Complete!</strong> Purple KMnO4 colour discharged. Ethanol oxidised cleanly into ethanoic acid: CH3CH2OH + 2[O] → CH3COOH + H2O.';
}

// ==========================================
// SIMULATOR 14: Addition vs Substitution
// ==========================================
function setSim14Mode(mode) {
    document.getElementById('sim14HydView').classList.toggle('hidden', mode !== 'hydrogenation');
    document.getElementById('sim14SubView').classList.toggle('hidden', mode !== 'substitution');

    document.getElementById('sim14BtnHyd').className = mode === 'hydrogenation' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim14BtnSub').className = mode === 'substitution' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

// ==========================================
// SIMULATOR 15: Reactions of Ethanol
// ==========================================
function setSim15Reaction(rxn) {
    document.getElementById('sim15NaView').classList.toggle('hidden', rxn !== 'sodium');
    document.getElementById('sim15DehydView').classList.toggle('hidden', rxn !== 'dehydrate');

    document.getElementById('sim15BtnNa').className = rxn === 'sodium' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim15BtnDehyd').className = rxn === 'dehydrate' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

// ==========================================
// SIMULATOR 16: Reactions of Ethanoic Acid
// ==========================================
function setSim16Mode(mode) {
    document.getElementById('sim16EsterView').classList.toggle('hidden', mode !== 'ester');
    document.getElementById('sim16FizzView').classList.toggle('hidden', mode !== 'fizz');

    document.getElementById('sim16BtnEster').className = mode === 'ester' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim16BtnFizz').className = mode === 'fizz' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}
'''

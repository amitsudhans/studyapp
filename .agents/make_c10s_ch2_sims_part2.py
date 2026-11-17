"""Interactive Simulators 9 to 16 for Class 10 Science Chapter 2: Acids, Bases and Salts
"""

simulators = {
    9: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.10: Exothermic Dilution & Laboratory Safety</h4>
        <span class="text-xs text-slate-400">Thermodynamics: Heat of Hydration</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <svg viewBox="0 0 220 180" class="w-full h-44 mx-auto">
                <!-- Beaker -->
                <rect x="50" y="40" width="120" height="110" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
                <!-- Liquid in beaker -->
                <rect id="sim9Liquid" x="52" y="80" width="116" height="68" rx="6" fill="#38bdf8" fill-opacity="0.3" class="transition-colors duration-500"/>
                <!-- Thermometer in beaker -->
                <rect x="135" y="10" width="8" height="135" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
                <rect id="sim9Mercury" x="137" y="100" width="4" height="42" fill="#ef4444" class="transition-all duration-700"/>
                <circle cx="139" cy="140" r="5" fill="#ef4444"/>
                <text id="sim9TempText" x="155" y="85" font-size="9" fill="#ef4444" font-weight="bold">25°C</text>

                <!-- Dropper / Flask above -->
                <g id="sim9Dropper" transform="translate(80, 5)">
                    <rect x="10" y="0" width="14" height="30" rx="2" fill="#64748b"/>
                    <polygon points="12,30 22,30 17,45" fill="#64748b"/>
                    <circle id="sim9Drop" cx="17" cy="55" r="3.5" fill="#ef4444" class="opacity-0 transition-opacity duration-300"/>
                </g>

                <!-- Spurting / Danger hazard effects -->
                <g id="sim9SpurtHazard" class="hidden">
                    <circle cx="110" cy="80" r="30" fill="#ef4444" fill-opacity="0.25" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
                    <text x="110" y="75" font-size="10" fill="#fca5a5" font-weight="extrabold" text-anchor="middle">FLASH BOILING!</text>
                    <text x="110" y="90" font-size="8" fill="#fecaca" text-anchor="middle">Violent Acid Spurting</text>
                </g>
            </svg>

            <div class="space-y-2.5 text-xs">
                <span class="text-slate-400 block font-semibold">Test Protocol Comparison:</span>
                <div class="flex gap-2">
                    <button onclick="runDilution('correct')" id="sim9BtnCorrect" class="flex-1 py-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 font-bold">1. Acid Added to Water (Safe)</button>
                    <button onclick="runDilution('wrong')" id="sim9BtnWrong" class="flex-1 py-1.5 rounded-lg bg-rose-600/30 text-rose-300 border border-rose-500/40 font-bold">2. Water into Acid (HAZARD!)</button>
                </div>
                <div id="sim9Result" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
                    Select a protocol above to simulate the thermodynamic outcome of acid dilution.
                </div>
                <div class="p-2 rounded bg-amber-500/10 border border-amber-500/30 text-[11px] text-amber-300">
                    <strong>Rule:</strong> Dilution steadily <em>decreases</em> the concentration of hydronium ions (H3O+) or hydroxide ions (OH-) per unit volume of solution.
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function runDilution(type) {
    const merc = document.getElementById('sim9Mercury');
    const tText = document.getElementById('sim9TempText');
    const spurt = document.getElementById('sim9SpurtHazard');
    const res = document.getElementById('sim9Result');
    const drop = document.getElementById('sim9Drop');

    drop.classList.remove('opacity-0');

    if (type === 'correct') {
        spurt.classList.add('hidden');
        merc.setAttribute('y', '60');
        merc.setAttribute('height', '82');
        tText.textContent = '48°C (Hot)';
        tText.setAttribute('y', '65');
        res.innerHTML = '<span class="text-emerald-400 font-bold">SAFE PROTOCOL:</span> Adding concentrated acid dropwise into water with constant stirring allows the large mass of water to dissipate the heat of hydration smoothly. The beaker becomes hot but does not boil or spurt!';
    } else {
        spurt.classList.remove('hidden');
        merc.setAttribute('y', '25');
        merc.setAttribute('height', '117');
        tText.textContent = '>100°C (Boiling)';
        tText.setAttribute('y', '30');
        res.innerHTML = '<span class="text-rose-400 font-extrabold">EXTREME DANGER:</span> Water poured into concentrated acid causes localized flash boiling in the small droplet. The boiling steam spurts corrosive concentrated acid outwards, breaking glass beakers and causing chemical burns!';
    }
}
</script>
''',

    10: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.11: Universal Indicator & pH Scale Simulator</h4>
        <span class="text-xs text-slate-400">pH = -log₁₀[H⁺] • Scale: 0 to 14</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-3">
        <!-- Rainbow Strip -->
        <div class="space-y-1">
            <div class="h-6 rounded-lg overflow-hidden flex shadow-inner border border-slate-700">
                <div class="flex-1 bg-red-600"></div>
                <div class="flex-1 bg-red-500"></div>
                <div class="flex-1 bg-orange-500"></div>
                <div class="flex-1 bg-amber-500"></div>
                <div class="flex-1 bg-yellow-400"></div>
                <div class="flex-1 bg-lime-400"></div>
                <div class="flex-1 bg-green-500"></div>
                <div class="flex-1 bg-emerald-500"></div>
                <div class="flex-1 bg-teal-500"></div>
                <div class="flex-1 bg-cyan-600"></div>
                <div class="flex-1 bg-blue-600"></div>
                <div class="flex-1 bg-indigo-600"></div>
                <div class="flex-1 bg-purple-600"></div>
                <div class="flex-1 bg-violet-700"></div>
                <div class="flex-1 bg-purple-900"></div>
            </div>
            <div class="flex justify-between text-[10px] text-slate-400 px-1 font-mono">
                <span>0 (Strong Acid)</span>
                <span>7 (Neutral)</span>
                <span>14 (Strong Base)</span>
            </div>
        </div>

        <!-- Interactive Slider -->
        <div class="space-y-1.5">
            <div class="flex justify-between items-center text-xs">
                <span class="text-slate-300">Adjust Solution pH:</span>
                <span id="sim10PhDisplay" class="font-bold text-base px-2 py-0.5 rounded bg-green-500/20 text-green-300 border border-green-500/40">pH 7.0</span>
            </div>
            <input type="range" id="sim10Slider" min="0" max="14" step="0.1" value="7" class="w-full accent-amber-500 cursor-pointer" oninput="updateSim10Ph(this.value)">
        </div>

        <!-- Quick Everyday Substance Buttons -->
        <div class="flex flex-wrap gap-1.5 text-xs">
            <span class="text-slate-400 self-center mr-1 text-[11px]">Daily Liquids:</span>
            <button onclick="setSim10Preset(1.2)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Gastric Juice (1.2)</button>
            <button onclick="setSim10Preset(2.2)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Lemon (2.2)</button>
            <button onclick="setSim10Preset(3.0)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Soda (3.0)</button>
            <button onclick="setSim10Preset(5.0)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Coffee (5.0)</button>
            <button onclick="setSim10Preset(7.0)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Water (7.0)</button>
            <button onclick="setSim10Preset(7.4)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Blood/Saliva (7.4)</button>
            <button onclick="setSim10Preset(10.0)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Mg(OH)2 (10.0)</button>
            <button onclick="setSim10Preset(14.0)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">1M NaOH (14.0)</button>
        </div>

        <div id="sim10Details" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            <strong>Neutral Solution:</strong> [H⁺] = 1.0 × 10⁻⁷ M, [OH⁻] = 1.0 × 10⁻⁷ M. Universal indicator displays an emerald green colour.
        </div>
    </div>
</div>

<script>
function getPhColor(ph) {
    if (ph < 2) return { col: '#dc2626', name: 'Dark Red', type: 'Strongly Acidic' };
    if (ph < 4) return { col: '#ea580c', name: 'Orange-Red', type: 'Moderately Acidic' };
    if (ph < 6) return { col: '#facc15', name: 'Yellow', type: 'Weakly Acidic' };
    if (ph < 6.8) return { col: '#a3e635', name: 'Yellow-Green', type: 'Mildly Acidic' };
    if (ph <= 7.4) return { col: '#22c55e', name: 'Emerald Green', type: 'Neutral' };
    if (ph < 9) return { col: '#0d9488', name: 'Greenish-Blue', type: 'Mildly Alkaline' };
    if (ph < 11) return { col: '#2563eb', name: 'Blue', type: 'Moderately Basic' };
    if (ph < 13) return { col: '#7c3aed', name: 'Violet', type: 'Strongly Basic' };
    return { col: '#581c87', name: 'Deep Purple', type: 'Extremely Alkaline' };
}

function updateSim10Ph(val) {
    const ph = parseFloat(val);
    const info = getPhColor(ph);
    const disp = document.getElementById('sim10PhDisplay');
    disp.textContent = 'pH ' + ph.toFixed(1) + ' (' + info.type + ')';
    disp.style.backgroundColor = info.col + '33';
    disp.style.color = info.col;
    disp.style.borderColor = info.col + '88';

    const hConc = Math.pow(10, -ph).toExponential(2);
    const ohConc = Math.pow(10, -(14 - ph)).toExponential(2);

    document.getElementById('sim10Details').innerHTML = 
        '<strong>Universal Indicator Colour:</strong> <span style="color:' + info.col + '; font-weight:bold;">' + info.name + '</span><br>' +
        '<strong>Ion Concentrations:</strong> [H₃O⁺] = ' + hConc + ' M | [OH⁻] = ' + ohConc + ' M.<br>' +
        (ph < 7 ? 'Higher [H₃O⁺] than [OH⁻]. Lower numerical pH indicates higher acidic strength.' :
         ph === 7 ? 'Perfect balance between hydronium and hydroxide ions (Pure water).' :
         'Higher [OH⁻] than [H₃O⁺]. Higher numerical pH indicates higher basic strength.');
}

function setSim10Preset(val) {
    document.getElementById('sim10Slider').value = val;
    updateSim10Ph(val);
}
</script>
''',

    11: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.12: Everyday pH Regulation & Ecological Balances</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim11Mode('body')" id="sim11BtnBody" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Human Body</button>
            <button onclick="setSim11Mode('rain')" id="sim11BtnRain" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Acid Rain</button>
            <button onclick="setSim11Mode('soil')" id="sim11BtnSoil" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Soil Treatment</button>
        </div>
    </div>

    <!-- Mode 1: Human Body pH -->
    <div id="sim11BodyView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center gap-3">
            <div class="text-3xl">🫀</div>
            <div>
                <span class="font-bold text-slate-200 block text-sm">Human Body pH Window: 7.0 to 7.8</span>
                <p class="text-slate-400 text-[11px]">Our biological enzymes function within this narrow range. Blood is regulated near 7.4 by the carbonic acid-bicarbonate buffer system.</p>
            </div>
        </div>
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
            <strong>Venusian Planetary Atmosphere:</strong> The planet Venus is covered with dense, opaque clouds of concentrated <strong>sulphuric acid</strong>, creating a permanently toxic hyper-acidic environment.
        </div>
    </div>

    <!-- Mode 2: Acid Rain -->
    <div id="sim11RainView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center">
            <span class="font-bold text-rose-400">Rainwater pH Threshold:</span>
            <span id="sim11RainPh" class="font-bold font-mono text-amber-400">pH 4.8 (Acid Rain)</span>
        </div>
        <input type="range" min="3.5" max="6.5" step="0.1" value="4.8" class="w-full accent-rose-500 cursor-pointer" oninput="updateRainSim(this.value)">
        <div id="sim11RainImpact" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
            <strong>Acid Rain (pH < 5.6):</strong> When rainwater pH drops below 5.6 due to dissolved SO2 and NO2 emissions, river water acidifies, leaching aluminium into water and severely harming aquatic fish reproduction.
        </div>
    </div>

    <!-- Mode 3: Soil Testing & Treatment -->
    <div id="sim11SoilView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center">
            <span class="font-bold text-slate-300">Agricultural Soil Condition:</span>
            <span id="sim11SoilBadge" class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 font-bold">Acidic Soil (pH 4.5)</span>
        </div>
        <p class="text-slate-400 text-[11px]">Crops grow best in neutral/slightly alkaline soil (pH 6.5–7.5). Select an agricultural amendment to neutralise soil acids:</p>
        <div class="flex flex-wrap gap-2">
            <button onclick="applySoilBase('quicklime')" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Add Quicklime (CaO)</button>
            <button onclick="applySoilBase('slaked')" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">Add Slaked Lime [Ca(OH)2]</button>
            <button onclick="applySoilBase('chalk')" class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-bold transition">Add Chalk (CaCO3)</button>
            <button onclick="resetSoilSim()" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300">Reset</button>
        </div>
        <div id="sim11SoilExplain" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
            Soil filtrate tests red on universal indicator paper (pH ~4.5). Crop yields will be severely stunted unless treated with an agricultural base.
        </div>
    </div>
</div>

<script>
function setSim11Mode(mode) {
    document.getElementById('sim11BodyView').classList.toggle('hidden', mode !== 'body');
    document.getElementById('sim11RainView').classList.toggle('hidden', mode !== 'rain');
    document.getElementById('sim11SoilView').classList.toggle('hidden', mode !== 'soil');
    document.getElementById('sim11BtnBody').className = mode === 'body' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim11BtnRain').className = mode === 'rain' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim11BtnSoil').className = mode === 'soil' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function updateRainSim(val) {
    const ph = parseFloat(val);
    const rPh = document.getElementById('sim11RainPh');
    const imp = document.getElementById('sim11RainImpact');
    rPh.textContent = 'pH ' + ph.toFixed(1) + (ph < 5.6 ? ' (Acid Rain)' : ' (Normal Rain)');
    if (ph < 5.6) {
        rPh.className = 'font-bold font-mono text-rose-400';
        imp.innerHTML = '<strong>Acid Rain Active (pH < 5.6):</strong> Corrosive precipitation lowers lake pH, leaches toxic minerals, and degrades calcium carbonate in stone monuments (marble cancer).';
    } else {
        rPh.className = 'font-bold font-mono text-emerald-400';
        imp.innerHTML = '<strong>Normal Rain (pH ~5.6 to 6.2):</strong> Weak carbonic acid from dissolved atmospheric CO2 is safe and natural for aquatic life and soil flora.';
    }
}

function applySoilBase(type) {
    const badge = document.getElementById('sim11SoilBadge');
    badge.textContent = 'Neutralized Optimal Soil (pH 7.0)';
    badge.className = 'px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold';
    const name = type === 'quicklime' ? 'Quicklime (CaO)' : type === 'slaked' ? 'Slaked Lime [Ca(OH)2]' : 'Chalk (CaCO3)';
    document.getElementById('sim11SoilExplain').innerHTML = '<span class="text-emerald-400 font-bold">Soil Successfully Neutralised!</span> ' + name + ' reacted with acidic hydronium ions in soil moisture, restoring optimal agricultural pH (7.0) for bumper crop harvest!';
}

function resetSoilSim() {
    const badge = document.getElementById('sim11SoilBadge');
    badge.textContent = 'Acidic Soil (pH 4.5)';
    badge.className = 'px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 font-bold';
    document.getElementById('sim11SoilExplain').textContent = 'Soil filtrate tests red on universal indicator paper (pH ~4.5). Crop yields will be stunted unless treated.';
}
</script>
''',

    12: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Chemical Warfare in Nature & Physiological Defence</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim12Tab('stomach')" id="sim12BtnStomach" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Stomach Acidity</button>
            <button onclick="setSim12Tab('tooth')" id="sim12BtnTooth" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Tooth Decay</button>
            <button onclick="setSim12Tab('sting')" id="sim12BtnSting" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Bee/Nettle Stings</button>
        </div>
    </div>

    <!-- Stomach Acidity & Antacids -->
    <div id="sim12StomachView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center gap-3">
            <div class="text-3xl">🫃</div>
            <div>
                <span class="font-bold text-slate-200 block text-sm">Hyperacidity & Antacid Neutralisation</span>
                <p class="text-slate-400 text-[11px]">Gastric juice contains hydrochloric acid (pH 1.2–2.0). Overproduction causes acute indigestion.</p>
            </div>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
            <button onclick="treatStomach('antacid')" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">Administer Milk of Magnesia [Mg(OH)2]</button>
            <button onclick="treatStomach('baking')" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">Administer Baking Soda [NaHCO3]</button>
        </div>
        <div id="sim12StomachStatus" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
            Excess HCl causes irritation and heartburn. Click a mild basic antacid to observe chemical neutralisation.
        </div>
    </div>

    <!-- Tooth Decay -->
    <div id="sim12ToothView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center gap-3">
            <div class="text-3xl">🦷</div>
            <div>
                <span class="font-bold text-slate-200 block text-sm">Tooth Enamel Corrosion Threshold: pH < 5.5</span>
                <p class="text-slate-400 text-[11px]">Enamel consists of calcium hydroxyapatite [Ca5(PO4)3(OH)].</p>
            </div>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
            <button onclick="simulateTooth('sugar')" class="px-3 py-1.5 rounded-lg bg-rose-600/30 text-rose-300 border border-rose-500/40 font-bold">1. Bacterial Sugar Fermentation</button>
            <button onclick="simulateTooth('brush')" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">2. Brush with Basic Toothpaste</button>
        </div>
        <div id="sim12ToothStatus" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
            Click <strong>1. Bacterial Sugar Fermentation</strong> to drop salivary pH below 5.5.
        </div>
    </div>

    <!-- Bee and Nettle Stings -->
    <div id="sim12StingView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center gap-3">
            <div class="text-3xl">🐝 🌿</div>
            <div>
                <span class="font-bold text-slate-200 block text-sm">Methanoic Acid (Formic Acid) Envenomation</span>
                <p class="text-slate-400 text-[11px]">Honeybee stings and stinging nettle hair trichomes inject methanoic acid (HCOOH).</p>
            </div>
        </div>
        <div class="flex flex-wrap gap-2 pt-1">
            <button onclick="remedySting('baking')" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Apply Baking Soda (Bee Sting)</button>
            <button onclick="remedySting('dock')" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">Rub Dock Plant Leaf (Nettle Sting)</button>
        </div>
        <div id="sim12StingStatus" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
            Select a natural or household basic remedy to neutralize the burning acid venom.
        </div>
    </div>
</div>

<script>
function setSim12Tab(tab) {
    document.getElementById('sim12StomachView').classList.toggle('hidden', tab !== 'stomach');
    document.getElementById('sim12ToothView').classList.toggle('hidden', tab !== 'tooth');
    document.getElementById('sim12StingView').classList.toggle('hidden', tab !== 'sting');
    document.getElementById('sim12BtnStomach').className = tab === 'stomach' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim12BtnTooth').className = tab === 'tooth' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim12BtnSting').className = tab === 'sting' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function treatStomach(med) {
    const stat = document.getElementById('sim12StomachStatus');
    if (med === 'antacid') {
        stat.innerHTML = '<span class="text-emerald-400 font-bold">Neutralisation:</span> Mg(OH)2 + 2HCl → MgCl2 + 2H2O. Milk of Magnesia safely neutralises excess gastric acid without irritating stomach walls!';
    } else {
        stat.innerHTML = '<span class="text-teal-400 font-bold">Neutralisation:</span> NaHCO3 + HCl → NaCl + H2O + CO2↑. Baking soda rapidly reduces acidity with a refreshing release of gas.';
    }
}

function simulateTooth(step) {
    const stat = document.getElementById('sim12ToothStatus');
    if (step === 'sugar') {
        stat.innerHTML = '<span class="text-rose-400 font-bold">Acid Attack! Oral pH Drops to 4.8 (< 5.5):</span> Bacterial breakdown of residual sugars produces lactic acid, demineralising and corroding calcium hydroxyapatite enamel.';
    } else {
        stat.innerHTML = '<span class="text-emerald-400 font-bold">Enamel Protection! pH Restored to 7.2:</span> Alkaline toothpastes neutralise bacterial acids, preventing dental decay and cavities!';
    }
}

function remedySting(rem) {
    const stat = document.getElementById('sim12StingStatus');
    if (rem === 'baking') {
        stat.innerHTML = '<span class="text-emerald-400 font-bold">Bee Sting Relieved:</span> Alkaline baking soda paste neutralises acidic venom: HCOOH + NaHCO3 → HCOONa + H2O + CO2, eliminating pain and swelling!';
    } else {
        stat.innerHTML = '<span class="text-emerald-400 font-bold">Dock Leaf Remedy Applied:</span> Mild alkaline sap from wild dock leaves neutralises methanoic acid injected by nettle hairs directly on the skin.';
    }
}
</script>
''',

    13: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Table 2.3: Natural Organic Acids & Cookware Compatibility</h4>
        <span class="text-xs text-slate-400">Naturally Occurring Carboxylic Acids</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-3">
        <p class="text-xs text-slate-300">Click any natural food or biological source to inspect its characteristic organic acid:</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 text-center text-xs">
            <button onclick="showAcidCard('vinegar')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 transition">
                <span class="text-xl block mb-1">🍶</span>
                <span class="font-bold text-slate-200">Vinegar</span>
                <span class="text-[10px] text-amber-400 block mt-0.5">Acetic Acid</span>
            </button>
            <button onclick="showAcidCard('lemon')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 transition">
                <span class="text-xl block mb-1">🍋 🍊</span>
                <span class="font-bold text-slate-200">Orange / Lemon</span>
                <span class="text-[10px] text-amber-400 block mt-0.5">Citric Acid</span>
            </button>
            <button onclick="showAcidCard('tamarind')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 transition">
                <span class="text-xl block mb-1">🫘</span>
                <span class="font-bold text-slate-200">Tamarind</span>
                <span class="text-[10px] text-amber-400 block mt-0.5">Tartaric Acid</span>
            </button>
            <button onclick="showAcidCard('tomato')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 transition">
                <span class="text-xl block mb-1">🍅</span>
                <span class="font-bold text-slate-200">Tomato</span>
                <span class="text-[10px] text-amber-400 block mt-0.5">Oxalic Acid</span>
            </button>
            <button onclick="showAcidCard('curd')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 transition">
                <span class="text-xl block mb-1">🥛</span>
                <span class="font-bold text-slate-200">Sour Milk (Curd)</span>
                <span class="text-[10px] text-amber-400 block mt-0.5">Lactic Acid</span>
            </button>
            <button onclick="showAcidCard('sting')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 transition">
                <span class="text-xl block mb-1">🐜 🌿</span>
                <span class="font-bold text-slate-200">Ant / Nettle Sting</span>
                <span class="text-[10px] text-amber-400 block mt-0.5">Methanoic Acid</span>
            </button>
        </div>

        <div id="sim13CardDetails" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Select a card above to view formula, chemical properties, and culinary significance.
        </div>

        <div class="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300">
            <strong>Cookware Safety Warning:</strong> Never store pickles, curd, or citrus juices in brass or copper vessels! Organic acids react with copper and zinc to form toxic, poisonous metallic salts. Conversely, tarnished copper pots are cleaned by rubbing with acidic lemon slices to dissolve basic copper carbonate patinas.
        </div>
    </div>
</div>

<script>
const sim13Data = {
    vinegar: { name: 'Acetic Acid (Ethanoic Acid)', formula: 'CH3COOH', desc: 'Pungent preservation liquid in pickles; inhibits bacterial putrefaction.' },
    lemon: { name: 'Citric Acid', formula: 'C6H8O7', desc: 'Natural antioxidant and refreshing sour constituent in oranges, lemons, and grapefruits.' },
    tamarind: { name: 'Tartaric Acid', formula: 'C4H6O6', desc: 'Abundant in tamarind and unripened grapes; added to baking soda to formulate baking powder.' },
    tomato: { name: 'Oxalic Acid', formula: '(COOH)2 or C2H2O4', desc: 'Dicarboxylic acid present in tomatoes and spinach; can form insoluble calcium oxalate crystals.' },
    curd: { name: 'Lactic Acid', formula: 'CH3CH(OH)COOH', desc: 'Synthesized by Lactobacillus bacteria fermenting lactose sugar in warm milk into creamy curd.' },
    sting: { name: 'Methanoic Acid (Formic Acid)', formula: 'HCOOH', desc: 'Single-carbon carboxylic acid injected by ant stings and nettle stinging hairs.' }
};

function showAcidCard(item) {
    const d = sim13Data[item];
    document.getElementById('sim13CardDetails').innerHTML = 
        '<strong class="text-amber-400">' + d.name + '</strong> (Formula: <span class="font-mono text-cyan-300">' + d.formula + '</span>)<br>' +
        d.desc;
}
</script>
''',

    14: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.13 & 2.14: Salt Families & Solution Hydrolysis pH</h4>
        <span class="text-xs text-slate-400">Parent Acid + Parent Base Classification</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-3">
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-center text-xs">
            <button onclick="testSaltHydrolysis('neutral')" id="sim14BtnNeutral" class="p-2.5 rounded-xl bg-emerald-600/20 border border-emerald-500/40 font-bold text-emerald-300">
                <span>NaCl (Sodium Chloride)</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-1">Strong Acid + Strong Base</span>
            </button>
            <button onclick="testSaltHydrolysis('acidic')" id="sim14BtnAcidic" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 font-bold text-slate-300">
                <span>NH4Cl (Ammonium Chloride)</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-1">Strong Acid + Weak Base</span>
            </button>
            <button onclick="testSaltHydrolysis('basic')" id="sim14BtnBasic" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 font-bold text-slate-300">
                <span>Na2CO3 (Sodium Carbonate)</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-1">Weak Acid + Strong Base</span>
            </button>
        </div>

        <div id="sim14Details" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            <strong>Sodium Chloride (NaCl):</strong> Parent acid is strong HCl; parent base is strong NaOH.<br>
            <span class="text-emerald-400 font-bold">Solution pH = 7 (Neutral):</span> Neither cation nor anion hydrolyses. Universal indicator turns green!
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] text-slate-300 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
            <div><strong>Sodium Salt Family:</strong> NaCl, Na2SO4, NaNO3, Na2CO3 (share Na⁺).</div>
            <div><strong>Chloride Salt Family:</strong> NaCl, KCl, CaCl2, MgCl2, NH4Cl (share Cl⁻).</div>
        </div>
    </div>
</div>

<script>
function testSaltHydrolysis(type) {
    const bNeu = document.getElementById('sim14BtnNeutral');
    const bAci = document.getElementById('sim14BtnAcidic');
    const bBas = document.getElementById('sim14BtnBasic');
    const det = document.getElementById('sim14Details');

    bNeu.className = type === 'neutral' ? 'p-2.5 rounded-xl bg-emerald-600/20 border border-emerald-500/40 font-bold text-emerald-300' : 'p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 font-bold text-slate-300';
    bAci.className = type === 'acidic' ? 'p-2.5 rounded-xl bg-rose-600/20 border border-rose-500/40 font-bold text-rose-300' : 'p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 font-bold text-slate-300';
    bBas.className = type === 'basic' ? 'p-2.5 rounded-xl bg-blue-600/20 border border-blue-500/40 font-bold text-blue-300' : 'p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 font-bold text-slate-300';

    if (type === 'neutral') {
        det.innerHTML = '<strong>Sodium Chloride (NaCl):</strong> Parent Acid: Strong HCl | Parent Base: Strong NaOH.<br><span class="text-emerald-400 font-bold">Aqueous Solution: pH = 7.0 (Neutral).</span> Neither cation nor anion hydrolyses with water.';
    } else if (type === 'acidic') {
        det.innerHTML = '<strong>Ammonium Chloride (NH4Cl):</strong> Parent Acid: Strong HCl | Parent Base: Weak NH4OH.<br><span class="text-rose-400 font-bold">Aqueous Solution: pH < 7 (Acidic ~5.2).</span> NH4⁺ undergoes cation hydrolysis: NH4⁺ + H2O ⇌ NH3 + H3O⁺, releasing hydronium ions.';
    } else {
        det.innerHTML = '<strong>Sodium Carbonate (Na2CO3):</strong> Parent Acid: Weak H2CO3 | Parent Base: Strong NaOH.<br><span class="text-cyan-400 font-bold">Aqueous Solution: pH > 7 (Basic ~11.5).</span> CO3²⁻ undergoes anion hydrolysis: CO3²⁻ + H2O ⇌ HCO3⁻ + OH⁻, producing alkaline hydroxide ions.';
    }
}
</script>
''',

    15: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Industrial Chlor-Alkali Process (Brine Electrolysis)</h4>
        <span class="text-xs font-mono text-cyan-300">2NaCl(aq) + 2H2O(l) → 2NaOH + Cl2↑ + H2↑</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <svg viewBox="0 0 240 180" class="w-full h-44 mx-auto">
                <!-- Electrolytic Cell Container -->
                <rect x="20" y="20" width="200" height="140" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
                <!-- Brine liquid -->
                <rect x="22" y="60" width="196" height="98" fill="#0284c7" fill-opacity="0.25"/>
                <!-- Semipermeable Cation Membrane Divider -->
                <line x1="120" y1="40" x2="120" y2="158" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
                <text x="120" y="32" font-size="7" fill="#fbbf24" font-weight="bold" text-anchor="middle">Membrane</text>

                <!-- Anode (+) Left -->
                <rect x="55" y="45" width="14" height="95" rx="3" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
                <text x="62" y="40" font-size="8" fill="#34d399" font-weight="bold" text-anchor="middle">Anode (+)</text>
                <!-- Cl2 gas bubbles -->
                <circle cx="58" cy="80" r="3" fill="#bef264" opacity="0.8"/>
                <circle cx="66" cy="65" r="3.5" fill="#bef264" opacity="0.8"/>
                <text x="62" y="152" font-size="8" fill="#bef264" font-weight="bold" text-anchor="middle">Cl2 Gas ↑</text>

                <!-- Cathode (-) Right -->
                <rect x="170" y="45" width="14" height="95" rx="3" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5"/>
                <text x="177" y="40" font-size="8" fill="#60a5fa" font-weight="bold" text-anchor="middle">Cathode (-)</text>
                <!-- H2 gas bubbles -->
                <circle cx="173" cy="80" r="2.5" fill="#e0f2fe" opacity="0.8"/>
                <circle cx="180" cy="65" r="3" fill="#e0f2fe" opacity="0.8"/>
                <text x="177" y="152" font-size="8" fill="#e0f2fe" font-weight="bold" text-anchor="middle">H2 Gas ↑</text>

                <!-- NaOH formation -->
                <text x="177" y="125" font-size="7" fill="#f43f5e" font-weight="bold" text-anchor="middle">NaOH (aq)</text>
            </svg>

            <div class="space-y-2 text-xs">
                <span class="text-slate-400 block font-semibold">Inspect Industrial Co-Products:</span>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="showChlorProduct('Cl2')" id="sim15BtnCl2" class="p-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 font-bold">Chlorine (Cl2)</button>
                    <button onclick="showChlorProduct('H2')" id="sim15BtnH2" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold">Hydrogen (H2)</button>
                    <button onclick="showChlorProduct('NaOH')" id="sim15BtnNaOH" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold">Alkali (NaOH)</button>
                </div>
                <div id="sim15Details" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
                    <strong>Chlorine Gas (Anode):</strong> Water disinfection, swimming pool treatment, manufacturing PVC plastics, disinfectants, and CFCs.
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function showChlorProduct(prod) {
    ['Cl2', 'H2', 'NaOH'].forEach(p => {
        document.getElementById('sim15Btn' + p).className = (p === prod) ? 'p-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 font-bold' : 'p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold';
    });
    const det = document.getElementById('sim15Details');
    if (prod === 'Cl2') {
        det.innerHTML = '<strong>Chlorine Gas (Liberated at Anode):</strong> Used for municipal drinking water purification, PVC pipes, bleaching agents, disinfectants, and pesticides.';
    } else if (prod === 'H2') {
        det.innerHTML = '<strong>Hydrogen Gas (Liberated at Cathode):</strong> Clean fuel, rocket propellants, hydrogenation of vegetable oils to margarine, and feedstock for industrial ammonia fertilizer synthesis.';
    } else {
        det.innerHTML = '<strong>Sodium Hydroxide (Formed near Cathode):</strong> Essential alkali for metal degreasing, soap and detergent manufacturing, paper pulp chemical processing, and artificial textile fibres.';
    }
}
</script>
''',

    16: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Commercial Salt Derivatives & Water of Crystallisation</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim16Tab('bleach')" id="sim16BtnBleach" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Bleaching Powder</button>
            <button onclick="setSim16Tab('baking')" id="sim16BtnBaking" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Baking Soda</button>
            <button onclick="setSim16Tab('washing')" id="sim16BtnWashing" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Washing Soda</button>
            <button onclick="setSim16Tab('pop')" id="sim16BtnPop" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Plaster of Paris</button>
        </div>
    </div>

    <!-- Bleaching Powder View -->
    <div id="sim16BleachView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center">
            <span class="font-bold text-slate-200">Bleaching Powder (Calcium Oxychloride): CaOCl2</span>
            <span class="text-emerald-400 font-mono text-[11px]">Ca(OH)2 + Cl2 → CaOCl2 + H2O</span>
        </div>
        <p class="text-slate-300 leading-relaxed">
            Prepared by the action of chlorine gas on dry slaked lime. Functions as a potent oxidizing agent, textile bleach for cotton/linen, wood pulp bleaching in paper mills, and germicidal disinfectant for municipal drinking water.
        </p>
    </div>

    <!-- Baking Soda View -->
    <div id="sim16BakingView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center">
            <span class="font-bold text-slate-200">Baking Soda (Sodium Hydrogencarbonate): NaHCO3</span>
            <span class="text-amber-400 font-mono text-[11px]">2NaHCO3 -Δ→ Na2CO3 + H2O + CO2↑</span>
        </div>
        <p class="text-slate-300 leading-relaxed">
            Synthesized via the Solvay process. Heating releases CO2 bubbles, making cakes soft and spongy. <strong>Baking powder</strong> mixes baking soda with mild edible tartaric acid to neutralize bitter sodium carbonate and synthesize additional CO2. Also used in soda-acid fire extinguishers.
        </p>
    </div>

    <!-- Washing Soda View -->
    <div id="sim16WashingView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center">
            <span class="font-bold text-slate-200">Washing Soda (Sodium Carbonate Decahydrate): Na2CO3·10H2O</span>
            <span class="text-cyan-400 font-mono text-[11px]">Na2CO3 + 10H2O → Na2CO3·10H2O</span>
        </div>
        <p class="text-slate-300 leading-relaxed">
            Recrystallised sodium carbonate containing 10 water molecules of crystallisation. Essential in glass, soap, and paper factories, domestic cleaning detergents, manufacturing borax, and <strong>removing permanent hardness of water</strong>.
        </p>
    </div>

    <!-- Plaster of Paris View -->
    <div id="sim16PopView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center">
            <span class="font-bold text-slate-200">Plaster of Paris: CaSO4·½H2O</span>
            <span class="text-teal-400 font-mono text-[11px]">Gypsum (CaSO4·2H2O) -373K→ CaSO4·½H2O + 1½H2O</span>
        </div>
        <p class="text-slate-300 leading-relaxed">
            Heating gypsum at carefully controlled 373 K (100°C) produces calcium sulphate hemihydrate. On mixing with water, it sets into a hard solid mass of interlocking gypsum crystals within 10–15 minutes. Used for setting fractured bones, making casts, toys, and smooth wall plaster.
        </p>
    </div>
</div>

<script>
function setSim16Tab(tab) {
    document.getElementById('sim16BleachView').classList.toggle('hidden', tab !== 'bleach');
    document.getElementById('sim16BakingView').classList.toggle('hidden', tab !== 'baking');
    document.getElementById('sim16WashingView').classList.toggle('hidden', tab !== 'washing');
    document.getElementById('sim16PopView').classList.toggle('hidden', tab !== 'pop');

    ['Bleach', 'Baking', 'Washing', 'Pop'].forEach(t => {
        document.getElementById('sim16Btn' + t).className = (t.toLowerCase() === tab) ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    });
}
</script>
'''
}

if __name__ == "__main__":
    for k, v in simulators.items():
        print(f"Simulator {k}: length {len(v)} chars")
    print("All simulators 9 to 16 defined successfully!")

"""Interactive Simulators 9 to 16 for Class 10 Science Chapter 4: Carbon and its Compounds
High-fidelity, responsive, SVG-based laboratory simulators with Tailwind CSS.
"""

simulators = {
    9: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Table 4.3: Functional Groups & Heteroatoms</h4>
        <div class="flex flex-wrap gap-1 text-xs">
            <button onclick="setSim9Group('halo')" id="sim9BtnHalo" class="px-2 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Halo (-Cl)</button>
            <button onclick="setSim9Group('alcohol')" id="sim9BtnAlc" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Alcohol (-OH)</button>
            <button onclick="setSim9Group('aldehyde')" id="sim9BtnAld" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Aldehyde (-CHO)</button>
            <button onclick="setSim9Group('ketone')" id="sim9BtnKet" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Ketone (>C=O)</button>
            <button onclick="setSim9Group('acid')" id="sim9BtnAcd" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Acid (-COOH)</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <div id="sim9FormulaDisplay" class="font-mono text-base text-amber-300">
            CH3 – CH2 – Cl
        </div>
        <span id="sim9NameDisplay" class="font-bold text-xs text-sky-400 block">Chloroethane (Haloalkane Family)</span>
        <p id="sim9DescDisplay" class="text-[11px] text-slate-400">Heteroatom chlorine replaces hydrogen, conferring distinct haloalkane properties.</p>
    </div>
</div>
''',

    10: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Homologous Series: -CH2- / 14u Gradation</h4>
        <span class="text-xs text-sky-300 font-mono">Alcohols: R–OH</span>
    </div>

    <div class="grid grid-cols-4 gap-2 text-center text-xs">
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-sky-300 block">Methanol</span>
            <span class="text-[10px] text-slate-400 font-mono block">CH3OH</span>
            <div class="mt-2 text-[11px] text-slate-300">Mass: 32 u</div>
            <div class="text-[11px] text-amber-400">BP: 337 K</div>
        </div>
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-indigo-300 block">Ethanol</span>
            <span class="text-[10px] text-slate-400 font-mono block">C2H5OH</span>
            <div class="mt-2 text-[11px] text-slate-300">Mass: 46 u (+14)</div>
            <div class="text-[11px] text-amber-400">BP: 351 K</div>
        </div>
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-emerald-300 block">Propanol</span>
            <span class="text-[10px] text-slate-400 font-mono block">C3H7OH</span>
            <div class="mt-2 text-[11px] text-slate-300">Mass: 60 u (+14)</div>
            <div class="text-[11px] text-amber-400">BP: 370 K</div>
        </div>
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-rose-300 block">Butanol</span>
            <span class="text-[10px] text-slate-400 font-mono block">C4H9OH</span>
            <div class="mt-2 text-[11px] text-slate-300">Mass: 74 u (+14)</div>
            <div class="text-[11px] text-amber-400">BP: 391 K</div>
        </div>
    </div>
    <p class="text-[11px] text-slate-400 text-center mt-2">Every step adds one -CH2- unit (14 u mass), steadily increasing boiling point while retaining identical chemical reactivity!</p>
</div>
''',

    11: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">IUPAC Systematic Nomenclature Machine</h4>
        <span class="text-xs text-sky-300 font-mono">Root + Suffix</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-3">
        <div class="flex flex-wrap items-center justify-center gap-3 text-xs">
            <div>
                <label class="block text-[10px] text-slate-400 mb-0.5">Carbon Chain:</label>
                <select id="sim11Chain" onchange="updateIUPAC()" class="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-amber-300">
                    <option value="1">1 Carbon (Meth-)</option>
                    <option value="2" selected>2 Carbons (Eth-)</option>
                    <option value="3">3 Carbons (Prop-)</option>
                    <option value="4">4 Carbons (But-)</option>
                    <option value="5">5 Carbons (Pent-)</option>
                    <option value="6">6 Carbons (Hex-)</option>
                </select>
            </div>
            <div>
                <label class="block text-[10px] text-slate-400 mb-0.5">Functional Group:</label>
                <select id="sim11Func" onchange="updateIUPAC()" class="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-emerald-300">
                    <option value="alkane" selected>Alkane (-ane)</option>
                    <option value="alkene">Alkene (-ene)</option>
                    <option value="alkyne">Alkyne (-yne)</option>
                    <option value="alcohol">Alcohol (-ol)</option>
                    <option value="aldehyde">Aldehyde (-al)</option>
                    <option value="ketone">Ketone (-one)</option>
                    <option value="acid">Carboxylic Acid (-oic acid)</option>
                    <option value="chloro">Chloro- (Haloalkane)</option>
                </select>
            </div>
        </div>

        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Generated IUPAC Name:</span>
            <div id="sim11OutputName" class="text-base font-bold text-amber-300 font-mono">Ethane</div>
            <div id="sim11FormulaText" class="text-xs text-slate-300 font-mono">CH3-CH3</div>
        </div>
    </div>
</div>
''',

    12: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Combustion: Blue Clean vs Yellow Sooty Flames</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim12Vent(true)" id="sim12BtnOpen" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Air Vent Open (Excess O2)</button>
            <button onclick="setSim12Vent(false)" id="sim12BtnClosed" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Air Vent Blocked (Limited O2)</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-4">
        <svg viewBox="0 0 160 110" class="w-36 h-26">
            <!-- Burner stem -->
            <rect x="72" y="60" width="16" height="40" fill="#475569"/>
            <rect x="60" y="95" width="40" height="10" rx="2" fill="#334155"/>
            <!-- Air vent hole -->
            <circle id="sim12VentHole" cx="80" cy="75" r="4" fill="#0f172a" stroke="#94a3b8"/>
            <!-- Flame -->
            <g id="sim12Flame">
                <polygon id="sim12OuterFlame" points="70,60 80,15 90,60" fill="#38bdf8"/>
                <polygon id="sim12InnerFlame" points="75,60 80,30 85,60" fill="#67e8f9"/>
            </g>
            <!-- Inverted pot bottom above flame -->
            <line x1="50" y1="12" x2="110" y2="12" stroke="#94a3b8" stroke-width="4"/>
            <rect id="sim12Soot" x="65" y="10" width="30" height="2" fill="#000" opacity="0"/>
        </svg>
        <div class="text-center sm:text-left space-y-1 text-xs">
            <span id="sim12FlameTitle" class="font-bold text-sky-400 block">Complete Combustion: Clean Blue Flame</span>
            <p id="sim12FlameDesc" class="text-slate-300">Adequate oxygen allows saturated gas to burn completely without forming soot.</p>
        </div>
    </div>
</div>
''',

    13: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Controlled Oxidation: Ethanol to Ethanoic Acid</h4>
        <span class="text-xs text-purple-300 font-mono">Alkaline KMnO4 Reagent</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-4">
        <svg viewBox="0 0 100 110" class="w-24 h-26">
            <!-- Test tube -->
            <rect x="30" y="15" width="40" height="85" rx="5" fill="#0f172a" stroke="#64748b"/>
            <!-- Liquid in tube -->
            <rect id="sim13Liquid" x="32" y="50" width="36" height="48" fill="#a855f7" fill-opacity="0.5" class="transition-colors duration-1000"/>
        </svg>
        <div class="space-y-2 text-center sm:text-left text-xs">
            <span class="font-bold text-purple-300 block">Warm with Alkaline KMnO4 in Water Bath</span>
            <p id="sim13Status" class="text-slate-300">Purple KMnO4 supplies oxygen to oxidise ethanol into ethanoic acid.</p>
            <button onclick="oxidiseAlcohol()" class="px-3 py-1 rounded bg-purple-600/30 hover:bg-purple-600/50 text-purple-200 border border-purple-500/40 text-xs font-bold">Heat Mixture</button>
        </div>
    </div>
</div>
''',

    14: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Addition (Hydrogenation) & Substitution (Chlorination)</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim14Mode('hydrogenation')" id="sim14BtnHyd" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Hydrogenation of Oil</button>
            <button onclick="setSim14Mode('substitution')" id="sim14BtnSub" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Chlorination of Methane</button>
        </div>
    </div>

    <!-- Hydrogenation View -->
    <div id="sim14HydView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-emerald-400 block">Catalytic Hydrogenation (Addition across C=C)</span>
        <div class="p-2 bg-slate-900 rounded font-mono text-xs text-emerald-300">
            Unsaturated Vegetable Oil (Liquid) + H2 ⎯⎯Ni catalyst⎯→ Saturated Fat (Solid Vanaspati)
        </div>
        <p class="text-[11px] text-slate-400">Nickel catalyst opens double bonds, adding hydrogen atoms to convert liquid oils into solid fats.</p>
    </div>

    <!-- Substitution View -->
    <div id="sim14SubView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-amber-300 block">Photochemical Substitution (Sunlight Activation)</span>
        <div class="p-2 bg-slate-900 rounded font-mono text-xs text-amber-300">
            CH4 + Cl2 ⎯⎯Sunlight (hν)⎯→ CH3Cl + HCl
        </div>
        <p class="text-[11px] text-slate-400">Chlorine free radicals replace hydrogen atoms on saturated methane progressively in sunlight.</p>
    </div>
</div>
''',

    15: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Reactions of Ethanol: Sodium Reaction & Acid Dehydration</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim15Reaction('sodium')" id="sim15BtnNa" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Reaction with Sodium</button>
            <button onclick="setSim15Reaction('dehydrate')" id="sim15BtnDehyd" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Dehydration to Ethene (443 K)</button>
        </div>
    </div>

    <!-- Sodium Reaction View -->
    <div id="sim15NaView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-sky-400 block">2Na + 2C2H5OH → 2C2H5ONa (Sodium Ethoxide) + H2 ↑</span>
        <svg viewBox="0 0 160 80" class="w-full h-18 mx-auto">
            <rect x="60" y="10" width="40" height="60" rx="4" fill="#0f172a" stroke="#64748b"/>
            <rect x="62" y="30" width="36" height="38" fill="#38bdf8" fill-opacity="0.2"/>
            <circle cx="80" cy="55" r="4" fill="#facc15"/>
            <!-- Hydrogen bubbles -->
            <circle cx="75" cy="40" r="2.5" fill="#e0f2fe"/>
            <circle cx="85" cy="35" r="2" fill="#e0f2fe"/>
        </svg>
        <p class="text-[11px] text-slate-300">Sodium metal reacts with ethanol to evolve hydrogen gas, verified by a burning splint's pop sound.</p>
    </div>

    <!-- Dehydration View -->
    <div id="sim15DehydView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-rose-400 block">Acid Dehydration: Ethanol ⎯Hot Conc. H2SO4 (443 K)⎯→ CH2=CH2 + H2O</span>
        <p class="text-[11px] text-slate-300">Excess hot concentrated sulphuric acid acts as a powerful dehydrating agent, stripping water to yield ethene alkene gas.</p>
    </div>
</div>
''',

    16: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Reactions of Ethanoic Acid: Esterification & Carbonate Fizz</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim16Mode('ester')" id="sim16BtnEster" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Activity 4.7 Esterification</button>
            <button onclick="setSim16Mode('fizz')" id="sim16BtnFizz" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Carbonate Fizz (CO2)</button>
        </div>
    </div>

    <!-- Esterification View -->
    <div id="sim16EsterView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-amber-300 block">Ethanoic Acid + Ethanol ⎯conc. H2SO4⎯→ Ethyl Ethanoate (Fruity Ester) + H2O</span>
        <div class="flex items-center justify-center gap-3 text-xs">
            <span class="p-1.5 bg-slate-900 rounded text-amber-300">Acetic Acid</span>
            <span>+</span>
            <span class="p-1.5 bg-slate-900 rounded text-sky-300">Ethanol</span>
            <span>=</span>
            <span class="p-1.5 bg-amber-950/80 border border-amber-500/60 rounded text-amber-200 font-bold">Sweet Fruity Aroma 🍎</span>
        </div>
        <p class="text-[11px] text-slate-400">Esters are sweet-smelling substances used in perfumes and artificial fruit flavourings.</p>
    </div>

    <!-- Carbonate Fizz View -->
    <div id="sim16FizzView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-emerald-400 block">2CH3COOH + Na2CO3 → 2CH3COONa + H2O + CO2 ↑ (Brisk Effervescence)</span>
        <p class="text-[11px] text-slate-300">Carbon dioxide gas is liberated with brisk bubbling, turning lime water milky. (Alcohols do not react!)</p>
    </div>
</div>
'''
}

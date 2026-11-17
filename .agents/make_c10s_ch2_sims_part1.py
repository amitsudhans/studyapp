"""Interactive Simulators 1 to 8 for Class 10 Science Chapter 2: Acids, Bases and Salts
"""

simulators = {
    1: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.1 & Indicator Lab: Natural Indicators</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim1Mode('litmus')" id="sim1BtnLitmus" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Litmus Tests</button>
            <button onclick="setSim1Mode('turmeric')" id="sim1BtnTurmeric" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Turmeric Stain</button>
            <button onclick="setSim1Mode('puzzle')" id="sim1BtnPuzzle" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">3-Tube Litmus Puzzle</button>
        </div>
    </div>

    <!-- Mode 1: Litmus Testing -->
    <div id="sim1LitmusView" class="space-y-3">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-rose-400 block mb-1">Acidic Solution (Dilute HCl)</span>
                <svg viewBox="0 0 200 120" class="w-full h-24 mx-auto">
                    <!-- Watch glass -->
                    <path d="M 20 80 Q 100 110 180 80" stroke="#94a3b8" stroke-width="3" fill="none"/>
                    <path d="M 30 82 Q 100 106 170 82" fill="#38bdf8" fill-opacity="0.25"/>
                    <!-- Blue Litmus Paper dipping -->
                    <rect id="sim1BluePaper" x="80" y="20" width="40" height="70" rx="3" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" class="transition-colors duration-500"/>
                    <text id="sim1BlueText" x="100" y="55" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">Blue Litmus</text>
                </svg>
                <button onclick="dipLitmus('acid')" class="mt-1 px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold">Dip Blue Litmus into Acid</button>
                <p id="sim1AcidRes" class="text-[11px] text-slate-400 mt-1">Neutral litmus is purple; acid turns blue litmus red.</p>
            </div>

            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-cyan-400 block mb-1">Basic Solution (Dilute NaOH)</span>
                <svg viewBox="0 0 200 120" class="w-full h-24 mx-auto">
                    <!-- Watch glass -->
                    <path d="M 20 80 Q 100 110 180 80" stroke="#94a3b8" stroke-width="3" fill="none"/>
                    <path d="M 30 82 Q 100 106 170 82" fill="#a855f7" fill-opacity="0.25"/>
                    <!-- Red Litmus Paper dipping -->
                    <rect id="sim1RedPaper" x="80" y="20" width="40" height="70" rx="3" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" class="transition-colors duration-500"/>
                    <text id="sim1RedText" x="100" y="55" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">Red Litmus</text>
                </svg>
                <button onclick="dipLitmus('base')" class="mt-1 px-3 py-1 rounded bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-200 border border-cyan-500/40 text-xs font-bold">Dip Red Litmus into Base</button>
                <p id="sim1BaseRes" class="text-[11px] text-slate-400 mt-1">Alkaline solutions turn red litmus blue.</p>
            </div>
        </div>
        <div class="p-2.5 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs text-slate-300 flex items-center justify-between">
            <span>Natural indicator plant extracts: <strong>Red cabbage leaves</strong> (red in acid, green in base), <strong>Hydrangea petals</strong> (blue in acid soil, pink in alkaline soil).</span>
            <button onclick="resetSim1Litmus()" class="text-[11px] text-amber-400 underline hover:text-amber-300 ml-2">Reset</button>
        </div>
    </div>

    <!-- Mode 2: Turmeric Stain -->
    <div id="sim1TurmericView" class="hidden space-y-3">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
            <svg viewBox="0 0 160 140" class="w-36 h-32 shrink-0">
                <!-- White cloth swatch -->
                <rect x="20" y="20" width="120" height="100" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <!-- Curry stain -->
                <ellipse id="sim1TurmericSpot" cx="80" cy="70" rx="35" ry="30" fill="#eab308" class="transition-colors duration-700"/>
                <text id="sim1TurmericLabel" x="80" y="73" font-size="10" fill="#713f12" font-weight="bold" text-anchor="middle">Curry Stain</text>
            </svg>
            <div class="space-y-2 flex-1 text-xs">
                <p class="text-slate-300">Turmeric contains <strong>curcumin</strong>. Watch its reversible response to alkaline soap and neutral water:</p>
                <div class="flex flex-wrap gap-2">
                    <button onclick="applyTurmeric('soap')" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Apply Alkaline Soap</button>
                    <button onclick="applyTurmeric('water')" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">Rinse with Water</button>
                    <button onclick="applyTurmeric('lemon')" class="px-3 py-1.5 rounded-lg bg-yellow-600 hover:bg-yellow-500 text-white font-bold transition">Add Acidic Lemon Juice</button>
                </div>
                <div id="sim1TurmericExplain" class="p-2 rounded bg-slate-900 border border-slate-800 text-amber-300 text-[11px]">
                    Status: Yellow turmeric stain on cloth.
                </div>
            </div>
        </div>
    </div>

    <!-- Mode 3: 3-Tube Litmus Puzzle -->
    <div id="sim1PuzzleView" class="hidden space-y-3">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="text-xs font-bold text-amber-400 block mb-2">Identification Challenge: Distilled Water, Acid, and Base with ONLY Red Litmus</span>
            <div class="grid grid-cols-3 gap-2 text-center text-xs">
                <div id="sim1Tube1" class="p-2.5 rounded-xl border border-slate-700 bg-slate-900 cursor-pointer hover:border-amber-500 transition" onclick="testPuzzleTube(1)">
                    <span class="font-bold text-slate-300 block mb-1">Tube A</span>
                    <div class="h-16 w-8 mx-auto rounded-b-xl border-2 border-slate-500 bg-slate-800/80 flex items-end justify-center pb-1">
                        <div class="w-full h-10 rounded-b-lg bg-blue-500/30"></div>
                    </div>
                    <span id="sim1Tube1Status" class="text-[10px] text-slate-400 mt-1 block">Unknown liquid</span>
                </div>
                <div id="sim1Tube2" class="p-2.5 rounded-xl border border-slate-700 bg-slate-900 cursor-pointer hover:border-amber-500 transition" onclick="testPuzzleTube(2)">
                    <span class="font-bold text-slate-300 block mb-1">Tube B</span>
                    <div class="h-16 w-8 mx-auto rounded-b-xl border-2 border-slate-500 bg-slate-800/80 flex items-end justify-center pb-1">
                        <div class="w-full h-10 rounded-b-lg bg-rose-500/30"></div>
                    </div>
                    <span id="sim1Tube2Status" class="text-[10px] text-slate-400 mt-1 block">Unknown liquid</span>
                </div>
                <div id="sim1Tube3" class="p-2.5 rounded-xl border border-slate-700 bg-slate-900 cursor-pointer hover:border-amber-500 transition" onclick="testPuzzleTube(3)">
                    <span class="font-bold text-slate-300 block mb-1">Tube C</span>
                    <div class="h-16 w-8 mx-auto rounded-b-xl border-2 border-slate-500 bg-slate-800/80 flex items-end justify-center pb-1">
                        <div class="w-full h-10 rounded-b-lg bg-teal-500/30"></div>
                    </div>
                    <span id="sim1Tube3Status" class="text-[10px] text-slate-400 mt-1 block">Unknown liquid</span>
                </div>
            </div>
            <div id="sim1PuzzleFeedback" class="mt-3 p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-xs text-slate-300">
                Click on any tube to dip your <strong>Red Litmus Paper</strong>. Look for which tube turns it blue first!
            </div>
            <button onclick="resetPuzzle()" class="mt-2 text-xs text-amber-400 underline">Reset Challenge</button>
        </div>
    </div>
</div>

<script>
function setSim1Mode(mode) {
    document.getElementById('sim1LitmusView').classList.toggle('hidden', mode !== 'litmus');
    document.getElementById('sim1TurmericView').classList.toggle('hidden', mode !== 'turmeric');
    document.getElementById('sim1PuzzleView').classList.toggle('hidden', mode !== 'puzzle');
    document.getElementById('sim1BtnLitmus').className = mode === 'litmus' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim1BtnTurmeric').className = mode === 'turmeric' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim1BtnPuzzle').className = mode === 'puzzle' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function dipLitmus(type) {
    if (type === 'acid') {
        document.getElementById('sim1BluePaper').setAttribute('fill', '#ef4444');
        document.getElementById('sim1BluePaper').setAttribute('stroke', '#b91c1c');
        document.getElementById('sim1BlueText').textContent = 'Turns Red!';
        document.getElementById('sim1AcidRes').textContent = 'Blue litmus turns RED in acid (HCl dissociates H+ ions).';
    } else {
        document.getElementById('sim1RedPaper').setAttribute('fill', '#3b82f6');
        document.getElementById('sim1RedPaper').setAttribute('stroke', '#1d4ed8');
        document.getElementById('sim1RedText').textContent = 'Turns Blue!';
        document.getElementById('sim1BaseRes').textContent = 'Red litmus turns BLUE in base (NaOH provides OH- ions).';
    }
}

function resetSim1Litmus() {
    document.getElementById('sim1BluePaper').setAttribute('fill', '#3b82f6');
    document.getElementById('sim1BluePaper').setAttribute('stroke', '#1d4ed8');
    document.getElementById('sim1BlueText').textContent = 'Blue Litmus';
    document.getElementById('sim1RedPaper').setAttribute('fill', '#ef4444');
    document.getElementById('sim1RedPaper').setAttribute('stroke', '#b91c1c');
    document.getElementById('sim1RedText').textContent = 'Red Litmus';
    document.getElementById('sim1AcidRes').textContent = 'Neutral litmus is purple; acid turns blue litmus red.';
    document.getElementById('sim1BaseRes').textContent = 'Alkaline solutions turn red litmus blue.';
}

function applyTurmeric(substance) {
    const spot = document.getElementById('sim1TurmericSpot');
    const label = document.getElementById('sim1TurmericLabel');
    const explain = document.getElementById('sim1TurmericExplain');
    if (substance === 'soap') {
        spot.setAttribute('fill', '#991b1b');
        label.textContent = 'Reddish-Brown';
        label.setAttribute('fill', '#fecaca');
        explain.innerHTML = '<strong>Alkaline Soap Applied:</strong> Curcumin reacts with alkaline sodium salts in soap, turning deep reddish-brown!';
    } else if (substance === 'water') {
        spot.setAttribute('fill', '#eab308');
        label.textContent = 'Yellow Restored';
        label.setAttribute('fill', '#713f12');
        explain.innerHTML = '<strong>Rinsed with Plenty of Water:</strong> Alkaline soap is diluted away; original bright yellow turmeric colour is restored!';
    } else {
        spot.setAttribute('fill', '#facc15');
        label.textContent = 'Bright Yellow';
        label.setAttribute('fill', '#854d0e');
        explain.innerHTML = '<strong>Acidic Lemon Juice Added:</strong> Acid stabilizes yellow neutral curcumin form.';
    }
}

let puzzleLitmusColor = 'red';
let identified = { base: false, acid: false, water: false };
// Random layout for puzzle: Tube 1 = Base, Tube 2 = Acid, Tube 3 = Distilled Water
function testPuzzleTube(tubeNum) {
    const fb = document.getElementById('sim1PuzzleFeedback');
    if (tubeNum === 1) { // Base
        puzzleLitmusColor = 'blue';
        identified.base = true;
        document.getElementById('sim1Tube1Status').innerHTML = '<span class="text-cyan-400 font-bold">Base (NaOH)</span>';
        fb.innerHTML = '<strong>Tube A turned Red Litmus BLUE!</strong> You have identified the <strong>Base</strong>. Now you hold <strong>Blue Litmus Paper</strong>! Use it on Tubes B and C.';
    } else if (tubeNum === 2) { // Acid
        if (puzzleLitmusColor === 'blue') {
            puzzleLitmusColor = 'red';
            identified.acid = true;
            document.getElementById('sim1Tube2Status').innerHTML = '<span class="text-rose-400 font-bold">Acid (HCl)</span>';
            fb.innerHTML = '<strong>Tube B turned Blue Litmus RED!</strong> You have identified the <strong>Acid</strong>. Only one tube remains!';
        } else {
            fb.innerHTML = 'Tube B had no effect on red litmus paper (acids do not change red litmus). Find the base first to turn your litmus blue!';
        }
    } else if (tubeNum === 3) { // Water
        if (puzzleLitmusColor === 'blue') {
            document.getElementById('sim1Tube3Status').innerHTML = '<span class="text-teal-400 font-bold">Distilled Water</span>';
            identified.water = true;
            fb.innerHTML = '<strong>Tube C left Blue Litmus BLUE!</strong> Distilled water is neutral and causes no colour change. All 3 tubes successfully identified!';
        } else {
            fb.innerHTML = 'Tube C left red litmus red (neutral liquid). Try dipping into Tube A to find the base first!';
        }
    }
}

function resetPuzzle() {
    puzzleLitmusColor = 'red';
    identified = { base: false, acid: false, water: false };
    document.getElementById('sim1Tube1Status').textContent = 'Unknown liquid';
    document.getElementById('sim1Tube2Status').textContent = 'Unknown liquid';
    document.getElementById('sim1Tube3Status').textContent = 'Unknown liquid';
    document.getElementById('sim1PuzzleFeedback').textContent = 'Click on any tube to dip your Red Litmus Paper. Look for which tube turns it blue first!';
}
</script>
''',

    2: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.1 & 2.2: Laboratory Indicators & Olfactory Testing</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim2Tab('chemical')" id="sim2TabChem" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Synthetic Spot Plate</button>
            <button onclick="setSim2Tab('olfactory')" id="sim2TabOlf" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Olfactory Indicators</button>
        </div>
    </div>

    <!-- Chemical Indicators Spot Plate -->
    <div id="sim2ChemView" class="space-y-3">
        <div class="flex flex-wrap gap-2 items-center text-xs">
            <span class="text-slate-400">Select Test Solution:</span>
            <button onclick="testSim2Solution('HCl')" id="sim2BtnHCl" class="px-2.5 py-1 rounded bg-rose-600/30 text-rose-300 border border-rose-500/40 font-bold">HCl (Acid)</button>
            <button onclick="testSim2Solution('H2SO4')" id="sim2BtnH2SO4" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold">H2SO4 (Acid)</button>
            <button onclick="testSim2Solution('NaOH')" id="sim2BtnNaOH" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold">NaOH (Base)</button>
            <button onclick="testSim2Solution('CaOH2')" id="sim2BtnCaOH2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold">Ca(OH)2 (Base)</button>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
            <!-- Well 1: Red Litmus -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-[11px] text-slate-400 block mb-1">Red Litmus</span>
                <div id="sim2WellRedLitmus" class="w-12 h-12 mx-auto rounded-full bg-rose-500 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white">Red</div>
                <span id="sim2LabelRed" class="text-[10px] text-slate-300 mt-1 block">No Change</span>
            </div>
            <!-- Well 2: Blue Litmus -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-[11px] text-slate-400 block mb-1">Blue Litmus</span>
                <div id="sim2WellBlueLitmus" class="w-12 h-12 mx-auto rounded-full bg-rose-500 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white">Red</div>
                <span id="sim2LabelBlue" class="text-[10px] text-rose-400 mt-1 block">Turns Red</span>
            </div>
            <!-- Well 3: Phenolphthalein -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-[11px] text-slate-400 block mb-1">Phenolphthalein</span>
                <div id="sim2WellPhenol" class="w-12 h-12 mx-auto rounded-full bg-slate-800/80 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-slate-300">Clear</div>
                <span id="sim2LabelPhenol" class="text-[10px] text-slate-300 mt-1 block">Colourless</span>
            </div>
            <!-- Well 4: Methyl Orange -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-[11px] text-slate-400 block mb-1">Methyl Orange</span>
                <div id="sim2WellMethyl" class="w-12 h-12 mx-auto rounded-full bg-red-600 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white">Red</div>
                <span id="sim2LabelMethyl" class="text-[10px] text-red-400 mt-1 block">Turns Red</span>
            </div>
        </div>

        <div id="sim2Summary" class="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-slate-300">
            <strong>HCl (Hydrochloric Acid):</strong> Turns blue litmus red, leaves red litmus unchanged, remains colourless with phenolphthalein, and turns methyl orange bright red.
        </div>
    </div>

    <!-- Olfactory Testing -->
    <div id="sim2OlfView" class="hidden space-y-3">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="text-xs font-bold text-amber-400 block mb-2">Olfactory Indicators: Scent Retention vs Destruction</span>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center text-xs">
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="font-bold text-slate-300 block mb-1">Onion Strip</span>
                    <div id="sim2OnionIcon" class="text-3xl my-1">🧅</div>
                    <span id="sim2OnionStatus" class="text-[11px] text-emerald-400">Pungent Aroma Retained</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="font-bold text-slate-300 block mb-1">Vanilla Essence</span>
                    <div id="sim2VanillaIcon" class="text-3xl my-1">🍦</div>
                    <span id="sim2VanillaStatus" class="text-[11px] text-emerald-400">Sweet Aroma Retained</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="font-bold text-slate-300 block mb-1">Clove Oil</span>
                    <div id="sim2CloveIcon" class="text-3xl my-1">🌿</div>
                    <span id="sim2CloveStatus" class="text-[11px] text-emerald-400">Spicy Aroma Retained</span>
                </div>
            </div>

            <div class="mt-3 flex gap-2">
                <button onclick="setOlfactoryMedium('acid')" id="sim2BtnOlfAcid" class="flex-1 py-1.5 rounded-lg bg-rose-600/30 text-rose-300 border border-rose-500/40 text-xs font-bold">Treat with Dilute HCl (Acid)</button>
                <button onclick="setOlfactoryMedium('base')" id="sim2BtnOlfBase" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold">Treat with Dilute NaOH (Base)</button>
            </div>
            <p id="sim2OlfExplain" class="mt-2 text-xs text-slate-300">
                In <strong>acidic medium (HCl)</strong>, aromatic volatile compounds remain chemically intact; distinct odours of onion, vanilla, and clove are fully preserved.
            </p>
        </div>
    </div>
</div>

<script>
function setSim2Tab(tab) {
    document.getElementById('sim2ChemView').classList.toggle('hidden', tab !== 'chemical');
    document.getElementById('sim2OlfView').classList.toggle('hidden', tab !== 'olfactory');
    document.getElementById('sim2TabChem').className = tab === 'chemical' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim2TabOlf').className = tab === 'olfactory' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
}

function testSim2Solution(sol) {
    const isAcid = (sol === 'HCl' || sol === 'H2SO4');
    ['HCl', 'H2SO4', 'NaOH', 'CaOH2'].forEach(s => {
        document.getElementById('sim2Btn' + s).className = (s === sol) ? 'px-2.5 py-1 rounded bg-amber-500/30 text-amber-300 border border-amber-500/50 font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold';
    });

    const wRed = document.getElementById('sim2WellRedLitmus');
    const wBlue = document.getElementById('sim2WellBlueLitmus');
    const wPhenol = document.getElementById('sim2WellPhenol');
    const wMethyl = document.getElementById('sim2WellMethyl');
    const lRed = document.getElementById('sim2LabelRed');
    const lBlue = document.getElementById('sim2LabelBlue');
    const lPhenol = document.getElementById('sim2LabelPhenol');
    const lMethyl = document.getElementById('sim2LabelMethyl');
    const sum = document.getElementById('sim2Summary');

    if (isAcid) {
        wRed.className = 'w-12 h-12 mx-auto rounded-full bg-rose-500 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white';
        wRed.textContent = 'Red';
        lRed.textContent = 'No Change';
        lRed.className = 'text-[10px] text-slate-300 mt-1 block';

        wBlue.className = 'w-12 h-12 mx-auto rounded-full bg-rose-500 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white';
        wBlue.textContent = 'Red';
        lBlue.textContent = 'Turns Red';
        lBlue.className = 'text-[10px] text-rose-400 mt-1 block';

        wPhenol.className = 'w-12 h-12 mx-auto rounded-full bg-slate-800/80 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-slate-300';
        wPhenol.textContent = 'Clear';
        lPhenol.textContent = 'Colourless';
        lPhenol.className = 'text-[10px] text-slate-300 mt-1 block';

        wMethyl.className = 'w-12 h-12 mx-auto rounded-full bg-red-600 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white';
        wMethyl.textContent = 'Red';
        lMethyl.textContent = 'Turns Red';
        lMethyl.className = 'text-[10px] text-red-400 mt-1 block';

        sum.innerHTML = '<strong>' + sol + ' (Acid):</strong> Blue litmus turns Red, Red litmus unchanged, Phenolphthalein remains Colourless, Methyl orange turns Red.';
    } else {
        wRed.className = 'w-12 h-12 mx-auto rounded-full bg-blue-600 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white';
        wRed.textContent = 'Blue';
        lRed.textContent = 'Turns Blue';
        lRed.className = 'text-[10px] text-blue-400 mt-1 block';

        wBlue.className = 'w-12 h-12 mx-auto rounded-full bg-blue-600 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white';
        wBlue.textContent = 'Blue';
        lBlue.textContent = 'No Change';
        lBlue.className = 'text-[10px] text-slate-300 mt-1 block';

        wPhenol.className = 'w-12 h-12 mx-auto rounded-full bg-pink-500 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-white';
        wPhenol.textContent = 'Pink';
        lPhenol.textContent = 'Intense Pink';
        lPhenol.className = 'text-[10px] text-pink-400 mt-1 block';

        wMethyl.className = 'w-12 h-12 mx-auto rounded-full bg-yellow-400 border-2 border-slate-600 transition-colors duration-500 flex items-center justify-center text-[10px] font-bold text-slate-900';
        wMethyl.textContent = 'Yellow';
        lMethyl.textContent = 'Turns Yellow';
        lMethyl.className = 'text-[10px] text-yellow-400 mt-1 block';

        sum.innerHTML = '<strong>' + sol + ' (Base/Alkali):</strong> Red litmus turns Blue, Blue litmus unchanged, Phenolphthalein turns Pink, Methyl orange turns Yellow.';
    }
}

function setOlfactoryMedium(med) {
    const isAcid = (med === 'acid');
    document.getElementById('sim2BtnOlfAcid').className = isAcid ? 'flex-1 py-1.5 rounded-lg bg-rose-600/30 text-rose-300 border border-rose-500/40 text-xs font-bold' : 'flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold';
    document.getElementById('sim2BtnOlfBase').className = !isAcid ? 'flex-1 py-1.5 rounded-lg bg-cyan-600/30 text-cyan-300 border border-cyan-500/40 text-xs font-bold' : 'flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold';

    if (isAcid) {
        document.getElementById('sim2OnionStatus').innerHTML = '<span class="text-emerald-400">Pungent Aroma Retained</span>';
        document.getElementById('sim2VanillaStatus').innerHTML = '<span class="text-emerald-400">Sweet Aroma Retained</span>';
        document.getElementById('sim2CloveStatus').innerHTML = '<span class="text-emerald-400">Spicy Aroma Retained</span>';
        document.getElementById('sim2OlfExplain').innerHTML = 'In <strong>acidic medium (dilute HCl)</strong>: The characteristic aromas of onion, vanilla, and clove persist strongly without chemical alteration.';
    } else {
        document.getElementById('sim2OnionStatus').innerHTML = '<span class="text-rose-400 font-bold">Odour Completely Destroyed</span>';
        document.getElementById('sim2VanillaStatus').innerHTML = '<span class="text-rose-400 font-bold">Odour Completely Destroyed</span>';
        document.getElementById('sim2CloveStatus').innerHTML = '<span class="text-rose-400 font-bold">Odour Completely Destroyed</span>';
        document.getElementById('sim2OlfExplain').innerHTML = 'In <strong>basic medium (dilute NaOH)</strong>: Hydroxide ions deprotonate and hydrolyse the aromatic aldehydes and phenols, entirely destroying their distinct scents!';
    }
}
</script>
''',

    3: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.3 & 2.4: Reaction of Metals with Acids & Alkalis</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim3Mode('acid')" id="sim3BtnAcid" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Zinc + Dilute H2SO4</button>
            <button onclick="setSim3Mode('base')" id="sim3BtnBase" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Zinc + Warm NaOH</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <svg viewBox="0 0 400 180" class="w-full h-44 mx-auto">
            <!-- Stand & Boiling tube -->
            <rect x="70" y="30" width="30" height="90" rx="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <!-- Zinc granules -->
            <circle cx="80" cy="110" r="4" fill="#94a3b8"/>
            <circle cx="90" cy="112" r="5" fill="#64748b"/>
            <circle cx="85" cy="105" r="4" fill="#94a3b8"/>
            <!-- Acid liquid -->
            <rect id="sim3AcidLiquid" x="72" y="70" width="26" height="48" rx="12" fill="#38bdf8" fill-opacity="0.35"/>
            <!-- Gas Bubbles in tube -->
            <g id="sim3Bubbles" class="opacity-0 transition-opacity duration-300">
                <circle cx="85" cy="95" r="2.5" fill="#ffffff" opacity="0.8"/>
                <circle cx="80" cy="85" r="2" fill="#ffffff" opacity="0.8"/>
                <circle cx="90" cy="78" r="2.5" fill="#ffffff" opacity="0.8"/>
                <circle cx="85" cy="65" r="3" fill="#ffffff" opacity="0.8"/>
            </g>
            <!-- Delivery Tube -->
            <path d="M 85 30 L 85 15 L 240 15 L 240 120" stroke="#94a3b8" stroke-width="3" fill="none"/>
            <!-- Soap solution trough -->
            <rect x="210" y="115" width="70" height="40" rx="4" fill="#0f172a" stroke="#475569" stroke-width="2"/>
            <rect x="212" y="125" width="66" height="28" fill="#14b8a6" fill-opacity="0.3"/>
            <!-- Floating Soap Bubbles -->
            <g id="sim3SoapBubbles" class="opacity-0 transition-opacity duration-300">
                <circle cx="250" cy="100" r="8" fill="#a7f3d0" fill-opacity="0.4" stroke="#34d399" stroke-width="1.5"/>
                <circle cx="265" cy="80" r="10" fill="#a7f3d0" fill-opacity="0.4" stroke="#34d399" stroke-width="1.5"/>
                <circle cx="280" cy="60" r="11" fill="#a7f3d0" fill-opacity="0.4" stroke="#34d399" stroke-width="1.5"/>
            </g>
            <!-- Burning candle / splint -->
            <g id="sim3Candle" transform="translate(300, 30)" class="cursor-pointer" onclick="testPopSound()">
                <rect x="15" y="40" width="10" height="50" rx="2" fill="#fde047"/>
                <line x1="20" y1="40" x2="20" y2="35" stroke="#475569" stroke-width="2"/>
                <!-- Flame -->
                <path d="M 20 20 Q 26 28 20 35 Q 14 28 20 20" fill="#f97316"/>
                <path d="M 20 24 Q 23 29 20 34 Q 17 29 20 24" fill="#fef08a"/>
                <text x="20" y="105" font-size="8" fill="#cbd5e1" text-anchor="middle">Click Candle to Pop!</text>
            </g>
            <!-- Pop shockwave -->
            <g id="sim3PopEffect" class="hidden">
                <circle cx="280" cy="60" r="22" fill="#fbbf24" fill-opacity="0.4" stroke="#f59e0b" stroke-width="3"/>
                <text x="280" y="65" font-size="14" font-weight="extrabold" fill="#ef4444" text-anchor="middle">POP!</text>
            </g>
        </svg>

        <div class="mt-2 flex flex-wrap gap-2 justify-between items-center text-xs">
            <div class="flex gap-2">
                <button onclick="startSim3Reaction()" id="sim3StartBtn" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">Add Acid & Evolve Gas</button>
                <button onclick="testPopSound()" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Bring Flame (Pop Test)</button>
            </div>
            <span id="sim3Formula" class="font-mono text-cyan-300 font-bold">Zn + H2SO4 → ZnSO4 + H2↑</span>
        </div>
        <p id="sim3Status" class="mt-2 text-xs text-slate-300">
            Click <strong>Add Acid</strong> to start effervescence of hydrogen gas, then bring the candle near floating bubbles.
        </p>
    </div>
</div>

<script>
let sim3Mode = 'acid';
let sim3GasEvolved = false;

function setSim3Mode(mode) {
    sim3Mode = mode;
    document.getElementById('sim3BtnAcid').className = mode === 'acid' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim3BtnBase').className = mode === 'base' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    
    if (mode === 'acid') {
        document.getElementById('sim3Formula').textContent = 'Zn + H2SO4 → ZnSO4 + H2↑';
        document.getElementById('sim3AcidLiquid').setAttribute('fill', '#38bdf8');
        document.getElementById('sim3Status').textContent = 'Acid + Metal reaction mode selected. Click Add Acid to evolve hydrogen gas.';
    } else {
        document.getElementById('sim3Formula').textContent = 'Zn + 2NaOH (warm) → Na2ZnO2 + H2↑';
        document.getElementById('sim3AcidLiquid').setAttribute('fill', '#a855f7');
        document.getElementById('sim3Status').textContent = 'Warming zinc with NaOH forms sodium zincate (Na2ZnO2) and releases hydrogen gas.';
    }
    resetSim3();
}

function startSim3Reaction() {
    document.getElementById('sim3Bubbles').classList.remove('opacity-0');
    document.getElementById('sim3SoapBubbles').classList.remove('opacity-0');
    sim3GasEvolved = true;
    document.getElementById('sim3Status').innerHTML = '<span class="text-emerald-400 font-bold">Vigorous Effervescence!</span> Hydrogen gas passes through delivery tube into soap solution, creating floating hydrogen-filled bubbles.';
}

function testPopSound() {
    if (!sim3GasEvolved) {
        document.getElementById('sim3Status').innerHTML = '<span class="text-amber-400">Start the reaction first to evolve hydrogen gas!</span>';
        return;
    }
    const pop = document.getElementById('sim3PopEffect');
    pop.classList.remove('hidden');
    document.getElementById('sim3SoapBubbles').classList.add('opacity-0');
    document.getElementById('sim3Status').innerHTML = '<span class="text-rose-400 font-extrabold">POP! Sound Produced!</span> Hydrogen ignites with atmospheric oxygen (2H2 + O2 → 2H2O), confirming hydrogen gas definitively!';
    setTimeout(() => { pop.classList.add('hidden'); }, 1200);
}

function resetSim3() {
    sim3GasEvolved = false;
    document.getElementById('sim3Bubbles').classList.add('opacity-0');
    document.getElementById('sim3SoapBubbles').classList.add('opacity-0');
    document.getElementById('sim3PopEffect').classList.add('hidden');
}
</script>
''',

    4: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.5: Metal Carbonates & Lime Water Milkiness</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim4Salt('Na2CO3')" id="sim4BtnNa2CO3" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Sodium Carbonate</button>
            <button onclick="setSim4Salt('NaHCO3')" id="sim4BtnNaHCO3" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Sodium Hydrogencarbonate</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <svg viewBox="0 0 380 160" class="w-full h-40 mx-auto">
            <!-- Tube A: Reaction Flask -->
            <rect x="50" y="30" width="35" height="95" rx="17" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <!-- Carbonate Salt solid -->
            <rect x="54" y="105" width="27" height="15" rx="3" fill="#f8fafc"/>
            <text x="67" y="116" font-size="7" fill="#0f172a" font-weight="bold" text-anchor="middle">Salt</text>
            <!-- Liquid acid in tube A -->
            <rect id="sim4AcidA" x="52" y="75" width="31" height="45" rx="14" fill="#38bdf8" fill-opacity="0.35"/>
            <!-- CO2 gas bubbles in tube A -->
            <g id="sim4BubblesA" class="opacity-0 transition-opacity duration-300">
                <circle cx="65" cy="95" r="2" fill="#ffffff"/>
                <circle cx="70" cy="85" r="2.5" fill="#ffffff"/>
                <circle cx="62" cy="70" r="3" fill="#ffffff"/>
            </g>
            <!-- Delivery Tube from Tube A to Tube B -->
            <path d="M 67 30 L 67 15 L 250 15 L 250 100" stroke="#94a3b8" stroke-width="3" fill="none"/>
            <!-- Tube B: Lime water -->
            <rect x="235" y="45" width="30" height="85" rx="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <!-- Lime water liquid -->
            <rect id="sim4LimeWater" x="237" y="70" width="26" height="56" rx="12" fill="#38bdf8" fill-opacity="0.2" class="transition-colors duration-700"/>
            <text id="sim4LimeText" x="250" y="105" font-size="8" fill="#e2e8f0" font-weight="bold" text-anchor="middle">Clear</text>

            <!-- Labels -->
            <text x="67" y="142" font-size="9" fill="#94a3b8" text-anchor="middle">Tube A (Acid + Salt)</text>
            <text x="250" y="145" font-size="9" fill="#94a3b8" text-anchor="middle">Tube B (Lime Water)</text>
        </svg>

        <div class="mt-2 flex flex-wrap gap-2 justify-between items-center text-xs">
            <div class="flex gap-2">
                <button onclick="addSim4Acid()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">1. Add HCl</button>
                <button onclick="bubbleCO2()" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">2. Pass CO2 into Lime Water</button>
                <button onclick="excessCO2()" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">3. Pass Excess CO2</button>
            </div>
            <button onclick="resetSim4()" class="text-xs text-amber-400 underline">Reset</button>
        </div>
        <div id="sim4Explain" class="mt-2 p-2 rounded bg-slate-900 border border-slate-800 text-xs text-slate-300">
            Click <strong>1. Add HCl</strong> to decompose the carbonate salt and generate carbon dioxide gas with brisk effervescence.
        </div>
    </div>
</div>

<script>
let sim4Salt = 'Na2CO3';

function setSim4Salt(salt) {
    sim4Salt = salt;
    document.getElementById('sim4BtnNa2CO3').className = salt === 'Na2CO3' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    document.getElementById('sim4BtnNaHCO3').className = salt === 'NaHCO3' ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
    resetSim4();
}

function addSim4Acid() {
    document.getElementById('sim4BubblesA').classList.remove('opacity-0');
    const eq = (sim4Salt === 'Na2CO3') ? 'Na2CO3 + 2HCl → 2NaCl + H2O + CO2↑' : 'NaHCO3 + HCl → NaCl + H2O + CO2↑';
    document.getElementById('sim4Explain').innerHTML = '<strong>Brisk Effervescence in Tube A:</strong> ' + eq + '. Carbon dioxide gas is traveling through the delivery tube toward Tube B.';
}

function bubbleCO2() {
    const lime = document.getElementById('sim4LimeWater');
    const txt = document.getElementById('sim4LimeText');
    lime.setAttribute('fill', '#ffffff');
    lime.setAttribute('fill-opacity', '0.85');
    txt.textContent = 'Milky';
    txt.setAttribute('fill', '#0f172a');
    document.getElementById('sim4Explain').innerHTML = '<strong>Lime Water Turns Milky White:</strong> Ca(OH)2 + CO2 → <strong>CaCO3↓ (insoluble white precipitate)</strong> + H2O. Diagnostic confirmation of carbon dioxide!';
}

function excessCO2() {
    const lime = document.getElementById('sim4LimeWater');
    const txt = document.getElementById('sim4LimeText');
    lime.setAttribute('fill', '#38bdf8');
    lime.setAttribute('fill-opacity', '0.2');
    txt.textContent = 'Clear';
    txt.setAttribute('fill', '#e2e8f0');
    document.getElementById('sim4Explain').innerHTML = '<strong>Milky Precipitate Dissolves Completely:</strong> CaCO3 + H2O + CO2 → <strong>Ca(HCO3)2 (aq) (water-soluble calcium hydrogencarbonate)</strong>. The solution turns fully clear again!';
}

function resetSim4() {
    document.getElementById('sim4BubblesA').classList.add('opacity-0');
    const lime = document.getElementById('sim4LimeWater');
    lime.setAttribute('fill', '#38bdf8');
    lime.setAttribute('fill-opacity', '0.2');
    document.getElementById('sim4LimeText').textContent = 'Clear';
    document.getElementById('sim4LimeText').setAttribute('fill', '#e2e8f0');
    document.getElementById('sim4Explain').textContent = 'Click 1. Add HCl to decompose the carbonate salt and generate carbon dioxide gas.';
}
</script>
''',

    5: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.6: Acid-Base Neutralisation Titration</h4>
        <span class="text-xs text-slate-400">NaOH + HCl → NaCl + H2O</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <svg viewBox="0 0 200 180" class="w-full h-44 mx-auto">
                <!-- Burette above -->
                <rect x="94" y="10" width="12" height="70" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
                <line x1="94" y1="30" x2="106" y2="30" stroke="#cbd5e1" stroke-width="1"/>
                <line x1="94" y1="50" x2="106" y2="50" stroke="#cbd5e1" stroke-width="1"/>
                <polygon points="98,80 102,80 100,88" fill="#64748b"/>
                <text x="115" y="45" font-size="8" fill="#94a3b8">Dil. HCl Burette</text>

                <!-- Conical Flask below -->
                <path d="M 85 105 L 94 105 L 70 160 L 130 160 L 106 105 L 115 105" stroke="#94a3b8" stroke-width="2" fill="none"/>
                <!-- Titration Solution -->
                <path id="sim5Solution" d="M 75 158 L 125 158 L 116 130 L 84 130 Z" fill="#ec4899" fill-opacity="0.8" class="transition-colors duration-500"/>
                <text id="sim5SolText" x="100" y="148" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">Pink (Basic)</text>
            </svg>

            <div class="space-y-2.5 text-xs">
                <div class="flex justify-between items-center p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400">Burette HCl Added:</span>
                    <span id="sim5HclCount" class="font-mono text-cyan-400 font-bold">0.0 mL</span>
                </div>
                <div class="flex justify-between items-center p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400">Solution pH Status:</span>
                    <span id="sim5PhBadge" class="px-2 py-0.5 rounded bg-pink-500/20 text-pink-300 font-bold border border-pink-500/40">Alkaline (pH ~12)</span>
                </div>

                <div class="flex flex-wrap gap-2 pt-1">
                    <button onclick="addSim5AcidDrop()" class="flex-1 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition">Add 1 mL HCl</button>
                    <button onclick="addSim5BaseDrop()" class="flex-1 py-1.5 rounded-lg bg-pink-600 hover:bg-pink-500 text-white font-bold transition">Add 1 mL NaOH</button>
                    <button onclick="resetSim5()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold">Reset</button>
                </div>

                <p id="sim5Details" class="text-[11px] text-slate-300 leading-relaxed">
                    Flask contains 2 mL dilute NaOH + 2 drops phenolphthalein (intense pink). Add acid drop by drop to observe the sharp neutralisation endpoint!
                </p>
            </div>
        </div>
    </div>
</div>

<script>
let sim5Volume = 0; // mL HCl added. Equivalence point at 10 mL.

function addSim5AcidDrop() {
    sim5Volume += 2;
    updateSim5State();
}

function addSim5BaseDrop() {
    if (sim5Volume >= 2) sim5Volume -= 2;
    updateSim5State();
}

function updateSim5State() {
    document.getElementById('sim5HclCount').textContent = sim5Volume.toFixed(1) + ' mL';
    const sol = document.getElementById('sim5Solution');
    const txt = document.getElementById('sim5SolText');
    const badge = document.getElementById('sim5PhBadge');
    const det = document.getElementById('sim5Details');

    if (sim5Volume < 10) {
        sol.setAttribute('fill', '#ec4899');
        sol.setAttribute('fill-opacity', '0.8');
        txt.textContent = 'Pink (Basic)';
        txt.setAttribute('fill', '#ffffff');
        badge.textContent = 'Alkaline (pH ~' + (12 - sim5Volume * 0.4).toFixed(1) + ')';
        badge.className = 'px-2 py-0.5 rounded bg-pink-500/20 text-pink-300 font-bold border border-pink-500/40';
        det.textContent = 'Base remains dominant in flask. Phenolphthalein retains bright pink colour in alkaline medium.';
    } else if (sim5Volume === 10) {
        sol.setAttribute('fill', '#38bdf8');
        sol.setAttribute('fill-opacity', '0.2');
        txt.textContent = 'Clear (Neutral)';
        txt.setAttribute('fill', '#e2e8f0');
        badge.textContent = 'Neutral (pH 7.0)';
        badge.className = 'px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/40';
        det.innerHTML = '<span class="text-emerald-400 font-bold">NEUTRALISATION EQUIVALENCE POINT REACHED!</span> Pink colour vanishes completely as all OH- ions are consumed by H+ ions: H+ + OH- → H2O.';
    } else {
        sol.setAttribute('fill', '#ef4444');
        sol.setAttribute('fill-opacity', '0.15');
        txt.textContent = 'Colourless (Acidic)';
        txt.setAttribute('fill', '#fca5a5');
        badge.textContent = 'Acidic (pH ~' + Math.max(1, 7 - (sim5Volume - 10) * 0.8).toFixed(1) + ')';
        badge.className = 'px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold border border-rose-500/40';
        det.textContent = 'Excess hydrochloric acid added. Solution is acidic; phenolphthalein remains completely colourless.';
    }
}

function resetSim5() {
    sim5Volume = 0;
    updateSim5State();
}
</script>
''',

    6: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.7: Reaction of Metallic Oxides with Acids</h4>
        <span class="text-xs text-slate-400">CuO (Black) + 2HCl → CuCl2 (Blue-Green) + H2O</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <svg viewBox="0 0 200 160" class="w-full h-40 mx-auto">
                <!-- Beaker -->
                <rect x="40" y="30" width="120" height="110" rx="6" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
                <line x1="36" y1="30" x2="164" y2="30" stroke="#94a3b8" stroke-width="2"/>
                <!-- Liquid in beaker -->
                <rect id="sim6Liquid" x="42" y="70" width="116" height="68" rx="4" fill="#0f172a" fill-opacity="0.8" class="transition-colors duration-1000"/>
                <!-- Black CuO powder particles at bottom -->
                <g id="sim6CuOParticles" class="transition-opacity duration-1000">
                    <circle cx="70" cy="130" r="5" fill="#020617"/>
                    <circle cx="85" cy="132" r="6" fill="#020617"/>
                    <circle cx="100" cy="129" r="5" fill="#020617"/>
                    <circle cx="115" cy="131" r="5.5" fill="#020617"/>
                    <circle cx="130" cy="130" r="4" fill="#020617"/>
                    <text x="100" y="125" font-size="8" fill="#cbd5e1" font-weight="bold" text-anchor="middle">Black CuO Powder</text>
                </g>
                <!-- Stirring rod -->
                <line x1="90" y1="15" x2="110" y2="120" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round"/>
                <text id="sim6LiquidLabel" x="100" y="95" font-size="9" fill="#94a3b8" font-weight="bold" text-anchor="middle">Dry Solid</text>
            </svg>

            <div class="space-y-2.5 text-xs">
                <p class="text-slate-300">
                    Observe how insoluble <strong>black copper(II) oxide</strong> reacts with hydrochloric acid to synthesize dissolved copper(II) chloride:
                </p>
                <div class="flex flex-wrap gap-2">
                    <button onclick="addSim6Acid()" class="flex-1 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition">1. Add Dilute HCl</button>
                    <button onclick="stirSim6Mixture()" class="flex-1 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">2. Stir Continuously</button>
                    <button onclick="resetSim6()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold">Reset</button>
                </div>
                <div id="sim6Status" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
                    Beaker contains black copper oxide powder (CuO). Click <strong>1. Add Dilute HCl</strong>.
                </div>
                <div class="p-2 rounded bg-amber-500/10 border border-amber-500/30 text-[11px] text-amber-300">
                    <strong>Rule:</strong> Metal Oxide + Acid → Salt + Water. Since metal oxides neutralise acids to produce salt and water, metallic oxides are <strong>basic oxides</strong>.
                </div>
            </div>
        </div>
    </div>
</div>

<script>
let sim6AcidAdded = false;

function addSim6Acid() {
    sim6AcidAdded = true;
    document.getElementById('sim6Liquid').setAttribute('fill', '#38bdf8');
    document.getElementById('sim6Liquid').setAttribute('fill-opacity', '0.25');
    document.getElementById('sim6LiquidLabel').textContent = 'Acid Added (HCl)';
    document.getElementById('sim6LiquidLabel').setAttribute('fill', '#e0f2fe');
    document.getElementById('sim6Status').innerHTML = 'Dilute HCl added. The black CuO powder sits at the bottom. Click <strong>2. Stir Continuously</strong> to facilitate reaction.';
}

function stirSim6Mixture() {
    if (!sim6AcidAdded) {
        document.getElementById('sim6Status').innerHTML = '<span class="text-amber-400">Add dilute HCl first before stirring!</span>';
        return;
    }
    document.getElementById('sim6CuOParticles').classList.add('opacity-0');
    const liq = document.getElementById('sim6Liquid');
    liq.setAttribute('fill', '#06b6d4');
    liq.setAttribute('fill-opacity', '0.65');
    document.getElementById('sim6LiquidLabel').textContent = 'Clear Blue-Green (CuCl2)';
    document.getElementById('sim6LiquidLabel').setAttribute('fill', '#ffffff');
    document.getElementById('sim6Status').innerHTML = '<span class="text-emerald-400 font-bold">Black Solid Dissolved!</span> CuO + 2HCl → CuCl2 (aq) + H2O. Soluble hydrated Cu2+ ions impart a characteristic <strong>blue-green colour</strong>.';
}

function resetSim6() {
    sim6AcidAdded = false;
    document.getElementById('sim6Liquid').setAttribute('fill', '#0f172a');
    document.getElementById('sim6Liquid').setAttribute('fill-opacity', '0.8');
    document.getElementById('sim6CuOParticles').classList.remove('opacity-0');
    document.getElementById('sim6LiquidLabel').textContent = 'Dry Solid';
    document.getElementById('sim6LiquidLabel').setAttribute('fill', '#94a3b8');
    document.getElementById('sim6Status').textContent = 'Beaker contains black copper oxide powder (CuO). Click 1. Add Dilute HCl.';
}
</script>
''',

    7: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.8: Electrical Conduction in Acids vs Non-Electrolytes</h4>
        <span class="text-xs text-slate-400">Circuit: 6V Battery • Switch • Bulb • Beaker Electrodes</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <svg viewBox="0 0 240 180" class="w-full h-44 mx-auto">
                <!-- Circuit Wires -->
                <path d="M 40 40 L 40 10 L 200 10 L 200 60" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
                <path d="M 40 40 L 40 90" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
                <path d="M 200 100 L 200 120 L 160 120" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
                <!-- 6V Battery -->
                <rect x="25" y="30" width="30" height="20" rx="3" fill="#334155" stroke="#94a3b8"/>
                <text x="40" y="44" font-size="8" fill="#f8fafc" font-weight="bold" text-anchor="middle">6V</text>
                <!-- Switch -->
                <circle cx="120" cy="10" r="3" fill="#cbd5e1"/>
                <circle cx="140" cy="10" r="3" fill="#cbd5e1"/>
                <line id="sim7SwitchArm" x1="120" y1="10" x2="140" y2="10" stroke="#f59e0b" stroke-width="3"/>
                <!-- Bulb -->
                <circle id="sim7BulbGlow" cx="200" cy="80" r="16" fill="#facc15" fill-opacity="0" class="transition-all duration-300"/>
                <circle id="sim7Bulb" cx="200" cy="80" r="10" fill="#334155" stroke="#94a3b8" stroke-width="1.5" class="transition-colors duration-300"/>
                <path d="M 197 80 Q 200 73 203 80" stroke="#f59e0b" stroke-width="1.5" fill="none"/>

                <!-- Beaker with Cork & Nails -->
                <rect x="70" y="80" width="100" height="90" rx="6" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
                <!-- Solution liquid -->
                <rect id="sim7Liquid" x="72" y="105" width="96" height="63" rx="4" fill="#38bdf8" fill-opacity="0.25" class="transition-colors duration-500"/>
                <!-- Rubber cork -->
                <rect x="95" y="145" width="50" height="15" rx="3" fill="#475569"/>
                <!-- Iron Nails (Electrodes) -->
                <line x1="105" y1="100" x2="105" y2="150" stroke="#94a3b8" stroke-width="3"/>
                <line x1="135" y1="100" x2="135" y2="150" stroke="#94a3b8" stroke-width="3"/>
                <!-- Connection wires to nails -->
                <path d="M 40 90 L 105 90 L 105 100" stroke="#f59e0b" stroke-width="2" fill="none"/>
                <path d="M 160 120 L 135 120 L 135 100" stroke="#f59e0b" stroke-width="2" fill="none"/>

                <!-- Ions in solution -->
                <g id="sim7Ions" class="transition-opacity duration-300">
                    <circle cx="90" cy="120" r="5" fill="#ef4444"/><text x="90" y="123" font-size="6" fill="#fff" text-anchor="middle">H+</text>
                    <circle cx="120" cy="115" r="5" fill="#3b82f6"/><text x="120" y="118" font-size="6" fill="#fff" text-anchor="middle">Cl-</text>
                    <circle cx="150" cy="125" r="5" fill="#ef4444"/><text x="150" y="128" font-size="6" fill="#fff" text-anchor="middle">H+</text>
                    <circle cx="115" cy="135" r="5" fill="#3b82f6"/><text x="115" y="138" font-size="6" fill="#fff" text-anchor="middle">Cl-</text>
                </g>
            </svg>

            <div class="space-y-2.5 text-xs">
                <span class="text-slate-400 block">Select Solution in Beaker:</span>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="setSim7Solution('HCl')" id="sim7BtnHCl" class="py-1.5 px-2 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 font-bold">Dilute HCl (Acid)</button>
                    <button onclick="setSim7Solution('H2SO4')" id="sim7BtnH2SO4" class="py-1.5 px-2 rounded-lg bg-slate-800 text-slate-300 font-bold">Dilute H2SO4 (Acid)</button>
                    <button onclick="setSim7Solution('glucose')" id="sim7BtnGlucose" class="py-1.5 px-2 rounded-lg bg-slate-800 text-slate-300 font-bold">Glucose (C6H12O6)</button>
                    <button onclick="setSim7Solution('alcohol')" id="sim7BtnAlcohol" class="py-1.5 px-2 rounded-lg bg-slate-800 text-slate-300 font-bold">Alcohol (C2H5OH)</button>
                </div>
                <div id="sim7BulbStatus" class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <span>Electric Bulb:</span>
                    <span id="sim7BulbText" class="font-bold text-amber-400">GLOWING BRIGHTLY</span>
                </div>
                <p id="sim7Explanation" class="text-[11px] text-slate-300 leading-relaxed">
                    <strong>HCl dissociates into mobile H+ and Cl- ions.</strong> These ions carry electric current through the solution gap, completing the circuit and lighting the bulb!
                </p>
            </div>
        </div>
    </div>
</div>

<script>
function setSim7Solution(sol) {
    ['HCl', 'H2SO4', 'glucose', 'alcohol'].forEach(s => {
        document.getElementById('sim7Btn' + s.charAt(0).toUpperCase() + s.slice(1)).className = (s === sol) ? 'py-1.5 px-2 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 font-bold' : 'py-1.5 px-2 rounded-lg bg-slate-800 text-slate-300 font-bold';
    });

    const bulb = document.getElementById('sim7Bulb');
    const glow = document.getElementById('sim7BulbGlow');
    const bText = document.getElementById('sim7BulbText');
    const ions = document.getElementById('sim7Ions');
    const exp = document.getElementById('sim7Explanation');

    if (sol === 'HCl' || sol === 'H2SO4') {
        bulb.setAttribute('fill', '#fde047');
        glow.setAttribute('fill-opacity', '0.6');
        bText.textContent = 'GLOWING BRIGHTLY';
        bText.className = 'font-bold text-amber-400';
        ions.classList.remove('opacity-0');
        exp.innerHTML = '<strong>' + sol + ' (Acid):</strong> Dissociates into free mobile cations (H+/H3O+) and anions that migrate toward the electrodes, conducting electricity and illuminating the bulb!';
    } else {
        bulb.setAttribute('fill', '#334155');
        glow.setAttribute('fill-opacity', '0');
        bText.textContent = 'BULB IS OFF (NO GLOW)';
        bText.className = 'font-bold text-slate-400';
        ions.classList.add('opacity-0');
        exp.innerHTML = '<strong>' + (sol === 'glucose' ? 'Glucose' : 'Alcohol') + ':</strong> Covalent bonds do not ionise in water. Without free mobile ions to carry charge, the liquid acts as an insulator and the bulb does not glow!';
    }
}
</script>
''',

    8: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 2.9: Water Requirement for Acid Ionisation (Dry vs Moist Litmus)</h4>
        <span class="text-xs text-slate-400">NaCl + conc. H2SO4 → NaHSO4 + HCl↑</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <svg viewBox="0 0 220 170" class="w-full h-44 mx-auto">
                <!-- Delivery Tube with exiting HCl Gas -->
                <path d="M 40 130 L 40 40 L 120 40" stroke="#94a3b8" stroke-width="4" fill="none"/>
                <!-- Test tube body -->
                <rect x="25" y="70" width="30" height="80" rx="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
                <rect x="27" y="115" width="26" height="30" rx="4" fill="#f8fafc" fill-opacity="0.8"/>
                <text x="40" y="132" font-size="7" fill="#0f172a" font-weight="bold" text-anchor="middle">NaCl + H2SO4</text>
                
                <!-- Exiting Dry HCl gas puffs -->
                <g id="sim8GasPuffs">
                    <circle cx="130" cy="40" r="5" fill="#e2e8f0" fill-opacity="0.5"/>
                    <circle cx="145" cy="38" r="6" fill="#e2e8f0" fill-opacity="0.4"/>
                    <circle cx="160" cy="36" r="7" fill="#e2e8f0" fill-opacity="0.3"/>
                    <text x="145" y="25" font-size="8" fill="#38bdf8" font-weight="bold">Dry HCl Gas</text>
                </g>

                <!-- Litmus Paper Strip held in front of gas -->
                <g id="sim8LitmusHolder" transform="translate(160, 20)">
                    <rect id="sim8PaperStrip" x="0" y="0" width="30" height="70" rx="2" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" class="transition-colors duration-500"/>
                    <text id="sim8PaperText" x="15" y="38" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">Blue Litmus</text>
                    <!-- Moisture droplets indicator -->
                    <g id="sim8MoistureDrops" class="hidden">
                        <circle cx="10" cy="20" r="2" fill="#38bdf8"/>
                        <circle cx="20" cy="30" r="2.5" fill="#38bdf8"/>
                        <circle cx="12" cy="50" r="2" fill="#38bdf8"/>
                    </g>
                </g>
            </svg>

            <div class="space-y-2.5 text-xs">
                <span class="text-slate-400 block">Select Litmus Paper State:</span>
                <div class="flex gap-2">
                    <button onclick="testSim8Litmus('dry')" id="sim8BtnDry" class="flex-1 py-1.5 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold">Dry Blue Litmus</button>
                    <button onclick="testSim8Litmus('moist')" id="sim8BtnMoist" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold">Moist Blue Litmus</button>
                </div>
                <div id="sim8ResultBox" class="p-2.5 rounded bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
                    <strong>Dry Blue Litmus exposed to Dry HCl Gas:</strong> No colour change whatsoever! Litmus remains completely blue because dry HCl cannot ionise without water.
                </div>
                <div class="p-2 rounded bg-cyan-500/10 border border-cyan-500/30 text-[11px] text-cyan-300">
                    <strong>Hydronium Ion Law:</strong> H+ cannot exist alone. In water: H+ + H2O → <strong>H3O+ (Hydronium Ion)</strong>.
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function testSim8Litmus(state) {
    const btnDry = document.getElementById('sim8BtnDry');
    const btnMoist = document.getElementById('sim8BtnMoist');
    const paper = document.getElementById('sim8PaperStrip');
    const pText = document.getElementById('sim8PaperText');
    const drops = document.getElementById('sim8MoistureDrops');
    const res = document.getElementById('sim8ResultBox');

    if (state === 'dry') {
        btnDry.className = 'flex-1 py-1.5 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold';
        btnMoist.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold';
        paper.setAttribute('fill', '#3b82f6');
        paper.setAttribute('stroke', '#1d4ed8');
        pText.textContent = 'Blue Litmus';
        drops.classList.add('hidden');
        res.innerHTML = '<strong>Dry Blue Litmus:</strong> NO COLOUR CHANGE. Hydrogen chloride gas does not liberate protons in the absence of water.';
    } else {
        btnDry.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold';
        btnMoist.className = 'flex-1 py-1.5 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-bold';
        drops.classList.remove('hidden');
        paper.setAttribute('fill', '#ef4444');
        paper.setAttribute('stroke', '#b91c1c');
        pText.textContent = 'Turns RED!';
        res.innerHTML = '<span class="text-rose-400 font-bold">MOIST BLUE LITMUS TURNS RED IMMEDIATELY!</span> Water on the paper pulls protons from HCl: HCl + H2O → H3O+ + Cl-, generating hydronium ions that change the indicator colour!';
    }
}
</script>
'''
}

if __name__ == "__main__":
    for k, v in simulators.items():
        print(f"Simulator {k}: length {len(v)} chars")
    print("All simulators 1 to 8 defined successfully!")

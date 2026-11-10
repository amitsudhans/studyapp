#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 11: Making Things
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Preparing Potter Clay
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏺</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Clay Preparation Bench (Wetting, Pounding &amp; Kneading)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Step-by-Step Studio</span>
    </div>

    <p class="text-xs text-slate-300">Click each clay preparation stage in order to transform rough dry soil clods into smooth, bubble-free potter dough!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setClayPrepStep('dry')" id="btn-cprep-dry" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">1. Dry Soil Clods</button>
        <button onclick="setClayPrepStep('wet')" id="btn-cprep-wet" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Wet With Water</button>
        <button onclick="setClayPrepStep('pound')" id="btn-cprep-pound" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Pound Hard</button>
        <button onclick="setClayPrepStep('knead')" id="btn-cprep-knead" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Knead Like Dough</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="0" y="135" width="320" height="45" fill="#451a03" opacity="0.6" />
            <!-- Wooden Prep Board -->
            <rect x="40" y="128" width="240" height="12" rx="4" fill="#78350f" />
            <!-- Dry Crumbly Clods -->
            <g id="cprep-dry-svg">
                <polygon points="95,128 115,92 148,96 155,128" fill="#92400e" />
                <polygon points="160,128 175,85 215,95 225,128" fill="#b45309" />
                <circle cx="135" cy="112" r="4" fill="#475569" />
                <circle cx="192" cy="108" r="5" fill="#64748b" />
            </g>
            <!-- Wet Slurry -->
            <g id="cprep-wet-svg" class="hidden">
                <ellipse cx="160" cy="116" rx="70" ry="20" fill="#78350f" />
                <path d="M125,52 Q160,82 155,105" stroke="#38bdf8" stroke-width="5" fill="none" stroke-linecap="round" />
                <path d="M185,48 Q170,82 175,105" stroke="#38bdf8" stroke-width="4" fill="none" stroke-linecap="round" />
                <circle cx="145" cy="68" r="3" fill="#7dd3fc" />
                <circle cx="165" cy="82" r="3" fill="#7dd3fc" />
            </g>
            <!-- Pounding Mallet -->
            <g id="cprep-pound-svg" class="hidden">
                <ellipse cx="160" cy="114" rx="68" ry="18" fill="#92400e" />
                <rect x="140" y="55" width="40" height="28" rx="5" fill="#d97706" />
                <rect x="180" y="64" width="60" height="8" rx="3" fill="#b45309" />
                <path d="M148,90 L140,80 M172,90 L180,80" stroke="#fde047" stroke-width="2" />
            </g>
            <!-- Smooth Kneaded Clay Ball -->
            <g id="cprep-knead-svg" class="hidden">
                <path d="M105,128 Q105,65 160,65 Q215,65 215,128 Z" fill="#c2410c" />
                <ellipse cx="145" cy="88" rx="16" ry="8" fill="#fdba74" opacity="0.35" />
            </g>
            <text x="160" y="162" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="cprep-svg-lbl">Dry crumbly soil clods cannot hold any pot shape yet!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="cprep-title">Stage 1: Raw Dry Soil Clods</h4>
            <p class="text-slate-300 leading-relaxed" id="cprep-desc">Hard dry earth lumps contain tiny air spaces, dried leaves, and pebbles. Shaping dry powder is impossible until water softens every grain!</p>
            <div class="text-[11px] bg-slate-900 p-2 rounded-lg border border-slate-800 text-emerald-300" id="cprep-stat">Plasticity: Low (0%) | Air Bubbles: Many</div>
        </div>
    </div>
</div>

<script>
function setClayPrepStep(step) {
    const info = {
        dry: { lbl: 'Dry crumbly soil clods cannot hold any pot shape yet!', t: 'Stage 1: Raw Dry Soil Clods', d: 'Hard dry earth lumps contain tiny air spaces, dried leaves, and pebbles. Shaping dry powder is impossible until water softens every grain!', stat: 'Plasticity: Low (0%) | Air Bubbles: Many' },
        wet: { lbl: 'Adding measured water softens sticky fine clay particles!', t: 'Stage 2: Wetting Fine Clay Soil', d: 'Adding clean water moistens every clay particle so particles begin sticking tightly together cleanly without crumbling apart.', stat: 'Plasticity: Medium (45%) | Moisture: Even' },
        pound: { lbl: 'Pounding forces out trapped air bubbles & pebbles!', t: 'Stage 3: Pounding Out Air Pockets', d: 'A heavy wooden mallet slams and pounds the moist clay repeatedly to break hard lumps and force out trapped air pockets cleanly!', stat: 'Plasticity: High (75%) | Air Bubbles: Almost Gone' },
        knead: { lbl: 'Smooth kneaded clay stretches cleanly just like chapati dough!', t: 'Stage 4: Kneading Smooth Like Dough', d: 'Just like kneading wheat flour dough for rotis, strong hands fold and press clay until glossy, silky, uniform, and ready for the spinning wheel!', stat: 'Plasticity: Maximum (100%) | Wheel Ready!' }
    };
    const d = info[step];
    if (!d) return;
    ['dry', 'wet', 'pound', 'knead'].forEach(k => {
        const b = document.getElementById('btn-cprep-' + k);
        if (b) {
            b.className = (k === step)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('cprep-' + k + '-svg');
        if (g) {
            if (k === step) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('cprep-svg-lbl').textContent = d.lbl;
    document.getElementById('cprep-title').textContent = d.t;
    document.getElementById('cprep-desc').textContent = d.d;
    document.getElementById('cprep-stat').textContent = d.stat;
}
</script>
"""

# Simulator 2: Spinning Stone Wheel
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎡</span>
            <h3 class="text-sm sm:text-base font-bold text-orange-300">Spinning Stone Potter Wheel Shaper</h3>
        </div>
        <span class="text-[11px] bg-orange-950/80 text-orange-300 px-2.5 py-1 rounded-full border border-orange-800">Interactive Wheel</span>
    </div>

    <p class="text-xs text-slate-300">Spin the heavy stone disc fast and gently press clay upwards or outwards to mould different symmetrical vessels!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="shapeWheelPot('lump')" id="btn-wpot-lump" class="p-2.5 rounded-xl bg-orange-600 text-white font-bold text-xs border border-orange-500">Clay Lump</button>
        <button onclick="shapeWheelPot('kulhad')" id="btn-wpot-kulhad" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">☕ Tea Kulhad</button>
        <button onclick="shapeWheelPot('matka')" id="btn-wpot-matka" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏺 Water Matka</button>
        <button onclick="shapeWheelPot('diya')" id="btn-wpot-diya" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪔 Clay Diya</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 185" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Stone Wheel Base & Axle -->
            <rect x="148" y="138" width="24" height="32" fill="#475569" />
            <ellipse cx="160" cy="135" rx="105" ry="18" fill="#64748b" stroke="#94a3b8" stroke-width="2" />
            <ellipse cx="160" cy="132" rx="75" ry="10" fill="#475569" stroke="#cbd5e1" stroke-dasharray="6,6" stroke-width="1.5">
                <animateTransform attributeName="transform" type="rotate" from="0 160 132" to="360 160 132" dur="2.5s" repeatCount="indefinite" />
            </ellipse>
            <!-- Center Lump -->
            <g id="wpot-lump-svg">
                <path d="M125,132 Q128,85 160,85 Q192,85 195,132 Z" fill="#c2410c" />
            </g>
            <!-- Kulhad -->
            <g id="wpot-kulhad-svg" class="hidden">
                <polygon points="138,132 128,68 192,68 182,132" fill="#ea580c" />
                <ellipse cx="160" cy="68" rx="32" ry="7" fill="#9a3412" />
            </g>
            <!-- Matka -->
            <g id="wpot-matka-svg" class="hidden">
                <path d="M135,132 Q100,100 135,68 L142,56 L178,56 L185,68 Q220,100 185,132 Z" fill="#c2410c" />
                <ellipse cx="160" cy="56" rx="18" ry="5" fill="#7c2d12" />
            </g>
            <!-- Diya -->
            <g id="wpot-diya-svg" class="hidden">
                <path d="M120,114 Q160,142 200,114 Q160,106 120,114 Z" fill="#ea580c" />
                <ellipse cx="160" cy="113" rx="36" ry="7" fill="#9a3412" />
            </g>
            <text x="160" y="175" fill="#fdba74" font-size="10" font-weight="bold" text-anchor="middle" id="wpot-svg-lbl">Centered soft dough lump spins steadily on the heavy stone wheel!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-orange-300 text-sm" id="wpot-title">Centered Clay Lump</h4>
            <p class="text-slate-300 leading-relaxed" id="wpot-desc">First, the skilled potter throws kneaded clay right onto the exact middle of the heavy stone disc so it spins evenly without wobbling sideways!</p>
            <div class="text-[11px] text-amber-300 bg-slate-900 p-2 rounded border border-slate-800">Tip: Wet fingers reduce friction while raising smooth round walls!</div>
        </div>
    </div>
</div>

<script>
function shapeWheelPot(shape) {
    const map = {
        lump: { lbl: 'Centered soft dough lump spins steadily on the heavy stone wheel!', t: 'Centered Clay Lump', d: 'First, the skilled potter throws kneaded clay right onto the exact middle of the heavy stone disc so it spins evenly without wobbling sideways!' },
        kulhad: { lbl: 'Thumbs open the center and fingers pull slender tall tea cup walls!', t: 'Symmetrical Tea Kulhad', d: 'Gently pulling upward between damp thumbs and forefingers lifts slender flaring cup walls, creating round, heat-safe traditional tea kulhads!' },
        matka: { lbl: 'Pushing outward from inside swells a cool rounded water pot belly!', t: 'Round Water Cooling Matka', d: 'While one hand supports outside, the other pushes gently from inside to swell out a wide, graceful water-cooling vessel with a narrow rim!' },
        diya: { lbl: 'Spreading clay low creates wide shallow festive diya saucers!', t: 'Shallow Festive Clay Diya', d: 'Opening clay gently outward and pinching one side creates neat shallow oil lamp saucers ready to illuminate celebrations cleanly!' }
    };
    const d = map[shape];
    if (!d) return;
    ['lump', 'kulhad', 'matka', 'diya'].forEach(k => {
        const b = document.getElementById('btn-wpot-' + k);
        if (b) {
            b.className = (k === shape)
                ? 'p-2.5 rounded-xl bg-orange-600 text-white font-bold text-xs border border-orange-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('wpot-' + k + '-svg');
        if (g) {
            if (k === shape) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('wpot-svg-lbl').textContent = d.lbl;
    document.getElementById('wpot-title').textContent = d.t;
    document.getElementById('wpot-desc').textContent = d.d;
}
</script>
"""

# Simulator 3: Drying And Kilns
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔥</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Sun Drying vs. Hot Kiln Baking Lab</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Thermal Hardening</span>
    </div>

    <p class="text-xs text-slate-300">Test pouring cool drinking water into three pots at different stages to see why hot kiln baking is crucial!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="testKilnPot('wet')" id="btn-kiln-wet" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">1. Wet Fresh Pot</button>
        <button onclick="testKilnPot('sundried')" id="btn-kiln-sundried" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Sun-Dried Pot</button>
        <button onclick="testKilnPot('baked')" id="btn-kiln-baked" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Kiln-Baked Pot</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 185" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Wet -->
            <g id="kiln-wet-svg">
                <path d="M120,135 Q105,110 130,90 L185,95 Q210,120 185,135 Z" fill="#78350f" />
                <path d="M140,135 Q160,145 190,135" stroke="#38bdf8" stroke-width="5" fill="none" />
                <text x="160" y="55" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">SOFT COLLAPSED MUD!</text>
            </g>
            <!-- Sun Dried -->
            <g id="kiln-sundried-svg" class="hidden">
                <circle cx="265" cy="40" r="18" fill="#fde047" />
                <path d="M130,135 Q110,95 140,68 L180,68 Q210,95 190,135 Z" fill="#a8a29e" />
                <path d="M150,95 L165,115 L155,130" stroke="#38bdf8" stroke-width="3" fill="none" />
                <text x="140" y="45" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">MELTS BACK INTO MUD IN WATER!</text>
            </g>
            <!-- Kiln Baked -->
            <g id="kiln-baked-svg" class="hidden">
                <path d="M120,145 Q160,55 200,145 Z" fill="#dc2626" opacity="0.25" />
                <path d="M130,135 Q110,95 140,68 L180,68 Q210,95 190,135 Z" fill="#ea580c" stroke="#fed7aa" stroke-width="1.5" />
                <ellipse cx="160" cy="68" rx="20" ry="5" fill="#38bdf8" />
                <path d="M142,155 Q150,140 160,155 Q170,140 178,155" stroke="#f97316" stroke-width="3" fill="none" />
                <text x="160" y="42" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">RINGING HARD WATERPROOF TERRACOTTA!</text>
            </g>
            <text x="160" y="172" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle" id="kiln-svg-lbl">Fresh wet clay slumps instantly when holding water!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-rose-300 text-sm" id="kiln-title">1. Unbaked Wet Greenware</h4>
            <p class="text-slate-300 leading-relaxed" id="kiln-desc">Straight off the spinning wheel, raw greenware is soft and squishy. Putting water directly inside dissolves walls back into sloppy brown mud!</p>
            <div class="text-[11px] bg-slate-900 p-2 rounded border border-slate-800 text-amber-300" id="kiln-stat">Water Resistance: 0% (Dissolves)</div>
        </div>
    </div>
</div>

<script>
function testKilnPot(state) {
    const map = {
        wet: { lbl: 'Fresh wet clay slumps instantly when holding water!', t: '1. Unbaked Wet Greenware', d: 'Straight off the spinning wheel, raw greenware is soft and squishy. Putting water directly inside dissolves walls back into sloppy brown mud!', stat: 'Water Resistance: 0% (Slumps Fast)' },
        sundried: { lbl: 'Warm sunlight dries water out, yet rain still softens raw clay!', t: '2. Sun-Dried Delicate Clay', d: 'Drying under warm sunshine turns pots light grey and stiff enough to lift carefully. However, raw unbaked clay still softens and crumbles if soaked in water!', stat: 'Water Resistance: 15% (Still Dissolves in Water)' },
        baked: { lbl: 'Fierce kiln heat transforms soft clay permanently into stone-hard pottery!', t: '3. Hot Kiln-Baked Pottery', d: 'Inside a roaring brick oven called a kiln, intense glowing heat fuses clay grains permanently into bright terracotta that holds water cleanly for years!', stat: 'Water Resistance: 100% (Waterproof Stone-Hard!)' }
    };
    const d = map[state];
    if (!d) return;
    ['wet', 'sundried', 'baked'].forEach(k => {
        const b = document.getElementById('btn-kiln-' + k);
        if (b) {
            b.className = (k === state)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('kiln-' + k + '-svg');
        if (g) {
            if (k === state) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('kiln-svg-lbl').textContent = d.lbl;
    document.getElementById('kiln-title').textContent = d.t;
    document.getElementById('kiln-desc').textContent = d.d;
    document.getElementById('kiln-stat').textContent = d.stat;
}
</script>
"""

# Simulator 4: Sieving Clay Craft (Activity 2)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧪</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Activity 2: Soil Sieving &amp; Sedimentation Clay Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Class Clay Craft</span>
    </div>

    <p class="text-xs text-slate-300">Follow all four classroom science steps to extract silky fine sculpting clay out of ordinary backyard soil!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setSieveStage(1)" id="btn-sieve-1" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Sieve Stones</button>
        <button onclick="setSieveStage(2)" id="btn-sieve-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Stir In Water</button>
        <button onclick="setSieveStage(3)" id="btn-sieve-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Pour Off Water</button>
        <button onclick="setSieveStage(4)" id="btn-sieve-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Sculpt &amp; Dry</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Step 1: Sieve -->
            <g id="sieve-stage-1">
                <rect x="85" y="45" width="150" height="22" rx="4" fill="#64748b" />
                <line x1="95" y1="67" x2="225" y2="67" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="2" />
                <circle cx="135" cy="40" r="6" fill="#94a3b8" />
                <circle cx="170" cy="42" r="5" fill="#94a3b8" />
                <path d="M100,145 Q160,95 220,145 Z" fill="#92400e" />
                <text x="160" y="92" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Fine dust falls through; stones stay above!</text>
            </g>
            <!-- Step 2: Water Settling Jar -->
            <g id="sieve-stage-2" class="hidden">
                <rect x="115" y="35" width="90" height="115" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
                <rect x="117" y="55" width="86" height="60" fill="#0ea5e9" opacity="0.4" />
                <rect x="117" y="115" width="86" height="33" fill="#92400e" />
                <text x="160" y="135" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">CLAY SEDIMENT</text>
            </g>
            <!-- Step 3: Decant Water -->
            <g id="sieve-stage-3" class="hidden">
                <rect x="85" y="45" width="75" height="90" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2" transform="rotate(-25 120 90)" />
                <path d="M162,72 Q195,95 198,135" stroke="#38bdf8" stroke-width="6" fill="none" stroke-linecap="round" />
                <rect x="92" y="112" width="60" height="22" fill="#b45309" transform="rotate(-25 120 90)" />
            </g>
            <!-- Step 4: Sculpt Toy -->
            <g id="sieve-stage-4" class="hidden">
                <circle cx="265" cy="40" r="16" fill="#fde047" />
                <ellipse cx="160" cy="118" rx="45" ry="25" fill="#d97706" />
                <circle cx="130" cy="95" r="18" fill="#d97706" />
                <circle cx="122" cy="90" r="3" fill="#0f172a" />
                <path d="M112,96 Q102,118 118,125" stroke="#d97706" stroke-width="7" fill="none" stroke-linecap="round" />
                <text x="160" y="158" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Cute Sculpted Clay Elephant Drying in Sun!</text>
            </g>
            <text x="160" y="172" fill="#67e8f9" font-size="10" font-weight="bold" text-anchor="middle" id="sieve-svg-lbl">Sieve catches heavy pebbles and twigs cleanly!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-cyan-300 text-sm" id="sieve-title">Step 1: Sieve Dry Soil</h4>
            <p class="text-slate-300 leading-relaxed" id="sieve-desc">Shaking garden soil through a fine mesh sieve catches sharp stones, twigs, and dry leaves while letting pure soft dust pile neatly underneath.</p>
        </div>
    </div>
</div>

<script>
function setSieveStage(n) {
    const info = {
        1: { lbl: 'Sieve catches heavy pebbles and twigs cleanly!', t: 'Step 1: Sieve Dry Soil', d: 'Shaking garden soil through a fine mesh sieve catches sharp stones, twigs, and dry leaves while letting pure soft dust pile neatly underneath.' },
        2: { lbl: 'Heavy fine clay settles peacefully at the bottom!', t: 'Step 2: Stir & Settle In Water', d: 'Mixing sieved soil thoroughly inside a jar of clean water floats tiny leaf bits upward while ultra-smooth fine clay settles heavily onto the bottom.' },
        3: { lbl: 'Pour out top water gently leaving silky wet clay behind!', t: 'Step 3: Decant Excess Top Water', d: 'Once top water turns mostly clear, slowly tilt the jar to pour off liquid carefully, uncovering smooth silky clay mud ready for shaping.' },
        4: { lbl: 'Sun warmth dries handmade bowls and animal models firm!', t: 'Step 4: Sculpt & Sun-Dry Models', d: 'Pinch, roll, and join smooth clay parts into charming bowls or toy elephants, then let open warm sunshine dry your sculptures gently!' }
    };
    const d = info[n];
    if (!d) return;
    [1, 2, 3, 4].forEach(k => {
        const b = document.getElementById('btn-sieve-' + k);
        if (b) {
            b.className = (k === n)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('sieve-stage-' + k);
        if (g) {
            if (k === n) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('sieve-svg-lbl').textContent = d.lbl;
    document.getElementById('sieve-title').textContent = d.t;
    document.getElementById('sieve-desc').textContent = d.d;
}
</script>
"""

# Simulator 5: Visiting Local Potters (Activity 1)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛍️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Activity 1: Potter Courtyard Vessels Showcase</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Field Visit</span>
    </div>

    <p class="text-xs text-slate-300">Explore traditional clay vessels drying outside a neighborhood workshop and learn how each clever shape serves families daily!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectVessel('matka')" id="btn-ves-matka" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🏺 Water Matka</button>
        <button onclick="inspectVessel('handi')" id="btn-ves-handi" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍲 Cooking Handi</button>
        <button onclick="inspectVessel('gamla')" id="btn-ves-gamla" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪴 Plant Gamla</button>
        <button onclick="inspectVessel('diya')" id="btn-ves-diya" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪔 Festive Diya</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="20" y="138" width="280" height="12" fill="#475569" />
            <!-- Matka -->
            <g id="ves-matka-svg">
                <circle cx="160" cy="96" r="42" fill="#c2410c" />
                <rect x="142" y="45" width="36" height="14" fill="#9a3412" />
                <path d="M210,80 L230,72 M210,100 L230,100" stroke="#38bdf8" stroke-width="2" />
                <text x="240" y="90" fill="#7dd3fc" font-size="9" font-weight="bold">COOLING PORES!</text>
            </g>
            <!-- Handi -->
            <g id="ves-handi-svg" class="hidden">
                <ellipse cx="160" cy="112" rx="52" ry="30" fill="#9a3412" />
                <ellipse cx="160" cy="88" rx="34" ry="8" fill="#431407" />
                <path d="M135,70 Q140,55 135,42 M160,65 Q165,50 160,38 M185,70 Q190,55 185,42" stroke="#cbd5e1" stroke-width="2" fill="none" />
            </g>
            <!-- Gamla -->
            <g id="ves-gamla-svg" class="hidden">
                <polygon points="120,75 200,75 185,138 135,138" fill="#b45309" />
                <rect x="115" y="68" width="90" height="10" rx="2" fill="#d97706" />
                <path d="M160,68 L160,32 M160,48 L142,35 M160,48 L178,35" stroke="#22c55e" stroke-width="3" fill="none" />
                <circle cx="140" cy="34" r="7" fill="#22c55e" />
                <circle cx="180" cy="34" r="7" fill="#22c55e" />
            </g>
            <!-- Diya -->
            <g id="ves-diya-svg" class="hidden">
                <path d="M110,115 Q160,145 210,115 Z" fill="#ea580c" />
                <path d="M198,108 Q210,75 200,60 Q188,75 198,108 Z" fill="#fde047" />
                <path d="M198,105 Q204,88 199,78 Q193,88 198,105 Z" fill="#f97316" />
            </g>
            <text x="160" y="168" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="ves-svg-lbl">Microscopic clay pores gently evaporate drops to cool drinking water!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="ves-title">Natural Cooling Water Matka</h4>
            <p class="text-slate-300 leading-relaxed" id="ves-desc">Tiny unseen pores inside baked terracotta let minute droplets seep outward and evaporate, chilling drinking water naturally without electricity!</p>
        </div>
    </div>
</div>

<script>
function inspectVessel(item) {
    const map = {
        matka: { lbl: 'Microscopic clay pores gently evaporate drops to cool drinking water!', t: 'Natural Cooling Water Matka', d: 'Tiny unseen pores inside baked terracotta let minute droplets seep outward and evaporate, chilling drinking water naturally without electricity!' },
        handi: { lbl: 'Thick clay walls hold gentle heat evenly for tasty slow-simmered dishes!', t: 'Traditional Cooking Clay Handi', d: 'Wide bellied cooking pots distribute mild warmth evenly across rice, dals, and curries while infusing a pleasant earthy aroma cleanly.' },
        gamla: { lbl: 'Breathable flowerpot walls help growing roots drink moisture comfortably!', t: 'Breathable Clay Garden Pot (Gamla)', d: 'Porous baked soil lets delicate roots breathe oxygen and drains excess water through bottom holes so garden herbs stay healthy!' },
        diya: { lbl: 'Eco-friendly clay oil lamps shine during festivals and return cleanly to Earth!', t: 'Festive Hand-Pinched Oil Diya', d: 'Millions of biodegradable diyas warm autumn festivals with golden flames and break down safely into natural garden soil afterward.' }
    };
    const d = map[item];
    if (!d) return;
    ['matka', 'handi', 'gamla', 'diya'].forEach(k => {
        const b = document.getElementById('btn-ves-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('ves-' + k + '-svg');
        if (g) {
            if (k === item) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('ves-svg-lbl').textContent = d.lbl;
    document.getElementById('ves-title').textContent = d.t;
    document.getElementById('ves-desc').textContent = d.d;
}
</script>
"""

# Simulator 6: Neem Branch Patterns
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌿</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Neem Twig &amp; Botanical Pattern Explorer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Nature Geometry</span>
    </div>

    <p class="text-xs text-slate-300">Highlight repeating mathematical structures along a compound neem leaf twig and discover nature pattern rules!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectNeem('pairs')" id="btn-neem-pairs" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Opposite Pairs</button>
        <button onclick="inspectNeem('edges')" id="btn-neem-edges" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Sawtooth Edges</button>
        <button onclick="inspectNeem('veins')" id="btn-neem-veins" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Repeating Veins</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Central Stem -->
            <line x1="60" y1="90" x2="265" y2="90" stroke="#166534" stroke-width="4" stroke-linecap="round" />
            <!-- Tip Leaflet -->
            <path d="M265,90 Q285,78 302,90 Q285,102 265,90 Z" fill="#22c55e" />
            <!-- 4 Pairs of Opposite Leaflets -->
            <path d="M100,90 Q112,50 135,45 Q130,75 100,90 Z" fill="#22c55e" />
            <path d="M100,90 Q112,130 135,135 Q130,105 100,90 Z" fill="#22c55e" />
            <path d="M145,90 Q157,52 180,47 Q175,77 145,90 Z" fill="#22c55e" />
            <path d="M145,90 Q157,128 180,133 Q175,103 145,90 Z" fill="#22c55e" />
            <path d="M190,90 Q202,55 225,50 Q220,78 190,90 Z" fill="#22c55e" />
            <path d="M190,90 Q202,125 225,130 Q220,102 190,90 Z" fill="#22c55e" />
            <path d="M235,90 Q245,62 262,58 Q258,82 235,90 Z" fill="#22c55e" />
            <path d="M235,90 Q245,118 262,122 Q258,98 235,90 Z" fill="#22c55e" />
            <!-- Highlight Overlay -->
            <g id="neem-ov-pairs">
                <circle cx="100" cy="90" r="5" fill="#fde047" />
                <circle cx="145" cy="90" r="5" fill="#fde047" />
                <circle cx="190" cy="90" r="5" fill="#fde047" />
                <circle cx="235" cy="90" r="5" fill="#fde047" />
            </g>
            <g id="neem-ov-edges" class="hidden">
                <path d="M110,60 L118,52 L126,56 L132,46" stroke="#fde047" stroke-width="2" fill="none" />
                <path d="M155,62 L163,54 L171,58 L177,48" stroke="#fde047" stroke-width="2" fill="none" />
            </g>
            <g id="neem-ov-veins" class="hidden">
                <line x1="100" y1="90" x2="128" y2="54" stroke="#bbf7d0" stroke-width="1.5" />
                <line x1="145" y1="90" x2="173" y2="56" stroke="#bbf7d0" stroke-width="1.5" />
                <line x1="190" y1="90" x2="218" y2="59" stroke="#bbf7d0" stroke-width="1.5" />
            </g>
            <text x="160" y="168" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" id="neem-svg-lbl">Neem leaflets line up rhythmically in balanced twin pairs!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="neem-title">Rhythmic Opposite Leaflet Pairs</h4>
            <p class="text-slate-300 leading-relaxed" id="neem-desc">Along one slender central twig, matching neem leaflets sprout in tidy pairs on both sides, creating a repeating ladder-like leaf rhythm potters love painting!</p>
        </div>
    </div>
</div>

<script>
function inspectNeem(mode) {
    const map = {
        pairs: { lbl: 'Neem leaflets line up rhythmically in balanced twin pairs!', t: 'Rhythmic Opposite Leaflet Pairs', d: 'Along one slender central twig, matching neem leaflets sprout in tidy pairs on both sides, creating a repeating ladder-like leaf rhythm potters love painting!' },
        edges: { lbl: 'Tiny zigzag tooth notches repeat evenly along leaf margins!', t: 'Repeating Sawtooth Margins', d: 'Look closer along every neem blade border: neat identical jagged curves repeat over and over, forming a delicate natural zigzag pattern!' },
        veins: { lbl: 'Branching veins deliver sap evenly across repeating angles!', t: 'Diagonal Parallel Vein Lattice', d: 'Fine glowing ribs branch out diagonally from every leaflet center line at regular intervals, inspiring carved line bands around earthen pots.' }
    };
    const d = map[mode];
    if (!d) return;
    ['pairs', 'edges', 'veins'].forEach(k => {
        const b = document.getElementById('btn-neem-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('neem-ov-' + k);
        if (g) {
            if (k === mode) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('neem-svg-lbl').textContent = d.lbl;
    document.getElementById('neem-title').textContent = d.t;
    document.getElementById('neem-desc').textContent = d.d;
}
</script>
"""

# Simulator 7: Wildlife Body Patterns
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🦚</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Wildlife Patterns &amp; Symmetry Explorer</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">5 Wild Creatures</span>
    </div>

    <p class="text-xs text-slate-300">Inspect zoomed animal coats, feathers, and wings to learn how repeating patterns protect wildlife and inspire art!</p>

    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
        <button onclick="inspectWildlife('tiger')" id="btn-wild-tiger" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">🐯 Tiger</button>
        <button onclick="inspectWildlife('zebra')" id="btn-wild-zebra" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🦓 Zebra</button>
        <button onclick="inspectWildlife('leopard')" id="btn-wild-leopard" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🐆 Leopard</button>
        <button onclick="inspectWildlife('peacock')" id="btn-wild-peacock" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🦚 Peacock</button>
        <button onclick="inspectWildlife('butterfly')" id="btn-wild-butterfly" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🦋 Butterfly</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Tiger Stripes -->
            <g id="wild-tiger-svg">
                <rect x="60" y="30" width="200" height="110" rx="16" fill="#f97316" />
                <path d="M85,30 L95,85 L105,30 M130,30 L142,95 L155,30 M180,30 L190,82 L202,30 M220,30 L230,90 L242,30" stroke="#0f172a" stroke-width="10" fill="none" />
                <path d="M110,140 L120,90 L132,140 M162,140 L172,88 L184,140 M205,140 L215,92 L226,140" stroke="#0f172a" stroke-width="9" fill="none" />
            </g>
            <!-- Zebra -->
            <g id="wild-zebra-svg" class="hidden">
                <rect x="60" y="30" width="200" height="110" rx="16" fill="#f8fafc" />
                <path d="M80,30 Q95,85 80,140 M115,30 Q130,85 115,140 M150,30 Q165,85 150,140 M185,30 Q200,85 185,140 M220,30 Q235,85 220,140" stroke="#0f172a" stroke-width="14" fill="none" />
            </g>
            <!-- Leopard -->
            <g id="wild-leopard-svg" class="hidden">
                <rect x="60" y="30" width="200" height="110" rx="16" fill="#fbbf24" />
                <circle cx="105" cy="65" r="14" fill="none" stroke="#451a03" stroke-width="5" stroke-dasharray="10,4" />
                <circle cx="160" cy="60" r="16" fill="none" stroke="#451a03" stroke-width="5" stroke-dasharray="12,4" />
                <circle cx="215" cy="70" r="14" fill="none" stroke="#451a03" stroke-width="5" stroke-dasharray="10,4" />
                <circle cx="130" cy="110" r="15" fill="none" stroke="#451a03" stroke-width="5" stroke-dasharray="11,4" />
                <circle cx="195" cy="112" r="14" fill="none" stroke="#451a03" stroke-width="5" stroke-dasharray="10,4" />
            </g>
            <!-- Peacock -->
            <g id="wild-peacock-svg" class="hidden">
                <rect x="60" y="30" width="200" height="110" rx="16" fill="#065f46" />
                <ellipse cx="160" cy="85" rx="45" ry="38" fill="#10b981" />
                <ellipse cx="160" cy="85" rx="28" ry="22" fill="#2563eb" />
                <circle cx="160" cy="85" r="12" fill="#1e1b4b" />
                <circle cx="164" cy="81" r="4" fill="#fde047" />
            </g>
            <!-- Butterfly -->
            <g id="wild-butterfly-svg" class="hidden">
                <path d="M160,85 Q90,20 85,75 Q95,105 160,85 Z" fill="#ec4899" />
                <path d="M160,85 Q230,20 235,75 Q225,105 160,85 Z" fill="#ec4899" />
                <path d="M160,85 Q105,95 110,132 Q145,125 160,85 Z" fill="#a855f7" />
                <path d="M160,85 Q215,95 210,132 Q175,125 160,85 Z" fill="#a855f7" />
                <rect x="157" y="55" width="6" height="55" rx="3" fill="#e2e8f0" />
            </g>
            <text x="160" y="164" fill="#d8b4fe" font-size="10" font-weight="bold" text-anchor="middle" id="wild-svg-lbl">Wavy dark stripes hide tigers neatly inside tall golden forest grass!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-purple-300 text-sm" id="wild-title">Bengal Tiger: Golden Orange &amp; Black Stripes</h4>
            <p class="text-slate-300 leading-relaxed" id="wild-desc">Irregular vertical dark bands break up the tiger silhouette inside tall swaying dry grass and dappled sunlit jungle shadows—helping it stay hidden cleanly!</p>
        </div>
    </div>
</div>

<script>
function inspectWildlife(animal) {
    const map = {
        tiger: { lbl: 'Wavy dark stripes hide tigers neatly inside tall golden forest grass!', t: 'Bengal Tiger: Golden Orange & Black Stripes', d: 'Irregular vertical dark bands break up the tiger silhouette inside tall swaying dry grass and dappled sunlit jungle shadows—helping it stay hidden cleanly!' },
        zebra: { lbl: 'Unique black-and-white zebra stripes dazzle fast-chasing predators!', t: 'Zebra Herd: Black & White Stripes', d: 'No two zebras share exact stripe maps! Running tightly in herds merges black and white ribbons into a dizzy optical puzzle for lions.' },
        leopard: { lbl: 'Ring-shaped dark rosettes blend leopards smoothly into shady tree leaves!', t: 'Leopard: Spotted Ring Rosettes', d: 'Clustered flower-like dark spots across warm gold fur mimic patchy leaves and shadow spots along tree branches where leopards rest quietly.' },
        peacock: { lbl: 'Vibrant green, cobalt blue & gold eye-spots shimmer across tail feathers!', t: 'Peacock: Shimmering Eye-Spot Plumes', d: 'Dozens of concentric turquoise, sapphire blue, and golden feather eyes fan outward gracefully—inspiring prized traditional Indian textile and pot designs!' },
        butterfly: { lbl: 'Left and right butterfly wings mirror each other in identical symmetry!', t: 'Butterfly: Mirror-Symmetrical Wings', d: 'Every bright swirl, rim dot, and band painted on a left butterfly wing repeats in exact mirror symmetry across its right wing!' }
    };
    const d = map[animal];
    if (!d) return;
    ['tiger', 'zebra', 'leopard', 'peacock', 'butterfly'].forEach(k => {
        const b = document.getElementById('btn-wild-' + k);
        if (b) {
            b.className = (k === animal)
                ? 'p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('wild-' + k + '-svg');
        if (g) {
            if (k === animal) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('wild-svg-lbl').textContent = d.lbl;
    document.getElementById('wild-title').textContent = d.t;
    document.getElementById('wild-desc').textContent = d.d;
}
</script>
"""

# Simulator 8: Decorating Indian Pottery (Activity 4)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎨</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Activity 4: Traditional Indian Pottery Pattern Studio</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Design Craft</span>
    </div>

    <p class="text-xs text-slate-300">Pick traditional natural motifs inspired by rivers, neem branches, dots, and peacocks to paint custom pottery bands!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="paintPotMotif('waves')" id="btn-pmot-waves" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">〰️ Zigzag Waves</button>
        <button onclick="paintPotMotif('leaves')" id="btn-pmot-leaves" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌿 Leaf Border</button>
        <button onclick="paintPotMotif('dots')" id="btn-pmot-dots" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⚪ Folk Dots</button>
        <button onclick="paintPotMotif('eyes')" id="btn-pmot-eyes" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🦚 Eye Motifs</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Base Painted Terracotta Surahi/Pot -->
            <path d="M125,148 Q82,110 128,62 L138,32 L182,32 L192,62 Q238,110 195,148 Z" fill="#b91c1c" stroke="#fef3c7" stroke-width="1.5" />
            <ellipse cx="160" cy="32" rx="22" ry="5" fill="#7f1d1d" />
            <!-- Motif 1: Zigzag Waves -->
            <g id="pmot-waves-svg">
                <polyline points="108,92 122,82 135,92 148,82 160,92 172,82 185,92 198,82 212,92" fill="none" stroke="#fef3c7" stroke-width="3" />
                <polyline points="108,116 122,106 135,116 148,106 160,116 172,106 185,116 198,106 212,116" fill="none" stroke="#fde047" stroke-width="3" />
            </g>
            <!-- Motif 2: Leaf Border -->
            <g id="pmot-leaves-svg" class="hidden">
                <line x1="106" y1="100" x2="214" y2="100" stroke="#fef3c7" stroke-width="2" />
                <ellipse cx="122" cy="91" rx="7" ry="4" transform="rotate(-30 122 91)" fill="#fef3c7" />
                <ellipse cx="148" cy="91" rx="7" ry="4" transform="rotate(-30 148 91)" fill="#fef3c7" />
                <ellipse cx="174" cy="91" rx="7" ry="4" transform="rotate(-30 174 91)" fill="#fef3c7" />
                <ellipse cx="200" cy="91" rx="7" ry="4" transform="rotate(-30 200 91)" fill="#fef3c7" />
                <ellipse cx="122" cy="109" rx="7" ry="4" transform="rotate(30 122 109)" fill="#fde047" />
                <ellipse cx="148" cy="109" rx="7" ry="4" transform="rotate(30 148 109)" fill="#fde047" />
                <ellipse cx="174" cy="109" rx="7" ry="4" transform="rotate(30 174 109)" fill="#fde047" />
                <ellipse cx="200" cy="109" rx="7" ry="4" transform="rotate(30 200 109)" fill="#fde047" />
            </g>
            <!-- Motif 3: Folk Dots -->
            <g id="pmot-dots-svg" class="hidden">
                <circle cx="115" cy="90" r="4" fill="#fef3c7" /><circle cx="137" cy="90" r="4" fill="#fef3c7" /><circle cx="160" cy="90" r="4" fill="#fef3c7" /><circle cx="183" cy="90" r="4" fill="#fef3c7" /><circle cx="205" cy="90" r="4" fill="#fef3c7" />
                <circle cx="126" cy="110" r="6" fill="#fde047" /><circle cx="160" cy="110" r="6" fill="#fde047" /><circle cx="194" cy="110" r="6" fill="#fde047" />
            </g>
            <!-- Motif 4: Peacock Eyes -->
            <g id="pmot-eyes-svg" class="hidden">
                <ellipse cx="128" cy="100" rx="10" ry="14" fill="#fef3c7" /><circle cx="128" cy="100" r="5" fill="#1e3a8a" />
                <ellipse cx="160" cy="100" rx="10" ry="14" fill="#fef3c7" /><circle cx="160" cy="100" r="5" fill="#1e3a8a" />
                <ellipse cx="192" cy="100" rx="10" ry="14" fill="#fef3c7" /><circle cx="192" cy="100" r="5" fill="#1e3a8a" />
            </g>
            <text x="160" y="168" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="pmot-svg-lbl">White &amp; ochre earth pigments paint rhythmic wavy river bands!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="pmot-title">Zigzag River Wave Bands</h4>
            <p class="text-slate-300 leading-relaxed" id="pmot-desc">Indian potters wrap horizontal circles of crisp white chalk clay and yellow ochre slips into flowing zigzag river stripes while spinning the wheel slowly!</p>
        </div>
    </div>
</div>

<script>
function paintPotMotif(motif) {
    const map = {
        waves: { lbl: 'White & ochre earth pigments paint rhythmic wavy river bands!', t: 'Zigzag River Wave Bands', d: 'Indian potters wrap horizontal circles of crisp white chalk clay and yellow ochre slips into flowing zigzag river stripes while spinning the wheel slowly!' },
        leaves: { lbl: 'Symmetrical leaf bands honor swaying garden neem branches!', t: 'Repeating Neem Leaf Vines', d: 'Paired teardrop strokes tilted neatly on alternating sides imitate living compound leaves along earthen water jars across India.' },
        dots: { lbl: 'Clustered folk dots echo vibrant leopard rosettes & wild berries!', t: 'Traditional Folk Dot Chains', d: 'Fine bamboo brushes dab crisp symmetrical white and golden dot garlands evenly around rounded pot bellies.' },
        eyes: { lbl: 'Stylized peacock eye medallions celebrate colorful native birds!', t: 'Peacock Plume Medallions', d: 'Inspired by dazzling wild peacock feathers, nested oval halos bring radiant royal beauty onto everyday terracotta kitchenware!' }
    };
    const d = map[motif];
    if (!d) return;
    ['waves', 'leaves', 'dots', 'eyes'].forEach(k => {
        const b = document.getElementById('btn-pmot-' + k);
        if (b) {
            b.className = (k === motif)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('pmot-' + k + '-svg');
        if (g) {
            if (k === motif) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('pmot-svg-lbl').textContent = d.lbl;
    document.getElementById('pmot-title').textContent = d.t;
    document.getElementById('pmot-desc').textContent = d.d;
}
</script>
"""

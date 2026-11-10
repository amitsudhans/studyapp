#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 10: This World of Things
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Tapping Sound Orchestra (Activity 5 Acoustic WebAudio Lab)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔔</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Activity 5: Metal Spoon Tapping Acoustic Orchestra</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Sound Acoustics</span>
    </div>

    <p class="text-xs text-slate-300">Tap each material gently with a stainless steel spoon to hear its unique live acoustic vibration and examine sonority!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="tapOrchestra('metal')" id="btn-tap-metal" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🥣 Tap Steel Bowl</button>
        <button onclick="tapOrchestra('wood')" id="btn-tap-wood" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪵 Tap Wood Block</button>
        <button onclick="tapOrchestra('clay')" id="btn-tap-clay" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏺 Tap Clay Matka</button>
        <button onclick="tapOrchestra('glass')" id="btn-tap-glass" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥛 Tap Glass Cup</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-4xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="tap-emoji">🔔✨</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="tap-sound">Clear Lingering Chime: "TIIIING!" (Sonorous Metal)</h4>
            <p class="text-slate-300" id="tap-desc">Smooth elastic metal crystals vibrate cleanly for seconds—why school bells, wind chimes, and cymbals are forged out of brass or steel!</p>
        </div>
    </div>
</div>

<script>
function playMaterialNote(freq, dur, type) {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, now);
        gain.gain.setValueAtTime(0.22, now);
        gain.gain.exponentialRampToValueAtTime(0.005, now + dur);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + dur);
    } catch(e) {}
}

function tapOrchestra(mat) {
    const map = {
        metal: { f: 880, dur: 0.9, ty: 'sine', e: '🔔✨', s: 'Clear Lingering Chime: "TIIIING!" (Sonorous Metal)', d: 'Smooth elastic metal crystals vibrate cleanly for seconds—why school bells, wind chimes, and cymbals are forged out of brass or steel!' },
        wood: { f: 160, dur: 0.12, ty: 'triangle', e: '🪵🥁', s: 'Short Dull Knock: "THUD / TOK!" (Absorbs Vibration)', d: 'Porous wooden fibers stop vibration quickly with zero lingering echo—creating sharp crisp wooden blocks and tabla bases.' },
        clay: { f: 240, dur: 0.25, ty: 'sine', e: '🏺🎶', s: 'Deep Hollow Resonance: "TUM!" (Earthen Percussion)', d: 'An empty kiln-baked clay matka amplifies warm hollow bass thumps—just like classical Indian ghatam percussion pots!' },
        glass: { f: 1320, dur: 0.45, ty: 'sine', e: '🥛🎵', s: 'Delicate High Tinkle: "PING!" (Gentle Glass Resonance)', d: 'Tap ultra-softly! Crisp glass vibrates briefly at clear high musical frequencies without metallic clang.' }
    };
    const d = map[mat];
    if (!d) return;

    playMaterialNote(d.f, d.dur, d.ty);

    ['metal', 'wood', 'clay', 'glass'].forEach(k => {
        const b = document.getElementById('btn-tap-' + k);
        if (b) {
            b.className = (k === mat)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('tap-emoji').textContent = d.e;
    document.getElementById('tap-sound').textContent = d.s;
    document.getElementById('tap-desc').textContent = d.d;
}
</script>
"""

# Simulator 10: Stiff Or Bendable
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎗️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Rigidity vs Flexibility Engineering Comparator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Mechanics Lab</span>
    </div>

    <p class="text-xs text-slate-300">Test bending resistance across rigid structural materials versus soft flexible fabrics and elastic bands!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="setBendMode('rigid')" id="btn-bd-rigid" class="p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2">
            <span class="text-2xl">🪵</span>
            <div><span class="block">Rigid Materials (Wood, Iron, Stone)</span><span class="text-[10px] text-cyan-200">Supports Heavy Weight Straight</span></div>
        </button>
        <button onclick="setBendMode('flex')" id="btn-bd-flex" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-2xl">👕</span>
            <div><span class="block">Flexible Materials (Cloth, Rope, Rubber)</span><span class="text-[10px] text-slate-400">Folds &amp; Drapes Comfortably</span></div>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="bd-emoji">🪑🧱</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="bd-title">Rigid Stiffness: Safe Desks, Bridges &amp; Steps</h4>
            <p class="text-slate-300" id="bd-desc">Hard wood, stone, and steel resist bending under heavy books or walking feet—staying flat and sturdy without sagging!</p>
        </div>
    </div>
</div>

<script>
function setBendMode(m) {
    const isRig = (m === 'rigid');
    document.getElementById('btn-bd-rigid').className = isRig
        ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-bd-flex').className = !isRig
        ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    document.getElementById('bd-emoji').textContent = isRig ? '🪑🧱' : '👕🎗️';
    document.getElementById('bd-title').textContent = isRig
        ? 'Rigid Stiffness: Safe Desks, Bridges & Steps'
        : 'Soft Flexibility: Shirts, Curtains & Jumping Ropes';
    document.getElementById('bd-desc').textContent = isRig
        ? 'Hard wood, stone, and steel resist bending under heavy books or walking feet—staying flat and sturdy without sagging!'
        : 'Woven cotton cloth, soft wool, and elastic rubber bend easily around moving arms, fold neatly into bags, and hang in airy window curtains!';
}
</script>
"""

# Simulator 11: Spotting Odd Pairs
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🤪</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Wacky 'Odd Pairs' Material Mismatch Tester</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Logic Detective</span>
    </div>

    <p class="text-xs text-slate-300">Click each absurd 'Odd Pair' invention to watch WHY selecting the wrong material fails catastrophically!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="testOddPair('umbrella')" id="btn-odd-umbrella" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">☂️ Paper Umbrella</button>
        <button onclick="testOddPair('ball')" id="btn-odd-ball" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⚽ Glass Football</button>
        <button onclick="testOddPair('pan')" id="btn-odd-pan" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍳 Cloth Frying Pan</button>
        <button onclick="testOddPair('pillow')" id="btn-odd-pillow" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪨 Iron Pillow</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-rose-800/50 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="odd-emoji">🌧️📃❌</div>
        <div class="space-y-1">
            <h4 class="font-bold text-rose-300 text-sm" id="odd-title">Fail #1: Paper Umbrella Soaks &amp; Rips in Seconds!</h4>
            <p class="text-slate-300" id="odd-desc">Plain paper drinks up pouring rain instantly and collapses into mush! Real umbrellas need waterproof coated fabric over sturdy spokes.</p>
        </div>
    </div>
</div>

<script>
function testOddPair(p) {
    const map = {
        umbrella: { e: '🌧️📃❌', t: 'Fail #1: Paper Umbrella Soaks & Rips in Seconds!', d: 'Plain paper drinks up pouring rain instantly and collapses into mush! Real umbrellas need waterproof coated fabric over sturdy spokes.' },
        ball: { e: '🦵🔮💥', t: 'Fail #2: Glass Football Shatters Upon First Kick!', d: 'Brittle rigid glass explodes dangerously into sharp shards on impact—footballs need bouncy flexible leather or tough rubber!' },
        pan: { e: '🔥👕💨', t: 'Fail #3: Cotton Frying Pan Catches Stove Fire!', d: 'Flammable woven cloth leaks hot oil cleanly through weaves and bursts into flame—cooking pans demand fireproof conductive metal!' },
        pillow: { e: '😴🔩🤕', t: 'Fail #4: Solid Iron Pillow Hurts Tired Necks!', d: 'Hard unyielding iron offers zero soft comfort—pillows rely on fluffy compressible cotton fiber or feather cushions!' }
    };
    const d = map[p];
    if (!d) return;

    ['umbrella', 'ball', 'pan', 'pillow'].forEach(k => {
        const b = document.getElementById('btn-odd-' + k);
        if (b) {
            b.className = (k === p)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('odd-emoji').textContent = d.e;
    document.getElementById('odd-title').textContent = d.t;
    document.getElementById('odd-desc').textContent = d.d;
}
</script>
"""

# Simulator 12: Fixed Shape Solids
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧱</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Matter State #1: Solids Inside Different Containers</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Solids Lab</span>
    </div>

    <p class="text-xs text-slate-300">Drop a solid river stone into three different containers and observe whether its shape or locked particle rows change!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="placeSolid('bowl')" id="btn-sol-bowl" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🥣 Round Steel Bowl</button>
        <button onclick="placeSolid('jar')" id="btn-sol-jar" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🫙 Tall Narrow Jar</button>
        <button onclick="placeSolid('box')" id="btn-sol-box" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">📦 Wide Square Box</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-4xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="sol-emoji">🪨👉🥣</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="sol-title">Inside Round Bowl: Stone Keeps Exact Fixed Shape!</h4>
            <p class="text-slate-300" id="sol-desc">Tightly locked solid particles sit shoulder-to-shoulder without sliding—so stones, bricks, and wooden pencils never flatten to match curved bowl walls!</p>
        </div>
    </div>
</div>

<script>
function placeSolid(c) {
    const map = {
        bowl: { e: '🪨👉🥣', t: 'Inside Round Bowl: Stone Keeps Exact Fixed Shape!', d: 'Tightly locked solid particles sit shoulder-to-shoulder without sliding—so stones, bricks, and wooden pencils never flatten to match curved bowl walls!' },
        jar: { e: '🪨👉🫙', t: 'Inside Tall Jar: Stone Still Retains Same Edges & Volume!', d: 'Unlike pouring water, solid objects maintain definite firm edges and take up constant rigid space regardless of vessel height.' },
        box: { e: '🪨👉📦', t: 'Inside Square Box: Zero Bending or Stretching!', d: 'Whether placed on desks or inside square boxes, solids remain stubbornly fixed unless cut, hammered, or melted with extreme heat!' }
    };
    const d = map[c];
    if (!d) return;

    ['bowl', 'jar', 'box'].forEach(k => {
        const b = document.getElementById('btn-sol-' + k);
        if (b) {
            b.className = (k === c)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sol-emoji').textContent = d.e;
    document.getElementById('sol-title').textContent = d.t;
    document.getElementById('sol-desc').textContent = d.d;
}
</script>
"""

# Simulator 13: Flowing Pouring Liquids
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💧</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Matter State #2: Liquid Flow &amp; Volume Conservation Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Liquids Lab</span>
    </div>

    <p class="text-xs text-slate-300">Pour 200 mL of water, milk, or thick honey across three vessel shapes—watch shape transform while total volume holds constant!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="pourLiquid('tall')" id="btn-lq-tall" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🥛 Tall Drinking Glass</button>
        <button onclick="pourLiquid('pan')" id="btn-lq-pan" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍳 Wide Shallow Pan</button>
        <button onclick="pourLiquid('honey')" id="btn-lq-honey" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍯 Slow Thick Honey</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-4xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="lq-emoji">💧➡️🥛</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="lq-title">200 mL Inside Tall Glass: Takes Vertical Cylinder Form!</h4>
            <p class="text-slate-300" id="lq-desc">Liquid particles roll freely past neighbors, sliding down to fill narrow upright glass walls cleanly while keeping exact 200 mL volume!</p>
        </div>
    </div>
</div>

<script>
function pourLiquid(l) {
    const map = {
        tall: { e: '💧➡️🥛', t: '200 mL Inside Tall Glass: Takes Vertical Cylinder Form!', d: 'Liquid particles roll freely past neighbors, sliding down to fill narrow upright glass walls cleanly while keeping exact 200 mL volume!' },
        pan: { e: '💧➡️🍳', t: '200 mL Inside Wide Pan: Spreads Thin & Flat!', d: 'No fixed shape! Poured water levels smoothly flat across broad pans—remaining exactly 200 mL without vanishing or multiplying.' },
        honey: { e: '🍯➡️🥣', t: 'Golden Honey: Slower Flow, Still 100% Liquid!', d: 'Honey resists sliding more thickly (high viscosity) than speedy tap water, yet still pours cleanly and adopts whatever spoon or bowl holds it!' }
    };
    const d = map[l];
    if (!d) return;

    ['tall', 'pan', 'honey'].forEach(k => {
        const b = document.getElementById('btn-lq-' + k);
        if (b) {
            b.className = (k === l)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('lq-emoji').textContent = d.e;
    document.getElementById('lq-title').textContent = d.t;
    document.getElementById('lq-desc').textContent = d.d;
}
</script>
"""

# Simulator 14: Floating Filling Gases
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎈</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Matter State #3: Expanding Gases &amp; Balloon Air Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Gases Lab</span>
    </div>

    <p class="text-xs text-slate-300">Test invisible air gas inside inflated rubber tires, boiling kettle steam, and spreading room scents!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectGas('balloon')" id="btn-gs-balloon" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🎈 Inflate Balloon</button>
        <button onclick="inspectGas('steam')" id="btn-gs-steam" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🫖 Boiling Steam</button>
        <button onclick="inspectGas('aroma')" id="btn-gs-aroma" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌸 Spice Aroma</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="gs-emoji">🎈💨</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="gs-title">Air Inside Balloons &amp; Bike Tires Occupies Real Space!</h4>
            <p class="text-slate-300" id="gs-desc">Pumping invisible air stretches rubber walls firmly outward—proving gases are real matter pushing equally in every direction!</p>
        </div>
    </div>
</div>

<script>
function inspectGas(g) {
    const map = {
        balloon: { e: '🎈💨', t: 'Air Inside Balloons & Bike Tires Occupies Real Space!', d: 'Pumping invisible air stretches rubber walls firmly outward—proving gases are real matter pushing equally in every direction!' },
        steam: { e: '🫖☁️', t: 'Hot Kettle Steam Expands Upward Everywhere!', d: 'Liquid water heated to boiling transforms into lively invisible vapor gas spreading high across kitchen ceilings.' },
        aroma: { e: '🌸👃', t: 'Perfume & Spice Vapors Diffuse Across Entire Rooms!', d: 'Widely spaced gas molecules zoom swiftly through air in all directions—letting noses detect kitchen treats from distant rooms!' }
    };
    const d = map[g];
    if (!d) return;

    ['balloon', 'steam', 'aroma'].forEach(k => {
        const b = document.getElementById('btn-gs-' + k);
        if (b) {
            b.className = (k === g)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('gs-emoji').textContent = d.e;
    document.getElementById('gs-title').textContent = d.t;
    document.getElementById('gs-desc').textContent = d.d;
}
</script>
"""

# Simulator 15: Natural Versus Artificial
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌍</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Natural (Living/Non-Living) vs Artificial Creation Classifier</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Origin Sorting</span>
    </div>

    <p class="text-xs text-slate-300">Separate Earth's untouched natural creations (both alive and non-living!) from human-crafted manufactured objects!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectWorldClass('living')" id="btn-wc-living" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🥭 Natural Living</button>
        <button onclick="inspectWorldClass('nonliving')" id="btn-wc-nonliving" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪨 Natural Non-Living</button>
        <button onclick="inspectWorldClass('artificial')" id="btn-wc-artificial" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">👟 Artificial Craft</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="wc-emoji">🥭🐦</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="wc-title">Natural &amp; Alive: Mango Trees, Birds &amp; Earthworms</h4>
            <p class="text-slate-300" id="wc-desc">Grow, breathe, reproduce, and flourish naturally across forests and soils without any human factory crafting them!</p>
        </div>
    </div>
</div>

<script>
function inspectWorldClass(w) {
    const map = {
        living: { e: '🥭🐦', t: 'Natural & Alive: Mango Trees, Birds & Earthworms', d: 'Grow, breathe, reproduce, and flourish naturally across forests and soils without any human factory crafting them!' },
        nonliving: { e: '🪨💧', t: 'Natural & Non-Living: Rocks, River Water & Air', d: 'Notice carefully! Mountain rocks, sunshine, clouds, rain, and breathing air are completely NATURAL creations even though they are non-living!' },
        artificial: { e: '👟👕', t: 'Artificial (Human-Made): Shoes, Clothes & Tables', d: 'Skillfully stitched, sawed, or molded by people out of natural fibers, rubber, and wood—never sprouting ready-made on trees!' }
    };
    const d = map[w];
    if (!d) return;

    ['living', 'nonliving', 'artificial'].forEach(k => {
        const b = document.getElementById('btn-wc-' + k);
        if (b) {
            b.className = (k === w)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('wc-emoji').textContent = d.e;
    document.getElementById('wc-title').textContent = d.t;
    document.getElementById('wc-desc').textContent = d.d;
}
</script>
"""

# Simulator 16: Material Review Match (Complete Synthesis Matching Workbench)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Chapter 10 Master Review: Complete Matching Workbench</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Master Synthesis</span>
    </div>

    <p class="text-xs text-slate-300">Verify your complete Chapter 10 scientific mastery by inspecting all four combined review categories on one breakfast table!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectReview('optics')" id="btn-rv-optics" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">👓 Light Match</button>
        <button onclick="inspectReview('matter')" id="btn-rv-matter" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">💧 3 States Match</button>
        <button onclick="inspectReview('sense')" id="btn-rv-sense" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🔔 Sense &amp; Tap</button>
        <button onclick="inspectReview('origin')" id="btn-rv-origin" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌍 Source Match</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-amber-800/50 text-xs space-y-2">
        <h4 class="font-bold text-amber-300 text-sm" id="rv-title">Optics Summary: Transparent vs Translucent vs Opaque</h4>
        <p class="text-slate-300 leading-relaxed" id="rv-desc">
            Clear window glass (Transparent: sharp sunlight), thin paper lampshade (Translucent: gentle glow), and solid oak shutters (Opaque: blocks light cleanly casting crisp shadows)!
        </p>
    </div>
</div>

<script>
function inspectReview(rv) {
    const map = {
        optics: { t: 'Optics Summary: Transparent vs Translucent vs Opaque', d: 'Clear window glass (Transparent: sharp sunlight), thin paper lampshade (Translucent: gentle glow), and solid oak shutters (Opaque: blocks light cleanly casting crisp shadows)!' },
        matter: { t: 'States of Matter: Steel Spoon (Solid) + Milk (Liquid) + Steam (Gas)', d: 'Solid spoons keep fixed shape; pouring liquid milk matches round cups cleanly; hot rising steam expands freely as invisible gas!' },
        sense: { t: 'Sensory Properties: Cold Shiny Sonorous Steel vs Warm Dull Wood', d: 'Steel conducts finger warmth fast (feels cold) and sings "TIIIING!" when tapped—wood insulates gently and gives a short crisp "THUD!"' },
        origin: { t: 'Origins: Natural Living/Non-Living vs Human-Crafted Artificial Objects', d: 'Glass melts from sand, metal smelts from rock ores, rubber flows from tree latex, and smart reuse honors Earth\\'s natural sources!' }
    };
    const d = map[rv];
    if (!d) return;

    ['optics', 'matter', 'sense', 'origin'].forEach(k => {
        const b = document.getElementById('btn-rv-' + k);
        if (b) {
            b.className = (k === rv)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('rv-title').textContent = d.t;
    document.getElementById('rv-desc').textContent = d.d;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part2)} simulators for Part 2 (9 to 16).")
    for k in sorted(simulators_part2.keys()):
        print(f"Sim {k}: {len(simulators_part2[k])} chars")

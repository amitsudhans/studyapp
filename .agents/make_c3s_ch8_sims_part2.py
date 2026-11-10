#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 8: Food We Eat
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Juicy Orchard Fruits
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥭</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Orchard Fruit Basket &amp; Seed Chamber Explorer</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Plant Parts #2</span>
    </div>

    <p class="text-xs text-slate-300">Click orchard harvests to discover hidden vitamins inside each juicy fruit—plus one surprising savory kitchen fruit!</p>

    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
        <button onclick="inspectFruit('guava')" id="btn-fr-guava" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🍐 Guava</button>
        <button onclick="inspectFruit('sapota')" id="btn-fr-sapota" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥔 Sapota</button>
        <button onclick="inspectFruit('apple')" id="btn-fr-apple" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍎 Apple</button>
        <button onclick="inspectFruit('mango')" id="btn-fr-mango" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥭 Mango</button>
        <button onclick="inspectFruit('tomato')" id="btn-fr-tomato" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍅 Surprise Fruit</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="fr-emoji">🍐</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="fr-title">Crisp Emerald Guava (Amrood) — Vitamin C Powerhouse</h4>
            <p class="text-slate-300" id="fr-desc">Contains even more immune-boosting vitamin C per bite than oranges! Wash outside skin cleanly so you enjoy crisp edible fiber and tiny crunchy seeds safely.</p>
        </div>
    </div>
</div>

<script>
function inspectFruit(f) {
    const map = {
        guava: { e: '🍐', t: 'Crisp Emerald Guava (Amrood) — Vitamin C Powerhouse', d: 'Contains even more immune-boosting vitamin C per bite than oranges! Wash outside skin cleanly so you enjoy crisp edible fiber and tiny crunchy seeds safely.' },
        sapota: { e: '🥔', t: 'Sweet Velvety Sapota (Chikoo) — Quick Fruit Energy', d: 'Sandy-brown tropical fruit packed with natural caramel fruit sweetness, potassium, and glossy black seeds inside soft pulp.' },
        apple: { e: '🍎', t: 'Crunchy Mountain Apple — Pectin Fiber Gem', d: 'Grown in cool mountain valleys, apples nourish gut health with natural pectin fiber and clean vitamins right underneath crisp red skin.' },
        mango: { e: '🥭', t: 'Golden Summer Mango — Eye-Brightening Vitamin A', d: 'Celebrated across India as the King of Fruits, golden mango pulp brims with natural carotenoids protecting bright vision and youthful skin.' },
        tomato: { e: '🍅', t: 'Botanical Surprise: Tomato, Cucumber & Brinjals Are Fruits!', d: 'Though cooked in savory curries, tomatoes and cucumbers grow from blossoms and carry seeds inside—making them true plant fruits scientifically!' }
    };
    const d = map[f];
    if (!d) return;

    ['guava', 'sapota', 'apple', 'mango', 'tomato'].forEach(k => {
        const b = document.getElementById('btn-fr-' + k);
        if (b) {
            b.className = (k === f)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('fr-emoji').textContent = d.e;
    document.getElementById('fr-title').textContent = d.t;
    document.getElementById('fr-desc').textContent = d.d;
}
</script>
"""

# Simulator 10: Underground Plant Roots
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥕</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Soil Cross-Section: Swollen Edible Taproots</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Plant Parts #3</span>
    </div>

    <p class="text-xs text-slate-300">Inspect swollen taproots underground storing dense starches and vitamins—spot the fine lateral root hairs along every side!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectRoot('carrot')" id="btn-rt-carrot" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🥕 Orange Carrot</button>
        <button onclick="inspectRoot('radish')" id="btn-rt-radish" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥗 White Radish (Mooli)</button>
        <button onclick="inspectRoot('beetroot')" id="btn-rt-beetroot" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🟣 Ruby Beetroot</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 200" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="0" y="0" width="320" height="55" fill="#0f172a" />
            <rect x="0" y="55" width="320" height="145" fill="#451a03" />
            <line x1="0" y1="55" x2="320" y2="55" stroke="#16a34a" stroke-width="3" />
            <!-- Green Feathery Tops -->
            <path d="M 160 55 Q 130 15 110 25 M 160 55 Q 160 10 165 18 M 160 55 Q 190 15 210 25" stroke="#22c55e" stroke-width="4" fill="none" stroke-linecap="round" />
            <!-- Main Taproot Body -->
            <polygon id="root-shape-poly" points="135,55 185,55 160,175" fill="#f97316" stroke="#ea580c" stroke-width="2" />
            <!-- Lateral Root Hairs -->
            <line x1="145" y1="95" x2="115" y2="105" stroke="#fdba74" stroke-width="1.5" />
            <line x1="175" y1="115" x2="205" y2="128" stroke="#fdba74" stroke-width="1.5" />
            <line x1="152" y1="145" x2="125" y2="155" stroke="#fdba74" stroke-width="1.5" />
            <text x="160" y="190" fill="#fed7aa" font-size="10" text-anchor="middle">Tiny side rootlets prove it is a true Taproot!</text>
        </svg>

        <div class="space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="rt-title">Orange &amp; Ruby Carrots — Vitamin A Eyesight Booster</h4>
            <p class="text-slate-300 leading-relaxed" id="rt-desc">Carrots store bright orange beta-carotene sugars deep beneath winter soil. Eating crisp scrubbed carrots strengthens keen eyes for reading and evening vision!</p>
        </div>
    </div>
</div>

<script>
function inspectRoot(rt) {
    const map = {
        carrot: { pts: '135,55 185,55 160,175', fill: '#f97316', stroke: '#ea580c', t: 'Orange & Ruby Carrots — Vitamin A Eyesight Booster', d: 'Carrots store bright orange beta-carotene sugars deep beneath winter soil. Eating crisp scrubbed carrots strengthens keen eyes for reading and evening vision!' },
        radish: { pts: '138,55 182,55 160,175', fill: '#f8fafc', stroke: '#cbd5e1', t: 'Peppery White Radish (Mooli) — Cool Digestive Fiber', d: 'Long crisp white taproots packed with cooling water and tangy digestive enzymes—enjoyed raw in winter salads or cooked with tender leafy tops.' },
        beetroot: { pts: '122,70 198,70 160,145', fill: '#be123c', stroke: '#9f1239', t: 'Crimson Beetroot (Chukandar) — Blood Iron & Folate', d: 'Deep magenta globe-shaped taproot rich in natural iron, folate, and mineral energy supporting bright red blood cells in active runners!' }
    };
    const d = map[rt];
    if (!d) return;

    ['carrot', 'radish', 'beetroot'].forEach(k => {
        const b = document.getElementById('btn-rt-' + k);
        if (b) {
            b.className = (k === rt)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const poly = document.getElementById('root-shape-poly');
    poly.setAttribute('points', d.pts);
    poly.setAttribute('fill', d.fill);
    poly.setAttribute('stroke', d.stroke);
    document.getElementById('rt-title').textContent = d.t;
    document.getElementById('rt-desc').textContent = d.d;
}
</script>
"""

# Simulator 11: Edible Plant Stems
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥔</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Botanical Detective: Proof of Edible Stems</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Plant Parts #4</span>
    </div>

    <p class="text-xs text-slate-300">Why aren't potatoes, ginger, and onions considered plant roots? Click each stem specimen to spot its telltale botanical stem clues!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectStem('potato')" id="btn-st-potato" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🥔 Potato Tuber</button>
        <button onclick="inspectStem('ginger')" id="btn-st-ginger" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🫚 Ginger Rhizome</button>
        <button onclick="inspectStem('onion')" id="btn-st-onion" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧅 Onion Bulb</button>
        <button onclick="inspectStem('bamboo')" id="btn-st-bamboo" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🎍 Bamboo Shoots</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="st-emoji">🥔🌱</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="st-title">Potato — Swollen Underground Stem Tuber With 'Eyes'</h4>
            <p class="text-slate-300" id="st-desc">Inspect those sunken little 'eyes' on a warm pantry potato: tiny green stems and leaves sprout directly from them! True roots never possess stem buds or nodes.</p>
        </div>
    </div>
</div>

<script>
function inspectStem(st) {
    const map = {
        potato: { e: '🥔🌱', t: 'Potato — Swollen Underground Stem Tuber With "Eyes"', d: 'Inspect those sunken little "eyes" on a warm pantry potato: tiny green stems and leaves sprout directly from them! True roots never possess stem buds or nodes.' },
        ginger: { e: '🫚🌿', t: 'Ginger — Horizontal Underground Stem (Rhizome)', d: 'Notice clear horizontal ring lines (nodes) and papery scale-leaf edges encircling spicy golden ginger—unmistakable anatomy of a horizontal creeping stem!' },
        onion: { e: '🧅⭕', t: 'Onion — Compressed Underground Stem Bulb', d: 'Cut an onion vertically to spot the tough small flat disc stem at its bottom base holding tightly stacked fleshy food-storing leaf bases!' },
        bamboo: { e: '🎍🍲', t: 'Tender Bamboo Shoots — Aboveground Crunchy Grass Stalk', d: 'In Assam and Northeast India, young hollow segmented stems of giant bamboo grasses are sliced into delicious curries and aromatic pickles!' }
    };
    const d = map[st];
    if (!d) return;

    ['potato', 'ginger', 'onion', 'bamboo'].forEach(k => {
        const b = document.getElementById('btn-st-' + k);
        if (b) {
            b.className = (k === st)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('st-emoji').textContent = d.e;
    document.getElementById('st-title').textContent = d.t;
    document.getElementById('st-desc').textContent = d.d;
}
</script>
"""

# Simulator 12: Grains And Seeds
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌾</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Farm Granary: Grains, Pulses &amp; Nuts (Edible Seeds)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Plant Parts #5</span>
    </div>

    <p class="text-xs text-slate-300">Open all three kitchen storage jars containing nutritious plant seeds powering energy, muscle repair, and brain focus!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="openSeedJar('grains')" id="btn-sd-grains" class="p-3 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left">
            <span class="block">1. Cereal Grains</span>
            <span class="text-[10px] text-amber-200">Wheat, Rice, Bajra, Ragi</span>
        </button>
        <button onclick="openSeedJar('pulses')" id="btn-sd-pulses" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">2. Protein Pulses</span>
            <span class="text-[10px] text-slate-400">Moong, Toor, Chana, Rajma</span>
        </button>
        <button onclick="openSeedJar('nuts')" id="btn-sd-nuts" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">3. Dry Fruits &amp; Nuts</span>
            <span class="text-[10px] text-slate-400">Almonds, Walnuts, Cashews</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="sd-emoji">🌾🫓</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="sd-title">Cereal Grain Seeds — Daily Fuel Carbohydrates</h4>
            <p class="text-slate-300" id="sd-desc">Ground into soft chapati atta or steamed into fluffy rice, grain seeds store dense natural starch meant to nourish baby plant sprouts—fueling every active game and study hour!</p>
        </div>
    </div>
</div>

<script>
function openSeedJar(jar) {
    const map = {
        grains: { e: '🌾🫓', t: 'Cereal Grain Seeds — Daily Fuel Carbohydrates', d: 'Ground into soft chapati atta or steamed into fluffy rice, grain seeds store dense natural starch meant to nourish baby plant sprouts—fueling every active game and study hour!' },
        pulses: { e: '🫘🍲', t: 'Legume Pulse Seeds — Vegetarian Muscle Builders', d: 'Golden toor dal, green moong, chickpeas, and kidney beans carry packed plant proteins indispensable for growing height, repairing tissues, and energizing vegetarians.' },
        nuts: { e: '🥜🧠', t: 'Tree Nuts & Dry Fruits — Healthy Oils & Minerals', d: 'Crunchy almonds, brain-shaped walnuts, cashews, and sesame seeds store healthy fats, vitamin E, and trace minerals supporting focused memory and winter warmth.' }
    };
    const d = map[jar];
    if (!d) return;

    ['grains', 'pulses', 'nuts'].forEach(k => {
        const b = document.getElementById('btn-sd-' + k);
        if (b) {
            b.className = (k === jar)
                ? 'p-3 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
        }
    });
    document.getElementById('sd-emoji').textContent = d.e;
    document.getElementById('sd-title').textContent = d.t;
    document.getElementById('sd-desc').textContent = d.d;
}
</script>
"""

# Simulator 13: Dairy And Honey (Animal Milk Transformations & Honey)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥛</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Dairy Kitchen Transformer &amp; Golden Honey Hive</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Animal Foods #1</span>
    </div>

    <p class="text-xs text-slate-300">Explore how kitchen science turns liquid milk into curd, ghee, cheese, and paneer—plus how worker bees craft sweet honey!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectDairyItem('curd')" id="btn-dy-curd" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🥣 Creamy Curd</button>
        <button onclick="selectDairyItem('ghee')" id="btn-dy-ghee" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧈 Butter &amp; Ghee</button>
        <button onclick="selectDairyItem('paneer')" id="btn-dy-paneer" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧀 Paneer / Cheese</button>
        <button onclick="selectDairyItem('honey')" id="btn-dy-honey" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍯 Bee Honey</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="dy-emoji">🥛➡️🥣</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="dy-title">Warm Milk + Helpful Bacteria &rarr; Probiotic Curd (Dahi)</h4>
            <p class="text-slate-300" id="dy-desc">Stirring one tiny spoon of starter curd into lukewarm milk introduces friendly lactobacillus bacteria that set creamy, tangy gut-healthy yogurt overnight!</p>
        </div>
    </div>
</div>

<script>
function selectDairyItem(dy) {
    const map = {
        curd: { e: '🥛➡️🥣', t: 'Warm Milk + Helpful Bacteria → Probiotic Curd (Dahi)', d: 'Stirring one tiny spoon of starter curd into lukewarm milk introduces friendly lactobacillus bacteria that set creamy, tangy gut-healthy yogurt overnight!' },
        ghee: { e: '🥛➡️🧈', t: 'Churned Milk Cream → Butter & Fragrant Ghee', d: 'Churning cool cream collects smooth golden butter fats; simmering butter slowly clears moisture to craft aromatic clarified ghee.' },
        paneer: { e: '🍋➡️🧀', t: 'Hot Milk + Tart Lemon Juice → Soft Protein Paneer', d: 'Adding tangy lemon juice into boiling milk gently separates solid protein curds—pressed softly into fresh white paneer cubes or aged cheeses!' },
        honey: { e: '🐝➡️🍯', t: 'Flower Nectar + Fanning Wings → Pure Golden Honey', d: 'Busy honeybees sip floral nectar across garden blooms and fan excess water away inside wax honeycombs to produce rich natural energy honey.' }
    };
    const d = map[dy];
    if (!d) return;

    ['curd', 'ghee', 'paneer', 'honey'].forEach(k => {
        const b = document.getElementById('btn-dy-' + k);
        if (b) {
            b.className = (k === dy)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('dy-emoji').textContent = d.e;
    document.getElementById('dy-title').textContent = d.t;
    document.getElementById('dy-desc').textContent = d.d;
}
</script>
"""

# Simulator 14: Eggs Meat Minerals (Non-Plant, Non-Animal Essentials)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧂</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Animal Proteins &amp; Earth's Non-Biological Essentials</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Riddle Solver</span>
    </div>

    <p class="text-xs text-slate-300">Inspect protein-rich eggs and fish alongside the ONLY two kitchen cooking essentials that come neither from plants nor from animals!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectOrigin('animal')" id="btn-org-animal" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🥚 Eggs, Fish &amp; Meat</button>
        <button onclick="inspectOrigin('salt')" id="btn-org-salt" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧂 Natural Earth Salt</button>
        <button onclick="inspectOrigin('water')" id="btn-org-water" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">💧 Fresh Cooking Water</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="org-emoji">🥚🐟</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="org-title">Animal Source: Protein-Dense Eggs, Fish &amp; Meats</h4>
            <p class="text-slate-300" id="org-desc">Eggs, fish, and poultry furnish concentrated complete proteins and vitamin B12—while vegetarian families thrive richly combining pulses, milk, paneer, and nuts!</p>
        </div>
    </div>
</div>

<script>
function inspectOrigin(org) {
    const map = {
        animal: { e: '🥚🐟', t: 'Animal Source: Protein-Dense Eggs, Fish & Meats', d: 'Eggs, fish, and poultry furnish concentrated complete proteins and vitamin B12—while vegetarian families thrive richly combining pulses, milk, paneer, and nuts!' },
        salt: { e: '🧂🌊', t: 'Neither Plant Nor Animal: Natural Earth Mineral Salt!', d: 'Harvested by solar evaporation inside sparkling coastal seawater pans or mined as pink rock salt—vital mineral salt flavors almost every cooked dish worldwide!' },
        water: { e: '💧🌍', t: 'Neither Plant Nor Animal: Pure Natural Water!', d: 'Collected from rain-fed wells, streams, and rivers, liquid water boils rice, simmers lentil dals, washes fresh greens, and hydrates every living cell!' }
    };
    const d = map[org];
    if (!d) return;

    ['animal', 'salt', 'water'].forEach(k => {
        const b = document.getElementById('btn-org-' + k);
        if (b) {
            b.className = (k === org)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('org-emoji').textContent = d.e;
    document.getElementById('org-title').textContent = d.t;
    document.getElementById('org-desc').textContent = d.d;
}
</script>
"""

# Simulator 15: Kindly Sharing Meals (Zero Waste & Gratitude)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🤝</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Zero Plate Waste &amp; Lunch Sharing Simulator</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Farmer Gratitude</span>
    </div>

    <p class="text-xs text-slate-300">Choose how you serve and share your school lunch to see its effect on farmers' hard harvest work and classroom friendship!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="testPlateHabit('waste')" id="btn-pl-waste" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">Option A: Heap Huge Mountain &amp; Toss Half</span>
            <span class="text-[10px] text-rose-400">Careless Over-Serving</span>
        </button>
        <button onclick="testPlateHabit('smart')" id="btn-pl-smart" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left shadow">
            <span class="block">Option B: Modest Portion + Share Kindness</span>
            <span class="text-[10px] text-emerald-200">Zero Waste Habit</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="pl-emoji">✨🍛</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="pl-title">0% Food Wasted — Proud Respect for Farmers!</h4>
            <p class="text-slate-300" id="pl-desc">Serving modest amounts first ensures every cooked grain is enjoyed cleanly, honoring months of farmer sweat and irrigation water while brightening a friend's recess!</p>
        </div>
    </div>
</div>

<script>
function testPlateHabit(h) {
    const isSmart = (h === 'smart');
    document.getElementById('btn-pl-smart').className = isSmart
        ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left shadow'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
    document.getElementById('btn-pl-waste').className = !isSmart
        ? 'p-3 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500 text-left shadow'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';

    document.getElementById('pl-emoji').textContent = isSmart ? '✨🍛' : '🗑️😔';
    document.getElementById('pl-title').textContent = isSmart
        ? '0% Food Wasted — Proud Respect for Farmers!'
        : '50% Wasted in Dustbins — Precious Harvest Lost!';
    document.getElementById('pl-title').className = isSmart ? 'font-bold text-emerald-300 text-sm' : 'font-bold text-rose-400 text-sm';
    document.getElementById('pl-desc').textContent = isSmart
        ? 'Serving modest amounts first ensures every cooked grain is enjoyed cleanly, honoring months of farmer sweat and irrigation water while brightening a friend\\'s recess!'
        : 'Dumping half-eaten rice and rotis wastes the water, sunshine, soil nutrients, and tireless labor farmers poured into growing that crop!';
}
</script>
"""

# Simulator 16: Making Fruit Chaat (4-Step Culinary Review Workbench)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥗</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Class Fruit Chaat Four-Step Recipe Workbench</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Chapter Finale Activity</span>
    </div>

    <p class="text-xs text-slate-300">Complete all four classroom steps in sequence to craft a safe, colorful, vitamin-packed rainbow Fruit Chaat together!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setChaatStep(1)" id="btn-ch-1" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">1. Scrub &amp; Rinse</button>
        <button onclick="setChaatStep(2)" id="btn-ch-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Safe Dicing</button>
        <button onclick="setChaatStep(3)" id="btn-ch-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Lemon &amp; Masala</button>
        <button onclick="setChaatStep(4)" id="btn-ch-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Share Bowls</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Stainless Steel Mixing Bowl -->
            <path d="M 230 95 Q 350 185 470 95 Z" fill="#64748b" stroke="#cbd5e1" stroke-width="3" />
            <ellipse cx="350" cy="95" rx="120" ry="18" fill="#1e293b" stroke="#94a3b8" stroke-width="2" />

            <!-- Rainbow Fruits inside Bowl -->
            <text x="275" y="96" font-size="24">🍎</text>
            <text x="315" y="92" font-size="24">🍌</text>
            <text x="355" y="97" font-size="24">🍐</text>
            <text x="395" y="93" font-size="24">🍊</text>

            <!-- Active Step Visual Badge -->
            <text id="chaat-step-icon" x="350" y="55" font-size="30" text-anchor="middle">🧼💧</text>
            <text id="chaat-svg-caption" x="350" y="165" fill="#4ade80" font-size="12" font-weight="bold" text-anchor="middle">Step 1: Wash Hands with Soap &amp; Rinse Fresh Fruits Cleanly</text>
        </svg>
    </div>

    <div class="bg-slate-950 p-3.5 rounded-xl border border-emerald-800/60 text-xs">
        <p id="chaat-step-desc" class="text-slate-200">
            <strong class="text-emerald-300">Clean Hygiene First:</strong> Because fruit chaat is enjoyed fresh and uncooked, scrubbing hands thoroughly and rinsing whole apples, guavas, and oranges in clean water prevents invisible farm dust and germs!
        </p>
    </div>
</div>

<script>
function setChaatStep(step) {
    const steps = {
        1: { icon: '🧼💧', cap: 'Step 1: Wash Hands with Soap & Rinse Fresh Fruits Cleanly', desc: '<strong class="text-emerald-300">Clean Hygiene First:</strong> Because fruit chaat is enjoyed fresh and uncooked, scrubbing hands thoroughly and rinsing whole apples, guavas, and oranges in clean water prevents invisible farm dust and germs!' },
        2: { icon: '🔪🧑‍🏫', cap: 'Step 2: Teachers Safely Dice Fruits Into Colorful Cubes', desc: '<strong class="text-amber-300">Kitchen Safety Rule:</strong> Supervising adults or teachers slice washed guavas, apples, and bananas neatly into bite-sized pieces inside a sparkling steel mixing bowl.' },
        3: { icon: '🍋🧂', cap: 'Step 3: Squeeze Fresh Lemon + Sprinkle Cumin & Black Salt', desc: '<strong class="text-cyan-300">Flavor & Freshness Science:</strong> Tangy vitamin C lemon juice prevents cut apple cubes from turning brown while roasted cumin and mild black salt blend sour, sweet, salty, and gentle spice harmoniously!' },
        4: { icon: '🥗🤝', cap: 'Step 4: Scoop Rainbow Sharing Bowls Across the Class!', desc: '<strong class="text-emerald-300">Joyful Community Feast:</strong> Every student enjoys colorful protective vitamins together—celebrating healthy balanced eating with zero food waste!' }
    };
    const s = steps[step];
    if (!s) return;

    for (let i = 1; i <= 4; i++) {
        const b = document.getElementById('btn-ch-' + i);
        if (b) {
            b.className = (i === step)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    }
    document.getElementById('chaat-step-icon').textContent = s.icon;
    document.getElementById('chaat-svg-caption').textContent = s.cap;
    document.getElementById('chaat-step-desc').innerHTML = s.desc;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part2)} simulators for Part 2 (9 to 16).")
    for k in sorted(simulators_part2.keys()):
        print(f"Sim {k}: {len(simulators_part2[k])} chars")

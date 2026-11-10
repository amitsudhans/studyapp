#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 8: Food We Eat
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Wholesome Homemade Dishes
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍲</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Home Kitchen vs Factory Packet Inspector</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Wholesome Nutrition</span>
    </div>

    <p class="text-xs text-slate-300">Compare freshly cooked homemade dishes against packaged factory junk snacks to inspect ingredients and cleanliness!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectHomeDish('dalroti')" id="btn-dish-dalroti" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left flex items-center gap-2">
            <span class="text-xl">🍛</span><span>Dal, Roti &amp; Greens</span>
        </button>
        <button onclick="inspectHomeDish('dosa')" id="btn-dish-dosa" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🥞</span><span>Idli / Dosa Meal</span>
        </button>
        <button onclick="inspectHomeDish('kheer')" id="btn-dish-kheer" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🥣</span><span>Nutty Milk Kheer</span>
        </button>
        <button onclick="inspectHomeDish('chips')" id="btn-dish-chips" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🍟</span><span>Factory Packet Chips</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center text-xs">
        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 text-center space-y-2">
            <div class="text-5xl" id="dish-emoji">🍛🥬</div>
            <h4 class="font-bold text-amber-300 text-sm" id="dish-name">Steaming Dal, Whole Wheat Roti &amp; Spinach</h4>
            <span class="inline-block px-2.5 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-bold" id="dish-badge">Fresh Homemade Kitchen Pot ✓</span>
        </div>
        <div class="space-y-2">
            <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                <span class="text-slate-400 text-[10px] uppercase block">Ingredients Inside:</span>
                <p id="dish-ingred" class="text-slate-200 mt-0.5 font-medium">Washed lentils, whole wheat flour, fresh spinach leaves, mild turmeric, cumin, and zero preservatives.</p>
            </div>
            <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                <span class="text-slate-400 text-[10px] uppercase block">Body Impact:</span>
                <p id="dish-impact" class="text-emerald-300 mt-0.5 font-semibold">Delivers clean steady energy, protein strength, and sharp focus for studies and sports!</p>
            </div>
        </div>
    </div>
</div>

<script>
function inspectHomeDish(dish) {
    const map = {
        dalroti: { e: '🍛🥬', n: 'Steaming Dal, Whole Wheat Roti & Spinach', b: 'Fresh Homemade Kitchen Pot ✓', ing: 'Washed lentils, whole wheat flour, fresh spinach leaves, mild turmeric, cumin, and zero preservatives.', imp: 'Delivers clean steady energy, protein strength, and sharp focus for studies and sports!', cls: 'inline-block px-2.5 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-bold' },
        dosa: { e: '🥞🥥', n: 'Crispy Dosa / Steamed Idli & Chutney', b: 'Naturally Fermented Home Meal ✓', ing: 'Fermented rice-and-urad lentil batter cooked light with fresh ground coconut and sambar lentils.', imp: 'Probiotic fermentation makes digestion effortless while supplying light energy!', cls: 'inline-block px-2.5 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-bold' },
        kheer: { e: '🥣🌰', n: 'Warm Homemade Milk & Almond Kheer', b: 'Calcium-Rich Home Dessert ✓', ing: 'Simmered cow milk, fragrant rice grains, gentle cardamom, jaggery or minimal sugar, and crushed almonds.', imp: 'Strengthens bones and teeth naturally without artificial food dyes or thick corn syrup.', cls: 'inline-block px-2.5 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-bold' },
        chips: { e: '🍟⚠️', n: 'Packaged Crinkly Factory Chips', b: 'Ultra-Processed Junk Snack ⚠️', ing: 'Excess sodium salt, repeated heated factory frying oil, artificial flavor enhancers, and shelf preservatives.', imp: 'Satisfies tongue cravings briefly yet causes thirst, sluggishness, and lacks vitamins or protein!', cls: 'inline-block px-2.5 py-0.5 rounded-full bg-rose-950 text-rose-300 border border-rose-800 text-[10px] font-bold' }
    };
    const d = map[dish];
    if (!d) return;

    ['dalroti', 'dosa', 'kheer', 'chips'].forEach(k => {
        const b = document.getElementById('btn-dish-' + k);
        if (b) {
            b.className = (k === dish)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
        }
    });
    document.getElementById('dish-emoji').textContent = d.e;
    document.getElementById('dish-name').textContent = d.n;
    document.getElementById('dish-badge').textContent = d.b;
    document.getElementById('dish-badge').className = d.cls;
    document.getElementById('dish-ingred').textContent = d.ing;
    document.getElementById('dish-impact').textContent = d.imp;
}
</script>
"""

# Simulator 2: Six Culinary Tastes (Chhappan Bhog Taste Explorer)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">👅</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Chhappan Bhog: Six-Taste Flavor Wheel</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Shad-Rasa Culinary Art</span>
    </div>

    <p class="text-xs text-slate-300">Explore all six distinct tastes celebrated inside traditional Chhappan Bhog spreads and discover how each helps the body!</p>

    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
        <button onclick="selectTaste('sweet')" id="btn-taste-sweet" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🍯 Sweet</button>
        <button onclick="selectTaste('sour')" id="btn-taste-sour" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍋 Sour</button>
        <button onclick="selectTaste('salty')" id="btn-taste-salty" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧂 Salty</button>
        <button onclick="selectTaste('spicy')" id="btn-taste-spicy" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌶️ Spicy</button>
        <button onclick="selectTaste('bitter')" id="btn-taste-bitter" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥬 Bitter</button>
        <button onclick="selectTaste('astringent')" id="btn-taste-astringent" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍏 Astringent</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-3 gap-4 items-center text-xs">
        <div class="text-center p-4 bg-slate-900 rounded-xl border border-slate-800">
            <div class="text-5xl mb-2" id="taste-emoji">🍯🥭</div>
            <div class="font-bold text-amber-300 text-sm" id="taste-name">Sweet (Madhura)</div>
        </div>
        <div class="md:col-span-2 space-y-2">
            <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                <span class="text-cyan-400 font-bold block text-[10px] uppercase">Natural Food Examples:</span>
                <p id="taste-foods" class="text-slate-200 mt-0.5">Ripe mangoes, jaggery (gur), pure golden honey, dates, ripe bananas, and warm milk.</p>
            </div>
            <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                <span class="text-emerald-400 font-bold block text-[10px] uppercase">Healthy Role in Moderation:</span>
                <p id="taste-role" class="text-slate-200 mt-0.5">Provides swift cellular energy and comforts tired tissues—when enjoyed naturally rather than refined white candy!</p>
            </div>
        </div>
    </div>
</div>

<script>
function selectTaste(t) {
    const map = {
        sweet: { e: '🍯🥭', n: 'Sweet (Madhura)', f: 'Ripe mangoes, jaggery (gur), pure golden honey, dates, ripe bananas, and warm milk.', r: 'Provides swift cellular energy and comforts tired tissues—when enjoyed naturally rather than refined white candy!' },
        sour: { e: '🍋🍊', n: 'Sour (Amla)', f: 'Fresh yellow lemons, raw green mangoes, tangy tamarind, tomatoes, and homemade yogurt.', r: 'Sparks joyful appetite, delivers antioxidant vitamin C, and aids smooth mineral absorption!' },
        salty: { e: '🧂🌊', n: 'Salty (Lavana)', f: 'Sea salt crystals, pink Himalayan rock salt, and mild pickled preserves.', r: 'Helps retain needed water balance and supports clear nerve signaling—when used lightly rather than excess!' },
        spicy: { e: '🌶️🫚', n: 'Spicy / Pungent (Katu)', f: 'Crushed black pepper, fresh ginger rhizome, aromatic cloves, garlic, and green chilies.', r: 'Warms chilly digestion, clears stuffy winter noses, and enhances delicious dish aromas!' },
        bitter: { e: '🥒🌿', n: 'Bitter (Tikta)', f: 'Bitter gourd (karela), fenugreek (methi) leaves and seeds, turmeric, and tender neem buds.', r: 'Cleanses blood impurities, sharpens balanced digestion, and guards against seasonal sluggishness!' },
        astringent: { e: '🍏🫖', n: 'Astringent (Kashaya)', f: 'Raw Indian gooseberry (amla), pomegranate rind tea, unripe green bananas, and split chickpeas.', r: 'Tightens delicate gum tissues mildly and balances rich oily dishes inside traditional Chhappan Bhog platters!' }
    };
    const d = map[t];
    if (!d) return;

    ['sweet', 'sour', 'salty', 'spicy', 'bitter', 'astringent'].forEach(k => {
        const b = document.getElementById('btn-taste-' + k);
        if (b) {
            b.className = (k === t)
                ? 'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('taste-emoji').textContent = d.e;
    document.getElementById('taste-name').textContent = d.n;
    document.getElementById('taste-foods').textContent = d.f;
    document.getElementById('taste-role').textContent = d.r;
}
</script>
"""

# Simulator 3: The Runner's Diet (Track Sprinter Performance Simulator)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏃</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Class 3 Sprinter Nutrition &amp; Stamina Race Lab</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Runner's Story</span>
    </div>

    <p class="text-xs text-slate-300">Compare the young runner's track speed, leg strength, and sick-day resistance under a narrow two-food diet versus a balanced champion meal plan!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="setRunnerDiet('narrow')" id="btn-run-narrow" class="p-3 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500 text-left flex items-center gap-2">
            <span class="text-2xl">🍚🥔</span>
            <div><span class="block">Diet A: Rice &amp; Potatoes Only</span><span class="text-[10px] text-rose-200">Lacks Proteins &amp; Vitamins</span></div>
        </button>
        <button onclick="setRunnerDiet('balanced')" id="btn-run-balanced" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-2xl">🥗🥛</span>
            <div><span class="block">Diet B: Balanced Champion Thali</span><span class="text-[10px] text-slate-400">Grains + Dal + Greens + Fruits</span></div>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Grassy Track Field -->
            <rect x="0" y="0" width="700" height="100" fill="#0f172a" />
            <rect x="0" y="100" width="700" height="80" fill="#7c2d12" />
            <line x1="0" y1="135" x2="700" y2="135" stroke="#ffffff" stroke-width="2" stroke-dasharray="10,8" opacity="0.6" />
            <!-- Finish Line Banner -->
            <line x1="610" y1="90" x2="610" y2="180" stroke="#fbbf24" stroke-width="4" />
            <text x="610" y="75" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">🏁 FINISH</text>

            <!-- Sprinter Figure -->
            <g id="sprinter-token" transform="translate(130, 118)">
                <circle cx="0" cy="-14" r="12" fill="#fed7aa" />
                <text x="-8" y="-9" font-size="14" id="sprinter-face">🤒</text>
                <text x="20" y="0" font-size="28">🏃</text>
            </g>

            <!-- Track Status Badge -->
            <g transform="translate(40, 22)">
                <rect x="0" y="0" width="280" height="54" rx="10" fill="#1e293b" stroke="#475569" />
                <text x="15" y="22" fill="#94a3b8" font-size="10">Health &amp; Speed Status:</text>
                <text id="run-svg-status" x="15" y="42" fill="#f87171" font-size="12" font-weight="bold">Low Immunity &amp; Weak Legs (Tired!)</text>
            </g>
        </svg>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs text-center">
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Muscle Repair Protein:</span>
            <span id="run-protein" class="text-rose-400 font-bold">Critically Low ❌</span>
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Vitamin Immune Shield:</span>
            <span id="run-immune" class="text-rose-400 font-bold">Weak (Catches Colds)</span>
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Finish Line Pace:</span>
            <span id="run-pace" class="text-amber-300 font-bold">Slow &amp; Dizzy Mid-Lap</span>
        </div>
    </div>
</div>

<script>
function setRunnerDiet(mode) {
    const isBal = (mode === 'balanced');
    document.getElementById('btn-run-narrow').className = !isBal
        ? 'p-3 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-run-balanced').className = isBal
        ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    document.getElementById('sprinter-token').setAttribute('transform', isBal ? 'translate(540, 118)' : 'translate(130, 118)');
    document.getElementById('sprinter-face').textContent = isBal ? '😄' : '🤒';
    document.getElementById('run-svg-status').textContent = isBal
        ? 'Strong Stamina & Illness-Free Champion!'
        : 'Low Immunity & Weak Legs (Tired!)';
    document.getElementById('run-svg-status').setAttribute('fill', isBal ? '#4ade80' : '#f87171');
    document.getElementById('run-protein').textContent = isBal ? 'Strong Muscles ✓' : 'Critically Low ❌';
    document.getElementById('run-protein').className = isBal ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold';
    document.getElementById('run-immune').textContent = isBal ? 'Protected & Healthy ✓' : 'Weak (Catches Colds)';
    document.getElementById('run-immune').className = isBal ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold';
    document.getElementById('run-pace').textContent = isBal ? 'Sprints Past Finish Line! 🏆' : 'Slow & Dizzy Mid-Lap';
}
</script>
"""

# Simulator 4: Balanced Food Plates (3-Group Thali Builder)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍽️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Three-Group Balanced Thali Plate Assembler</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Food Groups</span>
    </div>

    <p class="text-xs text-slate-300">Add one item from all three essential nutritional food groups onto your plate to achieve 100% Balanced Body Harmony!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="toggleThaliGroup('energy')" id="btn-thali-energy" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">1. Energy Fuels (+34%)</span>
            <span class="text-[10px] text-amber-300">Wheat Roti, Rice, Millets</span>
        </button>
        <button onclick="toggleThaliGroup('protein')" id="btn-thali-protein" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">2. Body-Builders (+33%)</span>
            <span class="text-[10px] text-cyan-300">Moong Dal, Curd, Paneer</span>
        </button>
        <button onclick="toggleThaliGroup('protect')" id="btn-thali-protect" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">3. Protective Shield (+33%)</span>
            <span class="text-[10px] text-emerald-300">Spinach, Carrots, Guava</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs">
        <div class="flex items-center gap-4">
            <div class="w-24 h-24 rounded-full bg-slate-900 border-4 border-slate-700 flex flex-col items-center justify-center text-2xl" id="thali-plate-visual">
                🍽️
            </div>
            <div>
                <span class="text-slate-400 text-[10px] uppercase block">Balanced Plate Score:</span>
                <span id="thali-score" class="text-2xl font-extrabold text-amber-400">0% Complete</span>
                <p id="thali-msg" class="text-slate-300 mt-1 max-w-md">Click the three buttons above to assemble your colorful complete meal!</p>
            </div>
        </div>
    </div>
</div>

<script>
const thaliState = { energy: false, protein: false, protect: false };

function toggleThaliGroup(g) {
    thaliState[g] = !thaliState[g];
    const btn = document.getElementById('btn-thali-' + g);
    if (btn) {
        btn.className = thaliState[g]
            ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left shadow'
            : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
    }

    let score = (thaliState.energy ? 34 : 0) + (thaliState.protein ? 33 : 0) + (thaliState.protect ? 33 : 0);
    let icons = [];
    if (thaliState.energy) icons.push('🫓');
    if (thaliState.protein) icons.push('🍛');
    if (thaliState.protect) icons.push('🥗');

    document.getElementById('thali-plate-visual').textContent = icons.length ? icons.join('') : '🍽️';
    document.getElementById('thali-score').textContent = `${score}% Complete`;
    document.getElementById('thali-score').className = score === 100
        ? 'text-2xl font-extrabold text-emerald-400'
        : 'text-2xl font-extrabold text-amber-400';
    document.getElementById('thali-msg').textContent = score === 100
        ? 'Champion Thali! Energy grains, muscle-building pulses/dairy, and vitamin-packed greens + fruits work together in perfect balance!'
        : 'Add every remaining food group so no body system stays hungry!';
}
</script>
"""

# Simulator 5: Cooling Summer Treats (Summer Sweat & Hydration Lab)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥥</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Summer Heatwave Hydration &amp; Cooling Treats</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Summer Foods</span>
    </div>

    <p class="text-xs text-slate-300">Pick a natural summer refreshment to inspect how it cools hot bodies and replaces water lost through summer sweat!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectSummerTreat('coconut')" id="btn-sum-coconut" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🥥 Coconut Water</button>
        <button onclick="selectSummerTreat('aampanna')" id="btn-sum-aampanna" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥭 Aam Panna</button>
        <button onclick="selectSummerTreat('lime')" id="btn-sum-lime" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍋 Lime Water</button>
        <button onclick="selectSummerTreat('kulfi')" id="btn-sum-kulfi" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍨 Fruit / Kulfi</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="sum-emoji">🥥</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="sum-title">Fresh Tender Coconut Water</h4>
            <p class="text-slate-300" id="sum-desc">Naturally sterile inside young green husks, tender coconut water bursts with potassium electrolytes and pure fluid that restore lost sweat minerals swiftly!</p>
        </div>
    </div>
</div>

<script>
function selectSummerTreat(t) {
    const map = {
        coconut: { e: '🥥', t: 'Fresh Tender Coconut Water', d: 'Naturally sterile inside young green husks, tender coconut water bursts with potassium electrolytes and pure fluid that restore lost sweat minerals swiftly!' },
        aampanna: { e: '🥭', t: 'Tangy Minty Aam Panna', d: 'Crafted from roasted green mangoes, cooling mint leaves, roasted cumin, and jaggery—protecting outdoor kids safely from dizzy summer heatstrokes!' },
        lime: { e: '🍋', t: 'Sparkling Nimbu Pani (Lime Water)', d: 'Fresh lemon squeezed into cool earthen matka water with a tiny pinch of rock salt quickly restores hydration and brightens tired energy!' },
        kulfi: { e: '🍨', t: 'Creamy Kulfi, Melon & Fresh Fruit Juices', d: 'Cool homemade milk kulfi, fresh mango or orange juice, and crisp 90%-water watermelon slices refresh sunny afternoons safely.' }
    };
    const d = map[t];
    if (!d) return;

    ['coconut', 'aampanna', 'lime', 'kulfi'].forEach(k => {
        const b = document.getElementById('btn-sum-' + k);
        if (b) {
            b.className = (k === t)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sum-emoji').textContent = d.e;
    document.getElementById('sum-title').textContent = d.t;
    document.getElementById('sum-desc').textContent = d.d;
}
</script>
"""

# Simulator 6: Warming Winter Meals (Cold Weather Foods)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥣</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Warming Winter Kitchen &amp; Harvest Picks</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Winter Comfort</span>
    </div>

    <p class="text-xs text-slate-300">Explore seasonal winter foods that burn gentle internal fuel to keep families snug and sniffle-free in chilly weather!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectWinterFood('soup')" id="btn-win-soup" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🥣 Hot Ginger Soup</button>
        <button onclick="selectWinterFood('saag')" id="btn-win-saag" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥬 Sarson Saag</button>
        <button onclick="selectWinterFood('chikki')" id="btn-win-chikki" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥜 Sesame Chikki</button>
        <button onclick="selectWinterFood('milk')" id="btn-win-milk" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥛 Turmeric Milk</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="win-emoji">🥣</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="win-title">Steaming Carrot-Tomato Ginger Soup</h4>
            <p class="text-slate-300" id="win-desc">Fresh seasonal winter carrots and ripe tomatoes simmered with ginger and crushed black pepper warm cold fingers instantly and strengthen immunity!</p>
        </div>
    </div>
</div>

<script>
function selectWinterFood(w) {
    const map = {
        soup: { e: '🥣', t: 'Steaming Carrot-Tomato Ginger Soup', d: 'Fresh seasonal winter carrots and ripe tomatoes simmered with ginger and crushed black pepper warm cold fingers instantly and strengthen immunity!' },
        saag: { e: '🥬', t: 'Warm Mustard Greens & Corn Roti', d: 'Dark green winter mustard leaves cooked into savory sarson saag pair warmly with golden makki roti and white butter.' },
        chikki: { e: '🥜', t: 'Crunchy Sesame-Jaggery & Peanut Chikki', d: 'Dense healthy fats in sesame seeds and peanuts combined with iron-rich jaggery deliver natural winter body warmth.' },
        milk: { e: '🥛', t: 'Bedtime Spiced Turmeric Milk (Haldi Doodh)', d: 'Warm milk stirred with golden anti-inflammatory turmeric powder shields throats and noses gently during frosty winter nights.' }
    };
    const d = map[w];
    if (!d) return;

    ['soup', 'saag', 'chikki', 'milk'].forEach(k => {
        const b = document.getElementById('btn-win-' + k);
        if (b) {
            b.className = (k === w)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('win-emoji').textContent = d.e;
    document.getElementById('win-title').textContent = d.t;
    document.getElementById('win-desc').textContent = d.d;
}
</script>
"""

# Simulator 7: Regional Indian Foods (Culinary Map Explorer)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗺️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">India Regional Crops &amp; Cuisine Explorer</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Cultural Diversity</span>
    </div>

    <p class="text-xs text-slate-300">Travel across four diverse corners of India to discover how local crops and terrain shape signature regional dishes!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectRegion('south')" id="btn-reg-south" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🌴 South Coasts</button>
        <button onclick="selectRegion('west')" id="btn-reg-west" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏜️ West Plains</button>
        <button onclick="selectRegion('east')" id="btn-reg-east" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌊 East Deltas</button>
        <button onclick="selectRegion('north')" id="btn-reg-north" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏔️ North &amp; Hills</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 space-y-1">
            <span class="text-slate-400 text-[10px] uppercase block">Local Climate &amp; Staple Crops:</span>
            <h4 class="font-bold text-emerald-300 text-sm" id="reg-crops">Warm Rainy Coastlines: Paddy Rice, Coconut &amp; Spices</h4>
            <p class="text-slate-300 mt-1" id="reg-why">Abundant monsoon rainfall and palm groves make fermented rice and rich coconut milk stars of southern kitchens.</p>
        </div>
        <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 space-y-1">
            <span class="text-slate-400 text-[10px] uppercase block">Iconic Homemade Regional Plates:</span>
            <h4 class="font-bold text-amber-300 text-sm" id="reg-dishes">Steamed Idli-Sambar, Crisp Dosa &amp; Coconut Avial</h4>
            <p class="text-slate-300 mt-1" id="reg-note">Often served delightfully atop freshly washed green banana leaves!</p>
        </div>
    </div>
</div>

<script>
function selectRegion(reg) {
    const map = {
        south: { crops: 'Warm Rainy Coastlines: Paddy Rice, Coconut & Spices', why: 'Abundant monsoon rainfall and palm groves make fermented rice and rich coconut milk stars of southern kitchens.', dishes: 'Steamed Idli-Sambar, Crisp Dosa & Coconut Avial', note: 'Often served delightfully atop freshly washed green banana leaves!' },
        west: { crops: 'Dry Sunny Plains: Chickpeas, Bajra Millet & Groundnuts', why: 'Hardy dryland millets and chickpeas thrive with modest rainfall, shaping wholesome western baking and steaming.', dishes: 'Gujarat Steamed Dhokla, Dal-Baati & Millet Bhakri', note: 'Spiced wonderfully with peanuts, sesame, and tangy dry kokum or buttermilk!' },
        east: { crops: 'Fertile River Deltas: Rice Paddies, Bamboo & Freshwater Fish', why: 'Lush delta waters of Odisha, Bengal, and Assam sustain bountiful paddy rice, vegetables, and bamboo shoots.', dishes: 'Cooling Pakhala Rice, Machher Jhol & Bamboo Shoot Curry', note: 'Traditional bamboo steaming and mustard-seed tempering create unforgettable regional aromas!' },
        north: { crops: 'Northern Wheat Valleys & Cold Himalayan Slopes', why: 'Golden wheat fields yield crusty parathas while chilly Himalayan valleys inspire warming noodle bowls and broths.', dishes: 'Wheat Paratha-Curd, Rajma-Chawal & Himalayan Thukpa', note: 'Every region reflects clever human adaptation to soil, rain, and season!' }
    };
    const d = map[reg];
    if (!d) return;

    ['south', 'west', 'east', 'north'].forEach(k => {
        const b = document.getElementById('btn-reg-' + k);
        if (b) {
            b.className = (k === reg)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('reg-crops').textContent = d.crops;
    document.getElementById('reg-why').textContent = d.why;
    document.getElementById('reg-dishes').textContent = d.dishes;
    document.getElementById('reg-note').textContent = d.note;
}
</script>
"""

# Simulator 8: Edible Plant Leaves (Farm Leafy Greens Microscope)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥬</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Farm Field Checklist: Edible Plant Leaves</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Plant Parts #1</span>
    </div>

    <p class="text-xs text-slate-300">Inspect the five famous green leafy crops grown in fields and verify why each counts botanically as a Plant Leaf!</p>

    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
        <button onclick="inspectLeaf('palak')" id="btn-lf-palak" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🥬 Spinach</button>
        <button onclick="inspectLeaf('methi')" id="btn-lf-methi" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌿 Fenugreek</button>
        <button onclick="inspectLeaf('cabbage')" id="btn-lf-cabbage" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥦 Cabbage</button>
        <button onclick="inspectLeaf('mustard')" id="btn-lf-mustard" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌱 Mustard</button>
        <button onclick="inspectLeaf('coriander')" id="btn-lf-coriander" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌿 Coriander</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="lf-emoji">🥬</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="lf-title">Spinach (Palak) — Iron-Rich Blood Builder</h4>
            <p class="text-slate-300" id="lf-desc">Broad tender dark-green leaves brimming with natural iron and vitamin K. Rinse thoroughly in water bowls before cooking lightly to preserve crisp nutrients!</p>
        </div>
    </div>
</div>

<script>
function inspectLeaf(lf) {
    const map = {
        palak: { e: '🥬', t: 'Spinach (Palak) — Iron-Rich Blood Builder', d: 'Broad tender dark-green leaves brimming with natural iron and vitamin K. Rinse thoroughly in water bowls before cooking lightly to preserve crisp nutrients!' },
        methi: { e: '🌿', t: 'Fenugreek (Methi) — Aromatic Digestive Leaves', d: 'Clustered trifoliate green leaflets carrying mild bitter warmth tucked wonderfully inside whole-wheat parathas and spiced potato dishes.' },
        cabbage: { e: '🥦', t: 'Cabbage — Tightly Layered Leaf Head', d: 'Peel back every crisp dome sheet to reveal branching leaf veins! A cabbage is dozens of broad leaves folded tightly into a round ball.' },
        mustard: { e: '🌱', t: 'Mustard Greens (Sarson) — Winter Super-Leaf', d: 'Large fuzzy peppery winter leaves rich in calcium and antioxidants, simmered slowly into comforting sarson ka saag.' },
        coriander: { e: '🌿', t: 'Coriander (Dhaniya) — Fragrant Lacy Garnish', d: 'Delicate scalloped green herb leaves sprinkled fresh atop curries and blended with green chilies into refreshing chutneys.' }
    };
    const d = map[lf];
    if (!d) return;

    ['palak', 'methi', 'cabbage', 'mustard', 'coriander'].forEach(k => {
        const b = document.getElementById('btn-lf-' + k);
        if (b) {
            b.className = (k === lf)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('lf-emoji').textContent = d.e;
    document.getElementById('lf-title').textContent = d.t;
    document.getElementById('lf-desc').textContent = d.d;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part1)} simulators for Part 1 (1 to 8).")
    for k in sorted(simulators_part1.keys()):
        print(f"Sim {k}: {len(simulators_part1[k])} chars")

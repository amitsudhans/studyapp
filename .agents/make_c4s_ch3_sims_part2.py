# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 3: Nature Trail
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Aquatic Life Adaptations</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Freshwater Survival</span>
    </div>

    <!-- Species Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="ala-btn-fish" onclick="selectAquaticSpecies('fish')" class="p-2.5 rounded-xl border border-sky-500 bg-sky-950/40 text-sky-300 font-bold ring-2 ring-sky-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐟</span>
            <span>River Fish</span>
        </button>
        <button id="ala-btn-gharial" onclick="selectAquaticSpecies('gharial')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐊</span>
            <span>Gharial</span>
        </button>
        <button id="ala-btn-turtle" onclick="selectAquaticSpecies('turtle')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐢</span>
            <span>River Turtle</span>
        </button>
        <button id="ala-btn-frog" onclick="selectAquaticSpecies('frog')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐸</span>
            <span>Bullfrog</span>
        </button>
    </div>

    <!-- Visual Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="ala-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic aquatic SVG -->
        </div>
        <div id="ala-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-sky-950/20 border border-sky-800/40 leading-relaxed">
            <strong class="text-sky-400">River Fish:</strong> Tapered streamlined body reduces water resistance, steering fins provide balance, and gills extract dissolved oxygen directly from water currents.
        </div>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-lime-500/20 text-lime-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Hexapod Insect Anatomy</h3>
        </div>
        <span class="text-xs text-lime-400 font-medium">Six-Legged Wonders</span>
    </div>

    <!-- Insect Feature Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="hia-btn-mantis" onclick="selectInsectFeature('mantis')" class="p-2.5 rounded-xl border border-lime-500 bg-lime-950/40 text-lime-300 font-bold ring-2 ring-lime-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦗</span>
            <span>Praying Mantis</span>
        </button>
        <button id="hia-btn-beetle" onclick="selectInsectFeature('beetle')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🪲</span>
            <span>Beetle Elytra</span>
        </button>
        <button id="hia-btn-bee" onclick="selectInsectFeature('bee')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐝</span>
            <span>Honeybee Pollen</span>
        </button>
        <button id="hia-btn-anatomy" onclick="selectInsectFeature('anatomy')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🔬</span>
            <span>3 Body Segments</span>
        </button>
    </div>

    <!-- Anatomy Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="hia-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic insect SVG -->
        </div>
        <div id="hia-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-lime-950/20 border border-lime-800/40 leading-relaxed">
            <strong class="text-lime-400">Praying Mantis:</strong> Cryptic green camouflage matches foliage, while spiny raptorial front legs snap forward in milliseconds to snare insect prey.
        </div>
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Botanical Leaf Shapes</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Plant Diversity</span>
    </div>

    <!-- Leaf Specimen Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="bls-btn-peepal" onclick="selectLeafSpecimen('peepal')" class="p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🍃</span>
            <span>Peepal Drip-Tip</span>
        </button>
        <button id="bls-btn-teak" onclick="selectLeafSpecimen('teak')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🍁</span>
            <span>Teak Broad Leaf</span>
        </button>
        <button id="bls-btn-pine" onclick="selectLeafSpecimen('pine')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌲</span>
            <span>Pine Needle</span>
        </button>
        <button id="bls-btn-lemon" onclick="selectLeafSpecimen('lemon')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🍋</span>
            <span>Aromatic Citrus</span>
        </button>
    </div>

    <!-- Visual Botanical Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="bls-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Leaf SVG -->
        </div>
        <div id="bls-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-emerald-950/20 border border-emerald-800/40 leading-relaxed">
            <strong class="text-emerald-400">Peepal Leaf:</strong> Heart-shaped leaf with an elongated, slender drip-tip that sheds heavy monsoon raindrops rapidly to prevent fungal infections.
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Leaf Vein Architecture</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Vascular Transport</span>
    </div>

    <!-- Venation Pattern Toggle -->
    <div class="grid grid-cols-2 gap-2 text-xs">
        <button id="lvp-btn-reticulate" onclick="selectVenationPattern('reticulate')" class="p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex items-center justify-center gap-2">
            <span class="text-lg">🕸️</span>
            <span>Reticulate (Net-like)</span>
        </button>
        <button id="lvp-btn-parallel" onclick="selectVenationPattern('parallel')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex items-center justify-center gap-2">
            <span class="text-lg">🌿</span>
            <span>Parallel (Straight lines)</span>
        </button>
    </div>

    <!-- Vein Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="lvp-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Vein SVG -->
        </div>
        <div id="lvp-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-teal-950/20 border border-teal-800/40 leading-relaxed">
            <strong class="text-teal-400">Reticulate Venation (Dicot):</strong> Prominent central midrib with branching lateral veins forming an interconnected mesh. Found in Mango, Peepal, and Banyan.
        </div>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Leaf Crayon Rubbing Studio</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Art & Science</span>
    </div>

    <!-- Step Controls -->
    <div class="flex items-center justify-between bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
        <span id="lcr-step-label" class="text-amber-400 font-bold">Step 1: Place Leaf Rough Side Up</span>
        <div class="flex gap-2">
            <button onclick="prevCrayonStep()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-white rounded font-medium transition">← Prev</button>
            <button onclick="nextCrayonStep()" class="px-2.5 py-1 bg-amber-600 hover:bg-amber-500 text-white rounded font-bold transition">Next →</button>
        </div>
    </div>

    <!-- Visual Interactive Area -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="lcr-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Crayon Rubbing SVG -->
        </div>
        <div id="lcr-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-amber-950/20 border border-amber-800/40 leading-relaxed">
            <strong class="text-amber-400">Step 1:</strong> Select a freshly fallen leaf and place its rough lower surface facing upward. Raised veins create friction for clear impressions.
        </div>
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Web Of Life Yarn Game</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Interdependence</span>
    </div>

    <!-- Node Connector Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-1.5 text-xs">
        <button id="wol-btn-sun" onclick="connectWebNode('sun')" class="p-2 rounded-lg border border-yellow-500 bg-yellow-950/40 text-yellow-300 font-bold ring-2 ring-yellow-500 transition-all flex flex-col items-center gap-1">
            <span class="text-lg">☀️</span>
            <span>Sun (Energy)</span>
        </button>
        <button id="wol-btn-plant" onclick="connectWebNode('plant')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🌱</span>
            <span>Grass (Producer)</span>
        </button>
        <button id="wol-btn-deer" onclick="connectWebNode('deer')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🦌</span>
            <span>Deer (Herbivore)</span>
        </button>
        <button id="wol-btn-tiger" onclick="connectWebNode('tiger')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🐅</span>
            <span>Tiger (Apex)</span>
        </button>
        <button id="wol-btn-fungi" onclick="connectWebNode('fungi')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🍄</span>
            <span>Fungi (Recycle)</span>
        </button>
    </div>

    <!-- Web Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="wol-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Yarn Web SVG -->
        </div>
        <div id="wol-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-yellow-950/20 border border-yellow-800/40 leading-relaxed">
            <strong class="text-yellow-400">Radiant Solar Energy:</strong> Sunlight provides the essential energy for green plants to manufacture food via photosynthesis, sustaining the entire food web.
        </div>
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Ecosystem Disruption Lab</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">Trophic Cascades</span>
    </div>

    <!-- Disruption Scenarios -->
    <div class="grid grid-cols-3 gap-2 text-xs">
        <button id="edl-btn-balanced" onclick="triggerDisruption('balanced')" class="p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">⚖️</span>
            <span>Balanced Forest</span>
        </button>
        <button id="edl-btn-deforest" onclick="triggerDisruption('deforest')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🪓</span>
            <span>Remove Trees</span>
        </button>
        <button id="edl-btn-notiger" onclick="triggerDisruption('notiger')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">⚠️</span>
            <span>Remove Predator</span>
        </button>
    </div>

    <!-- Cascade Visual -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="edl-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Food Web SVG -->
        </div>
        <div id="edl-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-rose-950/20 border border-rose-800/40 leading-relaxed">
            <strong class="text-emerald-400">Balanced Ecosystem:</strong> Intact canopies nourish herbivores, predators regulate grazing numbers, and decomposers recycle soil nutrients smoothly.
        </div>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-violet-500/20 text-violet-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">State Nature Symbols</h3>
        </div>
        <span class="text-xs text-violet-400 font-medium">Regional Heritage</span>
    </div>

    <!-- Symbol Category Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="sns-btn-animal" onclick="selectStateSymbol('animal')" class="p-2.5 rounded-xl border border-violet-500 bg-violet-950/40 text-violet-300 font-bold ring-2 ring-violet-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦌</span>
            <span>State Animal (Deer)</span>
        </button>
        <button id="sns-btn-bird" onclick="selectStateSymbol('bird')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🕊️</span>
            <span>State Bird (Dudhraj)</span>
        </button>
        <button id="sns-btn-tree" onclick="selectStateSymbol('tree')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌳</span>
            <span>State Tree (Banyan)</span>
        </button>
        <button id="sns-btn-origami" onclick="selectStateSymbol('origami')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐢</span>
            <span>Origami Turtle Craft</span>
        </button>
    </div>

    <!-- Symbol Exhibit Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="sns-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic State Symbol SVG -->
        </div>
        <div id="sns-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-violet-950/20 border border-violet-800/40 leading-relaxed">
            <strong class="text-violet-400">State Animal - Barasingha:</strong> The swamp deer of Madhya Pradesh features twelve-tined antlers. Successfully conserved in Kanha and Satpura national parks.
        </div>
    </div>
</div>
"""

sims_part2 = {
    9: sim9,
    10: sim10,
    11: sim11,
    12: sim12,
    13: sim13,
    14: sim14,
    15: sim15,
    16: sim16,
}


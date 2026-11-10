# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 3: Nature Trail
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Pachmarhi Biosphere Explorer</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Protected Sanctuary</span>
    </div>

    <!-- Hotspot Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="pbe-btn-cliffs" onclick="selectPachmarhiSpot('cliffs')" class="p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">⛰️</span>
            <span>Sandstone Cliffs</span>
        </button>
        <button id="pbe-btn-waterfall" onclick="selectPachmarhiSpot('waterfall')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌊</span>
            <span>Duchess Falls</span>
        </button>
        <button id="pbe-btn-canopy" onclick="selectPachmarhiSpot('canopy')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌳</span>
            <span>Teak & Sal Forest</span>
        </button>
        <button id="pbe-btn-dhoopgarh" onclick="selectPachmarhiSpot('dhoopgarh')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌅</span>
            <span>Dhoopgarh Peak</span>
        </button>
    </div>

    <!-- Interactive Visual Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="pbe-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic SVG illustration rendered by JS -->
        </div>
        <div id="pbe-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-emerald-950/20 border border-emerald-800/40 leading-relaxed">
            <strong class="text-emerald-400">Sandstone Cliffs:</strong> Towering prehistoric rock shelters in the Satpura range shelter ancient cave art and provide safe roosts for eagles and vultures.
        </div>
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Forest Safety & Etiquette</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Trail Guidelines</span>
    </div>

    <!-- Rule Selector Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="fse-btn-silence" onclick="selectForestRule('silence')" class="p-2.5 rounded-xl border border-amber-500 bg-amber-950/40 text-amber-300 font-bold ring-2 ring-amber-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🤫</span>
            <span>Keep Quiet</span>
        </button>
        <button id="fse-btn-nofeed" onclick="selectForestRule('nofeed')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚫🥪</span>
            <span>Do Not Feed</span>
        </button>
        <button id="fse-btn-noplastic" onclick="selectForestRule('noplastic')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚯</span>
            <span>No Plastic</span>
        </button>
        <button id="fse-btn-trail" onclick="selectForestRule('trail')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🥾</span>
            <span>Stay on Path</span>
        </button>
    </div>

    <!-- Rule Visual Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="fse-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic SVG rendered by JS -->
        </div>
        <div id="fse-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-amber-950/20 border border-amber-800/40 leading-relaxed">
            <strong class="text-amber-400">Keep Quiet:</strong> Speak in soft murmurs so wild animals are not startled into flight. Quiet observation rewards naturalists with intimate glimpses of wildlife.
        </div>
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Forest Wildlife Classifier</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Habitat Strata</span>
    </div>

    <!-- Stratum Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="fwc-btn-terrestrial" onclick="selectAnimalStratum('terrestrial')" class="p-2.5 rounded-xl border border-cyan-500 bg-cyan-950/40 text-cyan-300 font-bold ring-2 ring-cyan-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦌</span>
            <span>Land / Floor</span>
        </button>
        <button id="fwc-btn-arboreal" onclick="selectAnimalStratum('arboreal')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐒</span>
            <span>Tree Canopy</span>
        </button>
        <button id="fwc-btn-aerial" onclick="selectAnimalStratum('aerial')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦅</span>
            <span>Sky / Aerial</span>
        </button>
        <button id="fwc-btn-aquatic" onclick="selectAnimalStratum('aquatic')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐊</span>
            <span>Water / Aquatic</span>
        </button>
    </div>

    <!-- Visual Stratum Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="fwc-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic stratum SVG -->
        </div>
        <div id="fwc-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-cyan-950/20 border border-cyan-800/40 leading-relaxed">
            <strong class="text-cyan-400">Terrestrial Dwellers:</strong> Spotted deer (chital), sambar, and wild boars graze along the leaf-strewn forest floor, alert to nearby feline predators.
        </div>
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Unique Creature Features</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Anatomical Marvels</span>
    </div>

    <!-- Animal Selector -->
    <div class="grid grid-cols-3 gap-2 text-xs">
        <button id="ucf-btn-elephant" onclick="selectUniqueCreature('elephant')" class="p-2.5 rounded-xl border border-purple-500 bg-purple-950/40 text-purple-300 font-bold ring-2 ring-purple-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐘</span>
            <span>Elephant Trunk</span>
        </button>
        <button id="ucf-btn-squirrel" onclick="selectUniqueCreature('squirrel')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐿️</span>
            <span>Giant Squirrel</span>
        </button>
        <button id="ucf-btn-monkey" onclick="selectUniqueCreature('monkey')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐵</span>
            <span>Spectacled Monkey</span>
        </button>
    </div>

    <!-- Anatomy Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="ucf-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic creature SVG -->
        </div>
        <div id="ucf-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-purple-950/20 border border-purple-800/40 leading-relaxed">
            <strong class="text-purple-400">Asian Elephant Trunk:</strong> Contains over 40,000 muscle units and zero bones, allowing the elephant to uproot trees or gently pick up a tiny blade of grass.
        </div>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Pugmarks & Lookalikes</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Tracking Analysis</span>
    </div>

    <!-- Track & Lookalike Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="pml-btn-tiger" onclick="selectTrackComparator('tiger')" class="p-2.5 rounded-xl border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐾</span>
            <span>Tiger Pugmark</span>
        </button>
        <button id="pml-btn-wolf" onclick="selectTrackComparator('wolf')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐕</span>
            <span>Canine Track</span>
        </button>
        <button id="pml-btn-croc" onclick="selectTrackComparator('croc')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐊</span>
            <span>Croc vs Alligator</span>
        </button>
        <button id="pml-btn-dove" onclick="selectTrackComparator('dove')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🕊️</span>
            <span>Pigeon vs Dove</span>
        </button>
    </div>

    <!-- Comparative Visual Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="pml-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic footprint/comparison SVG -->
        </div>
        <div id="pml-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-orange-950/20 border border-orange-800/40 leading-relaxed">
            <strong class="text-orange-400">Tiger Pugmark:</strong> Round paw print with four distinct toe pads and NO visible claws. Big cats retract their sharp claws while walking.
        </div>
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Remarkable Bird Traits</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Avian Marvels</span>
    </div>

    <!-- Bird Selection Grid -->
    <div class="grid grid-cols-3 gap-2 text-xs">
        <button id="rbt-btn-hornbill" onclick="selectAvianFeature('hornbill')" class="p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦤</span>
            <span>Pied Hornbill</span>
        </button>
        <button id="rbt-btn-peacock" onclick="selectAvianFeature('peacock')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦚</span>
            <span>Indian Peacock</span>
        </button>
        <button id="rbt-btn-owl" onclick="selectAvianFeature('owl')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦉</span>
            <span>Barn Owl</span>
        </button>
    </div>

    <!-- Avian Visual Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="rbt-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic bird SVG -->
        </div>
        <div id="rbt-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-teal-950/20 border border-teal-800/40 leading-relaxed">
            <strong class="text-teal-400">Malabar Pied Hornbill:</strong> Features a massive casque atop its curved beak that acts as an acoustic sound resonator. The female seals herself in a tree hole to protect eggs.
        </div>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Beaks, Claws & Diet Matcher</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Functional Anatomy</span>
    </div>

    <!-- Bird Type Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="bcd-btn-eagle" onclick="selectBeakAndClaw('eagle')" class="p-2.5 rounded-xl border border-blue-500 bg-blue-950/40 text-blue-300 font-bold ring-2 ring-blue-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦅</span>
            <span>Raptor Eagle</span>
        </button>
        <button id="bcd-btn-sunbird" onclick="selectBeakAndClaw('sunbird')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌸</span>
            <span>Purple Sunbird</span>
        </button>
        <button id="bcd-btn-woodpecker" onclick="selectBeakAndClaw('woodpecker')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🪵</span>
            <span>Woodpecker</span>
        </button>
        <button id="bcd-btn-duck" onclick="selectBeakAndClaw('duck')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦆</span>
            <span>Pond Duck</span>
        </button>
    </div>

    <!-- Adaptation Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="bcd-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Beak & Claw SVG -->
        </div>
        <div id="bcd-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-blue-950/20 border border-blue-800/40 leading-relaxed">
            <strong class="text-blue-400">Raptor Eagle:</strong> Razor-sharp hooked beak tears prey, while muscular curved talons lock onto snakes and rodents with lethal grip force.
        </div>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Interactive Bird Diary</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Field Journal</span>
    </div>

    <!-- Sighting Selector -->
    <div class="grid grid-cols-3 gap-2 text-xs">
        <button id="ibd-btn-flycatcher" onclick="selectDiarySighting('flycatcher')" class="p-2.5 rounded-xl border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🕊️</span>
            <span>Paradise Flycatcher</span>
        </button>
        <button id="ibd-btn-barbet" onclick="selectDiarySighting('barbet')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐦</span>
            <span>Coppersmith Barbet</span>
        </button>
        <button id="ibd-btn-kingfisher" onclick="selectDiarySighting('kingfisher')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🐟</span>
            <span>Pied Kingfisher</span>
        </button>
    </div>

    <!-- Field Notebook Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="ibd-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Diary SVG -->
        </div>
        <div id="ibd-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-indigo-950/20 border border-indigo-800/40 leading-relaxed">
            <strong class="text-indigo-400">Field Entry:</strong> Asian Paradise Flycatcher spotted in Mahua canopy at 08:30 AM. Male with long white ribbon tail catching moths mid-air. Melodious territorial song recorded.
        </div>
    </div>
</div>
"""

sims_part1 = {
    1: sim1,
    2: sim2,
    3: sim3,
    4: sim4,
    5: sim5,
    6: sim6,
    7: sim7,
    8: sim8,
}


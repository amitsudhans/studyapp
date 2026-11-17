# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 7: How do Organisms Reproduce?
Simulators 1 to 8 HTML Generator
"""

import json

sims_part1 = {
    1: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔬</span> Reproduction & Species Continuity Simulator
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Compare population extinction without reproduction vs long-term species survival</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide1Scenario('extinction')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-rose-300 border border-rose-500/30 transition-all">
                    No Reproduction (Extinction)
                </button>
                <button onclick="setSlide1Scenario('continuity')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Continuous Reproduction (Survival)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide1Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide1Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click a scenario above to observe how reproduction maintains species visibility and prevents permanent extinction.
        </div>
    </div>
    """,

    2: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧬</span> DNA Replication & Cellular Apparatus Synthesis
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Biochemical DNA copying, organelle duplication & subtle variations</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide2Replication()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                    <span>⚡</span> Duplicate DNA & Cell
                </button>
                <button onclick="resetSlide2()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all">
                    Reset
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide2Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide2Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click <b>"Duplicate DNA & Cell"</b> to observe biochemical DNA copying accompanied by functional cellular apparatus creation.
        </div>
    </div>
    """,

    3: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌡️</span> Environmental Thermal Shock & Bacterial Variation
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Demonstrating how pre-existing genetic variations preserve species under environmental catastrophes</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide3Temp('normal')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Normal Pond (25°C)
                </button>
                <button onclick="setSlide3Temp('heatwave')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-rose-300 border border-rose-500/30 transition-all">
                    Thermal Shock (45°C)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide3Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide3Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Select <b>"Thermal Shock (45°C)"</b> to witness standard bacteria perish while rare heat-resistant variants survive to continue the species.
        </div>
    </div>
    """,

    4: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🦠</span> Unicellular Fission Lab: Binary vs Multiple
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Amoeba (any plane), Leishmania (flagellar orientation) & Plasmodium (cyst multiple)</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide4Mode('amoeba')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Amoeba
                </button>
                <button onclick="setSlide4Mode('leishmania')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Leishmania
                </button>
                <button onclick="setSlide4Mode('plasmodium')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 transition-all">
                    Plasmodium
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide4Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide4Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click on an organism above to observe how cellular structure governs the plane and mechanism of fission.
        </div>
    </div>
    """,

    5: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌱</span> Budding, Fragmentation & Regeneration
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Yeast budding, Spirogyra filament fragmentation & Planaria stem cell regeneration</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide5Type('yeast')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 transition-all">
                    Yeast Budding
                </button>
                <button onclick="setSlide5Type('spirogyra')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Spirogyra Fragmentation
                </button>
                <button onclick="setSlide5Type('planaria')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Planaria Regeneration
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide5Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide5Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Explore diverse asexual adaptations across simple unicellular and multicellular living organisms.
        </div>
    </div>
    """,

    6: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌿</span> Vegetative Propagation & Micropropagation
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Bryophyllum leaf margin buds, potato tuber eyes & laboratory callus tissue culture</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide6Veg('bryophyllum')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Bryophyllum Leaf
                </button>
                <button onclick="setSlide6Veg('potato')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 transition-all">
                    Potato Tuber Eyes
                </button>
                <button onclick="setSlide6Veg('tissue')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Tissue Culture
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide6Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide6Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click an option above to examine natural foliar budding, stem tuber sprouting, or commercial sterile callus culture.
        </div>
    </div>
    """,

    7: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🍞</span> Rhizopus Bread Mould Spore Formation
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Vegetative hyphae, protective thick-walled sporangia & atmospheric dispersal</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide7Rupture()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                    <span>💨</span> Rupture & Disperse Spores
                </button>
                <button onclick="resetSlide7()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all">
                    Reset
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide7Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide7Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click <b>"Rupture & Disperse Spores"</b> to observe the release of microscopic thick-walled spores from aerial sporangia capsules.
        </div>
    </div>
    """,

    8: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>⚖️</span> Sexual Reproduction Logic: Halving & Restoration
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Meiotic chromosome halving (2n -> n) in gametes & diploid restoration at fertilization</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide8Stage('meiosis')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 transition-all">
                    Meiosis (2n → n)
                </button>
                <button onclick="setSlide8Stage('fertilization')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Fertilization (n + n → 2n)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide8Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide8Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Select <b>"Meiosis (2n → n)"</b> or <b>"Fertilization (n + n → 2n)"</b> to see how sexual reproduction prevents doubling of DNA content.
        </div>
    </div>
    """
}

with open('.agents/c10s_ch7_sims_part1.json', 'w', encoding='utf-8') as f:
    json.dump(sims_part1, f, indent=2)

print("Simulators 1 to 8 successfully generated!")

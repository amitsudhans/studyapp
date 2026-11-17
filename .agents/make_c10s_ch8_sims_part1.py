# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 8: Heredity
Simulators 1 to 8 HTML Generator
"""

import json

sims_part1 = {
    1: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧬</span> Accumulation of Variation Across Generations
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Compare subtle copying inaccuracies in asexual division with diverse sexual recombination</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide1Mode('asexual')" id="btnSlide1Asexual" class="px-3 py-1.5 rounded-xl bg-cyan-600 text-white text-xs font-semibold shadow-md transition-all">
                    Asexual (Sugarcane / Bacteria)
                </button>
                <button onclick="setSlide1Mode('sexual')" id="btnSlide1Sexual" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Sexual (High Diversity)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide1Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="flex flex-wrap items-center justify-between gap-2 pt-1 border-t border-slate-800/80">
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400 font-medium">Generation:</span>
                <span id="slide1GenBadge" class="px-2.5 py-0.5 rounded-full bg-slate-800 text-cyan-400 text-xs font-bold border border-cyan-500/20">Gen 1</span>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="stepSlide1Gen()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-200 border border-slate-700 transition-all">
                    Next Generation (Reproduction)
                </button>
                <button onclick="resetSlide1()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-400 border border-slate-700 transition-all">
                    Reset
                </button>
            </div>
        </div>

        <div id="slide1Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In asexual reproduction, 1 individual divides into 2 with almost identical design; subtle variations accumulate very slowly over generations due to minor DNA copying inaccuracies.
        </div>
    </div>
    """,

    2: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔬</span> DNA Replication & Copying Inaccuracies
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Observe complementary base pairing and nucleotide mismatch variations</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="replicateSlide2DNA()" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md transition-all">
                    Replicate DNA Fork
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide2Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Copying Fidelity / Mutation Rate:</label>
                <input type="range" id="slide2FidelitySlider" min="1" max="3" value="2" oninput="setSlide2Fidelity(this.value)" class="w-full accent-indigo-500 cursor-pointer">
                <div class="flex justify-between text-[10px] text-slate-500 mt-0.5">
                    <span>Ultra-High (99.9%)</span>
                    <span class="text-indigo-400 font-semibold">Normal (99.0%)</span>
                    <span>High Mutation (95%)</span>
                </div>
            </div>
            <div id="slide2Stats" class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs text-slate-300 flex items-center justify-around">
                <span>Matching Bases: <strong class="text-emerald-400" id="slide2Matches">24/24</strong></span>
                <span>Mismatches: <strong class="text-amber-400" id="slide2Errors">0</strong></span>
            </div>
        </div>

        <div id="slide2Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            DNA replication is highly precise (A pairs with T, G pairs with C), but occasional biochemical slip-ups introduce single nucleotide variants that serve as the raw material for variation.
        </div>
    </div>
    """,

    3: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌡️</span> Environmental Selection of Advantageous Variants
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Simulate a heat wave acting on heat-sensitive vs heat-resistant bacterial variants</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="applySlide3HeatWave()" class="px-3 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-semibold shadow-md transition-all">
                    Trigger Heat Wave (65°C)
                </button>
                <button onclick="resetSlide3Culture()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Reset Culture
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide3Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Ambient Water Temperature: <span id="slide3TempDisplay" class="text-amber-400 font-bold">30°C</span></label>
                <input type="range" id="slide3TempSlider" min="20" max="75" value="30" oninput="setSlide3Temp(this.value)" class="w-full accent-rose-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-emerald-500 inline-block"></span> Normal (<span id="slide3NormalCount">45</span>)</span>
                <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-rose-500 inline-block"></span> Heat-Resistant (<span id="slide3ResistantCount">5</span>)</span>
            </div>
        </div>

        <div id="slide3Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In moderate temperatures (30°C), normal bacteria thrive. When water temperature surges past 55°C, normal bacteria perish while heat-resistant variants survive and multiply, demonstrating natural selection.
        </div>
    </div>
    """,

    4: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>👥</span> Equal Parental Contribution in Heredity
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore how maternal and paternal gametes each contribute one set of genes</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="fuseSlide4Gametes()" class="px-3 py-1.5 rounded-xl bg-teal-600 hover:bg-teal-500 text-white text-xs font-semibold shadow-md transition-all">
                    Fuse Gametes (Fertilization)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide4Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="flex flex-wrap items-center justify-between gap-2 pt-1 border-t border-slate-800/80">
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Select Character:</span>
                <select id="slide4TraitSelect" onchange="setSlide4Trait(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-teal-500">
                    <option value="height">Plant Height (Tall 'T' / Dwarf 't')</option>
                    <option value="seed">Seed Shape (Round 'R' / Wrinkled 'r')</option>
                    <option value="earlobe">Human Earlobe (Free 'E' / Attached 'e')</option>
                </select>
            </div>
            <span id="slide4GenotypeBadge" class="text-xs font-mono font-bold text-teal-400 px-3 py-1 rounded-full bg-slate-900 border border-teal-500/30">
                Ploidy: Diploid (2n)
            </span>
        </div>

        <div id="slide4Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Both parents contribute equal amounts of genetic material. Offspring inherit two copies of each gene: one maternal allele via the ovum and one paternal allele via the sperm.
        </div>
    </div>
    """,

    5: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>👂</span> Inherited Human Traits: Earlobe Survey (Activity 8.1)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Survey free earlobes (hanging) vs attached earlobes (fused) in a population</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="sampleSlide5Earlobes(40)" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-semibold shadow-md transition-all">
                    Survey Class (40)
                </button>
                <button onclick="sampleSlide5Earlobes(200)" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Large School (200)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide5Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Total Surveyed</span>
                <span id="slide5Total" class="text-sm font-bold text-white">40</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-amber-500/30">
                <span class="block text-[10px] text-amber-300">Free Earlobes</span>
                <span id="slide5Free" class="text-sm font-bold text-amber-400">30 (75%)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-700">
                <span class="block text-[10px] text-slate-400">Attached Earlobes</span>
                <span id="slide5Attached" class="text-sm font-bold text-slate-200">10 (25%)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Dominant Trait</span>
                <span class="text-sm font-bold text-emerald-400">Free (E)</span>
            </div>
        </div>

        <div id="slide5Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In human populations, free earlobes are far more common because the free earlobe allele is dominant, while attached earlobes require two copies of the recessive allele.
        </div>
    </div>
    """,

    6: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌱</span> Mendel's Pea Breeding Bench (Pisum sativum)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore the 7 contrasting pairs of characters and controlled cross-pollination</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="pollinateSlide6Peas()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow-md transition-all">
                    Cross-Pollinate Flowers
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide6Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="flex flex-wrap items-center justify-between gap-2 pt-1 border-t border-slate-800/80">
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Mendelian Trait:</span>
                <select id="slide6TraitSelect" onchange="setSlide6PeaTrait(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-emerald-500">
                    <option value="height">Plant Height: Tall vs Dwarf</option>
                    <option value="seed_shape">Seed Shape: Round vs Wrinkled</option>
                    <option value="seed_color">Seed Color: Yellow vs Green</option>
                    <option value="flower_color">Flower Color: Violet vs White</option>
                    <option value="pod_shape">Pod Shape: Inflated vs Constricted</option>
                </select>
            </div>
            <span id="slide6DomBadge" class="text-xs text-emerald-400 font-semibold px-2.5 py-0.5 rounded-full bg-slate-900 border border-emerald-500/20">
                Dominant vs Recessive Pair
            </span>
        </div>

        <div id="slide6Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Mendel chose garden peas because they have distinct contrasting traits, reproduce rapidly, and can be artificially cross-pollinated by dusting pollen onto emasculated flowers.
        </div>
    </div>
    """,

    7: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🪴</span> Monohybrid Cross: Tall × Short Pea Plants
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Track parental cross, uniform F1 progeny, and the 3:1 ratio in the F2 generation</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide7Stage('P')" id="btnSlide7P" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold">Parental (P)</button>
                <button onclick="setSlide7Stage('F1')" id="btnSlide7F1" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">F1 Progeny</button>
                <button onclick="setSlide7Stage('F2')" id="btnSlide7F2" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">F2 Selfing</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide7Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Current Generation</span>
                <span id="slide7CurrentGen" class="text-xs font-bold text-emerald-400">Parental (TT × tt)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Tall Plants</span>
                <span id="slide7TallCount" class="text-xs font-bold text-white">50% (P)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Dwarf Plants</span>
                <span id="slide7ShortCount" class="text-xs font-bold text-white">50% (P)</span>
            </div>
        </div>

        <div id="slide7Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In the parental cross, pure tall (TT) crosses with pure short (tt). The F1 generation is 100% tall (Tt). When F1 self-pollinates, the F2 generation yields exactly 3 tall : 1 short!
        </div>
    </div>
    """,

    8: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔲</span> Punnett Square & Allelic Dominance Calculator
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Determine genotypic (1:2:1) and phenotypic (3:1) distributions</p>
            </div>
            <div class="flex items-center gap-2">
                <select id="slide8CrossSelect" onchange="updateSlide8Cross(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-purple-500">
                    <option value="Tt_Tt">F1 Selfing: Tt × Tt (Heterozygous)</option>
                    <option value="TT_tt">Parental Cross: TT × tt</option>
                    <option value="Tt_tt">Test Cross: Tt × tt</option>
                </select>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide8Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Phenotype Ratio</span>
                <span id="slide8PhenoRatio" class="text-sm font-bold text-purple-400">3 Tall : 1 Dwarf (75% vs 25%)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Genotype Ratio</span>
                <span id="slide8GenoRatio" class="text-sm font-bold text-cyan-400">1 TT : 2 Tt : 1 tt (25% : 50% : 25%)</span>
            </div>
        </div>

        <div id="slide8Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            The Punnett square displays all 4 gametic combinations. Because allele 'T' is dominant, both 'TT' and 'Tt' develop as tall plants, creating the classic 3:1 phenotypic ratio.
        </div>
    </div>
    """
}

if __name__ == "__main__":
    with open(".agents/c10s_ch8_sims_part1.json", "w", encoding="utf-8") as f:
        json.dump(sims_part1, f, indent=2)
    print("Saved .agents/c10s_ch8_sims_part1.json successfully! (8 simulators)")

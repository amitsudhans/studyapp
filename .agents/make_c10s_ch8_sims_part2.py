# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 8: Heredity
Simulators 9 to 16 HTML Generator
"""

import json

sims_part2 = {
    9: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🟡</span> Dihybrid Cross: Round Yellow × Wrinkled Green
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Track simultaneous inheritance of two traits: seed shape and seed color</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="crossSlide9Parents()" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-semibold shadow-md transition-all">
                    Perform Dihybrid Cross
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide9Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Parent 1 (Dominant)</span>
                <span class="text-xs font-bold text-amber-400">Round Yellow (RRYY)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Parent 2 (Recessive)</span>
                <span class="text-xs font-bold text-emerald-400">Wrinkled Green (rryy)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-amber-500/30 col-span-2 sm:col-span-1">
                <span class="block text-[10px] text-slate-400">F1 Generation</span>
                <span class="text-xs font-bold text-white">100% Round Yellow (RrYy)</span>
            </div>
        </div>

        <div id="slide9Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Gametes from RRYY carry 'RY' and gametes from rryy carry 'ry'. All F1 offspring inherit the heterozygous genotype RrYy, producing 100% round yellow seeds because R and Y are completely dominant!
        </div>
    </div>
    """,

    10: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🎲</span> Law of Independent Assortment (16-Cell Punnett Grid)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore the 9:3:3:1 phenotypic ratio and appearance of new recombinant traits</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="filterSlide10Seeds('all')" id="btnSlide10All" class="px-2.5 py-1 rounded-lg bg-indigo-600 text-white text-xs font-semibold">All 16</button>
                <button onclick="filterSlide10Seeds('parental')" id="btnSlide10Parental" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Parentals (10)</button>
                <button onclick="filterSlide10Seeds('recombinant')" id="btnSlide10Recomb" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Recombinants (6)</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide10Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-amber-500/30">
                <span class="block text-[10px] text-amber-300">Round Yellow</span>
                <span id="slide10RY" class="text-sm font-bold text-white">9 / 16</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-emerald-500/30">
                <span class="block text-[10px] text-emerald-300">Round Green</span>
                <span id="slide10RG" class="text-sm font-bold text-emerald-400">3 / 16 (New)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-yellow-500/30">
                <span class="block text-[10px] text-yellow-300">Wrinkled Yellow</span>
                <span id="slide10WY" class="text-sm font-bold text-yellow-400">3 / 16 (New)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-teal-500/30">
                <span class="block text-[10px] text-teal-300">Wrinkled Green</span>
                <span id="slide10WG" class="text-sm font-bold text-teal-400">1 / 16</span>
            </div>
        </div>

        <div id="slide10Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            The appearance of round green (3) and wrinkled yellow (3) seeds demonstrates that seed shape and seed color assort independently during gamete formation, confirming Mendel's Law of Independent Assortment.
        </div>
    </div>
    """,

    11: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧬</span> Gene Expression: DNA to Functional Protein
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Cellular DNA contains coding segments (genes) that direct protein synthesis</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="transcribeSlide11Gene()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-semibold shadow-md transition-all">
                    Transcribe & Translate
                </button>
                <button onclick="toggleSlide11Mutation()" id="btnSlide11Mut" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Mutate Gene Segment
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide11Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">DNA Gene Code</span>
                <span id="slide11DNACode" class="text-xs font-mono font-bold text-cyan-400">TAC-GGC-TTA-ACT</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">mRNA Transcript</span>
                <span id="slide11RNACode" class="text-xs font-mono font-bold text-emerald-400">AUG-CCG-AAU-UGA</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Protein Activity</span>
                <span id="slide11ProteinStatus" class="text-xs font-bold text-emerald-400">Active Enzyme (100%)</span>
            </div>
        </div>

        <div id="slide11Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Cellular DNA stores information for proteins. A gene is transcribed into mRNA, which translates into an amino acid sequence forming an enzyme that controls cellular biochemical reactions.
        </div>
    </div>
    """,

    12: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌿</span> Enzyme Efficiency & Plant Growth Hormone
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Observe how gene-controlled enzyme efficiency governs tall vs dwarf plant height</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide12EnzymeLevel(100)" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold">Tall (100% Enzyme)</button>
                <button onclick="setSlide12EnzymeLevel(20)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Dwarf (20% Enzyme)</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide12Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Enzyme Catalytic Efficiency: <span id="slide12EffDisplay" class="text-emerald-400 font-bold">100%</span></label>
                <input type="range" id="slide12Slider" min="10" max="100" value="100" oninput="setSlide12EnzymeSlider(this.value)" class="w-full accent-emerald-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Hormone Synthesized: <strong id="slide12HormoneLevel" class="text-emerald-400">High (100 ppm)</strong></span>
                <span>Phenotype: <strong id="slide12Phenotype" class="text-white">Tall Plant</strong></span>
            </div>
        </div>

        <div id="slide12Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            The dominant gene 'T' produces an efficient enzyme that synthesizes abundant growth hormone, resulting in tall plants. An altered 't' gene produces a less efficient enzyme, synthesizing little hormone, leaving the plant dwarf.
        </div>
    </div>
    """,

    13: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔬</span> Chromosomal Mechanism of Heredity & Meiosis
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Homologous chromosome pairing, meiotic reduction division & fertilization restoration</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="runSlide13Meiosis()" class="px-3 py-1.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white text-xs font-semibold shadow-md transition-all">
                    Perform Meiosis (Reduction)
                </button>
                <button onclick="fuseSlide13Gametes()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Fertilize Zygote
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide13Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Somatic Body Cell</span>
                <span class="text-xs font-bold text-purple-400">Diploid (2n = 46 chr)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Germ Cell / Gamete</span>
                <span id="slide13GametePloidy" class="text-xs font-bold text-cyan-400">Haploid (n = 23 chr)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Zygote State</span>
                <span id="slide13ZygotePloidy" class="text-xs font-bold text-white">Restored Diploid (2n)</span>
            </div>
        </div>

        <div id="slide13Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Genes reside on discrete chromosomes organized in pairs. Meiotic cell division separates chromosome pairs so each gamete receives only one, and fertilization reunites them to restore the diploid number.
        </div>
    </div>
    """,

    14: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🦎</span> Environmental vs Genetic Sex Determination
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore temperature cues in reptiles, sex change in snails, and genetic cues in humans</p>
            </div>
            <div class="flex items-center gap-2">
                <select id="slide14SpeciesSelect" onchange="setSlide14Species(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-amber-500">
                    <option value="reptile">Reptiles: Incubation Temperature (Turtle / Crocodile)</option>
                    <option value="snail">Garden Snail: Flexible Non-Genetic Sex Change</option>
                    <option value="human">Humans: Strictly Genetic (XX / XY)</option>
                </select>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide14Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide14ControlArea" class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Nest Incubation Temperature: <span id="slide14TempDisplay" class="text-amber-400 font-bold">29°C</span></label>
                <input type="range" id="slide14TempSlider" min="24" max="34" value="29" oninput="setSlide14Temp(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Determined Sex: <strong id="slide14SexOutput" class="text-cyan-400">Mixed (50% M / 50% F)</strong></span>
                <span>Mechanism: <strong class="text-white">Environmental Cue</strong></span>
            </div>
        </div>

        <div id="slide14Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In some reptiles, cool incubation temperatures produce males while warm temperatures produce females. In contrast, human sex is strictly genetic and established at fertilization.
        </div>
    </div>
    """,

    15: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🗂️</span> Human Karyotype: 22 Autosomes + Sex Chromosomes
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Inspect the 23 chromosome pairs: Perfect XX female vs mismatched XY male</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide15Karyotype('female')" id="btnSlide15Female" class="px-3 py-1.5 rounded-xl bg-pink-600 text-white text-xs font-semibold shadow-md transition-all">
                    Female (44 + XX)
                </button>
                <button onclick="setSlide15Karyotype('male')" id="btnSlide15Male" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Male (44 + XY)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide15Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Autosomal Pairs</span>
                <span class="text-xs font-bold text-slate-200">22 Pairs (Identical M/F)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">23rd Sex Pair</span>
                <span id="slide15SexPairBadge" class="text-xs font-bold text-pink-400">XX (Homogametic)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Gametes Produced</span>
                <span id="slide15GameteBadge" class="text-xs font-bold text-emerald-400">100% X-bearing Eggs</span>
            </div>
        </div>

        <div id="slide15Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Human females have two full-sized X chromosomes (XX). Human males have a mismatched pair: one full-sized X and a noticeably shorter Y chromosome (XY).
        </div>
    </div>
    """,

    16: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>👶</span> Sex Inheritance Probability & Paternal Determination
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Punnett square analysis demonstrating exact 50-50 odds and father's genetic role</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="simulateSlide16Birth(1)" class="px-3 py-1.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold shadow-md transition-all">
                    Conceive Child
                </button>
                <button onclick="simulateSlide16Batch(20)" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Simulate 20 Births
                </button>
                <button onclick="resetSlide16Stats()" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 text-xs border border-slate-700 transition-all">
                    Reset
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide16Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Total Children</span>
                <span id="slide16TotalCount" class="text-sm font-bold text-white">0</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-pink-500/30">
                <span class="block text-[10px] text-pink-300">Girls (XX)</span>
                <span id="slide16GirlCount" class="text-sm font-bold text-pink-400">0 (50%)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-blue-500/30">
                <span class="block text-[10px] text-blue-300">Boys (XY)</span>
                <span id="slide16BoyCount" class="text-sm font-bold text-blue-400">0 (50%)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Paternal Role</span>
                <span class="text-xs font-bold text-emerald-400">Sperm Decides Sex</span>
            </div>
        </div>

        <div id="slide16Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Mothers only contribute X chromosomes. The father produces 50% X-bearing and 50% Y-bearing sperm. Therefore, the father's fertilizing sperm alone genetically determines the child's sex with an exact 50% probability!
        </div>
    </div>
    """
}

if __name__ == "__main__":
    with open(".agents/c10s_ch8_sims_part2.json", "w", encoding="utf-8") as f:
        json.dump(sims_part2, f, indent=2)
    print("Saved .agents/c10s_ch8_sims_part2.json successfully! (8 simulators)")

# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 7: How do Organisms Reproduce?
Simulators 9 to 16 HTML Generator
"""

import json

sims_part2 = {
    9: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌺</span> Complete Flower Anatomy & Whorl Explorer
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Interactive longitudinal section: Calyx, Corolla, Stamen & Carpel</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide9Whorl('all')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all">
                    All Whorls
                </button>
                <button onclick="setSlide9Whorl('stamen')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 transition-all">
                    Male Stamen
                </button>
                <button onclick="setSlide9Whorl('carpel')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-rose-300 border border-rose-500/30 transition-all">
                    Female Carpel
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide9Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide9Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Select a floral whorl above to inspect its anatomical structure, male anthers, or female ovule chambers.
        </div>
    </div>
    """,

    10: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌸</span> Pollination & Chemotropic Pollen Tube Growth
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Pollen landing on stigma, tube growth down style & gamete entry into ovule</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide10Tube()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                    <span>🌱</span> Germinate Pollen Tube
                </button>
                <button onclick="resetSlide10()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all">
                    Reset
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide10Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide10Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click <b>"Germinate Pollen Tube"</b> to observe chemotropic tube extension delivering male germ-cells down the style to the egg.
        </div>
    </div>
    """,

    11: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌱</span> Dicot Seed Structure & Seedling Germination
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Dissected gram bean seed (radicle, plumule, cotyledons) & seedling emergence</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide11View('anatomy')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-amber-300 border border-amber-500/30 transition-all">
                    Internal Seed Anatomy
                </button>
                <button onclick="setSlide11View('germinate')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Germinate Seedling
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide11Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide11Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Toggle between <b>"Internal Seed Anatomy"</b> and <b>"Germinate Seedling"</b> to view cotyledon reserves and radical/plumule elongation.
        </div>
    </div>
    """,

    12: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>⚡</span> Adolescent Puberty & Hormonal Signaling
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Pituitary gonadotropins, testosterone & estrogen secondary sexual adaptations</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide12Sex('male')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Male Puberty (Testosterone)
                </button>
                <button onclick="setSlide12Sex('female')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-rose-300 border border-rose-500/30 transition-all">
                    Female Puberty (Estrogen)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide12Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide12Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Select <b>"Male Puberty"</b> or <b>"Female Puberty"</b> to compare secondary sexual traits, hormonal triggers, and somatic changes.
        </div>
    </div>
    """,

    13: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🚹</span> Male Reproductive System & Sperm Anatomy
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Scrotum thermoregulation, vas deferens, prostate/seminal vesicles & motile sperm</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide13View('tract')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Reproductive Duct Tract
                </button>
                <button onclick="setSlide13View('sperm')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Sperm Cell Micro-Anatomy
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide13Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide13Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Explore the male duct system, scrotal thermoregulation (2–2.5°C cooler), or the streamlined DNA head and flagellar tail of a sperm.
        </div>
    </div>
    """,

    14: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🚺</span> Female Reproductive System & Ovulation
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Ovaries, ciliated fallopian tube fertilization site, muscular uterus & cervix</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide14Ovulation()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                    <span>🥚</span> Trigger Ovulation
                </button>
                <button onclick="resetSlide14()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all">
                    Reset
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide14Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide14Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click <b>"Trigger Ovulation"</b> to track the monthly release of an ovum into the fallopian tube (fertilization site).
        </div>
    </div>
    """,

    15: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🤰</span> Blastocyst Implantation & Placental Exchange
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Uterine wall embedding, embryonic villi, maternal blood spaces & 9-month gestation</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide15View('implant')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-rose-300 border border-rose-500/30 transition-all">
                    Uterine Implantation
                </button>
                <button onclick="setSlide15View('placenta')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 border border-cyan-500/30 transition-all">
                    Placenta Villi Exchange
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide15Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide15Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Examine how the blastocyst implants into the vascular uterine wall and how placental villi transfer oxygen and glucose to the fetus.
        </div>
    </div>
    """,

    16: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🛡️</span> Menstrual Cycle & Contraception Matrix
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">28-day endometrial shedding & barrier, hormonal, IUD and surgical contraception</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide16Mode('menstrual')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-rose-300 border border-rose-500/30 transition-all">
                    28-Day Menstrual Cycle
                </button>
                <button onclick="setSlide16Mode('contraception')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition-all">
                    Contraceptive Matrix
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide16Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide16Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Click <b>"28-Day Menstrual Cycle"</b> or <b>"Contraceptive Matrix"</b> to evaluate hormone cycles, barrier protection against STDs, and surgical methods.
        </div>
    </div>
    """
}

with open('.agents/c10s_ch7_sims_part2.json', 'w', encoding='utf-8') as f:
    json.dump(sims_part2, f, indent=2)

print("Simulators 9 to 16 successfully generated!")

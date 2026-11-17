#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Simulators 9 to 16 HTML markup for NCERT Class 10 Science Chapter 6: Control and Coordination.
"""

import json

sims_part2 = {
    9: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    Activity 6.2: Phototropism & Auxin Asymmetric Diffusion
                </h3>
                <p class="text-xs text-slate-400">Figure 6.5: Unilateral light induces lateral auxin migration to shaded flank, bending shoot tip</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide9Light('uniform')" id="s9BtnUni" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Uniform Light (Straight)</button>
                <button onclick="setSlide9Light('unilateral')" id="s9BtnUnilat" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all">Unilateral Light (Bending)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s9Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s9AuxinBox" class="space-y-2">
                    <span id="s9Title" class="font-bold text-amber-400 uppercase text-[10px] tracking-wider block">Asymmetric Auxin Distribution</span>
                    <p id="s9Desc" class="text-xs text-slate-300 leading-relaxed">
                        Light shines from one side. Auxin diffuses laterally to the shaded flank of the shoot tip, stimulating faster cell elongation and bending the shoot toward light.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1 text-[11px]">
                    <div class="flex justify-between"><span class="text-slate-400">Auxin Synthesis Site:</span><span class="text-emerald-300 font-bold">Shoot Growing Apical Tip</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Shaded Flank Growth:</span><span class="text-amber-300 font-bold">Accelerated Cell Elongation</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Root Phototropism:</span><span class="text-cyan-300 font-bold">Negative Phototropism (Away)</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Plant Phytohormone Quartet Dashboard
                </h3>
                <p class="text-xs text-slate-400">Compare physiological roles: Auxin, Gibberellin, Cytokinin, and Abscisic Acid (ABA)</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide10Hormone('auxin')" id="s10BtnAux" class="px-2 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all">Auxin</button>
                <button onclick="setSlide10Hormone('gibberellin')" id="s10BtnGib" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Gibberellin</button>
                <button onclick="setSlide10Hormone('cytokinin')" id="s10BtnCyto" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Cytokinin</button>
                <button onclick="setSlide10Hormone('aba')" id="s10BtnAba" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">ABA (Inhibitor)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s10Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s10DetailsBox" class="space-y-2">
                    <span id="s10Title" class="font-bold text-emerald-400 uppercase text-[10px] tracking-wider block">Auxin: Shoot Tip Cell Elongation</span>
                    <p id="s10Desc" class="text-xs text-slate-300 leading-relaxed">
                        Synthesized at shoot tips. Promotes cell elongation, apical growth dominance, and coordinates phototropic and gravitropic directional bending.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Promoters (3):</strong><span class="text-emerald-400 font-bold">Auxin, Gibberellin, Cytokinin</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Inhibitor (1):</strong><span class="text-rose-400 font-bold">Abscisic Acid (ABA)</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                    Endocrine Ductless Gland Secretion & Blood Distribution
                </h3>
                <p class="text-xs text-slate-400">Ductless gland capillary hormone discharge vs point-to-point axonal electrical wiring</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide11Mode('endocrine')" id="s11BtnEndo" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all">Endocrine (Blood Delivery)</button>
                <button onclick="setSlide11Mode('neural')" id="s11BtnNeural" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Neural (Axonal Wiring)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s11Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s11Details" class="space-y-2">
                    <span id="s11Title" class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider block">Endocrine Ductless Delivery</span>
                    <p id="s11Desc" class="text-xs text-slate-300 leading-relaxed">
                        Endocrine glands lack ducts and release hormones directly into blood capillaries. Circulating blood delivers them body-wide to target cells expressing specific matching receptors.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Speed:</strong><span id="s11Speed" class="text-amber-300 font-bold">Gradual / Sustained</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Reach:</strong><span id="s11Reach" class="text-emerald-300 font-bold">Whole-Body Target Cells</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
                    Adrenaline Emergency (Fight-or-Flight) Simulator
                </h3>
                <p class="text-xs text-slate-400">Trigger adrenal gland adrenaline release and observe simultaneous whole-body physiological adaptations</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide12Adrenaline()" id="s12AdrenalineBtn" class="px-3 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-slate-950 font-bold text-xs transition-all">
                    Trigger Threat (Adrenaline Surge) ⚡
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s12Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span class="font-bold text-rose-400 uppercase text-[10px] tracking-wider">Physiological Status</span>
                        <span id="s12StatusBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300">Resting Baseline</span>
                    </div>
                    <p id="s12StatusDesc" class="text-xs text-slate-300 leading-relaxed">
                        Heart beats normally, blood flows evenly to digestive organs and skin, breathing is steady, and liver stores glucose as glycogen.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Heart Rate:</strong><span id="s12HR" class="text-cyan-400 font-mono font-bold">72 BPM (Resting)</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Blood Flow:</strong><span id="s12BF" class="text-emerald-400 font-bold">Digestive & Skin Normal</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    Pituitary Growth Hormone & Thyroid Iodine Dynamics
                </h3>
                <p class="text-xs text-slate-400">Figure 6.7: Pituitary Growth Hormone balance (Dwarfism vs Gigantism) and Thyroid Thyroxin Goitre</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide13Gland('thyroid')" id="s13BtnThyroid" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all">Thyroid (Iodine/Goitre)</button>
                <button onclick="setSlide13Gland('pituitary')" id="s13BtnPituitary" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Pituitary (Growth Hormone)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s13Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s13GlandBox" class="space-y-2">
                    <span id="s13Title" class="font-bold text-amber-400 uppercase text-[10px] tracking-wider block">Thyroid Gland: Thyroxin & Iodine</span>
                    <p id="s13Desc" class="text-xs text-slate-300 leading-relaxed">
                        Thyroid gland in neck synthesizes thyroxin to regulate carbohydrate, protein, and fat metabolism. Dietary iodine deficiency causes gland enlargement (Goitre).
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Nutritional Mandate:</span><span class="text-amber-300 font-bold">Iodized Table Salt</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Pituitary GH Deficit:</span><span class="text-rose-400 font-bold">Dwarfism</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Pituitary GH Excess:</span><span class="text-cyan-400 font-bold">Gigantism</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-purple-400"></span>
                    Gonadal Puberty Hormones: Testosterone & Oestrogen
                </h3>
                <p class="text-xs text-slate-400">Adolescent puberty maturation at 10-12 years: male and female secondary sexual traits</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide14Gonad('male')" id="s14BtnMale" class="px-2.5 py-1 rounded-lg bg-purple-600 text-slate-950 font-bold text-xs transition-all">Testes (Testosterone)</button>
                <button onclick="setSlide14Gonad('female')" id="s14BtnFemale" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Ovaries (Oestrogen)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s14Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s14DetailsBox" class="space-y-2">
                    <span id="s14Title" class="font-bold text-purple-400 uppercase text-[10px] tracking-wider block">Male Puberty: Testes & Testosterone</span>
                    <p id="s14Desc" class="text-xs text-slate-300 leading-relaxed">
                        Testes in scrotum secrete testosterone around ages 10-12 years. Promotes sperm production, vocal deepening, facial/body hair, and muscular shoulder broadening.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Puberty Onset:</span><span class="text-purple-300 font-bold">10 - 12 Years</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Female Hormone:</span><span class="text-rose-400 font-bold">Oestrogen & Progesterone</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Cyclic Function:</span><span class="text-cyan-300 font-bold">28-Day Menstrual Cycle</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Pancreas Insulin & Negative Feedback Closed Loop
                </h3>
                <p class="text-xs text-slate-400">Observe meal carbohydrate intake, blood sugar spike, insulin secretion, and automatic feedback shut-off</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide15Meal()" id="s15MealBtn" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs transition-all">
                    Consume Meal (Glucose Inrush) 🍞
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s15Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span class="font-bold text-emerald-400 uppercase text-[10px] tracking-wider">Feedback Phase</span>
                        <span id="s15PhaseBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300">Homeostasis (Normal)</span>
                    </div>
                    <p id="s15PhaseDesc" class="text-xs text-slate-300 leading-relaxed">
                        Blood glucose is within normal resting range (~ 90 mg/dL). Pancreas maintains minimal baseline insulin release.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Blood Glucose:</strong><span id="s15SugarVal" class="text-emerald-400 font-mono font-bold">90 mg/dL</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Insulin Rate:</strong><span id="s15InsulinVal" class="text-cyan-400 font-bold">Low Baseline</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                    Control & Coordination Integration Matrix
                </h3>
                <p class="text-xs text-slate-400">Comparative synthesis: Nervous electrical speed vs Endocrine systemic breadth across animals and plants</p>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs text-slate-300">
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
                <strong class="text-cyan-400 uppercase text-[10px] tracking-wider block">1. Nervous System</strong>
                <ul class="space-y-1 text-[11px] text-slate-300">
                    <li>• Medium: Electrical action potentials + synapses</li>
                    <li>• Speed: Milliseconds (Lightning fast)</li>
                    <li>• Scope: Point-to-point innervated cells</li>
                    <li>• Duration: Brief, instantaneous action</li>
                </ul>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
                <strong class="text-amber-400 uppercase text-[10px] tracking-wider block">2. Endocrine System</strong>
                <ul class="space-y-1 text-[11px] text-slate-300">
                    <li>• Medium: Chemical hormones in blood</li>
                    <li>• Speed: Slower initiation (minutes/hours)</li>
                    <li>• Scope: Widespread target organ receptors</li>
                    <li>• Duration: Sustained, prolonged development</li>
                </ul>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
                <strong class="text-emerald-400 uppercase text-[10px] tracking-wider block">3. Plant Coordination</strong>
                <ul class="space-y-1 text-[11px] text-slate-300">
                    <li>• Medium: Phytohormones (Auxin, ABA, etc.)</li>
                    <li>• Hydraulic: Pulvinus turgor pressure shifts</li>
                    <li>• Growth Tropisms: Light, gravity, touch</li>
                    <li>• Homeostasis: Closed feedback loops</li>
                </ul>
            </div>
        </div>
    </div>
    """
}

with open('.agents/c10s_ch6_sims_part2.json', 'w', encoding='utf-8') as f:
    json.dump(sims_part2, f, indent=2)

print("Simulators 9 to 16 successfully generated!")

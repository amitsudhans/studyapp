#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Simulators 9 to 16 HTML markup for NCERT Class 10 Science Chapter 5: Life Processes.
"""

import json

sims_part2 = {
    9: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>
                    Gastric Secretions, Bile Emulsification & Microscopic Villi
                </h3>
                <p class="text-xs text-slate-400">Step through the stomach, liver bile fat emulsification, and intestinal villus absorption</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide9Section('stomach')" id="s9BtnStomach" class="px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all">Stomach & HCl</button>
                <button onclick="setSlide9Section('bile')" id="s9BtnBile" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Liver Bile & Pancreas</button>
                <button onclick="setSlide9Section('villi')" id="s9BtnVilli" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Intestinal Villi</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s9Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s9InfoBox" class="space-y-2">
                    <span id="s9Title" class="font-bold text-rose-400 uppercase text-[10px] tracking-wider block">Stomach: HCl, Pepsin & Mucus</span>
                    <p id="s9Desc" class="text-xs text-slate-300 leading-relaxed">
                        Gastric glands secrete HCl (creates acidic pH 2 and kills bacteria), pepsin (digests proteins), and mucus (shields gastric lining from acid corrosion).
                    </p>
                </div>
                <div class="grid grid-cols-3 gap-1.5 text-[10px] text-center">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Stomach pH:</strong><span class="text-rose-400 font-bold">1.5 - 2.0 (Acidic)</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Duodenum pH:</strong><span class="text-emerald-400 font-bold">7.8 - 8.4 (Alkaline)</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Villi Area:</strong><span class="text-cyan-400 font-bold">> 30 m² Absorptive</span></div>
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
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    Glucose Breakdown Pathways & Respiration Tests
                </h3>
                <p class="text-xs text-slate-400">Figure 5.8: Glycolysis to Pyruvate, Yeast Anaerobic, Muscle Cramps, and Aerobic Mitochondria</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide10Pathway('aerobic')" id="s10BtnAero" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all">Aerobic (Mitochondria)</button>
                <button onclick="setSlide10Pathway('muscle')" id="s10BtnMuscle" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Muscle Oxygen Lack</button>
                <button onclick="setSlide10Pathway('yeast')" id="s10BtnYeast" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Yeast Fermentation</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s10Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s10PathwayBox" class="space-y-2">
                    <span id="s10Title" class="font-bold text-emerald-400 uppercase text-[10px] tracking-wider block">Aerobic Respiration in Mitochondria</span>
                    <p id="s10Desc" class="text-xs text-slate-300 leading-relaxed">
                        In the presence of oxygen, 3-carbon pyruvate is oxidized completely inside mitochondria into carbon dioxide, water, and 38 ATP molecules.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1 text-[11px]">
                    <div class="flex justify-between"><span class="text-slate-400">Universal First Step:</span><span class="text-cyan-300 font-bold font-mono">Cytoplasmic Glycolysis (6C -> 2x 3C)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Energy Released:</span><span id="s10EnergyOut" class="text-emerald-400 font-bold font-mono">38 ATP (~30.5 kJ/mol per ATP)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Activity 5.4 Proof:</span><span class="text-amber-300">Exhaled air turns limewater milky fast!</span></div>
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
                    Gas Exchange Systems: Plants & Aquatic Gills
                </h3>
                <p class="text-xs text-slate-400">Day/Night stomatal gas reversal and aquatic gill counter-current extraction</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide11View('day')" id="s11BtnDay" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all">Plant Daylight (O2 Out)</button>
                <button onclick="setSlide11View('night')" id="s11BtnNight" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Plant Night (CO2 Out)</button>
                <button onclick="setSlide11View('fish')" id="s11BtnFish" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Aquatic Fish Gills</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s11Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s11DetailsBox" class="space-y-2">
                    <span id="s11Title" class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider block">Plant Daylight Gas Exchange</span>
                    <p id="s11Desc" class="text-xs text-slate-300 leading-relaxed">
                        Photosynthesis operates at high speed, consuming all respiratory CO2 internally and releasing large volumes of surplus oxygen through stomata into the air.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Aquatic O2 Challenge:</span><span class="text-amber-300 font-semibold">Low dissolved oxygen in water</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Fish Breathing Rate:</span><span class="text-rose-400 font-bold">Fast Gill Ventilation</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Terrestrial Advantage:</span><span class="text-emerald-400 font-bold">21% O2 in atmosphere</span></div>
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
                    <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                    Human Respiratory System & Alveolar Diffusion
                </h3>
                <p class="text-xs text-slate-400">Figure 5.9: Cartilaginous rings, thoracic inhalation mechanics, and 80 m² alveolar capillary exchange</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="toggleSlide12Breath()" id="s12BreathBtn" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold text-xs transition-all">
                    Inhale (Expand Chest)
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
                        <span class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider">Breathing Phase</span>
                        <span id="s12PhaseBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300">Exhaling / Resting</span>
                    </div>
                    <p id="s12PhaseDesc" class="text-xs text-slate-300 leading-relaxed">
                        Inhalation: Diaphragm flattens downward, ribs lift outward, expanding thoracic cavity and sucking air into alveoli.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Alveoli Area:</strong><span class="text-cyan-400 font-mono font-bold">~ 80 m² (Tennis Court)</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Trachea Support:</strong><span class="text-amber-400 font-bold">C-Shaped Cartilage</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Oxygen Carrier:</strong><span class="text-rose-400 font-bold">RBC Haemoglobin</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Residual Air:</strong><span class="text-emerald-400 font-bold">Always Present</span></div>
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
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
                    4-Chambered Human Heart Pumping Simulator
                </h3>
                <p class="text-xs text-slate-400">Figures 5.10 & 5.11: Right & left atria, ventricles, valves, and systemic/pulmonary outflow</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="stepSlide13Heart()" id="s13PumpBtn" class="px-3 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-slate-950 font-bold text-xs transition-all">
                    Step Cardiac Cycle (Beat) →
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s13Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span class="font-bold text-rose-400 uppercase text-[10px] tracking-wider">Current Pumping Phase</span>
                        <span id="s13PhaseBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300">Phase 1: Atrial Filling</span>
                    </div>
                    <div id="s13Title" class="font-bold text-white text-sm">Atria Receive Blood</div>
                    <p id="s13Desc" class="text-xs text-slate-300 leading-relaxed">
                        Right atrium collects deoxygenated blood from vena cava; left atrium collects oxygenated blood from pulmonary veins.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Left Ventricle Wall:</span><span class="text-rose-400 font-bold">Thick Myocardium (High Pressure)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Valves (Tricuspid/Bicuspid):</span><span class="text-amber-300 font-bold">Prevent Backward Regurgitation</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Warm-Blooded Advantage:</span><span class="text-emerald-400 font-bold">Zero Blood Mixing</span></div>
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
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>
                    Double Circulation, Blood Vessels & Pressure
                </h3>
                <p class="text-xs text-slate-400">Arteries vs Veins vs Capillaries, Platelet Clotting, and Sphygmomanometer (120/80 mm Hg)</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide14View('circuit')" id="s14BtnCircuit" class="px-2.5 py-1 rounded-lg bg-rose-600 text-slate-950 font-bold text-xs transition-all">Double Circuit</button>
                <button onclick="setSlide14View('vessels')" id="s14BtnVessels" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Artery vs Vein</button>
                <button onclick="setSlide14View('clot')" id="s14BtnClot" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Platelet Plug</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s14Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s14InfoBox" class="space-y-2">
                    <span id="s14Title" class="font-bold text-rose-400 uppercase text-[10px] tracking-wider block">Vertebrate Double Circulation</span>
                    <p id="s14Desc" class="text-xs text-slate-300 leading-relaxed">
                        Blood passes through the heart twice per complete body circuit: once through the pulmonary circuit (to lungs) and once through the systemic circuit (to body).
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Systolic Pressure:</strong><span class="text-emerald-400 font-mono font-bold">~ 120 mm Hg</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Diastolic Pressure:</strong><span class="text-cyan-400 font-mono font-bold">~ 80 mm Hg</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Artery Walls:</strong><span class="text-rose-300 font-bold">Thick, Elastic, No Valves</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Vein Walls:</strong><span class="text-amber-300 font-bold">Thin, Internal Flap Valves</span></div>
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
                    Plant Vascular Transport: Xylem & Phloem
                </h3>
                <p class="text-xs text-slate-400">Activity 5.8 & Figure 5.12: Transpiration pull in xylem vs ATP sucrose translocation in phloem</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide15System('xylem')" id="s15BtnXylem" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all">Xylem (Transpiration Pull)</button>
                <button onclick="setSlide15System('phloem')" id="s15BtnPhloem" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Phloem (Sucrose ATP)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s15Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s15Details" class="space-y-2">
                    <span id="s15Title" class="font-bold text-emerald-400 uppercase text-[10px] tracking-wider block">Xylem Water Ascent (Transpiration Pull)</span>
                    <p id="s15Desc" class="text-xs text-slate-300 leading-relaxed">
                        Daytime water evaporation from stomata generates negative suction tension that pulls continuous water columns upward through tracheids and vessel elements to tall treetops.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Night Mechanism:</span><span class="text-amber-300 font-bold">Osmotic Root Pressure</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Day Mechanism:</span><span class="text-emerald-400 font-bold">Transpiration Suction Pull</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Phloem Translocation:</span><span class="text-cyan-300 font-bold">Active ATP Osmotic Pressure Flow</span></div>
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
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    Human Nephron Filtration & Plant Excretion
                </h3>
                <p class="text-xs text-slate-400">Figure 5.14: Glomerular ultrafiltration, 180 L to 1-2 L selective reabsorption & hemodialysis</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide16Tab('nephron')" id="s16BtnNephron" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all">Nephron Filtration</button>
                <button onclick="setSlide16Tab('dialysis')" id="s16BtnDialysis" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Hemodialysis</button>
                <button onclick="setSlide16Tab('plant')" id="s16BtnPlant" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Plant Excretion</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s16Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s16Details" class="space-y-2">
                    <span id="s16Title" class="font-bold text-amber-400 uppercase text-[10px] tracking-wider block">Nephron: Glomerulus & Tubule (Figure 5.14)</span>
                    <p id="s16Desc" class="text-xs text-slate-300 leading-relaxed">
                        High blood pressure forces 180 L of initial filtrate into Bowman's capsule daily. The long coiled tubule reabsorbs >99% of water, glucose, and salts, leaving 1-2 L of concentrated urine.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Initial Filtrate:</strong><span class="text-cyan-400 font-mono font-bold">180 L / Day</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Actual Urine:</strong><span class="text-amber-400 font-mono font-bold">1 - 2 L / Day</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Reabsorption:</strong><span class="text-emerald-400 font-bold">> 99% Selective</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Hemodialysis:</strong><span class="text-rose-400 font-bold">No Reabsorption</span></div>
                </div>
            </div>
        </div>
    </div>
    """
}

with open('.agents/c10s_ch5_sims_part2.json', 'w', encoding='utf-8') as f:
    json.dump(sims_part2, f, indent=2)

print("Simulators 9 to 16 successfully generated!")

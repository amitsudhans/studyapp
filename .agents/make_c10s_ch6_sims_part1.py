#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Simulators 1 to 8 HTML markup for NCERT Class 10 Science Chapter 6: Control and Coordination.
"""

import json

sims_part1 = {
    1: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-indigo-400"></span>
                    Growth-Linked vs Non-Growth Biological Movements
                </h3>
                <p class="text-xs text-slate-400">Compare slow directional developmental growth with rapid behavioral animal locomotion</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide1Movement('growth')" id="s1BtnGrowth" class="px-2.5 py-1 rounded-lg bg-indigo-600 text-slate-950 font-bold text-xs transition-all">Growth-Related (Seedling)</button>
                <button onclick="setSlide1Movement('nongrowth')" id="s1BtnNonGrowth" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Non-Growth (Running Cat)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s1Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s1DescBox" class="space-y-2">
                    <span id="s1Title" class="font-bold text-indigo-400 uppercase text-[10px] tracking-wider block">Growth-Related Movement (Seedling)</span>
                    <p id="s1Desc" class="text-xs text-slate-300 leading-relaxed">
                        A germinating seed pushes soil particles aside as its hypocotyl elongates. If biological growth ceases, this directional movement stops permanently.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1 text-[11px]">
                    <div class="flex justify-between"><span class="text-slate-400">Movement Nature:</span><span id="s1Type" class="text-indigo-300 font-bold">Slow Directional Growth</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Reversibility:</span><span id="s1Rev" class="text-amber-300 font-bold">Irreversible Cellular Elongation</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Trigger Advantage:</span><span id="s1Adv" class="text-emerald-300 font-bold">Reaching sunlight & soil nutrients</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                    Neuron Anatomy, Action Potentials & Synaptic Cleft
                </h3>
                <p class="text-xs text-slate-400">Figure 6.1: Dendritic chemical-to-electrical transduction, axonal propagation, and neurotransmitter diffusion</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide2Impulse()" id="s2ImpulseBtn" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold text-xs transition-all">
                    Fire Electrical Impulse ⚡
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s2Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <span class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider block">Neural Signal Progression</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Dendritic tip acquires sensory stimuli -> chemical reaction creates electrical impulse -> propagates across cell body and axon -> terminal releases chemical neurotransmitters across synapse.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Gustatory Receptors:</span><span class="text-amber-300 font-bold">Tongue (Taste)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Olfactory Receptors:</span><span class="text-emerald-300 font-bold">Nose (Smell / Aroma)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Activity 6.1 Proof:</span><span class="text-cyan-300">Blocked nose impairs flavor appreciation!</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>
                    Spinal Reflex Arc Emergency Circuit
                </h3>
                <p class="text-xs text-slate-400">Figure 6.2: Heat stimulus, receptor, sensory neuron, spinal relay interneuron, motor neuron, and effector muscle</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide3Reflex()" id="s3ReflexBtn" class="px-3 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-slate-950 font-bold text-xs transition-all">
                    Touch Hot Object 🔥
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s3Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span class="font-bold text-rose-400 uppercase text-[10px] tracking-wider">Reflex Arc Sequence</span>
                        <span id="s3ReflexBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300">Ready</span>
                    </div>
                    <p id="s3ReflexDesc" class="text-xs text-slate-300 leading-relaxed">
                        Thermal pain receptors in skin activate sensory neuron -> enters spinal cord -> synapses with relay neuron -> motor neuron instantly triggers arm biceps contraction!
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    <strong class="text-white block mb-0.5">Evolutionary Urgency:</strong>
                    Direct spinal sensory-to-motor relay executes hand withdrawal in &lt; 20 milliseconds, avoiding severe tissue burning from slow conscious cerebral delays.
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-purple-400"></span>
                    Human Brain Anatomy & Major Centers
                </h3>
                <p class="text-xs text-slate-400">Figure 6.3: Fore-Brain (Cerebrum & Hunger Center), Mid-Brain, and Hind-Brain (Pons, Medulla, Cerebellum)</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide4BrainRegion('forebrain')" id="s4BtnFore" class="px-2.5 py-1 rounded-lg bg-purple-600 text-slate-950 font-bold text-xs transition-all">Fore-Brain (Cerebrum)</button>
                <button onclick="setSlide4BrainRegion('midbrain')" id="s4BtnMid" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Mid-Brain</button>
                <button onclick="setSlide4BrainRegion('hindbrain')" id="s4BtnHind" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Hind-Brain</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s4Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s4RegionBox" class="space-y-2">
                    <span id="s4Title" class="font-bold text-purple-400 uppercase text-[10px] tracking-wider block">Fore-Brain (Cerebrum & Hunger Center)</span>
                    <p id="s4Desc" class="text-xs text-slate-300 leading-relaxed">
                        The cerebrum is the main cognitive thinking part of the brain. It contains sensory receiving areas (hearing, smell, vision), association areas linking sensations with stored memories, and motor command areas.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Central System:</strong><span class="text-purple-300 font-bold">Brain + Spinal Cord</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Peripheral System:</strong><span class="text-cyan-300 font-bold">12 Cranial + 31 Spinal Nerves</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Voluntary vs Involuntary Motor Coordinator
                </h3>
                <p class="text-xs text-slate-400">Cerebellar posture & precision vs medullary autonomic control (BP, salivation, vomiting)</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide5Type('cerebellum')" id="s5BtnCereb" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all">Cerebellum (Balance)</button>
                <button onclick="setSlide5Type('medulla')" id="s5BtnMed" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Medulla (Involuntary)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s5Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s5InfoBox" class="space-y-2">
                    <span id="s5Title" class="font-bold text-emerald-400 uppercase text-[10px] tracking-wider block">Cerebellum: Precision, Posture & Equilibrium</span>
                    <p id="s5Desc" class="text-xs text-slate-300 leading-relaxed">
                        While voluntary actions are initiated by the cerebrum, the cerebellum coordinates precision: riding a bicycle, walking in a straight line, and picking up a pencil with fine dexterity.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Voluntary Example:</span><span class="text-emerald-300 font-bold">Conscious writing / talking</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Involuntary Example:</span><span class="text-rose-400 font-bold">Pupil reflex, heartbeat, peristalsis</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-blue-400"></span>
                    Nervous Armor & Muscle Protein Contraction
                </h3>
                <p class="text-xs text-slate-400">Bony cranium skull, cerebrospinal fluid (CSF) shock absorber & sliding actin-myosin filaments</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide6View('armor')" id="s6BtnArmor" class="px-2.5 py-1 rounded-lg bg-blue-600 text-slate-950 font-bold text-xs transition-all">Cranium & CSF Armor</button>
                <button onclick="setSlide6View('muscle')" id="s6BtnMuscle" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Muscle Protein Contraction</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s6Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s6DetailsBox" class="space-y-2">
                    <span id="s6Title" class="font-bold text-blue-400 uppercase text-[10px] tracking-wider block">Bony Cranium & Cerebrospinal Fluid (CSF)</span>
                    <p id="s6Desc" class="text-xs text-slate-300 leading-relaxed">
                        The brain is protected by a tough bony box (cranium) and cushioned inside a balloon filled with shock-absorbing cerebrospinal fluid (CSF). The spinal cord is protected by the vertebral backbone.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    <strong class="text-white block mb-0.5">Muscle Movement Mechanism:</strong>
                    When an impulse arrives, specialized muscle proteins change shape and spatial arrangement, causing cells to shorten physically and execute movement.
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Mimosa pudica (Touch-Me-Not) Nastic Drooping
                </h3>
                <p class="text-xs text-slate-400">Figure 6.4: Electrical-chemical communication and pulvinus hydraulic turgor loss independent of growth</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="touchSlide7Leaf()" id="s7TouchBtn" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs transition-all">
                    Touch Leaflet 🍃
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s7Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span class="font-bold text-emerald-400 uppercase text-[10px] tracking-wider">Leaf State</span>
                        <span id="s7StateBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300">Open & Turgid</span>
                    </div>
                    <p id="s7StateDesc" class="text-xs text-slate-300 leading-relaxed">
                        Plant cells communicate touch through electrical-chemical signals. Movement occurs by shifting water content: cells in the pulvinus swell or shrink, folding the leaves rapidly.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Response Speed:</span><span class="text-emerald-300 font-bold">&lt; 1 Second (Immediate)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Growth Dependency:</span><span class="text-amber-300 font-bold">Independent of Growth (Nastic)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Hinge Structure:</span><span class="text-cyan-300 font-bold">Pulvinus (Swollen Base)</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-teal-400"></span>
                    Plant Directional Tropisms Laboratory
                </h3>
                <p class="text-xs text-slate-400">Directional growth responses: Thigmotropism, Geotropism (Fig 6.6), Hydrotropism & Chemotropism</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide8Tropism('thigmo')" id="s8BtnThigmo" class="px-2.5 py-1 rounded-lg bg-teal-600 text-slate-950 font-bold text-xs transition-all">Thigmo (Tendril)</button>
                <button onclick="setSlide8Tropism('geo')" id="s8BtnGeo" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Geo (Gravity)</button>
                <button onclick="setSlide8Tropism('chemo')" id="s8BtnChemo" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Chemo (Pollen)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s8Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s8TropismBox" class="space-y-2">
                    <span id="s8Title" class="font-bold text-teal-400 uppercase text-[10px] tracking-wider block">Thigmotropism: Climbing Pea Tendril</span>
                    <p id="s8Desc" class="text-xs text-slate-300 leading-relaxed">
                        When a tendril touches a support, cells away from the support grow much faster than cells in contact, causing the tendril to circle and coil tightly around the stake.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Roots:</strong><span class="text-emerald-400 font-bold">Positive Geotropism (+)</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Shoots:</strong><span class="text-cyan-400 font-bold">Negative Geotropism (-)</span></div>
                </div>
            </div>
        </div>
    </div>
    """
}

with open('.agents/c10s_ch6_sims_part1.json', 'w', encoding='utf-8') as f:
    json.dump(sims_part1, f, indent=2)

print("Simulators 1 to 8 successfully generated!")

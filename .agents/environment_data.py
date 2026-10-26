# -*- coding: utf-8 -*-
"""
Data definition for NCERT Class 10 Science, Chapter 13: Our Environment.
Covers every sentence, activity (13.1 to 13.9), diagram (13.1 to 13.4), in-text questions,
and end-of-chapter exercises (Q1 to Q9) from the official textbook (Pages 208-217).
Total: 16 Content Slides (with 32 checkpoints) + 4 Dedicated Quiz Challenge Slides (40 questions with popup solutions).
"""

CONTENT_SLIDES = [
    # Slide 1: Ecosystem & Its Components
    {
        "id": 1,
        "title": "13.1 Ecosystem — What Are Its Components?",
        "subtitle": "Biotic Organisms, Abiotic Surroundings & Natural vs Artificial Systems",
        "narration": "Welcome to Chapter 13: Our Environment! An ecosystem consists of all interacting organisms in an area together with non-living physical surroundings. Biotic factors comprise living plants, animals, microbes, and humans, while abiotic factors include temperature, rainfall, wind, soil, and minerals. Natural ecosystems like forests, ponds, and lakes sustain themselves naturally, whereas gardens, crop-fields, and aquariums are human-made artificial ecosystems.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    All living organisms such as plants, animals, microorganisms, and human beings interact with one another and with their physical surroundings to maintain balance in nature. An <strong class="text-emerald-400">ecosystem</strong> is the structural and functional unit of the biosphere comprising both living organisms and the non-living physical environment.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 text-sm mb-2 flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                            Biotic Components (Living)
                        </h4>
                        <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300">
                            <li><strong class="text-emerald-300">Producers:</strong> Green plants and photosynthetic bacteria synthesizing food.</li>
                            <li><strong class="text-emerald-300">Consumers:</strong> Animals, insects, and humans feeding on other organisms.</li>
                            <li><strong class="text-emerald-300">Decomposers:</strong> Fungi and bacteria breaking down dead remains.</li>
                        </ul>
                    </div>
                    <div class="p-4 rounded-xl bg-slate-900 border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 text-sm mb-2 flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyan-500"></span>
                            Abiotic Components (Non-Living)
                        </h4>
                        <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300">
                            <li><strong class="text-cyan-300">Climatic factors:</strong> Temperature, sunlight, rainfall, and wind.</li>
                            <li><strong class="text-cyan-300">Edaphic factors:</strong> Soil texture, soil pH, moisture, and minerals.</li>
                            <li><strong class="text-cyan-300">Inorganic substances:</strong> Water, oxygen, carbon dioxide, and nitrogen salts.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
                    <h4 class="text-xs font-bold text-amber-300 mb-1">Ecosystem Classification & Activity 13.1 (Designing an Aquarium):</h4>
                    <p class="text-xs text-slate-400">
                        <strong>Natural Ecosystems:</strong> Forests, grasslands, deserts, ponds, lakes, and oceans operated by natural regulatory cycles.<br>
                        <strong>Artificial (Human-Made) Ecosystems:</strong> Gardens, agricultural crop-fields, and aquariums. In Activity 13.1, when designing an artificial aquarium, fish require sufficient swimming volume, clean water, an aeration pump (aerator) for continuous dissolved oxygen, and commercial fish food. Because it lacks a natural balanced food web and scavenger network, an aquarium requires regular artificial cleaning and maintenance!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following is classified as an artificial (human-made) ecosystem according to NCERT Section 13.1?",
                "options": [
                    "Freshwater pond",
                    "Dense deciduous forest",
                    "Crop-field of wheat",
                    "Natural deep-water lake"
                ],
                "ans": 2,
                "explanation": "Ponds, lakes, and forests are natural ecosystems, whereas crop-fields, gardens, and aquariums are artificial (man-made) ecosystems maintained by human intervention."
            },
            {
                "question": "In Activity 13.1, why does a home aquarium require periodic manual cleaning while a natural pond does not?",
                "options": [
                    "Ponds do not contain fish feces or decaying leaves",
                    "Ponds have natural decomposers and balanced self-sustaining biogeochemical cycles",
                    "Ponds have artificial aeration pumps hidden beneath the mud",
                    "Ponds contain only abiotic components without any biotic organisms"
                ],
                "ans": 1,
                "explanation": "Natural ponds are self-sustaining ecosystems where bacteria, fungi, and aquatic scavengers naturally decompose organic waste and recycle nutrients. An artificial aquarium lacks this complete natural cycle and accumulates toxic ammonia if not cleaned."
            }
        ]
    },

    # Slide 2: Producers, Consumers & Decomposers
    {
        "id": 2,
        "title": "Producers, Consumers & Decomposers",
        "subtitle": "Trophic Classification & The Essential Role of Saprophytic Microorganisms",
        "narration": "Organisms are grouped into producers, consumers, and decomposers based on how they obtain sustenance. Producers, like green plants, make organic food from sunlight via photosynthesis. Consumers depend directly or indirectly on producers and include herbivores, carnivores, omnivores, and parasites. Decomposers, consisting of bacteria and fungi, break down dead organic remains into simple inorganic substances, replenishing the soil.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    All living organisms in an ecosystem are categorised into three functional groups based on their nutritional mode:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-emerald-500/30">
                        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wide">1. Producers (Autotrophs)</span>
                        <p class="text-xs text-slate-300 mt-1.5">
                            Organisms that synthesize complex organic compounds (glucose, starch) from simple inorganic substances ($CO_2$, $H_2O$) using the radiant energy of the Sun in the presence of chlorophyll. Includes all green plants, blue-green algae (cyanobacteria), and photosynthetic bacteria.
                        </p>
                    </div>
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                        <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">2. Consumers (Heterotrophs)</span>
                        <p class="text-xs text-slate-300 mt-1.5">
                            Organisms that consume organic food directly from producers or indirectly by feeding on other consumers:
                            <br>• <strong>Herbivores:</strong> Plant-eaters (deer, rabbit).
                            <br>• <strong>Carnivores:</strong> Flesh-eaters (lion, frog).
                            <br>• <strong>Omnivores:</strong> Plants & meat (human, crow).
                            <br>• <strong>Parasites:</strong> Live on/in host without killing immediately (Cuscuta, leeches, tapeworms).
                        </p>
                    </div>
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-violet-500/30">
                        <span class="text-xs font-bold text-violet-400 uppercase tracking-wide">3. Decomposers (Saprophytes)</span>
                        <p class="text-xs text-slate-300 mt-1.5">
                            Microorganisms comprising bacteria and fungi that secrete enzymes to break down complex organic molecules in dead plants, animal carcasses, and excretory waste into simple inorganic minerals, returning them to soil and water for reabsorption by plant root systems.
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/90 border border-rose-500/30">
                    <h4 class="text-xs font-bold text-rose-300 mb-1">Critical NCERT Thought Experiment: What Happens in the Absence of Decomposers?</h4>
                    <p class="text-xs text-slate-300">
                        If decomposers were absent, dead bodies of plants and animals, fallen leaves, and animal excreta would pile up indefinitely across the planet. Nutrients like carbon, nitrogen, and phosphorus locked inside dead organic matter would never be released back into the soil, halting plant growth, depleting soil fertility, and causing the entire biosphere to collapse!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following organisms can convert radiant solar energy into chemical organic food using chlorophyll?",
                "options": [
                    "Rhizopus bread mould",
                    "Cuscuta (Amarbel) parasitic plant",
                    "Blue-green algae (Cyanobacteria)",
                    "Earthworm scavenger"
                ],
                "ans": 2,
                "explanation": "Blue-green algae and green plants possess chlorophyll and are autotrophic producers that synthesize organic compounds using solar energy."
            },
            {
                "question": "What primary ecological function do bacteria and fungi perform in an ecosystem?",
                "options": [
                    "They fix 100% of solar radiation into chemical ATP energy",
                    "They break down complex organic remains into simple inorganic substances for soil replenishment",
                    "They act as primary consumers feeding directly on green leaves",
                    "They convert oxygen into ozone at ground level"
                ],
                "ans": 1,
                "explanation": "Bacteria and fungi are decomposers that mineralize dead organic biomass into simple inorganic nutrients (nitrates, phosphates) used again by autotrophs."
            }
        ]
    },

    # Slide 3: Food Chains & Trophic Levels
    {
        "id": 3,
        "title": "13.1.1 Food Chains & Trophic Levels",
        "subtitle": "Sequential Feeding Links & The Stepped Energy Architecture of Ecosystems",
        "narration": "A food chain is a series of organisms where each step feeds on the preceding organism. Each step or level in a food chain constitutes a trophic level. Autotrophs or producers occupy the first trophic level, capturing approximately 1% of sunlight falling on their leaves. Herbivores occupy the second level, small carnivores the third level, and larger tertiary carnivores the fourth trophic level.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    In nature, organisms feed on one another in a sequential pathway. A <strong class="text-emerald-400">food chain</strong> is a linear sequence of organisms through which nutrients and energy pass as one organism eats another (NCERT Figure 13.1).
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="text-xs font-bold text-amber-300 mb-2">Three Representative Natural Food Chains (NCERT Fig 13.1):</h4>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-emerald-500/20">
                            <span class="font-bold text-emerald-400">(a) Forest Food Chain:</span>
                            <p class="text-slate-300 mt-1">Trees / Plants (Producer) → Deer (Herbivore) → Tiger (Top Carnivore)</p>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-amber-500/20">
                            <span class="font-bold text-amber-400">(b) Grassland Food Chain:</span>
                            <p class="text-slate-300 mt-1">Grass → Insect (Grasshopper) → Frog → Snake → Eagle / Hawk</p>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-cyan-500/20">
                            <span class="font-bold text-cyan-400">(c) Pond Aquatic Food Chain:</span>
                            <p class="text-slate-300 mt-1">Phytoplankton / Algae → Zooplankton / Insect larva → Fish → Stork / Bird</p>
                        </div>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-indigo-500/30">
                    <h4 class="text-xs font-bold text-indigo-300 mb-2">Trophic Levels Hierarchy (NCERT Figure 13.2):</h4>
                    <div class="space-y-2 text-xs">
                        <div class="flex items-center justify-between p-2 rounded bg-indigo-950/40 border border-indigo-500/20">
                            <span class="font-bold text-rose-300">Fourth Trophic Level ($T_4$)</span>
                            <span class="text-slate-300">Tertiary Consumers (Top Carnivores: Tiger, Lion, Hawk)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-indigo-950/40 border border-indigo-500/20">
                            <span class="font-bold text-amber-300">Third Trophic Level ($T_3$)</span>
                            <span class="text-slate-300">Secondary Consumers (Small Carnivores: Frog, Small Fish, Fox)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-indigo-950/40 border border-indigo-500/20">
                            <span class="font-bold text-cyan-300">Second Trophic Level ($T_2$)</span>
                            <span class="text-slate-300">Primary Consumers (Herbivores: Deer, Grasshopper, Zooplankton)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-indigo-950/40 border border-indigo-500/20">
                            <span class="font-bold text-emerald-300">First Trophic Level ($T_1$)</span>
                            <span class="text-slate-300">Producers (Autotrophs: Green plants, Phytoplankton)</span>
                        </div>
                    </div>
                    <p class="text-[11px] text-amber-300/90 mt-2">
                        ★ <strong>Key Solar Capture Fact:</strong> Green plants in a terrestrial ecosystem capture only about <strong>1% of the total solar energy</strong> that falls on their leaves and convert it into chemical food energy!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "What percentage of solar energy falling on green plant leaves in a terrestrial ecosystem is captured and converted into food energy?",
                "options": [
                    "Approximately 10%",
                    "Approximately 1%",
                    "Approximately 50%",
                    "Nearly 100%"
                ],
                "ans": 1,
                "explanation": "NCERT explicitly states that green plants in a terrestrial ecosystem capture only about 1% of the solar energy that strikes their leaves and convert it into chemical food energy."
            },
            {
                "question": "In the grassland food chain: Grass → Grasshopper → Frog → Snake → Hawk, which organism occupies the third trophic level?",
                "options": [
                    "Grasshopper (Primary Consumer)",
                    "Frog (Secondary Consumer)",
                    "Snake (Tertiary Consumer)",
                    "Hawk (Quaternary Consumer)"
                ],
                "ans": 1,
                "explanation": "First level ($T_1$) = Grass (Producer); Second level ($T_2$) = Grasshopper (Herbivore); Third level ($T_3$) = Frog (Secondary consumer/small carnivore)."
            }
        ]
    },

    # Slide 4: The 10% Law of Energy Transfer
    {
        "id": 4,
        "title": "The 10% Law of Energy Transfer",
        "subtitle": "Raymond Lindeman's Rule & Why Food Chains Are Limited to 3-4 Steps",
        "narration": "When food is eaten by an organism, a great deal of energy is lost as metabolic heat to the environment, while more is expended in digestion, movement, and maintenance. On average, only 10% of the food eaten is turned into the organism's own biomass and made available to the next trophic level. Because of this massive 90% loss at every step, very little usable energy remains after four trophic levels, limiting food chains to just 3 or 4 links.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    The transfer of energy from one trophic level to the next follows the famous <strong class="text-amber-400">10% Law</strong> (formulated by Raymond Lindeman in 1942).
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-2">Mathematical Formulation of 10% Energy Transfer:</h4>
                    <p class="text-xs text-slate-300 leading-normal">
                        When green plants are eaten by primary consumers, a great deal of energy is lost as heat to the environment, some is expended during digestion and respiration, and only an average of <strong>10%</strong> of the food eaten is converted into new body biomass available for the next consumer level:
                    </p>
                    <div class="p-2.5 mt-2 rounded bg-slate-950 text-center font-mono text-emerald-400 text-xs border border-emerald-500/20">
                        Energy at Next Level ($E_{n+1}$) = 0.10 × Energy at Current Level ($E_n$)
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="text-xs font-bold text-cyan-300 mb-2">Step-by-Step Energy Dissipation Example:</h4>
                    <div class="space-y-1.5 text-xs text-slate-300">
                        <div class="flex justify-between items-center py-1 border-b border-slate-800">
                            <span>Solar Incident Light on Forest Canopy:</span>
                            <span class="font-mono text-amber-300 font-bold">1,000,000 J</span>
                        </div>
                        <div class="flex justify-between items-center py-1 border-b border-slate-800">
                            <span>Captured by Plants (1% conversion efficiency):</span>
                            <span class="font-mono text-emerald-400 font-bold">10,000 J (T1)</span>
                        </div>
                        <div class="flex justify-between items-center py-1 border-b border-slate-800">
                            <span>Available to Herbivores / Deer (10% transferred):</span>
                            <span class="font-mono text-cyan-400 font-bold">1,000 J (T2)</span>
                        </div>
                        <div class="flex justify-between items-center py-1 border-b border-slate-800">
                            <span>Available to Carnivores / Wolves (10% transferred):</span>
                            <span class="font-mono text-indigo-400 font-bold">100 J (T3)</span>
                        </div>
                        <div class="flex justify-between items-center py-1">
                            <span>Available to Apex Predator / Tiger (10% transferred):</span>
                            <span class="font-mono text-rose-400 font-bold">10 J (T4)</span>
                        </div>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-rose-500/30">
                    <h4 class="text-xs font-bold text-rose-300 mb-1">Two Vital Ecological Consequences:</h4>
                    <ul class="text-xs space-y-1 text-slate-300 list-disc list-inside">
                        <li><strong>Short Length of Food Chains:</strong> Since 90% is dissipated as non-reusable metabolic heat at each step, food chains rarely exceed 3 to 4 steps because usable energy after four levels becomes too tiny to sustain a viable population.</li>
                        <li><strong>Pyramid of Numbers:</strong> The greatest number of individuals exists at the lowest trophic levels (producers are most numerous, while apex carnivores are fewest).</li>
                    </ul>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "If 20,000 Joules of energy is trapped by producers at the first trophic level, how much energy will be available to tertiary consumers in a 4-step food chain?",
                "options": [
                    "2,000 J",
                    "200 J",
                    "20 J",
                    "2 J"
                ],
                "ans": 2,
                "explanation": "T1 (Producers) = 20,000 J → T2 (Primary) = 2,000 J (10%) → T3 (Secondary) = 200 J (10%) → T4 (Tertiary Consumers) = 20 J (10%)."
            },
            {
                "question": "Why do natural food chains rarely contain more than 4 or 5 trophic levels?",
                "options": [
                    "Higher carnivores refuse to eat meat from secondary consumers",
                    "The loss of 90% energy at each step leaves negligible usable energy to sustain higher trophic populations",
                    "Producers stop photosynthesizing when apex predators reproduce",
                    "Solar light intensity drops after the fourth trophic level"
                ],
                "ans": 1,
                "explanation": "Because 90% of energy is lost as heat, respiration, and waste at each link, the energy reaching beyond 4 trophic levels is insufficient to sustain higher predator populations."
            }
        ]
    },

    # Slide 5: Food Webs
    {
        "id": 5,
        "title": "Food Webs & Ecological Resilience",
        "subtitle": "Branching Interconnected Networks (NCERT Figure 13.3)",
        "narration": "In nature, food chains do not exist as isolated straight lines. Instead, each organism is eaten by two or more other kinds of organisms, which in turn are eaten by several others. This branching network of interconnected feeding relationships is called a food web. Food webs provide alternative dietary choices, giving ecosystems resilience against disruptions.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    While food chains provide a simplified conceptual model of feeding, the true feeding relationships in any natural habitat are far more complex and branched.
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-400 text-sm mb-2">Food Chain vs Food Web:</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                        <div class="p-3 rounded-lg bg-slate-950 border border-slate-800">
                            <span class="font-bold text-cyan-300">Linear Food Chain:</span>
                            <p class="text-slate-400 mt-1">
                                A single straight-line feeding pathway where each organism feeds on only one specific organism below it. Highly vulnerable: if one intermediate link is removed, all organisms above it starve.
                            </p>
                        </div>
                        <div class="p-3 rounded-lg bg-slate-950 border border-slate-800">
                            <span class="font-bold text-emerald-300">Interconnected Food Web:</span>
                            <p class="text-slate-400 mt-1">
                                A series of branching, interconnected food chains operating simultaneously (NCERT Figure 13.3). Each species feeds on multiple types of prey and serves as prey to multiple predators.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-indigo-500/30">
                    <h4 class="text-xs font-bold text-indigo-300 mb-2">Why Are Food Webs Essential for Ecological Stability?</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        In a food web, if a disease or climatic drought reduces the rabbit population, the fox and hawk do not starve to extinction because they can switch to eating mice, squirrels, lizards, or small birds. This ecological redundancy cushions the system against collapse and maintains equilibrium in nature.
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "What is the primary difference between a food chain and a food web?",
                "options": [
                    "A food chain operates in water, while a food web operates on land",
                    "A food chain is a single straight-line sequence, while a food web consists of multiple interconnected branching food chains",
                    "A food chain includes decomposers, while a food web excludes all autotrophs",
                    "A food chain transfers 100% energy, while a food web transfers zero energy"
                ],
                "ans": 1,
                "explanation": "A food chain represents a single linear feeding pathway, whereas a food web is an interconnected network of multiple food chains providing alternative feeding routes."
            },
            {
                "question": "How does a complex food web contribute to ecosystem stability compared to a single linear chain?",
                "options": [
                    "It ensures organisms can feed on alternative prey if one population declines",
                    "It prevents green plants from performing photosynthesis",
                    "It completely stops the loss of metabolic heat to the environment",
                    "It reverses energy flow back into the Sun"
                ],
                "ans": 0,
                "explanation": "Alternative feeding pathways in a food web allow predators to switch prey when a particular species declines, preventing catastrophic ecosystem collapse."
            }
        ]
    },

    # Slide 6: Unidirectional Flow of Energy
    {
        "id": 6,
        "title": "Unidirectional Flow of Energy in Ecosystems",
        "subtitle": "Thermodynamics & Non-Cyclic Energy vs Cyclic Nutrient Movement",
        "narration": "From the energy flow diagram, two fundamental principles emerge. First, energy flow in an ecosystem is strictly unidirectional. Solar energy captured by autotrophs never reverts to the Sun, and energy passed to herbivores never returns to plants. Second, the energy available at each trophic level diminishes progressively due to metabolic heat loss at each transfer.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    Energy flow through an ecosystem obeys the fundamental laws of thermodynamics (NCERT Figure 13.4).
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-2">The Two Master Rules of Ecosystem Energy Flow (NCERT Page 211):</h4>
                    <div class="space-y-3 text-xs text-slate-300">
                        <div class="p-3 rounded-lg bg-slate-950 border border-slate-800">
                            <span class="font-bold text-amber-400">1. Unidirectional (One-Way) Flow:</span>
                            <p class="mt-1">
                                The energy captured by autotrophic producers does not revert back to the solar input. Similarly, energy passed from autotrophs to herbivores does not travel backward to autotrophs. As energy moves progressively through successive trophic levels, it is lost as heat and is no longer available to the previous trophic level.
                            </p>
                        </div>
                        <div class="p-3 rounded-lg bg-slate-950 border border-slate-800">
                            <span class="font-bold text-rose-400">2. Progressive Diminution:</span>
                            <p class="mt-1">
                                The amount of usable energy available diminishes progressively at each successive trophic tier because approximately 90% is dissipated as non-usable environmental heat during respiration and movement.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/90 border border-cyan-500/30">
                    <h4 class="text-xs font-bold text-cyan-300 mb-1">Crucial Distinction: Energy Flow vs Nutrient Cycling:</h4>
                    <p class="text-xs text-slate-300">
                        • <strong>Energy Flow:</strong> Strictly <em>unidirectional and non-cyclic</em>. Energy enters as solar radiation, flows through the trophic pyramid, and is permanently radiated out into space as degraded heat.<br>
                        • <strong>Nutrient (Matter) Cycling:</strong> Strictly <em>cyclic</em>. Inorganic minerals (carbon, nitrogen, phosphorus) are taken up from soil/air by plants, pass through consumers, and are returned completely to the soil and air by decomposers to be reused perpetually!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Why is the flow of energy in an ecosystem described as unidirectional?",
                "options": [
                    "Energy can only flow during daylight hours when sunlight is present",
                    "Energy captured by autotrophs cannot revert to the Sun and energy passing to herbivores cannot return to producers",
                    "All energy remains locked inside apex predators forever without any heat loss",
                    "Decomposers turn energy into inorganic rocks"
                ],
                "ans": 1,
                "explanation": "Energy flow is strictly unidirectional because once solar energy is trapped and transferred through trophic tiers, it dissipates as heat and can never travel backward."
            },
            {
                "question": "How does the pathway of mineral nutrients in an ecosystem differ fundamentally from the pathway of energy?",
                "options": [
                    "Both energy and nutrients flow in a strictly one-way direction into outer space",
                    "Nutrients flow unidirectionally while energy is recycled indefinitely by decomposers",
                    "Energy flows unidirectionally and non-cyclically, whereas mineral nutrients are recycled cyclically by decomposers",
                    "Neither energy nor nutrients ever leave the plant body"
                ],
                "ans": 2,
                "explanation": "Energy flows unidirectionally and is dissipated as heat, whereas matter and nutrients cycle repeatedly between biotic and abiotic components via decomposers."
            }
        ]
    },

    # Slide 7: Biological Magnification
    {
        "id": 7,
        "title": "Biological Magnification (Biomagnification)",
        "subtitle": "Progressive Accumulation of Non-Biodegradable Toxicants in Food Chains",
        "narration": "Harmful non-biodegradable chemicals such as synthetic pesticides and heavy metals enter water bodies and soil. Plants absorb them along with water, and aquatic organisms ingest them. Because these toxic chemicals cannot be metabolized or excreted by living tissues, they accumulate progressively at each trophic level. Since humans occupy the top trophic level, maximum concentration accumulates in our bodies. This phenomenon is known as biological magnification.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    Pesticides, insecticides (like DDT), and heavy metals sprayed to protect crops are washed into the soil or washed into water bodies (NCERT Section 13.1.1).
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/40">
                    <h4 class="font-bold text-rose-400 text-sm mb-2">Definition of Biological Magnification:</h4>
                    <p class="text-xs text-slate-300">
                        <strong class="text-rose-300">Biological Magnification</strong> is the progressive increase in the concentration of toxic, non-biodegradable chemicals (such as pesticides, DDT, and heavy metals) in the bodies of living organisms at each successive trophic level of a food chain.
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="text-xs font-bold text-amber-300 mb-2">How Toxic Chemicals Magnify Through Trophic Tiers:</h4>
                    <div class="space-y-2 text-xs">
                        <div class="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
                            <span class="text-cyan-400 font-bold">1. Water / Soil Source:</span>
                            <span class="font-mono text-slate-400">0.000003 ppm (parts per million)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
                            <span class="text-emerald-400 font-bold">2. Phytoplankton & Crop Plants:</span>
                            <span class="font-mono text-emerald-400">0.04 ppm (absorbed with water/minerals)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
                            <span class="text-amber-400 font-bold">3. Herbivores / Zooplankton / Small Fish:</span>
                            <span class="font-mono text-amber-400">0.5 ppm (eats thousands of plankton)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-slate-950 border border-slate-800">
                            <span class="text-indigo-400 font-bold">4. Secondary Consumers / Large Fish:</span>
                            <span class="font-mono text-indigo-400">2.0 ppm (concentrates fish fat stores)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded bg-rose-950/40 border border-rose-500/30">
                            <span class="text-rose-300 font-bold">5. Top Carnivores & Human Beings:</span>
                            <span class="font-mono text-rose-300 font-bold">Up to 25.0 ppm (Maximum Concentration!)</span>
                        </div>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="text-xs font-bold text-amber-300 mb-1">Why Are Humans Most Vulnerable?</h4>
                    <p class="text-xs text-slate-300">
                        Because human beings occupy the topmost position in multiple food chains, we consume grains, vegetables, milk, and meat that have already accumulated pesticide residues. Because these synthetic molecules are fat-soluble and cannot be excreted or broken down by human liver enzymes, they cannot always be removed by washing or cooking!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Which trophic level in a contaminated aquatic food chain will exhibit the highest concentration of non-biodegradable pesticide residues due to biological magnification?",
                "options": [
                    "Aquatic water weeds (Producers)",
                    "Zooplankton (Primary consumers)",
                    "Small herbivorous fish (Secondary consumers)",
                    "Fish-eating birds or humans (Top consumers)"
                ],
                "ans": 3,
                "explanation": "Because non-biodegradable chemicals cannot be metabolized or excreted, they accumulate progressively up the chain, reaching peak concentration in top consumers."
            },
            {
                "question": "Why can pesticide residues accumulated inside crop plants and animal tissues NOT be completely removed by washing with water?",
                "options": [
                    "Because pesticides convert water into poisonous alcohol",
                    "Because systemic pesticides are absorbed into internal plant tissues and fat reserves rather than remaining only on surface skins",
                    "Because water increases pesticide concentration by 10% automatically",
                    "Because sunlight glues pesticide molecules permanently to plant leaves"
                ],
                "ans": 1,
                "explanation": "Pesticides absorbed through roots become incorporated into internal cell structures and fat reserves of grains and animals, so external surface washing cannot remove them."
            }
        ]
    },

    # Slide 8: The Ozone Layer & Stratospheric Shield
    {
        "id": 8,
        "title": "13.2.1 Ozone Layer & Its Essential Shield",
        "subtitle": "Deadly Ground-Level Toxin vs Vital Stratospheric Solar Filter",
        "narration": "Ozone is a triatomic molecule made of three oxygen atoms, O3. While normal diatomic oxygen O2 is vital for all aerobic life, ozone is a deadly poison at ground level. However, at the higher levels of our atmosphere in the stratosphere, ozone performs an indispensable protective function: it absorbs harmful solar ultraviolet radiation, shielding life on Earth from skin cancer, cataracts, and genetic damage.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    Ozone ($O_3$) exhibits completely contrasting biological effects depending on its altitude in the atmosphere (NCERT Section 13.2.1).
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 text-sm mb-2 flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
                            Ground-Level Ozone (Troposphere)
                        </h4>
                        <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300">
                            <li><strong>Chemical Nature:</strong> Highly reactive triatomic oxidant ($O_3$).</li>
                            <li><strong>Biological Effect:</strong> A <strong class="text-rose-300">deadly poison</strong> and major constituent of photochemical smog.</li>
                            <li>Causes severe respiratory inflammation, asthma attacks, pulmonary edema, and plant leaf necrosis.</li>
                        </ul>
                    </div>
                    <div class="p-4 rounded-xl bg-slate-900 border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 text-sm mb-2 flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyan-500"></span>
                            Stratospheric Ozone Shield (15–30 km)
                        </h4>
                        <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300">
                            <li><strong>Atmospheric Location:</strong> High altitude stratosphere.</li>
                            <li><strong>Biological Effect:</strong> A <strong class="text-emerald-300">vital protective umbrella</strong> that absorbs 97–99% of solar ultraviolet (UV) radiation.</li>
                            <li>Prevents high-energy UV-B and UV-C rays from reaching the Earth's surface.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="text-xs font-bold text-amber-300 mb-1">Harmful Hazards of Ultraviolet (UV) Radiation:</h4>
                    <p class="text-xs text-slate-300">
                        If the stratospheric ozone layer is depleted, excessive UV radiation reaches the surface, causing:
                        <br>1. <strong>Skin Cancer:</strong> Melanoma and carcinoma due to direct DNA mutations in epithelial cells.
                        <br>2. <strong>Cataracts & Corneal Blindness:</strong> Photokeratitis and lens protein denaturation.
                        <br>3. <strong>Immune Suppression:</strong> Weakened disease resistance in animals and humans.
                        <br>4. <strong>Marine Ecosystem Collapse:</strong> Destruction of surface phytoplankton, devastating global ocean food webs!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "How does the biological role of ozone (O3) at ground level differ from its role in the stratosphere?",
                "options": [
                    "It is essential for human breathing at ground level but poisonous in the stratosphere",
                    "It is a deadly respiratory poison at ground level, but acts as an essential UV-radiation shield in the stratosphere",
                    "It cools the ground at night and freezes rainwater in the stratosphere",
                    "It acts as a plant fertilizer at both atmospheric levels"
                ],
                "ans": 1,
                "explanation": "NCERT Page 212 highlights that ozone is a deadly poison at ground level, but at stratospheric altitudes it performs the vital shield function absorbing UV radiation."
            },
            {
                "question": "Which of the following severe health hazards in human beings is directly linked to increased ultraviolet (UV) radiation penetrating a depleted ozone layer?",
                "options": [
                    "Iron deficiency anaemia",
                    "Skin cancer and cataract eye damage",
                    "Bacterial cholera infection",
                    "Goitre caused by iodine deficiency"
                ],
                "ans": 1,
                "explanation": "Excess UV radiation induces DNA mutations in skin cells causing skin cancers and denatures eye lens proteins causing cataracts."
            }
        ]
    },

    # Slide 9: Photochemical Formation & Catalytic Depletion of Ozone
    {
        "id": 9,
        "title": "Photochemical Formation & Catalytic Depletion",
        "subtitle": "Chapman Cycle Equations & CFC-Driven Stratospheric Degradation",
        "narration": "Stratospheric ozone is formed naturally through a two-step photochemical reaction. High-energy ultraviolet radiation splits diatomic oxygen molecules into free nascent oxygen atoms. These free atoms combine with molecular oxygen to produce ozone. In the 1980s, atmospheric scientists discovered a sharp drop in ozone over Antarctica caused by synthetic chlorofluorocarbons, or CFCs, used in refrigerants and fire extinguishers.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    The natural equilibrium of ozone in the stratosphere is governed by photochemical reactions (NCERT Page 213).
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-2">Two-Step Natural Ozone Formation Chemistry:</h4>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded bg-slate-950 border border-slate-800">
                            <span class="text-amber-400 font-bold">Step 1 (Photodissociation):</span> High-energy solar UV radiation breaks the strong double bond of molecular oxygen ($O_2$) into two reactive nascent oxygen atoms:
                            <div class="font-mono text-cyan-400 text-center my-1 text-sm">
                                O₂ ──(UV Radiation)──→ O + O
                            </div>
                        </div>
                        <div class="p-2.5 rounded bg-slate-950 border border-slate-800">
                            <span class="text-emerald-400 font-bold">Step 2 (Ozone Synthesis):</span> The highly reactive free oxygen atom ($O$) combines with an intact oxygen molecule ($O_2$) to form an ozone molecule ($O_3$):
                            <div class="font-mono text-emerald-400 text-center my-1 text-sm">
                                O + O₂ ────→ O₃ (Ozone)
                            </div>
                        </div>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/30">
                    <h4 class="font-bold text-rose-300 text-sm mb-2">Discovery of the Ozone Hole & CFCs:</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        In the 1980s, scientists discovered that the concentration of stratospheric ozone over Antarctica dropped precipitously each spring—a phenomenon popularly termed the <strong class="text-rose-400">Ozone Hole</strong>.
                        <br><br>
                        <strong>The Culprit: Chlorofluorocarbons (CFCs):</strong> Synthetic chemicals widely used as volatile refrigerants in refrigerators and air conditioners, as propellants in aerosol spray cans, and in fire extinguishers. CFCs are non-flammable and inert at ground level, but when they drift up into the stratosphere, harsh UV light breaks them apart, releasing free chlorine free radicals ($Cl^\bullet$):
                        <br>
                        <span class="font-mono text-rose-300 text-[11px] block mt-1">
                            Cl• + O₃ → ClO• + O₂ &nbsp;|&nbsp; ClO• + O → Cl• + O₂
                        </span>
                        <span class="text-[11px] text-slate-400 block mt-1">
                            Because the chlorine radical is regenerated unchanged, a single chlorine atom can catalytically destroy over <strong>100,000 ozone molecules</strong> before being removed!
                        </span>
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "What is the initial photochemical step in the natural formation of stratospheric ozone?",
                "options": [
                    "Chlorine atoms react with nitrogen gas to release heat",
                    "High-energy UV radiation splits molecular oxygen (O2) into free oxygen atoms (O)",
                    "Water vapor condenses to produce liquid ozone droplets",
                    "Bacteria in soil oxidize ammonia into ozone"
                ],
                "ans": 1,
                "explanation": "High-energy UV rays split molecular oxygen into free reactive nascent oxygen atoms (O2 → O + O), which then combine with intact O2 to synthesize O3."
            },
            {
                "question": "Which class of synthetic industrial chemicals was identified as the primary driver of stratospheric ozone depletion in the 1980s?",
                "options": [
                    "Carbon dioxide and methane emissions",
                    "Chlorofluorocarbons (CFCs) used in refrigeration and aerosol propellants",
                    "Sulfur dioxide released from coal power plants",
                    "Nitrogen fertilizers sprayed on agricultural fields"
                ],
                "ans": 1,
                "explanation": "CFCs release reactive chlorine radicals under high-energy UV in the stratosphere, catalytically destroying tens of thousands of ozone molecules."
            }
        ]
    },

    # Slide 10: The Montreal Protocol & Global Action
    {
        "id": 10,
        "title": "The 1987 Montreal Protocol & Global Recovery",
        "subtitle": "UNEP Action, CFC-Free Refrigeration & Stratospheric Healing",
        "narration": "In 1987, the United Nations Environment Programme succeeded in forging a landmark global agreement known as the Montreal Protocol. All member nations agreed to freeze CFC production at 1986 levels and systematically phase them out. Today, manufacturing companies worldwide produce CFC-free refrigerators using safer alternatives, and the ozone layer is gradually healing.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    The depletion of the ozone layer spurred the most successful international environmental treaty in human history (NCERT Page 213).
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-400 text-sm mb-2">The 1987 UNEP Agreement (Montreal Protocol):</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        In 1987, under the leadership of the <strong class="text-emerald-300">United Nations Environment Programme (UNEP)</strong>, nations forged an unprecedented treaty to freeze and phase out ozone-depleting substances:
                    </p>
                    <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300 mt-2">
                        <li><strong>CFC Production Freeze:</strong> Developed and developing nations agreed to immediately freeze CFC production at 1986 levels.</li>
                        <li><strong>Mandatory CFC-Free Appliances:</strong> Regulations made it globally mandatory for appliance manufacturers to transition to CFC-free refrigerators, air conditioners, and propellants.</li>
                        <li><strong>Transition to Safe Substitutes:</strong> Hydrofluorocarbons (HFCs), hydrofluoroolefins (HFOs), and natural hydrocarbon coolants (like isobutane) that lack ozone-destroying chlorine atoms.</li>
                    </ul>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-cyan-500/30">
                    <h4 class="text-xs font-bold text-cyan-300 mb-1">Activity 13.4 Insights & Atmospheric Recovery:</h4>
                    <p class="text-xs text-slate-300">
                        Has the size of the ozone hole changed in recent years? Yes! Due to universal adherence to the Montreal Protocol, atmospheric concentrations of active chlorine have dropped steadily. Scientific satellite monitoring shows that the Antarctic ozone hole is actively healing and is projected to recover completely back to 1980 levels by approximately 2060.
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "In 1987, which international organization successfully forged the treaty freezing global CFC production at 1986 levels?",
                "options": [
                    "World Health Organization (WHO)",
                    "United Nations Environment Programme (UNEP)",
                    "International Red Cross Committee",
                    "World Trade Organization (WTO)"
                ],
                "ans": 1,
                "explanation": "NCERT Page 213 states: 'In 1987, the United Nations Environment Programme (UNEP) succeeded in forging an agreement to freeze CFC production at 1986 levels.'"
            },
            {
                "question": "What technological mandate was imposed on appliance manufacturing companies worldwide as a result of international ozone agreements?",
                "options": [
                    "Manufacturing refrigerators that run entirely without electricity",
                    "Producing mandatory CFC-free refrigerators and air conditioning systems",
                    "Using radioactive uranium to cool refrigerator condensers",
                    "Banning all home food preservation systems"
                ],
                "ans": 1,
                "explanation": "It became mandatory for all refrigerator and cooling appliance manufacturers worldwide to replace CFCs with ozone-safe refrigerants."
            }
        ]
    },

    # Slide 11: Managing Daily Garbage: Biodegradable vs Non-Biodegradable
    {
        "id": 11,
        "title": "13.2.2 Managing the Garbage We Produce",
        "subtitle": "Biodegradable vs Non-Biodegradable Waste & Activity 13.5 Burial Test",
        "narration": "Our daily lifestyle generates substantial amounts of waste materials. Substances that can be broken down by biological processes through the action of bacteria and fungi are called biodegradable, such as fruit peels and paper. Substances that cannot be broken down by saprophytic microorganisms are called non-biodegradable, such as synthetic plastics and glass. In Activity 13.5, burying waste in soil proves that organic waste rots rapidly while plastic remains unchanged.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    All solid waste generated by human domestic, commercial, and industrial activities is divided into two broad categories based on biological breakdown (NCERT Section 13.2.2).
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 text-sm mb-2 flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                            Biodegradable Substances
                        </h4>
                        <p class="text-xs text-slate-300 mb-2">
                            Substances that are broken down into simple, harmless inorganic substances by the biological enzymatic action of saprophytic microorganisms (bacteria and fungi).
                        </p>
                        <ul class="text-xs space-y-1 list-disc list-inside text-slate-400">
                            <li>Kitchen vegetable & fruit peels, spoilt food.</li>
                            <li>Used tea leaves, eggshells, cow dung.</li>
                            <li>Waste paper, cardboard cartons, wood.</li>
                            <li>Natural fibers: pure cotton, wool, silk, leather.</li>
                        </ul>
                    </div>
                    <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 text-sm mb-2 flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
                            Non-Biodegradable Substances
                        </h4>
                        <p class="text-xs text-slate-300 mb-2">
                            Substances that cannot be broken down by the biological action of microorganisms. They persist in the environment for hundreds of years in an unaltered state.
                        </p>
                        <ul class="text-xs space-y-1 list-disc list-inside text-slate-400">
                            <li>Synthetic plastics (polythene, PVC, polystyrene).</li>
                            <li>Metal cans, blister medicine packaging.</li>
                            <li>Glass bottles, synthetic nylon/polyester fabrics.</li>
                            <li>Pesticides (DDT), heavy metals (mercury, lead).</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="text-xs font-bold text-amber-300 mb-1">Activity 13.5: Soil Burial Experiment:</h4>
                    <p class="text-xs text-slate-300">
                        Bury kitchen waste (peels, tea leaves, paper) alongside plastic wrappers, blister packs, and broken footwear in a pit covered with 15 cm of soil. At 15-day intervals, kitchen waste turns black and softens into humus-rich compost, whereas plastic wrappers and medicine blister packs remain completely unchanged!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following household waste items will undergo rapid biological decomposition when buried in moist garden soil for 30 days?",
                "options": [
                    "Plastic milk pouch wrapper",
                    "Aluminium foil food wrap",
                    "Potato peels and wet tea leaves",
                    "Empty plastic medicine blister strip"
                ],
                "ans": 2,
                "explanation": "Potato peels and used tea leaves are organic, biodegradable materials that bacteria and fungi decompose into simple humus and soil nutrients."
            },
            {
                "question": "Why are synthetic plastics classified as non-biodegradable waste in our environment?",
                "options": [
                    "They dissolve instantly in rainwater before bacteria can touch them",
                    "They cannot be broken down by the biological enzymatic action of bacteria and fungi",
                    "They are made exclusively of pure elemental gold",
                    "They absorb 100% of cosmic rays from outer space"
                ],
                "ans": 1,
                "explanation": "Saprophytic bacteria lack enzymes capable of breaking the synthetic carbon-carbon polymer bonds found in petroleum-based plastics."
            }
        ]
    },

    # Slide 12: Why Plastics Persist: Enzyme Specificity
    {
        "id": 12,
        "title": "Why Plastics Persist: Enzyme Specificity",
        "subtitle": "Biochemical Lock-and-Key Analogy & Ambient Environmental Resistance",
        "narration": "Have you ever wondered why human-made plastics persist for centuries without decomposing? In Chapter 5 on Life Processes, we learned that enzymes are highly specific in their action. Specific enzymes are required to break specific chemical bonds—which is why humans cannot get energy from eating coal. Soil bacteria possess enzymes evolved over millions of years to digest natural plant polymers, but they completely lack enzymes to break synthetic plastic polymer bonds.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    The biological persistence of plastics is rooted in fundamental biochemical enzyme kinetics (NCERT Page 214).
                </p>
                <div class="p-4 rounded-xl bg-slate-900 border border-indigo-500/30">
                    <h4 class="font-bold text-indigo-300 text-sm mb-2">The Principle of Enzyme Substrate Specificity:</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Enzymes are biocatalysts that operate by a strict <strong class="text-indigo-400">lock-and-key mechanism</strong>. The active site of an enzyme only fits a specific substrate molecule with exact geometric and chemical alignment.
                        <br><br>
                        • <strong>Why We Cannot Eat Coal:</strong> Human salivary and pancreatic enzymes like amylase are specifically shaped to cleave alpha-glycosidic bonds in plant starch. Even though coal is made of carbon, our enzymes cannot recognize or cleave the carbon bonds in coal, yielding zero calories!
                        <br><br>
                        • <strong>Why Bacteria Cannot Digest Plastics:</strong> Natural organic matter (cellulose, lignin, protein) has existed for hundreds of millions of years, allowing saprophytic bacteria and fungi to evolve specialized cellulase and protease enzymes. Synthetic plastics like polyethylene, polypropylene, and polystyrene were invented less than a century ago. Decomposers have no matching enzymes to break their synthetic polymer bonds.
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="text-xs font-bold text-amber-300 mb-1">Physical Fragmentation vs Biological Decomposition:</h4>
                    <p class="text-xs text-slate-300">
                        Under ambient environmental conditions, physical factors like solar heat, ultraviolet radiation, and mechanical abrasion can crack plastics into smaller fragments. However, these fragments remain plastics (<strong class="text-amber-300">microplastics</strong>), which persist in soil and water for hundreds of years, entering the food chain and harming living organisms!
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "According to NCERT Page 214, why do natural saprophytic bacteria fail to decompose synthetic plastics?",
                "options": [
                    "Plastics are radioactive and kill all nearby bacteria instantly",
                    "Enzymes are substrate-specific and microorganisms lack enzymes capable of breaking synthetic plastic polymer bonds",
                    "Plastics turn into gas whenever bacteria approach them",
                    "Bacteria only operate in boiling hot volcanic vents"
                ],
                "ans": 1,
                "explanation": "Enzymatic action requires precise substrate fit; decomposers have not evolved enzymes to cleave synthetic man-made polymer linkages."
            },
            {
                "question": "What is the biological reason humans cannot derive energy from eating coal even though coal is rich in carbon?",
                "options": [
                    "Coal has negative calories",
                    "Human digestive enzymes are specific in action and cannot break down the chemical structure of coal",
                    "Coal reflects all digestive enzymes into the pancreas",
                    "Stomach acid freezes upon touching coal"
                ],
                "ans": 1,
                "explanation": "Enzymes are specific in their action; human digestive enzymes can only cleave specific dietary bonds in carbohydrates, proteins, and fats, not the structure of coal."
            }
        ]
    },

    # Slide 13: Environmental Impacts of Waste
    {
        "id": 13,
        "title": "Environmental Impacts of Waste Disposal",
        "subtitle": "Dangers of Non-Biodegradable Accumulation & Hazards of Mismanaged Biodegradable Waste",
        "narration": "Both non-biodegradable and mismanaged biodegradable waste inflict severe damage on ecosystems. Non-biodegradable plastics clog city drainage systems, leach toxic chemicals into groundwater, and kill stray animals that swallow them. Even biodegradable waste, if allowed to accumulate in massive unmanaged heaps, undergoes anaerobic rotting, releasing foul odours and greenhouse methane, while breeding disease-carrying vectors.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    Uncontrolled disposal of urban solid waste is one of the most critical environmental crises today (NCERT Pages 214–215).
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 text-sm mb-2">Impacts of Non-Biodegradable Waste:</h4>
                        <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300">
                            <li><strong class="text-rose-300">Drainage Choking:</strong> Plastic bags clog municipal sewer pipes, causing dirty urban flash-flooding during monsoon rains.</li>
                            <li><strong class="text-rose-300">Animal Death:</strong> Stray cattle and wildlife ingest plastic wrappers containing food, leading to fatal rumen impaction.</li>
                            <li><strong class="text-rose-300">Chemical Leaching:</strong> Heavy metals, phthalates, and bisphenol-A leach from buried plastics, poisoning aquifers and soil.</li>
                            <li><strong class="text-rose-300">Toxic Air Pollution:</strong> Burning plastics releases carcinogenic dioxins, furans, and black soot.</li>
                        </ul>
                    </div>
                    <div class="p-4 rounded-xl bg-slate-900 border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 text-sm mb-2">Impacts of Mismanaged Biodegradable Waste:</h4>
                        <ul class="text-xs space-y-1.5 list-disc list-inside text-slate-300">
                            <li><strong class="text-amber-300">Foul Odour & Vectors:</strong> Decaying organic heaps release pungent hydrogen sulfide and become breeding grounds for disease-spreading flies, mosquitoes, and rodents.</li>
                            <li><strong class="text-amber-300">Methane Emissions:</strong> Anaerobic decomposition in dense landfills generates methane ($CH_4$), a greenhouse gas 25× more potent than $CO_2$.</li>
                            <li><strong class="text-amber-300">Water Eutrophication:</strong> Organic run-off depletes dissolved oxygen in ponds, asphyxiating fish populations.</li>
                        </ul>
                    </div>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following is a major catastrophic hazard caused specifically by non-biodegradable plastic bags in urban cities?",
                "options": [
                    "They cause sudden excessive rainfall in desert regions",
                    "They choke city underground sewer lines causing toxic urban flooding",
                    "They turn all freshwater into potable mineral water",
                    "They enrich topsoil fertility by adding humus"
                ],
                "ans": 1,
                "explanation": "Discarded plastic bags accumulate in underground drainage channels and sewers, clogging stormwater flows and causing urban flooding."
            },
            {
                "question": "If all waste generated by human activity were 100% biodegradable, why would it still pose significant environmental and health risks if dumped without proper management?",
                "options": [
                    "Biodegradable waste can never be decomposed by bacteria",
                    "Massive rotting heaps release foul gases, breed disease-spreading flies and mosquitoes, and pollute water bodies",
                    "Biodegradable materials immediately deplete the stratospheric ozone layer",
                    "It converts surrounding air into poisonous sulfur crystals"
                ],
                "ans": 1,
                "explanation": "Large heaps of decomposing organic waste rot anaerobically, emitting foul gases like methane and hydrogen sulfide, while breeding disease-carrying vectors like flies, mosquitoes, and rats."
            }
        ]
    },

    # Slide 14: Train Teacups & Top-Soil Conservation
    {
        "id": 14,
        "title": "Case Study: The Evolution of Train Teacups",
        "subtitle": "Reusable Glass vs Plastic vs Clay Kulhads vs Modern Paper Cups",
        "narration": "In the fascinating Think It Over section on Page 215, NCERT explores how tea was served on Indian trains. Tea was originally served in washable plastic or glass cups returned to vendors, raising hygiene concerns. Disposable plastic cups solved hygiene but created mountains of non-biodegradable trash. Disposable clay cups, or kulhads, were suggested, but making them on a large scale stripped millions of tonnes of fertile top-soil! Today, biodegradable disposable paper cups provide the optimal sustainable solution.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    The story of railway teacups illustrates how environmental problem-solving requires comprehensive ecological lifecycle analysis (NCERT Page 215: Think It Over).
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="text-xs font-bold text-amber-300 mb-2">The Four Stages of Railway Teacup Evolution:</h4>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded bg-slate-950 border border-slate-800">
                            <span class="font-bold text-slate-300">Phase 1: Returnable Glasses & Plastic Mugs</span>
                            <p class="text-slate-400 mt-1">
                                Tea was served in glasses that had to be returned to the vendor. While zero waste was generated, washing cups in unhygienic bucket water posed disease transmission risks to railway passengers.
                            </p>
                        </div>
                        <div class="p-2.5 rounded bg-slate-950 border border-rose-500/30">
                            <span class="font-bold text-rose-400">Phase 2: Disposable Plastic Cups</span>
                            <p class="text-slate-400 mt-1">
                                Hailed as a major hygiene breakthrough. However, disposing of millions of single-use polystyrene cups daily created colossal mountains of non-biodegradable plastic littering thousands of kilometres of railway tracks.
                            </p>
                        </div>
                        <div class="p-2.5 rounded bg-slate-950 border border-amber-500/30">
                            <span class="font-bold text-amber-400">Phase 3: Disposable Clay Kulhads</span>
                            <p class="text-slate-400 mt-1">
                                Introduced as a traditional, biodegradable alternative. But calculations showed that manufacturing billions of fired clay kulhads every month required stripping immense quantities of <strong>fertile agricultural top-soil</strong>, threatening crop productivity!
                            </p>
                        </div>
                        <div class="p-2.5 rounded bg-slate-950 border border-emerald-500/30">
                            <span class="font-bold text-emerald-400">Phase 4: Modern Disposable Paper Cups</span>
                            <p class="text-slate-400 mt-1">
                                The optimal balance: Made from renewable wood pulp, fully biodegradable, lightweight, highly hygienic, and requires zero stripping of fertile agricultural top-soil!
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "What serious environmental crisis emerged when disposable clay cups (kulhads) were proposed as a large-scale replacement for plastic cups in Indian railway trains?",
                "options": [
                    "Clay caused severe acid rain around railway stations",
                    "Making billions of kulhads on a national scale caused massive loss of fertile agricultural top-soil",
                    "Clay cups released toxic chlorofluorocarbons into the atmosphere",
                    "Tea reacted chemically with clay to produce explosive hydrogen"
                ],
                "ans": 1,
                "explanation": "NCERT Page 215 explains that producing kulhads on a massive scale requires huge quantities of top-soil, stripping the fertile upper layer crucial for agriculture."
            },
            {
                "question": "What makes modern disposable paper cups preferable over both plastic cups and clay kulhads?",
                "options": [
                    "Paper cups are made from heavy lead metal",
                    "Paper cups are hygienic, biodegradable, and do not destroy fertile agricultural topsoil",
                    "Paper cups can be eaten by passengers as nutritious snacks",
                    "Paper cups last for over 500 years in landfills without changing"
                ],
                "ans": 1,
                "explanation": "Paper cups are biodegradable, hygienic for single use, and unlike clay kulhads, their manufacture does not deplete agricultural top-soil."
            }
        ]
    },

    # Slide 15: Waste Management & 5 R's
    {
        "id": 15,
        "title": "Waste Segregation & The 5 R's Framework",
        "subtitle": "Source Separation, Green/Blue Bins, STPs & Sustainable Waste Hierarchy",
        "narration": "Dealing with the garbage crisis requires waste segregation at source and following the five R's of waste management: Refuse, Reduce, Reuse, Repurpose, and Recycle. Biodegradable wet waste collected in green bins can be converted into rich organic compost or biogas, while dry recyclable waste in blue bins is reprocessed into new products. In Activities 13.7 and 13.8, sewage treatment plants ensure wastewater is purified before entering rivers.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    Effective solid and liquid waste management requires action at household, community, and municipal levels (NCERT Activities 13.7 & 13.8).
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 text-xs mb-2">Two-Bin Household Segregation:</h4>
                        <div class="space-y-2 text-xs">
                            <div class="p-2 rounded bg-emerald-950/40 border border-emerald-500/20">
                                <span class="font-bold text-emerald-300">Green Bin (Wet / Biodegradable):</span>
                                <p class="text-slate-300 mt-1">Kitchen peels, food scraps, leaves, tea waste. Processed via aerobic vermicomposting or anaerobic biogas digestors to yield methane fuel and organic manure.</p>
                            </div>
                            <div class="p-2 rounded bg-cyan-950/40 border border-cyan-500/20">
                                <span class="font-bold text-cyan-300">Blue Bin (Dry / Recyclable):</span>
                                <p class="text-slate-300 mt-1">Clean paper, plastic bottles, glass, metal cans. Sent to material recovery facilities for sorting and industrial remanufacturing.</p>
                            </div>
                        </div>
                    </div>
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 text-xs mb-2">The 5 R's Sustainable Hierarchy:</h4>
                        <ul class="text-xs space-y-1 text-slate-300">
                            <li><strong class="text-indigo-300">1. Refuse:</strong> Say no to single-use plastic bags and disposable cutlery.</li>
                            <li><strong class="text-indigo-300">2. Reduce:</strong> Minimize unnecessary consumption and food waste.</li>
                            <li><strong class="text-indigo-300">3. Reuse:</strong> Use cloth shopping bags and refillable glass jars repeatedly.</li>
                            <li><strong class="text-indigo-300">4. Repurpose:</strong> Convert cracked plastic tubs into plant pots.</li>
                            <li><strong class="text-indigo-300">5. Recycle:</strong> Collect plastic, metal, and glass for industrial remelting.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-cyan-500/30">
                    <h4 class="text-xs font-bold text-cyan-300 mb-1">Sewage Treatment Plants (STPs) — Activity 13.8:</h4>
                    <p class="text-xs text-slate-300">
                        Municipal sewage must pass through primary physical screening, secondary biological aeration with aerobic bacteria to digest organic pollutants, and chemical chlorination before being released into natural water bodies to protect aquatic life.
                    </p>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following household waste disposal practices represents the highest priority in the sustainable 5 R's environmental framework?",
                "options": [
                    "Incinerating all household waste in backyard open fires",
                    "Refusing single-use plastic bags and carrying a washable cloth bag",
                    "Dumping wet and dry waste together into a single municipal dustbin",
                    "Recycling plastic after using it only once for two minutes"
                ],
                "ans": 1,
                "explanation": "In the waste hierarchy, 'Refuse' is the highest priority because preventing waste generation at source is far more effective than recycling or disposal."
            },
            {
                "question": "In municipal two-bin waste segregation systems, what should be placed into the Green Bin?",
                "options": [
                    "Broken window glass panes and fluorescent tubes",
                    "Aluminium beverage cans and metal wires",
                    "Biodegradable kitchen food leftovers, fruit peels, and garden leaves",
                    "Discarded computer circuit boards and mobile batteries"
                ],
                "ans": 2,
                "explanation": "Green bins are reserved for biodegradable wet organic waste (food scraps, vegetable peels, leaves) suitable for composting or biogas generation."
            }
        ]
    },

    # Slide 16: Complete NCERT Exercises Solutions (Q1 to Q9)
    {
        "id": 16,
        "title": "NCERT Exercises Solutions (Q1 to Q9)",
        "subtitle": "Official Textbook Solutions, Derivations & Board Exam Answer Keys",
        "narration": "Let's review the complete official NCERT textbook exercises from Pages 216 and 217. We will examine biodegradable groupings in Question 1, food chain sequences in Question 2, eco-friendly habits in Question 3, and detailed analytical answers for Questions 4 through 9 covering trophic level removal, biological magnification, and ozone layer protection.",
        "theory": """
            <div class="space-y-4 text-slate-300 text-sm leading-relaxed">
                <p>
                    Comprehensive step-by-step master walkthrough of NCERT Chapter 13 end-of-chapter exercises (Pages 216–217).
                </p>
                <div class="space-y-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="font-bold text-emerald-400">Exercise Q1: Biodegradable Groups (Multiple Correct in Textbook):</span>
                        <p class="text-slate-300 mt-1">
                            (a) Grass, flowers and leather: <strong>All Biodegradable</strong>.<br>
                            (b) Grass, wood and plastic: Plastic is non-biodegradable.<br>
                            (c) Fruit-peels, cake and lime-juice: <strong>All Biodegradable</strong>.<br>
                            (d) Cake, wood and grass: <strong>All Biodegradable</strong>.<br>
                            <em>(Note: In NCERT printing, options (a), (c), and (d) all contain exclusively biodegradable items).</em>
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="font-bold text-emerald-400">Exercise Q2: Food Chain Identification:</span>
                        <p class="text-slate-300 mt-1">
                            Correct sequence is <strong>(b) Grass, goat and human</strong> (Producer → Herbivore → Secondary Consumer). Option (a) has all plants, (c) has only herbivores, and (d) has fish eating grass and goat eating fish, which is ecologically invalid.
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="font-bold text-emerald-400">Exercise Q3: Environment-Friendly Practices:</span>
                        <p class="text-slate-300 mt-1">
                            <strong>(d) All of the above:</strong> (a) Carrying cloth-bags for shopping, (b) Switching off unnecessary lights/fans, and (c) Walking to school instead of scooter rides all conserve energy and eliminate waste.
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="font-bold text-amber-300">Exercise Q4 & Q5: What Happens If We Kill All Organisms in One Trophic Level?</span>
                        <p class="text-slate-300 mt-1">
                            • <strong>Starvation of Next Level:</strong> Organisms at the higher trophic level will starve to death or migrate due to lack of food.<br>
                            • <strong>Explosion of Lower Level:</strong> Organisms at the lower trophic level will multiply uncontrollably because their natural predators are gone, consuming all food and destroying the habitat.<br>
                            • <strong>Differential Impact:</strong> Removing producers causes total collapse of the entire ecosystem; removing top predators causes herbivore overpopulation and severe overgrazing. <em>No trophic level can be removed without causing ecological damage!</em>
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="font-bold text-cyan-300">Exercise Q6, Q7, Q8 & Q9 Highlights:</span>
                        <p class="text-slate-300 mt-1">
                            • <strong>Q6 (Biomagnification):</strong> Progressively increases at each trophic level; highest in humans/apex carnivores.<br>
                            • <strong>Q7 (Non-biodegradable waste):</strong> Clogs drains, chokes wildlife, contaminates soil/groundwater with toxic chemicals.<br>
                            • <strong>Q8 (All biodegradable waste):</strong> Excessive rotting heaps cause stench, greenhouse gas ($CH_4$) emissions, disease vectors, and aquatic deoxygenation.<br>
                            • <strong>Q9 (Ozone damage):</strong> Lets harmful UV reach Earth causing skin cancers and cataracts; mitigated by UNEP 1987 Montreal Protocol phasing out CFCs.
                        </p>
                    </div>
                </div>
            </div>
        """,
        "checkpoints": [
            {
                "question": "In NCERT Exercise Question 2, which of the following represents a biologically valid food chain?",
                "options": [
                    "Grass, wheat and mango",
                    "Grass, goat and human",
                    "Goat, cow and elephant",
                    "Grass, fish and goat"
                ],
                "ans": 1,
                "explanation": "Grass (Producer) is eaten by Goat (Primary consumer/herbivore), which is eaten by Human (Secondary consumer/omnivore)."
            },
            {
                "question": "According to NCERT Exercise Question 4, what happens to an ecosystem if all organisms in an intermediate trophic level (e.g. all herbivores) are eliminated?",
                "options": [
                    "All carnivores multiply tenfold and vegetation disappears completely",
                    "The higher carnivores starve while lower plant vegetation grows unchecked and unbrowsed, disrupting ecological balance",
                    "Solar light intensity drops to zero Joules",
                    "The ecosystem becomes permanently immune to all diseases"
                ],
                "ans": 1,
                "explanation": "Higher carnivores face starvation due to lack of prey, while lower producers overgrow initially without browsing pressure, throwing the ecosystem into severe disequilibrium."
            }
        ]
    }
]

# 4 Dedicated Quiz Slides (40 questions total, 10 per slide) with detailed popup solution modals
QUIZ_SLIDES = [
    # Quiz Slide 1 (Q1 to Q10): Ecosystems, Abiotic Factors, Producers & Decomposers
    {
        "id": 17,
        "title": "Mastery Challenge Part 1: Ecosystem Dynamics & Organism Roles",
        "subtitle": "Test Your Understanding of Sections 13.1 & 13.1.1 (Questions 1 to 10)",
        "questions": [
            {
                "id": 1,
                "q": "Which of the following constitutes an abiotic component of a forest ecosystem?",
                "options": ["Oak trees and ferns", "Soil moisture and temperature", "Earthworms and termites", "Spotted deer and tigers"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1:</strong> Abiotic components comprise non-living physical factors such as temperature, rainfall, wind, soil, minerals, and sunlight."
            },
            {
                "id": 2,
                "q": "Which of the following is an example of an artificial (human-made) ecosystem?",
                "options": ["Lake Baikal", "A tropical rainforest", "A cultivated crop-field", "A freshwater pond"],
                "ans": 2,
                "solution": "<strong>NCERT Section 13.1:</strong> Forests, ponds, and lakes are natural ecosystems, whereas gardens and crop-fields are artificial (human-made) ecosystems."
            },
            {
                "id": 3,
                "q": "All green plants and certain blue-green algae that synthesize organic food via photosynthesis are called:",
                "options": ["Primary consumers", "Decomposers", "Producers (Autotrophs)", "Tertiary consumers"],
                "ans": 2,
                "solution": "<strong>NCERT Section 13.1:</strong> Organisms that make organic compounds like sugar and starch from inorganic substances using radiant solar energy and chlorophyll are producers."
            },
            {
                "id": 4,
                "q": "Which organisms break down complex organic remains into simple inorganic substances that return to the soil?",
                "options": ["Producers", "Decomposers (bacteria and fungi)", "Herbivores", "Top carnivores"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1 & Activity 13.2:</strong> Decomposers (bacteria and fungi) break down dead remains and waste into simple inorganic nutrients used again by plants."
            },
            {
                "id": 5,
                "q": "Cuscuta (Amarbel), ticks, and tapeworms obtain nutrition from hosts without killing them immediately. They are classed as:",
                "options": ["Autotrophic producers", "Parasitic consumers", "Decomposing saprophytes", "Apex predators"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1:</strong> Consumers are categorized as herbivores, carnivores, omnivores, and parasites. Cuscuta and tapeworms are classic parasites."
            },
            {
                "id": 6,
                "q": "In Activity 13.1, what essential mechanical device must be installed in an artificial aquarium to supply dissolved oxygen to fish?",
                "options": ["A fluorescent UV lamp", "An aerator / oxygen pump", "A heating coil set to 100°C", "A chemical chlorinator"],
                "ans": 1,
                "solution": "<strong>NCERT Activity 13.1:</strong> Fish require dissolved oxygen in water, provided in an artificial aquarium through an oxygen pump or aerator."
            },
            {
                "id": 7,
                "q": "Why does a home aquarium require periodic manual water changes and cleaning, whereas a natural lake does not?",
                "options": ["Aquarium fish produce 100 times more waste than lake fish", "Natural lakes have self-sustaining cycles with natural decomposers and scavengers", "Lakes do not contain any living bacteria", "Lakes have artificial filters installed on the bottom"],
                "ans": 1,
                "solution": "<strong>NCERT Activity 13.1 & Page 209:</strong> Natural lakes possess a balanced, self-sustaining community of plants, animals, and decomposers that naturally recycle wastes."
            },
            {
                "id": 8,
                "q": "What would happen to the natural replenishment of soil minerals if all decomposers were eliminated from the biosphere?",
                "options": ["Soil mineral replenishment would accelerate dramatically", "Nutrient cycling would stop and dead organic remains would pile up permanently", "Producers would start photosynthesizing twice as fast", "The Earth would lose all gravity"],
                "ans": 1,
                "solution": "<strong>NCERT Page 209:</strong> Decomposers mineralize dead remains. Without them, nutrients would remain locked in dead biomass and natural soil replenishment would completely cease."
            },
            {
                "id": 9,
                "q": "Which of the following represents an omnivore that feeds on both producers and other consumers?",
                "options": ["Spotted deer", "Crow / Human", "Bengal tiger", "Green grasshopper"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1:</strong> Omnivores consume both plant products and meat. Crows and humans are omnivores."
            },
            {
                "id": 10,
                "q": "Which of the following is NOT an abiotic factor?",
                "options": ["Annual rainfall", "Soil pH and minerals", "Atmospheric wind", "Soil bacteria"],
                "ans": 3,
                "solution": "<strong>NCERT Section 13.1:</strong> Soil bacteria are living microorganisms and therefore constitute a biotic component, not an abiotic one."
            }
        ]
    },

    # Quiz Slide 2 (Q11 to Q20): Food Chains, Trophic Levels, 10% Law & Food Webs
    {
        "id": 18,
        "title": "Mastery Challenge Part 2: Energy Flow & Trophic Architecture",
        "subtitle": "Test Your Mastery of the 10% Law & Food Webs (Questions 11 to 20)",
        "questions": [
            {
                "id": 11,
                "q": "What proportion of sunlight falling on green leaves in a terrestrial ecosystem is captured and converted into food energy?",
                "options": ["About 10%", "About 1%", "About 25%", "About 50%"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1.1:</strong> Terrestrial green plants capture approximately 1% of the solar energy that strikes their leaves and convert it into chemical food energy."
            },
            {
                "id": 12,
                "q": "According to the 10% law, what percentage of the energy present in food is turned into an organism's own body and made available to the next trophic level?",
                "options": ["1%", "10%", "50%", "90%"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1.1:</strong> An average of 10% of the food eaten is turned into the organism's body biomass and made available for the next level of consumers."
            },
            {
                "id": 13,
                "q": "If plants at the first trophic level trap 10,000 J of energy from sunlight, how much energy reaches the secondary consumer level?",
                "options": ["1,000 J", "100 J", "10 J", "1 J"],
                "ans": 1,
                "solution": "<strong>Mathematical Derivation:</strong><br>T1 (Producers) = 10,000 J<br>T2 (Herbivores / Primary Consumers) = 10% of 10,000 J = 1,000 J<br>T3 (Secondary Consumers) = 10% of 1,000 J = <strong>100 J</strong>."
            },
            {
                "id": 14,
                "q": "Why do natural food chains rarely contain more than 3 or 4 trophic levels?",
                "options": ["Carnivores become herbivores after 4 steps", "Energy loss at each step is so great that very little usable energy remains after 4 trophic levels", "Organisms run out of oxygen at higher levels", "Sunlight cannot reach beyond 4 levels"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1.1:</strong> Because 90% of energy is lost as heat and metabolic maintenance at each level, usable energy after 4 steps is insufficient to sustain a viable population."
            },
            {
                "id": 15,
                "q": "In a pyramid of numbers for a typical terrestrial ecosystem, which trophic level contains the greatest number of individuals?",
                "options": ["Tertiary consumers", "Secondary consumers", "Primary consumers", "Producers"],
                "ans": 3,
                "solution": "<strong>NCERT Section 13.1.1:</strong> There are generally a greater number of individuals at the lower trophic levels of an ecosystem; the greatest number is of the producers."
            },
            {
                "id": 16,
                "q": "A series of branching lines showing interconnected feeding relationships among organisms is called a:",
                "options": ["Linear trophic chain", "Food web", "Biochemical cycle", "Ecological niche"],
                "ans": 1,
                "solution": "<strong>NCERT Figure 13.3 & Section 13.1.1:</strong> Instead of a straight line food chain, the branching relationships among organisms form an interconnected food web."
            },
            {
                "id": 17,
                "q": "In the pond food chain: Phytoplankton → Zooplankton → Small Fish → Water Bird, which organism occupies the second trophic level?",
                "options": ["Phytoplankton", "Zooplankton (Herbivore)", "Small Fish", "Water Bird"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1.1:</strong> Phytoplankton is at T1 (Producer); Zooplankton is at T2 (Primary consumer / herbivore); Small fish is at T3; Water bird is at T4."
            },
            {
                "id": 18,
                "q": "What happens to the remaining 90% of food energy that is NOT transferred to the next trophic level?",
                "options": ["It is destroyed into absolute nothingness violating conservation of energy", "It is lost as heat to the environment, expended during digestion, and used for respiration and work", "It travels back into the Sun as radio waves", "It turns into solid diamonds in the soil"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.1.1:</strong> The 90% is dissipated as metabolic heat during cellular respiration, digestion, movement, growth, and reproduction."
            },
            {
                "id": 19,
                "q": "If an ecosystem receives 500,000 J of incident sunlight, approximately how much energy is fixed into chemical energy by green plants?",
                "options": ["50,000 J", "5,000 J", "500 J", "50 J"],
                "ans": 1,
                "solution": "<strong>Calculation:</strong> Terrestrial plants fix 1% of incident sunlight into chemical energy: 1% of 500,000 J = 0.01 × 500,000 = <strong>5,000 J</strong>."
            },
            {
                "id": 20,
                "q": "Which of the following constitutes a food chain according to NCERT Exercise Question 2?",
                "options": ["Grass, wheat and mango", "Grass, goat and human", "Goat, cow and elephant", "Grass, fish and goat"],
                "ans": 1,
                "solution": "<strong>NCERT Exercise Q2:</strong> 'Grass, goat and human' is a valid food chain where grass is producer, goat is primary consumer, and human is secondary consumer."
            }
        ]
    },

    # Quiz Slide 3 (Q21 to Q30): Energy Flow, Biomagnification & Ozone Layer
    {
        "id": 19,
        "title": "Mastery Challenge Part 3: Unidirectional Energy, Biomagnification & Ozone",
        "subtitle": "Test Your Understanding of Sections 13.1.1 & 13.2.1 (Questions 21 to 30)",
        "questions": [
            {
                "id": 21,
                "q": "Why is the flow of energy in an ecosystem depicted as strictly unidirectional in NCERT Figure 13.4?",
                "options": ["Because energy flows in circles between plants and decomposers", "Because energy captured by autotrophs cannot revert to the Sun, and energy passing to herbivores cannot return to producers", "Because energy only travels during daylight hours", "Because predators give energy back to prey"],
                "ans": 1,
                "solution": "<strong>NCERT Page 211:</strong> The energy captured by autotrophs does not revert back to the solar input, and energy passed to herbivores does not come back to autotrophs."
            },
            {
                "id": 22,
                "q": "The phenomenon wherein non-biodegradable chemicals progressively increase in concentration at each successive trophic level is known as:",
                "options": ["Bio-diversity explosion", "Biological magnification (Biomagnification)", "Eutrophication", "Photochemical oxidation"],
                "ans": 1,
                "solution": "<strong>NCERT Page 212:</strong> Biological magnification is the progressive accumulation of non-biodegradable pesticides and chemicals at each successive trophic tier."
            },
            {
                "id": 23,
                "q": "Why do human bodies accumulate the maximum concentration of harmful pesticides like DDT in any ecosystem?",
                "options": ["Humans drink more water than other organisms", "Humans occupy the top trophic level in food chains", "Humans produce DDT internally inside the liver", "Humans have no skin pores"],
                "ans": 1,
                "solution": "<strong>NCERT Page 212:</strong> As human beings occupy the topmost position in multiple food chains, the maximum concentration of these non-biodegradable chemicals accumulates in our bodies."
            },
            {
                "id": 24,
                "q": "What is the molecular chemical formula of ozone?",
                "options": ["O", "O₂", "O₃", "O₄"],
                "ans": 2,
                "solution": "<strong>NCERT Section 13.2.1:</strong> Ozone ($O_3$) is a triatomic molecule formed by three atoms of oxygen."
            },
            {
                "id": 25,
                "q": "While diatomic oxygen (O2) is vital for aerobic life, what is the chemical nature of ozone (O3) at ground level?",
                "options": ["It is a harmless sweet-smelling perfume", "It is a deadly poison and respiratory irritant", "It is a liquid drinkable medicine", "It acts as a plant nutrient"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.2.1:</strong> 'While O2 is essential for all aerobic forms of life, ozone is a deadly poison.'"
            },
            {
                "id": 26,
                "q": "What essential ecological shield does the stratospheric ozone layer provide for living organisms on Earth?",
                "options": ["It blocks meteorite impacts", "It shields the Earth's surface from harmful solar ultraviolet (UV) radiation", "It prevents all atmospheric oxygen from escaping into outer space", "It reflects visible light to create nighttime"],
                "ans": 1,
                "solution": "<strong>NCERT Section 13.2.1:</strong> Stratospheric ozone shields the surface of the Earth from damaging ultraviolet (UV) radiation from the Sun."
            },
            {
                "id": 27,
                "q": "What happens in the first step of ozone formation when high-energy UV radiation strikes an O2 molecule in the stratosphere?",
                "options": ["O2 burns into carbon dioxide", "High-energy UV radiation splits molecular oxygen (O2) into two free nascent oxygen (O) atoms", "O2 freezes into ice crystals", "O2 turns into water vapor"],
                "ans": 1,
                "solution": "<strong>NCERT Page 213:</strong> High-energy UV radiation splits molecular oxygen ($O_2$) into free oxygen ($O$) atoms: $O_2 \\xrightarrow{UV} O + O$."
            },
            {
                "id": 28,
                "q": "Which synthetic chemical family was primarily responsible for the rapid depletion of stratospheric ozone observed in the 1980s?",
                "options": ["Dichlorodiphenyltrichloroethane (DDT)", "Chlorofluorocarbons (CFCs)", "Polyethene polymers", "Methane gas"],
                "ans": 1,
                "solution": "<strong>NCERT Page 213:</strong> Stratospheric ozone depletion has been directly linked to synthetic chlorofluorocarbons (CFCs) used as refrigerants and in fire extinguishers."
            },
            {
                "id": 29,
                "q": "In 1987, what international action was forged under the United Nations Environment Programme (UNEP)?",
                "options": ["An agreement to ban all motor vehicles", "The Montreal Protocol agreement to freeze CFC production at 1986 levels", "A treaty to stop all agricultural farming", "A mandate to build glass domes over all cities"],
                "ans": 1,
                "solution": "<strong>NCERT Page 213:</strong> In 1987, UNEP succeeded in forging an agreement to freeze CFC production at 1986 levels, leading to mandatory CFC-free refrigerators worldwide."
            },
            {
                "id": 30,
                "q": "Why can pesticide residues accumulated in our food grains, fruits, and meat NOT be completely removed by washing?",
                "options": ["Water causes pesticides to multiply", "Pesticides are absorbed internally into plant cells and animal lipid tissues during growth", "Pesticides evaporate into gold upon washing", "Washing creates new radioactive isotopes"],
                "ans": 1,
                "solution": "<strong>NCERT Page 212:</strong> Pesticides are absorbed through the roots along with water and minerals, becoming integrated into internal plant tissues and fats where washing cannot remove them."
            }
        ]
    },

    # Quiz Slide 4 (Q31 to Q40): Waste Management, Biodegradability & NCERT Exercises
    {
        "id": 20,
        "title": "Mastery Challenge Part 4: Waste Disposal & Complete NCERT Exercises",
        "subtitle": "Test Your Mastery of Waste Chemistry & End-of-Chapter Exercises (Questions 31 to 40)",
        "questions": [
            {
                "id": 31,
                "q": "Which of the following groups contains ONLY biodegradable items (NCERT Exercise Q1)?",
                "options": ["Grass, wood and plastic", "Fruit-peels, cake and lime-juice", "Polythene bags, cake and grass", "Aluminium foil, leather and plastic"],
                "ans": 1,
                "solution": "<strong>NCERT Exercise Q1:</strong> Fruit-peels, cake, and lime-juice are all organic matter that can be broken down by saprophytic bacteria and fungi."
            },
            {
                "id": 32,
                "q": "Which of the following is considered an environment-friendly practice (NCERT Exercise Q3)?",
                "options": ["Carrying cloth-bags to put purchases in while shopping", "Switching off unnecessary lights and fans", "Walking to school instead of taking a motorized scooter", "All of the above"],
                "ans": 3,
                "solution": "<strong>NCERT Exercise Q3:</strong> All listed practices reduce energy consumption, conserve fossil fuels, and eliminate plastic waste generation."
            },
            {
                "id": 33,
                "q": "Why was the large-scale introduction of disposable clay cups (kulhads) on Indian railway trains abandoned?",
                "options": ["Clay cups melted in hot tea", "Making kulhads on a massive scale caused catastrophic loss of fertile agricultural top-soil", "Kulhads released poisonous chlorine gas", "Passengers preferred drinking directly from teapots"],
                "ans": 1,
                "solution": "<strong>NCERT Page 215 (Think It Over):</strong> A little thought showed that making kulhads on a large scale would result in the loss of fertile top-soil crucial for agriculture."
            },
            {
                "id": 34,
                "q": "What is the biological reason why enzymes in soil bacteria cannot decompose human-made plastics?",
                "options": ["Plastics are too cold for bacteria to touch", "Enzymes are specific in their action and bacteria lack enzymes to cleave synthetic plastic bonds", "Plastics emit electrical shocks that destroy bacterial DNA", "Bacteria only consume metal cans"],
                "ans": 1,
                "solution": "<strong>NCERT Page 214:</strong> Enzymes are specific in their action. Microorganisms possess enzymes for natural organic polymers, but none for synthetic petroleum-based plastic polymers."
            },
            {
                "id": 35,
                "q": "What will happen if we kill all organisms in one trophic level, such as all herbivores in a grassland (NCERT Exercise Q4)?",
                "options": ["The ecosystem becomes completely stable and self-repairing", "Higher carnivores starve due to lack of food, while producers overgrow unchecked, destabilizing the entire ecosystem", "The Sun stops radiating ultraviolet light", "Decomposers turn all soil into solid plastic"],
                "ans": 1,
                "solution": "<strong>NCERT Exercise Q4:</strong> Organisms at the higher trophic level starve to death, while organisms at the lower level multiply uncontrollably, causing severe ecological collapse."
            },
            {
                "id": 36,
                "q": "If all waste generated by humans were 100% biodegradable, will this have NO impact on the environment (NCERT Exercise Q8)?",
                "options": ["Yes, it will have absolutely zero negative impact on the planet", "No, massive unmanaged heaps of rotting waste cause foul stench, breed disease vectors, emit methane, and deplete aquatic oxygen", "Yes, because biodegradable waste turns into gold automatically", "Yes, because bacteria consume all waste within one second"],
                "ans": 1,
                "solution": "<strong>NCERT Exercise Q8:</strong> Even biodegradable waste, if generated in huge quantities and left untreated, rots anaerobically, emitting greenhouse methane, causing foul odor, breeding disease vectors, and causing water eutrophication."
            },
            {
                "id": 37,
                "q": "In municipal waste management systems, what is the purpose of source segregation into green and blue bins?",
                "options": ["To separate waste by color matching clothes", "To separate biodegradable wet waste for composting from dry recyclable waste for industrial remanufacturing", "To hide plastic waste inside paper waste", "To burn all garbage together at higher temperatures"],
                "ans": 1,
                "solution": "<strong>NCERT Activity 13.7:</strong> Green bins collect biodegradable wet organic waste for composting/biogas, while blue bins collect clean dry recyclables for processing."
            },
            {
                "id": 38,
                "q": "Which of the following hazardous materials must be carefully handled when disposing of electronic waste (e-waste, Activity 13.9)?",
                "options": ["Pure water and table salt", "Toxic heavy metals like lead, mercury, and cadmium", "Vitamins A, C, and D", "Glucose and cane sugar"],
                "ans": 1,
                "solution": "<strong>NCERT Activity 13.9:</strong> E-waste contains hazardous heavy metals like lead, mercury, and cadmium that contaminate soil and groundwater if dumped in landfills."
            },
            {
                "id": 39,
                "q": "In the waste hierarchy, which 'R' represents preventing waste generation before it even occurs?",
                "options": ["Recycle", "Refuse", "Repurpose", "Rot"],
                "ans": 1,
                "solution": "<strong>5 R's Framework:</strong> 'Refuse' (saying no to single-use plastics and unnecessary packaging) stops waste before it enters the stream."
            },
            {
                "id": 40,
                "q": "Can organisms of any single trophic level be removed without causing any damage to the ecosystem (NCERT Exercise Q5)?",
                "options": ["Yes, apex predators can always be removed with zero consequence", "Yes, primary consumers can be eliminated safely", "No, every trophic level is an integral link; removing any level causes starvation above and overpopulation below", "Yes, decomposers can be removed without any impact"],
                "ans": 2,
                "solution": "<strong>NCERT Exercise Q5:</strong> No trophic level can be removed without causing damage because all levels are interdependent links in the transfer of energy and population regulation."
            }
        ]
    }
]


# -*- coding: utf-8 -*-
"""
Generate Part 3 (Slides 17 to 20) for Class 10 Science Chapter 13: Our Environment
40 challenge questions across 4 silent review slides with 3-step solutions
"""

import json

slides_part3 = [
    {
        "id": 17,
        "title": "Ecosystem Energy Review",
        "subtitle": "Challenge review covering biotic and abiotic factors, producers, and solar energy capture",
        "speech": "",
        "questions": [
            {
                "question": "Which of the following groups contains only biodegradable items?",
                "options": [
                    "Grass, flowers and leather",
                    "Grass, wood and plastic",
                    "Fruit-peels, cake and lime-juice",
                    "Cake, wood and grass"
                ],
                "answer": 0,
                "hint": "Check which materials are purely derived from plants or animals without synthetic polymers.",
                "explanation": "Grass, flowers, and leather are all natural organic materials derived from living organisms that can be fully broken down by microbial decomposers.",
                "solution_steps": [
                    "Step 1: Identify the origin of each item in the group. Grass and flowers are plant matter consisting of cellulose; leather is animal hide consisting of collagen protein.",
                    "Step 2: Evaluate microbial decomposition pathways. Saprophytic bacteria and fungi possess specific enzymes to digest cellulose and natural animal proteins.",
                    "Step 3: Conclude that since all three components degrade naturally via biological action, they are completely biodegradable."
                ]
            },
            {
                "question": "Which of the following constitutes a correct linear aquatic food chain?",
                "options": [
                    "Grass, wheat and mango",
                    "Grass, goat and human",
                    "Phytoplankton, zooplankton and small fish",
                    "Grass, fish and goat"
                ],
                "answer": 2,
                "hint": "Look for microscopic producers followed by aquatic consumers.",
                "explanation": "In an aquatic habitat, microscopic photosynthetic algae (phytoplankton) are eaten by microscopic animals (zooplankton), which are eaten by small fish.",
                "solution_steps": [
                    "Step 1: Identify the primary autotrophic producer in an aquatic water body (microscopic algae/phytoplankton).",
                    "Step 2: Trace the primary consumer (herbivorous zooplankton) that feeds on phytoplankton in the water column.",
                    "Step 3: Confirm that small carnivorous fish prey upon zooplankton, forming a continuous, valid aquatic food chain."
                ]
            },
            {
                "question": "If 100,000 J of solar sunlight strikes the leaves of green plants, how much food energy is captured into plant tissues?",
                "options": [
                    "10,000 J",
                    "1,000 J",
                    "100 J",
                    "10 J"
                ],
                "answer": 1,
                "hint": "Recall the percentage of incident solar energy captured by terrestrial green plants (1%).",
                "explanation": "Terrestrial green plants capture on average only about 1% of the total incident solar energy falling upon their leaves into synthesized chemical energy.",
                "solution_steps": [
                    "Step 1: Note the given incident solar radiation = 100,000 J.",
                    "Step 2: Apply the photosynthetic solar energy capture rule for terrestrial plants, which is 1% of total incident light: 1% × 100,000 J.",
                    "Step 3: Calculate: 0.01 × 100,000 J = 1,000 J of synthesized food energy stored in plant biomass."
                ]
            },
            {
                "question": "Which component of an ecosystem converts inorganic carbon dioxide and water into organic glucose?",
                "options": [
                    "Primary consumers (herbivores)",
                    "Decomposers (bacteria and fungi)",
                    "Autotrophic producers (green plants)",
                    "Tertiary consumers (carnivores)"
                ],
                "answer": 2,
                "hint": "Identify the organisms that possess chlorophyll and perform photosynthesis.",
                "explanation": "Producers contain chlorophyll pigments that absorb light energy to drive the photosynthetic reduction of carbon dioxide and water into glucose carbohydrates.",
                "solution_steps": [
                    "Step 1: Recall the biochemical equation of photosynthesis: 6 CO2 + 6 H2O + sunlight -> C6H12O6 + 6 O2.",
                    "Step 2: Identify that this transformation requires chlorophyll pigments to trap solar photons.",
                    "Step 3: Conclude that only autotrophic green plants and cyanobacteria function as ecological producers performing this conversion."
                ]
            },
            {
                "question": "Why is an agricultural crop-field classified as an artificial ecosystem?",
                "options": [
                    "It has no living biotic organisms",
                    "It is created, cultivated, and managed by human beings",
                    "It does not receive any natural sunlight or rain",
                    "It contains exclusively non-biodegradable synthetic matter"
                ],
                "answer": 1,
                "hint": "Consider whether human intervention is required for planting, weeding, and harvesting.",
                "explanation": "A crop field is an artificial ecosystem because humans clear the land, plant selected monoculture crops, provide artificial irrigation and fertilizers, and harvest the biomass.",
                "solution_steps": [
                    "Step 1: Distinguish natural ecosystems (forests, lakes) that develop and sustain without human intervention from artificial ones.",
                    "Step 2: Note that agricultural fields require continuous human labor, tilling, seeding, weeding, chemical pest management, and harvesting.",
                    "Step 3: Conclude that human manipulation and purposeful maintenance define crop fields as artificial ecosystems."
                ]
            },
            {
                "question": "Which of the following is an abiotic physical parameter that regulates an ecosystem?",
                "options": [
                    "Photosynthetic cyanobacteria",
                    "Soil temperature and annual rainfall",
                    "Microbial decomposers in humus",
                    "Parasitic dodder vines (Cuscuta)"
                ],
                "answer": 1,
                "hint": "Look for non-living climatic or physical factors.",
                "explanation": "Abiotic factors are non-living physical components such as ambient temperature, rainfall, sunlight, soil mineral texture, and wind velocity.",
                "solution_steps": [
                    "Step 1: Define abiotic components as non-living physical and chemical elements of an environment.",
                    "Step 2: Screen the options: cyanobacteria, fungi, and Cuscuta are living biological organisms (biotic).",
                    "Step 3: Confirm that temperature and rainfall are non-living meteorological abiotic factors."
                ]
            },
            {
                "question": "What is the primary ecological hazard of having zero decomposers in a forest ecosystem?",
                "options": [
                    "Immediate overproduction of atmospheric oxygen",
                    "Cessation of nutrient cycling and accumulation of dead biomass",
                    "Uncontrolled rapid proliferation of primary herbivores",
                    "Accelerated conversion of solar energy into coal beds"
                ],
                "answer": 1,
                "hint": "Consider what happens when dead leaves and animals are never broken down.",
                "explanation": "Without decomposers, dead organic matter and animal wastes would accumulate endlessly, locking away vital mineral nutrients and depriving plant roots of nourishment.",
                "solution_steps": [
                    "Step 1: Decomposers break down complex organic polymers in dead matter into simple inorganic soil minerals (mineralization).",
                    "Step 2: If decomposers are absent, organic detritus piles up indefinitely across the forest floor.",
                    "Step 3: Soil mineral reservoirs deplete because nutrients remain locked in carcasses, causing plant starvation and trophic collapse."
                ]
            },
            {
                "question": "Which organism is an example of a consumer that acts as an external parasite on animals?",
                "options": [
                    "Earthworm in soil",
                    "Leech on cattle skin",
                    "Fungi on fallen logs",
                    "Algae on pond rocks"
                ],
                "answer": 1,
                "hint": "Identify the blood-sucking organism that attaches to a living host to feed.",
                "explanation": "Leeches and ticks are ectoparasites that attach to host organisms to derive nutritional blood and fluids without immediately killing the host.",
                "solution_steps": [
                    "Step 1: Recall the definition of a parasite: an organism that lives on or in a host, obtaining food directly from the host tissues without immediate slaughter.",
                    "Step 2: Evaluate the options: earthworms are detritivores; fungi are saprophytes; algae are autotrophs; leeches are ectoparasites.",
                    "Step 3: Conclude that leeches feeding on host skin represent specialized parasitic consumers."
                ]
            },
            {
                "question": "In the terrestrial food chain: Tree -> Insects -> Woodpecker -> Falcon, what is the role of the woodpecker?",
                "options": [
                    "Primary producer",
                    "Primary consumer (herbivore)",
                    "Secondary consumer (carnivore)",
                    "Tertiary apex decomposer"
                ],
                "answer": 2,
                "hint": "Insects eat trees (primary consumer), so what trophic role does the insect-eating bird have?",
                "explanation": "The tree is producer (level 1), insects are primary consumers (level 2), woodpecker is a secondary consumer eating insects (level 3), and falcon is tertiary consumer (level 4).",
                "solution_steps": [
                    "Step 1: Assign trophic levels sequentially: Trophic level 1 = Tree (Autotrophic Producer).",
                    "Step 2: Assign Level 2 = Insects feeding on tree bark/leaves (Primary Consumer).",
                    "Step 3: Assign Level 3 = Woodpecker preying on insects (Secondary Consumer)."
                ]
            },
            {
                "question": "Why do natural freshwater ponds remain clean without human intervention while glass aquariums require frequent cleaning?",
                "options": [
                    "Pond water contains zero living fish or organic waste",
                    "Ponds possess natural balanced cycles of decomposers, aquatic plants, and sediment filtration",
                    "Pond fish do not produce any metabolic ammonia or feces",
                    "Sunlight completely evaporates all pond waste molecules instantly"
                ],
                "answer": 1,
                "hint": "Natural ecosystems are self-sustaining units with complete nutrient cycling.",
                "explanation": "Natural ponds are complete, self-sustaining ecosystems where microbial decomposers and plants balance waste production, whereas small aquariums rapidly accumulate toxins.",
                "solution_steps": [
                    "Step 1: Recognize that natural ponds have large volumes, balanced food webs, and extensive benthic microbial decomposers.",
                    "Step 2: In contrast, an aquarium is an artificial, high-density closed tank lacking natural hydrological turnover.",
                    "Step 3: Uneaten food and fish feces quickly overwhelm the small bacterial community in an aquarium, requiring manual cleaning."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Trophic Dynamics Review",
        "subtitle": "Challenge review covering 10% law, food webs, biomagnification, and energy pyramids",
        "speech": "",
        "questions": [
            {
                "question": "If autotrophs in an ecosystem fix 10,000 J of energy, how much energy reaches tertiary consumers according to Lindeman's 10% law?",
                "options": [
                    "1,000 J",
                    "100 J",
                    "10 J",
                    "1 J"
                ],
                "answer": 2,
                "hint": "Apply the 10% reduction three times: producers -> primary -> secondary -> tertiary.",
                "explanation": "Producers have 10,000 J. Herbivores get 10% (1,000 J). Secondary consumers get 10% (100 J). Tertiary consumers get 10% (10 J).",
                "solution_steps": [
                    "Step 1: First trophic level (Producers): 10,000 J.",
                    "Step 2: Second trophic level (Herbivores): 10,000 × 0.10 = 1,000 J; Third level (Secondary consumers): 1,000 × 0.10 = 100 J.",
                    "Step 3: Fourth trophic level (Tertiary consumers): 100 × 0.10 = 10 J."
                ]
            },
            {
                "question": "What happens if all organisms in a specific trophic level (e.g., all herbivores) are completely removed from a food chain?",
                "options": [
                    "The ecosystem becomes permanently more productive and diverse",
                    "Producer populations overgrow while carnivore populations starve and collapse",
                    "Carnivores instantly become photosynthetic autotrophs to survive",
                    "Energy flow reverses from decomposers back to the Sun"
                ],
                "answer": 1,
                "hint": "Consider the impact on the organisms below (no grazing) and organisms above (no food).",
                "explanation": "Removing herbivores removes the food supply for carnivores, causing carnivore starvation and death, while producer vegetation overgrows unchecked due to absence of grazing.",
                "solution_steps": [
                    "Step 1: Analyze the trophic level directly above herbivores (carnivores): deprived of their only food source, they face starvation, migration, or death.",
                    "Step 2: Analyze the trophic level below herbivores (producers): without grazing pressure, plant populations multiply excessively until resource competition halts growth.",
                    "Step 3: Conclude that removing any intermediate trophic level disrupts ecological balance and triggers a catastrophic trophic cascade."
                ]
            },
            {
                "question": "In a biological magnification ladder: Water -> Algae -> Small Fish -> Large Fish -> Fish-eating Bird, which organism has the highest pesticide concentration?",
                "options": [
                    "Water",
                    "Algae",
                    "Small Fish",
                    "Fish-eating Bird"
                ],
                "answer": 3,
                "hint": "Biomagnification concentrates non-biodegradable chemicals to the greatest extent at the top trophic level.",
                "explanation": "Because non-biodegradable chemicals cannot be excreted or metabolized, their concentration multiplies at each consecutive step, reaching peak levels in the apex predator (fish-eating bird).",
                "solution_steps": [
                    "Step 1: Identify that pesticides are persistent and non-biodegradable, accumulating in organism tissues without excretion.",
                    "Step 2: As organisms at higher trophic levels consume many lower-level organisms, the accumulated chemical dosage concentrates progressively.",
                    "Step 3: The fish-eating bird occupies the top trophic level of this chain, accumulating the highest parts-per-million concentration of toxic pesticide."
                ]
            },
            {
                "question": "Why do food chains in natural ecosystems rarely exceed four or five trophic levels?",
                "options": [
                    "Predators become physically too large to find shelters",
                    "Ninety percent of energy is lost at each step, leaving insufficient energy to sustain viable populations",
                    "Decomposers refuse to digest animals with more than four ancestors",
                    "Higher-level animals run out of atmospheric nitrogen"
                ],
                "answer": 1,
                "hint": "Recall that 90% of energy is dissipated as heat and metabolic work at every trophic step.",
                "explanation": "Because on average 90% of energy is dissipated at every trophic transfer, the remaining fraction after 4 to 5 levels is too minute to support another reproductive population.",
                "solution_steps": [
                    "Step 1: Recall Lindeman's 10% law: only 10% of ingested energy is stored as body biomass for the next level.",
                    "Step 2: Calculate energy fractions: Level 1 = 100%, Level 2 = 10%, Level 3 = 1%, Level 4 = 0.1%, Level 5 = 0.01%.",
                    "Step 3: At 0.01% or less, available energy cannot meet the basal metabolic and hunting demands of an additional consumer tier."
                ]
            },
            {
                "question": "Which of the following statements about the flow of energy in an ecosystem is TRUE?",
                "options": [
                    "Energy flows cyclicly between consumers and the Sun",
                    "Energy flow is strictly unidirectional and progressively decreases at higher trophic levels",
                    "Energy increases exponentially as it moves toward apex predators",
                    "Decomposers pump metabolic heat back into plant roots for photosynthesis"
                ],
                "answer": 1,
                "hint": "Energy moves in one direction only and dissipates as heat along the chain.",
                "explanation": "Energy flows in a single direction from the Sun to autotrophs and consumers without reversing, and dissipates as metabolic heat at every transition.",
                "solution_steps": [
                    "Step 1: Check directionality: solar photons captured by plants cannot return to the Sun; heat lost to the environment cannot be reconverted to chemical food.",
                    "Step 2: Check magnitude: energy diminishes at each successive trophic transfer due to 90% metabolic dissipation.",
                    "Step 3: Conclude that energy flow is strictly unidirectional and progressively diminishing."
                ]
            },
            {
                "question": "What structural advantage does an interconnected food web possess over an isolated linear food chain?",
                "options": [
                    "It eliminates all energy loss during cellular respiration",
                    "It offers alternative food sources, increasing community resilience against single-species collapses",
                    "It converts non-biodegradable plastics into biodegradable compost",
                    "It prevents producers from needing solar radiation"
                ],
                "answer": 1,
                "hint": "Having multiple dietary pathways prevents starvation if one prey species declines.",
                "explanation": "A food web contains multiple interconnected pathways. If one prey species is decimated, polyphagous predators switch to alternative prey, preventing community collapse.",
                "solution_steps": [
                    "Step 1: Contrast linear food chains (where organisms rely on a single prey species) with food webs (multiple alternative prey links).",
                    "Step 2: Recognize that if a disease or drought wipes out one prey in a food web, predators can shift feeding to alternative species.",
                    "Step 3: This dietary flexibility stabilizes predator numbers and gives depleted prey time to recover, providing ecological resilience."
                ]
            },
            {
                "question": "In a forest ecosystem, if deer consume 5,000 kg of plant leaves, approximately how much new herbivore biomass is produced?",
                "options": [
                    "5,000 kg",
                    "500 kg",
                    "50 kg",
                    "5 kg"
                ],
                "answer": 1,
                "hint": "Apply the 10% ecological biomass transfer efficiency rule.",
                "explanation": "According to the 10% law, approximately 10% of ingested organic biomass is converted into new consumer tissue (body biomass). 10% of 5,000 kg = 500 kg.",
                "solution_steps": [
                    "Step 1: Ingested food biomass = 5,000 kg.",
                    "Step 2: Average biomass assimilation efficiency across trophic levels = 10%.",
                    "Step 3: Calculate: 0.10 × 5,000 kg = 500 kg of new deer biomass."
                ]
            },
            {
                "question": "Why do humans accumulate the highest concentrations of DDT and heavy metals in agricultural landscapes?",
                "options": [
                    "Humans drink the largest volume of groundwater per day",
                    "Humans occupy the top trophic position in diverse omnivorous food chains",
                    "Human skin directly absorbs airborne pesticides more rapidly than plant leaves",
                    "Human digestive enzymes synthesize DDT internally from glucose"
                ],
                "answer": 1,
                "hint": "Consider the position of humans in food chains and the principle of biomagnification.",
                "explanation": "Because humans are apex omnivores feeding on both plant crops and herbivorous/carnivorous animals, accumulated non-biodegradable toxins reach maximum concentration in humans.",
                "solution_steps": [
                    "Step 1: Recall that biomagnification escalates toxin concentrations at each successive trophic level.",
                    "Step 2: Humans sit at the terminal, top trophic position of many terrestrial and aquatic food chains.",
                    "Step 3: Consuming accumulated toxins from agricultural plants, livestock meat, and fish concentrates the highest chemical burden in human tissues."
                ]
            },
            {
                "question": "Which ecological diagram always has a broad upright base that tapers toward the top in all natural ecosystems?",
                "options": [
                    "Pyramid of energy",
                    "Pyramid of pesticide concentrations",
                    "Pyramid of atmospheric pressure",
                    "Pyramid of toxic heavy metals"
                ],
                "answer": 0,
                "hint": "Available energy is always greatest at the producer base and least at the apex.",
                "explanation": "The pyramid of energy is always strictly upright because energy is progressively lost as heat at each transfer from producers to top consumers.",
                "solution_steps": [
                    "Step 1: Producers capture the maximum energy from sunlight at the base of the ecosystem.",
                    "Step 2: At each consecutive transfer, 90% of energy is dissipated as metabolic heat and respiration.",
                    "Step 3: Therefore, energy content decreases monotonically at each level, ensuring the energy pyramid is always upright."
                ]
            },
            {
                "question": "Which of the following practices is considered genuinely eco-friendly?",
                "options": [
                    "Carrying cloth bags for shopping instead of accepting plastic bags",
                    "Switching on all house lights to deter nocturnal insects",
                    "Using motor scooters for traveling 100-meter distances",
                    "Burning plastic trash in garden backyards"
                ],
                "answer": 0,
                "hint": "Look for an action that reduces single-use non-biodegradable waste.",
                "explanation": "Using reusable cloth bags reduces non-biodegradable plastic production and landfill disposal, conserving resources and preventing environmental pollution.",
                "solution_steps": [
                    "Step 1: Evaluate each option against environmental sustainability principles.",
                    "Step 2: Burning plastic releases toxic dioxins; unnecessary electricity and vehicle use burns fossil fuels.",
                    "Step 3: Carrying reusable cloth bags minimizes single-use plastic waste generation and is a model eco-friendly habit."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Ozone Chemistry Review",
        "subtitle": "Challenge review covering stratospheric ozone formation, UV radiation, CFCs, and Montreal Protocol",
        "speech": "",
        "questions": [
            {
                "question": "At which atmospheric layer is ozone predominantly concentrated as a protective shield for life on Earth?",
                "options": [
                    "Troposphere (0 to 10 km)",
                    "Stratosphere (15 to 30 km)",
                    "Mesosphere (50 to 85 km)",
                    "Ionosphere (above 100 km)"
                ],
                "answer": 1,
                "hint": "The ozone layer is located in the atmospheric stratum directly above the troposphere.",
                "explanation": "The ozone layer resides in the stratosphere, approximately 15 to 30 kilometers above sea level, where it absorbs hazardous ultraviolet solar radiation.",
                "solution_steps": [
                    "Step 1: Identify Earth's atmospheric layers: Troposphere (ground level), Stratosphere (above troposphere), Mesosphere, Thermosphere.",
                    "Step 2: Ground-level tropospheric ozone is a pollutant; high-altitude stratospheric ozone forms the protective planetary shield.",
                    "Step 3: Conclude that the ozone layer is located in the stratosphere between 15 and 30 km altitude."
                ]
            },
            {
                "question": "What is the primary biological hazard associated with the depletion of the stratospheric ozone layer?",
                "options": [
                    "Increased atmospheric oxygen leading to global forest fires",
                    "Excess UV radiation reaching Earth, causing skin cancer, cataracts, and DNA mutations",
                    "Immediate global freezing of all freshwater lakes",
                    "Sudden cessation of all microbial photosynthesis"
                ],
                "answer": 1,
                "hint": "Ozone filters out high-energy ultraviolet radiation that damages living cells.",
                "explanation": "Ozone depletion allows high-energy UV-B radiation to penetrate to Earth's surface, where it breaks DNA bonds, provoking skin melanoma, cataract blindness, and cellular mutations.",
                "solution_steps": [
                    "Step 1: Ozone absorbs harmful solar ultraviolet (UV) radiation, especially UV-B rays.",
                    "Step 2: When the ozone layer thins, higher doses of UV radiation reach Earth's surface.",
                    "Step 3: High-energy UV radiation damages nucleic acids in living cells, causing skin cancers, immune suppression, and eye cataracts."
                ]
            },
            {
                "question": "What photochemical equation represents the formation of a nascent oxygen atom by solar UV radiation?",
                "options": [
                    "O2 + UV -> O + O",
                    "O3 + UV -> O2 + O",
                    "CO2 + UV -> C + O2",
                    "H2O + UV -> H2 + O"
                ],
                "answer": 0,
                "hint": "Molecular oxygen (O2) is split by UV radiation into two individual oxygen atoms.",
                "explanation": "Energetic ultraviolet photons cleave the covalent double bond of diatomic oxygen (O2), liberating two highly reactive nascent oxygen atoms (O + O).",
                "solution_steps": [
                    "Step 1: High-energy UV photons possess sufficient quantum energy to photolyse molecular oxygen bonds.",
                    "Step 2: The reaction breaks O2 into two unbonded oxygen atoms: O2 + UV -> O + O.",
                    "Step 3: These liberated nascent oxygen atoms then react with intact O2 molecules to synthesize ozone (O3)."
                ]
            },
            {
                "question": "How does a free chlorine radical from CFCs catalytically destroy thousands of ozone molecules?",
                "options": [
                    "It physically blocks solar UV radiation from reaching O2",
                    "It attacks O3 to form ClO and O2, and is then regenerated by reaction with nascent oxygen",
                    "It freezes stratospheric water into opaque ice sheets",
                    "It combines permanently with nitrogen to form inert rock crystals"
                ],
                "answer": 1,
                "hint": "A catalyst participates in a reaction but is regenerated at the end to repeat the cycle.",
                "explanation": "Cl + O3 -> ClO + O2, followed by ClO + O -> Cl + O2. The chlorine radical is regenerated unchanged, allowing a single Cl atom to destroy over 100,000 ozone molecules.",
                "solution_steps": [
                    "Step 1: Chlorine radical attacks ozone: Cl + O3 -> ClO + O2.",
                    "Step 2: Chlorine monoxide reacts with a free oxygen atom: ClO + O -> Cl + O2.",
                    "Step 3: The chlorine radical (Cl) is regenerated unchanged to attack another ozone molecule in a repeating catalytic chain."
                ]
            },
            {
                "question": "What international agreement signed in 1987 under UNEP successfully froze CFC production at 1986 levels?",
                "options": [
                    "Kyoto Protocol",
                    "Montreal Protocol",
                    "Paris Climate Agreement",
                    "Stockholm Declaration"
                ],
                "answer": 1,
                "hint": "Named after the Canadian city of Montreal where the ozone protection treaty was signed.",
                "explanation": "The 1987 Montreal Protocol was forged under the United Nations Environment Programme (UNEP) to freeze and phase out the global production of ozone-depleting CFCs.",
                "solution_steps": [
                    "Step 1: Atmospheric discovery of the Antarctic ozone hole in the 1980s prompted rapid international scientific and political response.",
                    "Step 2: In 1987, UNEP negotiated the Montreal Protocol on Substances that Deplete the Ozone Layer.",
                    "Step 3: The treaty froze CFC production at 1986 levels and mandated a global phase-out, leading to modern CFC-free refrigeration."
                ]
            },
            {
                "question": "Why is ozone gas considered both a deadly poison and an indispensable protective shield?",
                "options": [
                    "It is healthy when breathed by humans but toxic to green plants",
                    "It is a lethal respiratory toxin at ground level but shields the biosphere from lethal UV radiation in the stratosphere",
                    "It dissolves mineral rock into drinking water but corrodes iron pipes",
                    "It cools polar ice caps while heating desert sand dunes"
                ],
                "answer": 1,
                "hint": "Location matters: harmful in the troposphere (where we breathe) versus beneficial in the stratosphere.",
                "explanation": "At tropospheric ground level, ozone is an aggressive oxidant and respiratory poison. In the high stratosphere, however, it absorbs damaging ultraviolet radiation.",
                "solution_steps": [
                    "Step 1: At ground level (troposphere), O3 is a strong irritant that damages lung tissues and living cells.",
                    "Step 2: In the stratosphere (15-30 km above ground), O3 absorbs high-energy UV-B and UV-C solar photons.",
                    "Step 3: Without this high-altitude shielding, solar UV would sterilize terrestrial life and cause severe genetic damage."
                ]
            },
            {
                "question": "Which of the following devices previously utilized large quantities of chlorofluorocarbons (CFCs)?",
                "options": [
                    "Domestic refrigerators and fire extinguishers",
                    "Clay water pots and incandescent bulbs",
                    "Electric dry cells and bicycle dynamos",
                    "Solar water heaters and windmill turbines"
                ],
                "answer": 0,
                "hint": "CFCs served as non-flammable coolants in cooling appliances and aerosol propellants.",
                "explanation": "CFCs were widely used as stable, non-toxic refrigerants in refrigerators, air conditioning units, and as foaming agents and fire extinguishing propellants.",
                "solution_steps": [
                    "Step 1: Identify that CFCs are volatile, chemically inert halogenated hydrocarbons.",
                    "Step 2: Their high enthalpy of vaporization made them ideal working fluids for compression refrigeration and air conditioning.",
                    "Step 3: Following the Montreal Protocol, CFCs were phased out and replaced with ozone-safe alternative hydrofluorocarbons and hydrocarbons."
                ]
            },
            {
                "question": "What role does the oxygen atom (O) play in the second step of stratospheric ozone synthesis?",
                "options": [
                    "It combines directly with an intact O2 molecule to produce O3",
                    "It splits ozone molecules back into carbon monoxide",
                    "It bonds with nitrogen gas to form nitric acid rain",
                    "It condenses into liquid water droplets in clouds"
                ],
                "answer": 0,
                "hint": "A single nascent oxygen atom joins a diatomic oxygen molecule: O + O2 -> O3.",
                "explanation": "The nascent oxygen atom produced in step 1 collides with an oxygen molecule (O2) in the presence of a third body to form ozone (O3).",
                "solution_steps": [
                    "Step 1: Step 1 generates free nascent oxygen atoms: O2 + UV -> O + O.",
                    "Step 2: In Step 2, each nascent oxygen atom reacts with an intact molecular oxygen: O + O2 -> O3.",
                    "Step 3: This reaction successfully synthesizes the triatomic ozone molecule."
                ]
            },
            {
                "question": "Over which geographic region was the most severe seasonal 'ozone hole' first documented in the 1980s?",
                "options": [
                    "Equatorial Amazon Basin",
                    "Antarctica (South Pole)",
                    "Sahara Desert",
                    "Greenland Ice Sheet"
                ],
                "answer": 1,
                "hint": "Extreme polar winter vortex clouds over the South Pole accelerate catalytic ozone destruction.",
                "explanation": "The seasonal thinning of stratospheric ozone, known as the ozone hole, was first detected and most severe over the Antarctic continent due to polar stratospheric clouds.",
                "solution_steps": [
                    "Step 1: Unique atmospheric conditions over Antarctica during polar winter create isolated polar stratospheric clouds (PSCs).",
                    "Step 2: Ice crystals in PSCs provide surface sites for inactive chlorine reservoirs to convert into reactive chlorine radicals.",
                    "Step 3: When sunlight returns in spring, explosive catalytic ozone destruction creates the prominent Antarctic ozone hole."
                ]
            },
            {
                "question": "What is the primary chemical difference between molecular oxygen and ozone?",
                "options": [
                    "Molecular oxygen has 2 oxygen atoms (O2); ozone has 3 oxygen atoms (O3)",
                    "Molecular oxygen contains hydrogen while ozone contains nitrogen",
                    "Molecular oxygen is a solid crystal while ozone is a dense liquid",
                    "Ozone has 4 oxygen atoms while molecular oxygen has 1"
                ],
                "answer": 0,
                "hint": "Check the molecular formulas: O2 versus O3.",
                "explanation": "Molecular oxygen is diatomic (O2), containing two oxygen atoms, while ozone is a triatomic allotrope of oxygen (O3), containing three oxygen atoms.",
                "solution_steps": [
                    "Step 1: Diatomic oxygen (O2) consists of two oxygen atoms joined by a double covalent bond.",
                    "Step 2: Ozone (O3) consists of three oxygen atoms joined in a bent resonance-stabilized triatomic structure.",
                    "Step 3: This atomic difference confers distinct physical, chemical, and biological properties to the two allotropes."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Waste Management Review",
        "subtitle": "Challenge review covering enzyme specificity, biodegradability, plastic persistence, and 5 Rs",
        "speech": "",
        "questions": [
            {
                "question": "Why are bacterial decomposers capable of digesting paper and cotton but incapable of digesting polyethylene bags?",
                "options": [
                    "Paper and cotton contain heavy metals that attract bacteria",
                    "Bacteria produce specific enzymes matching natural glycosidic bonds, but lack enzymes for synthetic plastic polymers",
                    "Polyethylene absorbs all bacterial moisture and freezes them instantly",
                    "Cotton fibers emit electrical pulses that activate bacterial digestion"
                ],
                "answer": 1,
                "hint": "Enzymes operate on a strict lock-and-key specificity for chemical bonds.",
                "explanation": "Enzymes exhibit substrate specificity. Bacteria evolved enzymes (cellulases) to cleave natural cellulose in cotton/paper, but lack enzymes to cleave synthetic C-C plastic bonds.",
                "solution_steps": [
                    "Step 1: Paper and cotton are natural cellulose biopolymers with specific beta-glycosidic bonds.",
                    "Step 2: Bacterial cellulase enzymes fit these natural bonds through lock-and-key active site configuration.",
                    "Step 3: Synthetic plastics possess unnatural synthetic polymer structures for which bacteria have no evolved digestive enzymes."
                ]
            },
            {
                "question": "What is the primary ecological downside of serving hot tea in disposable unglazed clay cups ('kulhads') across railways?",
                "options": [
                    "Clay releases poisonous lead fumes when heated by boiling tea",
                    "Making billions of kulhads strips vast quantities of fertile topsoil, worsening soil erosion",
                    "Kulhads are completely non-biodegradable and persist like plastic",
                    "Clay dissolves instantly into tea, turning it into mud soup"
                ],
                "answer": 1,
                "hint": "Manufacturing clay pots requires mining topsoil from farm fields.",
                "explanation": "Mass production of disposable clay kulhads requires excavating immense volumes of fertile agricultural topsoil, causing land degradation and threatening crop productivity.",
                "solution_steps": [
                    "Step 1: While clay is natural and biodegradable, producing hundreds of millions of daily single-use cups requires raw material.",
                    "Step 2: Potters excavate fertile topsoil from agricultural fields and burn them in rural kilns.",
                    "Step 3: Stripping topsoil causes severe farmland degradation, soil erosion, and reduces agricultural crop output."
                ]
            },
            {
                "question": "Which of the following materials is classified as NON-biodegradable in municipal solid waste audits?",
                "options": [
                    "Discarded vegetable peels",
                    "Fallen dry autumn leaves",
                    "Aluminium soft-drink cans",
                    "Shredded cardboard boxes"
                ],
                "answer": 2,
                "hint": "Look for a metal or synthetic item that cannot be broken down by bacteria.",
                "explanation": "Aluminium cans are metallic items that resist microbial breakdown and persist indefinitely unless mechanically collected and industrially remelted.",
                "solution_steps": [
                    "Step 1: Classify items into organic natural vs synthetic/metallic categories.",
                    "Step 2: Vegetable peels, leaves, and cardboard are organic plant-derived materials digestible by saprophytes.",
                    "Step 3: Aluminium is an elemental metal that cannot be digested by microorganisms, classifying it as non-biodegradable."
                ]
            },
            {
                "question": "What toxic environmental hazard occurs when biodegradable waste and non-biodegradable plastic are dumped together in landfills?",
                "options": [
                    "Plastic turns directly into nuclear radiation",
                    "Trapped organic matter rots anaerobically, generating foul methane gas and toxic leachate that poisons aquifers",
                    "Landfill soil instantly loses all gravitational attraction",
                    "Plastic decomposes into ozone gas, heating the surrounding air"
                ],
                "answer": 1,
                "hint": "Organic waste trapped under plastic layers rots without oxygen, forming foul gas and contaminated runoff.",
                "explanation": "Under impermeable plastic layers, organic waste decomposes anaerobically, releasing combustible greenhouse methane gas and producing toxic leachate that contaminates groundwater.",
                "solution_steps": [
                    "Step 1: Mixing waste prevents proper aeration, trapping organic waste beneath non-porous plastic sheets.",
                    "Step 2: Anaerobic bacteria ferment the organic waste into flammable methane gas (CH4) and organic acids.",
                    "Step 3: Rainwater seeping through the rotting mass dissolves hazardous compounds, forming toxic leachate that percolates into drinking water aquifers."
                ]
            },
            {
                "question": "What is the foremost recommendation of the 'Refuse' principle in the 5 R waste hierarchy?",
                "options": [
                    "Refuse to segregate waste at home",
                    "Say no to unnecessary single-use packaging and disposable plastic items",
                    "Refuse to use public transport or walk",
                    "Reject organic compost for agricultural crops"
                ],
                "answer": 1,
                "hint": "Preventing waste generation by declining single-use items is the first step of waste reduction.",
                "explanation": "'Refuse' means declining single-use plastics, excessive packaging, and disposable goods, preventing waste at the source before it ever enters the waste stream.",
                "solution_steps": [
                    "Step 1: The 5 R hierarchy places prevention at the pinnacle: Refuse, Reduce, Reuse, Repurpose, Recycle.",
                    "Step 2: 'Refuse' entails declining disposable cutlery, plastic carry bags, and non-essential packaging.",
                    "Step 3: Preventing waste generation at the consumer source eliminates downstream collection and disposal challenges."
                ]
            },
            {
                "question": "Why are disposable food-grade paper cups considered ecologically superior to both plastic cups and clay kulhads?",
                "options": [
                    "Paper cups last thousands of years without ever degrading",
                    "They are made from renewable tree pulp, decompose naturally, and do not strip agricultural topsoil",
                    "Paper cups eliminate all human bacterial diseases upon contact",
                    "They require zero energy or water to manufacture"
                ],
                "answer": 1,
                "hint": "Paper is biodegradable, renewable, and avoids excavating fertile soil.",
                "explanation": "Paper cups utilize renewable plant fiber, decompose naturally via microbial cellulases, maintain food hygiene, and prevent the severe topsoil stripping caused by clay kulhads.",
                "solution_steps": [
                    "Step 1: Compare with plastic: paper is biodegradable and derived from renewable plant pulp rather than non-renewable fossil petroleum.",
                    "Step 2: Compare with clay kulhads: paper production does not excavate fertile agricultural topsoil.",
                    "Step 3: Paper cups thus balance public hygiene, biodegradability, and topsoil preservation."
                ]
            },
            {
                "question": "What is the correct protocol for household waste segregation using color-coded bins?",
                "options": [
                    "Green bin for biodegradable kitchen waste; Blue bin for recyclable non-biodegradable waste",
                    "Blue bin for food scraps; Green bin for plastic bottles and glass",
                    "Red bin for paper; Yellow bin for vegetable peels; Green bin for aluminium cans",
                    "Mix all refuse together in a single black bin for street disposal"
                ],
                "answer": 0,
                "hint": "Green represents compostable organic matter; blue represents dry recyclable materials.",
                "explanation": "Standard municipal guidelines assign Green bins for wet biodegradable organic waste (food scraps, peels) and Blue bins for dry non-biodegradable recyclables (paper, plastic, metal).",
                "solution_steps": [
                    "Step 1: Wet/Organic Waste: vegetable peels, fruit rinds, leftover food belong in Green bins for composting.",
                    "Step 2: Dry/Recyclable Waste: clean plastic containers, glass bottles, metal tins, and cardboard belong in Blue bins.",
                    "Step 3: Segregating at source prevents contamination and ensures efficient composting and industrial recycling."
                ]
            },
            {
                "question": "What happens when stray cattle ingest plastic carrier bags discarded in municipal garbage heaps?",
                "options": [
                    "Plastic provides high nutrition and enhances milk output",
                    "Plastic cannot be digested, accumulating in the rumen to cause fatal alimentary blockages",
                    "Plastic is converted into natural fiber by bovine stomach enzymes",
                    "Plastic accelerates cud chewing without any health consequences"
                ],
                "answer": 1,
                "hint": "Cattle cannot digest plastic; it accumulates inside their digestive tract.",
                "explanation": "Plastics cannot be digested by ruminant stomach enzymes. Ingested bags accumulate in the rumen, forming large compact masses that cause fatal intestinal obstruction.",
                "solution_steps": [
                    "Step 1: Ruminant digestive enzymes digest cellulose and grasses, but cannot break synthetic polymers.",
                    "Step 2: Swallowed plastic bags twist and compact within the bovine stomach chambers.",
                    "Step 3: This leads to severe ruminal impaction, chronic starvation, and fatal gastrointestinal obstruction."
                ]
            },
            {
                "question": "Which of the following represents an example of 'Reusing' rather than 'Recycling' an item?",
                "options": [
                    "Melting discarded glass bottles in an industrial furnace to blow new jars",
                    "Refilling clean discarded jam jars to store kitchen pulses and spices",
                    "Reprocessing shredded PET bottles into polyester yarn for clothing",
                    "Crushing aluminium cans and smelting them into automobile parts"
                ],
                "answer": 1,
                "hint": "Reusing involves using an item again in its original physical form without reprocessing energy.",
                "explanation": "Reusing uses the existing item repeatedly without melting or reprocessing. Recycling breaks down and reprocesses materials into new products using industrial energy.",
                "solution_steps": [
                    "Step 1: Distinguish 'Reuse' (using the item again in its existing physical form) from 'Recycle' (breaking down material through chemical/thermal processing).",
                    "Step 2: Melting glass, crushing cans, and spinning PET into yarn require industrial energy and reprocessing (Recycling).",
                    "Step 3: Washing and refilling a jam jar for kitchen storage uses the existing glass vessel directly with zero reprocessing energy (Reuse)."
                ]
            },
            {
                "question": "What is the primary product of the anaerobic digestion of municipal biodegradable waste in a biogas plant?",
                "options": [
                    "Non-flammable nitrogen gas and plastic granules",
                    "Combustible methane gas fuel and nutrient-dense organic fertilizer",
                    "CFC refrigerant gas and molten sulfur",
                    "Pure synthetic petroleum and ozone gas"
                ],
                "answer": 1,
                "hint": "Anaerobic bacteria produce methane gas (biogas) and leave behind rich bio-slurry.",
                "explanation": "Anaerobic digestion of organic waste by methanogenic bacteria yields biogas (predominantly methane gas, CH4) for clean energy, and bio-slurry that serves as excellent organic fertilizer.",
                "solution_steps": [
                    "Step 1: Anaerobic digesters exclude oxygen, creating conditions for methanogenic bacterial fermentation.",
                    "Step 2: Methanogens break down complex organic acids into biogas, consisting primarily of 60-70% methane gas (CH4) and carbon dioxide.",
                    "Step 3: The remaining digested slurry is rich in nitrogen and phosphorus, serving as high-grade natural organic biofertilizer."
                ]
            }
        ]
    }
]

# Validation
print(f"Loaded {len(slides_part3)} review slides for Part 3.")
for s in slides_part3:
    assert s["speech"] == "", f"Slide {s['id']} must be silent (speech='')"
    assert len(s["title"].split()) <= 3, f"Slide {s['id']} title has more than 3 words: '{s['title']}'"
    assert len(s["questions"]) == 10, f"Slide {s['id']} must have exactly 10 questions"
    for qidx, q in enumerate(s["questions"]):
        qid = f"Slide {s['id']} Q{qidx+1}"
        assert len(q["options"]) == 4, f"{qid} must have 4 options"
        assert 0 <= q["answer"] <= 3, f"{qid} answer index out of range"
        assert "hint" in q and len(q["hint"]) > 5, f"{qid} missing valid hint"
        assert "explanation" in q and len(q["explanation"]) > 10, f"{qid} missing valid explanation"
        sol_steps = q.get("solution_steps") or q.get("solution") or q.get("steps")
        assert len(sol_steps) == 3, f"{qid} must have exactly 3 solution steps"
    slide_str = json.dumps(s)
    for forbidden in ["Raghav", "Dr.", "Dr ", "Sir", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof."]:
        assert forbidden not in slide_str, f"Forbidden term '{forbidden}' in slide {s['id']}"

with open(".agents/c10s_ch13_part3.json", "w", encoding="utf-8") as f:
    json.dump(slides_part3, f, indent=2, ensure_ascii=False)

print("Part 3 (Slides 17 to 20) validated and saved successfully!")

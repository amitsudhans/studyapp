# -*- coding: utf-8 -*-
"""
Generate Part 1 (Slides 1 to 8) for Class 10 Science Chapter 13: Our Environment
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Ecosystem Component Interactions",
        "subtitle": "Biotic community dynamics, physical abiotic factors, and self-sustaining ecological equilibrium",
        "speech": "Welcome to our comprehensive study of ecosystems and environmental biology. An ecosystem is fundamentally defined as a self-sustaining structural and functional unit of nature where living organisms interact dynamically among themselves and with their surrounding physical environment. In every ecosystem on Earth, two fundamental components operate in complete harmony. First, the biotic components encompass all living entities across taxonomic kingdoms, including photosynthetic autotrophs, diverse consumers, and microscopic saprophytes. Second, the abiotic components comprise non-living physical and climatic factors, including ambient temperature, annual rainfall, atmospheric humidity, incident solar radiation, soil mineral composition, and wind currents. Ecosystems are categorized into natural ecosystems, which function spontaneously without human interference like pristine terrestrial forests, vast grasslands, freshwater ponds, and deep lakes, versus artificial ecosystems engineered and managed by human beings, such as agricultural crop fields, botanical gardens, and aquatic glass tanks. Abiotic parameters constantly regulate the distribution, metabolic rate, reproductive success, and morphological adaptations of living communities. For example, temperature dictates enzyme kinetics, while soil minerals determine plant growth. When sunlight fuels autotrophic synthesis, matter continuously cycles between abiotic reservoirs and living biomass, sustaining structural stability across ecological boundaries. This enduring interaction ensures long-term biosphere continuity across diverse global geographic biomes.",
        "checkpoints": [
            {
                "question": "Which of the following represents an artificial, human-engineered ecosystem?",
                "options": ["Dense tropical rainforest", "Deep freshwater lake", "Agricultural crop field", "Open natural grassland"],
                "answer": 2,
                "hint": "Consider which ecosystem requires human preparation, planting, and agricultural management.",
                "explanation": "Agricultural crop fields and aquariums are artificial or human-made ecosystems, whereas forests, lakes, and grasslands develop and sustain naturally without human intervention."
            },
            {
                "question": "Which set contains solely abiotic components of an ecological environment?",
                "options": ["Soil minerals, temperature, and wind currents", "Soil bacteria, rainfall, and flowering plants", "Earthworms, ambient humidity, and nitrogen gas", "Aquatic algae, dissolved oxygen, and sunlight"],
                "answer": 0,
                "hint": "Identify factors that are non-living physical or chemical parameters.",
                "explanation": "Abiotic factors are purely non-living environmental elements such as mineral soil, temperature, rainfall, wind, and solar radiation. Bacteria, plants, algae, and worms are biotic components."
            }
        ]
    },
    {
        "id": 2,
        "title": "Artificial Aquarium Design",
        "subtitle": "Activity 13.1 artificial ecosystem architecture, aerator oxygenation, and waste cleanup",
        "speech": "In Activity 13.1 of our curriculum, we investigate the controlled design and functional operation of an artificial glass aquarium. When constructing an aquarium, we assemble a simulated aquatic habitat by combining clean water, submerged aquatic green plants like Hydrilla, aquatic fauna such as small fish, and essential mechanical life-support hardware. Unlike natural ponds and deep lakes, an aquarium possesses severe ecological constraints due to its small physical volume, absence of natural substrate turnover, and high metabolic stocking density. A mechanical aerator or air pump is strictly necessary to continuously bubble atmospheric air through the water column, ensuring adequate concentrations of dissolved oxygen for aerobic piscine respiration. Submerged green plants contribute oxygen via photosynthetic evolution during daylight hours while absorbing dissolved carbon dioxide. Furthermore, aquatic fish produce toxic nitrogenous metabolic excretions, primarily ammonia and solid organic fecal matter. In natural lakes, vast microbial decomposer communities and natural water currents efficiently dilute and recycle these wastes into harmless mineral nutrients. In a closed glass aquarium, however, decomposers cannot keep pace with waste generation, leading to lethal toxin accumulation and oxygen depletion. Consequently, artificial aquariums demand regular water renewal, glass surface scrubbing, and proactive mechanical filtration by human caretakers.",
        "checkpoints": [
            {
                "question": "Why must an aquarium aerator operate continuously in an artificial fish tank?",
                "options": ["To produce decorative bubbles for fish play", "To maintain essential dissolved oxygen levels for fish respiration", "To sterilize water against all beneficial bacterial growth", "To raise water temperature above ambient room conditions"],
                "answer": 1,
                "hint": "Fish absorb dissolved gas through their gills for aerobic respiration.",
                "explanation": "The mechanical aerator drives atmospheric oxygen into the confined water column, preventing lethal hypoxia as fish consume dissolved oxygen through respiration."
            },
            {
                "question": "Why do artificial aquariums require frequent manual cleaning whereas natural ponds do not?",
                "options": ["Natural ponds lack living fish and organic waste producers", "Natural ponds possess balanced self-cleaning decomposer and hydrological cycles", "Artificial aquariums receive excessive solar ultraviolet radiation", "Fish in natural ponds produce zero nitrogenous waste excretions"],
                "answer": 1,
                "hint": "Consider the presence of natural microbial turnover, expansive water bodies, and self-sustaining ecological balance.",
                "explanation": "Natural ponds are complete, self-sustaining ecosystems with vast bacterial decomposers and natural nutrient cycling. Small aquariums accumulate toxic wastes rapidly because decomposer communities cannot handle the confined volume."
            }
        ]
    },
    {
        "id": 3,
        "title": "Trophic Level Roles",
        "subtitle": "Autotrophic producers, macro-consumers, specialized parasites, and energy capture pathways",
        "speech": "Organisms within every ecosystem are classified into distinct functional trophic categories according to their mode of nutrition and energy acquisition. At the foundation stand producers, also designated autotrophs, which comprise chlorophyll-bearing green plants and photosynthetic cyanobacteria. Producers possess the remarkable biochemical capability to synthesize energy-rich organic compounds, namely glucose and complex starch, from simple inorganic substances like atmospheric carbon dioxide and soil water utilizing absorbed solar photons. The second functional tier comprises consumers, or heterotrophs, which cannot manufacture their own nourishment and depend directly or indirectly upon producers for sustenance. Consumers exhibit diverse dietary adaptations. Primary consumers are herbivores that feed directly upon plant tissues. Secondary and tertiary consumers are carnivores that prey upon other animal organisms. Omnivores consume both vegetal and animal matter, maintaining dietary flexibility. A specialized category consists of parasites, exemplified by non-photosynthetic flowering plants like Cuscuta, parasitic roundworms, ticks, and leeches, which derive nutritional fluids directly from the living tissues of host organisms without immediately killing them. Each functional grouping occupies a characteristic feeding position in natural communities, establishing the structural hierarchy through which solar energy captured by autotrophs is distributed to heterotrophic life. This systematic nutritional stratification maintains balanced energy flow throughout diverse terrestrial and aquatic communities.",
        "checkpoints": [
            {
                "question": "Which organism functions as a non-photosynthetic plant parasite in natural ecosystems?",
                "options": ["Hydrilla", "Cuscuta (Amarbel)", "Spirogyra", "Cyanobacteria"],
                "answer": 1,
                "hint": "Identify the yellow parasitic climber that derives nutrients directly from host trees.",
                "explanation": "Cuscuta (Amarbel) is a parasitic plant lacking chlorophyll; it sends specialized haustoria into the vascular tissues of host plants to absorb synthesized nutrients."
            },
            {
                "question": "What primary biochemical conversion characterizes ecological producers?",
                "options": ["Converting complex organic detritus into mineral rock salts", "Synthesizing organic sugars from inorganic molecules via solar energy", "Absorbing animal biomass directly through fungal hyphae", "Oxidizing atmospheric nitrogen into high-energy proteins anaerobically"],
                "answer": 1,
                "hint": "Think about the primary role of chlorophyll during photosynthetic carbohydrate formation.",
                "explanation": "Producers utilize chlorophyll to trap sunlight and convert inorganic carbon dioxide and water into organic sugars and starches through photosynthesis."
            }
        ]
    },
    {
        "id": 4,
        "title": "Decomposer Nutrient Recycling",
        "subtitle": "Microbial saprophytic breakdown, soil mineralization, and organic detritus clearance",
        "speech": "Decomposers constitute the indispensable recycling workforce of biosphere energetics. This ecological guild consists predominantly of heterotrophic microorganisms, specifically saprophytic bacteria and fungi, that obtain metabolic energy by digesting non-living organic detritus, including fallen leaves, plant litter, animal excreta, and dead animal carcasses. Decomposers secrete potent extracellular digestive enzymes directly onto organic matter, catalysing the breakdown of complex biopolymers such as cellulose, proteins, and lipids into simpler soluble molecules. During this saprophytic process, vital mineral nutrients such as nitrogen, phosphorus, potassium, sulphur, and magnesium are released in inorganic ionic forms into the surrounding soil and aquatic reservoirs. This process of mineralization replenishes the soil substrate, making essential elements immediately available once again for autotrophic root uptake and incorporation into fresh photosynthetic biomass. If decomposers were eliminated from an ecosystem, biological recycling would cease instantly. Dead organic remains and waste carcasses would pile up across landscapes indefinitely, locking up the global pool of vital elements. Without microbial mineralization, soils would rapidly deplete of essential inorganic nutrients, leading to agricultural failure, producer starvation, and the eventual catastrophic collapse of all dependent heterotrophic consumer trophic tiers. Saprophytes thus preserve perpetual biogeochemical cycles, ensuring continuous ecological replenishment and nutrient availability across nature.",
        "checkpoints": [
            {
                "question": "What fundamental ecological service do saprophytic bacteria and fungi deliver to soils?",
                "options": ["Fixing all solar light energy into high-energy fossil fuels", "Decomposing dead organic matter to replenish inorganic soil nutrients", "Consuming living primary herbivores to limit plant overgrazing", "Absorbing toxic radioactive minerals to sterilize groundwaters"],
                "answer": 1,
                "hint": "Consider how dead plant and animal remains are converted back into simple minerals.",
                "explanation": "Decomposers break down dead organic matter and animal wastes into simple inorganic substances, recycling vital mineral nutrients back into the soil for root absorption."
            },
            {
                "question": "What would occur immediately if all decomposers were suddenly removed from an ecosystem?",
                "options": ["Plants would grow significantly faster due to zero competition", "Dead organic waste would accumulate and soil nutrients would rapidly exhaust", "Herbivore populations would increase exponentially without predators", "Solar radiation incident on leaves would increase tenfold"],
                "answer": 1,
                "hint": "Think about what happens to dead bodies and the recycling of chemical elements.",
                "explanation": "Without decomposers, dead organisms and organic wastes would accumulate endlessly, mineral cycling would stop, soil nutrients would exhaust, and autotrophic synthesis would collapse."
            }
        ]
    },
    {
        "id": 5,
        "title": "Food Chain Hierarchy",
        "subtitle": "Linear feeding sequences, trophic level stratification, and consumer classification",
        "speech": "A food chain is defined as a sequential feeding relationship wherein living organisms consume one another at progressive biotic tiers to transfer chemical matter and metabolic energy. Each distinct nutritional step or operational link in a food chain constitutes a specific trophic level. At the first trophic level stand autotrophic producers, consisting of terrestrial green plants and aquatic algae that trap solar irradiance to manufacture organic biomass. Herbivores that ingest producer foliage directly occupy the second trophic level, functioning as primary consumers, such as grasshoppers, deer, and herbivorous rabbits. At the third trophic level sit small carnivores, termed secondary consumers, which prey directly upon herbivores; typical examples include insectivorous frogs, sparrows, and predatory lizards. At the fourth trophic level we find apex or larger carnivores, designated tertiary consumers, such as hawks, eagles, tigers, and humans, which hunt secondary consumers. Real ecosystems exhibit distinct food chains across habitats: a terrestrial grassland chain follows grass eaten by insect, insect by frog, frog by snake, and snake by eagle; an aquatic chain follows phytoplankton eaten by zooplankton, zooplankton by small fish, and small fish by aquatic birds. Each sequential link demonstrates the vital directional transfer of nutritional energy.",
        "checkpoints": [
            {
                "question": "In the grassland food chain: Grass -> Grasshopper -> Frog -> Snake -> Hawk, which organism occupies the third trophic level?",
                "options": ["Grasshopper", "Frog", "Snake", "Hawk"],
                "answer": 1,
                "hint": "Count the trophic levels starting with autotrophic grass as level 1.",
                "explanation": "Trophic level 1 = Grass (Producer); Trophic level 2 = Grasshopper (Primary consumer); Trophic level 3 = Frog (Secondary consumer); Trophic level 4 = Snake; Trophic level 5 = Hawk."
            },
            {
                "question": "Which trophic level in any stable ecosystem consistently possesses the largest population of individuals?",
                "options": ["Tertiary consumers (apex predators)", "Secondary consumers (small carnivores)", "Primary consumers (herbivores)", "Producers (autotrophic green plants)"],
                "answer": 3,
                "hint": "Consider the base of ecological pyramids required to sustain all higher consumer tiers.",
                "explanation": "The producer trophic level consistently contains the greatest number of individuals and highest biomass, forming the broad energetic base required to support all subsequent consumer tiers."
            }
        ]
    },
    {
        "id": 6,
        "title": "Solar Energy Capture",
        "subtitle": "One percent photosynthetic efficiency, solar irradiance limits, and chemical bond energy",
        "speech": "All terrestrial and aquatic life on Earth is energetically sustained by electromagnetic radiation emitted by our Sun. However, the quantitative efficiency with which biological communities capture incident solar energy is remarkably small. Terrestrial green plants capture on average merely about one percent of the total incident solar energy falling upon their photosynthetic leaves and convert it into chemical bond energy stored in synthesized carbohydrates. The remaining ninety-nine percent of incident solar radiation is reflected into space, absorbed as heat by ambient soil and water bodies, or dissipated during leaf transpiration. For instance, if one million joules of solar radiation strikes the canopy foliage of a forest over a sunny day, the autotrophic producers harness approximately ten thousand joules of usable food energy through photosynthetic photophosphorylation. This initial one percent capture forms the absolute energetic reservoir upon which all subsequent heterotrophic consumer trophic tiers must subsist. The primary producers utilize a portion of this synthesized energy for their own cellular respiration, vegetative growth, and reproductive tissues, while the remaining biochemical biomass becomes available as nutritional forage for primary consumers. Energy capture efficiency thus imposes an insurmountable upper thermodynamic limit on total biosphere biological productivity across all planetary ecosystems.",
        "checkpoints": [
            {
                "question": "What percentage of incident solar radiation striking terrestrial leaves is captured and converted into food energy?",
                "options": ["Approximately 1%", "Exactly 10%", "Roughly 50%", "Nearly 90%"],
                "answer": 0,
                "hint": "Differentiate between the solar capture percentage by plants versus trophic transfer efficiency.",
                "explanation": "Terrestrial green plants capture only about 1% of the total incident sunlight falling on their leaves and convert it into chemical food energy via photosynthesis."
            },
            {
                "question": "If 1,000,000 J of incident solar sunlight reaches a forest canopy, how much energy is converted into plant biomass?",
                "options": ["100,000 J", "10,000 J", "1,000 J", "100 J"],
                "answer": 1,
                "hint": "Calculate 1% of 1,000,000 Joules.",
                "explanation": "Applying the 1% photosynthetic efficiency rule: 1% of 1,000,000 J = 0.01 × 1,000,000 J = 10,000 J of stored chemical energy in plant tissues."
            }
        ]
    },
    {
        "id": 7,
        "title": "Ten Percent Law",
        "subtitle": "Raymond Lindeman trophic transfer efficiency, thermal dissipation, and chain length limits",
        "speech": "The transfer of energy from one trophic level to the subsequent trophic level is governed by the Ten Percent Law, formulated by ecologist Raymond Lindeman in 1942. According to this fundamental thermodynamic principle, on average only ten percent of the organic matter consumed at one trophic level is converted into new body biomass and made energetically available to organisms occupying the next higher trophic level. The remaining ninety percent of ingested energy is expended through metabolic cellular respiration to maintain body functions, utilized in muscular locomotion and reproduction, or dissipated into the environment as degraded low-grade thermal heat and unassimilated fecal waste. Consequently, available metabolic energy diminishes exponentially up the food chain. If autotrophs manufacture ten thousand joules of energy, primary herbivores assimilate only one thousand joules, secondary carnivores assimilate only one hundred joules, and tertiary apex carnivores receive a meager ten joules. Because ninety percent of energy is lost at every step, the energy remaining after three or four trophic transitions becomes insufficient to support another viable reproductive population. This severe thermodynamic attrition explains why food chains in natural ecosystems rarely exceed four to five links. The pyramid of energy therefore narrows dramatically toward top apex consumer levels.",
        "checkpoints": [
            {
                "question": "If primary producers possess 20,000 J of energy, how much energy is available to secondary consumers?",
                "options": ["2,000 J", "200 J", "20 J", "2 J"],
                "answer": 1,
                "hint": "Apply the 10% law twice: from producers to herbivores, then from herbivores to secondary consumers.",
                "explanation": "Producers (20,000 J) -> Primary consumers/herbivores (10% = 2,000 J) -> Secondary consumers/carnivores (10% = 200 J)."
            },
            {
                "question": "Why do natural food chains rarely contain more than four to five trophic levels?",
                "options": ["Higher predators refuse to consume small animal prey", "Available energy becomes too miniscule to support a viable population", "Atmospheric oxygen decreases sharply at higher ecological altitudes", "Decomposers actively kill tertiary predators to recycle nutrients"],
                "answer": 1,
                "hint": "Recall that 90% of energy is dissipated at every single trophic transfer step.",
                "explanation": "Due to the 10% law, 90% of energy is lost as heat and metabolic expenditure at each step. By the fourth or fifth trophic level, the remaining energy is too small to sustain another consumer population."
            }
        ]
    },
    {
        "id": 8,
        "title": "Food Web Networks",
        "subtitle": "Interconnected multi-branching feeding relationships and ecological resilience",
        "speech": "In natural biological communities, feeding relationships are rarely isolated linear chains; instead, organisms establish complex, multi-branching feeding connections known as food webs. A food web represents a network of interconnected food chains operating across an entire community. Individual organisms typically consume multiple distinct prey species and are themselves preyed upon by several distinct predator species. For instance, a terrestrial insect feeds on various flowering plants and agricultural crops, while being hunted by spiders, insectivorous birds, frogs, and lizards. Small rodents feed on seeds and berries while serving as quarry for snakes, foxes, and raptors. This branching architectural complexity imparts critical ecological stability and homeostatic resilience to ecosystems. If a disease or environmental blight suddenly decimates a specific prey population, polyphagous predators do not face immediate extinction because they flexibly switch dietary consumption to alternative abundant prey. Similarly, grazing pressure on depleted plant species eases, granting vegetative communities crucial time to regenerate. Conversely, simple ecosystems with few alternative pathways are fragile and susceptible to trophic cascades when key species decline. A food web thus provides dynamic biological buffering against environmental disturbances. Interconnected webs ensure the collective survival of diverse interacting species despite local environmental fluctuations across surrounding biomes.",
        "checkpoints": [
            {
                "question": "How does a complex food web contribute to overall ecosystem stability?",
                "options": ["By forcing all animals to become strict autotrophs", "By providing alternative dietary pathways when specific prey species decline", "By completely eliminating energy dissipation during trophic transfers", "By preventing decomposers from breaking down dead organic detritus"],
                "answer": 1,
                "hint": "Consider what happens if one food source becomes temporarily scarce in a multi-branched network.",
                "explanation": "In a food web, predators have access to multiple alternative food sources. If one prey species declines, predators shift their feeding habits, stabilizing the ecosystem."
            },
            {
                "question": "What is the structural relationship between food chains and a food web?",
                "options": ["Food webs are isolated, unbranched chains operating in total isolation", "A food web is an interconnected network of multiple overlapping food chains", "Food chains only occur in aquatic biomes while food webs exist only on land", "Food webs represent dead organic matter while food chains represent living biomass"],
                "answer": 1,
                "hint": "A web is formed by interlocking several distinct strands.",
                "explanation": "A food web is an interconnected network formed by numerous intersecting and overlapping food chains within an ecological community."
            }
        ]
    }
]

# Validation
print(f"Loaded {len(slides_part1)} slides for Part 1.")
for s in slides_part1:
    wc = len(s["speech"].split())
    print(f"Slide {s['id']}: '{s['title']}' -> {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} word count {wc} out of range (195-215)"
    assert len(s["title"].split()) <= 3, f"Slide {s['id']} title has more than 3 words: '{s['title']}'"
    assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    # Ensure no persona titles or fictional character names
    slide_str = json.dumps(s)
    for forbidden in ["Raghav", "Dr.", "Dr ", "Sir", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof."]:
        assert forbidden not in slide_str, f"Forbidden term '{forbidden}' in slide {s['id']}"

with open(".agents/c10s_ch13_part1.json", "w", encoding="utf-8") as f:
    json.dump(slides_part1, f, indent=2, ensure_ascii=False)

print("Part 1 (Slides 1 to 8) validated and saved successfully!")

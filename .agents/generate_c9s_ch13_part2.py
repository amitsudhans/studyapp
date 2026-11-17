#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 13 Part 2 Data Generator (Slides 9-16)
Chapter Title: Earth as a System: Energy, Matter, and Life
Strict constraints:
- All slide titles 1-3 words
- Speech word count strictly 195-215 words on Slides 9-16
- Pure Indian male teacher voice
- Zero forbidden character names or persona titles
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Planetary Wind Belts",
        "subtitle": "Global Pressure Belts & The Coriolis Force",
        "speech": (
            "On a planetary scale, unequal solar heating between the blistering equator and freezing poles organizes global "
            "atmospheric circulation into permanent pressure belts and circulating convection cells! Intense heating at the "
            "equator causes warm tropical air to expand and rise vigorously, creating the Equatorial Low Pressure Belt, often "
            "called the doldrums. This rising air flows poleward in the upper troposphere, cools, and sinks around thirty degrees "
            "north and south latitude, forming the Sub-tropical High Pressure Belts. Sinking air at the poles creates Polar Highs, "
            "while cold polar air meeting warmer sub-tropical air creates Sub-polar Lows around sixty degrees latitude. Crucially, "
            "winds do not blow in straight north-south lines! Because Earth continuously rotates eastward on its axis, moving fluids "
            "experience an apparent rotational deflection called the Coriolis force. In the Northern Hemisphere, the Coriolis "
            "force deflects winds toward the right of their motion, transforming equator-ward winds into the Northeast Trade Winds. "
            "In the Southern Hemisphere, winds deflect toward the left, producing the Southeast Trade Winds and roaring Westerlies! "
            "This planetary wind system drives global weather patterns, regulates monsoons, and steers ocean currents across Earth. "
            "Use the simulator to observe how the Coriolis effect curves wind vectors across both hemispheres."
        ),
        "checkpoints": [
            {
                "question": "In which direction does the Coriolis force deflect moving winds in the Northern Hemisphere?",
                "options": [
                    "Directly toward the equator",
                    "To the right of their direction of motion",
                    "To the left of their direction of motion",
                    "Directly upward into the stratosphere"
                ],
                "answer": 1,
                "hint": "Due to eastward planetary rotation, moving air in the north veers rightward.",
                "explanation": "Earth's counter-clockwise rotation (viewed from above the North Pole) creates a Coriolis deflection to the right in the Northern Hemisphere and to the left in the Southern Hemisphere."
            },
            {
                "question": "Which pressure belt forms along the equator due to intense thermal heating and rising air?",
                "options": [
                    "Sub-tropical High Pressure Belt",
                    "Polar High Pressure Belt",
                    "Equatorial Low Pressure Belt",
                    "Sub-polar High Pressure Belt"
                ],
                "answer": 2,
                "hint": "Warm air expands and ascends, creating a persistent trough of low surface pressure.",
                "explanation": "Intense solar heating along the equator causes buoyant air to ascend, producing the Equatorial Low Pressure Belt (Intertropical Convergence Zone)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Ocean Currents Gyres",
        "subtitle": "Thermohaline Conveyors & IITM Modeling",
        "speech": (
            "Planetary winds do not blow harmlessly over water; frictional drag between moving air and ocean surfaces sets the "
            "upper layers of the hydrosphere into vast, flowing oceanic highways called ocean currents! Combined with water density "
            "variations caused by temperature and salinity gradients—termed deep thermohaline circulation—and constrained by continental boundaries, "
            "winds organize surface waters into colossal circulating loops known as oceanic gyres. Because of the Coriolis deflection, "
            "oceanic gyres rotate clockwise in the Northern Hemisphere and counter-clockwise in the Southern Hemisphere. Ocean currents "
            "act as colossal planetary heat conveyors, moderating regional climates and sustaining marine ecosystems across Earth. A prime example is the warm Gulf "
            "Stream and North Atlantic Drift, which transport immense thermal energy from equatorial waters northeastward to northwestern "
            "Europe, keeping high-latitude Norwegian coastal harbors ice-free even in mid-winter! In India, understanding ocean-atmosphere coupling "
            "is essential for national food security and agrarian livelihoods. Modern supercomputers at the Indian Institute of Tropical Meteorology, or "
            "IITM in Pune, simulate coupled ocean-atmosphere models, analyzing Arabian Sea warming and Bay of Bengal storm dynamics to "
            "forecast the vital Indian summer monsoon with high precision! Manipulate the interactive simulator to trace global oceanic gyres and evaluate thermal "
            "heat distribution across Earth's continents."
        ),
        "checkpoints": [
            {
                "question": "How do major surface ocean gyres rotate in the Northern Hemisphere?",
                "options": ["Counter-clockwise", "Clockwise", "In straight east-west lines", "Purely randomly"],
                "answer": 1,
                "hint": "Coriolis deflection to the right causes circular water loops to turn in a clockwise direction.",
                "explanation": "Surface winds and the rightward Coriolis deflection in the Northern Hemisphere cause ocean gyres (like the North Atlantic Gyre) to circulate clockwise."
            },
            {
                "question": "Which Indian research institute utilizes supercomputers to model coupled ocean-atmosphere monsoon dynamics?",
                "options": [
                    "Bhabha Atomic Research Centre (BARC), Mumbai",
                    "Indian Institute of Tropical Meteorology (IITM), Pune",
                    "Birbal Sahni Institute of Palaeosciences, Lucknow",
                    "National Metallurgical Laboratory, Jamshedpur"
                ],
                "answer": 1,
                "hint": "Located in Maharashtra, this premier institute leads climate modeling for the Indian monsoon.",
                "explanation": "IITM Pune operates high-performance supercomputing clusters running coupled climate models that forecast seasonal Indian monsoon precipitation."
            }
        ]
    },
    {
        "id": 11,
        "title": "The Water Cycle",
        "subtitle": "Hydrological Fluxes & Cryosphere Vulnerability",
        "speech": (
            "Life on Earth requires continuous recycling of vital chemical substances across our five spheres, orchestrated through "
            "biogeochemical cycles. Among these, the water cycle, or hydrological cycle, is the global circulation of moisture driven "
            "by solar energy and gravity. Water evaporates from oceans, lakes, and soil, while plants release substantial moisture "
            "into the atmosphere through foliar transpiration. As warm, humid air ascends into the colder troposphere, water vapor "
            "undergoes condensation around microscopic aerosols to form clouds, eventually returning to the surface as rain, snow, "
            "or hail through precipitation. On land, precipitated water divides: a fraction infiltrates deep underground to recharge "
            "freshwater aquifers, while the remainder flows across the geosphere as surface runoff, replenishing rivers and oceans. "
            "Today, human-induced global warming is dangerously accelerating this hydrological machinery! Warmer air holds more moisture, "
            "intensifying extreme rainfall downpours while worsening prolonged droughts. Concurrently, rising temperatures are melting "
            "Himalayan glaciers at alarming rates. Rapid glacier melt initially causes catastrophic flash floods and landslides, followed "
            "by long-term river drying that threatens agriculture across north India, while accelerating global sea level rise that "
            "directly endangers coastal mega-cities like Mumbai and Chennai! Use the simulator to adjust planetary temperatures and "
            "observe hydrological disruptions."
        ),
        "checkpoints": [
            {
                "question": "Which hydrological process describes the release of water vapor into the air from plant foliage?",
                "options": ["Sublimation", "Transpiration", "Precipitation", "Infiltration"],
                "answer": 1,
                "hint": "Plants pull groundwater through roots and release vapor through microscopic leaf stomata.",
                "explanation": "Transpiration is the biological evaporation of water from plant leaves through stomata, contributing significantly to atmospheric humidity."
            },
            {
                "question": "How does accelerated Himalayan glacier melting impact downstream Indian river basins over time?",
                "options": [
                    "It permanently stabilizes river flow at uniform levels year-round",
                    "It causes initial flooding followed by severe dry-season freshwater shortages",
                    "It transforms all freshwater rivers into hypersaline oceanic lagoons",
                    "It stops all rainfall across the Indo-Gangetic plains"
                ],
                "answer": 1,
                "hint": "Glacier loss creates an initial burst of water, followed by the exhaustion of perennial river sources.",
                "explanation": "Rapid glacial retreat triggers catastrophic early floods, but as ice reserves dwindle, perennial river flows decline severely during dry seasons."
            }
        ]
    },
    {
        "id": 12,
        "title": "The Carbon Cycle",
        "subtitle": "Fast Biological Fluxes & Slow Geological Storage",
        "speech": (
            "Carbon is the foundational structural backbone of all organic molecules, from DNA and proteins to carbohydrates and fats. "
            "The global carbon cycle operates across two vastly different timescales: the fast biological cycle and the slow geological "
            "cycle. In the fast biological cycle, land plants, algae, and cyanobacteria absorb atmospheric carbon dioxide through "
            "photosynthesis, converting solar energy and carbon into glucose. This carbon moves through food chains and returns to the "
            "atmosphere within days or decades via cellular respiration and microbial decomposition. In stark contrast, the slow "
            "geological cycle spans millions of years! Millions of years ago, dead organic matter buried under high heat and pressure "
            "in sedimentary rock formations transformed into fossil fuels: coal, petroleum, and natural gas. In the oceans, marine organisms "
            "use dissolved bicarbonate ions to build calcium carbonate shells, which settle upon death to form limestone rock. Remarkably, "
            "Earth's oceans store seventy-one percent of global carbon, whereas the atmosphere holds only one percent! However, burning "
            "fossil fuels is rapidly unearthing ancient carbon. Charles Keeling's iconic curve shows atmospheric carbon dioxide rising "
            "from three hundred and fifteen parts per million in 1960 to over four hundred and twenty parts per million today! "
            "Use the simulator to balance carbon reservoirs across Earth's spheres."
        ),
        "checkpoints": [
            {
                "question": "What proportion of Earth's total mobile carbon is stored in the oceanic carbon sink?",
                "options": ["1 percent", "25 percent", "50 percent", "71 percent"],
                "answer": 3,
                "hint": "The oceans hold the overwhelming majority of global carbon as dissolved carbonate ions.",
                "explanation": "Oceans hold approximately 71% of global carbon, serving as the largest active carbon sink compared to only ~1% in the atmosphere."
            },
            {
                "question": "What is demonstrated by the famous scientific Keeling Curve?",
                "options": [
                    "A rapid drop in ocean salinity over two centuries",
                    "A steady, dramatic rise in atmospheric carbon dioxide from 1960 to the present",
                    "Fluctuations in solar constant energy outputs across eleven-year cycles",
                    "The declining rate of photosynthesis in tropical rainforests"
                ],
                "answer": 1,
                "hint": "Started by Charles Keeling at Mauna Loa, it charts carbon dioxide climbing from 315 to >420 ppm.",
                "explanation": "The Keeling Curve records the relentless post-industrial increase in atmospheric CO₂ concentration from 315 ppm in 1960 to over 420 ppm today."
            }
        ]
    },
    {
        "id": 13,
        "title": "The Nitrogen Cycle",
        "subtitle": "Biological Fixation & Bacterial Transformations",
        "speech": (
            "Although nitrogen gas constitutes seventy-eight percent of our atmosphere, neither humans, animals, nor plants can "
            "absorb it directly! The two nitrogen atoms in molecular nitrogen are locked together by a formidable chemical triple bond "
            "that renders the molecule completely unreactive under ordinary conditions. Life depends on specialized soil and root bacteria "
            "to convert atmospheric nitrogen into usable biological forms through the interconnected stages of the nitrogen cycle. First, biological nitrogen fixation "
            "is carried out by symbiotic bacteria like Rhizobium living inside the root nodules of leguminous plants, alongside free-living "
            "soil microbes like Azotobacter, which chemically reduce nitrogen gas into ammonia. Atmospheric lightning discharges also fix small amounts. Next, during "
            "nitrification, chemoautotrophic soil bacteria transform ammonia into plant-accessible forms: Nitrosomonas oxidizes ammonia "
            "into nitrite ions, after which Nitrobacter oxidizes nitrite into nitrate ions. Plants assimilate these dissolved nitrates through their "
            "roots to synthesize essential proteins and nucleic acids. When plants and animals produce organic waste or die, decomposers perform "
            "ammonification, releasing ammonia back into the soil matrix. Finally, anaerobic denitrifying bacteria such as Pseudomonas convert "
            "soil nitrates back into inert atmospheric nitrogen gas, completing this vital planetary biogeochemical cycle! Experiment with the simulator to inspect "
            "each step of bacterial nitrogen transformation."
        ),
        "checkpoints": [
            {
                "question": "Which specific bacterium oxidizes nitrite ions into nitrate ions during soil nitrification?",
                "options": ["Rhizobium", "Nitrosomonas", "Nitrobacter", "Pseudomonas"],
                "answer": 2,
                "hint": "Nitrosomonas converts ammonia to nitrite, and this related bacterium finishes the conversion to nitrate.",
                "explanation": "Nitrification is a two-step bacterial process: Nitrosomonas converts ammonia (NH₃) to nitrite (NO₂⁻), and Nitrobacter oxidizes nitrite to nitrate (NO₃⁻)."
            },
            {
                "question": "What critical role does Pseudomonas play in the nitrogen cycle?",
                "options": [
                    "Fixing nitrogen directly into legume root nodules",
                    "Synthesizing plant proteins from atmospheric ammonia",
                    "Converting soil nitrates back into atmospheric nitrogen gas (denitrification)",
                    "Decomposing dead animal tissue into urea"
                ],
                "answer": 2,
                "hint": "It operates anaerobically to return nitrogen gas to the atmosphere, closing the cycle.",
                "explanation": "Pseudomonas is a denitrifying bacterium that converts nitrates (NO₃⁻) back into inert atmospheric nitrogen gas (N₂), preventing nitrate over-accumulation."
            }
        ]
    },
    {
        "id": 14,
        "title": "Haber-Bosch & Fertilizers",
        "subtitle": "Industrial Fixation & The Green Revolution",
        "speech": (
            "For billions of years, biological nitrogen fixation by soil bacteria set a strict natural limit on how much food Earth's "
            "ecosystems could produce. In the early twentieth century, German chemists Fritz Haber and Carl Bosch revolutionized "
            "human civilization by inventing an industrial chemical process to fix atmospheric nitrogen directly. The Haber-Bosch process "
            "synthesizes ammonia by combining atmospheric nitrogen gas and hydrogen gas under extreme engineering conditions: temperatures of "
            "four hundred and fifty degrees Celsius, pressures exceeding two hundred atmospheres, and an active iron catalyst! This breakthrough "
            "allowed the large-scale industrial manufacture of synthetic nitrogen fertilizers like urea. In India, synthetic chemical fertilizers "
            "became the scientific engine of the historic Green Revolution during the nineteen-sixties and seventies, multiplying crop "
            "yields across Punjab, Haryana, and Uttar Pradesh, and rescuing our growing nation from catastrophic famines! Today, over "
            "half of all nitrogen atoms in human body tissues originate from Haber-Bosch industrial synthesis. However, this miraculous agricultural "
            "power carries profound ecological costs. The Haber-Bosch process consumes nearly two percent of global fossil fuel energy "
            "and generates heavy carbon dioxide emissions, while excess fertilizer runoff severely pollutes groundwater aquifers and surface "
            "aquatic ecosystems! Explore the interactive simulator to balance crop yields against industrial energy consumption."
        ),
        "checkpoints": [
            {
                "question": "What reaction conditions are required for the industrial Haber-Bosch synthesis of ammonia?",
                "options": [
                    "Sub-zero temperatures and room atmospheric pressure",
                    "High temperature (~450 °C), high pressure (~200 atm), and an iron catalyst",
                    "Pure liquid nitrogen immersed in sulfuric acid at room temperature",
                    "Photochemical reaction under strong ultraviolet lamps without heat"
                ],
                "answer": 1,
                "hint": "Breaking the tough N≡N triple bond requires high heat, extreme pressure, and a metal catalyst.",
                "explanation": "The Haber-Bosch process combines N₂ and H₂ at ~450 °C and ~200 atm over an iron catalyst to overcome the high activation energy of the triple bond."
            },
            {
                "question": "What major agricultural transformation in India was enabled by synthetic nitrogen fertilizers?",
                "options": [
                    "The White Revolution in dairy cooperative societies",
                    "The Blue Revolution in brackish water shrimp aquaculture",
                    "The Green Revolution multiplying wheat and rice yields",
                    "The Golden Revolution in commercial honey harvesting"
                ],
                "answer": 2,
                "hint": "Initiated in the 1960s, it dramatically boosted grain output in northern agricultural states.",
                "explanation": "Synthetic nitrogen fertilizers, paired with high-yielding seed varieties and irrigation, formed the core of India's Green Revolution."
            }
        ]
    },
    {
        "id": 15,
        "title": "The Oxygen Cycle",
        "subtitle": "Atmospheric Reserves & The Marine Phytoplankton Engine",
        "speech": (
            "Oxygen is essential for aerobic respiration, releasing stored biochemical energy within cells across the animal and "
            "plant kingdoms. Planet Earth's atmosphere maintains a remarkably stable oxygen concentration of approximately twenty-one "
            "percent, governed by the dynamic oxygen cycle. Atmospheric oxygen is constantly consumed by three major planetary sinks: "
            "cellular respiration by living organisms, decay and decomposition of organic waste by aerobic microbes, and industrial "
            "combustion of biomass and fossil fuels. Furthermore, chemical weathering of exposed rocks oxidizes iron and sulfur minerals, "
            "locking oxygen into the geosphere. How is this colossal oxygen consumption replenished? Exclusively through oxygenic "
            "photosynthesis! Plants on land harness sunlight to split water molecules, releasing oxygen gas into the atmosphere. "
            "However, many students are surprised to learn that terrestrial forests do not produce the majority of Earth's oxygen. "
            "Over fifty percent of our planetary oxygen is generated by microscopic marine organisms in the hydrosphere: oceanic "
            "phytoplankton, cyanobacteria, and floating seaweeds! These tiny photosynthetic engines form the very base of marine food "
            "webs, quietly generating every second breath we take on Earth. Protecting ocean health is therefore directly vital to our "
            "survival! Test the simulator to observe how deforestation and marine warming alter global oxygen reserves."
        ),
        "checkpoints": [
            {
                "question": "Which of the following planetary processes consumes atmospheric oxygen?",
                "options": [
                    "Plant photosynthesis in chloroplasts",
                    "Aerobic respiration, microbial decay, and combustion",
                    "Precipitation of rain and snowfall",
                    "Denitrification by soil bacteria"
                ],
                "answer": 1,
                "hint": "Think of processes that burn fuel, break down food for cellular energy, or rot dead matter.",
                "explanation": "Oxygen is consumed by aerobic respiration in living cells, decomposition of organic matter by microbes, and combustion of organic materials."
            },
            {
                "question": "Where does more than fifty percent of Earth's photosynthetic oxygen production originate?",
                "options": [
                    "Amazon and tropical African rainforests",
                    "Microscopic marine phytoplankton and algae in the oceans",
                    "Himalayan coniferous pine and deodar forests",
                    "Agricultural wheat and paddy crops across Asia"
                ],
                "answer": 1,
                "hint": "Microscopic drifting algae across the vast ocean surface produce the majority of global oxygen.",
                "explanation": "Marine phytoplankton, microalgae, and cyanobacteria in the world's oceans produce over 50% of the planetary oxygen supply."
            }
        ]
    },
    {
        "id": 16,
        "title": "Human Planetary Impacts",
        "subtitle": "Ocean Acidification, Eutrophication & Mission LiFE",
        "speech": (
            "Human activities have expanded so extensively that our species now acts as a dominant geological force disrupting Earth's "
            "natural spheres! When oceans absorb billions of tons of excess atmospheric carbon dioxide from smokestacks and vehicles, "
            "the gas reacts chemically with water to form carbonic acid. This process, called ocean acidification, lowers seawater pH, depleting "
            "carbonate ions and causing protective calcium carbonate shells of marine plankton and coral reefs to dissolve! In agriculture, runoff of "
            "synthetic nitrogen and phosphorus fertilizers washes into freshwater lakes, ponds, and rivers. This surplus of dissolved nutrients triggers "
            "eutrophication: explosive algal blooms cover the water surface, block sunlight from reaching underwater plants, and die. Decaying algae fuel dense bacterial "
            "populations that rapidly consume dissolved oxygen, creating suffocating hypoxic dead zones that trigger mass fish mortality! "
            "Widespread deforestation strips land cover, reducing plant transpiration, destabilizing regional rainfall patterns, and causing severe topsoil erosion. "
            "To counter these escalating crises, India launched Mission LiFE, or Lifestyle for Environment, at COP26, advocating "
            "mindful individual habits rooted in traditional ecological stewardship. Coupled with global accords like the Paris Agreement, "
            "humanity must urgently align technological progress with planetary ecological boundaries! Use the final interactive simulator to model "
            "sustainable community interventions and track ecological restoration across all five spheres."
        ),
        "checkpoints": [
            {
                "question": "What is the primary ecological mechanism behind aquatic eutrophication?",
                "options": [
                    "Glacier melt introducing extreme cold water that freezes fish gills",
                    "Agricultural fertilizer runoff causing algal blooms and subsequent bacterial oxygen depletion",
                    "Heavy oil spills preventing wind from creating surface waves",
                    "Acid rain neutralizing basic minerals in lake sediments"
                ],
                "answer": 1,
                "hint": "Excess nitrogen and phosphorus feed rapid algal growth; decaying algae trigger bacterial oxygen starvation.",
                "explanation": "Excess nutrient runoff sparks dense algal blooms; when these algae die, decomposers exhaust dissolved oxygen, creating lethal hypoxic conditions for aquatic life."
            },
            {
                "question": "What global environmental initiative did India launch at COP26 to promote sustainable individual behaviors?",
                "options": ["Mission Shakti", "Mission LiFE (Lifestyle for Environment)", "Project Tiger", "Namami Gange"],
                "answer": 1,
                "hint": "This initiative emphasizes conscious consumption and eco-friendly daily practices.",
                "explanation": "Mission LiFE (Lifestyle for Environment) was launched by India at COP26 to mobilize individuals globally toward sustainable living practices."
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides_part2:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: title='{s['title']}' ({tw} words), speech={wc} words")
        assert 1 <= tw <= 3, f"Title length {tw} not 1-3 words"
        assert 195 <= wc <= 215, f"Speech length {wc} not 195-215 words"
        assert len(s["checkpoints"]) == 2, "Must have 2 checkpoints"
    print("Part 2 verified successfully!")

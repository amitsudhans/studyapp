# -*- coding: utf-8 -*-
"""
Generate Part 2 (Slides 9 to 16) for Class 10 Science Chapter 13: Our Environment
"""

import json

slides_part2 = [
    {
        "id": 9,
        "title": "Unidirectional Energy Flow",
        "subtitle": "Irreversible thermodynamic dissipation, solar dependency, and open energy systems",
        "speech": "A defining thermodynamic law of planetary ecology is the strictly unidirectional flow of energy through ecosystems. Solar energy captured by autotrophic producers does not revert back to the Sun, nor can metabolic energy acquired by herbivores revert backward to primary producers. As radiant solar energy is captured by photosynthetic chloroplasts, it is transformed into chemical bond energy. When primary consumers ingest plant matter, that chemical energy is transferred upward. At every single trophic step, approximately ninety percent of available energy is irreversibly converted into metabolic work and dissipated into the surrounding atmosphere as low-grade thermal heat according to the second law of thermodynamics. Heat energy dissipated into the environment cannot be re-concentrated or reused by photosynthetic organisms to power carbon fixation. Consequently, the flow of energy across an ecosystem is strictly a one-way street, requiring a continuous, uninterrupted influx of fresh solar radiation from our Sun to sustain life on Earth. In sharp contrast, chemical nutrients and mineral elements follow cyclic biogeochemical trajectories, circulating repeatedly between living organisms, soil substrates, and atmospheric reservoirs. Energy flows through ecosystems and dissipates, whereas chemical nutrients cycle endlessly within the biosphere, maintaining the biochemical continuity of global biomes across geological millennia.",
        "checkpoints": [
            {
                "question": "Why is the flow of energy through an ecosystem described as strictly unidirectional?",
                "options": ["Energy captured by organisms cannot flow backwards to previous trophic levels or the Sun", "Producers absorb thermal energy directly from carnivores to make glucose", "Heat energy dissipated into the atmosphere is captured by plants for photosynthesis", "Energy increases progressively at each higher trophic tier"],
                "answer": 0,
                "hint": "Energy moves in only one direction from the Sun through trophic tiers and dissipates as heat.",
                "explanation": "Energy flows unidirectionally from the Sun to autotrophs and through successive consumer tiers. Dissipated heat cannot be gathered back by plants, making the flow strictly one-way."
            },
            {
                "question": "What fundamental difference distinguishes energy flow from mineral nutrient dynamics in ecosystems?",
                "options": ["Nutrients flow unidirectionally while energy cycles indefinitely", "Energy flows unidirectionally and dissipates while nutrients cycle repeatedly", "Both energy and nutrients cycle infinitely without external solar inputs", "Neither energy nor nutrients can ever be transferred to decomposers"],
                "answer": 1,
                "hint": "Think about whether sunlight must constantly enter, while mineral atoms are recycled by decomposers.",
                "explanation": "Energy flows unidirectionally through the ecosystem and is lost as heat, requiring continuous solar input. Mineral nutrients, by contrast, cycle continuously via decomposers."
            }
        ]
    },
    {
        "id": 10,
        "title": "Biological Toxic Magnification",
        "subtitle": "Non-biodegradable pesticide accumulation, trophic escalation, and apex consumer risk",
        "speech": "Biological magnification, or biomagnification, represents the progressive accumulation and increasing chemical concentration of non-biodegradable toxic substances at successively higher trophic levels of a food chain. When synthetic pesticides, industrial chemical effluents, synthetic organochlorines like DDT, and toxic heavy metals such as mercury or lead enter soil and aquatic ecosystems through agricultural runoff or industrial discharge, they cannot be decomposed by natural bacterial saprophytes. Autotrophic plants absorb these persistent synthetic chemicals along with soil water and essential minerals, while aquatic algae absorb them from contaminated water bodies. Because these synthetic toxins are chemically stable, fat-soluble, and cannot be metabolized, excreted, or digested by animal tissues, they accumulate permanently in the adipose body mass of organisms. When herbivores consume hundreds of contaminated plants, they assimilate the aggregate pesticide load into their own bodies. When carnivores subsequently consume numerous herbivores, the chemical concentration escalates by multiple orders of magnitude. Because human beings occupy the pinnacle trophic level across diverse terrestrial and aquatic food chains, the highest concentration of hazardous non-biodegradable chemicals inevitably accumulates in human tissues, provoking chronic organ toxicity, endocrine disruption, immunological suppression, and long-term carcinogenic risks across populations globally. This alarming ecological phenomenon highlights why toxic synthetic chemicals cause the greatest biological destruction to top-level apex consumers.",
        "checkpoints": [
            {
                "question": "Which trophic level accumulates the maximum concentration of non-biodegradable pesticides due to biological magnification?",
                "options": ["Primary autotrophs (green plants)", "Primary consumers (herbivores)", "Decomposers (soil bacteria)", "Top trophic level (apex consumers like humans)"],
                "answer": 3,
                "hint": "Toxins amplify progressively at each consecutive step up the food chain.",
                "explanation": "Because non-biodegradable chemicals cannot be excreted or broken down, their concentration multiplies at each successive trophic level, reaching peak concentrations in top apex consumers."
            },
            {
                "question": "What chemical characteristic makes synthetic pesticides like DDT prone to biomagnification?",
                "options": ["Rapid enzymatic breakdown by soil bacteria", "Non-biodegradable nature and accumulation in fatty tissues", "Instant sublimation into inert atmospheric gases", "High water solubility leading to complete urinary clearance"],
                "answer": 1,
                "hint": "Microorganisms cannot digest these persistent, fat-soluble compounds.",
                "explanation": "Synthetic pesticides are non-biodegradable and fat-soluble. Because organisms cannot metabolize or excrete them, they persist and concentrate within adipose body tissues."
            }
        ]
    },
    {
        "id": 11,
        "title": "Pesticide Biomagnification Impact",
        "subtitle": "Activity 13.3 aquatic food chains, bioamplification factors, and systemic residues",
        "speech": "In Activity 13.3, we explore the profound ecological and human health consequences of pesticide contamination in our everyday food supply. Modern agricultural practices rely extensively on chemical fertilizers, synthetic insecticides, and weedicides to maximize crop yields and suppress agricultural pests. However, rainwash and irrigation runoff transport surplus chemical residues into nearby water streams, rivers, and groundwater aquifers, initiating widespread aquatic biomagnification. In a classic freshwater food chain, water containing a minute, seemingly negligible pesticide concentration of 0.02 parts per billion leads to plankton accumulating 0.04 parts per million. Small fish feeding on plankton concentrate the toxin to 0.5 parts per million, and large predatory fish reach 2.0 parts per million. Fish-eating predatory birds and apex human consumers ultimately accumulate toxic concentrations exceeding 25 to 50 parts per million—a million-fold bioamplification from surrounding water. Thoroughly washing fruits, vegetables, and cereal grains with tap water can remove superficial surface sprays, but cannot dislodge systemic pesticides that have been absorbed internally into plant vascular tissues. Mitigating biomagnification demands transitioning to organic farming, implementing integrated biological pest management, and enacting strict statutory thresholds on pesticide residues in commercial food products across domestic markets, safeguarding human consumer health and preserving delicate regional aquatic ecosystems.",
        "checkpoints": [
            {
                "question": "Why does thoroughly washing commercial vegetables with plain water fail to remove all pesticide residues?",
                "options": ["Water causes pesticides to multiply chemically on fruit surfaces", "Systemic pesticides are absorbed into internal plant tissues through roots and vascular vessels", "Pesticides transform immediately into harmless mineral salts upon wetting", "Washing only attracts more airborne synthetic pollutants to the skin"],
                "answer": 1,
                "hint": "Consider pesticides taken up from the soil into the sap and plant pulp.",
                "explanation": "While surface washes remove topical dust and spray coatings, systemic pesticides absorbed through roots into plant vascular tissues remain embedded inside the cellular edible pulp."
            },
            {
                "question": "If water has 0.02 ppb pesticide and fish-eating birds accumulate 25 ppm, this concentration surge exemplifies:",
                "options": ["Ecosystem eutrophication", "Biological magnification", "Thermal dissipation", "Saprophytic decomposition"],
                "answer": 1,
                "hint": "Identify the progressive chemical amplification up trophic levels.",
                "explanation": "The million-fold concentration surge of persistent, non-biodegradable chemicals from ambient water to top predators is the textbook definition of biological magnification."
            }
        ]
    },
    {
        "id": 12,
        "title": "Stratospheric Ozone Formation",
        "subtitle": "Triatomic molecule synthesis, high-energy UV photolysis, and protective planetary shielding",
        "speech": "The stratospheric ozone layer functions as a vital protective umbrella shielding Earth's biosphere from harmful extraterrestrial solar radiation. Chemically, ozone is a triatomic molecule composed of three oxygen atoms, with the formula O3. While elemental ozone at ground tropospheric levels is an irritating and deadly respiratory poison, its presence in the upper stratosphere between fifteen and thirty kilometres above Earth's surface is absolutely indispensable for terrestrial life. Stratospheric ozone absorbs intense, high-energy solar ultraviolet radiation, particularly UV-C and UV-B rays, which have sufficient quantum energy to break chemical bonds in genetic DNA, triggering skin cancers, cataract blindness, and lethal mutations in living cells. Ozone is synthesized continuously in the stratosphere through a two-step photochemical reaction initiated by high-energy solar ultraviolet radiation. In the first step, energetic ultraviolet photons split diatomic oxygen molecules into two highly reactive, unbonded nascent oxygen atoms: O2 plus UV yields O plus O. In the second step, each free nascent oxygen atom instantly collides with an intact diatomic oxygen molecule to synthesize a stable triatomic ozone molecule: O plus O2 yields O3. This photolytic equilibrium sustains stratospheric ozone concentrations, maintaining an essential planetary shield for all living biomes across continental landmasses and expansive global oceans.",
        "checkpoints": [
            {
                "question": "What is the correct chemical formula and structural composition of an ozone molecule?",
                "options": ["O2 consisting of two oxygen atoms", "O3 consisting of three oxygen atoms", "O4 consisting of four oxygen atoms", "H2O consisting of hydrogen and oxygen"],
                "answer": 1,
                "hint": "Ozone is a triatomic allotrope of oxygen.",
                "explanation": "Ozone has the chemical formula O3, comprising three covalently bonded oxygen atoms."
            },
            {
                "question": "What is the two-step photochemical sequence that synthesizes stratospheric ozone?",
                "options": ["O2 + UV -> O + O, followed by O + O2 -> O3", "O3 + UV -> O2 + O, followed by O + O -> O2", "CO2 + UV -> C + O2, followed by C + O2 -> CO3", "H2O + UV -> H2 + O, followed by O + H2 -> H2O2"],
                "answer": 0,
                "hint": "UV radiation first splits molecular oxygen into nascent oxygen atoms, which combine with molecular oxygen.",
                "explanation": "UV photons photolyse diatomic oxygen: O2 -> O + O. Each nascent oxygen atom then combines with another O2 molecule to produce ozone: O + O2 -> O3."
            }
        ]
    },
    {
        "id": 13,
        "title": "Ozone Layer Depletion",
        "subtitle": "CFC synthetic refrigerants, chlorine catalytic breakdown, and 1987 Montreal Protocol",
        "speech": "During the 1980s, atmospheric scientists discovered an alarming, precipitous decline in stratospheric ozone concentrations, particularly manifesting as an expansive ozone hole over Antarctica. Extensive atmospheric investigations identified the primary culprits as synthetic industrial chemicals called chlorofluorocarbons, or CFCs, which had been widely manufactured as inert coolants in refrigerators, air conditioners, fire extinguishers, and aerosol propellants. Due to their extreme chemical stability at ground level, CFCs diffuse upward into the upper stratosphere intact without breaking down. Upon reaching the stratosphere, intense ultraviolet photons break the chemical bonds of CFC molecules, liberating highly reactive, unbonded chlorine free radicals. A single chlorine radical initiates a destructive catalytic cycle: the chlorine atom attacks an ozone molecule to form chlorine monoxide and diatomic oxygen, then reacts with another oxygen atom to regenerate the free chlorine radical. Consequently, a single chlorine atom can catalytically destroy over one hundred thousand ozone molecules. Recognizing this catastrophic planetary threat, the United Nations Environment Programme forged a historic international treaty in 1987 known as the Montreal Protocol, freezing CFC production at 1986 levels and mandating a worldwide transition to ozone-safe non-chlorinated refrigerants, fostering remarkable stratospheric recovery over subsequent decades. This historic global agreement demonstrates the power of international scientific cooperation in reversing planetary environmental damage.",
        "checkpoints": [
            {
                "question": "Which class of synthetic chemicals was primarily responsible for the rapid depletion of stratospheric ozone?",
                "options": ["Chlorofluorocarbons (CFCs)", "Carbon dioxide (CO2)", "Methane gas (CH4)", "Nitrogen dioxide (NO2)"],
                "answer": 0,
                "hint": "Commonly used as coolants in refrigerators and aerosol propellants before the 1990s.",
                "explanation": "Chlorofluorocarbons (CFCs) release reactive chlorine radicals under high-altitude UV radiation, which catalytically break down stratospheric ozone molecules."
            },
            {
                "question": "What milestone international treaty was signed in 1987 under UNEP to protect the ozone layer?",
                "options": ["Kyoto Protocol", "Montreal Protocol", "Paris Climate Accord", "Geneva Convention"],
                "answer": 1,
                "hint": "Named after the Canadian city where the agreement to freeze and phase out CFC production was adopted.",
                "explanation": "The 1987 Montreal Protocol, forged under the United Nations Environment Programme (UNEP), successfully froze and phased out the global manufacture of ozone-depleting CFCs."
            }
        ]
    },
    {
        "id": 14,
        "title": "Enzyme Biodegradation Specificity",
        "subtitle": "Activities 13.5 & 13.6 substrate lock-and-key action and plastic persistence",
        "speech": "In Activity 13.5 and 13.6, we examine the biochemical mechanisms governing material biodegradability through the principle of enzyme specificity. Why do biological microorganisms decompose organic kitchen scraps, plant leaves, and natural cotton, but fail completely to break down human-made plastics and synthetic polymers? The answer lies in the fundamental biochemistry of enzyme action. Living decomposers, including bacteria and fungi, secrete specific digestive enzymes that operate on a strict lock-and-key substrate specificity model. Enzymes possess intricately folded three-dimensional active sites that bind exclusively to specific chemical bonds found in naturally evolved organic polymers, such as the glycosidic linkages in cellulose, peptide bonds in proteins, and ester bonds in natural lipids. In stark contrast, synthetic plastics like polyethylene, polypropylene, and polyvinyl chloride consist of long, synthetic carbon-carbon backbones that do not occur in nature. Because saprophytic microorganisms never encountered these synthetic configurations throughout evolutionary history, they possess no digestive enzymes capable of cleaving these bonds. Consequently, plastics are biologically inert and classified as non-biodegradable, persisting in soils, water bodies, and landfills for hundreds of years, causing severe physical blockages, toxic leachates, and enduring ecological devastation across terrestrial ecosystems and marine food webs worldwide. Enzymatic specificity fundamentally differentiates organic natural waste from persistent synthetic contaminants.",
        "checkpoints": [
            {
                "question": "Why are bacterial decomposers unable to break down synthetic plastic polymers in soil?",
                "options": ["Plastics contain radioactive elements that kill bacteria instantly", "Bacteria lack specific enzymes capable of cleaving synthetic unnatural polymer bonds", "Bacteria only survive in freezing aquatic environments", "Plastics absorb all oxygen from bacterial cell membranes"],
                "answer": 1,
                "hint": "Enzymes operate like keys that fit only specific evolved biochemical locks.",
                "explanation": "Enzymes exhibit strict substrate specificity. Decomposers produce enzymes that only fit naturally evolved biopolymer bonds (like cellulose or protein), lacking enzymes to break synthetic plastic bonds."
            },
            {
                "question": "Which of the following items is classified as completely biodegradable in soil burial tests?",
                "options": ["Polyethylene carry bag", "Aluminium foil wrapper", "Discarded vegetable peels and scrap paper", "Synthetic nylon fishing line"],
                "answer": 2,
                "hint": "Identify materials derived directly from living plant matter.",
                "explanation": "Vegetable peels and paper are natural organic materials composed of cellulose and plant tissues, which microbial saprophytes rapidly break down into soil humus."
            }
        ]
    },
    {
        "id": 15,
        "title": "Solid Waste Management",
        "subtitle": "Source segregation, composting, vermiculture, and Five R environmental conservation",
        "speech": "Modern industrial expansion and urban lifestyle changes have generated unprecedented quantities of municipal solid waste, requiring urgent, scientific waste management strategies. As investigated in Activities 13.7 and 13.8, sustainable solid waste handling requires source segregation, dividing refuse into biodegradable and non-biodegradable categories using color-coded collection bins. Biodegradable waste, such as kitchen vegetable peels, discarded food scraps, livestock dung, and garden clippings, should be placed in green bins and directed to aerobic composting or anaerobic biogas digestion plants. Microbial decomposition converts this organic matter into nutrient-dense vermicompost and combustible methane fuel. Non-biodegradable waste, comprising plastics, glass bottles, aluminium cans, and electronic scraps, belongs in blue bins for mechanical sorting and industrial recycling. If mixed indiscriminately, decomposing organic matter rots anaerobically under plastic layers, generating foul methane gas and highly toxic liquid leachate that percolates into underground aquifers, poisoning municipal drinking water. Furthermore, careless plastic dumping chokes urban drainage sewers, leading to urban flash floods during monsoons, while stray cattle ingest plastic bags causing fatal alimentary obstruction. Adopting the five R's framework—Refuse, Reduce, Reuse, Repurpose, and Recycle—constitutes our foremost civic duty for environmental preservation, safeguarding public hygiene and fragile urban habitats across modern developing and developed communities.",
        "checkpoints": [
            {
                "question": "What is the primary scientific purpose of segregating municipal waste into green and blue bins at source?",
                "options": ["To make waste bins look aesthetically uniform along roads", "To separate biodegradable organics for composting from recyclables for processing", "To incinerate all waste types simultaneously at ultra-high temperatures", "To dump mixed waste into rivers during high tide cycles"],
                "answer": 1,
                "hint": "Green bins receive compostable organic matter; blue bins receive non-biodegradable recyclables.",
                "explanation": "Source segregation ensures organic biodegradable waste can be cleanly composted into fertilizer, while clean non-biodegradables like plastic and metals are routed to industrial recycling."
            },
            {
                "question": "Which set represents the comprehensive '5 R' framework for modern waste reduction?",
                "options": ["Refuse, Reduce, Reuse, Repurpose, Recycle", "React, Remove, Reheat, Replace, Resell", "Retain, Relocate, Rebuild, Restock, Return", "Recharge, Radiate, Reheat, Reduce, Reset"],
                "answer": 0,
                "hint": "The 5 R's begin with declining unnecessary packaging and end with material reprocessing.",
                "explanation": "The 5 R's of waste minimization are: Refuse (say no to single-use items), Reduce (consume less), Reuse (use items multiple times), Repurpose (adapt for new uses), and Recycle (reprocess materials)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Railway Cup Evolution",
        "subtitle": "Lifecycle assessments, glass sanitation, plastic culverts, clay topsoil, and paper cups",
        "speech": "The historical evolution of disposable beverage containers across Indian Railways presents an illuminating case study in environmental decision-making and sustainable resource management. Originally, hot tea on passenger trains was served in reusable glass glasses. However, collecting, thoroughly washing, and redistributing thousands of fragile glasses across moving trains proved logistically unhygienic, leading to widespread sanitary concerns and broken glass hazards. To solve this dilemma, Indian Railways introduced disposable plastic and polystyrene cups. While highly convenient and hygienic, discarded plastic cups were thrown out of train windows in astronomical volumes, littering tracks, choking drainage culverts, and creating an intolerable non-biodegradable pollution crisis. In response, an alternative plan proposed serving tea in disposable unglazed terracotta clay cups, locally known as kulhads. While completely biodegradable and culturally traditional, manufacturing hundreds of millions of kulhads required excavating immense quantities of fertile agricultural topsoil across rural brick kilns, threatening food security and aggravating soil erosion. Recognizing this unintended environmental consequence, modern railways transitioned to disposable, food-grade paper cups lined with thin biodegradable moisture barriers. Paper cups are manufactured from renewable plant pulp, decompose safely, and demonstrate how lifecycle environmental assessments must guide industrial material choices throughout modern industrial society, preventing unforeseen ecological damage across surrounding agricultural regions.",
        "checkpoints": [
            {
                "question": "Why was the large-scale introduction of clay 'kulhads' on railways discontinued despite being biodegradable?",
                "options": ["Clay cups altered the taste of tea to become bitter", "Manufacturing billions of kulhads depleted immense fertile agricultural topsoil", "Clay cups release toxic greenhouse gases when exposed to hot water", "Clay is completely impermeable to rainwater causing urban floods"],
                "answer": 1,
                "hint": "Making clay cups on a massive scale required digging up topsoil from farm fields.",
                "explanation": "Mass production of clay kulhads required excavating huge volumes of top fertile agricultural soil, causing severe soil erosion and threatening farming land."
            },
            {
                "question": "Why are modern food-grade paper cups considered an ecologically superior railway beverage container?",
                "options": ["They are made from durable heavy metal alloys that last centuries", "They are derived from renewable wood pulp, decompose naturally, and preserve topsoil", "They are completely non-biodegradable and impermeable to all bacteria", "They eliminate the need for drinking water on train journeys"],
                "answer": 1,
                "hint": "Paper comes from renewable tree pulp and decomposes organically without ruining topsoil.",
                "explanation": "Disposable paper cups are manufactured from renewable plant pulp, decompose safely through biological action, maintain hygiene, and avoid stripping fertile agricultural topsoil."
            }
        ]
    }
]

# Validation
print(f"Loaded {len(slides_part2)} slides for Part 2.")
for s in slides_part2:
    wc = len(s["speech"].split())
    print(f"Slide {s['id']}: '{s['title']}' -> {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} word count {wc} out of range (195-215)"
    assert len(s["title"].split()) <= 3, f"Slide {s['id']} title has more than 3 words: '{s['title']}'"
    assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    # Ensure no persona titles or fictional character names
    slide_str = json.dumps(s)
    for forbidden in ["Raghav", "Dr.", "Dr ", "Sir", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof."]:
        assert forbidden not in slide_str, f"Forbidden term '{forbidden}' in slide {s['id']}"

with open(".agents/c10s_ch13_part2.json", "w", encoding="utf-8") as f:
    json.dump(slides_part2, f, indent=2, ensure_ascii=False)

print("Part 2 (Slides 9 to 16) validated and saved successfully!")

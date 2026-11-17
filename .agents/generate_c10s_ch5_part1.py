#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for NCERT Class 10 Science Chapter 5: Life Processes.
Strict requirements:
- Titles: 1-3 words
- Speech: pure Indian male teacher voice, strictly 195-215 words per slide
- Zero persona titles (Dr, Sir, Madam, Mr, Mrs, Prof) and zero fictional character names
- 2 checkpoints per slide with 4 options, hint, and detailed explanation
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Life Molecular Movement",
        "subtitle": "Invisible Molecular Dynamics & Body Maintenance",
        "speech": (
            "Welcome students to our biology laboratory. When we observe living organisms, visible movements like a running "
            "dog, chewing cow, or shouting person provide obvious proof of life. In green plants, visible growth movements "
            "occur slowly over days, while breathing movements are seen in sleeping animals. However, visible movement alone "
            "cannot serve as an absolute defining criterion for life. The most vital movements sustaining living structures are "
            "completely invisible molecular movements occurring continuously within microscopic cells and cellular organelles. Living organisms exhibit highly "
            "organized physical structures consisting of specialized tissues, organized cells, and sub-cellular components. Due to environmental influences, thermal "
            "disturbances, and mechanical wear, this organized biological structure tends to break down over time. If this cellular order "
            "breaks down completely, the organism ceases to function and dies. Therefore, living creatures must continuously repair and "
            "maintain their structures through ceaseless molecular movements. Even non-cellular viruses show no molecular movement until they infect a "
            "host cell, which creates ongoing scientific debates about whether viruses are truly alive. Maintenance functions must persist "
            "uninterruptedly during sleep or physical stillness to preserve structural integrity, repair damaged tissues, and sustain life throughout existence. "
            "These vital microscopic dynamics prove that biological matter constantly expends metabolic energy to preserve its intricate cellular architecture against environmental degradation."
        ),
        "checkpoints": [
            {
                "question": "Why is visible movement alone insufficient to define whether an entity is living?",
                "options": [
                    "Molecular movements occur invisibly while some living plants show no rapid visible motion",
                    "Living organisms never show any visible physical movements at any stage",
                    "Visible movements only happen in non-living mechanical engines and machines",
                    "Environmental factors prevent all living organisms from moving visibly"
                ],
                "answer": 0,
                "hint": "Consider sleeping animals, slow plant growth, and microscopic cellular dynamics.",
                "explanation": "Plants grow slowly without immediate visible locomotion, and animals maintain vital molecular movements even while asleep."
            },
            {
                "question": "What happens to a living organism if invisible molecular maintenance ceases?",
                "options": [
                    "The organized cellular structure breaks down and the organism dies",
                    "The organism permanently transforms into an infectious crystalline virus",
                    "The organism enters an eternal dormant state without structural damage",
                    "The body increases its cellular organization through simple diffusion"
                ],
                "answer": 0,
                "hint": "Living order requires continuous energy and molecular repair against entropy.",
                "explanation": "Constant molecular repair is essential to counteract structural degradation; without it, tissues breakdown and death occurs."
            }
        ]
    },
    {
        "id": 2,
        "title": "Life Processes Overview",
        "subtitle": "Four Essential Functions & Multicellular Transport",
        "speech": (
            "Now let us examine life processes systematically. Life processes are defined as the combined ongoing maintenance functions "
            "that together keep an organism alive, ensuring continuous repair and structural stability even when an organism is inactive. "
            "Four interconnected physiological processes are universally essential: nutrition, respiration, transportation, and excretion. First, nutrition provides external carbon-based "
            "raw materials and chemical energy required for growth and tissue synthesis. Second, respiration brings oxygen into cells "
            "to oxidize organic nutrients, releasing energy in the form of uniform adenosine triphosphate molecules. Third, transportation distributes "
            "absorbed nutrients and oxygen across all body cells while collecting cellular metabolic by-products. In simple single-celled organisms like "
            "Amoeba, the entire body surface remains in direct contact with the surrounding aquatic environment, enabling simple diffusion to "
            "satisfy gas exchange, nutrient absorption, and waste removal. However, in complex multicellular organisms with specialized organ systems, "
            "individual cells are buried deep inside and cannot maintain direct contact with the outer environment. Because simple diffusion "
            "is exceedingly slow across large tissue distances, specialized vascular transportation networks are mandatory. Fourth, excretion eliminates toxic nitrogenous "
            "metabolic wastes generated by biochemical reactions, preventing cellular poisoning and maintaining an optimal internal chemical homeostasis to sustain healthy organismal life throughout existence."
        ),
        "checkpoints": [
            {
                "question": "Why is simple diffusion inadequate for gas and nutrient exchange in multicellular organisms?",
                "options": [
                    "Internal body cells are not in direct contact with the external environment",
                    "Diffusion only operates in non-living gaseous mixtures and solid minerals",
                    "Multicellular organisms lack internal chemical reactions that generate metabolic wastes",
                    "Diffusion transports materials too rapidly, causing severe osmotic cell rupture"
                ],
                "answer": 0,
                "hint": "Think about large tissue distances separating deep organs from surrounding air.",
                "explanation": "In large multicellular bodies, vast tissue distances prevent diffusion from supplying oxygen and nutrients to deep internal cells."
            },
            {
                "question": "Which set represents the four universal maintenance processes sustaining all living bodies?",
                "options": [
                    "Nutrition, respiration, internal transportation, and metabolic excretion",
                    "Locomotion, camouflage, hibernation, and acoustic communication",
                    "Fermentation, fossilization, calcification, and thermal convection",
                    "Bioluminescence, budding, vegetative regeneration, and spore dispersal"
                ],
                "answer": 0,
                "hint": "Focus on the core biochemical functions keeping organisms alive while resting.",
                "explanation": "Nutrition, respiration, transportation, and excretion constitute the fundamental life processes required by all living organisms."
            }
        ]
    },
    {
        "id": 3,
        "title": "Autotrophic Nutrition Mechanism",
        "subtitle": "Photosynthetic Chemistry & Solar Energy Conversion",
        "speech": (
            "Let us explore autotrophic nutrition, the biological engine powering the biosphere. Autotrophs, including green plants and certain photosynthetic "
            "bacteria, synthesize complex high-energy organic molecules from simple inorganic carbon dioxide and water using sunlight and chlorophyll. The "
            "balanced master equation of photosynthesis states that six carbon dioxide molecules react with twelve water molecules in the presence "
            "of light and chlorophyll to yield one glucose molecule, six oxygen molecules, and six water molecules. Unused glucose "
            "is stored inside plant cells as starch, serving as an internal energy reserve analogous to glycogen stored in human "
            "liver and muscle tissues. Photosynthesis proceeds through three fundamental sequential events. First, chlorophyll pigments within chloroplast thylakoids absorb "
            "solar photons. Second, absorbed light energy is converted into chemical energy while simultaneously splitting water molecules into hydrogen ions, "
            "electrons, and molecular oxygen through photolysis. Third, carbon dioxide is reduced to carbohydrates using assimilatory chemical power. These "
            "steps need not occur consecutively without interruption. In desert xerophytic plants, stomata open primarily at night to minimize water "
            "transpiration, taking up carbon dioxide to synthesize an intermediate organic acid. During daylight hours, chlorophyll absorbs solar energy to "
            "complete carbohydrate synthesis, demonstrating ecological biochemical adaptation to survive arid environmental conditions while maintaining necessary sugar production."
        ),
        "checkpoints": [
            {
                "question": "What is the primary carbohydrate storage form in autotrophic plants and animals respectively?",
                "options": [
                    "Starch in plants and glycogen in animals",
                    "Glycogen in plants and cellulose in animals",
                    "Glucose in plants and chitin in animals",
                    "Maltose in plants and lactose in animals"
                ],
                "answer": 0,
                "hint": "Plants store excess photosynthetic sugars as insoluble poly-glucose granules.",
                "explanation": "Unused carbohydrates are stored as starch in plant tissues, while animals store reserve carbohydrates as glycogen."
            },
            {
                "question": "How do desert plants adapt their photosynthetic carbon dioxide uptake to prevent water loss?",
                "options": [
                    "They absorb carbon dioxide at night, producing an intermediate processed in daylight",
                    "They eliminate the reduction phase of photosynthesis entirely",
                    "They utilize carbon monoxide absorbed through subterranean root hairs",
                    "They perform photosynthesis without light or chlorophyll using thermal steam"
                ],
                "answer": 0,
                "hint": "Consider night stomatal opening to avoid harsh daytime evaporation.",
                "explanation": "Xerophytes open stomata at night to absorb CO2 into an organic acid intermediate, which is reduced using daytime solar energy."
            }
        ]
    },
    {
        "id": 4,
        "title": "Leaf Starch Synthesis",
        "subtitle": "Cross-Section Anatomy & Variegated Starch Testing",
        "speech": (
            "We now examine internal leaf architecture and prove chlorophyll necessity through Activity 5.1. A microscopic transverse cross-section of "
            "a dorsiventral leaf reveals clear structural layers. The outermost upper surface is coated with a waterproof waxy cuticle "
            "layer, followed by a single-layered protective upper epidermis lacking chloroplasts. Beneath lies the photosynthetic mesophyll, packed with specialized "
            "palisade and spongy parenchyma cells containing numerous green cellular organelles called chloroplasts. Chloroplasts contain chlorophyll, the photosynthetic pigment. "
            "Interspersed vascular bundles supply water and dissolved minerals through xylem vessels while phloem tissues transport newly synthesized sucrose. The "
            "lower epidermis contains numerous microscopic stomatal pores flanked by regulatory guard cells. In Activity 5.1, we take a variegated "
            "leaf plant, such as money plant or croton, whose leaves possess distinct green and non-green white regions. We de-starch "
            "the potted plant by keeping it in complete darkness for three days, forcing cells to consume existing starch reserves. "
            "Next, we expose the plant to bright sunlight for six hours, detach a leaf, trace its green zones, "
            "and immerse it in boiling alcohol within a water bath to extract green chlorophyll. Rinsing the bleached leaf in "
            "dilute iodine solution causes only the previously green areas to turn deep blue-black, conclusively proving chlorophyll is indispensable for starch formation."
        ),
        "checkpoints": [
            {
                "question": "Why must the leaf be boiled in alcohol using a water bath rather than a direct flame?",
                "options": [
                    "Alcohol is highly inflammable and must be heated safely in a hot water bath",
                    "Alcohol evaporates instantly into ice crystals when exposed to open flame",
                    "Direct flame creates excess chlorophyll that darkens the entire leaf",
                    "Water baths convert alcohol into iodine solution needed for staining"
                ],
                "answer": 0,
                "hint": "Think about laboratory fire safety and alcohol's boiling point.",
                "explanation": "Alcohol is flammable; indirect heating inside a water bath prevents hazardous ignition while dissolving out leaf chlorophyll."
            },
            {
                "question": "What observation in Activity 5.1 confirms that chlorophyll is essential for starch synthesis?",
                "options": [
                    "Only the previously green leaf regions turn blue-black with iodine solution",
                    "The white non-green patches turn bright orange when exposed to sunlight",
                    "The entire leaf bleaches permanently into clear water without color change",
                    "The waxy cuticle layer dissolves completely into gaseous carbon dioxide"
                ],
                "answer": 0,
                "hint": "Iodine turns blue-black specifically in the presence of synthesized starch.",
                "explanation": "Blue-black staining occurs exclusively in chlorophyll-containing areas, proving photosynthetic starch production requires chlorophyll."
            }
        ]
    },
    {
        "id": 5,
        "title": "Stomatal Guard Cells",
        "subtitle": "Hydraulic Pore Regulation & Potassium Hydroxide Proof",
        "speech": (
            "Let us study stomatal mechanics and verify carbon dioxide requirements through Activity 5.2. Stomata are microscopic pores located predominantly "
            "on the lower epidermis of leaves, facilitating massive gaseous exchange of carbon dioxide and oxygen during active photosynthesis. Each "
            "stomatal pore is bounded by a pair of specialized kidney-shaped guard cells containing chloroplasts and possessing differentially thickened walls. "
            "The opening and closing of the stomatal aperture is a hydraulic turgor-driven mechanism. When surrounding epidermal cells transfer water "
            "into guard cells, they swell with osmotic pressure, causing their elastic outer walls to bulge outward while pulling the "
            "thick inner concave walls apart, thereby opening the pore. Conversely, when guard cells lose water, turgor pressure drops, "
            "causing them to shrink, straighten, and close the pore to conserve water. In Activity 5.2, two healthy de-starched potted "
            "plants are placed beneath separate airtight glass bell jars sealed with vaseline. Beside one plant, a watch glass containing "
            "potassium hydroxide crystals is placed to absorb all carbon dioxide from the enclosed atmosphere. After four hours of sunlight "
            "exposure, iodine testing reveals that leaves from the bell jar with potassium hydroxide fail to produce starch, demonstrating carbon "
            "dioxide is essential for photosynthesis. Roots also absorb vital soil minerals including nitrogen, phosphorus, iron, and magnesium."
        ),
        "checkpoints": [
            {
                "question": "What triggers the physical opening of a stomatal pore in plant leaves?",
                "options": [
                    "Water flows into guard cells, causing them to swell and curve open",
                    "Guard cells lose water completely and collapse against epidermal walls",
                    "Potassium hydroxide gas evaporates out through the outer cuticle layer",
                    "Atmospheric nitrogen creates negative vacuum pressure inside air spaces"
                ],
                "answer": 0,
                "hint": "Consider turgor pressure changes within guard cell walls.",
                "explanation": "When water enters guard cells, increased turgor pressure causes their curved outer walls to stretch, pulling the inner pore open."
            },
            {
                "question": "What is the specific role of potassium hydroxide in the bell jar experiment of Activity 5.2?",
                "options": [
                    "To chemically absorb all carbon dioxide from the enclosed jar atmosphere",
                    "To supply extra water vapor directly to the stomatal guard cells",
                    "To catalytically convert oxygen into starch without requiring sunlight",
                    "To dissolve the protective wax layer covering the lower leaf epidermis"
                ],
                "answer": 0,
                "hint": "KOH is a strong alkaline chemical absorbent for acidic gases.",
                "explanation": "Potassium hydroxide absorbs CO2 from the jar, creating a carbon-free environment that proves CO2 is essential for starch synthesis."
            }
        ]
    },
    {
        "id": 6,
        "title": "Heterotrophic Feeding Modes",
        "subtitle": "Saprophytic Fungi, Holozoic Ingestion & Parasitism",
        "speech": (
            "Now let us examine heterotrophic nutrition. Unlike autotrophs, heterotrophic organisms cannot synthesize their own organic food from inorganic precursors "
            "and must depend directly or indirectly on autotrophic biomass. Because food sources vary widely in nature, heterotrophs have evolved "
            "specialized digestive strategies categorized into saprophytic, holozoic, and parasitic modes. First, saprophytic nutrition is exhibited by fungi like bread "
            "mould Rhizopus, yeast, and mushrooms. Saprophytes release extracellular digestive enzymes directly onto dead, decaying organic matter, breaking down complex "
            "insoluble polymers into simple soluble molecules outside their bodies before absorbing them across their cellular hyphae. Second, holozoic nutrition "
            "involves ingesting whole food particles into the body, followed by internal enzymatic digestion, nutrient absorption, assimilation into tissues, and "
            "egestion of undigested waste. Humans, cows, birds, and Amoeba follow this holozoic path. Third, parasitic nutrition occurs when an organism "
            "derives sustained nourishment directly from a living host organism without killing it immediately. Parasitic plants such as Cuscuta, commonly known "
            "as amar-bel, penetrate host plant vascular bundles using specialized absorptive root-like structures called haustoria. In animals, external ectoparasites like "
            "ticks, lice, and leeches suck blood, while internal endoparasites like tapeworms and roundworms absorb pre-digested nutrients inside host intestines, "
            "demonstrating diverse evolutionary adaptations tailored to nutrient availability and feeding environments across the biological spectrum."
        ),
        "checkpoints": [
            {
                "question": "How do saprophytic organisms like mushrooms and bread moulds digest their food?",
                "options": [
                    "They secrete enzymes outside the body and absorb the digested nutrients",
                    "They swallow whole organisms and digest them inside a gastric stomach",
                    "They produce carbohydrates directly from carbon dioxide using sunlight",
                    "They suck blood from living host animals through specialized haustoria"
                ],
                "answer": 0,
                "hint": "Saprophytic digestion occurs externally upon dead organic substrates.",
                "explanation": "Saprophytes break down dead organic matter externally via secreted enzymes, then absorb the soluble breakdown products."
            },
            {
                "question": "Which organism is a classic example of a plant parasite deriving nutrition from a host?",
                "options": [
                    "Cuscuta (amar-bel)",
                    "Rhizopus (bread mould)",
                    "Paramoecium caudatum",
                    "Croton variegated plant"
                ],
                "answer": 0,
                "hint": "A leafless yellow climbing plant that coils around trees using haustoria.",
                "explanation": "Cuscuta is a non-green parasitic flowering plant that absorbs nutrients directly from host plant vascular tissues."
            }
        ]
    },
    {
        "id": 7,
        "title": "Unicellular Organism Digestion",
        "subtitle": "Amoeba Phagocytosis & Paramoecium Ciliary Wave",
        "speech": (
            "We now turn to nutrient acquisition in single-celled organisms, comparing Amoeba and Paramoecium. Because unicellular organisms consist of a "
            "single cell, their entire outer surface interacts directly with the surrounding aquatic environment. Amoeba lacks a permanent mouth or "
            "fixed digestive tract. When Amoeba senses a microscopic food particle, it extends temporary, flexible, finger-like projections of its cell "
            "membrane called pseudopodia. These pseudopodia gradually flow around and engulf the food particle, fusing together to form a temporary "
            "internal spherical chamber known as a food vacuole. Inside this food vacuole, complex food polymers are systematically broken down "
            "into simple soluble molecules by hydrolytic digestive enzymes secreted from the surrounding cytoplasm. The resulting simple nutrients diffuse directly "
            "into the cytoplasm to fuel cellular respiration, growth, and binary fission. Undigested waste material is subsequently moved to the "
            "periphery of the cell, where the outer membrane ruptures to expel it into the water via egestion. In contrast, "
            "Paramoecium maintains a rigid, definite slipper-shaped cellular morphology. Food particles cannot be engulfed at arbitrary membrane positions; instead, food "
            "is moved toward a specialized permanent intake spot called the oral groove or cytostome. This directional movement is driven "
            "by the coordinated, rhythmic, wave-like beating of thousands of microscopic hair-like cilia covering the entire Paramoecium cell surface."
        ),
        "checkpoints": [
            {
                "question": "How does Amoeba capture and engulf external food particles?",
                "options": [
                    "By extending flexible pseudopodia to surround food into a food vacuole",
                    "By beating specialized ciliary bands toward a fixed oral cytostome",
                    "By secreting external venom through rigid chitinous cell wall pores",
                    "By filtering water across internal vascular gills and sieve plates"
                ],
                "answer": 0,
                "hint": "Amoeba uses temporary false feet formed by cytoplasmic streaming.",
                "explanation": "Amoeba extends pseudopodia that encircle the food particle, forming a food vacuole where intracellular digestion occurs."
            },
            {
                "question": "What cellular structure enables Paramoecium to direct food toward its specific intake spot?",
                "options": [
                    "Thousands of coordinated hair-like cilia covering the cell surface",
                    "Temporary pseudopodia extending from the posterior contractile vacuole",
                    "A muscular peristaltic oesophagus lined with salivary glands",
                    "A chitinous jaw apparatus driven by hydraulic turgor pressure"
                ],
                "answer": 0,
                "hint": "Think of microscopic rhythmic oars covering the slipper-shaped organism.",
                "explanation": "The rhythmic beating of surface cilia creates fluid currents that guide food particles into Paramoecium's fixed oral groove."
            }
        ]
    },
    {
        "id": 8,
        "title": "Human Digestion Canal",
        "subtitle": "Buccal Cavity Saliva & Oesophageal Peristalsis",
        "speech": (
            "Let us begin exploring the human digestive system, starting from the mouth and oesophagus. The human alimentary canal is "
            "a continuous, highly specialized muscular tube approximately nine meters in length extending from mouth to anus. Digestion begins inside "
            "the buccal cavity. Teeth mechanically crush, tear, and masticate large food fragments into small uniform particles, increasing the surface "
            "area accessible to chemical enzymes. The muscular tongue rolls and mixes this masticated food with watery saliva secreted by "
            "three pairs of salivary glands. Saliva contains a critical biocatalytic enzyme named salivary amylase. In Activity 5.3, we test "
            "a starch solution treated with saliva against an untreated control using iodine. While the untreated starch solution turns deep "
            "blue-black, the saliva-treated starch tube shows no color change, confirming that salivary amylase hydrolyzes complex insoluble starch molecules into "
            "simple maltose sugars. Once food is thoroughly moistened into a slippery, cohesive bolus, the tongue pushes it backward into "
            "the pharynx. The wall of the oesophagus contains circular and longitudinal involuntary muscle layers that undergo rhythmic, coordinated contractions "
            "and relaxations known as peristalsis. Peristaltic waves propel the food bolus smoothly down the oesophagus into the stomach, preventing "
            "food accumulation. Saliva also neutralizes oral acids, protecting tooth enamel and dentine from bacterial decay that causes dental plaque."
        ),
        "checkpoints": [
            {
                "question": "What is the primary biochemical role of salivary amylase in the human buccal cavity?",
                "options": [
                    "To break down complex starch molecules into simpler sugars like maltose",
                    "To emulsify large dietary lipid droplets into microscopic micelles",
                    "To activate gastric pepsinogen into active hydrochloric acid",
                    "To convert soluble amino acids into insoluble structural proteins"
                ],
                "answer": 0,
                "hint": "Salivary amylase specifically targets dietary carbohydrates in the mouth.",
                "explanation": "Salivary amylase hydrolyzes insoluble complex starch into simpler disaccharide sugars like maltose in the mouth."
            },
            {
                "question": "What physiological mechanism pushes the food bolus downward through the oesophagus?",
                "options": [
                    "Rhythmic muscular contractions and relaxations known as peristalsis",
                    "Simple gravitational free fall through a rigid open cartilaginous tube",
                    "High-pressure suction created by rapid diaphragmatic inhalation",
                    "Ciliary wave motion driven by epidermal mucous cell beating"
                ],
                "answer": 0,
                "hint": "Involuntary muscular waves ensure food moves along the entire gut.",
                "explanation": "Peristaltic movements—rhythmic waves of muscular contraction and relaxation—push food along the alimentary canal."
            }
        ]
    }
]

with open('.agents/c10s_ch5_part1.json', 'w', encoding='utf-8') as f:
    json.dump(slides_part1, f, indent=2)

print("Slide part 1 (Slides 1-8) successfully written!")
for s in slides_part1:
    wc = len(s['speech'].split())
    print(f"Slide {s['id']}: '{s['title']}' - {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} speech word count {wc} out of range!"

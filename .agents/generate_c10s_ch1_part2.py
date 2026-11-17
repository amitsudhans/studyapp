#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Slides 9-16 for NCERT Class 10 Science - Chapter 1: Chemical Reactions and Equations
Strict constraints:
- Title strictly 1-3 words.
- Spoken lecture strictly 195-215 words.
- Pure Indian male teacher voice styling.
- Zero persona titles (Dr, Sir, Mr, Mrs, etc.) and zero fictional human names (Raghav, etc.).
- 2 checkpoints per slide with 4 options, hint, and explanation.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Exothermic Chemical Reactions",
        "subtitle": "Heat Liberation, Methane Combustion, Respiration, and Composting",
        "speech": (
            "We now explore chemical energetics, specifically exothermic chemical reactions. By definition, reactions "
            "in which heat energy is liberated along with the formation of products are classified as exothermic reactions. "
            "A familiar domestic example is the combustion of natural gas, primarily methane: CH4 gas plus two molecules "
            "of oxygen gas combust to yield carbon dioxide gas, water vapor, and substantial thermal energy. Have you ever "
            "wondered why eating food keeps our body warm? Cellular respiration is a vital exothermic biochemical process. "
            "During digestion, carbohydrates break down into simple glucose. In our body cells, this dissolved glucose "
            "combines with inhaled oxygen through enzymatic oxidation: C6H12O6 aqueous plus 6O2 yields 6CO2 plus 6H2O, "
            "liberating the metabolic energy that powers all biological cellular activity. Another natural exothermic "
            "transformation occurs during the decomposition of vegetable peelings, garden clippings, and animal dung "
            "into agricultural compost inside bio-digesters. Thermophilic microbes break molecular bonds, generating "
            "noticeable heat within the compost pile. In every exothermic reaction, the chemical potential energy stored "
            "in the reactant bonds exceeds the energy of product bonds, with the surplus energy discharged outward into the "
            "surrounding laboratory environment as heat, radiant warmth, or light, elevating the ambient system temperature naturally."
        ),
        "checkpoints": [
            {
                "question": "Why is cellular respiration scientifically classified as an exothermic chemical reaction?",
                "options": [
                    "It consumes electrical current from nerve cells",
                    "It releases metabolic energy along with carbon dioxide and water",
                    "It cools the bloodstream down to ambient room temperature",
                    "It absorbs external heat to synthesize complex carbohydrates"
                ],
                "answer": 1,
                "hint": "Consider the energy release when glucose oxidizes in living cells.",
                "explanation": "Cellular respiration oxidizes glucose to produce carbon dioxide, water, and metabolic energy (C6H12O6 + 6O2 -> 6CO2 + 6H2O + Energy), defining an exothermic process."
            },
            {
                "question": "Which of the following processes represents an exothermic reaction?",
                "options": [
                    "Photosynthesis in green leaves",
                    "Decomposition of vegetable matter into organic compost",
                    "Dissolution of ammonium chloride in water",
                    "Thermal breakdown of limestone into quicklime"
                ],
                "answer": 1,
                "hint": "Look for a biological decomposition process that releases warmth.",
                "explanation": "Microbial decomposition of vegetable matter into organic compost releases thermal energy, qualifying as an exothermic chemical change."
            }
        ]
    },
    {
        "id": 10,
        "title": "Thermal Decomposition Reactions",
        "subtitle": "Activity 1.5 & 1.6: Ferrous Sulphate, Limestone, and Lead Nitrate",
        "speech": (
            "Let us examine decomposition reactions, where a single chemical reactant splits into two or more simpler "
            "products. When decomposition is driven by heating, it is termed thermal decomposition. In Activity 1.5, "
            "heating dry green ferrous sulphate crystals in a boiling tube causes them to lose seven molecules of water "
            "of crystallization, changing colour from green to white. Further strong heating decomposes anhydrous ferrous "
            "sulphate into solid reddish-brown ferric oxide, while emitting choking gases with the pungent odour of burning "
            "sulphur: sulphur dioxide and sulphur trioxide. Industrially, heating calcium carbonate or limestone produces "
            "calcium oxide and carbon dioxide gas, the crucial reaction underpinning worldwide cement manufacturing. In "
            "Activity 1.6, heating white lead nitrate powder in a dry test tube produces crackling decrepitation. Dense, "
            "pungent reddish-brown fumes of nitrogen dioxide gas billow out, leaving behind a yellow residue of lead monoxide "
            "along with invisible oxygen gas: two formula units of lead nitrate decompose into two units of lead oxide, four "
            "molecules of nitrogen dioxide, and one oxygen molecule. In all these examples, thermal energy actively breaks "
            "chemical bonds within a complex compound, yielding multiple smaller, stable product fragments while requiring "
            "continuous external heat input to drive the endothermic cleavage process."
        ),
        "checkpoints": [
            {
                "question": "What characteristic observation is noted when dry lead nitrate powder is heated in Activity 1.6?",
                "options": [
                    "Evolution of dense reddish-brown fumes of nitrogen dioxide",
                    "Precipitation of a bright white insoluble solid",
                    "Formation of a clear blue solution in the tube",
                    "Evolution of hydrogen gas that burns with a pop sound"
                ],
                "answer": 0,
                "hint": "Recall the pungent brown gas emitted during lead nitrate thermal cleavage.",
                "explanation": "Thermal decomposition of lead nitrate (2Pb(NO3)2 -> 2PbO + 4NO2 + O2) liberates dense brown fumes of nitrogen dioxide (NO2) gas."
            },
            {
                "question": "What industrial product is manufactured by the thermal decomposition of limestone?",
                "options": [
                    "Nitrogen fertilizers for farming",
                    "Quicklime (calcium oxide) used in cement manufacturing",
                    "Lead monoxide pigments for paints",
                    "Sulphuric acid for lead-acid batteries"
                ],
                "answer": 1,
                "hint": "Heating limestone (CaCO3) yields quicklime (CaO) and carbon dioxide.",
                "explanation": "Thermal decomposition of limestone (CaCO3 -> CaO + CO2) yields calcium oxide (quicklime), a vital raw material in modern cement manufacturing."
            }
        ]
    },
    {
        "id": 11,
        "title": "Electrolytic Water Decomposition",
        "subtitle": "Activity 1.7: 6V Setup, Carbon Electrodes, and 2:1 Volume Ratio",
        "speech": (
            "Not all decomposition reactions rely on heat; electrical energy can also cleave chemical bonds. This process "
            "is termed electrolytic decomposition or electrolysis. In Activity 1.7, two holes are drilled in the base of a "
            "plastic mug, fitted with rubber stoppers and graphite carbon electrodes. The mug is filled with water, and a "
            "few drops of dilute sulphuric acid are added to increase electrical conductivity. Two inverted graduated test "
            "tubes filled with water are positioned over the electrodes, and a 6-volt direct current battery is connected. "
            "Immediately, gas bubbles begin forming at both electrodes, displacing water downward by downward displacement. "
            "Carefully observe the collected gas volumes: the volume of gas gathered at the negative electrode, called the "
            "cathode, is exactly double the volume collected at the positive electrode, called the anode. Why this precise "
            "two-to-one ratio? The water molecule consists of two hydrogen atoms covalently bonded to one oxygen atom. "
            "Electrochemical cleavage splits two molecules of liquid water into two molecules of diatomic hydrogen gas at "
            "the cathode and one molecule of diatomic oxygen gas at the anode. Testing with a glowing splinter confirms that "
            "cathode gas burns with a pop, while anode gas rekindles the flame vigorously."
        ),
        "checkpoints": [
            {
                "question": "Why is the volume of gas collected at the cathode double that at the anode in water electrolysis?",
                "options": [
                    "Hydrogen gas is twice as dense as oxygen gas",
                    "Water contains two hydrogen atoms for every one oxygen atom (H2O)",
                    "The cathode operates at twice the electrical voltage of the anode",
                    "Oxygen gas dissolves completely into the acidic electrolyte"
                ],
                "answer": 1,
                "hint": "Consider the molecular chemical formula and stoichiometry of water (H2O).",
                "explanation": "Water molecules have the formula H2O. Electrolysis yields two moles of hydrogen gas at the cathode for every one mole of oxygen gas at the anode (2H2O -> 2H2 + O2), producing a 2:1 volume ratio."
            },
            {
                "question": "What is the purpose of adding a few drops of dilute sulphuric acid to water before electrolysis?",
                "options": [
                    "To act as a bleaching agent for the electrodes",
                    "To provide free ions and enhance electrical conductivity",
                    "To prevent hydrogen gas from exploding in the tube",
                    "To neutralize the graphite electrodes before current flows"
                ],
                "answer": 1,
                "hint": "Pure water is a poor electrical conductor due to minimal self-ionization.",
                "explanation": "Pure water has very low electrical conductivity. Adding dilute sulphuric acid introduces free ions, greatly accelerating electrolysis."
            }
        ]
    },
    {
        "id": 12,
        "title": "Photolytic Chemical Decomposition",
        "subtitle": "Activity 1.8: Sunlight Cleavage, Silver Halides, and Photography",
        "speech": (
            "When chemical decomposition is initiated by radiant light energy, the reaction is termed photolysis or "
            "photolytic decomposition. In Activity 1.8, placing two grams of pure white silver chloride in a clean china "
            "dish on a sunny windowsill reveals a fascinating light-activated change. Exposed to sunlight, the pristine "
            "white crystals gradually turn dull grey over several minutes. What causes this colour alteration? Solar light "
            "photons carry sufficient quantum energy to break the ionic bonds between silver and chlorine: two formula "
            "units of solid silver chloride decompose under sunlight into two atoms of lustrous grey silver metal and one "
            "molecule of pale green chlorine gas. The chlorine gas escapes silently into the atmosphere, leaving pure silver "
            "powder in the dish. A completely analogous photolytic decomposition occurs with pale yellow silver bromide: "
            "two AgBr solid decompose under light into two Ag solid plus diatomic bromine gas. This specific photochemical "
            "reaction formed the historic chemical cornerstone of black-and-white photography for over a century. Because "
            "decomposition reactions require energy input—whether thermal heat, electrical current, or radiant sunlight—to "
            "break strong reactant bonds, they are fundamentally endothermic chemical transformations, as also seen when "
            "mixing solid barium hydroxide crystals with ammonium chloride in an ice-cold flask."
        ),
        "checkpoints": [
            {
                "question": "What causes white silver chloride to turn grey when placed in sunlight during Activity 1.8?",
                "options": [
                    "Absorption of ambient atmospheric moisture",
                    "Photolytic decomposition into elemental silver metal and chlorine gas",
                    "Oxidation of silver to form black silver oxide",
                    "Formation of an insoluble carbonate crust from ambient air"
                ],
                "answer": 1,
                "hint": "Solar photons break the chemical bonds, liberating silver metal.",
                "explanation": "Sunlight causes photolysis of silver chloride (2AgCl -> 2Ag + Cl2), yielding metallic silver powder which appears grey."
            },
            {
                "question": "Which silver halide photochemical reaction was historically utilized in black-and-white photography?",
                "options": [
                    "Photolytic decomposition of silver bromide (AgBr)",
                    "Thermal oxidation of silver iodide (AgI)",
                    "Precipitation of silver fluoride in darkrooms",
                    "Acidic displacement of silver nitrate crystals"
                ],
                "answer": 0,
                "hint": "Think of the silver halide that decomposes under light into silver and bromine.",
                "explanation": "Photolytic decomposition of silver bromide (2AgBr -> 2Ag + Br2) was the core light-sensitive reaction used in black-and-white photographic film."
            }
        ]
    },
    {
        "id": 13,
        "title": "Single Displacement Reactions",
        "subtitle": "Activity 1.9: Iron in Copper Sulphate and the Reactivity Series",
        "speech": (
            "We now explore single displacement reactions. In a displacement reaction, a more chemically reactive element "
            "displaces or expels a less reactive element from its aqueous compound. Activity 1.9 illustrates this principle "
            "cleanly. Clean iron nails, scrubbed with sandpaper to remove surface grease, are immersed into a test tube "
            "containing deep blue copper sulphate solution for twenty minutes. When retrieved, the iron nails have acquired "
            "a distinctive reddish-brown coating, while the brilliant blue solution has faded to a pale light-green tint. "
            "What occurred on the atomic scale? Iron occupies a higher position than copper on the chemical reactivity "
            "series, meaning iron has a stronger thermodynamic tendency to lose electrons. Solid iron atoms displace copper "
            "ions from solution: Fe solid plus CuSO4 aqueous yields FeSO4 aqueous plus solid Cu. The faded green solution "
            "is dissolved ferrous sulphate, while the reddish-brown deposit on the nails is metallic copper. Similarly, "
            "zinc metal immersed in copper sulphate displaces copper to form colourless zinc sulphate, and lead displaces "
            "copper from copper chloride to form lead chloride. These experiments confirm that more reactive electropositive metals reliably "
            "displace less active noble metals from their dissolved aqueous salts in predictable single displacement fashion inside chemistry laboratories."
        ),
        "checkpoints": [
            {
                "question": "Why does the blue colour of copper sulphate solution fade to pale green when iron nails are immersed?",
                "options": [
                    "Copper ions evaporate into the surrounding laboratory air",
                    "Iron displaces copper, forming green ferrous sulphate solution (FeSO4)",
                    "Iron nails absorb all dissolved sulphate ions from solution",
                    "The solution turns basic due to atmospheric hydrogen dissolution"
                ],
                "answer": 1,
                "hint": "Iron is more reactive than copper and forms ferrous sulphate.",
                "explanation": "More reactive iron displaces copper from copper sulphate (Fe + CuSO4 -> FeSO4 + Cu), forming pale green ferrous sulphate solution while copper plates onto the nail."
            },
            {
                "question": "Which of the following metals can successfully displace copper from an aqueous copper sulphate solution?",
                "options": [
                    "Gold metal",
                    "Silver metal",
                    "Zinc metal",
                    "Platinum metal"
                ],
                "answer": 2,
                "hint": "Select the metal that is positioned higher than copper in the metal reactivity series.",
                "explanation": "Zinc is more chemically reactive than copper (Zn + CuSO4 -> ZnSO4 + Cu) and readily displaces copper from its salt solution, whereas silver, gold, and platinum are less reactive."
            }
        ]
    },
    {
        "id": 14,
        "title": "Double Displacement Reactions",
        "subtitle": "Activity 1.10: Mutual Ion Exchange and Insoluble Precipitates",
        "speech": (
            "Double displacement reactions involve a mutual exchange of ions between two aqueous reactant compounds to "
            "produce two entirely new substances. The general pattern is: compound AB plus compound CD yields AD plus CB. "
            "In Activity 1.10, three millilitres of aqueous sodium sulphate solution are mixed with three millilitres of "
            "aqueous barium chloride solution. Instantly, an opaque, brilliant white insoluble solid forms throughout "
            "the mixture. Any chemical reaction that generates an insoluble solid precipitate is classified as a precipitation "
            "reaction. What is the identity of this white precipitate? Barium cations, carrying a plus two charge, unite "
            "with sulphate anions, carrying a minus two charge, to precipitate insoluble barium sulphate: Na2SO4 aqueous "
            "plus BaCl2 aqueous yields BaSO4 solid precipitate plus two NaCl aqueous. The sodium and chloride ions remain "
            "dissolved as soluble table salt in the water. We can revisit Activity 1.2 in this light: aqueous lead nitrate "
            "reacts with potassium iodide through double displacement, exchanging nitrate and iodide ions to precipitate "
            "bright yellow lead iodide while leaving soluble potassium nitrate in solution. Double displacement reactions "
            "are pivotal in analytical chemistry, wastewater heavy-metal removal, and industrial chemical pigment synthesis "
            "used throughout modern textile, paper, and paint manufacturing facilities."
        ),
        "checkpoints": [
            {
                "question": "What is the white precipitate formed when sodium sulphate reacts with barium chloride in Activity 1.10?",
                "options": [
                    "Barium sulphate (BaSO4)",
                    "Sodium chloride (NaCl)",
                    "Barium sulphite (BaSO3)",
                    "Sodium oxide (Na2O)"
                ],
                "answer": 0,
                "hint": "Identify the insoluble ionic compound formed by mutual exchange of ions.",
                "explanation": "Mixing sodium sulphate and barium chloride results in double displacement, precipitating insoluble white barium sulphate (Na2SO4 + BaCl2 -> BaSO4 + 2NaCl)."
            },
            {
                "question": "How is a precipitation reaction defined in chemical science?",
                "options": [
                    "Any reaction that releases volatile gaseous byproducts",
                    "Any reaction that produces an insoluble solid substance",
                    "Any reaction that requires electrical current to proceed",
                    "Any reaction that produces neutral water molecules only"
                ],
                "answer": 1,
                "hint": "Focus on the physical state of the newly formed insoluble compound.",
                "explanation": "A precipitation reaction is formally defined as any chemical reaction in solution that generates an insoluble solid precipitate."
            }
        ]
    },
    {
        "id": 15,
        "title": "Oxidation and Reduction",
        "subtitle": "Activity 1.11: Copper Oxidation, Hydrogen Reduction, and Redox Transfers",
        "speech": (
            "We now examine oxidation and reduction reactions, commonly unified as redox reactions. Classically, oxidation "
            "is defined as the gain of oxygen or the loss of hydrogen by a substance. Conversely, reduction is defined as "
            "the loss of oxygen or the gain of hydrogen. Activity 1.11 demonstrates both processes sequentially. When brown "
            "copper powder is heated in a china dish over a burner, its surface turns jet black. Copper metal combines with "
            "atmospheric oxygen to form black copper(II) oxide: two Cu plus O2 yields two CuO. Here, copper gains oxygen and "
            "is oxidised. Now, if hot hydrogen gas is passed over this blackened copper oxide, the black coating turns back "
            "into lustrous reddish-brown copper metal: CuO plus H2 yields Cu plus H2O. In this reverse step, copper oxide "
            "loses oxygen and is reduced to copper metal, while hydrogen gas gains oxygen and is oxidised to water. Because "
            "oxidation and reduction always occur concurrently, such coupled transformations are called redox reactions. "
            "Other classic redox examples include zinc oxide reacting with carbon to produce zinc metal and carbon monoxide, "
            "and manganese dioxide reacting with hydrochloric acid to yield manganese chloride, water, and chlorine gas, "
            "demonstrating fundamental electron and oxygen atom transfers across chemical systems."
        ),
        "checkpoints": [
            {
                "question": "In the reaction CuO + H2 -> Cu + H2O, which substance is reduced and which is oxidised?",
                "options": [
                    "CuO is oxidised to Cu; H2 is reduced to H2O",
                    "CuO is reduced to Cu; H2 is oxidised to H2O",
                    "Both CuO and H2 undergo simultaneous oxidation",
                    "Neither substance experiences any change in oxygen content"
                ],
                "answer": 1,
                "hint": "Identify which substance loses oxygen and which substance gains oxygen.",
                "explanation": "Copper oxide (CuO) loses oxygen to become copper (Cu), so it is reduced. Hydrogen gas (H2) gains oxygen to form water (H2O), so it is oxidised."
            },
            {
                "question": "What is the black compound formed when brown copper powder is heated in air during Activity 1.11?",
                "options": [
                    "Copper(I) oxide (Cu2O)",
                    "Copper(II) oxide (CuO)",
                    "Copper carbonate (CuCO3)",
                    "Copper sulphate (CuSO4)"
                ],
                "answer": 1,
                "hint": "Copper oxidizes to its divalent black oxide form.",
                "explanation": "Heating copper powder in air oxidizes it to form black copper(II) oxide (2Cu + O2 -> 2CuO)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Corrosion and Rancidity",
        "subtitle": "Metal Degradation, Oxide Patinas, Food Oxidation, and Nitrogen Packaging",
        "speech": (
            "To conclude our chemical foundation, let us observe the widespread effects of oxidation in daily life: corrosion "
            "and rancidity. Corrosion is the gradual degradation of metals when attacked by substances in their surrounding "
            "environment, such as moisture, oxygen, and acids. The most infamous example is the rusting of iron: in damp "
            "monsoon air, iron oxidizes into hydrated ferric oxide, a flaky reddish-brown powder that detaches, exposing "
            "fresh metal to continuous destruction. Silver ornaments develop a tarnished black coating of silver sulphide "
            "due to atmospheric hydrogen sulphide, while copper vessels develop a green patina of basic copper carbonate. "
            "Corrosion causes billions of rupees in structural damage annually to bridges, railway lines, car bodies, and "
            "ships. Meanwhile, rancidity represents the oxidative degradation of fats and edible oils in stored food. Over "
            "time, atmospheric oxygen oxidizes lipid molecules, creating volatile fatty acids and aldehydes with foul tastes "
            "and unpleasant odours. Food processors prevent rancidity by adding synthetic antioxidants like BHT, storing "
            "snacks in airtight containers, and flushing bags of potato chips with unreactive nitrogen gas to displace "
            "oxygen completely, ensuring prolonged crispness, nutritional safety, and fresh taste across commercial food supply chains "
            "operating worldwide in modern food logistics."
        ),
        "checkpoints": [
            {
                "question": "Why do snack manufacturers flush potato chip bags with nitrogen gas before sealing?",
                "options": [
                    "To add a savoury nitrogenous flavour to the chips",
                    "To displace oxygen and prevent oxidative rancidity of oils",
                    "To make the package completely biodegradable in soil",
                    "To keep the chips chilled without refrigeration"
                ],
                "answer": 1,
                "hint": "Nitrogen is an unreactive gas that prevents lipids from reacting with atmospheric oxygen.",
                "explanation": "Flushing snack bags with inert nitrogen gas displaces oxygen, preventing oxidation of fats and oils and thereby averting rancidity."
            },
            {
                "question": "What is the chemical nature of the green coating that gradually develops on copper vessels exposed to moist air?",
                "options": [
                    "Copper chloride crystals",
                    "Basic copper carbonate patina",
                    "Black copper(II) oxide layer",
                    "Anhydrous copper sulphate"
                ],
                "answer": 1,
                "hint": "Formed when copper reacts with atmospheric carbon dioxide, oxygen, and water.",
                "explanation": "Copper corrodes in moist air containing carbon dioxide to form a protective green patina of basic copper carbonate (CuCO3·Cu(OH)2)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        twc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) - Speech: {wc} words")
        assert 1 <= twc <= 3, f"Title length out of bounds: {twc}"
        assert 195 <= wc <= 215, f"Speech word count out of bounds on slide {s['id']}: {wc}"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("Part 2 verification: ALL PASSED!")

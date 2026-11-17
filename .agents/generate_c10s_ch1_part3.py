#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Slides 17-20 for NCERT Class 10 Science - Chapter 1: Chemical Reactions and Equations
Strict constraints:
- Title strictly 1-3 words.
- Spoken speech strictly 0 words (speech: "").
- Silent quiz slides.
- Exactly 10 questions per slide (total 40 questions).
- Each question has 4 options, answer index, hint, explanation, and 3 solution_steps.
- Zero persona titles (Dr, Sir, etc.) and zero fictional human names (Raghav, etc.).
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Chemical Equations Review",
        "subtitle": "Mastery Challenge: Hallmarks, Law of Conservation of Mass, and Balancing Equations",
        "speech": "",
        "questions": [
            {
                "question": "Which of the following observations confirms that a chemical reaction has taken place when zinc granules react with dilute sulphuric acid?",
                "options": [
                    "A decrease in temperature and evaporation of zinc",
                    "Evolution of hydrogen gas and noticeable temperature rise",
                    "Formation of an insoluble yellow precipitate",
                    "No change in temperature or physical state"
                ],
                "answer": 1,
                "hint": "Recall Activity 1.3: zinc reacts with acid liberating a gas that pops near a flame and produces warmth.",
                "explanation": "Zinc reacts with dilute sulphuric acid (Zn + H2SO4 -> ZnSO4 + H2) producing hydrogen gas and releasing heat, demonstrating two hallmarks: gas evolution and temperature change.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Zinc granules (Zn solid) react with dilute sulphuric acid (H2SO4 aqueous) in a conical flask.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Zinc displaces hydrogen from the acid: Zn(s) + H2SO4(aq) -> ZnSO4(aq) + H2(g) + Heat. Hydrogen gas bubbles evolve vigorously.",
                    "Step 3: Verification & Real-World Application: The gas pops with a burning candle, and the flask warms up, confirming an exothermic reaction with gas evolution."
                ]
            },
            {
                "question": "Why must every skeletal chemical equation be balanced before quantitative use?",
                "options": [
                    "To satisfy Avogadro's hypothesis of gaseous volumes",
                    "To satisfy the universal Law of Conservation of Mass",
                    "To ensure the products always exceed the reactants in volume",
                    "To make all chemical coefficients even numbers"
                ],
                "answer": 1,
                "hint": "Matter can neither be created nor destroyed during chemical transformations.",
                "explanation": "According to the Law of Conservation of Mass, the total mass and atom counts of each element must remain constant before and after a reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: A skeletal equation shows only chemical formulas without matching atom counts on reactant and product sides.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Antoine Lavoisier formulated that mass cannot be created or destroyed. Therefore, atoms of each element entering a reaction must equal atoms emerging.",
                    "Step 3: Verification & Real-World Application: Balancing provides exact stoichiometric coefficients ensuring physical reality and conservation of mass in industrial manufacturing."
                ]
            },
            {
                "question": "What is the stoichiometric coefficient of O2 when balancing the combustion of butane: 2 C4H10 + _ O2 -> 8 CO2 + 10 H2O?",
                "options": ["10", "12", "13", "15"],
                "answer": 2,
                "hint": "Calculate total oxygen atoms on the product side: (8 * 2) + (10 * 1) = 26 atoms.",
                "explanation": "The product side has (8 * 2) + 10 = 26 oxygen atoms. Since oxygen exists as diatomic O2, 26 / 2 = 13 molecules of O2 are required.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Reactant side: 2 C4H10 (8 Carbon, 20 Hydrogen) + x O2. Product side: 8 CO2 (8 Carbon, 16 Oxygen) + 10 H2O (20 Hydrogen, 10 Oxygen).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Total oxygen atoms on RHS = 16 (from CO2) + 10 (from H2O) = 26 atoms. Diatomic oxygen requires 26 / 2 = 13 molecules.",
                    "Step 3: Verification & Real-World Application: 2 C4H10 + 13 O2 -> 8 CO2 + 10 H2O balances 8 Carbon, 20 Hydrogen, and 26 Oxygen on both sides."
                ]
            },
            {
                "question": "What physical state symbol correctly represents an aqueous solution of a chemical substance?",
                "options": ["(s)", "(l)", "(g)", "(aq)"],
                "answer": 3,
                "hint": "Aqueous denotes that the solute is dissolved in water solvent.",
                "explanation": "In chemical notation, (s) denotes solid, (l) denotes liquid, (g) denotes gas, and (aq) denotes aqueous solution (dissolved in water).",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Standard IUPAC notations describe physical phases of reacting species in chemical equations.",
                    "Step 2: Reaction Mechanism & Stoichiometry: A pure liquid is written as (l), whereas a compound dissolved in water as solvent is denoted as (aq) for aqueous.",
                    "Step 3: Verification & Real-World Application: For example, NaCl(aq) indicates dissolved table salt solution, distinct from molten NaCl(l)."
                ]
            },
            {
                "question": "When balancing Fe + H2O -> Fe3O4 + H2, why do we balance oxygen atoms before hydrogen and iron?",
                "options": [
                    "Because oxygen has the lowest atomic mass",
                    "Because hit-and-trial begins with the element having the maximum number of atoms",
                    "Because oxygen only exists as a liquid in this reaction",
                    "Because iron atoms cannot be counted until all gases are balanced"
                ],
                "answer": 1,
                "hint": "Step 3 of the hit-and-trial protocol selects the formula with the highest atom count.",
                "explanation": "Step 3 of the 7-step hit-and-trial method mandates balancing the element with the largest number of atoms first, which is oxygen (4 atoms in Fe3O4).",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Identify formulas: Fe, H2O, Fe3O4, H2. Count atoms: Fe (1 vs 3), H (2 vs 2), O (1 vs 4).",
                    "Step 2: Reaction Mechanism & Stoichiometry: The highest atom count belongs to oxygen in Fe3O4 (4 atoms). Balancing oxygen first with coefficient 4 before H2O simplifies subsequent steps.",
                    "Step 3: Verification & Real-World Application: Balancing oxygen to 4 H2O fixes hydrogen at 8, which easily balances by placing 4 before H2 on the RHS."
                ]
            },
            {
                "question": "What reaction conditions are specified for the industrial synthesis of methanol: CO(g) + 2H2(g) -> CH3OH(l)?",
                "options": [
                    "Sub-zero cryogenic freezing",
                    "340 atm pressure above the reaction arrow",
                    "Complete vacuum in an unsealed container",
                    "Exposure to ultraviolet darkness"
                ],
                "answer": 1,
                "hint": "High industrial pressure drives carbon monoxide and hydrogen gas to condense into liquid methanol.",
                "explanation": "The industrial synthesis of methanol requires a high pressure of 340 atm, written above the reaction arrow: CO(g) + 2H2(g) --[340 atm]--> CH3OH(l).",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Carbon monoxide gas and hydrogen gas react to form liquid methanol.",
                    "Step 2: Reaction Mechanism & Stoichiometry: CO(g) + 2H2(g) -> CH3OH(l). High pressure shifts the thermodynamic equilibrium toward the lower-volume product.",
                    "Step 3: Verification & Real-World Application: The notation '340 atm' above the arrow specifies the required reaction environment for successful chemical yield."
                ]
            },
            {
                "question": "Which of the following represents a balanced equation for the reaction of barium chloride with aluminium sulphate?",
                "options": [
                    "BaCl2 + Al2(SO4)3 -> BaSO4 + AlCl3",
                    "3 BaCl2 + Al2(SO4)3 -> 3 BaSO4 + 2 AlCl3",
                    "2 BaCl2 + 3 Al2(SO4)3 -> 2 BaSO4 + 3 AlCl3",
                    "3 BaCl2 + 2 Al2(SO4)3 -> 3 BaSO4 + 4 AlCl3"
                ],
                "answer": 1,
                "hint": "Check that barium is 3, sulphate is 3, aluminium is 2, and chlorine is 6 on both sides.",
                "explanation": "3BaCl2 + Al2(SO4)3 -> 3BaSO4 + 2AlCl3 balances 3 Ba, 6 Cl, 2 Al, and 3 SO4 groups on both sides.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Reactants: BaCl2 and Al2(SO4)3. Products: BaSO4 precipitate and AlCl3 solution.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Three sulphate ions in Al2(SO4)3 require 3 BaCl2, forming 3 BaSO4 and releasing 6 Cl- ions. Two Al3+ ions combine with 6 Cl- to form 2 AlCl3.",
                    "Step 3: Verification & Real-World Application: Both sides have 3 Ba, 2 Al, 6 Cl, 3 S, and 12 O atoms, satisfying the Law of Conservation of Mass."
                ]
            },
            {
                "question": "What occurs when quicklime (calcium oxide) is added to water in Activity 1.4?",
                "options": [
                    "A mild cooling sensation with freezing of water",
                    "A vigorous hissing reaction releasing immense heat to form slaked lime",
                    "Evolution of choking brown nitrogen dioxide fumes",
                    "Instant precipitation of insoluble green copper crystals"
                ],
                "answer": 1,
                "hint": "CaO reacts exothermically with water to synthesize Ca(OH)2.",
                "explanation": "Calcium oxide combines vigorously with water (CaO + H2O -> Ca(OH)2 + Heat), releasing significant thermal energy in an exothermic combination reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid calcium oxide (CaO) is hydrated with liquid water (H2O).",
                    "Step 2: Reaction Mechanism & Stoichiometry: CaO(s) + H2O(l) -> Ca(OH)2(aq) + Heat. Two reactants combine into a single product, calcium hydroxide.",
                    "Step 3: Verification & Real-World Application: The release of heat causes the beaker to boil, illustrating an exothermic combination reaction used for whitewash preparation."
                ]
            },
            {
                "question": "In the reaction 2 Pb(NO3)2 -> 2 PbO + 4 NO2 + O2, what is the oxidation state of lead in PbO?",
                "options": ["+1", "+2", "+3", "+4"],
                "answer": 1,
                "hint": "Oxygen in oxides carries a -2 oxidation state; the compound PbO is neutral.",
                "explanation": "In lead(II) oxide (PbO), oxygen has an oxidation state of -2, so lead has an oxidation state of +2.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Thermal decomposition of lead nitrate yields lead(II) oxide, nitrogen dioxide, and oxygen.",
                    "Step 2: Reaction Mechanism & Stoichiometry: PbO is an electrically neutral ionic compound. The oxide anion is O(2-).",
                    "Step 3: Verification & Real-World Application: To balance O(2-), the lead cation must be Pb(2+), confirming lead(II) oxide."
                ]
            },
            {
                "question": "Which of the following equations accurately depicts the overall equation for photosynthesis?",
                "options": [
                    "6 CO2 + 12 H2O --[Chlorophyll/Sunlight]--> C6H12O6 + 6 O2 + 6 H2O",
                    "CO2 + H2O -> CH4 + O2",
                    "C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O + Energy",
                    "6 CO2 + 6 H2O -> C2H5OH + 2 CO2"
                ],
                "answer": 0,
                "hint": "Photosynthesis uses sunlight and chlorophyll to convert carbon dioxide and water into glucose and oxygen.",
                "explanation": "Photosynthesis is represented by 6 CO2 + 12 H2O --[Sunlight/Chlorophyll]--> C6H12O6 + 6 O2 + 6 H2O, an endothermic photochemical reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Carbon dioxide gas from air and water from soil are absorbed by green plants.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Solar radiant energy captured by chlorophyll drives the reduction of CO2 to glucose: 6 CO2 + 12 H2O -> C6H12O6 + 6 O2 + 6 H2O.",
                    "Step 3: Verification & Real-World Application: This reaction stores solar energy in organic bonds, providing oxygen and food for Earth's biosphere."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Reaction Types Mastery",
        "subtitle": "Mastery Challenge: Combination, Thermal Decomposition, and Exothermic Reactions",
        "speech": "",
        "questions": [
            {
                "question": "Which of the following is the definitive characteristic of all combination reactions?",
                "options": [
                    "Only elemental gases can participate as reactants",
                    "Two or more reactants combine to form exactly one single product",
                    "Heat energy must be continuously absorbed from the environment",
                    "One element displaces another from its aqueous compound"
                ],
                "answer": 1,
                "hint": "Look at the product side: there is always only a single compound formula.",
                "explanation": "A combination reaction is defined by multiple reactants combining to yield a single product (A + B -> AB).",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Examine the general form of combination reactions: A + B -> AB.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Reactant species merge through chemical bond formation. Regardless of the number of reactants, only one distinct product compound forms.",
                    "Step 3: Verification & Real-World Application: Examples include C + O2 -> CO2 and CaO + H2O -> Ca(OH)2, both forming a single product."
                ]
            },
            {
                "question": "What gas causes freshly prepared lime water to turn milky when carbon dioxide is bubbled through it?",
                "options": [
                    "Carbon monoxide (CO)",
                    "Carbon dioxide (CO2)",
                    "Sulphur dioxide (SO2)",
                    "Nitrogen dioxide (NO2)"
                ],
                "answer": 1,
                "hint": "This gas reacts with Ca(OH)2 to precipitate white calcium carbonate.",
                "explanation": "Bubbling CO2 through lime water Ca(OH)2 precipitates insoluble white calcium carbonate (CaCO3), giving the milky appearance.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Lime water is a clear dilute solution of calcium hydroxide, Ca(OH)2(aq).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l). Insoluble CaCO3 precipitates as fine white particles.",
                    "Step 3: Verification & Real-World Application: This milkiness test is the standard laboratory identification test for carbon dioxide gas."
                ]
            },
            {
                "question": "When green ferrous sulphate crystals (FeSO4·7H2O) are heated, what causes the initial colour change from green to white?",
                "options": [
                    "Oxidation of iron to black magnetite",
                    "Loss of water of crystallization",
                    "Sublimation of anhydrous iron salts",
                    "Absorption of ambient atmospheric nitrogen"
                ],
                "answer": 1,
                "hint": "Heating removes the 7 hydrate water molecules bound within the crystal lattice.",
                "explanation": "FeSO4·7H2O crystals lose their seven molecules of water of crystallization upon gentle heating, converting into anhydrous white FeSO4.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Green vitriol crystals have the hydrated chemical formula FeSO4·7H2O.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Gentle heating drives off coordinated water molecules: FeSO4·7H2O(s) --[Heat]--> FeSO4(s) + 7H2O(g).",
                    "Step 3: Verification & Real-World Application: The loss of coordinated water destroys the crystal ligand field, shifting colour from pale green to anhydrous white."
                ]
            },
            {
                "question": "What two gases with the pungent odour of burning sulphur are emitted during strong heating of anhydrous ferrous sulphate?",
                "options": [
                    "H2S and SO2",
                    "SO2 and SO3",
                    "CO2 and SO2",
                    "NO2 and SO3"
                ],
                "answer": 1,
                "hint": "Thermal decomposition of FeSO4 produces sulphur dioxide and sulphur trioxide.",
                "explanation": "2 FeSO4(s) --[Heat]--> Fe2O3(s) + SO2(g) + SO3(g). Both sulphur dioxide and sulphur trioxide are released.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Strong heating of dry FeSO4 causes chemical decomposition of the sulphate anion.",
                    "Step 2: Reaction Mechanism & Stoichiometry: 2 FeSO4(s) -> Fe2O3(s) + SO2(g) + SO3(g). Solid ferric oxide remains while SO2 and SO3 gases evolve.",
                    "Step 3: Verification & Real-World Application: The emitted gases possess the sharp, choking smell of burning sulphur matches."
                ]
            },
            {
                "question": "Why is the decomposition of vegetable matter into compost classified as an exothermic reaction?",
                "options": [
                    "It consumes electrical energy from soil moisture",
                    "Microbial breakdown of organic bonds releases heat into the compost pile",
                    "It requires constant external heating by kerosene burners",
                    "It produces liquid nitrogen that cools the soil"
                ],
                "answer": 1,
                "hint": "Microbial aerobic and anaerobic digestion discharges metabolic heat energy.",
                "explanation": "Microorganisms break down complex organic polymers in vegetable matter into simpler humus, releasing metabolic heat energy in an exothermic process.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Vegetable matter contains cellulose, starch, and organic molecules.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Microbes decompose these organic compounds. Energy released from breaking chemical bonds exceeds activation energy, yielding net thermal output.",
                    "Step 3: Verification & Real-World Application: The core of an active compost heap reaches 50 to 65 °C, directly demonstrating exothermic heat release."
                ]
            },
            {
                "question": "Which of the following reactions is used in the manufacture of cement?",
                "options": [
                    "2 H2 + O2 -> 2 H2O",
                    "CaCO3 --[Heat]--> CaO + CO2",
                    "Zn + CuSO4 -> ZnSO4 + Cu",
                    "2 Na + Cl2 -> 2 NaCl"
                ],
                "answer": 1,
                "hint": "Heating limestone decomposes it into quicklime, the primary binder in cement.",
                "explanation": "Thermal decomposition of limestone (CaCO3 -> CaO + CO2) produces quicklime (CaO), an essential raw material for portland cement.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Natural limestone rock consists predominantly of calcium carbonate, CaCO3.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In industrial rotary kilns at 1000 °C, CaCO3(s) decomposes: CaCO3(s) -> CaO(s) + CO2(g).",
                    "Step 3: Verification & Real-World Application: The resulting solid quicklime (CaO) is ground with silicates and gypsum to manufacture commercial construction cement."
                ]
            },
            {
                "question": "What type of reaction is represented by: C6H12O6(aq) + 6 O2(aq) -> 6 CO2(aq) + 6 H2O(l) + Energy?",
                "options": [
                    "Endothermic decomposition reaction",
                    "Exothermic cellular respiration reaction",
                    "Photochemical synthesis reaction",
                    "Electrolytic cleavage reaction"
                ],
                "answer": 1,
                "hint": "This reaction breaks down glucose in living cells, releasing energy.",
                "explanation": "Cellular respiration oxidizes glucose to release energy, water, and carbon dioxide, making it an exothermic reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Glucose and dissolved oxygen react within mitochondria in cellular cytoplasm.",
                    "Step 2: Reaction Mechanism & Stoichiometry: C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O + 38 ATP (Energy). High-energy C-H bonds oxidize to lower-energy C-O and H-O bonds.",
                    "Step 3: Verification & Real-World Application: The liberated energy maintains mammal body temperature at ~37 °C and powers muscular contractions."
                ]
            },
            {
                "question": "What happens when solid barium hydroxide is mixed with solid ammonium chloride in a flask?",
                "options": [
                    "A vigorous explosion with bright yellow light",
                    "An endothermic reaction where the flask becomes extremely cold",
                    "Instant formation of a black copper coating",
                    "Evolution of dense brown nitrogen dioxide gas"
                ],
                "answer": 1,
                "hint": "This reaction absorbs heat from its surroundings, dropping the flask temperature below 0 °C.",
                "explanation": "Ba(OH)2·8H2O + 2 NH4Cl -> BaCl2 + 2 NH3 + 10 H2O is highly endothermic, absorbing heat and making the flask freezing cold.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid barium hydroxide octahydrate is mixed with solid ammonium chloride.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Ba(OH)2·8H2O(s) + 2NH4Cl(s) -> BaCl2(aq) + 2NH3(g) + 10H2O(l) - Heat. Entropy increase drives endothermic heat absorption.",
                    "Step 3: Verification & Real-World Application: The flask bottom absorbs heat from a wet wooden block beneath it, freezing the water droplet and sticking the flask to the wood."
                ]
            },
            {
                "question": "What is the primary product when coal (carbon) burns completely in excess air?",
                "options": [
                    "Carbon monoxide gas (CO)",
                    "Carbon dioxide gas (CO2)",
                    "Methane gas (CH4)",
                    "Calcium carbonate solid (CaCO3)"
                ],
                "answer": 1,
                "hint": "Complete combustion of carbon with excess oxygen yields carbon dioxide.",
                "explanation": "Complete combustion of carbon in excess air yields carbon dioxide: C(s) + O2(g) -> CO2(g), an exothermic combination reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid carbon (coal) reacts with gaseous oxygen from air.",
                    "Step 2: Reaction Mechanism & Stoichiometry: C(s) + O2(g) -> CO2(g) + Heat. One carbon atom combines with one diatomic oxygen molecule.",
                    "Step 3: Verification & Real-World Application: In excess oxygen, complete combustion forms non-toxic but greenhouse gas CO2 rather than poisonous CO."
                ]
            },
            {
                "question": "Which of the following is an endothermic decomposition reaction?",
                "options": [
                    "Burning of natural gas",
                    "Thermal decomposition of lead nitrate",
                    "Hydration of quicklime",
                    "Respiration in human cells"
                ],
                "answer": 1,
                "hint": "Identify the reaction that requires continuous heat input to split a single reactant.",
                "explanation": "Thermal decomposition of lead nitrate (2 Pb(NO3)2 -> 2 PbO + 4 NO2 + O2) absorbs heat to break bonds, classifying it as an endothermic reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Compare thermal requirements: combustion, hydration of quicklime, and respiration all release heat.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Decomposing lead nitrate requires heat to cleave ionic-covalent bonds: 2Pb(NO3)2 + Heat -> 2PbO + 4NO2 + O2.",
                    "Step 3: Verification & Real-World Application: Because it continuously absorbs thermal energy from the burner, it is strictly endothermic."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Redox Precipitation Review",
        "subtitle": "Mastery Challenge: Displacement, Double Displacement, and Oxidation-Reduction",
        "speech": "",
        "questions": [
            {
                "question": "What happens when an iron nail is left immersed in copper sulphate solution for 20 minutes?",
                "options": [
                    "The nail turns white and the solution turns colourless",
                    "The nail gets coated with reddish-brown copper and the solution turns pale green",
                    "The nail dissolves completely with evolution of hydrogen gas",
                    "No reaction occurs because copper is more reactive than iron"
                ],
                "answer": 1,
                "hint": "Iron displaces copper from CuSO4, forming green FeSO4 and depositing copper metal.",
                "explanation": "Fe(s) + CuSO4(aq) -> FeSO4(aq) + Cu(s). Iron displaces copper, forming green ferrous sulphate and depositing reddish-brown copper on the nail.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid iron (Fe) is placed in blue aqueous copper sulphate (CuSO4).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Iron has a lower standard reduction potential than copper and oxidizes to Fe(2+), while Cu(2+) reduces to metallic copper: Fe + Cu(2+) -> Fe(2+) + Cu.",
                    "Step 3: Verification & Real-World Application: The solution colour shifts from deep blue (Cu(2+)) to pale green (Fe(2+)), with brown copper plating on the nail."
                ]
            },
            {
                "question": "In the reaction: ZnO + C -> Zn + CO, which substance acts as the reducing agent?",
                "options": [
                    "Zinc oxide (ZnO)",
                    "Carbon (C)",
                    "Zinc metal (Zn)",
                    "Carbon monoxide (CO)"
                ],
                "answer": 1,
                "hint": "The reducing agent undergoes oxidation by gaining oxygen or losing electrons.",
                "explanation": "Carbon gains oxygen from ZnO to form CO (it is oxidised), which means carbon acts as the reducing agent.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Zinc oxide reacts with elemental carbon: ZnO + C -> Zn + CO.",
                    "Step 2: Reaction Mechanism & Stoichiometry: ZnO loses oxygen to form Zn (reduction). Carbon gains oxygen to form CO (oxidation).",
                    "Step 3: Verification & Real-World Application: The substance that undergoes oxidation (Carbon) acts as the reducing agent, reducing ZnO to zinc metal."
                ]
            },
            {
                "question": "What is the precipitate formed when aqueous sodium sulphate reacts with aqueous barium chloride in Activity 1.10?",
                "options": [
                    "Sodium chloride precipitate",
                    "Barium sulphate white precipitate",
                    "Barium chloride precipitate",
                    "Sodium oxide precipitate"
                ],
                "answer": 1,
                "hint": "Barium ions combine with sulphate ions to form an insoluble white solid.",
                "explanation": "Na2SO4(aq) + BaCl2(aq) -> BaSO4(s) + 2 NaCl(aq). Insoluble white barium sulphate precipitates immediately.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Aqueous Na2SO4 supplies Na+ and SO4(2-) ions; aqueous BaCl2 supplies Ba(2+) and Cl- ions.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Ba(2+) and SO4(2-) have high lattice energy, forming insoluble white BaSO4 solid: Ba(2+) + SO4(2-) -> BaSO4(s).",
                    "Step 3: Verification & Real-World Application: The white precipitate confirms double displacement and is used in gravimetric sulphate analysis."
                ]
            },
            {
                "question": "In the reaction MnO2 + 4 HCl -> MnCl2 + 2 H2O + Cl2, which species is oxidised?",
                "options": [
                    "MnO2",
                    "HCl",
                    "MnCl2",
                    "H2O"
                ],
                "answer": 1,
                "hint": "HCl loses hydrogen (chloride ions lose electrons to form chlorine gas).",
                "explanation": "In HCl, chlorine has an oxidation state of -1 and is oxidised to 0 in Cl2 gas. Thus, HCl is oxidised by MnO2.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: MnO2 reacts with concentrated hydrochloric acid: MnO2 + 4HCl -> MnCl2 + 2H2O + Cl2.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Mn changes from +4 in MnO2 to +2 in MnCl2 (reduction). Cl changes from -1 in HCl to 0 in Cl2 (oxidation).",
                    "Step 3: Verification & Real-World Application: Because HCl loses hydrogen and electrons to form elemental chlorine, HCl is the oxidised species."
                ]
            },
            {
                "question": "What happens when hydrogen gas is passed over heated black copper(II) oxide in Activity 1.11?",
                "options": [
                    "The black coating dissolves into a blue solution",
                    "The black coating turns reddish-brown as copper metal is regenerated",
                    "A violent explosion producing metallic zinc",
                    "The copper oxide sublimates into colourless gas"
                ],
                "answer": 1,
                "hint": "Hydrogen reduces black CuO back to reddish-brown elemental copper.",
                "explanation": "CuO(s) + H2(g) --[Heat]--> Cu(s) + H2O(g). Hydrogen removes oxygen from black CuO, restoring lustrous brown copper metal.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid black copper(II) oxide (CuO) is heated in a stream of hydrogen gas (H2).",
                    "Step 2: Reaction Mechanism & Stoichiometry: CuO + H2 -> Cu + H2O. CuO loses oxygen (reduced to Cu); H2 gains oxygen (oxidised to H2O).",
                    "Step 3: Verification & Real-World Application: The colour shifts from dull black back to shiny reddish-brown copper, demonstrating reversible redox chemistry."
                ]
            },
            {
                "question": "Which of the following displacement reactions will NOT proceed spontaneously?",
                "options": [
                    "Fe + CuSO4 -> FeSO4 + Cu",
                    "Zn + CuSO4 -> ZnSO4 + Cu",
                    "Cu + FeSO4 -> CuSO4 + Fe",
                    "Pb + CuCl2 -> PbCl2 + Cu"
                ],
                "answer": 2,
                "hint": "Copper is lower than iron in the reactivity series and cannot displace iron.",
                "explanation": "Copper is less chemically reactive than iron. Therefore, copper cannot displace iron from ferrous sulphate solution: Cu + FeSO4 -> No reaction.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Consult the metal reactivity series: Zn > Fe > Pb > H > Cu > Ag > Au.",
                    "Step 2: Reaction Mechanism & Stoichiometry: A metal can only displace ions of metals positioned below it in the activity series.",
                    "Step 3: Verification & Real-World Application: Copper is below iron; hence Cu cannot reduce Fe(2+) ions, and no reaction takes place."
                ]
            },
            {
                "question": "During the electrolysis of water (Activity 1.7), what gas collects at the anode?",
                "options": [
                    "Hydrogen gas",
                    "Oxygen gas",
                    "Nitrogen gas",
                    "Chlorine gas"
                ],
                "answer": 1,
                "hint": "The anode is the positive electrode where oxidation of water liberates oxygen.",
                "explanation": "At the positive anode, water oxidation releases oxygen gas: 2 H2O -> O2 + 4 H+ + 4 e-. Thus, oxygen collects at the anode.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Water electrolysis in a 6V DC cell involves two half-cell reactions.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Anode (positive): 2 H2O(l) -> O2(g) + 4 H+(aq) + 4 e-. Cathode (negative): 4 H+(aq) + 4 e- -> 2 H2(g).",
                    "Step 3: Verification & Real-World Application: Oxygen gas collects at the anode in a 1:2 volume ratio relative to hydrogen at the cathode."
                ]
            },
            {
                "question": "Why is the reaction between lead nitrate and potassium iodide classified as double displacement?",
                "options": [
                    "Lead metal displaces potassium from the solution",
                    "There is a mutual exchange of cations and anions between the two salts",
                    "Potassium loses electrons to atmospheric oxygen",
                    "Both reactants decompose thermally into elemental powders"
                ],
                "answer": 1,
                "hint": "Pb(2+) pairs with I(-) and K(+) pairs with NO3(-).",
                "explanation": "Pb(NO3)2(aq) + 2 KI(aq) -> PbI2(s) + 2 KNO3(aq) involves a mutual exchange of ions between the two compounds, defining double displacement.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Reactants are aqueous solutions of lead nitrate and potassium iodide.",
                    "Step 2: Reaction Mechanism & Stoichiometry: The lead cation (Pb(2+)) exchanges its nitrate partner for iodide (I-), precipitating yellow PbI2, while potassium retains nitrate as KNO3.",
                    "Step 3: Verification & Real-World Application: Because both salts swap ion partners mutually, it is an authentic double displacement precipitation reaction."
                ]
            },
            {
                "question": "What is the role of sunlight in the photolysis of silver bromide in black-and-white photography?",
                "options": [
                    "It acts as a physical catalyst without energy transfer",
                    "It provides radiant photon energy to cleave the ionic bond between silver and bromine",
                    "It oxidizes bromine gas into bromate ions",
                    "It dissolves silver bromide into an aqueous solution"
                ],
                "answer": 1,
                "hint": "Photons provide the activation energy required to break the Ag-Br bond.",
                "explanation": "Sunlight photons carry activation energy that causes photolytic cleavage (2 AgBr -> 2 Ag + Br2), liberating grey metallic silver on the photographic film.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Light-sensitive silver bromide crystals are embedded in photographic gelatin emulsion.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Photons absorb into the crystal lattice, exciting electrons: 2 AgBr(s) --[hν]--> 2 Ag(s) + Br2(g).",
                    "Step 3: Verification & Real-World Application: The resulting clusters of metallic silver form the latent black-and-white photographic image."
                ]
            },
            {
                "question": "Which of the following defines a redox reaction accurately?",
                "options": [
                    "A reaction where only oxidation occurs while reduction is absent",
                    "A reaction where oxidation and reduction occur simultaneously",
                    "A reaction where precipitates dissolve in distilled water",
                    "A reaction where physical states remain unchanged throughout"
                ],
                "answer": 1,
                "hint": "Electrons or oxygen atoms transferred must come from one species and be received by another.",
                "explanation": "A redox reaction is an oxidation-reduction reaction in which one reactant is oxidised while another is simultaneously reduced.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Oxidation involves loss of electrons (or gain of oxygen); reduction involves gain of electrons (or loss of oxygen).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Free electrons cannot exist independently in solution; any electrons lost by the reducing agent must be gained by the oxidising agent.",
                    "Step 3: Verification & Real-World Application: Hence, oxidation and reduction are inseparable halves of a unified redox transformation."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Everyday Chemical Transformations",
        "subtitle": "Mastery Challenge: Corrosion, Rancidity, and Real-World Chemical Applications",
        "speech": "",
        "questions": [
            {
                "question": "What chemical conditions are strictly necessary for the rusting of iron?",
                "options": [
                    "Presence of pure nitrogen and dry carbon dioxide",
                    "Simultaneous presence of both oxygen and moisture (water)",
                    "Exposure to vacuum and intense ultraviolet sunlight",
                    "Presence of inert argon gas at high pressure"
                ],
                "answer": 1,
                "hint": "Iron does not rust in boiled dry water or in dry oxygen alone.",
                "explanation": "Rusting of iron requires both oxygen and moisture simultaneously (4 Fe + 3 O2 + 2x H2O -> 2 Fe2O3·xH2O).",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Metallic iron reacts with atmospheric components to form hydrated ferric oxide rust.",
                    "Step 2: Reaction Mechanism & Stoichiometry: An electrochemical corrosion cell forms on the iron surface. Iron oxidizes at anodic sites only when dissolved oxygen and liquid water films coexist.",
                    "Step 3: Verification & Real-World Application: Sealed test tubes with anhydrous calcium chloride (dry air) or boiled water sealed with oil (no oxygen) show zero rusting."
                ]
            },
            {
                "question": "What is the chemical composition of the black tarnish that forms on silver articles exposed to air?",
                "options": [
                    "Silver oxide (Ag2O)",
                    "Silver sulphide (Ag2S)",
                    "Silver carbonate (Ag2CO3)",
                    "Silver chloride (AgCl)"
                ],
                "answer": 1,
                "hint": "Silver reacts with trace hydrogen sulphide gas present in polluted air.",
                "explanation": "Silver reacts with trace atmospheric hydrogen sulphide (H2S) in air to form a black surface coating of silver sulphide: 2 Ag + H2S -> Ag2S + H2.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Silver ornaments and utensils gradually darken when worn or stored in urban atmospheres.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Trace H2S from decaying organic matter reacts with silver: 4 Ag(s) + 2 H2S(g) + O2(g) -> 2 Ag2S(s) + 2 H2O(l).",
                    "Step 3: Verification & Real-World Application: The black surface layer is silver sulphide (Ag2S), which can be chemically reduced back to lustrous silver in an aluminium foil and baking soda bath."
                ]
            },
            {
                "question": "What chemical formula best represents the green coating (patina) formed on corroded copper vessels?",
                "options": [
                    "CuSO4·5H2O",
                    "CuCO3·Cu(OH)2",
                    "CuO",
                    "CuCl2"
                ],
                "answer": 1,
                "hint": "Basic copper carbonate formed by reaction with moist carbon dioxide and oxygen.",
                "explanation": "Copper reacts with moist atmospheric carbon dioxide and oxygen to form basic copper carbonate, CuCO3·Cu(OH)2, appearing as a green patina.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Copper vessels exposed to humid air develop a dull green surface patina over years.",
                    "Step 2: Reaction Mechanism & Stoichiometry: 2 Cu(s) + H2O(l) + CO2(g) + O2(g) -> CuCO3·Cu(OH)2(s). The compound is an equimolar combination of copper carbonate and copper hydroxide.",
                    "Step 3: Verification & Real-World Application: Cleaning copper vessels with acidic lemon juice (citric acid) dissolves basic copper carbonate, restoring shiny copper."
                ]
            },
            {
                "question": "What is rancidity in food science?",
                "options": [
                    "Crystallization of sugar in sweet confectionery",
                    "Oxidation of fats and oils leading to unpleasant odour and foul taste",
                    "Fermentation of fruit juices into vinegar",
                    "Loss of moisture from fresh bread crusts"
                ],
                "answer": 1,
                "hint": "Lipids in fried snacks react with atmospheric oxygen over time.",
                "explanation": "Rancidity is the oxidation of unsaturated fats and oils in food materials, producing foul-smelling volatile aldehydes and acids.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Fried snacks and edible oils contain unsaturated fatty acid chains.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Atmospheric oxygen attacks double bonds via free-radical autoxidation, generating peroxides that decompose into foul-smelling short-chain aldehydes and ketones.",
                    "Step 3: Verification & Real-World Application: Rancid food exhibits an offensive stale smell and bitter taste, making it unpalatable and potentially toxic."
                ]
            },
            {
                "question": "Which of the following is NOT an effective method for preventing rancidity in oily foods?",
                "options": [
                    "Storing food in airtight containers",
                    "Flushing packaging with inert nitrogen gas",
                    "Adding synthetic antioxidants such as BHA and BHT",
                    "Storing food exposed to open sunlight and warm humid air"
                ],
                "answer": 3,
                "hint": "Warmth and sunlight accelerate lipid oxidation reactions.",
                "explanation": "Exposing food to sunlight and warm humid air accelerates lipid oxidation and rancidity, whereas airtight containers, nitrogen flushing, and antioxidants prevent it.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Identify environmental factors that accelerate versus inhibit chemical oxidation.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Light (photons) and heat provide activation energy that accelerates free-radical lipid oxidation.",
                    "Step 3: Verification & Real-World Application: Leaving oily snacks exposed to warm sunny air drastically speeds up rancidity, making it an adverse condition."
                ]
            },
            {
                "question": "Why is nitrogen gas chosen to flush bags of potato chips rather than oxygen or air?",
                "options": [
                    "Nitrogen reacts with potato starch to increase crispness",
                    "Nitrogen is an unreactive inert gas that displaces oxygen and halts lipid oxidation",
                    "Nitrogen provides a sweet aroma when the bag is opened",
                    "Nitrogen acts as an acidic preservative that lowers package pH"
                ],
                "answer": 1,
                "hint": "Nitrogen has a strong N≡N triple bond, making it chemically inert under ambient conditions.",
                "explanation": "Nitrogen is chemically inert at room temperature. Flushing chip bags with nitrogen displaces oxygen, preventing oxidation of oils and maintaining freshness.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Potato chips are deep-fried in vegetable oils rich in unsaturated fats.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Oxygen in ambient air initiates oxidative rancidity. Nitrogen possesses a stable triple bond (N≡N) and does not react with lipids.",
                    "Step 3: Verification & Real-World Application: Nitrogen cushion packaging prevents both chemical spoiling (rancidity) and physical crushing during transit."
                ]
            },
            {
                "question": "In a laboratory group experiment, dissolving ammonium nitrate in water causes the beaker temperature to drop sharply. How is this reaction classified?",
                "options": [
                    "Exothermic combination reaction",
                    "Endothermic dissolution process",
                    "Photolytic cleavage reaction",
                    "Electrolytic oxidation reaction"
                ],
                "answer": 1,
                "hint": "A drop in temperature indicates absorption of thermal energy from the surroundings.",
                "explanation": "When ammonium nitrate dissolves, it absorbs heat from the surrounding water, causing a temperature drop that defines an endothermic process.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid NH4NO3 crystals dissolve in water solvent.",
                    "Step 2: Reaction Mechanism & Stoichiometry: NH4NO3(s) + Heat -> NH4+(aq) + NO3-(aq). The lattice energy required to separate ions exceeds hydration energy released.",
                    "Step 3: Verification & Real-World Application: The deficit in energy is extracted from water thermal vibrations, cooling the beaker; this is the basis of instant medical ice packs."
                ]
            },
            {
                "question": "Why does whitewashing with slaked lime require 2 to 3 days to develop its full sparkling white sheen?",
                "options": [
                    "Slaked lime takes three days to dry by pure evaporation of water",
                    "Calcium hydroxide reacts gradually with atmospheric carbon dioxide to form a hard calcium carbonate layer",
                    "Slaked lime must absorb ultraviolet radiation from sunlight to turn white",
                    "Bacteria must decompose the slaked lime into calcium metal"
                ],
                "answer": 1,
                "hint": "The chemical reaction Ca(OH)2 + CO2 -> CaCO3 + H2O depends on diffusion of trace atmospheric CO2.",
                "explanation": "Atmospheric carbon dioxide is present in trace amounts (0.04%). Slaked lime Ca(OH)2 absorbs it slowly over 2-3 days, converting into shiny crystalline CaCO3.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Wet slaked lime paste Ca(OH)2 is painted onto porous brick or plaster walls.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Ca(OH)2(s) + CO2(g) -> CaCO3(s) + H2O(l). Gaseous CO2 must diffuse into the thin wet coating to react.",
                    "Step 3: Verification & Real-World Application: Because atmospheric CO2 is only ~400 ppm, complete carbonation takes 48 to 72 hours, producing a hard, gleaming marble-like finish."
                ]
            },
            {
                "question": "Which of the following processes involves BOTH a combination reaction AND an exothermic reaction?",
                "options": [
                    "Heating of limestone in a cement kiln",
                    "Electrolysis of acidified water in an electrolytic cell",
                    "Hydration of quicklime to form slaked lime",
                    "Photolysis of silver chloride in sunlight"
                ],
                "answer": 2,
                "hint": "CaO + H2O -> Ca(OH)2 releases intense heat while combining two reactants into one.",
                "explanation": "CaO(s) + H2O(l) -> Ca(OH)2(aq) + Heat combines two reactants into a single product while releasing large amounts of heat, satisfying both definitions.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Evaluate candidate reactions for two criteria: single product (combination) and heat release (exothermic).",
                    "Step 2: Reaction Mechanism & Stoichiometry: CaO + H2O -> Ca(OH)2 yields only one product (combination). The reaction boils water and releases heat (exothermic).",
                    "Step 3: Verification & Real-World Application: The other choices are all decomposition reactions that absorb energy (endothermic)."
                ]
            },
            {
                "question": "What is the primary industrial consequence of metallic corrosion across modern infrastructure?",
                "options": [
                    "Immediate transmutation of base metals into precious gold",
                    "Severe structural deterioration of bridges, ships, pipelines, and railings requiring costly repairs",
                    "Permanent loss of Earth's atmospheric nitrogen gas",
                    "Uncontrolled cooling of industrial chemical plants"
                ],
                "answer": 1,
                "hint": "Corrosion weakens load-bearing steel and iron structures globally.",
                "explanation": "Corrosion causes immense economic and structural damage to steel bridges, ships, underground oil pipelines, and railings, necessitating massive replacement costs.",
                "solution_steps": [
                    "Step 1: Chemical Equation & Reactants Analysis: Iron and structural steels oxidize in moist outdoor environments.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Unlike aluminum oxide which forms a protective passive layer, iron rust flakes off, exposing underlying metal to continuous destruction.",
                    "Step 3: Verification & Real-World Application: Rust weakens load-bearing cross-sections, creating hazardous bridge collapses and pipe leaks, costing billions annually in galvanization and cathodic protection."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    for s in slides_part3:
        twc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) - Questions: {len(s['questions'])}")
        assert 1 <= twc <= 3, f"Title length out of bounds: {twc}"
        assert s["speech"] == "", f"Speech must be silent on slide {s['id']}"
        assert len(s["questions"]) == 10, f"Slide {s['id']} must have exactly 10 questions"
        for qidx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4, f"Slide {s['id']} question {qidx+1} must have 4 options"
            assert "hint" in q, f"Slide {s['id']} question {qidx+1} missing hint"
            assert "explanation" in q, f"Slide {s['id']} question {qidx+1} missing explanation"
            assert len(q["solution_steps"]) == 3, f"Slide {s['id']} question {qidx+1} must have 3 solution steps"
    print("Part 3 verification: ALL PASSED!")

"""Generate Slides 17 to 20 (Review Exercises) for Class 10 Science Chapter 2: Acids, Bases and Salts
Strict constraints:
- Title: strictly 1 to 3 words
- Speech: strictly "" (silent)
- 10 comprehensive review questions per slide (40 total)
- 4 options per question, correct answer index, hint, explanation, and 3-step structured solution
"""

slides = [
    {
        "id": 17,
        "title": "Indicators Neutralisation Review",
        "subtitle": "Diagnostic Indicators, Metal Reactions, Carbonate Effervescence, and Neutralisation",
        "speech": "",
        "content": {
            "concept": "Mastery challenge covering natural and synthetic indicators, olfactory testing, acid reactions with metals, decomposition of carbonates and hydrogencarbonates, and mutual neutralisation.",
            "formula": "\\text{Acid} + \\text{Base} \\rightarrow \\text{Salt} + \\text{Water} \\quad | \\quad \\text{Acid} + \\text{Carbonate} \\rightarrow \\text{Salt} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}",
            "points": [
                "Litmus turns red in acid and blue in base; turmeric turns reddish-brown in base.",
                "Phenolphthalein is pink in base and colourless in acid; methyl orange is red in acid and yellow in base.",
                "Olfactory indicators (onion, vanilla, clove) retain aroma in acids and lose it in bases.",
                "Active metals release hydrogen gas with acids, producing a characteristic pop sound.",
                "Carbonates release CO2 turning lime water milky; excess CO2 dissolves precipitate to clear Ca(HCO3)2."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "A student is given three test tubes containing distilled water, an acidic solution, and a basic solution respectively, but only red litmus paper is provided. How can all three liquids be definitively identified?",
                "options": [
                    "Dip the paper in all tubes; the tube that turns it blue is basic. Then use that blue paper to find the acid (turns red) and water (no change).",
                    "Red litmus turns green in distilled water, yellow in acid, and blue in base directly in one step.",
                    "Red litmus bleaches white in distilled water and turns black in acidic solutions.",
                    "It is chemically impossible to identify three liquids using only red litmus paper."
                ],
                "answer": 0,
                "hint": "Base turns red litmus blue. That newly created blue paper can then test the remaining two tubes.",
                "explanation": "Dipping red litmus into the basic solution turns it blue. This blue paper is then dipped into the other two: the acidic solution turns it back to red, while distilled water causes no colour change.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Base + Red Litmus -> Blue color. Acid + Blue Litmus -> Red color. Neutral Water + Litmus -> No color change.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Test each tube with red litmus. Only the basic tube contains OH- ions capable of deprotonating the indicator dye to turn it blue.",
                    "Step 3: Verification & Real-World Application: Using the converted blue litmus paper, test the remaining two tubes. The tube turning it red is the acid, and the tube causing no change is distilled water."
                ]
            },
            {
                "id": 2,
                "question": "Which of the following substances behaves as an olfactory indicator by losing its characteristic smell in a basic solution?",
                "options": [
                    "Turmeric extract",
                    "Phenolphthalein",
                    "Vanilla essence",
                    "Methyl orange"
                ],
                "answer": 2,
                "hint": "Olfactory indicators change or lose their odour depending on acidic or basic media.",
                "explanation": "Vanilla essence, finely chopped onion, and clove oil are olfactory indicators. In alkaline solutions like NaOH, their volatile aromatic aldehydes react and lose their characteristic scent.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Olfactory indicators possess volatile organic scent molecules sensitive to alkaline deprotonation.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In acidic medium (dilute HCl), the aroma of vanilla essence persists unchanged. In basic medium (dilute NaOH), the scent is completely destroyed.",
                    "Step 3: Verification & Real-World Application: Olfactory indicators enable visually impaired students to conduct reliable acid-base diagnostic testing."
                ]
            },
            {
                "id": 3,
                "question": "When granulated zinc is treated with dilute sulphuric acid, a gas is evolved. What happens when this gas is passed through soap solution and ignited?",
                "options": [
                    "Soap bubbles sink rapidly and extinguish the flame silently",
                    "Soap bubbles filled with hydrogen gas float and burn with a characteristic pop sound",
                    "The gas turns the soap solution into a milky white precipitate",
                    "The gas rekindles a glowing wooden splinter into a bright flame"
                ],
                "answer": 1,
                "hint": "Hydrogen gas is lighter than air and combustible.",
                "explanation": "The reaction Zn + H2SO4 -> ZnSO4 + H2(g) evolves hydrogen gas. Trapped inside soap bubbles, hydrogen rises and burns rapidly with oxygen, making a diagnostic 'pop' sound.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Zn(s) + H2SO4(aq) -> ZnSO4(aq) + H2(g)^.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Zinc oxidises from oxidation state 0 to +2, reducing protons (2H+) to diatomic hydrogen gas molecules.",
                    "Step 3: Verification & Real-World Application: Igniting trapped H2 bubbles: 2H2(g) + O2(g) -> 2H2O(g) + Energy, producing a localized rapid miniature shockwave heard as a 'pop'."
                ]
            },
            {
                "id": 4,
                "question": "What is the balanced equation and product formed when granulated zinc metal is heated with concentrated sodium hydroxide solution?",
                "options": [
                    "Zn + NaOH -> ZnO + NaH",
                    "Zn + 2NaOH -> Na2ZnO2 + H2",
                    "2Zn + 2NaOH -> 2NaZnO + H2O",
                    "Zn + 4NaOH -> Na4ZnO4 + 2H2"
                ],
                "answer": 1,
                "hint": "Zinc is an amphoteric metal that forms sodium zincate: Na2ZnO2.",
                "explanation": "Active amphoteric metals like zinc react with hot alkalis: Zn(s) + 2NaOH(aq) -> Na2ZnO2(aq) (sodium zincate) + H2(g).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Zn(s) + 2NaOH(aq) -heat-> Na2ZnO2(aq) + H2(g)^.",
                    "Step 2: Reaction Mechanism & Stoichiometry: 1 mole of solid zinc reacts with 2 moles of sodium hydroxide to yield 1 mole of sodium zincate and 1 mole of hydrogen gas.",
                    "Step 3: Verification & Real-World Application: Not all metals react with bases; only amphoteric metals like zinc and aluminium displace hydrogen from strong alkalis."
                ]
            },
            {
                "id": 5,
                "question": "Eggshells are crushed and reacted with dilute hydrochloric acid. A gas is evolved that turns lime water milky. What is the major chemical constituent of eggshells?",
                "options": [
                    "Calcium sulphate (CaSO4)",
                    "Calcium carbonate (CaCO3)",
                    "Calcium oxide (CaO)",
                    "Sodium hydrogencarbonate (NaHCO3)"
                ],
                "answer": 1,
                "hint": "Eggshells, limestone, chalk, and marble are all composed of the same calcium salt.",
                "explanation": "Eggshells consist primarily of calcium carbonate (CaCO3). Reaction with HCl produces carbon dioxide: CaCO3 + 2HCl -> CaCl2 + H2O + CO2(g), which turns lime water milky.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g)^.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Carbonate ions (CO3 2-) are protonated by acid to form unstable carbonic acid, which decomposes immediately into water and CO2 gas.",
                    "Step 3: Verification & Real-World Application: The evolved CO2 gas passes into Ca(OH)2 lime water to precipitate insoluble CaCO3, turning the solution milky."
                ]
            },
            {
                "id": 6,
                "question": "What chemical change explains why lime water turns milky when carbon dioxide is bubbled through it, but becomes clear again upon passing excess gas?",
                "options": [
                    "Insoluble CaCO3 forms first, which converts into water-soluble Ca(HCO3)2 with excess CO2",
                    "Calcium oxide dissolves into calcium hydroxide and subsequently boils off into steam",
                    "Calcium chloride precipitates initially and then dissolves in acidic carbon dioxide",
                    "Carbon dioxide bleaches the lime water solution irreversibly"
                ],
                "answer": 0,
                "hint": "Excess CO2 converts the white carbonate precipitate into soluble hydrogencarbonate.",
                "explanation": "Initial reaction: Ca(OH)2 + CO2 -> CaCO3(s) [milky] + H2O. Excess CO2: CaCO3 + H2O + CO2 -> Ca(HCO3)2(aq) [clear soluble calcium hydrogencarbonate].",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Stage 1: Ca(OH)2 + CO2 -> CaCO3v (white precipitate) + H2O. Stage 2: CaCO3 + H2O + CO2 -> Ca(HCO3)2 (soluble).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Insoluble calcium carbonate reacts with dissolved carbonic acid (H2O + CO2) to form soluble calcium and bicarbonate ions.",
                    "Step 3: Verification & Real-World Application: This chemical dissolution process is responsible for the natural carving of limestone caves and sinkholes worldwide."
                ]
            },
            {
                "id": 7,
                "question": "In Activity 2.6, phenolphthalein is added to sodium hydroxide solution, turning it pink. Dilute hydrochloric acid is added until the colour disappears. What happens when a few drops of sodium hydroxide are added again?",
                "options": [
                    "A dense white precipitate forms immediately",
                    "The solution turns brilliant yellow",
                    "The vibrant pink colour reappears",
                    "The solution boils and evolves chlorine gas"
                ],
                "answer": 2,
                "hint": "Phenolphthalein turns pink in the presence of excess hydroxide ions.",
                "explanation": "Phenolphthalein is a reversible indicator. Adding excess NaOH restores alkaline OH- ions, shifting the indicator equilibrium back to its pink conjugate base form.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: HIn(aq) [Colorless] + OH-(aq) <=> In-(aq) [Pink] + H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Adding acid removes OH- ions, shifting equilibrium to colorless HIn. Re-adding base introduces OH-, restoring pink In-.",
                    "Step 3: Verification & Real-World Application: Demonstrates the dynamic reversibility of acid-base indicators used in quantitative volumetric titrations."
                ]
            },
            {
                "id": 8,
                "question": "Black copper(II) oxide powder dissolves in dilute hydrochloric acid to yield a clear blue-green solution. What does this reaction establish about the chemical nature of metallic oxides?",
                "options": [
                    "Metallic oxides are acidic in nature because they turn blue-green",
                    "Metallic oxides are basic in nature because they react with acids to form salt and water",
                    "Metallic oxides are strictly neutral and do not undergo chemical reaction",
                    "Metallic oxides behave exclusively as oxidizing gases"
                ],
                "answer": 1,
                "hint": "Metal oxide + Acid -> Salt + Water, perfectly paralleling Base + Acid -> Salt + Water.",
                "explanation": "CuO(s) + 2HCl(aq) -> CuCl2(aq) [blue-green] + H2O(l). Because metallic oxides neutralize acids to produce an ionic salt and water, they are classified as basic oxides.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CuO(s) [Black] + 2HCl(aq) -> CuCl2(aq) [Blue-Green] + H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Oxide ions (O 2-) in the copper oxide lattice accept protons from hydrochloric acid to synthesize neutral water molecules.",
                    "Step 3: Verification & Real-World Application: The formation of salt and water mirrors standard neutralisation, confirming that metallic oxides act as chemical bases."
                ]
            },
            {
                "id": 9,
                "question": "Why does carbon dioxide react with calcium hydroxide (lime water) to produce calcium carbonate salt and water?",
                "options": [
                    "Because non-metallic oxides are acidic in nature",
                    "Because carbon dioxide acts as a powerful reducing metal",
                    "Because calcium hydroxide is an acidic solution",
                    "Because both compounds are strong mineral alkalis"
                ],
                "answer": 0,
                "hint": "Non-metal oxide + Base -> Salt + Water.",
                "explanation": "CO2(g) + Ca(OH)2(aq) -> CaCO3(s) + H2O(l). The reaction of a non-metallic oxide with a base to yield salt and water proves that non-metallic oxides are acidic oxides.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CO2(g) [Non-metal oxide] + Ca(OH)2(aq) [Base] -> CaCO3(s) [Salt] + H2O(l) [Water].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Dissolved CO2 forms weak carbonic acid in water, which donates protons to hydroxide ions of the base.",
                    "Step 3: Verification & Real-World Application: Confirms the fundamental periodic rule: metallic oxides are basic, whereas non-metallic oxides are acidic."
                ]
            },
            {
                "id": 10,
                "question": "Which of the following represents the correct net ionic equation for the reaction between dilute nitric acid and potassium hydroxide solution?",
                "options": [
                    "K+(aq) + NO3-(aq) -> KNO3(s)",
                    "H+(aq) + OH-(aq) -> H2O(l)",
                    "2H+(aq) + O2-(aq) -> H2O(l)",
                    "KOH(aq) + HNO3(aq) -> KNO3(aq) + H2O(l)"
                ],
                "answer": 1,
                "hint": "The spectator ions K+ and NO3- cancel out from both sides of the complete ionic equation.",
                "explanation": "In any strong acid-strong base neutralization in water, the spectator ions (K+ and NO3-) remain dissolved, leaving the net ionic reaction: H+(aq) + OH-(aq) -> H2O(l).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Molecular: HNO3(aq) + KOH(aq) -> KNO3(aq) + H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Complete ionic: H+(aq) + NO3-(aq) + K+(aq) + OH-(aq) -> K+(aq) + NO3-(aq) + H2O(l). Spectator ions K+ and NO3- cancel out.",
                    "Step 3: Verification & Real-World Application: The net ionic equation H+(aq) + OH-(aq) -> H2O(l) represents the universal proton-transfer core of aqueous acid-base reactions."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Aqueous Dissociation Review",
        "subtitle": "Electrolytic Conduction, Water-Assisted Ionisation, Dilution Safety, and pH Scale",
        "speech": "",
        "content": {
            "concept": "Mastery challenge covering electrolytic conductivity of acids versus organic non-electrolytes, the necessity of water for proton release, hydronium formation, acid dilution thermodynamics, and the mathematical pH scale.",
            "formula": "\\text{pH} = -\\log_{10}[\\text{H}^+] \\quad | \\quad \\text{HCl} + \\text{H}_2\\text{O} \\rightarrow \\text{H}_3\\text{O}^+ + \\text{Cl}^- \\quad | \\quad [\\text{H}^+][\\text{OH}^-] = 10^{-14}",
            "points": [
                "Acids conduct electricity via mobile ions; glucose and alcohol contain hydrogen but do not ionise.",
                "Dry HCl gas does not affect dry litmus; water is mandatory to generate hydronium ions (H3O+).",
                "Alkalis are water-soluble bases producing hydroxide ions (OH-).",
                "Dilution of concentrated acids is highly exothermic: always add acid slowly to water.",
                "pH scale ranges from 0 to 14: pH < 7 is acidic, pH = 7 is neutral, pH > 7 is basic."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "Why does an aqueous solution of alcohol or glucose fail to conduct electricity in Activity 2.8, even though both contain hydrogen in their formulas?",
                "options": [
                    "Alcohol and glucose molecules do not dissociate into free ions in aqueous solution",
                    "Alcohol reacts with the iron electrodes to form an impenetrable insulating coating",
                    "Glucose molecules neutralize all water molecules into dry crystals",
                    "The 6-volt battery does not supply enough alternating current"
                ],
                "answer": 0,
                "hint": "Conduction through liquids requires mobile charged ions, not neutral covalent molecules.",
                "explanation": "Glucose (C6H12O6) and ethanol (C2H5OH) form covalent bonds that do not ionise in water. Without free mobile cations or anions to transport charge, the solution is non-conducting.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: C6H12O6(s) + H2O(l) -> C6H12O6(aq) (intact covalent molecules, zero ions).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Electrolytic current conduction requires mobile charge carriers. In contrast to mineral acids, glucose releases no H+ or H3O+ ions.",
                    "Step 3: Verification & Real-World Application: Proves that the presence of hydrogen atoms in a molecular formula does not classify a substance as an acid."
                ]
            },
            {
                "id": 2,
                "question": "In Activity 2.9, why does dry hydrogen chloride gas fail to change the colour of dry blue litmus paper, but turns moist blue litmus paper red?",
                "options": [
                    "Hydrogen chloride gas only dissociates to generate hydrogen ions in the presence of water",
                    "Dry litmus paper contains an impermeable plastic wax coating",
                    "Water acts as a bleaching agent that changes the paper colour to red",
                    "Chlorine gas is only absorbed by dry litmus paper"
                ],
                "answer": 0,
                "hint": "Polar water molecules are strictly required to pull protons away from covalent HCl molecules.",
                "explanation": "HCl gas is a covalent molecule that only ionises in the presence of water: HCl + H2O -> H3O+ + Cl-. Dry litmus has no water, so no hydronium ions are formed to induce a colour change.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: HCl(g) + H2O(l) -> H3O+(aq) + Cl-(aq). Without H2O, no ionization occurs.",
                    "Step 2: Reaction Mechanism & Stoichiometry: The high polarity of water molecules facilitates the heterolytic cleavage of the H-Cl bond, solvating the liberated proton into a hydronium ion.",
                    "Step 3: Verification & Real-World Application: Confirms that acidic properties emerge strictly in aqueous media where hydronium ions can exist."
                ]
            },
            {
                "id": 3,
                "question": "Why can an isolated hydrogen ion (H+) not exist independently in an aqueous solution?",
                "options": [
                    "A bare proton has an extremely high charge-to-size ratio and spontaneously binds to polar water as H3O+",
                    "Hydrogen ions immediately convert into metallic hydrogen crystals in water",
                    "Hydrogen ions are heavier than water molecules and sink to the bottom as sludge",
                    "Hydrogen ions instantly react with oxygen to form toxic hydrogen peroxide"
                ],
                "answer": 0,
                "hint": "A bare proton has a tiny radius (~10^-15 m), resulting in an enormous electric field that polarizes water.",
                "explanation": "A bare proton (H+) has an immense charge density. In water, it instantly forms a coordinate covalent bond with a lone pair on a water molecule to generate a stable hydronium ion (H3O+).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: H+ + :OH2 -> [H3O]+ (hydronium cation).",
                    "Step 2: Reaction Mechanism & Stoichiometry: The oxygen atom of H2O donates a lone electron pair to form a dative coordinate bond with the bare proton.",
                    "Step 3: Verification & Real-World Application: Because H+ exists as H3O+, chemical equations write H+(aq) and H3O+(aq) interchangeably."
                ]
            },
            {
                "id": 4,
                "question": "What is the critical laboratory safety rule for diluting concentrated sulphuric acid with water?",
                "options": [
                    "Always add water rapidly to the acid while sealing the flask with a stopper",
                    "Always add concentrated acid slowly to water with constant, vigorous stirring",
                    "Boil the water first before adding concentrated acid in a single pour",
                    "Mix equal quantities of acid and water simultaneously in a plastic beaker"
                ],
                "answer": 1,
                "hint": "Water has a high specific heat capacity and absorbs hydration enthalpy safely if acid is added dropwise.",
                "explanation": "Dilution is intensely exothermic. Adding acid to water allows the large bulk of water to absorb the heat. Adding water to acid causes localized flash boiling and explosive spurting of corrosive acid.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: H2SO4(conc) + H2O(l) -> H3O+(aq) + HSO4-(aq) + Large Heat (exothermic).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Adding water to acid concentrates heat in the incoming water droplet, instantly flashing it to steam and causing violent acid spurting.",
                    "Step 3: Verification & Real-World Application: Adding acid dropwise to a large volume of water with continuous stirring dissipates thermal energy safely."
                ]
            },
            {
                "id": 5,
                "question": "How does the concentration of hydronium ions (H3O+) change per unit volume when an acidic solution is diluted by adding distilled water?",
                "options": [
                    "The concentration of H3O+ per unit volume increases exponentially",
                    "The concentration of H3O+ per unit volume decreases steadily",
                    "The concentration remains perfectly constant regardless of water volume",
                    "All hydronium ions are converted into molecular hydrogen gas"
                ],
                "answer": 1,
                "hint": "Concentration is moles of solute divided by total volume of solution.",
                "explanation": "Adding water increases the total volume of the solution without changing the moles of acid. Consequently, the concentration of H3O+ ions per unit volume decreases.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Concentration C = n / V, where n is moles of H3O+ and V is total solution volume.",
                    "Step 2: Reaction Mechanism & Stoichiometry: As volume V increases through dilution, the ratio n/V decreases proportionally.",
                    "Step 3: Verification & Real-World Application: Dilution reduces acidic aggressiveness and increases the numerical pH of the solution toward 7."
                ]
            },
            {
                "id": 6,
                "question": "Solution X has a pH of 2 and Solution Y has a pH of 5. How do their hydrogen ion concentrations compare?",
                "options": [
                    "Solution X has 1000 times higher hydrogen ion concentration than Solution Y",
                    "Solution Y has 3 times higher hydrogen ion concentration than Solution X",
                    "Solution X has 3 times lower hydrogen ion concentration than Solution Y",
                    "Both solutions possess identical hydrogen ion concentrations"
                ],
                "answer": 0,
                "hint": "The pH scale is logarithmic: each unit decrease corresponds to a 10-fold increase in [H+].",
                "explanation": "pH difference = 5 - 2 = 3 units. Since pH is a negative base-10 logarithm, Solution X has 10^3 = 1000 times greater hydrogen ion concentration than Solution Y.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: pH = -log10[H+]. Therefore, [H+] = 10^(-pH).",
                    "Step 2: Reaction Mechanism & Stoichiometry: For Solution X, [H+] = 10^-2 M. For Solution Y, [H+] = 10^-5 M. Ratio = 10^-2 / 10^-5 = 10^3 = 1000.",
                    "Step 3: Verification & Real-World Application: Lower numerical pH indicates higher [H+]; a difference of 3 units signifies a 1000-fold concentration difference."
                ]
            },
            {
                "id": 7,
                "question": "What is the pH of pure distilled water at 25°C, and what does this signify regarding its ion concentrations?",
                "options": [
                    "pH = 0; contains only hydrogen ions and zero hydroxide ions",
                    "pH = 7; contains equal concentrations of H3O+ and OH- ions (10^-7 M each)",
                    "pH = 14; contains only hydroxide ions and zero hydronium ions",
                    "pH = 5.6; contains dissolved carbonic acid equilibrium"
                ],
                "answer": 1,
                "hint": "In neutral water, auto-ionisation yields [H3O+] = [OH-].",
                "explanation": "Pure water auto-ionises via 2H2O <=> H3O+ + OH-. At 25°C, [H3O+] = [OH-] = 1.0 x 10^-7 M, giving pH = -log10(10^-7) = 7, indicating perfect neutrality.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2H2O(l) <=> H3O+(aq) + OH-(aq), Kw = [H3O+][OH-] = 1.0 x 10^-14 at 25°C.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In pure water, [H3O+] = [OH-] = sqrt(10^-14) = 10^-7 M.",
                    "Step 3: Verification & Real-World Application: pH = -log10(10^-7) = 7.0. Perfect equivalence of hydronium and hydroxide ions defines chemical neutrality."
                ]
            },
            {
                "id": 8,
                "question": "Which of the following acids is classified as a strong acid that ionises completely in aqueous solution?",
                "options": [
                    "Acetic acid (CH3COOH)",
                    "Hydrochloric acid (HCl)",
                    "Carbonic acid (H2CO3)",
                    "Citric acid (C6H8O7)"
                ],
                "answer": 1,
                "hint": "Mineral acids like HCl, HNO3, and H2SO4 dissociate almost 100% in water.",
                "explanation": "Hydrochloric acid (HCl) is a strong mineral acid that completely dissociates into H+ and Cl- ions in water. Acetic, carbonic, and citric acids are weak acids that ionise only partially.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: HCl(aq) -> H+(aq) + Cl-(aq) (100% dissociation).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Strong acids completely release their protons with no intact covalent molecules remaining in solution.",
                    "Step 3: Verification & Real-World Application: Weak acids like CH3COOH establish an equilibrium with mostly un-ionised molecules: CH3COOH <=> CH3COO- + H+."
                ]
            },
            {
                "id": 9,
                "question": "What is the German meaning of the letter 'p' in the term pH?",
                "options": [
                    "Proton (subatomic particle)",
                    "Potenz (meaning power or strength)",
                    "Precipitate (insoluble solid)",
                    "Percentage (ratio per hundred)"
                ],
                "answer": 1,
                "hint": "Introduced by Sørensen in 1909, referencing the 'power' of hydrogen.",
                "explanation": "In pH, 'p' stands for 'potenz', the German word for power, referring to the power or mathematical exponent of the hydrogen ion concentration.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Introduced by Danish chemist Søren P. L. Sørensen in 1909.",
                    "Step 2: Reaction Mechanism & Stoichiometry: 'p' denotes 'potenz' (German for power/potency), expressing concentration as a negative power of 10.",
                    "Step 3: Verification & Real-World Application: Hence pH mathematically represents the power of hydrogen ion concentration: [H+] = 10^(-pH)."
                ]
            },
            {
                "id": 10,
                "question": "What happens to the pH of tap water if a few drops of sodium hydroxide solution are added?",
                "options": [
                    "The pH increases above 7 as hydroxide ion concentration rises",
                    "The pH decreases below 7 as acidity increases",
                    "The pH remains constant at exactly 7.0",
                    "The pH drops to zero immediately"
                ],
                "answer": 0,
                "hint": "Adding an alkali increases [OH-], which lowers [H+] and raises pH.",
                "explanation": "Sodium hydroxide is a strong base that releases OH- ions. Increasing [OH-] causes [H+] to decrease via the ionic product of water (Kw = [H+][OH-]), driving the pH above 7.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: NaOH(aq) -> Na+(aq) + OH-(aq).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Kw = [H+][OH-] = 10^-14. Increasing [OH-] forces [H+] to decrease, which increases the pH value: pH = -log10[H+].",
                    "Step 3: Verification & Real-World Application: Any addition of alkaline substances raises the solution pH into the basic domain (pH > 7)."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Everyday pH Review",
        "subtitle": "Digestive Acidity, Tooth Enamel Corrosion, Stinging Venoms, and Natural Organic Acids",
        "speech": "",
        "content": {
            "concept": "Mastery challenge covering physiological pH regulation, stomach acidity and antacids, dental decay mechanics, chemical warfare in plants and animals, and identification of natural organic acids.",
            "formula": "\\text{Enamel Decay: pH} < 5.5 \\quad | \\quad \\text{Antacid: } \\text{Mg(OH)}_2 + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + 2\\text{H}_2\\text{O} \\quad | \\quad \\text{Sting: HCOOH}",
            "points": [
                "Human physiological pH is tightly maintained between 7.0 and 7.8.",
                "Stomach hyperacidity is neutralised by antacids like Milk of Magnesia (Mg(OH)2).",
                "Tooth decay begins when oral pH drops below 5.5, corroding calcium hydroxyapatite enamel.",
                "Bee and nettle stings inject methanoic acid; neutralised by mild baking soda or dock plant leaves.",
                "Naturally occurring acids: acetic (vinegar), citric (citrus), tartaric (tamarind), oxalic (tomato), lactic (curd)."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "What is the physiological pH range within which the human body functions optimally and safely?",
                "options": [
                    "pH 1.0 to 2.5",
                    "pH 5.0 to 6.2",
                    "pH 7.0 to 7.8",
                    "pH 8.5 to 10.0"
                ],
                "answer": 2,
                "hint": "Human blood and extracellular fluids are slightly alkaline.",
                "explanation": "Our bodies function within a narrow, slightly alkaline pH window of 7.0 to 7.8. Blood pH is tightly regulated around 7.35 to 7.45 by physiological buffer systems.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Biological homeostasis requires optimal enzymatic conformational stability within pH 7.0 to 7.8.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Blood carbonic acid-bicarbonate buffer: CO2 + H2O <=> H2CO3 <=> H+ + HCO3- resists pH shifts.",
                    "Step 3: Verification & Real-World Application: Blood pH falling below 7.0 or rising above 7.8 causes acidosis or alkalosis, leading to severe metabolic failure."
                ]
            },
            {
                "id": 2,
                "question": "What is the threshold pH value below which atmospheric precipitation is formally classified as acid rain?",
                "options": [
                    "pH below 7.0",
                    "pH below 5.6",
                    "pH below 4.0",
                    "pH below 2.0"
                ],
                "answer": 1,
                "hint": "Normal unpolluted rain has a pH around 5.6 due to dissolved carbon dioxide.",
                "explanation": "Unpolluted rain has a natural pH of ~5.6 due to dissolved CO2 forming carbonic acid. When pollutants (SO2 and NO2) dissolve to form H2SO4 and HNO3, driving pH below 5.6, it is termed acid rain.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Unpolluted rain: CO2 + H2O <=> H2CO3 (pH ~5.6). Acid rain: SO2/NO2 + H2O -> H2SO4/HNO3 (pH < 5.6).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Strong mineral acids dissociate completely in rainwater, lowering environmental pH drastically.",
                    "Step 3: Verification & Real-World Application: Acid rain (pH < 5.6) leaches toxic aluminium ions into rivers, corrodes marble monuments (marble cancer), and kills aquatic life."
                ]
            },
            {
                "id": 3,
                "question": "What thick chemical clouds shroud the planet Venus, preventing any possibility of terrestrial life?",
                "options": [
                    "Thick clouds of concentrated sulphuric acid",
                    "Vast canopies of condensed liquid nitrogen",
                    "Dense vaporized plumes of hydrochloric acid",
                    "Pure methane and liquid ammonia clouds"
                ],
                "answer": 0,
                "hint": "Refer to the 'Do You Know?' box in the NCERT syllabus regarding Venus.",
                "explanation": "The atmosphere of Venus is dominated by dense, yellowish-white clouds composed of concentrated sulphuric acid (H2SO4), creating an ultra-corrosive, hyper-acidic environment.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Venusian atmospheric clouds consist of microscopic droplets of concentrated sulphuric acid (H2SO4).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Intense solar ultraviolet radiation photolyses atmospheric gases to produce sulfur trioxide, which combines with trace moisture to form H2SO4.",
                    "Step 3: Verification & Real-World Application: These thick sulphuric acid clouds produce a runaway greenhouse effect and extreme acidity that prevents biological life."
                ]
            },
            {
                "id": 4,
                "question": "Which antacid suspension is commonly administered to relieve stomach hyperacidity and heartburn?",
                "options": [
                    "Milk of Magnesia (magnesium hydroxide)",
                    "Concentrated sodium hydroxide solution",
                    "Dilute hydrochloric acid drops",
                    "Copper sulphate solution"
                ],
                "answer": 0,
                "hint": "A mild, sparingly soluble basic metal hydroxide that neutralises acid safely without corrosive damage.",
                "explanation": "Milk of Magnesia is a mild suspension of magnesium hydroxide, Mg(OH)2. Being a mild base, it safely neutralises excess stomach hydrochloric acid without damaging gastric mucosa.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Mg(OH)2(s) + 2HCl(aq) -> MgCl2(aq) + 2H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: 1 mole of magnesium hydroxide neutralises 2 moles of excess gastric hydrochloric acid to form harmless magnesium chloride and water.",
                    "Step 3: Verification & Real-World Application: Strong bases like NaOH cannot be used because their corrosive caustic properties would severely burn digestive tissue."
                ]
            },
            {
                "id": 5,
                "question": "Tooth enamel is the hardest substance in the human body. What is its chemical composition and at what oral pH does it begin to corrode?",
                "options": [
                    "Calcium carbonate; corrodes when pH rises above 8.5",
                    "Calcium hydroxyapatite (crystalline calcium phosphate); corrodes when pH falls below 5.5",
                    "Magnesium phosphate; corrodes when pH reaches exactly 7.0",
                    "Sodium chloride; corrodes when pH drops below 1.0"
                ],
                "answer": 1,
                "hint": "Enamel consists of crystalline calcium phosphate and demineralises in weak bacterial acids below pH 5.5.",
                "explanation": "Tooth enamel is made of calcium hydroxyapatite (a crystalline form of calcium phosphate). When oral bacteria ferment sugars to produce organic acids, dropping mouth pH below 5.5, enamel begins to corrode.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Calcium hydroxyapatite formula: Ca5(PO4)3(OH). Demineralisation begins at oral pH < 5.5.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Bacterial acid fermentation: Food sugars -> Lactic/organic acids. Acidic H+ dissolves the phosphate and calcium lattice.",
                    "Step 3: Verification & Real-World Application: Brushing teeth with alkaline toothpaste neutralises oral acids and promotes enamel remineralisation, preventing cavities."
                ]
            },
            {
                "id": 6,
                "question": "Which carboxylic acid is injected by a honeybee sting or by the stinging hairs of nettle leaves, causing intense burning pain?",
                "options": [
                    "Acetic acid",
                    "Methanoic acid (formic acid)",
                    "Oxalic acid",
                    "Tartaric acid"
                ],
                "answer": 1,
                "hint": "The simplest single-carbon carboxylic acid: HCOOH.",
                "explanation": "Both bee stings and stinging nettle hairs inject methanoic acid (formic acid, HCOOH). The acidic venom irritates skin nerve endings, causing burning pain and localized swelling.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Methanoic acid formula: HCOOH. Injected venom creates localized skin acidosis.",
                    "Step 2: Reaction Mechanism & Stoichiometry: HCOOH dissociates into H+ and HCOO- (formate anion), triggering inflammatory pain receptors.",
                    "Step 3: Verification & Real-World Application: Applying a mild base such as baking soda (NaHCO3) neutralises the acid: HCOOH + NaHCO3 -> HCOONa + H2O + CO2."
                ]
            },
            {
                "id": 7,
                "question": "Which wild plant commonly grows right next to stinging nettle patches and serves as an effective natural remedy for nettle stings when rubbed onto the skin?",
                "options": [
                    "Cactus plant",
                    "Dock plant",
                    "Hydrangea flower",
                    "Touch-me-not plant"
                ],
                "answer": 1,
                "hint": "Traditional folklore remedy mentioned in the NCERT 'Do You Know?' section.",
                "explanation": "The dock plant frequently grows in close proximity to wild nettles in nature. Rubbing fresh dock plant leaves onto the skin provides a mild alkaline sap that neutralises the methanoic acid from the nettle sting.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Nettle sting delivers methanoic acid (HCOOH). Dock plant sap contains mild basic components.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Direct mechanical rubbing releases alkaline sap that neutralises the acidic sting directly on the epidermis.",
                    "Step 3: Verification & Real-World Application: Exemplifies natural chemical coexistence where a biological poison and its corresponding antidote grow side by side."
                ]
            },
            {
                "id": 8,
                "question": "Match the naturally occurring acid present in sour milk (curd), vinegar, and tamarind:",
                "options": [
                    "Curd: Lactic acid; Vinegar: Acetic acid; Tamarind: Tartaric acid",
                    "Curd: Citric acid; Vinegar: Oxalic acid; Tamarind: Methanoic acid",
                    "Curd: Tartaric acid; Vinegar: Lactic acid; Tamarind: Acetic acid",
                    "Curd: Oxalic acid; Vinegar: Tartaric acid; Tamarind: Citric acid"
                ],
                "answer": 0,
                "hint": "Curd has lactic acid, vinegar has acetic acid, and tamarind has tartaric acid.",
                "explanation": "According to Table 2.3: Sour milk/curd contains lactic acid; vinegar contains acetic acid (ethanoic acid); tamarind contains tartaric acid.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Natural organic acids: Curd -> Lactic acid; Vinegar -> Acetic acid; Tamarind -> Tartaric acid; Tomato -> Oxalic acid.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Microbial fermentation of milk lactose yields lactic acid (CH3CH(OH)COOH). Acetobacter converts ethanol to acetic acid (CH3COOH).",
                    "Step 3: Verification & Real-World Application: Memorizing natural organic acids from Table 2.3 is a foundational component of Class 10 chemistry examinations."
                ]
            },
            {
                "id": 9,
                "question": "Which organic acid is predominantly present in ripe tomatoes and can form insoluble calcium salts in kidney stones?",
                "options": [
                    "Citric acid",
                    "Oxalic acid",
                    "Acetic acid",
                    "Lactic acid"
                ],
                "answer": 1,
                "hint": "A dicarboxylic acid with formula HOOC-COOH.",
                "explanation": "Tomatoes contain oxalic acid (HOOC-COOH). In biological systems, excessive oxalic acid can bind with calcium ions to precipitate insoluble calcium oxalate crystals (kidney stones).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Oxalic acid formula: (COOH)2 or C2H2O4.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Oxalate anions (C2O4 2-) react with divalent calcium cations: Ca2+(aq) + C2O4 2-(aq) -> CaC2O4(s) (insoluble calcium oxalate).",
                    "Step 3: Verification & Real-World Application: Demonstrates the dietary occurrence of oxalic acid in tomatoes and green leafy vegetables like spinach."
                ]
            },
            {
                "id": 10,
                "question": "Why does rubbing a tarnished copper vessel with a slice of lemon or tamarind paste quickly restore its brilliant reddish-brown metallic shine?",
                "options": [
                    "Citric and tartaric acids dissolve the basic copper carbonate patina coating",
                    "The acid deposits an artificial golden paint layer on the copper surface",
                    "Lemon juice oxidises copper metal into volatile copper gas",
                    "Tamarind contains abrasive diamond micro-particles that scrape off copper"
                ],
                "answer": 0,
                "hint": "Tarnish on copper is basic copper carbonate, which reacts with organic acids to form soluble salts.",
                "explanation": "Copper tarnishes in moist air to form a green patina of basic copper carbonate, CuCO3·Cu(OH)2. The organic acids in lemon (citric) and tamarind (tartaric) neutralize and dissolve this basic layer, exposing clean copper.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Tarnish patina: CuCO3·Cu(OH)2 (basic copper carbonate). Acid: Citric/tartaric acid.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Basic copper carbonate reacts with the organic acid: CuCO3·Cu(OH)2 + Acid -> Soluble Copper Citrate/Tartrate + H2O + CO2.",
                    "Step 3: Verification & Real-World Application: Washing with water rinses away the soluble copper salts, restoring the lustrous reddish-brown copper metal surface."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Salt Technology Review",
        "subtitle": "Chlor-Alkali Process, Bleaching Powder, Baking & Washing Soda, and Gypsum Chemistry",
        "speech": "",
        "content": {
            "concept": "Mastery challenge covering industrial chlor-alkali electrolysis, chemical preparation and uses of bleaching powder, baking soda, washing soda, water of crystallisation, and Plaster of Paris.",
            "formula": "2\\text{NaCl} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{Cl}_2 + \\text{H}_2 \\quad | \\quad \\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O} \\rightarrow \\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O}",
            "points": [
                "Chlor-alkali process: Brine electrolysis yields Cl2 (anode), H2 (cathode), and NaOH (cathode).",
                "Bleaching powder (CaOCl2) is prepared by acting chlorine on dry slaked lime Ca(OH)2.",
                "Baking soda (NaHCO3) decomposes on heating to release CO2; mixed with tartaric acid it forms baking powder.",
                "Washing soda (Na2CO3·10H2O) removes permanent water hardness and manufactures glass/soap.",
                "Plaster of Paris (CaSO4·1/2H2O) is prepared by heating gypsum at 373 K; sets into hard gypsum with water."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "In the industrial chlor-alkali process for electrolysing concentrated brine, which products are collected at the anode and cathode respectively?",
                "options": [
                    "Anode: Chlorine gas; Cathode: Hydrogen gas (with NaOH formed near cathode)",
                    "Anode: Hydrogen gas; Cathode: Chlorine gas (with HCl formed near anode)",
                    "Anode: Oxygen gas; Cathode: Metallic sodium crystals",
                    "Anode: Sodium hydroxide; Cathode: Pure liquid chlorine"
                ],
                "answer": 0,
                "hint": "Negative chloride ions are oxidised at the positive anode; positive hydrogen ions are reduced at the negative cathode.",
                "explanation": "In brine electrolysis: 2NaCl + 2H2O -> 2NaOH + Cl2(g) + H2(g). Chlorine gas evolves at the positive anode, hydrogen gas evolves at the negative cathode, and NaOH forms near the cathode.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2NaCl(aq) + 2H2O(l) -electricity-> 2NaOH(aq) + Cl2(g)^ [Anode] + H2(g)^ [Cathode].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Anode oxidation: 2Cl- -> Cl2 + 2e-. Cathode reduction: 2H2O + 2e- -> H2 + 2OH-. Na+ and OH- combine near the cathode to form NaOH.",
                    "Step 3: Verification & Real-World Application: The process is named 'chlor-alkali' because its co-products are chlorine ('chlor') and sodium hydroxide ('alkali')."
                ]
            },
            {
                "id": 2,
                "question": "How is bleaching powder (calcium oxychloride) synthesized commercially in chemical manufacturing?",
                "options": [
                    "By reacting chlorine gas with dry slaked lime [Ca(OH)2]",
                    "By passing carbon dioxide through calcium oxide",
                    "By treating limestone with concentrated hydrochloric acid",
                    "By heating calcium sulphate dihydrate at 373 K"
                ],
                "answer": 0,
                "hint": "Slaked lime is Ca(OH)2 and reacts directly with chlorine gas from the chlor-alkali process.",
                "explanation": "Bleaching powder is manufactured by the action of chlorine gas on dry slaked lime: Ca(OH)2 + Cl2 -> CaOCl2 (calcium oxychloride) + H2O.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Ca(OH)2(s) + Cl2(g) -> CaOCl2(s) + H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Chlorine acts on dry calcium hydroxide to form calcium oxychloride (CaOCl2), which acts as a chlorine reservoir.",
                    "Step 3: Verification & Real-World Application: Used extensively as a disinfectant for sterilizing municipal drinking water and as a bleaching agent in cotton and linen textile mills."
                ]
            },
            {
                "id": 3,
                "question": "What chemical reaction occurs when sodium hydrogencarbonate (baking soda) is heated during baking and cooking?",
                "options": [
                    "2NaHCO3 -heat-> Na2CO3 + H2O + CO2",
                    "NaHCO3 -heat-> NaOH + CO2",
                    "2NaHCO3 -heat-> Na2O + 2CO2 + H2",
                    "NaHCO3 does not decompose under heat"
                ],
                "answer": 0,
                "hint": "Thermal decomposition yields sodium carbonate, water vapor, and carbon dioxide gas.",
                "explanation": "When baking soda is heated, it decomposes: 2NaHCO3 -heat-> Na2CO3 + H2O + CO2(g). The released carbon dioxide bubbles cause dough to rise, making cakes soft and spongy.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2NaHCO3(s) -heat-> Na2CO3(s) + H2O(g) + CO2(g)^.",
                    "Step 2: Reaction Mechanism & Stoichiometry: 2 moles of solid sodium hydrogencarbonate yield 1 mole of sodium carbonate, 1 mole of steam, and 1 mole of carbon dioxide gas.",
                    "Step 3: Verification & Real-World Application: Entrapped CO2 gas expands thermally during baking, creating a porous spongy texture in breads and cakes."
                ]
            },
            {
                "id": 4,
                "question": "Why is commercial baking powder formulated as a mixture of baking soda and mild edible tartaric acid rather than pure baking soda alone?",
                "options": [
                    "Tartaric acid neutralises basic sodium carbonate formed on heating, preventing a bitter taste",
                    "Tartaric acid prevents baking soda from absorbing atmospheric moisture",
                    "Tartaric acid doubles the weight of the cake batter for commercial profit",
                    "Tartaric acid turns the baked cake bright white"
                ],
                "answer": 0,
                "hint": "Thermal decomposition of NaHCO3 produces alkaline Na2CO3, which tastes unpleasantly bitter.",
                "explanation": "Heating baking soda produces basic Na2CO3, which imparts a bitter taste to cakes. Tartaric acid reacts with this Na2CO3 to form neutral sodium tartrate, eliminating bitterness while producing additional CO2.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: NaHCO3 + H+(from tartaric acid) -> Na+(from tartrate salt) + H2O + CO2^.",
                    "Step 2: Reaction Mechanism & Stoichiometry: The hydrogen ions from edible tartaric acid neutralise the alkaline carbonate, forming harmless, pleasant-tasting sodium tartrate.",
                    "Step 3: Verification & Real-World Application: Ensures cakes taste delicious and sweet while maximizing carbon dioxide bubble aeration."
                ]
            },
            {
                "id": 5,
                "question": "What is the chemical name, molecular formula, and water of crystallisation of washing soda?",
                "options": [
                    "Sodium carbonate decahydrate, Na2CO3·10H2O (10 water molecules)",
                    "Sodium hydrogencarbonate, NaHCO3 (zero water molecules)",
                    "Calcium sulphate hemihydrate, CaSO4·1/2H2O (half water molecule)",
                    "Copper sulphate pentahydrate, CuSO4·5H2O (5 water molecules)"
                ],
                "answer": 0,
                "hint": "Washing soda is obtained by recrystallising sodium carbonate with ten water molecules.",
                "explanation": "Washing soda is sodium carbonate decahydrate, with formula Na2CO3·10H2O. It contains exactly 10 molecules of water of crystallisation per formula unit.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Na2CO3(s) + 10H2O(l) -> Na2CO3·10H2O(s).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Recrystallisation from aqueous solution incorporates ten water molecules into the crystal lattice per unit of Na2CO3.",
                    "Step 3: Verification & Real-World Application: Used in glass, soap, and paper manufacturing, in cleaning formulations, and for removing permanent water hardness."
                ]
            },
            {
                "id": 6,
                "question": "Which commercial salt is specifically employed for removing the permanent hardness of water caused by dissolved calcium and magnesium sulphates?",
                "options": [
                    "Washing soda (Na2CO3·10H2O)",
                    "Baking soda (NaHCO3)",
                    "Bleaching powder (CaOCl2)",
                    "Plaster of Paris (CaSO4·1/2H2O)"
                ],
                "answer": 0,
                "hint": "Soluble carbonate ions precipitate dissolved Ca2+ and Mg2+ as insoluble carbonates.",
                "explanation": "Washing soda (Na2CO3) precipitates dissolved calcium and magnesium ions responsible for permanent water hardness as insoluble carbonates: Ca2+ + CO3 2- -> CaCO3(s).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CaSO4(aq) [Hard water] + Na2CO3(aq) -> CaCO3(s)v + Na2SO4(aq).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Divalent Ca2+ and Mg2+ ions form insoluble carbonate precipitates, removing hard multivalent cations from solution.",
                    "Step 3: Verification & Real-World Application: The softened water can now lather freely with soap without forming insoluble scum."
                ]
            },
            {
                "id": 7,
                "question": "In Activity 2.15, blue crystals of hydrated copper sulphate are heated inside a dry test tube. What observation confirms the presence of water of crystallisation?",
                "options": [
                    "Water droplets condense on the cool upper walls and the blue crystals turn into white anhydrous powder",
                    "The crystals melt into an oily black liquid and evolve sulfur dioxide gas",
                    "The blue colour intensifies into dark navy blue with explosive sparks",
                    "The crystals double in volume and turn bright yellow"
                ],
                "answer": 0,
                "hint": "Heating drives off the 5 water molecules of hydration.",
                "explanation": "CuSO4·5H2O(s) [blue] -heat-> CuSO4(s) [white anhydrous] + 5H2O(g). The driven-off water condenses on the upper tube walls. Adding a few drops of water restores the blue colour immediately.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CuSO4·5H2O(s) [Blue] -heat-> CuSO4(s) [White] + 5H2O(g).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Thermal energy breaks coordinate and hydrogen bonds between water molecules and Cu2+/SO4 2- ions, releasing 5 moles of H2O per mole of salt.",
                    "Step 3: Verification & Real-World Application: Rehydration: CuSO4(s) + 5H2O(l) -> CuSO4·5H2O(s) restores hydrated crystal coordination and characteristic blue colour."
                ]
            },
            {
                "id": 8,
                "question": "What is the precise temperature condition for heating Gypsum to successfully synthesize Plaster of Paris without producing dead-burnt plaster?",
                "options": [
                    "373 K (100°C)",
                    "273 K (0°C)",
                    "473 K (200°C)",
                    "573 K (300°C)"
                ],
                "answer": 0,
                "hint": "373 Kelvin equals 100 degrees Celsius.",
                "explanation": "Heating gypsum (CaSO4·2H2O) carefully at exactly 373 K (100°C) removes 1.5 water molecules to yield Plaster of Paris (CaSO4·1/2H2O). Heating above 373 K drives off all water, forming inactive 'dead-burnt plaster'.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CaSO4·2H2O(s) [Gypsum] -373 K-> CaSO4·1/2H2O(s) [POP] + 1.5 H2O(g).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Controlled dehydration at 373 K retains exactly half a molecule of water per formula unit of calcium sulphate.",
                    "Step 3: Verification & Real-World Application: Exceeding 373 K causes complete dehydration to anhydrous CaSO4 (dead-burnt plaster), which loses the ability to set rapidly with water."
                ]
            },
            {
                "id": 9,
                "question": "What happens when Plaster of Paris is mixed with water during medical casting of fractured bones?",
                "options": [
                    "It hydrates and sets into a hard solid crystalline mass of gypsum within minutes",
                    "It dissolves completely to form a transparent liquid that never solidifies",
                    "It decomposes into toxic sulphur dioxide gas and calcium metal",
                    "It explodes violently due to an endothermic freezing reaction"
                ],
                "answer": 0,
                "hint": "Plaster of Paris absorbs 1.5 molecules of water to reform its original mineral dihydrate: Gypsum.",
                "explanation": "CaSO4·1/2H2O + 1.5 H2O -> CaSO4·2H2O (gypsum). POP absorbs water and recrystallises into interlocking gypsum crystals, setting into a hard, rigid mass that immobilizes fractured bones.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CaSO4·1/2H2O(s) + 1.5 H2O(l) -> CaSO4·2H2O(s) [Gypsum].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Half-hydrated crystals dissolve slightly, supersaturate, and rapidly precipitate as an interlocking lattice of needle-shaped gypsum dihydrate crystals.",
                    "Step 3: Verification & Real-World Application: The slight expansion upon crystallization ensures tight fitting of orthopaedic casts, decorative mouldings, and statues."
                ]
            },
            {
                "id": 10,
                "question": "Which of the following chemical formulas correctly represents the salt present in a working soda-acid fire extinguisher?",
                "options": [
                    "Sodium hydrogencarbonate (NaHCO3) and sulphuric acid (H2SO4)",
                    "Calcium chloride (CaCl2) and nitric acid (HNO3)",
                    "Sodium hydroxide (NaOH) and hydrochloric acid (HCl)",
                    "Copper sulphate (CuSO4) and acetic acid (CH3COOH)"
                ],
                "answer": 0,
                "hint": "The reaction rapidly produces pressurized carbon dioxide gas to smother flames.",
                "explanation": "A soda-acid fire extinguisher contains sodium hydrogencarbonate (baking soda) solution and an ignition tube of dilute sulphuric acid. Inverting the extinguisher mixes them: 2NaHCO3 + H2SO4 -> Na2SO4 + 2H2O + 2CO2(g), blasting pressurized CO2 to smother fires.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2NaHCO3(aq) + H2SO4(aq) -> Na2SO4(aq) + 2H2O(l) + 2CO2(g)^.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Rapid acid-carbonate neutralization generates immense carbon dioxide gas pressure inside the extinguisher canister.",
                    "Step 3: Verification & Real-World Application: The dense, non-combustible CO2 gas blankets the fire, displacing oxygen and extinguishing the flame immediately."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides:
        assert s["speech"] == "", f"Slide {s['id']} must have empty speech"
        assert len(s["title"].split()) <= 3, f"Slide {s['id']} title '{s['title']}' has > 3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} must have 10 questions"
        for q in s["questions"]:
            assert len(q["options"]) == 4, f"Question {q['id']} must have 4 options"
            assert 0 <= q["answer"] <= 3, f"Question {q['id']} answer out of range"
            assert len(q["solution"]) == 3, f"Question {q['id']} solution must have 3 steps"
    print("All slides 17 to 20 validated successfully!")

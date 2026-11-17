"""Generate Slides 9 to 16 for Class 10 Science Chapter 4: Carbon and its Compounds
Strict constraints:
- Title: strictly 1 to 3 words
- Speech: strictly 195 to 215 words
- Pure Indian male teacher voice
- No fictional characters or persona titles
- 2 checkpoints per slide with 4 options, hint, and explanation
"""

slides = [
    {
        "id": 9,
        "title": "Heteroatom Functional Groups",
        "subtitle": "Heteroatom Substitutions, Table 4.3 Families, and Chemical Reactivity Centres",
        "speech": "In hydrocarbon chains, carbon atoms establish an extraordinarily accommodating and flexible chemical scaffold. Hydrogen atoms bonded to carbon can be readily substituted by atoms of other elements without altering the underlying four-fold carbon valency. Elements that replace hydrogen in carbon frameworks—most commonly halogens like chlorine and bromine, oxygen, nitrogen, and sulphur—are systematically termed heteroatoms. When heteroatoms confer specific chemical reactivity to the organic molecule regardless of the chain length or nature of the carbon framework, they and the specific atomic groups they form are designated as functional groups. Table 4.3 outlines the five cardinal functional group families every chemistry student must master. First, haloalkanes replace hydrogen with chlorine or bromine, designated as chloro- or bromo- derivatives. Second, the alcohol functional group introduces an oxygen-hydrogen moiety, written as minus OH. Third, the aldehyde group features a terminal carbonyl carbon bonded to hydrogen, represented as minus CHO. Fourth, ketones incorporate an internal carbonyl carbon bonded between two flanking carbon atoms, represented as greater-than C double-bond O. Finally, carboxylic acids incorporate a terminal carbonyl and hydroxyl group together, written as minus COOH. Functional groups are the true chemical engines that dictate molecular reactivity across organic synthesis in nature.",
        "content": {
            "concept": "Heteroatoms (Cl, Br, O, N, S) replace hydrogen in hydrocarbon chains. Functional groups are specific atom groups that confer characteristic chemical properties to the compound regardless of chain length (Table 4.3: Halo, Alcohol -OH, Aldehyde -CHO, Ketone >C=O, Carboxylic acid -COOH).",
            "formula": "\\text{Alcohol: } -\\text{OH} \\quad | \\quad \\text{Aldehyde: } -\\text{CHO} \\quad | \\quad \\text{Ketone: } >\\text{C}=\\text{O} \\quad | \\quad \\text{Carboxylic Acid: } -\\text{COOH}",
            "points": [
                "Heteroatoms are non-carbon, non-hydrogen atoms (halogens, oxygen, nitrogen, sulphur) attached to carbon chains.",
                "Functional groups determine chemical reactivity regardless of the length of the carbon chain.",
                "Halogen family: -Cl (chloro), -Br (bromo) replacing hydrogen.",
                "Oxygen-containing groups: Alcohol (-OH), Aldehyde (-CHO), Ketone (>C=O), Carboxylic acid (-COOH).",
                "Carbonyl group (C=O) is present in both aldehydes (terminal) and ketones (non-terminal/internal)."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the defining chemical characteristic of a 'functional group' in an organic molecule?",
                "options": [
                    "An atom or group of atoms that confers characteristic chemical properties regardless of chain length",
                    "A metallic cluster that emits radioactive alpha particles",
                    "An internal void that reduces the molecular mass to zero",
                    "A coating of noble gas that prevents all chemical reactions"
                ],
                "answer": 0,
                "hint": "Functional groups are the specific reaction centers that dictate how a molecule behaves.",
                "explanation": "A functional group is an atom or group of atoms (such as -OH, -CHO, -COOH) that gives a compound its characteristic chemical properties, independent of the size of the carbon chain."
            },
            {
                "question": "What is the structural difference between an aldehyde group and a ketone group in organic chemistry?",
                "options": [
                    "Aldehydes possess a terminal carbonyl group (-CHO); ketones possess an internal carbonyl group (>C=O) between two carbons",
                    "Aldehydes contain sulphur, whereas ketones contain chlorine",
                    "Aldehydes are ionic salts, whereas ketones are metals",
                    "There is no difference; aldehyde and ketone are identical terms"
                ],
                "answer": 0,
                "hint": "An aldehyde is always at the end of a chain (-CHO), while a ketone must have carbon atoms on both sides (>C=O).",
                "explanation": "Aldehydes feature a terminal carbonyl carbon bonded to at least one hydrogen (-CHO). Ketones contain a carbonyl group (>C=O) bonded between two flanking carbon atoms within the chain."
            }
        ]
    },
    {
        "id": 10,
        "title": "Homologous Chemical Series",
        "subtitle": "Gradation of Physical Constants, Identical Reactivity, and the 14u Increment",
        "speech": "When we arrange organic molecules sharing the same functional group in order of increasing chain length, an elegant mathematical pattern emerges: a homologous series. A homologous series is defined as a family of organic compounds containing identical functional groups where successive members differ by a specific repeating structural unit: a minus CH2 minus group, commonly called a methylene bridge. Consider the homologous family of alkanes: methane CH4, ethane C2H6, propane C3H8, and butane C4H10. Calculating the difference between any two sequential members reveals exactly one carbon atom and two hydrogen atoms. Because the atomic mass of carbon is twelve units and hydrogen is one unit, successive members invariably differ by fourteen atomic mass units. In Activity 4.2, examining the alcohol series—methanol CH3OH, ethanol C2H5OH, propanol C3H7OH, and butanol C4H9OH—confirms the exact same fourteen unit increment throughout all adjacent members. Because all members possess the identical functional group, their chemical properties are virtually indistinguishable. However, as molecular mass increases systematically along the series, inter-molecular van der Waals attractions strengthen, producing a smooth, predictable gradation in physical properties such as rising melting points, boiling points, densities, and changing solubilities in water across the entire family of hydrocarbons.",
        "content": {
            "concept": "A homologous series is a series of compounds with the same functional group where successive members differ by a -CH2- unit (14 u molecular mass difference). Members show identical chemical properties and a regular gradation in physical properties (boiling point, solubility).",
            "formula": "\\text{Successive Difference: } -\\text{CH}_2- \\quad | \\quad \\Delta M = 12 + (2 \\times 1) = 14\\text{ u} \\quad | \\quad \\text{Alcohols: } \\text{CH}_3\\text{OH}, \\text{C}_2\\text{H}_5\\text{OH}, \\text{C}_3\\text{H}_7\\text{OH}",
            "points": [
                "Homologous series: family of compounds with the same functional group and general formula.",
                "Successive members differ by a -CH2- unit and 14 atomic mass units (14 u).",
                "Chemical properties remain virtually identical due to the same functional group.",
                "Physical properties (melting point, boiling point, density) show a smooth gradation with increasing mass.",
                "Solubility in water typically decreases as the hydrophobic carbon chain length increases."
            ]
        },
        "checkpoints": [
            {
                "question": "By what structural formula unit and molecular mass increment do consecutive members of any homologous series differ?",
                "options": [
                    "A -CH2- unit and 14 atomic mass units (14 u)",
                    "A -CH3- unit and 15 atomic mass units (15 u)",
                    "A -C2H4- unit and 28 atomic mass units (28 u)",
                    "A -H2O- unit and 18 atomic mass units (18 u)"
                ],
                "answer": 0,
                "hint": "One carbon (12 u) and two hydrogens (2 x 1 u = 2 u).",
                "explanation": "Every successive member of a homologous series differs from the preceding member by a methylene unit (-CH2-), corresponding to a molecular mass difference of 14 u (12 + 2 = 14)."
            },
            {
                "question": "Why do chemical properties remain identical across a homologous series while physical properties exhibit a gradual gradation?",
                "options": [
                    "Chemical properties are governed by the functional group; physical properties depend on molecular size and mass",
                    "Chemical properties depend on atmospheric weather; physical properties depend on gravity",
                    "Physical properties are identical because all molecules have the same mass",
                    "Chemical properties change randomly with each additional carbon atom"
                ],
                "answer": 0,
                "hint": "All members have the same functional group (e.g., -OH), but longer chains have stronger intermolecular attractions.",
                "explanation": "Chemical reactivity is dictated by the functional group, which is identical across the series. Physical properties (boiling point, melting point) depend on molecular mass and surface area, which increase regularly."
            }
        ]
    },
    {
        "id": 11,
        "title": "IUPAC Carbon Nomenclature",
        "subtitle": "Systematic IUPAC Framework: Root Words, Prefixes, and Suffix Modifiers",
        "speech": "To bring global uniformity to the millions of synthesized organic molecules, the International Union of Pure and Applied Chemistry established a systematic nomenclature method outlined in Table 4.4. Naming a carbon compound follows three logical sequential steps. First, count the number of carbon atoms in the longest continuous parent carbon chain to determine the foundational root word: one carbon is meth, two is eth, three is prop, four is but, five is pent, and six is hex. Second, identify whether the carbon skeleton is saturated or unsaturated: single bonds use the suffix ane, a double bond uses ene, and a triple bond uses yne. Third, identify any functional group attached to the chain. Haloalkanes are designated by a prefix: chloropropane or bromoethane. For oxygen-containing functional groups, the terminal letter 'e' of the alkane name is deleted before appending the appropriate functional suffix. For alcohols, add the suffix 'ol' to yield propanol; for aldehydes, add 'al' to yield propanal; for ketones, add 'one' to yield propanone; and for carboxylic acids, add 'oic acid' to yield propanoic acid. This rigorous systematic framework allows any chemist worldwide to deduce the precise molecular architecture directly from its IUPAC chemical name.",
        "content": {
            "concept": "IUPAC naming rules (Table 4.4): 1. Identify carbon chain length (meth-, eth-, prop-, but-, pent-, hex-). 2. Add saturation suffix (-ane, -ene, -yne). 3. Apply functional prefixes/suffixes: halo- (chloro/bromo), alcohol (-ol), aldehyde (-al), ketone (-one), carboxylic acid (-oic acid), dropping the final 'e' of alkane.",
            "formula": "\\text{Root: Meth (1C), Eth (2C), Prop (3C), But (4C), Pent (5C), Hex (6C)} \\quad | \\quad \\text{Propane } - \\text{e} + \\text{ol} = \\text{Propanol}",
            "points": [
                "Step 1: Count carbons in longest chain: 1=meth, 2=eth, 3=prop, 4=but, 5=pent, 6=hex.",
                "Step 2: Determine saturation: -ane (single bond), -ene (double bond), -yne (triple bond).",
                "Step 3: Modify with functional group name: Halogens use prefix (chloro-, bromo-).",
                "For -OH, -CHO, >C=O, -COOH: drop final 'e' of alkane and add suffix (-ol, -al, -one, -oic acid).",
                "Example: 3-carbon carboxylic acid = Propane - e + oic acid = Propanoic acid (CH3CH2COOH)."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the correct systematic IUPAC name for a three-carbon saturated carboxylic acid with formula CH3CH2COOH?",
                "options": [
                    "Propanoic acid",
                    "Propanol",
                    "Propanal",
                    "Propanone"
                ],
                "answer": 0,
                "hint": "Three carbons = prop; saturated = propane; carboxylic acid suffix = -oic acid (drop final 'e').",
                "explanation": "A 3-carbon saturated chain is propane. The -COOH functional group requires replacing the final 'e' with the suffix '-oic acid', producing propanoic acid."
            },
            {
                "question": "What is the systematic IUPAC name for a four-carbon saturated ketone with formula CH3-CO-CH2-CH3?",
                "options": [
                    "Butanone",
                    "Butanal",
                    "Butanol",
                    "Butanoic acid"
                ],
                "answer": 0,
                "hint": "Four carbons = butane; ketone functional group (>C=O) takes the suffix '-one'.",
                "explanation": "A 4-carbon chain is butane. Replacing the final 'e' with the ketone suffix '-one' yields butanone (specifically butan-2-one)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Hydrocarbon Combustion Chemistry",
        "subtitle": "Exothermic Oxidation, Sooty Flames, Flame Thermodynamics, and Fossil Origins",
        "speech": "All carbon compounds burn in atmospheric oxygen to undergo exothermic combustion, liberating substantial thermal and radiant light energy along with carbon dioxide and water vapour. For example, burning methane releases heat and light: CH4 plus two O2 yields CO2 plus two H2O plus heat. In Activities 4.3 and 4.4, observing different substances reveals critical flame characteristics. Saturated hydrocarbons generally burn with a clean, non-sooty blue flame because their high hydrogen-to-carbon ratio allows complete combustion in adequate air. However, if air vents are partially blocked—as seen in household gas stoves—incomplete combustion occurs, generating a yellow, sooty flame that deposits black unburnt carbon soot on cooking pots and utensils. In contrast, unsaturated hydrocarbons like alkenes and alkynes burn inherently with a smoky yellow flame because their higher carbon percentage cannot undergo complete oxidation in normal air. But why do some substances produce a flame while others merely glow? As explained in 'More to Know!', flames are produced exclusively when gaseous substances burn. Wood or candles contain volatile liquids or solids that vaporise upon heating into combustible gases; once volatile components escape, red-hot charcoal in an angithi glows without a flame, emitting pure radiant infrared heat steadily into the surroundings.",
        "content": {
            "concept": "Combustion of carbon compounds releases heat, light, CO2, and H2O. Saturated hydrocarbons give clean blue flames in excess air; unsaturated hydrocarbons give yellow sooty flames due to high carbon content. Flames require vaporised gases; glowing charcoal lacks volatiles and burns without flame.",
            "formula": "\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O} + \\text{Heat} + \\text{Light}",
            "points": [
                "Combustion is an exothermic oxidation reaction producing CO2, H2O, and substantial energy.",
                "Saturated hydrocarbons burn with a clean blue flame in sufficient oxygen (complete combustion).",
                "Unsaturated hydrocarbons burn with a yellow sooty flame due to incomplete combustion of excess carbon.",
                "Blocked air vents on gas stoves cause incomplete combustion and black soot on utensils.",
                "Flames occur only when vaporised gases burn; charcoal glows without a flame once volatiles are spent."
            ]
        },
        "checkpoints": [
            {
                "question": "Why do cooking pots develop black carbon soot on their bottoms when placed over a gas stove with blocked air vents?",
                "options": [
                    "Restricted air supply causes incomplete combustion, producing unburnt elemental carbon particles (soot)",
                    "The metal pot dissolves into soot under moderate heat",
                    "LPG gas reacts with iron to form black lead sulphide",
                    "Carbon dioxide gas freezes onto the metal surface"
                ],
                "answer": 0,
                "hint": "Insufficient oxygen leads to incomplete combustion rather than clean blue burning.",
                "explanation": "When air inlets are blocked, the oxygen supply is insufficient. Incomplete combustion of saturated hydrocarbons leaves unburnt carbon particles that deposit as black soot on cooking utensils."
            },
            {
                "question": "Why does a piece of burning wood produce a flickering flame initially, whereas glowing charcoal burns without any visible flame?",
                "options": [
                    "Flames are produced only when vaporised gases burn; charcoal has lost its volatile components and glows directly",
                    "Charcoal contains zero carbon atoms",
                    "Wood is a metal, while charcoal is an ionic crystal",
                    "Charcoal absorbs all light waves, creating an optical illusion"
                ],
                "answer": 0,
                "hint": "Only gaseous substances produce a flame when burned.",
                "explanation": "A flame is only observed when gaseous substances burn. Wood vaporises volatile organic components that burn with a flame; once these volatiles are expelled, solid charcoal glows without a flame."
            }
        ]
    },
    {
        "id": 13,
        "title": "Alcohol Oxidation Reactions",
        "subtitle": "Controlled Chemical Oxidation: Potassium Permanganate and Dichromate Reagents",
        "speech": "While combustion represents uncontrolled, destructive oxidation converting carbon skeletons entirely into carbon dioxide and water, organic chemistry also harnesses controlled chemical oxidation to synthesize valuable functional derivatives. Primary alcohols can be oxidized cleanly into carboxylic acids without destroying the carbon skeleton by using potent chemical oxidising agents. An oxidising agent is defined as a substance that is capable of adding oxygen to, or removing hydrogen from, another chemical compound. The two textbook industrial reagents used universally for this transformation are alkaline potassium permanganate, KMnO4, or acidified potassium dichromate, K2Cr2O7. When ethanol, CH3CH2OH, is warmed gently in a laboratory water bath with alkaline potassium permanganate, the distinctive deep purple colour of permanganate gradually discharges as it donates nascent oxygen atoms to the alcohol molecule. Upon continued heating and subsequent acidification, ethanol is cleanly oxidized into ethanoic acid: CH3CH2OH plus two nascent oxygens yields CH3COOH plus H2O. This controlled transformation is fundamental to synthetic organic chemistry: an alcohol containing a single oxygen atom is elevated to a carboxylic acid containing two oxygen atoms. Crucially, the carbon chain length remains completely conserved throughout the entire chemical oxidation reaction, with two-carbon ethanol yielding two-carbon ethanoic acid cleanly and quantitatively.",
        "content": {
            "concept": "Alcohols are oxidized to carboxylic acids using powerful oxidising agents like alkaline KMnO4 (purple) or acidified K2Cr2O7 (orange). Ethanol oxidises to ethanoic acid, conserving the 2-carbon skeleton while adding oxygen and removing hydrogen.",
            "formula": "\\text{CH}_3\\text{CH}_2\\text{OH} \\xrightarrow[\\text{or Acidified } \\text{K}_2\\text{Cr}_2\\text{O}_7 + \\Delta]{\\text{Alkaline } \\text{KMnO}_4 + \\Delta} \\text{CH}_3\\text{COOH} + \\text{H}_2\\text{O}",
            "points": [
                "Controlled oxidation transforms primary alcohols into carboxylic acids without breaking carbon chains.",
                "Oxidising agents supply oxygen to other substances (alkaline KMnO4 and acidified K2Cr2O7).",
                "Ethanol (CH3CH2OH) oxidises into ethanoic acid (CH3COOH).",
                "The purple colour of KMnO4 or orange colour of K2Cr2O7 changes as the reagent is reduced.",
                "This reaction proves that adding oxygen / removing hydrogen is an oxidation process."
            ]
        },
        "checkpoints": [
            {
                "question": "Which of the following chemical reagents serves as a powerful oxidising agent to convert ethanol into ethanoic acid?",
                "options": [
                    "Alkaline potassium permanganate (KMnO4) or acidified potassium dichromate (K2Cr2O7)",
                    "Concentrated hydrochloric acid with zinc dust",
                    "Liquid nitrogen cooled to absolute zero",
                    "Pure distilled water with table salt"
                ],
                "answer": 0,
                "hint": "Look for oxygen-rich transition metal salts that donate oxygen upon heating.",
                "explanation": "Alkaline KMnO4 and acidified K2Cr2O7 are strong oxidising agents that supply oxygen to oxidise alcohols into carboxylic acids upon warming."
            },
            {
                "question": "What happens to the number of carbon atoms when ethanol (CH3CH2OH) undergoes oxidation to form ethanoic acid (CH3COOH)?",
                "options": [
                    "The number of carbon atoms remains exactly two (conserved)",
                    "The carbon chain doubles to four carbons",
                    "One carbon is completely destroyed into gamma rays",
                    "The compound loses all carbon atoms and becomes pure water"
                ],
                "answer": 0,
                "hint": "Ethanol has 2 carbons; ethanoic acid has 2 carbons.",
                "explanation": "Controlled oxidation alters only the functional group (-CH2OH to -COOH); the two-carbon skeleton is fully conserved from ethanol (C2) to ethanoic acid (C2)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Addition Substitution Reactions",
        "subtitle": "Catalytic Hydrogenation of Vegetable Oils and Photochemical Chlorination",
        "speech": "Carbon compounds undergo two hallmark reaction mechanisms that distinguish saturated hydrocarbons from unsaturated hydrocarbons: addition reactions and substitution reactions. Addition reactions are the exclusive domain of unsaturated hydrocarbons. Because alkenes and alkynes possess reactive multiple bonds, they can add reagents across double or triple bonds to yield saturated products without eliminating any atoms. A monumental industrial application is catalytic hydrogenation: unsaturated vegetable oils containing long, healthy polyunsaturated liquid hydrocarbon chains are reacted with hydrogen gas at elevated temperature in the presence of a finely divided metallic nickel or palladium catalyst. The double bonds open up completely, adding hydrogen atoms across adjacent carbons to yield solid, saturated fats like vanaspati ghee or commercial margarine spread. Conversely, saturated hydrocarbons, having only single bonds, cannot undergo addition reactions under any normal conditions. Instead, alkanes undergo substitution reactions in the presence of ultraviolet sunlight. In diffuse sunlight, highly reactive chlorine radicals replace hydrogen atoms on methane one by one: CH4 plus Cl2 yields chloromethane, CH3Cl, plus HCl. As chlorination proceeds, successive substitutions yield dichloromethane, chloroform, and finally carbon tetrachloride. Saturated alkanes are normally unreactive, but photochemical substitution enables their chemical functionalisation and derivatisation cleanly in modern industrial chemical synthesis.",
        "content": {
            "concept": "Addition reactions: Unsaturated hydrocarbons add reagents across double/triple bonds with Ni/Pd catalyst (e.g., hydrogenation of vegetable oils into saturated fats). Substitution reactions: Saturated alkanes replace hydrogen atoms with halogens in the presence of sunlight (e.g., CH4 + Cl2 → CH3Cl + HCl).",
            "formula": "\\text{Addition: } \\text{R}_2\\text{C}=\\text{CR}_2 + \\text{H}_2 \\xrightarrow{\\text{Ni Catalyst}} \\text{R}_2\\text{CH}-\\text{CHR}_2 \\quad | \\quad \\text{Substitution: } \\text{CH}_4 + \\text{Cl}_2 \\xrightarrow{h\\nu} \\text{CH}_3\\text{Cl} + \\text{HCl}",
            "points": [
                "Addition reactions occur exclusively in unsaturated hydrocarbons (alkenes, alkynes).",
                "Industrial hydrogenation: vegetable oils (unsaturated liquids) + H2 + Ni catalyst → saturated fats (solids).",
                "Saturated fats are considered less healthy for human cardiovascular consumption than unsaturated oils.",
                "Substitution reactions occur in saturated hydrocarbons in the presence of sunlight.",
                "Methane undergoes progressive photochemical chlorination: CH4 → CH3Cl → CH2Cl2 → CHCl3 → CCl4."
            ]
        },
        "checkpoints": [
            {
                "question": "What catalyst and reactant gas are utilised industrially to convert liquid unsaturated vegetable oils into solid saturated fats?",
                "options": [
                    "Hydrogen gas in the presence of a nickel (Ni) catalyst",
                    "Carbon dioxide gas in the presence of gold foil",
                    "Helium gas in the presence of iron oxide",
                    "Chlorine gas in the presence of copper wire"
                ],
                "answer": 0,
                "hint": "Addition of H2 across double bonds is termed hydrogenation, catalysed by Ni or Pd.",
                "explanation": "Catalytic hydrogenation uses hydrogen gas (H2) in the presence of a nickel (Ni) catalyst to saturate the double bonds of liquid vegetable oils into solid saturated fats."
            },
            {
                "question": "Why does methane react with chlorine gas only in the presence of sunlight (ultraviolet light)?",
                "options": [
                    "Light energy dissociates chlorine molecules into reactive free radicals to initiate substitution",
                    "Sunlight melts the methane gas into liquid metal",
                    "Sunlight converts chlorine into pure oxygen gas",
                    "Methane freezes instantly in dark rooms and cannot move"
                ],
                "answer": 0,
                "hint": "UV radiation provides the activation energy to split the Cl-Cl bond into chlorine radicals.",
                "explanation": "The substitution reaction of methane with chlorine requires sunlight (photochemical activation) to cleave Cl2 molecules into highly reactive chlorine free radicals that displace hydrogen atoms."
            }
        ]
    },
    {
        "id": 15,
        "title": "Ethanol Chemical Properties",
        "subtitle": "Solvent Versatility, Physiological Hazards, Sodium Reaction, and Acid Dehydration",
        "speech": "Ethanol, formula C2H5OH, is the second member of the homologous alcohol series and a compound of immense industrial and physiological importance. At room temperature, pure ethanol is a volatile, colourless liquid with a distinct pleasant odour and a boiling point of 351 Kelvin. Ethanol is completely miscible with water in all proportions and is a superb industrial solvent, utilised extensively in medicines such as tincture of iodine, cough syrups, and invigorating health tonics. However, ethanol ingestion causes grave physiological harm: consuming dilute alcohol depresses the central nervous system, impairing motor coordination, judgment, and emotional restraint. Consuming pure absolute alcohol can be fatal. Furthermore, ingesting toxic methanol causes blindness and rapid death because methanol is metabolised in the liver into methanal, which reacts rapidly with cellular protoplasm, coagulating it like cooked egg albumen. To prevent the misuse of industrial alcohol, it is denatured by adding poisonous methanol and blue dyes. Chemically, ethanol undergoes two classic reactions. First, reacting ethanol with metallic sodium liberates bubbles of flammable hydrogen gas: two Na plus two CH3CH2OH yields sodium ethoxide plus H2. Second, heating ethanol at 443 Kelvin with excess concentrated sulphuric acid dehydrates ethanol into ethene and water cleanly and reliably.",
        "content": {
            "concept": "Ethanol (C2H5OH) is a versatile solvent and medicine base. Ingestion depresses the central nervous system. Methanol is extremely toxic (causes blindness/death by coagulating cell protoplasm). Denatured alcohol contains methanol and dyes. Reactions: with Na produces sodium ethoxide + H2; dehydration with hot conc. H2SO4 at 443 K yields ethene.",
            "formula": "2\\text{Na} + 2\\text{C}_2\\text{H}_5\\text{OH} \\rightarrow 2\\text{C}_2\\text{H}_5\\text{ONa} + \\text{H}_2\\uparrow \\quad | \\quad \\text{C}_2\\text{H}_5\\text{OH} \\xrightarrow[443\\text{ K}]{\\text{Hot Conc. H}_2\\text{SO}_4} \\text{CH}_2=\\text{CH}_2 + \\text{H}_2\\text{O}",
            "points": [
                "Ethanol is a liquid at room temperature (bp 351 K), miscible with water, used in medicines and tonics.",
                "CNS depressant; absolute alcohol is lethal; methanol intake causes blindness/death via methanal protoplasm coagulation.",
                "Denatured alcohol: industrial alcohol mixed with toxic methanol and blue dyes to prevent drinking.",
                "Reaction with sodium: 2Na + 2C2H5OH → 2C2H5ONa (sodium ethoxide) + H2 (pop test).",
                "Acid dehydration: Heating ethanol with excess conc. H2SO4 at 443 K removes water to form ethene (alkene)."
            ]
        },
        "checkpoints": [
            {
                "question": "What gas is evolved when a small piece of metallic sodium is dropped into absolute ethanol?",
                "options": [
                    "Hydrogen gas (burns with a characteristic pop sound)",
                    "Carbon dioxide gas (turns lime water milky)",
                    "Chlorine gas (bleaches litmus paper)",
                    "Oxygen gas (rekindles a glowing splint)"
                ],
                "answer": 0,
                "hint": "2Na + 2CH3CH2OH -> 2CH3CH2ONa + H2.",
                "explanation": "Active metals like sodium react with ethanol to evolve hydrogen gas along with sodium ethoxide (2Na + 2C2H5OH -> 2C2H5ONa + H2)."
            },
            {
                "question": "What role does hot concentrated sulphuric acid play when heated with ethanol at 443 Kelvin?",
                "options": [
                    "It acts as a dehydrating agent, removing water to produce ethene",
                    "It acts as an oxidising agent, converting ethanol into diamond",
                    "It acts as a freezing agent, turning ethanol into ice",
                    "It neutralises ethanol into table salt"
                ],
                "answer": 0,
                "hint": "Removal of a water molecule (H2O) from an alcohol is called dehydration.",
                "explanation": "Hot concentrated H2SO4 acts as a powerful dehydrating agent, stripping a molecule of water from ethanol at 443 K to synthesize ethene (CH3CH2OH -> CH2=CH2 + H2O)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Ethanoic Acid Chemistry",
        "subtitle": "Glacial Acetic Acid, Fruity Esterification, Saponification, and Carbonate Fizz",
        "speech": "Ethanoic acid, commonly called acetic acid, formula CH3COOH, belongs to the carboxylic acid family and is a foundational commercial chemical. A five to eight percent aqueous solution of ethanoic acid is universally known as vinegar, used widely as a culinary preservative in pickles. Pure anhydrous ethanoic acid possesses a melting point of 290 Kelvin; consequently, during cold winter climates in northern India, it readily freezes into an ice-like crystalline solid, earning the historic name glacial acetic acid. Ethanoic acid is a weak organic acid that ionises only partially in water, distinguishing it from strongly dissociated mineral acids like hydrochloric acid. In Activities 4.7 and 4.8, warming ethanol and glacial ethanoic acid together in a water bath with a few drops of concentrated sulphuric acid produces a delightfully sweet, fruity fragrance. This reaction is esterification: ethanoic acid reacts with ethanol to yield ethyl ethanoate ester and water. When esters are heated with sodium hydroxide base, they hydrolyse back into alcohol and sodium carboxylate soap, a reaction termed saponification. Furthermore, reacting ethanoic acid with sodium carbonate or hydrogencarbonate produces vigorous effervescence of carbon dioxide gas, providing a definitive laboratory test to distinguish carboxylic acids from neutral alcohols in analytical chemistry.",
        "content": {
            "concept": "Ethanoic acid (CH3COOH) is a weak acid. Vinegar is 5-8% solution; pure acid freezes at 290 K (glacial acetic acid). Esterification: reacts with ethanol + conc H2SO4 to form sweet-smelling ethyl ethanoate. Saponification: alkaline hydrolysis of esters produces soaps. Reacts with carbonates/bicarbonates to release CO2 gas.",
            "formula": "\\text{Esterification: } \\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH} \\xrightleftharpoons{\\text{H}^+} \\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O} \\quad | \\quad 2\\text{CH}_3\\text{COOH} + \\text{Na}_2\\text{CO}_3 \\rightarrow 2\\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow",
            "points": [
                "Vinegar is a 5-8% solution of ethanoic acid in water used as a food preservative.",
                "Glacial acetic acid: pure ethanoic acid freezes into solid crystals at 290 K (17°C).",
                "Esterification: Ethanoic acid + Ethanol (with conc. H2SO4) → Sweet-smelling ester (ethyl ethanoate).",
                "Saponification: Alkaline ester hydrolysis with NaOH yields soap (sodium carboxylate) and alcohol.",
                "Reaction with carbonates: 2CH3COOH + Na2CO3 → 2CH3COONa + H2O + CO2 (brisk effervescence)."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the distinctive sensory observation indicating that an esterification reaction has taken place in Activity 4.7?",
                "options": [
                    "A delightful, sweet, fruity aroma permeates the beaker",
                    "A pungent odour of rotten eggs fills the room",
                    "The solution explodes with a blinding purple flash",
                    "A dense green toxic cloud of chlorine is liberated"
                ],
                "answer": 0,
                "hint": "Esters are used in perfumes and artificial fruit flavourings due to their pleasant smell.",
                "explanation": "Esters possess characteristic sweet, fruity fragrances. When ethanoic acid reacts with ethanol in the presence of acid catalyst, the formation of ethyl ethanoate is confirmed by its sweet aroma."
            },
            {
                "question": "Which chemical test experimentally distinguishes a sample of ethanoic acid from a sample of ethanol in the laboratory?",
                "options": [
                    "Adding sodium hydrogencarbonate (NaHCO3): ethanoic acid causes brisk effervescence of CO2, while ethanol shows no reaction",
                    "Testing with a magnet: ethanoic acid is magnetic, while ethanol is not",
                    "Exposing to sound: ethanoic acid rings like a bell, while ethanol is silent",
                    "Measuring mass: ethanol weighs zero grams per mole"
                ],
                "answer": 0,
                "hint": "Carboxylic acids liberate carbon dioxide gas from metal carbonates and hydrogencarbonates.",
                "explanation": "Ethanoic acid reacts with sodium hydrogencarbonate (or sodium carbonate) to produce brisk effervescence of carbon dioxide gas (which turns lime water milky): CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2. Neutral ethanol does not react."
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides:
        words = s["speech"].split()
        wc = len(words)
        print(f"Slide {s['id']} ({s['title']}): {wc} words")
        assert 195 <= wc <= 215, f"Slide {s['id']} word count {wc} out of range [195, 215]"
        assert len(s["title"].split()) <= 3, f"Slide {s['id']} title '{s['title']}' has > 3 words"
    print("All slides 9 to 16 validated successfully!")

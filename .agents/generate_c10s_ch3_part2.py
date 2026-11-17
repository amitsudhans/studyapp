"""Generate Slides 9 to 16 for Class 10 Science Chapter 3: Metals and Non-metals
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
        "title": "Ionic Bond Formation",
        "subtitle": "Octet Stability, Complete Electron Transfer, and Electrostatic Crystal Lattices",
        "speech": "Why do chemical elements combine, and what dictates how metals interact with non-metals? Chemical reactivity is governed by the universal driving force of atoms to attain a completely filled valence electron shell, mimicking the ultra-stable electronic configuration of noble gases like helium, neon, and argon. Metals possess few valence electrons—typically one, two, or three—and tend to lose these electrons easily to form positively charged cations. Conversely, non-metals possess five, six, or seven valence electrons and readily gain electrons to complete their octet, forming negatively charged anions. The chemical bond formed by the complete transfer of valence electrons from a metal atom to a non-metal atom is termed an ionic or electrovalent bond. Consider the synthesis of sodium chloride: a neutral sodium atom with configuration two, eight, one surrenders its solitary valence electron to become a stable sodium cation, Na plus. A neutral chlorine atom with configuration two, eight, seven captures this transferred electron, transforming into a chloride anion, Cl minus, with configuration two, eight, eight. Similarly, magnesium transfers two valence electrons to two chlorine atoms, yielding magnesium chloride. These oppositely charged ions attract each other through powerful, non-directional electrostatic forces, assembling into a rigid, repeating three-dimensional cubic crystal lattice of sodium chloride.",
        "content": {
            "concept": "Atoms react to achieve a stable noble gas octet. Metals donate valence electrons to form cations; non-metals accept electrons to form anions. The electrostatic attraction between oppositely charged ions forms an ionic (electrovalent) bond.",
            "formula": "\\text{Na } (2,8,1) \\rightarrow \\text{Na}^+ (2,8) + e^- \\quad | \\quad \\text{Cl } (2,8,7) + e^- \\rightarrow \\text{Cl}^- (2,8,8) \\quad | \\quad \\text{Na}^+ + \\text{Cl}^- \\rightarrow \\text{NaCl}",
            "points": [
                "Reactivity is driven by the tendency to achieve a stable noble gas octet configuration.",
                "Metals lose electrons to form cations; non-metals gain electrons to form anions.",
                "Ionic/electrovalent bonds are formed by the complete transfer of electrons from metal to non-metal.",
                "Formation of NaCl: Na (2,8,1) transfers 1 electron to Cl (2,8,7), yielding Na+ and Cl-.",
                "Formation of MgCl2: Mg (2,8,2) transfers 2 electrons to two Cl atoms, yielding Mg2+ and 2Cl-.",
                "Oppositely charged ions are bound together by strong electrostatic attractive forces."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the primary thermodynamic driving force that compels metals and non-metals to react chemically?",
                "options": [
                    "The tendency to lose all nuclear protons and neutrons",
                    "The tendency to attain a completely filled valence shell octet like noble gases",
                    "The desire to convert into volatile hydrocarbon gases",
                    "The tendency to increase electrical resistance to infinity"
                ],
                "answer": 1,
                "hint": "Atoms seek the stable electronic configurations of inert gases like Ne and Ar.",
                "explanation": "Atoms react to attain a completely filled outer valence shell, achieving the stable electronic configuration (octet) of noble gases."
            },
            {
                "question": "How many electrons are transferred from a single magnesium atom during the formation of magnesium chloride (MgCl2)?",
                "options": [
                    "One electron transferred to one chlorine atom",
                    "Two electrons transferred, one to each of two chlorine atoms",
                    "Three electrons shared equally in a covalent triple bond",
                    "Four electrons accepted from atmospheric oxygen"
                ],
                "answer": 1,
                "hint": "Magnesium has valence configuration 2,8,2 and needs to lose two electrons.",
                "explanation": "Magnesium (2,8,2) loses two valence electrons to form Mg2+. Each of the two chlorine atoms (2,8,7) accepts one electron to form Cl-, producing MgCl2."
            }
        ]
    },
    {
        "id": 10,
        "title": "Ionic Compound Properties",
        "subtitle": "Crystal Brittleness, Thermal Lattice Enthalpy, Solvent Polarity, and Electrolysis",
        "speech": "The powerful electrostatic forces binding cations and anions endow ionic compounds with four distinctive physical and chemical characteristics, explored systematically in Activity 3.13. First, regarding physical nature, ionic compounds are crystalline solids that are notably hard due to strong inter-ionic attractions; however, they are mechanically brittle and fracture into pieces when subjected to shear stress because like-charged ions are forced alongside one another, causing violent electrostatic repulsion. Second, ionic compounds boast extraordinarily high melting and boiling points; for instance, sodium chloride melts at 1074 Kelvin and boils at 1686 Kelvin, while calcium oxide melts at an astonishing 2850 Kelvin. Overcoming the immense lattice energy of interlocking electrostatic bonds demands vast amounts of thermal kinetic energy. Third, regarding solubility, ionic compounds dissolve readily in polar solvents like water, where polar water molecules solvate and separate the ions; however, they are completely insoluble in non-polar organic solvents such as petrol, kerosene, and benzene. Finally, regarding electrical conductivity, solid ionic compounds cannot conduct electricity because their rigid crystal lattice locks constituent ions firmly and rigidly in place; conversely, when dissolved in aqueous solutions or melted into liquid molten state, the ions become completely mobile, migrating freely toward oppositely charged electrodes.",
        "content": {
            "concept": "Ionic compounds are hard, brittle crystalline solids with high melting and boiling points due to strong lattice attractions. They dissolve in polar water but not non-polar solvents. They conduct electricity only in molten or aqueous states where ions move freely.",
            "formula": "\\text{NaCl: Melting Point } 1074\\text{ K, Boiling Point } 1686\\text{ K} \\quad | \\quad \\text{CaO: Melting Point } 2850\\text{ K}",
            "points": [
                "Activity 3.13: Ionic compounds are hard and brittle; crystal layers shear under mechanical stress.",
                "High melting and boiling points stem from the enormous energy required to overcome ionic attractions.",
                "Ionic salts dissolve in polar water via hydration, but are insoluble in petrol and kerosene.",
                "Solid ionic compounds do not conduct electricity because ions are fixed in rigid lattice positions.",
                "Molten and aqueous states conduct electricity freely due to mobile dissociated cations and anions."
            ]
        },
        "checkpoints": [
            {
                "question": "Why do solid ionic compounds like sodium chloride fail to conduct electricity, whereas their aqueous solutions conduct readily?",
                "options": [
                    "Solid crystals contain no electrons or protons whatsoever",
                    "In the solid state, ions are locked rigidly in the crystal lattice and cannot migrate",
                    "Solid sodium chloride converts into an insulating gaseous plastic layer",
                    "Aqueous solutions destroy all ionic charges permanently"
                ],
                "answer": 1,
                "hint": "Electrical conduction requires mobile charge carriers. In solids, ions cannot move.",
                "explanation": "In solid state, strong electrostatic forces hold ions in fixed positions in the crystal lattice. In aqueous solution or molten state, ions dissociate and move freely to conduct electric current."
            },
            {
                "question": "Why do ionic compounds shatter into fragments when struck with a heavy mechanical hammer?",
                "options": [
                    "Impact forces like-charged ions into alignment, causing intense electrostatic repulsion",
                    "The hammer transfers protons that boil the compound into steam",
                    "Ionic crystals contain tiny trapped air pockets that explode mechanically",
                    "Hammering converts ionic bonds into weak temporary covalent bonds"
                ],
                "answer": 0,
                "hint": "Shearing the crystal brings positive ions next to positive ions and negative next to negative.",
                "explanation": "When an ionic crystal is struck, crystal layers slide slightly, bringing ions of the same charge into direct proximity. The resulting electrostatic repulsion shatters the crystal lattice (brittleness)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Mineral Ore Metallurgy",
        "subtitle": "Crustal Minerals, Economic Ores, Gangue Dressing, and Extraction Strategies",
        "speech": "Metals are foundational to human industry, but how are they harvested from the natural environment? Chemical elements and compounds found naturally in the Earth's crust are designated as minerals. When a specific mineral contains an exceptionally high concentration of a valuable metal that can be extracted profitably and economically, that mineral is termed an ore. For instance, bauxite is the primary commercial ore of aluminium, and cinnabar is the ore of mercury. Mined ores are invariably contaminated with substantial quantities of undesirable rocky, earthy impurities such as sand, silica, and clay, which are collectively termed gangue. Metallurgy is the multi-step scientific and technological domain encompassing ore concentration, chemical reduction, and electrolytic refining. Metallurgical extraction strategies are dictated strictly by a metal's position in the reactivity series. Metals situated at the bottom of the series, such as gold and silver, occur in native, uncombined elemental state and require minimal chemical processing. Moderately reactive metals in the middle, including zinc, iron, and lead, occur as sulphides, carbonates, or oxides, extracted through pyrometallurgical roasting, calcination, and carbon reduction. Highly reactive metals at the top, like sodium and aluminium, bind so tenaciously to oxygen that they necessitate powerful molten electrolytic reduction.",
        "content": {
            "concept": "Minerals are naturally occurring crustal compounds; ores are minerals from which metals can be profitably extracted; gangue refers to undesirable rocky impurities. Extraction methods depend on reactivity: low (thermal), medium (roasting/calcination + reduction), high (electrolysis).",
            "formula": "\\text{Mined Ore} = \\text{Valuable Mineral} + \\text{Unwanted Gangue (Sand, Clay, Rocks)}",
            "points": [
                "Minerals are natural inorganic crustal substances; ores yield metals profitably.",
                "Gangue comprises soil, sand, and rocky impurities that must be removed during concentration.",
                "Low reactivity metals (Au, Pt, Cu) occur native or are extracted by simple heating of sulphides.",
                "Medium reactivity metals (Zn, Fe, Pb) occur as oxides, sulphides, or carbonates; reduced with carbon or Al.",
                "High reactivity metals (K, Na, Ca, Mg, Al) are extracted exclusively by electrolytic reduction of molten salts."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the defining distinction between a naturally occurring mineral and an ore in industrial chemistry?",
                "options": [
                    "Minerals are artificial laboratory syntheses, whereas ores are always biological fossils",
                    "An ore is a mineral containing a sufficiently high percentage of metal to extract profitably",
                    "Minerals contain exclusively noble gases, whereas ores contain toxic heavy metals",
                    "There is no chemical or economic distinction between minerals and ores"
                ],
                "answer": 1,
                "hint": "All ores are minerals, but only commercially profitable minerals qualify as ores.",
                "explanation": "A mineral is any naturally occurring chemical compound in the earth. An ore is a specific mineral that contains a high concentration of a metal that can be extracted economically and profitably."
            },
            {
                "question": "What term is used in metallurgy to describe unwanted commercial contaminants like sand, clay, and rocky impurities in mined ore?",
                "options": [
                    "Flux",
                    "Slag",
                    "Gangue",
                    "Anode mud"
                ],
                "answer": 2,
                "hint": "These matrix impurities must be removed during the enrichment/concentration of the ore.",
                "explanation": "Gangue refers to the commercially useless rocky, sandy, and earthy impurities associated with mined ores that must be separated during ore dressing."
            }
        ]
    },
    {
        "id": 12,
        "title": "Low Reactivity Metallurgy",
        "subtitle": "Thermal Roasting of Cinnabar, Auto-Reduction of Copper Glance, and Native Metals",
        "speech": "Metals residing towards the bottom of the reactivity series exhibit very low chemical affinity for non-metallic elements, making their extraction chemically straightforward. The least reactive metals, such as gold and platinum, are found predominantly in free native elemental state in alluvial river sands and rock veins. Copper and silver also occur in native form, but are more widely distributed as sulphide and oxide minerals. Metals low in the activity series are extracted through simple thermal reduction by heating their sulphide ores in air. Consider the extraction of mercury from its primary ore, cinnabar, which is mercuric sulphide, HgS. When cinnabar is roasted strongly in excess air, it first oxidises into mercuric oxide: two mercuric sulphide plus three oxygen yields two mercuric oxide plus two sulphur dioxide. Upon further heating above three hundred degrees Celsius, unstable mercuric oxide decomposes automatically into pure liquid metallic mercury and oxygen gas: two mercuric oxide yields two mercury plus oxygen. Similarly, copper is extracted from its sulphide ore, copper glance, Cu2S. Heating copper glance in air oxidises part of it to cuprous oxide. When air is restricted, the remaining copper sulphide undergoes auto-reduction with cuprous oxide, yielding molten blister copper and sulphur dioxide gas.",
        "content": {
            "concept": "Metals low in the activity series (Hg, Cu) are extracted by heating their sulphide ores in air (thermal roasting followed by auto-reduction). Mercury is obtained from cinnabar (HgS); copper is obtained from copper glance (Cu2S).",
            "formula": "2\\text{HgS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{HgO} + 2\\text{SO}_2 \\quad | \\quad 2\\text{HgO} \\xrightarrow{\\Delta} 2\\text{Hg}(l) + \\text{O}_2 \\quad | \\quad 2\\text{Cu}_2\\text{O} + \\text{Cu}_2\\text{S} \\xrightarrow{\\Delta} 6\\text{Cu} + \\text{SO}_2",
            "points": [
                "Cinnabar (HgS) is the sulphide ore of mercury.",
                "Heating cinnabar in air oxidises it to HgO, which thermally decomposes into liquid mercury: Hg.",
                "Copper glance (Cu2S) is roasted to cuprous oxide (Cu2O).",
                "Auto-reduction: 2Cu2O + Cu2S → 6Cu + SO2 produces crude blister copper.",
                "Gold and platinum sit at the very bottom and are mined directly in native elemental form."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the mineral name and chemical formula of the primary ore used to extract metallic mercury?",
                "options": [
                    "Bauxite (Al2O3·2H2O)",
                    "Cinnabar (HgS)",
                    "Haematite (Fe2O3)",
                    "Galena (PbS)"
                ],
                "answer": 1,
                "hint": "This red sulphide mineral converts to mercuric oxide upon heating in air.",
                "explanation": "Cinnabar is mercuric sulphide (HgS), the primary commercial ore from which metallic mercury is extracted through thermal roasting in air."
            },
            {
                "question": "How is metallic copper produced from cuprous oxide (Cu2O) during the smelting of copper glance?",
                "options": [
                    "By adding concentrated nitric acid as a chemical reducing agent",
                    "By reacting cuprous oxide with remaining copper sulphide (auto-reduction)",
                    "By electrolysing cold aqueous copper carbonate",
                    "By bubbling pure hydrogen gas through molten rock salt"
                ],
                "answer": 1,
                "hint": "The oxide and sulphide react together: 2Cu2O + Cu2S -> 6Cu + SO2.",
                "explanation": "In copper metallurgy, unoxidised Cu2S reacts directly with formed Cu2O at high temperatures in an auto-reduction process: 2Cu2O + Cu2S -> 6Cu + SO2."
            }
        ]
    },
    {
        "id": 13,
        "title": "Moderate Reactivity Metallurgy",
        "subtitle": "Roasting Sulphides, Calcining Carbonates, Carbon Reduction, and Thermit Welding",
        "speech": "Metals situated in the middle of the reactivity series—such as zinc, iron, and lead—occur naturally as sulphides or carbonates. Because reducing metal oxides is far easier than reducing sulphides or carbonates, ores must first be converted into metallic oxides using two distinct pyrometallurgical techniques: roasting and calcination. Roasting involves heating sulphide ores strongly below their melting points in excess air; for example, roasting zinc blende yields zinc oxide and sulphur dioxide: two ZnS plus three O2 yields two ZnO plus two SO2. Conversely, calcination involves heating carbonate ores strongly in limited or absent air to drive off volatile carbon dioxide; calcining calamine yields zinc oxide: ZnCO3 yields ZnO plus CO2. Once obtained, the zinc oxide is reduced to free metal using a chemical reducing agent like carbon coke: zinc oxide plus carbon yields zinc plus carbon monoxide. Alternatively, highly reactive metals like aluminium, sodium, and calcium serve as potent reducing agents through displacement. A famous industrial application is the Thermit reaction: reacting iron(III) oxide with aluminium powder releases so much thermal energy that the produced iron melts into a white-hot liquid stream at over three thousand degrees, used directly to weld cracked railway tracks securely in heavy transport infrastructure.",
        "content": {
            "concept": "Moderate reactivity ores are converted to oxides via roasting (sulphides heated in excess air) or calcination (carbonates heated in limited air). Oxides are reduced using carbon (coke) or reactive metals (Al). The Thermit reaction produces molten iron to weld railway tracks.",
            "formula": "\\text{Roasting: } 2\\text{ZnS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{ZnO} + 2\\text{SO}_2 \\quad | \\quad \\text{Thermit: } \\text{Fe}_2\\text{O}_3 + 2\\text{Al} \\rightarrow 2\\text{Fe}(l) + \\text{Al}_2\\text{O}_3 + \\text{Heat}",
            "points": [
                "Roasting: Sulphide ores heated strongly in excess air convert to oxides, releasing SO2 gas.",
                "Calcination: Carbonate ores heated in limited air decompose to oxides, driving off CO2 gas.",
                "Reduction with carbon: ZnO + C → Zn + CO reduces zinc oxide using inexpensive coke.",
                "Displacement reduction: Highly reactive metals like Al displace metals from oxides with immense heat.",
                "Thermit reaction: Fe2O3 + 2Al → 2Fe(l) + Al2O3 + Heat produces molten iron to weld railway tracks."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the critical chemical difference between roasting and calcination in metallurgical processing?",
                "options": [
                    "Roasting heats sulphides in excess air; calcination heats carbonates in limited air",
                    "Roasting dissolves ores in water; calcination boils ores in concentrated acid",
                    "Roasting cools ores to zero Kelvin; calcination vaporizes ores into noble gases",
                    "There is no difference; roasting and calcination are identical synonyms"
                ],
                "answer": 0,
                "hint": "Consider the presence of excess atmospheric oxygen vs limited oxygen supply.",
                "explanation": "Roasting is the process of heating sulphide ores strongly in excess air to form oxides (releasing SO2). Calcination heats carbonate ores in limited or no air to expel CO2."
            },
            {
                "question": "What unique physical state of iron is produced during the highly exothermic aluminothermic Thermit reaction?",
                "options": [
                    "Solid iron powder suspended in liquid nitrogen",
                    "Molten liquid iron that flows into track joints to weld them",
                    "Volatile gaseous iron vapor that coats the railway ties",
                    "Magnetic iron carbonate rust flakes"
                ],
                "answer": 1,
                "hint": "The extreme heat evolved (>2500°C) exceeds the melting point of elemental iron.",
                "explanation": "The reaction Fe2O3 + 2Al -> 2Fe(l) + Al2O3 + Heat releases immense energy, producing iron in molten liquid state, which is poured directly into gaps to weld railway tracks."
            }
        ]
    },
    {
        "id": 14,
        "title": "Electrolytic Metal Extraction",
        "subtitle": "High Affinity Metals, Carbon Inadequacy, and Molten Salt Decomposition",
        "speech": "Metals positioned near the top of the reactivity series—including potassium, sodium, calcium, magnesium, and aluminium—possess extraordinarily high chemical affinity for oxygen and halogens. Consequently, their metal oxides cannot be reduced using common carbon coke, because these electropositive metals hold onto oxygen far more tenaciously than carbon does. Attempting to heat aluminium oxide with carbon fails completely because carbon lacks the reducing potential to strip oxygen away from aluminium. To extract these high-affinity metals, industrial metallurgy employs electrolytic reduction of their anhydrous molten salts. For example, metallic sodium is manufactured through the Down's cell electrolysis of molten sodium chloride. In the molten state, sodium and chloride ions are fully mobile. When an electric current is passed through molten sodium chloride using inert electrodes, positively charged sodium cations migrate toward the negative cathode, where each ion accepts an electron to deposit as pure molten metallic sodium: Na plus plus electron yields sodium metal. Simultaneously, negatively charged chloride anions migrate toward the positive anode, surrendering electrons to evolve as greenish-yellow chlorine gas: two Cl minus yields chlorine gas plus two electrons. Aluminium is similarly extracted by electrolysing purified molten aluminium oxide dissolved in molten cryolite solvent to lower its extreme operational melting point.",
        "content": {
            "concept": "Highly reactive metals (K, Na, Ca, Mg, Al) have greater affinity for oxygen than carbon and cannot be reduced by carbon. They are extracted via electrolytic reduction of their molten salts (e.g., molten NaCl yields Na at cathode and Cl2 at anode).",
            "formula": "\\text{Cathode (-): } \\text{Na}^+ + e^- \\rightarrow \\text{Na}(l) \\quad | \\quad \\text{Anode (+): } 2\\text{Cl}^- \\rightarrow \\text{Cl}_2(g)\\uparrow + 2e^-",
            "points": [
                "Metals at top of activity series (K, Na, Ca, Mg, Al) cannot be reduced by carbon.",
                "These metals have much higher chemical affinity for oxygen than carbon does.",
                "Extracted by electrolytic reduction of molten chlorides or oxides (never aqueous solutions).",
                "Electrolysis of molten NaCl: Pure sodium deposits at the cathode (reduction).",
                "Chlorine gas is liberated at the anode (oxidation): 2Cl- → Cl2 + 2e-.",
                "Aluminium is extracted by electrolysing molten bauxite alumina (Al2O3) dissolved in cryolite."
            ]
        },
        "checkpoints": [
            {
                "question": "Why can metallic sodium or aluminium not be extracted by heating their oxides with carbon coke in a blast furnace?",
                "options": [
                    "Carbon reacts violently with iron walls and explodes before heating",
                    "Sodium and aluminium have a much higher chemical affinity for oxygen than carbon does",
                    "Carbon coke is too expensive for industrial manufacturing applications",
                    "Sodium and aluminium convert into radioactive isotopes when mixed with carbon"
                ],
                "answer": 1,
                "hint": "Carbon cannot reduce oxides of metals positioned higher than itself in affinity.",
                "explanation": "High-reactivity metals (Na, Mg, Al) have a much greater affinity for oxygen than carbon does. Therefore, carbon cannot reduce their oxides; electrolytic reduction of molten salts is required."
            },
            {
                "question": "At which electrode does pure metallic sodium deposit during the electrolysis of molten sodium chloride?",
                "options": [
                    "At the positive anode",
                    "At the negative cathode",
                    "At the bottom of the electrolyte as anode mud",
                    "In the gaseous phase above the anode"
                ],
                "answer": 1,
                "hint": "Cations carry positive charge and migrate toward the negative electrode where they gain electrons.",
                "explanation": "Positively charged sodium ions (Na+) migrate to the negative cathode, where they gain electrons (reduction) to deposit as metallic sodium: Na+ + e- -> Na."
            }
        ]
    },
    {
        "id": 15,
        "title": "Electrolytic Copper Refining",
        "subtitle": "Impure Anode Dissolution, Pure Cathode Plating, and Precious Anode Mud",
        "speech": "Metals obtained through pyrometallurgical reduction processes invariably contain residual impurities and must undergo purification to achieve commercial and electrical grades. The most widely used technique for refining crude metals like copper, zinc, tin, nickel, silver, and gold is electrolytic refining. In the electrolytic refining of copper, an electrolytic tank is configured with three essential components: a thick slab of crude, impure blister copper serves as the positive anode; a thin, pristine sheet of pure copper acts as the negative cathode; and an aqueous solution of acidified copper(II) sulphate serves as the conducting electrolyte bath. When direct electric current passes through the cell, copper atoms from the impure anode lose two electrons each, dissolving into the electrolyte solution as divalent copper cations: Cu yields Cu2+ plus two electrons. Simultaneously, an equivalent quantity of pure copper ions from the electrolyte migrate to the negative cathode, gaining two electrons to plate out as a uniform layer of ultra-pure metallic copper. Soluble impurities remain dissolved in the acidic electrolyte bath. Crucially, insoluble impurities—including valuable trace noble metals like gold, silver, and platinum—fall away from the dissolving anode and settle at the tank floor as anode mud, which is collected profitably.",
        "content": {
            "concept": "Electrolytic refining purifies crude metals. In copper refining, the anode is impure copper, the cathode is pure copper, and the electrolyte is acidified CuSO4. Pure copper transfers to the cathode; insoluble impurities settle as anode mud containing gold and silver.",
            "formula": "\\text{Anode: } \\text{Cu}(s) \\rightarrow \\text{Cu}^{2+}(aq) + 2e^- \\quad | \\quad \\text{Cathode: } \\text{Cu}^{2+}(aq) + 2e^- \\rightarrow \\text{Cu}(s) [\\text{Pure}]",
            "points": [
                "Electrolytic refining purifies crude metals (Cu, Zn, Sn, Ni, Ag, Au).",
                "Anode (+): Thick slab of impure blister copper.",
                "Cathode (-): Thin strip of pure refined copper.",
                "Electrolyte: Acidified aqueous copper sulphate (CuSO4) solution.",
                "Pure copper dissolves from anode and plates out on cathode with 99.99% purity.",
                "Insoluble impurities settle beneath the anode as valuable anode mud containing Ag, Au, and Pt."
            ]
        },
        "checkpoints": [
            {
                "question": "In the electrolytic refining of copper, what material constitutes the positive anode and the negative cathode?",
                "options": [
                    "Anode is pure copper; cathode is impure copper",
                    "Anode is impure copper; cathode is a thin strip of pure copper",
                    "Anode is platinum; cathode is graphite",
                    "Both electrodes consist of identical stainless steel plates"
                ],
                "answer": 1,
                "hint": "The impure metal must dissolve into solution from the positive electrode.",
                "explanation": "In electrolytic refining, the impure metal slab serves as the anode (+), while a thin sheet of pure metal serves as the cathode (-)."
            },
            {
                "question": "What is the commercial significance of the insoluble residue known as 'anode mud' that settles beneath the anode?",
                "options": [
                    "It is hazardous toxic waste that has zero economic value",
                    "It contains valuable noble metals such as gold, silver, and platinum",
                    "It is converted into agricultural urea fertilizer",
                    "It is dried and used as domestic table salt"
                ],
                "answer": 1,
                "hint": "Metals less reactive than copper do not oxidise into solution and drop out as sludge.",
                "explanation": "Insoluble impurities that drop below the anode as anode mud contain precious, unreactive noble metals like gold, silver, and platinum, which are recovered to offset refining costs."
            }
        ]
    },
    {
        "id": 16,
        "title": "Corrosion And Alloying",
        "subtitle": "Galvanisation, Homogeneous Alloys, 22-Carat Gold, and the Delhi Iron Pillar",
        "speech": "Metals deteriorate over time through corrosion when exposed to atmospheric gases and moisture. Silver tarnishes black due to silver sulphide formation from trace hydrogen sulphide gas. Copper develops a green patina of basic copper carbonate when exposed to moist carbon dioxide. Iron forms reddish-brown hydrated ferric oxide, commonly known as rust. In Activity 3.14, three test tubes verify that iron nails rust only when both oxygen and liquid water are present simultaneously; nails sealed under boiled water with an oil film or kept in dry air with calcium chloride do not rust. Corrosion is prevented by painting, greasing, galvanising, or alloying. Galvanisation protects steel and iron by coating them with a thin layer of zinc, which provides sacrificial protection even if scratched. Alloying produces homogeneous mixtures of two or more metals, or a metal and non-metal, radically modifying physical properties. Pure iron is soft; adding zero point zero five percent carbon makes it hard and strong, while adding nickel and chromium creates rust-resistant stainless steel. Brass alloys copper with zinc, bronze combines copper with tin, and solder combines lead with tin for low-melting electrical joints. In India, 22-carat gold alloys pure gold with copper for durable jewellery, while Delhi's 1600-year-old Iron Pillar showcases ancient rust-resistant mastery.",
        "content": {
            "concept": "Corrosion requires both air and moisture (Activity 3.14). Prevention includes galvanisation (zinc coating) and alloying (homogeneous metallic mixtures). Alloys include stainless steel (Fe+C+Ni+Cr), brass (Cu+Zn), bronze (Cu+Sn), solder (Pb+Sn), and 22-carat gold (Au+Cu/Ag).",
            "formula": "\\text{Rust: } \\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O} \\quad | \\quad \\text{Bronze: Cu + Sn} \\quad | \\quad \\text{Brass: Cu + Zn} \\quad | \\quad \\text{Solder: Pb + Sn}",
            "points": [
                "Activity 3.14: Rusting requires both air (oxygen) and water (moisture).",
                "Silver tarnishes black (Ag2S); copper tarnishes green [CuCO3·Cu(OH)2].",
                "Galvanisation coats iron/steel with zinc; sacrificial zinc protects even when scratched.",
                "Alloying alters properties: pure iron is soft; adding 0.05% C makes it hard and strong.",
                "Stainless steel contains iron, carbon, nickel, and chromium; it never rusts.",
                "Amalgam is an alloy containing mercury; solder (Pb+Sn) has a low melting point.",
                "24-carat gold is pure and soft; 22-carat gold is alloyed with copper/silver for jewellery.",
                "Delhi Iron Pillar: 1600-year-old, 8-metre metallurgical marvel near Qutub Minar resists rust."
            ]
        },
        "checkpoints": [
            {
                "question": "What two environmental factors are proven indispensable for the rusting of iron in Activity 3.14?",
                "options": [
                    "Carbon dioxide and sunlight",
                    "Both oxygen (air) and moisture (water)",
                    "Pure nitrogen gas and zero gravity",
                    "Dry hydrogen chloride gas and kerosene"
                ],
                "answer": 1,
                "hint": "Dry air alone or boiled water alone without air does not cause iron to rust.",
                "explanation": "Activity 3.14 proves that iron nails rust only in Tube A where both atmospheric air (oxygen) and water (moisture) are present simultaneously."
            },
            {
                "question": "Why is pure 24-carat gold rarely used for fabricating fine commercial jewellery?",
                "options": [
                    "It tarnishes black upon exposure to human sweat",
                    "It is extremely soft and easily bends, deforms, or scratches",
                    "It is highly radioactive and hazardous to skin",
                    "It reacts violently with atmospheric oxygen and catches fire"
                ],
                "answer": 1,
                "hint": "Alloying with 2 parts copper or silver increases hardness and mechanical rigidity.",
                "explanation": "Pure 24-carat gold is too soft for crafting durable jewellery. In India, 22-carat gold (22 parts gold alloyed with 2 parts copper or silver) is used to impart hardness."
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

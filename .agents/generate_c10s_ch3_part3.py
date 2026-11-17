"""Generate Slides 17 to 20 (Quiz Review) for Class 10 Science Chapter 3: Metals and Non-metals
Strict constraints:
- Title: strictly 1 to 3 words
- Speech: strictly "" (silent)
- 10 comprehensive NCERT-aligned questions per slide
- 4 options per question, correct answer index, hint, explanation, and 3-step structured solution
- No fictional characters or persona titles
"""

slides = [
    {
        "id": 17,
        "title": "Physical Properties Review",
        "subtitle": "Comprehensive NCERT Review: Metallic Lustre, Conductivity, Ductility, and Exceptions",
        "speech": "",
        "content": {
            "concept": "Physical properties distinguish metals and non-metals, with key anomalies: Hg is liquid; Ga and Cs melt on palm; iodine is lustrous; diamond is hardest and conducts heat; graphite conducts electricity; alkali metals cut with a knife.",
            "formula": "1\\text{ g Gold} \\rightarrow 2\\text{ km Wire} \\quad | \\quad \\text{Thermal: Ag} > \\text{Cu} \\gg \\text{Pb, Hg}",
            "points": [
                "Metals possess metallic lustre, malleability, ductility, and high thermal and electrical conductivity.",
                "Non-metals exist as solids or gases, except bromine which is a reddish-brown liquid.",
                "Mercury is the only metal liquid at room temperature; gallium and caesium melt at palm temperature (302.8 K).",
                "Iodine is a non-metal with metallic lustre; diamond is the hardest natural substance with high mp and thermal conduction.",
                "Graphite conducts electricity; alkali metals (Li, Na, K) have low densities and can be cut with a butter knife."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "Which of the following elements is a non-metal that exists in the liquid state at room temperature?",
                "options": [
                    "Bromine",
                    "Mercury",
                    "Gallium",
                    "Chlorine"
                ],
                "answer": 0,
                "hint": "It is a reddish-brown halogen liquid at standard room temperature and pressure.",
                "explanation": "Bromine (Br2) is the only non-metal that is liquid at room temperature. Mercury and gallium are metals.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Examine the physical states of elements at 298 K (25°C). Bromine (Br2) exists as a diatomic covalent liquid.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Non-metals typically form diatomic gases (O2, N2, Cl2) or macromolecular solids (C, P4, S8). Bromine possesses an intermediate intermolecular London dispersion force that maintains liquid state at 25°C.",
                    "Step 3: Verification & Real-World Application: Confirming NCERT Table 3.1: Bromine is the sole liquid non-metal, whereas Mercury (Hg) is the sole liquid metal at room temperature."
                ]
            },
            {
                "id": 2,
                "question": "Which two metals have such exceptionally low melting points that they liquefy simply when held on the palm of your hand?",
                "options": [
                    "Gallium and Caesium",
                    "Sodium and Potassium",
                    "Iron and Copper",
                    "Lead and Mercury"
                ],
                "answer": 0,
                "hint": "Their melting points are 302.8 K (29.8°C) and 301.6 K (28.6°C), well below human core body temperature (310 K).",
                "explanation": "Gallium and caesium have very low melting points (around 30°C). Normal human body temperature (37°C) transfers sufficient heat to melt them on the palm.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid Ga(s) and Cs(s) undergo phase change to liquid state Ga(l) and Cs(l) at temperatures below 303 K.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Melting point of Ga = 29.8°C; Cs = 28.6°C. Since human body skin temperature is approximately 34°C–37°C, thermal conduction rapidly supplies the latent heat of fusion.",
                    "Step 3: Verification & Real-World Application: Activity 3.5 demonstrates that while metals generally have high melting points, Ga and Cs are textbook exceptions that melt on the palm."
                ]
            },
            {
                "id": 3,
                "question": "Which property of metals makes gold suitable for drawing a single gram of the metal into a wire approximately two kilometres long?",
                "options": [
                    "Ductility",
                    "Malleability",
                    "Sonority",
                    "Lustre"
                ],
                "answer": 0,
                "hint": "Ductility is the mechanical property of a material to be drawn out into thin, elongated wires without fracturing.",
                "explanation": "Ductility is the ability of metals to be drawn into thin wires. Gold is the most ductile metal known; 1 gram of gold can be drawn into a 2 km wire.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 1 g Au(s) -> wire of length ~2,000 m. Tensile stress elongates metallic grains along slip planes.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Metallic bonding consists of delocalised valence electron seas surrounding positive cations. Non-directional metallic bonds allow atomic planes to slide without catastrophic cleavage.",
                    "Step 3: Verification & Real-World Application: Malleability refers to hammering into sheets, while ductility refers to drawing into wires. Gold exhibits maximal ductility."
                ]
            },
            {
                "id": 4,
                "question": "Which of the following pairs represents the best conductor of heat and the poorest conductor of heat among metals, respectively?",
                "options": [
                    "Silver is the best conductor; Lead is a poor conductor",
                    "Iron is the best conductor; Copper is a poor conductor",
                    "Aluminium is the best conductor; Gold is a poor conductor",
                    "Mercury is the best conductor; Silver is a poor conductor"
                ],
                "answer": 0,
                "hint": "Silver and copper have the highest thermal conductivity; lead and mercury are comparatively very poor conductors.",
                "explanation": "Silver (followed closely by copper) is the best thermal conductor. Lead and mercury are comparatively poor thermal conductors among metals.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Thermal conductivity (k) measures heat flux per unit temperature gradient. Ag has k ~ 429 W/(m·K); Cu has k ~ 401 W/(m·K); Pb has k ~ 35 W/(m·K).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Heat transfer in metals occurs predominantly via free electron gas conduction and crystal lattice vibrations (phonons). Silver possesses the optimal electron mean free path.",
                    "Step 3: Verification & Real-World Application: In Activity 3.5 (wax pin drop test), wax on copper or silver melts rapidly, whereas lead exhibits minimal thermal conduction."
                ]
            },
            {
                "id": 5,
                "question": "Which non-metal possesses a lustrous, shiny appearance resembling that of polished metals?",
                "options": [
                    "Iodine",
                    "Sulphur",
                    "Phosphorus",
                    "Carbon (charcoal)"
                ],
                "answer": 0,
                "hint": "It is a dark purple-black halogen crystal in Group 17 that sublimes into violet vapour upon heating.",
                "explanation": "Iodine is a non-metal that naturally exhibits a distinct metallic lustre, making it an exception to the general rule that non-metals are dull.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solid I2(s) forms dark crystalline plates that reflect incident light with a shiny metallic sheen.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Iodine's large, polarisable electron cloud absorbs and re-emits photons across visible wavelengths, producing surface specular reflection.",
                    "Step 3: Verification & Real-World Application: Non-metals are typically non-lustrous, but iodine crystals present a striking metallic lustre in NCERT Activity 3.1."
                ]
            },
            {
                "id": 6,
                "question": "Diamond and graphite are allotropes of carbon with radically contrasting properties. Which statement is chemically accurate?",
                "options": [
                    "Diamond is the hardest natural substance and conducts heat; graphite is soft and conducts electricity",
                    "Graphite is the hardest natural substance; diamond is a soft electrical insulator",
                    "Both diamond and graphite conduct electricity due to free delocalised protons",
                    "Neither diamond nor graphite can withstand temperatures above room temperature"
                ],
                "answer": 0,
                "hint": "Diamond has a rigid 3D tetrahedral network with no free electrons; graphite has hexagonal layers with delocalised pi electrons.",
                "explanation": "Diamond is a rigid 3D network (hardest known natural substance, excellent thermal conductor, electrical insulator). Graphite has planar hexagonal layers with free delocalised electrons, making it a good electrical conductor.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Carbon allotropes: C(diamond) sp3 hybridized; C(graphite) sp2 hybridized with 1 delocalised electron per carbon atom.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In graphite, each carbon atom bonds to 3 adjacent carbons in hexagonal planes, leaving 1 valence electron free to migrate across layers under an applied potential difference.",
                    "Step 3: Verification & Real-World Application: Diamond is an electrical insulator used in cutting tools, whereas graphite is soft and slippery, used in pencil leads and battery electrodes."
                ]
            },
            {
                "id": 7,
                "question": "Why are alkali metals like lithium, sodium, and potassium stored under kerosene or mineral oil in laboratories?",
                "options": [
                    "They are soft enough to cut with a knife and react vigorously with atmospheric moisture and oxygen, catching fire",
                    "They dissolve completely in glass test tubes and convert into radioactive lead",
                    "They evaporate rapidly into toxic greenhouse gases at normal room temperature",
                    "They are magnetic and would fly out of unsealed containers toward nearby steel benches"
                ],
                "answer": 0,
                "hint": "Alkali metals have low ionization energy and react violently and exothermically with oxygen and water vapour.",
                "explanation": "Lithium, sodium, and potassium have very low densities and low melting points, and react so vigorously with atmospheric air and moisture that they catch fire if kept open. They are submerged in kerosene for safety.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 4Na(s) + O2(g) -> 2Na2O(s); 2Na(s) + 2H2O(l) -> 2NaOH(aq) + H2(g) + Heat. The heat evolved instantly ignites hydrogen gas.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Alkali metals have a solitary valence electron (ns1) shielded by inner electron shells, resulting in extremely low first ionization energy and high electropositivity.",
                    "Step 3: Verification & Real-World Application: NCERT Activity 3.8 notes that sodium and potassium react exothermically with open air, necessitating immersion in kerosene oil."
                ]
            },
            {
                "id": 8,
                "question": "In Activity 3.8, magnesium ribbon and sulphur powder are burnt separately in air and their combustion products dissolved in water. What litmus colour changes are observed?",
                "options": [
                    "Magnesium oxide turns red litmus blue (basic); Sulphur dioxide solution turns blue litmus red (acidic)",
                    "Magnesium oxide turns blue litmus red (acidic); Sulphur dioxide solution turns red litmus blue (basic)",
                    "Both combustion products turn blue litmus red because all combustion oxides are strongly acidic",
                    "Neither oxide dissolves in water or exhibits any effect on litmus indicators"
                ],
                "answer": 0,
                "hint": "Metal oxides are generally basic (forming hydroxide ions); non-metal oxides are acidic (forming hydrogen ions).",
                "explanation": "Burned magnesium produces MgO, which dissolves in water to form Mg(OH)2 (alkaline, turns red litmus blue). Burned sulphur produces SO2, forming sulphurous acid H2SO3 (acidic, turns blue litmus red).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2Mg + O2 -> 2MgO; MgO + H2O -> Mg(OH)2 [Basic]. S + O2 -> SO2; SO2 + H2O -> H2SO3 [Acidic].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Basic Mg(OH)2 releases OH- ions in water, deprotonating red litmus dye to turn it blue. Acidic H2SO3 releases H+ ions, protonating blue litmus to turn it red.",
                    "Step 3: Verification & Real-World Application: This fundamental experiment proves that most metal oxides are basic, whereas most non-metal oxides are acidic."
                ]
            },
            {
                "id": 9,
                "question": "Why are electrical transmission cables coated with polyvinylchloride (PVC) or rubber-like insulating materials?",
                "options": [
                    "To prevent electric shock and short-circuits because polymers are non-conducting insulators",
                    "To increase the speed of electric current flow through the copper core",
                    "To make the cables emit bright fluorescent light in nighttime darkness",
                    "To chemically react with copper wires and convert them into gold alloys"
                ],
                "answer": 0,
                "hint": "Polyvinylchloride (PVC) lacks free delocalised electrons or ions and is a robust electrical insulator.",
                "explanation": "Metals like copper and aluminium are excellent electrical conductors. PVC is an electrical insulator that coats wires to prevent accidental electric shocks and short-circuit faults.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Electrical cables comprise a high-conductivity metallic core (Cu or Al) surrounded by an outer sheath of polyvinylchloride [-CH2-CHCl-]n.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In PVC, all valence electrons are tightly localized in covalent C-C, C-H, and C-Cl bonds, preventing charge carrier mobility.",
                    "Step 3: Verification & Real-World Application: Activity 3.6 demonstrates that completing an electric circuit with a metal lights the bulb, whereas plastic insulators prevent current conduction."
                ]
            },
            {
                "id": 10,
                "question": "What property explains why school bells and musical instruments like gongs are fabricated from bronze or brass metals rather than wood or graphite?",
                "options": [
                    "Sonority",
                    "Malleability",
                    "Ductility",
                    "Thermal conductivity"
                ],
                "answer": 0,
                "hint": "Sonorous materials produce a deep, resonant ringing sound when struck with a hard object.",
                "explanation": "Metals produce a resonant ringing sound when struck by a hard surface; this property is called sonority. Hence, bells and cymbal plates are fabricated from metals.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Impact of clapper on bell body transfers acoustic vibration energy through metallic crystal grains.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Metals possess elastic crystalline lattices with high shear moduli that sustain acoustic oscillations without rapid internal friction damping.",
                    "Step 3: Verification & Real-World Application: NCERT defines sonority as the physical capability of metals to produce sound on being struck, which is why school bells are made of metals."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Chemical Reactions Review",
        "subtitle": "Comprehensive NCERT Review: Oxide Classification, Amphoterism, Water, and Acid Reactions",
        "speech": "",
        "content": {
            "concept": "Metals react with oxygen to form oxides, with water to form hydroxides/oxides and H2, and with acids to form salts and H2. Amphoteric oxides react with both acids and bases. Aqua Regia dissolves noble metals.",
            "formula": "\\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\rightarrow 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O} \\quad | \\quad \\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\rightarrow 2\\text{NaAlO}_2 + \\text{H}_2\\text{O}",
            "points": [
                "Amphoteric oxides (Al2O3, ZnO) react with both acids and bases to produce salt and water.",
                "Aluminium forms sodium aluminate (NaAlO2) when reacted with sodium hydroxide.",
                "Active metals (Na, K) react violently with cold water; Ca floats with H2 bubbles; Mg reacts with hot water.",
                "Al, Fe, and Zn react only with steam; copper, silver, and gold do not react with water at all.",
                "HNO3 oxidises evolved H2 into water, except with dilute HNO3 reacting with magnesium and manganese.",
                "Aqua Regia is a fresh 3:1 mixture of conc. HCl and conc. HNO3 that dissolves gold and platinum."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "Which of the following metallic oxides is classified as an amphoteric oxide?",
                "options": [
                    "Aluminium oxide (Al2O3)",
                    "Sodium oxide (Na2O)",
                    "Calcium oxide (CaO)",
                    "Potassium oxide (K2O)"
                ],
                "answer": 0,
                "hint": "It reacts with both hydrochloric acid and sodium hydroxide to produce salt and water.",
                "explanation": "Aluminium oxide (Al2O3) and zinc oxide (ZnO) exhibit both acidic and basic characteristics and are termed amphoteric oxides.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Al2O3 + 6HCl -> 2AlCl3 + 3H2O (basic role); Al2O3 + 2NaOH -> 2NaAlO2 + H2O (acidic role).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Oxides that neutralise acids to form salt and water behave as bases; when they neutralise strong bases, they behave as acids. Al2O3 performs both roles.",
                    "Step 3: Verification & Real-World Application: NCERT Section 3.2.1 identifies Al2O3 and ZnO as classic amphoteric oxides, whereas Na2O, K2O, and CaO are strictly basic oxides."
                ]
            },
            {
                "id": 2,
                "question": "What salt is formed when aluminium oxide reacts with aqueous sodium hydroxide solution?",
                "options": [
                    "Sodium aluminate (NaAlO2)",
                    "Sodium aluminium hydride (NaAlH4)",
                    "Sodium sulphate (Na2SO4)",
                    "Aluminium chloride (AlCl3)"
                ],
                "answer": 0,
                "hint": "The balanced equation is: Al2O3 + 2NaOH -> 2NaAlO2 + H2O.",
                "explanation": "Aluminium oxide acts as an acidic oxide when reacting with sodium hydroxide base, forming sodium aluminate (NaAlO2) and water.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Al2O3(s) + 2NaOH(aq) -> 2NaAlO2(aq) + H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Aluminium forms the aluminate complex anion [Al(OH)4]- or dehydrated meta-aluminate form [AlO2]- balanced by Na+ cations.",
                    "Step 3: Verification & Real-World Application: This specific reaction is vital for the Bayer process in alumina refining and demonstrates oxide amphoterism."
                ]
            },
            {
                "id": 3,
                "question": "Why does calcium float to the surface of water after sinking initially during its reaction with cold water?",
                "options": [
                    "Hydrogen gas bubbles adhere to the metallic calcium surface, lifting it upwards",
                    "Calcium transforms instantly into lightweight helium gas",
                    "The water evaporates instantly, leaving dry calcium suspended in air",
                    "Calcium forms a dense magnet that is repelled by the bottom of the beaker"
                ],
                "answer": 0,
                "hint": "The bubbles of evolved H2 gas stick to the metal pieces, acting like miniature floatation buoys.",
                "explanation": "Calcium reacts with water less violently: Ca + 2H2O -> Ca(OH)2 + H2. Bubbles of hydrogen gas stick to the surface of calcium, causing the pieces to float.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Ca(s) + 2H2O(l) -> Ca(OH)2(aq) + H2(g) + Heat. Bubbles of H2(g) nucleate on the calcium metal surface.",
                    "Step 2: Reaction Mechanism & Stoichiometry: The adhering hydrogen bubbles significantly lower the composite density of the calcium metal chunks below that of liquid water (1.0 g/cm3).",
                    "Step 3: Verification & Real-World Application: Activity 3.10 highlights that both calcium and magnesium float during reaction with water due to adhering hydrogen gas bubbles."
                ]
            },
            {
                "id": 4,
                "question": "Which of the following metals does not react with cold water or hot water, but reacts vigorously with steam to evolve hydrogen gas?",
                "options": [
                    "Iron (Fe)",
                    "Sodium (Na)",
                    "Copper (Cu)",
                    "Gold (Au)"
                ],
                "answer": 0,
                "hint": "It reacts with steam at red heat according to: 3Fe + 4H2O(steam) -> Fe3O4 + 4H2.",
                "explanation": "Metals like iron, aluminium, and zinc do not react with cold or hot water, but react with steam to form metallic oxides and hydrogen gas.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 3Fe(s) + 4H2O(g) -> Fe3O4(s) + 4H2(g). The oxide formed is mixed iron(II,III) oxide (magnetic iron oxide).",
                    "Step 2: Reaction Mechanism & Stoichiometry: At elevated temperatures, gaseous H2O molecules possess sufficient activation energy to penetrate the metal surface and oxidise Fe to Fe3O4.",
                    "Step 3: Verification & Real-World Application: NCERT Figure 3.3 shows the laboratory apparatus for passing steam over heated metals to collect H2 gas over water."
                ]
            },
            {
                "id": 5,
                "question": "Why is hydrogen gas generally not evolved when most metals react with nitric acid (HNO3)?",
                "options": [
                    "Nitric acid is a powerful oxidising agent that oxidises the evolved H2 into water (H2O) and is itself reduced to nitrogen oxides",
                    "Nitric acid contains no hydrogen atoms in its chemical formula",
                    "Metals dissolve completely into nitrogen gas without reacting",
                    "The reaction produces solid elemental nitrogen instead of gas"
                ],
                "answer": 0,
                "hint": "HNO3 reduces itself to NO, NO2, or N2O while oxidising hydrogen to H2O.",
                "explanation": "Nitric acid (HNO3) is a strong oxidising agent. It oxidises the hydrogen produced to water and is itself reduced to nitrogen oxides (N2O, NO, or NO2).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Metal + HNO3 -> Metal Nitrate + H2O + NOx (NO2, NO, or N2O).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Nascent hydrogen formed during acid attack is immediately oxidised by the nitrate group: 2[H] + [O] -> H2O.",
                    "Step 3: Verification & Real-World Application: Only very dilute nitric acid (1%) reacts with Magnesium (Mg) and Manganese (Mn) to liberate actual H2 gas."
                ]
            },
            {
                "id": 6,
                "question": "Which two metals react with very dilute nitric acid (HNO3) to evolve hydrogen gas?",
                "options": [
                    "Magnesium and Manganese",
                    "Copper and Silver",
                    "Gold and Platinum",
                    "Iron and Zinc"
                ],
                "answer": 0,
                "hint": "These two metals have very high oxidation potentials that overcome the oxidizing capacity of very dilute HNO3.",
                "explanation": "Very dilute nitric acid reacts with magnesium (Mg) and manganese (Mn) to liberate hydrogen gas: Mg + 2HNO3(dil) -> Mg(NO3)2 + H2.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Mg(s) + 2HNO3(very dil.) -> Mg(NO3)2(aq) + H2(g); Mn(s) + 2HNO3(very dil.) -> Mn(NO3)2(aq) + H2(g).",
                    "Step 2: Reaction Mechanism & Stoichiometry: When HNO3 is extremely dilute, its oxidising power is substantially reduced, allowing strong electropositive metals like Mg and Mn to displace H+ ions as H2 gas.",
                    "Step 3: Verification & Real-World Application: NCERT Section 3.2.3 explicitly highlights Mg and Mn as the two specific exceptions that evolve H2 with dilute HNO3."
                ]
            },
            {
                "id": 7,
                "question": "What is the volumetric ratio and composition of the fuming, highly corrosive reagent known as Aqua Regia?",
                "options": [
                    "3 parts concentrated HCl to 1 part concentrated HNO3",
                    "1 part concentrated HCl to 3 parts concentrated HNO3",
                    "3 parts dilute H2SO4 to 1 part concentrated HCl",
                    "Equal parts concentrated acetic acid and concentrated nitric acid"
                ],
                "answer": 0,
                "hint": "Aqua Regia ('Royal Water') contains three parts conc. hydrochloric acid to one part conc. nitric acid.",
                "explanation": "Aqua Regia is a freshly prepared mixture of concentrated hydrochloric acid and concentrated nitric acid in a 3:1 volumetric ratio. It dissolves noble metals like gold and platinum.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 3HCl(conc.) + HNO3(conc.) -> NOCl(aq) + 2H2O(l) + 2[Cl] (nascent chlorine).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Nascent chlorine attacks noble metals: Au + 3[Cl] + HCl -> HAuCl4 (chloroauric acid). Neither acid alone can dissolve gold.",
                    "Step 3: Verification & Real-World Application: Aqua Regia is called 'Royal Water' because of its unique ability to dissolve noble 'royal' metals (Au and Pt)."
                ]
            },
            {
                "id": 8,
                "question": "In Activity 3.12, what observable chemical changes occur when a clean iron nail is immersed in blue copper sulphate solution?",
                "options": [
                    "The blue solution turns light green (FeSO4) and a reddish-brown copper coating deposits on the nail",
                    "The solution turns deep purple and the nail dissolves completely into bubbles",
                    "The solution remains bright blue and no coating forms on the nail",
                    "A yellow precipitate of iron sulphide settles at the bottom"
                ],
                "answer": 0,
                "hint": "Iron is more reactive than copper and displaces it: Fe + CuSO4 -> FeSO4 + Cu.",
                "explanation": "Iron displaces copper from copper sulphate solution because Fe is higher in the reactivity series. The blue CuSO4 turns light green FeSO4, and reddish-brown copper deposits on the iron nail.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Fe(s) + CuSO4(aq)[blue] -> FeSO4(aq)[pale green] + Cu(s)[reddish-brown].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Redox transfer: Fe(s) -> Fe2+(aq) + 2e- (oxidation); Cu2+(aq) + 2e- -> Cu(s) (reduction).",
                    "Step 3: Verification & Real-World Application: When the reverse experiment is performed (copper wire in iron sulphate), no displacement occurs because copper cannot displace the more reactive iron."
                ]
            },
            {
                "id": 9,
                "question": "Which of the following arrangements correctly lists metals in decreasing order of their chemical reactivity?",
                "options": [
                    "K > Na > Ca > Mg > Al > Zn > Fe > Pb > Cu",
                    "Cu > Fe > Zn > Al > Mg > Ca > Na > K",
                    "Al > Mg > Ca > Na > K > Zn > Fe > Cu",
                    "Fe > Zn > Al > Mg > Ca > Na > K > Cu"
                ],
                "answer": 0,
                "hint": "Potassium and sodium are at the very top, while copper, silver, and gold are near the bottom.",
                "explanation": "The reactivity series ranks metals in order of decreasing reactivity: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Reactivity correlates with standard oxidation potential E° and ease of losing valence electrons in aqueous solution.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Group 1 alkali metals (K, Na) lose 1 electron with minimal ionisation energy; followed by Group 2 (Ca, Mg), Group 13 (Al), and transition metals (Zn, Fe, Pb).",
                    "Step 3: Verification & Real-World Application: Metals above hydrogen displace H2 from dilute acids; metals below hydrogen (Cu, Ag, Au) do not."
                ]
            },
            {
                "id": 10,
                "question": "What is the industrial process of 'anodising' used to protect aluminium articles?",
                "options": [
                    "Electrolytically thickening the protective aluminium oxide layer using dilute sulphuric acid",
                    "Coating aluminium with molten zinc by dipping it in a galvanising bath",
                    "Submerging aluminium in concentrated kerosene to remove surface oxygen",
                    "Electroplating aluminium with pure gold to prevent scratching"
                ],
                "answer": 0,
                "hint": "In anodising, aluminium is made the anode in an electrolytic cell containing dilute H2SO4.",
                "explanation": "Anodising is an electrolytic process that produces a thick, protective layer of aluminium oxide (Al2O3) on aluminium articles by making them the anode in dilute sulphuric acid electrolysis.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Anode (+): 2Al + 3O2- -> Al2O3 + 6e-. Dilute H2SO4 electrolyte conducts current and releases oxygen ions at the aluminium anode.",
                    "Step 2: Reaction Mechanism & Stoichiometry: The newly formed Al2O3 layer is uniform, dense, and non-porous, preventing subsequent corrosive attack by moisture and atmospheric pollutants.",
                    "Step 3: Verification & Real-World Application: The thickened oxide layer can also absorb vibrant organic dyes to give cookware and architectural frames attractive, fade-resistant colours."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Metallurgical Extraction Review",
        "subtitle": "Comprehensive NCERT Review: Ionic Crystals, Ore Roasting, Calcination, and Auto-Reduction",
        "speech": "",
        "content": {
            "concept": "Ionic compounds form by electron transfer and have high melting points, brittleness, and conduct electricity in molten/aqueous states. Metallurgy extracts metals based on reactivity: thermal for low, roasting/calcination for medium, electrolysis for high.",
            "formula": "2\\text{HgS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{HgO} + 2\\text{SO}_2 \\quad | \\quad 2\\text{HgO} \\xrightarrow{\\Delta} 2\\text{Hg} + \\text{O}_2 \\quad | \\quad \\text{ZnO} + \\text{C} \\rightarrow \\text{Zn} + \\text{CO}",
            "points": [
                "Ionic bonds arise from complete electron transfer from metal (cation) to non-metal (anion).",
                "Ionic solids are brittle because shear stress aligns like charges, causing repulsion.",
                "Minerals are natural crustal compounds; ores yield metals profitably; gangue is rocky waste.",
                "Low-reactivity metals: Cinnabar (HgS) is roasted to HgO, which thermally decomposes into liquid Hg.",
                "Copper glance (Cu2S) undergoes auto-reduction: 2Cu2O + Cu2S → 6Cu + SO2.",
                "Roasting heats sulphides in excess air; Calcination heats carbonates in limited air."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "Which electronic configuration corresponds to the formation of a stable magnesium cation (Mg2+)?",
                "options": [
                    "2, 8 (identical to Neon)",
                    "2, 8, 2 (identical to Magnesium atom)",
                    "2, 8, 8 (identical to Argon)",
                    "2, 7 (identical to Fluorine atom)"
                ],
                "answer": 0,
                "hint": "Neutral Mg has atomic number 12 (configuration 2,8,2). It loses two valence electrons.",
                "explanation": "Magnesium has atomic number 12 (2,8,2). To achieve octet stability, it loses its two outermost valence electrons to form Mg2+ with configuration 2,8 (noble gas neon core).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Mg (atomic number 12): 1s2 2s2 2p6 3s2 (2,8,2). Ionisation: Mg -> Mg2+ + 2e-.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Removing both 3s valence electrons leaves the n=2 principal shell completely filled with 8 electrons (2s2 2p6), conferring octet stability.",
                    "Step 3: Verification & Real-World Application: The Mg2+ cation combines with two Cl- anions (each 2,8,8) to form neutral ionic magnesium chloride (MgCl2)."
                ]
            },
            {
                "id": 2,
                "question": "Why do ionic crystals such as sodium chloride exhibit mechanical brittleness when struck with a hammer?",
                "options": [
                    "Shear forces shift lattice planes, forcing like-charged ions into proximity and causing intense electrostatic repulsion",
                    "The impact converts ionic bonds into volatile noble gas molecules",
                    "Ionic crystals contain pockets of vacuum that implode under physical pressure",
                    "The hammer absorbs all electrons from the crystal lattice"
                ],
                "answer": 0,
                "hint": "Displacing an ionic layer brings Na+ next to Na+ and Cl- next to Cl-.",
                "explanation": "Striking an ionic crystal forces layers of ions to slide. Like-charged ions come next to each other; the resulting electrostatic repulsion causes the crystal to shatter.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: In NaCl crystal, Na+ and Cl- ions alternate in a stable 3D lattice with maximum attractive contact and minimum repulsive contact.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Applied shear stress slides one layer by one atomic spacing. This brings positive ions directly opposite positive ions and negative opposite negative, generating massive Coulombic repulsion.",
                    "Step 3: Verification & Real-World Application: Brittleness is a hallmark physical property distinguishing ionic solids from malleable, ductile metals."
                ]
            },
            {
                "id": 3,
                "question": "In which pair of states do ionic compounds readily conduct an electric current?",
                "options": [
                    "Molten (liquid) state and aqueous solution state",
                    "Solid crystal state and gas state",
                    "Solid crystal state and non-polar benzene solvent",
                    "Sub-zero frozen state and dry powder state"
                ],
                "answer": 0,
                "hint": "Electric current requires mobile charge carriers. Ions are free to migrate only in molten or dissolved states.",
                "explanation": "In solid state, ions are held immobility in the rigid crystal lattice. When melted into liquid or dissolved in water, the lattice breaks down and free ions migrate to conduct electricity.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Conduction equation: Current I = q·n·v (where v is drift velocity of mobile charge carriers). In solid NaCl, v = 0.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In molten state (T > 1074 K) or aqueous solution, hydration energy or thermal energy overcomes lattice enthalpy, freeing Na+ and Cl- ions to move toward cathode and anode.",
                    "Step 3: Verification & Real-World Application: Activity 3.13 confirms that a circuit connected to dry salt does not conduct, but dissolving the salt in water causes the bulb to glow brightly."
                ]
            },
            {
                "id": 4,
                "question": "What is the primary commercial ore of mercury, and what chemical reaction takes place when it is heated strongly in air?",
                "options": [
                    "Cinnabar (HgS); it oxidises to HgO, which thermally decomposes to liquid mercury (Hg)",
                    "Bauxite (Al2O3); it reduces directly to mercury vapor in carbon monoxide",
                    "Galena (PbS); it converts to mercury sulphate upon roasting",
                    "Haematite (Fe2O3); it reacts with sulphur to form mercury amalgam"
                ],
                "answer": 0,
                "hint": "Cinnabar is mercuric sulphide (HgS). Roasting gives HgO, which decomposes above 300°C.",
                "explanation": "Cinnabar (HgS) is the sulphide ore of mercury. When heated in air, it converts to HgO: 2HgS + 3O2 -> 2HgO + 2SO2. Further heating decomposes HgO to metallic mercury: 2HgO -> 2Hg + O2.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Stage 1: 2HgS + 3O2(g) -> 2HgO(s) + 2SO2(g). Stage 2: 2HgO(s) -> 2Hg(l) + O2(g).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Mercuric oxide has a low thermal decomposition temperature (~400°C) because mercury has very low affinity for oxygen.",
                    "Step 3: Verification & Real-World Application: Mercury is located near the bottom of the reactivity series and is therefore extracted purely through thermal roasting without needing carbon coke."
                ]
            },
            {
                "id": 5,
                "question": "How is metallic copper extracted from its sulphide ore, copper glance (Cu2S), in the absence of carbon reducing agents?",
                "options": [
                    "Through auto-reduction between cuprous oxide (Cu2O) and unoxidised cuprous sulphide (Cu2S)",
                    "By adding concentrated sulphuric acid to dissolve all sulphur atoms",
                    "By passing high-voltage alternating current through cold solid ore",
                    "By mixing copper glance with molten sodium chloride in an open furnace"
                ],
                "answer": 0,
                "hint": "The oxide and sulphide react together at high temperature: 2Cu2O + Cu2S -> 6Cu + SO2.",
                "explanation": "Copper is extracted from copper glance (Cu2S) by auto-reduction. Roasting part of the sulphide forms Cu2O, which then reacts with the remaining Cu2S to produce blister copper: 2Cu2O + Cu2S -> 6Cu + SO2.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Partial roasting: 2Cu2S + 3O2 -> 2Cu2O + 2SO2. Auto-reduction: 2Cu2O + Cu2S -> 6Cu(l) + SO2(g).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Sulphide ions (S2-) act as internal reducing agents for cuprous ions (Cu+), evolving SO2 gas and leaving crude molten copper.",
                    "Step 3: Verification & Real-World Application: Evolving SO2 bubbles form blisters on the solidified copper surface, giving it the industrial designation 'blister copper'."
                ]
            },
            {
                "id": 6,
                "question": "What is the primary difference in industrial furnace conditions between roasting and calcination?",
                "options": [
                    "Roasting heats sulphide ores in excess air; Calcination heats carbonate ores in limited or absent air",
                    "Roasting cools ores in dry ice; Calcination burns ores in water",
                    "Roasting applies to high-reactivity metals; Calcination applies exclusively to gold and silver",
                    "Roasting uses electricity; Calcination uses nuclear radiation"
                ],
                "answer": 0,
                "hint": "Sulphide ores need oxygen to evolve SO2 (roasting); carbonate ores decompose thermally to evolve CO2 without air (calcination).",
                "explanation": "Roasting is heating sulphide ores strongly in the presence of excess air to produce oxides and SO2. Calcination is heating carbonate or hydrated ores in limited air to expel CO2 or moisture.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Roasting: 2ZnS + 3O2 -> 2ZnO + 2SO2. Calcination: ZnCO3 -> ZnO + CO2.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Sulphide minerals lack oxygen and require an atmospheric oxidant; carbonate minerals already contain oxygen and undergo endothermic thermal decomposition.",
                    "Step 3: Verification & Real-World Application: Converting sulphides and carbonates into oxides is essential because reducing oxides with carbon is thermodynamically more favourable."
                ]
            },
            {
                "id": 7,
                "question": "What reducing agent is used industrially to convert zinc oxide (ZnO) into elemental zinc metal?",
                "options": [
                    "Carbon (in the form of coke)",
                    "Concentrated nitric acid",
                    "Gaseous sulphur dioxide",
                    "Solid sodium chloride"
                ],
                "answer": 0,
                "hint": "Carbon reduces ZnO at high temperature: ZnO + C -> Zn + CO.",
                "explanation": "Zinc oxide is reduced to metallic zinc using carbon (coke) as a reducing agent: ZnO + C -> Zn + CO.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: ZnO(s) + C(s) -> Zn(g/s) + CO(g) (in a retort furnace at ~1400 K).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Carbon possesses a higher chemical affinity for oxygen at elevated temperatures than zinc, forming carbon monoxide gas.",
                    "Step 3: Verification & Real-World Application: Zinc vaporises during reduction and is condensed in condensers to yield commercial spelter zinc."
                ]
            },
            {
                "id": 8,
                "question": "What is the chemical equation and practical utility of the highly exothermic Thermit reaction?",
                "options": [
                    "Fe2O3 + 2Al -> 2Fe(l) + Al2O3 + Heat; used to weld cracked railway tracks and heavy machine parts on-site",
                    "Fe + CuSO4 -> FeSO4 + Cu; used to paint bridge cables green",
                    "CaO + H2O -> Ca(OH)2; used to whitewash building walls",
                    "2H2 + O2 -> 2H2O; used to fill weather balloons"
                ],
                "answer": 0,
                "hint": "Aluminium displaces iron from ferric oxide with so much heat that iron melts.",
                "explanation": "The reaction of iron(III) oxide with aluminium powder is the Thermit reaction: Fe2O3 + 2Al -> 2Fe(l) + Al2O3 + Heat. The heat evolved melts the displaced iron, which flows into cracks to weld railway tracks.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Fe2O3(s) + 2Al(s) -> 2Fe(l) + Al2O3(s) + Delta H (extreme exothermic heat ~3000°C).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Aluminium has a far greater affinity for oxygen than iron does, driving rapid single displacement and releasing massive enthalpy of formation of Al2O3.",
                    "Step 3: Verification & Real-World Application: The superheated liquid iron flows directly into a refractory crucible mould placed over cracked railway rail joints, welding them seamlessly."
                ]
            },
            {
                "id": 9,
                "question": "Why is an aqueous solution of sodium chloride never used to extract metallic sodium via electrolysis?",
                "options": [
                    "Hydrogen gas is liberated at the cathode instead of sodium because hydrogen has a higher reduction potential than sodium",
                    "Sodium chloride does not dissolve in water",
                    "The electric current converts water into liquid petroleum",
                    "Water causes the anode to convert into solid gold"
                ],
                "answer": 0,
                "hint": "In aqueous solution, H+ ions from water are reduced much more easily than Na+ ions.",
                "explanation": "If aqueous NaCl is electrolysed, H+ ions from water are preferentially reduced at the cathode, evolving H2 gas rather than depositing sodium metal. Hence, anhydrous molten NaCl must be electrolysed.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: E°(Na+/Na) = -2.71 V; E°(H+/H2) = 0.00 V. In aqueous solution, reduction of H+ (or H2O) is thermodynamically favored over Na+.",
                    "Step 2: Reaction Mechanism & Stoichiometry: At cathode in water: 2H2O + 2e- -> H2(g) + 2OH-(aq). Sodium metal is never deposited; instead, the chlor-alkali process yields NaOH, Cl2, and H2.",
                    "Step 3: Verification & Real-World Application: To extract elemental sodium, anhydrous molten NaCl (with CaCl2 added to lower the melting point) is electrolysed in a Down's cell."
                ]
            },
            {
                "id": 10,
                "question": "Which of the following describes the gangue removal process during ore dressing?",
                "options": [
                    "Separating undesirable rocky impurities (sand, clay, limestone) from the valued ore based on physical or chemical differences",
                    "Burning pure metal until it converts entirely into black soot",
                    "Dissolving gold bullion in concentrated nitric acid",
                    "Freezing liquid mercury into solid bricks using liquid helium"
                ],
                "answer": 0,
                "hint": "Gangue refers to the commercially useless rocky matrix enclosing the ore.",
                "explanation": "Gangue refers to unwanted sand, rock, and clay associated with mined ores. Concentration (dressing) removes gangue using techniques like gravity separation, froth floatation, or magnetic separation.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Mined ore = Valuable mineral + Gangue. Beneficiation upgrades the metal concentration before chemical reduction.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Separation exploits physical disparities such as density differences (gravity washing), magnetic susceptibility (magnetic separators), or surface wetting properties (froth floatation).",
                    "Step 3: Verification & Real-World Application: Removing gangue first minimizes energy consumption and flux requirements in downstream smelting furnaces."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Corrosion Alloying Review",
        "subtitle": "Comprehensive NCERT Review: Rust Chemistry, Sacrificial Galvanisation, Alloys, and Delhi Pillar",
        "speech": "",
        "content": {
            "concept": "Corrosion requires air and moisture (Activity 3.14). Prevention includes painting, oiling, galvanisation (zinc coating), and alloying. Alloys modify metal properties (stainless steel, brass, bronze, solder, 22-carat gold).",
            "formula": "\\text{Rust: } \\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O} \\quad | \\quad \\text{Stainless Steel: Fe + 0.05\\% C + Ni + Cr} \\quad | \\quad \\text{Brass: Cu + Zn}",
            "points": [
                "Activity 3.14 confirms iron nails rust only when both oxygen (air) and moisture (water) are present.",
                "Silver tarnishes black due to Ag2S; copper forms green basic carbonate CuCO3·Cu(OH)2.",
                "Galvanisation coats steel/iron with zinc; sacrificial zinc protects even when scratched.",
                "Alloying is a homogeneous mixture of two or more metals, or a metal and non-metal.",
                "Pure iron is soft; adding 0.05% carbon makes it hard; nickel and chromium create stainless steel.",
                "Alloy compositions: Brass (Cu+Zn), Bronze (Cu+Sn), Solder (Pb+Sn, low mp), Amalgam (contains Hg).",
                "22-carat gold contains 22 parts gold and 2 parts copper/silver to impart strength for jewellery.",
                "Delhi Iron Pillar: 1600-year-old metallurgical marvel resisting corrosion due to a thin protective film."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "In NCERT Activity 3.14 (the three-test-tube corrosion experiment), why do iron nails in Test Tube B (boiled distilled water covered with an oil layer) fail to rust?",
                "options": [
                    "Boiling drives out dissolved air, and the oil film prevents atmospheric oxygen from dissolving in the water",
                    "Boiled water destroys all chemical bonds in iron permanently",
                    "The oil film reacts with iron to form a diamond protective shell",
                    "Distilled water turns into concentrated sulphuric acid when boiled"
                ],
                "answer": 0,
                "hint": "Both oxygen and moisture are necessary for rusting. Tube B contains moisture but lacks oxygen.",
                "explanation": "Boiling removes dissolved oxygen from water, and the layer of oil prevents atmospheric oxygen from re-dissolving. Without oxygen, iron cannot rust.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Rust formation requires: 4Fe + 3O2 + 2xH2O -> 2Fe2O3·xH2O. Both O2 and H2O are mandatory reactants.",
                    "Step 2: Reaction Mechanism & Stoichiometry: In Tube B, water is boiled to expel dissolved gases and sealed with 1 mL kerosene/oil. Because [O2] = 0, the cathodic half-reaction (O2 + 2H2O + 4e- -> 4OH-) cannot proceed.",
                    "Step 3: Verification & Real-World Application: This proves definitively that water alone without oxygen cannot cause rusting of iron."
                ]
            },
            {
                "id": 2,
                "question": "What is the chemical composition of the black tarnish that gradually coats silver articles exposed to polluted air?",
                "options": [
                    "Silver sulphide (Ag2S)",
                    "Silver chloride (AgCl)",
                    "Silver oxide (Ag2O)",
                    "Silver carbonate (Ag2CO3)"
                ],
                "answer": 0,
                "hint": "Silver reacts slowly with trace hydrogen sulphide (H2S) gas present in the atmosphere.",
                "explanation": "Silver articles turn black when exposed to air because silver reacts with trace hydrogen sulphide (H2S) in the air to form a black coating of silver sulphide (Ag2S).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2Ag(s) + H2S(g) + 1/2 O2(g) -> Ag2S(s)[black] + H2O(l).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Silver has high chemical affinity for sulphur. Hydrogen sulphide from biological decay or vehicle exhaust attacks the silver surface.",
                    "Step 3: Verification & Real-World Application: NCERT Section 3.5 notes that the black tarnish on heirloom silver spoons and jewellery is silver sulphide."
                ]
            },
            {
                "id": 3,
                "question": "What is the chemical identity of the green patina that develops on copper vessels exposed to moist ambient air?",
                "options": [
                    "Basic copper carbonate [CuCO3·Cu(OH)2]",
                    "Copper(II) nitrate [Cu(NO3)2]",
                    "Pure copper metal powder",
                    "Copper(I) chloride [Cu2Cl2]"
                ],
                "answer": 0,
                "hint": "Copper reacts with moist carbon dioxide in air to form a mixture of copper carbonate and copper hydroxide.",
                "explanation": "Copper reacts slowly with moist carbon dioxide in the air to form a green coating of basic copper carbonate, composed of CuCO3·Cu(OH)2.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2Cu(s) + H2O(l) + CO2(g) + O2(g) -> CuCO3·Cu(OH)2(s)[green].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Surface copper atoms oxidise in the combined presence of atmospheric O2, H2O, and CO2, producing an insoluble protective basic patina.",
                    "Step 3: Verification & Real-World Application: This green patina is famously observed on copper roofs and statues (such as the Statue of Liberty). Washing with acidic lemon juice (citric acid) dissolves the basic carbonate to restore shiny copper."
                ]
            },
            {
                "id": 4,
                "question": "Why does a galvanised iron pipe remain protected against rusting even if its outer zinc coating is scratched and iron is exposed?",
                "options": [
                    "Zinc is more reactive than iron and undergoes preferential sacrificial oxidation, protecting the underlying iron",
                    "Zinc reacts with air to release an invisible shield of helium gas",
                    "Scratched zinc converts immediately into stainless steel",
                    "Iron absorbs zinc atoms and becomes completely non-metallic"
                ],
                "answer": 0,
                "hint": "Zinc has a lower reduction potential (E° = -0.76 V) than iron (E° = -0.44 V) and oxidises first as a sacrificial anode.",
                "explanation": "Zinc is more electropositive than iron. Even when the coating is scratched, zinc acts as a sacrificial anode, corroding in preference to iron and supplying electrons to keep iron reduced.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Zn -> Zn2+ + 2e- (E° = -0.76 V); Fe -> Fe2+ + 2e- (E° = -0.44 V). Zinc has higher oxidation tendency.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Exposed iron becomes the cathode, while adjacent zinc becomes the sacrificial anode. The electrons released by zinc oxidation flow to iron, preventing Fe from oxidising to Fe2+.",
                    "Step 3: Verification & Real-World Application: Unlike tin-plating (which accelerates iron rusting if scratched), galvanised zinc offers sacrificial cathodic protection under all conditions."
                ]
            },
            {
                "id": 5,
                "question": "What is the elemental composition of stainless steel, and why is it superior to pure iron for kitchen utensils and surgical instruments?",
                "options": [
                    "Iron mixed with nickel, chromium, and carbon; it is hard and does not rust",
                    "Iron mixed with pure gold and lead; it melts at room temperature",
                    "Copper mixed with tin and zinc; it conducts electricity without wires",
                    "Pure aluminium hammered with charcoal; it is lightweight and brittle"
                ],
                "answer": 0,
                "hint": "Nickel and chromium impart corrosion resistance, while carbon imparts mechanical hardness.",
                "explanation": "Stainless steel is an alloy composed of iron, nickel, chromium, and a small percentage of carbon. It is hard, strong, and completely resistant to rusting and corrosion.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Stainless steel composition: ~70-74% Fe, ~18% Cr, ~8% Ni, ~0.1-0.2% C.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Chromium in the alloy reacts with atmospheric oxygen to form an invisible, self-healing, passivating surface film of Cr2O3 that blocks moisture and acid attack.",
                    "Step 3: Verification & Real-World Application: Pure iron is soft and stretches easily when hot; alloying with Ni and Cr transforms it into an unreactive, high-strength material."
                ]
            },
            {
                "id": 6,
                "question": "What are the constituent metals that make up the commercial alloys brass and bronze, respectively?",
                "options": [
                    "Brass is Copper and Zinc (Cu + Zn); Bronze is Copper and Tin (Cu + Sn)",
                    "Brass is Copper and Tin (Cu + Sn); Bronze is Copper and Zinc (Cu + Zn)",
                    "Brass is Lead and Tin (Pb + Sn); Bronze is Iron and Carbon (Fe + C)",
                    "Brass is Gold and Silver (Au + Ag); Bronze is Aluminium and Copper (Al + Cu)"
                ],
                "answer": 0,
                "hint": "Brass contains zinc (remember: 'B-Z' sounds like buzz); bronze contains tin (Sn).",
                "explanation": "Brass is an alloy of copper and zinc (Cu + Zn). Bronze is an alloy of copper and tin (Cu + Sn). Both have lower electrical conductivity than pure copper.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Brass = Cu (~70%) + Zn (~30%). Bronze = Cu (~90%) + Sn (~10%).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Introducing zinc or tin solute atoms of differing atomic radii into the copper face-centered cubic lattice disrupts lattice symmetry and increases hardness and yield strength.",
                    "Step 3: Verification & Real-World Application: Brass is used for musical instruments and hardware fittings; bronze is used for medals, statues, and heavy-duty marine bearings."
                ]
            },
            {
                "id": 7,
                "question": "Why is the alloy 'solder' (an alloy of lead and tin) universally utilised for welding electrical circuit wires?",
                "options": [
                    "It possesses a remarkably low melting point, allowing it to melt quickly with a soldering iron without damaging components",
                    "It conducts electricity faster than the speed of light",
                    "It converts electrical current into pure distilled water",
                    "It glues wires purely through permanent magnetic attraction"
                ],
                "answer": 0,
                "hint": "Solder consists of roughly 50% lead (Pb) and 50% tin (Sn) and has a eutectic-like low melting point (~183°C).",
                "explanation": "Solder is an alloy of lead and tin (Pb + Sn). It has a low melting point (~183°C), making it ideal for joining electrical wires together smoothly without overheating sensitive electronic circuits.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Alloy composition: ~50% Pb + ~50% Sn. Pure Pb melts at 327°C; pure Sn melts at 232°C. The alloy melts at ~183°C.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Alloying creates a eutectic depression in the solid-liquid phase diagram, yielding a melting temperature substantially lower than either constituent metal.",
                    "Step 3: Verification & Real-World Application: NCERT Section 3.5 highlights solder's low melting point as the specific functional reason for its universal use in electrical wire joints."
                ]
            },
            {
                "id": 8,
                "question": "What is an 'amalgam' in metallurgical and dental chemistry?",
                "options": [
                    "An alloy where one of the constituent metals is liquid mercury",
                    "A mixture of solid gold and radioactive uranium",
                    "An alloy composed strictly of non-metals dissolved in molten carbon",
                    "A mineral ore that contains zero metallic elements"
                ],
                "answer": 0,
                "hint": "Whenever mercury (Hg) is alloyed with another metal (e.g., sodium or silver), the resulting alloy is termed an amalgam.",
                "explanation": "An amalgam is an alloy of mercury with one or more other metals. Examples include sodium amalgam (a laboratory reducing agent) and silver-tin amalgam (used in dental fillings).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Metal + Hg(l) -> Metal Amalgam (e.g., Na/Hg, Zn/Hg, Ag-Sn-Hg).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Liquid mercury wets and dissolves metallic lattices at room temperature, forming intermetallic solution phases that harden over time.",
                    "Step 3: Verification & Real-World Application: NCERT specifies: If one of the metals in an alloy is mercury, the alloy is designated as an amalgam."
                ]
            },
            {
                "id": 9,
                "question": "What does '22-carat gold' mean in Indian jewellery craftsmanship?",
                "options": [
                    "22 parts by weight of pure gold alloyed with 2 parts of copper or silver to increase hardness",
                    "22% pure gold mixed with 78% zinc metal",
                    "Pure gold that has been boiled 22 times in nitric acid",
                    "Gold that weighs exactly 22 kilograms per cubic centimetre"
                ],
                "answer": 0,
                "hint": "Pure gold is 24-carat (100% Au), but is too soft for jewellery. 22-carat gold contains 22/24 parts gold.",
                "explanation": "Pure gold is 24-carat and is extremely soft. In India, jewellery is typically crafted from 22-carat gold, meaning 22 parts of pure gold are alloyed with 2 parts of copper or silver to make it durable and rigid.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 22-carat gold purity = (22/24) * 100% = 91.6% pure Au (hallmark 916), alloyed with 8.4% Cu or Ag.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Copper and silver atoms substitute into the gold crystal lattice, inducing lattice strain that pins dislocations and prevents ductile plastic deformation.",
                    "Step 3: Verification & Real-World Application: Pure 24-carat gold bends and scratches easily under gentle finger pressure; 22-carat gold maintains intricate jewelry shapes for decades."
                ]
            },
            {
                "id": 10,
                "question": "What remarkable feature of the 1600-year-old Iron Pillar near the Qutub Minar in Delhi astonishes modern materials scientists?",
                "options": [
                    "It has resisted atmospheric rusting and corrosion for over 16 centuries due to a protective surface film of iron hydrogen phosphate",
                    "It was carved from a single solid meteor of pure plutonium",
                    "It floats weightlessly in the air without touching the ground",
                    "It emits alternating magnetic pulses that power the Delhi metro system"
                ],
                "answer": 0,
                "hint": "Forged by ancient Indian ironworkers around 400 CE, it stands rust-free in the open air.",
                "explanation": "The Iron Pillar near Qutub Minar in Delhi was built over 1600 years ago. Despite standing outdoors in rain and sun for sixteen centuries, it has remarkably resisted rusting due to the formation of a protective passive surface oxide/phosphate film (misawite/protective iron hydrogen phosphate).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Forged wrought iron with high phosphorus content (0.25%) forms a passive protective barrier layer: FePO4·H3PO4 (misawite / amorphous iron oxyhydroxide).",
                    "Step 2: Reaction Mechanism & Stoichiometry: High slag inclusions and phosphorus catalysed the rapid creation of a dense, protective, pore-free catalytic surface film that arrested subsequent moisture and oxygen ingress.",
                    "Step 3: Verification & Real-World Application: Standing 8 metres high and weighing over 6 tonnes, the Delhi Iron Pillar stands as enduring evidence of the sophisticated metallurgical expertise of ancient Indian metallurgists."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides:
        print(f"Slide {s['id']} ({s['title']}): {len(s['questions'])} questions, speech len={len(s['speech'])}")
        assert s["speech"] == "", f"Slide {s['id']} speech must be empty"
        assert len(s["title"].split()) <= 3, f"Slide {s['id']} title '{s['title']}' has > 3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} questions count {len(s['questions'])} != 10"
        for q in s["questions"]:
            assert len(q["options"]) == 4, f"Slide {s['id']} Q{q['id']} does not have 4 options"
            assert 0 <= q["answer"] <= 3, f"Slide {s['id']} Q{q['id']} answer index out of bounds"
            assert len(q["solution"]) == 3, f"Slide {s['id']} Q{q['id']} solution does not have 3 steps"
    print("All slides 17 to 20 validated successfully!")

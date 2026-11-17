"""Generate Slides 17 to 20 (Quiz Review) for Class 10 Science Chapter 4: Carbon and its Compounds
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
        "title": "Covalent Bonding Review",
        "subtitle": "Comprehensive NCERT Review: Tetravalency, Allotropes, and Electron Sharing",
        "speech": "",
        "content": {
            "concept": "Carbon shares four valence electrons to attain a noble gas octet, forming single, double, or triple covalent bonds. Carbon allotropes include diamond (3D rigid tetrahedral, hardest), graphite (hexagonal layers, conductor), and fullerenes (C60).",
            "formula": "\\text{Crust: } 0.02\\% \\quad | \\quad \\text{Atmosphere: } 0.03\\% \\quad | \\quad \\text{Bonding: Covalent Sharing of } 4e^-",
            "points": [
                "Carbon is present as 0.02% in Earth's crust (minerals, coal, petroleum) and 0.03% in atmosphere (CO2).",
                "Carbon compounds have low melting/boiling points and are poor electrical conductors due to covalent bonding.",
                "Carbon avoids C4- (nuclear instability) and C4+ (excessive ionisation energy) by sharing electron pairs.",
                "Single (H2, CH4), double (O2, CO2), and triple (N2, C2H2) covalent bonds arise from shared pairs.",
                "Diamond is an insulator with a rigid 3D tetrahedral network; graphite has free delocalised electrons.",
                "Fullerene (C60) consists of 60 carbon atoms arranged in a spherical geodesic cage."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "What is the natural percentage abundance of carbon in the Earth's crust and the atmosphere, respectively?",
                "options": [
                    "0.02% in the crust (minerals) and 0.03% in the atmosphere (CO2)",
                    "2.0% in the crust and 3.0% in the atmosphere",
                    "0.2% in the crust and 0.003% in the atmosphere",
                    "12.0% in the crust and 21.0% in the atmosphere"
                ],
                "answer": 0,
                "hint": "Carbon is remarkably scarce in non-living reservoirs despite making up all living tissue.",
                "explanation": "Carbon exists as only 0.02% in the Earth's crust (in carbonates, coal, petroleum) and 0.03% in the atmosphere as carbon dioxide gas.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Crustal carbon occurs as metal carbonates (CaCO3, MgCO3), coal, and petroleum hydrocarbons totaling 0.02% of crustal mass; atmospheric carbon exists as CO2 at 0.03% by volume.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Despite this tiny geochemical fraction, carbon forms the fundamental structural basis of all living biological tissues, polymers, and synthetic pharmaceuticals.",
                    "Step 3: Verification & Real-World Application: NCERT Chapter 4 Introduction highlights this stark contrast between carbon's tiny natural abundance and its overwhelming everyday ubiquity."
                ]
            },
            {
                "id": 2,
                "question": "Why do covalent carbon compounds like methane and chloroform exhibit low melting and boiling points compared to ionic compounds like sodium chloride?",
                "options": [
                    "Inter-molecular forces between covalent molecules are weak and easily overcome by heat",
                    "Covalent bonds inside carbon molecules break at room temperature",
                    "Carbon compounds contain no electrons or protons",
                    "Carbon atoms undergo nuclear fission when warmed"
                ],
                "answer": 0,
                "hint": "Distinguish between intra-molecular covalent bonds and inter-molecular attractions.",
                "explanation": "Covalent carbon compounds have strong covalent bonds within individual molecules, but weak intermolecular forces between separate molecules, requiring little thermal energy to separate them.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Compare NaCl (melting point 1074 K) with CH4 (melting point 90 K, boiling point 111 K) and CHCl3 (boiling point 334 K).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Ionic compounds require overcoming powerful electrostatic lattice attractions between oppositely charged ions; covalent molecular substances require overcoming only weak dispersion/dipole-dipole forces between neutral molecules.",
                    "Step 3: Verification & Real-World Application: Because no ions exist to carry charge or create strong crystal lattices, carbon compounds are low-melting electrical insulators."
                ]
            },
            {
                "id": 3,
                "question": "Why does a carbon atom not form a C4- anion by gaining four electrons to achieve a neon noble gas octet?",
                "options": [
                    "A small nucleus with only six protons cannot stably hold ten electrons against intense inter-electron repulsion",
                    "Carbon has zero protons in its atomic nucleus",
                    "Gaining electrons causes carbon to emit lethal gamma radiation",
                    "Carbon atoms can only bond with alkali metals"
                ],
                "answer": 0,
                "hint": "Evaluate the electrostatic ratio of 6 nuclear protons to 10 orbital electrons.",
                "explanation": "It would be extremely difficult for the carbon nucleus with only 6 protons to hold onto 10 electrons (6 original + 4 extra) due to massive inter-electronic repulsion and small atomic volume.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: C (atomic number 6, 6p+, 6e-) + 4e- -> C4- (6p+, 10e-).",
                    "Step 2: Reaction Mechanism & Stoichiometry: The high electron-to-proton ratio (10:6) produces overwhelming electron-electron shielding and repulsion, rendering the tetra-anion thermodynamically unstable.",
                    "Step 3: Verification & Real-World Application: NCERT Section 4.1 establishes that carbon avoids both C4- and C4+ ions, choosing electron sharing instead."
                ]
            },
            {
                "id": 4,
                "question": "Why does a carbon atom not form a C4+ cation by losing its four valence electrons to attain a helium duplet?",
                "options": [
                    "Removing four successive electrons requires an immense amount of ionisation energy, leaving a naked, unstable nucleus",
                    "Losing electrons converts carbon into pure radioactive plutonium",
                    "Carbon atoms possess no valence electrons in their outer shell",
                    "Electrons can never be removed from any non-metallic atom"
                ],
                "answer": 0,
                "hint": "Consider the cumulative sum of four successive ionisation energies (IE1 + IE2 + IE3 + IE4).",
                "explanation": "Removing four successive electrons from a carbon atom requires an astronomical quantity of ionisation energy, leaving an unstable C4+ cation with 6 protons holding just 2 electrons.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: C -> C4+ + 4e-. Cumulative ionisation energy exceeds thousands of kilojoules per mole.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Each successive electron removal faces an increasingly concentrated positive nuclear charge, making the fourth ionisation energy prohibitive under chemical conditions.",
                    "Step 3: Verification & Real-World Application: Carbon resolves this thermodynamic barrier by mutually sharing valence electron pairs in covalent bonds."
                ]
            },
            {
                "id": 5,
                "question": "How many total covalent bonds and shared electron pairs are present in a molecule of ethane (C2H6)?",
                "options": [
                    "Seven covalent bonds (one C-C bond and six C-H bonds)",
                    "Six covalent bonds",
                    "Eight covalent bonds",
                    "Four covalent bonds"
                ],
                "answer": 0,
                "hint": "Draw the Lewis structure: H3C-CH3. Count all shared pairs.",
                "explanation": "In ethane (C2H6), there is 1 carbon-carbon single bond and 6 carbon-hydrogen single bonds, making a total of 7 covalent bonds (7 shared electron pairs, or 14 shared electrons).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Ethane structural formula: H-C(H)2-C(H)2-H, or H3C-CH3.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Central C-C linkage = 1 shared pair. Six C-H linkages = 6 shared pairs. Total shared pairs = 1 + 6 = 7 single covalent bonds.",
                    "Step 3: Verification & Real-World Application: NCERT Exercise 1 explicitly tests this: ethane with the molecular formula C2H6 has 7 covalent bonds."
                ]
            },
            {
                "id": 6,
                "question": "Which of the following molecules contains a triple covalent bond formed by the sharing of three pairs of valence electrons?",
                "options": [
                    "Diatomic nitrogen (N2)",
                    "Diatomic oxygen (O2)",
                    "Methane (CH4)",
                    "Water (H2O)"
                ],
                "answer": 0,
                "hint": "Each nitrogen atom has 5 valence electrons and needs 3 electrons to complete its octet.",
                "explanation": "In diatomic nitrogen (N2), each nitrogen atom (2,5) contributes three electrons, sharing three pairs of electrons to form a strong triple covalent bond (:N≡N:).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Two nitrogen atoms (electronic configuration 2,5) require 3 electrons each to achieve neon configuration (2,8).",
                    "Step 2: Reaction Mechanism & Stoichiometry: 3 valence electrons from atom A + 3 valence electrons from atom B = 6 shared electrons (3 pairs), forming a triple bond (N≡N) with 1 lone pair on each atom.",
                    "Step 3: Verification & Real-World Application: O2 contains a double bond (O=O), H2O contains two single bonds, and CH4 contains four single bonds."
                ]
            },
            {
                "id": 7,
                "question": "Why is graphite an electrical conductor, while diamond is an electrical insulator, despite both consisting of pure carbon?",
                "options": [
                    "In graphite, each carbon bonds to three carbons, leaving one delocalised electron free to move; in diamond, all four electrons are locked in 3D tetrahedral bonds",
                    "Graphite contains free protons that conduct electricity through air",
                    "Diamond contains no carbon atoms in its crystal lattice",
                    "Graphite is an alloy of copper and carbon"
                ],
                "answer": 0,
                "hint": "Conduction requires mobile charge carriers. Check the number of bonds per carbon atom.",
                "explanation": "In graphite, each carbon atom is bonded to only 3 other carbon atoms in planar hexagonal layers, leaving one valence electron delocalised and free to conduct electricity. In diamond, all 4 valence electrons form rigid tetrahedral bonds.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Diamond: sp3 hybridization, 4 localized sigma bonds per carbon atom, band gap > 5.5 eV (insulator). Graphite: sp2 hybridization, 3 sigma bonds + 1 delocalised pi electron per carbon atom.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Delocalised pi electrons in graphite form a conducting valence band that allows electron migration along hexagonal planes under an applied voltage.",
                    "Step 3: Verification & Real-World Application: Graphite is used as non-metallic battery electrodes and motor brushes; diamond is an electrical insulator with high thermal conductivity."
                ]
            },
            {
                "id": 8,
                "question": "What is the structural geometry of the Buckminsterfullerene (C60) carbon allotrope discovered in 1985?",
                "options": [
                    "A hollow spherical cage of 60 carbon atoms assembled into 20 hexagons and 12 pentagons like a soccer ball",
                    "A flat triangular sheet of graphite layers",
                    "A single infinite chain of carbon-carbon triple bonds",
                    "A solid cube of compressed diamond crystals"
                ],
                "answer": 0,
                "hint": "Named after architect Buckminster Fuller, its structure resembles a geodesic dome or soccer ball.",
                "explanation": "Buckminsterfullerene (C60) consists of 60 carbon atoms arranged in a hollow sphere consisting of 20 interlocking hexagons and 12 pentagons, resembling a soccer ball.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Fullerenes form the third major allotropic family of elemental carbon, designated Cn (with C60 as the archetype).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Euler's polyhedral formula requires exactly 12 pentagonal rings to close a spherical carbon cage, surrounded by 20 hexagonal benzenoid rings (truncated icosahedron).",
                    "Step 3: Verification & Real-World Application: Discovered by Kroto, Curl, and Smalley, C60 was named in honor of architect Buckminster Fuller's geodesic dome designs."
                ]
            },
            {
                "id": 9,
                "question": "What is the molecular geometry and electron dot sharing in a carbon dioxide (CO2) molecule?",
                "options": [
                    "Linear molecule where the central carbon atom forms two separate double covalent bonds with two oxygen atoms (O=C=O)",
                    "A bent molecule with two single bonds and four ionic charges",
                    "A tetrahedral molecule with four oxygen atoms around carbon",
                    "A cyclic three-membered ring with single bonds"
                ],
                "answer": 0,
                "hint": "Carbon has 4 valence electrons; each oxygen has 6 valence electrons and needs 2.",
                "explanation": "In CO2, the central carbon shares two electron pairs with each of two oxygen atoms, creating two double covalent bonds in a linear geometry: :O::C::O: or O=C=O.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: C (4 valence electrons) + 2 O (6 valence electrons each). Total valence electrons = 4 + (2 * 6) = 16.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Carbon shares two pairs with oxygen 1 (double bond) and two pairs with oxygen 2 (double bond). Each oxygen retains two non-bonding lone pairs.",
                    "Step 3: Verification & Real-World Application: This linear O=C=O structure satisfies octets for all three atoms and has zero net dipole moment."
                ]
            },
            {
                "id": 10,
                "question": "What is the physical structure of an eight-atom sulphur molecule (S8), as described in NCERT Section 4.1?",
                "options": [
                    "A puckered, crown-shaped eight-membered cyclic ring of sulphur atoms linked by single covalent bonds",
                    "A linear straight chain of eight sulphur atoms with ionic endpoints",
                    "A spherical cage identical to Buckminsterfullerene",
                    "A single solid cubic crystal held by metallic bonds"
                ],
                "answer": 0,
                "hint": "Sulphur has atomic number 16 (2,8,6) and forms a ring resembling a royal crown.",
                "explanation": "Sulphur exists as an S8 molecule where eight sulphur atoms are joined in a closed, puckered ring shaped like a crown, with each sulphur sharing one electron pair with two adjacent atoms.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Sulphur atom has configuration 2,8,6 (needs 2 electrons to complete its valence octet).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Each sulphur atom forms two single covalent bonds with two neighbouring sulphur atoms, forming an 8-membered cyclic ring: -S-S-S-S-S-S-S-S-.",
                    "Step 3: Verification & Real-World Application: To relieve bond strain, the S8 ring adopts a non-planar puckered 'crown' conformation, as illustrated in NCERT Figure 4.4."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Hydrocarbon Structure Review",
        "subtitle": "Comprehensive NCERT Review: Catenation, Isomerism, Rings, and Functional Groups",
        "speech": "",
        "content": {
            "concept": "Carbon forms straight chains, branched isomers (butane C4H10 has 2 isomers; pentane C5H12 has 3 isomers), and rings (cyclohexane C6H12, benzene C6H6). Heteroatoms create functional groups (-OH, -CHO, >C=O, -COOH) with homologous series differing by -CH2- (14 u).",
            "formula": "\\text{Alkanes: } \\text{C}_n\\text{H}_{2n+2} \\quad | \\quad \\text{Alkenes: } \\text{C}_n\\text{H}_{2n} \\quad | \\quad \\text{Alkynes: } \\text{C}_n\\text{H}_{2n-2} \\quad | \\quad \\Delta = 14\\text{ u}",
            "points": [
                "Catenation and tetravalency with small atomic size enable millions of carbon compounds.",
                "Friedrich Wöhler disproved vital force theory in 1828 by heating ammonium cyanate to form urea.",
                "Structural isomers have identical molecular formula but different structural connectivity.",
                "Butane (C4H10) has 2 isomers; Pentane (C5H12) has 3 isomers (n-pentane, isopentane, neopentane).",
                "Cyclic rings: Cyclohexane (C6H12, saturated) and Benzene (C6H6, 3 alternating double bonds).",
                "Homologous series: same functional group, successive difference of -CH2- (14 u), graded physical properties."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "Which historic experiment conducted by Friedrich Wöhler in 1828 permanently disproved the 'vital force' theory of organic compounds?",
                "options": [
                    "Synthesizing organic urea by heating inorganic ammonium cyanate in the laboratory",
                    "Extracting pure acetic acid from fermenting apple cider",
                    "Burning diamond in pure oxygen to produce carbon dioxide",
                    "Electrolysing molten sodium chloride to produce sodium metal"
                ],
                "answer": 0,
                "hint": "He prepared an animal urine compound from an inanimate mineral salt.",
                "explanation": "In 1828, Friedrich Wöhler heated ammonium cyanate (an inorganic salt) and discovered it isomerised into urea (an organic compound excreted by animals), proving organic synthesis requires no vital force.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: NH4CNO (ammonium cyanate, inorganic) -> NH2CONH2 (urea, organic).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Thermal isomerization rearranges ionic [NH4]+[CNO]- into a covalent carbonyl diamide molecule without biological intervention.",
                    "Step 3: Verification & Real-World Application: This breakthrough shattered the dualistic dogma separating 'vital biological' compounds from inanimate minerals, founding modern organic chemistry."
                ]
            },
            {
                "id": 2,
                "question": "How many structural isomers can be drawn for the saturated alkane pentane (C5H12)?",
                "options": [
                    "Three isomers: n-pentane, isopentane (2-methylbutane), and neopentane (2,2-dimethylpropane)",
                    "Two isomers: n-pentane and isopentane only",
                    "Five isomers: one for each carbon atom",
                    "Only one isomer; alkanes cannot form isomers"
                ],
                "answer": 0,
                "hint": "A 5-carbon chain can be straight (5C), branched (4C+1C), or doubly branched (3C+2C).",
                "explanation": "Pentane (C5H12) has 3 structural isomers: normal-pentane (straight 5C chain), isopentane / 2-methylbutane (branched 4C chain), and neopentane / 2,2-dimethylpropane (cross-shaped 3C chain).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Molecular formula C5H12. Saturated acyclic alkane obeying CnH2n+2.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Isomer 1: CH3-CH2-CH2-CH2-CH3 (n-pentane). Isomer 2: CH3-CH(CH3)-CH2-CH3 (2-methylbutane). Isomer 3: C(CH3)4 (2,2-dimethylpropane).",
                    "Step 3: Verification & Real-World Application: All three share identical mass (72 u) but exhibit different boiling points due to branching reducing surface contact area."
                ]
            },
            {
                "id": 3,
                "question": "What is the molecular formula and structural classification of cyclohexane?",
                "options": [
                    "C6H12; a saturated cyclic hydrocarbon containing a closed ring of six single-bonded carbon atoms",
                    "C6H6; an unsaturated aromatic ring with three double bonds",
                    "C6H14; a straight-chain saturated alkane",
                    "C6H10; an alkyne containing a triple bond"
                ],
                "answer": 0,
                "hint": "Forming a ring eliminates two terminal hydrogen atoms compared to hexane (C6H14 -> C6H12).",
                "explanation": "Cyclohexane (C6H12) is a saturated cyclic hydrocarbon consisting of a ring of six carbon atoms joined by single bonds, with each carbon bonded to two hydrogen atoms (-CH2-).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Cycloalkanes follow the general formula CnH2n (same as alkenes, but containing zero double bonds).",
                    "Step 2: Reaction Mechanism & Stoichiometry: In cyclohexane, six -CH2- methylene units join into a closed hexagonal ring. Every carbon forms 4 single covalent bonds.",
                    "Step 3: Verification & Real-World Application: In contrast, benzene is C6H6 with alternating double bonds; hexane is open-chain C6H14."
                ]
            },
            {
                "id": 4,
                "question": "What is the molecular formula and structure of the unsaturated cyclic hydrocarbon benzene?",
                "options": [
                    "C6H6; a hexagonal ring of six carbon atoms linked by alternating single and double bonds",
                    "C6H12; a saturated hexagonal ring with only single bonds",
                    "C6H14; an open branched alkane",
                    "C2H2; a linear alkyne"
                ],
                "answer": 0,
                "hint": "Each of the six carbon atoms is bonded to exactly one hydrogen atom (C6H6).",
                "explanation": "Benzene has the molecular formula C6H6. It consists of a planar hexagonal ring of 6 carbon atoms with alternating single and double bonds, each carbon bearing one hydrogen.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Benzene formula: C6H6. Skeletons: 6 carbons arranged in a ring with three C=C double bonds and three C-C single bonds.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Each carbon atom is sp2 hybridized, sharing electrons in a conjugated pi ring system that confers exceptional resonance stability.",
                    "Step 3: Verification & Real-World Application: NCERT Figure 4.7 illustrates the structure and electron dot formula of benzene as the archetype of aromatic compounds."
                ]
            },
            {
                "id": 5,
                "question": "What functional group is present in the compound propanone (CH3-CO-CH3)?",
                "options": [
                    "Ketone group (>C=O bonded to two carbon atoms)",
                    "Aldehyde group (-CHO)",
                    "Alcohol group (-OH)",
                    "Carboxylic acid group (-COOH)"
                ],
                "answer": 0,
                "hint": "The name ends in '-one' and has a carbonyl group flanked by two methyl groups.",
                "explanation": "Propanone (commonly known as acetone) contains a ketone functional group, where a carbonyl carbon (C=O) is bonded between two adjacent carbon atoms.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Propanone formula: CH3-C(=O)-CH3. Root: prop (3 carbons); suffix: -one (ketone).",
                    "Step 2: Reaction Mechanism & Stoichiometry: The carbonyl group (>C=O) is internal, distinguishing it from propanal (CH3CH2CHO) where the carbonyl group is terminal.",
                    "Step 3: Verification & Real-World Application: Propanone is the simplest possible ketone because a ketone requires at least three carbons to flank the carbonyl carbon."
                ]
            },
            {
                "id": 6,
                "question": "What is the molecular mass difference between any two successive members of a homologous series?",
                "options": [
                    "14 atomic mass units (14 u), corresponding to one -CH2- unit",
                    "12 atomic mass units (12 u), corresponding to one carbon atom",
                    "16 atomic mass units (16 u), corresponding to one oxygen atom",
                    "2 atomic mass units (2 u), corresponding to two hydrogen atoms"
                ],
                "answer": 0,
                "hint": "Carbon has mass 12 u; two hydrogens have mass 2 x 1 = 2 u. Total = 12 + 2 = 14 u.",
                "explanation": "Successive members of any homologous series differ by a methylene group (-CH2-). Carbon has mass 12 u and two hydrogens have mass 2 u, yielding a constant mass difference of 14 u.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: M(CH2) = M(C) + 2 * M(H) = 12.011 + (2 * 1.008) = 14.027 u ~ 14 u.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Example in alkanes: CH4 (16 u) -> C2H6 (30 u) -> C3H8 (44 u) -> C4H10 (58 u). Difference between every adjacent pair is exactly 14 u.",
                    "Step 3: Verification & Real-World Application: Example in alcohols: CH3OH (32 u) -> C2H5OH (46 u) -> C3H7OH (60 u). The increment is universal across all homologous series."
                ]
            },
            {
                "id": 7,
                "question": "What is the systematic IUPAC name for an organic compound with molecular formula CH3-CH2-CHO?",
                "options": [
                    "Propanal",
                    "Propanol",
                    "Propanone",
                    "Propanoic acid"
                ],
                "answer": 0,
                "hint": "Three carbons = prop; terminal -CHO group gives the suffix '-al'.",
                "explanation": "A 3-carbon chain with a terminal aldehyde functional group (-CHO) is named propanal (propane - e + al = propanal).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Formula CH3CH2CHO contains 3 carbon atoms. Saturated parent alkane is propane.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Functional group is an aldehyde (-CHO). By IUPAC rules, delete the terminal 'e' of propane and append the suffix 'al': Propanal.",
                    "Step 3: Verification & Real-World Application: Propanol has an -OH group; propanone has an internal >C=O; propanoic acid has a -COOH group."
                ]
            },
            {
                "id": 8,
                "question": "Which of the following represents the correct condensed structural formula of the haloalkane bromopentane?",
                "options": [
                    "CH3-CH2-CH2-CH2-CH2-Br",
                    "CH3-CH2-CH2-Br",
                    "CH3-CH(Br)-CH3",
                    "CH3-CO-CH2-CH2-Br"
                ],
                "answer": 0,
                "hint": "Pentane indicates 5 carbon atoms in the parent chain, with one hydrogen replaced by bromine (-Br).",
                "explanation": "Bromopentane consists of a 5-carbon alkane chain with a bromine atom replacing one hydrogen: CH3-CH2-CH2-CH2-CH2-Br (1-bromopentane).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 'Pent' signifies a 5-carbon backbone: C-C-C-C-C. 'Bromo' prefix denotes a bromine substituent replacing hydrogen.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Unbranched 1-bromopentane formula: C5H11Br, structured as CH3-(CH2)4-Br.",
                    "Step 3: Verification & Real-World Application: NCERT Section 4.2.5 explicitly requires students to draw the structure of bromopentane as part of IUPAC nomenclature exercises."
                ]
            },
            {
                "id": 9,
                "question": "Why does the boiling point of alkanes systematically increase as you move from methane (CH4) to hexane (C6H14)?",
                "options": [
                    "Larger molecular size and mass increase the surface area for intermolecular van der Waals attractions",
                    "Higher alkanes contain nuclear magnets that attract nearby water molecules",
                    "Methane is an ionic crystal, whereas hexane is a liquid metal",
                    "Hexane contains radioactive carbon atoms that prevent boiling"
                ],
                "answer": 0,
                "hint": "Longer carbon chains have greater electron clouds and greater contact surface area.",
                "explanation": "As the carbon chain lengthens, molecular mass and surface area increase, strengthening intermolecular van der Waals forces. More thermal energy is required to vaporise the liquid, raising the boiling point.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Boiling points: CH4 (111 K) < C2H6 (184 K) < C3H8 (231 K) < C4H10 (273 K) < C5H12 (309 K) < C6H14 (342 K).",
                    "Step 2: Reaction Mechanism & Stoichiometry: London dispersion attractive forces scale directly with the polarisability and surface area of the molecular electron cloud.",
                    "Step 3: Verification & Real-World Application: This predictable physical gradation is a defining hallmark of every homologous series in chemistry."
                ]
            },
            {
                "id": 10,
                "question": "What is the general molecular formula for the homologous series of alkenes containing one double bond?",
                "options": [
                    "CnH2n",
                    "CnH2n+2",
                    "CnH2n-2",
                    "CnHn"
                ],
                "answer": 0,
                "hint": "Ethene has 2 carbons and 4 hydrogens (C2H4); propene has 3 carbons and 6 hydrogens (C3H6).",
                "explanation": "Alkenes contain one carbon-carbon double bond and follow the general formula CnH2n (e.g., ethene C2H4, propene C3H6, butene C4H8).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Compare formulas: Alkanes = CnH2n+2; Alkenes = CnH2n; Alkynes = CnH2n-2.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Introducing one C=C double bond removes two hydrogen atoms from the saturated alkane parent formula, yielding CnH2n.",
                    "Step 3: Verification & Real-World Application: For n=2: C2H4 (ethene); for n=3: C3H6 (propene); for n=4: C4H8 (butene)."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Reaction Mechanisms Review",
        "subtitle": "Comprehensive NCERT Review: Combustion, Oxidation, Hydrogenation, and Esterification",
        "speech": "",
        "content": {
            "concept": "Combustion yields CO2, H2O, and energy. Alcohols oxidise to carboxylic acids via alkaline KMnO4. Addition reactions hydrogenate vegetable oils into saturated fats with Ni catalyst. Substitution chlorinates methane in sunlight. Ethanol and ethanoic acid undergo esterification and saponification.",
            "formula": "\\text{Hydrogenation: } \\text{Oil} + \\text{H}_2 \\xrightarrow{\\text{Ni}} \\text{Fat} \\quad | \\quad \\text{Esterification: } \\text{Acid} + \\text{Alcohol} \\xrightleftharpoons{\\text{H}^+} \\text{Ester} + \\text{H}_2\\text{O}",
            "points": [
                "Complete combustion produces clean blue flame; incomplete combustion produces yellow sooty smoke.",
                "Alkaline KMnO4 or acidified K2Cr2O7 oxidises ethanol to ethanoic acid (adds oxygen, removes hydrogen).",
                "Addition reaction: unsaturated vegetable oils + H2 (Ni catalyst) → solid saturated fats (vanaspati ghee).",
                "Substitution reaction: CH4 + Cl2 (in sunlight) → CH3Cl + HCl.",
                "Ethanol reacts with sodium metal to liberate H2 gas and sodium ethoxide (2Na + 2C2H5OH → 2C2H5ONa + H2).",
                "Ethanol dehydrates to ethene when heated with hot concentrated H2SO4 at 443 K.",
                "Esterification: Ethanoic acid + Ethanol (conc. H2SO4) → Sweet fruity ethyl ethanoate ester.",
                "Carboxylic acids produce brisk CO2 effervescence with sodium carbonates/bicarbonates."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "Why is an ethyne and pure oxygen gas mixture used for industrial metal welding, rather than an ethyne and air mixture?",
                "options": [
                    "Burning ethyne in air produces an incomplete, sooty flame with insufficient heat; burning ethyne in pure oxygen yields a clean, high-temperature flame (>3000°C) capable of melting steel",
                    "Air contains helium that extinguishes the welding torch immediately",
                    "Ethyne reacts with atmospheric nitrogen to form poisonous cyanide gas",
                    "Oxygen freezes the metal to weld it by cryo-fusion"
                ],
                "answer": 0,
                "hint": "Incomplete combustion in air wastes energy and produces soot, whereas oxy-acetylene generates intense heat.",
                "explanation": "Ethyne (acetylene) has a high carbon percentage. In air (only 21% O2), incomplete combustion produces a smoky, lower-temperature flame. Pure oxygen ensures complete combustion, generating an intense flame exceeding 3000°C needed to weld metals.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Complete combustion in pure oxygen: 2C2H2 + 5O2 -> 4CO2 + 2H2O + Delta H (intense heat ~3300°C).",
                    "Step 2: Reaction Mechanism & Stoichiometry: In atmospheric air, the 78% inert nitrogen dilutes the flame temperature and limits oxygen availability, causing incomplete combustion and soot deposition.",
                    "Step 3: Verification & Real-World Application: NCERT Section 4.3.1 explicitly explains why oxy-acetylene welding relies on pure cylinder oxygen rather than atmospheric air."
                ]
            },
            {
                "id": 2,
                "question": "What is the chemical function of alkaline potassium permanganate (KMnO4) in the reaction converting ethanol into ethanoic acid?",
                "options": [
                    "It acts as an oxidising agent, supplying nascent oxygen to oxidise the alcohol",
                    "It acts as a reducing agent, removing oxygen from ethanol",
                    "It acts as a dehydrating agent, removing water to produce ethene",
                    "It acts as a detergent, dissolving oily impurities in the flask"
                ],
                "answer": 0,
                "hint": "Substances that supply oxygen to other reactants are called oxidising agents.",
                "explanation": "Alkaline KMnO4 acts as an oxidising agent. It supplies oxygen to convert ethanol (CH3CH2OH) into ethanoic acid (CH3COOH) while discharging its own purple colour.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH3CH2OH + 2[O] (from alkaline KMnO4 + Heat) -> CH3COOH + H2O.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Permanganate ion (MnO4-) in alkaline solution is reduced from Mn(+7) to Mn(+4) (MnO2 precipitate), while oxidising the alcohol carbon from -1 to +3.",
                    "Step 3: Verification & Real-World Application: This reaction proves that alcohol-to-acid conversion is an oxidation process requiring an external oxidising agent."
                ]
            },
            {
                "id": 3,
                "question": "Which of the following organic compounds will decolourise bromine water through an addition reaction?",
                "options": [
                    "Ethene (C2H4)",
                    "Methane (CH4)",
                    "Ethane (C2H6)",
                    "Propane (C3H8)"
                ],
                "answer": 0,
                "hint": "Addition reactions are characteristic of unsaturated hydrocarbons containing double or triple bonds.",
                "explanation": "Ethene (C2H4) is an unsaturated alkene with a reactive double bond. It rapidly undergoes an addition reaction with bromine water, decolourising reddish-brown bromine to form colourless 1,2-dibromoethane.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH2=CH2 + Br2(aq)[reddish-brown] -> CH2Br-CH2Br(aq)[colourless 1,2-dibromoethane].",
                    "Step 2: Reaction Mechanism & Stoichiometry: Electrophilic addition: the pi electron cloud of ethene attacks the polarised bromine molecule, breaking the double bond to form a saturated dibromo derivative.",
                    "Step 3: Verification & Real-World Application: Saturated alkanes (CH4, C2H6, C3H8) lack multiple bonds and cannot decolourise bromine water in the absence of sunlight."
                ]
            },
            {
                "id": 4,
                "question": "What catalyst and reaction conditions are required for the industrial hydrogenation of vegetable oils into vanaspati ghee?",
                "options": [
                    "Hydrogen gas in the presence of a nickel (Ni) or palladium (Pd) catalyst at elevated temperature",
                    "Chlorine gas in the presence of sunlight",
                    "Carbon dioxide gas in the presence of concentrated sulphuric acid",
                    "Liquid water in the presence of limestone"
                ],
                "answer": 0,
                "hint": "Addition of H2 across double bonds in vegetable oils requires a transition metal catalyst.",
                "explanation": "Unsaturated vegetable oils react with hydrogen gas in the presence of a finely divided nickel (Ni) catalyst to saturate the carbon-carbon double bonds, producing solid saturated fats.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: -CH=CH- (liquid vegetable oil) + H2(g) -> -CH2-CH2- (solid saturated fat) using Ni catalyst at ~473 K.",
                    "Step 2: Reaction Mechanism & Stoichiometry: The nickel surface chemisorbs H2 and alkene molecules, lowering the activation energy barrier for syn-addition across the double bond.",
                    "Step 3: Verification & Real-World Application: Vegetable oils contain healthy unsaturated fatty acids; commercial hydrogenation produces solid vanaspati fats (margarine)."
                ]
            },
            {
                "id": 5,
                "question": "What type of chemical reaction occurs when methane reacts with chlorine gas in the presence of diffuse sunlight?",
                "options": [
                    "Substitution reaction (chlorine atoms progressively replace hydrogen atoms)",
                    "Addition reaction (chlorine adds across carbon-carbon bonds)",
                    "Saponification reaction (forming soap and alcohol)",
                    "Esterification reaction (forming fruity esters)"
                ],
                "answer": 0,
                "hint": "Methane is saturated and has only single bonds; one atom replaces another.",
                "explanation": "Methane undergoes a photochemical free-radical substitution reaction where chlorine atoms displace hydrogen atoms one by one in the presence of sunlight: CH4 + Cl2 -> CH3Cl + HCl.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH4 + Cl2 -> CH3Cl (chloromethane) + HCl (in the presence of h*nu sunlight).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Sunlight dissociates Cl2 into two reactive chlorine free radicals (Cl·). A chlorine radical abstracts H from CH4 to form ·CH3, which then attacks another Cl2 molecule.",
                    "Step 3: Verification & Real-World Application: Continued exposure yields CH2Cl2 (dichloromethane), CHCl3 (chloroform), and CCl4 (carbon tetrachloride)."
                ]
            },
            {
                "id": 6,
                "question": "What gas is evolved when a clean piece of sodium metal is dropped into absolute ethanol, and how is it tested?",
                "options": [
                    "Hydrogen gas (H2), confirmed by a burning matchstick producing a characteristic 'pop' sound",
                    "Carbon dioxide gas (CO2), confirmed by turning lime water milky",
                    "Oxygen gas (O2), confirmed by rekindling a glowing wooden splint",
                    "Nitrogen dioxide gas (NO2), confirmed by dense brown fumes"
                ],
                "answer": 0,
                "hint": "2Na + 2C2H5OH -> 2C2H5ONa + H2.",
                "explanation": "Sodium reacts with ethanol to evolve colourless hydrogen gas along with sodium ethoxide: 2Na + 2CH3CH2OH -> 2CH3CH2ONa + H2. Hydrogen gas burns with a classic pop sound.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2CH3CH2OH(l) + 2Na(s) -> 2CH3CH2ONa(alc) + H2(g)↑.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Sodium oxidises to Na+, while acidic protons on the hydroxyl groups of ethanol are reduced to diatomic hydrogen gas.",
                    "Step 3: Verification & Real-World Application: This reaction provides a definitive laboratory test to confirm the presence of an alcohol group in an organic liquid."
                ]
            },
            {
                "id": 7,
                "question": "What product is formed when ethanol is heated with excess concentrated sulphuric acid at 443 Kelvin?",
                "options": [
                    "Ethene (CH2=CH2) and water",
                    "Ethanoic acid and hydrogen gas",
                    "Methane and carbon dioxide",
                    "Diethyl ether and table salt"
                ],
                "answer": 0,
                "hint": "Hot conc. H2SO4 acts as a dehydrating agent, removing water from ethanol.",
                "explanation": "Heating ethanol with excess concentrated H2SO4 at 443 K causes acid dehydration, removing a molecule of water to synthesize ethene (CH3CH2OH -> CH2=CH2 + H2O).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH3CH2OH -> CH2=CH2 + H2O (in the presence of hot conc. H2SO4 at 443 K / 170°C).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Concentrated sulphuric acid protonates the -OH group, followed by elimination of a water molecule and loss of an adjacent proton to establish a C=C double bond.",
                    "Step 3: Verification & Real-World Application: This reaction illustrates the industrial preparation of alkenes from renewable bio-ethanol via catalytic dehydration."
                ]
            },
            {
                "id": 8,
                "question": "What type of organic compound is synthesized during the reaction between ethanoic acid and ethanol in the presence of concentrated sulphuric acid catalyst?",
                "options": [
                    "An ester (ethyl ethanoate), identified by its sweet, fruity aroma",
                    "A soap micelle, identified by thick lather",
                    "An alkane gas, identified by a foul rotten egg smell",
                    "A synthetic detergent, identified by scum formation"
                ],
                "answer": 0,
                "hint": "Carboxylic acid + Alcohol -> Ester + Water (Esterification reaction).",
                "explanation": "Ethanoic acid reacts with ethanol in the presence of an acid catalyst to produce ethyl ethanoate (an ester) and water. Esters possess delightful, sweet fruity fragrances.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH3COOH + CH3CH2OH <===(conc. H2SO4)===> CH3COOCH2CH3 (ethyl ethanoate) + H2O.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Acid-catalysed condensation esterification: the hydroxyl group of the acid and hydrogen of the alcohol combine to eliminate water, forming an ester linkage (-COO-).",
                    "Step 3: Verification & Real-World Application: In Activity 4.8, warming this mixture in a water bath produces a sweet fruity scent, used widely in perfumes and food flavourings."
                ]
            },
            {
                "id": 9,
                "question": "What is 'saponification' in industrial organic chemistry?",
                "options": [
                    "The alkaline hydrolysis of an ester using sodium hydroxide to yield soap and alcohol",
                    "The burning of fossil fuels to produce carbon dioxide",
                    "The dehydration of ethanol into gaseous ethene",
                    "The chlorination of methane in bright sunlight"
                ],
                "answer": 0,
                "hint": "Saponification literally means 'soap-making', reversing the esterification reaction.",
                "explanation": "Saponification is the alkaline hydrolysis of esters using a strong base like sodium hydroxide (NaOH) to produce an alcohol and a sodium carboxylate salt (soap).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH3COOC2H5 (ethyl ethanoate) + NaOH -> C2H5OH (ethanol) + CH3COONa (sodium acetate).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Hydroxide ion (OH-) nucleophilically attacks the carbonyl carbon, cleaving the ester bond and regenerating alcohol while producing a carboxylate salt.",
                    "Step 3: Verification & Real-World Application: Soaps are prepared commercially by saponifying naturally occurring glyceryl esters (fats and oils) with concentrated NaOH or KOH."
                ]
            },
            {
                "id": 10,
                "question": "What observable phenomenon occurs when ethanoic acid is added to a test tube containing sodium hydrogencarbonate (baking soda)?",
                "options": [
                    "Brisk effervescence of colourless carbon dioxide gas that turns lime water milky",
                    "A violent purple explosion releasing chlorine gas",
                    "The solution turns solid yellow with zero gas evolution",
                    "The test tube freezes instantly into solid ice"
                ],
                "answer": 0,
                "hint": "Acid + Carbonate/Bicarbonate -> Salt + Water + Carbon Dioxide gas.",
                "explanation": "Ethanoic acid reacts with sodium hydrogencarbonate (NaHCO3) to produce brisk effervescence of CO2 gas: CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2. The gas turns lime water milky.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: CH3COOH(aq) + NaHCO3(s) -> CH3COONa(aq) + H2O(l) + CO2(g)↑.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Ethanoic acid protonates the hydrogencarbonate ion: H+ + HCO3- -> H2CO3 -> H2O + CO2. Evolving CO2 bubbles cause brisk effervescence.",
                    "Step 3: Verification & Real-World Application: Passing the gas through lime water [Ca(OH)2] forms insoluble CaCO3 precipitate (milky appearance), distinguishing carboxylic acids from neutral alcohols."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Soaps Micelles Review",
        "subtitle": "Comprehensive NCERT Review: Micelle Cleansing, Emulsion Physics, and Hard Water Scum",
        "speech": "",
        "content": {
            "concept": "Soap molecules are sodium/potassium salts of long-chain fatty acids with a hydrophilic ionic head and hydrophobic hydrocarbon tail. In water, they form spherical colloidal micelles that trap oily dirt in the center. Hard water contains Ca2+ and Mg2+ ions forming insoluble scum; synthetic detergents overcome scum.",
            "formula": "\\text{Soap: } \\text{R-COO}^-\\text{Na}^+ \\quad | \\quad \\text{Scum: } 2\\text{R-COO}^- + \\text{Ca}^{2+} \\rightarrow (\\text{R-COO})_2\\text{Ca}\\downarrow",
            "points": [
                "Soap molecules have two ends: hydrophilic ionic head (water-soluble) and hydrophobic hydrocarbon tail (oil-soluble).",
                "Micelle formation: in water, hydrocarbon tails cluster inward around oily dirt; ionic heads face outward toward water.",
                "Soap micelles form a stable colloidal emulsion, allowing oily dirt to be rinsed away with water.",
                "Mechanical agitation (scrubbing/beating) is necessary to dislodge and suspend the trapped oil droplets.",
                "Hard water contains dissolved calcium (Ca2+) and magnesium (Mg2+) ions that react with soap to form insoluble scum.",
                "Detergents are sodium salts of sulfonic acids or ammonium salts; their charged ends do not form scum in hard water."
            ]
        },
        "questions": [
            {
                "id": 1,
                "question": "What are the two structurally distinct chemical ends of a typical soap molecule (such as sodium stearate)?",
                "options": [
                    "A hydrophilic ionic head that interacts with water and a hydrophobic hydrocarbon tail that interacts with oil",
                    "A metallic iron head and an acidic plastic tail",
                    "Two identical hydrophobic ends that dissolve only in kerosene",
                    "Two hydrophilic ionic heads with no hydrocarbon chain"
                ],
                "answer": 0,
                "hint": "Hydrophilic means 'water-loving' (ionic); hydrophobic means 'water-fearing' (hydrocarbon tail).",
                "explanation": "A soap molecule has an amphipathic structure: an ionic hydrophilic head (-COO- Na+) that dissolves in polar water, and a long non-polar hydrophobic hydrocarbon tail that dissolves in non-polar oils and grease.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Sodium stearate formula: C17H35COO- Na+. Hydrocarbon chain C17H35- is non-polar; carboxylate group -COO- Na+ is ionic.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Like dissolves like: the non-polar hydrophobic tail embeds into non-polar oily dirt, while the ionic hydrophilic head remains solvated by polar water dipoles.",
                    "Step 3: Verification & Real-World Application: This dual-affinity structure is indispensable for emulsifying and suspending water-insoluble greases during laundering."
                ]
            },
            {
                "id": 2,
                "question": "What is a 'micelle' in the cleansing mechanism of soaps in aqueous solution (Activity 4.10)?",
                "options": [
                    "A spherical colloidal cluster where hydrophobic hydrocarbon tails point inward trapping oil, and ionic heads point outward toward water",
                    "A solid flat sheet of sodium chloride crystals",
                    "A radioactive particle that dissolves cotton fibers",
                    "A gas bubble composed entirely of pure methane"
                ],
                "answer": 0,
                "hint": "In water, soap molecules assemble radially with oil trapped in the core.",
                "explanation": "In aqueous solution, soap molecules aggregate into spherical clusters called micelles: hydrophobic hydrocarbon tails orient inward to dissolve and trap the oily droplet, while hydrophilic ionic heads face outward into water.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Soap + Water + Oily Dirt -> Colloidal Micelle Emulsion.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Thermodynamic minimization of free energy drives non-polar tails away from water into a central hydrophobic pocket, while ionic carboxylate heads (-COO-) project into the surrounding aqueous medium.",
                    "Step 3: Verification & Real-World Application: Ion-ion electrostatic repulsion between outward-facing negative carboxylate heads prevents individual micelles from coalescing, keeping dirt suspended as an emulsion that rinses away."
                ]
            },
            {
                "id": 3,
                "question": "Why does a soap micelle solution scatter a beam of light (exhibiting the Tyndall effect) and appear somewhat cloudy?",
                "options": [
                    "Soap micelles are colloidal-sized aggregates large enough to scatter incident visible light rays",
                    "Soap absorbs all light and converts it into heat",
                    "Water decomposes into opaque hydrogen gas bubbles",
                    "Soap dissolves the glass walls of the beaker"
                ],
                "answer": 0,
                "hint": "Colloidal particles have dimensions between 1 and 1000 nm, scattering light beams.",
                "explanation": "Soap micelles aggregate into colloidal clusters. Because colloidal particles are large relative to simple dissolved molecules, they scatter light rays (Tyndall effect), making soap solutions appear cloudy or translucent.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: True solutions (particle size < 1 nm) do not scatter visible light. Colloidal micelle aggregates (size 10-100 nm) scatter visible wavelengths.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Rayleigh/Mie light scattering occurs when the refractive index of suspended micelle clusters differs from the continuous aqueous solvent phase.",
                    "Step 3: Verification & Real-World Application: NCERT Section 4.5 notes that soap solutions appear cloudy and scatter light because soap micelles exist as colloidal suspensions."
                ]
            },
            {
                "id": 4,
                "question": "Why do soap micelles fail to form when soap is dissolved in ethanol instead of water?",
                "options": [
                    "Ethanol is a non-polar/organic solvent that dissolves the hydrophobic hydrocarbon tail directly, eliminating the thermodynamic driving force for micelle clustering",
                    "Ethanol reacts with soap to produce explosive dynamite",
                    "Soap is completely insoluble in ethanol and settles as dry stones",
                    "Ethanol converts soap into gaseous carbon dioxide"
                ],
                "answer": 0,
                "hint": "Micelle formation requires a polar solvent (water) that repels the hydrophobic tail.",
                "explanation": "Micelle formation in water is driven by water's high polarity repelling the hydrophobic hydrocarbon tail. Ethanol has lower polarity and dissolves hydrocarbon chains readily; hence, soap molecules dissolve individually without clustering into micelles.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Solvation thermodynamics: In water (dielectric constant 80), water molecules form strong hydrogen-bonded cages around non-polar solutes (hydrophobic effect).",
                    "Step 2: Reaction Mechanism & Stoichiometry: In ethanol (dielectric constant 24), the solvent easily solvates alkyl tails via dispersion forces, removing the hydrophobic penalty. Soap molecules disperse as individual solvated units.",
                    "Step 3: Verification & Real-World Application: NCERT In-Text Question explicitly asks whether micellar aggregation occurs in ethanol; the answer is no, because ethanol dissolves hydrocarbon tails."
                ]
            },
            {
                "id": 5,
                "question": "Why is physical agitation—such as scrubbing with a brush, rubbing by hand, or beating on a stone—necessary when washing clothes with soap?",
                "options": [
                    "Physical force is required to detach the oil droplets surrounded by soap molecules from the fabric fibers so they can be suspended into the water emulsion",
                    "Agitation creates electric sparks that burn off the dirt",
                    "Agitation turns the soap into concentrated sulphuric acid",
                    "Clothes must be heated to boiling temperature through mechanical friction"
                ],
                "answer": 0,
                "hint": "Micelles weaken the adhesion of dirt, but mechanical work is needed to pull the droplets off cloth fibers.",
                "explanation": "The hydrocarbon tails of soap penetrate the oily dirt, loosening its grip on cloth fibers. Mechanical agitation (scrubbing, beating, or washing machine tumbling) dislodges the emulsified dirt droplets into the water to be rinsed away.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Fabric-Dirt Adhesion: Oily grease adheres to cellulose or synthetic textile microfibers through van der Waals surface attractions.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Soap lowers interfacial surface tension and encapsulates oil within micelles. Mechanical shear stress provides kinetic energy to dislodge the encapsulated grease droplets into bulk water.",
                    "Step 3: Verification & Real-World Application: NCERT In-Text Question specifically addresses why physical scrubbing or beating is indispensable for effective laundry cleaning."
                ]
            },
            {
                "id": 6,
                "question": "What causes the formation of an insoluble curdy white precipitate known as 'scum' when soap is added to hard water (Activity 4.11)?",
                "options": [
                    "Divalent calcium (Ca2+) and magnesium (Mg2+) ions in hard water react with soluble soap to form insoluble calcium and magnesium carboxylate precipitates",
                    "Hard water contains solid sand that sticks to the soap",
                    "Soap turns into pure chalk under high water pressure",
                    "Hard water freezes the soap into solid ice crystals"
                ],
                "answer": 0,
                "hint": "2R-COO- Na+ + Ca2+ -> (R-COO)2Ca (insoluble white precipitate) + 2Na+.",
                "explanation": "Hard water contains dissolved calcium (Ca2+) and magnesium (Mg2+) ions. These ions react with soluble sodium soap molecules to form insoluble calcium and magnesium salts of fatty acids, called scum.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: 2C17H35COONa(aq)[soluble soap] + Ca2+(aq)[hard water] -> (C17H35COO)2Ca(s)[insoluble scum]↓ + 2Na+(aq).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Divalent alkaline earth cations crosslink two carboxylate anions, precipitating an insoluble curdy mass that wastes soap and deposits on fabric.",
                    "Step 3: Verification & Real-World Application: Until all Ca2+ and Mg2+ ions are precipitated as scum, soap cannot form lather, wasting significant amounts of cleaning agent."
                ]
            },
            {
                "id": 7,
                "question": "What are synthetic detergents chemically, and why do they remain completely effective even in hard water (Activity 4.12)?",
                "options": [
                    "They are sodium salts of sulfonic acids or ammonium salts whose charged heads do not form insoluble precipitates with calcium and magnesium ions",
                    "They are metallic alloys of lead and tin that dissolve in water",
                    "They are strong mineral acids that dissolve fabric completely",
                    "They contain radioactive isotopes that vaporise hard water minerals"
                ],
                "answer": 0,
                "hint": "Detergents are usually sodium alkylbenzene sulfonates or alkyl sulphates.",
                "explanation": "Detergents are sodium salts of long-chain alkylbenzene sulfonic acids or alkyl sulphates. Their charged sulfonate heads (-SO3- Na+) do not form insoluble precipitates with Ca2+ and Mg2+ ions, so they lather easily even in hard water.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Detergent formula: R-C6H4-SO3- Na+ (sodium alkylbenzene sulfonate). Reaction with Ca2+: 2R-SO3- + Ca2+ -> (R-SO3)2Ca (soluble complex).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Calcium and magnesium sulfonates remain fully soluble in water, preventing scum formation and preserving 100% of the surfactant for micellar cleansing.",
                    "Step 3: Verification & Real-World Application: This chemical property makes synthetic detergents ideal for laundry detergents, shampoos, and dishwashing liquids in regions with hard groundwater."
                ]
            },
            {
                "id": 8,
                "question": "Can you check whether a given sample of water is hard or soft simply by testing it with a synthetic detergent?",
                "options": [
                    "No, because synthetic detergents produce rich lather in both hard and soft water without forming scum",
                    "Yes, because detergents turn bright red in hard water",
                    "Yes, because detergents explode when mixed with hard water",
                    "No, because detergents cannot dissolve in any liquid water"
                ],
                "answer": 0,
                "hint": "Detergents lather equally well in hard and soft water; you must use soap to detect hardness.",
                "explanation": "No. Synthetic detergents form lather abundantly in both hard and soft water without forming insoluble scum. To test for water hardness, soap must be used (soap forms curdy scum in hard water and rich foam in soft water).",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Distinguishing water hardness requires an indicator that reacts differently with Ca2+/Mg2+. Detergents lather freely in both types of water.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Soap + Soft water -> Instant rich lather. Soap + Hard water -> Curdy white scum before any lather forms.",
                    "Step 3: Verification & Real-World Application: NCERT In-Text Question explicitly notes: Detergents cannot be used to test water hardness because they lather readily in all water types."
                ]
            },
            {
                "id": 9,
                "question": "What is the primary ecological disadvantage associated with early non-biodegradable synthetic detergents?",
                "options": [
                    "Highly branched hydrocarbon chains cannot be broken down by aquatic bacteria, causing persistent foaming in rivers and water bodies",
                    "They react with river sand to form volcanic lava",
                    "They turn all river water into concentrated hydrochloric acid",
                    "They produce radioactive fallout in wastewater pipes"
                ],
                "answer": 0,
                "hint": "Bacterial enzymes cannot decompose highly branched alkyl chains, causing environmental water pollution.",
                "explanation": "Early synthetic detergents featured highly branched hydrocarbon chains that bacteria could not biodegrade. They accumulated in sewage effluents, causing persistent foam blankets on rivers and lakes.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Branched alkylbenzene sulfonates (ABS) resist microbial beta-oxidation enzymes in aquatic ecosystems.",
                    "Step 2: Reaction Mechanism & Stoichiometry: Persistent surfactant foam reduces oxygen dissolution in rivers, choking aquatic flora and fauna.",
                    "Step 3: Verification & Real-World Application: Modern synthetic detergents are formulated with unbranched, straight-chain alkyl groups (LAS) that microorganisms easily biodegrade."
                ]
            },
            {
                "id": 10,
                "question": "How does soap prepare a stable emulsion of oil in water, allowing dirt to be washed away during laundering?",
                "options": [
                    "The hydrophobic tails trap oil inside spherical micelles, while outward-facing negatively charged heads repel other micelles, keeping oil droplets suspended in water",
                    "Soap converts the oil droplets into gaseous helium that floats away",
                    "Soap converts liquid water into a solid brick of plastic",
                    "Soap dissolves the fabric fibers so dirt falls to the floor"
                ],
                "answer": 0,
                "hint": "The outward-facing negative ionic heads prevent oil droplets from coalescing together.",
                "explanation": "Soap acts as an emulsifier: its hydrophobic tails trap oil droplets within micelles, while its negatively charged ionic heads project outward into the water. Mutual electrostatic repulsion between negative heads prevents oil droplets from aggregating, maintaining a stable emulsion that rinses away.",
                "solution": [
                    "Step 1: Chemical Equation & Reactants Analysis: Emulsion = Colloidal dispersion of one liquid in another immiscible liquid (oil suspended in water).",
                    "Step 2: Reaction Mechanism & Stoichiometry: Without soap, oil and water quickly separate into two distinct layers. Soap molecules coat oil droplets, presenting a hydrophilic exterior with negative charges (-COO-) that repel adjacent droplets.",
                    "Step 3: Verification & Real-World Application: In Activity 4.10, shaking test tubes of oil and water shows that water and oil separate rapidly, but adding soap creates a persistent, milky emulsion that washes away."
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

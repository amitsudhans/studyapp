"""Generate Slides 1 to 8 for Class 10 Science Chapter 4: Carbon and its Compounds
Strict constraints:
- Title: strictly 1 to 3 words
- Speech: strictly 195 to 215 words
- Pure Indian male teacher voice
- No fictional characters or persona titles
- 2 checkpoints per slide with 4 options, hint, and explanation
"""

slides = [
    {
        "id": 1,
        "title": "Carbon Covalent Bonding",
        "subtitle": "Elemental Ubiquity, Crustal Abundance, and Physical Contrasts with Ionic Salts",
        "speech": "Look around your study room: your clothes, food, medicines, paper notebooks, wooden desk, and plastic pen are all constructed from carbon compounds. Carbon is the undisputed elemental backbone of all terrestrial living structures and organic chemistry. Remarkably, despite this overwhelming ubiquity in everyday life, carbon's natural abundance is surprisingly minuscule: the Earth's crust contains merely zero point zero two percent carbon in the form of minerals like carbonates, coal, and petroleum, while our atmosphere holds only zero point zero three percent carbon dioxide. In Activity 4.1, sorting household articles into metals, glass, and clay reveals that nearly all remaining daily substances belong to the carbon domain. When we examine the physical properties of carbon compounds—such as acetic acid, chloroform, ethanol, and methane in Table 4.1—we uncover a profound chemical contrast with ionic compounds. Carbon compounds exhibit strikingly low melting and boiling points; for example, methane melts at ninety Kelvin and boils at one hundred eleven Kelvin. Furthermore, these organic compounds are exceptionally poor conductors of electricity in both solid and liquid states. This evidence confirms that bonding in carbon compounds does not involve ionic lattices, but rather weak inter-molecular forces with zero free mobile ions.",
        "content": {
            "concept": "Carbon is ubiquitous in all living systems and everyday items, despite making up only 0.02% of Earth's crust and 0.03% of the atmosphere. Carbon compounds have low melting/boiling points and are poor conductors of electricity, indicating covalent bonding with weak intermolecular forces.",
            "formula": "\\text{Crust: } 0.02\\% \\text{ (Carbonates, Coal, Petroleum)} \\quad | \\quad \\text{Atmosphere: } 0.03\\% \\text{ CO}_2",
            "points": [
                "Carbon forms the chemical backbone of all biological structures, food, textiles, and medicines.",
                "Crustal abundance is only 0.02% (minerals, fossil fuels); atmospheric abundance is 0.03% (CO2).",
                "Activity 4.1: Sorting common daily items reveals that the vast majority are carbon compounds.",
                "Carbon compounds possess low melting and boiling points (e.g., methane melts at 90 K, boils at 111 K).",
                "They are electrical insulators because their molecules do not dissociate into free ions."
            ]
        },
        "checkpoints": [
            {
                "question": "What percentage of carbon is found naturally in the Earth's crust and atmosphere, respectively?",
                "options": [
                    "0.02% in crust as minerals; 0.03% in atmosphere as CO2",
                    "20% in crust as coal; 78% in atmosphere as CO2",
                    "5% in crust as limestone; 12% in atmosphere as CO2",
                    "0.5% in crust as petroleum; 5.0% in atmosphere as CO2"
                ],
                "answer": 0,
                "hint": "Carbon is remarkably scarce in non-living reservoirs despite its overwhelming presence in living organisms.",
                "explanation": "The Earth's crust contains just 0.02% carbon in minerals (carbonates, coal, petroleum), and the atmosphere contains only 0.03% carbon dioxide."
            },
            {
                "question": "Why do simple carbon compounds like methane and ethanol possess low melting and boiling points compared to ionic salts?",
                "options": [
                    "They contain radioactive protons that evaporate at room temperature",
                    "Inter-molecular attractive forces between covalent molecules are relatively weak",
                    "They possess infinitely rigid metallic crystal lattices",
                    "Carbon atoms undergo rapid nuclear fission when heated"
                ],
                "answer": 1,
                "hint": "Covalent molecules have strong internal bonds but weak forces between separate molecules.",
                "explanation": "In covalent carbon compounds, atoms are strongly bonded within molecules, but intermolecular forces between separate molecules are weak, requiring minimal thermal energy to overcome."
            }
        ]
    },
    {
        "id": 2,
        "title": "Valence Electron Sharing",
        "subtitle": "Tetravalent Dilemma: Energy Barriers to Ionisation and Covalent Resolution",
        "speech": "Why does carbon choose to share electrons rather than form ionic bonds like sodium or magnesium? Carbon has atomic number six, giving it an electronic configuration of two, four, with four electrons residing in its outer valence shell. To attain the stable octet of the nearest noble gas, neon, carbon requires four additional electrons. However, gaining four electrons to form a C4 minus anion is energetically impossible: the tiny carbon nucleus containing only six protons cannot stably hold ten electrons due to overwhelming inter-electronic repulsion. Conversely, losing four valence electrons to form a C4 plus cation is equally prohibitive: removing four successive electrons demands an astronomical quantity of ionisation energy, leaving a naked, unstable nucleus holding just two inner electrons. Because neither anion nor cation formation is thermodynamically viable, carbon overcomes this obstacle through a brilliant chemical alternative: sharing its four valence electrons with other carbon atoms or with atoms of other elements. By mutually sharing electron pairs, each participating atom attains a completely filled, ultra-stable valence shell without creating destabilising electrical charges. This mutual sharing of valence electron pairs constitutes a covalent bond, unlocking the vast, stable architecture of organic chemistry across the natural universe.",
        "content": {
            "concept": "Carbon has valence configuration 2,4. Forming C4- is impossible because 6 protons cannot hold 10 electrons; forming C4+ requires massive ionization energy. Carbon resolves this by sharing 4 valence electrons to achieve noble gas stability via covalent bonding.",
            "formula": "\\text{C } (Z=6): 1s^2 2s^2 2p^2 \\quad [2,4] \\quad \\xrightarrow{\\text{Sharing } 4e^-} \\text{Stable Octet } [2,8] \\text{ (Neon Core)}",
            "points": [
                "Carbon has atomic number 6 with 4 valence electrons (tetravalent).",
                "Forming C4- is unstable: 6 protons cannot hold 10 electrons due to inter-electron repulsion.",
                "Forming C4+ is impossible: requires enormous energy to strip four successive electrons.",
                "Carbon overcomes this by sharing valence electrons with other atoms.",
                "Shared electron pairs belong to the outer shells of both atoms, achieving noble gas octets."
            ]
        },
        "checkpoints": [
            {
                "question": "Why is it thermodynamically impossible for a carbon atom to form a C4- tetra-anion by gaining four electrons?",
                "options": [
                    "A nucleus with only six protons cannot stably hold ten electrons against electron-electron repulsion",
                    "Carbon has zero protons in its atomic nucleus",
                    "Gaining electrons causes carbon to transform into liquid helium",
                    "Electrons can never be captured by non-metallic elements"
                ],
                "answer": 0,
                "hint": "Consider the ratio of positive nuclear charge (6 protons) to negative orbital charge (10 electrons).",
                "explanation": "If carbon gained 4 electrons to form C4-, its small nucleus with only 6 protons could not hold onto 10 electrons due to intense electrostatic repulsion between electrons."
            },
            {
                "question": "How does a neutral carbon atom achieve a stable noble gas configuration without gaining or losing four electrons?",
                "options": [
                    "By undergoing alpha decay into beryllium",
                    "By sharing its four valence electrons with other atoms in covalent bonds",
                    "By absorbing gamma radiation from outer space",
                    "By permanently dissolving in liquid water"
                ],
                "answer": 1,
                "hint": "Mutual contribution and mutual ownership of electron pairs avoids forming high-energy ions.",
                "explanation": "Carbon overcomes the ionisation energy and charge barriers by sharing its valence electrons with other atoms, forming covalent bonds where both atoms share electron pairs."
            }
        ]
    },
    {
        "id": 3,
        "title": "Covalent Bond Types",
        "subtitle": "Single, Double, and Triple Electron Sharing in Simple Molecules",
        "speech": "Covalent bonding is not exclusive to carbon; it represents a universal mechanism by which non-metals achieve noble gas electronic stability. The simplest illustration is the diatomic hydrogen molecule, H2. A hydrogen atom possesses atomic number one with a single valence electron in its K-shell. Two hydrogen atoms share one pair of electrons, allowing both to attain the stable duplet configuration of helium, joined by a single covalent bond represented by a single line. In chlorine, Cl2, two atoms with configuration two, eight, seven share one pair of electrons to complete their octets. In a methane molecule, CH4, a central tetravalent carbon atom shares its four valence electrons with four individual hydrogen atoms, creating four robust single covalent bonds. When atoms require two electrons to complete their octet, they share two electron pairs to form a double covalent bond, as seen in diatomic oxygen, O2, where two oxygen atoms share four electrons. When atoms require three electrons, as in diatomic nitrogen, N2, each atom contributes three valence electrons, resulting in a powerful triple covalent bond. In carbon dioxide, CO2, carbon forms two separate double bonds with two flanking oxygen atoms, illustrating multi-centre covalent sharing throughout molecular chemistry.",
        "content": {
            "concept": "Covalent bonds form by sharing electron pairs: single bond (1 pair shared, e.g., H2, Cl2, CH4), double bond (2 pairs shared, e.g., O2, CO2), and triple bond (3 pairs shared, e.g., N2, ethyne).",
            "formula": "\\text{Single: } \\text{H}-\\text{H} \\quad | \\quad \\text{Double: } \\text{O}=\\text{O} \\quad | \\quad \\text{Triple: } \\text{N}\\equiv\\text{N} \\quad | \\quad \\text{Methane: } \\text{CH}_4",
            "points": [
                "Single covalent bond: sharing of one electron pair (e.g., H2, Cl2, CH4).",
                "In methane (CH4), carbon shares 4 valence electrons with 4 hydrogen atoms.",
                "Double covalent bond: sharing of two electron pairs (e.g., O2, CO2).",
                "Triple covalent bond: sharing of three electron pairs (e.g., N2, C2H2).",
                "Electron dot structures (Lewis structures) map shared and unshared valence pairs."
            ]
        },
        "checkpoints": [
            {
                "question": "How many total covalent bonds and shared electron pairs are present in a single molecule of methane (CH4)?",
                "options": [
                    "Four single covalent bonds consisting of four shared electron pairs",
                    "One quadruple covalent bond consisting of eight shared electrons",
                    "Two double bonds with four shared pairs",
                    "Zero covalent bonds; methane is an ionic salt"
                ],
                "answer": 0,
                "hint": "Carbon shares one electron with each of four hydrogen atoms.",
                "explanation": "In methane (CH4), tetravalent carbon forms four single covalent bonds by sharing one electron pair with each of four hydrogen atoms, totaling 4 shared electron pairs (8 shared electrons)."
            },
            {
                "question": "How many pairs of valence electrons are shared between the two nitrogen atoms in a diatomic nitrogen molecule (N2)?",
                "options": [
                    "One pair (single bond)",
                    "Two pairs (double bond)",
                    "Three pairs (triple bond)",
                    "Four pairs (quadruple bond)"
                ],
                "answer": 2,
                "hint": "Nitrogen has atomic number 7 (2,5) and needs 3 electrons to complete its valence octet.",
                "explanation": "Each nitrogen atom has 5 valence electrons and needs 3 more. Two nitrogen atoms share three pairs of electrons, forming a strong triple covalent bond (N≡N)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Carbon Allotrope Structures",
        "subtitle": "Diamond Tetrahedral Network, Graphite Planar Layers, and C60 Fullerene",
        "speech": "Elemental carbon demonstrates that structural geometry dictates physical behaviour through allotropy—the phenomenon where an element exists in multiple distinct physical forms with identical chemical identities but contrasting physical architectures. In diamond, each carbon atom is covalently linked to four adjacent carbon atoms in a rigid, three-dimensional tetrahedral network. Because every single valence electron is locked firmly in localised covalent bonds and the inter-atomic spacing is compact, diamond is the hardest natural substance known to science, with an extraordinary melting point, while behaving as an electrical insulator. Conversely, in graphite, each carbon atom bonds to only three neighbouring carbon atoms within flat, planar hexagonal arrays. This specific geometry leaves one delocalised valence electron per carbon atom free to move across the sheets. The parallel hexagonal layers are held together only by weak van der Waals forces, allowing them to slide smoothly over one another; hence, graphite is soft, slippery, and an exceptional electrical conductor. A third allotrope, discovered in the year 1985, is Buckminsterfullerene, C60, where sixty carbon atoms assemble into twenty hexagons and twelve pentagons, forming a hollow spherical cage resembling the geodesic domes designed by famous American architect Buckminster Fuller in innovative modern architectural engineering.",
        "content": {
            "concept": "Allotropes have identical chemical composition but different structures. Diamond: 3D tetrahedral network, hardest substance, electrical insulator. Graphite: layered hexagonal sheets with free delocalised electrons, slippery lubricant, electrical conductor. Fullerene (C60): spherical football cage.",
            "formula": "\\text{Diamond: 3D Tetrahedral } (sp^3) \\quad | \\quad \\text{Graphite: 2D Hexagonal Layers } (sp^2) \\quad | \\quad \\text{C}_{60} \\text{ Fullerene}",
            "points": [
                "Diamond: each carbon bonds to 4 carbons in a rigid 3D tetrahedral lattice (hardest known substance).",
                "Diamond has no free electrons and is an electrical insulator with an extremely high melting point.",
                "Graphite: each carbon bonds to 3 carbons in hexagonal planes; 4th electron is delocalised.",
                "Graphite conducts electricity and has slippery layers used as a solid industrial lubricant.",
                "Buckminsterfullerene (C60) consists of 60 carbon atoms arranged in a spherical football cage."
            ]
        },
        "checkpoints": [
            {
                "question": "Why is graphite an excellent conductor of electricity, whereas diamond is a complete electrical insulator?",
                "options": [
                    "Graphite contains delocalised valence electrons free to migrate; diamond locks all four valence electrons in bonds",
                    "Diamond contains no protons in its nucleus, preventing electrical flow",
                    "Graphite is a metal alloy of lead and tin",
                    "Diamond evaporates into carbon dioxide whenever voltage is applied"
                ],
                "answer": 0,
                "hint": "In graphite, each carbon bonds to only 3 neighbors, leaving the fourth electron free to move.",
                "explanation": "In graphite, each carbon atom bonds to 3 others, leaving one delocalised electron per atom free to conduct electric current. In diamond, all 4 valence electrons are tightly locked in rigid 3D tetrahedral covalent bonds."
            },
            {
                "question": "What geometric architecture characterizes the Buckminsterfullerene (C60) allotrope of carbon?",
                "options": [
                    "A hollow spherical cage of 60 carbon atoms arranged in interlocking hexagons and pentagons like a football",
                    "An infinitely long linear chain of carbon atoms linked by ionic bonds",
                    "A flat triangular sheet identical to common window glass",
                    "A dense cube of pure radioactive carbon isotopes"
                ],
                "answer": 0,
                "hint": "Named after architect Buckminster Fuller, it resembles a classic soccer ball and geodesic dome.",
                "explanation": "Buckminsterfullerene (C60) consists of 60 carbon atoms linked in interlocking pentagons and hexagons to form a hollow spherical cage resembling a soccer ball."
            }
        ]
    },
    {
        "id": 5,
        "title": "Carbon Versatile Nature",
        "subtitle": "Catenation Self-Linking, Tetravalency, and Compact Nuclear Stability",
        "speech": "Chemists have catalogued millions of distinct carbon compounds, vastly outnumbering the chemical compounds formed by all other elements of the periodic table combined together in science. What unique atomic superpowers explain carbon's versatile nature in the physical world? Two foundational properties account for this astonishing molecular diversity: catenation and tetravalency combined with compact atomic size. Catenation is the unparalleled ability of an element to form strong, stable covalent bonds with other atoms of its own kind, giving rise to gigantic molecular architectures. Carbon atoms can link together continuously to forge unbranched straight chains, intricately branched dendrites, and closed cyclic rings of virtually unlimited size. Furthermore, carbon-carbon linkages can incorporate single, double, or triple covalent bonds freely. While silicon also exhibits catenation with hydrogen, forming silanes up to seven or eight atoms, silicon-silicon bonds are weak and chemically reactive; in contrast, carbon-carbon bonds are extraordinarily strong, robust, and thermodynamically resilient. The second vital factor is carbon's tetravalency combined with its small atomic radius. Because carbon possesses only two compact electron shells, its nucleus is situated very close to the shared valence electron pairs, holding them with immense electrostatic tenacity and conferring exceptional thermodynamic stability on carbon compounds throughout nature.",
        "content": {
            "concept": "Carbon forms millions of compounds due to two unique properties: Catenation (ability to self-link into long chains, branches, and rings via single, double, or triple bonds) and Tetravalency with small atomic size (strong nuclear grip on shared electrons).",
            "formula": "\\text{Catenation: } -\\text{C}-\\text{C}-\\text{C}-\\text{C}- \\quad | \\quad \\text{Bond Energy: } \\text{C}-\\text{C } (348\\text{ kJ/mol}) \\gg \\text{Si}-\\text{Si } (222\\text{ kJ/mol})",
            "points": [
                "Catenation: the unique ability of carbon atoms to form stable covalent bonds with other carbon atoms.",
                "Forms straight chains, branched frameworks, and closed cyclic rings of varying complexity.",
                "Can form single (C-C), double (C=C), or triple (C≡C) bonds between carbon atoms.",
                "Silicon forms chains up to 7-8 atoms, but Si-Si bonds are weak and reactive; C-C bonds are exceptionally strong.",
                "Small atomic size of carbon allows its nucleus to hold shared electron pairs tightly and stably."
            ]
        },
        "checkpoints": [
            {
                "question": "What is 'catenation' in organic chemistry, and why is carbon exceptionally proficient at it?",
                "options": [
                    "The ability of an element to form strong, stable covalent bonds with atoms of its own kind",
                    "The process of converting metals into radioactive noble gases",
                    "The property of dissolving completely in liquid nitrogen",
                    "The chemical destruction of atomic nuclei through acid attack"
                ],
                "answer": 0,
                "hint": "Carbon links with itself to form long chains, branches, and rings.",
                "explanation": "Catenation is the ability of an element to bond with itself to form chains, branches, and rings. Carbon-carbon bonds are strong and stable due to carbon's compact atomic radius."
            },
            {
                "question": "Why are carbon-carbon covalent bonds substantially stronger and more stable than silicon-silicon bonds?",
                "options": [
                    "Carbon has a much smaller atomic size, allowing its nucleus to hold shared electron pairs tightly",
                    "Silicon atoms possess zero protons and cannot form covalent bonds",
                    "Carbon atoms are magnetic and pull each other together by magnetic fields",
                    "Silicon compounds can only exist at absolute zero"
                ],
                "answer": 0,
                "hint": "Smaller atomic radius means the positive nucleus is closer to the shared electron cloud.",
                "explanation": "Carbon's small atomic radius allows its nucleus to hold shared electron pairs tightly. Silicon has larger atoms, making Si-Si bonds longer, weaker, and chemically unstable."
            }
        ]
    },
    {
        "id": 6,
        "title": "Vital Force Demise",
        "subtitle": "Overthrow of Vitalism and Friedrich Wöhler's 1828 Urea Synthesis",
        "speech": "For centuries, early scientists believed that carbon compounds synthesized by living organisms were fundamentally distinct from inanimate mineral compounds found in the earth. It was long standing dogma that organic compounds could only be fabricated inside biological tissues under the influence of a mysterious, supernatural life energy termed the vital force. Consequently, chemists believed it was inherently impossible to manufacture an organic compound artificially from non-living inorganic mineral reagents in a laboratory test tube. This mystical dogma collapsed completely in 1828 when German chemist Friedrich Wöhler performed a landmark experiment in his laboratory. Wöhler heated ammonium cyanate—a purely inorganic, crystalline mineral salt—and discovered that its atoms rearranged to produce urea, a well-known organic compound excreted in animal urine: ammonium cyanate yields urea upon thermal treatment. This monumental discovery proved conclusively that organic substances obey the exact same physical and chemical laws of valence and thermodynamics as inorganic compounds, requiring no mystical vital force whatsoever. Although the vital force theory was permanently discredited, all carbon compounds—excluding simple oxides like carbon monoxide and dioxide, carbonates, and hydrogencarbonates—continue to be studied systematically under the specialized branch known as organic chemistry because of their vast numbers and unique catenated bonding.",
        "content": {
            "concept": "The historical 'vital force' theory held that organic compounds could only be formed inside living beings. In 1828, Friedrich Wöhler disproved this by synthesizing urea (organic) from ammonium cyanate (inorganic salt) by heating.",
            "formula": "\\text{NH}_4\\text{CNO } (\\text{Inorganic Ammonium Cyanate}) \\xrightarrow{\\Delta} \\text{NH}_2\\text{CONH}_2 \\text{ (Organic Urea)}",
            "points": [
                "Early chemists believed a mysterious 'vital force' was required to produce organic compounds.",
                "In 1828, Friedrich Wöhler heated inorganic ammonium cyanate and produced organic urea.",
                "This single reaction disproved the vital force theory and founded modern synthetic organic chemistry.",
                "Organic compounds obey the same chemical and thermodynamic laws as inorganic substances.",
                "Carbon oxides (CO, CO2), carbonates, and bicarbonates are studied as inorganic carbon compounds."
            ]
        },
        "checkpoints": [
            {
                "question": "How did Friedrich Wöhler permanently disprove the mystical 'vital force' theory of organic compounds in 1828?",
                "options": [
                    "By synthesizing organic urea in the laboratory by heating inorganic ammonium cyanate",
                    "By proving that living cells run entirely on nuclear energy",
                    "By extracting pure liquid gold from river water",
                    "By inventing the electric light bulb from graphite fibers"
                ],
                "answer": 0,
                "hint": "He turned an inorganic salt into a compound found in animal urine without any living organism.",
                "explanation": "In 1828, Friedrich Wöhler heated inorganic ammonium cyanate (NH4CNO) and synthesized urea (NH2CONH2), proving that organic compounds can be made from inorganic precursors without any 'vital force'."
            },
            {
                "question": "Which of the following carbon-containing substances is classified as an inorganic compound rather than an organic compound?",
                "options": [
                    "Calcium carbonate (CaCO3)",
                    "Methane (CH4)",
                    "Ethanol (C2H5OH)",
                    "Ethanoic acid (CH3COOH)"
                ],
                "answer": 0,
                "hint": "Carbonates, oxides, and bicarbonates are traditionally classified under inorganic chemistry.",
                "explanation": "Carbonates (like CaCO3), hydrogencarbonates, and oxides of carbon (CO, CO2) are classified as inorganic compounds due to their structure and mineral origin."
            }
        ]
    },
    {
        "id": 7,
        "title": "Hydrocarbon Saturation States",
        "subtitle": "Single-Bonded Alkanes versus Double-Bonded Alkenes and Triple-Bonded Alkynes",
        "speech": "Hydrocarbons are fundamental organic compounds composed exclusively of carbon and hydrogen atoms, classified into two broad primary categories based on their internal bonding: saturated and unsaturated hydrocarbons. Saturated hydrocarbons are compounds in which all adjacent carbon atoms are linked exclusively by single covalent bonds. These compounds are known systematically as alkanes, following the general formula C n H 2n plus 2. Everyday representative examples include methane CH4, ethane C2H6, and propane C3H8. Because every carbon valence is completely satisfied by single sigma bonds, saturated hydrocarbons are relatively stable and chemically unreactive under normal laboratory conditions. Conversely, unsaturated hydrocarbons contain at least one multiple bond between adjacent carbon atoms. Unsaturated compounds containing one or more double bonds are termed alkenes, possessing the general formula C n H 2n; the simplest alkene is ethene, C2H4, where two carbon atoms share four electrons. Unsaturated compounds containing one or more carbon-carbon triple bonds are termed alkynes, following the general formula C n H 2n minus 2; the simplest alkyne is ethyne, C2H2, commonly known as industrial acetylene gas. Unsaturated hydrocarbons are substantially more reactive than saturated alkanes because multiple electron-rich pi bonds readily open up to undergo rapid addition reactions.",
        "content": {
            "concept": "Saturated hydrocarbons (alkanes, CnH2n+2) have only single C-C bonds and are relatively unreactive. Unsaturated hydrocarbons have double bonds (alkenes, CnH2n) or triple bonds (alkynes, CnH2n-2) and undergo addition reactions.",
            "formula": "\\text{Alkanes: } \\text{C}_n\\text{H}_{2n+2} \\quad | \\quad \\text{Alkenes: } \\text{C}_n\\text{H}_{2n} \\quad | \\quad \\text{Alkynes: } \\text{C}_n\\text{H}_{2n-2}",
            "points": [
                "Saturated hydrocarbons (alkanes) contain only single carbon-carbon bonds (general formula CnH2n+2).",
                "Examples: Methane (CH4), Ethane (C2H6), Propane (C3H8).",
                "Unsaturated hydrocarbons contain double bonds (alkenes, CnH2n) or triple bonds (alkynes, CnH2n-2).",
                "Simplest alkene is ethene (C2H4, H2C=CH2); simplest alkyne is ethyne (C2H2, HC≡CH).",
                "Unsaturated hydrocarbons are significantly more reactive than alkanes due to electron-rich multiple bonds."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the general molecular formula and bond classification for the homologous family of saturated alkanes?",
                "options": [
                    "CnH2n+2, linked exclusively by single carbon-carbon covalent bonds",
                    "CnH2n, linked by carbon-carbon double bonds",
                    "CnH2n-2, linked by carbon-carbon triple bonds",
                    "CnHn, linked by alternating ionic bonds"
                ],
                "answer": 0,
                "hint": "For n carbons, saturated alkanes have 2n + 2 hydrogens.",
                "explanation": "Alkanes are saturated hydrocarbons containing only single C-C bonds, with the general formula CnH2n+2 (e.g., methane CH4, ethane C2H6)."
            },
            {
                "question": "What is the systematic name and molecular formula of the simplest unsaturated hydrocarbon containing a carbon-carbon triple bond?",
                "options": [
                    "Ethyne (C2H2)",
                    "Ethene (C2H4)",
                    "Ethane (C2H6)",
                    "Methane (CH4)"
                ],
                "answer": 0,
                "hint": "Its common industrial name is acetylene, used in oxy-acetylene welding.",
                "explanation": "Ethyne (C2H2), commonly known as acetylene, is the simplest alkyne containing a carbon-carbon triple bond (H-C≡C-H)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Chains Branches Rings",
        "subtitle": "Structural Isomerism in Butane and Cyclic Saturated and Aromatic Ring Systems",
        "speech": "Carbon's catenation capability allows carbon skeletons to assemble into diverse topological arrangements: straight continuous chains, branched frameworks, and closed cyclic rings. As explored in Table 4.2, straight-chain alkanes extend from methane through hexane, C6H14. When a hydrocarbon contains four or more carbon atoms, an intriguing chemical phenomenon arises: structural isomerism. Structural isomers are chemical compounds that possess the exact same molecular formula but exhibit completely different structural arrangements of atoms in space. For instance, with butane, formula C4H10, carbon atoms can link into a continuous four-carbon unbranched chain called normal-butane, or three carbon atoms can form a main chain with the fourth carbon branching off the central atom to form isobutane, systematically named 2-methylpropane. Both isomers share the formula C4H10 but exhibit distinctly different boiling points and densities. Carbon chains can also bend and join end-to-end to form closed cyclic rings. In cyclohexane, formula C6H12, six carbon atoms form a saturated hexagonal ring linked by single bonds, with each carbon carrying two hydrogens. In contrast, benzene, formula C6H6, is an unsaturated aromatic hexagonal ring containing three alternating carbon-carbon double bonds and three single bonds, forming an exceptionally stable conjugated electronic ring system in modern organic chemistry.",
        "content": {
            "concept": "Carbon skeletons form straight chains, branched chains, and rings. Structural isomers share the same molecular formula but different structural arrangements (e.g., n-butane and isobutane, C4H10). Rings can be saturated (cyclohexane, C6H12) or unsaturated (benzene, C6H6).",
            "formula": "\\text{Butane Isomers: } \\text{C}_4\\text{H}_{10} \\quad | \\quad \\text{Cyclohexane: } \\text{C}_6\\text{H}_{12} \\quad | \\quad \\text{Benzene: } \\text{C}_6\\text{H}_6",
            "points": [
                "Structural isomers have identical molecular formulas but different structural connectivity.",
                "Butane (C4H10) has two isomers: n-butane (straight chain) and isobutane / 2-methylpropane (branched).",
                "Pentane (C5H12) has three isomers: n-pentane, isopentane (2-methylbutane), and neopentane (2,2-dimethylpropane).",
                "Cyclic hydrocarbons form rings: Cyclohexane (C6H12) is a saturated ring with only single bonds.",
                "Benzene (C6H6) is an unsaturated cyclic compound with alternating single and double bonds."
            ]
        },
        "checkpoints": [
            {
                "question": "What are structural isomers in organic chemistry, as demonstrated by the two forms of butane (C4H10)?",
                "options": [
                    "Compounds with identical molecular formulas but different structural arrangements of atoms",
                    "Molecules that contain different chemical elements entirely",
                    "Identical compounds that have different radioactive half-lives",
                    "Atoms that have different numbers of neutrons in their nucleus"
                ],
                "answer": 0,
                "hint": "Same chemical formula (C4H10), but one is a straight chain and the other is branched.",
                "explanation": "Structural isomers are compounds that share the same molecular formula but differ in how their atoms are connected in space (e.g., straight-chain n-butane vs branched isobutane)."
            },
            {
                "question": "How many double bonds and single bonds are present in the hexagonal carbon ring of benzene (C6H6)?",
                "options": [
                    "Three alternating double bonds and three single bonds",
                    "Six continuous double bonds",
                    "Zero double bonds; all bonds are single",
                    "Two triple bonds and two single bonds"
                ],
                "answer": 0,
                "hint": "Benzene has formula C6H6, where each carbon is bonded to one hydrogen and shares alternating single and double bonds in the ring.",
                "explanation": "Benzene (C6H6) consists of a 6-carbon hexagonal ring with alternating single and double bonds (three C-C single bonds and three C=C double bonds)."
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
    print("All slides 1 to 8 validated successfully!")

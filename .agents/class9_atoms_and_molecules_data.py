# -*- coding: utf-8 -*-
"""
Class 9 Science - Chapter 7: Atoms and Molecules
Curriculum Data with 20 Slides:
- Slides 1-16: Core Content with 32 In-Slide Checkpoints (2 per slide) and 16 Bespoke Simulators
- Slides 17-20: 4 Dedicated Quiz Challenge Slides (40 Questions Total, 10 per slide) with Step-by-Step Pop-up Solutions
- Full alignment with competencies: C-1.1, C-1.3, C-5.1, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
"""

SLIDES_DATA = [
    {
        "id": 1,
        "badge": "Slide 01 • Competency C-1.1, C-7.1",
        "title": "Chemical Combination & Lavoisier's Law of Conservation of Mass",
        "subtitle": "Matter cannot be created or destroyed in chemical transformations",
        "teacher": "Welcome to our Atoms and Molecules Master Lab! In 1774, Antoine Lavoisier revolutionized chemistry by introducing quantitative mass measurements. He established the Law of Conservation of Mass: in any chemical reaction, the total mass of the reactants always equals the total mass of the products. Let's explore the classic closed conical flask experiment where barium chloride and sodium sulphate react to form an insoluble white precipitate.",
        "theory": [
            "<strong>Antoine Laurent Lavoisier (1743–1794)</strong> is universally recognized as the Father of Modern Chemistry for transitioning chemistry from qualitative alchemical speculation to rigorous quantitative mass-based science.",
            "<strong>The Law of Conservation of Mass states:</strong> <em>'Mass can neither be created nor destroyed in a chemical reaction.'</em> Total mass of reactants = Total mass of products.",
            "<strong>Classic Demonstration Activity:</strong> Prepare aqueous solutions of Barium Chloride (\\(BaCl_2\\)) and Sodium Sulphate (\\(Na_2SO_4\\)). Place \\(10\\text{ mL}\\) of \\(Na_2SO_4\\) in a conical flask, and suspend a small ignition tube containing \\(5\\text{ mL}\\) of \\(BaCl_2\\) inside using a thread, sealed with a rubber cork.",
            "Weigh the entire sealed apparatus on an analytical balance (e.g. \\(142.50\\text{ g}\\)). Now tilt and swirl the flask so the two clear solutions mix. An immediate double displacement reaction occurs:",
            "$$\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\longrightarrow \\text{BaSO}_4(s)\\downarrow \\text{ (white precipitate)} + 2\\text{NaCl}(aq)$$",
            "Reweighing the flask reveals the exact same reading: \\(142.50\\text{ g}\\). The physical state changed and a solid precipitated, but not a single atom was lost or created.",
            "<strong>Crucial Laboratory Safety:</strong> The flask must be tightly corked to prevent loss of volatile vapors or atmospheric exchange, ensuring a strictly closed thermodynamic system."
        ],
        "key_points": [
            "Law of Conservation of Mass: Mass of Reactants = Mass of Products.",
            "Formulated by Antoine Lavoisier in 1774 using high-precision analytical balances.",
            "Precipitation of white \\(BaSO_4\\) verifies mass conservation in a sealed flask.",
            "A closed system prevents matter exchange with the external surroundings."
        ],
        "checkpoints": [
            {
                "num": 1,
                "q": "If 10.0 g of calcium carbonate (CaCO₃) is heated in a closed vessel and decomposes into 5.6 g of calcium oxide (CaO) and carbon dioxide gas (CO₂), what is the mass of CO₂ produced?",
                "options": ["3.4 g", "4.4 g", "5.6 g", "10.0 g"],
                "ans": 1,
                "exp": "By the Law of Conservation of Mass, Mass of Reactant (CaCO₃) = Mass of CaO + Mass of CO₂. Therefore: Mass of CO₂ = 10.0 g - 5.6 g = 4.4 g."
            },
            {
                "num": 2,
                "q": "Why is it essential to put a tight rubber cork on the conical flask when verifying the law of conservation of mass?",
                "options": [
                    "To prevent atmospheric pressure from breaking the glassware",
                    "To ensure no gaseous reactants or products escape into the surroundings",
                    "To accelerate the rate of the chemical reaction",
                    "To keep the solution at a constant temperature"
                ],
                "ans": 1,
                "exp": "A tight rubber cork seals the system. If any gaseous product (like CO₂ or water vapor) escapes into the atmosphere, the open system would show an apparent loss of mass, violating accurate measurement of mass conservation."
            }
        ]
    },
    {
        "id": 2,
        "badge": "Slide 02 • Competency C-1.1, C-7.1",
        "title": "Law of Constant Proportions & Joseph Proust",
        "subtitle": "Elements combine in definite, fixed ratios by mass",
        "teacher": "Following Lavoisier, French chemist Joseph Proust announced the Law of Constant Proportions in 1799. Whether water is gathered from the Ganges, Antarctic ice, or synthesized in a laboratory from pure hydrogen and oxygen, it always contains hydrogen and oxygen combined in a fixed mass ratio of 1 to 8. Let's see how nature preserves this stoichiometry.",
        "theory": [
            "<strong>Joseph Louis Proust (1754–1826)</strong> established the <strong>Law of Constant Proportions</strong> (also known as the <em>Law of Definite Proportions</em>):",
            "<em>'In a chemical substance, the elements are always present in definite proportions by mass.'</em>",
            "<strong>Example 1: Pure Water (\\(\\text{H}_2\\text{O}\\)):</strong>",
            "Water consists of 2 atoms of Hydrogen (atomic mass \\(1\\text{ u}\\)) and 1 atom of Oxygen (atomic mass \\(16\\text{ u}\\)). The mass ratio is:",
            "$$\\text{Mass of H} : \\text{Mass of O} = (2 \\times 1) : (1 \\times 16) = 2 : 16 = 1 : 8$$",
            "This implies that if \\(9\\text{ g}\\) of water is decomposed by electrolysis, it will yield exactly \\(1\\text{ g}\\) of hydrogen gas and \\(8\\text{ g}\\) of oxygen gas. If you react \\(3\\text{ g}\\) of hydrogen with \\(16\\text{ g}\\) of oxygen, only \\(2\\text{ g}\\) of hydrogen will react with \\(16\\text{ g}\\) of oxygen to give \\(18\\text{ g}\\) of water; \\(1\\text{ g}\\) of unreacted hydrogen will remain as excess reactant!",
            "<strong>Example 2: Ammonia (\\(\\text{NH}_3\\)):</strong> Nitrogen (\\(14\\text{ u}\\)) and Hydrogen (\\(3 \\times 1\\text{ u}\\)) always combine in a fixed mass ratio of \\(14 : 3\\).",
            "<strong>Example 3: Carbon Dioxide (\\(\\text{CO}_2\\)):</strong> Carbon (\\(12\\text{ u}\\)) and Oxygen (\\(2 \\times 16 = 32\\text{ u}\\)) always combine in \\(12 : 32 = 3 : 8\\) mass ratio."
        ],
        "key_points": [
            "Law of Constant Proportions: Elements combine in a fixed, definite mass ratio.",
            "Water (H₂O) always has an H : O mass ratio of 1 : 8.",
            "Ammonia (NH₃) always has an N : H mass ratio of 14 : 3.",
            "Carbon dioxide (CO₂) always has a C : O mass ratio of 3 : 8."
        ],
        "checkpoints": [
            {
                "num": 3,
                "q": "What mass of oxygen gas is required to react completely with 4.0 g of hydrogen gas to form water?",
                "options": ["16.0 g", "24.0 g", "32.0 g", "36.0 g"],
                "ans": 2,
                "exp": "Since hydrogen and oxygen combine in a 1 : 8 ratio by mass, 1.0 g of H requires 8.0 g of O. Therefore, 4.0 g of H requires 4.0 × 8.0 = 32.0 g of oxygen gas."
            },
            {
                "num": 4,
                "q": "When 3.0 g of carbon is burnt in 8.0 g of oxygen, 11.0 g of CO₂ is produced. What mass of CO₂ will be formed when 3.0 g of carbon is burnt in 50.0 g of oxygen?",
                "options": ["11.0 g", "53.0 g", "38.0 g", "44.0 g"],
                "ans": 0,
                "exp": "By the Law of Constant Proportions, 3.0 g of carbon combines strictly with 8.0 g of oxygen to yield 11.0 g of CO₂. The remaining 42.0 g of oxygen will remain unreacted as excess reagent. Only 11.0 g of CO₂ is formed."
            }
        ]
    },
    {
        "id": 3,
        "badge": "Slide 03 • Competency C-1.1, C-7.1",
        "title": "Dalton's Atomic Theory & Its Postulates",
        "subtitle": "The foundational microscopic explanation for the laws of chemical combination",
        "teacher": "While Lavoisier and Proust gave empirical laws of mass, neither could explain *why* nature behaves this way. In 1808, British schoolteacher John Dalton provided the groundbreaking microscopic theory: all matter is composed of indivisible fundamental building blocks called atoms. Let's study Dalton's six postulates.",
        "theory": [
            "<strong>John Dalton (1766–1844)</strong> published <em>'A New System of Chemical Philosophy'</em> (1808), providing the theoretical foundation connecting macroscopic laws to microscopic particles.",
            "<strong>Key Postulates of Dalton's Atomic Theory:</strong>",
            "1. <strong>All matter is made of very tiny particles called atoms</strong>, which participate in chemical reactions.",
            "2. <strong>Atoms are indivisible particles</strong>, which cannot be created or destroyed in a chemical reaction. (Directly explains the <em>Law of Conservation of Mass</em>).",
            "3. <strong>Atoms of a given element are identical in mass and chemical properties.</strong>",
            "4. <strong>Atoms of different elements have different masses and chemical properties.</strong>",
            "5. <strong>Atoms combine in the ratio of small whole numbers to form compounds.</strong> (Directly explains the <em>Law of Constant Proportions</em>).",
            "6. <strong>The relative number and kinds of atoms are constant in a given compound.</strong>",
            "<strong>Historic Daltonian Symbols:</strong> Dalton was the first scientist to use specific graphic symbols for elements (e.g. circle with dot for Hydrogen, circle with cross for Sulphur, solid black circle for Carbon)."
        ],
        "key_points": [
            "Dalton explained Lavoisier's and Proust's laws using indivisible atomic particles.",
            "Postulate 2 (indivisible/indestructible atoms) explains Conservation of Mass.",
            "Postulates 5 & 6 (whole number combinations) explain Constant Proportions.",
            "Though later modified by discoveries of subatomic particles and isotopes, it remains chemistry's bedrock."
        ],
        "checkpoints": [
            {
                "num": 5,
                "q": "Which postulate of Dalton's atomic theory is the direct result of the Law of Conservation of Mass?",
                "options": [
                    "All matter is made of very tiny particles called atoms.",
                    "Atoms are indivisible particles which cannot be created or destroyed in a chemical reaction.",
                    "Atoms of a given element are identical in mass and chemical properties.",
                    "Atoms combine in the ratio of small whole numbers to form compounds."
                ],
                "ans": 1,
                "exp": "Dalton's postulate that 'Atoms are indivisible particles, which cannot be created or destroyed in a chemical reaction' is the direct theoretical microscopic expression of Lavoisier's Law of Conservation of Mass."
            },
            {
                "num": 6,
                "q": "Which postulate of Dalton's atomic theory successfully explains the Law of Definite Proportions?",
                "options": [
                    "Atoms of different elements have different chemical properties.",
                    "Atoms combine in the ratio of small whole numbers, and the relative number and kinds of atoms are constant in a given compound.",
                    "Matter is composed of indivisible particles.",
                    "Atoms of a given element have identical mass."
                ],
                "ans": 1,
                "exp": "Because atoms of specific elements have fixed masses and always combine in fixed small whole-number ratios (like 2 H to 1 O), the proportion by mass in a compound must always remain constant."
            }
        ]
    },
    {
        "id": 4,
        "badge": "Slide 04 • Competency C-1.1, C-1.3",
        "title": "Atoms: Nanoscale Dimensions & IUPAC Chemical Symbols",
        "subtitle": "From nanometres to international IUPAC nomenclature conventions",
        "teacher": "How small is an atom? An atom is unimaginably tiny—so small that millions of atoms stacked together would barely match the thickness of a single sheet of paper! We measure atomic radii in nanometres (1 nm = 10⁻⁹ m). Let's also examine how Berzelius and modern IUPAC established standard symbols and their fascinating Latin roots.",
        "theory": [
            "<strong>Atomic Scale & Nanometres:</strong>",
            "Atomic radius is measured in <strong>nanometres (nm)</strong>: \\(1\\text{ nm} = 10^{-9}\\text{ m} = \\frac{1}{1,000,000,000}\\text{ metre}\\), or \\(1\\text{ m} = 10^9\\text{ nm}\\).",
            "• Radius of a Hydrogen atom \\(\\approx 10^{-10}\\text{ m} = 0.1\\text{ nm}\\).",
            "• Molecule of water \\(\\approx 10^{-9}\\text{ m} = 1\\text{ nm}\\).",
            "• Molecule of haemoglobin \\(\\approx 10^{-8}\\text{ m} = 10\\text{ nm}\\).",
            "• Grain of sand \\(\\approx 10^{-4}\\text{ m} = 100,000\\text{ nm}\\).",
            "<strong>IUPAC (International Union of Pure and Applied Chemistry) Symbol Rules:</strong>",
            "J.J. Berzelius suggested that symbols be derived from one or two letters of the element's name.",
            "1. <strong>Single Letter Symbols:</strong> Always written in UPPERCASE (e.g. Hydrogen = \\(H\\), Oxygen = \\(O\\), Nitrogen = \\(N\\), Carbon = \\(C\\)).",
            "2. <strong>Two Letter Symbols:</strong> First letter is ALWAYS UPPERCASE, and the second letter is ALWAYS LOWERCASE (e.g. Aluminium = \\(Al\\), not AL; Cobalt = \\(Co\\), while CO represents carbon monoxide!).",
            "<strong>Classical Latin Origins of Elemental Symbols:</strong>",
            "• Sodium = \\(\\text{Na}\\) (from Latin <em>Natrium</em>) • Potassium = \\(\\text{K}\\) (from Latin <em>Kalium</em>)",
            "• Iron = \\(\\text{Fe}\\) (from Latin <em>Ferrum</em>) • Copper = \\(\\text{Cu}\\) (from Latin <em>Cuprum</em>)",
            "• Silver = \\(\\text{Ag}\\) (from Latin <em>Argentum</em>) • Gold = \\(\\text{Au}\\) (from Latin <em>Aurum</em>)",
            "• Lead = \\(\\text{Pb}\\) (from Latin <em>Plumbum</em>) • Mercury = \\(\\text{Hg}\\) (from Latin <em>Hydrargyrum</em>)"
        ],
        "key_points": [
            "1 nanometre (nm) = 10⁻⁹ metre. Hydrogen atom radius ≈ 0.1 nm.",
            "IUPAC rules: First letter capital, second letter strictly lower case (e.g. Ca, Cl, Mg, Ne).",
            "Watch out: 'Co' is Cobalt (element), while 'CO' is Carbon Monoxide (compound)!",
            "Latin names explain non-intuitive symbols: Na (Natrium), K (Kalium), Fe (Ferrum), Au (Aurum)."
        ],
        "checkpoints": [
            {
                "num": 7,
                "q": "Which of the following correctly pairs an element with its IUPAC symbol and Latin origin name?",
                "options": [
                    "Potassium — P — Phosphorus",
                    "Sodium — Na — Natrium",
                    "Iron — Ir — Iridium",
                    "Lead — Ld — Litharge"
                ],
                "ans": 1,
                "exp": "Sodium is assigned the IUPAC symbol Na from its Latin root 'Natrium'. Potassium is K (Kalium), Iron is Fe (Ferrum), and Lead is Pb (Plumbum)."
            },
            {
                "num": 8,
                "q": "Why is it chemically incorrect to write the symbol of Calcium as 'CA' or Chlorine as 'CL'?",
                "options": [
                    "Because all elemental symbols must contain exactly 3 letters",
                    "Because IUPAC rules mandate that the first letter must be uppercase and the second strictly lowercase",
                    "Because uppercase combinations are reserved exclusively for organic acids",
                    "Because lowercase letters represent radioactive isotopes"
                ],
                "ans": 1,
                "exp": "IUPAC convention requires the first letter to be capital and the second lowercase (Ca, Cl). Writing two capital letters (like CO) designates a compound of two elements (Carbon and Oxygen), not a single element (Cobalt is Co)."
            }
        ]
    },
    {
        "id": 5,
        "badge": "Slide 05 • Competency C-1.1, C-7.1",
        "title": "Atomic Mass & The Unified Atomic Mass Unit (u)",
        "subtitle": "Defining relative atomic weights using the Carbon-12 standard",
        "teacher": "Because individual atoms have masses on the order of 10⁻²⁴ grams, weighing single atoms directly is impractical. Chemists therefore measure relative atomic masses using a standard reference. Since 1961, the universal international standard is the Carbon-12 isotope. Let's understand how the unified atomic mass unit 'u' works.",
        "theory": [
            "<strong>Relative Atomic Mass Concept:</strong> Dalton initially used Hydrogen (mass = 1) and later Oxygen (1/16th of O-16). In 1961, IUPAC unanimously adopted the <strong>Carbon-12 isotope (\\(^{12}\\text{C}\\))</strong> as the universal reference standard.",
            "<strong>Definition of Unified Atomic Mass Unit (\\(u\\)):</strong>",
            "<em>'One unified atomic mass unit (\\(1\\text{ u}\\)) is a mass unit equal to exactly one-twelfth (\\(\\frac{1}{12}\\text{th}\\)) the mass of one atom of carbon-12.'</em>",
            "$$1\\text{ u} = \\frac{1}{12} \\times \\text{Mass of one } ^{12}\\text{C atom} \\approx 1.66054 \\times 10^{-24}\\text{ g} = 1.66054 \\times 10^{-27}\\text{ kg}$$",
            "<strong>The Famous Watermelon Analogy:</strong>",
            "Imagine a watermelon representing a Carbon-12 atom. Cut the watermelon into 12 equal slices. Each slice represents \\(1\\text{ u}\\). When we say the atomic mass of Magnesium is \\(24\\text{ u}\\), it means one magnesium atom is 24 times heavier than one slice of the carbon-12 watermelon!",
            "<strong>Standard Relative Atomic Masses of Common Elements:</strong>",
            "• Hydrogen (\\(H\\)) = \\(1\\text{ u}\\) • Carbon (\\(C\\)) = \\(12\\text{ u}\\) • Nitrogen (\\(N\\)) = \\(14\\text{ u}\\)",
            "• Oxygen (\\(O\\)) = \\(16\\text{ u}\\) • Sodium (\\(Na\\)) = \\(23\\text{ u}\\) • Magnesium (\\(Mg\\)) = \\(24\\text{ u}\\)",
            "• Sulphur (\\(S\\)) = \\(32\\text{ u}\\) • Chlorine (\\(Cl\\)) = \\(35.5\\text{ u}\\) • Calcium (\\(Ca\\)) = \\(40\\text{ u}\\)"
        ],
        "key_points": [
            "Standard reference: 1/12th the mass of an unbound Carbon-12 atom = 1 u.",
            "1 u = 1.6605 × 10⁻²⁷ kg.",
            "Relative atomic mass is a dimensionless ratio comparing an atom's mass to 1 u.",
            "Common masses to remember: H=1, C=12, N=14, O=16, Na=23, S=32, Cl=35.5, Ca=40."
        ],
        "checkpoints": [
            {
                "num": 9,
                "q": "What is the universally accepted standard for defining relative atomic mass since 1961?",
                "options": [
                    "1/16th of the mass of an oxygen-16 atom",
                    "The mass of one hydrogen-1 atom",
                    "1/12th of the mass of one carbon-12 atom",
                    "1/14th of the mass of one nitrogen-14 atom"
                ],
                "ans": 2,
                "exp": "By IUPAC agreement in 1961, 1 unified atomic mass unit (1 u) is defined strictly as exactly 1/12th the mass of one atom of Carbon-12."
            },
            {
                "num": 10,
                "q": "An atom of element X is 4 times heavier than 1/12th of a carbon-12 atom. What is element X?",
                "options": ["Hydrogen (1 u)", "Helium (4 u)", "Carbon (12 u)", "Beryllium (9 u)"],
                "ans": 1,
                "exp": "Since 1/12th of a C-12 atom equals 1 u, an atom that is 4 times heavier has an atomic mass of 4 u, which is Helium (He, Z=2, A=4 u)."
            }
        ]
    },
    {
        "id": 6,
        "badge": "Slide 06 • Competency C-1.1, C-5.1",
        "title": "Molecules of Elements & Atomicity",
        "subtitle": "Single atoms vs homonuclear polyatomic molecular architectures",
        "teacher": "Atoms of most elements cannot exist independently in nature due to incomplete valence shells. They bond together into molecules! When atoms of the same element combine, they form molecules of elements. The number of atoms present in one molecule of an element is called its atomicity. Let's explore everything from monoatomic argon to octatomic sulphur rings.",
        "theory": [
            "<strong>What is a Molecule?</strong> A molecule is the smallest particle of an element or compound that is capable of an independent existence and shows all the physical and chemical properties of that substance.",
            "<strong>Atomicity:</strong> The number of atoms constituting a molecule is known as its <strong>atomicity</strong>.",
            "<strong>Classification of Elements by Atomicity:</strong>",
            "1. <strong>Monoatomic (Atomicity = 1):</strong> Noble gases have stable valence shells and exist as single isolated atoms (e.g. Helium \\(He\\), Neon \\(Ne\\), Argon \\(Ar\\), Krypton \\(Kr\\)). Metals like \\(Na, Fe, Cu\\) are also traditionally represented as monoatomic.",
            "2. <strong>Diatomic (Atomicity = 2):</strong> Two identical atoms share electrons to form a stable molecule. Examples: Hydrogen (\\(H_2\\)), Nitrogen (\\(N_2\\)), Oxygen (\\(O_2\\)), Fluorine (\\(F_2\\)), Chlorine (\\(Cl_2\\)), Bromine (\\(Br_2\\)), Iodine (\\(I_2\\)).",
            "3. <strong>Triatomic (Atomicity = 3):</strong> Ozone (\\(O_3\\)) consists of 3 bonded oxygen atoms.",
            "4. <strong>Tetra-atomic (Atomicity = 4):</strong> White Phosphorus exists as a \\(P_4\\) molecule where four phosphorus atoms form a three-dimensional tetrahedron.",
            "5. <strong>Poly-atomic (Atomicity > 4):</strong> Rhombic sulphur consists of \\(S_8\\) molecules arranged in a distinctive puckered 'crown' ring structure."
        ],
        "key_points": [
            "Atomicity = Number of atoms inside a single molecule of the element.",
            "Monoatomic: Noble gases (He, Ne, Ar).",
            "Diatomic: H₂, N₂, O₂, Cl₂.",
            "Tetra-atomic: Phosphorus (P₄ tetrahedral structure).",
            "Poly-atomic: Sulphur (S₈ puckered crown ring)."
        ],
        "checkpoints": [
            {
                "num": 11,
                "q": "What is the atomicity of ozone (O₃) and phosphorus (P₄) respectively?",
                "options": [
                    "2 and 4",
                    "3 and 4",
                    "3 and 8",
                    "1 and 4"
                ],
                "ans": 1,
                "exp": "Ozone contains 3 oxygen atoms per molecule (atomicity = 3, triatomic). White phosphorus contains 4 phosphorus atoms per molecule in a tetrahedral cage (atomicity = 4, tetra-atomic)."
            },
            {
                "num": 12,
                "q": "Sulphur molecules exist as puckered crown rings with the formula S₈. What is the atomicity of sulphur?",
                "options": ["2", "4", "6", "8 (Poly-atomic)"],
                "ans": 3,
                "exp": "Because one molecule of elemental sulphur is composed of 8 covalently bonded sulphur atoms arranged in a ring, its atomicity is 8 (poly-atomic)."
            }
        ]
    },
    {
        "id": 7,
        "badge": "Slide 07 • Competency C-1.1, C-5.1, C-7.1",
        "title": "Molecules of Compounds & Covalent Bonding",
        "subtitle": "Mutual electron sharing and Lewis electron dot representations",
        "teacher": "When atoms of different non-metallic elements combine in fixed proportions, they form molecules of compounds. Instead of giving up electrons completely, these non-metals share pairs of electrons to attain stable noble gas octets. This mutual sharing creates strong covalent bonds. Let's draw and examine Lewis electron dot structures for water, methane, and ammonia.",
        "theory": [
            "<strong>Molecules of Compounds:</strong> Formed when atoms of two or more different elements chemically combine in definite proportions by mass (e.g. \\(H_2O, CO_2, NH_3, CH_4\\)).",
            "<strong>Covalent Bonding Principle:</strong> A chemical bond formed by the <strong>mutual sharing of electron pairs</strong> between two non-metal atoms so each atom attains a stable valence shell (duplet for H, octet for others).",
            "<strong>Lewis Electron Dot Structures (C-5.1):</strong>",
            "• <strong>Hydrogen molecule (\\(H_2\\)):</strong> Each H has 1 valence electron. They share 1 pair to form a single covalent bond: \\(H:H\\) or \\(H-H\\).",
            "• <strong>Oxygen molecule (\\(O_2\\)):</strong> Each O has 6 valence electrons and needs 2. They share 2 pairs to form a double bond: \\(O::O\\) or \\(O=O\\).",
            "• <strong>Nitrogen molecule (\\(N_2\\)):</strong> Each N has 5 valence electrons and needs 3. They share 3 pairs to form a strong triple bond: \\(N:::N\\) or \\(N\\equiv N\\).",
            "• <strong>Water (\\(\\text{H}_2\\text{O}\\)):</strong> Central Oxygen (6 valence \\(e^-\\)) shares 1 electron with each of two Hydrogen atoms, leaving 2 non-bonding lone pairs and creating a bent \\(104.5^\\circ\\) molecule.",
            "• <strong>Methane (\\(\\text{CH}_4\\)):</strong> Central Carbon (4 valence \\(e^-\\)) shares electrons with 4 Hydrogen atoms, forming a symmetrical 3D tetrahedron.",
            "<strong>Characteristic Properties of Covalent Molecular Compounds:</strong>",
            "1. Consist of discrete neutral molecules held together by weak intermolecular van der Waals forces.",
            "2. Low melting and boiling points (e.g. ice melts at \\(0^\\circ\\text{C}\\), methane boils at \\(-161.5^\\circ\\text{C}\\)).",
            "3. Poor electrical conductors in all states because they contain no free mobile ions or electrons."
        ],
        "key_points": [
            "Covalent bond: Formed by mutual sharing of valence electron pairs between non-metals.",
            "Single bond (H-H), Double bond (O=O), Triple bond (N≡N).",
            "Lewis dot structures visually map bonding pairs and non-bonding lone pairs.",
            "Covalent compounds have low melting/boiling points and are electrical non-conductors."
        ],
        "checkpoints": [
            {
                "num": 13,
                "q": "How many shared electron pairs (covalent bonds) exist in a molecule of Nitrogen (N₂)?",
                "options": ["1 pair (single bond)", "2 pairs (double bond)", "3 pairs (triple bond)", "4 pairs"],
                "ans": 2,
                "exp": "A nitrogen atom has 5 valence electrons and requires 3 electrons to complete its octet. Two nitrogen atoms mutually share 3 pairs of electrons (total 6 electrons), forming a strong triple covalent bond (N≡N)."
            },
            {
                "num": 14,
                "q": "Why do covalent compounds like methane (CH₄) or sugar exhibit low melting points compared to table salt (NaCl)?",
                "options": [
                    "Covalent bonds inside the molecule are extremely weak",
                    "Intermolecular forces between discrete neutral molecules are weak van der Waals forces",
                    "Covalent compounds contain high concentrations of free mobile ions",
                    "Covalent molecules dissolve spontaneously in air"
                ],
                "ans": 1,
                "exp": "While the intramolecular covalent bonds holding the atoms together are strong, the intermolecular forces between separate neutral molecules are weak. Little thermal energy is required to overcome these intermolecular forces, resulting in low melting points."
            }
        ]
    },
    {
        "id": 8,
        "badge": "Slide 08 • Competency C-1.1",
        "title": "Ions: Cations, Anions, and Polyatomic Radicals",
        "subtitle": "Charged atomic species carrying net positive or negative electrostatic charge",
        "teacher": "Compounds composed of metals and non-metals contain charged species known as ions. An atom that loses electrons becomes a positively charged cation, while an atom that gains electrons becomes a negatively charged anion. Groups of atoms carrying a collective net charge are polyatomic ions. Let's master their symbols, charges, and valencies.",
        "theory": [
            "<strong>What is an Ion?</strong> An ion is an atom or a group of bonded atoms that carries an overall electrical charge due to the loss or gain of electrons.",
            "<strong>Cations (Positively Charged Ions):</strong> Formed when electropositive metal atoms <strong>lose</strong> one or more valence electrons to achieve noble gas stability.",
            "• Monovalent: \\(Na^+, K^+, Ag^+, Cu^+, H^+\\)",
            "• Divalent: \\(Mg^{2+}, Ca^{2+}, Fe^{2+}\\text{ (ferrous)}, Cu^{2+}\\text{ (cupric)}, Zn^{2+}, Ba^{2+}\\)",
            "• Trivalent: \\(Al^{3+}, Fe^{3+}\\text{ (ferric)}\\)",
            "<strong>Anions (Negatively Charged Ions):</strong> Formed when electronegative non-metal atoms <strong>gain</strong> valence electrons.",
            "• Monovalent: Chloride (\\(Cl^-\\)), Bromide (\\(Br^-\\)), Iodide (\\(I^-\\)), Hydride (\\(H^-\\))",
            "• Divalent: Oxide (\\(O^{2-}\\)), Sulphide (\\(S^{2-}\\))",
            "• Trivalent: Nitride (\\(N^{3-}\\)), Phosphide (\\(P^{3-}\\))",
            "<strong>Polyatomic Ions (Compound Radicals):</strong> A stable cluster of covalently bonded atoms carrying a net overall electrical charge:",
            "• Ammonium: \\(\\text{NH}_4^+\\) (charge \\(+1\\))",
            "• Hydroxide: \\(\\text{OH}^-\\) (charge \\(-1\\)) • Nitrate: \\(\\text{NO}_3^-\\) (charge \\(-1\\))",
            "• Hydrogen Carbonate (Bicarbonate): \\(\\text{HCO}_3^-\\) (charge \\(-1\\))",
            "• Carbonate: \\(\\text{CO}_3^{2-}\\) (charge \\(-2\\)) • Sulphate: \\(\\text{SO}_4^{2-}\\) (charge \\(-2\\)) • Sulphite: \\(\\text{SO}_3^{2-}\\) (charge \\(-2\\))",
            "• Phosphate: \\(\\text{PO}_4^{3-}\\) (charge \\(-3\\))"
        ],
        "key_points": [
            "Cation = Positively charged ion formed by electron loss (e.g. Na⁺, Mg²⁺, Al³⁺).",
            "Anion = Negatively charged ion formed by electron gain (e.g. Cl⁻, O²⁻, N³⁻).",
            "Polyatomic ion = Group of atoms acting as a single unit with a net charge (e.g. NH₄⁺, OH⁻, SO₄²⁻).",
            "The charge on the ion represents its combining capacity (valency)."
        ],
        "checkpoints": [
            {
                "num": 15,
                "q": "Which of the following is a polyatomic divalent anion?",
                "options": [
                    "Ammonium (NH₄⁺)",
                    "Chloride (Cl⁻)",
                    "Sulphate (SO₄²⁻)",
                    "Phosphate (PO₄³⁻)"
                ],
                "ans": 2,
                "exp": "Sulphate (SO₄²⁻) consists of 1 sulphur and 4 oxygen atoms acting as a single polyatomic unit with a 2- negative charge (divalent anion). NH₄⁺ is a monovalent cation, Cl⁻ is a monoatomic anion, and PO₄³⁻ is trivalent."
            },
            {
                "num": 16,
                "q": "How does an aluminum atom (Z = 13, configuration 2, 8, 3) become an aluminum ion (Al³⁺)?",
                "options": [
                    "By gaining 3 protons in its nucleus",
                    "By losing its 3 valence electrons to achieve a stable neon octet (2, 8)",
                    "By sharing 3 electrons with another aluminum atom",
                    "By absorbing 3 neutrons"
                ],
                "ans": 1,
                "exp": "Aluminum has 3 valence electrons. It readily loses all 3 electrons, leaving 10 electrons and 13 positive protons, generating a stable Al³⁺ cation with neon-like configuration (2, 8)."
            }
        ]
    },
    {
        "id": 9,
        "badge": "Slide 09 • Competency C-1.1, C-7.1",
        "title": "Ionic Compounds & Their Crystalline Lattice Properties",
        "subtitle": "Electrostatic attraction, continuous networks, and electrical conductivity",
        "teacher": "When metals meet non-metals, electrons transfer completely from electropositive to electronegative atoms. The resulting cations and anions attract each other through powerful omnidirectional electrostatic forces, organizing into infinite 3D crystalline lattices like rock salt. Let's investigate their high melting points and why salt conducts electricity only when dissolved or molten.",
        "theory": [
            "<strong>Ionic Bonding Mechanism:</strong> Consider the formation of Sodium Chloride (\\(\\text{NaCl}\\)):",
            "$$\\text{Na (2, 8, 1)} \\longrightarrow \\text{Na}^+ (2, 8) + e^- \\quad \\text{(Oxidation/Electron loss)}$$",
            "$$\\text{Cl (2, 8, 7)} + e^- \\longrightarrow \\text{Cl}^- (2, 8, 8) \\quad \\text{(Reduction/Electron gain)}$$",
            "$$\\text{Na}^+ + \\text{Cl}^- \\longrightarrow \\text{NaCl (Ionic bond)}$$",
            "<strong>The Giant 3D Crystalline Lattice:</strong> \\(\\text{NaCl}\\) does not exist as isolated single molecules. Instead, each \\(\\text{Na}^+\\) ion is symmetrically surrounded by \\(6\\ \\text{Cl}^-\\) ions, and each \\(\\text{Cl}^-\\) is surrounded by \\(6\\ \\text{Na}^+\\) ions in a rigid face-centered cubic lattice.",
            "<strong>Physical Hallmarks of Ionic Compounds:</strong>",
            "1. <strong>High Melting and Boiling Points:</strong> Enormous thermal energy is required to break the strong omnidirectional electrostatic forces (e.g. \\(\\text{NaCl}\\) melts at \\(801^\\circ\\text{C}\\) and boils at \\(1413^\\circ\\text{C}\\)).",
            "2. <strong>Hardness & Brittleness:</strong> Sharp mechanical impact shifts crystal layers, causing like charges to align and violently repel, shattering the crystal along cleavage planes.",
            "3. <strong>Solubility:</strong> Highly soluble in polar solvents (like water, which hydrates the ions) but insoluble in non-polar organic liquids (petrol, kerosene).",
            "4. <strong>Electrical Conductivity:</strong>",
            "• <em>Solid State:</em> Poor conductor/insulator because ions are locked rigidly in lattice positions and cannot move.",
            "• <em>Molten State or Aqueous Solution:</em> Excellent conductor because electrostatic bonds break, allowing ions to freely migrate toward oppositely charged electrodes."
        ],
        "key_points": [
            "Ionic compounds form via complete electron transfer from metal to non-metal.",
            "Form continuous 3D repeating crystal lattices (no discrete molecules).",
            "High melting/boiling points due to strong electrostatic attraction.",
            "Insulators in solid state; conduct electricity in molten state or aqueous solution due to mobile ions."
        ],
        "checkpoints": [
            {
                "num": 17,
                "q": "Why does solid sodium chloride fail to conduct electricity, whereas aqueous sodium chloride conducts electricity brilliantly?",
                "options": [
                    "Solid NaCl has no electrons",
                    "In solid NaCl, ions are locked in fixed lattice sites; in water, ions dissociate and move freely",
                    "Water creates new metal atoms that conduct electricity",
                    "Solid salt has zero density"
                ],
                "ans": 1,
                "exp": "Conduction of electricity requires mobile charge carriers. In solid NaCl, ions are immobilized by strong electrostatic forces. When dissolved in water, the hydration energy overcomes lattice energy, freeing Na⁺ and Cl⁻ ions to migrate freely."
            },
            {
                "num": 18,
                "q": "Why do ionic crystals shatter when struck with a hammer (exhibiting brittleness)?",
                "options": [
                    "The hammer strike produces intense chemical oxidation",
                    "Displacement forces like-charged ions into direct alignment, causing intense electrostatic repulsion",
                    "Covalent bonds inside the ions snap",
                    "The electrons instantly vaporize"
                ],
                "ans": 1,
                "exp": "A mechanical blow causes planes of ions to slide past one another. This brings ions of like charges (Na⁺ next to Na⁺, Cl⁻ next to Cl⁻) into proximity, producing massive electrostatic repulsion that fractures the crystal."
            }
        ]
    },
    {
        "id": 10,
        "badge": "Slide 10 • Competency C-1.1, C-5.3",
        "title": "Rules for Writing Chemical Formulae: The Criss-Cross Method",
        "subtitle": "Balancing ionic charges and IUPAC subscript conventions",
        "teacher": "A chemical formula is the symbolic shorthand representation of a compound's composition. To write formulas accurately without memorizing thousands of combinations, chemists use the elegant Criss-Cross Method. Let's learn the three cardinal rules: balancing total valency, writing metals first, and correctly using parentheses for polyatomic radicals.",
        "theory": [
            "<strong>What is a Chemical Formula?</strong> The chemical formula of a compound is a symbolic representation of its elemental composition and combining proportions.",
            "<strong>The Three Cardinal Rules for Writing Chemical Formulae:</strong>",
            "1. <strong>Valencies or charges on the ions must balance</strong> to yield a net neutral compound (Net charge = \\(0\\)).",
            "2. <strong>When a compound consists of a metal and a non-metal:</strong> The name or symbol of the metal is always written <em>first</em> on the left (e.g. Calcium oxide \\(\\text{CaO}\\), Sodium chloride \\(\\text{NaCl}\\), Iron sulphide \\(\\text{FeS}\\), Copper oxide \\(\\text{CuO}\\)).",
            "3. <strong>Polyatomic Ions and Parentheses:</strong> When a compound contains two or more identical polyatomic ions, the formula of the polyatomic radical is enclosed within brackets before writing the subscript (e.g. \\(\\text{Ca(OH)}_2\\), \\(\\text{(NH}_4\\text{)}_2\\text{SO}_4\\), \\(\\text{Al}_2\\text{(SO}_4\\text{)}_3\\)). If the subscript is 1, brackets are omitted (e.g. \\(\\text{NaOH}\\), \\(\\text{KNO}_3\\)).",
            "<strong>The Criss-Cross Protocol in 4 Steps:</strong>",
            "• <strong>Step 1:</strong> Write the symbols of constituent elements/ions side by side (cation on left, anion on right).",
            "• <strong>Step 2:</strong> Write their respective valencies or charges directly underneath.",
            "• <strong>Step 3:</strong> Cross over the valencies from top right to bottom left and vice-versa.",
            "• <strong>Step 4:</strong> Simplify the subscript ratio to the lowest whole numbers (e.g. \\(\\text{Mg}_2\\text{O}_2 \\to \\text{MgO}\\); \\(\\text{C}_2\\text{O}_4 \\to \\text{CO}_2\\))."
        ],
        "key_points": [
            "Rule 1: Net electrical charge of the compound must sum to zero.",
            "Rule 2: Metal (cation) is written on the left; non-metal (anion) on the right.",
            "Rule 3: Use parentheses for multiple polyatomic ions: Ca(OH)₂, Al₂(SO₄)₃.",
            "Criss-cross: Cross valencies as subscripts and simplify to lowest whole integers."
        ],
        "checkpoints": [
            {
                "num": 19,
                "q": "Why is the chemical formula of calcium hydroxide written as Ca(OH)₂ rather than CaOH₂?",
                "options": [
                    "CaOH₂ means 1 calcium, 1 oxygen, and 2 hydrogens; Ca(OH)₂ correctly indicates 2 hydroxide (OH) groups",
                    "Parentheses are optional and both notations are identical",
                    "CaOH₂ represents an explosive gas",
                    "The number 2 applies only to the calcium atom"
                ],
                "ans": 0,
                "exp": "Writing CaOH₂ without brackets implies that the subscript 2 belongs only to hydrogen. Since the polyatomic hydroxide ion is (OH)⁻, parentheses are required: Ca(OH)₂ contains 1 Ca²⁺ ion and 2 entire OH⁻ ions."
            },
            {
                "num": 20,
                "q": "What is the correct chemical formula formed between Magnesium (Mg²⁺) and Oxide (O²⁻)?",
                "options": ["Mg₂O₂", "MgO", "Mg₂O", "MgO₂"],
                "ans": 1,
                "exp": "Crossing valencies gives Mg₂O₂. Dividing both subscripts by their common factor 2 yields the simplest whole-number empirical ratio: MgO."
            }
        ]
    },
    {
        "id": 11,
        "badge": "Slide 11 • Competency C-1.1, C-5.3",
        "title": "Formula Mastery: Binary Compounds to Polyatomic Salts",
        "subtitle": "Step-by-step criss-cross derivations and the Valency Builder Game",
        "teacher": "Let's put the criss-cross method into action across a wide range of essential compounds! Whether dealing with simple binary hydrides or complex polyatomic sulphates and carbonates, the rules never fail. Practice each derivation and play our formula puzzle challenge.",
        "theory": [
            "<strong>Master Examples of Chemical Formula Derivations:</strong>",
            "1. <strong>Hydrogen Chloride:</strong> Symbols \\(H\\) and \\(Cl\\). Valencies \\(1\\) and \\(1\\). Criss-cross gives: $$\\mathbf{\\text{HCl}}$$",
            "2. <strong>Hydrogen Sulphide:</strong> Symbols \\(H\\) and \\(S\\). Valencies \\(1\\) and \\(2\\). Criss-cross gives: $$\\mathbf{\\text{H}_2\\text{S}}$$",
            "3. <strong>Carbon Tetrachloride:</strong> Symbols \\(C\\) and \\(Cl\\). Valencies \\(4\\) and \\(1\\). Criss-cross gives: $$\\mathbf{\\text{CCl}_4}$$",
            "4. <strong>Aluminium Oxide:</strong> Symbols \\(Al\\) and \\(O\\). Valencies \\(3\\) and \\(2\\). Criss-cross gives: $$\\mathbf{\\text{Al}_2\\text{O}_3}$$",
            "5. <strong>Sodium Carbonate:</strong> Symbols \\(Na^+\\) and \\(CO_3^{2-}\\). Charges \\(+1\\) and \\(-2\\). Criss-cross gives: $$\\mathbf{\\text{Na}_2\\text{CO}_3}$$",
            "6. <strong>Aluminium Sulphate:</strong> Symbols \\(Al^{3+}\\) and \\(SO_4^{2-}\\). Charges \\(+3\\) and \\(-2\\). Criss-cross gives: $$\\mathbf{\\text{Al}_2(\\text{SO}_4)_3}$$",
            "7. <strong>Ammonium Sulphate:</strong> Symbols \\(NH_4^+\\) and \\(SO_4^{2-}\\). Charges \\(+1\\) and \\(-2\\). Criss-cross gives: $$\\mathbf{(\\text{NH}_4)_2\\text{SO}_4}$$",
            "8. <strong>Calcium Phosphate:</strong> Symbols \\(Ca^{2+}\\) and \\(PO_4^{3-}\\). Charges \\(+2\\) and \\(-3\\). Criss-cross gives: $$\\mathbf{\\text{Ca}_3(\\text{PO}_4)_2}$$"
        ],
        "key_points": [
            "Aluminium Oxide: Al³⁺ and O²⁻ criss-cross to Al₂O₃.",
            "Sodium Carbonate: Na⁺ and CO₃²⁻ criss-cross to Na₂CO₃.",
            "Aluminium Sulphate: Al³⁺ and SO₄²⁻ criss-cross to Al₂(SO₄)₃.",
            "Calcium Phosphate: Ca²⁺ and PO₄³⁻ criss-cross to Ca₃(PO₄)₂."
        ],
        "checkpoints": [
            {
                "num": 21,
                "q": "What is the correct chemical formula for Ammonium Phosphate?",
                "options": [
                    "NH₄PO₄",
                    "(NH₄)₃PO₄",
                    "(NH₄)₂PO₄",
                    "NH₄(PO₄)₃"
                ],
                "ans": 1,
                "exp": "Ammonium is NH₄⁺ (valency 1) and Phosphate is PO₄³⁻ (valency 3). Criss-crossing valencies places 3 on the ammonium radical: (NH₄)₃PO₄."
            },
            {
                "num": 22,
                "q": "An element M forms an oxide with formula M₂O₃. What will be the formula of its chloride?",
                "options": ["MCl", "MCl₂", "MCl₃", "M₂Cl₃"],
                "ans": 2,
                "exp": "In M₂O₃, since Oxygen has a valency of 2, element M must have a valency of 3 (M³⁺). Chlorine has a valency of 1 (Cl⁻). Criss-crossing M³⁺ and Cl⁻ produces MCl₃."
            }
        ]
    },
    {
        "id": 12,
        "badge": "Slide 12 • Competency C-1.1",
        "title": "Molecular Mass Calculations",
        "subtitle": "Summing atomic masses for covalent molecules",
        "teacher": "Just as an individual atom has an atomic mass, a molecule has a molecular mass. The molecular mass of a substance is simply the algebraic sum of the atomic masses of all the constituent atoms present in one molecule. Let's master the calculation protocol for everything from simple water to nitric acid and glucose.",
        "theory": [
            "<strong>Definition of Molecular Mass:</strong> The <strong>molecular mass</strong> of a substance is the sum of the atomic masses of all the atoms in a molecule of the substance. It is expressed in unified atomic mass units (\\(u\\)).",
            "<strong>Step-by-Step Worked Calculations:</strong>",
            "• <strong>Water (\\(\\text{H}_2\\text{O}\\)):</strong>",
            "$$\\text{Mass} = (2 \\times \\text{Mass of H}) + (1 \\times \\text{Mass of O}) = (2 \\times 1) + (1 \\times 16) = 2 + 16 = \\mathbf{18\\text{ u}}$$",
            "• <strong>Carbon Dioxide (\\(\\text{CO}_2\\)):</strong>",
            "$$\\text{Mass} = (1 \\times 12) + (2 \\times 16) = 12 + 32 = \\mathbf{44\\text{ u}}$$",
            "• <strong>Nitric Acid (\\(\\text{HNO}_3\\)):</strong>",
            "$$\\text{Mass} = (1 \\times 1) + (1 \\times 14) + (3 \\times 16) = 1 + 14 + 48 = \\mathbf{63\\text{ u}}$$",
            "• <strong>Methane (\\(\\text{CH}_4\\)):</strong>",
            "$$\\text{Mass} = (1 \\times 12) + (4 \\times 1) = 12 + 4 = \\mathbf{16\\text{ u}}$$",
            "• <strong>Ethyl Alcohol / Ethanol (\\(\\text{C}_2\\text{H}_5\\text{OH}\\)):</strong>",
            "$$\\text{Mass} = (2 \\times 12) + (6 \\times 1) + (1 \\times 16) = 24 + 6 + 16 = \\mathbf{46\\text{ u}}$$",
            "• <strong>Glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\)):</strong>",
            "$$\\text{Mass} = (6 \\times 12) + (12 \\times 1) + (6 \\times 16) = 72 + 12 + 96 = \\mathbf{180\\text{ u}}$$"
        ],
        "key_points": [
            "Molecular mass = Sum of atomic masses of all atoms in one molecule.",
            "Water (H₂O) = 18 u; Carbon dioxide (CO₂) = 44 u.",
            "Nitric acid (HNO₃) = 1 + 14 + 48 = 63 u.",
            "Glucose (C₆H₁₂O₆) = 72 + 12 + 96 = 180 u."
        ],
        "checkpoints": [
            {
                "num": 23,
                "q": "What is the molecular mass of Sulphuric Acid (H₂SO₄)? (Given: H = 1 u, S = 32 u, O = 16 u)",
                "options": ["49 u", "96 u", "98 u", "102 u"],
                "ans": 2,
                "exp": "Mass of H₂SO₄ = (2 × 1) + (1 × 32) + (4 × 16) = 2 + 32 + 64 = 98 u."
            },
            {
                "num": 24,
                "q": "What is the molecular mass of chloroform (CHCl₃)? (Given: C = 12 u, H = 1 u, Cl = 35.5 u)",
                "options": ["84.5 u", "119.5 u", "118.0 u", "120.5 u"],
                "ans": 1,
                "exp": "Mass of CHCl₃ = (1 × 12) + (1 × 1) + (3 × 35.5) = 12 + 1 + 106.5 = 119.5 u."
            }
        ]
    },
    {
        "id": 13,
        "badge": "Slide 13 • Competency C-1.1",
        "title": "Formula Unit Mass for Ionic Species",
        "subtitle": "Why ionic crystals use formula units rather than molecular masses",
        "teacher": "Why do textbooks distinguish between 'molecular mass' and 'formula unit mass'? Because ionic substances like sodium chloride or calcium chloride do not exist as isolated single molecules! They form continuous 3D networks. For such ionic crystals, we calculate the Formula Unit Mass—the sum of atomic masses of the atoms in one empirical formula unit.",
        "theory": [
            "<strong>Distinction Between Molecular Mass and Formula Unit Mass:</strong>",
            "• <strong>Molecular Mass</strong> is strictly reserved for substances that exist as <em>discrete independent molecules</em> (e.g. \\(H_2O, CO_2, CH_4\\)).",
            "• <strong>Formula Unit Mass</strong> is used for compounds whose constituent particles are <em>ions organized in giant continuous crystalline lattices</em> (e.g. \\(NaCl, CaCl_2, CuSO_4\\)).",
            "The calculation method is identical: sum the atomic masses of all atoms in one formula unit.",
            "<strong>Step-by-Step Worked Calculations:</strong>",
            "• <strong>Sodium Chloride (\\(\\text{NaCl}\\)):</strong>",
            "$$\\text{Mass} = (1 \\times 23) + (1 \\times 35.5) = \\mathbf{58.5\\text{ u}}$$",
            "• <strong>Calcium Chloride (\\(\\text{CaCl}_2\\)):</strong>",
            "$$\\text{Mass} = (1 \\times 40) + (2 \\times 35.5) = 40 + 71 = \\mathbf{111\\text{ u}}$$",
            "• <strong>Zinc Oxide (\\(\\text{ZnO}\\)):</strong>",
            "$$\\text{Mass} = (1 \\times 65) + (1 \\times 16) = \\mathbf{81\\text{ u}}$$",
            "• <strong>Sodium Carbonate Decahydrate / Washing Soda (\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)):</strong>",
            "$$\\text{Mass of } \\text{Na}_2\\text{CO}_3 = (2 \\times 23) + 12 + (3 \\times 16) = 46 + 12 + 48 = 106\\text{ u}$$",
            "$$\\text{Mass of } 10\\text{H}_2\\text{O} = 10 \\times 18 = 180\\text{ u}$$",
            "$$\\text{Total Formula Unit Mass} = 106 + 180 = \\mathbf{286\\text{ u}}$$"
        ],
        "key_points": [
            "Formula unit mass applies to ionic network solids having no discrete molecules.",
            "Calculation follows identical additive rules in unified atomic mass units (u).",
            "NaCl = 23 + 35.5 = 58.5 u.",
            "CaCl₂ = 40 + 71 = 111 u.",
            "Water of crystallisation must be included: Na₂CO₃·10H₂O = 106 + 180 = 286 u."
        ],
        "checkpoints": [
            {
                "num": 25,
                "q": "Why is the term 'formula unit mass' used for sodium chloride instead of 'molecular mass'?",
                "options": [
                    "Because sodium chloride is a liquid at room temperature",
                    "Because sodium chloride forms an infinite 3D ionic lattice without discrete independent NaCl molecules",
                    "Because chlorine is a radioactive gas",
                    "Because sodium chloride has zero mass"
                ],
                "ans": 1,
                "exp": "In sodium chloride crystals, every Na⁺ is coordinated by 6 Cl⁻ ions in an extended repeating lattice. Since there are no discrete, isolated 'NaCl' molecules, the term 'formula unit mass' is used for its empirical formula unit."
            },
            {
                "num": 26,
                "q": "What is the formula unit mass of potassium carbonate (K₂CO₃)? (Given: K = 39 u, C = 12 u, O = 16 u)",
                "options": ["106 u", "138 u", "126 u", "142 u"],
                "ans": 1,
                "exp": "Formula Unit Mass of K₂CO₃ = (2 × 39) + (1 × 12) + (3 × 16) = 78 + 12 + 48 = 138 u."
            }
        ]
    },
    {
        "id": 14,
        "badge": "Slide 14 • Competency C-8.1, C-5.1",
        "title": "Model Building & Molecular Architecture",
        "subtitle": "Ball-and-stick geometries and spatial symmetry of chemical compounds",
        "teacher": "Molecules are not flat drawings on paper—they are dynamic 3-dimensional architectural masterpieces! By using standardized CPK color conventions and ball-and-stick or space-filling models, scientists visualize molecular geometry, bond angles, and steric interactions. Let's explore linear, bent, pyramidal, and tetrahedral molecular geometries.",
        "theory": [
            "<strong>Standard CPK Color Conventions for Molecular Modeling (C-8.1):</strong>",
            "• <strong>Hydrogen (H):</strong> White",
            "• <strong>Carbon (C):</strong> Grey / Black",
            "• <strong>Oxygen (O):</strong> Red",
            "• <strong>Nitrogen (N):</strong> Blue",
            "• <strong>Chlorine (Cl):</strong> Green",
            "• <strong>Sulphur (S):</strong> Yellow",
            "<strong>Fundamental 3D Molecular Geometries:</strong>",
            "1. <strong>Linear Geometry (\\(180^\\circ\\)):</strong> Carbon Dioxide (\\(\\text{CO}_2\\)). The two double bonds (\\(O=C=O\\)) repel each other symmetrically, producing a straight line.",
            "2. <strong>Bent / V-Shaped Geometry (\\(104.5^\\circ\\)):</strong> Water (\\(\\text{H}_2\\text{O}\\)). The central oxygen atom has two bonded hydrogen atoms and two non-bonding lone pairs. The strong repulsion from the lone pairs squeezes the \\(H-O-H\\) bond angle down to \\(104.5^\\circ\\).",
            "3. <strong>Trigonal Pyramidal (\\(107.8^\\circ\\)):</strong> Ammonia (\\(\\text{NH}_3\\)). One lone pair at the apex pushes the three \\(N-H\\) bonds down into a tripod pyramid.",
            "4. <strong>Tetrahedral Geometry (\\(109.5^\\circ\\)):</strong> Methane (\\(\\text{CH}_4\\)). Carbon's 4 identical single covalent bonds point toward the corners of a regular tetrahedron, maximizing mutual angular separation.",
            "<strong>Collaborative Modeling:</strong> Constructing physical models using plastic spheres or clay and toothpicks reinforces concepts of valency, steric hindrance, and molecular symmetry."
        ],
        "key_points": [
            "CPK color standard: H = White, C = Black/Grey, O = Red, N = Blue, Cl = Green.",
            "CO₂ is linear (180°); H₂O is bent (104.5°) due to oxygen's 2 lone pairs.",
            "NH₃ is trigonal pyramidal (107.8°); CH₄ is regular tetrahedral (109.5°).",
            "3D spatial orientation governs molecular stability and biological interactions."
        ],
        "checkpoints": [
            {
                "num": 27,
                "q": "Why is a water molecule (H₂O) bent with an angle of 104.5° instead of being linear like carbon dioxide (CO₂)?",
                "options": [
                    "Because hydrogen atoms are magnetic",
                    "Because the central oxygen atom has two non-bonding electron lone pairs that exert repulsive force",
                    "Because water contains ionic bonds",
                    "Because oxygen has a higher atomic number than carbon"
                ],
                "ans": 1,
                "exp": "The central oxygen atom in H₂O possesses two bonding pairs and two non-bonding lone pairs. Lone pair-lone pair and lone pair-bond pair repulsions push the two O-H bonds closer, producing a bent V-shape (104.5°)."
            },
            {
                "num": 28,
                "q": "What is the 3D molecular geometry and bond angle of methane (CH₄)?",
                "options": [
                    "Planar square, 90°",
                    "Linear, 180°",
                    "Regular tetrahedral, 109.5°",
                    "Trigonal planar, 120°"
                ],
                "ans": 2,
                "exp": "In methane (CH₄), the 4 C-H bonding electron pairs experience equal mutual repulsion in 3D space, orienting themselves toward the vertices of a regular tetrahedron with bond angles of 109.5°."
            }
        ]
    },
    {
        "id": 15,
        "badge": "Slide 15 • Competency C-5.2, C-6.1",
        "title": "Indian Heritage, Cinnabar & Peaceful Atomic Science",
        "subtitle": "Ancient Rasashastra metallurgy to modern peaceful applications of atomic science",
        "teacher": "India has a rich tradition in molecular and chemical sciences! Centuries before modern chemistry, Indian alchemical texts like the Rasashastra recorded the extraction of elemental mercury from the red rock mineral cinnabar (Hingula). In modern times, Indian scientists have spearheaded the peaceful application of atomic energy in medicine and agriculture. Let's also explore the beautiful metaphor connecting atomic bonding to human social harmony.",
        "theory": [
            "<strong>Ancient Indian Metallurgy: Cinnabar & Rasashastra (C-6.1):</strong>",
            "• <strong>Cinnabar (Mercuric Sulphide, \\(\\text{HgS}\\))</strong>, known in Sanskrit as <em>'Hingula'</em>, is a natural red rock mineral used traditionally across India for centuries as the sacred vermilion red pigment (<em>Sindoor</em>).",
            "• The pioneering Indian alchemist-philosopher <strong>Nagarjuna (~8th–9th century CE)</strong> in treatises like <em>Rasaratnakara</em> described the thermal distillation and extraction of pure elemental mercury from cinnabar using a specialized dual-chamber apparatus called the <em>Urdhva-patana Yantra</em> (upward sublimation):",
            "$$\\text{HgS}(s) + \\text{O}_2(g) \\xrightarrow{\\Delta} \\text{Hg}(g)\\uparrow + \\text{SO}_2(g)$$",
            "The mercury vapor condensed on the cold upper inverted pot, demonstrating ancient mastery of thermal decomposition and gas condensation.",
            "<strong>Peaceful Applications of Atomic Science in Modern India (C-5.2):</strong>",
            "• <strong>Nuclear Medicine & Diagnostics:</strong> Radio-pharmaceuticals synthesized at the Bhabha Atomic Research Centre (BARC) like Technetium-99m for organ scans, Cobalt-60 for teletherapy cancer eradication, and Iodine-131 for thyroid therapies.",
            "• <strong>Agricultural Mutation Breeding:</strong> BARC scientists developed over 60 mutant crop varieties (including Trombay groundnut, high-yield pulses, and disease-resistant mustard), greatly boosting India's food security.",
            "• <strong>Food Preservation:</strong> Gamma irradiation facilities preserve spices, potatoes, and onions, preventing post-harvest spoilage without chemical additives.",
            "<strong>Metaphor: Atomic Bonding as Social Bonding (C-5.2):</strong>",
            "• <em>Covalent Bonding (Sharing):</em> Like two non-metals sharing electrons for mutual stability, human communities thrive when members share resources, knowledge, and mutual support.",
            "• <em>Ionic Bonding (Complementarity):</em> Electropositive donors and electronegative acceptors complement each other, forming strong, resilient social fabrics where diverse talents fit harmoniously together."
        ],
        "key_points": [
            "Cinnabar (HgS, Hingula) is the traditional natural red pigment used as Sindoor.",
            "Ancient Indian Rasashastra mastered thermal extraction of pure mercury from cinnabar.",
            "Indian peaceful atomic science: BARC medical radioisotopes and mutant agricultural crops.",
            "Social analogy: Covalent bonding = sharing; Ionic bonding = complementary support."
        ],
        "checkpoints": [
            {
                "num": 29,
                "q": "What is the chemical identity and formula of the traditional Indian red mineral pigment 'cinnabar' (Hingula)?",
                "options": [
                    "Lead Oxide (Pb₃O₄)",
                    "Mercuric Sulphide (HgS)",
                    "Ferric Oxide (Fe₂O₃)",
                    "Cuprous Oxide (Cu₂O)"
                ],
                "ans": 1,
                "exp": "Cinnabar is naturally occurring Mercuric Sulphide (HgS), famous in ancient Indian Rasashastra for its deep vermilion red color and as the principal ore for extracting elemental mercury."
            },
            {
                "num": 30,
                "q": "How does the Bhabha Atomic Research Centre (BARC) utilize atomic science for peaceful agricultural enhancement in India?",
                "options": [
                    "By replacing all natural soil with synthetic polymers",
                    "By developing high-yielding, disease-resistant mutant crop varieties through gamma radiation-induced mutations",
                    "By heating rivers to accelerate fish growth",
                    "By converting agricultural weeds into radioactive uranium"
                ],
                "ans": 1,
                "exp": "BARC has successfully developed dozens of certified high-yielding mutant crop varieties (groundnuts, black gram, mung bean) through peaceful radiation-induced genetic mutation breeding, significantly boosting agricultural productivity."
            }
        ]
    },
    {
        "id": 16,
        "badge": "Slide 16 • Competency C-7.2, C-8.2",
        "title": "Scientific Frontiers: Are There Reactions That Defy Mass Conservation?",
        "subtitle": "Einstein's mass-energy equivalence and the boundaries of classical chemical laws",
        "teacher": "Let us pose an audacious scientific inquiry: Are there any reactions that do NOT strictly obey Lavoisier's Law of Conservation of Mass? In everyday benchtop chemistry, Lavoisier's law appears absolute. However, Albert Einstein revealed that mass and energy are interconvertible via E = mc²! Let's explore the revolutionary boundary between chemical mass conservation and relativistic nuclear mass defects.",
        "theory": [
            "<strong>The Provocative Scientific Question (C-7.2):</strong>",
            "<em>'Are there any chemical or physical transformations that do not obey the classical Law of Conservation of Mass?'</em>",
            "<strong>Einstein's Mass-Energy Equivalence:</strong>",
            "In 1905, Albert Einstein formulated the universal equation:",
            "$$E = \\Delta m \\cdot c^2 \\quad \\implies \\quad \\Delta m = \\frac{\\Delta E}{c^2}$$",
            "where \\(c = 3 \\times 10^8\\text{ m/s}\\) is the speed of light. This means whenever energy is released (\\(\\Delta E < 0\\)), there MUST be a corresponding loss of mass (\\(\\Delta m\\))!",
            "<strong>Why Chemical Reactions Appear to Conserve Mass Perfectly:</strong>",
            "Consider burning \\(1\\text{ mole}\\) of methane gas (\\(\\text{CH}_4\\)), releasing \\(890\\text{ kJ}\\) of exothermic heat:",
            "$$\\Delta m = \\frac{890 \\times 10^3\\text{ J}}{(3 \\times 10^8\\text{ m/s})^2} = \\frac{8.9 \\times 10^5}{9 \\times 10^{16}} \\approx 9.9 \\times 10^{-12}\\text{ kg} = 9.9 \\times 10^{-9}\\text{ g} = 0.00000001\\text{ mg}!$$",
            "This mass defect (less than one-billionth of a gram) is far beyond the detection threshold of even the most sophisticated laboratory analytical balances (which detect down to \\(10^{-5}\\text{ g}\\)). Thus, for all practical chemical laboratory purposes, Lavoisier's Law of Conservation of Mass holds with magnificent precision!",
            "<strong>Where Conservation of Mass Breaks Down: Nuclear Reactions:</strong>",
            "In nuclear fission (such as \\(^{235}\\text{U}\\)) or nuclear fusion in the Sun (\\(4\\ ^1\\text{H} \\to\\ ^4\\text{He}\\)), mass defects are millions of times larger (about \\(0.1\\%\\) to \\(0.7\\%\\) of initial mass), releasing tremendous energy. Here, classical mass alone is not conserved; instead, the unified <strong>Law of Conservation of Mass-Energy</strong> governs the universe."
        ],
        "key_points": [
            "Einstein's equation E = Δm·c² links energy release to mass change.",
            "In chemical reactions, mass defects are ≈ 10⁻¹² kg, undetectable by balances.",
            "Therefore, Lavoisier's Law of Conservation of Mass is extraordinarily accurate in all chemistry.",
            "In nuclear reactions, measurable mass converts to energy, governed by Mass-Energy Conservation."
        ],
        "checkpoints": [
            {
                "num": 31,
                "q": "Why is the mass change resulting from heat release in an exothermic chemical reaction impossible to observe on a standard laboratory balance?",
                "options": [
                    "Because chemical reactions involve zero energy exchange",
                    "Because dividing chemical energy (in Joules) by c² (9 × 10¹⁶ m²/s²) produces an infinitesimally tiny mass defect (~10⁻⁹ g)",
                    "Because laboratory balances automatically recalibrate during reactions",
                    "Because heat has negative mass that cancels out"
                ],
                "ans": 1,
                "exp": "Because c² = 9 × 10¹⁶ m²/s² is an enormous number, Δm = ΔE / c² yields a mass difference on the order of 10⁻⁹ g to 10⁻¹² kg, which is far below the sensitivity limit of chemical laboratory balances."
            },
            {
                "num": 32,
                "q": "What unified universal law replaces the separate conservation of mass and conservation of energy in high-energy nuclear physics?",
                "options": [
                    "The Law of Constant Proportions",
                    "The Law of Conservation of Mass-Energy",
                    "Dalton's Fourth Postulate",
                    "The Law of Multiple Proportions"
                ],
                "ans": 1,
                "exp": "In high-energy nuclear processes where mass is directly converted into energy, the separate classical conservation laws merge into the unified Law of Conservation of Mass-Energy."
            }
        ]
    },
    # Slides 17-20: Dedicated Mastery Quiz Challenge (40 Questions)
    {
        "id": 17,
        "badge": "Slide 17 • Dedicated Quiz Challenge (Part 1/4)",
        "title": "Mastery Quiz: Laws of Chemical Combination & Dalton's Theory",
        "subtitle": "Test your grasp on mass conservation, constant proportions, and atomic postulates",
        "teacher": "Welcome to Part 1 of our Atoms and Molecules Mastery Quiz Challenge! Here are 10 rigorous questions testing your conceptual and computational understanding of the laws of chemical combination. Solve each question and click 'View Solution' for detailed step-by-step teacher explanations.",
        "quiz": [
            {
                "id": "q1",
                "q": "1. Who is recognized as the Father of Modern Chemistry for establishing the Law of Conservation of Mass?",
                "options": ["John Dalton", "Antoine Lavoisier", "Joseph Proust", "J.J. Berzelius"],
                "ans": 1,
                "sol": "Antoine Lavoisier established the Law of Conservation of Mass in 1774 through rigorous quantitative experiments, earning him the title of the Father of Modern Chemistry."
            },
            {
                "id": "q2",
                "q": "2. When 100 g of calcium carbonate is completely decomposed by heat in a sealed tube, 56 g of solid residue (CaO) is obtained. What is the volume of CO₂ gas produced if its density is 1.96 g/L?",
                "options": ["11.2 L", "22.45 L", "44.0 L", "10.0 L"],
                "ans": 1,
                "sol": "Mass of CO₂ = Mass of CaCO₃ - Mass of CaO = 100 g - 56 g = 44 g. Volume = Mass / Density = 44 g / 1.96 g/L ≈ 22.45 L."
            },
            {
                "id": "q3",
                "q": "3. In water (H₂O), the ratio of the mass of hydrogen to the mass of oxygen is always strictly:",
                "options": ["1 : 2", "1 : 8", "1 : 16", "2 : 1"],
                "ans": 1,
                "sol": "Water contains 2 hydrogen atoms (mass = 2 u) and 1 oxygen atom (mass = 16 u). The mass ratio is 2 : 16 = 1 : 8."
            },
            {
                "id": "q4",
                "q": "4. If 12 g of carbon is burnt in 32 g of oxygen, 44 g of CO₂ is produced. What mass of CO₂ is formed if 12 g of carbon is heated in 40 g of oxygen?",
                "options": ["52 g", "44 g", "32 g", "40 g"],
                "ans": 1,
                "sol": "By the Law of Constant Proportions, 12 g of carbon requires exactly 32 g of oxygen to yield 44 g of CO₂. The extra 8 g of oxygen remains unreacted. Only 44 g of CO₂ is formed."
            },
            {
                "id": "q5",
                "q": "5. Which postulate of Dalton's atomic theory provides the microscopic basis for the Law of Conservation of Mass?",
                "options": [
                    "All matter is made of tiny particles called atoms.",
                    "Atoms of an element are identical in mass and properties.",
                    "Atoms are indivisible particles that cannot be created or destroyed in a chemical reaction.",
                    "Atoms combine in small whole-number ratios."
                ],
                "ans": 2,
                "sol": "Postulate 2 states that atoms cannot be created or destroyed during chemical reactions, explaining why total mass remains unchanged before and after the reaction."
            },
            {
                "id": "q6",
                "q": "6. In ammonia (NH₃), the mass ratio of nitrogen to hydrogen is:",
                "options": ["14 : 1", "7 : 3", "14 : 3", "3 : 14"],
                "ans": 2,
                "sol": "Nitrogen has atomic mass 14 u and 3 Hydrogens have mass 3 × 1 = 3 u. Thus, the mass ratio of N : H is 14 : 3."
            },
            {
                "id": "q7",
                "q": "7. A student mixes 20.8 g of BaCl₂ with 14.2 g of Na₂SO₄ in an aqueous solution. What is the total mass of BaSO₄ precipitate and NaCl formed in the reaction?",
                "options": ["20.8 g", "14.2 g", "35.0 g", "42.5 g"],
                "ans": 2,
                "sol": "By Conservation of Mass, Total Mass of Products = Total Mass of Reactants = 20.8 g + 14.2 g = 35.0 g."
            },
            {
                "id": "q8",
                "q": "8. Which French scientist formulated the Law of Constant / Definite Proportions in 1799?",
                "options": ["Joseph Proust", "Antoine Lavoisier", "Louis Pasteur", "Jacques Charles"],
                "ans": 0,
                "sol": "Joseph Louis Proust formulated the Law of Constant Proportions in 1799."
            },
            {
                "id": "q9",
                "q": "9. A sample of pure calcium oxide (CaO) contains 40 g of calcium and 16 g of oxygen. What is the percentage of calcium by mass in CaO?",
                "options": ["40%", "71.43%", "50%", "28.57%"],
                "ans": 1,
                "sol": "Total mass of CaO = 40 + 16 = 56 g. Percentage of Ca = (40 / 56) × 100% ≈ 71.43%."
            },
            {
                "id": "q10",
                "q": "10. Dalton's theory was later modified because:",
                "options": [
                    "Atoms were found to be divisible into electrons, protons, and neutrons",
                    "Isotopes proved atoms of the same element can have different masses",
                    "Both A and B are true",
                    "Atoms cannot participate in chemical reactions"
                ],
                "ans": 2,
                "sol": "Dalton's postulates of indivisible atoms and identical atomic masses for a given element were modified by the discovery of subatomic particles and isotopes."
            }
        ]
    },
    {
        "id": 18,
        "badge": "Slide 18 • Dedicated Quiz Challenge (Part 2/4)",
        "title": "Mastery Quiz: Atomic Scale, IUPAC Symbols & Radicals",
        "subtitle": "Test your mastery on nanometres, Latin roots, valency, and polyatomic ions",
        "teacher": "Part 2 tests your command of IUPAC chemical symbols, unit conversions, atomic scale, and radical charges. Let's see how many of these 10 questions you can solve correctly!",
        "quiz": [
            {
                "id": "q11",
                "q": "11. How many nanometres (nm) are there in 1 metre?",
                "options": ["10⁶ nm", "10⁸ nm", "10⁹ nm", "10¹² nm"],
                "ans": 2,
                "sol": "1 metre = 10⁹ nanometres (1 nm = 10⁻⁹ m)."
            },
            {
                "id": "q12",
                "q": "12. What is the approximate radius of a hydrogen atom?",
                "options": ["10⁻⁶ m", "10⁻⁸ m", "10⁻¹⁰ m (0.1 nm)", "10⁻¹² m"],
                "ans": 2,
                "sol": "The atomic radius of a hydrogen atom is approximately 10⁻¹⁰ m, which equals 0.1 nm."
            },
            {
                "id": "q13",
                "q": "13. What is the IUPAC symbol for the element Potassium, and what is its Latin origin?",
                "options": ["P — Phosphorus", "Pt — Platinum", "K — Kalium", "Po — Polonium"],
                "ans": 2,
                "sol": "Potassium's symbol is K, derived from its Neo-Latin name Kalium."
            },
            {
                "id": "q14",
                "q": "14. Which element's symbol is derived from the Latin word 'Plumbum'?",
                "options": ["Platinum", "Phosphorus", "Lead (Pb)", "Palladium"],
                "ans": 2,
                "sol": "Lead has the chemical symbol Pb from its Latin name Plumbum."
            },
            {
                "id": "q15",
                "q": "15. What is the unified atomic mass unit (u) equivalent to in grams?",
                "options": ["1.00 × 10⁻²⁴ g", "1.66 × 10⁻²⁴ g", "6.022 × 10²³ g", "9.11 × 10⁻²⁸ g"],
                "ans": 1,
                "sol": "1 unified atomic mass unit (1 u) = 1/12th mass of C-12 ≈ 1.66054 × 10⁻²⁴ g (or 1.66054 × 10⁻²⁷ kg)."
            },
            {
                "id": "q16",
                "q": "16. Which of the following elements has an atomicity of 4?",
                "options": ["Helium", "Nitrogen", "Phosphorus (P₄)", "Sulphur (S₈)"],
                "ans": 2,
                "sol": "White phosphorus exists as P₄ tetrahedral molecules, so its atomicity is 4 (tetra-atomic)."
            },
            {
                "id": "q17",
                "q": "17. What is the chemical formula and net electrical charge of the Phosphate radical?",
                "options": ["PO₃²⁻", "PO₄³⁻ (Charge = -3)", "PO₄²⁻", "P³⁻"],
                "ans": 1,
                "sol": "The phosphate ion is a polyatomic anion with formula PO₄³⁻ and net charge -3 (trivalent)."
            },
            {
                "id": "q18",
                "q": "18. What is the formula and charge of the Ammonium ion?",
                "options": ["NH₃ (neutral)", "NH₄⁺ (Charge = +1)", "NH₂⁻", "NH₄²⁺"],
                "ans": 1,
                "sol": "Ammonium is a polyatomic cation with formula NH₄⁺ and charge +1."
            },
            {
                "id": "q19",
                "q": "19. An ion of iron in the 'ferric' state carries a charge of:",
                "options": ["+1", "+2", "+3 (Fe³⁺)", "+4"],
                "ans": 2,
                "sol": "Iron exhibits variable valency: Ferrous is Fe²⁺ (+2) and Ferric is Fe³⁺ (+3)."
            },
            {
                "id": "q20",
                "q": "20. Which of the following is a monoatomic noble gas?",
                "options": ["Oxygen", "Argon (Ar)", "Chlorine", "Hydrogen"],
                "ans": 1,
                "sol": "Argon has a complete valence octet (2, 8, 8) and exists as single independent atoms (atomicity = 1)."
            }
        ]
    },
    {
        "id": 19,
        "badge": "Slide 19 • Dedicated Quiz Challenge (Part 3/4)",
        "title": "Mastery Quiz: Chemical Formulae & The Criss-Cross Method",
        "subtitle": "Test your skill in writing accurate formulas for binary and polyatomic compounds",
        "teacher": "Part 3 is the ultimate test of chemical formula construction. Apply the criss-cross method, cancel common factors, and use brackets properly. Click 'View Solution' for complete step-by-step guidance.",
        "quiz": [
            {
                "id": "q21",
                "q": "21. What is the chemical formula of Aluminium Oxide?",
                "options": ["AlO", "AlO₂", "Al₂O₃", "Al₃O₂"],
                "ans": 2,
                "sol": "Aluminium ion has charge +3 (Al³⁺) and Oxide has charge -2 (O²⁻). Crossing charges yields Al₂O₃."
            },
            {
                "id": "q22",
                "q": "22. What is the chemical formula of Magnesium Hydroxide?",
                "options": ["MgOH", "MgOH₂", "Mg(OH)₂", "Mg₂(OH)"],
                "ans": 2,
                "sol": "Magnesium has valency 2 (Mg²⁺) and Hydroxide has valency 1 (OH⁻). Crossing valencies gives Mg(OH)₂."
            },
            {
                "id": "q23",
                "q": "23. What is the formula of Calcium Carbonate?",
                "options": ["Ca₂(CO₃)₂", "CaCO₃", "Ca(CO₃)₂", "Ca₃(CO₃)₂"],
                "ans": 1,
                "sol": "Calcium has valency 2 (Ca²⁺) and Carbonate has valency 2 (CO₃²⁻). Crossing gives Ca₂(CO₃)₂, which simplifies to CaCO₃."
            },
            {
                "id": "q24",
                "q": "24. What is the chemical formula of Sodium Carbonate?",
                "options": ["NaCO₃", "Na₂CO₃", "Na(CO₃)₂", "Na₂C"],
                "ans": 1,
                "sol": "Sodium is Na⁺ (valency 1) and Carbonate is CO₃²⁻ (valency 2). Crossing gives Na₂CO₃."
            },
            {
                "id": "q25",
                "q": "25. What is the chemical formula of Ammonium Sulphate?",
                "options": ["NH₄SO₄", "(NH₄)₂SO₄", "(NH₄)₂S", "NH₄(SO₄)₂"],
                "ans": 1,
                "sol": "Ammonium is NH₄⁺ (valency 1) and Sulphate is SO₄²⁻ (valency 2). Crossing valencies yields (NH₄)₂SO₄."
            },
            {
                "id": "q26",
                "q": "26. What is the chemical formula of Calcium Phosphate?",
                "options": ["CaPO₄", "Ca₂(PO₄)₃", "Ca₃(PO₄)₂", "Ca(PO₄)₂"],
                "ans": 2,
                "sol": "Calcium is Ca²⁺ (valency 2) and Phosphate is PO₄³⁻ (valency 3). Crossing valencies gives Ca₃(PO₄)₂."
            },
            {
                "id": "q27",
                "q": "27. An element X has valency 3 and element Y has valency 2. The formula of the compound formed between X and Y is:",
                "options": ["XY", "X₂Y₃", "X₃Y₂", "XY₃"],
                "ans": 1,
                "sol": "Writing symbols with valencies underneath: X (3), Y (2). Criss-crossing gives X₂Y₃."
            },
            {
                "id": "q28",
                "q": "28. An element A forms a chloride ACl₄. What will be the formula of its oxide?",
                "options": ["AO", "AO₂", "A₂O", "A₂O₃"],
                "ans": 1,
                "sol": "Since Chlorine has valency 1, in ACl₄ the valency of A must be 4. When A (valency 4) combines with O (valency 2), crossing gives A₂O₄, which simplifies to AO₂."
            },
            {
                "id": "q29",
                "q": "29. What is the chemical formula of Copper(II) Nitrate?",
                "options": ["CuNO₃", "Cu(NO₃)₂", "Cu₂NO₃", "Cu₃(NO₃)₂"],
                "ans": 1,
                "sol": "Copper(II) has charge +2 (Cu²⁺) and Nitrate is NO₃⁻ (charge -1). Crossing yields Cu(NO₃)₂."
            },
            {
                "id": "q30",
                "q": "30. What is the chemical formula of Sodium Sulphite?",
                "options": ["Na₂SO₄", "Na₂S", "Na₂SO₃", "NaSO₃"],
                "ans": 2,
                "sol": "Sodium is Na⁺ (valency 1) and Sulphite is SO₃²⁻ (valency 2). Crossing yields Na₂SO₃ (distinguished from sulphate Na₂SO₄ and sulphide Na₂S)."
            }
        ]
    },
    {
        "id": 20,
        "badge": "Slide 20 • Dedicated Quiz Challenge (Part 4/4)",
        "title": "Mastery Quiz: Molecular Mass, Formula Units & Frontiers",
        "subtitle": "Calculate masses, evaluate limits of mass conservation, and review historical discoveries",
        "teacher": "Congratulations on reaching the final slide of our Atoms and Molecules Chapter! This last challenge covers molecular mass, formula unit mass calculations, the cinnabar mineral, and mass-energy frontiers. Once completed, your chapter mastery will be complete!",
        "quiz": [
            {
                "id": "q31",
                "q": "31. What is the molecular mass of Nitric Acid (HNO₃)? (Given: H = 1 u, N = 14 u, O = 16 u)",
                "options": ["31 u", "48 u", "63 u", "79 u"],
                "ans": 2,
                "sol": "Molecular mass of HNO₃ = 1 + 14 + (3 × 16) = 1 + 14 + 48 = 63 u."
            },
            {
                "id": "q32",
                "q": "32. What is the molecular mass of Glucose (C₆H₁₂O₆)? (Given: C = 12 u, H = 1 u, O = 16 u)",
                "options": ["90 u", "180 u", "174 u", "204 u"],
                "ans": 1,
                "sol": "Molecular mass of C₆H₁₂O₆ = (6 × 12) + (12 × 1) + (6 × 16) = 72 + 12 + 96 = 180 u."
            },
            {
                "id": "q33",
                "q": "33. What is the formula unit mass of Calcium Chloride (CaCl₂)? (Given: Ca = 40 u, Cl = 35.5 u)",
                "options": ["75.5 u", "111 u", "112 u", "146 u"],
                "ans": 1,
                "sol": "Formula Unit Mass of CaCl₂ = (1 × 40) + (2 × 35.5) = 40 + 71 = 111 u."
            },
            {
                "id": "q34",
                "q": "34. What is the percentage of oxygen by mass in pure water (H₂O)? (Given: H = 1 u, O = 16 u)",
                "options": ["11.11%", "50.00%", "88.89%", "94.20%"],
                "ans": 2,
                "sol": "Molecular mass of H₂O = 18 u. Mass of Oxygen = 16 u. Percentage = (16 / 18) × 100% = 88.89%."
            },
            {
                "id": "q35",
                "q": "35. What is the formula unit mass of Blue Vitriol (CuSO₄·5H₂O)? (Given: Cu = 63.5 u, S = 32 u, O = 16 u, H = 1 u)",
                "options": ["159.5 u", "249.5 u", "210.5 u", "285.5 u"],
                "ans": 1,
                "sol": "Mass of CuSO₄ = 63.5 + 32 + (4 × 16) = 159.5 u. Mass of 5H₂O = 5 × 18 = 90 u. Total = 159.5 + 90 = 249.5 u."
            },
            {
                "id": "q36",
                "q": "36. Cinnabar (Hingula) is an ancient Indian ore of which transition metal?",
                "options": ["Gold", "Silver", "Mercury (Hg)", "Copper"],
                "ans": 2,
                "sol": "Cinnabar is Mercuric Sulphide (HgS), the primary historical ore used in India for the thermal extraction of liquid mercury."
            },
            {
                "id": "q37",
                "q": "37. According to Einstein's mass-energy equation E = Δm·c², why does the mass of products in an ordinary chemical reaction appear strictly identical to the reactants?",
                "options": [
                    "Because chemical reactions produce zero energy change",
                    "Because the mass defect Δm = ΔE / c² is extremely tiny (~10⁻¹¹ kg) and impossible to detect on laboratory balances",
                    "Because energy is converted into extra atoms",
                    "Because the speed of light is zero in chemical glassware"
                ],
                "ans": 1,
                "sol": "Because the speed of light squared (c² ≈ 9 × 10¹⁶ m²/s²) is gigantic, dividing typical chemical energy release (~10⁵ J) by c² gives a mass change of ~10⁻¹² kg, which is far too tiny for any balance to register."
            },
            {
                "id": "q38",
                "q": "38. What is the molecular mass of ethanol (C₂H₅OH)? (Given: C = 12 u, H = 1 u, O = 16 u)",
                "options": ["30 u", "46 u", "45 u", "60 u"],
                "ans": 1,
                "sol": "Molecular mass = (2 × 12) + (6 × 1) + 16 = 24 + 6 + 16 = 46 u."
            },
            {
                "id": "q39",
                "q": "39. The formula unit mass of sodium oxide (Na₂O) is: (Given: Na = 23 u, O = 16 u)",
                "options": ["39 u", "62 u", "54 u", "78 u"],
                "ans": 1,
                "sol": "Mass of Na₂O = (2 × 23) + (1 × 16) = 46 + 16 = 62 u."
            },
            {
                "id": "q40",
                "q": "40. Which radioisotope developed at the Bhabha Atomic Research Centre (BARC) is extensively used in teletherapy for cancer treatment?",
                "options": ["Carbon-14", "Cobalt-60", "Sodium-23", "Lead-206"],
                "ans": 1,
                "sol": "Cobalt-60 (⁶⁰Co) is a high-energy gamma-emitting radioisotope widely produced and deployed by BARC for teletherapy radiation treatment of cancer."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Total Slides: {len(SLIDES_DATA)}")
    checkpoints_count = sum(len(s.get("checkpoints", [])) for s in SLIDES_DATA)
    quiz_count = sum(len(s.get("quiz", [])) for s in SLIDES_DATA)
    print(f"Total In-Slide Checkpoints: {checkpoints_count}")
    print(f"Total Quiz Questions: {quiz_count}")
    assert len(SLIDES_DATA) == 20, "Must be exactly 20 slides"
    assert checkpoints_count == 32, "Must be exactly 32 checkpoints (2 per content slide)"
    assert quiz_count == 40, "Must be exactly 40 quiz questions across slides 17-20"
    print("All curriculum data validations passed!")


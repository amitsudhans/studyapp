#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Slides 1-8 for NCERT Class 10 Science - Chapter 1: Chemical Reactions and Equations
Strict constraints:
- Title strictly 1-3 words.
- Spoken lecture strictly 195-215 words.
- Pure Indian male teacher voice styling.
- Zero persona titles (Dr, Sir, Mr, Mrs, etc.) and zero fictional human names (Raghav, etc.).
- 2 checkpoints per slide with 4 options, hint, and explanation.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Everyday Chemical Changes",
        "subtitle": "Daily Transformations, Rearrangements of Atoms, and Breaking Bonds",
        "speech": (
            "Welcome to our laboratory exploration of chemical reactions and equations. Look around your home "
            "and kitchen each day. When fresh milk is left uncovered during warm Indian summers, it turns sour "
            "due to bacterial fermentation producing lactic acid. An iron tawa, pan, or nail exposed to humid "
            "monsoon atmosphere develops a flaky reddish-brown coating called rust. Grapes ferment on vines under "
            "the action of yeasts, converting sugary juices into ethanol. When vegetables and lentils are cooked on "
            "a stove, or when our digestive system breaks complex foods into simple glucose, chemical transformations "
            "take place. Even during cellular respiration, glucose reacts with inhaled oxygen to supply energy "
            "to our body tissues. In all these real-world scenarios, the chemical nature and identity of the "
            "starting material change completely. A chemical reaction has occurred whenever chemical bonds break "
            "and new bonds form between atoms. In contrast to simple physical alterations like melting wax or "
            "boiling water where chemical formulas remain identical, a chemical change produces entirely new "
            "substances with novel physical and chemical properties. Recognizing these fundamental atomic reorganizations "
            "allows us to understand the molecular foundation of materials, biological processes, and industrial synthesis "
            "across our everyday natural world."
        ),
        "checkpoints": [
            {
                "question": "Which of the following everyday events represents a genuine chemical change rather than a physical change?",
                "options": [
                    "Melting of ice cubes in water",
                    "Souring of milk during summer",
                    "Evaporation of rubbing alcohol",
                    "Breaking a glassware flask"
                ],
                "answer": 1,
                "hint": "Identify which process forms a new chemical substance with altered molecular composition.",
                "explanation": "Souring of milk involves bacterial fermentation converting lactose sugars into lactic acid, forming entirely new chemical substances with distinct properties."
            },
            {
                "question": "What fundamental molecular event characterizes every chemical reaction?",
                "options": [
                    "Destruction of fundamental atomic nuclei",
                    "Breaking old bonds and forming new chemical bonds",
                    "Only a physical phase change without bond alterations",
                    "Creation of brand new atomic elements"
                ],
                "answer": 1,
                "hint": "Think about how atoms rearrange while preserving elemental identities.",
                "explanation": "Chemical reactions involve rearranging atoms by breaking reactant bonds and forming new product bonds, without converting atoms into different elements."
            }
        ]
    },
    {
        "id": 2,
        "title": "Magnesium Ribbon Burning",
        "subtitle": "Activity 1.1: Sandpaper Cleaning, Dazzling Flame, and Oxide Ash",
        "speech": (
            "Let us examine Activity 1.1 from your textbook, focusing on the combustion of magnesium ribbon. "
            "Before igniting magnesium ribbon in the laboratory, you must thoroughly rub its surface with sandpaper. "
            "Magnesium is a reactive alkaline earth metal that gradually reacts with atmospheric oxygen at room "
            "temperature, depositing a tough, non-reactive protective film of basic magnesium oxide. Sandpaper abrasive "
            "action strips away this passive oxide barrier, exposing lustrous, pure magnesium metal ready for combustion. "
            "Holding a three-centimeter strip of cleaned ribbon with laboratory tongs over a spirit burner flame causes "
            "it to ignite vigorously. The ribbon burns with a dazzling, brilliant white flame that requires eye protection. "
            "A fine white powdery ash collects inside a clean watch glass held beneath the reaction zone. This white "
            "powder is magnesium oxide. During this vigorous reaction, solid magnesium atoms combine with gaseous oxygen "
            "molecules from the air to synthesize a single compound. The chemical reaction is written as: two atoms of "
            "solid magnesium plus one diatomic oxygen molecule react to produce two formula units of solid magnesium oxide. "
            "This classic experiment proves how solid metals react with invisible gases, transforming lustrous elemental "
            "conductors into ionic oxide powders while liberating immense thermal and radiant light energy."
        ),
        "checkpoints": [
            {
                "question": "Why is magnesium ribbon rubbed with sandpaper before ignition in laboratory Activity 1.1?",
                "options": [
                    "To heat the ribbon to its ignition temperature",
                    "To strip away the protective basic oxide coating",
                    "To coat the ribbon with carbon particles",
                    "To reduce the ribbon's electrical conductivity"
                ],
                "answer": 1,
                "hint": "Consider the passive layer formed when reactive magnesium contacts ambient oxygen.",
                "explanation": "Sandpaper abrasion removes the passive layer of basic magnesium oxide formed by air exposure, allowing pure magnesium to ignite cleanly."
            },
            {
                "question": "What is the chemical composition of the white ash formed when magnesium ribbon burns in air?",
                "options": [
                    "Magnesium carbonate powder",
                    "Magnesium hydroxide paste",
                    "Magnesium oxide compound",
                    "Magnesium nitride crystals"
                ],
                "answer": 2,
                "hint": "Recall the product formed when magnesium combines directly with diatomic atmospheric oxygen.",
                "explanation": "Burning magnesium ribbon combines with oxygen to produce solid magnesium oxide (2Mg + O2 -> 2MgO) collected as a white powdery ash."
            }
        ]
    },
    {
        "id": 3,
        "title": "Chemical Reaction Hallmarks",
        "subtitle": "Activities 1.2 & 1.3: State, Colour, Gas Evolution, and Heat",
        "speech": (
            "How can we determine with scientific certainty whether a chemical reaction has taken place? Laboratory "
            "observations reveal four universal indicators of chemical change. In Activity 1.2, mixing two clear, "
            "colorless aqueous solutions—lead nitrate and potassium iodide—instantly precipitates a brilliant bright "
            "yellow insoluble solid of lead iodide. This dramatic transformation demonstrates an unmistakable change "
            "in colour and change in physical state from clear liquids to a solid precipitate. In Activity 1.3, "
            "placing zinc granules into a conical flask and adding dilute sulphuric acid triggers energetic effervescence. "
            "Bubbles of invisible hydrogen gas evolve rapidly around the metallic granules. Passing this gas near a "
            "burning candle produces a distinct, sharp pop sound, confirming hydrogen liberation. Touching the bottom "
            "of the conical flask reveals that the glass has become noticeably warm. This confirms an exothermic temperature "
            "increase alongside gas evolution. In summary, whenever chemical substances interact, look carefully for four hallmarks: "
            "first, change in state; second, change in colour; third, evolution of a gas; and fourth, change in temperature. "
            "Observing one or more of these distinct thermodynamic and visual signatures proves that existing chemical bonds "
            "have rearranged into entirely new chemical substances with altered physical states and energetic potentials in the flask."
        ),
        "checkpoints": [
            {
                "question": "What visual hallmark is observed when aqueous lead nitrate is mixed with aqueous potassium iodide?",
                "options": [
                    "Evolution of pungent brown fumes",
                    "Formation of a bright yellow precipitate",
                    "Rapid drop in temperature below freezing",
                    "Dissolution of solid into a blue solution"
                ],
                "answer": 1,
                "hint": "Recall Activity 1.2 involving insoluble lead iodide.",
                "explanation": "Mixing lead nitrate and potassium iodide produces a double displacement reaction forming an insoluble bright yellow precipitate of lead iodide (PbI2)."
            },
            {
                "question": "Which gas is evolved when zinc granules react with dilute sulphuric acid in Activity 1.3?",
                "options": [
                    "Carbon dioxide gas",
                    "Oxygen gas",
                    "Hydrogen gas",
                    "Sulphur dioxide gas"
                ],
                "answer": 2,
                "hint": "This light diatomic gas burns with a characteristic pop sound.",
                "explanation": "Zinc reacts with dilute sulphuric acid (Zn + H2SO4 -> ZnSO4 + H2) releasing hydrogen gas, while releasing heat in an exothermic process."
            }
        ]
    },
    {
        "id": 4,
        "title": "Chemical Word Equations",
        "subtitle": "Reactants, Products, Reaction Arrows, and Skeletal Formulas",
        "speech": (
            "Describing chemical reactions using full descriptive prose can be cumbersome. Chemists developed chemical "
            "equations as concise, standardized shorthand representations. Consider our magnesium combustion: writing "
            "out full sentences is condensed into a word equation: Magnesium plus Oxygen yields Magnesium oxide. In any "
            "chemical equation, the starting chemical substances that undergo change are called reactants. Reactants are "
            "placed on the left-hand side with plus signs separating multiple substances. The new substances produced "
            "during the chemical change are called products, written on the right-hand side. An arrow points from reactants "
            "to products, representing the chemical direction of the reaction. We advance further by substituting chemical "
            "names with precise chemical formulas: Mg plus O2 yields MgO. This formula representation is known as a skeletal "
            "chemical equation. Notice something crucial here: on the left side, we have one magnesium atom and two oxygen "
            "atoms, while the right side shows only one magnesium atom and one oxygen atom. Because the number of oxygen "
            "atoms on the reactant side does not match the product side, this skeletal equation is unbalanced. In our next "
            "study session, we will explore why nature requires every single skeletal equation to be strictly balanced before any laboratory calculation or stoichiometry."
        ),
        "checkpoints": [
            {
                "question": "In a standard chemical word equation, where are the reactants positioned relative to the arrow?",
                "options": [
                    "Always above the horizontal reaction arrow",
                    "On the left-hand side pointing toward products",
                    "On the right-hand side after the arrow tip",
                    "Alternating randomly on either side of the arrow"
                ],
                "answer": 1,
                "hint": "Reactants represent the starting ingredients before chemical transformation.",
                "explanation": "Reactants are systematically written on the left-hand side (LHS) with an arrow pointing toward the products on the right-hand side (RHS)."
            },
            {
                "question": "Why is the chemical equation Mg + O2 -> MgO classified as a skeletal equation?",
                "options": [
                    "Because it contains organic hydrocarbon backbones",
                    "Because the number of atoms of each element is not equal on both sides",
                    "Because it can only proceed at absolute zero temperature",
                    "Because magnesium forms a hollow skeletal lattice structure"
                ],
                "answer": 1,
                "hint": "Check the oxygen atom counts on both sides of the equation.",
                "explanation": "An unbalanced chemical equation showing only chemical formulas where atom counts differ between reactants and products is termed a skeletal equation."
            }
        ]
    },
    {
        "id": 5,
        "title": "Conservation of Mass",
        "subtitle": "Lavoisier's Principle, Constant Atom Numbers, and Stoichiometry",
        "speech": (
            "The foundation of chemical equation balancing rests upon the universal Law of Conservation of Mass, "
            "formulated by French chemist Antoine Lavoisier. This fundamental physical law states that matter can neither "
            "be created nor destroyed in any chemical reaction. Consequently, the total mass of all elements present in "
            "the reaction products must exactly equal the total mass of all elements present in the starting reactants. "
            "Because mass is an intrinsic property of individual atoms, this law dictates that the total number of atoms "
            "of each element must remain constant before and after a chemical reaction. When bonds break and re-form, "
            "atoms merely trade partners like dancers in a ballroom; not a single atomic nucleus vanishes, and no new "
            "atoms materialize out of empty space. If an unbalanced skeletal equation shows two oxygen atoms entering a "
            "reaction but only one emerging, it violates mass conservation. Balancing an equation means finding whole-number "
            "stoichiometric coefficients placed in front of chemical formulas so that atom counts for every element on the "
            "reactant side match the product side identically. Mastering this fundamental principle ensures that quantitative calculations, "
            "yield forecasts, and industrial chemical manufacturing adhere strictly to physical reality and atomic mass conservation rules."
        ),
        "checkpoints": [
            {
                "question": "What does the Law of Conservation of Mass demand during any chemical reaction?",
                "options": [
                    "Total product volume must equal total reactant volume",
                    "Total mass of products must equal total mass of reactants",
                    "Reactants must lose half their original molecular mass",
                    "Product temperature must always exceed reactant temperature"
                ],
                "answer": 1,
                "hint": "Matter can neither be created nor destroyed during chemical transformations.",
                "explanation": "The Law of Conservation of Mass dictates that mass cannot be created or destroyed; hence total product mass equals total reactant mass."
            },
            {
                "question": "How does the Law of Conservation of Mass apply to the total number of atoms in a reaction?",
                "options": [
                    "Total atom count increases due to bond energy release",
                    "The number of atoms of each element remains identical on both sides",
                    "Heavier atoms decompose into lighter subatomic fragments",
                    "Atoms double whenever an exothermic reaction occurs"
                ],
                "answer": 1,
                "hint": "Since atomic mass is conserved, elemental atom counts cannot change.",
                "explanation": "Conserving mass requires that the number of atoms of each individual element remains exactly the same before and after the reaction."
            }
        ]
    },
    {
        "id": 6,
        "title": "Balancing Chemical Equations",
        "subtitle": "7-Step Hit-and-Trial Method, Coefficients, and Physical States",
        "speech": (
            "Let us master the systematic 7-step hit-and-trial method using iron reacting with steam: "
            "Fe plus H2O yields Fe3O4 plus H2. In Step 1, draw protective boxes around each chemical formula; never "
            "alter internal subscripts inside formulas. In Step 2, tabulate atom numbers for each element on both sides: "
            "iron shows 1 on left and 3 on right; hydrogen shows 2 on left and 2 on right; oxygen shows 1 on left and 4 on "
            "right. In Step 3, balance the element with the maximum number of atoms first—here, oxygen. Place coefficient 4 "
            "before water, giving 4 oxygen atoms on both sides. In Step 4, balance hydrogen: four water molecules provide 8 "
            "hydrogen atoms, so place coefficient 4 before hydrogen gas on the right. In Step 5, balance iron: three iron atoms "
            "appear in Fe3O4, so place coefficient 3 before Fe on the left. In Step 6, verify all counts: 3 iron, 8 hydrogen, "
            "and 4 oxygen on both sides. The balanced equation reads: 3Fe plus 4H2O yields Fe3O4 plus 4H2. Finally, in Step 7, "
            "append physical state notations: solid for Fe, gas for steam, solid for iron oxide, and gas for hydrogen. Write "
            "reaction conditions like temperature or pressure above the arrow."
        ),
        "checkpoints": [
            {
                "question": "What is the critical rule regarding subscripts when balancing chemical equations?",
                "options": [
                    "Subscripts should be multiplied by two whenever odd",
                    "Formula subscripts must never be altered; only coefficients change",
                    "Subscripts can be removed if atom counts exceed ten",
                    "Subscripts are adjusted before writing state notations"
                ],
                "answer": 1,
                "hint": "Changing a subscript alters the chemical identity of the substance.",
                "explanation": "Chemical formula subscripts define the molecular identity of compounds and must never be altered. Balancing is achieved solely by modifying stoichiometric coefficients."
            },
            {
                "question": "What are the correct stoichiometric coefficients to balance Fe + H2O -> Fe3O4 + H2?",
                "options": [
                    "1 Fe, 2 H2O -> 1 Fe3O4, 2 H2",
                    "3 Fe, 4 H2O -> 1 Fe3O4, 4 H2",
                    "2 Fe, 3 H2O -> 1 Fe3O4, 3 H2",
                    "3 Fe, 2 H2O -> 1 Fe3O4, 2 H2"
                ],
                "answer": 1,
                "hint": "Count 3 iron atoms, 4 oxygen atoms, and 8 hydrogen atoms on both sides.",
                "explanation": "3Fe + 4H2O -> Fe3O4 + 4H2 balances 3 iron atoms, 8 hydrogen atoms, and 4 oxygen atoms on both sides of the equation."
            }
        ]
    },
    {
        "id": 7,
        "title": "Combination Reactions Overview",
        "subtitle": "Single Product Synthesis, Coal Burning, and Water Formation",
        "speech": (
            "Now let us classify chemical reactions systematically, beginning with combination reactions. By definition, "
            "a combination reaction is a process in which two or more reactants combine chemically to form a single "
            "product. The general format is simple: reactant A plus reactant B yields compound AB. Consider the combustion "
            "of coal in a furnace: solid carbon reacts with gaseous oxygen from the air to synthesize one single product, "
            "carbon dioxide gas: C solid plus O2 gas yields CO2 gas. Similarly, when hydrogen gas burns in the presence of "
            "oxygen, water is synthesized: two molecules of hydrogen gas combine with one molecule of oxygen gas to yield "
            "two molecules of liquid water. In both cases, multiple distinct elemental or compound reactants unite into "
            "a single unified product species. Combination reactions are often energetically favorable because new bond "
            "formations release substantial bonding energy. These reactions form the bedrock of geological mineral formation, "
            "industrial chemical production like synthetic ammonia, and everyday atmospheric combustion. Whenever you observe "
            "several starting substances merging into one single chemical formula on the right side of the reaction arrow, "
            "you can confidently identify that chemical transformation as an authentic, single-product combination reaction in fundamental laboratory chemistry."
        ),
        "checkpoints": [
            {
                "question": "How is a combination reaction formally defined in chemical science?",
                "options": [
                    "A reaction where one compound splits into multiple simpler gases",
                    "A reaction where two or more substances combine to form a single product",
                    "A reaction involving mutual exchange of cations and anions",
                    "A reaction where an element loses electrons without bonding"
                ],
                "answer": 1,
                "hint": "Look for multiple starting materials yielding only one final compound.",
                "explanation": "A combination reaction occurs when two or more reactants combine chemically to produce a single product (A + B -> AB)."
            },
            {
                "question": "Which of the following balanced equations represents a combination reaction?",
                "options": [
                    "Zn + CuSO4 -> ZnSO4 + Cu",
                    "2H2(g) + O2(g) -> 2H2O(l)",
                    "CaCO3(s) -> CaO(s) + CO2(g)",
                    "NaCl + AgNO3 -> AgCl + NaNO3"
                ],
                "answer": 1,
                "hint": "Identify the equation where two elemental gases combine into a single product.",
                "explanation": "2H2(g) + O2(g) -> 2H2O(l) features two reactants combining to form a single product, water, defining a combination reaction."
            }
        ]
    },
    {
        "id": 8,
        "title": "Quicklime and Slaked-Lime",
        "subtitle": "Activity 1.4: Vigorous Hydration, Boiling Heat, and Wall Whitewashing",
        "speech": (
            "Activity 1.4 presents one of chemistry's most dramatic combination reactions: the hydration of quicklime. "
            "When water is poured slowly into a beaker containing solid calcium oxide, commonly known as quicklime, a "
            "violent reaction begins. The mixture hisses vigorously, swells, and releases tremendous heat, causing the "
            "liquid to boil. Touching the beaker confirms an intense exothermic temperature rise. Calcium oxide combines "
            "with water to synthesize calcium hydroxide, commonly called slaked lime: CaO solid plus H2O liquid yields "
            "Ca(OH)2 aqueous plus heat. A dilute clear suspension of slaked lime has been used for centuries across "
            "India for whitewashing building walls. When wet slaked lime is applied to a wall, it slowly absorbs carbon "
            "dioxide gas from the ambient air over two to three days. Calcium hydroxide reacts with carbon dioxide to "
            "form an insoluble, durable, brilliant white crust of calcium carbonate: Ca(OH)2 plus CO2 yields CaCO3 plus "
            "H2O. Calcium carbonate is the exact chemical compound that constitutes natural limestone and sparkling marble. "
            "This remarkable two-step sequence demonstrates how an exothermic combination reaction produces slaked lime, "
            "which subsequently undergoes atmospheric carbonation to provide hard, weather-resistant architectural finishes across traditional homes, "
            "temples, and historical monuments throughout our vast nation."
        ),
        "checkpoints": [
            {
                "question": "What is the common chemical name and formula of quicklime used in Activity 1.4?",
                "options": [
                    "Calcium carbonate, CaCO3",
                    "Calcium oxide, CaO",
                    "Calcium hydroxide, Ca(OH)2",
                    "Calcium sulphate, CaSO4"
                ],
                "answer": 1,
                "hint": "This white solid reacts violently with water to produce slaked lime.",
                "explanation": "Quicklime is the common name for solid calcium oxide (CaO), which reacts exothermically with water to form slaked lime."
            },
            {
                "question": "What substance gives freshly whitewashed walls a shiny, marble-like finish after 2 to 3 days?",
                "options": [
                    "Calcium oxide powder",
                    "Calcium chloride crystals",
                    "Calcium carbonate layer",
                    "Calcium bicarbonate solution"
                ],
                "answer": 2,
                "hint": "Formed when slaked lime reacts with atmospheric carbon dioxide.",
                "explanation": "Slaked lime Ca(OH)2 absorbs ambient CO2 over 2-3 days, reacting to form a hard, shiny layer of calcium carbonate (CaCO3), identical in formula to marble."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        twc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) - Speech: {wc} words")
        assert 1 <= twc <= 3, f"Title length out of bounds: {twc}"
        assert 195 <= wc <= 215, f"Speech word count out of bounds on slide {s['id']}: {wc}"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("Part 1 verification: ALL PASSED!")

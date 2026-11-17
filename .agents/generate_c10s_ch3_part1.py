"""Generate Slides 1 to 8 for Class 10 Science Chapter 3: Metals and Non-metals
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
        "title": "Metallic Physical Properties",
        "subtitle": "Lustre, Hardness Variation, Malleability, Ductility, and Conduction Profiles",
        "speech": "Welcome to our laboratory study of metals and non-metals. Elements are classified based on physical and chemical behavior. In Activity 3.1, examining iron, copper, aluminium, and magnesium reveals that when cleaned with sandpaper to remove surface oxide films, pure metals display a brilliant reflective sheen known as metallic lustre. Metals are generally hard and mechanically robust, though hardness varies considerably across elements. In Activity 3.2, while iron and copper resist cutting, alkali metals like sodium and potassium are exceptionally soft and easily sliced with a regular knife. In Activity 3.3, hammering metals demonstrates malleability; metals flatten into thin foils without shattering, with gold and silver being the most malleable substances known. Activity 3.4 highlights ductility, which is the physical ability to be drawn into fine wires; remarkably, a single gram of gold can be drawn into a wire two kilometres long. Activity 3.5 demonstrates that metals are exceptional heat conductors with high melting points; silver and copper conduct heat best, while lead and mercury are poor conductors. Finally, Activity 3.6 proves electrical conductivity as metal samples complete an electric circuit, explaining why copper wires are insulated with polyvinylchloride, while sonorous resonance makes metals ideal for school bells.",
        "content": {
            "concept": "Metals possess distinctive physical properties: metallic lustre, variable hardness, high malleability (sheets), high ductility (wires), thermal and electrical conductivity, and sonority. Silver and copper are the best heat conductors.",
            "formula": "\\text{Malleability: Beaten into Sheets} \\quad | \\quad \\text{Ductility: Drawn into Wires (1 g Gold } \\rightarrow 2\\text{ km Wire)}",
            "points": [
                "Activity 3.1: Rubbing metal surfaces with sandpaper uncovers shiny metallic lustre.",
                "Activity 3.2: Iron and copper are hard; alkali metals like sodium are soft enough to cut with a knife.",
                "Activity 3.3: Malleability allows metals to be hammered into thin sheets (gold and silver lead).",
                "Activity 3.4: Ductility enables wire drawing; 1 g gold yields a 2 km continuous wire.",
                "Activity 3.5 & 3.6: Silver and copper are prime thermal/electrical conductors; wires are coated with insulating PVC."
            ]
        },
        "checkpoints": [
            {
                "question": "Which metal exhibits the highest ductility, allowing a two-kilometre wire to be drawn from just one gram of metal?",
                "options": [
                    "Aluminium",
                    "Copper",
                    "Gold",
                    "Silver"
                ],
                "answer": 2,
                "hint": "This precious yellow metal is also among the most malleable substances known.",
                "explanation": "Gold is the most ductile metal known. A continuous wire of approximately two kilometres can be drawn from a single gram of pure gold."
            },
            {
                "question": "Why are domestic electric transmission wires coated with materials like polyvinylchloride (PVC) or rubber?",
                "options": [
                    "To increase the overall mass and speed of current transmission",
                    "To insulate the conducting metal and prevent electric shocks",
                    "To make the copper wire sonorous when struck",
                    "To protect the metal from melting under normal sunlight"
                ],
                "answer": 1,
                "hint": "PVC and rubber are non-conducting insulating polymers that block electrical leakage.",
                "explanation": "Metals are excellent conductors of electricity. Coating electrical wires with non-conducting insulating materials like PVC or rubber prevents accidental electrical contact and dangerous shocks."
            }
        ]
    },
    {
        "id": 2,
        "title": "Nonmetal Physical Exceptions",
        "subtitle": "Anomalous Liquid States, Palm Melting, Iodine Lustre, and Carbon Allotropes",
        "speech": "While general physical rules help classify elements in the periodic table, nature presents remarkable exceptions that must be thoroughly understood for chemical study. Non-metals encompass diverse elements such as carbon, sulphur, iodine, oxygen, and hydrogen, existing predominantly as solids or gases. However, bromine is the solitary non-metal that exists as a volatile reddish-brown liquid at room temperature. Conversely, among metals, mercury is the only metal found in liquid state under standard laboratory conditions. Furthermore, while metals typically boast high melting points, gallium and caesium possess extraordinarily low melting thresholds of around thirty degrees Celsius, causing solid pellets to melt into liquid puddles simply from the warmth of human palms. In optical properties, while non-metals are dull, iodine is a striking crystalline non-metal displaying brilliant metallic lustre. Carbon defies physical generalizations through its distinct allotropic forms: diamond, a tetrahedral carbon crystal lattice, is the hardest naturally occurring substance known, possessing exceptionally high melting and boiling points; meanwhile, graphite, arranged in layered hexagonal graphene sheets with delocalised pi electrons, serves as an outstanding conductor of electricity. Finally, alkali metals including lithium, sodium, and potassium exhibit remarkably low densities and low melting points, allowing them to float on water while reacting vigorously.",
        "content": {
            "concept": "Physical property exceptions: Mercury is a liquid metal; bromine is a liquid non-metal. Gallium and caesium melt on human palms. Iodine is a lustrous non-metal. Diamond is the hardest natural substance, while graphite conducts electricity. Alkali metals are soft with low densities.",
            "formula": "\\text{Liquid Elements: Mercury (Metal) } & \\text{ Bromine (Non-metal)} \\quad | \\quad \\text{Palm Melting: Gallium (29.8°C), Caesium (28.4°C)}",
            "points": [
                "Mercury is the only metal that is liquid at room temperature; bromine is the only liquid non-metal.",
                "Gallium and caesium have exceptionally low melting points and melt on the warmth of the palm.",
                "Iodine is a non-metal that possesses bright metallic lustre.",
                "Diamond (carbon allotrope) is the hardest natural substance with a very high melting point.",
                "Graphite (carbon allotrope) conducts electricity due to free mobile electrons in its hexagonal sheets.",
                "Lithium, sodium, and potassium are soft alkali metals with low densities cut easily with knives."
            ]
        },
        "checkpoints": [
            {
                "question": "Which of the following non-metals exists as a liquid under standard room temperature and pressure?",
                "options": [
                    "Chlorine",
                    "Bromine",
                    "Iodine",
                    "Sulphur"
                ],
                "answer": 1,
                "hint": "This halogen forms a reddish-brown fuming liquid at ambient conditions.",
                "explanation": "Bromine is the only non-metal that exists as a liquid at room temperature. Chlorine is a gas, while iodine and sulphur are solids."
            },
            {
                "question": "Why does graphite conduct electricity whereas diamond behaves as an electrical insulator?",
                "options": [
                    "Graphite contains delocalised mobile electrons between its hexagonal carbon layers",
                    "Diamond contains metallic iron impurities that absorb all electrical charge",
                    "Graphite dissolves in atmospheric moisture to form conducting hydronium ions",
                    "Diamond undergoes radioactive decay that blocks current flow"
                ],
                "answer": 0,
                "hint": "In graphite, each carbon atom forms three covalent bonds, leaving one free valence electron.",
                "explanation": "In graphite, each carbon atom is bonded to three others in planar hexagonal rings, leaving one free valence electron per carbon atom. These delocalised electrons move freely to conduct electricity."
            }
        ]
    },
    {
        "id": 3,
        "title": "Metal Oxide Synthesis",
        "subtitle": "Thermal Combustion in Air, Basicity vs Acidity, and Kerosene Oil Storage",
        "speech": "When metals are heated in the presence of air, they combine directly with atmospheric oxygen to form solid metallic oxides. In Activity 3.9, burning magnesium ribbon produces a dazzling white flame and leaves behind basic magnesium oxide ash. When dissolved in water, this oxide turns red litmus paper blue, proving its basic character. In contrast, burning sulphur powder produces choking sulphur dioxide gas that dissolves in water to form sulphurous acid, turning blue litmus paper red and demonstrating the acidic nature of non-metallic oxides. Copper does not burn with an open flame, but prolonged heating coats the orange metal with a durable black layer of copper(II) oxide. Aluminium reacts with oxygen to form aluminium oxide. The chemical affinity for oxygen varies dramatically across the reactivity series. Alkali metals like sodium and potassium react so vigorously with atmospheric oxygen and moisture that they ignite spontaneously; consequently, they must be stored permanently immersed in unreactive kerosene oil. Moderately active metals such as magnesium, aluminium, zinc, and lead develop a thin, protective surface layer of oxide at room temperature that seals the underlying metal from further corrosion. Iron filings burn vigorously when sprinkled into a flame, whereas silver and gold remain unreacted.",
        "content": {
            "concept": "Metals combine with oxygen to form metallic oxides, which are typically basic. Sodium and potassium catch fire in air and must be stored in kerosene. Magnesium, aluminium, zinc, and lead form self-protecting oxide layers. Silver and gold do not react with oxygen.",
            "formula": "\\text{Metal} + \\text{Oxygen} \\rightarrow \\text{Metal oxide} \\quad | \\quad 2\\text{Cu} + \\text{O}_2 \\xrightarrow{\\Delta} 2\\text{CuO} [\\text{Black}] \\quad | \\quad 4\\text{Al} + 3\\text{O}_2 \\rightarrow 2\\text{Al}_2\\text{O}_3",
            "points": [
                "Activity 3.9: Heating metals produces metal oxides; basic metal oxides turn red litmus blue.",
                "Non-metal combustion produces acidic oxides (SO2 dissolves to form H2SO3, turning blue litmus red).",
                "Copper forms a surface layer of black copper(II) oxide (CuO) on prolonged heating.",
                "Sodium and potassium react violently with air and moisture, requiring storage under kerosene oil.",
                "Protective oxide films on Mg, Al, Zn, and Pb prevent continuous progressive oxidation.",
                "Noble metals silver and gold do not react with oxygen even at elevated temperatures."
            ]
        },
        "checkpoints": [
            {
                "question": "Why are metallic sodium and potassium kept permanently immersed in kerosene oil?",
                "options": [
                    "To prevent them from dissolving into atmospheric nitrogen",
                    "Because they react vigorously and ignite spontaneously with atmospheric oxygen and moisture",
                    "To harden their soft surfaces so they cannot be cut by knives",
                    "To convert them into unreactive liquid amalgam fuels"
                ],
                "answer": 1,
                "hint": "Alkali metals have very low ionization energies and react violently with air and water.",
                "explanation": "Sodium and potassium react vigorously with oxygen and water vapour in the air, catching fire immediately. Storing them under kerosene prevents contact with air and moisture."
            },
            {
                "question": "What product is formed on the surface of copper metal when it is heated strongly in air?",
                "options": [
                    "Green basic copper carbonate",
                    "Reddish copper(I) hydride",
                    "Black copper(II) oxide",
                    "White copper sulphate"
                ],
                "answer": 2,
                "hint": "The balanced reaction is 2Cu + O2 -> 2CuO.",
                "explanation": "Heating copper strongly in air forms a black surface coating of copper(II) oxide: 2Cu + O2 -> 2CuO."
            }
        ]
    },
    {
        "id": 4,
        "title": "Amphoteric Oxide Chemistry",
        "subtitle": "Dual Acid-Base Reactivity, Sodium Aluminate Formation, and Anodising Protection",
        "speech": "While most metallic oxides exhibit strictly basic properties, certain metal oxides display a remarkable dual chemical nature. Oxides that react with both acids and bases to produce a salt and water are defined as amphoteric oxides. Aluminium oxide and zinc oxide serve as classical examples of this amphoteric behavior. When aluminium oxide reacts with hydrochloric acid, it functions as a base, yielding aluminium chloride salt and water: aluminium oxide plus six hydrochloric acid yields two aluminium chloride plus three water. Conversely, when aluminium oxide is treated with concentrated sodium hydroxide base, it acts as an acid, forming water-soluble sodium aluminate and water: aluminium oxide plus two sodium hydroxide yields two sodium aluminate plus water. Most metal oxides are completely insoluble in water, but sodium oxide and potassium oxide dissolve readily to form potent alkalis, sodium hydroxide and potassium hydroxide. The formation of unreactive oxide coatings on aluminium inspires the industrial process known as anodising. In anodising, cleaned aluminium articles serve as the anode during the electrolysis of dilute sulphuric acid. Evolved oxygen gas reacts with the aluminium anode to create a thick, uniform, non-porous aluminium oxide barrier layer that confers superior corrosion resistance and readily accepts decorative dye pigments.",
        "content": {
            "concept": "Amphoteric oxides react with both acids and bases to produce salt and water (e.g., Al2O3, ZnO). Anodising is an electrolytic process that thickens the protective aluminium oxide layer on aluminium articles using dilute sulphuric acid.",
            "formula": "\\text{Acid: } \\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\rightarrow 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O} \\quad | \\quad \\text{Base: } \\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\rightarrow 2\\text{NaAlO}_2 + \\text{H}_2\\text{O}",
            "points": [
                "Amphoteric oxides react with both acids and bases to yield salt and water.",
                "Aluminium oxide (Al2O3) and zinc oxide (ZnO) are primary amphoteric oxides.",
                "Al2O3 reacts with NaOH to produce soluble sodium aluminate (NaAlO2) and water.",
                "Soluble metallic oxides like Na2O and K2O dissolve in water to form strong alkalis.",
                "Anodising electrolytically thickens the natural Al2O3 protective oxide film using dilute H2SO4.",
                "Anodised aluminium resists corrosion and accepts vibrant dyes for commercial cookware and aircraft."
            ]
        },
        "checkpoints": [
            {
                "question": "Which of the following compounds is an amphoteric oxide that reacts with both acids and bases?",
                "options": [
                    "Sodium oxide (Na2O)",
                    "Aluminium oxide (Al2O3)",
                    "Magnesium oxide (MgO)",
                    "Calcium oxide (CaO)"
                ],
                "answer": 1,
                "hint": "This oxide reacts with HCl to form chloride and with NaOH to form aluminate.",
                "explanation": "Aluminium oxide (Al2O3) and zinc oxide (ZnO) are amphoteric oxides. They react with acids to form salts and water, and also react with bases to form aluminates or zincates."
            },
            {
                "question": "What is the function of the anodising process applied to aluminium articles?",
                "options": [
                    "To electroplate a layer of pure gold over aluminium",
                    "To thicken the natural protective aluminium oxide layer for corrosion resistance",
                    "To dissolve the aluminium core into a light porous foam",
                    "To convert aluminium into an electric superconductor"
                ],
                "answer": 1,
                "hint": "Anodising uses electrolysis in dilute sulphuric acid to grow a durable Al2O3 layer.",
                "explanation": "Anodising is an electrolytic technique where aluminium acts as the anode in dilute H2SO4. Evolved oxygen thickens the surface Al2O3 layer, rendering the article highly corrosion-resistant."
            }
        ]
    },
    {
        "id": 5,
        "title": "Metals Reacting Water",
        "subtitle": "Cold Water Flame Ignition, Floating Calcium Bubbles, Steam Gas-Wool Reactions",
        "speech": "Metals interact with water with vastly differing intensities, producing a metal oxide or hydroxide alongside liberated hydrogen gas. In Activity 3.10, testing cold water reveals that sodium and potassium react violently and exothermically; the heat evolved is so intense that the released hydrogen gas immediately ignites with violet and yellow flames. Calcium reacts less violently with cold water; the heat released is insufficient to ignite the hydrogen gas. Interestingly, calcium pieces begin floating on the water surface because generated bubbles of hydrogen gas adhere tenaciously to the metal surface. Magnesium does not react with cold water at all; however, it reacts smoothly with hot boiling water to form magnesium hydroxide and hydrogen gas, also floating as bubbles stick to its surface. Metals like aluminium, iron, and zinc show zero reaction with cold or hot liquid water, but react readily with steam. Passing steam over red-hot iron inside a combustion tube forms magnetic iron(II,III) oxide and hydrogen gas in laboratory apparatus: three iron plus four steam yields Fe3O4 plus four hydrogen. Finally, least reactive metals including lead, copper, silver, and gold show absolutely no reaction with water or steam under any rigorous laboratory heating conditions during classroom investigations.",
        "content": {
            "concept": "Metals react with water to form metal oxides/hydroxides and hydrogen gas. Potassium and sodium react violently with cold water, igniting H2. Calcium and magnesium float due to adhering H2 bubbles. Al, Fe, and Zn react only with steam. Cu, Ag, and Au do not react.",
            "formula": "2\\text{K} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{KOH} + \\text{H}_2\\uparrow + \\text{Heat} \\quad | \\quad 3\\text{Fe} + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4 + 4\\text{H}_2\\uparrow",
            "points": [
                "Activity 3.10: Potassium and sodium react violently with cold water; evolved H2 catches fire.",
                "Calcium reacts moderately with cold water; it floats because H2 bubbles stick to its surface.",
                "Magnesium does not react with cold water, but reacts with hot water and floats.",
                "Aluminium, iron, and zinc react exclusively with steam to form metal oxides and H2 gas.",
                "Lead, copper, silver, and gold do not react with water in liquid or steam form under any conditions."
            ]
        },
        "checkpoints": [
            {
                "question": "Why do pieces of calcium metal begin floating when dropped into cold water?",
                "options": [
                    "Calcium metal has a density lower than liquid water",
                    "Bubbles of liberated hydrogen gas stick to the surface of the calcium pieces",
                    "Calcium absorbs water molecules and converts into an airy gaseous foam",
                    "Heat from the reaction boils water into a supporting steam cushion"
                ],
                "answer": 1,
                "hint": "The evolved gas forms tiny clinging bubbles that impart buoyancy to the metal.",
                "explanation": "Calcium reacts with cold water: Ca + 2H2O -> Ca(OH)2 + H2. The reaction is less violent, and bubbles of hydrogen gas stick to the metal surface, causing it to float."
            },
            {
                "question": "Which of the following metals reacts neither with cold water nor with hot water, but reacts vigorously with steam?",
                "options": [
                    "Sodium",
                    "Calcium",
                    "Iron",
                    "Copper"
                ],
                "answer": 2,
                "hint": "This metal forms magnetic oxide Fe3O4 when exposed to steam at high temperature.",
                "explanation": "Iron, aluminium, and zinc do not react with cold or hot liquid water, but react with steam: 3Fe + 4H2O(g) -> Fe3O4 + 4H2."
            }
        ]
    },
    {
        "id": 6,
        "title": "Metals Reacting Acids",
        "subtitle": "Effervescence Kinetics, Nitric Acid Oxidation Exceptions, and Aqua Regia Fumes",
        "speech": "When metals react with dilute mineral acids, they displace hydrogen to form an ionic salt and hydrogen gas. In Activity 3.11, placing cleaned metal samples into test tubes containing dilute hydrochloric acid with suspended thermometers reveals a clear kinetic hierarchy. Magnesium reacts most rapidly with vigorous bubbling and the highest exothermic temperature rise. The reactivity follows the sequence: magnesium is greater than aluminium, which is greater than zinc, which is greater than iron. Copper displays zero effervescence and zero temperature change, confirming its low reactivity. Intriguingly, when metals react with nitric acid, hydrogen gas is generally not evolved. Nitric acid is a powerful oxidising agent; it immediately oxidises the generated hydrogen into water while undergoing reduction to various nitrogen oxides such as nitrous oxide, nitric oxide, or nitrogen dioxide. However, magnesium and manganese are notable exceptions that react with very dilute nitric acid to liberate hydrogen gas. When chemists need to dissolve unreactive noble metals like gold and platinum, they employ aqua regia, meaning royal water. Aqua regia is a freshly prepared, highly corrosive, fuming mixture of three parts concentrated hydrochloric acid and one part concentrated nitric acid, which dissolves noble metals by forming soluble chloro-complexes.",
        "content": {
            "concept": "Metals react with dilute acids to yield salts and hydrogen gas (Mg > Al > Zn > Fe). Nitric acid (HNO3) oxidises liberated H2 to H2O and reduces to nitrogen oxides; only Mg and Mn evolve H2 with very dilute HNO3. Aqua regia (3:1 conc. HCl:HNO3) dissolves gold and platinum.",
            "formula": "\\text{Metal} + \\text{Dilute Acid} \\rightarrow \\text{Salt} + \\text{H}_2\\uparrow \\quad | \\quad \\text{Aqua Regia: 3 Conc. HCl : 1 Conc. HNO}_3",
            "points": [
                "Activity 3.11: Acid reactivity order is Mg > Al > Zn > Fe; copper shows zero reaction.",
                "Hydrogen gas is not evolved with HNO3 because it is a strong oxidising agent that forms H2O.",
                "Magnesium and manganese react with very dilute (1%) HNO3 to evolve H2 gas.",
                "Aqua regia is a freshly prepared 3:1 mixture of concentrated HCl and concentrated HNO3.",
                "Aqua regia can dissolve noble metals including gold and platinum through complexation."
            ]
        },
        "checkpoints": [
            {
                "question": "Why is hydrogen gas generally not evolved when most metals react with dilute nitric acid?",
                "options": [
                    "Nitric acid is too weak to displace hydrogen from metal lattices",
                    "Nitric acid is a strong oxidising agent that oxidises liberated H2 into water",
                    "Nitric acid precipitates an insoluble metal nitrate crust that halts reaction",
                    "Nitrogen gas absorbs all liberated hydrogen atoms to synthesize ammonia"
                ],
                "answer": 1,
                "hint": "Nitric acid acts as a powerful electron acceptor, reducing itself to nitrogen oxides.",
                "explanation": "Nitric acid (HNO3) is a strong oxidising agent. It oxidises the generated H2 gas into water (H2O) and is itself reduced to nitrogen oxides (N2O, NO, or NO2)."
            },
            {
                "question": "What is the volumetric ratio of concentrated hydrochloric acid to concentrated nitric acid in aqua regia?",
                "options": [
                    "1 part conc. HCl to 3 parts conc. HNO3",
                    "3 parts conc. HCl to 1 part conc. HNO3",
                    "1 part conc. HCl to 1 part conc. HNO3",
                    "4 parts conc. HCl to 2 parts conc. HNO3"
                ],
                "answer": 1,
                "hint": "Hydrochloric acid constitutes the major component (75% by volume).",
                "explanation": "Aqua regia (royal water) is a freshly prepared mixture containing concentrated hydrochloric acid and concentrated nitric acid in a 3:1 ratio by volume."
            }
        ]
    },
    {
        "id": 7,
        "title": "Metal Displacement Reactions",
        "subtitle": "Single Displacement Mechanics, Solution Colour Transitions, and Relative Activity",
        "speech": "How do we establish the relative chemical reactivity between two metals that do not react with water or acids decisively? We utilize single displacement reactions in metal salt solutions during laboratory experiments. According to the displacement principle, a more reactive metal displaces a less reactive metal from its aqueous salt solution: metal A plus salt solution of B yields salt solution of A plus displaced metal B. In Activity 3.12, a clean iron nail is suspended inside a test tube containing blue copper(II) sulphate solution, while a clean copper wire is placed inside a second tube containing pale green iron(II) sulphate solution. After twenty minutes, the blue copper sulphate solution gradually fades to pale green iron sulphate, and the iron nail becomes coated with a characteristic reddish-brown deposit of metallic copper. The balanced chemical equation is iron solid plus copper sulphate aqueous yields iron sulphate aqueous plus copper solid. In the second test tube, the copper wire shows no reaction whatsoever in iron sulphate solution. This decisive experimental outcome proves unequivocally that iron is more electropositive and reactive than copper, successfully displacing copper ions from solution while copper lacks the chemical reducing power to displace iron.",
        "content": {
            "concept": "A more reactive metal displaces a less reactive metal from its aqueous salt solution. Iron displaces copper from blue CuSO4 to form pale green FeSO4 and reddish-brown copper deposit. Copper cannot displace iron from FeSO4.",
            "formula": "\\text{Fe}(s) + \\text{CuSO}_4(aq) [\\text{Blue}] \\rightarrow \\text{FeSO}_4(aq) [\\text{Pale Green}] + \\text{Cu}(s) [\\text{Red-Brown}]",
            "points": [
                "Displacement rule: More reactive Metal A + Salt of B → Salt of A + Less reactive Metal B.",
                "Activity 3.12: Iron nail in blue CuSO4 solution turns liquid pale green and deposits copper.",
                "Copper wire in iron sulphate (FeSO4) produces no reaction, confirming Iron > Copper reactivity.",
                "Single displacement provides an empirical basis for assembling the activity series.",
                "Zinc and lead similarly displace copper from its salt solutions due to higher reactivity."
            ]
        },
        "checkpoints": [
            {
                "question": "What visible colour change occurs when an iron nail is immersed in blue copper sulphate solution for twenty minutes?",
                "options": [
                    "The solution turns deep purple and the nail dissolves completely",
                    "The blue solution turns pale green and a reddish-brown coating forms on the nail",
                    "The solution turns milky white and evolves choking chlorine gas",
                    "The solution turns golden yellow with no change to the nail surface"
                ],
                "answer": 1,
                "hint": "Hydrated Fe2+ ions are pale green, and displaced elemental copper is reddish-brown.",
                "explanation": "Iron displaces copper: Fe + CuSO4 (blue) -> FeSO4 (pale green) + Cu. Reddish-brown metallic copper deposits onto the iron nail surface."
            },
            {
                "question": "What observation is recorded when a strip of copper wire is immersed in iron(II) sulphate solution?",
                "options": [
                    "The solution immediately turns deep blue with vigorous bubbling",
                    "A thick layer of black iron oxide coats the copper wire",
                    "No chemical reaction occurs because copper is less reactive than iron",
                    "The copper wire dissolves completely into copper sulphate"
                ],
                "answer": 2,
                "hint": "Check the position of copper relative to iron in the reactivity series.",
                "explanation": "Copper is lower than iron in the reactivity series and cannot displace iron from its salt solution. Therefore, no chemical reaction occurs."
            }
        ]
    },
    {
        "id": 8,
        "title": "Chemical Reactivity Series",
        "subtitle": "Activity Ranking, Hydrogen Reduction Boundary, and Reaction Predictability",
        "speech": "By synthesizing experimental observations from reactions with oxygen, water, acids, and metal salt displacement, chemists assembled the reactivity series, also known as the activity series. The reactivity series is a vertical arrangement of metals in decreasing order of their chemical reactivity. At the pinnacle of the series sit the most reactive alkali and alkaline earth metals: potassium, followed by sodium, calcium, magnesium, and aluminium. These electropositive metals surrender their valence electrons with minimal energy and react vigorously with cold water. In the middle section reside moderately reactive transition and post-transition metals: zinc, iron, and lead. These metals react sluggishly with acids and require steam to oxidize. Non-metal hydrogen is strategically placed in the series as a fundamental chemical benchmark; all metals situated above hydrogen displace hydrogen gas from dilute acids and water, whereas metals positioned below hydrogen cannot displace protons from solution. Below hydrogen sit the least reactive coinage and noble metals: copper, mercury, silver, and gold. Gold occupies the absolute bottom of the activity series as the least reactive element, existing primarily in native uncombined elemental state. Understanding this hierarchy allows us to predict displacement outcomes, extraction metallurgy, and cathodic deposition potentials with precision.",
        "content": {
            "concept": "The reactivity series ranks metals in descending order of chemical reactivity: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au. Metals above hydrogen displace H2 from dilute acids; metals below hydrogen do not.",
            "formula": "\\text{Reactivity: } \\text{K} > \\text{Na} > \\text{Ca} > \\text{Mg} > \\text{Al} > \\text{Zn} > \\text{Fe} > \\text{Pb} > [\\text{H}] > \\text{Cu} > \\text{Hg} > \\text{Ag} > \\text{Au}",
            "points": [
                "Top metals (K, Na, Ca, Mg, Al) are highly electropositive and react with cold water/air readily.",
                "Middle metals (Zn, Fe, Pb) are moderately reactive and react with steam and dilute acids.",
                "Hydrogen serves as an electron-transfer benchmark dividing electropositive metals from noble metals.",
                "Metals above hydrogen displace H2 from acids; metals below hydrogen (Cu, Hg, Ag, Au) cannot.",
                "Gold (Au) sits at the bottom as the least reactive metal, persisting unoxidized in nature."
            ]
        },
        "checkpoints": [
            {
                "question": "Which of the following metals is positioned immediately below hydrogen in the reactivity series and cannot displace hydrogen from dilute hydrochloric acid?",
                "options": [
                    "Zinc (Zn)",
                    "Iron (Fe)",
                    "Lead (Pb)",
                    "Copper (Cu)"
                ],
                "answer": 3,
                "hint": "This coinage metal forms blue solutions and does not react with dilute acids.",
                "explanation": "Copper (Cu) is positioned below hydrogen in the reactivity series. Since it is less reactive than hydrogen, it cannot reduce protons to evolve hydrogen gas from dilute acids."
            },
            {
                "question": "If metal X displaces metal Y from its salt solution, but cannot displace metal Z, what is the correct order of decreasing reactivity?",
                "options": [
                    "X > Y > Z",
                    "Z > X > Y",
                    "Y > X > Z",
                    "Z > Y > X"
                ],
                "answer": 1,
                "hint": "Metal X is more reactive than Y, but less reactive than Z.",
                "explanation": "Since X displaces Y, X is more reactive than Y (X > Y). Since X cannot displace Z, Z is more reactive than X (Z > X). Combining these gives: Z > X > Y."
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

"""Generate Slides 9 to 16 for Class 10 Science Chapter 2: Acids, Bases and Salts
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
        "title": "Exothermic Acid Dilution",
        "subtitle": "Thermodynamics of Mixing, Acid-Into-Water Rule, and Ion Volume Dilution",
        "speech": "When concentrated mineral acids or concentrated alkalis dissolve in water, the process is extraordinarily exothermic, releasing enormous amounts of thermal energy. In Activity 2.10, adding a few drops of concentrated sulphuric acid to ten millilitres of water inside a test tube causes the base of the tube to become remarkably hot. Because hydration releases intense heat, strict laboratory safety protocols must be observed at all times. The concentrated acid must always be added very slowly to a large volume of water with continuous, vigorous stirring. This allows the large heat capacity of water to dissipate hydration enthalpy safely without flash boiling. One must never, under any circumstances, pour water directly into concentrated acid. If water is poured into concentrated acid, the small droplet of water instantaneously boils due to local heat concentration, causing the corrosive acidic mixture to spurt violently outward onto the experimenter's skin and face, potentially fracturing thick glass beakers. The chemical process of dilution involves mixing an acid or base with water, which steadily decreases the concentration of hydronium or hydroxide ions per unit volume. Although total solute quantity remains unchanged, spreading ions across a larger volume decreases both electrical conductivity per unit cross-section and chemical corrosiveness.",
        "content": {
            "concept": "Dissolving concentrated acids or bases in water is highly exothermic. Acid must always be added slowly to water with constant stirring to prevent violent spurting. Dilution reduces the concentration of H3O+ or OH- ions per unit volume.",
            "formula": "\\text{Concentrated Acid} + \\text{Water} \\rightarrow \\text{Dilute Acid} + \\text{Heat} \\quad [\\text{Always Add Acid To Water}]",
            "points": [
                "Activity 2.10: Adding concentrated H2SO4 or NaOH to water releases immense heat.",
                "Mandatory rule: Always add acid slowly to water with constant stirring.",
                "Pouring water into concentrated acid causes localized flash boiling, spurting, and glass fracture.",
                "Dilution decreases the concentration of H3O+ or OH- ions per unit volume of solution.",
                "Diluting an acid lowers its corrosive aggression while increasing total solution volume."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the mandatory laboratory procedure when diluting concentrated sulphuric acid?",
                "options": [
                    "Pour water rapidly into the acid container while cooling on ice",
                    "Add concentrated acid slowly to water with constant stirring",
                    "Mix equal volumes of acid and water simultaneously in a sealed flask",
                    "Heat the concentrated acid gently before adding cold water"
                ],
                "answer": 1,
                "hint": "Water has a high heat capacity and can absorb hydration enthalpy safely if acid is added dropwise.",
                "explanation": "Acid must always be added slowly to water with continuous stirring. If water is added to acid, localized boiling causes dangerous spurting of concentrated corrosive acid."
            },
            {
                "question": "How does the concentration of hydronium ions (H3O+) change when an acidic solution is diluted with water?",
                "options": [
                    "The concentration of H3O+ per unit volume increases sharply",
                    "The concentration of H3O+ per unit volume decreases steadily",
                    "The concentration of H3O+ converts entirely into hydroxide ions",
                    "The concentration remains unchanged regardless of volume added"
                ],
                "answer": 1,
                "hint": "Adding more solvent spreads existing ions across a larger total liquid volume.",
                "explanation": "Dilution increases the total liquid volume without adding new solute, thereby decreasing the number of hydronium ions (H3O+) per unit volume."
            }
        ]
    },
    {
        "id": 10,
        "title": "Universal Indicator Scale",
        "subtitle": "Universal Indicator Spectrum, Logarithmic pH Definition, and Daily Fluid Ranges",
        "speech": "How do we quantitatively determine the relative strength of an acidic or basic solution? We utilize universal indicator, which is a carefully calibrated mixture of organic dyes that displays a continuous spectrum of distinct colours across varying hydrogen ion concentrations. In 1909, the pH scale was introduced to measure hydrogen ion concentration, where p stands for potenz, the German word for power. The pH scale spans from zero to fourteen. A pH of exactly seven represents a completely neutral solution, such as pure distilled water. Values below seven indicate an acidic solution, where lower numbers signify greater hydronium ion concentration and stronger acidity. Values above seven signify a basic or alkaline solution, where higher numbers represent higher hydroxide ion concentrations. Strong acids like hydrochloric acid ionise completely in water, whereas weak acids like acetic acid ionise only partially in solution. The pH value is inversely proportional to hydronium ion concentration. In Activity 2.11, testing everyday liquids reveals fascinating variations: human saliva before meals has a slightly alkaline pH around 7.4, but drops to an acidic 5.8 after meals due to bacterial fermentation. Lemon juice exhibits strong acidity near 2.2, aerated soft drinks around 3.0, black coffee near 5.0, tomato juice around 4.1, while one molar sodium hydroxide reaches a strongly alkaline 14.",
        "content": {
            "concept": "Universal indicator shows distinct colours at different pH values. The pH scale ranges from 0 (strongly acidic) to 14 (strongly basic), with 7 being neutral. The letter p stands for 'potenz' (power). pH is inversely related to hydronium ion concentration.",
            "formula": "\\text{pH} = -\\log_{10}[\\text{H}^+] \\quad | \\quad \\text{Acidic: pH} < 7 \\quad | \\quad \\text{Neutral: pH} = 7 \\quad | \\quad \\text{Basic: pH} > 7",
            "points": [
                "Universal indicator is a mixture of several dyes indicating pH across a continuous colour spectrum.",
                "pH scale: 0 (strongly acidic, red) to 14 (strongly basic, violet), with 7 (neutral, green).",
                "Higher hydronium ion concentration corresponds to a lower numerical pH value.",
                "Strong acids (HCl) completely ionise in water; weak acids (CH3COOH) ionise partially.",
                "Activity 2.11 tests pH: lemon juice ~2.2, saliva 7.4 (before) / 5.8 (after), 1M NaOH ~14."
            ]
        },
        "checkpoints": [
            {
                "question": "If solution A has a pH of 3 and solution B has a pH of 6, which solution possesses a higher concentration of hydrogen ions?",
                "options": [
                    "Solution B has a higher hydrogen ion concentration",
                    "Solution A has a higher hydrogen ion concentration",
                    "Both solutions have identical hydrogen ion concentrations",
                    "Neither solution contains any hydrogen ions"
                ],
                "answer": 1,
                "hint": "The pH scale is inversely related to hydrogen ion concentration: lower numerical pH indicates higher acidity.",
                "explanation": "Because pH is inversely proportional to [H+], solution A with pH 3 contains 1000 times higher hydrogen ion concentration than solution B with pH 6."
            },
            {
                "question": "What is the colour shown by universal indicator in a neutral solution of pH 7?",
                "options": [
                    "Intense dark red",
                    "Brilliant yellow",
                    "Grass green",
                    "Deep royal purple"
                ],
                "answer": 2,
                "hint": "The midpoint of the universal indicator rainbow spectrum corresponds to green.",
                "explanation": "Universal indicator turns red in strong acids, yellow-orange in weak acids, green in neutral solutions (pH 7), and blue-violet in strong bases."
            }
        ]
    },
    {
        "id": 11,
        "title": "Everyday pH Regulation",
        "subtitle": "Biological Homeostasis, Acid Rain Ecological Damage, and Agricultural Soil Testing",
        "speech": "Maintaining strict pH regulation is vital for living organisms and natural ecosystems. The human body functions optimally within an exceptionally narrow physiological pH range of 7.0 to 7.8. Even minor deviations outside this window can impair enzymatic catalysis and cellular metabolism. In atmospheric chemistry, clean rainwater absorbs ambient carbon dioxide, giving it a natural pH near 5.6. However, when industrial emissions release toxic sulphur dioxide and nitrogen oxides, they react with atmospheric moisture to form sulphuric and nitric acids. When rainwater pH drops below 5.6, it is classified as acid rain. As acid rain flows into lakes and rivers, it sharply lowers aquatic pH, leaching toxic aluminium into water bodies and killing fish populations. Beyond Earth, planetary atmospheres exhibit extreme acidity; Venus is completely shrouded by dense, opaque clouds of concentrated sulphuric acid, rendering life impossible. In agriculture, Activity 2.12 emphasizes soil testing: crops require a specific soil pH window, typically between 6.0 and 7.5, for optimal nutrient absorption. Testing soil filtrate with universal indicator paper enables precise determination of agricultural lime requirements. If farm soil becomes excessively acidic due to prolonged fertilizer use or acid precipitation, farmers treat the land by adding quicklime, slaked lime, or chalk to neutralise excess acidity.",
        "content": {
            "concept": "Living organisms function within a narrow pH window of 7.0 to 7.8. Rainwater with pH < 5.6 is acid rain, which severely damages aquatic life. Farmers treat acidic soil with quicklime, slaked lime, or chalk to restore optimal agricultural pH.",
            "formula": "\\text{Acid Rain: pH} < 5.6 \\quad | \\quad \\text{Human Body: pH } 7.0 - 7.8 \\quad | \\quad \\text{Soil Treatment: } \\text{Acid} + \\text{Ca(OH)}_2 \\rightarrow \\text{Neutral}",
            "points": [
                "Human physiological survival requires an extracellular pH range between 7.0 and 7.8.",
                "Rainwater with pH lower than 5.6 is termed acid rain, which endangers aquatic ecosystems.",
                "The atmosphere of planet Venus is composed of thick white and yellowish sulphuric acid clouds.",
                "Activity 2.12: Agricultural soil requires optimal pH; overly acidic soil inhibits crop growth.",
                "Acidic soil is neutralised using basic agricultural amendments: CaO (quicklime), Ca(OH)2, or CaCO3."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the threshold pH value below which precipitation is officially designated as acid rain?",
                "options": [
                    "pH below 7.0",
                    "pH below 5.6",
                    "pH below 4.0",
                    "pH below 2.5"
                ],
                "answer": 1,
                "hint": "Normal unpolluted rain has a pH around 5.6 due to dissolved carbon dioxide forming weak carbonic acid.",
                "explanation": "When pollutants like SO2 and NO2 drive the pH of rainwater below 5.6, it is termed acid rain, which lowers river pH and threatens aquatic fauna."
            },
            {
                "question": "Which basic chemical compound is commonly applied by farmers to treat excessively acidic agricultural soil?",
                "options": [
                    "Concentrated nitric acid",
                    "Ammonium chloride fertilizer",
                    "Slaked lime (calcium hydroxide)",
                    "Sodium chloride rock salt"
                ],
                "answer": 2,
                "hint": "A basic calcium compound like quicklime, slaked lime, or chalk neutralises soil acids.",
                "explanation": "Slaked lime (Ca(OH)2), quicklime (CaO), or chalk (CaCO3) are bases added to acidic soil to raise its pH back to the optimal neutral range for crop growth."
            }
        ]
    },
    {
        "id": 12,
        "title": "Physiological Acid Warfare",
        "subtitle": "Digestive Indigestion, Tooth Enamel Corrosion, and Stinging Plant Formic Acid",
        "speech": "Chemical acid-base interactions play critical roles in human physiology and natural defence mechanisms. In human digestion, the stomach secretes hydrochloric acid, creating an acidic environment with a pH between 1.2 and 2.0 that activates pepsin to break down proteins without harming stomach walls. However, overeating or stress causes hyperacidity, leading to severe heartburn and acute pain. To counter this excess acid, doctors prescribe antacids such as Milk of Magnesia, a mild suspension of magnesium hydroxide, or baking soda, which neutralise excess hydrochloric acid. Inside our mouths, tooth decay begins whenever salivary pH drops below 5.5. Tooth enamel, the hardest crystalline substance in the human body, is composed of calcium hydroxyapatite. When bacteria ferment residual sugar particles between teeth, they produce organic acids that corrode this calcium phosphate lattice. Brushing teeth with alkaline toothpaste neutralises oral acids and prevents caries. In the animal and plant kingdoms, chemical warfare provides defense: honeybee stings inject acidic venom causing acute swelling, which is relieved by applying mild basic baking soda. Similarly, wild nettle leaves possess stinging hairs that inject methanoic acid; rubbing the affected skin with leaves of the dock plant, which grows nearby, provides immediate basic relief through chemical neutralization.",
        "content": {
            "concept": "Stomach HCl aids digestion; excess causes acidity treated with antacids like Mg(OH)2. Tooth enamel corrodes when mouth pH falls below 5.5 due to bacterial acids. Bee stings and nettle hairs inject acidic venom (methanoic acid), neutralised by mild bases or dock leaves.",
            "formula": "\\text{Antacid: } \\text{Mg(OH)}_2 + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + 2\\text{H}_2\\text{O} \\quad | \\quad \\text{Tooth Enamel: } \\text{Corrodes at pH} < 5.5",
            "points": [
                "Stomach produces hydrochloric acid (pH 1.2-2.0); excess acid causes indigestion treated with antacids.",
                "Milk of Magnesia (magnesium hydroxide) is a mild base used as an effective antacid.",
                "Tooth enamel made of calcium hydroxyapatite corrodes when oral pH drops below 5.5.",
                "Toothpastes are mildly basic to neutralise mouth acids and prevent bacterial enamel breakdown.",
                "Bee and nettle stings inject methanoic acid; treated with baking soda and alkaline dock plant leaves."
            ]
        },
        "checkpoints": [
            {
                "question": "At what mouth pH threshold does tooth enamel corrosion and dental decay commence?",
                "options": [
                    "When oral pH falls below 5.5",
                    "When oral pH rises above 7.8",
                    "When oral pH reaches exactly 7.0",
                    "When oral pH drops below 2.0"
                ],
                "answer": 0,
                "hint": "Enamel consists of calcium hydroxyapatite, which dissolves in weak organic acids below this benchmark.",
                "explanation": "Bacterial breakdown of food sugars produces acids in the mouth. When oral pH falls below 5.5, calcium hydroxyapatite enamel begins to demineralise and corrode."
            },
            {
                "question": "Which chemical compound is injected by stinging hairs of nettle leaves, causing burning pain?",
                "options": [
                    "Acetic acid",
                    "Methanoic acid (formic acid)",
                    "Tartaric acid",
                    "Oxalic acid"
                ],
                "answer": 1,
                "hint": "This single-carbon carboxylic acid is also found in ant stings: HCOOH.",
                "explanation": "Nettle leaf hairs inject methanoic acid (HCOOH), causing painful burning stings. Rubbing with alkaline dock plant leaves neutralises the acid."
            }
        ]
    },
    {
        "id": 13,
        "title": "Natural Organic Acids",
        "subtitle": "Naturally Occurring Carboxylic Acids and Cookware Chemical Compatibility",
        "speech": "Nature provides a rich repository of organic carboxylic acids synthesized by plants and animals for biological functions and preservation. Understanding Table 2.3 allows us to trace common acids in culinary and everyday substances. Vinegar contains acetic acid, also known as ethanoic acid, which provides its pungent aroma and antibacterial preservation properties. Citrus fruits like oranges and lemons contain citric acid, delivering their characteristic refreshing sour flavor. Tamarind and unripened grapes contain tartaric acid, which is also incorporated into commercial baking powders to create carbon dioxide bubbles. Ripe tomatoes contain oxalic acid, while sour milk or curd contains lactic acid generated by bacterial fermentation of lactose sugar. Both ant stings and stinging nettle hairs contain methanoic acid, commonly referred to as formic acid. Recognizing these naturally occurring acids explains why traditional culinary wisdom strictly forbids storing sour foods like pickles, curd, or lemon juice in brass or copper vessels in traditional kitchens. The natural organic acids slowly attack the copper and zinc metal lining, synthesizing water-soluble, toxic metallic salts that can cause severe food poisoning when ingested. Conversely, tarnished copper cookware is safely cleaned by rubbing with acidic lemon juice or tamarind paste to dissolve basic patina coatings.",
        "content": {
            "concept": "Natural organic acids are found across various plants and animals: acetic acid in vinegar, citric acid in citrus fruits, tartaric acid in tamarind, oxalic acid in tomatoes, lactic acid in curd, and methanoic acid in ant/nettle stings.",
            "formula": "\\text{Curd: Lactic} \\quad | \\quad \\text{Vinegar: Acetic} \\quad | \\quad \\text{Lemon: Citric} \\quad | \\quad \\text{Tamarind: Tartaric} \\quad | \\quad \\text{Stings: Methanoic}",
            "points": [
                "Vinegar contains acetic acid (CH3COOH); citrus fruits contain citric acid.",
                "Tamarind contains tartaric acid; tomatoes contain oxalic acid.",
                "Sour milk and curd contain lactic acid produced by bacterial lactose fermentation.",
                "Ant stings and nettle stings contain methanoic acid (formic acid, HCOOH).",
                "Sour food substances must not be stored in brass/copper cookware due to toxic salt formation.",
                "Tarnished copper vessels are cleaned by rubbing with acidic lemon or tamarind."
            ]
        },
        "checkpoints": [
            {
                "question": "Which naturally occurring organic acid is present in sour milk and curd?",
                "options": [
                    "Oxalic acid",
                    "Citric acid",
                    "Lactic acid",
                    "Tartaric acid"
                ],
                "answer": 2,
                "hint": "Lactobacillus bacteria ferment lactose sugar into this carboxylic acid.",
                "explanation": "Curd and sour milk contain lactic acid, formed through the microbial conversion of milk sugars by lactic acid bacteria."
            },
            {
                "question": "Why should pickles, curd, and citrus juices never be stored in brass or copper containers?",
                "options": [
                    "The containers absorb the liquids and leak completely",
                    "Acids react with brass and copper to form poisonous soluble metal salts",
                    "The sour taste is neutralised and converted into bitter salt",
                    "Brass precipitates solid gold flakes into the food mixture"
                ],
                "answer": 1,
                "hint": "Acids react with active metals like copper and zinc to liberate harmful chemical salts.",
                "explanation": "Organic acids in sour foods react with copper and zinc in brass/copper vessels to produce toxic metallic salts that lead to chemical food poisoning."
            }
        ]
    },
    {
        "id": 14,
        "title": "Salt Hydrolysis Chemistry",
        "subtitle": "Parent Acid-Base Lineage, Salt Families, and Aqueous Solution pH Categories",
        "speech": "Salts are ionic compounds synthesized through neutralisation reactions between acids and bases, consisting of positive metallic cations and negative acid anions. In Activity 2.13, we classify salts into distinct chemical families based on shared ionic radicals. For example, sodium chloride and sodium sulphate belong to the sodium salt family because they share common sodium cations. Similarly, sodium chloride and potassium chloride belong to the chloride salt family because they share chloride anions. Although salts originate from neutralisation, their aqueous solutions are not always neutral! In Activity 2.14, dissolving diverse salt samples in pure water reveals three fundamental hydrolysis categories depending on the relative strengths of parent reactants. Salts formed from a strong acid and a strong base, such as sodium chloride, do not hydrolyse and yield neutral solutions with a pH of exactly seven. Salts synthesized from a strong acid and a weak base, such as ammonium chloride, undergo cation hydrolysis to yield acidic solutions with a pH below seven. Conversely, salts derived from a strong base and a weak acid, such as sodium carbonate, undergo anion hydrolysis to produce basic solutions with a pH greater than seven. These hydrolysis equilibria illustrate how constituent ions interact dynamically with water molecules.",
        "content": {
            "concept": "Salts sharing common cations or anions belong to the same family. Strong acid + Strong base yields a neutral salt (pH = 7). Strong acid + Weak base yields an acidic salt (pH < 7). Strong base + Weak acid yields a basic salt (pH > 7).",
            "formula": "\\text{Strong Acid} + \\text{Strong Base} \\rightarrow \\text{pH} = 7 \\quad | \\quad \\text{Strong Acid} + \\text{Weak Base} \\rightarrow \\text{pH} < 7 \\quad | \\quad \\text{Weak Acid} + \\text{Strong Base} \\rightarrow \\text{pH} > 7",
            "points": [
                "Salts having common positive or negative radicals belong to a family (e.g., sodium or chloride family).",
                "Strong Acid + Strong Base (e.g., NaCl, KNO3) → Neutral solution (pH = 7).",
                "Strong Acid + Weak Base (e.g., NH4Cl, CuSO4) → Acidic solution (pH < 7).",
                "Weak Acid + Strong Base (e.g., CH3COONa, Na2CO3) → Basic solution (pH > 7).",
                "Salt hydrolysis occurs when constituent ions react with water to shift hydronium/hydroxide balance."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the expected pH range of an aqueous solution of ammonium chloride (NH4Cl)?",
                "options": [
                    "pH is strictly greater than 7 (basic)",
                    "pH is strictly less than 7 (acidic)",
                    "pH is exactly equal to 7 (neutral)",
                    "pH is equal to 14 (strongly alkaline)"
                ],
                "answer": 1,
                "hint": "Identify the parent acid (strong HCl) and parent base (weak NH4OH) forming this salt.",
                "explanation": "Ammonium chloride is formed from strong hydrochloric acid and weak ammonium hydroxide. The resulting salt undergoes cation hydrolysis, making the aqueous solution acidic with pH < 7."
            },
            {
                "question": "Which combination of parent acid and parent base produces a basic salt with a pH greater than 7?",
                "options": [
                    "Strong acid and strong base",
                    "Strong acid and weak base",
                    "Weak acid and strong base",
                    "Weak acid and weak base"
                ],
                "answer": 2,
                "hint": "The stronger parent reactant dominates the final aqueous pH of the salt solution.",
                "explanation": "When a weak acid (e.g., carbonic acid) reacts with a strong base (e.g., sodium hydroxide), the resulting salt (Na2CO3) produces an alkaline solution with pH > 7 via anion hydrolysis."
            }
        ]
    },
    {
        "id": 15,
        "title": "Chlor-Alkali Industrial Process",
        "subtitle": "Brine Electrolysis, Anodic Chlorine, Cathodic Hydrogen, and Sodium Hydroxide",
        "speech": "Common salt, sodium chloride, is far more than a kitchen seasoning; it serves as the foundational industrial raw material for manufacturing vital chemical commodities. Mined from massive underground rock salt deposits formed when ancient inland seas dried up, common salt carries deep historic significance, exemplified by Mahatma Gandhi's famous Dandi March. In the chlor-alkali process, a concentrated aqueous solution of sodium chloride, known industrially as brine, undergoes electrical decomposition in an electrolytic membrane cell. When electric current passes through brine, water and salt molecules dissociate into their constituent chemical elements. Chlorine gas is liberated at the positive anode, while hydrogen gas is evolved at the negative cathode. Simultaneously, sodium hydroxide solution forms in the liquid compartment near the cathode. The balanced industrial equation is two sodium chloride aqueous plus two water liquid yields two sodium hydroxide aqueous plus chlorine gas plus hydrogen gas. Each of these three co-products possesses immense industrial utility: chlorine gas is utilized for water disinfection, PVC manufacturing, and CFC production; hydrogen gas serves as a rocket fuel, margarine hydrogenator, and ammonia feedstock for agricultural fertilizers; sodium hydroxide is critical for metal degreasing, soap manufacturing, and paper production in commercial mills and textile factories.",
        "content": {
            "concept": "The chlor-alkali process electrolyses aqueous brine (NaCl solution) to yield chlorine gas at the anode, hydrogen gas at the cathode, and sodium hydroxide near the cathode. All three co-products are critical industrial chemicals.",
            "formula": "2\\text{NaCl}(aq) + 2\\text{H}_2\\text{O}(l) \\xrightarrow{\\text{Electricity}} 2\\text{NaOH}(aq) + \\text{Cl}_2(g)\\uparrow [\\text{Anode}] + \\text{H}_2(g)\\uparrow [\\text{Cathode}]",
            "points": [
                "Common salt (NaCl) is obtained from seawater evaporation or mining ancient brown rock salt.",
                "Chlor-alkali process electrolyses concentrated aqueous NaCl (brine).",
                "Chlorine gas (Cl2) is collected at the anode (used in PVC, water purification, disinfectants).",
                "Hydrogen gas (H2) is collected at the cathode (used in clean fuels, margarine, ammonia synthesis).",
                "Sodium hydroxide (NaOH) forms near the cathode (used in soaps, detergents, degreasing, papermaking)."
            ]
        },
        "checkpoints": [
            {
                "question": "At which electrode is chlorine gas evolved during the industrial chlor-alkali electrolysis of brine?",
                "options": [
                    "At the negative cathode",
                    "At the positive anode",
                    "At both electrodes equally",
                    "In the liquid electrolyte center"
                ],
                "answer": 1,
                "hint": "Chloride anions carry negative charge and migrate toward the positive electrode where they undergo oxidation.",
                "explanation": "Chloride ions (Cl-) lose electrons at the positive anode, oxidising into greenish-yellow chlorine gas: 2Cl- -> Cl2 + 2e-."
            },
            {
                "question": "What are the primary commercial applications of sodium hydroxide produced in the chlor-alkali process?",
                "options": [
                    "Water chlorination and swimming pool bleaching",
                    "Rocket propellants and margarine hydrogenation",
                    "Soap manufacturing, paper pulp processing, and metal degreasing",
                    "Agricultural nitrogen fixation in soil"
                ],
                "answer": 2,
                "hint": "NaOH is a strong alkali widely used to saponify fatty acids and break down cellulose.",
                "explanation": "Sodium hydroxide is an indispensable industrial alkali used extensively in saponification for soaps and detergents, degreasing machinery metals, and chemical wood pulp refining in paper mills."
            }
        ]
    },
    {
        "id": 16,
        "title": "Commercial Salt Derivatives",
        "subtitle": "Bleaching Powder, Baking Soda, Washing Soda, and Plaster of Paris",
        "speech": "Common salt and chlor-alkali products enable the synthesis of four major commercial chemical derivatives. First, bleaching powder, calcium oxychloride, is manufactured by treating dry slaked lime with chlorine gas: calcium hydroxide plus chlorine yields calcium oxychloride plus water. It serves as a textile bleach, chemical oxidizer, and germicidal water disinfectant. Second, baking soda, sodium hydrogencarbonate, is produced via the Solvay process from brine, carbon dioxide, ammonia, and water. Heating baking soda during cooking decomposes it into sodium carbonate, water, and carbon dioxide gas, which causes cakes and breads to rise soft and spongy. Baking powder contains baking soda mixed with mild edible tartaric acid to prevent a bitter metallic taste. Third, washing soda, sodium carbonate decahydrate, is produced by recrystallising sodium carbonate with ten water molecules: sodium carbonate plus ten water yields sodium carbonate decahydrate. It is essential in glass, soap, and paper industries, and removes permanent water hardness. Finally, salts contain water of crystallisation—a fixed number of water molecules in their crystal lattice. Heating blue hydrated copper sulphate drives off five water molecules, leaving white anhydrous powder. Heating gypsum at 373 Kelvin produces Plaster of Paris, calcium sulphate hemihydrate, used for setting fractured bones and sculpting.",
        "content": {
            "concept": "Commercial salt derivatives: Bleaching powder (CaOCl2) from chlorine and slaked lime. Baking soda (NaHCO3) releases CO2 on heating; mixed with tartaric acid it forms baking powder. Washing soda (Na2CO3·10H2O) softens hard water. Plaster of Paris (CaSO4·1/2H2O) forms gypsum upon hydration.",
            "formula": "\\text{Ca(OH)}_2 + \\text{Cl}_2 \\rightarrow \\text{CaOCl}_2 + \\text{H}_2\\text{O} \\quad | \\quad \\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O} \\xrightarrow{373\\text{ K}} \\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O}",
            "points": [
                "Bleaching powder (CaOCl2): Ca(OH)2 + Cl2 → CaOCl2 + H2O (disinfectant and textile bleach).",
                "Baking soda (NaHCO3): 2NaHCO3 + Heat → Na2CO3 + H2O + CO2 (baking, antacid, fire extinguishers).",
                "Baking powder is a mixture of baking soda and mild edible tartaric acid.",
                "Washing soda (Na2CO3·10H2O): Removes permanent hardness of water and manufactures borax.",
                "Water of crystallisation: Fixed water molecules per formula unit (CuSO4·5H2O, FeSO4·7H2O).",
                "Plaster of Paris (CaSO4·1/2H2O): Obtained by heating gypsum at 373 K; sets hard with water."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the chemical identity and formula of Plaster of Paris?",
                "options": [
                    "Calcium sulphate dihydrate (CaSO4·2H2O)",
                    "Calcium sulphate hemihydrate (CaSO4·1/2H2O)",
                    "Calcium carbonate decahydrate (CaCO3·10H2O)",
                    "Calcium chloride hexahydrate (CaCl2·6H2O)"
                ],
                "answer": 1,
                "hint": "Heating gypsum removes three-quarters of its structural water, leaving half a water molecule per formula unit.",
                "explanation": "Plaster of Paris is calcium sulphate hemihydrate, CaSO4·1/2H2O, produced by heating gypsum (CaSO4·2H2O) carefully at 373 K (100°C)."
            },
            {
                "question": "Why is mild edible tartaric acid added to baking soda to formulate commercial baking powder?",
                "options": [
                    "To prevent baking soda from dissolving in liquid cake batter",
                    "To neutralise alkaline sodium carbonate formed on heating and eliminate its bitter taste",
                    "To turn the cake mixture bright yellow for decoration",
                    "To double the shelf life of the baking powder container"
                ],
                "answer": 1,
                "hint": "Thermal decomposition of NaHCO3 yields basic Na2CO3, which tastes bitter unless neutralised.",
                "explanation": "When baking soda is heated, basic Na2CO3 is produced. Tartaric acid reacts with this sodium carbonate to form neutral sodium tartrate, eliminating bitterness while producing additional CO2."
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

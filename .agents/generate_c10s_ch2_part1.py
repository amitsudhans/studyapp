"""Generate Slides 1 to 8 for Class 10 Science Chapter 2: Acids, Bases and Salts
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
        "title": "Natural Chemical Indicators",
        "subtitle": "Daily Food Tastes, Lichen Litmus Dye, Turmeric and Natural Flower Extracts",
        "speech": "Welcome to our laboratory exploration of acids, bases, and salts. In our daily lives, we encounter acids in sour citrus fruits and curd, while bases taste characteristically bitter and feel soapy to touch. When someone suffers from excess stomach acidity after overeating, a mild baking soda solution serves as an effective remedy by neutralising the acid, whereas lemon juice or vinegar would aggravate the condition. Chemical substances known as indicators allow us to identify acidic and basic solutions through clear colour transitions. Litmus is a widely used natural indicator extracted from lichens belonging to the plant division Thallophyta. In a neutral solution, litmus dye displays a distinct purple hue. Acidic media turn blue litmus paper red, whereas alkaline or basic solutions turn red litmus paper blue. Common kitchen turmeric acts as another sensitive natural indicator; a curry stain turns reddish-brown when scrubbed with alkaline soap, returning to yellow upon thorough rinsing with water. Other natural indicators include red cabbage leaves and colourful flower petals of Hydrangea, Petunia, and Geranium. If provided with only red litmus paper, dipping it into three unknown test tubes identifies the basic solution first by turning blue, which subsequently detects the acidic solution.",
        "content": {
            "concept": "Acids taste sour and turn blue litmus red. Bases taste bitter, feel slippery, and turn red litmus blue. Natural indicators derived from lichens, turmeric, and flowering plants provide visible colour indicators without requiring synthetic chemicals.",
            "formula": "\\text{Acid: Blue Litmus} \\rightarrow \\text{Red} \\quad | \\quad \\text{Base: Red Litmus} \\rightarrow \\text{Blue}",
            "points": [
                "Litmus dye is extracted from lichens (Thallophyta) and shows a neutral purple colour.",
                "Acids turn blue litmus red; bases turn red litmus blue.",
                "Turmeric turns reddish-brown in alkaline soap solutions and restores yellow with water.",
                "Natural indicators include red cabbage leaves and petals of Hydrangea, Petunia, and Geranium.",
                "A single strip of red litmus distinguishes distilled water, acid, and base sequentially."
            ]
        },
        "checkpoints": [
            {
                "question": "What happens when alkaline soap solution touches a yellow turmeric stain on white cloth?",
                "options": [
                    "The stain immediately bleaches completely white",
                    "The stain turns a deep reddish-brown colour",
                    "The stain turns bright green with effervescence",
                    "The stain remains unchanged yellow without reaction"
                ],
                "answer": 1,
                "hint": "Turmeric is a natural indicator that reacts selectively with alkaline compounds like sodium carboxylates in soap.",
                "explanation": "Turmeric contains curcumin which turns reddish-brown in basic or alkaline conditions. Washing with water removes the base and restores the original yellow colour."
            },
            {
                "question": "From which division of organisms is natural litmus dye extracted?",
                "options": [
                    "Bryophyta mosses",
                    "Pteridophyta ferns",
                    "Thallophyta lichens",
                    "Gymnosperm conifers"
                ],
                "answer": 2,
                "hint": "Litmus is derived from a symbiotic association of algae and fungi belonging to primitive thallus plants.",
                "explanation": "Litmus is a water-soluble dye extracted from lichens, which belong to the plant division Thallophyta. In neutral water, it retains a characteristic purple colour."
            }
        ]
    },
    {
        "id": 2,
        "title": "Laboratory Indicator Testing",
        "subtitle": "Synthetic pH Indicators and Sensory Olfactory Testing in Acids and Bases",
        "speech": "In standard chemical laboratories, we employ both synthetic chemical indicators and olfactory indicators to systematically test acidic and basic solutions through careful visual inspection. Common mineral acids including hydrochloric acid, sulphuric acid, and nitric acid, alongside organic acetic acid, produce uniform diagnostic responses across indicators. Similarly, common laboratory bases such as sodium hydroxide, calcium hydroxide, potassium hydroxide, magnesium hydroxide, and ammonium hydroxide produce reciprocal alkaline colorations. When tested on a spot plate or watch glass, acidic droplets turn blue litmus red while leaving red litmus unchanged. In stark contrast, basic drops turn red litmus blue while leaving blue litmus unaffected. Synthetic phenolphthalein serves as an exceptional indicator; it remains completely colourless in acidic and neutral media, but develops an intense magenta-pink hue in basic solutions containing hydroxide ions. Synthetic methyl orange exhibits the opposite spectrum, turning vibrant red in acidic solutions and brilliant yellow in basic environments. For visually impaired researchers or specialized olfactory assays, olfactory indicators detect chemical acidity and basicity through distinctive changes in scent. Distinct aromas of finely chopped onions, vanilla essence, and clove oil persist prominently in acidic solutions, but their characteristic smells are entirely destroyed when exposed to strong bases like sodium hydroxide.",
        "content": {
            "concept": "Laboratory indicators enable systematic chemical classification. Phenolphthalein turns bright pink in bases and stays colourless in acids. Methyl orange turns red in acids and yellow in bases. Olfactory indicators like onion, vanilla, and clove lose their distinct odour in basic media.",
            "formula": "\\text{Phenolphthalein: Acid (Colourless)} \\leftrightarrow \\text{Base (Pink)} \\quad | \\quad \\text{Methyl Orange: Acid (Red)} \\leftrightarrow \\text{Base (Yellow)}",
            "points": [
                "Common laboratory acids: HCl, H2SO4, HNO3, and CH3COOH.",
                "Common laboratory bases: NaOH, Ca(OH)2, KOH, Mg(OH)2, and NH4OH.",
                "Phenolphthalein is colourless in acidic medium and turns pink in alkaline medium.",
                "Methyl orange exhibits a sharp red colour in acids and turns yellow in bases.",
                "Olfactory indicators (onion, vanilla essence, clove oil) retain aroma in acids but lose it in bases."
            ]
        },
        "checkpoints": [
            {
                "question": "Which visual colour change occurs when phenolphthalein is added to sodium hydroxide solution?",
                "options": [
                    "The solution turns deep red",
                    "The solution turns intense magenta-pink",
                    "The solution turns bright yellow",
                    "The solution remains completely colourless"
                ],
                "answer": 1,
                "hint": "Phenolphthalein is an organic indicator that develops a vivid pink conjugate structure in alkaline environments.",
                "explanation": "In basic solutions containing hydroxide ions such as NaOH, phenolphthalein dissociates to form a pink anion. In acidic or neutral solutions, it remains non-ionised and colourless."
            },
            {
                "question": "How do olfactory indicators such as vanilla essence behave in basic solutions?",
                "options": [
                    "Their aroma intensifies significantly",
                    "Their distinct scent is completely eliminated",
                    "Their smell converts into an ester fruit aroma",
                    "Their odour remains entirely unaffected"
                ],
                "answer": 1,
                "hint": "Basic media react chemically with aromatic volatile aldehydes, destroying their characteristic odour.",
                "explanation": "Olfactory indicators such as onion extract, vanilla essence, and clove oil lose their characteristic smell when treated with a base like dilute NaOH, but retain their aroma in acidic media."
            }
        ]
    },
    {
        "id": 3,
        "title": "Acids Reacting Metals",
        "subtitle": "Hydrogen Gas Evolution, Soap Bubble Pop Test, and Amphoteric Zinc Reactions",
        "speech": "When active metals react with dilute acids, electropositive metal atoms displace hydrogen atoms, releasing hydrogen gas while forming an ionic metal salt. In Activity 2.3, placing granulated zinc into dilute sulphuric acid inside a boiling tube triggers vigorous effervescence as bubbling streams of gas emerge continuously. The generated gas travels through a glass delivery tube into a trough filled with liquid soap solution. Soap bubbles filled with light hydrogen gas form rapidly and rise toward the surface. When a burning candle or wooden splinter is brought near a floating bubble, the trapped hydrogen gas ignites with a sharp, characteristic popping sound, confirming its chemical identity unequivocally. The balanced chemical equation is zinc solid plus sulphuric acid aqueous yields zinc sulphate aqueous plus hydrogen gas. Interestingly, certain amphoteric metals like zinc can also react with strong bases upon gentle heating. In Activity 2.4, warming granulated zinc with concentrated sodium hydroxide solution releases hydrogen gas along with the formation of water-soluble sodium zincate. The balanced equation is two sodium hydroxide plus zinc yields sodium zincate plus hydrogen gas. However, such hydrogen displacement reactions do not occur uniformly with all metals, as only specific amphoteric elements can liberate hydrogen from alkaline solutions.",
        "content": {
            "concept": "Acids react with active metals to liberate hydrogen gas and form metal salts. Amphoteric metals such as zinc also react with concentrated alkalis upon heating to release hydrogen gas and form zincate salts.",
            "formula": "\\text{Zn}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{H}_2(g)\\uparrow \\quad | \\quad 2\\text{NaOH}(aq) + \\text{Zn}(s) \\xrightarrow{\\Delta} \\text{Na}_2\\text{ZnO}_2(aq) + \\text{H}_2(g)\\uparrow",
            "points": [
                "Acid + Metal → Salt + Hydrogen gas.",
                "Passing evolved gas through soap solution creates floating gas-filled bubbles.",
                "Hydrogen burns with a characteristic pop sound when ignited with a burning splint.",
                "Granulated zinc reacts with hot sodium hydroxide to produce sodium zincate (Na2ZnO2) and H2.",
                "Hydrogen displacement from bases occurs only with specific amphoteric metals like zinc and aluminium."
            ]
        },
        "checkpoints": [
            {
                "question": "Which diagnostic laboratory test definitively confirms the presence of hydrogen gas?",
                "options": [
                    "Turning lime water milky white",
                    "Rekindling a glowing wooden splinter",
                    "Burning with a characteristic popping sound",
                    "Turning moist red litmus paper deep blue"
                ],
                "answer": 2,
                "hint": "Hydrogen gas is combustible and reacts explosively on a miniature scale when mixed with atmospheric oxygen.",
                "explanation": "Hydrogen gas burns rapidly with atmospheric oxygen near an open flame, producing a rapid miniature shockwave known as a characteristic 'pop' sound."
            },
            {
                "question": "What are the reaction products when zinc metal is heated with sodium hydroxide solution?",
                "options": [
                    "Zinc oxide, water, and oxygen gas",
                    "Sodium zincate and hydrogen gas",
                    "Sodium hydride and zinc hydroxide",
                    "Zinc carbonate and sodium oxide"
                ],
                "answer": 1,
                "hint": "The formula of sodium zincate is Na2ZnO2, where zinc is integrated into the complex zincate anion.",
                "explanation": "Granulated zinc reacts with hot NaOH via: 2NaOH + Zn -> Na2ZnO2 + H2. Sodium zincate (Na2ZnO2) and hydrogen gas are formed."
            }
        ]
    },
    {
        "id": 4,
        "title": "Carbonates Acid Reactions",
        "subtitle": "Effervescence of Carbon Dioxide, Lime Water Milkiness, and Soluble Bicarbonates",
        "speech": "When acids react with metal carbonates or metal hydrogencarbonates, they decompose them vigorously to produce an ionic salt, liquid water, and carbon dioxide gas with rapid effervescence. In Activity 2.5, treating solid sodium carbonate or sodium hydrogencarbonate with dilute hydrochloric acid inside a test tube releases continuous streams of carbon dioxide gas bubbles. To verify this gas systematically, it is channeled through freshly prepared lime water, which is a clear aqueous solution of calcium hydroxide. The carbon dioxide reacts with calcium hydroxide to form an insoluble white precipitate of calcium carbonate, turning the lime water visibly cloudy and milky. The balanced equation is calcium hydroxide plus carbon dioxide yields calcium carbonate precipitate plus water. If excess carbon dioxide gas is continuously bubbled through this milky suspension, the white precipitate completely dissolves, rendering the solution transparent once again. This complete clearing occurs because insoluble calcium carbonate converts into water-soluble calcium hydrogencarbonate. Common natural substances like limestone, chalk, marble, and sea shells are diverse physical forms of calcium carbonate. Storing acidic food items such as curd, vinegar, or citrus juices in brass or copper vessels is strictly avoided because acids react with copper and zinc to synthesize toxic metal salts.",
        "content": {
            "concept": "Metal carbonates and hydrogencarbonates react with acids to yield salts, carbon dioxide gas, and water. Carbon dioxide turns lime water milky due to calcium carbonate formation, which dissolves in excess CO2 as soluble calcium hydrogencarbonate.",
            "formula": "\\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\rightarrow 2\\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow \\quad | \\quad \\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}",
            "points": [
                "Metal carbonate/hydrogencarbonate + Acid → Salt + Carbon dioxide + Water.",
                "Carbon dioxide gas turns clear lime water (Ca(OH)2) milky due to insoluble CaCO3 precipitate.",
                "Passing excess CO2 dissolves the milkiness: CaCO3 + H2O + CO2 → Ca(HCO3)2 (soluble).",
                "Limestone, chalk, marble, and sea shells are distinct physical forms of calcium carbonate.",
                "Sour food substances must not be stored in brass or copper vessels to avoid forming toxic salts."
            ]
        },
        "checkpoints": [
            {
                "question": "Why does lime water turn milky when carbon dioxide gas is passed through it?",
                "options": [
                    "Formation of water-soluble calcium chloride",
                    "Precipitation of insoluble white calcium carbonate",
                    "Dissolution of calcium oxide into hydroxide",
                    "Evolution of dense white steam bubbles"
                ],
                "answer": 1,
                "hint": "Calcium hydroxide reacts with carbon dioxide to yield an insoluble white mineral precipitate.",
                "explanation": "The reaction Ca(OH)2 + CO2 -> CaCO3 (insoluble white precipitate) + H2O causes the characteristic milky suspension in lime water."
            },
            {
                "question": "What chemical compound causes the milky lime water to turn clear again upon adding excess carbon dioxide?",
                "options": [
                    "Solid calcium oxide",
                    "Soluble calcium hydrogencarbonate",
                    "Insoluble calcium sulphate",
                    "Precipitated calcium chloride"
                ],
                "answer": 1,
                "hint": "The chemical formula of this soluble salt is Ca(HCO3)2.",
                "explanation": "Passing excess CO2 through the suspension converts insoluble CaCO3 into water-soluble calcium hydrogencarbonate: CaCO3 + H2O + CO2 -> Ca(HCO3)2, restoring a clear solution."
            }
        ]
    },
    {
        "id": 5,
        "title": "Acid Base Neutralisation",
        "subtitle": "Titration Endpoint, Mutual Effect Cancellation, and Salt Plus Water Synthesis",
        "speech": "When an acid and a base are mixed together in exact stoichiometric proportions, their opposing chemical properties cancel each other out completely, producing an ionic salt and neutral water. This mutual nullification is formally defined as a neutralisation reaction. In Activity 2.6, we place approximately two millilitres of dilute sodium hydroxide solution into a conical flask and add two drops of phenolphthalein indicator, yielding an intense pink alkaline solution. Using a calibrated burette or dropper, dilute hydrochloric acid is carefully added drop by drop while gently swirling the flask continuously. As acid molecules introduce hydronium ions that progressively consume hydroxide ions, the basicity decreases steadily throughout the titration. At the exact neutralisation endpoint, a single final drop of acid completely discharges the pink colour, turning the solution totally transparent and neutral. If we subsequently add a few drops of sodium hydroxide, hydroxide ions regain dominance and the vibrant pink coloration reappears instantly. The fundamental chemical mechanism of neutralisation involves hydrogen ions from the acid combining with hydroxide ions from the base to synthesize neutral covalent water molecules, accompanied by the formation of dissolved sodium chloride salt in aqueous solution. This classic experiment highlights the exact stoichiometric equivalence ratio of hydronium and hydroxide ions.",
        "content": {
            "concept": "Neutralisation is the reaction between an acid and a base to form salt and water. Hydrogen ions from the acid combine with hydroxide ions from the base to produce stable water molecules, while spectator ions form a salt.",
            "formula": "\\text{Base} + \\text{Acid} \\rightarrow \\text{Salt} + \\text{Water} \\quad \\implies \\quad \\text{H}^+(aq) + \\text{OH}^-(aq) \\rightarrow \\text{H}_2\\text{O}(l)",
            "points": [
                "Neutralisation: Acid + Base → Salt + Water.",
                "Activity 2.6 demonstrates titration of NaOH against dilute HCl using phenolphthalein.",
                "Phenolphthalein turns from pink to colourless at the exact neutralisation equivalence point.",
                "Re-adding base restores the alkaline pink coloration, confirming reversible indicator behavior.",
                "The core net ionic reaction is the combination of H+ and OH- ions into water molecules."
            ]
        },
        "checkpoints": [
            {
                "question": "What is the net ionic equation representing all aqueous acid-base neutralisation reactions?",
                "options": [
                    "Na+(aq) + Cl-(aq) -> NaCl(s)",
                    "H+(aq) + OH-(aq) -> H2O(l)",
                    "2H+(aq) + O2-(aq) -> H2O(l)",
                    "H2(g) + O2(g) -> 2H2O(l)"
                ],
                "answer": 1,
                "hint": "The spectator metal and halide ions remain dissolved while hydronium and hydroxide cancel each other.",
                "explanation": "In any aqueous neutralisation between strong acids and bases, the essential net reaction is H+(aq) + OH-(aq) -> H2O(l), forming neutral liquid water."
            },
            {
                "question": "In Activity 2.6, what indicates that sodium hydroxide has been completely neutralised by hydrochloric acid?",
                "options": [
                    "Vigorous evolution of gas bubbles",
                    "Formation of an insoluble yellow precipitate",
                    "Disappearance of the pink phenolphthalein colour",
                    "A sudden boiling of the aqueous mixture"
                ],
                "answer": 2,
                "hint": "Phenolphthalein requires alkaline hydroxide ions to remain pink; neutral and acidic media turn it colourless.",
                "explanation": "When all OH- ions are neutralised by added H+ ions, the solution ceases to be basic, causing the pink phenolphthalein colour to disappear completely."
            }
        ]
    },
    {
        "id": 6,
        "title": "Oxides Acid Reactions",
        "subtitle": "Basic Nature of Metallic Oxides and Acidic Nature of Non-Metallic Oxides",
        "speech": "We can determine the fundamental chemical nature of metallic and non-metallic oxides by examining how they interact with acids and bases in systematic laboratory experiments. In Activity 2.7, a small quantity of black copper(II) oxide powder is placed in a beaker and treated with dilute hydrochloric acid while stirring continuously with a glass rod. Gradually, the black solid dissolves completely, transforming the suspension into a captivating clear blue-green liquid under standard ambient conditions. This distinct colour change is caused by the synthesis of dissolved copper(II) chloride salt and water. The balanced chemical equation is copper oxide solid plus two hydrochloric acid aqueous yields copper chloride aqueous plus water. Because metallic oxides react with acids to produce salt and water alone, metallic oxides are categorized as basic oxides. Conversely, non-metallic oxides exhibit pronounced acidic properties in chemical reactions. When carbon dioxide, a non-metallic oxide, reacts with calcium hydroxide, which is a basic solution of lime water, they produce calcium carbonate salt and water. This identical neutralization pattern demonstrates that non-metallic oxides behave as acidic oxides. Understanding these oxide classifications explains why sour acidic foods react destructively with metal cookware and why industrial carbon emissions generate acid rain in nature.",
        "content": {
            "concept": "Metallic oxides react with acids to yield salt and water, establishing that metallic oxides are basic in nature. Non-metallic oxides react with bases to yield salt and water, demonstrating their acidic nature.",
            "formula": "\\text{CuO}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{CuCl}_2(aq) [\\text{Blue-Green}] + \\text{H}_2\\text{O}(l) \\quad | \\quad \\text{CO}_2(g) + \\text{Ca(OH)}_2(aq) \\rightarrow \\text{CaCO}_3(s) + \\text{H}_2\\text{O}(l)",
            "points": [
                "Metallic oxide + Acid → Salt + Water (Metal oxides are basic).",
                "Black CuO dissolves in HCl to form a clear blue-green solution of CuCl2.",
                "Non-metallic oxide + Base → Salt + Water (Non-metal oxides are acidic).",
                "Carbon dioxide reacting with calcium hydroxide confirms the acidic character of non-metal oxides.",
                "Acidic food storage in copper or brass pots leads to toxic metallic salt synthesis."
            ]
        },
        "checkpoints": [
            {
                "question": "What causes the black copper oxide suspension to turn into a blue-green solution when mixed with hydrochloric acid?",
                "options": [
                    "Formation of dissolved copper(II) chloride",
                    "Evolution of greenish-yellow chlorine gas",
                    "Formation of copper carbonate precipitate",
                    "Dissolution of metallic copper flakes"
                ],
                "answer": 0,
                "hint": "The reaction produces a hydrated divalent transition metal chloride salt: CuCl2.",
                "explanation": "Black CuO reacts with dilute HCl via: CuO + 2HCl -> CuCl2 + H2O. The resulting hydrated Cu2+ ions impart a characteristic blue-green colour to the aqueous solution."
            },
            {
                "question": "What fundamental chemical property is established by the reaction of carbon dioxide with calcium hydroxide?",
                "options": [
                    "Carbon dioxide is an amphoteric neutral oxide",
                    "Non-metallic oxides are acidic in character",
                    "Metallic oxides are strictly neutral compounds",
                    "Calcium hydroxide behaves as a powerful acid"
                ],
                "answer": 1,
                "hint": "A substance that reacts with a base to form salt and water acts as an acid.",
                "explanation": "Because non-metallic CO2 reacts with the base Ca(OH)2 to produce salt (CaCO3) and water, non-metallic oxides are classified as acidic oxides."
            }
        ]
    },
    {
        "id": 7,
        "title": "Electrolytic Ion Conduction",
        "subtitle": "Circuit Conduction, Acidic Ion Dissociation, and Organic Molecule Resistance",
        "speech": "What fundamental property do all acids and all bases have in common? In Activity 2.8, we construct an electrical testing circuit containing a six-volt battery, a light bulb, a switch, and two iron nails fixed onto a rubber cork placed inside a glass beaker. When dilute hydrochloric acid or dilute sulphuric acid is poured into the beaker and the circuit switch is closed, the electric bulb immediately glows brightly and steadily. Current flows smoothly through the solution because dissolved mineral acids dissociate completely into mobile positively charged hydrogen cations and corresponding negatively charged anions. Under this electric field, cations migrate toward the negative cathode while anions travel toward the positive anode. These mobile ions act as microscopic charge carriers traversing across the liquid gap between the iron electrodes under applied electrical voltage. In sharp contrast, when the identical experiment is repeated using aqueous solutions of glucose or ethyl alcohol, the electric bulb does not glow at all. Even though glucose and alcohol molecules contain numerous hydrogen atoms in their chemical formulas, their covalent bonds do not ionise in water to generate free hydrogen ions. This crucial distinction proves that acidic behavior and electrical conductivity strictly require the active generation of mobile ions in aqueous solution.",
        "content": {
            "concept": "Aqueous acids conduct electricity because they dissociate into free mobile cations (H+/H3O+) and anions that carry electric current. Covalent organic compounds like glucose and alcohol contain hydrogen but do not ionise, failing to conduct current.",
            "formula": "\\text{HCl}(aq) \\rightarrow \\text{H}^+(aq) + \\text{Cl}^-(aq) \\quad | \\quad \\text{Glucose/Alcohol} \\xrightarrow{\\text{H}_2\\text{O}} \\text{No Free Ions (No Glow)}",
            "points": [
                "Activity 2.8 tests electrical conductivity using a 6V battery, bulb, and iron electrodes.",
                "Dilute HCl and H2SO4 solutions cause the bulb to glow brightly due to mobile ions.",
                "Electric current in electrolytic solutions is carried by mobile cations and anions.",
                "Aqueous solutions of glucose (C6H12O6) and ethyl alcohol (C2H5OH) do not conduct electricity.",
                "Possessing hydrogen atoms in a molecular formula does not automatically make a compound an acid."
            ]
        },
        "checkpoints": [
            {
                "question": "Why does an electric bulb glow when connected across an aqueous solution of hydrochloric acid?",
                "options": [
                    "Free electrons migrate directly through the acidic water",
                    "Dissociated hydrogen and chloride ions carry electric charge",
                    "Hydrochloric acid converts into molten conducting metal",
                    "Water decomposes into explosive hydrogen gas bubbles"
                ],
                "answer": 1,
                "hint": "Electrical conduction in electrolytic solutions requires mobile charged particles: ions.",
                "explanation": "HCl dissociates completely in water into H+(aq) and Cl-(aq) ions. These mobile ions migrate toward oppositely charged electrodes, carrying electric current and lighting the bulb."
            },
            {
                "question": "Why does an aqueous glucose solution fail to conduct electric current despite containing hydrogen atoms?",
                "options": [
                    "Glucose molecules do not dissociate to form free ions in water",
                    "Glucose reacts violently with the iron electrodes",
                    "Glucose forms an insulating layer of gas on the nails",
                    "The molecular mass of glucose is too heavy to conduct electricity"
                ],
                "answer": 0,
                "hint": "Covalent bonds in glucose remain intact without liberating hydrogen ions.",
                "explanation": "Although glucose (C6H12O6) contains hydrogen, its covalent bonds do not ionise in aqueous solution to yield free H+ or H3O+ ions, making it non-conducting."
            }
        ]
    },
    {
        "id": 8,
        "title": "Aqueous Acid Ionisation",
        "subtitle": "Water Obligation for Proton Release, Hydronium Ions, and Corrosive Alkalis",
        "speech": "Do acids generate hydrogen ions only in the presence of water? In Activity 2.9, solid sodium chloride is reacted with concentrated sulphuric acid inside a dry boiling tube, evolving pungent dry hydrogen chloride gas. When dry blue litmus paper is held directly in the path of the exiting gas, no colour change occurs whatsoever. However, when a strip of moist blue litmus paper is exposed to the identical gas, it turns bright red instantly. This pivotal observation proves that hydrogen chloride gas cannot dissociate into free hydrogen ions in the dry state; water molecules are strictly required to pull protons away from chlorine atoms. Because a bare hydrogen ion is simply a subatomic proton with an intense electric charge density, it cannot exist independently in water. Instead, it combines spontaneously with a polar water molecule to form a stable hydronium ion, designated as H3O+. Similarly, bases dissociate in water to produce hydroxide ions, OH-. Bases that dissolve freely in water are specifically called alkalis, such as sodium hydroxide and potassium hydroxide. Alkalis feel soapy to touch, taste bitter, and are highly corrosive to biological tissue, which is why commercial containers carry prominent hazard warning labels.",
        "content": {
            "concept": "Acids generate hydrogen ions only in the presence of water. Bare protons cannot exist independently in water and instantly combine with water molecules to form hydronium ions (H3O+). Bases produce hydroxide ions (OH-); water-soluble bases are known as alkalis.",
            "formula": "\\text{HCl} + \\text{H}_2\\text{O} \\rightarrow \\text{H}_3\\text{O}^+ + \\text{Cl}^- \\quad | \\quad \\text{NaOH}(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{Na}^+(aq) + \\text{OH}^-(aq)",
            "points": [
                "Activity 2.9: Dry HCl gas does not change dry blue litmus paper.",
                "Moist blue litmus paper turns red, proving water is indispensable for acid ionisation.",
                "Hydrogen ions combine with water molecules to form hydronium ions: H+ + H2O → H3O+.",
                "Bases generate mobile hydroxide ions (OH-) in aqueous solution.",
                "Water-soluble bases are called alkalis; they are soapy to touch, bitter, and corrosive."
            ]
        },
        "checkpoints": [
            {
                "question": "Why does dry hydrogen chloride gas fail to change the colour of dry blue litmus paper?",
                "options": [
                    "Hydrogen chloride gas is an alkaline compound in dry form",
                    "Acidic ionisation and proton liberation strictly require water molecules",
                    "Dry litmus paper is coated with an impervious plastic layer",
                    "Chlorine gas bleaches the blue dye completely before reaction"
                ],
                "answer": 1,
                "hint": "Proton transfer from HCl can only occur when polar water molecules act as proton acceptors.",
                "explanation": "HCl molecules only ionise to release H+ ions in the presence of water. Without moisture, no hydronium ions are formed, so dry litmus paper remains unaffected."
            },
            {
                "question": "What chemical species is formed when a liberated hydrogen ion binds to a water molecule?",
                "options": [
                    "Hydroxide ion (OH-)",
                    "Hydronium ion (H3O+)",
                    "Hydrogen peroxide (H2O2)",
                    "Hydride anion (H-)"
                ],
                "answer": 1,
                "hint": "The formula represents a proton attached to a neutral water molecule: H+ + H2O.",
                "explanation": "Isolated H+ ions cannot exist independently in aqueous solution due to their high charge density. They combine with polar H2O molecules to form hydronium ions: H3O+."
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

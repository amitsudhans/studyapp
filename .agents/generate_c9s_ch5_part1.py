#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part1 = [
    {
        "id": 1,
        "title": "Mixtures Around Us",
        "subtitle": "Introduction & Overview: Everyday Applications & Chapter Objectives",
        "speech": (
            "Welcome, students, to Chapter 5, Exploring Mixtures and their Separation. Look around your home "
            "and kitchen: almost everything we eat, drink, and breathe is a mixture of two or more substances. "
            "In daily life, mixtures power remarkable processes—from extracting pure white sugar crystals out of "
            "fresh sugarcane juice to diagnosing serious illnesses like malaria using just a tiny drop of blood "
            "under a microscope! Building upon what you learned in earlier grades about pure substances and "
            "simple handpicking, this chapter takes you deeper into the science of mixtures. We will classify "
            "mixtures by uniformity and particle size, measure exact solution concentrations for medicine and "
            "farming, and explore how temperature governs solubility. Most importantly, you will master laboratory "
            "and industrial separation techniques—including crystallization, distillation, paper chromatography, "
            "separating funnels, sublimation, centrifugation, and coagulation. We will also examine colloids, "
            "the Tyndall effect, traditional Indian craft methods like Kannauj attar distillation, and modern "
            "challenges like lithium battery recycling and artificial blood. Let us dive into the fascinating "
            "world of mixtures and discover how scientists isolate exactly what they need. By observing particle "
            "size, solubility, boiling points, and light scattering, you will soon choose the smartest separation "
            "method for any everyday, laboratory, or industrial mixture with complete confidence."
        ),
        "checkpoints": [
            {
                "question": "Which pair illustrates everyday applications of mixtures and separation introduced in this chapter?",
                "options": [
                    "Extracting white sugar crystals from sugarcane and detecting malaria from blood drops",
                    "Melting iron ore in space and freezing nitrogen",
                    "Painting walls and writing with chalk",
                    "Charging batteries without chemicals"
                ],
                "answer": 0,
                "hint": "Think of both food processing from crops and medical diagnostics.",
                "explanation": "Sugar crystal extraction from sugarcane and malaria diagnosis from blood drops both rely on mixture properties and separation."
            },
            {
                "question": "Why do scientists and industries develop specialized separation techniques?",
                "options": [
                    "Because all mixtures are already pure substances",
                    "To isolate useful components or remove impurities based on physical properties",
                    "To destroy all solutes inside water",
                    "To turn liquids into permanent alloys"
                ],
                "answer": 1,
                "hint": "Separation exploits differences in boiling point, solubility, density, or particle size.",
                "explanation": "Separation techniques isolate desired pure substances or remove unwanted impurities using physical property differences."
            }
        ]
    },
    {
        "id": 2,
        "title": "Classifying Mixtures",
        "subtitle": "Section 5.1 & Activity 5.1: Homogeneous vs Heterogeneous Mixtures",
        "speech": (
            "How can we classify the countless mixtures around us? Scientists divide them into two broad "
            "families based on uniformity. Homogeneous mixtures, also called solutions, have a completely "
            "uniform composition throughout—every spoonful tastes or looks identical, such as sugar dissolved "
            "in water, vinegar, or aerated soda drinks. Heterogeneous mixtures lack uniformity: their distinct "
            "components stay visible or settle over time, like sand in water or oil floating on water. Let us "
            "perform Activity 5.1 by preparing three water mixtures: common salt for Group A, chalk powder for "
            "Group B, and a few drops of milk for Group C. Watch four tests carefully. First, particle "
            "visibility: salt vanishes completely, milk looks uniformly cloudy, while chalk grains are clearly "
            "seen. Second, shine a laser pointer: the beam passes invisibly through salt water, yet its path "
            "glows brightly in milk and chalk water! Third, leave them undisturbed: chalk settles to the bottom, "
            "whereas salt and milk stay suspended. Fourth, filter them: only chalk leaves residue on filter paper. "
            "Why did milk scatter light like chalk yet pass through filter paper like salt? Because milk is a "
            "colloid—sitting right between a true solution and a coarse suspension! These four simple tests give "
            "us a reliable scientific toolkit for classifying any mixture we encounter."
        ),
        "checkpoints": [
            {
                "question": "In Activity 5.1, which mixture leaves a solid residue on filter paper and settles down on standing?",
                "options": [
                    "Group A (common salt in water)",
                    "Group B (chalk powder in water)",
                    "Group C (milk drops in water)",
                    "Vinegar and water"
                ],
                "answer": 1,
                "hint": "Chalk powder forms a coarse suspension with large visible particles.",
                "explanation": "Chalk powder in water is a heterogeneous suspension whose large particles settle and get trapped by filter paper."
            },
            {
                "question": "Which list contains only homogeneous mixtures (solutions)?",
                "options": [
                    "Sand in water, oil in water, chalk in water",
                    "Sugar in water, vinegar, aerated soda drink",
                    "Milk, muddy water, smoke",
                    "Sawdust in water, iron filings in sulfur"
                ],
                "answer": 1,
                "hint": "Look for mixtures with completely uniform composition throughout.",
                "explanation": "Sugar water, vinegar, and aerated soda have uniform composition throughout, making them homogeneous solutions."
            }
        ]
    },
    {
        "id": 3,
        "title": "Solutions & Concentration",
        "subtitle": "Section 5.2, 5.2.1 & 5.2.2: Solute, Solvent & Percentage Formulas",
        "speech": (
            "In every true solution, two roles exist: the solute is the substance that gets dissolved, usually "
            "present in smaller quantity, while the solvent is the substance that does the dissolving, usually "
            "present in larger quantity. Why do exact proportions matter so much? Imagine preparing Oral "
            "Rehydration Solution, or ORS, for a dehydrated patient, or mixing agricultural pesticides: too "
            "weak and it fails, too strong and it becomes harmful! Concentration measures the amount of solute "
            "dissolved in a given amount of solvent or solution. Scientists express concentration in three "
            "standard percentage ways. First, mass by mass percentage, percent m by m, equals mass of solute "
            "divided by total mass of solution times one hundred—useful for solid-in-liquid or solid mixtures. "
            "Second, mass by volume percentage, percent m by v, equals grams of solute per one hundred "
            "millilitres of solution, widely printed on medical drips like five percent glucose or zero point "
            "nine percent saline. Third, volume by volume percentage, percent v by v, equals millilitres of "
            "solute per one hundred millilitres of solution, ideal for miscible liquids like perfumes and vinegar. "
            "Always remember: the denominator in every percentage formula is the total mass or total volume of the "
            "complete solution, not the solvent alone! Checking units carefully prevents costly mixing errors."
        ),
        "checkpoints": [
            {
                "question": "If 20 g of sugar is dissolved in 80 g of water, what is the mass by mass percentage (% m/m) of the solution?",
                "options": [
                    "20%",
                    "25%",
                    "80%",
                    "10%"
                ],
                "answer": 0,
                "hint": "Total mass of solution = mass of solute + mass of solvent = 20 g + 80 g = 100 g.",
                "explanation": "% m/m = (20 g / (20 g + 80 g)) × 100 = (20 / 100) × 100 = 20%."
            },
            {
                "question": "Which concentration unit is commonly used on medical IV bags like 5% glucose or 0.9% saline?",
                "options": [
                    "Volume by volume (% v/v)",
                    "Mass by volume (% m/v)",
                    "Parts per million only",
                    "Density in kg/m³"
                ],
                "answer": 1,
                "hint": "Solid glucose or salt is weighed in grams and dissolved to make a solution volume in millilitres.",
                "explanation": "Medical infusions commonly express solid solute mass (g) per 100 mL of solution as % m/v."
            }
        ]
    },
    {
        "id": 4,
        "title": "Solubility & Temperature",
        "subtitle": "Section 5.2.3 & Activity 5.2: Saturated Solutions & Solubility Curves",
        "speech": (
            "Can you keep dissolving spoon after spoon of salt into a single glass of water forever? No! At a "
            "given temperature, there is a strict upper limit. Solubility is the maximum amount of solute that "
            "can dissolve in one hundred millilitres or one hundred grams of solvent at a specific temperature. "
            "Once a solution holds that maximum limit, it becomes a saturated solution—any extra solute added "
            "simply settles undissolved at the bottom. Temperature strongly controls this limit, but solids "
            "and gases behave oppositely! For most solid solutes like sugar or potassium nitrate, solubility "
            "increases as temperature rises, because warmer solvent particles have more kinetic energy to "
            "separate and surround solute particles. Conversely, for gases dissolved in liquids—like oxygen in "
            "pond water or carbon dioxide in soda—solubility decreases as temperature rises, which is why warm "
            "soda goes flat quickly! In Activity 5.2, plotting solubility curves for compounds A and B versus "
            "temperature lets us compare how steeply each substance's solubility responds to heating and predict "
            "how much solute will crystallize out when cooled. For instance, if a compound's solubility drops from "
            "eighty grams at sixty degrees Celsius to twenty grams at twenty degrees, cooling forces sixty grams "
            "to separate as pure crystals!"
        ),
        "checkpoints": [
            {
                "question": "What happens when extra solute is added to a saturated solution at constant temperature?",
                "options": [
                    "It dissolves faster than before",
                    "It remains undissolved and settles at the bottom",
                    "The solvent freezes immediately",
                    "The solution turns into a gas"
                ],
                "answer": 1,
                "hint": "A saturated solution already holds the maximum solute possible at that temperature.",
                "explanation": "At saturation, no more solute can dissolve at that temperature, so extra solute settles undissolved."
            },
            {
                "question": "How does raising temperature generally affect the solubility of solids versus gases in water?",
                "options": [
                    "Both solid and gas solubility decrease",
                    "Solid solubility generally increases, whereas gas solubility decreases",
                    "Solid solubility decreases, whereas gas solubility increases",
                    "Temperature has no effect on either"
                ],
                "answer": 1,
                "hint": "Think of hot tea dissolving sugar easily, while warm soda loses its fizz.",
                "explanation": "Heating generally increases solid solubility in water, while decreasing gas solubility."
            }
        ]
    },
    {
        "id": 5,
        "title": "Crystallization",
        "subtitle": "Section 5.3.1 & Activity 5.3: Pure Crystals & Traditional Salt Making",
        "speech": (
            "Suppose you want to recover pure solid crystals from a solution without burning or decomposing "
            "them, and without trapping dissolved impurities. You use crystallization! Crystallization is the "
            "process of forming pure, regularly patterned geometric crystals from a hot saturated solution as "
            "it cools, relying on the drop in solubility at lower temperatures. In Activity 5.3, we prepare "
            "blue copper sulfate crystals step by step: dissolve impure copper sulfate in water, add a drop "
            "of dilute sulfuric acid to prevent hydrolysis, heat gently in a water bath to make a saturated "
            "solution, filter out insoluble dirt, and let the clear filtrate cool undisturbed overnight. By "
            "morning, sparkling triclinic blue crystals appear, which we dry gently between filter paper folds. "
            "Nature forms breathtaking crystals too—from rock salt and candy sugar to six-sided snowflakes, "
            "frost, quartz, and limestone formations inside Mawsmai Cave in Meghalaya. In India, traditional "
            "salt artisans also produce distinct crystalline salts like fine panga salt and coarse solar-evaporated "
            "karkatch salt along our coastlines and salt pans. Unlike harsh boiling to dryness, slow crystallization "
            "leaves soluble impurities behind in the remaining mother liquor and protects delicate solid crystals from "
            "charring or decomposing on a hot laboratory flame."
        ),
        "checkpoints": [
            {
                "question": "Why is crystallization preferred over simple evaporation to dryness for purifying copper sulfate?",
                "options": [
                    "Evaporation is always faster",
                    "Crystallization leaves soluble impurities behind in solution and avoids charring the solid",
                    "Crystallization works without any solvent",
                    "Evaporation produces larger geometric crystals"
                ],
                "answer": 1,
                "hint": "Think about what happens to soluble impurities and heat-sensitive solids during boiling to dryness.",
                "explanation": "Crystallization yields pure geometric crystals while leaving soluble impurities dissolved and preventing thermal decomposition."
            },
            {
                "question": "In Activity 5.3, why is a drop of dilute sulfuric acid added while preparing copper sulfate crystals?",
                "options": [
                    "To turn the crystals red",
                    "To prevent hydrolysis of copper sulfate during heating",
                    "To freeze the water bath",
                    "To make the mixture heterogeneous"
                ],
                "answer": 1,
                "hint": "Acid stabilizes copper ions in hot aqueous solution.",
                "explanation": "Adding a drop of dilute sulfuric acid prevents hydrolysis so clean copper sulfate crystals form."
            }
        ]
    },
    {
        "id": 6,
        "title": "Distillation",
        "subtitle": "Section 5.3.2: Simple & Fractional Distillation, Kannauj Ittar & Refining",
        "speech": (
            "How do we separate a pure liquid from dissolved solids, or separate two miscible liquids like "
            "acetone and water? We use distillation! Simple distillation separates miscible liquids whose "
            "boiling points differ by at least twenty-five degrees Celsius, or recovers pure solvent from a "
            "salt solution. As the mixture is heated in a distillation flask, the lower-boiling component "
            "vaporizes first, travels through a water-cooled Liebig condenser, and condenses into a pure liquid "
            "called the distillate. India boasts a centuries-old mastery of distillation in Kannauj, where "
            "artisans use the traditional copper Deg-Bhapka apparatus to steam-distill baked clay or flowers "
            "into fragrant Mitti ka Ittar, capturing earthy aroma in sandalwood oil! On a massive industrial "
            "scale, petroleum refineries use fractional distillation inside tall fractionating towers. Crude "
            "oil is heated and separated by boiling-point ranges into essential fuels and products: LPG at the "
            "cool top, followed by petrol, kerosene, diesel, lubricating oil, and thick bitumen at the hot "
            "bottom—powering transport, aviation, and road construction. Whether in a glass flask, a copper "
            "Deg-Bhapka, or a towering industrial refinery column, distillation relies on reversible evaporation and condensation "
            "at distinct boiling temperatures, yielding pure liquid fractions cleanly without wasting any valuable raw materials."
        ),
        "checkpoints": [
            {
                "question": "Simple distillation works cleanly for two miscible liquids when their boiling points differ by at least:",
                "options": [
                    "2°C",
                    "10°C",
                    "25°C",
                    "100°C"
                ],
                "answer": 2,
                "hint": "Closer boiling points require a fractionating column.",
                "explanation": "Simple distillation separates miscible liquids whose boiling points differ by at least about 25°C."
            },
            {
                "question": "What does the traditional Kannauj Deg-Bhapka method use distillation to produce?",
                "options": [
                    "Bitumen for highways",
                    "Mitti ka Ittar (earthy perfume)",
                    "Copper sulfate crystals",
                    "Stainless steel alloys"
                ],
                "answer": 1,
                "hint": "Kannauj is India's historic perfume capital.",
                "explanation": "Kannauj's traditional Deg-Bhapka hydro-distillation extracts natural fragrances such as Mitti ka Ittar."
            }
        ]
    },
    {
        "id": 7,
        "title": "Paper Chromatography",
        "subtitle": "Section 5.3.3: Separating Dyes & Leaf Pigments by Movement Rate",
        "speech": (
            "Imagine a drop of black ink on filter paper. It looks like a single black colour, yet it is "
            "actually a clever mixture of several different dyes! How can we separate tiny amounts of closely "
            "related dissolved substances without boiling them? The answer is paper chromatography, whose name "
            "comes from the Greek word chroma, meaning colour. Take a strip of chromatographic or filter paper "
            "and draw a pencil baseline near the bottom—never ink, because ink would run! Place a small spot "
            "of black ink, food colouring, or crushed spinach leaf extract on the line. Suspend the strip in "
            "a jar so just the bottom tip touches a suitable solvent like water or two percent salt solution, "
            "keeping the spot above the liquid level. As the solvent climbs upward by capillary action, each "
            "component dissolves and travels at a different speed depending on how strongly it prefers the "
            "moving solvent versus sticking to the paper fibres. Soon, hidden yellow, blue, and red bands "
            "appear separated cleanly along the strip! Chemists, food inspectors, and forensic laboratories rely "
            "on chromatography every day because it needs only a tiny drop of sample, works at room temperature, "
            "and reveals whether a dye or medicine is pure or blended."
        ),
        "checkpoints": [
            {
                "question": "In paper chromatography, why is the baseline drawn with a pencil rather than a pen?",
                "options": [
                    "Pencil graphite is insoluble in the solvent and will not smear or interfere",
                    "Pen ink evaporates faster than water",
                    "Pencil lead attracts magnetic pigments",
                    "Pen ink stops capillary action completely"
                ],
                "answer": 0,
                "hint": "Think about what happens to pen ink when the solvent climbs past it.",
                "explanation": "Graphite is insoluble and stays fixed, whereas pen ink would dissolve and contaminate the chromatogram."
            },
            {
                "question": "On what principle does paper chromatography separate components of ink or spinach pigments?",
                "options": [
                    "Differences in boiling points above 25°C",
                    "Differing rates of movement across the paper with the rising solvent",
                    "Magnetic attraction to the glass jar",
                    "Sublimation of solid dyes"
                ],
                "answer": 1,
                "hint": "Some dyes travel fast with the solvent while others cling more to the paper.",
                "explanation": "Components separate because they move at different rates along the paper based on their solubility and affinity."
            }
        ]
    },
    {
        "id": 8,
        "title": "Separating Funnel",
        "subtitle": "Section 5.4.1: Separating Immiscible Liquids by Density Layers",
        "speech": (
            "We have explored three methods for homogeneous mixtures—crystallization, distillation, and paper "
            "chromatography. Now let us cross over to Section 5.4: separating heterogeneous mixtures! Start "
            "with two liquids that refuse to dissolve in each other, such as mustard oil and water, or kerosene "
            "and water. Because they do not mix, we call them immiscible liquids. When poured together and left "
            "undisturbed inside a pear-shaped glass separating funnel, gravity sorts them into two sharp, "
            "distinct layers based on density. Since mustard oil is less dense than water, it floats on top, "
            "while denser water sinks to form the bottom layer. Open the glass stopcock carefully at the base "
            "of the funnel! The heavier water layer drains smoothly into a beaker below. The moment the oily "
            "interface reaches the stopcock, shut the tap immediately. You have cleanly separated both liquids "
            "without heating a single drop! This simple density-layer principle is also used in industry to "
            "separate molten iron from lighter slag in blast furnaces. Notice why a separating funnel never works "
            "for alcohol and water or salt water: those liquids are completely miscible and form one single phase with no "
            "visible boundary layer to drain separately through the glass stopcock."
        ),
        "checkpoints": [
            {
                "question": "When mustard oil and water are placed in a separating funnel, which liquid forms the lower layer and drains first?",
                "options": [
                    "Mustard oil, because it is less dense",
                    "Water, because it is denser than mustard oil",
                    "Both drain together as a uniform solution",
                    "Neither can pass through a stopcock"
                ],
                "answer": 1,
                "hint": "Oil floats on water because oil has lower density.",
                "explanation": "Water is denser than mustard oil, so water forms the bottom layer and drains first through the stopcock."
            },
            {
                "question": "A separating funnel is suitable ONLY for separating:",
                "options": [
                    "Miscible liquids like alcohol and water",
                    "Immiscible liquids that form distinct density layers",
                    "Dissolved salt from seawater",
                    "Gases dissolved in soda"
                ],
                "answer": 1,
                "hint": "Two liquids must not dissolve into a single uniform phase.",
                "explanation": "A separating funnel separates immiscible liquids that separate into distinct layers by density."
            }
        ]
    }
]

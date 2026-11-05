"""
Data generator for NCERT Class 5 Science Chapter 3: The Mystery of Food - Part 2 (Slides 9 to 16)
Zero lecturer names. Indian male voice priority. Short punchy headings (1-3 words).
Zero raw LaTeX.
"""

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Fermenting Batter",
        "subtitle": "Finding #7: Beneficial Airborne Microbes Making Fluffy Idlis",
        "concept_html": """
            <p>Disha watched her mother grind soaked rice and black gram (urad dal) into a thick, smooth batter, leaving the covered bowl in a warm corner overnight. By dawn, the batter had miraculously swelled, doubled in volume, and filled with frothy bubbles!</p>
            <div class="my-3 p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200 text-xs">
                🌾 <strong>Finding #7 (Fermentation):</strong> Beneficial airborne wild yeasts and lactic acid bacteria naturally settle into the batter, consuming sugars and releasing harmless <strong>carbon dioxide gas</strong> and aromatic lactic acid.
            </div>
            <p>This biological transformation is called <strong>fermentation</strong>:</p>
            <div class="mt-3 grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🥣</span>
                    <strong class="text-slate-200 block">Fresh Batter</strong>
                    Dense, flat mixture of ground rice and soaked urad dal.
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🫧</span>
                    <strong class="text-amber-400 block">Overnight Warmth</strong>
                    Beneficial microbes ferment, generating trapped carbon dioxide bubbles.
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">☁️</span>
                    <strong class="text-cyan-400 block">Steamed Idli</strong>
                    Gas bubbles expand in steam, yielding soft, spongy, easily digestible cakes.
                </div>
            </div>
        """,
        "spoken_text": "Have you ever wondered how dense rice batter transforms into feather-light, spongy idlis? In the evening, Disha's mother left freshly ground rice and urad dal batter in a warm kitchen. By morning, the batter had risen to the very brim, frothing with tiny bubbles. Finding Number Seven reveals that beneficial wild microbes in the air land on the batter and ferment it. As these friendly bacteria and yeasts feed on starch, they produce carbon dioxide gas bubbles that get trapped in the dough. When steamed, these trapped bubbles expand, creating pillowy soft, wholesome idlis.",
        "lecture_script": "The biochemical process of batter fermentation, lactic acid bacteria and yeasts, carbon dioxide aeration, and nutritional enhancement of steamed idlis.",
        "checkpoints": [
            {
                "question": "What gas is produced by beneficial microbes during batter fermentation that causes idli and dosa batter to rise?",
                "options": [
                    "Pure liquid nitrogen",
                    "Carbon dioxide gas bubbles",
                    "Poisonous sulfur dioxide vapor",
                    "Chilled atmospheric oxygen"
                ],
                "correct": 1,
                "explanation": "Friendly wild yeasts and lactic acid bacteria consume starches and release carbon dioxide gas, which forms pockets of bubbles that cause the batter to swell and become fluffy.",
                "study_insight": "Fermentation also synthesizes B-complex vitamins and breaks down complex phytic acid, making minerals easier for our body to absorb."
            },
            {
                "question": "Why is fermented food like idli, dhokla, and curd considered exceptionally healthy for our digestive system?",
                "options": [
                    "Fermentation removes all calories so food has no energy",
                    "Fermentation pre-digests complex nutrients and enriches food with gut-friendly probiotics",
                    "Fermentation turns all food into pure solid stone",
                    "Fermented foods never need to be chewed"
                ],
                "correct": 1,
                "explanation": "Microbial fermentation breaks down complex starches and proteins into simpler compounds, making the food gentle on the stomach while providing helpful probiotic flora.",
                "study_insight": "Traditional fermented foods have supported gut health in world cuisines for thousands of years."
            }
        ]
    },
    {
        "id": 10,
        "title": "Gut Healing",
        "subtitle": "Finding #8: Fair Food Indigestion, Probiotics & Buttermilk Remedies",
        "concept_html": """
            <p>Disha\'s older brother Aditya visited a lively village fair and indulged in oily, uncovered street snacks that had been exposed to buzzing flies and road dust. That evening, he suffered from stomach cramps, bloating, and painful indigestion.</p>
            <div class="my-3 p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200 text-xs">
                ⚠️ <strong>Finding #8 (Indigestion):</strong> Consuming unhygienic, improperly cooked food or harmful microbes upsets the normal digestive balance, leading to <strong>indigestion</strong>.
            </div>
            <p>Their grandmother Paati prepared a time-tested soothing remedy: a tall glass of fresh <strong>curd and churned buttermilk (chaas)</strong> seasoned with roasted cumin and ginger:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">🥛 Probiotic Reinforcement</strong>
                    Curd is brimming with billions of live, friendly <em>Lactobacillus</em> bacteria that repopulate the gut lining and outcompete harmful germs.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">🌿 Soothing Carminatives</strong>
                    Ginger and roasted jeera soothe irritated stomach linings, stimulate digestive secretions, and relieve gas.
                </div>
            </div>
        """,
        "spoken_text": "After eating unhygienic snacks at a dusty fair, Disha's brother developed stomach cramps and severe indigestion. Uncovered street food exposed to flies can carry harmful bacteria that upset our delicate gut balance. Finding Number Eight reminds us that bad eating habits or harmful pathogens cause indigestion. To restore health, their grandmother served cool, fresh buttermilk seasoned with roasted cumin. Curd contains billions of friendly probiotic bacteria that colonize our digestive tract, driving away bad microbes and restoring calm, natural digestion.",
        "lecture_script": "Etiology of indigestion from unhygienic foods, pathogenic gastrointestinal disruption, and therapeutic gut restoration using probiotic buttermilk and carminative spices.",
        "checkpoints": [
            {
                "question": "Why is consuming fresh curd or churned buttermilk an effective home remedy for an upset stomach?",
                "options": [
                    "It freezes the stomach contents into solid ice",
                    "It supplies billions of beneficial probiotic bacteria that restore natural intestinal flora",
                    "It contains harsh acids that burn the stomach walls clean",
                    "It replaces all digestive fluids with mineral oil"
                ],
                "correct": 1,
                "explanation": "Curd and buttermilk are rich natural sources of live Lactobacillus probiotics that soothe the digestive lining, neutralize acidity, and outcompete harmful gastrointestinal pathogens.",
                "study_insight": "Consuming buttermilk after meals is an ancient Indian culinary tradition backed by modern microbiome science."
            },
            {
                "question": "Which habit is most likely to cause food poisoning and painful indigestion?",
                "options": [
                    "Drinking boiled, filtered drinking water",
                    "Eating uncovered street snacks exposed to dust, flies, and warm stagnant air",
                    "Eating fresh homemade vegetable stew served steaming hot",
                    "Chewing food thoroughly before swallowing"
                ],
                "correct": 1,
                "explanation": "Uncovered street food easily catches airborne dust, vehicle exhaust, and microbes carried on the legs of houseflies, causing rapid microbial contamination and food poisoning.",
                "study_insight": "Always prefer freshly prepared, piping-hot food served in clean, covered surroundings."
            }
        ]
    },
    {
        "id": 11,
        "title": "Market Fresh",
        "subtitle": "Inspecting Fresh Produce: Firmness, Color, Aroma & Defect Detection",
        "concept_html": """
            <p>Disha accompanied her grandfather Thatha to the bustling morning vegetable market. Thatha taught her that smart detectives inspect produce with all four senses before putting anything in their jute shopping bag:</p>
            <div class="my-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200">
                    <strong class="text-emerald-300 block mb-1">👁️ Visual Check</strong>
                    Vibrant natural color, intact unblemished peel, no dark bruised blotches, mold spots, or insect boreholes.
                </div>
                <div class="p-2.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-cyan-200">
                    <strong class="text-cyan-300 block mb-1">✋ Touch & Firmness</strong>
                    Firm, crisp stem ends; heavy for its size. Reject soggy, squishy, or unnaturally wrinkled items.
                </div>
                <div class="p-2.5 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200">
                    <strong class="text-amber-300 block mb-1">👃 Scent Assessment</strong>
                    Fresh, clean, earthy, or sweet natural aroma. Reject sour, fermented, or pungent rotting odors.
                </div>
                <div class="p-2.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-indigo-200">
                    <strong class="text-indigo-300 block mb-1">🚿 Thorough Washing</strong>
                    Wash all vegetables thoroughly under clean running tap water to remove soil particles and pesticide residues.
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Selecting fresh, unbruised produce ensures maximum nutrient density and prevents premature spoilage in home vegetable baskets.</p>
        """,
        "spoken_text": "At the vibrant morning bazaar, grandfather Thatha demonstrated how to select the freshest vegetables. A smart shopper uses all senses. Look closely for bright, healthy colors and smooth skin without dark mold spots or wormholes. Gently feel the vegetable; fresh carrots and ladyfingers should feel crisp and firm, never squishy or limp. Take a gentle sniff: fresh produce smells earthy and sweet, never sour or rancid. Always wash vegetables in clean running water before cooking to rinse away field dust and residues.",
        "lecture_script": "Sensory guidelines for fresh vegetable and fruit selection at the market, identifying fungal blemishes and decay, and pre-cooking washing protocols.",
        "checkpoints": [
            {
                "question": "Which observation indicates that a basket of tomatoes in the market is fresh and high quality?",
                "options": [
                    "Squishy, watery feel with patches of white fuzz near the stalk",
                    "Firm texture, taut unbroken skin, and bright red natural color",
                    "Sour fermented smell oozing from deep skin cracks",
                    "Dark brown sunken spots covering half the surface"
                ],
                "correct": 1,
                "explanation": "Fresh tomatoes are plump and firm to the touch, with taut, glossy skin free of cuts, punctures, dark bruises, or fuzzy mold growths.",
                "study_insight": "Bruised or punctured skins provide open entryways for spoilage bacteria to invade and spoil the interior pulp rapidly."
            },
            {
                "question": "Why is it essential to wash fresh fruits and vegetables under running tap water before eating or cooking?",
                "options": [
                    "To change their biological species completely",
                    "To wash away surface dirt, road dust, microbial spores, and chemical residues",
                    "To cook them without using any stove heat",
                    "To make them lose all natural vitamins"
                ],
                "correct": 1,
                "explanation": "Thorough washing under clean running water removes surface contaminants, adhering soil bacteria, fungal spores, and agricultural chemical residues from the peel.",
                "study_insight": "Never soak cut vegetables in water for long periods, as water-soluble vitamins (like Vitamin C and B-complex) will leach out."
            }
        ]
    },
    {
        "id": 12,
        "title": "Seasonal Harvest",
        "subtitle": "Finding #9: The Joy & Science of Seasonal, Local Produce",
        "concept_html": """
            <p>Disha\'s father brought home a basket of fragrant, sweet red lychees and juicy regional mangoes. He explained why these fruits taste so extraordinarily delicious right now: they are in their natural season!</p>
            <div class="my-3 p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200 text-xs">
                🥭 <strong>Finding #9 (Seasonal Nutrition):</strong> Fruits and vegetables taste best, cost less, and possess the highest concentration of vitamins and antioxidants when harvested during their natural season.
            </div>
            <p>Eating locally grown, seasonal produce offers tremendous advantages:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs text-slate-300">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                    <strong class="text-amber-400 block mb-1">Peak Ripeness & Flavor</strong>
                    Tree-ripened under natural sunshine without artificial chemical gas ripening; packed with natural sugars and nutrients.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                    <strong class="text-emerald-400 block mb-1">Local & Eco-Friendly</strong>
                    Does not travel thousands of kilometers in refrigerated diesel trucks, drastically reducing spoilage and carbon footprint.
                </div>
            </div>
            <div class="mt-2 p-2 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-400">
                <strong>Indian Seasonal Calendar:</strong> Watermelons & mangoes in scorching summer; guavas, carrots, and sweet oranges in crisp winter; custard apples in autumn.
            </div>
        """,
        "spoken_text": "When Disha's father brought home a basket of fragrant lychees and regional mangoes, their sweet aroma filled the kitchen. Finding Number Nine highlights the joy of seasonal fruits. Fruits that ripen naturally in their own season taste sweetest, have the highest levels of vitamins, and are free from artificial ripening chemicals. Choosing locally grown produce also means food does not need to travel across long distances in refrigerated transport, ensuring freshness on our plates while supporting our local farming communities.",
        "lecture_script": "The physiological advantages of seasonal crop cycles, nutritional density of naturally ripened fruits, and ecological benefits of local food systems.",
        "checkpoints": [
            {
                "question": "Why do seasonal fruits like summer mangoes or winter guavas have superior taste and nutritional value?",
                "options": [
                    "They are grown inside frozen plastic containers underground",
                    "They ripen naturally under seasonal sunlight, developing maximum vitamins, minerals, and natural sugars",
                    "They are injected with artificial coloring dyes every morning",
                    "They contain zero natural moisture"
                ],
                "correct": 1,
                "explanation": "Seasonal fruits develop under optimal climate and sunlight conditions, allowing complete metabolic synthesis of natural sugars, aromatic terpenes, and protective antioxidants.",
                "study_insight": "Nature provides high-water fruits like watermelon in hot summers to keep us hydrated, and Vitamin C-rich citrus fruits in winter to boost immunity."
            },
            {
                "question": "What is an ecological advantage of purchasing locally produced vegetables over exotic produce shipped from abroad?",
                "options": [
                    "Locally grown vegetables can never be cooked",
                    "It eliminates long-distance transport, reducing fuel consumption, pollution, and preservation chemicals",
                    "It ensures that no plants ever grow in farms again",
                    "Local vegetables have no seeds"
                ],
                "correct": 1,
                "explanation": "Local produce has low 'food miles', requiring minimal shipping and packaging, which lowers greenhouse gas emissions and reduces the need for post-harvest chemical preservatives.",
                "study_insight": "Food miles refer to the distance food travels from where it is grown to where it is consumed."
            }
        ]
    },
    {
        "id": 13,
        "title": "Chewing Tools",
        "subtitle": "Findings #10 & #11: The Four Types of Teeth & Mechanical Breakdown",
        "concept_html": """
            <p>What happens the moment you take a bite of fresh food? Digestion begins right in the mouth! <strong>Findings #10 & #11: Different types of teeth perform specialized mechanical tasks to break food down.</strong></p>
            <p>Humans possess 32 permanent teeth categorized into four specialized dental tools:</p>
            <div class="my-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <div class="flex items-center space-x-1.5 mb-1">
                        <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                        <strong class="text-white">Incisors (8 total)</strong>
                    </div>
                    Sharp, chisel-like flat front teeth designed for <strong>cutting and biting</strong> into foods (like biting an apple).
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <div class="flex items-center space-x-1.5 mb-1">
                        <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                        <strong class="text-white">Canines (4 total)</strong>
                    </div>
                    Pointed, dagger-like sharp teeth beside incisors, specialized for <strong>piercing and tearing</strong> tough fibrous food.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <div class="flex items-center space-x-1.5 mb-1">
                        <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
                        <strong class="text-white">Premolars (8 total)</strong>
                    </div>
                    Broad teeth with two ridges behind canines, designed for <strong>crushing and holding</strong> food chunks.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <div class="flex items-center space-x-1.5 mb-1">
                        <span class="w-3 h-3 rounded-full bg-indigo-400"></span>
                        <strong class="text-white">Molars (12 total)</strong>
                    </div>
                    Wide, flat back teeth with deep grooves, engineered for powerful <strong>grinding and pulping</strong> into fine paste.
                </div>
            </div>
        """,
        "spoken_text": "Did you know that human digestion begins right inside your mouth? Look closely at your teeth in a mirror. You will discover four distinct shapes, each designed like a precision engineering tool. In the front, your eight incisors are flat like chisels to cut and bite into food. Next to them sit four sharp, pointed canines designed to pierce and tear. Further back are eight broad premolars that crush, followed by twelve wide, bumpy molars that grind food into a fine, smooth paste. Together, they perform mechanical mastication, preparing every bite for digestion.",
        "lecture_script": "Dental morphology and functional specialization: incisors for cutting, canines for tearing, premolars for crushing, and molars for grinding.",
        "checkpoints": [
            {
                "question": "Which teeth act like sharp chisels to bite and cut off a crisp piece of carrot or apple?",
                "options": [
                    "Back grinding molars",
                    "Front flat incisors",
                    "Wisdom molars",
                    "Side tongue taste buds"
                ],
                "correct": 1,
                "explanation": "The 8 front incisors (4 upper, 4 lower) have thin, sharp horizontal cutting edges designed specifically for slicing and biting off food portions.",
                "study_insight": "Incisors act like kitchen knives, cutting larger food into bite-sized morsels."
            },
            {
                "question": "What is the primary role of the broad, flat molars located at the back of the mouth?",
                "options": [
                    "Tasting bitter medicines",
                    "Grinding and pulverizing food into a fine, digestible paste",
                    "Injecting stomach acid directly into food",
                    "Producing enamel tears"
                ],
                "correct": 1,
                "explanation": "Molars possess large, flattened occlusal surfaces with cusps that crush and grind food particles against each other under powerful jaw muscle forces.",
                "study_insight": "Molars provide the grinding surface area needed to turn solid grains and vegetables into an easily swallowable paste."
            }
        ]
    },
    {
        "id": 14,
        "title": "Saliva Power",
        "subtitle": "Finding #10: Salivary Amylase, Chemical Digestion & Bolus Formation",
        "concept_html": """
            <p>Try chewing a piece of plain boiled rice or dry chapati slowly for two minutes without swallowing. What happens? It begins to taste delightfully <strong>sweet</strong>! Why?</p>
            <div class="my-3 p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-cyan-200 text-xs">
                💧 <strong>Finding #10 (Saliva & Digestion):</strong> Chewing food thoroughly stimulates three pairs of salivary glands to pour <strong>saliva</strong> into the mouth, initiating chemical digestion.
            </div>
            <p>Saliva is not just water—it is a powerful biological digestive fluid:</p>
            <ul class="mt-2 space-y-1.5 text-xs text-slate-300">
                <li class="flex items-start space-x-2">
                    <span class="text-cyan-400 font-bold shrink-0">1.</span>
                    <span><strong>Enzyme Starch Breakdown:</strong> Saliva contains an enzyme called <em>salivary amylase (ptyalin)</em> that breaks down complex, tasteless starch molecules into simple, sweet maltose sugar.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-cyan-400 font-bold shrink-0">2.</span>
                    <span><strong>Moistening & Lubrication:</strong> Mucus in saliva binds crushed food into a soft, slippery ball called a <strong>bolus</strong>, allowing it to slide smoothly down the food pipe (esophagus).</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-cyan-400 font-bold shrink-0">3.</span>
                    <span><strong>Germ Defense:</strong> Saliva contains natural antibacterial enzymes (lysozyme) that neutralize bacteria entering with food.</span>
                </li>
            </ul>
        """,
        "spoken_text": "If you chew a piece of plain roti or boiled rice slowly for two minutes, you will notice a wonderful sweet taste spreading over your tongue. That sweetness is the magic of saliva! Your salivary glands release a digestive fluid containing an enzyme called salivary amylase. This enzyme immediately goes to work, breaking down complex starch into simple, sweet sugars right inside your mouth. Thorough chewing also lubricates the crushed food with mucus, turning it into a soft, smooth ball that glides effortlessly down your food pipe without scratching your throat.",
        "lecture_script": "The physiology of mastication and salivation, salivary amylase enzymatic hydrolysis of starch into maltose, and bolus lubrication.",
        "checkpoints": [
            {
                "question": "Why does a piece of plain wheat roti or rice begin to taste sweet after being chewed thoroughly for over a minute?",
                "options": [
                    "The teeth produce table sugar crystals while grinding",
                    "Salivary amylase enzyme breaks down complex starch into simpler sweet sugars",
                    "The tongue changes its color into sweet glucose",
                    "Water inside the food evaporates, leaving only sugar syrup"
                ],
                "correct": 1,
                "explanation": "Salivary amylase in our saliva chemically digests complex, tasteless starches in wheat and rice, converting them into simple disaccharide sugars like maltose.",
                "study_insight": "Chewing 20 to 30 times per bite maximizes enzyme contact, reducing the digestive workload on the stomach."
            },
            {
                "question": "What is the soft, moistened ball of chewed food that slides down the esophagus called?",
                "options": [
                    "Chyme",
                    "Bolus",
                    "Calculus",
                    "Plaque"
                ],
                "correct": 1,
                "explanation": "The smooth, lubricated mass of crushed food mixed with saliva is called a bolus. It is shaped by the tongue and swallowed into the esophagus.",
                "study_insight": "The muscular contractions of the esophagus that push the bolus down toward the stomach are called peristalsis."
            }
        ]
    },
    {
        "id": 15,
        "title": "Tooth Care",
        "subtitle": "Finding #12: Oral Hygiene, Enamel Protection & Cavity Defense",
        "concept_html": """
            <p>After visiting a dentist to treat a painful toothache, Disha learned how cavities form. <strong>Finding #12: Maintaining oral hygiene and visiting a dentist is essential for tooth health.</strong></p>
            <div class="my-3 p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200 text-xs">
                🦷 <strong>How Cavities Form:</strong> When sugary sweets or sticky food particles remain trapped between teeth, mouth bacteria feed on the sugars and produce corrosive <strong>acid</strong>. This acid dissolves hard tooth <strong>enamel</strong>, creating holes called <strong>cavities</strong> (dental caries).
            </div>
            <p>The Golden Rules of Daily Oral Health:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">🪥 Brush Twice Daily</strong>
                    Brush gently for 2 full minutes in circular motions every morning and before bed at night.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-emerald-400 block mb-1">💧 Rinse After Eating</strong>
                    Gargle with clean water after every meal to flush away lingering food particles and acids.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">🍬 Limit Sticky Sugars</strong>
                    Avoid frequent toffees, sodas, and sticky sweets that cling tenaciously to enamel crevices.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-indigo-400 block mb-1">🩺 Dental Checkups</strong>
                    Visit a dentist twice a year to detect microscopic plaque and tartar before cavities become painful.
                </div>
            </div>
        """,
        "spoken_text": "Our teeth are coated with tooth enamel, the hardest substance in the human body. Yet, enamel can be destroyed by tiny oral bacteria! When sweet or sticky food stays trapped between your teeth, bacteria feast on the sugars and produce corrosive acid. This acid gradually dissolves the enamel, carving out tiny holes called cavities that cause severe toothaches. Finding Number Twelve emphasizes the importance of oral hygiene. Brush your teeth gently twice a day, rinse your mouth with clean water after every meal, cut down on sticky candies, and visit your dentist for checkups.",
        "lecture_script": "The pathology of dental caries, bacterial acid demineralization of hydroxyapatite enamel, and preventive oral hygiene protocols.",
        "checkpoints": [
            {
                "question": "What is the primary cause of tooth cavities (dental caries)?",
                "options": [
                    "Drinking chilled water on hot summer days",
                    "Mouth bacteria feeding on trapped sugars and producing acid that dissolves tooth enamel",
                    "Chewing raw crispy carrots and cucumbers",
                    "Brushing teeth with a soft toothbrush"
                ],
                "correct": 1,
                "explanation": "Bacteria in dental plaque ferment trapped food sugars into lactic and organic acids. These acids demineralize and dissolve the calcium-rich tooth enamel, forming cavities.",
                "study_insight": "Enamel cannot regenerate once destroyed by deep cavities; dentists must clean and fill the hollow space."
            },
            {
                "question": "Which daily habit best protects teeth from acid attacks after meals?",
                "options": [
                    "Eating chocolate before sleeping without brushing",
                    "Rinsing the mouth thoroughly with clean water to flush out food particles and neutralize acid",
                    "Chewing toothpicks forcefully between gums",
                    "Avoiding drinking any water during the day"
                ],
                "correct": 1,
                "explanation": "Rinsing with clean water immediately after meals flushes out trapped food debris and dilutes acidic byproducts before they can erode the tooth surface.",
                "study_insight": "Fluoride in toothpaste helps remineralize microscopic enamel weaknesses before full cavities form."
            }
        ]
    },
    {
        "id": 16,
        "title": "Choking Defense",
        "subtitle": "Finding #13: Epiglottis Airway Shield, Slow Eating & Choking Prevention",
        "concept_html": """
            <p>Have you ever coughed violently when laughing or talking excitedly while gulping lunch? Disha\'s mother cautioned her never to talk or hurry while eating. <strong>Finding #13: Food must be eaten slowly and chewed thoroughly to prevent choking.</strong></p>
            <div class="my-3 p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200 text-xs">
                ⚠️ <strong>The Crossroads in Your Throat:</strong> The pharynx divides into two parallel tubes: the <strong>food pipe (esophagus)</strong> leading to the stomach, and the <strong>windpipe (trachea)</strong> leading to the lungs.
            </div>
            <p>A miraculous leaf-shaped muscular flap called the <strong>epiglottis</strong> guards this junction:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200">
                    <strong class="text-emerald-300 block mb-1">🛡️ Normal Swallowing</strong>
                    When you swallow calmly, the epiglottis automatically folds downward like a trapdoor, sealing the windpipe so food slides safely into the esophagus.
                </div>
                <div class="p-2.5 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200">
                    <strong class="text-rose-300 block mb-1">🚨 Choking Hazard</strong>
                    If you talk, laugh, or gasp while eating, the windpipe stays open to let air pass. Food slips into the windpipe, triggering violent coughing to blow it out!
                </div>
            </div>
        """,
        "spoken_text": "Why do our elders always tell us to sit quietly and never speak with food in our mouths? Inside your throat lies a busy biological crossroad. Two parallel tubes run side by side: the food pipe going to your stomach, and the windpipe going to your lungs. Right above your windpipe sits a marvelous flap of tissue called the epiglottis. When you swallow food calmly, the epiglottis folds down like a safety lid, sealing your windpipe. But if you talk or laugh while eating, your windpipe opens to allow air to vibrate your vocal cords. A stray grain of rice or piece of food can slip down the wrong pipe, causing choking. Finding Number Thirteen reminds us: eat slowly, sit calmly, and chew thoroughly.",
        "lecture_script": "The anatomy of the pharynx, larynx, and epiglottis valve mechanism, the mechanics of swallowing, and choking prevention.",
        "checkpoints": [
            {
                "question": "What is the biological function of the flap of tissue called the epiglottis during swallowing?",
                "options": [
                    "It releases stomach acid into the tongue",
                    "It covers and seals the windpipe (trachea) so food enters only the esophagus",
                    "It crushes hard food grains like a molar tooth",
                    "It produces saliva to cool down spicy curries"
                ],
                "correct": 1,
                "explanation": "The epiglottis acts like an automatic lid, tilting over the entrance of the trachea (windpipe) during swallowing to prevent food or liquids from entering the respiratory airways.",
                "study_insight": "The cough reflex is an emergency defense mechanism designed to expel foreign particles accidentally lodged in the airway."
            },
            {
                "question": "Why is it dangerous to laugh, talk excitedly, or run while chewing food?",
                "options": [
                    "Food will instantly turn into ice",
                    "Talking forces the epiglottis to open for air, allowing food particles to slip into the windpipe and cause choking",
                    "It stops the heart from beating completely",
                    "It permanently breaks all front incisor teeth"
                ],
                "correct": 1,
                "explanation": "Vocalizing requires airflow through an open windpipe. Talking while swallowing prevents the epiglottis from closing tightly, creating a life-threatening choking risk if food blocks the trachea.",
                "study_insight": "Always sit comfortably, chew with your mouth closed, and finish swallowing before speaking."
            }
        ]
    }
]


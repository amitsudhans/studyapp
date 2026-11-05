"""
Part 3 of NCERT Class 5 Science Chapter 6: Some Unique Places
Mastery Challenge Quiz Questions 1 to 40 (Slides 17 to 20)
10 Questions per Challenge Slide with instant feedback, explanation, and solution_html
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

QUIZ_QUESTIONS = [
    # Challenge 1 (Q1 to Q10)
    {
        "id": 1,
        "question": "What is the geographical definition of an island?",
        "options": [
            "A high mountain completely covered with thick snow",
            "A landmass completely surrounded by water on all sides",
            "A piece of land surrounded by water on three sides only",
            "A flat desert bordered on one side by an ocean"
        ],
        "answer": 1,
        "explanation": "An island is a body of land surrounded by water on all sides. Land surrounded by water on three sides is a peninsula.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Geographical Landform Classifications:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>Island:</strong> Land completely surrounded by water on all 4 sides (e.g. Andaman and Nicobar Islands).</li>
                    <li><strong>Peninsula:</strong> Land surrounded by water on 3 sides (e.g. Peninsular India bounded by Arabian Sea, Bay of Bengal, Indian Ocean).</li>
                    <li><strong>Isthmus:</strong> A narrow strip of land connecting two larger land masses.</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (A landmass completely surrounded by water on all sides)</p>
            </div>
        """
    },
    {
        "id": 2,
        "question": "Where is India's southernmost geographical point, Indira Point, situated?",
        "options": [
            "Kanyakumari, Tamil Nadu",
            "Great Nicobar Island in the Andaman and Nicobar archipelago",
            "Rameswaram Island",
            "Minicoy Island in Lakshadweep"
        ],
        "answer": 1,
        "explanation": "Indira Point is located at the southern tip of Great Nicobar Island at approximately 6°45' North latitude.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Geographic Boundaries of India:</strong></p>
                <p class='text-slate-300'>Kanyakumari (Cape Comorin at 8°4'N) is the southernmost point of mainland India. However, the absolute southernmost point of the entire Indian union is Indira Point on Great Nicobar Island (6°45'N), marking our maritime gateway to the Malacca Strait.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Great Nicobar Island)</p>
            </div>
        """
    },
    {
        "id": 3,
        "question": "Why do massive canopy trees in Andaman rainforests grow wide, flared buttress roots?",
        "options": [
            "To absorb saltwater directly from the sea",
            "Because rainforest topsoil is very shallow above bedrock, so flared roots provide a wide mechanical tripod base against winds",
            "To catch passing wild animals for food",
            "To float on floodwaters like boats"
        ],
        "answer": 1,
        "explanation": "Shallow rainforest soil prevents deep taproot growth. Flared buttress roots act as external structural buttresses, distributing mechanical tension and anchoring tall trees against cyclonic gales.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Structural Biomechanics of Buttress Roots:</strong></p>
                <p class='text-slate-300'>In tropical rainforests, high rainfall quickly leaches nutrients into a thin topsoil layer (30-50 cm). Buttress roots flare outward horizontally up to 10 metres, functioning like architectural flying buttresses that withstand wind shear and prevent tree toppling.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 4,
        "question": "Which prized timber tree with prominent buttress roots serves as the State Tree of the Andaman and Nicobar Islands?",
        "options": ["Teak", "Andaman Padauk (Pterocarpus dalbergioides)", "Sal", "Rosewood"],
        "answer": 1,
        "explanation": "The Andaman Padauk, renowned for its strong reddish-brown wood and majestic buttressed trunk, is the official State Tree.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>State Emblems of Andaman & Nicobar:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>State Tree:</strong> Andaman Padauk (<em>Pterocarpus dalbergioides</em>)</li>
                    <li><strong>State Bird:</strong> Andaman Wood Pigeon (<em>Columba palumboides</em>)</li>
                    <li><strong>State Animal:</strong> Dugong (Sea Cow, <em>Dugong dugon</em>)</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Andaman Padauk)</p>
            </div>
        """
    },
    {
        "id": 5,
        "question": "What is the official State Bird of the Andaman and Nicobar Islands?",
        "options": ["House Sparrow", "Andaman Wood Pigeon (Columba palumboides)", "Indian Peafowl", "Greater Flamingo"],
        "answer": 1,
        "explanation": "The Andaman Wood Pigeon is a large, endemic forest canopy pigeon and the designated State Bird of the archipelago.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Andaman Wood Pigeon Profile:</strong></p>
                <p class='text-slate-300'>Measuring about 40 cm in length, this shy canopy frugivore has a dark slate-grey body, a white head, and an iridescent violet-purple sheen on its neck. It feeds on forest figs and wild berries.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Andaman Wood Pigeon)</p>
            </div>
        """
    },
    {
        "id": 6,
        "question": "On which isolated volcanic island of the Andaman archipelago does the rare Narcondam Hornbill live exclusively?",
        "options": ["Barren Island", "Narcondam Island", "Havelock Island", "Neil Island"],
        "answer": 1,
        "explanation": "The Narcondam Hornbill (Rhyticeros narcondami) is strictly endemic to the tiny 6.8 sq km dormant volcanic island of Narcondam.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Narcondam Hornbill Endemism:</strong></p>
                <p class='text-slate-300'>Living on a single isolated volcano rising sharply from the Andaman Sea, this endangered hornbill has one of the smallest geographic ranges of any bird on Earth (under 7 sq km) with a population of only about 1,000 birds.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Narcondam Island)</p>
            </div>
        """
    },
    {
        "id": 7,
        "question": "What are corals scientifically classified as in marine biology?",
        "options": [
            "Inanimate mineral rocks",
            "Colonies of tiny invertebrate animals (polyps) that secrete calcium carbonate skeletons",
            "Marine plants with leaves and stems",
            "Fossilized algae shells"
        ],
        "answer": 1,
        "explanation": "Corals are colonies of tiny invertebrate marine animals called polyps that secrete calcium carbonate (limestone) to build rigid protective structures.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Biology of Coral Polyps:</strong></p>
                <p class='text-slate-300'>Each individual coral polyp is a soft-bodied tubular animal with stinging tentacles related to sea anemones. Over thousands of years, billions of interconnected polyps deposit limestone, creating vast underwater reefs.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 8,
        "question": "What microscopic organisms live inside coral tissues in a vital mutualistic symbiotic relationship?",
        "options": [
            "Freshwater bacteria",
            "Photosynthetic algae called zooxanthellae",
            "Parasitic sea worms",
            "Baby jellyfish"
        ],
        "answer": 1,
        "explanation": "Zooxanthellae algae reside within coral polyps, providing food via photosynthesis while receiving shelter and nutrients in return.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Coral-Algae Symbiosis:</strong></p>
                <p class='text-slate-300'>Zooxanthellae convert sunlight into glucose, providing up to 90% of the polyp's energy needs and giving corals their dazzling colours. In return, the coral provides carbon dioxide, nitrogen, and a safe calcium carbonate home.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Photosynthetic algae called zooxanthellae)</p>
            </div>
        """
    },
    {
        "id": 9,
        "question": "Why are coral reefs often celebrated as the 'Rainforests of the Ocean'?",
        "options": [
            "Because it rains heavily underwater",
            "Because they harbour extraordinary marine biodiversity, supporting over 25% of all marine species while occupying less than 0.1% of the seabed",
            "Because giant pine trees grow inside coral reefs",
            "Because coral reefs are made of wood"
        ],
        "answer": 1,
        "explanation": "Like terrestrial rainforests, coral reefs boast an immense concentration of biological diversity and complex food webs despite occupying a tiny fraction of the planet's surface.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Marine Biodiversity Hotspots:</strong></p>
                <p class='text-slate-300'>Reefs provide breeding grounds, nurseries, food, and shelter for thousands of species of fish, crustaceans, molluscs, and turtles, making them the most biodiverse marine habitats on Earth.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 10,
        "question": "Approximately what percentage of violent storm wave energy is absorbed and dissipated by healthy offshore coral reefs?",
        "options": ["10%", "30%", "60%", "Up to 97%"],
        "answer": 3,
        "explanation": "Healthy coral reefs absorb up to 97% of incident wave energy, protecting coastlines from storm surges and erosion.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Coastal Defense Mechanics:</strong></p>
                <p class='text-slate-300'>The rough, complex 3D topography of shallow coral reefs forces approaching oceanic waves to break offshore, dissipating up to 97% of wave impact energy before it can strike human beaches and island villages.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: D (Up to 97%)</p>
            </div>
        """
    },

    # Challenge 2 (Q11 to Q20)
    {
        "id": 11,
        "question": "Which indigenous community has lived in complete voluntary isolation on North Sentinel Island for tens of thousands of years?",
        "options": ["Inuit people", "Sentinelese people", "Maori people", "Bedouin nomads"],
        "answer": 1,
        "explanation": "The Sentinelese are an uncontacted indigenous hunter-gatherer tribe inhabiting North Sentinel Island in the Andaman archipelago.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Indigenous Sentinelese Heritage:</strong></p>
                <p class='text-slate-300'>The Sentinelese are descendants of the earliest human migrations out of Africa into Asia, maintaining a pure Paleolithic hunter-gatherer way of life completely independent of modern agriculture or metal smelting.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Sentinelese people)</p>
            </div>
        """
    },
    {
        "id": 12,
        "question": "How did the Sentinelese survive the catastrophic December 2004 Indian Ocean Tsunami with zero casualties?",
        "options": [
            "They received mobile phone alerts from coastal weather departments",
            "They read subtle ecological signs (bird alarms, wind shifts, ocean water receding) and climbed to high forest ridges before the waves hit",
            "They stayed inside concrete bunkers",
            "They escaped on motorboats to Sri Lanka"
        ],
        "answer": 1,
        "explanation": "Their deep traditional ecological knowledge enabled them to recognize rapid ocean recession and animal panic as precursors to massive waves, leading them to higher ground in time.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Traditional Ecological Knowledge (TEK) in Action:</strong></p>
                <p class='text-slate-300'>Generational oral wisdom taught islanders that when the sea retreats drastically exposing coral beds, a giant wave is coming. They moved inland to elevated forested ridges and survived completely unscathed.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 13,
        "question": "What is the primary danger that modern outside visitors pose to isolated tribes like the Sentinelese?",
        "options": [
            "Visitors take all the island's timber",
            "Visitors introduce common infectious germs (flu, measles) against which isolated tribes have zero immunological antibodies",
            "Visitors change the island's ocean currents",
            "Visitors bring too much food"
        ],
        "answer": 1,
        "explanation": "Because isolated populations have had no contact with modern diseases, common viruses like the common cold or measles could easily wipe out their entire community.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Immunological Vulnerability:</strong></p>
                <p class='text-slate-300'>Historically, contact between European colonizers and isolated island tribes elsewhere resulted in tragic epidemics. Strict quarantine laws protect the Sentinelese from external pathogens for which they have no genetic immunity.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 14,
        "question": "Where is the Sundarbans, the world's largest mangrove forest, situated?",
        "options": [
            "At the delta where the Ganga and Brahmaputra meet the Bay of Bengal (West Bengal & Bangladesh)",
            "In the desert of Rajasthan",
            "Along the coast of Gujarat",
            "On the peaks of the Himalayas"
        ],
        "answer": 0,
        "explanation": "The Sundarbans spans the immense delta formed by the Ganga, Brahmaputra, and Meghna rivers emptying into the Bay of Bengal across West Bengal and Bangladesh.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Sundarbans Geographical Setting:</strong></p>
                <p class='text-slate-300'>Covering over 10,000 square kilometres, the Sundarbans is a UNESCO World Heritage site and Biosphere Reserve, comprising an intricate network of tidal waterways, mudflats, and salt-tolerant mangrove islands.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A</p>
            </div>
        """
    },
    {
        "id": 15,
        "question": "What type of water is found in the Sundarbans mangrove delta where river freshwater mixes with ocean seawater?",
        "options": ["Pure distilled water", "Brackish water (slightly salty)", "Hot sulfur water", "Frozen glacier water"],
        "answer": 1,
        "explanation": "Water that results from the mixing of river freshwater and ocean saltwater is called brackish water.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Estuarine Brackish Water:</strong></p>
                <p class='text-slate-300'>Brackish water has salinity between 0.5 and 30 parts per thousand—saltier than freshwater rivers but less salty than open ocean seawater (which averages 35 ppt). Mangroves are specially adapted to flourish in brackish conditions.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Brackish water)</p>
            </div>
        """
    },
    {
        "id": 16,
        "question": "What is the biological term for the upright, pencil-like breathing roots that mangroves send above the mud into the air?",
        "options": ["Taproots", "Pneumatophores", "Fibrous roots", "Adventitious tendrils"],
        "answer": 1,
        "explanation": "Pneumatophores are specialized erect roots that grow upward into the air to breathe oxygen in waterlogged, anoxic mud.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Pneumatophore Respiratory Mechanism:</strong></p>
                <p class='text-slate-300'>Derived from the Greek 'pneuma' (breath) and 'pherein' (to bear), pneumatophores grow negatively geotropic (upward against gravity), containing spongy tissue and microscopic surface pores called lenticels for gas exchange.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Pneumatophores)</p>
            </div>
        """
    },
    {
        "id": 17,
        "question": "What microscopic breathing pores are located on the surface of mangrove pneumatophores for gas exchange?",
        "options": ["Stomata", "Lenticels", "Pores", "Chloroplasts"],
        "answer": 1,
        "explanation": "Lenticels are porous spongy openings on the woody surface of pneumatophores that permit air to enter submerged roots during low tide.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Lenticel Gas Exchange Anatomy:</strong></p>
                <p class='text-slate-300'>When the tide retreats, hydrophobic lenticels open to take in atmospheric oxygen, diffusing it down through continuous aerenchyma air channels into the buried root tips. When high tide rises, hydrostatic pressure seals them shut against water inundation.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Lenticels)</p>
            </div>
        """
    },
    {
        "id": 18,
        "question": "Why is the delta mud of the Sundarbans naturally anoxic (devoid of dissolved oxygen gas)?",
        "options": [
            "Because fish eat all the oxygen",
            "Because twice-daily high tides keep the fine clay silt continuously saturated with standing water, preventing atmospheric air from penetrating",
            "Because too many boats sail on the water",
            "Because the sun shines too brightly"
        ],
        "answer": 1,
        "explanation": "Waterlogged conditions and decomposing organic silt in tidal mudflats consume all available oxygen, creating an anaerobic, oxygen-deprived environment in the soil.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Anoxic Soil Chemistry:</strong></p>
                <p class='text-slate-300'>Oxygen diffuses 10,000 times slower through water than through air. Bacterial decomposition of fallen mangrove leaves rapidly exhausts dissolved oxygen in the silt, leaving buried roots starved of air unless equipped with pneumatophores.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 19,
        "question": "What unique swimming ability distinguishes Royal Bengal Tigers in the Sundarbans from other tigers in India?",
        "options": [
            "They cannot swim and always stay in trees",
            "They are powerful swimmers that regularly swim across wide salty tidal channels up to 5 kilometres across",
            "They use logs as rafts to cross rivers",
            "They only swim during full moons"
        ],
        "answer": 1,
        "explanation": "Sundarbans tigers are uniquely adapted to an amphibious tidal life, swimming across broad estuaries with ease to hunt on different islands.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Amphibious Tiger Adaptations:</strong></p>
                <p class='text-slate-300'>Sundarbans tigers possess muscular shoulders and webbed-like toe spacing, allowing them to swim effortlessly against strong ocean currents across rivers 3 to 5 kilometres wide in pursuit of spotted deer and wild boar.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 20,
        "question": "Why do Sundarbans honey collectors (Mouleys) wear human face masks on the back of their heads?",
        "options": [
            "To keep their necks warm during winter",
            "Because tigers are ambush hunters that stalk from behind; seeing human eyes staring back tricks the tiger into abandoning its attack",
            "To scare away wild honey bees",
            "To signal their boat location to other villagers"
        ],
        "answer": 1,
        "explanation": "Tigers rely on ambush from the rear. When they see painted eyes staring directly at them, they believe they have been spotted and forfeit the element of surprise.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Animal Behaviour & Mask Innovation:</strong></p>
                <p class='text-slate-300'>Big cats rarely attack prey that is making direct eye contact with them. In the 1980s, wildlife experts introduced plastic masks worn facing backward; over several years, zero attacks occurred on workers wearing these masks.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },

    # Challenge 3 (Q21 to Q30)
    {
        "id": 21,
        "question": "How many states are collectively referred to as the 'Seven Sisters' of Northeast India?",
        "options": ["5 states", "7 states (Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Tripura)", "8 states", "12 states"],
        "answer": 1,
        "explanation": "The contiguous northeastern states—Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, and Tripura—are known as the Seven Sisters, with Sikkim being their brother state.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Northeast India Geography:</strong></p>
                <p class='text-slate-300'>Connected to the rest of India through the narrow Siliguri Corridor ('Chicken's Neck'), the Seven Sister states and Sikkim form a unique cultural and ecological biogeographic zone.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (7 states)</p>
            </div>
        """
    },
    {
        "id": 22,
        "question": "Which state of Northeast India is celebrated for becoming the world's first 100% certified organic farming state?",
        "options": ["Nagaland", "Sikkim", "Manipur", "Mizoram"],
        "answer": 1,
        "explanation": "Sikkim banned all synthetic chemical pesticides and fertilizers in 2016, becoming the world's first fully organic agricultural state.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Sikkim's Organic Triumph:</strong></p>
                <p class='text-slate-300'>By replacing synthetic fertilizers with compost, bio-pesticides, and traditional rotation farming across 75,000 hectares of farmland, Sikkim demonstrated that agriculture can be 100% sustainable and chemical-free.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Sikkim)</p>
            </div>
        """
    },
    {
        "id": 23,
        "question": "What is the primary ecological purpose of a traditional 'Sacred Grove' in indigenous communities?",
        "options": [
            "A place to build shopping markets",
            "An ancient forest sanctuary preserved by traditional religious taboos where plants and animals are strictly protected from harvesting",
            "A timber farm where trees are cut every year",
            "An artificial botanical zoo"
        ],
        "answer": 1,
        "explanation": "Sacred Groves are virgin forest remnants protected by indigenous communities, acting as invaluable repositories of biodiversity and medicinal flora.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Sacred Groves (Law Kyntang in Meghalaya):</strong></p>
                <p class='text-slate-300'>These ancient forests are protected by customary tribal laws that strictly forbid hunting, logging, or grazing, preserving centuries-old canopy trees and rare orchids in an untouched state.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 24,
        "question": "What is the local Assamese name for the endangered Greater Adjutant Stork protected in the Brahmaputra floodplains?",
        "options": ["Baya", "Hargila", "Neelkanth", "Hornbill"],
        "answer": 1,
        "explanation": "The Greater Adjutant Stork is known as the 'Hargila' in Assam, meaning 'the swallower of bones'.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Hargila (Leptoptilos dubius) Profile:</strong></p>
                <p class='text-slate-300'>This massive wetland stork stands 1.5 m tall with a pale pouch on its neck. Once found across South Asia, over 70% of its surviving global population is now concentrated in the Brahmaputra valley of Assam.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Hargila)</p>
            </div>
        """
    },
    {
        "id": 25,
        "question": "Why is the Hargila stork biologically referred to as nature's 'wetland sanitizer'?",
        "options": [
            "It washes muddy river rocks with water",
            "It feeds on animal carcasses, dead fish, and organic waste, preventing the spread of waterborne diseases and bacterial epidemics",
            "It builds wooden water filters in rivers",
            "It plants lotus seeds in ponds"
        ],
        "answer": 1,
        "explanation": "As large scavengers, Hargila storks consume decaying animal matter and waste, keeping wetlands clean and preventing infectious disease outbreaks.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Ecological Scavenger Importance:</strong></p>
                <p class='text-slate-300'>Scavengers are vital components of nutrient cycles. By consuming rotting biomass that would otherwise pollute drinking water sources, Hargila storks protect both wetland biodiversity and human village health.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 26,
        "question": "What is the name of the celebrated women-led conservation brigade in Assam that protects the Hargila stork?",
        "options": ["Van Devi", "Hargila Army", "Chipko Women", "Green Brigade"],
        "answer": 1,
        "explanation": "The 'Hargila Army', founded by wildlife biologist Dr. Purnima Devi Barman, is an all-women grassroots conservation brigade in Assam.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Hargila Army Movement:</strong></p>
                <p class='text-slate-300'>Comprising over 10,000 rural women, the Hargila Army transformed an outcast bird into a proud cultural symbol by weaving stork motifs on traditional gamusas and protecting nesting colonies.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Hargila Army)</p>
            </div>
        """
    },
    {
        "id": 27,
        "question": "Which indigenous tree species provides the flexible aerial roots used by Khasi communities to form Living Root Bridges?",
        "options": ["Teak", "Indian Rubber Fig (Ficus elastica)", "Sal", "Pine"],
        "answer": 1,
        "explanation": "Ficus elastica (the rubber fig) produces strong aerial roots that can be guided across river gorges to form living suspension bridges.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Ficus elastica Bio-Engineering:</strong></p>
                <p class='text-slate-300'>The rubber fig thrives along steep rocky riverbanks in Meghalaya. Its secondary aerial roots are pliable when young and can be guided through hollow betel palm trunks to span turbulent mountain rivers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Indian Rubber Fig - Ficus elastica)</p>
            </div>
        """
    },
    {
        "id": 28,
        "question": "What is the traditional indigenous name for Living Root Bridges in the Khasi language of Meghalaya?",
        "options": ["Phumdi", "Jingkieng Jri", "Appemidi", "Pneumatophore"],
        "answer": 1,
        "explanation": "In the local Khasi language, a living root bridge is known as 'Jingkieng Jri'.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Jingkieng Jri Living Architecture:</strong></p>
                <p class='text-slate-300'>'Jingkieng' means bridge and 'Jri' refers to the rubber tree. Over 75 living root bridges have been documented across the southern slopes of Meghalaya's Khasi and Jaintia Hills.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Jingkieng Jri)</p>
            </div>
        """
    },
    {
        "id": 29,
        "question": "Why do living root bridges grow stronger over time, unlike man-made concrete or steel bridges?",
        "options": [
            "Because villagers coat them in thick cement every year",
            "Because they are living trees that continually grow thicker roots, absorb nutrients, and heal themselves as decades pass",
            "Because they are taken down and rebuilt every month",
            "Because the water in the river turns to ice"
        ],
        "answer": 1,
        "explanation": "Because they are living biological structures, their roots continue to grow, thicken, and fuse together (anastomosis), increasing load-bearing capacity as decades pass.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Self-Strengthening Bio-Architecture:</strong></p>
                <p class='text-slate-300'>While abiotic materials like steel rust and concrete fractures under heavy monsoonal moisture, living plant roots continually perform secondary radial growth and self-repair, lasting over 500 years.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 30,
        "question": "Where is the famous 'Umshiang Double Decker' living root bridge located in Meghalaya?",
        "options": ["Shillong", "Nongriat village near Cherrapunji (Sohra)", "Dawki", "Tura"],
        "answer": 1,
        "explanation": "The world-famous Double Decker living root bridge is located in Nongriat village, accessible via 3,500 stone steps descending from Tyrna near Sohra.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Umshiang Double Decker Bridge:</strong></p>
                <p class='text-slate-300'>When seasonal monsoon floods regularly submerged the original lower root bridge, Khasi villagers guided a second tier of roots higher up the trunk, creating a magnificent two-story living bridge.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Nongriat village near Cherrapunji)</p>
            </div>
        """
    },

    # Challenge 4 (Q31 to Q40)
    {
        "id": 31,
        "question": "What is the ancient Sanskrit and Marathi name for the Western Ghats mountain chain in peninsular India?",
        "options": ["Himalaya", "Sahyadri", "Aravalli", "Vindhya"],
        "answer": 1,
        "explanation": "The Western Ghats is traditionally known as the Sahyadri mountains ('the benevolent mountains').",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Sahyadri Mountain Heritage:</strong></p>
                <p class='text-slate-300'>Stretching 1,600 km from the Tapti River in Gujarat to Kanyakumari in Tamil Nadu, the Sahyadri ranges formed during the breakup of the ancient supercontinent Gondwana over 150 million years ago.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Sahyadri)</p>
            </div>
        """
    },
    {
        "id": 32,
        "question": "Which endangered arboreal primate with a silver-white mane is endemic to the tropical rainforests of the Western Ghats?",
        "options": ["Rhesus Macaque", "Lion-Tailed Macaque (Macaca silenus)", "Golden Langur", "Chimpanzee"],
        "answer": 1,
        "explanation": "The Lion-Tailed Macaque is an endangered monkey found exclusively in the dense rainforest canopies of the southern Western Ghats.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Lion-Tailed Macaque (Macaca silenus):</strong></p>
                <p class='text-slate-300'>With only an estimated 3,500 individuals remaining in the wild, this shy primate relies on undisturbed continuous rainforest canopies, feeding on fruits, seeds, and insects.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Lion-Tailed Macaque)</p>
            </div>
        """
    },
    {
        "id": 33,
        "question": "What is the name of the multi-coloured, tree-dwelling giant squirrel that serves as the State Animal of Maharashtra?",
        "options": ["Indian Flying Squirrel", "Malabar Giant Squirrel (Ratufa indica / Shekru)", "Himalayan Marmot", "Grey Squirrel"],
        "answer": 1,
        "explanation": "The Malabar Giant Squirrel (locally called Shekru in Marathi) is a giant canopy squirrel and Maharashtra's State Animal.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Malabar Giant Squirrel (Shekru):</strong></p>
                <p class='text-slate-300'>Measuring nearly a metre long from nose to tail tip with striking maroon, buff, and black fur, it builds globe-shaped leaf nests (dreys) high in the canopy and can leap 6 metres between branches.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Malabar Giant Squirrel)</p>
            </div>
        """
    },
    {
        "id": 34,
        "question": "Which major peninsular river of South India takes birth at Trimbakeshwar in the Western Ghats of Maharashtra?",
        "options": ["Ganga", "Godavari River", "Narmada", "Brahmaputra"],
        "answer": 1,
        "explanation": "The Godavari, India's second-longest river, originates from the Brahmagiri hills at Trimbakeshwar in the Western Ghats.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>River Birthplaces in the Ghats:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>Godavari:</strong> Trimbakeshwar (Maharashtra)</li>
                    <li><strong>Krishna:</strong> Mahabaleshwar (Maharashtra)</li>
                    <li><strong>Cauvery:</strong> Talakaveri, Brahmagiri hills (Karnataka)</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Godavari River)</p>
            </div>
        """
    },
    {
        "id": 35,
        "question": "How do dense forests on mountain peaks ensure perennial (year-round) water flow in rivers?",
        "options": [
            "By melting snow quickly in summer",
            "By acting like a sponge: absorbing rainwater during monsoons and releasing it slowly through mountain springs across dry months",
            "By storing river water in wooden barrels",
            "By evaporating all rainfall into clouds"
        ],
        "answer": 1,
        "explanation": "Spongy forest soil and leaf litter slow surface runoff, percolate water into deep aquifers, and maintain clean perennial spring discharge.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Hydrological Sponge Mechanism:</strong></p>
                <p class='text-slate-300'>In a forested watershed, tree canopies intercept raindrops, reducing soil impact. Deep root networks create soil pores that absorb up to 80% of rainfall, filtering it into underground reservoirs that feed rivers through dry summers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 36,
        "question": "What did student citizen scientists in the Western Ghats document in local orchards and forest fringes?",
        "options": [
            "They discovered over 200 distinct local varieties of wild and cultivated mangoes",
            "They found dinosaur eggs in tree trunks",
            "They proved that trees do not need soil to grow",
            "They built wooden aeroplanes"
        ],
        "answer": 0,
        "explanation": "Through community surveys, students documented more than 200 indigenous mango varieties, preserving genetic diversity for agriculture.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Mango Landrace Diversity:</strong></p>
                <p class='text-slate-300'>Indigenous mangoes like Appemidi and wild cultivars possess natural resilience against drought, fungal rot, and pests. Documenting them preserves genetic traits essential for future food security.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A</p>
            </div>
        """
    },
    {
        "id": 37,
        "question": "Why is the tropical evergreen rainforest in Palakkad, Kerala named 'Silent Valley'?",
        "options": [
            "Because tourists are forbidden from making noise",
            "Because loud cicada insects that usually screech in other rainforests are curiously absent here, creating an unusually quiet canopy",
            "Because birds do not sing there",
            "Because there are no running rivers in the valley"
        ],
        "answer": 1,
        "explanation": "Naturalist Robert Wight discovered in 1857 that noisy cicada bugs were virtually absent from this serene forest, leading to the name 'Silent Valley'.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Acoustic Mystery of Silent Valley:</strong></p>
                <p class='text-slate-300'>Cicadas produce sound up to 100 decibels using timbal membranes on their abdomen. Their absence from the main valley creates a remarkably tranquil acoustic atmosphere.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 38,
        "question": "What river was saved from a proposed hydroelectric dam project by the famous 'Save Silent Valley Movement'?",
        "options": ["Periyar River", "Kunthipuzha River", "Pamba River", "Bharathappuzha"],
        "answer": 1,
        "explanation": "The proposed dam on the Kunthipuzha River would have flooded 8.3 sq km of virgin tropical rainforest in Silent Valley.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Kunthipuzha River Preservation:</strong></p>
                <p class='text-slate-300'>The Kunthipuzha flows unpolluted through the entire length of Silent Valley. The public movement prevented dam construction, ensuring the river remains one of India's cleanest flowing waterways.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Kunthipuzha River)</p>
            </div>
        """
    },
    {
        "id": 39,
        "question": "Approximately how many National Parks, Wildlife Sanctuaries, and Tiger Reserves are maintained across the Western Ghats?",
        "options": ["2 areas", "10 areas", "Over 50 protected areas", "Over 500 areas"],
        "answer": 2,
        "explanation": "Over 50 protected areas—including world-famous parks like Periyar, Bandipur, Nagarhole, and Mudumalai—safeguard the Western Ghats ecosystem.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Conservation Network in the Ghats:</strong></p>
                <p class='text-slate-300'>Spanning 39 UNESCO World Heritage sub-clusters, this extensive network of over 50 protected areas forms interconnected ecological corridors essential for elephants, tigers, and hornbills.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: C (Over 50 protected areas)</p>
            </div>
        """
    },
    {
        "id": 40,
        "question": "What is the primary ecological purpose of preserving 'wildlife corridors' between separated forest reserves?",
        "options": [
            "To allow long-distance animal migration for feeding, breeding, and genetic diversity without human-wildlife conflict",
            "To build four-lane expressways through forests",
            "To keep all animals in small cages",
            "To clear forest trees for farming"
        ],
        "answer": 0,
        "explanation": "Wildlife corridors connect fragmented forest islands, allowing elephants, tigers, and deer to migrate safely, preventing genetic inbreeding and reducing road accidents.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Corridor Ecology & Genetic Flow:</strong></p>
                <p class='text-slate-300'>Isolated animal populations suffer genetic inbreeding and local extinction. Natural forest corridors allow gene flow, maintain viable breeding populations, and guide wildlife safely around human highways and towns.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A</p>
            </div>
        """
    }
]

print(f"Mastery quiz questions defined: {len(QUIZ_QUESTIONS)}")


"""
Generate 40 Mastery Challenge Quiz Questions for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
Curiosity curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols.
10 questions per challenge slide:
- Challenge 1 (Slide 17): Questions 1 to 10
- Challenge 2 (Slide 18): Questions 11 to 20
- Challenge 3 (Slide 19): Questions 21 to 30
- Challenge 4 (Slide 20): Questions 31 to 40
"""

QUIZ_QUESTIONS = [
    # Challenge 1 (Questions 1 to 10)
    {
        "id": 1,
        "question": "What famous impression did Wing Commander Rakesh Sharma share when asked how India looked from space in 1984?",
        "options": [
            "He said India was covered in red dust",
            "He quoted 'Sare Jahan Se Achha', noting that borders were invisible from orbit",
            "He said India looked like a square grid",
            "He reported that national boundary lines were clearly painted"
        ],
        "answer": 1,
        "explanation": "Wing Commander Rakesh Sharma famously quoted poet Iqbal's words 'Sare Jahan Se Achha' (Better than all the world), describing India's unified beauty without artificial borders.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. In April 1984, Wing Commander Rakesh Sharma became the first Indian citizen in space aboard Soyuz T-11.<br>2. When Prime Minister Indira Gandhi asked how India appeared from orbit, he immediately replied: <em>'Sare Jahan Se Achha'</em>.<br>3. Space travel offers the 'Overview Effect', where human political boundaries vanish, revealing Earth as one continuous living oasis."
    },
    {
        "id": 2,
        "question": "Why does planet Earth appear predominantly bright blue when viewed from outer space?",
        "options": [
            "Earth's rocks and soil are naturally blue in color",
            "Liquid water in oceans and seas covers roughly 71% of the surface and scatters blue light",
            "Astronauts wear blue tinted visors on their helmets",
            "The sky reflects blue neon city lights from below"
        ],
        "answer": 1,
        "explanation": "Oceans and seas cover approximately 71% of Earth's surface. Water molecules absorb red wavelengths of sunlight and scatter blue light, giving Earth its brilliant blue appearance.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Liquid water covers ~71% of Earth's total surface area (~361 million sq km).<br>2. When white sunlight hits the deep ocean, longer red and orange wavelengths are absorbed, while shorter blue wavelengths are scattered back into space.<br>3. This gives Earth its famous celestial nickname: <strong>The Blue Planet</strong>."
    },
    {
        "id": 3,
        "question": "How fast does the International Space Station (ISS) travel, and how many sunrises and sunsets do astronauts see each day?",
        "options": [
            "100 km/h; 1 sunrise and sunset per week",
            "1,000 km/h; 2 sunrises and sunsets per day",
            "Approximately 28,000 km/h; 16 sunrises and sunsets every 24 hours",
            "100,000 km/h; zero sunrises because it is always daylight"
        ],
        "answer": 2,
        "explanation": "Orbiting at roughly 28,000 km/h, the ISS orbits Earth every 90 minutes. In a 24-hour day, astronauts witness 16 complete orbital revolutions, experiencing 16 sunrises and sunsets.",
        "solution_html": "<strong>Step-by-Step Calculation:</strong><br>1. Orbit time: ~90 minutes = 1.5 hours.<br>2. Number of orbits in 24 hours = 24 ÷ 1.5 = 16 orbits.<br>3. Each orbit passes through Earth's day and night sides, resulting in 16 sunrises and 16 sunsets every 24 hours."
    },
    {
        "id": 4,
        "question": "Which of the following natural elements moves freely across the planet without being stopped by national boundaries?",
        "options": [
            "Atmospheric winds and rainclouds",
            "Ocean currents carrying warm and cold water",
            "Migratory birds and airborne pollen seeds",
            "All of the above"
        ],
        "answer": 3,
        "explanation": "Nature recognizes no human political borders. Winds, rain clouds, ocean waters, migratory species, and plant seeds circulate across the globe as part of unified Earth systems.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. The atmosphere is a continuous fluid layer circulating around the globe.<br>2. Oceans connect into a single world hydrosphere driven by thermohaline circulation.<br>3. Living creatures migrate across thousands of kilometres following seasons, proving that Earth's biosphere is boundless."
    },
    {
        "id": 5,
        "question": "Where do rosy starlings spend their summer breeding months before flying to India in winter?",
        "options": [
            "The grasslands and steppes of Southern Russia, Kazakhstan, and Mongolia",
            "The Sahara Desert in North Africa",
            "The Amazon Rainforest in Brazil",
            "The glaciers of Antarctica"
        ],
        "answer": 0,
        "explanation": "Rosy starlings breed across the temperate steppes of Southern Russia, Central Asia, and Mongolia during summer, and migrate south to India to escape freezing winter temperatures.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. In summer (May–July), Central Asian grasslands provide abundant insects for rosy starlings to rear chicks.<br>2. By September and October, freezing blizzards cover the steppes with snow, hiding food.<br>3. Flocks fly south across the Himalayas into sunny India, arriving in Gujarat, Rajasthan, and Peninsular India."
    },
    {
        "id": 6,
        "question": "Why are migrating rosy starlings considered exceptional friends and allies to Indian farmers?",
        "options": [
            "They plant cereal seeds in straight furrows",
            "They devour massive swarms of destructive crop pests like locusts and grasshoppers",
            "They dig drainage canals through paddy fields",
            "They guard farm storehouses from thieves"
        ],
        "answer": 1,
        "explanation": "Rosy starlings are voracious insect eaters. A single flock can consume millions of locusts, grasshoppers, and caterpillars daily, protecting agricultural crops naturally.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Locust swarms can devour hundreds of tonnes of standing green crops in a matter of hours.<br>2. Rosy starlings target these swarms as their primary food source, providing biological pest control.<br>3. This natural service saves millions of rupees in crop yields and reduces reliance on chemical pesticides."
    },
    {
        "id": 7,
        "question": "What is the ancient Sanskrit origin and meaning of the word 'Yoga'?",
        "options": [
            "From 'Yodha', meaning a warrior in battle",
            "From 'Yuj', meaning to join, unite, or live in harmony",
            "From 'Yuga', meaning a thousand years of sleep",
            "From 'Yantra', meaning an iron machine"
        ],
        "answer": 1,
        "explanation": "The word 'Yoga' is derived from the Sanskrit root 'Yuj', which means to unite or bind together—symbolizing the union of mind, body, spirit, and nature.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Root: Sanskrit <em>'Yuj'</em> = to yoke, join, or unite.<br>2. Purpose: Harmony of body (asanas), breath (pranayama), and mind (dhyana).<br>3. Historical Depth: Practiced in India for more than 3,000 years and documented in ancient Vedic and Patanjali texts."
    },
    {
        "id": 8,
        "question": "Why did the United Nations choose June 21 as the International Day of Yoga?",
        "options": [
            "It is the birthday of the first UN Secretary General",
            "It is the Summer Solstice, the longest day of the year in the Northern Hemisphere symbolizing light and vitality",
            "It is the date when yoga was first written down in a book",
            "It marks the start of the winter freeze in Antarctica"
        ],
        "answer": 1,
        "explanation": "June 21 is the Summer Solstice in the Northern Hemisphere—the day with the longest duration of daylight—symbolizing energy, vitality, and alignment with the Sun.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. In 2014, India proposed June 21 at the UN General Assembly.<br>2. June 21 is astronomical Summer Solstice in the Northern Hemisphere (Earth's North Pole tilts closest to the Sun).<br>3. Across global traditions, this solstice marks illumination and transitions toward holistic wellness."
    },
    {
        "id": 9,
        "question": "Which indigenous spice provided pungent heat and warmth to traditional Indian food before chillies were introduced?",
        "options": [
            "Red chilli flakes",
            "Black pepper from the Western Ghats of Kerala and dry ginger",
            "Jalapeno peppers",
            "Paprika paste"
        ],
        "answer": 1,
        "explanation": "Black pepper (Piper nigrum) native to the rainforests of Kerala's Western Ghats, along with dry ginger and long pepper (Pippali), provided warmth to ancient Indian food.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Black pepper was so prized in the ancient world that Roman traders called it 'Black Gold'.<br>2. Chillies were completely unknown in Asia, Europe, and Africa before maritime contact with the Americas.<br>3. Indian curries historically balanced black pepper with ginger, mustard, and cumin for heat."
    },
    {
        "id": 10,
        "question": "From which continent did chilli plants (genus Capsicum) originally come before spreading globally?",
        "options": [
            "Australia",
            "Central and South America",
            "Antarctica",
            "Northern Europe"
        ],
        "answer": 1,
        "explanation": "Chillies originated in Central and South America (regions of Mexico, Bolivia, and Peru) and were brought to India by Portuguese maritime traders roughly 400 to 500 years ago.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Wild ancestors of chillies were cultivated in the Americas over 6,000 years ago.<br>2. Following 15th-century Atlantic voyages, European sea traders carried seeds to Asia.<br>3. In India, Portuguese merchants introduced chillies through Goa on the Malabar Coast in the 1500s."
    },

    # Challenge 2 (Questions 11 to 20)
    {
        "id": 11,
        "question": "Which culture first developed the technology to boil sugarcane juice and crystallize it into sugar?",
        "options": [
            "Ancient Roman glassmakers",
            "Ancient Indian farmers and sugar artisans",
            "Viking sea raiders",
            "Egyptian pyramid architects"
        ],
        "answer": 1,
        "explanation": "Ancient India was the first civilization to master the extraction of sugarcane juice, clarifying and boiling it into jaggery (gur) and crystalline sugar (sarkara).",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Sugarcane was indigenous to tropical South and Southeast Asia.<br>2. Indian artisans developed crushing presses and open-pan evaporators to make solid jaggery.<br>3. By the Gupta period (c. 350 CE), Indians developed crystal sugar (<em>Sarkara</em>), sparking global trade."
    },
    {
        "id": 12,
        "question": "What is the Sanskrit origin of the modern English words 'sugar' and 'candy'?",
        "options": [
            "From Sanskrit 'Sarkara' (sugar crystals) and 'Khanda' (candied sugar chunks)",
            "From Greek words meaning white flour",
            "From Latin words for sweet honey",
            "From Portuguese words for sweet sugarcane stems"
        ],
        "answer": 0,
        "explanation": "The English word 'sugar' comes via Arabic 'sukkar' from Sanskrit 'Sarkara'. The word 'candy' comes via Arabic 'qandi' from Sanskrit 'Khanda' (sugar piece).",
        "solution_html": "<strong>Linguistic Lineage:</strong><br>1. Sanskrit <em>Sarkara</em> → Persian <em>Shakar</em> → Arabic <em>Al-Sukkar</em> → Spanish <em>Azúcar</em> / English <em>Sugar</em>.<br>2. Sanskrit <em>Khanda</em> (broken sugar pieces) → Persian <em>Qand</em> → Arabic <em>Qandi</em> → English <em>Candy</em>.<br>3. This linguistic trail documents how Indian sugar technology travelled worldwide."
    },
    {
        "id": 13,
        "question": "From which North American indigenous civilization did the marigold (Genda Phool) originate before coming to India?",
        "options": [
            "The Aztec people of Mexico",
            "The Inuit of the Arctic",
            "The Aboriginal tribes of Australia",
            "The Maori of New Zealand"
        ],
        "answer": 0,
        "explanation": "Marigolds were cultivated by the Aztec civilization in Mexico, where they were revered as 'Cempasúchil' and used in religious ceremonies and the Day of the Dead festival.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. Genus <em>Tagetes</em> (marigold) is native to Central and South America, especially Mexico.<br>2. Aztecs named it <em>Cempohualxochitl</em> ('twenty flowers'), using it as spiritual offerings and medicine.<br>3. Spanish and Portuguese galleons transported seeds across oceans to India during the 1500s."
    },
    {
        "id": 14,
        "question": "Why do Indian vegetable gardeners frequently plant marigolds along borders and between rows of crops?",
        "options": [
            "Marigold flowers make tomatoes grow three times faster",
            "Marigold roots and pungent aromatic leaves naturally deter soil nematodes and insect pests",
            "Marigolds absorb all rainwater so vegetables stay dry",
            "Marigolds scare birds away because of their color"
        ],
        "answer": 1,
        "explanation": "Marigolds produce chemical exudates (such as alpha-terthienyl) in their roots and strong aromatic terpenes in their foliage that repel harmful nematodes and crop-damaging insects.",
        "solution_html": "<strong>Scientific Principle (Companion Planting):</strong><br>1. Marigold roots excrete biochemical compounds that suppress root-knot nematodes in the soil.<br>2. Their bright orange blossoms attract beneficial predatory insects like hoverflies and ladybugs.<br>3. This makes marigolds a traditional, chemical-free form of biological pest control."
    },
    {
        "id": 15,
        "question": "Which Indian cattle breeds were brought to Brazil, and why did they thrive better than European cattle?",
        "options": [
            "Gir, Kankrej, and Ongole; because their sweat glands and tick immunity helped them handle tropical heat",
            "Jersey and Holstein; because they preferred freezing mountain blizzards",
            "Water buffaloes; because they could swim across the Atlantic Ocean",
            "Tibetan yaks; because they had thick woolly coats"
        ],
        "answer": 0,
        "explanation": "Indigenous Indian Zebu breeds like Gir, Kankrej, and Ongole evolved in tropical climates. Their heat-reflecting coats, abundant sweat glands, and tick resistance made them thrive in Brazil.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. European cattle breeds suffered severe heat stress, low fertility, and tick-borne diseases in Brazil's tropical pasturelands.<br>2. Indian Zebu cattle (<em>Bos indicus</em>) have loose pendulous skin, large dewlaps for heat dissipation, and dense sweat glands.<br>3. Today, over 75% of Brazil's cattle have Indian genetic lineage, and Ongole cattle are known there as 'Nelore'."
    },
    {
        "id": 16,
        "question": "What is the ancient Sanskrit meaning of 'Vasudhaiva Kutumbakam'?",
        "options": [
            "Earth belongs only to kings and rulers",
            "The entire world is one unified family",
            "Every country should live in complete isolation",
            "Nature should be cleared to build concrete roads"
        ],
        "answer": 1,
        "explanation": "'Vasudhaiva Kutumbakam' comes from the Maha Upanishad and means 'The World is One Family', recognizing the universal kinship of all human beings and living creatures.",
        "solution_html": "<strong>Step-by-Step Breakdown:</strong><br>1. <em>Vasudha</em> = Earth / The ground.<br>2. <em>Eva</em> = Indeed / Truly.<br>3. <em>Kutumbakam</em> = One family / Household.<br>4. Conclusion: All living beings sharing our planetary home are part of one cosmic family."
    },
    {
        "id": 17,
        "question": "What is the official motto of the Indian Ministry of Environment, Forest and Climate Change (MoEFCC)?",
        "options": [
            "Satyameva Jayate (Truth Alone Triumphs)",
            "Prakriti Rakshati Rakshita (Nature Protects if She is Protected)",
            "Shramena Sarvam Sadhyam (Hard Work Conquers All)",
            "Vidya Dadati Vinayam (Education Imparts Humility)"
        ],
        "answer": 1,
        "explanation": "The MoEFCC motto is 'Prakriti Rakshati Rakshita', meaning 'Nature Protects if She is Protected', highlighting our duty to care for the environment that sustains us.",
        "solution_html": "<strong>Ethical Principle:</strong><br>1. In Sanskrit: <em>प्रकृतिः रक्षति रक्षिता</em> (Prakriti Rakshati Rakshita).<br>2. Meaning: When humanity preserves forests, pure water, clean air, and living ecosystems, nature reciprocates by shielding us from climatic disasters, drought, and disease."
    },
    {
        "id": 18,
        "question": "Which everyday pantry items originated in the Americas and were unknown in ancient Europe, Asia, and Africa?",
        "options": [
            "Potatoes, tomatoes, maize (corn), and peanuts",
            "Wheat, barley, lentils, and mustard",
            "Rice, black pepper, and sugarcane",
            "Apples, pears, and garlic"
        ],
        "answer": 0,
        "explanation": "Potatoes, tomatoes, maize, chillies, peanuts, cashews, and pineapples were indigenous to the Americas and reached Asia and Europe only after 1492 via the Columbian Exchange.",
        "solution_html": "<strong>Global Crop Mapping:</strong><br>1. Americas: Potatoes, tomatoes, chillies, maize, pineapples, cashews, cacao (chocolate), peanuts.<br>2. India: Rice, sugarcane, black pepper, mangoes, bananas, cardamoms.<br>3. China: Tea, paper, silk, peaches.<br>4. West Asia: Wheat, barley, chickpeas, dates."
    },
    {
        "id": 19,
        "question": "How did ancient Indians write sacred scriptures and books before paper was introduced from China?",
        "options": [
            "On dried palm leaves (Tala-patra) and Himalayan birch bark (Bhurja-patra)",
            "On metal sheets using laser cutters",
            "On plastic synthetic tablets",
            "On frozen blocks of ice"
        ],
        "answer": 0,
        "explanation": "Before paper-making arrived along trade routes from China, ancient Indian scholars preserved knowledge on treated palm leaves (Tala-patra) and birch tree bark (Bhurja-patra).",
        "solution_html": "<strong>Historical Writing Surfaces:</strong><br>1. In Southern India: Dried, polished leaves of the Palmyra palm (<em>Tala-patra</em>) etched with iron styluses and smeared with soot.<br>2. In Northern India: Paper-like peeled bark of Himalayan birch trees (<em>Bhurja-patra</em>).<br>3. Paper-making invented in China (c. 105 CE) eventually replaced these organic plant sheets."
    },
    {
        "id": 20,
        "question": "Why is Earth often called the 'Goldilocks Planet' in space science?",
        "options": [
            "Its rocks are made entirely of pure 24-carat gold",
            "It orbits at just the right distance from the Sun—not too hot and not too cold—allowing liquid water and life to flourish",
            "It has three moons that look like golden bowls",
            "Astronauts discovered golden fairy tales on its surface"
        ],
        "answer": 1,
        "explanation": "Earth orbits within the circumstellar habitable zone ('Goldilocks Zone') where temperatures are neither too boiling hot (like Venus) nor freezing cold (like Mars), permitting liquid water.",
        "solution_html": "<strong>The Habitable Zone:</strong><br>1. Too close to Sun: Water boils away into steam (runaway greenhouse effect on Venus).<br>2. Too far from Sun: Water freezes into solid ice (frozen deserts of Mars).<br>3. Just right: Earth's orbital distance (~150 million km) maintains stable liquid oceans, shielding life."
    },

    # Challenge 3 (Questions 21 to 30)
    {
        "id": 21,
        "question": "What is the 'Overview Effect' reported by astronauts when they gaze back at Earth from space?",
        "options": [
            "Dizziness caused by staring at artificial satellite dishes",
            "A deep cognitive shift realizing Earth's fragility, unity, and absence of national borders",
            "The inability to remember what continent they came from",
            "Fear of dark space monsters"
        ],
        "answer": 1,
        "explanation": "The Overview Effect is a well-documented psychological experience where viewing Earth as a fragile, borderless blue marble fosters deep planetary empathy and environmental devotion.",
        "solution_html": "<strong>Cognitive Shift:</strong><br>1. Term coined by space philosopher Frank White in 1987.<br>2. Seeing Earth without lines makes national conflicts appear trivial compared to our shared planetary survival.<br>3. Inspires astronauts to become lifelong ambassadors for global peace and environmental protection."
    },
    {
        "id": 22,
        "question": "What essential biological process do green plants perform that replenishes oxygen for all animals and humans on Earth?",
        "options": [
            "Photosynthesis (using sunlight, carbon dioxide, and water to produce food and oxygen)",
            "Fermentation of sugar into vinegar",
            "Condensation of water droplets on leaves",
            "Evaporation of groundwater into clouds"
        ],
        "answer": 0,
        "explanation": "Through photosynthesis, green plants and ocean phytoplankton convert solar light, water, and carbon dioxide into glucose, releasing vital oxygen into the atmosphere.",
        "solution_html": "<strong>Photosynthesis Formula:</strong><br>Carbon Dioxide + Water + Sunlight → Glucose (Plant Food) + Oxygen (O₂).<br>Plants and ocean phytoplankton produce virtually all the breathable oxygen in Earth's atmosphere."
    },
    {
        "id": 23,
        "question": "What is the single most important difference between Earth and all other known planets in our solar system?",
        "options": [
            "Earth is the largest planet in the solar system",
            "Earth is the only known planet that harbors living organisms and flowing surface liquid water",
            "Earth is the only planet with a rocky solid ground",
            "Earth has more moons than Jupiter and Saturn"
        ],
        "answer": 1,
        "explanation": "Earth is unique because it possesses a stable liquid water hydrosphere, an oxygen-rich atmosphere, a protective magnetic field, and a thriving biosphere.",
        "solution_html": "<strong>Planetary Uniqueness:</strong><br>1. Jupiter and Saturn are gas giants without solid surfaces.<br>2. Mercury and Venus are scorching barren wastelands.<br>3. Earth is the sole cosmic oasis where conditions support plants, animals, fungi, microbes, and human civilization."
    },
    {
        "id": 24,
        "question": "How do migrating birds like rosy starlings and Arctic terns navigate across thousands of kilometres without getting lost?",
        "options": [
            "They use smartphone mapping applications",
            "They sense Earth's magnetic field, observe the Sun and stars, and recognize geographical landmarks",
            "They follow commercial airline flight paths",
            "They stop to ask directions from mountain climbers"
        ],
        "answer": 1,
        "explanation": "Migratory birds possess specialized internal magneto-receptors to sense Earth's magnetic field, alongside celestial navigation (sun and star positions) and memory of coastlines and river valleys.",
        "solution_html": "<strong>Avian Navigation Mechanisms:</strong><br>1. <strong>Magnetoreception:</strong> Proteins called cryptochromes in birds' eyes detect Earth's geomagnetic lines.<br>2. <strong>Celestial Clues:</strong> Tracking the Sun's polarized light during day and star constellations by night.<br>3. <strong>Landscape Memory:</strong> Recognizing river bends, mountain passes, and coastlines across generations."
    },
    {
        "id": 25,
        "question": "What is a 'murmuration' in bird behavior?",
        "options": [
            "A bird singing alone inside a cage",
            "A breathtaking aerial dance where thousands of starlings fly and swirl together in synchronized harmony",
            "A bird sleeping with its head tucked under its wing",
            "A bird building a nest out of clay and pebbles"
        ],
        "answer": 1,
        "explanation": "A murmuration is the synchronized, fluid flocking behavior of thousands of starlings flying together, creating swirling shape-shifting clouds in the evening sky.",
        "solution_html": "<strong>Science of Murmurations:</strong><br>1. Starlings fly in tightly packed groups of thousands to confuse flying predators like falcons and hawks.<br>2. Each starling mirrors the velocity and direction of its 7 nearest neighbors.<br>3. This localized response ripples through the entire flock at high speed, creating hypnotic waves across the sky."
    },
    {
        "id": 26,
        "question": "Which international organization declared June 21 as the International Day of Yoga in December 2014?",
        "options": [
            "The International Olympic Committee",
            "The United Nations General Assembly (UNGA)",
            "The World Wildlife Fund",
            "The International Astronomical Union"
        ],
        "answer": 1,
        "explanation": "The United Nations General Assembly adopted resolution 69/131 in December 2014, officially proclaiming June 21 as the International Day of Yoga.",
        "solution_html": "<strong>UN Resolution 69/131:</strong><br>1. Proposed by India during the 69th session of the UN General Assembly.<br>2. Received overwhelming global consensus with 177 co-sponsoring member countries.<br>3. The first global celebration took place on June 21, 2015, across over 190 nations."
    },
    {
        "id": 27,
        "question": "What happens when humans produce excessive non-biodegradable single-use plastic waste?",
        "options": [
            "It turns into sweet sugar crystals in the soil",
            "It persists for hundreds of years, polluting oceans, choking marine life, and breaking into toxic microplastics",
            "It evaporates into harmless steam",
            "It helps deep-sea fish breathe underwater"
        ],
        "answer": 1,
        "explanation": "Petrochemical plastics do not biodegrade naturally. They persist for centuries, fragmenting into microplastics that enter food chains and poison terrestrial and marine wildlife.",
        "solution_html": "<strong>The Plastic Menace:</strong><br>1. Synthetic plastics take between 400 to 1,000 years to break down.<br>2. Over 8 million tonnes of plastic waste enter global oceans annually, ingested by turtles, whales, and seabirds.<br>3. Earth Guardians practice the 5 Rs: Refuse, Reduce, Reuse, Repurpose, and Recycle."
    },
    {
        "id": 28,
        "question": "Why is the preservation of mangrove forests in coastal regions like the Sundarbans crucial for human communities?",
        "options": [
            "Mangrove trees act as natural shock absorbers that blunt cyclonic storm surges and prevent coastal erosion",
            "Mangroves produce sweet sugarcane juice naturally",
            "Mangroves prevent sunlight from reaching the ground",
            "Mangroves make seawater freeze into ice cubes"
        ],
        "answer": 0,
        "explanation": "Dense mangrove root systems trap sediments, absorb fierce tidal waves, buffer cyclonic sea surges, and provide breeding nurseries for fish and crabs.",
        "solution_html": "<strong>Coastal Ecological Service:</strong><br>1. Mangrove stilt roots and breathing pneumatophores anchor muddy coastlines against fierce waves.<br>2. During Bay of Bengal cyclones, mangrove belts reduce wave height and velocity, protecting inland villages from floods.<br>3. Demonstrates the motto: <em>Prakriti Rakshati Rakshita</em> (Protecting mangroves protects humans)."
    },
    {
        "id": 29,
        "question": "What simple kitchen practice transforms fruit and vegetable peels into nutrient-rich organic plant food?",
        "options": [
            "Burning them with kerosene",
            "Composting (allowing organic waste to naturally decompose with air, moisture, and soil microbes)",
            "Flushing them down bathroom drains",
            "Sealing them tightly in plastic shopping bags"
        ],
        "answer": 1,
        "explanation": "Composting breaks down wet organic waste (peels, leaves, food scraps) into dark, crumbly organic compost (humus) that enriches garden soil without chemical fertilizers.",
        "solution_html": "<strong>Science of Composting:</strong><br>1. Microorganisms (bacteria, fungi, actinomycetes) and earthworms consume organic plant matter.<br>2. They convert complex carbon and nitrogen into bioavailable soil nutrients (NPK).<br>3. Composting reduces municipal landfill burden and prevents methane emissions."
    },
    {
        "id": 30,
        "question": "Which animal group is responsible for pollinating over 75% of global flowering plant and food crop species?",
        "options": [
            "Insects like honeybees, butterflies, moths, and hoverflies",
            "Polar bears and arctic foxes",
            "Deep-sea sharks and octopuses",
            "Underground earthworms and termites"
        ],
        "answer": 0,
        "explanation": "Insect pollinators—especially bees, butterflies, moths, and beetles—transfer pollen between flowers, allowing fruits, vegetables, seeds, and nuts to develop.",
        "solution_html": "<strong>Pollination Ecology:</strong><br>1. One out of every three bites of food humans eat depends directly on animal pollinators.<br>2. Bees visit flowers for nectar and pollen, unintentionally dusting female stigmas with male pollen grains.<br>3. Protecting flower habitats from pesticide toxicity directly safeguards global food security."
    },

    # Challenge 4 (Questions 31 to 40)
    {
        "id": 31,
        "question": "How does turning off unused lights and fans in classrooms contribute to protecting the global environment?",
        "options": [
            "It cleans the chalkboard automatically",
            "It saves electricity, reducing the burning of coal in thermal power stations and lowering air pollution",
            "It makes school bells ring louder",
            "It prevents winds from blowing outside"
        ],
        "answer": 1,
        "explanation": "Most electricity is generated by burning fossil fuels like coal. Saving power directly reduces coal combustion, greenhouse gas emissions, and acid rain.",
        "solution_html": "<strong>Energy Connection:</strong><br>1. Coal thermal power plants burn coal to produce high-pressure steam that drives electric generators.<br>2. Coal combustion releases huge volumes of carbon dioxide (CO₂), sulfur dioxide, and fly ash.<br>3. Conserving kilowatt-hours at school directly reduces coal burnt and preserves clean planetary air."
    },
    {
        "id": 32,
        "question": "Which of the following describes the 'water footprint' of an everyday item?",
        "options": [
            "The puddle left behind after dropping an ice cube on the floor",
            "The total volume of freshwater consumed directly and indirectly to manufacture, process, and deliver that item",
            "The weight of a glass of drinking water",
            "The depth of water inside an aquarium"
        ],
        "answer": 1,
        "explanation": "A water footprint measures the total volume of freshwater utilized across the complete supply chain to produce goods, food, and services.",
        "solution_html": "<strong>Water Footprint Concept:</strong><br>1. A single cotton shirt requires ~2,700 litres of water (growing cotton, dyeing, finishing).<br>2. One kilogram of polished rice can require ~2,500 to 5,000 litres of irrigation water.<br>3. Avoiding waste and reusing clothes and food directly conserves precious planetary freshwater."
    },
    {
        "id": 33,
        "question": "In the interconnected web of life, what is the role of decomposers like fungi, bacteria, and earthworms?",
        "options": [
            "They hunt live birds in forest treetops",
            "They break down dead leaves and animal remains, recycling essential mineral nutrients back into the soil for plants",
            "They stop rain clouds from falling",
            "They produce synthetic plastic bags in the ground"
        ],
        "answer": 1,
        "explanation": "Decomposers are nature's cleanup crew and recyclers. They break down organic matter, returning minerals (nitrogen, phosphorus, potassium) to the soil for green plants to reuse.",
        "solution_html": "<strong>Nutrient Recycling:</strong><br>1. Without decomposers, dead leaves and organisms would pile up indefinitely without rotting.<br>2. Decomposers convert complex biological molecules into simple mineral nutrients.<br>3. This closed-loop circular economy is nature's original zero-waste model."
    },
    {
        "id": 34,
        "question": "Why is planting native tree species (like Neem, Banyan, and Peepal) superior to planting exotic ornamental trees in India?",
        "options": [
            "Native species require chemical fertilizers every morning",
            "Native trees have adapted over thousands of years to local soils and rainfall, supporting local birds, bees, and insects",
            "Native trees do not drop any leaves during the year",
            "Exotic trees produce gold coins instead of fruit"
        ],
        "answer": 1,
        "explanation": "Native trees are adapted to local climate conditions, consume less water once established, and co-evolved with native birds, caterpillars, and pollinators that depend on them for food.",
        "solution_html": "<strong>Ecological Harmony:</strong><br>1. A native Banyan or Peepal tree can support dozens of species of birds, bats, insects, and epiphytes.<br>2. Exotic ornamental trees often cannot support local caterpillar species, disrupting bird food supplies.<br>3. Native species possess deep root systems that recharge groundwater and withstand severe monsoons."
    },
    {
        "id": 35,
        "question": "What is the primary message of the ancient text quote: 'अयं निजः परो वेति गणना लघुचेतसाम् । उदारचरितानां तु वसुधैव कुटुम्बकम् ॥'?",
        "options": [
            "Only people from your own neighbourhood should be helped",
            "Dividing beings into 'mine' versus 'theirs' is narrow-minded; for the magnanimous, the entire Earth is one family",
            "Space exploration is a waste of time",
            "All animals should be kept in city cages"
        ],
        "answer": 1,
        "explanation": "This verse from the Maha Upanishad teaches that narrow minds distinguish between 'ours' and 'strangers', while noble, generous hearts embrace the entire world as one loving family.",
        "solution_html": "<strong>Philosophical Depth:</strong><br>1. <em>Laghucetasam</em> = Narrow, petty thinking.<br>2. <em>Udaracaritanam</em> = Noble, generous, open-hearted individuals.<br>3. This philosophy teaches universal empathy, transcending artificial barriers of nation, language, and species."
    },
    {
        "id": 36,
        "question": "What is the ozone layer, and why is its protection vital for all life on Earth?",
        "options": [
            "A layer of ocean water that freezes into icebergs",
            "A high-altitude gas shield in the stratosphere that absorbs harmful solar ultraviolet (UV) radiation",
            "A ring of space rocks orbiting Earth",
            "A layer of green moss covering trees"
        ],
        "answer": 1,
        "explanation": "The ozone layer (O₃) in the stratosphere acts as a planetary sunblock, absorbing dangerous solar ultraviolet rays that would otherwise cause skin cancer, cataracts, and crop destruction.",
        "solution_html": "<strong>The Atmospheric Sunscreen:</strong><br>1. Located in the stratosphere (15 to 35 km above sea level).<br>2. Absorbs 97% to 99% of medium-frequency ultraviolet radiation from the Sun.<br>3. The global Montreal Protocol phased out ozone-depleting CFCs, demonstrating how international cooperation can heal planetary wounds."
    },
    {
        "id": 37,
        "question": "How does rainwater harvesting help communities care for our shared home?",
        "options": [
            "It turns rainwater into cooking oil",
            "It captures clean monsoon run-off from rooftops to replenish drying underground aquifers and reduce municipal demand",
            "It stops monsoon clouds from raining on neighbouring cities",
            "It causes road flooding in school parking lots"
        ],
        "answer": 1,
        "explanation": "Rainwater harvesting collects clean rain from rooftops and open grounds, directing it into storage tanks or recharge pits that replenish groundwater tables.",
        "solution_html": "<strong>Groundwater Recharge:</strong><br>1. Concrete cities cause rapid water runoff into storm drains, preventing groundwater percolation.<br>2. Rainwater harvesting filters rain and injects it back into subterranean aquifers.<br>3. This ensures sustainable drinking water availability through dry summer months."
    },
    {
        "id": 38,
        "question": "What is the global significance of the motto chosen for India's G20 Presidency: 'One Earth • One Family • One Future'?",
        "options": [
            "It encouraged every country to print identical paper currency",
            "It united global leaders around shared climate responsibility, sustainable growth, and universal brotherhood rooted in Vasudhaiva Kutumbakam",
            "It mandated that all nations celebrate only one national festival",
            "It proposed building a giant glass dome over the equator"
        ],
        "answer": 1,
        "explanation": "The theme highlighted that all nations share a single planet, form an interconnected family, and must collaborate on climate, energy, and peace for a shared sustainable future.",
        "solution_html": "<strong>G20 Global Consensus:</strong><br>1. <strong>One Earth:</strong> Protecting biodiversity, accelerating green transition, and halting land degradation.<br>2. <strong>One Family:</strong> Inclusive human-centric development and equitable healthcare.<br>3. <strong>One Future:</strong> Empowering youth, bridging digital divides, and safeguarding future generations."
    },
    {
        "id": 39,
        "question": "Why is the phrase 'There is no Planet B' widely used by environmental scientists and youth climate activists?",
        "options": [
            "Because astronomers forgot to name the letter B in the alphabet",
            "Because Earth is our only habitable home in the universe, and we have no other planet to escape to if we destroy it",
            "Because Mars is made entirely of red candy",
            "Because all other planets are already fully populated"
        ],
        "answer": 1,
        "explanation": "'There is no Planet B' emphasizes the utter irreplaceable uniqueness of Earth's life-support systems, reminding humanity that protecting Earth is our non-negotiable imperative.",
        "solution_html": "<strong>Planetary Fragility:</strong><br>1. Even the closest planets (Mars and Venus) lack breathable oxygen, liquid oceans, fertile soils, and atmospheric protection.<br>2. Terraforming or colonizing other worlds is not a viable evacuation plan for billions of people.<br>3. Therefore, nurturing and healing Earth is humanity's paramount moral and scientific priority."
    },
    {
        "id": 40,
        "question": "What final commitment should every young scientist and student make as a custodian of our shared home?",
        "options": [
            "To ignore pollution as long as someone else cleans it up",
            "To live mindfully, conserve resources, plant trees, respect all life forms, and champion harmony across humanity and nature",
            "To build concrete walls to keep wild animals out of the world",
            "To use disposable plastic bottles every single day"
        ],
        "answer": 1,
        "explanation": "Every student can be an active Earth Guardian by practicing conservation, embracing unity in diversity, respecting all living creatures, and preserving our planet for generations to come.",
        "solution_html": "<strong>The Earth Guardian's Pledge:</strong><br>1. I will conserve water, electricity, and food in my daily life.<br>2. I will refuse single-use plastics and plant trees to heal the soil.<br>3. I will live with kindness toward all people, animals, and plants, honouring the timeless wisdom: <em>Vasudhaiva Kutumbakam</em>."
    }
]

print("Mastery Quiz Questions (40 questions) authored successfully.")


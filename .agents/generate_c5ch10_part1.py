"""
Generate Slides 1 to 8 for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
Curiosity curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols.
"""

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "One Shared Home",
        "subtitle": "Cosmic Perspective from the International Space Station",
        "concept_html": """
            <p class="mb-3">When astronauts journey beyond Earth's atmosphere, their view of our world changes forever. Wing Commander Rakesh Sharma, the first Indian in space aboard Soyuz T-11 in 1984, famously described India from orbit as <em>'Sare Jahan Se Achha'</em>, looking seamless and unified without borders. Decades later, Group Captain Shubhanshu Shukla, aboard the International Space Station (ISS), reiterated this breathtaking truth: from space, Earth appears not as a map of separate countries, but as a single, shining home shared by all living beings.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-sky-400 block mb-1">Orbiting at 28,000 km/h</span>
                    <p class="text-xs text-slate-300">The ISS circles Earth every 90 minutes. Astronauts witness 16 sunrises and sunsets every single day, seeing continents merge seamlessly into blue oceans.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">The Overview Effect</span>
                    <p class="text-xs text-slate-300">A profound psychological shift experienced by space travellers when seeing Earth hanging in the blackness of space as an interconnected, fragile oasis of life.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Human-drawn boundaries, fences, and political borders are completely invisible from space. All creatures, mountains, rivers, and atmosphere belong to one indivisible planetary home.</p>
        """,
        "spoken_text": "Look up into the vastness of space. When Indian astronauts like Wing Commander Rakesh Sharma and Group Captain Shubhanshu Shukla looked down at Earth from orbit, they did not see lines, fences, or borders. They saw a brilliant, swirling blue and white sphere floating serenely in the deep dark ocean of space. From 400 kilometres above, cities and territorial divides vanish completely. We are all passengers and caretakers travelling together on one shared cosmic home.",
        "checkpoints": [
            {
                "question": "What did astronauts notice about national borders when viewing Earth from the International Space Station?",
                "options": [
                    "Borders appear as bright glowing lines across continents",
                    "Borders and boundaries are completely invisible from space",
                    "Borders can only be seen during night-time with city lights",
                    "Borders are visible as tall concrete walls"
                ],
                "correct": 1,
                "explanation": "From space, national borders and political divisions do not exist. Earth appears as one continuous, beautiful ecosystem of land, cloud, and ocean.",
                "study_insight": "Astronauts describe this realization as the 'Overview Effect'—recognizing our shared planetary identity beyond artificial divisions."
            },
            {
                "question": "How often does the International Space Station orbit Earth, giving astronauts multiple views of our shared home?",
                "options": [
                    "Once every 24 hours",
                    "Once every 7 days",
                    "Approximately every 90 minutes (16 times a day)",
                    "Once every month"
                ],
                "correct": 2,
                "explanation": "Orbiting at approximately 28,000 kilometres per hour, the ISS completes a full lap around Earth every 90 minutes, observing our shared planet day and night.",
                "study_insight": "At this rapid orbital speed, day and night cycle 16 times in 24 hours aboard the space station."
            }
        ]
    },
    {
        "id": 2,
        "title": "The Blue Planet",
        "subtitle": "Watery Oceans and Broad Continents from Orbit",
        "concept_html": """
            <p class="mb-3">Earth is affectionately known across the cosmos as the <strong>Blue Planet</strong> because liquid water covers roughly 71% of its total surface. From deep space, our planet looks like a radiant blue marble swirling with pure white cloud ribbons. The intense blue coloration is caused by deep oceans absorbing red wavelengths of sunlight while scattering blue light back into space.</p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3">
                <span class="text-xs font-bold text-sky-400 block mb-1.5">Planetary Surface Composition</span>
                <div class="w-full bg-slate-800 h-4 rounded-full overflow-hidden flex">
                    <div class="bg-sky-500 h-full text-[9px] font-bold text-white flex items-center justify-center" style="width: 71%;">71% Oceans & Seas</div>
                    <div class="bg-amber-600 h-full text-[9px] font-bold text-white flex items-center justify-center" style="width: 29%;">29% Land</div>
                </div>
            </div>
            <p class="text-xs text-slate-300">As distance increases, tiny human artefacts—skyscrapers, roadways, villages, and farmland—dissolve from sight. What remains visible are nature's grand features: vast oceans like the Indian, Pacific, and Atlantic, towering mountain ranges like the snow-capped Himalayas, massive river deltas, and expansive green forests.</p>
        """,
        "spoken_text": "Why do scientists call Earth the Blue Planet? Because over seventy percent of our planet's surface is covered with liquid oceans, seas, and lakes! When sunlight hits these immense bodies of water, blue light scatters into space, making our home glow like a precious sapphire. From high above, individual cities and buildings disappear. Only broad continents, mighty rivers, winding coasts, and vast blue waters remain visible.",
        "checkpoints": [
            {
                "question": "Approximately how much of Earth's surface is covered by oceans, seas, and water bodies?",
                "options": [
                    "About 25%",
                    "About 50%",
                    "Approximately 71%",
                    "Exactly 99%"
                ],
                "correct": 2,
                "explanation": "Liquid water covers about 71% of Earth's surface, making it appear strikingly blue when seen from outer space.",
                "study_insight": "Earth is the only known planet in our Solar System with stable liquid water bodies on its surface, enabling life to flourish."
            },
            {
                "question": "Which features remain visible from high space orbit while smaller details like streets and houses vanish?",
                "options": [
                    "Individual cars and village houses",
                    "Massive landmasses, mountain chains, and sprawling oceans",
                    "Classroom chalkboards and school playgrounds",
                    "Telephone poles and garden fences"
                ],
                "correct": 1,
                "explanation": "From space orbit, only continental landmasses, mountain ranges like the Himalayas, deserts, and vast oceans can be distinguished.",
                "study_insight": "Scale perspective teaches us that human existence is part of a grander geological and planetary tapestry."
            }
        ]
    },
    {
        "id": 3,
        "title": "Boundless Nature",
        "subtitle": "Global Movement of Air, Water, Clouds, Seeds, and Ideas",
        "concept_html": """
            <p class="mb-3">Nature does not carry passports or acknowledge international boundaries. The atmosphere is a continuous fluid blanket wrapping around the entire globe. A gust of wind originating over the Arabian Sea carries moisture that falls as refreshing monsoon rain thousands of kilometres inland. Ocean currents continuously circulate thermal energy, carrying nutrients across hemispheres.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Natural Transits</span>
                    <p class="text-xs text-slate-300">Dandelion parachutes, coconut seeds drifting on ocean waves, volcanic ash, and pollen grain travel effortlessly across vast continents and seas.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-indigo-400 block mb-1">Human Interconnection</span>
                    <p class="text-xs text-slate-300">Humanity is woven together through shared recipes, textiles, games, music melodies, scientific inventions, and folk tales passed along ancient trade routes.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Clean air breathed in New Delhi today may have circulated over Siberian forests or Antarctic ice sheets weeks ago. Our atmosphere, hydrosphere, and culture are shared heritages belonging to all living beings.</p>
        """,
        "spoken_text": "Have you ever stopped to wonder if the wind needs permission to cross from one country to another? Of course not! Clouds, rainwater, wandering seeds, and migrating animals move freely across the planet. In the very same way, human beings across continents are interconnected. We eat food that originated on distant continents, play games invented thousands of miles away, and share scientific discoveries that improve health everywhere.",
        "checkpoints": [
            {
                "question": "Why do clouds, winds, and ocean currents ignore human country borders?",
                "options": [
                    "Because they travel only during night-time",
                    "Because Earth's atmosphere and oceans form one continuous, boundary-free natural system",
                    "Because they follow special railway tracks",
                    "Because borders have large doors for wind to pass"
                ],
                "correct": 1,
                "explanation": "Earth's atmosphere and hydrosphere are continuous fluid systems that move freely around the globe driven by solar heating and Earth's spin.",
                "study_insight": "Global wind circulation, such as trade winds and jet streams, transports weather and water vapor across all continents."
            },
            {
                "question": "Which of the following demonstrates how human cultures around the world are interconnected?",
                "options": [
                    "Every country has completely separate air that never mixes",
                    "Sharing food ingredients, musical tunes, scientific discoveries, and folk tales",
                    "Living in total isolation without using any imported goods",
                    "Preventing birds from flying across rivers"
                ],
                "correct": 1,
                "explanation": "Human societies have always exchanged food, spices, musical instruments, languages, and inventions through trade and cultural travel.",
                "study_insight": "Trade routes like the ancient Silk Road and spice maritime lanes connected Asia, Africa, and Europe thousands of years ago."
            }
        ]
    },
    {
        "id": 4,
        "title": "Travelling Birds",
        "subtitle": "The Amazing Winter Odyssey of Rosy Starlings",
        "concept_html": """
            <p class="mb-3">Every year as autumn arrives, millions of birds embark on epic transcontinental journeys. One of the most remarkable seasonal travellers to India is the <strong>Rosy Starling</strong> (<em>Pastor roseus</em>), locally known as <em>Tilor</em> or <em>Gulabi Maina</em>. Sporting distinctive pastel pink bodies, glossy black crested heads, and sleek wings, these birds travel more than 4,000 to 5,000 kilometres!</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-pink-400 block mb-1">Breeding Grounds</span>
                    <p class="text-xs text-slate-300">During summer, rosy starlings nest across the open steppes and grasslands of southern Russia, Kazakhstan, Uzbekistan, and Mongolia.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Winter Haven in India</span>
                    <p class="text-xs text-slate-300">Fleeing freezing Central Asian blizzards, they fly across the Hindu Kush and Himalayas to winter across Gujarat, Rajasthan, and Peninsular India.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300"><strong>Farmer's Natural Ally:</strong> Rosy starlings perform an immense ecological service. They consume vast swarms of agricultural pests—voracious locusts and grasshoppers—safeguarding standing crops without chemical pesticides.</p>
        """,
        "spoken_text": "Imagine strapping on a pair of tiny wings and flying five thousand kilometres without a single road map! That is precisely what the rosy starling does. These lovely pink and black birds breed in the grassy plains of southern Russia and Mongolia during the warm summer. When harsh winter freezes their homeland, they take flight in massive, swirling flocks called murmurations, flying all the way to warm, sunny India. Here, they feast on locusts and grasshoppers, acting as natural pest busters for our farmers!",
        "checkpoints": [
            {
                "question": "From which region do rosy starlings migrate to India each winter?",
                "options": [
                    "Antarctica and the South Pole",
                    "Southern Russia, Central Asian steppes, and Mongolia",
                    "South America's Amazon rainforest",
                    "The Sahara Desert"
                ],
                "correct": 1,
                "explanation": "Rosy starlings breed in Central Asia, Southern Russia, and Mongolia during summer and migrate south to India to escape freezing winter temperatures.",
                "study_insight": "Migratory birds navigate using Earth's magnetic field, celestial stars, the position of the Sun, and geographical landmarks."
            },
            {
                "question": "How do migrating rosy starlings provide crucial help to Indian farmers?",
                "options": [
                    "They help harvest ripe wheat with their beaks",
                    "They dig irrigation canals in fields",
                    "They consume millions of destructive crop pests like locusts and grasshoppers",
                    "They frighten cattle away from grain bins"
                ],
                "correct": 2,
                "explanation": "Rosy starlings are voracious insectivores that eat swarms of locusts and grasshoppers, protecting crops naturally without requiring harmful toxic sprays.",
                "study_insight": "Biological pest control by insect-eating birds is an essential ecological balance mechanism recognized worldwide."
            }
        ]
    },
    {
        "id": 5,
        "title": "Yoga's Gift",
        "subtitle": "Ancient Indian Science of Wellness Celebrated Globally",
        "concept_html": """
            <p class="mb-3">Originating in ancient India more than 3,000 years ago, <strong>Yoga</strong> is a timeless holistic science connecting body, breath, and mind. Derived from the Sanskrit root <em>'Yuj'</em> (meaning to unite or join), yoga teaches human beings how to live in balance with themselves, their communities, and the natural ecosystem around them.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-teal-400 block mb-1">Three Pillars of Practice</span>
                    <p class="text-xs text-slate-300"><strong>Asanas:</strong> Gentle physical postures improving flexibility. <strong>Pranayama:</strong> Mindful rhythmic breathing. <strong>Dhyana:</strong> Meditative mental calmness.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">UN Recognition: June 21</span>
                    <p class="text-xs text-slate-300">In 2014, the United Nations General Assembly declared June 21 as the <em>International Day of Yoga</em>, adopted with support from 177 member nations.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">June 21 is the <strong>Summer Solstice</strong>—the longest day of the year in the Northern Hemisphere—symbolizing illuminating light, vitality, and planetary harmony. Today, millions practice yoga from Tokyo to New York and Paris.</p>
        """,
        "spoken_text": "Did you know that a practice born in India thousands of years ago is now celebrated in over one hundred and seventy countries? That is yoga! The word yoga comes from an ancient Sanskrit word meaning 'to unite'. Through simple physical postures, mindful breathing, and quiet meditation, yoga keeps our bodies strong and our minds calm. In 2014, the United Nations declared June 21 as International Day of Yoga, turning India's ancient treasure into a gift of peace for the entire planet.",
        "checkpoints": [
            {
                "question": "What does the ancient Sanskrit root word 'Yuj', from which 'Yoga' is derived, mean?",
                "options": [
                    "To run quickly",
                    "To unite or join together in harmony",
                    "To conquer through battle",
                    "To sleep deeply"
                ],
                "correct": 1,
                "explanation": "'Yuj' means to unite or join—symbolizing the union of individual body, breath, and mind with universal nature and community.",
                "study_insight": "Yoga is recognized by UNESCO as an Intangible Cultural Heritage of Humanity."
            },
            {
                "question": "On which astronomical date does the world celebrate the United Nations International Day of Yoga each year?",
                "options": [
                    "January 1 (New Year)",
                    "June 21 (Summer Solstice)",
                    "August 15 (Independence Day)",
                    "October 2 (Gandhi Jayanti)"
                ],
                "correct": 1,
                "explanation": "June 21 was designated by the United Nations because it marks the Summer Solstice, the longest day of the year in the Northern Hemisphere.",
                "study_insight": "A record 177 nations co-sponsored the UN resolution recognizing Yoga's universal holistic health benefits."
            }
        ]
    },
    {
        "id": 6,
        "title": "Chilli's Journey",
        "subtitle": "How a South American Pod Revolutionized Indian Cooking",
        "concept_html": """
            <p class="mb-3">It is almost impossible to imagine Indian food today without spicy red and green chillies. Yet, for thousands of years, Indian cooking used no chillies at all! Traditional Indian curries got their pungent warmth from <strong>black pepper</strong> (<em>Piper nigrum</em>), native to Kerala's lush Western Ghats, and dry ginger (<em>Sonth</em>).</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-rose-400 block mb-1">Native to South America</span>
                    <p class="text-xs text-slate-300">Wild chilli plants (genus <em>Capsicum</em>) originated in Central and South America (regions of modern Mexico, Bolivia, and Peru), cultivated for over 6,000 years.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Maritime Trade Voyage</span>
                    <p class="text-xs text-slate-300">Following Christopher Columbus's voyages, Portuguese traders brought chilli seeds to Goa on India's western coast roughly 400 to 500 years ago.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Indian farmers quickly discovered that chillies grew easily in tropical soil. Within decades, chillies spread across India, creating iconic regional varieties like Guntur chillies in Andhra Pradesh, Byadgi in Karnataka, and Bhut Jolokia in Assam!</p>
        """,
        "spoken_text": "If you love spicy food, you might be surprised to learn that Indian cuisine had no chillies five hundred years ago! Ancient Indian chefs used black pepper from Kerala and dry ginger to make dishes spicy. Chillies actually grew wild in South America! When Portuguese sailors sailed across the Atlantic and Indian Oceans, they carried bright red chilli pods to Goa. Indian farmers loved how easily they grew, and soon chillies became the fiery heart of our curries and chutneys.",
        "checkpoints": [
            {
                "question": "What primary indigenous spice did ancient Indian cooks use to make food spicy before chillies arrived?",
                "options": [
                    "Green bell peppers",
                    "Black pepper from the Western Ghats and dry ginger",
                    "Red paprika powder",
                    "Chemical food seasonings"
                ],
                "correct": 1,
                "explanation": "Before the arrival of chillies, indigenous black pepper (known as 'Black Gold' across Roman and Arab trade) provided pungent spice to Indian cooking.",
                "study_insight": "Black pepper vines are native to the tropical rainforests of the Western Ghats in Southwestern India."
            },
            {
                "question": "Where did chilli plants originally originate before being brought to India by maritime traders?",
                "options": [
                    "Central and South America",
                    "Australia",
                    "Antarctica",
                    "Northern Europe"
                ],
                "correct": 0,
                "explanation": "Chillies originated in Central and South America and were introduced to India via Portuguese sea traders in the late 15th and early 16th centuries.",
                "study_insight": "Capsaicin is the chemical compound inside chilli membranes that triggers heat receptors on human tastebuds."
            }
        ]
    },
    {
        "id": 7,
        "title": "Sweet Sugar",
        "subtitle": "Ancient Indian Sugarcane Mastery and the Global Sweet Tooth",
        "concept_html": """
            <p class="mb-3">While the chilli travelled from the Americas to India, <strong>sugar</strong> travelled in the exact opposite direction—from India to the entire world! Ancient Indians were the very first people on Earth to invent methods for extracting, clarifying, and boiling sugarcane juice to create solid sweetness.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">From Gur to Sarkara</span>
                    <p class="text-xs text-slate-300">Indian artisans boiled sugarcane juice into nutritious golden <strong>Jaggery</strong> (<em>Gur</em>). Later, they refined it into white sparkling crystals called <em>Sarkara</em> in Sanskrit (the root of the English word 'Sugar').</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-sky-400 block mb-1">Global Sweet Trade</span>
                    <p class="text-xs text-slate-300">Persians, Arabs, Greeks, and Chinese learned the art of crystallization from India. Indian sugar crystals (<em>Khanda</em>, root of 'Candy') became prized luxury commodities worldwide.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">India similarly shared succulent mangoes, rice cultivars, and bananas with global travellers, while adopting paper-making and tea cultivation originally refined in China.</p>
        """,
        "spoken_text": "Did you know that the sweet white crystals in your kitchen sugar jar have an ancient Indian ancestry? That is right! Ancient Indian farmers were the pioneers who figured out how to crush sugarcane stalks, boil the sweet juice, and crystalize it into jaggery and sparkling sugar crystals called Sarkara in Sanskrit. Persian and Arab merchants fell in love with this sweet marvel, taking sugarcane stems and crystallization secrets across Europe, Africa, and the Americas.",
        "checkpoints": [
            {
                "question": "Which ancient civilization first invented the technology to extract juice from sugarcane and crystallize it into sugar?",
                "options": [
                    "Ancient Rome",
                    "Ancient India",
                    "Viking explorers",
                    "Inca mountain tribes"
                ],
                "correct": 1,
                "explanation": "Sugarcane crystallization into jaggery (gur) and sugar crystals (sarkara) was pioneered in ancient India during the Gupta and Vedic periods.",
                "study_insight": "The English words 'sugar' and 'candy' trace their linguistic lineage to the Sanskrit terms 'sarkara' and 'khanda'."
            },
            {
                "question": "Which of the following agricultural and craft treasures travelled to India from China across ancient trade routes?",
                "options": [
                    "Sugarcane processing",
                    "Paper-making and tea cultivation",
                    "Black pepper cultivation",
                    "Pashmina weaving"
                ],
                "correct": 1,
                "explanation": "Paper manufacturing and tea varieties originated in China and spread along trade routes into India and the rest of the world.",
                "study_insight": "Cross-cultural trade was two-way: India shared cotton, sugar, and spices, while adopting paper, silk, and porcelain."
            }
        ]
    },
    {
        "id": 8,
        "title": "Mexican Marigold",
        "subtitle": "The Bright Aztec Bloom that Became India's Festive Soul",
        "concept_html": """
            <p class="mb-3">Walk through any Indian flower market today, and you will see mountains of fragrant, bright orange and golden yellow flowers: the <strong>Genda Phool</strong> or <strong>Marigold</strong> (genus <em>Tagetes</em>). From welcoming guests with garlands to decorating temple entrances, wedding mandaps, and Diwali rangolis, marigolds seem quintessentially Indian. Yet, their ancestral home lies across the ocean in Mexico!</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Cempasúchil of the Aztecs</span>
                    <p class="text-xs text-slate-300">In pre-Columbian Mexico, indigenous Aztecs cultivated the flower as <em>Cempasúchil</em> (meaning 'twenty flowers'). They believed its bright petals guided ancestral spirits during Day of the Dead ceremonies.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-orange-400 block mb-1">Thriving in Indian Soil</span>
                    <p class="text-xs text-slate-300">Portuguese and Spanish sailors carried the hardy seeds across trade routes in the 16th century. Marigolds adapted instantly to India's warm sunshine and soil, flowering year-round.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">The marigold's aromatic leaves naturally repel nematodes and insect pests, making them beloved companion plants in Indian vegetable gardens and farms!</p>
        """,
        "spoken_text": "Look at the cheerful golden garlands decorating our homes during Diwali and weddings! That beloved flower is the marigold, or Genda Phool. But did you know its homeland is Mexico? Thousands of years ago, the Aztec people in Mexico cultivated these bright blooms and called them Cempasuchil, meaning twenty flowers in their language. When Spanish and Portuguese ships brought marigold seeds across the seas to India, our soil welcomed them with open arms. Today, no Indian festival feels complete without their glowing orange petals!",
        "checkpoints": [
            {
                "question": "In which country did the vibrant orange and yellow marigold (Genda Phool) originally grow before travelling to India?",
                "options": [
                    "Canada",
                    "Mexico (Central America)",
                    "Japan",
                    "Norway"
                ],
                "correct": 1,
                "explanation": "Marigolds are native to Mexico, where Aztec civilizations cultivated them for spiritual festivals centuries before European trade ships transported them globally.",
                "study_insight": "In Mexico, marigolds are called 'Flor de Muerto' (Flower of the Dead), guiding loved ones with their vibrant colour and strong scent."
            },
            {
                "question": "What agricultural benefit do marigold plants provide when planted alongside crops in Indian gardens?",
                "options": [
                    "They produce sweet edible fruit pods",
                    "Their pungent aroma and roots repel soil pests and destructive nematodes",
                    "They warm the soil during freezing winters",
                    "They attract termites to field edges"
                ],
                "correct": 1,
                "explanation": "Marigold roots secrete natural compounds that deter root-knot nematodes and insect pests, making them excellent natural companion plants for vegetables.",
                "study_insight": "Intercropping with marigolds is a traditional method of organic farming that reduces chemical pesticide usage."
            }
        ]
    }
]

print("Slides 1 to 8 authored successfully.")


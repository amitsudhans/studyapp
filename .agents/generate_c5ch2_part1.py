"""
Part 1 Generator for NCERT Class 5 Science - Chapter 2: Journey of a River
Slides 1 to 8:
- Short punchy headings (1-3 words)
- Subtitles
- Rich concept HTML
- Spoken text (Classroom lecture, Indian English narration, NO lecturer names, river journey perspective)
- 2 formative checkpoints per slide with instant feedback and study insights
- Zero raw LaTeX (Clean Unicode only)
"""

CHAPTER_META = {
    "title": "Journey of a River",
    "chapter_no": 2,
    "class": "Class 5 Science",
    "subject": "Science",
}

SLIDES_PART1 = [
    # Slide 1: River Origin
    {
        "id": 1,
        "title": "River Origin",
        "subtitle": "Birth of the Godavari at Brahmagiri Hills",
        "concept_html": """
            <p class="mb-3">
                High up in the mist-shrouded <strong>Brahmagiri Hills</strong> of the Western Ghats at Trimbakeshwar in Maharashtra, tiny trickles of crystalline groundwater emerge from the rocks. This humble spring is the birthplace of the mighty <strong>Godavari River</strong>, affectionately celebrated as the <em>Dakshin Ganga</em> (Ganga of the South).
            </p>
            <p class="mb-3">
                From this mountain crag, the river embarks on a grand journey of <strong>1,465 kilometres</strong> across peninsular India. It flows eastwards across the Deccan Plateau, traversing Maharashtra, Telangana, and Andhra Pradesh, before gently fanning out into the Bay of Bengal.
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-300 block mb-1">🏔️ The Source (Origin)</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Trimbakeshwar, Nashik district, Maharashtra. Elevation of about 1,067 meters above sea level. Cold, rapid, and crystal clear.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">🌊 The Mouth (Destination)</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Bay of Bengal near Antarvedi and Yanam. Forms an expansive, fertile delta and mangrove estuary stretching hundreds of kilometers.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                A river's journey is a story of continuous transformation: starting as a modest trickling brook, carving valleys, and swelling into a majestic freshwater highway.
            </p>
        """,
        "spoken_text": "Imagine standing atop the misty green Brahmagiri Hills at Trimbakeshwar in the Western Ghats of Maharashtra. Here, from deep crevices in the rock, cold drops of crystal water bubble to the surface. This humble spring marks the birth of the majestic Godavari River, often called the Dakshin Ganga, or Ganga of the South. From this single mountain origin, the Godavari begins an epic one thousand four hundred and sixty-five kilometer voyage across the heart of peninsular India. Flowing eastward across the dry, rugged Deccan Plateau, it carves magnificent gorges, nourishes millions of farms, and journeys through Maharashtra, Telangana, and Andhra Pradesh until it empties peacefully into the vast Bay of Bengal.",
        "lecture_script": "Imagine standing atop the misty green Brahmagiri Hills at Trimbakeshwar in the Western Ghats...",
        "checkpoints": [
            {
                "question": "At which historic location in the Western Ghats of Maharashtra does the Godavari River originate?",
                "options": [
                    "Brahmagiri Hills at Trimbakeshwar",
                    "Gangotri Glacier in the Himalayas",
                    "Marina Beach in Chennai",
                    "Thar Desert in Rajasthan"
                ],
                "correct": 0,
                "explanation": "The Godavari originates at Trimbakeshwar in the Brahmagiri Hills, Nashik district, Maharashtra.",
                "study_insight": "The place where a river begins its journey is called its source or origin."
            },
            {
                "question": "Approximately how long is the entire journey of the Godavari River from its source to the Bay of Bengal?",
                "options": [
                    "About 1,465 kilometres",
                    "Exactly 100 kilometres",
                    "Over 10,000 kilometres",
                    "Only 50 kilometres"
                ],
                "correct": 0,
                "explanation": "The Godavari is peninsular India's longest river, flowing roughly 1,465 km across the Deccan Plateau to the Bay of Bengal.",
                "study_insight": "The Godavari is the second longest river in India after the Ganga."
            }
        ]
    },

    # Slide 2: Joining Streams
    {
        "id": 2,
        "title": "Joining Streams",
        "subtitle": "Tributaries Swelling the Main River Channel",
        "concept_html": """
            <p class="mb-3">
                A large river does not travel alone. As the Godavari flows downstream through valleys and forests, other smaller rivers and mountain streams flow into it, joining their waters to the main channel. These contributing streams are called <strong>tributaries</strong>.
            </p>
            <div class="grid grid-cols-3 gap-2.5 my-3 text-center">
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">Manjira River</span>
                    <p class="text-[11px] text-slate-300">
                        Major right-bank tributary flowing from Balaghat Range through Karnataka, Telangana, and Maharashtra.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">Indravati River</span>
                    <p class="text-[11px] text-slate-300">
                        Vibrant left-bank tributary rushing through the dense sal forests of Dandakaranya and Bastar in Chhattisgarh.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">Sabari River</span>
                    <p class="text-[11px] text-slate-300">
                        Fast-flowing tributary emerging from the Eastern Ghats of Odisha, adding immense volume near Kunavaram.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                With every tributary that unites with it, the Godavari's channel grows broader, deeper, and more powerful, carrying millions of cubic meters of fresh water toward the plains.
            </p>
        """,
        "spoken_text": "As a river travels across the land, it is joined by companion streams that increase its volume and strength. These smaller rivers and streams that flow into a larger parent river are called tributaries. For the Godavari, tributaries like the Manjira from the south, and the Indravati and Sabari from the dense eastern forests, pour their sparkling waters into its channel. At every confluence, known as a sangam, the main river broadens and gains momentum. Without its vast network of tributaries draining rain from hundreds of surrounding hills, a giant river could never maintain its magnificent flow across thousands of kilometers.",
        "lecture_script": "As a river travels across the land, it is joined by companion streams that increase its volume...",
        "checkpoints": [
            {
                "question": "What is the scientific geographical term for a smaller stream or river that joins and feeds a larger main river?",
                "options": [
                    "A tributary",
                    "An iceberg",
                    "A desert dune",
                    "A volcano"
                ],
                "correct": 0,
                "explanation": "A tributary is a freshwater stream or river that feeds into a larger main stream or parent river rather than directly into an ocean.",
                "study_insight": "The meeting point of a river and its tributary is called a confluence or sangam."
            },
            {
                "question": "Which of the following is an important tributary that merges into the Godavari River?",
                "options": [
                    "Indravati River",
                    "Thames River",
                    "Nile River",
                    "Amazon River"
                ],
                "correct": 0,
                "explanation": "The Indravati, Manjira, Pranhita, and Sabari are key tributaries of the Godavari River basin in India.",
                "study_insight": "The Indravati is famous for the majestic Chitrakote Falls in Bastar."
            }
        ]
    },

    # Slide 3: Flowing Forever
    {
        "id": 3,
        "title": "Flowing Forever",
        "subtitle": "Perennial Rivers vs Seasonal Rain-Fed Rivers",
        "concept_html": """
            <p class="mb-3">
                Rivers exhibit diverse lifecycles based on where they receive their water. In physical geography, rivers are classified into two major categories:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3.5 rounded-xl bg-blue-950/40 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-300 block mb-1">🌊 Perennial Rivers (Sada Neera)</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li>Flow with abundant water throughout the entire 365 days of the year.</li>
                        <li>Fed by deep groundwater springs, high mountain runoff, and seasonal monsoon rains.</li>
                        <li>Examples: Ganga, Brahmaputra, and the mighty Godavari.</li>
                    </ul>
                </div>
                <div class="p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">☀️ Seasonal Rivers (Mausami Nadi)</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li>Flow vigorously only during the rainy monsoon season.</li>
                        <li>Shrink to narrow trickles, disconnected pools, or dry sandy beds during hot summer months.</li>
                        <li>Rely exclusively on direct rainfall runoff without perennial glacial or spring sources.</li>
                    </ul>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Understanding whether a river is perennial or seasonal helps farmers choose suitable crops and guides communities in building water storage tanks.
            </p>
        """,
        "spoken_text": "Have you ever seen a river that roars with water during the July monsoon but turns into a dry, dusty track of sand by May? Rivers on Earth fall into two great categories: perennial and seasonal. Perennial rivers, like the Godavari and the Himalayan Ganga, flow with water every single day of the year. They are fed by persistent groundwater aquifers, deep mountain springs, and melting snow, so they never completely run out of water. Seasonal rivers, on the other hand, depend entirely on monsoon rains. When the rains cease in October, their flow slows down, and by peak summer, they dry up into cracked clay. Knowing whether a river flows all year helps farmers decide which crops to plant.",
        "lecture_script": "Have you ever seen a river that roars with water during the July monsoon...",
        "checkpoints": [
            {
                "question": "What is a river called that maintains a continuous flow of water throughout all twelve months of the year?",
                "options": [
                    "A perennial river",
                    "A seasonal river",
                    "An artificial fountain",
                    "A dry wadi"
                ],
                "correct": 0,
                "explanation": "Perennial rivers flow continuously throughout the year because they are replenished by persistent springs, aquifers, or melting snow.",
                "study_insight": "The word 'perennial' means lasting or continuing through the entire year."
            },
            {
                "question": "Why do seasonal rivers dry up or reduce to small trickles during the summer months?",
                "options": [
                    "They depend entirely on rainwater and lack deep spring or snowmelt sources during dry seasons",
                    "The water turns into solid stone during summer",
                    "Underground monsters drink all the water",
                    "Fish block the water from flowing"
                ],
                "correct": 0,
                "explanation": "Seasonal rivers rely solely on precipitation runoff; when monsoon rains stop and high temperatures cause evaporation, their flow ceases.",
                "study_insight": "Rain-fed seasonal streams require rainwater harvesting structures to preserve water for dry months."
            }
        ]
    },

    # Slide 4: Forest Life
    {
        "id": 4,
        "title": "Forest Life",
        "subtitle": "Riparian Corridors & Deccan Wildlife Habitats",
        "concept_html": """
            <p class="mb-3">
                As a river carves its path, the land immediately bordering its banks—known as the <strong>riparian corridor</strong>—develops into a haven for terrestrial and arboreal biodiversity:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">🐾 Thriving Forest Wildlife</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Royal Bengal tigers, leopards, barking deer (muntjac), sloth bears, and wild boars roam the river basin, coming to the water's edge at dawn and twilight to drink.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🦎 Rare Reptiles & Flora</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        The river valley shelters rare endemic creatures like the <em>Indian Golden Gecko</em> in rocky crevices, alongside precious timber forests of <em>Red Sandalwood</em> (Raktachandan).
                    </p>
                </div>
            </div>
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <strong>River Corridor Shield:</strong> Lush riverside forests prevent the soil from baking under the harsh sun, maintain cooler microclimates, and provide wildlife migration highways across dry peninsular plains.
            </div>
        """,
        "spoken_text": "A river is never just water; it is the lifeblood of entire forest realms. As the Godavari winds through the Deccan Plateau and Eastern Ghats, its banks are lined with dense, vibrant jungles. Royal Bengal tigers, leopards, and gentle barking deer tread softly along the moist riverbanks to drink cool water in the evening glow. In the rocky gorges, rare creatures like the luminous Indian golden gecko make their homes among ancient boulders. The surrounding hills are famous for fragrant red sandalwood trees and towering teak forests. The river creates a living corridor of green, offering food, shelter, and shade to thousands of wild species.",
        "lecture_script": "A river is never just water; it is the lifeblood of entire forest realms...",
        "checkpoints": [
            {
                "question": "Which of the following rare, endemic reptiles finds shelter in the rocky hill crevices along the Godavari River basin?",
                "options": [
                    "Indian Golden Gecko",
                    "Polar bear",
                    "Arctic penguin",
                    "Sea turtle"
                ],
                "correct": 0,
                "explanation": "The Indian Golden Gecko (Calodactylodes aureus) is a rare gecko endemic to the rocky hills and gorges of the Eastern Ghats along river valleys.",
                "study_insight": "Golden geckos are nocturnal reptiles adapted to granite boulders in river valleys."
            },
            {
                "question": "Why are riverside forests (riparian zones) critical for wildlife in hot regions like the Deccan Plateau?",
                "options": [
                    "They provide continuous drinking water, cooler shade, and natural migration routes for animals",
                    "They turn all animals into birds",
                    "They prevent sunlight from ever reaching Earth",
                    "They freeze all water into solid ice"
                ],
                "correct": 0,
                "explanation": "Riverside vegetation moderates air temperature, supplies water, and acts as a safe biological highway for animals traveling across dry landscapes.",
                "study_insight": "Riparian buffers also filter agricultural runoff before it enters the river."
            }
        ]
    },

    # Slide 5: Mangrove Delta
    {
        "id": 5,
        "title": "Mangrove Delta",
        "subtitle": "Coringa Mangroves & Estuarine Ecosystems",
        "concept_html": """
            <p class="mb-3">
                Near the end of its 1,465 km journey in Andhra Pradesh, the Godavari splits into distributary branches (Gautami and Vasishta) and meets the salty Bay of Bengal. Here lies one of India's grandest natural treasures: the <strong>Coringa Mangrove Forests</strong>.
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-teal-950/40 border border-teal-500/30">
                    <span class="text-xs font-bold text-teal-300 block mb-1">🌊 Brackish Water Estuary</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        An estuary is a coastal area where river freshwater mixes with salty sea tides. This nutrient-rich brackish soup is the nursery of the ocean.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">🌿 Stilt Roots & Pneumatophores</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Mangrove trees grow specialized breathing roots (pneumatophores) that stick up out of oxygen-poor coastal mud like snorkels to breathe air!
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                Coringa is home to fishing cats, smooth-coated otters, saltwater crocodiles, and hundreds of species of migratory sea birds. Mangroves act as living bio-shields against deadly ocean cyclones.
            </p>
        """,
        "spoken_text": "At the final stage of its long journey, the Godavari meets the salty ocean in Andhra Pradesh. Here, in the shelter of the delta, lies the magical world of the Coringa Mangrove Forests—the second largest mangrove formation in India! In this estuarine zone, fresh river water mixes with salty sea tides to form brackish water. Because coastal mud is waterlogged and lacks oxygen, mangrove trees have developed remarkable vertical breathing roots, called pneumatophores, that rise above the mud like wooden pencils to breathe atmospheric air. This rich wetland is a vital nursery where juvenile fish, crabs, and prawns grow, and it serves as a protective wall defending coastal villages against violent cyclone waves.",
        "lecture_script": "At the final stage of its long journey, the Godavari meets the salty ocean in Andhra Pradesh...",
        "checkpoints": [
            {
                "question": "What is the coastal wetland zone called where river freshwater merges with salty ocean tides?",
                "options": [
                    "An estuary (brackish water delta)",
                    "A dry mountain ridge",
                    "A desert sand dune",
                    "An underground cave"
                ],
                "correct": 0,
                "explanation": "An estuary is a partially enclosed coastal body of water where river freshwater mixes with seawater from the open ocean.",
                "study_insight": "Estuaries produce more organic matter each year than comparably sized agricultural lands."
            },
            {
                "question": "Why do mangrove trees in the Coringa estuary produce vertical roots (pneumatophores) that project upward above the mud?",
                "options": [
                    "To breathe atmospheric oxygen because waterlogged coastal mud lacks air",
                    "To catch flying birds for food",
                    "To collect rainwater in tiny wooden cups",
                    "To push the sea away from the land"
                ],
                "correct": 0,
                "explanation": "Waterlogged estuarine mud is anaerobic (oxygen-poor); pneumatophores have lenticels that take in atmospheric oxygen and transport it to underground roots.",
                "study_insight": "Pneumatophores function like natural snorkels for tree roots."
            }
        ]
    },

    # Slide 6: Lifeline Waters
    {
        "id": 6,
        "title": "Lifeline Waters",
        "subtitle": "Domestic Hydration, Agriculture, and Industrial Support",
        "concept_html": """
            <p class="mb-3">
                For millennia, human settlements have clustered along riverbanks. Rivers are not merely natural waterways; they are the <strong>lifelines of human civilization</strong>, supporting daily life across villages, towns, and mega-cities:
            </p>
            <div class="space-y-2.5 my-3">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-sky-300">1. Domestic Survival (Drinking & Cooking)</span>
                        <p class="text-[11px] text-slate-300">Filtered river water is pumped into municipal water filtration plants, supplying daily drinking water to millions of households.</p>
                    </div>
                    <span class="text-lg">🚰</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-emerald-300">2. Agricultural Irrigation (Food Security)</span>
                        <p class="text-[11px] text-slate-300">Thousands of canals divert river water to irrigate sprawling fields of paddy rice, sugarcane, cotton, and oilseeds across the Deccan plains.</p>
                    </div>
                    <span class="text-lg">🌾</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-amber-300">3. Industrial Manufacturing</span>
                        <p class="text-[11px] text-slate-300">Thermal power plants, textile factories, paper mills, and steel works rely on river water for cooling, processing, and steam turbines.</p>
                    </div>
                    <span class="text-lg">🏭</span>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Without the reliable flow of our rivers, agriculture would wither, cities would face acute dehydration, and the economy would grind to a halt.
            </p>
        """,
        "spoken_text": "Why have all the great civilizations of world history been born on riverbanks? Because rivers provide the very foundation of human survival and prosperity. The Godavari River quenches the thirst of millions of citizens living in towns, pilgrimage centers, and villages across three states. Every morning, municipal waterworks filter and distribute its water for cooking and household needs. Networked canals branch out into rural districts, irrigating vast emerald fields of rice, sugarcane, and cotton. Furthermore, industries, textile factories, and thermal power stations depend on river water to cool equipment and generate electricity. The river is our silent, generous lifeline.",
        "lecture_script": "Why have all the great civilizations of world history been born on riverbanks?...",
        "checkpoints": [
            {
                "question": "What primary agricultural purpose does river water channeled through canal networks serve?",
                "options": [
                    "Crop irrigation for rice, cotton, and sugarcane fields",
                    "Washing aeroplane wings in the sky",
                    "Painting farm tractors",
                    "Drying wheat grains in the sun"
                ],
                "correct": 0,
                "explanation": "Canal networks divert river water directly to farm fields, ensuring reliable irrigation for food and cash crops throughout the growing season.",
                "study_insight": "River valley irrigation systems are the backbone of national food security."
            },
            {
                "question": "Why did ancient humans build their earliest settlements and major cities directly alongside rivers?",
                "options": [
                    "Rivers provided an uninterrupted supply of freshwater for drinking, farming, and transport",
                    "Rivers were made of solid gold",
                    "To hide from the Sun",
                    "Because there was no air anywhere else"
                ],
                "correct": 0,
                "explanation": "Rivers offered accessible drinking water, fertile alluvial floodplains for agriculture, and convenient water highways for trade and transportation.",
                "study_insight": "All ancient civilizations—Harappan, Mesopotamian, Nile, and Chinese—arose in fertile river valleys."
            }
        ]
    },

    # Slide 7: River Trades
    {
        "id": 7,
        "title": "River Trades",
        "subtitle": "Traditional Fisheries, Inland Navigation, and Ecotourism",
        "concept_html": """
            <p class="mb-3">
                A river does not just carry water; it sustains millions of livelihoods through traditional crafts, commercial fisheries, water navigation, and modern <strong>ecotourism</strong>:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">🎣 Traditional Inland Fisheries</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Fisherfolk cast hand-woven cast nets from wooden boats (dhonis) to harvest freshwater fish, prawns, and crabs, providing protein and local market income.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">🌿 Sustainable Ecotourism</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Responsible travel to natural river landscapes (such as the breathtaking Papi Hills gorge or Coringa boat tours) to observe wildlife and scenic beauty <em>without harming the environment</em>.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                Ecotourism generates alternative income for local tribal and riverbank communities while building public commitment to preserve river ecosystems in their pristine state.
            </p>
        """,
        "spoken_text": "Beyond drinking water and agriculture, rivers create vibrant livelihoods for millions of people. Traditional fisherfolk set out in wooden boats at dawn, casting nets into the tranquil waters to harvest freshwater fish, carp, and crabs that feed local towns. Rivers also serve as historic inland waterways for transporting grain and goods. In recent years, sustainable ecotourism has flourished. Ecotourism means traveling responsibly to pristine natural areas—like the dramatic Papi Hills on the Godavari—to admire nature and observe wildlife without polluting or disturbing the natural habitat. It provides local boatmen and guides with respectable livelihoods while teaching visitors to treasure and protect our rivers.",
        "lecture_script": "Beyond drinking water and agriculture, rivers create vibrant livelihoods for millions...",
        "checkpoints": [
            {
                "question": "What is the defining principle of 'ecotourism' along natural river valleys and sanctuaries?",
                "options": [
                    "Visiting natural landscapes to appreciate wildlife and beauty without harming or polluting the environment",
                    "Cutting down all trees to build large concrete factories",
                    "Dumping plastic bags into river channels",
                    "Hunting wild animals for sport"
                ],
                "correct": 0,
                "explanation": "Ecotourism is responsible travel to natural areas that conserves the environment, minimizes tourist impact, and improves the well-being of local people.",
                "study_insight": "True ecotourists take only photos, leave only footprints, and keep waterways clean."
            },
            {
                "question": "Which historic gorge on the Godavari River is renowned for scenic ecotourism boat cruises between green hills?",
                "options": [
                    "Papi Hills (Papikondalu)",
                    "Mount Everest summit",
                    "Thar desert sand sea",
                    "Sundarbans saltwater creek"
                ],
                "correct": 0,
                "explanation": "Papikondalu (Papi Hills) is a scenic gorge where the Godavari River narrows and winds between steep forested hills in Andhra Pradesh.",
                "study_insight": "Boat journeys through Papikondalu highlight the raw geological beauty of river gorges."
            }
        ]
    },

    # Slide 8: Giant Walls
    {
        "id": 8,
        "title": "Giant Walls",
        "subtitle": "Dams, Reservoirs, and Hydroelectric Energy",
        "concept_html": """
            <p class="mb-3">
                To capture torrential monsoon floods and store water for scorched dry months, humans erect colossal concrete and masonry barricades across river channels: <strong>dams</strong>. Over 900 large dams have been constructed across the Godavari river basin alone!
            </p>
            <div class="space-y-2.5 my-3">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-sky-300">1. Reservoir Storage</span>
                        <p class="text-[11px] text-slate-300">Dams create massive artificial lakes (reservoirs) behind their walls, holding billions of liters of water for dry summer months.</p>
                    </div>
                    <span class="text-lg">🌊</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-amber-300">2. Hydroelectric Power Generation</span>
                        <p class="text-[11px] text-slate-300">Pressurized water plunges through deep penstock pipes, spinning giant turbines to generate clean electricity without burning coal.</p>
                    </div>
                    <span class="text-lg">⚡</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-emerald-300">3. Flood Attenuation</span>
                        <p class="text-[11px] text-slate-300">Dam gates regulate downstream outflow during torrential downpours, reducing the risk of catastrophic flash floods in delta towns.</p>
                    </div>
                    <span class="text-lg">🛡️</span>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Major examples on the Godavari include Jayakwadi Dam (Maharashtra), Sriram Sagar Project (Telangana), and the Polavaram Project (Andhra Pradesh).
            </p>
        """,
        "spoken_text": "To capture the immense volume of seasonal monsoon rain before it rushes wasted into the sea, engineers build massive concrete barriers across river valleys called dams. Across the Godavari basin alone, over nine hundred dams of various sizes have been erected. A dam acts like a giant stopper in a bottle, backing water up into a colossal artificial lake called a reservoir. This stored water is steadily released through dry months to irrigate farmland and supply drinking water to cities. Inside the dam wall, rushing pressurized water plunges through giant pipes, spinning massive metal turbines to generate clean hydroelectric power. Famous landmarks like Jayakwadi Dam and Sriram Sagar store billions of liters to safeguard our water security.",
        "lecture_script": "To capture the immense volume of seasonal monsoon rain before it rushes wasted...",
        "checkpoints": [
            {
                "question": "What is the massive artificial lake formed behind a dam wall to store river water called?",
                "options": [
                    "A reservoir",
                    "A glacier",
                    "A swimming pool",
                    "An ocean trench"
                ],
                "correct": 0,
                "explanation": "A reservoir is a large natural or artificial lake used as a source of water supply, created by damming a flowing river.",
                "study_insight": "Reservoirs store monsoon surplus to ensure year-round water supply."
            },
            {
                "question": "How do hydroelectric power stations located inside large dams generate clean electrical energy?",
                "options": [
                    "By using the kinetic force of falling water to spin giant power turbines",
                    "By burning millions of tons of dry firewood",
                    "By boiling petroleum oil in metal tanks",
                    "By pulling electricity directly out of clouds using kites"
                ],
                "correct": 0,
                "explanation": "Falling water turns turbine blades connected to a generator rotor, converting gravitational potential and kinetic energy into clean electricity.",
                "study_insight": "Hydroelectricity produces zero greenhouse gas smoke during power generation."
            }
        ]
    }
]


"""
Part 2 of NCERT Class 5 Science Chapter 6: Some Unique Places
Slides 9 to 16
Short Headings (1-3 words) with exact same meaning:
9. Seven Sisters
10. Hargila Stork
11. Root Bridges
12. Western Ghats
13. Mountain Springs
14. Citizen Science
15. Silent Valley
16. Eco Sanctuaries
"""

import sys

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Seven Sisters",
        "subtitle": "Northeast India & Sikkim: Cloud Forests, Rivers & Indigenous Heritage",
        "concept_html": """
            <p>From the tidal mangroves of Bengal, our journey ascends into <strong>Northeast India</strong>—a breathtaking realm of mist-covered mountain ranges, emerald valleys, and sacred groves comprising the contiguous <strong>'Seven Sister' States</strong> plus their brother state <strong>Sikkim</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-emerald-400 block mb-0.5">🌿 The Seven Sisters</span>
                    <span class="text-slate-300"><strong>Arunachal Pradesh</strong> (Land of Dawn-Lit Mountains), <strong>Assam</strong> (River Brahmaputra & one-horned rhinos), <strong>Manipur</strong> (Jewel of India & Loktak floating phumdis), <strong>Meghalaya</strong> (Abode of Clouds & living root bridges), <strong>Mizoram</strong> (Bamboo hills), <strong>Nagaland</strong> (Falcon capital & hornbill festival), and <strong>Tripura</strong> (Rich palace arts).</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-sky-400 block mb-0.5">🏔️ Sikkim: The Himalayan Brother</span>
                    <span class="text-slate-300">Nestled under the majestic shadow of <strong>Mount Kangchenjunga</strong> (India's highest peak at 8,586 m), Sikkim became the world's first <strong>100% certified organic farming state</strong>, banning all chemical pesticides.</span>
                </div>
            </div>
            <p>Northeast India is celebrated for its deep indigenous reverence for nature—communities protect <em>Sacred Groves</em> (ancient virgin forests where not even a twig may be broken), preserving pristine biodiversity for generations.</p>
        """,
        "spoken_text": "Now our expedition travels to the misty hills of Northeast India! This spectacular region includes the Seven Sister states—Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, and Tripura—along with their brother state, Sikkim. Here, mighty rivers like the Brahmaputra thunder through deep green valleys, fed by monsoon clouds. Under Mount Kangchenjunga, Sikkim became the world's first completely organic state, growing crops without harmful chemicals. The people of Northeast India hold sacred bonds with the wilderness, protecting sacred forest groves and living in complete harmony with animals and rivers.",
        "lecture_script": "Introduces Northeast India's Seven Sister states and Sikkim, sacred groves, geographic features including Mount Kangchenjunga and Brahmaputra, and Sikkim's organic farming milestone.",
        "checkpoints": [
            {
                "question": "Which Himalayan state of Northeast India became the world's first fully certified 100% organic farming state?",
                "options": [
                    "Assam",
                    "Sikkim",
                    "Meghalaya",
                    "Tripura"
                ],
                "correct": 1,
                "explanation": "In 2016, Sikkim became the world's first 100% organic state by completely phasing out chemical fertilizers and toxic pesticides in favor of natural composting and traditional ecological pest control.",
                "study_insight": "Sikkim won the UN Food and Agriculture Organization's prestigious Future Policy Gold Award for this milestone."
            },
            {
                "question": "What is a 'Sacred Grove' preserved by indigenous communities across Northeast India?",
                "options": [
                    "A commercial timber plantation harvested for paper",
                    "An ancient patch of pristine forest protected by traditional taboos where hunting and tree felling are strictly forbidden",
                    "An artificial botanical greenhouse made of glass",
                    "A city park with paved walkways and electric lights"
                ],
                "correct": 1,
                "explanation": "Sacred Groves (like the Mawphlang Sacred Forest in Meghalaya) are untouched forest patches protected by indigenous spiritual beliefs, acting as critical refuges for rare medicinal plants and wildlife.",
                "study_insight": "In Meghalaya, tradition dictates that anyone who removes even a single leaf from a sacred grove invites bad luck, keeping the ecosystem completely pristine."
            }
        ]
    },
    {
        "id": 10,
        "title": "Hargila Stork",
        "subtitle": "Greater Adjutant Stork & The Women-Led 'Hargila Army' Conservation",
        "concept_html": """
            <p>In the Brahmaputra floodplains of Assam lives one of the rarest, most magnificent wetland birds in Asia: the <strong>Greater Adjutant Stork</strong>, known locally in Assamese as the <strong>Hargila</strong> (meaning 'bone-swallower' due to its enormous bayonet-like bill).</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🪶 Ecological Scavenger Role</span>
                    <p class="text-xs text-slate-300">
                        Standing 1.5 metres tall with a massive 2.5-metre wingspan, the Hargila is nature's vital wetland sanitizer. It feeds on decaying organic matter, dead fish, and rodents, preventing toxic water contamination and disease outbreaks.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">👩 The Inspiring 'Hargila Army'</span>
                    <p class="text-xs text-slate-300">
                        Once hunted and despised because of its noisy nesting in tall village Kadam trees, the bird was brought back from the brink of extinction by biologist <strong>Dr. Purnima Devi Barman</strong> and a rural women-led conservation brigade called the <em>Hargila Army</em>!
                    </p>
                </div>
            </div>
            <p>Today, over 10,000 village women weave Hargila motifs into traditional Assamese handloom textiles, celebrate stork baby-showers, and install safety nets under tall trees to save falling chicks, making Assam the world's greatest stronghold for this endangered stork!</p>
        """,
        "spoken_text": "Meet one of the most astonishing birds of Assam: the Hargila, or Greater Adjutant Stork! Standing five feet tall with an enormous bill, the Hargila is a giant wetland bird. For a long time, villagers disliked the bird because its nests in tall trees smelled bad and made messes, so trees were cut down. But a brave scientist and an army of dedicated village women—known as the Hargila Army—stepped in! They taught everyone that the Hargila is nature's essential garbage cleaner that keeps wetlands sanitary. They built soft safety nets under tall trees to catch falling baby chicks. Today, Assam protects over seventy percent of the world's remaining Hargila storks!",
        "lecture_script": "Presents the Greater Adjutant Stork (Hargila) in Assam, its ecological scavenger role in wetlands, and the community-led conservation movement by the women of the 'Hargila Army'.",
        "checkpoints": [
            {
                "question": "Why is the Greater Adjutant Stork (Hargila) biologically vital for healthy wetland ecosystems in Assam?",
                "options": [
                    "It digs deep trenches for water storage",
                    "It acts as a primary wetland scavenger, feeding on decaying fish, carcasses, and waste, preventing waterborne disease outbreaks",
                    "It carries seeds across oceans to other continents",
                    "It sings loud alarms to warn human villagers of rain"
                ],
                "correct": 1,
                "explanation": "As top wetland scavengers, Hargila storks consume decaying organic waste and carcasses, cleaning aquatic environments and halting the spread of harmful bacterial pathogens.",
                "study_insight": "The word 'Hargila' comes from Sanskrit, meaning 'the swallower of bones', reflecting its powerful digestive system capable of breaking down bone matter."
            },
            {
                "question": "What practical measure did the women-led 'Hargila Army' introduce to rescue baby stork chicks from dying?",
                "options": [
                    "They brought all the birds into indoor cages",
                    "They tied safety nets and cushioned bamboo mats beneath tall nesting trees to catch chicks that accidentally fell from nests",
                    "They cut down all tall trees so birds would nest on the grass",
                    "They fed the chicks synthetic baby formula"
                ],
                "correct": 1,
                "explanation": "Because baby storks frequently fall out of flimsy nests in 70-foot Kadam and Simul trees, the Hargila Army strung wide safety nets below tree branches, nursing rescued chicks back to health before release.",
                "study_insight": "Dr. Purnima Devi Barman received the prestigious UN Champions of the Earth award for spearheading this community conservation model."
            }
        ]
    },
    {
        "id": 11,
        "title": "Root Bridges",
        "subtitle": "Indigenous Bio-Engineering of Meghalaya: Living Architecture",
        "concept_html": """
            <p>In the subtropical rainforests of the <strong>Khasi and Jaintia Hills</strong> of Meghalaya—home to Sohra (Cherrapunji) and Mawsynram, the rainiest places on Earth—raging mountain torrents during monsoons would wash away or rot ordinary wooden or steel suspension bridges within months.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌱 The Rubber Fig (Ficus elastica)</span>
                    <p class="text-xs text-slate-300">
                        Indigenous Khasi communities developed an astonishing system of living architecture known as <strong>Jingkieng Jri</strong> (Living Root Bridges). They plant young rubber fig trees on opposite riverbanks.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🌉 Centuries of Guided Growth</span>
                    <p class="text-xs text-slate-300">
                        Pliant aerial roots are guided across the gorge through hollowed-out betel nut (Areca catechu) trunks. Over 15 to 30 years, roots reach the opposite bank, take firm root in the soil, and interweave into a living, breathing suspension bridge!
                    </p>
                </div>
            </div>
            <p>Unlike concrete or iron bridges that rust, crack, and weaken with time, living root bridges become <strong>stronger every year</strong> as the living roots grow thicker, support up to 50 people simultaneously, and endure for over 500 years!</p>
        """,
        "spoken_text": "Prepare to behold one of the greatest engineering wonders created by humans and nature working as one: the Living Root Bridges of Meghalaya! Meghalaya is the rainiest place on our planet, where rushing monsoon torrents quickly rot ordinary wooden bridges and rust steel beams. Centuries ago, the indigenous Khasi people invented living architecture! They guide the flexible aerial roots of the rubber fig tree across deep roaring gorges inside hollow bamboo trunks. Over decades, the roots reach the opposite bank and anchor into the earth. Unlike concrete bridges that weaken with age, these living bridges grow stronger every single year as the roots thicken, lasting for over five hundred years!",
        "lecture_script": "Explains living root bridges (Jingkieng Jri) in Meghalaya, the biological mechanics of Ficus elastica aerial roots guided across rivers, self-strengthening living architecture, and indigenous Khasi engineering.",
        "checkpoints": [
            {
                "question": "Which tree species provides the flexible aerial roots used by Khasi communities in Meghalaya to cultivate living root bridges?",
                "options": [
                    "Coconut palm",
                    "Indian Rubber Fig (Ficus elastica)",
                    "Neem tree",
                    "Eucalyptus tree"
                ],
                "correct": 1,
                "explanation": "Ficus elastica produces strong, flexible aerial roots that can be guided across river gorges and trained to interweave and anastomose (fuse together) into a living pathway.",
                "study_insight": "The most famous example is the 'Umshiang Double Decker' root bridge in Nongriat village, where two bridges are stacked one above the other!"
            },
            {
                "question": "Why do living root bridges last longer and resist flash floods better than conventional wooden or steel bridges in Meghalaya?",
                "options": [
                    "Because they are covered in waterproof plastic paint",
                    "Because they are living organisms that heal themselves and grow thicker and stronger with every passing year instead of decaying",
                    "Because they float up into the air during floods",
                    "Because they are taken inside houses during rainy days"
                ],
                "correct": 1,
                "explanation": "Traditional man-made materials decay in humid, torrential rain. Because root bridges are living trees, they constantly absorb nutrients, heal structural stress, and increase in mechanical strength over centuries.",
                "study_insight": "A fully mature living root bridge can support the weight of over 50 adult pedestrians simultaneously without shaking."
            }
        ]
    },
    {
        "id": 12,
        "title": "Western Ghats",
        "subtitle": "Global Biodiversity Hotspot Spanning Six Indian States",
        "concept_html": """
            <p>Leaving the misty northeast, our journey traverses to the western spine of peninsular India: the magnificent <strong>Western Ghats</strong> (or <em>Sahyadri</em>), an ancient chain of mountains spanning 1,600 kilometres across six states: <strong>Gujarat, Maharashtra, Goa, Karnataka, Kerala, and Tamil Nadu</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🐒 Lion-Tailed Macaque (Macaca silenus)</span>
                    <p class="text-xs text-slate-300">
                        An endangered arboreal primate living in the evergreen rainforest canopies of the southern Ghats. It features a shiny black coat, an aristocratic silver-white mane framing its face, and a tufted lion-like tail tip.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🐿️ Malabar Giant Squirrel (Ratufa indica)</span>
                    <p class="text-xs text-slate-300">
                        The <strong>State Animal of Maharashtra</strong> (<em>Shekru</em>). A giant multicoloured arboreal squirrel measuring nearly 1 metre in length, capable of making massive 6-metre leaps between canopy branches!
                    </p>
                </div>
            </div>
            <p>Older than the Himalayas, the Western Ghats is recognized as one of the world's <strong>top eight global biodiversity hotspots</strong>, harbouring thousands of flowering plants, amphibians, and butterflies found nowhere else on Earth.</p>
        """,
        "spoken_text": "Now our expedition travels to the great mountain spine of western India: the Western Ghats, also known as the Sahyadris! Older than the mighty Himalayas, this continuous chain of forested ridges runs sixteen hundred kilometres across six states. It is celebrated as one of the world's top eight biodiversity hotspots! High in the rainforest canopy lives the rare Lion-Tailed Macaque, an endangered monkey with a regal silver mane around its face. Leaping from tree to tree is the colourful Malabar Giant Squirrel, which can leap twenty feet through the air in a single bound! These misty mountains are nature's treasure chest.",
        "lecture_script": "Explains the Western Ghats as an ancient mountain range and global biodiversity hotspot, and highlights endemic canopy wildlife: the Lion-Tailed Macaque and the Malabar Giant Squirrel.",
        "checkpoints": [
            {
                "question": "How many Indian states does the mountain range of the Western Ghats span across from north to south?",
                "options": [
                    "2 states",
                    "4 states",
                    "6 states (Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu)",
                    "10 states"
                ],
                "correct": 2,
                "explanation": "The Western Ghats runs 1,600 kilometres parallel to India's western coast across 6 states: Gujarat, Maharashtra, Goa, Karnataka, Kerala, and Tamil Nadu.",
                "study_insight": "The Western Ghats influences the Indian monsoon by intercepting rain-bearing Arabian Sea monsoon winds, triggering heavy orographic precipitation."
            },
            {
                "question": "What striking visual feature distinguishes the endangered Lion-Tailed Macaque of the Western Ghats?",
                "options": [
                    "Bright yellow feathers on its wings",
                    "A striking silver-white mane surrounding its face and a black tuft at the tip of its tail",
                    "Two long curved horns on its head",
                    "Stripes like a zebra across its legs"
                ],
                "correct": 1,
                "explanation": "The Lion-Tailed Macaque has a glossy black body encircled by a prominent halo of silver-white hair around its cheeks and chin, and a tail ending in a tassel resembling a lion's tail.",
                "study_insight": "They feed primarily on rainforest fruits, seeds, and flower nectar, rarely coming down to the forest floor."
            }
        ]
    },
    {
        "id": 13,
        "title": "Mountain Springs",
        "subtitle": "Water Towers of South India & Ancient Rainforest Pharmacy",
        "concept_html": """
            <p>The Western Ghats functions as the ecological <strong>'Water Tower of Peninsular India'</strong>. The dense mossy rainforests act like a giant terrestrial sponge, capturing monsoon rainwater and releasing it gradually through crystal mountain springs throughout the year.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🌊 Birthplace of Peninsular Rivers</span>
                    <p class="text-xs text-slate-300">
                        Major rivers that nourish hundreds of millions of people originate here: the <strong>Godavari</strong> at Trimbakeshwar, the <strong>Krishna</strong> at Mahabaleshwar, and the <strong>Cauvery</strong> at Talakaveri in the Brahmagiri hills.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌿 Natural Living Pharmacy</span>
                    <p class="text-xs text-slate-300">
                        Over <strong>4,000 species of medicinal plants</strong> thrive in the Ghats. Indigenous forest-dwelling communities have used species like <em>Sarpagandha</em> (Rauvolfia serpentina for blood pressure) and <em>Arogyapacha</em> for centuries to cure ailments.
                    </p>
                </div>
            </div>
            <p>If these mountain forests are cleared, rivers dry up into trickles during summer and unleash catastrophic flash floods during monsoons, proving that forest conservation directly protects human water security.</p>
        """,
        "spoken_text": "Did you know that the Western Ghats is the great water tower of South India? The thick carpets of moss, roots, and trees on these mountain slopes act like an enormous sponge! During the monsoon, they soak up millions of litres of rain, and then slowly filter it out through bubbling mountain springs throughout the hot summer. The mighty rivers Godavari, Krishna, and Cauvery all take birth right here on these peaks! These forests are also an ancient living pharmacy, housing thousands of wild healing plants known to traditional healers for centuries. Protecting these hills means protecting the drinking water and health of millions of people!",
        "lecture_script": "Explains the Western Ghats as South India's water tower, the origins of Godavari, Krishna, and Cauvery rivers, sponge effect hydrology, and the rich biodiversity of medicinal plants.",
        "checkpoints": [
            {
                "question": "Which major peninsular river of southern India originates at Talakaveri in the Brahmagiri hills of the Western Ghats?",
                "options": [
                    "Yamuna River",
                    "Cauvery (Kaveri) River",
                    "Indus River",
                    "Ganga River"
                ],
                "correct": 1,
                "explanation": "The sacred river Cauvery originates at Talakaveri in the Kodagu district of Karnataka in the Western Ghats, flowing east across Tamil Nadu into the Bay of Bengal.",
                "study_insight": "The Godavari originates at Trimbakeshwar in Maharashtra, while the Krishna originates at Mahabaleshwar."
            },
            {
                "question": "How do dense forests on mountain slopes function like a 'sponge' for river watersheds?",
                "options": [
                    "They wipe rainwater off the rocks into buckets",
                    "Their organic soil and root networks absorb monsoon rainfall and release it gradually through underground springs, ensuring perennial river flow",
                    "They turn river water into salt water",
                    "They stop all water from leaving the mountain"
                ],
                "correct": 1,
                "explanation": "Forest soil covered in leaf litter has high permeability, absorbing rainwater, refilling underground aquifers, and maintaining steady river flow long after the monsoon ends.",
                "study_insight": "Deforested hills lose water rapidly through surface runoff, causing flash floods followed by severe summer droughts."
            }
        ]
    },
    {
        "id": 14,
        "title": "Citizen Science",
        "subtitle": "Community Biodiversity Mapping & The 200 Mango Varieties",
        "concept_html": """
            <p>Science is not restricted to professional university laboratories with microscopes! In the Western Ghats, students, farmers, and everyday nature lovers actively participate in <strong>Citizen Science</strong>—scientific research conducted collaboratively by ordinary citizens.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🥭 The 200-Mango Survey Discovery</span>
                    <p class="text-xs text-slate-300">
                        In Karnataka and Maharashtra, school students partnered with village elders to document wild and cultivated mango varieties. They recorded over <strong>200 distinct local varieties</strong>—from tiny sweet wild forest mangoes (<em>Appemidi</em> for pickles) to giant fragrant cultivars!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">📱 Modern Biodiversity Apps</span>
                    <p class="text-xs text-slate-300">
                        Using accessible mobile smartphone platforms like the <em>India Biodiversity Portal</em> and <em>iNaturalist</em>, students photograph unknown frogs, butterflies, and trees, allowing global scientists to map species distributions in real-time.
                    </p>
                </div>
            </div>
            <p>Citizen science proves that young students can make real, groundbreaking contributions to national scientific archives and environmental conservation simply through curious, disciplined observation.</p>
        """,
        "spoken_text": "You do not need a white laboratory coat to be a scientist; you can be an active citizen scientist right now! In the Western Ghats, enthusiastic school students took clipboards and cameras to interview village farmers. Together, they documented more than two hundred distinct varieties of mangoes growing in the region! From tiny wild pickling mangoes called Appemidi to giant sweet table fruits, their survey protected rare agricultural varieties from being forgotten. When students like you observe butterflies, record tree flowering times, and map local birds using mobile apps, you help scientists protect the nature around us!",
        "lecture_script": "Explains Citizen Science through student and community biodiversity surveys in the Western Ghats documenting 200+ varieties of wild and cultivated mangoes, and modern mobile mapping apps.",
        "checkpoints": [
            {
                "question": "What is 'Citizen Science' in modern ecological research?",
                "options": [
                    "Buying electronic equipment from foreign countries",
                    "Scientific research and data collection conducted by everyday public citizens, students, and communities in collaboration with scientists",
                    "Reading newspapers in school libraries",
                    "Passing government citizenship examinations"
                ],
                "correct": 1,
                "explanation": "Citizen science democratizes research: ordinary citizens, students, and amateurs collect observations (like bird sightings, tree varieties, or weather data) that scientists use to monitor national biodiversity.",
                "study_insight": "The Great Backyard Bird Count and India's Appemidi mango documentation are famous examples of successful citizen science."
            },
            {
                "question": "What did student citizen scientists in the Western Ghats document that astonished plant geneticists?",
                "options": [
                    "They found plastic trees growing on mountain tops",
                    "They documented over 200 distinct wild and cultivated varieties of local mangoes preserved by communities",
                    "They discovered that mango trees produce apples in winter",
                    "They proved mangoes do not need water to grow"
                ],
                "correct": 1,
                "explanation": "By surveying local orchards, sacred groves, and forest fringes, students discovered more than 200 distinct indigenous mango landraces, protecting diverse genetic traits against climate change.",
                "study_insight": "Appemidi wild mangoes from the Western Ghats of Karnataka possess a pungent aroma and tender flesh so distinct they have received a Geographical Indication (GI) tag."
            }
        ]
    },
    {
        "id": 15,
        "title": "Silent Valley",
        "subtitle": "The Historic People's Movement That Saved a Virgin Rainforest",
        "concept_html": """
            <p>In the Palakkad district of Kerala lies one of India's last undisturbed tracts of South Western Ghats tropical evergreen rainforest: <strong>Silent Valley National Park</strong>. But why is this vibrant forest named 'Silent Valley'?</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-sky-400 block mb-1">🦗 The Mystery of the Silent Canopy</span>
                    <p class="text-xs text-slate-300">
                        In most tropical rainforests, male <strong>cicadas</strong> create a loud, piercing buzzing noise throughout the evening. Early British explorers noticed a curious acoustic phenomenon here: cicadas were virtually absent, creating an ethereal, tranquil silence!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌊 The Save Silent Valley Movement</span>
                    <p class="text-xs text-slate-300">
                        In the 1970s, a hydroelectric dam was proposed across the pristine <strong>Kunthipuzha River</strong> that would have permanently drowned 8.3 sq km of virgin rainforest, threatening the endangered lion-tailed macaque.
                    </p>
                </div>
            </div>
            <p>Led by the <em>Kerala Sasthra Sahithya Parishad (KSSP)</em>, thousands of ecologists, poets like Sugathakumari, students, and citizens united in peaceful environmental activism. Their decade-long campaign forced the government in 1983 to cancel the dam and declare the area a protected National Park!</p>
        """,
        "spoken_text": "Listen to the quiet canopy of Silent Valley National Park in Kerala! Most tropical rainforests buzz loudly at sunset with the piercing screech of cicada bugs. But here, cicadas are largely absent, giving this tranquil valley its famous name: Silent Valley! In the 1970s, an electricity dam was planned across the sparkling Kunthipuzha River. The dam would have drowned this ancient rainforest and wiped out the endangered lion-tailed macaques. But ordinary citizens—ecologists, school students, poets, and villagers—rose together in the historic 'Save Silent Valley Movement'. Their united voices saved the forest, proving that people's peaceful movement can protect our ecological heritage forever!",
        "lecture_script": "Explains Silent Valley National Park in Kerala, the acoustic absence of cicadas, the historic Save Silent Valley public movement against the Kunthipuzha dam, and its landmark ecological victory.",
        "checkpoints": [
            {
                "question": "Why was the pristine rainforest in Palakkad, Kerala named 'Silent Valley' by early naturalists?",
                "options": [
                    "Because birds are forbidden from singing there",
                    "Because noisy cicada insects, which create a loud buzzing drone in other rainforests, are largely absent from this valley",
                    "Because all rivers freeze completely silent during monsoons",
                    "Because tourists are not allowed to talk in the forest"
                ],
                "correct": 1,
                "explanation": "Naturalist Robert Wight noted in 1857 that the loud buzzing call of cicadas—ubiquitous in other tropical forests—was noticeably absent here, creating an unusually serene and silent forest atmosphere.",
                "study_insight": "Silent Valley is also associated with the epic Mahabharata, where it is known locally as Sairandhrivanam, the forest where the Pandavas and Draupadi hid during exile."
            },
            {
                "question": "What historic environmental victory was achieved by the 'Save Silent Valley Movement' in the 1970s and 1980s?",
                "options": [
                    "They constructed the world's tallest concrete dam",
                    "Citizens, students, and scientists successfully prevented a hydroelectric dam on the Kunthipuzha River, saving a virgin rainforest from submergence",
                    "They turned the rainforest into a shopping complex",
                    "They cut down the trees to build an airport"
                ],
                "correct": 1,
                "explanation": "The Save Silent Valley campaign was one of India's earliest successful ecological movements: public rallies, poems, and ecological surveys led Prime Minister Indira Gandhi to scrap the dam in 1983, establishing a protected National Park.",
                "study_insight": "The movement established the principle that economic development must not destroy irreplaceable, million-year-old biological habitats."
            }
        ]
    },
    {
        "id": 16,
        "title": "Eco Sanctuaries",
        "subtitle": "Network of 50+ Protected Sanctuaries & Living in Harmony",
        "concept_html": """
            <p>As our expedition through India's unique places reaches its conclusion, we recognize that nature does not survive by accident; it thrives through deliberate, committed <strong>conservation networks and citizen stewardship</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🛡️ Protected Areas of the Ghats</span>
                    <p class="text-xs text-slate-300">
                        The Indian Government maintains over <strong>50 National Parks, Wildlife Sanctuaries, and Tiger Reserves</strong> across the Western Ghats—including Mudumalai, Bandipur, Periyar, and Anamalai—connecting continuous wildlife corridors.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🤝 Living in Ecological Harmony</span>
                    <p class="text-xs text-slate-300">
                        From the Sentinelese islanders living lightly on coral shores to Khasi villagers training living root bridges and women protecting Hargila storks, India's greatest strength is the ancient wisdom that human survival is inextricably linked with nature's well-being.
                    </p>
                </div>
            </div>
            <p>Every unique place in India—from oceanic coral atolls to muddy mangrove deltas, cloud forests, and mist-clad mountain peaks—is a sacred trust. As young scientists, our lifelong duty is to explore, respect, and defend these living wonders!</p>
        """,
        "spoken_text": "What an unforgettable journey we have shared across India's unique ecological wonders! We stood at Indira Point where island trees balance on buttress roots and colourful corals shelter marine kingdoms. We navigated the muddy Sundarbans where mangroves breathe through snorkels and honey collectors wear face masks to outsmart tigers. We climbed into the mist of Northeast India where living root bridges span roaring rivers and courageous women protect the endangered Hargila stork. And we stood atop the Western Ghats where rain-soaked forests feed mighty rivers and citizens saved Silent Valley. These unique places remind us that we do not own nature; we belong to nature. Let us protect these living treasures for all generations to come!",
        "lecture_script": "Synthesizes the journey across Andaman islands, Sundarbans mangroves, Northeast cloud forests, and Western Ghats, emphasizing protected wildlife corridors and citizen stewardship.",
        "checkpoints": [
            {
                "question": "Why is it vital to maintain continuous 'wildlife corridors' connecting different national parks and sanctuaries across mountain ranges like the Western Ghats?",
                "options": [
                    "So tourists can drive sports cars between forests",
                    "To allow large animals like elephants and tigers to migrate freely across seasons to find food, water, and mates without human conflict",
                    "To build long rows of shopping centres in the forest",
                    "To build high concrete fences separating all trees"
                ],
                "correct": 1,
                "explanation": "Wildlife corridors prevent forest fragmentation: they allow wide-ranging animals (such as elephant herds and tigers) to move safely between seasonal feeding grounds, preventing genetic inbreeding and reducing road accidents.",
                "study_insight": "The Elephant Corridor project across the Western Ghats protects traditional migratory pathways used by pachyderms for centuries."
            },
            {
                "question": "What common ecological lesson connects the Sentinelese, Khasi bridge builders, Hargila Army, and Save Silent Valley activists?",
                "options": [
                    "That forests should be rapidly cleared for industries",
                    "That human prosperity and safety depend on understanding, respecting, and protecting the living ecosystems around us",
                    "That modern cities do not need water from rivers",
                    "That only scientists are allowed to care about nature"
                ],
                "correct": 1,
                "explanation": "Across all of India's unique places, the central enduring truth is that indigenous knowledge, community stewardship, and peaceful conservation are essential to preserve the living web of life that sustains us all.",
                "study_insight": "As Mahatma Gandhi wisely said: 'Earth provides enough to satisfy every man's need, but not every man's greed.'"
            }
        ]
    }
]

print(f"Part 2 slides defined: {len(SLIDES_PART2)}")

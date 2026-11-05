"""
Part 1 of NCERT Class 5 Science Chapter 5: Our Vibrant Country
Slides 1 to 8
Short Headings (1-3 words) with exact same meaning:
1. Republic Day
2. The Constitution
3. Currency Secrets
4. Accessible Money
5. National Emblem
6. The Tiger
7. The Peacock
8. Sacred Symbols
"""

import sys

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Republic Day",
        "subtitle": "National Pride, Tricolour Unfurling & The Grand New Delhi Parade",
        "concept_html": """
            <p>Every year on <strong>January 26th</strong>, our entire nation joins together in celebration of <strong>Republic Day</strong>. Schools across cities, towns, and villages begin the morning with students gathering around the central flagpole to witness the majestic unfurling of the Indian Tricolour flag (Tiranga), showered with rose petals as it rises to the breeze.</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-orange-950/40 border border-orange-500/30">
                    <span class="font-bold text-orange-400 block mb-1">Saffron (Kesari)</span>
                    <span>Top band representing supreme courage, sacrifice, and the strength of our people.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700">
                    <span class="font-bold text-slate-200 block mb-1">White & Navy Chakra</span>
                    <span>Middle band of peace and truth, bearing the 24-spoke Ashoka Chakra denoting continuous righteous progress.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="font-bold text-emerald-400 block mb-1">Green (Hara)</span>
                    <span>Bottom band symbolising fertility, growth, auspiciousness, and the rich agricultural bounty of India.</span>
                </div>
            </div>
            <p>As the flag unfurls, students stand in disciplined attention to sing the <strong>National Anthem</strong>, <em>Jana Gana Mana</em>, composed by Rabindranath Tagore. Its lyrics celebrate the grand geographic expanse of our motherland—tracing sacred rivers like the Ganga and Yamuna, mountain chains like the Himalayas and Vindhyas, and coastal ocean shores.</p>
            <p>In New Delhi along Kartavya Path, the grand parade showcases the brave Indian Defence Forces, supersonic aircraft flypasts, and colourful state tableaux displaying the diverse arts, architectures, and cultural folk dances from every corner of India.</p>
        """,
        "spoken_text": "Good morning students! Today we embark on an inspiring journey across our homeland in Chapter 5: Our Vibrant Country. Every year on January 26th, India comes alive celebrating Republic Day. We gather around our school flagpole, watching our proud tricolour unfurl towards the blue sky as fragrant flower petals flutter down. We stand tall singing Jana Gana Mana, a poetic salute celebrating our great rivers like the Ganga and Yamuna, and majestic peaks like the Himalayas. In New Delhi, the grand Republic Day parade presents state tableaux celebrating our unmatched diversity, alongside our courageous defence forces.",
        "lecture_script": "Explains Republic Day, the symbolism of the Tricolour bands and the 24-spoke Ashoka Chakra, singing the National Anthem referencing India's rivers and mountains, and the New Delhi parade.",
        "checkpoints": [
            {
                "question": "What does the 24-spoke navy blue Ashoka Chakra at the centre of the Indian flag signify?",
                "options": [
                    "24 seasons of the agrarian calendar",
                    "Continuous righteous motion and 24 hours of purposeful national progress",
                    "24 major languages spoken across India",
                    "24 mountain ranges in the Himalayas"
                ],
                "correct": 1,
                "explanation": "The 24 spokes of the navy blue Ashoka Chakra represent the 24 hours of the day, signifying that there is life in movement and death in stagnation; our nation must constantly advance in truth and righteousness.",
                "study_insight": "The Ashoka Chakra is adapted from the Lion Capital of Emperor Ashoka at Sarnath, dating back to the 3rd century BCE."
            },
            {
                "question": "Which two majestic geographical features are celebrated within the lyrics of the Indian National Anthem?",
                "options": [
                    "Thar Desert and Rann of Kutch",
                    "Vindhyas, Himalayas, and rivers Yamuna and Ganga",
                    "Western Ghats and Sunderbans",
                    "Deccan Plateau and Nilgiri Hills"
                ],
                "correct": 1,
                "explanation": "Jana Gana Mana specifically glorifies India's geography with 'Uchchala-Jaladhi-Taranga, Vindhya-Himachala-Yamuna-Ganga', highlighting our eternal mountains and life-giving rivers.",
                "study_insight": "Singing the national anthem takes approximately 52 seconds and instills a shared sense of patriotic unity."
            }
        ]
    },
    {
        "id": 2,
        "title": "The Constitution",
        "subtitle": "The Supreme Law of the Land, Democratic Values & Peaceful Governance",
        "concept_html": """
            <p>While India attained independence from colonial rule on <strong>August 15, 1947</strong>, our country required its own foundational book of supreme laws to safeguard citizen rights, ensure justice, and guide democratic governance. On <strong>January 26, 1950</strong>, the <strong>Constitution of India</strong> came into full legal effect.</p>
            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 my-3">
                <span class="text-xs font-bold text-indigo-400 block mb-1">The Architecture of Our Supreme Rulebook</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Prepared under the leadership of <strong>Dr. Bhimrao Ramji Ambedkar</strong>, Chairman of the Drafting Committee, the Indian Constitution is the longest written national constitution in the world. It guarantees Fundamental Rights to all citizens regardless of religion, caste, gender, or birthplace.
                </p>
            </div>
            <p>Just as a school playground needs clear game rules so that every child can play fairly and safely without bullies taking over, a massive nation of over 1.4 billion people needs a shared Constitution. It defines how laws are made by Parliament, enforced by the government, and protected by independent courts of law.</p>
            <p>The Constitution also outlines our <strong>Fundamental Duties</strong>—reminding every child to protect public property, defend natural environments including forests and wildlife, strive towards excellence, and cherish our composite culture.</p>
        """,
        "spoken_text": "Did you know that gaining freedom on August 15, 1947 was only the first step? To ensure that every single citizen is treated with fairness and respect, India needed a supreme rulebook. That sacred book is the Constitution of India, adopted on January 26, 1950, which is why we celebrate Republic Day! Drafted under the visionary guidance of Dr. B. R. Ambedkar, our Constitution guarantees justice, equality, and liberty to all. Just as sports need strict rules so every student plays happily without bullying, our Constitution ensures peaceful harmony across our nation.",
        "lecture_script": "Distinguishes Independence Day from Republic Day, explains why a nation needs a written Constitution, Dr. B.R. Ambedkar's role, and the balance of fundamental rights with duties.",
        "checkpoints": [
            {
                "question": "Why is Republic Day celebrated specifically on January 26th rather than August 15th?",
                "options": [
                    "August 15th marks independence, while January 26, 1950 marks the adoption of India's Constitution",
                    "January 26th is the birth anniversary of Rabindranath Tagore",
                    "The Red Fort in Delhi was constructed on January 26th",
                    "India won its first hockey Olympic gold on that day"
                ],
                "correct": 0,
                "explanation": "Independence Day on August 15, 1947 celebrated freedom from foreign rule, whereas Republic Day on January 26, 1950 celebrated India establishing its own supreme democratic Constitution.",
                "study_insight": "January 26 was chosen because in 1930, the Indian National Congress had declared Purna Swaraj (complete self-rule) on that exact date."
            },
            {
                "question": "Who served as the Chairman of the Drafting Committee that formulated the Constitution of India?",
                "options": [
                    "Sardar Vallabhbhai Patel",
                    "Dr. B. R. Ambedkar",
                    "Subhas Chandra Bose",
                    "Sarojini Naidu"
                ],
                "correct": 1,
                "explanation": "Dr. Bhimrao Ramji Ambedkar chaired the Drafting Committee, harmonising democratic principles to ensure social justice and fundamental equality for all Indian citizens.",
                "study_insight": "The original Constitution of India was handwritten in beautiful calligraphy by Prem Behari Narain Raizada, with exquisite illustrations by Nandalal Bose."
            }
        ]
    },
    {
        "id": 3,
        "title": "Currency Secrets",
        "subtitle": "Micro-Details, Security Features & The Swachh Bharat Spectacles",
        "concept_html": """
            <p>Every Indian bank note—from ₹10 to ₹500—is not merely paper for buying supplies; it is an incredible canvas of Indian history, scientific engineering, and national ideals designed by the <strong>Reserve Bank of India (RBI)</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🔍 Hidden Optical Watermark</span>
                    <p class="text-xs text-slate-300">
                        When held up against sunlight or a lamp, a glowing translucent portrait of <strong>Mahatma Gandhi</strong> and the numerical denomination appear inside the blank white watermark window.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">👓 Swachh Bharat Spectacles</span>
                    <p class="text-xs text-slate-300">
                        Turn the note over! Beneath the central image, you will spot a pair of round spectacles with the words <em>'Swachh'</em> on the left lens and <em>'Bharat'</em> on the right lens, promoting national cleanliness.
                    </p>
                </div>
            </div>
            <p>Currency notes also feature historical monuments that celebrate India's architectural and cultural glory: the Konark Sun Temple Wheel on the ₹10 note, the Ellora Caves on the ₹20 note, Hampi Stone Chariot on the ₹50 note, Rani ki Vav stepwell on the ₹100 note, Sanchi Stupa on the ₹200 note, and Delhi's Red Fort on the ₹500 note.</p>
            <p>Across the back of each note is the <strong>Language Panel</strong>, printing the value in 15 distinct official Indian regional languages in addition to English and Hindi on the front, demonstrating linguistic inclusion.</p>
        """,
        "spoken_text": "Take a close look at an Indian currency note, like a ten-rupee or five-hundred-rupee note. It is packed with fascinating scientific and patriotic secrets! If you hold it up towards the sunlight, an invisible watermark of Mahatma Gandhi smiles back at you. Flip the note around, and you will spot a small pair of round spectacles. These glasses carry the slogan of the Swachh Bharat Mission, reminding us that cleanliness is a national service. You will also discover famous Indian monuments, and a language panel proudly displaying the note's value in fifteen different regional scripts!",
        "lecture_script": "Walks through security features on Indian currency notes: Mahatma Gandhi watermark, Swachh Bharat Abhiyan spectacles logo, architectural monuments, and the 15-language panel.",
        "checkpoints": [
            {
                "question": "What national mission is represented on the reverse of modern Indian currency notes by a pair of round spectacles?",
                "options": [
                    "Digital India Mission",
                    "Swachh Bharat Abhiyan (Clean India Mission)",
                    "Make in India",
                    "National Solar Mission"
                ],
                "correct": 1,
                "explanation": "The round spectacles of Mahatma Gandhi with 'Swachh Bharat' printed inside the lenses represent the nationwide Swachh Bharat Abhiyan, urging citizens to maintain clean surroundings.",
                "study_insight": "Gandhiji believed that sanitation and cleanliness are just as vital as political independence."
            },
            {
                "question": "How many regional languages are printed within the language panel on the reverse of an Indian rupee banknote?",
                "options": [
                    "5 languages",
                    "10 languages",
                    "15 languages",
                    "28 languages"
                ],
                "correct": 2,
                "explanation": "The language panel on the reverse displays the denomination in 15 regional Indian languages, in addition to Hindi and English displayed on the front of the note.",
                "study_insight": "The languages appear in alphabetical order according to the English spelling of each language name."
            }
        ]
    },
    {
        "id": 4,
        "title": "Accessible Money",
        "subtitle": "Intaglio Tactile Markings, Bleed Lines & Assistive MANI Technology",
        "concept_html": """
            <p>How does a visually impaired person identify whether a bill in their hand is a ₹20, ₹100, or ₹500 note without having to ask someone else? Indian currency notes incorporate ingenious <strong>universal accessibility design</strong>.</p>
            <div class="space-y-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/70 flex items-start space-x-2.5">
                    <span class="text-base">🖐️</span>
                    <div>
                        <strong class="text-emerald-400">Raised Intaglio Printing:</strong>
                        <span class="text-slate-300"> The portrait of Mahatma Gandhi, the Reserve Bank seal, and the denomination numerals are printed using raised relief ink that can be instantly felt by fingertips.</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/70 flex items-start space-x-2.5">
                    <span class="text-base">📐</span>
                    <div>
                        <strong class="text-indigo-400">Raised Angular Bleed Lines & Shapes:</strong>
                        <span class="text-slate-300"> Higher denomination notes feature raised diagonal lines along the edges: 4 bleed lines on ₹100 with a triangle, 4 lines with 2 circles on ₹200, and 5 bleed lines with a circle on ₹500.</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/70 flex items-start space-x-2.5">
                    <span class="text-base">📱</span>
                    <div>
                        <strong class="text-amber-400">MANI Assistive Mobile App:</strong>
                        <span class="text-slate-300"> The Reserve Bank of India developed the <em>Mobile Aided Note Identifier (MANI)</em> app. By holding a smartphone camera over any note, the app instantly identifies the denomination offline and speaks it aloud through audio or vibration cues.</span>
                    </div>
                </div>
            </div>
            <p>In addition, each denomination increases progressively in physical length and width, providing natural tactile size differentiation when stacked together in a wallet.</p>
        """,
        "spoken_text": "Have you ever wondered how people with visual challenges know the value of a currency note? India's currency includes wonderful accessibility features! Using special raised intaglio printing, the portrait of Mahatma Gandhi and distinct geometric marks can be felt with your fingertips. For example, the five-hundred-rupee note features five raised angular bleed lines on each border. Moreover, the Reserve Bank created a smart mobile app called MANI—Mobile Aided Note Identifier—which scans the note with a smartphone camera and speaks the value aloud, ensuring financial independence for everyone.",
        "lecture_script": "Explains universal design in Indian currency: raised intaglio tactile printing, angular bleed lines, size differentiation, and the RBI's MANI assistive smartphone app.",
        "checkpoints": [
            {
                "question": "What is the primary function of the raised angular bleed lines along the edges of higher-value banknotes?",
                "options": [
                    "To prevent the note from tearing at the corners",
                    "To allow visually impaired people to identify denominations by touch",
                    "To show where the note should be folded",
                    "To indicate the year the note was printed"
                ],
                "correct": 1,
                "explanation": "Raised angular bleed lines and geometric shapes printed in intaglio ink enable visually impaired citizens to discern the exact note denomination through tactile fingertip touch.",
                "study_insight": "Different denominations feature different counts of bleed lines: ₹100 has 4 lines, ₹200 has 4 with circles, and ₹500 has 5 lines."
            },
            {
                "question": "What is the full name of the assistive mobile app developed by the RBI to help people identify currency denominations?",
                "options": [
                    "BHIM (Bharat Interface for Money)",
                    "MANI (Mobile Aided Note Identifier)",
                    "UMANG (Unified Mobile Application)",
                    "AADHAAR Financial Scanner"
                ],
                "correct": 1,
                "explanation": "MANI stands for Mobile Aided Note Identifier. It scans currency notes using phone cameras even when offline and announces the denomination via voice audio or haptic vibration.",
                "study_insight": "MANI does not verify whether a currency note is authentic or counterfeit; it purely identifies denomination."
            }
        ]
    },
    {
        "id": 5,
        "title": "National Emblem",
        "subtitle": "The Sarnath Lion Capital, Satyameva Jayate & The Gir Lion Miracle",
        "concept_html": """
            <p>The <strong>State Emblem of India</strong> is an adaptation of the ancient sandstone <strong>Lion Capital of Ashoka</strong>, carved around 250 BCE at Sarnath, Uttar Pradesh, where Gautama Buddha first taught his message of peace and compassion.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🏛️ Anatomy of the Emblem</span>
                    <p class="text-xs text-slate-300">
                        Four Asiatic lions stand back-to-back mounted on a circular abacus (three are visible in 2D views, while the fourth is hidden behind). Below them is the Ashoka Chakra flanked by a galloping horse on the left (energy and speed) and a humped bull on the right (steadfast hard work).
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">📜 Satyameva Jayate</span>
                    <p class="text-xs text-slate-300">
                        Inscribed below the base in Devanagari script is our sacred national motto: <em>'सत्यमेव जयते'</em> (<strong>Truth Alone Triumphs</strong>), drawn from the ancient <em>Mundaka Upanishad</em>.
                    </p>
                </div>
            </div>
            <p>The lions symbolise courage, power, and guardianship. In the wild, India is home to the world's only surviving population of <strong>Asiatic Lions</strong> in the dry deciduous forests of <strong>Gir National Park, Gujarat</strong>. Once reduced to barely 20 animals due to hunting a century ago, rigorous community-led conservation has revived their numbers to over 670 majestic lions today!</p>
        """,
        "spoken_text": "Look closely at any official government document, coin, or passport, and you will see our National Emblem! It is adapted from the great Lion Capital erected by Emperor Ashoka over two thousand two hundred years ago at Sarnath. Four majestic Asiatic lions stand back-to-back, symbolising courage and vigilance, though in drawings we only see three. Underneath, our national motto proclaims in Devanagari: Satyameva Jayate, meaning Truth Alone Triumphs. India is also blessed to be the exclusive home of wild Asiatic lions in Gujarat's Gir forest, protected through proud conservation efforts.",
        "lecture_script": "Explains the State Emblem of India adapted from Sarnath Lion Capital, the four lions, the horse and bull, the motto Satyameva Jayate, and Asiatic lion conservation in Gir, Gujarat.",
        "checkpoints": [
            {
                "question": "What is the meaning of the national motto 'Satyameva Jayate' inscribed below the National Emblem?",
                "options": [
                    "Unity is Our Strength",
                    "Truth Alone Triumphs",
                    "Peace Above All",
                    "Knowledge is Immortal"
                ],
                "correct": 1,
                "explanation": "'Satyameva Jayate' is a Sanskrit phrase from the Mundaka Upanishad that translates to 'Truth Alone Triumphs', reminding citizens and leaders that justice and truth always prevail.",
                "study_insight": "The motto was chosen by national leaders including Pandit Madan Mohan Malaviya and adopted on January 26, 1950."
            },
            {
                "question": "Where is the only natural wild habitat of the Asiatic Lion located in India?",
                "options": [
                    "Kaziranga National Park, Assam",
                    "Gir Forest National Park, Gujarat",
                    "Jim Corbett National Park, Uttarakhand",
                    "Sundarbans Mangrove Forest, West Bengal"
                ],
                "correct": 1,
                "explanation": "The Gir National Park and Wildlife Sanctuary in Gujarat is the only place on Earth where the Asiatic lion (Panthera leo persica) thrives in the wild.",
                "study_insight": "Asiatic lions have a distinct longitudinal fold of skin running along their belly, a feature rarely seen in African lions."
            }
        ]
    },
    {
        "id": 6,
        "title": "The Tiger",
        "subtitle": "Apex Forest Predator, Natural Camouflage & Project Tiger",
        "concept_html": """
            <p>The majestic <strong>Royal Bengal Tiger</strong> (<em>Panthera tigris</em>) was declared the <strong>National Animal of India</strong> in 1973. Renowned for its grace, strength, and agility, the tiger reigns as the apex predator across India's varied ecosystems—from the snowy foothills of Uttarakhand to the tidal mangrove swamps of the Sundarbans.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-orange-950/40 border border-orange-500/30">
                    <span class="text-xs font-bold text-orange-400 block mb-1">🌿 Striped Camouflage & Biology</span>
                    <p class="text-xs text-slate-300">
                        No two tigers possess the exact same pattern of vertical dark stripes! In the dappled sunlight of grasslands and forests, these stripes break up the tiger's outline, making it practically invisible to prey like spotted deer and wild boar.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🛡️ Project Tiger Success Story</span>
                    <p class="text-xs text-slate-300">
                        Launched in 1973 at Corbett National Park, <strong>Project Tiger</strong> established dedicated core sanctuaries free from human interference. Today, India is home to more than 75% of the world's wild tigers (over 3,600 tigers)!
                    </p>
                </div>
            </div>
            <p>Tigers are known as an <strong>umbrella species</strong>. When we protect one tiger, we automatically protect its entire territory—thousands of hectares of lush forests, life-giving river watersheds, and hundreds of species of birds, insects, and deer.</p>
        """,
        "spoken_text": "With its glowing amber coat and dramatic black stripes, the Royal Bengal Tiger is India's National Animal. A tiger's stripes are as unique as human fingerprints; no two tigers on Earth have identical patterns! In tall grass, these stripes camouflage the tiger completely, enabling it to stalk silently on padded paws. Through India's pioneering Project Tiger launched in 1973, we turned the tide against poaching and habitat loss. Today, India proudly protects over three-quarters of the entire planet's wild tiger population, preserving forest biodiversity across the subcontinent.",
        "lecture_script": "Explains the Royal Bengal Tiger as India's National Animal, unique stripe patterns, predatory camouflage, the umbrella species concept, and Project Tiger's success.",
        "checkpoints": [
            {
                "question": "Why is the tiger described as an 'umbrella species' by wildlife biologists?",
                "options": [
                    "Because tigers use forest leaf canopies as shelter from heavy monsoon rains",
                    "Because conserving the tiger's habitat automatically protects all other plants, rivers, and animals within that forest",
                    "Because tigers hunt animals that destroy shade trees",
                    "Because tigers have wide protective paws shaped like umbrellas"
                ],
                "correct": 1,
                "explanation": "An umbrella species requires a vast, healthy ecosystem to survive. By conserving large tiger reserves, we simultaneously safeguard rivers, forests, herbivores, insects, and birds living under that 'umbrella'.",
                "study_insight": "A single adult tiger's territory can span between 20 to 100 square kilometres depending on prey availability."
            },
            {
                "question": "What is unique about the dark vertical stripe pattern found on a tiger's coat?",
                "options": [
                    "The stripes disappear during winter months",
                    "Every tiger has an entirely unique stripe pattern, just like human fingerprints",
                    "Male and female tigers have identical stripe counts",
                    "The stripes are painted by other tigers using tree sap"
                ],
                "correct": 1,
                "explanation": "Every tiger has a completely unique stripe arrangement that remains on its skin even if shaved. Forest rangers use camera-trap stripe matching to identify individual tigers.",
                "study_insight": "A tiger's roar can be heard echoing through the forest up to 3 kilometres away!"
            }
        ]
    },
    {
        "id": 7,
        "title": "The Peacock",
        "subtitle": "Iridescent Photonic Feathers, Cultural Lore & The Monsoon Dance",
        "concept_html": """
            <p>Declared the <strong>National Bird of India</strong> in 1963, the <strong>Indian Peafowl</strong> (<em>Pavo cristatus</em>) is celebrated for its unmatched elegance, rich cultural mythology, and close connection with the arrival of life-giving monsoon rains.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-500/30">
                    <span class="text-xs font-bold text-sky-400 block mb-1">🪶 The Science of Iridescence</span>
                    <p class="text-xs text-slate-300">
                        The brilliant emerald greens and shimmering sapphire blues of the peacock's long train are not caused by chemical dye pigments! Instead, microscopic two-dimensional photonic crystal structures on the feather barbules reflect light at specific wavelengths, shifting hues as the bird moves.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                    <span class="text-xs font-bold text-indigo-400 block mb-1">🌧️ The Joyous Rain Dance</span>
                    <p class="text-xs text-slate-300">
                        When heavy monsoon clouds gather and cool moist winds blow across parched plains, male peacocks fan out their magnificent iridescent trains into a giant circular disc, quivering their feathers with a distinct rustling sound to attract peahens.
                    </p>
                </div>
            </div>
            <p>Peacocks are deeply woven into Indian heritage—adorning the crown of Lord Krishna, depicted in classical temple sculptures, and inspiring exquisite classical dance postures such as the <em>Mayura Mudra</em>.</p>
        """,
        "spoken_text": "Now turn your gaze to the skies and forest clearings for our National Bird: the Indian Peafowl, or Peacock! Its glittering blue neck and magnificent fanned tail have captivated Indian poets, dancers, and artists for thousands of years. But here is an astonishing scientific fact: the glowing blues and greens of its feathers are not made of coloured ink or pigment! They are created by tiny microscopic crystals on the feather surface that reflect light like prisms. When dark monsoon clouds roll in, the peacock fans its tail into a giant shimmering halo, dancing in celebration of the coming rain.",
        "lecture_script": "Explains the Indian Peafowl as the National Bird, the physics of feather iridescence, the courtship monsoon dance, and its cultural presence in classical dance mudras.",
        "checkpoints": [
            {
                "question": "What scientific physical property produces the vivid shifting blue and green colours of a peacock's train feathers?",
                "options": [
                    "Deep blue chemical ink absorbed from berry seeds",
                    "Microscopic photonic crystalline structures that bend and reflect light waves (structural colouration)",
                    "Algae growing on the surface of the feathers",
                    "Bioluminescent bacteria glowing under moonlight"
                ],
                "correct": 1,
                "explanation": "Peacock feathers exhibit structural colouration: nanometre-scale keratin and melanin structures on the feather barbules interfere with light waves to produce vibrant, shifting iridescent colours without chemical pigments.",
                "study_insight": "Only male birds (peacocks) possess the long ornamental eye-spotted train; females (peahens) are mottled brown for nest camouflage."
            },
            {
                "question": "Which season is traditionally associated with the famous circular fanned dance of the Indian peacock?",
                "options": [
                    "Peak dry summer in May",
                    "Arrival of the monsoon rains with dark cloudy skies",
                    "Harsh winter frost in December",
                    "Post-harvest autumn festivals"
                ],
                "correct": 1,
                "explanation": "Peacocks display their spectacular fanned courtship dance during the monsoon season, when cloudy skies, humidity, and thunder trigger energetic displays.",
                "study_insight": "In classical Indian dance traditions like Bharatanatyam and Kathak, dancers use the Mayura Mudra (hand gesture) to signify the peacock."
            }
        ]
    },
    {
        "id": 8,
        "title": "Sacred Symbols",
        "subtitle": "The Banyan Tree, Lotus, River Dolphin & Elephant Heritage",
        "concept_html": """
            <p>Beyond the tiger and peacock, India's national emblems encompass sacred botanical wonders, aquatic marvels, and gentle forest giants that reflect our deep reverence for nature.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-emerald-400 block mb-0.5">🌳 National Tree: Banyan (Kalpavriksha)</span>
                    <span class="text-slate-300"><em>Ficus benghalensis</em> sends down thick aerial prop roots from its horizontal branches, creating sprawling, pillar-like canopies that shelter whole villages and live for centuries.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-pink-400 block mb-0.5">🪷 National Flower: Lotus (Kamal)</span>
                    <span class="text-slate-300"><em>Nelumbo nucifera</em> roots in muddy pond bottoms yet emerges with clean, pristine petals. Its leaves have a microscopic waxy texture that repels water droplets—the famous <em>Lotus Effect</em>.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-cyan-400 block mb-0.5">🐬 National Aquatic Animal: Ganges River Dolphin</span>
                    <span class="text-slate-300">The <em>Susu</em> (<em>Platanista gangetica</em>) is virtually blind in murky river silt; it navigates and hunts fish using high-frequency ultrasonic echolocation clicks.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-amber-400 block mb-0.5">🐘 National Heritage Animal: Indian Elephant</span>
                    <span class="text-slate-300"><em>Elephas maximus</em> shapes forest corridors, disperses seeds across vast distances, and holds a sacred position in Indian folklore and festival traditions.</span>
                </div>
            </div>
            <p>Each of these living treasures reminds us that ancient India recognized ecological balance as an essential sacred duty centuries before modern conservation science arose.</p>
        """,
        "spoken_text": "Our vibrant national symbols extend far into the plant and animal kingdoms! The majestic Banyan tree, our National Tree, spreads its massive branches and drops aerial roots down into the soil, creating giant shady sanctuaries that endure for hundreds of years. The pink Lotus, our National Flower, blossoms untainted above muddy waters, showcasing its super-clean water-repellent leaves. In our sacred rivers swims the Ganges River Dolphin, our National Aquatic Animal, navigating murky waters using ultrasonic echolocation clicks. And roaming our dense forests is the Indian Elephant, our National Heritage Animal, revered as a wise guardian of biodiversity.",
        "lecture_script": "Presents India's national natural heritage: Banyan tree (aerial prop roots), Lotus (Nelumbo nucifera and lotus effect), Ganges River Dolphin (echolocation), and Indian Elephant.",
        "checkpoints": [
            {
                "question": "How does the Ganges River Dolphin navigate and locate fish in turbid, muddy river waters?",
                "options": [
                    "Using powerful night-vision eyes with glowing retinas",
                    "Using ultrasonic echolocation clicks that bounce off objects in the water",
                    "By detecting electric fields using long whiskers",
                    "By swimming only along the sunny surface of the river"
                ],
                "correct": 1,
                "explanation": "Because the silt-heavy waters of the Ganga and Brahmaputra are murky, the Ganges River Dolphin has rudimentary eyes without lenses; it emits ultrasonic echolocation clicks to 'see' its aquatic surroundings through sound echoes.",
                "study_insight": "The dolphin surfaces every 30 to 120 seconds to breathe air, making a characteristic puffing sound called 'Susu'."
            },
            {
                "question": "What biological adaptation allows the Banyan tree (Ficus benghalensis) to expand outward over massive land areas?",
                "options": [
                    "Stems that burrow horizontally through deep bedrock",
                    "Aerial prop roots growing downward from horizontal branches that root into the earth as secondary trunks",
                    "Seeds that explode outward like mini-fireworks",
                    "Leaves that float across ponds to sprout new clones"
                ],
                "correct": 1,
                "explanation": "The Banyan produces aerial roots from horizontal limbs. Upon reaching the ground, they thicken into stout woody pillars, supporting heavy branches and allowing the tree to spread over vast areas.",
                "study_insight": "The Great Banyan Tree in Howrah, West Bengal, has a canopy circumference of nearly half a kilometre and over 3,000 aerial roots!"
            }
        ]
    }
]

print(f"Part 1 slides defined: {len(SLIDES_PART1)}")


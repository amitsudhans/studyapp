"""
Part 2 of NCERT Class 5 Science Chapter 5: Our Vibrant Country
Slides 9 to 16
Short Headings (1-3 words) with exact same meaning:
9. Many Languages
10. Forest Metaphor
11. Regional Headgear
12. Rhythm Drums
13. Classical Dances
14. Ancient Wisdom
15. Modern Progress
16. United Fabric
"""

import sys

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Many Languages",
        "subtitle": "A Thousand Living Tongues, Diverse Scripts & Eighth Schedule Heritage",
        "concept_html": """
            <p>One of the most extraordinary wonders of India is our linguistic richness. Over <strong>one thousand distinct mother tongues and dialects</strong> are spoken across the length and breadth of our country, each carrying centuries of poetry, folklore, lullabies, and scientific wisdom.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">📜 The Eighth Schedule</span>
                    <p class="text-xs text-slate-300">
                        The Constitution of India formally recognizes <strong>22 official languages</strong> in the Eighth Schedule, including Assamese, Bengali, Gujarati, Hindi, Kannada, Kashmiri, Malayalam, Marathi, Odia, Punjabi, Sanskrit, Tamil, Telugu, and Urdu.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🔤 Ancient Scripts & Phonetics</span>
                    <p class="text-xs text-slate-300">
                        Most Indian scripts—including Devanagari, Bengali, Gurmukhi, and Tamil—evolved from the ancient <strong>Brahmi script</strong>. Their phonetic systems are scientifically organized by place of articulation (throat, palate, teeth, lips).
                    </p>
                </div>
            </div>
            <p>Traveling just 100 kilometres in India often brings a new dialect, new idioms, and new greeting customs. Despite having different alphabets and pronunciations, Indian languages share common cultural roots, philosophical concepts, and deep emotional warmth.</p>
        """,
        "spoken_text": "Imagine stepping into a magical library where over one thousand different tongues are spoken! That living library is India. Across our states, people speak hundreds of regional languages and dialects, each blessed with enchanting songs, bedtime tales, and profound literature. The Constitution of India recognizes twenty-two official languages in its Eighth Schedule. What is fascinating is that most Indian writing systems descend from the ancient Brahmi script, scientifically arranging sounds from the back of the throat to the tip of your lips. While our words may sound different, they speak the same universal message of love and fellowship.",
        "lecture_script": "Explains India's linguistic diversity, the 22 languages recognized in the Eighth Schedule, the evolution of Indian scripts from Brahmi, and the scientific phonetic organization of Indian alphabets.",
        "checkpoints": [
            {
                "question": "How many official regional languages are recognized under the Eighth Schedule of the Indian Constitution?",
                "options": [
                    "12 languages",
                    "18 languages",
                    "22 languages",
                    "36 languages"
                ],
                "correct": 2,
                "explanation": "The Eighth Schedule of the Constitution currently recognizes 22 official languages, providing each with institutional support and cultural dignity.",
                "study_insight": "English and Hindi are the official languages used for union government administrative communication."
            },
            {
                "question": "From which ancient mother script did most modern Indian writing systems (like Devanagari, Bengali, and Tamil) evolve?",
                "options": [
                    "Egyptian Hieroglyphics",
                    "Ancient Brahmi Script",
                    "Roman Alphabet",
                    "Cuneiform Script"
                ],
                "correct": 1,
                "explanation": "The Brahmi script, visible on Emperor Ashoka's rock pillars from the 3rd century BCE, is the ancestral source of almost all modern Indian writing scripts.",
                "study_insight": "Indian alphabets are arranged scientifically: vowels first, followed by consonants classified by tongue contact points."
            }
        ]
    },
    {
        "id": 10,
        "title": "Forest Metaphor",
        "subtitle": "Ecosystem Resilience: Why Diversity Makes India Unbreakable",
        "concept_html": """
            <p>Why is diversity a country's greatest strength rather than a weakness? In science, we can understand human society by observing the contrast between a <strong>man-made garden</strong> and a <strong>natural forest ecosystem</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🏡 The Monoculture Garden</span>
                    <p class="text-xs text-slate-300">
                        A lawn or rose garden features only one or two plant varieties. It requires artificial watering, chemical fertilizers, and constant weed removal. If a single fungus or insect pest attacks, the entire garden can wither and perish overnight.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌲 The Self-Sustaining Forest</span>
                    <p class="text-xs text-slate-300">
                        A virgin forest thrives without human gardeners! Tall teak trees, thorny shrubs, climbing vines, deep mosses, predatory birds, earthworms, and soil fungi form a robust web. If one species suffers, other species step in, maintaining total balance.
                    </p>
                </div>
            </div>
            <p>India is like a vast ancient forest. If everyone wore identical clothes, ate the exact same meal, and spoke identical phrases, our society would be brittle and uniform. Our multiplicity of languages, cuisines, festival calendars, and skills creates an unbreakable, resilient national fabric!</p>
        """,
        "spoken_text": "Let us explore a profound science lesson from nature: the power of diversity! Think about a manicured garden with only one type of rose. It looks neat, but it needs constant care. If a single disease strikes, every bush dies because they are all identical. Now look at a wild natural forest! A forest contains thousands of trees, birds, insects, and creepers. It needs no watering cans or fertilizers because its diversity makes it self-healing and indestructible. India is just like that grand forest! Our diversity of customs, crafts, and ideas makes our nation resilient, vibrant, and strong.",
        "lecture_script": "Compares an artificial monoculture garden to a biodiverse forest ecosystem to explain why cultural and social diversity creates strength and adaptability for India.",
        "checkpoints": [
            {
                "question": "In ecological science, why is a diverse natural forest far more resilient to diseases and droughts than a monoculture lawn?",
                "options": [
                    "Forest trees have deeper roots that drink up all rainwater instantly",
                    "Multiple diverse species support mutual nutrient cycling, natural pest control, and ecological redundancy",
                    "Forest animals chase away storms and hail",
                    "Monoculture lawns grow faster than forest trees"
                ],
                "correct": 1,
                "explanation": "Ecological diversity ensures that if one plant species suffers an infection or drought stress, hundreds of other companion species sustain the food web and soil health, keeping the entire forest alive.",
                "study_insight": "In society, cognitive and cultural diversity provides varied perspectives to solve complex problems innovatively."
            },
            {
                "question": "How does the 'forest versus garden' comparison explain India's national strength?",
                "options": [
                    "India should cut down gardens to plant more fruit trees",
                    "Our wide variety of traditions, languages, and skills makes the nation resilient and adaptable like a forest",
                    "Everyone in India must live in the forest",
                    "Gardens are weaker because they have no fences"
                ],
                "correct": 1,
                "explanation": "Just like a forest thrives on varied plant and animal species, India's plural traditions and mutual community support make our society resilient and unshakeable.",
                "study_insight": "Ecologist Charles Elton proved in 1958 that diverse natural communities are more stable than simple, uniform communities."
            }
        ]
    },
    {
        "id": 11,
        "title": "Regional Headgear",
        "subtitle": "Saafas, Topis, Turbans & Functional Modern Safety Helmets",
        "concept_html": """
            <p>From the arid dunes of the Thar Desert to the snowy valleys of the Himalayas, traditional Indian headgear represents local climate adaptations, festive honour, and artistic identity.</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-orange-950/40 border border-orange-500/30">
                    <span class="font-bold text-orange-400 block mb-1">🏜️ Rajasthani Saafa / Pagri</span>
                    <span>Multi-metre bright cotton turban wrapped with dozens of airy folds. It shields the head from scorching desert sun and traps cool morning air inside the insulating fabric layers.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-sky-950/40 border border-sky-500/30">
                    <span class="font-bold text-sky-400 block mb-1">🏔️ Himachali & Kullu Topi</span>
                    <span>Sturdy woollen cap adorned with vibrant handwoven geometric patterned borders. Designed to insulate the scalp and ears from frigid mountain frost and icy winds.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="font-bold text-amber-400 block mb-1">👑 Mysore Peta & Maharashtrian Pheta</span>
                    <span>Aristocratic silk and zari turbans worn during weddings, formal celebrations, and state convocations as a mark of deep respect, scholarship, and festive dignity.</span>
                </div>
            </div>
            <p>Alongside traditional heritage turbans, modern India embraces <strong>functional safety headgear</strong>: tough shock-absorbing polycarbonate helmets worn by construction engineers, factory workers, and two-wheeler motorists to protect human brains from impact injuries.</p>
        """,
        "spoken_text": "Look at the colorful headgear worn across India! In the scorching deserts of Rajasthan, men wear the voluminous Saafa or Pagri—long strips of cotton wrapped in airy folds that insulate the skull from burning sunbeams. High in the cold Himalayan ranges of Himachal Pradesh, people wear warm woollen topis with intricate embroidered bands to lock in body heat. In Maharashtra and Karnataka, the regal Pheta and Mysore Peta represent royal honour and academic excellence. And on modern roads and work sites, citizens wear sturdy safety helmets to protect the fragile human skull, uniting tradition with safety science.",
        "lecture_script": "Explores traditional headgear across India: Rajasthani Saafa (thermal desert insulation), Himachali woollen Topi, Mysore Peta, and the life-saving physics of modern safety helmets.",
        "checkpoints": [
            {
                "question": "What scientific climatic function does the multi-layered cotton Saafa or Pagri serve for desert dwellers in Rajasthan?",
                "options": [
                    "It acts as a radio antenna to catch regional songs",
                    "It traps layers of air within the loose cotton folds, providing thermal insulation against scorching solar heat",
                    "It serves as a heavy weight to help walking during sandstorms",
                    "It glows in the dark to guide camels at night"
                ],
                "correct": 1,
                "explanation": "Air trapped between the multiple folds of lightweight cotton serves as a natural thermal insulator, keeping the wearer's skull cooler during hot desert days.",
                "study_insight": "In ancient times, a traveler's long turban could also be unwound to draw water from deep desert wells or act as a blanket at night."
            },
            {
                "question": "Why is wearing an ISI-certified safety helmet compulsory for two-wheeler motorists and construction workers?",
                "options": [
                    "To prevent wind from messing up hair",
                    "To cushion deceleration force and protect the skull and brain from traumatic impact injury",
                    "To match the colour of the motorcycle",
                    "To block the sound of car horns"
                ],
                "correct": 1,
                "explanation": "Safety helmets have a hard outer shell that disperses impact energy and an inner EPS foam liner that crushes gradually, slowing down the head's deceleration and preventing deadly concussions.",
                "study_insight": "Wearing a proper helmet reduces the risk of fatal head injury by more than 70% in two-wheeler accidents."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rhythm Drums",
        "subtitle": "The Acoustic Science of Dhol, Mridangam, Tabla & Pakhawaj",
        "concept_html": """
            <p>From festival processions to classical music concerts, India pulses with extraordinary rhythmic energy. Our regional percussion instruments—known as <strong>Avanaddha Vadya</strong> (membranophones)—showcase ingenious acoustic physics.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🥁 The Booming Dhol & Dholak</span>
                    <p class="text-xs text-slate-300">
                        A large barrel-shaped wooden drum with two leather heads. The wider base head produces a deep, resonant bass thump that carries across vast outdoor agricultural harvest fairs like Baisakhi and Lohri.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🎶 Mridangam, Tabla & Pakhawaj</span>
                    <p class="text-xs text-slate-300">
                        In classical Carnatic and Hindustani music, drum heads feature a central black circular patch called <strong>Syahi</strong> or <em>Karanai</em> (made of iron filings, soot, and starch). This extra mass tunes vibrating overtones into clear, harmonic musical notes!
                    </p>
                </div>
            </div>
            <p>Unlike Western drums that often produce unpitched noise, Indian percussionists engineered membranes capable of producing exact musical pitches (tones) matching the tanpura drone!</p>
        """,
        "spoken_text": "Listen to the beating heartbeat of India: our drums! From the thunderous Dhol of Punjab to the sweet rhythms of the Dholak, percussion instruments bring our festivals alive. In classical traditions, Indian musicians developed instruments like the Mridangam and Tabla. If you look at a Tabla head, you will notice a dark circular spot in the centre called the Syahi. Indian craftsmen discovered hundreds of years ago that applying a paste of iron filings and rice starch adds weight to the drum skin, dampening harsh clatter and turning the drum beat into melodious musical notes with perfect pitch!",
        "lecture_script": "Explores the acoustic physics of Indian drums: membranophone sound production, the deep bass resonance of Dhol, and the harmonic overtones created by the syahi patch on Tabla and Mridangam.",
        "checkpoints": [
            {
                "question": "What is the scientific purpose of the dark circular patch (Syahi or Karanai) applied to the leather head of a Tabla or Mridangam?",
                "options": [
                    "To hide accidental cuts or holes in the animal hide",
                    "To weight the central membrane, eliminating dissonance and producing harmonically tuned musical overtones",
                    "To make the drum waterproof against rain",
                    "To prevent the player's fingers from slipping"
                ],
                "correct": 1,
                "explanation": "Physicist Sir C.V. Raman studied the Indian drum in 1920 and proved that the concentric black Syahi loading shifts non-harmonic circular drum modes into harmonic overtones, making drums pitch-tunable like string instruments.",
                "study_insight": "Sir C. V. Raman called the Mridangam and Tabla a triumph of Indian acoustic genius."
            },
            {
                "question": "Which festival is famously associated with energetic outdoor dancing to the booming beats of the Dhol in northern India?",
                "options": [
                    "Baisakhi (Harvest celebration of Punjab)",
                    "Onam boat races",
                    "Hemis Festival in Ladakh",
                    "Rath Yatra in Puri"
                ],
                "correct": 0,
                "explanation": "Baisakhi is the joyous spring harvest festival of Punjab where farmers and communities perform the energetic Bhangra dance accompanied by the thunderous rhythm of the Dhol.",
                "study_insight": "The dhol is played using two wooden sticks: a thicker curved 'dagga' for the bass and a thin flexible 'tihli' for the treble."
            }
        ]
    },
    {
        "id": 13,
        "title": "Classical Dances",
        "subtitle": "Geometrical Postures, Storytelling Mudras & Expressive Abhinaya",
        "concept_html": """
            <p>India is home to eight celebrated <strong>Classical Dance Forms</strong> recognized across different geographic regions, each originating from temple storytelling and rooted in the ancient Sanskrit treatise <em>Natya Shastra</em>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-orange-400 block mb-0.5">💃 Bharatanatyam (Tamil Nadu)</span>
                    <span class="text-slate-300">Characterized by sculptural geometric lines, crisp stamping footwork (tattadavu), bent-knee plie postures (aramandi), and dynamic torso poise.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-sky-400 block mb-0.5">🌀 Kathak (Northern India)</span>
                    <span class="text-slate-300">Renowned for lightning-fast pirouettes (chakkars), subtle facial mime (abhinaya), and rhythmic conversation between ghungroo ankle bells and the tabla.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-emerald-400 block mb-0.5">🎭 Kathakali (Kerala)</span>
                    <span class="text-slate-300">Vivid dance-drama featuring elaborate facial face-paint (chutti), monumental headdresses, and hyper-expressive ocular (eye) ball movements.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-pink-400 block mb-0.5">🌊 Odissi (Odisha) & Manipuri (Manipur)</span>
                    <span class="text-slate-300">Odissi captures temple sculpture stances with its lyrical <em>Tribhanga</em> (three-bend posture), while Manipuri glides with graceful, floating circular movements.</span>
                </div>
            </div>
            <p>Dancers communicate complex epics without uttering a word using <strong>Hastas or Mudras</strong> (codified hand gestures representing deer, lotuses, kings, and rivers) paired with <strong>Navarasas</strong> (the nine human emotions).</p>
        """,
        "spoken_text": "Step into the magical realm of Indian classical dance! Our motherland has gifted the world eight splendid classical dance styles. In Tamil Nadu, Bharatanatyam features sharp geometric postures and lightning footwork. In the north, Kathak dazzles with spinning pirouettes and intricate rhythmic footwork matching the tabla. In Kerala, Kathakali artists paint their faces in vibrant greens and reds to enact epics through dramatic eye movements. In Odisha, Odissi dancers bend like living temple sculptures in the graceful three-part Tribhanga posture. Through graceful hand gestures called Mudras, dancers can depict a flying swan, a blossoming lotus, or gentle raindrops!",
        "lecture_script": "Introduces Indian classical dance forms: Bharatanatyam, Kathak, Kathakali, Odissi, Manipuri, the use of Mudras (hand gestures) and Navarasas (nine emotions) for storytelling.",
        "checkpoints": [
            {
                "question": "What is the three-bend body posture characteristic of classical Odissi dance called?",
                "options": [
                    "Aramandi",
                    "Tribhanga (head, torso, and hips curved in opposite directions)",
                    "Chakkar",
                    "Tattadavu"
                ],
                "correct": 1,
                "explanation": "'Tribhanga' literally translates to 'three bends'. In Odissi, the body curves gracefully at the neck, waist, and knee, mimicking the immortal stone sculptures of Konark and Puri temples.",
                "study_insight": "The opposite grounded stance in Odissi is called 'Chauka', a square posture representing Lord Jagannatha."
            },
            {
                "question": "What visual communication tool do classical Indian dancers use to depict animals, flowers, and natural elements?",
                "options": [
                    "Hand-drawn flashcards held up to the audience",
                    "Hastas or Mudras (codified symbolic hand and finger gestures)",
                    "Chalk drawings on the stage floor",
                    "Shadow puppet projections"
                ],
                "correct": 1,
                "explanation": "Mudras (or Hastas) are codified hand and finger gestures used in Indian classical dance to silently convey characters, animals (like deer and peacocks), water, and emotions.",
                "study_insight": "The Natya Shastra enumerates 28 single-hand gestures (Asamyutta Hastas) and 24 double-hand gestures (Samyutta Hastas)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Ancient Wisdom",
        "subtitle": "Ayurvedic Phytotherapy, Yoga Physiology & Daily Wellness Science",
        "concept_html": """
            <p>Thousands of years before modern synthetic pharmaceuticals and fitness gyms, ancient Indian scholars developed systematic sciences of health, mind control, and preventative wellness: <strong>Ayurveda</strong> (the science of life) and <strong>Yoga</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🌿 Botanical Phytochemistry</span>
                    <p class="text-xs text-slate-300">
                        Household herbs long prescribed in Ayurveda are now verified by modern biochemistry: <strong>Haldi (Turmeric)</strong> contains <em>curcumin</em>, a powerful anti-inflammatory and antiseptic; <strong>Tulsi (Holy Basil)</strong> contains <em>eugenol</em> for respiratory immunity; and <strong>Neem</strong> provides potent antibacterial and antifungal protection.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🧘 Yoga & Pranayama Biology</span>
                    <p class="text-xs text-slate-300">
                        Synthesised by Sage Patanjali, Yoga unites physical posture (Asana) with rhythmic breath regulation (Pranayama). Deep, slow breathing stimulates the parasympathetic nervous system, lowering heart rate, soothing anxiety, and boosting cerebral oxygen delivery.
                    </p>
                </div>
            </div>
            <p>Today, the entire world joins India on <strong>June 21st</strong> to celebrate the <strong>International Day of Yoga</strong>, recognizing our ancient heritage as a universal gift for global health and mental peace.</p>
        """,
        "spoken_text": "Long before modern hospitals and synthetic medicines were invented, India pioneered holistic systems of health and balance: Ayurveda and Yoga! Think of the home remedies your elders share: golden turmeric milk when you have a sore throat, fresh Tulsi leaves for a cough, or bitter Neem for clean skin. Modern science has now proved that turmeric contains curcumin, a powerful germ-fighting molecule! Meanwhile, the science of Yoga and Pranayama trains our breathing and postures, calming the nervous system and sharpening memory. Today, millions of people worldwide celebrate the International Day of Yoga on June 21st!",
        "lecture_script": "Explains Ayurveda and household medicinal herbs (turmeric/curcumin, tulsi, neem), the biological benefits of Yoga and Pranayama on heart rate and oxygenation, and International Yoga Day on June 21st.",
        "checkpoints": [
            {
                "question": "What bioactive compound found in golden turmeric (Haldi) gives it powerful anti-inflammatory and antiseptic properties?",
                "options": [
                    "Caffeine",
                    "Curcumin",
                    "Chlorophyll",
                    "Nicotine"
                ],
                "correct": 1,
                "explanation": "Curcumin is the active phytochemical in turmeric, proven by modern pharmacology to reduce cellular inflammation, accelerate wound healing, and fight bacterial infections.",
                "study_insight": "Turmeric combined with black pepper increases curcumin absorption in the human body by up to 2,000% due to piperine."
            },
            {
                "question": "On which date does the world celebrate the International Day of Yoga, established through India's initiative at the United Nations?",
                "options": [
                    "January 26th",
                    "June 21st (Summer Solstice)",
                    "August 15th",
                    "October 2nd"
                ],
                "correct": 1,
                "explanation": "June 21st, the longest day of the year in the Northern Hemisphere (Summer Solstice), was designated as the International Day of Yoga by the UN General Assembly in 2014.",
                "study_insight": "Yoga comes from the Sanskrit root 'Yuj', meaning to join or unite individual consciousness with universal awareness."
            }
        ]
    },
    {
        "id": 15,
        "title": "Modern Progress",
        "subtitle": "ISRO Space Exploration, Digital UPI & Vande Bharat High-Speed Rail",
        "concept_html": """
            <p>While deeply rooted in thousands of years of tradition, India simultaneously charges forward as a global leader in high-tech innovation, digital public infrastructure, and space exploration.</p>
            <div class="space-y-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/70 flex items-start space-x-2.5">
                    <span class="text-base">🚀</span>
                    <div>
                        <strong class="text-orange-400">ISRO Cosmic Triumphs:</strong>
                        <span class="text-slate-300"> India made history with the <strong>Chandrayaan-3</strong> mission by becoming the first country on Earth to land a spacecraft near the challenging South Pole of the Moon! Alongside the <em>Aditya-L1</em> solar observatory, the Indian Space Research Organisation delivers world-class space science at a fraction of global costs.</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/70 flex items-start space-x-2.5">
                    <span class="text-base">💳</span>
                    <div>
                        <strong class="text-cyan-400">UPI Digital Revolution:</strong>
                        <span class="text-slate-300"> The <strong>Unified Payments Interface (UPI)</strong> allows roadside vegetable vendors, autorickshaw drivers, and large stores to receive instant, zero-cost payments using simple QR codes on mobile phones. India now powers over 45% of all real-time digital payments across the planet!</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/70 flex items-start space-x-2.5">
                    <span class="text-base">🚅</span>
                    <div>
                        <strong class="text-emerald-400">Vande Bharat Express & Clean Energy:</strong>
                        <span class="text-slate-300"> Indigenously designed semi-high-speed electric trains connect cities with aerodynamic energy efficiency, complemented by massive solar parks and wind energy grids driving green development.</span>
                    </div>
                </div>
            </div>
            <p>Modern technology in India does not erase our ancient heritage; it empowers citizens, connects distant villages, and carries our timeless values into the future.</p>
        """,
        "spoken_text": "Behold the breathtaking modern face of India! Our nation is taking giant leaps into the future. With the historic Chandrayaan-3 mission, the Indian Space Research Organisation, ISRO, made India the first nation in history to land a rover on the Moon's mysterious South Pole! Down on our streets, the Unified Payments Interface, or UPI, has transformed our economy. Even a coconut vendor on a cart accepts instant payments with a quick smartphone QR scan, making India the world leader in digital transactions. Add to that our supersonic Vande Bharat trains and massive solar parks, and you see how India builds the future while honouring her roots!",
        "lecture_script": "Highlights India's modern achievements: ISRO's Chandrayaan-3 south pole lunar landing, Aditya-L1 solar probe, the UPI digital payment revolution, and aerodynamic Vande Bharat trains.",
        "checkpoints": [
            {
                "question": "Which historic global space milestone was achieved by the Indian Space Research Organisation (ISRO) with Chandrayaan-3 in 2023?",
                "options": [
                    "First crewed landing on Mars",
                    "First nation to achieve a soft touchdown near the lunar South Pole",
                    "First space probe to leave the solar system",
                    "First telescope built on an asteroid"
                ],
                "correct": 1,
                "explanation": "On August 23, 2023, ISRO's Vikram lander successfully touched down near the south pole of the Moon, making India the first nation in human history to land in this rugged, water-ice-rich polar region.",
                "study_insight": "August 23 is now commemorated annually in India as National Space Day."
            },
            {
                "question": "What is the primary benefit of the Unified Payments Interface (UPI) in India's daily economic life?",
                "options": [
                    "It charges high fees on all transactions",
                    "It enables instant, secure, real-time money transfers between bank accounts using simple phone QR codes",
                    "It replaces banks entirely with foreign servers",
                    "It works only in air-conditioned shopping malls"
                ],
                "correct": 1,
                "explanation": "Developed by the National Payments Corporation of India (NPCI), UPI enables real-time peer-to-peer and merchant digital transactions directly from smartphones via QR codes with zero friction.",
                "study_insight": "India processes billions of UPI transactions every month, exceeding the digital transaction volumes of many major economies combined."
            }
        ]
    },
    {
        "id": 16,
        "title": "United Fabric",
        "subtitle": "Unity in Diversity: The Irreplaceable Strength of Our Composite Culture",
        "concept_html": """
            <p>Throughout our journey across Chapter 5, we have discovered that India is not a melting pot where all unique flavours vanish into one dull soup. Instead, India is a magnificent <strong>mosaic or rich tapestry</strong>, where every thread—every dialect, every folk dance, every festival, and every modern dream—retains its own brilliant colour while weaving together into one unbreakable fabric.</p>
            <div class="p-3.5 rounded-xl bg-gradient-to-r from-orange-950/40 via-slate-900 to-emerald-950/40 border border-amber-500/30 my-3">
                <span class="text-xs font-bold text-amber-300 block mb-1">🤝 The Principles of Unity in Diversity</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Whether we celebrate Diwali, Eid, Christmas, Gurpurab, Baisakhi, Pongal, or Buddha Purnima, we share our sweets and greetings with neighbors. When our scientists launch a rocket or our athletes win Olympic medals, every Indian heart beats with the same swelling pride.
                </p>
            </div>
            <p>Our founding leaders encapsulated this spirit in the historic phrase: <strong>'Unity in Diversity'</strong>. It reminds us that our differences are not barriers that divide us; they are the dazzling treasures that make India vibrant, compassionate, and enduring.</p>
            <p>As responsible young citizens of this vibrant democracy, our duty is to celebrate each other's languages, protect our environment, uphold constitutional justice, and contribute our unique talents to national progress.</p>
        """,
        "spoken_text": "As we conclude our conceptual journey, let us celebrate the grand truth of our motherland: Unity in Diversity! India is not like a melting pot where everything gets ground into the same dull shape. India is like a magnificent handwoven saree or grand carpet! Each strand of thread—whether it is a folk song from Assam, a temple dance from Tamil Nadu, a desert turban from Rajasthan, or a space rover built in Bengaluru—keeps its unique, sparkling brilliance while binding tightly into an invincible national fabric. When we respect each other, care for our environment, and stand shoulder-to-shoulder, our vibrant India shines bright across the world!",
        "lecture_script": "Synthesizes the core philosophy of 'Unity in Diversity', composite cultural heritage, mutual respect across communities, and citizen duty toward a harmonious, progressive India.",
        "checkpoints": [
            {
                "question": "What does the famous national phrase 'Unity in Diversity' truly mean in the context of Indian culture?",
                "options": [
                    "That everyone must abandon their native language and speak only one language",
                    "That our diverse regional languages, arts, and traditions unite into a harmonious, strong national fabric without erasing individuality",
                    "That people must wear identical clothes during festivals",
                    "That state borders should be permanently sealed"
                ],
                "correct": 1,
                "explanation": "'Unity in Diversity' describes a composite society where varied cultures, languages, and belief systems harmoniously coexist, finding common purpose, mutual respect, and national integration.",
                "study_insight": "The phrase was popularized by Jawaharlal Nehru in his landmark book 'The Discovery of India'."
            },
            {
                "question": "What is the primary responsibility of young Indian citizens toward preserving this vibrant national fabric?",
                "options": [
                    "To only associate with people from their own state",
                    "To respect all cultures, protect nature, uphold constitutional values, and learn from one another",
                    "To avoid learning regional languages",
                    "To stop playing sports with students from other communities"
                ],
                "correct": 1,
                "explanation": "Active citizenship requires mutual respect across communities, protecting shared natural heritage, upholding constitutional rights and duties, and celebrating India's rich cultural diversity.",
                "study_insight": "Article 51A of the Indian Constitution enshrines the duty of every citizen to value and preserve the rich heritage of our composite culture."
            }
        ]
    }
]

print(f"Part 2 slides defined: {len(SLIDES_PART2)}")


"""
Part 3 of NCERT Class 5 Science Chapter 5: Our Vibrant Country
Mastery Challenge Quiz Questions 1 to 40 (Slides 17 to 20)
10 Questions per Challenge Slide with instant feedback, explanation, and solution_html
Zero Raw LaTeX!
"""

import sys

QUIZ_QUESTIONS = [
    # Challenge 1 (Q1 to Q10)
    {
        "id": 1,
        "question": "Which date marks the historic adoption of the Constitution of India, celebrated nationwide as Republic Day?",
        "options": ["15 August 1947", "26 January 1950", "2 October 1869", "14 November 1889"],
        "answer": 1,
        "explanation": "India adopted its Constitution on 26 January 1950, transitioning into a sovereign democratic republic.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Step-by-Step Historical Analysis:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>15 August 1947:</strong> India gained independence from British colonial rule (Independence Day).</li>
                    <li><strong>26 January 1950:</strong> The Constitution of India came into full legal force, giving the nation its supreme democratic law (Republic Day).</li>
                    <li><strong>2 October:</strong> Gandhi Jayanti (birth anniversary of Mahatma Gandhi).</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (26 January 1950)</p>
            </div>
        """
    },
    {
        "id": 2,
        "question": "What does the top saffron (Kesari) colour band of the Indian National Flag represent?",
        "options": ["Wealth and gold mines", "Courage, sacrifice, and the strength of the nation", "Abundance of agricultural crops", "Peace and silence"],
        "answer": 1,
        "explanation": "Saffron represents courage, selfless sacrifice, and the indomitable strength of the people of India.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Tricolour Band Symbolism:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong class='text-orange-400'>Saffron (Top):</strong> Courage, valor, and sacrifice.</li>
                    <li><strong class='text-slate-200'>White (Middle):</strong> Peace, truth, and purity with Dharma Chakra.</li>
                    <li><strong class='text-emerald-400'>Green (Bottom):</strong> Prosperity, fertility, and auspiciousness of the soil.</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Courage, sacrifice, and the strength of the nation)</p>
            </div>
        """
    },
    {
        "id": 3,
        "question": "How many spokes are carved into the Ashoka Chakra situated at the centre of the Indian Flag?",
        "options": ["12 spokes", "16 spokes", "24 spokes", "36 spokes"],
        "answer": 2,
        "explanation": "The Ashoka Chakra contains 24 navy blue spokes representing the 24 hours of the day and relentless righteous progress.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Ashoka Chakra Geometry & Meaning:</strong></p>
                <p class='text-slate-300'>The wheel of law is taken from the Sarnath Lion Capital of Emperor Ashoka. Its 24 spokes represent 24 righteous virtues and 24 hours of continuous purposeful motion: movement is life, stagnation is death.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: C (24 spokes)</p>
            </div>
        """
    },
    {
        "id": 4,
        "question": "Who composed India's National Anthem, 'Jana Gana Mana'?",
        "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Subhas Chandra Bose"],
        "answer": 1,
        "explanation": "Rabindranath Tagore composed 'Jana Gana Mana' in 1911, officially adopted as India's National Anthem in January 1950.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Literary & Patriotic Origin:</strong></p>
                <p class='text-slate-300'>Nobel laureate Rabindranath Tagore penned 'Jana Gana Mana' in highly Sanskritized Bengali. Bankim Chandra Chatterjee composed 'Vande Mataram' (the National Song).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Rabindranath Tagore)</p>
            </div>
        """
    },
    {
        "id": 5,
        "question": "Which of the following bodies of water is specifically glorified in the lyrics of the Indian National Anthem?",
        "options": ["Arabian Sea", "Yamuna and Ganga", "Brahmaputra and Godavari", "Chilika Lake"],
        "answer": 1,
        "explanation": "The anthem contains the verse 'Vindhya-Himachala-Yamuna-Ganga', revering the sacred rivers Yamuna and Ganga.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Geographical Sweep in the Anthem:</strong></p>
                <p class='text-slate-300'>The stanza celebrates Punjab, Sindh, Gujarat, Maratha, Dravida, Utkala, and Vanga, alongside the Vindhya and Himachal mountain ranges and the life-giving Yamuna and Ganga rivers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Yamuna and Ganga)</p>
            </div>
        """
    },
    {
        "id": 6,
        "question": "Who served as the Chairman of the Drafting Committee of the Constitution of India?",
        "options": ["Jawaharlal Nehru", "Dr. B. R. Ambedkar", "Dr. Rajendra Prasad", "Maulana Abul Kalam Azad"],
        "answer": 1,
        "explanation": "Dr. Bhimrao Ramji Ambedkar chaired the committee that drafted the supreme Constitution of India.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Constitutional Leadership:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>Dr. B. R. Ambedkar:</strong> Chairman of the Drafting Committee ('Architect of the Indian Constitution').</li>
                    <li><strong>Dr. Rajendra Prasad:</strong> President of the Constituent Assembly.</li>
                    <li><strong>Jawaharlal Nehru:</strong> Prime Minister who moved the historic Objectives Resolution.</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Dr. B. R. Ambedkar)</p>
            </div>
        """
    },
    {
        "id": 7,
        "question": "What is the primary role of a Constitution in a democratic nation like India?",
        "options": [
            "To tell shopkeepers what prices to charge for food",
            "To provide a supreme framework of rules, guarantee fundamental rights, and balance government powers",
            "To decide which sports teams win competitions",
            "To choose which movies should be shown in theatres"
        ],
        "answer": 1,
        "explanation": "A Constitution is the foundational legal document defining citizen rights, state obligations, and legal governance rules.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Purpose of the Constitution:</strong></p>
                <p class='text-slate-300'>The Constitution prevents authoritarian abuse of power, guarantees fundamental human rights (equality, freedom of speech, justice), and establishes fair checks between the Legislature, Executive, and Judiciary.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 8,
        "question": "Along which historic avenue in New Delhi is the Republic Day Parade conducted every year?",
        "options": ["Marine Drive", "Kartavya Path (formerly Rajpath)", "Mall Road", "Grand Trunk Road"],
        "answer": 1,
        "explanation": "The Republic Day parade takes place along Kartavya Path from Rashtrapati Bhavan to India Gate in New Delhi.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Ceremonial Avenue of New Delhi:</strong></p>
                <p class='text-slate-300'>Kartavya Path ('Path of Duty') serves as the ceremonial boulevard hosting the President, foreign heads of state, the Armed Forces, and cultural tableaux representing diverse states.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Kartavya Path)</p>
            </div>
        """
    },
    {
        "id": 9,
        "question": "What is the normal duration required to sing the full version of the Indian National Anthem?",
        "options": ["25 seconds", "52 seconds", "90 seconds", "120 seconds"],
        "answer": 1,
        "explanation": "The standard official timing for playing or singing the full version of Jana Gana Mana is approximately 52 seconds.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Anthem Timing Code:</strong></p>
                <p class='text-slate-300'>By national protocol, the complete 5-stanza song's first formal verse is performed with dignified cadence in exactly 52 seconds (with an abbreviated version of the first and last lines taking about 20 seconds).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (52 seconds)</p>
            </div>
        """
    },
    {
        "id": 10,
        "question": "Which of the following is a Fundamental Duty of every Indian citizen according to the Constitution?",
        "options": [
            "To watch the Republic Day parade on television",
            "To protect and improve the natural environment, including forests, lakes, rivers, and wildlife",
            "To speak at least five languages",
            "To visit New Delhi once a year"
        ],
        "answer": 1,
        "explanation": "Article 51A(g) states it is the duty of every citizen to protect and improve forests, lakes, rivers, and wildlife and have compassion for living creatures.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Constitutional Ecological Duty:</strong></p>
                <p class='text-slate-300'>Fundamental Duties remind citizens that rights come with responsibilities. Preserving natural environments and public property is essential for the nation's well-being.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },

    # Challenge 2 (Q11 to Q20)
    {
        "id": 11,
        "question": "Which national leader's portrait appears as a hidden translucent watermark on Indian currency notes?",
        "options": ["Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Subhas Chandra Bose", "Dr. B. R. Ambedkar"],
        "answer": 1,
        "explanation": "A delicate portrait of Mahatma Gandhi appears in the translucent watermark window when held to light.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Watermark Security Technology:</strong></p>
                <p class='text-slate-300'>During paper manufacturing, paper thickness is varied in specific regions. When backlit by light, varying paper density reveals a three-dimensional grayscale portrait of Mahatma Gandhi and denomination figures.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Mahatma Gandhi)</p>
            </div>
        """
    },
    {
        "id": 12,
        "question": "What is depicted inside the lenses of the round spectacles logo printed on the back of modern Indian banknotes?",
        "options": ["'Satyameva' and 'Jayate'", "'Swachh' and 'Bharat'", "'Reserve' and 'Bank'", "'Clean' and 'Green'"],
        "answer": 1,
        "explanation": "The spectacles feature the words 'Swachh' on the left lens and 'Bharat' on the right lens, commemorating the Swachh Bharat Abhiyan.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Clean India Emblem on Currency:</strong></p>
                <p class='text-slate-300'>Mahatma Gandhi's iconic wire-rimmed glasses serve as the official logo for Swachh Bharat Abhiyan, reminding every citizen exchanging currency of our shared duty toward cleanliness.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B ('Swachh' and 'Bharat')</p>
            </div>
        """
    },
    {
        "id": 13,
        "question": "Which historic architectural monument is illustrated on the reverse side of the Indian ₹10 banknote?",
        "options": ["Red Fort, Delhi", "Konark Sun Temple Stone Wheel, Odisha", "Sanchi Stupa, Madhya Pradesh", "Hampi Chariot, Karnataka"],
        "answer": 1,
        "explanation": "The ₹10 note features the famous 24-spoke stone wheel from the 13th-century Konark Sun Temple in Odisha.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Currency Monument Matcher:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>₹10:</strong> Konark Sun Temple Wheel (Odisha)</li>
                    <li><strong>₹50:</strong> Hampi Stone Chariot (Karnataka)</li>
                    <li><strong>₹100:</strong> Rani ki Vav Stepwell (Gujarat)</li>
                    <li><strong>₹500:</strong> Red Fort (New Delhi)</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Konark Sun Temple Stone Wheel, Odisha)</p>
            </div>
        """
    },
    {
        "id": 14,
        "question": "What printing technique gives the portrait of Mahatma Gandhi on banknotes a raised relief texture felt by fingertips?",
        "options": ["Lithography printing", "Intaglio printing", "Screen printing", "Dot matrix stamping"],
        "answer": 1,
        "explanation": "Intaglio printing transfers thick viscous ink under immense mechanical pressure, leaving raised tactile ridges that can be easily felt by touch.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Science of Intaglio Printing:</strong></p>
                <p class='text-slate-300'>Intaglio plates have engraved recessed grooves that hold heavy ink. When paper is pressed against the plate at thousands of pounds per square inch, ink adheres in raised ridges, providing security and tactile accessibility.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Intaglio printing)</p>
            </div>
        """
    },
    {
        "id": 15,
        "question": "How many raised diagonal bleed lines are present on the left and right margins of an Indian ₹500 banknote for accessibility?",
        "options": ["3 bleed lines", "4 bleed lines", "5 bleed lines", "7 bleed lines"],
        "answer": 2,
        "explanation": "The ₹500 banknote features 5 raised angular bleed lines on each edge along with a circular tactile identification mark.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Tactile Bleed Line Standards:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>₹100:</strong> 4 bleed lines + triangle symbol</li>
                    <li><strong>₹200:</strong> 4 bleed lines with 2 circles in between + round symbol</li>
                    <li><strong>₹500:</strong> 5 bleed lines + circle symbol</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: C (5 bleed lines)</p>
            </div>
        """
    },
    {
        "id": 16,
        "question": "What does the abbreviation MANI stand for in the assistive mobile application launched by the Reserve Bank of India?",
        "options": [
            "Money And National Income",
            "Mobile Aided Note Identifier",
            "Micro Asset Network Interface",
            "Mutual Account Net Identification"
        ],
        "answer": 1,
        "explanation": "MANI stands for Mobile Aided Note Identifier, developed to assist visually challenged individuals in recognizing banknote denominations.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>MANI App Functions:</strong></p>
                <p class='text-slate-300'>The app uses computer vision machine learning on a smartphone to detect currency notes under varied lighting conditions and speaks the denomination in Hindi or English, completely offline.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Mobile Aided Note Identifier)</p>
            </div>
        """
    },
    {
        "id": 17,
        "question": "How many regional languages are printed within the language panel on the reverse of an Indian rupee banknote?",
        "options": ["10 languages", "12 languages", "15 languages", "22 languages"],
        "answer": 2,
        "explanation": "The central language panel on the reverse side features 15 regional languages in alphabetical order.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Language Panel Breakdown:</strong></p>
                <p class='text-slate-300'>The front displays Hindi and English prominently. The reverse panel contains 15 languages: Assamese, Bengali, Gujarati, Kannada, Kashmiri, Konkani, Malayalam, Marathi, Nepali, Odia, Punjabi, Sanskrit, Tamil, Telugu, and Urdu (total 17 linguistic representations on each note).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: C (15 languages)</p>
            </div>
        """
    },
    {
        "id": 18,
        "question": "Which historic monument is depicted on the reverse side of the Indian ₹500 note?",
        "options": ["Taj Mahal, Agra", "Red Fort, New Delhi", "Gateway of India, Mumbai", "Qutub Minar, Delhi"],
        "answer": 1,
        "explanation": "The reverse of the stone-grey ₹500 banknote depicts the Red Fort in Delhi with the Indian Tricolour flag flying above its ramparts.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Red Fort Symbolism:</strong></p>
                <p class='text-slate-300'>Built by Mughal Emperor Shah Jahan in 1638, the Red Fort serves as the historic venue from where the Prime Minister addresses the nation and hoists the flag on Independence Day.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Red Fort, New Delhi)</p>
            </div>
        """
    },
    {
        "id": 19,
        "question": "How does physical banknote dimension differ across denominations from ₹10 up to ₹500?",
        "options": [
            "All notes have identical height and width",
            "Notes decrease in size as their value increases",
            "Notes progressively increase in length and width as denomination value increases",
            "Size changes randomly every year"
        ],
        "answer": 2,
        "explanation": "Higher denomination banknotes are physically wider and longer, allowing visually impaired people to sort notes by tactile size comparison.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Progressive Dimensional Sizing:</strong></p>
                <p class='text-slate-300'>A ₹10 note measures 123 mm × 63 mm, while a ₹500 note measures 150 mm × 66 mm. This systematic gradient aids rapid physical sorting.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: C</p>
            </div>
        """
    },
    {
        "id": 20,
        "question": "What is the green-to-blue colour-shifting security thread embedded vertically into higher-denomination banknotes called?",
        "options": ["Cotton ribbon", "Optically Variable Security Thread", "Plastic bookmark", "Magnetic tape"],
        "answer": 1,
        "explanation": "The windowed security thread contains colour-shifting ink that transitions from green to blue when the note is tilted in light.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Security Thread Physics:</strong></p>
                <p class='text-slate-300'>The thread carries micro-inscriptions reading 'RBI' and 'भारत'. When tilted, microscopic optical coatings interfere with light wavelengths, shifting perceived colour from green to deep blue to thwart photocopiers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Optically Variable Security Thread)</p>
            </div>
        """
    },

    # Challenge 3 (Q21 to Q30)
    {
        "id": 21,
        "question": "From which ancient archaeological sculpture was the State Emblem of India adapted?",
        "options": [
            "Iron Pillar of Delhi",
            "Sarnath Lion Capital of Emperor Ashoka",
            "Ajanta Cave Frescoes",
            "Brihadisvara Temple sculptures"
        ],
        "answer": 1,
        "explanation": "The National Emblem is an adaptation of the 3rd century BCE polished sandstone Lion Capital erected by Emperor Ashoka at Sarnath.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Historical Heritage of the Capital:</strong></p>
                <p class='text-slate-300'>Erected around 250 BCE at Sarnath, where Lord Buddha gave his first sermon (Dharmachakra Pravartana), the sculpture represents spiritual authority, peace, and universal dharma.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Sarnath Lion Capital of Emperor Ashoka)</p>
            </div>
        """
    },
    {
        "id": 22,
        "question": "How many Asiatic lions stand carved back-to-back on the Lion Capital at Sarnath?",
        "options": ["2 lions", "3 lions", "4 lions", "8 lions"],
        "answer": 2,
        "explanation": "There are four Asiatic lions standing back-to-back facing the four cardinal directions, although only three can be seen simultaneously in a 2D drawing.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Three-Dimensional Sculpture Design:</strong></p>
                <p class='text-slate-300'>The sculpture has 4 lions guarding north, south, east, and west. In official 2D paper seals, three lions are visible from any single viewing angle, while the fourth remains hidden behind.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: C (4 lions)</p>
            </div>
        """
    },
    {
        "id": 23,
        "question": "Which two animals flank the central Ashoka Chakra on the circular abacus of India's National Emblem?",
        "options": [
            "A tiger on the left and an elephant on the right",
            "A galloping horse on the left and a humped bull on the right",
            "A deer on the left and a peacock on the right",
            "A camel on the left and a rhinoceros on the right"
        ],
        "answer": 1,
        "explanation": "The circular abacus features a galloping horse on the left (representing speed and energy) and a bull on the right (representing steadfast labour).",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Animals on the Abacus:</strong></p>
                <p class='text-slate-300'>Between the wheels, the abacus depicts four animals in relief: a lion, an elephant, a galloping horse, and a humped zebu bull. In the front view, the horse and bull flank the wheel.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (A galloping horse on the left and a humped bull on the right)</p>
            </div>
        """
    },
    {
        "id": 24,
        "question": "From which sacred ancient text is the national motto 'Satyameva Jayate' taken?",
        "options": ["Bhagavad Gita", "Mundaka Upanishad", "Rigveda", "Panchatantra"],
        "answer": 1,
        "explanation": "'Satyameva Jayate' is an aphorism from the Mundaka Upanishad, proclaiming that truth alone triumphs.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Upanishadic Origin:</strong></p>
                <p class='text-slate-300'>Mundaka Upanishad (3.1.6) states: 'Satyameva Jayate Nanritam'—Truth alone triumphs, not falsehood. Through truth divine the path is widened.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Mundaka Upanishad)</p>
            </div>
        """
    },
    {
        "id": 25,
        "question": "Which state of India is the exclusive home to the world's only wild population of Asiatic lions?",
        "options": ["Rajasthan", "Gujarat (Gir Forest)", "Madhya Pradesh", "Karnataka"],
        "answer": 1,
        "explanation": "The Gir National Park and surrounding sanctuary in Gujarat is the only wild refuge for the Asiatic Lion on Earth.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Gir Conservation Triumph:</strong></p>
                <p class='text-slate-300'>Through strict protection by the Gujarat forest department and local Maldhari pastoralist communities, Asiatic lion numbers have grown from fewer than 20 in 1913 to over 674 lions today.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Gujarat - Gir Forest)</p>
            </div>
        """
    },
    {
        "id": 26,
        "question": "In which year was the Royal Bengal Tiger declared the National Animal of India under Project Tiger?",
        "options": ["1947", "1950", "1973", "2000"],
        "answer": 2,
        "explanation": "The tiger replaced the lion as India's National Animal in 1973, when Project Tiger was inaugurated at Corbett National Park.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Project Tiger Milestone:</strong></p>
                <p class='text-slate-300'>Prior to 1973, the lion was considered the national animal. Project Tiger was launched in April 1973 to save Bengal tigers from extinction caused by rampant colonial trophy hunting and habitat loss.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: C (1973)</p>
            </div>
        """
    },
    {
        "id": 27,
        "question": "Approximately what percentage of the entire world's wild tiger population lives in India today?",
        "options": ["10%", "25%", "50%", "More than 75%"],
        "answer": 3,
        "explanation": "India houses more than 75% of all wild tigers globally, with the 2023 census estimating over 3,682 wild tigers.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Global Tiger Census Data:</strong></p>
                <p class='text-slate-300'>Across 55 dedicated tiger reserves spanning over 78,000 square kilometres, India has successfully doubled its tiger count well ahead of global conservation targets.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: D (More than 75%)</p>
            </div>
        """
    },
    {
        "id": 28,
        "question": "What is the scientific name of the Indian Peafowl, the National Bird of India?",
        "options": ["Panthera tigris", "Pavo cristatus", "Nelumbo nucifera", "Ficus benghalensis"],
        "answer": 1,
        "explanation": "The scientific binomial name of the Indian Peafowl is Pavo cristatus.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Taxonomic Identification:</strong></p>
                <ul class='list-disc pl-4 space-y-1 text-slate-300'>
                    <li><strong>Pavo cristatus:</strong> Indian Peafowl (National Bird)</li>
                    <li><strong>Panthera tigris:</strong> Bengal Tiger (National Animal)</li>
                    <li><strong>Nelumbo nucifera:</strong> Indian Lotus (National Flower)</li>
                    <li><strong>Ficus benghalensis:</strong> Banyan Tree (National Tree)</li>
                </ul>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Pavo cristatus)</p>
            </div>
        """
    },
    {
        "id": 29,
        "question": "What sensory technique does the blind Ganges River Dolphin use to locate food and navigate muddy river silt?",
        "options": ["Infrared heat sensing", "Ultrasonic echolocation clicks", "Magnetic field compass", "Taste sensors on its fins"],
        "answer": 1,
        "explanation": "The Ganges River Dolphin emits high-frequency ultrasonic clicks and listens to echoes bouncing off objects, navigating flawlessly without eyesight.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Acoustic Biosonar in Murky Water:</strong></p>
                <p class='text-slate-300'>In turbid river waters of the Ganga and Brahmaputra, optical vision is useless. The dolphin uses a specialized fatty organ called a 'melon' on its head to focus sound beam clicks for echolocation.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Ultrasonic echolocation clicks)</p>
            </div>
        """
    },
    {
        "id": 30,
        "question": "What botanical structure allows a Banyan tree (Ficus benghalensis) to support enormous horizontal limbs and spread across acres?",
        "options": ["Floating water bulbs", "Thick woody aerial prop roots", "Thorny creeping tendrils", "Hollow underground bamboo shoots"],
        "answer": 1,
        "explanation": "Aerial prop roots drop from horizontal branches into the ground, thickening into secondary supporting trunks.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Prop Root Biomechanics:</strong></p>
                <p class='text-slate-300'>As branches grow heavy and extend horizontally, aerial roots descend from them. Once anchored in soil, they absorb nutrients and thicken into stout columnar pillars, supporting immense canopies.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Thick woody aerial prop roots)</p>
            </div>
        """
    },

    # Challenge 4 (Q31 to Q40)
    {
        "id": 31,
        "question": "From which ancient mother script did almost all modern Indian writing scripts (including Devanagari, Bengali, and Tamil) evolve?",
        "options": ["Cuneiform", "Brahmi script", "Phoenician", "Hieratic"],
        "answer": 1,
        "explanation": "The ancient Brahmi script, dating back over 2,300 years, is the historical ancestor of the Brahmic family of Indian scripts.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Script Lineage of India:</strong></p>
                <p class='text-slate-300'>Emperor Ashoka used Brahmi for his edicts. Over centuries, northern variants developed into Gupta script, Nagari, and Devanagari, while southern variants evolved into Grantha, Tamil, Telugu, and Kannada scripts.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Brahmi script)</p>
            </div>
        """
    },
    {
        "id": 32,
        "question": "Why is a diverse natural forest resilient to pests and droughts, whereas a single-crop garden collapses easily?",
        "options": [
            "A single-crop garden has no soil",
            "A diverse forest ecosystem features multiple complementary species that balance pests, share nutrients, and prevent single-point disease failure",
            "Forest animals carry water in buckets to trees",
            "Single-crop gardens never receive sunlight"
        ],
        "answer": 1,
        "explanation": "Ecosystem biodiversity provides redundancy and ecological stability: diverse root depths, multiple food chains, and natural predator balance protect the forest.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Biodiversity & Stability Principle:</strong></p>
                <p class='text-slate-300'>Monocultures are vulnerable because all plants share identical genetic weaknesses. A biodiverse forest interweaves different root layers, mycorrhizal networks, and natural predators that prevent pest outbreaks.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 33,
        "question": "What is the primary function of the multi-layered cotton Saafa or Pagri worn by people in Rajasthan?",
        "options": [
            "To hold keys and coins inside",
            "To insulate the head from scorching desert solar radiation by trapping dead air in cotton folds",
            "To make the wearer look taller than horses",
            "To protect the ears from cold snow"
        ],
        "answer": 1,
        "explanation": "The multiple loose folds of lightweight cotton trap dead air, which is a poor conductor of heat, shielding the skull from extreme desert temperatures.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermal Physics of Desert Turbans:</strong></p>
                <p class='text-slate-300'>Air is one of nature's best thermal insulators when trapped in small spaces. The saafa prevents direct radiant sunbeams from heating the cranial bone and evaporating body moisture.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 34,
        "question": "What acoustic feature on the membrane of an Indian Tabla or Mridangam enables it to produce harmonically tuned pitch?",
        "options": [
            "A small hole drilled in the wooden shell",
            "The Syahi (or Karanai), a black loaded circular paste of iron filings and starch in the centre",
            "Thick metal strings tied across the leather head",
            "A coat of waterproof varnish"
        ],
        "answer": 1,
        "explanation": "The central black Syahi paste adds localized mass to the membrane, suppressing discordant non-harmonic frequencies and generating pure musical harmonics.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Acoustic Tuning by Mass Loading:</strong></p>
                <p class='text-slate-300'>Simple circular drum skins vibrate in Bessel modes with non-integer overtone ratios (sounding like noise). The Syahi's parabolic mass distribution shifts overtones into harmonic ratios (1:2:3:4), creating musical notes.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 35,
        "question": "Which Indian classical dance style from Kerala is renowned for elaborate facial face-paint (chutti) and dramatic ocular (eye) storytelling?",
        "options": ["Bharatanatyam", "Kathakali", "Bhangra", "Garba"],
        "answer": 1,
        "explanation": "Kathakali is the celebrated classical dance-drama of Kerala famous for its stylized makeup, gigantic headdresses, and intricate eye movements.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Kathakali Characteristics:</strong></p>
                <p class='text-slate-300'>Green face paint (Paccha) represents noble heroes; red (Katti) represents fierce characters. Actors undergo years of rigorous eye exercises to express emotions without spoken dialogue.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Kathakali)</p>
            </div>
        """
    },
    {
        "id": 36,
        "question": "What are codified symbolic hand and finger gestures used in Indian classical dance and drama called?",
        "options": ["Asanas", "Hastas or Mudras", "Chakkars", "Ragas"],
        "answer": 1,
        "explanation": "Mudras (or Hastas) are symbolic finger and hand gestures used to depict natural objects, characters, and actions.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Sign Language of Classical Dance:</strong></p>
                <p class='text-slate-300'>From the Sanskrit root 'Mud' (delight), Mudras act as a visual vocabulary. Dancers form specific hand shapes to portray flowers, water currents, peacocks, elephants, and philosophical concepts.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Hastas or Mudras)</p>
            </div>
        """
    },
    {
        "id": 37,
        "question": "Which active chemical compound in golden turmeric (Haldi) provides scientifically proven anti-inflammatory and antiseptic effects?",
        "options": ["Quinine", "Curcumin", "Ascorbic acid", "Acetic acid"],
        "answer": 1,
        "explanation": "Curcumin is the primary bioactive polyphenol in turmeric responsible for suppressing inflammatory enzymes and accelerating tissue healing.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Curcumin Phytochemistry:</strong></p>
                <p class='text-slate-300'>Centuries of Ayurvedic use of Haridra (turmeric) are corroborated by modern clinical trials proving curcumin neutralizes free radicals and inhibits NF-kB inflammatory pathways.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Curcumin)</p>
            </div>
        """
    },
    {
        "id": 38,
        "question": "What historic achievement made ISRO's Chandrayaan-3 mission in 2023 celebrated across the entire world?",
        "options": [
            "It carried the first astronaut to Mars",
            "It achieved the world's first successful soft landing near the lunar South Pole",
            "It orbited the Sun closer than any probe",
            "It discovered a new ring around Saturn"
        ],
        "answer": 1,
        "explanation": "On August 23, 2023, India's Chandrayaan-3 became the first spacecraft to touch down on the rugged lunar south polar region.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Lunar South Pole Milestone:</strong></p>
                <p class='text-slate-300'>The lunar south pole contains permanently shadowed craters harbouring deep water-ice deposits. India's Vikram lander and Pragyan rover conducted in-situ soil measurements, confirming the presence of sulphur and oxygen.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    },
    {
        "id": 39,
        "question": "What digital payment technology developed in India allows instant, direct bank-to-bank transactions via mobile QR codes?",
        "options": ["SwiftWire", "Unified Payments Interface (UPI)", "BitToken Network", "CardSwipe Direct"],
        "answer": 1,
        "explanation": "UPI (Unified Payments Interface), launched by NPCI, powers real-time, interoperable mobile payments across millions of merchants and citizens.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Digital Public Infrastructure:</strong></p>
                <p class='text-slate-300'>UPI integrates multiple bank accounts into a single mobile application, merging seamless fund routing and merchant payments without requiring credit card machines or exposing bank account numbers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Unified Payments Interface - UPI)</p>
            </div>
        """
    },
    {
        "id": 40,
        "question": "What core message does the philosophy of 'Unity in Diversity' convey about the Indian nation?",
        "options": [
            "All people must forget their regional cultures and wear identical clothes",
            "That our diverse languages, arts, cuisines, and traditions strengthen and enrich our united national fabric rather than dividing it",
            "That only one festival should be celebrated each year",
            "That people should stop traveling between states"
        ],
        "answer": 1,
        "explanation": "'Unity in Diversity' celebrates how India's rich pluralism forms a resilient, harmonious, and indivisible national identity.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Grand Synthesis of Indian Unity:</strong></p>
                <p class='text-slate-300'>Just as different threads in a tapestry or different species in a pristine forest create an unbreakable, beautiful whole, India's multiplicity of traditions, combined with constitutional brotherhood, forms the proud backbone of our vibrant nation.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B</p>
            </div>
        """
    }
]

print(f"Mastery quiz questions defined: {len(QUIZ_QUESTIONS)}")


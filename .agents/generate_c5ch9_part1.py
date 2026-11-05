"""
Part 1 of NCERT Class 5 Science Chapter 9: Rhythms of Nature
Slides 1 to 8: Core Theory, Audio Lecture Scripts (Zero Mentor/Lecturer Names),
Formative Checkpoints (2 per slide = 16 Checkpoints).
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

SLIDES_PART1 = [
    # Slide 1: Nature's Clock
    {
        "id": 1,
        "title": "Nature's Clock",
        "subtitle": "Observing Change Across Seconds, Days, and Years",
        "concept_html": """
            <p>Look around and notice how everything in our world is constantly changing. Some changes happen in the blink of an eye, like a heartbeat or a flash of lightning. Other changes take hours, such as a blooming jasmine bud or the sun moving across the sky from morning to evening.</p>
            <p>When friends meet after a long summer break, they notice they have grown taller, their hair is longer, and the garden trees are filled with new fruits. Changes unfold across different time scales: <strong>seconds</strong> for rapid motion, <strong>hours and days</strong> for day and night, and <strong>months and years</strong> for growth and seasons. Nature is never completely frozen; it moves in continuous, magnificent rhythms.</p>
        """,
        "spoken_text": "Look closely at the world around you. Change is happening every single moment. Some changes take just a few seconds, like catching a falling leaf or blinking your eyes. Other changes happen over hours, like the shadow of a flagpole moving across the school ground. And some changes take months or years, such as a tiny mango sapling growing into a shady, fruit-bearing tree. Nature has its own clock, and learning to observe these different paces of change helps us understand the great rhythms that shape our planet.",
        "lecture_script": "Look closely at the world around you. Change is happening every single moment. Some changes take just a few seconds, like catching a falling leaf or blinking your eyes. Other changes happen over hours, like the shadow of a flagpole moving across the school ground. And some changes take months or years, such as a tiny mango sapling growing into a shady, fruit-bearing tree. Nature has its own clock, and learning to observe these different paces of change helps us understand the great rhythms that shape our planet.",
        "checkpoints": [
            {
                "question": "Which of these events represents a change that takes place over months or years rather than seconds?",
                "options": [
                    "A child growing out of their school shoes and a mango seed growing into a tree",
                    "A firefly flashing its light in the night",
                    "A rubber ball bouncing off the classroom wall",
                    "Snapping your fingers during music class"
                ],
                "correct": 0,
                "explanation": "Biological growth in living organisms, such as human bone development and tree maturation, occurs gradually over months and years.",
                "study_insight": "Physical changes like collisions take milliseconds, while biological maturation requires years of cell division."
            },
            {
                "question": "Why does nature feel both changing and predictable at the same time?",
                "options": [
                    "Because all changes occur in complete chaos without any pattern",
                    "Because many changes repeat in regular, cyclic patterns such as day and night and yearly seasons",
                    "Because the Earth completely stops spinning once every week",
                    "Because trees never shed their leaves"
                ],
                "correct": 1,
                "explanation": "Although changes happen continuously, astronomical motions cause them to repeat in reliable, predictable cycles called rhythms.",
                "study_insight": "The word rhythm refers to regular, repeating cycles of change observed across astronomical and ecological systems."
            }
        ]
    },

    # Slide 2: Day and Night
    {
        "id": 2,
        "title": "Day and Night",
        "subtitle": "The 24-Hour Cycle of Solar Light and Shadow",
        "concept_html": """
            <p>Every morning, warm golden sunlight bathes our homes, waking birds and opening flowers. By evening, shadows stretch long and thin, the sky turns crimson and indigo, and night descends with glittering stars. How does this daily transformation occur?</p>
            <p>In a classroom demonstration using a stationary torch and a globe, we discover a remarkable truth: <strong>the Sun does not travel around the Earth</strong>. Instead, the Earth spins continuously like a giant top. The half of the Earth facing toward the stationary Sun receives direct light and experiences <strong>day</strong>, while the opposite half turned away is in shadow and experiences <strong>night</strong>.</p>
        """,
        "spoken_text": "Every morning begins with bright sunshine, and every evening ends in starry darkness. It might feel like the Sun travels across the sky, but our senses are tricking us. In reality, the Sun remains stationary at the center of our solar system. It is our planet Earth that is spinning smoothly on its axis, like a top. When our town rotates to face the Sun, we enjoy daytime. As our part of the globe turns away into shadow, night arrives, allowing the Earth to cool and living creatures to rest.",
        "lecture_script": "Every morning begins with bright sunshine, and every evening ends in starry darkness. It might feel like the Sun travels across the sky, but our senses are tricking us. In reality, the Sun remains stationary at the center of our solar system. It is our planet Earth that is spinning smoothly on its axis, like a top. When our town rotates to face the Sun, we enjoy daytime. As our part of the globe turns away into shadow, night arrives, allowing the Earth to cool and living creatures to rest.",
        "checkpoints": [
            {
                "question": "In the classroom torch and globe experiment, what does the torch represent?",
                "options": [
                    "The stationary Sun radiating light toward the spinning Earth",
                    "A moving full moon orbiting a classroom desk",
                    "A flashing lighthouse on the seashore",
                    "A distant shooting star passing by"
                ],
                "correct": 0,
                "explanation": "The torch acts as a fixed source of parallel light rays simulating the stationary Sun, illuminating only one hemisphere of the globe at a time.",
                "study_insight": "Light travels in straight lines; a spherical planet blocks light, casting a shadow on its opposite half."
            },
            {
                "question": "If India is directly facing the Sun and experiencing bright midday, what is the opposite side of the Earth (like America) experiencing?",
                "options": [
                    "Nighttime, because that hemisphere is turned away from the Sun in Earth's shadow",
                    "Midday lunch break with bright sunlight",
                    "A solar eclipse lasting 24 hours",
                    "Total absence of gravity"
                ],
                "correct": 0,
                "explanation": "Because Earth is a solid sphere, only 50% can face the Sun at any instant; the opposite hemisphere is in darkness.",
                "study_insight": "This geometric illumination division line between day and night is called the circle of illumination."
            }
        ]
    },

    # Slide 3: Earth's Spin
    {
        "id": 3,
        "title": "Earth's Spin",
        "subtitle": "Axial Rotation and the 24-Hour Day",
        "concept_html": """
            <p>The imaginary line running through the center of the Earth from the North Pole to the South Pole is called the <strong>axis of rotation</strong>. The Earth completes one full rotation on this axis once every <strong>24 hours</strong>, which defines the length of one complete day on Earth.</p>
            <p>Earth rotates from <strong>west to east</strong> (counter-clockwise when viewed from above the North Pole). Because our planet spins eastward beneath our feet, celestial bodies like the Sun, Moon, and stars appear to rise in the eastern horizon and set in the western horizon, creating the daily cycle of sunrise, solar noon, sunset, and midnight.</p>
        """,
        "spoken_text": "Earth spins on an imaginary tilted line called its axis, connecting the North and South Poles. It takes exactly twenty-four hours to complete one full rotation. Because the Earth spins from west to east, everything in the sky appears to move in the opposite direction. That is why the Sun always rises in the east, climbs high above us at midday, and sets peacefully in the west. This steady eastward spin is our planet's primary heartbeat, giving us the twenty-four hour day.",
        "lecture_script": "Earth spins on an imaginary tilted line called its axis, connecting the North and South Poles. It takes exactly twenty-four hours to complete one full rotation. Because the Earth spins from west to east, everything in the sky appears to move in the opposite direction. That is why the Sun always rises in the east, climbs high above us at midday, and sets peacefully in the west. This steady eastward spin is our planet's primary heartbeat, giving us the twenty-four hour day.",
        "checkpoints": [
            {
                "question": "In which direction does the Earth spin on its axis, causing the Sun to appear to rise in the east?",
                "options": [
                    "From west to east",
                    "From north to south",
                    "From east to west",
                    "From top to bottom"
                ],
                "correct": 0,
                "explanation": "Earth's eastward rotation causes stationary celestial objects to appear to move westward across the horizon.",
                "study_insight": "This apparent motion is just like looking out a train window: moving forward makes trees seem to rush backward."
            },
            {
                "question": "How long does the Earth take to complete one full rotation on its axis?",
                "options": [
                    "24 hours (1 solar day)",
                    "365 days (1 year)",
                    "12 hours (half a day)",
                    "60 minutes (1 hour)"
                ],
                "correct": 0,
                "explanation": "One complete 360-degree rotation of Earth on its axis takes approximately 24 hours.",
                "study_insight": "Rotation refers to spinning on an internal axis, while revolution refers to orbiting around the Sun."
            }
        ]
    },

    # Slide 4: Seasons' Journal
    {
        "id": 4,
        "title": "Seasons' Journal",
        "subtitle": "Tracking Annual Environmental Changes Across Four Quarters",
        "concept_html": """
            <p>While day and night repeat every 24 hours, another grand rhythm unfolds slowly across an entire year: <strong>the seasons</strong>. To understand these slow changes, students maintain a personal Seasons' Journal and compile their observations into a large wall chart.</p>
            <p>The classroom chart divides the year into four broad three-month quarters:
                <ul class='list-disc pl-5 space-y-1 text-slate-300'>
                    <li><strong>April to June:</strong> Blazing sunshine, heatwaves, summer holidays, and harvest of ripe mangoes.</li>
                    <li><strong>July to September:</strong> Heavy monsoon downpours, swelling rivers, lush green fields, and paper boats.</li>
                    <li><strong>October to December:</strong> Clear blue skies, pleasant autumn breeze, festive lights, and morning mist.</li>
                    <li><strong>January to March:</strong> Crisp winter chill, blooming mustard fields, warming sun, and vibrant spring flowers.</li>
                </ul>
            </p>
        """,
        "spoken_text": "While day and night happen in hours, the seasons unfold across months. By keeping a Seasons Journal, students become nature detectives. They record observations across the four quarters of the year: the blazing heat and juicy mangoes of April to June, the thundering monsoon clouds and flooded streams of July to September, the pleasant autumn breezes and festive lights of October to December, and the crisp winter chill and blooming mustard flowers of January to March.",
        "lecture_script": "While day and night happen in hours, the seasons unfold across months. By keeping a Seasons Journal, students become nature detectives. They record observations across the four quarters of the year: the blazing heat and juicy mangoes of April to June, the thundering monsoon clouds and flooded streams of July to September, the pleasant autumn breezes and festive lights of October to December, and the crisp winter chill and blooming mustard flowers of January to March.",
        "checkpoints": [
            {
                "question": "What is the primary scientific purpose of maintaining a classroom Seasons' Journal?",
                "options": [
                    "To systematically record and identify repeating annual patterns in weather, plant life, and animal behavior",
                    "To memorize the names of foreign planets",
                    "To draw pictures of cartoon characters",
                    "To count how many times students sharpen their pencils"
                ],
                "correct": 0,
                "explanation": "A journal enables students to record longitudinal environmental data and uncover predictable seasonal cycles over months.",
                "study_insight": "Scientific observation over time transforms separate daily weather events into an understanding of annual climate cycles."
            },
            {
                "question": "Which quarterly period in India is typically characterized by swelling rivers, heavy rainfall, and lush green countryside?",
                "options": [
                    "July to September (Monsoon quarter)",
                    "April to June (Peak summer heat)",
                    "January to March (Late winter and early spring)",
                    "November to December (Dry pre-winter)"
                ],
                "correct": 0,
                "explanation": "The southwest monsoon brings the majority of India's annual precipitation between July and September.",
                "study_insight": "Over 75% of India's total rainfall occurs during the four monsoon months of June to September."
            }
        ]
    },

    # Slide 5: Yearly Rhythms
    {
        "id": 5,
        "title": "Yearly Rhythms",
        "subtitle": "Analyzing Patterns Across Five Core Ecological Themes",
        "concept_html": """
            <p>By analyzing the classroom seasons chart, students investigate how nature transforms across <strong>five fundamental ecological themes</strong>:
                <ul class='list-disc pl-5 space-y-1 text-slate-300'>
                    <li><strong>Plant Life:</strong> Trees shed leaves to conserve water, sprout fresh tender red-green foliage, burst into fragrant blooms, and bear ripe fruit.</li>
                    <li><strong>Birds and Animals:</strong> Migratory birds fly thousands of kilometres to escape freezing Arctic winters; frogs croak in monsoon ponds; insects emerge and lay eggs.</li>
                    <li><strong>Air and Wind:</strong> From hot, dusty summer winds (<em>Loo</em>) to moisture-laden monsoon gales and crisp, dry winter chills.</li>
                    <li><strong>Heat and Light:</strong> Scorching overhead summer sunshine with long days vs gentle low-angle winter sunlight with short days.</li>
                    <li><strong>Water Bodies & Human Habits:</strong> Evaporating ponds and mud cracks vs overflowing reservoirs; woollens and hot soup vs cotton kurtas and chilled aam panna.</li>
                </ul>
            </p>
        """,
        "spoken_text": "When we analyze our seasonal chart, we discover five deeply connected themes. First, plant life changes: trees bud, bloom, bear fruit, and shed leaves. Second, animals respond: migratory Siberian cranes arrive at Indian wetlands, while earthworms and frogs celebrate the monsoon. Third, the air shifts from the scorching summer Loo to cool winter breezes. Fourth, the Sun climbs high in summer giving long days, but stays lower in winter. And fifth, human lives adjust: we switch our clothes, our favourite meals, and our daily chores to match nature's rhythm.",
        "lecture_script": "When we analyze our seasonal chart, we discover five deeply connected themes. First, plant life changes: trees bud, bloom, bear fruit, and shed leaves. Second, animals respond: migratory Siberian cranes arrive at Indian wetlands, while earthworms and frogs celebrate the monsoon. Third, the air shifts from the scorching summer Loo to cool winter breezes. Fourth, the Sun climbs high in summer giving long days, but stays lower in winter. And fifth, human lives adjust: we switch our clothes, our favourite meals, and our daily chores to match nature's rhythm.",
        "checkpoints": [
            {
                "question": "Why do deciduous trees in many parts of India shed their leaves before the peak of summer or winter?",
                "options": [
                    "To minimize water loss through leaf transpiration during dry seasons",
                    "Because they are permanently dead and will never grow again",
                    "To hide from passing herbivores",
                    "Because the wind blows them away by force"
                ],
                "correct": 0,
                "explanation": "Shedding leaves reduces surface area, stopping stomatal water transpiration and helping the tree survive dry, rainless spells.",
                "study_insight": "Transpiration is the evaporation of water from plant leaves; shedding leaves is an evolutionary survival adaptation."
            },
            {
                "question": "Which of these is an example of an animal behavior adapting to annual seasonal rhythms?",
                "options": [
                    "Migratory birds flying to warm Indian wetlands in winter to find food and nest",
                    "Goldfish swimming in a plastic glass tank indoors",
                    "A street dog barking at a passing scooter",
                    "A cat drinking milk from a saucer"
                ],
                "correct": 0,
                "explanation": "Seasonal migration is an instinctive annual rhythm where birds travel thousands of miles to avoid freezing temperatures and starvation.",
                "study_insight": "Wetlands like Keoladeo National Park in Bharatpur host over 350 migratory bird species every winter."
            }
        ]
    },

    # Slide 6: Vasanta Spring
    {
        "id": 6,
        "title": "Vasanta Spring",
        "subtitle": "The King of Seasons: Blossom, Fragrance, and Rebirth",
        "concept_html": """
            <p>In traditional Indian astronomy and literature, the annual cycle is divided into <strong>six distinct seasons (Shad Ritu)</strong>, each lasting approximately two lunar months. The cycle begins with <strong>Vasanta (Spring)</strong>, celebrated as <em>Rituraj</em>—the King of Seasons.</p>
            <p>Falling during the Hindu calendar months of <strong>Chaitra and Vaishakha</strong> (mid-March to mid-May), Vasanta brings pleasant temperatures where the air is neither too hot nor too cold. Trees like the Palash (Flame of the Forest), Gulmohar, and Mango burst into brilliant orange blooms and fragrant blossoms (<em>Manjari</em>). The melodious song of the Asian Koel echoes through the groves, signaling nature's awakening.</p>
        """,
        "spoken_text": "In the traditional Indian calendar, the year is divided into six distinct seasons called the Shad Ritu. The cycle begins with Vasanta, known as the King of Seasons. Arriving in March and April, Vasanta brings delightful weather: the biting cold has faded, and the blazing summer heat has not yet begun. Red and orange flowers blanket the Palash and Semal trees, mango orchards fill with sweet-smelling blossoms, and the melodious call of the Koel bird rings across every town and village.",
        "lecture_script": "In the traditional Indian calendar, the year is divided into six distinct seasons called the Shad Ritu. The cycle begins with Vasanta, known as the King of Seasons. Arriving in March and April, Vasanta brings delightful weather: the biting cold has faded, and the blazing summer heat has not yet begun. Red and orange flowers blanket the Palash and Semal trees, mango orchards fill with sweet-smelling blossoms, and the melodious call of the Koel bird rings across every town and village.",
        "checkpoints": [
            {
                "question": "Which traditional Indian season is revered as 'Rituraj' (King of Seasons) for its pleasant weather and bursting blossoms?",
                "options": [
                    "Vasanta (Spring)",
                    "Shishir (Winter)",
                    "Grishma (Summer)",
                    "Varsha (Monsoon)"
                ],
                "correct": 0,
                "explanation": "Vasanta is crowned Rituraj because of its moderate, refreshing temperature, blooming flowers, and vibrant rebirth of foliage.",
                "study_insight": "In the Sanskrit calendar, Vasanta spans the lunar months of Chaitra and Vaishakha, marking the start of the new agricultural year."
            },
            {
                "question": "What famous bird call is traditionally associated with the arrival of blooming mango groves in Vasanta?",
                "options": [
                    "The Asian Koel (Cuckoo)",
                    "The barn owl",
                    "The white seagull",
                    "The grey vulture"
                ],
                "correct": 0,
                "explanation": "The male Asian Koel's melodious 'ku-oo' call rings out during spring when mango trees are in full blossom.",
                "study_insight": "Koels feed on ripe spring berries and wild figs, and their breeding season coincides with the onset of warm spring weather."
            }
        ]
    },

    # Slide 7: Grishma Summer
    {
        "id": 7,
        "title": "Grishma Summer",
        "subtitle": "Blazing Sun, Heatwaves, and Tropical Fruits",
        "concept_html": """
            <p>Following spring comes <strong>Grishma (Summer)</strong>, spanning the months of <strong>Jyeshtha and Ashadha</strong> (mid-May to mid-July). During this season, the northern hemisphere tilts closest to the Sun, causing direct, intense solar radiation and long daylight hours.</p>
            <p>Dry, scorching winds called <strong>Loo</strong> sweep across northern and central plains, and water levels in village ponds, wells, and rivers drop sharply. However, Grishma is also nature's sweetest season! It brings the bounty of tropical fruits: kingly mangoes, hydrating watermelons, muskmelons, and juicy litchis. Families drink traditional cooling beverages like <em>Aam Panna</em>, <em>Sattu</em>, buttermilk, and kokum sharbat to maintain hydration.</p>
        """,
        "spoken_text": "Next arrives Grishma, our peak summer season, spanning May, June, and early July. The Sun climbs directly overhead, delivering intense heat and stretching daylight hours to their longest. In northern India, strong, hot winds called the Loo blow across the land. Ponds dry down to cracked mud. Yet Grishma brings extraordinary natural treats: sweet mangoes ripen to golden perfection, and markets overflow with cooling watermelons, litchis, and cucumbers. We stay indoors during the afternoon, wearing breathable cotton clothes and drinking tangy aam panna.",
        "lecture_script": "Next arrives Grishma, our peak summer season, spanning May, June, and early July. The Sun climbs directly overhead, delivering intense heat and stretching daylight hours to their longest. In northern India, strong, hot winds called the Loo blow across the land. Ponds dry down to cracked mud. Yet Grishma brings extraordinary natural treats: sweet mangoes ripen to golden perfection, and markets overflow with cooling watermelons, litchis, and cucumbers. We stay indoors during the afternoon, wearing breathable cotton clothes and drinking tangy aam panna.",
        "checkpoints": [
            {
                "question": "What are the hot, dry, dust-laden summer winds blowing across northern India during Grishma called?",
                "options": [
                    "The Loo",
                    "The Trade Winds",
                    "The Polar Easterlies",
                    "The Blizzard"
                ],
                "correct": 0,
                "explanation": "The Loo is a strong, gusty, hot and dry summer wind from the Thar desert that causes rapid dehydration and heatstroke if precautions are not taken.",
                "study_insight": "Staying hydrated with natural salt and electrolytes prevents heatstroke during intense Loo conditions."
            },
            {
                "question": "Why do seasonal fruits like watermelons, cucumbers, and muskmelons naturally ripen during the peak heat of Grishma?",
                "options": [
                    "They possess exceptionally high water content (over 90%), offering natural hydration to animals and humans in extreme heat",
                    "They can only grow under thick layers of snow",
                    "They absorb all sunlight and turn into ice",
                    "They need freezing frost to develop sweetness"
                ],
                "correct": 0,
                "explanation": "Nature's foods match bodily needs: summer melons contain over 92% water and essential minerals, naturally replenishing body moisture lost through sweat.",
                "study_insight": "Consuming seasonal foods aligns human nutrition with the environmental demands of each climate phase."
            }
        ]
    },

    # Slide 8: Varsha Monsoon
    {
        "id": 8,
        "title": "Varsha Monsoon",
        "subtitle": "The Life-Giving Rains: Clouds, Frogs, and Rebirth",
        "concept_html": """
            <p>When the intense summer heat creates low air pressure over the subcontinent, moist winds from the Indian Ocean rush in, heralding <strong>Varsha (Monsoon)</strong>. Spanning the months of <strong>Shravana and Bhadrapada</strong> (mid-July to mid-September), Varsha transforms the entire landscape.</p>
            <p>Dry brown soils turn into vibrant emerald-green carpets overnight. Dried riverbeds swell with foaming waters, and dry wells replenish their aquifers. Earthworms surface to aerate the soaked soil, peacocks spread their dazzling iridescent trains in monsoon dances, and choruses of bullfrogs celebrate in puddles. For Indian farmers, Varsha is the lifeline that waters the staple <strong>Kharif crops</strong> like rice paddy, maize, and millets.</p>
        """,
        "spoken_text": "After the blistering heat of summer, dense dark clouds gather in the sky, bringing Varsha, the glorious Indian monsoon. Falling during July, August, and September, rain showers awaken the parched earth with the unforgettable, sweet smell of wet soil called petrichor. Ponds and rivers fill to their brim, baby ferns sprout from brick walls, and peacocks dance with joyful outspread feathers. For millions of farming families across India, the monsoon rain brings life and prosperity, nourishing the green paddy fields that feed our nation.",
        "lecture_script": "After the blistering heat of summer, dense dark clouds gather in the sky, bringing Varsha, the glorious Indian monsoon. Falling during July, August, and September, rain showers awaken the parched earth with the unforgettable, sweet smell of wet soil called petrichor. Ponds and rivers fill to their brim, baby ferns sprout from brick walls, and peacocks dance with joyful outspread feathers. For millions of farming families across India, the monsoon rain brings life and prosperity, nourishing the green paddy fields that feed our nation.",
        "checkpoints": [
            {
                "question": "What is the pleasant, earthy aroma produced when the first monsoon raindrops hit dry soil called?",
                "options": [
                    "Petrichor",
                    "Chlorophyll",
                    "Nectar",
                    "Ammonia"
                ],
                "correct": 0,
                "explanation": "Petrichor is the scent released when rain moistens dry soil, caused by plant oils and an organic bacterial compound called geosmin.",
                "study_insight": "The word petrichor originates from Greek: 'petra' (stone) and 'ichor' (the mythical blood of the gods)."
            },
            {
                "question": "Why is the Varsha monsoon season considered the vital lifeline of Indian agriculture?",
                "options": [
                    "Because it provides natural irrigation for major food crops like rice paddy, pulses, and millets across rainfed farmlands",
                    "Because it turns all crops into solid stone",
                    "Because farmers stop growing food and go on holiday",
                    "Because it freezes all water into ice"
                ],
                "correct": 0,
                "explanation": "Over 50% of India's cultivated farmland depends directly on monsoon rainfall to grow Kharif staple grains.",
                "study_insight": "A normal monsoon ensures abundant food harvest, full water reservoirs, and stable food prices throughout the year."
            }
        ]
    }
]

print("Part 1 slides defined:", len(SLIDES_PART1))


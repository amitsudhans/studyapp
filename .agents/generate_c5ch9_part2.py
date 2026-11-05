"""
Part 2 of NCERT Class 5 Science Chapter 9: Rhythms of Nature
Slides 9 to 16: Core Theory, Audio Lecture Scripts (Zero Mentor/Lecturer Names),
Formative Checkpoints (2 per slide = 16 Checkpoints).
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

SLIDES_PART2 = [
    # Slide 9: Sharad Autumn
    {
        "id": 9,
        "title": "Sharad Autumn",
        "subtitle": "Clear Blue Skies, White Kash Grass, and Cool Nights",
        "concept_html": """
            <p>As the dense rain clouds drift away, the sky clears into a brilliant, deep sapphire blue, welcoming <strong>Sharad (Autumn)</strong>. Occurring during the lunar months of <strong>Ashvina and Kartika</strong> (mid-September to mid-November), this season represents a period of tranquil balance.</p>
            <p>Rivers run clear and tranquil, silver-white <em>Kash</em> reed flowers (Saccharum spontaneum) sway along riverbanks like gentle feather plumes, and fragrant nocturnal <em>Shiuli</em> (Parijat) blossoms carpet the morning grass. The daytime sunshine is bright and crisp, while the nights grow noticeably cooler, marked by the luminous autumn full moon known as <em>Sharad Purnima</em>.</p>
        """,
        "spoken_text": "When the monsoon rains finally retreat, the atmosphere clears into the crystal-blue skies of Sharad, our autumn season. Spanning late September, October, and early November, Sharad is known for its serene beauty. Riverbanks turn into waving seas of silvery-white Kash grass flowers, and sweet-scented white Shiuli blossoms fall upon the dewy grass at dawn. The days are comfortably warm, while nights turn pleasantly cool, signaling the arrival of major festive celebrations across the land.",
        "lecture_script": "When the monsoon rains finally retreat, the atmosphere clears into the crystal-blue skies of Sharad, our autumn season. Spanning late September, October, and early November, Sharad is known for its serene beauty. Riverbanks turn into waving seas of silvery-white Kash grass flowers, and sweet-scented white Shiuli blossoms fall upon the dewy grass at dawn. The days are comfortably warm, while nights turn pleasantly cool, signaling the arrival of major festive celebrations across the land.",
        "checkpoints": [
            {
                "question": "Which silvery-white feathery grass famously blooms along Indian riverbanks to herald the arrival of Sharad (Autumn)?",
                "options": [
                    "Kash grass (Kaash phool)",
                    "Cactus spines",
                    "Pine needles",
                    "Mangrove breathing roots"
                ],
                "correct": 0,
                "explanation": "Kash grass blossoms with fluffy, silver-white feathery plumes right at the end of the monsoon, iconic in eastern and northern India.",
                "study_insight": "In Bengal and eastern states, the blooming of Kash flowers traditionally announces the homecoming of festival season."
            },
            {
                "question": "What happens to the appearance of the sky and river waters during Sharad compared to the monsoon?",
                "options": [
                    "Skies turn deep, clear blue and rivers settle into clear, transparent streams",
                    "Skies turn completely black and rivers turn into solid ice",
                    "Rivers dry up to desert dust instantly",
                    "The Sun disappears for two months"
                ],
                "correct": 0,
                "explanation": "With the cessation of rain and soil runoff, airborne dust settles, giving clear skies and sparkling, sediment-free river water.",
                "study_insight": "Turbidity (cloudiness) of water drops sharply in autumn as suspended silt settles on the riverbed."
            }
        ]
    },

    # Slide 10: Hemant Pre-Winter
    {
        "id": 10,
        "title": "Hemant Pre-Winter",
        "subtitle": "Golden Harvest Fields, Dewdrops, and Early Chills",
        "concept_html": """
            <p>Following autumn comes <strong>Hemant (Pre-Winter)</strong>, spanning the months of <strong>Margashirsha and Pausha</strong> (mid-November to mid-January). Hemant marks the transition into cooler weather, with morning fog rolling over fields and glistening dewdrops clinging to spiderwebs and grass blades.</p>
            <p>The vast countryside glows in warm golden hues as the lush summer paddy ripens into golden grain ready for harvest. The air carries an invigorating, crisp nip, and families begin bringing out light woollen cardigans and quilts. The aroma of freshly harvested rice, new jaggery (<em>Gur</em>), and roasted sesame seeds fills kitchen courtyards as communities celebrate successful harvests.</p>
        """,
        "spoken_text": "Next comes Hemant, our pre-winter season, spanning November and December. During Hemant, early mornings are wrapped in soft, mysterious mist, and cold dewdrops sparkle like tiny diamonds on the grass. The countryside turns into a sea of glittering gold as the ripe rice crops are gathered from the fields. The air carries a crisp, refreshing nip, prompting us to reach for light sweaters and quilts. Kitchens fill with the delicious warmth of new sugarcane jaggery, roasted peanuts, and fragrant freshly harvested rice.",
        "lecture_script": "Next comes Hemant, our pre-winter season, spanning November and December. During Hemant, early mornings are wrapped in soft, mysterious mist, and cold dewdrops sparkle like tiny diamonds on the grass. The countryside turns into a sea of glittering gold as the ripe rice crops are gathered from the fields. The air carries a crisp, refreshing nip, prompting us to reach for light sweaters and quilts. Kitchens fill with the delicious warmth of new sugarcane jaggery, roasted peanuts, and fragrant freshly harvested rice.",
        "checkpoints": [
            {
                "question": "What atmospheric phenomenon creates tiny liquid droplets on grass blades and leaves on cool Hemant mornings?",
                "options": [
                    "Condensation of water vapor from the humid air contacting chilled nighttime ground surfaces (Dew)",
                    "Underground water fountains spraying upward",
                    "Melted plastic falling from the sky",
                    "Chemical smoke from airplanes"
                ],
                "correct": 0,
                "explanation": "At night, the ground radiates heat into space and cools; ambient water vapor in contact with the cold grass condenses into liquid dewdrops.",
                "study_insight": "The temperature at which airborne water vapor begins condensing into liquid dew is known as the dew point."
            },
            {
                "question": "Which major staple crop turns golden and is harvested across Indian villages during Hemant?",
                "options": [
                    "Paddy (Rice)",
                    "Watermelon",
                    "Mangoes",
                    "Litchis"
                ],
                "correct": 0,
                "explanation": "Rice paddy sown during the monsoon reaches full maturity and turns golden-yellow, marking the main autumn-winter harvest.",
                "study_insight": "India is the world's second-largest producer of rice, harvesting over 130 million tonnes annually."
            }
        ]
    },

    # Slide 11: Shishir Winter
    {
        "id": 11,
        "title": "Shishir Winter",
        "subtitle": "Frosty Winds, Woollen Shawls, and Vitamin Bounty",
        "concept_html": """
            <p>The sixth and coldest season of the Indian cycle is <strong>Shishir (Winter)</strong>, occupying the months of <strong>Magha and Phalguna</strong> (mid-January to mid-March). In northern India, cold continental winds sweep down from the snow-clad Himalayas, dropping temperatures sharply.</p>
            <p>Dense morning fogs often blanket the plains, and daylight hours are noticeably shorter. Deciduous trees shed the last of their dry leaves in anticipation of spring rebirth. To stay healthy in the dry chill, people wear thick woollens, sit in the warm afternoon sunshine, and enjoy nature's winter bounty: rich green leafy vegetables like spinach, fenugreek, and mustard leaves (<em>Sarson ka Saag</em>), accompanied by vitamin-C rich citrus oranges and immunity-boosting Amla.</p>
        """,
        "spoken_text": "The cycle reaches its coldest point with Shishir, our peak winter season, spanning January, February, and early March. Chilly winds sweep across northern India, blanketing towns in thick morning fog and frost. People wear warm woollen caps, mufflers, and jackets, gathering around bonfires or enjoying the comforting afternoon sun. Nature provides exactly what our bodies need to fight seasonal colds: dark green leafy vegetables like sarson and palak, sweet juicy oranges, and nutrient-dense amla packed with natural vitamin C.",
        "lecture_script": "The cycle reaches its coldest point with Shishir, our peak winter season, spanning January, February, and early March. Chilly winds sweep across northern India, blanketing towns in thick morning fog and frost. People wear warm woollen caps, mufflers, and jackets, gathering around bonfires or enjoying the comforting afternoon sun. Nature provides exactly what our bodies need to fight seasonal colds: dark green leafy vegetables like sarson and palak, sweet juicy oranges, and nutrient-dense amla packed with natural vitamin C.",
        "checkpoints": [
            {
                "question": "Why are seasonal winter vegetables like spinach, fenugreek, and mustard greens scientifically valuable during Shishir?",
                "options": [
                    "They are rich in iron, minerals, and vitamins that strengthen human immunity and nourish the body during cold weather",
                    "They contain toxic chemicals that freeze the body",
                    "They can only be digested in boiling oil",
                    "They turn humans green like trees"
                ],
                "correct": 0,
                "explanation": "Green winter leafy vegetables are loaded with essential micronutrients, vitamins A, C, and K, and dietary iron that boost winter health.",
                "study_insight": "Eating locally grown seasonal produce provides the optimal nutritional balance for each environmental phase."
            },
            {
                "question": "What is the complete chronological sequence of the Six Traditional Indian Seasons (Shad Ritu)?",
                "options": [
                    "Vasanta (Spring) -> Grishma (Summer) -> Varsha (Monsoon) -> Sharad (Autumn) -> Hemant (Pre-winter) -> Shishir (Winter)",
                    "Grishma -> Shishir -> Vasanta -> Varsha -> Hemant -> Sharad",
                    "Varsha -> Hemant -> Grishma -> Shishir -> Vasanta -> Sharad",
                    "Shishir -> Grishma -> Sharad -> Vasanta -> Varsha -> Hemant"
                ],
                "correct": 0,
                "explanation": "The traditional Vedic calendar tracks the astronomical solar year through 6 distinct two-month seasons starting with Vasanta.",
                "study_insight": "Each of the six seasons lasts two lunar months, perfectly dividing the 12-month solar year into harmonious ecological chapters."
            }
        ]
    },

    # Slide 12: Regional Contrasts
    {
        "id": 12,
        "title": "Regional Contrasts",
        "subtitle": "Geographical Diversity in India's Seasonal Climate",
        "concept_html": """
            <p>India is a vast subcontinent with dramatic geographical contrasts, meaning that seasons are experienced very differently in different parts of our country:
                <ul class='list-disc pl-5 space-y-1 text-slate-300'>
                    <li><strong>The Himalayan North (Kashmir, Ladakh, Himachal):</strong> Winters bring sub-zero temperatures, freezing blizzards, and feet of powdery snow. People live in insulated wooden homes with charcoal-heated <em>Kangris</em>.</li>
                    <li><strong>The Peninsular South (Kerala, Tamil Nadu):</strong> Surrounded by oceans near the equator, southern India experiences a maritime tropical climate with mild, warm winters (rarely dropping below 20 °C) and two monsoon spells (Southwest and Northeast monsoons).</li>
                    <li><strong>The Western Desert (Rajasthan):</strong> Extreme temperature swings: blazing 48 °C summer days, cold winter desert nights, and very sparse rainfall.</li>
                    <li><strong>The Rainy Northeast (Meghalaya, Assam):</strong> Home to Mawsynram and Cherrapunji, receiving the world's highest annual rainfall (over 11,000 mm) during massive monsoons.</li>
                </ul>
            </p>
        """,
        "spoken_text": "Because India is so geographically diverse, our seasons feel completely different depending on where you live. While children in Kashmir and Ladakh build snowmen and wear heavy woollen pherans in freezing sub-zero winters, children in Kerala and Tamil Nadu experience pleasant, warm days by the Arabian Sea, wearing light cotton clothes all year. In Rajasthan, the Thar Desert experiences blistering summer heat, while the lush green hills of Meghalaya in the Northeast receive the highest rainfall in the world. India's geography paints every season with unique local colours.",
        "lecture_script": "Because India is so geographically diverse, our seasons feel completely different depending on where you live. While children in Kashmir and Ladakh build snowmen and wear heavy woollen pherans in freezing sub-zero winters, children in Kerala and Tamil Nadu experience pleasant, warm days by the Arabian Sea, wearing light cotton clothes all year. In Rajasthan, the Thar Desert experiences blistering summer heat, while the lush green hills of Meghalaya in the Northeast receive the highest rainfall in the world. India's geography paints every season with unique local colours.",
        "checkpoints": [
            {
                "question": "Why does coastal Kerala experience mild, pleasant winters while mountainous Kashmir experiences freezing snow during December and January?",
                "options": [
                    "Kerala is near the warm tropical equator and bordered by stabilizing oceans, whereas Kashmir is at high northern latitude and elevated mountain altitude",
                    "Kerala has no winter season at all because the Earth does not spin there",
                    "Kashmir is located on the Moon",
                    "Kerala is heated by volcanic lava every night"
                ],
                "correct": 0,
                "explanation": "Climate depends on latitude, altitude above sea level, and proximity to oceans (maritime effect vs continental mountain climate).",
                "study_insight": "Large water bodies heat and cool much more slowly than land, keeping coastal regions warm in winter and moderate in summer."
            },
            {
                "question": "Which northeastern Indian state holds the global record for the highest annual monsoon rainfall on Earth?",
                "options": [
                    "Meghalaya (Mawsynram / Cherrapunji)",
                    "Rajasthan",
                    "Gujarat",
                    "Punjab"
                ],
                "correct": 0,
                "explanation": "Mawsynram in Meghalaya receives an average of over 11,800 millimetres of rainfall each year due to funneling monsoon winds hitting the Khasi Hills.",
                "study_insight": "The name Meghalaya literally means 'Abode of the Clouds' in Sanskrit (Megha = cloud, Alaya = abode)."
            }
        ]
    },

    # Slide 13: Seasonal Crops
    {
        "id": 13,
        "title": "Seasonal Crops",
        "subtitle": "Kharif, Rabi, and Zaid: Agricultural Rhythm of the Land",
        "concept_html": """
            <p>Indian agriculture dances in tune with nature's rhythm, categorized into three distinct cropping seasons:
                <ul class='list-disc pl-5 space-y-1 text-slate-300'>
                    <li><strong>Kharif Crops (Monsoon / Summer Sowing):</strong> Sown with the onset of the monsoon in June and July, and harvested in autumn (September–October). These crops require abundant water and warm sunshine: <em>Rice (Paddy), Maize, Jowar, Bajra, Cotton, Soybean, and Groundnut</em>.</li>
                    <li><strong>Rabi Crops (Winter Sowing):</strong> Sown in winter (October–November) and harvested in spring (March–April). These crops thrive in cool weather and moderate moisture: <em>Wheat, Barley, Mustard, Gram (Chickpeas), and Green Peas</em>.</li>
                    <li><strong>Zaid Crops (Short Summer Season):</strong> Grown during the short dry gap between Rabi harvest and Kharif monsoon (March to June): <em>Watermelon, Muskmelon, Cucumber, Bitter Gourd, and Fodder crops</em>.</li>
                </ul>
            </p>
        """,
        "spoken_text": "Our farmers organize their agricultural work into three seasonal cycles. First are the Kharif crops, sown as the monsoon rains begin in June and harvested in autumn. These thirsty crops include rice paddy, maize, cotton, and groundnuts. Next come the Rabi crops, sown in the cool soil of November and harvested in sunny March and April. Wheat, golden mustard, chickpeas, and green peas are famous Rabi crops. Finally, during the hot summer gap between March and June, farmers plant quick-growing Zaid crops like sweet watermelons, cucumbers, and gourds.",
        "lecture_script": "Our farmers organize their agricultural work into three seasonal cycles. First are the Kharif crops, sown as the monsoon rains begin in June and harvested in autumn. These thirsty crops include rice paddy, maize, cotton, and groundnuts. Next come the Rabi crops, sown in the cool soil of November and harvested in sunny March and April. Wheat, golden mustard, chickpeas, and green peas are famous Rabi crops. Finally, during the hot summer gap between March and June, farmers plant quick-growing Zaid crops like sweet watermelons, cucumbers, and gourds.",
        "checkpoints": [
            {
                "question": "Which of these crop groups represents classic Rabi (winter-sown, spring-harvested) crops in India?",
                "options": [
                    "Wheat, Mustard, Barley, and Green Peas",
                    "Paddy rice, Cotton, and Jute",
                    "Watermelon and Muskmelon",
                    "Rubber trees and tea leaves"
                ],
                "correct": 0,
                "explanation": "Wheat and mustard require cool temperatures for vegetative growth and warm sunshine for seed ripening, making them classic Rabi crops.",
                "study_insight": "The word Rabi comes from Arabic, meaning 'spring', referring to the season in which the crop is harvested."
            },
            {
                "question": "Why is rice paddy sown at the start of the monsoon season rather than in the middle of dry winter?",
                "options": [
                    "Rice is a semi-aquatic crop that requires standing water and warm temperatures for healthy seedling growth",
                    "Rice seeds freeze into stone if touched by rain",
                    "Rice only grows in complete darkness",
                    "Because farmers are not allowed to farm in winter"
                ],
                "correct": 0,
                "explanation": "Rice seedlings require standing water (often 5 to 10 cm deep) in the early stages, relying on heavy monsoon downpours for natural irrigation.",
                "study_insight": "Flooding paddy fields also naturally suppresses weed growth without requiring chemical herbicides."
            }
        ]
    },

    # Slide 14: Harvest Festivals
    {
        "id": 14,
        "title": "Harvest Festivals",
        "subtitle": "Connecting Nature's Bountiful Cycles with Human Celebration",
        "concept_html": """
            <p>Across every state of India, traditional festivals are inextricably linked with the astronomical movements of the Sun, the arrival of seasons, and the harvesting of crops:
                <ul class='list-disc pl-5 space-y-1 text-slate-300'>
                    <li><strong>Makar Sankranti / Pongal / Lohri / Magh Bihu (January):</strong> Celebrates the winter harvest and the Sun entering the northern hemisphere (<em>Uttarayana</em>). Families prepare sweet dishes of freshly harvested rice, sesame (til), and jaggery.</li>
                    <li><strong>Baisakhi (Punjab) & Rongali Bihu (Assam) (April):</strong> Welcomes spring and celebrates the bountiful golden wheat harvest in the north and the new year seeding in the northeast.</li>
                    <li><strong>Onam (Kerala - August/September):</strong> Welcomes legendary King Mahabali and celebrates the grand post-monsoon harvest with floral carpets (Pookalam) and boat races.</li>
                    <li><strong>Holi (March):</strong> Welcomes the vibrant arrival of Vasanta spring, celebrating blossoming flowers with natural herbal colours.</li>
                </ul>
            </p>
        """,
        "spoken_text": "Across India, our greatest cultural celebrations are joyful thank-you parties for nature's bounty. In January, when winter crops are gathered and the Sun begins its northward journey, the entire country celebrates under different regional names: Makar Sankranti with soaring kites, Pongal in Tamil Nadu with boiling pots of sweet rice, Lohri with community bonfires in Punjab, and Magh Bihu with community feasts in Assam. In April, farmers celebrate the golden wheat harvest with energetic Bhangra dancing during Baisakhi. Our festivals remind us that human happiness is deeply rooted in the fertility of the earth.",
        "lecture_script": "Across India, our greatest cultural celebrations are joyful thank-you parties for nature's bounty. In January, when winter crops are gathered and the Sun begins its northward journey, the entire country celebrates under different regional names: Makar Sankranti with soaring kites, Pongal in Tamil Nadu with boiling pots of sweet rice, Lohri with community bonfires in Punjab, and Magh Bihu with community feasts in Assam. In April, farmers celebrate the golden wheat harvest with energetic Bhangra dancing during Baisakhi. Our festivals remind us that human happiness is deeply rooted in the fertility of the earth.",
        "checkpoints": [
            {
                "question": "Which major pan-Indian festival celebrated in mid-January honors the winter harvest and the northward journey of the Sun (Uttarayana)?",
                "options": [
                    "Makar Sankranti (known also as Pongal, Lohri, and Magh Bihu)",
                    "Independence Day",
                    "Children's Day",
                    "Teachers' Day"
                ],
                "correct": 0,
                "explanation": "Makar Sankranti marks the solar transition into the constellation Capricorn (Makara) and celebrates the winter harvest across India.",
                "study_insight": "Unlike many Indian lunar festivals, Makar Sankranti is based on the solar calendar and almost always falls on January 14 or 15."
            },
            {
                "question": "What common theme unites harvest festivals like Baisakhi in Punjab, Rongali Bihu in Assam, and Nabanna in Bengal?",
                "options": [
                    "Gratitude to nature, soil, rain, and livestock for granting an abundant crop harvest",
                    "Celebrating the invention of mobile phones",
                    "Honoring industrial plastic manufacturing",
                    "Competing in video games"
                ],
                "correct": 0,
                "explanation": "Harvest festivals are expressions of communal gratitude to the elements of nature that sustained the community's food supply.",
                "study_insight": "In many harvest festivals, the first grains harvested are offered to the community and cattle before personal consumption."
            }
        ]
    },

    # Slide 15: Living in Rhythm
    {
        "id": 15,
        "title": "Living in Rhythm",
        "subtitle": "Harmonizing Food, Clothing, and Daily Health with Nature",
        "concept_html": """
            <p>For thousands of years, Indian traditional wisdom and modern biological science have emphasized living in harmony with nature's seasonal rhythms:
                <ul class='list-disc pl-5 space-y-1 text-slate-300'>
                    <li><strong>Seasonal Diet (Ritucharya):</strong> Eating what is fresh, local, and in season. Cooling foods like cucumber, barley, and buttermilk in summer; warming, energy-dense foods like millet (bajra), sesame, and ghee in winter.</li>
                    <li><strong>Protective Clothing:</strong> Airy, light-colored cotton weaves that promote evaporative cooling in summer vs layered woollen fabrics that trap insulating dead air in winter.</li>
                    <li><strong>Hydration and Wellness:</strong> Replenishing water and electrolytes through lemon water and aam panna during heatwaves; boosting immunity with turmeric milk, ginger, and tulsi during wet monsoon dampness and winter chills.</li>
                </ul>
            </p>
        """,
        "spoken_text": "Living in rhythm with nature means listening to our bodies as the seasons turn. In summer, we choose light, loose cotton fabrics that allow perspiration to evaporate, and enjoy cooling meals of curd, buttermilk, and cucumbers. In the cold winter, we layer warm woollen shawls and nourish ourselves with hearty hot meals of bajra roti, jaggery, and golden ghee. By eating local, seasonal foods and dressing appropriately for the weather, we stay healthy, energized, and deeply connected to the natural world.",
        "lecture_script": "Living in rhythm with nature means listening to our bodies as the seasons turn. In summer, we choose light, loose cotton fabrics that allow perspiration to evaporate, and enjoy cooling meals of curd, buttermilk, and cucumbers. In the cold winter, we layer warm woollen shawls and nourish ourselves with hearty hot meals of bajra roti, jaggery, and golden ghee. By eating local, seasonal foods and dressing appropriately for the weather, we stay healthy, energized, and deeply connected to the natural world.",
        "checkpoints": [
            {
                "question": "Why is eating local, seasonal food during its natural harvest period scientifically beneficial for human health?",
                "options": [
                    "Seasonal produce is harvested at peak nutritional value, requires less artificial preservation, and matches bodily thermal needs",
                    "Because non-seasonal food glows in the dark",
                    "Because out-of-season food turns into plastic in the stomach",
                    "Because all seasonal food is naturally salty"
                ],
                "correct": 0,
                "explanation": "Seasonal produce delivers maximum freshness, vitamins, and antioxidants while naturally addressing the body's climatic demands.",
                "study_insight": "The ancient Indian medical tradition of Ritucharya outlines seasonal lifestyle and dietary routines to maintain bodily balance."
            },
            {
                "question": "How do layered woollen clothes keep us warm during the coldest weeks of Shishir winter?",
                "options": [
                    "By trapping stagnant pockets of air between layers, creating an insulating thermal barrier that prevents body heat from escaping",
                    "By radiating radioactive heat directly into our muscles",
                    "By attracting magnetic heat waves from the Moon",
                    "By preventing human blood from moving"
                ],
                "correct": 0,
                "explanation": "Stagnant trapped air is an exceptionally poor conductor of heat, preventing metabolic body warmth from being conducted away into cold air.",
                "study_insight": "Two thin sweaters with trapped air between them keep you warmer than a single heavy sweater of equal thickness."
            }
        ]
    },

    # Slide 16: Nature's Harmony
    {
        "id": 16,
        "title": "Nature's Harmony",
        "subtitle": "Change as Cyclic, Essential, and Interconnected",
        "concept_html": """
            <p>As we conclude our journey through the rhythms of nature, we understand a profound ecological truth: <strong>change is not something to fear—it is the very breath of life</strong>. Without the scorching heat of summer, the rain-bearing monsoon clouds would never gather. Without the drenching monsoon, crops would wither and wells would dry up. Without the resting chill of winter, trees would not renew their vitality for the vibrant blooms of spring.</p>
            <p>Every living creature, from the microscopic soil microbe to the soaring eagle and human beings, is part of this grand, interconnected web. By caring for our environment, planting trees, conserving water, and honoring the seasonal cycles, we protect the eternal rhythm of our planet.</p>
        """,
        "spoken_text": "As we complete our study of nature's rhythms, we realize a profound lesson: change is not something to worry about; it is the very heartbeat of our planet. Without the blazing heat of summer, the monsoon winds would never arise. Without the life-giving monsoon, our rivers would dry up and crops could not grow. And without the quiet rest of winter, spring could never bring its burst of fresh green leaves and sweet blossoms. Each season is essential for the next. When we respect, protect, and cherish these cycles, we become true guardians of our planet.",
        "lecture_script": "As we complete our study of nature's rhythms, we realize a profound lesson: change is not something to worry about; it is the very heartbeat of our planet. Without the blazing heat of summer, the monsoon winds would never arise. Without the life-giving monsoon, our rivers would dry up and crops could not grow. And without the quiet rest of winter, spring could never bring its burst of fresh green leaves and sweet blossoms. Each season is essential for the next. When we respect, protect, and cherish these cycles, we become true guardians of our planet.",
        "checkpoints": [
            {
                "question": "Why is the intense heat of summer essential for the arrival of the life-giving monsoon rains in India?",
                "options": [
                    "Summer solar heating warms the Indian landmass, creating an intense low-pressure zone that pulls moisture-heavy winds from the cool Indian Ocean",
                    "Because summer heat boils the ocean into steam that flies over mountains",
                    "Because lightning only exists during hot days",
                    "Because rain clouds only form near burning coal fires"
                ],
                "correct": 0,
                "explanation": "Differential heating between the warm landmass (low pressure) and cooler southern oceans (high pressure) powers the southwest monsoon.",
                "study_insight": "The monsoon is a continental-scale sea breeze powered by solar thermodynamic imbalances across the hemispheres."
            },
            {
                "question": "What overall environmental attitude does NCERT Chapter 9 encourage students to adopt toward nature's changing seasons?",
                "options": [
                    "To recognize the interconnected necessity of each season, adapt mindfully to cyclic changes, and protect nature's balance",
                    "To try to eliminate winter completely by heating the outdoors with electric heaters",
                    "To chop down trees so that leaves never fall on the school ground",
                    "To ignore the weather and stay indoors playing video games all year"
                ],
                "correct": 0,
                "explanation": "Understanding natural rhythms fosters environmental stewardship, ecological gratitude, and proactive conservation habits.",
                "study_insight": "Human civilization thrives when living in harmony with planetary rhythms rather than working against ecological systems."
            }
        ]
    }
]

print("Part 2 slides defined:", len(SLIDES_PART2))


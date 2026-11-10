# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 4 Science Chapter 9: Different Lands, Different Lives.
Strictly 195-215 words per speech.
Strictly 1-3 words per title.
2 checkpoints per slide with 4 options each.
Zero human character names, zero lecturer personas.
"""

import re
import json

slides_part1 = [
    {
        "id": 1,
        "title": "Diverse Indian Landforms",
        "badge": "Geographical Diversity",
        "sim_id": "sim_landforms_map",
        "description": "Survey the four primary physical environments of India: fertile plains, arid deserts, coastal seashores, and high mountain ranges.",
        "speech": "Welcome to our detailed science exploration of the diverse physical environments of India. Our vast country features four major geographical landforms that shape how plants, animals, and human communities thrive. Across northern and central regions lie expansive agricultural plains formed by rich river silt deposits where flat terrain supports intensive farming. To the west stretches the Thar desert, an arid wilderness of rolling sand dunes, high daytime temperatures, and scarce rainfall where drought-adapted organisms flourish. Moving southward along the vast peninsula brings us to thousands of kilometres of scenic coastal seashores where ocean tides, sandy beaches, palm groves, and rich marine biodiversity define daily coastal life. Finally, rising high into the northern skies are the mighty Himalayas, presenting rocky snow-clad peaks, steep alpine valleys, cold climates, and dense coniferous forests. Each distinct landform provides unique natural resources including varying soil types, water availability, and distinct climatic conditions. Consequently, people living in these four contrasting environments develop specialized styles of housing, distinct agricultural crops, wholesome regional cuisines, protective clothing, and colorful cultural celebrations directly attuned to their surrounding geography. As young scientists, observing these natural adaptations helps us understand the profound bond between physical landscapes and living beings everywhere.",
        "checkpoints": [
            {
                "q": "Which of the following is NOT one of the four primary landforms explored across India?",
                "options": ["Fertile agricultural plains", "Arid sandy deserts", "Coastal ocean shores", "Deep volcanic magma chambers"],
                "ans": "Deep volcanic magma chambers",
                "explanation": "India features four major surface landforms: fertile river plains, sandy arid deserts, long coastal shorelines, and high Himalayan mountain ranges."
            },
            {
                "q": "What primarily determines the housing styles, crops, and clothing of people across different regions?",
                "options": ["Surrounding physical geography and climate", "Random arbitrary decisions", "Only the color of paint available", "Factory machine brand numbers"],
                "ans": "Surrounding physical geography and climate",
                "explanation": "Human shelter, agriculture, clothing, and diets directly adapt to local climatic conditions, available natural resources, and regional landform features."
            }
        ]
    },
    {
        "id": 2,
        "title": "Fertile Agricultural Plains",
        "badge": "River Basin Ecology",
        "sim_id": "sim_punjab_plains",
        "description": "Investigate the fertile alluvial plains of northern India where perennial rivers, rich soil, cattle, and tractors sustain farming.",
        "speech": "Let us step into the expansive agricultural plains of northern India, such as the fertile river basins of Punjab. These vast flat plains were created over thousands of years by perennial rivers carrying mineral-rich silt down from the Himalayas, depositing deep layers of nutrient-dense alluvial soil. Because the terrain is remarkably level, farmers can efficiently plow vast fields, construct extensive irrigation canals, and deploy modern tractors alongside hardworking farm cattle. The agricultural calendar follows seasonal cycles, yielding abundant staple crops including golden wheat during the cool winter season and tall rice paddies during the warm monsoon months. Cattle play a central role in village farming ecosystems, providing nutrient-rich milk, pulling traditional wooden carts, and generating organic manure that replenishes soil fertility without synthetic chemicals. Groundwater tube wells and canal networks distribute fresh river water evenly across emerald green fields of mustard, sugarcane, and legumes. The level landscape also greatly simplifies the construction of rural roads, granaries, and railway networks connecting rural farms to bustling urban markets. Life on the agricultural plains is deeply intertwined with nature's seasonal rhythms, where morning mist over lush fields reflects the immense food-producing power of healthy fertile soil and collaborative rural communities.",
        "checkpoints": [
            {
                "q": "What natural geological process created the fertile agricultural plains of northern India?",
                "options": ["River silt deposition over thousands of years", "Volcanic lava cooling suddenly", "Ocean sand blown inland by storms", "Glacier ice carving deep granite canyons"],
                "ans": "River silt deposition over thousands of years",
                "explanation": "Perennial rivers flowing down from mountain ranges carry mineral-rich silt and sediment, depositing fertile alluvial soil across flat river basins."
            },
            {
                "q": "Which two major staple crops dominate the seasonal agricultural cycles in the northern plains?",
                "options": ["Wheat and rice", "Coffee and tea bushes", "Apples and saffron flowers", "Coconut and seaweed fronds"],
                "ans": "Wheat and rice",
                "explanation": "The fertile northern plains primarily cultivate golden wheat during the winter rabi cycle and rice paddies during the monsoon kharif cycle."
            }
        ]
    },
    {
        "id": 3,
        "title": "Plains Harvest Cuisine",
        "badge": "Nutritional Science",
        "sim_id": "sim_plains_nutrition",
        "description": "Analyze the wholesome farm-to-table cuisine of the northern plains, featuring yellow maize flatbread, mustard greens, and probiotic lassi.",
        "speech": "The meals enjoyed across the agricultural plains provide a magnificent lesson in nutritional science, directly reflecting local farm harvests. During chilly winter months, rural kitchens prepare steaming hot makki di roti, a hearty flatbread made from coarsely ground yellow maize flour. Yellow corn provides dense carbohydrates and dietary fiber that supply long-lasting energy for strenuous outdoor agricultural labor. This maize flatbread is traditionally paired with sarson da saag, a vibrant green preparation made by slow-cooking freshly harvested tender mustard greens alongside spinach and bathua leaves. Mustard greens are packed with essential vitamins A, C, and K, as well as vital minerals like iron and calcium that bolster human immune defenses against winter infections. To aid digestion and complete the balanced meal, farmers consume a tall brass glass of refreshing lassi, a traditional churned beverage made from thick cow or buffalo curd. Lassi delivers abundant proteins, calcium, and millions of beneficial probiotic bacteria that support healthy gut flora. When seasoned with a dollop of freshly churned white butter and wholesome jaggery, this iconic farm meal provides complete thermal warmth, muscular strength, and digestive health derived entirely from local seasonal agriculture, keeping hardworking farming families active throughout the winter.",
        "checkpoints": [
            {
                "q": "Which nutrient-dense leafy vegetable forms the primary base of the traditional dish sarson da saag?",
                "options": ["Tender mustard greens", "Dried desert cactus pads", "Saltwater marine kelp", "Highland pine needles"],
                "ans": "Tender mustard greens",
                "explanation": "Sarson da saag is prepared from fresh tender mustard greens, rich in vitamins A, C, and iron, slow-cooked with spinach leaves."
            },
            {
                "q": "What health benefit is provided by drinking traditional curd-based lassi with meals?",
                "options": ["Supplies proteins, calcium, and probiotic gut bacteria", "Stops the body from digesting any food", "Removes all water from body tissues", "Prevents teeth from absorbing minerals"],
                "ans": "Supplies proteins, calcium, and probiotic gut bacteria",
                "explanation": "Churned curd lassi delivers bioavailable protein, bone-building calcium, and beneficial live probiotics that nourish the human digestive system."
            }
        ]
    },
    {
        "id": 4,
        "title": "Golden Temple Langar",
        "badge": "Community Ecology",
        "sim_id": "sim_langar_kitchen",
        "description": "Examine the world's largest community kitchen at Sri Harmandir Sahib in Amritsar, serving hot nutritious meals to everyone.",
        "speech": "In the historic plains city of Amritsar stands the sacred Golden Temple, known as Sri Harmandir Sahib. Its gilded gold-plated sanctum rises serenely in the centre of a large freshwater lake called the Amrit Sarovar, where gentle water ripples reflect bright morning sunlight. Beyond its architectural magnificence, this revered sanctuary houses one of humanity's greatest demonstrations of social equality and community service: the historic langar kitchen. Operating continuously day and night, this massive community kitchen prepares and serves hot, hygienic, wholesome vegetarian meals free of cost to over one hundred thousand visitors every single day, regardless of social status, religion, or background. Volunteers manage enormous iron cauldrons boiling fragrant lentil dal, automated roti-making machines rolling out thousands of wheat flatbreads per hour, and large copper pots cooking warm rice pudding. Visitors sit together on long floor mats side by side, exemplifying universal brotherhood and the complete absence of social discrimination. The langar demonstrates extraordinary logistics, food safety management, and zero-waste recycling, where organic vegetable scraps are composted and stainless steel plates are systematically washed across multi-stage sanitizing tanks. It proves how communal cooperation, shared kindness, and selfless volunteer labor can eliminate hunger through noble collective human effort.",
        "checkpoints": [
            {
                "q": "What is the unique social founding principle of the historic community langar kitchen?",
                "options": ["Serving free wholesome meals to all people equally", "Charging high entry ticket fees to visitors", "Serving only wealthy royalty in private rooms", "Using disposable plastic plates once and dumping them"],
                "ans": "Serving free wholesome meals to all people equally",
                "explanation": "Langar is founded on selfless service (sewa) and absolute equality, serving free nutritious meals to everyone seated side by side on the floor."
            },
            {
                "q": "What is the name of the sacred freshwater tank surrounding the Golden Temple sanctum?",
                "options": ["Amrit Sarovar", "Chilika Lagoon", "Dal Lake", "Arabian Sea"],
                "ans": "Amrit Sarovar",
                "explanation": "The Golden Temple sanctum is situated in the centre of a large rectangular sacred freshwater tank called the Amrit Sarovar (Pool of Nectar)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Arid Desert Ecosystem",
        "badge": "Xerophytic Adaptations",
        "sim_id": "sim_desert_ecology",
        "description": "Explore the harsh Thar desert ecosystem, observing xerophytic vegetation, water storage adaptations, and nocturnal desert wildlife.",
        "speech": "Travelling westward into Rajasthan brings us to the Thar desert, an arid environment where annual rainfall is extremely low and sandy dunes stretch toward the distant horizon. Under intense solar radiation, surface temperatures soar during daytime hours, while clear desert skies cause rapid heat loss at night, creating dramatic temperature swings. To survive these dry conditions, desert plants, called xerophytes, have evolved extraordinary morphological adaptations. The iconic khejri tree sends deep taproots dozens of metres subterranean to reach hidden groundwater, while its small waxy leaflets minimize evaporative water loss. Spiny babool trees and fleshy cactus plants store precious water within swollen green stems, having transformed their leaves into sharp defensive spines that deter herbivores and reduce transpiration. Desert wildlife also displays clever survival strategies. The camel, celebrated as the ship of the desert, possesses wide padded feet that walk smoothly over loose shifting sand, long double-layered eyelashes that block blowing dust, and fat-storing humps that supply metabolic energy during long journeys. Nocturnal desert foxes, spiny-tailed lizards, sand pythons, and desert eagles conserve bodily fluids by resting in underground burrows and hunting during cooler twilight hours, demonstrating nature's resilient survival mechanisms under extreme drought and heat.",
        "checkpoints": [
            {
                "q": "Why have desert cacti evolved sharp spines instead of broad green leaves?",
                "options": ["To minimize water loss and deter grazing animals", "To attract heavy rain clouds overhead", "To absorb sunlight exclusively at night", "To freeze morning dew into solid ice"],
                "ans": "To minimize water loss and deter grazing animals",
                "explanation": "Spines minimize transpiration surface area, preventing precious moisture loss while providing physical defense against thirsty desert animals."
            },
            {
                "q": "How do wide padded feet assist camels travelling across desert environments?",
                "options": ["Distribute body weight to prevent sinking into loose sand", "Help the camel swim across deep ocean trenches", "Generate electric sparks to illuminate paths", "Allow the camel to climb sheer vertical trees"],
                "ans": "Distribute body weight to prevent sinking into loose sand",
                "explanation": "Broad, padded hooves act like snowshoes, distributing body mass over a larger surface area so camels walk effortlessly over soft shifting dunes."
            }
        ]
    },
    {
        "id": 6,
        "title": "Desert Culture Attire",
        "badge": "Cultural Anthropology",
        "sim_id": "sim_desert_culture",
        "description": "Examine how vibrant Rajasthani clothing, bandhini tie-dye textiles, and acoustic folk instruments brighten the monochromatic desert.",
        "speech": "Against the pale yellow expanses of desert sands, the traditional attire and musical heritage of Rajasthan burst with dazzling vibrancy. People wear brilliant shades of saffron, crimson, emerald green, and peacock blue, bringing joyful visual energy to the arid landscape. Men wear large multi-layered turbans, known locally as pagris, wrapped from long cotton fabric. These distinctive turbans serve vital survival functions: the dense cotton folds insulate the wearer's skull against scorching afternoon sunlight, cushion heavy loads carried on the head, and can be unfurled to filter blowing sand or act as emergency rope. Women wear graceful flared ghaghras paired with odhnis decorated using ancient tie-dye bandhini techniques, where tiny pinches of cloth are tightly knotted with thread before dyeing to create intricate circular patterns. In the evening, desert communities gather beneath starry skies to play soulful acoustic folk instruments. Musicians strike resonant wooden castanets called khartals, producing rapid rhythmic clicks, accompanied by the haunting, bowed melodies of the multi-stringed sarangi and deep clay matka drums. These vibrant artistic traditions preserve oral history, celebrate nature's precious rainfall, and strengthen community resilience across generations living happily in challenging, arid desert landscapes of western India with immense joy, courage, and enduring community solidarity.",
        "checkpoints": [
            {
                "q": "What practical environmental purpose is served by the large cotton turban (pagri) worn in desert regions?",
                "options": ["Insulates the head from intense solar heat and filters blowing sand", "Attracts lightning strikes to generate warmth", "Stores drinking water inside hollow fabric tubes", "Acts as a parachute for jumping off cliffs"],
                "ans": "Insulates the head from intense solar heat and filters blowing sand",
                "explanation": "Thick cotton turbans provide excellent thermal insulation against extreme solar radiation, protect ears from dust storms, and can filter blowing sand."
            },
            {
                "q": "What traditional Rajasthani acoustic instrument consists of hand-held wooden clappers that produce rhythmic clicks?",
                "options": ["Khartal", "Piano", "Synthesizer", "Brass trumpet"],
                "ans": "Khartal",
                "explanation": "The khartal is a traditional Rajasthani percussion instrument made of hardwood pieces clicked together by hand in rapid rhythmic accompaniment."
            }
        ]
    },
    {
        "id": 7,
        "title": "Desert Water Tankas",
        "badge": "Hydro-Engineering",
        "sim_id": "sim_tanka_system",
        "description": "Discover traditional desert architecture, thick insulating mud walls, thatch roofs, and underground rainwater harvesting tankas.",
        "speech": "In arid desert settlements where every drop of moisture is precious, traditional architectural engineering creates comfortable, sustainable living spaces. Village homes, known as jhopas, feature thick walls built from local clay, cow dung, and straw mixtures. These dense earthen walls have high thermal mass, which absorbs intense daytime heat slowly, keeping indoor rooms refreshingly cool at noon and releasing stored warmth during chilly desert nights. Conical thatched roofs woven from dry desert grasses allow air to circulate freely while deflecting direct sunlight. Most importantly, desert houses incorporate an ingenious traditional rainwater harvesting structure called a tanka. A tanka is a large underground masonry cistern built beneath the central courtyard or near the home. The paved sloping courtyard acts as a clean catchment area; when rare desert rain falls, water flows through gravel and charcoal filtration channels straight into the sealed underground chamber. Because the tanka is buried subterranean and tightly covered, stored water remains sheltered from sun evaporation, bacterial contamination, and insect breeding, providing clean drinking water for families throughout long dry months. Paired with desert delicacies like protein-rich ker sangri and dal-bati-churma, desert dwellers thrive through resourcefulness, ingenuity, mutual cooperation, and deep environmental wisdom.",
        "checkpoints": [
            {
                "q": "How do thick earthen mud walls maintain comfortable indoor temperatures in desert houses?",
                "options": ["Absorb daytime heat slowly and radiate stored warmth at night", "Allow cold winter winds to blow directly through the bedrooms", "Melt into liquid mud whenever outdoor temperatures rise", "Generate artificial air conditioning using electric batteries"],
                "ans": "Absorb daytime heat slowly and radiate stored warmth at night",
                "explanation": "High thermal mass earthen walls absorb intense daytime heat slowly, keeping interiors cool, and release warmth during cold desert nights."
            },
            {
                "q": "What is the primary function of an underground desert tanka?",
                "options": ["Harvest and store precious rainwater safely underground", "Store large quantities of coal for steam engines", "Keep pet desert foxes safe from sand eagles", "Grow freshwater aquatic lotus plants in total darkness"],
                "ans": "Harvest and store precious rainwater safely underground",
                "explanation": "A tanka is an underground covered cistern designed to collect and store filtered rainwater for household drinking throughout dry seasons."
            }
        ]
    },
    {
        "id": 8,
        "title": "Golden Sandstone Fort",
        "badge": "Passive Architecture",
        "sim_id": "sim_jaisalmer_fort",
        "description": "Examine the historic Jaisalmer Fort built from yellow sandstone, demonstrating passive cooling, narrow streets, and living heritage.",
        "speech": "Rising dramatically above the Thar desert upon the triangular Trikuta Hill stands the magnificent Jaisalmer Fort, affectionately celebrated as the Golden Fort. Constructed during the twelfth century entirely from local yellow sandstone without any binding mortar, the fort displays an uncanny camouflage, merging seamlessly with the surrounding golden sand dunes during midday and glowing with amber brilliance at sunset. Unlike museum monuments that stand empty, Jaisalmer is a vibrant living fort where thousands of residents continue to inhabit ancestral residences, operate craft workshops, and maintain age-old traditions within its fortified stone walls. The architecture demonstrates brilliant passive cooling principles tailored for extreme desert heat. Streets inside the fort are intentionally laid out narrow and winding, ensuring that towering stone facades cast cooling shadows across cobblestone walkways throughout the hottest hours of the day. Houses feature intricate overhanging balconies, called jharokhas, with delicate stone lattice screens called jalis. These perforated stone grilles utilize the Venturi effect: as hot desert air squeezes through tiny perforations, its velocity increases while its temperature drops, funneling refreshing breezes into interior living quarters without any mechanical machinery, proving how ancient builders mastered thermal comfort, climate engineering, and sustainable desert living across centuries.",
        "checkpoints": [
            {
                "q": "What unique local geological material gives Jaisalmer Fort its distinctive golden glow?",
                "options": ["Yellow sandstone", "Polished white marble", "Black volcanic basalt", "Red baked terracotta clay"],
                "ans": "Yellow sandstone",
                "explanation": "Jaisalmer Fort is built entirely from local yellow sandstone, which reflects golden hues under the desert sun and blends into the surrounding dunes."
            },
            {
                "q": "How do narrow winding streets and perforated stone jharokhas cool the interior of the fort?",
                "options": ["Cast perpetual shadows and accelerate cool breezes through lattice screens", "Trap boiling hot air permanently inside closed rooms", "Block all fresh airflow completely from entering homes", "Pump cold underground water onto exterior wall surfaces"],
                "ans": "Cast perpetual shadows and accelerate cool breezes through lattice screens",
                "explanation": "Tall facades shade narrow streets from direct solar rays, while intricate stone jali screens cool passing air via natural ventilation and the Venturi effect."
            }
        ]
    }
]

# Validation
HUMAN_NAMES = [
    'Meera', 'Dhruv', 'Raghav', 'Chandan', 'Navya', 'Amit', 'Reena', 'Pihu',
    'Gurpreet', 'Ritika', 'Chandni', 'Nayan', 'Satyajit', 'Ray',
    'Dada', 'Dadaji', 'Diya', 'Raziya', 'Rukhsana', 'Simran', 'Sunil', 'Bablu',
    'Ikra', 'Samina', 'Sumedha', 'Vinayak', 'Kumar', 'Paridhi', 'Idha', 'Karan',
    'Jaspreet', 'Gulnaz', 'Mithali', 'Suzie', 'Bates', 'Gundappa', 'Muniamma',
    'Shirley', 'Shiv', 'Jagat', 'Bholu', 'Rani', 'Preet', 'Diksha', 'Raman',
    'Sheela', 'Sunita', 'Mary', 'Akira', 'Preetha', 'Adrit', 'Rohan', 'Anjali',
    'Aarav', 'Ananya', 'Priya', 'Rahul', 'Neha', 'Sanjay', 'Vikram', 'Shrinathan',
    'Mirabai', 'Gulabo', 'Anvi', 'Raju', 'Parv', 'Chinnu', 'Abha', 'Didi',
    'Daisy', 'Lou', 'Sapan', 'Udaya', 'Krishna', 'Sudama', 'Mala', 'Neela', 'Bhola'
]

FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== CHECKING SLIDES 1 TO 8 ===")
for s in slides_part1:
    sid = s['id']
    title = s['title']
    wc = len(s['speech'].split())
    print(f"Slide {sid} '{title}': {wc} words")

for s in slides_part1:
    sid = s['id']
    title = s['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"
    
    wc = len(s['speech'].split())
    assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words (must be 195-215)"
    
    s_str = json.dumps(s)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + re.escape(name) + r'\b', s_str, re.IGNORECASE), f"Slide {sid} contains name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
    
    assert len(s['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
    for cp in s['checkpoints']:
        assert len(cp['options']) == 4, f"Slide {sid} checkpoint must have 4 options"

print("Slides 1 to 8 verified successfully!")

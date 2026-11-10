# -*- coding: utf-8 -*-
"""
Generate Slides 9 to 16 for Class 4 Science Chapter 9: Different Lands, Different Lives.
Strictly 195-215 words per speech.
Strictly 1-3 words per title.
2 checkpoints per slide with 4 options each.
Zero human character names, zero lecturer personas.
"""

import re
import json

slides_part2 = [
    {
        "id": 9,
        "title": "Puri Coastal Seashore",
        "badge": "Marine Shoreline Ecology",
        "sim_id": "sim_puri_coast",
        "description": "Examine the dynamic sandy beaches of Puri on the eastern coast of Odisha, coastal palm trees, and fishing livelihoods.",
        "speech": "Journeying south-east toward the Bay of Bengal brings us to the vibrant coastal shoreline of Puri in Odisha. Here, the ocean interface creates a dynamic marine environment where rhythmic tidal waves continuously shape expansive golden sand beaches. Tall coconut palms and slender palmyra trees line the coastal dunes, their flexible curved trunks bending gracefully with powerful ocean breezes while their deep root networks stabilize loose shoreline sand against coastal erosion. Artisanal fishing forms the economic backbone of coastal communities. Early in the morning, traditional fishermen navigate motorized wooden boats and catamarans through crashing surf into open sea waters, deploying large cast nets to catch fish, prawns, and crabs. On the sandy shore, talented sculptors carve magnificent temporary sand art, sculpting intricate animals, mythical figures, and environmental conservation messages out of moist sea sand and saltwater. The sea air is rich in moisture and saline aerosols, providing moderate temperatures that remain relatively consistent throughout the year. Children stroll along the high-tide line collecting smooth wave-polished pebbles, delicate spiraled sea shells, and moulted crab carapaces, discovering firsthand how ocean currents continuously deliver biological treasures from hidden underwater realms onto sunny sandy shores throughout every season of the year.",
        "checkpoints": [
            {
                "q": "How do deep root systems of coastal coconut and palm trees protect shorelines?",
                "options": ["Anchor loose sand and protect dunes from ocean erosion", "Pump salty seawater directly onto inland farm crops", "Attract fierce hurricane waves toward village homes", "Turn beach sand into solid hard grey granite rock"],
                "ans": "Anchor loose sand and protect dunes from ocean erosion",
                "explanation": "Extensive fibrous root systems of coastal palms bind loose sand grains together, preventing tidal waves and coastal winds from washing away dunes."
            },
            {
                "q": "What primary natural activity shapes the dynamic beaches along coastal seashores?",
                "options": ["Rhythmic ocean tides and continuous wave action", "Hot volcanic lava spilling across beaches daily", "Deep underground earthquake faults shifting mountains", "Heavy snowfalls freezing the sand into glaciers"],
                "ans": "Rhythmic ocean tides and continuous wave action",
                "explanation": "Beaches are shaped constantly by the mechanical energy of incoming tides and breaking ocean waves that transport, sort, and deposit sand particles."
            }
        ]
    },
    {
        "id": 10,
        "title": "Marine Coastal Biodiversity",
        "badge": "Ocean Biology",
        "sim_id": "sim_marine_life",
        "description": "Investigate the rich marine biodiversity of the Odisha coast, including endangered olive ridley sea turtles, dolphins, and crabs.",
        "speech": "The waters and sandy shores along the Odisha coastline harbor an astonishing diversity of specialized marine wildlife. Among the most celebrated ocean visitors are endangered olive ridley sea turtles. Every winter, hundreds of thousands of these ancient reptiles migrate thousands of kilometres across vast oceans to assemble at specific sandy nesting beaches, such as Gahirmatha and the Rushikulya river mouth. During mass nesting events, called arribadas, mother turtles crawl ashore under nocturnal skies, using their hind flippers to scoop deep flask-shaped pits in the sand where they deposit approximately one hundred soft-shelled eggs before returning to the sea. The warm beach sand incubates the eggs until tiny hatchlings emerge and scurry toward the moonlit ocean waves. Just offshore, graceful dolphins leap through breaking swells, communicating with high-frequency clicks and echolocation whistles as they hunt schools of silver fish. Along intertidal rock pools and mudflats, scurrying ghost crabs, hermit crabs living in discarded gastropod shells, spiny sea starfish, and green seaweeds create intricate coastal food webs. Preserving these sensitive marine habitats against plastic litter, artificial light pollution, and mechanical fishing trawlers is critical for safeguarding planetary ocean biodiversity and protecting fragile marine organisms for future generations to cherish.",
        "checkpoints": [
            {
                "q": "What is the unique phenomenon of synchronized mass nesting by olive ridley sea turtles called?",
                "options": ["Arribada", "Metamorphosis", "Echolocation", "Photosynthesis"],
                "ans": "Arribada",
                "explanation": "Arribada is the Spanish term used worldwide for the synchronized nocturnal arrival of thousands of sea turtles nesting simultaneously on beaches."
            },
            {
                "q": "Why are artificial bright beach lights dangerous for newly hatched baby sea turtles?",
                "options": ["Disorient hatchlings, leading them away from the moonlit ocean", "Cause the hatchlings to grow feathers and fly into trees", "Cool the ocean water down into freezing ice blocks", "Make the sand so heavy that baby turtles cannot move"],
                "ans": "Disorient hatchlings, leading them away from the moonlit ocean",
                "explanation": "Hatchlings instinctively follow the natural bright horizon of the moon over the sea; artificial shore lighting misguides them toward roads and predators."
            }
        ]
    },
    {
        "id": 11,
        "title": "Coastal Chariot Heritage",
        "badge": "Living Cultural Heritage",
        "sim_id": "sim_rath_yatra",
        "description": "Examine the sacred architecture of the Shree Jagannath Temple in Puri, the grand annual Rath Yatra, and classical Odissi dance.",
        "speech": "Beyond its natural oceanic wealth, Puri is globally celebrated for its majestic spiritual heritage and architectural marvels. The grand Shree Jagannath Temple, built over eight centuries ago from weather-resistant khondalite stone, rises sixty-five metres into the coastal sky. Its carved curvilinear spire displays master stone masonry, featuring intricate relief carvings of elephants, floral creepers, and musicians. Every summer, Puri hosts the awe-inspiring Rath Yatra festival, where three towering wooden chariots, reaching heights of forty-five feet and mounted upon massive multi-spoke wooden wheels, are constructed anew by hereditary carpenters using traditional joinery without metal nails. Millions of pilgrims gather on the Grand Avenue, eagerly grasping enormous coir ropes to pull the massive sacred chariots through the streets in an extraordinary display of shared devotion, unity, and communal cooperation. Coastal Odisha is equally famous for classical Odissi dance, one of India's oldest performing arts. Dancers wear gorgeous local silk saris adorned with silver filigree jewellery, stamping rhythmic feet and using graceful torso bends called tribhanga that mirror the undulating waves of the adjacent ocean. These centuries-old traditions celebrate the deep spiritual connection between coastal communities, artistic devotion, architectural mastery, and their dynamic maritime environment throughout human history.",
        "checkpoints": [
            {
                "q": "What remarkable traditional feature characterizes the construction of the giant chariots for Rath Yatra?",
                "options": ["Built entirely from seasoned wood using interlocking joints without metal nails", "Constructed using welded industrial steel sheets and diesel engines", "Made from inflated rubber balloons filled with helium gas", "Printed overnight using large plastic three-dimensional machines"],
                "ans": "Built entirely from seasoned wood using interlocking joints without metal nails",
                "explanation": "Hereditary master craftsmen construct the three mammoth chariots each year from timber using ancient wooden joinery, dowels, and clamps without iron nails."
            },
            {
                "q": "Which classical Indian dance form originating from coastal Odisha features fluid wave-like postures?",
                "options": ["Odissi", "Kathakali", "Bhangra", "Garba"],
                "ans": "Odissi",
                "explanation": "Odissi is the classical dance form of Odisha, characterized by rhythmic footwork and the graceful three-bend body posture called tribhanga."
            }
        ]
    },
    {
        "id": 12,
        "title": "Cyclone Early Warning",
        "badge": "Disaster Management",
        "sim_id": "sim_cyclone_warning",
        "description": "Investigate coastal tropical cyclone hazards, ocean storm surges, and Odisha's award-winning disaster preparedness network.",
        "speech": "Living along the coastal shoreline requires exceptional resilience, because the warm waters of the Bay of Bengal regularly generate intense tropical cyclones. These ferocious ocean storms bring roaring gale-force winds exceeding one hundred and fifty kilometres per hour, torrential downpours, and devastating seawater storm surges that inundate low-lying coastal villages. In past decades, unexpected super cyclones caused catastrophic loss of human life. However, the coastal state of Odisha has developed an internationally celebrated, award-winning disaster management system. State-of-the-art Doppler weather radars, ocean buoys, and meteorological satellites continuously track storm formations hundreds of kilometres offshore, calculating precise landfall trajectories forty-eight hours in advance. High-decibel coastal siren towers broadcast urgent multilingual evacuation warnings to seaside fishing villages. A widespread network of elevated concrete multi-purpose cyclone shelters, equipped with solar power generators, emergency medical supplies, and purified drinking water reservoirs, provide safe refuge for coastal families and their livestock. Community volunteers systematically organize pre-landfall evacuations, clearing drainage channels, stocking dry food rations, and demonstrating zero-casualty disaster preparedness. This modern scientific framework proves that while humans cannot prevent extreme natural hazards, rigorous early warning technology and coordinated community action can protect vulnerable coastal lives with extraordinary success and lasting peace of mind.",
        "checkpoints": [
            {
                "q": "What modern scientific equipment tracks incoming tropical cyclones hundreds of kilometres out at sea?",
                "options": ["Doppler weather radars and meteorological satellites", "Handheld magnifying glasses and paper kites", "Traditional wooden flutes and acoustic drums", "Underground coal mining drill bits"],
                "ans": "Doppler weather radars and meteorological satellites",
                "explanation": "Meteorological satellites and coastal Doppler radar systems track cyclone pressure, cloud rotation, and wind speeds in real time to forecast landfall."
            },
            {
                "q": "What specialized community infrastructure provides safe refuge during severe coastal cyclones?",
                "options": ["Elevated concrete multi-purpose cyclone shelters", "Temporary cloth camping tents pitched on beaches", "Underground coal mine shafts prone to flooding", "Open wooden fishing boats anchored near coral reefs"],
                "ans": "Elevated concrete multi-purpose cyclone shelters",
                "explanation": "Elevated cyclone shelters built on reinforced concrete pillars withstand high storm surges and ferocious winds, sheltering thousands safely."
            }
        ]
    },
    {
        "id": 13,
        "title": "Himalayan Mountain Landforms",
        "badge": "Alpine Geography",
        "sim_id": "sim_sikkim_mountains",
        "description": "Explore the breathtaking mountain landscapes of Sikkim, steep rocky ridges, rushing glacial torrents, and Mount Kangchenjunga.",
        "speech": "Leaving the coastal plains behind and ascending thousands of metres northward brings us into the spectacular mountain landscapes of Sikkim in the eastern Himalayas. Here, the earth rises in dramatic vertical relief, featuring towering snow-capped mountain peaks, deep V-shaped river gorges, steep rocky escarpments, and crystal-clear glacial streams tumbling over granite boulders. Dominating the skyline is Mount Kangchenjunga, the third highest peak on Earth, rising majestically to an altitude of eight thousand five hundred and eighty-six metres. At dawn, as the first rays of morning sunlight strike its permanent glaciers, the snow glows with ethereal golden and crimson hues, revered by local mountain communities as a sacred protective guardian. Because of the steep terrain, flat land is virtually non-existent; hill communities construct tiered terrace farms on hillsides to cultivate maize, ginger, and large black cardamom. The thin alpine air holds less atmospheric pressure and oxygen, while temperatures drop significantly with increasing altitude, bringing freezing winter snowfalls and cool summer breezes. Swift rivers like the Teesta surge through valleys, carving dramatic canyons and powering eco-friendly hydroelectric turbines, exemplifying the awe-inspiring geological forces, raw beauty, ecological majesty, and clean renewable energy potential of high mountain regions in the Himalayas.",
        "checkpoints": [
            {
                "q": "Which magnificent Himalayan mountain peak dominates the skyline of Sikkim as the third highest mountain on Earth?",
                "options": ["Mount Kangchenjunga", "Mount Kilimanjaro", "Mount Fuji", "Mount Aconcagua"],
                "ans": "Mount Kangchenjunga",
                "explanation": "Mount Kangchenjunga, standing at 8,586 metres in Sikkim, is the third highest mountain peak in the world and sacred to local communities."
            },
            {
                "q": "Why do mountain farmers construct stepped terrace fields on steep hillside slopes?",
                "options": ["Create flat planting surfaces and prevent soil erosion from rainwater runoff", "Allow farm tractors to drive at supersonic speeds down hills", "Make the mountain look like giant stairs for pet mountain goats", "Block all sunshine from reaching the river valleys below"],
                "ans": "Create flat planting surfaces and prevent soil erosion from rainwater runoff",
                "explanation": "Terrace farming cuts flat stepped benches into hillsides, enabling crop cultivation while reducing downhill water runoff and preventing topsoil erosion."
            }
        ]
    },
    {
        "id": 14,
        "title": "Mountain Lifestyle Warmth",
        "badge": "Highland Living",
        "sim_id": "sim_mountain_lifestyle",
        "description": "Examine highland living in Sikkim, thermal woollen bakhu garments, steaming thukpa noodle soup, sel roti, and domesticated yaks.",
        "speech": "Living in cold Himalayan altitudes requires practical cultural adaptations designed to preserve bodily warmth, sustain physical energy, and traverse rugged mountainous terrain. People wear warm traditional garments crafted from heavy sheep wool and silk. The iconic attire, known as the bakhu, is a voluminous wrap-around woollen coat tied securely at the waist with a broad fabric sash, paired with a colourful inner blouse called a honju. This layered attire traps insulating air pockets near the body, shielding the wearer from icy mountain gales. Highland culinary habits prioritize piping-hot, calorie-dense foods that generate metabolic heat. Families gather around crackling wood stoves to enjoy steaming bowls of thukpa, a wholesome Tibetan noodle soup loaded with vegetables, seasonal greens, and aromatic warming spices, alongside golden-brown, ring-shaped crispy rice flatbreads called sel roti. For high-altitude transportation, communities depend upon the magnificent domestic yak. Possessing thick, shaggy double-layered wool coats, broad hooves that grip icy mountain ledges securely, and specialized lungs adapted for thin high-altitude air, yaks transport heavy loads across snowbound mountain passes while providing nutritious, rich milk churned into protein-dense chhurpi cheese, showcasing how mountain communities thrive in complete harmony with highland fauna across the eastern Himalayas with great resilience.",
        "checkpoints": [
            {
                "q": "What is the traditional wrap-around woollen dress worn in Sikkim to insulate against cold mountain winds?",
                "options": ["Bakhu", "Kimono", "Sombrero", "Toga"],
                "ans": "Bakhu",
                "explanation": "The bakhu is the traditional Sikkimese full-length dress tied at the waist with a belt, providing excellent thermal insulation against alpine cold."
            },
            {
                "q": "Which sturdy domesticated highland animal provides rich milk, wool, and sure-footed transport across snowy mountain passes?",
                "options": ["Yak", "Desert camel", "Coastal dolphin", "River crocodile"],
                "ans": "Yak",
                "explanation": "Yaks are superbly adapted to freezing Himalayan altitudes, having thick shaggy wool, powerful lungs for thin air, and sure-footed hooves for rocky trails."
            }
        ]
    },
    {
        "id": 15,
        "title": "Mountain Flora Festivals",
        "badge": "Montane Ecology",
        "sim_id": "sim_mountain_festivals",
        "description": "Discover alpine forests of oak, pine, and chestnut, sloping-roof wooden architecture, Loosong harvest celebrations, and masked chaam dances.",
        "speech": "The lush slopes of Sikkim are blanketed with magnificent montane temperate and alpine forests. Sturdy evergreen oaks, towering Himalayan blue pines, silver firs, fragrant walnuts, and sweet chestnut trees thrive along hillside contours, their roots binding steep rocky soil against heavy monsoon downpours. Traditional mountain houses are ingeniously engineered for cold, wet conditions. Built primarily from seasoned local timber with stone plinths, these homes feature steep, pitched roofs made of corrugated iron sheets or wooden shingles. These steep angles ensure that heavy seasonal monsoon rains and winter snowfalls slide off roofs instantly, preventing structural water accumulation and roof collapse. In December, following the harvest, mountain communities celebrate Loosong and Namsoong, marking the joyous Sikkimese New Year. In ancient Buddhist monasteries like Enchey and Rumtek, monks perform the mesmerizing chaam dance, donning vibrant silk robes and magnificent wooden masks depicting benevolent deities and mythical animals. Accompanied by the deep resonance of long copper horns called dungchens, sounding drums, and rhythmic cymbals, the masked dancers whirl gracefully in monastery courtyards, celebrating the triumph of good over evil, purifying the environment, and invoking divine blessings for abundant future harvests throughout every single peaceful highland village and fertile mountain valley.",
        "checkpoints": [
            {
                "q": "Why do traditional mountain houses feature steeply sloping roofs?",
                "options": ["Allow heavy rain and winter snow to slide off quickly without collapsing the roof", "Provide a smooth runway for aeroplanes to land safely", "Collect large quantities of autumn fallen leaves permanently", "Block all fresh mountain air from entering through the chimney"],
                "ans": "Allow heavy rain and winter snow to slide off quickly without collapsing the roof",
                "explanation": "Pitched, sloping roofs shed heavy monsoon rainwater and thick winter snow rapidly, preventing structural overload and water damage."
            },
            {
                "q": "What traditional sacred dance featuring elaborate wooden masks and silk robes is performed during mountain festivals?",
                "options": ["Chaam dance", "Breakdance", "Salsa", "Flamenco"],
                "ans": "Chaam dance",
                "explanation": "The chaam is a sacred monastic masked dance performed during festivals like Loosong to purify negative energy and celebrate spiritual harmony."
            }
        ]
    },
    {
        "id": 16,
        "title": "Landform Comparison Matrix",
        "badge": "Comparative Geography",
        "sim_id": "sim_comparison_matrix",
        "description": "Synthesize and compare the four distinct Indian landforms across climate, soil, flora, fauna, shelter, cuisine, and human adaptations.",
        "speech": "As we conclude our comprehensive scientific survey of India's physical geography, comparing our findings across all four landforms reveals profound ecological insights. Each geographical realm represents a complete, harmonious web of interconnections where climate, soil, vegetation, and human culture exist in perfect balance. On the agricultural plains, flat alluvial soil, river networks, and seasonal monsoons yield abundant wheat, mustard greens, and dairy herds that feed millions through cooperative farming. In the arid Thar desert, extreme drought, intense solar heat, and shifting dunes foster deep-rooted khejri trees, padded-footed camels, thick-walled mud jhopas, and underground rainwater tankas. Along the coastal seashores of Odisha, ocean tides, saline breezes, and marine ecosystems inspire artisanal fishing, olive ridley conservation, wooden chariot craftsmanship, and resilient cyclone shelter networks. High in the Himalayan mountains of Sikkim, steep rocky ridges, alpine chill, and rapid rivers lead to terrace farming, insulating woollen bakhus, hardy domestic yaks, and sloping-roof wooden homes. Despite their contrasting landscapes, every regional community demonstrates ingenuity, resourcefulness, and sustainable living practices. By appreciating how geography shapes diverse human lives across India, we learn to cherish our nation's incredible diversity, protect fragile ecosystems, and build resilient, sustainable, and thriving communities everywhere across our magnificent land.",
        "checkpoints": [
            {
                "q": "What fundamental scientific truth is revealed by comparing life across plains, deserts, coasts, and mountains?",
                "options": ["Human cultures, diets, and shelters adapt directly to their physical environments", "All regions across the entire planet have exactly identical climates and soil", "Physical geography has zero influence on the survival of living organisms", "People can only survive by building identical concrete high-rises everywhere"],
                "ans": "Human cultures, diets, and shelters adapt directly to their physical environments",
                "explanation": "Living organisms and human societies develop specialized physiological and cultural adaptations finely tuned to their local physical geography and climate."
            },
            {
                "q": "Which pair correctly matches a regional landform with its sustainable traditional water adaptation?",
                "options": ["Desert with underground rainwater harvesting tankas", "High mountains with ocean wave tidal power generators", "Coastal beach with high-altitude yak milk storage cellars", "Agricultural plains with deep snow melting solar boilers"],
                "ans": "Desert with underground rainwater harvesting tankas",
                "explanation": "In arid desert landscapes, underground tankas harvest and preserve precious rainwater, preventing evaporation and contamination throughout dry months."
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

print("=== CHECKING SLIDES 9 TO 16 ===")
for s in slides_part2:
    sid = s['id']
    title = s['title']
    wc = len(s['speech'].split())
    print(f"Slide {sid} '{title}': {wc} words")

for s in slides_part2:
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

print("Slides 9 to 16 verified successfully!")

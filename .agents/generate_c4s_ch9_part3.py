# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 for Class 4 Science Chapter 9: Different Lands, Different Lives.
4 Mastery Challenge Slides × 10 Questions each = 40 Questions total.
Each question has id, q, 4 options, ans, hint, explanation, and 3 solution steps.
Zero human character names, zero lecturer personas.
"""

import re
import json

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Plains Mastery",
        "sim_id": "sim_quiz_plains",
        "description": "Mastery challenge testing scientific concepts of river plains, alluvial soil formation, seasonal crops, and community service.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "What type of soil predominantly characterizes the flat northern agricultural river plains?",
                "options": ["Fertile alluvial soil", "Dry coarse desert sand", "Acidic volcanic pumice", "Hard glacial permafrost"],
                "ans": "Fertile alluvial soil",
                "hint": "Think of the mineral-rich silt washed down from the Himalayas by flowing rivers.",
                "explanation": "Alluvial soil is composed of fine mineral-rich silt and clay deposited by perennial river networks, making it exceptionally fertile for agriculture.",
                "solution_steps": [
                    "Step 1: Identify that northern plains were formed by perennial rivers carrying sediment from high mountains.",
                    "Step 2: Recall that river sediment deposits create deep layers of nutrient-rich alluvial soil.",
                    "Step 3: Conclude that fertile alluvial soil is the predominant soil type across agricultural river plains."
                ]
            },
            {
                "id": "c1_q2",
                "q": "Which winter staple grain is widely cultivated across the northern plains during the rabi season?",
                "options": ["Golden wheat", "Tropical coconut", "Wetland mangrove", "Highland tea leaves"],
                "ans": "Golden wheat",
                "hint": "This golden grain is milled into flour to bake everyday chapatis.",
                "explanation": "Wheat is the principal rabi (winter) cereal crop of northern India, thriving in cool temperatures and well-drained alluvial soil.",
                "solution_steps": [
                    "Step 1: Distinguish between winter (rabi) and monsoon (kharif) agricultural seasons.",
                    "Step 2: Identify wheat as the primary cereal crop sown in autumn and harvested in spring.",
                    "Step 3: Confirm that golden wheat is the signature winter staple grain of the northern plains."
                ]
            },
            {
                "id": "c1_q3",
                "q": "What nutritional benefit makes sarson da saag particularly healthy during cold winter months?",
                "options": ["High concentrations of vitamins A, C, iron, and calcium", "Pure sugar crystals that prevent body sweating", "Excess synthetic chemical coloring agents", "High concentrations of salt that dehydrate cells"],
                "ans": "High concentrations of vitamins A, C, iron, and calcium",
                "hint": "Green leafy vegetables are rich in essential vitamins and blood-building iron.",
                "explanation": "Mustard greens are packed with vitamins A, C, K, iron, and dietary fiber, which strengthen immune resistance against seasonal winter infections.",
                "solution_steps": [
                    "Step 1: Analyze the ingredients of sarson da saag, made from fresh tender mustard leaves.",
                    "Step 2: Identify the micronutrients present in leafy green vegetables: vitamins A, C, iron, and calcium.",
                    "Step 3: Conclude that these essential vitamins and minerals provide superior nutritional warmth and immunity."
                ]
            },
            {
                "id": "c1_q4",
                "q": "Why is churned curd lassi an effective digestive beverage when paired with rich winter meals?",
                "options": ["Delivers live probiotic bacteria and easily absorbed protein", "Replaces all stomach acid with pure saltwater", "Freezes digestive enzymes to prevent food absorption", "Eliminates all calcium from the human skeleton"],
                "ans": "Delivers live probiotic bacteria and easily absorbed protein",
                "hint": "Fermented curd provides living beneficial microorganisms that aid digestion.",
                "explanation": "Fermented curd contains millions of beneficial probiotic bacteria (lactobacilli) that aid gut microbiome balance and promote digestion of heavy meals.",
                "solution_steps": [
                    "Step 1: Recognize that lassi is made by churning cultured milk curd.",
                    "Step 2: Recall that fermented dairy contains beneficial probiotic microorganisms and bioavailable protein.",
                    "Step 3: Confirm that probiotics facilitate gut digestion and nutrient absorption."
                ]
            },
            {
                "id": "c1_q5",
                "q": "What is the primary agricultural role of cattle in traditional northern plains ecosystems?",
                "options": ["Providing nutritious milk, draft labor for carts, and organic manure", "Hunting small desert scorpions in sandy dunes", "Carrying heavy packs across snowy high-altitude glaciers", "Filtering saltwater in ocean mangroves"],
                "ans": "Providing nutritious milk, draft labor for carts, and organic manure",
                "hint": "They provide dairy, pull ploughs, and supply manure to replenish the soil.",
                "explanation": "Cattle form a closed-loop farm system by converting crop stalks into dairy protein, farm draft power, and organic manure to fertilize fields.",
                "solution_steps": [
                    "Step 1: Examine the multiple contributions of cows and oxen on smallholder farms.",
                    "Step 2: Note the production of milk for nutrition, physical draft power for ploughing/transport, and dung for soil manure.",
                    "Step 3: Conclude that cattle provide milk, draft labor, and organic manure to maintain soil fertility."
                ]
            },
            {
                "id": "c1_q6",
                "q": "How does the flat, level terrain of the plains benefit transportation and infrastructure?",
                "options": ["Simplifies the construction of straight roads, canals, and railways", "Causes rivers to flow upward into mountain peaks", "Prevents all wheeled vehicles from moving forward", "Requires residents to travel exclusively by suspension bridges"],
                "ans": "Simplifies the construction of straight roads, canals, and railways",
                "hint": "Flat land requires minimal cutting or tunnel excavation compared to mountains.",
                "explanation": "Level topography enables engineers to build expansive networks of roads, railway tracks, and irrigation canals with minimal earthwork.",
                "solution_steps": [
                    "Step 1: Contrast flat plains with rugged hills and steep mountain valleys.",
                    "Step 2: Recognize that level land eliminates the need for expensive tunnels and winding mountain roads.",
                    "Step 3: Confirm that flat terrain greatly simplifies the construction of transport and irrigation infrastructure."
                ]
            },
            {
                "id": "c1_q7",
                "q": "What core social principle is demonstrated by the langar service at Sri Harmandir Sahib?",
                "options": ["Universal human equality and selfless community service", "Segregating people according to wealth and title", "Charging premium commercial prices for banquet dining", "Allowing only royal officials to enter the dining hall"],
                "ans": "Universal human equality and selfless community service",
                "hint": "Everyone sits together on floor mats side by side regardless of background.",
                "explanation": "Langar embodies the foundational value of sewa (selfless service) and pangat (eating together on the floor as equals without social discrimination).",
                "solution_steps": [
                    "Step 1: Observe how hundreds of thousands of guests are served free hot meals daily.",
                    "Step 2: Notice that all visitors sit together on continuous floor mats as equals.",
                    "Step 3: Conclude that the langar demonstrates universal human equality and selfless community service."
                ]
            },
            {
                "id": "c1_q8",
                "q": "How are vegetable wastes and food residues responsibly managed in large community kitchens?",
                "options": ["Composted into nutrient-rich organic manure for farm soil", "Dumped untreated into local drinking water reservoirs", "Burned openly in metal barrels to create thick black smoke", "Sealed permanently inside single-use non-recyclable plastic bags"],
                "ans": "Composted into nutrient-rich organic manure for farm soil",
                "hint": "Organic peelings can break down naturally to nourish plant crops.",
                "explanation": "Organic kitchen scraps are converted via biological composting into rich humus, returning vital nutrients to agricultural soils.",
                "solution_steps": [
                    "Step 1: Identify that vegetable scraps and leftover organic material are biodegradable.",
                    "Step 2: Recall that biological decomposition turns organic waste into nutrient-dense compost.",
                    "Step 3: Confirm that composting returns nutrients to farm soil sustainably."
                ]
            },
            {
                "id": "c1_q9",
                "q": "What agricultural tool has largely augmented traditional draft cattle in modern plains farming?",
                "options": ["Motorized farm tractors", "Wooden dog sledges", "Ocean fishing trawlers", "High-altitude hot air balloons"],
                "ans": "Motorized farm tractors",
                "hint": "These powerful wheeled farm machines pull multi-blade ploughs across wide acres.",
                "explanation": "Motorized tractors increase agricultural productivity by rapidly ploughing, harrowing, and harvesting extensive flat fields.",
                "solution_steps": [
                    "Step 1: Consider how modern mechanization speeds up farming operations across expansive plains.",
                    "Step 2: Identify diesel-powered tractors as the ubiquitous machine in northern plains fields.",
                    "Step 3: Conclude that motorized farm tractors have augmented traditional draft animals."
                ]
            },
            {
                "id": "c1_q10",
                "q": "Which yellow-flowering crop is commonly grown alongside wheat in the northern winter plains?",
                "options": ["Mustard crop", "Red sea kelp", "Highland fir tree", "Desert prickly pear"],
                "ans": "Mustard crop",
                "hint": "Its bright yellow blooms blanket fields and its seeds yield pungent cooking oil.",
                "explanation": "Mustard is an essential winter rabi oilseed crop cultivated widely across northern plains, recognized by its radiant yellow flowers.",
                "solution_steps": [
                    "Step 1: Recall the vibrant yellow blankets seen across northern agricultural fields in winter.",
                    "Step 2: Identify the plant as mustard (sarson), valued for both edible leaves and cooking oil seeds.",
                    "Step 3: Confirm that the mustard crop is grown alongside winter wheat."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Desert Mastery",
        "sim_id": "sim_quiz_desert",
        "description": "Mastery challenge testing xerophytic plant adaptations, camel biology, traditional tanka engineering, and passive architecture.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "What physiological adaptation allows the camel to walk easily over soft shifting sand without sinking?",
                "options": ["Wide, cushioned foot pads that distribute body weight", "Sharp iron claws that dig deep trenches", "Webbed duck-like feet for swimming", "Narrow metal-tipped pointed hooves"],
                "ans": "Wide, cushioned foot pads that distribute body weight",
                "hint": "Broad feet spread weight over a large area, lowering ground pressure.",
                "explanation": "Camels have broad, two-toed feet connected by a tough fibrous pad that spreads body weight over a large surface area to prevent sinking in sand.",
                "solution_steps": [
                    "Step 1: Understand the physical relationship between contact surface area and pressure (Pressure = Force / Area).",
                    "Step 2: Recognize that wider foot pads decrease pressure exerted on loose sand grains.",
                    "Step 3: Confirm that broad cushioned pads prevent the camel from sinking into dunes."
                ]
            },
            {
                "id": "c2_q2",
                "q": "Why do desert plants like cacti possess sharp spines instead of wide leafy surfaces?",
                "options": ["Minimize transpiration water loss and deter grazing herbivores", "Absorb large volumes of liquid rain directly from clouds", "Trap flying birds to absorb their body heat", "Cast dark shadows to freeze the ground at noon"],
                "ans": "Minimize transpiration water loss and deter grazing herbivores",
                "hint": "Broad leaves lose moisture rapidly through stomatal pores during hot days.",
                "explanation": "Modified leaves (spines) have minimal surface area, drastically reducing water vapour loss while physically protecting stored water from thirsty animals.",
                "solution_steps": [
                    "Step 1: Recall that plants lose water through microscopic leaf pores via transpiration.",
                    "Step 2: Understand that reducing leaf area to sharp needles minimizes evaporative surface area.",
                    "Step 3: Conclude that spines conserve scarce moisture and deter hungry herbivores."
                ]
            },
            {
                "id": "c2_q3",
                "q": "What is the primary function of the camel's dorsal hump?",
                "options": ["Storing fatty tissue that converts into energy and metabolic water", "Storing hundreds of litres of liquid water like an internal bucket", "Cooling the camel's brain using mechanical fan blades", "Carrying baby camels safe from desert eagles"],
                "ans": "Storing fatty tissue that converts into energy and metabolic water",
                "hint": "The hump is composed of dense adipose lipid tissue rather than a hollow water tank.",
                "explanation": "The camel's hump stores fat, which can be metabolized for nutrition during food scarcity, releasing metabolic water during biochemical respiration.",
                "solution_steps": [
                    "Step 1: Clarify the common scientific misconception that the hump stores liquid drinking water.",
                    "Step 2: Note that the hump is composed of concentrated fat reserves.",
                    "Step 3: Conclude that this fat reserves energy and releases metabolic water during breakdown."
                ]
            },
            {
                "id": "c2_q4",
                "q": "How does the deep root system of the desert khejri tree help it survive extreme droughts?",
                "options": ["Taps deep subterranean water tables dozens of metres below ground", "Absorbs salty seawater directly from underground oceans", "Freezes underground rocks into solid ice cubes", "Anchors floating sand dunes so they cannot blow away"],
                "ans": "Taps deep subterranean water tables dozens of metres below ground",
                "hint": "Its primary taproot extends straight downward to seek hidden moisture.",
                "explanation": "The khejri tree develops deep vertical taproots reaching up to thirty metres deep, accessing permanent subterranean groundwater during dry spells.",
                "solution_steps": [
                    "Step 1: Consider how desert surface sand becomes completely parched under hot sun.",
                    "Step 2: Recognize that deep underground rock strata may still hold moisture.",
                    "Step 3: Confirm that deep taproots access subterranean water tables to sustain the khejri tree."
                ]
            },
            {
                "id": "c2_q5",
                "q": "Why are traditional desert houses built with very thick earthen mud walls?",
                "options": ["Provide high thermal mass that resists daytime heat and stores night warmth", "Allow rain moisture to dissolve the walls every month", "Make the home as light as a camping tent to move easily", "Trap cold winter frost permanently inside bedrooms"],
                "ans": "Provide high thermal mass that resists daytime heat and stores night warmth",
                "hint": "Dense earthen materials conduct thermal heat very slowly.",
                "explanation": "Thick earthen walls have high thermal inertia; they absorb daytime heat slowly, keeping interiors cool at midday, and release warmth at night.",
                "solution_steps": [
                    "Step 1: Identify that desert climates experience extreme daytime heat and rapid nighttime cooling.",
                    "Step 2: Understand that thick clay walls have high thermal mass, delaying heat transfer by several hours.",
                    "Step 3: Conclude that thick earthen walls moderate indoor temperatures sustainably without electricity."
                ]
            },
            {
                "id": "c2_q6",
                "q": "What is the primary purpose of an underground desert tanka?",
                "options": ["Harvest and preserve filtered rainwater safe from evaporation", "Store heavy diesel fuel for motorized farm tractors", "Keep pet camels inside during desert dust storms", "Cool high-altitude yak cheese under river currents"],
                "ans": "Harvest and preserve filtered rainwater safe from evaporation",
                "hint": "It is a covered masonry cistern catching runoff from courtyards.",
                "explanation": "A tanka collects rainwater from clean paved catchments, filtering and storing it underground where sun cannot evaporate it and microbes cannot breed.",
                "solution_steps": [
                    "Step 1: Identify water scarcity as the most acute challenge in arid desert environments.",
                    "Step 2: Understand that open surface ponds lose water rapidly to solar evaporation.",
                    "Step 3: Conclude that underground sealed tankas store and protect rainwater from evaporation."
                ]
            },
            {
                "id": "c2_q7",
                "q": "How do narrow winding alleys inside Jaisalmer Fort keep pedestrians cool?",
                "options": ["Tall stone facades shade walkways from direct solar radiation", "Giant mechanical ceiling fans blow artificial cold air", "Pipes spray ocean saltwater continuously onto the cobblestones", "Thick trees grow across the alleys, blocking all light"],
                "ans": "Tall stone facades shade walkways from direct solar radiation",
                "hint": "High walls block the sun from reaching the ground for most of the day.",
                "explanation": "Narrow street geometry ensures that adjacent multi-story stone buildings cast continuous shadows over walkways, preventing pavement solar heating.",
                "solution_steps": [
                    "Step 1: Observe the tight urban layout of ancient desert fortress streets.",
                    "Step 2: Recognize that high building facades block direct midday solar rays from heating the ground.",
                    "Step 3: Confirm that shading from tall stone walls keeps walkways pleasantly cool."
                ]
            },
            {
                "id": "c2_q8",
                "q": "What physical principle allows stone jali screens to accelerate and cool passing breezes?",
                "options": ["The Venturi effect compressing air through small apertures", "Centrifugal magnetic separation of warm and cold atoms", "Chemical combustion of nitrogen gas in the screen pores", "Direct solar evaporation of liquid stone"],
                "ans": "The Venturi effect compressing air through small apertures",
                "hint": "Forcing air through narrow openings increases air speed and drops temperature.",
                "explanation": "Perforated stone jalis act as constrictions: when ambient air is squeezed through small openings, its velocity increases, creating a cooling draft.",
                "solution_steps": [
                    "Step 1: Examine the intricate lattice holes cut into sandstone jali screens.",
                    "Step 2: Apply fluid dynamics: fluid velocity increases when passing through a restricted opening (Venturi effect).",
                    "Step 3: Confirm that the Venturi effect accelerates and cools breezes entering living spaces."
                ]
            },
            {
                "id": "c2_q9",
                "q": "Why do desert dwellers traditionally wear long, multi-layered cotton turbans (pagris)?",
                "options": ["Insulate the head against solar heat and protect from sandstorms", "Attract rainfall clouds directly overhead during summer", "Act as heavy diving helmets for swimming underwater", "Weigh down the body so desert winds cannot blow a person away"],
                "ans": "Insulate the head against solar heat and protect from sandstorms",
                "hint": "Layers of natural cotton create an air cushion over the crown of the head.",
                "explanation": "The multi-fold cotton turban traps insulating air pockets, shielding the head from dangerous solar heat while offering fabric to cover the mouth during dust storms.",
                "solution_steps": [
                    "Step 1: Consider the extreme danger of heatstroke and sun exposure in open deserts.",
                    "Step 2: Note that cotton folds provide thermal insulation and can be unwrapped to shield the face from blowing sand.",
                    "Step 3: Conclude that turbans insulate against solar heat and filter sandstorm dust."
                ]
            },
            {
                "id": "c2_q10",
                "q": "Which drought-resistant desert bean and wild berry are combined in a classic nutritious desert dish?",
                "options": ["Ker sangri", "Sarson da saag", "Thukpa noodles", "Coconut fish curry"],
                "ans": "Ker sangri",
                "hint": "These wild desert berries and dried bean pods are harvested directly from thorny trees.",
                "explanation": "Ker (wild caper berries) and sangri (pods of the khejri tree) are protein-rich wild desert crops preserved dry and prepared as a nutritious delicacy.",
                "solution_steps": [
                    "Step 1: Identify native vegetation adapted to survive in the arid Thar desert.",
                    "Step 2: Recognize ker berries from thorny shrubs and sangri bean pods from khejri trees.",
                    "Step 3: Confirm that ker sangri is the classic traditional desert delicacy."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Coastal Mastery",
        "sim_id": "sim_quiz_coastal",
        "description": "Mastery challenge testing coastal ecosystems, marine nesting behaviors, storm surge physics, and early disaster preparedness.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "What natural seasonal event brings hundreds of thousands of olive ridley sea turtles to Odisha beaches?",
                "options": ["Mass synchronized nesting (arribada)", "Hibernation inside deep sea trenches", "Annual molting of their outer bone carapace", "Building permanent wooden nests in coconut trees"],
                "ans": "Mass synchronized nesting (arribada)",
                "hint": "The Spanish term for this synchronized mass arrival on sandy shores.",
                "explanation": "Olive ridley turtles exhibit arribada, where thousands of breeding females crawl ashore simultaneously to lay eggs in flask-shaped sandy pits.",
                "solution_steps": [
                    "Step 1: Recall the unique reproductive behavior of olive ridley sea turtles.",
                    "Step 2: Identify arribada as the synchronized mass arrival of egg-laying sea turtles on shores.",
                    "Step 3: Confirm that mass synchronized nesting (arribada) brings turtles to Odisha's beaches."
                ]
            },
            {
                "id": "c3_q2",
                "q": "How does beach sand temperature determine the incubation of sea turtle eggs?",
                "options": ["Warm sand incubates eggs until hatchlings emerge naturally", "Freezes eggs so they turn into marine seashells", "Dissolves the eggshell instantly with concentrated acid", "Prevents baby turtles from developing any flippers"],
                "ans": "Warm sand incubates eggs until hatchlings emerge naturally",
                "hint": "Solar heat absorbed by moist sand provides incubation warmth for reptilian development.",
                "explanation": "The warm thermal mass of tropical beach sand incubates buried eggs over approximately seven weeks until baby turtles hatch and emerge.",
                "solution_steps": [
                    "Step 1: Recognize that reptiles are cold-blooded animals relying on environmental heat for incubation.",
                    "Step 2: Understand that mother turtles bury eggs deep in warm, aerated beach sand.",
                    "Step 3: Confirm that solar warmth in beach sand incubates eggs until hatchlings emerge."
                ]
            },
            {
                "id": "c3_q3",
                "q": "Why must artificial lights along nesting beaches be switched off during turtle hatching seasons?",
                "options": ["Artificial lights mislead emerging hatchlings away from the sea", "Bright lights cause sand dunes to melt into seawater", "Lighting makes ocean waves stop rolling toward the shore", "Lights attract cold snowstorms onto tropical beaches"],
                "ans": "Artificial lights mislead emerging hatchlings away from the sea",
                "hint": "Hatchlings navigate toward the naturally bright horizon of moonlight reflected on waves.",
                "explanation": "Hatchlings instinctively orient toward the brightest natural horizon (the ocean reflecting starlight); artificial shore lighting misguides them toward fatal hazards.",
                "solution_steps": [
                    "Step 1: Examine how newly hatched sea turtles find their way to open water at night.",
                    "Step 2: Understand that hatchlings follow the brighter horizon of moonlight over the sea.",
                    "Step 3: Conclude that artificial lights disorient hatchlings, drawing them toward inland dangers."
                ]
            },
            {
                "id": "c3_q4",
                "q": "What primary ecological service is performed by coastal coconut and palmyra palm trees?",
                "options": ["Stabilizing loose sand dunes and shielding coastlines from erosion", "Filtering all salt out of the entire ocean basin", "Generating hurricane winds through leaf vibration", "Turning moist sand dunes into volcanic rock"],
                "ans": "Stabilizing loose sand dunes and shielding coastlines from erosion",
                "hint": "Their extensive web of fibrous roots holds sand grains together against waves.",
                "explanation": "Dense, fibrous palm root networks bind shoreline sediment, mitigating coastal erosion caused by storm surges, tides, and ocean winds.",
                "solution_steps": [
                    "Step 1: Analyze the root architecture of coastal palms growing along sandy shores.",
                    "Step 2: Recognize that their dense root mats trap sand particles against wind and wave action.",
                    "Step 3: Confirm that palms stabilize dunes and protect coastlines from erosion."
                ]
            },
            {
                "id": "c3_q5",
                "q": "What natural atmospheric hazard forms over the warm waters of the Bay of Bengal during transition seasons?",
                "options": ["Severe tropical cyclones with storm surges", "Volcanic lava eruptions on sandy beaches", "Dry sand blizzards freezing palm trees", "Subterranean magma geysers flooding villages"],
                "ans": "Severe tropical cyclones with storm surges",
                "hint": "These spiral storms bring torrential rains and high-speed gale winds.",
                "explanation": "Warm sea surface temperatures (>26.5°C) fuel intense rotating low-pressure systems, causing tropical cyclones with ferocious winds and coastal surges.",
                "solution_steps": [
                    "Step 1: Identify the geographical vulnerability of the Bay of Bengal coastline.",
                    "Step 2: Recognize that warm sea temperatures evaporate moisture into powerful rotating cyclonic storms.",
                    "Step 3: Conclude that severe tropical cyclones with storm surges form over these waters."
                ]
            },
            {
                "id": "c3_q6",
                "q": "What modern scientific instrument allows meteorologists to track cyclone paths 48 hours before landfall?",
                "options": ["Doppler weather radar and satellite imagery", "Underwater acoustic bells and fishing lures", "Handheld magnifying glasses and mercury thermometers", "Acoustic wooden flutes played on the beach"],
                "ans": "Doppler weather radar and satellite imagery",
                "hint": "Orbital satellites and coastal radar systems track cloud swirl and wind speed.",
                "explanation": "Doppler radar measures cloud precipitation reflectivity and wind speed, while weather satellites track storm coordinates in real time.",
                "solution_steps": [
                    "Step 1: Consider how meteorologists observe storms hundreds of kilometres offshore.",
                    "Step 2: Identify orbital weather satellites and coastal Doppler radar systems as key detection tools.",
                    "Step 3: Confirm that Doppler radar and satellites provide accurate 48-hour landfall forecasting."
                ]
            },
            {
                "id": "c3_q7",
                "q": "How do elevated multi-purpose cyclone shelters protect coastal populations during extreme storm surges?",
                "options": ["Raised on reinforced concrete pillars above sea inundation levels", "Float like giant cruise ships out into open ocean trenches", "Bury the community in deep underground coal mines", "Provide wooden stilts for each family to walk on the water"],
                "ans": "Raised on reinforced concrete pillars above sea inundation levels",
                "hint": "Sturdy elevated concrete structures remain dry even when surge water covers the ground.",
                "explanation": "Cyclone shelters are constructed on high concrete stilts above predicted maximum surge heights, with reinforced walls withstanding severe gale winds.",
                "solution_steps": [
                    "Step 1: Understand that storm surges can push sea waters several metres deep over coastal land.",
                    "Step 2: Recognize that building shelters on elevated concrete pillars keeps interior living spaces above floodwaters.",
                    "Step 3: Conclude that elevated shelters protect people and livestock from deadly seawater inundation."
                ]
            },
            {
                "id": "c3_q8",
                "q": "What is unique about the construction of the three giant sacred chariots for the Puri Rath Yatra?",
                "options": ["Constructed anew each year from timber using interlocking joinery without iron nails", "Welded permanently from stainless steel sheets and powered by batteries", "Assembled from synthetic plastic bricks and fiberglass panels", "Forged from cast iron and left anchored in the sea permanently"],
                "ans": "Constructed anew each year from timber using interlocking joinery without iron nails",
                "hint": "Master carpenters use traditional wooden dowels and seasoned timber every summer.",
                "explanation": "The chariots are crafted each year from designated tree species using intricate mortise and tenon wooden joinery without metal fasteners.",
                "solution_steps": [
                    "Step 1: Examine the centuries-old artisanal traditions of the Puri Rath Yatra festival.",
                    "Step 2: Note that hereditary carpenters assemble the 45-foot chariots each year from timber without metal nails.",
                    "Step 3: Confirm that the chariots are rebuilt annually using traditional wooden joinery."
                ]
            },
            {
                "id": "c3_q9",
                "q": "Which marine mammal species is known to inhabit coastal bays and lagoons along the Odisha coast?",
                "options": ["Dolphins", "Polar bears", "Mountain yaks", "Desert camels"],
                "ans": "Dolphins",
                "hint": "These intelligent aquatic mammals use echolocation clicks to hunt in schools.",
                "explanation": "Irrawaddy dolphins and coastal bottlenose dolphins inhabit protected estuarine lagoons and coastal bays, such as Chilika Lagoon in Odisha.",
                "solution_steps": [
                    "Step 1: Identify animals adapted to marine and brackish coastal waters.",
                    "Step 2: Recognize dolphins as the famous aquatic mammals leaping in coastal bays.",
                    "Step 3: Confirm that dolphins are native marine mammals of the Odisha coast."
                ]
            },
            {
                "id": "c3_q10",
                "q": "What primary economic livelihood supports the majority of coastal village families along the seashore?",
                "options": ["Artisanal fishing and seafood harvesting", "Highland yak herding across snowy passes", "Desert camel breeding and wool weaving", "Underground coal mining and gold panning"],
                "ans": "Artisanal fishing and seafood harvesting",
                "hint": "Villagers launch wooden catamarans and cast nets into the morning surf.",
                "explanation": "Marine fishing, catching fish, prawns, and crabs using traditional nets and coastal boats, is the primary economic livelihood of coastal communities.",
                "solution_steps": [
                    "Step 1: Connect the geographical resource of the ocean with local human occupations.",
                    "Step 2: Identify harvesting fish and shellfish from the sea as the principal coastal trade.",
                    "Step 3: Conclude that artisanal fishing is the primary economic livelihood along the coast."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Mountain Mastery",
        "sim_id": "sim_quiz_mountain",
        "description": "Mastery challenge testing Himalayan geology, alpine climate adaptations, terrace farming, and highland culture.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "Which magnificent Himalayan mountain peak rises to 8,586 metres in Sikkim as the third highest mountain on Earth?",
                "options": ["Mount Kangchenjunga", "Mount Everest", "Mount Blanc", "Mount Vesuvius"],
                "ans": "Mount Kangchenjunga",
                "hint": "Its name translates to 'The Five Treasures of Snow' and it dominates Sikkim's skyline.",
                "explanation": "Mount Kangchenjunga (8,586 m) lies on the boundary between Sikkim and Nepal, revered as sacred by the Sikkimese people.",
                "solution_steps": [
                    "Step 1: Identify the geographical setting of Sikkim in the eastern Himalayas.",
                    "Step 2: Recall that Kangchenjunga is the third highest peak on Earth and the crowning summit of Sikkim.",
                    "Step 3: Confirm that Mount Kangchenjunga is the third highest mountain peak."
                ]
            },
            {
                "id": "c4_q2",
                "q": "Why do mountain farmers construct stepped terrace benches along steep hillside slopes?",
                "options": ["Create level cultivable soil and prevent rapid rainfall runoff from washing away topsoil", "Provide straight running tracks for mountain sheep races", "Encourage deep mud landslides to slide down into river valleys", "Block cold winter winds from blowing into high cloud layers"],
                "ans": "Create level cultivable soil and prevent rapid rainfall runoff from washing away topsoil",
                "hint": "Flat steps slow down rushing rainwater and prevent soil erosion.",
                "explanation": "Terracing carves stepped flat fields into steep terrain, allowing crop cultivation while slowing rainwater runoff to prevent soil erosion.",
                "solution_steps": [
                    "Step 1: Understand that steep hillsides allow rainfall to wash away fertile topsoil rapidly.",
                    "Step 2: Recognize that cutting stepped flat terraces creates manageable farming surfaces and slows runoff.",
                    "Step 3: Conclude that terrace benches create level farmland and protect against topsoil erosion."
                ]
            },
            {
                "id": "c4_q3",
                "q": "What physical adaptation enables domestic yaks to thrive in freezing high-altitude mountain environments?",
                "options": ["Dense double-layered wool coats, broad gripping hooves, and high-efficiency lungs", "Thin bare skin that absorbs intense solar heat directly", "Webbed aquatic flippers for swimming through glacial lakes", "Spiny needles that store water inside green body trunks"],
                "ans": "Dense double-layered wool coats, broad gripping hooves, and high-efficiency lungs",
                "hint": "They have thick shaggy coats and specialized lungs adapted for thin, low-oxygen air.",
                "explanation": "Yaks have a dense undercoat of fine wool beneath coarse outer hair, large hearts and lungs adapted for low oxygen, and hooves adapted for rocky ridges.",
                "solution_steps": [
                    "Step 1: Consider the harsh conditions of high altitudes: freezing cold, rocky cliffs, and thin oxygen.",
                    "Step 2: Note the yak's thick wool insulation, large lungs for oxygen uptake, and sure-footed hooves.",
                    "Step 3: Confirm that thick double-layer wool, gripping hooves, and high-efficiency lungs enable yak survival."
                ]
            },
            {
                "id": "c4_q4",
                "q": "What is the traditional full-length wrap-around woollen dress worn by communities in Sikkim?",
                "options": ["Bakhu", "Sari", "Kimono", "Sherwani"],
                "ans": "Bakhu",
                "hint": "It is worn tied at the waist with a broad sash over an inner blouse called a honju.",
                "explanation": "The bakhu (or kho) is the traditional wrap-around dress worn by the Bhutia and Lepcha communities, providing superior insulation against mountain cold.",
                "solution_steps": [
                    "Step 1: Recall the traditional cultural attire of Sikkim.",
                    "Step 2: Identify the bakhu as the heavy woollen wrap-around garment tied with a belt.",
                    "Step 3: Confirm that the bakhu is the traditional Sikkimese dress."
                ]
            },
            {
                "id": "c4_q5",
                "q": "Why do traditional mountain houses feature steeply pitched, sloping roofs?",
                "options": ["Allow heavy monsoon rainwater and thick snow to shed quickly without overloading the roof", "Provide an aerodynamic launch ramp for flying mountain gliders", "Trap fallen autumn leaves permanently on top of the house", "Ensure that birds cannot land on the building at any time"],
                "ans": "Allow heavy monsoon rainwater and thick snow to shed quickly without overloading the roof",
                "hint": "Sloped surfaces prevent heavy snow and water from accumulating and collapsing the ceiling.",
                "explanation": "Pitched roofs shed rain and snow rapidly under gravity, preventing structural water leaks and heavy snow loads that could collapse flat roofs.",
                "solution_steps": [
                    "Step 1: Identify that high mountain zones experience torrential monsoon rains and heavy winter snowfalls.",
                    "Step 2: Recognize that flat roofs would accumulate tremendous snow weight, risking structural collapse.",
                    "Step 3: Conclude that steeply pitched roofs shed rain and snow rapidly to maintain structural safety."
                ]
            },
            {
                "id": "c4_q6",
                "q": "What popular Tibetan noodle soup is widely consumed in cold mountain regions to generate metabolic warmth?",
                "options": ["Thukpa", "Lassi", "Ker sangri", "Dhokla"],
                "ans": "Thukpa",
                "hint": "A hot, steaming bowl of noodles served with seasonal greens and warming spices.",
                "explanation": "Thukpa is a hearty, piping-hot noodle soup enriched with vegetables and spices, perfectly designed to restore body heat in chilly mountain climates.",
                "solution_steps": [
                    "Step 1: Identify traditional culinary adaptations in cold Himalayan mountain areas.",
                    "Step 2: Distinguish thukpa (hot noodle soup) from plains lassi and desert ker sangri.",
                    "Step 3: Confirm that thukpa is the warming noodle soup of high mountain regions."
                ]
            },
            {
                "id": "c4_q7",
                "q": "Which sacred masked dance is performed by Buddhist monks during Sikkim's Loosong festival?",
                "options": ["Chaam dance", "Kathak", "Bhangra", "Garba"],
                "ans": "Chaam dance",
                "hint": "Monks wear carved wooden masks of deities and spin to long copper horn music.",
                "explanation": "The chaam is a sacred ritual dance performed by lamas in Buddhist monasteries, depicting moral tales and the victory of wisdom over negativity.",
                "solution_steps": [
                    "Step 1: Recall the harvest and new year celebrations in Sikkim (Loosong and Namsoong).",
                    "Step 2: Identify the monastic masked dance performed in monastery courtyards.",
                    "Step 3: Confirm that the chaam dance is the traditional sacred masked dance."
                ]
            },
            {
                "id": "c4_q8",
                "q": "What environmental hazard commonly affects steep mountain slopes during heavy monsoon rains?",
                "options": ["Landslides and debris flows down saturated slopes", "Severe sand dust storms burying village houses", "High ocean storm surges flooding mountain peaks", "Volcanic lava rivers emerging from frozen snow"],
                "ans": "Landslides and debris flows down saturated slopes",
                "hint": "Rainwater saturates soil on steep slopes, causing mud and rock to slide downhill.",
                "explanation": "Heavy rainfall saturates loose hillside topsoil, increasing weight while reducing friction, triggering catastrophic gravity-driven landslides.",
                "solution_steps": [
                    "Step 1: Consider the physical forces acting on steep, water-saturated mountain slopes.",
                    "Step 2: Understand that water saturation weakens soil cohesion and triggers rapid downhill sliding.",
                    "Step 3: Conclude that landslides and debris flows are common hazards during monsoon rains."
                ]
            },
            {
                "id": "c4_q9",
                "q": "Which valuable spice crop is widely cultivated in shaded mountain hillside groves across Sikkim?",
                "options": ["Large black cardamom", "Saltwater kelp seaweed", "Desert babool thorn", "Lowland sugarcane"],
                "ans": "Large black cardamom",
                "hint": "Sikkim produces a major share of India's aromatic large black cardamom.",
                "explanation": "Sikkim is renowned as the primary producer of large black cardamom (badi elaichi), which thrives in moist, shaded mountain hillside microclimates.",
                "solution_steps": [
                    "Step 1: Identify specialized cash crops suited to moist, cool Himalayan hillside elevations.",
                    "Step 2: Recognize large black cardamom as the signature aromatic spice grown in Sikkim's agro-forestry systems.",
                    "Step 3: Confirm that large black cardamom is cultivated across shaded mountain hillsides."
                ]
            },
            {
                "id": "c4_q10",
                "q": "What overarching scientific lesson is learned by comparing life across all four Indian landforms?",
                "options": ["Human shelters, clothing, agriculture, and cultures adapt sustainably to local geography", "All humans should wear heavy woollen bakhus regardless of climate", "Every landform has identical physical features, weather, and animal life", "Only desert regions can support human communities comfortably"],
                "ans": "Human shelters, clothing, agriculture, and cultures adapt sustainably to local geography",
                "hint": "From plains to deserts, coasts, and mountains, people live in harmony with their surroundings.",
                "explanation": "Human ingenuity and ecological sustainability emerge from adapting shelters, diets, clothing, and water systems directly to local geographical conditions.",
                "solution_steps": [
                    "Step 1: Review the key findings across plains (alluvial/agriculture), deserts (xerophytes/tankas), coasts (fishing/cyclone shelters), and mountains (terraces/bakhus).",
                    "Step 2: Observe that in every region, humans develop specialized sustainable systems aligned with nature.",
                    "Step 3: Conclude that human lifestyles and shelters adapt sustainably to their local physical geography."
                ]
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

print("=== CHECKING SLIDES 17 TO 20 ===")
assert len(slides_part3) == 4, f"Expected 4 slides, got {len(slides_part3)}"

for s in slides_part3:
    sid = s['id']
    title = s['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"
    
    assert len(s['questions']) == 10, f"Slide {sid} must have 10 questions (got {len(s['questions'])})"
    
    s_str = json.dumps(s)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + re.escape(name) + r'\b', s_str, re.IGNORECASE), f"Slide {sid} contains name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
        
    for q in s['questions']:
        qid = q['id']
        assert len(q['options']) == 4, f"Question {qid} must have 4 options"
        assert q['ans'] in q['options'], f"Question {qid} ans '{q['ans']}' not in options"
        assert len(q['hint']) > 5, f"Question {qid} hint too short"
        assert len(q['explanation']) > 15, f"Question {qid} explanation too short"
        assert len(q['solution_steps']) == 3, f"Question {qid} must have 3 solution steps (got {len(q['solution_steps'])})"

print("Slides 17 to 20 verified successfully!")

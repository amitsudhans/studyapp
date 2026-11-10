# generate_c4s_ch6_part3.py
# Generates Slides 17-20 for Class 4 Science Chapter 6: Happy and Healthy Living
# 4 Challenges x 10 questions each = 40 comprehensive quiz questions

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Grand Challenge I",
        "description": "Mastery challenge on the farm-to-plate journey, ecological and human contributors, grain storage, and gratitude festivals.",
        "sim_id": "sim-17",
        "sim_title": "Interactive Mastery Assessment",
        "speech": "",
        "questions": [
            {
                "id": "c1_q1",
                "q": "What is the very first step in the journey of food grains before seeds can be sown?",
                "options": [
                    "Ploughing and aerating the soil to prepare the field bed",
                    "Harvesting mature golden stalks with sickles",
                    "Packaging grains into jute sacks for supermarket delivery",
                    "Cooking chapatis on an iron tawa over a gas stove"
                ],
                "ans": "Ploughing and aerating the soil to prepare the field bed",
                "hint": "Think about loosening the soil so tender seeds receive air and moisture.",
                "explanation": "Ploughing loosens the earth, creating loose soil channels that let seeds breathe and extend root systems.",
                "solution_steps": {
                    "step1": "Identify the initial agricultural action taken by farmers on raw soil.",
                    "step2": "Recognize that unploughed soil is too hard and compact for delicate roots to penetrate.",
                    "step3": "Conclude that ploughing and aerating the seedbed precedes sowing, irrigation, and harvesting."
                }
            },
            {
                "id": "c1_q2",
                "q": "Why are earthworms scientifically honored as the best natural friends of farmers?",
                "options": [
                    "They burrow underground, loosening soil and enriching it with nutrient-rich castings",
                    "They eat up all the ripe wheat crops at night",
                    "They frighten away birds by making loud buzzing noises",
                    "They produce synthetic chemical fertilizers inside their bodies"
                ],
                "ans": "They burrow underground, loosening soil and enriching it with nutrient-rich castings",
                "hint": "Consider how underground burrowing aerates soil and creates natural compost.",
                "explanation": "Earthworms aerate the soil by burrowing and leave behind castings that act as organic, fertile vermicompost.",
                "solution_steps": {
                    "step1": "Recall the ecological role of soil organisms in organic agriculture.",
                    "step2": "Observe that earthworms digest decomposing organic matter and burrow deep channels.",
                    "step3": "Conclude that their burrows aerate roots and their castings provide rich natural nourishment."
                }
            },
            {
                "id": "c1_q3",
                "q": "Which abiotic natural factors are indispensable for crop plants to manufacture food via photosynthesis?",
                "options": [
                    "Sunlight, carbon dioxide, fertile soil, and freshwater",
                    "Plastic mulch, neon streetlights, and petrol fumes",
                    "Artificial refrigeration and cold air conditioning",
                    "Complete total darkness and dry barren sand"
                ],
                "ans": "Sunlight, carbon dioxide, fertile soil, and freshwater",
                "hint": "Recall the key environmental elements plants absorb to create glucose.",
                "explanation": "Plants require radiant solar energy, carbon dioxide from air, and water plus minerals from fertile soil.",
                "solution_steps": {
                    "step1": "Analyze the essential reactants needed for green plant photosynthesis.",
                    "step2": "Identify radiant sunlight, atmospheric carbon dioxide, moisture, and soil minerals.",
                    "step3": "Select the option that combines these fundamental abiotic ingredients."
                }
            },
            {
                "id": "c1_q4",
                "q": "What agricultural operation separates edible grain kernels from inedible outer chaff?",
                "options": [
                    "Threshing and winnowing",
                    "Deep well digging",
                    "Baking in an electric oven",
                    "Sprinkling powdered sugar"
                ],
                "ans": "Threshing and winnowing",
                "hint": "Think of the process where harvested stalks are beaten or dropped in the breeze.",
                "explanation": "Threshing beats stalks to loosen seeds, and winnowing uses wind currents to blow away lighter husk particles.",
                "solution_steps": {
                    "step1": "Review post-harvest grain processing terminology.",
                    "step2": "Threshing detaches grain kernels from stalks; winnowing blows away light chaff in the wind.",
                    "step3": "Match this combined post-harvest mechanism to threshing and winnowing."
                }
            },
            {
                "id": "c1_q5",
                "q": "Why must harvested grains be thoroughly sun-dried before being sealed in storage bins or granaries?",
                "options": [
                    "To eliminate moisture that promotes fungal mold and bacterial rot",
                    "To make the grains change color from cream to dark purple",
                    "To melt the grains into liquid porridge",
                    "To make the grains lightweight enough to fly away in the air"
                ],
                "ans": "To eliminate moisture that promotes fungal mold and bacterial rot",
                "hint": "Microorganisms like mold and fungus thrive in damp, warm grain silos.",
                "explanation": "Moisture inside stored grains encourages fungal spores and insect pests to multiply, spoiling the harvest.",
                "solution_steps": {
                    "step1": "Determine what triggers grain decay and mold growth in storage.",
                    "step2": "Understand that high internal moisture activates fungi and insect eggs.",
                    "step3": "Conclude that thorough sun-drying dehydrates grains, guaranteeing safe storage for months."
                }
            },
            {
                "id": "c1_q6",
                "q": "What natural insect repellent is traditionally placed inside grain containers in Indian households?",
                "options": [
                    "Dried neem leaves",
                    "Spicy red chili paste",
                    "Slices of sweet ripe mango",
                    "Boiled potato skins"
                ],
                "ans": "Dried neem leaves",
                "hint": "A bitter medicinal tree leaf widely used across India for pest control.",
                "explanation": "Dried neem leaves contain natural bitter compounds like azadirachtin that deter beetles and weevils safely.",
                "solution_steps": {
                    "step1": "Recall traditional eco-friendly food preservation techniques in rural homes.",
                    "step2": "Identify Azadirachta indica (neem) as an aromatic, non-toxic bio-pesticide.",
                    "step3": "Confirm that placing dry neem leaves prevents pest infestation without toxic chemicals."
                }
            },
            {
                "id": "c1_q7",
                "q": "Which traditional harvest festival is celebrated across India in mid-January to honor the winter crop harvest and the Sun God?",
                "options": [
                    "Makar Sankranti",
                    "Earth Day",
                    "World Water Day",
                    "National Sports Day"
                ],
                "ans": "Makar Sankranti",
                "hint": "Celebrated with til-gur laddus, kite flying, and prayers to the Sun.",
                "explanation": "Makar Sankranti marks the sun's transition into Capricorn and celebrates the bountiful winter crop harvest across India.",
                "solution_steps": {
                    "step1": "Identify harvest celebrations that express gratitude to nature in January.",
                    "step2": "Recognize Makar Sankranti (also celebrated as Pongal, Lohri, and Magh Bihu).",
                    "step3": "Select Makar Sankranti as the Pan-Indian harvest celebration honoring the Sun God."
                }
            },
            {
                "id": "c1_q8",
                "q": "Onam is a famous annual harvest festival celebrated with grand feasts and boat races in which Indian state?",
                "options": [
                    "Kerala",
                    "Himachal Pradesh",
                    "Rajasthan",
                    "Goa"
                ],
                "ans": "Kerala",
                "hint": "A coastal state in south-western India famous for backwaters and Onasadya.",
                "explanation": "Onam is Kerala's prime harvest festival, celebrated with the magnificent Onasadya feast served on banana leaves.",
                "solution_steps": {
                    "step1": "Recall geographical locations of prominent regional Indian harvest festivals.",
                    "step2": "Connect Onam, snake boat races (Vallam Kali), and Onasadya to south India.",
                    "step3": "Conclude that Kerala is the home state of the Onam harvest celebration."
                }
            },
            {
                "id": "c1_q9",
                "q": "Which sequence correctly traces a wheat chapati from the initial farm to your kitchen plate?",
                "options": [
                    "Soil preparation -> Sowing -> Harvesting -> Storage -> Transport -> Grinding -> Kneading and Cooking",
                    "Cooking -> Grinding -> Harvesting -> Sowing -> Storage -> Transport",
                    "Transport -> Sowing -> Cooking -> Harvesting -> Ploughing",
                    "Storage -> Cooking -> Sowing -> Harvesting -> Grinding"
                ],
                "ans": "Soil preparation -> Sowing -> Harvesting -> Storage -> Transport -> Grinding -> Kneading and Cooking",
                "hint": "Follow the chronological timeline from the field soil to the kitchen stove.",
                "explanation": "Food flows chronologically from soil tilling and sowing to harvesting, dry storage, transport, milling, and cooking.",
                "solution_steps": {
                    "step1": "Establish the start point in agricultural production (soil preparation and sowing).",
                    "step2": "Trace the intermediary phases: plant growth, harvest, storage, and logistics to retail.",
                    "step3": "Complete with processing: flour milling, dough kneading, and tawa cooking."
                }
            },
            {
                "id": "c1_q10",
                "q": "What ethical virtue is nurtured when students write thank-you notes to farmers, transporters, and school cooks?",
                "options": [
                    "Gratitude and social empathy for all community contributors",
                    "Selfish pride and greed",
                    "Indifference towards agricultural labor",
                    "Belief that food appears magically without effort"
                ],
                "ans": "Gratitude and social empathy for all community contributors",
                "hint": "Expressing sincere thanks helps us appreciate the hard work of others.",
                "explanation": "Acknowledging the toil of all food contributors fosters deep gratitude, humility, and compassionate social empathy.",
                "solution_steps": {
                    "step1": "Reflect on the emotional and moral impact of acknowledging community work.",
                    "step2": "Writing thank-you messages highlights how dependent we are on collective labor.",
                    "step3": "Conclude that this activity cultivates genuine gratitude and social empathy."
                }
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Grand Challenge II",
        "description": "Mastery challenge on mindful eating mechanics, sensory evaluation, saliva digestion enzymes, and food conservation economics.",
        "sim_id": "sim-18",
        "sim_title": "Interactive Mastery Assessment",
        "speech": "",
        "questions": [
            {
                "id": "c2_q1",
                "q": "What is the core practice of 'mindful eating' during meals?",
                "options": [
                    "Eating slowly while engaging all five senses and paying full attention to the food",
                    "Swallowing large food chunks in under two minutes while watching television",
                    "Talking loudly on a mobile phone without looking at the plate",
                    "Reading an action comic book while tossing snacks into the mouth blindly"
                ],
                "ans": "Eating slowly while engaging all five senses and paying full attention to the food",
                "hint": "Mindfulness means focusing your awareness fully on the present experience.",
                "explanation": "Mindful eating means eating deliberately, engaging sight, aroma, texture, and taste while listening to hunger cues.",
                "solution_steps": {
                    "step1": "Define mindful eating as sensory awareness and intentional pacing during meals.",
                    "step2": "Differentiate between distracted eating (screens, rushing) and conscious dining.",
                    "step3": "Select the option emphasizing deliberate sensory engagement and full attention."
                }
            },
            {
                "id": "c2_q2",
                "q": "In the classroom mindful eating exercise with a single peanut, what should be observed before chewing?",
                "options": [
                    "Its ridged surface texture, golden-brown color, and warm earthy aroma",
                    "Its chemical melting point using a Bunsen burner",
                    "Its electrical resistance using a voltmeter",
                    "Its weight in tons using a truck scale"
                ],
                "ans": "Its ridged surface texture, golden-brown color, and warm earthy aroma",
                "hint": "Think of using touch, vision, and smell before placing food inside the mouth.",
                "explanation": "Observing the peanut's outer ridges, natural color, and aroma awakens sensory receptors and salivary glands.",
                "solution_steps": {
                    "step1": "Review the multi-sensory peanut observation protocol.",
                    "step2": "Identify sensory checks: fingertips feel the shell ridges, eyes observe shade, nose smells aroma.",
                    "step3": "Select the option representing tactile, visual, and olfactory observation."
                }
            },
            {
                "id": "c2_q3",
                "q": "Which digestive enzyme present in human saliva breaks down complex starch molecules into simpler sweet sugars?",
                "options": [
                    "Salivary amylase",
                    "Hydrochloric acid",
                    "Bile pigment",
                    "Hemoglobin"
                ],
                "ans": "Salivary amylase",
                "hint": "This enzyme begins chemical carbohydrate breakdown right in the oral cavity.",
                "explanation": "Salivary amylase hydrolyzes complex starch into maltose, making plain bread taste sweet after prolonged chewing.",
                "solution_steps": {
                    "step1": "Recall the biochemical components of human saliva secreted by salivary glands.",
                    "step2": "Identify amylase as the enzyme specifically responsible for carbohydrate digestion.",
                    "step3": "Confirm that salivary amylase converts complex starch into simpler sweet sugars."
                }
            },
            {
                "id": "c2_q4",
                "q": "Why does a piece of dry roti or plain rice begin to taste noticeably sweet after chewing it thirty times?",
                "options": [
                    "Salivary amylase breaks insoluble wheat starch into sweet tasting maltose sugars",
                    "The teeth produce natural cane sugar crystals from enamel",
                    "The tongue secretes powdered artificial sweetener",
                    "Sugar particles fall from the roof of the mouth"
                ],
                "ans": "Salivary amylase breaks insoluble wheat starch into sweet tasting maltose sugars",
                "hint": "Chewing mixes the food thoroughly with saliva containing digestive enzymes.",
                "explanation": "Prolonged chewing allows salivary amylase to break starch chains into sweet tasting disaccharides like maltose.",
                "solution_steps": {
                    "step1": "Understand the chemical transformation occurring during thorough oral mastication.",
                    "step2": "Wheat starch is a tasteless polysaccharide; saliva contains amylase enzymes.",
                    "step3": "Amylase breaks bonds, releasing simpler sweet tasting sugars."
                }
            },
            {
                "id": "c2_q5",
                "q": "How does thorough chewing support the stomach and intestines during digestion?",
                "options": [
                    "It pulverizes food into a smooth paste with high surface area for gastric juices to act efficiently",
                    "It freezes food so the stomach does not overheat",
                    "It turns all swallowed food into heavy solid rocks",
                    "It prevents any nutrients from being absorbed into the blood"
                ],
                "ans": "It pulverizes food into a smooth paste with high surface area for gastric juices to act efficiently",
                "hint": "Smaller food particles have vastly greater contact area for digestive enzymes.",
                "explanation": "Grinding food into microscopic particles allows stomach acids and enzymes to access and digest nutrients easily.",
                "solution_steps": {
                    "step1": "Examine the mechanical benefit of mastication on surface area to volume ratio.",
                    "step2": "Smaller food particles allow gastric secretions to penetrate instantly without strain.",
                    "step3": "Conclude that thorough chewing prevents indigestion and speeds up nutrient absorption."
                }
            },
            {
                "id": "c2_q6",
                "q": "Approximately how long does it take for the stomach to send fullness satiety signals to the human brain?",
                "options": [
                    "About 15 to 20 minutes",
                    "Less than 5 seconds",
                    "Exactly 4 hours",
                    "Fullness signals are never sent to the brain"
                ],
                "ans": "About 15 to 20 minutes",
                "hint": "Eating too rapidly leads to overeating because the brain has not yet registered satiety.",
                "explanation": "Hormones like leptin and stretch receptors take 15 to 20 minutes to inform the brain that the stomach is pleasantly satisfied.",
                "solution_steps": {
                    "step1": "Recall the physiological timeline for gut-brain endocrine communication.",
                    "step2": "Stretch receptors and digestive hormones require 15 to 20 minutes to signal satiety.",
                    "step3": "Slow eating ensures fullness is detected before excess calories are consumed."
                }
            },
            {
                "id": "c2_q7",
                "q": "What hidden environmental resource is squandered whenever edible food is discarded into a trash bin?",
                "options": [
                    "Thousands of liters of freshwater, fertile topsoil nutrients, and fossil fuel transport energy",
                    "Only the decorative paper wrapper",
                    "Nothing of value, since food is infinitely free",
                    "Only atmospheric nitrogen gas"
                ],
                "ans": "Thousands of liters of freshwater, fertile topsoil nutrients, and fossil fuel transport energy",
                "hint": "Consider the invisible water and diesel fuel consumed during cultivation and delivery.",
                "explanation": "Food production consumes enormous virtual water (e.g., 2,500 liters for 1 kg of rice), plus soil nutrients and tractor fuel.",
                "solution_steps": {
                    "step1": "Analyze the concept of embedded virtual resources in food production.",
                    "step2": "Growing grains requires vast groundwater irrigation, diesel fuel, and soil fertility.",
                    "step3": "Throwing away food discards all the natural resources invested in growing it."
                }
            },
            {
                "id": "c2_q8",
                "q": "What sensible eating habit prevents food wastage during school lunch or family meals?",
                "options": [
                    "Taking small portions first and requesting a second helping only if still hungry",
                    "Piling the plate high with mountainous mounds of food that cannot be finished",
                    "Throwing leftover food out of the window to feed pigeons immediately",
                    "Ordering five different meals simultaneously and tasting only one spoon"
                ],
                "ans": "Taking small portions first and requesting a second helping only if still hungry",
                "hint": "Only serve on your plate what your stomach can comfortably digest.",
                "explanation": "Serving modest initial portions guarantees that food remains clean in serving bowls, preventing plate waste.",
                "solution_steps": {
                    "step1": "Identify practical behavioral habits that eliminate plate leftovers.",
                    "step2": "Starting with smaller servings allows second helpings without wasting uneaten food.",
                    "step3": "Select the portion control strategy as the gold standard of mindful conservation."
                }
            },
            {
                "id": "c2_q9",
                "q": "How can families safely utilize clean, untouched dinner leftovers instead of discarding them?",
                "options": [
                    "Refrigerate promptly and creatively transform them into breakfast dishes the next day",
                    "Leave them uncovered in direct sunlight for three days",
                    "Flush them down the bathroom drain",
                    "Bury them under plastic trash bags in the living room"
                ],
                "ans": "Refrigerate promptly and creatively transform them into breakfast dishes the next day",
                "hint": "Leftover chapati can become tasty chapati noodles or poha.",
                "explanation": "Prompt refrigeration keeps food safe; leftovers can be remade into fresh snacks like vegetable cutlets or fried rice.",
                "solution_steps": {
                    "step1": "Evaluate sustainable home food management strategies.",
                    "step2": "Proper cooling halts bacteria; creative recipes turn extra rice or chapatis into tasty breakfast.",
                    "step3": "Conclude that refrigeration and creative repurposing saves food and money."
                }
            },
            {
                "id": "c2_q10",
                "q": "What is the primary scientific purpose of maintaining a weekly Mindful Food Diary?",
                "options": [
                    "To reflect on eating speed, nutrient variety, hunger signals, and zero-waste habits",
                    "To boast to classmates about eating the most chocolate bars",
                    "To draw funny cartoon doodles on expensive paper",
                    "To force children to stop eating all meals permanently"
                ],
                "ans": "To reflect on eating speed, nutrient variety, hunger signals, and zero-waste habits",
                "hint": "A diary helps build self-awareness and track healthy daily routines.",
                "explanation": "A food diary encourages children to track chewing pacing, colorful vegetable intake, water consumption, and clean plates.",
                "solution_steps": {
                    "step1": "Understand the pedagogical role of self-monitoring diaries in health education.",
                    "step2": "Recording meals builds mindful metacognition regarding speed, variety, and waste.",
                    "step3": "Select the reflection option covering speed, balance, and conservation."
                }
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Grand Challenge III",
        "description": "Mastery challenge on aerobic fitness, skeletal-muscular benefits of yoga postures, sleep neurobiology, and circadian melatonin rhythms.",
        "sim_id": "sim-19",
        "sim_title": "Interactive Mastery Assessment",
        "speech": "",
        "questions": [
            {
                "id": "c3_q1",
                "q": "How does 60 minutes of daily vigorous physical play impact the human cardiovascular system?",
                "options": [
                    "It strengthens cardiac muscle, boosts blood circulation, and enhances lung oxygen uptake",
                    "It turns the heart into a fragile plastic tube",
                    "It completely blocks blood vessels with solid salt crystals",
                    "It stops the lungs from absorbing any oxygen"
                ],
                "ans": "It strengthens cardiac muscle, boosts blood circulation, and enhances lung oxygen uptake",
                "hint": "Physical exercise makes the heart pump vigorously, improving endurance.",
                "explanation": "Vigorous aerobic play trains the cardiac muscle to pump more blood per stroke while expanding lung vital capacity.",
                "solution_steps": {
                    "step1": "Analyze the physiological adaptations resulting from sustained aerobic activity.",
                    "step2": "Cardiac output increases, vascular resistance decreases, and oxygen transport improves.",
                    "step3": "Select the response detailing strengthened cardiac muscle and enhanced oxygenation."
                }
            },
            {
                "id": "c3_q2",
                "q": "Which mood-elevating chemical neurotransmitters are released by the brain during active outdoor play?",
                "options": [
                    "Endorphins and dopamine",
                    "Sulfuric acid and bleach",
                    "Carbon monoxide bubbles",
                    "Lead particles"
                ],
                "ans": "Endorphins and dopamine",
                "hint": "These natural brain chemicals reduce stress and produce joyful feelings.",
                "explanation": "Vigorous exercise stimulates the release of endorphins and dopamine, reducing anxiety and promoting happiness.",
                "solution_steps": {
                    "step1": "Identify neurochemicals associated with the positive feelings experienced after running.",
                    "step2": "Endorphins act as natural pain-relievers and mood lifters; dopamine drives motivation.",
                    "step3": "Confirm that endorphins and dopamine are the key exercise-induced brain chemicals."
                }
            },
            {
                "id": "c3_q3",
                "q": "Why are traditional active games like Kho-Kho, Kabaddi, and skipping rope superior to sedentary video games?",
                "options": [
                    "They develop muscular strength, cardiovascular endurance, agility, and teamwork simultaneously",
                    "They require sitting in a dark corner for ten hours",
                    "They cause eye strain and spinal stiffness",
                    "They prevent children from breathing fresh air"
                ],
                "ans": "They develop muscular strength, cardiovascular endurance, agility, and teamwork simultaneously",
                "hint": "Traditional games require running, dodging, jumping, and cooperating with friends.",
                "explanation": "Active traditional games build physical coordination, bone density, cardiac stamina, and cooperative social bonds.",
                "solution_steps": {
                    "step1": "Compare the biomechanical and social demands of physical tag games versus screen games.",
                    "step2": "Running, sprinting, and leaping engage large muscle groups and socialize players.",
                    "step3": "Choose the option highlighting strength, endurance, agility, and team camaraderie."
                }
            },
            {
                "id": "c3_q4",
                "q": "Which yoga posture, also known as Vrikshasana, trains neuromuscular balance, mental concentration, and ankle stability?",
                "options": [
                    "Tree Pose",
                    "Snake Pose",
                    "Child Pose",
                    "Bow Pose"
                ],
                "ans": "Tree Pose",
                "hint": "In this asana, one foot rests on the inner thigh while hands stretch upward like branches.",
                "explanation": "Vrikshasana (Tree Pose) requires standing on one leg with palms joined overhead, refining balance and focus.",
                "solution_steps": {
                    "step1": "Translate the Sanskrit term 'Vrikshasana' ('Vriksha' means tree).",
                    "step2": "Recall the posture geometry: single-leg standing balance with arms reaching like foliage.",
                    "step3": "Identify the Tree Pose as the target balance asana."
                }
            },
            {
                "id": "c3_q5",
                "q": "How does practicing Bhujangasana (Cobra Pose) physically benefit a growing student's spine?",
                "options": [
                    "It gently arches the spinal column backward, opening the chest and countering desk slouching",
                    "It bends the spine into a permanent right angle",
                    "It makes the ribs snap like dry twigs",
                    "It stops blood flow to the head"
                ],
                "ans": "It gently arches the spinal column backward, opening the chest and countering desk slouching",
                "hint": "The body lifts the upper chest off the floor, mimicking a cobra with raised hood.",
                "explanation": "Cobra Pose stretches the abdominal wall, expands lung volume, and strengthens back muscles to reverse desk slouching.",
                "solution_steps": {
                    "step1": "Recall the biomechanics of the Bhujangasana backward extension.",
                    "step2": "Students spend hours hunching forward over desks; cobra extension decompresses spinal vertebrae.",
                    "step3": "Select the answer explaining spinal arching, chest opening, and slouch correction."
                }
            },
            {
                "id": "c3_q6",
                "q": "What crucial physiological maintenance occurs in the brain during deep nighttime slow-wave sleep?",
                "options": [
                    "The glymphatic system flushes away metabolic toxic waste while memories are consolidated",
                    "The brain switches off entirely like an unplugged television",
                    "Brain cells shrink and dissolve permanently",
                    "All facts learned in school are completely forgotten"
                ],
                "ans": "The glymphatic system flushes away metabolic toxic waste while memories are consolidated",
                "hint": "Cerebrospinal fluid bathes the brain to wash out cellular waste proteins.",
                "explanation": "During deep sleep, the brain activates the glymphatic rinse to eliminate toxins and cement daytime memories into long-term storage.",
                "solution_steps": {
                    "step1": "Identify the neurobiological functions of deep stage 3 and REM sleep.",
                    "step2": "The glymphatic network cleanses metabolic waste products like beta-amyloid.",
                    "step3": "Simultaneously, hippocampus circuits replay and consolidate daily academic learning."
                }
            },
            {
                "id": "c3_q7",
                "q": "Which endocrine gland secretes human growth hormone primarily during deep sleep in children?",
                "options": [
                    "Pituitary gland",
                    "Salivary gland",
                    "Sweat gland",
                    "Tear gland"
                ],
                "ans": "Pituitary gland",
                "hint": "A master pea-sized gland located at the base of the brain.",
                "explanation": "The pituitary gland releases pulses of growth hormone during deep slow-wave sleep to stimulate bone and muscle growth.",
                "solution_steps": {
                    "step1": "Identify the anatomical gland responsible for producing human growth hormone.",
                    "step2": "Recall that deep sleep triggers the anterior pituitary to secrete growth hormone.",
                    "step3": "Confirm that the pituitary gland drives physical growth and cellular repair during sleep."
                }
            },
            {
                "id": "c3_q8",
                "q": "What is the biological name of the natural 24-hour day-night cycle governing human sleep and wakefulness?",
                "options": [
                    "Circadian rhythm",
                    "Carbon cycle",
                    "Water cycle",
                    "Nitrogen fixation"
                ],
                "ans": "Circadian rhythm",
                "hint": "Derived from the Latin 'circa diem', meaning 'around a day'.",
                "explanation": "The circadian rhythm is our internal biological clock that coordinates hormone levels, body temperature, and sleep cycles over 24 hours.",
                "solution_steps": {
                    "step1": "Recognize the scientific term for the internal daily biological pacemaker.",
                    "step2": "'Circadian' describes physiological oscillations that repeat roughly every 24 hours.",
                    "step3": "Select circadian rhythm as the regulatory cycle for sleep and wakefulness."
                }
            },
            {
                "id": "c3_q9",
                "q": "Why does using mobile phones, tablets, or televisions in bed disrupt natural sleep onset?",
                "options": [
                    "The blue light emitted from screens suppresses the secretion of the sleep hormone melatonin",
                    "The screen emits freezing cold air that chills the eyes",
                    "The device produces high-voltage electricity that shocks the fingers",
                    "The phone makes the bedroom spin around in circles"
                ],
                "ans": "The blue light emitted from screens suppresses the secretion of the sleep hormone melatonin",
                "hint": "Blue light tricks the brain into thinking it is still bright midday.",
                "explanation": "Blue wavelength light strikes retinal ganglion cells, tricking the pineal gland into blocking melatonin release.",
                "solution_steps": {
                    "step1": "Examine how short-wavelength blue screen light affects the pineal gland.",
                    "step2": "Retinal photoreceptors perceive blue light as solar noon, shutting down melatonin production.",
                    "step3": "Without melatonin, sleep onset is delayed, resulting in nighttime insomnia."
                }
            },
            {
                "id": "c3_q10",
                "q": "What is an ideal bedroom environment for achieving deep, undisturbed, restorative sleep?",
                "options": [
                    "Dark, quiet, well-ventilated, cool, and completely free of glowing electronic screens",
                    "Blaring loud rock music with flashing bright strobe lights all night",
                    "A stuffy, overheated room with five active televisions playing action movies",
                    "An open room full of buzzing mosquitoes and constant car horn honking"
                ],
                "ans": "Dark, quiet, well-ventilated, cool, and completely free of glowing electronic screens",
                "hint": "Think of conditions that allow the nervous system to relax without sensory stimulation.",
                "explanation": "A cool, quiet, pitch-dark, and well-ventilated bedroom minimizes sensory arousal, facilitating deep slumber.",
                "solution_steps": {
                    "step1": "Review recommended clinical sleep hygiene guidelines.",
                    "step2": "Low ambient temperature, complete darkness, silence, and fresh airflow maximize sleep quality.",
                    "step3": "Choose the serene, screen-free dark and cool bedroom setting."
                }
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Grand Challenge IV",
        "description": "Mastery challenge on personal body boundaries, the universal Swimsuit Rule, the NO-RUN-TELL action sequence, and balanced lifestyle design.",
        "sim_id": "sim-20",
        "sim_title": "Interactive Mastery Assessment",
        "speech": "",
        "questions": [
            {
                "id": "c4_q1",
                "q": "What is the defining characteristic of a 'safe touch'?",
                "options": [
                    "It feels comforting, caring, open, and makes you feel secure and respected",
                    "It makes you feel terrified, confused, hurt, and uneasy",
                    "It must always be kept a top secret from parents",
                    "It is accompanied by painful pinches and threats"
                ],
                "ans": "It feels comforting, caring, open, and makes you feel secure and respected",
                "hint": "Safe touches bring warmth and never demand hiding or secrecy.",
                "explanation": "Safe touches (like a supportive parent hug or high-five) promote emotional security and mutual respect.",
                "solution_steps": {
                    "step1": "Define what constitutes safe physical touch in child welfare education.",
                    "step2": "Safe touches are caring, open, respectful, and never induce shame or confusion.",
                    "step3": "Select the option emphasizing comfort, security, and open mutual respect."
                }
            },
            {
                "id": "c4_q2",
                "q": "According to the universal Swimsuit Rule, which parts of your body are strictly private?",
                "options": [
                    "The parts covered by a swimsuit: chest, groin, buttocks, and the mouth",
                    "Only the hair and eyelashes",
                    "Only the elbows and kneecaps",
                    "No parts of the human body are private"
                ],
                "ans": "The parts covered by a swimsuit: chest, groin, buttocks, and the mouth",
                "hint": "Picture the areas concealed when wearing a traditional one-piece bathing suit.",
                "explanation": "The Swimsuit Rule teaches that areas covered by swimwear plus the mouth belong solely to the individual child.",
                "solution_steps": {
                    "step1": "Recall the pedagogical definition of the universal Swimsuit Rule.",
                    "step2": "Identify swimsuit-covered zones: chest, genitals/groin, buttocks, plus the mouth.",
                    "step3": "Confirm these zones are strictly private and protected from unauthorized contact."
                }
            },
            {
                "id": "c4_q3",
                "q": "Under what singular condition may a doctor or nurse examine your private body parts?",
                "options": [
                    "Only for medical health reasons, and strictly with your parent or guardian present in the room",
                    "Whenever they want in a hidden locked basement with nobody watching",
                    "Only when accompanied by strangers from the street",
                    "Never under any circumstances even in emergencies"
                ],
                "ans": "Only for medical health reasons, and strictly with your parent or guardian present in the room",
                "hint": "Medical examinations of private zones must always have parental supervision.",
                "explanation": "A physician may only examine private areas for legitimate medical checkups when a parent is right there beside the child.",
                "solution_steps": {
                    "step1": "Understand the ethical medical protocol regarding physical checkups on children.",
                    "step2": "Doctor checkups must be strictly clinical and require a parent/guardian present in the room.",
                    "step3": "Select the supervised medical checkup option with parent presence."
                }
            },
            {
                "id": "c4_q4",
                "q": "What is the very first step in the three-step personal safety action plan if someone crosses your boundaries?",
                "options": [
                    "Say a loud, firm and confident 'NO!' or 'STOP!'",
                    "Whisper an apology and hang your head in shame",
                    "Smile and pretend it was a funny joke",
                    "Promise to keep the incident a strict secret"
                ],
                "ans": "Say a loud, firm and confident 'NO!' or 'STOP!'",
                "hint": "Use your voice decisively to reject the inappropriate contact immediately.",
                "explanation": "The first step of 'NO - RUN - TELL' is asserting your boundary firmly with a clear, loud 'NO!' or 'STOP!'.",
                "solution_steps": {
                    "step1": "Recall the 3-step sequence: 1. NO, 2. RUN, 3. TELL.",
                    "step2": "The initial action requires using an assertive, commanding voice.",
                    "step3": "Identify saying a firm, confident 'NO!' as the first crucial defensive action."
                }
            },
            {
                "id": "c4_q5",
                "q": "Where should you run after shouting 'NO' to an unsafe person?",
                "options": [
                    "To a well-lit, open public place where other people and trusted adults are present",
                    "Into a dark, deserted, locked alleyway",
                    "Under a hidden bed in an empty house",
                    "Behind a tall wall far away from any living human being"
                ],
                "ans": "To a well-lit, open public place where other people and trusted adults are present",
                "hint": "Safety lies in open spaces where witnesses and protective adults are nearby.",
                "explanation": "Running to a populated, bright area deters offenders and allows you to find adult assistance immediately.",
                "solution_steps": {
                    "step1": "Analyze the spatial tactics of escaping personal danger.",
                    "step2": "Dark or isolated spaces increase vulnerability; open, busy public spaces provide safety.",
                    "step3": "Conclude that running to bright spaces with trusted people is the safest choice."
                }
            },
            {
                "id": "c4_q6",
                "q": "Who belongs in a child's personal 'Safety Circle'?",
                "options": [
                    "Reliable adults who listen, believe, and protect—such as parents, grandparents, and school teachers",
                    "Total strangers met once on an internet gaming chat",
                    "Unfriendly bullies from an older neighborhood gang",
                    "Anonymous callers who ask for home addresses"
                ],
                "ans": "Reliable adults who listen, believe, and protect—such as parents, grandparents, and school teachers",
                "hint": "Trusted caregivers with proven track records of protecting your welfare.",
                "explanation": "A Safety Circle consists of dependable caregivers (family members, trusted teachers, school counselors) who ensure safety.",
                "solution_steps": {
                    "step1": "Define what constitutes a child's protective Safety Circle.",
                    "step2": "Members must be trustworthy adults with authority to protect the child unconditionally.",
                    "step3": "Identify parents, teachers, and grandparents as core Safety Circle guardians."
                }
            },
            {
                "id": "c4_q7",
                "q": "If someone tells you, 'If you tell your parents about this touch, bad things will happen', what should you do?",
                "options": [
                    "Tell your trusted parents immediately; safe adults never use threats or secrets",
                    "Obey the threat and keep the secret forever",
                    "Blame yourself and hide in your bedroom",
                    "Stop going to school permanently without telling anyone why"
                ],
                "ans": "Tell your trusted parents immediately; safe adults never use threats or secrets",
                "hint": "Threats and forced secrecy are red-flag manipulative tactics used by unsafe individuals.",
                "explanation": "Perpetrators use threats to intimidate children into silence. Safe adults never demand secrecy regarding physical touch.",
                "solution_steps": {
                    "step1": "Deconstruct the manipulative psychological pattern of boundary violators.",
                    "step2": "Threats are designed to enforce silence; breaking the silence breaks the offender's power.",
                    "step3": "Tell parents immediately because threats are proof of wrongful behavior by the offender."
                }
            },
            {
                "id": "c4_q8",
                "q": "If a child experiences an unsafe touch or boundary violation, whose fault is it?",
                "options": [
                    "100% the fault of the person who committed the violation; the child is never at fault",
                    "The child's fault for walking in the hallway",
                    "The child's fault for being polite earlier",
                    "The fault of the clothes the child was wearing"
                ],
                "ans": "100% the fault of the person who committed the violation; the child is never at fault",
                "hint": "A victim of inappropriate behavior is never to blame.",
                "explanation": "Children must always understand that boundary violations are entirely the fault of the violator, never the child.",
                "solution_steps": {
                    "step1": "Reinforce the core child protection tenet regarding personal culpability.",
                    "step2": "Offenders bear 100% moral and legal responsibility for their actions.",
                    "step3": "Assert definitively that the child is never, under any circumstances, at fault."
                }
            },
            {
                "id": "c4_q9",
                "q": "What should you do if the first adult you tell about an unsafe incident does not believe or help you?",
                "options": [
                    "Keep telling other trusted adults in your Safety Circle until someone takes active steps to protect you",
                    "Give up completely and decide nobody in the world cares",
                    "Apologize to the person who hurt you",
                    "Assume you must have imagined the entire experience"
                ],
                "ans": "Keep telling other trusted adults in your Safety Circle until someone takes active steps to protect you",
                "hint": "Persistence is key: do not stop until someone takes action.",
                "explanation": "If one adult dismisses your concern, keep speaking to other adults (teachers, counselors, relatives) until you are safe.",
                "solution_steps": {
                    "step1": "Identify the resilience protocol when initial disclosure meets disbelief or inaction.",
                    "step2": "A single adult's failure to respond does not negate the reality of the danger.",
                    "step3": "Advocate persistently by approaching next trusted guardians until protection is secured."
                }
            },
            {
                "id": "c4_q10",
                "q": "How does combining wholesome food, daily exercise, boundary safety, and 9-10 hours of sleep create holistic happiness?",
                "options": [
                    "It builds physical strength, mental clarity, emotional security, and energetic vitality for life",
                    "It makes the human body turn into an iron robot that never laughs",
                    "It causes people to stop having any emotions or fun",
                    "It ensures that a person will sleep 24 hours every day"
                ],
                "ans": "It builds physical strength, mental clarity, emotional security, and energetic vitality for life",
                "hint": "Holistic health unites body, mind, and emotional protection into balanced vitality.",
                "explanation": "Holistic living integrates nutritious food, athletic vigor, emotional boundaries, and sleep into vibrant lifelong well-being.",
                "solution_steps": {
                    "step1": "Synthesize the overarching thematic pillars of Chapter 6.",
                    "step2": "Connect nutrition + physical fitness + emotional boundary safety + restorative sleep.",
                    "step3": "Conclude that this balanced combination delivers lifelong strength, joy, and vitality."
                }
            }
        ]
    }
]

if __name__ == '__main__':
    total_q = sum(len(s.get('questions', [])) for s in slides_part3)
    print(f"Total quiz questions across Slides 17-20: {total_q}")
    assert total_q == 40, f"Expected 40 questions, got {total_q}"
    for s in slides_part3:
        assert len(s['title'].split()) <= 3, f"Title too long: {s['title']}"
        assert len(s['questions']) == 10, f"Slide {s['id']} needs 10 questions"
        for q in s['questions']:
            assert q['ans'] in q['options'], f"Answer '{q['ans']}' not in options for {q['id']}"
            assert len(q['options']) == 4, f"Question {q['id']} must have 4 options"
            assert 'step1' in q['solution_steps'] and 'step2' in q['solution_steps'] and 'step3' in q['solution_steps'], f"Missing steps in {q['id']}"
    print("All 40 challenge questions passed verification successfully!")


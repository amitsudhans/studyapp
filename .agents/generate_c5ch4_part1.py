"""
Data generator for NCERT Class 5 Science Chapter 4: Our School - A Happy Place - Part 1 (Slides 1 to 8)
Zero lecturer names. Indian male voice priority. Short punchy headings (1-3 words).
Zero raw LaTeX.
"""

CHAPTER_META = {
    "chapter_num": 4,
    "title": "Our School - A Happy Place",
    "subtitle": "Campus Ecology, Resource Conservation, Safety Drills & Inclusive Empathy",
    "class": "Class 5",
    "subject": "Science"
}

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Happy Campus",
        "subtitle": "Aasha & Mohit's Vision of a Safe, Caring & Green School",
        "concept_html": """
            <p>Walking to school on a bright morning, students <strong>Aasha and Mohit</strong> discuss what makes their school truly special. School is more than classrooms and blackboards—it is a <strong>happy place</strong> where every child feels emotionally safe, cared for, respected, and inspired to discover the world.</p>
            <div class="my-3 p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-xs">
                🌱 <strong>The Green School Vision:</strong> A forward-thinking campus that manages its own waste, conserves every drop of water, switches off idle electricity, and plants indigenous trees for birds and shade.
            </div>
            <p>A sustainable school balances physical infrastructure with environmental stewardship:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-0.5">Emotional Well-being</strong>
                    Warm welcomes, mutual kindness, inclusive friendships, and freedom from bullying or fear.
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-emerald-400 block mb-0.5">Eco-Action Campus</strong>
                    Active composting, rainwater recharge pits, rooftop solar cells, and shaded green verandas.
                </div>
            </div>
        """,
        "spoken_text": "Welcome to our school, a happy place. As students Aasha and Mohit walked through the campus gates, they reflected on why school feels so comforting and joyful. A true school is a haven where every student feels safe, encouraged, and excited to learn. But a great school also cares for our Mother Earth. They imagined transforming their campus into a vibrant green school, where water is cherished, waste is transformed into compost, energy is conserved, and leafy trees shelter singing birds. Every child can be an active leader in creating a happy, healthy school environment.",
        "lecture_script": "Introduction to the concept of a safe, inclusive school, emotional well-being, and the four pillars of a green campus: water, energy, waste, and biodiversity.",
        "checkpoints": [
            {
                "question": "Which set of characteristics best describes a school that is a genuine 'happy place' for all students?",
                "options": [
                    "Strict silence, zero playtime, and locked libraries",
                    "A safe, welcoming environment where students feel respected, cared for, and inspired to learn",
                    "A campus with no trees or outdoor playing fields",
                    "An exam-only building with no social interaction"
                ],
                "correct": 1,
                "explanation": "A happy school fosters safety, mutual respect, encouragement, inclusive participation, and joyous experiential learning for every student.",
                "study_insight": "Emotional safety and mutual kindness allow children's minds to concentrate better and absorb scientific concepts enthusiastically."
            },
            {
                "question": "What is the primary objective of creating a 'green school' campus?",
                "options": [
                    "Painting all classroom walls and desks dark green",
                    "Practicing sustainable habits: waste segregation, water conservation, energy saving, and tree planting",
                    "Replacing all printed books with plastic leaves",
                    "Forbidding students from drinking water during the day"
                ],
                "correct": 1,
                "explanation": "A green school practices ecological responsibility by minimizing waste, conserving water and electricity, and creating biodiverse native plant habitats.",
                "study_insight": "A green school turns the entire campus into a living laboratory where environmental science is practiced daily."
            }
        ]
    },
    {
        "id": 2,
        "title": "School Explorers",
        "subtitle": "Specialized Inquiry Teams Auditing the School Environment",
        "concept_html": """
            <p>To turn green ideas into concrete action, students organize into specialized <strong>School Explorer Teams</strong>. Each team maps, observes, and audits different environmental aspects of the campus:</p>
            <div class="my-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">💧 Water Watchers</strong>
                    Inspect taps, washbasins, drinking coolers, and water tanks to spot dripping leaks and overflowing troughs.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">⚡ Electricity Savers</strong>
                    Check empty classrooms to switch off running fans, tube lights, and monitors during recess and sports periods.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-rose-400 block mb-1">🗑️ Waste Warriors</strong>
                    Audit campus litter, monitor classroom dustbins, and check if food scraps and papers are separated properly.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-emerald-400 block mb-1">🌳 Green Guardians</strong>
                    Nurture garden beds, count mature shade trees, water saplings, and record visiting birds and butterflies.
                </div>
            </div>
            <div class="p-2 rounded-lg bg-indigo-950/40 border border-indigo-500/30 text-[11px] text-indigo-300">
                🚶 <strong>Traffic Trackers:</strong> Observe the main gate during morning drop-off and afternoon dismissal to record vehicle congestion and pedestrian crosswalk safety.
            </div>
        """,
        "spoken_text": "To investigate the school environment scientifically, students formed specialized explorer brigades. The Water Watchers walked from tap to tap, listening for leaks and measuring wasted drips. The Electricity Savers patrolled corridors during recess, switching off idle fans and lights left spinning in empty rooms. The Waste Warriors inspected dustbins to make sure fruit peels were separated from paper. Meanwhile, the Green Guardians mapped campus trees and watered young saplings, while the Traffic Trackers observed safety around the school gate.",
        "lecture_script": "The structure and operational roles of student environmental audit brigades: Water Watchers, Electricity Savers, Waste Warriors, Green Guardians, and Traffic Trackers.",
        "checkpoints": [
            {
                "question": "What is the primary responsibility of the student 'Electricity Savers' team during daily school hours?",
                "options": [
                    "Cutting electrical power cables with scissors",
                    "Patrolling empty rooms to turn off idle fans, lights, and projectors during lunch and recess",
                    "Removing all electric bulbs permanently from science labs",
                    "Prohibiting computers from running educational videos"
                ],
                "correct": 1,
                "explanation": "Electricity Savers actively audit rooms to ensure lights, fans, and electronics are turned off when not in use, preventing unnecessary energy wastage.",
                "study_insight": "A single ceiling fan left spinning in an empty classroom for an hour wastes over 75 watt-hours of electrical energy."
            },
            {
                "question": "Which student audit team is specifically tasked with monitoring leaking taps and overflowing overhead water tanks?",
                "options": [
                    "Traffic Trackers",
                    "Water Watchers",
                    "Waste Warriors",
                    "Green Guardians"
                ],
                "correct": 1,
                "explanation": "The Water Watchers team monitors campus plumbing, identifying dripping taps, broken washers, and overflow pipes to conserve drinking water.",
                "study_insight": "Regular student audits allow minor leaks to be reported to school plumbers before thousands of liters are lost."
            }
        ]
    },
    {
        "id": 3,
        "title": "Waste Sorting",
        "subtitle": "The 3Rs Hierarchy & Source Segregation: Wet vs Dry Waste",
        "concept_html": """
            <p>Every school day generates kilograms of discard: pencil shavings, snack wrappers, leftover tiffin peels, and torn paper sheets. Managing this begins with the <strong>3Rs principle: Reduce, Reuse, and Recycle</strong>.</p>
            <div class="my-3 p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-cyan-200 text-xs">
                🔄 <strong>Source Segregation Rule:</strong> Mixing wet organic waste with dry recyclable materials ruins both! Waste must be separated right at the point of disposal into designated bins.
            </div>
            <p>The two fundamental waste categories:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200">
                    <strong class="text-emerald-300 block mb-1">🟢 Wet (Biodegradable) Waste</strong>
                    Fruit skins, vegetable peels, leftover lunch food, tea leaves, and garden fallen leaves. Decomposes naturally into nutrient-rich compost.
                </div>
                <div class="p-2.5 rounded-xl bg-sky-950/40 border border-sky-500/30 text-sky-200">
                    <strong class="text-sky-300 block mb-1">🔵 Dry (Non-Biodegradable) Waste</strong>
                    Used paper, cardboard boxes, plastic wrappers, metal foil, glass bottles, and dry pencil shavings. Can be sorted, cleaned, and recycled.
                </div>
            </div>
        """,
        "spoken_text": "Every single day, classrooms produce waste. But trash is only trash when it is mixed up! When wet food scraps are thrown into the same bin as clean paper, the paper gets soiled, soggy, and cannot be recycled. Waste sorting at source is our golden rule. Green bins receive wet, biodegradable organic waste like banana peels and cucumber scraps, which decompose into rich garden compost. Blue bins hold clean, dry items like worksheets and cardboard, ready to be sent to paper recycling mills.",
        "lecture_script": "The 3Rs hierarchy (Reduce, Reuse, Recycle), biodegradable vs non-biodegradable waste classification, and the dual-bin source segregation system.",
        "checkpoints": [
            {
                "question": "Why is it critical to separate wet food waste from dry paper waste right at the classroom dustbin?",
                "options": [
                    "To make the dustbins look colorful for photography",
                    "Mixing wet food with paper makes paper soggy, foul-smelling, and impossible to recycle into new books",
                    "Wet waste cannot touch air under any circumstances",
                    "Dry paper catches fire whenever it touches banana peels"
                ],
                "correct": 1,
                "explanation": "Wet organic food soils dry paper and cardboard, contaminating them with moisture and oils that jam paper-pulping recycling machinery.",
                "study_insight": "Separating waste at source is ten times more efficient than trying to separate mixed garbage at a city landfill."
            },
            {
                "question": "Which of the following discarded school items belongs strictly in the green bin for wet organic waste?",
                "options": [
                    "Empty plastic ballpoint pen refills",
                    "Banana peels, orange skins, and apple cores from lunch boxes",
                    "Old glossy science magazines",
                    "Broken steel geometry compasses"
                ],
                "correct": 1,
                "explanation": "Fruit skins and food scraps are biodegradable organic matter that microorganisms break down into natural compost for school gardens.",
                "study_insight": "Composting wet waste prevents greenhouse methane gas emissions that form when food rots in deep, airless landfills."
            }
        ]
    },
    {
        "id": 4,
        "title": "Clean Hands",
        "subtitle": "Recycling Chains & The Dignity of Labour of Sanitation Workers",
        "concept_html": """
            <p>What happens after dry waste is deposited in the blue bin? Local <strong>recyclers (kabbadiwalas)</strong> and municipal sanitation teams collect sorted newspapers, cardboard cartons, and plastics to channel them back into production factories.</p>
            <div class="my-3 p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200 text-xs">
                🤝 <strong>Dignity of Labour:</strong> Sanitation workers, cleaners, and recyclers perform vital public health work. They keep our classrooms clean, prevent disease epidemics, and protect our natural environment. They deserve our deepest respect, gratitude, and cooperation!
            </div>
            <p>How students practice dignity of labour and hygiene:</p>
            <ul class="mt-2 space-y-1.5 text-xs text-slate-300">
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">1.</span>
                    <span><strong>Clean Up After Yourself:</strong> Never leave tiffin crumbs on desks or throw wrappers on the floor expecting staff to pick them up.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">2.</span>
                    <span><strong>Say Thank You:</strong> Greet school housekeeping and sanitation staff with polite smiles and respectful words every day.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">3.</span>
                    <span><strong>Hand Hygiene:</strong> Wash hands thoroughly with soap and water after handling waste or using the restroom.</span>
                </li>
            </ul>
        """,
        "spoken_text": "Who keeps our school corridors sparkling clean every morning? Sanitation workers and paper recyclers carry out essential work that protects community health. Without them, cities would drown in mountains of disease-breeding garbage. The concept of dignity of labour teaches us that all honest work is noble and deserving of deep respect. We can honor sanitation staff by keeping our desks tidy, throwing trash into the proper bin ourselves, greeting them with warmth, and washing our hands thoroughly after waste disposal.",
        "lecture_script": "The informal recycling economy, community hygiene infrastructure, ethical appreciation of the dignity of labour, and personal cleanliness habits.",
        "checkpoints": [
            {
                "question": "Why is the work performed by sanitation workers and scrap recyclers considered essential for society?",
                "options": [
                    "They hide all garbage underground so it disappears into space",
                    "They maintain community hygiene, prevent deadly disease outbreaks, and recover recyclable materials to save raw trees and ores",
                    "They ensure that no new paper mills are ever built",
                    "They turn old plastic directly into edible sweets"
                ],
                "correct": 1,
                "explanation": "Sanitation teams protect public health by preventing pest infestations and water contamination, while recyclers divert valuable materials back into productive manufacturing loops.",
                "study_insight": "Recycling one ton of old newspaper saves approximately 17 mature trees and 26,000 liters of fresh water."
            },
            {
                "question": "Which action by a student best demonstrates respect and dignity of labour toward school housekeeping staff?",
                "options": [
                    "Tossing pencil shavings deliberately onto the floor for cleaners to sweep",
                    "Discarding trash responsibly in dustbins, cleaning personal tiffin crumbs, and greeting staff with polite gratitude",
                    "Demanding that sanitation workers carry personal school bags",
                    "Leaving washbasin taps running continuously"
                ],
                "correct": 1,
                "explanation": "Dignity of labour is practiced through personal responsibility—cleaning up after oneself and treating sanitation personnel with polite appreciation and respect.",
                "study_insight": "Every honest occupation contributes to the smooth functioning of society and deserves equal respect."
            }
        ]
    },
    {
        "id": 5,
        "title": "Natural Cooling",
        "subtitle": "Passive Architecture: Shade, Cross-Ventilation & Reflective White Roofs",
        "concept_html": """
            <p>Have you ever noticed that some classrooms feel cool and breezy on hot afternoons, while top-floor rooms feel like hot ovens? Buildings can be kept comfortable naturally through <strong>passive thermal cooling</strong>:</p>
            <div class="my-3 grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🌳</span>
                    <strong class="text-emerald-400 block">Canopy Shade</strong>
                    Trees block direct solar radiation from heating exterior brick walls.
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🪟</span>
                    <strong class="text-cyan-400 block">Cross-Ventilation</strong>
                    Open windows on opposite walls create a cooling breeze, flushing out hot trapped air.
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">⚪</span>
                    <strong class="text-amber-400 block">White Cool Roofs</strong>
                    White surfaces reflect up to 85% of solar radiation instead of absorbing heat like dark tar roofs.
                </div>
            </div>
            <div class="mt-3 p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-xs text-slate-300">
                <strong>Color & Solar Absorption:</strong> Dark black surfaces absorb nearly all incoming solar wavelengths, converting radiant light into intense heat. White and light-colored coatings reflect light away, keeping indoor room temperatures 3°C to 5°C cooler!
            </div>
        """,
        "spoken_text": "Why are some rooms in school naturally cool and breezy while others feel stifling and hot? We do not always need noisy air conditioners to stay cool! Clever architectural science gives us natural cooling. When mature trees shade our classroom walls, brick walls do not heat up. Opening windows on opposite walls allows fresh air to stream through in a continuous draft called cross-ventilation. Furthermore, painting school roofs with reflective white lime or solar-reflective paint bounces the sun's scorching rays right back into the sky, lowering indoor temperatures by up to five degrees.",
        "lecture_script": "Thermal physics of building design: solar albedo and reflective white coatings, convective cross-ventilation, and vegetative shading.",
        "checkpoints": [
            {
                "question": "Why does painting school roofs with bright white reflective paint keep top-floor classrooms noticeably cooler in summer?",
                "options": [
                    "White paint releases artificial ice into the ceiling tiles",
                    "White surfaces have high solar reflectance, bouncing away sunlight instead of absorbing it as heat",
                    "White paint attracts rainy clouds directly above the building",
                    "White color absorbs all heat and stores it inside the paint layer"
                ],
                "correct": 1,
                "explanation": "White surfaces have a high albedo (reflectivity), reflecting up to 80-85% of solar radiation back into the atmosphere, preventing the concrete roof slab from soaking in thermal energy.",
                "study_insight": "In traditional Indian architecture, whitewashing roofs and outer walls with lime (chuna) is an ancient, cost-effective cooling technique."
            },
            {
                "question": "How does cross-ventilation improve classroom comfort on a warm afternoon?",
                "options": [
                    "It seals the room completely so air cannot move",
                    "Opening windows on opposite walls allows cool outside air to enter while expelling stale, warm air",
                    "It converts nitrogen gas into liquid water",
                    "It blocks all natural light from entering the room"
                ],
                "correct": 1,
                "explanation": "Cross-ventilation harnesses natural pressure differentials. Wind entering through windward windows pushes warm, stagnant indoor air out through leeward windows, refreshing the room.",
                "study_insight": "Warm air is lighter and naturally rises toward the ceiling, so high windows and transoms help hot air escape."
            }
        ]
    },
    {
        "id": 6,
        "title": "Water Leaks",
        "subtitle": "Drop-by-Drop Wastage, Tap Repairs & The Jal Shakti Abhiyan",
        "concept_html": """
            <p>During their morning audit, the Water Watchers found a washroom tap that appeared to be turned off, yet leaked a single drop every few seconds. Is a dripping tap really a big deal?</p>
            <div class="my-3 p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-cyan-200 text-xs">
                💧 <strong>The Shocking Math of Leaks:</strong> A tap dripping just once per second wastes over <strong>30 liters of water every single day</strong>—that is more than <strong>10,000 liters of pure drinking water wasted per year</strong> from a single loose rubber washer!
            </div>
            <p>National water conservation initiatives like the <strong>Jal Shakti Abhiyan</strong> promote action across campuses:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs text-slate-300">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                    <strong class="text-cyan-400 block mb-1">🛠️ Rapid Plumbing Repairs</strong>
                    Replace worn rubber gaskets and washers promptly to stop trickles immediately.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                    <strong class="text-emerald-400 block mb-1">🌧️ Rooftop Rain Harvesting</strong>
                    Channel clean monsoon rain from terrace gutters into percolation pits to recharge underground aquifers.
                </div>
            </div>
        """,
        "spoken_text": "Drip, drip, drip. Have you ever walked past a tap dripping slowly and thought it was harmless? Let us look at the mathematics. A tap that drips just one drop every second wastes more than thirty liters of precious water in twenty-four hours! That is enough water to supply a family's daily cooking needs. Across a year, a single leaking tap wastes ten thousand liters. Initiatives like the Jal Shakti Abhiyan remind us that every drop matters. When you spot a leak, report it to the plumber immediately and turn taps off firmly after washing your hands.",
        "lecture_script": "Quantitative analysis of dripping tap water wastage, mechanical washer failure, rainwater harvesting recharge pits, and community participation under Jal Shakti Abhiyan.",
        "checkpoints": [
            {
                "question": "How much water can a single tap dripping at the rate of one drop per second waste over the course of a full day?",
                "options": [
                    "Less than one teaspoon",
                    "Over 30 liters of clean water",
                    "Exactly 1,000,000 liters",
                    "Zero water, because drops evaporate instantly"
                ],
                "correct": 1,
                "explanation": "At one drop per second, approximately 86,400 drops fall every day, accumulating into over 30 liters of pure wasted water daily.",
                "study_insight": "Placing a measuring cup beneath a dripping tap for 10 minutes helps students calculate the real rate of campus water loss."
            },
            {
                "question": "What is the primary objective of community initiatives like the Jal Shakti Abhiyan in schools and villages?",
                "options": [
                    "Emptying all lakes into underground pipes",
                    "Promoting water conservation, fixing leaks, planting trees, and building rainwater harvesting systems",
                    "Replacing fresh tap water with salty ocean water",
                    "Stopping the monsoon rains from falling"
                ],
                "correct": 1,
                "explanation": "Jal Shakti Abhiyan is a national water security campaign focusing on rainwater harvesting, watershed rejuvenation, leak prevention, and groundwater recharge.",
                "study_insight": "Rainwater falling on school rooftops can be filtered through sand and gravel pits to replenish depleted groundwater tables."
            }
        ]
    },
    {
        "id": 7,
        "title": "Tree Canopies",
        "subtitle": "Microclimate Cooling, Air Filtration & Avian Habitats",
        "concept_html": """
            <p>On a hot afternoon, the Green Guardians carried a digital thermometer outdoors. Under direct blistering sunlight on the asphalt basketball court, the ground measured <strong>43°C</strong>. But stepping beneath the dense leafy canopy of a mature neem tree, the temperature plummeted to a gentle <strong>34°C</strong>!</p>
            <div class="my-3 p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-xs">
                🌳 <strong>Nature's Living Air Conditioners:</strong> Trees cool surroundings not just by physical shade, but through <strong>transpiration</strong>—roots pump groundwater up to leaves, where it evaporates as cool water vapor into the air.
            </div>
            <p>Trees provide multifaceted ecosystem services to a school campus:</p>
            <div class="mt-3 grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🐦</span>
                    <strong class="text-amber-400 block">Wildlife Homes</strong>
                    Nesting forks for sparrows, barbets, mynas, and honeybees.
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🍃</span>
                    <strong class="text-emerald-400 block">Air Purifiers</strong>
                    Leaf surfaces trap airborne dust particles and vehicle exhaust soot.
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">💨</span>
                    <strong class="text-cyan-400 block">Oxygen Factories</strong>
                    Leaves absorb carbon dioxide during photosynthesis, pumping fresh oxygen.
                </div>
            </div>
        """,
        "spoken_text": "Step out onto the concrete playground on a hot afternoon, and the ground radiates heat like an oven at over forty degrees Celsius. But take five steps beneath the leafy boughs of a big banyan or neem tree, and you instantly feel cool and refreshed. Why? Trees are living air conditioners. Through transpiration, trees draw moisture from deep in the soil and release it as cool invisible water vapor from their leaves. Trees also clean the air, trapping city dust on their bark and providing safe nesting homes for singing sparrows and cheerful squirrels.",
        "lecture_script": "The microclimate buffering of urban tree canopies, evaporative cooling via foliar transpiration, particulate matter trapping, and biodiversity support.",
        "checkpoints": [
            {
                "question": "Why is the air beneath a large leafy tree significantly cooler than under a concrete shelter on a sunny afternoon?",
                "options": [
                    "Trees release refrigerated coolant gases from their bark",
                    "Trees combine physical shade with transpiration, releasing cool water vapor that absorbs heat from the surrounding air",
                    "Trees suck all sunlight inside their trunks permanently",
                    "The wind only blows where trees are planted"
                ],
                "correct": 1,
                "explanation": "Transpiration is the evaporative loss of water from microscopic leaf pores (stomata). Just like sweat cools our skin, evaporating water cools the microclimate beneath the tree canopy.",
                "study_insight": "A single mature tree can transpire hundreds of liters of water daily, providing the cooling equivalent of 10 room-sized air conditioners running continuously."
            },
            {
                "question": "Which of the following represents an ecological benefit provided by native trees on a school campus?",
                "options": [
                    "They permanently replace the need for textbooks",
                    "They trap airborne dust on their leaves, generate oxygen, and provide nesting habitats for local birds and insects",
                    "They convert soil into pure plastic",
                    "They stop birds from flying"
                ],
                "correct": 1,
                "explanation": "Trees filter particulate matter from the air, release oxygen via photosynthesis, anchor soil with their roots, and shelter diverse birds, bees, and squirrels.",
                "study_insight": "Planting indigenous trees like neem, peepal, and jamun supports local wildlife far better than exotic ornamental trees."
            }
        ]
    },
    {
        "id": 8,
        "title": "Pollinator Gardens",
        "subtitle": "Designing Butterfly Gardens with Nectar & Caterpillar Host Plants",
        "concept_html": """
            <p>The Green Guardians decided to transform an unused sunny patch of campus into a flourishing <strong>Butterfly Garden</strong>. Butterflies do not visit random flowers; they require two specific types of botanical companions:</p>
            <div class="my-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200">
                    <strong class="text-rose-300 block mb-1">🌺 Nectar Plants (For Adult Butterflies)</strong>
                    Colorful, nectar-rich flowers like lantana, zinnia, marigold, cosmos, and periwinkle (sadabahar) where winged adult butterflies drink sweet floral nectar.
                </div>
                <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200">
                    <strong class="text-emerald-300 block mb-1">🌿 Host Plants (For Caterpillars)</strong>
                    Specific leafy plants where female butterflies lay eggs so hatched caterpillars can munch leaves (e.g., curry leaves for Common Mormon, milkweed for Plain Tiger).
                </div>
            </div>
            <p class="text-xs text-slate-300 mt-2">Butterflies are key <strong>pollinators</strong>. As they flit from flower to flower, pollen grains cling to their legs, fertilizing fruits and vegetables across the neighborhood.</p>
        """,
        "spoken_text": "Did you know that you can invite dazzling winged visitors to your school by planting a butterfly garden? Butterflies need two special kinds of plants to make your garden their home. First, they need nectar plants with bright, flat flowers like marigolds and zinnias, where adult butterflies sip sweet nectar through their straw-like proboscis. Second, they need host plants with tender green leaves, like curry leaf plants or lemon saplings, where mother butterflies lay eggs so hungry baby caterpillars can hatch and feast. By planting both, your campus becomes a sanctuary of biodiversity.",
        "lecture_script": "The biology of butterfly conservation gardens, distinguishing nectar-providing angiosperms from larval host plants, and the ecological role of insect pollination.",
        "checkpoints": [
            {
                "question": "What is the difference between a nectar plant and a larval host plant in a school butterfly garden?",
                "options": [
                    "Nectar plants are made of plastic while host plants are made of paper",
                    "Nectar plants provide sweet nectar for adult flying butterflies, while host plants provide specific leaves for caterpillars to feed on",
                    "Nectar plants grow only in winter while host plants grow only in water",
                    "There is no difference between them"
                ],
                "correct": 1,
                "explanation": "Adult butterflies sip sugary nectar from open flowers for flight energy, but female butterflies strictly deposit eggs on specific host plants that their caterpillars can digest.",
                "study_insight": "For example, the beautiful Lime Butterfly lays its eggs only on citrus and curry leaf foliage."
            },
            {
                "question": "Why are butterflies and bees considered essential insect allies in nature?",
                "options": [
                    "They eat all the flowers so plants cannot reproduce",
                    "They act as pollinators, transferring pollen between flowers so plants can produce fruits, vegetables, and seeds",
                    "They frighten away birds from school playgrounds",
                    "They turn garden soil into stone"
                ],
                "correct": 1,
                "explanation": "Pollinators transfer pollen from anther to stigma, enabling fertilization and the development of seeds, grains, nuts, and juicy fruits that feed humanity.",
                "study_insight": "Nearly one out of every three bites of food we eat depends directly on insect pollination."
            }
        ]
    }
]


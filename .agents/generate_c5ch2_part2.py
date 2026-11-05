"""
Part 2 Generator for NCERT Class 5 Science - Chapter 2: Journey of a River
Slides 9 to 16:
- Short punchy headings (1-3 words)
- Subtitles
- Rich concept HTML
- Spoken text (Classroom lecture, Indian English narration, NO lecturer names)
- 2 formative checkpoints per slide with instant feedback and study insights
- Zero raw LaTeX (Clean Unicode only)
"""

SLIDES_PART2 = [
    # Slide 9: Dam Trade-Offs
    {
        "id": 9,
        "title": "Dam Trade-Offs",
        "subtitle": "Submergence, Ecological Disruption, and Community Displacement",
        "concept_html": """
            <p class="mb-3">
                While dams provide crucial water storage and electricity, they come with substantial environmental and social consequences. Building a giant reservoir fundamentally alters the river ecosystem:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30">
                    <span class="text-xs font-bold text-rose-300 block mb-1">🌲 Forest Submergence</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Rising reservoir waters drown thousands of hectares of ancient forests, destroying valuable biodiversity and severing ancient wildlife migration corridors.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🏘️ Community Displacement</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Hundreds of historic villages and indigenous tribal settlements are submerged, forcing families to leave ancestral lands, farms, and cultural heritage behind.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                Downstream consequences: River deltas receive less natural silt, causing coastal beaches to erode and blocking migratory fish from swimming upriver to breed.
            </p>
        """,
        "spoken_text": "Dams are marvels of human engineering, but they also bring heartbreak to the natural world. When a colossal dam wall blocks a valley, the rising reservoir waters permanently submerge vast tracts of ancient forests. Thousands of wild animals lose their homes, and natural migration corridors are severed. Even more poignantly, hundreds of rural villages, schools, and indigenous tribal settlements are submerged beneath the lake. Families who have farmed the same soil for generations are displaced and must rebuild their lives elsewhere. Furthermore, dams trap rich mineral silt, starving the fertile delta downstream, and block fish from swimming upriver to spawn. Every dam requires a careful balance between human progress and environmental preservation.",
        "lecture_script": "Dams are marvels of human engineering, but they also bring heartbreak to the natural world...",
        "checkpoints": [
            {
                "question": "What major social and human consequence occurs when a massive reservoir fills behind a newly constructed dam?",
                "options": [
                    "Villages and farmlands are submerged, forcing local communities to relocate and resettle elsewhere",
                    "All people in the valley turn into fish",
                    "The Sun stops shining on the valley",
                    "Gold coins rain down from the sky"
                ],
                "correct": 0,
                "explanation": "Reservoir inundation floods inhabited valleys, requiring the displacement and rehabilitation of entire rural and tribal populations.",
                "study_insight": "Fair compensation and sustainable rehabilitation for displaced communities are critical ethical requirements."
            },
            {
                "question": "How do large dam walls impact aquatic wildlife like migratory fish swimming upstream to spawn?",
                "options": [
                    "They physically block the river channel, preventing fish from migrating to their natural breeding grounds",
                    "They make all fish grow wings and fly",
                    "They turn all freshwater into salt",
                    "They have no impact on fish whatsoever"
                ],
                "correct": 0,
                "explanation": "High concrete walls fragment river ecosystems, preventing migratory species like the Mahseer from swimming upstream to reproduce.",
                "study_insight": "Some modern dams incorporate specialized 'fish ladders' to help fish bypass the barrier."
            }
        ]
    },

    # Slide 10: Murky Currents
    {
        "id": 10,
        "title": "Murky Currents",
        "subtitle": "Domestic Sewage, Plastic Waste, and Factory Effluents",
        "concept_html": """
            <p class="mb-3">
                As a river flows past growing cities and industrial corridors, its crystal-clear mountain waters are severely contaminated by human activity:
            </p>
            <div class="space-y-2.5 my-3">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-amber-300">1. Untreated Domestic Sewage</span>
                        <p class="text-[11px] text-slate-300">Millions of liters of soapy greywater, toilet waste, and detergents discharge directly from municipal storm drains into rivers.</p>
                    </div>
                    <span class="text-lg">🚽</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-rose-300">2. Non-Biodegradable Plastic Garbage</span>
                        <p class="text-[11px] text-slate-300">Single-use polythene bags, packaging wrappers, and plastic bottles float in stagnant eddies, choking aquatic turtles and fish.</p>
                    </div>
                    <span class="text-lg">🥤</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-purple-300">3. Industrial Toxic Effluents</span>
                        <p class="text-[11px] text-slate-300">Chemical dyeing units, tanneries, and factories dump untreated acids, heavy metals (lead, mercury), and dyes into the water.</p>
                    </div>
                    <span class="text-lg">🏭</span>
                </div>
            </div>
            <p class="text-xs text-rose-300 font-medium">
                Polluted rivers become breeding grounds for dangerous pathogens (causing cholera and typhoid) and destroy aquatic life.
            </p>
        """,
        "spoken_text": "Although rivers generously nourish us, we often treat them as open garbage dumps. As the Godavari winds past bustling towns and industrial cities, its crystal-clear water turns dark and foul-smelling. Growing urban populations pour millions of liters of untreated sewage, soapy dishwater, and toxic detergents into the current every day. Careless citizens toss non-biodegradable plastic bottles, polythene bags, and synthetic trash into the water, entangling aquatic creatures. Worst of all, unscrupulous factories dump untreated chemical effluents containing poisonous dyes and heavy metals like mercury and lead. This pollution turns sacred rivers into toxic hazards, poisoning drinking water and suffocating aquatic life.",
        "lecture_script": "Although rivers generously nourish us, we often treat them as open garbage dumps...",
        "checkpoints": [
            {
                "question": "Which of the following pollutants in river water is non-biodegradable and persists in the environment for hundreds of years?",
                "options": [
                    "Single-use plastic bottles and polythene bags",
                    "Fallen tree leaves",
                    "Natural sand grains",
                    "Wooden river driftwood"
                ],
                "correct": 0,
                "explanation": "Plastics are synthetic polymers that bacteria cannot decompose naturally, persisting in waterways for centuries and breaking into microplastics.",
                "study_insight": "Refusing single-use plastics directly protects river ecosystems."
            },
            {
                "question": "What happens to the quality of drinking water when untreated industrial chemicals and sewage are dumped into a river?",
                "options": [
                    "Water becomes contaminated with toxic chemicals and pathogens, spreading waterborne diseases",
                    "Water turns into pure fresh milk",
                    "Water becomes cleaner and tastier",
                    "Water freezes into solid ice instantly"
                ],
                "correct": 0,
                "explanation": "Sewage introduces disease-causing bacteria (cholera, dysentery), while industrial chemicals make water carcinogenic and unsafe for consumption.",
                "study_insight": "Sewage Treatment Plants (STPs) must treat all wastewater before it reaches a river."
            }
        ]
    },

    # Slide 11: Green Blanket
    {
        "id": 11,
        "title": "Green Blanket",
        "subtitle": "Eutrophication, Algal Blooms, and Oxygen Depletion",
        "concept_html": """
            <p class="mb-3">
                Have you ever seen a river or lake whose surface is completely concealed beneath a thick, slimy green mat? This phenomenon is known as an <strong>algal bloom</strong> or the <em>green blanket</em> effect, driven by <strong>eutrophication</strong>:
            </p>
            <div class="space-y-2.5 my-3">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-amber-300">1. Fertilizer Runoff from Farms</span>
                        <p class="text-[11px] text-slate-300">Farmers spray excessive chemical fertilizers (nitrogen and phosphorus) on crops. Monsoon rains wash surplus chemicals into the river.</p>
                    </div>
                    <span class="text-lg">🌾</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-emerald-400">2. Explosive Weed & Algae Growth</span>
                        <p class="text-[11px] text-slate-300">These agricultural nutrients trigger an unnatural population explosion of microscopic algae and invasive water weeds like water hyacinth.</p>
                    </div>
                    <span class="text-lg">🌿</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-rose-400">3. Sun Block & Oxygen Starvation</span>
                        <p class="text-[11px] text-slate-300">The dense mat blocks sunlight from submerged plants. When the algae die, decomposing bacteria consume all dissolved oxygen, suffocating fish!</p>
                    </div>
                    <span class="text-lg">🐟</span>
                </div>
            </div>
            <p class="text-xs text-rose-300 font-medium">
                Dead zones form where dissolved oxygen drops near zero, causing mass fish mortality.
            </p>
        """,
        "spoken_text": "Have you ever looked at a pond or river and seen its surface choked beneath a thick, slimy green mat of weeds and scum? This dangerous condition is called an algal bloom, or eutrophication. It begins on farm fields where farmers apply heavy amounts of synthetic chemical fertilizers rich in nitrogen and phosphorus. When heavy rains arrive, the surplus fertilizer is washed directly into nearby rivers and ponds. In the water, these chemicals act like supercharged plant food, causing algae and invasive water weeds to multiply uncontrollably into a dense green blanket. This thick mat blocks vital sunlight from reaching underwater plants. When the massive mass of algae dies, bacteria decompose it, consuming all the dissolved oxygen in the water. Without oxygen, thousands of fish suffocate and die.",
        "lecture_script": "Have you ever looked at a pond or river and seen its surface choked beneath a thick, slimy green mat...",
        "checkpoints": [
            {
                "question": "What agricultural substance washed into rivers by monsoon rains triggers the explosive growth of the 'green blanket' (algae)?",
                "options": [
                    "Excess chemical fertilizers rich in nitrogen and phosphorus",
                    "Dry autumn leaves",
                    "Pure river stones",
                    "Natural wood shavings"
                ],
                "correct": 0,
                "explanation": "Chemical fertilizers contain concentrated nitrogen and phosphorus compounds that act as intense plant nutrients in aquatic ecosystems.",
                "study_insight": "Organic farming and riparian tree buffers reduce fertilizer runoff into rivers."
            },
            {
                "question": "Why do fish suffocate and die when an overgrown algal bloom dies and decays in a river?",
                "options": [
                    "Decomposing bacteria consume nearly all the dissolved oxygen in the water",
                    "The water turns into boiling oil",
                    "The fish eat too much green ice cream",
                    "The fish lose their fins completely"
                ],
                "correct": 0,
                "explanation": "Aerobic bacteria breaking down dead algae consume massive quantities of dissolved oxygen, creating hypoxic 'dead zones' where fish cannot breathe.",
                "study_insight": "Healthy water has high dissolved oxygen (>6 mg/L); eutrophic water drops to near zero."
            }
        ]
    },

    # Slide 12: River Fury
    {
        "id": 12,
        "title": "River Fury",
        "subtitle": "Monsoon Floods: Causes, Inundation, and Devastation",
        "concept_html": """
            <p class="mb-3">
                During the height of the south-west monsoon, relentless cloudbursts pour millions of tons of water across river catchments. When the volume exceeds the river channel's carrying capacity, the river roars over its banks in a <strong>flood</strong>:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🌊 Destructive Flood Impacts</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li>Submerges rural villages, towns, and low-lying agricultural fields.</li>
                        <li>Destroys standing food crops and washes away farm livestock.</li>
                        <li>Breaches highway bridges and snaps power lines.</li>
                        <li>Contaminates drinking water wells with muddy flood sludge.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-300 block mb-1">🌾 The Silver Lining: Alluvium</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Historically, seasonal gentle river overflows deposit fine mineral silt (alluvial soil) across plains, naturally renewing farm soil fertility for future harvests.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Severe flooding turns catastrophic when humans encroach upon natural floodplains and build concrete structures over natural drainage channels.
            </p>
        """,
        "spoken_text": "During the height of the monsoon, a peaceful river can transform into a roaring torrent of immense power. When torrential cloudbursts lash mountain catchments for days on end, the volume of rushing water overwhelms the river's channel. The river expands dramatically, bursting its banks and inundating low-lying towns, farmlands, and highways. Rushing brown currents sweep away standing crops, breach bridges, flood homes, and displace thousands of families and animals. Drinking water wells are contaminated with muddy silt, creating severe health emergencies. Yet, in nature's grand design, natural seasonal floods also deposit fresh, mineral-rich silt onto valley plains, renewing the fertility of the soil for future years. However, when humans build houses right on the river's floodplain, disaster is inevitable.",
        "lecture_script": "During the height of the monsoon, a peaceful river can transform into a roaring torrent...",
        "checkpoints": [
            {
                "question": "What primary weather event causes rivers to overflow their banks and flood surrounding land?",
                "options": [
                    "Prolonged heavy torrential rainfall across the river catchment",
                    "A mild afternoon breeze",
                    "A full moon in clear skies",
                    "Winter morning frost on grass"
                ],
                "correct": 0,
                "explanation": "Excessive continuous precipitation generates massive runoff that exceeds the volumetric carrying capacity of the river channel.",
                "study_insight": "Deforestation in hills accelerates runoff, turning gentle rain into violent flood surges."
            },
            {
                "question": "What positive agricultural benefit do natural river floods historically bring to valley plains once waters recede?",
                "options": [
                    "They deposit a fresh layer of mineral-rich alluvial silt, naturally renewing soil fertility",
                    "They bury all farmland under solid rock slabs",
                    "They turn all soil into salty ocean sand",
                    "They permanently prevent seeds from germinating"
                ],
                "correct": 0,
                "explanation": "Floodwaters carry fine suspended mineral silt from mountain erosion and spread it over plains, creating nutrient-rich alluvium ideal for farming.",
                "study_insight": "Ancient Egyptian and Harappan civilizations relied entirely on annual river silt deposits."
            }
        ]
    },

    # Slide 13: Forest Shields
    {
        "id": 13,
        "title": "Forest Shields",
        "subtitle": "Roots, Soil Binding, and Natural Flood Mitigation",
        "concept_html": """
            <p class="mb-3">
                Why do rivers originating in dense, pristine forests flood far less violently than those whose catchment hills have been deforested? <strong>Trees are nature's ultimate flood defense shield</strong>:
            </p>
            <div class="space-y-2.5 my-3">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-emerald-300">1. Canopy Interception</span>
                        <p class="text-[11px] text-slate-300">Leaves and tree branches catch torrential raindrops, breaking their momentum and converting violent downpours into gentle drips.</p>
                    </div>
                    <span class="text-lg">🍃</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-amber-300">2. Sponge-like Soil Infiltration</span>
                        <p class="text-[11px] text-slate-300">Spongy organic humus on the forest floor absorbs billions of liters of water, releasing it slowly into streams over weeks instead of hours.</p>
                    </div>
                    <span class="text-lg">🧽</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-cyan-300">3. Root Net Soil Anchoring</span>
                        <p class="text-[11px] text-slate-300">Extensive tree roots bind soil particles tightly like steel rebar in concrete, preventing riverbanks from crumbling and silting up the channel.</p>
                    </div>
                    <span class="text-lg">🌳</span>
                </div>
            </div>
            <p class="text-xs text-emerald-300 font-medium">
                When catchment forests are clear-cut, rainwater rushes down bare slopes within minutes, triggering devastating flash floods!
            </p>
        """,
        "spoken_text": "Nature has engineered its own living shield against devastating floods: trees and forests. When rain hammers down on a forested mountain, the multi-layered tree canopy intercepts the falling drops, breaking their violent momentum. On the forest floor, a thick, spongy blanket of fallen leaves and organic humus soaks up the water like a giant reservoir, allowing it to percolate gently into underground aquifers. Even more importantly, deep, intertwined tree roots grip the soil tightly, acting like living mesh rebar that anchors riverbanks firmly in place. When humans strip hillsides of their forests, this protective sponge vanishes. Rainwater rushes down bare rocks in minutes, carrying tons of mud that silts up the river and triggers catastrophic flash floods.",
        "lecture_script": "Nature has engineered its own living shield against devastating floods: trees and forests...",
        "checkpoints": [
            {
                "question": "How do tree root networks along riverbanks protect surrounding villages from flood devastation?",
                "options": [
                    "They bind soil particles firmly in place, preventing bank erosion and slowing surface runoff",
                    "They drink all the river water until the river disappears",
                    "They turn river water into solid concrete walls",
                    "They push the river backward into the sky"
                ],
                "correct": 0,
                "explanation": "Interlocking root systems physically anchor riverbanks against rushing currents and increase soil porosity so more water infiltrates underground.",
                "study_insight": "Planting trees along riverbanks is the most cost-effective natural flood defense."
            },
            {
                "question": "What disastrous consequence occurs when forested hills in a river catchment are completely cleared of trees?",
                "options": [
                    "Rainwater rushes rapidly down bare slopes, causing devastating flash floods and heavy soil erosion",
                    "The mountains turn into gold nuggets",
                    "The weather becomes permanently rainless forever",
                    "The river begins flowing upside down"
                ],
                "correct": 0,
                "explanation": "Without tree canopies and spongy humus to slow and absorb rainwater, surface runoff speeds up drastically, causing rapid flash floods and mudslides.",
                "study_insight": "Deforestation dramatically increases peak flood discharges."
            }
        ]
    },

    # Slide 14: Flood Safety
    {
        "id": 14,
        "title": "Flood Safety",
        "subtitle": "Essential Preparedness: Before, During, and After a Flood",
        "concept_html": """
            <p class="mb-3">
                Floods are among the most frequent natural disasters in India. Knowing exact safety protocols can save lives and prevent injuries:
            </p>
            <div class="grid grid-cols-3 gap-2 my-3 text-center">
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">1. Before the Flood</span>
                    <p class="text-[11px] text-slate-300">
                        Prepare an Emergency Kit (torch, batteries, clean water, dry food, first-aid, medicines). Keep emergency radio tuned to weather alerts. Move valuables to upper floors.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30">
                    <span class="text-xs font-bold text-rose-300 block mb-1">2. During the Flood</span>
                    <p class="text-[11px] text-slate-300">
                        Evacuate immediately to designated high ground or cyclone shelters. <strong>Never walk or drive through moving floodwaters</strong>—just 15 cm of moving water can knock you down! Switch off main electrical power.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">3. After the Flood</span>
                    <p class="text-[11px] text-slate-300">
                        Drink only boiled or purified water to prevent cholera. Stay away from downed power lines. Watch for venomous snakes that seek dry shelter in flooded homes.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Golden Safety Rule: Turn Around, Don't Drown! Moving water carries invisible debris and collapses roads beneath it.
            </p>
        """,
        "spoken_text": "Floods can strike with startling speed, making preparedness a matter of life and death. Safety protocols are divided into three essential phases. Before a flood, prepare a family emergency disaster kit with a battery-operated torch, fresh drinking water, non-perishable food, and essential medicines. Listen carefully to official weather radio broadcasts. During a flood, evacuate immediately to high ground or government relief shelters. Never, ever attempt to walk, swim, or drive through moving floodwaters—just fifteen centimeters of fast-moving water can sweep an adult off their feet! Switch off home electricity at the main breaker. After floodwaters recede, drink only thoroughly boiled water to prevent deadly waterborne infections, beware of exposed electric wires, and watch for snakes seeking dry refuge inside homes.",
        "lecture_script": "Floods can strike with startling speed, making preparedness a matter of life and death...",
        "checkpoints": [
            {
                "question": "What is the single most critical safety rule when encountering fast-moving floodwaters across a road or bridge?",
                "options": [
                    "Never attempt to walk, swim, or drive through moving floodwaters",
                    "Jump in and try to swim across for fun",
                    "Drink the muddy floodwater immediately",
                    "Wash your school clothes in the flood"
                ],
                "correct": 0,
                "explanation": "Just 15 cm (6 inches) of moving water can sweep an adult off their feet, and 30 cm can float a car. Hidden currents and collapsed roadbeds make wading deadly.",
                "study_insight": "The universal disaster advisory is: 'Turn Around, Don't Drown!'"
            },
            {
                "question": "Why must families drink ONLY boiled or thoroughly disinfected water after returning home following a major flood?",
                "options": [
                    "Floodwaters contaminate open wells and water pipelines with sewage and deadly waterborne pathogens",
                    "Boiling water turns it into gasoline",
                    "Because cold water creates earthquakes",
                    "Boiling water makes it disappear completely"
                ],
                "correct": 0,
                "explanation": "Floods wash sewage, animal carcasses, and mud into drinking water supplies, spreading lethal waterborne epidemics like cholera, typhoid, and hepatitis.",
                "study_insight": "Boiling water rolling for at least 1 minute kills virtually all pathogenic bacteria and viruses."
            }
        ]
    },

    # Slide 15: Dry Riverbed
    {
        "id": 15,
        "title": "Dry Riverbed",
        "subtitle": "Water Scarcity Crises & The 2019 Chennai Water Train",
        "concept_html": """
            <p class="mb-3">
                The opposite of a flood is equally terrifying: when rivers, reservoirs, and wells completely run dry. Across India, over-extraction, climate change, and delayed monsoons trigger acute <strong>water scarcity crises</strong>:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🚂 The 2019 Chennai Water Train</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        In the summer of 2019, four major reservoirs supplying Chennai dried up completely ("Day Zero"). Indian Railways deployed special <strong>Jaldoot water trains</strong> carrying 2.5 million liters per trip from Jolarpettai (over 200 km away) to quench the city's thirst!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30">
                    <span class="text-xs font-bold text-rose-300 block mb-1">⚠️ Impacts of Water Distress</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Families stand in kilometers-long queues for private water tankers; schools shut down due to lack of sanitation; farmers suffer total crop failure, forcing mass distress migration to slums.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                Water scarcity is not a distant future nightmare; it is a reality that occurs whenever we consume groundwater faster than nature can recharge it.
            </p>
        """,
        "spoken_text": "While a flooding river is terrifying, an empty, dry riverbed is equally devastating. In recent summers, prolonged droughts, vanishing forests, and reckless over-pumping of groundwater have pushed major Indian cities to the brink of Day Zero—when taps completely run dry. In the scorching summer of 2019, all four major drinking water reservoirs supplying the metropolis of Chennai dried up into cracked dust. The crisis was so severe that Indian Railways had to deploy special water trains, each carrying two and a half million liters of fresh water across hundreds of kilometers from Jolarpettai just to keep hospitals and citizens alive. Families waited in grueling lines under the sun for hours with plastic pots. This historic crisis was a stark wake-up call for the entire nation.",
        "lecture_script": "While a flooding river is terrifying, an empty, dry riverbed is equally devastating...",
        "checkpoints": [
            {
                "question": "What extraordinary emergency transport measure did Indian Railways deploy during the severe 2019 water crisis in Chennai?",
                "options": [
                    "Special 'Jaldoot' water trains transporting millions of liters of drinking water from hundreds of kilometers away",
                    "Flying hot air balloons carrying ice blocks",
                    "Submarines sailing across dry city streets",
                    "Underground rockets pumping sea salt"
                ],
                "correct": 0,
                "explanation": "Special railway tanker wagons transported 2.5 to 5 million liters of drinking water daily from Jolarpettai in Vellore to Chennai during the acute 2019 drought.",
                "study_insight": "Water trains demonstrate how acute municipal drought can become when local reservoirs run dry."
            },
            {
                "question": "What primary human factor accelerates the drying up of rivers and municipal water crises across peninsular India?",
                "options": [
                    "Reckless over-extraction of groundwater through borewells and destruction of catchment forests",
                    "Planting too many mango trees in orchards",
                    "Building too many public libraries",
                    "Painting houses white in summer"
                ],
                "correct": 0,
                "explanation": "Uncontrolled borewell drilling without rainwater harvesting, combined with deforestation in river catchments, drains aquifers and dries up baseflow.",
                "study_insight": "Healthy river baseflow depends directly on recharged groundwater aquifers."
            }
        ]
    },

    # Slide 16: Water Guardians
    {
        "id": 16,
        "title": "Water Guardians",
        "subtitle": "National Water Mission, Water ATMs, and Daily Conservation",
        "concept_html": """
            <p class="mb-3">
                To secure our water future, India has launched visionary national programs alongside community-level technologies:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-300 block mb-1">🏛️ National Water Mission</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Key initiative under the National Action Plan on Climate Change: <em>"Catch the Rain, Where it Falls, When it Falls."</em> Aims to increase water efficiency by 20% through mandatory rainwater harvesting and recycling.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">💳 Automated Water ATMs</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Solar-powered dispensing kiosks installed in rural and urban areas. Citizens swipe a smart card or drop a coin to obtain clean, purified RO drinking water at low cost, eliminating plastic bottle waste.
                    </p>
                </div>
            </div>
            <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 space-y-1 text-xs text-slate-300">
                <span class="font-bold text-emerald-300 block">Personal Water-Wise Pledges:</span>
                <p>• <strong>Turn off taps</strong> while brushing teeth or soaping hands (saves ~15 liters per person daily).</p>
                <p>• <strong>Fix leaky washers</strong> promptly (one dripping tap wastes 2,000+ liters every year).</p>
                <p>• <strong>Reuse kitchen wash water</strong> (water used for rinsing rice, dal, and vegetables is excellent for garden plants).</p>
            </div>
        """,
        "spoken_text": "To protect our rivers and ensure clean drinking water for every child, India has embraced progressive conservation solutions. The National Water Mission champions the powerful motto: Catch the rain, where it falls, when it falls. Across villages and railway stations, smart automated Water ATMs have been installed. By inserting a small coin or swiping a prepaid card, citizens can collect chilled, pure drinking water into their own reusable containers, eliminating tons of plastic pollution. But the greatest guardians of water are you and me. By making simple conscious choices—turning off running taps while brushing, repairing dripping faucets, and reusing kitchen vegetable wash water for potted plants—we each save thousands of liters every year. Protecting our rivers begins with the very drops we touch at home.",
        "lecture_script": "To protect our rivers and ensure clean drinking water for every child...",
        "checkpoints": [
            {
                "question": "What is an automated 'Water ATM' installed in public places and rural areas designed to do?",
                "options": [
                    "Dispense pure, safe drinking water at low cost when a coin or smart card is used",
                    "Print paper currency notes out of river mud",
                    "Dispense hot vegetable soup for free",
                    "Wash railway trains with sparkling water"
                ],
                "correct": 0,
                "explanation": "Water ATMs are decentralized water purification kiosks that dispense affordable, safe drinking water, reducing waterborne illness and plastic waste.",
                "study_insight": "Water ATMs eliminate the need to purchase single-use plastic bottled water."
            },
            {
                "question": "What is the famous national conservation slogan of the National Water Mission?",
                "options": [
                    "'Catch the Rain, Where it Falls, When it Falls'",
                    "'Pour all rainwater into the ocean quickly'",
                    "'Cover all rivers with concrete ceilings'",
                    "'Use water without thinking'"
                ],
                "correct": 0,
                "explanation": "The 'Catch the Rain' campaign emphasizes decentralised rooftop and community rainwater harvesting across all agro-climatic zones in India.",
                "study_insight": "Capturing rain where it falls minimizes runoff and maximizes local aquifer recharge."
            }
        ]
    }
]


"""
Data generator for NCERT Class 5 Science Chapter 4: Our School - A Happy Place - Part 2 (Slides 9 to 16)
Zero lecturer names. Indian male voice priority. Short punchy headings (1-3 words).
Zero raw LaTeX.
"""

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Gate Safety",
        "subtitle": "Road Safety, Pedestrian Crossings & Calming School Zone Traffic",
        "concept_html": """
            <p>During morning arrival and afternoon dismissal, the area immediately outside the school gate becomes a bustling storm of auto-rickshaws, school buses, bicycles, parents on scooters, and walking children.</p>
            <div class="my-3 p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200 text-xs">
                ⚠️ <strong>The Danger Zone:</strong> Road accidents occur when drivers speed carelessly or pedestrians cross without looking. Establishing strict <strong>School Zone Safety Protocols</strong> protects young lives.
            </div>
            <p>Essential safety rules around the school gate:</p>
            <ul class="mt-2 space-y-1.5 text-xs text-slate-300">
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">1.</span>
                    <span><strong>School Speed Limit (20 km/h):</strong> Vehicles must crawl at low speeds near school gates to ensure drivers can brake instantly.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">2.</span>
                    <span><strong>Use the Footpath (Sidewalk):</strong> Walk on elevated pedestrian paths; never run into moving traffic or weave between parked buses.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">3.</span>
                    <span><strong>Stop, Look & Listen:</strong> Before stepping onto the road: Look right, look left, look right again. Cross only when traffic is completely clear.</span>
                </li>
            </ul>
        """,
        "spoken_text": "Every morning, the street outside our school gate fills with speeding cars, buses, and hundreds of walking children. Road accidents happen when people ignore traffic rules or rush carelessly. The Traffic Trackers remind us that school gates must be safe zones. Vehicles must slow down to twenty kilometers per hour. When walking, always stay on the raised footpath. Never sprint into the street or dart between parked vans. When crossing, look right, look left, and look right again, crossing calmly only when vehicles have come to a complete stop.",
        "lecture_script": "Pedestrian safety engineering around school zones, speed calming protocols, vehicle-pedestrian conflict zones, and defensive crossing rules.",
        "checkpoints": [
            {
                "question": "What is the recommended maximum driving speed limit for motor vehicles traveling through a designated school zone?",
                "options": [
                    "80 km/h for rapid clearance",
                    "20 to 25 km/h to allow drivers to stop instantly if a child steps forward",
                    "120 km/h on express lanes",
                    "Zero speed, vehicles must be pushed by hand"
                ],
                "correct": 1,
                "explanation": "Strict speed limits (20-25 km/h) in school zones drastically reduce vehicle stopping distance and prevent fatal collisions with pedestrians.",
                "study_insight": "A car moving at 20 km/h can stop within 6 meters, whereas a car speeding at 50 km/h takes nearly 25 meters to come to a halt."
            },
            {
                "question": "What is the golden rule every student must practice before crossing any roadway?",
                "options": [
                    "Close your eyes and run as fast as possible across the asphalt",
                    "Look right, look left, look right again, listen for horns, and cross only when traffic is clear",
                    "Look only at your mobile phone screen while stepping off the curb",
                    "Wave your arms and expect all moving trucks to vanish"
                ],
                "correct": 1,
                "explanation": "The defensive crossing sequence (Look Right, Look Left, Look Right Again in India's left-side drive system) ensures full awareness of oncoming traffic.",
                "study_insight": "Always cross at designated zebra crossings where drivers expect pedestrians to cross."
            }
        ]
    },
    {
        "id": 10,
        "title": "Traffic Signs",
        "subtitle": "Deciphering Mandatory, Cautionary & Informatory Road Signboards",
        "concept_html": """
            <p>Road signs are the universal language of transportation. Designed using standardized geometric shapes and colors, they alert, guide, and protect commuters across the country:</p>
            <div class="my-3 grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200">
                    <span class="text-base block mb-1">🛑</span>
                    <strong class="text-rose-300 block">Mandatory (Red Circle)</strong>
                    Orders what you MUST or MUST NOT do (e.g., Stop, No Entry, Speed Limit 20).
                </div>
                <div class="p-2 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200">
                    <span class="text-base block mb-1">⚠️</span>
                    <strong class="text-amber-300 block">Cautionary (Triangle)</strong>
                    Warns of upcoming hazards ahead (e.g., School Ahead, Sharp Curve, Pedestrian Crossing).
                </div>
                <div class="p-2 rounded-xl bg-sky-950/40 border border-sky-500/30 text-sky-200">
                    <span class="text-base block mb-1">ℹ️</span>
                    <strong class="text-sky-300 block">Informatory (Blue Box)</strong>
                    Gives helpful directions and facilities (e.g., Hospital, Public Telephone, Bus Stop).
                </div>
            </div>
            <div class="mt-3 p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                🦓 <strong>The Zebra Crossing:</strong> Broad black and white alternating stripes painted across roads. Drivers must stop before the stop line to let pedestrians cross safely.
            </div>
        """,
        "spoken_text": "Road signs speak an international language of shapes and colors. Red circular signs are mandatory rules that every driver must obey by law, such as Stop or Speed Limit Twenty. Yellow or white triangular signs with red borders are cautionary warnings, alerting drivers to slow down because a school, speed breaker, or sharp bend lies ahead. Blue rectangular signs are informatory guides showing hospitals, bus stops, and parking. Broad black-and-white zebra stripes give pedestrians a safe corridor where traffic must yield.",
        "lecture_script": "The typology of road traffic signs: circular regulatory signs, triangular warning signs, rectangular informatory signs, and zebra crossing right-of-way regulations.",
        "checkpoints": [
            {
                "question": "What geometric shape and color are universally used for cautionary (warning) traffic signs like 'School Ahead'?",
                "options": [
                    "Green circles with pink borders",
                    "Equilateral triangles pointing upward with bold red borders and yellow/white background",
                    "Black stars with neon green dots",
                    "Blue squares with wavy lines"
                ],
                "correct": 1,
                "explanation": "Triangular signs with red borders are universally used as warning signs to prepare drivers for road hazards, pedestrian crossings, and school zones ahead.",
                "study_insight": "The triangular shape catches the peripheral vision of drivers faster than rectangular shapes."
            },
            {
                "question": "What is the legal duty of a motor vehicle driver approaching a painted zebra crossing with pedestrians waiting?",
                "options": [
                    "Honk loudly and accelerate through the stripes",
                    "Slow down and stop completely before the stop line to allow pedestrians to cross safely",
                    "Switch off headlights and close eyes",
                    "Park the car directly on top of the zebra stripes"
                ],
                "correct": 1,
                "explanation": "Under traffic law, pedestrians have absolute right-of-way on zebra crossings. Drivers must stop before the crossing until pedestrians have crossed safely.",
                "study_insight": "Never overtake another vehicle that has stopped at a zebra crossing, as pedestrians may be crossing in front of it."
            }
        ]
    },
    {
        "id": 11,
        "title": "Fire Drill",
        "subtitle": "Emergency Preparedness: Alarms, Calm Evacuation & Assembly Points",
        "concept_html": """
            <p>Suddenly, a piercing, continuous alarm siren rings throughout the corridors! A smoke alarm has triggered in the science lab. Is it time to scream and run? <strong>NO! Panic is the greatest danger in an emergency.</strong></p>
            <div class="my-3 p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200 text-xs">
                🚨 <strong>The Golden Fire Drill Rule:</strong> Move quickly, stay calm, do not run, do not scream, do not collect personal belongings, and follow designated evacuation routes immediately.
            </div>
            <p>The 4-Step School Evacuation Routine:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">1. Stop & Listen</strong>
                    Cease all classroom activities instantly. Leave school bags, water bottles, and books behind.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-rose-400 block mb-1">2. Single-File Evacuation</strong>
                    Walk briskly in a single line down staircases; hold handrails and never push or shove.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">3. Assembly Point</strong>
                    Head directly to the open football ground or central courtyard away from buildings and power lines.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-emerald-400 block mb-1">4. Roll Call & Headcount</strong>
                    Stand quietly in your class line so teachers can take attendance and ensure every student is safe.
                </div>
            </div>
        """,
        "spoken_text": "When the loud fire alarm shrieks, your heart might race. But panic is your worst enemy! Fire drills teach our bodies how to react calmly and safely. When the alarm sounds, drop your pencil, leave your heavy school bag behind, and stand up quietly. Form a single file line. Walk briskly toward the emergency exit without running, pushing, or screaming. Never take elevators or hide in bathrooms. Head straight to the designated assembly point on the open playground, where class teachers take roll call to ensure every friend is accounted for.",
        "lecture_script": "Emergency response procedures during school fire incidents: alarm recognition, calm single-file evacuation, avoiding stair stampedes, and muster point roll call protocols.",
        "checkpoints": [
            {
                "question": "What is the single most important rule of personal conduct when a school fire alarm rings?",
                "options": [
                    "Scream at the top of your lungs and sprint blindly down hallways",
                    "Stay calm, do not panic, leave school bags behind, and walk quickly in a single line toward emergency exits",
                    "Run back to your desk to find lost pencil sharpeners",
                    "Lock the classroom door and hide under benches"
                ],
                "correct": 1,
                "explanation": "Panic, screaming, and rushing cause dangerous stampedes. Walking briskly and calmly ensures an orderly, fast evacuation without tripping or injuries.",
                "study_insight": "Never stop to gather heavy school bags; human life is infinitely more valuable than books or stationery."
            },
            {
                "question": "Where should students assemble immediately after evacuating a school building during a fire emergency?",
                "options": [
                    "In the narrow school basement",
                    "At the pre-designated open assembly point (like the sports field) well away from buildings and glass windows",
                    "Inside locked washrooms",
                    "Under wooden staircases"
                ],
                "correct": 1,
                "explanation": "An open assembly ground provides safety from falling debris, shattering window glass, and intense smoke, while allowing teachers to conduct an accurate headcount.",
                "study_insight": "Never leave the assembly area without telling your teacher, or rescue teams might risk their lives searching for you inside a burning building."
            }
        ]
    },
    {
        "id": 12,
        "title": "Smoke Crawl",
        "subtitle": "Toxic Smoke Physics: Why Hot Smoke Rises & How to Crawl Low",
        "concept_html": """
            <p>During a building fire, flames are not the only danger—<strong>smoke and toxic fumes</strong> are often far more dangerous! Fire consumes atmospheric oxygen and generates suffocating carbon monoxide and soot particles.</p>
            <div class="my-3 p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-rose-200 text-xs">
                🔥 <strong>Thermal Convection Physics:</strong> Hot smoke, burning gases, and poisonous fumes are less dense than room air, so they naturally rise and form a dense, blinding blanket near the ceiling!
            </div>
            <p>The Life-Saving "Crawl Low under Smoke" Technique:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">🧎 Get Down on Hands & Knees</strong>
                    The cleanest, coolest, breathable air is located in the bottom 30 to 60 cm zone right above the floor.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">🧣 Cover Mouth & Nose</strong>
                    Use a handkerchief, sleeve, or cloth (dampened with water if possible) to filter out soot particles.
                </div>
            </div>
            <div class="mt-2 p-2 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-400">
                🛑 <strong>Never Hide:</strong> Never hide inside cupboards, closets, or under beds. Firefighters in heavy gear need to find you quickly!
            </div>
        """,
        "spoken_text": "Did you know that during a fire, smoke is often far more dangerous than the flames themselves? When materials burn, they create thick black smoke and poisonous gases. Because hot air is light, boiling smoke rises rapidly, collecting like a thick blanket against the ceiling. If you walk upright, you will breathe in scorching, toxic fumes. The life-saving secret is to get down on your hands and knees! The coolest, cleanest, breathable air remains down near the floor. Cover your nose and mouth with a cloth, crawl low under the smoke, and make your way to safety.",
        "lecture_script": "Thermal buoyancy of combustion gases, inhalation injury hazards of carbon monoxide and particulates, and the biomechanics of the low-smoke crawl technique.",
        "checkpoints": [
            {
                "question": "Why must you drop to your hands and knees and crawl low if a corridor fills with thick fire smoke?",
                "options": [
                    "Because crawling is a fun game during drills",
                    "Hot, poisonous smoke and toxic gases rise toward the ceiling, leaving the cleanest, coolest air in a 30 to 60 cm layer near the floor",
                    "To hide from the fire alarm sirens",
                    "Because classroom doors are only 50 cm high"
                ],
                "correct": 1,
                "explanation": "Thermal convection causes superheated smoke and lethal gases to rise toward the ceiling. The air closest to the floor is cooler, has more oxygen, and allows clear vision.",
                "study_insight": "Just two or three breaths of dense, hot toxic smoke can cause a person to lose consciousness."
            },
            {
                "question": "Why is it strictly forbidden to hide inside closets, cupboards, or washrooms during a building fire?",
                "options": [
                    "Closets are reserved for textbooks only",
                    "Hiding traps you in confined spaces without escape exits, making it extremely difficult for firefighters to locate and rescue you",
                    "Washrooms have no electric lights",
                    "Cupboards make fires spread twice as fast"
                ],
                "correct": 1,
                "explanation": "Firefighters wearing heavy masks and air tanks search rooms quickly. Hiding in enclosed closets or under furniture delays rescue while smoke fills the room.",
                "study_insight": "Always move toward an exit. If an exit is blocked, stay near a window and wave a bright cloth to signal firefighters."
            }
        ]
    },
    {
        "id": 13,
        "title": "Kind Actions",
        "subtitle": "Behaviour, Empathy & Civic Stewardship in School Life",
        "concept_html": """
            <p>What transforms a concrete school building into a warm, joyful community? It is the small, everyday choices we make in how we treat our friends, teachers, and shared environment. <strong>What we do matters!</strong></p>
            <div class="my-3 p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-indigo-200 text-xs">
                💖 <strong>The Power of Everyday Empathy:</strong> Empathy means stepping into someone else\'s shoes—feeling what they feel and acting with kindness and fairness.
            </div>
            <p>Everyday actions that cultivate collective well-being:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">Queue Courtesy</strong>
                    Wait patiently in line at the water cooler, library, and canteen. Take turns without pushing.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-emerald-400 block mb-1">Property Stewardship</strong>
                    Never scratch or scribble graffiti on wooden desks, walls, or library books. Preserve school heritage.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">Inclusive Games</strong>
                    Invite classmates standing alone on the playground sidelines to join sports and group activities.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-rose-400 block mb-1">Gentle Words</strong>
                    Use "Please", "Thank you", and "Sorry" freely. Praise a friend\'s effort and celebrate their success.
                </div>
            </div>
        """,
        "spoken_text": "What makes a school truly feel like a happy second home? It is not the size of the building or the color of the paint. It is how we treat each other every single day. When you wait patiently in line at the drinking water tap instead of pushing, everyone feels respected. When you refuse to scribble on wooden desks, you protect our shared heritage for future younger students. When you invite a shy classmate who is standing alone to join your football game, you build a circle of empathy and friendship. Every kind act creates ripples of happiness across the entire school.",
        "lecture_script": "The social-emotional foundation of positive school climate: pro-social behavior, empathy, public property stewardship, and inclusive peer culture.",
        "checkpoints": [
            {
                "question": "Which of the following student behaviors directly contributes to a respectful, peaceful, and happy school environment?",
                "options": [
                    "Scribbling graffiti with permanent markers across library books and wooden desks",
                    "Waiting patiently in queue, sharing playground equipment, and inviting lonely peers to play",
                    "Pushing younger students in the lunch line",
                    "Leaving running water taps on in restrooms"
                ],
                "correct": 1,
                "explanation": "Queue discipline, sharing, public property respect, and inclusive friendliness foster mutual trust and emotional safety across the campus.",
                "study_insight": "School furniture and library books are shared community treasures; preserving them demonstrates civic maturity."
            },
            {
                "question": "What is the meaning of practicing 'empathy' in our daily interactions with classmates?",
                "options": [
                    "Making fun of friends who make mistakes in class",
                    "Understanding and sharing the feelings of another person, and treating them with kindness and fairness",
                    "Refusing to speak with anyone who does not sit next to you",
                    "Demanding that everyone agree with your opinion"
                ],
                "correct": 1,
                "explanation": "Empathy is the emotional ability to understand what someone else is going through and offering compassionate support.",
                "study_insight": "Practicing empathy prevents teasing and bullying, ensuring that school remains a joyful sanctuary for all."
            }
        ]
    },
    {
        "id": 14,
        "title": "Inclusive Care",
        "subtitle": "Universal Accessibility: Ramps, Tactile Paving & Welcoming Every Friend",
        "concept_html": """
            <p>Imagine arriving at school using a wheelchair, only to find three steep concrete steps at the main entrance with no ramp. How would that feel? A truly happy school is an <strong>inclusive school</strong> where physical barriers are eliminated.</p>
            <div class="my-3 p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-xs">
                ♿ <strong>Universal Accessibility (RPwD Act Principles):</strong> Every child, regardless of physical or sensory abilities, has the fundamental right to navigate school buildings independently and with dignity.
            </div>
            <p>Essential components of an inclusive campus:</p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-cyan-400 block mb-1">♿ Gentle Ramps & Handrails</strong>
                    Smooth, non-slip entry ramps beside staircases allowing wheelchair users and injured friends to enter easily.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-amber-400 block mb-1">🟡 Tactile Guiding Tiles</strong>
                    Textured yellow floor tiles with raised bumps and lines guiding visually challenged students safely through corridors.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-emerald-400 block mb-1">🚻 Accessible Restrooms</strong>
                    Wide doors, sturdy grab bars, and low washbasins accessible to all physical body types.
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300">
                    <strong class="text-indigo-400 block mb-1">🤝 Peer Buddy Support</strong>
                    Offering assistance willingly—carrying books or walking alongside friends who need a steady hand.
                </div>
            </div>
        """,
        "spoken_text": "Imagine wanting to join your friends in the science lab, but being blocked by a tall flight of stairs because you use crutches or a wheelchair. A happy school leaves no child behind! Inclusive architecture means designing our school so that everyone can move freely and independently. Gentle concrete ramps with handrails allow wheelchair users to enter every classroom. Textured tactile paths on corridor floors guide friends with visual impairments safely. True inclusion also lives in our hearts, through buddy support and warm encouragement that embraces every single student.",
        "lecture_script": "The principles of universal accessibility, barrier-free built environment (ramps, tactile paving, accessible sanitation), and peer buddy inclusion.",
        "checkpoints": [
            {
                "question": "Why should every school building feature gentle ramps with handrails alongside staircases?",
                "options": [
                    "To allow bicycle racing inside classroom hallways",
                    "To ensure students using wheelchairs, crutches, or recovering from injuries can enter buildings independently and safely",
                    "To make rainwater flow into classrooms faster",
                    "To prevent teachers from using stairs"
                ],
                "correct": 1,
                "explanation": "Ramps provide barrier-free mobility, ensuring children with physical disabilities or temporary injuries can access educational spaces with dignity.",
                "study_insight": "A ramp should have a gentle gradient (slope) of at least 1:12 so a wheelchair user can roll up comfortably without tipping."
            },
            {
                "question": "What is the purpose of the yellow textured tiles with raised lines and bumps installed along school corridors?",
                "options": [
                    "They are decorative stickers that glow in the dark",
                    "They provide tactile pathways that visually impaired students can feel with their shoes or walking canes to navigate safely",
                    "They warn students that the floor is permanently broken",
                    "They show where teachers are standing"
                ],
                "correct": 1,
                "explanation": "Tactile paving uses raised straight lines to indicate safe walking paths and raised blister dots to warn of upcoming stairs, doors, or turns for visually impaired pedestrians.",
                "study_insight": "Tactile pathways allow students with blindness to navigate entire school campuses with full independence."
            }
        ]
    },
    {
        "id": 15,
        "title": "Energy Savers",
        "subtitle": "Conservation Habits: Natural Daylighting, Idle Loads & Solar Energy",
        "concept_html": """
            <p>Thermal power plants burn hundreds of tons of fossil fuel coal to generate electricity, releasing greenhouse gases that warm our planet. Conserving electricity on our school campus directly protects the Earth\'s climate!</p>
            <div class="my-3 p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200 text-xs">
                💡 <strong>The Energy Savers' Motto:</strong> "A unit of electricity saved at the switch is more valuable than a unit generated at a polluting power station!"
            </div>
            <p>Smart energy conservation habits for every student:</p>
            <ul class="mt-2 space-y-1.5 text-xs text-slate-300">
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">1.</span>
                    <span><strong>Harness Natural Daylighting:</strong> Open curtains and windows on bright sunny mornings; use sunshine instead of burning artificial tube lights.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">2.</span>
                    <span><strong>Switch Off During Breaks:</strong> Assign a classroom energy monitor to turn off all ceiling fans and lights before leaving for assembly, sports, or lunch.</span>
                </li>
                <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold shrink-0">3.</span>
                    <span><strong>Eliminate Standby Loads:</strong> Turn off computer lab monitors, smartboards, and audio speakers at the wall plug; avoid vampire power drain.</span>
                </li>
            </ul>
        """,
        "spoken_text": "Did you know that most of the electricity powering our fans and lights comes from burning coal in distant power plants? Every time a fan spins in an empty room, fossil fuels are burned and smoke enters our atmosphere. The Electricity Savers remind us of our power to make a difference. On bright sunny mornings, slide open the curtains and let golden sunlight illuminate your notebooks. Whenever your class leaves for recess or sports, flip the switches off. Turning off idle appliances at the plug stops silent energy drain, keeping our air clean and our campus green.",
        "lecture_script": "Electrical energy conservation, fossil fuel thermal generation impacts, natural daylight harvesting, phantom standby load elimination, and student energy audits.",
        "checkpoints": [
            {
                "question": "What is an immediate environmental benefit of switching off lights and fans in empty school classrooms?",
                "options": [
                    "It makes the classroom colder than the North Pole",
                    "It reduces electricity consumption, decreasing coal burning at power plants and cutting harmful air pollution",
                    "It turns electrical cables into copper water pipes",
                    "It stops the sun from shining outside"
                ],
                "correct": 1,
                "explanation": "Saving electricity directly reduces the demand on thermal power grids, cutting coal combustion and greenhouse gas emissions.",
                "study_insight": "If every school in a city turned off lights during recess, megawatts of clean energy would be saved every single hour."
            },
            {
                "question": "What is 'daylight harvesting' in classroom design?",
                "options": [
                    "Catching sunlight in glass jars to sell at markets",
                    "Opening curtains and large windows to utilize free, natural solar light instead of turning on electric tube lights",
                    "Planting wheat inside school desks",
                    "Covering windows with dark cardboard during sunny mornings"
                ],
                "correct": 1,
                "explanation": "Daylight harvesting relies on architectural natural lighting. Utilizing daylight saves electricity, reduces eye strain, and improves students' focus and mood.",
                "study_insight": "Natural daylight provides full-spectrum light that stimulates healthy circadian alertness in growing children."
            }
        ]
    },
    {
        "id": 16,
        "title": "Happiness Tree",
        "subtitle": "Reflective Action: Cultivating Gratitude, Kindness & Eco-Pledges",
        "concept_html": """
            <p>To conclude their environmental and social investigation, Aasha, Mohit, and their classmates constructed a magnificent <strong>Happiness Tree</strong> on a large recycled bulletin board in the central hallway.</p>
            <div class="my-3 p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-xs">
                🌳 <strong>The Happiness Tree Tradition:</strong> A bare painted tree trunk that grows hundreds of colorful paper leaves, each inscribed with a real act of kindness, an eco-action, or a note of heartfelt gratitude.
            </div>
            <p>Categories of leaves that bring the tree to life:</p>
            <div class="mt-3 grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🍃</span>
                    <strong class="text-emerald-400 block">Eco Pledges</strong>
                    "I fixed a dripping tap", "I brought a reusable cloth napkin", "I watered the neem sapling".
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">💖</span>
                    <strong class="text-rose-400 block">Kindness Acts</strong>
                    "I helped a classmate pick up dropped pencils", "I shared my crayons with a friend".
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-base block mb-1">🙏</span>
                    <strong class="text-amber-400 block">Gratitude Notes</strong>
                    "Thank you to our school bus driver", "Thank you to the bhaiya who cleans our hallway".
                </div>
            </div>
        """,
        "spoken_text": "To celebrate their journey, the students created a magnificent Happiness Tree in the school corridor. They started with a painted brown trunk on recycled paper. Every time a student performed a kind action, planted a sapling, or thanked a sanitation worker, they wrote it on a green paper leaf and pinned it to the branches. Within weeks, the bare tree bloomed into a dense canopy of kindness, gratitude, and sustainability. Our school becomes a happy place through the choices we make every day. Together, we can make every corner of our campus safe, green, and joyful.",
        "lecture_script": "Social-emotional synthesis through the Happiness Tree project: gratitude expression, collective eco-commitments, positive school culture, and student agency.",
        "checkpoints": [
            {
                "question": "What does each paper leaf on the school's 'Happiness Tree' represent?",
                "options": [
                    "A list of test marks and exam ranks",
                    "A real student act of kindness, an environmental conservation pledge, or a note of gratitude to campus workers",
                    "A price tag for purchasing school uniforms",
                    "A complaint about rainy weather"
                ],
                "correct": 1,
                "explanation": "The Happiness Tree serves as a visual celebration of positive contributions—recognizing kindness, environmental action, and gratitude across the school community.",
                "study_insight": "Displaying collective positive actions encourages peer emulation, inspiring other students to practice kindness daily."
            },
            {
                "question": "What is the overarching lesson learned by Aasha and Mohit during their school environment exploration?",
                "options": [
                    "Students should never care about what happens outside their classrooms",
                    "A happy and sustainable school is created through collective responsibility, empathy, conservation, and daily kind actions",
                    "Only adult engineers can keep a school clean and safe",
                    "School happiness depends entirely on the size of the computer screens"
                ],
                "correct": 1,
                "explanation": "Every student holds the power to shape school culture through daily mindful habits—saving resources, practicing safety, welcoming friends, and caring for nature.",
                "study_insight": "True environmental education is not just memorizing facts, but taking active responsibility for the world around us."
            }
        ]
    }
]


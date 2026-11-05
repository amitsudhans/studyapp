"""
NCERT Class 6 Science Curiosity - Chapter 7: Temperature and its Measurement
Data Module: 16 Concept Slides (with Full Classroom Audio Lectures & 32 Checkpoints) + 40 Mastery Assessment Questions
Zero raw LaTeX - Pure Unicode formatting (°C, °F, K).
Zero lecturer persona names.
"""

CHAPTER_META = {
    "chapter_num": 7,
    "title": "Temperature and its Measurement",
    "subtitle": "Thermal Sensation, Thermometric Physics, and Precision Measurement",
    "grade": "Grade 6 Science",
    "curriculum": "NCERT Curiosity (NEP 2020)",
    "total_slides": 20,
    "total_checkpoints": 32,
    "total_quiz_questions": 40
}

# 16 High-Yield Concept Slides
SLIDES = [
    {
        "id": 1,
        "title": "Touch vs Tool",
        "subtitle": "The Human Touch Sensation vs Reliable Scientific Measurement",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Imagine coming home from a cold rain in Shillong feeling exhausted and warm. If someone places their palm on your forehead, they might wonder: <em>"Do you have a fever, or is your forehead just warm from walking?"</em>
                </p>
                <div class="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700/80 space-y-2">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">The Sensory Dilemma</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Touching a forehead with a hand only tells us whether one surface is warmer or cooler than the examiner's own skin. If the examiner has cold hands, even a normal forehead feels feverish!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">The Need for an Objective Tool:</strong> To make an accurate medical diagnosis, we cannot guess based on touch. We require a calibrated, scientific measuring instrument: the <strong class="text-emerald-300">thermometer</strong>.
                </div>
            </div>
        """,
        "lecture_script": "Welcome to Temperature and its Measurement! Imagine walking home on a chilly evening in Shillong. Your cheeks feel flushed and you think you might have caught a fever. A family member places a hand on your forehead and says you feel warm. But can we trust this touch? What if the person touching you just came in from washing dishes in cold water? To their cold palm, your perfectly healthy skin will feel scorching hot! Conversely, if someone with hot hands touches you, your fever might go completely unnoticed. Human skin is an organ of sensation, not a calibrated scientific instrument. To determine true thermal state without bias, we must replace subjective touch with an objective measurement tool: the thermometer.",
        "spoken_text": "Welcome to Temperature and its Measurement! Imagine walking home on a chilly evening in Shillong. Your cheeks feel flushed and you think you might have caught a fever. A family member places a hand on your forehead and says you feel warm. But can we trust this touch? What if the person touching you just came in from washing dishes in cold water? To their cold palm, your perfectly healthy skin will feel scorching hot! Conversely, if someone with hot hands touches you, your fever might go completely unnoticed. Human skin is an organ of sensation, not a calibrated scientific instrument. To determine true thermal state without bias, we must replace subjective touch with an objective measurement tool: the thermometer.",
        "checkpoints": [
            {
                "question": "Why is touching someone's forehead with your hand an unreliable method to verify whether they have a medical fever?",
                "options": [
                    "Because our sense of touch is subjective and depends on how hot or cold our own hand is",
                    "Because human hands emit magnetic waves that erase body heat",
                    "Because touch changes a person's body temperature instantly by ten degrees",
                    "Because foreheads do not possess any physical temperature"
                ],
                "correct": 0,
                "explanation": "The sensation of warmth via touch is relative to the temperature of the examiner's hand. Cold hands perceive normal skin as feverish, while warm hands fail to detect mild fevers.",
                "study_insight": "Skin senses the rate of heat transfer, not absolute numerical temperature."
            },
            {
                "question": "What is the specialized scientific instrument designed to provide an objective, reliable numerical measurement of body hotness?",
                "options": [
                    "A barometer",
                    "A thermometer",
                    "An anemometer",
                    "A galvanometer"
                ],
                "correct": 1,
                "explanation": "A thermometer is an instrument specifically calibrated to measure temperature objectively on standardized numerical scales.",
                "study_insight": "Thermometers eliminate human subjective perception from thermal measurement."
            }
        ]
    },
    {
        "id": 2,
        "title": "Sensory Trick",
        "subtitle": "Activity 7.1: The Three-Bowl Paradox and the Limits of Touch",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Can our sense of touch deceive us? Let us perform the famous <strong class="text-amber-300 font-semibold">Three-Bowl Investigation (Activity 7.1)</strong>:
                </p>
                <div class="grid grid-cols-3 gap-2 text-center text-xs">
                    <div class="p-2.5 rounded-xl bg-rose-950/40 border border-rose-500/30">
                        <span class="font-bold text-rose-300 block mb-1">Bowl A</span>
                        <span class="text-slate-300 text-[11px]">Lukewarm / Warm Water</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-300 block mb-1">Bowl B</span>
                        <span class="text-slate-300 text-[11px]">Ordinary Room Tap Water</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                        <span class="font-bold text-cyan-300 block mb-1">Bowl C</span>
                        <span class="text-slate-300 text-[11px]">Ice-Cold Water</span>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-1.5">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider">The Sensory Contradiction</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Dip your left hand into Bowl A (warm) and your right hand into Bowl C (ice-cold) for two minutes. Now, pull both hands out and plunge them <strong class="text-white">simultaneously into Bowl B</strong>.
                    </p>
                    <p class="text-amber-300 font-semibold">
                        • Left Hand reports: <em>"Bowl B feels cold!"</em><br>
                        • Right Hand reports: <em>"Bowl B feels warm!"</em>
                    </p>
                    <p class="text-slate-400 text-[11px]">
                        The exact same water in Bowl B cannot be both cold and warm at the same instant! This proves our skin detects relative heat flow, not true temperature.
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us examine the fascinating three-bowl experiment, known as Activity 7.1. Line up three bowls on a table: Bowl A containing warm water, Bowl C containing ice-cold water, and Bowl B in the middle containing normal room-temperature tap water. Place your left hand into the warm water and your right hand into the ice-cold water. Keep them there for two full minutes so your skin receptors adapt. Now, remove both hands at once and plunge them together into the middle bowl, Bowl B. What happens? Your brain receives two completely conflicting messages at the exact same moment! Your left hand insists the water is cold, because it is losing heat to the water. Your right hand insists the water is warm, because it is absorbing heat from the water. Can a single bowl of water be simultaneously cold and warm? Of course not! This classic experiment proves conclusively that the human sense of touch cannot be relied upon for objective scientific measurement.",
        "spoken_text": "Let us examine the fascinating three-bowl experiment, known as Activity 7.1. Line up three bowls on a table: Bowl A containing warm water, Bowl C containing ice-cold water, and Bowl B in the middle containing normal room-temperature tap water. Place your left hand into the warm water and your right hand into the ice-cold water. Keep them there for two full minutes so your skin receptors adapt. Now, remove both hands at once and plunge them together into the middle bowl, Bowl B. What happens? Your brain receives two completely conflicting messages at the exact same moment! Your left hand insists the water is cold, because it is losing heat to the water. Your right hand insists the water is warm, because it is absorbing heat from the water. Can a single bowl of water be simultaneously cold and warm? Of course not! This classic experiment proves conclusively that the human sense of touch cannot be relied upon for objective scientific measurement.",
        "checkpoints": [
            {
                "question": "In Activity 7.1, why does Bowl B feel simultaneously cool to the left hand and warm to the right hand?",
                "options": [
                    "Bowl B contains two completely different liquids separated by an invisible barrier",
                    "Skin thermoreceptors respond to the direction of heat transfer relative to each hand's previous thermal state",
                    "The water in Bowl B has two different boiling points",
                    "One hand has lost all nervous sensation"
                ],
                "correct": 1,
                "explanation": "The hand pre-adapted in warm water loses heat to Bowl B (perceiving cold), while the hand pre-adapted in ice water gains heat from Bowl B (perceiving warmth).",
                "study_insight": "Thermal sensation is relative to baseline adaptation, proving touch is subjective."
            },
            {
                "question": "What is the key scientific conclusion drawn from the three-bowl investigation?",
                "options": [
                    "Our sense of touch is unreliable for judging temperature objectively",
                    "Water in bowls always turns into ice within two minutes",
                    "Lukewarm water is hotter than boiling oil",
                    "Human hands can act as precision calibrated laboratory thermometers"
                ],
                "correct": 0,
                "explanation": "Because identical tap water produces contradictory sensations, human touch cannot serve as a reliable quantitative measurement of temperature.",
                "study_insight": "Subjective perceptions fail where quantitative scientific measurement succeeds."
            }
        ]
    },
    {
        "id": 3,
        "title": "Defining Heat",
        "subtitle": "Scientific Definition of Temperature and Molecular Kinetic Energy",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    If our senses cannot provide an objective reading, how does physical science define hotness and coldness?
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Scientific Definition of Temperature</h4>
                    <p class="text-sm font-bold text-white bg-slate-950 p-2.5 rounded-lg border border-slate-800 text-center">
                        <strong class="text-cyan-400">Temperature</strong> is a reliable, objective measure of the degree of hotness or coldness of an object.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-400 block mb-1">Hot Body</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">Possesses a <strong class="text-white">higher temperature</strong>; its constituent molecules vibrate and collide with high kinetic energy.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-cyan-400 block mb-1">Cold Body</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">Possesses a <strong class="text-white">lower temperature</strong>; its constituent molecules move with slower, lower kinetic energy.</p>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">Direction of Heat Flow:</strong> Heat energy spontaneously flows from a region of higher temperature to a region of lower temperature until thermal equilibrium is established.
                </div>
            </div>
        """,
        "lecture_script": "Now, let us define temperature with scientific rigour. In physics, temperature is defined as the reliable, objective measure of the degree of hotness or coldness of a body. A hotter body always possesses a higher temperature than a colder one. But what is happening deep inside the matter? Everything around us is composed of tiny atoms and molecules. In a hot object, such as boiling soup or a glowing iron rod, the molecules vibrate and collide with tremendous speed and kinetic energy. In a cold object, like an ice cube, the molecules move sluggishly with much lower kinetic energy. Temperature is essentially a direct reflection of this average microscopic motion! Furthermore, temperature governs the direction of heat energy transfer: thermal energy always flows spontaneously from a body at higher temperature to one at lower temperature.",
        "spoken_text": "Now, let us define temperature with scientific rigour. In physics, temperature is defined as the reliable, objective measure of the degree of hotness or coldness of a body. A hotter body always possesses a higher temperature than a colder one. But what is happening deep inside the matter? Everything around us is composed of tiny atoms and molecules. In a hot object, such as boiling soup or a glowing iron rod, the molecules vibrate and collide with tremendous speed and kinetic energy. In a cold object, like an ice cube, the molecules move sluggishly with much lower kinetic energy. Temperature is essentially a direct reflection of this average microscopic motion! Furthermore, temperature governs the direction of heat energy transfer: thermal energy always flows spontaneously from a body at higher temperature to one at lower temperature.",
        "checkpoints": [
            {
                "question": "What is the precise scientific definition of temperature?",
                "options": [
                    "The total weight of an object measured on a balance",
                    "A reliable and objective measure of the hotness or coldness of a body",
                    "The amount of light reflected from an object's surface",
                    "The magnetic pull exerted by the Earth on liquids"
                ],
                "correct": 1,
                "explanation": "Temperature quantifies the thermal state of a body objectively, reflecting the average kinetic energy of its constituent particles.",
                "study_insight": "Temperature measures hotness objectively, independent of human touch."
            },
            {
                "question": "When a hot copper block at 80°C is placed in direct contact with a cold water beaker at 20°C, in which direction does thermal energy flow?",
                "options": [
                    "From the cold water (20°C) into the hot copper block (80°C)",
                    "From the hot copper block (80°C) into the colder water (20°C)",
                    "No heat transfer occurs between metals and liquids",
                    "Heat only flows horizontally, never vertically"
                ],
                "correct": 1,
                "explanation": "Heat energy spontaneously flows from a body of higher temperature to one of lower temperature until their temperatures become equal.",
                "study_insight": "Heat flows down temperature gradients until thermal equilibrium is attained."
            }
        ]
    },
    {
        "id": 4,
        "title": "Digital Sensor",
        "subtitle": "The Anatomy of Modern Electronic Clinical Thermometers",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Thermometers are specialized devices used to measure temperature. The device specifically designed to measure human body temperature is called a <strong class="text-indigo-300 font-semibold">clinical thermometer</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider">The Modern Digital Revolution</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Today, traditional glass-mercury clinical thermometers have been almost universally replaced by <strong class="text-white">digital clinical thermometers</strong>.
                    </p>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs pt-1">
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">
                            <span class="font-bold text-indigo-300 block">Thermistor Tip</span>
                            <span class="text-[10px] text-slate-400">Electrical resistance changes with heat</span>
                        </div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">
                            <span class="font-bold text-amber-300 block">Microchip & LCD</span>
                            <span class="text-[10px] text-slate-400">Calculates & displays reading in digits</span>
                        </div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">
                            <span class="font-bold text-emerald-300 block">Beeper Alert</span>
                            <span class="text-[10px] text-slate-400">Chirps when temperature stabilizes</span>
                        </div>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-xs space-y-1">
                    <strong class="text-rose-300 font-semibold">Why Did We Ban Mercury?</strong>
                    <p class="text-slate-300 leading-relaxed text-[11px]">
                        Mercury is an extremely toxic heavy metal. If a glass thermometer breaks in a child's mouth, toxic liquid mercury and vapors cause severe poisoning. Mercury is also impossible to dispose of safely without polluting waterways. Digital thermometers are mercury-free, shatterproof, and fast!
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us examine the modern digital clinical thermometer. For over two centuries, doctors used glass tubes filled with liquid mercury. But today, mercury clinical thermometers are being actively phased out worldwide. Why? Because mercury is a hazardous, toxic heavy metal! If a thin glass thermometer broke inside a patient's or child's mouth, liquid mercury and its invisible vapors could be swallowed or inhaled, causing severe neurological damage. Furthermore, disposing of broken mercury thermometers pollutes our rivers and soil. Modern electronic digital thermometers solve every single one of these dangers. They contain zero mercury and are encased in durable, shatterproof plastic. At the metal probe tip sits an electronic heat sensor called a thermistor. When placed against warm skin, its electrical resistance shifts predictably. A microchip converts this signal into a crystal-clear digital decimal readout on an LCD screen and sounds a gentle beep when finished.",
        "spoken_text": "Let us examine the modern digital clinical thermometer. For over two centuries, doctors used glass tubes filled with liquid mercury. But today, mercury clinical thermometers are being actively phased out worldwide. Why? Because mercury is a hazardous, toxic heavy metal! If a thin glass thermometer broke inside a patient's or child's mouth, liquid mercury and its invisible vapors could be swallowed or inhaled, causing severe neurological damage. Furthermore, disposing of broken mercury thermometers pollutes our rivers and soil. Modern electronic digital thermometers solve every single one of these dangers. They contain zero mercury and are encased in durable, shatterproof plastic. At the metal probe tip sits an electronic heat sensor called a thermistor. When placed against warm skin, its electrical resistance shifts predictably. A microchip converts this signal into a crystal-clear digital decimal readout on an LCD screen and sounds a gentle beep when finished.",
        "checkpoints": [
            {
                "question": "What is the primary public health and environmental reason for replacing mercury thermometers with digital clinical thermometers?",
                "options": [
                    "Mercury is an extremely toxic substance that poses severe poisoning and environmental disposal hazards",
                    "Mercury makes thermometers too heavy for human hands to lift",
                    "Mercury evaporates into diamonds when exposed to room air",
                    "Mercury cannot measure any temperature above zero degrees"
                ],
                "correct": 0,
                "explanation": "Mercury is a bioaccumulative neurotoxin; broken glass thermometers risk toxic ingestion, inhalation, and persistent ecological pollution.",
                "study_insight": "Digital thermometers provide safe, mercury-free, unbreakable electronic sensing."
            },
            {
                "question": "How does a digital clinical thermometer detect temperature at its metal probe tip?",
                "options": [
                    "By counting the number of heartbeats per minute",
                    "Using an electronic heat sensor (thermistor) whose electrical properties change predictably with temperature",
                    "By releasing colored steam into the room",
                    "By measuring the person's height"
                ],
                "correct": 1,
                "explanation": "A thermistor changes electrical resistance in direct proportion to temperature, which an internal microprocessor converts into an exact digital readout.",
                "study_insight": "Electronic thermistors replace expanding mercury columns with digital precision."
            }
        ]
    },
    {
        "id": 5,
        "title": "Infrared Scan",
        "subtitle": "Non-Contact Infrared Thermometry and Pandemic Screening",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    During the COVID-19 pandemic, you likely saw healthcare workers and school staff pointing small handheld "forehead guns" at people from a few centimetres away. These are <strong class="text-cyan-300 font-semibold">Infrared (Non-Contact) Thermometers</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wider">How Do Infrared Thermometers Work?</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Every physical body with a temperature above absolute zero constantly emits invisible thermal radiation called <strong class="text-white">infrared radiation (IR)</strong>. The hotter the forehead, the more intense the infrared emission.
                    </p>
                    <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1">
                        <span class="text-amber-400 font-bold block">• Optical Lens:</span> Gathers infrared rays emitted by the temporal artery of the forehead.
                        <span class="text-amber-400 font-bold block">• Thermopile Detector:</span> Converts incoming thermal radiation directly into an electric voltage.
                        <span class="text-amber-400 font-bold block">• Instant Reading:</span> Displays body temperature in under 1 second without touching!
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-200">
                    <strong class="text-white font-semibold">Zero-Contact Advantage:</strong> Because the device never touches the patient's skin, it eliminates the risk of transmitting infectious viruses or bacteria between consecutive individuals.
                </div>
            </div>
        """,
        "lecture_script": "During global viral outbreaks like the COVID-19 pandemic, healthcare workers faced a major safety challenge: if you place a contact thermometer into the mouth of a sick person, you must thoroughly disinfect it before touching anyone else, or risk spreading disease. The solution was the non-contact infrared thermometer. How can a device measure your heat without touching you? The secret lies in thermal physics: every object in the universe radiates invisible energy called infrared radiation. The warmer your body, the more infrared radiation radiates from your skin. The infrared thermometer features a small optical lens that focuses these invisible heat waves onto a sensor called a thermopile. In less than one second, the device calculates your exact body temperature from a safe distance of three to five centimetres. It is hygienic, instantaneous, and prevents cross-contamination.",
        "spoken_text": "During global viral outbreaks like the COVID-19 pandemic, healthcare workers faced a major safety challenge: if you place a contact thermometer into the mouth of a sick person, you must thoroughly disinfect it before touching anyone else, or risk spreading disease. The solution was the non-contact infrared thermometer. How can a device measure your heat without touching you? The secret lies in thermal physics: every object in the universe radiates invisible energy called infrared radiation. The warmer your body, the more infrared radiation radiates from your skin. The infrared thermometer features a small optical lens that focuses these invisible heat waves onto a sensor called a thermopile. In less than one second, the device calculates your exact body temperature from a safe distance of three to five centimetres. It is hygienic, instantaneous, and prevents cross-contamination.",
        "checkpoints": [
            {
                "question": "What physical emission is detected by a non-contact forehead thermometer to calculate body temperature?",
                "options": [
                    "Invisible thermal infrared radiation emitted by the skin",
                    "Visible green light reflected from clothing",
                    "Audible sound waves produced by breathing",
                    "Radio waves broadcast by cell phones"
                ],
                "correct": 0,
                "explanation": "All warm objects emit infrared radiation proportional to their temperature. The thermometer's sensor detects this radiation without requiring physical contact.",
                "study_insight": "Thermal radiation allows temperature measurement across open space."
            },
            {
                "question": "Why were non-contact infrared thermometers prioritized for rapid public screening during the COVID-19 pandemic?",
                "options": [
                    "They can measure temperature through solid concrete walls from a kilometer away",
                    "They eliminate physical skin contact, preventing cross-contamination of contagious pathogens between patients",
                    "They permanently cure viral infections on contact",
                    "They do not require any batteries to function"
                ],
                "correct": 1,
                "explanation": "Non-contact measurement operates at a distance of 3–5 cm, preventing the device from becoming a fomite that transmits contagious viruses.",
                "study_insight": "Hygiene and infection control dictate tool choice in clinical epidemiology."
            }
        ]
    },
    {
        "id": 6,
        "title": "Clinical Steps",
        "subtitle": "Activity 7.2: Clinical Protocol for Measuring Human Body Temperature",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Measuring body temperature accurately requires following standardized clinical hygiene and measurement steps (<strong class="text-amber-300 font-semibold">Activity 7.2</strong>).
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Step-by-Step Clinical Procedure</h4>
                    <ol class="space-y-2 text-slate-300 list-decimal list-inside leading-relaxed">
                        <li><strong class="text-white">Sanitize the Tip:</strong> Wipe the metallic probe thoroughly with an alcohol swab or wash with clean water and antiseptic solution before use.</li>
                        <li><strong class="text-white">Power On & Ready Check:</strong> Press the power button. Ensure the LCD screen displays a self-test message followed by <strong class="text-emerald-400 font-mono">'Lo °C'</strong> (indicating readiness).</li>
                        <li><strong class="text-white">Placement:</strong> Place the probe tip firmly under the patient's tongue with mouth closed. For infants or elderly, place deep into the centre of the armpit (axillary reading).</li>
                        <li><strong class="text-white">Wait for Beeper:</strong> Hold steady for approximately 60 seconds until the thermometer sounds consecutive <strong class="text-amber-300 font-bold">beeps</strong>.</li>
                        <li><strong class="text-white">Record & Disinfect:</strong> Read the digital value on the screen, power off, and sanitize the probe again before storage.</li>
                    </ol>
                </div>
            </div>
        """,
        "lecture_script": "Let us learn the correct clinical procedure for measuring body temperature, as outlined in Activity 7.2. Step one: hygiene is paramount. Before inserting any thermometer, wash the metal probe with an antiseptic solution or wipe it with an alcohol swab. Step two: press the power button and inspect the screen. You should see a brief self-test followed by the letters L-o and the degree Celsius symbol. This does not mean the battery is low; it simply indicates that the current room temperature is lower than the lowest measurable body threshold of thirty-two degrees! Step three: place the tip beneath the tongue at the back of the mouth, and instruct the patient to breathe through the nose with lips closed. For young infants who might bite the probe, place it securely in the fold of the armpit. Step four: wait patiently for about one minute until the electronic beeper sounds. Finally, record the reading and sanitize the probe once more.",
        "spoken_text": "Let us learn the correct clinical procedure for measuring body temperature, as outlined in Activity 7.2. Step one: hygiene is paramount. Before inserting any thermometer, wash the metal probe with an antiseptic solution or wipe it with an alcohol swab. Step two: press the power button and inspect the screen. You should see a brief self-test followed by the letters L-o and the degree Celsius symbol. This does not mean the battery is low; it simply indicates that the current room temperature is lower than the lowest measurable body threshold of thirty-two degrees! Step three: place the tip beneath the tongue at the back of the mouth, and instruct the patient to breathe through the nose with lips closed. For young infants who might bite the probe, place it securely in the fold of the armpit. Step four: wait patiently for about one minute until the electronic beeper sounds. Finally, record the reading and sanitize the probe once more.",
        "checkpoints": [
            {
                "question": "What does the symbol 'Lo' on a digital clinical thermometer's display indicate when turned on at room temperature?",
                "options": [
                    "The battery is completely dead and must be replaced immediately",
                    "The ambient temperature is lower than the clinical thermometer's minimum measurable limit (typically 32°C)",
                    "The thermometer is broken and dangerous to touch",
                    "The patient has hypothermia before touching the probe"
                ],
                "correct": 1,
                "explanation": "'Lo' stands for 'Low Temperature', meaning the detected temperature is below the clinical measuring window (32°C to 42°C). It confirms readiness for measurement.",
                "study_insight": "'Lo' confirms ready state, not battery failure."
            },
            {
                "question": "Why should the thermometer probe be sanitized both BEFORE and AFTER taking a measurement?",
                "options": [
                    "To prevent the transfer of germs, saliva bacteria, and cross-infection between individuals",
                    "To reset the digital numbers to zero",
                    "To increase the weight of the plastic probe",
                    "To charge the internal electronic battery"
                ],
                "correct": 0,
                "explanation": "Antiseptic cleaning sterilizes the probe, neutralizing oral pathogens and preventing microbial transmission between patients.",
                "study_insight": "Aseptic technique is mandatory in clinical thermometry."
            }
        ]
    },
    {
        "id": 7,
        "title": "Body Baseline",
        "subtitle": "Normal Human Body Temperature and Circadian Fluctuations",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    What is the "normal" temperature of a healthy human being? In science and medicine, the accepted benchmark is:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-1">
                    <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Average Normal Human Body Temperature</span>
                    <div class="text-2xl font-extrabold text-emerald-400 font-mono">
                        37.0 °C <span class="text-sm font-normal text-slate-300">(98.6 °F)</span>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-850 border border-slate-800 text-xs space-y-2">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Crucial Scientific Nuance</h4>
                    <p class="text-slate-300 leading-relaxed">
                        37.0°C is <strong class="text-white">not</strong> an identical static number for every single person at every single moment! It represents the <strong class="text-emerald-300 font-semibold">statistical average</strong> of thousands of healthy individuals.
                    </p>
                    <div class="grid grid-cols-2 gap-2 text-[11px] pt-1">
                        <div class="p-2 rounded bg-slate-900 border border-slate-800">
                            <span class="font-bold text-indigo-300 block">Circadian Rhythm</span>
                            <span class="text-slate-400">Lowest at dawn (~36.4°C); peaks in late afternoon (~37.3°C).</span>
                        </div>
                        <div class="p-2 rounded bg-slate-900 border border-slate-800">
                            <span class="font-bold text-amber-300 block">Physical Activity</span>
                            <span class="text-slate-400">Running, playing sports, or hot weather temporarily raises temperature.</span>
                        </div>
                    </div>
                </div>
            </div>
        """,
        "lecture_script": "What is normal human body temperature? Every textbook will tell you that normal human body temperature is 37.0 degrees Celsius, which equals 98.6 degrees Fahrenheit. But here is a crucial scientific nuance: 37.0 degrees Celsius is not a rigid, magical constant that holds true for every person every second of the day! It is the statistical average calculated from measurements of thousands of healthy human beings. If you measure your own temperature at six o'clock in the morning just as you wake up, it might be 36.4 degrees Celsius. If you measure it again at five in the afternoon after playing football in the sun, it might be 37.3 degrees Celsius! Both values are completely normal. Body temperature fluctuates across a natural daily circadian rhythm and varies slightly with age, metabolic rate, and physical exertion.",
        "spoken_text": "What is normal human body temperature? Every textbook will tell you that normal human body temperature is 37.0 degrees Celsius, which equals 98.6 degrees Fahrenheit. But here is a crucial scientific nuance: 37.0 degrees Celsius is not a rigid, magical constant that holds true for every person every second of the day! It is the statistical average calculated from measurements of thousands of healthy human beings. If you measure your own temperature at six o'clock in the morning just as you wake up, it might be 36.4 degrees Celsius. If you measure it again at five in the afternoon after playing football in the sun, it might be 37.3 degrees Celsius! Both values are completely normal. Body temperature fluctuates across a natural daily circadian rhythm and varies slightly with age, metabolic rate, and physical exertion.",
        "checkpoints": [
            {
                "question": "What is the standard average normal temperature of a healthy human body in degrees Celsius and Fahrenheit?",
                "options": [
                    "37.0°C (98.6°F)",
                    "100.0°C (212.0°F)",
                    "0.0°C (32.0°F)",
                    "50.0°C (122.0°F)"
                ],
                "correct": 0,
                "explanation": "37.0°C (corresponding to 98.6°F on the Fahrenheit scale) is the worldwide medical baseline average for healthy adults.",
                "study_insight": "Memorize the dual baseline: 37.0°C = 98.6°F."
            },
            {
                "question": "A healthy student's temperature reads 36.6°C early in the morning and 37.2°C in the afternoon. What should be concluded?",
                "options": [
                    "The student has contracted a severe tropical infection",
                    "The thermometer is completely defective and must be discarded",
                    "This is normal physiological variation due to natural circadian rhythms and daily activity",
                    "The student's blood has frozen"
                ],
                "correct": 2,
                "explanation": "Human body temperature naturally fluctuates by roughly 0.5°C to 0.8°C throughout the day due to circadian metabolic cycles.",
                "study_insight": "Normal body temperature is a dynamic healthy range, not an absolute fixed point."
            }
        ]
    },
    {
        "id": 8,
        "title": "Scale Trio",
        "subtitle": "Celsius, Fahrenheit, and the SI Thermodynamic Standard: Kelvin",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Temperature cannot be stated as a bare number; it requires a standardized numerical scale. Scientists and engineers utilize three major temperature scales:
                </p>
                <div class="grid grid-cols-3 gap-2 text-xs">
                    <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-cyan-300 block mb-1">Celsius (°C)</span>
                        <p class="text-[11px] text-slate-300 leading-relaxed">
                            Everyday metric scale. Ice melts at <strong class="text-white">0 °C</strong>; water boils at <strong class="text-white">100 °C</strong> at standard pressure.
                        </p>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-300 block mb-1">Fahrenheit (°F)</span>
                        <p class="text-[11px] text-slate-300 leading-relaxed">
                            Traditional clinical scale. Ice melts at <strong class="text-white">32 °F</strong>; water boils at <strong class="text-white">212 °F</strong> (180 intervals).
                        </p>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-emerald-300 block mb-1">Kelvin (K)</span>
                        <p class="text-[11px] text-slate-300 leading-relaxed">
                            <strong class="text-white">Official SI Unit</strong>. Absolute zero is <strong class="text-white">0 K</strong> (-273.15 °C). Never written with a degree symbol!
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-1">
                    <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-wider">Conversion Relationships</h4>
                    <div class="p-2 rounded bg-slate-950 font-mono text-center text-slate-200 border border-slate-800 space-y-1">
                        <div>K = °C + 273.15</div>
                        <div class="text-[11px] text-slate-400">°F = (°C × 9/5) + 32</div>
                    </div>
                </div>
            </div>
        """,
        "lecture_script": "Let us explore the three major temperature scales used across the world. First is the Celsius scale, denoted by degree C, devised by Swedish astronomer Anders Celsius. On this scale, pure water freezes at zero degrees and boils at one hundred degrees at sea level. The interval is divided into one hundred equal divisions. Second is the Fahrenheit scale, denoted by degree F. Here, water freezes at thirty-two degrees and boils at two hundred and twelve degrees, creating one hundred and eighty divisions. In India, clinical fever is often spoken of in Fahrenheit—such as a fever of one hundred and one degrees. But the most important scale for global physical science is the Kelvin scale, named after Lord Kelvin. Kelvin is the official SI base unit of temperature! Zero Kelvin is absolute zero, the theoretical point where all molecular motion ceases. Notice a strict international rule: Kelvin is written simply as capital K, never with a degree symbol. We write three hundred Kelvin, not three hundred degrees Kelvin.",
        "spoken_text": "Let us explore the three major temperature scales used across the world. First is the Celsius scale, denoted by degree C, devised by Swedish astronomer Anders Celsius. On this scale, pure water freezes at zero degrees and boils at one hundred degrees at sea level. The interval is divided into one hundred equal divisions. Second is the Fahrenheit scale, denoted by degree F. Here, water freezes at thirty-two degrees and boils at two hundred and twelve degrees, creating one hundred and eighty divisions. In India, clinical fever is often spoken of in Fahrenheit—such as a fever of one hundred and one degrees. But the most important scale for global physical science is the Kelvin scale, named after Lord Kelvin. Kelvin is the official SI base unit of temperature! Zero Kelvin is absolute zero, the theoretical point where all molecular motion ceases. Notice a strict international rule: Kelvin is written simply as capital K, never with a degree symbol. We write three hundred Kelvin, not three hundred degrees Kelvin.",
        "checkpoints": [
            {
                "question": "What is the official International System of Units (SI) standard unit for measuring temperature?",
                "options": [
                    "The Kelvin (K)",
                    "The degree Celsius (°C)",
                    "The degree Fahrenheit (°F)",
                    "The Calorie (cal)"
                ],
                "correct": 0,
                "explanation": "The Kelvin (symbol K) is the fundamental SI base unit of thermodynamic temperature.",
                "study_insight": "Kelvin (K) is the SI unit; Celsius (°C) is metric everyday, Fahrenheit (°F) is customary."
            },
            {
                "question": "What is the correct scientific notation convention when writing a temperature of 300 in the Kelvin scale?",
                "options": [
                    "300 K (capital K with a space, no degree symbol)",
                    "300°K (with degree symbol)",
                    "300 kgs.",
                    "300 kelvins°"
                ],
                "correct": 0,
                "explanation": "By international metrological standards, the Kelvin scale is an absolute thermodynamic scale and is written without a degree symbol: 300 K.",
                "study_insight": "Never write a degree symbol (° ) with Kelvin: write K, not °K."
            }
        ]
    },
    {
        "id": 9,
        "title": "Lab Stem",
        "subtitle": "Structure and Range of the Laboratory Thermometer",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    While a clinical thermometer measures human body heat (35°C to 42°C), measuring boiling liquids, chemical reactions, or melting ice requires a <strong class="text-indigo-300 font-semibold">Laboratory Thermometer</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Anatomy of a Laboratory Thermometer</h4>
                    <ul class="text-xs space-y-1.5 text-slate-300">
                        <li>• <strong class="text-white">Bulb:</strong> Thin-walled glass reservoir at the base containing thermometric liquid (red-dyed alcohol or silvery mercury).</li>
                        <li>• <strong class="text-white">Capillary Bore:</strong> An extremely narrow, uniform glass tube running through the center. Thermal expansion pushes the liquid column upward.</li>
                        <li>• <strong class="text-white">Glass Stem:</strong> Heavy, thick protective outer casing with etched temperature graduations.</li>
                        <li>• <strong class="text-white">Typical Range:</strong> Spans from <strong class="text-cyan-400">-10 °C</strong> (below freezing) to <strong class="text-rose-400">110 °C</strong> (above boiling).</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-xs text-rose-200">
                    <strong class="text-white font-semibold">NO Constriction Kink:</strong> Unlike clinical thermometers, laboratory thermometers have <span class="underline">no kink or constriction</span> above the bulb. The liquid falls immediately when removed from heat!
                </div>
            </div>
        """,
        "lecture_script": "Now, let us examine the laboratory thermometer. A clinical thermometer has a very narrow window of measurement—usually thirty-five to forty-two degrees Celsius—because human bodies never survive far beyond those extremes. But in a science laboratory, we must measure melting ice at zero degrees or boiling brine at over one hundred degrees. For this, we use a laboratory thermometer. It consists of a long, uniform, thick-walled glass stem with an ultra-thin capillary tube running through the center. At the bottom is a thin-walled bulb filled with a thermometric liquid, typically red-dyed alcohol or mercury. When the bulb absorbs heat, the liquid expands up the narrow capillary bore. A standard laboratory thermometer covers a wide range from minus ten degrees Celsius to one hundred and ten degrees Celsius. But notice one critical structural difference: a laboratory thermometer has no constriction or kink above its bulb. The liquid column drops immediately the moment it leaves the hot medium.",
        "spoken_text": "Now, let us examine the laboratory thermometer. A clinical thermometer has a very narrow window of measurement—usually thirty-five to forty-two degrees Celsius—because human bodies never survive far beyond those extremes. But in a science laboratory, we must measure melting ice at zero degrees or boiling brine at over one hundred degrees. For this, we use a laboratory thermometer. It consists of a long, uniform, thick-walled glass stem with an ultra-thin capillary tube running through the center. At the bottom is a thin-walled bulb filled with a thermometric liquid, typically red-dyed alcohol or mercury. When the bulb absorbs heat, the liquid expands up the narrow capillary bore. A standard laboratory thermometer covers a wide range from minus ten degrees Celsius to one hundred and ten degrees Celsius. But notice one critical structural difference: a laboratory thermometer has no constriction or kink above its bulb. The liquid column drops immediately the moment it leaves the hot medium.",
        "checkpoints": [
            {
                "question": "What is the typical measurement temperature range of a standard laboratory thermometer?",
                "options": [
                    "35°C to 42°C",
                    "-10°C to 110°C",
                    "0°C to 10°C",
                    "100°C to 1000°C"
                ],
                "correct": 1,
                "explanation": "Standard laboratory thermometers are graduated from -10°C (below water's freezing point) to 110°C (above water's normal boiling point).",
                "study_insight": "Lab range: -10°C to 110°C. Clinical range: 35°C to 42°C."
            },
            {
                "question": "Why can a standard laboratory thermometer NOT be used to measure body temperature by placing it in the mouth and then reading it after taking it out?",
                "options": [
                    "It has no constriction kink above the bulb, so the liquid column immediately drops when exposed to cooler room air",
                    "Its glass instantly dissolves in saliva",
                    "It produces a loud explosion when touching skin",
                    "It cannot measure any temperature below 50°C"
                ],
                "correct": 0,
                "explanation": "Without a constriction kink to trap the column, the thermometric liquid contracts the instant the bulb encounters cooler ambient air outside the mouth.",
                "study_insight": "A constriction kink is unique to clinical thermometers to preserve readings."
            }
        ]
    },
    {
        "id": 10,
        "title": "Least Count",
        "subtitle": "Activities 7.3 & 7.4: Determining Range and Value of the Smallest Division",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Before using any laboratory thermometer, you must perform two essential mathematical inspections: determining its <strong class="text-cyan-300 font-semibold">range</strong> and calculating its <strong class="text-amber-300 font-semibold">least count (smallest division value)</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">How to Calculate Least Count (Activity 7.4)</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Step 1: Note the temperature difference between two consecutive major numbered marks (e.g., between 10°C and 20°C = 10°C).
                    </p>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Step 2: Count the total number of small subdivisions between these two major marks.
                    </p>
                    <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-center font-mono text-xs text-emerald-400">
                        Value of 1 Small Division = (Major Difference) ÷ (Number of Subdivisions)
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2.5 rounded-xl bg-slate-850 border border-slate-700">
                        <span class="font-bold text-white block">Case A: 10 Subdivisions</span>
                        <span class="text-slate-300 text-[11px]">10°C ÷ 10 = <strong class="text-cyan-300">1 °C per mark</strong></span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-850 border border-slate-700">
                        <span class="font-bold text-white block">Case B: 5 Subdivisions</span>
                        <span class="text-slate-300 text-[11px]">10°C ÷ 5 = <strong class="text-emerald-300">2 °C per mark</strong></span>
                    </div>
                </div>
            </div>
        """,
        "lecture_script": "Before you take a single measurement in the science lab, you must determine two properties of your thermometer, as taught in Activities 7.3 and 7.4. First, find its range: look at the lowest engraved number and the highest engraved number. On a typical thermometer, that is minus ten degrees to one hundred and ten degrees Celsius. Second, calculate its least count—which means the temperature value represented by a single tiny subdivision mark. Look at two consecutive big numbers, say ten degrees and twenty degrees. The difference between them is ten degrees. Now, count the small tick marks between them. If there are ten small divisions between ten and twenty, then ten degrees divided by ten equals one degree Celsius per mark! If there are five divisions, each mark represents two degrees Celsius. If there are fifty divisions, each represents zero point two degrees Celsius. Knowing this smallest division value is essential to avoid misreading data.",
        "spoken_text": "Before you take a single measurement in the science lab, you must determine two properties of your thermometer, as taught in Activities 7.3 and 7.4. First, find its range: look at the lowest engraved number and the highest engraved number. On a typical thermometer, that is minus ten degrees to one hundred and ten degrees Celsius. Second, calculate its least count—which means the temperature value represented by a single tiny subdivision mark. Look at two consecutive big numbers, say ten degrees and twenty degrees. The difference between them is ten degrees. Now, count the small tick marks between them. If there are ten small divisions between ten and twenty, then ten degrees divided by ten equals one degree Celsius per mark! If there are five divisions, each mark represents two degrees Celsius. If there are fifty divisions, each represents zero point two degrees Celsius. Knowing this smallest division value is essential to avoid misreading data.",
        "checkpoints": [
            {
                "question": "If there are 10 small subdivisions between the 20°C and 30°C markings on a laboratory thermometer, what temperature does each single division mark represent?",
                "options": [
                    "1°C",
                    "0.1°C",
                    "5°C",
                    "10°C"
                ],
                "correct": 0,
                "explanation": "Temperature span = 30°C - 20°C = 10°C. Divided by 10 subdivisions: 10°C ÷ 10 = 1°C per division.",
                "study_insight": "Least Count Formula = (Difference between major marks) / (Number of divisions)."
            },
            {
                "question": "If a thermometer's major marks are 1°C apart and there are 5 small subdivisions between each degree, what is the least count?",
                "options": [
                    "0.2°C",
                    "0.5°C",
                    "1°C",
                    "2°C"
                ],
                "correct": 0,
                "explanation": "Least Count = 1°C ÷ 5 = 0.2°C. Each small tick mark represents two-tenths of a degree Celsius.",
                "study_insight": "Finer subdivisions yield higher measurement resolution."
            }
        ]
    },
    {
        "id": 11,
        "title": "Zero Parallax",
        "subtitle": "Strict Lab Precautions: Vertical Alignment and Line-of-Sight Geometry",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Reading a laboratory thermometer requires strict adherence to three fundamental physical precautions to avoid measurement errors and instrument breakage:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">The Three Golden Lab Rules</h4>
                    <ul class="space-y-2 text-slate-300">
                        <li>
                            <strong class="text-cyan-300">1. Strict Vertical Orientation:</strong> Always keep the thermometer vertical. Tilting the tube causes gravity to distort the liquid meniscus level.
                        </li>
                        <li>
                            <strong class="text-emerald-300">2. Free Immersion:</strong> The bulb must be fully surrounded by the liquid being measured, without touching the bottom or sides of the beaker (which conduct direct heat from burners or table surfaces).
                        </li>
                        <li>
                            <strong class="text-rose-300">3. Eliminating Parallax Error:</strong> The observer's eye must be positioned at the exact same horizontal level as the top of the liquid column. Looking from above or below skews the reading!
                        </li>
                    </ul>
                </div>
            </div>
        """,
        "lecture_script": "Operating a laboratory thermometer safely and accurately requires strict adherence to three golden rules. Rule number one: hold the thermometer strictly vertical. Never tilt it diagonally, as gravity can alter the apparent level of the liquid meniscus against the glass capillary. Rule number two: the bulb must be fully immersed in the liquid, suspended in the center. The bulb must never touch the bottom or sides of the glass beaker! Why? Because the bottom of the beaker is in direct contact with the hot wire gauze or flame, and the sides are cooled by ambient air. Touching the walls gives you the temperature of the container, not the liquid! Rule number three: eliminate parallax error. When taking a reading, position your eye at the exact horizontal level of the top of the liquid column. Looking down from above makes the reading look artificially high; looking up from below makes it look artificially low.",
        "spoken_text": "Operating a laboratory thermometer safely and accurately requires strict adherence to three golden rules. Rule number one: hold the thermometer strictly vertical. Never tilt it diagonally, as gravity can alter the apparent level of the liquid meniscus against the glass capillary. Rule number two: the bulb must be fully immersed in the liquid, suspended in the center. The bulb must never touch the bottom or sides of the glass beaker! Why? Because the bottom of the beaker is in direct contact with the hot wire gauze or flame, and the sides are cooled by ambient air. Touching the walls gives you the temperature of the container, not the liquid! Rule number three: eliminate parallax error. When taking a reading, position your eye at the exact horizontal level of the top of the liquid column. Looking down from above makes the reading look artificially high; looking up from below makes it look artificially low.",
        "checkpoints": [
            {
                "question": "Why must the bulb of a laboratory thermometer NEVER touch the bottom or sides of the container during measurement?",
                "options": [
                    "The container walls reflect false temperatures due to direct burner heating or room cooling",
                    "The bulb is magnetic and sticks permanently to glass",
                    "Touching glass causes the liquid inside to freeze into ice",
                    "The glass will turn transparent and vanish"
                ],
                "correct": 0,
                "explanation": "Container bottoms receive direct conducted heat from burners, while container sides lose heat to room air. The bulb must measure the bulk liquid alone.",
                "study_insight": "Suspended immersion ensures thermal equilibrium with the fluid under test."
            },
            {
                "question": "To avoid parallax error when reading a liquid column on a thermometer scale, the observer's line of sight must be:",
                "options": [
                    "Tilted at 45 degrees from above the scale",
                    "Tilted at 45 degrees from below the scale",
                    "Perpendicular and exactly horizontal at the level of the liquid meniscus",
                    "Closed with both eyes shut"
                ],
                "correct": 2,
                "explanation": "Positioning the line of sight at exact 90° horizontal alignment with the meniscus eliminates optical parallax distortion.",
                "study_insight": "Perpendicular eye alignment is the universal rule for all analogue scales."
            }
        ]
    },
    {
        "id": 12,
        "title": "Immersion Rule",
        "subtitle": "Why Laboratory Thermometers Must Be Read While Still Immersed",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Here is the most common mistake students make in the laboratory: taking the thermometer out of the hot water beaker to read it comfortably!
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-rose-400 uppercase tracking-wider">The Instant Contraction Hazard</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        A laboratory thermometer has <strong class="text-white">no constriction</strong>. The moment you pull the bulb out of the hot liquid, the bulb encounters cooler room air.
                    </p>
                    <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-xs text-rose-300 font-semibold space-y-1">
                        ⚠️ The liquid column drops instantly! Within 3 seconds, the reading drops by 10°C to 20°C toward room temperature.
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-200">
                    <strong class="text-white font-semibold">The Inviolable Immersion Rule:</strong> A laboratory thermometer MUST be read <span class="underline">while its bulb is still fully immersed</span> in the substance being measured!
                </div>
            </div>
        """,
        "lecture_script": "Here is one of the most vital rules in practical laboratory science: you must read a laboratory thermometer while its bulb is still submerged inside the liquid! In a clinic, a nurse places a clinical thermometer under your tongue, pulls it out, and inspects the number. You can do that with a clinical thermometer because it has a special constriction kink that traps the mercury column in place. But a laboratory thermometer has no constriction. Its capillary bore is straight and open. If you lift the thermometer out of a beaker of hot water at eighty degrees, the thin-walled bulb instantly hits the twenty-degree air of the room. Heat conducts rapidly into the room, the thermometric liquid contracts, and the column plunges downward before your eyes! By the time you look at it, your eighty-degree reading has dropped to sixty degrees. Remember: never remove a laboratory thermometer from the liquid to read it.",
        "spoken_text": "Here is one of the most vital rules in practical laboratory science: you must read a laboratory thermometer while its bulb is still submerged inside the liquid! In a clinic, a nurse places a clinical thermometer under your tongue, pulls it out, and inspects the number. You can do that with a clinical thermometer because it has a special constriction kink that traps the mercury column in place. But a laboratory thermometer has no constriction. Its capillary bore is straight and open. If you lift the thermometer out of a beaker of hot water at eighty degrees, the thin-walled bulb instantly hits the twenty-degree air of the room. Heat conducts rapidly into the room, the thermometric liquid contracts, and the column plunges downward before your eyes! By the time you look at it, your eighty-degree reading has dropped to sixty degrees. Remember: never remove a laboratory thermometer from the liquid to read it.",
        "checkpoints": [
            {
                "question": "Why must the temperature of hot water be recorded while the laboratory thermometer is still immersed in the beaker?",
                "options": [
                    "Because as soon as the thermometer is taken out, the liquid column immediately begins falling due to exposure to cooler room air",
                    "Because water evaporates if a thermometer is lifted",
                    "Because the thermometer becomes magnetic outside of water",
                    "Because laboratory thermometers can only be lifted with heavy cranes"
                ],
                "correct": 0,
                "explanation": "Without a constriction kink, the thermometric liquid contracts immediately when exposed to cooler room air, corrupting the measurement.",
                "study_insight": "In-situ reading is mandatory for non-constricted laboratory thermometers."
            },
            {
                "question": "What structural feature allows a clinical thermometer to be read outside the patient's mouth, which a laboratory thermometer lacks?",
                "options": [
                    "A built-in radio antenna",
                    "A constriction (kink) in the capillary tube just above the bulb that prevents the liquid from falling back on its own",
                    "A thick lead shield",
                    "A digital solar panel"
                ],
                "correct": 1,
                "explanation": "The capillary kink in clinical thermometers breaks the contracting mercury thread when cooled, holding the maximum reading until vigorously jerked reset.",
                "study_insight": "Constriction kink = holds peak reading; Open bore = responds instantly in real-time."
            }
        ]
    },
    {
        "id": 13,
        "title": "Ice Lock",
        "subtitle": "Activity 7.5: The 0°C Phase Transition Plateau of Melting Ice",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    What happens to the temperature of ice as it melts into liquid water? Let us examine the <strong class="text-cyan-300 font-semibold">Melting Ice Investigation (Activity 7.5)</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wider">The 0°C Thermal Plateau</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Place a laboratory thermometer into a beaker filled with crushed melting ice. The liquid column drops until it reaches exactly:
                    </p>
                    <div class="p-2 rounded bg-slate-950 font-mono text-center text-cyan-400 text-sm font-bold border border-slate-800">
                        0.0 °C (32 °F) — The Melting Point of Pure Water
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-850 border border-slate-700 text-xs text-slate-300 space-y-1.5">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Where Does the Room Heat Go?</h4>
                    <p class="leading-relaxed">
                        Even though warm room heat continuously enters the beaker, the thermometer stays <strong class="text-white">firmly locked at 0°C</strong> for twenty minutes!
                    </p>
                    <p class="text-slate-400 text-[11px]">
                        The heat energy is absorbed as <strong class="text-emerald-400">latent heat of fusion</strong> to break the rigid crystalline bonds of solid ice, rather than raising the temperature. Only after the very last flake of ice melts does the temperature begin rising!
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us explore one of the most remarkable phenomena in physical chemistry: the melting of ice, as described in Activity 7.5. Take a beaker packed with crushed ice and insert a laboratory thermometer. The liquid column drops steadily until it hits exactly zero degrees Celsius. Now, place the beaker on a table in a warm room. Heat from the room pours into the ice. You see water droplets forming as the ice melts. But look closely at the thermometer. What does it read? Five degrees? Two degrees? No! It stays firmly locked at exactly zero point zero degrees Celsius! Why does the temperature refuse to rise even though heat is entering? Because that thermal energy is being consumed to do work: it is breaking the rigid crystal hydrogen bonds holding the water molecules into solid ice. This energy is called the latent heat of fusion. As long as even a tiny sliver of ice remains in the slush, the temperature cannot rise above zero degrees.",
        "spoken_text": "Let us explore one of the most remarkable phenomena in physical chemistry: the melting of ice, as described in Activity 7.5. Take a beaker packed with crushed ice and insert a laboratory thermometer. The liquid column drops steadily until it hits exactly zero degrees Celsius. Now, place the beaker on a table in a warm room. Heat from the room pours into the ice. You see water droplets forming as the ice melts. But look closely at the thermometer. What does it read? Five degrees? Two degrees? No! It stays firmly locked at exactly zero point zero degrees Celsius! Why does the temperature refuse to rise even though heat is entering? Because that thermal energy is being consumed to do work: it is breaking the rigid crystal hydrogen bonds holding the water molecules into solid ice. This energy is called the latent heat of fusion. As long as even a tiny sliver of ice remains in the slush, the temperature cannot rise above zero degrees.",
        "checkpoints": [
            {
                "question": "What is the recorded temperature of a mixture of pure crushed ice and water while melting occurs under standard atmospheric pressure?",
                "options": [
                    "0°C",
                    "10°C",
                    "37°C",
                    "-50°C"
                ],
                "correct": 0,
                "explanation": "Pure water freezes and melts at 0°C (32°F) at standard atmospheric pressure; during the phase transition, temperature remains constant.",
                "study_insight": "Phase change temperature remains constant: melting ice = 0°C."
            },
            {
                "question": "Why does the temperature of melting ice remain constant at 0°C even when continuous heat is supplied from the surrounding room?",
                "options": [
                    "The supplied heat is consumed to break molecular crystal bonds (latent heat of fusion) rather than increasing kinetic energy",
                    "Thermometers stop working in the presence of water",
                    "Ice destroys all incoming heat energy into nothingness",
                    "The beaker insulates 100% of room heat completely"
                ],
                "correct": 0,
                "explanation": "Latent heat of fusion changes the physical state from solid to liquid without altering kinetic energy, holding the temperature constant.",
                "study_insight": "Latent heat alters phase without changing temperature."
            }
        ]
    },
    {
        "id": 14,
        "title": "Boiling Flat",
        "subtitle": "Activity 7.6: The 100°C Vaporization Plateau of Boiling Water",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Now let us heat water over a Bunsen burner or gas stove until it boils vigorously (<strong class="text-rose-300 font-semibold">Activity 7.6</strong>). What does the thermometer record?
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-rose-400 uppercase tracking-wider">The 100°C Boiling Plateau</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        As the water is heated, the liquid column climbs rapidly: 40°C... 60°C... 80°C... 95°C... until vigorous steam bubbles erupt throughout the liquid. The reading stops at:
                    </p>
                    <div class="p-2 rounded bg-slate-950 font-mono text-center text-rose-400 text-sm font-bold border border-slate-800">
                        100.0 °C (212 °F) — Boiling Point of Pure Water at Sea Level
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-850 border border-slate-700 text-xs text-slate-300 space-y-1">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Turn Up the Flame?</h4>
                    <p class="leading-relaxed">
                        If you turn the gas flame up to maximum, does the water reach 105°C or 110°C? <strong class="text-white">Never!</strong>
                    </p>
                    <p class="text-slate-400 text-[11px]">
                        The extra heat only converts liquid water into steam faster (<strong class="text-rose-300">latent heat of vaporization</strong>). In an open vessel, boiling water cannot exceed 100°C at normal atmospheric pressure.
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Now let us turn to the opposite phase change: boiling water, explored in Activity 7.6. Place a beaker of water over a Bunsen flame with a laboratory thermometer suspended inside. As thermal energy enters, the liquid column climbs swiftly: fifty, seventy, ninety degrees. Soon, vigorous steam bubbles form at the bottom, rise, and burst at the surface. The water is boiling! Look at the thermometer: it reads exactly one hundred degrees Celsius. Now, try turning the flame up to its highest setting. Does the water get hotter? Does it reach one hundred and five degrees? Absolutely not! The thermometer stays glued to one hundred point zero degrees Celsius. All the additional heat pouring in from the blazing burner is absorbed as the latent heat of vaporization, converting liquid water into gaseous steam. As long as water boils freely at normal atmospheric pressure, its temperature remains completely flat at one hundred degrees.",
        "spoken_text": "Now let us turn to the opposite phase change: boiling water, explored in Activity 7.6. Place a beaker of water over a Bunsen flame with a laboratory thermometer suspended inside. As thermal energy enters, the liquid column climbs swiftly: fifty, seventy, ninety degrees. Soon, vigorous steam bubbles form at the bottom, rise, and burst at the surface. The water is boiling! Look at the thermometer: it reads exactly one hundred degrees Celsius. Now, try turning the flame up to its highest setting. Does the water get hotter? Does it reach one hundred and five degrees? Absolutely not! The thermometer stays glued to one hundred point zero degrees Celsius. All the additional heat pouring in from the blazing burner is absorbed as the latent heat of vaporization, converting liquid water into gaseous steam. As long as water boils freely at normal atmospheric pressure, its temperature remains completely flat at one hundred degrees.",
        "checkpoints": [
            {
                "question": "What is the boiling point of pure water under standard atmospheric sea-level pressure?",
                "options": [
                    "100°C (212°F)",
                    "37°C (98.6°F)",
                    "0°C (32°F)",
                    "500°C (932°F)"
                ],
                "correct": 0,
                "explanation": "At sea level (1 atmosphere pressure), pure water boils at 100.0°C (212.0°F).",
                "study_insight": "Pure water boiling point at 1 atm = 100°C."
            },
            {
                "question": "If you increase the burner flame under a pot of vigorously boiling water in an open kitchen, what happens to the water's temperature?",
                "options": [
                    "The temperature remains constant at 100°C while water evaporates into steam more rapidly",
                    "The temperature jumps immediately to 150°C",
                    "The water turns back into ice cubes",
                    "The water becomes solid steel"
                ],
                "correct": 0,
                "explanation": "In an open vessel, extra heat supplies latent heat of vaporization, accelerating boiling without increasing water temperature beyond 100°C.",
                "study_insight": "Boiling temperature remains locked at 100°C in open containers."
            }
        ]
    },
    {
        "id": 15,
        "title": "Room & Sky",
        "subtitle": "Room Thermometers, Weather Stations, and Maximum-Minimum Cycles",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Measuring atmospheric air temperature is vital for human comfort, agriculture, and meteorological forecasting.
                </p>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-400 block mb-1">Room Thermometer</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            Mounted on walls in clinics, warehouses, and homes. Displays ambient indoor air temperature (typically 18°C to 28°C).
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-cyan-400 block mb-1">Max-Min Thermometer</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            Specialized meteorological U-tube (Six's thermometer) that automatically records the highest and lowest temperatures over 24 hours.
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-1.5">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider">The Daily Diurnal Weather Cycle</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Every day on Earth exhibits a natural temperature curve:
                    </p>
                    <div class="p-2 rounded bg-slate-950 text-[11px] text-slate-300 border border-slate-800 space-y-1">
                        <div>• <strong class="text-cyan-300">Minimum Temperature:</strong> Occurs around early dawn (just before sunrise) after nocturnal cooling.</div>
                        <div>• <strong class="text-amber-300">Maximum Temperature:</strong> Occurs in the early-to-mid afternoon (around 2:00 PM to 3:00 PM) due to accumulated solar ground heat.</div>
                    </div>
                </div>
            </div>
        """,
        "lecture_script": "Now, let us step outside the laboratory to look at atmospheric temperature. In weather reports on TV or smartphones, you always see two numbers: the maximum temperature and the minimum temperature of the day. How are these measured? Weather stations worldwide utilize a specialized instrument called a Maximum-Minimum thermometer, or Six's thermometer. Inside its U-shaped tube, small steel markers called dumb-bells are pushed by expanding alcohol and mercury. When the temperature drops at night, one marker stays locked at the lowest point. When it peaks in the daytime, the other marker stays locked at the highest point. When do these extremes occur? The minimum temperature almost always happens at early dawn, just before the Sun rises, because the Earth has radiated heat into space all night long. The maximum temperature occurs in early afternoon, around two to three PM, when cumulative solar radiation heating the soil reaches its maximum peak.",
        "spoken_text": "Now, let us step outside the laboratory to look at atmospheric temperature. In weather reports on TV or smartphones, you always see two numbers: the maximum temperature and the minimum temperature of the day. How are these measured? Weather stations worldwide utilize a specialized instrument called a Maximum-Minimum thermometer, or Six's thermometer. Inside its U-shaped tube, small steel markers called dumb-bells are pushed by expanding alcohol and mercury. When the temperature drops at night, one marker stays locked at the lowest point. When it peaks in the daytime, the other marker stays locked at the highest point. When do these extremes occur? The minimum temperature almost always happens at early dawn, just before the Sun rises, because the Earth has radiated heat into space all night long. The maximum temperature occurs in early afternoon, around two to three PM, when cumulative solar radiation heating the soil reaches its maximum peak.",
        "checkpoints": [
            {
                "question": "At what time of day does the minimum air temperature typically occur in nature under clear sky conditions?",
                "options": [
                    "Early dawn, just before sunrise",
                    "Exactly at 12:00 noon",
                    "Early afternoon at 3:00 PM",
                    "At sunset"
                ],
                "correct": 0,
                "explanation": "Earth's surface cools by radiating heat into space throughout the night, reaching its lowest temperature just prior to dawn.",
                "study_insight": "Minimum temperature occurs at dawn; maximum temperature occurs in early afternoon."
            },
            {
                "question": "What specialized meteorological instrument is used at weather forecasting stations to automatically record the 24-hour daily extremes of air temperature?",
                "options": [
                    "A Maximum-Minimum thermometer",
                    "A clinical mouth thermometer",
                    "A kitchen oven meat probe",
                    "A mercury blood pressure cuff"
                ],
                "correct": 0,
                "explanation": "A Maximum-Minimum thermometer (Six's thermometer) uses metal index markers in a U-tube to record daily peak high and low temperatures.",
                "study_insight": "Maximum-Minimum thermometers capture 24-hour diurnal weather extremes."
            }
        ]
    },
    {
        "id": 16,
        "title": "Anna Mani",
        "subtitle": "The Weather Woman of India & Pioneer of Meteorological Instrumentation",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    India possesses a proud heritage in atmospheric measurement led by pioneering physicist <strong class="text-amber-300 font-semibold">Anna Mani (1918–2001)</strong>, affectionately celebrated as the <em class="text-white">"Weather Woman of India"</em>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Groundbreaking Scientific Contributions</h4>
                    <ul class="space-y-1.5 text-slate-300 leading-relaxed">
                        <li>• <strong class="text-white">Indigenous Meteorological Tools:</strong> Designed and standardized over 100 weather instruments at the India Meteorological Department (IMD) in Pune, freeing India from foreign equipment imports.</li>
                        <li>• <strong class="text-white">Ozonesonde Innovation:</strong> Built the Indian ozonesonde—a high-altitude balloon instrument measuring atmospheric ozone layers long before the ozone hole became a global crisis.</li>
                        <li>• <strong class="text-white">Renewable Energy Mapping:</strong> Set up a nationwide network of solar radiation monitoring stations and wind measuring towers, laying the scientific foundation for India's modern wind and solar power industries!</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">Inspirational Legacy:</strong> Anna Mani proved that precision measurement is the bedrock of scientific discovery, environmental protection, and national self-reliance.
                </div>
            </div>
        """,
        "lecture_script": "To conclude our study of temperature and measurement, let us celebrate the remarkable legacy of Anna Mani, renowned as the Weather Woman of India. Born in Kerala in 1918, Anna Mani conducted research under Nobel Laureate Sir C.V. Raman before joining the India Meteorological Department in Pune. At that time, India had to import nearly all its weather instruments from Europe at huge expense. Anna Mani transformed this completely. She designed, calibrated, and manufactured nearly one hundred precision meteorological instruments indigenously in India—including sensitive barometers, anemometers, and thermometers. She invented the Indian ozonesonde, a lightweight instrument sent into the upper atmosphere via weather balloons to measure ozone concentrations. Later, she mapped solar radiation and wind speeds across the Indian subcontinent, creating the exact scientific maps that power India's modern solar and wind energy farms today. Anna Mani proved that accurate measurement instruments can change the destiny of a nation.",
        "spoken_text": "To conclude our study of temperature and measurement, let us celebrate the remarkable legacy of Anna Mani, renowned as the Weather Woman of India. Born in Kerala in 1918, Anna Mani conducted research under Nobel Laureate Sir C.V. Raman before joining the India Meteorological Department in Pune. At that time, India had to import nearly all its weather instruments from Europe at huge expense. Anna Mani transformed this completely. She designed, calibrated, and manufactured nearly one hundred precision meteorological instruments indigenously in India—including sensitive barometers, anemometers, and thermometers. She invented the Indian ozonesonde, a lightweight instrument sent into the upper atmosphere via weather balloons to measure ozone concentrations. Later, she mapped solar radiation and wind speeds across the Indian subcontinent, creating the exact scientific maps that power India's modern solar and wind energy farms today. Anna Mani proved that accurate measurement instruments can change the destiny of a nation.",
        "checkpoints": [
            {
                "question": "Which pioneering Indian physicist is celebrated as the 'Weather Woman of India' for indigenizing meteorological instruments and ozone measurement?",
                "options": [
                    "Anna Mani",
                    "Janaki Ammal",
                    "Kalpana Chawla",
                    "Tessy Thomas"
                ],
                "correct": 0,
                "explanation": "Anna Mani (1918–2001) pioneered indigenous weather instrument manufacturing, atmospheric ozone monitoring, and solar/wind resource mapping in India.",
                "study_insight": "Anna Mani revolutionized Indian meteorological instrumentation and renewable energy planning."
            },
            {
                "question": "What high-altitude weather balloon device did Anna Mani develop to measure ozone concentrations in the upper atmosphere?",
                "options": [
                    "The Ozonesonde",
                    "The Seismograph",
                    "The Periscope",
                    "The Stethoscope"
                ],
                "correct": 0,
                "explanation": "An ozonesonde is an electrochemical balloon-borne sensor that measures atmospheric ozone profiles as it ascends into the stratosphere.",
                "study_insight": "Ozonesondes provide vertical profiling of Earth's protective ozone layer."
            }
        ]
    }
]

# 40 Mastery Assessment Questions across Slides 17 to 20
QUIZ_QUESTIONS = [
    # Slide 17: Questions 1 to 10 (Challenge 1)
    {
        "id": 1,
        "question": "Why can human skin NOT be relied upon as an objective thermometer?",
        "options": [
            "Because skin senses relative heat transfer based on prior adaptation rather than absolute temperature",
            "Because human skin does not contain any nerve endings",
            "Because skin temperature is always identical to outer space",
            "Because skin reflects 100% of all magnetic fields"
        ],
        "correct": 0,
        "explanation": "Human thermoreceptors respond to the rate and direction of heat flow relative to the skin's baseline temperature, producing subjective and contradictory readings.",
        "solution_html": "<strong>Physiological Proof:</strong> In Activity 7.1 (Three Bowls), the exact same tap water feels warm to a chilled hand and cold to a warmed hand."
    },
    {
        "id": 2,
        "question": "In the Three-Bowl Experiment (Activity 7.1), Hand 1 was in warm water (Bowl A) and Hand 2 was in ice water (Bowl C). When both hands enter room-temperature tap water (Bowl B):",
        "options": [
            "Hand 1 feels the water is cold, while Hand 2 feels the water is warm",
            "Both hands feel the water is boiling hot",
            "Both hands freeze into solid ice",
            "Hand 1 feels warm and Hand 2 feels cold"
        ],
        "correct": 0,
        "explanation": "Hand 1 loses heat to Bowl B (sensing cold), while Hand 2 absorbs heat from Bowl B (sensing warmth).",
        "solution_html": "<strong>Relative Perception:</strong> Heat flows out of Hand 1 (warm -> room water) and into Hand 2 (room water -> cold hand)."
    },
    {
        "id": 3,
        "question": "What is the scientific definition of temperature?",
        "options": [
            "A reliable and objective quantitative measure of the hotness or coldness of a body",
            "The volume of space occupied by steam",
            "The weight of mercury inside a glass bulb",
            "The time taken for water to evaporate"
        ],
        "correct": 0,
        "explanation": "Temperature is the quantitative physical property measuring the degree of hotness or coldness of an object, directly reflecting average molecular kinetic energy.",
        "solution_html": "<strong>Definition:</strong> Temperature is the objective thermal measure of hotness or coldness, measured in °C, °F, or K."
    },
    {
        "id": 4,
        "question": "When an object's temperature increases, what is occurring at the microscopic molecular level?",
        "options": [
            "Its constituent molecules vibrate and collide with greater average kinetic energy",
            "Its atoms stop moving and become completely motionless",
            "Its molecules turn into liquid gold",
            "Its gravitational mass increases tenfold"
        ],
        "correct": 0,
        "explanation": "Temperature is proportional to average microscopic kinetic energy; higher temperature means faster molecular vibrations and collisions.",
        "solution_html": "<strong>Kinetic Theory:</strong> Heat energy directly excites atomic vibrations, raising kinetic speed and thermal temperature."
    },
    {
        "id": 5,
        "question": "Which of the following devices is specifically designed to measure human body temperature?",
        "options": [
            "A clinical thermometer",
            "A laboratory thermometer",
            "A Six's maximum-minimum thermometer",
            "A barometer"
        ],
        "correct": 0,
        "explanation": "A clinical thermometer is calibrated specifically for the human physiological range (35°C to 42°C).",
        "solution_html": "<strong>Instrument Specialty:</strong> Clinical thermometers measure human body heat with high medical precision."
    },
    {
        "id": 6,
        "question": "Why are traditional mercury clinical thermometers being phased out and replaced by digital thermometers?",
        "options": [
            "Mercury is an extremely toxic heavy metal that poses severe poisoning and environmental contamination risks if glass breaks",
            "Mercury is too light and floats away into the sky",
            "Mercury changes into water after one use",
            "Digital thermometers are made of diamond"
        ],
        "correct": 0,
        "explanation": "Mercury is a hazardous neurotoxin with severe disposal and inhalation risks when glass tubes break, leading to international phase-out treaties.",
        "solution_html": "<strong>Toxicology & Safety:</strong> Mercury poisoning risks led to the global adoption of unbreakable, non-toxic digital thermistors."
    },
    {
        "id": 7,
        "question": "How does an electronic digital clinical thermometer measure temperature at its metallic tip?",
        "options": [
            "Using an electronic heat sensor (thermistor) whose electrical resistance changes predictably with temperature",
            "By boiling water inside a miniature chamber",
            "By taking a digital photograph of the tongue",
            "By measuring sound echoes from the teeth"
        ],
        "correct": 0,
        "explanation": "A thermistor's electrical resistance varies in direct relation to temperature. An onboard microchip translates this into a digital LCD number.",
        "solution_html": "<strong>Electronic Mechanism:</strong> Thermistors change electrical conductivity with heat, providing fast, accurate digital readouts."
    },
    {
        "id": 8,
        "question": "How does a non-contact infrared thermometer determine body temperature from several centimetres away?",
        "options": [
            "By detecting the intensity of invisible infrared thermal radiation naturally emitted by warm skin",
            "By firing laser beams that burn the skin surface",
            "By transmitting Wi-Fi signals to the brain",
            "By listening to sound waves"
        ],
        "correct": 0,
        "explanation": "All matter emits infrared radiation proportional to its thermal temperature. The thermometer's sensor detects these thermal emissions without contact.",
        "solution_html": "<strong>Infrared Physics:</strong> Planck's radiation law dictates that emitted infrared intensity corresponds directly to surface temperature."
    },
    {
        "id": 9,
        "question": "Why were non-contact infrared thermometers essential during the COVID-19 pandemic?",
        "options": [
            "They measure temperature without physical contact, preventing pathogen transmission between people",
            "They can cure viral fever within five seconds",
            "They run on solar power without any batteries",
            "They can detect thoughts"
        ],
        "correct": 0,
        "explanation": "Measuring from a distance of 3–5 cm avoids physical contact, eliminating the instrument as a vehicle (fomite) for contagious viral spread.",
        "solution_html": "<strong>Epidemiological Protection:</strong> Non-contact scanning protects healthcare workers and prevents cross-infection."
    },
    {
        "id": 10,
        "question": "What does the display 'Lo' signify when a digital clinical thermometer is first turned on at normal room temperature?",
        "options": [
            "The ambient temperature is lower than the thermometer's lowest measurable limit (around 32°C)",
            "The battery is completely exhausted and must be thrown away",
            "The thermometer is broken",
            "The patient's temperature is below freezing"
        ],
        "correct": 0,
        "explanation": "'Lo' stands for 'Low Temperature' (below 32°C/90°F), indicating that ambient room air is below the clinical range and the device is ready to measure.",
        "solution_html": "<strong>Clinical Indication:</strong> 'Lo' indicates readiness to measure body temperatures above 32°C, not battery failure."
    },

    # Slide 18: Questions 11 to 20 (Challenge 2)
    {
        "id": 11,
        "question": "What is the accepted standard average normal temperature of a healthy human body?",
        "options": [
            "37.0°C (98.6°F)",
            "100.0°C (212.0°F)",
            "0.0°C (32.0°F)",
            "45.0°C (113.0°F)"
        ],
        "correct": 0,
        "explanation": "37.0°C (98.6°F) is the internationally recognized physiological benchmark average for healthy individuals.",
        "solution_html": "<strong>Medical Benchmark:</strong> 37.0°C (98.6°F) represents the statistical mean for human homeostatic body temperature."
    },
    {
        "id": 12,
        "question": "Why is it scientifically inaccurate to claim that every healthy person must have an exact body temperature of 37.0°C at all times?",
        "options": [
            "Because 37.0°C is a statistical average; individual temperatures fluctuate naturally throughout the day (circadian rhythm) and with activity",
            "Because human bodies never have temperatures higher than 10°C",
            "Because thermometers always produce random numbers",
            "Because body temperature changes only once every ten years"
        ],
        "correct": 0,
        "explanation": "Normal body temperature varies naturally across a daily circadian rhythm (lower at dawn, higher in late afternoon) and with physical exertion.",
        "solution_html": "<strong>Circadian Fluctuation:</strong> Normal body temperature exists within a healthy range (~36.4°C to ~37.3°C) around the 37.0°C average."
    },
    {
        "id": 13,
        "question": "What is the official base unit of temperature in the International System of Units (SI)?",
        "options": [
            "Kelvin (K)",
            "Degree Celsius (°C)",
            "Degree Fahrenheit (°F)",
            "Joule (J)"
        ],
        "correct": 0,
        "explanation": "The Kelvin (symbol K) is the base SI unit of thermodynamic temperature.",
        "solution_html": "<strong>SI Metrology:</strong> The SI base unit is Kelvin (K). Celsius (°C) is an approved derived unit, and Fahrenheit is customary."
    },
    {
        "id": 14,
        "question": "What is the freezing point and boiling point of pure water on the Celsius scale at standard sea-level pressure?",
        "options": [
            "Freezing point: 0°C; Boiling point: 100°C",
            "Freezing point: 32°C; Boiling point: 212°C",
            "Freezing point: 0°C; Boiling point: 50°C",
            "Freezing point: -10°C; Boiling point: 110°C"
        ],
        "correct": 0,
        "explanation": "The Celsius scale is defined with 0°C as the melting/freezing point of pure water and 100°C as its boiling point at 1 atmosphere pressure.",
        "solution_html": "<strong>Celsius Calibration:</strong> 0°C (ice point) to 100°C (steam point) with 100 equal degree intervals."
    },
    {
        "id": 15,
        "question": "How many degree intervals exist between the freezing point of water and the boiling point of water on the Fahrenheit scale?",
        "options": [
            "180 degrees (from 32°F to 212°F)",
            "100 degrees (from 0°F to 100°F)",
            "37 degrees (from 0°F to 37°F)",
            "273 degrees (from 0°F to 273°F)"
        ],
        "correct": 0,
        "explanation": "On the Fahrenheit scale, water freezes at 32°F and boils at 212°F. The interval is 212 - 32 = 180 degrees.",
        "solution_html": "<strong>Fahrenheit Scale:</strong> 212°F - 32°F = 180 equal intervals between fundamental calibration points."
    },
    {
        "id": 16,
        "question": "Which of the following temperature notations violates international scientific grammar standards?",
        "options": [
            "310 °K (writing a degree symbol with Kelvin)",
            "37.0 °C",
            "98.6 °F",
            "300 K"
        ],
        "correct": 0,
        "explanation": "Kelvin is an absolute thermodynamic temperature scale and must never be written with a degree symbol. Writing '°K' is strictly incorrect; it should be written as 'K'.",
        "solution_html": "<strong>SI Grammar Rule:</strong> Write 310 K, never 310 °K. Both Celsius (°C) and Fahrenheit (°F) use the degree symbol, but Kelvin does not."
    },
    {
        "id": 17,
        "question": "What is the typical measurement range of a standard laboratory glass thermometer?",
        "options": [
            "-10°C to 110°C",
            "35°C to 42°C",
            "0°C to 37°C",
            "98°C to 108°C"
        ],
        "correct": 0,
        "explanation": "Laboratory thermometers are graduated to measure from -10°C (sub-freezing) up to 110°C (above boiling water).",
        "solution_html": "<strong>Lab Scale Range:</strong> Spans -10°C to 110°C to accommodate melting ice and boiling liquids."
    },
    {
        "id": 18,
        "question": "Why does a laboratory thermometer NOT have a constriction (kink) in its capillary tube above the bulb?",
        "options": [
            "Because it is designed to measure temperature changes continuously in real time while immersed",
            "Because glass blowers forgot to bend the tube",
            "Because a kink would make the thermometer explode at 100°C",
            "Because a kink would turn the liquid into gas"
        ],
        "correct": 0,
        "explanation": "Laboratory experiments require real-time continuous tracking of rising and falling temperatures, which an unconstricted capillary provides.",
        "solution_html": "<strong>Open Capillary Purpose:</strong> Real-time dynamic response requires free liquid expansion and contraction without a kink."
    },
    {
        "id": 19,
        "question": "What happens if you remove a laboratory thermometer from a beaker of hot water to read it in the air?",
        "options": [
            "The liquid column falls immediately due to exposure to cooler room air, corrupting the measurement",
            "The reading stays locked forever",
            "The glass tube shatters instantly into dust",
            "The liquid column turns bright purple"
        ],
        "correct": 0,
        "explanation": "Because there is no constriction, the liquid contracts immediately upon contact with cooler ambient air.",
        "solution_html": "<strong>The Immersion Rule:</strong> Laboratory thermometers must be read while the bulb remains immersed in the liquid."
    },
    {
        "id": 20,
        "question": "If there are 5 small subdivisions between the 10°C and 20°C marks on a thermometer, what temperature value does each single mark represent?",
        "options": [
            "2°C",
            "1°C",
            "0.5°C",
            "5°C"
        ],
        "correct": 0,
        "explanation": "Major span = 20°C - 10°C = 10°C. Least count = 10°C ÷ 5 = 2°C per division.",
        "solution_html": "<strong>Least Count Math:</strong> Least Count = (20 - 10) / 5 = 10 / 5 = 2°C per division."
    },

    # Slide 19: Questions 21 to 30 (Challenge 3)
    {
        "id": 21,
        "question": "If there are 10 small subdivisions between 0°C and 1°C on a precision thermometer, what is its least count?",
        "options": [
            "0.1°C",
            "1°C",
            "0.5°C",
            "0.01°C"
        ],
        "correct": 0,
        "explanation": "Least Count = 1°C ÷ 10 = 0.1°C per division.",
        "solution_html": "<strong>Precision Calculation:</strong> 1°C / 10 divisions = 0.1°C per mark."
    },
    {
        "id": 22,
        "question": "Why must the bulb of a laboratory thermometer be completely immersed in the liquid without touching the bottom or sides of the beaker?",
        "options": [
            "The container walls are affected by direct flame heating or room air, giving a false reading of the container rather than the liquid",
            "The bulb will stick permanently to the glass beaker",
            "The beaker will shatter from electric shock",
            "The liquid will stop boiling"
        ],
        "correct": 0,
        "explanation": "The beaker base conducts direct heat from the burner, and the walls lose heat to room air. The bulb must measure the fluid itself.",
        "solution_html": "<strong>Isolation Precaution:</strong> Measuring bulk fluid requires free suspension away from heated or cooled container boundaries."
    },
    {
        "id": 23,
        "question": "How should an observer position their eye when reading a thermometer to avoid parallax error?",
        "options": [
            "Exactly horizontal and perpendicular to the top level of the liquid column",
            "Looking down steeply from above the liquid column",
            "Looking up from beneath the beaker",
            "Holding the thermometer at arm's length while walking"
        ],
        "correct": 0,
        "explanation": "Parallax error is eliminated when the line of sight is at an exact 90° right angle to the scale at the level of the meniscus.",
        "solution_html": "<strong>Optical Alignment:</strong> Horizontal eye alignment prevents angular displacement between the meniscus and the etched scale."
    },
    {
        "id": 24,
        "question": "What is observed when a thermometer is placed into a beaker of pure melting ice?",
        "options": [
            "The temperature remains constant at 0°C until all the ice has melted",
            "The temperature rises continuously from -10°C to 50°C during melting",
            "The temperature drops to -100°C",
            "The thermometer liquid boils"
        ],
        "correct": 0,
        "explanation": "During a phase transition (solid to liquid), the temperature remains locked at 0°C as latent heat melts the crystal lattice.",
        "solution_html": "<strong>Phase Plateau:</strong> Pure ice melts at a fixed 0°C plateau under standard pressure."
    },
    {
        "id": 25,
        "question": "Where does the heat energy go when room heat enters a beaker of melting ice without raising its temperature above 0°C?",
        "options": [
            "It is used as latent heat of fusion to break the crystalline bonds between ice molecules",
            "It disappears from the universe completely",
            "It is transformed into nuclear radiation",
            "It is reflected back into the room as green light"
        ],
        "correct": 0,
        "explanation": "Latent heat of fusion breaks intermolecular bonds during melting, altering phase without increasing kinetic temperature.",
        "solution_html": "<strong>Latent Heat of Fusion:</strong> Energy absorbed during melting breaks crystal bonds, holding temperature at 0°C."
    },
    {
        "id": 26,
        "question": "What happens to the temperature of water in an open beaker once it reaches a vigorous boil at sea level?",
        "options": [
            "It remains strictly locked at 100°C regardless of how high the flame is turned",
            "It increases by 10°C every minute",
            "It jumps immediately to 200°C",
            "It drops back to 0°C"
        ],
        "correct": 0,
        "explanation": "In an open vessel at 1 atmosphere, boiling water remains at 100°C; excess heat supplies latent heat of vaporization to generate steam.",
        "solution_html": "<strong>Boiling Plateau:</strong> Liquid water cannot exceed its boiling point (100°C at 1 atm) in an open container."
    },
    {
        "id": 27,
        "question": "What is the primary function of a room thermometer mounted on a wall?",
        "options": [
            "To measure the ambient air temperature of an indoor space",
            "To measure human fever from five metres away",
            "To detect earthquakes",
            "To regulate the electrical voltage of appliances"
        ],
        "correct": 0,
        "explanation": "Room thermometers measure ambient air temperature to monitor indoor climate, comfort, and storage conditions.",
        "solution_html": "<strong>Ambient Measurement:</strong> Wall-mounted room thermometers display indoor atmospheric temperature."
    },
    {
        "id": 28,
        "question": "Why does the maximum daily air temperature typically occur in early afternoon (around 2:00 PM to 3:00 PM) rather than at 12:00 noon when the sun is highest?",
        "options": [
            "Because solar heat accumulates in the ground and air for several hours after noon before heat loss exceeds incoming solar radiation",
            "Because the sun turns off at noon",
            "Because wind stops blowing in the afternoon",
            "Because clocks run slower in the morning"
        ],
        "correct": 0,
        "explanation": "Thermal inertia causes a lag: the earth's surface continues absorbing more radiation than it emits for a few hours past solar noon.",
        "solution_html": "<strong>Thermal Lag:</strong> Maximum temperature occurs in early afternoon due to cumulative ground and atmospheric heating."
    },
    {
        "id": 29,
        "question": "What is the primary scientific achievement of Anna Mani, celebrated as the 'Weather Woman of India'?",
        "options": [
            "She designed and manufactured over 100 indigenous meteorological instruments and pioneered ozone and solar radiation monitoring in India",
            "She discovered the planet Neptune",
            "She invented the steam engine",
            "She built the first nuclear submarine"
        ],
        "correct": 0,
        "explanation": "Anna Mani standardized Indian weather instrumentation at IMD, developed the Indian ozonesonde, and mapped solar and wind resources.",
        "solution_html": "<strong>Anna Mani's Legacy:</strong> Pioneered indigenous meteorological instruments, atmospheric ozone profiling, and renewable energy resource mapping."
    },
    {
        "id": 30,
        "question": "What is an ozonesonde, the instrument developed by Anna Mani for atmospheric research?",
        "options": [
            "A balloon-borne instrument that measures the concentration of ozone at various altitudes in the atmosphere",
            "A telescope used to look at the Moon",
            "A device for measuring the depth of ocean trenches",
            "A medical probe for checking ear infections"
        ],
        "correct": 0,
        "explanation": "An ozonesonde is an electrochemical instrument carried aloft by weather balloons to record vertical ozone profiles in the stratosphere.",
        "solution_html": "<strong>Atmospheric Tool:</strong> Ozonesondes measure ozone concentrations throughout atmospheric layers."
    },

    # Slide 20: Questions 31 to 40 (Challenge 4)
    {
        "id": 31,
        "question": "What is the temperature reading when water freezes on the Fahrenheit scale?",
        "options": [
            "32°F",
            "0°F",
            "100°F",
            "212°F"
        ],
        "correct": 0,
        "explanation": "On the Fahrenheit scale, the freezing point of pure water is defined as 32°F.",
        "solution_html": "<strong>Fahrenheit Freezing Point:</strong> 0°C corresponds exactly to 32°F."
    },
    {
        "id": 32,
        "question": "A person has a fever of 102°F. What scale is being used to report this body temperature?",
        "options": [
            "The Fahrenheit scale",
            "The Celsius scale",
            "The Kelvin scale",
            "The Richter scale"
        ],
        "correct": 0,
        "explanation": "A temperature of 102°F is on the Fahrenheit scale (equivalent to ~38.9°C). On the Celsius scale, 102°C would be above boiling water!",
        "solution_html": "<strong>Clinical Scale Context:</strong> A fever of 102° is Fahrenheit (102°F = 38.9°C)."
    },
    {
        "id": 33,
        "question": "Convert 0°C into the Kelvin scale:",
        "options": [
            "273.15 K",
            "0 K",
            "100 K",
            "-273.15 K"
        ],
        "correct": 0,
        "explanation": "Kelvin = Celsius + 273.15. Therefore, 0°C = 0 + 273.15 = 273.15 K.",
        "solution_html": "<strong>Formula:</strong> K = °C + 273.15. At 0°C, K = 273.15 K."
    },
    {
        "id": 34,
        "question": "Convert 100°C (the boiling point of water) into the Kelvin scale:",
        "options": [
            "373.15 K",
            "273.15 K",
            "100 K",
            "0 K"
        ],
        "correct": 0,
        "explanation": "K = 100 + 273.15 = 373.15 K.",
        "solution_html": "<strong>Kelvin Boiling Point:</strong> 100°C = 373.15 K."
    },
    {
        "id": 35,
        "question": "What is 'absolute zero' (0 K) in the study of temperature?",
        "options": [
            "The lowest theoretical temperature possible, where all classical molecular motion ceases (-273.15°C)",
            "The freezing point of tap water",
            "The average temperature of a refrigerator",
            "The temperature of boiling liquid nitrogen"
        ],
        "correct": 0,
        "explanation": "Absolute zero (0 K or -273.15°C) is the theoretical lower limit of thermodynamic temperature where thermal particle motion reaches its minimum.",
        "solution_html": "<strong>Absolute Zero:</strong> 0 K (-273.15°C) is the absolute floor of physical temperature."
    },
    {
        "id": 36,
        "question": "Why is alcohol often used instead of mercury in low-temperature laboratory thermometers?",
        "options": [
            "Alcohol has a much lower freezing point (-114°C) than mercury (-39°C), allowing it to measure extreme Arctic cold",
            "Alcohol is solid at room temperature",
            "Alcohol is magnetic",
            "Alcohol boils at 1000°C"
        ],
        "correct": 0,
        "explanation": "Mercury freezes solid at -38.8°C, making it useless in polar climates. Pure ethanol freezes at -114°C, allowing sub-zero measurement.",
        "solution_html": "<strong>Freezing Point Physics:</strong> Ethanol remains liquid down to -114°C, whereas mercury freezes at -39°C."
    },
    {
        "id": 37,
        "question": "What liquid is commonly dyed red in school laboratory thermometers to ensure high visual contrast?",
        "options": [
            "Ethanol (alcohol) with red dye",
            "Red molten iron",
            "Strawberry juice",
            "Red liquid mercury"
        ],
        "correct": 0,
        "explanation": "School thermometers frequently use red-dyed alcohol because it is non-toxic, expands uniformly, and is clearly visible against the glass.",
        "solution_html": "<strong>Thermometric Fluid:</strong> Red-dyed ethanol provides safe, high-visibility capillary tracking."
    },
    {
        "id": 38,
        "question": "A student measures boiling water using four thermometers: Thermometer A reads 99.8°C, B reads 100.1°C, C reads 100.0°C, and D reads 100.2°C. Why do these slight variations occur?",
        "options": [
            "Slight differences in thermometer manufacturing calibration, minor local air pressure differences, and impurities in water",
            "The water is changing into liquid mercury",
            "The student is standing upside down",
            "Thermometers never agree because temperature does not exist"
        ],
        "correct": 0,
        "explanation": "Minor instrument calibration tolerances, local atmospheric barometric variations, and trace dissolved minerals naturally cause variations around 100°C.",
        "solution_html": "<strong>Measurement Variability:</strong> Experimental tolerance and atmospheric pressure influence boiling readings."
    },
    {
        "id": 39,
        "question": "How did Anna Mani's wind and solar radiation measurements contribute to modern India's economy?",
        "options": [
            "Her data maps identified the optimal locations across India for establishing modern wind farms and solar power installations",
            "She discovered offshore oil reserves",
            "She built nuclear power plants",
            "She designed coal trains"
        ],
        "correct": 0,
        "explanation": "Anna Mani published foundational wind and solar resource data books that guided the site selection for India's massive renewable energy infrastructure.",
        "solution_html": "<strong>Renewable Infrastructure:</strong> Anna Mani's solar and wind surveys laid the groundwork for India's clean energy transition."
    },
    {
        "id": 40,
        "question": "Which of the following summaries best expresses the core lesson of Chapter 7: Temperature and its Measurement?",
        "options": [
            "Touch is a subjective perception; temperature is the objective quantitative measure of thermal energy, requiring calibrated tools and scientific protocols",
            "All bodies in the universe have the same temperature",
            "Thermometers should always be removed from hot liquids before reading",
            "Human body temperature is 100°C"
        ],
        "correct": 0,
        "explanation": "Chapter 7 demonstrates the subjectivity of touch, defines temperature objectively, introduces clinical and lab thermometers, and outlines precision protocols.",
        "solution_html": "<strong>Chapter Synthesis:</strong> Objective thermometry replaces subjective touch, ensuring accuracy in clinical healthcare and scientific investigation."
    }
]

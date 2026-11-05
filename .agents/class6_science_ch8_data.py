"""
NCERT Class 6 Science - Chapter 8: A Journey through States of Water
Curriculum Data Module (NEP 2020 Curiosity Syllabus)
Zero raw LaTeX. All instructional content spoken as lecture. Exercises excluded. Zero lecturer names.
"""

CHAPTER_META = {
    "title": "A Journey through States of Water",
    "class": "Class 6",
    "subject": "Science",
    "chapter": 8,
    "book": "Curiosity",
    "total_slides": 20,
    "concept_slides": 16,
    "quiz_slides": 4,
    "total_checkpoints": 32,
    "total_quiz_questions": 40
}

SLIDES = [
    {
        "id": 1,
        "title": "Ice & Flow",
        "subtitle": "Activity 8.1: A Tale of Two States - Shikanji, Ice, and Fluid Water",
        "concept_html": "\n            <blockquote class='p-3 rounded-xl bg-slate-900 border-l-4 border-indigo-500 text-xs italic text-slate-300 mb-3'>\n                \"If it does not rain well, even the mighty ocean will be drained.\"\n                <span class='block text-right text-indigo-400 font-semibold mt-1'>- Thirukkural</span>\n            </blockquote>\n            <p class='mb-2'>On a bright, scorching summer afternoon, two friends, Aavi and Thirav, sit down to enjoy a glass of cold <strong>shikanji</strong> (lemonade). Clinking inside their glasses are translucent, solid blocks of ice.</p>\n            <p class='mb-2'>Thirav ponders aloud: <em>\"Ice feels hard, rigid, and can be held firmly in our hands. Liquid water slips right through our fingers and flows away. How could they possibly be the same thing?\"</em></p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs'>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-bold'>Observation</span>\n                    <span class='text-slate-300'>Place an ice cube in a bowl at room temperature (Activity 8.1). Within minutes, the rigid crystal softens and converts entirely into clear, liquid water.</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold'>Conclusion</span>\n                    <span class='text-slate-300'>Ice and water are <strong>two physical states of the exact same chemical substance</strong>. No extra ingredients are added in the freezer; temperature alone transforms its state!</span>\n                </div>\n            </div>\n        ",
        "lecture_script": "Welcome to A Journey through States of Water. On a bright summer afternoon, friends Aavi and Thirav enjoyed a glass of cold shikanji with ice cubes clinking inside. Thirav wondered about the nature of ice. Ice is hard to touch, rigid, and holds its shape in our hands, whereas liquid water cannot be held without a container and flows freely. Aavi argued that ice and water are simply two forms of the exact same substance. To prove this, let us perform Activity 8.1. Place an ice cube in a cup on a table at room temperature. Soon, the solid ice melts into clear liquid water. If you place that water back into a freezer, it turns back into solid ice. Temperature alone governs whether water exists as a rigid solid or a flowing liquid.",
        "spoken_text": "On a bright summer afternoon, friends Aavi and Thirav enjoyed a glass of cold shikanji with ice cubes clinking inside. Thirav wondered about the nature of ice. Ice is hard to touch, rigid, and holds its shape in our hands, whereas liquid water cannot be held without a container and flows freely. Aavi argued that ice and water are simply two forms of the exact same substance. To prove this, let us perform Activity 8.1. Place an ice cube in a cup on a table at room temperature. Soon, the solid ice melts into clear liquid water. If you place that water back into a freezer, it turns back into solid ice. Temperature alone governs whether water exists as a rigid solid or a flowing liquid.",
        "checkpoints": [
            {
                "question": "What happens when an ice cube is placed in an open cup at room temperature?",
                "options": [
                    "It reacts chemically with air and vanishes permanently",
                    "It absorbs thermal energy from the surroundings and melts into liquid water",
                    "It gains mass as room air crystallizes around it",
                    "It changes its fundamental chemical composition into a new liquid"
                ],
                "correct": 1,
                "explanation": "Ice absorbs ambient thermal energy at room temperature, causing its rigid solid structure to collapse into flowing liquid water of identical chemical nature.",
                "study_insight": "Physical changes of state alter molecular arrangement and thermal energy without altering the identity of the substance."
            },
            {
                "question": "Which of the following properties distinguishes liquid water from solid ice?",
                "options": [
                    "Liquid water has a fixed rigid shape while ice takes the container shape",
                    "Liquid water flows and splashes easily whereas solid ice retains its rigid shape",
                    "Ice has a higher temperature than liquid water",
                    "Water can only be frozen if special chemicals are added in the refrigerator"
                ],
                "correct": 1,
                "explanation": "Liquids exhibit fluidity and deformation under gravity, allowing water to flow and splash, whereas solids resist deformation and maintain fixed geometric forms.",
                "study_insight": "Fluidity is the defining mechanical property of liquids and gases compared to rigid solids."
            }
        ]
    },
    {
        "id": 2,
        "title": "Puddle Fade",
        "subtitle": "Section 8.1: Investigating Water's Vanishing Act Across Earth's Surfaces",
        "concept_html": "\n            <p class='mb-2'>It is a brisk, rainy morning. On their morning walk to school, students navigate around dozens of muddy <strong>water puddles</strong> scattered across the school playground.</p>\n            <p class='mb-2'>By afternoon, when they return outdoors to play games, the ground is entirely dry and the puddles have completely vanished! Where did the water go?</p>\n            <div class='grid grid-cols-2 gap-3 my-3 text-xs'>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800'>\n                    <div class='font-bold text-amber-400 mb-1'>Hypothesis A: Soil Absorption</div>\n                    <p class='text-slate-300'>Puddle water soaks directly into porous soil and sand particles, moving downward into underground aquifers.</p>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800'>\n                    <div class='font-bold text-cyan-400 mb-1'>The Utensil Counter-Proof</div>\n                    <p class='text-slate-300'>After washing stainless steel utensils, thin layers of water droplets on non-porous metal dry up completely without seeping through solid metal!</p>\n                </div>\n            </div>\n            <p class='text-xs text-slate-300 leading-relaxed'>While soil does absorb rainwater, the fact that water vanishes from impermeable steel, stone, and glass proves that water also enters the atmosphere as an invisible gas.</p>\n        ",
        "lecture_script": "Section 8.1 explores water's disappearing act. On a rainy morning, children notice wide puddles across the school playground. But when they come out to play in the evening, the water in the puddles has mysteriously vanished. Thirav suggests that the water simply soaked into the playground soil. Soil does absorb water, but consider another everyday clue. When you wash stainless steel utensils, thin films of water remain on their surfaces. Within an hour, the utensils are bone-dry. Steel is completely impermeable and has no pores. Water cannot soak through metal. Therefore, another powerful natural process must be causing water to disappear into thin air.",
        "spoken_text": "On a rainy morning, children notice wide puddles across the school playground. But when they come out to play in the evening, the water in the puddles has mysteriously vanished. Thirav suggests that the water simply soaked into the playground soil. Soil does absorb water, but consider another everyday clue. When you wash stainless steel utensils, thin films of water remain on their surfaces. Within an hour, the utensils are bone-dry. Steel is completely impermeable and has no pores. Water cannot soak through metal. Therefore, another powerful natural process must be causing water to disappear into thin air.",
        "checkpoints": [
            {
                "question": "Why does the drying of washed steel utensils prove that water disappearance is not solely due to absorption into the ground?",
                "options": [
                    "Stainless steel plates are porous like soil",
                    "Water cannot seep through non-porous solid metal, proving it escapes into the air",
                    "Utensils absorb water internally through magnetic attraction",
                    "Water on metal plates decomposes into hydrogen gas instantly"
                ],
                "correct": 1,
                "explanation": "Solid stainless steel is impermeable to water. If water disappears from its surface, it must escape into the surrounding atmosphere rather than seeping through the material.",
                "study_insight": "Testing a phenomenon on an impermeable surface isolates atmospheric phase change from underground percolation."
            },
            {
                "question": "What happens to the water in playground puddles on a sunny, windy afternoon?",
                "options": [
                    "It exclusively drains into deep underground caverns",
                    "It partly seeps into the soil and partly evaporates into the atmosphere as water vapour",
                    "It converts into solid crystals on the grass",
                    "It is consumed entirely by earthworms"
                ],
                "correct": 1,
                "explanation": "In an open playground, water loss occurs through two simultaneous channels: gravity-driven percolation into the soil and evaporation into the atmosphere.",
                "study_insight": "Environmental water loss is a combination of surface evaporation and soil infiltration."
            }
        ]
    },
    {
        "id": 3,
        "title": "Plate Test",
        "subtitle": "Activity 8.2: Testing Seepage vs Gaseous Evaporation on Non-Porous Surfaces",
        "concept_html": "\n            <p class='mb-2'>To determine conclusively whether water seeps through solid containers or escapes into the air, we conduct <strong>Activity 8.2</strong> using a clean stainless steel plate.</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs my-2'>\n                <div class='flex items-center gap-2'>\n                    <span class='w-5 h-5 rounded-full bg-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center shrink-0'>1</span>\n                    <span class='text-slate-300'>Place exactly one tablespoon of water onto the upper surface of a dry steel plate.</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='w-5 h-5 rounded-full bg-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center shrink-0'>2</span>\n                    <span class='text-slate-300'>Lift and inspect the bottom underside of the plate. It remains completely dry with zero droplets.</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='w-5 h-5 rounded-full bg-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center shrink-0'>3</span>\n                    <span class='text-slate-300'>Observe the plate at regular 15-minute intervals at room temperature until the water disappears.</span>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200 mt-2'>\n                <strong>Scientific Law:</strong> The liquid water on the plate was converted into a gaseous state called <strong>water vapour</strong>, dispersing invisibly into the surrounding ambient room air.\n            </div>\n        ",
        "lecture_script": "Let us examine Activity 8.2 to verify what happens to water on an impermeable surface. Take a stainless steel plate and pour one tablespoon of water onto its top face. Check underneath the plate. The underside is completely dry, confirming that water cannot seep through solid metal. Leave the plate undisturbed and observe it every fifteen minutes. Slowly, the water pool shrinks in diameter, and after some time, it completely vanishes. Because the underside never became wet, the water could not have leaked downward. Instead, it transitioned from a liquid into a gaseous state called water vapour, dispersing directly into the air of the room.",
        "spoken_text": "Let us examine Activity 8.2 to verify what happens to water on an impermeable surface. Take a stainless steel plate and pour one tablespoon of water onto its top face. Check underneath the plate. The underside is completely dry, confirming that water cannot seep through solid metal. Leave the plate undisturbed and observe it every fifteen minutes. Slowly, the water pool shrinks in diameter, and after some time, it completely vanishes. Because the underside never became wet, the water could not have leaked downward. Instead, it transitioned from a liquid into a gaseous state called water vapour, dispersing directly into the air of the room.",
        "checkpoints": [
            {
                "question": "What key observation during Activity 8.2 rules out the hypothesis that water leaks through the steel plate?",
                "options": [
                    "The water turns into ice before evaporating",
                    "The underside of the steel plate remains completely dry throughout the experiment",
                    "The plate becomes heavier over time",
                    "The water produces bubbles of oxygen gas"
                ],
                "correct": 1,
                "explanation": "Because the bottom of the plate remains dry, water molecules do not permeate the solid steel; they leave from the top surface into the air.",
                "study_insight": "A dry underside confirms that phase change to the gaseous state occurs exclusively at the exposed upper boundary."
            },
            {
                "question": "What is the name of the gaseous state of water that forms when liquid water dries up?",
                "options": [
                    "Liquid oxygen",
                    "Water vapour",
                    "Carbon monoxide",
                    "Ozone"
                ],
                "correct": 1,
                "explanation": "Water in its gaseous phase is called water vapour, which is colorless, odorless, and transparent.",
                "study_insight": "Water vapour is the gaseous phase of water and is a natural, invisible component of Earth's atmosphere."
            }
        ]
    },
    {
        "id": 4,
        "title": "Steam Mist",
        "subtitle": "The Physics of Evaporation: Dosa Griddles, Ambient Heat, and Invisible Molecules",
        "concept_html": "\n            <p class='mb-2'>When preparing a dosa, cooks often sprinkle a few drops of water onto a smoking-hot iron tawa (griddle). Instantly, a loud hiss erupts and a cloud of white mist billows upward before vanishing!</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs mb-3'>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-bold'>Water Vapour</span>\n                    <span class='text-slate-300'>True water vapour consists of individual, separate gaseous water molecules. It is <strong>completely invisible</strong> to the human eye.</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-bold'>Visible Steam</span>\n                    <span class='text-slate-300'>The white clouds seen above boiling kettles or hot tawas are actually <em>liquid micro-droplets</em> suspended in air, formed when hot vapour cools and condenses.</span>\n                </div>\n            </div>\n            <div class='p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-200'>\n                <strong>Definition of Evaporation:</strong> The continuous physical process by which a liquid converts into its gaseous vapour state at any temperature below its boiling point.\n            </div>\n            <p class='text-xs text-slate-400 mt-2'>Evaporation operates continuously at all room temperatures: drying wet laundry, clearing mopped floors, and evaporating perspiration from human skin.</p>\n        ",
        "lecture_script": "When making a dosa, we sprinkle droplets of water onto a hot griddle. The water sizzles and instantly disappears as a puff of steam. But what is steam, and how does it relate to water vapour? Scientifically, water vapour is entirely invisible. You cannot see it with your naked eyes. What you see as white billowing steam is actually millions of microscopic water droplets that have already begun to condense back into liquid in cooler air. The conversion of liquid water into its vapour state is formally termed evaporation. Evaporation does not require a roaring flame or boiling temperatures. It takes place continuously all the time, even at room temperature. When clothes dry on a washing line, when wet floors dry after mopping, or when hand sanitizer dries on your palms, evaporation is at work.",
        "spoken_text": "When making a dosa, we sprinkle droplets of water onto a hot griddle. The water sizzles and instantly disappears as a puff of steam. But what is steam, and how does it relate to water vapour? Scientifically, water vapour is entirely invisible. You cannot see it with your naked eyes. What you see as white billowing steam is actually millions of microscopic water droplets that have already begun to condense back into liquid in cooler air. The conversion of liquid water into its vapour state is formally termed evaporation. Evaporation does not require a roaring flame or boiling temperatures. It takes place continuously all the time, even at room temperature. When clothes dry on a washing line, when wet floors dry after mopping, or when hand sanitizer dries on your palms, evaporation is at work.",
        "checkpoints": [
            {
                "question": "Why is true water vapour invisible to human eyes?",
                "options": [
                    "It absorbs all wavelengths of visible light",
                    "It exists as dispersed individual molecules that do not scatter visible light",
                    "It only exists in outer space",
                    "It is shielded by atmospheric nitrogen molecules"
                ],
                "correct": 1,
                "explanation": "True water vapour consists of separated gas molecules too small to scatter light. The visible white clouds called steam are actually tiny suspended liquid water droplets.",
                "study_insight": "Water vapour is a clear, transparent gas; visible steam is an aerosol of condensed liquid water droplets."
            },
            {
                "question": "Which of the following processes represents an everyday example of evaporation at room temperature?",
                "options": [
                    "Freezing water in an ice tray inside a freezer",
                    "Drying of freshly mopped tile floors in a living room",
                    "Melting of a candle wax stick near a flame",
                    "Dissolving sugar crystals in hot milk"
                ],
                "correct": 1,
                "explanation": "Water spread across a mopped floor absorbs room thermal energy and continuously evaporates into gaseous water vapour.",
                "study_insight": "Evaporation is a surface phenomenon occurring at any temperature below the boiling point."
            }
        ]
    },
    {
        "id": 5,
        "title": "Cold Glass",
        "subtitle": "Activity 8.3: The Mystery of Droplets Forming on the Outer Wall of an Icy Glass",
        "concept_html": "\n            <p class='mb-2'>The following day, Aavi and Thirav prepare another batch of chilled lemonade. They fill a clear glass tumbler with cold water and drop several cubes of solid ice into it (<strong>Activity 8.3</strong>).</p>\n            <p class='mb-2'>After five minutes of sitting undisturbed on the dining table, a surprising transformation occurs on the <em>outer exterior surface</em> of the glass!</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-2 my-2'>\n                <div class='text-amber-400 font-bold'>Key Observations:</div>\n                <ul class='list-disc pl-5 text-slate-300 space-y-1'>\n                    <li>Fine, tiny misty droplets gradually appear on the outside of the dry glass tumbler.</li>\n                    <li>As time passes, small droplets coalesce and combine into larger, heavy droplets that trickle downward.</li>\n                    <li>Touching the exterior reveals cold, wet moisture where the surface was previously bone-dry.</li>\n                </ul>\n            </div>\n            <div class='p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-slate-300'>\n                <strong>Critical Question:</strong> Did the lemonade water somehow leak through the solid glass wall, or did ice magically escape over the rim? What is the true source of this exterior water?\n            </div>\n        ",
        "lecture_script": "Section 8.2 presents another intriguing mystery. Friends make lemonade by pouring cold water into a glass tumbler and adding ice cubes. After leaving it undisturbed for five minutes, fine droplets of water begin to form on the outer surface of the tumbler. Initially, tiny misty beads appear. As more beads deposit, they merge together to form larger droplets that run down the exterior wall. If you run your finger along the outside, it comes away wet and cold. Where did these water droplets come from? Did water leak through microscopic cracks in the glass? Did ice melt and overflow? Or is there water in the surrounding air waiting to be discovered?",
        "spoken_text": "Section 8.2 presents another intriguing mystery. Friends make lemonade by pouring cold water into a glass tumbler and adding ice cubes. After leaving it undisturbed for five minutes, fine droplets of water begin to form on the outer surface of the tumbler. Initially, tiny misty beads appear. As more beads deposit, they merge together to form larger droplets that run down the exterior wall. If you run your finger along the outside, it comes away wet and cold. Where did these water droplets come from? Did water leak through microscopic cracks in the glass? Did ice melt and overflow? Or is there water in the surrounding air waiting to be discovered?",
        "checkpoints": [
            {
                "question": "What happens on the outer wall of a glass tumbler containing ice cubes left undisturbed for five minutes?",
                "options": [
                    "The glass becomes frosty and catches fire",
                    "Tiny water droplets appear, coalesce into larger drops, and trickle down the exterior",
                    "The glass wall dissolves and turns into liquid",
                    "Air inside the glass escapes through the glass bottom"
                ],
                "correct": 1,
                "explanation": "Chilled outer glass walls cool adjacent ambient air, causing airborne water vapour to condense into visible liquid beads on the exterior.",
                "study_insight": "Outer wall droplet formation is a universal thermal phenomenon seen on any cold container, including glass, metal, and ceramic."
            },
            {
                "question": "If you repeat Activity 8.3 with water at normal room temperature instead of ice water, what do you observe on the outer glass surface?",
                "options": [
                    "Twice as many water droplets form",
                    "No water droplets appear on the outer surface",
                    "The glass immediately cracks into pieces",
                    "The glass turns completely opaque"
                ],
                "correct": 1,
                "explanation": "Room-temperature water does not cool the glass below the surrounding air's dew point; therefore, airborne water vapour does not condense and the surface stays dry.",
                "study_insight": "A temperature difference between the cold surface and the ambient air is essential to trigger condensation."
            }
        ]
    },
    {
        "id": 6,
        "title": "Dew Drops",
        "subtitle": "Activity 8.4: Proving Condensation via Digital Balance Mass Measurements",
        "concept_html": "\n            <p class='mb-2'>To scientifically prove that exterior droplets do <strong>not</strong> seep from inside the tumbler, Aavi and Thirav design an ingenious quantitative experiment (<strong>Activity 8.4</strong>):</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs mb-3'>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-bold'>Step 1</span>\n                    <span class='text-slate-300'>Fill a glass tumbler half-full of ice water. Cover its mouth with a small steel plate to prevent internal evaporation. Mark the water level with permanent ink.</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-bold'>Step 2</span>\n                    <span class='text-slate-300'>Place the entire assembly on a precision digital balance and record the initial mass at time 0 min (e.g. 250.0 g).</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold'>Step 3</span>\n                    <span class='text-slate-300'>Record readings every 5 minutes for 30 minutes. The mass steadily <strong>increases</strong> from 250.0 g to 251.8 g!</span>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-xs text-cyan-200'>\n                <strong>Definition of Condensation:</strong> The phase transition by which gaseous water vapour converts into liquid water upon contacting a cold surface.\n            </div>\n            <p class='text-xs text-slate-400 mt-2'>Because the internal water level mark remained perfectly constant, the extra 1.8 grams of mass arrived exclusively from invisible water vapour in the room air!</p>\n        ",
        "lecture_script": "To settle the debate over where the outside water comes from, Aavi and Thirav conduct Activity 8.4 using a digital balance. They take a glass tumbler half-filled with ice water and cover it with a small steel plate so no water can evaporate from the top. They mark the internal liquid level with a marker pen and place the tumbler on the digital scale. At zero minutes, the mass reads 250 grams. Every five minutes, they record the reading. To their excitement, the balance reading does not decrease; it steadily increases! After thirty minutes, the scale reads 251.8 grams. Furthermore, the internal water level line has not dropped at all. This conclusive test proves water is not leaking from inside. The extra mass comes from invisible water vapour in the ambient air condensing onto the cold exterior. Condensation is the process where water vapour turns back into liquid water when cooled.",
        "spoken_text": "To settle the debate over where the outside water comes from, Aavi and Thirav conduct Activity 8.4 using a digital balance. They take a glass tumbler half-filled with ice water and cover it with a small steel plate so no water can evaporate from the top. They mark the internal liquid level with a marker pen and place the tumbler on the digital scale. At zero minutes, the mass reads 250 grams. Every five minutes, they record the reading. To their excitement, the balance reading does not decrease; it steadily increases! After thirty minutes, the scale reads 251.8 grams. Furthermore, the internal water level line has not dropped at all. This conclusive test proves water is not leaking from inside. The extra mass comes from invisible water vapour in the ambient air condensing onto the cold exterior. Condensation is the process where water vapour turns back into liquid water when cooled.",
        "checkpoints": [
            {
                "question": "In Activity 8.4, why does the digital balance reading increase over 30 minutes for a covered iced tumbler?",
                "options": [
                    "The glass expands and generates more gravitational pull",
                    "Water vapour from surrounding ambient air condenses onto the cold exterior, adding measurable mass",
                    "Ice weighs significantly more after it melts inside",
                    "Dust in the room accumulates exclusively on the steel lid"
                ],
                "correct": 1,
                "explanation": "Airborne water vapour loses thermal energy upon touching the cold glass walls and transitions into liquid water droplets, adding its mass to the scale.",
                "study_insight": "A closed system gaining mass demonstrates mass accretion from ambient atmospheric moisture via condensation."
            },
            {
                "question": "What is the scientific term for the conversion of gaseous water vapour into liquid droplets upon touching a cool surface?",
                "options": [
                    "Evaporation",
                    "Condensation",
                    "Sublimation",
                    "Sedimentation"
                ],
                "correct": 1,
                "explanation": "Condensation is the exact reverse of evaporation; it is the physical transition from gas to liquid driven by thermal energy removal.",
                "study_insight": "Evaporation is liquid-to-gas phase transition; condensation is gas-to-liquid phase transition."
            }
        ]
    },
    {
        "id": 7,
        "title": "Air Harvest",
        "subtitle": "Atmospheric Moisture Content, Dew Formation, and Atmospheric Water Generators",
        "concept_html": "\n            <p class='mb-2'>The invisible water vapour present in Earth's atmosphere is known scientifically as <strong>humidity</strong>. High humidity makes air feel sticky and damp, while low humidity creates dry, arid conditions.</p>\n            <div class='grid grid-cols-2 gap-3 my-3 text-xs'>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800'>\n                    <div class='font-bold text-emerald-400 mb-1'>Natural Dew Drops</div>\n                    <p class='text-slate-300'>During cold nights, plant leaves cool rapidly by radiation. Water vapour in the dawn air condenses onto cold blades of grass and flower petals as sparkling <strong>dew drops</strong>.</p>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800'>\n                    <div class='font-bold text-sky-400 mb-1'>Atmospheric Water Generator (AWG)</div>\n                    <p class='text-slate-300'>Modern AWG machines pass humid air over chilled condensation coils. The condensed water is filtered and mineralized to provide clean, potable drinking water directly from air!</p>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200'>\n                <strong>Did You Know?</strong> The atmosphere holds thousands of cubic kilometers of pure fresh water at any moment. AWGs mimic the glass tumbler condensation effect on an industrial engineering scale!\n            </div>\n        ",
        "lecture_script": "The amount of invisible water vapour present in the air around us is called humidity. Weather reports in daily newspapers always mention the relative humidity percentage. When humidity is high, such as during the monsoon season, clothes take much longer to dry, and our sweat does not evaporate easily. On clear cold mornings, you often see glistening dew drops clinging to rose petals and grass blades. During the night, plants cool down, and when moist air touches their cold surfaces, water vapour condenses into liquid dew. Today, modern science uses this exact principle in Atmospheric Water Generators, or AWGs. These remarkable machines pull humid air across cooled condensation coils, condensing airborne moisture into pure, drinkable water. It is the cold tumbler experiment engineered to solve drinking water shortages in dry coastal regions.",
        "spoken_text": "The amount of invisible water vapour present in the air around us is called humidity. Weather reports in daily newspapers always mention the relative humidity percentage. When humidity is high, such as during the monsoon season, clothes take much longer to dry, and our sweat does not evaporate easily. On clear cold mornings, you often see glistening dew drops clinging to rose petals and grass blades. During the night, plants cool down, and when moist air touches their cold surfaces, water vapour condenses into liquid dew. Today, modern science uses this exact principle in Atmospheric Water Generators, or AWGs. These remarkable machines pull humid air across cooled condensation coils, condensing airborne moisture into pure, drinkable water. It is the cold tumbler experiment engineered to solve drinking water shortages in dry coastal regions.",
        "checkpoints": [
            {
                "question": "What is the meteorological term for the amount of water vapour present in the atmosphere?",
                "options": [
                    "Atmospheric pressure",
                    "Humidity",
                    "Precipitation index",
                    "Solar irradiance"
                ],
                "correct": 1,
                "explanation": "Humidity is the scientific measure of the concentration of water vapour present in ambient air.",
                "study_insight": "Higher humidity values indicate that ambient air is closer to saturation with water vapour."
            },
            {
                "question": "How do Atmospheric Water Generator (AWG) machines extract drinking water from the atmosphere?",
                "options": [
                    "By burning hydrogen and oxygen gases at high pressure",
                    "By cooling humid air over refrigeration coils to induce condensation of water vapour",
                    "By filtering ground dirt through activated charcoal filters",
                    "By using giant magnets to attract water ions"
                ],
                "correct": 1,
                "explanation": "AWGs chill incoming ambient humid air below its dew point, causing water vapour to condense into liquid droplets, which are collected and purified for drinking.",
                "study_insight": "AWG technology is a practical engineering application of phase-change condensation."
            }
        ]
    },
    {
        "id": 8,
        "title": "Three States",
        "subtitle": "Activity 8.5: Rigorous Matrix Comparison of Solid, Liquid, and Gaseous States",
        "concept_html": "\n            <p class='mb-2'>Water is one of the very few substances on Earth that comfortably coexists in <strong>three distinct physical states</strong> under natural ambient conditions (<strong>Activity 8.5</strong>).</p>\n            <div class='overflow-x-auto my-3'>\n                <table class='w-full text-xs text-left text-slate-300 border border-slate-800 rounded-xl overflow-hidden'>\n                    <thead class='bg-slate-900 text-indigo-400 font-bold'>\n                        <tr>\n                            <th class='p-2 border-b border-slate-800'>Physical Property</th>\n                            <th class='p-2 border-b border-slate-800 text-sky-400'>Solid (Ice)</th>\n                            <th class='p-2 border-b border-slate-800 text-indigo-400'>Liquid (Water)</th>\n                            <th class='p-2 border-b border-slate-800 text-amber-400'>Gas (Water Vapour)</th>\n                        </tr>\n                    </thead>\n                    <tbody class='divide-y divide-slate-800 bg-slate-950/40'>\n                        <tr>\n                            <td class='p-2 font-semibold text-white'>Geometric Shape</td>\n                            <td class='p-2'>Fixed, rigid shape; independent of container</td>\n                            <td class='p-2'>No fixed shape; takes container's geometry</td>\n                            <td class='p-2'>No fixed shape; fills entire enclosed volume</td>\n                        </tr>\n                        <tr>\n                            <td class='p-2 font-semibold text-white'>Ability to Flow</td>\n                            <td class='p-2'>Cannot flow under gravity</td>\n                            <td class='p-2'>Flows freely from higher to lower levels</td>\n                            <td class='p-2'>Flows and diffuses rapidly in all directions</td>\n                        </tr>\n                        <tr>\n                            <td class='p-2 font-semibold text-white'>Ability to Spread</td>\n                            <td class='p-2'>Does not spread; maintains perimeter</td>\n                            <td class='p-2'>Spreads on flat surface; constant volume</td>\n                            <td class='p-2'>Spreads infinitely into all available space</td>\n                        </tr>\n                        <tr>\n                            <td class='p-2 font-semibold text-white'>Definite Volume</td>\n                            <td class='p-2'>Definite, constant volume</td>\n                            <td class='p-2'>Definite, constant volume</td>\n                            <td class='p-2'>No definite volume; highly compressible</td>\n                        </tr>\n                    </tbody>\n                </table>\n            </div>\n            <p class='text-xs text-slate-400'>When liquid water is poured from a tumbler into a wide bowl, its shape conforms immediately to the bowl, yet its exact volume in millilitres remains identical.</p>\n        ",
        "lecture_script": "In Activity 8.5, we perform a systematic comparison of the three states of water. Let us observe ice, liquid water, and water vapour across three crucial physical properties: shape, ability to flow, and ability to spread. Solid ice retains its rigid shape regardless of the container it is placed in. It does not flow and does not spread across a table. Liquid water, on the other hand, has no fixed shape. If you pour one hundred millilitres of water from a tall cylindrical glass into a flat square tray, it instantly takes the shape of the tray. However, its volume remains strictly constant at one hundred millilitres. Liquid water flows downhill and spreads into a thin layer. Finally, gaseous water vapour has neither a fixed shape nor a fixed volume. It expands and spreads out to occupy the entirety of any available space in a room.",
        "spoken_text": "In Activity 8.5, we perform a systematic comparison of the three states of water. Let us observe ice, liquid water, and water vapour across three crucial physical properties: shape, ability to flow, and ability to spread. Solid ice retains its rigid shape regardless of the container it is placed in. It does not flow and does not spread across a table. Liquid water, on the other hand, has no fixed shape. If you pour one hundred millilitres of water from a tall cylindrical glass into a flat square tray, it instantly takes the shape of the tray. However, its volume remains strictly constant at one hundred millilitres. Liquid water flows downhill and spreads into a thin layer. Finally, gaseous water vapour has neither a fixed shape nor a fixed volume. It expands and spreads out to occupy the entirety of any available space in a room.",
        "checkpoints": [
            {
                "question": "When 200 mL of water is poured from a narrow bottle into a wide shallow pan, what happens to its shape and volume?",
                "options": [
                    "Both its shape and its volume change drastically",
                    "Its shape changes to match the pan, but its volume remains exactly 200 mL",
                    "Its shape stays unchanged while its volume doubles",
                    "Its volume contracts to 50 mL while its shape stays unchanged"
                ],
                "correct": 1,
                "explanation": "Liquids adopt the shape of whatever vessel holds them, but maintain an incompressible, definite volume under constant pressure.",
                "study_insight": "Liquids have an indefinite shape but a definite, constant volume."
            },
            {
                "question": "Which state of matter expands and spreads out to occupy the entire volume of any closed container?",
                "options": [
                    "Solid state (Ice)",
                    "Liquid state (Water)",
                    "Gaseous state (Water vapour)",
                    "Crystalline state (Quartz)"
                ],
                "correct": 2,
                "explanation": "Gaseous particles have high kinetic energy and negligible intermolecular bonds, allowing them to expand until they fill the container uniformly.",
                "study_insight": "Gases have neither a fixed shape nor a fixed volume, diffusing into all accessible volume."
            }
        ]
    },
    {
        "id": 9,
        "title": "Wax & Oil",
        "subtitle": "State Transformations Beyond Water: Candles, Oils, and Kitchen Aroma Diffusion",
        "concept_html": "\n            <p class='mb-2'>Water is not the only substance that transitions between solid, liquid, and gas. Many familiar materials in our homes display identical state changes upon heating or cooling:</p>\n            <div class='grid grid-cols-3 gap-2 my-3 text-xs'>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-amber-400 font-bold block mb-1'>Candle Wax</span>\n                    <span class='text-slate-300'>Solid wax melts into liquid near a flame; when liquid wax drips onto cold tables, it freezes back into a solid.</span>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-emerald-400 font-bold block mb-1'>Coconut Oil & Ghee</span>\n                    <span class='text-slate-300'>In cold winter months, liquid coconut oil and clarified butter (ghee) freeze into opaque, solid pastes at room temperature.</span>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-sky-400 font-bold block mb-1'>Food Aromas</span>\n                    <span class='text-slate-300'>Gaseous spices and aromatic molecules evaporate from hot food and diffuse across entire houses into our nostrils.</span>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-slate-300'>\n                <strong>Core Physical Principle:</strong> State changes are universal physical phenomena driven by thermal energy transfer, preserving the chemical identity of the underlying matter.\n            </div>\n        ",
        "lecture_script": "Water is our most common example, but state transitions occur in many everyday materials. Consider a burning candle made of wax. The flame's heat melts the solid wax into clear liquid wax near the wick. When this molten wax drips down the side onto the cooler candlestick, it quickly solidifies back into solid wax. Similarly, during brisk winter mornings, liquid coconut oil or desi ghee in your kitchen solidifies into a thick white paste without any chemical alteration. When heated gently in a pan, it liquefies immediately. Furthermore, have you ever noticed that you can smell delicious food cooking before you even enter the kitchen? The heat of cooking causes volatile flavour compounds to vaporize into gases. Because gas molecules spread rapidly in all directions through air, they diffuse through hallways and reach our olfactory receptors.",
        "spoken_text": "Water is our most common example, but state transitions occur in many everyday materials. Consider a burning candle made of wax. The flame's heat melts the solid wax into clear liquid wax near the wick. When this molten wax drips down the side onto the cooler candlestick, it quickly solidifies back into solid wax. Similarly, during brisk winter mornings, liquid coconut oil or desi ghee in your kitchen solidifies into a thick white paste without any chemical alteration. When heated gently in a pan, it liquefies immediately. Furthermore, have you ever noticed that you can smell delicious food cooking before you even enter the kitchen? The heat of cooking causes volatile flavour compounds to vaporize into gases. Because gas molecules spread rapidly in all directions through air, they diffuse through hallways and reach our olfactory receptors.",
        "checkpoints": [
            {
                "question": "Why does liquid coconut oil turn into a white solid during cold winter mornings?",
                "options": [
                    "It absorbs nitrogen from winter air",
                    "Its temperature drops below its freezing point, causing a physical phase change from liquid to solid",
                    "Bacteria in the bottle ferment the oil into curd",
                    "Light exposure causes the oil to undergo chemical polymerization"
                ],
                "correct": 1,
                "explanation": "Coconut oil has a relatively high freezing point (around 24 \u00b0C). When ambient winter temperature drops below this threshold, it solidifies.",
                "study_insight": "Freezing is the thermal phase change from liquid to solid that occurs when heat is removed below a substance's freezing threshold."
            },
            {
                "question": "How does the aroma of hot sizzling food reach a person sitting two rooms away?",
                "options": [
                    "Heat waves propel solid food particles along magnetic field lines",
                    "Volatile aroma molecules vaporize into gas and diffuse rapidly through the air",
                    "Sound vibrations carry the smell through ceiling fans",
                    "Air currents exclusively push liquid oil droplets along walls"
                ],
                "correct": 1,
                "explanation": "Thermal energy vaporizes aromatic compounds into gaseous molecules, which disperse rapidly through air via molecular diffusion and convection.",
                "study_insight": "Gas diffusion allows vaporized molecules to disperse freely and fill accessible ambient air."
            }
        ]
    },
    {
        "id": 10,
        "title": "Phase Cycle",
        "subtitle": "Activity 8.6: The Complete Thermodynamic Cycle of Melting, Freezing, Evaporation, and Condensation",
        "concept_html": "\n            <p class='mb-2'>The three states of matter form a reversible thermodynamic cycle governed strictly by the addition or removal of <strong>thermal energy</strong> (heat):</p>\n            <div class='p-4 rounded-xl bg-slate-900 border border-slate-800 my-3 text-xs space-y-3'>\n                <div class='grid grid-cols-2 gap-2 text-center'>\n                    <div class='p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30 text-rose-200'>\n                        <span class='font-bold block text-sm'>Heating (Heat Absorbed)</span>\n                        <span>Solid \u2192 Liquid (<strong>Melting</strong>)</span><br>\n                        <span>Liquid \u2192 Gas (<strong>Evaporation</strong>)</span>\n                    </div>\n                    <div class='p-2.5 rounded-lg bg-sky-950/40 border border-sky-500/30 text-sky-200'>\n                        <span class='font-bold block text-sm'>Cooling (Heat Released)</span>\n                        <span>Gas \u2192 Liquid (<strong>Condensation</strong>)</span><br>\n                        <span>Liquid \u2192 Solid (<strong>Freezing</strong>)</span>\n                    </div>\n                </div>\n                <div class='p-2.5 rounded-lg bg-slate-950/60 border border-slate-800 text-slate-300'>\n                    <strong>Activity 8.6 Schematic:</strong><br>\n                    \u2022 [A: Solid (Ice)] \u2500\u2500(1: Melts / Heat)\u2500\u2500\u25ba [B: Liquid (Water)] \u2500\u2500(2: Evaporates / Heat)\u2500\u2500\u25ba [C: Gas (Vapour)]<br>\n                    \u2022 [C: Gas (Vapour)] \u2500\u2500(4: Condenses / Cool)\u2500\u2500\u25ba [B: Liquid (Water)] \u2500\u2500(3: Freezes / Cool)\u2500\u2500\u25ba [A: Solid (Ice)]\n                </div>\n            </div>\n            <p class='text-xs text-slate-400'>Each transition is perfectly reversible. Matter is neither created nor destroyed during state changes; only the arrangement and kinetic motion of molecules change.</p>\n        ",
        "lecture_script": "Section 8.4 and Activity 8.6 summarize the fundamental pathways of state transitions. To convert solid ice into liquid water, we supply heat energy, a process called melting. To convert liquid water into gaseous water vapour, we continue supplying heat, a process called evaporation or vaporization. Conversely, if we take water vapour and cool it down by removing heat, it condenses back into liquid water. If we cool that liquid water further, down to zero degrees Celsius, it undergoes freezing and returns to solid ice. Notice that melting and freezing are exact thermodynamic opposites, just as evaporation and condensation are exact opposites. Heating increases molecular motion and pushes substances toward gaseous states, while cooling reduces molecular motion and pulls them toward solid states.",
        "spoken_text": "Section 8.4 and Activity 8.6 summarize the fundamental pathways of state transitions. To convert solid ice into liquid water, we supply heat energy, a process called melting. To convert liquid water into gaseous water vapour, we continue supplying heat, a process called evaporation or vaporization. Conversely, if we take water vapour and cool it down by removing heat, it condenses back into liquid water. If we cool that liquid water further, down to zero degrees Celsius, it undergoes freezing and returns to solid ice. Notice that melting and freezing are exact thermodynamic opposites, just as evaporation and condensation are exact opposites. Heating increases molecular motion and pushes substances toward gaseous states, while cooling reduces molecular motion and pulls them toward solid states.",
        "checkpoints": [
            {
                "question": "Which pair of phase transitions both require thermal energy (heat) to be supplied to the substance?",
                "options": [
                    "Melting and Condensation",
                    "Freezing and Condensation",
                    "Melting and Evaporation",
                    "Freezing and Evaporation"
                ],
                "correct": 2,
                "explanation": "Melting (solid to liquid) and Evaporation (liquid to gas) are endothermic processes requiring heat input to overcome intermolecular attractions.",
                "study_insight": "Melting and evaporation absorb heat; freezing and condensation release heat."
            },
            {
                "question": "What is the exact scientific term for the transition of liquid water into solid ice upon cooling?",
                "options": [
                    "Condensation",
                    "Freezing",
                    "Melting",
                    "Precipitation"
                ],
                "correct": 1,
                "explanation": "Freezing (also called solidification) is the phase transition from liquid to solid as thermal energy is extracted.",
                "study_insight": "Freezing point of pure water at sea level is exactly 0 degrees Celsius."
            }
        ]
    },
    {
        "id": 11,
        "title": "Plate Area",
        "subtitle": "Activity 8.7: Controlled Investigation into How Exposed Surface Area Controls Evaporation Rate",
        "concept_html": "\n            <p class='mb-2'>Why do we spread out wet clothes on a laundry line rather than leaving them balled up in a bucket? <strong>Activity 8.7</strong> systematically investigates the effect of <strong>exposed surface area</strong> on evaporation rate.</p>\n            <div class='grid grid-cols-2 gap-3 my-3 text-xs'>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-amber-400 font-bold block mb-1'>Small Bottle Cap</span>\n                    <span class='text-slate-300'>Water volume: 5 mL<br>Exposed Area: ~3 cm\u00b2<br>Time to Dry: <strong>~180 minutes</strong></span>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-cyan-400 font-bold block mb-1'>Broad Steel Plate</span>\n                    <span class='text-slate-300'>Water volume: 5 mL<br>Exposed Area: ~200 cm\u00b2<br>Time to Dry: <strong>~25 minutes</strong></span>\n                </div>\n            </div>\n            <div class='p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-xs space-y-1'>\n                <div class='font-bold text-indigo-400'>Scientific Controls in Activity 8.7:</div>\n                <p class='text-slate-300'>\u2022 <strong>Controlled Variables (Kept Same):</strong> Volume of water (5 mL), ambient temperature, room humidity, air movement.</p>\n                <p class='text-slate-300'>\u2022 <strong>Independent Variable (Changed):</strong> Exposed surface area in contact with air.</p>\n                <p class='text-slate-300'>\u2022 <strong>Dependent Variable (Measured):</strong> Time taken for complete evaporation.</p>\n            </div>\n            <p class='text-xs text-emerald-300 mt-2 font-semibold'>Direct Law: Greater exposed surface area provides more escape boundaries for surface molecules, drastically increasing evaporation rate!</p>\n        ",
        "lecture_script": "Section 8.5 introduces how we can make water evaporate faster or slower. In Activity 8.7, we test the effect of exposed surface area. Take two identical amounts of water, exactly five millilitres each. Pour one into a small, narrow bottle cap and pour the other into a wide, flat dinner plate. Place them side by side in the same room so that temperature, sunlight, and air movement remain identical. What did we change? The surface area exposed to air. What did we measure? The time taken for complete evaporation. The water spread out over the wide plate evaporates in about twenty-five minutes, while the water in the bottle cap takes over three hours! Evaporation is a surface phenomenon. When you increase the exposed surface area, far more water molecules sit at the boundary, ready to absorb energy and escape into the air. That is why we spread out clothes on a washing line.",
        "spoken_text": "Section 8.5 introduces how we can make water evaporate faster or slower. In Activity 8.7, we test the effect of exposed surface area. Take two identical amounts of water, exactly five millilitres each. Pour one into a small, narrow bottle cap and pour the other into a wide, flat dinner plate. Place them side by side in the same room so that temperature, sunlight, and air movement remain identical. What did we change? The surface area exposed to air. What did we measure? The time taken for complete evaporation. The water spread out over the wide plate evaporates in about twenty-five minutes, while the water in the bottle cap takes over three hours! Evaporation is a surface phenomenon. When you increase the exposed surface area, far more water molecules sit at the boundary, ready to absorb energy and escape into the air. That is why we spread out clothes on a washing line.",
        "checkpoints": [
            {
                "question": "Why does a saucer of hot tea cool down and evaporate faster than hot tea kept in a tall, narrow cup?",
                "options": [
                    "The saucer creates a magnetic field that expels steam",
                    "The larger exposed surface area allows more surface molecules to evaporate and release heat rapidly",
                    "The saucer material has a higher thermal insulation capacity",
                    "The liquid in the saucer gains chemical mass from table air"
                ],
                "correct": 1,
                "explanation": "A wider surface area increases the liquid-air interface, accelerating molecular evaporation and evaporative heat loss.",
                "study_insight": "Evaporation rate is directly proportional to the exposed surface area of the liquid."
            },
            {
                "question": "In a fair scientific experiment comparing evaporation from a bottle cap and a plate, which factor must be kept identical?",
                "options": [
                    "The exposed surface area of the containers",
                    "The initial volume of water and ambient environmental conditions",
                    "The diameter of the vessels",
                    "The color of the plates"
                ],
                "correct": 1,
                "explanation": "To isolate the effect of surface area, all other variables\u2014water volume, room temperature, wind speed, and humidity\u2014must be held constant.",
                "study_insight": "A controlled experiment changes only one independent variable while keeping all others constant."
            }
        ]
    },
    {
        "id": 12,
        "title": "Sun & Wind",
        "subtitle": "Activity 8.8: The Influence of Temperature, Wind Speed, and Atmospheric Humidity on Evaporation",
        "concept_html": "\n            <p class='mb-2'>Beyond surface area, three dominant environmental conditions govern how rapidly water molecules vaporize into the surrounding air (<strong>Activity 8.8</strong>):</p>\n            <div class='grid grid-cols-3 gap-2 my-3 text-xs'>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-amber-400 font-bold block mb-1'>1. Sunlight & Temp</span>\n                    <span class='text-slate-300'>Water in a bottle cap placed in direct sunlight evaporates twice as fast as an identical cap kept in the shade. Higher thermal energy energizes molecules to escape!</span>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-cyan-400 font-bold block mb-1'>2. Wind & Air Flow</span>\n                    <span class='text-slate-300'>Clothes dry significantly faster on a windy day. Moving air sweeps away saturated vapor layers above the fabric, making room for new vapor.</span>\n                </div>\n                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-center'>\n                    <span class='text-rose-400 font-bold block mb-1'>3. Humidity Level</span>\n                    <span class='text-slate-300'>On rainy monsoon days, air already carries high moisture. High humidity retards evaporation, causing clothes to stay damp for days.</span>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-slate-300'>\n                <strong>Evaporation Rate Formula Summary:</strong> Rate increases with higher Surface Area, higher Temperature, and higher Wind Speed; rate decreases with higher Humidity.\n            </div>\n        ",
        "lecture_script": "Activity 8.8 explores the other key factors controlling evaporation: temperature, wind, and humidity. Take two identical bottle caps with equal amounts of water. Place one cap in direct, radiant sunlight and the other inside the house in the shade. The cap under bright sunlight evaporates much faster because thermal energy increases the kinetic speed of water molecules, allowing them to overcome liquid surface tension and break away into vapour. Next, consider wind. On a windy day, or if you hang clothes under a running ceiling fan, the laundry dries much faster. Fast-moving air sweeps away the humid boundary layer hovering over the wet fabric, allowing dry air to take its place. Conversely, consider a humid, rainy day. Because the atmosphere is already saturated with water vapour, evaporation slows down to a crawl.",
        "spoken_text": "Activity 8.8 explores the other key factors controlling evaporation: temperature, wind, and humidity. Take two identical bottle caps with equal amounts of water. Place one cap in direct, radiant sunlight and the other inside the house in the shade. The cap under bright sunlight evaporates much faster because thermal energy increases the kinetic speed of water molecules, allowing them to overcome liquid surface tension and break away into vapour. Next, consider wind. On a windy day, or if you hang clothes under a running ceiling fan, the laundry dries much faster. Fast-moving air sweeps away the humid boundary layer hovering over the wet fabric, allowing dry air to take its place. Conversely, consider a humid, rainy day. Because the atmosphere is already saturated with water vapour, evaporation slows down to a crawl.",
        "checkpoints": [
            {
                "question": "Why do freshly washed clothes dry faster when hung beneath a rapidly spinning ceiling fan?",
                "options": [
                    "The fan cools the water until it freezes into crystals",
                    "Moving air rapidly sweeps away the moist air layer around the cloth, sustaining a steep evaporation gradient",
                    "The fan blows electrical charges onto the fabric",
                    "Air currents compress the liquid water into the center of the cloth"
                ],
                "correct": 1,
                "explanation": "Air currents disperse saturated moisture hovering directly above the fabric surface, maintaining a low local humidity and accelerating evaporation.",
                "study_insight": "Increased air velocity accelerates evaporation by removing the stagnant boundary layer of water vapour."
            },
            {
                "question": "How does high atmospheric humidity on a rainy day affect the rate of water evaporation?",
                "options": [
                    "It dramatically speeds up evaporation",
                    "It retards and slows down the rate of evaporation",
                    "It has zero effect on evaporation rate",
                    "It causes water to boil spontaneously at room temperature"
                ],
                "correct": 1,
                "explanation": "When ambient air is already loaded with water vapour (high humidity), the capacity of the air to absorb additional vapour is reduced, slowing evaporation.",
                "study_insight": "Evaporation rate is inversely related to the humidity of the surrounding air."
            }
        ]
    },
    {
        "id": 13,
        "title": "Clay Chill",
        "subtitle": "Section 8.6: The Thermodynamic Science of the Traditional Indian Matka and Latent Heat Extraction",
        "concept_html": "\n            <p class='mb-2'>When Aavi returns home from school on a sweltering May afternoon, she pours drinking water from a newly purchased clay <strong>matka</strong> (earthen pot). To her delight, the water is refreshingly cold!</p>\n            <p class='mb-2'>Why does water stored in a porous earthenware pot turn cold, whereas water in a polished stainless steel vessel remains warm?</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs my-2'>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-bold'>Porous Walls</span>\n                    <span class='text-slate-300'>Baked clay possesses thousands of microscopic, sub-millimetre capillary pores running through its structure. Water slowly seeps through to the outer wall.</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-bold'>Surface Evaporation</span>\n                    <span class='text-slate-300'>The thin film of seeped moisture on the exterior wall continuously evaporates into the warm outdoor air.</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold'>Cooling Effect</span>\n                    <span class='text-slate-300'>To evaporate, each escaping water molecule absorbs <strong>latent heat of vaporization</strong> directly from the pot and remaining water inside, steadily chilling it!</span>\n                </div>\n            </div>\n            <p class='text-xs text-slate-400'>This same evaporative cooling principle explains why we feel cool when rubbing alcohol sanitizer on our hands or sitting under a breeze when sweating.</p>\n        ",
        "lecture_script": "Section 8.6 uncovers the remarkable cooling effect of evaporation. Aavi noticed that drinking water stored in a clay matka is refreshingly cool, whereas water in a stainless steel pot stays warm. Baked clay has millions of tiny, microscopic pores. Water from inside the pot slowly seeps through these microscopic channels to the exterior surface. Once on the outside, this thin layer of water evaporates into the warm air. To transform from liquid to vapour, water molecules must absorb thermal energy. Where do they get this heat? They absorb it directly from the pot and the water remaining inside! As heat is continuously extracted to fuel evaporation, the temperature of the water inside drops noticeably. This is why evaporation always produces a cooling effect. The same principle cools our bodies when sweat evaporates, or when you sprinkle cold water across a scorching rooftop in summer.",
        "spoken_text": "Section 8.6 uncovers the remarkable cooling effect of evaporation. Aavi noticed that drinking water stored in a clay matka is refreshingly cool, whereas water in a stainless steel pot stays warm. Baked clay has millions of tiny, microscopic pores. Water from inside the pot slowly seeps through these microscopic channels to the exterior surface. Once on the outside, this thin layer of water evaporates into the warm air. To transform from liquid to vapour, water molecules must absorb thermal energy. Where do they get this heat? They absorb it directly from the pot and the water remaining inside! As heat is continuously extracted to fuel evaporation, the temperature of the water inside drops noticeably. This is why evaporation always produces a cooling effect. The same principle cools our bodies when sweat evaporates, or when you sprinkle cold water across a scorching rooftop in summer.",
        "checkpoints": [
            {
                "question": "What is the primary mechanism that causes water in an earthen matka to stay cool during hot summer days?",
                "options": [
                    "Clay creates a chemical endothermic reaction with atmospheric nitrogen",
                    "Water continuously seeps through microscopic clay pores and evaporates from the outer surface, extracting heat from the water inside",
                    "The reddish color of terracotta reflects 100% of cosmic rays",
                    "The matka attracts cold air currents into its neck"
                ],
                "correct": 1,
                "explanation": "Evaporation requires latent heat of vaporization, which the evaporating surface water extracts from the pot and the remaining internal water, cooling it.",
                "study_insight": "Evaporative cooling extracts thermal energy from the remaining liquid and container."
            },
            {
                "question": "Why does rubbing alcohol hand sanitizer onto your palms create an intense sensation of coldness?",
                "options": [
                    "Sanitizer freezes the epidermal nerve endings permanently",
                    "Alcohol evaporates extremely rapidly at room temperature, extracting thermal energy quickly from your skin",
                    "Sanitizer has a temperature of minus 50 degrees Celsius inside the bottle",
                    "Chemical friction generates negative calories"
                ],
                "correct": 1,
                "explanation": "Alcohol has a low boiling point and high volatility; it evaporates rapidly from skin, extracting heat and triggering thermal receptors that detect cooling.",
                "study_insight": "Highly volatile liquids evaporate rapidly, causing a sharp drop in surface temperature."
            }
        ]
    },
    {
        "id": 14,
        "title": "Pot Cooler",
        "subtitle": "Activity 8.9: Zero-Electricity Desert Refrigeration: The Zeer Pot and Heritage Surahi",
        "concept_html": "\n            <p class='mb-2'>Can fruits and fresh vegetables be refrigerated in remote off-grid rural communities without electrical power? <strong>Activity 8.9</strong> demonstrates how to construct a <strong>pot-in-pot evaporative cooler</strong> (also known as a Zeer cooler):</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs mb-3'>\n                <div class='flex items-center gap-2'>\n                    <span class='w-5 h-5 rounded-full bg-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center shrink-0'>1</span>\n                    <span class='text-slate-300'>Place a smaller clay pot inside a larger clay pot, leaving a 3-5 cm gap between their walls.</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='w-5 h-5 rounded-full bg-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center shrink-0'>2</span>\n                    <span class='text-slate-300'>Fill the bottom and gap completely with clean sand, and saturate the sand with water daily.</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='w-5 h-5 rounded-full bg-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center shrink-0'>3</span>\n                    <span class='text-slate-300'>Store fresh tomatoes, leafy greens, or milk in the inner pot and cover with a damp jute sack.</span>\n                </div>\n            </div>\n            <div class='grid grid-cols-2 gap-2 text-xs'>\n                <div class='p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-emerald-200'>\n                    <strong>Food Preservation:</strong> Continuous evaporation from the outer pot drops inner temperature by 5 \u00b0C to 12 \u00b0C below ambient air, extending vegetable shelf life from 2 days to over 20 days!\n                </div>\n                <div class='p-2.5 rounded-xl bg-amber-950/40 border border-amber-500/30 text-amber-200'>\n                    <strong>Heritage Surahi:</strong> A slender, long-necked traditional Indian clay vessel engineered to maximize evaporative cooling of summer drinking water.\n                </div>\n            </div>\n        ",
        "lecture_script": "Activity 8.9 demonstrates a simple, brilliant invention: the electricity-free pot-in-pot evaporative cooler, often called a Zeer refrigerator. Take a large clay pot and place a layer of sand in the bottom. Center a smaller clay pot inside it and fill the gap between the two walls with more sand. Pour water into the sand until it is thoroughly soaked, then cover the inner pot with a damp jute cloth or clay lid. As water in the wet sand seeps through the porous outer pot and evaporates into the dry surrounding air, it pulls heat away from the inner compartment. In dry desert regions, this simple device drops the temperature inside by up to twelve degrees Celsius! Fresh vegetables, fruits, and milk that would spoil in two days can stay fresh for weeks. We also see this heritage engineering in the Surahi, an elegant long-necked clay jug used across India to keep water chilled during hot summer months.",
        "spoken_text": "Activity 8.9 demonstrates a simple, brilliant invention: the electricity-free pot-in-pot evaporative cooler, often called a Zeer refrigerator. Take a large clay pot and place a layer of sand in the bottom. Center a smaller clay pot inside it and fill the gap between the two walls with more sand. Pour water into the sand until it is thoroughly soaked, then cover the inner pot with a damp jute cloth or clay lid. As water in the wet sand seeps through the porous outer pot and evaporates into the dry surrounding air, it pulls heat away from the inner compartment. In dry desert regions, this simple device drops the temperature inside by up to twelve degrees Celsius! Fresh vegetables, fruits, and milk that would spoil in two days can stay fresh for weeks. We also see this heritage engineering in the Surahi, an elegant long-necked clay jug used across India to keep water chilled during hot summer months.",
        "checkpoints": [
            {
                "question": "What role does the wet sand play in the pot-in-pot evaporative refrigerator (Activity 8.9)?",
                "options": [
                    "It acts as an electrical conductor powering a miniature fan",
                    "It serves as a water reservoir that continuously feeds moisture to the porous outer pot for steady evaporation",
                    "It reacts chemically with tomatoes to prevent bacterial growth",
                    "It absorbs cosmic radiation from sunlight"
                ],
                "correct": 1,
                "explanation": "Wet sand holds a steady supply of moisture that migrates through the porous earthenware walls, sustaining continuous evaporative cooling.",
                "study_insight": "Wet sand acts as a capillary moisture buffer maintaining an uninterrupted evaporative gradient."
            },
            {
                "question": "In which climate is a pot-in-pot evaporative cooler most effective at lowering internal temperatures?",
                "options": [
                    "A hot, arid (dry) desert climate with low relative humidity",
                    "A cool, rainy tropical climate with 100% relative humidity",
                    "An underwater submarine chamber",
                    "A frozen tundra at minus 20 degrees Celsius"
                ],
                "correct": 0,
                "explanation": "Evaporative cooling works best in hot, dry environments with low humidity, where evaporation occurs rapidly, extracting maximum latent heat.",
                "study_insight": "Evaporative cooling efficiency is maximized in hot, dry climates where ambient humidity is low."
            }
        ]
    },
    {
        "id": 15,
        "title": "Cloud Seeds",
        "subtitle": "Section 8.7 & Activity 8.10: Why Water Vapour Rises, Altitude Chilling, and Cloud-in-a-Bottle",
        "concept_html": "\n            <p class='mb-2'>Water evaporates from oceans and lakes every second. How does this evaporated vapour travel kilometres into the sky and transform into rain clouds? (<strong>Section 8.7</strong>)</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs mb-3'>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-bold'>1. Vapour Rises</span>\n                    <span class='text-slate-300'>Water vapour has a lower molecular mass (18 g/mol) than dry air (~29 g/mol). Like a helium balloon, warm humid air is less dense and naturally ascends high into the atmosphere.</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-bold'>2. Altitude Cooling</span>\n                    <span class='text-slate-300'>As air rises higher above Earth's surface, atmospheric pressure drops and air expands, cooling steadily (about 6.5 \u00b0C drop per kilometre of altitude).</span>\n                </div>\n                <div class='flex items-start gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-bold'>3. Nucleation Seeds</span>\n                    <span class='text-slate-300'>When cooled sufficiently, water vapour condenses around microscopic airborne dust and smoke particles (<strong>cloud condensation nuclei</strong>), creating visible billowing clouds!</span>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-slate-300'>\n                <strong>Activity 8.10 (Cloud in a Bottle):</strong> Squeezing a plastic bottle containing water and a trace of burnt newspaper smoke demonstrates that clouds form instantaneously when air decompresses and cools around smoke particles.\n            </div>\n        ",
        "lecture_script": "Section 8.7 explains how clouds form and give us rain. Why does air containing water vapour ascend into the upper atmosphere? Just like a gas balloon rises because it contains a lighter gas, water vapour is lighter and less dense than the surrounding dry air. As warm, moist air ascends higher above Earth's surface, it enters regions of lower atmospheric pressure and begins to expand. Expanding air cools down dramatically. At high altitudes, the air becomes so cold that water vapour can no longer remain a gas. But to condense into droplets, it requires tiny airborne dust or smoke particles known as condensation nuclei. In Activity 8.10, we demonstrate this inside a plastic bottle. When you add a tiny puff of smoke from a burnt piece of paper into a bottle with water, and squeeze and release it, a visible fog cloud appears immediately! Millions of these microscopic droplets floating together in the sky form clouds.",
        "spoken_text": "Section 8.7 explains how clouds form and give us rain. Why does air containing water vapour ascend into the upper atmosphere? Just like a gas balloon rises because it contains a lighter gas, water vapour is lighter and less dense than the surrounding dry air. As warm, moist air ascends higher above Earth's surface, it enters regions of lower atmospheric pressure and begins to expand. Expanding air cools down dramatically. At high altitudes, the air becomes so cold that water vapour can no longer remain a gas. But to condense into droplets, it requires tiny airborne dust or smoke particles known as condensation nuclei. In Activity 8.10, we demonstrate this inside a plastic bottle. When you add a tiny puff of smoke from a burnt piece of paper into a bottle with water, and squeeze and release it, a visible fog cloud appears immediately! Millions of these microscopic droplets floating together in the sky form clouds.",
        "checkpoints": [
            {
                "question": "Why does warm air containing water vapour rise upward into the atmosphere?",
                "options": [
                    "Water vapour is heavier than atmospheric nitrogen and sinks downward",
                    "Water vapour is lighter and less dense than surrounding dry air, causing humid air parcels to rise buoyantly",
                    "Earth's magnetic poles pull water molecules upward toward space",
                    "Sunlight repels liquid droplets into the stratosphere"
                ],
                "correct": 1,
                "explanation": "Water vapour has a lower molecular mass than oxygen and nitrogen, making warm moist air less dense and buoyant.",
                "study_insight": "Lighter, warm humid air rises through cooler, denser ambient air via buoyant convection."
            },
            {
                "question": "In Activity 8.10 (Cloud in a Bottle), what critical role do the smoke particles from the burnt paper play?",
                "options": [
                    "They provide heat that keeps the water boiling inside the bottle",
                    "They act as microscopic condensation nuclei around which water vapour condenses to form visible cloud droplets",
                    "They dye the water white so it looks like cotton",
                    "They absorb oxygen so only pure nitrogen remains"
                ],
                "correct": 1,
                "explanation": "In nature and in the bottle, water vapour requires solid microscopic surfaces (dust, pollen, or smoke nuclei) to condense into liquid droplet aerosols.",
                "study_insight": "Cloud formation requires both cool temperatures below the dew point and condensation nuclei."
            }
        ]
    },
    {
        "id": 16,
        "title": "Water Cycle",
        "subtitle": "Activity 8.11: The Global Hydrological Engine, Precipitation, and Freshwater Stewardship",
        "concept_html": "\n            <p class='mb-2'>The global circulation of water between Earth's surface and the atmosphere is a continuous, closed thermodynamic engine known as the <strong>Water Cycle</strong> (<strong>Activity 8.11</strong>):</p>\n            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-2 mb-3'>\n                <div class='flex items-center gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-bold'>1. Evaporation & Transpiration</span>\n                    <span class='text-slate-300'>Solar radiation heats oceans, lakes, and rivers, vaporizing water. Plants release water vapour through leaf stomata (transpiration).</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-bold'>2. Condensation</span>\n                    <span class='text-slate-300'>Rising vapour cools at high altitudes and condenses around airborne dust to form clouds and fog.</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-bold'>3. Precipitation</span>\n                    <span class='text-slate-300'>Droplets coalesce and grow heavy. Gravity pulls them down as rain, hail, sleet, or snow.</span>\n                </div>\n                <div class='flex items-center gap-2'>\n                    <span class='px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold'>4. Collection & Infiltration</span>\n                    <span class='text-slate-300'>Rainwater feeds rivers, lakes, and recharges underground groundwater tables, eventually returning to the oceans.</span>\n                </div>\n            </div>\n            <div class='p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-200'>\n                <strong>Water Responsibility:</strong> Over 97% of Earth's water is saline ocean water. Usable fresh water makes up less than 1% of the planetary total. Water is our collective responsibility before it is our right!\n            </div>\n        ",
        "lecture_script": "Activity 8.11 brings our journey full circle with the global water cycle. Water from oceans, rivers, and lakes evaporates into the atmosphere under the sun's warmth. Living plants also contribute through transpiration. As this vast mass of water vapour ascends, it cools and condenses into billows of clouds. When cloud droplets merge and become too heavy to remain suspended in the air, gravity pulls them down to Earth as precipitation, whether as life-giving rain, hail, or snow. Rainwater flows across landscapes into streams, rivers, and deep underground aquifers, ultimately flowing back into the oceans to begin the cycle anew. Remember, although Earth looks like a blue planet, more than ninety-seven percent of its water is salty ocean water. Fresh water fit for human, plant, and animal use represents only a tiny sliver. As citizens, water is our responsibility before it is our right. We must prevent water pollution and conserve every drop.",
        "spoken_text": "Activity 8.11 brings our journey full circle with the global water cycle. Water from oceans, rivers, and lakes evaporates into the atmosphere under the sun's warmth. Living plants also contribute through transpiration. As this vast mass of water vapour ascends, it cools and condenses into billows of clouds. When cloud droplets merge and become too heavy to remain suspended in the air, gravity pulls them down to Earth as precipitation, whether as life-giving rain, hail, or snow. Rainwater flows across landscapes into streams, rivers, and deep underground aquifers, ultimately flowing back into the oceans to begin the cycle anew. Remember, although Earth looks like a blue planet, more than ninety-seven percent of its water is salty ocean water. Fresh water fit for human, plant, and animal use represents only a tiny sliver. As citizens, water is our responsibility before it is our right. We must prevent water pollution and conserve every drop.",
        "checkpoints": [
            {
                "question": "What is the primary driving energy source that powers the entire global water cycle?",
                "options": [
                    "Earth's molten iron core",
                    "Solar thermal radiation from the Sun",
                    "Gravitational pull from the Moon",
                    "Wind turbine electrical generators"
                ],
                "correct": 1,
                "explanation": "Solar energy provides the heat that evaporates water from ocean and terrestrial surfaces and drives atmospheric circulation.",
                "study_insight": "The Sun's radiation is the primary energy engine of the global hydrological cycle."
            },
            {
                "question": "Approximately what percentage of all water on planet Earth is fresh and directly fit for human consumption and agriculture?",
                "options": [
                    "Nearly 50%",
                    "About 25%",
                    "Less than 1%",
                    "Exactly 97%"
                ],
                "correct": 2,
                "explanation": "Over 97% of Earth's water is saline ocean water, and most freshwater is locked in polar ice sheets, leaving less than 1% available as accessible liquid fresh water.",
                "study_insight": "Accessible fresh water is extremely scarce, highlighting the urgency of conservation."
            }
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "slide": 17,
        "challenge_set": 1,
        "question": "Which of the following best describes the process of condensation?",
        "options": [
            "Conversion of liquid water into solid ice upon cooling",
            "Conversion of gaseous water vapour into its liquid state",
            "Disappearance of liquid water from an open plate into air",
            "The flow of groundwater into ocean trenches"
        ],
        "correct": 1,
        "explanation": "Condensation is specifically defined in Section 8.2 as the physical phase transition of water vapour (gas) into liquid water upon cooling.",
        "solution_html": "<p><strong>Definition Review:</strong> Condensation is the exact reverse of evaporation. When airborne water vapour loses thermal energy upon touching a cold surface or entering cold altitudes, it transforms from a gas into liquid water droplets.</p>"
    },
    {
        "id": 2,
        "slide": 17,
        "challenge_set": 1,
        "question": "Why are ice and liquid water classified as the same chemical substance despite having different physical appearances?",
        "options": [
            "They have identical colors when viewed under a microscope",
            "Both consist of identical water molecules (two hydrogen atoms bonded to one oxygen atom) differing only in thermal kinetic state",
            "Ice is simply frozen nitrogen while water is hydrogen",
            "They can only exist inside refrigerators"
        ],
        "correct": 1,
        "explanation": "Phase changes are physical transformations that alter intermolecular spacing and thermal kinetic motion, leaving the chemical structure of H2O unchanged.",
        "solution_html": "<p><strong>Chemical vs Physical Change:</strong> Ice and liquid water share the exact same chemical formula (H2O). The phase transition between solid and liquid is purely physical and completely reversible.</p>"
    },
    {
        "id": 3,
        "slide": 17,
        "challenge_set": 1,
        "question": "What happens to the shape and volume of an ice cube when it is transferred from a round glass bowl to a rectangular steel box?",
        "options": [
            "It immediately adopts a rectangular shape and doubles its volume",
            "Both its shape and its volume remain completely unchanged",
            "Its volume decreases by 50% while its shape changes",
            "It turns instantly into gaseous steam"
        ],
        "correct": 1,
        "explanation": "Solids possess a rigid, fixed crystalline lattice that maintains both a definite geometric shape and a definite volume independent of the container.",
        "solution_html": "<p><strong>Solid Properties:</strong> As tested in Activity 8.5, ice retains its rigid shape and volume regardless of container geometry.</p>"
    },
    {
        "id": 4,
        "slide": 17,
        "challenge_set": 1,
        "question": "Which ancient Tamil literary text opens Chapter 8 with the verse on the ocean drying if rain fails?",
        "options": [
            "Silappadikaram",
            "Thirukkural",
            "Manimekalai",
            "Tolkappiyam"
        ],
        "correct": 1,
        "explanation": "The chapter opens with a celebrated couplet from the Thirukkural: 'If it does not rain well, even the mighty ocean will be drained.'",
        "solution_html": "<p><strong>Literary Context:</strong> The Thirukkural emphasizes the irreplaceable value of rainfall in maintaining life and even feeding the vast planetary oceans.</p>"
    },
    {
        "id": 5,
        "slide": 17,
        "challenge_set": 1,
        "question": "What is the gaseous state of water called?",
        "options": [
            "Liquid nitrogen",
            "Water vapour",
            "Carbon dioxide",
            "Methane"
        ],
        "correct": 1,
        "explanation": "Water in its gaseous phase is termed water vapour.",
        "solution_html": "<p><strong>Key Term:</strong> Water vapour is the invisible gas form of water present throughout Earth's atmosphere.</p>"
    },
    {
        "id": 6,
        "slide": 17,
        "challenge_set": 1,
        "question": "When water on a clean plate disappears at room temperature, what state does it transition into?",
        "options": [
            "It decomposes into solid minerals on the plate",
            "It converts into gaseous water vapour that mixes invisibly with room air",
            "It transforms into solid ice cubes",
            "It seeps through solid stainless steel"
        ],
        "correct": 1,
        "explanation": "At room temperature, water molecules at the exposed surface absorb thermal energy and evaporate into gaseous water vapour.",
        "solution_html": "<p><strong>Activity 8.2 Inference:</strong> Water on an impermeable plate evaporates directly into the gaseous state.</p>"
    },
    {
        "id": 7,
        "slide": 17,
        "challenge_set": 1,
        "question": "Why is true water vapour invisible, whereas steam from a kettle appears as a visible white mist?",
        "options": [
            "Steam is a toxic poison while vapour is clean",
            "Water vapour consists of isolated gas molecules, whereas steam contains tiny suspended liquid water droplets that scatter light",
            "Water vapour absorbs 100% of visible light",
            "Steam is composed of glowing carbon particles"
        ],
        "correct": 1,
        "explanation": "Molecules of water vapour are too small to interact with light waves, while the micro-droplets in steam scatter light, rendering it visible.",
        "solution_html": "<p><strong>Optics of Steam:</strong> The white mist seen above hot pans is an aerosol of condensed liquid micro-droplets, not gaseous water vapour.</p>"
    },
    {
        "id": 8,
        "slide": 17,
        "challenge_set": 1,
        "question": "Which of the following substances exists as a solid at cold winter room temperatures and liquefies upon gentle heating?",
        "options": [
            "Oxygen gas",
            "Desi ghee / coconut oil",
            "Nitrogen gas",
            "Distilled water at 50 degrees Celsius"
        ],
        "correct": 1,
        "explanation": "Coconut oil and ghee solidify into opaque pastes during winter and liquefy when heated, illustrating everyday reversible phase transitions.",
        "solution_html": "<p><strong>Everyday Solids & Liquids:</strong> Fats like coconut oil and ghee have melting points near 24 \u00b0C, making their phase changes observable across seasons.</p>"
    },
    {
        "id": 9,
        "slide": 17,
        "challenge_set": 1,
        "question": "What is the process called when solid ice absorbs heat and converts into liquid water?",
        "options": [
            "Freezing",
            "Melting",
            "Condensation",
            "Deposition"
        ],
        "correct": 1,
        "explanation": "The transition from solid to liquid upon the addition of thermal energy is called melting.",
        "solution_html": "<p><strong>Phase Definition:</strong> Melting occurs at 0 \u00b0C for pure water at standard atmospheric pressure.</p>"
    },
    {
        "id": 10,
        "slide": 17,
        "challenge_set": 1,
        "question": "Which state of water exhibits the ability to flow and take the shape of its vessel while maintaining a constant volume?",
        "options": [
            "Solid state (Ice)",
            "Liquid state (Water)",
            "Gaseous state (Water vapour)",
            "Plasma state"
        ],
        "correct": 1,
        "explanation": "Liquids are fluids that deform to match container boundaries while resisting compression, maintaining a constant volume.",
        "solution_html": "<p><strong>Liquid Characteristics:</strong> Water has an indefinite shape (conforms to container) but a definite volume.</p>"
    },
    {
        "id": 11,
        "slide": 18,
        "challenge_set": 2,
        "question": "In Activity 8.4, what happened to the reading on the digital weighing balance when a covered glass of ice water was weighed over 30 minutes?",
        "options": [
            "The mass decreased continuously as water leaked out",
            "The mass remained precisely at 0.0 grams",
            "The mass steadily increased as airborne water vapour condensed on the cold outside surface",
            "The scale fluctuated randomly due to magnetic interference"
        ],
        "correct": 2,
        "explanation": "Moisture from the room air deposited onto the cold outer tumbler walls, adding measurable mass to the balance.",
        "solution_html": "<p><strong>Quantitative Proof:</strong> The mass increased (e.g. from 250.0 g to 251.8 g), proving that outside water comes from the air, not from inside the glass.</p>"
    },
    {
        "id": 12,
        "slide": 18,
        "challenge_set": 2,
        "question": "During Activity 8.4, why was a permanent marker line drawn at the internal water level of the iced tumbler?",
        "options": [
            "To decorate the glass for aesthetic purposes",
            "To verify conclusively that the internal water level did not drop, proving water was not seeping through the glass",
            "To measure the expansion rate of glass",
            "To absorb solar radiation"
        ],
        "correct": 1,
        "explanation": "The unchanged marker level proved that no water leaked out from inside the tumbler.",
        "solution_html": "<p><strong>Experimental Verification:</strong> Constant internal level + increasing total mass = external condensation from ambient air.</p>"
    },
    {
        "id": 13,
        "slide": 18,
        "challenge_set": 2,
        "question": "What is the scientific term for the amount of water vapour present in ambient air?",
        "options": [
            "Precipitation",
            "Humidity",
            "Barometric index",
            "Viscosity"
        ],
        "correct": 1,
        "explanation": "Humidity represents the concentration of water vapour in air.",
        "solution_html": "<p><strong>Meteorological Definition:</strong> High humidity means air is carrying abundant water vapour; low humidity corresponds to dry, parched air.</p>"
    },
    {
        "id": 14,
        "slide": 18,
        "challenge_set": 2,
        "question": "Why do glistening dew drops form on plant leaves and grass blades during calm, cold mornings?",
        "options": [
            "Plants excrete excess water from internal veins during nighttime",
            "Water vapour in the air touches the cold surfaces of leaves chilled by night radiation and condenses into liquid drops",
            "Rain falls exclusively between 4 AM and 5 AM",
            "Dew drops are dropped by migratory birds"
        ],
        "correct": 1,
        "explanation": "Radiative cooling lowers leaf temperature below the ambient dew point, causing water vapour in air to condense on them.",
        "solution_html": "<p><strong>Natural Condensation:</strong> Dew formation is atmospheric condensation occurring on ground-level objects that have cooled overnight.</p>"
    },
    {
        "id": 15,
        "slide": 18,
        "challenge_set": 2,
        "question": "How does an Atmospheric Water Generator (AWG) machine harvest drinkable water in coastal regions?",
        "options": [
            "It extracts hydrogen from seawater by nuclear fission",
            "It cools humid air over refrigeration coils, condensing airborne moisture into pure liquid water",
            "It scoops water from passing clouds using drones",
            "It burns diesel fuel to create steam"
        ],
        "correct": 1,
        "explanation": "AWGs cool humid air below its dew point, condensing vapour into liquid water, which is filtered for drinking.",
        "solution_html": "<p><strong>Modern Technology:</strong> AWGs apply the exact same physical principle seen on the cold glass tumbler on an industrial engineering scale.</p>"
    },
    {
        "id": 16,
        "slide": 18,
        "challenge_set": 2,
        "question": "Which of the following processes represents evaporation taking place at normal room temperature?",
        "options": [
            "Water freezing into ice cubes inside a domestic freezer at -18 \u00b0C",
            "Drying of a wet tiled bathroom floor after cleaning",
            "Melting of butter in a hot frying pan over a gas burner",
            "Formation of frost on mountain peaks during a blizzard"
        ],
        "correct": 1,
        "explanation": "A wet floor dries because surface water molecules absorb ambient heat and evaporate at room temperature.",
        "solution_html": "<p><strong>Room Temperature Evaporation:</strong> Evaporation occurs at all temperatures between 0 \u00b0C and 100 \u00b0C, not just at the boiling point.</p>"
    },
    {
        "id": 17,
        "slide": 18,
        "challenge_set": 2,
        "question": "If you leave a glass tumbler containing water at room temperature on a table, will droplets form on its outer wall?",
        "options": [
            "Yes, twice as many droplets as an ice glass",
            "No, because the glass surface is not colder than the surrounding air to trigger condensation",
            "Yes, but only if the lights are turned off",
            "Yes, because glass is naturally permeable to water"
        ],
        "correct": 1,
        "explanation": "Condensation requires the contact surface to be colder than the surrounding air's dew point; a room-temperature tumbler will stay dry.",
        "solution_html": "<p><strong>Thermal Condition:</strong> Condensation requires heat extraction. Without a temperature difference, water vapour does not condense on the surface.</p>"
    },
    {
        "id": 18,
        "slide": 18,
        "challenge_set": 2,
        "question": "In Activity 8.6, which phase transition converts a gas directly into a liquid upon cooling?",
        "options": [
            "Melting",
            "Freezing",
            "Condensation",
            "Evaporation"
        ],
        "correct": 2,
        "explanation": "Gas to liquid is condensation.",
        "solution_html": "<p><strong>Phase Transition Pathways:</strong> Gas \u2192 Liquid = Condensation; Liquid \u2192 Gas = Evaporation; Liquid \u2192 Solid = Freezing; Solid \u2192 Liquid = Melting.</p>"
    },
    {
        "id": 19,
        "slide": 18,
        "challenge_set": 2,
        "question": "Why does a lid placed over a pot of steaming soup collect water droplets on its underside?",
        "options": [
            "Soup splatters upward in explosive microscopic geysers",
            "Hot water vapour rising from the soup cools upon contacting the cooler lid and condenses into liquid drops",
            "Metal lids produce water through chemical reaction with salt",
            "Air outside leaks through the lid metal"
        ],
        "correct": 1,
        "explanation": "Hot vapour rising from hot food strikes the cooler underside of the pot lid, releasing heat and condensing into droplets.",
        "solution_html": "<p><strong>Culinary Condensation:</strong> Steam rising from hot liquids condenses on any cooler surface above it.</p>"
    },
    {
        "id": 20,
        "slide": 18,
        "challenge_set": 2,
        "question": "What is the reverse physical process of freezing?",
        "options": [
            "Condensation",
            "Melting",
            "Evaporation",
            "Precipitation"
        ],
        "correct": 1,
        "explanation": "Freezing turns liquid into solid; melting turns solid back into liquid.",
        "solution_html": "<p><strong>Reversibility:</strong> Freezing and melting occur at the same transition temperature (0 \u00b0C for pure water) and are exact opposites.</p>"
    },
    {
        "id": 21,
        "slide": 19,
        "challenge_set": 3,
        "question": "In Activity 8.7, why did 5 mL of water in a broad steel plate evaporate much faster than 5 mL of water in a narrow bottle cap?",
        "options": [
            "Steel attracts water molecules with magnetic force",
            "The plate offered a much larger surface area exposed to ambient air",
            "The bottle cap generated a protective gravitational shield",
            "Water in the bottle cap was frozen solid"
        ],
        "correct": 1,
        "explanation": "Evaporation is a surface phenomenon; a larger exposed surface allows more molecules to escape into the atmosphere simultaneously.",
        "solution_html": "<p><strong>Surface Area Principle:</strong> Evaporation rate is directly proportional to exposed surface area.</p>"
    },
    {
        "id": 22,
        "slide": 19,
        "challenge_set": 3,
        "question": "How does an increase in wind speed affect the drying time of laundry hung outside?",
        "options": [
            "It increases drying time by making clothes wetter",
            "It decreases drying time because moving air rapidly carries away saturated vapour layers above the cloth",
            "It has zero impact on drying speed",
            "It turns the water on the cloth into oil"
        ],
        "correct": 1,
        "explanation": "Wind removes humid air layers from the fabric boundary, maintaining a steep concentration gradient that speeds evaporation.",
        "solution_html": "<p><strong>Wind Effect:</strong> Strong air movement sweeps away local humidity, accelerating evaporation.</p>"
    },
    {
        "id": 23,
        "slide": 19,
        "challenge_set": 3,
        "question": "Why do wet clothes take a frustratingly long time to dry on a rainy monsoon day?",
        "options": [
            "Atmospheric pressure drops to absolute zero",
            "The surrounding air already carries high humidity, greatly reducing its ability to absorb additional water vapour",
            "Sunlight is completely destroyed on rainy days",
            "Rainwater turns into solid ice on clothes lines"
        ],
        "correct": 1,
        "explanation": "When humidity is near 100%, ambient air is near saturation, causing evaporation to slow drastically.",
        "solution_html": "<p><strong>Humidity Factor:</strong> High ambient humidity retards the net rate of liquid evaporation.</p>"
    },
    {
        "id": 24,
        "slide": 19,
        "challenge_set": 3,
        "question": "Why does water stored in a traditional terracotta matka (earthen pot) become cool even in scorching summer heat?",
        "options": [
            "Baked clay absorbs cold energy from planetary gravity",
            "Water seeps through microscopic clay pores and evaporates from the outer surface, extracting heat from the water inside",
            "The earthen pot contains chemical refrigerants like Freon",
            "Clay converts heat into sound waves"
        ],
        "correct": 1,
        "explanation": "Evaporation of water from the outer porous clay walls consumes latent heat of vaporization, extracting thermal energy from the remaining water inside.",
        "solution_html": "<p><strong>Matka Thermodynamics:</strong> Porous clay allows slow seepage and continuous surface evaporation, extracting heat from the interior.</p>"
    },
    {
        "id": 25,
        "slide": 19,
        "challenge_set": 3,
        "question": "How does sitting beneath a spinning ceiling fan cool a person who is sweating after exercising?",
        "options": [
            "The fan drops the ambient room air temperature by 20 degrees Celsius",
            "The moving air accelerates evaporation of sweat from the skin, extracting body heat and producing a cooling sensation",
            "The fan injects microscopic ice crystals into the pores",
            "The fan stops blood circulation in the arms"
        ],
        "correct": 1,
        "explanation": "Air movement speeds up sweat evaporation, which absorbs latent heat directly from human skin.",
        "solution_html": "<p><strong>Physiological Cooling:</strong> Human sweat functions as an evaporative coolant. Air movement accelerates this heat-extraction process.</p>"
    },
    {
        "id": 26,
        "slide": 19,
        "challenge_set": 3,
        "question": "Why do people in Indian towns and villages sprinkle water on their hot brick courtyards and rooftops on summer evenings?",
        "options": [
            "To attract clouds directly over their house",
            "The sprinkled water absorbs heat from the hot bricks and evaporates, significantly cooling the roof and courtyard",
            "To make the bricks softer to walk on",
            "To wash away negative magnetic fields"
        ],
        "correct": 1,
        "explanation": "Water absorbs large amounts of sensible and latent heat from hot masonry as it evaporates, reducing rooftop temperature.",
        "solution_html": "<p><strong>Evaporative Cooling in Architecture:</strong> Water's high latent heat of vaporization cools hot surfaces effectively when sprinkled on them.</p>"
    },
    {
        "id": 27,
        "slide": 19,
        "challenge_set": 3,
        "question": "What is the traditional Indian long-necked clay pot designed for evaporative cooling of summer drinking water called?",
        "options": [
            "Handi",
            "Surahi",
            "Kadahi",
            "Degchi"
        ],
        "correct": 1,
        "explanation": "A Surahi is a traditional clay pitcher with a slender neck and rounded body designed to chill drinking water via evaporative cooling.",
        "solution_html": "<p><strong>Heritage Vessel:</strong> As highlighted in Fig 8.8, the Surahi is a celebrated clay pot used across India for cooling water.</p>"
    },
    {
        "id": 28,
        "slide": 19,
        "challenge_set": 3,
        "question": "In the pot-in-pot refrigerator (Activity 8.9), why must water be poured into the sand layer regularly?",
        "options": [
            "To drown burrowing insects in the sand",
            "To keep the sand moist so that water can continuously evaporate through the porous outer pot to sustain cooling",
            "To make the cooler heavier so wind does not blow it away",
            "To turn the sand into cement"
        ],
        "correct": 1,
        "explanation": "Continuous evaporative cooling requires a steady moisture supply in the sand buffer to replace evaporated water.",
        "solution_html": "<p><strong>Zeer Operation:</strong> If the sand dries out, evaporation stops, and the interior returns to ambient temperature.</p>"
    },
    {
        "id": 29,
        "slide": 19,
        "challenge_set": 3,
        "question": "Which set of conditions will produce the fastest evaporation rate of water from an open container?",
        "options": [
            "Small surface area, low temperature, calm air, high humidity",
            "Large surface area, high temperature, strong wind, low humidity",
            "Large surface area, low temperature, high humidity, dark room",
            "Small surface area, high temperature, high humidity, calm air"
        ],
        "correct": 1,
        "explanation": "Evaporation is maximized by high surface area, high temperature, high wind speed, and low humidity.",
        "solution_html": "<p><strong>Optimal Evaporation:</strong> High heat + broad surface + low humidity + brisk wind = maximum molecular escape rate.</p>"
    },
    {
        "id": 30,
        "slide": 19,
        "challenge_set": 3,
        "question": "Why does a metal container filled with water fail to cool the water through evaporative cooling like a clay pot?",
        "options": [
            "Metal does not conduct heat",
            "Metal is non-porous; water cannot seep through to the outside to evaporate and extract heat",
            "Metal reflects all air molecules",
            "Metal generates its own internal heat"
        ],
        "correct": 1,
        "explanation": "Solid metal has no capillary pores. Without seepage to the outer surface, surface evaporation and evaporative cooling cannot occur.",
        "solution_html": "<p><strong>Impermeability:</strong> Stainless steel lacks the porosity essential for evaporative cooling.</p>"
    },
    {
        "id": 31,
        "slide": 20,
        "challenge_set": 4,
        "question": "Why does warm air containing water vapour rise upward into Earth's atmosphere?",
        "options": [
            "Water vapour is denser than dry nitrogen and oxygen",
            "Water vapour is lighter (lower molecular mass) than dry air, making warm humid air parcels less dense and buoyant",
            "Gravity pushes gas molecules upward toward the moon",
            "Centrifugal force from Earth's rotation lifts gases into orbit"
        ],
        "correct": 1,
        "explanation": "Water vapour (molar mass 18 g/mol) is lighter than dry air (average molar mass 29 g/mol); rising warm humid air ascends by buoyant convection.",
        "solution_html": "<p><strong>Buoyancy Principle:</strong> Warm, humid air is lighter than surrounding cold, dry air and rises like a hot air balloon.</p>"
    },
    {
        "id": 32,
        "slide": 20,
        "challenge_set": 4,
        "question": "As warm moist air ascends several kilometres above Earth's surface, what happens to its temperature?",
        "options": [
            "It gets hotter and hotter because it is closer to the Sun",
            "It becomes cooler and cooler as atmospheric pressure decreases and air expands",
            "Its temperature stays exactly at 100 degrees Celsius",
            "It turns instantly into molten lava"
        ],
        "correct": 1,
        "explanation": "Atmospheric pressure decreases with altitude, causing rising air to expand and cool adiabatically.",
        "solution_html": "<p><strong>Atmospheric Lapse Rate:</strong> Temperature drops steadily with altitude in the troposphere (roughly 6.5 \u00b0C per kilometre).</p>"
    },
    {
        "id": 33,
        "slide": 20,
        "challenge_set": 4,
        "question": "What are the microscopic airborne dust or smoke particles around which water vapour condenses to form cloud droplets called?",
        "options": [
            "Precipitation ions",
            "Cloud condensation nuclei",
            "Evaporation catalysts",
            "Hydrological crystals"
        ],
        "correct": 1,
        "explanation": "Dust, smoke, and salt aerosols serve as cloud condensation nuclei (CCN) upon which vapour condenses.",
        "solution_html": "<p><strong>Cloud Physics:</strong> Water vapour requires solid or liquid microscopic surfaces to condense into droplets in the atmosphere.</p>"
    },
    {
        "id": 34,
        "slide": 20,
        "challenge_set": 4,
        "question": "In Activity 8.10, why did haziness (a visible cloud) appear inside the bottle after burnt newspaper smoke was added and the bottle was released?",
        "options": [
            "The smoke burned the plastic bottle walls into ash",
            "Water vapour condensed onto the tiny smoke particles upon decompression and cooling, creating an aerosol cloud",
            "Paper ash dissolved into carbon dioxide gas",
            "The water turned into solid ice cubes inside the bottle"
        ],
        "correct": 1,
        "explanation": "Releasing the bottle drops the internal pressure, cooling the air and causing vapour to condense on the smoke nuclei.",
        "solution_html": "<p><strong>Cloud in a Bottle:</strong> Pressure release causes adiabatic cooling, triggering condensation onto smoke nuclei.</p>"
    },
    {
        "id": 35,
        "slide": 20,
        "challenge_set": 4,
        "question": "What happens when tiny suspended water droplets in a cloud collide and merge together into larger drops?",
        "options": [
            "They turn into invisible oxygen gas and disappear",
            "They become too heavy to remain suspended by updrafts and fall to Earth as rain",
            "They shoot upward into outer space",
            "They turn into solid volcanic rock"
        ],
        "correct": 1,
        "explanation": "Coalescence causes cloud droplets to grow until gravitational pull overcomes buoyant updrafts, resulting in rainfall.",
        "solution_html": "<p><strong>Rainfall Mechanism:</strong> Droplet growth through coalescence produces raindrops heavy enough to fall as precipitation.</p>"
    },
    {
        "id": 36,
        "slide": 20,
        "challenge_set": 4,
        "question": "Under freezing atmospheric conditions high above the ground, what forms of precipitation can fall instead of liquid rain?",
        "options": [
            "Hail or snow",
            "Molten iron",
            "Liquid methane",
            "Sandstorms"
        ],
        "correct": 0,
        "explanation": "Sub-zero temperatures freeze condensing moisture into ice crystals, which fall as snow, sleet, or hail.",
        "solution_html": "<p><strong>Solid Precipitation:</strong> When atmospheric temperatures fall below 0 \u00b0C, water precipitates as snow or hail.</p>"
    },
    {
        "id": 37,
        "slide": 20,
        "challenge_set": 4,
        "question": "Which of the following terms describes the continuous planetary circulation of water between oceans, atmosphere, and land?",
        "options": [
            "Rock cycle",
            "Water cycle (Hydrological cycle)",
            "Nitrogen cycle",
            "Carbon cycle"
        ],
        "correct": 1,
        "explanation": "The continuous circulation of water across Earth's reservoirs is called the water cycle.",
        "solution_html": "<p><strong>Earth Systems:</strong> The water cycle maintains life on land and redistributes solar thermal energy across the globe.</p>"
    },
    {
        "id": 38,
        "slide": 20,
        "challenge_set": 4,
        "question": "Why is ocean water, which makes up over 97% of Earth's total water, unsuitable for direct agricultural irrigation and human drinking?",
        "options": [
            "It is highly radioactive",
            "It contains high concentrations of dissolved mineral salts",
            "It is completely frozen into solid rock",
            "It has zero oxygen content"
        ],
        "correct": 1,
        "explanation": "Ocean water contains about 3.5% dissolved salts (mainly sodium chloride), making it saline and harmful to human kidneys and most crops.",
        "solution_html": "<p><strong>Salinity Barrier:</strong> Desalination requires massive energy, which is why freshwater preservation is critical.</p>"
    },
    {
        "id": 39,
        "slide": 20,
        "challenge_set": 4,
        "question": "What happens to the sludge removed from urban wastewater drains when it is heaped beside the drain for 3 to 4 days?",
        "options": [
            "It absorbs rainwater and doubles its total volume",
            "Water in the sludge evaporates, drastically reducing its weight and transportation costs before use as agricultural manure",
            "It dissolves into the asphalt road surface",
            "It undergoes nuclear transmutation into gold"
        ],
        "correct": 1,
        "explanation": "Solar evaporation dewaters the sludge, making it much lighter, safer, and cheaper to transport to farm fields as fertilizer.",
        "solution_html": "<p><strong>Exercise Q6 Application:</strong> Evaporation dewaters municipal sludge, reducing transport costs and biological hazards.</p>"
    },
    {
        "id": 40,
        "slide": 20,
        "challenge_set": 4,
        "question": "Which action best demonstrates the textbook's principle: 'Water is our responsibility before it is our right'?",
        "options": [
            "Leaving garden hoses running unattended all afternoon",
            "Practicing rainwater harvesting, turning off leaking taps, and keeping rivers free from untreated industrial effluents",
            "Dumping chemical plastic waste into local ponds",
            "Using filtered drinking water to wash car tires daily"
        ],
        "correct": 1,
        "explanation": "Conservation, water stewardship, and pollution prevention embody our civic responsibility toward planetary water security.",
        "solution_html": "<p><strong>Civic Stewardship:</strong> Conserving water resources and protecting freshwater ecosystems ensures sustainable water for all living beings.</p>"
    }
]

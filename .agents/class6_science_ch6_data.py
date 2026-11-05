"""
NCERT Class 6 Science Curiosity - Chapter 6: Materials Around Us
Data Module: 16 Concept Slides (with Full Classroom Audio Lectures & 32 Checkpoints) + 40 Mastery Assessment Questions
Zero raw LaTeX - Pure Unicode formatting.
Zero lecturer persona names.
"""

CHAPTER_META = {
    "chapter_num": 6,
    "title": "Materials Around Us",
    "subtitle": "Properties, Classification, and the Nature of Physical Matter",
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
        "title": "Object & Material",
        "subtitle": "Distinguishing Physical Items from the Substances That Form Them",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Look around your classroom or home. You see notebooks, pens, water bottles, desks, windows, and clothes. Every single physical item in our environment is an <strong class="text-indigo-300 font-semibold">object</strong>, but the substance from which an object is fashioned is called a <strong class="text-emerald-300 font-semibold">material</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700/80 space-y-2">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">The Fundamental Distinction</h4>
                    <ul class="text-xs space-y-1.5 text-slate-300">
                        <li>• <strong class="text-white">Object:</strong> A distinct item manufactured or found with a specific shape and purpose (e.g., a ballpoint pen, a dining chair).</li>
                        <li>• <strong class="text-white">Material:</strong> The matter or substance utilized to build that object (e.g., plastic, stainless steel, wood, glass, cotton, clay).</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">Multi-Material Anatomy:</strong> Many everyday items require multiple distinct materials working in harmony. A simple pen combines an outer plastic barrel, a brass or tungsten ball tip, a steel spring, and liquid solvent ink.
                </div>
            </div>
        """,
        "lecture_script": "Welcome to Materials Around Us! Look around at your desk, your bag, and your books. Everything you see and touch is an object. But what are these objects made of? The substance used to create any object is called a material. Notice that while a notebook is an object, paper is the material. While a window is an object, glass and wood are the materials. Furthermore, many everyday objects are engineered by combining several materials together. A pen, for instance, uses plastic for its outer barrel, steel for its clip and spring, brass for the tip, and liquid ink. Recognizing the distinction between an object and its constituent materials is the first fundamental step in physical science.",
        "spoken_text": "Welcome to Materials Around Us! Look around at your desk, your bag, and your books. Everything you see and touch is an object. But what are these objects made of? The substance used to create any object is called a material. Notice that while a notebook is an object, paper is the material. While a window is an object, glass and wood are the materials. Furthermore, many everyday objects are engineered by combining several materials together. A pen, for instance, uses plastic for its outer barrel, steel for its clip and spring, brass for the tip, and liquid ink. Recognizing the distinction between an object and its constituent materials is the first fundamental step in physical science.",
        "checkpoints": [
            {
                "question": "Which of the following correctly pairs an 'object' with its primary 'material'?",
                "options": [
                    "Wood (object) made from Chair (material)",
                    "Tumbler (object) made from Glass (material)",
                    "Plastic (object) made from Bucket (material)",
                    "Cotton (object) made from Shirt (material)"
                ],
                "correct": 1,
                "explanation": "A tumbler is an object fashioned for drinking, while glass is the material of which it is made. In all other choices, the relationship is inverted.",
                "study_insight": "Remember: You hold an object; it is manufactured out of a material."
            },
            {
                "question": "A typical wooden graphite pencil consists of which combination of materials?",
                "options": [
                    "Wood casing, graphite clay core, metal ferrule, and rubber eraser",
                    "Pure carbon diamond casing with liquid ink core",
                    "A single solid rod of pure cast iron",
                    "Molded glass casing with paper core"
                ],
                "correct": 0,
                "explanation": "A standard pencil is a multi-material assembly: softwood casing for gripping, compressed graphite-clay mixture for writing, an aluminium ferrule collar, and vulcanized rubber for erasing.",
                "study_insight": "Complex everyday tools combine distinct materials to leverage the unique physical properties of each part."
            }
        ]
    },
    {
        "id": 2,
        "title": "Ancient Terracotta",
        "subtitle": "India's Deep Heritage in Pottery, Metallurgy, and Fired Clay",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Humans have transformed natural materials for thousands of years. In ancient India, early settlements at <strong class="text-amber-300 font-semibold">Lahuradewa</strong> (Uttar Pradesh) and <strong class="text-amber-300 font-semibold">Mehrgarh</strong> mastered the art of pottery dating back over 8,000 years.
                </p>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-400 block mb-1">Raw River Clay</span>
                        <p class="text-slate-300 leading-relaxed">Soft, malleable, and plastic when moist; easily shaped on a rotating potter's wheel but fragile and dissolves in water when raw.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-emerald-400 block mb-1">Fired Terracotta</span>
                        <p class="text-slate-300 leading-relaxed">Heated in high-temperature kilns (600°C to 1000°C); chemically transforms into rock-hard, waterproof, ceramic terracotta with distinctive reddish hue.</p>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    <strong class="text-indigo-300">Harappan Craftsmanship:</strong> The Indus Valley Civilization produced world-renowned terracotta figurines, granary storage jars, drainage pipes, and painted pottery featuring bold black geometric patterns on lustrous red slip.
                </div>
            </div>
        """,
        "lecture_script": "Humanity's journey with materials has deep historical roots in the Indian subcontinent. Thousands of years ago, ancient artisans discovered that raw clay gathered from riverbeds possessed remarkable plasticity when mixed with water. It could be spun on a potter's wheel into delicate vessels. However, raw dried clay remains brittle and dissolves when exposed to rain. The breakthrough came with the invention of high-temperature pottery kilns at sites like Lahuradewa and Mehrgarh. Firing clay at over 800 degrees Celsius permanently alters its internal structure, transforming soft mud into durable, rock-hard terracotta. During the Harappan civilization, terracotta was engineered into waterproof grain silos, urban drainage channels, and intricately painted artistic figurines.",
        "spoken_text": "Humanity's journey with materials has deep historical roots in the Indian subcontinent. Thousands of years ago, ancient artisans discovered that raw clay gathered from riverbeds possessed remarkable plasticity when mixed with water. It could be spun on a potter's wheel into delicate vessels. However, raw dried clay remains brittle and dissolves when exposed to rain. The breakthrough came with the invention of high-temperature pottery kilns at sites like Lahuradewa and Mehrgarh. Firing clay at over 800 degrees Celsius permanently alters its internal structure, transforming soft mud into durable, rock-hard terracotta. During the Harappan civilization, terracotta was engineered into waterproof grain silos, urban drainage channels, and intricately painted artistic figurines.",
        "checkpoints": [
            {
                "question": "What critical transformation occurs when soft river clay is fired in a potter's kiln to produce terracotta?",
                "options": [
                    "The clay becomes softer and melts into transparent liquid glass",
                    "The clay permanently hardens, loses moisture, and becomes insoluble and durable",
                    "The clay transforms into pure metallic gold",
                    "The clay expands into flexible spongy rubber"
                ],
                "correct": 1,
                "explanation": "High-temperature baking permanently drives out chemically bound water and vitrifies mineral particles, turning soft, soluble clay into hard, insoluble terracotta.",
                "study_insight": "Thermal processing alters physical and chemical properties, turning fragile raw mud into durable ceramic."
            },
            {
                "question": "Which historic archaeological civilization is celebrated for its painted red-and-black terracotta pottery and urban sanitation pipes?",
                "options": [
                    "The Harappan (Indus Valley) Civilization",
                    "The Viking explorers",
                    "The Roman Colosseum gladiators",
                    "The Aztec pyramid builders"
                ],
                "correct": 0,
                "explanation": "The Harappan civilization (2600–1900 BCE) achieved world-renowned mastery in terracotta technology, creating interlocking sanitary drainage pipes, storage vessels, and toy carts.",
                "study_insight": "Material science has ancient origins; early civilizations thrived by mastering pyrotechnology and ceramics."
            }
        ]
    },
    {
        "id": 3,
        "title": "Many Materials",
        "subtitle": "How a Single Object Can Be Manufactured from Diverse Materials",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    A single functional object can be manufactured from a wide variety of different materials depending on cost, availability, aesthetic preference, and operating conditions.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2.5">
                    <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Example: The Humble Drinking Tumbler</h4>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-[11px] text-center">
                        <div class="p-2 rounded-lg bg-slate-800 border border-slate-700">
                            <span class="block text-lg mb-1">🥛</span>
                            <span class="font-bold text-white block">Glass</span>
                            <span class="text-slate-400 text-[10px]">Transparent, inert, fragile</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-800 border border-slate-700">
                            <span class="block text-lg mb-1">🥤</span>
                            <span class="font-bold text-white block">Plastic</span>
                            <span class="text-slate-400 text-[10px]">Lightweight, unbreakable</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-800 border border-slate-700">
                            <span class="block text-lg mb-1">☕</span>
                            <span class="font-bold text-white block">Steel</span>
                            <span class="text-slate-400 text-[10px]">Sturdy, rust-proof, opaque</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-800 border border-slate-700">
                            <span class="block text-lg mb-1">🏺</span>
                            <span class="font-bold text-white block">Clay Kulhad</span>
                            <span class="text-slate-400 text-[10px]">Eco-friendly, cooling</span>
                        </div>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-200">
                    <strong class="font-semibold text-white">Other Universal Objects:</strong> Plates (thalis) can be crafted from steel, porcelain ceramic, silver, brass, or disposable dried banana leaves!
                </div>
            </div>
        """,
        "lecture_script": "Consider a common everyday object like a drinking tumbler. What material must it be made of? You might use a sparkling transparent glass tumbler at a restaurant, a lightweight colorful plastic tumbler during a train journey, an unbreakable stainless steel tumbler at home, a brass tumbler during traditional festivals, or a porous earthen kulhad at a tea stall. All five items serve the identical purpose of holding liquid to drink, yet each is crafted from a completely different material. Each material imparts distinct advantages: glass offers transparency and chemical neutrality, steel provides lifetime durability, plastic is shatterproof and portable, while terracotta imparts natural evaporative cooling and earthy aroma.",
        "spoken_text": "Consider a common everyday object like a drinking tumbler. What material must it be made of? You might use a sparkling transparent glass tumbler at a restaurant, a lightweight colorful plastic tumbler during a train journey, an unbreakable stainless steel tumbler at home, a brass tumbler during traditional festivals, or a porous earthen kulhad at a tea stall. All five items serve the identical purpose of holding liquid to drink, yet each is crafted from a completely different material. Each material imparts distinct advantages: glass offers transparency and chemical neutrality, steel provides lifetime durability, plastic is shatterproof and portable, while terracotta imparts natural evaporative cooling and earthy aroma.",
        "checkpoints": [
            {
                "question": "Which of the following objects can be made from glass, metal, plastic, or ceramic?",
                "options": [
                    "A dining dinner plate (thali)",
                    "A woolen winter muffler",
                    "A paper notebook page",
                    "A wooden cricket bat handle"
                ],
                "correct": 0,
                "explanation": "Dinner plates are manufactured out of stainless steel, melamine plastic, borosilicate glass, porcelain ceramic, or even silver. Mufflers require fibers, notebook pages require paper pulp, and cricket bats require wood.",
                "study_insight": "Objects defined by rigid structural shapes (like vessels or furniture) often permit diverse material choices."
            },
            {
                "question": "Why is stainless steel preferred over glass for tumblers used by young school children?",
                "options": [
                    "Steel is completely transparent so drinks can be inspected",
                    "Steel is shatterproof, durable, and will not produce sharp dangerous shards if dropped",
                    "Steel is extremely soft and dissolves in drinking water",
                    "Steel is much lighter than air and floats effortlessly"
                ],
                "correct": 1,
                "explanation": "Steel has high tensile strength and toughness, meaning it resists impact without shattering, making it significantly safer for children compared to brittle glass.",
                "study_insight": "Safety and resilience often determine material selection in everyday consumer goods."
            }
        ]
    },
    {
        "id": 4,
        "title": "Many Objects",
        "subtitle": "How a Single Material Can Be Fashioned into Thousands of Unique Items",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Just as one object can be made from many materials, the reverse is equally true: a single raw material can be shaped, molded, or fabricated into thousands of entirely different objects.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700/80 space-y-2">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Case Study: The Versatility of Wood</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        From a single felled tree trunk, artisans and factories produce:
                    </p>
                    <div class="flex flex-wrap gap-2 text-xs">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 text-amber-300 border border-slate-700">🪑 Chairs & Desks</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 text-amber-300 border border-slate-700">🚪 Doors & Windows</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 text-amber-300 border border-slate-700">🏏 Cricket Bats</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 text-amber-300 border border-slate-700">✏️ Pencil Casings</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 text-amber-300 border border-slate-700">🚣 Rowboats</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 text-amber-300 border border-slate-700">🚜 Bullock Carts</span>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    <strong class="text-sky-300">Other Super-Materials:</strong> <strong class="text-white">Plastic</strong> forms toothbrushes, water pipes, toy blocks, bucket containers, and electrical insulation; <strong class="text-white">Iron</strong> forms railway tracks, bridge girders, kitchen tongs, and sewing needles.
                </div>
            </div>
        """,
        "lecture_script": "Now look at the reciprocal concept. What happens when you inspect a single versatile material like wood? Wood can be carved into a sturdy study table, planed into a flat doorway, turned on a lathe into a cricket bat, hollowed into a floating canoe, sliced into matchsticks, or shaped into a bullock cart wheel. Likewise, petroleum-derived plastic can be extruded into thin food wrap, blow-molded into a rigid storage tub, injection-molded into telephone casings, or woven into nylon rope. A material's innate physical qualities—such as its mechanical strength, workability, and thermal resistance—allow designers to transform it into an astonishing catalog of functional objects.",
        "spoken_text": "Now look at the reciprocal concept. What happens when you inspect a single versatile material like wood? Wood can be carved into a sturdy study table, planed into a flat doorway, turned on a lathe into a cricket bat, hollowed into a floating canoe, sliced into matchsticks, or shaped into a bullock cart wheel. Likewise, petroleum-derived plastic can be extruded into thin food wrap, blow-molded into a rigid storage tub, injection-molded into telephone casings, or woven into nylon rope. A material's innate physical qualities—such as its mechanical strength, workability, and thermal resistance—allow designers to transform it into an astonishing catalog of functional objects.",
        "checkpoints": [
            {
                "question": "Which of the following groups consists ENTIRELY of objects commonly made from leather?",
                "options": [
                    "Shoes, belts, cricket balls, and wallets",
                    "Window panes, drinking cups, and reading spectacles",
                    "Cooking pans, sewing needles, and railway tracks",
                    "Notebook pages, paper envelopes, and cardboard boxes"
                ],
                "correct": 0,
                "explanation": "Leather (processed animal hide) is tough, flexible, and wear-resistant, making it ideal for footwear, formal waistbelts, regulation cricket balls, and wallets.",
                "study_insight": "A single material's distinct balance of flexibility and toughness enables a wide family of related items."
            },
            {
                "question": "What common material is used to manufacture automobile tires, rubber bands, elastic shoe soles, and pencil erasers?",
                "options": [
                    "Pure copper metal",
                    "Natural and synthetic rubber",
                    "Transparent glass",
                    "Granite stone rock"
                ],
                "correct": 1,
                "explanation": "Rubber has high elasticity, frictional grip, and shock absorption, making it the universal material for tires, rubber bands, shoe soles, and pencil erasers.",
                "study_insight": "Elasticity and high friction make rubber irreplaceable for gripping surfaces and stretching fasteners."
            }
        ]
    },
    {
        "id": 5,
        "title": "Sorting Groups",
        "subtitle": "The Scientific Method of Arranging Materials into Coherent Categories",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Imagine walking into a grocery store where grains, soaps, biscuits, and oils were dumped together in random heaps. Finding anything would be impossible! Grouping objects systematically makes our study efficient and organized.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">What is Classification?</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        <strong class="text-white">Classification</strong> is the systematic grouping of objects or materials on the basis of their similarities and differences in observable properties.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-indigo-300 block mb-1">By Geometrical Shape</span>
                        <span class="text-slate-300 text-[11px]">Spherical (footballs, apples, marbles, oranges) vs Non-spherical (books, cubical boxes, pencils).</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-emerald-300 block mb-1">By Edibility & Use</span>
                        <span class="text-slate-300 text-[11px]">Edible food items (milk, rice, bananas) vs Inedible non-food tools (screwdrivers, erasers, locks).</span>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">Scientific Benefit:</strong> Grouping helps scientists discern patterns in material behaviors, predict how unfamiliar materials will react, and locate items rapidly.
                </div>
            </div>
        """,
        "lecture_script": "Imagine walking into a massive library containing one hundred thousand books, but having all the books dumped in a giant chaotic mountain on the floor. Searching for a single science textbook would take days! Instead, librarians classify books by subject, language, and author. In the exact same way, scientists classify the vast universe of materials. Classification is the systematic method of sorting objects into groups based on shared similarities and noticeable differences. We can group items by shape—such as round objects like marbles, cricket balls, and oranges. We can group by edibility, sorting vegetables and grains away from inedible tools. Or we can group by material origin, separating plant-derived wood and cotton from mined metals and refined plastics. Grouping reveals systematic patterns across nature.",
        "spoken_text": "Imagine walking into a massive library containing one hundred thousand books, but having all the books dumped in a giant chaotic mountain on the floor. Searching for a single science textbook would take days! Instead, librarians classify books by subject, language, and author. In the exact same way, scientists classify the vast universe of materials. Classification is the systematic method of sorting objects into groups based on shared similarities and noticeable differences. We can group items by shape—such as round objects like marbles, cricket balls, and oranges. We can group by edibility, sorting vegetables and grains away from inedible tools. Or we can group by material origin, separating plant-derived wood and cotton from mined metals and refined plastics. Grouping reveals systematic patterns across nature.",
        "checkpoints": [
            {
                "question": "Which of the following sets contains objects that are ALL approximately spherical or round in shape?",
                "options": [
                    "A tennis ball, a globe, an orange, and a glass marble",
                    "A geometry ruler, a blackboard, a brick, and an eraser",
                    "A pencil box, a shoe carton, a smartphone, and a table top",
                    "A piece of chalk, a sewing needle, a test tube, and a nail"
                ],
                "correct": 0,
                "explanation": "Tennis balls, planetary globes, oranges, and marbles are all three-dimensional spheres, sharing the property of roundness.",
                "study_insight": "Shape is one of the quickest initial physical criteria for macroscopic grouping."
            },
            {
                "question": "Why is systematic classification of materials considered essential in science?",
                "options": [
                    "It makes materials completely disappear from the laboratory",
                    "It allows systematic study, reveals patterns in properties, and simplifies organization",
                    "It transforms all liquids permanently into solid metals",
                    "It stops gravitational attraction between objects"
                ],
                "correct": 1,
                "explanation": "Classification enables organized storage, systematic comparison, and rapid deduction of general properties belonging to entire material classes.",
                "study_insight": "Classification transforms disorganized data into predictive, structured scientific knowledge."
            }
        ]
    },
    {
        "id": 6,
        "title": "Fit for Purpose",
        "subtitle": "Why Material Choice Strictly Depends on Physical Properties & Function",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Have you ever wondered why cooking pots are never made of cardboard, or why umbrellas are never stitched out of porous cotton netting? The choice of a material depends strictly on its <strong class="text-indigo-300 font-semibold">properties</strong> and the <strong class="text-emerald-300 font-semibold">purpose</strong> for which the object will be used.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-rose-300 uppercase tracking-wider">The Cloth Tumbler Paradox</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        To hold water, a container must possess the property of being <strong class="text-white">water-tight and impermeable</strong>. A piece of woven cotton fabric contains thousands of microscopic pores; liquid instantly leaks through. Hence, making a tumbler out of cloth is absurd!
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700 space-y-2 text-xs">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Activity 6.4: Ball Bounce Investigation</h4>
                    <div class="grid grid-cols-3 gap-2 text-center text-[11px]">
                        <div class="p-2 rounded bg-slate-900 border border-slate-700">
                            <span class="font-bold text-emerald-400 block">Tennis Ball</span>
                            <span class="text-slate-300">Hollow rubber + felt; high elastic rebound for tennis.</span>
                        </div>
                        <div class="p-2 rounded bg-slate-900 border border-slate-700">
                            <span class="font-bold text-amber-400 block">Cricket Ball</span>
                            <span class="text-slate-300">Cork core + stitched leather; heavy, firm, durable.</span>
                        </div>
                        <div class="p-2 rounded bg-slate-900 border border-slate-700">
                            <span class="font-bold text-sky-400 block">Foam Stress Ball</span>
                            <span class="text-slate-300">Polyurethane sponge; absorbs energy, zero bounce!</span>
                        </div>
                    </div>
                </div>
            </div>
        """,
        "lecture_script": "Why do engineers choose specific materials for specific machines? Imagine trying to make a cooking pan out of paper. The moment you place it over a gas burner, the paper ignites into flames! Or imagine making an umbrella out of wire mesh—rain would pour straight through. Material selection is always purpose-driven. To boil water, you need a material that conducts heat rapidly and withstands high temperatures without melting, like copper or aluminium. But to hold that scorching pan safely, the handle must be an insulator that stays cool, like Bakelite plastic or wood. Consider balls used in sports: a tennis ball uses vulcanized pressurized rubber to generate elastic rebound, whereas a cricket ball uses wound twine and thick leather to provide mass, hardness, and durability. Function strictly dictates the material.",
        "spoken_text": "Why do engineers choose specific materials for specific machines? Imagine trying to make a cooking pan out of paper. The moment you place it over a gas burner, the paper ignites into flames! Or imagine making an umbrella out of wire mesh—rain would pour straight through. Material selection is always purpose-driven. To boil water, you need a material that conducts heat rapidly and withstands high temperatures without melting, like copper or aluminium. But to hold that scorching pan safely, the handle must be an insulator that stays cool, like Bakelite plastic or wood. Consider balls used in sports: a tennis ball uses vulcanized pressurized rubber to generate elastic rebound, whereas a cricket ball uses wound twine and thick leather to provide mass, hardness, and durability. Function strictly dictates the material.",
        "checkpoints": [
            {
                "question": "Why would constructing a bucket out of unlaminated cardboard be an engineering failure for holding water?",
                "options": [
                    "Cardboard is too shiny and reflects too much sunlight",
                    "Cardboard absorbs water, loses structural strength, softens, and leaks liquid",
                    "Cardboard is magnetic and pulls iron out of drinking water",
                    "Cardboard instantly freezes all room temperature water into solid ice"
                ],
                "correct": 1,
                "explanation": "Cellulose cardboard is porous and hydrophilic; it rapidly absorbs water, disintegrates into pulp, and cannot contain liquid under hydrostatic pressure.",
                "study_insight": "Properties must match operational demands: liquid containers require non-porous, waterproof materials."
            },
            {
                "question": "Why are pressure cooker bodies made of aluminium or steel while the handles are made of Bakelite plastic?",
                "options": [
                    "Aluminium insulates heat, while Bakelite conducts heat to the chef's hand",
                    "Metals conduct heat to cook food quickly, while Bakelite is a thermal insulator protecting hands from burns",
                    "Bakelite is much cheaper to throw into fire than aluminium",
                    "Metals are transparent so the chef can watch the food steam"
                ],
                "correct": 1,
                "explanation": "Cooking requires high thermal conductivity in the vessel body to transfer heat from the flame to the food, but low thermal conductivity (insulation) in the handle so it can be held safely.",
                "study_insight": "Smart engineering pairs conductors with insulators in the same thermal device."
            }
        ]
    },
    {
        "id": 7,
        "title": "Shiny Metals",
        "subtitle": "Understanding Lustre, Metallic Sheen, and Surface Oxidation",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    When you look at different materials, one of the first physical properties you observe is their surface shine or appearance. Materials that exhibit a characteristic shiny, reflective sheen are termed <strong class="text-amber-300 font-semibold">lustrous</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">What Gives Metals Their Lustre?</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Pure metals such as <strong class="text-white">gold, silver, copper, aluminium, and iron</strong> possess metallic lustre. Their tightly packed, orderly crystalline atoms and free electrons reflect incident light rays directly back to our eyes.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-xs space-y-1.5">
                    <span class="font-bold text-rose-300 block">The Tarnish & Oxidation Trap</span>
                    <p class="text-slate-300 leading-relaxed">
                        Why do old iron rods or copper vessels look dull and dark? Exposure to moist air, oxygen, and carbon dioxide causes chemical reactions on the surface, creating thin layers of rust (iron oxide) or green patina (basic copper carbonate).
                    </p>
                    <p class="text-amber-300 font-semibold">
                        💡 Key Scientific Test: Always inspect a <span class="underline">freshly cut</span> or sandpapered metal surface to observe its true, uncorrupted metallic lustre!
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us explore the property called lustre. Lustre simply refers to the natural shine or gleaming surface characteristic of pure materials, especially metals. Gold jewellery, silver coins, copper wires, and aluminium sheets all shine brightly under the light. But here is an important scientific question: why does an iron rod lying in a construction yard look reddish-brown and dull, without any shine? Has it lost its nature as a metal? No! Over weeks and months, the surface of iron reacts with oxygen and atmospheric moisture to form iron oxide, commonly known as rust. This dull outer coating masks the metal's true appearance. If a blacksmith cuts that old iron rod with a hacksaw or rubs it with rough sandpaper, the freshly exposed surface gleams with unmistakable metallic lustre. To test for true lustre, always examine a freshly cut surface.",
        "spoken_text": "Let us explore the property called lustre. Lustre simply refers to the natural shine or gleaming surface characteristic of pure materials, especially metals. Gold jewellery, silver coins, copper wires, and aluminium sheets all shine brightly under the light. But here is an important scientific question: why does an iron rod lying in a construction yard look reddish-brown and dull, without any shine? Has it lost its nature as a metal? No! Over weeks and months, the surface of iron reacts with oxygen and atmospheric moisture to form iron oxide, commonly known as rust. This dull outer coating masks the metal's true appearance. If a blacksmith cuts that old iron rod with a hacksaw or rubs it with rough sandpaper, the freshly exposed surface gleams with unmistakable metallic lustre. To test for true lustre, always examine a freshly cut surface.",
        "checkpoints": [
            {
                "question": "Which of the following materials naturally possesses metallic lustre?",
                "options": [
                    "A freshly cut copper pipe",
                    "A dry wooden block",
                    "A strip of cotton cardboard",
                    "A lump of dry garden soil"
                ],
                "correct": 0,
                "explanation": "Copper is a transition metal with high reflectivity and distinctive reddish-golden metallic lustre. Wood, cardboard, and soil are non-lustrous.",
                "study_insight": "Metallic lustre is a characteristic physical signature of metallic elements and their alloys."
            },
            {
                "question": "Why do copper water jugs often lose their shine and develop a dull, greenish coating after prolonged use?",
                "options": [
                    "The copper slowly turns into molten plastic",
                    "The copper surface reacts with atmospheric oxygen, moisture, and carbon dioxide",
                    "The copper evaporates completely into the surrounding air",
                    "The copper is magnetized by Earth's gravitational pull"
                ],
                "correct": 1,
                "explanation": "Copper oxidizes when exposed to moist air, forming a dull surface film of copper oxide and basic copper carbonate (patina), which dulls its lustre.",
                "study_insight": "Chemical corrosion taints outer surfaces; rubbing with lemon or tamarind reveals fresh lustre."
            }
        ]
    },
    {
        "id": 8,
        "title": "Dull Surfaces",
        "subtitle": "Non-Lustrous Materials and the Science of Artificial Coatings",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    In contrast to metals, most non-metallic materials in our surroundings are naturally <strong class="text-slate-300 font-semibold">non-lustrous</strong>. Their surfaces scatter light in all random directions (diffuse reflection), appearing dull, matte, or textured.
                </p>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-400 block mb-1">Naturally Non-Lustrous</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">Paper, cardboard, dry wood, rubber, leather, chalk, jute ropes, and natural cotton fabrics.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-sky-400 block mb-1">Artificial Shine</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">Polishing wooden tables with polyurethane lacquer, wax coatings on apples, or electroplating zinc onto iron.</p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 space-y-1">
                    <strong class="text-indigo-300">True Lustre vs Cosmetic Glaze:</strong>
                    <p class="leading-relaxed">
                        A polished wooden tabletop shines because of an artificial coat of clear chemical varnish, not because wood itself has metallic lustre. Cutting through the polished wood reveals dull cellulose fibers inside.
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Now consider non-lustrous materials. When you observe a wooden plank, a cardboard box, a rubber shoe sole, or a piece of chalk, light does not reflect back in a concentrated, shiny beam. Instead, the microscopic irregularities of these materials scatter light rays in all random directions. This is called diffuse reflection, and it makes the surface look dull and matte. However, humans have learned to apply artificial coatings. When an artisan applies glossy varnish or clear lacquer to a dining table, the liquid fills the microscopic pores and cures into a glass-smooth surface. The table looks shiny! But do not be misled: that shine belongs to the chemical polish, not to the wood itself. If you saw the wood in half, the interior grain remains completely non-lustrous.",
        "spoken_text": "Now consider non-lustrous materials. When you observe a wooden plank, a cardboard box, a rubber shoe sole, or a piece of chalk, light does not reflect back in a concentrated, shiny beam. Instead, the microscopic irregularities of these materials scatter light rays in all random directions. This is called diffuse reflection, and it makes the surface look dull and matte. However, humans have learned to apply artificial coatings. When an artisan applies glossy varnish or clear lacquer to a dining table, the liquid fills the microscopic pores and cures into a glass-smooth surface. The table looks shiny! But do not be misled: that shine belongs to the chemical polish, not to the wood itself. If you saw the wood in half, the interior grain remains completely non-lustrous.",
        "checkpoints": [
            {
                "question": "Which of the following items is naturally non-lustrous in its pure, untreated state?",
                "options": [
                    "A gold wedding ring",
                    "A dry wooden branch",
                    "A polished silver spoon",
                    "An aluminium cooking foil"
                ],
                "correct": 1,
                "explanation": "A dry wooden branch is made of cellulose plant fibers and lignin, which diffuse light and lack metallic crystalline lustre.",
                "study_insight": "Biological materials like plant wood and cotton are naturally non-lustrous."
            },
            {
                "question": "How can a scientist verify whether a shiny object owes its shine to natural metallic lustre or an artificial surface varnish?",
                "options": [
                    "By boiling it in water for ten hours",
                    "By cutting it open or scraping the surface to inspect the freshly exposed interior",
                    "By placing a strong magnet next to it",
                    "By weighing it on a kitchen balance"
                ],
                "correct": 1,
                "explanation": "Inspecting a freshly cut cross-section reveals whether the internal bulk substance has intrinsic metallic lustre or merely a thin external cosmetic coating.",
                "study_insight": "True material properties exist throughout the bulk substance, not just on the outer skin."
            }
        ]
    },
    {
        "id": 9,
        "title": "Hard & Soft",
        "subtitle": "Compressibility, Scratch Resistance, and Relative Hardness",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    When you press different materials with your hands, some compress easily while others resist your force completely. This tactile difference defines the physical property of <strong class="text-indigo-300 font-semibold">hardness</strong>.
                </p>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-emerald-400 block mb-1">Soft Materials</span>
                        <p class="text-slate-300 leading-relaxed">
                            Materials that can be <strong class="text-white">easily compressed</strong> or scratched with your fingernail (e.g., bath sponge, cotton balls, candle wax, soft eraser).
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-rose-400 block mb-1">Hard Materials</span>
                        <p class="text-slate-300 leading-relaxed">
                            Materials that are <strong class="text-white">difficult to compress</strong> or scratch even with an iron nail (e.g., iron rod, granite stone, diamond, hardened wood).
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-1.5">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Hardness is Relative!</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Hardness is not an all-or-nothing label; it exists on a comparative continuum:
                    </p>
                    <div class="p-2 rounded bg-slate-950 font-mono text-center text-indigo-300 border border-slate-800">
                        Cotton &lt; Candle Wax &lt; Soft Wood &lt; Iron &lt; Diamond
                    </div>
                    <p class="text-slate-400 text-[11px]">
                        Rubber is harder than sponge (it resists finger squishing much more), yet rubber is softer than iron (an iron nail easily punctures and scratches rubber).
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us examine hardness and softness. When you squeeze a foam sponge or a ball of cotton wool between your fingers, its volume visibly shrinks. You can compress it effortlessly. Materials that are easily compressed or scratched with a fingernail are classified as soft. Candle wax, clay, and ripe fruit are common examples. Now, try squeezing a steel spoon or a piece of granite rock with all your strength. You cannot compress them by even a fraction of a millimeter. Materials that are difficult or impossible to compress and resist being scratched by metal tools are termed hard. But notice something crucial: hardness is relative! A solid rubber ball feels very firm and hard compared to a soft kitchen sponge. Yet, if you press an iron nail into that same rubber ball, the nail pierces right through it. Rubber is harder than sponge, but far softer than iron. Hardness is always a comparison between two substances.",
        "spoken_text": "Let us examine hardness and softness. When you squeeze a foam sponge or a ball of cotton wool between your fingers, its volume visibly shrinks. You can compress it effortlessly. Materials that are easily compressed or scratched with a fingernail are classified as soft. Candle wax, clay, and ripe fruit are common examples. Now, try squeezing a steel spoon or a piece of granite rock with all your strength. You cannot compress them by even a fraction of a millimeter. Materials that are difficult or impossible to compress and resist being scratched by metal tools are termed hard. But notice something crucial: hardness is relative! A solid rubber ball feels very firm and hard compared to a soft kitchen sponge. Yet, if you press an iron nail into that same rubber ball, the nail pierces right through it. Rubber is harder than sponge, but far softer than iron. Hardness is always a comparison between two substances.",
        "checkpoints": [
            {
                "question": "Which of the following objects can be easily compressed between your thumb and index finger?",
                "options": [
                    "A piece of bath foam sponge",
                    "A steel ball bearing",
                    "A glass marble",
                    "A granite pebble"
                ],
                "correct": 0,
                "explanation": "Foam sponge contains flexible open cells filled with air, allowing it to compress under very light finger pressure.",
                "study_insight": "High compressibility is the benchmark of soft materials."
            },
            {
                "question": "If an iron nail easily scratches a wooden desk, but the same nail cannot scratch a sheet of hardened glass, which ranking of hardness is correct?",
                "options": [
                    "Wood is harder than Iron, and Iron is harder than Glass",
                    "Glass is harder than Iron, and Iron is harder than Wood",
                    "All three materials have exactly identical hardness",
                    "Wood is the hardest substance in the universe"
                ],
                "correct": 1,
                "explanation": "A harder substance scratches a softer one. Since iron scratches wood, iron > wood. Since glass resists scratching by iron, glass > iron. Therefore: Glass > Iron > Wood.",
                "study_insight": "The scratch test determines relative hardness: the scratcher is harder than the scratched."
            }
        ]
    },
    {
        "id": 10,
        "title": "Clear Vision",
        "subtitle": "The Optical Physics of Transparent Materials",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Have you ever looked out of a clean glass window on a sunny morning? You see trees, birds, and distant buildings with sharp clarity. Materials that permit light to pass straight through them without scattering are called <strong class="text-cyan-300 font-semibold">transparent</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Definition: Transparent Materials</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Those materials through which objects can be seen <strong class="text-white">clearly and distinctly</strong> because nearly 100% of incident light rays pass directly through in parallel lines.
                    </p>
                    <div class="grid grid-cols-2 gap-2 text-xs pt-1 text-slate-200">
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🔍 Clear Window Glass</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">💧 Pure Clean Water</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">💨 Invisible Atmospheric Air</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">📄 Clear Cellophane Film</div>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">Everyday Application:</strong> Shopkeepers store biscuits, candies, and sweets in transparent glass or plastic jars so customers can see and choose them instantly without opening the lids!
                </div>
            </div>
        """,
        "lecture_script": "Now we arrive at the optical properties of materials—how they interact with light. First are transparent materials. When light strikes a sheet of clean window glass, pure water, or the air around us, the light waves pass straight through without obstruction. Because the light paths remain orderly and parallel, images formed on our eyes are crisp, sharp, and detailed. You can see objects on the other side with complete clarity. Think about a candy shop: the shopkeeper stores colourful sweets, lozenges, and biscuits inside transparent glass or clear plastic jars. Why? Because customers and children can immediately see the delicious treats inside without needing to open every container. Transparent materials are essential whenever visibility is paramount.",
        "spoken_text": "Now we arrive at the optical properties of materials—how they interact with light. First are transparent materials. When light strikes a sheet of clean window glass, pure water, or the air around us, the light waves pass straight through without obstruction. Because the light paths remain orderly and parallel, images formed on our eyes are crisp, sharp, and detailed. You can see objects on the other side with complete clarity. Think about a candy shop: the shopkeeper stores colourful sweets, lozenges, and biscuits inside transparent glass or clear plastic jars. Why? Because customers and children can immediately see the delicious treats inside without needing to open every container. Transparent materials are essential whenever visibility is paramount.",
        "checkpoints": [
            {
                "question": "Which of the following is an example of a transparent medium?",
                "options": [
                    "Clean, filtered drinking water",
                    "A thick wooden plank",
                    "A solid sheet of cast iron",
                    "A piece of heavy cardboard"
                ],
                "correct": 0,
                "explanation": "Clean water allows light rays to pass freely without scattering, allowing objects submerged at the bottom of a pool or glass to be seen clearly.",
                "study_insight": "Transparent materials permit undisturbed light transmission."
            },
            {
                "question": "Why are car windshields made of transparent laminated safety glass rather than sheet metal or plywood?",
                "options": [
                    "Glass is much softer than plywood and bends easily in wind",
                    "Glass allows light to transmit freely, giving the driver an unobstructed view of the road ahead",
                    "Sheet metal is completely transparent in daytime",
                    "Plywood dissolves whenever it rains"
                ],
                "correct": 1,
                "explanation": "Safe navigation requires clear optical transmission; the driver must see road hazards, pedestrians, and signals without visual blockage.",
                "study_insight": "Transparency is mandatory wherever human safety depends on unimpeded vision."
            }
        ]
    },
    {
        "id": 11,
        "title": "Blocked Light",
        "subtitle": "Total Light Occlusion and the Nature of Opaque Materials",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Now, hold a heavy textbook or a wooden clipboard in front of your face. Can you see your friend sitting across the table? Not at all! Materials that block light completely are termed <strong class="text-rose-300 font-semibold">opaque</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-rose-400 uppercase tracking-wider">Definition: Opaque Materials</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Those materials through which you <strong class="text-white">cannot see at all</strong> because 0% of visible light can penetrate through their bulk structure; light is either fully reflected or absorbed.
                    </p>
                    <div class="grid grid-cols-2 gap-2 text-xs pt-1 text-slate-200">
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🪵 Solid Wood Planks</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">📦 Cardboard Cartons</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">⚙️ Sheet Metals & Iron</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🧱 Brick & Concrete Walls</div>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-200">
                    <strong class="text-white font-semibold">Shadow Connection:</strong> Because opaque objects block the rectilinear path of light rays completely, they cast sharp, dark <strong class="text-white">shadows</strong> on the surface behind them!
                </div>
            </div>
        """,
        "lecture_script": "Now consider the opposite optical behavior: opaque materials. When you place a thick piece of cardboard, a wooden door, or an iron sheet between your eyes and a bright lamp, the light cannot penetrate. Zero light passes through. Consequently, you cannot see anything situated behind an opaque barrier. Why do opaque materials behave this way? Their dense molecular structure either absorbs the light energy or bounces it back in reflection. This is why house walls and bedroom doors are built from opaque bricks and timber—to guarantee privacy and shelter. It is also the exact reason why shadows exist: when sunlight hits an opaque tree or building, the light rays cannot pass through, creating a dark silhouette on the ground directly behind.",
        "spoken_text": "Now consider the opposite optical behavior: opaque materials. When you place a thick piece of cardboard, a wooden door, or an iron sheet between your eyes and a bright lamp, the light cannot penetrate. Zero light passes through. Consequently, you cannot see anything situated behind an opaque barrier. Why do opaque materials behave this way? Their dense molecular structure either absorbs the light energy or bounces it back in reflection. This is why house walls and bedroom doors are built from opaque bricks and timber—to guarantee privacy and shelter. It is also the exact reason why shadows exist: when sunlight hits an opaque tree or building, the light rays cannot pass through, creating a dark silhouette on the ground directly behind.",
        "checkpoints": [
            {
                "question": "Which of the following objects is completely opaque?",
                "options": [
                    "A corrugated cardboard shipping box",
                    "A clear glass lens",
                    "A beaker of pure clean water",
                    "A thin sheet of clear cellophane"
                ],
                "correct": 0,
                "explanation": "Corrugated cardboard absorbs and reflects all visible light, preventing any optical transmission through its thickness.",
                "study_insight": "Opaque materials completely extinguish light transmission through their bulk."
            },
            {
                "question": "What optical phenomenon occurs behind an opaque object when placed directly in front of a point light source?",
                "options": [
                    "A bright glowing rainbow halo",
                    "A dark, sharp shadow region where light is blocked",
                    "The object turns completely transparent",
                    "The light speeds up to infinite velocity"
                ],
                "correct": 1,
                "explanation": "Because light travels in straight lines and cannot pass through opaque objects, an unlit shadow region forms on the surface behind.",
                "study_insight": "Opaque bodies form dark shadows due to the rectilinear propagation of light."
            }
        ]
    },
    {
        "id": 12,
        "title": "Hazy View",
        "subtitle": "Diffuse Light Scattering Through Translucent Materials",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    What happens when a material allows some light to pass through, but scatters the rays in chaotic directions? You get a blurred, hazy view! Such materials are classified as <strong class="text-amber-300 font-semibold">translucent</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Definition: Translucent Materials</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Materials through which objects can be seen, but <strong class="text-white">not clearly or sharply</strong> (partial, scattered light transmission).
                    </p>
                    <div class="grid grid-cols-2 gap-2 text-xs pt-1 text-slate-200">
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🧈 Butter / Wax Paper</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🌫️ Frosted / Ground Glass</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🧻 Thin Tissue Paper</div>
                        <div class="p-2 rounded bg-slate-800 border border-slate-700">🛢️ Oily Paper Patch</div>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-white font-semibold">Classic Oil Spot Test:</strong> If a drop of edible oil falls onto ordinary white writing paper, that oily patch immediately becomes translucent! Hold it up to a light bulb, and the filament becomes dimly visible through the patch.
                </div>
            </div>
        """,
        "lecture_script": "Between perfectly clear transparent glass and pitch-black opaque cardboard lies a fascinating middle category: translucent materials. Take a sheet of ordinary tracing paper, butter paper, or frosted bathroom glass. If you hold it up to a bright bulb, plenty of light passes through—the room brightens. But try reading the text in a book placed behind that butter paper. The letters blur into an unrecognizable fuzzy smudge! Light penetrates, but its straight-line path is scrambled by internal micro-crystals or rough surface textures. Translucent materials are brilliantly used in privacy windows, lampshades, and decorative panels. They let natural daylight flood into a bathroom or clinic without letting anyone on the outside see inside. You can test this yourself: a single drop of mustard oil on white writing paper turns the opaque paper into a translucent patch.",
        "spoken_text": "Between perfectly clear transparent glass and pitch-black opaque cardboard lies a fascinating middle category: translucent materials. Take a sheet of ordinary tracing paper, butter paper, or frosted bathroom glass. If you hold it up to a bright bulb, plenty of light passes through—the room brightens. But try reading the text in a book placed behind that butter paper. The letters blur into an unrecognizable fuzzy smudge! Light penetrates, but its straight-line path is scrambled by internal micro-crystals or rough surface textures. Translucent materials are brilliantly used in privacy windows, lampshades, and decorative panels. They let natural daylight flood into a bathroom or clinic without letting anyone on the outside see inside. You can test this yourself: a single drop of mustard oil on white writing paper turns the opaque paper into a translucent patch.",
        "checkpoints": [
            {
                "question": "Which of the following materials is translucent?",
                "options": [
                    "Frosted bathroom window glass",
                    "A crystal clear glass lens",
                    "A solid block of stainless steel",
                    "Pure distilled laboratory water"
                ],
                "correct": 0,
                "explanation": "Frosted glass transmits diffused light while scattering the rays, preventing clear visibility of shapes on the other side.",
                "study_insight": "Translucent media provide diffused illumination while preserving visual privacy."
            },
            {
                "question": "What happens when a small drop of cooking oil is rubbed onto a piece of plain white opaque paper?",
                "options": [
                    "The paper transforms into magnetic iron",
                    "The oily patch becomes translucent, allowing a dim view of light through it",
                    "The paper evaporates into smoke within one second",
                    "The paper becomes 100% crystal transparent like high-grade optical glass"
                ],
                "correct": 1,
                "explanation": "Oil fills the microscopic air voids between cellulose fibers, matching refractive indices enough to transmit scattered light, creating a translucent patch.",
                "study_insight": "The oil-spot test illustrates how altering internal optical scattering changes transparency."
            }
        ]
    },
    {
        "id": 13,
        "title": "Water Solubility",
        "subtitle": "Dissolution of Solids in Water: Soluble vs Insoluble Substances",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Water is known as the <strong class="text-cyan-300 font-semibold">universal solvent</strong> because it can dissolve an extraordinarily wide variety of substances. Let us test what happens when different solid powders are stirred into water.
                </p>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-emerald-400 block mb-1">Soluble Substances</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            Substances that <strong class="text-white">completely disappear</strong> in water, breaking down into individual ions or molecules to form a clear, homogeneous solution (e.g., table salt, sugar, copper sulphate).
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-rose-400 block mb-1">Insoluble Substances</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            Substances that <strong class="text-white">do not dissolve</strong> even after prolonged stirring. They remain suspended or settle at the bottom as sediment (e.g., sand, chalk powder, sawdust, charcoal).
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 space-y-1">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">The Microscopic Reality</h4>
                    <p class="leading-relaxed">
                        When sugar dissolves, it does not vanish from existence! Polar water molecules surround individual sugar molecules, pulling them into the intermolecular spaces. The sweet taste throughout the entire solution proves the sugar is fully present.
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us investigate how materials interact with water. Take a glass of clean water and add a teaspoon of common salt or cane sugar. Stir it vigorously for thirty seconds. What do you see? The white crystals disappear completely! The liquid remains clear. When a substance dissolves completely into water and breaks down so finely that its particles cannot be seen even under a microscope, we call it soluble. But what if you stir a spoonful of fine river sand, chalk powder, or wood sawdust into the water? Even after stirring for ten minutes, the sand particles swirl around and eventually settle onto the bottom as a heavy layer of sediment. Substances that do not dissolve in water are called insoluble. The solubility of materials is crucial for biological life: nutrients, minerals, and medicines must dissolve in our watery blood to be absorbed by our body cells.",
        "spoken_text": "Let us investigate how materials interact with water. Take a glass of clean water and add a teaspoon of common salt or cane sugar. Stir it vigorously for thirty seconds. What do you see? The white crystals disappear completely! The liquid remains clear. When a substance dissolves completely into water and breaks down so finely that its particles cannot be seen even under a microscope, we call it soluble. But what if you stir a spoonful of fine river sand, chalk powder, or wood sawdust into the water? Even after stirring for ten minutes, the sand particles swirl around and eventually settle onto the bottom as a heavy layer of sediment. Substances that do not dissolve in water are called insoluble. The solubility of materials is crucial for biological life: nutrients, minerals, and medicines must dissolve in our watery blood to be absorbed by our body cells.",
        "checkpoints": [
            {
                "question": "Which of the following substances will completely dissolve when thoroughly stirred in a glass of water?",
                "options": [
                    "Refined cane sugar crystals",
                    "Granite rock gravel",
                    "Wood sawdust",
                    "Plastic micro-beads"
                ],
                "correct": 0,
                "explanation": "Cane sugar (sucrose) is highly polar and forms hydrogen bonds with water molecules, dissolving completely into a clear solution.",
                "study_insight": "Sugar and table salt are quintessential soluble solids in everyday science."
            },
            {
                "question": "When chalk powder is stirred into water, the liquid turns cloudy white, and after standing undisturbed, a white layer forms at the bottom. This proves that chalk powder is:",
                "options": [
                    "Completely soluble in water",
                    "Insoluble in water",
                    "A transparent gas",
                    "A magnetic metallic element"
                ],
                "correct": 1,
                "explanation": "Chalk powder (calcium carbonate) does not dissolve; its insoluble solid particles remain in temporary suspension and eventually sediment out.",
                "study_insight": "Sedimentation of particles after resting confirms insolubility."
            }
        ]
    },
    {
        "id": 14,
        "title": "Liquid & Gas Mix",
        "subtitle": "Miscibility of Liquids, Dissolved Gases, and Life-Saving ORS",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Solubility is not limited to solid powders! Liquids and gases also exhibit distinct solubility behaviors in water that are vital for technology and planetary life.
                </p>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-emerald-400 block mb-1">Miscible Liquids</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            Liquids that <strong class="text-white">mix completely</strong> and uniformly with water in all proportions (e.g., vinegar, lemon juice, milk, alcohol).
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-rose-400 block mb-1">Immiscible Liquids</span>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            Liquids that <strong class="text-white">do not mix</strong>; they separate into distinct layers on standing (e.g., mustard oil, kerosene, diesel, coconut oil).
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-cyan-300 uppercase tracking-wider">Dissolved Gases & ORS</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Life Science</span>
                    </div>
                    <p class="text-slate-300 leading-relaxed">
                        • <strong class="text-white">Dissolved Oxygen (DO):</strong> Oxygen gas dissolves slightly in water (about 8-10 mg/L). Without this dissolved gas, fish, crabs, and aquatic plants would suffocate and die!
                    </p>
                    <p class="text-slate-300 leading-relaxed">
                        • <strong class="text-white">ORS (Oral Rehydration Solution):</strong> A life-saving electrolyte drink made by dissolving clean water, sugar (energy/glucose), and salt (sodium ions) to stop fatal dehydration during diarrhea.
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Now, let us examine how liquids and gases behave in water. If you pour a spoonful of vinegar or fresh lemon juice into water, it mixes seamlessly into a single uniform liquid. We call such liquids miscible. But what happens if you pour mustard oil, coconut oil, or kerosene into water? The oil beads up, rises to the top, and forms an unmistakable separate floating layer! Oil and water are immiscible; they refuse to mix. Even more remarkable is the behavior of gases. You might think water contains only liquids, but gases dissolve in it too! Gaseous oxygen dissolves into ponds, lakes, and oceans. Fish use their gills to extract this dissolved oxygen directly from water to breathe. Furthermore, understanding solubility saves millions of human lives through Oral Rehydration Solution, or ORS. By dissolving precise ratios of sugar and common salt in clean drinking water, we create an electrolyte solution that saves children from deadly dehydration.",
        "spoken_text": "Now, let us examine how liquids and gases behave in water. If you pour a spoonful of vinegar or fresh lemon juice into water, it mixes seamlessly into a single uniform liquid. We call such liquids miscible. But what happens if you pour mustard oil, coconut oil, or kerosene into water? The oil beads up, rises to the top, and forms an unmistakable separate floating layer! Oil and water are immiscible; they refuse to mix. Even more remarkable is the behavior of gases. You might think water contains only liquids, but gases dissolve in it too! Gaseous oxygen dissolves into ponds, lakes, and oceans. Fish use their gills to extract this dissolved oxygen directly from water to breathe. Furthermore, understanding solubility saves millions of human lives through Oral Rehydration Solution, or ORS. By dissolving precise ratios of sugar and common salt in clean drinking water, we create an electrolyte solution that saves children from deadly dehydration.",
        "checkpoints": [
            {
                "question": "What happens when vegetable cooking oil is poured into a beaker of water and vigorously stirred?",
                "options": [
                    "The oil dissolves completely and turns the water crystal clear",
                    "The oil and water do not mix; after resting, the oil floats on top in a separate layer",
                    "The oil instantly turns into solid ice at room temperature",
                    "The water evaporates instantly within one millisecond"
                ],
                "correct": 1,
                "explanation": "Cooking oil is non-polar and hydrophobic (immiscible with polar water); being less dense than water, it floats to form a distinct upper layer.",
                "study_insight": "Density differences and immiscibility cause oil to float on water."
            },
            {
                "question": "How do fish and other aquatic animals obtain the oxygen necessary for cellular respiration underwater?",
                "options": [
                    "They split liquid water into hydrogen and oxygen using nuclear reactors",
                    "They breathe oxygen gas that is naturally dissolved in water through their gills",
                    "They do not require any oxygen to stay alive",
                    "They leap out of the ocean every five seconds to inhale air"
                ],
                "correct": 1,
                "explanation": "Fish pass water over thin, capillary-rich gill filaments that absorb oxygen gas dissolved in the water.",
                "study_insight": "Dissolved gases in aquatic habitats are essential for supporting water-dwelling organisms."
            }
        ]
    },
    {
        "id": 15,
        "title": "Mass & Volume",
        "subtitle": "Quantifying the Heaviness of Matter and the Three-Dimensional Space It Occupies",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    Take two identical plastic cups. Fill Cup A with dry cotton wool and fill Cup B with garden sand or pebbles. Hold one in each hand. Even though both cups take up the exact same physical space, Cup B feels dramatically heavier! Why?
                </p>
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-amber-400 block mb-1">Mass (Quantity of Matter)</span>
                        <p class="text-slate-300 leading-relaxed">
                            <strong class="text-white">Mass</strong> quantifies how heavy or light an object is. It represents the total amount of matter packed inside. Measured in <strong class="text-amber-300">kilograms (kg)</strong> and <strong class="text-amber-300">grams (g)</strong> using a dual-pan beam balance.
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700">
                        <span class="font-bold text-sky-400 block mb-1">Volume (Occupied Space)</span>
                        <p class="text-slate-300 leading-relaxed">
                            <strong class="text-white">Volume</strong> is the three-dimensional space occupied by an object. Measured in <strong class="text-sky-300">cubic metres (m³)</strong> for solids, or <strong class="text-sky-300">litres (L)</strong> and <strong class="text-sky-300">millilitres (mL)</strong> for liquids.
                        </p>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 space-y-1">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Water Displacement Principle</h4>
                    <p class="leading-relaxed">
                        When an irregular stone pebble is submerged in a measuring cylinder filled with water, the water level rises. The volume of water pushed upward equals the exact physical volume of the stone!
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "Let us explore two fundamental physical quantities: mass and volume. Take two identical paper cups. Fill the first with fluffy cotton and the second with dense pebbles. Both occupy the identical three-dimensional volume, yet when you lift them, the cup of pebbles pulls down with far greater force. Why? Because the pebbles pack vastly more matter into that space! Mass is the physical property that quantifies how heavy an object is—it measures the actual quantity of matter contained within. We measure mass using a balance in kilograms and grams. Volume, on the other hand, measures the amount of three-dimensional space an object occupies. We measure the volume of liquids in litres and millilitres, or solid cubic metres. You can measure the volume of any irregular object—like a rock—by dropping it into a graduated cylinder of water and observing how many millilitres of water it displaces.",
        "spoken_text": "Let us explore two fundamental physical quantities: mass and volume. Take two identical paper cups. Fill the first with fluffy cotton and the second with dense pebbles. Both occupy the identical three-dimensional volume, yet when you lift them, the cup of pebbles pulls down with far greater force. Why? Because the pebbles pack vastly more matter into that space! Mass is the physical property that quantifies how heavy an object is—it measures the actual quantity of matter contained within. We measure mass using a balance in kilograms and grams. Volume, on the other hand, measures the amount of three-dimensional space an object occupies. We measure the volume of liquids in litres and millilitres, or solid cubic metres. You can measure the volume of any irregular object—like a rock—by dropping it into a graduated cylinder of water and observing how many millilitres of water it displaces.",
        "checkpoints": [
            {
                "question": "What is the standard metric SI unit used worldwide for measuring mass?",
                "options": [
                    "The kilogram (kg)",
                    "The metre (m)",
                    "The second (s)",
                    "The litre (L)"
                ],
                "correct": 0,
                "explanation": "The kilogram (kg) is the fundamental SI base unit of mass; smaller quantities are expressed in grams (g), where 1 kg = 1000 g.",
                "study_insight": "Mass is measured in kilograms (kg) and grams (g); volume is measured in litres (L) or cubic metres (m³)."
            },
            {
                "question": "If a stone dropped into a measuring cylinder causes the water level to rise from 50 mL to 75 mL, what is the volume of the stone?",
                "options": [
                    "125 mL",
                    "25 mL",
                    "50 mL",
                    "0 mL"
                ],
                "correct": 1,
                "explanation": "By Archimedes' principle, the volume of water displaced equals the volume of the submerged object: 75 mL - 50 mL = 25 mL.",
                "study_insight": "Water displacement allows exact measurement of irregular solid volume."
            }
        ]
    },
    {
        "id": 16,
        "title": "What is Matter",
        "subtitle": "The Universal Definition of Matter, Non-Matter, and Ancient Ayurvedic Gunas",
        "concept_html": """
            <div class="space-y-3">
                <p class="leading-relaxed">
                    We now arrive at the overarching grand concept uniting all materials: <strong class="text-indigo-300 font-semibold">Matter</strong>.
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider">The Golden Scientific Definition</h4>
                    <p class="text-sm font-bold text-white bg-slate-950 p-2.5 rounded-lg border border-slate-800 text-center">
                        Anything that occupies space and has mass is called <span class="text-emerald-400">Matter</span>.
                    </p>
                </div>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2.5 rounded-xl bg-emerald-950/30 border border-emerald-500/30">
                        <span class="font-bold text-emerald-300 block mb-1">Matter (Has Mass & Space)</span>
                        <span class="text-slate-300 text-[11px]">Water, air, rocks, iron nails, trees, books, milk, oxygen gas, human bodies.</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-rose-950/30 border border-rose-500/30">
                        <span class="font-bold text-rose-300 block mb-1">Non-Matter (No Mass/Space)</span>
                        <span class="text-slate-300 text-[11px]">Light rays, heat, sound waves, thoughts, friendship, love, shadows.</span>
                    </div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700 text-xs text-slate-300 space-y-1">
                    <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Ayurvedic Connection: Ashtanga Hridaya</h4>
                    <p class="leading-relaxed">
                        In ancient Indian science, the medical classic <em class="text-white">Ashtanga Hridaya</em> classified physical substances using <strong class="text-amber-300">20 opposite gunas (properties)</strong>: Heavy (Guru) vs Light (Laghu), Cold (Sheeta) vs Hot (Ushna), Oily (Snigdha) vs Dry (Ruksha), Soft (Mridu) vs Hard (Kathina).
                    </p>
                </div>
            </div>
        """,
        "lecture_script": "We have explored lustre, hardness, transparency, solubility, mass, and volume. Now, we unite all these observations under the master concept of physical science: what is matter? Scientists define matter with total precision: anything that occupies space and has mass is called matter. The desk you sit at is matter. The water you drink is matter. Even the invisible air filling your lungs is matter—it has mass and takes up volume inside an inflated balloon! But what is NOT matter? Sunlight shining through a window is not matter; it is radiant energy. The sound of a bird chirping is not matter; it is acoustic vibrational energy. Thoughts, feelings, memories, and shadows are not matter, because they occupy no physical volume and register zero mass on a balance. Interestingly, thousands of years ago, Indian medical thinkers in the Ashtanga Hridaya organized all physical substances using twenty fundamental dual properties, or gunas—such as heavy versus light, cold versus hot, and soft versus hard. This ancient framework anticipated modern material science.",
        "spoken_text": "We have explored lustre, hardness, transparency, solubility, mass, and volume. Now, we unite all these observations under the master concept of physical science: what is matter? Scientists define matter with total precision: anything that occupies space and has mass is called matter. The desk you sit at is matter. The water you drink is matter. Even the invisible air filling your lungs is matter—it has mass and takes up volume inside an inflated balloon! But what is NOT matter? Sunlight shining through a window is not matter; it is radiant energy. The sound of a bird chirping is not matter; it is acoustic vibrational energy. Thoughts, feelings, memories, and shadows are not matter, because they occupy no physical volume and register zero mass on a balance. Interestingly, thousands of years ago, Indian medical thinkers in the Ashtanga Hridaya organized all physical substances using twenty fundamental dual properties, or gunas—such as heavy versus light, cold versus hot, and soft versus hard. This ancient framework anticipated modern material science.",
        "checkpoints": [
            {
                "question": "According to physical science, which of the following is classified as MATTER?",
                "options": [
                    "Compressed atmospheric air inside an inflated bicycle tire",
                    "A warm thought about your best friend",
                    "The sound produced by ringing a school bell",
                    "The shadow cast by an umbrella on a sunny pavement"
                ],
                "correct": 0,
                "explanation": "Air has mass (an inflated tire weighs more than a deflated one) and occupies volume inside the tire tube; therefore, air is matter. Sound and shadows lack mass and physical volume.",
                "study_insight": "If it occupies volume and registers mass on a sensitive scale, it is matter."
            },
            {
                "question": "Which ancient Indian scientific treatise organized physical matter using 20 opposite fundamental properties (gunas), such as Guru/Laghu (heavy/light) and Mridu/Kathina (soft/hard)?",
                "options": [
                    "Ashtanga Hridaya",
                    "The Roman Legal Digest",
                    "The British Maritime Charter",
                    "The Parisian Metric Treaty"
                ],
                "correct": 0,
                "explanation": "The Ashtanga Hridaya, an authoritative classical Ayurvedic treatise, classified all physical medicines and foods using twenty paired fundamental properties (sharira gunas).",
                "study_insight": "India has a rich tradition of systematic physical taxonomy that mirrors modern material science."
            }
        ]
    }
]

# 40 High-Yield Mastery Assessment Questions across Slides 17 to 20
QUIZ_QUESTIONS = [
    # Slide 17: Questions 1 to 10 (Challenge 1)
    {
        "id": 1,
        "question": "Which of the following statements correctly distinguishes an 'object' from a 'material'?",
        "options": [
            "An object is a specific finished item, while a material is the substance used to create it",
            "An object is always a liquid, while a material is always a solid rock",
            "An object exists only in outer space, while a material exists only underground",
            "There is zero difference; the words are identical synonyms in physical science"
        ],
        "correct": 0,
        "explanation": "An object (e.g., a chair, a window) is a finished article defined by its shape and function. A material (e.g., wood, glass) is the substance from which the object is constructed.",
        "solution_html": "<strong>Conceptual Proof:</strong> An object is defined by form and utility (e.g., a bucket). A material is the physical substance of composition (e.g., plastic or galvanized iron)."
    },
    {
        "id": 2,
        "question": "Which of the following objects is typically constructed by assembling MULTIPLE distinct materials?",
        "options": [
            "A standard ballpoint pen with plastic barrel, steel spring, and brass ball tip",
            "A solid single block of pure unworked sandstone",
            "A seamless drop of pure liquid mercury",
            "A single diamond gemstone crystal"
        ],
        "correct": 0,
        "explanation": "A ballpoint pen combines molded plastic for its casing, hardened tungsten carbide or brass for its writing ball, stainless steel for its spring and clip, and oil-based solvent ink.",
        "solution_html": "<strong>Assembly Analysis:</strong> Many everyday tools leverage composite multi-material construction to utilize different physical properties for different sub-components."
    },
    {
        "id": 3,
        "question": "Ancient pottery discovered at Lahuradewa and Mehrgarh demonstrates that early Indian craftspeople learned to transform raw clay into terracotta by:",
        "options": [
            "Freezing wet mud in glacier caves",
            "Firing shaped clay in high-temperature kilns to induce permanent hardening",
            "Dissolving the clay in concentrated mustard oil",
            "Sprinkling powdered copper on riverbanks"
        ],
        "correct": 1,
        "explanation": "Pottery kilns reaching 600°C–1000°C permanently alter the silicate structure of clay, driving out moisture and converting malleable mud into rock-hard, waterproof terracotta.",
        "solution_html": "<strong>Thermal Transformation:</strong> Kiln pyrotechnology irreversibly vitrifies clay particles, yielding durable, water-resistant ceramic artifacts."
    },
    {
        "id": 4,
        "question": "Which material would be completely UNFIT for manufacturing a cooking pan intended for frying on a gas stove?",
        "options": [
            "Cast iron",
            "Aluminium alloy",
            "Waxed paper cardboard",
            "Stainless steel"
        ],
        "correct": 2,
        "explanation": "Cardboard has an ignition temperature far below cooking flame levels; it catches fire rapidly and lacks the thermal conductivity and durability needed for frying.",
        "solution_html": "<strong>Material Suitability:</strong> Cooking vessels require high thermal tolerance and non-flammability, making metals ideal and paper/wax utterly inappropriate."
    },
    {
        "id": 5,
        "question": "Why can a drinking tumbler be successfully manufactured from stainless steel, glass, or plastic, but NOT from woven cotton fabric?",
        "options": [
            "Cotton fabric is too shiny to hold in hand",
            "Cotton fabric is porous and cannot contain liquid without leaking immediately",
            "Cotton fabric turns all drinking water into solid rock",
            "Cotton fabric is magnetic and repels pure water"
        ],
        "correct": 1,
        "explanation": "A container for liquids must be non-porous and impermeable. Woven cotton contains millions of microscopic gaps between fibers through which liquid flows freely.",
        "solution_html": "<strong>Functional Requirement:</strong> Liquid containment demands impermeable walls; porous cloth lacks liquid-tight structural integrity."
    },
    {
        "id": 6,
        "question": "Which of the following properties is shared by gold, copper, aluminium, and silver?",
        "options": [
            "They are completely soluble in cold water",
            "They exhibit characteristic metallic lustre on freshly cut or polished surfaces",
            "They are naturally transparent to visible light",
            "They crumble into soft powder when touched with a finger"
        ],
        "correct": 1,
        "explanation": "Gold, copper, aluminium, and silver are metals; metals naturally possess metallic lustre, reflecting light from their dense, free-electron atomic structures.",
        "solution_html": "<strong>Metallic Trait:</strong> Lustre (specular reflectivity) is an intrinsic physical characteristic of metallic elements and alloys."
    },
    {
        "id": 7,
        "question": "Why does a piece of freshly cut iron shine brightly, whereas an iron bridge girder exposed to monsoon weather appears dull reddish-brown?",
        "options": [
            "The iron girder permanently converts into tree wood",
            "The outer surface of the iron reacts with moist atmospheric oxygen to form a dull layer of rust",
            "The iron girder loses its gravitational mass",
            "The iron girder becomes completely transparent under sunlight"
        ],
        "correct": 1,
        "explanation": "Atmospheric moisture and oxygen cause oxidation, forming hydrated iron(III) oxide (rust). This dull corrosion layer covers the metal, masking its true lustre.",
        "solution_html": "<strong>Surface Oxidation:</strong> Rusting dulls metallic surfaces; slicing or sandpapering removes the oxide film to reveal pristine metallic lustre."
    },
    {
        "id": 8,
        "question": "A dining table made of teak wood shines under chandelier lighting. Why is this shine NOT classified as true metallic lustre?",
        "options": [
            "Because wood is actually a liquid metal",
            "Because the shine is caused by a cosmetic outer layer of chemical varnish or lacquer, not by the wood itself",
            "Because the table is vibrating at high frequencies",
            "Because chandelier light changes wood into solid gold"
        ],
        "correct": 1,
        "explanation": "Wood is naturally non-lustrous; its cellular grain scatters light diffusely. The shine comes exclusively from the smooth, synthetic resin varnish coating.",
        "solution_html": "<strong>True vs Artificial Shine:</strong> True lustre is an intrinsic property of the bulk substance. Cutting the wood reveals a dull, fibrous non-lustrous interior."
    },
    {
        "id": 9,
        "question": "A student attempts to scratch three materials with an iron nail. The nail easily scratches a wax candle and a wooden ruler, but fails to make any mark on a glass slide. What can be concluded?",
        "options": [
            "Wax is harder than Glass",
            "Wood is the hardest of all three",
            "Glass is harder than the iron nail, while wax and wood are softer than the iron nail",
            "The iron nail is made of soft cotton"
        ],
        "correct": 2,
        "explanation": "A material scratches softer substances but cannot scratch harder ones. Since the iron nail scratches wax and wood, it is harder than them. Since it cannot scratch glass, glass is harder than iron.",
        "solution_html": "<strong>Relative Hardness Derivation:</strong> Hardness hierarchy: Glass > Iron Nail > Wood > Wax Candle."
    },
    {
        "id": 10,
        "question": "Which of the following lists contains only materials that are CLASSIFIED AS SOFT (easily compressed or scratched)?",
        "options": [
            "Iron rod, granite stone, ceramic tile",
            "Bath sponge, cotton wool, candle wax, rubber eraser",
            "Diamond crystal, steel needle, copper coin",
            "Brick block, concrete pillar, glass marble"
        ],
        "correct": 1,
        "explanation": "Foam sponges, cotton balls, paraffin wax, and soft rubber erasers yield readily to finger pressure or fingernail scratches, classifying them as soft.",
        "solution_html": "<strong>Compressibility Criteria:</strong> Soft substances possess low compressive resistance and yield easily to manual deformation."
    },

    # Slide 18: Questions 11 to 20 (Challenge 2)
    {
        "id": 11,
        "question": "Why are eyeglasses, microscope lenses, and aquarium walls manufactured from high-grade transparent glass or acrylic?",
        "options": [
            "Because they absorb 100% of visible light and turn black",
            "Because they transmit light clearly in straight paths, allowing sharp, unobstructed vision of objects behind them",
            "Because transparent materials are the heaviest substances known to science",
            "Because they bend all light rays into pure darkness"
        ],
        "correct": 1,
        "explanation": "Transparent materials permit parallel light transmission with minimal scattering or absorption, delivering crisp optical images to the viewer.",
        "solution_html": "<strong>Optical Transmission:</strong> Transparency allows undisturbed light propagation, essential for precision lenses, aquariums, and corrective spectacles."
    },
    {
        "id": 12,
        "question": "Which of the following objects is OPAQUE?",
        "options": [
            "A clean glass microscope slide",
            "A container of pure distilled water",
            "A sheet of steel metal plate",
            "A thin layer of invisible atmospheric air"
        ],
        "correct": 2,
        "explanation": "Metals completely reflect or absorb visible light; zero light penetrates through a steel sheet, making it completely opaque.",
        "solution_html": "<strong>Occlusion Test:</strong> Opaque objects block 100% of incident light, preventing vision of anything positioned on the opposite side."
    },
    {
        "id": 13,
        "question": "You can see that someone is standing behind a frosted bathroom door, but you cannot recognize who it is or make out any facial features. This proves that frosted glass is:",
        "options": [
            "Transparent",
            "Translucent",
            "Completely Opaque",
            "A superconductor"
        ],
        "correct": 1,
        "explanation": "Translucent materials allow light to pass through but scatter the rays randomly, making objects visible only as indistinct, blurry outlines.",
        "solution_html": "<strong>Translucency Signature:</strong> Light transmits diffusely, illuminating the space while destroying sharp image resolution."
    },
    {
        "id": 14,
        "question": "A drop of groundnut cooking oil falls onto a white paper envelope. When the oily patch is held against a lamp, what optical change is observed?",
        "options": [
            "The patch becomes magnetic and attracts paper clips",
            "The patch becomes translucent, dimly transmitting light through the paper fibers",
            "The patch turns into pure diamond",
            "The paper catches fire instantly at room temperature"
        ],
        "correct": 1,
        "explanation": "The oil penetrates the porous paper, reducing the refractive index mismatch between cellulose fibers and air, allowing partial, scattered light transmission (translucency).",
        "solution_html": "<strong>The Oil-Spot Test:</strong> Oil reduces internal optical reflections in paper, converting opaque cellulose into a translucent diffuse light transmitter."
    },
    {
        "id": 15,
        "question": "When a teaspoon of common table salt is stirred into a beaker of pure water, what happens to the salt crystals?",
        "options": [
            "They permanently vanish from the universe",
            "They dissolve completely, separating into individual ions dispersed evenly throughout the water",
            "They float on top of the water like cork wood",
            "They turn into bright green gas bubbles"
        ],
        "correct": 1,
        "explanation": "Sodium chloride (salt) is highly soluble in polar water; its ionic lattice dissociates, and the ions become solvated, forming a homogeneous solution.",
        "solution_html": "<strong>Solubility Mechanism:</strong> Soluble solutes dissociate into microscopic particles that intersperse evenly among water molecules without settling."
    },
    {
        "id": 16,
        "question": "Which of the following solid powders is INSOLUBLE in water?",
        "options": [
            "Cane sugar powder",
            "Fine river sand",
            "Common table salt",
            "Copper sulphate crystals"
        ],
        "correct": 1,
        "explanation": "River sand is primarily silicon dioxide (silica), which has strong covalent network bonds that water cannot break; it remains undissolved as sediment.",
        "solution_html": "<strong>Insolubility Analysis:</strong> Silica sand does not dissolve in water; it remains suspended during agitation and precipitates to the beaker floor upon standing."
    },
    {
        "id": 17,
        "question": "Liquids that blend together completely and uniformly in any proportion, like water and lemon juice, are described as:",
        "options": [
            "Immiscible",
            "Miscible",
            "Opaque solids",
            "Gaseous vapours"
        ],
        "correct": 1,
        "explanation": "Miscible liquids dissolve completely in each other to form a single, uniform liquid phase.",
        "solution_html": "<strong>Miscibility Definition:</strong> Two liquids that form a single homogeneous solution upon mixing are miscible (e.g., vinegar + water)."
    },
    {
        "id": 18,
        "question": "When kerosene oil or mustard oil is shaken vigorously with water in a test tube and then allowed to stand undisturbed for five minutes:",
        "options": [
            "The oil completely dissolves into a crystal clear solution",
            "The oil separates and forms a distinct floating layer on top of the water",
            "The water turns into pure solid copper metal",
            "The test tube shatters from nuclear energy"
        ],
        "correct": 1,
        "explanation": "Oils are non-polar hydrocarbons that do not dissolve in polar water (immiscible). Being less dense than water, the oil floats to form a separate top layer.",
        "solution_html": "<strong>Immiscibility & Density:</strong> Non-polar oil molecules are repelled by hydrogen-bonded water networks; lower density forces the oil to the surface."
    },
    {
        "id": 19,
        "question": "Why is the presence of DISSOLVED OXYGEN in natural water bodies essential for the biosphere?",
        "options": [
            "It prevents rivers from flowing downhill",
            "It allows fish, prawns, and aquatic organisms to perform cellular respiration through their gills",
            "It turns river water into solid concrete",
            "It stops sunlight from entering the water"
        ],
        "correct": 1,
        "explanation": "Aquatic animals rely on oxygen gas dissolved in water. Gills extract this dissolved oxygen to sustain life.",
        "solution_html": "<strong>Ecological Role of Dissolved Gases:</strong> Without dissolved oxygen (DO), aquatic fauna would suffocate and marine ecosystems would collapse."
    },
    {
        "id": 20,
        "question": "What are the core components used to prepare life-saving Oral Rehydration Solution (ORS)?",
        "options": [
            "Clean drinking water, a precise amount of sugar (glucose), and a pinch of salt (sodium chloride)",
            "Boiling mustard oil, sand, and chalk powder",
            "Pure kerosene, mercury, and crushed glass",
            "Vinegar, iron filings, and cement powder"
        ],
        "correct": 0,
        "explanation": "ORS is a medical electrolyte solution made of clean water, sugar (to provide metabolic energy and facilitate sodium transport), and salt to restore lost bodily electrolytes.",
        "solution_html": "<strong>ORS Physiology:</strong> Intestinal cotransporters absorb sodium and water rapidly in the presence of glucose, reversing fatal dehydration."
    },

    # Slide 19: Questions 21 to 30 (Challenge 3)
    {
        "id": 21,
        "question": "Two identical plastic tumblers are placed on a table. Tumbler X is filled with dry cotton balls, while Tumbler Y is filled with lead shot pellets. What can be observed?",
        "options": [
            "Both tumblers have identical mass and identical volume",
            "Both tumblers occupy equal volume, but Tumbler Y has vastly greater mass than Tumbler X",
            "Tumbler X has greater mass because cotton is white",
            "Neither tumbler occupies any space"
        ],
        "correct": 1,
        "explanation": "Because both tumblers have the same internal capacity, the volumes are equal. However, lead is vastly denser than fluffy cotton, packing much more matter into that volume.",
        "solution_html": "<strong>Mass vs Volume:</strong> Equal volume does not imply equal mass. Denser substances pack more matter into identical space."
    },
    {
        "id": 22,
        "question": "What is the physical property that quantifies the AMOUNT OF MATTER present in an object?",
        "options": [
            "Mass",
            "Lustre",
            "Transparency",
            "Solubility"
        ],
        "correct": 0,
        "explanation": "Mass is the measure of the quantity of matter contained within a physical body, typically measured in kilograms or grams.",
        "solution_html": "<strong>Definition of Mass:</strong> Mass represents the total quantity of material matter comprising an object and remains constant regardless of shape."
    },
    {
        "id": 23,
        "question": "What is the term for the THREE-DIMENSIONAL SPACE occupied by a physical body?",
        "options": [
            "Mass",
            "Volume",
            "Hardness",
            "Miscibility"
        ],
        "correct": 1,
        "explanation": "Volume is the quantity of three-dimensional space enclosed by a boundary or occupied by a substance.",
        "solution_html": "<strong>Definition of Volume:</strong> Measured in cubic metres (m³), litres (L), or millilitres (mL), volume quantifies spatial occupancy."
    },
    {
        "id": 24,
        "question": "A student pours 40 mL of water into a graduated cylinder. After gently sliding in an irregular iron bolt, the water level climbs to 62 mL. What is the volume of the iron bolt?",
        "options": [
            "102 mL",
            "22 mL",
            "40 mL",
            "62 mL"
        ],
        "correct": 1,
        "explanation": "The volume of an irregular solid equals the volume of liquid it displaces: 62 mL - 40 mL = 22 mL.",
        "solution_html": "<strong>Displacement Calculation:</strong> Displaced Volume = Final Volume - Initial Volume = 62 mL - 40 mL = 22 mL (or 22 cm³)."
    },
    {
        "id": 25,
        "question": "Which of the following satisfies the universal scientific definition of MATTER?",
        "options": [
            "A glass of tap water",
            "A beam of sunlight from a torch",
            "The emotion of happiness",
            "The shadow of a tall banyan tree"
        ],
        "correct": 0,
        "explanation": "Water has measurable mass and occupies volume (space) in a container; hence it is matter. Sunlight is energy, happiness is an emotion, and a shadow is the absence of light.",
        "solution_html": "<strong>Criteria for Matter:</strong> Matter must possess both mass and spatial volume. Tap water has both; energy and mental states have neither."
    },
    {
        "id": 26,
        "question": "Why is invisible atmospheric AIR classified as matter, even though we cannot see it with our eyes?",
        "options": [
            "Because air turns into solid stone at noon",
            "Because air has measurable mass (an inflated football weighs more than a deflated one) and occupies volume",
            "Because air is made of pure liquid gold",
            "Air is actually not matter; science classifies air as an emotion"
        ],
        "correct": 1,
        "explanation": "Air consists of gaseous molecules (nitrogen, oxygen, argon, carbon dioxide) that have mass and fill three-dimensional space inside containers and balloons.",
        "solution_html": "<strong>Air as Matter:</strong> Pumping air into a tire or balloon increases its total weight and expands its volume, proving that air has mass and occupies space."
    },
    {
        "id": 27,
        "question": "Which of the following entities is NOT matter?",
        "options": [
            "An iron padlock",
            "A cloud of steam",
            "The sound wave produced by a guitar string",
            "A teaspoon of table salt"
        ],
        "correct": 2,
        "explanation": "Sound is acoustic mechanical energy propagating as pressure waves through a medium; it has no resting mass and occupies no physical volume.",
        "solution_html": "<strong>Energy vs Matter:</strong> Sound, light, heat, and gravity are forms of energy or force interactions, not material matter."
    },
    {
        "id": 28,
        "question": "In the classical Ayurvedic medical treatise Ashtanga Hridaya, matter is categorized using how many opposite physical properties (gunas)?",
        "options": [
            "20 opposite gunas (properties arranged in 10 dual pairs)",
            "Only 1 single property",
            "Exactly 1,000,000 random traits",
            "Zero properties"
        ],
        "correct": 0,
        "explanation": "Ashtanga Hridaya describes 20 sharira gunas organized in 10 opposing pairs: Heavy/Light (Guru/Laghu), Cold/Hot (Sheeta/Ushna), Soft/Hard (Mridu/Kathina), etc.",
        "solution_html": "<strong>Classical Taxonomy:</strong> Ancient Indian physical philosophy cataloged all material substances using twenty fundamental dual qualitative attributes."
    },
    {
        "id": 29,
        "question": "Which of the following represents a correct pair of opposite gunas described in ancient Indian material science?",
        "options": [
            "Guru (Heavy) and Laghu (Light)",
            "Solid and Elephant",
            "Cold and Green",
            "Lustrous and Musical"
        ],
        "correct": 0,
        "explanation": "Guru (heavy) and Laghu (light) form one of the fundamental opposing pairs of physical qualities in classical Indian categorization.",
        "solution_html": "<strong>Ayurvedic Gunas:</strong> The 10 dual pairs juxtapose opposite physical behaviors, including heavy/light, hot/cold, and mobile/stable."
    },
    {
        "id": 30,
        "question": "What is the correct SI rule for writing the symbol for kilograms when expressing mass in scientific notation?",
        "options": [
            "Always write 'kgs.' with a plural s and a period",
            "Write lowercase 'kg' with a space after the numerical value (e.g., '5 kg')",
            "Write uppercase 'KG' in bold italics",
            "Write 'KiloGrams' with mixed capitals"
        ],
        "correct": 1,
        "explanation": "International SI rules stipulate: unit symbols are lowercase (unless named after a person), never take a plural 's', and have a space between the number and unit.",
        "solution_html": "<strong>SI Grammar Standards:</strong> '5 kg' is correct. '5kgs', '5 KG', or '5kg.' violate international metrological standards."
    },

    # Slide 20: Questions 31 to 40 (Challenge 4)
    {
        "id": 31,
        "question": "A shopkeeper organizes goods by grouping lentils together, toilet soaps on a separate rack, and cooking oils on another shelf. This is a practical example of:",
        "options": [
            "Classification",
            "Combustion",
            "Evaporation",
            "Rusting"
        ],
        "correct": 0,
        "explanation": "Arranging items into distinct categories based on shared function and material properties is classification.",
        "solution_html": "<strong>Classification in Commerce:</strong> Systematic grouping facilitates inventory tracking, customer retrieval, and organized storage."
    },
    {
        "id": 32,
        "question": "Which of the following objects can be fashioned from WOOD, PLASTIC, or METAL?",
        "options": [
            "A dining chair",
            "A cotton handkerchief",
            "A wool sweater",
            "A glass window lens"
        ],
        "correct": 0,
        "explanation": "Chairs are manufactured out of molded plastic, carved timber, or welded metal tubes (such as steel or aluminium).",
        "solution_html": "<strong>Material Versatility:</strong> Furniture design permits diverse material execution while preserving the underlying functional object geometry."
    },
    {
        "id": 33,
        "question": "Why are electrical wires manufactured with a copper core covered by an outer layer of PVC plastic?",
        "options": [
            "Copper conducts electricity efficiently, while the plastic coating acts as an insulator to prevent electric shocks",
            "Plastic conducts electricity, while copper is used only for decoration",
            "Copper is transparent so you can watch electrons flowing",
            "Plastic is heavier than copper and anchors the wire to the floor"
        ],
        "correct": 0,
        "explanation": "Copper has high electrical conductivity, allowing electric current to flow with low resistance. Plastic has high electrical resistance, insulating users from shocks.",
        "solution_html": "<strong>Conductor-Insulator Pairing:</strong> Safe electrical engineering couples conductive metallic cores with protective insulating polymer sheaths."
    },
    {
        "id": 34,
        "question": "A student drops an iron key, a wooden cork, and a lead sinker into a tub of water. What happens?",
        "options": [
            "The wooden cork floats because it is less dense than water, while the iron key and lead sinker sink",
            "All three objects float high in the air above the water",
            "All three objects instantly dissolve like sugar",
            "The water turns into pure kerosene"
        ],
        "correct": 0,
        "explanation": "Substances denser than water (iron and lead) sink; substances less dense than water (wooden cork) float on the surface.",
        "solution_html": "<strong>Flotation Criterion:</strong> An object floats if its overall density is less than the density of the surrounding liquid medium."
    },
    {
        "id": 35,
        "question": "Which of the following sets consists ENTIRELY of materials that DO NOT dissolve in water (insoluble)?",
        "options": [
            "Sawdust, sand, stone pebbles, chalk powder",
            "Sugar, common salt, honey, milk",
            "Lemon juice, vinegar, salt, alcohol",
            "Glucose powder, copper sulphate, baking soda, salt"
        ],
        "correct": 0,
        "explanation": "Wood sawdust, silica sand, mineral stones, and chalk powder are all insoluble in water and will settle out or remain suspended.",
        "solution_html": "<strong>Insoluble Group:</strong> None of these four materials dissolve in water; they all maintain distinct solid particulate phases."
    },
    {
        "id": 36,
        "question": "A student claims: 'A shadow is matter because it is very large and dark.' How should a science teacher respond?",
        "options": [
            "Agree completely, because shadows can be stored in bottles",
            "Correct the student: a shadow has zero mass and occupies no physical volume; it is merely an area of blocked light",
            "Tell the student that shadows are living animals",
            "Say that shadows are made of solid iron"
        ],
        "correct": 1,
        "explanation": "A shadow is an optical silhouette resulting from the blockage of light rays by an opaque body. It contains no matter, has zero mass, and occupies no physical volume.",
        "solution_html": "<strong>Shadows are Non-Matter:</strong> An absence of light has no molecular composition, no gravitational mass, and cannot be captured or weighed."
    },
    {
        "id": 37,
        "question": "Which of the following materials is BOTH hard and transparent?",
        "options": [
            "Tempered sheet glass",
            "Soft sponge",
            "Wax candle",
            "Cardboard sheet"
        ],
        "correct": 0,
        "explanation": "Tempered glass is difficult to scratch or compress (hard) and transmits parallel light clearly (transparent).",
        "solution_html": "<strong>Cross-Property Identification:</strong> Glass uniquely combines high mechanical surface hardness with exceptional optical transparency."
    },
    {
        "id": 38,
        "question": "Why is an ordinary unglazed earthen pot (matka) effective for keeping water cool during hot Indian summers?",
        "options": [
            "The clay produces cold ice cubes internally using nuclear cooling",
            "The microscopic pores in the baked clay allow water to seep out slowly and evaporate, drawing heat away from the pot",
            "Clay reflects 100% of all gravitational radiation",
            "Clay converts water into liquid nitrogen"
        ],
        "correct": 1,
        "explanation": "Porous terracotta permits tiny amounts of water to reach the outer surface. Evaporating water absorbs latent heat from the pot, cooling the stored water inside.",
        "solution_html": "<strong>Evaporative Cooling:</strong> Latent heat of vaporization drawn from the clay container cools the remaining liquid naturally."
    },
    {
        "id": 39,
        "question": "Which of the following units is used specifically to measure the VOLUME of liquids in everyday life?",
        "options": [
            "Litre (L) and millilitre (mL)",
            "Kilogram (kg)",
            "Metre (m)",
            "Second (s)"
        ],
        "correct": 0,
        "explanation": "Litres (L) and millilitres (mL) are standard metric capacity units for measuring liquid volumes (where 1 L = 1000 mL = 0.001 m³).",
        "solution_html": "<strong>Liquid Volume Units:</strong> Litres and millilitres quantify fluid spatial volume."
    },
    {
        "id": 40,
        "question": "What is the primary scientific reason for classifying and studying materials based on their properties?",
        "options": [
            "To understand the material world, predict behaviors, and select the right material for every practical engineering purpose",
            "To eliminate all physical matter from planet Earth",
            "To prove that all objects in the universe are made of plastic",
            "To stop time from flowing forward"
        ],
        "correct": 0,
        "explanation": "Understanding properties allows systematic taxonomy, predicts how materials will perform under stress, and guides the design of tools, clothing, and structures.",
        "solution_html": "<strong>The Goal of Material Science:</strong> Matching material properties to human and technological needs is the cornerstone of scientific progress."
    }
]


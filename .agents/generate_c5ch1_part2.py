"""
Part 2 Generator for NCERT Class 5 Science - Chapter 1: Water - The Essence of Life
Slides 9 to 16:
- Short punchy headings (1-3 words)
- Subtitles
- Rich concept HTML
- Spoken text (Classroom lecture, Indian English narration, NO lecturer names)
- 2 formative checkpoints per slide with instant feedback and study insights
- Zero raw LaTeX (Clean Unicode only)
"""

SLIDES_PART2 = [
    # Slide 9: Paved vs Green
    {
        "id": 9,
        "title": "Paved vs Green",
        "subtitle": "Urban Impervious Runoff vs Natural Infiltration",
        "concept_html": """
            <p class="mb-3">
                Modern cities face a paradox: even during massive torrential monsoon rains, urban groundwater levels continue to plummet while streets flood with knee-deep water. Why does this happen?
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30">
                    <span class="text-xs font-bold text-rose-300 block mb-1">🏢 Concrete & Asphalt Cities</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Tar roads, tiled courtyards, and cemented footpaths create an impervious seal. Rainwater cannot penetrate, turning into rapid surface runoff that overloads storm drains and rushes out to sea unabsorbed!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">🌳 Forests, Parks & Soak Pits</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Open soil, grassy gardens, village ponds, and porous gravel soak pits hold rainwater, allowing it to percolate slowly downward to replenish deep underground aquifers for future years.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                Urban Solution: Constructing rooftop rainwater harvesting systems and underground soak pits forces pure rainwater directly back into the subterranean water table.
            </p>
        """,
        "spoken_text": "Have you ever wondered why city streets drown in waterlogging during the monsoon, yet nearby tube wells run dry just a few months later? The answer lies in how we design our cities. In modern towns, vast areas of natural soil are paved over with asphalt roads, concrete footpaths, and tiled courtyards. These materials are completely waterproof. When rain falls, not a single drop can seep through the cement. Instead, the water rushes across the surface into drains, causing flash floods and flowing away wasted into the ocean. In contrast, in forests, grassy lawns, and open soil, rainwater is trapped by plant roots and slowly percolates underground, recharging our aquifers. By planting trees, maintaining open soil, and building soak pits, we help mother Earth drink her fill.",
        "lecture_script": "Have you ever wondered why city streets drown in waterlogging during the monsoon...",
        "checkpoints": [
            {
                "question": "Why does rain falling on paved city streets fail to recharge the underground water table?",
                "options": [
                    "Concrete and asphalt are impermeable surfaces that prevent water from seeping through",
                    "City rainwater evaporates instantaneously before touching the road",
                    "Vehicles drink up all the fallen rainwater",
                    "Underground rocks repel rainwater using magnetic fields"
                ],
                "correct": 0,
                "explanation": "Impervious materials like concrete and tar prevent infiltration, forcing water to flow away as surface runoff into drains instead of soaking into aquifers.",
                "study_insight": "Replacing solid concrete driveways with perforated paver blocks allows rainwater to soak into the soil."
            },
            {
                "question": "Which practical eco-friendly engineering feature helps recharge groundwater directly in urban buildings?",
                "options": [
                    "A rooftop rainwater collection system leading to a gravel soak pit",
                    "Covering every square meter of open garden soil with ceramic tiles",
                    "Pumping toxic sewage into rivers",
                    "Drying clothes under electric heaters"
                ],
                "correct": 0,
                "explanation": "Rooftop harvesting catches clean rainwater and directs it into a gravel-and-sand soak pit that filters it directly into the underground aquifer.",
                "study_insight": "Soak pits act as artificial percolation recharge wells for cities."
            }
        ]
    },

    # Slide 10: Surface Wealth
    {
        "id": 10,
        "title": "Surface Wealth",
        "subtitle": "Ponds, Lakes, Streams, and Perennial Rivers",
        "concept_html": """
            <p class="mb-3">
                Aside from water hidden deep underground, nature provides open, visible reservoirs of fresh liquid water across landscapes, collectively referred to as <strong>surface water</strong>:
            </p>
            <div class="grid grid-cols-3 gap-2.5 my-3 text-center">
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-300 block mb-1">🏞️ Ponds (Talab)</span>
                    <p class="text-[11px] text-slate-300">
                        Shallow, localized bodies of still water replenished by seasonal monsoon rains. Vital for village cattle and community washing.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">🌊 Lakes (Jheel)</span>
                    <p class="text-[11px] text-slate-300">
                        Much larger, deeper basins holding millions of liters of freshwater. Modulate regional climate and support thriving fisheries.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                    <span class="text-xs font-bold text-indigo-300 block mb-1">🏔️ Rivers (Nadi)</span>
                    <p class="text-[11px] text-slate-300">
                        Continuous flowing channels of freshwater that carve paths across entire continents from high mountains to the ocean.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-300">
                India's mighty rivers are divided into two great families: <strong>Himalayan Perennial Rivers</strong> (fed by melting mountain snow and rain, flowing all year) and <strong>Peninsular Rain-fed Rivers</strong> (whose flow swells during the monsoon and reduces during summer).
            </p>
        """,
        "spoken_text": "Besides groundwater hidden beneath our feet, nature gives us sparkling surface water bodies across the landscape. Ponds, or talabs, are shallow depressions that catch local monsoon runoff, providing drinking water for livestock and birds. Lakes are vast, deep natural water bodies, like Dal Lake in Kashmir or Vembanad Lake in Kerala, which cradle diverse aquatic life and cool the surrounding air. And then we have rivers—the living arteries of our nation. Rivers like the Ganga, Yamuna, and Brahmaputra originate high in snow-capped Himalayan glaciers, flowing year-round as perennial rivers. Other rivers in central and southern India, like the Godavari and Kaveri, depend primarily on seasonal monsoon downpours.",
        "lecture_script": "Besides groundwater hidden beneath our feet, nature gives us sparkling surface water bodies...",
        "checkpoints": [
            {
                "question": "Why do Himalayan rivers like the Ganga and Yamuna flow continuously throughout the scorching hot months of May and June?",
                "options": [
                    "They are continuously fed by melting ice and snow from high mountain glaciers",
                    "People pour water into them from overhead tanks",
                    "They receive heavy ocean tidal water flowing backward",
                    "Underground boiling lava pushes steam into them"
                ],
                "correct": 0,
                "explanation": "Glacial ice caps in the Himalayas melt during hot summer months, releasing abundant meltwater into rivers even before the monsoon rains arrive.",
                "study_insight": "Rivers that flow year-round are called perennial rivers."
            },
            {
                "question": "Which of the following is an example of a natural surface freshwater body rather than an underground source?",
                "options": [
                    "A freshwater lake",
                    "A borewell 200 feet deep",
                    "An artesian aquifer",
                    "A tube well casing pipe"
                ],
                "correct": 0,
                "explanation": "Lakes, ponds, and rivers exist openly on the Earth's surface and are classified as surface freshwater bodies.",
                "study_insight": "Surface water is directly exposed to sunlight and the atmosphere, whereas groundwater is sealed underground."
            }
        ]
    },

    # Slide 11: River Flow
    {
        "id": 11,
        "title": "River Flow",
        "subtitle": "Activity 6: Crumpled Paper Landforms & Water Contours",
        "concept_html": """
            <p class="mb-3">
                Why do rivers bend, snake, and meander across the plains instead of running in a straight line? In <strong>Activity 6</strong>, students crumple a sheet of newspaper, spread it gently across a tray to create peaks and valleys, sprinkle tiny mustard seeds along the ridges, and spray fine water mists.
            </p>
            <div class="space-y-2 my-3">
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-start space-x-3">
                    <span class="text-indigo-400 font-bold text-sm">🏔️</span>
                    <div>
                        <span class="text-xs font-bold text-white">Gravity is King:</span>
                        <p class="text-xs text-slate-300">Water always seeks the lowest point, pulled inexorably downhill by Earth's gravity from high elevations to sea level.</p>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-start space-x-3">
                    <span class="text-amber-400 font-bold text-sm">🌀</span>
                    <div>
                        <span class="text-xs font-bold text-white">Following the Contours:</span>
                        <p class="text-xs text-slate-300">Water cannot climb uphill; it navigates around stubborn hard rock ridges, carving winding curves called <em>meanders</em>.</p>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-start space-x-3">
                    <span class="text-emerald-400 font-bold text-sm">🌾</span>
                    <div>
                        <span class="text-xs font-bold text-white">Sediment Transport:</span>
                        <p class="text-xs text-slate-300">Just like the moving water carries tiny mustard seeds, rushing mountain streams transport gravel, sand, and fertile silt onto valley plains.</p>
                    </div>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Landforms dictate water's path, but over millions of years, water's hydraulic force carves canyons and reshapes the land!
            </p>
        """,
        "spoken_text": "Have you ever observed how a river snakes and curves gracefully across the countryside? We can discover why using a sheet of crumpled newspaper and a handful of mustard seeds. When we crumple the paper and lay it in a tray, its folds create miniature mountain peaks, ridges, and valleys. When we spray water on top, gravity pulls the droplets downhill along the easiest path through the creases. Just like the flowing droplets carry the tiny mustard seeds down into the folds, real rainwater rushes down mountain slopes, gathering into streams and valleys. Water always flows from higher elevations to lower elevations. Hard rocks and sloping contours force the river to bend and meander, depositing rich, fertile silt on the plains below.",
        "lecture_script": "Have you ever observed how a river snakes and curves gracefully across the countryside?...",
        "checkpoints": [
            {
                "question": "What fundamental physical force drives all rivers on Earth to flow constantly from mountains toward the ocean?",
                "options": [
                    "Earth's gravitational force pulling water downhill",
                    "Magnetic pull of the North Pole",
                    "Electric charges in sea fish",
                    "Atmospheric air blowing outward from space"
                ],
                "correct": 0,
                "explanation": "Gravity pulls every liquid droplet downward toward the center of the Earth, forcing water to flow from higher elevations to lower elevations.",
                "study_insight": "Water always flows along the path of least resistance under gravity."
            },
            {
                "question": "What is the scientific term for the graceful, winding S-shaped curves formed by mature rivers across flat plains?",
                "options": [
                    "Meanders",
                    "Glaciers",
                    "Craters",
                    "Geysers"
                ],
                "correct": 0,
                "explanation": "Meanders are looping curves in a river caused by continuous erosion of the outer bank and deposition of sediment along the inner bank.",
                "study_insight": "As a river slows down on flat plains, it meanders back and forth across its valley floor."
            }
        ]
    },

    # Slide 12: Aquatic Homes
    {
        "id": 12,
        "title": "Aquatic Homes",
        "subtitle": "Biodiversity of Freshwater Ecosystems",
        "concept_html": """
            <p class="mb-3">
                Freshwater ponds, rivers, and wetlands are vibrant biological hotspots. Countless species of flora and fauna make their homes in and around these aquatic environments:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌿 Aquatic Flora (Plants)</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li><strong>Lotus & Water Lily:</strong> Rooted in bottom mud with floating leaves and blossoms.</li>
                        <li><strong>Water Hyacinth (Jalkumbhi):</strong> Free-floating plants with swollen air-filled leaf stems.</li>
                        <li><strong>Hydrilla & Vallisneria:</strong> Submerged ribbon-like weeds producing oxygen underwater.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🐟 Aquatic Fauna (Animals)</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li><strong>Fish:</strong> Swimming in open water using fins and gills.</li>
                        <li><strong>Amphibians:</strong> Frogs and toads living dual lives in water and on land.</li>
                        <li><strong>Invertebrates:</strong> Dragonflies, water boatmen, and water scorpions.</li>
                        <li><strong>Wading Birds:</strong> Pond herons, egrets, and kingfishers patrolling the water's edge.</li>
                    </ul>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                Water provides buoyancy, dissolved oxygen, nutrients, and protection, making freshwater habitats among the most productive ecosystems on Earth.
            </p>
        """,
        "spoken_text": "Water bodies are not just liquid reservoirs; they are bustling, vibrant communities teeming with extraordinary life. A healthy freshwater pond or river ecosystem is home to hundreds of plant and animal species living in harmony. Floating on the surface, you will spot majestic lotus blooms, water lilies, and free-floating water hyacinths with lovely purple flowers. Beneath the calm surface, fish glide through underwater forests of hydrilla weeds, while frogs lay gelatinous eggs along muddy banks. Along the edges, slender dragonflies hover over the water, and patient pond herons stand motionless on long legs, waiting to snatch passing fish. Every zone of an aquatic habitat supports life.",
        "lecture_script": "Water bodies are not just liquid reservoirs; they are bustling, vibrant communities...",
        "checkpoints": [
            {
                "question": "Which of the following animals is an amphibian that can live both on land and in freshwater?",
                "options": [
                    "Frog",
                    "Shark",
                    "Pigeon",
                    "Earthworm"
                ],
                "correct": 0,
                "explanation": "Frogs are amphibians. They breathe through gills as aquatic tadpoles and develop lungs and moist permeable skin to breathe on land and in water as adults.",
                "study_insight": "Amphibian comes from Greek words meaning 'double life'."
            },
            {
                "question": "Why are submerged water weeds like Hydrilla crucial for fish in an aquarium or pond?",
                "options": [
                    "They produce dissolved oxygen during photosynthesis for fish to breathe",
                    "They heat the water like an electric stove",
                    "They turn all freshwater into salty ocean water",
                    "They block all sunlight from ever reaching the bottom"
                ],
                "correct": 0,
                "explanation": "During photosynthesis in sunlight, submerged plants release dissolved oxygen bubbles into the water, which fish extract through their gills.",
                "study_insight": "Aquatic plants oxygenate the water and provide protective shelters for baby fish."
            }
        ]
    },

    # Slide 13: Water Wonders
    {
        "id": 13,
        "title": "Water Wonders",
        "subtitle": "Specialized Morphological Adaptations of Aquatic Plants",
        "concept_html": """
            <p class="mb-3">
                How do water plants thrive without rotting in stagnant water, and how do their leaves float effortlessly on the surface? Over millions of years, aquatic plants (<strong>hydrophytes</strong>) evolved extraordinary morphological adaptations:
            </p>
            <div class="space-y-2.5 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🪷 Waxy Leaf Coating (Lotus & Lily)</span>
                    <p class="text-xs text-slate-300">
                        Lotus leaves are coated in microscopic waxy crystals creating the <em>Lotus Effect</em>. Water droplets roll off like beads, carrying away dirt and preventing waterlogged fungal rotting. Stomata are located only on the <strong>upper leaf surface</strong> for air exchange!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">🎈 Spongy Air Chambers (Water Hyacinth)</span>
                    <p class="text-xs text-slate-300">
                        The leaf stems (petioles) of water hyacinth are swollen with air-filled spongy tissue (<em>aerenchyma</em>). These internal air pockets act like natural life jackets, providing buoyancy to keep the plant afloat.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">🌿 Flexible Ribbon Stems (Hydrilla & Vallisneria)</span>
                    <p class="text-xs text-slate-300">
                        Submerged plants have thin, highly flexible ribbon-like leaves and hollow flexible stems that bend freely with water currents without snapping.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400">
                These adaptations allow aquatic plants to capture sunlight, stay buoyant, and breathe efficiently in aquatic realms.
            </p>
        """,
        "spoken_text": "If a terrestrial rose plant were submerged in a pond, its roots would rot and its leaves would decay in days. So how do aquatic plants thrive in water without rotting? Nature has gifted them extraordinary adaptations. Look closely at a lotus leaf: its upper surface is coated with a waterproof waxy layer. Raindrops roll right off like glistening mercury beads, keeping the breathing stomata completely dry. Furthermore, plants like the water hyacinth have swollen, bulbous leaf stalks packed with microscopic air chambers called aerenchyma. These spongy air pockets function just like life jackets, keeping the plant floating high on the water surface. Meanwhile, completely submerged plants have narrow, ribbon-like leaves that bend flexibly with river currents so they never break.",
        "lecture_script": "If a terrestrial rose plant were submerged in a pond, its roots would rot and its leaves would decay...",
        "checkpoints": [
            {
                "question": "Where are the breathing microscopic pores (stomata) located on floating lotus leaves?",
                "options": [
                    "Only on the upper dry surface facing the air",
                    "On the underside submerged in water",
                    "Inside the muddy roots",
                    "Lotus leaves possess no stomata"
                ],
                "correct": 0,
                "explanation": "Because the bottom surface rests directly on water, stomata are situated exclusively on the upper surface exposed to atmospheric air for gas exchange.",
                "study_insight": "Terrestrial leaves have stomata mostly on their underside, while floating aquatic leaves have them on top."
            },
            {
                "question": "What internal anatomical feature enables the water hyacinth (Jalkumbhi) to float effortlessly on water?",
                "options": [
                    "Spongy leaf petioles filled with buoyant air chambers (aerenchyma)",
                    "Heavy iron deposits in the roots",
                    "Solid wooden bark",
                    "Sticky glue on the flower petals"
                ],
                "correct": 0,
                "explanation": "Aerenchyma tissue contains wide air-filled cavities that dramatically reduce the plant's overall density, allowing it to float like a boat on water.",
                "study_insight": "Trapped air provides the upward buoyant force described by Archimedes' principle."
            }
        ]
    },

    # Slide 14: Fish & Fowl
    {
        "id": 14,
        "title": "Fish & Fowl",
        "subtitle": "Locomotion, Respiration, and Hunting Adaptations in Aquatic Animals",
        "concept_html": """
            <p class="mb-3">
                Water is nearly 800 times denser than air and contains far less free oxygen. To survive, freshwater animals have developed ingenious survival toolkits:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-cyan-300 block mb-1">🐟 The Fish Architecture</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        <strong>Streamlined Body:</strong> Spindle shape cuts through water with minimum friction drag.<br>
                        <strong>Fins & Tail:</strong> Pectoral and pelvic fins steer; powerful caudal tail propels forward.<br>
                        <strong>Gills:</strong> Feather-like crimson gills absorb dissolved oxygen directly from water.<br>
                        <strong>Swim Bladder:</strong> Internal gas sac for adjusting buoyancy at different depths.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🦤 The Pond Heron Wader</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        <strong>Stilt Legs:</strong> Long, slender legs allow silent wading through shallow mud without wetting body feathers.<br>
                        <strong>Spread Toes:</strong> Wide claw distribution prevents sinking into soft mud.<br>
                        <strong>Spear Beak:</strong> Dagger-like pointed bill strikes like lightning to capture darting fish.
                    </p>
                </div>
            </div>
            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-slate-300">
                <strong>Insect Snorkel:</strong> The water scorpion cannot breathe underwater; it possesses a long, hollow tail tube that it pokes through the water surface like a submarine snorkel to breathe atmospheric air!
            </div>
        """,
        "spoken_text": "Animals that live in water face unique challenges: water is dense and heavy to move through, and oxygen is dissolved in scarce amounts. Fish have evolved the ultimate aquatic blueprint. Their bodies are streamlined—narrow at both ends and broader in the middle—which allows them to slice through water currents with minimal friction. They use fins for steering and balance, and a strong tail fin for propulsion. Instead of lungs, fish breathe using delicate crimson gills that filter dissolved oxygen directly out of the water. Above the water, birds like the Indian pond heron have adapted as wading hunters. Their long, stilt-like legs let them wade through wetlands silently without splashing, and their long spear-like beaks strike instantly to catch fish. Even the tiny water scorpion has a long snorkel tail tube to breathe air while lurking underwater.",
        "lecture_script": "Animals that live in water face unique challenges: water is dense and heavy to move through...",
        "checkpoints": [
            {
                "question": "What specialized respiratory organ allows fish to extract dissolved oxygen directly from water?",
                "options": [
                    "Gills",
                    "Lungs",
                    "Skin pores",
                    "Scales"
                ],
                "correct": 0,
                "explanation": "Gills are rich in blood capillaries. As water passes over gill filaments, oxygen diffuses into the bloodstream while carbon dioxide diffuses out.",
                "study_insight": "Fish gulp water through their mouths and push it out through their gill slits."
            },
            {
                "question": "How does the aquatic insect known as the water scorpion obtain fresh air while submerged underwater?",
                "options": [
                    "It extends a long, hollow tail tube to the water surface like a snorkel",
                    "It breaks water molecules using an electric shock",
                    "It drinks water and manufactures oxygen in its stomach",
                    "It hibernates without oxygen for years"
                ],
                "correct": 0,
                "explanation": "The water scorpion possesses a pair of caudal breathing tubes at the tip of its abdomen that act as a snorkel to draw atmospheric air.",
                "study_insight": "Many aquatic insects breathe atmospheric air through siphon tubes or carry air bubbles on their bodies."
            }
        ]
    },

    # Slide 15: River Food Web
    {
        "id": 15,
        "title": "River Food Web",
        "subtitle": "Energy Flow, Producers, Consumers, and Ecological Balance",
        "concept_html": """
            <p class="mb-3">
                All living beings in an aquatic ecosystem are connected in an intricate web of energy flow known as a <strong>food chain</strong>. Every organism depends on others for nourishment and survival:
            </p>
            <div class="space-y-2 my-3">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div class="flex items-center space-x-2.5">
                        <span class="text-base">☀️ ➔ 🌿</span>
                        <span class="text-xs font-bold text-emerald-400">1. Primary Producers:</span>
                    </div>
                    <span class="text-xs text-slate-300">Microscopic green algae & water plants manufacture food using solar energy.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div class="flex items-center space-x-2.5">
                        <span class="text-base">🌿 ➔ 🦐</span>
                        <span class="text-xs font-bold text-cyan-400">2. Primary Consumers (Herbivores):</span>
                    </div>
                    <span class="text-xs text-slate-300">Water fleas, insect larvae, tadpoles, and snails graze on green algae.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div class="flex items-center space-x-2.5">
                        <span class="text-base">🦐 ➔ 🐟</span>
                        <span class="text-xs font-bold text-blue-400">3. Secondary Consumers (Carnivores):</span>
                    </div>
                    <span class="text-xs text-slate-300">Small fish, water scorpions, and diving beetles feed on insect larvae and tadpoles.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                    <div class="flex items-center space-x-2.5">
                        <span class="text-base">🐟 ➔ 🦤</span>
                        <span class="text-xs font-bold text-amber-400">4. Apex Predators:</span>
                    </div>
                    <span class="text-xs text-slate-300">Large fish, water snakes, pond herons, and otters sit at the top of the food chain.</span>
                </div>
            </div>
            <p class="text-xs text-rose-300 font-medium">
                Ecological Warning: Discharging industrial chemical poisons or sewage kills algae and insects, triggering a collapse of the entire river food web!
            </p>
        """,
        "spoken_text": "In every healthy river and pond, life is woven together in a beautiful chain of mutual dependence called a food chain. At the very foundation are the primary producers: microscopic green algae and floating water plants that harness radiant sunlight to manufacture food through photosynthesis. Next, primary consumers, such as tiny water fleas, aquatic snails, and herbivorous tadpoles, graze on this green buffet. In turn, small fish, dragonfly nymphs, and water scorpions prey upon the smaller insects. Finally, apex predators like large predatory fish, water snakes, and patient pond herons hunt the fish. If humans pollute a river with toxic chemicals or untreated sewage, the delicate algae die, causing the entire food web to collapse.",
        "lecture_script": "In every healthy river and pond, life is woven together in a beautiful chain of mutual dependence...",
        "checkpoints": [
            {
                "question": "Which organisms serve as the primary producers that generate initial food energy in an aquatic food chain?",
                "options": [
                    "Microscopic green algae and aquatic plants",
                    "Pond herons and egrets",
                    "Water scorpions",
                    "Predatory catfish"
                ],
                "correct": 0,
                "explanation": "Algae and water plants contain chlorophyll and produce organic carbohydrates using sunlight, water, and carbon dioxide through photosynthesis.",
                "study_insight": "All animal life in an aquatic ecosystem ultimately traces its energy back to solar-powered plant producers."
            },
            {
                "question": "What happens to the population of pond herons if severe water pollution wipes out all the small fish in a lake?",
                "options": [
                    "The heron population starves or is forced to abandon the lake due to food shortage",
                    "The herons begin eating stones and mud",
                    "The heron population multiplies ten times",
                    "The herons turn into fish"
                ],
                "correct": 0,
                "explanation": "Predators depend directly on their prey. If prey fish perish due to pollution, apex predators like herons face starvation and breeding collapse.",
                "study_insight": "Every link in an ecological food chain depends directly on the health of the links below it."
            }
        ]
    },

    # Slide 16: Every Drop Counts
    {
        "id": 16,
        "title": "Every Drop Counts",
        "subtitle": "Drought Impact, Water Conservation, and Sustainable Stewardship",
        "concept_html": """
            <p class="mb-3">
                In the review section <em>"Let us reflect"</em>, students examine what happens when rains fail for months or years, leading to severe <strong>drought (sookha)</strong>:
            </p>
            <div class="grid grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-300 block mb-1">🏜️ Devastation of Drought</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li>Lakes, ponds, and wells dry up completely.</li>
                        <li>Topsoil cracks, loses fertility, and blows away as dust.</li>
                        <li>Crops wither, triggering severe famine and cattle death.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-300 block mb-1">🛡️ Water-Wise Habits</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4">
                        <li>Turn off running taps while brushing teeth (saves 15 L).</li>
                        <li>Fix leaky faucets (1 dripping tap wastes 2,000 L/year).</li>
                        <li>Harvest monsoon rain from rooftops into soak pits.</li>
                        <li>Reuse kitchen vegetable wash water for potted plants.</li>
                    </ul>
                </div>
            </div>
            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-slate-300">
                <strong>Paper Fish Craft:</strong> Folding a paper fish reminds us that while we can craft origami creatures out of paper, real aquatic life cannot survive for a single hour without clean freshwater. Water is life!
            </div>
        """,
        "spoken_text": "Water is Earth's greatest gift, yet it is shockingly fragile. When monsoon rains fail for consecutive seasons, regions plunge into devastating droughts. Rivers shrink into dusty trails, the underground water table sinks out of reach, lush farmland cracks into barren dust, and both wildlife and humans suffer immense hardship. This teaches us that every single drop of freshwater is sacred. We can all become water guardians by practicing simple daily habits: turning off running taps while brushing, repairing dripping faucets promptly, reusing vegetable wash water for garden plants, and harvesting every drop of monsoon rain from our rooftops into recharge soak pits. Remember: water is not an endless commodity—it is the very essence of life.",
        "lecture_script": "Water is Earth's greatest gift, yet it is shockingly fragile. When monsoon rains fail...",
        "checkpoints": [
            {
                "question": "What severe environmental crisis develops when an agricultural region receives no rainfall for several consecutive seasons?",
                "options": [
                    "A severe drought, leading to crop failure and water shortages",
                    "A massive oceanic tsunami on mountain tops",
                    "Glaciers expanding across the desert",
                    "The water table rising to the treetops"
                ],
                "correct": 0,
                "explanation": "A prolonged absence of precipitation causes drought, drying up soil moisture, surface water bodies, and shallow wells.",
                "study_insight": "Droughts deplete groundwater reserves, making rainwater harvesting vital for regional resilience."
            },
            {
                "question": "Which of the following domestic practices represents the most effective daily method to conserve municipal freshwater?",
                "options": [
                    "Turning off the tap while lathering soap or brushing teeth, and fixing dripping washers immediately",
                    "Leaving the garden hose running continuously on concrete driveways",
                    "Throwing plastic garbage into drinking water wells",
                    "Boiling twenty buckets of water and pouring it down the gutter"
                ],
                "correct": 0,
                "explanation": "A single dripping faucet can waste up to 20 liters of pure water every day; closing taps promptly prevents thousands of liters of annual wastage.",
                "study_insight": "Small conservation habits practiced by millions of citizens save billions of liters of water."
            }
        ]
    }
]


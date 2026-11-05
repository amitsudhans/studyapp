"""
Part 1 of NCERT Class 5 Science Chapter 8: Clothes - How Things are Made
Slides 1 to 8
Short Headings (1-3 words) with exact same meaning:
1. Nature's Weavers
2. Warp and Weft
3. Handloom Heritage
4. Charkha Spinning
5. Natural Fibres
6. Silk Cocoon
7. Synthetic Fibres
8. Tailorbird Stitches
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Nature's Weavers",
        "subtitle": "The Baya Weaverbird: Master Architects of Hanging Woven Pouch Nests",
        "concept_html": """
            <p>Long before human beings invented spinning wheels or automated looms, animals and birds were already the planet's master textile engineers. Foremost among them is the extraordinary <strong>male baya weaver (weaverbird)</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🌾 Harvesting Fibre Strands</span>
                    <p class="text-xs text-slate-300">
                        During the monsoon breeding season, the male baya weaver uses its strong, sharp conical beak to snip long, flexible blades of tough grass, palm fronds, and paddy leaves, stripping them into uniform ribbons.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🪹 Over-and-Under Interlacing</span>
                    <p class="text-xs text-slate-300">
                        Perched on an acacia or thorny palm branch hanging over water (to deter snakes), the bird ties complex knots and interlaces hundreds of grass strips <strong>over and under each other</strong>. It weaves a waterproof, wind-resistant pouch with a central nesting chamber and a downward-hanging tubular entrance tunnel!
                    </p>
                </div>
            </div>
            <p>Female baya weavers inspect multiple woven nests across the colony, choosing a mate based on the tightness, security, and craftsmanship of the weaving!</p>
        """,
        "spoken_text": "Welcome young scientists to Chapter 8: Clothes, How Things are Made! Before humans ever held a needle or operated a loom, nature had already invented the art of weaving. High on thorny acacia trees swaying in the monsoon wind, look at the male baya weaverbird! With its conical beak, this industrious bird strips long, tough fibres of grass and palm leaves. Holding one blade steady with its claws, it weaves another strand over and under, tying intricate loops and knots. It constructs a magnificent hanging pouch nest complete with a secure nursery chamber and a downward tube entrance to protect eggs from predators. Nature is the original master weaver!",
        "lecture_script": "Introduces natural architectural weaving, highlighting the male baya weaverbird's technique of stripping grass and interlacing strands over-and-under to construct suspended pouch nests.",
        "checkpoints": [
            {
                "question": "How does the male baya weaver construct its intricate hanging pouch nest?",
                "options": [
                    "By digging deep burrows under the earth",
                    "By weaving long grass and palm leaf strips over and under each other with its beak",
                    "By sticking large rocks together with mud",
                    "By collecting plastic bags from roadsides"
                ],
                "correct": 1,
                "explanation": "The baya weaver uses its sharp beak to harvest flexible grass ribbons, looping and interlacing them over and under in a true weaving pattern.",
                "study_insight": "Male weaverbirds often paste wet mud blobs inside the nest walls; scientists believe this adds ballast against heavy winds and balances the structure."
            },
            {
                "question": "Why do baya weaverbirds typically build their hanging nests on branches dangling over water bodies?",
                "options": [
                    "To prevent tree snakes, monkeys, and ground predators from reaching their eggs and chicks",
                    "To wash their feathers before entering the nest",
                    "Because grass only grows underwater",
                    "To catch swimming fish from the doorway"
                ],
                "correct": 0,
                "explanation": "Suspended branches over rivers or ponds prevent land-based predators like snakes and rodents from easily raiding the nesting chamber.",
                "study_insight": "Spiders are another ancient weaver in nature, using liquid protein extruded from spinnerets to weave elastic orb webs to capture prey."
            }
        ]
    },
    {
        "id": 2,
        "title": "Warp and Weft",
        "subtitle": "The Art of Weaving: Orthogonal Interlacing of Threads to Create Fabric",
        "concept_html": """
            <p>Every piece of woven cloth—from your school uniform shirt to a cotton bedsheet or a bamboo basket—is constructed using one timeless geometric principle: <strong>weaving</strong>.</p>
            <div class="p-3.5 my-3 rounded-2xl bg-cyan-950/40 border border-cyan-500/40">
                <span class="text-xs font-bold text-cyan-300 block mb-1">Scientific Definition of Weaving:</span>
                <p class="text-xs text-slate-200 leading-relaxed">
                    <strong>Weaving</strong> is the process of interlacing two distinct sets of threads or strips at right angles (perpendicularly) to form a unified, continuous textile fabric, mat, or basket.
                </p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">⬆️ The Warp (Tana)</span>
                    <p class="text-xs text-slate-300">
                        The vertical or lengthwise set of parallel threads held stationary under tension across the frame or loom.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">➡️ The Weft (Bana)</span>
                    <p class="text-xs text-slate-300">
                        The horizontal or crosswise thread carried back and forth by a shuttle, passing alternately <em>over and under</em> each warp yarn.
                    </p>
                </div>
            </div>
            <p>In <strong>Activity 1: Paper Strip Weaving</strong>, students cut vertical slits into a colored paper sheet (warp) and thread horizontal contrasting paper strips (weft) over and under to create checkered mats!</p>
        """,
        "spoken_text": "What makes a shirt, a towel, or a grass mat hold together? It is the geometry of weaving! Weaving requires two distinct sets of yarns crossing each other at ninety-degree right angles. The vertical threads stretched tightly along the length of the loom are called the warp, or tana in Hindi. The horizontal thread passed back and forth across them is called the weft, or bana. As the shuttle carries the weft over one warp yarn and under the next, the loose strands lock securely together, transforming hundreds of fragile individual threads into a strong, flexible sheet of wearable fabric!",
        "lecture_script": "Defines weaving through the two orthogonal thread components: longitudinal warp (tana) and transversal weft (bana), explaining the over-and-under locking mechanism.",
        "checkpoints": [
            {
                "question": "In weaving technology, what are the lengthwise vertical threads held under tension on a loom called?",
                "options": [
                    "The warp (or tana)",
                    "The weft (or bana)",
                    "The sewing needle",
                    "The scissor blade"
                ],
                "correct": 0,
                "explanation": "The warp consists of longitudinal parallel yarns stretched along the loom, while the weft is passed perpendicularly over and under them.",
                "study_insight": "Warp yarns must withstand significant mechanical tension during weaving, so they are typically spun stronger and tighter than weft yarns."
            },
            {
                "question": "What is the purpose of Activity 1 (Paper Strip Weaving) in Class 5 Science?",
                "options": [
                    "To demonstrate how interlacing horizontal and vertical strips over and under forms a unified sheet of fabric",
                    "To test which paper burns the fastest",
                    "To make paper completely dissolve in water",
                    "To create a flying paper aeroplane"
                ],
                "correct": 0,
                "explanation": "Weaving paper strips demonstrates tactile, hands-on understanding of how orthogonal over-and-under interlacing locks loose strands into a sturdy cohesive mat.",
                "study_insight": "Basketry and cane furniture use this identical over-and-under weaving principle with thicker botanical stems like willow, bamboo, and rattan."
            }
        ]
    },
    {
        "id": 3,
        "title": "Handloom Heritage",
        "subtitle": "4,000 Years of Indian Weaving: Kanjeevaram, Pashmina & Ikat Traditions",
        "concept_html": """
            <p>India is universally recognized as the cradle of global cotton and silk textiles. Archaeological excavations at Mohenjo-daro and Harappa prove that Indian craftspeople have operated <strong>handlooms for over 4,000 years</strong>!</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-amber-400 block mb-1">🏛️ Kanjeevaram (Tamil Nadu)</span>
                    <span class="text-slate-300">Woven from pure mulberry silk with three single threads twisted with silver-gold zari, featuring temple border motifs.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-cyan-400 block mb-1">🏔️ Pashmina (Kashmir)</span>
                    <span class="text-slate-300">Hand-spun from the ultra-fine downy undercoat of Himalayan Changthangi mountain goats, renowned for ethereal featherlight warmth.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-rose-400 block mb-1">🎨 Ikat / Patola (Odisha & Gujarat)</span>
                    <span class="text-slate-300">Complex resist tie-dyeing of individual warp and weft yarns <em>before</em> weaving so vivid geometric patterns align on the loom!</span>
                </div>
            </div>
            <p>A traditional handloom is operated manually using foot pedals (treddles) and wooden shuttles, requiring zero electricity and sustaining millions of rural artisan families.</p>
        """,
        "spoken_text": "Step into India's four-thousand-year-old textile heritage! For millennia, our motherland has been the world's epicentre of exquisite handcrafted fabrics. Handloom weavers create legendary regional masterpieces: in Tamil Nadu, master weavers interlace pure mulberry silk and golden zari into heavy, lustrous Kanjeevaram sarees with temple borders. High in the cold Himalayas of Kashmir, artisans weave ultra-fine Pashmina shawls from the downy undercoat of mountain goats. In Odisha and Gujarat, weavers practice the breathtaking art of Ikat, tie-dyeing individual threads with mathematical precision before weaving them together. Every handloom cloth is a living canvas of Indian art!",
        "lecture_script": "Celebrates 4,000 years of Indian handloom heritage, exploring regional masterpieces including Kanjeevaram mulberry silk, Kashmiri Pashmina cashmere, and Odisha/Gujarat tie-dye Ikat.",
        "checkpoints": [
            {
                "question": "From which animal is genuine, ultra-soft Kashmiri Pashmina wool collected?",
                "options": [
                    "The fine undercoat of Changthangi mountain goats living at high altitudes in Ladakh and Kashmir",
                    "Domestic sheep living in coastal deserts",
                    "Wild desert camels",
                    "Himalayan snow leopards"
                ],
                "correct": 0,
                "explanation": "Pashmina is harvested from the ultra-fine winter down underfleece shed naturally by Changthangi goats grazing at elevations above 4,000 metres.",
                "study_insight": "A single Pashmina wool fibre is approximately 12 to 15 microns thick—six times finer than a strand of human hair!"
            },
            {
                "question": "What makes the 'Ikat' weaving tradition of Odisha and Gujarat distinct from ordinary printed fabrics?",
                "options": [
                    "Individual warp and weft threads are tied and dyed in precise patterns BEFORE being woven on the loom",
                    "Fabric is painted using chemical sprays after it is stitched into clothes",
                    "Threads are glued together using tree sap without any loom",
                    "Clothes are woven only from melted plastic ropes"
                ],
                "correct": 0,
                "explanation": "Ikat is a complex resist-dyeing technique where yarns are mathematically bundled, tied, and dyed prior to weaving, producing blurred feathered motifs when woven.",
                "study_insight": "Double Ikat (such as Patan Patola of Gujarat) requires both warp and weft threads to be independently tie-dyed, aligning perfectly during weaving."
            }
        ]
    },
    {
        "id": 4,
        "title": "Charkha Spinning",
        "subtitle": "Drawing and Twisting Fibres: Spindles, Charkhas & Gandhi's Khadi Freedom",
        "concept_html": """
            <p>Before any fabric can be woven, loose fluffy fibres must be converted into continuous, durable yarn. This transformative process is called <strong>spinning</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🌀 Pulling and Twisting Mechanics</span>
                    <p class="text-xs text-slate-300">
                        A raw cotton ball pulled apart is delicate and tears easily. But when you simultaneously <strong>pull out a slender strand and twist it</strong>, friction between overlapping microscopic fibres binds them together into strong, unbreakable thread!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🇮🇳 The Charkha & Khadi Movement</span>
                    <p class="text-xs text-slate-300">
                        From simple hand spindles (takli) evolved the traditional wooden <strong>charkha (spinning wheel)</strong>. Mahatma Gandhi championed the charkha and handspun <strong>Khadi</strong> cloth as a supreme symbol of self-reliance (Atmanirbhar), rural dignity, and peaceful freedom from foreign goods.
                    </p>
                </div>
            </div>
            <p>Today, spinning is performed by massive high-speed industrial ring frames that spin hundreds of kilometres of fine yarn every hour.</p>
        """,
        "spoken_text": "How do fluffy, cloud-like cotton bolls become strong sewing thread? Through the magic of spinning! If you simply pull raw cotton, it breaks apart. But when you pull out a few fibres and twist them between your fingers, microscopic ridges on the cotton fibres interlock tightly. Twisting creates immense friction, turning delicate fuzz into strong yarn! Centuries ago, people spun yarn using a simple hand spindle called a takli, followed by the wooden spinning wheel, or charkha. Mahatma Gandhi made the charkha and handspun Khadi cloth a national symbol of Indian self-reliance, freedom, and rural self-respect.",
        "lecture_script": "Explains the mechanical physics of spinning (drawing out and twisting fibres to create interlocking frictional strength), the hand spindle (takli), the charkha, and Gandhi's Khadi movement.",
        "checkpoints": [
            {
                "question": "What physical action converts loose, fragile cotton fibres into strong, durable yarn during spinning?",
                "options": [
                    "Drawing out fibres while simultaneously twisting them to create interlocking friction",
                    "Soaking fibres in cold water until they freeze solid",
                    "Hammering fibres flat with heavy iron stones",
                    "Painting fibres with bright red oil paint"
                ],
                "correct": 0,
                "explanation": "Spinning draws out parallel strands and twists them together; the spiral twist forces microscopic surface scales to interlock, providing tensile strength.",
                "study_insight": "You can experience spinning with your own fingers by gently twisting cotton wool while pulling it outward—it instantly turns into sturdy string!"
            },
            {
                "question": "Why did Mahatma Gandhi promote the Charkha and Khadi cloth across India during the Independence movement?",
                "options": [
                    "As a national symbol of self-reliance (Atmanirbhar), rural self-employment, and unity against foreign exploitation",
                    "Because there was a complete shortage of paper",
                    "Because he wanted everyone to wear raincoats",
                    "Because cotton only grew in one city"
                ],
                "correct": 0,
                "explanation": "Spinning Khadi empowered rural villagers economically and symbolized freedom from dependency on imported British machine-manufactured cloth.",
                "study_insight": "The Indian National Flag originally featured the spinning Charkha in its central white band before it was updated to Emperor Ashoka's 24-spoke Chakra."
            }
        ]
    },
    {
        "id": 5,
        "title": "Natural Fibres",
        "subtitle": "Earth's Bounty: Plant Cellulose (Cotton, Flax, Jute) & Animal Proteins (Wool, Silk)",
        "concept_html": """
            <p>Every textile material begins with raw <strong>fibres</strong>—slender, hair-like flexible strands. Natural fibres are harvested directly from botanical plants and living animals without industrial synthesis.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌱 Plant Fibres (Cellulose Based)</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><strong>Cotton:</strong> Fluffy seed pod hairs from cotton plants; breathable, soft, and absorbs sweat easily.</li>
                        <li><strong>Linen (Flax):</strong> Strong bast fibres extracted from flax plant stems; crisp, cool, and durable.</li>
                        <li><strong>Jute & Bamboo:</strong> Sturdy golden stem fibres used for eco-bags, ropes, mats, and sustainable apparel.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🐑 Animal Fibres (Protein Based)</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><strong>Wool:</strong> Curly keratin fleece sheared humanely from sheep, yak, and camels; traps pockets of insulating air.</li>
                        <li><strong>Silk:</strong> Continuous shimmering protein filament extruded by silkworm caterpillars to build cocoons.</li>
                    </ul>
                </div>
            </div>
            <p>Natural fibres are 100% biodegradable: when discarded, soil microorganisms decompose them naturally without leaving toxic microplastics!</p>
        """,
        "spoken_text": "Let us examine where our clothing fibres come from. Nature provides us with two major classes of natural fibres: plant fibres and animal fibres. Plant fibres, like soft cotton harvested from seed bolls, crisp linen obtained from flax plant stems, and golden jute, are made of plant cellulose. They are lightweight, highly breathable, and absorb sweat perfectly during hot Indian summers. Animal fibres, like wool sheared from sheep and yak, and shimmering silk produced by caterpillars, are made of natural proteins. Wool fibres are crimped, trapping pockets of still air to keep our bodies warm in winter!",
        "lecture_script": "Classifies natural fibres into plant-based cellulose (cotton, linen, jute, bamboo) and animal-based protein (wool, silk), detailing their physical properties and biodegradability.",
        "checkpoints": [
            {
                "question": "Which of the following is an example of a natural plant fibre harvested directly from seed pods?",
                "options": [
                    "Cotton",
                    "Nylon",
                    "Polyester",
                    "Wool"
                ],
                "correct": 0,
                "explanation": "Cotton grows as protective soft fluffy fibres surrounding the seeds of the Gossypium cotton plant.",
                "study_insight": "India is the world's largest producer of cotton, with the black regur soil of Gujarat, Maharashtra, and Telangana offering ideal growing conditions."
            },
            {
                "question": "Why do woolen sweaters keep us comfortably warm during chilly winter mornings?",
                "options": [
                    "Curly, crimped wool fibres trap millions of microscopic pockets of still air, which is an excellent thermal insulator",
                    "Wool contains tiny internal electric heaters",
                    "Wool radiates green nuclear light",
                    "Wool turns cold air into steam"
                ],
                "correct": 0,
                "explanation": "Trapped air is a very poor conductor of heat. The crimped structure of wool fibers creates air cushions that prevent body heat from escaping.",
                "study_insight": "Unlike synthetic garments, natural wool and cotton garments naturally decompose in composting soil within a few months."
            }
        ]
    },
    {
        "id": 6,
        "title": "Silk Cocoon",
        "subtitle": "Sericulture: The Metamorphic Life Cycle of the Bombyx mori Silkmoth",
        "concept_html": """
            <p>Silk is celebrated as the 'Queen of Textiles' for its shimmering elegance and featherlight tensile strength. The production of silk from the silkworm is an agricultural science called <strong>sericulture</strong>.</p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 my-3 text-xs text-center">
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-base block mb-1">🥚</span>
                    <span class="font-bold text-amber-400 block">1. Egg</span>
                    <span class="text-slate-400 text-[10px]">Female moth lays 300-500 tiny eggs</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-base block mb-1">🐛</span>
                    <span class="font-bold text-emerald-400 block">2. Caterpillar</span>
                    <span class="text-slate-400 text-[10px]">Feeds voraciously on fresh mulberry leaves for 30 days</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-base block mb-1">🧶</span>
                    <span class="font-bold text-cyan-400 block">3. Cocoon</span>
                    <span class="text-slate-400 text-[10px]">Spins a 1,000 m continuous protein filament around itself</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-base block mb-1">🦋</span>
                    <span class="font-bold text-purple-400 block">4. Adult Moth</span>
                    <span class="text-slate-400 text-[10px]">Metamorphoses into pupa and emerges as adult silk moth</span>
                </div>
            </div>
            <p>The caterpillar moves its head in a figure-eight (8) motion, secreting liquid protein (fibroin and sericin) from salivary glands that hardens upon contact with air into shimmering silk filament.</p>
        """,
        "spoken_text": "Discover the incredible secret of silk! Silk is spun by a small creature: the caterpillar of the silk moth, Bombyx mori. A mother moth lays hundreds of tiny eggs. When they hatch, the ravenous caterpillars feed non-stop on fresh green mulberry leaves for four weeks, growing thousands of times their original weight! Ready to pupate, the caterpillar weaves a protective oval home called a cocoon. Moving its head in figure-eight patterns, it extrudes a continuous liquid protein thread from its glands that hardens in the air. A single unbroken silk thread from one cocoon can measure nearly one kilometre in length!",
        "lecture_script": "Outlines sericulture and the complete 4-stage metamorphic life cycle of the Bombyx mori silkmoth: egg, voracious mulberry-eating caterpillar, protein cocoon spinning, and adult moth.",
        "checkpoints": [
            {
                "question": "What primary food do silkworm caterpillars eat voraciously before spinning their silk cocoons?",
                "options": [
                    "Fresh green mulberry leaves",
                    "Dry wheat flour grains",
                    "Sugarcane juice drops",
                    "Neem tree bark"
                ],
                "correct": 0,
                "explanation": "Silkworms (Bombyx mori) feed almost exclusively on the nutritious leaves of the white mulberry tree (Morus alba) to build protein reserves.",
                "study_insight": "India produces four diverse varieties of natural silk: Mulberry, Tasar (wild forest silk), Muga (golden silk of Assam), and Eri (peace silk)."
            },
            {
                "question": "What geometric pattern does a silkworm caterpillar trace with its head while spinning its silk cocoon?",
                "options": [
                    "A continuous figure-eight (8) pattern",
                    "A perfect straight triangle",
                    "A zigzag staircase",
                    "It holds its head completely still"
                ],
                "correct": 0,
                "explanation": "The caterpillar swings its head in regular figure-8 loops to distribute the liquid fibroin filament evenly around its body into an oval cocoon shell.",
                "study_insight": "A single continuous strand of silk reeled from one cocoon can extend between 800 and 1,200 metres!"
            }
        ]
    },
    {
        "id": 7,
        "title": "Synthetic Fibres",
        "subtitle": "Human-Made Polymers: Nylon, Rayon, Polyester & Petroleum Chemistry",
        "concept_html": """
            <p>While natural fibres have clothed humanity for thousands of years, modern chemists invented <strong>synthetic (man-made) fibres</strong> in industrial laboratories using petrochemicals.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🧪 Chemical Polymer Synthesis</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><strong>Nylon:</strong> First fully synthetic polymer; ultra-strong, elastic, used for parachutes, ropes, and toothbrushes.</li>
                        <li><strong>Polyester & Terylene:</strong> Wrinkle-free, dries exceptionally fast; common in sportswear and raincoats.</li>
                        <li><strong>Rayon (Artificial Silk):</strong> Semi-synthetic fibre regenerated from processed wood pulp cellulose; soft and shiny.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">⚖️ Advantages vs Disadvantages</span>
                    <p class="text-xs text-slate-300">
                        <strong>Pros:</strong> Highly durable, moth-resistant, wrinkle-free, and affordable.<br>
                        <strong>Cons:</strong> Poor breathability (traps sweat), melts and sticks to skin when exposed to kitchen fire, and sheds non-biodegradable microplastics into oceans!
                    </p>
                </div>
            </div>
            <p><strong>Safety Warning:</strong> Never wear synthetic polyester or nylon clothes while working in the kitchen near gas stoves or lighting Diwali crackers!</p>
        """,
        "spoken_text": "Now let us examine human-made synthetic fibres. In the twentieth century, chemists invented fibres synthesized from petroleum chemicals, called synthetic polymers. The most famous include nylon, polyester, acrylic, and terylene. Synthetic fibres have remarkable advantages: they are extraordinarily strong, wrinkle-resistant, insect-proof, and dry in minutes after washing. But they have critical drawbacks: synthetic fabrics do not absorb sweat well, making them clammy in hot weather. More dangerously, synthetic clothes melt like hot plastic when exposed to flame, sticking painfully to human skin. Always wear natural cotton clothes when near kitchen stoves or fire!",
        "lecture_script": "Contrasts synthetic petrochemical fibres (nylon, polyester, terylene, rayon) with natural fibres, examining their tensile strength, low breathability, and dangerous fire melting hazards.",
        "checkpoints": [
            {
                "question": "What is a major safety danger of wearing synthetic fabrics like nylon and polyester near open flames or kitchen stoves?",
                "options": [
                    "Synthetic fibres melt rapidly into hot sticky liquid that clings to the skin, causing severe burns",
                    "Synthetic fabrics turn into ice water",
                    "Synthetic clothes become five times heavier",
                    "They immediately change colour to bright blue"
                ],
                "correct": 0,
                "explanation": "Because synthetics are thermoplastic polymers, exposure to fire causes them to melt and fuse into flesh rather than charring into ash like natural cotton.",
                "study_insight": "Firefighters, chefs, and laboratory scientists always wear 100% natural treated cotton or fire-retardant aramid fibers for thermal protection."
            },
            {
                "question": "Which of the following is an advantage of synthetic polyester sportswear over pure natural cotton?",
                "options": [
                    "It dries very quickly after washing, resists wrinkles, and has high tensile strength",
                    "It is made by silkworms in gardens",
                    "It decomposes in garden soil within two days",
                    "It grows on mulberry trees"
                ],
                "correct": 0,
                "explanation": "Polyester does not absorb moisture into its polymer chains (hydrophobic), allowing wash water and sweat to evaporate rapidly from its surface.",
                "study_insight": "Rayon is unique as a 'semi-synthetic' fibre: it is manufactured from natural wood pulp cellulose that has been chemically dissolved and extruded."
            }
        ]
    },
    {
        "id": 8,
        "title": "Tailorbird Stitches",
        "subtitle": "Natural Craftsmanship: Orthotomus sutorius Stitching Leaves with Silk",
        "concept_html": """
            <p>Just as the baya weaver bird inspired human weaving, another tiny winged neighbor inspired human stitching: the lively <strong>common tailorbird (Orthotomus sutorius)</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🪡 Needle-Like Beak Punctures</span>
                    <p class="text-xs text-slate-300">
                        This restless, olive-green songbird selects two large living leaves on a garden shrub. Using its long, slender, curved beak like an awl or cobbler's needle, it punctures a neat line of tiny matching eyelet holes along the leaf margins!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🧵 Spider Silk Knots & Rivets</span>
                    <p class="text-xs text-slate-300">
                        For thread, the tailorbird gathers sticky cobweb silk, fine plant fibres, or cotton lint. Pulling the strand through the punctured holes, the bird tugs on the end to form a tangled little fuzzy knot (rivet) that stops the thread from slipping out, pulling the green leaves into a concealed cradling cup!
                    </p>
                </div>
            </div>
            <p>Inside this stitched living cradle, the tailorbird lines the pouch with soft kapok fluff and feathers, keeping its hatchlings safely hidden from marauding crows and cats.</p>
        """,
        "spoken_text": "Meet nature's most skilled tailor: the common tailorbird! Flitting through Indian gardens with an upright cocked tail, this small olive-green bird builds its nest through genuine stitching. The tailorbird selects two broad green leaves on a plant. Using its sharp, slender beak like a sewing needle, it punches neat holes along the edges of both leaves. Next, it collects sticky spider cobwebs or cotton threads. Threading the fibre through the holes, it tangles the ends into fuzzy little knots that prevent the thread from pulling back out. It stitches the two leaves tightly together into a green sleeve, then pads the inside with soft feathers to cradle its babies!",
        "lecture_script": "Examines the nesting biology of the common tailorbird, detailing its needle-like beak punching leaf eyelets and using spider silk/cotton threads with knotted rivets to stitch living leaves together.",
        "checkpoints": [
            {
                "question": "How does the tailorbird create eyelet holes along the edges of broad leaves?",
                "options": [
                    "By puncturing them with its sharp, slender, needle-like beak",
                    "By burning holes with hot embers",
                    "By chewing holes with large teeth",
                    "By dropping stones from the sky"
                ],
                "correct": 0,
                "explanation": "The tailorbird uses its thin, pointed bill as a surgical puncture awl to make evenly spaced holes along the leaf margins.",
                "study_insight": "The tailorbird chooses living leaves still attached to the plant stem so the cradle remains fresh, green, and camouflaged among garden foliage."
            },
            {
                "question": "What material does the tailorbird collect to use as sewing thread to join the punctured leaves?",
                "options": [
                    "Sticky spider silk, fine plant fibres, and soft cotton lint",
                    "Thick iron wire cables",
                    "Nylon fishing lines bought from shops",
                    "Strips of copper metal"
                ],
                "correct": 0,
                "explanation": "The tailorbird gathers sticky cobweb strands and natural plant fibers, threading them through the leaf holes and forming knots to lock them in place.",
                "study_insight": "Human tailors adopted this exact technique thousands of years ago, using bone needles and animal sinew before metal needles and cotton thread were invented."
            }
        ]
    }
]

print("Part 1 slides defined:", len(SLIDES_PART1))


"""
Class 6 Science Chapter 10: Living Creatures: Exploring their Characteristics
Part 3: 40 Quiz Questions across 4 Mastery Challenge Slides (Slides 17 to 20)
Every question contains id, question, options, answer, explanation, and solution_html.
Zero raw LaTeX. Pure clean Unicode.
"""

QUIZ_QUESTIONS = [
    # Challenge 1: Questions 1 to 10 (Slide 17)
    {
        "id": 1,
        "question": "Which of the following is a non-negotiable biological characteristic shared by ALL living organisms without exception?",
        "options": [
            "Possessing red blood and four walking limbs",
            "Undergoing metabolic respiration, cellular growth, and responsiveness to stimuli",
            "Flying through the air to capture flying insects",
            "Living exclusively submerged under oceanic water"
        ],
        "answer": 1,
        "explanation": "While specialized traits like walking limbs or flying vary, all living beings must respire, grow, excrete, and respond to stimuli at a cellular level.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Locomotion vs. Life:</strong> Many living organisms (such as rooted trees, corals, and fungi) do not possess walking limbs or fly.</p>
            <p>2. <strong>Core Characteristics:</strong> The universal criteria that define living organisms across all kingdoms are: cellular organization, nutrition, cellular respiration, metabolic excretion, growth, irritability (response to stimuli), reproduction, and death.</p>
            <p>3. <strong>Conclusion:</strong> Option B captures the universal biological processes shared by all living entities.</p>
        """
    },
    {
        "id": 2,
        "question": "Why is an empty spiral snail shell found on garden soil considered a non-living remnant rather than an active living organism?",
        "options": [
            "Because it is made purely of plastic manufactured in factories",
            "Because without the living snail, the shell does not respire, grow, eat, or reproduce",
            "Because living things never have any calcium in their bodies",
            "Because snails are mythical creatures that do not truly exist"
        ],
        "answer": 1,
        "explanation": "An empty shell is an organic-calcium structure produced by a living organism, but on its own it lacks cellular metabolism, respiration, and self-repair.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Biological Origin:</strong> The shell was produced by the mantle tissue of a living snail as an exoskeleton.</p>
            <p>2. <strong>Status of the Abandoned Shell:</strong> Once the organism dies or abandons the shell, the remaining calcium carbonate casing has no living cells, conducts no metabolism, consumes no food, and cannot reproduce.</p>
            <p>3. <strong>Conclusion:</strong> Hence, the isolated shell is classified as a non-living remnant.</p>
        """
    },
    {
        "id": 3,
        "question": "How do plants exhibit biological movement despite being anchored firmly into the soil by their root systems?",
        "options": [
            "By lifting their roots into the air and walking across fields at midnight",
            "Through directional tropisms such as stems bending to sunlight and tendrils coiling around supports",
            "Plants never exhibit any form of movement under any circumstances",
            "By shrinking their total volume to zero during cold winter nights"
        ],
        "answer": 1,
        "explanation": "Plants do not exhibit whole-body locomotion, but they display active differential growth movements (tropisms), opening/closing of flowers, and coiling of tendrils.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Locomotion vs. Movement:</strong> Locomotion is the movement of an entire organism from one place to another (common in animals). Movement refers to the change in posture, orientation, or shape of organs.</p>
            <p>2. <strong>Botanical Movements:</strong> Examples include phototropism (stems bending towards light), hydrotropism (roots seeking water), thigmotropism (tendrils coiling upon touch), and nastic movements (sleep movements of amla leaves and Mimosa folding).</p>
            <p>3. <strong>Conclusion:</strong> Option B accurately highlights plant-specific biological movements.</p>
        """
    },
    {
        "id": 4,
        "question": "What is the specialized prey-trapping mechanism employed by the carnivorous plant Drosera (Sundew)?",
        "options": [
            "It digs underground pitfall traps lined with spiderwebs",
            "Its leaves possess glandular tentacles tipped with sticky glistening droplets that curl around trapped insects",
            "It fires toxic spines from a distance of three meters",
            "It emits ultrasonic sounds that stun bees mid-flight"
        ],
        "answer": 1,
        "explanation": "Drosera leaves are covered with mucilage-secreting glandular hairs (tentacles). When an insect sticks to the mucilage, the tentacles bend inward to trap and digest it.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Morphology:</strong> The sundew (<em>Drosera</em>) grows in nutrient-poor acidic soils and supplements its nitrogen needs by capturing insects.</p>
            <p>2. <strong>Trapping Mechanism:</strong> Glandular hairs secrete sticky, glistening mucilage drops resembling morning dew. Contact with an insect stimulates thigmonastic bending of surrounding hairs within seconds.</p>
            <p>3. <strong>Digestion:</strong> Digestive enzymes break down the insect's soft tissues into absorbable nitrogen compounds.</p>
        """
    },
    {
        "id": 5,
        "question": "Which statement correctly distinguishes physical expansion in non-living objects from biological growth in living organisms?",
        "options": [
            "Biological growth occurs by internal cellular division and synthesis of protoplasm, whereas non-living growth is external accumulation",
            "Non-living growth requires water and oxygen, while animals grow without absorbing any matter",
            "Biological growth can be reversed by rubbing the animal with a towel",
            "There is no physical or biological difference between the two"
        ],
        "answer": 0,
        "explanation": "Living growth is intrinsic (from within) and irreversible, driven by cell division and metabolism. Non-living 'growth' (like a sand dune or crystal) is extrinsic accretion of surface matter.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Intrinsic Growth:</strong> In living beings, food is ingested, digested, and converted into cellular structures via mitosis, increasing size permanently.</p>
            <p>2. <strong>Extrinsic Growth:</strong> A crystal growing in a supersaturated solution or a sand dune expanding in the desert simply accumulates existing particles on its exterior surface.</p>
            <p>3. <strong>Conclusion:</strong> Option A describes the exact scientific difference.</p>
        """
    },
    {
        "id": 6,
        "question": "What is the primary difference between physical breathing and cellular respiration?",
        "options": [
            "Breathing occurs inside mitochondria while respiration occurs in the nose",
            "Breathing is the mechanical exchange of gases, whereas respiration is the biochemical breakdown of glucose to release energy",
            "Breathing produces food while respiration destroys water",
            "Only fish respire while land animals exclusively breathe"
        ],
        "answer": 1,
        "explanation": "Breathing is the physical ventilation process (inhaling oxygen, exhaling carbon dioxide). Cellular respiration is the chemical oxidation of nutrients yielding ATP energy.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Mechanical Breathing:</strong> Involves physical respiratory organs (lungs, gills, trachea) drawing in environmental oxygen and venting carbon dioxide.</p>
            <p>2. <strong>Biochemical Respiration:</strong> Occurs within every living cell (cytoplasm and mitochondria): Glucose + Oxygen ➔ Carbon Dioxide + Water + Usable Chemical Energy (ATP).</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the accurate distinction.</p>
        """
    },
    {
        "id": 7,
        "question": "Through which microscopic structures do plant leaves exchange gases during cellular respiration and photosynthesis?",
        "options": [
            "Stomata regulated by pairs of guard cells",
            "Root cap mucilage vesicles",
            "Petal pigment chromoplasts",
            "Xylem tracheid pits"
        ],
        "answer": 0,
        "explanation": "Stomata are microscopic pores located primarily on the lower surface of leaves. Guard cells swell or shrink to open or close the stoma, facilitating gas exchange.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Structure of Stomata:</strong> Each stoma is an elliptical aperture enclosed by two specialized, chlorophyll-containing guard cells.</p>
            <p>2. <strong>Function:</strong> They permit oxygen uptake and carbon dioxide release during respiration, as well as carbon dioxide intake and oxygen release during daytime photosynthesis.</p>
            <p>3. <strong>Conclusion:</strong> Option A is correct.</p>
        """
    },
    {
        "id": 8,
        "question": "Why do earthworms surface from their underground burrows onto open soil during heavy monsoon rainstorms?",
        "options": [
            "Because rainwater fills soil air pores, causing hypoxia and suffocation underground",
            "Because earthworms require direct sunlight to tan their outer cuticle",
            "Because they feed exclusively on falling raindrops",
            "Because earthworms cannot crawl when soil is moist"
        ],
        "answer": 0,
        "explanation": "Earthworms breathe cutaneously by absorbing oxygen dissolved in the film of moisture on their skin from soil air pores. When soil is flooded, air is displaced, forcing worms to surface for air.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Cutaneous Respiration:</strong> Earthworms lack lungs and gills; oxygen diffuses directly through their moist, capillary-rich outer cuticle into their bloodstream.</p>
            <p>2. <strong>Effect of Waterlogging:</strong> When heavy rains saturate the soil, water replaces all air in subterranean tunnels. Without oxygen, earthworms must emerge to the surface to breathe.</p>
            <p>3. <strong>Conclusion:</strong> Option A accurately explains this ecological observation.</p>
        """
    },
    {
        "id": 9,
        "question": "Which of the following processes is a true example of metabolic excretion in living plants?",
        "options": [
            "Absorbing water and mineral salts through root hairs",
            "Guttation of excess water and dissolved mineral salts from leaf margins, and shedding waste in autumn leaves",
            "Producing glucose in chloroplasts during daytime photosynthesis",
            "Opening flower petals in response to morning sunlight"
        ],
        "answer": 1,
        "explanation": "Excretion involves the elimination of metabolic wastes. Plants excrete excess water and salts via guttation hydathodes and store wastes in leaves that drop seasonally.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Definition of Excretion:</strong> The biological removal of metabolic waste products from the body.</p>
            <p>2. <strong>Botanical Strategies:</strong> Plants eliminate wastes through hydathodes (guttation droplets), bark shedding, and leaf abscission where accumulated mineral wastes are discarded.</p>
            <p>3. <strong>Conclusion:</strong> Option B represents plant excretory mechanisms.</p>
        """
    },
    {
        "id": 10,
        "question": "What is the biological significance of sweat production in humans during strenuous exercise or hot summer afternoons?",
        "options": [
            "It produces new muscle tissue directly on the skin surface",
            "It eliminates metabolic wastes (water, urea, salts) and cools the body via evaporative cooling",
            "It turns excess body fat directly into atmospheric nitrogen",
            "It prevents skin from absorbing necessary atmospheric oxygen"
        ],
        "answer": 1,
        "explanation": "Sweating serves dual functions: excretory elimination of excess water, salts, and traces of urea, and thermoregulatory cooling through the latent heat of evaporation.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Excretory Role:</strong> Sweat glands filter interstitial fluid, discharging water, sodium chloride, and metabolic waste traces onto the epidermal surface.</p>
            <p>2. <strong>Thermoregulatory Role:</strong> As sweat evaporates, it absorbs latent heat of vaporization from the skin, effectively cooling core body temperature.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the complete biological rationale.</p>
        """
    },

    # Challenge 2: Questions 11 to 20 (Slide 18)
    {
        "id": 11,
        "question": "What is a 'stimulus' in biological science?",
        "options": [
            "A non-living stone that never changes",
            "Any environmental change or event that evokes an active physiological or behavioral response from an organism",
            "The permanent death of an entire biological species",
            "A microscopic seed that cannot absorb water"
        ],
        "answer": 1,
        "explanation": "A stimulus is any detectable change in an organism's external or internal environment (light, heat, sound, touch, chemical) that triggers a response.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Definition:</strong> In physiology, a stimulus is an energetic change in the physical or chemical environment that excites sensory receptors.</p>
            <p>2. <strong>Examples:</strong> Bright light hitting the eye, the prick of a thorn on a fingertip, or the scent of food detecting by a hungry animal.</p>
            <p>3. <strong>Conclusion:</strong> Option B defines a biological stimulus accurately.</p>
        """
    },
    {
        "id": 12,
        "question": "When you accidentally step on a sharp thorn, your foot jerks upward before you consciously register the pain. What is this rapid reaction called?",
        "options": [
            "A reflex action",
            "Voluntary muscle fatigue",
            "Cellular photosynthesis",
            "Imbibition of water"
        ],
        "answer": 0,
        "explanation": "A reflex action is an automatic, involuntary, and rapid neural response to a dangerous stimulus, routed through the spinal cord to protect the body from severe injury.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Reflex Arc:</strong> The sensory receptor detects the thorn, transmits an impulse along sensory neurons to the spinal cord, which immediately fires a motor neuron causing leg flexor muscles to contract.</p>
            <p>2. <strong>Speed Advantage:</strong> By bypassing the cognitive processing of the brain, the reflex action prevents deeper tissue puncture.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the correct physiological term.</p>
        """
    },
    {
        "id": 13,
        "question": "Why do the leaflets of the Chhui-mui (Mimosa pudica) plant fold shut rapidly when lightly touched?",
        "options": [
            "Muscles in the stem contract just like animal arm muscles",
            "Water rapidly exits the cells of the swollen leaf base (pulvinus), causing an immediate loss of turgor pressure",
            "The leaves dry out and die permanently upon the touch of human skin",
            "The plant generates flames to scorch touching fingers"
        ],
        "answer": 1,
        "explanation": "Mechanical touch triggers an electrical action potential that causes potassium ions and water to rush out of the pulvinus cells at the base of leaflets, collapsing them.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Pulvinus Anatomy:</strong> The swollen hinge-like joint at the base of each petiole and leaflet is called the pulvinus.</p>
            <p>2. <strong>Turgor Dynamics:</strong> Touch generates an electrical wave. Cells in the lower half of the pulvinus rapidly pump out potassium and chloride ions, followed by osmotic water loss.</p>
            <p>3. <strong>Folding:</strong> Without internal fluid pressure (turgor), the leaf structure droops and leaflets fold together.</p>
        """
    },
    {
        "id": 14,
        "question": "What ecological or biological advantage does the Amla tree gain from its 'sleeping leaves' (nyctinasty) closing at sunset?",
        "options": [
            "It allows the tree to capture nocturnal moonlight for boiling sap",
            "It conserves leaf moisture, protects delicate tissues from nocturnal cold, and reduces surface exposure to pests",
            "It turns the leaves into poisonous fruits overnight",
            "It allows the tree to walk to another garden during the night"
        ],
        "answer": 1,
        "explanation": "Nyctinastic sleep movements reduce convective heat loss and nocturnal transpiration, while shielding delicate foliage from nocturnal herbivores and cold.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Nyctinasty:</strong> Circadian rhythm-driven closing of leaves during dark periods.</p>
            <p>2. <strong>Adaptive Value:</strong> At night, photosynthesis cannot occur. Folding leaflets reduces exposed surface area, retaining warmth and limiting water vapor loss.</p>
            <p>3. <strong>Conclusion:</strong> Option B explains the physiological benefits.</p>
        """
    },
    {
        "id": 15,
        "question": "Why is the biological process of reproduction considered essential for the survival of a species, even though an individual can survive without having offspring?",
        "options": [
            "Reproduction keeps an individual organism alive forever without eating",
            "Individual organisms eventually die, so reproduction ensures that new generations replace them, preventing species extinction",
            "Reproduction changes plants into mammals within one year",
            "Reproduction prevents rainwater from entering lakes"
        ],
        "answer": 1,
        "explanation": "Reproduction is not essential for the individual organism's survival, but it is indispensable for the continuity and survival of the species across generations.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Individual vs. Population:</strong> A sterile animal can live a full, healthy life. However, if an entire population ceases to reproduce, no new individuals are born.</p>
            <p>2. <strong>Extinction Prevention:</strong> As existing members succumb to predation, disease, or aging, the species would vanish without reproduction.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the accurate evolutionary explanation.</p>
        """
    },
    {
        "id": 16,
        "question": "Which of the following organisms reproduces by laying eggs (oviparous) rather than giving birth to live young?",
        "options": [
            "Cow",
            "Pigeon",
            "Elephant",
            "Human"
        ],
        "answer": 1,
        "explanation": "Pigeons (and birds in general) are oviparous; they lay hard-shelled eggs that are incubated until chicks hatch. Cows, elephants, and humans are viviparous mammals.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Ovipary:</strong> Embryo develops outside the mother's body within an egg protected by a shell (birds, reptiles, amphibians, insects, fish).</p>
            <p>2. <strong>Vivipary:</strong> Embryo develops directly inside the female uterus, receiving nourishment via the placenta, followed by live birth (mammals).</p>
            <p>3. <strong>Conclusion:</strong> Pigeons are oviparous birds (Option B).</p>
        """
    },
    {
        "id": 17,
        "question": "What is the biological definition of 'death' in living organisms?",
        "options": [
            "A temporary sleep from which an animal awakens after ten minutes",
            "The irreversible, permanent cessation of all metabolic processes, cellular repair, and vital functions in an organism",
            "The seasonal loss of leaves in deciduous trees during winter",
            "The movement of a seed through the digestive tract of a bird"
        ],
        "answer": 1,
        "explanation": "Death is the permanent, irreversible cessation of all biological functions that sustain a living organism, marking the terminal phase of its lifespan.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Lifespan Trajectory:</strong> Every living creature traverses a defined ontogenetic arc: birth ➔ growth ➔ maturity ➔ senescence ➔ death.</p>
            <p>2. <strong>Irreversibility:</strong> Unlike dormancy or hibernation (which are reversible), death involves the permanent breakdown of cellular homeostasis and metabolic pathways.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the rigorous scientific definition.</p>
        """
    },
    {
        "id": 18,
        "question": "In Activity 10.2, what are the three indispensable environmental factors tested for successful seed germination?",
        "options": [
            "Direct sunlight, motor oil, and table salt",
            "Water (moisture), oxygen (air), and suitable moderate temperature",
            "Continuous darkness, boiling water, and high vacuum",
            "Chemical pesticides, chemical dyes, and freezing ice"
        ],
        "answer": 1,
        "explanation": "Seed germination requires moisture to hydrate tissues and soften the coat, oxygen for aerobic cellular respiration, and favorable warmth for enzymatic action.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Moisture:</strong> Activates hydrolytic enzymes and softens the testa.</p>
            <p>2. <strong>Air (Oxygen):</strong> Drives aerobic ATP generation in embryo cells.</p>
            <p>3. <strong>Temperature:</strong> Most seeds have an optimum range of 20°C to 30°C where enzymes function at maximum velocity.</p>
            <p>4. <strong>Conclusion:</strong> Option B summarizes the three vital requirements.</p>
        """
    },
    {
        "id": 19,
        "question": "What happens if dry gram seeds are placed inside a deep freezer kept at -15°C with water and air present?",
        "options": [
            "They germinate twice as fast as seeds at room temperature",
            "They fail to germinate because extreme cold inactivates the metabolic enzymes necessary for embryo growth",
            "They turn into adult green plants with ripe pods in one day",
            "They absorb ice and start walking around the freezer"
        ],
        "answer": 1,
        "explanation": "Enzymes operate within specific thermal boundaries. At sub-zero temperatures, water freezes and enzymes are immobilized, preventing germination.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Enzyme Kinetics:</strong> Biochemical reactions of germination require thermal energy. At -15°C, kinetic energy is too low for enzymes to catalyze reactions.</p>
            <p>2. <strong>Water Freezing:</strong> Frozen water cannot be transported osmotically into seed tissues.</p>
            <p>3. <strong>Conclusion:</strong> The seeds remain dormant or suffer frost damage (Option B).</p>
        """
    },
    {
        "id": 20,
        "question": "What is the specialized role of the tiny microscopic pore called the 'micropyle' located on the seed coat?",
        "options": [
            "It serves as a chimney to exhaust green smoke during the night",
            "It allows water and oxygen to enter the dry seed during imbibition and provides an exit point for the emerging radicle",
            "It traps flying beetles inside the seed coat to act as food",
            "It absorbs radio waves from the surrounding environment"
        ],
        "answer": 1,
        "explanation": "The micropyle is the tiny opening through which pollen entered during fertilization, and through which water and oxygen enter during seed germination.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Anatomy:</strong> The micropyle is a minute pore in the testa (seed coat) of an angiosperm seed.</p>
            <p>2. <strong>Functional Role:</strong> During soaking, water enters rapidly through the micropyle into the cotyledons. During germination, the embryonic root (radicle) pushes out through this same aperture.</p>
            <p>3. <strong>Conclusion:</strong> Option B accurately specifies its dual role.</p>
        """
    },

    # Challenge 3: Questions 21 to 30 (Slide 19)
    {
        "id": 21,
        "question": "What is the biological term for the rapid, physical absorption of water by solid dry colloids (like dry seed starch and proteins) that causes immense swelling?",
        "options": [
            "Imbibition",
            "Transpiration",
            "Sublimation",
            "Photosynthesis"
        ],
        "answer": 0,
        "explanation": "Imbibition is the adsorption of water molecules by hydrophilic colloidal substances within seeds, generating massive hydrostatic swelling pressure.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Colloidal Chemistry:</strong> Dry proteins, cellulose, and starch in seed cotyledons have strong negative electrical affinities for polar water molecules.</p>
            <p>2. <strong>Imbibition Pressure:</strong> The swelling pressure generated can exceed hundreds of atmospheres, easily rupturing the toughest seed coats.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the precise botanical term.</p>
        """
    },
    {
        "id": 22,
        "question": "Why do seeds soaked in water swell and soften their tough outer coat (testa)?",
        "options": [
            "Because water molecules hydrate the dried cellulose matrix, increasing its elasticity and volume",
            "Because the seed fills with air bubbles that expand under pressure",
            "Because seeds consume water to build iron armour",
            "Because water turns the seed into pure sugar crystals"
        ],
        "answer": 0,
        "explanation": "Water molecules infiltrate the dense intermolecular spaces of the dry seed coat and cotyledons, hydrating cellular polymers and causing structural expansion and softening.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Hydration Effect:</strong> Dry seed coats are brittle and impermeable. Water hydration loosens intermolecular bonds in the testa, making it pliable and permeable.</p>
            <p>2. <strong>Facilitating Emergence:</strong> The softened coat allows the delicate radicle to pierce through without tearing or blunt trauma.</p>
            <p>3. <strong>Conclusion:</strong> Option A correctly explains the biophysical mechanism.</p>
        """
    },
    {
        "id": 23,
        "question": "Why does covering the water surface with an oil layer in a seed submersion experiment prevent seeds from sprouting?",
        "options": [
            "Oil turns the water into boiling acid",
            "The oil layer acts as a physical barrier preventing atmospheric oxygen from dissolving into the water",
            "Oil attracts hungry aquatic birds that eat the seeds",
            "Oil blocks gravitational forces from pulling the roots down"
        ],
        "answer": 1,
        "explanation": "Oil is immiscible and floats on water, sealing the liquid surface against atmospheric gas exchange. The seeds consume any residual oxygen and then suffocate.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Experimental Setup:</strong> Boiled water expels dissolved oxygen. Adding an oil layer on top prevents fresh oxygen from redissolving from the atmosphere.</p>
            <p>2. <strong>Oxygen Starvation:</strong> The embryo cannot perform aerobic respiration, halting ATP production and preventing cell division in the radicle.</p>
            <p>3. <strong>Conclusion:</strong> Option B is the scientific reason.</p>
        """
    },
    {
        "id": 24,
        "question": "What is the biological state called when healthy seeds kept in a dry environment remain alive but metabolically dormant for months or years?",
        "options": [
            "Seed dormancy",
            "Cellular necrosis",
            "Permanent extinction",
            "Active pollination"
        ],
        "answer": 0,
        "explanation": "Seed dormancy is an evolutionary adaptation that arrests embryo development in unfavorable conditions (dryness/cold), preserving viability until favorable cues return.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Suspended Animation:</strong> In dry seeds, cellular metabolic rates drop to less than 1% of normal levels, minimizing nutrient consumption.</p>
            <p>2. <strong>Survival Strategy:</strong> This prevents seeds from sprouting during harsh droughts or freezing winters when young seedlings would surely perish.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the correct biological term.</p>
        """
    },
    {
        "id": 25,
        "question": "How do seedlings grown in total darkness (etiolated) differ morphologically from seedlings grown in natural sunlight?",
        "options": [
            "They are short, thick, and possess deep purple flowers",
            "They become abnormally elongated, pale yellowish-white, and fragile due to lack of chlorophyll synthesis",
            "They develop giant roots and zero stems",
            "They turn into wooden branches within two hours"
        ],
        "answer": 1,
        "explanation": "In darkness, seedlings undergo etiolation: stems rapidly elongate searching for light, while chlorophyll production is blocked, leaving them pale yellow and frail.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Etiolation Syndrome:</strong> Without light cues, the plant allocates all resources to rapid stem elongation to pierce through what it perceives as deep soil.</p>
            <p>2. <strong>Chlorophyll Block:</strong> Light is required to convert protochlorophyllide into chlorophyll; without it, plastids remain etioplasts containing yellow carotenoids.</p>
            <p>3. <strong>Conclusion:</strong> Option B describes the classic etiolated appearance.</p>
        """
    },
    {
        "id": 26,
        "question": "Which directional growth movement causes the roots of a germinating seedling to grow downwards into the soil in response to gravity?",
        "options": [
            "Positive geotropism (gravitropism)",
            "Negative phototropism exclusively",
            "Positive hydrotropism only",
            "Nastic leaflet folding"
        ],
        "answer": 0,
        "explanation": "Positive geotropism (or gravitropism) is the directional growth of roots towards the pull of gravity, ensuring deep soil anchoring and water uptake.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Gravity Sensing:</strong> Dense starch grains called statoliths in root cap cells settle at the bottom of cells under gravity.</p>
            <p>2. <strong>Hormonal Response:</strong> This triggers asymmetric distribution of the growth hormone auxin, which in roots inhibits cell elongation on the lower side, curving the root tip downwards.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the correct botanical classification.</p>
        """
    },
    {
        "id": 27,
        "question": "When a potted plant is placed near a window inside a room, why does its green stem bend towards the sunlight?",
        "options": [
            "The stem is fleeing from room furniture",
            "Auxin hormones accumulate on the shaded side of the stem, causing those cells to elongate faster and curve the shoot toward light",
            "Sunlight pulls the stem mechanically using magnetic forces",
            "The leaves on the sunny side become heavy and drag the stem down"
        ],
        "answer": 1,
        "explanation": "Phototropism is driven by auxin redistribution. Light causes auxins to migrate to the shaded side of the stem, stimulating greater cell elongation there and bending the shoot toward light.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Auxin Redistribution:</strong> When light strikes a plant unilaterally, auxin moves laterally from the irradiated side to the shaded side.</p>
            <p>2. <strong>Differential Growth:</strong> In stems, higher auxin concentrations accelerate cell elongation. As the shaded side expands faster than the lit side, the stem curves toward the light.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the exact physiological mechanism.</p>
        """
    },
    {
        "id": 28,
        "question": "What remarkable capability did Sir Jagadish Chandra Bose's invention, the crescograph, offer to the scientific world?",
        "options": [
            "It allowed scientists to listen to radio stations on Mars",
            "It magnified minute plant growth and physiological movements by up to 10,000 times using optical levers",
            "It transformed dry desert sand into fertile black soil",
            "It predicted monsoon rainfall six years in advance"
        ],
        "answer": 1,
        "explanation": "J.C. Bose's crescograph used a compound system of mechanical levers and optical mirrors to magnify tiny plant movements up to 10,000 times, demonstrating plant responsiveness.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Engineering Marvel:</strong> Plant growth is imperceptibly slow (fractions of a millimeter per hour). Direct observation was impossible with ordinary microscopes.</p>
            <p>2. <strong>Optical Crescograph:</strong> Bose linked a delicate probe on the growing plant tip to a dual-lever system that recorded deflections onto a smoked glass plate, magnifying movements by up to 10,000×.</p>
            <p>3. <strong>Conclusion:</strong> Option B describes Bose's historic breakthrough.</p>
        """
    },
    {
        "id": 29,
        "question": "What major physiological discovery did J.C. Bose prove regarding the response of plants to anesthetics like chloroform and ether?",
        "options": [
            "Plants grew wooden legs and ran away",
            "Plants became anesthetized, losing electrical responsiveness and growth, and revived when fresh air was restored",
            "Plants exploded with loud popping sounds",
            "Plants showed zero change because chemicals cannot affect plant cells"
        ],
        "answer": 1,
        "explanation": "Bose exposed plants to chloroform vapor, demonstrating that plant electrical pulsations ceased under anesthesia, exactly like an anesthetized animal, and resumed upon ventilation.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Comparative Biophysics:</strong> Bose sought to demonstrate unity in biological matter. He subjected plants to animal anesthetics (chloroform, ether).</p>
            <p>2. <strong>Electrical Quenching:</strong> The crescograph and galvanometer showed complete cessation of electrical action potentials during exposure, followed by full recovery upon aeration.</p>
            <p>3. <strong>Conclusion:</strong> Option B summarizes Bose's groundbreaking experimental proof.</p>
        """
    },
    {
        "id": 30,
        "question": "Which of the following stages correctly outlines the chronological life cycle of a flowering plant?",
        "options": [
            "Adult tree ➔ Seedling ➔ Flower ➔ Seed",
            "Seed ➔ Germination & Seedling ➔ Vegetative Growth ➔ Flowering ➔ Fruit & Seed Formation ➔ Dispersal",
            "Fruit ➔ Flower ➔ Trunk ➔ Underground radicle",
            "Pollen ➔ Seedling ➔ Root hair ➔ Rotten wood"
        ],
        "answer": 1,
        "explanation": "The plant life cycle proceeds sequentially: dormant seed ➔ germination ➔ vegetative maturation ➔ flowering ➔ fruit/seed development ➔ seed dispersal.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Germination:</strong> Imbibition wakes the embryo, giving rise to radicle and plumule.</p>
            <p>2. <strong>Vegetative Stage:</strong> Formation of roots, stems, and photosynthetic foliage.</p>
            <p>3. <strong>Reproductive Stage:</strong> Flowering, pollination, double fertilization, fruit formation, and seed dispersal completing the generational loop.</p>
            <p>4. <strong>Conclusion:</strong> Option B represents the chronological sequence.</p>
        """
    },

    # Challenge 4: Questions 31 to 40 (Slide 20)
    {
        "id": 31,
        "question": "Which developmental stage of the mosquito life cycle is commonly referred to as a 'tumbler'?",
        "options": [
            "The egg raft",
            "The pupal stage",
            "The winged adult",
            "The crawling caterpillar"
        ],
        "answer": 1,
        "explanation": "The mosquito pupa is called a tumbler because of its tumbling motion through water when disturbed. The larva is called a wriggler.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Larva (Wriggler):</strong> Moves with rhythmic serpentine wriggling motions and actively feeds on micro-algae.</p>
            <p>2. <strong>Pupa (Tumbler):</strong> Comma-shaped, non-feeding stage that rolls and tumbles rapidly towards the pond bottom when shadow or movement threatens it.</p>
            <p>3. <strong>Conclusion:</strong> The pupal stage is the tumbler (Option B).</p>
        """
    },
    {
        "id": 32,
        "question": "Why do mosquito larvae (wrigglers) hang upside down just beneath the surface film of stagnant pond water?",
        "options": [
            "To sunbathe their transparent tails in the afternoon sun",
            "To project their respiratory siphon tube through the surface tension film into atmospheric air to breathe",
            "To catch flying honeybees with their tail appendages",
            "To avoid swimming near muddy bottom vegetation"
        ],
        "answer": 1,
        "explanation": "Wrigglers lack aquatic gills; they possess a specialized breathing siphon tube located at their posterior end that must pierce the water's surface film to breathe air.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Respiratory Anatomy:</strong> The mosquito larva is an aquatic insect that breathes atmospheric oxygen via a posterior siphon tube ringed with hydrofuge hairs.</p>
            <p>2. <strong>Posture:</strong> By hanging upside down, its mouth brushes sweep food from water currents while the siphon tip stays dry and open to ambient air.</p>
            <p>3. <strong>Conclusion:</strong> Option B is the biological explanation.</p>
        """
    },
    {
        "id": 33,
        "question": "How does pouring kerosene or eco-friendly larvicidal oil onto stagnant drains eradicate mosquito breeding?",
        "options": [
            "It turns the wrigglers into frogs within five minutes",
            "The oil forms an impenetrable floating film that blocks the breathing siphons of larvae and pupae, suffocating them",
            "It raises the water temperature to boiling point instantly",
            "It makes the water taste bitter so mosquitoes fly away to another country"
        ],
        "answer": 1,
        "explanation": "Oil spreads across the water surface, lowering surface tension and sealing the air-water interface so breathing siphons cannot draw air, suffocating the aquatic stages.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Surface Tension Disruption:</strong> A monomolecular or thin hydrocarbon oil slick spreads rapidly across the surface of stagnant pools.</p>
            <p>2. <strong>Mechanical Suffocation:</strong> Larval siphons and pupal breathing trumpets rely on surface tension to stay unflooded. The oil enters and clogs the siphon tubes, cutting off oxygen and suffocating them.</p>
            <p>3. <strong>Conclusion:</strong> Option B describes this effective physical vector control method.</p>
        """
    },
    {
        "id": 34,
        "question": "What is the primary commercial product derived from the protective cocoon stage of the silk moth (Bombyx mori)?",
        "options": [
            "Natural silk filament",
            "Synthetic polyester fiber",
            "Cotton lint batting",
            "Jute twine rope"
        ],
        "answer": 0,
        "explanation": "The cocoon of the silkworm consists of a continuous natural protein filament (fibroin bound by sericin) up to 1,000 meters long, which is harvested and reeled to produce natural silk.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Cocoon Formation:</strong> The mature silkworm extrudes liquid protein from salivary sericteries, weaving an elliptical shell around itself to protect the transforming pupa.</p>
            <p>2. <strong>Reeling Silk:</strong> In sericulture, cocoons are processed in warm water to soften the sericin gum and unwind the continuous silk filaments into yarn.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the natural silk filament.</p>
        """
    },
    {
        "id": 35,
        "question": "Which Indian organization promotes and supports rural sericulture, khadi spinning, and village silk cottage industries?",
        "options": [
            "Khadi and Village Industries Commission (KVIC)",
            "Indian Space Research Organisation (ISRO)",
            "Geological Survey of India (GSI)",
            "Automobile Association of Upper India (AAUI)"
        ],
        "answer": 0,
        "explanation": "KVIC (Khadi and Village Industries Commission) is the premier Indian statutory body fostering rural cottage industries, hand-spun khadi, and traditional sericulture weaving.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Institutional Heritage:</strong> The Khadi and Village Industries Commission (KVIC) was established to empower rural artisans and farmers through self-reliant cottage industries.</p>
            <p>2. <strong>Sericulture Link:</strong> Mulberry cultivation, silkworm rearing, and handloom silk weaving are heavily supported by KVIC schemes across India.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the correct national institution.</p>
        """
    },
    {
        "id": 36,
        "question": "What is the biological term for the dramatic anatomical transformation from an aquatic tadpole into a leaping terrestrial adult frog?",
        "options": [
            "Metamorphosis",
            "Imbibition",
            "Sedimentation",
            "Transpiration"
        ],
        "answer": 0,
        "explanation": "Metamorphosis is the biological process by which an animal physically develops after birth or hatching, involving a conspicuous and relatively abrupt change in body structure.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Etymology & Concept:</strong> Derived from Greek (<em>meta</em> = change, <em>morphe</em> = form). It describes major morphological restructuring between developmental stages.</p>
            <p>2. <strong>Amphibian Example:</strong> The limbless, gill-breathing, vegetarian tadpole transforms into a four-legged, lung-breathing, carnivorous adult frog.</p>
            <p>3. <strong>Conclusion:</strong> Option A is the correct biological term.</p>
        """
    },
    {
        "id": 37,
        "question": "What happens to the tail of an aquatic tadpole during its final stages of transformation into an adult frog?",
        "options": [
            "It drops off into the water like a fallen leaf and rots away",
            "It is enzymatically broken down and its nutrients are reabsorbed by the body to nourish growing limbs and lungs",
            "It transforms into a fifth jumping leg on the frog's belly",
            "It grows longer and becomes a poisonous defense stinger"
        ],
        "answer": 1,
        "explanation": "Through programmed cell death (apoptosis) and lysosomal enzymes, tail tissues are systematically broken down and reabsorbed into the froglet's body to fuel organ restructuring.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Apoptosis & Autophagy:</strong> During metamorphic climax, thyroid hormones trigger programmed cell destruction of the tail muscles, vertebrae, and skin.</p>
            <p>2. <strong>Nutrient Recycling:</strong> The amino acids and lipids from the degraded tail are transported through the bloodstream to build limbs, eyes, and lungs, leaving no external tail behind.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the accurate biological account.</p>
        """
    },
    {
        "id": 38,
        "question": "How does an adult frog breathe when it is resting quietly underwater at the bottom of a pond?",
        "options": [
            "It uses external feathered fish gills on its cheeks",
            "It conducts cutaneous gas exchange directly through its thin, moist, blood-vessel-rich skin",
            "It extends a long snorkel pipe out of the water surface",
            "It stops needing oxygen entirely and enters non-living stasis"
        ],
        "answer": 1,
        "explanation": "Adult frogs exhibit cutaneous respiration. When submerged, their lungs are inactive and gas exchange occurs entirely across their thin, mucus-covered, vascularized skin.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Cutaneous Respiration:</strong> Amphibian skin is permeable to water and gases. Mucus glands keep the skin moist, allowing dissolved oxygen in pond water to diffuse into subcutaneous capillaries.</p>
            <p>2. <strong>Dual Respiratory Modes:</strong> On land, frogs use pulmonary (lung) respiration and buccopharyngeal breathing; underwater, cutaneous respiration takes over.</p>
            <p>3. <strong>Conclusion:</strong> Option B is the correct physiological adaptation.</p>
        """
    },
    {
        "id": 39,
        "question": "Which of the following comparisons between a tadpole and an adult frog is scientifically ACCURATE?",
        "options": [
            "Tadpole has legs and breathes with lungs; adult frog has a tail and breathes with gills",
            "Tadpole is aquatic, has a tail, and breathes with gills; adult frog has four limbs, lacks a tail, and breathes via lungs and moist skin",
            "Tadpole lives on trees while adult frog lives inside dry desert cacti",
            "Both tadpole and adult frog have feathers and lay hard-shelled bird eggs"
        ],
        "answer": 1,
        "explanation": "The tadpole is aquatic with a tail and gills; the adult frog is semi-terrestrial, tailless, four-limbed, and breathes using lungs on land and moist skin in water.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Tadpole Traits:</strong> Hydrodynamic tail for propulsion, horny beak for scraping algae, internal/external gills for aquatic respiration, lack of limbs.</p>
            <p>2. <strong>Adult Frog Traits:</strong> Long muscular hind legs for leaping, wide mouth with projectile tongue for catching insects, lungs and moist vascular skin for dual respiration, tailless body.</p>
            <p>3. <strong>Conclusion:</strong> Option B is completely accurate.</p>
        """
    },
    {
        "id": 40,
        "question": "Why is eliminating stagnant water in discarded tyres, coconut shells, and air coolers an effective community health measure?",
        "options": [
            "It makes city streets look aesthetically cleaner for tourists",
            "It destroys the essential aquatic breeding habitat of mosquito eggs, wrigglers, and tumblers, preventing the spread of dengue and malaria",
            "It prevents frogs from jumping into people's living rooms",
            "It forces silkworms to weave cocoons on telegraph poles"
        ],
        "answer": 1,
        "explanation": "Female mosquitoes can only lay eggs in standing water where wrigglers and tumblers develop. Emptying stagnant water eliminates vector breeding sites and curbs disease transmission.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Vector Life Cycle Dependence:</strong> Mosquitoes (such as <em>Aedes</em> transmitting dengue and <em>Anopheles</em> transmitting malaria) require stagnant freshwater for their egg, larval, and pupal stages.</p>
            <p>2. <strong>Source Reduction:</strong> Eliminating small pools of standing water denies adult females egg-laying sites, breaking the reproductive cycle and dramatically slashing vector populations.</p>
            <p>3. <strong>Conclusion:</strong> Option B is the vital public health rationale.</p>
        """
    }
]


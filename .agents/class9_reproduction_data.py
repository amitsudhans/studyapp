"""
Data definitions for NCERT Class 9 Science Chapter 3: Reproduction
Covers Asexual and Sexual Reproduction, Plant Reproduction, Human Reproductive Systems,
Gestation, Menstrual Cycle, Reproductive Health & Contraception, Variations,
Assisted Reproductive Technologies (ART), and Indian Pioneers (Acharya Sushruta & Prof. Panchanan Maheshwari).
Syllabus Competencies: C-2.8, C-3.2, C-3.3, C-4.3, C-5.1, C-5.2, C-6.1, C-7.1, C-7.2.
"""

SLIDES_DATA = [
    # Slide 1: Introduction to Reproduction & Evolutionary Significance
    {
        "id": 1,
        "title": "Introduction to Reproduction & Evolutionary Significance",
        "subtitle": "Continuity of Life, DNA Replication Fidelity, and the Emergence of Variations",
        "narration": "Welcome students to our exploration of Reproduction! Unlike respiration, digestion, or circulation, reproduction is not necessary to keep an individual organism alive. Yet, without reproduction, life on Earth would cease in a single generation! Reproduction is the biological process by which existing organisms give rise to new offspring of their own kind, ensuring the continuity of species through geological time. At the deepest molecular level, reproduction involves the copying of DNA. Because no biochemical copying mechanism is 100% error-free, subtle variations arise during DNA replication. In asexual reproduction, a single parent produces genetically identical clones. In sexual reproduction, two parents combine their genetic blueprints, generating rich variations that allow species to survive in shifting environmental niches. Let us dive into this remarkable mechanism!",
        "points": [
            "<strong>Biological Purpose of Reproduction:</strong> Not required for individual survival, but absolutely essential for the perpetuation and continuity of species across generations.",
            "<strong>Molecular Foundation (DNA Copying):</strong> Involves the precise replication of genetic DNA followed by the creation of cellular apparatus to house daughter chromosomes.",
            "<strong>Asexual vs Sexual Paradigms:</strong> Asexual reproduction is uniparental producing genetically identical clones; sexual reproduction is biparental involving gametic fusion and genetic recombination.",
            "<strong>Significance of DNA Variation:</strong> Inherent biochemical inaccuracies during DNA replication introduce variations, serving as the essential raw material for natural selection and evolutionary adaptation."
        ],
        "checkpoints": [
            {
                "question": "Why is reproduction considered fundamentally different from life processes like nutrition and respiration?",
                "options": [
                    "It requires no cellular energy or enzymes",
                    "It is essential for the perpetuation of the species, but not for the survival of the individual organism",
                    "It occurs only in warm-blooded organisms",
                    "It eliminates the need for DNA replication"
                ],
                "correct": 1,
                "explanation": "An individual organism can live a healthy life without reproducing, but without reproduction, the species would become extinct upon the death of existing individuals."
            },
            {
                "question": "What is the primary evolutionary benefit of subtle variations arising during DNA replication?",
                "options": [
                    "They ensure all offspring look identical to the parent",
                    "They enhance the likelihood of species survival if environmental niches undergo drastic temperature or climatic changes",
                    "They prevent cells from undergoing mitosis",
                    "They stop organisms from consuming nutrients"
                ],
                "correct": 1,
                "explanation": "Variations give some individuals in a population unique traits (such as heat or drought tolerance) that allow them to survive if catastrophic changes alter their ecological niche."
            }
        ]
    },

    # Slide 2: Modes of Asexual Reproduction: Fission, Budding & Spore Formation
    {
        "id": 2,
        "title": "Modes of Asexual Reproduction: Fission, Budding & Spore Formation",
        "subtitle": "Uniparental Strategies: Binary Fission, Multiple Fission, Budding, and Sporogenesis",
        "narration": "In asexual reproduction, a single parent gives rise to new individuals without gametic fusion. Let us examine three fundamental asexual modes. First, Fission: in unicellular organisms like Amoeba, binary fission can occur in any plane. But in Leishmania, the pathogen causing kala-azar, binary fission occurs along a definite longitudinal plane relative to its whip-like flagellum! When conditions become harsh, Plasmodium, the malarial parasite, undergoes multiple fission inside a protective cyst, dividing into dozens of daughter cells simultaneously. Second, Budding: in Hydra and yeast, repeated mitotic cell division at a specific site creates an outgrowth or bud, which develops miniature organs before detaching as an independent organism. Third, Spore Formation: in the bread mould Rhizopus, thread-like hyphae develop swollen reproductive knobs called sporangia, containing hundreds of microscopic spores shielded by thick walls until they land on moist surfaces and germinate.",
        "points": [
            "<strong>Binary Fission (Amoeba vs Leishmania):</strong> Simple fission in Amoeba occurs in any plane; in Leishmania (kala-azar parasite), division occurs in a fixed longitudinal orientation relative to its apical flagellum.",
            "<strong>Multiple Fission (Plasmodium):</strong> The malarial parasite protects itself inside a resilient cyst, dividing mitotically into numerous daughter cells that emerge simultaneously when the cyst ruptures.",
            "<strong>Budding (Hydra & Yeast):</strong> Mitotic cell proliferation creates a localized outgrowth (bud) that develops into a miniature adult before detaching to lead an independent existence.",
            "<strong>Spore Formation (Rhizopus):</strong> Reproductive sporangia on erect hyphae produce hundreds of resistant spores with thick protective walls, enabling survival until landing on moist organic food."
        ],
        "checkpoints": [
            {
                "question": "How does binary fission in Leishmania differ fundamentally from binary fission in Amoeba?",
                "options": [
                    "Amoeba divides only at night, while Leishmania divides during the day",
                    "Leishmania binary fission occurs in a fixed longitudinal plane relative to its whip-like flagellum, whereas Amoeba divides in any arbitrary plane",
                    "Amoeba produces spores, while Leishmania produces seeds",
                    "Leishmania requires two parents, while Amoeba requires one"
                ],
                "correct": 1,
                "explanation": "Leishmania has a defined cellular orientation with a whip-like flagellum at one end, dictating that binary fission occurs strictly along a longitudinal plane."
            },
            {
                "question": "What protective structural feature allows Rhizopus spores to survive prolonged periods of drought and cold?",
                "options": [
                    "A calcium carbonate shell like a bird egg",
                    "A thick, resilient cell wall that shields the spore until it contacts a moist, nutrient-rich substrate",
                    "Active flagella that propel them into underground water",
                    "A waxy cuticle identical to plant leaves"
                ],
                "correct": 1,
                "explanation": "Rhizopus spores are encased in thick, resistant walls that shield the dormant protoplast from desiccation until favorable temperature and moisture stimulate germination."
            }
        ]
    },

    # Slide 3: Modes of Asexual Reproduction: Fragmentation, Regeneration & Vegetative Propagation
    {
        "id": 3,
        "title": "Modes of Asexual Reproduction: Fragmentation, Regeneration & Vegetative Propagation",
        "subtitle": "Spirogyra Cleavage, Planarian Pluripotency, and Horticultural Propagation",
        "narration": "Continuing our survey of asexual mechanisms: In simple multicellular organisms like the green alga Spirogyra, the filamentous body simply breaks into smaller fragments upon reaching maturity, each fragment growing into a complete filament through Fragmentation. In contrast, complex animals with organ systems cannot simply fragment. However, organisms like Planaria and Hydra possess remarkable Regenerative capacity: if sliced into several pieces, specialized proliferating cells regenerate the missing organs, reconstructing complete individuals! Furthermore, plants have perfected Vegetative Propagation, where vegetative parts—leaves, stems, or roots—produce new plants. Bryophyllum produces plantlets along the notches of its leaf margins; potato tubers sprout from axillary buds or 'eyes'. In agriculture, layering, cutting, and grafting allow farmers to propagate seedless crops like bananas, grapes, and oranges with guaranteed genetic uniformity and faster fruiting.",
        "points": [
            "<strong>Fragmentation in Spirogyra:</strong> Simple multicellular filaments break upon maturation into multiple pieces that grow into new filaments; feasible only in organisms with simple tissue grade.",
            "<strong>Regeneration in Planaria & Hydra:</strong> Specialized stem-like cells proliferate into an undifferentiated mass that differentiates into missing bodily tissues to reconstruct whole individuals.",
            "<strong>Natural Vegetative Propagation:</strong> Leaves of <em>Bryophyllum</em> develop foliar plantlets in marginal notches; potato tubers sprout from dormant 'eyes' (axillary buds); ginger propagates via rhizomes.",
            "<strong>Artificial Vegetative Techniques (Layering, Cutting, Grafting):</strong> Widely harnessed in horticulture to clone seedless crops (banana, orange, rose, jasmine), accelerating fruit bearing and preserving desirable agricultural traits."
        ],
        "checkpoints": [
            {
                "question": "Which plant is famous for producing vegetative adventitious plantlets along the notches of its leaf margins?",
                "options": [
                    "Rhizopus",
                    "Bryophyllum",
                    "Spirogyra",
                    "Hydra"
                ],
                "correct": 1,
                "explanation": "Bryophyllum leaves feature adventitious buds in marginal notches that sprout into miniature plantlets, which detach and root in soil to form new plants."
            },
            {
                "question": "Why is vegetative propagation commercially essential for cultivating fruits like bananas, seedless grapes, and oranges?",
                "options": [
                    "These plants cannot produce viable seeds, so vegetative propagation is the only reliable method to reproduce them true-to-type",
                    "Vegetative propagation makes the fruits poisonous to insects",
                    "It changes the fruit color to bright red",
                    "It converts flowering plants into ferns"
                ],
                "correct": 0,
                "explanation": "Commercial seedless varieties have lost the ability to produce viable seeds; vegetative propagation (cuttings, suckers, tissue culture) is essential for their reproduction."
            }
        ]
    },

    # Slide 4: Sexual Reproduction in Flowering Plants: Floral Anatomy & Functions
    {
        "id": 4,
        "title": "Sexual Reproduction in Flowering Plants: Floral Anatomy & Functions",
        "subtitle": "The Four Whorls: Calyx, Corolla, Stamen (Androecium), and Carpel (Gynoecium)",
        "narration": "In angiosperms, the flower is the specialized reproductive organ. A complete flower exhibits four concentric whorls anchored on a swollen receptacle. The outermost whorl is the Calyx, consisting of green sepals that protect the flower in its delicate bud stage. Inside lies the Corolla, made of vibrant, scented petals designed to attract animal pollinators. The reproductive whorls are central: the male organ is the Stamen, or Androecium, composed of a slender filament supporting a two-lobed Anther that produces haploid pollen grains containing male germ cells. In the center sits the female organ, the Carpel or Pistil (Gynoecium), consisting of a sticky terminal Stigma for capturing pollen, an elongated Style, and a swollen basal Ovary. Inside the ovary reside one or more Ovules, each housing an embryo sac with a female egg cell. Flowers containing both stamens and carpels, like mustard and hibiscus, are bisexual; flowers bearing only stamens or carpels, like papaya and watermelon, are unisexual.",
        "points": [
            "<strong>Four Floral Whorls:</strong> Non-reproductive accessory whorls (Calyx/sepals & Corolla/petals) protect organs and attract pollinators; essential reproductive whorls (Stamens & Carpels) produce gametes.",
            "<strong>Male Unit (Stamen / Androecium):</strong> Consists of a filament and terminal anther containing pollen sacs where microspores divide into pollen grains with male gametes.",
            "<strong>Female Unit (Pistil / Carpel / Gynoecium):</strong> Composed of a sticky receptive Stigma, a conduit Style, and a basal Ovary containing Ovules with female egg cells (female gametes).",
            "<strong>Unisexual vs Bisexual Flowers:</strong> Bisexual flowers (Hibiscus, Mustard) possess both stamens and pistils; unisexual flowers (Papaya, Watermelon) possess either stamens (staminate) or carpels (pistillate)."
        ],
        "checkpoints": [
            {
                "question": "Which part of the female reproductive organ in a flower is specialized with a sticky surface to capture pollen grains?",
                "options": [
                    "Filament",
                    "Stigma",
                    "Sepal",
                    "Petal"
                ],
                "correct": 1,
                "explanation": "The stigma is the sticky, receptive terminal landing pad of the carpel/pistil, designed to trap pollen grains transferred by wind, water, or pollinators."
            },
            {
                "question": "Which of the following plants produces unisexual flowers containing either only stamens or only carpels?",
                "options": [
                    "Hibiscus",
                    "Mustard",
                    "Papaya",
                    "Rose"
                ],
                "correct": 2,
                "explanation": "Papaya and watermelon produce unisexual flowers, meaning individual flowers possess either male reproductive stamens or female carpels, but not both."
            }
        ]
    },

    # Slide 5: Pollination Dynamics: Self vs Cross-Pollination & Plant-Pollinator Ecology (C-2.8, C-4.3)
    {
        "id": 5,
        "title": "Pollination Dynamics: Self vs Cross-Pollination & Plant-Pollinator Ecology",
        "subtitle": "Biotic & Abiotic Vectors: Co-Evolution, Mutualism, and Agricultural Security",
        "narration": "For fertilisation to occur, non-motile pollen grains must travel from the anther to the stigma—a transfer known as Pollination. If pollen lands on the stigma of the same flower or another flower on the same plant, it is Self-Pollination. If pollen is carried to the stigma of a flower on a different plant of the same species, it is Cross-Pollination, which promotes evolutionary variation. Plants utilize Abiotic vectors like Wind (anemophily) and Water (hydrophily). Wind-pollinated plants, like corn and grasses, produce copious amounts of light, non-sticky pollen and large, feathery stigmas to catch airborne grains. However, the majority of angiosperms rely on Biotic pollinators (C-2.8): insects like bees, butterflies, moths, and birds. Plants and pollinators exhibit magnificent co-evolution: flowers provide sugary nectar rewards, aromatic scents, and UV nectar guides, while pollinators ensure cross-fertilisation. Protecting insect pollinators is crucial, as one-third of global human food crops depend directly on animal pollination!",
        "points": [
            "<strong>Self vs Cross-Pollination:</strong> Self-pollination transfers pollen within the same plant; cross-pollination transfers pollen between different plants of the same species, introducing valuable genetic diversity.",
            "<strong>Abiotic Pollination (Wind & Water):</strong> Wind-pollinated flowers produce millions of lightweight, non-sticky pollen grains, possess feathery stigmas, and lack petals/nectar (e.g., maize, grasses).",
            "<strong>Biotic Pollination & Co-Evolution (C-2.8):</strong> Animal-pollinated flowers display vibrant petals, potent fragrances, and nectar rewards, establishing mutualistic partnerships with bees, butterflies, and birds.",
            "<strong>Ecological & Agricultural Impact:</strong> Over 75% of global flowering plants and 35% of agricultural crops rely on insect pollinators; pollinator decline directly threatens global food security."
        ],
        "checkpoints": [
            {
                "question": "What morphological characteristics typically adapt wind-pollinated flowers like maize and grasses for efficient pollination?",
                "options": [
                    "Large brightly colored petals with intense sweet perfume",
                    "Enormous nectar chambers to feed bats",
                    "Lightweight, smooth, non-sticky pollen grains produced in huge numbers with exposed feathery stigmas",
                    "Thick fleshy edible fruits surrounding the floral bud"
                ],
                "correct": 2,
                "explanation": "Wind pollination requires vast quantities of light, dry pollen that can drift on air currents, and large protruding feathery stigmas to maximize the capture of passing grains."
            },
            {
                "question": "Why is the mutualistic interaction between flowering plants and honeybees (C-2.8) considered vital for human agriculture?",
                "options": [
                    "Bees eat all parasitic weeds in agricultural fields",
                    "Cross-pollination by bees is essential for fruit and seed set in over one-third of major food crops consumed by humans",
                    "Honeybees convert plant pollen directly into synthetic fertilizer",
                    "Bees prevent plant leaves from transpiring water"
                ],
                "correct": 1,
                "explanation": "Animal pollinators like honeybees mediate cross-pollination in major agricultural crops (fruits, vegetables, nuts, oilseeds), making them indispensable for global food production."
            }
        ]
    },

    # Slide 6: Fertilisation in Angiosperms: Pollen Tube Growth & Double Fertilisation
    {
        "id": 6,
        "title": "Fertilisation in Angiosperms: Pollen Tube Growth & Double Fertilisation",
        "subtitle": "Chemotropic Tube Guidance, Syngamy, and Triploid Endosperm Formation",
        "narration": "Once a compatible pollen grain settles on the sticky stigma, it absorbs sugary secretions and germinates. A delicate Pollen Tube emerges and elongates downward through the tissues of the style, guided by chemotropic chemical gradients secreted by the ovary. Inside the pollen tube travel two haploid male gametes. The pollen tube reaches the ovary, enters an ovule through a microscopic aperture called the Micropyle, and penetrates the embryo sac. Here, a phenomenon unique to flowering plants unfolds: Double Fertilisation! The first male gamete fuses with the female egg cell to form a diploid Zygote ($2n$), a process called Syngamy. Simultaneously, the second male gamete fuses with the two polar nuclei in the central cell to produce a triploid Primary Endosperm Nucleus ($3n$), termed Triple Fusion. The endosperm develops into a nutritive tissue that feeds the growing embryo!",
        "points": [
            "<strong>Pollen Germination & Chemotropism:</strong> The pollen grain absorbs stigma fluids, germinating into a pollen tube that grows down the style guided by chemotropic ovarian signaling.",
            "<strong>Micropylar Entry:</strong> The pollen tube delivers two male gametes directly into the female embryo sac via the micropyle pore.",
            "<strong>Syngamy (First Fusion):</strong> Fusion of the first male gamete ($n$) with the female egg cell ($n$) produces the diploid Zygote ($2n$), which develops into the future plant embryo.",
            "<strong>Triple Fusion & Double Fertilisation:</strong> The second male gamete ($n$) fuses with the diploid central polar nuclei ($2n$) to form the triploid Endosperm ($3n$), which nourishes the embryo. This dual event is unique to Angiosperms."
        ],
        "checkpoints": [
            {
                "question": "In flowering plants, what is the biological product and ploidy of 'Triple Fusion'?",
                "options": [
                    "Diploid Zygote ($2n$)",
                    "Triploid Primary Endosperm Nucleus ($3n$)",
                    "Haploid Pollen Grain ($n$)",
                    "Tetraploid Seed Coat ($4n$)"
                ],
                "correct": 1,
                "explanation": "Triple fusion involves the fusion of one haploid male gamete ($n$) with two haploid polar nuclei ($2n$), forming a triploid ($3n$) endosperm that nourishes the embryo."
            },
            {
                "question": "What phenomenon guides the elongation of the pollen tube through the style toward the ovarian micropyle?",
                "options": [
                    "Phototropism toward sunlight",
                    "Geotropism toward gravity",
                    "Chemotropism in response to chemical gradients secreted by the ovary",
                    "Hydrotropism toward raindrops on petals"
                ],
                "correct": 2,
                "explanation": "The directed growth of the pollen tube through the style toward the ovule is a classic example of chemotropism, guided by ovarian chemical attractants."
            }
        ]
    },

    # Slide 7: Post-Fertilisation Transformations & Seed Dispersal Dynamics (C-3.2, C-4.3)
    {
        "id": 7,
        "title": "Post-Fertilisation Transformations & Seed Dispersal Dynamics",
        "subtitle": "Ovule to Seed, Ovary to Fruit, and Abiotic vs Biotic Dispersal Vectors",
        "narration": "Following double fertilisation, the flower undergoes dramatic post-fertilisation transformations. The petals, sepals, stamens, style, and stigma wither, dry, and fall away. Inside the ovary, the zygote divides repeatedly to form an embryo comprising the Radicle (future root), Plumule (future shoot), and one or two Cotyledons packed with food reserves. Crucially, memorize this anatomical rule: the Ovule develops a tough protective coat (testa) and transforms into the Seed, while the surrounding Ovary expands rapidly, ripens, and transforms into the Fruit! To prevent offspring from competing with the parent plant for light, water, and soil minerals, seeds are dispersed across landscapes (C-4.3) via Wind (winged seeds of maple, dandelion parachutes), Water (fibrous buoyant husks of coconuts), Animals (hooked burs of Xanthium clinging to fur, edible fleshy fruits like mangoes), and Explosive mechanisms (pea pods bursting open upon drying).",
        "points": [
            "<strong>Fundamental Post-Fertilisation Rule:</strong> The fertilised <strong>Ovule</strong> develops into the <strong>Seed</strong>; the surrounding <strong>Ovary</strong> matures and ripens into the <strong>Fruit</strong>.",
            "<strong>Embryo Anatomy:</strong> Housed within the protective seed coat (testa), the embryo contains the Plumule (future shoot), Radicle (future root), and Cotyledons (nutrient storage leaves).",
            "<strong>Ecological Purpose of Seed Dispersal:</strong> Prevents overcrowding, reduces intra-specific competition for sunlight, water, and soil minerals, and enables colonization of new geographic habitats.",
            "<strong>Dispersal Vectors (C-4.3):</strong> Wind (dandelion pappus, winged drumstick), Water (buoyant coconut husk), Animals (hooked Xanthium spines, edible berries dispersed via endozoochory), and Explosive dehiscence (balsam pods)."
        ],
        "checkpoints": [
            {
                "question": "What do the ovule and the ovary transform into respectively following successful double fertilisation in plants?",
                "options": [
                    "Ovule becomes Fruit; Ovary becomes Seed",
                    "Ovule becomes Seed; Ovary matures into Fruit",
                    "Ovule becomes Petal; Ovary becomes Stamen",
                    "Ovule becomes Pollen; Ovary becomes Stigma"
                ],
                "correct": 1,
                "explanation": "Following fertilisation, the ovule develops a tough protective seed coat and becomes the Seed, while the ovary walls swell and ripen into the protective Fruit."
            },
            {
                "question": "How are the hooked, spiny seeds of Xanthium (cocklebur) dispersed to new geographic environments (C-4.3)?",
                "options": [
                    "They float on ocean currents like coconuts",
                    "Their hooked spines latch onto animal fur and human clothing, carrying them far away",
                    "They explode like gunpowder when exposed to rain",
                    "They fly like helicopters using broad aerodynamic wings"
                ],
                "correct": 1,
                "explanation": "Xanthium seeds possess stiff hooked spines that easily catch onto the hair, fur, or feathers of passing animals (epizoochory), hitchhiking to distant locations."
            }
        ]
    },

    # Slide 8: Human Male Reproductive System: Anatomy & Spermatogenesis (C-5.1, C-7.2)
    {
        "id": 8,
        "title": "Human Male Reproductive System: Anatomy & Spermatogenesis",
        "subtitle": "Scrotal Thermoregulation, Vas Deferens, Accessory Glands, and Sperm Ultrastructure",
        "narration": "Shifting to human biology, the male reproductive system consists of gamete-producing organs and conducting ducts. The primary male sex organs are a pair of Testes located outside the abdominal cavity in a pouch of skin called the Scrotum. Why are testes situated outside the body? Because viable sperm production (spermatogenesis) requires a temperature 2 to 2.5 degrees Celsius lower than core body temperature (37 degrees Celsius)! Testes execute dual roles: producing millions of microscopic sperms and secreting the hormone Testosterone, which governs sperm maturation and secondary sexual characteristics like facial hair and voice deepening. From each testis, sperm pass through the Epididymis into the Vas Deferens. Along the way, accessory glands—the Seminal Vesicles and Prostate Gland—add nutrient-rich alkaline secretions that activate sperm motility and neutralize vaginal acidity, forming Semen. The semen exits through the Urethra inside the muscular Penis. Each sperm is a microscopic streamlined torpedo with an Acrosome-capped head housing the nucleus, a mitochondria-packed middle piece generating ATP, and a propelling flagellar tail.",
        "points": [
            "<strong>Scrotal Thermoregulation (C-7.2):</strong> Testes reside in the scrotum outside the abdominal cavity to maintain a temperature $2\\text{--}2.5^\\circ\\text{C}$ below normal core body temperature ($37^\\circ\\text{C}$), mandatory for spermatogenesis.",
            "<strong>Dual Testicular Function:</strong> Spermatogenesis (formation of haploid spermatozoa) and endocrine secretion of Testosterone (driving secondary male sexual characteristics).",
            "<strong>Conducting Ducts & Accessory Glands:</strong> Vas Deferens conducts sperm; Seminal Vesicles (fructose nutrients) and Prostate Gland (alkaline buffer) contribute fluids to create Semen.",
            "<strong>Sperm Ultrastructure:</strong> Head with condensed haploid nucleus and enzymatic Acrosome for ovum penetration; Middle piece packed with ATP-generating mitochondria; Flagellar Tail for swimming."
        ],
        "checkpoints": [
            {
                "question": "Why are human testes anatomically positioned outside the abdominal cavity within the scrotum (C-7.2)?",
                "options": [
                    "To allow easier access for hormone absorption from the skin",
                    "Because spermatogenesis requires a specialized temperature $2\\text{--}2.5^\\circ\\text{C}$ cooler than core internal body temperature",
                    "To protect the kidneys from mechanical shock",
                    "To completely prevent sperm cells from producing ATP"
                ],
                "correct": 1,
                "explanation": "Human spermatogenesis is temperature-sensitive and fails at core body temperature ($37^\\circ\\text{C}$); the scrotum acts as a thermoregulatory cooling radiator ($34.5\\text{--}35^\\circ\\text{C}$)."
            },
            {
                "question": "What is the primary physiological function of the secretion produced by the prostate gland and seminal vesicles?",
                "options": [
                    "To digest the walls of the bladder",
                    "To provide nutrients (fructose) and an alkaline lubricating fluid that enhances sperm motility and survival",
                    "To filter red blood cells out of the semen",
                    "To destroy female egg cells before fertilisation"
                ],
                "correct": 1,
                "explanation": "Prostate and seminal secretions nourish the sperms, provide an alkaline fluid to neutralize the acidic vaginal environment, and facilitate motility."
            }
        ]
    },

    # Slide 9: Human Female Reproductive System: Anatomy & Oogenesis (C-5.1)
    {
        "id": 9,
        "title": "Human Female Reproductive System: Anatomy & Oogenesis",
        "subtitle": "Ovarian Folliculogenesis, Fallopian Oviducts, and the Muscular Uterine Womb",
        "narration": "The human female reproductive system is situated entirely within the pelvic cavity, designed for gamete production, fertilisation, and nurturing a developing fetus. It comprises a pair of Ovaries, which produce female gametes (Ova or eggs) and secrete the vital steroid hormones Estrogen and Progesterone. At birth, a female's ovaries already contain thousands of immature follicles; starting at puberty, hormones stimulate one mature ovum to be released alternately every month in a process called Ovulation. Near each ovary lies the funnel-shaped fimbriated opening of the Fallopian Tube, or Oviduct. Ciliated epithelial cells lining the oviduct sweep the released ovum inward. Pay special attention: the Fallopian Tube is the precise anatomical site where fertilisation between sperm and egg takes place! The two oviducts unite into an elastic, hollow, highly muscular, inverted pear-shaped organ called the Uterus, or Womb. The inner vascular lining of the uterus, the Endometrium, prepares monthly to receive and nourish an embryo. The uterus opens into the muscular Vagina through the narrow Cervix.",
        "points": [
            "<strong>Ovaries & Endocrine Secretion:</strong> Primary female sex organs producing mature haploid ova and secreting Estrogen (follicle development, secondary sexual traits) and Progesterone (pregnancy maintenance).",
            "<strong>Ovulation:</strong> Cyclical release of one mature ovum alternately from one of the ovaries approximately every 28 days following the onset of menarche at puberty.",
            "<strong>Fallopian Tubes (Oviducts) - Site of Fertilisation:</strong> Ciliated tubes that convey the ovum toward the uterus; fertilisation strictly occurs within the ampulla of the fallopian tube.",
            "<strong>Uterus (Womb) & Endometrium:</strong> Muscular inverted pear-shaped chamber where the blastocyst implants; features a specialized vascular endometrial lining designed to support pregnancy."
        ],
        "checkpoints": [
            {
                "question": "In the human female reproductive tract, where does fertilisation of the ovum by a sperm typically occur?",
                "options": [
                    "Inside the ovary",
                    "In the ampullary region of the Fallopian Tube (Oviduct)",
                    "Inside the vaginal canal",
                    "On the surface of the cervix"
                ],
                "correct": 1,
                "explanation": "Fertilisation between a swimming sperm and a viable ovum strictly takes place in the upper third of the Fallopian tube (oviduct), not in the uterus or ovary."
            },
            {
                "question": "Which female hormone is primarily responsible for triggering the development of female secondary sexual characteristics at puberty?",
                "options": [
                    "Testosterone",
                    "Estrogen",
                    "Thyroxine",
                    "Insulin"
                ],
                "correct": 1,
                "explanation": "Estrogen, secreted by developing ovarian follicles at puberty, regulates the development of female secondary sexual characteristics (breast development, widened pelvis, pubic hair)."
            }
        ]
    },

    # Slide 10: The Menstrual Cycle: Hormonal Orchestration & Physiological Phases
    {
        "id": 10,
        "title": "The Menstrual Cycle: Hormonal Orchestration & Physiological Phases",
        "subtitle": "The 28-Day Feedback Loop: Follicular Growth, LH Surge Ovulation, and Luteal Maintenance",
        "narration": "If a released ovum is not fertilised, the female body resets its reproductive preparations through a monthly 28-day rhythm known as the Menstrual Cycle. Let us break down its four distinct phases. Phase 1 is the Menstrual Phase (Days 1–5): falling hormone levels cause the thickened, blood-rich endometrial lining of the uterus to break down, discharging as menstrual flow along with the unfertilised ovum. Phase 2 is the Follicular or Proliferative Phase (Days 6–13): pituitary FSH stimulates ovarian follicles to grow, which secrete rising levels of Estrogen to reconstruct a thick, vascular endometrium. Phase 3 is Ovulation (around Day 14): a massive spike in Luteinizing Hormone, known as the LH Surge, triggers the mature Graafian follicle to rupture, releasing the ovum into the oviduct. Phase 4 is the Luteal or Secretory Phase (Days 15–28): the ruptured follicle transforms into a glandular yellow body called the Corpus Luteum, pumping out high levels of Progesterone to make the endometrium lush and receptive. If fertilisation does not occur, the corpus luteum degenerates, progesterone crashes, and menstruation begins anew!",
        "points": [
            "<strong>Four Cyclic Phases (28-Day Periodicity):</strong> Menstrual Phase (Days 1–5), Follicular/Proliferative Phase (Days 6–13), Ovulation (~Day 14), and Luteal/Secretory Phase (Days 15–28).",
            "<strong>Hormonal Feedback Axis:</strong> Pituitary gonadotropins (FSH & LH) regulate ovarian follicular development and ovulation; ovarian steroids (Estrogen & Progesterone) govern uterine endometrial proliferation.",
            "<strong>The Ovulatory LH Surge:</strong> A sharp peak in Luteinizing Hormone (LH) at mid-cycle (~Day 14) induces the final maturation and rupture of the Graafian follicle, expelling the ovum.",
            "<strong>Corpus Luteum & Progesterone:</strong> The post-ovulatory collapsed follicle transforms into the Corpus Luteum, secreting Progesterone to maintain the vascular endometrium; its regression triggers menstruation."
        ],
        "checkpoints": [
            {
                "question": "What hormonal event is directly responsible for triggering ovulation (release of the egg) around Day 14 of the human menstrual cycle?",
                "options": [
                    "A rapid drop in insulin",
                    "A dramatic surge in pituitary Luteinizing Hormone (LH surge)",
                    "A total cessation of thyroid hormone production",
                    "A spike in adrenaline"
                ],
                "correct": 1,
                "explanation": "The LH surge (a sharp peak in luteinizing hormone from the anterior pituitary) triggers the rupture of the mature follicle and release of the secondary oocyte."
            },
            {
                "question": "What happens to the uterine endometrial lining if the released egg is not fertilised by a sperm?",
                "options": [
                    "It transforms into solid bone",
                    "Progesterone levels crash as the corpus luteum degenerates, causing the vascular endometrial lining to slough off as menstrual flow",
                    "It remains thickened permanently for the rest of the woman's life",
                    "It is absorbed directly into the liver"
                ],
                "correct": 1,
                "explanation": "In the absence of fertilisation, the corpus luteum regresses, causing progesterone levels to plummet; without hormonal support, the endometrium breaks down and sheds."
            }
        ]
    },

    # Slide 11: Fertilisation, Blastocyst Implantation, Placental Physiology & Gestation (C-3.2, C-5.1)
    {
        "id": 11,
        "title": "Fertilisation, Blastocyst Implantation, Placental Physiology & Gestation",
        "subtitle": "From Zygote Cleavage to Blastocyst Nidation, Hemochorial Exchange, and Parturition",
        "narration": "During coitus, millions of sperms are deposited into the vagina and swim through the cervix and uterus into the fallopian tubes. Although hundreds reach the ovum, only a single sperm penetrates the outer egg coat via acrosomal digestive enzymes, fusing its haploid nucleus ($n$) with the egg nucleus ($n$) to create a diploid Zygote ($2n$). The zygote immediately begins mitotic cleavage divisions as it travels down the oviduct, transforming into a hollow sphere of cells called a Blastocyst. Approximately seven days after fertilisation, the blastocyst embeds into the lush uterine endometrium—an event called Implantation. Following implantation, a specialized disc-like vascular bridge called the Placenta develops between maternal uterine tissues and fetal chorionic villi. The placenta is an absolute biological marvel: it diffuses glucose, amino acids, and oxygen from the mother's blood into fetal capillaries, while simultaneously expelling fetal metabolic wastes like urea and carbon dioxide into the maternal circulation via the umbilical cord. Following a gestation period of approximately nine months (280 days), powerful rhythmic contractions of the muscular uterine wall expel the baby during childbirth (Parturition).",
        "points": [
            "<strong>Monospermic Syngamy:</strong> Acrosomal enzymes dissolve the ovum's zona pellucida; fusion of haploid pronuclei restores diploidy ($2n = 46$ chromosomes), creating the Zygote.",
            "<strong>Cleavage & Implantation:</strong> Mitotic divisions convert the zygote into a morula and then a hollow Blastocyst, which embeds into the maternal uterine endometrium ~Day 7 post-fertilisation.",
            "<strong>Placental Architecture & Physiology:</strong> Disc-shaped vascular organ providing chorionic villi on the fetal side bathed in maternal blood pools; mediates nutrient uptake, gas exchange, and waste removal without mixing maternal and fetal blood directly.",
            "<strong>Gestation & Parturition:</strong> Full-term human development lasts ~9 months (38–40 weeks / 280 days); birth is mediated by neuroendocrine oxytocin surges inducing coordinated uterine myometrial contractions."
        ],
        "checkpoints": [
            {
                "question": "What is the primary physiological role of the placenta during human pregnancy?",
                "options": [
                    "To generate electrical impulses that jumpstart the fetal heartbeat",
                    "To mediate the diffusion of oxygen, glucose, and nutrients from mother to fetus, and the removal of fetal metabolic waste like carbon dioxide and urea",
                    "To directly pump maternal red blood cells into the fetal brain",
                    "To produce hydrochloric acid for fetal digestion"
                ],
                "correct": 1,
                "explanation": "The placenta acts as a selective exchange organ, allowing vital nutrients and oxygen to diffuse from maternal blood to the fetus while clearing fetal wastes via the umbilical vessels."
            },
            {
                "question": "What is the average duration of human gestation from fertilisation to parturition?",
                "options": [
                    "3 months (90 days)",
                    "Approximately 9 months (38–40 weeks or ~280 days)",
                    "15 months (450 days)",
                    "2 years"
                ],
                "correct": 1,
                "explanation": "The human gestation period lasts approximately 9 calendar months, equivalent to 38 to 40 weeks or roughly 280 days calculated from the last menstrual period."
            }
        ]
    },

    # Slide 12: Genetic Variations: The Evolutionary Fuel of Sexual Reproduction (C-3.3)
    {
        "id": 12,
        "title": "Genetic Variations: The Evolutionary Fuel of Sexual Reproduction",
        "subtitle": "Meiotic Crossing Over, Reassortment, and Niche Resilience vs Clonal Stagnation",
        "narration": "Why did sexual reproduction evolve if asexual reproduction is significantly faster and energetically less expensive? The definitive answer is Genetic Variation! In asexual reproduction, offspring are near-exact genetic clones of their single parent. If a sudden catastrophic shift occurs in their ecological niche—such as unprecedented global warming, a drought, or a virulent bacterial pathogen—an entire clonal population can be wiped out instantly because every individual shares the exact same genetic vulnerabilities. In contrast, sexual reproduction incorporates two parents and deploys meiosis: during meiotic crossing over, homologous chromosomes exchange genetic segments, and maternal and paternal chromosomes assort independently. When genetically unique sperm and egg combine, the resulting offspring display an extraordinary spectrum of diverse combinations. If environmental adversity strikes, some variant individuals possess fortuitous adaptations to survive and reproduce. Thus, variation is not an error—it is the indispensable evolutionary fuel of natural selection and species survival!",
        "points": [
            "<strong>Asexual Clonal Vulnerability:</strong> Genetically uniform clonal populations lack phenotypic diversity, leaving them susceptible to catastrophic extinction under abrupt environmental stress or pathogens.",
            "<strong>Triad of Sexual Variation (C-3.3):</strong> (1) Meiotic crossing over (homologous genetic recombination); (2) Independent assortment of chromosomes; (3) Random gametic fertilization generating astronomical unique combinations ($>70\\text{ trillion}$ in humans!).",
            "<strong>Niche Resilience & Adaptation:</strong> Genetic variants in a sexually reproducing population ensure that at least some individuals survive novel diseases, climatic extremes, or habitat shifts.",
            "<strong>Substrate for Natural Selection:</strong> Variation provides the phenotypic diversity upon which environmental natural selection acts, driving speciation and macroevolutionary adaptation over geological epochs."
        ],
        "checkpoints": [
            {
                "question": "Which of the following cellular mechanisms generates novel genetic combinations during sexual reproduction (C-3.3)?",
                "options": [
                    "Simple mitosis without chromosomal pairing",
                    "Crossing over between homologous chromosomes and independent assortment during meiosis",
                    "Binary fission in prokaryotes",
                    "Budding in yeast cells"
                ],
                "correct": 1,
                "explanation": "Meiotic crossing over shuffles alleles between homologous non-sister chromatids, and independent assortment mixes maternal and paternal chromosomes into novel combinations."
            },
            {
                "question": "Why does a sexually reproducing population have a higher survival probability in a rapidly changing environment than an asexually reproducing clonal population?",
                "options": [
                    "Sexually reproducing organisms consume zero food during winter",
                    "Genetic variations ensure that some variant individuals possess traits enabling them to withstand novel environmental stresses, preventing total population collapse",
                    "Asexual organisms cannot divide when exposed to normal atmospheric nitrogen",
                    "Sexual reproduction produces millions of offspring every hour"
                ],
                "correct": 1,
                "explanation": "Clonal populations share identical vulnerabilities. In sexually reproducing populations, genetic diversity ensures some individuals carry alleles allowing survival under novel ecological pressures."
            }
        ]
    },

    # Slide 13: Reproductive Health, Hygiene & Sexually Transmitted Infections (C-5.2, C-7.2)
    {
        "id": 13,
        "title": "Reproductive Health, Hygiene & Sexually Transmitted Infections",
        "subtitle": "WHO Health Paradigm, Bacterial vs Viral STIs, and Environmental Toxicity Risks",
        "narration": "Reproductive health, as defined by the World Health Organization, encompasses a state of complete physical, mental, and social well-being in all matters relating to the reproductive system, its functions, and processes. A central facet of reproductive health is safeguarding against Sexually Transmitted Infections (STIs), which transmit through unprotected sexual intercourse. STIs fall into two major etiologies: Bacterial infections like Gonorrhea (caused by Neisseria gonorrhoeae) and Syphilis (Treponema pallidum), which can be treated and cured with targeted antibiotics if diagnosed early; and Viral infections like Genital Warts (Human Papillomavirus / HPV), Genital Herpes, and HIV-AIDS, which cause incurable, chronic immune or cellular damage. Maintaining personal hygiene and utilizing barrier contraception like condoms provides critical dual protection against STIs and unintended pregnancy. Furthermore, modern scientific inquiry (C-7.2) reveals that environmental toxins significantly threaten reproductive health: heavy metals like lead, cadmium, and mercury accumulate in gonadal tissues, inducing oxidative stress that drastically damages sperm DNA, impairs motility, and causes ovarian follicle apoptosis! Similarly, chronic scrotal heat exposure disrupts testicular thermoregulation, inducing germ cell apoptosis and male subfertility.",
        "points": [
            "<strong>WHO Definition of Reproductive Health:</strong> A holistic state of total physical, emotional, behavioral, and social well-being in all aspects relating to the reproductive system across one's lifespan.",
            "<strong>Bacterial STIs (Curable with Antibiotics):</strong> Gonorrhea (<em>Neisseria gonorrhoeae</em>) and Syphilis (<em>Treponema pallidum</em>); early diagnosis prevents pelvic inflammatory disease and systemic organ damage.",
            "<strong>Viral STIs (Incurable & Chronic):</strong> HIV-AIDS (infects CD4 T-lymphocytes), Genital Warts (HPV - linked to cervical cancer), and Genital Herpes; managed via lifelong antiretroviral therapy.",
            "<strong>Environmental Toxicity & Extreme Heat (C-7.2):</strong> Heavy metals (lead, cadmium, mercury) trigger oxidative stress and sperm DNA fragmentation; elevated scrotal temperatures (varicocele, foundry heat, long hot baths) severely suppress spermatogenesis."
        ],
        "checkpoints": [
            {
                "question": "Which of the following sexually transmitted infections is caused by a virus and cannot be cured with conventional antibiotic medications?",
                "options": [
                    "Syphilis",
                    "Gonorrhea",
                    "HIV-AIDS",
                    "Bacterial vaginosis"
                ],
                "correct": 2,
                "explanation": "HIV-AIDS is caused by a retrovirus (Human Immunodeficiency Virus) and cannot be cured by antibiotics, which target bacterial cell walls and bacterial ribosomes exclusively."
            },
            {
                "question": "How do environmental heavy metal pollutants like lead and cadmium harm human reproductive fertility (C-7.2)?",
                "options": [
                    "They turn reproductive organs into photosynthetic tissues",
                    "They accumulate in gonads, inducing reactive oxygen species (oxidative stress) that fragment sperm DNA and impair gamete viability",
                    "They speed up the menstrual cycle to occur every 3 hours",
                    "They convert male testosterone directly into pure calcium"
                ],
                "correct": 1,
                "explanation": "Heavy metals disrupt cellular redox balance, generating oxidative stress that damages sperm membranes, compromises motility, and induces DNA strand breaks in gametes."
            }
        ]
    },

    # Slide 14: Contraceptive Methodologies & Population Dynamics (C-5.2)
    {
        "id": 14,
        "title": "Contraceptive Methodologies & Population Dynamics",
        "subtitle": "Barrier, Hormonal, Intrauterine, and Surgical Strategies for Family Planning",
        "narration": "As global human population surges, family planning and contraception become paramount for maternal health, child welfare, and ecological sustainability. Contraception refers to the deliberate prevention of conception or pregnancy through various scientific methodologies. Modern contraceptives are categorized into four distinct groups. First, Mechanical Barrier Methods: male and female condoms, diaphragms, and cervical caps prevent physical entry of sperms into the female tract; condoms hold the unique advantage of protecting against both unintended pregnancy AND sexually transmitted infections! Second, Chemical / Hormonal Methods: oral contraceptive pills containing synthetic estrogen and progesterone alter the hormonal axis to suppress ovulation; though highly effective, they do not prevent STIs and may have metabolic side effects. Third, Intrauterine Devices (IUDs): clinical devices like Copper-T inserted into the uterus release copper ions that suppress sperm motility and inhibit endometrial blastocyst implantation. Fourth, Surgical / Permanent Methods: Vasectomy in males (cutting and tying the vas deferens) and Tubectomy in females (cutting and ligating the fallopian tubes) provide irreversible, highly reliable sterilization by blocking gamete transit.",
        "points": [
            "<strong>Four Contraceptive Modalities (C-5.2):</strong> Barrier methods, Chemical/Hormonal methods, Intrauterine Devices (IUDs), and Surgical permanent sterilization.",
            "<strong>Barrier Methods (Dual Protection):</strong> Condoms (male and female) physically block sperm transport and represent the only contraceptive modality that simultaneously protects against STIs like HIV.",
            "<strong>Hormonal Contraceptive Pills:</strong> Oral synthetic hormone regimens alter endocrine feedback to inhibit pituitary FSH/LH release, preventing ovulation and thickening cervical mucus.",
            "<strong>Intrauterine Devices (Copper-T):</strong> Medically inserted into the uterus; releases copper ions that act as spermicides and alter endometrial receptivity to prevent blastocyst implantation.",
            "<strong>Surgical Sterilization (Vasectomy & Tubectomy):</strong> Vasectomy cuts and ligates the vas deferens in males; Tubectomy cuts and ligates the fallopian tubes in females, permanently blocking gamete transport."
        ],
        "checkpoints": [
            {
                "question": "Which contraceptive method provides the unique dual benefit of preventing unintended pregnancy while simultaneously shielding against sexually transmitted infections (STIs)?",
                "options": [
                    "Oral contraceptive pills",
                    "Copper-T intrauterine device",
                    "Mechanical barrier methods like condoms",
                    "Tubectomy surgical ligation"
                ],
                "correct": 2,
                "explanation": "Condoms physically prevent contact with bodily fluids and skin lesions, offering dual protection against both pregnancy and sexually transmitted infections."
            },
            {
                "question": "What is the physiological mechanism of action of the Copper-T intrauterine device (IUD)?",
                "options": [
                    "It stops the male from producing testosterone",
                    "It releases copper ions that suppress sperm motility and fertilising capacity, and alters the endometrium to prevent implantation",
                    "It freezes the ovaries to stop egg production permanently",
                    "It dissolves all chromosomes inside the sperm"
                ],
                "correct": 1,
                "explanation": "Copper ions released by Copper-T exert a toxic spermicidal effect, suppress sperm motility, and cause an endometrial inflammatory reaction that prevents blastocyst implantation."
            }
        ]
    },

    # Slide 15: Assisted Reproductive Technologies (ART) & Modern Clinical Interventions (C-7.1)
    {
        "id": 15,
        "title": "Assisted Reproductive Technologies (ART) & Modern Clinical Interventions",
        "subtitle": "IVF, ICSI, IUI, and Cryopreservation: Overcoming Infertility Barriers",
        "narration": "Infertility—the inability to conceive after 12 months of regular, unprotected intercourse—affects roughly 10 to 15 percent of couples worldwide due to male factors, female factors, or unexplained causes. Today, breakthroughs in Assisted Reproductive Technologies (ART) offer miraculous clinical solutions! The flagship technique is IVF (In Vitro Fertilisation), popularized as the 'test-tube baby' technique: mature ova harvested from the female's ovaries are fertilised with sperm outside the body in a sterile culture dish; the resulting zygote or early blastocyst is then transferred into the woman's uterus for implantation. In cases of severe male factor infertility (such as extremely low sperm count or poor motility), specialists deploy ICSI (Intracytoplasmic Sperm Injection), where a single viable sperm is micro-injected directly into the cytoplasm of an ovum using a microscopic robotic needle! Other modalities include IUI (Intrauterine Insemination), where concentrated washed sperm is placed directly into the uterine cavity, as well as gamete and embryo cryopreservation in liquid nitrogen at -196 °C for future use.",
        "points": [
            "<strong>Clinical Scope of ART (C-7.1):</strong> Specialized medical interventions designed to overcome physical blockages, ovulatory disorders, or sperm deficiencies causing clinical infertility.",
            "<strong>In Vitro Fertilisation (IVF):</strong> Ova and sperm are fertilised extracorporeally in specialized incubators; resulting embryos are monitored and transferred back to the uterus for gestation.",
            "<strong>Intracytoplasmic Sperm Injection (ICSI):</strong> Precision micromanipulation where a single selected spermatozoon is injected directly into an oocyte, overcoming severe oligospermia or asthenospermia.",
            "<strong>Intrauterine Insemination (IUI) & Cryopreservation:</strong> IUI concentrates motile sperm directly into the uterine fundus; cryobanking preserves gametes and embryos in liquid nitrogen ($-196^\\circ\\text{C}$) indefinitely."
        ],
        "checkpoints": [
            {
                "question": "What procedure defines In Vitro Fertilisation (IVF) as an Assisted Reproductive Technology (C-7.1)?",
                "options": [
                    "Surgical removal of both ovaries to cure diabetes",
                    "Harvesting mature ova and sperm to achieve fertilisation outside the body in a laboratory dish, followed by embryo transfer to the uterus",
                    "Injecting cow hormones directly into human bone marrow",
                    "Using magnets to speed up sperm swimming in the bloodstream"
                ],
                "correct": 1,
                "explanation": "IVF involves extracorporeal fertilisation where eggs and sperm combine in an incubator dish, and the resulting embryo is transferred into the maternal uterus for gestation."
            },
            {
                "question": "Under what clinical circumstances is Intracytoplasmic Sperm Injection (ICSI) specifically recommended over conventional IVF?",
                "options": [
                    "When the mother has twin pregnancies",
                    "In severe male-factor infertility involving very low sperm counts, abnormal morphology, or inability of sperm to penetrate the ovum coat",
                    "When the father has normal sperm count and perfect motility",
                    "When parents want to choose the eye color of the baby"
                ],
                "correct": 1,
                "explanation": "ICSI bypasses the sperm's need to penetrate the outer zona pellucida by micro-injecting a single selected sperm directly into the ooplasm, resolving severe male-factor barriers."
            }
        ]
    },

    # Slide 16: Indian Scientific Pioneers: Acharya Sushruta & Prof. Panchanan Maheshwari (C-6.1)
    {
        "id": 16,
        "title": "Indian Scientific Pioneers: Acharya Sushruta & Prof. Panchanan Maheshwari",
        "subtitle": "Ancient Dissection & Embryology (Sushruta) and Landmark Plant Embryo Culture (Maheshwari)",
        "narration": "India has contributed monumental milestones to both animal and plant reproductive sciences! In antiquity, Acharya Sushruta (circa 6th century BCE), revered as the 'Father of Surgery', authored the celebrated Sushruta Samhita. In the treatise's Sharira Sthana section, Sushruta provided the world's earliest systematic treatises on human anatomy and human embryology, termed Garbha-Sharira. He pioneered non-destructive anatomical dissection by immersing cadavers in slow-flowing river water and peeling tissue layers with soft bamboo whisks. He meticulously documented the monthly embryological development of the fetus, identifying the fusion of Sukra (sperm) and Sonita (ovum) as the genesis of life! In modern biological history, Professor Panchanan Maheshwari (1904–1966) stands as a giant of world botany. Working at the University of Delhi, he established India as the global capital for plant embryology. In 1950, he published the seminal international text 'An Introduction to the Embryology of Angiosperms'. Most famously, Prof. Maheshwari pioneered in vitro fertilisation of ovules and test-tube fertilisation in angiosperms, bypassing natural cross-pollination barriers and laying the foundational bedrock of plant tissue culture research in India!",
        "points": [
            "<strong>Acharya Sushruta (Ancient Anatomist & Embryologist):</strong> Author of <em>Sushruta Samhita</em> (~6th century BCE); formulated <em>Sharira Sthana</em> (human anatomy and <em>Garbha-Sharira</em> embryology), documenting fertilization of <em>Sukra</em> (sperm) and <em>Sonita</em> (ovum) and monthly fetal milestones.",
            "<strong>Pioneering Anatomical Dissection:</strong> Invented immersion dissection (*Avamarthana*) using natural water immersion and brush exploration to study internal organs centuries ahead of western anatomists.",
            "<strong>Prof. Panchanan Maheshwari (Father of Modern Indian Plant Embryology):</strong> Renowned University of Delhi botanist whose 1950 textbook became the global definitive reference on Angiosperm embryology.",
            "<strong>In Vitro Ovule Fertilisation Breakthrough:</strong> Pioneered test-tube fertilisation of angiosperm ovules on artificial culture media, laying the bedrock for haploid breeding, embryo rescue, and modern plant tissue culture in India."
        ],
        "checkpoints": [
            {
                "question": "Which ancient Indian medical treatise authored by Acharya Sushruta contains detailed classical descriptions of human anatomy and embryology (Garbha-Sharira)?",
                "options": [
                    "Arthashastra",
                    "Sushruta Samhita (Sharira Sthana)",
                    "Aryabhatiya",
                    "Surya Siddhanta"
                ],
                "correct": 1,
                "explanation": "The Sharira Sthana of the Sushruta Samhita is ancient India's foundational medical text on human anatomy, cadaveric dissection, and monthly embryological development."
            },
            {
                "question": "What major botanical breakthrough was achieved by Indian scientist Professor Panchanan Maheshwari at the University of Delhi?",
                "options": [
                    "Invention of chemical pesticides from coal tar",
                    "Pioneering in vitro fertilisation of angiosperm ovules and establishing plant embryological and tissue culture research in India",
                    "Discovery of the laws of animal heredity in pea plants",
                    "Classification of marine sharks in the Indian Ocean"
                ],
                "correct": 1,
                "explanation": "Prof. Panchanan Maheshwari pioneered test-tube in vitro fertilisation of ovules in seed plants and founded the school of plant embryology and tissue culture in India."
            }
        ]
    },

    # Slide 17: Dedicated Quiz Challenge 1 — Asexual & Floral Reproduction Mastery
    {
        "id": 17,
        "title": "Dedicated Quiz Challenge 1: Asexual & Floral Reproduction Mastery",
        "subtitle": "Test Your Knowledge on Fission, Budding, Flower Anatomy, Pollination, and Seed Biology",
        "narration": "Welcome to Quiz Challenge 1! Test your conceptual mastery of asexual modalities and angiosperm floral biology—including binary fission, Rhizopus spores, floral whorls, cross-pollination ecology, and double fertilisation. Select your chosen option for each question and inspect the step-by-step solutions.",
        "is_quiz": True,
        "quiz_title": "Asexual & Floral Reproduction Mastery Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. In which of the following organisms does binary fission take place along a fixed longitudinal plane relative to its whip-like flagellum?",
                "options": ["Amoeba", "Leishmania", "Rhizopus", "Planaria"],
                "correct": 1,
                "solution": "Leishmania, the protozoan parasite causing kala-azar, possesses a flagellum at one end and divides strictly along a defined longitudinal plane."
            },
            {
                "q": "2. Multiple fission inside a protective cyst under adverse conditions is characteristic of which organism?",
                "options": ["Hydra", "Plasmodium", "Spirogyra", "Bryophyllum"],
                "correct": 1,
                "solution": "Plasmodium, the malarial parasite, undergoes multiple fission within a cyst, dividing into dozens of daughter cells that release simultaneously upon rupture."
            },
            {
                "q": "3. The black bread mould Rhizopus reproduces asexually by forming microscopic resistant spores inside swollen structures called:",
                "options": ["Sporangia", "Conidia", "Buds", "Pollen sacs"],
                "correct": 0,
                "solution": "Rhizopus produces erect reproductive hyphae capped with swollen globular sporangia, within which hundreds of thick-walled spores develop."
            },
            {
                "q": "4. Vegetative propagation in Bryophyllum occurs naturally through adventitious buds produced on its:",
                "options": ["Roots", "Leaf marginal notches", "Bark", "Flower petals"],
                "correct": 1,
                "solution": "Bryophyllum leaves have marginal notches where dormant adventitious buds sprout into miniature plantlets with roots, which drop to the ground and grow."
            },
            {
                "q": "5. Which floral whorl constitutes the essential male reproductive organ in angiosperms?",
                "options": ["Calyx (sepals)", "Corolla (petals)", "Stamen / Androecium", "Pistil / Gynoecium"],
                "correct": 2,
                "solution": "The stamen (androecium) is the male organ, consisting of a filament supporting an anther that produces pollen grains housing male gametes."
            },
            {
                "q": "6. A flower that possesses both male stamens and female carpels within the same blossom (such as Hibiscus or Mustard) is termed:",
                "options": ["Unisexual", "Bisexual (Hermaphrodite)", "Staminate", "Pistillate"],
                "correct": 1,
                "solution": "Flowers that contain both stamens and pistils are bisexual (hermaphroditic), whereas flowers having only stamens or only pistils are unisexual."
            },
            {
                "q": "7. What adaptation is typical of flowers adapted for wind pollination (anemophily)?",
                "options": [
                    "Brightly colored petals with strong perfumed fragrance",
                    "Massive production of light, dry, non-sticky pollen and large feathery stigmas",
                    "Abundant sugary nectar rewards inside deep spurs",
                    "Thick sticky glue coating all petals"
                ],
                "correct": 1,
                "solution": "Wind-pollinated flowers produce millions of lightweight, aerodynamic pollen grains that float easily on air currents to land on large feathery receptive stigmas."
            },
            {
                "q": "8. What unique botanical event occurs when the second male gamete fuses with the two polar nuclei in an angiosperm embryo sac?",
                "options": ["Syngamy", "Triple Fusion forming triploid Endosperm ($3n$)", "Parthenogenesis", "Spore germination"],
                "correct": 1,
                "solution": "Triple fusion is the union of one haploid male gamete ($n$) with the two central polar nuclei ($2n$), generating triploid ($3n$) endosperm to nourish the embryo."
            },
            {
                "q": "9. Following fertilisation in flowering plants, the ovule and ovary develop into which mature structures respectively?",
                "options": [
                    "Ovule becomes Fruit; Ovary becomes Seed",
                    "Ovule becomes Seed; Ovary matures into Fruit",
                    "Ovule becomes Petal; Ovary becomes Calyx",
                    "Ovule becomes Embryo; Ovary becomes Stigma"
                ],
                "correct": 1,
                "solution": "The fertilised ovule develops a tough seed coat and matures into the Seed; the surrounding ovary walls ripen into the protective pericarp of the Fruit."
            },
            {
                "q": "10. How are the winged seeds of plants like drumstick and maple primarily dispersed across landscapes (C-4.3)?",
                "options": ["By wind currents", "By clinging to the fur of birds", "By explosive chemical detonation", "By sinking in fast rivers"],
                "correct": 0,
                "solution": "Winged seeds possess flattened aerodynamic extensions that catch wind currents, allowing them to glide and disperse across broad distances."
            }
        ]
    },

    # Slide 18: Dedicated Quiz Challenge 2 — Human Reproductive Systems & Hormones
    {
        "id": 18,
        "title": "Dedicated Quiz Challenge 2: Human Reproductive Systems & Hormones",
        "subtitle": "Test Your Knowledge on Male & Female Anatomy, Scrotal Thermoregulation, and Menstruation",
        "narration": "Welcome to Quiz Challenge 2! Evaluate your command over human reproductive anatomy and endocrinology—including testicular temperature regulation, sperm anatomy, fallopian fertilisation, and the hormonal stages of the 28-day menstrual cycle. Select your answers and review the solutions.",
        "is_quiz": True,
        "quiz_title": "Human Reproductive Anatomy & Hormones Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. Why are human testes situated outside the pelvic cavity inside the scrotum (C-7.2)?",
                "options": [
                    "To allow easier access for hormone absorption from sunlight",
                    "Because spermatogenesis requires a temperature $2\\text{--}2.5^\\circ\\text{C}$ cooler than normal core body temperature",
                    "To completely prevent testosterone from reaching the blood",
                    "To keep the testes frozen at zero degrees Celsius"
                ],
                "correct": 1,
                "explanation": "Human sperm production is temperature-sensitive and requires a cooler environment ($34.5\\text{--}35^\\circ\\text{C}$); the scrotum acts as an external thermal radiator."
            },
            {
                "q": "2. Which gland secretes an alkaline, nutrient-rich fluid that neutralizes vaginal acidity and activates sperm motility in semen?",
                "options": ["Thyroid gland", "Prostate gland and seminal vesicles", "Adrenal gland", "Pituitary gland"],
                "correct": 1,
                "solution": "The prostate gland and seminal vesicles produce alkaline secretions rich in fructose, enzymes, and buffers that nourish sperms and neutralize vaginal acidity."
            },
            {
                "q": "3. Which part of a human spermatozoon contains abundant spiral mitochondria that generate ATP energy for active swimming?",
                "options": ["Acrosome", "Middle piece", "Haploid nucleus", "Tail tip"],
                "correct": 1,
                "solution": "The middle piece of a sperm is densely packed with spiral mitochondria that produce the ATP needed to power flagellar wave motion."
            },
            {
                "q": "4. In the human female reproductive system, fertilisation of the ovum by a sperm typically occurs in the:",
                "options": ["Ovary", "Fallopian Tube (Oviduct)", "Uterus", "Vagina"],
                "correct": 1,
                "solution": "Fertilisation between a swimming sperm and a viable ovum strictly takes place in the ampulla of the Fallopian tube (oviduct)."
            },
            {
                "q": "5. What hormone secreted by ovarian follicles stimulates the development of female secondary sexual characteristics and endometrial proliferation?",
                "options": ["Testosterone", "Estrogen", "Adrenaline", "Insulin"],
                "correct": 1,
                "solution": "Estrogen, produced by developing ovarian follicles, drives female secondary sexual characteristics and stimulates the proliferation of the uterine endometrium."
            },
            {
                "q": "6. A sharp surge in which anterior pituitary hormone triggers ovulation (rupture of the follicle) around Day 14 of the menstrual cycle?",
                "options": ["Thyroid-stimulating hormone", "Luteinizing Hormone (LH)", "Growth Hormone", "Prolactin"],
                "correct": 1,
                "solution": "A dramatic mid-cycle surge in Luteinizing Hormone (LH surge) triggers the final maturation and rupture of the Graafian follicle, releasing the ovum."
            },
            {
                "q": "7. What endocrine structure is formed by the ruptured follicle following ovulation to secrete progesterone?",
                "options": ["Corpus Luteum", "Placenta", "Graafian follicle", "Acrosome"],
                "correct": 0,
                "solution": "Following ovulation, the collapsed follicle transforms into the glandular Corpus Luteum, which secretes progesterone to maintain the uterine lining."
            },
            {
                "q": "8. What causes the onset of menstrual bleeding (menses) in a non-pregnant female around Day 28?",
                "options": [
                    "A massive surge in testosterone",
                    "Degeneration of the corpus luteum leading to a sharp drop in progesterone and estrogen",
                    "Rupture of the liver arteries",
                    "High levels of growth hormone"
                ],
                "correct": 1,
                "solution": "In the absence of fertilisation, the corpus luteum regresses, causing progesterone and estrogen levels to crash, leading to endometrial sloughing and bleeding."
            },
            {
                "q": "9. What is the role of the cap-like Acrosome located at the anterior tip of the sperm head?",
                "options": [
                    "It contains hydrolytic digestive enzymes that break down the outer zona pellucida coat of the ovum",
                    "It acts as a flashlight in the dark uterus",
                    "It stores fat for long-distance swimming",
                    "It produces female estrogen"
                ],
                "correct": 0,
                "solution": "The acrosome contains hyaluronidase and proteolytic enzymes that digest through the corona radiata and zona pellucida of the ovum to enable sperm entry."
            },
            {
                "q": "10. In human males, which duct transports sperms from the epididymis toward the urethra?",
                "options": ["Fallopian tube", "Vas Deferens", "Ureter", "Bile duct"],
                "correct": 1,
                "solution": "The vas deferens is the muscular tube that conducts sperms from the storage epididymis around the bladder to join the urethra."
            }
        ]
    },

    # Slide 19: Dedicated Quiz Challenge 3 — Embryology, Contraception & Reproductive Health
    {
        "id": 19,
        "title": "Dedicated Quiz Challenge 3: Embryology, Contraception & Reproductive Health",
        "subtitle": "Test Your Knowledge on Implantation, Placental Exchange, Contraceptives, and Toxicity",
        "narration": "Welcome to Quiz Challenge 3! Delve into embryological development, blastocyst implantation, placental gas and nutrient exchange, modern contraceptive mechanisms, STIs, and environmental fertility threats. Answer every question and check the step-by-step solutions.",
        "is_quiz": True,
        "quiz_title": "Embryology, Contraception & Reproductive Health Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. What is the hollow, multicellular sphere of cells that embeds into the uterine endometrium approximately 7 days after fertilisation called?",
                "options": ["Zygote", "Blastocyst", "Fetus", "Pollen grain"],
                "correct": 1,
                "solution": "Following mitotic cleavage of the zygote, the embryo reaches the uterus as a hollow sphere called a Blastocyst, which embeds into the endometrium (implantation)."
            },
            {
                "q": "2. Which specialized vascular organ mediates the diffusion of nutrients and oxygen to the fetus and removes fetal carbon dioxide and urea?",
                "options": ["Placenta", "Amniotic sac alone", "Corpus luteum", "Fimbriae"],
                "correct": 0,
                "solution": "The placenta contains chorionic villi bathed in maternal blood sinuses, facilitating nutrient and respiratory gas exchange while transferring metabolic wastes away."
            },
            {
                "q": "3. Which of the following is a permanent surgical method of contraception performed in human males?",
                "options": ["Tubectomy", "Vasectomy", "Copper-T insertion", "Oral pill administration"],
                "correct": 1,
                "solution": "Vasectomy is the minor surgical procedure in males where a small section of both vasa deferentia is excised and tied off, preventing sperms from entering semen."
            },
            {
                "q": "4. What is the surgical sterilization procedure in females where the fallopian tubes are cut and ligated?",
                "options": ["Tubectomy", "Vasectomy", "Amniocentesis", "Dialysis"],
                "correct": 0,
                "solution": "Tubectomy involves cutting and ligating a portion of both fallopian tubes, permanently blocking the passage of ova and preventing sperm from encountering the egg."
            },
            {
                "q": "5. Which contraceptive device is unique in offering effective protection against both unintended pregnancy AND Sexually Transmitted Infections (STIs)?",
                "options": ["Oral contraceptive pills", "Condoms (mechanical barriers)", "Copper-T", "Emergency morning-after pills"],
                "correct": 1,
                "solution": "Condoms physically prevent direct mucosal contact and exchange of infected bodily fluids, providing dual protection against pregnancy and STIs like HIV."
            },
            {
                "q": "6. How do hormonal oral contraceptive pills prevent pregnancy in human females?",
                "options": [
                    "They surgically block the fallopian tubes",
                    "They alter systemic hormone levels to suppress pituitary FSH and LH, thereby inhibiting ovulation",
                    "They destroy all egg cells in the ovaries permanently",
                    "They turn vaginal secretions into pure alcohol"
                ],
                "correct": 1,
                "solution": "Oral contraceptive pills contain synthetic progesterone and estrogen that exert negative feedback on the pituitary gland, suppressing the FSH/LH surge and preventing ovulation."
            },
            {
                "q": "7. How does an intrauterine device like Copper-T function to prevent pregnancy?",
                "options": [
                    "It stops the heartbeat of the mother",
                    "It releases copper ions that suppress sperm motility and induces an endometrial reaction preventing implantation",
                    "It converts the uterus into an ovary",
                    "It produces testosterone in the female"
                ],
                "correct": 1,
                "explanation": "Copper ions exert a spermicidal effect, diminishing sperm motility and viability, and evoke an inflammatory response in the endometrium that prevents blastocyst implantation."
            },
            {
                "q": "8. Which of the following sexually transmitted diseases is caused by a bacterial infection and can be successfully cured with antibiotics?",
                "options": ["HIV-AIDS", "Syphilis", "Genital Warts (HPV)", "Genital Herpes"],
                "correct": 1,
                "solution": "Syphilis is caused by the spirochete bacterium Treponema pallidum and can be cured with antibiotics like penicillin if diagnosed early."
            },
            {
                "q": "9. How does occupational exposure to heavy metals like lead and cadmium harm human reproductive capacity (C-7.2)?",
                "options": [
                    "They cause reactive oxygen species (ROS) formation, inducing oxidative damage to sperm DNA and reducing motility",
                    "They convert female eggs into male sperms",
                    "They turn semen into solid bone",
                    "They eliminate all chromosomes from red blood cells"
                ],
                "correct": 0,
                "solution": "Lead and cadmium induce oxidative stress in reproductive tissues, causing lipid peroxidation of sperm membranes, motility loss, and sperm DNA fragmentation."
            },
            {
                "q": "10. What effect does chronic elevated temperature in the scrotal area (e.g., from tight synthetic clothing, varicocele, or foundry work) have on male fertility (C-7.2)?",
                "options": [
                    "It increases sperm count by 500%",
                    "It elevates scrotal temperature above the optimal $34.5\\text{--}35^\\circ\\text{C}$ range, causing germ cell apoptosis and severe reduction in sperm count",
                    "It speeds up sperm swimming by ten times",
                    "It converts testosterone into insulin"
                ],
                "correct": 1,
                "solution": "Spermatogenic germ cells require a temperature $2\\text{--}2.5^\\circ\\text{C}$ lower than core body heat; prolonged elevated heat induces germ cell death and subfertility."
            }
        ]
    },

    # Slide 20: Dedicated Quiz Challenge 4 — Comprehensive Competency Master Quiz
    {
        "id": 20,
        "title": "Dedicated Quiz Challenge 4: Comprehensive Competency Master Quiz",
        "subtitle": "Synthesizing Genetic Variation, Assisted Reproduction (ART), and Indian Science History",
        "narration": "Congratulations on reaching the final Quiz Challenge! This master challenge evaluates your synthesis of genetic variation mechanisms, modern clinical Assisted Reproductive Technologies (IVF/ICSI), and the monumental contributions of ancient and modern Indian scientists. Complete every question and examine the thorough solutions.",
        "is_quiz": True,
        "quiz_title": "Comprehensive Competency Master Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. Why does sexual reproduction provide a distinct evolutionary advantage over asexual cloning in a changing global climate (C-3.3)?",
                "options": [
                    "It requires fewer enzymes for protein synthesis",
                    "It generates high genetic variation through meiotic recombination and gametic fusion, enabling some individuals to survive environmental changes",
                    "It eliminates the need for water in biological tissues",
                    "It makes organisms completely immune to all bacteria"
                ],
                "correct": 1,
                "solution": "Genetic diversity produced by meiotic crossing over and random fertilization ensures a heterogeneous population where some variants carry adaptations to survive environmental shifts."
            },
            {
                "q": "2. In an Assisted Reproductive Technology (ART) clinic, what procedure involves micro-injecting a single selected sperm directly into an ovum (C-7.1)?",
                "options": ["Intracytoplasmic Sperm Injection (ICSI)", "Tubectomy", "Vasectomy", "Amniocentesis"],
                "correct": 0,
                "solution": "ICSI (Intracytoplasmic Sperm Injection) uses micromanipulators to inject a single sperm directly into the cytoplasm of an oocyte, overcoming severe male factor infertility."
            },
            {
                "q": "3. What is the fundamental procedure involved in In Vitro Fertilisation (IVF) (C-7.1)?",
                "options": [
                    "Injecting cow milk into human blood",
                    "Fertilising mature harvested ova and sperms outside the maternal body in an incubator dish, followed by embryo transfer to the uterus",
                    "Performing surgery to remove the placenta",
                    "Freezing the mother at sub-zero temperatures"
                ],
                "correct": 1,
                "solution": "IVF achieves fertilisation outside the body in vitro under controlled laboratory conditions, culturing the resulting embryo before uterine embryo transfer."
            },
            {
                "q": "4. Which ancient Indian medical pioneer authored the Sushruta Samhita, detailing early accounts of human anatomy and embryology (Garbha-Sharira) (C-6.1)?",
                "options": ["Charaka", "Acharya Sushruta", "Panini", "Aryabhata"],
                "correct": 1,
                "solution": "Acharya Sushruta (~6th century BCE), renowned as the Father of Surgery, authored the Sushruta Samhita with extensive chapters on human anatomy and fetal embryology in Sharira Sthana."
            },
            {
                "q": "5. What pioneering botanical breakthrough was achieved by Indian scientist Professor Panchanan Maheshwari at the University of Delhi (C-6.1)?",
                "options": [
                    "Discovery of the light-dependent reactions of photosynthesis",
                    "Pioneering in vitro fertilisation of angiosperm ovules and founding modern plant embryology and tissue culture in India",
                    "Synthesis of artificial chemical pesticides",
                    "Invention of mechanical tractors for farming"
                ],
                "correct": 1,
                "solution": "Prof. Panchanan Maheshwari achieved test-tube in vitro fertilisation of ovules in seed plants, establishing India as a world leader in plant embryological and morphogenetic research."
            },
            {
                "q": "6. In flowering plants, what tissue is formed by the union of the second male gamete ($n$) with the two polar nuclei ($2n$)?",
                "options": ["Diploid Zygote", "Triploid Endosperm ($3n$)", "Haploid Testa", "Pollen Tube"],
                "correct": 1,
                "solution": "Triple fusion generates a triploid ($3n$) primary endosperm nucleus, which develops into nutritive endosperm tissue feeding the embryo."
            },
            {
                "q": "7. Match the following terms with their definitions: (A) Ovulation, (B) Implantation, (C) Parturition, (D) Syngamy.",
                "options": [
                    "(A) Release of egg from ovary; (B) Attachment of blastocyst to endometrium; (C) Childbirth; (D) Fusion of sperm and egg",
                    "(A) Childbirth; (B) Release of egg; (C) Fusion of sperm and egg; (D) Implantation",
                    "(A) Fusion of sperm and egg; (B) Childbirth; (C) Implantation; (D) Release of egg",
                    "(A) Implantation; (B) Fusion of gametes; (C) Release of egg; (D) Childbirth"
                ],
                "correct": 0,
                "solution": "Ovulation = release of egg from ovary; Implantation = blastocyst embedding in uterine wall; Parturition = childbirth; Syngamy = fertilization of sperm and egg."
            },
            {
                "q": "8. Which of the following is an abiotic pollinating agent that carries lightweight, dry pollen grains across fields (C-4.3)?",
                "options": ["Honeybee", "Wind", "Hummingbird", "Bat"],
                "correct": 1,
                "solution": "Wind is an abiotic pollinating agent (anemophily), whereas bees, birds, and bats are living biotic pollinating vectors."
            },
            {
                "q": "9. Why are simple asexual clones identical to their parents while sexually produced offspring are not?",
                "options": [
                    "Asexual reproduction involves only mitosis copying identical DNA, whereas sexual reproduction involves meiotic recombination of two distinct parental genomes",
                    "Asexual offspring have no DNA at all",
                    "Sexual offspring inherit chromosomes from only their father",
                    "Asexual reproduction occurs only in outer space"
                ],
                "correct": 0,
                "solution": "Asexual reproduction relies on mitotic duplication of a single parental genome (cloning), while sexual reproduction combines two different parental genomes via meiosis and fertilization."
            },
            {
                "q": "10. At what temperature are human gametes and early embryos cryopreserved in liquid nitrogen for Assisted Reproductive Technology (C-7.1)?",
                "options": [
                    "$0^\\circ\\text{C}$",
                    "$-20^\\circ\\text{C}$",
                    "$-196^\\circ\\text{C}$",
                    "$-50^\\circ\\text{C}$"
                ],
                "correct": 2,
                "solution": "Cryopreservation uses liquid nitrogen at $-196^\\circ\\text{C}$ to vitrify gametes and embryos, arresting all metabolic activity and halting biological aging indefinitely."
            }
        ]
    }
]

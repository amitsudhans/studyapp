"""
Data definitions for NCERT Class 9 Science Chapter 4: Diversity in Living Organisms
Covers Importance of Classification, Whittaker's Five Kingdoms, Carl Woese's Three Domains,
Plant Divisions (Thallophyta to Angiosperms, Monocots vs Dicots),
Animal Phyla (Porifera to Chordata, Coelom Architecture), Lichen Symbiosis,
Binomial Nomenclature (Linnaean Rules & Local Surroundings), and Acellular Viruses/Viroids/Prions.
Syllabus Competencies: C-2.8, C-4.1, C-7.1.
"""

SLIDES_DATA = [
    # Slide 1: Introduction to Biodiversity & The Need for Classification
    {
        "id": 1,
        "title": "Introduction to Biodiversity & The Need for Classification",
        "subtitle": "Unlocking the Vast Tree of Life: From Microscopic Bacteria to Giant Blue Whales",
        "narration": "Welcome students to the magnificent world of Diversity in Living Organisms! Earth is home to an extraordinary spectrum of life—over 1.7 million species have been scientifically documented, ranging from microscopic bacteria barely 1 micrometre in size to colossal blue whales spanning 30 metres and giant California redwoods towering over 100 metres! How can human beings study, comprehend, and conserve this staggering biodiversity without examining every single individual? The answer is biological classification! Classification is the systematic grouping of organisms into distinct categories based on similarities, structural differences, and evolutionary lineages. Carolus Linnaeus established the hierarchical framework of taxonomy, descending from the broad Kingdom down through Phylum, Class, Order, Family, Genus, to the basic unit of life—the Species. Let us explore the scientific architecture that organizes the living world!",
        "points": [
            "<strong>Immense Scale of Biodiversity:</strong> Earth harbors over 1.7 million described species exhibiting vast variations in size, lifespan, habitat, and physiological adaptations.",
            "<strong>Scientific Need for Classification:</strong> Essential to comprehend vast species diversity, deduce evolutionary phylogenetic relationships, and establish a universal standard of communication.",
            "<strong>The Linnaean Taxonomic Hierarchy:</strong> Descending rank framework: Kingdom $\\to$ Phylum (Animals) / Division (Plants) $\\to$ Class $\\to$ Order $\\to$ Family $\\to$ Genus $\\to$ Species.",
            "<strong>Species as the Fundamental Unit:</strong> A group of closely related individuals capable of freely interbreeding in nature to produce fertile, viable offspring."
        ],
        "checkpoints": [
            {
                "question": "What is the primary scientific purpose of classifying living organisms into taxonomic categories?",
                "options": [
                    "To prove that all organisms possess identical DNA sequences",
                    "To systematically comprehend vast species diversity and establish evolutionary relationships without examining each organism individually",
                    "To convert all wild animals into domesticated farm livestock",
                    "To eliminate the need for microscopic study in biology"
                ],
                "correct": 1,
                "explanation": "Classification enables biologists to study broad groups of organisms systematically, reveal common ancestral origins, and comprehend millions of species efficiently."
            },
            {
                "question": "Which taxonomic category represents the fundamental, basic unit of biological classification?",
                "options": [
                    "Phylum",
                    "Genus",
                    "Species",
                    "Order"
                ],
                "correct": 2,
                "explanation": "Species is the primary, fundamental unit of classification; individuals of a species share a common gene pool and interbreed to yield fertile offspring."
            }
        ]
    },

    # Slide 2: Fundamental Bases of Biological Classification
    {
        "id": 2,
        "title": "Fundamental Bases of Biological Classification",
        "subtitle": "Cellular Design, Body Organisation, Nutritional Modes, and Cell Wall Chemistry",
        "narration": "What biological criteria do scientists use to sort organisms into primary groups? Modern classification does not rely on superficial traits like habitat or size. Instead, it is anchored on four fundamental cellular and evolutionary characteristics. First: Cellular Complexity—is the cell Prokaryotic, possessing a primitive nucleoid lacking a nuclear envelope and membrane-bound organelles, or Eukaryotic, with a membrane-enclosed nucleus and compartmentalized organelles? Second: Body Organisation—is the organism Unicellular, executing all life functions in a single cell, or Multicellular, displaying tissue and organ-system division of labour? Third: Mode of Nutrition—is the organism Autotrophic, manufacturing organic food through photosynthesis with chlorophyll, or Heterotrophic, obtaining nutrition via saprophytic absorption or holozoic ingestion? Fourth: Cell Wall Presence and Chemistry—does it have a cellulosic wall like plants, a chitinous wall like fungi, a peptidoglycan wall like bacteria, or no wall at all like animals? These four pillars form the bedrock of taxonomy!",
        "points": [
            "<strong>Pillar 1: Cellular Complexity:</strong> Prokaryotic (primitive nucleoid, absent membrane-bound organelles, 70S ribosomes) vs Eukaryotic (true double-membrane nucleus, 80S ribosomes, compartmentalization).",
            "<strong>Pillar 2: Body Organisation:</strong> Unicellular organisms (autonomous single cell) vs Multicellular organisms (coordinated division of labour across tissues, organs, and organ systems).",
            "<strong>Pillar 3: Mode of Nutrition:</strong> Autotrophic (photosynthetic synthesis of carbohydrates) vs Heterotrophic (absorptive saprophytes, parasitic absorbers, and ingestive holozoic consumers).",
            "<strong>Pillar 4: Cell Wall Presence & Matrix:</strong> Present (cellulose in plants, chitin in fungi, peptidoglycan in bacteria) vs absent (animals lacking cell walls, permitting high mobility)."
        ],
        "checkpoints": [
            {
                "question": "Which of the following cellular features fundamentally distinguishes a prokaryotic organism from a eukaryotic organism?",
                "options": [
                    "Presence of a cell membrane",
                    "Absence of a membrane-enclosed nucleus and membrane-bound organelles in prokaryotes",
                    "Presence of genetic DNA",
                    "Capacity to divide and reproduce"
                ],
                "correct": 1,
                "explanation": "Prokaryotes lack a nuclear envelope around their genetic material (forming a nucleoid) and lack membrane-bound organelles like mitochondria and chloroplasts."
            },
            {
                "question": "Why is the mode of nutrition considered a foundational criterion for separating fungi from plants?",
                "options": [
                    "Plants are heterotrophic consumers, while fungi produce all atmospheric oxygen",
                    "Plants are autotrophic producers possessing chlorophyll, whereas fungi are heterotrophic saprophytes that absorb preformed nutrients",
                    "Fungi have no cell walls, while plants have bones",
                    "Fungi perform photosynthesis only in the dark"
                ],
                "correct": 1,
                "explanation": "Plants synthesize their own organic food using sunlight and chlorophyll, while fungi completely lack chlorophyll and must absorb nutrients as heterotrophic saprophytes."
            }
        ]
    },

    # Slide 3: Whittaker’s Five Kingdom System & Ecological Roles (C-4.1, C-2.8)
    {
        "id": 3,
        "title": "Whittaker’s Five Kingdom System & Ecological Roles",
        "subtitle": "Monera, Protista, Fungi, Plantae, and Animalia: The Global Trophic Web",
        "narration": "In 1969, American ecologist Robert H. Whittaker revolutionized biology by proposing the Five Kingdom Classification. Let us examine each kingdom and its ecological role! Kingdom 1: Monera—comprising all unicellular prokaryotes, including true bacteria and cyanobacteria (blue-green algae); they possess non-cellulosic walls and serve as vital nutrient cyclers and nitrogen fixers. Kingdom 2: Protista—comprising single-celled eukaryotes with diverse locomotion mechanisms like cilia in Paramecium, flagella in Euglena, and pseudopodia in Amoeba. Kingdom 3: Fungi—multicellular heterotrophic eukaryotes with cell walls reinforced with Chitin; they secrete digestive enzymes to absorb decaying organic matter as Saprophytes, serving as nature's primary Decomposers. Kingdom 4: Plantae—multicellular photosynthetic autotrophs with cellulosic cell walls, serving as the Earth's primary Producers. Kingdom 5: Animalia—multicellular, holozoic heterotrophs lacking cell walls, possessing sensory nerve systems and active locomotion, serving as Consumers. Together, these five kingdoms drive the biogeochemical cycles of our planet!",
        "points": [
            "<strong>Kingdom Monera (Prokaryotes):</strong> Unicellular, non-cellulosic peptidoglycan walls; includes heterotrophic bacteria, nitrogen-fixing Rhizobium, and photosynthetic cyanobacteria.",
            "<strong>Kingdom Protista (Unicellular Eukaryotes):</strong> Microscopic eukaryotes including protozoans (Amoeba, Paramecium), photosynthetic diatoms, and flagellated Euglena.",
            "<strong>Kingdom Fungi (Chitinous Decomposers):</strong> Heterotrophic saprophytes/parasites with cell walls composed of tough <strong>Chitin</strong> (e.g., bread mould Rhizopus, Penicillium, edible Agaricus mushrooms).",
            "<strong>Kingdom Plantae & Animalia:</strong> Plantae are primary autotrophic Producers with cellulose walls; Animalia are multicellular Consumers lacking walls, characterized by ingestion and motility.",
            "<strong>Ecological Trophic Cycle (C-2.8):</strong> Producers (Plantae) $\\to$ Consumers (Animalia) $\\to$ Decomposers (Fungi & Monera) continuously recycling vital chemical elements."
        ],
        "checkpoints": [
            {
                "question": "What complex carbohydrate polymer forms the cell wall of organisms in Kingdom Fungi?",
                "options": [
                    "Cellulose",
                    "Chitin",
                    "Peptidoglycan",
                    "Glycogen"
                ],
                "correct": 1,
                "explanation": "Fungal cell walls are composed of chitin—a tough, nitrogen-containing polysaccharide distinct from the cellulose found in plant cell walls."
            },
            {
                "question": "What is the primary ecological role fulfilled by organisms belonging to Kingdom Fungi and Kingdom Monera in an ecosystem (C-2.8)?",
                "options": [
                    "Primary Producers capturing solar energy",
                    "Apex Carnivore Consumers hunting herbivores",
                    "Decomposers breaking down dead organic matter and recycling mineral nutrients",
                    "Inert mineral rocks providing physical shelter"
                ],
                "correct": 2,
                "explanation": "Fungi and bacteria decompose dead organisms and organic wastes, returning essential carbon, nitrogen, and phosphorus minerals back to the soil and atmosphere."
            }
        ]
    },

    # Slide 4: Carl Woese's Three Domains of Life on Molecular Basis (C-7.1)
    {
        "id": 4,
        "title": "Carl Woese's Three Domains of Life on Molecular Basis",
        "subtitle": "The 16S/18S rRNA Phylogenetic Revolution: Archaea, Bacteria, and Eukarya",
        "narration": "In 1990, American microbiologist Carl Woese shattered traditional classifications by introducing the Three Domains of Life based on deep molecular phylogenetic analysis. Instead of comparing physical traits, Woese sequenced the universal gene coding for ribosomal RNA—16S rRNA in prokaryotes and 18S rRNA in eukaryotes. Because all living ribosomes perform translation, rRNA changes extraordinarily slowly, acting as a molecular clock! Woese discovered that Kingdom Monera actually consists of two profoundly different evolutionary lineages: Domain Archaea and Domain Bacteria, alongside Domain Eukarya. Domain Archaea contains ancient extremophiles with unique ether-linked branched lipid cell membranes: Methanogens producing marsh gas, Halophiles flourishing in saturated brine lakes, and Thermoacidophiles thriving in boiling volcanic acid springs at 100 degrees Celsius! Remarkably, molecular sequences prove that Archaea share a closer common ancestor with us—Domain Eukarya—than with true Bacteria!",
        "points": [
            "<strong>The rRNA Molecular Clock (C-7.1):</strong> Carl Woese (1990) utilized 16S and 18S ribosomal RNA nucleotide sequence divergence to reconstruct the deepest universal evolutionary lineages of life.",
            "<strong>Domain Archaea (Ancient Extremophiles):</strong> Possess unique ether-linked branched lipid membranes; thrive in hostile niches: Methanogens (anaerobic gut/bogs), Halophiles (salt lakes), Thermoacidophiles (hot acid vents).",
            "<strong>Domain Bacteria (True Eubacteria):</strong> Prokaryotes with ester-linked unbranched lipids and peptidoglycan walls (e.g., cyanobacteria, E. coli, soil nitrogen-fixers).",
            "<strong>Domain Eukarya:</strong> Encompasses all organisms possessing true membrane-bound nuclei and 80S cytosolic ribosomes (Protista, Fungi, Plantae, and Animalia).",
            "<strong>Evolutionary Insight:</strong> Archaea and Eukarya share common transcriptional and translational proteins, proving they are sister evolutionary clades."
        ],
        "checkpoints": [
            {
                "question": "What molecular biomarker did Carl Woese sequence to establish the Three Domains of biological classification (C-7.1)?",
                "options": [
                    "Hemoglobin protein chains",
                    "16S and 18S ribosomal RNA (rRNA) gene sequences",
                    "Plant chlorophyll pigments",
                    "Calcium phosphate bone crystals"
                ],
                "correct": 1,
                "explanation": "Carl Woese analyzed the highly conserved nucleotide sequences of small subunit ribosomal RNA (16S rRNA in prokaryotes, 18S rRNA in eukaryotes) to uncover deepest evolutionary roots."
            },
            {
                "question": "Which of the following extremophile groups belongs to Domain Archaea and thrives in boiling acidic hot springs at temperatures near 100 °C?",
                "options": [
                    "Methanogens",
                    "Halophiles",
                    "Thermoacidophiles",
                    "Cyanobacteria"
                ],
                "correct": 2,
                "explanation": "Thermoacidophiles are specialized Archaea possessing ether-linked branched membrane lipids that maintain cellular integrity in scalding, highly acidic geothermal springs."
            }
        ]
    },

    # Slide 5: Symbiosis in Nature: Lichens & Mycorrhiza as Ecological Keystone Models (C-2.8)
    {
        "id": 5,
        "title": "Symbiosis in Nature: Lichens & Mycorrhiza as Ecological Keystone Models",
        "subtitle": "Mutualistic Cohabitation: Phycobionts, Mycobionts, and Pollution Bio-Monitoring",
        "narration": "Nature reveals extraordinary examples where different kingdoms intertwine in mutualistic harmony. A prime example is the Lichen. A lichen is not a single organism, but an intimate symbiotic partnership between two distinct kingdoms! The Phycobiont is an autotrophic green alga or cyanobacterium that manufactures carbohydrates through photosynthesis. The Mycobiont is a heterotrophic fungus—usually an ascomycete—that provides physical anchorage, shields the delicate alga from harsh sunlight, and absorbs water and atmospheric minerals. Lichens are ecological pioneers: they secrete organic acids that slowly crumble bare rock faces into mineral soil, initiating ecological succession. Crucially, lichens absorb atmospheric moisture directly and possess zero protective cuticles, making them hyper-sensitive to air pollutants like Sulfur Dioxide ($SO_2$). You will never find lichens growing in heavily polluted industrial cities; their disappearance serves as a biological early-warning system for airborne toxic smog!",
        "points": [
            "<strong>Anatomy of a Lichen (C-2.8):</strong> Obligate mutualistic symbiosis between a photosynthetic <strong>Phycobiont</strong> (alga or cyanobacterium) and a protective, absorbent <strong>Mycobiont</strong> (fungus).",
            "<strong>Reciprocal Metabolic Synergy:</strong> The alga synthesizes organic food via photosynthesis; the fungus furnishes moisture, structural shelter, mineral nutrients, and protection from UV radiation.",
            "<strong>Ecological Pioneers of Succession:</strong> Lichens colonize bare rocks, secreting lichen acids that weather granite into fertile soil, paving the way for mosses and vascular plants.",
            "<strong>Bio-Indicators of Air Pollution:</strong> Lacking a waxy cuticle, lichens readily absorb atmospheric sulfur dioxide ($SO_2$), leading to chlorophyll destruction; industrial areas form barren 'lichen deserts'."
        ],
        "checkpoints": [
            {
                "question": "What is the specific physiological contribution of the fungal partner (mycobiont) in a lichen symbiosis (C-2.8)?",
                "options": [
                    "It performs photosynthesis to manufacture sugars",
                    "It provides structural anchorage, physical shelter, and absorbs water and mineral nutrients from the atmosphere",
                    "It produces seeds that sprout into trees",
                    "It digests rocks using hydrochloric acid to generate electricity"
                ],
                "correct": 1,
                "explanation": "The fungal mycobiont forms the physical body of the lichen, protecting the photosynthetic alga from desiccation while absorbing ambient moisture and minerals."
            },
            {
                "question": "Why are lichens absent from industrial cities and recognized worldwide as biological pollution indicators?",
                "options": [
                    "City birds eat all lichens every morning",
                    "Lichens lack a protective waxy cuticle and are killed by low concentrations of airborne sulfur dioxide ($SO_2$) gas",
                    "Lichens cannot grow on concrete or stone",
                    "Traffic noise destroys fungal cell membranes"
                ],
                "correct": 1,
                "explanation": "Lichens absorb water and nutrients directly from the air; toxic sulfur dioxide ($SO_2$) from vehicular and coal emissions accumulates inside, poisoning the algal chlorophyll."
            }
        ]
    },

    # Slide 6: Plant Kingdom (Plantae): The Evolutionary Hierarchy
    {
        "id": 6,
        "title": "Plant Kingdom (Plantae): The Evolutionary Hierarchy",
        "subtitle": "Body Differentiation, Vascular Conduits, and Enclosed vs Naked Seeds",
        "narration": "Kingdom Plantae encompasses non-motile, multicellular photosynthetic autotrophs with cellulosic cell walls. Botanists classify plants using three major evolutionary milestones. Level 1: Body Differentiation—does the plant possess a simple, undifferentiated thallus body, or does it feature distinct roots, stems, and leaves? Level 2: Vascular Tissues—does the plant possess specialized conducting vascular bundles (Xylem for water and Phloem for food), or does it rely on slow cellular diffusion? Level 3: Seed Formation—does the plant reproduce via microscopic hidden spores (Cryptogamae), or does it produce visible, multi-cellular seeds with embryo reserves (Phanerogamae)? Furthermore, within seed-bearing phanerogams, are the seeds naked on cones (Gymnosperms), or are they securely enclosed inside ovaries that ripen into succulent protective fruits (Angiosperms)? Let us trace this magnificent evolutionary ascent!",
        "points": [
            "<strong>Evolutionary Classification Metric:</strong> Categorized sequentially based on: (1) thallus vs differentiated organs; (2) absence vs presence of vascular bundles; (3) spore-bearing vs seed-bearing habit; (4) naked vs fruit-enclosed seeds.",
            "<strong>Cryptogamae (Hidden Gametes / Non-Seed Plants):</strong> Thallophyta (Algae), Bryophyta (Mosses), and Pteridophyta (Ferns); reproduce using microscopic spores without forming flowers or seeds.",
            "<strong>Phanerogamae (Visible Seeds):</strong> Gymnosperms and Angiosperms; produce seeds containing an embryo and stored nutritive food reserves (endosperm/cotyledons).",
            "<strong>Naked vs Enclosed Seeds:</strong> Gymnosperms bear exposed seeds on woody cones; Angiosperms enclose seeds inside protective fruit walls derived from floral ovaries."
        ],
        "checkpoints": [
            {
                "question": "Which of the following plant divisions represents non-seed-bearing plants with hidden reproductive organs (Cryptogams)?",
                "options": [
                    "Angiosperms",
                    "Gymnosperms",
                    "Pteridophyta",
                    "Monocotyledons"
                ],
                "correct": 2,
                "explanation": "Pteridophyta (ferns) are cryptogams; they possess vascular tissues but reproduce via microscopic spores without forming flowers or seeds."
            },
            {
                "question": "What is the primary evolutionary advantage of producing seeds (Phanerogams) over microscopic spores (Cryptogams)?",
                "options": [
                    "Seeds contain a multicellular embryo equipped with stored food reserves enclosed in a protective coat, ensuring higher germination survival",
                    "Seeds are lighter than individual bacteria and float into outer space",
                    "Seeds allow plants to swim in rivers like fish",
                    "Seeds convert sunlight into nitrogen gas"
                ],
                "correct": 0,
                "explanation": "Seeds provide a ready supply of stored food (endosperm or cotyledons) and a resilient seed coat, shielding the embryo until conditions support germination."
            }
        ]
    },

    # Slide 7: Cryptogams: Thallophyta, Bryophyta & Pteridophyta
    {
        "id": 7,
        "title": "Cryptogams: Thallophyta, Bryophyta & Pteridophyta",
        "subtitle": "Algal Thalli, Amphibious Mosses, and the First Vascular Ferns",
        "narration": "Let us examine the three cryptogamic divisions. Division 1: Thallophyta, commonly known as Algae. Their body is an undifferentiated thallus lacking true roots, stems, leaves, and vascular tissues. They are predominantly aquatic, including Spirogyra with ribbon-like spiral chloroplasts, Ulothrix, Cladophora, and Chara. Division 2: Bryophyta, famously crowned the 'Amphibians of the Plant Kingdom'. Bryophytes, such as Funaria moss and Marchantia liverworts, have differentiated stem-like and leaf-like structures anchored by rhizoids. But why are they amphibians? Because while they live on terrestrial soil, they absolutely require a film of water for their flagellated male sperms to swim to the egg for sexual fertilisation! Division 3: Pteridophyta, the ferns! Pteridophytes are the evolutionary pioneers of the plant world—the first terrestrial plants to evolve true vascular tissues (Xylem and Phloem)! Their body is fully differentiated into true roots, stems, and feathery leaves called fronds, which bear spore-producing clusters called sori, as seen in Marsilea and Dryopteris.",
        "points": [
            "<strong>Thallophyta (Algae):</strong> Undifferentiated thallus body; aquatic habit; zero vascular tissues; autotrophic with diverse pigments (e.g., <em>Spirogyra</em>, <em>Ulothrix</em>, <em>Chara</em>).",
            "<strong>Bryophyta (Amphibians of Plant Kingdom):</strong> Differentiated into pseudo-stems, leaves, and rhizoids; lack true vascular tissues; strictly require water for flagellated sperm swimming during fertilization (e.g., <em>Funaria</em>, <em>Marchantia</em>, <em>Riccia</em>).",
            "<strong>Pteridophyta (First Vascular Plants):</strong> True roots, stems, and frond leaves; possess functional Xylem and Phloem conducting channels; reproduce via spore clusters (sori) on fronds (e.g., <em>Marsilea</em>, <em>Dryopteris</em>, <em>Equisetum</em>).",
            "<strong>Evolutionary Trajectory:</strong> Progressive transition from aquatic thalli without conduits (algae) to terrestrial vascular systems (ferns)."
        ],
        "checkpoints": [
            {
                "question": "Why are bryophytes (mosses and liverworts) classified as the 'Amphibians of the Plant Kingdom'?",
                "options": [
                    "They can transform into frogs during heavy rainfall",
                    "They grow on terrestrial soil but strictly depend on water for flagellated sperms to swim and achieve sexual fertilisation",
                    "They can breathe underwater using internal gills",
                    "They live exclusively inside the digestive tract of reptiles"
                ],
                "correct": 1,
                "explanation": "Like animal amphibians that must return to water to breed, bryophytes live on damp land but require a film of water for sperm transit to the female archegonium."
            },
            {
                "question": "Which plant group was the first in evolutionary history to develop true vascular tissues (xylem and phloem) for conducting water and nutrients?",
                "options": [
                    "Thallophyta",
                    "Bryophyta",
                    "Pteridophyta (Ferns)",
                    "Algae"
                ],
                "correct": 2,
                "explanation": "Pteridophytes were the first terrestrial plants to evolve specialized conducting vascular tissues (xylem and phloem), enabling larger upright growth."
            }
        ]
    },

    # Slide 8: Phanerogams: Gymnosperms vs Angiosperms (Monocots & Dicots)
    {
        "id": 8,
        "title": "Phanerogams: Gymnosperms vs Angiosperms (Monocots & Dicots)",
        "subtitle": "Conifer Naked Cones, Enclosed Floral Ovaries, and the Monocot/Dicot Divide",
        "narration": "Moving to seed-bearing Phanerogams, plants diverge into Gymnosperms and Angiosperms. In Gymnosperms (from Greek 'gymnos' meaning naked, and 'sperma' meaning seed), plants are perennial, evergreen, and woody, such as majestic pines (Pinus) and Cycas. Their ovules are not enclosed inside an ovary wall, so their seeds develop exposed on the scales of woody cones. In Angiosperms (from 'angeion' meaning vessel), true flowers evolve! Ovules reside inside an ovary chamber that ripens into a protective fruit. Angiosperms are further divided into two great classes based on their seed embryonic leaves: Monocotyledons, having seeds with a single cotyledon, parallel leaf venation, fibrous roots, and scattered stem vascular bundles, as seen in maize, wheat, and bamboo; and Dicotyledons, having seeds with two cotyledons, reticulate net-like leaf venation, a deep taproot system, and ring-arranged vascular bundles, as seen in peas, mangoes, and sunflowers!",
        "points": [
            "<strong>Gymnosperms (Naked Seeds):</strong> Perennial woody evergreens; non-flowering; naked ovules borne on scales of male and female cones; seeds lack fruit coverings (e.g., <em>Pinus</em>, <em>Cycas</em>, <em>Deodar</em>).",
            "<strong>Angiosperms (Flowering / Enclosed Seeds):</strong> Highly evolved floral organs; ovules enclosed inside ovaries that swell into fruits; divided into Monocots and Dicots.",
            "<strong>Monocotyledon Characteristics:</strong> 1 cotyledon in seed; parallel leaf venation; fibrous root system; trimerous flowers (e.g., maize, rice, wheat, grass, lily).",
            "<strong>Dicotyledon Characteristics:</strong> 2 cotyledons in seed; reticulate (net) leaf venation; deep taproot system; tetramerous or pentamerous flowers (e.g., gram, pea, sunflower, mustard, mango)."
        ],
        "checkpoints": [
            {
                "question": "What is the defining anatomical difference between gymnosperm seeds and angiosperm seeds?",
                "options": [
                    "Gymnosperm seeds are enclosed in fleshy fruits, while angiosperm seeds are naked",
                    "Gymnosperm seeds are naked and develop exposed on cone scales, whereas angiosperm seeds develop enclosed within an ovary wall that forms a fruit",
                    "Gymnosperm seeds contain three embryos, while angiosperm seeds contain none",
                    "Angiosperm seeds do not have a seed coat"
                ],
                "correct": 1,
                "explanation": "Gymnosperms bear exposed 'naked' seeds without an enclosing fruit wall; angiosperms enclose their seeds inside the mature fruit derived from the floral ovary."
            },
            {
                "question": "A student examines a plant displaying parallel leaf venation and a fibrous root system. How should this plant be classified?",
                "options": [
                    "Gymnosperm",
                    "Dicotyledon",
                    "Monocotyledon",
                    "Pteridophyte"
                ],
                "correct": 2,
                "explanation": "Parallel leaf venation, fibrous roots, and a single embryonic seed cotyledon are classic diagnostic hallmarks of Monocotyledonous angiosperms."
            }
        ]
    },

    # Slide 9: Animal Kingdom (Animalia): Taxonomic Criteria & Coelom Architecture
    {
        "id": 9,
        "title": "Animal Kingdom (Animalia): Taxonomic Criteria & Coelom Architecture",
        "subtitle": "Symmetry, Germ Layers, and the Crucial Evolution of the Body Cavity (Coelom)",
        "narration": "Kingdom Animalia encompasses multicellular, heterotrophic, holozoic eukaryotes lacking cell walls. To systematically classify animals across 10 major phyla, zoologists analyze four fundamental body plan criteria. First: Level of Organisation—cellular grade in sponges, tissue grade in cnidarians, or organ-system grade in flatworms to vertebrates? Second: Body Symmetry—asymmetrical like irregular sponges, radial like jellyfish (cut into identical halves in multiple planes), or bilateral like humans and insects (identical left and right halves along a single longitudinal plane)? Third: Germ Layers—diploblastic (two embryonic layers: ectoderm and endoderm) or triploblastic (three layers: ectoderm, mesoderm, and endoderm)? Fourth and most critical: the Coelom! The coelom is the fluid-filled body cavity between the gut wall and outer body wall, completely lined by mesodermal peritoneum. Acoelomates (flatworms) have no cavity. Pseudocoelomates (roundworms) have a false cavity with mesodermal pouches. Eucoelomates (earthworms, insects, humans) possess a true mesoderm-lined coelom that cushions internal organs!",
        "points": [
            "<strong>Four Foundational Animal Body Plan Criteria:</strong> Level of organisation, body symmetry, embryonic germ layer count, and coelom architecture.",
            "<strong>Symmetry Spectrum:</strong> Asymmetrical (sponges) $\\to$ Radial symmetry (Cnidaria, adult echinoderms) $\\to$ Bilateral symmetry (cephalization with head and bilateral sides).",
            "<strong>Germ Layers:</strong> Diploblastic (ectoderm + endoderm) vs Triploblastic (ectoderm + mesoderm + endoderm enabling complex muscle and organ development).",
            "<strong>Coelom Classification:</strong> (1) <strong>Acoelomates</strong>: solid mesenchyme, no cavity (Platyhelminthes); (2) <strong>Pseudocoelomates</strong>: false body cavity, mesodermal pouches (Nematoda); (3) <strong>Eucoelomates</strong>: true body cavity completely lined by mesodermal peritoneum (Annelids to Chordates)."
        ],
        "checkpoints": [
            {
                "question": "What is meant by the biological term 'true coelom' in animal anatomy?",
                "options": [
                    "A chamber inside the lungs for storing air",
                    "A fluid-filled internal body cavity situated between the gut and body wall that is completely lined by mesoderm-derived tissue",
                    "A hollow space inside bone marrow",
                    "The digestive stomach chamber in birds"
                ],
                "correct": 1,
                "explanation": "A true coelom (eucoelom) is an internal body cavity that arises within the embryonic mesoderm and is completely lined on all sides by mesodermal peritoneum."
            },
            {
                "question": "Which of the following animal groups is characterized by a 'pseudocoelom' where mesoderm occurs as scattered pouches rather than a continuous peritoneal lining?",
                "options": [
                    "Platyhelminthes (Flatworms)",
                    "Nematoda (Roundworms)",
                    "Annelida (Earthworms)",
                    "Arthropoda (Insects)"
                ],
                "correct": 1,
                "explanation": "Nematodes (roundworms like Ascaris) possess a pseudocoelom, where the body cavity is not completely lined by mesodermal epithelium."
            }
        ]
    },

    # Slide 10: Invertebrates I: Porifera, Coelenterata, Platyhelminthes & Nematoda
    {
        "id": 10,
        "title": "Invertebrates I: Porifera, Coelenterata, Platyhelminthes & Nematoda",
        "subtitle": "From Sponge Canal Systems and Stinging Cnidocytes to Flatworms and Parasitic Nematodes",
        "narration": "Let us explore the lower invertebrate phyla! Phylum 1: Porifera (Sponges). Sessile, non-motile marine animals at the cellular grade of organisation. Their body is perforated by thousands of microscopic pores called ostia leading into a central spongocoel and exiting via a large osculum; this water canal system brings oxygen and food while sweeping away wastes. Phylum 2: Coelenterata or Cnidaria. Aquatic animals at the tissue grade with radial symmetry and a gastrovascular cavity. Their tentacles bristle with specialized stinging cells called cnidocytes or nematocysts, firing toxin-loaded harpoons to paralyze prey and repel predators, seen in Hydra and jellyfish! Phylum 3: Platyhelminthes (Flatworms). Dorsoventrally flattened, bilateral, triploblastic, but acoelomate; they use specialized flame cells for excretion, as seen in free-living Planaria and parasitic tapeworms. Phylum 4: Nematoda (Roundworms). Cylindrical, unsegmented, pseudocoelomate worms with a complete tubular gut from mouth to anus, including intestinal Ascaris and Wuchereria bancrofti, the parasite causing elephantiasis!",
        "points": [
            "<strong>Porifera (Pore Bearers / Sponges):</strong> Cellular grade; sessile; perforated by ostia pores connected to a water canal system with choanocytes; spicule skeleton (e.g., <em>Sycon</em>, <em>Spongilla</em>).",
            "<strong>Coelenterata / Cnidaria (Stinging Tentacles):</strong> Tissue grade; radial symmetry; gastrovascular cavity with single opening; armed with <strong>cnidocytes (nematocysts)</strong> for defense/prey capture (e.g., <em>Hydra</em>, <em>Aurelia</em>/Jellyfish).",
            "<strong>Platyhelminthes (Flatworms):</strong> Dorsoventrally flattened; bilateral; triploblastic; <strong>acoelomate</strong>; possess flame cells for osmoregulation and excretion (e.g., <em>Planaria</em>, <em>Fasciola</em>/Liver fluke, <em>Taenia</em>).",
            "<strong>Nematoda (Roundworms):</strong> Cylindrical unsegmented body; bilateral; triploblastic; <strong>pseudocoelomate</strong>; complete alimentary canal (e.g., <em>Ascaris</em>, <em>Wuchereria</em> causing elephantiasis/filariasis)."
        ],
        "checkpoints": [
            {
                "question": "Which specialized cell type is deployed by Cnidarians (Coelenterates) like Hydra and jellyfish for defense and capturing prey?",
                "options": [
                    "Choanocytes (collar cells)",
                    "Cnidocytes containing stinging nematocyst capsules",
                    "Flame cells",
                    "Nephridia"
                ],
                "correct": 1,
                "explanation": "Cnidarians possess cnidocytes on their tentacles, which fire pressurized, venom-injecting barbed threads (nematocysts) to immobilize prey."
            },
            {
                "question": "Which parasitic roundworm belonging to Phylum Nematoda causes the chronic disfiguring human disease elephantiasis (filariasis)?",
                "options": [
                    "Taenia solium",
                    "Wuchereria bancrofti",
                    "Planaria",
                    "Fasciola hepatica"
                ],
                "correct": 1,
                "explanation": "Wuchereria bancrofti (filarial worm) is a parasitic nematode transmitted by mosquitoes that lodges in human lymphatic vessels, causing massive elephantiasis swelling."
            }
        ]
    },

    # Slide 11: Invertebrates II: Annelida, Arthropoda, Mollusca & Echinodermata
    {
        "id": 11,
        "title": "Invertebrates II: Annelida, Arthropoda, Mollusca & Echinodermata",
        "subtitle": "Metameric Rings, Jointed Exoskeletons, Mantle Shells, and Water Vascular Systems",
        "narration": "Next, we examine the advanced coelomate invertebrates! Phylum Annelida features true metameric segmentation: the body is divided into repeating ring-like segments inside and out; they possess a closed circulatory system and coiled nephridia for excretion, exemplified by the earthworm and blood-sucking leech. Next is Phylum Arthropoda—the undisputed titan of the animal kingdom, comprising over 80% of all known animal species! Arthropods feature jointed legs, bilateral symmetry, an open circulatory system, and a tough exoskeleton made of chitin that must be molted periodically through ecdysis; examples include butterflies, crabs, prawns, spiders, and scorpions. Phylum Mollusca contains soft-bodied animals protected by a calcareous shell secreted by a fleshy fold called the mantle; they move via a muscular foot, as in snails and octopuses. Finally, Phylum Echinodermata—exclusively marine spiny-skinned creatures like starfish and sea urchins. Adult echinoderms exhibit radial symmetry and possess a remarkable hydraulic Water Vascular System that powers hundreds of tiny suction tube feet for locomotion!",
        "points": [
            "<strong>Annelida (True Segmented Worms):</strong> Metameric segmentation; eucoelomate; closed blood vascular system; paired <strong>nephridia</strong> for excretion (e.g., earthworm <em>Pheretima</em>, leech <em>Hirudinaria</em>).",
            "<strong>Arthropoda (Jointed Appendages - Largest Phylum):</strong> Over 80% of animal species; segmented body (head, thorax, abdomen); jointed legs; tough chitinous exoskeleton; open hemocoel circulation (e.g., prawn, butterfly, scorpion).",
            "<strong>Mollusca (Soft Bodies with Shells):</strong> Soft unsegmented body divided into head, visceral mass, and muscular foot; mantle secretes external calcareous shell (e.g., snail <em>Pila</em>, octopus, mussel <em>Unio</em>).",
            "<strong>Echinodermata (Spiny Skinned Marine Animals):</strong> Exclusively marine; spiny calcareous skeleton; adult radial symmetry; unique hydraulic <strong>Water Vascular System</strong> operating tube feet for crawling and prey capture (e.g., starfish <em>Asterias</em>, sea urchin)."
        ],
        "checkpoints": [
            {
                "question": "Which phylum is the largest in the entire animal kingdom, comprising over 80 percent of all documented animal species?",
                "options": [
                    "Annelida",
                    "Mollusca",
                    "Arthropoda",
                    "Echinodermata"
                ],
                "correct": 2,
                "explanation": "Phylum Arthropoda (insects, crustaceans, arachnids, myriapods) is by far the largest phylum, characterized by jointed appendages and a chitinous exoskeleton."
            },
            {
                "question": "What unique hydraulic organ system is deployed exclusively by echinoderms like starfish for locomotion and food capture?",
                "options": [
                    "Closed capillary network",
                    "Water Vascular System operating hydraulic tube feet",
                    "Flame cell excretory system",
                    "Tracheal respiratory tubule system"
                ],
                "correct": 1,
                "explanation": "Echinoderms uniquely possess a water vascular system of fluid-filled canals that operates hundreds of muscular, suction-tipped tube feet for crawling and opening bivalves."
            }
        ]
    },

    # Slide 12: Chordates & The Vertebrate Spectrum: From Pisces to Mammals
    {
        "id": 12,
        "title": "Chordates & The Vertebrate Spectrum: From Pisces to Mammals",
        "subtitle": "Notochord Foundations and the 5 Classes: Pisces, Amphibia, Reptilia, Aves, and Mammalia",
        "narration": "At the apex of animal evolution stands Phylum Chordata, defined by four embryonic hallmarks: a dorsal supporting Notochord, a dorsal hollow nerve cord, pharyngeal gill slits, and a post-anal tail. In Subphylum Vertebrata, the flexible notochord is replaced during development by a hard, articulated cartilaginous or bony Vertebral Column. Vertebrates span five great classes: Class Pisces (Fishes)—streamlined aquatic poikilotherms with 2-chambered hearts and gills; Class Amphibia (Frogs, Salamanders)—dual life on land and water, moist skin lacking scales, and 3-chambered hearts; Class Reptilia (Lizards, Snakes, Crocodiles)—dry scaly epidermal skin, creeping locomotion, and leathery-shelled eggs; Class Aves (Birds)—forelimbs modified into feathered wings for flight, pneumatic hollow bones, 4-chambered hearts, and warm-blooded homeothermy; and Class Mammalia (Humans, Whales, Bats)—distinguished by mammary glands that produce milk for the young, body hair, external ear pinnae, and giving live birth (viviparity)!",
        "points": [
            "<strong>Diagnostic Chordate Features:</strong> Notochord (flexible axial rod), dorsal hollow tubular nerve cord, pharyngeal gill clefts, and post-anal tail; replaced in vertebrates by the spinal column.",
            "<strong>Pisces (Fishes):</strong> Aquatic; streamlined body; 2-chambered heart (single venous circulation); breathe via gills; cold-blooded (poikilotherms); cartilaginous (shark) or bony (rohu).",
            "<strong>Amphibia & Reptilia:</strong> Amphibians have moist glandular skin, dual aquatic/terrestrial life, 3-chambered heart; Reptiles have dry keratinized scales, amniotic leathery eggs, and 3-chambered hearts (4-chambered in crocodiles).",
            "<strong>Aves (Birds):</strong> Forelimbs modified into wings; body feathered; pneumatic hollow bones; 4-chambered heart; warm-blooded (homeotherms); oviparous with calcareous shelled eggs.",
            "<strong>Mammalia (Mammals):</strong> Possess milk-secreting mammary glands; skin covered with hair/fur; external ear pinnae; 4-chambered heart; homeothermic; mostly viviparous."
        ],
        "checkpoints": [
            {
                "question": "Which of the following vertebrate classes is warm-blooded (homeothermic) and possesses a four-chambered heart?",
                "options": [
                    "Pisces",
                    "Amphibia",
                    "Reptilia",
                    "Aves (Birds)"
                ],
                "correct": 3,
                "explanation": "Birds (Aves) and Mammals are warm-blooded (homeothermic) with fully separated four-chambered hearts that completely segregate oxygenated and deoxygenated blood."
            },
            {
                "question": "What unique anatomical feature distinguishes Class Mammalia from all other vertebrate classes in the animal kingdom?",
                "options": [
                    "Possession of lungs for respiration",
                    "Presence of milk-producing mammary glands to nourish the young, along with external ear pinnae and body hair",
                    "Internal skeleton made of bone",
                    "Bilateral symmetry with a true coelom"
                ],
                "correct": 1,
                "explanation": "Mammals are uniquely characterized by mammary glands that produce milk for nursing offspring, external ear flaps (pinnae), and body hair or fur."
            }
        ]
    },

    # Slide 13: Binomial Nomenclature: Principles & Scientific Rules (Carolus Linnaeus)
    {
        "id": 13,
        "title": "Binomial Nomenclature: Principles & Scientific Rules (Carolus Linnaeus)",
        "subtitle": "Eliminating Linguistic Confusion: The Global Rules of Botanical & Zoological Naming",
        "narration": "Why do scientists use names like Homo sapiens or Mangifera indica instead of common vernacular names? Because common names cause absolute chaos across countries and languages! In India alone, an onion is called 'Pyaz' in Hindi, 'Kanda' in Marathi, 'Ullipaya' in Telugu, and 'Vengayam' in Tamil! To resolve this confusion, Swedish naturalist Carolus Linnaeus introduced Binomial Nomenclature in 1753. Under binomial nomenclature, every organism receives a unique, universally accepted two-word scientific name. The International Codes of Nomenclature mandate five strict rules: Rule 1: All scientific names are Latin or Latinized, reflecting Latin's status as a stable dead language. Rule 2: The first word denotes the Genus; the second word denotes the specific Species. Rule 3: The Genus name ALWAYS begins with a Capital letter, while the species name ALWAYS begins with a lowercase letter! Rule 4: When printed in books, names are set in italics; when written by hand, the Genus and species must be underlined separately! Rule 5: The name of the author who first described the species may appear abbreviated at the end, such as Mangifera indica Linn.",
        "points": [
            "<strong>Vernacular Confusion:</strong> Common regional names vary across dialects and languages; multiple unrelated organisms often share identical colloquial names.",
            "<strong>Linnaeus's Binomial Revolution (1753):</strong> Standardized a universal, unambiguous two-word Latin scientific naming protocol for every biological organism.",
            "<strong>Rule 1 & 2 (Genus + Species):</strong> First word represents the broader Genus category; second word identifies the specific biological Species epithet.",
            "<strong>Rule 3 (Capitalization Law):</strong> Genus name must begin with an uppercase capital letter; Species name must strictly begin with a lowercase letter (e.g., <em>Homo sapiens</em>, NOT <em>Homo Sapiens</em>).",
            "<strong>Rule 4 (Typography Law):</strong> Printed in <em>italics</em>; when handwritten, the Genus and species MUST be underlined separately (e.g., <u>Homo</u> <u>sapiens</u>)."
        ],
        "checkpoints": [
            {
                "question": "Which of the following represents the correct typographical way to handwrite the scientific name of the mango plant?",
                "options": [
                    "Mangifera Indica (without underline)",
                    "<u>Mangifera</u> <u>indica</u> (Genus capitalized, species lowercase, underlined separately)",
                    "<u>MANGIFERA INDICA</u> (all uppercase)",
                    "mangifera indica (all lowercase without underline)"
                ],
                "correct": 1,
                "explanation": "According to the rules of binomial nomenclature, the Genus begins with a capital letter, the species is lowercase, and when handwritten, both words must be underlined separately."
            },
            {
                "question": "Why are all scientific names in binomial nomenclature derived from or treated as Latin words?",
                "options": [
                    "Latin is spoken as the primary language in every United Nations meeting",
                    "Latin is a stable 'dead language' whose grammar and vocabulary do not change over time, ensuring international consistency",
                    "Linnaeus was legally forbidden from using any other alphabet",
                    "Latin names are shorter than English names"
                ],
                "correct": 1,
                "explanation": "Latin is a dead language that does not evolve or alter its grammatical meanings, providing an immutable, universally stable standard for international science."
            }
        ]
    },

    # Slide 14: Applying Binomial Nomenclature in Local Surroundings (C-4.1)
    {
        "id": 14,
        "title": "Applying Binomial Nomenclature in Local Surroundings",
        "subtitle": "Connecting Taxonomy to Everyday Indian Flora and Fauna",
        "narration": "Now let us apply binomial nomenclature to common organisms in your everyday Indian surroundings (C-4.1)! Take the great feline carnivores: the Royal Bengal Tiger is Panthera tigris, the Lion is Panthera leo, and the Leopard is Panthera pardus. Notice that all three share the generic name Panthera, proving their close evolutionary kinship and shared ancestral lineage! In your garden, the holy basil or Tulsi is Ocimum sanctum; the sacred Peepal tree is Ficus religiosa; while its sister species, the Banyan tree, is Ficus benghalensis. The medicinal Neem tree is Azadirachta indica; the sweet mango is Mangifera indica; and our national bird, the Indian Peacock, is Pavo cristatus. The garden pea used in genetics is Pisum sativum; the staple cereal rice is Oryza sativa; and wheat is Triticum aestivum. And what about us humans? We are Homo sapiens—the 'wise humans'! By mastering these scientific names, you connect local biodiversity to global taxonomy!",
        "points": [
            "<strong>Shared Generic Affinity:</strong> Closely related species share a common genus name, revealing evolutionary kinship: Tiger (<em>Panthera tigris</em>), Lion (<em>Panthera leo</em>), Leopard (<em>Panthera pardus</em>).",
            "<strong>Common Indian Botanical Examples:</strong> Holy Basil/Tulsi (<em>Ocimum sanctum</em>), Peepal (<em>Ficus religiosa</em>), Banyan (<em>Ficus benghalensis</em>), Neem (<em>Azadirachta indica</em>), Mango (<em>Mangifera indica</em>).",
            "<strong>Common Indian Agricultural & Floral Crops:</strong> Garden Pea (<em>Pisum sativum</em>), Rice (<em>Oryza sativa</em>), Wheat (<em>Triticum aestivum</em>), Mustard (<em>Brassica campestris</em>).",
            "<strong>Common Zoological Examples:</strong> Human (<em>Homo sapiens</em>), Indian Peacock (<em>Pavo cristatus</em>), House Crow (<em>Corvus splendens</em>), Frog (<em>Rana tigrina</em>)."
        ],
        "checkpoints": [
            {
                "question": "What biological conclusion can be drawn from the fact that the Lion (*Panthera leo*), Tiger (*Panthera tigris*), and Leopard (*Panthera pardus*) share the same genus name?",
                "options": [
                    "They can freely mate to produce fertile offspring in nature",
                    "They share close evolutionary kinship and common anatomical characteristics inherited from a common feline ancestor",
                    "They consume the exact same grass in agricultural fields",
                    "Their scientific names were assigned by accident"
                ],
                "correct": 1,
                "explanation": "Sharing a genus (*Panthera*) signifies that lions, tigers, and leopards are closely related species that evolved from a recent common ancestral feline lineage."
            },
            {
                "question": "What is the scientific botanical name of the medicinal Neem tree commonly found across India (C-4.1)?",
                "options": [
                    "<em>Mangifera indica</em>",
                    "<em>Azadirachta indica</em>",
                    "<em>Ficus religiosa</em>",
                    "<em>Ocimum sanctum</em>"
                ],
                "correct": 1,
                "explanation": "The scientific name of the Indian neem tree, celebrated for its antimicrobial and medicinal properties, is <em>Azadirachta indica</em>."
            }
        ]
    },

    # Slide 15: Acellular Entities: Viruses, Viroids & Prions (The Biological Borderland)
    {
        "id": 15,
        "title": "Acellular Entities: Viruses, Viroids & Prions (The Biological Borderland)",
        "subtitle": "Entities Lacking Cellular Organization: Capsids, RNA, and Infectious Misfolded Proteins",
        "narration": "Why did Whittaker omit Viruses from his Five Kingdom System? Because viruses do not possess cellular organisation—they are acellular entities that exist on the threshold between the living and non-living worlds! Outside a living host, a virus is completely inert, forming non-living crystals lacking cytoplasm, cell membranes, ribosomes, and metabolic machinery. But once a virus infects a host cell, its genetic material hijacks the host's ribosomes and enzymes, commanding the host to synthesize thousands of viral copies like a living organism! Structurally, a virus consists of genetic material—either DNA or RNA, NEVER both—encased in a protective protein coat called a Capsid made of capsomere subunits. Bacteriophages infect bacteria, Tobacco Mosaic Virus (TMV) infects plants, and influenza, HIV, and SARS-CoV-2 infect humans. Even smaller are Viroids, discovered by T.O. Diener in 1971: free infectious RNA molecules lacking any protein coat that infect crops like potatoes. And Prions: abnormally misfolded infectious proteins lacking nucleic acids that trigger fatal neurodegenerative diseases like Mad Cow disease!",
        "points": [
            "<strong>Why Excluded from 5 Kingdoms:</strong> Viruses lack cellular organisation; they possess no cytoplasm, cell membranes, metabolic enzymes, or autonomous energy generation.",
            "<strong>Biphasic Nature:</strong> Non-living inert crystalline particles in the extracellular environment; living obligate intracellular parasites that hijack host machinery once inside a cell.",
            "<strong>Viral Molecular Anatomy:</strong> Genetic core containing either DNA or RNA (never both) enclosed in a protective protein coat called a <strong>Capsid</strong> composed of capsomeres.",
            "<strong>Viroids & Prions:</strong> Viroids (discovered by T.O. Diener 1971) are naked infectious single-stranded RNA molecules lacking protein coats; Prions are infectious misfolded proteins causing Mad Cow Disease (BSE)."
        ],
        "checkpoints": [
            {
                "question": "Why are viruses not placed into any of the five kingdoms of Whittaker's classification system?",
                "options": [
                    "They are too large to be viewed under normal microscopes",
                    "They are acellular entities lacking cellular organisation, cytoplasm, and autonomous metabolic machinery",
                    "They live exclusively in outer space",
                    "They contain only pure water without genetic material"
                ],
                "correct": 1,
                "explanation": "Whittaker's classification is based on cellular organisation; viruses are non-cellular (acellular) nucleoprotein packages that are metabolically inert outside a host cell."
            },
            {
                "question": "What defines a 'viroid' discovered by T.O. Diener in 1971 as distinct from a conventional virus?",
                "options": [
                    "Viroids are giant multicellular bacteria",
                    "Viroids consist of free, low molecular weight infectious RNA completely lacking any protective protein capsid",
                    "Viroids have a double cell wall made of chitin and cellulose",
                    "Viroids reproduce exclusively through seeds"
                ],
                "correct": 1,
                "explanation": "Viroids are sub-viral plant pathogens consisting purely of a short strand of circular, single-stranded infectious RNA without any surrounding protein coat."
            }
        ]
    },

    # Slide 16: Ecological Synergy & Environmental Conservation (C-2.8, C-4.1)
    {
        "id": 16,
        "title": "Ecological Synergy & Environmental Conservation",
        "subtitle": "Trophic Stability, Nitrogen Fixation, Keystone Species, and Conservation Frameworks",
        "narration": "To conclude our journey through biological diversity, let us reflect on ecological synergy and planetary conservation (C-2.8). Every organism, from microscopic cyanobacteria to apex predators, occupies an irreplaceable ecological niche. Cyanobacteria in the oceans produce over 50% of the oxygen we breathe! Symbiotic Rhizobium bacteria living in the root nodules of leguminous plants fix inert atmospheric nitrogen into nitrates, enriching soil fertility without synthetic chemicals. Fungi and soil actinomycetes decompose dead matter, closing the circular biogeochemical loops of carbon and nitrogen. When human activities cause habitat destruction, chemical pollution, or introduce aggressive alien invasive species like Parthenium weed or Eichhornia water hyacinth, delicate ecological webs collapse. Protecting biological diversity requires both In Situ conservation—protecting species in their natural habitats via National Parks, Wildlife Sanctuaries, and Biosphere Reserves—and Ex Situ conservation—preserving endangered species in Botanical Gardens, Zoological Parks, and Cryogenic Seed Banks at -196 °C. Safeguarding biodiversity is safeguarding our own future!",
        "points": [
            "<strong>Ecological Keystone Roles (C-2.8):</strong> Marine cyanobacteria produce over half of Earth's oxygen; nitrogen-fixing <em>Rhizobium</em> enriches soil fertility; saprophytic fungi recycle essential biogeochemical elements.",
            "<strong>Ecological Interdependence:</strong> Loss of a single keystone species can trigger trophic cascades, destabilizing food webs and ecosystem services.",
            "<strong>Threats to Global Biodiversity:</strong> Habitat destruction and deforestation, industrial chemical pollution, climate disruption, and invasive alien species (e.g., <em>Eichhornia</em> / water hyacinth, <em>Parthenium</em>).",
            "<strong>Conservation Strategies:</strong> <strong>In Situ</strong> (on-site protection in National Parks, Sanctuaries, Biosphere Reserves) vs <strong>Ex Situ</strong> (off-site protection in Botanical Gardens, Zoological Parks, Cryogenic Gene Banks at -196 °C)."
        ],
        "checkpoints": [
            {
                "question": "Which of the following conservation strategies represents an 'In Situ' method of protecting biological diversity?",
                "options": [
                    "Preserving seeds in a liquid nitrogen cryo-bank",
                    "Establishing a protected National Park or Biosphere Reserve in the organism's natural habitat",
                    "Keeping an animal inside a metropolitan zoological garden cage",
                    "Culturing plant tissues in a glass petri dish"
                ],
                "correct": 1,
                "explanation": "In situ conservation protects endangered species within their native, natural ecosystems (National Parks, Sanctuaries, Biosphere Reserves); ex situ preserves them in artificial off-site facilities."
            },
            {
                "question": "What ecological service is provided by symbiotic *Rhizobium* bacteria residing in the root nodules of leguminous plants (C-2.8)?",
                "options": [
                    "They convert sunlight into vitamin D for the plant",
                    "They fix atmospheric nitrogen gas into soluble nitrates that plants can absorb to synthesize proteins",
                    "They cause the soil to become strongly acidic",
                    "They prevent the plant leaves from transpiring water"
                ],
                "correct": 1,
                "explanation": "Rhizobium bacteria convert inert atmospheric nitrogen ($N_2$) into biologically usable nitrates, enriching soil fertility naturally without synthetic chemical fertilizers."
            }
        ]
    },

    # Slide 17: Dedicated Quiz Challenge 1 — Five Kingdoms & Classification Principles
    {
        "id": 17,
        "title": "Dedicated Quiz Challenge 1: Five Kingdoms & Classification Principles",
        "subtitle": "Test Your Knowledge on Whittaker's 5 Kingdoms, Monera, Protista, Fungi, and Criteria",
        "narration": "Welcome to Quiz Challenge 1! Test your conceptual mastery of the five-kingdom classification, prokaryotic vs eukaryotic distinctions, fungal chitin walls, and the nutritional foundations of taxonomy. Click your answers and examine the step-by-step solutions.",
        "is_quiz": True,
        "quiz_title": "Five Kingdoms & Classification Principles Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. Who proposed the widely accepted Five Kingdom Classification of living organisms in 1969?",
                "options": ["Carolus Linnaeus", "Robert H. Whittaker", "Carl Woese", "Charles Darwin"],
                "correct": 1,
                "solution": "R.H. Whittaker proposed the Five Kingdom Classification in 1969 based on cellular complexity, body organisation, mode of nutrition, and ecological roles."
            },
            {
                "q": "2. An organism is unicellular, possesses a peptidoglycan cell wall, and lacks a nuclear envelope and membrane-bound organelles. Into which kingdom should it be placed?",
                "options": ["Protista", "Fungi", "Monera", "Plantae"],
                "correct": 2,
                "solution": "Kingdom Monera encompasses all unicellular prokaryotes lacking a membrane-bound nucleus and membrane-bound organelles, including true bacteria and cyanobacteria."
            },
            {
                "q": "3. Unicellular eukaryotic organisms such as Amoeba, Paramecium, and Euglena are classified under which kingdom?",
                "options": ["Monera", "Protista", "Fungi", "Animalia"],
                "correct": 1,
                "solution": "Kingdom Protista comprises unicellular eukaryotic organisms that possess a true nucleus and membrane-bound organelles."
            },
            {
                "q": "4. Fungi differ fundamentally from plants because their cell walls are constructed of:",
                "options": ["Cellulose", "Chitin", "Pectin", "Peptidoglycan"],
                "correct": 1,
                "solution": "Fungi possess cell walls composed of chitin (a nitrogenous polysaccharide), whereas plant cell walls are made predominantly of cellulose."
            },
            {
                "q": "5. Blue-green algae (Cyanobacteria) that execute photosynthesis are taxonomically classified under Kingdom:",
                "options": ["Plantae", "Monera", "Protista", "Fungi"],
                "correct": 1,
                "solution": "Cyanobacteria are prokaryotes lacking membrane-bound nuclei and organelles; despite possessing chlorophyll, their prokaryotic cytology places them in Kingdom Monera."
            },
            {
                "q": "6. Which of the following is the correct hierarchical sequence of taxonomic ranks from highest to lowest?",
                "options": [
                    "Kingdom $\\to$ Phylum $\\to$ Class $\\to$ Order $\\to$ Family $\\to$ Genus $\\to$ Species",
                    "Species $\\to$ Genus $\\to$ Family $\\to$ Class $\\to$ Order $\\to$ Phylum $\\to$ Kingdom",
                    "Kingdom $\\to$ Order $\\to$ Class $\\to$ Family $\\to$ Genus $\\to$ Phylum $\\to$ Species",
                    "Phylum $\\to$ Kingdom $\\to$ Class $\\to$ Order $\\to$ Family $\\to$ Species $\\to$ Genus"
                ],
                "correct": 0,
                "solution": "The correct descending taxonomic hierarchy is Kingdom $\\to$ Phylum/Division $\\to$ Class $\\to$ Order $\\to$ Family $\\to$ Genus $\\to$ Species."
            },
            {
                "q": "7. What mode of nutrition characterizes organisms belonging to Kingdom Fungi?",
                "options": [
                    "Autotrophic photosynthesis",
                    "Heterotrophic saprophytic absorption of decayed organic matter",
                    "Chemosynthetic nitrogen oxidation",
                    "Holozoic phagocytosis of large prey"
                ],
                "correct": 1,
                "solution": "Fungi are heterotrophic saprophytes that secrete extracellular enzymes onto organic substrates and absorb the digested soluble nutrients."
            },
            {
                "q": "8. What cellular characteristic separates Kingdom Animalia from Kingdom Plantae?",
                "options": [
                    "Animals have true cell nuclei while plants do not",
                    "Animals lack cell walls and possess holozoic ingestive nutrition, while plants have cellulosic cell walls and autotrophic nutrition",
                    "Animals contain large central sap vacuoles in every cell",
                    "Animals are unicellular prokaryotes"
                ],
                "correct": 1,
                "solution": "Animal cells lack cell walls and chloroplasts and perform holozoic ingestive heterotrophy, whereas plant cells have cellulosic walls and perform photosynthesis."
            },
            {
                "q": "9. Which organism is a unicellular fungus widely used in baking and brewing?",
                "options": ["Rhizopus", "Agaricus", "Yeast (Saccharomyces)", "Penicillium"],
                "correct": 2,
                "solution": "Yeast is an exceptional unicellular fungus that reproduces asexually via budding and ferments sugars into alcohol and carbon dioxide."
            },
            {
                "q": "10. In ecological trophic dynamics, which kingdom primarily serves as the Producers capturing solar energy (C-2.8)?",
                "options": ["Animalia", "Fungi", "Plantae", "Monera exclusively"],
                "correct": 2,
                "solution": "Kingdom Plantae contains multicellular autotrophs with chlorophyll that synthesize organic biomass from sunlight, serving as primary producers."
            }
        ]
    },

    # Slide 18: Dedicated Quiz Challenge 2 — Plant & Animal Taxonomy Mastery
    {
        "id": 18,
        "title": "Dedicated Quiz Challenge 2: Plant & Animal Taxonomy Mastery",
        "subtitle": "Test Your Knowledge on Plant Divisions, Monocots/Dicots, Coelom Types, and Animal Phyla",
        "narration": "Welcome to Quiz Challenge 2! Evaluate your command over botanical divisions and zoological phyla—including Thallophyta, Bryophyta amphibians, Pteridophytes, Gymnosperms vs Angiosperms, acoelomates vs eucoelomates, and vertebrate classes. Select your answers and inspect the solutions.",
        "is_quiz": True,
        "quiz_title": "Plant & Animal Taxonomy Mastery Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. Why are bryophytes (such as mosses and Marchantia) referred to as the 'Amphibians of the Plant Kingdom'?",
                "options": [
                    "They can breathe through skin like salamanders",
                    "They live on soil but strictly require water for flagellated male sperms to swim and fertilize the egg",
                    "They transform into green algae in summer",
                    "They have gills and swim like fish"
                ],
                "correct": 1,
                "solution": "Bryophytes are terrestrial plants that require a layer of external water for sperm to swim toward the female archegonium for sexual reproduction."
            },
            {
                "q": "2. Which plant division was the first in evolutionary history to develop specialized conducting vascular tissues (xylem and phloem)?",
                "options": ["Thallophyta", "Bryophyta", "Pteridophyta (Ferns)", "Algae"],
                "correct": 2,
                "solution": "Pteridophytes (ferns like Marsilea and Dryopteris) were the first vascular cryptogams, evolving true xylem and phloem conducting tissues."
            },
            {
                "q": "3. Gymnosperms are distinct from Angiosperms because their seeds are:",
                "options": [
                    "Enclosed inside fleshy fruits",
                    "Naked and borne exposed on the scales of cones without an enclosing ovary wall",
                    "Lacking an embryo",
                    "Produced underwater"
                ],
                "correct": 1,
                "solution": "Gymnosperms bear naked ovules not enclosed by an ovary wall; their seeds develop exposed on the surfaces of reproductive cone scales."
            },
            {
                "q": "4. A plant specimen displays leaves with reticulate net-like venation, two cotyledons in its seeds, and a deep taproot. It is a:",
                "options": ["Monocotyledon", "Dicotyledon", "Gymnosperm", "Bryophyte"],
                "correct": 1,
                "solution": "Two seed cotyledons, reticulate leaf venation, and a taproot system are the classic diagnostic hallmarks of Dicotyledonous angiosperms."
            },
            {
                "q": "5. Which animal phylum is characterized by an acoelomate body plan with dorsoventrally flattened bodies and flame cells for excretion?",
                "options": ["Porifera", "Coelenterata", "Platyhelminthes (Flatworms)", "Nematoda"],
                "correct": 2,
                "solution": "Platyhelminthes (flatworms like Planaria and tapeworms) are triploblastic, bilaterally symmetrical, and acoelomate, using flame cells for excretion."
            },
            {
                "q": "6. Parasitic roundworms like Ascaris and Wuchereria possess which type of body cavity?",
                "options": ["Acoelomate (no cavity)", "Pseudocoelomate (false body cavity)", "Eucoelomate (true coelom)", "Hemocoel only"],
                "correct": 1,
                "solution": "Nematodes (roundworms) possess a pseudocoelom, where the body cavity is derived from the embryonic blastocoel and lacks a complete mesodermal peritoneal lining."
            },
            {
                "q": "7. Metameric true segmentation and coiled excretory nephridia are defining characteristics of which animal phylum?",
                "options": ["Arthropoda", "Annelida (Earthworms & Leeches)", "Mollusca", "Platyhelminthes"],
                "correct": 1,
                "solution": "Annelids exhibit true metameric segmentation (body divided into repeating serial rings) and possess paired nephridia in each segment for excretion."
            },
            {
                "q": "8. What structural feature is shared by all organisms in Phylum Arthropoda?",
                "options": [
                    "A soft unsegmented body with a calcareous shell",
                    "Jointed appendages and a tough chitinous exoskeleton",
                    "A water vascular system with tube feet",
                    "A 4-chambered heart and feathers"
                ],
                "correct": 1,
                "solution": "Arthropods (insects, crustaceans, spiders) possess paired jointed appendages and an external chitinous cuticle that is periodically shed during growth."
            },
            {
                "q": "9. Starfish and sea urchins belong to Phylum Echinodermata and move using a hydraulic organ system called the:",
                "options": ["Canal water system", "Water Vascular System operating tube feet", "Open hemocoel", "Tracheal system"],
                "correct": 1,
                "solution": "Echinoderms uniquely possess a hydraulic water vascular system that drives hundreds of suction-tipped tube feet for locomotion and gripping prey."
            },
            {
                "q": "10. Which class of vertebrates possesses milk-producing mammary glands, external ear pinnae, and skin covered with hair?",
                "options": ["Aves", "Reptilia", "Amphibia", "Mammalia"],
                "correct": 3,
                "solution": "Mammalia is uniquely characterized by mammary glands for nursing the young, external ear flaps (pinnae), and epidermal hair or fur."
            }
        ]
    },

    # Slide 19: Dedicated Quiz Challenge 3 — Binomial Nomenclature & Indian Species
    {
        "id": 19,
        "title": "Dedicated Quiz Challenge 3: Binomial Nomenclature & Indian Species",
        "subtitle": "Test Your Knowledge on Linnaean Rules, Capitalization, Italics, and Indian Biodiversity",
        "narration": "Welcome to Quiz Challenge 3! Delve into the rules of binomial nomenclature formulated by Carolus Linnaeus, typographical guidelines, and the scientific names of common Indian plants and animals. Choose your answers and review the solutions.",
        "is_quiz": True,
        "quiz_title": "Binomial Nomenclature & Indian Species Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. Who is recognized worldwide as the Father of Modern Taxonomy for formulating the system of Binomial Nomenclature?",
                "options": ["Aristotle", "Carolus Linnaeus", "Robert Whittaker", "Gregor Mendel"],
                "correct": 1,
                "solution": "Swedish naturalist Carolus Linnaeus introduced binomial nomenclature in his landmark 1753 work, standardizing a two-word scientific naming protocol."
            },
            {
                "q": "2. In the scientific name *Mangifera indica* Linn., what does the word 'indica' represent?",
                "options": ["The Genus name", "The Species epithet", "The Family name", "The Country of discovery"],
                "correct": 1,
                "solution": "In binomial nomenclature, the first word (*Mangifera*) is the Genus, and the second word (*indica*) is the specific Species epithet."
            },
            {
                "q": "3. Which of the following is written strictly in accordance with the International Rules of Binomial Nomenclature?",
                "options": [
                    "<em>panthera Tigris</em>",
                    "<em>Panthera tigris</em>",
                    "Panthera Tigris",
                    "<u>Panthera</u> <u>Tigris</u>"
                ],
                "correct": 1,
                "solution": "The Genus must begin with a capital letter (*Panthera*), the species must begin with a lowercase letter (*tigris*), and both must be italicized in print."
            },
            {
                "q": "4. When a scientific name is handwritten in a laboratory notebook, how must it be formatted?",
                "options": [
                    "Written in bold cursive without any underlines",
                    "The Genus and species must be underlined separately with a straight line",
                    "All letters must be written in capital block letters",
                    "Written in red ink with an exclamation mark"
                ],
                "correct": 1,
                "solution": "When handwritten, the Genus and species must be underlined separately (e.g., <u>Homo</u> <u>sapiens</u>) to denote their Latinized origin."
            },
            {
                "q": "5. What is the scientific binomial name of the human species?",
                "options": ["<em>Pan troglodytes</em>", "<em>Homo sapiens</em>", "<em>Canis familiaris</em>", "<em>Felis catus</em>"],
                "correct": 1,
                "solution": "The scientific name of modern humans is <em>Homo sapiens</em>, meaning 'wise human'."
            },
            {
                "q": "6. What is the scientific name of India's national animal, the Royal Bengal Tiger?",
                "options": ["<em>Panthera leo</em>", "<em>Panthera tigris</em>", "<em>Panthera pardus</em>", "<em>Acinonyx jubatus</em>"],
                "correct": 1,
                "solution": "The scientific name of the Royal Bengal Tiger is <em>Panthera tigris</em>."
            },
            {
                "q": "7. The medicinal Neem tree widely revered across India has the scientific botanical name of (C-4.1):",
                "options": ["<em>Ocimum sanctum</em>", "<em>Azadirachta indica</em>", "<em>Ficus benghalensis</em>", "<em>Pisum sativum</em>"],
                "correct": 1,
                "solution": "The scientific name of the medicinal Neem tree is <em>Azadirachta indica</em>."
            },
            {
                "q": "8. What is the scientific botanical name of the sacred Tulsi (Holy Basil) plant (C-4.1)?",
                "options": ["<em>Ocimum sanctum</em>", "<em>Mangifera indica</em>", "<em>Ficus religiosa</em>", "<em>Oryza sativa</em>"],
                "correct": 0,
                "solution": "The botanical name of the sacred Tulsi plant is <em>Ocimum sanctum</em>."
            },
            {
                "q": "9. Both the sacred Peepal (*Ficus religiosa*) and the Banyan tree (*Ficus benghalensis*) share the generic name *Ficus*. What does this indicate?",
                "options": [
                    "They are identical species with different leaves",
                    "They are closely related species belonging to the same genus, sharing a recent common evolutionary ancestor",
                    "They cannot grow in Indian soil",
                    "They belong to different plant kingdoms"
                ],
                "correct": 1,
                "solution": "Sharing the same genus (*Ficus*) indicates that Peepal and Banyan are closely related distinct species that evolved from a shared ancestral lineage."
            },
            {
                "q": "10. In the scientific name *Pisum sativum* Linn., what does the abbreviation 'Linn.' denote?",
                "options": [
                    "The plant was discovered in the city of London",
                    "The species produces linear pea pods",
                    "The name was first published and described by Carolus Linnaeus",
                    "The plant belongs to the family Linaceae"
                ],
                "correct": 2,
                "solution": "An author citation (like 'Linn.' or 'L.') indicates the taxonomist who first described and formally named the species—in this case, Carolus Linnaeus."
            }
        ]
    },

    # Slide 20: Dedicated Quiz Challenge 4 — 3 Domains, Viruses, Lichens & Ecological Mastery
    {
        "id": 20,
        "title": "Dedicated Quiz Challenge 4: 3 Domains, Viruses, Lichens & Ecological Mastery",
        "subtitle": "Synthesizing Carl Woese's Domains, Lichen Symbiosis, Acellular Entities, and Conservation",
        "narration": "Congratulations on reaching the final Quiz Challenge! This master challenge evaluates your synthesis of modern 3-domain phylogenetics, lichen air pollution monitoring, acellular virus and viroid biology, and keystone conservation strategies. Answer every question and examine the complete solutions.",
        "is_quiz": True,
        "quiz_title": "3 Domains, Viruses & Ecological Mastery Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. In Carl Woese's Three Domain system (C-7.1), which domain contains ancient extremophiles with unique ether-linked branched lipid cell membranes?",
                "options": ["Domain Bacteria", "Domain Archaea", "Domain Eukarya", "Domain Protista"],
                "correct": 1,
                "solution": "Domain Archaea comprises ancient extremophilic prokaryotes possessing unique ether-linked branched membrane lipids that withstand extreme heat, salt, and acidity."
            },
            {
                "q": "2. Why are viruses universally described as living on the biological borderland between living and non-living entities?",
                "options": [
                    "They can breathe under water but walk on land",
                    "They are inert crystalline particles lacking cellular machinery outside a host, but replicate by hijacking host cellular apparatus once inside",
                    "They have animal heads and plant roots",
                    "They are visible only when exposed to moonlight"
                ],
                "correct": 1,
                "solution": "Viruses exhibit no metabolic activity or cellular structure outside a host, but reproduce and evolve using the host cell's molecular machinery upon infection."
            },
            {
                "q": "3. What is the fundamental structural composition of a simple virus particle?",
                "options": [
                    "A nucleus surrounded by mitochondria and ribosomes",
                    "A core of genetic material (DNA or RNA) enclosed in a protective protein coat called a Capsid",
                    "A cellulose cell wall containing chlorophyll",
                    "A droplet of pure fat without proteins"
                ],
                "correct": 1,
                "solution": "A virus consists of a nucleic acid genetic core (either DNA or RNA, never both) encased in a protein shell called a capsid made of capsomeres."
            },
            {
                "q": "4. What sub-viral infectious entity, discovered by T.O. Diener in 1971, consists of free infectious RNA lacking any protective protein capsid?",
                "options": ["Bacteriophage", "Viroid", "Prion", "Lichen"],
                "correct": 1,
                "solution": "Viroids are infectious plant pathogens consisting exclusively of short, circular, single-stranded RNA molecules without any protein coat."
            },
            {
                "q": "5. What are Prions that cause neurodegenerative diseases like Bovine Spongiform Encephalopathy (Mad Cow Disease)?",
                "options": [
                    "Giant marine flatworms",
                    "Abnormally misfolded infectious protein particles completely lacking nucleic acid genomes",
                    "Photosynthetic blue-green algae",
                    "Carnivorous fungi"
                ],
                "correct": 1,
                "solution": "Prions are infectious agents composed purely of abnormally folded proteins that induce misfolding in normal cellular proteins, lacking DNA and RNA."
            },
            {
                "q": "6. A lichen is a mutualistic symbiotic association between which two organisms (C-2.8)?",
                "options": [
                    "A virus and a bacterium",
                    "An autotrophic alga/cyanobacterium (phycobiont) and a heterotrophic fungus (mycobiont)",
                    "A fern and a moss",
                    "A tree root and an insect"
                ],
                "correct": 1,
                "solution": "A lichen is a composite organism formed by a symbiotic partnership between a photosynthetic alga (phycobiont) and a protective fungus (mycobiont)."
            },
            {
                "q": "7. Why are lichens recognized worldwide as biological bio-indicators of atmospheric sulfur dioxide ($SO_2$) pollution (C-2.8)?",
                "options": [
                    "They turn bright gold when exposed to factory smoke",
                    "Lacking a protective cuticle, they absorb air pollutants directly, causing chlorophyll destruction and death in industrial zones",
                    "They produce sulfur dioxide to poison nearby trees",
                    "They grow only on car exhaust pipes"
                ],
                "correct": 1,
                "solution": "Lichens absorb moisture and minerals directly from the atmosphere; they lack protective waxy cuticles and are poisoned by sulfur dioxide, leaving polluted areas barren."
            },
            {
                "q": "8. What mutualistic association occurs between soil fungi and the roots of higher vascular plants to enhance phosphorus nutrient uptake (C-2.8)?",
                "options": ["Lichen", "Mycorrhiza", "Canal system", "Flame cell network"],
                "correct": 1,
                "solution": "Mycorrhiza is a symbiotic association between soil fungi and plant roots, where the fungus enhances mineral (especially phosphorus) and water absorption in return for sugars."
            },
            {
                "q": "9. Which of the following is an example of an aggressive invasive alien plant species that disrupts native Indian biodiversity?",
                "options": [
                    "<em>Azadirachta indica</em> (Neem)",
                    "<em>Eichhornia crassipes</em> (Water hyacinth / Terror of Bengal)",
                    "<em>Ficus religiosa</em> (Peepal)",
                    "<em>Mangifera indica</em> (Mango)"
                ],
                "correct": 1,
                "solution": "Water hyacinth (<em>Eichhornia crassipes</em>) is an invasive alien weed that grows aggressively, choking waterways and depleting dissolved oxygen, threatening aquatic life."
            },
            {
                "q": "10. At what temperature are endangered plant seeds, animal gametes, and tissues cryopreserved in liquid nitrogen for ex situ conservation?",
                "options": [
                    "$0^\\circ\\text{C}$",
                    "$-20^\\circ\\text{C}$",
                    "$-196^\\circ\\text{C}$",
                    "$-50^\\circ\\text{C}$"
                ],
                "correct": 2,
                "solution": "Ex situ cryogenic gene banks preserve biological materials in liquid nitrogen at $-196^\\circ\\text{C}$, arresting metabolic degradation indefinitely."
            }
        ]
    }
]


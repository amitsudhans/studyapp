#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 12: Patterns in Life: Diversity and Classification
Part 2: Slides 9-16 Data Generator
Titles: 1-3 words each.
Speech: Strictly 195-215 words each. Pure Indian male teacher lecture style.
Zero fictional human names. Zero personas (Dr, Sir, Madam, Mr, Mrs, Miss, Prof).
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Algae to Pteridophytes",
        "subtitle": "Section 12.6.4: Thallophyta, Bryophyta, Pteridophyta & Lichen Mutualism",
        "speech": (
            "Kingdom Plantae comprises multicellular, photosynthetic autotrophic eukaryotes whose cells are fortified by "
            "tough cellulose cell walls! The evolutionary transition of plants from aquatic origins to dry land unfolds through "
            "five successive divisions. The most primitive division is Thallophyta, commonly known as algae, exemplified by "
            "the freshwater filamentous green alga Spirogyra. Algae possess an undifferentiated plant body called a thallus, lacking "
            "true roots, stems, or leaves, relying entirely on surrounding water for mechanical support and direct nutrient diffusion. "
            "Remarkable mutualistic partnerships called lichens combine photosynthetic green algae with absorptive fungal hyphae; "
            "lichens serve as exceptionally sensitive natural bioindicators of air quality and provide traditional culinary spices, "
            "known as patthar ke phool in Indian cuisine! Next, Bryophyta represents the true amphibians of the plant kingdom, including "
            "liverworts like Marchantia and terrestrial mosses. Bryophytes display differentiated stem-like and leaf-like structures "
            "anchored by hair-like rhizoids; although living on moist soil, they strictly require a film of external water for their "
            "flagellated male gametes to swim and fertilize female egg cells! Advancing further onto dry land, Pteridophyta, comprising "
            "ferns, evolved true roots, stems, leaves, and specialized vascular conducting tissues—xylem for water transport and phloem "
            "for sugar distribution—though they remain seedless and still depend on moisture for reproduction."
        ),
        "checkpoints": [
            {
                "question": "Why are bryophytes (mosses and liverworts) traditionally designated as the 'amphibians of the plant kingdom'?",
                "options": [
                    "They possess webbed swimming feet and breathe through lungs",
                    "They live on land but strictly require an external film of water for flagellated male gametes to swim during fertilisation",
                    "They transform into tadpoles during dry summer seasons",
                    "They produce swimming seeds that travel across ocean currents"
                ],
                "answer": 1,
                "hint": "Like amphibians, they inhabit land but must return to water for sexual reproduction.",
                "explanation": "Bryophytes grow on land but depend on water for their flagellated sperm to swim to the egg cell, earning the title 'amphibians of the plant kingdom'."
            },
            {
                "question": "Which major evolutionary adaptation distinguishes pteridophytes (ferns) from more primitive bryophytes?",
                "options": [
                    "The production of edible succulent fruits containing seeds",
                    "The presence of true roots, stems, leaves, and specialized vascular tissues (xylem and phloem)",
                    "The absence of cellular nuclei and chloroplasts",
                    "The ability to move freely using muscular legs"
                ],
                "answer": 1,
                "hint": "Ferns were the first land plants to evolve vascular conducting pipes (xylem and phloem).",
                "explanation": "Pteridophytes possess true vascular transport tissues (xylem and phloem) and differentiated roots, stems, and leaves, unlike non-vascular bryophytes."
            }
        ]
    },
    {
        "id": 10,
        "title": "Gymnosperms & Angiosperms",
        "subtitle": "Section 12.6.4: Naked-Seeded Plants, Flowering Plants & Hortus Malabaricus",
        "speech": (
            "The evolutionary conquest of dry land culminated with the emergence of seed-bearing plants, divided into Gymnosperms "
            "and Angiosperms! Gymnosperms, derived from the Greek words meaning naked seeds, include rugged woody conifers like pines, "
            "deodars, and cycads. Adapted to harsh, cold, or arid mountainous climates, gymnosperms possess tough needle-like leaves "
            "with thick cuticles and sunken stomata to minimize water loss. Crucially, their ovules and developing seeds remain exposed "
            "nakedly on the scales of woody cones, completely unenclosed by ovary walls! Fertilisation is achieved via wind-blown pollen "
            "tubes, completely emancipating plant reproduction from external water. In dramatic contrast, Angiosperms, or flowering "
            "plants, represent the pinnacle of plant diversification. In angiosperms, ovules develop securely enclosed within a "
            "protective ovary, which ripens into a fruit following fertilisation. Angiosperms deploy vibrant flowers to enlist animal "
            "pollinators and are subdivided based on embryonic seed leaves into monocots, exhibiting parallel leaf venation and fibrous "
            "roots like wheat and grasses, and dicots, displaying reticulate netted venation and taproots like peas and mangoes! We celebrate "
            "the seventeenth-century treatise Hortus Malabaricus, compiled by Hendrik van Rheede with the profound botanical expertise "
            "of Ayurvedic physician Itty Achudan, which systematically documented the medicinal properties and taxonomy of Kerala's "
            "magnificent flowering flora."
        ),
        "checkpoints": [
            {
                "question": "What is the primary anatomical difference between the seeds of gymnosperms and angiosperms?",
                "options": [
                    "Gymnosperm seeds lack DNA, while angiosperm seeds contain proteins",
                    "Gymnosperm seeds are naked on cone scales, while angiosperm seeds are enclosed within a protective fruit",
                    "Gymnosperm seeds only grow in deep ocean water",
                    "Angiosperm seeds cannot germinate in soil"
                ],
                "answer": 1,
                "hint": "Gymnosperm = naked seed; Angiosperm = vessel seed (enclosed in fruit).",
                "explanation": "Gymnosperms bear naked exposed seeds on cone scales without an ovary, whereas angiosperm seeds develop enclosed inside an ovary that matures into fruit."
            },
            {
                "question": "How can monocots and dicots be distinguished easily by inspecting their foliage leaves?",
                "options": [
                    "Monocots have blue leaves; dicots have purple leaves",
                    "Monocots display parallel venation, whereas dicots display reticulate (net-like) venation",
                    "Monocots produce woody bark; dicots lack cell walls",
                    "Monocots only grow underground without leaves"
                ],
                "answer": 1,
                "hint": "Grass leaves have parallel veins; mango or pea leaves have a branched network.",
                "explanation": "Monocots (like wheat and maize) show parallel leaf venation, while dicots (like mango and pea) show reticulate, net-like venation."
            }
        ]
    },
    {
        "id": 11,
        "title": "Lower Invertebrate Phyla",
        "subtitle": "Section 12.6.5: Porifera, Cnidaria, Platyhelminthes & Nematoda",
        "speech": (
            "Kingdom Animalia comprises multicellular, eukaryotic heterotrophs that lack cell walls and exhibit sensory "
            "coordination and active motility! Animals are classified broadly by the presence or absence of a supportive notochord "
            "into Invertebrates and Chordates. Among lower invertebrates, Phylum Porifera represents the most primitive animals: "
            "sessile aquatic sea sponges possessing cellular-level organization without true tissues. Sponges circulate water through "
            "thousands of microscopic pores called ostia, filtering up to twenty-four thousand liters of seawater per kilogram daily "
            "to extract bacterial nutrients! Advancing to tissue-level organization, Phylum Cnidaria includes freshwater Hydra, marine "
            "jellyfish, and reef-building corals. Cnidarians display radial symmetry, a single central gastrovascular opening, and "
            "waving tentacles armed with stinging cnidocyte cells that paralyze microscopic prey. Next, Phylum Platyhelminthes introduces "
            "bilateral symmetry and organ-level organization in dorsoventrally flattened flatworms, including free-living Planaria and "
            "parasitic tapeworms equipped with adhesive hooks and suckers. Finally, Phylum Nematoda comprises unsegmented cylindrical "
            "roundworms like Ascaris, which achieve organ-system level complexity and introduce a complete, through-gut digestive "
            "tract possessing two separate openings: a mouth for ingestion and an anus for egestion! Personal hygiene, sanitation, and "
            "safe drinking water prevent parasitic roundworm and flatworm infections across human populations, highlighting taxonomy's "
            "direct biomedical relevance to public health."
        ),
        "checkpoints": [
            {
                "question": "Which primitive invertebrate phylum displays a porous body filter-feeding system with cellular-level organization?",
                "options": [
                    "Arthropoda",
                    "Porifera (Sponges)",
                    "Mollusca",
                    "Chordata"
                ],
                "answer": 1,
                "hint": "Pore-bearing animals with ostia and an osculum.",
                "explanation": "Porifera (sponges) are pore-bearing, sessile aquatic animals with cellular-level organization and an internal water canal system."
            },
            {
                "question": "What major digestive evolutionary milestone appears in Phylum Nematoda (roundworms)?",
                "options": [
                    "Complete absence of any stomach or intestines",
                    "A complete digestive tract with two separate openings: mouth and anus",
                    "Photosynthetic stomach chambers containing green algae",
                    "Digestion occurring entirely outside the body using venomous fangs"
                ],
                "answer": 1,
                "hint": "Nematodes evolved a one-way tube with separate entry and exit points.",
                "explanation": "Nematodes possess a complete digestive system with both a mouth and an anus, allowing continuous, specialized digestion."
            }
        ]
    },
    {
        "id": 12,
        "title": "Higher Invertebrate Phyla",
        "subtitle": "Section 12.6.5: Annelida, Arthropoda, Mollusca, Echinodermata & Protochordates",
        "speech": (
            "Higher invertebrates demonstrate sophisticated organ systems, true body cavities, and specialized locomotion! "
            "Phylum Annelida, comprising earthworms and leeches, introduces true segmentation, known as metamerism, and a true internal "
            "fluid-filled body cavity called a coelom lined by mesoderm. Earthworms utilize coordinated circular and longitudinal "
            "body muscles alongside microscopic bristle-like setae to burrow through soil, aerating farmland. Phylum Arthropoda represents "
            "the largest, most triumphant animal group on Earth, encompassing insects, spiders, and crabs! Arthropods possess jointed "
            "appendages, segmented body tagmata, and a lightweight, waterproof exoskeleton composed of tough chitin that must be shed "
            "periodically through molting. Next, Phylum Mollusca includes soft-bodied creatures like snails, bivalves, and octopuses, "
            "characterized by a muscular locomotion foot, a visceral mass, and a glandular mantle fold that secretes a protective calcareous "
            "shell. Phylum Echinodermata comprises exclusively marine spiny-skinned animals like starfish and sea urchins, featuring a "
            "calcium carbonate endoskeleton, adult radial symmetry, and a unique hydraulic water vascular system powering suction tube "
            "feet for locomotion! Finally, bridging non-chordates and vertebrates are the primitive Protochordates, such as the marine "
            "lancelet Amphioxus. Protochordates possess a flexible, rod-like internal support called a notochord during at least one "
            "life stage, foreshadowing the evolutionary emergence of backboned vertebrates."
        ),
        "checkpoints": [
            {
                "question": "What external structural hallmark allows Phylum Arthropoda to be the most species-rich animal phylum on Earth?",
                "options": [
                    "A soft gelatinous body that dissolves in sunlight",
                    "Jointed appendages and a durable, waterproof chitinous exoskeleton",
                    "A single opening serving as both mouth and anus",
                    "Radial symmetry with a water vascular canal"
                ],
                "answer": 1,
                "hint": "Arthro = jointed, Poda = foot; covered by a chitinous suit of armor.",
                "explanation": "Arthropods possess jointed appendages and a protective, waterproof chitinous exoskeleton, allowing adaptation to almost every habitat."
            },
            {
                "question": "What primitive skeletal structure characterizes Protochordates like Amphioxus?",
                "options": [
                    "A bony skull containing a mammalian brain",
                    "A flexible, rod-like supportive notochord running along the dorsal body axis",
                    "A calcareous spiral shell secreted by a mantle",
                    "A porous network of glass sponge spicules"
                ],
                "answer": 1,
                "hint": "This rod provides internal axial support before the evolution of a vertebral backbone.",
                "explanation": "Protochordates possess a dorsal, flexible notochord that provides axial structural support without forming a true bony vertebral column."
            }
        ]
    },
    {
        "id": 13,
        "title": "Vertebrates & Adaptations",
        "subtitle": "Sections 12.6.5 & 12.7: Five Vertebrate Classes, Adaptations & Disaster Barriers",
        "speech": (
            "In subphylum Vertebrata, the primitive embryonic notochord is replaced during development by a jointed, internal "
            "bony or cartilaginous vertebral column, or backbone! Vertebrates are grouped into five major classes illustrating exquisite "
            "adaptive radiation across aquatic and terrestrial biomes. Pisces, or fish, are streamlined aquatic vertebrates breathing "
            "dissolved oxygen through vascular gills and pumping blood via a two-chambered heart. Amphibians, like frogs and salamanders, "
            "bridge land and water: possessing moist, scaleless, respiratory skin, a three-chambered heart, and a life cycle requiring aquatic "
            "larval metamorphosis. Class Reptilia achieved terrestrial independence through dry, cornified epidermal scales preventing water "
            "loss, cold-blooded poikilothermy, and internal fertilisation yielding yolk-rich, leathery shelled eggs. Class Aves, or birds, "
            "mastered aerial flight through warm-blooded homeothermy, insulating feathers, modified forelimb wings, lightweight hollow pneumatic "
            "bones, and efficient four-chambered hearts! Finally, Class Mammalia is distinguished by insulating body hair, external ear pinnae, "
            "a four-chambered heart, and specialized mammary glands that produce nourishing breast milk for live-born young! Healthy, biodiverse "
            "ecosystems act as crucial natural disaster barriers: dense mangrove forests shielded coastal Odisha from catastrophic tidal waves "
            "during the nineteen ninety-nine super cyclone, and intact Western Ghats rainforests buffer zoonotic viral pathogens like Kyasanur "
            "Forest Disease, highlighting nature's protective bioshields."
        ),
        "checkpoints": [
            {
                "question": "Which combination of physiological characteristics uniquely defines Class Mammalia?",
                "options": [
                    "Feathered wings, hollow pneumatic bones, and toothless beaks",
                    "Mammary glands producing milk, insulating body hair, four-chambered heart, and giving birth to live young",
                    "Moist glandular skin, gills, and cold-blooded two-chambered circulation",
                    "Dry epidermal scales and laying soft jelly eggs in open ponds"
                ],
                "answer": 1,
                "hint": "Mammals nurse their offspring with milk and possess body hair.",
                "explanation": "Mammals are warm-blooded vertebrates characterized by mammary glands, hair/fur, a 4-chambered heart, and internal embryo development (viviparity)."
            },
            {
                "question": "How did coastal mangrove ecosystems protect local communities during the 1999 Odisha super cyclone?",
                "options": [
                    "By generating artificial electrical lightning storms",
                    "Dense mangrove root networks absorbed storm surges and drastically dissipated violent tidal wave energy",
                    "By causing the cyclone winds to freeze into solid ice",
                    "By pumping seawater into deep subterranean aquifers"
                ],
                "answer": 1,
                "hint": "Stilted tangled mangrove roots absorb the physical kinetic impact of high tidal waves.",
                "explanation": "Mangrove forests serve as living bioshields, their dense intertwined stilt root systems dissipating kinetic wave energy and buffering storm surges."
            }
        ]
    },
    {
        "id": 14,
        "title": "Taxonomic Hierarchy Levels",
        "subtitle": "Section 12.7.1: The 7 Obligate Ranks from Kingdom to Species (Tiger & Pea)",
        "speech": (
            "Biological classification organizes the living world into a nested, step-by-step framework known as the taxonomic "
            "hierarchy! First conceptualized by Carolus Linnaeus, this system arranges organisms into seven obligate hierarchical "
            "ranks: Kingdom, Phylum for animals or Division for plants, Class, Order, Family, Genus, and Species. At the broad "
            "summit lies Kingdom, which unites vast, diverse assemblages of organisms sharing only fundamental cellular and nutritional "
            "features, such as all multicellular motile animals grouped under Kingdom Animalia. As one descends through Phylum, Class, "
            "Order, and Family, organisms share progressively more specific anatomical, physiological, and behavioral similarities. The "
            "penultimate rank is Genus, grouping closely related species that share common structural features, while the fundamental "
            "base unit is Species—a group of closely related individual organisms capable of interbreeding in nature to produce fertile "
            "offspring! Consider the royal Bengal tiger: Kingdom Animalia, Phylum Chordata, Class Mammalia, Order Carnivora, Family Felidae, "
            "Genus Panthera, and Species tigris. Similarly, the garden pea plant is classified as Kingdom Plantae, Division Magnoliophyta, "
            "Class Magnoliopsida, Order Fabales, Family Fabaceae, Genus Pisum, and Species sativum! This hierarchical structure provides "
            "an orderly, universal roadmap connecting every living organism to its precise evolutionary lineage, revealing the profound "
            "genealogical continuity uniting all earthly life."
        ),
        "checkpoints": [
            {
                "question": "What is the correct descending order of the seven standard taxonomic ranks?",
                "options": [
                    "Species -> Genus -> Family -> Order -> Class -> Phylum -> Kingdom",
                    "Kingdom -> Phylum (or Division) -> Class -> Order -> Family -> Genus -> Species",
                    "Class -> Order -> Kingdom -> Phylum -> Family -> Species -> Genus",
                    "Kingdom -> Family -> Class -> Order -> Phylum -> Genus -> Species"
                ],
                "answer": 1,
                "hint": "From broadest (Kingdom) to most specific basic unit (Species).",
                "explanation": "The taxonomic hierarchy descends from Kingdom to Phylum/Division, Class, Order, Family, Genus, and finally Species."
            },
            {
                "question": "What defines a biological 'species' as the fundamental base unit of taxonomic classification?",
                "options": [
                    "Any group of organisms living on the same mountain",
                    "A group of closely related individual organisms capable of naturally interbreeding to produce fertile offspring",
                    "All animals that have the exact same body weight",
                    "Any plant that blooms during winter months"
                ],
                "answer": 1,
                "hint": "Members of a species share a gene pool and interbreed to produce fertile young.",
                "explanation": "A species consists of individuals sharing common genetic ancestry who can interbreed naturally to produce viable, fertile offspring."
            }
        ]
    },
    {
        "id": 15,
        "title": "Binomial Scientific Naming",
        "subtitle": "Section 12.8: Linnaean Nomenclature Rules, Three Domains & The Purple Frog",
        "speech": (
            "Because common local names for plants and animals vary dramatically across languages and regions, biological science "
            "relies on a standardized universal naming method called binomial nomenclature! Formulated by Swedish botanist Carolus Linnaeus, "
            "this system assigns every discovered species a unique, two-part scientific name derived from Latin. The first word denotes "
            "the Genus to which the organism belongs and is always capitalized. The second word denotes the specific Species epithet "
            "and is written in lowercase. When printed in books, scientific names are italicized, as in Panthera tigris for the tiger or "
            "Homo sapiens for modern humans; when handwritten, the genus and species words must be underlined separately! Classification "
            "systems continuously evolve as molecular analytical tools advance. In nineteen seventy-seven, American microbiologist Carl Woese "
            "analyzed ribosomal RNA gene sequences and introduced the Three Domain system, dividing all life into Domain Bacteria, Domain "
            "Archaea, and Domain Eukarya, demonstrating that ancient Archaea are fundamentally distinct from true bacteria! Indian field "
            "discoveries continually enrich taxonomy: in two thousand and three, scientists discovered the bizarre Purple Frog, named "
            "Nasikabatrachus sahyadrensis, burrowed underground in Kerala's Sahyadri Hills. This living fossil belongs to a lineage that "
            "diverged over one hundred million years ago, proving our subcontinent's deep evolutionary antiquity."
        ),
        "checkpoints": [
            {
                "question": "According to the international rules of binomial nomenclature, how must a scientific name be formatted?",
                "options": [
                    "Both genus and species words must be fully capitalized and written in English",
                    "The genus name is capitalized, the species name is lowercase, and both are italicized (or underlined separately when handwritten)",
                    "The species name comes first, followed by the country where it was found",
                    "Names are written entirely in numbers without any alphabet letters"
                ],
                "answer": 1,
                "hint": "Genus capitalized, species lowercase, Latinized, and italicized or underlined.",
                "explanation": "Binomial names have a capitalized Genus, lowercase species epithet, Latin roots, and are italicized in print or underlined when handwritten."
            },
            {
                "question": "What molecular breakthrough led Carl Woese to propose the Three Domain system (Bacteria, Archaea, Eukarya) in 1977?",
                "options": [
                    "Weighing animals on mechanical laboratory balances",
                    "Comparative sequencing of ribosomal RNA (rRNA) revealing fundamental genetic differences between Archaea and Bacteria",
                    "Counting the number of petals on rose flowers",
                    "Observing pond water with hand magnifying glasses"
                ],
                "answer": 1,
                "hint": "Ribosomal RNA gene sequencing revealed that Archaea are distinct from true Bacteria.",
                "explanation": "Carl Woese compared 16S ribosomal RNA gene sequences, proving Archaea constitute a distinct ancient domain separate from Bacteria and Eukarya."
            }
        ]
    },
    {
        "id": 16,
        "title": "Fossils & Conservation",
        "subtitle": "Sections 12.9 & 12.10: Sedimentary Strata, Birbal Sahni & Loktak Phumdis",
        "speech": (
            "The physical history of biodiversity is indelibly recorded in the Earth's crust as fossils—the preserved "
            "remains, mineralized impressions, or traces of prehistoric organisms encased in sedimentary rock strata! Examining rock "
            "layers demonstrates a clear evolutionary progression: deeper, older geological strata contain simple, primitive organisms "
            "such as ancient bacteria and trilobites, while upper, newer strata contain complex, modern flowering plants and mammals. We "
            "honor visionary Indian paleobotanist Birbal Sahni, who founded the world-renowned Birbal Sahni Institute of Palaeosciences "
            "in Lucknow, deciphering fossilized plant anatomy and proving that the Indian tectonic plate drifted from the ancient southern "
            "supercontinent Gondwana! Today, however, Earth's extraordinary biodiversity faces severe anthropogenic crises driven by rapid "
            "habitat destruction, deforestation, industrial pollution, invasive alien species, and accelerating climate change. In Manipur, "
            "the unique floating organic biomass islands known as phumdis on Loktak Lake—protected within Keibul Lamjao National Park—provide "
            "the solitary remaining habitat for the critically endangered Sangai deer, also celebrated as the dancing deer of India! Safeguarding "
            "such delicate ecosystems requires rigorous scientific classification, extensive habitat preservation, strict environmental legislation, "
            "and passionate civic stewardship to ensure that Earth's marvelous living patterns continue flourishing vibrantly for future generations, "
            "preserving the precious genetic heritage of our living biosphere."
        ),
        "checkpoints": [
            {
                "question": "What geological pattern is revealed when examining fossils in undisturbed sedimentary rock strata?",
                "options": [
                    "Complex modern mammals are always found in the deepest, oldest rock layers",
                    "Deeper, older rock strata contain simpler organisms, while upper, newer strata contain progressively more complex forms",
                    "All fossils across all rock layers are completely identical in size and shape",
                    "Fossils only exist in volcanic lava that erupted yesterday"
                ],
                "answer": 1,
                "hint": "Law of superposition: older rocks are at the bottom, showing simpler ancestral forms.",
                "explanation": "Sedimentary layers show that simpler organisms appear in older, deeper layers, tracing the progressive evolutionary history of life."
            },
            {
                "question": "What unique ecosystem feature in Manipur's Keibul Lamjao National Park supports the endangered Sangai deer?",
                "options": [
                    "Subterranean marble caves filled with ice crystals",
                    "Floating organic biomass mats termed 'phumdis' on Loktak Lake",
                    "Artificial indoor greenhouse domes",
                    "Desert sand dunes surrounded by cactus hedges"
                ],
                "answer": 1,
                "hint": "The world's only floating national park on Loktak Lake.",
                "explanation": "Keibul Lamjao National Park features floating heterogeneous mats of vegetation, soil, and organic matter called phumdis on Loktak Lake, home to the Sangai deer."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        title_len = len(s["title"].split())
        print(f"Slide {s['id']}: Title='{s['title']}' ({title_len} words), Speech={wc} words")
        assert 1 <= title_len <= 3, f"Title length {title_len} not 1-3 words"
        assert 195 <= wc <= 215, f"Speech word count {wc} not in 195-215"

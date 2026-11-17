# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 7: How do Organisms Reproduce?
Part 1: Slides 1 to 8 Generator
Strict constraints:
- Title: 1 to 3 words
- Speech: strictly 195 to 215 words for slides 1 to 16
- 2 checkpoints per slide with 4 options, hint, and explanation
- Zero fictional names, zero persona titles
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Reproduction Biological Purpose",
        "subtitle": "Why Organisms Reproduce & The Preservation of Species Identity",
        "speech": (
            "Welcome to our study of reproduction in living organisms. Unlike fundamental life processes such as cellular "
            "nutrition, aerobic respiration, and waste excretion, reproduction is not necessary to sustain the immediate physical "
            "survival of an individual organism. A starving or suffocating creature perishes quickly, but an organism that never "
            "reproduces lives out its full biological lifespan completely undisturbed. Why then do living organisms spend enormous "
            "amounts of biological energy creating new individuals? The essential answer lies in species continuity and ecological "
            "visibility. If a biological species consisted of only a single individual without the capacity for reproduction, "
            "that entire unique lineage would vanish permanently whenever that solitary organism died. Large thriving populations "
            "of organisms exist across the planet only because countless individuals continually reproduce, steadily replacing older "
            "dying members and maintaining their ongoing numerical presence in ecological habitats. Furthermore, organisms look remarkably "
            "alike because their basic bodily blueprints are similar. Organisms classified within the same species share recognizable "
            "body contours, limb arrangements, physiological metabolic pathways, and anatomical configurations because they inherit "
            "identical biological instructions. Reproduction is therefore fundamentally an act of genetic blueprint replication, "
            "ensuring that newly formed generations inherit structural stability while perpetuating species presence across planetary "
            "ecosystems and vast evolutionary epochs."
        ),
        "checkpoints": [
            {
                "question": "Why is reproduction considered non-essential for an individual's immediate survival?",
                "options": [
                    "It consumes minimal energy compared to digestion",
                    "An individual survives normally without reproducing, unlike respiration or excretion",
                    "It only occurs in multicellular higher animals",
                    "It prevents the accumulation of genetic variations"
                ],
                "answer": 1,
                "hint": "Consider whether an organism dies immediately if it does not produce offspring.",
                "explanation": "Nutrition, respiration, and excretion are vital for immediate cellular survival, whereas an organism can live out its full life without reproducing."
            },
            {
                "question": "What primary biological factor makes individuals of the same species look remarkably similar?",
                "options": [
                    "They occupy identical physical climates simultaneously",
                    "They synthesize proteins from identical body design blueprints",
                    "They ingest identical nutrients in similar quantities",
                    "Their cells reproduce solely through fragmentation"
                ],
                "answer": 1,
                "hint": "Focus on the inherited genetic blueprint stored in the nucleus.",
                "explanation": "Organisms appear similar because their cells reproduce using similar genetic blueprints, directing the synthesis of matching proteins and structural tissues."
            }
        ]
    },
    {
        "id": 2,
        "title": "DNA Replication Blueprint",
        "subtitle": "Chemical Information Inheritance & Biochemical Copying Inaccuracies",
        "speech": (
            "At the deep molecular heart of cellular reproduction lies the genetic master molecule deoxyribonucleic acid, universally "
            "known as DNA. Inside the nucleus of every eukaryotic cell, chromosomes carry structural hereditary information encoded within "
            "their DNA strands, functioning as the master architectural blueprint for synthesizing cellular proteins. If this coded "
            "information is chemically altered, different enzymes and structural proteins are produced, modifying cellular structures and "
            "ultimately altering gross body design. When a cell prepares to divide, it employs precise biochemical reactions to synthesize "
            "faithful duplicates of its DNA molecules. However, simply duplicating DNA strands alone is completely inadequate to perpetuate "
            "living cells. An isolated strand of bare DNA separated from its cellular machinery cannot conduct cellular respiration, absorb "
            "nutrients, or sustain metabolism. Therefore, DNA copying is consistently accompanied by the simultaneous synthesis of an "
            "additional cellular apparatus, encompassing fresh cytoplasm, enzyme complexes, and functional membrane organelles. When the parent "
            "cell cleaves, each resulting daughter cell receives its own complete DNA strand enveloped by active metabolic machinery. Crucially, "
            "no biochemical reaction achieves absolute mathematical perfection. Every copying cycle introduces subtle chemical variations. While "
            "severe copying errors yield non-viable cells that perish rapidly, subtle variations produce viable offspring that remain structurally "
            "similar yet distinct, providing the foundation for evolutionary progress."
        ),
        "checkpoints": [
            {
                "question": "Why must DNA copying be accompanied by the creation of an additional cellular apparatus?",
                "options": [
                    "DNA cannot survive or carry out metabolic reactions without cellular machinery",
                    "Cellular apparatus protects DNA from being replicated too quickly",
                    "Proteins must be dismantled before nuclear division occurs",
                    "Cellular apparatus eliminates all potential genetic mutations"
                ],
                "answer": 0,
                "hint": "Consider whether an isolated DNA strand can metabolize nutrients on its own.",
                "explanation": "A naked DNA copy without cytoplasm, organelles, and enzymes cannot sustain metabolic activity, so a complete cellular apparatus must accompany each copy."
            },
            {
                "question": "What is the biological outcome of subtle chemical variations occurring during DNA replication?",
                "options": [
                    "Immediate death of all newly formed daughter cells",
                    "Complete loss of chromosomes in the subsequent generation",
                    "Creation of viable offspring that are similar yet distinct, fostering evolution",
                    "Total conversion from sexual to asexual reproduction"
                ],
                "answer": 2,
                "hint": "Think about how diversity arises without destroying the organism.",
                "explanation": "Subtle variations keep daughter cells structurally viable and similar to parents while introducing individual diversity essential for evolutionary adaptation."
            }
        ]
    },
    {
        "id": 3,
        "title": "Evolutionary Variation Importance",
        "subtitle": "Niche Stability, Environmental Shocks & Population Survival",
        "speech": (
            "The high fidelity of DNA copying during reproduction is vital because it preserves specific anatomical and physiological "
            "traits, enabling a biological population to inhabit and effectively exploit a defined ecological niche. Organisms establish "
            "specialized feeding structures, metabolic enzymes, and climatic tolerances specifically tailored to their localized environmental "
            "habitats. Nevertheless, ecological niches are never permanently immutable. The planetary biosphere undergoes drastic shifts caused "
            "by global climate change, sharp temperature fluctuations, fluctuating water tables, or catastrophic external impacts. If a "
            "population consists exclusively of genetically uniform clones lacking variation, any sudden environmental catastrophe can wipe out "
            "every individual simultaneously, driving the entire species into extinction. Consider a dense bacterial colony flourishing in "
            "temperate freshwater ponds. If global warming or sudden industrial thermal effluent sharply elevates the pond water temperature, "
            "all typical bacteria accustomed to cool conditions will perish immediately. However, if subtle copying variations during DNA "
            "replication had previously produced a few heat-resistant mutant variants within the population, those rare individuals survive "
            "the severe thermal stress, reproduce rapidly, and establish a thriving resilient colony. Variation may not offer immediate "
            "perceptible benefits to an individual during stable periods, but it serves as an indispensable survival buffer protecting entire "
            "species against unpredictable environmental catastrophes."
        ),
        "checkpoints": [
            {
                "question": "How does genetic variation benefit a species during an environmental catastrophe?",
                "options": [
                    "It guarantees that every single individual will survive untouched",
                    "It ensures some adapted variants survive to continue the species lineage",
                    "It converts multicellular organisms back into simple single cells",
                    "It eliminates the need for ongoing cellular DNA replication"
                ],
                "answer": 1,
                "hint": "Recall the scenario of temperate pond bacteria exposed to high heat.",
                "explanation": "While most uniform individuals perish during drastic environmental shifts, pre-existing resistant variants survive and replenish the population."
            },
            {
                "question": "Why is consistency in DNA copying important for organisms living in stable niches?",
                "options": [
                    "It allows organisms to change species classification every generation",
                    "It maintains body design features optimized for exploiting that specific niche",
                    "It prevents the organism from utilizing cellular respiration enzymes",
                    "It stops the organism from growing beyond microscopic dimensions"
                ],
                "answer": 1,
                "hint": "Consider how specialized body designs match environmental demands.",
                "explanation": "Accurate DNA replication ensures that offspring inherit the precise anatomical and physiological adaptations needed to thrive in their ecological niche."
            }
        ]
    },
    {
        "id": 4,
        "title": "Cellular Fission Modes",
        "subtitle": "Binary Fission Orientations & Multiple Fission in Protozoans",
        "speech": (
            "Single-celled microscopic organisms exhibit distinct modes of asexual fission depending upon their structural complexity and cellular "
            "polarity. In the simplest unicellular organisms like Amoeba, reproduction takes place via simple binary fission, where the mature "
            "parent cell splits into two equal daughter cells. Because Amoeba possesses an irregular, continually shifting body contour without "
            "fixed polarity, nuclear division and subsequent cytoplasmic constriction can occur across any arbitrary geometric plane. First, the "
            "nucleus elongates and divides by karyokinesis, followed by cytokinesis cleaving the cell into two independent amoebae. In contrast, "
            "protozoans with higher organizational structure display strictly oriented fission. Leishmania, the pathogenic parasite responsible "
            "for causing the disease Kala-azar or black fever, possesses a specialized whip-like flagellum anchored at one end of its elongated "
            "body. In Leishmania, binary fission occurs strictly in a definite longitudinal orientation relative to this flagellar apparatus, "
            "ensuring that each resulting daughter cell inherits correct bilateral symmetry and organized motility structures. Meanwhile, other "
            "parasitic protozoans undergo multiple fission under adverse conditions. In Plasmodium, the microscopic malarial parasite, the parent "
            "cell constructs a durable protective cyst wall. Inside this cyst, the nucleus undergoes repeated divisions into numerous daughter nuclei. "
            "Each nucleus gathers surrounding cytoplasm, producing dozens of daughter cells simultaneously that burst forth when the cyst ruptures."
        ),
        "checkpoints": [
            {
                "question": "How does binary fission in Leishmania differ from binary fission in Amoeba?",
                "options": [
                    "Leishmania reproduces solely inside a protective cyst wall",
                    "Leishmania splits in a definite longitudinal orientation relative to its whip-like flagellum",
                    "Amoeba forms hundreds of daughter cells simultaneously in every cycle",
                    "Amoeba requires two parent cells to exchange nuclear genetic material"
                ],
                "answer": 1,
                "hint": "Notice the specialized whip-like appendage on Leishmania.",
                "explanation": "Amoeba splits across any plane due to its amoeboid shape, while Leishmania divides strictly along a definite plane aligned with its flagellar structure."
            },
            {
                "question": "Which of the following organisms reproduces via multiple fission inside a protective cyst?",
                "options": [
                    "Spirogyra",
                    "Planaria",
                    "Plasmodium",
                    "Hydra"
                ],
                "answer": 2,
                "hint": "Think of the microscopic parasite responsible for causing malaria.",
                "explanation": "Plasmodium, the malarial parasite, undergoes repeated nuclear divisions within a cyst to produce numerous daughter cells simultaneously via multiple fission."
            }
        ]
    },
    {
        "id": 5,
        "title": "Budding Fragmentation Regeneration",
        "subtitle": "Asexual Mechanisms in Yeast, Spirogyra, Planaria & Hydra",
        "speech": (
            "Asexual reproduction in simple organisms encompasses diverse specialized mechanisms including budding, fragmentation, and "
            "regenerative growth. In unicellular baker's yeast, a small protuberance or bud emerges from the parent cell wall. Following mitotic "
            "nuclear division, one daughter nucleus migrates into the expanding bud, which constricts at its base, separates, and matures into an "
            "independent yeast cell. In simple multicellular green algae such as Spirogyra, mature filaments simply break into smaller fragments "
            "upon reaching maturity. Each detached fragment undergoes simple mitotic cell divisions, rapidly elongating into a complete new "
            "filament. However, complex multicellular animals cannot reproduce by fragmentation because their differentiated cells are permanently "
            "organized into specialized tissues, localized organs, and intricate organ systems that cannot reassemble from random pieces. In "
            "contrast, simple animals like Hydra and Planaria possess remarkable regenerative capacities. If a Planaria flatworm is cut into several "
            "segments, specialized proliferating stem cells at each wound site divide rapidly, forming a mass of undifferentiated cells that "
            "subsequently differentiate into missing tissues, reconstructing complete worms. Similarly, Hydra utilizes regenerative cells located "
            "at a specific body locus to develop an external bud, which grows tentacles and a mouth before detaching. Importantly, natural regeneration "
            "functions primarily as an injury repair response rather than planned reproduction."
        ),
        "checkpoints": [
            {
                "question": "Why can simple Spirogyra reproduce by fragmentation whereas complex organisms cannot?",
                "options": [
                    "Spirogyra possesses complex internal organ systems throughout its filament",
                    "Complex organisms have specialized cells arranged in definite tissues and organs that cannot be reformed from random pieces",
                    "Spirogyra produces motile flagellated gametes for fragmentation",
                    "Complex organisms lack cell membranes capable of undergoing mitosis"
                ],
                "answer": 1,
                "hint": "Consider the high degree of structural specialization in higher animals.",
                "explanation": "In complex organisms, tissues and organs are organized at fixed locations, making simple bodily breakdown into viable fragments biologically impossible."
            },
            {
                "question": "How does budding in Hydra lead to the formation of a separate new individual?",
                "options": [
                    "The parent Hydra breaks into equal halves along its longitudinal axis",
                    "Regenerative cells divide repeatedly at a specific site to form an outgrowth that matures and detaches",
                    "Spores are released into the surrounding water from apical tentacles",
                    "The nucleus divides multiple times inside an impermeable cyst"
                ],
                "answer": 1,
                "hint": "Look for repeated cell division forming an external outgrowth.",
                "explanation": "In Hydra, regenerative cells form a localized bud that develops miniature tentacles and a mouth before detaching from the parent body."
            }
        ]
    },
    {
        "id": 6,
        "title": "Vegetative Propagation Techniques",
        "subtitle": "Natural Plant Structures, Horticultural Cuttings & Tissue Culture",
        "speech": (
            "Vegetative propagation represents a widespread form of asexual reproduction in plants where new individuals develop directly from "
            "vegetative structures such as roots, stems, or leaves, entirely bypassing seeds and flowers. Under favorable environmental moisture, "
            "underground tubers like potato produce vigorous aerial shoots from dormant buds nestled inside surface depressions termed eyes. In "
            "the succulent plant Bryophyllum, adventitious foliar buds arise along the scalloped notches of mature leaf margins; when these leaves "
            "detach and fall onto moist garden soil, each notched bud sprouts roots and produces an independent plantlet. Horticulturalists exploit "
            "vegetative propagation commercially through artificial techniques such as stem cutting in sugarcane and roses, underground layering "
            "in jasmine, and branch grafting in commercial apple and mango orchards. This approach delivers outstanding agricultural benefits: "
            "vegetatively propagated crops produce flowers and marketable fruits significantly earlier than seed-grown plants. Furthermore, it "
            "allows the commercial propagation of seedless varieties such as bananas, naval oranges, seedless grapes, and ornamental roses that "
            "have lost the capacity to form viable seeds. Moreover, all offspring are genetically uniform clones of the parent stock, faithfully "
            "preserving prized commercial traits. Modern plant tissue culture extends this power by culturing shoot tip cells in sterile nutrient "
            "media to produce disease-free plantlets in massive quantities."
        ),
        "checkpoints": [
            {
                "question": "Where do vegetative buds form on Bryophyllum to produce independent new plantlets?",
                "options": [
                    "Inside underground tuberous taproots",
                    "Along the scalloped notches of the leaf margins",
                    "At the tips of aerial floral filaments",
                    "Within the inner vascular xylem cylinders"
                ],
                "answer": 1,
                "hint": "Think about the specialized leaf edges shown in NCERT Figure 7.5.",
                "explanation": "Bryophyllum develops adventitious buds in the notches along its leaf margins, which sprout roots and form new plants when contacting moist soil."
            },
            {
                "question": "What is an important commercial advantage of vegetative propagation in horticulture?",
                "options": [
                    "It doubles the chromosome number in every subsequent crop cycle",
                    "It allows propagation of seedless varieties like bananas and ensures earlier flowering",
                    "It eliminates the necessity of water for agricultural growth",
                    "It forces plants to undergo meiotic gamete fusion"
                ],
                "answer": 1,
                "hint": "Consider crops that do not produce viable seeds.",
                "explanation": "Vegetative propagation allows farmers to grow seedless varieties (such as banana and jasmine) and harvest fruits earlier than seed-propagated crops."
            }
        ]
    },
    {
        "id": 7,
        "title": "Rhizopus Spore Formation",
        "subtitle": "Fungal Mycelium, Sporangia Blobs & Resilient Asexual Spores",
        "speech": (
            "Spore formation serves as an exceptionally resilient asexual reproductive adaptation in terrestrial fungi such as Rhizopus, commonly "
            "known as black bread mould. When a moist slice of bread is left exposed in a warm shaded room, a delicate white cottony network "
            "rapidly carpets the substrate. This vegetative fungal body consists of horizontal, branching, thread-like structures called hyphae "
            "that secrete digestive enzymes and absorb organic nutrients. Upon reaching reproductive maturity, the fungal mycelium produces "
            "erect vertical hyphae topped by tiny, dark, globular capsules known as sporangia, frequently characterized as tiny blobs on sticks. "
            "Each sporangium functions as a protective chamber enclosing hundreds of microscopic asexual reproductive units known as spores. "
            "Crucially, every individual spore is enveloped by a thick, resilient, durable outer wall that shields the delicate inner cell against "
            "desiccation, temperature extremes, and nutrient scarcity. When the mature sporangium dries out, its outer wall ruptures, discharging "
            "clouds of lightweight spores into ambient air currents. Carried across considerable distances by breezes, when a spore eventually "
            "settles upon a favorable moist, nutrient-rich surface, its protective wall softens, permitting the spore to germinate, emerge as a "
            "germ tube, and rapidly establish a thriving new fungal mycelium without requiring gamete fusion."
        ),
        "checkpoints": [
            {
                "question": "What structural feature enables Rhizopus spores to survive harsh, dry environmental conditions?",
                "options": [
                    "A motile flagellum that propels them toward water",
                    "A thick, durable protective wall shielding them against dehydration",
                    "High concentrations of contractile actin-myosin proteins",
                    "A diploid multicellular embryo ready for instant hatching"
                ],
                "answer": 1,
                "hint": "Focus on the protective outer layer of fungal spores.",
                "explanation": "Rhizopus spores are surrounded by thick, resistant outer walls that prevent desiccation until they encounter moist, nutrient-rich surfaces."
            },
            {
                "question": "In the bread mould Rhizopus, what is the specific reproductive structure containing spores?",
                "options": [
                    "Nutrient-absorbing horizontal hyphae",
                    "Terminal globular capsules called sporangia",
                    "Surface foliar vegetative notches",
                    "Adventitious root nodules"
                ],
                "answer": 1,
                "hint": "Recall the 'blob-on-a-stick' structure described in NCERT Section 7.2.6.",
                "explanation": "The erect aerial hyphae bear swollen globular capsules called sporangia, inside which hundreds of reproductive spores are formed."
            }
        ]
    },
    {
        "id": 8,
        "title": "Sexual Reproduction Logic",
        "subtitle": "Genetic Diversification, Meiotic Halving & Gamete Specialization",
        "speech": (
            "While asexual reproduction enables rapid clonal multiplication from a solitary parent, it produces genetically uniform offspring "
            "possessing limited adaptive variability. To overcome this evolutionary limitation, complex organisms developed sexual reproduction, "
            "which systematically combines accumulated genetic variations from two distinct parental individuals. By pooling DNA sequences "
            "originating from different genealogical lines, sexual reproduction creates novel, unprecedented combinations of genetic traits in "
            "every generation, tremendously enhancing species adaptability and accelerating evolutionary progress. However, combining full sets "
            "of chromosomes from two parents poses a formidable biological crisis: if each parent contributed a complete diploid complement of "
            "forty-six chromosomes, the offspring would possess ninety-two, doubling cellular DNA content in every succeeding generation and "
            "disrupting cellular genetics. Sexually reproducing organisms elegantly resolve this crisis through a specialized reduction division "
            "termed meiosis. During meiosis in reproductive organs, chromosome numbers and DNA content are precisely halved, producing haploid "
            "germ-cells or gametes carrying only a single chromosomal set. When male and female gametes fuse during fertilization, the species-specific "
            "diploid chromosome number is completely restored in the zygote. Furthermore, gametes undergo structural division of labor: the male "
            "gamete is small, streamlined, and actively motile, whereas the female gamete is significantly larger, stationary, and loaded with "
            "nutritive reserves."
        ),
        "checkpoints": [
            {
                "question": "Why is the reduction division (meiosis) essential in sexual reproduction?",
                "options": [
                    "It quadruples cellular DNA content to make offspring larger",
                    "It halves the chromosome number in germ-cells so fertilization restores the original species chromosome count",
                    "It completely stops the synthesis of cellular proteins in gametes",
                    "It converts diploid somatic cells directly into vegetative tubers"
                ],
                "answer": 1,
                "hint": "Consider what would happen if two full chromosome sets merged without prior halving.",
                "explanation": "Meiosis halves chromosome number in gametes (from 2n to n) so that fertilization restores the exact diploid number (2n) in the offspring."
            },
            {
                "question": "How do male and female gametes differ structurally in sexually reproducing organisms?",
                "options": [
                    "Male gametes are large and stationary; female gametes are tiny and motile",
                    "Male gametes are small and actively motile; female gametes are larger and packed with stored food",
                    "Both gametes are identical in size, motility, and nutrient storage",
                    "Male gametes lack DNA, while female gametes contain doubled DNA sets"
                ],
                "answer": 1,
                "hint": "Think about sperm mobility vs egg food storage.",
                "explanation": "Male gametes are streamlined and motile to reach the egg, whereas female gametes are larger, stationary, and stocked with nutrients to sustain the embryo."
            }
        ]
    }
]

print("=== CHECKING SLIDES 1 TO 8 DATA ===")
for s in slides_part1:
    wc = len(s['speech'].split())
    tw = len(s['title'].split())
    print(f"Slide {s['id']}: '{s['title']}' | Title words: {tw} | Speech words: {wc}")
    assert 1 <= tw <= 3, f"Title words out of range: {tw}"
    assert 195 <= wc <= 215, f"Speech words out of range: {wc}"
    assert len(s['checkpoints']) == 2, "Must have exactly 2 checkpoints"

with open('.agents/c10s_ch7_part1.json', 'w', encoding='utf-8') as f:
    json.dump(slides_part1, f, indent=2)

print("Saved .agents/c10s_ch7_part1.json successfully!")

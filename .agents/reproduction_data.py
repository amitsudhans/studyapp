#!/usr/bin/env python3
"""
Full data for NCERT Class 10 Science, Chapter 7: How do Organisms Reproduce?
Contains:
- 17 Content Slides with detailed theory, quotes, lead, teacher narration, 34 checkpoint questions, and simulator specifications
- 4 Quiz Challenge Slides with 40 questions and detailed step-by-step popup solutions
"""

CONTENT_SLIDES = [
    # Slide 1: Why do Organisms Reproduce? DNA Copying & Body Design (Pages 113-114)
    {
        "index": 0,
        "title": "Why Reproduce? The Role of DNA Copying in Reproduction",
        "short_title": "1. DNA Copying",
        "badge": "Chapter 7 • Section 7.1 (Pages 113–114)",
        "quote": "Reproduction is not essential to maintain the life of an individual organism, but it is essential for the perpetuation and survival of the species.",
        "lead": "Unlike respiration or nutrition, an individual organism can survive without reproducing. Yet organisms spend vast amounts of biological energy creating offspring. Reproduction at its most fundamental molecular level is the faithful replication of DNA blueprints.",
        "theory_blocks": [
            {
                "heading": "Why Do Organisms Reproduce?",
                "content": "• Individual survival depends on maintenance life processes (nutrition, respiration, excretion). However, without reproduction, existing individuals would age and die, leading to the rapid extinction of the entire species.<br>• Organisms belong to the same species because they share similar body designs. Similar body designs require similar genetic blueprints, stored in <strong>DNA (Deoxyribonucleic Acid)</strong> inside cell chromosomes."
            },
            {
                "heading": "DNA Copying & Creation of Cellular Apparatus (Pages 113–114)",
                "content": "• <strong>The Genetic Blueprint:</strong> DNA sequences in cell nuclei code for specific proteins. Altered DNA produces altered proteins, resulting in modified body structures.<br>• <strong>Cell Division Protocol:</strong> A reproducing cell uses enzyme reactions to duplicate its DNA. However, simply pushing one naked DNA molecule out of the cell would fail because it lacks organelles to sustain metabolism.<br>• Therefore, <strong>DNA copying is always accompanied by the creation of an additional cellular apparatus</strong> (mitochondria, ribosomes, membranes) before the cell physically divides into two daughter cells."
            }
        ],
        "narration": "Welcome students to Chapter 7: How do Organisms Reproduce! You can live your entire life without reproducing, so why do living things spend so much energy making babies? Because without reproduction, species would go extinct! At the heart of reproduction lies DNA copying. Your cell nucleus duplicates its DNA strands, builds a complete second cellular machinery, and splits into two viable new cells!",
        "interactive_type": "dna_replication_sim",
        "checkpoints": [
            {
                "q": "Why is the creation of a cellular apparatus necessary alongside DNA copying during cell division?",
                "options": [
                    "A naked DNA copy cannot survive or maintain life processes without surrounding cellular machinery and organelles",
                    "To change the color of the cell",
                    "DNA cannot exist inside a nucleus",
                    "Cells must double their weight before DNA can dissolve"
                ],
                "ans": 0,
                "solution": "A separated DNA copy without cytoplasm, enzymes, and organelles cannot maintain metabolic life processes. Therefore, DNA duplication must be matched by the synthesis of an additional cellular apparatus (NCERT Page 114)."
            },
            {
                "q": "What molecule located on chromosomes in the cell nucleus carries the inherited blueprints for making body proteins?",
                "options": [
                    "Hemoglobin",
                    "DNA (Deoxyribonucleic Acid)",
                    "Adrenaline",
                    "Chlorophyll"
                ],
                "ans": 1,
                "solution": "Chromosomes in the nucleus contain information for inheritance of features from parents to offspring in the form of DNA molecules (NCERT Page 113)."
            }
        ]
    },

    # Slide 2: Inbuilt Tendency for Variation & Importance in Ecological Niches (Page 114)
    {
        "index": 1,
        "title": "The Importance of Variation: Resilience in Changing Niches",
        "short_title": "2. Variation & Niches",
        "badge": "Section 7.1.1 • Page 114",
        "quote": "No biochemical copying reaction is absolutely reliable; inbuilt variations during DNA replication provide the raw material for species survival and evolution.",
        "lead": "Populations occupy specialized ecological niches. While faithful DNA copying ensures stability of body design, slight inaccuracies generate variations that rescue species from extinction when environments abruptly change.",
        "theory_blocks": [
            {
                "heading": "Origin of Variations in DNA Replication",
                "content": "• Biochemical reactions are not 100% precise. Small copying errors occur during DNA replication, producing daughter DNA molecules that are similar but not absolutely identical.<br>• <strong>Drastic Errors:</strong> If a DNA alteration is too extreme, the new DNA cannot cooperate with the inherited cellular apparatus; the cell dies.<br>• <strong>Subtle Variations:</strong> Non-lethal variations persist. This inbuilt tendency for variation during reproduction forms the bedrock of <strong>natural selection and organic evolution</strong>."
            },
            {
                "heading": "Importance of Variation in Ecological Niches (Page 114)",
                "content": "• <strong>Niche Stability vs Disruption:</strong> Consistent DNA copying keeps body features suited to a specific niche. But niches change unpredictably (global warming, droughts, asteroid strikes).<br>• <strong>The Heat-Resistant Bacteria Example:</strong> Consider a bacterial population living in temperate water. If global warming drastically raises water temperatures, the majority of standard bacteria will perish. However, a few variant individuals possessing thermal-resistant cell membranes will survive, multiply, and save the species from extinction!"
            }
        ],
        "narration": "Are daughter cells 100% carbon copies? No biochemical reaction is flawless! Tiny variations slip into DNA copies. While extreme errors kill the cell, subtle variations accumulate. Imagine a colony of temperate water bacteria: if global warming boils the lake, normal bacteria die—but lucky variants with heat-resistant mutations survive and reproduce! That's why variation is beneficial for the species, even if not vital for the single individual!",
        "interactive_type": "variation_niche_sim",
        "checkpoints": [
            {
                "q": "Why is genetic variation beneficial to a biological species even if it offers no immediate advantage to a single individual?",
                "options": [
                    "It ensures all individuals look identical",
                    "It provides a buffer against environmental catastrophes, enabling resistant variants to survive and prevent species extinction",
                    "It eliminates the need for DNA copying",
                    "It stops cell division permanently"
                ],
                "ans": 1,
                "solution": "If an ecological niche changes drastically (e.g., thermal spike), standard organisms may die, but pre-existing variants capable of withstanding the new condition survive to perpetuate the species (NCERT Page 114)."
            },
            {
                "q": "What happens if an error during DNA copying produces an alteration that is completely incompatible with the cell's machinery?",
                "options": [
                    "The cell transforms into a virus",
                    "The newborn cell cannot function and simply dies",
                    "The cell multiplies at tenfold speed",
                    "The cell switches to plant photosynthesis"
                ],
                "ans": 1,
                "solution": "If DNA copying errors are too drastic, the new DNA copy cannot coordinate with the inherited cellular apparatus, causing the newborn cell to die (NCERT Page 114)."
            }
        ]
    },

    # Slide 3: Asexual Reproduction: Binary Fission & Multiple Fission (Pages 115-116, Fig 7.1 & 7.2)
    {
        "index": 2,
        "title": "Fission: Binary Fission in Amoeba & Leishmania vs Multiple Fission",
        "short_title": "3. Fission Modes",
        "badge": "Section 7.2.1 • Pages 115–116",
        "quote": "In unicellular organisms, cell division or fission directly creates new individuals—splitting in any plane (Amoeba), a longitudinal plane (Leishmania), or multiple daughter cells (Plasmodium).",
        "lead": "Fission is the simplest mode of asexual reproduction where a parent unicellular organism divides into two or more independent daughter cells.",
        "theory_blocks": [
            {
                "heading": "Binary Fission: Amoeba vs Leishmania (Figure 7.1 a & b)",
                "content": "• <strong>Amoeba:</strong> Simple protozoan with irregular shape. During binary fission, the nucleus elongates and divides (karyokinesis), followed by cytoplasmic division (cytokinesis) in <em>any random plane</em> (Activity 7.3).<br>• <strong>Leishmania:</strong> Protozoan parasite that causes the disease <strong>kala-azar</strong> (black fever). It has higher structural organization with a whip-like <strong>flagellum</strong> at one end. Binary fission occurs in a <em>definite longitudinal orientation</em> relative to the flagellum."
            },
            {
                "heading": "Multiple Fission in Plasmodium (Figure 7.2)",
                "content": "• <strong>Plasmodium (Malarial Parasite):</strong> Under unfavorable conditions, the single cell forms a protective cyst wall.<br>• Inside the cyst, the nucleus divides repeatedly by mitosis into numerous nuclei surrounded by cytoplasm.<br>• When favorable conditions return, the cyst ruptures, releasing <strong>many daughter cells simultaneously</strong>."
            }
        ],
        "narration": "Let's explore fission! In Amoeba, the cell splits into two in any random direction. But look at Leishmania, the parasite causing kala-azar: it has a whip-like flagellum, so it must divide strictly in a longitudinal plane along its body axis! And what about Plasmodium, the malaria parasite? Inside a protective cyst, it undergoes multiple fission, dividing its nucleus repeatedly to burst open and release dozens of daughter cells all at once!",
        "interactive_type": "fission_comparison_sim",
        "checkpoints": [
            {
                "q": "How does binary fission in Leishmania differ from that in Amoeba?",
                "options": [
                    "Amoeba divides inside a cyst, whereas Leishmania does not",
                    "In Amoeba, division occurs in any plane; in Leishmania, binary fission occurs in a definite longitudinal orientation relative to its whip-like flagellum",
                    "Leishmania produces hundreds of cells simultaneously",
                    "Amoeba requires two parent organisms"
                ],
                "ans": 1,
                "solution": "Amoeba splits across any plane due to its irregular shape, while Leishmania has a whip-like flagellum at one end, restricting fission to a definite orientation (NCERT Page 115)."
            },
            {
                "q": "Which organism reproduces by multiple fission, dividing into many daughter cells simultaneously inside a cyst?",
                "options": [
                    "Amoeba",
                    "Hydra",
                    "Plasmodium (Malarial parasite)",
                    "Spirogyra"
                ],
                "ans": 2,
                "solution": "Plasmodium, the malarial parasite, undergoes multiple fission to produce many daughter cells simultaneously (NCERT Page 116, Figure 7.2)."
            }
        ]
    },

    # Slide 4: Fragmentation in Spirogyra & Why Complex Animals Cannot Fragment (Page 116, Activity 7.4)
    {
        "index": 3,
        "title": "Fragmentation in Spirogyra: Simplicity vs Tissue Complexity",
        "short_title": "4. Fragmentation",
        "badge": "Section 7.2.2 • Page 116 (Activity 7.4)",
        "quote": "Spirogyra simply breaks into fragments upon maturity; complex multicellular organisms cannot divide cell-by-cell because specialized tissues occupy definite anatomical positions.",
        "lead": "Why can green filamentous algae simply snap into pieces to reproduce, while complex animals like dogs, humans, or insects cannot?",
        "theory_blocks": [
            {
                "heading": "Fragmentation in Spirogyra (Activity 7.4)",
                "content": "• <strong>Spirogyra:</strong> A filamentous green alga with relatively simple, unspecialized body organization.<br>• Upon reaching maturity, the long green filament simply breaks into smaller fragments.<br>• Each fragment continues mitotic cell division and grows into a full, new Spirogyra individual."
            },
            {
                "heading": "Why Complex Multicellular Organisms Cannot Reproduce by Fragmentation",
                "content": "• Complex multicellular organisms are not random clusters of independent cells.<br>• Specialized cells are arranged into distinct <strong>tissues</strong>, tissues are built into specific <strong>organs</strong> (heart, kidneys, brain), and organs occupy fixed, definite positions inside organ systems.<br>• In such intricate architecture, simple cell-by-cell division or breaking into pieces would be lethal and impractical.<br>• Instead, complex organisms delegate reproduction to a dedicated lineage of specialized germ-cells capable of developmental proliferation."
            }
        ],
        "narration": "Activity 7.4 shows us Spirogyra, a simple green pond alga. When it matures, its filament snaps into smaller pieces, and each fragment grows into a brand new alga! But why can't a human or cat do this? Because complex organisms aren't just random piles of cells! Our specialized cells form tissues, organs, and organ systems positioned in exact anatomical spots. Breaking a dog in half destroys its organs—it cannot fragment! Complex life requires specialized reproductive germ cells!",
        "interactive_type": "fragmentation_spirogyra_sim",
        "checkpoints": [
            {
                "q": "Why can Spirogyra reproduce by fragmentation, whereas complex multicellular organisms cannot?",
                "options": [
                    "Spirogyra lives in water while complex organisms live on land",
                    "Spirogyra has a simple body organization of similar cells; complex organisms have specialized cells organized into tissues and organs placed at definite positions",
                    "Complex organisms lack cell membranes",
                    "Spirogyra does not possess DNA"
                ],
                "ans": 1,
                "solution": "Complex multicellular organisms have high tissue differentiation where specific organs perform vital functions at definite locations; random fragmentation would disrupt this organized architecture (NCERT Page 116)."
            },
            {
                "q": "In Activity 7.4, what happens when a mature Spirogyra filament breaks into fragments?",
                "options": [
                    "All fragments dissolve into pond water",
                    "Each individual fragment grows into a complete new Spirogyra filament",
                    "The fragments turn into fungal bread mould",
                    "The fragments fuse into a single seed"
                ],
                "ans": 1,
                "solution": "Upon maturation, Spirogyra filaments break into fragments, and each fragment elongates into a new individual alga (NCERT Page 116)."
            }
        ]
    },

    # Slide 5: Regeneration in Planaria and Hydra (Pages 116-117, Fig 7.3)
    {
        "index": 4,
        "title": "Regeneration: Developmental Re-growth in Planaria and Hydra",
        "short_title": "5. Regeneration",
        "badge": "Section 7.2.3 • Pages 116–117 (Figure 7.3)",
        "quote": "If Planaria is cut into pieces, each piece regenerates into a complete individual; yet regeneration is not the same as reproduction.",
        "lead": "Planaria and Hydra possess remarkable developmental powers. If accidentally sliced into multiple fragments, specialized stem-like cells proliferate and differentiate to reconstruct whole organisms.",
        "theory_blocks": [
            {
                "heading": "The Mechanism of Regeneration (Figure 7.3)",
                "content": "• If simple animals like <strong>Hydra</strong> or the flatworm <strong>Planaria</strong> are cut into any number of pieces, each piece can grow into a complete, viable individual.<br>• <strong>Specialized Regenerative Cells:</strong> Cut surfaces contain specialized cells that proliferate rapidly, forming a dense mass (blastema) of cells.<br>• <strong>Development & Differentiation:</strong> From this mass, cells migrate, change their molecular identity, and differentiate into specific tissues (epidermis, nervous cords, digestive tracts) in an organized sequence termed <em>development</em>."
            },
            {
                "heading": "Why Regeneration is NOT the Same as Reproduction",
                "content": "• Reproduction is a proactive, purposeful biological function undertaken naturally by healthy organisms to propagate their species.<br>• Most organisms do not normally rely on being sliced, crushed, or mutilated to reproduce! Regeneration is primarily an evolutionary repair and wound-healing adaptation."
            }
        ],
        "narration": "Meet the flatworm Planaria—a real-life superhero! If you cut Planaria into three pieces—head, middle, and tail—each single piece regenerates into a complete worm! Specialized regenerative cells multiply into a mass of cells, which then differentiate into eyespots, nerves, and guts. But remember: regeneration is NOT the same as reproduction! Animals don't wait around to be sliced in half to produce offspring; regeneration is an extraordinary injury repair adaptation!",
        "interactive_type": "regeneration_planaria_sim",
        "checkpoints": [
            {
                "q": "What cellular mechanism allows a severed fragment of Planaria to reconstruct a complete flatworm?",
                "options": [
                    "Surrounding water fills the void and turns into cells",
                    "Specialized regenerative cells proliferate into a mass of cells, which undergo organized differentiation into tissues and organs",
                    "The fragment captures bacteria and converts them into organs",
                    "The cut ends secrete calcium to grow a shell"
                ],
                "ans": 1,
                "solution": "Specialized regenerative cells multiply rapidly at the wound site and undergo morphogenetic differentiation to reform missing organs and body segments (NCERT Page 116-117)."
            },
            {
                "q": "Why is regeneration strictly distinguished from true biological reproduction?",
                "options": [
                    "Regenerated animals have no DNA",
                    "Organisms would not normally depend on being cut up or mutilated in order to reproduce",
                    "Regeneration only happens in plants",
                    "Regenerated parts always fall off within hours"
                ],
                "ans": 1,
                "solution": "Reproduction is a natural life cycle process; organisms do not rely on accidental injury or mechanical slicing to perpetuate their species (NCERT Page 117)."
            }
        ]
    },

    # Slide 6: Budding in Hydra and Yeast (Pages 115, 117, Fig 7.4, Activity 7.1)
    {
        "index": 5,
        "title": "Budding: Outgrowths in Hydra and Yeast",
        "short_title": "6. Budding",
        "badge": "Section 7.2.4 • Pages 115 & 117 (Figure 7.4)",
        "quote": "In Hydra, a bud develops as an outgrowth due to repeated cell division at one specific site, developing into a tiny individual that detaches when mature.",
        "lead": "Budding is an asexual strategy where a miniature progeny develops directly on the body wall of the parent through localized cell proliferation.",
        "theory_blocks": [
            {
                "heading": "Budding in Hydra (Figure 7.4)",
                "content": "• Hydra uses its regenerative cells for reproduction.<br>• A localized <strong>bud</strong> arises as a small protrusion or outgrowth caused by repeated mitotic cell divisions at one specific body site.<br>• The bud develops miniature tentacles and a mouth, nourished continuously by the parent.<br>• Upon reaching full maturity, the tiny Hydra constricts at its base, detaches from the parent body, and establishes an independent life."
            },
            {
                "heading": "Budding in Yeast (Activity 7.1)",
                "content": "• Yeast is a unicellular fungus. In warm sugar solution (Activity 7.1), yeast cells rapidly metabolize glucose.<br>• A small bulb-like projection, called a <strong>bud</strong>, emerges from the mother cell.<br>• The nucleus divides, and one daughter nucleus migrates into the bud.<br>• The bud can pinch off or remain attached, forming branching chains of yeast cells."
            }
        ],
        "narration": "Budding is nature's way of growing a clone on your shoulder! In Hydra, regenerative cells at one spot divide repeatedly to form a small bump called a bud. It develops its own tiny tentacles and mouth. Once fully grown, it simply detaches and swims off to live on its own! Yeast does something similar: in sweet, warm water, yeast cells sprout small buds that pinch off or form long clonal chains!",
        "interactive_type": "budding_hydra_yeast_sim",
        "checkpoints": [
            {
                "q": "How does budding occur in the freshwater animal Hydra?",
                "options": [
                    "The parent breaks into two equal halves along its center",
                    "A bud forms as an outgrowth due to repeated cell divisions at one specific site, which matures and detaches as a new individual",
                    "Hydra releases airborne seeds",
                    "The tentacles fall off and turn into worms"
                ],
                "ans": 1,
                "solution": "Repeated mitotic divisions of regenerative cells at a specific site produce an outgrowth (bud) that develops into a tiny individual before separating (NCERT Page 117, Figure 7.4)."
            },
            {
                "q": "What type of organism is yeast, and which asexual mode of reproduction does it exhibit in warm sugar solution (Activity 7.1)?",
                "options": [
                    "A multicellular bacterium that reproduces by fragmentation",
                    "A unicellular fungus that reproduces by budding",
                    "A photosynthetic alga that reproduces by multiple fission",
                    "A protozoan that reproduces by seed formation"
                ],
                "ans": 1,
                "solution": "Yeast is a single-celled fungus that reproduces rapidly through budding when provided with nutrients like warm sugar solution (Activity 7.1, Page 115)."
            }
        ]
    },

    # Slide 7: Vegetative Propagation in Plants (Pages 117-118, Fig 7.5, Activities 7.5 & 7.6)
    {
        "index": 6,
        "title": "Vegetative Propagation: Roots, Stems, Leaves & Agronomic Advantages",
        "short_title": "7. Vegetative Propagation",
        "badge": "Section 7.2.5 • Pages 117–118",
        "quote": "Vegetative propagation enables seedless plants to reproduce, produces flowers and fruits earlier, and preserves exact parental genetic characteristics.",
        "lead": "Unlike animals, many plants can regenerate whole new individuals directly from vegetative structures—roots, stems, or leaves—under suitable environmental conditions.",
        "theory_blocks": [
            {
                "heading": "Natural Vegetative Propagation Examples",
                "content": "• <strong>By Roots:</strong> Sweet potato, Dahlia, and Guava produce adventitious buds on roots.<br>• <strong>By Stems:</strong> Potato tubers possess 'eyes' (notches with buds, Activity 7.5); ginger and turmeric propagate via rhizomes; money plants grow roots from stem nodes (Activity 7.6).<br>• <strong>By Leaves:</strong> <em>Bryophyllum</em> produces vegetative buds in notches along its scalloped leaf margins (Figure 7.5); when leaves drop onto moist soil, these plantlets take root!"
            },
            {
                "heading": "Commercial & Agronomic Advantages of Vegetative Propagation",
                "content": "1. <strong>Earlier Yield:</strong> Plants raised vegetatively bear flowers and fruits much sooner than those grown from seeds.<br>2. <strong>Rescue of Seedless Varieties:</strong> Essential for propagating crops that have lost the capacity to produce viable seeds (banana, seedless grapes, orange, rose, jasmine).<br>3. <strong>Genetic Uniformity:</strong> All offspring are genetically identical clones of the parent plant, preserving high-yielding and disease-resistant traits.<br>4. <strong>Artificial Methods:</strong> Layering, cutting, and grafting are widely used in agriculture (sugarcane, apples, roses)."
            }
        ],
        "narration": "Did you know you can plant a potato slice or a Bryophyllum leaf and get brand new plants? That's vegetative propagation! In potato, buds in the 'eyes' sprout into green shoots. In Bryophyllum, miniature plantlets grow right in the notches of the leaf margins! For farmers, vegetative propagation is a superpower: crops like bananas and seedless grapes that cannot make seeds are easily multiplied, bearing fruit much faster while preserving exact parent genetics!",
        "interactive_type": "vegetative_prop_sim",
        "checkpoints": [
            {
                "q": "Where are the vegetative reproductive buds located in the plant Bryophyllum (Figure 7.5)?",
                "options": [
                    "Inside deep underground roots",
                    "In the notches along the margins of the leaf",
                    "At the center of its yellow petals",
                    "Inside the wood of the stem trunk"
                ],
                "ans": 1,
                "solution": "Bryophyllum develops adventitious buds in the notches along the leaf margins, which fall to the soil and sprout into new plants (NCERT Page 118, Figure 7.5)."
            },
            {
                "q": "Which of the following is a key agricultural advantage of vegetative propagation over seed reproduction?",
                "options": [
                    "It introduces massive random genetic mutations",
                    "Plants raised vegetatively bear flowers and fruits earlier, and it allows propagation of seedless varieties like banana and jasmine",
                    "It requires pollination by bees and bats",
                    "It produces seeds with double tough coats"
                ],
                "ans": 1,
                "solution": "Vegetative propagation yields earlier flowering and fruiting, preserves genetic identity, and enables propagation of plants that have lost seed viability (NCERT Page 117)."
            }
        ]
    },

    # Slide 8: Tissue Culture & Spore Formation in Rhizopus (Pages 118-119, Fig 7.6)
    {
        "index": 7,
        "title": "Tissue Culture (Micropropagation) & Spore Formation in Rhizopus",
        "short_title": "8. Spores & Culture",
        "badge": "Sections 7.2.5 & 7.2.6 • Pages 118–119",
        "quote": "Tissue culture grows thousands of disease-free plants from cell calluses; Rhizopus produces millions of thick-walled spores inside protected sporangia.",
        "lead": "From sterile biotechnology laboratories cloning ornamental orchids to common mould thriving on moist bread, non-flowering species employ specialized techniques and resilient spores for propagation.",
        "theory_blocks": [
            {
                "heading": "Tissue Culture (Micropropagation) Protocol (Page 118)",
                "content": "1. <strong>Explant Isolation:</strong> Small tissue samples or cells are excised from the growing shoot tip of a parent plant.<br>2. <strong>Callus Induction:</strong> Cells are placed on an artificial nutrient agar medium where they divide rapidly into an undifferentiated mass called a <strong>callus</strong>.<br>3. <strong>Hormone Differentiation:</strong> The callus is transferred to media containing plant hormones (auxins, cytokinins) stimulating root and shoot differentiation into plantlets.<br>4. <strong>Hardening & Planting:</strong> Disease-free plantlets are transplanted to soil. Widely used for ornamental plants and commercial horticulture."
            },
            {
                "heading": "Spore Formation in Bread Mould (Rhizopus) (Figure 7.6 & Activity 7.2)",
                "content": "• On moist bread, thread-like vegetative filaments called <strong>hyphae</strong> form the mycelium.<br>• Erect reproductive stalks develop tiny globular 'blob-on-a-stick' structures called <strong>sporangia</strong>.<br>• Inside each sporangium, hundreds of reproductive cells called <strong>spores</strong> are formed.<br>• <strong>Protective Armor:</strong> Spores are shielded by thick, resistant outer coats that survive drought and heat until they land on a moist nutrient surface and germinate."
            }
        ],
        "narration": "Look at tissue culture: scientists take a tiny cluster of cells from a plant shoot tip, place it in nutrient jelly with plant hormones, and grow thousands of disease-free cloned plantlets! Now look at bread mould, Rhizopus: the white threads are hyphae, but look at those black blobs on sticks! Those are sporangia, packed with thousands of spores. Each spore has a thick armored coat that survives drying out until it lands on warm, moist bread to grow a new fungus!",
        "interactive_type": "tissue_culture_spores_sim",
        "checkpoints": [
            {
                "q": "What is the primary role of the thick protective outer wall surrounding fungal spores in Rhizopus?",
                "options": [
                    "To generate heat to cook the bread",
                    "To protect the spores against adverse environmental conditions (drying, heat) until they land on a moist surface to germinate",
                    "To help the spore swim in pond water",
                    "To attract pollinating insects"
                ],
                "ans": 1,
                "solution": "Spores are covered by thick protective walls that allow them to endure adverse dry conditions until they encounter moisture and nutrients (NCERT Page 118)."
            },
            {
                "q": "In plant tissue culture, what is the undifferentiated cellular mass formed after cells divide on nutrient medium called?",
                "options": [
                    "Zygote",
                    "Callus",
                    "Sporangium",
                    "Hypha"
                ],
                "ans": 1,
                "solution": "Cells removed from the growing tip divide rapidly in artificial nutrient medium to form a small, unorganized cluster of cells called a callus (NCERT Page 118)."
            }
        ]
    },

    # Slide 9: Why Sexual Reproduction? Meiosis & Gamete Specialization (Pages 119-120)
    {
        "index": 8,
        "title": "Why Sexual Reproduction? Meiosis & Gametic Dimorphism",
        "short_title": "9. Sexual Advantage",
        "badge": "Section 7.3 & 7.3.1 • Pages 119–120",
        "quote": "Sexual reproduction combines variations from two different individuals; meiosis halves chromosome numbers to prevent genomic doubling in offspring.",
        "lead": "Asexual reproduction creates clones with limited evolutionary flexibility. Sexual reproduction introduces novel combinations of accumulated variations from two parents, while meiosis maintains stable species chromosome numbers.",
        "theory_blocks": [
            {
                "heading": "Why Sexual Reproduction Drives Evolution",
                "content": "• Combining DNA copies from two distinct individuals creates novel gene combinations in every generation.<br>• Since both parents survived in their environment, their accumulated variations are non-lethal and biologically tested.<br>• This accelerates the generation of diversity, equipping populations with diverse adaptations for survival against changing climates and pathogens."
            },
            {
                "heading": "The Chromosome Doubling Dilemma & Meiosis (Page 120)",
                "content": "• <strong>The Dilemma:</strong> If two parent cells each contributed their full complement of DNA, offspring would end up with twice the chromosome count of their parents (46 → 92 → 184), disrupting cellular homeostasis.<br>• <strong>The Solution (Meiosis):</strong> Organisms possess specialized germ-line cells in gonads that undergo reduction division (<strong>meiosis</strong>), halving both chromosome number and DNA content (haploid, $n$).<br>• Upon fertilisation, the fusion of two haploid gametes ($n + n$) re-establishes the normal diploid ($2n$) chromosome count in the zygote!"
            },
            {
                "heading": "Gamete Specialization (Male vs Female)",
                "content": "• <strong>Male Gamete (Sperm/Pollen):</strong> Typically small, lightweight, and motile (equipped with a flagellum or pollen tube) to seek out the partner.<br>• <strong>Female Gamete (Egg/Ovum):</strong> Significantly larger, non-motile, and packed with abundant food stores and organelles to nourish the developing embryo."
            }
        ],
        "narration": "Why did sexual reproduction evolve? Because combining DNA from two individuals produces brand new combinations of variations, supercharging evolution! But wait: if two parents combine their DNA, wouldn't the baby have twice as many chromosomes? That would be a biological disaster! Nature solved this through meiosis: a special cell division that cuts chromosome numbers exactly in half in sperm and eggs! When they fuse, the original diploid number is perfectly restored!",
        "interactive_type": "meiosis_gamete_sim",
        "checkpoints": [
            {
                "q": "Why is the reduction division (meiosis) essential during the formation of germ-cells in sexually reproducing organisms?",
                "options": [
                    "To double the amount of DNA in the offspring",
                    "To halve chromosome numbers in gametes so that fertilisation re-establishes the normal species chromosome count in the zygote",
                    "To destroy all parental genes",
                    "To turn animal cells into plant cells"
                ],
                "ans": 1,
                "solution": "Meiosis halves chromosome number and DNA content in gametes so that when male and female gametes fuse, the normal diploid chromosome count is restored in the zygote (NCERT Page 120)."
            },
            {
                "q": "How do male and female gametes differ functionally in complex organisms?",
                "options": [
                    "Male gametes are large and store food; female gametes are tiny and motile",
                    "Male gametes are smaller and motile; female gametes are larger and contain nutrient food reserves to nourish the embryo",
                    "Both gametes are identical in size, motility, and organelle content",
                    "Male gametes carry no chromosomes"
                ],
                "ans": 1,
                "solution": "Male gametes specialize in motility to reach the female germ-cell, whereas female gametes are larger and packed with stored nutrients for embryonic development (NCERT Page 120)."
            }
        ]
    },

    # Slide 10: Sexual Reproduction in Flowering Plants (Pages 120-121, Fig 7.7)
    {
        "index": 9,
        "title": "Sexual Reproduction in Flowering Plants: Flower Anatomy",
        "short_title": "10. Flower Anatomy",
        "badge": "Section 7.3.2 • Pages 120–121 (Figure 7.7)",
        "quote": "Stamens and pistil are the reproductive organs of a flower; the stamen produces male pollen, and the pistil houses the female ovule.",
        "lead": "Flowers are the exquisite reproductive organs of angiosperms. Arranged in four concentric whorls, their specialized floral parts facilitate gamete production and pollination.",
        "theory_blocks": [
            {
                "heading": "Anatomy of an Angiosperm Flower (Figure 7.7)",
                "content": "• <strong>Non-Essential (Accessory) Whorls:</strong><br>&nbsp;&nbsp;1. <em>Sepals (Calyx):</em> Green leaf-like outer structures that protect the floral bud.<br>&nbsp;&nbsp;2. <em>Petals (Corolla):</em> Brightly colored, scented structures that attract insect and bird pollinators.<br>• <strong>Essential (Reproductive) Whorls:</strong><br>&nbsp;&nbsp;3. <em>Stamen (Androecium - Male):</em> Consists of a slender <strong>filament</strong> supporting a terminal two-lobed <strong>anther</strong>, which produces yellowish powdery <strong>pollen grains</strong> containing male germ-cells.<br>&nbsp;&nbsp;4. <em>Pistil / Carpel (Gynoecium - Female):</em> Centrally located; composed of three parts:<br>&nbsp;&nbsp;&nbsp;&nbsp;a) <strong>Stigma:</strong> Sticky terminal surface that captures pollen grains.<br>&nbsp;&nbsp;&nbsp;&nbsp;b) <strong>Style:</strong> Slender elongated neck supporting the stigma.<br>&nbsp;&nbsp;&nbsp;&nbsp;c) <strong>Ovary:</strong> Swollen basal chamber containing one or more <strong>ovules</strong>, each housing a female egg cell."
            },
            {
                "heading": "Unisexual vs Bisexual Flowers",
                "content": "• <strong>Unisexual Flowers:</strong> Contain <em>either</em> stamens or carpels, but not both (e.g., <strong>papaya, watermelon</strong>). Cross-pollination is mandatory.<br>• <strong>Bisexual Flowers:</strong> Contain <em>both</em> stamens and carpels in the same flower (e.g., <strong>Hibiscus, mustard</strong>)."
            }
        ],
        "narration": "Let's examine a flower! Sepals protect the young bud, while colorful petals attract bees and butterflies. At the center are the reproductive organs: the male Stamens, with anthers producing yellow powdery pollen; and the female Pistil, with a sticky stigma, an elongated style, and a swollen ovary at the base! Some flowers like Hibiscus are bisexual with both organs, while papaya and watermelon are unisexual!",
        "interactive_type": "flower_anatomy_sim",
        "checkpoints": [
            {
                "q": "Which of the following plants bear unisexual flowers containing either stamens or carpels?",
                "options": [
                    "Hibiscus and Mustard",
                    "Papaya and Watermelon",
                    "Rose and Pea",
                    "Mango and Tomato"
                ],
                "ans": 1,
                "solution": "Papaya and watermelon are classic examples of unisexual flowers, possessing either male stamens or female carpels on a given flower (NCERT Page 120)."
            },
            {
                "q": "What are the three anatomical components that constitute the female pistil (carpel) of a flower?",
                "options": [
                    "Sepal, petal, and stamen",
                    "Anther, filament, and pollen sac",
                    "Stigma (terminal sticky surface), Style (elongated neck), and Ovary (swollen base with ovules)",
                    "Radicle, plumule, and cotyledon"
                ],
                "ans": 2,
                "solution": "The pistil consists of the terminal sticky stigma, the elongated style, and the basal swollen ovary containing ovules (NCERT Page 120-121)."
            }
        ]
    },

    # Slide 11: Pollination, Fertilisation & Post-Fertilisation Fruit/Seed Formation (Pages 121-122, Fig 7.8 & 7.9)
    {
        "index": 10,
        "title": "Pollination, Pollen Germination & Post-Fertilisation Transformation",
        "short_title": "11. Pollination & Seed",
        "badge": "Section 7.3.2 • Pages 121–122 (Figures 7.8 & 7.9)",
        "quote": "After pollen tube fertilisation, the ovule develops into a tough seed and the ovary ripens into a fruit, while petals and sepals fall away.",
        "lead": "From the flight of pollen grains across flowers to the growth of pollen tubes down the style, double fertilisation transforms the floral ovary into a nourishing fruit containing dormant seeds.",
        "theory_blocks": [
            {
                "heading": "Pollination & Pollen Tube Germination (Figure 7.8)",
                "content": "• <strong>Self-Pollination:</strong> Transfer of pollen grains from the anther to the stigma of the <em>same flower</em> or another flower on the same plant.<br>• <strong>Cross-Pollination:</strong> Transfer of pollen grains from an anther of one flower to the stigma of a flower on a <em>different plant of the same species</em>, mediated by wind, water, or animal pollinators (insects, birds).<br>• <strong>Pollen Tube Growth:</strong> Upon landing on a compatible receptive stigma, a pollen grain absorbs moisture and germinates. A <strong>pollen tube</strong> emerges, carrying two male gametes down through the style tissue into the ovary, entering the ovule micropyle."
            },
            {
                "heading": "Fertilisation & The Post-Fertilisation Metamorphosis (Activity 7.7 & Figure 7.9)",
                "content": "1. <strong>Fertilisation:</strong> The male germ-cell fuses with the female egg cell inside the ovule to produce a <strong>diploid zygote</strong>.<br>2. <strong>Embryo Formation:</strong> The zygote divides repeatedly by mitosis to form an <strong>embryo</strong> with a radicle (future root), plumule (future shoot), and cotyledons (food store).<br>3. <strong>Ovule → Seed:</strong> The ovule develops a tough protective coat (testa) and dehydrates into a dormant <strong>seed</strong>.<br>4. <strong>Ovary → Fruit:</strong> The surrounding ovary grows rapidly, accumulates sugars and nutrients, and ripens into a <strong>fruit</strong>.<br>5. Petals, sepals, stamens, style, and stigma shrivel and fall off. Under moisture and oxygen, the seed undergoes <strong>germination</strong> (Activity 7.7)!"
            }
        ],
        "narration": "Watch the miracle of plant fertilisation! Pollen lands on the sticky stigma. It sprouts a long pollen tube that tunnels through the style into the ovary! The male germ cell travels down and fertilises the female egg inside the ovule, forming a zygote. After fertilisation, petals and sepals wither away. The ovule transforms into a tough seed carrying a baby plant, while the ovary swells and ripens into a delicious fruit!",
        "interactive_type": "pollination_seed_sim",
        "checkpoints": [
            {
                "q": "What do the ovule and the ovary respectively transform into after successful fertilisation in a flower?",
                "options": [
                    "Ovule becomes fruit; ovary becomes seed",
                    "Ovule becomes a protective seed; ovary ripens into the fruit",
                    "Both ovule and ovary transform into green leaves",
                    "Ovule becomes pollen; ovary becomes petal"
                ],
                "ans": 1,
                "solution": "Following fertilisation, the ovule develops a tough seed coat to become the seed, while the ovary wall expands and ripens into the fruit (NCERT Page 121)."
            },
            {
                "q": "In a germinating dicot seed like Bengal gram (Activity 7.7, Figure 7.9), what do the radicle and plumule respectively develop into?",
                "options": [
                    "Radicle develops into the future root; plumule develops into the future shoot",
                    "Radicle develops into petals; plumule develops into roots",
                    "Both develop into cotyledons",
                    "Plumule develops into roots; radicle develops into fruit"
                ],
                "ans": 0,
                "solution": "During germination, the radicle elongates downward to form the primary root system, while the plumule grows upward to establish the leafy shoot system (NCERT Figure 7.9, Page 121)."
            }
        ]
    },

    # Slide 12: Human Reproduction: Adolescence, Puberty & Secondary Sexual Characteristics (Pages 121-123)
    {
        "index": 11,
        "title": "Human Reproduction: Adolescence, Puberty & Hormonal Changes",
        "short_title": "12. Puberty Changes",
        "badge": "Section 7.3.3 • Pages 121–123",
        "quote": "As the rate of general body growth begins to slow down, reproductive tissues mature—a transition phase called puberty.",
        "lead": "During teenage years, the human body undergoes profound anatomical, physiological, and emotional transformations marking the onset of sexual maturation.",
        "theory_blocks": [
            {
                "heading": "General Body Growth vs Sexual Maturation",
                "content": "• In childhood, body resources are prioritized toward somatic growth (increasing height, gaining weight, replacing milk teeth with permanent teeth).<br>• As general somatic growth plateaus in early adolescence, the body activates specialized reproductive tissues.<br>• <strong>Puberty:</strong> The developmental period during adolescence when reproductive organs mature, gametogenesis begins, and secondary sexual characteristics appear under the control of sex hormones (testosterone and oestrogen)."
            },
            {
                "heading": "Changes Common to Both Sexes vs Sex-Specific Changes",
                "content": "• <strong>Common Changes:</strong> Growth of darker, thicker hair in armpits and the pubic genital region; finer hair on limbs and face; oily skin with acne/pimples; heightened body awareness.<br>• <strong>Specific to Girls (Driven by Oestrogen):</strong> Enlargement of breasts with darkening of areolar skin around nipples; broadening of hips; initiation of monthly <strong>menstruation</strong> (menarche).<br>• <strong>Specific to Boys (Driven by Testosterone):</strong> Facial hair growth (mustache, beard); voice cracking and deepening due to enlargement of the larynx (Adam's apple); broadening of shoulders; occasional enlargement/erection of penis."
            }
        ],
        "narration": "During childhood, your body focuses on getting taller and stronger. But in your teenage years, general growth slows down as puberty begins! Driven by testosterone in boys and oestrogen in girls, your body matures for reproduction. Both sexes develop hair in armpits and pubic regions, and skin becomes oily. Boys experience voice deepening and facial hair, while girls develop breasts and begin menstruation. These physical changes signal sexual maturation!",
        "interactive_type": "puberty_timeline_sim",
        "checkpoints": [
            {
                "q": "Which primary sex hormones are responsible for triggering the secondary sexual characteristics during puberty in human males and females respectively?",
                "options": [
                    "Insulin and Glucagon",
                    "Testosterone in males and Oestrogen in females",
                    "Thyroxin and Adrenaline",
                    "Growth hormone and Prolactin"
                ],
                "ans": 1,
                "solution": "Testosterone secreted by the testes drives male secondary sexual changes, while oestrogen secreted by the ovaries regulates female puberty changes (NCERT Page 122-123)."
            },
            {
                "q": "Why do reproductive tissues mature during adolescence rather than during early childhood?",
                "options": [
                    "Because children have no blood supply",
                    "Early childhood resources are prioritized for somatic growth; as the rate of general growth slows down, energy is allocated to reproductive tissue maturation",
                    "DNA cannot replicate before age 10",
                    "Children do not consume proteins"
                ],
                "ans": 1,
                "solution": "While the body is rapidly growing to adult size, bodily resources are prioritized for somatic development. Once somatic growth stabilizes, reproductive maturation becomes a priority (NCERT Page 122)."
            }
        ]
    },

    # Slide 13: Male Reproductive System (Pages 123-124, Fig 7.10)
    {
        "index": 12,
        "title": "The Male Reproductive System: Testes, Ducts & Accessory Glands",
        "short_title": "13. Male System",
        "badge": "Section 7.3.3 (a) • Pages 123–124 (Figure 7.10)",
        "quote": "Testes lie outside the abdomen in the scrotum because sperm formation requires a temperature 2-2.5°C lower than normal core body temperature.",
        "lead": "The male reproductive system is engineered for continuous spermatogenesis and delivery of motile male gametes to the female reproductive tract.",
        "theory_blocks": [
            {
                "heading": "The Testes & Scrotum (Figure 7.10)",
                "content": "• <strong>Testes:</strong> Paired oval male gonads located outside the abdominal cavity in a pouch of skin called the <strong>scrotum</strong>.<br>• <strong>Thermoregulation:</strong> Human spermatogenesis cannot occur at core body temperature (37°C); the scrotum maintains a temperature <strong>2 to 2.5°C cooler</strong> than internal body temperature.<br>• <strong>Dual Function of Testes:</strong> (1) Production of male germ-cells (<strong>sperms</strong>), and (2) Secretion of the endocrine hormone <strong>testosterone</strong>."
            },
            {
                "heading": "Ducts, Glands & Semen Composition",
                "content": "• <strong>Vas Deferens:</strong> Muscular tube that ascends from each testis into the abdomen, looping over the urinary bladder.<br>• <strong>Accessory Glands (Prostate & Seminal Vesicles):</strong> Add seminal secretions along the vas deferens, creating a milky fluid (semen) that:<br>&nbsp;&nbsp;1. Provides nutritional fructose to sustain sperm metabolism.<br>&nbsp;&nbsp;2. Neutralizes acidity and provides a fluid medium making sperm transport easier.<br>• <strong>Urethra:</strong> Forms a <em>common passage</em> for both urine and sperm, exiting through the muscular, vascular <strong>penis</strong>.<br>• <strong>Sperm Structure:</strong> Microscopic cells consisting of a condensed genetic head, mitochondrial middle piece, and a long motile flagellar tail."
            }
        ],
        "narration": "Let's examine the Male Reproductive System! The testes are located outside the abdominal cavity inside the scrotum. Why? Because sperm formation requires a temperature 2 to 2.5 degrees cooler than your 37-degree core body temperature! The testes produce millions of sperms and the hormone testosterone. Sperms travel through the vas deferens, where the seminal vesicles and prostate gland add alkaline, nutrient-rich fluids to help them swim through the urethra!",
        "interactive_type": "male_system_sim",
        "checkpoints": [
            {
                "q": "Why are the human testes anatomically positioned outside the abdominal cavity inside the scrotum?",
                "options": [
                    "To protect them from stomach hydrochloric acid",
                    "Sperm formation requires a temperature 2 to 2.5°C lower than normal core body temperature",
                    "To allow them to receive direct sunlight",
                    "Because they are connected directly to the lungs"
                ],
                "ans": 1,
                "solution": "The scrotum acts as a thermoregulatory sac maintaining testes at a temperature lower than normal body temperature (37°C), essential for viable spermatogenesis (NCERT Page 123)."
            },
            {
                "q": "What dual vital roles do the secretions of the prostate gland and seminal vesicles serve?",
                "options": [
                    "They destroy surplus sperms and produce urine",
                    "They provide nutrition to the sperms and provide a fluid medium that makes sperm transport easier",
                    "They secrete testosterone directly into the urethra",
                    "They filter blood like kidneys"
                ],
                "ans": 1,
                "solution": "Secretions from the seminal vesicles and prostate gland create semen, providing essential nutrients and a fluid vehicle for motile sperm transport (NCERT Page 123)."
            }
        ]
    },

    # Slide 14: Female Reproductive System (Pages 123-124, Fig 7.11)
    {
        "index": 13,
        "title": "The Female Reproductive System: Ovaries, Oviducts & Uterus",
        "short_title": "14. Female System",
        "badge": "Section 7.3.3 (b) • Pages 123–124 (Figure 7.11)",
        "quote": "The ovaries produce eggs and hormones; fertilisation occurs in the fallopian tube, and the embryo implants into the thick uterine wall.",
        "lead": "The female reproductive system is designed not only to produce female germ-cells, but to house, nourish, and gestate a developing human embryo for nine months.",
        "theory_blocks": [
            {
                "heading": "Anatomy of the Female Reproductive System (Figure 7.11)",
                "content": "• <strong>Ovaries:</strong> Paired oval organs in the lower abdominal cavity. At birth, each ovary already contains thousands of immature follicles. After puberty, one mature egg (ovum) is released every month alternately by one of the ovaries (<strong>ovulation</strong>). Also produce oestrogen and progesterone.<br>• <strong>Oviducts (Fallopian Tubes):</strong> Delicate ciliated muscular tubes that sweep up the released egg. The oviduct is the <strong>site of fertilisation</strong> where sperm encounters the ovum."
            },
            {
                "heading": "Uterus, Cervix & Vagina",
                "content": "• <strong>Uterus (Womb):</strong> An elastic, inverted pear-shaped muscular bag where the fertilised blastocyst implants and grows into a foetus.<br>• <strong>Cervix:</strong> The narrow lower neck of the uterus that connects to the vagina.<br>• <strong>Vagina:</strong> The muscular passage that receives sperm during intercourse and serves as the birth canal during parturition."
            }
        ],
        "narration": "Now let's explore the Female Reproductive System! At birth, a girl's ovaries already contain thousands of immature eggs. After puberty, one ovary releases a mature egg every month into the fallopian tube. If sperms are present, fertilisation happens right inside this oviduct! The fertilised egg divides into an embryo and travels into the uterus—an elastic, muscular womb with a rich blood lining ready to nurture a growing baby!",
        "interactive_type": "female_system_sim",
        "checkpoints": [
            {
                "q": "Where in the female reproductive tract does fertilisation (fusion of sperm and egg) normally take place?",
                "options": [
                    "Vagina",
                    "Uterus (womb)",
                    "Oviduct (Fallopian tube)",
                    "Ovary"
                ],
                "ans": 2,
                "solution": "Sperms travel upward through the cervix and uterus into the oviduct (fallopian tube), where fertilisation with the released egg occurs (NCERT Page 124)."
            },
            {
                "q": "How many mature eggs are typically released each month by the ovaries of a healthy human female after puberty?",
                "options": [
                    "Approximately 500 eggs",
                    "One egg is produced every month by one of the ovaries",
                    "Tens of thousands of eggs simultaneously",
                    "Two dozen eggs every week"
                ],
                "ans": 1,
                "solution": "On reaching puberty, one egg is matured and released roughly every 28 days (monthly) alternately by one of the ovaries (NCERT Page 124)."
            }
        ]
    },

    # Slide 15: Fertilisation, Implantation & The Placenta (Pages 124-125)
    {
        "index": 14,
        "title": "Embryo Implantation, The Placenta & Gestation",
        "short_title": "15. Placenta & Gestation",
        "badge": "Section 7.3.3 (b) • Pages 124–125",
        "quote": "The placenta is a disc embedded in the uterine wall with embryonic villi, providing a large surface area for glucose, oxygen, and waste exchange.",
        "lead": "Following fertilisation in the fallopian tube, the dividing zygote migrates to the uterus and implants into the blood-rich endometrium, sustained by the miraculous lifeline of the placenta.",
        "theory_blocks": [
            {
                "heading": "Zygote Division & Uterine Implantation",
                "content": "1. <strong>Cleavage:</strong> The single-cell fertilised zygote divides mitotically into a ball of cells called an <strong>embryo</strong>.<br>2. <strong>Implantation:</strong> The embryo enters the uterine cavity and embeds itself deeply into the thick, spongy, vascular uterine lining (endometrium).<br>3. <strong>Embryogenesis:</strong> The embedded embryo gradually differentiates specialized tissues and organs, transitioning into a <strong>foetus</strong>."
            },
            {
                "heading": "Structure and Function of the Placenta (Page 124)",
                "content": "• <strong>Structure:</strong> A specialized vascular disc-like organ embedded in the uterine wall, connected to the foetus via the umbilical cord.<br>• <strong>Embryo's Side:</strong> Features finger-like <strong>villi</strong> that dramatically expand surface area.<br>• <strong>Mother's Side:</strong> Large maternal blood spaces surround the villi.<br>• <strong>Physiological Functions:</strong><br>&nbsp;&nbsp;a) Delivers glucose, amino acids, and oxygen from mother's blood to embryo.<br>&nbsp;&nbsp;b) Eliminates carbon dioxide and metabolic nitrogenous wastes from embryonic blood into maternal circulation.<br>• <strong>Gestation & Birth:</strong> Human gestation lasts approximately <strong>nine months</strong> (40 weeks); birth occurs via rhythmic oxytocin-driven contractions of uterine smooth muscle."
            }
        ],
        "narration": "How does an embryo breathe and eat inside the womb? Through the placenta! The placenta is a specialized disc embedded in the mother's uterine wall. On the baby's side are microscopic finger-like villi, bathed in maternal blood pools! This massive surface area allows oxygen and glucose to diffuse easily into the baby's blood, while metabolic wastes like carbon dioxide diffuse back into the mother's circulation for removal! After nine months of growth, rhythmic uterine contractions bring the baby into the world!",
        "interactive_type": "placenta_exchange_sim",
        "checkpoints": [
            {
                "q": "How does the developing embryo receive oxygen and nutrition from the mother's body?",
                "options": [
                    "By drinking amniotic fluid directly through its mouth",
                    "Through a specialized vascular tissue called the placenta, where embryonic villi are surrounded by maternal blood spaces",
                    "Through direct nerve connections to the mother's brain",
                    "By absorbing nutrients from the abdominal skin"
                ],
                "ans": 1,
                "solution": "The placenta provides a huge vascular surface area through embryonic villi bathed in maternal blood spaces for the diffusion of oxygen and glucose (NCERT Page 124)."
            },
            {
                "q": "What is the approximate gestation period (duration of development from fertilisation to birth) in humans?",
                "options": [
                    "3 months",
                    "6 months",
                    "Approximately 9 months (38 to 40 weeks)",
                    "18 months"
                ],
                "ans": 2,
                "solution": "Human embryonic and foetal development within the mother's uterus takes approximately nine months (NCERT Page 124)."
            }
        ]
    },

    # Slide 16: What Happens When the Egg is Not Fertilised? Menstruation (Pages 124-125)
    {
        "index": 15,
        "title": "When the Egg is Not Fertilised: The Menstrual Cycle",
        "short_title": "16. Menstruation",
        "badge": "Section 7.3.3 (c) • Pages 124–125",
        "quote": "If the egg is not fertilised, the spongy uterine lining breaks down and sheds through the vagina as blood and mucus—a cycle called menstruation.",
        "lead": "Every single month, the female body prepares for pregnancy by building a rich, cushioned uterine lining. When fertilisation does not occur, this biological preparation is reset through the menstrual cycle.",
        "theory_blocks": [
            {
                "heading": "The Egg's Lifespan & Endometrial Preparation",
                "content": "• Following ovulation, the released egg travels down the fallopian tube; it remains viable for fertilisation for only <strong>about 24 hours (one day)</strong>.<br>• In anticipation of pregnancy, the uterus thickens its inner lining (endometrium), making it highly spongy, glandular, and densely vascularized with capillaries to nourish a potential embryo."
            },
            {
                "heading": "The Mechanism of Menstruation (Page 124)",
                "content": "1. If sperms do not fertilise the egg, progesterone levels drop precipitously.<br>2. Because pregnancy has not occurred, the thick, blood-rich endometrial lining is no longer required.<br>3. The lining tissue slowly breaks down and disintegrates.<br>4. Fragmented tissues, mucus, and blood are discharged through the cervix and exit the body via the <strong>vagina</strong>.<br>5. <strong>Duration:</strong> This menstrual flow typically lasts between <strong>2 to 8 days</strong>.<br>6. <strong>Periodicity:</strong> The cycle recurs roughly every 28 days (monthly) throughout a woman's reproductive life."
            }
        ],
        "narration": "Every month, the uterus prepares a soft, blood-rich lining like a cozy bed for a potential baby. But the unfertilised egg lives for only about one day! If no sperm fertilises the egg, the body realizes the lining is not needed. The blood vessels and tissues gently break down and shed through the vagina as blood and mucus—this is menstruation! It lasts two to eight days and resets the cycle for the next month!",
        "interactive_type": "menstrual_cycle_sim",
        "checkpoints": [
            {
                "q": "Why does menstruation occur in human females roughly every month?",
                "options": [
                    "To remove excess water from the kidneys",
                    "When an ovulated egg is not fertilised, the thick and spongy uterine lining is no longer needed, so it breaks down and sheds as blood and mucus",
                    "Because ovaries produce too much testosterone",
                    "To replace damaged skeletal bones"
                ],
                "ans": 1,
                "solution": "When fertilisation fails, the unneeded thick uterine lining breaks down and is discharged through the vagina, initiating menstruation (NCERT Page 124)."
            },
            {
                "q": "Approximately how long does an unfertilised human ovum (egg) survive after being released from the ovary?",
                "options": [
                    "About 1 hour",
                    "About one day (24 hours)",
                    "About 14 days",
                    "For several months"
                ],
                "ans": 1,
                "solution": "An unfertilised ovum remains viable for approximately 24 hours after ovulation before degenerating (NCERT Page 124)."
            }
        ]
    },

    # Slide 17: Reproductive Health, STDs & Contraceptive Methods (Pages 125-126)
    {
        "index": 16,
        "title": "Reproductive Health: STDs, Contraceptive Strategies & Sex Ratio",
        "short_title": "17. Reproductive Health",
        "badge": "Section 7.3.3 (d) • Pages 125–126",
        "quote": "Contraception prevents unwanted pregnancy through barrier, hormonal, chemical, or surgical methods; barrier methods also protect against STDs.",
        "lead": "Reproductive health encompasses physical, mental, and social well-being in all matters relating to the reproductive system. Modern contraception empowers family planning and shields against sexually transmitted infections.",
        "theory_blocks": [
            {
                "heading": "Sexually Transmitted Diseases (STDs)",
                "content": "• Sexual intercourse involves intimate bodily contact, facilitating pathogen transmission:<br>&nbsp;&nbsp;1. <strong>Bacterial STDs:</strong> <em>Gonorrhoea</em> and <em>Syphilis</em> (curable with antibiotics).<br>&nbsp;&nbsp;2. <strong>Viral STDs:</strong> <em>Genital Warts</em> and <em>HIV-AIDS</em> (incurable viral infections).<br>• <strong>Barrier Protection:</strong> Condoms on the penis provide a mechanical barrier that prevents transmission of many STDs."
            },
            {
                "heading": "Categories of Contraceptive Methods (Page 125)",
                "content": "1. <strong>Barrier Methods:</strong> Condoms on the penis or diaphragms/caps in the vagina mechanically prevent sperm from reaching the egg. <em>Bonus:</em> Only barrier methods shield against STDs!<br>2. <strong>Hormonal Methods (Oral Pills):</strong> Pills contain synthetic hormones that suppress ovulation; can have hormonal side-effects.<br>3. <strong>Intrauterine Contraceptive Devices (IUCDs):</strong> Copper-T or Loop inserted into the uterus by doctors; prevents implantation (does NOT protect against STDs!).<br>4. <strong>Surgical Methods (Permanent):</strong><br>&nbsp;&nbsp;a) <em>Vasectomy:</em> In males, the vas deferens is cut and ligated, blocking sperm release.<br>&nbsp;&nbsp;b) <em>Tubectomy:</em> In females, fallopian tubes are blocked, preventing egg passage."
            },
            {
                "heading": "Female Foeticide & The Child Sex Ratio",
                "content": "• Misuse of surgical and prenatal diagnostic techniques (ultrasound) for sex-selective abortion of female foetuses has caused an alarming decline in the child sex ratio.<br>• Prenatal sex determination is strictly prohibited and punished by law to protect a balanced, healthy society."
            }
        ],
        "narration": "Reproductive health is all about staying safe and informed! Sexual contact can transmit bacterial infections like gonorrhoea and syphilis, or viral infections like HIV-AIDS. Contraceptive methods prevent unwanted pregnancy: barrier methods like condoms block sperm and protect against STDs! Hormonal pills stop ovulation, while Copper-T in the uterus blocks implantation. Permanent surgical methods include vasectomy in men and tubectomy in women. Remember, prenatal sex determination is illegal to stop female foeticide and maintain a healthy sex ratio!",
        "interactive_type": "contraception_matrix_sim",
        "checkpoints": [
            {
                "q": "If a woman is using an intrauterine device like a Copper-T, will it help protect her from sexually transmitted diseases (STDs)?",
                "options": [
                    "Yes, it protects against all viral and bacterial STDs",
                    "No, Copper-T prevents implantation in the uterus to avoid pregnancy, but does not prevent fluid contact or protect against STDs",
                    "Yes, but only against HIV",
                    "Copper-T is an oral antibiotic"
                ],
                "ans": 1,
                "solution": "Copper-T acts inside the uterus to prevent pregnancy; it provides no mechanical barrier against fluid pathogen exchange and cannot protect against STDs (NCERT Page 125-126, Question 5)."
            },
            {
                "q": "Which contraceptive method involves surgically cutting and tying the vas deferens in males to prevent sperm transfer?",
                "options": [
                    "Tubectomy",
                    "Vasectomy",
                    "Copper-T insertion",
                    "Oral pill administration"
                ],
                "ans": 1,
                "solution": "Vasectomy is the surgical blocking/ligation of the vas deferens in males, preventing sperm from entering semen (NCERT Page 125)."
            }
        ]
    }
]

# 4 Dedicated Quiz Challenge Slides (10 questions each = 40 questions total)
QUIZ_SLIDES = [
    # Quiz 1: DNA Copying, Variations & Asexual Reproduction (Questions 1 to 10)
    {
        "index": 17,
        "title": "Mastery Challenge Quiz — Part 1: DNA Copying, Variations & Asexual Modes",
        "short_title": "18. Quiz Part 1",
        "badge": "Quiz Challenge • Part 1 of 4",
        "description": "Test your mastery on DNA replication accuracy, importance of variation in ecological niches, binary fission in Amoeba & Leishmania, multiple fission in Plasmodium, and fragmentation in Spirogyra. Click Solution for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 1,
                "q": "Asexual reproduction takes place through budding in:",
                "options": [
                    "Amoeba",
                    "Yeast",
                    "Plasmodium",
                    "Leishmania"
                ],
                "ans": 1,
                "solution": "Asexual reproduction takes place through budding in Yeast (and Hydra). Amoeba and Leishmania reproduce by binary fission, while Plasmodium reproduces by multiple fission (NCERT Page 127, Exercise Q1)."
            },
            {
                "id": 2,
                "q": "Why is DNA copying an essential event in the process of reproduction?",
                "options": [
                    "DNA copying converts animal cells into plant cells",
                    "DNA contains the genetic information for inheritance and protein synthesis; duplicating it ensures each daughter cell receives an intact set of body design blueprints",
                    "DNA copying prevents cells from growing",
                    "DNA dissolves the cell membrane"
                ],
                "ans": 1,
                "solution": "DNA molecules carry the master blueprints for synthesizing cellular proteins. Creating a copy ensures that both daughter cells receive identical genetic instructions to maintain life processes (NCERT Page 113, Intext Q5)."
            },
            {
                "id": 3,
                "q": "How does binary fission in Leishmania differ from that observed in Amoeba?",
                "options": [
                    "Leishmania divides inside a hard cyst wall into hundreds of cells",
                    "In Amoeba, division occurs in any plane; in Leishmania, binary fission occurs in a definite longitudinal orientation in relation to its whip-like flagellum",
                    "Leishmania reproduces by fragmentation",
                    "Amoeba reproduces sexually"
                ],
                "ans": 1,
                "solution": "Amoeba has an irregular shape and splits in any plane, whereas Leishmania has a whip-like flagellum at one end, causing fission to occur in a definite longitudinal orientation (NCERT Page 115)."
            },
            {
                "id": 4,
                "q": "The protozoan parasite responsible for causing the disease kala-azar is:",
                "options": [
                    "Plasmodium",
                    "Leishmania",
                    "Spirogyra",
                    "Planaria"
                ],
                "ans": 1,
                "solution": "Leishmania is the flagellated unicellular protozoan that causes kala-azar (visceral leishmaniasis) (NCERT Page 115)."
            },
            {
                "id": 5,
                "q": "Which organism divides into many daughter cells simultaneously by the process of multiple fission?",
                "options": [
                    "Malarial parasite (Plasmodium)",
                    "Yeast",
                    "Hydra",
                    "Rhizopus"
                ],
                "ans": 0,
                "solution": "The malarial parasite Plasmodium undergoes multiple fission inside a protective cyst to produce many daughter cells simultaneously (NCERT Page 116, Figure 7.2)."
            },
            {
                "id": 6,
                "q": "Why can simple organisms like Spirogyra reproduce by fragmentation, while complex multicellular organisms cannot?",
                "options": [
                    "Complex organisms lack cell membranes",
                    "Spirogyra possesses simple, similar cells throughout; complex organisms have specialized cells organized into tissues and organs placed at definite anatomical positions",
                    "Spirogyra produces flowers",
                    "Complex organisms have no reproductive cells"
                ],
                "ans": 1,
                "solution": "Complex multicellular organisms have high structural differentiation with specialized tissues and organs in fixed positions; random fragmentation would destroy organ systems (NCERT Page 116)."
            },
            {
                "id": 7,
                "q": "How does genetic variation during DNA copying benefit a species facing climate change (e.g., global warming in a temperate pond)?",
                "options": [
                    "It ensures all bacteria die at the exact same temperature",
                    "A few pre-existing heat-resistant variants survive the rising temperature and reproduce, preventing the extinction of the species",
                    "It turns bacteria into multicellular fish",
                    "It stops bacterial respiration"
                ],
                "ans": 1,
                "solution": "If temperature rises, standard bacteria perish, but heat-tolerant variants survive and multiply, ensuring the continuation of the species (NCERT Page 114)."
            },
            {
                "id": 8,
                "q": "What happens if an error in DNA copying creates a genetic sequence that is completely incompatible with the cellular apparatus it inherits?",
                "options": [
                    "The cell transforms into a virus",
                    "The newborn cell cannot maintain metabolic processes and simply dies",
                    "The cell divides a thousand times faster",
                    "The cell becomes a stem cell"
                ],
                "ans": 1,
                "solution": "When DNA variations are too drastic, the new DNA copy cannot work with the cellular apparatus, and the newborn cell dies (NCERT Page 114)."
            },
            {
                "id": 9,
                "q": "What is the primary substance synthesized inside cells using the genetic information stored in nuclear DNA?",
                "options": [
                    "Lipids",
                    "Proteins",
                    "Cellulose",
                    "Starch"
                ],
                "ans": 1,
                "solution": "The DNA in the cell nucleus is the direct information source for synthesizing specific cellular proteins (NCERT Page 113)."
            },
            {
                "id": 10,
                "q": "In Activity 7.1, what structure develops on the yeast cell during asexual reproduction in warm sugar solution?",
                "options": [
                    "A spore with a thick wall",
                    "A small bulb-like outgrowth called a bud",
                    "A long root hair",
                    "A pollen grain"
                ],
                "ans": 1,
                "solution": "In yeast, small bulb-like projections called buds emerge from the parent cell and can detach or form chains (NCERT Page 115-116)."
            }
        ]
    },

    # Quiz 2: Regeneration, Budding, Vegetative Propagation & Spores (Questions 11 to 20)
    {
        "index": 18,
        "title": "Mastery Challenge Quiz — Part 2: Regeneration, Vegetative Propagation & Spores",
        "short_title": "19. Quiz Part 2",
        "badge": "Quiz Challenge • Part 2 of 4",
        "description": "Test your mastery on Planaria regeneration, Hydra budding, Bryophyllum leaf notches, potato eyes, tissue culture callus, and Rhizopus sporangia. Click Solution for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 11,
                "q": "Which of the following organisms can regenerate into complete individuals if cut or broken into several pieces?",
                "options": [
                    "Hydra and Planaria",
                    "Amoeba and Paramecium",
                    "Mosquito and Housefly",
                    "Spirogyra and Yeast"
                ],
                "ans": 0,
                "solution": "Hydra and the flatworm Planaria possess specialized regenerative cells capable of proliferating and differentiating to reconstruct complete organisms from cut body fragments (NCERT Page 116-117, Figure 7.3)."
            },
            {
                "id": 12,
                "q": "Why is regeneration not considered the same as reproduction?",
                "options": [
                    "Regenerated organisms have no DNA",
                    "Most organisms would not normally depend on being cut up or mutilated to be able to reproduce",
                    "Regeneration is only seen in dead animals",
                    "Regeneration requires two parents"
                ],
                "ans": 1,
                "solution": "Reproduction is a natural life cycle process; organisms do not rely on accidental injury or mechanical slicing to propagate their species (NCERT Page 117)."
            },
            {
                "id": 13,
                "q": "In which plant do vegetative buds produced in the notches along the leaf margins fall on soil and develop into new plants?",
                "options": [
                    "Money plant",
                    "Bryophyllum",
                    "Potato",
                    "Sugarcane"
                ],
                "ans": 1,
                "solution": "Bryophyllum produces adventitious vegetative buds in the scalloped notches along its leaf margins, which develop into new plantlets when detached (NCERT Page 118, Figure 7.5)."
            },
            {
                "id": 14,
                "q": "What structures on the surface of a potato tuber give rise to fresh green shoots and roots (Activity 7.5)?",
                "options": [
                    "Flower petals",
                    "Notches or 'eyes' containing dormant vegetative buds",
                    "Lenticels",
                    "Root caps"
                ],
                "ans": 1,
                "solution": "The 'eyes' of a potato tuber are modified stem nodes containing buds that sprout into shoots and adventitious roots when placed on moist cotton (Activity 7.5, Page 118)."
            },
            {
                "id": 15,
                "q": "Which of the following plants have lost the capacity to produce viable seeds and are widely propagated through vegetative methods?",
                "options": [
                    "Wheat and Rice",
                    "Banana, Orange, Rose, and Jasmine",
                    "Mustard and Gram",
                    "Maize and Pea"
                ],
                "ans": 1,
                "solution": "Crops like banana, seedless orange, cultivated rose, and jasmine have lost seed viability and rely entirely on vegetative propagation (NCERT Page 117)."
            },
            {
                "id": 16,
                "q": "In plant tissue culture, what is the undifferentiated cellular mass formed after cells divide on an artificial nutrient medium called?",
                "options": [
                    "Sporangium",
                    "Callus",
                    "Hypha",
                    "Zygote"
                ],
                "ans": 1,
                "solution": "Excised shoot tip cells divide rapidly on nutrient agar to form an unorganized group of cells called a callus before hormone-induced differentiation (NCERT Page 118)."
            },
            {
                "id": 17,
                "q": "On bread mould (Rhizopus), what are the thread-like non-reproductive structures and the tiny reproductive 'blob-on-a-stick' structures respectively called?",
                "options": [
                    "Spores and Petals",
                    "Hyphae (vegetative threads) and Sporangia (blob-on-a-stick structures containing spores)",
                    "Roots and Stems",
                    "Pollen and Stigma"
                ],
                "ans": 1,
                "solution": "The vegetative filamentous threads are hyphae, while the bulbous reproductive structures holding spores are sporangia (NCERT Page 118, Figure 7.6)."
            },
            {
                "id": 18,
                "q": "How does an organism benefit by reproducing through spores?",
                "options": [
                    "Spores can swim actively like fish",
                    "Spores are covered by thick protective walls that endure adverse heat and drying, and are produced in large numbers for wide dispersal",
                    "Spores eliminate the need for cell division",
                    "Spores immediately turn into flowers"
                ],
                "ans": 1,
                "solution": "Spores are microscopic, light for wind dispersal, produced in huge numbers, and shielded by thick walls that survive drought until favorable moist conditions arrive (NCERT Page 118, Intext Q2)."
            },
            {
                "id": 19,
                "q": "What agricultural method is used to grow plants like sugarcane, roses, and grapes by attaching shoots to rooted stems?",
                "options": [
                    "Multiple fission",
                    "Layering or Grafting",
                    "Spore culture",
                    "Budding in water"
                ],
                "ans": 1,
                "solution": "Layering and grafting are artificial vegetative propagation techniques widely practiced in horticulture for sugarcane, roses, and grapes (NCERT Page 117)."
            },
            {
                "id": 20,
                "q": "Why are all plants produced through vegetative propagation genetically identical to the parent plant?",
                "options": [
                    "Because they undergo meiosis ten times",
                    "Because they arise from mitotic division of somatic cells of a single parent without gametic fusion",
                    "Because they absorb artificial fertilizer",
                    "Because bees pollinate them"
                ],
                "ans": 1,
                "solution": "Vegetative propagation involves only mitotic cell division from somatic parts of a single individual; hence offspring are genetic clones of the parent (NCERT Page 117)."
            }
        ]
    },

    # Quiz 3: Sexual Reproduction in Flowering Plants (Questions 21 to 30)
    {
        "index": 19,
        "title": "Mastery Challenge Quiz — Part 3: Sexual Reproduction in Plants & Flowers",
        "short_title": "20. Quiz Part 3",
        "badge": "Quiz Challenge • Part 3 of 4",
        "description": "Test your mastery on flower parts, anther pollen, pistil ovary, self vs cross-pollination, pollen tube growth, seed germination, and embryo cotyledons. Click Solution for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 21,
                "q": "The anther contains:",
                "options": [
                    "Sepals",
                    "Ovules",
                    "Pistil",
                    "Pollen grains"
                ],
                "ans": 3,
                "solution": "The anther is the terminal bilobed portion of the stamen that produces and stores yellow pollen grains containing male germ-cells (NCERT Page 127, Exercise Q3)."
            },
            {
                "id": 22,
                "q": "Which of the following flowers is bisexual, containing both stamens and pistil?",
                "options": [
                    "Papaya",
                    "Watermelon",
                    "Hibiscus (or Mustard)",
                    "Date palm"
                ],
                "ans": 2,
                "solution": "Hibiscus and mustard are bisexual flowers possessing both male stamens and female carpels; papaya and watermelon are unisexual (NCERT Page 120)."
            },
            {
                "id": 23,
                "q": "What is the primary difference between pollination and fertilisation in plants?",
                "options": [
                    "Pollination is the transfer of pollen from anther to stigma; fertilisation is the biochemical fusion of the male germ-cell with the female egg cell inside the ovule",
                    "Pollination occurs only in animals; fertilisation occurs in plants",
                    "Pollination produces seeds; fertilisation produces flowers",
                    "There is no difference between them"
                ],
                "ans": 0,
                "solution": "Pollination is the physical transfer of pollen grains to the stigma (via wind, water, or insects), whereas fertilisation is the cellular fusion of male and female gametes to form a zygote (NCERT Page 121, Intext Q1)."
            },
            {
                "id": 24,
                "q": "After pollen lands on a compatible stigma, how does the male germ-cell reach the female egg cell located deep in the ovary?",
                "options": [
                    "It is absorbed by the petals",
                    "A pollen tube grows out of the pollen grain and travels through the style into the ovary",
                    "It floats through rain water inside the stem",
                    "The ovary opens up and swallows the pollen"
                ],
                "ans": 1,
                "solution": "The germinated pollen grain sprouts a pollen tube that digests its way down the style to deliver the male gametes to the ovule inside the ovary (NCERT Page 121, Figure 7.8)."
            },
            {
                "id": 25,
                "q": "After successful fertilisation in a flower, the ovule and the ovary develop into which respective structures?",
                "options": [
                    "Ovule becomes fruit; ovary becomes seed",
                    "Ovule develops a tough coat to become a seed; ovary grows rapidly and ripens to form a fruit",
                    "Both develop into petals",
                    "Ovule becomes pollen; ovary becomes root"
                ],
                "ans": 1,
                "solution": "Following fertilisation, the ovule transforms into a seed, while the surrounding ovary swells and ripens into a fruit (NCERT Page 121)."
            },
            {
                "id": 26,
                "q": "In a soaked Bengal gram (chana) seed (Activity 7.7, Figure 7.9), which part serves as the primary food store for the dormant embryo?",
                "options": [
                    "Radicle",
                    "Plumule",
                    "Cotyledons",
                    "Seed coat only"
                ],
                "ans": 2,
                "solution": "The fleshy cotyledons store concentrated carbohydrates and proteins to sustain the embryo until its first green leaves begin photosynthesis (NCERT Page 121, Figure 7.9)."
            },
            {
                "id": 27,
                "q": "Why does cross-pollination offer an evolutionary advantage over self-pollination in flowering plants?",
                "options": [
                    "It produces fewer seeds",
                    "It combines genetic variations from two different individual parent plants, enhancing adaptability and vigour in offspring",
                    "It requires no water or wind",
                    "It prevents fruits from ripening"
                ],
                "ans": 1,
                "solution": "Cross-pollination introduces novel combinations of genetic variations from two separate parent plants, increasing adaptability (NCERT Page 119-121)."
            },
            {
                "id": 28,
                "q": "What happens to the sepals, petals, stamens, style, and stigma after fertilisation is completed?",
                "options": [
                    "They turn into seeds",
                    "They shrivel and fall off as the ovary ripens into a fruit",
                    "They grow ten times larger to shade the fruit",
                    "They transform into roots"
                ],
                "ans": 1,
                "solution": "Once fertilisation is complete, accessory floral organs (petals, sepals, stamens, style, stigma) wither and fall away (NCERT Page 121)."
            },
            {
                "id": 29,
                "q": "What part of the female pistil contains the ovules and egg cells?",
                "options": [
                    "Terminal stigma",
                    "Elongated style",
                    "Swollen basal ovary",
                    "Anther filament"
                ],
                "ans": 2,
                "solution": "The ovary is the swollen bottom part of the carpel that houses ovules, each containing a female egg cell (NCERT Page 121)."
            },
            {
                "id": 30,
                "q": "In seed germination, the future root and future shoot develop respectively from the:",
                "options": [
                    "Cotyledon and Testa",
                    "Radicle and Plumule",
                    "Plumule and Radicle",
                    "Style and Stigma"
                ],
                "ans": 1,
                "solution": "The radicle gives rise to the primary root, while the plumule gives rise to the future leafy shoot (NCERT Page 121, Figure 7.9)."
            }
        ]
    },

    # Quiz 4: Human Reproduction, Reproductive Health & Contraception (Questions 31 to 40)
    {
        "index": 20,
        "title": "Mastery Challenge Quiz — Part 4: Human Reproduction & Reproductive Health",
        "short_title": "21. Quiz Part 4",
        "badge": "Quiz Challenge • Part 4 of 4",
        "description": "Test your mastery on male & female systems, vas deferens, oviduct, fertilisation, placenta, menstruation, contraception, and STDs. Click Solution for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 31,
                "q": "Which of the following is NOT a part of the female reproductive system in human beings?",
                "options": [
                    "Ovary",
                    "Uterus",
                    "Vas deferens",
                    "Fallopian tube"
                ],
                "ans": 2,
                "solution": "The vas deferens is a duct of the male reproductive system that transports sperm; ovary, uterus, and fallopian tube are female reproductive organs (NCERT Page 127, Exercise Q2)."
            },
            {
                "id": 32,
                "q": "What are the two primary physiological functions performed by the testes in human males?",
                "options": [
                    "Filtration of urine and storage of bile",
                    "Production of male germ-cells (sperms) and secretion of the hormone testosterone",
                    "Digestion of proteins and secretion of insulin",
                    "Circulation of lymph and production of platelets"
                ],
                "ans": 1,
                "solution": "The testes produce male gametes (sperms) via spermatogenesis and secrete the steroid hormone testosterone (NCERT Page 123, Exercise Q5)."
            },
            {
                "id": 33,
                "q": "Where in the human female reproductive tract does fertilisation of the egg by a sperm normally occur?",
                "options": [
                    "Vagina",
                    "Cervix",
                    "Oviduct (Fallopian tube)",
                    "Uterine fundus"
                ],
                "ans": 2,
                "solution": "Fertilisation occurs in the upper portion of the oviduct (fallopian tube) when ascending sperms encounter the ovulated egg (NCERT Page 124)."
            },
            {
                "id": 34,
                "q": "What is the specialized vascular disc tissue through which the embryo receives nutrition and oxygen from the mother's blood?",
                "options": [
                    "Amniotic sac",
                    "Placenta",
                    "Cervix",
                    "Fallopian villus"
                ],
                "ans": 1,
                "solution": "The placenta is a disc embedded in the uterine wall with embryonic villi surrounded by maternal blood spaces for nutrient and respiratory exchange (NCERT Page 124, Intext Q4)."
            },
            {
                "id": 35,
                "q": "Why does menstruation occur in human females roughly every 28 days?",
                "options": [
                    "Because ovaries produce too much testosterone",
                    "If the ovulated egg is not fertilised, the thick, spongy, and vascular uterine lining is no longer required, so it breaks down and sheds through the vagina as blood and mucus",
                    "To prevent kidney stones",
                    "Because stomach acid leaks into the pelvis"
                ],
                "ans": 1,
                "solution": "When fertilisation fails, the unneeded thick endometrial lining breaks down and is discharged through the vagina, initiating the menstrual flow (NCERT Page 124, Exercise Q6)."
            },
            {
                "id": 36,
                "q": "Which of the following is a sexually transmitted bacterial infection?",
                "options": [
                    "HIV-AIDS",
                    "Gonorrhoea (and Syphilis)",
                    "Genital Warts",
                    "Hepatitis B"
                ],
                "ans": 1,
                "solution": "Gonorrhoea and syphilis are bacterial STDs, while warts and HIV-AIDS are viral STDs (NCERT Page 125)."
            },
            {
                "id": 37,
                "q": "Which contraceptive method prevents pregnancy while also providing significant protection against sexually transmitted diseases (STDs)?",
                "options": [
                    "Oral contraceptive hormonal pills",
                    "Copper-T (IUCD)",
                    "Condoms (Mechanical barrier)",
                    "Tubectomy surgery"
                ],
                "ans": 2,
                "solution": "Condoms act as a mechanical barrier preventing direct genital fluid contact, shielding against both pregnancy and STDs (NCERT Page 125)."
            },
            {
                "id": 38,
                "q": "If a woman is using an intrauterine device like a Copper-T, will it protect her from sexually transmitted diseases?",
                "options": [
                    "Yes, it kills all viruses and bacteria",
                    "No, Copper-T prevents implantation in the uterus but does not prevent fluid contact or transmission of STDs",
                    "Yes, but only against syphilis",
                    "Copper-T is a vaccine"
                ],
                "ans": 1,
                "solution": "Copper-T acts locally in the uterus to block implantation; it does not prevent mucosal fluid exchange and provides no protection against STDs (NCERT Page 126, Intext Q5)."
            },
            {
                "id": 39,
                "q": "What surgical contraceptive procedure blocks sperm transfer in males by cutting and tying the vas deferens?",
                "options": [
                    "Tubectomy",
                    "Vasectomy",
                    "Laparoscopy",
                    "Hysterectomy"
                ],
                "ans": 1,
                "solution": "Vasectomy is the surgical cutting and ligation of the vas deferens in males, preventing sperms from reaching the urethra (NCERT Page 125)."
            },
            {
                "id": 40,
                "q": "Why has prenatal sex determination using ultrasound techniques been strictly prohibited by law in India?",
                "options": [
                    "Ultrasound harms maternal skin",
                    "To prevent reckless illegal sex-selective abortion of female foetuses (female foeticide) and halt the alarming decline in the child sex ratio",
                    "Because hospitals lack electricity",
                    "To encourage larger family sizes"
                ],
                "ans": 1,
                "solution": "Prenatal sex determination is prohibited by law to prevent illegal female foeticide and maintain a balanced female-male sex ratio in society (NCERT Page 125)."
            }
        ]
    }
]

print(f"Content Slides: {len(CONTENT_SLIDES)}")
print(f"Quiz Slides: {len(QUIZ_SLIDES)}")
print(f"Total Slides: {len(CONTENT_SLIDES) + len(QUIZ_SLIDES)}")


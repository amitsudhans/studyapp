"""
Data definitions for NCERT Class 9 Science Chapter 2: Tissues
Includes 16 teaching slides with 32 in-slide checkpoints and 4 quiz challenge slides with 40 questions and step-by-step solutions.
"""

SLIDES_DATA = [
    # Slide 1: Introduction to Tissues & Levels of Organisation
    {
        "id": 1,
        "title": "Introduction to Tissues & Levels of Organisation",
        "subtitle": "Division of Labour: From Specialized Cells to Complex Multicellular Organisms",
        "narration": "Welcome students to our exploration of Tissues! In unicellular organisms like Amoeba, a single cell performs every vital function—ingestion, respiration, excretion, and reproduction. But in multicellular organisms like humans and towering banyan trees, millions of cells specialize into coordinated teams through the principle of division of labour. A tissue is defined as a cluster of cells similar in structure, origin, and physiological role, working collaboratively to achieve a specific function. These tissues assemble into organs, organs form organ systems, and organ systems create a harmonious living organism. Let us examine this architectural hierarchy!",
        "points": [
            "<strong>Division of Labour:</strong> In multicellular life, specialised cell populations group together to perform specific bodily functions with maximal physiological efficiency.",
            "<strong>Scientific Definition of Tissue:</strong> A cluster of cells similar in structure and origin that work cooperatively to perform a common, specialized function.",
            "<strong>Hierarchy of Biological Organisation:</strong> Cell $\\to$ Tissue $\\to$ Organ $\\to$ Organ System $\\to$ Complex Multicellular Organism.",
            "<strong>Structural & Functional Synergy:</strong> For example, muscle cells contract to create movement, nerve cells carry impulses, and vascular tissues transport water and food."
        ],
        "checkpoints": [
            {
                "question": "Which of the following best defines a biological tissue?",
                "options": [
                    "Any random collection of cells within an organism",
                    "A group of cells similar in structure and origin working together to perform a specific function",
                    "An isolated single cell that performs all metabolic functions",
                    "A cluster of dead cells providing exclusively physical protection"
                ],
                "correct": 1,
                "explanation": "A tissue is precisely defined as an ensemble of cells with similar structure and developmental origin working collaboratively to carry out a specific physiological function."
            },
            {
                "question": "What is the primary evolutionary advantage of having tissues in multicellular organisms?",
                "options": [
                    "Decreased need for nutrient absorption",
                    "Division of labour leading to high functional efficiency and specialization",
                    "Elimination of the need for an organ system",
                    "Complete independence of individual cells from one another"
                ],
                "correct": 1,
                "explanation": "Division of labour assigns distinct tasks to specialized cellular groups, ensuring far higher metabolic efficiency and functional competence than a single unspecialized cell."
            }
        ]
    },

    # Slide 2: Plant vs Animal Tissues: Fundamental Architectural Contrast
    {
        "id": 2,
        "title": "Plant vs Animal Tissues: Fundamental Architectural Contrast",
        "subtitle": "Stationary Autotrophs vs Motile Heterotrophs Shaping Cellular Anatomy",
        "narration": "Why do plants and animals possess fundamentally different tissues? The answer lies in their modes of life! Plants are stationary and rooted. They require immense mechanical strength and structural rigidity to withstand fierce winds and environmental stress; consequently, most plant supportive tissues—such as sclerenchyma and cork—consist of dead cells with thick walls. Furthermore, plant growth is restricted to localized zones called meristems. Animals, in contrast, are active, motile heterotrophs that move in search of food, mates, and shelter. Their tissues are overwhelmingly living, demand substantially more energy, and experience uniform, non-localized growth across the body.",
        "points": [
            "<strong>Locomotion vs Stationary Habit:</strong> Plants are rooted and stationary, whereas animals exhibit active locomotion for food, shelter, and survival.",
            "<strong>Living vs Dead Structural Components:</strong> Plant supportive tissues are predominantly composed of dead, lignified cells providing mechanical rigidity without metabolic cost; animal tissues are largely living.",
            "<strong>Growth Patterns:</strong> Plant growth is localized to perpetual dividing zones (meristems); animal cell growth is uniform and unlocalized throughout organs.",
            "<strong>Metabolic Energy Demand:</strong> Animals possess higher metabolic rates and demand more ATP energy than plants, requiring specialized circulatory and respiratory tissues."
        ],
        "checkpoints": [
            {
                "question": "Why do most supportive structural tissues in mature plants consist of dead cells?",
                "options": [
                    "Dead cells cannot be attacked by pathogens",
                    "Dead cells provide mechanical tensile strength with minimal energy and maintenance cost",
                    "Plant roots cannot absorb enough water to keep supportive cells alive",
                    "Plants intentionally destroy cells to reduce their weight"
                ],
                "correct": 1,
                "explanation": "Dead lignified cell walls provide immense structural support and rigidity to stationary plants without requiring ongoing metabolic maintenance or ATP consumption."
            },
            {
                "question": "How does the pattern of growth differ between plants and animals?",
                "options": [
                    "Plant growth is restricted to specific localized meristematic regions, whereas animal growth is uniform throughout the body",
                    "Animal growth occurs only at the tips of fingers and toes",
                    "Plants grow only for the first two years of their life",
                    "Animal tissues divide only in the presence of direct sunlight"
                ],
                "correct": 0,
                "explanation": "Plant growth is localized to specific regions called meristems (apical, intercalary, lateral), while animal tissue growth is uniform and distributed throughout the organism."
            }
        ]
    },

    # Slide 3: Plant Meristematic Tissues: The Cellular Division Engines
    {
        "id": 3,
        "title": "Plant Meristematic Tissues: The Cellular Division Engines",
        "subtitle": "Characteristics & Regional Classification: Apical, Intercalary, and Lateral",
        "narration": "Plants grow continuously throughout their lifespan because of specialized dividing tissues known as meristematic tissues. Meristematic cells are compact, possessing thin primary cellulose walls, dense granular cytoplasm, and prominent nuclei. Noticeably, they lack vacuoles because their sole mission is active, continuous mitotic division, leaving no need for nutrient or sap storage. Depending on their location, meristems are classified into three types: Apical meristems at root and shoot tips for primary linear elongation; Intercalary meristems at internodes and leaf bases allowing rapid regrowth in grazed grasses; and Lateral meristems, such as cambium, which expand stem and root girth through secondary growth.",
        "points": [
            "<strong>Cytological Features:</strong> Meristematic cells possess dense cytoplasm, thin cellulose walls, prominent nuclei, and lack vacuoles due to continuous cell division.",
            "<strong>Apical Meristem:</strong> Located at the growing apices of stems and roots; responsible for primary linear elongation (increasing plant height and root depth).",
            "<strong>Intercalary Meristem:</strong> Situated at the base of leaves or internodes (e.g., in grasses and bamboo); elongates internodal regions and enables regrowth after grazing.",
            "<strong>Lateral Meristem (Cambium):</strong> Located along the lateral axes of roots and stems; responsible for secondary growth, increasing the diameter and girth."
        ],
        "checkpoints": [
            {
                "question": "Why do actively dividing meristematic cells typically lack vacuoles?",
                "options": [
                    "Vacuoles would cause the cells to burst under atmospheric pressure",
                    "They are actively engaged in rapid mitotic division and do not require nutrient storage or turgor regulation",
                    "They do not have a nucleus to synthesize vacuoles",
                    "Plant cell walls prevent the formation of vacuoles in all plant cells"
                ],
                "correct": 1,
                "explanation": "Meristematic cells divide rapidly and continually; they do not store food, metabolic waste, or cell sap, making large vacuoles functionally unnecessary."
            },
            {
                "question": "Which meristematic tissue is specifically responsible for the increase in girth (thickness) of a tree trunk?",
                "options": [
                    "Apical meristem",
                    "Intercalary meristem",
                    "Lateral meristem (cambium)",
                    "Protoderm"
                ],
                "correct": 2,
                "explanation": "Lateral meristems (vascular cambium and cork cambium) divide tangentially to produce secondary vascular tissues and bark, thereby expanding trunk girth."
            }
        ]
    },

    # Slide 4: C-8.2 Laboratory Investigation: Onion Root Tip Apical Growth
    {
        "id": 4,
        "title": "C-8.2 Laboratory Investigation: Onion Root Tip Apical Growth",
        "subtitle": "Empirical Proof of Apical Meristem Activity Through Tip Excision",
        "narration": "To empirically investigate meristematic growth, NCERT outlines a foundational experiment using two onion bulbs placed over glass jars filled with water. In both Jar 1 and Jar 2, roots emerge and elongate steadily during Days 1, 2, and 3. On Day 4, we use fine scissors to clip off the terminal 1 cm of the roots in Jar 2, leaving Jar 1 completely intact as our control. When we measure and record the root lengths on Day 4 and Day 5, the data reveals a dramatic divergence: Jar 1 roots continue elongating from 2.5 cm to over 4.2 cm, whereas Jar 2 roots halt growth completely! This proves conclusively that the cells responsible for linear root elongation reside strictly in the terminal apical meristem.",
        "points": [
            "<strong>Experimental Protocol:</strong> Place two onion bulbs over water-filled glass jars; roots grow down into the water under ambient conditions.",
            "<strong>Observation & Measurement (Days 1–3):</strong> Record root lengths daily using a transparent metric ruler; both jars show steady primary elongation.",
            "<strong>Experimental Intervention (Day 4):</strong> Excise the terminal 1 cm root tip from all roots in Jar 2, while maintaining Jar 1 as an unmanipulated control.",
            "<strong>Empirical Finding & Inference:</strong> Jar 1 roots continue growing to 4.2 cm; Jar 2 roots show zero elongation after Day 4, demonstrating that primary linear growth depends entirely on intact apical meristematic tissues."
        ],
        "checkpoints": [
            {
                "question": "In the onion root tip experiment, why did the roots in Jar 2 stop growing after their tips were clipped on Day 4?",
                "options": [
                    "Water could no longer enter the clipped roots",
                    "The apical meristem responsible for cell division and linear elongation was excised",
                    "The onion bulb ran out of stored carbohydrates",
                    "Root hairs poisoned the surrounding water"
                ],
                "correct": 1,
                "explanation": "Linear growth in roots is driven exclusively by the root apical meristem located at the apex. Removing the terminal tip eliminates the dividing cell pool, halting elongation."
            },
            {
                "question": "What is the scientific purpose of keeping Jar 1 unclipped throughout the entire five-day observation period?",
                "options": [
                    "To serve as an experimental control demonstrating normal baseline growth under identical conditions",
                    "To allow the onion bulb in Jar 1 to flower faster",
                    "To collect extra water for chemical testing",
                    "To observe lateral root formation only"
                ],
                "correct": 0,
                "explanation": "Jar 1 acts as the experimental control group, confirming that environmental factors (water, temperature, light) support normal elongation throughout the testing period."
            }
        ]
    },

    # Slide 5: Permanent Tissues & The Differentiation Process
    {
        "id": 5,
        "title": "Permanent Tissues & The Differentiation Process",
        "subtitle": "From Actively Dividing Meristems to Specialized Permanent Architectures",
        "narration": "What happens to the new daughter cells produced by meristematic division? They do not divide indefinitely! Instead, they undergo a magnificent developmental transformation known as cellular differentiation. Differentiation is the developmental process whereby newly formed cells lose the capacity to divide, take up a fixed shape and size, and acquire specialized structural adaptations to execute specific physiological functions. Once differentiated, they constitute permanent tissues. Permanent tissues are broadly categorized into two major divisions: Simple Permanent Tissues, composed of a single cell type acting uniformly, and Complex Permanent Tissues, constructed from multiple collaborating cell types.",
        "points": [
            "<strong>Concept of Differentiation:</strong> The developmental process wherein meristem-derived cells cease dividing and acquire permanent anatomical shapes, wall modifications, and physiological specializations.",
            "<strong>Formation of Permanent Tissues:</strong> Arise directly from meristematic cells that have matured and exited the cell division cycle.",
            "<strong>Simple Permanent Tissues:</strong> Homogeneous tissues composed of only one morphological cell type performing a uniform function (e.g., parenchyma, collenchyma, sclerenchyma).",
            "<strong>Complex Permanent Tissues:</strong> Heterogeneous tissues composed of multiple structurally distinct cell types working in coordinated synergy (e.g., xylem and phloem)."
        ],
        "checkpoints": [
            {
                "question": "What is meant by the biological term 'differentiation' in plant development?",
                "options": [
                    "The process of a cell dividing into two identical daughter cells",
                    "The process by which unspecialized cells take up a permanent shape, size, and specialized function, losing the ability to divide",
                    "The death and decomposition of aged plant tissues",
                    "The movement of water through the vascular bundle"
                ],
                "correct": 1,
                "explanation": "Differentiation refers to the developmental maturation of newly divided cells into permanent, functionally specialized tissues with fixed morphological properties."
            },
            {
                "question": "Which of the following distinguishes a simple permanent tissue from a complex permanent tissue?",
                "options": [
                    "Simple tissues are dead while complex tissues are always living",
                    "Simple tissues consist of a single cell type, whereas complex tissues are composed of more than one cell type working together",
                    "Simple tissues are found only in roots, while complex tissues are found only in leaves",
                    "Simple tissues can divide indefinitely, while complex tissues cannot"
                ],
                "correct": 1,
                "explanation": "Simple permanent tissues (parenchyma, collenchyma, sclerenchyma) are made of only one cell type, whereas complex tissues (xylem, phloem) integrate multiple distinct cell types."
            }
        ]
    },

    # Slide 6: Simple Permanent Tissues: Parenchyma, Chlorenchyma & Aerenchyma
    {
        "id": 6,
        "title": "Simple Permanent Tissues: Parenchyma, Chlorenchyma & Aerenchyma",
        "subtitle": "Living Ground Tissue: Food Storage, Photosynthesis, and Aquatic Buoyancy",
        "narration": "Parenchyma is the most abundant, fundamental simple permanent tissue in plants. Parenchyma cells are living, possess thin primary walls made of cellulose, and feature prominent intercellular spaces between loosely packed cells. They form the basic packing tissue in roots, stems, and fruits, functioning primarily in nutrient and water storage. When parenchyma cells develop chloroplasts in leaves and green stems to carry out photosynthesis, they are termed Chlorenchyma. In aquatic plants like water hyacinth and lotus petioles, parenchyma cells form enormous internal air chambers; this specialized tissue is known as Aerenchyma, providing both buoyancy to float on water and pathways for gas exchange.",
        "points": [
            "<strong>Parenchyma Structure:</strong> Living, isodiametric or oval cells with thin primary cellulose walls, large central vacuoles, and distinct intercellular spaces.",
            "<strong>Primary Functions:</strong> Serves as general ground packing tissue, stores food (starch, proteins, oils), and maintains turgidity in soft plant organs.",
            "<strong>Chlorenchyma Specialization:</strong> Parenchyma containing abundant chloroplasts, forming the mesophyll of leaves to actively synthesize carbohydrates via photosynthesis.",
            "<strong>Aerenchyma Specialization:</strong> Parenchyma containing extensive interconnected air cavities in aquatic hydrophytes (e.g., Eichhornia), providing positive buoyancy and facilitating internal ventilation."
        ],
        "checkpoints": [
            {
                "question": "What special modification characterizes aerenchyma in aquatic hydrophytes?",
                "options": [
                    "Heavily lignified cell walls that prevent water entry",
                    "Large interconnected air cavities that provide buoyancy and facilitate internal gas exchange",
                    "Complete absence of cell membranes to allow rapid nutrient flow",
                    "Dense clusters of calcium carbonate crystals"
                ],
                "correct": 1,
                "explanation": "Aerenchyma features large internal air spaces that trap air, giving aquatic plants buoyancy to float on water surfaces and aiding gas diffusion."
            },
            {
                "question": "Chlorenchyma is a specialized form of which plant tissue?",
                "options": [
                    "Sclerenchyma",
                    "Collenchyma",
                    "Parenchyma containing chloroplasts",
                    "Xylem vessels"
                ],
                "correct": 2,
                "explanation": "Chlorenchyma is simply parenchyma tissue that contains chloroplasts, performing photosynthesis in leaves and green herbaceous stems."
            }
        ]
    },

    # Slide 7: Collenchyma & Sclerenchyma: Flexibility vs Hard Armor
    {
        "id": 7,
        "title": "Collenchyma & Sclerenchyma: Flexibility vs Hard Armor",
        "subtitle": "Tensile Elasticity in Stalks vs Lignified Compressive Armour in Shells",
        "narration": "Next, let us compare the two mechanical supportive tissues: Collenchyma and Sclerenchyma. Collenchyma consists of elongated, living cells that possess irregular thickenings at their corners, deposited with pectin and cellulose, with little or no intercellular space. Collenchyma provides mechanical flexibility, allowing plant parts like leaf stalks, young stems, and climbing tendrils to bend gracefully in stormy winds without snapping! In contrast, Sclerenchyma consists of long, narrow, dead cells with tremendously thickened secondary walls impregnated with lignin—a waterproof chemical cement. Sclerenchyma cells lack cytoplasm and lumen space, providing extraordinary hardness, as seen in the protective husk of coconuts, walnut shells, and jute fibres.",
        "points": [
            "<strong>Collenchyma Anatomy:</strong> Elongated living cells with localized corner wall thickenings rich in pectin and cellulose; minimal intercellular spaces.",
            "<strong>Collenchyma Function:</strong> Imparts mechanical flexibility and tensile elasticity, permitting leaves, petioles, and tendrils to bend without breaking.",
            "<strong>Sclerenchyma Anatomy:</strong> Dead, long, narrow fibre-like cells with heavily lignified secondary cell walls and narrow or obliterated central lumens; zero intercellular spaces.",
            "<strong>Sclerenchyma Occurrence:</strong> Provides extreme rigidity and compressive strength; abundant in coconut husk (coir), walnut shells, seed coats, pear fruit grit (sclereids), and jute/hemp fibres."
        ],
        "checkpoints": [
            {
                "question": "Which tissue allows plant tendrils and leaf petioles to bend flexibly in high winds without breaking?",
                "options": [
                    "Sclerenchyma",
                    "Collenchyma",
                    "Aerenchyma",
                    "Xylem vessels"
                ],
                "correct": 1,
                "explanation": "Collenchyma is the living mechanical tissue that provides tensile flexibility and elasticity, allowing climbing tendrils and petioles to bend without snapping."
            },
            {
                "question": "What chemical substance is deposited in the cell walls of sclerenchyma, making them hard, rigid, and impermeable?",
                "options": [
                    "Lignin",
                    "Starch",
                    "Chlorophyll",
                    "Glycogen"
                ],
                "correct": 0,
                "explanation": "Lignin is a complex organic polymer deposited in sclerenchyma secondary cell walls that acts as a waterproof cement, providing extreme rigidity and strength."
            }
        ]
    },

    # Slide 8: Protective Tissues in Plants: Epidermis, Stomata & Cork (Phellem)
    {
        "id": 8,
        "title": "Protective Tissues in Plants: Epidermis, Stomata & Cork (Phellem)",
        "subtitle": "Outer Protective Armours: Cuticular Waxes, Guard Cell Gates, and Suberised Bark",
        "narration": "Plants shield themselves from desiccating winds, mechanical injury, and fungal parasites through specialized protective tissues. The outermost layer is the Epidermis, typically a single sheet of continuous cells covered by a waxy, water-resistant layer called the cuticle, made of cutin. The epidermis is punctuated by microscopic pores called Stomata, guarded by paired, kidney-shaped guard cells that regulate transpirational water loss and photosynthetic gas exchange. In desert xerophytes, the cuticle is exceptionally thick to conserve water. As perennial trees age, secondary meristems produce Cork, or Phellem. Cork consists of compactly arranged, dead cells impregnated with Suberin, a fatty substance that renders tree bark completely impervious to water and gases.",
        "points": [
            "<strong>Epidermal Layer:</strong> Single outermost cell layer covered by a waxy cuticle made of cutin; shields internal tissues from water loss, physical abrasion, and fungal infection.",
            "<strong>Stomatal Apparatus:</strong> Microscopic pores bounded by two kidney-shaped guard cells (dumb-bell shaped in grasses) regulating transpiration and $CO_2/O_2$ exchange.",
            "<strong>Xerophytic Adaptations:</strong> Desert plants possess sunken stomata and thick waxy cuticles to drastically minimize transpirational water loss.",
            "<strong>Cork (Phellem) Formation:</strong> In mature woody stems, cork cambium generates dense layers of dead cork cells impregnated with suberin, forming an impermeable, fire-resistant protective bark."
        ],
        "checkpoints": [
            {
                "question": "What is the primary role of the chemical 'suberin' found in the walls of cork cells?",
                "options": [
                    "To attract pollinating insects",
                    "To make the cell walls impervious to gases and water",
                    "To speed up photosynthesis in tree trunks",
                    "To absorb mineral salts directly from the atmosphere"
                ],
                "correct": 1,
                "explanation": "Suberin is a waxy, hydrophobic substance deposited in cork cell walls that makes bark impermeable to water and gases, protecting mature trees."
            },
            {
                "question": "Which specialized epidermal cells regulate the opening and closing of stomatal pores for gas exchange and transpiration?",
                "options": [
                    "Companion cells",
                    "Guard cells",
                    "Tracheids",
                    "Sclereids"
                ],
                "correct": 1,
                "explanation": "Guard cells are paired, kidney-shaped epidermal cells that swell with turgor pressure to open the stomatal pore and shrink when flaccid to close it."
            }
        ]
    },

    # Slide 9: Complex Permanent Tissues: Xylem (Water & Mineral Transport)
    {
        "id": 9,
        "title": "Complex Permanent Tissues: Xylem (Water & Mineral Transport)",
        "subtitle": "Vascular Plumbing: Unidirectional Ascent of Sap Driven by Transpirational Pull",
        "narration": "Now let us examine the complex permanent tissues that form the plant vascular bundle. Xylem is the specialized conducting tissue responsible for the unidirectional upward transport of water and dissolved mineral nutrients from roots to leaves. Xylem is constructed from four distinct cellular elements. Tracheids are elongated, dead tubular cells with tapering ends and lignified pitted walls. Vessels are continuous, cylindrical pipelines formed by dead cells with dissolved end walls. Xylem Fibres provide mechanical support with thick lignified walls. Crucially, Xylem Parenchyma is the ONLY living component of xylem; it stores starch and fats and assists in the sideways, radial conduction of water.",
        "points": [
            "<strong>Unidirectional Conduction:</strong> Xylem transports water and dissolved inorganic minerals strictly upward from subterranean roots to aerial stems and leaves.",
            "<strong>Tracheids & Vessels:</strong> Dead, tubular conducting conduits with lignified walls; vessels form continuous open-ended pipes, ensuring efficient bulk sap ascent.",
            "<strong>Xylem Fibres:</strong> Dead sclerenchymatous elements with heavily thickened walls providing tensile mechanical support to the vascular bundle.",
            "<strong>Xylem Parenchyma (The Living Element):</strong> The sole living component of xylem; stores starch and lipids, and facilitates radial, lateral transport of water through ray parenchyma."
        ],
        "checkpoints": [
            {
                "question": "Which of the four cellular components of xylem is the only living tissue element?",
                "options": [
                    "Tracheids",
                    "Xylem vessels",
                    "Xylem parenchyma",
                    "Xylem fibres"
                ],
                "correct": 2,
                "explanation": "Xylem parenchyma is the only living component in xylem; tracheids, vessels, and xylem fibres are all dead at maturity with lignified walls."
            },
            {
                "question": "What is the primary direction of sap flow in xylem conducting elements?",
                "options": [
                    "Bidirectional, moving up and down simultaneously",
                    "Unidirectional, moving upward from roots to leaves",
                    "Strictly downward from leaves to roots",
                    "Circular around the circumference of the stem"
                ],
                "correct": 1,
                "explanation": "Xylem sap transport is strictly unidirectional, moving upward from roots to stems and leaves, driven by root pressure and transpirational pull."
            }
        ]
    },

    # Slide 10: Complex Permanent Tissues: Phloem (Translocation of Solutes)
    {
        "id": 10,
        "title": "Complex Permanent Tissues: Phloem (Translocation of Solutes)",
        "subtitle": "Bidirectional Translocation of Photosynthates: Sieve Tubes & Companion Cells",
        "narration": "While xylem carries water upward, Phloem conducts synthesized organic food—primarily sucrose and amino acids—bidirectionally from photosynthetic leaf sources to growing sinks like roots, shoot apices, fruits, and storage organs. Phloem comprises four cellular elements. Sieve Tubes are elongated, living cylindrical cells connected by perforated end walls called sieve plates; remarkably, mature sieve tubes lack a nucleus to maximize solute flow! Adjacent to each sieve tube sits a nucleated Companion Cell, which serves as its metabolic lifeline, actively regulating sugar loading using ATP. Phloem Parenchyma stores nutrients, while Phloem Fibres, or bast fibres, are the ONLY dead elements in phloem, harvested commercially as linen, jute, and hemp.",
        "points": [
            "<strong>Bidirectional Translocation:</strong> Transports organic photosynthates (sucrose, amino acids) bidirectionally between photosynthetic sources and storage/growth sinks.",
            "<strong>Sieve Tubes & Sieve Plates:</strong> Living tubular cells with perforated end plates; mature sieve tube elements lack a nucleus, vacuoles, and ribosomes to facilitate flow.",
            "<strong>Companion Cells (Metabolic Lifeline):</strong> Nucleated, specialized parenchymatous cells connected via plasmodesmata to sieve tubes, actively driving solute loading via ATP.",
            "<strong>Phloem Fibres (Bast Fibres):</strong> The only dead component in phloem; highly lignified sclerenchyma providing support and harvested commercially as jute, flax, and hemp."
        ],
        "checkpoints": [
            {
                "question": "Which component of phloem is unique in being the only dead element at functional maturity?",
                "options": [
                    "Sieve tubes",
                    "Companion cells",
                    "Phloem parenchyma",
                    "Phloem fibres (bast fibres)"
                ],
                "correct": 3,
                "explanation": "Phloem fibres are the only dead component in phloem; sieve tubes, companion cells, and phloem parenchyma are all living cellular elements."
            },
            {
                "question": "How do mature sieve tube elements manage their metabolic functions despite lacking a cell nucleus?",
                "options": [
                    "They absorb DNA directly from passing rainwater",
                    "They are metabolically managed and regulated by intimately connected, nucleated companion cells",
                    "They do not perform any living functions and are completely dead",
                    "Their chloroplasts take over all nuclear functions"
                ],
                "correct": 1,
                "explanation": "Sieve tubes are connected to companion cells via dense plasmodesmata; the companion cell's nucleus and metabolic machinery sustain both cells."
            }
        ]
    },

    # Slide 11: Animal Epithelial Tissues: The Protective Body Coverings
    {
        "id": 11,
        "title": "Animal Epithelial Tissues: The Protective Body Coverings",
        "subtitle": "Cellular Sheets, Basement Membranes, and Specialized Surface Morphologies",
        "narration": "Turning our focus to animal biology, the simplest and most widespread covering tissues are Epithelial Tissues. Epithelial cells form tight, continuous sheets covering the entire body surface, lining internal body cavities, and enclosing visceral organs. They possess virtually no intercellular spaces and rest upon an acellular, fibrous basement membrane that separates them from underlying connective tissue. Depending on cellular morphology and physiological demand, epithelia are classified into four major varieties: Simple Squamous, extremely thin and flat for rapid diffusion in lung alveoli; Stratified Squamous, multi-layered in skin to resist mechanical abrasion; Cuboidal, cube-shaped for absorption and secretion in kidney tubules; and Columnar, tall pillar-like cells in the digestive tract, often equipped with motile cilia in the respiratory tract to propel mucus.",
        "points": [
            "<strong>General Architectural Features:</strong> Closely packed cellular sheets with minimal extracellular cement, avascular in nature, resting upon an acellular basement membrane.",
            "<strong>Squamous Epithelium:</strong> Simple flat scale-like cells (alveoli, capillary lining) for rapid gas/nutrient diffusion; Stratified squamous (skin epidermis) with keratin layers to resist physical wear and tear.",
            "<strong>Cuboidal Epithelium:</strong> Cube-shaped cells lining kidney nephron tubules and salivary ducts; provides mechanical support and participates in active secretion and selective reabsorption.",
            "<strong>Columnar & Ciliated Epithelium:</strong> Tall pillar-like cells lining stomach and intestines for absorption; Ciliated columnar in the trachea and fallopian tubes has hair-like cilia that beat rhythmically to propel mucus and ova.",
            "<strong>Glandular Epithelium:</strong> Epithelial folds that form multicellular exocrine or endocrine glands secreting enzymes, sweat, saliva, and hormones."
        ],
        "checkpoints": [
            {
                "question": "Which epithelial tissue lines the alveoli of the lungs to facilitate rapid diffusion of oxygen and carbon dioxide?",
                "options": [
                    "Stratified squamous epithelium",
                    "Simple squamous epithelium",
                    "Columnar ciliated epithelium",
                    "Glandular cuboidal epithelium"
                ],
                "correct": 1,
                "explanation": "Simple squamous epithelium consists of extremely thin, flat, single-layered cells, offering minimal resistance to the rapid diffusion of respiratory gases."
            },
            {
                "question": "What is the function of the cilia found on ciliated columnar epithelium in the human respiratory tract?",
                "options": [
                    "To digest solid food particles entering the windpipe",
                    "To beat rhythmically and sweep trapped dust, microbes, and mucus outward toward the throat",
                    "To absorb oxygen directly into bone marrow",
                    "To synthesize hormones for metabolic regulation"
                ],
                "correct": 1,
                "explanation": "Rhythmic, coordinated beating of cilia sweeps mucus laden with inhaled dust particles and pathogens upward away from the lungs toward the pharynx."
            }
        ]
    },

    # Slide 12: Animal Connective Tissues: Blood, Bone, Cartilage, Tendons & Ligaments
    {
        "id": 12,
        "title": "Animal Connective Tissues: Blood, Bone, Cartilage, Tendons & Ligaments",
        "subtitle": "Specialized Cells Embedded in Diverse Extracellular Matrices",
        "narration": "Connective tissues are the binding, supportive, and protective framework of the animal body. Unlike closely packed epithelia, connective tissue cells are loosely spaced and embedded within an abundant extracellular matrix, which may be fluid, jelly-like, dense, or rigid. Blood has a fluid matrix called plasma carrying erythrocytes (RBCs) for oxygen transport, leukocytes (WBCs) for immune defense, and thrombocytes (platelets) for clotting. Bone features a hard, rigid matrix heavily mineralized with calcium and phosphorus salts surrounding osteocytes. Cartilage, found in the ear pinna, nose tip, and joint surfaces, has a solid yet flexible matrix of proteins and sugars. Furthermore, dense regular fibrous tissues include Ligaments, which connect Bone to Bone with high elasticity, and Tendons, which anchor Muscle to Bone with exceptional tensile toughness.",
        "points": [
            "<strong>Matrix-Based Organization:</strong> Widely separated cells suspended in an extracellular matrix that determines the tissue's physical and mechanical properties.",
            "<strong>Vascular Fluid Tissue (Blood & Lymph):</strong> Liquid plasma matrix containing RBCs (hemoglobin), WBCs (phagocytes and lymphocytes), and platelets (clotting cascade).",
            "<strong>Skeletal Framework (Bone & Cartilage):</strong> Bone has a rigid matrix rich in calcium phosphate and collagen; Cartilage possesses a pliable matrix of chondroitin sulfate and proteins, smoothing articular joint surfaces.",
            "<strong>Dense Regular Connective Tissue:</strong> Ligaments connect bone to bone with high elasticity and strength; Tendons connect muscle to bone with immense tensile strength but limited elasticity.",
            "<strong>Areolar & Adipose Tissues:</strong> Areolar tissue packs spaces between organs and aids tissue repair; Adipose tissue stores lipid fat droplets beneath the skin, functioning as an indispensable thermal insulator."
        ],
        "checkpoints": [
            {
                "question": "What structural difference distinguishes ligaments from tendons?",
                "options": [
                    "Ligaments connect muscle to bone, while tendons connect bone to bone",
                    "Ligaments connect bone to bone and are highly elastic, while tendons connect muscle to bone and are tough with limited elasticity",
                    "Tendons contain a liquid matrix, while ligaments have a mineralized matrix",
                    "Ligaments are found only in the brain, while tendons are found only in the heart"
                ],
                "correct": 1,
                "explanation": "Ligaments bind bone to bone with remarkable elasticity and tensile strength; tendons anchor skeletal muscle to bone with great toughness and limited flexibility."
            },
            {
                "question": "Which mineral salts constitute the primary hardening components of the human bone extracellular matrix?",
                "options": [
                    "Sodium chloride and potassium iodide",
                    "Calcium and phosphorus compounds",
                    "Magnesium sulphate and iron oxide",
                    "Copper carbonate and zinc silicate"
                ],
                "correct": 1,
                "explanation": "The rigid extracellular matrix of bone is heavily impregnated with calcium phosphate and calcium carbonate salts, imparting exceptional compressive hardness."
            }
        ]
    },

    # Slide 13: Muscular Tissues: Striated, Smooth & Cardiac Muscles
    {
        "id": 13,
        "title": "Muscular Tissues: Striated, Smooth & Cardiac Muscles",
        "subtitle": "Contractile Myofibrils Driving Voluntary Locomotion and Involuntary Rhythms",
        "narration": "Muscular tissues consist of elongated muscle fibres containing specialized contractile proteins—actin and myosin—that slide past one another to contract and relax, producing bodily movement. Animal muscles are divided into three distinct categories. Striated or skeletal muscle fibres are long, cylindrical, unbranched, multinucleate, and feature alternating light and dark bands under the microscope; they are voluntary, attached to bones, and fatigue under sustained exertion. Smooth or unstriated muscle fibres are spindle-shaped, uninucleate, and lack striations; they are involuntary, lining internal organs like the stomach, intestines, and blood vessels. Finally, Cardiac muscle forms the heart wall; its cells are cylindrical, branched, uninucleate, and linked by specialized intercalated discs, generating rhythmic, involuntary contractions tirelessly throughout a human life without fatigue!",
        "points": [
            "<strong>Contractile Engine:</strong> Muscle fibres shorten and lengthen via sliding interactions of actin and myosin filaments, converting chemical ATP into mechanical force.",
            "<strong>Striated (Skeletal / Voluntary):</strong> Long cylindrical unbranched fibres, multinucleated (syncytial), distinct cross-striations, under conscious voluntary control, susceptible to fatigue.",
            "<strong>Smooth (Visceral / Involuntary):</strong> Spindle-shaped (fusiform) unbranched cells, single central nucleus, no striations, involuntary control in gut, iris, bronchi, and blood vessels, fatigue-resistant.",
            "<strong>Cardiac (Heart Wall / Involuntary):</strong> Cylindrical, branched, uninucleated cells with faint striations and unique intercalated discs; contracts rhythmically and autonomously without fatigue."
        ],
        "checkpoints": [
            {
                "question": "Which of the following muscle tissues is branched, uninucleated, and contracts rhythmically without fatigue throughout life?",
                "options": [
                    "Striated skeletal muscle",
                    "Smooth visceral muscle",
                    "Cardiac muscle",
                    "Collenchymatous muscle"
                ],
                "correct": 2,
                "explanation": "Cardiac muscle fibres are uniquely branched, uninucleated, faintly striated, joined by intercalated discs, and execute continuous rhythmic contractions without muscular fatigue."
            },
            {
                "question": "What microscopic feature gives skeletal muscle fibres their alternate 'striated' appearance?",
                "options": [
                    "Bacterial colonies living on the cell membrane",
                    "Regularly organized alternating light (actin) and dark (myosin) protein bands",
                    "Layers of dead cork cells deposited along the fibres",
                    "Perforations in the cell wall resembling sieve plates"
                ],
                "correct": 1,
                "explanation": "The striated appearance arises from the precise repeating alignment of thin actin filaments (I bands) and thick myosin filaments (A bands) along the myofibrils."
            }
        ]
    },

    # Slide 14: Nervous Tissue: Neurons & The Reflex Highway
    {
        "id": 14,
        "title": "Nervous Tissue: Neurons & The Reflex Highway",
        "subtitle": "High Excitability and Rapid Electrochemical Signal Transmission",
        "narration": "Nervous tissue forms the master communication network of the animal body, comprising the brain, spinal cord, and peripheral nerves. Its fundamental structural and functional unit is the Neuron, or nerve cell, which can reach up to a meter in length! A neuron consists of three anatomical zones: the Cyton or cell body, housing a prominent nucleus and granular cytoplasm; multiple short, branched Dendrites that receive incoming chemical signals from receptors or adjacent neurons; and a single elongated conducting fibre called the Axon. The axon is insulated by a fatty myelin sheath to accelerate signal speed, terminating in fine axon terminals. When an electrical nerve impulse reaches these terminals, it triggers the release of neurotransmitter chemicals across the microscopic synaptic gap, stimulating the next neuron or muscle fibre.",
        "points": [
            "<strong>Excitability & Conduction:</strong> Nervous tissue is specialized to perceive external and internal stimuli and transmit rapid electrochemical impulses over long bodily distances.",
            "<strong>Cyton (Cell Body / Soma):</strong> Central metabolic hub containing the nucleus, cytoplasm, and granular Nissl bodies.",
            "<strong>Dendrites:</strong> Short, highly branched protoplasmic projections that receive sensory inputs and direct incoming electrical impulses toward the cyton.",
            "<strong>Axon & Synapse:</strong> A single, extended transmission fibre (often up to 1 meter long) insulated by a myelin sheath that conducts action potentials to axon terminals, triggering neurotransmitter release across synapses."
        ],
        "checkpoints": [
            {
                "question": "What is the correct pathway of a nerve impulse traveling through a single neuron?",
                "options": [
                    "Axon $\\to$ Cyton $\\to$ Dendrite $\\to$ Synapse",
                    "Dendrite $\\to$ Cyton (Cell Body) $\\to$ Axon $\\to$ Axon Terminal (Synapse)",
                    "Synapse $\\to$ Axon $\\to$ Cyton $\\to$ Dendrite",
                    "Cyton $\\to$ Dendrite $\\to$ Axon Terminal $\\to$ Axon"
                ],
                "correct": 1,
                "explanation": "Incoming stimuli are received by dendrites, integrated in the cyton (cell body), and conducted away along the axon to the axon terminal for synaptic transmission."
            },
            {
                "question": "What is the specialized microscopic junction where a nerve impulse passes chemically from one neuron to another called?",
                "options": [
                    "Sieve plate",
                    "Intercalated disc",
                    "Synapse",
                    "Basement membrane"
                ],
                "correct": 2,
                "explanation": "A synapse is the microscopic junction between the terminal end of an axon and the dendrite or cell body of an adjacent neuron, mediated by neurotransmitters."
            }
        ]
    },

    # Slide 15: Musculoskeletal System, Joints, Injury Recovery & Posture (C-5.3, C-6.1, C-7.1)
    {
        "id": 15,
        "title": "Musculoskeletal System, Joints, Injury Recovery & Posture",
        "subtitle": "Joint Mechanics, R.I.C.E. Rehabilitation Protocol, and Yogic Ergonomics",
        "narration": "Movement is an intricate symphony orchestrated by the musculoskeletal system. Bones provide the rigid levers, synovial joints furnish articulation, ligaments stabilize the framework, and skeletal muscles apply pulling forces through non-elastic tendons. Synovial joints include ball-and-socket joints at the shoulder and hip for 360-degree rotation, hinge joints at the elbow and knee for planar swing, pivot joints at the neck atlas-axis, and gliding joints between wrist carpals. When overexertion occurs, athletes distinguish between a Strain—a stretch or micro-tear of muscle or tendon—and a Sprain, which involves ligament damage. Medical rehabilitation adheres to the R.I.C.E protocol: Rest to prevent tear expansion, Ice to vasoconstrict and limit swelling, Compression to reduce interstitial edema, and Elevation to facilitate lymphatic drainage. Finally, ancient Indian yogic asanas like Tadasana and Bhujangasana enhance spinal alignment, engage core stabilizer muscles, and lubricate articular cartilage, preventing postural defects.",
        "points": [
            "<strong>Joint Classifications:</strong> Immovable fibrous sutures (skull), slightly movable cartilaginous joints (intervertebral discs), and freely movable synovial joints (ball-and-socket, hinge, pivot, gliding, saddle).",
            "<strong>Biomechanical Coordination:</strong> Antagonistic muscle pairs (e.g., biceps flexion vs triceps extension) exert mechanical traction through tendons across articulating synovial joints stabilized by collateral ligaments.",
            "<strong>Clinical Injury Distinction:</strong> Strain = injury/overstretch to muscle fibres or tendons; Sprain = stretching or tearing of stabilizing joint ligaments.",
            "<strong>Medical Recovery Protocol (R.I.C.E):</strong> Rest (immobilization), Ice (cold therapy for vasoconstriction), Compression (elastic wrap limiting edema), and Elevation (gravity venous drainage).",
            "<strong>Yogic Ergonomics (C-6.1):</strong> Daily practice of asanas (Tadasana, Bhujangasana) engages deep postural core muscles, maintains physiological spinal curvature, and prevents kyphosis and lordosis."
        ],
        "checkpoints": [
            {
                "question": "Which medical protocol is universally recommended as the immediate first-line response for acute muscle strains and ligament sprains?",
                "options": [
                    "Vigorous deep tissue massage and immediate sprinting",
                    "R.I.C.E protocol: Rest, Ice, Compression, and Elevation",
                    "Applying boiling hot compresses directly over the swollen joint",
                    "Complete dehydration to eliminate fluid build-up"
                ],
                "correct": 1,
                "explanation": "The R.I.C.E protocol (Rest, Ice, Compression, Elevation) limits internal bleeding, reduces inflammatory edema via vasoconstriction, and protects damaged tissues from further trauma."
            },
            {
                "question": "What type of synovial joint allows 360-degree multidirectional rotational movement in the human shoulder and hip?",
                "options": [
                    "Hinge joint",
                    "Pivot joint",
                    "Ball-and-socket joint",
                    "Gliding joint"
                ],
                "correct": 2,
                "explanation": "A ball-and-socket joint features a rounded spherical bone head articulating inside a cup-like depression, providing the greatest range of rotational motion."
            }
        ]
    },

    # Slide 16: Indian Scientific Pioneer: Prof. Sipra Guha-Mukherjee & Prof. S.C. Maheshwari (C-6.1)
    {
        "id": 16,
        "title": "Indian Scientific Pioneer: Prof. Sipra Guha-Mukherjee & Prof. S.C. Maheshwari",
        "subtitle": "Breakthrough Discovery of In Vitro Androgenesis & Haploid Plant Regeneration",
        "narration": "In the annals of plant biotechnology, India holds a pioneering position through the transformative work of Professor Sipra Guha-Mukherjee and Professor Satish Chandra Maheshwari at the Department of Botany, University of Delhi. In 1964, they achieved an extraordinary world-first breakthrough: by culturing immature anthers and pollen microspores of the thorn-apple plant, Datura innoxia, on nutrient agar media, they discovered that haploid pollen cells could be stimulated to bypass normal sexual gamete pathways and develop directly into embryos and whole, viable haploid plants! Published in the prestigious journal Nature in 1964 and 1966, this discovery of in vitro androgenesis proved cellular totipotency in pollen grains, revolutionizing plant tissue culture and crop breeding by enabling the production of completely homozygous pure lines in a single generation.",
        "points": [
            "<strong>Historic Discovery (1964–1966):</strong> Prof. Sipra Guha-Mukherjee and Prof. S.C. Maheshwari at University of Delhi discovered that cultured anthers of Datura innoxia generate haploid embryos and whole plants.",
            "<strong>World Landmark in Androgenesis:</strong> First empirical demonstration in the world that male gametophytic pollen cells possess cellular totipotency and can develop directly into sporophytic plantlets without fertilization.",
            "<strong>International Acclaim:</strong> Their milestone findings, published in <em>Nature</em> (1964 & 1966), placed Indian botanical research at the absolute forefront of modern plant tissue culture.",
            "<strong>Agricultural & Genetic Impact:</strong> Revolutionized plant breeding by dramatically accelerating the creation of homozygous pure-breeding diploid lines through chromosome doubling in just one generation."
        ],
        "checkpoints": [
            {
                "question": "What groundbreaking biological phenomenon was discovered by Indian scientists Prof. Sipra Guha-Mukherjee and Prof. S.C. Maheshwari in 1964?",
                "options": [
                    "Production of synthetic plastic polymers from algae",
                    "Induction of haploid embryos and whole plants directly from cultured anther pollen grains (in vitro androgenesis)",
                    "Discovery of the light-independent reactions of photosynthesis",
                    "Invention of synthetic chemical insecticides"
                ],
                "correct": 1,
                "explanation": "They discovered in vitro androgenesis by culturing Datura innoxia anthers, showing that haploid pollen grains can develop directly into embryos and haploid plantlets."
            },
            {
                "question": "Why is the production of haploid plants via anther culture of immense value in agricultural crop improvement?",
                "options": [
                    "Haploid plants grow ten times taller than normal trees",
                    "It allows breeders to generate 100% homozygous pure-breeding lines in a single generation after chromosome doubling",
                    "Haploid plants do not require water or soil nutrients",
                    "It replaces the need for cellular mitosis in all crops"
                ],
                "correct": 1,
                "explanation": "Doubling the chromosome number of haploid plants produces completely homozygous diploid lines instantly, shortening plant breeding programs by many years."
            }
        ]
    },

    # Slide 17: Dedicated Quiz Challenge 1 — Plant Tissues Mastery
    {
        "id": 17,
        "title": "Dedicated Quiz Challenge 1: Plant Tissues Mastery",
        "subtitle": "Test Your Knowledge on Meristems, Simple Tissues, Xylem, and Phloem",
        "narration": "Welcome to Quiz Challenge 1! Test your conceptual mastery of plant tissues—including meristem types, onion root growth dynamics, parenchyma, collenchyma, sclerenchyma, and complex vascular conduits. Click your chosen option for each question and open the step-by-step solution modal for detailed explanations.",
        "is_quiz": True,
        "quiz_title": "Plant Tissues Mastery Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. Which plant tissue is responsible for continuous linear primary growth at the tips of shoots and roots?",
                "options": ["Lateral meristem", "Apical meristem", "Intercalary meristem", "Parenchyma"],
                "correct": 1,
                "solution": "Apical meristem is situated at the terminal tips of stems and roots, actively undergoing mitotic division to produce new cells that increase plant height and root depth."
            },
            {
                "q": "2. In the onion bulb root experiment, what caused the roots in Jar 2 to stop growing after Day 4?",
                "options": ["Lack of sunlight", "Removal of the root apical meristem by excision", "Excessive water absorption", "Bacterial infection in the water"],
                "correct": 1,
                "solution": "Excising the terminal 1 cm of the roots removed the apical meristematic zone containing dividing cells, permanently halting primary root elongation."
            },
            {
                "q": "3. Which simple permanent tissue is composed of living cells with irregular wall thickenings at corners due to pectin and cellulose deposition?",
                "options": ["Sclerenchyma", "Parenchyma", "Collenchyma", "Aerenchyma"],
                "correct": 2,
                "solution": "Collenchyma cells are living, elongated cells with localized pectocellulose thickenings at their corners, providing flexibility and tensile elasticity to growing organs."
            },
            {
                "q": "4. Coconut husk (coir) is made of which of the following mechanical plant tissues?",
                "options": ["Collenchyma", "Sclerenchyma fibres", "Parenchyma", "Chlorenchyma"],
                "correct": 1,
                "solution": "Coconut coir is composed of dead, heavily lignified sclerenchymatous fibres with thick secondary walls and narrow lumens, providing extreme hardness."
            },
            {
                "q": "5. Which tissue modification provides aquatic hydrophytes like water hyacinth with buoyancy to float?",
                "options": ["Collenchyma", "Aerenchyma", "Sclerenchyma", "Cork"],
                "correct": 1,
                "solution": "Aerenchyma is specialized parenchyma featuring large internal air chambers that trap air, giving aquatic plants positive buoyancy and aiding aeration."
            },
            {
                "q": "6. What waxy chemical deposited in the cell walls of cork makes tree bark impervious to water and gases?",
                "options": ["Pectin", "Suberin", "Cellulose", "Starch"],
                "correct": 1,
                "solution": "Suberin is a hydrophobic fatty substance deposited in the walls of dead cork cells, making them impermeable to water vapour and atmospheric gases."
            },
            {
                "q": "7. Which of the following is the only living cellular component found in xylem tissue?",
                "options": ["Tracheids", "Xylem vessels", "Xylem fibres", "Xylem parenchyma"],
                "correct": 3,
                "solution": "Xylem parenchyma is the only living element in xylem; it functions in nutrient storage and radial sideways water conduction, whereas tracheids, vessels, and fibres are dead."
            },
            {
                "q": "8. Sieve tube elements are unique because at functional maturity they:",
                "options": ["Lack a cell nucleus and ribosomes to maximize organic sap flow", "Have walls completely covered in suberin", "Are completely dead with lignified walls", "Contain numerous large chloroplasts"],
                "correct": 0,
                "solution": "Mature sieve tube elements lack a nucleus, ribosomes, and large vacuoles to minimize resistance to solute translocation; their metabolism is maintained by companion cells."
            },
            {
                "q": "9. Commercial fibres such as jute, flax, and hemp are anatomically composed of:",
                "options": ["Xylem vessels", "Phloem fibres (bast fibres)", "Epidermal hairs", "Collenchymatous petioles"],
                "correct": 1,
                "solution": "Commercial jute and flax fibres are phloem fibres (bast fibres)—the only dead sclerenchymatous element in phloem tissue, prized for high tensile strength."
            },
            {
                "q": "10. What drives the bidirectional transport of sucrose in phloem tissue compared to unidirectional ascent in xylem?",
                "options": ["Gravity pulling water down", "Active translocation requiring cellular ATP energy to move solutes from source to sink", "Capillary action in dead cell walls", "Magnetic attraction of mineral ions"],
                "correct": 1,
                "solution": "Phloem translocation is an active physiological process requiring ATP energy to load sucrose into sieve tubes, generating hydrostatic pressure gradients that drive sap toward various sinks."
            }
        ]
    },

    # Slide 18: Dedicated Quiz Challenge 2 — Animal Tissues Mastery
    {
        "id": 18,
        "title": "Dedicated Quiz Challenge 2: Animal Tissues Mastery",
        "subtitle": "Test Your Knowledge on Epithelia, Connective Tissues, Muscles, and Neurons",
        "narration": "Welcome to Quiz Challenge 2! Evaluate your command over animal histology, covering squamous and ciliated epithelia, blood and bone matrix biology, voluntary vs involuntary muscles, and neuronal anatomy. Select your answers and inspect the step-by-step solutions.",
        "is_quiz": True,
        "quiz_title": "Animal Tissues Mastery Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. What separates an epithelial tissue layer from the underlying connective tissue?",
                "options": ["A thick layer of sclerenchyma", "An acellular fibrous basement membrane", "A layer of myelin", "A continuous sheet of cork"],
                "correct": 1,
                "solution": "All epithelial tissues are anchored to an underlying acellular, non-cellular basement membrane composed of collagen and glycoproteins that separates them from connective tissue."
            },
            {
                "q": "2. Which type of epithelium forms the outer protective layer of human skin to resist mechanical abrasion?",
                "options": ["Simple cuboidal epithelium", "Stratified squamous epithelium", "Ciliated columnar epithelium", "Simple squamous epithelium"],
                "correct": 1,
                "solution": "The skin epidermis is composed of stratified squamous epithelium, consisting of multiple cell layers arranged in strata with keratin to prevent tearing and water loss."
            },
            {
                "q": "3. The fluid extracellular matrix of blood that carries red blood cells, white blood cells, and platelets is called:",
                "options": ["Lymph", "Plasma", "Synovial fluid", "Mucus"],
                "correct": 1,
                "solution": "Blood consists of a liquid extracellular matrix called plasma (containing proteins, salts, and hormones) in which RBCs, WBCs, and platelets are suspended."
            },
            {
                "q": "4. Which dense regular connective tissue connects bone to bone and possesses high elasticity?",
                "options": ["Tendon", "Ligament", "Areolar tissue", "Adipose tissue"],
                "correct": 1,
                "solution": "Ligaments are highly elastic and strong bands of dense regular connective tissue that bind articulating bones to bones at joints."
            },
            {
                "q": "5. Which tissue acts as a storage reservoir for fat droplets and serves as a thermal insulator under the skin?",
                "options": ["Areolar tissue", "Adipose tissue", "Cartilage", "Striated muscle"],
                "correct": 1,
                "solution": "Adipose tissue contains adipocytes filled with fat droplets beneath the skin and around internal organs, serving as a shock absorber and thermal insulator."
            },
            {
                "q": "6. Cartilage differs from bone primarily because its extracellular matrix is:",
                "options": ["Solid yet flexible, composed of proteins and sugars rather than hard calcium minerals", "Completely fluid like plasma", "Made exclusively of dead lignified cells", "Lacking all living cells"],
                "correct": 0,
                "solution": "Cartilage possesses a pliable, slightly elastic solid matrix composed of chondroitin sulfate proteins and sugars with widely spaced chondrocytes, unlike rigid mineralized bone."
            },
            {
                "q": "7. Skeletal muscle fibres are characterized cytologically as:",
                "options": ["Spindle-shaped, uninucleated, and involuntary", "Cylindrical, branched, and uninucleated", "Long, cylindrical, unbranched, multinucleated, and voluntary", "Non-striated, branched, and voluntary"],
                "correct": 2,
                "solution": "Skeletal (striated) muscle fibres are long, unbranched cylinders containing multiple nuclei (multinucleated/syncytial) located beneath the sarcolemma, under voluntary control."
            },
            {
                "q": "8. Involuntary, spindle-shaped muscle fibres lacking cross-striations located in the stomach and blood vessels are:",
                "options": ["Striated muscles", "Smooth (visceral) muscles", "Cardiac muscles", "Skeletal muscles"],
                "correct": 1,
                "solution": "Smooth muscle fibres are fusiform (spindle-shaped) with pointed ends, have a single central nucleus, lack striations, and govern involuntary peristalsis and vasomotion."
            },
            {
                "q": "9. Unique structural junctions called 'intercalated discs' that allow synchronized electrical conduction are found in:",
                "options": ["Cardiac muscle", "Skeletal muscle", "Smooth muscle", "Ligaments"],
                "correct": 0,
                "solution": "Intercalated discs are specialized cell junctions with gap junctions unique to cardiac muscle, synchronizing ion flow so the heart chambers contract as a coordinated functional unit."
            },
            {
                "q": "10. Which part of a neuron conducts electrical nerve impulses away from the cell body (cyton) toward the synapse?",
                "options": ["Dendrite", "Axon", "Nissl granule", "Basement membrane"],
                "correct": 1,
                "solution": "The axon is a single, elongated tubular extension of a neuron that conducts nerve impulses away from the cyton toward the axon terminals for synaptic transmission."
            }
        ]
    },

    # Slide 19: Dedicated Quiz Challenge 3 — Musculoskeletal, Joints, Injuries & Yoga
    {
        "id": 19,
        "title": "Dedicated Quiz Challenge 3: Musculoskeletal, Joints, Injuries & Yoga",
        "subtitle": "Test Your Knowledge on Joint Types, Biomechanics, R.I.C.E., and Posture",
        "narration": "Welcome to Quiz Challenge 3! Delve into the functional mechanics of the musculoskeletal system, joint varieties, agonist-antagonist muscle pairs, sports injury management via the R.I.C.E protocol, and the postural benefits of yoga asanas. Choose your answers and review the solutions.",
        "is_quiz": True,
        "quiz_title": "Musculoskeletal & Postural Care Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. What type of joint is found between the skull bones (cranial sutures)?",
                "options": ["Synovial joint", "Cartilaginous joint", "Fibrous (immovable) joint", "Pivot joint"],
                "correct": 2,
                "solution": "The cranial sutures are fibrous synarthrodial joints where bone plates interlock tightly with dense collagen, allowing zero movement to protect the brain."
            },
            {
                "q": "2. The elbow joint, which permits movement in only one plane like a hinged door, is an example of a:",
                "options": ["Ball-and-socket joint", "Hinge joint", "Pivot joint", "Gliding joint"],
                "correct": 1,
                "solution": "A hinge joint (ginglymus), seen at the elbow, knee, and interphalangeal finger joints, permits motion restricted to a single angular plane (flexion and extension)."
            },
            {
                "q": "3. What fluid acts as a hydraulic shock absorber and lubricant within freely movable joints?",
                "options": ["Cerebrospinal fluid", "Synovial fluid", "Lymph", "Amniotic fluid"],
                "correct": 1,
                "solution": "Synovial fluid is a viscous, egg-white-like fluid secreted by the synovial membrane that lubricates articulating cartilage surfaces and absorbs mechanical shocks."
            },
            {
                "q": "4. When you bend your elbow to lift a backpack, which muscle acts as the primary agonist (contracting mover) and which relaxes as the antagonist?",
                "options": ["Biceps contracts (agonist), Triceps relaxes (antagonist)", "Triceps contracts (agonist), Biceps relaxes (antagonist)", "Both contract simultaneously with equal force", "Neither contracts; movement is driven purely by bone pressure"],
                "correct": 0,
                "solution": "During forearm flexion at the elbow, the biceps brachii acts as the agonist by contracting, while the opposing triceps brachii acts as the antagonist by relaxing."
            },
            {
                "q": "5. What is the clinical distinction between a 'sprain' and a 'strain'?",
                "options": ["A sprain is a bone fracture, while a strain is a skin cut", "A sprain is an injury to a joint ligament, while a strain is an injury/tear to a muscle or tendon", "A strain occurs only in the brain, while a sprain occurs in the heart", "There is no difference; they are identical terms"],
                "correct": 1,
                "solution": "A sprain involves overstretching or tearing of ligaments that stabilize bones at a joint; a strain involves damage, tearing, or overstretching of muscle fibres or tendons."
            },
            {
                "q": "6. In the R.I.C.E protocol for acute muscular or ligament injuries, what is the physiological purpose of applying Ice?",
                "options": ["To melt fat cells under the skin", "To cause local vasoconstriction of blood vessels, reducing internal bleeding, inflammation, and edema", "To increase blood flow to cause rapid swelling", "To permanently freeze nerve endings"],
                "correct": 1,
                "solution": "Cold cryotherapy induces vasoconstriction of local arterioles, drastically reducing capillary fluid leakage, internal bruising, and inflammatory swelling."
            },
            {
                "q": "7. Why is 'Elevation' recommended as part of the R.I.C.E treatment for an injured ankle?",
                "options": ["It increases atmospheric pressure on the toes", "It allows gravity to facilitate venous and lymphatic fluid drainage back toward the heart, reducing swelling", "It keeps the ankle warmer than the rest of the body", "It stretches the torn ligaments back into place"],
                "correct": 1,
                "solution": "Elevating the injured extremity above the level of the heart harnesses gravity to assist venous blood and lymphatic drainage away from the injury site, combating edema."
            },
            {
                "q": "8. Which dietary nutrient is essential for repairing microscopic tears in muscle fibres following strenuous exercise?",
                "options": ["Saturated fats", "Dietary protein (amino acids)", "Simple sugars", "Vitamin K alone"],
                "correct": 1,
                "solution": "Proteins are broken down into amino acids that cells use to synthesize new actin, myosin, and structural collagen, repairing micro-teared muscle fibres."
            },
            {
                "q": "9. Daily practice of yoga asanas such as Tadasana (Palm Tree pose) and Bhujangasana (Cobra pose) maintains health by:",
                "options": ["Strengthening postural core muscles and preserving natural spinal curvature", "Replacing bone calcium with liquid cartilage", "Eliminating all sensory neurons in the limbs", "Converting striated muscles into smooth muscles"],
                "correct": 0,
                "solution": "Tadasana and Bhujangasana elongate the vertebral column, engage deep transverse abdominal and erector spinae muscles, and maintain balanced spinal alignment."
            },
            {
                "q": "10. The pivot joint between the first vertebra (Atlas) and second vertebra (Axis) of the neck allows what movement?",
                "options": ["Complete 360-degree rotation of the head", "Rotational side-to-side turning ('No' movement) of the head", "Only backward hyperextension", "Zero movement because it is completely fused"],
                "correct": 1,
                "solution": "The atlantoaxial pivot joint features the odontoid process (dens) of the axis pivoting within a ring formed by the atlas, permitting side-to-side rotation of the head."
            }
        ]
    },

    # Slide 20: Dedicated Quiz Challenge 4 — Comprehensive Competency Master Quiz
    {
        "id": 20,
        "title": "Dedicated Quiz Challenge 4: Comprehensive Competency Master Quiz",
        "subtitle": "Synthesizing Plant & Animal Tissues, C-8.2 Experiment Data, and Indian Science History",
        "narration": "Congratulations on reaching the final Quiz Challenge! This master challenge evaluates your synthesis of botanical and zoological histology, experimental data analysis from root tip excision, and the milestone contributions of Indian scientists. Answer every question and examine the complete solutions.",
        "is_quiz": True,
        "quiz_title": "Comprehensive Competency Master Quiz (10 Questions)",
        "questions": [
            {
                "q": "1. In an onion root tip experiment, the daily length of roots in Jar 1 (intact) was 1.5 cm, 2.2 cm, 3.1 cm, 3.9 cm, 4.8 cm. In Jar 2, the tip was cut on Day 3 at 2.8 cm, and lengths on Days 4 and 5 were 2.8 cm and 2.8 cm. What scientific conclusion is supported?",
                "options": ["Roots grow faster after clipping", "Cell division causing root elongation is localized strictly at the root apical meristem", "Water in Jar 2 was toxic", "Onion bulbs cannot grow in water"],
                "correct": 1,
                "solution": "Jar 2's root length stagnated at 2.8 cm following tip excision on Day 3, proving conclusively that root elongation requires the mitotic activity of the terminal apical meristem."
            },
            {
                "q": "2. What landmark discovery in plant tissue culture was achieved in 1964 by Indian botanists Prof. Sipra Guha-Mukherjee and Prof. S.C. Maheshwari?",
                "options": ["Discovery that chlorophyll contains magnesium", "In vitro production of haploid plantlets from cultured Datura innoxia pollen grains", "Synthesis of artificial soil from plastic", "Cloning of the first mammalian organism"],
                "correct": 1,
                "solution": "At the University of Delhi, they discovered in vitro androgenesis by demonstrating that cultured pollen microspores of Datura innoxia could develop directly into haploid plantlets."
            },
            {
                "q": "3. The term 'cellular totipotency' demonstrated in plant tissue culture experiments refers to the capacity of:",
                "options": ["A cell to divide only twice before dying", "A single living plant cell to regenerate into an entire, complete multicellular plant", "A plant cell to survive without sunlight", "A plant root to absorb petroleum"],
                "correct": 1,
                "solution": "Totipotency is the inherent genetic potential of a single living plant cell to dedifferentiate, divide, and regenerate into a complete, fertile multicellular organism."
            },
            {
                "q": "4. Match the tissue with its correct defining characteristic: (A) Xylem Vessels, (B) Collenchyma, (C) Sclerenchyma, (D) Phloem Sieve Tubes.",
                "options": [
                    "(A) Dead with open ends; (B) Living with corner thickenings; (C) Dead with lignified walls; (D) Living with perforated plates",
                    "(A) Living with perforated plates; (B) Dead with lignified walls; (C) Living with corner thickenings; (D) Dead with open ends",
                    "(A) Living ground tissue; (B) Fluid tissue; (C) Dense matrix; (D) Contractile fibre",
                    "(A) Dead with corner thickenings; (B) Dead with open ends; (C) Living with sieve plates; (D) Dead with lignified walls"
                ],
                "correct": 0,
                "solution": "Xylem vessels are dead conducting pipes with open ends; collenchyma cells are living with corner thickenings; sclerenchyma cells are dead with lignified walls; sieve tubes are living with perforated sieve plates."
            },
            {
                "q": "5. Which cellular organelle is conspicuously absent or negligible in actively dividing meristematic cells?",
                "options": ["Nucleus", "Large central vacuole", "Mitochondria", "Ribosomes"],
                "correct": 1,
                "solution": "Meristematic cells have dense cytoplasm and prominent nuclei but lack large vacuoles because they do not store sap or waste and divide continuously."
            },
            {
                "q": "6. A patient suffers a sports injury where a bone in the ankle becomes abnormally loose and unstable without muscle damage. Which tissue was most likely torn?",
                "options": ["Tendon", "Ligament", "Areolar tissue", "Adipose tissue"],
                "correct": 1,
                "solution": "Ligaments connect bone to bone at joints; a torn ligament compromises joint stability, resulting in pathological bone looseness or dislocation."
            },
            {
                "q": "7. What anatomical property allows cardiac muscle to function without fatigue throughout a person's entire lifetime?",
                "options": ["Abundant mitochondria, rich capillary blood supply, and continuous oxidative aerobic metabolism", "Lack of all contractile proteins", "Reliance exclusively on dead lignified cells", "Having no cell membranes"],
                "correct": 0,
                "solution": "Cardiac muscle cells possess an extraordinarily high density of mitochondria (occupying ~40% of cell volume) and a rich coronary blood supply, relying purely on aerobic ATP production without lactic acid accumulation."
            },
            {
                "q": "8. Which of the following statements about plant complex tissues is FALSE?",
                "options": [
                    "Xylem transports water and minerals unidirectionally upward",
                    "Phloem transports food solutes bidirectionally",
                    "Xylem parenchyma is the only living cell in mature xylem",
                    "Phloem companion cells are dead cells lacking a nucleus"
                ],
                "correct": 3,
                "solution": "The statement is FALSE because companion cells are specialized LIVING parenchymatous cells with a prominent nucleus and dense cytoplasm that metabolically regulate sieve tubes."
            },
            {
                "q": "9. In human anatomy, which type of cartilage covers the articulating ends of long bones to reduce friction during movement?",
                "options": ["Elastic cartilage of ear", "Hyaline articular cartilage", "Calcified bone marrow", "Fibrous suture tissue"],
                "correct": 1,
                "solution": "Hyaline articular cartilage covers bone ends at synovial joints, providing a glass-like, smooth, low-friction surface that absorbs compressive loads during movement."
            },
            {
                "q": "10. Why was the discovery of in vitro androgenesis by Guha-Mukherjee and Maheshwari particularly celebrated in crop breeding?",
                "options": [
                    "It allowed farmers to plant seeds without watering",
                    "Chromosome doubling of the resulting haploid plants produces completely homozygous pure lines in a single generation, saving 6–8 years of conventional inbreeding",
                    "It made plants resistant to gravity",
                    "It prevented plants from ever forming flowers"
                ],
                "correct": 1,
                "solution": "Conventional breeding takes 6–8 generations of self-pollination to achieve homozygous pure lines. Anther culture produces haploids that yield 100% homozygous lines in one generation upon doubling."
            }
        ]
    }
]


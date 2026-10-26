# -*- coding: utf-8 -*-
"""
Data module for Class 9 Science Chapter 1 (Biology): The Fundamental Unit of Life (Cell)
Syllabus Competencies: C-3.1, C-3.2, C-3.3, C-4.2, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

SLIDES = [
    {
        "id": 1,
        "title": "Discovery of the Cell & The Classical Cell Theory",
        "subtitle": "From Robert Hooke's 1665 Cork 'Cellulae' to Virchow's Principle of Biogenesis",
        "category": "Historical Foundations",
        "badge": "C-7.1 • Cell as Unit of Life",
        "summary": "The cell is the basic structural, functional, and biological unit of all living organisms. The discovery and understanding of cells progressed alongside advances in optical lenses: (1) Robert Hooke (1665): Observed thin slices of dead Spanish oak tree cork under a primitive self-designed microscope. He noticed honeycomb-like porous compartments and coined the term 'cell' (Latin 'cellula' meaning a small room); (2) Anton van Leeuwenhoek (1674): Using improved high-magnification ground lenses, discovered free-living living cells (bacteria, spirogyra protozoa, and red blood cells) in pond water; (3) Robert Brown (1831): Discovered and named the 'nucleus' as a spherical central body inside plant cells; (4) J.E. Purkinje (1839): Coined the term 'protoplasm' for the living, fluid, jelly-like substance enclosed within the cell; (5) The Cell Theory was formulated by German botanist Matthias Schleiden (1838) and zoologist Theodor Schwann (1839): 'All plants and animals are composed of cells, and the cell is the fundamental unit of life'; (6) Rudolf Virchow (1855): Expanded the theory with the celebrated Latin aphorism 'Omnis cellula-e cellula' — all cells arise exclusively from pre-existing living cells through cell division, disproving spontaneous generation.",
        "key_points": [
            "Robert Hooke (1665): Discovered dead cork cells ('cellulae') using a primitive compound microscope.",
            "Leeuwenhoek (1674): First to observe living, mobile microscopic organisms in pond water.",
            "Brown (1831) & Purkinje (1839): Brown discovered the nucleus; Purkinje coined 'protoplasm' for living cell matter.",
            "Schleiden & Schwann (1838-39): Formulated the foundational Cell Theory (all organisms are made of cells).",
            "Virchow (1855): Added 'Omnis cellula-e cellula' (all living cells arise from pre-existing cells)."
        ],
        "narration": "Welcome to the Fundamental Unit of Life: the Cell! In 1665, an English scientist named Robert Hooke sliced a thin piece of tree cork and placed it under his microscope. He saw tiny honeycomb boxes and called them cells, from the Latin word for little rooms! Nine years later, Anton van Leeuwenhoek discovered the first living, swimming microbes in pond water. Later, Schleiden and Schwann realized that every living plant and animal on Earth is built from cells, and Rudolf Virchow proved that all cells come from pre-existing living cells! Explore our interactive microscope timeline to see Hooke's dead cork honeycomb turn into living pond microbes.",
        "sim_title": "Interactive Microscope Timeline & Cork-to-Living Cell Explorer",
        "checkpoints": [
            {
                "q": "Who was the first scientist to observe free-living cells in pond water with an improved microscope?",
                "options": ["Robert Hooke", "Anton van Leeuwenhoek", "Robert Brown", "Rudolf Virchow"],
                "ans": 1,
                "exp": "Anton van Leeuwenhoek (1674) was the first to observe free-living cells (such as bacteria and protozoa) in pond water. Robert Hooke observed non-living cork cell walls in 1665."
            },
            {
                "q": "The Latin phrase 'Omnis cellula-e cellula', stating that all cells arise from pre-existing cells, was proposed by:",
                "options": ["Theodor Schwann", "Matthias Schleiden", "Rudolf Virchow", "J.E. Purkinje"],
                "ans": 2,
                "exp": "Rudolf Virchow in 1855 expanded the Cell Theory by proposing that all living cells arise exclusively from pre-existing cells through division."
            }
        ]
    },
    {
        "id": 2,
        "title": "Prokaryotic vs Eukaryotic Cells: Structural Architectures",
        "subtitle": "Primitive Nucleoids vs Membrane-Bound Organelle Compartmentalization",
        "category": "Cellular Classification",
        "badge": "C-3.1 • Prokaryotes vs Eukaryotes",
        "summary": "Living cells are divided into two fundamental architectural domains: (1) Prokaryotic Cells (Greek 'pro' = primitive/before, 'karyon' = nucleus): Ancient, simple cells represented by bacteria and blue-green cyanobacteria. Typically microscopic in size (1 to 10 µm). They lack a true nuclear membrane; their genetic material is an uncoiled, circular loop of naked DNA located in an undefined central region called the 'nucleoid'. They possess a single circular chromosome, 70S ribosomes, and completely lack membrane-bound organelles (mitochondria, endoplasmic reticulum, chloroplasts, Golgi apparatus). Cell division occurs rapidly via simple binary fission; (2) Eukaryotic Cells (Greek 'eu' = true, 'karyon' = nucleus): Evolutionarily advanced cells forming fungi, protists, plants, and animals. Typically larger (5 to 100 µm). They possess a distinct, well-defined nucleus enclosed by a double-layered nuclear envelope with nuclear pores, multiple complex linear chromosomes with histone proteins, 80S ribosomes, and compartmentalized membrane-bound organelles performing specialized biochemical functions.",
        "key_points": [
            "Size Comparison: Prokaryotes are small (1–10 µm); eukaryotes are significantly larger (5–100 µm).",
            "Nuclear Organization: Prokaryotes have an undefined 'nucleoid' lacking a membrane; eukaryotes possess a true double-membrane nucleus.",
            "Chromosomes: Single circular DNA in prokaryotes; multiple linear chromosomes with histones in eukaryotes.",
            "Organelles: Membrane-bound organelles (mitochondria, ER, plastids, Golgi) are absent in prokaryotes and present in eukaryotes.",
            "Ribosome Differences: Prokaryotes possess 70S ribosomes; eukaryotic cytoplasm contains 80S ribosomes."
        ],
        "narration": "Look across all life on Earth and you will find two grand architectural blueprints: Prokaryotes and Eukaryotes! Bacteria are prokaryotes—primitive cells without a true nucleus. Their single loop of DNA floats freely in a region called the nucleoid, and they have no membrane-bound organelles. In contrast, you, trees, and mushrooms are eukaryotes! Our cells have a true nucleus guarded by a double membrane, and our cytoplasm is packed with specialized organelles like mitochondria and Golgi bodies. Compare both cell blueprints in our interactive dual-cell simulator!",
        "sim_title": "Interactive Dual-Cell Architect: Prokaryote vs Eukaryote",
        "checkpoints": [
            {
                "q": "The undefined, membrane-less nuclear region containing only nucleic acid in a bacterial cell is known as the:",
                "options": ["Nucleolus", "Nucleoid", "Nucleosome", "Centrosome"],
                "ans": 1,
                "exp": "In prokaryotic cells like bacteria, the nuclear region is not enclosed by a nuclear membrane and is termed the 'nucleoid'."
            },
            {
                "q": "Which of the following cellular structures is present in BOTH prokaryotic and eukaryotic cells?",
                "options": ["Mitochondria", "Endoplasmic Reticulum", "Ribosomes", "Nuclear Envelope"],
                "ans": 2,
                "exp": "Ribosomes are non-membrane-bound molecular machines for protein synthesis found in both prokaryotes (70S) and eukaryotes (80S). Mitochondria, ER, and nuclear envelopes exist only in eukaryotes."
            }
        ]
    },
    {
        "id": 3,
        "title": "Plant vs Animal Cells: Compartmentalization & Specialization",
        "subtitle": "Cell Walls, Chloroplasts, Vacuolar Turgidity, and Centrioles",
        "category": "Cellular Classification",
        "badge": "C-3.1 • Plant vs Animal Cells",
        "summary": "Although both plant and animal cells are eukaryotic and share fundamental organelles (nucleus, mitochondria, endoplasmic reticulum, Golgi body, ribosomes), they exhibit distinct structural adaptations suited to their ecological lifestyles: (1) Plant Cells: Surrounded by a rigid outer non-living Cell Wall made of cellulose located outside the plasma membrane, providing mechanical strength and preventing lysis in hypotonic water. They contain Plastids (notably green Chloroplasts for photosynthesis). Mature plant cells feature a gigantic, permanent central Vacuole that occupies 50% to 90% of total cell volume, filled with cell sap that exerts internal turgor pressure to keep the plant erect. Centrosomes and centrioles are absent; (2) Animal Cells: Lack a cell wall and plastids, possessing only a flexible, living plasma membrane that allows shape changes, locomotion, and endocytosis. They contain numerous small, temporary vacuoles. They possess Centrosomes with paired Centrioles that organize spindle fibers during mitotic cell division.",
        "key_points": [
            "Outer Boundaries: Plant cells have a rigid cellulose cell wall outside the plasma membrane; animal cells have only a plasma membrane.",
            "Plastids / Chloroplasts: Present in green plant cells for photosynthetic glucose synthesis; completely absent in animal cells.",
            "Vacuolar Structure: Plant cells feature a single massive central sap vacuole (50–90% volume); animal cells have small, transient vacuoles.",
            "Centrioles / Centrosomes: Present in animal cells to guide chromosome separation during mitosis; absent in higher plant cells.",
            "Shape & Plasticity: Plant cells maintain fixed, rigid, polygonal shapes; animal cells are pliable and irregular."
        ],
        "narration": "Why don't trees need a skeleton like humans do? Because every single plant cell wears its own armor: a tough, rigid cell wall made of cellulose! Inside, a massive central vacuole fills up with fluid sap, creating internal turgor pressure that keeps stems and leaves standing tall. Plant cells also possess green chloroplasts—the solar factories of our planet. Animal cells, on the other hand, have no cell walls and no chloroplasts. Instead, they have flexible membranes for movement and centrioles for cell division. Dissect and compare both cells in our 3D interactive laboratory!",
        "sim_title": "Interactive Plant vs Animal Cell Dissection Laboratory",
        "checkpoints": [
            {
                "q": "Which of the following organelles is exclusively present in plant cells and absent in animal cells?",
                "options": ["Mitochondria", "Chloroplasts", "Golgi Apparatus", "Ribosomes"],
                "ans": 1,
                "exp": "Chloroplasts (and other plastids) are exclusive to plant cells (and algae) for photosynthesis. Mitochondria, Golgi apparatus, and ribosomes are present in both."
            },
            {
                "q": "What accounts for the mechanical rigidity and structural uprightness of non-woody plant stems in the absence of bones?",
                "options": [
                    "High cholesterol content in animal membranes",
                    "Cellulose cell wall combined with internal vacuolar turgor pressure",
                    "Presence of multiple centrioles",
                    "Dense mitochondrial cristae"
                ],
                "ans": 1,
                "exp": "The rigid cellulose cell wall combined with the high turgor pressure exerted by the large central sap vacuole provides structural firmness to herbaceous plants."
            }
        ]
    },
    {
        "id": 4,
        "title": "The Plasma Membrane: Fluid Mosaic Model & Selective Permeability",
        "subtitle": "The Phospholipid Bilayer, Embedded Protein Channels, and Endocytosis",
        "category": "Membrane Dynamics",
        "badge": "C-4.2 • Biomolecules & Membrane",
        "summary": "The Plasma Membrane (or cell membrane) is the living, flexible, ultra-thin outer boundary enclosing the cytoplasm of all cells. In 1972, S.J. Singer and G.L. Nicolson proposed the celebrated Fluid Mosaic Model to explain its dynamic architecture: (1) Phospholipid Bilayer: Composed of two back-to-back layers of amphipathic phospholipids. Each molecule features a polar hydrophilic (water-loving) phosphate head facing external and internal aqueous fluids, and two non-polar hydrophobic (water-repelling) fatty acid tails hidden in the oily interior; (2) Membrane Proteins: Embedded within the bilayer like icebergs floating in a lipid sea. Integral (intrinsic) proteins form transmembrane transport channels and pumps, while peripheral (extrinsic) proteins serve as receptor sites and enzymes; (3) Selective Permeability: The membrane regulates the traffic of materials—freely permitting small non-polar molecules (O₂, CO₂) and water, while restricting large polar solutes (glucose, ions) without specific transport proteins; (4) Membrane Flexibility & Endocytosis: The flexible lipid bilayer allows unicellular organisms like Amoeba to engulf food particles from the external environment via pseudopodia (endocytosis/phagocytosis).",
        "key_points": [
            "Fluid Mosaic Model (Singer & Nicolson, 1972): Phospholipid bilayer with floating mosaic of intrinsic and extrinsic proteins.",
            "Amphipathic Bilayer: Hydrophilic phosphate heads orient outward; hydrophobic fatty acid tails sequester inward.",
            "Selective Permeability: Selects which substances enter and exit, maintaining strict intracellular homeostasis.",
            "Endocytosis: Membrane flexibility enables Amoeba to engulf external food particles by forming food vacuoles.",
            "Biomolecule Composition: Built primarily of lipids (phospholipids, cholesterol) and functional structural proteins."
        ],
        "narration": "Every cell is an active biochemical fortress, and the plasma membrane is its border security! Singer and Nicolson described it as the Fluid Mosaic Model—think of a sea of fluid lipid molecules with protein icebergs floating inside it. The outer heads love water, while the inner fatty tails repel water. Because it is selectively permeable, it lets oxygen and water slip through, but blocks harmful toxins. Its incredible flexibility even lets an Amoeba stretch out its membrane into pseudopodia to swallow food! Test different molecules entering the cell in our interactive membrane gatekeeper simulator.",
        "sim_title": "Interactive Fluid Mosaic Membrane & Molecular Gatekeeper",
        "checkpoints": [
            {
                "q": "The process by which an Amoeba engulfs external food particles by virtue of its flexible plasma membrane is called:",
                "options": ["Plasmolysis", "Endocytosis", "Exosmosis", "Cellular Respiration"],
                "ans": 1,
                "exp": "The flexibility of the plasma membrane enables unicellular organisms like Amoeba to engulf food and other materials from their external environment, a process known as endocytosis (or phagocytosis)."
            },
            {
                "q": "According to the Fluid Mosaic Model of Singer and Nicolson, the plasma membrane is primarily composed of:",
                "options": ["Cellulose and pectin", "Lipid bilayer with embedded proteins", "Chitin and peptidoglycan", "Lignin and glycogen"],
                "ans": 1,
                "exp": "The plasma membrane is chemically composed of a phospholipid bilayer with embedded (intrinsic) and surface (extrinsic) proteins."
            }
        ]
    },
    {
        "id": 5,
        "title": "Cell Wall & Turgor Pressure: Plant Resilience in Hypotonic Media",
        "subtitle": "Cellulose Tensile Architecture, Counter-Wall Pressure, and Lysis Prevention",
        "category": "Membrane Dynamics",
        "badge": "C-3.1 • Cell Wall Physiology",
        "summary": "Plant cells, fungi, and bacteria possess an additional non-living, rigid protective outer envelope called the Cell Wall, situated entirely outside the plasma membrane. Plant cell walls are composed of cellulose, a complex structural polysaccharide carbohydrate that imparts tremendous tensile strength: (1) Free Permeability: Unlike the selectively permeable plasma membrane, the cell wall is completely permeable, allowing water, mineral solutes, and gases to pass through without barrier; (2) Mechanical Protection & Osmotic Buffering: When a plant cell is placed in a dilute hypotonic environment (such as rainwater), water enters the cell via endosmosis. The expanding central vacuole swells the protoplast against the cell wall, generating high internal Turgor Pressure; (3) Wall Pressure Invariant: Because of its rigid cellulose fibers, the cell wall exerts an equal and opposite Wall Pressure back against the swollen cell contents. This prevents the plant cell from bursting (lysing); (4) Comparison with Animal Cells: Animal cells lack a cell wall; when placed in pure water, animal cells swell until their plasma membrane ruptures (osmotic lysis).",
        "key_points": [
            "Cellulose Composition: Tough fibrous carbohydrate providing immense tensile strength to plant cell walls.",
            "Permeability Difference: The cell wall is freely permeable; the inner plasma membrane is selectively permeable.",
            "Turgor Pressure Generation: Water influx expands the vacuole, pressing cytoplasm against the rigid wall.",
            "Resistance to Bursting: Wall pressure balances turgor pressure, allowing plant cells to endure hypotonic media safely.",
            "Fungal & Bacterial Walls: Fungi have cell walls made of chitin; bacteria have walls made of peptidoglycan."
        ],
        "narration": "What happens when you drop a living cell into pure distilled water? If it is a human red blood cell, water rushes in until it violently pops and bursts like an over-inflated balloon! But a plant cell never bursts. Why? Because of its rigid cellulose cell wall! As water rushes into the plant cell, the swelling vacuole pushes outward with turgor pressure. The tough cell wall pushes right back with equal force! This mechanical harmony allows trees to drink gallons of rainwater without a single cell bursting. Watch this contrast live in our osmotic rupture simulator!",
        "sim_title": "Plant Cell Turgor vs Animal RBC Osmotic Rupture Simulator",
        "checkpoints": [
            {
                "q": "Why do plant cells withstand much greater changes in the surrounding hypotonic medium than animal cells without bursting?",
                "options": [
                    "Plant cells have thicker plasma membranes",
                    "Plant cells possess a rigid cellulose cell wall that exerts counter-wall pressure",
                    "Plant cells do not absorb water",
                    "Plant cells have mitochondria that pump water out"
                ],
                "ans": 1,
                "exp": "Plant cells are surrounded by a rigid cellulose cell wall. When endosmosis creates internal turgor pressure, the wall exerts equal counter-wall pressure, preventing osmotic lysis."
            },
            {
                "q": "Plant cell walls are primarily synthesized from which complex structural biomolecule?",
                "options": ["Glycogen", "Phospholipids", "Cellulose", "Peptidoglycan"],
                "ans": 2,
                "exp": "Plant cell walls are made of cellulose, a complex carbohydrate polymer that provides mechanical and structural strength."
            }
        ]
    },
    {
        "id": 6,
        "title": "Transport Across Membranes: Diffusion vs Osmosis",
        "subtitle": "Passive Molecular Dispersion Down Chemical and Osmotic Gradients",
        "category": "Membrane Dynamics",
        "badge": "C-3.2 • Diffusion vs Osmosis",
        "summary": "Molecules constantly move across biological boundaries to maintain cellular metabolism through two passive transport mechanisms: (1) Diffusion: The spontaneous net physical movement of molecules (solutes, gases, liquids) from a region of higher concentration to a region of lower concentration down a concentration gradient until uniform distribution is achieved. Diffusion does NOT require a selectively permeable membrane or metabolic energy (ATP). Essential biological role: Gaseous exchange in cellular respiration. Carbon dioxide (CO₂) produced during cellular respiration accumulates inside the cell ([CO₂]_in > [CO₂]_out) and diffuses out into the blood; oxygen (O₂) in blood capillaries ([O₂]_out > [O₂]_in) diffuses into the oxygen-hungry cell; (2) Osmosis: A specialized sub-type of diffusion restricted exclusively to solvent molecules. Osmosis is the passage of water from a region of higher water concentration (dilute solution) through a selectively permeable membrane to a region of lower water concentration (concentrated solution); (3) Fundamental Distinctions: Diffusion involves any substance across any medium; osmosis strictly involves water solvent moving across a selectively permeable membrane.",
        "key_points": [
            "Diffusion Definition: Spontaneous movement of any substance from higher to lower concentration down its gradient.",
            "Respiratory Gaseous Exchange: CO₂ diffuses out of cells, while O₂ diffuses in down their respective partial pressure gradients.",
            "Osmosis Definition: Movement of water molecules from a dilute solution to a concentrated solution across a semipermeable membrane.",
            "Membrane Requirement: Diffusion does not require a membrane; osmosis strictly requires a selectively permeable membrane.",
            "Passive Transport: Both diffusion and osmosis occur spontaneously without the expenditure of cellular metabolic energy (ATP)."
        ],
        "narration": "Inside your body right now, trillions of molecules are on the move! When you smell perfume sprayed across a room, that is Diffusion: particles spreading from high concentration to low concentration. Your cells use diffusion to breathe—carbon dioxide diffuses out into your blood, while fresh oxygen diffuses in. But when water moves across a selectively permeable cell membrane, we call that Osmosis! Remember this rule: water always flows from where water is abundant to where water is scarce. Explore both processes in our dual-chamber transport simulator!",
        "sim_title": "Interactive Diffusion vs Osmosis Chamber & Dynamic Equilibrium Studio",
        "checkpoints": [
            {
                "q": "Which of the following statements correctly differentiates osmosis from simple diffusion?",
                "options": [
                    "Diffusion requires ATP, whereas osmosis is passive",
                    "Diffusion applies to gases and solutes, whereas osmosis specifically involves water moving across a selectively permeable membrane",
                    "Osmosis occurs from low water concentration to high water concentration",
                    "Diffusion can only occur in living cells"
                ],
                "ans": 1,
                "exp": "Diffusion is the general movement of any substance down its concentration gradient without needing a membrane, whereas osmosis is specifically the diffusion of water across a selectively permeable membrane."
            },
            {
                "q": "During cellular respiration in animal tissues, carbon dioxide (CO₂) moves out of the cell because:",
                "options": [
                    "The concentration of CO₂ inside the cell is lower than outside",
                    "The concentration of CO₂ inside the cell is higher than outside, driving outward diffusion",
                    "Active transport pumps CO₂ out using ATP",
                    "Osmotic pressure pushes CO₂ through water channels"
                ],
                "ans": 1,
                "exp": "Cellular respiration produces CO₂, causing its intracellular concentration to rise above that of the extracellular blood environment. CO₂ moves out down its concentration gradient by passive diffusion."
            }
        ]
    },
    {
        "id": 7,
        "title": "The Three Osmotic Environments & Plasmolysis",
        "subtitle": "Hypotonic Swelling, Isotonic Equilibrium, and Hypertonic Protoplast Shrinkage",
        "category": "Membrane Dynamics",
        "badge": "C-8.2 • Osmosis & Plasmolysis",
        "summary": "When living cells are immersed in external aqueous solutions, net water movement depends on the relative concentration of water versus solute: (1) Hypotonic Solution (Dilute medium, higher water concentration outside): Water enters the cell via endosmosis. Animal cells swell and burst; plant cells swell, become turgid, and push firmly against the cell wall; (2) Isotonic Solution (Identical water and solute concentration): Net water movement is zero (dynamic equilibrium; rate of water entering equals rate of water leaving). The cell retains its exact size and volume; (3) Hypertonic Solution (Concentrated medium, lower water concentration outside): Water exits the cell via exosmosis into the surrounding brine or sugar syrup. Animal cells shrivel and crenate; (4) Plasmolysis in Plant Cells: When a living plant cell (e.g., Rheo or Tradescantia leaf peel) is placed in a concentrated hypertonic sugar or salt solution, water leaves the vacuole via exosmosis. As the vacuole loses water, the living protoplast (plasma membrane + cytoplasm) contracts and shrinks away from the rigid cellulose cell wall, leaving a clear gap between wall and membrane. Placing the plasmolysed cell back into pure water causes water re-entry and de-plasmolysis.",
        "key_points": [
            "Hypotonic Medium: External water concentration is higher; endosmosis causes swelling and plant cell turgidity.",
            "Isotonic Medium: Equal water concentration across boundary; zero net movement; cell volume is conserved.",
            "Hypertonic Medium: External water concentration is lower; exosmosis causes water loss and cellular shrinkage.",
            "Plasmolysis Phenomenon: Contraction of living plant protoplast away from the cell wall in a hypertonic solution.",
            "Reversibility: De-plasmolysis restores cell turgor when plasmolysed cells are returned to pure water."
        ],
        "narration": "Have you ever wondered why pickles are preserved in heavy salt or jams in thick sugar? Because bacteria that touch them lose all their water and shrivel up! When a plant cell sits in concentrated salt water—a hypertonic solution—water rushes out of its vacuole. The living protoplast shrinks and pulls away from the cell wall like a deflating balloon inside a cardboard box. This dramatic shrinkage is called Plasmolysis! But put that cell back into pure water, and it plumps back up in de-plasmolysis. Adjust solution tonicity in our virtual beaker and observe plasmolysis in action!",
        "sim_title": "Interactive Rheo Leaf Plasmolysis & Osmotic Tonicity Studio",
        "checkpoints": [
            {
                "q": "When a living plant cell loses water through exosmosis in a hypertonic solution and its protoplast shrinks away from the cell wall, the phenomenon is called:",
                "options": ["De-plasmolysis", "Plasmolysis", "Endosmosis", "Cytolysis"],
                "ans": 1,
                "exp": "Plasmolysis is the shrinkage or contraction of the contents of the plant cell (the living protoplast) away from the cell wall under hypertonic conditions."
            },
            {
                "q": "What happens when dried raisins or apricots are soaked in plain water for several hours?",
                "options": [
                    "They shrink due to exosmosis",
                    "They remain unchanged because they are dead",
                    "They swell due to endosmosis as water enters from the hypotonic medium",
                    "They undergo plasmolysis"
                ],
                "ans": 2,
                "exp": "The sugar concentration inside dried raisins is much higher than in plain water (hypotonic medium). Water enters the raisins by endosmosis, causing them to swell."
            }
        ]
    },
    {
        "id": 8,
        "title": "Hands-On Microscopy: Slide Preparation of Onion Peel & Human Cheek Cells",
        "subtitle": "Microtechniques: Epidermal Peeling, Staining (Safranin/Methylene Blue) & Coverslip Mounting",
        "category": "Laboratory Skills",
        "badge": "C-3.1 • Slide Preparation",
        "summary": "Observing cell architecture requires mastering fundamental histology and temporary mount microtechniques: (1) Temporary Mount of Onion Peel (Plant Cells): (a) Strip a transparent, paper-thin epidermal layer from the concave surface of an onion bulb fleshy scale leaf; (b) Transfer immediately to water in a watch glass to prevent desiccation; (c) Stain with dilute Safranin stain for 1–2 minutes (Safranin stains lignified and cellulosic cell walls and nuclei pinkish-red); (d) Transfer peel onto a clean glass slide with a drop of glycerine (glycerine acts as a clearing agent and prevents the specimen from drying out); (e) Coverslip Placement: Hold the coverslip at a 45° angle with a mounting needle and gently lower it to prevent trapped air bubbles; (f) Microscopic Observation: Interlocking rectangular cells with distinct cell walls, thin peripheral cytoplasm, large central vacuole, and distinct dark nuclei; (2) Temporary Mount of Human Cheek Cells (Animal Cells): (i) Gently scrape the inner lining of the cheek with a clean toothpick; (ii) Smear scrapings onto a slide, add a drop of Methylene Blue stain (stains animal nuclei deep blue); (iii) Mount under a coverslip; (iv) Observation: Thin, flat, irregular polygonal cells without cell walls, containing granular cytoplasm and centrally positioned nuclei.",
        "key_points": [
            "Onion Peel Technique: Concave epidermal peel stained with Safranin to observe rectangular plant cells with walls.",
            "Cheek Epithelial Technique: Inner mucosal scrapings stained with Methylene Blue to observe wall-less animal cells.",
            "Role of Glycerine: Keeps the mounted tissue hydrated and acts as an optical clearing medium.",
            "45° Coverslip Angle: Essential microtechnique to prevent formation of spherical air bubbles that distort vision.",
            "Staining Rationale: Different cellular components absorb specific stains (nuclei absorb basic stains intensely)."
        ],
        "narration": "Let's step into the biology laboratory! To observe plant cells, we peel a paper-thin skin from an onion scale leaf and stain it with safranin. Under the microscope, you will see neat rows of brick-like cells, each with a distinct cell wall and a dark nucleus. To see animal cells, we gently scrape the inside of our cheek and stain it with methylene blue. Look closely: animal cells have no cell walls—they are irregular, rounded, and soft! Notice our golden laboratory rule: always lower the coverslip at a forty-five-degree angle using a needle to avoid trapping air bubbles. Practice slide mounting in our virtual laboratory!",
        "sim_title": "Virtual Slide Preparation & Coverslip Air-Bubble Simulator",
        "checkpoints": [
            {
                "q": "Why is glycerine added to the biological specimen during the preparation of a temporary slide mount?",
                "options": [
                    "To kill any living bacteria",
                    "To prevent the specimen from drying out and improve optical clarity",
                    "To dissolve the cell wall",
                    "To stain the mitochondria green"
                ],
                "ans": 1,
                "exp": "Glycerine keeps the mounted tissue moist, preventing shrinkage due to desiccation, and matches the refractive index for clear optical microscopy."
            },
            {
                "q": "When viewing an onion peel mount under a compound microscope, which structural feature clearly proves these are plant cells?",
                "options": [
                    "Presence of multiple small vacuoles",
                    "Presence of a distinct outer cell wall bounding each rectangular cell",
                    "Presence of centrioles next to the nucleus",
                    "Absence of a nucleus"
                ],
                "ans": 1,
                "exp": "The presence of a rigid, rectangular outer cell wall surrounding the plasma membrane confirms that onion epidermal cells are plant cells."
            }
        ]
    },
    {
        "id": 9,
        "title": "The Nucleus: Director of the Cell & Chromosome Architecture",
        "subtitle": "The Nuclear Envelope, Pores, Nucleolus, Chromatin, and Genomic DNA",
        "category": "Organelles",
        "badge": "C-3.1 • Nuclear Architecture",
        "summary": "The Nucleus is the largest, most prominent organelle, serving as the master control center and genetic library of eukaryotic cells: (1) Nuclear Envelope: A double-membrane barrier enclosing the nuclear contents. It is perforated by thousands of Nuclear Pores that regulate the bidirectional exchange of macromolecules (RNA, ribosomal subunits, proteins) between the nucleoplasm and cytoplasm; (2) Nucleoplasm & Nucleolus: The nucleoplasm is the dense fluid matrix of the nucleus. Inside lies the Nucleolus (one or more dense non-membrane bodies), which acts as the factory synthesizing ribosomal RNA (rRNA) and assembling ribosome subunits; (3) Chromatin Material: In a non-dividing cell, the genetic material exists as an entangled, diffuse fibrous network called Chromatin. Chemically, chromatin consists of Deoxyribonucleic Acid (DNA) wound around basic histone proteins; (4) Chromosomes & Genes: When a cell prepares to divide, chromatin fibers condense into distinct rod-like bodies called Chromosomes. Functional segments of DNA that carry genetic instructions for heredity and protein synthesis are called Genes; (5) Master Functions: Controls cellular metabolism, growth, differentiation, and directs cellular reproduction (mitosis/meiosis).",
        "key_points": [
            "Master Control Center: Regulates all metabolic, enzymatic, and biochemical operations of the cell.",
            "Nuclear Envelope & Pores: Double membrane with pores controlling nucleo-cytoplasmic molecular transport.",
            "Nucleolus: Dense intranuclear site dedicated to the transcription of rRNA and ribosome assembly.",
            "Chromatin to Chromosomes: Diffuse chromatin coils and condenses into rod-shaped chromosomes during division.",
            "Genes as Functional Units: Functional coding segments of genomic DNA molecules that carry hereditary traits."
        ],
        "narration": "If the cell is a bustling city, the Nucleus is City Hall! It is wrapped in a double membrane with tiny gateways called nuclear pores. Inside lies your complete genetic blueprint: DNA! When a cell is resting, the DNA looks like a tangled bowl of spaghetti called chromatin. But when the cell gets ready to divide, this chromatin neatly coils up into tight, X-shaped packages called Chromosomes. Functional instructions along the DNA are called Genes—they determine your eye color, height, and blood type! Zoom into the nucleus and watch chromatin condense into chromosomes in our interactive simulator.",
        "sim_title": "Interactive Nucleus & Chromatin-to-Chromosome Condensation Engine",
        "checkpoints": [
            {
                "q": "The functional informational segments of DNA that carry hereditary instructions from parents to offspring are called:",
                "options": ["Histones", "Chromatids", "Genes", "Nucleoli"],
                "ans": 2,
                "exp": "Genes are the functional, protein-coding segments of DNA molecules responsible for hereditary transmission of biological characteristics."
            },
            {
                "q": "What is the primary function of the nucleolus found within the nucleus?",
                "options": [
                    "ATP synthesis through oxidative phosphorylation",
                    "Synthesis of ribosomal RNA (rRNA) and assembly of ribosomes",
                    "Digestion of cellular waste",
                    "Lipid detoxification"
                ],
                "ans": 1,
                "exp": "The nucleolus is the specialized non-membrane sub-compartment of the nucleus responsible for transcribing ribosomal RNA and assembling ribosome subunits."
            }
        ]
    },
    {
        "id": 10,
        "title": "Mitochondria: Cellular Powerhouse & ATP Synthesis",
        "subtitle": "Double Membrane Architecture, Folded Cristae, Semi-Autonomy, and the Energy Currency ATP",
        "category": "Organelles",
        "badge": "C-3.1 • Powerhouse Mitochondria",
        "summary": "Mitochondria (singular: mitochondrion) are the 'powerhouses of the cell', responsible for generating the chemical energy required for cellular life processes through aerobic respiration: (1) Double Membrane Architecture: (a) Outer Membrane: Smooth, porous, containing transport proteins (porins) that permit metabolite entry; (b) Inner Membrane: Selectively permeable and thrown into deep, finger-like convolutions called Cristae. These cristae folds dramatically expand the surface area for the electron transport chain and ATP-synthase complexes; (c) Intermembrane space and internal Matrix (containing Krebs cycle enzymes); (2) ATP Generation: Mitochondria oxidize carbohydrates and fatty acids to synthesize Adenosine Triphosphate (ATP). ATP is the universal 'energy currency' of living cells; hydrolysis of its terminal phosphate releases energy to drive muscle contraction, protein synthesis, nerve impulse transmission, and active transport; (3) Semi-Autonomous Nature: Mitochondria possess their own circular DNA (mtDNA) and 70S ribosomes. Consequently, they can synthesize some of their own proteins and replicate independently by fission, supporting the Endosymbiotic Theory.",
        "key_points": [
            "Powerhouse of the Cell: Sites of aerobic cellular respiration generating ATP from food substrates.",
            "Cristae Surface Amplification: Deep folds of the inner membrane provide vast surface area for ATP-generating enzymes.",
            "ATP as Energy Currency: Adenosine Triphosphate powers cellular mechanical, chemical, and transport work.",
            "Semi-Autonomous Organelle: Contains its own circular DNA and 70S ribosomes; replicates via binary fission.",
            "Metabolic Density: Cells with high energy demands (cardiac muscle, sperm tails, liver cells) contain thousands of mitochondria."
        ],
        "narration": "Meet the mighty power plant of your body: the Mitochondrion! Whenever you jump, run, or think, you are burning fuel made by these tiny organelles. Notice their incredible design: a smooth outer jacket and an inner membrane folded into deep fingers called Cristae. Why are they folded? To pack millions of microscopic ATP generators onto a huge surface area! Mitochondria generate ATP—Adenosine Triphosphate—the rechargeable energy currency of life. And here is an amazing evolutionary secret: mitochondria have their own circular DNA and ribosomes, proving they were once free-living bacteria that moved into our ancestor cells billions of years ago! Explore our 3D cutaway mitochondrion in the simulator.",
        "sim_title": "Interactive 3D Mitochondrion & Cristae ATP Generator",
        "checkpoints": [
            {
                "q": "Why is the inner mitochondrial membrane deeply folded into finger-like cristae?",
                "options": [
                    "To store extra glucose",
                    "To increase the surface area available for ATP-generating chemical reactions",
                    "To prevent oxygen from entering the matrix",
                    "To produce ribosomal subunits"
                ],
                "ans": 1,
                "exp": "The cristae folds dramatically expand the surface area of the inner membrane, accommodating millions of electron transport chain complexes and ATP synthase enzymes."
            },
            {
                "q": "Mitochondria are called semi-autonomous organelles because they possess their own:",
                "options": [
                    "Cell wall and chloroplasts",
                    "Circular DNA and ribosomes, enabling protein synthesis and replication",
                    "Endoplasmic reticulum and Golgi bodies",
                    "Nucleus and nucleolus"
                ],
                "ans": 1,
                "exp": "Mitochondria contain their own circular DNA and 70S ribosomes, allowing them to synthesize some of their own proteins and divide independently by fission."
            }
        ]
    },
    {
        "id": 11,
        "title": "Plastids & Chloroplasts: Photosynthetic Solar Converters",
        "subtitle": "Chloroplasts (Chlorophyll), Chromoplasts (Pigments), and Leucoplasts (Storage)",
        "category": "Organelles",
        "badge": "C-3.1 • Plastid Biology",
        "summary": "Plastids are major double-membrane-bound organelles found exclusively in plant cells and photosynthetic algae. Like mitochondria, plastids possess their own circular DNA and 70S ribosomes (semi-autonomous). They are categorized into three distinct functional classes: (1) Chloroplasts: The photosynthetic solar engines of plants. They contain green chlorophyll pigments along with carotenoids. Internal Structure: Surrounded by a double membrane enclosing a protein-rich fluid matrix called the Stroma (site of dark reaction carbon fixation). Suspended within the stroma is an extensive membrane network of flattened disc-like sacs called Thylakoids. Thylakoids are stacked like piles of coins into Grana (singular: granum), housing chlorophyll for light absorption; (2) Chromoplasts: Plastids containing non-green fat-soluble pigments (yellow carotene, red xanthophylls) that impart vibrant colors to flowers, petals, and ripening fruits to attract insect pollinators and seed-dispersing animals; (3) Leucoplasts: Colorless, non-pigmented plastids found in non-photosynthetic storage tissues (roots, seeds, tubers). Types: Amyloplasts (store starch, e.g., potatoes), Elaioplasts (store lipids/oils, e.g., mustard seeds), and Aleuroplasts (store proteins).",
        "key_points": [
            "Plastid Classes: Chloroplasts (green/photosynthetic), Chromoplasts (colored/attraction), Leucoplasts (colorless/storage).",
            "Chloroplast Thylakoids & Grana: Flattened thylakoid discs stacked into grana harbor chlorophyll to trap sunlight.",
            "Stroma Matrix: The fluid matrix containing circular DNA, 70S ribosomes, and enzymatic machinery for sugar synthesis.",
            "Leucoplast Storage Subtypes: Amyloplasts store starch; elaioplasts store oils/fats; aleuroplasts store proteins.",
            "Semi-Autonomy: Possess their own circular genome and ribosomes, reproducing independently inside plant cells."
        ],
        "narration": "Without plastids, life on Earth could not exist! Green Chloroplasts are nature's solar panels. Inside their fluid stroma, green thylakoid discs are stacked like coins into grana, trapping photons of sunlight to turn water and carbon dioxide into sweet glucose. But plastids are master shape-shifters! When a green tomato ripens into bright red, its chloroplasts transform into Chromoplasts, packed with vibrant carotenoids to attract birds. Underground, in potato roots, colorless Leucoplasts store tons of starch for energy. Dissect a chloroplast and watch plastids transform in our interactive simulator!",
        "sim_title": "Interactive Chloroplast Anatomy & Plastid Transformation Studio",
        "checkpoints": [
            {
                "q": "The colorless plastids specialized for storing starch grains, oils, and protein granules in plant roots and seeds are:",
                "options": ["Chloroplasts", "Chromoplasts", "Leucoplasts", "Lysosomes"],
                "ans": 2,
                "exp": "Leucoplasts are non-pigmented plastids whose primary function is the storage of nutrients: starch (amyloplasts), oils (elaioplasts), and proteins (aleuroplasts)."
            },
            {
                "q": "Inside a chloroplast, stacks of flattened membrane-bound thylakoid discs are known as:",
                "options": ["Stroma", "Grana", "Cristae", "Cisternae"],
                "ans": 1,
                "exp": "Thylakoid discs are organized into stacks resembling piles of coins called grana (singular: granum), where light-dependent photosynthetic reactions take place."
            }
        ]
    },
    {
        "id": 12,
        "title": "Endomembrane System: Endoplasmic Reticulum, Golgi Apparatus & Lysosomes",
        "subtitle": "Biosynthesis, Cisternal Processing, Membrane Biogenesis, and Autophagic Hydrolysis",
        "category": "Organelles",
        "badge": "C-3.1 • Endomembrane Traffic",
        "summary": "The Endomembrane System forms a coordinated metabolic pipeline for synthesizing, modifying, packaging, and dispatching cellular products: (1) Endoplasmic Reticulum (ER): An extensive network of membrane-bound tubules and flattened sacs extending from the nuclear envelope throughout the cytoplasm. Two types: (a) Rough ER (RER): Surface is studded with ribosomes, giving it a rough appearance under electron microscopy; synthesizes secretory and membrane proteins; (b) Smooth ER (SER): Lacks ribosomes; synthesizes lipids, phospholipids, and steroid hormones. In vertebrate liver cells, SER plays a crucial role in detoxifying harmful drugs, chemicals, and metabolic poisons; (2) Membrane Biogenesis: Proteins from RER and lipids from SER combine to construct, repair, and replenish cellular membranes (plasma membrane and organelle boundaries); (3) Golgi Apparatus (Camillo Golgi, 1898): Stacks of parallel, flattened, membrane-bound cisternae. Functions as the cell's postal shipping center: receives transition vesicles from ER at its cis-face, modifies, concentrates, packages them into secretory vesicles, and manufactures complex sugars and lysosomes; (4) Lysosomes ('Suicide Bags'): Spherical vesicles budded from Golgi, packed with powerful hydrolytic digestive enzymes synthesized by RER. They digest foreign pathogens, clean up cellular debris, and, during cellular trauma or starvation, burst to self-digest the cell (autolysis).",
        "key_points": [
            "RER vs SER: RER synthesizes proteins on ribosomes; SER synthesizes lipids and detoxifies liver poisons.",
            "Membrane Biogenesis: Joint assembly of cell membranes using RER proteins and SER lipids.",
            "Golgi Apparatus (Camillo Golgi): Cisternae stacks modifying, packaging, storing, and routing cellular secretions.",
            "Lysosomes as Waste Disposal: Hydrolytic enzymes break down foreign bacteria, worn-out organelles, and cellular food.",
            "The 'Suicide Bag' Phenomenon: Ruptured lysosomes release hydrolytic enzymes that digest their own damaged parent cell."
        ],
        "narration": "Inside every cell lies an industrial assembly line called the Endomembrane System! First, the Rough Endoplasmic Reticulum manufactures proteins on its tiny ribosomes. Next door, the Smooth ER pumps out lipids and detoxifies poisons in liver cells. Together, these proteins and lipids build new cell membranes in a process called membrane biogenesis! Next, the products arrive at the Golgi apparatus—the cell's post office—where Camillo Golgi's cisternae stacks inspect, modify, and package them into delivery vesicles. Some vesicles become Lysosomes: the cell's waste disposal crew. But if a cell is mortally wounded, its lysosomes burst open, digesting the damaged cell from within—which is why they are called suicide bags! Trace this protein assembly line in our interactive factory.",
        "sim_title": "Interactive Endomembrane Transport Factory & Lysosome Autophagy Engine",
        "checkpoints": [
            {
                "q": "Why are lysosomes universally referred to as the 'suicide bags' of a cell?",
                "options": [
                    "They produce toxic gases that kill neighboring cells",
                    "When the cell is damaged, lysosomes may burst and their powerful hydrolytic enzymes digest their own cell",
                    "They consume all the cell's ATP",
                    "They fuse with the nucleus to destroy DNA"
                ],
                "ans": 1,
                "exp": "Lysosomes contain potent hydrolytic digestive enzymes. If a cell undergoes metabolic damage or death, lysosomes rupture, releasing enzymes that autolyse (self-digest) the entire cell."
            },
            {
                "q": "Which organelle is responsible for the detoxification of many poisons and drugs in vertebrate liver cells?",
                "options": ["Rough Endoplasmic Reticulum", "Smooth Endoplasmic Reticulum", "Golgi Apparatus", "Lysosome"],
                "ans": 1,
                "exp": "In the liver cells of vertebrates, the Smooth Endoplasmic Reticulum (SER) plays a crucial physiological role in detoxifying a wide variety of drugs, chemicals, and metabolic poisons."
            }
        ]
    },
    {
        "id": 13,
        "title": "Vacuoles & Role of Biomolecules in Cellular Architecture",
        "subtitle": "Cell Sap Reservoirs, Protozoan Osmoregulation, and the Four Major Biomolecular Pillars",
        "category": "Organelles",
        "badge": "C-4.2 • Biomolecules & Vacuoles",
        "summary": "Vacuoles are membrane-bound storage compartments enclosing fluid, sap, or solid nutrients: (1) Plant Central Vacuole: In mature plant cells, a single gigantic permanent vacuole occupies 50% to 90% of cell volume, bounded by a specialized membrane called the Tonoplast. It is filled with cell sap containing water, amino acids, sugars, mineral ions, and organic acids, exerting turgor pressure against the cell wall to maintain structural firmness; (2) Animal Vacuoles: Small, numerous, and temporary, primarily serving nutrient and pinocytic storage; (3) Specialized Protozoan Vacuoles: In Amoeba, the Food Vacuole encapsulates engulfed prey for enzymatic digestion. In freshwater ciliates like Paramecium, the Contractile Vacuole actively pumps excess hypoosmotic water out of the cell to prevent bursting (osmoregulation); (4) The Four Major Biomolecular Pillars of Life (Competency C-4.2): (a) Proteins: Structural cytoskeletal fibers (actin, tubulin), enzymes catalyzing all biochemical reactions, and membrane channel pumps; (b) Lipids: Hydrophobic barrier of phospholipid membranes, steroid hormones, and dense energy storage; (c) Carbohydrates: Structural cellulose cell walls, cell surface recognition markers, and quick energy glucose/glycogen; (d) Nucleic Acids: DNA holds hereditary genes; RNA directs ribosomal protein synthesis; (e) ATP: High-energy phosphate currency powering mechanical and biochemical work.",
        "key_points": [
            "Plant Tonoplast & Central Vacuole: Large storage reservoir (50–90% volume) maintaining turgidity and storing nutrients.",
            "Amoeba Food Vacuole: Nutrient storage pouch where digestive enzymes break down engulfed food.",
            "Contractile Vacuole Osmoregulation: Specialized vacuole pumping out excess water to prevent protozoan lysis.",
            "Biomolecule Architecture: Proteins (enzymes/structure), Lipids (membranes/storage), Carbohydrates (cellulose/fuel), Nucleic Acids (DNA/RNA).",
            "ATP Energetics: Triphosphate bonds store readily available chemical energy driving all cellular physiological activities."
        ],
        "narration": "Vacuoles are far more than simple storage lockers! In plant cells, the giant central vacuole is wrapped in a membrane called the tonoplast, packed with nutrient-rich cell sap that keeps the whole plant pressurized and crisp. In microscopic creatures like Amoeba, vacuoles act as mobile stomachs to digest food, while Paramecium uses a pulsating contractile vacuole like a bilge pump to squirt out excess water so it doesn't pop! And underneath all this machinery work four master biomolecules: Proteins build enzymes and motors, Lipids build water-tight membranes, Carbohydrates provide cellulose armor and energy, and Nucleic Acids store the master genetic code. Explore vacuolar mechanics and biomolecules in our interactive studio!",
        "sim_title": "Interactive Vacuolar Turgidity & Biomolecule Molecular Palette",
        "checkpoints": [
            {
                "q": "In freshwater protozoa such as Amoeba and Paramecium, which specialized organelle plays an essential role in osmoregulation (expelling excess water)?",
                "options": ["Food vacuole", "Contractile vacuole", "Lysosome", "Centrosome"],
                "ans": 1,
                "exp": "The contractile vacuole collects and periodically expels excess water entering the freshwater protozoan cell via osmosis, maintaining osmotic balance (osmoregulation)."
            },
            {
                "q": "The membrane bounding the large central vacuole of a plant cell is specifically known as the:",
                "options": ["Crista", "Tonoplast", "Nuclear envelope", "Thylakoid"],
                "ans": 1,
                "exp": "The semipermeable membrane that encloses the central vacuole in a plant cell is called the tonoplast."
            }
        ]
    },
    {
        "id": 14,
        "title": "Cell Division: Mitosis, Meiosis & Cancer Dynamics",
        "subtitle": "Equational Somatic Growth, Reductional Gamete Variation, and Oncogenic Checkpoint Failure",
        "category": "Cell Division",
        "badge": "C-3.3 • Mitosis, Meiosis & Cancer",
        "summary": "Cell division is the biological mechanism by which new cells are formed for organismal growth, tissue repair, and reproduction: (1) Mitosis (Equational Division): Occurs in somatic (body) cells for growth, tissue repair, wound healing, and asexual reproduction. Process: A single diploid parent cell (2n = 46 in humans) duplicates its chromosomes and undergoes one nuclear division, producing two genetically identical diploid daughter cells (2n) with an invariant chromosome count. Maintains genetic stability and tissue identity; (2) Meiosis (Reduction Division): Occurs exclusively in specialized germ cells of reproductive organs (testes and ovaries in animals; anthers and ovaries in flowering plants) to produce gametes (sperm and egg). Process: A diploid germ cell (2n) undergoes DNA duplication followed by TWO sequential nuclear divisions (Meiosis I and Meiosis II), producing four non-identical haploid daughter cells (n = 23 in humans) with half the original chromosome number. Crossing-over (genetic recombination) during Prophase I creates novel gene combinations, generating the natural variations that drive evolution and diversity; (3) Cellular Division and Cancer: Normal cell division is rigorously controlled by molecular cell cycle checkpoints (cyclins and tumor suppressor proteins). When gene mutations disrupt these checkpoints, cells escape contact inhibition and divide uncontrollably, forming abnormal masses of tissue called malignant tumors (Cancer).",
        "key_points": [
            "Mitosis (Equational): Produces 2 genetically identical diploid (2n) daughter cells for growth and tissue repair.",
            "Meiosis (Reductional): Produces 4 genetically diverse haploid (n) gametes with half the chromosome count for reproduction.",
            "Chromosome Invariance: Mitosis preserves chromosome number (2n → 2n); meiosis halves it (2n → n) to maintain species ploidy upon fertilization.",
            "Crossing-Over: Physical exchange of chromosome segments in meiosis creates genetic variations essential for adaptation.",
            "Cancer Pathology: Uncontrolled, unregulated mitotic proliferation caused by failed cell cycle checkpoints and oncogenic mutations."
        ],
        "narration": "How does a single fertilized egg cell grow into a human with thirty trillion cells? Through Cell Division! When your body needs to grow taller or heal a scraped knee, somatic cells perform Mitosis—one mother cell divides into two identical twin daughter cells with the exact same chromosome count. But when your body creates sperm or egg cells for reproduction, it performs Meiosis! Meiosis cuts the chromosome number in half from forty-six to twenty-three, and shuffles genes through crossing over to create unique variations. But what happens if the brake pedal on mitosis breaks? The cells divide uncontrollably, forming a tumor—this is Cancer. Track chromosomes through mitosis, meiosis, and cancer in our interactive division simulator!",
        "sim_title": "Mitosis vs Meiosis Chromosome Tracker & Oncogenic Tumor Simulator",
        "checkpoints": [
            {
                "q": "How many daughter cells are produced at the end of meiosis, and what is their chromosome ploidy relative to the diploid parent cell?",
                "options": [
                    "2 diploid daughter cells with the same chromosome number",
                    "4 haploid daughter cells with half the original chromosome number",
                    "4 diploid daughter cells with double the chromosome number",
                    "2 haploid daughter cells"
                ],
                "ans": 1,
                "exp": "Meiosis involves two successive divisions resulting in 4 genetically non-identical haploid (n) daughter cells, each containing half the chromosome number of the diploid (2n) parent cell."
            },
            {
                "q": "Cancer in human tissues is fundamentally characterized at the cellular level by:",
                "options": [
                    "Permanent cessation of all cell division",
                    "Uncontrolled, unregulated mitotic proliferation due to failure of cell cycle checkpoints",
                    "Conversion of mitosis into meiosis in somatic cells",
                    "Excessive accumulation of chloroplasts in human cells"
                ],
                "ans": 1,
                "exp": "Cancer is a disease of unregulated cell division where mutations destroy checkpoint controls, causing cells to divide rapidly, disregard contact inhibition, and form malignant tumors."
            }
        ]
    },
    {
        "id": 15,
        "title": "Indian Pioneers & Medical Case Studies: Prof. A.K. Sharma & Leigh Syndrome",
        "subtitle": "Cytogenetic Banding Innovations, Mitochondrial Neuropathies, and Muscular Biomechanics",
        "category": "Interdisciplinary Science",
        "badge": "C-6.1 • C-5.2 • Indian Cytogenetics",
        "summary": "Bridging fundamental cell biology with historical innovations, clinical medicine, and physical culture: (1) Indian Pioneer Contribution — Prof. Arun Kumar Sharma (1924–2017) (C-6.1): Known as the 'Father of Indian Cytogenetics'. Professor Sharma revolutionized chromosome research globally by developing specialized orcein staining and banding techniques to analyze plant chromosome morphology. He demonstrated that repetitive non-coding DNA and heterochromatin play vital functional roles in speciation and chromosomal evolution, founding the internationally renowned Centre of Advanced Study in Cell and Chromosome Research at the University of Calcutta; (2) Clinical Case Study — Leigh Syndrome & Mitochondrial Dysfunction (C-5.2): Leigh Syndrome (Subacute Necrotizing Encephalomyelopathy) is a severe neurometabolic disorder caused by genetic mutations in mitochondrial DNA (mtDNA) or nuclear genes encoding oxidative phosphorylation enzymes. Mitochondrial ATP production collapses; energy-starved neural tissues (basal ganglia, brainstem) and skeletal muscles suffer focal necrosis, producing hypotonia, ataxia, and respiratory failure, illustrating the clinical criticality of functional mitochondria; (3) Muscle Cell Biomechanics in Dance and Sports (C-5.3): Skeletal muscle fibers contain parallel sarcomeres with interdigitating actin and myosin filaments. ATP hydrolysis drives cyclic myosin cross-bridge sliding, producing rapid mechanical tension. In classical Indian dance forms (e.g., the deep knee-flexion Aramandi posture of Bharatanatyam) and athletic sprints, muscle fibers synchronize ATP consumption, lactic acid buffering, and synovial joint levers to maintain dynamic equilibrium.",
        "key_points": [
            "Prof. Arun Kumar Sharma: Father of Indian Cytogenetics; pioneered chromosome banding and orcein stain microtechniques.",
            "Heterochromatin Discovery: Demonstrated that repeated DNA sequences stabilize chromosome architecture and drive evolution.",
            "Leigh Syndrome Pathology: Genetic defects in mitochondrial ATP synthesis produce catastrophic neuro-muscular starvation.",
            "Sarcomere Sliding Filament Theory: Actin-myosin cross-bridges powered by mitochondrial ATP drive muscular contraction.",
            "Dance & Sports Ergonomics: Muscle fiber ATP metabolism and joint levers enable demanding postures like Bharatanatyam Aramandi."
        ],
        "narration": "Cell biology has deep roots in Indian science and profound impacts on human health! Professor Arun Kumar Sharma, the Father of Indian Cytogenetics, invented brilliant chromosome staining techniques using orcein, proving that repetitive DNA is critical for chromosome evolution. In medicine, when mitochondria fail due to genetic defects, the disease Leigh Syndrome occurs—without ATP, the brain and muscles are starved of energy, leading to motor loss. And every time a Bharatanatyam dancer drops into the Aramandi stance or a sprinter bursts off the blocks, trillions of muscle cells slide actin and myosin filaments using mitochondrial ATP! Explore Professor Sharma's chromosome karyotypes and muscle mechanics in our interactive lab.",
        "sim_title": "Interactive Cytogenetics Karyotyper & Mitochondrial Dysfunction Analyzer",
        "checkpoints": [
            {
                "q": "Professor Arun Kumar Sharma is celebrated in the history of Indian biological sciences as the Father of Indian Cytogenetics primarily for his pioneering work on:",
                "options": [
                    "Developing synthetic insulin",
                    "Innovating chromosome staining, orcein banding, and clarifying the structural role of repeated DNA",
                    "Discovering the endoplasmic reticulum",
                    "Isolating antibiotic penicillin from penicillium"
                ],
                "ans": 1,
                "exp": "Prof. A.K. Sharma developed innovative microtechniques and stains (like orcein) to reveal chromosome bands and proved that repetitive DNA plays an active role in chromosomal evolution."
            },
            {
                "q": "Leigh syndrome is a severe neuromuscular disorder directly caused by the failure of which cellular organelle to produce ATP?",
                "options": ["Golgi apparatus", "Mitochondria", "Lysosomes", "Vacuoles"],
                "ans": 1,
                "exp": "Leigh syndrome is caused by genetic defects in mitochondrial respiratory chain enzymes, crippling oxidative phosphorylation and depriving high-energy organs (brain and muscles) of ATP."
            }
        ]
    },
    {
        "id": 16,
        "title": "Synthetic Biology & Creative Eco-Modeling: The Future of the Cell",
        "subtitle": "Craig Venter's Synthetic JCVI-syn3.0, Minimal Genomes, and Sustainable Pedagogical Models",
        "category": "Future Horizons",
        "badge": "C-7.2 • C-8.1 • Synthetic Biology",
        "summary": "Frontiers of modern cytology combine bioengineering inquiry with sustainable pedagogical design: (1) Philosophical Inquiry — Can We Create an Artificial Cell? (Competency C-7.2): In 2016, J. Craig Venter and his research institute synthesized JCVI-syn3.0, a living bacterium possessing a chemically synthesized, computer-designed minimal genome of only 473 genes (the smallest genome of any free-living autonomous organism). Strikingly, 149 of these 473 essential genes (nearly one-third) have biological functions that remain completely unknown to modern science! Scientists are assembling 'Protocells' from the bottom up by encapsulating artificial enzymatic cascades, self-replicating ribozymes, and synthetic DNA within artificial lipid liposomes to create programmable cellular biosensors; (2) Creative Eco-Friendly Cell Modeling (Competency C-8.1): Students can exhibit creativity by modeling 3D eukaryotic cells using zero-cost, biodegradable materials: dough/clay for cytoplasm and nucleus, discarded cardboard boxes for cell walls, lentils/kidney beans for mitochondria, dried peas for ribosomes, and vegetable peelings for endoplasmic reticulum cisternae, demonstrating how complex biological concepts can be represented sustainably without plastic waste.",
        "key_points": [
            "JCVI-syn3.0 Synthetic Organism: Synthetic cell engineered with a bare minimal genome of 473 genes required for autonomous life.",
            "The Unknown Genome Mystery: ~31% of the minimal genome's essential genes have unknown functions, highlighting cytological frontiers.",
            "Protocell Bioengineering: Constructing artificial life-like compartments using liposomes, synthetic enzymes, and metabolic RNA.",
            "Eco-Friendly Cell Modeling: Constructing 3D biological models using discarded cardboard, clay, seeds, and organic waste.",
            "Pedagogical Synthesis: Combines cutting-edge scientific frontiers with hands-on sustainable classroom creativity."
        ],
        "narration": "Can human beings build a living cell from scratch? In 2016, scientists chemically synthesized a minimal artificial genome with just four hundred and seventy-three genes and booted it up inside an empty bacterial shell—creating JCVI-syn3.0, the world's first synthetic organism! Astonishingly, scientists still do not know what one-third of those vital genes actually do, showing how many cell mysteries remain for you to discover. You can also become a biological architect by designing 3D cell models using eco-friendly materials like clay, dried seeds, and cardboard! Build your own synthetic cell in our final interactive engineering simulator.",
        "sim_title": "Interactive Synthetic Cell Designer & Minimal Genome Builder",
        "checkpoints": [
            {
                "q": "What major breakthrough in synthetic cell biology was achieved by the creation of the synthetic organism JCVI-syn3.0?",
                "options": [
                    "Creating a human embryo in a test tube",
                    "Engineering a viable, dividing bacterial cell powered by a chemically synthesized minimal genome of 473 genes",
                    "Curing all bacterial infections using artificial mitochondria",
                    "Replacing all plant chloroplasts with solar cells"
                ],
                "ans": 1,
                "exp": "JCVI-syn3.0 demonstrated that a living, autonomous, replicating cell can be booted up from a chemically synthesized, computer-designed minimal genome of 473 genes."
            },
            {
                "q": "Which of the following approaches embodies creative eco-friendly cell modeling in education?",
                "options": [
                    "Buying non-biodegradable plastic cell kits from commercial stores",
                    "Using discarded cardboard, edible dough, clay, and dried seeds to construct 3D cellular structures",
                    "Disposing of toxic chemical stains in drinking water sinks",
                    "Constructing non-recyclable styrofoam organelle displays"
                ],
                "ans": 1,
                "exp": "Using sustainable, low-cost or zero-cost biodegradable materials (dough, clay, dried seeds, scrap cardboard) enables creative, eco-friendly 3D modeling of cell structures without environmental waste."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 1,
        "title": "Mastery Challenge 1: Cell Discovery, Microscopy & Prokaryotes vs Eukaryotes",
        "badge": "Quiz 1 • Foundations & Types",
        "questions": [
            {
                "q": "1. Robert Hooke observed thin cork slices in 1665 and discovered cells. What was he actually observing under his primitive microscope?",
                "options": [
                    "Living cytoplasm and nuclei",
                    "Empty dead cell walls of Spanish oak bark tissue",
                    "Active mitochondria producing ATP",
                    "Prokaryotic bacteria dividing by fission"
                ],
                "ans": 1,
                "solution": "Step 1: Cork is dead plant bark tissue derived from the cork oak tree (Quercus suber).\nStep 2: In mature cork, living protoplasm has degenerated, leaving behind rigid suberin-impregnated cellulose cell walls.\nStep 3: Hooke observed these empty cellulose compartments, which he termed 'cellulae'."
            },
            {
                "q": "2. Who discovered the nucleus in plant cells in 1831?",
                "options": ["Robert Hooke", "Robert Brown", "Anton van Leeuwenhoek", "Rudolf Virchow"],
                "ans": 1,
                "solution": "Step 1: In 1831, Scottish botanist Robert Brown was observing orchid epidermal cells.\nStep 2: He noted a consistent opaque circular structure inside each cell and coined the term 'nucleus'.\nStep 3: Correct answer is Robert Brown."
            },
            {
                "q": "3. Which of the following is a key component of the classical Cell Theory formulated by Schleiden and Schwann?",
                "options": [
                    "All cells have a nucleus and chloroplasts",
                    "All living organisms are composed of one or more cells, and the cell is the basic unit of life",
                    "Cells spontaneously crystallize from non-living fluids",
                    "All cells have rigid cellulose walls"
                ],
                "ans": 1,
                "solution": "Step 1: Matthias Schleiden (1838) concluded all plant tissues are composed of cells.\nStep 2: Theodor Schwann (1839) unified this with animal tissues, declaring that all living organisms are composed of cells, making the cell the basic structural and functional unit of life.\nStep 3: The correct option is the second statement."
            },
            {
                "q": "4. How does the nuclear material of a prokaryotic cell differ fundamentally from that of a eukaryotic cell?",
                "options": [
                    "Prokaryotes have multiple linear chromosomes wrapped in histones",
                    "Prokaryotes lack a nuclear envelope; their genetic material is naked circular DNA in a nucleoid region",
                    "Prokaryotes have a larger nucleus with multiple nucleoli",
                    "Prokaryotes possess RNA instead of DNA"
                ],
                "ans": 1,
                "solution": "Step 1: Eukaryotic cells possess a double-membrane nuclear envelope enclosing multiple linear chromosomes.\nStep 2: Prokaryotic cells (bacteria) lack any nuclear membrane; their genetic material is a single circular DNA molecule located in the cytoplasm in an undefined region termed the 'nucleoid'.\nStep 3: Correct option is statement 2."
            },
            {
                "q": "5. Which ribosome type is found suspended in the cytoplasm of a prokaryotic bacterium?",
                "options": ["60S ribosomes", "70S ribosomes", "80S ribosomes", "90S ribosomes"],
                "ans": 1,
                "solution": "Step 1: Prokaryotes possess 70S ribosomes composed of 50S and 30S subunits.\nStep 2: Eukaryotic cytoplasm possesses larger 80S ribosomes (composed of 60S and 40S subunits).\nStep 3: Therefore, bacteria possess 70S ribosomes."
            },
            {
                "q": "6. Which of the following structures is present in plant cells but absent in typical animal cells?",
                "options": ["Plasma membrane", "Ribosomes", "Cellulose cell wall", "Mitochondria"],
                "ans": 2,
                "solution": "Step 1: Plant cells have a rigid outer cell wall composed of cellulose.\nStep 2: Animal cells have only a flexible outer plasma membrane and lack a cell wall.\nStep 3: Correct answer is Cellulose cell wall."
            },
            {
                "q": "7. What is the typical size range of a prokaryotic cell compared to a eukaryotic cell?",
                "options": [
                    "Prokaryotes: 1 to 10 µm; Eukaryotes: 5 to 100 µm",
                    "Prokaryotes: 50 to 500 µm; Eukaryotes: 1 to 5 µm",
                    "Both are identical in size (100 to 200 µm)",
                    "Prokaryotes are visible to the naked eye (1 to 2 cm)"
                ],
                "ans": 0,
                "solution": "Step 1: Prokaryotes are small, primitive cells generally ranging from 1 to 10 micrometers (µm).\nStep 2: Eukaryotes are substantially larger and more complex, generally ranging from 5 to 100 µm.\nStep 3: Correct option is 1 to 10 µm vs 5 to 100 µm."
            },
            {
                "q": "8. Which of the following organisms is an example of a prokaryote?",
                "options": ["Amoeba proteus", "Escherichia coli (bacterium)", "Saccharomyces cerevisiae (yeast)", "Spirogyra (alga)"],
                "ans": 1,
                "solution": "Step 1: Amoeba is a unicellular eukaryote (protist); yeast is a unicellular eukaryotic fungus; Spirogyra is a green eukaryotic alga.\nStep 2: Escherichia coli (E. coli) is a bacterium possessing a nucleoid and 70S ribosomes, making it a true prokaryote.\nStep 3: Correct answer is E. coli."
            },
            {
                "q": "9. During preparation of a temporary slide of onion peel, what stain is typically used to color the cell walls and nuclei?",
                "options": ["Safranin", "Methylene Blue", "Phenolphthalein", "Gram's Iodine alone"],
                "ans": 0,
                "exp": "Step 1: Safranin is a basic biological stain that imparts a pinkish-red color to lignified and cellulosic cell walls and nuclei of plant tissues.\nStep 2: Methylene blue is generally preferred for animal epithelial cells.\nStep 3: Hence, Safranin is the standard stain for onion peel mounts."
            },
            {
                "q": "10. In animal cells, which non-membrane organelle containing a pair of centrioles organizes the spindle apparatus during mitosis?",
                "options": ["Centrosome", "Peroxisome", "Lysosome", "Nucleolus"],
                "ans": 0,
                "solution": "Step 1: Animal cells contain a specialized organelle called the Centrosome located near the nucleus.\nStep 2: The centrosome contains two perpendicularly oriented cylindrical structures called centrioles.\nStep 3: Centrioles organize the mitotic spindle fibers during nuclear division."
            }
        ]
    },
    {
        "id": 2,
        "title": "Mastery Challenge 2: Organelles: Nucleus, Mitochondria, Plastids & ER",
        "badge": "Quiz 2 • Organellar Biology",
        "questions": [
            {
                "q": "11. Why are mitochondria capable of synthesizing some of their own structural proteins independently of the cell's nucleus?",
                "options": [
                    "They borrow proteins from the Golgi body",
                    "They possess their own circular DNA and 70S ribosomes",
                    "Their outer membrane is made of pure amino acids",
                    "They do not require any proteins to function"
                ],
                "ans": 1,
                "solution": "Step 1: Mitochondria are semi-autonomous organelles originating from ancestral endosymbiotic alpha-proteobacteria.\nStep 2: They retain their own maternal circular mitochondrial DNA (mtDNA) and 70S ribosomes.\nStep 3: This molecular machinery allows them to synthesize critical respiratory enzyme subunits directly."
            },
            {
                "q": "12. What molecule represents the universal 'energy currency' generated by mitochondria during cellular respiration?",
                "options": ["DNA (Deoxyribonucleic acid)", "ATP (Adenosine triphosphate)", "RNA (Ribonucleic acid)", "NADH only"],
                "ans": 1,
                "solution": "Step 1: Mitochondria perform oxidative phosphorylation to convert energy from food into Adenosine Triphosphate.\nStep 2: Hydrolysis of the phosphoanhydride bonds of ATP releases free energy (~30.5 kJ/mol) powering cellular work.\nStep 3: ATP is known as the energy currency of the cell."
            },
            {
                "q": "13. What is the primary functional difference between the Rough Endoplasmic Reticulum (RER) and Smooth Endoplasmic Reticulum (SER)?",
                "options": [
                    "RER synthesizes lipids; SER synthesizes proteins",
                    "RER is studded with ribosomes and synthesizes proteins; SER lacks ribosomes and synthesizes lipids/steroids",
                    "RER is located only in plant cells; SER only in animal cells",
                    "RER produces ATP; SER produces glucose"
                ],
                "ans": 1,
                "solution": "Step 1: Rough ER is named for the presence of membrane-bound 80S ribosomes on its cytoplasmic surface, which synthesize secretory and membrane proteins.\nStep 2: Smooth ER lacks ribosomes and houses enzymes responsible for lipid, phospholipid, and steroid hormone biosynthesis, as well as detoxification.\nStep 3: Correct answer is statement 2."
            },
            {
                "q": "14. Which organelle receives proteins from the ER, modifies them, packages them into vesicles, and forms lysosomes?",
                "options": ["Peroxisome", "Golgi apparatus", "Centrosome", "Tonoplast"],
                "ans": 1,
                "solution": "Step 1: Camillo Golgi discovered the reticular cisternal apparatus in 1898.\nStep 2: The Golgi apparatus receives vesicles from the ER at its cis-face, glycosylates/modifies proteins, sorts and packages them at the trans-face, and buds off primary lysosomes.\nStep 3: Correct answer is the Golgi apparatus."
            },
            {
                "q": "15. The green pigment responsible for trapping sunlight inside chloroplast thylakoids during photosynthesis is:",
                "options": ["Anthocyanin", "Chlorophyll", "Carotene", "Xanthophyll"],
                "ans": 1,
                "solution": "Step 1: Chloroplasts contain the photosynthetic pigment chlorophyll (primarily chlorophyll a and b).\nStep 2: Chlorophyll molecules embedded in the thylakoid membranes absorb blue and red light while reflecting green light.\nStep 3: Correct answer is Chlorophyll."
            },
            {
                "q": "16. Potato tubers store abundant reserves of food in specialized colorless leucoplasts known as:",
                "options": ["Amyloplasts", "Elaioplasts", "Aleuroplasts", "Chromoplasts"],
                "ans": 0,
                "solution": "Step 1: Leucoplasts are non-pigmented storage plastids.\nStep 2: Amyloplasts are specialized leucoplasts that synthesize and store starch (amylose and amylopectin) in tubers like potatoes.\nStep 3: Correct answer is Amyloplasts."
            },
            {
                "q": "17. What biological event occurs during 'membrane biogenesis'?",
                "options": [
                    "DNA replicates inside the nucleus",
                    "Proteins synthesized by RER and lipids synthesized by SER combine to build cellular membranes",
                    "Cellulose fibers are woven to form the cell wall",
                    "Lysosomes burst to destroy the plasma membrane"
                ],
                "ans": 1,
                "solution": "Step 1: Membrane biogenesis is the synthesis of new biological membranes within the cell.\nStep 2: RER synthesizes structural and transport proteins, while SER synthesizes membrane phospholipids and cholesterol.\nStep 3: These constituents are transported via vesicles to assemble and replenish the plasma membrane."
            },
            {
                "q": "18. What is the role of the nuclear pores present across the nuclear envelope?",
                "options": [
                    "Allow free diffusion of all organelles out of the nucleus",
                    "Permit regulated bidirectional transport of RNA, ribosomal subunits, and proteins between nucleus and cytoplasm",
                    "Let water rush into the nucleus to create turgor pressure",
                    "Trap sunlight for photosynthesis"
                ],
                "ans": 1,
                "solution": "Step 1: Nuclear pores are large multi-protein complexes spanning both layers of the nuclear envelope.\nStep 2: They selectively regulate the export of mRNA and ribosomal subunits and the import of nuclear proteins (histones, polymerases).\nStep 3: Correct answer is statement 2."
            },
            {
                "q": "19. Which of the following organelles contains potent hydrolytic enzymes that function at an acidic pH to digest foreign bacteria and damaged organelles?",
                "options": ["Vacuole", "Mitochondrion", "Lysosome", "Centriole"],
                "ans": 2,
                "solution": "Step 1: Lysosomes are membrane-bound vesicles containing over 50 acidic hydrolases (proteases, nucleases, lipases).\nStep 2: They fuse with phagosomes or autophagosomes to degrade foreign microbes and worn-out organelles.\nStep 3: Correct answer is Lysosome."
            },
            {
                "q": "20. The fluid proteinaceous matrix of a chloroplast in which thylakoids are suspended is called the:",
                "options": ["Matrix", "Stroma", "Crista", "Cytosol"],
                "ans": 1,
                "solution": "Step 1: Mitochondria contain an internal matrix; chloroplasts contain an internal fluid called the Stroma.\nStep 2: The stroma houses circular chloroplast DNA, 70S ribosomes, and Calvin cycle enzymes for carbon fixation.\nStep 3: Correct answer is Stroma."
            }
        ]
    },
    {
        "id": 3,
        "title": "Mastery Challenge 3: Membrane Transport, Diffusion, Osmosis & Plasmolysis",
        "badge": "Quiz 3 • Transport & Osmosis",
        "questions": [
            {
                "q": "21. A red blood cell (animal cell) is placed in a strongly hypotonic solution of pure distilled water. What will happen to the cell?",
                "options": [
                    "It will lose water and undergo plasmolysis",
                    "It will absorb water by endosmosis, swell, and burst (osmotic lysis)",
                    "Its size will remain unchanged because animal membranes are impermeable to water",
                    "It will divide immediately by mitosis"
                ],
                "ans": 1,
                "solution": "Step 1: Pure water is hypotonic relative to intracellular cytoplasm (which contains ~0.9% salt).\nStep 2: Water rushes into the RBC down its concentration gradient by endosmosis.\nStep 3: Lacking a rigid cell wall to exert counter-wall pressure, the fragile plasma membrane stretches and bursts (hemolysis/osmotic lysis)."
            },
            {
                "q": "22. What happens to a living plant cell when placed in a hypertonic concentrated sugar syrup?",
                "options": [
                    "Water enters the cell causing extreme turgidity",
                    "Water leaves the cell via exosmosis, causing the protoplast to shrink away from the cell wall (plasmolysis)",
                    "The cell wall dissolves completely",
                    "The cell undergoes rapid meiosis"
                ],
                "ans": 1,
                "solution": "Step 1: The external concentrated sugar syrup has a lower water concentration than the cell sap.\nStep 2: Water exits the central vacuole by exosmosis.\nStep 3: The living protoplast contracts and pulls away from the rigid cell wall, a state known as plasmolysis."
            },
            {
                "q": "23. If the external medium surrounding a cell has exactly the same water concentration as the cell's interior, the solution is described as:",
                "options": ["Hypotonic", "Hypertonic", "Isotonic", "Osmotic"],
                "ans": 2,
                "solution": "Step 1: An isotonic solution has identical effective solute and water concentrations to the cell cytoplasm.\nStep 2: Water moves across the membrane in both directions at equal rates (net movement is zero).\nStep 3: The cell maintains its stable volume in an isotonic solution."
            },
            {
                "q": "24. In the Fluid Mosaic Model, the term 'mosaic' refers to:",
                "options": [
                    "The pattern formed by different colored lipids",
                    "The irregular arrangement of diverse proteins embedded in or associated with the lipid bilayer",
                    "The tiled structure of cellulose microfibrils",
                    "The stained appearance of chromosomes under the microscope"
                ],
                "ans": 1,
                "solution": "Step 1: The 'fluid' component refers to the viscous, laterally moving phospholipid bilayer.\nStep 2: The 'mosaic' component refers to the heterogeneous proteins embedded within (integral) or attached to (peripheral) this lipid matrix, resembling a mosaic tile floor.\nStep 3: Correct answer is statement 2."
            },
            {
                "q": "25. Which of the following is an example of simple diffusion in biological organisms?",
                "options": [
                    "Exchange of respiratory gases (O₂ and CO₂) between blood capillaries and body cells",
                    "Absorption of water by roots from soil via a semipermeable membrane",
                    "Pumping of sodium and potassium ions against their concentration gradient using ATP",
                    "Shrinkage of a plant protoplast in salt solution"
                ],
                "ans": 0,
                "solution": "Step 1: Diffusion is the passive movement of solutes or gases down their concentration gradient without requiring a membrane.\nStep 2: Respiratory exchange of O₂ and CO₂ across alveolar and capillary walls occurs entirely by passive diffusion.\nStep 3: Water absorption by roots is osmosis; sodium-potassium pumping is active transport."
            },
            {
                "q": "26. Why do dried raisins swell when placed in a bowl of pure tap water?",
                "options": [
                    "Tap water is hypertonic, drawing sugar out of the raisins",
                    "Tap water is hypotonic, so water enters the raisins by endosmosis",
                    "The raisins reproduce by budding",
                    "The cell wall of the raisin contracts"
                ],
                "ans": 1,
                "solution": "Step 1: Inside dried raisins, sugar concentration is high and water concentration is low.\nStep 2: Tap water is hypotonic relative to the raisin's interior.\nStep 3: Water moves into the raisins by endosmosis across the cell membranes, causing them to swell."
            },
            {
                "q": "27. In a freshwater protozoan such as Paramecium, what would happen if its contractile vacuole stopped working?",
                "options": [
                    "The cell would shrink from plasmolysis",
                    "Water entering by osmosis would accumulate until the cell swelled and burst",
                    "The cell would immediately begin photosynthesis",
                    "The cell would produce double the amount of ATP"
                ],
                "ans": 1,
                "solution": "Step 1: Freshwater is hypotonic to the protozoan's cytoplasm, so water continuously enters by osmosis.\nStep 2: The contractile vacuole acts as a bilge pump, collecting and expelling this excess water.\nStep 3: If the vacuole fails, water accumulates until the membrane ruptures (lysis)."
            },
            {
                "q": "28. What is the specialized semipermeable membrane that bounds the central vacuole in a plant cell called?",
                "options": ["Plasma membrane", "Tonoplast", "Pellicle", "Percoll"],
                "ans": 1,
                "solution": "Step 1: The vacuole in plant cells is bounded by a single selectively permeable membrane.\nStep 2: This membrane is specifically termed the Tonoplast.\nStep 3: It regulates ion and metabolite transport between the cytoplasm and vacuolar sap."
            },
            {
                "q": "29. What property of the plasma membrane enables Amoeba to extend pseudopodia and engulf prey through endocytosis?",
                "options": [
                    "Rigid cellulose cross-linking",
                    "Fluidity and mechanical flexibility of the phospholipid bilayer",
                    "High concentration of calcium phosphate crystals",
                    "Complete impermeability to water"
                ],
                "ans": 1,
                "solution": "Step 1: The phospholipid molecules in the bilayer are not locked in place; they move laterally in a fluid state.\nStep 2: This fluidity gives the membrane physical flexibility, allowing the cell to deform, project pseudopodia, and pinch off endocytic vesicles.\nStep 3: Correct answer is statement 2."
            },
            {
                "q": "30. When a plasmolysed plant cell is removed from brine and placed back into pure distilled water, what process restores its normal turgid state?",
                "options": ["De-plasmolysis via endosmosis", "Exosmosis", "Autolysis", "Phagocytosis"],
                "ans": 0,
                "solution": "Step 1: Placing the plasmolysed cell into hypotonic pure water creates an inward water gradient.\nStep 2: Water enters the vacuole by endosmosis.\nStep 3: The vacuole inflates, pushing the protoplast back against the cell wall in a process termed de-plasmolysis."
            }
        ]
    },
    {
        "id": 4,
        "title": "Mastery Challenge 4: Cell Division, Cancer, Indian Cytogenetics & Case Studies",
        "badge": "Quiz 4 • Advanced Synthesis",
        "questions": [
            {
                "q": "31. A human somatic skin cell with 46 chromosomes divides by mitosis to heal a wound. How many chromosomes will each of the two resulting daughter cells contain?",
                "options": ["23 chromosomes", "46 chromosomes", "92 chromosomes", "12 chromosomes"],
                "ans": 1,
                "solution": "Step 1: Mitosis is an equational division occurring in somatic cells.\nStep 2: DNA replicates during S-phase, and sister chromatids separate equally into two new nuclei.\nStep 3: Each daughter cell receives the exact diploid chromosome complement (2n = 46 chromosomes)."
            },
            {
                "q": "32. During which type of cell division does genetic recombination (crossing-over) occur, generating novel variations for evolution?",
                "options": ["Binary fission", "Mitosis", "Meiosis (Prophase I)", "Budding"],
                "ans": 2,
                "solution": "Step 1: During Prophase I of Meiosis, homologous maternal and paternal chromosomes pair up (synapsis).\nStep 2: Non-sister chromatids exchange genetic segments at chiasmata (crossing-over).\nStep 3: This recombination creates unique combinations of alleles, producing genetic variation in gametes."
            },
            {
                "q": "33. What is the fundamental cellular malfunction that leads to the development of cancer in human tissues?",
                "options": [
                    "Cells stop dividing and enter permanent dormancy",
                    "Mutations disrupt cell cycle checkpoints, causing uncontrolled and continuous mitotic cell division",
                    "Mitochondria convert into chloroplasts",
                    "Lysosomes stop producing enzymes"
                ],
                "ans": 1,
                "solution": "Step 1: In healthy tissues, cell division is strictly governed by checkpoint proteins and growth factors.\nStep 2: When mutations damage tumor-suppressor genes or activate oncogenes, cell cycle checkpoints fail.\nStep 3: Cells divide incessantly, ignore contact inhibition, and accumulate into malignant tumors."
            },
            {
                "q": "34. Professor Arun Kumar Sharma is venerated as the 'Father of Indian Cytogenetics' for his revolutionary contributions to:",
                "options": [
                    "Developing antibiotics from soil bacteria",
                    "Innovating chromosome banding techniques using orcein stain and uncovering the role of repetitive DNA",
                    "Mapping the complete human genome in 1950",
                    "Creating the first synthetic bacterium"
                ],
                "ans": 1,
                "solution": "Step 1: Prof. A.K. Sharma at the University of Calcutta developed novel orcein-based chromosome staining protocols.\nStep 2: His research proved that heterochromatin and repeated non-coding DNA sequences play vital dynamic roles in chromosome stability and plant speciation.\nStep 3: Correct answer is statement 2."
            },
            {
                "q": "35. In the clinical case study of Leigh Syndrome, patients suffer severe neuro-muscular failure primarily because:",
                "options": [
                    "Their red blood cells burst due to defective cell walls",
                    "Genetic mutations in mitochondrial DNA impair oxidative phosphorylation, starving brain and muscle cells of ATP",
                    "Their lysosomes digest healthy bone tissue",
                    "Their ribosomes produce excessive cellulose"
                ],
                "ans": 1,
                "solution": "Step 1: Leigh syndrome is a genetic neurometabolic disorder affecting respiratory chain complexes in mitochondria.\nStep 2: Collapse of ATP synthesis starves energy-intensive organs (basal ganglia, brainstem, motor neurons, skeletal muscles).\nStep 3: This causes progressive neurodegeneration and loss of motor function."
            },
            {
                "q": "36. In sports and classical dance forms like the Bharatanatyam 'Aramandi' knee-bend, sustained muscle contraction is powered at the cellular level by:",
                "options": [
                    "Passive diffusion of starch grains",
                    "Cyclic sliding of actin and myosin protein filaments powered by mitochondrial ATP hydrolysis",
                    "Rapid mitotic division of muscle fibers during performance",
                    "Accumulation of DNA in the sarcoplasm"
                ],
                "ans": 1,
                "solution": "Step 1: Muscle fibers contain sarcomeres composed of thin actin and thick myosin protein filaments.\nStep 2: Myosin heads bind to actin and perform power strokes driven by ATP produced in abundant muscle mitochondria.\nStep 3: This sliding filament mechanism generates tension supporting demanding postures."
            },
            {
                "q": "37. In 2016, synthetic biologists at the J. Craig Venter Institute created 'JCVI-syn3.0'. What was the primary scientific significance of this organism?",
                "options": [
                    "It was the first multicellular animal engineered with chloroplasts",
                    "It was a viable, replicating cell booted up using a chemically synthesized minimal genome of only 473 genes",
                    "It proved that cells can survive without any DNA",
                    "It lived entirely on nuclear radiation"
                ],
                "ans": 1,
                "solution": "Step 1: JCVI-syn3.0 was engineered to identify the bare minimum set of genes necessary for autonomous cellular life.\nStep 2: Scientists chemically synthesized a 531-kilobase genome containing only 473 genes and booted it up in an empty bacterial cytoplasm.\nStep 3: It proved that an autonomous replicating cell can function with a minimal synthetic genome."
            },
            {
                "q": "38. Approximately what proportion of the 473 essential genes in the minimal synthetic cell JCVI-syn3.0 have biological functions that are still completely unknown to science?",
                "options": ["0% (all are known)", "About 31% (149 genes)", "100%", "Less than 1%"],
                "ans": 1,
                "solution": "Step 1: Out of 473 genes essential for JCVI-syn3.0's survival, 149 genes (~31%) had no known biological function at the time of publication.\nStep 2: This demonstrates that even in the simplest life form, nearly one-third of essential life processes remain uncharacterized cytological frontiers.\nStep 3: Correct answer is ~31% (149 genes)."
            },
            {
                "q": "39. Which of the following examples represents an eco-friendly, zero-cost material choice for constructing a 3D model of a plant cell for a science exhibition?",
                "options": [
                    "Single-use non-recyclable plastic thermocol sheets",
                    "Discarded scrap cardboard for the cell wall and edible dough or clay with dried seeds for organelles",
                    "Toxic lead-based paint on synthetic styrofoam",
                    "Imported non-biodegradable resin molds"
                ],
                "ans": 1,
                "solution": "Step 1: Competency C-8.1 emphasizes creativity using low-cost, eco-friendly, biodegradable materials.\nStep 2: Using discarded cardboard boxes for cell walls and natural clay/dough with lentils, beans, and seeds for organelles models cell biology sustainably without plastic pollution.\nStep 3: Correct answer is statement 2."
            },
            {
                "q": "40. Why does meiosis produce gametes with half the chromosome number (haploid, n) rather than the full somatic number (diploid, 2n)?",
                "options": [
                    "To save energy inside the reproductive organs",
                    "So that upon fertilization (fusion of sperm and egg), the resulting zygote restores the constant diploid (2n) chromosome count of the species",
                    "Because gametes are too small to hold 46 chromosomes",
                    "To ensure daughter cells have no DNA"
                ],
                "ans": 1,
                "solution": "Step 1: Sexual reproduction involves the fusion of male and female gametes (sperm + egg).\nStep 2: If gametes were diploid (2n), fertilization would double the chromosome count in every generation (4n, 8n, etc.).\nStep 3: Meiosis halves the chromosome count to n (haploid), ensuring that upon fertilization (n + n = 2n), the species-specific chromosome number is conserved."
            }
        ]
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(SLIDES)} slides, {len(QUIZZES)} quiz challenge slides.")
    total_cp = sum(len(s['checkpoints']) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    total_qz = sum(len(q['questions']) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, f"Expected 16 content slides, got {len(SLIDES)}"
    assert total_cp == 32, f"Expected 32 checkpoints, got {total_cp}"
    assert len(QUIZZES) == 4, f"Expected 4 quiz challenge slides, got {len(QUIZZES)}"
    assert total_qz == 40, f"Expected 40 quiz questions, got {total_qz}"
    print("All cell biology data assertions passed cleanly!")


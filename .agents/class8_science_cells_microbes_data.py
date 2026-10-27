# Class 8 Science Chapter 2: Cell Structure, Variation, and Microorganisms
# Complete data specification with 20 slides, 32 in-slide checkpoints, and 40 mastery questions with step-by-step solutions.

SLIDES_DATA = [
    {
        "id": 1,
        "title": "Discovery of Cells",
        "subtitle": "Micrographia, Robert Hooke (1665), and the First Glimpse",
        "badge": "Cellular History",
        "narration": "Welcome to Chapter 2: The Cell and Microorganisms. The human eye cannot resolve structures smaller than one-tenth of a millimeter. For centuries, the building blocks of living organisms remained completely hidden. That changed in 1665 when British polymath Robert Hooke examined thin shavings of bottle cork under a primitive compound microscope magnifying 200 to 300 times.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                The human eye has an optical resolution limit of approximately $0.1\text{ mm}$ ($100\,\mu\text{m}$). Any biological structure smaller than this threshold cannot be distinguished without optical assistance.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wider mb-1">Robert Hooke (1665)</h4>
                    <p class="text-xs text-slate-300">
                        In 1665, <strong>Robert Hooke</strong> observed thin slices of dead bottle cork under a compound microscope magnifying $200\times$ to $300\times$. He noticed a honeycomb pattern of tiny, hollow compartments and published his drawings in <em>Micrographia</em>.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-1">Origin of the Word 'Cell'</h4>
                    <p class="text-xs text-slate-300">
                        Hooke named these tiny boxes <strong>cells</strong> (from Latin <em>cellula</em>, meaning 'a small room'), because they reminded him of the small bare rooms inhabited by monks in a monastery. Hooke was actually observing the rigid, dead cellulose cell walls of plant tissue.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 leading-relaxed">
                Hooke's landmark publication laid the foundation for biological cytology, sparking a scientific revolution to explore what lies inside these miniature chambers.
            </p>
        """,
        "key_points": [
            "The unaided human eye cannot resolve microscopic objects smaller than ~0.1 mm (100 μm).",
            "In 1665, Robert Hooke published 'Micrographia' after examining cork slices under a 200×–300× microscope.",
            "Hooke coined the word 'cell' (from Latin 'cellula', little room) to describe the honeycomb compartments.",
            "The cork compartments Hooke observed were actually empty cellulose walls of dead plant bark cells."
        ],
        "sim_id": "hooke_cork_microscope_sim",
        "checkpoints": [
            {
                "question": "What biological material was Robert Hooke examining when he first coined the term 'cell' in 1665?",
                "options": [
                    "Thin slices of dead bottle cork bark",
                    "Living blood droplets from a frog",
                    "Fresh green onion peel",
                    "Pond water animalcules"
                ],
                "correct": 0,
                "explanation": "Robert Hooke examined thin shavings of dead bottle cork (tree bark tissue) under his microscope, noticing box-like compartments that he named cells."
            },
            {
                "question": "What was the magnification range of the compound microscope used by Robert Hooke in his 1665 study?",
                "options": [
                    "200 to 300 times (200×–300×)",
                    "10 to 20 times (10×–20×)",
                    "1,000,000 times (1,000,000×)",
                    "5 to 8 times (5×–8×)"
                ],
                "correct": 0,
                "explanation": "Hooke's compound microscope magnified specimens between 200× and 300×, sufficient to clearly resolve plant cell walls in cork."
            }
        ]
    },
    {
        "id": 2,
        "title": "Leeuwenhoek & Modern Lenses",
        "subtitle": "From Animalcules to 1,000,000× Electron Microscopes",
        "badge": "Microscopy Frontiers",
        "narration": "While Hooke saw dead cell walls, Dutch lensmaker Antonie van Leeuwenhoek was the first human to observe living, swimming cells. In the late 1660s and 1670s, his precision glass spheres revealed bacteria and red blood cells. Fast forward to the modern era: advanced transmission and scanning electron microscopes can magnify up to one million times, revealing individual ribosomes and DNA macromolecules.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                The evolution of microscopy progressed from simple handcrafted glass beads to electromagnetic lenses that focus high-velocity electron beams.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider mb-1">Father of Microbiology</h4>
                    <p class="text-xs text-slate-300">
                        In the 1660s–1670s, <strong>Antonie van Leeuwenhoek</strong> hand-ground tiny biconvex lenses with exceptional optical clarity. He became the first person to describe <strong>living bacteria</strong>, free-living protozoa, and red blood cells, earning the title <em>Father of Microbiology</em>.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-indigo-500/30">
                    <h4 class="text-xs font-bold text-indigo-400 uppercase tracking-wider mb-1">Electron Microscopes (~1,000,000×)</h4>
                    <p class="text-xs text-slate-300">
                        While light microscopes are limited by the wavelength of visible light (~$1500\times$ max), modern <strong>Electron Microscopes (TEM & SEM)</strong> use electron beams with sub-nanometer wavelengths, achieving up to <strong>1,000,000×</strong> magnification to photograph subcellular organelles and viral capsids.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 leading-relaxed">
                From Hooke's cork to the modern electron microscope, humanity unlocked the deepest molecular secrets of life.
            </p>
        """,
        "key_points": [
            "Antonie van Leeuwenhoek (1660s) crafted superior lenses and was the first to see living bacteria and blood cells.",
            "Leeuwenhoek is universally recognized as the 'Father of Microbiology'.",
            "Compound light microscopes are limited to ~1500× by the wavelength of visible light photons.",
            "Modern Electron Microscopes magnify up to 1,000,000×, revealing ultra-fine subcellular organelles."
        ],
        "sim_id": "magnification_evolution_sim",
        "checkpoints": [
            {
                "question": "Who is honored as the 'Father of Microbiology' for being the first person to clearly see and describe living bacteria and blood cells?",
                "options": [
                    "Antonie van Leeuwenhoek",
                    "Robert Hooke",
                    "Louis Pasteur",
                    "Alexander Fleming"
                ],
                "correct": 0,
                "explanation": "Antonie van Leeuwenhoek built handcrafted lenses with remarkable clarity and first observed living bacteria, protozoa, and red blood cells."
            },
            {
                "question": "What is the approximate magnification capability of modern high-resolution electron microscopes?",
                "options": [
                    "About 1,000,000 times (1,000,000×)",
                    "About 300 times (300×)",
                    "About 50 times (50×)",
                    "About 2,000 times (2,000×)"
                ],
                "correct": 0,
                "explanation": "Modern electron microscopes use focused beams of electrons to achieve magnifications around 1,000,000×, resolving ultra-fine organelle structures."
            }
        ]
    },
    {
        "id": 3,
        "title": "The Cell Triad",
        "subtitle": "The 3 Fundamental Pillars: Membrane, Cytoplasm, and Nucleus",
        "badge": "Cell Biology Basics",
        "narration": "Regardless of whether a cell belongs to a human, a tiger, a banyan tree, or an amoeba, every typical eukaryotic cell shares three fundamental parts that make life possible: the outer cell membrane, the jelly-like internal cytoplasm, and the central control nucleus.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                All living organisms are composed of one or more cells. The cell is the structural and functional unit of life. A typical cell contains three core components:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-3 text-xs">
                <div class="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400 block mb-1">1. Cell Membrane</span>
                    <p class="text-slate-300">The flexible outer boundary that encloses the interior contents, separates cells from each other, and regulates molecular traffic.</p>
                </div>
                <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/30">
                    <span class="font-bold text-emerald-400 block mb-1">2. Cytoplasm</span>
                    <p class="text-slate-300">The transparent, gelatinous matrix filling the cell interior where biochemical metabolic reactions take place.</p>
                </div>
                <div class="p-3 rounded-lg bg-purple-950/20 border border-purple-500/30">
                    <span class="font-bold text-purple-400 block mb-1">3. Nucleus</span>
                    <p class="text-slate-300">The prominent central sphere that directs and coordinates all cellular activities, protein synthesis, and reproduction.</p>
                </div>
            </div>
            <p class="text-xs text-slate-400 leading-relaxed">
                These three components work in seamless harmony: the membrane protects, the cytoplasm metabolizes, and the nucleus commands.
            </p>
        """,
        "key_points": [
            "All living organisms are made up of basic microscopic structural units called cells.",
            "The 3 fundamental components of a typical eukaryotic cell are the cell membrane, cytoplasm, and nucleus.",
            "The cell membrane encloses and demarcates the living contents from the external environment.",
            "The cytoplasm hosts metabolic life processes, while the nucleus governs cell regulation."
        ],
        "sim_id": "cell_triad_anatomy_sim",
        "checkpoints": [
            {
                "question": "What are the three fundamental components found in every typical animal and plant cell?",
                "options": [
                    "Cell membrane, cytoplasm, and nucleus",
                    "Cell wall, chloroplast, and flagellum",
                    "Hemoglobin, bone marrow, and hair",
                    "Root, stem, and leaf"
                ],
                "correct": 0,
                "explanation": "Every typical cell contains the outer cell membrane (plasma membrane), the internal jelly-like cytoplasm, and the central control nucleus."
            },
            {
                "question": "Which statement correctly describes the overarching biological principle of cells?",
                "options": [
                    "All living beings are made up of cells, which form the basic unit of life",
                    "Only animals have cells; plants are made of pure stone",
                    "Cells are non-living minerals formed in dry rocks",
                    "Cells can only be created inside chemical factories"
                ],
                "correct": 0,
                "explanation": "Cells are the fundamental structural and functional building blocks of all living organisms, from single-celled bacteria to massive trees and humans."
            }
        ]
    },
    {
        "id": 4,
        "title": "Membrane & Cytoplasm",
        "subtitle": "Selective Permeability and the Metabolic Matrix",
        "badge": "Cytological Physiology",
        "narration": "Let us take a closer look at the cell's outer gate and inner factory floor. The cell membrane is porous and selectively permeable: it acts like an intelligent security checkpoint, welcoming essential sugars and minerals while barring toxins and expelling waste. Inside lies the cytoplasm, a rich chemical soup loaded with proteins, fats, carbohydrates, and mineral salts.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                The cell membrane and cytoplasm form a dynamic biochemical transport and reaction system.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Cell Membrane (Plasma Membrane)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        A thin, flexible, and <strong>porous</strong> phospholipid bilayer. It is <strong>selectively permeable</strong>, meaning it strictly regulates the passage of substances: admitting vital nutrients (glucose, oxygen, ions) into the cell while permitting metabolic waste products (carbon dioxide, urea) to exit. It also maintains cell shape and integrity.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-teal-500/30">
                    <h4 class="font-bold text-teal-300 text-sm mb-1">Cytoplasm: The Life Matrix</h4>
                    <p class="text-slate-300 leading-relaxed">
                        A jelly-like fluid composed of water ($~80\%$) and dissolved vital compounds: <strong>proteins, carbohydrates, fats, and mineral salts</strong>. Almost all cellular life processes, glycolysis, enzyme reactions, and waste packaging occur suspended within this colloidal soup.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Without the membrane's selective permeability, toxic wastes would accumulate and kill the cell, or essential nutrients would leak away.
            </p>
        """,
        "key_points": [
            "The cell membrane is a porous, selectively permeable barrier enclosing the cytoplasm and nucleus.",
            "It controls inward transport of vital nutrients and outward excretion of metabolic waste materials.",
            "Cytoplasm is an aqueous colloidal matrix containing vital proteins, fats, carbohydrates, and salts.",
            "Most foundational biochemical life processes and enzyme reactions occur inside the cytoplasm."
        ],
        "sim_id": "membrane_transport_cytoplasm_sim",
        "checkpoints": [
            {
                "question": "Why is the cell membrane described as 'porous' and 'selectively permeable'?",
                "options": [
                    "It allows essential nutrients inside while letting metabolic wastes out, blocking harmful substances",
                    "It allows all materials, both toxic and beneficial, to pass completely unrestricted",
                    "It completely seals the cell like solid glass so nothing can enter or leave",
                    "It only allows air bubbles to enter during sleep"
                ],
                "correct": 0,
                "explanation": "Selective permeability means the porous plasma membrane regulates molecular movement, admitting nutrients and expelling wastes while maintaining internal cellular homeostasis."
            },
            {
                "question": "What essential biomolecules and compounds are dissolved within the jelly-like matrix of cytoplasm?",
                "options": [
                    "Proteins, carbohydrates, fats, and mineral salts",
                    "Pure sand and crushed granite",
                    "Solid iron bars and plastic polymers",
                    "Dry nitrogen gas only"
                ],
                "correct": 0,
                "explanation": "Cytoplasm is a nutrient-rich aqueous matrix containing dissolved proteins, carbohydrates, lipids, and essential mineral ions that fuel biochemical metabolic reactions."
            }
        ]
    },
    {
        "id": 5,
        "title": "The Nucleus",
        "subtitle": "The Master Control Center of Cellular Life and Growth",
        "badge": "Cellular Command",
        "narration": "Deep in the center of the cell lies its brain and command center: the nucleus. It oversees every decision the cell makes—when to synthesize proteins, when to absorb energy, when to grow, and when to divide. Inside, it safeguards the hereditary blueprint of life.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                The <strong>nucleus</strong> is typically the largest and most prominent spherical organelle in eukaryotic cells, acting as the executive control headquarters.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-purple-500/30">
                    <h4 class="font-bold text-purple-300 text-sm mb-1">Regulation of Activities</h4>
                    <p class="text-slate-300 leading-relaxed">
                        The nucleus regulates all biochemical activities, nutrient metabolism, cellular respiration rates, and structural growth. It sends chemical messenger signals (RNA) through porous nuclear membranes into the cytoplasm to instruct ribosomes to build specific functional proteins.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-indigo-500/30">
                    <h4 class="font-bold text-indigo-300 text-sm mb-1">Genetic Material & Chromatin</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Inside the nucleoplasm lies a network of thread-like <strong>chromatin</strong>, which condenses into rod-shaped <strong>chromosomes</strong> during cell division. These chromosomes carry genes made of DNA that pass hereditary characteristics from parent cells to offspring.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                If the nucleus is surgically removed from an amoeba (enucleation), the cell ceases protein production, stops growing, and dies within a few days.
            </p>
        """,
        "key_points": [
            "The nucleus is the master control center responsible for regulating all cellular activities and growth.",
            "It is surrounded by a double-layered nuclear membrane studded with nuclear pores.",
            "The nucleus houses chromatin fibers that condense into chromosomes containing hereditary DNA genes.",
            "A cell deprived of its nucleus loses its ability to divide or synthesize vital proteins and eventually perishes."
        ],
        "sim_id": "nucleus_command_center_sim",
        "checkpoints": [
            {
                "question": "What is the primary function of the nucleus in a living cell?",
                "options": [
                    "Regulating all cellular activities, growth, and protein synthesis",
                    "Absorbing direct sunlight like a solar panel",
                    "Pumping red blood through the bones",
                    "Grinding solid food like human teeth"
                ],
                "correct": 0,
                "explanation": "The nucleus acts as the command center of the cell, directing growth, metabolic operations, protein synthesis, and cellular reproduction."
            },
            {
                "question": "What happens to a single-celled organism like Amoeba if its nucleus is carefully removed?",
                "options": [
                    "It stops growing, ceases cellular operations, and soon dies",
                    "It instantly turns into a giant plant",
                    "It divides into twenty healthy daughter cells",
                    "It starts flying through the air"
                ],
                "correct": 0,
                "explanation": "Without the nucleus, the cell loses the master instructions needed to make proteins, regulate enzymes, and divide, causing it to die."
            }
        ]
    },
    {
        "id": 6,
        "title": "Cell Wall & Plant Features",
        "subtitle": "Cell Wall, Plastids (Chloroplasts), and Large Central Vacuoles",
        "badge": "Plant Cytology",
        "narration": "Why do giant trees stand tall against ferocious winds without bones, while animal bodies collapse into soft tissue? The answer lies in plant-specific structures: the rigid cellulose cell wall, green photosynthetic plastids called chloroplasts, and massive central vacuoles that maintain internal hydraulic turgor pressure.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Plant cells possess distinctive structural organelles absent in animal cells that provide rigidity, autotrophic nutrition, and hydraulic turgor stability.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-2 text-xs">
                <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/30">
                    <span class="font-bold text-emerald-400 block mb-1">1. Cell Wall</span>
                    <p class="text-slate-300">An extra rigid outer coat located outside the cell membrane in plant, fungal, and bacterial cells. Made of tough <strong>cellulose</strong> in plants, it confers structural strength, fixes cell shape, and protects against high osmotic pressures.</p>
                </div>
                <div class="p-3 rounded-lg bg-lime-950/20 border border-lime-500/30">
                    <span class="font-bold text-lime-400 block mb-1">2. Plastids (Chloroplasts)</span>
                    <p class="text-slate-300">Double-membrane organelles. <strong>Chloroplasts</strong> contain green <strong>chlorophyll</strong> pigments that trap solar energy for photosynthesis. Non-green plastids (leucoplasts & chromoplasts) store starches, oils, and pigments in fruits and roots.</p>
                </div>
                <div class="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400 block mb-1">3. Large Central Vacuole</span>
                    <p class="text-slate-300">A giant fluid-filled sac occupying up to $90\%$ of mature plant cell volume. Stores cell sap (sugars, amino acids, minerals), isolates waste, and exerts outward <strong>turgor pressure</strong> keeping leaves crisp and upright.</p>
                </div>
            </div>
        """,
        "key_points": [
            "The cell wall is an extra protective outer coat found in plant, fungal, and bacterial cells (absent in animals).",
            "In plants, the cell wall is composed of tough cellulose, providing rigidity and mechanical support.",
            "Plastids are plant organelles; chloroplasts contain green chlorophyll for photosynthesis, while other plastids store food.",
            "A large central vacuole stores water and nutrients, removes waste, and maintains turgidity and cell shape."
        ],
        "sim_id": "plant_vs_animal_organelles_sim",
        "checkpoints": [
            {
                "question": "Which of the following structures is found in plant cells but is completely ABSENT in animal cells?",
                "options": [
                    "A rigid outer cell wall and chloroplasts",
                    "Cell membrane",
                    "Cytoplasm",
                    "Nucleus"
                ],
                "correct": 0,
                "explanation": "Plant cells possess a rigid cellulose cell wall and plastids (chloroplasts) for photosynthesis, both of which are absent in animal cells."
            },
            {
                "question": "What is the primary role of the large fluid-filled central vacuole in mature plant cells?",
                "options": [
                    "Storing water and nutrients, removing waste, and maintaining turgor pressure to keep the cell rigid",
                    "Generating electrical current to shock insects",
                    "Producing sound waves so plants can talk",
                    "Absorbing nitrogen gas directly from clouds"
                ],
                "correct": 0,
                "explanation": "The large central vacuole stores cell sap, sequesters waste, and pushes outward against the cell wall (turgor pressure), keeping plant stems and leaves upright."
            }
        ]
    },
    {
        "id": 7,
        "title": "Bacterial Nucleoid",
        "subtitle": "Prokaryotic Simplicity vs Eukaryotic Compartmentalization",
        "badge": "Prokaryotic Genetics",
        "narration": "Not every cell packages its genetic blueprints inside a neat, membrane-bound sphere. In bacteria, the DNA floats freely in direct contact with the cytoplasm in an irregular central region called the nucleoid. This fundamental difference splits all life on Earth into two great empires: prokaryotes and eukaryotes.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                One of the most profound evolutionary distinctions in biology is the presence or absence of a true, membrane-bound nucleus.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Bacterial Cells (Prokaryotes)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Bacterial cells do not possess a well-defined nucleus or nuclear envelope. Instead, their genetic material consists of a single circular chromosome located in an un-enclosed, irregular central zone termed the <strong>nucleoid</strong>.<br>
                        They lack membrane-bound organelles (no mitochondria, chloroplasts, or endoplasmic reticulum).
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Plant & Animal Cells (Eukaryotes)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Eukaryotic cells possess a true, double-membrane nucleus that houses linear chromosomes wrapped around histone proteins. The interior cytoplasm is subdivided into specialized membrane-bound compartments (organelles) that isolate chemical reactions.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Bacteria also feature a cell wall containing peptidoglycan, a plasma membrane, and ribosomes, allowing rapid binary fission.
            </p>
        """,
        "key_points": [
            "Bacterial cells lack a membrane-bound nucleus and nuclear envelope.",
            "The un-enclosed region where bacterial circular DNA resides is called the nucleoid.",
            "Organisms lacking a membrane-bound nucleus are called prokaryotes (e.g., bacteria, blue-green algae).",
            "Organisms with a well-defined membrane-bound nucleus are called eukaryotes (plants, animals, fungi, protozoa)."
        ],
        "sim_id": "prokaryote_vs_eukaryote_sim",
        "checkpoints": [
            {
                "question": "What is the un-enclosed region containing genetic material in bacterial cells called?",
                "options": [
                    "Nucleoid",
                    "True nucleus",
                    "Vacuole",
                    "Centrosome"
                ],
                "correct": 0,
                "explanation": "Bacteria do not have a nuclear membrane. Their circular genetic DNA lies directly in an un-enclosed region of cytoplasm called the nucleoid."
            },
            {
                "question": "Which of the following organisms is a prokaryote lacking a membrane-bound nucleus?",
                "options": [
                    "Bacterium (e.g., Lactobacillus or E. coli)",
                    "Amoeba (Protozoan)",
                    "Onion peel cell (Plant)",
                    "Human cheek epithelial cell (Animal)"
                ],
                "correct": 0,
                "explanation": "Bacteria are prokaryotes with a nucleoid and no nuclear membrane. Amoeba, onion cells, and human cells are all eukaryotes with true nuclei."
            }
        ]
    },
    {
        "id": 8,
        "title": "Cell Shapes & Function",
        "subtitle": "Spindle Muscle Cells, Branched Neurons, and Specialization",
        "badge": "Morphology & Specialization",
        "narration": "Cells are not boring little round balls. Their shapes, sizes, and internal structures are exquisitely adapted to the specific jobs they perform in the body. Long, branched neurons fire electrical signals across distances, spindle-shaped muscle fibers contract to produce motion, and biconcave red blood cells squeeze through narrow capillaries.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                In multicellular organisms, cells undergo <strong>differentiation</strong>: their shape, size, and internal architecture are tailored to maximize functional efficiency.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-2 text-xs">
                <div class="p-3 rounded-lg bg-rose-950/20 border border-rose-500/30">
                    <span class="font-bold text-rose-400 block mb-1">1. Muscle Cells (Myocytes)</span>
                    <p class="text-slate-300">Elongated and <strong>spindle-shaped</strong> (tapered at both ends). Packed with actin and myosin protein filaments that contract and relax to generate physical pulling forces and body motion.</p>
                </div>
                <div class="p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/30">
                    <span class="font-bold text-indigo-400 block mb-1">2. Nerve Cells (Neurons)</span>
                    <p class="text-slate-300">Remarkably <strong>long and branched</strong> with thin dendrites and an extended axon (up to 1 meter long). Designed to transmit electrical impulses rapidly across the body like biological telephone wires.</p>
                </div>
                <div class="p-3 rounded-lg bg-red-950/20 border border-red-500/30">
                    <span class="font-bold text-red-400 block mb-1">3. Red Blood Cells (RBCs)</span>
                    <p class="text-slate-300">Spherical, <strong>biconcave disc-shaped</strong> and lack a nucleus at maturity. This disc shape maximizes surface area for rapid oxygen diffusion and allows cells to flex through microscopic capillaries.</p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                White blood cells (like Amoeba) can constantly change their shape to squeeze through capillary walls (diapedesis) and engulf bacteria.
            </p>
        """,
        "key_points": [
            "The specific shape, size, and structure of a cell directly correspond to its functional role.",
            "Muscle cells are spindle-shaped (tapered ends) to contract and generate mechanical force.",
            "Nerve cells (neurons) are long and branched to transmit electrical nerve impulses across long distances.",
            "Red blood cells are biconcave discs optimized for oxygen exchange and flexible capillary passage."
        ],
        "sim_id": "cell_shapes_specialization_sim",
        "checkpoints": [
            {
                "question": "Why do nerve cells (neurons) have an elongated shape with numerous branching dendrites?",
                "options": [
                    "To receive and pass electrical impulses quickly over long distances across the body",
                    "To store heavy fat molecules under the skin",
                    "To absorb sunlight for photosynthesis",
                    "To pump blood to the lungs"
                ],
                "correct": 0,
                "explanation": "The elongated axon and branched dendrites of neurons allow rapid transmission of electrical impulses from sensory receptors to the brain and muscles."
            },
            {
                "question": "What is the characteristic shape of smooth muscle cells in animals?",
                "options": [
                    "Spindle-shaped (elongated with pointed, tapered ends)",
                    "Perfect square cubes",
                    "Hollow circular rings with holes",
                    "Star-shaped with sharp crystal corners"
                ],
                "correct": 0,
                "explanation": "Smooth muscle cells are spindle-shaped (fusiform), with a wider central body containing the nucleus and tapered ends, optimized for contracting along one axis."
            }
        ]
    },
    {
        "id": 9,
        "title": "Cell Sizes & Ostrich Egg",
        "subtitle": "From Micrometers to the Largest Known Single Cell (170 mm)",
        "badge": "Cytological Scales",
        "narration": "How small can a cell be, and how big can a single cell grow? While the smallest bacteria measure just a fraction of a micrometer, the living world boasts a giant single cell that you can hold in your hand: the yolk of an ostrich egg, measuring up to 170 millimeters across!",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Cell dimensions span an astronomical range across living kingdoms, varying by a factor of over $100,000$.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Smallest Cells (Mycoplasma & Bacteria)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        The smallest known free-living cells are <em>Mycoplasma</em> (PPLO), measuring only $0.1\,\mu\text{m}$ to $0.3\,\mu\text{m}$ in diameter. Typical bacteria measure between $0.5\,\mu\text{m}$ and $5\,\mu\text{m}$, invisible to the human eye.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Largest Single Cell: The Ostrich Egg Yolk</h4>
                    <p class="text-slate-300 leading-relaxed">
                        The unfertilized egg of an ostrich holds the world record as the largest known single cell. Its central yolk measures <strong>$130\text{ mm}$ to $170\text{ mm}$ across</strong> ($13\text{ cm}$ to $17\text{ cm}$), weighing over $1.5\text{ kg}$. It can be observed clearly without any magnifying tool!
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Remember: the overall size of an organism depends on the <strong>total number of cells</strong>, not the individual size of its cells. An elephant's kidney cell is roughly the same size as a mouse's kidney cell!
            </p>
        """,
        "key_points": [
            "Cell sizes range from 0.1 μm (Mycoplasma) up to 170 mm (Ostrich egg yolk).",
            "The yolk of an unfertilized ostrich egg is the largest known single cell in the living world (130–170 mm diameter).",
            "Organism body size depends on the total count of cells, not on cell volume.",
            "Cells remain microscopic because a high surface-area-to-volume ratio is required for nutrient diffusion."
        ],
        "sim_id": "cell_size_scale_comparator_sim",
        "checkpoints": [
            {
                "question": "What holds the biological record as the largest known single cell in the living world?",
                "options": [
                    "The yolk of an ostrich egg (130 mm to 170 mm in diameter)",
                    "A blue whale liver cell",
                    "A red kangaroo brain neuron",
                    "An elephant skin cell"
                ],
                "correct": 0,
                "explanation": "The yolk of an unfertilized ostrich egg is a single gigantic cell measuring 130 to 170 mm in diameter, visible to the unaided human eye."
            },
            {
                "question": "Does a large animal like an elephant have substantially larger individual cells than a small animal like a mouse?",
                "options": [
                    "No, their individual cells are of similar size; the elephant simply has billions more cells",
                    "Yes, elephant cells are as large as basketballs",
                    "No, mouse cells are 500 times larger than elephant cells",
                    "Yes, elephant cells contain solid bone inside their cytoplasm"
                ],
                "correct": 0,
                "explanation": "Cell sizes are determined by diffusion physics and are similar across mammals. An elephant is larger simply because it possesses vastly more total cells, not larger cells."
            }
        ]
    },
    {
        "id": 10,
        "title": "Levels of Organisation",
        "subtitle": "Cell → Tissue → Organ → Organ System → Organism",
        "badge": "Biological Hierarchy",
        "narration": "How do trillions of cells cooperate to build a living human or an oak tree? Life organizes itself into an elegant structural hierarchy. Every complex multicellular organism starts its existence as just a single fertilized egg cell that divides repeatedly, specializing into tissues, organs, and organ systems.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Multicellular life follows a strict structural ladder of biological organization, where each tier represents an emergent level of complexity:
            </p>
            <div class="space-y-2 text-xs my-2">
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-cyan-500/30 flex items-center gap-3">
                    <span class="font-mono font-bold text-cyan-400 shrink-0">1. Cell</span>
                    <span class="text-slate-300">The basic building block of life (e.g., muscle cell, epithelial cell, root hair cell).</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-teal-500/30 flex items-center gap-3">
                    <span class="font-mono font-bold text-teal-400 shrink-0">2. Tissue</span>
                    <span class="text-slate-300">A group of similar cells working together to perform a specific function (e.g., muscular tissue, vascular xylem).</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-emerald-500/30 flex items-center gap-3">
                    <span class="font-mono font-bold text-emerald-400 shrink-0">3. Organ</span>
                    <span class="text-slate-300">Different tissues integrated together to perform major tasks (e.g., stomach, heart, lungs, leaf, root).</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-indigo-500/30 flex items-center gap-3">
                    <span class="font-mono font-bold text-indigo-400 shrink-0">4. Organ System</span>
                    <span class="text-slate-300">A coordinated team of organs carrying out comprehensive life functions (e.g., digestive system, circulatory system).</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-purple-500/30 flex items-center gap-3">
                    <span class="font-mono font-bold text-purple-400 shrink-0">5. Organism</span>
                    <span class="text-slate-300">The complete living entity composed of cooperating organ systems (e.g., human, tiger, mango tree).</span>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                All complex organisms begin as a <strong>single cell (zygote)</strong> that undergoes millions of successive divisions and cell differentiations.
            </p>
        """,
        "key_points": [
            "The hierarchy of life follows: Cell → Tissue → Organ → Organ System → Organism.",
            "A tissue is a cooperative group of specialized cells performing a common task.",
            "An organ is composed of multiple tissues; an organ system consists of coordinating organs.",
            "Every complex multicellular organism develops from a single fertilized egg (zygote) through repeated divisions."
        ],
        "sim_id": "biological_hierarchy_ladder_sim",
        "checkpoints": [
            {
                "question": "Which of the following represents the correct biological hierarchy of organization from simplest to most complex?",
                "options": [
                    "Cell → Tissue → Organ → Organ system → Organism",
                    "Organism → Organ → Tissue → Cell → Organ system",
                    "Tissue → Cell → Organism → Organ → Organ system",
                    "Cell → Organ → Tissue → Organism → Organ system"
                ],
                "correct": 0,
                "explanation": "Life builds progressively: similar cells form tissues, tissues form organs, organs form organ systems, and organ systems form the complete organism."
            },
            {
                "question": "From what single starting entity does a complex multicellular organism (such as a human or horse) develop?",
                "options": [
                    "A single fertilized egg cell (zygote) that divides repeatedly",
                    "A cluster of soil minerals glued by water",
                    "An adult organ system formed out of dust",
                    "A group of hundred different dead animals"
                ],
                "correct": 0,
                "explanation": "All complex multicellular creatures start their life as a single fertilized egg cell (zygote) that divides repeatedly and differentiates into trillions of specialized cells."
            }
        ]
    },
    {
        "id": 11,
        "title": "The Microbial World",
        "subtitle": "Ubiquity, Unicellular vs Multicellular, and Acellular Viruses",
        "badge": "Microbial Biosphere",
        "narration": "Microorganisms are the true rulers of Earth. They thrive everywhere—in rich fertile soil, fresh river water, the air we breathe, boiling geothermal hot springs, subzero polar glaciers, and deep inside human intestines. Some are unicellular, some form multicellular filaments, and viruses represent acellular parasites on the border of life.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Microorganisms encompass an immense range of living forms that colonize every ecological niche on the planet.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-2.5 my-2 text-xs">
                <div class="p-3 rounded-lg bg-amber-950/20 border border-amber-500/30">
                    <span class="font-bold text-amber-400 block mb-1">1. Ubiquitous Habitats</span>
                    <p class="text-slate-300">Microbes survive in extreme environments: boiling hot springs ($>80^\circ\text{C}$), frozen Antarctic ice sheets, hyper-saline lakes, deep seabed crust, and inside animal digestive tracts.</p>
                </div>
                <div class="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400 block mb-1">2. Unicellular vs Multicellular</span>
                    <p class="text-slate-300"><strong>Unicellular:</strong> Entire organism is a single standalone cell (Bacteria, <em>Amoeba</em>, <em>Paramecium</em>, Yeast).<br><strong>Multicellular:</strong> Many cells cooperate as colonies or filaments (molds like <em>Rhizopus</em>, filamentous algae like <em>Spirogyra</em>).</p>
                </div>
                <div class="p-3 rounded-lg bg-purple-950/20 border border-purple-500/30">
                    <span class="font-bold text-purple-400 block mb-1">3. Viruses (Acellular)</span>
                    <p class="text-slate-300">Acellular microscopic agents containing DNA or RNA in a protein capsid. Completely inert outside host cells; can only reproduce and multiply inside living host cells, frequently causing diseases.</p>
                </div>
            </div>
        """,
        "key_points": [
            "Microorganisms exist in soil, water, air, thermal hot springs, snow zones, and inside animal bodies.",
            "They can be unicellular (Bacteria, Amoeba) or multicellular (certain algae and fungi).",
            "Viruses are microscopic and acellular entities that reproduce strictly inside living host cells.",
            "Viruses lack cellular metabolic machinery and often cause disease in humans, animals, and plants."
        ],
        "sim_id": "microbial_ubiquity_habitats_sim",
        "checkpoints": [
            {
                "question": "Which of the following is an example of an acellular entity that can multiply ONLY inside a living host cell?",
                "options": [
                    "A virus (e.g., Influenza or Poliovirus)",
                    "Amoeba proteus",
                    "Lactobacillus bacterium",
                    "Yeast (Saccharomyces)"
                ],
                "correct": 0,
                "explanation": "Viruses are acellular (lacking cellular structure and cytoplasm) and must hijack a living host cell's machinery to replicate."
            },
            {
                "question": "Where can living microorganisms be found on Earth?",
                "options": [
                    "Everywhere—in soil, water, air, hot springs, snow zones, and inside animal bodies",
                    "Exclusively in clean hospital operating rooms",
                    "Only at the very center of the Earth's iron core",
                    "Only inside commercial grocery stores"
                ],
                "correct": 0,
                "explanation": "Microorganisms are ubiquitous, colonizing soil, water, atmosphere, thermal springs, polar glaciers, and the bodies of animals and plants."
            }
        ]
    },
    {
        "id": 12,
        "title": "Decomposers & Biogas",
        "subtitle": "Nature's Waste Recyclers and Clean Renewable Energy",
        "badge": "Ecological Biotechnology",
        "narration": "What happens to fallen leaves, food scraps, and organic farm waste? Soil bacteria and fungi act as nature's recycling squad, breaking down complex organic molecules into rich, black manure. In sealed, oxygen-free digesters, specialized anaerobic microbes turn that same animal dung into clean-burning biogas.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Microbes play an irreplaceable role in maintaining ecological equilibrium and generating renewable clean fuel through two distinct pathways:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-lime-500/30">
                    <h4 class="font-bold text-lime-300 text-sm mb-1">Environmental Cleanup & Humus</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Saprophytic fungi and bacteria break down complex vegetable waste, fallen leaves, and dead animal remains. They release mineral nutrients back into the soil, forming dark, nutrient-rich <strong>manure (humus)</strong> that enriches farmland without chemical contamination.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-300 text-sm mb-1">Biogas Generation (Methanogens)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        In oxygen-free (anaerobic) underground digesters, specialized microorganisms decompose cattle dung (gobar) and sewage. They release <strong>biogas</strong>, an eco-friendly fuel composed primarily of <strong>methane ($\text{CH}_4$, $55\%-70\%$)</strong> and carbon dioxide ($\text{CO}_2$). The leftover slurry serves as concentrated organic fertilizer.
                    </p>
                </div>
            </div>
        """,
        "key_points": [
            "Fungi and bacteria decompose organic plant and animal waste into simpler, nutrient-rich soil manure.",
            "Anaerobic microorganisms decompose organic matter in oxygen-free digesters to produce biogas.",
            "Biogas consists primarily of clean-burning methane (CH₄) along with carbon dioxide (CO₂).",
            "Biogas plants provide clean cooking fuel and light while generating rich organic bio-fertilizer."
        ],
        "sim_id": "biogas_anaerobic_digester_sim",
        "checkpoints": [
            {
                "question": "What is the primary combustible gas component found in biogas produced by anaerobic microbial digestion?",
                "options": [
                    "Methane (CH₄)",
                    "Oxygen (O₂)",
                    "Helium (He)",
                    "Chlorine (Cl₂)"
                ],
                "correct": 0,
                "explanation": "Biogas is produced by anaerobic bacteria (methanogens) and consists primarily of methane (CH₄, 55%–70%), making it an excellent smokeless fuel."
            },
            {
                "question": "How do saprophytic bacteria and fungi contribute to environmental cleanup in nature?",
                "options": [
                    "By breaking down dead plant and animal remains into simple, nutrient-rich manure",
                    "By turning all tree trunks into solid plastic",
                    "By freezing fallen leaves so they never decay",
                    "By transporting garbage to outer space"
                ],
                "correct": 0,
                "explanation": "Decomposers secrete digestive enzymes that break down fallen leaves and dead organic waste into simple soil nutrients and humus, naturally recycling matter."
            }
        ]
    },
    {
        "id": 13,
        "title": "Fermentation in Foods",
        "subtitle": "Yeast in Bread & Lactobacillus in Curd, Idli, and Dosa",
        "badge": "Culinary Biotechnology",
        "narration": "Step into your kitchen and you are stepping into a microbiology laboratory! The fluffy lightness of baked bread, the sour tang of curd, and the bubbly rise of idli and dosa batter are all created by friendly microbes carrying out fermentation.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Humans have harnessed microbial fermentation for millennia to transform raw grains and milk into digestible, long-lasting foods.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Yeast (Baking & Brewing)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        <em>Yeast</em> is a unicellular fungus. In warm, sugary dough, yeast respires anaerobically:
                        <br><span class="font-mono text-cyan-300 block my-1 font-bold">Glucose → Alcohol + CO₂ ↑ + Energy</span>
                        Bubbles of released <strong>carbon dioxide gas</strong> expand within the dough, making it soft, airy, and fluffy when baked.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Lactobacillus (Dairy & Batter)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        <em>Lactobacillus</em> bacteria ferment milk sugar (lactose) into <strong>lactic acid</strong>. The acid coagulates milk protein (casein), turning milk sour and creating thick curd. They also ferment fermented batters for <strong>idli, dosa, and bhatura</strong>, improving flavor, texture, and B-vitamin content.
                    </p>
                </div>
            </div>
        """,
        "key_points": [
            "Yeast is a unicellular fungus that releases carbon dioxide gas in warm dough, making bread soft and fluffy.",
            "Yeast fermentation also produces small amounts of alcohol, used in commercial brewing.",
            "Lactobacillus bacteria ferment milk lactose into lactic acid, forming thick curd.",
            "Fermentation of traditional batters (idli, dosa, bhatura) improves taste, fluffiness, and nutrient availability."
        ],
        "sim_id": "kitchen_fermentation_lab_sim",
        "checkpoints": [
            {
                "question": "What gas does yeast produce during anaerobic respiration in dough that causes it to rise and become porous?",
                "options": [
                    "Carbon dioxide (CO₂)",
                    "Oxygen (O₂)",
                    "Nitrogen (N₂)",
                    "Methane (CH₄)"
                ],
                "correct": 0,
                "explanation": "Yeast respires anaerobically in dough, releasing carbon dioxide gas bubbles that get trapped in the gluten network, causing the dough to swell and rise."
            },
            {
                "question": "Which bacterium ferments milk into curd and helps ferment idli, dosa, and bhatura batter?",
                "options": [
                    "Lactobacillus",
                    "Rhizobium",
                    "Pseudomonas",
                    "Mycobacterium"
                ],
                "correct": 0,
                "explanation": "Lactobacillus bacteria convert lactose sugar into lactic acid, which curdles milk into curd and provides the tangy fluffiness of idli and dosa batter."
            }
        ]
    },
    {
        "id": 14,
        "title": "Nitrogen Fixers & Algae",
        "subtitle": "Rhizobium Root Nodules, Spirulina, and 50%+ Earth's Oxygen",
        "badge": "Agricultural & Marine Botany",
        "narration": "Plants cannot absorb atmospheric nitrogen gas directly, nor could animals survive without oxygen. In the soil, Rhizobium bacteria in legume root nodules convert air nitrogen into plant food. Meanwhile in our oceans, microscopic algae produce more than half the oxygen in our atmosphere!",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Microbes drive global biochemical cycles that make planetary agriculture and oxygen breathing possible.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-300 text-sm mb-1">Rhizobium & Nitrogen Fixation</h4>
                    <p class="text-slate-300 leading-relaxed">
                        <em>Rhizobium</em> bacteria live symbiotically inside swollen <strong>root nodules</strong> of leguminous crops (peas, beans, gram, lentils). They trap inert atmospheric nitrogen ($\text{N}_2$) and convert it into plant-usable nitrates ($\text{NO}_3^-$), naturally boosting soil fertility without synthetic chemicals.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-teal-500/30">
                    <h4 class="font-bold text-teal-300 text-sm mb-1">Microalgae: Earth's Oxygen Champions</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Aquatic micro-algae (<em>Spirulina</em>, <em>Chlorella</em>, Diatoms) carry out intensive photosynthesis, generating <strong>more than half of Earth's oxygen</strong>! They sustain marine food chains, purify water, and serve as superfoods—<em>Spirulina</em> is packed with proteins, iron, and Vitamin $\text{B}_{12}$.
                    </p>
                </div>
            </div>
        """,
        "key_points": [
            "Rhizobium bacteria reside in legume root nodules, converting atmospheric N₂ into fertile soil nitrates.",
            "Aquatic microalgae (Diatoms, Chlorella, Spirulina) generate more than 50% of the Earth's atmospheric oxygen.",
            "Microalgae form the base of aquatic food chains and aid in wastewater biological purification.",
            "Spirulina is cultivated commercially as a powerful dietary supplement rich in complete proteins and Vitamin B12."
        ],
        "sim_id": "rhizobium_microalgae_lab_sim",
        "checkpoints": [
            {
                "question": "What proportion of Earth's total atmospheric oxygen is produced by aquatic micro-algae like diatoms and phytoplankton?",
                "options": [
                    "More than half (over 50%)",
                    "Less than 1%",
                    "Exactly 5%",
                    "Zero percent"
                ],
                "correct": 0,
                "explanation": "Marine phytoplankton and aquatic micro-algae (such as diatoms) carry out immense photosynthetic activity, producing over half of Earth's oxygen."
            },
            {
                "question": "Which microscopic blue-green alga is commercially cultivated as a protein- and vitamin B12-rich dietary supplement?",
                "options": [
                    "Spirulina",
                    "Amoeba",
                    "Bread mold",
                    "Poliovirus"
                ],
                "correct": 0,
                "explanation": "Spirulina is a nutrient-dense cyanobacterium (microalga) widely consumed worldwide as a health supplement for its high protein, iron, and Vitamin B12 content."
            }
        ]
    },
    {
        "id": 15,
        "title": "Heritage & Modern Pioneers",
        "subtitle": "Vedic 'Krimi' and Ananda Mohan Chakrabarty's Oil-Eating Superbug",
        "badge": "Indian Scientific Heritage",
        "narration": "Long before European microscopes were invented, ancient Indian scholars recognized the existence of invisible living entities. In the Atharvaveda, they described 'Krimi'—microscopic beings categorized as visible and invisible. Fast forward to modern times: Indian-American microbiologist Dr. Ananda Mohan Chakrabarty engineered the world's first patented oil-eating bacterium to clean oceanic spills.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                India has a profound tradition of microbiology spanning ancient philosophical inquiries to landmark 20th-century biotechnology patents.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Ancient Indian Texts & 'Krimi'</h4>
                    <p class="text-slate-300 leading-relaxed">
                        In ancient Indian texts, including the <em>Atharvaveda</em> and Ayurvedic treatises (Charaka Samhita), tiny entities were denoted by the Sanskrit word <strong>Krimi</strong>. These were classified into:
                        <br>• <strong>Drishya:</strong> Visible parasites and organisms.
                        <br>• <strong>Adrishya:</strong> Invisible organisms too tiny to be seen, describing both their beneficial and disease-causing effects.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Ananda Mohan Chakrabarty (1938–2020)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        In 1971, Indian-born scientist <strong>Dr. Ananda Mohan Chakrabarty</strong> developed a specialized genetic strain of <em>Pseudomonas putida</em>. This 'superbug' could digest four separate hydrocarbon fractions of crude oil, rapidly biodegrading oil slicks in marine spills. In 1980, the US Supreme Court granted him the <strong>first-ever patent for a genetically engineered organism</strong> (<em>Diamond v. Chakrabarty</em>).
                    </p>
                </div>
            </div>
        """,
        "key_points": [
            "Ancient Indian Vedas (Atharvaveda) refer to microorganisms as 'Krimi', divided into Drishya (visible) and Adrishya (invisible).",
            "Ayurvedic texts documented both the beneficial and disease-causing roles of unseen Krimi.",
            "Dr. Ananda Mohan Chakrabarty developed an oil-eating bacterium (Pseudomonas putida) in 1971 to treat ocean oil spills.",
            "In 1980, Dr. Chakrabarty was awarded the world's first patent for a genetically modified living organism."
        ],
        "sim_id": "oil_spill_bioremediation_sim",
        "checkpoints": [
            {
                "question": "What Sanskrit word was used in ancient Indian texts like the Atharvaveda to denote both visible (Drishya) and invisible (Adrishya) organisms?",
                "options": [
                    "Krimi",
                    "Vriksha",
                    "Agni",
                    "Vayu"
                ],
                "correct": 0,
                "explanation": "The Atharvaveda uses the term 'Krimi' to designate tiny living entities, classifying them into Drishya (visible) and Adrishya (invisible)."
            },
            {
                "question": "For what groundbreaking scientific achievement was Dr. Ananda Mohan Chakrabarty granted a historic patent in 1980?",
                "options": [
                    "Developing a specialized bacterium capable of breaking down toxic crude oil spills in oceans",
                    "Inventing the compound glass microscope",
                    "Discovering the penicillin mold",
                    "Breeding giant ostriches in laboratory cages"
                ],
                "correct": 0,
                "explanation": "Dr. Chakrabarty engineered a multi-plasmid Pseudomonas strain capable of digesting crude oil hydrocarbons, receiving a historic patent in 1980 for oil spill bioremediation."
            }
        ]
    },
    {
        "id": 16,
        "title": "Master Synthesis Matrix",
        "subtitle": "Cellular Foundations, Organelles, and Microbial Roles",
        "badge": "Chapter Synthesis",
        "narration": "We have explored the cell from Hooke's 1665 cork chambers to electron microscopes, plant vacuoles, bacterial nucleoids, and ecological microbes. Here is our master comparative synthesis matrix bringing together cellular structures, functions, and the microbial world.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Review this master comparison table summarizing cellular architecture and microbial roles for Class 8 Science Chapter 2.
            </p>
            <div class="overflow-x-auto my-2">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-slate-700 bg-slate-900/80 text-cyan-400 font-bold">
                            <th class="p-2">Feature / Organism</th>
                            <th class="p-2">Key Structure</th>
                            <th class="p-2">Primary Function</th>
                            <th class="p-2">Found In</th>
                            <th class="p-2">Scientific Significance</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-cyan-400">Cell Membrane</td>
                            <td class="p-2">Porous lipid bilayer</td>
                            <td class="p-2">Regulates entry of nutrients and exit of waste</td>
                            <td class="p-2">All cells (Universal)</td>
                            <td class="p-2 text-cyan-300">Selective permeability</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-emerald-400">Cell Wall</td>
                            <td class="p-2">Tough cellulose / chitin</td>
                            <td class="p-2">Rigidity, strength, and structural protection</td>
                            <td class="p-2">Plants, Fungi, Bacteria</td>
                            <td class="p-2 text-cyan-300">Withstands high turgor pressure</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-purple-400">Nucleus / Nucleoid</td>
                            <td class="p-2">Membrane nucleus vs naked nucleoid</td>
                            <td class="p-2">Controls cell activities, growth, reproduction</td>
                            <td class="p-2">Eukaryotes vs Bacteria</td>
                            <td class="p-2 text-cyan-300">Hereditary genetic blueprint</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-lime-400">Chloroplast & Vacuole</td>
                            <td class="p-2">Chlorophyll thylakoids; large fluid sac</td>
                            <td class="p-2">Photosynthesis; turgidity and waste storage</td>
                            <td class="p-2">Plant cells exclusively</td>
                            <td class="p-2 text-cyan-300">Autotrophy and plant posture</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-amber-400">Beneficial Microbes</td>
                            <td class="p-2">Yeast, Lactobacillus, Rhizobium, Spirulina</td>
                            <td class="p-2">Bread rising, curd, nitrogen fixation, oxygen</td>
                            <td class="p-2">Soil, food, water</td>
                            <td class="p-2 text-cyan-300">Biotechnology & Agriculture</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        """,
        "key_points": [
            "Every typical cell features a cell membrane, cytoplasm, and nucleus (or nucleoid in bacteria).",
            "Plant cells are distinguished by cellulose cell walls, photosynthetic chloroplasts, and large central vacuoles.",
            "Biological organization scales hierarchically: Cell → Tissue → Organ → Organ System → Organism.",
            "Microorganisms perform essential environmental decomposition, food fermentation, and biological nitrogen fixation."
        ],
        "sim_id": "cells_microbes_master_matrix_sim",
        "checkpoints": [
            {
                "question": "Which combination correctly matches an organelle with its primary function in a plant cell?",
                "options": [
                    "Chloroplast • Trapping sunlight for photosynthesis",
                    "Cell wall • Carrying electrical thoughts to the brain",
                    "Nucleus • Pumping food out of the roots into clouds",
                    "Vacuole • Breathing in oxygen through ears"
                ],
                "correct": 0,
                "explanation": "Chloroplasts contain green chlorophyll pigments that absorb sunlight energy to synthesize glucose during photosynthesis."
            },
            {
                "question": "What is the primary difference between a bacterial cell and a human cheek cell?",
                "options": [
                    "Bacterial cells lack a membrane-bound nucleus (they have a nucleoid), while human cheek cells have a true nucleus",
                    "Bacterial cells have bones and teeth inside their cytoplasm",
                    "Human cheek cells are 10 meters long",
                    "Bacterial cells are made of solid rock"
                ],
                "correct": 0,
                "explanation": "Bacteria are prokaryotes with an un-enclosed nucleoid and no nuclear membrane, whereas human cells are eukaryotes with a distinct double-membrane nucleus."
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "subtitle": "Questions 1–10: History of Microscopy, Hooke, Leeuwenhoek & Cell Parts",
        "badge": "Exam Certification",
        "narration": "Test your mastery of cellular history and fundamental cell components. Click Solution on any question to view step-by-step scientific explanations.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering Hooke's Micrographia, Leeuwenhoek's living cells, electron microscopes, the cell triad, and selective membrane permeability.</p>",
        "key_points": [
            "Attempt all 10 questions independently.",
            "Review step-by-step scientific solutions.",
            "Master the historical milestones and foundational parts of the cell."
        ],
        "is_quiz_slide": True,
        "quiz_range": "1–10"
    },
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "subtitle": "Questions 11–20: Plant Structures, Bacterial Nucleoids & Cell Specialization",
        "badge": "Exam Certification",
        "narration": "Mastery challenge part two covers plant-specific cell walls, plastids, vacuoles, the bacterial nucleoid, and functional cell shapes like spindle muscle cells and neurons.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions testing cell wall composition, chloroplasts, central vacuoles, prokaryotic nucleoids, spindle muscle fibers, and long branched neurons.</p>",
        "key_points": [
            "Differentiate between plant and animal cellular architecture.",
            "Understand why bacterial DNA lacks a nuclear membrane.",
            "Relate specific cell shapes to specialized biological functions."
        ],
        "is_quiz_slide": True,
        "quiz_range": "11–20"
    },
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "subtitle": "Questions 21–30: Cell Sizes, Ostrich Egg, Hierarchy & Microbial Types",
        "badge": "Exam Certification",
        "narration": "Part three tests your understanding of cell sizes, the record-holding ostrich egg yolk, levels of biological organization, and the diversity of microbes and acellular viruses.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering ostrich egg diameter, the cell-to-organism hierarchy, zygote division, microbial ubiquity, and viral obligate parasitism.</p>",
        "key_points": [
            "Assess cell size records and the surface-area-to-volume rule.",
            "Trace the structural ladder from cells to complete organisms.",
            "Examine viral acellular nature and replication mechanisms."
        ],
        "is_quiz_slide": True,
        "quiz_range": "21–30"
    },
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "subtitle": "Questions 31–40: Beneficial Roles, Biogas, Microalgae & Scientific Pioneers",
        "badge": "Exam Certification",
        "narration": "The final mastery challenge covers decomposers, biogas generation, yeast & lactobacillus, Rhizobium nitrogen fixation, microalgae, Vedic Krimi, and Dr. Chakrabarty's superbug.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering composting, methane biogas, fermentation chemistry, symbiotic root nodules, Spirulina oxygen/nutrition, Vedic Krimi, and oil bioremediation.</p>",
        "key_points": [
            "Master economic and environmental benefits of microorganisms.",
            "Explain industrial fermentation in bread, curd, and batter.",
            "Connect ancient Indian scientific insights with modern biotechnology."
        ],
        "is_quiz_slide": True,
        "quiz_range": "31–40"
    }
]

QUIZ_QUESTIONS = [
    # Questions 1–10 (Slide 17)
    {
        "id": 1,
        "question": "In 1665, who observed thin slices of bottle cork under a compound microscope and coined the term 'cell'?",
        "options": [
            "Robert Hooke",
            "Antonie van Leeuwenhoek",
            "Louis Pasteur",
            "Alexander Fleming"
        ],
        "correct": 0,
        "solution": "Step 1: In 1665, British scientist Robert Hooke examined thin shavings of dead cork under his compound microscope.\nStep 2: He observed a honeycomb pattern of tiny box-like compartments and published his drawings in 'Micrographia'.\nStep 3: He termed these compartments 'cells' (from Latin cellula, meaning small room)."
    },
    {
        "id": 2,
        "question": "What was the landmark book published by Robert Hooke in 1665 that contained his famous illustrations of cork cells?",
        "options": [
            "Micrographia",
            "Origin of Species",
            "Philosophiae Naturalis Principia Mathematica",
            "Systema Naturae"
        ],
        "correct": 0,
        "solution": "Step 1: Robert Hooke's pioneering book on microscopy was titled 'Micrographia' (1665).\nStep 2: It featured detailed engravings of microscopic observations, including flea anatomy and cork cells."
    },
    {
        "id": 3,
        "question": "What was the magnification range of Robert Hooke's compound microscope in 1665?",
        "options": [
            "200 to 300 times (200×–300×)",
            "1,000,000 times (1,000,000×)",
            "10 to 20 times (10×–20×)",
            "5 to 8 times (5×–8×)"
        ],
        "correct": 0,
        "solution": "Step 1: Hooke utilized a compound microscope combining an objective lens and an eyepiece.\nStep 2: It achieved a magnification of approximately 200× to 300×, enabling clear visualization of plant cell walls."
    },
    {
        "id": 4,
        "question": "Who was the first person to clearly see and describe living single-celled bacteria and blood cells, earning the title 'Father of Microbiology'?",
        "options": [
            "Antonie van Leeuwenhoek",
            "Robert Hooke",
            "Edward Jenner",
            "Gregor Mendel"
        ],
        "correct": 0,
        "solution": "Step 1: Antonie van Leeuwenhoek hand-ground high-quality spherical lenses in the late 1660s.\nStep 2: He observed living motile bacteria ('animalcules'), protozoa, and red blood cells for the first time.\nStep 3: For these pioneering discoveries, he is honored as the 'Father of Microbiology'."
    },
    {
        "id": 5,
        "question": "What is the approximate magnification achieved by modern electron microscopes to view subcellular components?",
        "options": [
            "About 1,000,000 times (one million times)",
            "About 300 times",
            "About 1,500 times",
            "About 20 times"
        ],
        "correct": 0,
        "solution": "Step 1: Electron microscopes use high-velocity electron beams with extremely short wavelengths.\nStep 2: This enables magnifications up to approximately 1,000,000×, resolving ribosomes, membranes, and viral capsids."
    },
    {
        "id": 6,
        "question": "What are the three fundamental components present in every typical eukaryotic cell?",
        "options": [
            "Cell membrane, cytoplasm, and nucleus",
            "Cell wall, chloroplast, and flagellum",
            "Bones, blood, and cartilage",
            "Root, stem, and flower"
        ],
        "correct": 0,
        "solution": "Step 1: All typical eukaryotic cells possess three essential structural pillars:\nStep 2: (1) The outer cell membrane, (2) the internal cytoplasm, and (3) the central control nucleus."
    },
    {
        "id": 7,
        "question": "Why is the cell membrane (plasma membrane) described as 'selectively permeable'?",
        "options": [
            "It selectively admits essential nutrients while allowing metabolic wastes out, blocking harmful toxins",
            "It permits all substances to pass indiscriminately without any control",
            "It is completely impermeable and solid like iron",
            "It only opens when exposed to direct boiling water"
        ],
        "correct": 0,
        "solution": "Step 1: The cell membrane contains microscopic pores and protein channels.\nStep 2: It exhibits selective permeability, regulating the ingress of glucose and ions while expelling cellular waste."
    },
    {
        "id": 8,
        "question": "What is the cytoplasm in a living cell?",
        "options": [
            "The internal gelatinous matrix containing proteins, fats, carbohydrates, and salts where life processes occur",
            "A hard wooden shell on the outer surface of animal cells",
            "The empty vacuum chamber inside bone marrow",
            "A dry gas bubble inside the nucleus"
        ],
        "correct": 0,
        "solution": "Step 1: Cytoplasm is the colloidal, semi-transparent matrix enclosed within the cell membrane.\nStep 2: It contains dissolved proteins, lipids, sugars, and mineral salts, hosting the majority of biochemical reactions."
    },
    {
        "id": 9,
        "question": "What is the primary role of the nucleus in a eukaryotic cell?",
        "options": [
            "Regulating all cellular activities, growth, metabolic functions, and division",
            "Storing solid calcium like a skeleton",
            "Trapping direct sunlight for photosynthesis in animal cells",
            "Pumping blood through the human body"
        ],
        "correct": 0,
        "solution": "Step 1: The nucleus contains the genetic instructions (DNA) of the cell.\nStep 2: It serves as the master command center, directing protein synthesis, nutrient metabolism, growth, and replication."
    },
    {
        "id": 10,
        "question": "What was the true biological nature of the cork 'cells' observed by Robert Hooke in 1665?",
        "options": [
            "Empty cellulose cell walls of dead plant bark tissue",
            "Swimming living bacteria inside water",
            "Active red blood cells carrying oxygen",
            "Infectious viral particles"
        ],
        "correct": 0,
        "solution": "Step 1: Bottle cork is harvested from the outer bark of the cork oak tree.\nStep 2: The living protoplasm of these cork cells had dried out and died, leaving behind only the rigid cellulose cell walls."
    },

    # Questions 11–20 (Slide 18)
    {
        "id": 11,
        "question": "Which extra protective outer covering is present in plant, fungal, and bacterial cells to give rigidity and structural support?",
        "options": [
            "Cell wall",
            "Cell membrane only",
            "Nuclear envelope",
            "Centrosome"
        ],
        "correct": 0,
        "solution": "Step 1: Plant, fungal, and bacterial cells possess a rigid outer coat called the cell wall.\nStep 2: In plants, it is composed of cellulose, providing structural strength to withstand high turgor pressure."
    },
    {
        "id": 12,
        "question": "What plant-specific organelles contain the green pigment chlorophyll and carry out photosynthesis?",
        "options": [
            "Chloroplasts (a type of plastid)",
            "Centrosomes",
            "Lysosomes",
            "Ribosomes"
        ],
        "correct": 0,
        "solution": "Step 1: Plastids are double-membrane organelles found in plant cells.\nStep 2: Chloroplasts contain chlorophyll, which captures solar photon energy to convert carbon dioxide and water into glucose."
    },
    {
        "id": 13,
        "question": "What is the function of the large central vacuole found in mature plant cells?",
        "options": [
            "Storing cell sap, removing wastes, and maintaining turgor pressure to keep the cell rigid",
            "Producing electrical shocks to repel birds",
            "Pumping blood into the xylem veins",
            "Generating sound waves during rain"
        ],
        "correct": 0,
        "solution": "Step 1: The large central vacuole occupies 50%–90% of plant cell volume.\nStep 2: It stores cell sap, isolates metabolic byproducts, and exerts outward hydrostatic pressure against the cell wall."
    },
    {
        "id": 14,
        "question": "How does the genetic region of a bacterial cell differ from the nucleus of a plant or animal cell?",
        "options": [
            "Bacterial cells lack a nuclear membrane; their DNA resides in an un-enclosed region called a nucleoid",
            "Bacterial cells have five separate nuclei enclosed in bone",
            "Bacterial cells do not have any genetic material at all",
            "Bacterial nuclei are 100 times larger than plant cells"
        ],
        "correct": 0,
        "solution": "Step 1: Bacteria are prokaryotes, meaning 'before a nucleus'.\nStep 2: They lack a membrane-bound nucleus and nuclear envelope; their circular DNA floats in an un-enclosed zone called the nucleoid."
    },
    {
        "id": 15,
        "question": "What characteristic shape do smooth muscle cells possess, and why?",
        "options": [
            "Spindle-shaped (pointed tapered ends) to contract and relax along a single axis",
            "Round biconcave discs to carry oxygen",
            "Long branched fibers to pass electrical nerve signals",
            "Irregular amoeboid shape to engulf bacteria"
        ],
        "correct": 0,
        "solution": "Step 1: Smooth muscle cells (myocytes) are fusiform or spindle-shaped (tapered at both ends).\nStep 2: This elongated shape aligns actin and myosin protein filaments for effective contractile pulling."
    },
    {
        "id": 16,
        "question": "Why are nerve cells (neurons) long and branched with dendrites and extended axons?",
        "options": [
            "To quickly transmit electrical and chemical messages across long distances in the body",
            "To filter toxic chemicals out of the urine",
            "To absorb vitamins from sunlight through the scalp",
            "To store extra fat reserves for winter hibernation"
        ],
        "correct": 0,
        "solution": "Step 1: Neurons are the communication cables of the nervous system.\nStep 2: Their elongated axons and branched dendrites allow rapid, coordinated transmission of nerve impulses across the body."
    },
    {
        "id": 17,
        "question": "Which of the following cell structures is present in onion peel cells but ABSENT in human cheek epithelial cells?",
        "options": [
            "Cell wall",
            "Cell membrane",
            "Cytoplasm",
            "Nucleus"
        ],
        "correct": 0,
        "solution": "Step 1: Onion peel cells are plant cells and possess a rigid cellulose cell wall.\nStep 2: Human cheek cells are animal cells and possess only an outer plasma membrane, lacking a cell wall."
    },
    {
        "id": 18,
        "question": "What type of plastids do non-green plant tissues (such as roots and potato tubers) contain for food storage?",
        "options": [
            "Leucoplasts",
            "Chloroplasts",
            "Chromoplasts",
            "Mitochondria"
        ],
        "correct": 0,
        "solution": "Step 1: Plastids are categorized by pigment and function.\nStep 2: Leucoplasts are non-pigmented, colorless plastids specialized for storing starches, oils, and proteins in roots and tubers."
    },
    {
        "id": 19,
        "question": "What is the structural term for the thread-like genetic network found inside a non-dividing eukaryotic nucleus?",
        "options": [
            "Chromatin",
            "Chlorophyll",
            "Chitin",
            "Cellulose"
        ],
        "correct": 0,
        "solution": "Step 1: In a non-dividing cell, DNA is loosely coiled around histone proteins as a diffuse network termed chromatin.\nStep 2: During cell division, chromatin condenses into distinct rod-shaped chromosomes."
    },
    {
        "id": 20,
        "question": "Why do plant cells require a rigid cell wall in addition to a cell membrane, unlike animals?",
        "options": [
            "To withstand variations in temperature, high wind velocity, and osmotic turgor pressure without bursting",
            "Because plant cells do not have any water inside them",
            "To allow plants to walk and run across fields",
            "To prevent leaves from absorbing sunlight"
        ],
        "correct": 0,
        "solution": "Step 1: Plants cannot move to shelter from wind, rain, and thermal extremes.\nStep 2: The tough cellulose cell wall provides structural rigidity and prevents hypotonic osmotic lysis (bursting)."
    },

    # Questions 21–30 (Slide 19)
    {
        "id": 21,
        "question": "What holds the biological record as the largest known single cell in the living world?",
        "options": [
            "The yolk of an ostrich egg (130 mm to 170 mm in diameter)",
            "A blue whale muscle cell",
            "An elephant neuron",
            "A giant redwood tree leaf cell"
        ],
        "correct": 0,
        "solution": "Step 1: The yolk of an unfertilized ostrich egg is a single gigantic ovum cell.\nStep 2: It measures 130 mm to 170 mm across (13 to 17 cm) and can weigh over 1.5 kilograms."
    },
    {
        "id": 22,
        "question": "Which of the following correctly displays the hierarchical levels of organization in multicellular life?",
        "options": [
            "Cell → Tissue → Organ → Organ system → Organism",
            "Organism → Organ system → Tissue → Organ → Cell",
            "Tissue → Cell → Organ → Organism → Organ system",
            "Cell → Organ → Tissue → Organ system → Organism"
        ],
        "correct": 0,
        "solution": "Step 1: Life organizes from simple to complex:\nStep 2: Cells assemble into tissues; tissues form organs; organs form organ systems; organ systems make up the organism."
    },
    {
        "id": 23,
        "question": "From what single starting entity do all complex multicellular animals and plants develop?",
        "options": [
            "A single fertilized egg cell (zygote) that divides repeatedly",
            "A clump of mud and river water",
            "An adult organ system formed out of air",
            "Ten different dead cells glued together"
        ],
        "correct": 0,
        "solution": "Step 1: Sexual reproduction produces a single diploid cell: the fertilized egg (zygote).\nStep 2: Through repeated mitotic divisions and cellular differentiation, this single cell develops into a complex organism."
    },
    {
        "id": 24,
        "question": "Which of the following is a unicellular microorganism made of only a single cell?",
        "options": [
            "Amoeba",
            "Bread mold (Rhizopus)",
            "Mushroom (Agaricus)",
            "Earthworm"
        ],
        "correct": 0,
        "solution": "Step 1: Unicellular organisms carry out all life processes inside a single independent cell.\nStep 2: *Amoeba* and bacteria are unicellular. Molds, mushrooms, and earthworms are multicellular."
    },
    {
        "id": 25,
        "question": "Why are viruses described as 'acellular' and placed on the boundary between the living and the non-living?",
        "options": [
            "They lack cellular structures (cytoplasm, organelles) and can only replicate inside a living host cell",
            "They have three nuclei and five cell walls",
            "They are giant multicellular animals that live underground",
            "They can synthesize glucose through photosynthesis at night"
        ],
        "correct": 0,
        "solution": "Step 1: Viruses lack cellular components (no plasma membrane, cytoplasm, or ribosomes).\nStep 2: Outside a host, they are inert particles; they exhibit replication only after invading a living host cell."
    },
    {
        "id": 26,
        "question": "In what diverse environments on Earth can living microorganisms be found?",
        "options": [
            "Everywhere—in soil, water, air, thermal hot springs, snow zones, and inside animal bodies",
            "Only in refrigerated milk cartons",
            "Exclusively in clean glass test tubes in laboratories",
            "Only on the dry surface of the moon"
        ],
        "correct": 0,
        "solution": "Step 1: Microbes are ubiquitous extremophiles and mesophiles.\nStep 2: They populate soil, atmosphere, oceans, thermal geysers, polar ice sheets, and animal digestive tracts."
    },
    {
        "id": 27,
        "question": "What is a 'tissue' in the biological hierarchy of life?",
        "options": [
            "A group of similar specialized cells performing a specific common function",
            "A collection of ten different complete animals",
            "The outer bone of a bird",
            "A single isolated atom of carbon"
        ],
        "correct": 0,
        "solution": "Step 1: In multicellular biology, cells differentiate and cooperate.\nStep 2: A group of morphologically similar cells working together to carry out a common task forms a tissue (e.g., muscle tissue)."
    },
    {
        "id": 28,
        "question": "What is an 'organ' in the biological hierarchy?",
        "options": [
            "A structure composed of different tissues working together to carry out a specific body task",
            "A single standalone bacterium",
            "A drop of water in the blood",
            "A chemical fertilizer used on plants"
        ],
        "correct": 0,
        "solution": "Step 1: Different tissues integrate structurally and functionally to form an organ.\nStep 2: For example, the stomach combines epithelial, muscular, connective, and nervous tissues to digest food."
    },
    {
        "id": 29,
        "question": "Why are cells generally microscopic rather than growing to the size of watermelons?",
        "options": [
            "A high surface-area-to-volume ratio is required for rapid diffusion of nutrients and waste across the membrane",
            "Because Earth's gravity crushes large cells into powder",
            "Because cells are afraid of direct sunlight",
            "Because nuclei can only see objects smaller than 1 micrometer"
        ],
        "correct": 0,
        "solution": "Step 1: As a cell increases in size, its volume ($r^3$) grows much faster than its surface area ($r^2$).\nStep 2: Beyond a microscopic size, the surface area becomes insufficient to transport necessary nutrients and wastes, forcing cells to remain small."
    },
    {
        "id": 30,
        "question": "Which of the following is an example of a multicellular microscopic fungus?",
        "options": [
            "Bread mold (Rhizopus)",
            "Amoeba",
            "Paramecium",
            "Bacteriophage"
        ],
        "correct": 0,
        "solution": "Step 1: *Rhizopus* (bread mold) is composed of branching multicellular fungal filaments called hyphae.\nStep 2: *Amoeba* and *Paramecium* are unicellular protozoa; bacteriophage is an acellular virus."
    },

    # Questions 31–40 (Slide 20)
    {
        "id": 31,
        "question": "How do saprophytic fungi and bacteria clean the environment and enrich soil fertility?",
        "options": [
            "By decomposing fallen leaves, dead plant material, and animal remains into nutrient-rich humus (manure)",
            "By burying all organic waste in solid plastic boxes",
            "By freezing the forest floor into solid ice",
            "By converting dirt into poisonous chlorine gas"
        ],
        "correct": 0,
        "solution": "Step 1: Decomposers secrete extracellular hydrolytic enzymes onto dead organic matter.\nStep 2: They break complex polymers into simple mineral nutrients, creating dark humus (manure) that enriches soil."
    },
    {
        "id": 32,
        "question": "What gas mixture is produced when microorganisms decompose organic waste in an oxygen-free (anaerobic) environment?",
        "options": [
            "Biogas (composed primarily of methane with carbon dioxide)",
            "Pure oxygen gas with nitrogen",
            "Chlorofluorocarbons (CFCs)",
            "Pure hydrogen gas only"
        ],
        "correct": 0,
        "solution": "Step 1: In an anaerobic environment, methanogenic bacteria digest organic waste.\nStep 2: This produces biogas, which is composed of 55%–70% methane ($\text{CH}_4$) and carbon dioxide ($\text{CO}_2$)."
    },
    {
        "id": 33,
        "question": "What gas released by yeast fermentation makes bread dough expand, rise, and become soft and spongy?",
        "options": [
            "Carbon dioxide (CO₂)",
            "Nitrogen (N₂)",
            "Oxygen (O₂)",
            "Sulfur dioxide (SO₂)"
        ],
        "correct": 0,
        "solution": "Step 1: Baker's yeast (*Saccharomyces cerevisiae*) respires anaerobically in warm, sugary dough:\n$$\\text{Glucose} \\to \\text{Alcohol} + \\text{CO}_2 \\uparrow$$\nStep 2: The expanding $\\text{CO}_2$ gas bubbles are trapped in the dough, creating its light, spongy texture."
    },
    {
        "id": 34,
        "question": "Which bacterium converts milk into curd by fermenting lactose sugar into lactic acid?",
        "options": [
            "Lactobacillus",
            "Rhizobium",
            "Spirulina",
            "Pseudomonas"
        ],
        "correct": 0,
        "solution": "Step 1: Starter curd introduces *Lactobacillus* bacteria into warm milk.\nStep 2: They ferment milk sugar (lactose) into lactic acid, lowering the pH and coagulating casein proteins into curd."
    },
    {
        "id": 35,
        "question": "Where are symbiotic Rhizobium bacteria located in leguminous plants (beans, peas, lentils), and what is their function?",
        "options": [
            "Inside root nodules; they trap atmospheric nitrogen and convert it into plant-usable nitrates",
            "On leaf tips; they capture rainwater to make honey",
            "Inside flower petals; they produce sweet scent for bees",
            "Inside the bark; they make the plant grow taller than trees"
        ],
        "correct": 0,
        "solution": "Step 1: *Rhizobium* forms a mutualistic symbiosis inside legume root nodules.\nStep 2: They fix unreactive atmospheric $\\text{N}_2$ into ammonium and nitrates, boosting soil fertility naturally."
    },
    {
        "id": 36,
        "question": "What critical planetary role do aquatic microalgae (such as diatoms and phytoplankton) perform for Earth's biosphere?",
        "options": [
            "They produce more than half (50%+) of Earth's atmospheric oxygen through photosynthesis",
            "They absorb all sunlight so the oceans freeze into ice",
            "They drink all river water to prevent sea levels from rising",
            "They turn seawater into sweet sugar syrup"
        ],
        "correct": 0,
        "solution": "Step 1: Aquatic microalgae are primary producers that inhabit oceans and lakes.\nStep 2: Through vast photosynthetic activity, they generate more than 50% of the oxygen in Earth's atmosphere."
    },
    {
        "id": 37,
        "question": "Which microscopic aquatic organism is cultivated as a commercial superfood due to its high concentration of complete protein and Vitamin B12?",
        "options": [
            "Spirulina",
            "Amoeba",
            "Bread mold",
            "Yeast"
        ],
        "correct": 0,
        "solution": "Step 1: *Spirulina* is a filamentous cyanobacterium (blue-green microalga).\nStep 2: It contains up to 60%–70% complete protein by dry weight and is rich in iron, beta-carotene, and Vitamin $\\text{B}_{12}$."
    },
    {
        "id": 38,
        "question": "What Sanskrit word was used in ancient Indian texts like the Atharvaveda to denote microscopic and visible entities?",
        "options": [
            "Krimi (divided into Drishya and Adrishya)",
            "Chakra",
            "Prana",
            "Mantra"
        ],
        "correct": 0,
        "solution": "Step 1: The *Atharvaveda* and early Ayurvedic texts employ the term 'Krimi'.\nStep 2: They categorized Krimi into Drishya (visible parasites) and Adrishya (invisible entities), noting both beneficial and pathogenic roles."
    },
    {
        "id": 39,
        "question": "What was the landmark scientific contribution of Indian-American microbiologist Dr. Ananda Mohan Chakrabarty (1938–2020)?",
        "options": [
            "Engineering an oil-eating bacterium in 1971 to break down marine oil spills, receiving a historic patent in 1980",
            "Discovering the compound microscope in 1665",
            "Inventing the polio vaccine drops in 1955",
            "Synthesizing artificial chlorophyll in 1800"
        ],
        "correct": 0,
        "solution": "Step 1: In 1971, Dr. Ananda Mohan Chakrabarty combined plasmids in *Pseudomonas putida*.\nStep 2: This 'superbug' could digest multiple crude oil hydrocarbons to clean oil spills.\nStep 3: In 1980, he was awarded the world's first patent for a genetically modified living organism."
    },
    {
        "id": 40,
        "question": "Which combination correctly matches a microorganism with its beneficial human application?",
        "options": [
            "Lactobacillus • Curd & Fermented Batter | Yeast • Bread Rising | Rhizobium • Nitrogen Fixation",
            "Virus • Curd Formation | Bacterium • Rabies Vaccine | Amoeba • Biogas",
            "Rhizobium • Bread Dough Rising | Yeast • Malaria Cure | Diatoms • Poison",
            "Lactobacillus • Smallpox Vaccine | Fungus • Plastic Manufacturing"
        ],
        "correct": 0,
        "solution": "Step 1: *Lactobacillus* ferments milk into curd and leavens batters.\nStep 2: *Yeast* produces $\\text{CO}_2$ to make bread dough light and spongy.\nStep 3: *Rhizobium* fixes atmospheric nitrogen in legume root nodules to fertilize soil."
    }
]


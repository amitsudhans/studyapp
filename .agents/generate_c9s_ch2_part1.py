#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Science Chapter 2: Cell: The Building Block of Life
Part 1: Slides 1 to 8 (Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Origin Of Life",
        "subtitle": "Origin of Life (3.5 Billion Years Ago), Puga Valley Hot Springs & Cellular Organization",
        "speech": (
            "Welcome to Class Nine Science, Chapter Two: Cell, The Building Block of Life! Let us begin with a "
            "breathtaking question: where and how did life first appear on Earth? Scientific consensus shows that "
            "life originated in water roughly three point five billion years ago! Early Earth was hot, volcanic, "
            "and extreme—much like modern geothermal hot springs in Puga Valley, Ladakh! In those scalding waters, "
            "single-celled thermophilic bacteria thrive even today! Researchers at the Birbal Sahni Institute of "
            "Palaeosciences have studied protective calcium carbonate deposits formed around such ancient microbes, "
            "preserving vital clues to Earth's earliest living cells! "
            "Across all of biology, the cell is the fundamental unit of structure and function in every living "
            "organism! Some organisms are unicellular—like bacteria and yeast, where a single cell performs every "
            "life process independently! Other organisms are multicellular—like plants and animals, where millions "
            "or trillions of specialized cells cooperate in a clear hierarchy: Cells combine to form Tissues, Tissues "
            "organize into Organs, Organs work together as Organ Systems, and Organ Systems build a complete, "
            "self-sustaining living organism! From microscopic bacteria in steaming Ladakh springs to towering forests "
            "and human bodies, every complex creature begins with the remarkable architecture of a single cell!"
        ),
        "checkpoints": [
            {
                "question": "Why do scientists study hot springs such as Puga Valley in Ladakh to understand the origin of life?",
                "options": [
                    "Their extreme thermal conditions resemble early Earth (~3.5 billion years ago) and host thermophilic bacteria",
                    "Hot springs contain zero water or minerals",
                    "Multicellular trees originated inside boiling geysers",
                    "Calcium carbonate dissolves all fossils instantly",
                ],
                "answer": 0,
                "hint": "Think about extreme environments where ancient single-celled thermophiles thrive and leave mineral deposits!",
                "explanation": "Puga Valley hot springs mirror early Earth's extreme aquatic habitats and host thermophilic bacteria studied by the Birbal Sahni Institute of Palaeosciences.",
            },
            {
                "question": "Which sequence correctly shows the hierarchical cellular organization in multicellular organisms?",
                "options": [
                    "Cells → Tissues → Organs → Organ Systems",
                    "Organs → Cells → Tissues → Organ Systems",
                    "Tissues → Organ Systems → Cells → Organs",
                    "Organ Systems → Organs → Cells → Tissues",
                ],
                "answer": 0,
                "hint": "Start from the fundamental unit of life and build upward!",
                "explanation": "Specialized cells form tissues, tissues form organs, and organs collaborate within organ systems.",
            },
        ],
    },
    {
        "id": 2,
        "title": "Microscopy Cell Size",
        "subtitle": "Limit of Eye Resolution (0.1 mm), Hooke (1665), Light & Electron Microscopy, Activity 2.1",
        "speech": (
            "If every organism is built from cells, why can we not see most cells with our naked eyes? Because the "
            "human eye has a resolution limit of roughly zero point one millimetres at our comfortable near point of "
            "about twenty-five centimetres! Anything smaller blurs together unless we magnify it! "
            "In sixteen sixty-five, Robert Hooke used a self-designed microscope magnifying two hundred to three "
            "hundred times to examine thin slices of cork, discovering tiny honeycomb-like compartments he named "
            "cells! Modern school laboratories use compound light microscopes combining an eyepiece with objective "
            "lenses—typically ten times and forty times—to view stained cells clearly! To see even tinier internal "
            "structures at the nanometre scale, scientists use electron microscopes, which focus a beam of electrons "
            "instead of visible light! "
            "In Activity Two Point One, you can estimate cell size yourself! Place a transparent millimetre ruler "
            "under the microscope to measure the visible field diameter, convert millimetres into micrometres by "
            "multiplying by one thousand, count how many cells fit across that diameter, and divide! Cell Size "
            "equals Diameter of the visible field in micrometres divided by the number of cells along the diameter! "
            "That simple ratio turns an ordinary classroom microscope into a precise biological measuring tool!"
        ),
        "checkpoints": [
            {
                "question": "What is the approximate resolution limit of the unaided human eye at a near point of ~25 cm?",
                "options": ["0.1 mm", "10 cm", "1 nm", "5 mm"],
                "answer": 0,
                "hint": "Most cells are 1–100 µm, which is smaller than 100 µm (0.1 mm)!",
                "explanation": "The unaided human eye resolves details down to about 0.1 mm (100 µm) at ~25 cm, requiring magnification for most cells.",
            },
            {
                "question": "In Activity 2.1, if the visible field diameter is 1.5 mm (1,500 µm) and 15 cells lie end-to-end across it, what is the average cell size?",
                "options": ["100 µm", "15 µm", "1,500 µm", "10 µm"],
                "answer": 0,
                "hint": "Use Cell Size = Diameter in µm ÷ Number of cells!",
                "explanation": "1,500 µm ÷ 15 cells = 100 µm per cell.",
            },
        ],
    },
    {
        "id": 3,
        "title": "Plasma Membrane Osmosis",
        "subtitle": "Cell Membrane (7–10 nm), Activity 2.2 Potato Osmosis, Diffusion & Solution Tonicity",
        "speech": (
            "Every cell interacts continuously with its neighbours and external environment across a delicate outer "
            "boundary: the plasma membrane, also called the cell membrane! Measuring only seven to ten nanometres "
            "thick, this universal feature of every cell is selectively permeable—it protects cellular contents while "
            "carefully regulating which molecules enter or leave! "
            "How does water cross this membrane? Observe Activity Two Point Two: Potato Osmosis! Take two equal-sized "
            "potato blocks and weigh them! Place Block A in plain water and Block B in a concentrated twenty-percent "
            "salt or sugar solution! Later, weigh both blocks again! Block A gains weight and swells, whereas Block B "
            "loses weight and shrinks! "
            "Why does this happen? Diffusion is the net movement of particles down a concentration gradient, while "
            "osmosis is specifically the net diffusion of water across a selectively permeable membrane! Solution "
            "tonicity predicts every outcome! In a hypotonic solution, outside solute concentration is lower than "
            "inside, so water enters and the cell swells! In a hypertonic solution, outside solute concentration is "
            "higher, so water leaves and the cell shrinks! In an isotonic solution, concentrations match, producing "
            "no net water movement at all! Knowing tonicity helps biologists explain crisp vegetables, wilted leaves, "
            "and safe medical intravenous fluids!"
        ),
        "checkpoints": [
            {
                "question": "In Activity 2.2, what happens to a potato block placed in a concentrated 20% salt/sugar solution (Beaker B)?",
                "options": [
                    "It loses water by osmosis and shrinks/loses weight because the outside solution is hypertonic",
                    "It absorbs salt and doubles in weight",
                    "No water moves because potato cells lack membranes",
                    "It immediately turns into starch crystals",
                ],
                "answer": 0,
                "hint": "Compare solute concentration outside (20%) vs inside the potato cells!",
                "explanation": "In a hypertonic 20% solution, water moves out of the potato cells across their selectively permeable membranes, decreasing weight.",
            },
            {
                "question": "How does osmosis differ from general diffusion?",
                "options": [
                    "Osmosis is specifically the net diffusion of water across a selectively permeable membrane",
                    "Osmosis only happens in dry air without membranes",
                    "Osmosis moves solutes against a gradient using electricity",
                    "Osmosis occurs only in dead plastic",
                ],
                "answer": 0,
                "hint": "Remember which molecule moves and what barrier it crosses!",
                "explanation": "Osmosis is a special case of diffusion involving net water movement across a selectively permeable membrane.",
            },
        ],
    },
    {
        "id": 4,
        "title": "Fluid Mosaic Model",
        "subtitle": "Structure of the Cell Membrane: Lipid Bilayer & Embedded Gatekeeper Proteins",
        "speech": (
            "What gives the seven-to-ten-nanometre plasma membrane its remarkable flexibility and selective control? "
            "Biologists explain its architecture using the Fluid-Mosaic Model! Picture a dynamic, flexible double "
            "layer of lipid molecules—called a lipid bilayer—studded with specialized proteins like tiles in a moving "
            "mosaic! "
            "Why do lipids arrange into a bilayer automatically in water? Each lipid molecule has two contrasting "
            "parts! Its water-loving, hydrophilic head faces outward toward the watery cytoplasm inside the cell and "
            "the watery fluid outside the cell! Meanwhile, its water-fearing, hydrophobic tails tuck inward, facing "
            "each other away from water! This clever sandwich creates a stable yet fluid barrier that blocks random "
            "water-soluble ions and large molecules from leaking freely! "
            "Then how do essential nutrients like glucose, amino acids, and specific ions cross? Embedded proteins act "
            "as selective gatekeepers, channels, and pumps! Because the lipid bilayer is fluid, proteins can shift "
            "laterally, allowing the cell to change shape, engulf particles, repair tiny tears, sense chemical "
            "signals, and communicate with neighbouring cells! Together, the hydrophilic-head, hydrophobic-tail lipid "
            "bilayer and embedded gatekeeper proteins make the plasma membrane a smart, dynamic, protective, and "
            "intelligently selective living boundary around every single prokaryotic and eukaryotic living cell on Earth!"
        ),
        "checkpoints": [
            {
                "question": "In the Fluid-Mosaic Model of the cell membrane, how are the lipid molecules arranged?",
                "options": [
                    "As a flexible bilayer with hydrophilic heads facing outward and hydrophobic tails facing inward",
                    "As a rigid brick wall with hydrophobic tails facing water",
                    "As a single solid layer of cellulose",
                    "As free floating DNA strands",
                ],
                "answer": 0,
                "hint": "Hydrophilic means water-loving; hydrophobic means water-fearing!",
                "explanation": "Hydrophilic heads face the watery interior and exterior, while hydrophobic tails tuck inward away from water.",
            },
            {
                "question": "What is the primary role of proteins embedded within the lipid bilayer?",
                "options": [
                    "Acting as selective gatekeepers/channels/pumps regulating transport and communication",
                    "Making the membrane completely impermeable to everything",
                    "Storing starch granules inside the bilayer",
                    "Producing chlorophyll",
                ],
                "answer": 0,
                "hint": "Think of how specific nutrients cross a hydrophobic lipid core!",
                "explanation": "Embedded membrane proteins serve as selective gatekeepers and channels for controlled transport.",
            },
        ],
    },
    {
        "id": 5,
        "title": "Cell Wall Microscopy",
        "subtitle": "Cellulose Cell Wall, Activity 2.3 (Onion, Rhoeo, Cheek Cells & Plasmolysis), Pause & Ponder 1–3",
        "speech": (
            "Outside the plasma membrane, plant, fungal, and bacterial cells possess an extra outer coat: a rigid, "
            "fully permeable cell wall! In plants, this wall is built mainly of tough cellulose fibres, giving fixed "
            "shape and protecting stationary plants against wind, rain, and osmotic bursting! Animal cells lack cell "
            "walls, giving them flexibility for movement! "
            "In Activity Two Point Three, compare plant and animal cells directly under a microscope! Peel a thin "
            "onion scale or Rhoeo leaf epidermis and stain it with safranin—you will observe neat, box-shaped plant "
            "cells with clear cell walls! Gently scrape inner cheek cells and stain them with methylene blue—you will "
            "see irregular, wall-less animal cells! Now add a twenty-percent sugar solution to the plant peel: water "
            "rushes out by osmosis, and the living plasma membrane shrinks away from the rigid cell wall—a dramatic "
            "phenomenon called plasmolysis! "
            "As Pause and Ponder Questions One to Three ask: stationary plants need rigid walls because they cannot "
            "walk indoors during storms; if plant walls turned floppy, tall stems would collapse immediately; and "
            "keeping an untreated control slide in plain water proves beyond doubt that plasmolysis is truly caused "
            "by the external twenty-percent sugar concentration gradient!"
        ),
        "checkpoints": [
            {
                "question": "In Activity 2.3, which stains are used respectively for plant (onion peel/Rhoeo) and animal (human cheek) cells?",
                "options": [
                    "Safranin for plant cells; Methylene blue for animal cheek cells",
                    "Methylene blue for onion peel; Aceto-carmine for cheek cells",
                    "Plain salt for both",
                    "Chlorophyll for cheek cells; Sugar for onion peel",
                ],
                "answer": 0,
                "hint": "Reddish safranin highlights plant walls, while methylene blue highlights translucent animal cheek cells!",
                "explanation": "Safranin stains plant cells (onion/Rhoeo) and methylene blue stains human cheek cells.",
            },
            {
                "question": "What happens during plasmolysis when a plant cell is placed in a 20% sugar solution?",
                "options": [
                    "Water leaves the cell and the plasma membrane shrinks away from the rigid cellulose cell wall",
                    "The cellulose cell wall dissolves completely",
                    "The cell swells until it explodes",
                    "Animal cheek cells grow a cell wall",
                ],
                "answer": 0,
                "hint": "The outer cellulose wall stays rigid while the inner living contents shrink!",
                "explanation": "In a hypertonic 20% sugar solution, exosmosis shrinks the cytoplasm and plasma membrane away from the rigid cell wall.",
            },
        ],
    },
    {
        "id": 6,
        "title": "Prokaryotes Versus Eukaryotes",
        "subtitle": "Cell Interior, Activity 2.4 (Prokaryotes vs Eukaryotes), Acellular Agents & Cytoskeleton",
        "speech": (
            "Step inside the cell! A eukaryotic cell interior is a coordinated working system containing jelly-like "
            "cytoplasm, a central nucleus, and specialized membrane-bound organelles! Yet not every cell shares this "
            "compartmentalized layout! "
            "In Activity Two Point Four, compare bacterial, plant, and animal cells! Bacteria are prokaryotes, "
            "typically tiny at one to ten micrometres! They lack a true nuclear membrane and lack membrane-bound "
            "organelles—instead, their genetic material sits in an open region called a nucleoid! By contrast, plant, "
            "animal, and fungal cells are eukaryotes, much larger at ten to one hundred micrometres, housing a true "
            "membrane-bound nucleus and dedicated organelles! "
            "Notice two more fascinating details from Ready to Go Beyond! First, viruses, viroids, and prions are "
            "acellular infectious agents—they have no cellular structure of their own and must hijack host cells to "
            "multiply! Second, inside eukaryotic cytoplasm runs a protein fibre network called the cytoskeleton, "
            "providing internal scaffolding, shape, and cargo tracks for movement! Alongside living organelles, cells "
            "also hold non-living cell inclusions such as stored starch grains, calcium oxalate crystals, or silica "
            "crystals that serve protective, structural, or energy-reserve roles! Comparing these architectures shows "
            "how evolution scaled cells from simple prokaryotes into complex, compartmentalized eukaryotic cities!"
        ),
        "checkpoints": [
            {
                "question": "Which combination accurately distinguishes prokaryotic cells from eukaryotic cells?",
                "options": [
                    "Prokaryotes (1–10 µm) have a nucleoid without a nuclear membrane or membrane-bound organelles; eukaryotes (10–100 µm) have both",
                    "Prokaryotes are 100 µm with a double-membrane nucleus",
                    "Eukaryotes lack cytoplasm and DNA",
                    "Bacteria are eukaryotic while plants are prokaryotic",
                ],
                "answer": 0,
                "hint": "Compare size (1–10 µm vs 10–100 µm) and presence of membrane-bound nucleus/organelles!",
                "explanation": "Prokaryotes lack a nuclear membrane and membrane-bound organelles (nucleoid instead), whereas eukaryotes possess both.",
            },
            {
                "question": "Why are viruses, viroids, and prions classified as acellular agents?",
                "options": [
                    "They lack a cellular organization (no cell membrane, cytoplasm, or independent metabolism)",
                    "They are larger than plant cells",
                    "They contain chloroplasts and mitochondria",
                    "They are made of cellulose cell walls",
                ],
                "answer": 0,
                "hint": "Think about what defines a living cell vs an infectious non-cellular particle!",
                "explanation": "Viruses, viroids, and prions lack cellular membranes and organelles, relying on host cells to replicate.",
            },
        ],
    },
    {
        "id": 7,
        "title": "Nucleus And Ribosomes",
        "subtitle": "Nucleus (DNA, Chromatin, Nucleolus), Enucleate RBCs (~120 Days) & Ribosome Protein Factories",
        "speech": (
            "Now let us tour the specialized organelles of eukaryotic cells, starting with the control headquarters: "
            "the Nucleus! Enclosed by a double-layered nuclear membrane perforated with tiny nuclear pores, the nucleus "
            "exchanges chemical messages with the cytoplasm! Inside sits a dense spot called the nucleolus, where "
            "ribosomal subunits are assembled, surrounded by tangled threads of chromatin made of DNA and proteins! "
            "Functional segments of DNA are called genes—our coded hereditary instructions! When a cell prepares to "
            "divide, loose chromatin condenses tightly into distinct, rod-shaped chromosomes! "
            "Here is a surprising Threads of Curiosity twist: mature human red blood cells actually lose their "
            "nucleus! Why? Going enucleate maximizes internal space for hemoglobin to carry oxygen across your body—at "
            "the trade-off of a limited lifespan of roughly one hundred twenty days without fresh genetic repair, "
            "after which bone marrow replaces them! "
            "Finally, meet the Ribosomes—tiny, non-membranous protein factories found floating freely in cytoplasm or "
            "docked onto membranes! Reading coded genetic instructions sent from the nucleus, ribosomes link amino "
            "acids together into digestive enzymes, hormones, transport carriers, and structural proteins essential for "
            "every single living biochemical reaction happening continuously inside the growing, metabolically active "
            "plant, fungal, or animal eukaryotic cell!"
        ),
        "checkpoints": [
            {
                "question": "Why do mature human red blood cells (RBCs) lack a nucleus?",
                "options": [
                    "To maximize internal space for hemoglobin to transport oxygen, resulting in a ~120-day lifespan",
                    "Because RBCs are prokaryotic bacteria",
                    "So they can perform photosynthesis",
                    "To store cellulose cell walls",
                ],
                "answer": 0,
                "hint": "More room inside means more oxygen-carrying protein, though the cell cannot repair DNA!",
                "explanation": "Enucleate mature RBCs pack more hemoglobin for oxygen transport, giving them an average ~120-day lifespan.",
            },
            {
                "question": "What is the main function of the nucleolus inside the nucleus?",
                "options": [
                    "Assembling ribosomal subunits",
                    "Generating ATP via cristae",
                    "Digesting worn-out organelles",
                    "Storing chlorophyll pigment",
                ],
                "answer": 0,
                "hint": "Ribosomes are built in this dense nuclear region before exiting through nuclear pores!",
                "explanation": "The nucleolus produces and assembles ribosomal subunits, which then form ribosomes in the cytoplasm.",
            },
        ],
    },
    {
        "id": 8,
        "title": "Endomembrane Transport System",
        "subtitle": "Endoplasmic Reticulum (RER & SER) & Golgi Apparatus (Camillo Golgi, 1898 Barn Owl)",
        "speech": (
            "Once ribosomes build proteins, how does a cell manufacture, modify, and ship molecules to the right "
            "destination? Through the Endoplasmic Reticulum and Golgi Apparatus working as an integrated factory "
            "and post office! "
            "The Endoplasmic Reticulum, or ER, is an extensive membrane network directly continuous with the outer "
            "nuclear envelope! It comes in two distinct forms! Rough Endoplasmic Reticulum, or RER, looks studded "
            "under an electron microscope because ribosomes cling to its surface—it synthesizes and folds proteins "
            "destined for membranes or secretion! Smooth Endoplasmic Reticulum, or SER, lacks ribosomes and specializes "
            "in synthesizing lipids, steroid hormones, and detoxifying harmful compounds! "
            "Next, freshly made proteins and lipids travel in tiny transport vesicles to the Golgi Apparatus—stacks "
            "of flattened membrane sacs that modify, sort, label, and package molecules for export outside the cell or "
            "delivery to internal organelles! "
            "Meet a Scientist: in eighteen ninety-eight, Italian scientist Camillo Golgi first observed this delicate "
            "network inside barn owl nerve cells using a special silver-staining technique! Today, his name honours "
            "the Golgi Apparatus across every biology textbook worldwide, reminding us how careful microscopy and "
            "silver staining reveal hidden cellular transport, sorting, and packaging machinery inside living animal "
            "nerve cells and secretory tissues!"
        ),
        "checkpoints": [
            {
                "question": "How do Rough ER (RER) and Smooth ER (SER) differ in structure and function?",
                "options": [
                    "RER has attached ribosomes and handles protein synthesis/secretion; SER lacks ribosomes and synthesizes lipids and hormones",
                    "SER has ribosomes while RER stores starch",
                    "Both are found inside the nucleolus",
                    "RER produces ATP while SER captures sunlight",
                ],
                "answer": 0,
                "hint": "Remember why RER looks 'rough' under an electron microscope!",
                "explanation": "Ribosomes stud RER for protein synthesis; ribosome-free SER synthesizes lipids and hormones.",
            },
            {
                "question": "What did Camillo Golgi discover in 1898 while studying barn owl nerve cells?",
                "options": [
                    "The Golgi Apparatus—stacks of flattened sacs that modify, sort, and package cellular products",
                    "Thermophilic bacteria in Ladakh",
                    "Cork cells under a 200X lens",
                    "Plant cell totipotency",
                ],
                "answer": 0,
                "hint": "The organelle is named directly after him!",
                "explanation": "Camillo Golgi observed the flattened sac network (Golgi Apparatus) in barn owl nerve cells in 1898.",
            },
        ],
    },
]

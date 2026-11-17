#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part1 = [
    {
        "id": 1,
        "title": "Building Blocks",
        "subtitle": "Introduction & Overview: Matter Hierarchy & Core Inquiries",
        "speech": (
            "Welcome, students, to Chapter 8, Journey Inside the Atom! Look around your classroom and at yourself. "
            "Every non-living object—brick walls, glass windows made of silicates, and steel desks—as well as every "
            "living organism—human bodies built from organs, tissues, cells, and complex proteins—is ultimately "
            "constructed from unimaginably tiny subatomic building blocks called atoms! Just as bricks stack to build "
            "a house, atoms join together to form all matter in the universe. Yet peering inside an atom raises "
            "deep scientific puzzles, which our Think It Over questions highlight right at the start. First, are atoms "
            "truly the smallest indivisible particles, or do even tinier parts hide within them? Second, if negative "
            "electrons revolve rapidly around a positively charged central nucleus, why do they not lose energy and "
            "crash straight into the nucleus? And third, why did scientists continuously modify and replace atomic "
            "models over two centuries? In this chapter, we will trace that thrilling detective story from ancient "
            "philosophers to modern nuclear science, uncovering protons, neutrons, electrons, energy shells, valency, "
            "and isotopes. Get ready to explore the invisible architecture inside every single speck of matter! "
            "Use the interactive simulator beside each slide to test every atomic model with your own hands."
        ),
        "checkpoints": [
            {
                "question": "Which hierarchy correctly traces a living organism down to its fundamental chemical building blocks?",
                "options": [
                    "Atoms → Bricks → Silicates → Organs",
                    "Organism → Organs → Tissues → Cells → Proteins → Atoms",
                    "Cells → Organs → Tissues → Atoms",
                    "Proteins → Silicates → Tissues → Cells"
                ],
                "answer": 1,
                "hint": "Move from largest biological level to smallest chemical unit.",
                "explanation": "Living organisms consist of organs, tissues, cells, and proteins, all ultimately built from atoms."
            },
            {
                "question": "Why did scientists continuously modify atomic models over time?",
                "options": [
                    "Atoms themselves changed every decade",
                    "New experimental discoveries (like electrons and alpha scattering) revealed flaws in older models",
                    "Philosophers voted to rename particles",
                    "Older models were too mathematical"
                ],
                "answer": 1,
                "hint": "Science updates models whenever new experimental evidence contradicts predictions.",
                "explanation": "Discoveries of cathode rays, alpha-particle scattering, and spectral lines required progressively better atomic models."
            }
        ]
    },
    {
        "id": 2,
        "title": "Ancient Atomic Roots",
        "subtitle": "Section 8.1: Acharya Kanada, Democritus & John Dalton (1808)",
        "speech": (
            "Long before microscopes or particle accelerators existed, curious thinkers wondered: what happens if you "
            "keep cutting a substance into smaller and smaller pieces forever? In Section 8.1, we rediscover the "
            "ancient philosophical roots of atomic theory! Over two thousand five hundred years ago in India, the sage "
            "Acharya Kanada wrote the Vaisesika Sutras, proposing that all physical matter—called dravya—can be "
            "divided only until you reach ultimate, eternal, indivisible particles called parmanus. Kanada reasoned "
            "that parmanus combine in pairs called dyads and threes called triads to form every visible substance! "
            "Around the fifth century BCE in ancient Greece, philosophers Leucippus and his student Democritus reached "
            "a remarkably similar insight, coining the word atomos, meaning indivisible or uncuttable. For centuries, "
            "however, these remained philosophical ideas without laboratory measurements. Then in 1808, English "
            "chemist John Dalton transformed philosophy into quantitative science with Dalton's Atomic Theory! Dalton "
            "proposed that all matter consists of tiny, indivisible atoms, atoms of a given element are identical "
            "in mass and properties, and atoms combine in simple whole-number ratios to form compounds—laying the "
            "unshakeable foundation of modern chemistry and quantitative science, proving that chemical reactions simply "
            "rearrange existing indivisible atoms in fixed whole-number ratios."
        ),
        "checkpoints": [
            {
                "question": "In Acharya Kanada's Vaisesika Sutras, what are the ultimate indivisible particles of matter (dravya) called?",
                "options": [
                    "Electrons",
                    "Parmanus (which combine into dyads and triads)",
                    "Protons",
                    "Neutrons"
                ],
                "answer": 1,
                "hint": "It is the Sanskrit root word still used for atom in India today.",
                "explanation": "Acharya Kanada proposed that dravya divides down to indivisible parmanus that combine into dyads and triads."
            },
            {
                "question": "What does the Greek word 'atomos' coined by Leucippus and Democritus mean, and who formulated the 1808 scientific theory?",
                "options": [
                    "Charged; Ernest Rutherford",
                    "Indivisible (uncuttable); John Dalton",
                    "Heavy sphere; James Chadwick",
                    "Orbiting; Niels Bohr"
                ],
                "answer": 1,
                "hint": "a-tomos literally means 'cannot be cut'.",
                "explanation": "Atomos means indivisible; John Dalton gave the first quantitative scientific atomic theory in 1808."
            }
        ]
    },
    {
        "id": 3,
        "title": "Discovery of Electron",
        "subtitle": "Section 8.2: Cathode Rays & J. J. Thomson (1897)",
        "speech": (
            "John Dalton believed atoms were completely indivisible, like solid billiard balls. Yet by the late "
            "nineteenth century, two breakthroughs—radioactivity and electrical conductivity through gases—proved "
            "that atoms CAN be broken into smaller subatomic particles! In 1897, British physicist J. J. Thomson "
            "performed a landmark experiment using a partially evacuated glass cathode ray tube. When he applied a "
            "high voltage across metal electrodes inside the tube, invisible rays streamed from the negative cathode "
            "toward the positive anode, producing a glow on a fluorescent screen! Thomson deflected these cathode rays "
            "using electric and magnetic fields, proving they consisted of tiny negatively charged particles. Even more "
            "astonishingly, whether he changed the gas inside the tube or swapped the metal of the electrodes, the "
            "particles always had the exact same charge-to-mass ratio! That proved these particles—named electrons—are "
            "universal constituents of ALL atoms! Each electron carries a tiny negative charge of minus one point "
            "six zero two times ten to the power minus nineteen coulombs, assigned a relative charge of minus one. "
            "Thomson won the 1906 Nobel Prize in Physics and led the famous Cavendish Laboratory, transforming "
            "how humanity understood matter at the subatomic scale forever, opening the door to modern electronics and "
            "quantum physics."
        ),
        "checkpoints": [
            {
                "question": "How did J. J. Thomson prove in 1897 that electrons are universal constituents of all atoms?",
                "options": [
                    "By burning gold foil in oxygen",
                    "Cathode rays had identical properties regardless of the gas or electrode metal used",
                    "By weighing water droplets",
                    "By splitting uranium with neutrons"
                ],
                "answer": 1,
                "hint": "He tested different gases and different cathode materials in the discharge tube.",
                "explanation": "Because cathode-ray particles were identical across all gases and electrodes, Thomson concluded electrons exist in all atoms."
            },
            {
                "question": "What are the absolute electric charge and relative charge of an electron?",
                "options": [
                    "+1.602 × 10⁻¹⁹ C; +1",
                    "-1.602 × 10⁻¹⁹ C; -1",
                    "0 C; 0",
                    "-1.602 × 10⁻¹⁰ C; -2"
                ],
                "answer": 1,
                "hint": "Electrons carry a unit negative charge.",
                "explanation": "An electron has a charge of -1.602 × 10⁻¹⁹ C, assigned a relative charge of -1."
            }
        ]
    },
    {
        "id": 4,
        "title": "Thomson's Atom Model",
        "subtitle": "Section 8.2.1: The Plum Pudding / Watermelon Model",
        "speech": (
            "Once J. J. Thomson discovered negatively charged electrons inside atoms, an immediate puzzle arose: if "
            "every atom contains negative electrons, why is normal matter electrically neutral? Why do you not get an "
            "electric shock every time you touch a wooden desk or a copper coin? To explain this, Thomson proposed "
            "his famous 1904 atomic model—popularly called the Plum Pudding Model, or in India, the Watermelon Model! "
            "Picture slicing open a ripe red watermelon: the sweet red edible pulp represents a uniform, continuous "
            "sphere of positive charge filling the entire atom, while the black seeds scattered throughout represent "
            "the negatively charged electrons embedded inside that positive sphere! In Thomson's model, the total "
            "positive charge of the sphere exactly equals the total negative charge of all embedded electrons, so "
            "their charges cancel out to make the whole atom electrically neutral. In our Pause and Ponder checks, "
            "if you build a clay-bead model where positive clay balances negative beads, removing two beads leaves "
            "a net positive charge! Though beautifully simple and explaining electrical neutrality, Thomson's model "
            "had no central nucleus and was about to face a decisive experimental test in Ernest Rutherford's "
            "famous physics laboratory using fast alpha rays."
        ),
        "checkpoints": [
            {
                "question": "In the Watermelon analogy of J. J. Thomson's model, what do the red pulp and black seeds represent?",
                "options": [
                    "Pulp = electrons; Seeds = neutrons",
                    "Pulp = uniform sphere of positive charge; Seeds = embedded negatively charged electrons",
                    "Pulp = empty space; Seeds = protons",
                    "Pulp = nucleus; Seeds = stationary orbits"
                ],
                "answer": 1,
                "hint": "Thomson imagined positive charge spread uniformly throughout the atom.",
                "explanation": "Thomson proposed a uniform positive sphere (red pulp) with negative electrons (seeds) embedded inside."
            },
            {
                "question": "How did Thomson's model explain that an atom as a whole is electrically neutral?",
                "options": [
                    "Atoms contain no charged particles",
                    "Total positive charge of the sphere equals total negative charge of embedded electrons",
                    "Neutrons cancel out the electrons",
                    "Electrons orbit outside the atom"
                ],
                "answer": 1,
                "hint": "Equal and opposite charges add up to zero.",
                "explanation": "In Thomson's model, the magnitude of positive and negative charges is equal, yielding zero net charge."
            }
        ]
    },
    {
        "id": 5,
        "title": "Gold Foil Experiment",
        "subtitle": "Section 8.2.2: Geiger & Marsden's Alpha Scattering (1911)",
        "speech": (
            "In 1911, Ernest Rutherford designed an experiment to test Thomson's watermelon model, carried out by "
            "his researchers Hans Geiger and Ernest Marsden. They fired a narrow beam of fast-moving, positively "
            "charged alpha particles—which are actually helium nuclei—at an ultra-thin sheet of hammered gold foil, "
            "only about one thousand atoms thick, surrounded by a circular zinc sulphide fluorescent screen! Now ask "
            "yourself: if Thomson's model were true, with positive charge spread thinly like soft watermelon pulp, "
            "what should happen? Heavy, high-speed alpha particles should plough straight through with tiny deflections "
            "at most! Indeed, most alpha particles passed straight through the foil undeflected. However, Geiger and "
            "Marsden witnessed something jaw-dropping: a small fraction of alpha particles were deflected through "
            "large angles, and about one in every twenty thousand bounced straight back toward the source! Rutherford "
            "famously remarked it was as incredible as firing a fifteen-inch artillery shell at a piece of tissue "
            "paper and watching it bounce back to hit you! Thomson's uniform positive sphere could never produce "
            "such a violent electrostatic repulsion—a brand new nuclear model of the atom was urgently needed "
            "to explain these shocking rebounds and rewrite our scientific picture of the atom completely."
        ),
        "checkpoints": [
            {
                "question": "Why did Rutherford expect almost all alpha particles to pass straight through the gold foil if Thomson's model were correct?",
                "options": [
                    "Alpha particles have zero charge",
                    "In Thomson's model, positive charge is spread too thinly to strongly repel heavy, fast alpha particles",
                    "Gold foil melts when hit by alpha rays",
                    "Electrons attract alpha particles backward"
                ],
                "answer": 1,
                "hint": "A diffuse positive sphere produces only weak local electric fields.",
                "explanation": "Thomson's diffuse positive charge could only cause tiny deflections, never a 180° rebound."
            },
            {
                "question": "What shocking observation in the 1911 gold foil experiment disproved Thomson's model?",
                "options": [
                    "All alpha particles stopped in the foil",
                    "A small fraction deflected at large angles, and ~1 in 20,000 bounced back sharply",
                    "Gold turned into lead",
                    "No flashes appeared on the zinc sulphide screen"
                ],
                "answer": 1,
                "hint": "About 1 in 20,000 alpha particles suffered nearly 180° back-scattering.",
                "explanation": "Large-angle deflections and 1-in-20,000 rebounds proved positive charge and mass are concentrated in a tiny core."
            }
        ]
    },
    {
        "id": 6,
        "title": "Rutherford's Nuclear Model",
        "subtitle": "Section 8.2.2 (A–C): Nucleus, Protons & Stability Limitation",
        "speech": (
            "From the gold foil results, Ernest Rutherford—honoured with the 1908 Nobel Prize in Chemistry and known "
            "as the Father of Nuclear Physics—deduced the Planetary Model of the atom! First, since most alpha "
            "particles passed straight through, most of the atom is empty space! Second, since a tiny fraction "
            "rebounded, all positive charge and nearly all mass must be packed into an extraordinarily tiny central "
            "core called the nucleus! The nucleus diameter is about ten to the minus fifteen metres—one hundred "
            "thousand times smaller than the atom's diameter of ten to the minus ten metres! Imagine a football "
            "stadium: the nucleus is like a tiny marble at the centre! Even so, stacking about one million atoms "
            "edge to edge equals just zero point one millimetres, the thickness of paper. Third, electrons revolve "
            "around this nucleus in circular orbits. Rutherford also established that the nucleus holds heavy "
            "positively charged protons, each with charge plus one balancing an electron's minus one! Yet Rutherford's "
            "model had one fatal flaw: classical electromagnetism says any accelerating charged electron in a circle "
            "must continuously radiate energy, spiral inward, and collapse into the nucleus within a fraction of a "
            "second—failing to explain atomic stability!"
        ),
        "checkpoints": [
            {
                "question": "How does the diameter of an atomic nucleus (~10⁻¹⁵ m) compare to the diameter of the whole atom (~10⁻¹⁰ m)?",
                "options": [
                    "The nucleus is 10 times larger",
                    "The nucleus is about 10⁵ (100,000) times smaller than the atom",
                    "They have the exact same diameter",
                    "The nucleus is half the atom's diameter"
                ],
                "answer": 1,
                "hint": "Compare 10⁻¹⁰ m divided by 10⁻¹⁵ m.",
                "explanation": "10⁻¹⁰ / 10⁻¹⁵ = 10⁵, meaning the nucleus is ~100,000 times smaller than the atom."
            },
            {
                "question": "What was the major limitation of Rutherford's planetary atomic model?",
                "options": [
                    "It could not explain protons",
                    "By classical electromagnetism, orbiting electrons should continuously radiate energy, spiral inward, and collapse",
                    "It assumed atoms are solid spheres",
                    "It placed protons outside the nucleus"
                ],
                "answer": 1,
                "hint": "Circular motion involves centripetal acceleration, and accelerating charges radiate EM waves.",
                "explanation": "Classical physics predicted orbiting electrons would lose energy and crash into the nucleus, contradicting atomic stability."
            }
        ]
    },
    {
        "id": 7,
        "title": "Bohr's Energy Levels",
        "subtitle": "Section 8.2.3: Stationary Orbits (K, L, M, N) & Niels Bohr (1913)",
        "speech": (
            "How did physics rescue the atom from collapsing? In 1913, Danish physicist Niels Bohr—who later won "
            "the 1922 Nobel Prize—proposed a bold quantum solution! Bohr stated that electrons cannot revolve at "
            "just any arbitrary distance around the nucleus. Instead, they are permitted to move ONLY in specific "
            "discrete circular paths called stationary states, orbits, or energy levels, labeled K, L, M, N and so on, "
            "corresponding to principal numbers n equals one, two, three, and four! Why do those letters start at K "
            "instead of A? Our Threads of Curiosity note reveals that physicist Charles Barkla originally labeled "
            "X-ray spectral lines starting at K to leave room for undiscovered deeper lines! Inside any stationary "
            "orbit, an electron does NOT radiate or lose energy—solving Rutherford's stability puzzle! Energy "
            "increases outward from the nucleus, so the K shell has lower energy than L, which has lower energy than "
            "M. An electron absorbs or emits a discrete packet of energy ONLY when it jumps from one permitted orbit "
            "orbit to another: jumping outward absorbs energy, while dropping inward emits light of specific colours! "
            "This quantum rule explained both atomic stability and the sharp coloured emission lines of glowing "
            "gases."
        ),
        "checkpoints": [
            {
                "question": "How did Niels Bohr's 1913 model solve the stability problem of Rutherford's atom?",
                "options": [
                    "By stopping all electrons from moving",
                    "Electrons move only in discrete stationary orbits (K, L, M, N...) where they do not radiate energy",
                    "By removing positive charge from the nucleus",
                    "By embedding electrons in positive pulp"
                ],
                "answer": 1,
                "hint": "Energy is only emitted or absorbed during transitions between permitted shells.",
                "explanation": "Bohr postulated that electrons in stationary orbits do not lose energy continuously."
            },
            {
                "question": "How do the energies of Bohr's shells K (n=1), L (n=2), and M (n=3) compare, and when is energy emitted?",
                "options": [
                    "E_K > E_L > E_M; emitted when jumping outward",
                    "E_K < E_L < E_M; emitted when an electron jumps from a higher outer shell to a lower inner shell",
                    "All shells have equal energy",
                    "Energy is emitted continuously inside every shell"
                ],
                "answer": 1,
                "hint": "Energy increases as you move farther from the nucleus.",
                "explanation": "Energy increases outward (E_K < E_L < E_M); dropping to a lower shell emits the energy difference."
            }
        ]
    },
    {
        "id": 8,
        "title": "Discovery of Neutron",
        "subtitle": "Sections 8.3 & 8.3.1: Mass Anomaly, Chadwick (1932) & BARC",
        "speech": (
            "By 1920, scientists knew about protons and electrons, yet a glaring mass puzzle remained! Hydrogen has "
            "one proton, and helium has two protons. Since electrons have negligible mass, helium ought to weigh "
            "twice as much as hydrogen—right? Wrong! Measurements showed helium actually weighs FOUR times as much "
            "as hydrogen! Clearly, another heavy particle with zero electric charge had to be hiding inside the "
            "nucleus! In 1932, English physicist James Chadwick solved this mystery by discovering the neutron, "
            "denoted n-zero! Look at Table 8.1: an electron has relative charge minus one, a proton has plus one, "
            "and a neutron has zero charge with a mass nearly equal to a proton! Neutrons perform a vital job in "
            "heavier nuclei: positively charged protons fiercely repel one another, so extra neutrons dilute that "
            "repulsion and supply the strong nuclear force that binds the nucleus together! In India's Scientific "
            "Contributions, remember Homi Jehangir Bhabha—the Father of the Indian Nuclear Programme—and the Bhabha "
            "Atomic Research Centre, BARC, in Mumbai, where the Dhruva research reactor harnesses neutrons for "
            "peaceful medicine, agriculture, and clean energy! Today, India's nuclear science stands on the exact "
            "subatomic discoveries pioneered by Chadwick and Bhabha, powering medical isotopes and clean energy."
        ),
        "checkpoints": [
            {
                "question": "What mass anomaly led James Chadwick to discover the neutron in 1932?",
                "options": [
                    "Electrons were heavier than protons",
                    "Helium has 2 protons (2× hydrogen's protons) yet weighs 4 times as much as hydrogen",
                    "Hydrogen had 4 protons",
                    "Gold foil had no mass"
                ],
                "answer": 1,
                "hint": "Two protons alone could only explain twice hydrogen's mass, not four times.",
                "explanation": "Helium contains 2 protons + 2 uncharged neutrons, explaining its 4:1 mass ratio relative to hydrogen."
            },
            {
                "question": "Which Indian institution houses the Dhruva research reactor, and who is called the Father of the Indian Nuclear Programme?",
                "options": [
                    "ISRO; Vikram Sarabhai",
                    "Bhabha Atomic Research Centre (BARC), Mumbai; Homi Jehangir Bhabha",
                    "Cavendish Lab; J. J. Thomson",
                    "CERN; Niels Bohr"
                ],
                "answer": 1,
                "hint": "The research centre in Mumbai is named after its visionary founder.",
                "explanation": "BARC in Mumbai operates the Dhruva reactor, founded under Homi Jehangir Bhabha's leadership."
            }
        ]
    }
]

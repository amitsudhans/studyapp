# -*- coding: utf-8 -*-
"""
Class 9 Science • Chapter 6: Structure of an Atom
Complete curriculum data with 20 slides:
- Slides 1-16: Core teaching slides with 32 in-slide checkpoints (2 per slide)
- Slides 17-20: Dedicated quiz challenges (10 questions each = 40 questions total)
Syllabus Competencies: C-1.1, C-1.3, C-5.1, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
"""

SLIDES_DATA = [
    # SLIDE 1
    {
        "id": 1,
        "title": "Historical Foundations: Acharya Kanad’s Parmanu to Subatomic Discoveries",
        "subtitle": "From Ancient Indivisibility Philosophies to the Cleavage of the Atom",
        "narration": "Welcome students! For centuries, humanity believed the atom was the ultimate, indivisible building block of matter. In ancient India around 600 BCE, the philosopher Acharya Kanad postulated that dividing matter repeatedly leads to 'Parmanu'—indivisible particles that cannot be further split. In 1808, John Dalton formalized this in Western science. However, late 19th-century electrical experiments shattered the idea of indivisibility, revealing that atoms are themselves composite structures made of subatomic particles!",
        "points": [
            "<strong>Acharya Kanad & Ancient Indian Philosophy (~600 BCE):</strong> In the Vaisheshika Darshana, Acharya Kanad formulated the concept of <em>Parmanu</em>—positing that if you divide a grain of matter repeatedly, you reach an ultimate indestructible particle beyond which division is impossible.",
            "<strong>Dalton's Indivisible Atom (1808):</strong> Postulated that atoms are tiny, hard, indivisible spheres that can neither be created nor destroyed during chemical combinations.",
            "<strong>Discovery of the Electron (J.J. Thomson, 1897):</strong> Through cathode ray discharge tube experiments under high voltage and vacuum, Thomson discovered negatively charged subatomic corpuscles—the <em>electron</em> ($e^-$).",
            "<strong>Discovery of Canal Rays / Proton (E. Goldstein, 1886):</strong> Discovered positively charged radiation in gas discharge tubes called canal rays, which led to the discovery of the positively charged <em>proton</em> ($p^+$).",
            "<strong>Discovery of the Neutron (James Chadwick, 1932):</strong> By bombarding a thin beryllium foil with alpha particles, Chadwick proved the existence of an uncharged neutral particle with mass nearly equal to that of a proton—the <em>neutron</em> ($n^0$)."
        ],
        "checkpoints": [
            {
                "q": "Which experimental breakthrough in 1897 disproved John Dalton's postulate that atoms are indivisible and indestructible?",
                "options": [
                    "Boyle's gas pressure experiments",
                    "J.J. Thomson's cathode ray discharge tube discovery of the electron",
                    "Röntgen's discovery of X-rays",
                    "Mendeleev's periodic table arrangement"
                ],
                "correct": 1,
                "explanation": "J.J. Thomson's cathode ray experiments proved that negatively charged electrons exist as subatomic constituents inside all atoms, directly disproving Dalton's postulate of atomic indivisibility."
            },
            {
                "q": "What ancient Indian concept was proposed by Acharya Kanad in the Vaisheshika philosophy regarding the ultimate nature of matter?",
                "options": [
                    "The four humors",
                    "The Parmanu—the ultimate, indivisible particle of matter",
                    "The concept of atomic radiation",
                    "The discovery of cathode rays"
                ],
                "correct": 1,
                "explanation": "Around the 6th century BCE, Acharya Kanad postulated the existence of 'Parmanu', defining it as the eternal and indivisible limit of material subdivision."
            }
        ]
    },

    # SLIDE 2
    {
        "id": 2,
        "title": "The Triad of Subatomic Particles: Electron, Proton & Neutron",
        "subtitle": "Charges, Relative Masses, SI Units, and Fundamental Roles in the Atom",
        "narration": "Every neutral atom is built from three fundamental subatomic particles: the positively charged proton, the electrically neutral neutron, and the negatively charged electron. Protons and neutrons are massive and reside packed tightly inside the atomic nucleus, while electrons have negligible mass and orbit in the outer space.",
        "points": [
            "<strong>The Electron ($e^-$):</strong> Discovered by J.J. Thomson (1897). Carries a single unit negative charge: $-1.602 \\times 10^{-19}\\text{ C}$ (relative charge: $-1$). Negligible rest mass: $9.109 \\times 10^{-31}\\text{ kg} \\approx \\frac{1}{1840}\\text{ u}$.",
            "<strong>The Proton ($p^+$):</strong> Discovered by E. Goldstein (1886). Carries a single unit positive charge: $+1.602 \\times 10^{-19}\\text{ C}$ (relative charge: $+1$). Rest mass: $1.673 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}$ (approx. $1836$ times heavier than an electron).",
            "<strong>The Neutron ($n^0$):</strong> Discovered by James Chadwick (1932). Electrically neutral: charge $0\\text{ C}$. Rest mass: $1.675 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}$ (slightly heavier than a proton).",
            "<strong>Nucleons:</strong> Protons and neutrons are bound together in the microscopic atomic nucleus by the fundamental strong nuclear force; collectively they are termed <em>nucleons</em>.",
            "<strong>Ordinary Hydrogen Exception:</strong> Ordinary Protium (${}_1^1\\text{H}$) is the ONLY atom in the universe that contains NO neutrons (consists of $1\\text{ proton}$ and $1\\text{ electron}$)."
        ],
        "checkpoints": [
            {
                "q": "Which subatomic particle has approximately 1/1840th the mass of a hydrogen atom?",
                "options": [
                    "Alpha particle",
                    "Proton",
                    "Neutron",
                    "Electron"
                ],
                "correct": 3,
                "explanation": "An electron has a rest mass of ~9.1 × 10⁻³¹ kg, which is approximately 1/1840 (or 1/1836) the mass of a proton or hydrogen atom, making its mass negligible in mass number calculations."
            },
            {
                "q": "Which of the following atoms contains NO neutrons in its nucleus?",
                "options": [
                    "Helium-4",
                    "Protium (Ordinary Hydrogen, ¹H)",
                    "Deuterium (Heavy Hydrogen, ²H)",
                    "Carbon-12"
                ],
                "correct": 1,
                "explanation": "Ordinary hydrogen (Protium, ¹₁H) has mass number A=1 and atomic number Z=1, meaning it contains 1 proton and 0 neutrons."
            }
        ]
    },

    # SLIDE 3
    {
        "id": 3,
        "title": "J.J. Thomson’s Atomic Model: The Plum Pudding / Watermelon Model",
        "subtitle": "The First Classical Atomic Architecture (1904) & Its Fundamental Limitations",
        "narration": "Following his discovery of the electron in 1897, J.J. Thomson proposed the first scientific model of the atom in 1904. He visualized an atom as a positively charged sphere in which electrons are embedded like dry raisins in a Christmas pudding, or black seeds embedded in the red edible pulp of a watermelon.",
        "points": [
            "<strong>Thomson's Postulates:</strong><br>1. An atom consists of a uniform sphere of positive electricity of radius approximately $10^{-10}\\text{ m}$.<br>2. Negatively charged electrons are embedded throughout this positive sphere, like plums in a pudding or seeds in a watermelon.",
            "<strong>Electrical Neutrality Explained:</strong> The total negative charge of the embedded electrons is equal in magnitude to the total positive charge of the sphere, making the atom electrically neutral overall.",
            "<strong>Key Strength:</strong> First model to successfully account for the electrical neutrality of matter and the presence of subatomic electrons without chemical destruction.",
            "<strong>Fatal Limitation:</strong> Thomson's model predicted that positive charge was spread uniformly throughout the atomic volume. It could NOT explain the results of alpha-particle scattering experiments conducted later by Ernest Rutherford!"
        ],
        "checkpoints": [
            {
                "q": "In J.J. Thomson's watermelon analogy of the atom, what does the red edible flesh of the watermelon represent?",
                "options": [
                    "Negatively charged electrons",
                    "Positively charged uniform spherical matter",
                    "The empty space inside the atom",
                    "Electrically neutral neutrons"
                ],
                "correct": 1,
                "explanation": "In Thomson's watermelon model, the red edible pulp represents the continuous positive charge sphere, while the black seeds embedded inside represent the electrons."
            },
            {
                "q": "Why was J.J. Thomson's atomic model ultimately discarded by physicists?",
                "options": [
                    "It failed to explain why atoms are electrically neutral",
                    "It could not explain how high-energy alpha particles could be deflected at large angles in scattering experiments",
                    "It claimed that atoms have no mass",
                    "It predicted that electrons carry a positive charge"
                ],
                "correct": 1,
                "explanation": "Because Thomson assumed positive charge was diffuse and spread out thinly over the entire atom, it could never exert the immense concentrated repulsive force needed to bounce heavy alpha particles backwards."
            }
        ]
    },

    # SLIDE 4
    {
        "id": 4,
        "title": "Rutherford’s Alpha Particle Scattering Experiment (1911)",
        "subtitle": "Probing the Interior of the Atom with Fast-Moving Helium Nuclei",
        "narration": "In 1911, Ernest Rutherford, along with Hans Geiger and Ernest Marsden, designed an experiment that revolutionized our view of matter. They directed a beam of fast-moving, high-energy alpha particles (doubly charged helium ions, He²⁺) at an ultra-thin gold foil, observing where the particles struck a fluorescent zinc sulfide screen.",
        "points": [
            "<strong>Experimental Apparatus:</strong><br>• Alpha particle source: Radioactive element (Bismuth/Radium) emitting high-energy $\\alpha$-particles (mass $4\\text{ u}$, charge $+2e$).<br>• Target: Gold foil beaten to extreme thinness (approx. $1000\\text{ atoms}$ thick, $\\sim 100\\text{ nm}$). Gold was chosen because it has the highest malleability of all metals.<br>• Detector: Circular zinc sulfide ($\\text{ZnS}$) fluorescent screen that produced micro-scintillations (flashes of light) when struck by $\\alpha$-particles.",
            "<strong>Unexpected Observations:</strong><br>1. <em>Most $\\alpha$-particles ($>99.9\\%$)</em> passed straight through the gold foil without any deflection.<br>2. <em>A small fraction</em> were deflected by small angles ($1^\\circ\\text{ to }10^\\circ$).<br>3. <em>Astonishingly rare:</em> Approximately $1$ out of every $12,000$ particles rebounded backwards ($>90^\\circ$ or even $180^\\circ$).",
            "<strong>Rutherford's Famous Reaction:</strong> 'It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you!'"
        ],
        "checkpoints": [
            {
                "q": "Why did Ernest Rutherford select gold foil rather than aluminium or copper for his alpha scattering experiment?",
                "options": [
                    "Gold is radioactive and emits its own alpha particles",
                    "Gold is the most malleable metal and can be hammered into an ultra-thin layer only ~1000 atoms thick",
                    "Gold has no electrons in its atoms",
                    "Gold absorbs 100% of the alpha radiation"
                ],
                "correct": 1,
                "explanation": "Rutherford required the thinnest possible metallic target so that alpha particles would interact with as few atomic layers as possible; gold's exceptional malleability enabled foils only ~100 nm thick."
            },
            {
                "q": "What conclusion did Rutherford deduce from the fact that most alpha particles passed straight through the gold foil without any deflection?",
                "options": [
                    "Most of the space inside an atom is completely empty",
                    "The atom is a solid sphere of positive charge",
                    "Alpha particles carry zero mass",
                    "Electrons attract alpha particles with immense gravitational force"
                ],
                "correct": 0,
                "explanation": "Because over 99.9% of alpha particles passed unhindered through the foil without feeling any repulsive force, Rutherford concluded that most of the space inside the atom is completely empty."
            }
        ]
    },

    # SLIDE 5
    {
        "id": 5,
        "title": "Rutherford’s Nuclear Model & The Maxwell Collapse Dilemma",
        "subtitle": "Discovery of the Dense Nucleus and the Theoretical Crisis of Accelerating Charges",
        "narration": "From his scattering observations, Rutherford concluded that all the positive charge and virtually all the mass of an atom are concentrated in an unimaginably tiny, dense central core called the nucleus. While revolutionary, his model faced a fatal theoretical crisis under classical physics: revolving electrons are accelerating charges, and classical electrodynamics dictates they must radiate energy and spiral into the nucleus within a split microsecond!",
        "points": [
            "<strong>Rutherford's Nuclear Model Postulates:</strong><br>1. There is a positively charged, extremely dense center in an atom called the <em>nucleus</em>. Nearly all the mass of an atom resides in the nucleus.<br>2. The electrons revolve around the nucleus in circular planetary paths.<br>3. The size of the nucleus is minuscule compared to the atom: radius of nucleus is $\\sim 10^{-15}\\text{ m}$, while radius of atom is $\\sim 10^{-10}\\text{ m}$ (a factor of $10^5$, like a cricket ball in a huge 5-kilometer stadium!).",
            "<strong>The Drawback / Classical Crisis (Maxwell's Electrodynamics):</strong><br>• Any particle in circular motion undergoes centripetal acceleration ($a = v^2/r$).<br>• According to James Clerk Maxwell's classical electromagnetic theory, an accelerating charged particle must continuously radiate electromagnetic energy.<br>• As the orbiting electron loses energy, its orbital radius must shrink continuously, spiraling into the nucleus in less than $10^{-8}\\text{ seconds}$!<br>• This implied matter should spontaneously collapse into a dead mass, yet real atoms are exceptionally stable."
        ],
        "checkpoints": [
            {
                "q": "According to classical electromagnetic theory (Maxwell), why was Rutherford's planetary model of revolving electrons considered unstable?",
                "options": [
                    "Revolving electrons would lose charge and turn into neutrons",
                    "Accelerating revolving electrons would continuously radiate energy, shrink their orbits, and spiral into the nucleus in ~10⁻⁸ seconds",
                    "The positive nucleus would repel the electrons outwards into space",
                    "Centrifugal force would fling the nucleus apart"
                ],
                "correct": 1,
                "explanation": "Classical physics dictates that any charged particle undergoing circular acceleration must radiate energy. An electron radiating energy would rapidly spiral into the nucleus, causing atomic collapse."
            },
            {
                "q": "If an atom has a diameter of approximately 10⁻¹⁰ m (0.1 nm), what is the approximate diameter of its nucleus based on Rutherford's deductions?",
                "options": [
                    "10⁻¹⁰ m",
                    "10⁻¹⁵ m",
                    "10⁻⁵ m",
                    "10⁻² m"
                ],
                "correct": 1,
                "explanation": "The atomic nucleus is approximately 100,000 times smaller than the atom itself: atomic diameter ~10⁻¹⁰ m, nuclear diameter ~10⁻¹⁵ m."
            }
        ]
    },

    # SLIDE 6
    {
        "id": 6,
        "title": "Neils Bohr’s Model of the Atom: Discrete Stationary Orbits (1913)",
        "subtitle": "Quantization of Energy Levels (K, L, M, N...) and Quantum Transitions",
        "narration": "In 1913, Danish physicist Niels Bohr rescued atomic physics from the Maxwell collapse paradox. He applied Max Planck's quantum theory to Rutherford's nuclear model, postulating that electrons do NOT radiate energy when revolving in certain special, non-radiating orbits called discrete energy levels. Radiation is emitted or absorbed only when an electron jumps between these fixed levels!",
        "points": [
            "<strong>Bohr's Postulate 1 (Discrete Stationary Orbits):</strong> Only certain special orbits known as <em>discrete orbits</em> (or non-radiating stationary energy levels) of electrons are permitted inside the atom.",
            "<strong>Bohr's Postulate 2 (Energy Invariance):</strong> While revolving in these discrete orbits, the electrons do NOT radiate energy. Hence, the electron does not lose energy and will never spiral into the nucleus.",
            "<strong>Energy Level Nomenclature:</strong> These orbits or shells are designated by capital letters <strong>K, L, M, N...</strong> or by primary quantum numbers <strong>n = 1, 2, 3, 4...</strong> counting outward from the nucleus.",
            "• Shell $n = 1$ is the innermost <strong>K-shell</strong> (lowest energy ground state).<br>• Shell $n = 2$ is the <strong>L-shell</strong>.<br>• Shell $n = 3$ is the <strong>M-shell</strong>.<br>• Shell $n = 4$ is the <strong>N-shell</strong>.",
            "<strong>Quantum Jumps (Spectroscopy):</strong> An electron absorbs a photon of energy $\\Delta E = h\\nu$ when jumping from a lower energy orbit to an outer higher orbit, and emits a photon when falling back from a higher orbit to a lower orbit."
        ],
        "checkpoints": [
            {
                "q": "How did Niels Bohr resolve the fatal drawback of Rutherford's model regarding the stability of the atom?",
                "options": [
                    "He claimed that electrons have positive charge inside the atom",
                    "He postulated that electrons revolve only in discrete, non-radiating stationary orbits where they do not lose energy",
                    "He asserted that protons revolve around stationary electrons",
                    "He argued that nuclear gravity prevents electromagnetic radiation"
                ],
                "correct": 1,
                "explanation": "Bohr proposed that electrons occupy discrete non-radiating stationary energy shells (K, L, M, N), overcoming the classical prediction of continuous radiative energy loss."
            },
            {
                "q": "What happens when an electron jumps from the L-shell (n=2) down to the K-shell (n=1)?",
                "options": [
                    "The electron absorbs a photon of light",
                    "The electron emits a discrete quantum of energy (photon) equal to the energy difference between the shells",
                    "The electron is destroyed completely",
                    "The nucleus expands by 50%"
                ],
                "correct": 1,
                "explanation": "Dropping from a higher energy state (L-shell) to a lower energy state (K-shell) releases the exact energy difference (ΔE = E₂ - E₁) as emitted electromagnetic radiation."
            }
        ]
    },

    # SLIDE 7
    {
        "id": 7,
        "title": "The Bohr-Bury Rules of Electron Distribution",
        "subtitle": "The 2n² Law, Octet Ceiling, and Step-wise Electronic Architecture",
        "narration": "How are electrons arranged in the different shells around the nucleus? In 1921, Niels Bohr and Charles Bury formulated three fundamental rules that govern the electronic configuration of elements. Knowing these rules allows you to predict how every atom bonds and behaves chemically!",
        "points": [
            "<strong>Rule 1: Maximum Electron Capacity ($2n^2$ Rule):</strong> The maximum number of electrons that can be accommodated in a given energy level or shell is given by the formula $2n^2$, where $n$ is the principal orbit number:<br>• For <strong>K-shell</strong> ($n=1$): $\\text{Max} = 2(1)^2 = 2\\text{ electrons}$<br>• For <strong>L-shell</strong> ($n=2$): $\\text{Max} = 2(2)^2 = 8\\text{ electrons}$<br>• For <strong>M-shell</strong> ($n=3$): $\\text{Max} = 2(3)^2 = 18\\text{ electrons}$<br>• For <strong>N-shell</strong> ($n=4$): $\\text{Max} = 2(4)^2 = 32\\text{ electrons}$",
            "<strong>Rule 2: The Outermost Octet Ceiling:</strong> The maximum number of electrons that can be accommodated in the outermost valence shell is strictly <strong>8</strong>, even if that shell has the capacity under the $2n^2$ rule to hold more electrons.",
            "<strong>Rule 3: Step-wise Progressive Filling:</strong> Electrons are not accommodated in a given outer shell unless the inner shells are completely filled. Shells are filled in a progressive step-wise manner from lowest energy ($n=1$) to higher levels."
        ],
        "checkpoints": [
            {
                "q": "What is the theoretical maximum electron capacity of the third energy shell (M-shell, n = 3)?",
                "options": [
                    "8 electrons",
                    "18 electrons",
                    "32 electrons",
                    "2 electrons"
                ],
                "correct": 1,
                "explanation": "Using the 2n² formula for n = 3: Maximum capacity = 2 × (3)² = 2 × 9 = 18 electrons."
            },
            {
                "q": "Even though the M-shell (n=3) can hold up to 18 electrons, what is the maximum number of electrons permitted in it when it serves as the outermost valence shell?",
                "options": [
                    "2 electrons",
                    "18 electrons",
                    "8 electrons",
                    "32 electrons"
                ],
                "correct": 2,
                "explanation": "Under Bohr-Bury Rule 2, the outermost shell of an atom can never hold more than 8 electrons (octet rule) for stability, regardless of its theoretical 2n² capacity."
            }
        ]
    },

    # SLIDE 8
    {
        "id": 8,
        "title": "Electronic Configurations of the First 18 Elements",
        "subtitle": "Step-by-Step Shell Filling from Hydrogen (Z=1) to Argon (Z=18)",
        "narration": "Let us systematically distribute electrons across shells for the first 18 elements of the periodic table, following IUPAC conventions. Observe how the K-shell fills first with up to 2 electrons, followed by the L-shell with up to 8 electrons, and then the M-shell up to Argon with configuration (2, 8, 8).",
        "points": [
            "<strong>Period 1 (K-shell Filling):</strong><br>• <strong>Hydrogen (${}_1\\text{H}$):</strong> $1$ electron $\\to$ K: $1$<br>• <strong>Helium (${}_2\\text{He}$):</strong> $2$ electrons $\\to$ K: $2$ (Duplet complete; highly stable noble gas)",
            "<strong>Period 2 (L-shell Filling from 1 to 8):</strong><br>• <strong>Lithium (${}_3\\text{Li}$):</strong> K: $2$, L: $1$<br>• <strong>Beryllium (${}_4\\text{Be}$):</strong> K: $2$, L: $2$<br>• <strong>Boron (${}_5\\text{B}$):</strong> K: $2$, L: $3$<br>• <strong>Carbon (${}_6\\text{C}$):</strong> K: $2$, L: $4$<br>• <strong>Nitrogen (${}_7\\text{N}$):</strong> K: $2$, L: $5$<br>• <strong>Oxygen (${}_8\\text{O}$):</strong> K: $2$, L: $6$<br>• <strong>Fluorine (${}_9\\text{F}$):</strong> K: $2$, L: $7$<br>• <strong>Neon (${}_{10}\\text{Ne}$):</strong> K: $2$, L: $8$ (Octet complete; inert noble gas)",
            "<strong>Period 3 (M-shell Filling from 1 to 8):</strong><br>• <strong>Sodium (${}_{11}\\text{Na}$):</strong> K: $2$, L: $8$, M: $1$<br>• <strong>Magnesium (${}_{12}\\text{Mg}$):</strong> K: $2$, L: $8$, M: $2$<br>• <strong>Aluminium (${}_{13}\\text{Al}$):</strong> K: $2$, L: $8$, M: $3$<br>• <strong>Silicon (${}_{14}\\text{Si}$):</strong> K: $2$, L: $8$, M: $4$<br>• <strong>Phosphorus (${}_{15}\\text{P}$):</strong> K: $2$, L: $8$, M: $5$<br>• <strong>Sulfur (${}_{16}\\text{S}$):</strong> K: $2$, L: $8$, M: $6$<br>• <strong>Chlorine (${}_{17}\\text{Cl}$):</strong> K: $2$, L: $8$, M: $7$<br>• <strong>Argon (${}_{18}\\text{Ar}$):</strong> K: $2$, L: $8$, M: $8$ (Stable valence octet; noble gas)"
        ],
        "checkpoints": [
            {
                "q": "What is the correct electronic configuration of a neutral phosphorus atom (Atomic number Z = 15)?",
                "options": [
                    "K: 2, L: 8, M: 5",
                    "K: 2, L: 5, M: 8",
                    "K: 8, L: 2, M: 5",
                    "K: 2, L: 13"
                ],
                "correct": 0,
                "explanation": "Phosphorus (Z=15) fills K-shell with 2 electrons, L-shell with 8 electrons, and the remaining 5 electrons enter the M-shell, giving configuration (2, 8, 5)."
            },
            {
                "q": "Which of the following elements has a completely filled valence shell with a stable octet (8 electrons)?",
                "options": [
                    "Sodium (Z = 11)",
                    "Chlorine (Z = 17)",
                    "Argon (Z = 18)",
                    "Aluminium (Z = 13)"
                ],
                "correct": 2,
                "explanation": "Argon (Z = 18) has electronic configuration (2, 8, 8), possessing 8 electrons in its outermost M-shell, which gives it a stable, unreactive noble gas octet."
            }
        ]
    },

    # SLIDE 9
    {
        "id": 9,
        "title": "Valence Electrons & Valency as Combining Capacity",
        "subtitle": "The Octet Driving Force: Chemical Bonding, Electron Gain/Loss, and Sharing",
        "narration": "The electrons present in the outermost shell of an atom are called valence electrons. They determine the entire chemical personality of an element! An atom's combining capacity—the number of electrons it must gain, lose, or share to attain a stable octet or duplet—is defined as its valency.",
        "points": [
            "<strong>Valence Electrons:</strong> The number of electrons located in the outermost shell (valence shell) of an atom. For example, Sodium (${}_{11}\\text{Na}$: $2,8,1$) has $1$ valence electron; Oxygen (${}_8\\text{O}$: $2,6$) has $6$ valence electrons.",
            "<strong>The Octet Rule of Chemical Stability:</strong> Atoms of elements combine with one another to achieve a completely filled, energetically stable outermost shell of $8$ electrons (or $2$ electrons for Helium).",
            "<strong>Rules for Calculating Valency:</strong><br>• If valence electrons ($v$) are $1, 2, 3,\\text{ or }4$: $\\text{Valency} = v$.<br>  - Sodium ($v=1$): Loses $1\\ e^- \\to \\text{Valency} = 1$<br>  - Magnesium ($v=2$): Loses $2\\ e^- \\to \\text{Valency} = 2$<br>  - Aluminium ($v=3$): Loses $3\\ e^- \\to \\text{Valency} = 3$<br>  - Carbon ($v=4$): Shares $4\\ e^- \\to \\text{Valency} = 4$",
            "• If valence electrons ($v$) are $5, 6,\\text{ or }7$: $\\text{Valency} = 8 - v$.<br>  - Nitrogen ($v=5$): Gains $3\\ e^- \\to \\text{Valency} = 8 - 5 = 3$<br>  - Oxygen ($v=6$): Gains $2\\ e^- \\to \\text{Valency} = 8 - 6 = 2$<br>  - Chlorine ($v=7$): Gains $1\\ e^- \\to \\text{Valency} = 8 - 7 = 1$",
            "<strong>Noble Gases ($He, Ne, Ar$):</strong> Outermost shell is already completely filled; combining capacity is zero ($\\text{Valency} = 0$)."
        ],
        "checkpoints": [
            {
                "q": "Why does oxygen (atomic number Z = 8) have a valency of 2, even though it possesses 6 valence electrons?",
                "options": [
                    "Because oxygen loses all 6 electrons during bonding",
                    "Because it is energetically easier for oxygen to gain 2 electrons to complete its octet (8 - 6 = 2)",
                    "Because oxygen has 2 protons in its nucleus",
                    "Because oxygen is a noble gas"
                ],
                "correct": 1,
                "explanation": "With 6 valence electrons, oxygen needs 2 more electrons to attain a stable 8-electron octet. Therefore, its combining capacity (valency) is 8 - 6 = 2."
            },
            {
                "q": "What is the valency of neon (Atomic number Z = 10, configuration 2, 8)?",
                "options": [
                    "8",
                    "2",
                    "0",
                    "1"
                ],
                "correct": 2,
                "explanation": "Neon has a completely filled outermost shell with 8 electrons (stable octet). It neither gains, loses, nor shares electrons, so its valency is 0."
            }
        ]
    },

    # SLIDE 10
    {
        "id": 10,
        "title": "Atomic Number (Z), Mass Number (A) & Standard IUPAC Notation",
        "subtitle": "Deciphering Subatomic Counts: p⁺, e⁻, n⁰ and Nuclear Invariants",
        "narration": "Two numbers uniquely identify any atom: the atomic number, Z, which defines what element it is, and the mass number, A, which tells us how heavy its nucleus is. In standard IUPAC notation, we write the chemical symbol with the mass number as an upper prefix and the atomic number as a lower prefix: ᴬ_Z X.",
        "points": [
            "<strong>Atomic Number ($Z$):</strong> The total number of protons present in the nucleus of an atom. It is the fundamental chemical identity of an element ($Z$ never changes in chemical reactions).<br>$$\\text{In a neutral atom: } Z = \\text{Number of protons} = \\text{Number of electrons}$$",
            "<strong>Mass Number ($A$):</strong> The total number of nucleons (protons + neutrons) residing inside the nucleus.<br>$$A = \\text{Number of protons } (Z) + \\text{Number of neutrons } (N)$$",
            "<strong>Calculating Number of Neutrons ($N$):</strong><br>$$N = A - Z = \\text{Mass Number} - \\text{Atomic Number}$$",
            "<strong>Standard IUPAC Notation:</strong> Written as ${}_Z^A\\text{X}$, where $\\text{X}$ is the element symbol.<br>• Example: ${}_{11}^{23}\\text{Na}$ indicates Sodium with $Z=11$ protons, $11$ electrons, and $N = 23 - 11 = 12$ neutrons.",
            "• Example: ${}_{17}^{35}\\text{Cl}$ indicates Chlorine with $Z=17$ protons, $17$ electrons, and $N = 35 - 17 = 18$ neutrons."
        ],
        "checkpoints": [
            {
                "q": "An atom has an atomic number Z = 13 and a mass number A = 27. How many electrons, protons, and neutrons does this neutral atom contain?",
                "options": [
                    "Protons: 13, Electrons: 13, Neutrons: 14",
                    "Protons: 14, Electrons: 13, Neutrons: 13",
                    "Protons: 13, Electrons: 14, Neutrons: 27",
                    "Protons: 27, Electrons: 13, Neutrons: 14"
                ],
                "correct": 0,
                "explanation": "For neutral atom: Protons = Z = 13; Electrons = Z = 13; Neutrons = A - Z = 27 - 13 = 14 (this is Aluminium, ²⁷₁₃Al)."
            },
            {
                "q": "The notation ⁴⁰₂₀Ca represents a neutral calcium atom. How many neutrons are in its nucleus?",
                "options": [
                    "40",
                    "20",
                    "60",
                    "10"
                ],
                "correct": 1,
                "explanation": "Neutrons = Mass Number (A) - Atomic Number (Z) = 40 - 20 = 20 neutrons."
            }
        ]
    },

    # SLIDE 11
    {
        "id": 11,
        "title": "Isotopes: Same Atomic Number, Different Mass Numbers",
        "subtitle": "Nuclear Variants with Identical Chemistry: Protium, Deuterium & Tritium",
        "narration": "Isotopes are atoms of the same element that possess the exact same atomic number (number of protons) but different mass numbers due to differing numbers of neutrons. Because they have identical electron configurations, isotopes exhibit identical chemical properties, but slightly different physical properties like mass and density.",
        "points": [
            "<strong>Definition of Isotopes:</strong> Atoms of the same element that have the same atomic number ($Z$) but different mass numbers ($A$). They have the same number of protons and electrons, but different numbers of neutrons.",
            "<strong>The Three Isotopes of Hydrogen:</strong><br>1. <strong>Protium (${}_1^1\\text{H}$):</strong> $1\\text{ proton}, 0\\text{ neutrons}, 1\\text{ electron}$ (approx. $99.98\\%$ of natural hydrogen).<br>2. <strong>Deuterium (${}_1^2\\text{H}$ or $\\text{D}$):</strong> $1\\text{ proton}, 1\\text{ neutron}, 1\\text{ electron}$ (Heavy hydrogen; forms heavy water $\\text{D}_2\\text{O}$ used as nuclear moderator).<br>3. <strong>Tritium (${}_1^3\\text{H}$ or $\\text{T}$):</strong> $1\\text{ proton}, 2\\text{ neutrons}, 1\\text{ electron}$ (Radioactive isotope with half-life $12.3\\text{ years}$).",
            "<strong>Other Common Isotope Pairs:</strong><br>• Carbon: Carbon-12 (${}_6^{12}\\text{C}$) and Carbon-14 (${}_6^{14}\\text{C}$, used in archaeological carbon dating).<br>• Chlorine: Chlorine-35 (${}_{17}^{35}\\text{Cl}$) and Chlorine-37 (${}_{17}^{37}\\text{Cl}$).",
            "<strong>Chemical vs Physical Properties:</strong> Since chemical reactions depend entirely on valence electrons, all isotopes of an element participate in identical chemical reactions. Physical properties (density, boiling point, mass) differ because of differing masses."
        ],
        "checkpoints": [
            {
                "q": "Why do the two isotopes of carbon (Carbon-12 and Carbon-14) exhibit identical chemical reactions with oxygen to form CO₂?",
                "options": [
                    "They have the exact same number of neutrons in their nucleus",
                    "They have the exact same atomic number (Z=6) and identical electronic configuration (2, 4)",
                    "They possess identical radioactive decay rates",
                    "Carbon-14 has no electrons"
                ],
                "correct": 1,
                "explanation": "Chemical behavior is dictated entirely by electronic configuration and valence electrons; since all isotopes of carbon have 6 electrons (configuration 2, 4), they react identically."
            },
            {
                "q": "How many neutrons are present in a nucleus of Tritium (³₁H)?",
                "options": [
                    "1 neutron",
                    "2 neutrons",
                    "3 neutrons",
                    "0 neutrons"
                ],
                "correct": 1,
                "explanation": "In Tritium (³₁H), Mass number A = 3 and Atomic number Z = 1. Number of neutrons N = A - Z = 3 - 1 = 2 neutrons."
            }
        ]
    },

    # SLIDE 12
    {
        "id": 12,
        "title": "Fractional Atomic Mass & The Chlorine Puzzle: 35.5 u",
        "subtitle": "Weighted Average Atomic Masses Derived from Natural Isotopic Abundances",
        "narration": "Have you ever wondered why the periodic table shows the atomic mass of Chlorine as 35.5 u rather than a whole integer number? The atomic mass of an element is the weighted average of the masses of its naturally occurring isotopes, weighted by their natural percentage abundances in nature.",
        "points": [
            "<strong>The Origin of Non-Integer Atomic Masses:</strong> In nature, most elements exist as mixtures of two or more isotopes in fixed percentage proportions.",
            "<strong>Chlorine Case Study (${}_{17}^{35}\\text{Cl}$ and ${}_{17}^{37}\\text{Cl}$):</strong><br>• Naturally occurring chlorine consists of two major isotopes in a $3:1$ ratio:<br>  - Chlorine-35 (${}_{17}^{35}\\text{Cl}$) with abundance $\\approx 75\\%$ (or $\\frac{3}{4}$).<br>  - Chlorine-37 (${}_{17}^{37}\\text{Cl}$) with abundance $\\approx 25\\%$ (or $\\frac{1}{4}$).",
            "<strong>Step-by-Step Calculation of Average Atomic Mass:</strong><br>$$\\text{Average Atomic Mass} = \\left(35 \\times \\frac{75}{100}\\right) + \\left(37 \\times \\frac{25}{100}\\right)$$<br>$$= \\left(35 \\times \\frac{3}{4}\\right) + \\left(37 \\times \\frac{1}{4}\\right) = \\frac{105}{4} + \\frac{37}{4} = \\frac{142}{4} = 35.5\\text{ u}$$",
            "<strong>Important Conceptual Note:</strong> This does NOT mean that an individual atom of chlorine has a mass of $35.5\\text{ u}$. Any single chlorine atom has a mass of either $35\\text{ u}$ or $37\\text{ u}$. But in any macroscopic sample, the average mass per atom is $35.5\\text{ u}$."
        ],
        "checkpoints": [
            {
                "q": "If element X has two isotopes: X-10 (20% natural abundance) and X-11 (80% natural abundance), what is the average atomic mass of element X?",
                "options": [
                    "10.5 u",
                    "10.8 u",
                    "11.0 u",
                    "10.2 u"
                ],
                "correct": 1,
                "explanation": "Average mass = (10 × 20/100) + (11 × 80/100) = 2.0 + 8.8 = 10.8 u."
            },
            {
                "q": "Does any single individual chlorine atom ever have a mass of 35.5 u?",
                "options": [
                    "Yes, 75% of chlorine atoms have a mass of 35.5 u",
                    "No; every individual chlorine atom has a whole-number mass of either 35 u or 37 u, and 35.5 u is the statistical weighted average",
                    "Yes, during chemical combination",
                    "Yes, when chlorine is cooled to absolute zero"
                ],
                "correct": 1,
                "explanation": "Atoms contain discrete integer numbers of nucleons. Individual chlorine atoms have mass 35 u (18 neutrons) or 37 u (20 neutrons); 35.5 u is solely the weighted average of the mixture."
            }
        ]
    },

    # SLIDE 13
    {
        "id": 13,
        "title": "Societal Applications of Radioisotopes: Medicine, Energy & Archeology",
        "subtitle": "Cancer Radiotherapy, Thyroid Endocrinology, Nuclear Fission & Carbon Dating (C-5.3)",
        "narration": "Because radioactive isotopes decay at precise exponential rates and emit high-energy radiation (gamma rays and beta particles), they have revolutionized modern medicine, agricultural science, and clean electricity generation, directly impacting millions of lives every single day.",
        "points": [
            "<strong>Cobalt-60 (${}^{60}\\text{Co}$) in Cancer Radiotherapy:</strong> Emits highly penetrating, collimated gamma ($\\gamma$) radiation used in teletherapy to destroy deep-seated malignant cancer cells and tumors while sparing surrounding tissue.",
            "<strong>Iodine-131 (${}^{131}\\text{I}$) in Thyroid Endocrinology:</strong> The thyroid gland selectively absorbs iodine. Administering radioactive ${}^{131}\\text{I}$ allows imaging of thyroid function and targeted radiation destruction of hyperthyroid tissue and goitres.",
            "<strong>Uranium-235 (${}^{235}\\text{U}$) in Nuclear Power Generation:</strong> Undergoes thermal neutron-induced nuclear fission inside nuclear power reactors, releasing $\\approx 200\\text{ MeV}$ per fission to generate clean baseload electricity.",
            "<strong>Carbon-14 (${}^{14}\\text{C}$) in Radiocarbon Archaeological Dating:</strong> Has a half-life of $5,730\\text{ years}$. Used to date fossilized organic remains, ancient wooden tools, and prehistoric human settlements.",
            "<strong>Sodium-24 (${}^{24}\\text{Na}$) in Vascular Medicine:</strong> Injected as a saline tracer into the bloodstream to detect circulatory obstructions, thrombosis, and arterial blood clots."
        ],
        "checkpoints": [
            {
                "q": "Which isotope is universally used in medicine for the diagnosis and treatment of goitre (thyroid disorders)?",
                "options": [
                    "Cobalt-60",
                    "Iodine-131",
                    "Uranium-235",
                    "Carbon-14"
                ],
                "correct": 1,
                "explanation": "Because the human thyroid gland selectively concentrates iodine, Iodine-131 (¹³¹I) is used in endocrinology for thyroid scanning and targeted therapy of goitre and thyroid carcinoma."
            },
            {
                "q": "What is the primary peaceful societal application of the isotope Uranium-235 (²³⁵U)?",
                "options": [
                    "Treating cataracts in eye surgery",
                    "Fuel in nuclear reactors for commercial electric power generation",
                    "Carbon dating ancient mummies",
                    "Water purification in municipal reservoirs"
                ],
                "correct": 1,
                "explanation": "Uranium-235 undergoes controlled nuclear fission inside nuclear reactors, producing immense thermal energy used to drive steam turbines for electrical power generation."
            }
        ]
    },

    # SLIDE 14
    {
        "id": 14,
        "title": "Isobars: Different Elements with Identical Mass Numbers",
        "subtitle": "Same Nucleon Total, Different Nuclear Charges: ⁴⁰Ar vs ⁴⁰Ca and ¹⁴C vs ¹⁴N",
        "narration": "While isotopes are atoms of the SAME element with different mass numbers, isobars are atoms of DIFFERENT chemical elements that have the same mass number! They have different numbers of protons and different electronic configurations, which means their chemical properties are completely different.",
        "points": [
            "<strong>Definition of Isobars:</strong> Atoms of different chemical elements that have different atomic numbers ($Z$) but possess the same mass number ($A$).<br>$$\\text{Isobars have: } Z_1 \\neq Z_2 \\quad \\text{and} \\quad A_1 = A_2$$",
            "<strong>The Classic Argon-Calcium Isobaric Pair:</strong><br>• <strong>Argon (${}_{18}^{40}\\text{Ar}$):</strong> $Z = 18$ (18 protons, 18 electrons, 22 neutrons). It is an unreactive, inert monoatomic noble gas.<br>• <strong>Calcium (${}_{20}^{40}\\text{Ca}$):</strong> $Z = 20$ (20 protons, 20 electrons, 20 neutrons). It is a highly reactive, divalent alkaline earth metal.",
            "<strong>The Carbon-Nitrogen Isobaric Pair:</strong><br>• Carbon-14 (${}_6^{14}\\text{C}$): $6$ protons, $8$ neutrons ($A=14$).<br>• Nitrogen-14 (${}_7^{14}\\text{N}$): $7$ protons, $7$ neutrons ($A=14$).",
            "<strong>Diagnostic Comparison (Isotopes vs Isobars):</strong><br>• <em>Isotopes:</em> Same $Z$, different $A$, same element, identical chemical properties.<br>• <em>Isobars:</em> Different $Z$, same $A$, completely different elements, completely different chemical properties!"
        ],
        "checkpoints": [
            {
                "q": "Why do the isobars Argon-40 (⁴⁰₁₈Ar) and Calcium-40 (⁴⁰₂₀Ca) exhibit radically different chemical behaviors despite having the exact same mass number of 40?",
                "options": [
                    "They have different atomic numbers, different proton counts, and completely different valence electron configurations",
                    "Calcium contains no protons",
                    "Argon has a higher mass than calcium",
                    "They have the same number of neutrons"
                ],
                "correct": 0,
                "explanation": "Argon has Z=18 (config 2,8,8 - noble gas) while Calcium has Z=20 (config 2,8,8,2 - reactive metal). Chemical properties depend on valence electrons, not mass numbers."
            },
            {
                "q": "Which of the following pairs represents isobars?",
                "options": [
                    "¹²₆C and ¹⁴₆C",
                    "⁴⁰₁₈Ar and ⁴⁰₂₀Ca",
                    "³⁵₁₇Cl and ³⁷₁₇Cl",
                    "¹₁H and ²₁H"
                ],
                "correct": 1,
                "explanation": "⁴⁰₁₈Ar and ⁴⁰₂₀Ca have different atomic numbers (18 vs 20) but identical mass numbers (A = 40), which makes them isobars."
            }
        ]
    },

    # SLIDE 15
    {
        "id": 15,
        "title": "Indian Scientific Pioneer: Dr. Homi J. Bhabha & Peaceful Atomic Energy (C-5.2)",
        "subtitle": "Father of the Indian Nuclear Programme & The 3-Stage Thorium Fuel Vision",
        "narration": "India's journey in modern atomic science was forged by the visionary theoretical physicist Dr. Homi Jehangir Bhabha (1909–1966). Recognized globally for Bhabha Scattering in quantum electrodynamics, Dr. Bhabha passionately advocated for atomic energy as a peaceful engine to lift millions of citizens out of poverty through self-reliant clean electricity.",
        "points": [
            "<strong>Architect of Indian Science:</strong> In 1945, Dr. Homi Bhabha established the Tata Institute of Fundamental Research (TIFR) in Mumbai, followed by the Atomic Energy Establishment Trombay (AEET, renamed Bhabha Atomic Research Centre - BARC in his honour in 1967).",
            "<strong>Global Theoretical Physics Contributions:</strong> Formulated the relativistic quantum mechanics of electron-positron scattering, known worldwide as <em>Bhabha Scattering</em>, and co-discovered cosmic ray shower cascades with Walter Heitler.",
            "<strong>The Visionary 3-Stage Nuclear Programme:</strong> Recognizing that India possessed limited domestic uranium reserves but the world's largest deposits of <strong>Thorium-232</strong> in monazite sands along the Kerala coast, Bhabha formulated India's unique 3-stage nuclear strategy:<br>• <em>Stage 1:</em> Pressurised Heavy Water Reactors (PHWRs) using natural Uranium to produce Plutonium-239.<br>• <em>Stage 2:</em> Fast Breeder Reactors (FBRs) using Plutonium to breed more fuel and convert Thorium into Uranium-233.<br>• <em>Stage 3:</em> Advanced Thermal Thorium Reactors using abundant Thorium-233 to generate centuries of clean, carbon-free energy.",
            "<strong>C-5.2 Peaceful Development:</strong> BARC pioneered indigenous radioisotope production for cancer treatment (Bhabhatron radiotherapy unit) and agricultural crop mutation breeding (producing high-yield groundnut, pulse, and mustard varieties)."
        ],
        "checkpoints": [
            {
                "q": "Why did Dr. Homi J. Bhabha design a unique 3-stage nuclear power programme specifically tailored for India?",
                "options": [
                    "India had zero access to water for cooling reactors",
                    "India possessed limited natural uranium but world-leading reserves of Thorium-232 in coastal monazite sands",
                    "To build nuclear weapons for export",
                    "To replace all solar power in India"
                ],
                "correct": 1,
                "explanation": "Dr. Bhabha strategically designed India's 3-stage programme to transition from scarce natural Uranium to India's vast domestic Thorium-232 reserves, ensuring centuries of long-term energy independence."
            },
            {
                "q": "What peaceful medical technology was developed by BARC to treat cancer patients in developing nations?",
                "options": [
                    "The Bhabhatron teletherapy Cobalt-60 unit",
                    "The Paperfuge",
                    "Oral Rehydration Solution",
                    "The artificial lung machine"
                ],
                "correct": 0,
                "explanation": "BARC engineered the 'Bhabhatron', an indigenous, highly affordable Cobalt-60 teletherapy machine designed to deliver precision cancer radiotherapy in India and developing countries."
            }
        ]
    },

    # SLIDE 16
    {
        "id": 16,
        "title": "Open Scientific Inquiry: Can We Ever Completely Understand the Atom? (C-7.2)",
        "subtitle": "Heisenberg Uncertainty, Quantum Probability Clouds, Quarks & The Nature of Reality",
        "narration": "Can we ever obtain a complete, perfect mechanical snapshot of an atom? In the 1920s, Werner Heisenberg and Erwin Schrödinger proved that the neat planetary tracks of Bohr's model were an oversimplification. At the subatomic scale, quantum mechanics dictates that electrons are not solid billiard balls orbiting like planets, but probabilistic wave packets governed by fundamental uncertainty!",
        "points": [
            "<strong>The Heisenberg Uncertainty Principle (1927):</strong> It is fundamentally impossible to simultaneously measure both the exact position ($x$) and the exact momentum ($p$) of an electron with arbitrary precision:<br>$$\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi}$$<br>The more precisely you pin down an electron's position, the less you know about its velocity!",
            "<strong>From Fixed Orbits to Orbital Electron Clouds:</strong> Modern quantum chemistry replaces fixed 2D planetary tracks with 3D <em>orbitals</em>—mathematical wavefunctions where there is a $90\\%$ probability of finding an electron around the nucleus.",
            "<strong>Inside the Nucleon: The Quark Frontier:</strong> In the 1960s, Murray Gell-Mann showed that protons and neutrons are NOT fundamental particles! Each is composed of three elementary particles called <strong>quarks</strong> held together by gluons (the strong force):<br>• Proton ($p^+$) = $2\\text{ Up Quarks } (+2/3) + 1\\text{ Down Quark } (-1/3) = +1\\text{ charge}$<br>• Neutron ($n^0$) = $1\\text{ Up Quark } (+2/3) + 2\\text{ Down Quarks } (-1/3) = 0\\text{ charge}$",
            "<strong>C-7.2 Philosophical Frontier:</strong> As quantum field theory reveals, vacuum space inside an atom is not empty—it roils with virtual particle-antiparticle pairs constantly popping in and out of existence! The deeper science probes, the more mysterious and interconnected reality becomes."
        ],
        "checkpoints": [
            {
                "q": "According to the Heisenberg Uncertainty Principle, why can we never draw exact circular planetary tracks for electrons inside an atom?",
                "options": [
                    "Electrons move too slowly to be tracked",
                    "It is fundamentally impossible to simultaneously know both the exact position and momentum of an electron",
                    "The nucleus repels all measuring instruments",
                    "Electrons turn into photons when observed"
                ],
                "correct": 1,
                "explanation": "Heisenberg's principle (Δx · Δp ≥ h/4π) establishes a fundamental quantum limit: pinning down an electron's exact position makes its velocity uncertain, precluding fixed planetary orbits."
            },
            {
                "q": "What subatomic components constitute a proton inside the atomic nucleus?",
                "options": [
                    "Two Up quarks (+2/3 each) and one Down quark (-1/3)",
                    "Three electrons",
                    "Two Down quarks and one Up quark",
                    "Four photons and two neutrons"
                ],
                "correct": 0,
                "explanation": "A proton is composed of two Up quarks (charge +2/3 each) and one Down quark (charge -1/3), yielding a net charge of +2/3 + 2/3 - 1/3 = +1."
            }
        ]
    },

    # SLIDE 17 - QUIZ 1
    {
        "id": 17,
        "title": "Dedicated Quiz Challenge 1: Subatomic Particles & Historical Atomic Models",
        "subtitle": "Mastery Assessment: Thomson, Goldstein, Chadwick, Rutherford & Bohr (C-1.1, C-5.1)",
        "narration": "Welcome to Quiz Challenge 1! Test your foundational knowledge of the three subatomic particles, the watermelon model, Rutherford's alpha scattering experiment, and Bohr's quantized orbits. Answer all 10 questions and use 'View Solution' for detailed step-by-step reasoning.",
        "questions": [
            {
                "q": "Which scientist discovered the neutron by bombarding thin beryllium foil with alpha particles in 1932?",
                "options": ["J.J. Thomson", "Ernest Rutherford", "James Chadwick", "Niels Bohr"],
                "correct": 2,
                "solution": "James Chadwick discovered the neutron in 1932 by bombarding beryllium with alpha particles, observing penetrating neutral radiation composed of particles with mass nearly equal to a proton."
            },
            {
                "q": "What major observation from Rutherford's gold foil experiment proved that the positive charge and mass of an atom are concentrated in a tiny fraction of the total atomic volume?",
                "options": [
                    "Most alpha particles passed straight through without deflection",
                    "Approximately 1 in 12,000 alpha particles rebounded backwards at angles greater than 90°",
                    "All alpha particles were absorbed by the gold atoms",
                    "The gold foil melted into liquid gold"
                ],
                "correct": 1,
                "solution": "Only a concentrated, extremely dense positive mass (the nucleus) could exert the immense electrostatic repulsion required to bounce a fast-moving, heavy alpha particle backwards (180°)."
            },
            {
                "q": "What is the relative mass and charge of an electron compared to a proton?",
                "options": [
                    "Mass ~ 1/1840 u, Charge -1",
                    "Mass ~ 1 u, Charge +1",
                    "Mass ~ 1 u, Charge 0",
                    "Mass ~ 1840 u, Charge -1"
                ],
                "correct": 0,
                "solution": "An electron has relative mass approximately 1/1840th of a proton (negligible in mass calculations) and carries a single unit negative charge (-1)."
            },
            {
                "q": "What was the critical flaw in Rutherford's planetary model under classical Maxwellian physics?",
                "options": [
                    "It could not explain why gold is yellow",
                    "Accelerating revolving electrons should continuously radiate energy and spiral into the nucleus in ~10⁻⁸ seconds",
                    "It predicted that the nucleus is negative",
                    "It required neutrons to have positive charge"
                ],
                "correct": 1,
                "solution": "According to classical electrodynamics, any accelerating charged particle radiates electromagnetic energy. An electron orbiting in a circle is continuously accelerating and would spiral into the nucleus within 10⁻⁸ s."
            },
            {
                "q": "In Niels Bohr's atomic model, what is the name and principal quantum number of the innermost electron shell?",
                "options": ["L-shell, n = 2", "K-shell, n = 1", "M-shell, n = 3", "N-shell, n = 4"],
                "correct": 1,
                "solution": "The innermost discrete shell closest to the nucleus is the K-shell, designated by principal quantum number n = 1."
            },
            {
                "q": "What did E. Goldstein discover in 1886 using a perforated cathode in a gas discharge tube?",
                "options": [
                    "Cathode rays consisting of electrons",
                    "Canal rays (anode rays) consisting of positively charged ions/protons",
                    "X-rays",
                    "Cosmic radiation"
                ],
                "correct": 1,
                "solution": "E. Goldstein used a perforated cathode to discover luminous rays traveling in the opposite direction from cathode rays, which he named 'canal rays' (positively charged protons)."
            },
            {
                "q": "Why do electrons in Bohr's discrete orbits NOT radiate energy and fall into the nucleus?",
                "options": [
                    "Gravity repels the electrons",
                    "Bohr postulated that stationary orbits are non-radiating states where energy remains conserved",
                    "The nucleus has zero charge",
                    "Electrons freeze at room temperature"
                ],
                "correct": 1,
                "solution": "Bohr's fundamental quantum postulate states that discrete stationary orbits are non-radiating; an electron only gains or loses energy when transitioning between levels."
            },
            {
                "q": "Which atomic model was compared to a Christmas pudding or a watermelon?",
                "options": ["Rutherford's Model", "Bohr's Model", "Thomson's Model", "Dalton's Model"],
                "correct": 2,
                "solution": "J.J. Thomson (1904) proposed the Plum Pudding (or Watermelon) model, with negative electrons embedded in a positive sphere like raisins in a pudding."
            },
            {
                "q": "How does the radius of an atomic nucleus compare to the overall radius of the atom?",
                "options": [
                    "Nuclear radius is about 100,000 times smaller (10⁻¹⁵ m vs 10⁻¹⁰ m)",
                    "Nuclear radius is 10 times larger",
                    "They are exactly identical",
                    "Nuclear radius is 1 millimeter"
                ],
                "correct": 0,
                "solution": "The radius of the nucleus is ~10⁻¹⁵ m, while the radius of the atom is ~10⁻¹⁰ m—a ratio of 1 to 100,000 (comparable to a marble in the center of a football stadium)."
            },
            {
                "q": "Which ancient philosopher first proposed that matter is composed of ultimate indivisible particles called Parmanu?",
                "options": ["Aristotle", "Democritus", "Acharya Kanad", "John Dalton"],
                "correct": 2,
                "solution": "Around 600 BCE, Indian sage Acharya Kanad founded the Vaisheshika philosophy and formulated the theory of 'Parmanu' as the indestructible, indivisible limit of matter."
            }
        ]
    },

    # SLIDE 18 - QUIZ 2
    {
        "id": 18,
        "title": "Dedicated Quiz Challenge 2: Bohr-Bury Rules, Configurations & Valency",
        "subtitle": "Mastery Assessment: 2n² Law, Octet Rule, First 18 Elements & Valency Calculations",
        "narration": "Welcome to Quiz Challenge 2! Test your ability to distribute electrons using the 2n² rule and determine valence electrons and combining capacity (valency) for elements from Hydrogen to Argon.",
        "questions": [
            {
                "q": "According to the 2n² formula, what is the maximum number of electrons that the N-shell (n = 4) can accommodate?",
                "options": ["18 electrons", "32 electrons", "8 electrons", "50 electrons"],
                "correct": 1,
                "solution": "For the N-shell (n = 4), Maximum capacity = 2n² = 2 × (4)² = 2 × 16 = 32 electrons."
            },
            {
                "q": "What is the valency of Magnesium (Atomic number Z = 12)?",
                "options": ["1", "2", "6", "0"],
                "correct": 1,
                "solution": "Magnesium has Z=12 and electronic configuration (2, 8, 2). It has 2 valence electrons in its outermost shell, which it readily loses to form Mg²⁺, giving it a valency of 2."
            },
            {
                "q": "What is the electronic configuration of a chlorine atom (Atomic number Z = 17)?",
                "options": ["2, 8, 7", "2, 7, 8", "2, 8, 18", "7, 8, 2"],
                "correct": 0,
                "solution": "Chlorine (Z=17) fills K-shell with 2, L-shell with 8, and the remaining 7 electrons enter the M-shell: configuration (2, 8, 7)."
            },
            {
                "q": "Why is the valency of nitrogen (Atomic number Z = 7, configuration 2, 5) equal to 3 rather than 5?",
                "options": [
                    "Nitrogen loses all 5 electrons during bonding",
                    "It is energetically more favorable to gain or share 3 electrons to attain an octet (8 - 5 = 3)",
                    "Nitrogen has 3 protons in its nucleus",
                    "Nitrogen forms only triple bonds with metals"
                ],
                "correct": 1,
                "solution": "For non-metals with 5, 6, or 7 valence electrons, valency = 8 - (valence electrons). For nitrogen: Valency = 8 - 5 = 3."
            },
            {
                "q": "Which of the following elements has a valency of zero?",
                "options": ["Helium (Z = 2)", "Neon (Z = 10)", "Argon (Z = 18)", "All of the above"],
                "correct": 3,
                "solution": "Helium (complete duplet), Neon (complete octet), and Argon (complete octet) all have completely filled valence shells, so none of them gain, lose, or share electrons; their valency is 0."
            },
            {
                "q": "What is the maximum number of electrons permitted in the outermost shell of ANY atom, according to Bohr-Bury Rule 2?",
                "options": ["2 electrons", "8 electrons", "18 electrons", "32 electrons"],
                "correct": 1,
                "solution": "Rule 2 states that the outermost valence shell of an atom can never accommodate more than 8 electrons, regardless of its theoretical 2n² capacity."
            },
            {
                "q": "An element X has electronic configuration (2, 8, 4). What is the identity and valency of element X?",
                "options": [
                    "Carbon, Valency 4",
                    "Silicon, Valency 4",
                    "Aluminium, Valency 3",
                    "Sulfur, Valency 2"
                ],
                "correct": 1,
                "solution": "Total electrons = 2 + 8 + 4 = 14, which corresponds to Silicon (Si, Z=14). With 4 valence electrons, its combining capacity (valency) is 4."
            },
            {
                "q": "What is the valency of Aluminium (Atomic number Z = 13)?",
                "options": ["1", "2", "3", "5"],
                "correct": 2,
                "solution": "Aluminium (Z=13) has configuration (2, 8, 3). It loses its 3 outermost valence electrons to form Al³⁺, giving a valency of 3."
            },
            {
                "q": "How many electrons are in the outermost M-shell of a sulfur atom (Z = 16)?",
                "options": ["2", "4", "6", "8"],
                "correct": 2,
                "solution": "Sulfur has Z=16 and electronic configuration (2, 8, 6). The outermost M-shell contains 6 valence electrons."
            },
            {
                "q": "Which element in the first 18 elements has the same number of valence electrons as sodium (Z = 11)?",
                "options": ["Lithium (Z = 3)", "Potassium (Z = 19)", "Hydrogen (Z = 1)", "Both Lithium and Hydrogen"],
                "correct": 3,
                "solution": "Hydrogen (1), Lithium (2, 1), and Sodium (2, 8, 1) all belong to Group 1 and possess exactly 1 valence electron."
            }
        ]
    },

    # SLIDE 19 - QUIZ 3
    {
        "id": 19,
        "title": "Dedicated Quiz Challenge 3: Atomic Numbers, Mass Numbers & Isotopes",
        "subtitle": "Mastery Assessment: p⁺, e⁻, n⁰ Calculations, IUPAC Notations & Fractional Masses",
        "narration": "Welcome to Quiz Challenge 3! Master the calculations connecting atomic numbers, mass numbers, subatomic particle counts, and fractional average atomic masses from isotopic abundances.",
        "questions": [
            {
                "q": "An atom has 8 protons, 8 electrons, and 9 neutrons. What is its atomic number (Z) and mass number (A)?",
                "options": [
                    "Z = 8, A = 16",
                    "Z = 8, A = 17",
                    "Z = 9, A = 17",
                    "Z = 17, A = 8"
                ],
                "correct": 1,
                "solution": "Atomic number Z = number of protons = 8. Mass number A = protons + neutrons = 8 + 9 = 17 (this is Oxygen-17, ¹⁷₈O)."
            },
            {
                "q": "Naturally occurring Boron consists of two isotopes: ¹⁰B (mass 10 u, 20% abundance) and ¹¹B (mass 11 u, 80% abundance). What is the average atomic mass of Boron?",
                "options": ["10.2 u", "10.5 u", "10.8 u", "11.2 u"],
                "correct": 2,
                "solution": "Average mass = (10 × 20/100) + (11 × 80/100) = 2.0 + 8.8 = 10.8 u."
            },
            {
                "q": "The isotope Deuterium (²₁H) is widely used in nuclear technology. How many neutrons does it have?",
                "options": ["0 neutrons", "1 neutron", "2 neutrons", "3 neutrons"],
                "correct": 1,
                "solution": "Deuterium has mass number A = 2 and atomic number Z = 1. Number of neutrons N = A - Z = 2 - 1 = 1 neutron."
            },
            {
                "q": "How many protons and neutrons are present in the nucleus of Carbon-14 (¹⁴₆C)?",
                "options": [
                    "6 protons and 8 neutrons",
                    "8 protons and 6 neutrons",
                    "6 protons and 6 neutrons",
                    "14 protons and 0 neutrons"
                ],
                "correct": 0,
                "solution": "Atomic number Z = 6 protons. Neutrons = A - Z = 14 - 6 = 8 neutrons."
            },
            {
                "q": "What is the 3:1 natural abundance ratio of Chlorine-35 to Chlorine-37 that gives chlorine its fractional average mass of 35.5 u?",
                "options": [
                    "50% Chlorine-35 and 50% Chlorine-37",
                    "75% Chlorine-35 and 25% Chlorine-37",
                    "25% Chlorine-35 and 75% Chlorine-37",
                    "90% Chlorine-35 and 10% Chlorine-37"
                ],
                "correct": 1,
                "solution": "Chlorine-35 comprises ~75% and Chlorine-37 comprises ~25% of natural chlorine: Average mass = (35 × 0.75) + (37 × 0.25) = 26.25 + 9.25 = 35.5 u."
            },
            {
                "q": "In the standard notation ²³₁₁Na, what does the superscript 23 represent?",
                "options": [
                    "The atomic number (Z)",
                    "The number of electrons",
                    "The mass number (A = protons + neutrons)",
                    "The valency of sodium"
                ],
                "correct": 2,
                "solution": "In standard IUPAC notation ᴬ_Z X, the superscript A represents the mass number (total number of nucleons: 11 protons + 12 neutrons = 23)."
            },
            {
                "q": "Why do isotopes of an element have virtually identical chemical properties?",
                "options": [
                    "They have the exact same number of neutrons",
                    "They have the same atomic number and identical valence electron configuration",
                    "They have identical physical densities",
                    "They have the same nuclear half-life"
                ],
                "correct": 1,
                "solution": "Chemical reactions involve valence electrons; because isotopes have identical electron configurations, their chemical reactivity is identical."
            },
            {
                "q": "How many neutrons are present in the nucleus of Potassium-39 (³⁹₁₉K)?",
                "options": ["19", "20", "39", "58"],
                "correct": 1,
                "solution": "Neutrons = Mass Number (A) - Atomic Number (Z) = 39 - 19 = 20 neutrons."
            },
            {
                "q": "What definition of the unified atomic mass unit (u) was established by IUPAC in 1961?",
                "options": [
                    "The mass of one hydrogen atom",
                    "Exactly 1/12th the mass of one neutral Carbon-12 atom at rest",
                    "The mass of one electron",
                    "The mass of one oxygen-16 atom"
                ],
                "correct": 1,
                "solution": "By international IUPAC agreement, 1 unified atomic mass unit (1 u) is defined as exactly 1/12th the rest mass of an unbound neutral Carbon-12 (¹²C) atom (approx. 1.6605 × 10⁻²⁷ kg)."
            },
            {
                "q": "Which subatomic particle defines the fundamental chemical identity of an element?",
                "options": ["Neutron", "Proton (Atomic Number Z)", "Electron", "Positron"],
                "correct": 1,
                "solution": "The number of protons (atomic number Z) is the unique invariant identifying an element. Changing proton count changes the element itself."
            }
        ]
    },

    # SLIDE 20 - QUIZ 4
    {
        "id": 20,
        "title": "Dedicated Quiz Challenge 4: Isobars, Nuclear Science & Indian Pioneers",
        "subtitle": "Mastery Assessment: Isobars, Bhabha's Thorium Vision, Radioisotopes & Quantum Clouds (C-5.2, C-5.3, C-6.1, C-7.2)",
        "narration": "Welcome to the final Mastery Quiz Challenge! Synthesize your deep understanding across isobars, medical radioisotopes, Dr. Homi Bhabha's 3-stage nuclear programme, and quantum orbital clouds.",
        "questions": [
            {
                "q": "Which of the following pairs are isobars?",
                "options": [
                    "⁴⁰₁₈Ar and ⁴⁰₂₀Ca",
                    "¹²₆C and ¹⁴₆C",
                    "³⁵₁₇Cl and ³⁷₁₇Cl",
                    "¹₆O and ¹⁸₆O"
                ],
                "correct": 0,
                "solution": "Isobars have different atomic numbers but the same mass number: ⁴⁰₁₈Ar and ⁴⁰₂₀Ca both have mass number A = 40 with different atomic numbers (18 vs 20)."
            },
            {
                "q": "Which radioactive isotope is utilized in medicine for gamma-ray teletherapy to destroy cancer tumors?",
                "options": ["Uranium-235", "Cobalt-60", "Carbon-14", "Sodium-23"],
                "correct": 1,
                "solution": "Cobalt-60 (⁶⁰Co) decays by emitting high-energy gamma rays (1.17 MeV and 1.33 MeV) used in radiotherapy to destroy malignant tumor cells."
            },
            {
                "q": "Why did Dr. Homi J. Bhabha formulate India's unique 3-stage nuclear energy programme to utilize Thorium-232?",
                "options": [
                    "Thorium can be enriched in ordinary kitchen stoves",
                    "India holds approximately 25% of the world's Thorium reserves in monazite sands, ensuring energy sovereignty",
                    "Thorium has zero protons in its nucleus",
                    "Thorium does not require nuclear reactors"
                ],
                "correct": 1,
                "solution": "India has vast coastal monazite deposits of Thorium-232 but modest Uranium reserves; Bhabha's 3-stage strategy breeds fissile U-233 from Thorium for sustainable long-term power."
            },
            {
                "q": "What is the half-life of Carbon-14 used in archaeological radiocarbon dating?",
                "options": ["24 hours", "30 days", "5,730 years", "1 million years"],
                "correct": 2,
                "solution": "Carbon-14 has a half-life of approximately 5,730 years, making it ideal for dating biological artifacts up to ~50,000 years old."
            },
            {
                "q": "Which subatomic quarks compose a neutron?",
                "options": [
                    "Two Up quarks and one Down quark",
                    "One Up quark (+2/3) and two Down quarks (-1/3 each)",
                    "Three Up quarks",
                    "Three electrons"
                ],
                "correct": 1,
                "solution": "A neutron consists of one Up quark (+2/3) and two Down quarks (-1/3 each): Net charge = +2/3 - 1/3 - 1/3 = 0."
            },
            {
                "q": "What does the Heisenberg Uncertainty Principle (Δx · Δp ≥ h/4π) imply about the structure of an atom?",
                "options": [
                    "Electrons do not exist",
                    "We cannot simultaneously determine the exact position and velocity of an electron, so fixed circular planetary orbits are physically impossible",
                    "Protons move faster than the speed of light",
                    "Neutrons orbit the electrons"
                ],
                "correct": 1,
                "solution": "Heisenberg showed that electrons cannot be pictured as tiny marbles following definite orbits; instead, they exist in 3D probabilistic cloud regions called orbitals."
            },
            {
                "q": "Which Indian research institution was founded by Dr. Homi J. Bhabha in 1945 to advance fundamental physics research in India?",
                "options": [
                    "Tata Institute of Fundamental Research (TIFR)",
                    "Indian Space Research Organisation (ISRO)",
                    "National Chemical Laboratory",
                    "All India Institute of Medical Sciences"
                ],
                "correct": 0,
                "solution": "Dr. Homi J. Bhabha established the Tata Institute of Fundamental Research (TIFR) in Mumbai in 1945 with the support of J.R.D. Tata."
            },
            {
                "q": "What is the difference between isotopes and isobars in terms of chemical properties?",
                "options": [
                    "Isotopes have identical chemical properties; isobars have completely different chemical properties",
                    "Isotopes have different chemical properties; isobars have identical chemical properties",
                    "Both isotopes and isobars have identical chemical properties",
                    "Neither isotopes nor isobars can participate in chemical reactions"
                ],
                "correct": 0,
                "solution": "Chemical reactivity depends on valence electrons and atomic number: isotopes share the same atomic number and have identical chemistry; isobars have different atomic numbers and differ chemically."
            },
            {
                "q": "Which radioactive tracer isotope is injected into the bloodstream to detect circulatory thrombosis and vascular blood clots?",
                "options": ["Sodium-24 (²⁴Na)", "Cobalt-60", "Uranium-238", "Argon-40"],
                "correct": 0,
                "solution": "Sodium-24 (²⁴Na), with a half-life of 15 hours, is administered as a radioactive sodium chloride tracer to monitor arterial blood flow and locate circulatory obstructions."
            },
            {
                "q": "In the modern quantum mechanical model of the atom, what is an 'orbital'?",
                "options": [
                    "A rigid wire on which electrons slide",
                    "A three-dimensional mathematical region in space around the nucleus where the probability of finding an electron is high (~90%)",
                    "The hollow center inside a proton",
                    "A track carved by alpha particles"
                ],
                "correct": 1,
                "solution": "An orbital is a quantum mechanical probability density cloud representing the 3D volume around the nucleus where there is a high statistical likelihood (~90%) of finding an electron."
            }
        ]
    }
]


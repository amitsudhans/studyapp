"""
Comprehensive dataset for NCERT Class 10 Science Chapter 11: Electricity.
Contains 18 content slides covering all lines, figures, activities, tables, and exercises + 4 dedicated quiz challenge slides (40 questions).
"""

CONTENT_SLIDES = [
    {
        "id": 1,
        "title": "Electric Current & Circuit Fundamentals",
        "subtitle": "Chapter 11 • Pages 171–172",
        "tag": "Section 11.1 Current & Circuit",
        "quote": "Electric current is the controllable lifeblood of modern society—a steady rate of charge flow through a continuous closed conducting loop.",
        "lead": "Just as flowing water constitutes a water current in a river, electric charges flowing through a metallic conductor constitute an electric current.",
        "narration": "Welcome to Chapter 11: Electricity! Just as flowing water constitutes a water current in rivers, electric charge flowing through a metallic wire constitutes an electric current. An electric circuit is a continuous and closed path of an electric current. If the circuit is broken anywhere, such as when a switch is opened, the current stops flowing and the bulb cannot glow.",
        "theory_blocks": [
            {
                "title": "Water Analogy & Continuous Circuit Path",
                "content": "<p class='mb-2 text-slate-300'>Electricity is a controllable and convenient form of energy used in homes, schools, hospitals, and industries.</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Flow of Charge:</strong> Just as water flows in rivers to form water currents, electric charges (free electrons in metals) flow through conductors to constitute an <strong>electric current</strong>.</li><li><strong>Electric Circuit:</strong> A <strong>continuous and closed path</strong> of an electric current. If the circuit is broken anywhere (or the switch is turned off), the current stops flowing immediately.</li><li><strong>Role of a Switch:</strong> A switch makes a conducting link between the power source (cell or battery) and the load (such as a torch bulb).</li></ul>"
            },
            {
                "title": "Rate of Flow of Charge & Flow Directions",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Quantitative Definition:</strong> Electric current ($I$) is defined as the amount of net electric charge ($Q$) flowing across any cross-section of a conductor per unit time ($t$):<br><span class='text-amber-400 font-mono font-bold text-xs sm:text-sm'>$$I = \\frac{Q}{t}$$</span></li><li><strong>Charge Carriers:</strong> In metallic conductors, negatively charged <strong>electrons</strong> constitute the moving charges.</li><li><strong>Conventional Direction:</strong> Electricity was discovered before electrons were known. Historically, current was considered the flow of positive charges. Conventionally, current direction is taken as <strong>opposite to the direction of electron flow</strong> (from positive terminal to negative terminal outside the cell).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the defining condition for an electric circuit to allow continuous current flow?",
                "options": [
                    "It must be an open loop with a single terminal connected",
                    "It must be a continuous and closed conducting path",
                    "It must operate only inside a vacuum chamber",
                    "It must possess zero electrical resistance"
                ],
                "ans": 1,
                "solution": "An electric circuit is defined as a continuous and closed path of an electric current. If broken anywhere, current immediately ceases to flow (NCERT Page 171)."
            },
            {
                "q": "Conventionally, what is taken as the direction of electric current in a metallic circuit?",
                "options": [
                    "In the same direction as the flow of negative electrons",
                    "From the negative terminal to the positive terminal of the cell",
                    "Opposite to the direction of electron flow (from positive to negative terminal)",
                    "Randomly fluctuating in both directions at all times"
                ],
                "ans": 2,
                "solution": "Conventionally, in an electric circuit the direction of electric current is taken as opposite to the direction of the flow of electrons, flowing from positive to negative terminal through the external circuit (NCERT Page 171)."
            }
        ]
    },
    {
        "id": 2,
        "title": "SI Units of Charge, Current & Ammeter Measurement",
        "subtitle": "Chapter 11 • Page 172",
        "tag": "Section 11.1 Units & Ammeter",
        "quote": "One ampere is the flow of one coulomb of charge per second—representing nearly six quintillion electrons drifting in unison.",
        "lead": "Electric charge is measured in coulombs, while current is quantified in amperes using a low-resistance ammeter always wired in series.",
        "narration": "Let us examine the units. The SI unit of electric charge is the coulomb, denoted by C. One electron carries a charge of 1.6 times 10 to the minus 19 coulombs, so one coulomb contains nearly 6 times 10 to the 18 electrons. Current is measured in amperes, where one ampere equals one coulomb per second. We measure current using an ammeter connected in series with the component.",
        "theory_blocks": [
            {
                "title": "The Coulomb & Electron Number Derivation",
                "content": "<p class='mb-2 text-slate-300'>The SI unit of electric charge is the <strong>coulomb (C)</strong>.</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Each electron carries an elementary negative charge of magnitude $e = 1.6 \\times 10^{-19}\\text{ C}$.</li><li><strong>Number of electrons ($n$) in $1\\text{ C}$ of charge:</strong><br><span class='text-cyan-400 font-mono font-bold text-xs sm:text-sm'>$$Q = n e \\implies n = \\frac{Q}{e} = \\frac{1\\text{ C}}{1.6 \\times 10^{-19}\\text{ C}} \\approx 6.25 \\times 10^{18} \\approx 6 \\times 10^{18}\\text{ electrons}$$</span></li><li>Thus, $1\\text{ coulomb}$ is equivalent to the collective charge carried by nearly $6 \\times 10^{18}$ electrons!</li></ul>"
            },
            {
                "title": "The Ampere & Ammeter Measurement in Series",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Ampere (A):</strong> Named in honour of French physicist André-Marie Ampère (1775–1836).<br><strong>One Ampere</strong> is constituted by the flow of one coulomb of charge per second:<br><span class='text-amber-400 font-mono font-bold text-xs sm:text-sm'>$$1\\text{ A} = 1\\text{ C} / 1\\text{ s} = 1\\text{ C}\\cdot\\text{s}^{-1}$$</span></li><li><strong>Submultiples:</strong> Milliampere ($1\\text{ mA} = 10^{-3}\\text{ A}$) and Microampere ($1\\text{ }\\mu\\text{A} = 10^{-6}\\text{ A}$).</li><li><strong>Ammeter:</strong> An instrument with very low resistance used to measure current. It is <strong>always connected in series</strong> in the circuit branch so that the entire current to be measured passes through it.</li><li><strong>Example 11.1:</strong> Current $I = 0.5\\text{ A}$ for $t = 10\\text{ min} = 600\\text{ s} \\implies Q = It = 0.5 \\times 600 = 300\\text{ C}$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "How many electrons collectively constitute a net charge of 1 coulomb?",
                "options": [
                    "6 × 10¹² electrons",
                    "6 × 10¹⁸ electrons",
                    "1.6 × 10⁻¹⁹ electrons",
                    "3 × 10⁸ electrons"
                ],
                "ans": 1,
                "solution": "Since Q = n × e, n = 1 / (1.6 × 10⁻¹⁹) ≈ 6.25 × 10¹⁸ ≈ 6 × 10¹⁸ electrons (NCERT Page 172, Intext Q3)."
            },
            {
                "q": "Why is an ammeter always connected in series in an electric circuit?",
                "options": [
                    "To increase the overall resistance of the circuit to prevent short-circuits",
                    "Because it has very low resistance and all current must flow through it to be measured",
                    "Because it has infinite resistance and prevents battery drainage",
                    "To divide the potential difference equally across the load"
                ],
                "ans": 1,
                "solution": "An ammeter has very low resistance and is connected in series so that the entire electric current flowing in the circuit passes directly through it without altering the current value (NCERT Page 172)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Electric Potential & Potential Difference",
        "subtitle": "Chapter 11 • Pages 173–174",
        "tag": "Section 11.2 Potential & Volt",
        "quote": "Electrons do not drift spontaneously; they require an electric pressure difference generated by the chemical action of a cell.",
        "lead": "Electric potential difference between two points is the work done in moving a unit positive charge from one point to the other.",
        "narration": "What causes electric charge to flow? Consider a water tube: water only flows if there is a pressure difference between the two ends. Similarly, electrons in a wire move only when there is an electric pressure difference, called potential difference, provided by a battery. Potential difference V is defined as work done W divided by charge Q. Its SI unit is the volt, and it is measured using a voltmeter connected in parallel.",
        "theory_blocks": [
            {
                "title": "The Hydraulic Analogy & Chemical Origin",
                "content": "<p class='mb-2 text-slate-300'>Charges do not flow in a copper wire on their own, just as water in a horizontal tube does not flow without a height or pressure difference.</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Electric Pressure Difference:</strong> In a circuit, electrons move only if there is a difference of electric pressure—called the <strong>potential difference</strong> ($V$)—along the conductor.</li><li><strong>Chemical Action of a Cell:</strong> Chemical reactions inside a cell create a potential difference across its terminals even when no current is drawn. Connecting the cell to a circuit releases this chemical energy to establish a steady current.</li></ul>"
            },
            {
                "title": "Mathematical Definition, The Volt & Voltmeter",
                "content": "<p class='mb-2 text-slate-300'>Electric potential difference ($V$) between two points is defined as the work done ($W$) to move a unit charge ($Q$) from one point to the other:</p><p class='text-amber-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$V = \\frac{W}{Q} \\iff W = V Q$$</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>The Volt (V):</strong> Named after Italian physicist Alessandro Volta (1745–1827).<br><strong>One Volt</strong> is the potential difference between two points when <strong>1 joule of work</strong> is done to move a charge of <strong>1 coulomb</strong> between them:<br><span class='text-cyan-400 font-mono font-bold text-xs'>$$1\\text{ V} = \\frac{1\\text{ J}}{1\\text{ C}} = 1\\text{ J}\\cdot\\text{C}^{-1}$$</span></li><li><strong>Voltmeter:</strong> An instrument with very high resistance used to measure potential difference. It is <strong>always connected in parallel</strong> across the two points under test.</li><li><strong>Example 11.2:</strong> Moving $Q = 2\\text{ C}$ across $V = 12\\text{ V} \\implies W = VQ = 12 \\times 2 = 24\\text{ J}$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is meant by saying that the potential difference between two points is 1 Volt?",
                "options": [
                    "One ampere of current flows for one hour through a conductor",
                    "One joule of work is done in moving a charge of one coulomb from one point to the other",
                    "One watt of electrical power is dissipated continuously across the points",
                    "Six quintillion electrons are stored permanently at the positive terminal"
                ],
                "ans": 1,
                "solution": "One volt is defined as the potential difference between two points when 1 joule of work is done in moving a charge of 1 coulomb from one point to the other (NCERT Page 173, Intext Q2)."
            },
            {
                "q": "How much energy is given to each coulomb of charge passing through a 6 V battery?",
                "options": [
                    "1 Joule",
                    "6 Joules",
                    "12 Joules",
                    "36 Joules"
                ],
                "ans": 1,
                "solution": "From W = V × Q, with Q = 1 C and V = 6 V, W = 6 V × 1 C = 6 Joules of energy is supplied to each coulomb of charge (NCERT Page 174, Intext Q3)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Standard Circuit Diagram Symbols",
        "subtitle": "Chapter 11 • Pages 174–175",
        "tag": "Section 11.3 Circuit Symbols",
        "quote": "Standardized graphical symbols provide a universal blueprint for analyzing and constructing electrical circuits.",
        "lead": "Table 11.1 provides the universally accepted schematic symbols for electric cells, batteries, switches, resistors, rheostats, and meters.",
        "narration": "To represent electric circuits clearly, engineers and scientists use standardized schematic symbols. An electric cell is shown with a long positive line and a shorter thick negative line. A battery is a combination of cells. Notice how plug keys are represented as open or closed, and distinguish between a fixed resistor and a variable rheostat.",
        "theory_blocks": [
            {
                "title": "Power Sources, Switches & Wire Connections",
                "content": "<p class='mb-2 text-slate-300'>Standardized schematic representations from NCERT Table 11.1:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Electric Cell:</strong> Long thin vertical line (positive terminal, $+$) paired with a shorter thick vertical line (negative terminal, $-$).</li><li><strong>Battery:</strong> A series combination of two or more cells connected alternating $+ - + -$.</li><li><strong>Plug Key / Switch (Open):</strong> Brackets $( \\quad )$ representing a disconnected gap where no current flows.</li><li><strong>Plug Key / Switch (Closed):</strong> Brackets with a center dot $(\\cdot)$ indicating a completed conducting path.</li><li><strong>Wire Joint:</strong> Perpendicular lines meeting with a prominent dot $(\\bullet)$ at the intersection.</li><li><strong>Crossing Wires without Joining:</strong> A wire looping over another with an arched bridge curve.</li></ul>"
            },
            {
                "title": "Loads, Resistors & Measuring Instruments",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Electric Bulb:</strong> A coiled loop inside a circle or an inverted curly filament symbol.</li><li><strong>Resistor ($R$):</strong> A clean zigzag pattern representing electrical resistance to current flow.</li><li><strong>Variable Resistor / Rheostat:</strong> A resistor zigzag with an inclined arrow across it or a slider tap pointing downward from above. Used to regulate current without changing voltage!</li><li><strong>Ammeter:</strong> A circle enclosing capital letter 'A' with positive ($+$) and negative ($-$) terminals. Wired in series.</li><li><strong>Voltmeter:</strong> A circle enclosing capital letter 'V' with positive ($+$) and negative ($-$) terminals. Wired in parallel.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Which component is specifically utilized in an electric circuit to regulate current without changing the source voltage?",
                "options": [
                    "A voltmeter connected in parallel",
                    "A variable resistance or rheostat",
                    "An open plug key",
                    "A copper wire crossing without joining"
                ],
                "ans": 1,
                "solution": "A variable resistance or rheostat is used to regulate the current in an electric circuit without changing the voltage of the power source (NCERT Pages 175-176)."
            },
            {
                "q": "In a schematic circuit symbol for a cell, what does the longer, thinner vertical line represent?",
                "options": [
                    "The negative terminal of the cell",
                    "The positive terminal of the cell",
                    "The internal resistance of the electrolyte",
                    "The ground earth connection"
                ],
                "ans": 1,
                "solution": "In standard circuit diagrams, the longer thin vertical line represents the positive terminal (+) while the shorter thick line represents the negative terminal (-) (NCERT Page 174, Table 11.1)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Ohm’s Law & The Linear V–I Characteristic",
        "subtitle": "Chapter 11 • Pages 175–176",
        "tag": "Section 11.4 Ohm's Law",
        "quote": "Potential difference is directly proportional to current—yielding a straight line through the origin whose slope reveals resistance.",
        "lead": "Georg Simon Ohm formulated in 1827 that at constant temperature, the current in a metallic conductor is directly proportional to the potential difference across it.",
        "narration": "In 1827, German physicist Georg Simon Ohm discovered that the potential difference across a metallic wire is directly proportional to the current flowing through it, provided its temperature remains constant. This is Ohm's Law: V equals I times R. Plotting potential difference V against current I yields a straight line passing directly through the origin. The slope of this line represents the conductor's resistance R.",
        "theory_blocks": [
            {
                "title": "Activity 11.1 & Mathematical Formulation",
                "content": "<p class='mb-2 text-slate-300'>In Activity 11.1, a nichrome wire $XY$ is connected to 1, 2, 3, and 4 cells in turn. In every trial, the ratio $V/I$ remains constant!</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Ohm's Law Statement:</strong> The potential difference, $V$, across the ends of a given metallic wire in an electric circuit is directly proportional to the current $I$ flowing through it, provided its temperature remains constant:</li></ul><p class='text-amber-400 font-mono font-bold text-xs sm:text-sm my-2'>$$V \\propto I \\implies \\frac{V}{I} = \\text{constant} = R \\implies V = I R$$</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>Resistance ($R$):</strong> The property of a conductor to oppose or resist the flow of charges through it.</li><li><strong>The Ohm ($\\Omega$):</strong> SI unit of resistance. $1\\ \\Omega = \\frac{1\\text{ V}}{1\\text{ A}}$. If $V = 1\\text{ V}$ produces $I = 1\\text{ A}$, the resistance is exactly $1\\ \\Omega$.</li></ul>"
            },
            {
                "title": "The V–I Graph & Inverse Current Relationship",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Linear V–I Graph (Fig 11.3):</strong> A plot of $V$ against $I$ for a metallic conductor is a straight line passing through the origin $(0, 0)$. The slope $\\Delta V / \\Delta I$ gives the resistance $R$.</li><li><strong>Inverse Dependence ($I = V/R$):</strong> Current is directly proportional to voltage and <strong>inversely proportional to resistance</strong>:</li></ul><p class='text-cyan-400 font-mono font-bold text-xs sm:text-sm my-2'>$$I = \\frac{V}{R}$$</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li>If resistance is doubled while voltage remains constant, the current is <strong>halved</strong>!</li><li>If resistance is halved, current <strong>doubles</strong>.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "If the potential difference across a constant resistance component decreases to half its original value, what happens to the current?",
                "options": [
                    "The current doubles",
                    "The current decreases to half of its former value",
                    "The current remains completely unchanged",
                    "The current drops immediately to zero"
                ],
                "ans": 1,
                "solution": "According to Ohm's law (I = V/R), current is directly proportional to potential difference. When V is halved with R constant, the current I also decreases to half (NCERT Page 181, Intext Q3)."
            },
            {
                "q": "What physical quantity does the slope of a straight-line V–I graph represent for a metallic conductor?",
                "options": [
                    "The total electric charge Q",
                    "The electrical resistance R of the conductor",
                    "The chemical potential energy of the battery",
                    "The drift velocity of free electrons"
                ],
                "ans": 1,
                "solution": "The ratio V/I is the slope of the V-I graph, which equals the electrical resistance R of the conductor according to Ohm's law (NCERT Page 176)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Resistance, Rheostats & Microscopic Conduction",
        "subtitle": "Chapter 11 • Pages 176–177",
        "tag": "Section 11.4 Microscopic Resistance",
        "quote": "Electrons are not entirely free; their drift is retarded by relentless collisions with the vibrating atoms of the metal lattice.",
        "lead": "Activity 11.2 demonstrates that different materials and components offer vastly different opposition to electric current.",
        "narration": "Why do different components draw different currents from the very same battery? In Activity 11.2, we replace a nichrome wire with a torch bulb and then a 10-watt bulb. The current changes drastically! Within a conductor, moving electrons collide with the vibrating atoms of the metal lattice. A material that offers low resistance is a good conductor, while insulators present enormous resistance.",
        "theory_blocks": [
            {
                "title": "Activity 11.2 & The Spectrum of Conductivity",
                "content": "<p class='mb-2 text-slate-300'>In Activity 11.2, inserting different materials into circuit gap $XY$ produces different ammeter readings:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Good Conductor:</strong> A component of a given size that offers very low resistance (e.g., silver, copper, aluminium).</li><li><strong>Resistor:</strong> A conductor that possesses an appreciable resistance designed to limit current (e.g., nichrome wire, carbon resistors).</li><li><strong>Poor Conductor:</strong> A component that offers higher resistance than ordinary metals.</li><li><strong>Insulator:</strong> A substance that offers extremely high resistance, practically blocking current flow entirely (e.g., rubber, glass, dry paper).</li></ul>"
            },
            {
                "title": "Microscopic Cause of Electrical Resistance",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Atomic Collisions:</strong> Electrons do not travel unimpeded through a metal. As they accelerate under the electric field, they repeatedly collide with positive metal ions/atoms in the lattice.</li><li>These collisions retard electron forward drift and convert kinetic energy into thermal vibrations (heat).</li><li><strong>Rheostat Operation:</strong> A rheostat contains a coil of high-resistance wire (like nichrome) and a sliding contact. Sliding the contact changes the effective length of wire in the circuit, thus smoothly varying $R$ and controlling $I$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the microscopic origin of electrical resistance inside a metallic conductor?",
                "options": [
                    "Electrons disappearing due to nuclear annihilation",
                    "Moving electrons colliding with and being retarded by the atoms of the conductor",
                    "Gravitational attraction pulling electrons toward the Earth's core",
                    "Magnetic repulsion between protons and neutrons"
                ],
                "ans": 1,
                "solution": "Electrons moving through a conductor are restrained by attraction and repeated collisions with the atoms of the lattice, retarding their motion and creating resistance (NCERT Page 177)."
            },
            {
                "q": "How does a sliding rheostat regulate the current in an electric circuit?",
                "options": [
                    "By changing the chemical potential of the battery",
                    "By altering the effective length of resistance wire included in the circuit",
                    "By ionizing the air surrounding the circuit terminals",
                    "By switching the circuit between alternating and direct current"
                ],
                "ans": 1,
                "solution": "Moving the slider of a rheostat alters the length of resistance wire connected in the circuit, changing the resistance and regulating current according to I = V/R (NCERT Pages 176-177)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Factors Determining Resistance: Length, Area & Material",
        "subtitle": "Chapter 11 • Pages 177–178",
        "tag": "Section 11.5 Factors Governing R",
        "quote": "Resistance is directly proportional to length and inversely proportional to cross-sectional area: R = ρ l / A.",
        "lead": "Activity 11.3 establishes that doubling conductor length halves current, while doubling thickness doubles current.",
        "narration": "On what factors does the resistance of a conductor depend? Activity 11.3 reveals three key factors: length, cross-sectional area, and the material. Resistance is directly proportional to length l, because electrons suffer more collisions over a longer path. It is inversely proportional to cross-sectional area A, because a thicker wire provides a wider highway for charge carriers. This gives R equals rho times l over A, where rho is the electrical resistivity.",
        "theory_blocks": [
            {
                "title": "Activity 11.3 Experimental Findings",
                "content": "<p class='mb-2 text-slate-300'>By testing different wires in circuit Fig 11.5, we observe:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Doubling Length ($l \\to 2l$):</strong> Current in the ammeter decreases to exactly <strong>one-half</strong>. Thus, resistance doubles!</li><li><strong>Thicker Wire ($A \\to 2A$):</strong> Current in the ammeter increases. A thicker wire offers <strong>lower resistance</strong>!</li><li><strong>Different Material (Copper vs Nichrome):</strong> Current changes drastically even when length and cross-section are identical!</li></ul>"
            },
            {
                "title": "The Master Equation & Electrical Resistivity (ρ)",
                "content": "<p class='mb-2 text-slate-300'>Combining experimental proportionalities:</p><p class='text-amber-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$R \\propto l \\quad \\text{and} \\quad R \\propto \\frac{1}{A} \\implies R \\propto \\frac{l}{A} \\implies R = \\rho \\frac{l}{A}$$</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Resistivity ($\\rho$, rho):</strong> A constant of proportionality called the <strong>electrical resistivity</strong> of the material.</li><li><strong>SI Unit of Resistivity:</strong> $\\rho = \\frac{R A}{l} \\implies \\frac{\\Omega \\cdot \\text{m}^2}{\\text{m}} = \\mathbf{\\Omega \\cdot \\text{m}}$ (ohm-metre).</li><li><strong>Characteristic Property:</strong> Resistivity does <strong>NOT</strong> depend on the length or shape of the wire; it depends strictly on the <strong>nature of the material</strong> and <strong>temperature</strong>!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Will electric current flow more easily through a thick wire or a thin wire of the same material and length when connected to the same source?",
                "options": [
                    "Through the thin wire, because electrons travel faster in tight spaces",
                    "Through the thick wire, because resistance is inversely proportional to cross-sectional area",
                    "Equally through both wires because length and material are identical",
                    "Through neither wire, because thickness eliminates potential difference"
                ],
                "ans": 1,
                "solution": "Current flows more easily through the thick wire. Since R ∝ 1/A, a thicker wire has larger cross-sectional area, offering lower resistance to current (NCERT Page 181, Intext Q2)."
            },
            {
                "q": "If a wire is stretched to double its original length while keeping its volume constant, how does its resistance change?",
                "options": [
                    "It doubles (2R)",
                    "It quadruples (4R)",
                    "It is halved (R/2)",
                    "It remains exactly R"
                ],
                "ans": 1,
                "solution": "When length doubles to 2l at constant volume (V = A × l), area halves to A/2. The new resistance is R' = ρ(2l)/(A/2) = 4(ρl/A) = 4R (quadrupled)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Resistivity Spectrum: Conductors, Alloys & Insulators",
        "subtitle": "Chapter 11 • Page 179",
        "tag": "Section 11.5 Table 11.2 Analysis",
        "quote": "Metals have resistivities down to 10⁻⁸ Ω·m; alloys resist oxidation at high temperatures; insulators reach 10¹⁷ Ω·m.",
        "lead": "NCERT Table 11.2 organizes substances across 25 orders of magnitude based on their electrical resistivity at 20°C.",
        "narration": "Let us examine the resistivity table. Good conductors like silver, copper, and aluminium have very low resistivities of ten to the minus eight ohm metres. Silver is the best conductor of all. Alloys like nichrome have much higher resistivities and crucially, they do not oxidise or burn easily at high temperatures. That is why heating appliances use alloy elements. Insulators like glass and rubber have massive resistivities up to ten to the seventeen ohm metres.",
        "theory_blocks": [
            {
                "title": "Conductors vs Alloys (Table 11.2)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Metals (Good Conductors):</strong> Range from $10^{-8}\\ \\Omega\\cdot\\text{m}$ to $10^{-6}\\ \\Omega\\cdot\\text{m}$.<br>• <strong>Silver:</strong> $1.60 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}$ (The best electrical conductor!).<br>• <strong>Copper:</strong> $1.62 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}$ & <strong>Aluminium:</strong> $2.63 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}$ (Widely used for power transmission lines).<br>• <strong>Tungsten:</strong> $5.20 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}$ (Used exclusively for incandescent bulb filaments; melting point $3380^\\circ\\text{C}$).</li><li><strong>Alloys:</strong> Constantan ($49 \\times 10^{-6}\\ \\Omega\\cdot\\text{m}$), Manganin ($44 \\times 10^{-6}\\ \\Omega\\cdot\\text{m}$), Nichrome ($100 \\times 10^{-6}\\ \\Omega\\cdot\\text{m}$).</li></ul>"
            },
            {
                "title": "Why Heating Appliances Use Alloys & Insulators",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Higher Resistivity:</strong> The resistivity of an alloy is generally higher than that of its constituent pure metals.</li><li><strong>Thermal Stability (No Oxidation):</strong> Alloys <strong>do not oxidise (burn) readily at high temperatures</strong>! For this reason, coils of electric irons, toasters, and heaters are made of alloys (like nichrome) rather than pure metals.</li><li><strong>Insulators:</strong> Glass ($10^{10} - 10^{14}\\ \\Omega\\cdot\\text{m}$), Hard rubber ($10^{13} - 10^{16}\\ \\Omega\\cdot\\text{m}$), Ebonite ($10^{15} - 10^{17}\\ \\Omega\\cdot\\text{m}$), Diamond ($10^{12} - 10^{13}\\ \\Omega\\cdot\\text{m}$). Both resistance and resistivity vary with temperature.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why are heating coils of electric toasters and irons made of alloys (like nichrome) rather than pure metals?",
                "options": [
                    "Alloys have lower melting points and melt easily to prevent fires",
                    "Alloys have higher resistivity and do not oxidise (burn) readily at high temperatures",
                    "Alloys have zero resistance, allowing infinite current flow",
                    "Alloys are transparent to magnetic radiation"
                ],
                "ans": 1,
                "solution": "Alloys have higher resistivity than pure metals and do not oxidise (burn) readily even at red-hot high temperatures, making them ideal for heating elements (NCERT Page 179 & 181, Intext Q4)."
            },
            {
                "q": "Based on Table 11.2, which of the following is the single best electrical conductor at 20°C?",
                "options": [
                    "Copper (1.62 × 10⁻⁸ Ω·m)",
                    "Silver (1.60 × 10⁻⁸ Ω·m)",
                    "Iron (10.0 × 10⁻⁸ Ω·m)",
                    "Mercury (94.0 × 10⁻⁸ Ω·m)"
                ],
                "ans": 1,
                "solution": "Silver has the lowest resistivity (1.60 × 10⁻⁸ Ω·m) among all listed substances, making it the best electrical conductor (NCERT Page 179, Table 11.2 & Page 181, Intext Q5b)."
            }
        ]
    },
    {
        "id": 9,
        "title": "Resistance & Resistivity Numerical Solvers",
        "subtitle": "Chapter 11 • Pages 179–181",
        "tag": "Examples 11.3 to 11.6",
        "quote": "Mastering the interplay between length, cross-section, resistivity, and voltage unlocks precision circuit engineering.",
        "lead": "Worked textbook examples demonstrate how geometric modifications and material properties dictate circuit current and resistance.",
        "narration": "Now let us master numerical problems from the textbook. In Example 11.3, an electric bulb with 1200 ohms draws only 0.18 amperes from 220 volts, whereas a 100-ohm heater coil draws 2.2 amperes. In Example 11.5, given a wire of length 1 metre, diameter 0.3 millimetres, and resistance 26 ohms, we calculate its resistivity to be 1.84 times 10 to the minus 6 ohm metres, identifying the material as manganese.",
        "theory_blocks": [
            {
                "title": "Example 11.3 & 11.4 Solutions",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Example 11.3 (Bulb vs Heater on 220 V):</strong><br>(a) Bulb filament ($R = 1200\\ \\Omega$): $I = \\frac{V}{R} = \\frac{220\\text{ V}}{1200\\ \\Omega} = 0.18\\text{ A}$.<br>(b) Heater coil ($R = 100\\ \\Omega$): $I = \\frac{V}{R} = \\frac{220\\text{ V}}{100\\ \\Omega} = 2.2\\text{ A}$.<br><em>Observation:</em> Lower resistance appliance draws over 12 times more current!</li><li><strong>Example 11.4 (Heater Voltage Increase):</strong><br>Initially: $V_1 = 60\\text{ V}, I_1 = 4\\text{ A} \\implies R = \\frac{60}{4} = 15\\ \\Omega$.<br>When voltage increases to $120\\text{ V}$: $I_2 = \\frac{120\\text{ V}}{15\\ \\Omega} = 8\\text{ A}$.</li></ul>"
            },
            {
                "title": "Example 11.5 & 11.6 Solutions",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Example 11.5 (Predicting Wire Material):</strong><br>$l = 1\\text{ m}, R = 26\\ \\Omega, d = 0.3\\text{ mm} = 3 \\times 10^{-4}\\text{ m}$.<br>$A = \\frac{\\pi d^2}{4} = \\frac{\\pi (3 \\times 10^{-4})^2}{4} = 7.068 \\times 10^{-8}\\text{ m}^2$.<br>$\\rho = \\frac{RA}{l} = \\frac{26 \\times 7.068 \\times 10^{-8}}{1} = 1.84 \\times 10^{-6}\\ \\Omega\\cdot\\text{m}$.<br><em>Conclusion:</em> Table 11.2 identifies this material as <strong>manganese</strong>!</li><li><strong>Example 11.6 (Wire Geometry Variation):</strong><br>Initial wire: $R_1 = \\rho \\frac{l}{A} = 4\\ \\Omega$.<br>New wire with length $l/2$ and area $2A$:<br>$R_2 = \\rho \\frac{l/2}{2A} = \\frac{1}{4} \\left(\\rho \\frac{l}{A}\\right) = \\frac{1}{4} R_1 = \\frac{1}{4}(4) = \\mathbf{1\\ \\Omega}$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "An electric heater draws 4 A at 60 V. What current will it draw if the potential difference is increased to 120 V?",
                "options": [
                    "2 A",
                    "4 A",
                    "8 A",
                    "16 A"
                ],
                "ans": 2,
                "solution": "Heater resistance R = V/I = 60/4 = 15 Ω. At 120 V, current is I = V/R = 120/15 = 8 A (NCERT Page 180, Example 11.4)."
            },
            {
                "q": "A wire of resistance 4 Ω is replaced by another wire of the same material having half the length (l/2) and double the area (2A). What is the new resistance?",
                "options": [
                    "1 Ω",
                    "2 Ω",
                    "8 Ω",
                    "16 Ω"
                ],
                "ans": 0,
                "solution": "R₂ = ρ(l/2)/(2A) = (1/4)(ρl/A) = R₁/4 = 4/4 = 1 Ω (NCERT Page 180, Example 11.6)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Resistors in Series: Derivation & Constant Current",
        "subtitle": "Chapter 11 • Pages 181–184",
        "tag": "Section 11.6.1 Series Combination",
        "quote": "In a series chain, identical current traverses every resistor while voltages add: Rs = R1 + R2 + R3.",
        "lead": "Activities 11.4 and 11.5 demonstrate that current is uniform throughout a series circuit, while total potential difference is the sum of individual voltage drops.",
        "narration": "Let us explore resistors in series. When resistors are connected end to end in a single line, they are in series. Activity 11.4 shows that an ammeter placed anywhere in the series circuit measures the exact same current I. Activity 11.5 shows that the total voltage V across the combination equals the sum of the individual potential differences V1 plus V2 plus V3. Applying Ohm's law, we derive that the equivalent resistance Rs equals R1 plus R2 plus R3.",
        "theory_blocks": [
            {
                "title": "Activities 11.4 & 11.5 Experimental Proofs",
                "content": "<p class='mb-2 text-slate-300'>Consider three resistors $R_1, R_2, R_3$ joined end-to-end (Fig 11.6):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Activity 11.4 (Uniform Current):</strong> Shifting the ammeter to any position between the resistors gives the exact same reading! <strong>In a series circuit, current $I$ is constant through every resistor.</strong></li><li><strong>Activity 11.5 (Voltage Addition):</strong> Measuring voltmeter readings across individual resistors gives $V_1, V_2, V_3$. Measuring across the entire chain gives $V$:<br><span class='text-amber-400 font-mono font-bold text-xs sm:text-sm'>$$V = V_1 + V_2 + V_3$$</span></li></ul>"
            },
            {
                "title": "Mathematical Derivation of Equivalent Resistance",
                "content": "<p class='mb-2 text-slate-300'>Applying Ohm's law ($V = IR$) to each individual resistor:</p><p class='text-cyan-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$V_1 = I R_1, \\quad V_2 = I R_2, \\quad V_3 = I R_3$$</p><p class='text-slate-300 mb-2'>For the equivalent single resistor $R_s$ with total voltage $V = I R_s$:</p><p class='text-emerald-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$I R_s = I R_1 + I R_2 + I R_3 \\implies R_s = R_1 + R_2 + R_3$$</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>Key Principle:</strong> When several resistors are joined in series, the equivalent resistance $R_s$ equals the <strong>sum of their individual resistances</strong> and is therefore <strong>greater than any individual resistance</strong> in the group!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "In a series combination of three resistors (1 Ω, 2 Ω, and 3 Ω), how does the electric current compare across the three resistors?",
                "options": [
                    "Current is largest in the 1 Ω resistor",
                    "Current is largest in the 3 Ω resistor",
                    "The current is exactly the same through every resistor",
                    "Current fluctuates inversely with the square of voltage"
                ],
                "ans": 2,
                "solution": "In a series circuit, there is only one continuous conducting path; therefore, the current is identical in every part of the circuit and through each resistor (NCERT Page 182, Activity 11.4)."
            },
            {
                "q": "What is the equivalent resistance of three resistors of values 4 Ω, 8 Ω, and 12 Ω connected in series?",
                "options": [
                    "2.18 Ω",
                    "12 Ω",
                    "24 Ω",
                    "96 Ω"
                ],
                "ans": 2,
                "solution": "For resistors in series, Rs = R₁ + R₂ + R₃ = 4 + 8 + 12 = 24 Ω (NCERT Page 184, Eq. 11.14)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Series Circuit Calculations & Practical Limitations",
        "subtitle": "Chapter 11 • Pages 184–185",
        "tag": "Example 11.7 & Intext",
        "quote": "If a single bulb fuses in a series string, the entire circuit is broken and every appliance goes dark.",
        "lead": "Example 11.7 illustrates series potential division, while practical analysis highlights why series wiring is unsuitable for homes.",
        "narration": "Let us examine Example 11.7. An electric lamp of 20 ohms and a conductor of 4 ohms are connected in series to a 6-volt battery. Total resistance is 24 ohms, and circuit current is 0.25 amperes. The lamp gets 5 volts while the conductor gets 1 volt. Notice why series circuits are impractical for domestic wiring: if one component fails, the circuit opens and everything stops working, just like troubleshooting a fused bulb in decorative fairy lights.",
        "theory_blocks": [
            {
                "title": "Example 11.7: Lamp & Conductor in Series",
                "content": "<p class='mb-2 text-slate-300'>An electric lamp ($R_1 = 20\\ \\Omega$) and conductor ($R_2 = 4\\ \\Omega$) connected to a $6\\text{ V}$ battery (Fig 11.9):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>(a) Total Resistance:</strong> $R_s = R_1 + R_2 = 20 + 4 = \\mathbf{24\\ \\Omega}$.</li><li><strong>(b) Circuit Current:</strong> $I = \\frac{V}{R_s} = \\frac{6\\text{ V}}{24\\ \\Omega} = \\mathbf{0.25\\text{ A}}$.</li><li><strong>(c) Potential Differences:</strong><br>• Across lamp: $V_1 = I R_1 = 0.25\\text{ A} \\times 20\\ \\Omega = \\mathbf{5\\text{ V}}$.<br>• Across conductor: $V_2 = I R_2 = 0.25\\text{ A} \\times 4\\ \\Omega = \\mathbf{1\\text{ V}}$.<br><em>Check:</em> $V_1 + V_2 = 5\\text{ V} + 1\\text{ V} = 6\\text{ V}$ (Matches battery voltage!).</li></ul>"
            },
            {
                "title": "Why Series Wiring Fails in Household Circuits",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Single Fault Breakdown:</strong> In a series circuit, if any single appliance fuses or is switched off, the entire circuit is broken and <strong>none of the components work</strong>!</li><li><strong>Fairy Lights Nightmare:</strong> In decorative festival lights, an electrician spends hours locating the single fused bulb because every bulb must be tested individually.</li><li><strong>Differing Current Demands:</strong> An electric bulb needs $\\approx 0.18\\text{ A}$, while an electric heater requires $\\approx 2.2\\text{ A}$ (Example 11.3). In series, forcing the same current through both makes it impossible for either to operate properly!</li><li><strong>Cumulative Resistance:</strong> Adding devices increases $R_s$, severely reducing circuit current and power.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "A battery of 6 V is connected in series with a 5 Ω resistor, an 8 Ω resistor, and a 12 Ω resistor. What will be the reading on an ammeter in the circuit?",
                "options": [
                    "0.24 A",
                    "0.50 A",
                    "1.0 A",
                    "2.4 A"
                ],
                "ans": 0,
                "solution": "Total resistance Rs = 5 + 8 + 12 = 25 Ω. Current I = V / Rs = 6 V / 25 Ω = 0.24 A (NCERT Page 185, Intext Q2)."
            },
            {
                "q": "What will be the voltmeter reading connected across the 12 Ω resistor in the circuit above?",
                "options": [
                    "1.20 V",
                    "1.92 V",
                    "2.88 V",
                    "6.00 V"
                ],
                "ans": 2,
                "solution": "Potential difference across 12 Ω resistor is V = I × R = 0.24 A × 12 Ω = 2.88 V (NCERT Page 185, Intext Q2)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Resistors in Parallel: Derivation & Current Branching",
        "subtitle": "Chapter 11 • Pages 185–186",
        "tag": "Section 11.6.2 Parallel Combination",
        "quote": "In a parallel network, uniform voltage energizes every branch while currents divide: 1/Rp = 1/R1 + 1/R2 + 1/R3.",
        "lead": "Activity 11.6 proves that the potential difference across parallel branches is identical, while the total circuit current is the sum of branch currents.",
        "narration": "Now let us analyze resistors in parallel. When resistors are connected between two common junction points, they are in parallel. Activity 11.6 shows that the potential difference V across each individual resistor is identical to the battery voltage. However, the total current I divides into branch currents I1, I2, and I3. Applying Ohm's law, we find that the reciprocal of equivalent resistance 1 over Rp equals 1 over R1 plus 1 over R2 plus 1 over R3.",
        "theory_blocks": [
            {
                "title": "Activity 11.6 Experimental Observations",
                "content": "<p class='mb-2 text-slate-300'>Three resistors $R_1, R_2, R_3$ joined across points $X$ and $Y$ (Fig 11.10 & 11.11):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Uniform Potential Difference:</strong> A voltmeter connected across any individual resistor reads the exact same voltage $V$ (equal to the battery potential).</li><li><strong>Current Division:</strong> Inserting ammeters in each branch reveals currents $I_1, I_2, I_3$. The total main line current $I$ equals their sum:<br><span class='text-amber-400 font-mono font-bold text-xs sm:text-sm'>$$I = I_1 + I_2 + I_3$$</span></li></ul>"
            },
            {
                "title": "Derivation of Equivalent Parallel Resistance (Rp)",
                "content": "<p class='mb-2 text-slate-300'>Applying Ohm's law ($I = V/R$) to each parallel branch:</p><p class='text-cyan-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$I_1 = \\frac{V}{R_1}, \\quad I_2 = \\frac{V}{R_2}, \\quad I_3 = \\frac{V}{R_3}$$</p><p class='text-slate-300 mb-2'>For the equivalent parallel resistor $R_p$, main line current $I = V / R_p$:</p><p class='text-emerald-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$\\frac{V}{R_p} = \\frac{V}{R_1} + \\frac{V}{R_2} + \\frac{V}{R_3} \\implies \\mathbf{\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}}$$</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>Key Principle:</strong> The reciprocal of equivalent resistance equals the sum of the reciprocals of individual resistances.</li><li><strong>Crucial Theorem:</strong> $R_p$ is <strong>always less than the smallest individual resistance</strong> in the combination!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What happens to the equivalent resistance when more resistors are added in parallel to an existing circuit?",
                "options": [
                    "The equivalent resistance increases linearly",
                    "The equivalent resistance decreases, providing more conducting pathways",
                    "The equivalent resistance remains constant",
                    "The equivalent resistance fluctuates wildly"
                ],
                "ans": 1,
                "solution": "Adding resistors in parallel adds extra paths for charge flow, thereby decreasing the total equivalent resistance of the network (NCERT Page 186, Eq. 11.18)."
            },
            {
                "q": "Calculate the equivalent resistance when a 1 Ω resistor and a 10⁶ Ω resistor are connected in parallel.",
                "options": [
                    "Exactly 10⁶ Ω",
                    "1000001 Ω",
                    "Slightly less than 1 Ω",
                    "0.5 Ω"
                ],
                "ans": 2,
                "solution": "1/Rp = 1/1 + 1/10⁶ = (10⁶ + 1)/10⁶. Thus Rp = 10⁶ / (10⁶ + 1) ≈ 0.999999 Ω, which is strictly less than the smallest resistor (1 Ω) (NCERT Page 188, Intext Q1a)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Parallel & Mixed Circuit Networks Solved",
        "subtitle": "Chapter 11 • Pages 186–188",
        "tag": "Examples 11.8, 11.9 & Intext",
        "quote": "Parallel circuits divide current safely, maintain full supply voltage across each appliance, and prevent total blackout.",
        "lead": "Step-by-step solutions for multi-branch circuits and mixed series-parallel networks found in domestic electrical design.",
        "narration": "Let us solve worked Examples 11.8 and 11.9. In Example 11.8, resistors of 5, 10, and 30 ohms are in parallel across a 12-volt battery. Branch currents are 2.4, 1.2, and 0.4 amperes, yielding a total current of 4 amperes and an equivalent resistance of only 3 ohms. In Example 11.9, we simplify a mixed circuit by resolving parallel pairs first, then adding the equivalent series values to find the total resistance of 18 ohms.",
        "theory_blocks": [
            {
                "title": "Example 11.8 & Example 11.9 Step-by-Step",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Example 11.8 ($5, 10, 30\\ \\Omega$ on 12 V):</strong><br>• Branch currents: $I_1 = \\frac{12}{5} = 2.4\\text{ A}$, $I_2 = \\frac{12}{10} = 1.2\\text{ A}$, $I_3 = \\frac{12}{30} = 0.4\\text{ A}$.<br>• Total current: $I = 2.4 + 1.2 + 0.4 = \\mathbf{4\\text{ A}}$.<br>• Equivalent resistance: $\\frac{1}{R_p} = \\frac{1}{5} + \\frac{1}{10} + \\frac{1}{30} = \\frac{6+3+1}{30} = \\frac{10}{30} = \\frac{1}{3} \\implies \\mathbf{R_p = 3\\ \\Omega}$.</li><li><strong>Example 11.9 (Mixed Network Fig 11.12):</strong><br>• Group 1 ($R_1 = 10\\ \\Omega, R_2 = 40\\ \\Omega$ in parallel): $\\frac{1}{R'} = \\frac{1}{10} + \\frac{1}{40} = \\frac{5}{40} \\implies R' = 8\\ \\Omega$.<br>• Group 2 ($R_3 = 30, R_4 = 20, R_5 = 60\\ \\Omega$ in parallel): $\\frac{1}{R''} = \\frac{1}{30} + \\frac{1}{20} + \\frac{1}{60} = \\frac{6}{60} \\implies R'' = 10\\ \\Omega$.<br>• Total circuit resistance: $R = R' + R'' = 8 + 10 = \\mathbf{18\\ \\Omega}$.<br>• Total current: $I = \\frac{V}{R} = \\frac{12\\text{ V}}{18\\ \\Omega} = \\mathbf{0.67\\text{ A}}$.</li></ul>"
            },
            {
                "title": "Four Distinct Advantages of Household Parallel Wiring",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>1. Independent Operation:</strong> Each gadget has its own switch; turning off or failure of one appliance does not disrupt any other.</li><li><strong>2. Full Mains Voltage (220 V):</strong> Every appliance receives the full rated line voltage across its terminals.</li><li><strong>3. Appropriate Current Allocation:</strong> Different appliances (low current bulbs vs high current heaters) automatically draw current suited to their individual resistances.</li><li><strong>4. Lower Total Resistance:</strong> Parallel equivalent resistance is small, reducing unwanted line power dissipation.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "How should three resistors of resistances 2 Ω, 3 Ω, and 6 Ω be connected to yield a total resistance of 4 Ω?",
                "options": [
                    "All three in series",
                    "All three in parallel",
                    "3 Ω and 6 Ω in parallel, connected in series with the 2 Ω resistor",
                    "2 Ω and 3 Ω in series, connected in parallel with the 6 Ω resistor"
                ],
                "ans": 2,
                "solution": "Parallel combination of 3 Ω and 6 Ω gives Rp = (3 × 6)/(3 + 6) = 18/9 = 2 Ω. Connecting this in series with the 2 Ω resistor gives R_total = 2 + 2 = 4 Ω (NCERT Page 188, Intext Q4a)."
            },
            {
                "q": "What is the lowest total resistance that can be secured using four coils of resistances 4 Ω, 8 Ω, 12 Ω, and 24 Ω?",
                "options": [
                    "48 Ω",
                    "24 Ω",
                    "2 Ω",
                    "1 Ω"
                ],
                "ans": 2,
                "solution": "Lowest resistance is obtained by connecting all four coils in parallel: 1/Rp = 1/4 + 1/8 + 1/12 + 1/24 = (6 + 3 + 2 + 1)/24 = 12/24 = 1/2 Ω⁻¹ ⇒ Rp = 2 Ω (NCERT Page 188, Intext Q5b)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Heating Effect of Electric Current & Joule’s Law",
        "subtitle": "Chapter 11 • Pages 188–190",
        "tag": "Section 11.7 Joule's Heating",
        "quote": "Heat generated in a resistor is directly proportional to the square of current, resistance, and time: H = I²Rt.",
        "lead": "When electric current overcomes resistance, electrical energy is continuously transformed into heat.",
        "narration": "What happens to the chemical energy expended by a battery? In a purely resistive circuit, all electrical energy is dissipated as heat. The work done in moving charge Q through potential difference V is V times Q. Since charge Q equals current I times time t, the electrical energy supplied is V I t. Using Ohm's law, this becomes H equals I squared R t, known worldwide as Joule's Law of Heating.",
        "theory_blocks": [
            {
                "title": "Derivation of the Heating Formula",
                "content": "<p class='mb-2 text-slate-300'>Consider current $I$ flowing through a resistor $R$ across potential difference $V$ for time $t$ (Fig 11.13):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Work done in moving charge $Q$ across potential difference $V$ is $W = V Q$.</li><li>Since $Q = I t$, energy supplied by source in time $t$ is:<br><span class='text-amber-400 font-mono font-bold text-xs sm:text-sm'>$$W = V I t$$</span></li><li>Power input to the circuit is $P = W/t = V I$.</li><li>In a purely resistive circuit, this energy is dissipated entirely as heat ($H = W$):</li></ul><p class='text-cyan-400 font-mono font-bold text-xs sm:text-sm my-2'>$$H = V I t = (I R) I t = \\mathbf{I^2 R t}$$</p>"
            },
            {
                "title": "Joule’s Law of Heating: Three Fundamental Rules",
                "content": "<p class='mb-2 text-slate-300'><strong>Joule's Law of Heating</strong> states that the heat produced in a resistor is:</p><ol class='list-decimal pl-5 space-y-1.5 text-slate-300'><li><strong>Directly proportional to the square of current</strong> for a given resistance: $H \\propto I^2$.</li><li><strong>Directly proportional to the resistance</strong> for a given current: $H \\propto R$.</li><li><strong>Directly proportional to the time</strong> for which the current flows: $H \\propto t$.</li></ol><p class='text-xs text-slate-400 mt-2'><strong>Example 11.11:</strong> $100\\text{ J}$ heat produced each second in a $4\\ \\Omega$ resistor $\\implies I = \\sqrt{H / (Rt)} = \\sqrt{100 / (4 \\times 1)} = 5\\text{ A} \\implies V = IR = 5 \\times 4 = 20\\text{ V}$.</p>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why does the heating element of an electric heater glow red-hot, while its connecting power cord does not?",
                "options": [
                    "The cord is made of superconducting ceramic that emits no photons",
                    "The heating element has much higher resistance than the low-resistance copper cord; since H ∝ R for series current, element generates far more heat",
                    "Current only flows through the heating element and skips the cord completely",
                    "The cord is kept immersed in liquid nitrogen"
                ],
                "ans": 1,
                "solution": "The connecting cord (copper) has very low resistance, so heat produced (I²Rt) is negligible. The nichrome heating element has very high resistance, producing intense heat that makes it glow red-hot (NCERT Page 190, Intext Q1)."
            },
            {
                "q": "Compute the heat generated while transferring 96,000 C of charge in 1 hour through a potential difference of 50 V.",
                "options": [
                    "4.8 × 10⁴ J",
                    "9.6 × 10⁵ J",
                    "4.8 × 10⁶ J",
                    "2.4 × 10⁷ J"
                ],
                "ans": 2,
                "solution": "Heat generated H = W = V × Q = 50 V × 96,000 C = 4,800,000 J = 4.8 × 10⁶ J (NCERT Page 190, Intext Q2)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Practical Applications: Appliances, Bulbs & Safety Fuse",
        "subtitle": "Chapter 11 • Page 190",
        "tag": "Section 11.7.1 Applications of Heating",
        "quote": "Joule heating powers our toasters and kettles, illuminates tungsten bulbs, and protects our homes via safety fuses.",
        "lead": "From incandescent filaments glowing at 3380°C to sacrificial fuse wires interrupting short-circuits, heating effect is indispensable.",
        "narration": "Heating effects are utilized throughout everyday technology. In electric laundry irons, toasters, and ovens, nichrome coils convert electrical energy into useful heat. In electric bulbs, a strong tungsten filament with a melting point of 3380 degrees Celsius gets white-hot and radiates light, protected inside an inert nitrogen and argon atmosphere. In electric fuses, a low melting point wire melts whenever current exceeds the safety rating, breaking the circuit and preventing electrical fires.",
        "theory_blocks": [
            {
                "title": "Heating Appliances & Incandescent Bulbs",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Heating Appliances:</strong> Electric iron, toaster, oven, electric kettle, and room heaters utilize high-resistivity alloy coils (nichrome) to produce localized heat.</li><li><strong>Incandescent Bulbs:</strong><br>• <strong>Tungsten Filament:</strong> Has an extraordinary melting point of <strong>$3380^\\circ\\text{C}$</strong>, allowing it to reach incandescence without melting.<br>• <strong>Inert Gas Filling:</strong> Bulbs are filled with chemically unreactive <strong>nitrogen and argon</strong> gases to prevent filament oxidation and prolong service life.<br>• Most power consumed appears as heat; only a small fraction is radiated as visible light.</li></ul>"
            },
            {
                "title": "The Electric Fuse: Working Principle & Rating",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Function:</strong> A vital safety device that protects circuits and appliances by stopping the flow of unduly high current (overloads or short-circuits).</li><li><strong>Connection:</strong> <strong>Always connected in series</strong> with the live wire before the appliance.</li><li><strong>Mechanism:</strong> Made of a lead-tin alloy wire of suitable low melting point encased in a porcelain cartridge. When current exceeds the rated limit, $I^2Rt$ heat melts the fuse wire, breaking the circuit!</li><li><strong>Ratings:</strong> Domestic fuses are rated $1\\text{ A}, 2\\text{ A}, 3\\text{ A}, 5\\text{ A}, 10\\text{ A}$, etc.</li><li><strong>Worked Case:</strong> A $1\\text{ kW}$ iron at $220\\text{ V}$ draws $I = 1000/220 = 4.54\\text{ A}$. A <strong>$5\\text{ A}$ fuse</strong> must be used!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why are incandescent electric bulbs filled with chemically inactive nitrogen and argon gases?",
                "options": [
                    "To generate static electricity inside the bulb",
                    "To prevent oxidation of the hot tungsten filament and prolong its operational lifespan",
                    "To absorb all infrared radiation emitted by the filament",
                    "To convert visible light into ultraviolet radiation"
                ],
                "ans": 1,
                "solution": "Chemically inactive nitrogen and argon prevent the tungsten filament from burning or oxidising at temperatures exceeding 2500°C, significantly prolonging bulb life (NCERT Page 190)."
            },
            {
                "q": "An electric iron consumes 1 kW electric power when operated at 220 V. Which standard commercial fuse rating must be used?",
                "options": [
                    "1 A fuse",
                    "2 A fuse",
                    "3 A fuse",
                    "5 A fuse"
                ],
                "ans": 3,
                "solution": "Current drawn I = P/V = 1000 W / 220 V ≈ 4.54 A. The next standard commercial fuse rating above 4.54 A is a 5 A fuse (NCERT Page 190)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Electric Power & Commercial Energy Consumption",
        "subtitle": "Chapter 11 • Pages 191–192",
        "tag": "Section 11.8 Power & Units",
        "quote": "One kilowatt-hour equals 3.6 million joules—the commercial unit of electrical energy we pay utility companies to deliver.",
        "lead": "Electric power is the rate at which electrical energy is consumed, quantified in watts and billed in commercial kilowatt-hours.",
        "narration": "Let us explore electric power. Power is the rate at which electrical energy is consumed or dissipated. P equals V times I, which can also be written as I squared R or V squared over R. The SI unit of power is the watt, where one watt equals one volt multiplied by one ampere. In daily life, we use the commercial unit of energy: the kilowatt-hour, or unit. One kilowatt-hour equals 3.6 times 10 to the 6 joules. Remember, we do not pay for electrons; we pay for the energy to move them!",
        "theory_blocks": [
            {
                "title": "Formulas for Electric Power (P)",
                "content": "<p class='mb-2 text-slate-300'>Power is the rate of doing electrical work ($P = W/t$):</p><p class='text-amber-400 font-mono font-bold text-xs sm:text-sm mb-2'>$$P = V I = I^2 R = \\frac{V^2}{R}$$</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>The Watt (W):</strong> Power consumed when $1\\text{ A}$ flows at a potential difference of $1\\text{ V}$ ($1\\text{ W} = 1\\text{ V} \\times 1\\text{ A} = 1\\text{ V}\\cdot\\text{A}$).</li><li><strong>Kilowatt ($1\\text{ kW} = 1000\\text{ W}$):</strong> Practical unit for high-power appliances.</li><li><strong>Example 11.12:</strong> Bulb on $220\\text{ V}$ draws $0.50\\text{ A} \\implies P = VI = 220 \\times 0.50 = 110\\text{ W}$.</li></ul>"
            },
            {
                "title": "Commercial Energy Unit: The Kilowatt-Hour (kWh)",
                "content": "<p class='mb-2 text-slate-300'>Electrical energy is power multiplied by time ($E = P \\times t$):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Commercial Unit (The 'Unit'):</strong> <strong>Kilowatt-hour (kW h)</strong>.</li><li><strong>Joule Conversion:</strong><br><span class='text-cyan-400 font-mono font-bold text-xs sm:text-sm'>$$1\\text{ kW h} = 1000\\text{ W} \\times 3600\\text{ s} = 3,600,000\\text{ J} = \\mathbf{3.6 \\times 10^6\\text{ J}}$$</span></li><li><strong>More to Know:</strong> Electrons are <strong>not consumed</strong> in a circuit! We pay electricity boards for the energy needed to push electrons through our appliances.</li><li><strong>Example 11.13:</strong> A $400\\text{ W}$ refrigerator runs $8\\text{ h/day}$ for $30\\text{ days}$ $\\implies E = 400 \\times 8 \\times 30 = 96,000\\text{ Wh} = 96\\text{ kWh}$. At $\\text{Rs } 3.00/\\text{kWh}$, cost is $96 \\times 3 = \\mathbf{\\text{Rs } 288.00}$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "How many Joules of energy are represented by exactly 1 kilowatt-hour (1 commercial 'unit') of electricity?",
                "options": [
                    "3.6 × 10³ Joules",
                    "3.6 × 10⁵ Joules",
                    "3.6 × 10⁶ Joules",
                    "1.0 × 10⁶ Joules"
                ],
                "ans": 2,
                "solution": "1 kWh = 1000 W × 3600 s = 3,600,000 J = 3.6 × 10⁶ Joules (NCERT Page 191)."
            },
            {
                "q": "An electric motor takes 5 A from a 220 V supply line. What is the power of the motor and energy consumed in 2 hours?",
                "options": [
                    "P = 1100 W; Energy = 2.2 kWh",
                    "P = 44 W; Energy = 88 Wh",
                    "P = 2200 W; Energy = 4.4 kWh",
                    "P = 550 W; Energy = 1.1 kWh"
                ],
                "ans": 0,
                "solution": "P = V × I = 220 V × 5 A = 1100 W = 1.1 kW. Energy E = P × t = 1.1 kW × 2 h = 2.2 kWh = 2.2 × 3.6 × 10⁶ J = 7.92 × 10⁶ J (NCERT Page 192, Intext Q2)."
            }
        ]
    },
    {
        "id": 17,
        "title": "NCERT Textbook Exercises Solutions (Q1 to Q9)",
        "subtitle": "Chapter 11 • Page 193",
        "tag": "Exercises Q1 to Q9",
        "quote": "Rigorous application of circuit laws turns theoretical equations into definitive problem-solving precision.",
        "lead": "Complete step-by-step verified derivations and numerical solutions for official NCERT Exercises 1 through 9.",
        "narration": "Let us solve Exercises 1 through 9 from the textbook. In Question 1, cutting a wire of resistance R into 5 equal parts gives parts of R over 5. Connecting them in parallel yields R prime equals R over 25, giving a ratio of R to R prime of 25. In Question 3, a 220-volt 100-watt bulb operated at 110 volts consumes 25 watts. Follow each derivation carefully.",
        "theory_blocks": [
            {
                "title": "Exercise Questions 1 to 4 Detailed Derivations",
                "content": "<div class='space-y-2 text-xs text-slate-300'><p><strong>Q1: Wire Cut into 5 Equal Parts in Parallel:</strong><br>Resistance of each part is $r = R/5$. In parallel:<br>$1/R' = 5/r = 5/(R/5) = 25/R \\implies R' = R/25 \\implies \\mathbf{R/R' = 25}$ (Option d).</p><p><strong>Q2: Term NOT Representing Electrical Power:</strong><br>$P = VI = I^2R = V^2/R$. The expression $\\mathbf{IR^2}$ does NOT represent power (Option b).</p><p><strong>Q3: Bulb (220 V, 100 W) Operated at 110 V:</strong><br>Bulb resistance $R = V^2/P = 220^2 / 100 = 484\\ \\Omega$.<br>Power at $110\\text{ V}$: $P' = V'^2 / R = 110^2 / 484 = 12100 / 484 = \\mathbf{25\\text{ W}}$ (Option d).</p><p><strong>Q4: Ratio of Heat in Series vs Parallel at Same V:</strong><br>$H_s = \\frac{V^2 t}{R_s} = \\frac{V^2 t}{2R}$; $H_p = \\frac{V^2 t}{R_p} = \\frac{V^2 t}{R/2} = \\frac{2V^2 t}{R}$.<br>$\\frac{H_s}{H_p} = \\frac{1/2}{2} = \\mathbf{1:4}$ (Option c).</p></div>"
            },
            {
                "title": "Exercise Questions 5 to 9 Detailed Derivations",
                "content": "<div class='space-y-2 text-xs text-slate-300'><p><strong>Q5: Voltmeter Connection:</strong> Always connected in <strong>parallel</strong> across the two circuit points to measure potential difference.</p><p><strong>Q6: Copper Wire Length ($d = 0.5\\text{ mm}, \\rho = 1.6 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}, R = 10\\ \\Omega$):</strong><br>$A = \\pi (0.25 \\times 10^{-3})^2 = 1.963 \\times 10^{-7}\\text{ m}^2$.<br>$l = \\frac{RA}{\\rho} = \\frac{10 \\times 1.963 \\times 10^{-7}}{1.6 \\times 10^{-8}} = \\mathbf{122.7\\text{ m}}$.<br>Doubling diameter quadruples area ($A' = 4A$), so resistance becomes <strong>one-fourth: $10/4 = 2.5\\ \\Omega$</strong>.</p><p><strong>Q7: V–I Table Graph:</strong> Slope $R = \\Delta V / \\Delta I = (13.2 - 1.6) / (4.0 - 0.5) = 11.6 / 3.5 \\approx \\mathbf{3.3\\ \\Omega}$.</p><p><strong>Q8: Unknown Resistor ($V = 12\\text{ V}, I = 2.5\\text{ mA}$):</strong><br>$R = \\frac{V}{I} = \\frac{12}{2.5 \\times 10^{-3}} = \\mathbf{4800\\ \\Omega = 4.8\\text{ k}\\Omega}$.</p><p><strong>Q9: 9 V with Series Resistors (0.2, 0.3, 0.4, 0.5, 12 Ω):</strong><br>$R_s = 0.2 + 0.3 + 0.4 + 0.5 + 12 = 13.4\\ \\Omega$.<br>Current $I = 9 / 13.4 = \\mathbf{0.67\\text{ A}}$ through ALL resistors including $12\\ \\Omega$!</p></div>"
            }
        ],
        "checkpoints": [
            {
                "q": "An electric bulb is rated 220 V and 100 W. When it is operated on 110 V, the power consumed will be:",
                "options": [
                    "100 W",
                    "75 W",
                    "50 W",
                    "25 W"
                ],
                "ans": 3,
                "solution": "Resistance R = V²/P = 220²/100 = 484 Ω. Power at 110 V is P' = V'²/R = 110²/484 = 25 W (NCERT Page 193, Exercise Q3)."
            },
            {
                "q": "A copper wire of diameter 0.5 mm has resistance 10 Ω. How much does its resistance become if its diameter is doubled without changing its length?",
                "options": [
                    "20 Ω",
                    "5 Ω",
                    "2.5 Ω",
                    "1.25 Ω"
                ],
                "ans": 2,
                "solution": "Since R ∝ 1/A ∝ 1/d², doubling diameter increases cross-sectional area by 4 times. New resistance is R' = 10 / 4 = 2.5 Ω (NCERT Page 193, Exercise Q6)."
            }
        ]
    },
    {
        "id": 18,
        "title": "NCERT Textbook Exercises Solutions (Q10 to Q18)",
        "subtitle": "Chapter 11 • Pages 193–194",
        "tag": "Exercises Q10 to Q18",
        "quote": "Mastery of appliances, parallel bulb loading, power ratings, and heat dissipation concludes our electrical journey.",
        "lead": "Comprehensive solutions for textbook Exercises 10 through 18, completing 100% curriculum coverage.",
        "narration": "Finally, let us solve Exercises 10 through 18. In Question 10, four 176-ohm resistors in parallel carry 5 amperes on a 220-volt line. In Question 12, 110 ten-watt bulbs can be connected in parallel on a 5-ampere fuse. Question 14 shows that a 2-ohm resistor consumes exactly 8 watts in both specified circuits. Question 16 proves that a 250-watt TV running for one hour uses more energy than a 1200-watt toaster in ten minutes.",
        "theory_blocks": [
            {
                "title": "Exercise Questions 10 to 14 Derivations",
                "content": "<div class='space-y-2 text-xs text-slate-300'><p><strong>Q10: Number of 176 Ω Resistors for 5 A on 220 V:</strong><br>Required resistance $R_p = V/I = 220/5 = 44\\ \\Omega$.<br>Since $R_p = R/n \\implies 44 = 176/n \\implies n = 176/44 = \\mathbf{4\\text{ resistors}}$.</p><p><strong>Q11: Three 6 Ω Resistors for 9 Ω and 4 Ω:</strong><br>(i) $9\\ \\Omega$: Two in parallel ($6 \\parallel 6 = 3\\ \\Omega$) in series with third ($3 + 6 = 9\\ \\Omega$).<br>(ii) $4\\ \\Omega$: Two in series ($6 + 6 = 12\\ \\Omega$) in parallel with third ($12 \\parallel 6 = (12 \\times 6)/(18) = 4\\ \\Omega$).</p><p><strong>Q12: Parallel 10 W Bulbs on 220 V (Max 5 A):</strong><br>Max power $P_{\\max} = VI = 220 \\times 5 = 1100\\text{ W}$. Number of bulbs $n = 1100 / 10 = \\mathbf{110\\text{ lamps}}$.</p><p><strong>Q13: Hot Plate Two 24 Ω Coils on 220 V:</strong><br>(a) Separately: $I = 220/24 = \\mathbf{9.17\\text{ A}}$.<br>(b) In series ($R = 48\\ \\Omega$): $I = 220/48 = \\mathbf{4.58\\text{ A}}$.<br>(c) In parallel ($R = 12\\ \\Omega$): $I = 220/12 = \\mathbf{18.33\\text{ A}}$.</p><p><strong>Q14: Power in 2 Ω Resistor Comparison:</strong><br>(i) $6\\text{ V}$ with $1\\ \\Omega, 2\\ \\Omega$ series: $I = 6/(1+2) = 2\\text{ A} \\implies P = I^2R = 2^2 \\times 2 = \\mathbf{8\\text{ W}}$.<br>(ii) $4\\text{ V}$ with $12\\ \\Omega, 2\\ \\Omega$ parallel: $V = 4\\text{ V} \\implies P = V^2/R = 4^2/2 = \\mathbf{8\\text{ W}}$. Equal power!</p></div>"
            },
            {
                "title": "Exercise Questions 15 to 18 Solutions",
                "content": "<div class='space-y-2 text-xs text-slate-300'><p><strong>Q15: Two Lamps (100 W & 60 W at 220 V) in Parallel:</strong><br>$I_1 = 100/220 = 0.455\\text{ A}$; $I_2 = 60/220 = 0.273\\text{ A}$.<br>Total current drawn $I = 0.455 + 0.273 = \\mathbf{0.727\\text{ A} \\approx 0.73\\text{ A}}$.</p><p><strong>Q16: TV vs Toaster Energy Comparison:</strong><br>• TV ($250\\text{ W}, 1\\text{ h}$): $E = 250 \\times 3600 = \\mathbf{9.0 \\times 10^5\\text{ J}}$ ($250\\text{ Wh}$).<br>• Toaster ($1200\\text{ W}, 10\\text{ min} = 600\\text{ s}$): $E = 1200 \\times 600 = \\mathbf{7.2 \\times 10^5\\text{ J}}$ ($200\\text{ Wh}$).<br><em>Result:</em> The <strong>TV set consumes more energy</strong>!</p><p><strong>Q17: Heater Rate of Heat Development ($R = 44\\ \\Omega, I = 5\\text{ A}$):</strong><br>Rate of heat = Power $P = I^2R = 5^2 \\times 44 = 25 \\times 44 = \\mathbf{1100\\text{ J/s} = 1100\\text{ W}}$.</p><p><strong>Q18 Conceptual Explanations:</strong><br>(a) Tungsten has high melting point ($3380^\\circ\\text{C}$) and retains heat to glow.<br>(b) Alloys have higher resistivity and do not oxidise at high temperature.<br>(c) In series, current is uniform; if one fails, entire domestic circuit breaks.<br>(d) Resistance is inversely proportional to cross-sectional area ($R \\propto 1/A$).<br>(e) Copper and aluminium have very low resistivity, minimizing line transmission losses.</p></div>"
            }
        ],
        "checkpoints": [
            {
                "q": "How many 176 Ω resistors connected in parallel are required to carry 5 A on a 220 V line?",
                "options": [
                    "2 resistors",
                    "4 resistors",
                    "6 resistors",
                    "8 resistors"
                ],
                "ans": 1,
                "solution": "Required equivalent resistance Rp = V/I = 220/5 = 44 Ω. Since Rp = 176/n, n = 176/44 = 4 resistors (NCERT Page 193, Exercise Q10)."
            },
            {
                "q": "Which appliance consumes more electrical energy: a 250 W TV set in 1 hour or a 1200 W toaster in 10 minutes?",
                "options": [
                    "The 1200 W toaster consumes more energy",
                    "The 250 W TV set consumes more energy",
                    "Both consume exactly the same energy",
                    "Neither consumes energy because voltage is constant"
                ],
                "ans": 1,
                "solution": "TV energy = 250 W × 3600 s = 900,000 J (250 Wh). Toaster energy = 1200 W × 600 s = 720,000 J (200 Wh). The TV set consumes more energy (NCERT Page 194, Exercise Q16)."
            }
        ]
    }
]

QUIZ_SLIDES = [
    {
        "id": 19,
        "title": "Mastery Challenge: Electric Current, Charge & Potential",
        "subtitle": "Challenge Quiz 1 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 1: Current & Potential",
        "narration": "Welcome to Quiz Challenge 1! Test your foundational understanding of electric current, electron counts, potential difference, and circuit symbols with these ten board-level questions. Click View Solution on any card to examine the step-by-step teacher derivation in a popup.",
        "questions": [
            {
                "id": 1,
                "q": "A current of 0.75 A is drawn by a filament of an electric bulb for 20 minutes. The amount of electric charge that flows through the circuit is:",
                "options": ["15 C", "90 C", "900 C", "1500 C"],
                "ans": 2,
                "solution": "Given I = 0.75 A, t = 20 min = 20 × 60 = 1200 s. Charge Q = I × t = 0.75 A × 1200 s = 900 C (Formula: Q = It)."
            },
            {
                "id": 2,
                "q": "If the charge on an electron is 1.6 × 10⁻¹⁹ C, the number of electrons passing per second through a conductor carrying a current of 1 A is:",
                "options": ["6.25 × 10¹⁶", "6.25 × 10¹⁸", "1.6 × 10¹⁹", "6.25 × 10²¹"],
                "ans": 1,
                "solution": "For 1 A current, charge flowing per second is Q = 1 C. Number of electrons n = Q/e = 1 / (1.6 × 10⁻¹⁹) = 6.25 × 10¹⁸ electrons."
            },
            {
                "id": 3,
                "q": "How much work is done in moving a charge of 4 C across two points having a potential difference of 24 V?",
                "options": ["6 J", "48 J", "96 J", "120 J"],
                "ans": 2,
                "solution": "Work done W = V × Q = 24 V × 4 C = 96 J (Formula: V = W/Q ⇒ W = VQ)."
            },
            {
                "id": 4,
                "q": "Which instrument is always connected in series to measure electric current, and what is its ideal resistance?",
                "options": [
                    "Voltmeter; infinite resistance",
                    "Ammeter; zero (very low) resistance",
                    "Rheostat; variable resistance",
                    "Galvanometer; high resistance"
                ],
                "ans": 1,
                "solution": "An ammeter is connected in series to measure current and has very low (ideally zero) resistance so that it does not reduce the circuit current."
            },
            {
                "id": 5,
                "q": "The SI unit of electric potential difference is named after which physicist?",
                "options": ["André-Marie Ampère", "Alessandro Volta", "Georg Simon Ohm", "James Prescott Joule"],
                "ans": 1,
                "solution": "The volt (V) is named after Italian physicist Alessandro Volta (1745–1827), inventor of the electric battery (voltaic pile)."
            },
            {
                "id": 6,
                "q": "What is the equivalent value of 1 milliampere (1 mA) and 1 microampere (1 μA) in amperes respectively?",
                "options": [
                    "10⁻² A and 10⁻⁴ A",
                    "10⁻³ A and 10⁻⁶ A",
                    "10⁻⁶ A and 10⁻⁹ A",
                    "10³ A and 10⁶ A"
                ],
                "ans": 1,
                "solution": "1 mA = 10⁻³ A (one-thousandth of an ampere); 1 μA = 10⁻⁶ A (one-millionth of an ampere) (NCERT Page 172)."
            },
            {
                "id": 7,
                "q": "A closed plug key in a circuit diagram is represented by which symbol in NCERT Table 11.1?",
                "options": [
                    "(   )",
                    "( • )",
                    "—[ Resistor Symbol ]—",
                    "—( A )—"
                ],
                "ans": 1,
                "solution": "An open key is represented by ( ), while a closed plug key with current flowing is represented by brackets containing a central dot ( • )."
            },
            {
                "id": 8,
                "q": "In an electric circuit containing a cell, the direction of conventional current through the external circuit is:",
                "options": [
                    "From the negative terminal to the positive terminal",
                    "From the positive terminal to the negative terminal",
                    "In the same direction as the drift of electrons",
                    "Oscillating between both terminals"
                ],
                "ans": 1,
                "solution": "Conventionally, electric current flows outside the cell from the positive terminal (+) to the negative terminal (-), opposite to the flow of negative electrons."
            },
            {
                "id": 9,
                "q": "How is a voltmeter connected in a circuit to measure the potential difference across a resistor?",
                "options": [
                    "Always in series with the resistor",
                    "Always in parallel across the resistor",
                    "In series with the battery only",
                    "Directly between the earth ground and neutral line"
                ],
                "ans": 1,
                "solution": "A voltmeter has very high resistance and must be connected in parallel across the two points between which potential difference is to be measured."
            },
            {
                "id": 10,
                "q": "If 100 J of work is done in moving 5 C of charge between two points, what is the potential difference between them?",
                "options": ["5 V", "20 V", "100 V", "500 V"],
                "ans": 1,
                "solution": "Potential difference V = W / Q = 100 J / 5 C = 20 V (NCERT Eq. 11.2)."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge: Ohm’s Law, Resistance & Resistivity",
        "subtitle": "Challenge Quiz 2 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 2: Ohm's Law & Resistivity",
        "narration": "Quiz Challenge 2 focuses on Ohm's Law, electrical resistance, and resistivity calculations. Solve each problem carefully and click View Solution for full mathematical workings.",
        "questions": [
            {
                "id": 11,
                "q": "Ohm's law states that the potential difference across a metallic wire is directly proportional to current, provided that:",
                "options": [
                    "The wire's cross-sectional area changes continuously",
                    "Its temperature remains constant",
                    "The battery is replaced every 10 seconds",
                    "An alternating current generator is connected"
                ],
                "ans": 1,
                "solution": "Ohm's law holds strictly provided the temperature and other physical conditions of the metallic conductor remain constant (NCERT Page 176)."
            },
            {
                "id": 12,
                "q": "A potential difference of 10 V across a conductor produces a current of 2 A. What is the resistance of the conductor?",
                "options": ["0.2 Ω", "5 Ω", "12 Ω", "20 Ω"],
                "ans": 1,
                "solution": "From Ohm's law, R = V / I = 10 V / 2 A = 5 Ω."
            },
            {
                "id": 13,
                "q": "The SI unit of electrical resistivity is:",
                "options": ["Ohm (Ω)", "Ohm per metre (Ω/m)", "Ohm-metre (Ω·m)", "Volt per ampere (V/A)"],
                "ans": 2,
                "solution": "From R = ρ l / A, ρ = R A / l. Unit = (Ω × m²) / m = Ω·m (ohm-metre) (NCERT Page 178)."
            },
            {
                "id": 14,
                "q": "A cylindrical conductor of length l and uniform cross-section A has resistance R. Another conductor of length 2l and cross-section A/2 of the same material has resistance:",
                "options": ["R", "2R", "4R", "8R"],
                "ans": 2,
                "solution": "R' = ρ (2l) / (A/2) = 4 (ρ l / A) = 4R. Resistance quadruples!"
            },
            {
                "id": 15,
                "q": "Which of the following materials has the lowest electrical resistivity at 20°C?",
                "options": ["Copper", "Nichrome", "Silver", "Iron"],
                "ans": 2,
                "solution": "Silver has the lowest resistivity of all metals (1.60 × 10⁻⁸ Ω·m at 20°C) according to NCERT Table 11.2."
            },
            {
                "id": 16,
                "q": "If the radius of a metallic wire is halved while its length remains unchanged, its resistance becomes:",
                "options": ["Halved", "Doubled", "Four times its original value", "One-fourth its original value"],
                "ans": 2,
                "solution": "Area A = πr². If radius r is halved, area becomes A' = π(r/2)² = A/4. Since R ∝ 1/A, R' = 4R."
            },
            {
                "id": 17,
                "q": "Why is tungsten metal used almost exclusively for the incandescent filaments of electric lamps?",
                "options": [
                    "It has very high electrical resistivity and a melting point of 3380°C",
                    "It is the cheapest metal available",
                    "It absorbs all heat and remains freezing cold",
                    "It is a liquid metal at room temperature"
                ],
                "ans": 0,
                "solution": "Tungsten has an exceptionally high melting point (3380°C) and high tensile strength, enabling it to glow white-hot without melting (NCERT Page 179 & 190)."
            },
            {
                "id": 18,
                "q": "How does electrical resistivity vary when a metallic conductor is stretched without changing its temperature?",
                "options": [
                    "It increases proportionally with length",
                    "It decreases inversely with area",
                    "It remains completely unchanged because resistivity is a characteristic material property",
                    "It drops immediately to zero"
                ],
                "ans": 2,
                "solution": "Resistivity ρ depends solely on the nature of the material and temperature; it is independent of the conductor's length or cross-sectional area (NCERT Page 178)."
            },
            {
                "id": 19,
                "q": "A current of 2.5 mA flows through an unknown resistor connected to a 12 V battery. The resistance is:",
                "options": ["4.8 Ω", "48 Ω", "480 Ω", "4800 Ω"],
                "ans": 3,
                "solution": "I = 2.5 mA = 2.5 × 10⁻³ A. Resistance R = V / I = 12 / (2.5 × 10⁻³) = 4800 Ω = 4.8 kΩ (NCERT Page 193, Exercise Q8)."
            },
            {
                "id": 20,
                "q": "Nichrome is an alloy consisting of which metals?",
                "options": [
                    "Copper and zinc",
                    "Nickel, chromium, manganese, and iron",
                    "Copper, aluminium, and tin",
                    "Iron and carbon only"
                ],
                "ans": 1,
                "solution": "Nichrome is an alloy of Nickel (Ni), Chromium (Cr), Manganese (Mn), and Iron (Fe) (NCERT Page 175, Activity 11.1 footnote)."
            }
        ]
    },
    {
        "id": 21,
        "title": "Mastery Challenge: Series & Parallel Resistor Networks",
        "subtitle": "Challenge Quiz 3 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 3: Resistor Networks",
        "narration": "Quiz Challenge 3 tests your mastery of combination circuits: series strings, parallel branches, and mixed networks. Click View Solution on any question card for the verified derivation.",
        "questions": [
            {
                "id": 21,
                "q": "When two resistors of resistances R₁ and R₂ are connected in series, the equivalent resistance Rs is:",
                "options": [
                    "Rs = R₁ R₂ / (R₁ + R₂)",
                    "Rs = R₁ + R₂",
                    "Rs = 1/R₁ + 1/R₂",
                    "Rs = √(R₁² + R₂²)"
                ],
                "ans": 1,
                "solution": "For resistors in series, equivalent resistance equals the direct algebraic sum: Rs = R₁ + R₂ (NCERT Page 184)."
            },
            {
                "id": 22,
                "q": "When two resistors of resistances 3 Ω and 6 Ω are connected in parallel, their equivalent resistance Rp is:",
                "options": ["9 Ω", "4.5 Ω", "2 Ω", "0.5 Ω"],
                "ans": 2,
                "solution": "1/Rp = 1/3 + 1/6 = (2 + 1)/6 = 3/6 = 1/2 ⇒ Rp = 2 Ω."
            },
            {
                "id": 23,
                "q": "Three resistors of 2 Ω, 4 Ω, and 6 Ω are connected in series across a 12 V battery. What is the current flowing through the 4 Ω resistor?",
                "options": ["1 A", "2 A", "3 A", "6 A"],
                "ans": 0,
                "solution": "Rs = 2 + 4 + 6 = 12 Ω. Current I = V / Rs = 12 V / 12 Ω = 1 A. In a series circuit, current is identical (1 A) through all resistors!"
            },
            {
                "id": 24,
                "q": "In the circuit above, what is the potential difference across the 6 Ω resistor?",
                "options": ["2 V", "4 V", "6 V", "12 V"],
                "ans": 2,
                "solution": "V = I × R = 1 A × 6 Ω = 6 V."
            },
            {
                "id": 25,
                "q": "What is the equivalent resistance of 'n' identical resistors, each of resistance R, connected in parallel?",
                "options": ["n × R", "R / n", "n² R", "R / n²"],
                "ans": 1,
                "solution": "1/Rp = 1/R + 1/R + ... (n terms) = n / R ⇒ Rp = R / n."
            },
            {
                "id": 26,
                "q": "A piece of wire of resistance R is cut into 4 equal parts. These parts are then connected in parallel. What is the equivalent resistance R'?",
                "options": ["R / 4", "R / 8", "R / 16", "4 R"],
                "ans": 2,
                "solution": "Each part has resistance r = R/4. In parallel, 1/R' = 4 × (1/r) = 4 / (R/4) = 16/R ⇒ R' = R / 16."
            },
            {
                "id": 27,
                "q": "Why is the series arrangement NOT used for domestic lighting and power circuits?",
                "options": [
                    "Because series circuits require alternating current only",
                    "If one appliance fuses, the circuit breaks and all other appliances switch off",
                    "Because all appliances in series would receive 440 V",
                    "Because series circuits have zero total resistance"
                ],
                "ans": 1,
                "solution": "In a series circuit, a single failed component creates an open circuit, shutting down every connected device (NCERT Page 187)."
            },
            {
                "id": 28,
                "q": "How can three resistors of 6 Ω each be connected to produce an equivalent resistance of 9 Ω?",
                "options": [
                    "All three in series",
                    "All three in parallel",
                    "Two in parallel, connected in series with the third",
                    "Two in series, connected in parallel with the third"
                ],
                "ans": 2,
                "solution": "Two 6 Ω resistors in parallel have Rp = 6/2 = 3 Ω. Connecting this in series with the remaining 6 Ω gives 3 + 6 = 9 Ω (NCERT Page 193, Exercise Q11)."
            },
            {
                "id": 29,
                "q": "In a parallel circuit with branches of 10 Ω, 20 Ω, and 30 Ω connected to a 12 V battery, which resistor carries the largest current?",
                "options": [
                    "The 10 Ω resistor",
                    "The 20 Ω resistor",
                    "The 30 Ω resistor",
                    "All carry the same current"
                ],
                "ans": 0,
                "solution": "Voltage is constant across parallel branches (V = 12 V). Since I = V/R, current is largest through the branch with smallest resistance: I₁₀ = 12/10 = 1.2 A."
            },
            {
                "id": 30,
                "q": "What is the maximum resistance that can be obtained using four coils of resistances 4 Ω, 8 Ω, 12 Ω, and 24 Ω?",
                "options": ["24 Ω", "48 Ω", "96 Ω", "120 Ω"],
                "ans": 1,
                "solution": "Maximum resistance is achieved by connecting all resistors in series: Rs = 4 + 8 + 12 + 24 = 48 Ω (NCERT Page 188, Intext Q5a)."
            }
        ]
    },
    {
        "id": 22,
        "title": "Mastery Challenge: Joule’s Heating, Appliances & Electric Power",
        "subtitle": "Challenge Quiz 4 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 4: Heating & Electric Power",
        "narration": "Welcome to the final Mastery Challenge Quiz! Test your knowledge on Joule's law of heating, electric fuses, bulb ratings, power equations, and commercial electrical energy billing. Click View Solution on any card for full step-by-step teacher solutions.",
        "questions": [
            {
                "id": 31,
                "q": "According to Joule's law of heating, the heat produced in a resistor is directly proportional to:",
                "options": [
                    "The current I",
                    "The square of current I²",
                    "The square root of current √I",
                    "The inverse of current 1/I"
                ],
                "ans": 1,
                "solution": "Joule's law states H = I²Rt; heat is directly proportional to the square of current (I²) (NCERT Page 189, Eq. 11.21)."
            },
            {
                "id": 32,
                "q": "Which of the following does NOT represent electric power P?",
                "options": ["V × I", "I² × R", "I × R²", "V² / R"],
                "ans": 2,
                "solution": "Electric power is given by P = VI = I²R = V²/R. The expression IR² does not represent power (NCERT Page 193, Exercise Q2)."
            },
            {
                "id": 33,
                "q": "An electric iron of resistance 20 Ω takes a current of 5 A. The heat developed in 30 seconds is:",
                "options": ["1500 J", "3000 J", "15000 J", "30000 J"],
                "ans": 2,
                "solution": "Heat H = I²Rt = (5)² × 20 × 30 = 25 × 20 × 30 = 15,000 J = 1.5 × 10⁴ J (NCERT Page 190, Intext Q3)."
            },
            {
                "id": 34,
                "q": "An electric fuse wire protects circuits by melting when an overcurrent occurs. It must possess:",
                "options": [
                    "High melting point and high resistance",
                    "Low melting point and appropriate conductivity",
                    "Infinite resistance and zero melting point",
                    "Superconducting magnetic properties"
                ],
                "ans": 1,
                "solution": "A fuse wire must have a relatively low melting point (e.g. tin-lead alloy) so that excessive current heats and melts it promptly, interrupting the circuit (NCERT Page 190)."
            },
            {
                "id": 35,
                "q": "An electric bulb is rated 220 V and 100 W. Its operational resistance is:",
                "options": ["2.2 Ω", "48.4 Ω", "484 Ω", "2200 Ω"],
                "ans": 2,
                "solution": "From P = V²/R, R = V²/P = 220² / 100 = 48,400 / 100 = 484 Ω."
            },
            {
                "id": 36,
                "q": "One commercial unit of electrical energy (1 kilowatt-hour) equals:",
                "options": ["3.6 × 10⁵ J", "3.6 × 10⁶ J", "1.0 × 10⁶ J", "3.6 × 10⁸ J"],
                "ans": 1,
                "solution": "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J (NCERT Page 191)."
            },
            {
                "id": 37,
                "q": "Two electric bulbs rated 100 W and 60 W are connected in parallel to a 220 V mains supply. The current drawn from the line is:",
                "options": ["0.27 A", "0.45 A", "0.73 A", "1.10 A"],
                "ans": 2,
                "solution": "Total power P = 100 + 60 = 160 W. Total current I = P/V = 160/220 ≈ 0.727 A ≈ 0.73 A (NCERT Page 194, Exercise Q15)."
            },
            {
                "id": 38,
                "q": "An electric heater of resistance 44 Ω draws 5 A from the mains. The rate at which heat is developed in the heater is:",
                "options": ["220 W", "1100 W", "2200 W", "4400 W"],
                "ans": 1,
                "solution": "Rate of heat development is power: P = I²R = 5² × 44 = 25 × 44 = 1100 W (or J/s) (NCERT Page 194, Exercise Q17)."
            },
            {
                "id": 39,
                "q": "Why are copper and aluminium wires predominantly used for long-distance electrical power transmission?",
                "options": [
                    "They have extremely high electrical resistance to dissipate heat",
                    "They have very low electrical resistivity, minimizing power transmission loss (I²R)",
                    "They are magnetic and stick to pylons without screws",
                    "They emit visible light at night for highway illumination"
                ],
                "ans": 1,
                "solution": "Copper and aluminium have very low electrical resistivities (around 1.6 to 2.6 × 10⁻⁸ Ω·m), keeping line resistance R and resistive power loss (I²R) minimal (NCERT Page 179 & 194)."
            },
            {
                "id": 40,
                "q": "How many 10 W, 220 V electric bulbs can be connected in parallel on a 220 V line with a 5 A fuse without blowing the fuse?",
                "options": ["11 bulbs", "50 bulbs", "110 bulbs", "220 bulbs"],
                "ans": 2,
                "solution": "Maximum safe power P = V × I = 220 V × 5 A = 1100 W. Each bulb consumes 10 W. Number of bulbs n = 1100 W / 10 W = 110 bulbs (NCERT Page 193, Exercise Q12)."
            }
        ]
    }
]

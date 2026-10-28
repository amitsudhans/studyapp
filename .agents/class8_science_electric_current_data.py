# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 4: Electric Current: Magnetic & Heating Effects, and Chemical Cells
Complete curriculum dataset with compact headings, vocabulary, 16 content slides + 4 mastery challenge slides,
32 in-slide checkpoints, and 40 mastery quiz questions with comprehensive step-by-step solutions.
"""

SLIDES = [
    # SLIDE 1
    {
        "id": 1,
        "title": "Oersted's Discovery",
        "tag": "Magnetic Effect • Historical Milestone",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Welcome, young scientists! In 1820, Danish physicist Hans Christian Oersted stumbled upon one of the greatest accidental discoveries in human history: electric current can act like a magnet! Let's explore how an electric wire deflects a compass needle.",
        "theory": r"""
<h3>The Historic Discovery of 1820</h3>
<p>For centuries, electricity (lightning, static shocks) and magnetism (lodestones, compass needles) were viewed as entirely separate forces of nature. That changed in <strong>1820</strong> when Danish physicist and chemist <strong>Hans Christian Oersted</strong> set up an electric circuit on his lecture bench.</p>

<p>When Oersted switched current <strong>ON</strong> in a wire placed parallel to a magnetic compass, he was astonished to see the <strong>magnetic compass needle deflect immediately</strong> away from its natural North-South alignment! When he switched the current <strong>OFF</strong>, the needle instantly snapped back to geographic North.</p>

<h4>Core Scientific Principle</h4>
<ul>
  <li><strong>Magnetic Effect of Electric Current:</strong> Whenever an electric current flows through a conductor (wire), it generates an invisible magnetic field in the space surrounding the conductor.</li>
  <li><strong>Instantaneous Field:</strong> The magnetic field exists <em>only as long as current flows</em>. The moment the circuit opens and current drops to zero, the magnetic field disappears completely.</li>
  <li><strong>Reversing Current:</strong> Reversing the direction of current (swapping battery terminals) reverses the magnetic field's direction, causing the compass needle to deflect in the exact opposite direction.</li>
</ul>

<h4>Practical Impact</h4>
<p>Oersted's discovery proved that <strong>electricity creates magnetism</strong> (electromagnetism). This breakthrough laid the foundation for modern civilization—powering electric bells, motors, fans, loudspeakers, generators, and transformers!</p>
""",
        "vocabulary": [
            {"word": "Magnetic Effect", "definition": "The creation of a magnetic field in the surrounding space whenever electric current flows through a conductor."},
            {"word": "Conductor", "definition": "A material (such as copper or aluminum wire) that allows electric charges to flow freely through it."},
            {"word": "Deflection", "definition": "The angular movement or rotation of a magnetic compass needle away from its resting North-South position."},
            {"word": "Circuit", "definition": "A closed, unbroken conducting loop through which electric current can flow from the power source and back."}
        ],
        "sim_id": "oersted_compass_sim",
        "checkpoints": [
            {
                "question": "What happens to a magnetic compass needle placed near a wire when electric current is switched ON?",
                "options": [
                    "It stops working permanently",
                    "It deflects away from geographic North due to the wire's magnetic field",
                    "It points toward the ceiling",
                    "It loses all its magnetism"
                ],
                "correct": 1,
                "explanation": "Electric current flowing through the wire generates an invisible magnetic field around it, exerting a magnetic force that deflects the compass needle.",
                "solution": "1. Current flows through the conductor.\n2. A magnetic field forms around the conductor.\n3. The magnetic field exerts a torque on the magnetic compass needle.\n4. Therefore, the needle deflects away from geographic North."
            },
            {
                "question": "Who discovered the magnetic effect of electric current in 1820?",
                "options": [
                    "Alessandro Volta",
                    "Hans Christian Oersted",
                    "Alexander Fleming",
                    "Luigi Galvani"
                ],
                "correct": 1,
                "explanation": "Danish physicist Hans Christian Oersted discovered in 1820 that an electric current deflecting a magnetic compass needle proved the link between electricity and magnetism.",
                "solution": "Historical fact: Hans Christian Oersted observed this accidental deflection during a lecture demonstration in 1820."
            }
        ]
    },

    # SLIDE 2
    {
        "id": 2,
        "title": "Magnetic Field of Current",
        "tag": "Field Geometry • Right-Hand Rule",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "What does this invisible magnetic field look like? If you sprinkle iron filings around a straight vertical wire, they arrange into perfect concentric circles! Let's explore the shape, direction, and rules governing these lines of force.",
        "theory": r"""
<h3>Visualizing the Magnetic Field</h3>
<p>The magnetic field created around a straight current-carrying wire is not random. It forms a pattern of <strong>concentric circles</strong> centered on the wire, lying in a plane perpendicular to the wire.</p>

<h4>Key Properties of the Field</h4>
<ul>
  <li><strong>Field Strength vs. Distance:</strong> The magnetic field is strongest closest to the wire where the concentric circles are tightly packed. It weakens gradually as distance from the wire increases ($B \propto 1/r$).</li>
  <li><strong>Field Strength vs. Current:</strong> Increasing the electric current ($I$) increases the magnetic flux density ($B \propto I$), pushing compass needles with greater force.</li>
  <li><strong>Concentric Ring Geometry:</strong> Iron filings sprinkled onto a smooth cardboard sheet through which a straight wire passes will tap into circular concentric rings when current flows.</li>
</ul>

<h4>Right-Hand Thumb Rule</h4>
<p>To determine the direction of the magnetic field lines:</p>
<p><em>Imagine holding the current-carrying wire in your right hand with your thumb pointing in the direction of conventional electric current (from positive to negative). Your curled fingers will point in the exact direction of the magnetic field lines!</em></p>
<p>If the current flows vertically upward, the field lines circulate <strong>counter-clockwise</strong> when viewed from above. If current flows downward, the field lines circulate <strong>clockwise</strong>.</p>
""",
        "vocabulary": [
            {"word": "Magnetic Field", "definition": "The invisible region of space around a magnet or current-carrying wire where magnetic forces can be detected."},
            {"word": "Magnetic Field Lines", "definition": "Imaginary continuous lines whose tangent at any point gives the direction of the magnetic force."},
            {"word": "Right-Hand Thumb Rule", "definition": "A rule stating that if the right thumb points along current flow, curled fingers show the magnetic field direction."},
            {"word": "Concentric Circles", "definition": "Circles of different radii that all share the exact same central point or axis (the wire)."}
        ],
        "sim_id": "wire_field_lines_sim",
        "checkpoints": [
            {
                "question": "What geometric pattern do magnetic field lines form around a straight current-carrying conductor?",
                "options": [
                    "Concentric circles centered on the wire",
                    "Straight parallel lines radiating outward like sun rays",
                    "Random criss-cross zig-zag lines",
                    "Triangular loops"
                ],
                "correct": 0,
                "explanation": "Iron filings demonstrate that magnetic field lines form concentric circular loops around a straight current-carrying wire.",
                "solution": "1. Field around a long straight conductor has cylindrical symmetry.\n2. In any perpendicular cross-section, the lines form concentric circles centered on the wire.\n3. Direction is given by the Right-Hand Thumb Rule."
            },
            {
                "question": "If you double the electric current flowing through a straight wire, what happens to the magnetic field strength?",
                "options": [
                    "It drops to zero immediately",
                    "It doubles in strength",
                    "It decreases by half",
                    "It becomes electrostatic"
                ],
                "correct": 1,
                "explanation": "Magnetic field strength ($B$) is directly proportional to electric current ($I$). Doubling the current doubles the magnetic field strength.",
                "solution": r"Formula: $B \propto I$. When current $I$ increases from $1\text{A}$ to $2\text{A}$, magnetic field strength $B$ doubles."
            }
        ]
    },

    # SLIDE 3
    {
        "id": 3,
        "title": "Electromagnet Anatomy",
        "tag": "Solenoid & Core • Temporary Magnetism",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "A single straight wire creates a modest magnetic field, but what if we wind it into hundreds of tight circular coils? We get a solenoid! Add an iron core inside, and you've created a mighty electromagnet. Let's inspect its anatomy.",
        "theory": r"""
<h3>What is an Electromagnet?</h3>
<p>An <strong>electromagnet</strong> is a magnet consisting of an insulated wire coil wound tightly around a ferromagnetic core (usually soft iron) that produces a strong magnetic field only when an electric current passes through the coil.</p>

<h4>Key Components</h4>
<ul>
  <li><strong>Solenoid (Wire Coil):</strong> A long cylindrical coil of insulated copper wire containing many closely spaced circular turns. Each individual turn produces a small magnetic field; because all turns circulate current in the same direction, their magnetic fields add together constructively!</li>
  <li><strong>Soft Iron Core:</strong> A rod of soft iron (or an iron nail) placed inside the solenoid. Iron has high magnetic permeability, which concentrates and amplifies the magnetic field lines by hundreds of times!</li>
  <li><strong>Insulation Coating:</strong> The copper wire is coated with enamel or varnish insulation to prevent short-circuiting between adjacent touching turns.</li>
</ul>

<h4>Magnetic Polarity</h4>
<p>An electromagnet behaves exactly like a bar magnet, possessing distinct <strong>North (N)</strong> and <strong>South (S)</strong> poles at its two ends. Polarity is determined by the direction of current:</p>
<ul>
  <li><strong>Clock Face Rule:</strong> Looking at an end face of the coil, if the electric current appears to flow in a <strong>clockwise</strong> direction, that face is a <strong>South pole (S)</strong>. If it flows in a <strong>counter-clockwise</strong> direction, that face is a <strong>North pole (N)</strong>.</li>
  <li><strong>Reversibility:</strong> Swapping battery connections instantly swaps the North and South poles!</li>
</ul>
""",
        "vocabulary": [
            {"word": "Electromagnet", "definition": "A temporary magnet created by winding an insulated wire coil around a magnetic core and passing electric current through it."},
            {"word": "Solenoid", "definition": "A long cylindrical coil of insulated wire consisting of many turns that generates a uniform magnetic field inside."},
            {"word": "Soft Iron Core", "definition": "A high-permeability iron rod inserted inside a coil to vastly concentrate and amplify magnetic field strength."},
            {"word": "Magnetic Polarity", "definition": "The orientation of North and South magnetic poles at opposite ends of a magnet or energized solenoid."}
        ],
        "sim_id": "electromagnet_anatomy_sim",
        "checkpoints": [
            {
                "question": "Why is an insulated copper wire used to build an electromagnet rather than bare uninsulated wire?",
                "options": [
                    "To prevent electric current from jumping between adjacent turns and short-circuiting",
                    "To make the wire magnetic even without battery power",
                    "To keep the wire cool and prevent melting",
                    "To make the wire transparent"
                ],
                "correct": 0,
                "explanation": "Insulation forces the current to travel through every single spiral loop, ensuring the magnetic fields of all turns add up constructively.",
                "solution": "1. If bare wire touches adjacent turns, current takes the shortest path across contact points (short circuit).\n2. Insulation ensures current spirals through every turn of the coil, maximizing total magnetic field."
            },
            {
                "question": "Why is soft iron preferred over steel for making the core of a temporary electromagnet?",
                "options": [
                    "Soft iron magnetizes rapidly and loses magnetism immediately when current is cut off",
                    "Soft iron becomes a permanent magnet forever",
                    "Soft iron does not conduct magnetic field lines",
                    "Soft iron melts easily at room temperature"
                ],
                "correct": 0,
                "explanation": "Soft iron is easily magnetized when current flows and demagnetizes instantly when current ceases, making it ideal for temporary electromagnets.",
                "solution": "Soft iron has high magnetic permeability and low retentivity (coercivity), meaning it does not retain residual magnetism when power is switched off."
            }
        ]
    },

    # SLIDE 4
    {
        "id": 4,
        "title": "Electromagnet Strength",
        "tag": "Controlling Variables • Field Tuning",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "How can an engineer build an electromagnet capable of lifting an entire steel automobile? By mastering the three control variables of electromagnet strength! Let's experiment with turns, current, and core materials.",
        "theory": r"""
<h3>The Factors Governing Electromagnet Strength</h3>
<p>Unlike natural permanent magnets whose strength is fixed, an electromagnet's lifting power can be precisely controlled and scaled by adjusting three main factors:</p>

<h4>1. Number of Turns in the Coil ($N$)</h4>
<p>The total magnetic field is the algebraic sum of the magnetic fields produced by every single turn of wire. Increasing the number of turns from 20 to 100 turns concentrates five times as many magnetic loops in the same volume, greatly multiplying the pulling force ($B \propto N$).</p>

<h4>2. Magnitude of Electric Current ($I$)</h4>
<p>Supplying a higher current by adding more cells or a higher-voltage battery drives more charges through the coil per second. A stronger current generates a denser magnetic flux ($B \propto I$).</p>

<h4>3. The Core Material</h4>
<p>Placing a ferromagnetic material (like soft iron) inside the coil concentrates magnetic field lines through the core because iron has a magnetic permeability hundreds of times greater than empty air.</p>

<h4>Electromagnet Formula</h4>
<p>For a solenoid of length $L$ with $N$ turns carrying current $I$ with a core of relative permeability $\mu_r$:</p>
<p style="text-align: center; font-weight: bold; color: #38bdf8;">
  $$B = \mu_r \mu_0 \left(\frac{N}{L}\right) I$$
</p>
<p>Where $B$ is the magnetic flux density (in Tesla). Increasing either $N$ or $I$, or using soft iron ($\mu_r \gg 1$), drastically increases $B$!</p>
""",
        "vocabulary": [
            {"word": "Magnetic Flux Density", "definition": "A quantitative measure of the strength and concentration of magnetic field lines passing through a given area ($B$)."},
            {"word": "Number of Turns", "definition": "The total count of complete circular wire loops wound around the core of a coil or solenoid."},
            {"word": "Current Magnitude", "definition": "The rate of electric charge flow passing through the wire, measured in Amperes (A)."},
            {"word": "Magnetic Permeability", "definition": "The ability of a substance (like soft iron) to support and concentrate magnetic field lines within itself."}
        ],
        "sim_id": "electromagnet_strength_sim",
        "checkpoints": [
            {
                "question": "Which of the following modifications will INCREASE the lifting strength of an electromagnet?",
                "options": [
                    "Decreasing the number of turns of wire",
                    "Removing the iron core so the coil is empty air",
                    "Increasing the electric current flowing through the coil",
                    "Disconnecting one of the batteries"
                ],
                "correct": 2,
                "explanation": r"Increasing current ($I$) directly increases the magnetic field strength ($B \propto I$), allowing the electromagnet to lift heavier iron loads.",
                "solution": r"Strength depends on: $B \propto N \cdot I$. Increasing current $I$ increases $B$ proportionally."
            },
            {
                "question": "If an electromagnet with 30 turns lifts 4 paperclips, approximately how many will it lift if turns are increased to 90 at the same current?",
                "options": [
                    "4 paperclips",
                    "12 paperclips",
                    "1 paperclip",
                    "0 paperclips"
                ],
                "correct": 1,
                "explanation": "Increasing turns by 3 times ($30 \times 3 = 90$) roughly triples the magnetic field strength, allowing it to lift about $4 \times 3 = 12$ paperclips.",
                "solution": "Ratio: $N_2 / N_1 = 90 / 30 = 3$. Expected lifting capacity = $4 \times 3 = 12$ paperclips."
            }
        ]
    },

    # SLIDE 5
    {
        "id": 5,
        "title": "Industrial Electromagnet Cranes",
        "tag": "Scrap Yards • Switchable Magnetism",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Imagine trying to sort mountain-high piles of scrap metal by hand! Heavy-duty industrial cranes use massive electromagnets to lift tons of scrap iron and release them at the flick of a switch. Let's see how they work.",
        "theory": r"""
<h3>The Scrap Yard Workhorse</h3>
<p>In recycling centers, scrap yards, ports, and steel mills, handling jagged scrap metal, discarded car bodies, and heavy steel girders is dangerous and time-consuming. <strong>Industrial lifting electromagnets</strong> suspended from heavy cranes solve this effortlessly.</p>

<h4>How the Lifting Crane Operates</h4>
<ol>
  <li><strong>Positioning:</strong> The crane operator lowers the massive circular electromagnet disk onto a pile of mixed waste (steel, aluminum, wood, glass, plastics).</li>
  <li><strong>Energizing (Current ON):</strong> The operator flips a switch to turn current <strong>ON</strong>. A powerful magnetic field instantly magnetizes the heavy iron disk.</li>
  <li><strong>Magnetic Sorting:</strong> Ferromagnetic materials (iron, steel) snap firmly to the bottom face of the magnet. Non-magnetic materials (copper, aluminum, plastics, glass) are left behind on the ground!</li>
  <li><strong>Transportation:</strong> The crane lifts the load and swings it over to a train hopper or furnace feed chute.</li>
  <li><strong>Release (Current OFF):</strong> The operator turns the current <strong>OFF</strong>. The magnetic field instantly collapses to zero, and the entire heavy load drops cleanly into place!</li>
</ol>

<h4>Advantage Over Permanent Magnets</h4>
<p>A permanent magnet of equivalent strength would be useless for this job—once it grabbed a five-ton steel beam, workers would have no way to pry it off! The superpower of an electromagnet is its <strong>instant switchability</strong>.</p>
""",
        "vocabulary": [
            {"word": "Industrial Electromagnet", "definition": "A heavy-duty crane-mounted magnet designed to lift and drop tons of ferromagnetic scrap metal on command."},
            {"word": "Ferromagnetic Material", "definition": "Substances like iron, steel, nickel, and cobalt that are strongly attracted by magnetic fields and can be magnetized."},
            {"word": "Switchable Magnetism", "definition": "The operational ability to activate or collapse a magnetic field instantly by opening or closing an electrical circuit."},
            {"word": "Scrap Sorting", "definition": "The industrial process of separating iron and steel recyclables from non-magnetic plastics, aluminum, and glass."}
        ],
        "sim_id": "scrap_crane_sim",
        "checkpoints": [
            {
                "question": "Why are permanent magnets NOT used on scrap yard cranes to unload heavy steel scrap?",
                "options": [
                    "Permanent magnets are too expensive to build",
                    "There is no easy way to release or drop the heavy steel once attached to a permanent magnet",
                    "Permanent magnets only attract plastic",
                    "Permanent magnets require high voltage electricity"
                ],
                "correct": 1,
                "explanation": "An electromagnet's magnetism can be turned OFF instantly to release the load, whereas a strong permanent magnet cannot be switched off.",
                "solution": "1. Permanent magnets have non-switchable magnetic fields.\n2. Once tons of steel stick, manual detachment is impossible.\n3. Electromagnets drop loads instantly when current is cut off."
            },
            {
                "question": "Which of the following materials will NOT be picked up by a crane's lifting electromagnet?",
                "options": [
                    "Cast iron machine blocks",
                    "Steel structural girders",
                    "Aluminum drink cans and plastic bottles",
                    "Iron automotive scrap"
                ],
                "correct": 2,
                "explanation": "Electromagnets only attract ferromagnetic materials (iron, steel, nickel, cobalt). Aluminum, copper, and plastics are non-magnetic.",
                "solution": "Aluminum and plastics are diamagnetic/non-magnetic, so magnetic forces cannot attract them."
            }
        ]
    },

    # SLIDE 6
    {
        "id": 6,
        "title": "Earth's Magnetic Shield",
        "tag": "Geomagnetism • Planetary Dynamo",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Did you know that you are standing on a giant, spinning electromagnet? Deep beneath our feet, churning molten liquid iron generates Earth's geomagnetic field, shielding us from cosmic radiation and guiding migratory birds!",
        "theory": r"""
<h3>The Earth as a Giant Magnet</h3>
<p>Earth acts as though a gigantic bar magnet were buried inside its interior, inclined at an angle of roughly $11.3^\circ$ to its geographic rotational axis. This magnetic field is why small compass needles align in a North-South orientation anywhere on the globe.</p>

<h4>The Geodynamo: What Creates the Field?</h4>
<ul>
  <li><strong>Outer Core Convection:</strong> Deep inside Earth (between 2,900 km and 5,150 km below the crust), there is an <strong>outer core composed of molten liquid iron and nickel</strong>.</li>
  <li><strong>Electric Currents in Liquid Metal:</strong> As heat escapes from Earth's solid inner core, convection currents churn this molten liquid metal. Earth's daily rotation adds spiral Coriolis forces.</li>
  <li><strong>Dynamo Action:</strong> These swirling conductive flows generate gigantic electric currents, which in turn produce Earth's global magnetic field (the <em>Geodynamo</em>).</li>
</ul>

<h4>Vital Roles of Earth's Magnetic Shield</h4>
<ol>
  <li><strong>The Magnetosphere Shield:</strong> The magnetic field extends tens of thousands of kilometers into outer space, creating a protective bubble (the <em>magnetosphere</em>) that deflects hazardous solar wind particles and lethal cosmic radiation. Without it, our atmosphere would be stripped away!</li>
  <li><strong>Animal Navigation (Magnetoreception):</strong> Migratory birds, sea turtles, honeybees, and whales possess microscopic biological magnetite crystals that detect Earth's field, allowing them to navigate thousands of miles across oceans without maps.</li>
</ol>
""",
        "vocabulary": [
            {"word": "Geomagnetism", "definition": "The natural magnetic field generated by and surrounding planet Earth."},
            {"word": "Geodynamo", "definition": "The physical mechanism whereby convection in Earth's molten iron outer core generates continuous global magnetic fields."},
            {"word": "Magnetosphere", "definition": "The protective magnetic region surrounding Earth that deflects energetic charged particles emitted by the Sun (solar wind)."},
            {"word": "Magnetoreception", "definition": "The biological sensory ability of animals (such as migratory birds) to perceive Earth's magnetic field for navigation."}
        ],
        "sim_id": "earth_magnetism_sim",
        "checkpoints": [
            {
                "question": "What physical process generates Earth's natural magnetic field?",
                "options": [
                    "Giant solid bar magnets buried in the Himalayan mountains",
                    "Convection currents of molten liquid iron and nickel in Earth's outer core",
                    "Friction between ocean waves and sandy coastlines",
                    "Solar light reflecting off the polar ice caps"
                ],
                "correct": 1,
                "explanation": "The movement of electrically conductive molten iron and nickel in Earth's outer core acts as a planetary geodynamo, generating Earth's magnetic field.",
                "solution": "Molten iron convection + planetary rotation = moving electric charges = massive geomagnetic dynamo."
            },
            {
                "question": "How does Earth's magnetic field protect biological life on our planet?",
                "options": [
                    "It keeps Earth warm like an electric blanket",
                    "It deflects dangerous solar wind particles and cosmic radiation",
                    "It stops earthquakes from occurring",
                    "It generates oxygen in the clouds"
                ],
                "correct": 1,
                "explanation": "Earth's magnetosphere deflects harmful energetic charged particles streaming from the Sun (solar wind), preventing them from stripping the atmosphere and harming living tissue.",
                "solution": "The magnetosphere acts as a cosmic magnetic shield deflecting ionized solar wind particles."
            }
        ]
    },

    # SLIDE 7
    {
        "id": 7,
        "title": "Resistance & Heating Effect",
        "tag": "Joule Heating • Microscopic Collisions",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Why does your phone charger or laptop adapter get warm after hours of use? When electrons hustle through a conductor, they encounter resistance, colliding with metal atoms and generating heat! Let's explore the heating effect of electric current.",
        "theory": r"""
<h3>The Origin of Electric Heating</h3>
<p>When an electric current passes through a conductor, the conductor offers opposition or friction to the flow of charges. This opposition is known as <strong>electrical resistance ($R$)</strong>.</p>

<h4>Microscopic Mechanism of Heating</h4>
<ol>
  <li><strong>Electric Field Acceleration:</strong> A battery or power outlet establishes an electric field across the wire, pulling free electrons through the metal lattice.</li>
  <li><strong>Lattice Collisions:</strong> As these electrons drift, they repeatedly collide with the vibrating positive metal ions (atoms) fixed in the conductor's crystal lattice.</li>
  <li><strong>Energy Transfer:</strong> In each collision, electrons transfer a portion of their kinetic energy to the lattice ions, causing the ions to vibrate more violently.</li>
  <li><strong>Temperature Rise:</strong> The increased vibrational kinetic energy of the metal lattice manifests macroscopically as an increase in temperature—converting electrical energy into <strong>thermal (heat) energy</strong>!</li>
</ol>

<h4>The Heating Effect of Electric Current</h4>
<p>This conversion of electrical energy into thermal energy when current flows through a resistive conductor is called the <strong>heating effect of electric current</strong> (or <em>Joule heating</em>).</p>
<p>While heating represents unwanted energy loss in transmission cables and computer chips, it is intentionally harnessed in hundreds of household and industrial appliances!</p>
""",
        "vocabulary": [
            {"word": "Electrical Resistance", "definition": "The property of a conductor by virtue of which it opposes or impedes the flow of electric current through it ($R$, measured in Ohms $\\Omega$)."},
            {"word": "Heating Effect", "definition": "The phenomenon by which electrical energy is converted into heat energy as current overcomes resistance in a conductor."},
            {"word": "Lattice Ions", "definition": "Fixed metal atoms arranged in a regular geometric crystal array that vibrate and collide with passing conduction electrons."},
            {"word": "Joule Heating", "definition": "The scientific term for the thermal energy generated per second inside a resistive conductor carrying electric current."}
        ],
        "sim_id": "electron_collision_sim",
        "checkpoints": [
            {
                "question": "What causes a conductor to heat up when an electric current passes through it?",
                "options": [
                    "Electrons colliding with the vibrating atoms (lattice ions) of the conductor",
                    "Chemical combustion of the metal wire",
                    "Air friction rubbing against the outside of the rubber insulation",
                    "Nuclear fission inside the copper atoms"
                ],
                "correct": 0,
                "explanation": "Collisions between moving free electrons and the fixed lattice ions transfer kinetic energy into lattice vibrations, which manifests as heat.",
                "solution": "Drifting electrons collide with lattice ions $\\rightarrow$ lattice vibration increases $\\rightarrow$ temperature rises."
            },
            {
                "question": "What is the scientific term for the opposition offered by a conductor to the flow of electric current?",
                "options": [
                    "Capacitance",
                    "Electrical Resistance",
                    "Inductance",
                    "Electromagnetism"
                ],
                "correct": 1,
                "explanation": "Electrical resistance is the property that measures how strongly a material opposes the passage of electric current.",
                "solution": "Resistance ($R$, unit: Ohms $\\Omega$) quantifies opposition to electric current flow."
            }
        ]
    },

    # SLIDE 8
    {
        "id": 8,
        "title": "Nichrome Heating Elements",
        "tag": "Material Science • Copper vs. Nichrome",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Why are connection cords made of copper, while toaster coils are made of nichrome? If you pass current through both, the copper cord stays cool, but the nichrome coil glows fiery red! Let's examine material resistance.",
        "theory": r"""
<h3>The Tale of Two Conductors: Copper vs. Nichrome</h3>
<p>Different materials offer vastly different resistance to electric current. The selection of wire material determines whether a circuit conducts electricity with minimal loss or converts it efficiently into glowing heat.</p>

<h4>Copper Wire: The Ideal Transmitter</h4>
<ul>
  <li><strong>Extremely Low Resistance:</strong> Copper is a premier electrical conductor with very low resistivity ($\approx 1.68 \times 10^{-8} \;\Omega\cdot\text{m}$). Electrons glide through with minimal collisions.</li>
  <li><strong>Stays Cool:</strong> Because resistance is negligible, connecting wires and appliance power cords generate almost no heat, safely delivering power without wasting energy.</li>
</ul>

<h4>Nichrome Wire: The Heating Specialist</h4>
<ul>
  <li><strong>Composition:</strong> An alloy composed of approximately <strong>80% Nickel (Ni)</strong> and <strong>20% Chromium (Cr)</strong>.</li>
  <li><strong>High Electrical Resistance:</strong> Nichrome offers roughly <strong>60 times higher resistance</strong> than copper of identical dimensions! Electrons undergo intense lattice collisions.</li>
  <li><strong>High Melting Point:</strong> Nichrome melts at approximately <strong>$1,400^\circ\text{C}$</strong>, allowing it to glow orange-red hot without melting or breaking.</li>
  <li><strong>Resistance to Oxidation:</strong> Unlike iron, nichrome forms an invisible protective chromium oxide surface layer that prevents it from burning or oxidizing in atmospheric oxygen at high temperatures.</li>
</ul>

<h4>The Heating Element</h4>
<p>The specialized high-resistance coil or rod inside an electric toaster, geyser, or room heater is called the <strong>heating element</strong>.</p>
""",
        "vocabulary": [
            {"word": "Heating Element", "definition": "A high-resistance, heat-tolerant wire coil (typically nichrome) designed to convert electric current into intense heat."},
            {"word": "Nichrome", "definition": "A metallic alloy of nickel and chromium with high electrical resistivity, high melting point, and extreme resistance to oxidation."},
            {"word": "Resistivity", "definition": "The intrinsic physical property of a material that quantifies how strongly it opposes electric current flow."},
            {"word": "Oxidation Resistance", "definition": "The ability of an alloy to resist reacting with atmospheric oxygen at red-hot temperatures, preventing wire burnout."}
        ],
        "sim_id": "nichrome_copper_sim",
        "checkpoints": [
            {
                "question": "Why is nichrome wire chosen for the heating elements of electric toasters and irons instead of copper?",
                "options": [
                    "Nichrome is cheaper than copper and conducts electricity better",
                    "Nichrome has high resistance, a high melting point, and does not oxidize when red-hot",
                    "Nichrome is a liquid at room temperature",
                    "Nichrome produces a strong magnetic field that cooks food"
                ],
                "correct": 1,
                "explanation": "Nichrome's high resistance produces intense heat, while its high melting point ($1400^\\circ\\text{C}$) and anti-oxidation properties prevent it from burning out.",
                "solution": "Key criteria for heating elements: High resistivity + High melting point + Oxidation resistance. Nichrome meets all three."
            },
            {
                "question": "What happens to the copper cord connecting an electric room heater to the wall socket while the heater runs?",
                "options": [
                    "It glows orange-red hot just like the heating element",
                    "It stays cool because copper has very low electrical resistance",
                    "It melts within two minutes",
                    "It converts electricity into magnetic waves"
                ],
                "correct": 1,
                "explanation": "Copper has extremely low electrical resistance, so negligible heat is generated in the power cord, keeping it safe and cool to touch.",
                "solution": "Since $H = I^2 R t$ and $R_{\\text{copper}} \\approx 0$, thermal heat dissipation in the copper cord is minimal."
            }
        ]
    },

    # SLIDE 9
    {
        "id": 9,
        "title": "Joule's Heating & Filaments",
        "tag": "Mathematical Law • Incandescent Glow",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "British physicist James Prescott Joule discovered the exact mathematical formula governing heat generation: $H = I^2 R t$! Let's see how tweaking current, resistance, and wire thickness makes a bulb filament glow brilliant white.",
        "theory": r"""
<h3>Joule's Law of Heating</h3>
<p>In the 1840s, <strong>James Prescott Joule</strong> established that the heat ($H$) produced in a resistor is directly proportional to three independent physical factors:</p>

<p style="text-align: center; font-size: 1.25rem; font-weight: bold; color: #f59e0b;">
  $$H = I^2 R t$$
</p>

<h4>The Three Governing Factors</h4>
<ol>
  <li><strong>Square of Electric Current ($I^2$):</strong> Heat generated is directly proportional to the square of current ($H \propto I^2$). If you double the current from $1\text{A}$ to $2\text{A}$, heat generation quadruples ($2^2 = 4\times$)!</li>
  <li><strong>Electrical Resistance ($R$):</strong> Heat generated is directly proportional to the resistance of the conductor ($H \propto R$). Higher resistance produces proportionally more heat.</li>
  <li><strong>Duration of Flow ($t$):</strong> Heat generated is directly proportional to the time period during which current flows ($H \propto t$). Leaving an appliance ON longer accumulates more thermal energy.</li>
</ol>

<h4>Wire Dimensions & Resistance</h4>
<ul>
  <li><strong>Length:</strong> Longer wire = greater resistance ($R \propto L$).</li>
  <li><strong>Thickness:</strong> Thinner wire = higher resistance ($R \propto 1/A$). Therefore, a <em>long and thin wire</em> produces far more heat than a short, thick wire of the same material!</li>
</ul>

<h4>The Incandescent Bulb Filament</h4>
<p>An incandescent light bulb contains an ultra-thin, tightly coiled <strong>tungsten filament</strong>. Tungsten has the highest melting point of any metal ($3,422^\circ\text{C}$). The current heats the tungsten filament to over $2,500^\circ\text{C}$, making it glow <strong>white-hot</strong>, radiating both heat and visible light! The bulb is filled with chemically inactive argon or nitrogen gas to prevent tungsten from evaporating or burning.</p>
""",
        "vocabulary": [
            {"word": "Joule's Law of Heating", "definition": "A physical law stating that heat generated is proportional to the square of current, resistance, and time ($H = I^2 R t$)."},
            {"word": "Tungsten Filament", "definition": "An ultra-thin coiled wire with an extraordinarily high melting point ($3,422^\\circ\\text{C}$) that glows white-hot in incandescent bulbs."},
            {"word": "Inert Gas Filling", "definition": "Non-reactive gases (like argon and nitrogen) sealed inside a lightbulb to prevent the hot filament from oxidizing."},
            {"word": "Cross-Sectional Area", "definition": "The thickness of a wire; thinner wires offer greater resistance to current flow."}
        ],
        "sim_id": "joule_heating_sim",
        "checkpoints": [
            {
                "question": "According to Joule's Law ($H = I^2 R t$), what happens to heat production if the current through a fixed resistor is doubled?",
                "options": [
                    "Heat production remains unchanged",
                    "Heat production doubles ($2\\times$)",
                    "Heat production quadruples ($4\\times$)",
                    "Heat production decreases by half"
                ],
                "correct": 2,
                "explanation": "Heat depends on current squared ($I^2$). Doubling current ($2^2 = 4$) quadruples heat generation.",
                "solution": "Formula: $H \\propto I^2$. If $I \\rightarrow 2I$, then $H' = (2I)^2 = 4I^2 = 4H$."
            },
            {
                "question": "Why is tungsten metal used specifically for the filament of incandescent light bulbs?",
                "options": [
                    "It has an extraordinarily high melting point ($3,422^\\circ\\text{C}$) and glows white-hot without melting",
                    "It is the best conductor of electricity among all elements",
                    "It is transparent to visible light",
                    "It turns into liquid mercury when heated"
                ],
                "correct": 0,
                "explanation": "Tungsten's unmatched melting point ($3,422^\\circ\\text{C}$) enables it to reach white-hot incandescence ($>2500^\\circ\\text{C}$) safely inside an inert gas bulb.",
                "solution": "Filament requirement: Must emit visible light at white heat without melting. Tungsten has melting point $3,422^\\circ\\text{C}$."
            }
        ]
    },

    # SLIDE 10
    {
        "id": 10,
        "title": "Domestic Appliances & Fuses",
        "tag": "Household Heating • Circuit Protection",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "From your morning electric kettle to the clothes iron, heating elements make life comfortable. But what protects your home if a power surge strikes? An electric fuse—the ultimate sacrificial safety guard! Let's examine how it works.",
        "theory": r"""
<h3>Everyday Heating Appliances</h3>
<p>Many household conveniences rely directly on the heating effect of electric current. Inside each appliance is an insulated nichrome heating element:</p>
<ul>
  <li><strong>Electric Iron:</strong> The heating element is sandwiched between mica insulating sheets and a heavy, smooth polished metal base plate.</li>
  <li><strong>Electric Geyser & Immersion Rod:</strong> The nichrome coil is sealed inside a watertight copper or stainless-steel tube surrounded by magnesium oxide insulation.</li>
  <li><strong>Electric Room Heater:</strong> Nichrome coils wound on ceramic rods glow red-hot, radiating infrared thermal waves.</li>
  <li><strong>Electric Kettle & Toaster:</strong> Nichrome ribbons heat water or toast bread slices directly.</li>
</ul>

<h3>The Electric Fuse: Sacrificial Guardian</h3>
<p>Electrical circuits are designed to carry a maximum safe current limit (e.g., $5\text{A}$ for lights, $15\text{A}$ for heavy heaters). If overloading or a short-circuit occurs, an excessive surge of current rushes through the wiring, generating dangerous heat ($H = I^2 R t$) that can melt insulation and ignite house fires!</p>

<h4>How an Electric Fuse Operates</h4>
<ul>
  <li><strong>Composition:</strong> A short piece of thin wire made from an alloy of <strong>tin and lead</strong> (or copper-tin alloy) with a <strong>low melting point</strong>.</li>
  <li><strong>Series Connection:</strong> The fuse is always connected in <strong>series</strong> with the live wire entering the circuit.</li>
  <li><strong>Tripping Action:</strong> Under normal current, the fuse stays intact. When an unsafe current surge exceeds its rated threshold (e.g., $10\text{A}$), the excessive Joule heat causes the fuse wire to <strong>melt and vaporize instantly</strong>, breaking the open circuit and stopping current before wires catch fire!</li>
</ul>
""",
        "vocabulary": [
            {"word": "Electric Fuse", "definition": "A safety device containing a low-melting-point wire that melts to break an overloaded circuit, preventing electrical fires."},
            {"word": "Fuse Rating", "definition": "The maximum electric current (e.g., $5\\text{A}$, $15\\text{A}$) that a fuse wire can safely carry continuously without melting."},
            {"word": "Short Circuit", "definition": "An accidental direct contact between live and neutral wires with near-zero resistance, resulting in an enormous dangerous current surge."},
            {"word": "Overloading", "definition": "Connecting too many heavy electrical appliances to a single socket simultaneously, exceeding the circuit's safe current capacity."}
        ],
        "sim_id": "appliance_fuse_sim",
        "checkpoints": [
            {
                "question": "What is the primary function of an electric fuse in a household electrical circuit?",
                "options": [
                    "To increase the voltage of the incoming electricity",
                    "To melt and break the circuit when current exceeds a safe limit, preventing fires",
                    "To store backup electricity for power cuts",
                    "To cool down the heating element of the electric iron"
                ],
                "correct": 1,
                "explanation": "A fuse is a safety device designed with a low melting point so it melts and opens the circuit during dangerous current overloads.",
                "solution": "Excess current $\\rightarrow$ excessive Joule heat ($H = I^2 R t$) $\\rightarrow$ fuse wire melts $\\rightarrow$ circuit breaks $\\rightarrow$ fire prevented."
            },
            {
                "question": "Why should you NEVER replace a blown fuse wire with a thick iron nail or thick copper cable?",
                "options": [
                    "Because thick wire has a high melting point and will not melt during a current surge, risking a house fire",
                    "Because iron does not conduct any electricity",
                    "Because copper will attract lightning strikes into the house",
                    "Because thick wire will cause the lightbulbs to turn purple"
                ],
                "correct": 0,
                "explanation": "A thick copper wire has a very high melting point and will not melt during an overload. The house wiring inside walls will melt and catch fire instead!",
                "solution": "Safety rule: Fuses require calibrated low-melting alloy wires. A thick copper wire bypasses the safety mechanism completely."
            }
        ]
    },

    # SLIDE 11
    {
        "id": 11,
        "title": "Electric Furnaces & Safety",
        "tag": "Industrial Metallurgy • Electrical Hazards",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "The heating effect isn't just for boiling water—it can melt tons of solid steel! Industrial electric arc furnaces generate temperatures exceeding 3,000°C to recycle scrap steel. But improper wiring at home brings severe fire hazards. Let's study both.",
        "theory": r"""
<h3>Industrial Scale: Electric Arc Furnaces</h3>
<p>In modern steelmaking and circular recycling, <strong>Electric Arc Furnaces (EAF)</strong> have replaced coal blast furnaces. They utilize the extreme heating effect of electric currents to melt recycled scrap steel:</p>
<ul>
  <li><strong>Gigantic Graphite Electrodes:</strong> Massive carbon-graphite electrodes are lowered into tons of scrap iron and steel.</li>
  <li><strong>Electric Arc Generation:</strong> Hundreds of thousands of Amperes pass through the electrodes, striking an electric plasma arc with the scrap steel.</li>
  <li><strong>Extreme Temperatures:</strong> The electrical resistance of the arc generates temperatures exceeding <strong>$3,000^\circ\text{C}$</strong>, melting 100 tons of solid steel into glowing orange liquid metal in under an hour!</li>
  <li><strong>Green Recycling:</strong> Electric arc furnaces produce 75% fewer greenhouse emissions than traditional coal-fired blast furnaces.</li>
</ul>

<h3>Electrical Safety & Wiring Hazards</h3>
<p>While the heating effect powers modern industry, uncontrolled electrical heating poses major domestic hazards:</p>
<ol>
  <li><strong>Improper Wire Gauge:</strong> Using thin wires for high-power loads (like air conditioners or geysers) creates excessive resistance, causing wires inside walls to overheat.</li>
  <li><strong>Insulation Melting:</strong> Prolonged overheating melts polyvinyl chloride (PVC) wire insulation, exposing live conductors.</li>
  <li><strong>Electrical Fires:</strong> Sparks from melted wires ignite dry wooden framing and wall insulation. Modern installations use <strong>Miniature Circuit Breakers (MCBs)</strong> that automatically trip switch levers magnetically and thermally during overloads.</li>
</ol>
""",
        "vocabulary": [
            {"word": "Electric Arc Furnace", "definition": "A heavy industrial furnace that melts scrap steel using intense heat generated by high-current electric arcs."},
            {"word": "Plasma Arc", "definition": "An intensely hot, luminous electrical discharge formed when current ionizes the air or gas gap between electrodes."},
            {"word": "Wire Gauge", "definition": "The standardized measurement of wire thickness; thicker gauges are required for heavy-current appliances."},
            {"word": "MCB", "definition": "Miniature Circuit Breaker; a reusable automatic electromagnetic switch that trips open during current overloads."}
        ],
        "sim_id": "arc_furnace_safety_sim",
        "checkpoints": [
            {
                "question": "What key environmental and economic advantage do electric arc furnaces offer in steel manufacturing?",
                "options": [
                    "They can efficiently melt and recycle scrap steel with significantly lower emissions than coal blast furnaces",
                    "They operate without any electrical power",
                    "They turn steel directly into gold",
                    "They freeze molten iron into liquid nitrogen"
                ],
                "correct": 0,
                "explanation": "Electric arc furnaces recycle scrap steel using electric energy, drastically reducing carbon emissions compared to mining raw iron ore with coal.",
                "solution": "Electric Arc Furnaces recycle scrap metal with clean high-temperature plasma arcs, lowering emissions by up to 75%."
            },
            {
                "question": "What is the primary danger of connecting a heavy 15-Ampere room heater through a thin, low-rated extension cord?",
                "options": [
                    "The extension cord's high resistance generates excessive heat, melting plastic insulation and risking a fire",
                    "The room heater will generate cold air instead of warm air",
                    "The electric current will reverse and drain the power station",
                    "The copper inside the wire will evaporate into water"
                ],
                "correct": 0,
                "explanation": "High current through an undersized, thin cord creates extreme Joule heating ($H = I^2 R t$), melting insulation and causing short circuits or fires.",
                "solution": "Thin cord = high resistance $R$. Combined with high current $I = 15\\text{A}$, Joule heating $I^2 R t$ causes dangerous overheating."
            }
        ]
    },

    # SLIDE 12
    {
        "id": 12,
        "title": "Voltaic Cell & Galvani",
        "tag": "Chemical Generation • The Historic Feud",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Where does steady electric current come from when there are no wall outlets? The story begins with a fierce scientific dispute between Luigi Galvani and Alessandro Volta over a twitching frog's leg! Let's explore the birth of the first electric battery.",
        "theory": r"""
<h3>The Great Debate: Animal Tissue vs. Chemical Metals</h3>
<p>In the late 1700s, Italian physician <strong>Luigi Galvani</strong> made an accidental observation: when he touched a dissected frog's leg nerves with two different metals (brass and iron), the leg twitched violently! Galvani concluded that electricity was generated internally by animal tissue, coining the term <strong>'Animal Electricity'</strong>.</p>

<p>However, fellow Italian physicist <strong>Alessandro Volta</strong> disagreed. Volta hypothesized that the frog's moist leg was simply acting as a passive conductor (an electrolyte), and that <strong>electricity was generated by chemical reactions between two dissimilar metals</strong>!</p>

<h3>Alessandro Volta's Triumph: The Voltaic Pile (1800)</h3>
<p>To prove his hypothesis beyond doubt, Volta constructed an apparatus completely without animal tissue in 1800:</p>
<ul>
  <li><strong>Dissimilar Metals:</strong> He alternated disks of <strong>Zinc (Zn)</strong> and <strong>Copper (Cu)</strong>.</li>
  <li><strong>Electrolyte Moistened Disks:</strong> Between each metal pair, he placed pieces of cardboard or cloth soaked in brine (salt water) or dilute sulfuric acid.</li>
  <li><strong>Continuous Current:</strong> When the top and bottom metal terminals were connected with a wire, a steady, continuous electric current flowed! This was the <strong>Voltaic Pile—the world's first chemical electric battery</strong>.</li>
</ul>

<h4>How a Simple Voltaic Cell Works</h4>
<p>A simple Voltaic cell consists of two different metal plates called <strong>electrodes</strong> dipped into a conductive liquid called an <strong>electrolyte</strong>. Chemical oxidation at the Zinc electrode releases electrons, while reduction at the Copper electrode accepts electrons, driving electric current through the external circuit!</p>
""",
        "vocabulary": [
            {"word": "Voltaic Cell", "definition": "An electrochemical cell that converts chemical energy directly into electrical energy through spontaneous redox reactions."},
            {"word": "Electrode", "definition": "A solid electrical conductor (metal plate or carbon rod) through which electric charges enter or leave an electrolyte."},
            {"word": "Electrolyte", "definition": "A liquid or moist paste containing free mobile ions that conducts electric current through chemical movement."},
            {"word": "Animal Electricity", "definition": "Luigi Galvani's mistaken hypothesis that living animal tissues generate their own intrinsic electrical fluids."}
        ],
        "sim_id": "galvani_volta_sim",
        "checkpoints": [
            {
                "question": "What did Alessandro Volta prove regarding the twitching frog legs in Galvani's experiment?",
                "options": [
                    "Electricity was generated chemically between two dissimilar metals in contact with a moist electrolyte, not by the animal tissue",
                    "Frogs generate lightning bolts inside their muscles",
                    "Electricity cannot flow through liquids",
                    "Metals only conduct heat, never electricity"
                ],
                "correct": 0,
                "explanation": "Volta showed that dissimilar metals (like zinc and copper) separated by a moist conducting electrolyte produce chemical electricity.",
                "solution": "Volta replaced the frog with brine-soaked cardboard, proving electricity originates from chemical reactions between dissimilar metals."
            },
            {
                "question": "What essential components make up a basic Voltaic (Galvanic) cell?",
                "options": [
                    "Two identical pieces of plastic in dry air",
                    "Two dissimilar metal electrodes dipped in a conducting liquid electrolyte",
                    "A single bar magnet wrapped in paper",
                    "A piece of charcoal in pure oil"
                ],
                "correct": 1,
                "explanation": "A Voltaic cell requires two dissimilar metals (such as zinc and copper) with different chemical potentials dipped in an electrolyte.",
                "solution": "Basic requirements: Anode (oxidizable metal) + Cathode (reduction metal) + Ion-conducting electrolyte."
            }
        ]
    },

    # SLIDE 13
    {
        "id": 13,
        "title": "Lemon Cell Electrolyte",
        "tag": "Kitchen Science • Fruit Batteries",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Can you power a digital clock or an LED using a fresh lemon from your kitchen? Yes! The juicy lemon acts as a natural chemical electrolyte. Let's build and test a citrus Voltaic cell.",
        "theory": r"""
<h3>The Science of a Citrus Battery</h3>
<p>You can construct a working Voltaic cell using common household items: a fresh, juicy lemon, a copper wire or coin, and a galvanized iron nail (coated with zinc).</p>

<h4>How to Assemble the Lemon Cell</h4>
<ol>
  <li><strong>Roll the Lemon:</strong> Gently press and roll the lemon on a table to rupture internal pulp sacs, freeing citric acid juice inside.</li>
  <li><strong>Insert Electrodes:</strong> Push a clean <strong>copper coin or strip</strong> into one side, and a <strong>galvanized zinc nail</strong> into the other side (separated by about 2 cm, without touching inside).</li>
  <li><strong>Connect Meter:</strong> Connect wires from the copper strip and zinc nail to a sensitive digital multimeter or a low-voltage LED. The meter instantly registers approximately <strong>$0.9\text{ V}$ to $1.0\text{ V}$</strong>!</li>
</ol>

<h4>Chemical Reactions Inside the Lemon</h4>
<ul>
  <li><strong>The Electrolyte:</strong> Lemon juice contains <strong>citric acid ($\text{C}_6\text{H}_8\text{O}_7$)</strong> dissolved in water, providing mobile positive hydrogen ions ($\text{H}^+$).</li>
  <li><strong>Negative Terminal (Zinc Anode):</strong> Zinc is chemically more reactive than copper. Zinc atoms lose two electrons and dissolve into the acid:
    $$\text{Zn} \rightarrow \text{Zn}^{2+} + 2e^-$$
    These accumulated electrons make the zinc nail the negative ($-$) terminal.</li>
  <li><strong>Positive Terminal (Copper Cathode):</strong> Electrons travel through the external wire to the copper strip, where hydrogen ions from the lemon juice pick them up:
    $$2\text{H}^+ + 2e^- \rightarrow \text{H}_2 \uparrow$$
    The copper strip acts as the positive ($+$) terminal!</li>
</ul>
<p>Connecting 3 or 4 lemon cells in <strong>series</strong> (zinc of one to copper of the next) adds their voltages ($3 \times 0.9\text{V} \approx 2.7\text{V}$), brightly lighting a red LED!</p>
""",
        "vocabulary": [
            {"word": "Citric Acid", "definition": "A weak organic acid ($\text{C}_6\text{H}_8\text{O}_7$) present in citrus fruits that dissociates into hydrogen ions, acting as an electrolyte."},
            {"word": "Anode", "definition": "The electrode where oxidation (loss of electrons) occurs; in a Voltaic cell, this is the negative terminal (Zinc)."},
            {"word": "Cathode", "definition": "The electrode where reduction (gain of electrons) occurs; in a Voltaic cell, this is the positive terminal (Copper)."},
            {"word": "Series Battery", "definition": "Connecting multiple cells end-to-end (positive to negative) so their individual voltages add together."}
        ],
        "sim_id": "lemon_cell_sim",
        "checkpoints": [
            {
                "question": "In a lemon battery using a copper strip and a galvanized zinc nail, which electrode acts as the negative terminal where electrons are released?",
                "options": [
                    "The copper strip",
                    "The zinc nail",
                    "The yellow lemon skin",
                    "The multimeter dial"
                ],
                "correct": 1,
                "explanation": "Zinc is more reactive and oxidizes ($\text{Zn} \rightarrow \text{Zn}^{2+} + 2e^-$), releasing electrons that make it the negative terminal (anode).",
                "solution": "Zinc oxidizes and donates electrons to the external circuit, making the zinc nail the negative electrode."
            },
            {
                "question": "If one lemon cell produces roughly $0.9\text{ V}$, how can you power a $2.7\text{ V}$ LED bulb?",
                "options": [
                    "Connect 3 lemon cells in series (positive to negative)",
                    "Freeze the lemon in liquid nitrogen",
                    "Peel the lemon skin off",
                    "Connect 3 lemon cells in parallel"
                ],
                "correct": 0,
                "explanation": "Connecting cells in series adds their voltages: $0.9\text{ V} + 0.9\text{ V} + 0.9\text{ V} = 2.7\text{ V}$, providing sufficient voltage to light the LED.",
                "solution": "Series combination formula: $V_{\\text{total}} = V_1 + V_2 + V_3 = 0.9 + 0.9 + 0.9 = 2.7\\text{ V}$."
            }
        ]
    },

    # SLIDE 14
    {
        "id": 14,
        "title": "Dry Cell Architecture",
        "tag": "Portable Power • Zinc-Carbon Anatomy",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Liquid acid in Voltaic cells spills easily and is dangerous to carry around. That's why German inventor Carl Gassner perfected the dry cell in 1886, replacing liquid acid with a moist chemical paste! Let's examine a cutaway dry cell.",
        "theory": r"""
<h3>The Portable Revolution: Dry Cells</h3>
<p>A standard AA, AAA, C, or D flashlight battery is scientifically known as a <strong>Dry Cell</strong> (specifically a Leclanché-Gassner zinc-carbon cell). It isn't actually bone-dry—it contains a moist chemical paste that provides mobile ions without spilling!</p>

<h4>Anatomy of a Zinc-Carbon Dry Cell</h4>
<ol>
  <li><strong>Zinc Outer Can (Negative Terminal $-$):</strong> The outer cylindrical casing is made of metallic zinc. It serves a double purpose: as the structural container and as the oxidizable anode ($\text{Zn} \rightarrow \text{Zn}^{2+} + 2e^-$). The flat bottom acts as the negative terminal.</li>
  <li><strong>Carbon (Graphite) Rod (Positive Terminal $+$):</strong> A central graphite rod runs down the middle of the cell, capped with a shiny metal top. Carbon is chemically inert and serves as a conductor to collect electrons, acting as the positive terminal.</li>
  <li><strong>Depolarizer ($\text{MnO}_2$):</strong> The carbon rod is surrounded by a dense black mixture of <strong>Manganese Dioxide ($\text{MnO}_2$)</strong> and powdered carbon. $\text{MnO}_2$ acts as a chemical depolarizer—it oxidizes hydrogen gas bubbles into water, preventing insulating gas bubbles from choking the cell!</li>
  <li><strong>Moist Paste Electrolyte:</strong> A moist chemical paste of <strong>Ammonium Chloride ($\text{NH}_4\text{Cl}$)</strong> and <strong>Zinc Chloride ($\text{ZnCl}_2$)</strong> fills the space between the zinc can and the manganese dioxide layer.</li>
  <li><strong>Porous Separator:</strong> A porous paper or cardboard lining prevents direct contact between the zinc container and the black mixture while permitting ions to migrate freely.</li>
</ol>
<p>A fresh single dry cell generates a standard potential difference of <strong>$1.5\text{ Volts}$</strong>.</p>
""",
        "vocabulary": [
            {"word": "Dry Cell", "definition": "A portable electrochemical cell with a moist paste electrolyte immobilized inside a sealed container, preventing liquid spillage."},
            {"word": "Zinc Canister", "definition": "The outer zinc metal casing that acts both as the physical container and as the negative anode terminal."},
            {"word": "Carbon Rod", "definition": "The central inert graphite rod with a metal cap that functions as the positive cathode terminal to collect electrons."},
            {"word": "Depolarizer", "definition": "A substance like manganese dioxide ($\text{MnO}_2$) that prevents hydrogen gas accumulation on the positive electrode."}
        ],
        "sim_id": "dry_cell_cutaway_sim",
        "checkpoints": [
            {
                "question": "Which component of a standard dry cell acts as the negative terminal (anode)?",
                "options": [
                    "The central carbon graphite rod",
                    "The outer zinc metal container",
                    "The brass metal top cap",
                    "The plastic outer decorative label"
                ],
                "correct": 1,
                "explanation": "The outer zinc container oxidizes and releases electrons, acting as the negative terminal (flat bottom).",
                "solution": "Zinc acts as the anode: $\\text{Zn} \\rightarrow \\text{Zn}^{2+} + 2e^-$, making the bottom zinc plate the negative terminal."
            },
            {
                "question": "Why is manganese dioxide ($\text{MnO}_2$) packed around the carbon rod inside a dry cell?",
                "options": [
                    "To act as a depolarizer that prevents insulating hydrogen gas bubbles from collecting on the rod",
                    "To make the dry cell glow in the dark",
                    "To keep the carbon rod cold",
                    "To convert the cell into a permanent magnet"
                ],
                "correct": 0,
                "explanation": "Manganese dioxide oxidizes hydrogen gas into water, preventing hydrogen bubbles from insulating the carbon cathode and halting current.",
                "solution": "Depolarization role: Removes $H_2$ gas bubbles via reaction $\\text{H}_2 + 2\\text{MnO}_2 \\rightarrow \\text{Mn}_2\\text{O}_3 + \\text{H}_2\\text{O}$."
            }
        ]
    },

    # SLIDE 15
    {
        "id": 15,
        "title": "Rechargeable & Li-Ion Cells",
        "tag": "Modern Energy • Lithium-Ion Chemistry",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Single-use dry cells die once their chemicals are consumed. But rechargeable batteries can be restored thousands of times! Lithium-ion batteries power your smartphone, laptop, and modern electric cars. Let's see how they work.",
        "theory": r"""
<h3>Primary vs. Secondary Cells</h3>
<ul>
  <li><strong>Primary Cells (Non-Rechargeable):</strong> Single-use cells (like alkaline and zinc-carbon dry cells). The chemical reactions are irreversible. Once the zinc is consumed, the cell is exhausted and must be discarded.</li>
  <li><strong>Secondary Cells (Rechargeable Batteries):</strong> Cells where the chemical redox reactions are <strong>electrically reversible</strong>. By passing electric current through the battery in the opposite direction from a charger, the original chemical reactants are restored!</li>
</ul>

<h3>The Lithium-Ion (Li-Ion) Revolution</h3>
<p>Awarded the Nobel Prize in Chemistry in 2019, <strong>Lithium-ion batteries</strong> have transformed portable electronics and green transportation.</p>

<h4>Why Lithium?</h4>
<ul>
  <li><strong>Lightest Metal:</strong> Lithium has an atomic number of 3, making it the lightest of all solid elements.</li>
  <li><strong>High Electrochemical Potential:</strong> Delivers high cell voltages (typically <strong>$3.7\text{ V}$ to $4.2\text{ V}$</strong> per cell compared to only $1.5\text{V}$ for dry cells).</li>
  <li><strong>High Energy Density:</strong> Packs massive amounts of energy into compact, lightweight packages.</li>
</ul>

<h4>The 'Rocking Chair' Mechanism</h4>
<ul>
  <li><strong>Discharging (Powering Phone):</strong> $\text{Li}^+$ ions shuttle from the graphite anode through the liquid electrolyte to the lithium cobalt oxide cathode, releasing electrons through your phone's processor.</li>
  <li><strong>Charging (Plugged into Wall):</strong> The charger forces electrons and $\text{Li}^+$ ions to migrate in reverse, embedding back into the graphite lattice.</li>
</ul>

<h4>Critical Challenges</h4>
<p>Lithium-ion cells rely on scarce critical minerals (<strong>lithium</strong> and <strong>cobalt</strong>). Liquid organic electrolytes are flammable, posing risks of <em>thermal runaway</em> (fire) if punctured or overcharged.</p>
""",
        "vocabulary": [
            {"word": "Secondary Cell", "definition": "A rechargeable electrochemical battery whose chemical reactions can be reversed repeatedly by applying external electrical energy."},
            {"word": "Lithium-Ion Battery", "definition": "A high-energy-density rechargeable battery where lithium ions shuttle between positive and negative electrodes."},
            {"word": "Energy Density", "definition": "The amount of electrical energy stored per unit weight or volume of a battery."},
            {"word": "Thermal Runaway", "definition": "An uncontrolled chain reaction where internal short circuits or overheating cause a battery to rapidly catch fire."}
        ],
        "sim_id": "lithium_ion_sim",
        "checkpoints": [
            {
                "question": "What fundamental feature distinguishes a secondary cell (rechargeable battery) from a primary cell?",
                "options": [
                    "A secondary cell's chemical reactions can be reversed by forcing electric current through it in the opposite direction",
                    "A secondary cell is made completely of wood",
                    "A secondary cell produces direct alternating current",
                    "A primary cell can be recharged unlimited times"
                ],
                "correct": 0,
                "explanation": "Secondary cells feature reversible electrochemical reactions, allowing recharging by reversing current flow with an external charger.",
                "solution": "Rechargeability: Secondary cell reactions are reversible: Reactants $\\rightleftharpoons$ Products."
            },
            {
                "question": "Why are lithium-ion batteries preferred for smartphones, laptops, and electric vehicles over lead-acid car batteries?",
                "options": [
                    "They are much heavier and bulkier",
                    "They offer exceptionally high energy density in a lightweight, compact package",
                    "They run entirely without any chemical reactions",
                    "They only work when submerged in water"
                ],
                "correct": 1,
                "explanation": "Lithium is the lightest metal and provides high voltage ($3.7\\text{ V}$), giving Li-ion batteries high energy density for portable devices.",
                "solution": "Advantage: High energy density + light weight + high operating voltage ($3.7\\text{V}$ vs $1.5\\text{V}$)."
            }
        ]
    },

    # SLIDE 16
    {
        "id": 16,
        "title": "Solid-State & E-Waste Recycling",
        "tag": "Future Batteries • Environmental Duty",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "What is the future of energy storage? Solid-state batteries promise ultra-fast charging and zero fire risks! But what happens when batteries die? Disposing them in trash cans poisons soil and water. Let's explore solid-state tech and e-waste recycling.",
        "theory": r"""
<h3>The Frontier: Solid-State Batteries</h3>
<p>To overcome the fire risks and capacity limits of current lithium-ion batteries, scientists are developing <strong>Solid-State Batteries</strong>:</p>
<ul>
  <li><strong>Solid Electrolyte:</strong> Replaces flammable liquid/gel electrolytes with a solid ceramic, glass, or solid polymer electrolyte.</li>
  <li><strong>Non-Flammable & Safe:</strong> Cannot leak, catch fire, or undergo thermal runaway, even when damaged or punctured.</li>
  <li><strong>Ultra-Fast Charging:</strong> Allows ions to shuttle rapidly, charging electric vehicles in under 10 to 15 minutes.</li>
  <li><strong>Longer Lifespan:</strong> Retains capacity over thousands of cycles with minimal degradation.</li>
</ul>

<h3>Environmental Responsibility & E-Waste Hazards</h3>
<p>Every year, billions of spent household and smartphone batteries are discarded. Tossing batteries into ordinary household trash cans causes severe ecological devastation:</p>

<h4>Toxic Heavy Metals in Batteries</h4>
<ul>
  <li><strong>Lead ($\text{Pb}$) & Cadmium ($\text{Cd}$):</strong> Extremely toxic neurotoxins found in lead-acid and Ni-Cd batteries that cause kidney and brain damage.</li>
  <li><strong>Lithium ($\text{Li}$) & Cobalt ($\text{Co}$):</strong> Flammable and toxic; landfill pressure can rupture them, sparking stubborn chemical landfill fires that release toxic plumes.</li>
  <li><strong>Corrosive Acids & Alkalis:</strong> Leak from decaying battery casings into surrounding soil, percolating into municipal groundwater reserves and contaminating drinking water.</li>
</ul>

<h4>The Solution: Dedicated E-Waste Recycling</h4>
<p>Spent batteries must always be deposited at certified <strong>E-Waste Collection Centers</strong>. Modern recycling facilities crush spent batteries under inert gas, neutralizing acids and recovering up to <strong>95% of purified lithium, cobalt, nickel, and copper</strong> to manufacture new green batteries!</p>
""",
        "vocabulary": [
            {"word": "Solid-State Battery", "definition": "A next-generation battery utilizing a solid ceramic or polymer electrolyte instead of flammable liquid chemicals."},
            {"word": "E-Waste", "definition": "Electronic waste comprising discarded electrical appliances, circuitry, and spent chemical batteries."},
            {"word": "Heavy Metal Leaching", "definition": "The harmful percolation of toxic metals (lead, cadmium, mercury) from decaying landfill batteries into soil and groundwater."},
            {"word": "Closed-Loop Recycling", "definition": "Recovering purified raw elements (lithium, cobalt, copper) from spent batteries to manufacture new batteries."}
        ],
        "sim_id": "solid_state_ewaste_sim",
        "checkpoints": [
            {
                "question": "What is the primary safety advantage of solid-state batteries over conventional lithium-ion batteries?",
                "options": [
                    "They replace flammable liquid electrolytes with solid non-flammable ceramics, eliminating fire and explosion risks",
                    "They do not contain any atoms",
                    "They can only be used once and must be thrown away",
                    "They only operate at freezing temperatures"
                ],
                "correct": 0,
                "explanation": "Solid-state batteries replace volatile liquid electrolytes with non-flammable solid ceramic or polymer layers, eliminating thermal runaway fires.",
                "solution": "Safety breakthrough: Solid electrolyte = non-flammable, non-leaking, high thermal stability."
            },
            {
                "question": "Why should discarded batteries NEVER be thrown into ordinary household trash destined for landfills?",
                "options": [
                    "They leak toxic heavy metals (lead, cadmium, lithium) that contaminate soil, groundwater, and ignite landfill fires",
                    "They will turn into living frogs in the garbage truck",
                    "They make household trash too magnetic to pick up",
                    "They absorb all sunlight falling on the landfill"
                ],
                "correct": 0,
                "explanation": "Decaying batteries leach toxic heavy metals and corrosive acids into groundwater and cause spontaneous chemical fires in landfills.",
                "solution": "Environmental hazard: Heavy metal leaching (Pb, Cd, Li) poisons ecosystems. Solution: Deposit at authorized e-waste recycling centers."
            }
        ]
    },

    # SLIDE 17 - MASTERY CHALLENGE PART I (Q1-Q10)
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "tag": "Comprehensive Review • Questions 1 to 10",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Outstanding work completing the first half of the curriculum! Now it's time to test your mastery. Tackle these 10 in-depth conceptual questions, and click the solution button to review the complete step-by-step scientific breakdown for each!",
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10
    },

    # SLIDE 18 - MASTERY CHALLENGE PART II (Q11-Q20)
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "tag": "Comprehensive Review • Questions 11 to 20",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "You're powering through brilliantly! Part II focuses on electromagnet strength, scrap yard crane mechanics, and Earth's geodynamo shield. Read each question carefully and analyze the physical principles.",
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10
    },

    # SLIDE 19 - MASTERY CHALLENGE PART III (Q21-Q30)
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "tag": "Comprehensive Review • Questions 21 to 30",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "Welcome to Part III! Here we dive deep into Joule's heating effect ($H = I^2 R t$), nichrome heating elements, safety fuses, and industrial electric arc furnaces. Challenge your understanding!",
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10
    },

    # SLIDE 20 - MASTERY CHALLENGE PART IV (Q31-Q40)
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "tag": "Comprehensive Review • Questions 31 to 40",
        "badge": "Class 8 Science • Chapter 4",
        "avatar_dialogue": "The final frontier! Part IV tests your knowledge of Voltaic cells, dry cell architecture, lithium-ion mechanics, solid-state batteries, and e-waste stewardship. Finish strong and achieve complete mastery!",
        "is_quiz_slide": True,
        "quiz_start_idx": 31,
        "quiz_count": 10
    }
]

# 40 MASTERY CHALLENGE QUESTIONS WITH COMPLETE STEP-BY-STEP SOLUTIONS
QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "In Oersted's famous 1820 experiment, what physical evidence proved that an electric current produces a magnetic field?",
        "options": [
            "The wire became red-hot and melted immediately",
            "A magnetic compass needle placed near the wire deflected away from its North-South alignment when current flowed",
            "The wire attracted wooden toothpicks and paper scraps",
            "Small sparks leaped from the wire into the ceiling"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Background:</strong> Prior to 1820, electricity and magnetism were believed to be completely independent phenomena.</li>
  <li><strong>The Observation:</strong> Hans Christian Oersted placed a magnetic compass directly beneath an electric conducting wire aligned along the Earth's magnetic meridian.</li>
  <li><strong>Circuit Closed:</strong> The moment electric current was switched ON, the compass needle rotated sharply away from geographic North.</li>
  <li><strong>Circuit Opened:</strong> When current stopped, the compass returned instantly to its resting position.</li>
  <li><strong>Conclusion:</strong> Since only a magnetic field can exert torque on a magnetic compass needle, the electric current must have generated a magnetic field in the surrounding space.</li>
</ol>
"""
    },

    # Q2
    {
        "id": 2,
        "question": "What happens to the magnetic field around a conductor if the direction of electric current is reversed?",
        "options": [
            "The magnetic field disappears permanently",
            "The direction of the magnetic field lines reverses completely",
            "The field changes into an electrostatic field",
            "The strength of the magnetic field becomes infinitely large"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Right-Hand Thumb Rule:</strong> The direction of magnetic field lines depends strictly on the direction of conventional current flow.</li>
  <li><strong>Reversing Current:</strong> When the battery terminals are swapped, current flows in the opposite direction through the wire.</li>
  <li><strong>Field Reversal:</strong> Applying the Right-Hand Thumb Rule shows that the curled fingers now circulate in the opposite direction.</li>
  <li><strong>Compass Behavior:</strong> The compass needle deflects to the opposite side (e.g., from East deflection to West deflection).</li>
</ol>
"""
    },

    # Q3
    {
        "id": 3,
        "question": "What shape do the magnetic field lines take in a plane perpendicular to a long straight current-carrying wire?",
        "options": [
            "Concentric circles centered on the wire axis",
            "Straight lines radiating radially outward like spokes on a bicycle wheel",
            "Helical corkscrews expanding to infinity",
            "Square boxes surrounding the wire"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Experimental Demonstration:</strong> Pass a thick vertical copper wire through a horizontal sheet of white cardboard and sprinkle iron filings.</li>
  <li><strong>Tapping Cardboard:</strong> When current flows and the board is gently tapped, iron filings align along lines of magnetic force.</li>
  <li><strong>Pattern:</strong> The filings arrange themselves into concentric circles centered directly on the wire.</li>
  <li><strong>Density:</strong> The circles are packed closer together near the wire (where the magnetic field is strongest) and spread farther apart at greater distances.</li>
</ol>
"""
    },

    # Q4
    {
        "id": 4,
        "question": "Which of the following devices relies directly on the magnetic effect of electric current to function?",
        "options": [
            "Electric immersion water heater",
            "Electric toaster",
            "Electric bell and loudspeaker",
            "Incandescent filament light bulb"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Immersion heaters, toasters, and filament bulbs:</strong> All operate on the <em>heating effect</em> of electric current ($H = I^2 R t$), converting electrical energy into thermal energy.</li>
  <li><strong>Electric Bell & Loudspeaker:</strong> An electric bell uses an electromagnet to repeatedly pull an iron striker against a metal gong. A loudspeaker uses an electromagnet coil interacting with a permanent magnet to vibrate a speaker cone, producing sound waves.</li>
  <li><strong>Conclusion:</strong> Electric bells and loudspeakers rely directly on the magnetic effect of electric current.</li>
</ol>
"""
    },

    # Q5
    {
        "id": 5,
        "question": "Why is a solenoid with an iron core much stronger than an air-core solenoid carrying the same current?",
        "options": [
            "Iron adds its own electricity to the wire",
            "Soft iron has very high magnetic permeability, concentrating and multiplying the magnetic field lines",
            "Iron prevents the wire from getting hot",
            "Iron turns the current from DC into AC"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Magnetic Permeability ($\mu$):</strong> A measure of a material's ability to support the formation of a magnetic field within itself.</li>
  <li><strong>Ferromagnetic Core:</strong> Soft iron contains tiny magnetic domains. When placed inside the solenoid's magnetic field, these domains align in the same direction.</li>
  <li><strong>Field Multiplication:</strong> The combined magnetic field of the aligned iron domains adds to the solenoid's field, multiplying total magnetic flux density ($B$) by hundreds of times compared to empty air.</li>
</ol>
"""
    },

    # Q6
    {
        "id": 6,
        "question": "How can you determine which end of an energized solenoid behaves as a North magnetic pole?",
        "options": [
            "By checking which end is heavier",
            "Using the Clock Face Rule: if current flows counter-clockwise when viewed from that end, it is a North pole",
            "The end connected to the negative terminal is always North",
            "By measuring which end is warmer"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Clock Face Rule:</strong> Look directly at the circular face of one end of the coil.</li>
  <li><strong>Counter-Clockwise Flow:</strong> If electric current appears to circulate counter-clockwise, the letters 'N' can be drawn with arrows matching the current, indicating a <strong>North (N) pole</strong>.</li>
  <li><strong>Clockwise Flow:</strong> If current circulates clockwise, the letter 'S' can be drawn with arrows matching the current, indicating a <strong>South (S) pole</strong>.</li>
</ol>
"""
    },

    # Q7
    {
        "id": 7,
        "question": "A student winds 20 turns of wire around a nail and lifts 3 paper clips. If she rewinds it with 60 turns using the same battery, how many clips should it roughly lift?",
        "options": [
            "1 paper clip",
            "3 paper clips",
            "9 paper clips",
            "30 paper clips"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Proportionality:</strong> The magnetic field strength of an electromagnet is directly proportional to the number of turns ($B \propto N$) when current remains constant.</li>
  <li><strong>Ratio Calculation:</strong>
    $$\text{Ratio of turns} = \frac{N_2}{N_1} = \frac{60}{20} = 3$$
  </li>
  <li><strong>Lifting Capacity:</strong>
    $$\text{Expected clips lifted} = 3 \times 3 = 9\text{ paper clips}$$
  </li>
  <li>Tripling the turns roughly triples the magnetic lifting force.</li>
</ol>
"""
    },

    # Q8
    {
        "id": 8,
        "question": "What is the crucial operational advantage of an electromagnet over a permanent magnet in scrap yard cranes?",
        "options": [
            "Electromagnets are cheaper to manufacture",
            "Electromagnets can have their magnetism switched ON to grab iron scrap and switched OFF to instantly drop it",
            "Electromagnets never require any electrical power",
            "Electromagnets can attract plastic and rubber"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Permanent Magnets:</strong> Cannot be deactivated. If a crane picked up tons of steel scrap with a permanent magnet, there would be no simple way to pull the scrap off to release it into a truck!</li>
  <li><strong>Electromagnets:</strong> By simply opening the electrical circuit (current OFF), the magnetic field drops to zero instantly.</li>
  <li><strong>Result:</strong> The heavy scrap falls cleanly into the hopper by gravity, enabling rapid, automated sorting.</li>
</ol>
"""
    },

    # Q9
    {
        "id": 9,
        "question": "What generates Earth's geomagnetic field in its deep interior?",
        "options": [
            "A giant solid bar magnet trapped in the Earth's crust",
            "Convection currents of molten liquid iron and nickel circulating in Earth's outer core",
            "The rotation of the Moon pulling on ocean tides",
            "Underground volcanic magma exploding in caves"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Geodynamo Theory:</strong> Earth's outer core (approx. 2,900 to 5,150 km deep) consists of molten liquid iron and nickel, which are excellent electrical conductors.</li>
  <li><strong>Convection & Coriolis Forces:</strong> Heat escaping from the core drives convection currents, while Earth's rotation twists these flows into helical rolls.</li>
  <li><strong>Current Generation:</strong> Moving liquid metal creates massive circulating electric currents, which generate Earth's magnetic field.</li>
</ol>
"""
    },

    # Q10
    {
        "id": 10,
        "question": "How do migratory birds navigate thousands of kilometers across continents without GPS?",
        "options": [
            "They follow streetlights and highway signs",
            "They utilize magnetoreception, detecting Earth's magnetic field lines with biological magnetite in their bodies",
            "They smell the salt in ocean air",
            "They are blown purely randomly by high-altitude winds"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Magnetoreception:</strong> Many migratory animals (birds, sea turtles, monarch butterflies) possess specialized biological receptors containing microscopic magnetite ($\text{Fe}_3\text{O}_4$) crystals.</li>
  <li><strong>Magnetic Sensing:</strong> These sensors detect both the direction (inclination) and intensity of Earth's geomagnetic field.</li>
  <li><strong>Navigation:</strong> This internal biological compass provides reliable navigational orientation even on cloudy days and during night flights over open oceans.</li>
</ol>
"""
    },

    # Q11
    {
        "id": 11,
        "question": "What is the microscopic origin of the heating effect of electric current?",
        "options": [
            "Electrons burning up like tiny matches inside the wire",
            "Collisions between moving conduction electrons and the vibrating lattice ions of the metal conductor",
            "Air molecules rubbing vigorously against the plastic wire casing",
            "Atomic nuclei splitting in two inside the copper wire"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Electric Field:</strong> The voltage source accelerates free conduction electrons through the metal.</li>
  <li><strong>Inelastic Collisions:</strong> The drifting electrons collide frequently with the fixed positive metal ions forming the crystalline lattice.</li>
  <li><strong>Energy Transfer:</strong> Kinetic energy from electrons is transferred to the lattice ions, causing them to vibrate with greater amplitude.</li>
  <li><strong>Macroscopic Heat:</strong> Increased atomic lattice vibration corresponds directly to an increase in thermal energy (temperature).</li>
</ol>
"""
    },

    # Q12
    {
        "id": 12,
        "question": "Why does a nichrome heating element glow red-hot while the copper cord connecting it to the wall stays cool?",
        "options": [
            "Copper is insulated with rubber, which absorbs all heat",
            "Nichrome has approximately 60 times higher electrical resistance than copper, generating vastly more Joule heat for the same current",
            "Current only flows through the nichrome, not through the copper cord",
            "Copper creates a cold magnetic field"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Series Circuit:</strong> The copper cord and nichrome heating element carry the exact same current ($I$).</li>
  <li><strong>Joule's Law:</strong> Heat generated per second is $H/t = I^2 R$.</li>
  <li><strong>Resistance Comparison:</strong> Nichrome has roughly 60 times higher resistivity than copper ($R_{\\text{nichrome}} \\gg R_{\\text{copper}}$).</li>
  <li><strong>Outcome:</strong> Because $R_{\\text{copper}} \\approx 0$, very little heat is produced in the cord. In contrast, the high resistance of nichrome converts electrical energy into intense heat, making it glow orange-red.</li>
</ol>
"""
    },

    # Q13
    {
        "id": 13,
        "question": "According to Joule's Law ($H = I^2 R t$), how does the heat produced in a fixed resistor change if the current passing through it is tripled?",
        "options": [
            "Heat increases by 3 times",
            "Heat increases by 6 times",
            "Heat increases by 9 times ($3^2$)",
            "Heat decreases to one-third"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Joule's Law:</strong> $H = I^2 R t$, so heat $H$ is proportional to the square of current ($H \propto I^2$).</li>
  <li><strong>New Current:</strong> Let initial current be $I_1$ and new current be $I_2 = 3I_1$.</li>
  <li><strong>Calculation:</strong>
    $$H_2 \propto (3I_1)^2 = 9 I_1^2 = 9 H_1$$
  </li>
  <li>Tripling the current results in a <strong>9-fold increase</strong> in heat generation.</li>
</ol>
"""
    },

    # Q14
    {
        "id": 14,
        "question": "Between a short, thick wire and a long, thin wire of the same material, which will have higher resistance and generate more heat?",
        "options": [
            "The short, thick wire",
            "The long, thin wire",
            "Both will have identical resistance",
            "Neither wire will have any resistance"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Resistance Formula:</strong> $R = \rho \frac{L}{A}$, where $L$ is length and $A$ is cross-sectional area.</li>
  <li><strong>Length Effect:</strong> Longer length ($L$) means electrons encounter more lattice collisions ($R \propto L$).</li>
  <li><strong>Area Effect:</strong> Thinner wire (smaller $A$) restricts the pathway, increasing resistance ($R \propto 1/A$).</li>
  <li><strong>Conclusion:</strong> A long, thin wire maximizes resistance $R$, and by $H = I^2 R t$, it generates far more heat for a given current.</li>
</ol>
"""
    },

    # Q15
    {
        "id": 15,
        "question": "Why is tungsten metal used exclusively for incandescent light bulb filaments?",
        "options": [
            "Tungsten is a transparent metal that lets light shine through",
            r"Tungsten has an extraordinarily high melting point ($3,422^\circ\text{C}$), allowing it to glow white-hot without melting",
            "Tungsten is cheaper than iron and plastic",
            "Tungsten does not conduct any electric current"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Incandescence Principle:</strong> To emit bright visible white light, a filament must be heated to temperatures above $2,500^\circ\text{C}$.</li>
  <li><strong>Melting Point Requirement:</strong> Most common metals melt far below this temperature (copper melts at $1,085^\circ\text{C}$, iron at $1,538^\circ\text{C}$).</li>
  <li><strong>Tungsten Properties:</strong> Tungsten has the highest melting point of all metals ($3,422^\circ\text{C}$) and high tensile strength, enabling it to glow white-hot safely for thousands of hours.</li>
</ol>
"""
    },

    # Q16
    {
        "id": 16,
        "question": "Why are incandescent light bulbs filled with chemically inert argon or nitrogen gas rather than ordinary air?",
        "options": [
            "To prevent the white-hot tungsten filament from reacting with atmospheric oxygen and burning up",
            "To make the light bulb float in the air",
            "To cool the glass bulb down to freezing temperatures",
            "To absorb electric sparks from the socket"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Oxidation at High Temperatures:</strong> At temperatures above $2,000^\circ\text{C}$, tungsten reacts instantly and violently with oxygen in the air, vaporizing into tungsten oxide and snapping the filament.</li>
  <li><strong>Inert Atmosphere:</strong> Argon and nitrogen are chemically unreactive (inert). They do not react with hot tungsten.</li>
  <li><strong>Reducing Evaporation:</strong> Gas pressure also slows down the physical evaporation of tungsten atoms from the filament.</li>
</ol>
"""
    },

    # Q17
    {
        "id": 17,
        "question": "How is an electric safety fuse connected into a domestic household circuit?",
        "options": [
            "In parallel with the neutral wire",
            "In series with the live wire",
            "Directly connected to the water pipe earth",
            "Inside the lightbulb glass"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Series Connection:</strong> A fuse must be placed in <strong>series</strong> so that all current entering the circuit passes directly through the fuse wire.</li>
  <li><strong>Live Wire Placement:</strong> Connecting it to the live wire ensures that when the fuse blows, high voltage is completely disconnected from the appliances, preventing electrical shock.</li>
  <li>If connected in parallel, current would bypass the fuse, making it completely ineffective.</li>
</ol>
"""
    },

    # Q18
    {
        "id": 18,
        "question": "What happens when an electrical short circuit occurs in a home?",
        "options": [
            "Resistance becomes extremely low, causing an enormous current surge that generates dangerous heat",
            "The voltage drops to zero and appliances freeze",
            "The wires become permanent magnets and attract iron furniture",
            "Current flows backward into the power station"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Short Circuit Definition:</strong> An accidental direct contact between the live wire and neutral wire.</li>
  <li><strong>Ohm's Law:</strong> $I = V / R$. When resistance drops to near zero ($R \approx 0$), current $I$ surges to hundreds of Amperes.</li>
  <li><strong>Joule Heating:</strong> Since $H \propto I^2$, this massive current surge generates intense heat in milliseconds, melting wire insulation and igniting fires unless a fuse or MCB trips.</li>
</ol>
"""
    },

    # Q19
    {
        "id": 19,
        "question": "How does an industrial Electric Arc Furnace (EAF) melt scrap steel?",
        "options": [
            "By burning millions of tons of firewood inside a brick oven",
            r"By striking high-current electric plasma arcs between massive graphite electrodes and the steel scrap, generating over $3,000^\circ\text{C}$",
            "By using giant magnifying glasses to focus sunlight",
            "By spinning scrap steel rapidly until friction melts it"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Setup:</strong> Massive carbon-graphite electrodes are lowered into a refractory-lined furnace vessel filled with shredded steel scrap.</li>
  <li><strong>Arc Ignition:</strong> Heavy electric current passes through the electrodes, ionizing air/gas into an electric plasma arc.</li>
  <li><strong>Intense Heat:</strong> Resistance across the arc generates temperatures exceeding $3,000^\circ\text{C}$, rapidly liquefying steel scrap.</li>
  <li><strong>Eco-Friendly:</strong> Avoids coal combustion, drastically cutting greenhouse gas emissions.</li>
</ol>
"""
    },

    # Q20
    {
        "id": 20,
        "question": "What is the primary function of a Miniature Circuit Breaker (MCB) in modern electrical switchboards?",
        "options": [
            "It measures the total electricity bill in dollars",
            "It automatically trips open to break the circuit during overloads or short circuits, and can be easily reset with a switch",
            "It converts household AC electricity into solar energy",
            "It cools down hot appliance cords using internal fans"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Reusability:</strong> Unlike traditional fuses where melted wire must be physically replaced, an MCB is a reusable electromagnetic and bimetallic switch.</li>
  <li><strong>Overcurrent Protection:</strong> When excessive current flows, an internal electromagnet or heated bimetallic strip trips the mechanical latch.</li>
  <li><strong>Restoration:</strong> Once the fault is fixed, the user simply flips the lever back to the 'ON' position.</li>
</ol>
"""
    },

    # Q21
    {
        "id": 21,
        "question": "In Luigi Galvani's 1780s experiment, what caused the frog's leg to twitch?",
        "options": [
            "The frog was still alive and jumping",
            "Two dissimilar metals (brass and iron) formed an electrochemical circuit with the moist, salty fluid in the frog's leg",
            "Galvani was projecting static electricity from his eyes",
            "The frog's muscle contained a permanent magnet"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>The Setup:</strong> Galvani mounted a frog's leg on an iron trellis using a brass hook touching the spinal nerve.</li>
  <li><strong>Galvani's View:</strong> He believed the twitch came from intrinsic 'animal electricity' inside the frog's nerves.</li>
  <li><strong>Volta's Revelation:</strong> Alessandro Volta proved the twitch was caused by external current generated between the two dissimilar metals (brass and iron) using the frog's salty tissue fluid as an electrolyte.</li>
</ol>
"""
    },

    # Q22
    {
        "id": 22,
        "question": "What was the structure of Alessandro Volta's original 1800 'Voltaic Pile'?",
        "options": [
            "A glass jar filled with gasoline and iron nails",
            "Alternating discs of zinc and copper separated by cardboard soaked in saltwater (brine)",
            "A single giant block of solid gold connected to water pipes",
            "A coil of wire wrapped around a magnet"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Composition:</strong> Volta stacked pairs of dissimilar metal discs: <strong>Zinc</strong> (anode) and <strong>Copper</strong> (cathode).</li>
  <li><strong>Electrolyte Layer:</strong> Between each pair, he inserted a piece of cloth or cardboard soaked in brine (salt water) or dilute acid.</li>
  <li><strong>Multiplication:</strong> Stacking dozens of these pairs in series multiplied the overall voltage, producing the world's first continuous, reliable electric current without animal tissue.</li>
</ol>
"""
    },

    # Q23
    {
        "id": 23,
        "question": "What role does lemon juice play in an experimental citrus fruit battery?",
        "options": [
            "It acts as a mechanical glue holding the wires in place",
            "It acts as an electrolyte providing mobile hydrogen ions ($\text{H}^+$) to conduct chemical reactions",
            "It acts as an electrical insulator preventing current flow",
            "It provides yellow color to the electrons"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Chemical Nature:</strong> Lemon juice contains citric acid ($\text{C}_6\text{H}_8\text{O}_7$) dissolved in water.</li>
  <li><strong>Electrolyte Function:</strong> Citric acid dissociates into mobile positive hydrogen ions ($\text{H}^+$) and citrate anions.</li>
  <li><strong>Charge Transport:</strong> These mobile ions allow charges to travel through the liquid inside the lemon between the zinc nail and copper coin, completing the circuit.</li>
</ol>
"""
    },

    # Q24
    {
        "id": 24,
        "question": "In a lemon battery using a copper strip and a zinc nail, what chemical reaction occurs at the zinc electrode?",
        "options": [
            "Zinc gains electrons and turns into gold",
            "Zinc atoms lose electrons and dissolve into the acid ($\text{Zn} \rightarrow \text{Zn}^{2+} + 2e^-$)",
            "Zinc reacts with oxygen to freeze the lemon",
            "Zinc absorbs all the citric acid without reacting"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Oxidation:</strong> Zinc is chemically more reactive than copper and has a strong tendency to lose electrons.</li>
  <li><strong>Anode Reaction:</strong> Each zinc atom loses two electrons:
    $$\text{Zn} \rightarrow \text{Zn}^{2+} + 2e^-$$
  </li>
  <li><strong>Electron Flow:</strong> The freed electrons accumulate on the zinc nail, making it the negative terminal, and flow through the external wire to the copper strip.</li>
</ol>
"""
    },

    # Q25
    {
        "id": 25,
        "question": "Why is a commercial flashlight battery called a 'dry' cell even though it is not completely dry inside?",
        "options": [
            "Because it is dried in an oven before packaging",
            "Because its electrolyte is a thick, moist paste rather than a free-flowing liquid, preventing leakage when tipped or carried",
            "Because it only works in dry desert climates",
            "Because it contains no moisture whatsoever"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Wet Cells:</strong> Early Voltaic cells used liquid acids that spilled easily when moved or tilted.</li>
  <li><strong>Dry Cell Innovation:</strong> Carl Gassner immobilized the electrolyte by mixing ammonium chloride and zinc chloride into a moist paste with starch.</li>
  <li><strong>Portability:</strong> While containing sufficient moisture for ion transport, there is no loose liquid to spill, making it safely portable in flashlights and toys.</li>
</ol>
"""
    },

    # Q26
    {
        "id": 26,
        "question": "What is the function of the central graphite (carbon) rod in a standard zinc-carbon dry cell?",
        "options": [
            "It acts as the negative terminal where zinc dissolves",
            "It acts as an inert positive electrode (cathode) to collect electrons from the external circuit",
            "It stores electrical energy like a magnetic sponge",
            "It releases oxygen gas to cool the battery"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Inert Conductor:</strong> Carbon (graphite) conducts electricity well and does not chemically corrode in acidic paste.</li>
  <li><strong>Positive Terminal:</strong> The carbon rod conducts electrons arriving from the external circuit into the surrounding manganese dioxide mixture.</li>
  <li>The metal cap at the top of the rod serves as the positive terminal ($+$).</li>
</ol>
"""
    },

    # Q27
    {
        "id": 27,
        "question": "What role does Manganese Dioxide ($\text{MnO}_2$) play inside a dry cell?",
        "options": [
            "It acts as a depolarizer to oxidize hydrogen gas into water, preventing gas buildup",
            "It serves as the outer protective metal casing",
            "It turns the flashlight bulb purple",
            "It provides sweet scent to the paste"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Polarization Problem:</strong> During discharge, hydrogen gas ($\text{H}_2$) forms at the positive carbon cathode.</li>
  <li><strong>Insulation Barrier:</strong> If hydrogen gas bubbles coat the carbon rod, they insulate it and cause current to drop to zero.</li>
  <li><strong>Depolarization:</strong> $\text{MnO}_2$ reacts with hydrogen gas, oxidizing it safely into water ($\text{H}_2\text{O}$), keeping current flowing smoothly.</li>
</ol>
"""
    },

    # Q28
    {
        "id": 28,
        "question": "Why can secondary cells (like car batteries or smartphone batteries) be recharged while primary cells cannot?",
        "options": [
            "Secondary cells are made of rubber, which bounces current back",
            "The chemical reactions in secondary cells are electrically reversible when connected to an external charger",
            "Primary cells produce too much voltage to be recharged",
            "Secondary cells do not use any chemical reactions"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Primary Cells:</strong> Chemical reactions consume active materials (e.g., zinc container dissolves away) irreversibly. Discharging destroys the chemical structure.</li>
  <li><strong>Secondary Cells:</strong> The electrochemical reactions are designed to be reversible. Applying an opposing external electrical voltage forces electrons and ions back into their original starting compounds, restoring full charge.</li>
</ol>
"""
    },

    # Q29
    {
        "id": 29,
        "question": "Why are lithium-ion batteries so widely used in modern smartphones and electric cars instead of older lead-acid batteries?",
        "options": [
            "Lithium is the heaviest metal on Earth",
            "They offer much higher energy density, higher cell voltage ($3.7\text{ V}$), and lighter weight",
            "They are completely free to manufacture",
            "They never lose charge even after 100 years"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Weight:</strong> Lithium is the lightest solid element (atomic number 3), making batteries far lighter than lead-acid.</li>
  <li><strong>High Voltage:</strong> Delivers $3.7\text{ V}$ per cell compared to $1.2\text{ V}$ (NiMH) or $2.0\text{ V}$ (lead-acid).</li>
  <li><strong>Energy Density:</strong> Stores vastly more watt-hours per kilogram, enabling thin smartphones and long-range electric vehicles.</li>
</ol>
"""
    },

    # Q30
    {
        "id": 30,
        "question": "What is the primary risk associated with the liquid organic electrolyte used in conventional lithium-ion batteries?",
        "options": [
            "It turns into ice at room temperature",
            "It is flammable and can ignite a runaway chemical fire if punctured, overheated, or overcharged",
            "It attracts swarms of insects",
            "It prevents electric current from flowing"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Volatile Solvents:</strong> Conventional Li-ion cells use liquid organic carbonate solvents to transport $\text{Li}^+$ ions.</li>
  <li><strong>Thermal Runaway:</strong> If an internal short circuit occurs or the cell is punctured, runaway exothermic heat boils the solvent.</li>
  <li><strong>Combustion:</strong> Flammable vapors vent and ignite rapidly, leading to stubborn battery fires.</li>
</ol>
"""
    },

    # Q31
    {
        "id": 31,
        "question": "What is the defining innovation of next-generation solid-state batteries?",
        "options": [
            "They replace flammable liquid/paste electrolytes with solid non-flammable ceramic or polymer materials",
            "They run on solid coal instead of electricity",
            "They do not contain any electrodes",
            "They only store magnetic energy"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Solid Electrolyte:</strong> Replaces liquid electrolytes with solid crystalline ceramic or glass layers.</li>
  <li><strong>Fire Safety:</strong> Eliminates volatile, flammable solvents, preventing thermal runaway fires.</li>
  <li><strong>Performance:</strong> Enables lithium-metal anodes for double the energy density, faster charging times, and thousands of recharge cycles.</li>
</ol>
"""
    },

    # Q32
    {
        "id": 32,
        "question": "What ecological disaster occurs when spent batteries are dumped into municipal landfills?",
        "options": [
            "They turn the garbage into diamond crystals",
            "Corrosive acids and toxic heavy metals (lead, cadmium, lithium) leak into soil and contaminate groundwater supplies",
            "They freeze the landfill into solid ice",
            "They neutralize all other garbage safely"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Corrosion:</strong> Weathering and landfill moisture corrode the outer casings of discarded batteries.</li>
  <li><strong>Heavy Metal Leaching:</strong> Toxic neurotoxins (lead, cadmium) and corrosive electrolytes leak into surrounding soil.</li>
  <li><strong>Aquifer Poisoning:</strong> Rainwater carries these dissolved contaminants into underground aquifers, poisoning drinking water for humans and wildlife.</li>
</ol>
"""
    },

    # Q33
    {
        "id": 33,
        "question": "How do specialized e-waste recycling facilities recover valuable resources from spent batteries?",
        "options": [
            "They bury them in deep ocean trenches",
            "They crush spent batteries in inert atmospheres, neutralize chemicals, and extract up to 95% of purified lithium, cobalt, and copper",
            "They burn them in open backyard fires",
            "They wash them in bleach and resell them as new"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Inert Shredding:</strong> Batteries are shredded under nitrogen gas to prevent sparks and chemical fires.</li>
  <li><strong>Hydrometallurgy:</strong> Chemical leaching dissolves the metals into solution.</li>
  <li><strong>Element Recovery:</strong> High-purity lithium, cobalt, nickel, and copper are extracted and refined for direct reuse in manufacturing brand-new batteries.</li>
</ol>
"""
    },

    # Q34
    {
        "id": 34,
        "question": "If you connect three 1.5 V AA dry cells in series (positive to negative), what is the total voltage supplied?",
        "options": [
            "1.5 V",
            "3.0 V",
            "4.5 V",
            "0.5 V"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Series Rule:</strong> When cells are connected in series ($+ \rightarrow - \rightarrow + \rightarrow -$), their individual voltages add directly together:
    $$V_{\text{total}} = V_1 + V_2 + V_3$$
  </li>
  <li><strong>Calculation:</strong>
    $$V_{\text{total}} = 1.5\text{ V} + 1.5\text{ V} + 1.5\text{ V} = 4.5\text{ V}$$
  </li>
  <li>This is why devices needing 4.5 V use 3 AA batteries in series.</li>
</ol>
"""
    },

    # Q35
    {
        "id": 35,
        "question": "What happens if you connect an electromagnet to a DC battery and then to an AC power supply?",
        "options": [
            "With DC, the magnetic poles remain constant; with AC, the magnetic poles reverse every half-cycle",
            "With AC, the magnet becomes permanent and cannot be turned off",
            "With DC, no magnetic field is produced at all",
            "AC destroys the copper wire instantly"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Direct Current (DC):</strong> Current flows in one constant direction. The magnetic poles (North and South) remain stationary and fixed.</li>
  <li><strong>Alternating Current (AC):</strong> Current direction alternates back and forth 50 or 60 times per second ($50\text{ Hz}$).</li>
  <li><strong>Polarity Oscillation:</strong> As current reverses, the North and South poles of the electromagnet swap places 100 times every second!</li>
</ol>
"""
    },

    # Q36
    {
        "id": 36,
        "question": "Why is an alloy of lead and tin chosen for making electric fuse wire?",
        "options": [
            "It has a very low melting point and moderate resistance, allowing it to melt quickly during current surges",
            "It has the highest melting point of all known metals",
            "It is completely non-conductive to electricity",
            "It glows bright green to show current is flowing"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Low Melting Point:</strong> Solder alloy (approx. 63% tin, 37% lead) melts at roughly $183^\circ\text{C}$—far lower than copper ($1,085^\circ\text{C}$).</li>
  <li><strong>Protective Rupture:</strong> When excessive current surges through, Joule heat ($H = I^2 R t$) raises the fuse temperature past its melting point within milliseconds.</li>
  <li><strong>Safety:</strong> The wire melts and breaks the circuit long before copper building wires can overheat.</li>
</ol>
"""
    },

    # Q37
    {
        "id": 37,
        "question": "Why does an electric toaster have its heating coils exposed to air, while an electric geyser element is enclosed in a metal tube?",
        "options": [
            "Toasters do not use electricity",
            "The geyser element is immersed in water; enclosing it in a sealed tube with mineral insulation prevents electrical short circuits and water electrocution",
            "Bread needs to be electrocuted to become toast",
            "Geysers only heat water using magnetic fields"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Toaster:</strong> Operates in dry air; nichrome ribbons radiate infrared heat directly onto bread.</li>
  <li><strong>Geyser / Immersion Rod:</strong> Operates fully submerged in water. Since tap water conducts electricity, bare wire would short-circuit and electrocute anyone touching the water!</li>
  <li><strong>Tube Insulation:</strong> The nichrome coil is sealed inside a watertight copper/steel tube packed with compacted magnesium oxide ($\text{MgO}$) powder, which conducts heat well but is an electrical insulator.</li>
</ol>
"""
    },

    # Q38
    {
        "id": 38,
        "question": "What is the relationship between wire thickness (gauge) and safe current carrying capacity?",
        "options": [
            "Thicker wires have lower resistance and can safely carry higher electric currents without dangerous overheating",
            "Thinner wires carry more current because electrons are squeezed tighter",
            "Wire thickness has no effect on current carrying capacity",
            "Thick wires always melt faster than thin wires"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Resistance vs. Area:</strong> $R \propto 1/A$. A thicker wire has a larger cross-sectional area, offering much lower resistance to electron flow.</li>
  <li><strong>Reduced Heating:</strong> With lower resistance, $H = I^2 R t$ produces less heat for a given current.</li>
  <li><strong>Safety Standards:</strong> Heavy appliances (like $15\text{ A}$ air conditioners) require thick gauge wires to prevent dangerous heat buildup.</li>
</ol>
"""
    },

    # Q39
    {
        "id": 39,
        "question": "Which of the following metals is classified as a ferromagnetic material that will be attracted to an active electromagnet?",
        "options": [
            "Pure copper",
            "Pure aluminum",
            "Soft iron and nickel",
            "Pure silver"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Ferromagnetic Elements:</strong> Only a few elements—primarily <strong>Iron ($\text{Fe}$)</strong>, <strong>Cobalt ($\text{Co}$)</strong>, and <strong>Nickel ($\text{Ni}$)</strong>—possess unpaired electron spins that align strongly with external magnetic fields.</li>
  <li><strong>Non-Magnetic Metals:</strong> Copper, aluminum, silver, and gold are non-ferromagnetic (diamagnetic or paramagnetic) and are not attracted to electromagnets.</li>
</ol>
"""
    },

    # Q40
    {
        "id": 40,
        "question": "Why is the development of solid-state batteries considered a crucial breakthrough for electric vehicles (EVs)?",
        "options": [
            "They will enable faster charging times (10-15 minutes), higher driving range, and eliminate the danger of battery fires",
            "They will allow electric cars to fly through the air",
            "They will make cars run entirely on ocean salt water",
            "They will eliminate the need for an electric motor"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Fire Safety:</strong> Solid ceramic/polymer electrolytes are completely non-flammable, eliminating catastrophic EV battery fires.</li>
  <li><strong>Fast Charging:</strong> Solid electrolytes can tolerate higher current densities without forming dendritic short circuits, slashing charging time from an hour down to 10–15 minutes.</li>
  <li><strong>High Range:</strong> Compatible with pure lithium metal anodes, solid-state batteries offer up to double the energy density, enabling 800+ km driving range on a single charge.</li>
</ol>
"""
    }
]

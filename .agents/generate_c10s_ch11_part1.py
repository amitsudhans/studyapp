# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 11: Electricity
Part 1: Slides 1 to 8 Generator
Speech strictly 195-215 words. Titles strictly 1-3 words. Zero persona titles or forbidden names.
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Electric Current Fundamentals",
        "subtitle": "Flow of Electric Charge, Charge Carriers, and Coulomb Definition",
        "badge": "Section 11.1",
        "summary": "Electric current is the continuous rate of flow of electric charges through a conductor. By historical convention, electric current flows from positive to negative terminal, which is opposite to the physical drift of negatively charged mobile electrons.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Definition of Electric Current:</strong> Electric current is expressed by the amount of net electric charge flowing through any particular cross-sectional area of a conductor per unit time. If a net charge $Q$ flows across any cross-section in time $t$, the current $I$ is given by:</p>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-amber-300 text-sm">
                    $$I = \\frac{Q}{t}$$
                </div>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>⚡</span> Charge Quantization & Flow Direction:
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Charge Carrier Drift:</strong> In metallic conductors, conduction electrons constitute the physical flow of charge. An individual electron carries a fundamental negative charge of $e = 1.6 \\times 10^{-19}\\text{ C}$.</li>
                        <li><strong class="text-teal-300">The Coulomb ($1\\text{ C}$):</strong> One coulomb corresponds to the total combined charge of approximately $6 \\times 10^{18}$ electrons ($Q = ne$).</li>
                        <li><strong class="text-teal-300">Conventional Current:</strong> Because electricity was discovered before the electron, current was considered a flow of positive charges. Thus, conventional current flows from <span class="text-emerald-400 font-semibold">positive terminal to negative terminal</span>, opposite to electron drift.</li>
                    </ul>
                </div>
            </div>
        """,
        "speech": "Welcome to our comprehensive study of electricity, one of the most versatile and indispensable forms of energy powering modern human civilization. At the microscopic core of electrical science is electric charge. Electric current is precisely defined as the rate at which electric charge flows across a given cross-sectional boundary of a conducting wire. Mathematically, current I equals the total net charge Q divided by the total elapsed time t. In metallic conductors such as copper or aluminium, current is constituted by the movement of microscopic, negatively charged conduction electrons. A single electron possesses a tiny elementary negative charge of one point six times ten to the power of minus nineteen coulombs. Consequently, one coulomb of charge represents the colossal combined electrostatic quantity of nearly six times ten to the power of eighteen electrons. When scientists first investigated electrical phenomena, atomic electrons had not yet been identified. Physicists assumed that positive charges flowed through circuits. By historical convention, the direction of electric current in an electrical circuit is still defined from the positive terminal of a power source to the negative terminal, which is exactly opposite to the actual physical drift direction of mobile conduction electrons through the crystalline wire.",
        "checkpoints": [
            {
                "question": "What is the direction of conventional electric current in an external circuit?",
                "options": [
                    "From the positive terminal to the negative terminal",
                    "From the negative terminal to the positive terminal",
                    "Perpendicular to the conducting wire surface",
                    "Randomly fluctuating in both directions"
                ],
                "answer": 0,
                "hint": "Recall the historical scientific convention established prior to the discovery of electrons.",
                "explanation": "Conventionally, electric current is treated as the flow of positive charge from positive to negative terminal, opposite to actual electron drift."
            },
            {
                "question": "Approximately how many electrons are required to constitute one coulomb of electric charge?",
                "options": [
                    "6 × 10¹⁸ electrons",
                    "1.6 × 10⁻¹⁹ electrons",
                    "9.1 × 10⁻³¹ electrons",
                    "3 × 10⁸ electrons"
                ],
                "answer": 0,
                "hint": "Use the quantization relation n = Q/e where Q = 1 C and e = 1.6 × 10⁻¹⁹ C.",
                "explanation": "Since Q = n × e, n = 1 / (1.6 × 10⁻¹⁹) ≈ 6.25 × 10¹⁸ electrons, which is approximately 6 × 10¹⁸ electrons."
            }
        ]
    },
    {
        "id": 2,
        "title": "Circuit Ammeter Measurement",
        "subtitle": "The Ampere Unit, Continuous Closed Paths, and Series Ammeters",
        "badge": "Section 11.1",
        "summary": "An electric circuit is a continuous and closed conducting loop. Electric current is measured in amperes using an ammeter, which must always be connected in series so that all circulating charges flow through its low-resistance meter.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">SI Unit of Current — The Ampere:</strong> The SI unit of electric current is the <span class="text-amber-300 font-semibold">Ampere (A)</span>, named in honour of French physicist André-Marie Ampère. One ampere is defined as the flow of one coulomb of charge per second:</p>
                <div class="p-2 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-cyan-300 text-xs">
                    $$1\\text{ A} = 1\\text{ C/s} = 1\\text{ Coulomb per second}$$
                </div>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>🔌</span> Circuit Architecture & Metering:
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Closed Circuit Loop:</strong> A continuous conducting path consisting of a cell, switch, load, and connecting wires. If broken at any point (open switch), current stops immediately.</li>
                        <li><strong class="text-teal-300">Smaller Units:</strong> Milliampere ($1\\text{ mA} = 10^{-3}\\text{ A}$) and microampere ($1\\ \\mu\\text{A} = 10^{-6}\\text{ A}$).</li>
                        <li><strong class="text-teal-300">The Ammeter:</strong> An instrument designed to measure electric current. It features an extremely low internal resistance and is <span class="text-amber-300 font-semibold">always connected in series</span> with the circuit components.</li>
                    </ul>
                </div>
                <p><strong class="text-amber-400">Example 11.1 Reference:</strong> A current of $0.5\\text{ A}$ drawn by an electric bulb filament for $10\\text{ minutes}$ ($600\\text{ s}$) transports total charge $Q = I \\times t = 0.5 \\times 600 = 300\\text{ C}$.</p>
            </div>
        """,
        "speech": "We now explore how electric current is quantified and measured within practical electrical circuits and domestic networks. The international unit of electric current is the ampere, represented by capital letter A, named in honour of the celebrated French scientist André-Marie Ampère. One ampere is formally defined as the flow of one coulomb of electric charge passing through a circuit per second. For smaller electronic appliances, current is frequently measured in milliamperes, where one milliampere equals ten to the power of minus three amperes, or microamperes, where one microampere equals ten to the power of minus six amperes. To sustain electric current, components must form a continuous and completely closed conducting loop known as an electric circuit. If the circuit is broken anywhere, such as when a switch is opened, the current ceases to flow instantly. To measure the magnitude of electric current in a circuit, an instrument called an ammeter is deployed. An ammeter possesses negligible internal electrical resistance and is always installed strictly in series with circuit devices. Connecting the ammeter in series ensures that the exact same stream of flowing electric charge traverses the instrument without altering total circuit resistance or perturbing circuit behavior.",
        "checkpoints": [
            {
                "question": "How must an ammeter always be connected in an electrical circuit to measure current?",
                "options": [
                    "In series with the component",
                    "In parallel across the power source",
                    "Directly between battery terminals",
                    "Outside the metallic enclosure"
                ],
                "answer": 0,
                "hint": "All circulating charges must flow directly through the meter without bypassing it.",
                "explanation": "An ammeter has very low internal resistance and must be connected in series so that the entire circuit current passes through it."
            },
            {
                "question": "A current of 0.5 A flows through a bulb filament for 10 minutes. What total charge passes through the circuit?",
                "options": [
                    "300 C",
                    "5 C",
                    "50 C",
                    "3000 C"
                ],
                "answer": 0,
                "hint": "Convert 10 minutes to seconds (t = 600 s) and use Q = I × t.",
                "explanation": "Q = I × t = 0.5 A × (10 × 60 s) = 0.5 A × 600 s = 300 Coulombs (NCERT Example 11.1)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Electric Potential Difference",
        "subtitle": "Electrical Pressure, Work Done per Unit Charge, and The Volt Unit",
        "badge": "Section 11.2",
        "summary": "Charges do not move on their own; they require an electric potential difference, analogous to pressure differences driving water flow. Potential difference ($V = W/Q$) is the work done to transport a unit positive charge between two points.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">The Hydraulic Analogy:</strong> Water in a perfectly horizontal tube does not flow on its own. However, connecting one end to an elevated reservoir creates a hydrostatic pressure difference that forces water through the pipe. Similarly, electrons flow in a metallic wire only when there is an <span class="text-teal-300 font-semibold">electric potential difference</span> maintained across its ends.</p>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>🔋</span> Chemical Batteries & Potential Difference ($V$):
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Chemical Generation:</strong> Chemical reactions inside an electrochemical cell produce a potential difference between its two terminals even when no current is drawn.</li>
                        <li><strong class="text-teal-300">Mathematical Definition:</strong> Electric potential difference ($V$) between two points is defined as the work done ($W$) in moving a unit charge ($Q$) from one point to the other:
                            $$V = \\frac{W}{Q} \\implies W = V \\times Q$$
                        </li>
                        <li><strong class="text-teal-300">The Volt ($1\\text{ V}$):</strong> Named after Alessandro Volta. One volt is the potential difference between two points when one joule of work is done in moving a charge of one coulomb:
                            $$1\\text{ V} = 1\\text{ J/C} = 1\\text{ Joule per Coulomb}$$
                        </li>
                    </ul>
                </div>
                <p><strong class="text-amber-400">Example 11.2:</strong> Moving a charge of $2\\text{ C}$ across two points having potential difference $12\\text{ V}$ requires work $W = V \\times Q = 12\\text{ V} \\times 2\\text{ C} = 24\\text{ Joules}$.</p>
            </div>
        """,
        "speech": "To understand what causes electric charges to move through a solid metallic conductor, consider water flowing inside a pipe. Water does not circulate through a horizontal tube on its own. But if one end of the tube is connected to an elevated tank, a pressure differential develops, causing water to surge toward the lower end. In exact analogy, conduction electrons inside a copper wire move only when an electric pressure difference, known as electric potential difference, is established across its ends. An electrochemical cell or battery generates and maintains this potential difference across its terminals through internal chemical reactions. We define electric potential difference between two points in an electrical circuit as the total mechanical or chemical work done in moving a unit electric charge between those two points. Mathematically, potential difference V equals work done W divided by charge Q. The SI unit of electric potential difference is the volt, symbolized by capital V, named in honour of Alessandro Volta. One volt represents the potential difference between two points when exactly one joule of energy is expended to transport a charge of one coulomb. A higher voltage exerts a stronger electromotive force, driving charges through resistive pathways.",
        "checkpoints": [
            {
                "question": "What is the SI unit of electric potential difference?",
                "options": [
                    "Volt (V)",
                    "Ampere (A)",
                    "Coulomb (C)",
                    "Ohm (Ω)"
                ],
                "answer": 0,
                "hint": "Named after the Italian inventor of the chemical battery, Alessandro Volta.",
                "explanation": "The SI unit of electric potential difference is the volt (V), where 1 V = 1 Joule per Coulomb."
            },
            {
                "question": "How much work is done in moving a charge of 2 C across two points having a potential difference of 12 V?",
                "options": [
                    "24 J",
                    "6 J",
                    "14 J",
                    "0.16 J"
                ],
                "answer": 0,
                "hint": "Use the work formula W = V × Q.",
                "explanation": "Work done W = V × Q = 12 V × 2 C = 24 Joules (NCERT Example 11.2)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Circuit Diagram Symbols",
        "subtitle": "Voltmeters, Rheostats, and Standard Schematic Conventions",
        "badge": "Section 11.2 & 11.3",
        "summary": "Circuit diagrams provide standardized symbolic representations of electrical networks. A voltmeter measures potential difference and is connected in parallel, while standard symbols represent cells, batteries, switches, resistors, and rheostats.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Voltmeter Parallel Installation:</strong> Potential difference is measured by an instrument called a <span class="text-teal-300 font-semibold">voltmeter</span>. Because it must determine the energy drop across two specific nodes without drawing current, it has an extremely high internal resistance and is <span class="text-amber-300 font-semibold">always connected in parallel</span> across the points of interest.</p>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>📐</span> Standard Circuit Schematic Symbols (Table 11.1):
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Electric Cell:</strong> Long thin vertical line (positive terminal) paired with a short thick vertical line (negative terminal).</li>
                        <li><strong class="text-teal-300">Battery of Cells:</strong> Series combination of alternating long and short terminal plates.</li>
                        <li><strong class="text-teal-300">Plug Key (Switch):</strong> Parentheses `()` for open key (no dot); `(·)` for closed key with central dot.</li>
                        <li><strong class="text-teal-300">Wire Joint vs Crossing:</strong> T-junction dot for physical joint; arch bridge symbol for crossing wires without contact.</li>
                        <li><strong class="text-teal-300">Resistor & Rheostat:</strong> Zig-zag line for fixed resistor; zig-zag with diagonal arrow or slider for variable resistor (rheostat).</li>
                        <li><strong class="text-teal-300">Ammeter vs Voltmeter:</strong> Encircled `A` with polarity signs (series); encircled `V` with polarity signs (parallel).</li>
                    </ul>
                </div>
            </div>
        """,
        "speech": "To design, analyze, and troubleshoot electrical systems conveniently, engineers utilize standardized schematic symbols assembled and compiled into standard circuit diagrams. Instead of drawing realistic physical pictures of bulbs, batteries, and switches, standard graphical representations established in Table 11.1 of the textbook are used globally. An individual electric cell is depicted by two parallel vertical lines: a long thin line denoting the positive terminal, and a shorter thick line representing the negative terminal. A battery consists of several cells connected in series. A plug key or switch is drawn using curved parentheses, where an empty pair of parentheses indicates an open switch and a central dot signifies a closed, conducting switch. A fixed resistor is shown as a sharp zig-zag line, representing resistance to charge motion. When a circuit requires continuous current adjustment without altering source voltage, a variable resistor, commonly termed a rheostat, is introduced, depicted by a zig-zag line with an arrow. To measure potential difference across any component, a voltmeter is deployed. In sharp contrast to an ammeter, a voltmeter possesses an exceptionally high internal resistance and is always connected strictly in parallel across the two points under evaluation to prevent drawing significant measurement current away from the circuit.",
        "checkpoints": [
            {
                "question": "How must a voltmeter always be connected across a circuit component?",
                "options": [
                    "In parallel across the component",
                    "In series with the component",
                    "Directly in line with the ammeter",
                    "Grounded to the circuit chassis"
                ],
                "answer": 0,
                "hint": "A voltmeter measures potential difference between two distinct points.",
                "explanation": "A voltmeter has high internal resistance and is always connected in parallel across the two points between which potential difference is measured."
            },
            {
                "question": "What is the primary function of a rheostat (variable resistor) in an electric circuit?",
                "options": [
                    "Regulating current without changing source voltage",
                    "Reversing the chemical polarity of the battery",
                    "Converting alternating current into direct current",
                    "Increasing the total electrostatic charge of the universe"
                ],
                "answer": 0,
                "hint": "Recall the definition of a variable resistance device in Section 11.4.",
                "explanation": "A rheostat allows continuous variation of circuit resistance to regulate current magnitude without altering the applied potential difference."
            }
        ]
    },
    {
        "id": 5,
        "title": "Ohms Law Verification",
        "subtitle": "Activity 11.1, Linear Proportionality, and Constant V/I Ratio",
        "badge": "Section 11.4",
        "summary": "Ohm's law establishes that the electric current through a metallic conductor is directly proportional to the potential difference across its ends, provided temperature remains constant. The ratio V/I is a characteristic constant known as resistance.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Activity 11.1 Investigation:</strong> Connect a nichrome resistance wire in series with an ammeter, plug key, and an adjustable power source made of 1, 2, 3, or 4 dry cells ($1.5\\text{ V}$ each). A voltmeter is connected in parallel across the nichrome wire.</p>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>🔬</span> Experimental Observations (Table 11.2 Data):
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li>With 1 cell ($V = 1.5\\text{ V}$), current is measured as $I_1$.</li>
                        <li>With 2 cells ($V = 3.0\\text{ V}$), current doubles to $I_2 = 2 I_1$.</li>
                        <li>With 3 cells ($V = 4.5\\text{ V}$), current triples to $I_3 = 3 I_1$.</li>
                        <li>Calculating the ratio $\\frac{V}{I}$ for each trial yields an identical numerical constant within experimental error:
                            $$\\frac{V}{I} = \\text{Constant} = R$$
                        </li>
                    </ul>
                </div>
                <p><strong class="text-amber-400">Formal Law Statement:</strong> In 1827, German physicist Georg Simon Ohm discovered that the electric current flowing through a metallic wire is <span class="text-teal-300 font-semibold">directly proportional</span> to the potential difference across its ends, provided its temperature remains strictly constant ($V \\propto I$).</p>
            </div>
        """,
        "speech": "In 1827, German physicist Georg Simon Ohm formulated the fundamental relationship governing electrical circuits, universally known as Ohm's law. In Activity 11.1, we investigate this principle using a simple test circuit containing a length of nichrome wire, an ammeter, a sensitive voltmeter, and a series of dry cells. Initially, a single one point five volt cell is connected, and the corresponding current is recorded from the ammeter. Next, two cells in series supply three volts, then three cells supply four point five volts, and finally four cells provide six volts. In each experimental step, both the potential difference V and the circuit current I increase simultaneously in direct proportion. When you compute the mathematical ratio of voltage to current, V divided by I, for each experimental trial, you discover an invariant numerical value. This experimental milestone proves that the electric current flowing through a metallic conductor is directly proportional to the potential difference across its terminals, provided the conductor's physical dimensions and temperature remain constant. Mathematically, V is proportional to I, which we express as V equals I multiplied by R. Here, R is a constant of proportionality unique to the conductor, termed its electrical resistance.",
        "checkpoints": [
            {
                "question": "What essential physical condition must remain constant for Ohm's law to hold strictly true?",
                "options": [
                    "Temperature of the metallic conductor",
                    "Mass of the ammeter needle",
                    "Atmospheric air pressure in the room",
                    "Color of the connecting wire insulation"
                ],
                "answer": 0,
                "hint": "Thermal variations alter the internal kinetic vibration of metallic lattice ions.",
                "explanation": "Ohm's law requires that temperature and other physical conditions of the conductor remain constant, since resistance changes with temperature."
            },
            {
                "question": "If the potential difference across an ohmic conductor is tripled, what happens to the electric current?",
                "options": [
                    "It triples (increases by a factor of 3)",
                    "It drops to one-third its original value",
                    "It increases nine-fold (3²)",
                    "It remains completely unchanged"
                ],
                "answer": 0,
                "hint": "Current is directly proportional to potential difference (V ∝ I).",
                "explanation": "Because current is directly proportional to voltage (I ∝ V), tripling the potential difference triples the current flowing through the conductor."
            }
        ]
    },
    {
        "id": 6,
        "title": "Current Voltage Graph",
        "subtitle": "Linear V-I Characteristics, The Ohm Unit, and Resistance Concept",
        "badge": "Section 11.4",
        "summary": "Plotting potential difference (V) against current (I) for an ohmic conductor yields a straight line passing through the origin. Resistance is the property of a conductor to resist charge flow; its SI unit is the ohm (Ω).",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">The Linear $V\\text{--}I$ Graph:</strong> When the experimental data from Activity 11.1 are plotted with potential difference $V$ on the vertical y-axis and current $I$ on the horizontal x-axis, the resulting curve is a <span class="text-teal-300 font-semibold">straight line passing through the origin</span> $(0,0)$.</p>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>📈</span> Slope & Resistance Interpretation:
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Slope Equals Resistance:</strong> The slope of the $V\\text{--}I$ graph represents the electrical resistance of the metallic conductor:
                            $$\\text{Slope} = \\frac{\\Delta V}{\\Delta I} = R$$
                        </li>
                        <li><strong class="text-teal-300">Physical Origin of Resistance:</strong> Electrons drifting through a metal collide repeatedly with vibrating positive lattice ions, dissipating kinetic energy and impeding flow.</li>
                        <li><strong class="text-teal-300">The Ohm ($\\Omega$):</strong> SI unit of resistance, denoted by Greek letter omega ($\\Omega$). One ohm is the resistance of a conductor carrying a current of $1\\text{ A}$ under a potential difference of $1\\text{ V}$:
                            $$1\\ \\Omega = \\frac{1\\text{ V}}{1\\text{ A}}$$
                        </li>
                    </ul>
                </div>
                <p><strong class="text-amber-400">Inverse Current Relation:</strong> From $I = V/R$, current is inversely proportional to resistance. Doubling circuit resistance cuts current by half for a fixed voltage.</p>
            </div>
        """,
        "speech": "When we graphically plot the experimental measurements of potential difference on the vertical axis against the corresponding electric current on the horizontal axis, we obtain a straight line passing directly through the coordinate origin. This linear graph is the definitive optical hallmark of an ohmic conductor. The slope of this line, calculated as the change in voltage divided by the change in current, gives the electrical resistance R of the conductor. Resistance is the intrinsic property of a conductor to oppose the flow of electric charges. At the atomic scale, as free electrons accelerate under an applied electric field, they collide continuously with vibrating positive metallic ions in the crystal lattice. These collisions impede electron migration and dissipate electrical energy into thermal vibrations. The SI unit of electrical resistance is the ohm, symbolized by the uppercase Greek letter omega. One ohm is formally defined as the resistance of a conductor through which a current of one ampere flows when a potential difference of one volt is maintained across its ends. Ohm's law also reveals that current is inversely proportional to resistance. If resistance is doubled while voltage remains constant, the current is reduced to exactly half its previous value.",
        "checkpoints": [
            {
                "question": "What is represented by the slope of a straight-line V-I graph?",
                "options": [
                    "Electrical resistance of the conductor (R)",
                    "Total electrostatic charge in the wire (Q)",
                    "Electric power consumed per second (P)",
                    "Magnetic flux density of the circuit (B)"
                ],
                "answer": 0,
                "hint": "Slope = ΔV / ΔI. Recall Ohm's law formula R = V/I.",
                "explanation": "In a V-I graph, the slope is ΔV / ΔI, which equals the electrical resistance (R) of the conductor."
            },
            {
                "question": "If the resistance of an active circuit is doubled while applied voltage is kept constant, what happens to current?",
                "options": [
                    "Current is halved",
                    "Current is doubled",
                    "Current quadruples",
                    "Current drops to zero"
                ],
                "answer": 0,
                "hint": "Recall that I = V / R, showing inverse proportionality between current and resistance.",
                "explanation": "Since current is inversely proportional to resistance (I = V/R), doubling resistance cuts the electric current to half its original value."
            }
        ]
    },
    {
        "id": 7,
        "title": "Resistance Geometric Factors",
        "subtitle": "Activity 11.3, Length Proportionality, and Cross-Sectional Area",
        "badge": "Section 11.5",
        "summary": "Activity 11.3 proves that conductor resistance is directly proportional to its length ($R \\propto l$) and inversely proportional to its cross-sectional area ($R \\propto 1/A$). A thicker wire provides lower resistance, while a longer wire provides higher resistance.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Activity 11.3 Experimental Tests:</strong> In a circuit powered by a fixed battery, insert different test wires and measure current with an ammeter:</p>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>📏</span> Empirical Dependencies of Resistance:
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Length ($l$):</strong> Doubling wire length ($2l$) cuts current in half, proving resistance is directly proportional to length:
                            $$R \\propto l$$
                        </li>
                        <li><strong class="text-teal-300">Cross-Sectional Area ($A$):</strong> Using a thicker wire of identical material and length increases current, proving resistance is inversely proportional to cross-sectional area:
                            $$R \\propto \\frac{1}{A}$$
                        </li>
                        <li><strong class="text-teal-300">Material Composition:</strong> Wires of identical length and cross-section made of copper, nichrome, and iron conduct vastly different currents, showing resistance depends fundamentally on material nature.</li>
                    </ul>
                </div>
                <p><strong class="text-amber-400">Combined Proportionality:</strong> Combining these empirical geometric factors gives:
                    $$R \\propto \\frac{l}{A} \\implies R = \\rho \\frac{l}{A}$$
                where $\\rho$ is the constant of proportionality termed electrical resistivity.</p>
            </div>
        """,
        "speech": "We now examine the physical and geometric parameters that determine the electrical resistance of a conductor, systematically investigated in Activity 11.3 in the laboratory. When you test a variety of conducting wires in a constant-voltage circuit, three clear relationships emerge. First, when a wire of double the length is introduced, the ammeter reading drops to exactly half its initial value. This demonstrates that electrical resistance is directly proportional to conductor length. A longer wire presents a longer obstacle course of atomic lattice ions, multiplying the frequency of electron-ion scattering collisions. Second, when a thicker wire possessing a larger cross-sectional area is tested, the current increases substantially. This proves that resistance is inversely proportional to the cross-sectional area of the conductor. A thicker wire provides a wider corridor, allowing electrons to drift with far fewer bottleneck constraints. Third, when wires of identical length and diameter made of different metals such as copper and nichrome are compared, they register markedly different currents. This shows that resistance depends fundamentally on the material nature itself. Combining these geometric factors yields the universal resistance equation: R equals rho multiplied by length l divided by cross-sectional area A, where rho represents the intrinsic electrical resistivity of the material.",
        "checkpoints": [
            {
                "question": "How does the resistance of a metallic wire change if its length is doubled while maintaining constant thickness?",
                "options": [
                    "Resistance is doubled",
                    "Resistance is halved",
                    "Resistance quadruples",
                    "Resistance decreases to zero"
                ],
                "answer": 0,
                "hint": "Resistance is directly proportional to length (R ∝ l).",
                "explanation": "Because resistance is directly proportional to length, doubling the length of the wire doubles its electrical resistance."
            },
            {
                "question": "Why does a thick wire carry more current than a thin wire of the same material and length?",
                "options": [
                    "A thick wire has a larger cross-sectional area, offering lower resistance",
                    "A thick wire creates a stronger gravitational field",
                    "Electrons travel at twice the speed of light in thick wires",
                    "A thick wire absorbs all electric potential difference"
                ],
                "answer": 0,
                "hint": "Recall that resistance is inversely proportional to cross-sectional area (R ∝ 1/A).",
                "explanation": "A larger cross-sectional area provides more parallel conduction channels for electrons, decreasing resistance (R ∝ 1/A) and allowing greater current flow."
            }
        ]
    },
    {
        "id": 8,
        "title": "Electrical Resistivity Spectrum",
        "subtitle": "Material Properties, Ohm-Metre Unit, and Heating Device Alloys",
        "badge": "Section 11.5",
        "summary": "Electrical resistivity (ρ) is an intrinsic material property measured in ohm-metres (Ω·m). Metals have very low resistivity, insulators have enormous resistivity, and alloys with high resistivity and non-oxidizing properties are used in electric heating elements.",
        "theory": """
            <div class="space-y-3 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Definition of Electrical Resistivity ($\\rho$):</strong> From the resistance formula $R = \\rho \\frac{l}{A}$, isolating resistivity yields:</p>
                <div class="p-2 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-cyan-300 text-xs">
                    $$\\rho = \\frac{R \\times A}{l} \\implies \\text{Unit: } \\frac{\\Omega \\times \\text{m}^2}{\\text{m}} = \\Omega\\cdot\\text{m}$$
                </div>
                <div class="p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5">
                    <div class="text-amber-300 font-bold flex items-center gap-1.5">
                        <span>📊</span> Resistivity Classification (Table 11.2):
                    </div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        <li><strong class="text-teal-300">Conductors ($10^{-8} \\text{ to } 10^{-6}\\ \\Omega\\cdot\\text{m}$):</strong> Silver ($\\rho = 1.60 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}$) is the best electrical conductor, followed by copper and aluminium, which are used for electrical transmission lines.</li>
                        <li><strong class="text-teal-300">Alloys ($10^{-6}\\ \\Omega\\cdot\\text{m}$):</strong> Nichrome, constantan, and manganin have higher resistivities than their constituent metals. Crucially, alloys <span class="text-rose-400 font-semibold">do not oxidize (burn) easily at high temperatures</span>, making them ideal for heating coils in toasters, geysers, and electric irons.</li>
                        <li><strong class="text-teal-300">Insulators ($10^{12} \\text{ to } 10^{17}\\ \\Omega\\cdot\\text{m}$):</strong> Glass, hard rubber, and ebonite prevent charge transport entirely.</li>
                        <li><strong class="text-teal-300">Tungsten Filaments:</strong> High melting point ($3380^\\circ\\text{C}$) makes tungsten indispensable for glowing incandescent bulb filaments.</li>
                    </ul>
                </div>
            </div>
        """,
        "speech": "We now examine electrical resistivity, symbolized by the Greek letter rho, which measures a material's intrinsic opposition to electric charge flow regardless of physical dimensions. While resistance R depends on both geometry and material, resistivity rho is an inherent physical constant of the material at a given temperature. The SI unit of electrical resistivity is the ohm-metre. Examining Table 11.2 reveals that materials span an astonishing twenty orders of magnitude in resistivity. Metals such as silver, copper, and aluminium exhibit exceptionally low resistivities in the range of ten to the power of minus eight to ten to the power of minus six ohm-metres, making them outstanding choices for long-distance power transmission cables. In contrast, electrical insulators such as glass, rubber, and plastics possess colossal resistivities ranging from ten to the power of twelve to ten to the power of seventeen ohm-metres. Alloys such as nichrome occupy an intermediate bracket. Nichrome exhibits much higher resistivity than its constituent pure metals and possesses the vital property that it does not oxidize or burn easily even when glowing red-hot at high temperatures. Consequently, alloys are universally employed to construct the heating elements of electric irons, toasters, and room heaters.",
        "checkpoints": [
            {
                "question": "What is the SI unit of electrical resistivity?",
                "options": [
                    "Ohm-metre (Ω·m)",
                    "Ohm per metre (Ω/m)",
                    "Volt per ampere (V/A)",
                    "Coulomb per second (C/s)"
                ],
                "answer": 0,
                "hint": "From ρ = R × A / l, evaluate the unit dimension (Ω × m² / m).",
                "explanation": "The SI unit of resistivity is the ohm-metre (Ω·m)."
            },
            {
                "question": "Why are alloys such as nichrome preferred over pure metals for the heating elements of electric irons and toasters?",
                "options": [
                    "They have higher resistivity and do not oxidize at high temperatures",
                    "They conduct electricity with zero resistance at room temperature",
                    "They melt at low temperatures to serve as safety fuses",
                    "They emit blue light without producing any thermal energy"
                ],
                "answer": 0,
                "hint": "Consider heating performance and resistance to thermal degradation.",
                "explanation": "Alloys have higher resistivity than pure metals and do not oxidize (burn) easily even at high operating temperatures."
            }
        ]
    }
]

with open(".agents/c10s_ch11_part1.json", "w", encoding="utf-8") as f:
    json.dump(slides_part1, f, indent=2)

print(f"Generated {len(slides_part1)} slides in Part 1.")
for s in slides_part1:
    wc = len(s["speech"].split())
    tc = len(s["title"].split())
    print(f"Slide {s['id']}: '{s['title']}' ({tc} words) | Speech: {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} speech out of range: {wc}"
    assert 1 <= tc <= 3, f"Slide {s['id']} title out of range: {tc}"

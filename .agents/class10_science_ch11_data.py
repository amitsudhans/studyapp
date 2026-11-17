# -*- coding: utf-8 -*-
"""Class 10 Science Chapter 11 Slide Data"""

slides = [
  {
    "id": 1,
    "title": "Electric Current Fundamentals",
    "subtitle": "Flow of Electric Charge, Charge Carriers, and Coulomb Definition",
    "badge": "Section 11.1",
    "summary": "Electric current is the continuous rate of flow of electric charges through a conductor. By historical convention, electric current flows from positive to negative terminal, which is opposite to the physical drift of negatively charged mobile electrons.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Definition of Electric Current:</strong> Electric current is expressed by the amount of net electric charge flowing through any particular cross-sectional area of a conductor per unit time. If a net charge $Q$ flows across any cross-section in time $t$, the current $I$ is given by:</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-amber-300 text-sm\">\n                    $$I = \\frac{Q}{t}$$\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\u26a1</span> Charge Quantization & Flow Direction:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Charge Carrier Drift:</strong> In metallic conductors, conduction electrons constitute the physical flow of charge. An individual electron carries a fundamental negative charge of $e = 1.6 \\times 10^{-19}\\text{ C}$.</li>\n                        <li><strong class=\"text-teal-300\">The Coulomb ($1\\text{ C}$):</strong> One coulomb corresponds to the total combined charge of approximately $6 \\times 10^{18}$ electrons ($Q = ne$).</li>\n                        <li><strong class=\"text-teal-300\">Conventional Current:</strong> Because electricity was discovered before the electron, current was considered a flow of positive charges. Thus, conventional current flows from <span class=\"text-emerald-400 font-semibold\">positive terminal to negative terminal</span>, opposite to electron drift.</li>\n                    </ul>\n                </div>\n            </div>\n        ",
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
          "6 \u00d7 10\u00b9\u2078 electrons",
          "1.6 \u00d7 10\u207b\u00b9\u2079 electrons",
          "9.1 \u00d7 10\u207b\u00b3\u00b9 electrons",
          "3 \u00d7 10\u2078 electrons"
        ],
        "answer": 0,
        "hint": "Use the quantization relation n = Q/e where Q = 1 C and e = 1.6 \u00d7 10\u207b\u00b9\u2079 C.",
        "explanation": "Since Q = n \u00d7 e, n = 1 / (1.6 \u00d7 10\u207b\u00b9\u2079) \u2248 6.25 \u00d7 10\u00b9\u2078 electrons, which is approximately 6 \u00d7 10\u00b9\u2078 electrons."
      }
    ]
  },
  {
    "id": 2,
    "title": "Circuit Ammeter Measurement",
    "subtitle": "The Ampere Unit, Continuous Closed Paths, and Series Ammeters",
    "badge": "Section 11.1",
    "summary": "An electric circuit is a continuous and closed conducting loop. Electric current is measured in amperes using an ammeter, which must always be connected in series so that all circulating charges flow through its low-resistance meter.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">SI Unit of Current \u2014 The Ampere:</strong> The SI unit of electric current is the <span class=\"text-amber-300 font-semibold\">Ampere (A)</span>, named in honour of French physicist Andr\u00e9-Marie Amp\u00e8re. One ampere is defined as the flow of one coulomb of charge per second:</p>\n                <div class=\"p-2 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-cyan-300 text-xs\">\n                    $$1\\text{ A} = 1\\text{ C/s} = 1\\text{ Coulomb per second}$$\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udd0c</span> Circuit Architecture & Metering:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Closed Circuit Loop:</strong> A continuous conducting path consisting of a cell, switch, load, and connecting wires. If broken at any point (open switch), current stops immediately.</li>\n                        <li><strong class=\"text-teal-300\">Smaller Units:</strong> Milliampere ($1\\text{ mA} = 10^{-3}\\text{ A}$) and microampere ($1\\ \\mu\\text{A} = 10^{-6}\\text{ A}$).</li>\n                        <li><strong class=\"text-teal-300\">The Ammeter:</strong> An instrument designed to measure electric current. It features an extremely low internal resistance and is <span class=\"text-amber-300 font-semibold\">always connected in series</span> with the circuit components.</li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Example 11.1 Reference:</strong> A current of $0.5\\text{ A}$ drawn by an electric bulb filament for $10\\text{ minutes}$ ($600\\text{ s}$) transports total charge $Q = I \\times t = 0.5 \\times 600 = 300\\text{ C}$.</p>\n            </div>\n        ",
    "speech": "We now explore how electric current is quantified and measured within practical electrical circuits and domestic networks. The international unit of electric current is the ampere, represented by capital letter A, named in honour of the celebrated French scientist Andr\u00e9-Marie Amp\u00e8re. One ampere is formally defined as the flow of one coulomb of electric charge passing through a circuit per second. For smaller electronic appliances, current is frequently measured in milliamperes, where one milliampere equals ten to the power of minus three amperes, or microamperes, where one microampere equals ten to the power of minus six amperes. To sustain electric current, components must form a continuous and completely closed conducting loop known as an electric circuit. If the circuit is broken anywhere, such as when a switch is opened, the current ceases to flow instantly. To measure the magnitude of electric current in a circuit, an instrument called an ammeter is deployed. An ammeter possesses negligible internal electrical resistance and is always installed strictly in series with circuit devices. Connecting the ammeter in series ensures that the exact same stream of flowing electric charge traverses the instrument without altering total circuit resistance or perturbing circuit behavior.",
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
        "hint": "Convert 10 minutes to seconds (t = 600 s) and use Q = I \u00d7 t.",
        "explanation": "Q = I \u00d7 t = 0.5 A \u00d7 (10 \u00d7 60 s) = 0.5 A \u00d7 600 s = 300 Coulombs (NCERT Example 11.1)."
      }
    ]
  },
  {
    "id": 3,
    "title": "Electric Potential Difference",
    "subtitle": "Electrical Pressure, Work Done per Unit Charge, and The Volt Unit",
    "badge": "Section 11.2",
    "summary": "Charges do not move on their own; they require an electric potential difference, analogous to pressure differences driving water flow. Potential difference ($V = W/Q$) is the work done to transport a unit positive charge between two points.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">The Hydraulic Analogy:</strong> Water in a perfectly horizontal tube does not flow on its own. However, connecting one end to an elevated reservoir creates a hydrostatic pressure difference that forces water through the pipe. Similarly, electrons flow in a metallic wire only when there is an <span class=\"text-teal-300 font-semibold\">electric potential difference</span> maintained across its ends.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udd0b</span> Chemical Batteries & Potential Difference ($V$):\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Chemical Generation:</strong> Chemical reactions inside an electrochemical cell produce a potential difference between its two terminals even when no current is drawn.</li>\n                        <li><strong class=\"text-teal-300\">Mathematical Definition:</strong> Electric potential difference ($V$) between two points is defined as the work done ($W$) in moving a unit charge ($Q$) from one point to the other:\n                            $$V = \\frac{W}{Q} \\implies W = V \\times Q$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">The Volt ($1\\text{ V}$):</strong> Named after Alessandro Volta. One volt is the potential difference between two points when one joule of work is done in moving a charge of one coulomb:\n                            $$1\\text{ V} = 1\\text{ J/C} = 1\\text{ Joule per Coulomb}$$\n                        </li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Example 11.2:</strong> Moving a charge of $2\\text{ C}$ across two points having potential difference $12\\text{ V}$ requires work $W = V \\times Q = 12\\text{ V} \\times 2\\text{ C} = 24\\text{ Joules}$.</p>\n            </div>\n        ",
    "speech": "To understand what causes electric charges to move through a solid metallic conductor, consider water flowing inside a pipe. Water does not circulate through a horizontal tube on its own. But if one end of the tube is connected to an elevated tank, a pressure differential develops, causing water to surge toward the lower end. In exact analogy, conduction electrons inside a copper wire move only when an electric pressure difference, known as electric potential difference, is established across its ends. An electrochemical cell or battery generates and maintains this potential difference across its terminals through internal chemical reactions. We define electric potential difference between two points in an electrical circuit as the total mechanical or chemical work done in moving a unit electric charge between those two points. Mathematically, potential difference V equals work done W divided by charge Q. The SI unit of electric potential difference is the volt, symbolized by capital V, named in honour of Alessandro Volta. One volt represents the potential difference between two points when exactly one joule of energy is expended to transport a charge of one coulomb. A higher voltage exerts a stronger electromotive force, driving charges through resistive pathways.",
    "checkpoints": [
      {
        "question": "What is the SI unit of electric potential difference?",
        "options": [
          "Volt (V)",
          "Ampere (A)",
          "Coulomb (C)",
          "Ohm (\u03a9)"
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
        "hint": "Use the work formula W = V \u00d7 Q.",
        "explanation": "Work done W = V \u00d7 Q = 12 V \u00d7 2 C = 24 Joules (NCERT Example 11.2)."
      }
    ]
  },
  {
    "id": 4,
    "title": "Circuit Diagram Symbols",
    "subtitle": "Voltmeters, Rheostats, and Standard Schematic Conventions",
    "badge": "Section 11.2 & 11.3",
    "summary": "Circuit diagrams provide standardized symbolic representations of electrical networks. A voltmeter measures potential difference and is connected in parallel, while standard symbols represent cells, batteries, switches, resistors, and rheostats.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Voltmeter Parallel Installation:</strong> Potential difference is measured by an instrument called a <span class=\"text-teal-300 font-semibold\">voltmeter</span>. Because it must determine the energy drop across two specific nodes without drawing current, it has an extremely high internal resistance and is <span class=\"text-amber-300 font-semibold\">always connected in parallel</span> across the points of interest.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udcd0</span> Standard Circuit Schematic Symbols (Table 11.1):\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Electric Cell:</strong> Long thin vertical line (positive terminal) paired with a short thick vertical line (negative terminal).</li>\n                        <li><strong class=\"text-teal-300\">Battery of Cells:</strong> Series combination of alternating long and short terminal plates.</li>\n                        <li><strong class=\"text-teal-300\">Plug Key (Switch):</strong> Parentheses `()` for open key (no dot); `(\u00b7)` for closed key with central dot.</li>\n                        <li><strong class=\"text-teal-300\">Wire Joint vs Crossing:</strong> T-junction dot for physical joint; arch bridge symbol for crossing wires without contact.</li>\n                        <li><strong class=\"text-teal-300\">Resistor & Rheostat:</strong> Zig-zag line for fixed resistor; zig-zag with diagonal arrow or slider for variable resistor (rheostat).</li>\n                        <li><strong class=\"text-teal-300\">Ammeter vs Voltmeter:</strong> Encircled `A` with polarity signs (series); encircled `V` with polarity signs (parallel).</li>\n                    </ul>\n                </div>\n            </div>\n        ",
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
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Activity 11.1 Investigation:</strong> Connect a nichrome resistance wire in series with an ammeter, plug key, and an adjustable power source made of 1, 2, 3, or 4 dry cells ($1.5\\text{ V}$ each). A voltmeter is connected in parallel across the nichrome wire.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udd2c</span> Experimental Observations (Table 11.2 Data):\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li>With 1 cell ($V = 1.5\\text{ V}$), current is measured as $I_1$.</li>\n                        <li>With 2 cells ($V = 3.0\\text{ V}$), current doubles to $I_2 = 2 I_1$.</li>\n                        <li>With 3 cells ($V = 4.5\\text{ V}$), current triples to $I_3 = 3 I_1$.</li>\n                        <li>Calculating the ratio $\\frac{V}{I}$ for each trial yields an identical numerical constant within experimental error:\n                            $$\\frac{V}{I} = \\text{Constant} = R$$\n                        </li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Formal Law Statement:</strong> In 1827, German physicist Georg Simon Ohm discovered that the electric current flowing through a metallic wire is <span class=\"text-teal-300 font-semibold\">directly proportional</span> to the potential difference across its ends, provided its temperature remains strictly constant ($V \\propto I$).</p>\n            </div>\n        ",
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
          "It increases nine-fold (3\u00b2)",
          "It remains completely unchanged"
        ],
        "answer": 0,
        "hint": "Current is directly proportional to potential difference (V \u221d I).",
        "explanation": "Because current is directly proportional to voltage (I \u221d V), tripling the potential difference triples the current flowing through the conductor."
      }
    ]
  },
  {
    "id": 6,
    "title": "Current Voltage Graph",
    "subtitle": "Linear V-I Characteristics, The Ohm Unit, and Resistance Concept",
    "badge": "Section 11.4",
    "summary": "Plotting potential difference (V) against current (I) for an ohmic conductor yields a straight line passing through the origin. Resistance is the property of a conductor to resist charge flow; its SI unit is the ohm (\u03a9).",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">The Linear $V\\text{--}I$ Graph:</strong> When the experimental data from Activity 11.1 are plotted with potential difference $V$ on the vertical y-axis and current $I$ on the horizontal x-axis, the resulting curve is a <span class=\"text-teal-300 font-semibold\">straight line passing through the origin</span> $(0,0)$.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udcc8</span> Slope & Resistance Interpretation:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Slope Equals Resistance:</strong> The slope of the $V\\text{--}I$ graph represents the electrical resistance of the metallic conductor:\n                            $$\\text{Slope} = \\frac{\\Delta V}{\\Delta I} = R$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Physical Origin of Resistance:</strong> Electrons drifting through a metal collide repeatedly with vibrating positive lattice ions, dissipating kinetic energy and impeding flow.</li>\n                        <li><strong class=\"text-teal-300\">The Ohm ($\\Omega$):</strong> SI unit of resistance, denoted by Greek letter omega ($\\Omega$). One ohm is the resistance of a conductor carrying a current of $1\\text{ A}$ under a potential difference of $1\\text{ V}$:\n                            $$1\\ \\Omega = \\frac{1\\text{ V}}{1\\text{ A}}$$\n                        </li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Inverse Current Relation:</strong> From $I = V/R$, current is inversely proportional to resistance. Doubling circuit resistance cuts current by half for a fixed voltage.</p>\n            </div>\n        ",
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
        "hint": "Slope = \u0394V / \u0394I. Recall Ohm's law formula R = V/I.",
        "explanation": "In a V-I graph, the slope is \u0394V / \u0394I, which equals the electrical resistance (R) of the conductor."
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
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Activity 11.3 Experimental Tests:</strong> In a circuit powered by a fixed battery, insert different test wires and measure current with an ammeter:</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udccf</span> Empirical Dependencies of Resistance:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Length ($l$):</strong> Doubling wire length ($2l$) cuts current in half, proving resistance is directly proportional to length:\n                            $$R \\propto l$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Cross-Sectional Area ($A$):</strong> Using a thicker wire of identical material and length increases current, proving resistance is inversely proportional to cross-sectional area:\n                            $$R \\propto \\frac{1}{A}$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Material Composition:</strong> Wires of identical length and cross-section made of copper, nichrome, and iron conduct vastly different currents, showing resistance depends fundamentally on material nature.</li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Combined Proportionality:</strong> Combining these empirical geometric factors gives:\n                    $$R \\propto \\frac{l}{A} \\implies R = \\rho \\frac{l}{A}$$\n                where $\\rho$ is the constant of proportionality termed electrical resistivity.</p>\n            </div>\n        ",
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
        "hint": "Resistance is directly proportional to length (R \u221d l).",
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
        "hint": "Recall that resistance is inversely proportional to cross-sectional area (R \u221d 1/A).",
        "explanation": "A larger cross-sectional area provides more parallel conduction channels for electrons, decreasing resistance (R \u221d 1/A) and allowing greater current flow."
      }
    ]
  },
  {
    "id": 8,
    "title": "Electrical Resistivity Spectrum",
    "subtitle": "Material Properties, Ohm-Metre Unit, and Heating Device Alloys",
    "badge": "Section 11.5",
    "summary": "Electrical resistivity (\u03c1) is an intrinsic material property measured in ohm-metres (\u03a9\u00b7m). Metals have very low resistivity, insulators have enormous resistivity, and alloys with high resistivity and non-oxidizing properties are used in electric heating elements.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Definition of Electrical Resistivity ($\\rho$):</strong> From the resistance formula $R = \\rho \\frac{l}{A}$, isolating resistivity yields:</p>\n                <div class=\"p-2 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-cyan-300 text-xs\">\n                    $$\\rho = \\frac{R \\times A}{l} \\implies \\text{Unit: } \\frac{\\Omega \\times \\text{m}^2}{\\text{m}} = \\Omega\\cdot\\text{m}$$\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udcca</span> Resistivity Classification (Table 11.2):\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Conductors ($10^{-8} \\text{ to } 10^{-6}\\ \\Omega\\cdot\\text{m}$):</strong> Silver ($\\rho = 1.60 \\times 10^{-8}\\ \\Omega\\cdot\\text{m}$) is the best electrical conductor, followed by copper and aluminium, which are used for electrical transmission lines.</li>\n                        <li><strong class=\"text-teal-300\">Alloys ($10^{-6}\\ \\Omega\\cdot\\text{m}$):</strong> Nichrome, constantan, and manganin have higher resistivities than their constituent metals. Crucially, alloys <span class=\"text-rose-400 font-semibold\">do not oxidize (burn) easily at high temperatures</span>, making them ideal for heating coils in toasters, geysers, and electric irons.</li>\n                        <li><strong class=\"text-teal-300\">Insulators ($10^{12} \\text{ to } 10^{17}\\ \\Omega\\cdot\\text{m}$):</strong> Glass, hard rubber, and ebonite prevent charge transport entirely.</li>\n                        <li><strong class=\"text-teal-300\">Tungsten Filaments:</strong> High melting point ($3380^\\circ\\text{C}$) makes tungsten indispensable for glowing incandescent bulb filaments.</li>\n                    </ul>\n                </div>\n            </div>\n        ",
    "speech": "We now examine electrical resistivity, symbolized by the Greek letter rho, which measures a material's intrinsic opposition to electric charge flow regardless of physical dimensions. While resistance R depends on both geometry and material, resistivity rho is an inherent physical constant of the material at a given temperature. The SI unit of electrical resistivity is the ohm-metre. Examining Table 11.2 reveals that materials span an astonishing twenty orders of magnitude in resistivity. Metals such as silver, copper, and aluminium exhibit exceptionally low resistivities in the range of ten to the power of minus eight to ten to the power of minus six ohm-metres, making them outstanding choices for long-distance power transmission cables. In contrast, electrical insulators such as glass, rubber, and plastics possess colossal resistivities ranging from ten to the power of twelve to ten to the power of seventeen ohm-metres. Alloys such as nichrome occupy an intermediate bracket. Nichrome exhibits much higher resistivity than its constituent pure metals and possesses the vital property that it does not oxidize or burn easily even when glowing red-hot at high temperatures. Consequently, alloys are universally employed to construct the heating elements of electric irons, toasters, and room heaters.",
    "checkpoints": [
      {
        "question": "What is the SI unit of electrical resistivity?",
        "options": [
          "Ohm-metre (\u03a9\u00b7m)",
          "Ohm per metre (\u03a9/m)",
          "Volt per ampere (V/A)",
          "Coulomb per second (C/s)"
        ],
        "answer": 0,
        "hint": "From \u03c1 = R \u00d7 A / l, evaluate the unit dimension (\u03a9 \u00d7 m\u00b2 / m).",
        "explanation": "The SI unit of resistivity is the ohm-metre (\u03a9\u00b7m)."
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
  },
  {
    "id": 9,
    "title": "Series Resistor Circuits",
    "subtitle": "Current Invariance, Potential Difference Division, and Rs Derivation",
    "badge": "Section 11.6.1",
    "summary": "In a series circuit, resistors are joined end-to-end. The exact same current flows through each resistor, while the total applied potential difference divides across them. The equivalent series resistance is the direct algebraic sum: Rs = R1 + R2 + R3.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Activities 11.4 & 11.5 Findings:</strong> When three resistors $R_1, R_2, R_3$ are connected end-to-end in series across a battery of voltage $V$:</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\u26d3\ufe0f</span> Fundamental Laws of Series Combinations:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Uniform Current ($I$):</strong> An ammeter inserted anywhere in the series loop measures the identical current magnitude. Charges have only a single, undivided pathway:\n                            $$I = I_1 = I_2 = I_3$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Voltage Division ($V$):</strong> A voltmeter across each individual resistor reads $V_1, V_2, V_3$. The total potential difference equals the sum of individual voltage drops:\n                            $$V = V_1 + V_2 + V_3$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Equivalent Resistance ($R_s$) Derivation:</strong> Applying Ohm's law ($V = I R_s$, $V_1 = I R_1$, $V_2 = I R_2$, $V_3 = I R_3$):\n                            $$I R_s = I R_1 + I R_2 + I R_3 \\implies R_s = R_1 + R_2 + R_3$$\n                        </li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Key Characteristic:</strong> The equivalent resistance $R_s$ of any series combination is always greater than the largest individual resistance in the combination.</p>\n            </div>\n        ",
    "speech": "We now investigate the behaviour of electric circuits when multiple resistors are linked together in a series combination. When two or more resistors are joined end-to-end consecutively, they form a single conducting pathway across a common direct current power source. In Activities 11.4 and 11.5, we discover two cardinal rules governing all series connections. First, when an ammeter is repositioned between different resistors in a series loop, it records the exact same value of electric current throughout. Because there are no alternative branch paths, the current I remains strictly uniform through every component in the chain. Second, when measuring potential difference with a voltmeter across individual resistors, we find that the total battery voltage V splits into fractional voltage drops across each resistor, such that V equals V1 plus V2 plus V3. Applying Ohm's law to each component, we replace V with I multiplied by equivalent resistance Rs, and individual voltages with I times each corresponding resistance. Dividing the resulting algebraic expression by the common uniform current I establishes the fundamental the celebrated series resistance formula: Rs equals R1 plus R2 plus R3. The equivalent resistance of a series network is always strictly greater than any individual resistance in the chain.",
    "checkpoints": [
      {
        "question": "What happens to the electric current as it traverses three resistors connected in series?",
        "options": [
          "It remains exactly the same through all three resistors",
          "It divides equally into three separate parts",
          "It increases after passing through each resistor",
          "It drops to zero at the middle resistor"
        ],
        "answer": 0,
        "hint": "In a series circuit, there is only one continuous path for flowing charge.",
        "explanation": "In a series circuit, current is uniform throughout because charge cannot accumulate or branch off along the single pathway."
      },
      {
        "question": "Three resistors of values 2 \u03a9, 3 \u03a9, and 5 \u03a9 are connected in series. What is their equivalent resistance?",
        "options": [
          "10 \u03a9",
          "0.97 \u03a9",
          "1 \u03a9",
          "30 \u03a9"
        ],
        "answer": 0,
        "hint": "Use the series formula Rs = R1 + R2 + R3.",
        "explanation": "Rs = 2 \u03a9 + 3 \u03a9 + 5 \u03a9 = 10 \u03a9."
      }
    ]
  },
  {
    "id": 10,
    "title": "Series Circuit Analysis",
    "subtitle": "Worked Example 11.7, Component Voltage Drops, and Single-Point Failure",
    "badge": "Section 11.6.1",
    "summary": "NCERT Example 11.7 demonstrates calculating total series resistance, current, and individual voltage drops for an electric lamp and conductor connected to a 6 V battery. A major disadvantage of series circuits is that if one component fails, the entire circuit is broken.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Worked Example 11.7 Walkthrough:</strong> An electric lamp of resistance $R_1 = 20\\ \\Omega$ and a conductor of resistance $R_2 = 4\\ \\Omega$ are connected in series to a $6\\text{ V}$ battery (Figure 11.9):</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udd22</span> Mathematical Analysis:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Total Resistance ($R_s$):</strong>\n                            $$R_s = R_1 + R_2 = 20\\ \\Omega + 4\\ \\Omega = 24\\ \\Omega$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Total Circuit Current ($I$):</strong>\n                            $$I = \\frac{V}{R_s} = \\frac{6\\text{ V}}{24\\ \\Omega} = 0.25\\text{ A}$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Voltage Across Lamp ($V_1$):</strong>\n                            $$V_1 = I \\times R_1 = 0.25\\text{ A} \\times 20\\ \\Omega = 5\\text{ V}$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Voltage Across Conductor ($V_2$):</strong>\n                            $$V_2 = I \\times R_2 = 0.25\\text{ A} \\times 4\\ \\Omega = 1\\text{ V}$$\n                        </li>\n                    </ul>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30 space-y-1 text-rose-200\">\n                    <div class=\"text-rose-400 font-bold flex items-center gap-1.5\">\n                        <span>\u26a0\ufe0f</span> Disadvantages of Series Connections:\n                    </div>\n                    <p>If any single component in a series chain burns out (e.g., one bulb in decorative festive fairy lights), the entire circuit breaks and all lights extinguish simultaneously. Furthermore, appliances requiring different currents cannot function effectively in series.</p>\n                </div>\n            </div>\n        ",
    "speech": "Let us examine a numerical application of series circuits through worked Example 11.7 from the textbook. Suppose an electric lamp with a resistance of twenty ohms is connected in series with a four-ohm resistor across a six-volt battery. First, we compute the total equivalent resistance of the circuit by summing the individual values, yielding twenty plus four equals twenty-four ohms. Next, using Ohm's law, the circuit current is calculated by dividing the total battery potential of six volts by the twenty-four-ohm equivalent resistance, giving zero point two five amperes. Because current is uniform throughout the series loop, zero point two five amperes passes through both the lamp and the resistor. Applying Ohm's law to each component reveals that the potential difference across the lamp is zero point two five times twenty, which equals five volts, while across the conductor it is zero point two five times four, which equals one volt. Notice that five volts plus one volt equals the six-volt battery supply. Despite its mathematical simplicity, series wiring has severe practical drawbacks in domestic installations. If one component fails or burns out, such as a single bulb in festive fairy lights, the entire circuit is broken and all connected appliances cease operating.",
    "checkpoints": [
      {
        "question": "In a series circuit with a 20 \u03a9 lamp and a 4 \u03a9 resistor powered by a 6 V battery, what is the current?",
        "options": [
          "0.25 A",
          "4.0 A",
          "1.5 A",
          "0.50 A"
        ],
        "answer": 0,
        "hint": "Find total resistance Rs = 20 + 4 = 24 \u03a9, then use I = V / Rs.",
        "explanation": "Total resistance Rs = 24 \u03a9. Current I = V / Rs = 6 V / 24 \u03a9 = 0.25 A (NCERT Example 11.7)."
      },
      {
        "question": "What is a major practical disadvantage of wiring domestic household appliances in series?",
        "options": [
          "If one appliance fails or is turned off, all other appliances stop working",
          "The equivalent resistance drops to zero, causing short circuits",
          "The battery voltage increases uncontrollably",
          "All appliances draw identical high currents of 100 amperes"
        ],
        "answer": 0,
        "hint": "Consider the effect of a break in a single continuous circuit path.",
        "explanation": "In a series circuit, if any single device fails or is switched off, the entire circuit path is opened and all appliances shut down."
      }
    ]
  },
  {
    "id": 11,
    "title": "Parallel Resistor Circuits",
    "subtitle": "Voltage Invariance, Current Splitting, and Reciprocal Rp Formula",
    "badge": "Section 11.6.2",
    "summary": "In a parallel circuit, resistors are connected across the same two common nodes. The potential difference across each branch is identical, while total current splits among branches. The reciprocal of equivalent resistance is the sum of reciprocals: 1/Rp = 1/R1 + 1/R2 + 1/R3.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Activity 11.6 Circuit Dynamics:</strong> In a parallel combination, three resistors $R_1, R_2, R_3$ are joined across common junction nodes $X$ and $Y$ across a battery of voltage $V$ (Figures 11.7 & 11.10):</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udd00</span> Fundamental Laws of Parallel Combinations:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Uniform Potential Difference ($V$):</strong> A voltmeter connected across common nodes $X$ and $Y$ measures the exact same voltage $V$ across every parallel branch:\n                            $$V = V_1 = V_2 = V_3$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Current Division ($I$):</strong> Total current $I$ entering junction $X$ splits into separate branch currents $I_1, I_2, I_3$, recombining at junction $Y$:\n                            $$I = I_1 + I_2 + I_3$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Equivalent Resistance ($R_p$) Derivation:</strong> Applying Ohm's law ($I = V/R_p$, $I_1 = V/R_1$, $I_2 = V/R_2$, $I_3 = V/R_3$):\n                            $$\\frac{V}{R_p} = \\frac{V}{R_1} + \\frac{V}{R_2} + \\frac{V}{R_3} \\implies \\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$$\n                        </li>\n                    </ul>\n                </div>\n                <p><strong class=\"text-amber-400\">Key Characteristic:</strong> The equivalent resistance $R_p$ of a parallel combination is always <span class=\"text-teal-300 font-semibold\">less than the smallest individual resistance</span> in the network.</p>\n            </div>\n        ",
    "speech": "We now examine the second primary circuit configuration: resistors connected in parallel. In a parallel circuit, two or more resistors are linked in parallel between two common junction points, providing multiple independent parallel conduits for circulating charges. In Activity 11.6, we establish the two defining laws of parallel circuits. First, the applied electric potential difference across every parallel branch is strictly identical and equals the terminal voltage supplied by the battery. A voltmeter placed across any branch reads the exact same voltage V. Second, the total electric current I entering the main circuit junction splits among the branches according to their individual resistances. By the conservation of electrical charge, total current I equals I1 plus I2 plus I3. Applying Ohm's law, each branch current is expressed as the common voltage V divided by that branch's resistance. Factoring out voltage V from both sides leads to the fundamental reciprocal parallel formula: one divided by Rp equals one divided by R1 plus one divided by R2 plus one divided by R3. A remarkable property of parallel circuits is that the equivalent resistance Rp is always smaller than the lowest individual resistor in the combination, greatly reducing the overall opposition to circulating electric current flow.",
    "checkpoints": [
      {
        "question": "What quantity remains constant across all individual branches in a parallel circuit?",
        "options": [
          "Potential difference (voltage)",
          "Electric current in amperes",
          "Physical temperature of wires",
          "Mass of copper atoms"
        ],
        "answer": 0,
        "hint": "All branches connect across the exact same pair of electrical nodes.",
        "explanation": "Because all branches connect directly across the same two junction nodes, the potential difference (voltage) is identical across every parallel branch."
      },
      {
        "question": "Two resistors of 3 \u03a9 and 6 \u03a9 are connected in parallel. What is their equivalent resistance?",
        "options": [
          "2 \u03a9",
          "9 \u03a9",
          "4.5 \u03a9",
          "18 \u03a9"
        ],
        "answer": 0,
        "hint": "Use 1/Rp = 1/3 + 1/6 = 2/6 + 1/6 = 3/6 = 1/2.",
        "explanation": "1/Rp = 1/3 + 1/6 = 3/6 = 1/2 \u03a9\u207b\u00b9, so Rp = 2 \u03a9. Notice that 2 \u03a9 is less than the smallest resistor (3 \u03a9)."
      }
    ]
  },
  {
    "id": 12,
    "title": "Parallel Circuit Advantages",
    "subtitle": "Independent Branch Control, Reduced Total Resistance, and Domestic Wiring",
    "badge": "Section 11.6.2",
    "summary": "Parallel circuits offer immense advantages in domestic wiring: independent on/off switches for each device, full supply voltage (220 V) across all appliances, and branch currents tailored to individual power ratings without total circuit shutdown if one fails.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Why Domestic Wiring is Parallel:</strong> In household electrical circuits, appliances are never connected in series; they are universally wired in <span class=\"text-teal-300 font-semibold\">parallel across the mains supply</span> ($220\\text{ V}$ in India).</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83c\udfe1</span> Four Key Advantages of Parallel Circuits:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">1. Independent Switching:</strong> Each appliance has its own dedicated switch. Turning off a bedroom light does not shut down the refrigerator or ceiling fan.</li>\n                        <li><strong class=\"text-teal-300\">2. Uniform Voltage Rating:</strong> Every appliance receives the full rated line potential difference ($220\\text{ V}$), allowing optimal designed performance.</li>\n                        <li><strong class=\"text-teal-300\">3. Tailored Current Allocation:</strong> Different devices require vastly different currents (e.g., electric heater draws $10\\text{ A}$, while an LED bulb draws $0.05\\text{ A}$). Parallel branches draw current independently according to their resistance ($I = V/R$).</li>\n                        <li><strong class=\"text-teal-300\">4. Fault Isolation:</strong> If one appliance develops a short circuit or burns its filament, other branches remain fully energized and continue operating normally.</li>\n                    </ul>\n                </div>\n            </div>\n        ",
    "speech": "Understanding the profound operational contrast between series and parallel circuits explains why modern household wiring is universally configured and installed in parallel. Imagine a home where all appliances were wired in series. If you switched off the television in your living room, the refrigerator, ceiling fans, and bedroom lights would shut down simultaneously because the single conduction path would be broken. In stark contrast, a parallel electrical wiring scheme offers four indispensable advantages. First, every individual appliance possesses its own dedicated switch, allowing independent control without disrupting other devices in the building. Second, each parallel branch connects directly across the full, stable mains supply voltage of two hundred and twenty volts, ensuring that every electrical device operates at its optimal designed potential. Third, different household appliances demand vastly different operating currents to function correctly; for example, an electric water heater requires ten amperes, while an energy-efficient light bulb needs only a fraction of an ampere. Parallel branches naturally allocate appropriate current levels inversely proportional to appliance resistance. Fourth, if an individual device suffers an electrical fault or a filament burns out, only that specific branch is deactivated, leaving the rest of the household circuit operating safely and uninterrupted.",
    "checkpoints": [
      {
        "question": "Why is parallel wiring universally used for household domestic electrical installations?",
        "options": [
          "Each appliance can be operated independently at full supply voltage",
          "It forces all appliances to share a single common switch",
          "It increases total circuit resistance to reduce electric bills",
          "It prevents electrons from moving through metallic cables"
        ],
        "answer": 0,
        "hint": "Consider convenience, safety, and operating voltage requirements in a home.",
        "explanation": "Parallel circuits give each appliance full supply voltage (220 V), allow independent switching, and ensure other devices keep working if one fails."
      },
      {
        "question": "How does connecting additional appliances in parallel affect the total equivalent resistance of a house circuit?",
        "options": [
          "Total equivalent resistance decreases",
          "Total equivalent resistance increases",
          "Total equivalent resistance remains perfectly constant",
          "Total equivalent resistance becomes infinite"
        ],
        "answer": 0,
        "hint": "Adding more parallel branches adds more pathways for current to flow.",
        "explanation": "In parallel combinations (1/Rp = \u03a3 1/Ri), adding branches provides more conduction paths, reducing the total equivalent resistance."
      }
    ]
  },
  {
    "id": 13,
    "title": "Joules Heating Law",
    "subtitle": "Work Dissipation, Thermal Energy Formula, and Square of Current",
    "badge": "Section 11.7",
    "summary": "When electric current flows through a purely resistive conductor, electrical energy is converted entirely into heat due to lattice electron collisions. Joule's law of heating states that heat produced is directly proportional to I\u00b2Rt.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Origin of Heating Effect:</strong> A battery maintains a potential difference across a conductor. To transport charge $Q$ across voltage $V$, the source performs work $W = V \\times Q$. If this energy is not used for mechanical work (as in a motor), it is dissipated entirely as <span class=\"text-rose-400 font-semibold\">thermal energy (heat)</span>.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udd25</span> Derivation of Joule's Law:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li>Power input supplied by the source is:\n                            $$P = \\frac{W}{t} = \\frac{V \\times Q}{t} = V \\times I$$\n                        </li>\n                        <li>Total heat energy ($H$) dissipated in time $t$ in a purely resistive circuit is:\n                            $$H = P \\times t = V \\times I \\times t$$\n                        </li>\n                        <li>Substituting Ohm's law ($V = IR$) into the energy equation:\n                            $$H = (IR) \\times I \\times t \\implies H = I^2 R t$$\n                        </li>\n                    </ul>\n                </div>\n                <div class=\"p-2 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-amber-300 text-xs\">\n                    $$H \\propto I^2 \\quad | \\quad H \\propto R \\quad | \\quad H \\propto t$$\n                </div>\n                <p><strong class=\"text-amber-400\">Joule's Law of Heating:</strong> Heat produced in a resistor is directly proportional to: (1) the <span class=\"text-rose-400 font-semibold\">square of current</span> ($I^2$); (2) resistance ($R$); and (3) time ($t$).</p>\n            </div>\n        ",
    "speech": "We now examine the heating effect of electric current and Joule's universal law of heating. When an electric current flows through a conductor, the chemical energy stored within the electrochemical battery does work to drive charges across the circuit. If the circuit is purely resistive, consisting only of resistance elements like nichrome coils without any mechanical motors, the supplied electrical energy cannot be converted into macroscopic kinetic motion. Instead, as drifting electrons collide continuously with the vibrating atoms of the metal crystal lattice, their kinetic energy is transformed entirely into microscopic thermal vibrations, causing the conductor to heat up. British physicist James Prescott Joule established the exact mathematical law governing this thermal dissipation. Starting from the electrical work definition, energy equals power multiplied by time, which equals potential difference V times current I times elapsed time t. Substituting Ohm's law, where V equals I times R, gives the famous formula: H equals I squared multiplied by R multiplied by t. Joule's law states that the thermal heat produced in a resistor is directly proportional to the square of the current, directly proportional to the electrical resistance, and directly proportional to the total time duration for which the current flows.",
    "checkpoints": [
      {
        "question": "If the electric current flowing through a fixed resistor is doubled, by what factor does the heat produced per second increase?",
        "options": [
          "It increases by a factor of 4 (quadruples)",
          "It doubles (increases by a factor of 2)",
          "It increases by a factor of 8",
          "It remains exactly constant"
        ],
        "answer": 0,
        "hint": "Recall that heat is proportional to the square of current (H \u221d I\u00b2).",
        "explanation": "According to Joule's law (H \u221d I\u00b2), doubling current results in 2\u00b2 = 4 times the heat generated per second."
      },
      {
        "question": "An electric iron of resistance 20 \u03a9 carries a current of 5 A for 30 seconds. How much heat is produced?",
        "options": [
          "15,000 J (1.5 \u00d7 10\u2074 J)",
          "3,000 J",
          "300 J",
          "75,000 J"
        ],
        "answer": 0,
        "hint": "Apply Joule's law formula H = I\u00b2Rt: H = 5\u00b2 \u00d7 20 \u00d7 30.",
        "explanation": "H = I\u00b2Rt = (5 A)\u00b2 \u00d7 20 \u03a9 \u00d7 30 s = 25 \u00d7 20 \u00d7 30 = 15,000 Joules (15 kJ)."
      }
    ]
  },
  {
    "id": 14,
    "title": "Thermal Appliance Applications",
    "subtitle": "Electric Heating Elements, Tungsten Filaments, and Inactive Gases",
    "badge": "Section 11.7.1",
    "summary": "Practical applications of Joule's heating include electric irons, toasters, and room heaters using high-resistivity non-oxidizing alloys. In incandescent lamps, high-melting-point tungsten (3380\u00b0C) glows to emit light, protected by inert nitrogen and argon gases.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Heating Appliances:</strong> Devices such as electric laundry irons, electric toasters, electric ovens, water geysers, and room heaters rely directly on the heating effect of electric current.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udca1</span> The Physics of Incandescent Bulbs:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Tungsten Filament:</strong> The filament must retain as much generated heat as possible to reach white-hot incandescence without melting. <span class=\"text-amber-300 font-semibold\">Tungsten</span> has an exceptionally high melting point of <span class=\"text-rose-400 font-bold\">3380\u00b0C</span>.</li>\n                        <li><strong class=\"text-teal-300\">Thermal Isolation:</strong> The filament is thermally isolated using thick supports and a vacuum or gas-filled glass envelope.</li>\n                        <li><strong class=\"text-teal-300\">Inactive Gas Filling:</strong> Bulbs are chemically filled with inactive gases like <span class=\"text-teal-300 font-semibold\">nitrogen ($N_2$) and argon ($Ar$)</span> to prevent filament oxidation and prolong operational lifespan.</li>\n                        <li><strong class=\"text-teal-300\">Power Inefficiency:</strong> Most electrical power consumed by an incandescent filament is radiated as invisible heat; only a small fraction is radiated as visible light.</li>\n                    </ul>\n                </div>\n            </div>\n        ",
    "speech": "The heating effect of electric current finds indispensable and wide-ranging practical applications across everyday domestic and industrial technology. Common household domestic appliances such as electric laundry irons, toasters, kettles, and room heaters contain specialized heating elements made of alloys like nichrome. When electric current passes through, the high resistance of the heating element generates intense heat, while the low-resistance copper connecting cord remains safely cool to the touch. Another classic application of Joule's heating is the incandescent electric light bulb. In a light bulb, the filament must retain thermal energy to achieve extreme temperatures, glowing white-hot with brilliant luminosity so that it emits visible light. To withstand such intense temperatures without melting, filaments are crafted exclusively from pure metallic tungsten, which possesses an exceptionally high melting point benchmark of three thousand three hundred and eighty degrees Celsius. To prevent the glowing tungsten filament from rapidly oxidizing and vaporizing in air, the glass bulb is evacuated and carefully filled with chemically inert gases, typically an inactive mixture of nitrogen and argon. These inert gases suppress tungsten evaporation and significantly prolong the functional lifespan of the bulb, although most energy is radiated as heat rather than light.",
    "checkpoints": [
      {
        "question": "Why is tungsten metal exclusively used for the filaments of incandescent electric lamps?",
        "options": [
          "It has an extraordinarily high melting point of 3380\u00b0C",
          "It has the lowest electrical resistance among all metals",
          "It is completely transparent to visible light rays",
          "It generates electrical power without requiring a battery"
        ],
        "answer": 0,
        "hint": "The filament must reach white-hot temperatures without melting.",
        "explanation": "Tungsten has an extremely high melting point (3380\u00b0C), allowing it to glow white-hot and emit visible light without melting."
      },
      {
        "question": "Which gases are filled inside incandescent electric bulbs to prolong filament lifespan?",
        "options": [
          "Chemically inactive nitrogen and argon",
          "Flammable hydrogen and methane",
          "Pure reactive oxygen gas",
          "Corrosive chlorine gas"
        ],
        "answer": 0,
        "hint": "Inert, non-reactive gases prevent hot tungsten from oxidizing.",
        "explanation": "Electric bulbs are filled with chemically inactive gases like nitrogen and argon to prevent oxidation of the tungsten filament, greatly extending its life."
      }
    ]
  },
  {
    "id": 15,
    "title": "Electric Fuse Protection",
    "subtitle": "Series Circuit Shield, Low Melting Alloys, and Fuse Current Ratings",
    "badge": "Section 11.7.1",
    "summary": "An electric fuse is a critical safety device connected in series to protect circuits and appliances from overcurrent and short circuits. It consists of a lead-tin alloy wire that safely melts and breaks the circuit when current exceeds its designated rating.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">The Fuse Safety Mechanism:</strong> An electric fuse is a sacrificial protective device inserted in <span class=\"text-teal-300 font-semibold\">series with the live wire</span> of a circuit. It protects domestic wiring and expensive appliances from dangerous current surges and accidental short circuits.</p>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\ud83d\udee1\ufe0f</span> Operating Principle & Construction:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">Alloy Composition:</strong> A piece of wire made of a metal or alloy with an appropriate <span class=\"text-rose-400 font-semibold\">low melting point</span> (e.g., lead-tin alloy, aluminium, copper, or lead).</li>\n                        <li><strong class=\"text-teal-300\">Thermal Meltdown:</strong> If a current larger than the specified rating flows through the circuit, Joule heating ($H = I^2 Rt$) raises the temperature of the fuse wire above its melting point. The wire melts and breaks the circuit path immediately.</li>\n                        <li><strong class=\"text-teal-300\">Standard Ratings:</strong> Fuses for domestic usage are rated at $1\\text{ A}, 2\\text{ A}, 3\\text{ A}, 5\\text{ A}, 10\\text{ A}$, and $16\\text{ A}$.</li>\n                        <li><strong class=\"text-teal-300\">Fuse Calculation Example:</strong> An electric iron consuming $1\\text{ kW}$ ($1000\\text{ W}$) at $220\\text{ V}$ operates with current:\n                            $$I = \\frac{P}{V} = \\frac{1000\\text{ W}}{220\\text{ V}} = 4.54\\text{ A}$$\n                            A <span class=\"text-amber-300 font-semibold\">5 A fuse</span> must be chosen to provide safe, reliable protection.\n                        </li>\n                    </ul>\n                </div>\n            </div>\n        ",
    "speech": "Another crucial protective application of Joule's heating effect is the electric fuse, an essential safety device designed to protect home electrical circuits and costly household appliances against sudden dangerous current overloads. An electric fuse consists of a short segment of thin wire made from a metallic alloy having an appropriately calibrated low melting point, typically a lead-tin alloy. The fuse is always installed strictly in series with the live incoming wire of the electrical circuit, encased safely within a fireproof ceramic cartridge with metal end caps. Under normal operating conditions, the regular current flowing through the circuit generates minimal heat, leaving the fuse wire intact. However, if a sudden electrical fault occurs, such as a short circuit or an unexpected power surge, the current skyrockets to dangerous levels. According to Joule's law, heat generated increases with the square of the current. This rapid thermal surge raises the fuse wire temperature beyond its melting point within milliseconds. The fuse wire melts, severing the physical conduction pathway completely and disconnecting the power supply before the surging current can ignite electrical fires or destroy connected appliances. Standard domestic fuses are rated at values such as one, two, three, five, or ten amperes.",
    "checkpoints": [
      {
        "question": "How is an electric fuse connected in an electrical circuit, and what is its working principle?",
        "options": [
          "Connected in series; melts and breaks the circuit upon overcurrent",
          "Connected in parallel; absorbs magnetic fields during lightening",
          "Connected to the earth wire; converts alternating current to direct current",
          "Connected outside the building; amplifies incoming voltage"
        ],
        "answer": 0,
        "hint": "The fuse acts as a sacrificial gatekeeper in the main conduction path.",
        "explanation": "An electric fuse is connected in series with the circuit; when current exceeds its rated limit, Joule heating melts the wire, opening the circuit safely."
      },
      {
        "question": "An electric iron consumes 1000 W power when operated on a 220 V line. What fuse rating is appropriate?",
        "options": [
          "5 A fuse",
          "1 A fuse",
          "2 A fuse",
          "25 A fuse"
        ],
        "answer": 0,
        "hint": "Calculate operating current I = P / V = 1000 / 220 \u2248 4.54 A.",
        "explanation": "Current I = 1000 W / 220 V \u2248 4.54 A. Therefore, the next higher standard rating of 5 A must be chosen (NCERT Section 11.7.1)."
      }
    ]
  },
  {
    "id": 16,
    "title": "Electric Power Rating",
    "subtitle": "Power Formulas, The Watt, Commercial kWh Units, and Energy Tariffs",
    "badge": "Section 11.8",
    "summary": "Electric power is the rate at which electrical energy is consumed in an electric circuit (P = VI = I\u00b2R = V\u00b2/R). Its SI unit is the Watt. The commercial unit of electrical energy is the kilowatt-hour (1 kWh = 3.6 \u00d7 10\u2076 J), commonly termed a 'unit'.",
    "theory": "\n            <div class=\"space-y-3 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Definition of Electric Power ($P$):</strong> Electric power is defined as the rate at which electrical energy is consumed or dissipated in an electrical circuit:</p>\n                <div class=\"p-2 rounded-lg bg-slate-800/80 border border-slate-700/80 text-center font-mono text-cyan-300 text-xs\">\n                    $$P = \\frac{W}{t} = V \\times I = I^2 R = \\frac{V^2}{R}$$\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-800/80 border border-slate-700/80 space-y-1.5\">\n                    <div class=\"text-amber-300 font-bold flex items-center gap-1.5\">\n                        <span>\u26a1</span> Units of Power & Commercial Electrical Energy:\n                    </div>\n                    <ul class=\"list-disc list-inside space-y-1 text-slate-300 pl-1\">\n                        <li><strong class=\"text-teal-300\">The Watt ($1\\text{ W}$):</strong> Power consumed by a device carrying $1\\text{ A}$ current at $1\\text{ V}$ potential difference ($1\\text{ W} = 1\\text{ V} \\times 1\\text{ A}$). Larger unit: $1\\text{ kW} = 1000\\text{ W}$.</li>\n                        <li><strong class=\"text-teal-300\">Commercial Energy Unit (Kilowatt-Hour):</strong> The joule is too small for commercial billing. The commercial unit of electrical energy is the <span class=\"text-amber-300 font-semibold\">kilowatt-hour (kWh)</span>, commonly called a 'unit':\n                            $$1\\text{ kWh} = 1\\text{ kW} \\times 1\\text{ h} = 1000\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^6\\text{ Joules (J)}$$\n                        </li>\n                        <li><strong class=\"text-teal-300\">Billing Example 11.13:</strong> A $400\\text{ W}$ refrigerator running $8\\text{ h/day}$ for $30\\text{ days}$ consumes:\n                            $$E = 400\\text{ W} \\times 8\\text{ h/day} \\times 30\\text{ days} = 96,000\\text{ Wh} = 96\\text{ kWh}$$\n                            At $\\text{Rs } 3.00\\text{ per kWh}$, total cost is $96 \\times 3.00 = \\text{Rs } 288.00$.\n                        </li>\n                    </ul>\n                </div>\n            </div>\n        ",
    "speech": "We conclude our theoretical journey by examining electric power, the rate at which electrical energy is delivered, consumed, or converted into other forms of energy within an electrical circuit. Electric power P is defined as the work done per unit time. By combining fundamental circuit relationships, power is expressed in three equivalent mathematical equations: P equals voltage V times current I, P equals I squared multiplied by resistance R, and P equals voltage squared divided by resistance R. The SI unit of electric power is the watt, symbolized by W, named after James Watt. One watt represents the power consumed by an appliance that carries a current of one ampere when operated under a potential difference of one volt. Because a watt is a relatively small unit, power companies utilize the kilowatt, which equals one thousand watts. When calculating domestic electricity bills, energy is measured in the commercial unit called the kilowatt-hour, popularly referred to as a unit of electricity. One kilowatt-hour represents the total energy consumed by an appliance operating at one thousand watts for one full hour, which equals exactly three point six million joules. We pay utility companies for this electrical energy that drives charges through our appliances.",
    "checkpoints": [
      {
        "question": "Which of the following mathematical expressions correctly represents electrical power?",
        "options": [
          "P = VI = I\u00b2R = V\u00b2/R",
          "P = V/I = IR\u00b2",
          "P = I/V = VR\u00b2",
          "P = V\u00b2I = I/R"
        ],
        "answer": 0,
        "hint": "Recall the three standard equivalent power formulas derived in Section 11.8.",
        "explanation": "Electric power is given by P = VI, and using Ohm's law, it can also be expressed as P = I\u00b2R or P = V\u00b2/R."
      },
      {
        "question": "How many joules of energy are equal to one kilowatt-hour (1 kWh) of electricity?",
        "options": [
          "3.6 \u00d7 10\u2076 J",
          "3.6 \u00d7 10\u00b3 J",
          "1.0 \u00d7 10\u2075 J",
          "6.0 \u00d7 10\u2074 J"
        ],
        "answer": 0,
        "hint": "Convert 1 kilowatt to 1000 watts and 1 hour to 3600 seconds, then multiply.",
        "explanation": "1 kWh = 1000 W \u00d7 3600 s = 3,600,000 Joules = 3.6 \u00d7 10\u2076 J."
      }
    ]
  },
  {
    "id": 17,
    "title": "Current Potential Review",
    "subtitle": "Current, Charge, Potential Difference, and Circuit Fundamentals",
    "badge": "Review Set 1",
    "speech": "",
    "theory": "\n            <div class=\"space-y-2 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Section Focus:</strong> Review of electric current ($I = Q/t$), charge quantization ($Q = ne$), potential difference ($V = W/Q$), ammeter series connection, and voltmeter parallel connection.</p>\n            </div>\n        ",
    "questions": [
      {
        "id": "c11_q1",
        "question": "What is the continuous rate of flow of electric charge through a conductor called?",
        "options": [
          "Electric current",
          "Electric potential",
          "Electrical resistance",
          "Electric power"
        ],
        "answer": 0,
        "hint": "Expressed mathematically as I = Q / t.",
        "explanation": "Electric current is defined as the amount of electric charge flowing across a cross-section of a conductor per unit time.",
        "steps": [
          "Step 1: Identify that the rate of flow of charge Q through a conductor in time t is I = Q/t.",
          "Step 2: In the SI system, 1 Coulomb per second is defined as 1 Ampere.",
          "Step 3: This physical quantity is called electric current."
        ]
      },
      {
        "id": "c11_q2",
        "question": "How many electrons constitute a net charge of one coulomb (1 C)?",
        "options": [
          "6.25 \u00d7 10\u00b9\u2078 electrons",
          "1.6 \u00d7 10\u207b\u00b9\u2079 electrons",
          "6.02 \u00d7 10\u00b2\u00b3 electrons",
          "9.1 \u00d7 10\u207b\u00b3\u00b9 electrons"
        ],
        "answer": 0,
        "hint": "Use n = Q / e where e = 1.6 \u00d7 10\u207b\u00b9\u2079 C.",
        "explanation": "Since Q = n \u00d7 e, n = 1 / (1.6 \u00d7 10\u207b\u00b9\u2079) = 6.25 \u00d7 10\u00b9\u2078 electrons.",
        "steps": [
          "Step 1: Charge on a single electron is e = 1.6 \u00d7 10\u207b\u00b9\u2079 C.",
          "Step 2: The total number of electrons n in charge Q is n = Q / e.",
          "Step 3: For Q = 1 C, n = 1 / (1.6 \u00d7 10\u207b\u00b9\u2079) = 6.25 \u00d7 10\u00b9\u2078 electrons."
        ]
      },
      {
        "id": "c11_q3",
        "question": "A current of 0.75 A is drawn by a filament of an electric bulb for 20 minutes. What total charge flows through the circuit?",
        "options": [
          "900 C",
          "15 C",
          "45 C",
          "1800 C"
        ],
        "answer": 0,
        "hint": "Convert 20 minutes to seconds: t = 20 \u00d7 60 = 1200 s, then apply Q = I \u00d7 t.",
        "explanation": "Q = I \u00d7 t = 0.75 A \u00d7 (20 \u00d7 60 s) = 0.75 A \u00d7 1200 s = 900 C.",
        "steps": [
          "Step 1: Convert time duration to SI units: t = 20 minutes = 20 \u00d7 60 = 1200 seconds.",
          "Step 2: Apply the electric current formula: Q = I \u00d7 t.",
          "Step 3: Calculate: Q = 0.75 A \u00d7 1200 s = 900 Coulombs."
        ]
      },
      {
        "id": "c11_q4",
        "question": "What is the work done in moving a unit positive charge from one point to another in an electric circuit called?",
        "options": [
          "Electric potential difference",
          "Electric conductance",
          "Electromotive current",
          "Capacitive reactance"
        ],
        "answer": 0,
        "hint": "Formula: V = W / Q.",
        "explanation": "Electric potential difference between two points is defined as the work done per unit charge in moving a charge between them.",
        "steps": [
          "Step 1: Consider work W performed to move charge Q between two circuit points.",
          "Step 2: The work done per unit charge is expressed as V = W/Q.",
          "Step 3: This physical quantity is defined as electric potential difference, measured in volts."
        ]
      },
      {
        "id": "c11_q5",
        "question": "How much work is required to move a charge of 3 C across two points having a potential difference of 15 V?",
        "options": [
          "45 J",
          "5 J",
          "0.2 J",
          "18 J"
        ],
        "answer": 0,
        "hint": "Apply W = V \u00d7 Q.",
        "explanation": "Work done W = V \u00d7 Q = 15 V \u00d7 3 C = 45 Joules.",
        "steps": [
          "Step 1: Identify given parameters: potential difference V = 15 V and charge Q = 3 C.",
          "Step 2: From the potential difference formula, work done is W = V \u00d7 Q.",
          "Step 3: Multiply: W = 15 V \u00d7 3 C = 45 Joules."
        ]
      },
      {
        "id": "c11_q6",
        "question": "How are an ammeter and a voltmeter connected in a standard test circuit?",
        "options": [
          "Ammeter in series, voltmeter in parallel",
          "Ammeter in parallel, voltmeter in series",
          "Both connected in series",
          "Both connected in parallel"
        ],
        "answer": 0,
        "hint": "An ammeter measures through-current; a voltmeter measures across-voltage.",
        "explanation": "An ammeter has low resistance and is connected in series; a voltmeter has high resistance and is connected in parallel.",
        "steps": [
          "Step 1: Current must pass entirely through the ammeter, requiring a series connection with low resistance.",
          "Step 2: Potential difference is measured across two nodes, requiring a parallel connection with high resistance.",
          "Step 3: Therefore, the ammeter is in series and the voltmeter is in parallel."
        ]
      },
      {
        "id": "c11_q7",
        "question": "What device is commonly used to maintain a potential difference across an external circuit?",
        "options": [
          "Chemical cell or battery",
          "Ammeter",
          "Rheostat alone",
          "Voltmeter"
        ],
        "answer": 0,
        "hint": "Chemical reactions maintain the voltage difference across its terminals.",
        "explanation": "A chemical cell or battery maintains a constant potential difference between its terminals by chemical action.",
        "steps": [
          "Step 1: Charges require an electric pressure difference to flow through conductors.",
          "Step 2: Chemical reactions inside a cell continuously generate electromotive potential across its terminals.",
          "Step 3: Thus, an electric cell or battery maintains the potential difference."
        ]
      },
      {
        "id": "c11_q8",
        "question": "How much energy is given to each coulomb of charge passing through a 6 V battery?",
        "options": [
          "6 J",
          "1 J",
          "36 J",
          "0.16 J"
        ],
        "answer": 0,
        "hint": "Each coulomb means Q = 1 C. Work done W = V \u00d7 Q.",
        "explanation": "Work done W = V \u00d7 Q = 6 V \u00d7 1 C = 6 Joules of energy per coulomb.",
        "steps": [
          "Step 1: Identify that 'each coulomb' corresponds to a charge Q = 1 C.",
          "Step 2: The battery maintains a potential difference of V = 6 V.",
          "Step 3: Energy delivered W = V \u00d7 Q = 6 V \u00d7 1 C = 6 Joules."
        ]
      },
      {
        "id": "c11_q9",
        "question": "What is the conventional graphical symbol for an open plug key in an electrical schematic?",
        "options": [
          "Parentheses with no center dot ()",
          "Parentheses with center dot (\u00b7)",
          "A zig-zag line",
          "A circle with letter A"
        ],
        "answer": 0,
        "hint": "A central dot indicates conducting contact (closed key).",
        "explanation": "According to NCERT Table 11.1, an open plug key is symbolized by empty parentheses (), while a closed key contains a center dot (\u00b7).",
        "steps": [
          "Step 1: Standard circuit notation represents a switch via parentheses.",
          "Step 2: When open, no conduction occurs and the space inside remains blank ().",
          "Step 3: When closed, a central dot is inserted (\u00b7) to denote electrical continuity."
        ]
      },
      {
        "id": "c11_q10",
        "question": "If 1 microampere (1 \u03bcA) of current flows in a wire, how many amperes does this represent?",
        "options": [
          "10\u207b\u2076 A",
          "10\u207b\u00b3 A",
          "10\u2076 A",
          "10\u207b\u2079 A"
        ],
        "answer": 0,
        "hint": "Micro denotes the metric prefix for one-millionth (10\u207b\u2076).",
        "explanation": "1 microampere = 1 \u03bcA = 10\u207b\u2076 A (one-millionth of an ampere).",
        "steps": [
          "Step 1: Recall the standard metric prefixes: milli = 10\u207b\u00b3 and micro = 10\u207b\u2076.",
          "Step 2: Apply the prefix to amperes: 1 \u03bcA = 1 \u00d7 10\u207b\u2076 A.",
          "Step 3: Therefore, 1 microampere represents 10\u207b\u2076 amperes."
        ]
      }
    ]
  },
  {
    "id": 18,
    "title": "Resistor Geometry Review",
    "subtitle": "Ohm's Law, V-I Graphs, Geometric Factors, and Resistivity",
    "badge": "Review Set 2",
    "speech": "",
    "theory": "\n            <div class=\"space-y-2 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Section Focus:</strong> Review of Ohm's law ($V = IR$), linear $V\\text{--}I$ characteristics, geometric resistance dependencies ($R = \\rho l/A$), wire stretching/cutting, and resistivity comparisons.</p>\n            </div>\n        ",
    "questions": [
      {
        "id": "c11_q11",
        "question": "What mathematical relationship constitutes Ohm's law at constant temperature?",
        "options": [
          "V = IR",
          "V = I / R",
          "V = I\u00b2R",
          "V = R / I"
        ],
        "answer": 0,
        "hint": "Potential difference is directly proportional to current (V \u221d I).",
        "explanation": "Ohm's law states that V \u221d I at constant temperature, giving the equation V = IR.",
        "steps": [
          "Step 1: Ohm's law establishes direct proportionality between potential difference and current: V \u221d I.",
          "Step 2: Introducing the constant of proportionality R (resistance) gives V = IR.",
          "Step 3: Therefore, V = IR is the definitive mathematical formulation."
        ]
      },
      {
        "id": "c11_q12",
        "question": "A piece of wire of resistance R is cut into 5 equal parts. These parts are then connected in parallel. If the equivalent resistance of this combination is R', what is the ratio R/R'?",
        "options": [
          "25",
          "1/25",
          "5",
          "1/5"
        ],
        "answer": 0,
        "hint": "Each piece has resistance r = R/5. Combining 5 equal resistors in parallel gives R' = r/5 = R/25.",
        "explanation": "Each of the 5 pieces has resistance r = R/5. When connected in parallel, 1/R' = 5 \u00d7 (1/r) = 5 \u00d7 (5/R) = 25/R. Thus R' = R/25, giving R/R' = 25 (NCERT Exercise Q1).",
        "steps": [
          "Step 1: Cutting wire of resistance R into 5 equal lengths gives each part a resistance r = R/5 (since R \u221d l).",
          "Step 2: Connecting 5 such parts in parallel gives 1/R' = 1/r + 1/r + 1/r + 1/r + 1/r = 5/r = 5 / (R/5) = 25/R.",
          "Step 3: Taking the reciprocal gives R' = R/25. Thus, the ratio R / R' = 25."
        ]
      },
      {
        "id": "c11_q13",
        "question": "How does the resistance of a cylindrical conductor change if its length is doubled and its cross-sectional area is halved?",
        "options": [
          "It increases by a factor of 4",
          "It remains unchanged",
          "It doubles",
          "It is halved"
        ],
        "answer": 0,
        "hint": "Apply R = \u03c1 l / A with l' = 2l and A' = A/2.",
        "explanation": "R' = \u03c1 (2l) / (A/2) = 4 \u00d7 (\u03c1 l / A) = 4R. Resistance quadruples.",
        "steps": [
          "Step 1: The original resistance is R = \u03c1 l / A.",
          "Step 2: When length doubles (l' = 2l) and area is halved (A' = A/2), the new resistance is R' = \u03c1 (2l) / (A/2).",
          "Step 3: Simplifying gives R' = 4 (\u03c1 l / A) = 4R. Thus, resistance increases four-fold."
        ]
      },
      {
        "id": "c11_q14",
        "question": "An electric heater draws 4 A current from a 60 V source. What current will it draw if the potential difference is increased to 120 V?",
        "options": [
          "8 A",
          "2 A",
          "16 A",
          "4 A"
        ],
        "answer": 0,
        "hint": "First find resistance R = V / I = 60 / 4 = 15 \u03a9, then find I' = 120 / 15.",
        "explanation": "Resistance R = 60 V / 4 A = 15 \u03a9. At 120 V, new current I' = 120 V / 15 \u03a9 = 8 A (NCERT Example 11.4).",
        "steps": [
          "Step 1: Calculate the heater resistance: R = V / I = 60 V / 4 A = 15 \u03a9.",
          "Step 2: When potential difference increases to 120 V, apply Ohm's law: I' = V' / R.",
          "Step 3: Compute: I' = 120 V / 15 \u03a9 = 8 A."
        ]
      },
      {
        "id": "c11_q15",
        "question": "Which of the following materials has the lowest electrical resistivity at 20\u00b0C?",
        "options": [
          "Silver (1.60 \u00d7 10\u207b\u2078 \u03a9\u00b7m)",
          "Copper (1.62 \u00d7 10\u207b\u2078 \u03a9\u00b7m)",
          "Nichrome (100 \u00d7 10\u207b\u2076 \u03a9\u00b7m)",
          "Glass (10\u00b9\u2070 to 10\u00b9\u2074 \u03a9\u00b7m)"
        ],
        "answer": 0,
        "hint": "Refer to Table 11.2 for the best known electrical conductor.",
        "explanation": "Silver has the lowest resistivity (1.60 \u00d7 10\u207b\u2078 \u03a9\u00b7m) among all known metals at 20\u00b0C, making it the best conductor.",
        "steps": [
          "Step 1: Check NCERT Table 11.2 for conductor resistivity values.",
          "Step 2: Silver has \u03c1 = 1.60 \u00d7 10\u207b\u2078 \u03a9\u00b7m, copper has 1.62 \u00d7 10\u207b\u2078 \u03a9\u00b7m, nichrome has 100 \u00d7 10\u207b\u2076 \u03a9\u00b7m, and glass is an insulator.",
          "Step 3: Therefore, silver possesses the lowest electrical resistivity."
        ]
      },
      {
        "id": "c11_q16",
        "question": "A cylindrical copper wire has radius r and length l with resistance R. If stretched to radius r/2 while keeping volume constant, what is its new resistance?",
        "options": [
          "16 R",
          "4 R",
          "2 R",
          "8 R"
        ],
        "answer": 0,
        "hint": "Volume V = A \u00d7 l = constant. Halving radius reduces area to A/4, which increases length to 4l. Then R' = \u03c1 (4l)/(A/4).",
        "explanation": "When radius is halved, area becomes A' = A/4. Because volume is conserved, length quadruples (l' = 4l). R' = \u03c1 (4l) / (A/4) = 16 R.",
        "steps": [
          "Step 1: Volume of wire is V = A \u00d7 l = \u03c0 r\u00b2 l = constant.",
          "Step 2: When radius becomes r/2, cross-sectional area becomes A' = \u03c0(r/2)\u00b2 = A/4, so length becomes l' = 4l.",
          "Step 3: New resistance R' = \u03c1 l' / A' = \u03c1 (4l) / (A/4) = 16 (\u03c1 l / A) = 16 R."
        ]
      },
      {
        "id": "c11_q17",
        "question": "Why does the cord of an electric heater not glow while the heating element glows red-hot?",
        "options": [
          "Cord has very low resistance copper wire, while element has high resistance nichrome",
          "Cord is insulated with rubber which reflects light",
          "Current flows through the element but bypasses the cord",
          "The element contains active chemical combustible gases"
        ],
        "answer": 0,
        "hint": "Joule heating H = I\u00b2Rt depends directly on resistance R.",
        "explanation": "The copper connecting cord has very low resistance so heat generated is negligible; the nichrome element has high resistance so H = I\u00b2Rt produces high temperature and glowing.",
        "steps": [
          "Step 1: The cord and the heating element are connected in series, carrying the identical current I.",
          "Step 2: From Joule's law (H = I\u00b2Rt), heat produced is directly proportional to resistance R.",
          "Step 3: The copper cord has very low resistance (stays cool), while the nichrome coil has high resistance (glows red-hot)."
        ]
      },
      {
        "id": "c11_q18",
        "question": "A 1 m long wire of radius 0.15 mm has a resistance of 26 \u03a9 at 20\u00b0C. What is its resistivity?",
        "options": [
          "1.84 \u00d7 10\u207b\u2076 \u03a9\u00b7m",
          "1.84 \u00d7 10\u207b\u2078 \u03a9\u00b7m",
          "2.6 \u00d7 10\u207b\u2075 \u03a9\u00b7m",
          "5.2 \u00d7 10\u207b\u2076 \u03a9\u00b7m"
        ],
        "answer": 0,
        "hint": "Area A = \u03c0 r\u00b2 = 3.14 \u00d7 (1.5 \u00d7 10\u207b\u2074)\u00b2. Apply \u03c1 = R \u00d7 A / l.",
        "explanation": "A = \u03c0 \u00d7 (0.15 \u00d7 10\u207b\u00b3)\u00b2 \u2248 7.07 \u00d7 10\u207b\u2078 m\u00b2. \u03c1 = R \u00d7 A / l = 26 \u00d7 7.07 \u00d7 10\u207b\u2078 / 1 \u2248 1.84 \u00d7 10\u207b\u2076 \u03a9\u00b7m (NCERT Example 11.5).",
        "steps": [
          "Step 1: Convert radius to metres: r = 0.15 mm = 1.5 \u00d7 10\u207b\u2074 m. Cross-sectional area A = \u03c0 r\u00b2 \u2248 7.069 \u00d7 10\u207b\u2078 m\u00b2.",
          "Step 2: Use the resistivity formula: \u03c1 = R \u00d7 A / l.",
          "Step 3: Calculate: \u03c1 = 26 \u03a9 \u00d7 7.069 \u00d7 10\u207b\u2078 m\u00b2 / 1 m = 1.84 \u00d7 10\u207b\u2076 \u03a9\u00b7m (manganin)."
        ]
      },
      {
        "id": "c11_q19",
        "question": "How does electrical resistivity vary when a metal is heated to a higher temperature?",
        "options": [
          "Resistivity of pure metals increases with temperature",
          "Resistivity drops to zero at high temperature",
          "Resistivity is completely independent of temperature",
          "Resistivity alternates periodically between positive and negative"
        ],
        "answer": 0,
        "hint": "Higher temperature increases lattice ion vibrations, scattering electrons more frequently.",
        "explanation": "In pure metals, thermal energy increases lattice ion vibrations, increasing electron collisions and causing electrical resistivity to increase with temperature.",
        "steps": [
          "Step 1: Heating a metal imparts kinetic energy to the positive metallic crystal ions.",
          "Step 2: Increased amplitude of ionic vibrations enhances the collision cross-section for drifting electrons.",
          "Step 3: Consequently, electron mobility decreases and resistivity increases with temperature."
        ]
      },
      {
        "id": "c11_q20",
        "question": "What is the equivalent resistance of a conductor through which a current of 2 A flows under a potential difference of 8 V?",
        "options": [
          "4 \u03a9",
          "16 \u03a9",
          "0.25 \u03a9",
          "10 \u03a9"
        ],
        "answer": 0,
        "hint": "Use Ohm's law R = V / I.",
        "explanation": "R = V / I = 8 V / 2 A = 4 \u03a9.",
        "steps": [
          "Step 1: Identify given parameters: voltage V = 8 V and current I = 2 A.",
          "Step 2: Apply Ohm's law: R = V / I.",
          "Step 3: Calculate: R = 8 V / 2 A = 4 \u03a9."
        ]
      }
    ]
  },
  {
    "id": 19,
    "title": "Resistor Networks Review",
    "subtitle": "Series, Parallel, and Complex Equivalent Network Analysis",
    "badge": "Review Set 3",
    "speech": "",
    "theory": "\n            <div class=\"space-y-2 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Section Focus:</strong> Review of series resistor formulas ($R_s = R_1 + R_2 + R_3$), parallel resistor formulas ($1/R_p = 1/R_1 + 1/R_2 + 1/R_3$), branch current division, and complex series-parallel equivalent circuits.</p>\n            </div>\n        ",
    "questions": [
      {
        "id": "c11_q21",
        "question": "How can three resistors of 2 \u03a9, 3 \u03a9, and 6 \u03a9 be connected to give a total equivalent resistance of 4 \u03a9?",
        "options": [
          "3 \u03a9 and 6 \u03a9 in parallel, connected in series with 2 \u03a9",
          "All three in series",
          "All three in parallel",
          "2 \u03a9 and 3 \u03a9 in parallel, in series with 6 \u03a9"
        ],
        "answer": 0,
        "hint": "Parallel combination of 3 \u03a9 and 6 \u03a9 gives (3\u00d76)/(3+6) = 2 \u03a9. Then add 2 \u03a9 in series: 2 + 2 = 4 \u03a9.",
        "explanation": "Connecting 3 \u03a9 and 6 \u03a9 in parallel gives Rp = (3\u00d76)/(3+6) = 2 \u03a9. Placing this in series with 2 \u03a9 gives R_total = 2 + 2 = 4 \u03a9 (NCERT In-text Q1).",
        "steps": [
          "Step 1: Test parallel combination of 3 \u03a9 and 6 \u03a9: 1/Rp = 1/3 + 1/6 = 3/6 = 1/2, so Rp = 2 \u03a9.",
          "Step 2: Connect the remaining 2 \u03a9 resistor in series with this parallel pair.",
          "Step 3: Total equivalent resistance R_total = Rp + 2 \u03a9 = 2 + 2 = 4 \u03a9."
        ]
      },
      {
        "id": "c11_q22",
        "question": "How can the same three resistors of 2 \u03a9, 3 \u03a9, and 6 \u03a9 be connected to give a total equivalent resistance of 1 \u03a9?",
        "options": [
          "All three connected in parallel",
          "All three connected in series",
          "2 \u03a9 and 6 \u03a9 in series, in parallel with 3 \u03a9",
          "3 \u03a9 and 6 \u03a9 in series, in parallel with 2 \u03a9"
        ],
        "answer": 0,
        "hint": "Calculate 1/Rp = 1/2 + 1/3 + 1/6.",
        "explanation": "1/Rp = 1/2 + 1/3 + 1/6 = 3/6 + 2/6 + 1/6 = 6/6 = 1 \u03a9\u207b\u00b9. Thus Rp = 1 \u03a9 (NCERT In-text Q2).",
        "steps": [
          "Step 1: Connect all three resistors in parallel across two common junction nodes.",
          "Step 2: Apply the parallel formula: 1/Rp = 1/2 + 1/3 + 1/6 = (3 + 2 + 1) / 6 = 6/6 = 1 \u03a9\u207b\u00b9.",
          "Step 3: Taking the reciprocal gives Rp = 1 \u03a9."
        ]
      },
      {
        "id": "c11_q23",
        "question": "What is the highest equivalent resistance that can be obtained by combining four coils of resistances 4 \u03a9, 8 \u03a9, 12 \u03a9, and 24 \u03a9?",
        "options": [
          "48 \u03a9",
          "2 \u03a9",
          "24 \u03a9",
          "96 \u03a9"
        ],
        "answer": 0,
        "hint": "Highest resistance is always obtained by connecting all resistors in series.",
        "explanation": "The highest resistance is obtained in series: Rs = 4 + 8 + 12 + 24 = 48 \u03a9 (NCERT In-text Q3).",
        "steps": [
          "Step 1: The maximum possible resistance of any resistor set is achieved in a series configuration.",
          "Step 2: Sum the individual resistance values: Rs = R1 + R2 + R3 + R4.",
          "Step 3: Calculate: Rs = 4 + 8 + 12 + 24 = 48 \u03a9."
        ]
      },
      {
        "id": "c11_q24",
        "question": "What is the lowest equivalent resistance that can be obtained from the same four coils (4 \u03a9, 8 \u03a9, 12 \u03a9, and 24 \u03a9)?",
        "options": [
          "2 \u03a9",
          "48 \u03a9",
          "1 \u03a9",
          "4 \u03a9"
        ],
        "answer": 0,
        "hint": "Lowest resistance is always obtained by connecting all resistors in parallel.",
        "explanation": "1/Rp = 1/4 + 1/8 + 1/12 + 1/24 = (6 + 3 + 2 + 1) / 24 = 12/24 = 1/2. Thus Rp = 2 \u03a9 (NCERT In-text Q4).",
        "steps": [
          "Step 1: The minimum possible resistance is achieved by connecting all resistors in parallel.",
          "Step 2: 1/Rp = 1/4 + 1/8 + 1/12 + 1/24 = (6 + 3 + 2 + 1) / 24 = 12/24 = 1/2 \u03a9\u207b\u00b9.",
          "Step 3: Taking the reciprocal gives Rp = 2 \u03a9."
        ]
      },
      {
        "id": "c11_q25",
        "question": "In a parallel circuit with resistors R1 = 5 \u03a9, R2 = 10 \u03a9, and R3 = 30 \u03a9 connected to a 12 V battery, what is the total circuit current?",
        "options": [
          "4 A",
          "0.4 A",
          "2.4 A",
          "1.2 A"
        ],
        "answer": 0,
        "hint": "Find branch currents: I1 = 12/5 = 2.4 A, I2 = 12/10 = 1.2 A, I3 = 12/30 = 0.4 A. Sum them.",
        "explanation": "I1 = 2.4 A, I2 = 1.2 A, I3 = 0.4 A. Total current I = 2.4 + 1.2 + 0.4 = 4.0 A (NCERT Example 11.8).",
        "steps": [
          "Step 1: Voltage across each branch is V = 12 V.",
          "Step 2: Branch currents are I1 = 12/5 = 2.4 A, I2 = 12/10 = 1.2 A, and I3 = 12/30 = 0.4 A.",
          "Step 3: Total current I = I1 + I2 + I3 = 2.4 + 1.2 + 0.4 = 4.0 A."
        ]
      },
      {
        "id": "c11_q26",
        "question": "What is the equivalent resistance of the parallel combination of 5 \u03a9, 10 \u03a9, and 30 \u03a9?",
        "options": [
          "3 \u03a9",
          "45 \u03a9",
          "15 \u03a9",
          "5 \u03a9"
        ],
        "answer": 0,
        "hint": "1/Rp = 1/5 + 1/10 + 1/30 = (6 + 3 + 1)/30 = 10/30 = 1/3.",
        "explanation": "1/Rp = 1/5 + 1/10 + 1/30 = 10/30 = 1/3 \u03a9\u207b\u00b9. Rp = 3 \u03a9 (NCERT Example 11.8).",
        "steps": [
          "Step 1: Write the reciprocal parallel formula: 1/Rp = 1/5 + 1/10 + 1/30.",
          "Step 2: Find common denominator 30: 1/Rp = (6 + 3 + 1) / 30 = 10/30 = 1/3 \u03a9\u207b\u00b9.",
          "Step 3: Invert to find Rp: Rp = 3 \u03a9."
        ]
      },
      {
        "id": "c11_q27",
        "question": "Two identical resistors of resistance R each are connected first in series and then in parallel. What is the ratio of series to parallel equivalent resistance (Rs / Rp)?",
        "options": [
          "4",
          "1/4",
          "2",
          "1/2"
        ],
        "answer": 0,
        "hint": "Rs = 2R, Rp = R/2. Ratio Rs / Rp = (2R) / (R/2) = 4.",
        "explanation": "Rs = R + R = 2R. Rp = (R \u00d7 R) / (R + R) = R/2. Ratio Rs / Rp = 2R / (R/2) = 4.",
        "steps": [
          "Step 1: Equivalent resistance in series is Rs = R + R = 2R.",
          "Step 2: Equivalent resistance in parallel is Rp = R / 2.",
          "Step 3: Compute the ratio: Rs / Rp = (2R) / (R/2) = 4."
        ]
      },
      {
        "id": "c11_q28",
        "question": "In a series circuit containing an 8 \u03a9 resistor and a 12 \u03a9 resistor powered by a 10 V battery, what is the voltage drop across the 12 \u03a9 resistor?",
        "options": [
          "6 V",
          "4 V",
          "10 V",
          "2.4 V"
        ],
        "answer": 0,
        "hint": "Total Rs = 8 + 12 = 20 \u03a9. Current I = 10 / 20 = 0.5 A. Voltage across 12 \u03a9 is V = 0.5 \u00d7 12 = 6 V.",
        "explanation": "Rs = 8 + 12 = 20 \u03a9. Current I = 10 V / 20 \u03a9 = 0.5 A. V\u2082 = I \u00d7 R\u2082 = 0.5 A \u00d7 12 \u03a9 = 6 V.",
        "steps": [
          "Step 1: Total series resistance is Rs = 8 + 12 = 20 \u03a9.",
          "Step 2: Circuit current is I = V / Rs = 10 V / 20 \u03a9 = 0.5 A.",
          "Step 3: Voltage drop across the 12 \u03a9 resistor is V2 = I \u00d7 R2 = 0.5 A \u00d7 12 \u03a9 = 6 V."
        ]
      },
      {
        "id": "c11_q29",
        "question": "How many 176 \u03a9 resistors connected in parallel are required to carry a total current of 5 A on a 220 V line?",
        "options": [
          "4 resistors",
          "5 resistors",
          "2 resistors",
          "8 resistors"
        ],
        "answer": 0,
        "hint": "Required equivalent resistance Rp = V / I = 220 / 5 = 44 \u03a9. Since Rp = R / n, n = R / Rp = 176 / 44.",
        "explanation": "Target resistance Rp = 220 V / 5 A = 44 \u03a9. For n identical resistors in parallel, Rp = 176 / n. Thus n = 176 / 44 = 4 resistors (NCERT Exercise Q10).",
        "steps": [
          "Step 1: Calculate the required total circuit resistance: Rp = V / I = 220 V / 5 A = 44 \u03a9.",
          "Step 2: For n parallel resistors of value R, the equivalent resistance is Rp = R / n.",
          "Step 3: Solve for n: n = R / Rp = 176 \u03a9 / 44 \u03a9 = 4 resistors."
        ]
      },
      {
        "id": "c11_q30",
        "question": "Why is an ammeter never connected in parallel across a power source?",
        "options": [
          "Its extremely low resistance would cause a dangerous short circuit and burn out the meter",
          "It has infinite resistance and would prevent all current flow",
          "It would reverse the chemical polarity of the battery cells",
          "Voltmeters and ammeters must always be installed in pairs"
        ],
        "answer": 0,
        "hint": "A low-resistance device placed directly across a voltage source draws enormous current.",
        "explanation": "Because an ammeter has virtually zero internal resistance, connecting it in parallel across a voltage source creates a dead short circuit, resulting in massive current that destroys the instrument.",
        "steps": [
          "Step 1: Ammeters are engineered with minimal internal resistance (R \u2248 0) to avoid disturbing series circuits.",
          "Step 2: Placing an ammeter in parallel connects near-zero resistance directly across the battery terminals.",
          "Step 3: By Ohm's law (I = V/R), a catastrophic surge of current occurs, blowing the meter or circuit."
        ]
      }
    ]
  },
  {
    "id": 20,
    "title": "Power Heating Review",
    "subtitle": "Joule's Law, Bulb Filaments, Fuse Ratings, and Commercial kWh Billing",
    "badge": "Review Set 4",
    "speech": "",
    "theory": "\n            <div class=\"space-y-2 text-slate-300 text-xs leading-relaxed\">\n                <p><strong class=\"text-amber-400\">Section Focus:</strong> Review of Joule's heating law ($H = I^2 Rt$), tungsten filaments, fuse protection, power ratings ($P = VI = I^2 R = V^2/R$), commercial energy units ($1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$), and electricity cost calculations.</p>\n            </div>\n        ",
    "questions": [
      {
        "id": "c11_q31",
        "question": "Which of the following is NOT an expression for electrical power in a circuit?",
        "options": [
          "IR\u00b2",
          "I\u00b2R",
          "VI",
          "V\u00b2/R"
        ],
        "answer": 0,
        "hint": "Power is VI, I\u00b2R, or V\u00b2/R. Notice the placement of the square.",
        "explanation": "P = VI = I\u00b2R = V\u00b2/R. The expression IR\u00b2 has no physical meaning in electrical power (NCERT Exercise Q2).",
        "steps": [
          "Step 1: Electric power is defined as P = V \u00d7 I.",
          "Step 2: Substituting V = IR gives P = (IR) \u00d7 I = I\u00b2R.",
          "Step 3: Substituting I = V/R gives P = V \u00d7 (V/R) = V\u00b2/R. The expression IR\u00b2 is incorrect."
        ]
      },
      {
        "id": "c11_q32",
        "question": "An electric bulb is rated 220 V and 100 W. When operated on 110 V, what power will it consume?",
        "options": [
          "25 W",
          "50 W",
          "75 W",
          "100 W"
        ],
        "answer": 0,
        "hint": "Resistance R = V\u00b2 / P = 220\u00b2 / 100 = 484 \u03a9. At 110 V, P' = V'\u00b2 / R = 110\u00b2 / 484.",
        "explanation": "Bulb resistance R = V\u00b2 / P = 220\u00b2 / 100 = 484 \u03a9. When operated at 110 V: P' = V'\u00b2 / R = 110\u00b2 / 484 = 12100 / 484 = 25 W (NCERT Exercise Q3).",
        "steps": [
          "Step 1: Filament resistance is R = V\u00b2 / P = (220)\u00b2 / 100 = 484 \u03a9.",
          "Step 2: When supply voltage is halved to V' = 110 V, power consumed is P' = (V')\u00b2 / R.",
          "Step 3: Calculate: P' = (110)\u00b2 / 484 = 12,100 / 484 = 25 W (power drops to one-fourth)."
        ]
      },
      {
        "id": "c11_q33",
        "question": "Two conducting wires of the same material, equal length, and equal diameter are connected first in series and then in parallel across the same potential difference. What is the ratio of heat produced in series to parallel (Hs / Hp)?",
        "options": [
          "1 : 4",
          "1 : 2",
          "2 : 1",
          "4 : 1"
        ],
        "answer": 0,
        "hint": "At constant V, H = (V\u00b2/R) \u00d7 t. Rs = 2R, Rp = R/2. Hs / Hp = (V\u00b2/2R) / (V\u00b2/(R/2)) = (1/2) / 2 = 1/4.",
        "explanation": "Since voltage V is constant across both setups, H \u221d 1/R. Hs / Hp = Rp / Rs = (R/2) / (2R) = 1/4 = 1:4 (NCERT Exercise Q4).",
        "steps": [
          "Step 1: When connected to the same voltage source V, heat produced is H = (V\u00b2 / R_eq) \u00d7 t.",
          "Step 2: Series equivalent is Rs = 2R; parallel equivalent is Rp = R/2.",
          "Step 3: Ratio Hs / Hp = (V\u00b2 / Rs) / (V\u00b2 / Rp) = Rp / Rs = (R/2) / (2R) = 1/4 = 1 : 4."
        ]
      },
      {
        "id": "c11_q34",
        "question": "An electric refrigerator rated 400 W operates 8 hours/day for 30 days. What is the cost of energy at Rs 3.00 per kWh?",
        "options": [
          "Rs 288.00",
          "Rs 96.00",
          "Rs 576.00",
          "Rs 144.00"
        ],
        "answer": 0,
        "hint": "Energy E = 400 W \u00d7 8 h/day \u00d7 30 days = 96,000 Wh = 96 kWh. Cost = 96 \u00d7 3.00.",
        "explanation": "Total energy = 400 W \u00d7 8 h \u00d7 30 = 96,000 Wh = 96 kWh. Total cost = 96 kWh \u00d7 Rs 3.00 = Rs 288.00 (NCERT Example 11.13).",
        "steps": [
          "Step 1: Total operating hours in 30 days = 8 hours/day \u00d7 30 days = 240 hours.",
          "Step 2: Total electrical energy consumed = 400 W \u00d7 240 h = 96,000 Watt-hours = 96 kWh.",
          "Step 3: Cost = 96 kWh \u00d7 Rs 3.00/kWh = Rs 288.00."
        ]
      },
      {
        "id": "c11_q35",
        "question": "Which uses more energy: a 250 W TV set in 1 hour, or a 1200 W toaster in 10 minutes?",
        "options": [
          "The TV set uses more energy (250 Wh vs 200 Wh)",
          "The toaster uses more energy (1200 Wh vs 250 Wh)",
          "Both appliances use exactly identical energy",
          "Neither appliance consumes any electrical energy"
        ],
        "answer": 0,
        "hint": "E(TV) = 250 W \u00d7 1 h = 250 Wh. E(toaster) = 1200 W \u00d7 (10/60) h = 200 Wh.",
        "explanation": "Energy for TV = 250 W \u00d7 1 h = 250 Wh. Energy for toaster = 1200 W \u00d7 (1/6 h) = 200 Wh. The TV set uses more energy (NCERT Exercise Q16).",
        "steps": [
          "Step 1: Calculate energy used by TV: E\u2081 = 250 W \u00d7 1 hour = 250 Watt-hours (Wh).",
          "Step 2: Calculate energy used by toaster: E\u2082 = 1200 W \u00d7 (10/60) hours = 200 Watt-hours (Wh).",
          "Step 3: Comparing E\u2081 = 250 Wh and E\u2082 = 200 Wh shows that the TV set consumes more energy."
        ]
      },
      {
        "id": "c11_q36",
        "question": "An electric lamp is marked 100 W, 220 V. What is the current drawn by the lamp under rated conditions?",
        "options": [
          "0.45 A",
          "2.2 A",
          "4.5 A",
          "0.22 A"
        ],
        "answer": 0,
        "hint": "Use I = P / V = 100 / 220.",
        "explanation": "I = P / V = 100 W / 220 V = 5/11 A \u2248 0.45 A.",
        "steps": [
          "Step 1: Identify rated power P = 100 W and rated voltage V = 220 V.",
          "Step 2: Apply the power formula: P = V \u00d7 I, which rearranges to I = P / V.",
          "Step 3: Calculate: I = 100 W / 220 V = 0.454 A \u2248 0.45 A."
        ]
      },
      {
        "id": "c11_q37",
        "question": "What is the primary physical reason for filling inactive nitrogen and argon gases into incandescent light bulbs?",
        "options": [
          "To prevent oxidation and evaporation of the hot tungsten filament",
          "To cause chemical fluorescence emitting blue light",
          "To conduct electrical current directly across the glass bulb",
          "To absorb all infrared heat radiation"
        ],
        "answer": 0,
        "hint": "Oxygen at high temperatures would burn the glowing metallic filament instantly.",
        "explanation": "Nitrogen and argon are chemically inert gases that prevent oxidation and thermal evaporation of the tungsten filament, extending its lifespan.",
        "steps": [
          "Step 1: The tungsten filament operates at temperatures exceeding 2500\u00b0C.",
          "Step 2: In the presence of oxygen, tungsten would oxidize and vaporize rapidly, burning out the bulb.",
          "Step 3: Inert nitrogen and argon do not react with tungsten and retard evaporation, prolonging filament life."
        ]
      },
      {
        "id": "c11_q38",
        "question": "An electric iron draws 3.82 A current from a 220 V source. What is its power rating?",
        "options": [
          "840 W",
          "57.6 W",
          "360 W",
          "1200 W"
        ],
        "answer": 0,
        "hint": "Apply P = V \u00d7 I = 220 \u00d7 3.82.",
        "explanation": "P = V \u00d7 I = 220 V \u00d7 3.82 A \u2248 840 W (NCERT Example 11.10).",
        "steps": [
          "Step 1: Identify potential difference V = 220 V and current I = 3.82 A.",
          "Step 2: Use the electric power equation: P = V \u00d7 I.",
          "Step 3: Calculate: P = 220 V \u00d7 3.82 A = 840.4 W \u2248 840 W."
        ]
      },
      {
        "id": "c11_q39",
        "question": "What is the equivalent resistance of an electric iron that produces 100 J of heat per second when connected across a 20 V supply?",
        "options": [
          "4 \u03a9",
          "20 \u03a9",
          "5 \u03a9",
          "100 \u03a9"
        ],
        "answer": 0,
        "hint": "Heat per second is power P = 100 W. Use R = V\u00b2 / P = 20\u00b2 / 100.",
        "explanation": "P = 100 J/s = 100 W. R = V\u00b2 / P = 20\u00b2 / 100 = 400 / 100 = 4 \u03a9 (NCERT Example 11.11).",
        "steps": [
          "Step 1: 100 Joules of heat per second corresponds to an electrical power P = 100 W.",
          "Step 2: From the power formula P = V\u00b2 / R, isolate resistance: R = V\u00b2 / P.",
          "Step 3: Calculate: R = (20 V)\u00b2 / 100 W = 400 / 100 = 4 \u03a9."
        ]
      },
      {
        "id": "c11_q40",
        "question": "If an appliance of 2 kW power operates for 3 hours daily for 10 days, how many commercial units of electricity are consumed?",
        "options": [
          "60 units (60 kWh)",
          "6 units",
          "180 units",
          "20 units"
        ],
        "answer": 0,
        "hint": "Energy = Power (kW) \u00d7 Total Hours = 2 kW \u00d7 (3 \u00d7 10) h = 2 \u00d7 30 = 60 kWh.",
        "explanation": "Total hours = 3 h/day \u00d7 10 days = 30 h. Total energy = 2 kW \u00d7 30 h = 60 kWh = 60 commercial units.",
        "steps": [
          "Step 1: 1 commercial unit of electricity = 1 kilowatt-hour (1 kWh).",
          "Step 2: Total operating time = 3 hours/day \u00d7 10 days = 30 hours.",
          "Step 3: Energy consumed = 2 kW \u00d7 30 hours = 60 kWh = 60 units."
        ]
      }
    ]
  }
]

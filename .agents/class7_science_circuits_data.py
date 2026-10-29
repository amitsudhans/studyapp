# -*- coding: utf-8 -*-
"""Class 7 Science Chapter 3: Electricity: Circuits and their Components Data"""

SLIDES_DATA = [
  {
    "id": 1,
    "type": "theory_slide",
    "title": "A Torchlight: Portable Illumination & Safety Laws",
    "subtitle": "3.1 A Torchlight — Deconstructing Everyday Portable Lighting & The Golden Safety Rules",
    "content": "A common torchlight (flashlight) is one of the most familiar and reliable electrical instruments in our homes. When you slide the switch on, a small bulb instantly casts a bright beam of light into darkness. But what makes it work? Inside its cylindrical casing lies an elegant, self-contained electrical system consisting of <strong>electric cells</strong>, a sliding <strong>metallic switch strip</strong>, a <strong>helical spring</strong>, and an <strong>electric lamp</strong> nested within a parabolic reflector.<br><br><span class='text-amber-400 font-bold'>The Golden Safety Commandment of Science:</span> In our classroom experiments, we <em>only and strictly</em> use small dry electric cells 1.5 V. You must <strong>never</strong> connect wires, lamps, or homemade switches to domestic wall sockets 220 V – 240 V AC mains, domestic inverters, or portable fuel-driven generators. Mains electricity carries dangerous high voltages that can cause lethal electric shocks, severe burns, or catastrophic short circuits.",
    "formula": "Mains Voltage (230 V AC) ≫ Dry Cell Voltage (1.5 V DC)  ➔  Classroom Safety Guaranteed!",
    "key_takeaways": [
      "A torchlight converts stored chemical energy into electrical energy and radiant light.",
      "Key internal parts: dry electric cells, metallic contact strip, slide switch, helical spring, and reflector bulb.",
      "Classroom experiments must strictly use small dry cells (1.5 V to 9 V).",
      "Never ever connect student experiment wires to domestic mains sockets, generators, or car batteries."
    ],
    "checkpoints": [
      {
        "question": "Why is it strictly prohibited to conduct classroom circuit experiments using domestic wall sockets?",
        "options": [
          "Domestic sockets provide 230 V AC mains voltage which can cause lethal electric shocks and burns",
          "Wall socket electricity does not make light bulbs glow",
          "Wall sockets do not have positive or negative terminals",
          "Domestic sockets only power air conditioners and refrigerators"
        ],
        "correct": 0,
        "explanation": "Domestic AC mains voltage (230 V) is extremely high and hazardous. A 1.5 V dry cell provides safe, low-voltage direct current (DC) ideal for learning."
      },
      {
        "question": "What is the primary function of the helical metal spring located at the base of a torchlight?",
        "options": [
          "To generate electricity from mechanical compression",
          "To keep the electric cells pressed firmly together to maintain continuous electrical contact",
          "To change the color of the bulb's light",
          "To absorb excess electrical heat"
        ],
        "correct": 1,
        "explanation": "The metal spring exerts continuous elastic force against the negative terminal of the bottom cell, keeping all cells in firm electrical contact."
      }
    ],
    "simulator_type": "torchlight_anatomy_sim"
  },
  {
    "id": 2,
    "type": "theory_slide",
    "title": "The Electric Cell: Anatomy of a Portable Power Source",
    "subtitle": "3.2.1 Electric Cell — Terminals, Zinc Canister, Carbon Rod & Chemical Energy Conversion",
    "content": "An <strong>electric cell</strong> is a compact electrochemical device that generates electrical energy from chemical reactions occurring within its interior. A standard cylindrical dry cell features two distinct terminals:<br><br>1. <strong class='text-cyan-400'>Positive Terminal (+)</strong>: The raised metal cap at the top, electrically connected to an internal central carbon (graphite) rod.<br>2. <strong class='text-rose-400'>Negative Terminal (-)</strong>: The flat circular metal disc at the bottom, which forms the base of the outer zinc canister container.<br><br>Between the central carbon rod and the outer zinc container lies an electrolyte paste composed of manganese dioxide (MnO₂), ammonium chloride (NH₄Cl), and zinc chloride (ZnCl₂). As the chemicals react, they produce a steady potential difference of approximately 1.5 V. When the chemical reserves are entirely exhausted, the cell stops producing electricity and must be responsibly recycled.",
    "formula": "Chemical Energy (Electrolyte Paste) ➔ [Electrochemical Reaction] ➔ Electrical Energy (V ≈ 1.5 V DC)",
    "key_takeaways": [
      "An electric cell has two distinct terminals: a positive metal cap (+) and a flat negative disc (-).",
      "The cylindrical outer casing is made of zinc metal, serving as the negative electrode.",
      "The central positive terminal connects to an internal carbon/graphite electrode rod surrounded by chemical paste.",
      "A standard dry cell produces a direct current (DC) potential difference of approximately 1.5 V."
    ],
    "checkpoints": [
      {
        "question": "Which physical feature marks the positive (+) terminal of a standard cylindrical dry cell?",
        "options": [
          "The flat metal disc at the base",
          "The raised metal cap at the top",
          "The plastic label wrapping",
          "The hollow side wall"
        ],
        "correct": 1,
        "explanation": "The raised metal cap at the top is the positive (+) terminal, while the flat circular metal disc at the base is the negative (-) terminal."
      },
      {
        "question": "What happens when the internal chemical substances inside an electric cell are completely used up?",
        "options": [
          "The cell automatically recharges itself from atmospheric moisture",
          "The cell stops producing electricity because chemical energy conversion has ceased",
          "The cell explodes with high voltage sparks",
          "The cell transforms into an electrical insulator forever"
        ],
        "correct": 1,
        "explanation": "Dry cells generate electricity via chemical reactions. Once the active chemicals are fully reacted and exhausted, the cell can no longer supply electrical energy."
      }
    ],
    "simulator_type": "cell_anatomy_sim"
  },
  {
    "id": 3,
    "type": "theory_slide",
    "title": "Forming a Battery: Series Connection & Voltage Addition",
    "subtitle": "3.2.2 Battery — Connecting Cells in Series for Greater Electrical Power & Longevity",
    "content": "In everyday speech, people often call a single cell a 'battery', but in physics, a <strong>battery</strong> is defined as a combination of two or more electric cells connected together. To construct a functional battery, the <strong>positive terminal</strong> (+) of the first cell must be connected to the <strong>negative terminal</strong> (-) of the second cell, and so forth.<br><br>When cells are connected end-to-end in this alternating series configuration (+ → − → + → −), their individual electrical voltages add together directly:<br><br><div class=\"p-2 my-2 rounded bg-slate-950 border border-amber-500/30 text-amber-300 font-mono text-center font-bold\">Total Voltage (V_total) = V₁ + V₂ + V₃ + ... + Vₙ</div><br>For example, combining two 1.5 V cells in series provides 3.0 V, illuminating a lamp far brighter than a single cell can. However, if two cells are placed with their like terminals facing each other (+ to + or − to −), their voltages cancel each other out (1.5 V − 1.5 V = 0 V), and no current flows through the circuit!",
    "formula": "Series Rule: V_total = 1.5 V + 1.5 V = 3.0 V   vs   Opposing: 1.5 V − 1.5 V = 0 V",
    "key_takeaways": [
      "A battery consists of two or more electric cells properly connected together.",
      "In a series battery, the positive terminal (+) of one cell connects to the negative terminal (-) of the next.",
      "Series connection sums the voltages: two 1.5 V cells produce 3.0 V; three produce 4.5 V.",
      "Connecting like terminals together (+ to + or - to -) causes voltage cancellation, producing 0 V."
    ],
    "checkpoints": [
      {
        "question": "If you connect three identical 1.5 V cells correctly in series, what total voltage does the battery provide?",
        "options": [
          "1.5 V",
          "3.0 V",
          "4.5 V",
          "0.5 V"
        ],
        "correct": 2,
        "explanation": "In series connection, voltages add together: 1.5 V + 1.5 V + 1.5 V = 4.5 V."
      },
      {
        "question": "What occurs if two 1.5 V cells in a toy car are inserted with their positive terminals touching each other (+ to +)?",
        "options": [
          "The toy car runs at double speed",
          "The two voltages oppose and cancel each other out, so no current flows and the toy does not work",
          "The cells automatically recharge each other",
          "The circuit converts direct current into alternating current"
        ],
        "correct": 1,
        "explanation": "Opposing like terminals (+ to +) create equal and opposite potential differences, yielding a net voltage of 0 V and zero current."
      }
    ],
    "simulator_type": "battery_series_sim"
  },
  {
    "id": 4,
    "type": "theory_slide",
    "title": "Electric Lamps & Modern LEDs: Anatomy & Evolution",
    "subtitle": "3.2.3 Electric Lamp — Tungsten Filament Anatomy vs Solid-State Light Emitting Diodes",
    "content": "To convert electrical energy into visible light, scientists developed two remarkable technologies across history:<br><br>1. <strong class='text-amber-400'>Incandescent Bulb</strong>: Invented in the 19th century, it consists of a transparent glass bulb enclosing a vacuum or inert argon gas, two thick supporting copper wires, and a coiled, hair-thin wire called the <strong>filament</strong>, made of tungsten metal (melting point 3422°C). When electric current flows through the filament, electrical resistance heats it to over 2500°C, making it glow white-hot (incandescence).<br><br>2. <strong class='text-cyan-400'>Light Emitting Diode (LED)</strong>: Modern lighting uses solid-state semiconductor diodes without any fragile glass or burning filament! LEDs consume over 85% less electrical power and produce very little waste heat. Crucially, LEDs have <strong>strict polarity</strong>:<br>- <span class='text-emerald-400 font-bold'>Anode (+)</span>: The <em>longer</em> wire lead (must connect to cell +).<br>- <span class='text-rose-400 font-bold'>Cathode (-)</span>: The <em>shorter</em> wire lead with a flat notch on the plastic rim (connects to cell −).",
    "formula": "Incandescent: Heat ➔ Light (10% Efficient)   ⟷   LED: Direct Electron-Hole Recombination (90% Efficient)",
    "key_takeaways": [
      "An incandescent bulb produces light by heating a coiled tungsten filament until it glows white-hot.",
      "Tungsten is chosen for bulb filaments due to its exceptionally high melting point (3422°C).",
      "Modern LEDs are solid-state semiconductor devices that emit light directly without a filament.",
      "LEDs have strict polarity: longer leg is Anode (+), shorter leg is Cathode (-). Reversing polarity prevents light."
    ],
    "checkpoints": [
      {
        "question": "Which property of tungsten metal makes it uniquely suitable for the filament of an incandescent bulb?",
        "options": [
          "It has a low electrical resistance",
          "It has an extremely high melting point (over 3400°C) and can glow white-hot without melting",
          "It is completely transparent to visible light",
          "It produces negative voltage when heated"
        ],
        "correct": 1,
        "explanation": "Tungsten can withstand temperatures exceeding 2500°C required for bright incandescence without melting or vaporizing rapidly."
      },
      {
        "question": "How can a student identify the positive anode terminal of an unfamiliar LED?",
        "options": [
          "By finding the shorter wire lead",
          "By finding the longer wire lead",
          "By looking for the flat notch on the plastic casing",
          "All LED leads are interchangeable and have no polarity"
        ],
        "correct": 1,
        "explanation": "By universal manufacturing convention, the longer lead of an LED is the positive Anode (+), and the shorter lead is the negative Cathode (-)."
      }
    ],
    "simulator_type": "lamp_vs_led_sim"
  },
  {
    "id": 5,
    "type": "theory_slide",
    "title": "Making a Lamp Glow: Testing Circuit Arrangements",
    "subtitle": "3.2.4 Hands-on Construction — Exploring Complete Loops vs Broken Geometries",
    "content": "To make an electric lamp glow using a cell and two connecting wires, students in the science laboratory test various geometric arrangements. What makes the bulb light up in some setups while remaining completely dark in others?<br><br>The secret lies in establishing an <strong>unbroken continuous loop</strong> connecting both terminals of the power source to both terminals of the lamp:<br><br>• <strong class='text-emerald-400'>Setup A (Working)</strong>: Wire 1 connects cell (+) to lamp base tip; Wire 2 connects lamp metal casing to cell (-). Current has a complete continuous pathway. <em>Bulb glows brightly!</em><br>• <strong class='text-rose-400'>Setup B (Broken Top)</strong>: Top wire is severed or disconnected. Air gap blocks electrical flow. <em>Bulb dark.</em><br>• <strong class='text-rose-400'>Setup C (Broken Bottom)</strong>: Bottom wire is disconnected from cell (-). <em>Bulb dark.</em><br>• <strong class='text-amber-400'>Setup D (Direct Short Circuit)</strong>: Wires connect cell (+) directly to cell (-) without passing through the bulb! The bulb remains dark, while the cell discharges rapidly and heats up dangerously.",
    "formula": "Condition for Glow: Cell (+) Terminal ➔ Wire ➔ Filament ➔ Wire ➔ Cell (−) Terminal (Complete Loop)",
    "key_takeaways": [
      "A lamp glows only when there is an unbroken, continuous loop from one cell terminal, through the lamp filament, back to the other terminal.",
      "Disconnecting either wire creates an air gap that halts electric current completely.",
      "Connecting both ends of a wire to the same terminal of the cell will not light the lamp.",
      "Connecting cell (+) directly to cell (-) bypasses the load (short circuit), causing rapid battery drainage and heating."
    ],
    "checkpoints": [
      {
        "question": "In a classroom circuit experiment, a student connects both wires coming from the bulb to the positive (+) metal cap of the cell only. What happens?",
        "options": [
          "The bulb glows twice as bright",
          "The bulb does not glow because there is no connection to the negative (-) terminal to establish a potential difference",
          "The bulb filament melts instantly",
          "The bulb flashes with red light"
        ],
        "correct": 1,
        "explanation": "Electric current requires a potential difference between (+) and (-) terminals. Connecting both wires to the same terminal provides zero potential difference."
      },
      {
        "question": "What is the danger of connecting the positive and negative terminals of a dry cell directly with a bare copper wire without any bulb or resistor in between?",
        "options": [
          "It creates a short circuit that causes massive current flow, excessive heating, and rapid cell exhaustion",
          "It freezes the electrolyte into a solid crystal",
          "It converts the direct current into alternating current",
          "It increases the cell's lifespan tenfold"
        ],
        "correct": 0,
        "explanation": "A direct connection between terminals without a load is a short circuit. The absence of resistance causes high current, rapid chemical depletion, and overheating."
      }
    ],
    "simulator_type": "circuit_loop_lab_sim"
  },
  {
    "id": 6,
    "type": "theory_slide",
    "title": "The Electrical Circuit: Direction of Current & Closed Loops",
    "subtitle": "3.2.5 Electrical Circuit — Closed Complete Paths vs Open Circuits & Conventional Direction",
    "content": "An <strong>electric circuit</strong> is defined as a closed, conducting loop through which electric charges can continuously flow. When all connections are tight, continuous, and uninterrupted, the circuit is called a <strong class='text-emerald-400'>closed circuit</strong>. If there is a break anywhere in the loop, it is called an <strong class='text-rose-400'>open circuit</strong>, and the current ceases instantly.<br><br><span class='text-cyan-400 font-bold'>Direction of Electric Current:</span><br>By universal scientific convention, established by early physicists like Benjamin Franklin and André-Marie Ampère, the <strong>conventional direction of electric current</strong> in an external circuit is taken to be:<br><br><div class=\"p-2 my-2 rounded bg-slate-950 border border-amber-500/30 text-amber-300 font-mono text-center font-bold\">Current Direction: Positive Terminal (+) ➔ Negative Terminal (−)</div><br>Inside the conducting metallic wires, free subatomic electrons actually drift in the opposite direction (from negative to positive), but standard circuit analysis always follows the conventional positive-to-negative direction.",
    "formula": "Conventional Current (I): Cell (+) ➔ [External Circuit] ➔ Bulb Load ➔ Cell (−)",
    "key_takeaways": [
      "An electric circuit provides a complete closed path for electricity to circulate.",
      "Closed Circuit: Unbroken path, current flows, lamp illuminates.",
      "Open Circuit: Broken path or air gap anywhere in the loop, zero current flows, lamp is dark.",
      "Conventional electric current flows from the positive (+) terminal to the negative (-) terminal outside the cell."
    ],
    "checkpoints": [
      {
        "question": "By international scientific convention, in which direction does electric current flow in the external circuit?",
        "options": [
          "From the negative (-) terminal to the positive (+) terminal",
          "From the positive (+) terminal to the negative (-) terminal",
          "Current flows outward from both terminals simultaneously",
          "Current only flows when the cell is shaken"
        ],
        "correct": 1,
        "explanation": "Conventional current direction is universally defined as flowing from the positive (+) terminal through the circuit to the negative (-) terminal."
      },
      {
        "question": "If a circuit is interrupted by cutting just one connecting wire, what happens to the current in the remaining intact wires?",
        "options": [
          "Current continues flowing up to the cut end and leaks into the air",
          "Current stops completely everywhere throughout the entire loop simultaneously",
          "Current reverses direction",
          "The intact wire catches fire"
        ],
        "correct": 1,
        "explanation": "Electric current requires a continuous unbroken loop. Any break creates an open circuit, instantly halting current throughout the entire circuit."
      }
    ],
    "simulator_type": "current_flow_sim"
  },
  {
    "id": 7,
    "type": "theory_slide",
    "title": "Fused Bulb Diagnostics: Anatomy of a Broken Circuit",
    "subtitle": "3.2.5 Fused Lamps — Thermal Stress, Evaporation & Internal Circuit Discontinuity",
    "content": "Have you ever turned on a light switch only to hear a faint 'click', followed by total darkness? When a bulb fails to light even though the battery and wires are in perfect condition, the bulb is said to be <strong>'fused'</strong>.<br><br>Let us examine the internal anatomy of a fused bulb under a magnifying lens:<br><br>1. <strong class='text-amber-400'>Normal Filament</strong>: A continuous, coiled spring-like tungsten wire bridges the two thick supporting posts.<br>2. <strong class='text-rose-400'>Fused Filament</strong>: Over hundreds of hours of high-temperature operation (2500°C), atoms of tungsten slowly evaporate. Eventually, the thinnest section overheats, melts, and snaps, leaving a microscopic <strong>air gap</strong> between the broken ends.<br><br>Because the filament itself forms an indispensable segment of the circuit's conducting path, a broken filament means the circuit is <strong class='text-rose-400'>open</strong> internally! Even if external wires are securely attached to the terminals, current cannot jump the gap, and the bulb cannot glow.",
    "formula": "Fused Bulb  ⟺  Broken Filament  ⟺  Internal Air Gap  ⟺  Open Circuit (I = 0 A)",
    "key_takeaways": [
      "A bulb is 'fused' when its internal tungsten filament breaks.",
      "Filaments break due to gradual metal evaporation, thermal fatigue, or mechanical shock.",
      "A broken filament introduces an open air gap inside the bulb's glass envelope.",
      "Even in an otherwise complete circuit, a fused bulb prevents current from flowing anywhere in the loop."
    ],
    "checkpoints": [
      {
        "question": "Why does a fused incandescent bulb fail to glow even when connected to a brand new 1.5 V cell?",
        "options": [
          "The glass bulb absorbs all the electricity",
          "The broken filament creates an open break in the circuit, preventing current from circulating",
          "The battery becomes discharged instantly upon touching a fused bulb",
          "The base of the bulb turns into an insulator"
        ],
        "correct": 1,
        "explanation": "The filament is part of the electrical conduction loop. When it snaps, it creates an open circuit with an air gap, blocking all electric current."
      },
      {
        "question": "Which instrument can a student use to test whether a light bulb's filament is intact without seeing through tinted glass?",
        "options": [
          "A mercury thermometer",
          "A conduction tester or multimeter measuring electrical continuity",
          "A magnetic compass placed next to the glass",
          "A litmus paper strip"
        ],
        "correct": 1,
        "explanation": "A conduction tester or multimeter tests continuity. If the filament is intact, current flows; if fused, the tester indicates an open circuit."
      }
    ],
    "simulator_type": "fused_bulb_sim"
  },
  {
    "id": 8,
    "type": "theory_slide",
    "title": "LED Polarity & Unidirectional Conduction (Forward Bias)",
    "subtitle": "3.2.5 Semiconductor Diodes — Why LEDs Act as One-Way Valves for Electric Current",
    "content": "Unlike traditional incandescent bulbs—which glow regardless of which terminal connects to (+) or (-)—modern <strong>Light Emitting Diodes (LEDs)</strong> possess a fascinating property: they only permit electric current to flow in <strong>one specific direction</strong>!<br><br>An LED is made of two joined semiconductor layers: a P-type layer (abundant in positive 'holes') and an N-type layer (abundant in mobile electrons):<br><br>• <strong class='text-emerald-400'>Forward Bias (ON)</strong>: When the longer lead (Anode, +) is connected to the cell's positive terminal and the shorter lead (Cathode, −) is connected to the negative terminal, electrons and holes are pushed toward the central junction. When they recombine, they release energy directly as photons of colored light! <em>LED glows brightly!</em><br>• <strong class='text-rose-400'>Reverse Bias (OFF)</strong>: If connections are swapped (cell (+) to shorter lead, cell (-) to longer lead), the internal junction expands into a wide barrier. Current is completely blocked, and the LED remains dark.<br><br>This one-way valve behavior makes LEDs essential in electronics, rectifiers, indicators, and low-energy lighting.",
    "formula": "Forward Bias: Cell (+) ➔ Anode (Long Lead) & Cell (−) ➔ Cathode (Short Lead)  ⟹  GLOW!",
    "key_takeaways": [
      "Incandescent bulbs have no polarity; they glow equally well with current flowing in either direction.",
      "LEDs are directional semiconductor devices (diodes) that only conduct current in forward bias.",
      "Forward Bias: Cell (+) connected to longer lead (Anode) and Cell (-) to shorter lead (Cathode).",
      "In reverse bias, an LED blocks current flow and does not emit any light."
    ],
    "checkpoints": [
      {
        "question": "A student connects an LED to a 3 V battery, but it does not light up. The battery and wires are verified to be working. What is the most likely issue?",
        "options": [
          "The LED's tungsten filament has melted",
          "The LED is connected in reverse bias with its leads reversed (+ to short lead, - to long lead)",
          "The LED requires alternating current (AC) to function",
          "The connecting wires are made of copper instead of iron"
        ],
        "correct": 1,
        "explanation": "Because LEDs have strict polarity, reversing the leads places the diode in reverse bias, completely blocking current flow. Reversing the connections will light it up."
      },
      {
        "question": "Why do incandescent bulbs light up regardless of which way the battery terminals are connected, unlike LEDs?",
        "options": [
          "Incandescent filaments rely on pure thermal resistance heating, which occurs regardless of current direction",
          "Incandescent bulbs contain two separate filaments for opposite directions",
          "Incandescent bulbs generate their own internal magnetic field",
          "Incandescent bulbs operate only on chemical reactions"
        ],
        "correct": 0,
        "explanation": "Filament heating (H = I²Rt) depends on the square of current and electrical resistance. Heat is generated equally whether current flows clockwise or counter-clockwise."
      }
    ],
    "simulator_type": "led_polarity_sim"
  },
  {
    "id": 9,
    "type": "theory_slide",
    "title": "The Electric Switch: Making a Homemade Safety Pin Switch",
    "subtitle": "3.2.6 Electric Switch — Bridge Mechanism, Air Gaps, ON/OFF States & Control",
    "content": "Imagine having to physically disconnect and reconnect wires with your fingers every time you wanted to turn a lamp on or off! An <strong>electric switch</strong> is a simple, convenient mechanical device designed to break or complete the conducting path in a circuit at will.<br><br>In the school laboratory, you can easily build an elegant switch using three common items: two brass drawing pins, an iron safety pin, and a cardboard or thermocol base:<br><br>1. Push one drawing pin through the ring end of the safety pin into the cardboard base, securing it in place while allowing the pin to rotate freely.<br>2. Press a second drawing pin into the board a small distance away, so the free metal tip of the safety pin can touch it.<br>3. Connect one circuit wire to each drawing pin.<br><br>• <strong class='text-emerald-400'>Switch in 'ON' Position (Closed)</strong>: The safety pin rotates to rest on both drawing pins. Being made of steel (a good conductor), it bridges the gap, allowing current to flow continuously. <em>Bulb lights up!</em><br>• <strong class='text-rose-400'>Switch in 'OFF' Position (Open)</strong>: The safety pin is rotated away. An <strong>air gap</strong> is created. Since air is an electrical insulator, current cannot jump the gap. <em>Bulb turns off instantly!</em>",
    "formula": "Switch ON: Metallic Bridge ➔ Closed Circuit (I > 0)   ⟷   Switch OFF: Air Gap ➔ Open Circuit (I = 0)",
    "key_takeaways": [
      "A switch is a control device used to easily open or close an electric circuit.",
      "When the switch is in the ON position, it provides a continuous metallic conducting path (closed circuit).",
      "When the switch is in the OFF position, it introduces an insulating air gap that breaks the circuit (open circuit).",
      "A switch can be placed anywhere in the circuit loop; opening it stops current throughout the entire loop."
    ],
    "checkpoints": [
      {
        "question": "What is present between the contacts of an electric switch when it is switched to the OFF position?",
        "options": [
          "A vacuum chamber that traps electricity",
          "An air gap, which acts as an electrical insulator and prevents current from flowing",
          "A layer of liquid copper",
          "A magnetic shield"
        ],
        "correct": 1,
        "explanation": "In the OFF position, switch contacts are physically separated by an air gap. Air is an insulator, so current cannot cross it at low cell voltages."
      },
      {
        "question": "Does it matter where in a simple single-loop circuit a switch is placed (near the positive terminal, near the negative terminal, or next to the bulb)?",
        "options": [
          "Yes, it only works if placed directly touching the positive terminal",
          "No, opening the switch breaks the single loop and stops current everywhere regardless of its location",
          "Yes, placing it near the negative terminal causes the battery to drain backwards",
          "Yes, switches only work when placed inside the bulb socket"
        ],
        "correct": 1,
        "explanation": "In a series single-loop circuit, current is identical everywhere. A break anywhere in the loop halts current flow across the entire circuit."
      }
    ],
    "simulator_type": "switch_mechanism_sim"
  },
  {
    "id": 10,
    "type": "theory_slide",
    "title": "Circuit Diagrams: Standard Universal Schematic Symbols",
    "subtitle": "3.3 Circuit Diagrams — Representing Electrical Components with Clean Engineering Symbols",
    "content": "Drawing realistic sketches of cells, wires, safety pins, and glass bulbs is time-consuming and often confusing. To communicate electrical circuits clearly across the globe, scientists and engineers invented a universal visual language called <strong>circuit symbols</strong>.<br><br>Here are the standard NCERT symbols you must master:<br><br>1. <strong class='text-cyan-400'>Electric Cell</strong>: One long, thin vertical line (representing the positive terminal, +) paired with a parallel shorter, thicker vertical line (representing the negative terminal, −).<br>2. <strong class='text-purple-400'>Battery</strong>: A series of alternating long thin and short thick lines, showing cells joined + → − → + → −.<br>3. <strong class='text-amber-400'>Electric Bulb</strong>: A circle containing a loop resembling a curled filament, or a circle with a cross inside.<br>4. <strong class='text-emerald-400'>Switch in 'ON' Position</strong>: A solid straight line connecting two filled circular terminal dots (●—●).<br>5. <strong class='text-rose-400'>Switch in 'OFF' Position</strong>: A line lifted up at an angle away from one terminal dot, clearly showing an air gap (● / ●).<br>6. <strong class='text-slate-300'>Connecting Wire</strong>: Clean, straight horizontal or vertical lines.",
    "formula": "Cell Symbol: (+) Long Thin Line | Short Thick Line (−)     Battery: (+) | ❚ | ❚ (−)",
    "key_takeaways": [
      "Circuit diagrams use standardized symbols so that anyone in the world can understand and build the circuit.",
      "Electric Cell: Long thin line = Positive (+) terminal; Short thick line = Negative (-) terminal.",
      "Battery: Combination of multiple alternating cell symbols connected in series.",
      "Switch ON is drawn as a closed bridge connecting two dots; Switch OFF is drawn tilted open with a visible gap."
    ],
    "checkpoints": [
      {
        "question": "In the standard schematic symbol for an electric cell, what does the longer, thinner parallel line represent?",
        "options": [
          "The negative (-) terminal",
          "The positive (+) terminal",
          "The internal electrolyte paste",
          "The switch lever"
        ],
        "correct": 1,
        "explanation": "By international convention, the longer and thinner line represents the positive (+) terminal, while the shorter and thicker line represents the negative (-) terminal."
      },
      {
        "question": "How is a switch in the 'OFF' (open) position depicted in a circuit schematic diagram?",
        "options": [
          "As two dots with a line bridging them horizontally",
          "As a line tilted upward at an angle, showing an open gap between the terminal dots",
          "As a circle with an 'X' through it",
          "As a zigzag line"
        ],
        "correct": 1,
        "explanation": "A tilted line showing an air gap between terminal dots visually indicates that the circuit is broken and open (OFF position)."
      }
    ],
    "simulator_type": "symbols_rosetta_sim"
  },
  {
    "id": 11,
    "type": "theory_slide",
    "title": "Drawing & Analyzing Circuit Schematics",
    "subtitle": "3.3 Circuit Diagrams — Translating Physical Workbench Setups into Clean Schematics",
    "content": "A <strong>circuit diagram</strong> (or schematic) is a visual blueprint that represents an electrical circuit using standard symbols instead of pictorial drawings. When drawing circuit diagrams, engineers follow golden drafting conventions:<br><br>1. Connecting wires are always drawn as <strong>straight horizontal and vertical lines</strong> with crisp 90° right-angled corners, forming a neat rectangular layout.<br>2. Components (cells, switches, lamps) are placed along the straight line paths, never jammed into tight corners.<br>3. The state of the switch (open or closed) immediately tells you whether current is circulating.<br><br>Let us trace a standard circuit schematic: Starting at the long line of the cell (+), the path follows a straight wire through a closed switch (●—●), through the bulb symbol (⨂), and returns along a bottom wire to the short thick line of the cell (-). Because the loop is completely closed without any gaps, current circulates and the bulb glows!",
    "formula": "Physical Components (Cell + Wire + Switch + Bulb) ➔ [Symbolic Translation] ➔ Clean Rectangular Blueprint",
    "key_takeaways": [
      "A circuit diagram represents an electrical circuit using standardized schematic symbols.",
      "Wires are drawn as clean straight lines with 90° rectangular turns for maximum clarity.",
      "Tracing the continuous loop from (+) to (-) allows quick visual verification of circuit completeness.",
      "Schematic blueprints are used by scientists, electricians, and engineers worldwide."
    ],
    "checkpoints": [
      {
        "question": "Why do engineers and scientists prefer circuit schematic diagrams over realistic artistic drawings of batteries and bulbs?",
        "options": [
          "Schematic symbols are universally understood, faster to draw, and eliminate ambiguity regardless of artistic skill",
          "Realistic drawings conduct real electricity through paper",
          "Schematic symbols make light bulbs glow brighter",
          "Drawing realistic batteries is illegal in science labs"
        ],
        "correct": 0,
        "explanation": "Universal symbols allow anyone anywhere in the world to understand, analyze, and construct electrical circuits accurately and without confusion."
      },
      {
        "question": "When inspecting a circuit diagram, you notice a gap where the switch line does not touch the second dot. What is the state of the circuit?",
        "options": [
          "Closed circuit, current flows, bulb is ON",
          "Open circuit, current is zero, bulb is OFF",
          "Short circuit, wires will melt",
          "Alternating current circuit"
        ],
        "correct": 1,
        "explanation": "A visible gap at the switch indicates the switch is in the open/OFF position. The circuit is open, so no current flows and the bulb is OFF."
      }
    ],
    "simulator_type": "schematic_designer_sim"
  },
  {
    "id": 12,
    "type": "theory_slide",
    "title": "Circuit Architectures: Single Loop (Series) vs Branching",
    "subtitle": "3.3 Circuit Configurations — Comparing What Happens When One Bulb Is Removed",
    "content": "When connecting multiple lamps in a circuit, there are two fundamental ways to arrange them:<br><br>1. <strong class='text-cyan-400'>Series Circuit (Single Loop)</strong>:<br>All lamps are connected one after another in a single unbroken loop (+ → Bulb 1 → Bulb 2 → -). Electric current has only <em>one single pathway</em> to travel. If one bulb burns out or is unscrewed, the single pathway is broken, creating an open circuit! As a result, <strong>all other bulbs turn off instantly</strong>. Furthermore, sharing the voltage causes each additional bulb to glow dimmer.<br><br>2. <strong class='text-emerald-400'>Parallel Circuit (Independent Branches)</strong>:<br>Each lamp is connected on its own independent branch directly across the battery terminals. Current divides into separate pathways. If one bulb burns out or is removed, current continues flowing through the other independent branches uninterrupted! This is why all household appliances and decorative festival lights are wired in parallel.",
    "formula": "Series: Single Path (I_total = I₁ = I₂)   ⟷   Parallel: Independent Branches (I_total = I₁ + I₂)",
    "key_takeaways": [
      "In a series circuit, components are connected along a single continuous path; current is identical everywhere.",
      "If one bulb fuses or is disconnected in a series circuit, all other bulbs in that circuit go out immediately.",
      "In a parallel circuit, each component has its own separate branch connected to the power source.",
      "If one branch in a parallel circuit is broken, other branches continue working independently. Homes use parallel wiring."
    ],
    "checkpoints": [
      {
        "question": "Two bulbs are connected in a single series loop with a battery. If one bulb fuses (breaks its filament), what happens to the second bulb?",
        "options": [
          "The second bulb glows twice as bright",
          "The second bulb immediately goes out because the single continuous loop is broken",
          "The second bulb changes color to blue",
          "The second bulb continues glowing with unchanged brightness"
        ],
        "correct": 1,
        "explanation": "In a series circuit, all components share the same single path. If one bulb fuses, it creates an open circuit, stopping current throughout the entire loop."
      },
      {
        "question": "Why are electrical lights, fans, and appliances in homes wired in parallel circuits rather than in series?",
        "options": [
          "So that turning off or unplugging one appliance does not shut off every other appliance in the house",
          "Because parallel circuits do not require any electrical power source",
          "Because series circuits cannot use copper wires",
          "Because parallel circuits convert electrical energy into water"
        ],
        "correct": 0,
        "explanation": "Parallel wiring ensures that each appliance operates independently on its own branch, maintaining full mains voltage (230 V) even if other appliances are switched off."
      }
    ],
    "simulator_type": "series_parallel_sim"
  },
  {
    "id": 13,
    "type": "theory_slide",
    "title": "Conductors and Insulators: Conduction Tester Lab",
    "subtitle": "3.4 Electrical Conductors and Insulators — Testing Material Properties with an Open Probe Gap",
    "content": "Why are electrical wires made of shiny copper metal inside, yet coated with colorful plastic on the outside? To understand this, we classify all materials based on how easily they allow electric charges to travel through them:<br><br>A <strong>conduction tester</strong> is simply a basic circuit consisting of a cell and a bulb, where the two connecting wires are left with exposed free ends (probes A and B). When an object is placed between probes A and B:<br><br>1. <strong class='text-emerald-400'>Electrical Conductors</strong>: Materials that allow electric current to pass through them freely due to abundant mobile electrons. When a conductor bridges the probes, the circuit closes and the <strong>lamp glows brightly</strong>. <em>Examples:</em> Copper, aluminum, iron, brass, gold, graphite (pencil lead), and tap water / salt solution.<br>2. <strong class='text-rose-400'>Electrical Insulators (Poor Conductors)</strong>: Materials that strongly resist and block the flow of electric charges. When an insulator bridges the probes, the circuit remains effectively open and the <strong>lamp remains dark</strong>. <em>Examples:</em> Plastic, rubber, dry wood, glass, ceramics, air, and pure distilled water.",
    "formula": "Conductor: Low Resistance (R ≈ 0 Ω) ➔ Bulb GLOWS   ⟷   Insulator: High Resistance (R → ∞) ➔ Bulb DARK",
    "key_takeaways": [
      "Conductors allow electric current to pass through them easily with very low resistance.",
      "Metals (copper, aluminum, iron, silver) and pencil graphite are excellent electrical conductors.",
      "Insulators do not allow electric current to pass through them easily under normal voltages.",
      "Non-metals like rubber, plastics, dry wood, glass, and air are good electrical insulators."
    ],
    "checkpoints": [
      {
        "question": "Which of the following everyday objects will cause the bulb of a conduction tester to glow when placed between the test probes?",
        "options": [
          "A plastic ruler",
          "A wooden toothpick",
          "An iron paper clip",
          "A rubber eraser"
        ],
        "correct": 2,
        "explanation": "An iron paper clip is made of metal (iron/steel), which is a good electrical conductor that completes the circuit, allowing the bulb to glow."
      },
      {
        "question": "Pencil lead is not made of lead metal, but of graphite (a form of carbon). What happens when pencil lead is tested with a conduction tester?",
        "options": [
          "The bulb glows because graphite is an excellent non-metal electrical conductor",
          "The bulb does not glow because graphite is a total insulator",
          "The pencil lead melts into liquid glass",
          "The battery reverses its polarity"
        ],
        "correct": 0,
        "explanation": "Graphite is a unique crystalline allotrope of carbon featuring delocalized mobile electrons, making it a good non-metal conductor."
      }
    ],
    "simulator_type": "conduction_tester_sim"
  },
  {
    "id": 14,
    "type": "theory_slide",
    "title": "Wire Insulation: Engineering Safety & Preventing Short Circuits",
    "subtitle": "3.4 Conductor-Insulator Synergy — PVC Sheaths, Core Conductors & Electrical Safety",
    "content": "Every power cord and connecting wire in modern technology represents a brilliant synergy between <strong>conductors</strong> and <strong>insulators</strong> working together in harmony:<br><br>• <strong class='text-amber-400'>The Inner Core (Conductor)</strong>: Made of multiple fine strands of high-purity copper or aluminum metal. Copper is chosen for its superb electrical conductivity, mechanical flexibility, and low resistance, ensuring that electrical energy travels long distances with minimal heat dissipation (P = I²R).<br><br>• <strong class='text-cyan-400'>The Outer Sheath (Insulator)</strong>: Made of Polyvinyl Chloride (PVC) plastic or synthetic rubber. This thick insulating jacket accomplishes two vital safety functions:<br>1. <span class='text-emerald-400 font-bold'>User Protection</span>: It prevents humans from directly touching the live high-voltage metal core, protecting us from electric shocks.<br>2. <span class='text-rose-400 font-bold'>Short Circuit Prevention</span>: It prevents adjacent bare wires from accidentally touching each other, which would otherwise create a dangerous short circuit, catastrophic sparks, or electrical fires.",
    "formula": "Safe Power Cable = Copper Core (Good Conductor) + PVC Outer Sheath (Protective Insulator)",
    "key_takeaways": [
      "Electrical cables combine a metallic inner conductor with a flexible plastic/rubber insulating jacket.",
      "Copper is the primary metal chosen for wires due to its high conductivity and high malleability.",
      "Insulating PVC coating protects humans from electric shock when handling plugged-in cables.",
      "Insulation prevents bare wires from touching each other, eliminating dangerous short circuits and electrical fires."
    ],
    "checkpoints": [
      {
        "question": "Why are electrical transmission cords in our homes wrapped in PVC plastic or rubber coatings?",
        "options": [
          "To make the cables heavier so they do not blow away in the wind",
          "Because plastic is an insulator that protects humans from electric shock and prevents bare wires from touching",
          "To generate extra electricity from ambient room heat",
          "To keep the copper wire warm so electricity flows faster"
        ],
        "correct": 1,
        "explanation": "Plastic and rubber are insulators. They prevent electric current from leaking to human hands and stop adjacent wires from touching and causing short circuits."
      },
      {
        "question": "Before connecting a plastic-coated wire to a cell or lamp holder in a lab experiment, what critical step must be performed on the wire ends?",
        "options": [
          "Soak the wire in cold water for an hour",
          "Strip off about 1-2 cm of the plastic insulating coating to expose the bare metallic copper conductor",
          "Paint the plastic ends with black ink",
          "Burn the entire wire with a match"
        ],
        "correct": 1,
        "explanation": "Plastic is an insulator. If the plastic is not stripped off, the insulating coating prevents metallic electrical contact between the cell and the wire."
      }
    ],
    "simulator_type": "wire_insulation_sim"
  },
  {
    "id": 15,
    "type": "theory_slide",
    "title": "Electrician Safety: Tools, Rubber PPE & Human Body Conduction",
    "subtitle": "3.4 Conduction in Practice — Why Electricians Wear Rubber & The Wet Skin Hazard",
    "content": "Have you noticed the specialized tools used by professional electricians? Their screwdrivers, pliers, and wire cutters feature thick handles made of tough molded plastic or rubber. Furthermore, electricians always wear heavy rubber-soled boots and thick rubber gloves when repairing electrical switches or overhead wires.<br><br><span class='text-rose-400 font-bold'>Is the Human Body a Conductor or an Insulator?</span><br>The human body is an <strong>electrical conductor</strong>! Over 60% of our body weight consists of water rich in dissolved electrolytes (sodium Na⁺, potassium K⁺, and chloride Cl⁻ ions). If a person touches an exposed live wire while in contact with the ground, electric current will flow right through their body to the earth, causing severe muscle spasms, cardiac arrest, or death.<br><br>• <strong class='text-cyan-400'>Dry Skin vs Wet Skin</strong>: Dry skin offers substantial electrical resistance (100,000 Ω). However, when skin is wet from water or sweat, its electrical resistance plummets to under 1,000 Ω—allowing lethal currents to surge through easily! This is why you must <strong>never touch electrical switches with wet hands</strong>.",
    "formula": "R_dry skin ≈ 100,000 Ω   ➔   [Water / Sweat]   ➔   R_wet skin ≈ 1,000 Ω (100-Fold Shock Danger!)",
    "key_takeaways": [
      "The human body is a conductor of electricity due to dissolved ions and water in our tissues.",
      "Water with dissolved mineral salts conducts electricity; wet hands dramatically lower skin resistance.",
      "Never touch electrical switches, plugs, or appliances with wet hands or while standing on a wet floor.",
      "Electricians wear thick rubber gloves and shoes because rubber is an insulator that prevents current from reaching the ground."
    ],
    "checkpoints": [
      {
        "question": "Why is it extremely dangerous to operate an electric switch or plug in an appliance with wet hands?",
        "options": [
          "Water makes the plastic switch dissolve",
          "Water conducts electricity and lowers skin resistance, allowing dangerous current to flow through the body",
          "Water drains the power station's generators immediately",
          "Water turns alternating current into static sparks"
        ],
        "correct": 1,
        "explanation": "Water contains dissolved salts, making it a good conductor. Wet hands drop skin resistance dramatically, dramatically increasing the risk of electric shock."
      },
      {
        "question": "Why do the handles of screwdrivers and pliers used by electricians have thick covers of plastic or rubber?",
        "options": [
          "To make the tools look colorful and attractive",
          "Rubber and plastic are insulators that block current, protecting the electrician from electric shocks during repairs",
          "To make the tools float on water",
          "To keep the steel blades from getting cold"
        ],
        "correct": 1,
        "explanation": "Rubber and plastic insulation ensures that even if the metal tip touches a live electrical wire, current cannot travel through the handle into the technician's hand."
      }
    ],
    "simulator_type": "electrician_safety_sim"
  },
  {
    "id": 16,
    "type": "theory_slide",
    "title": "Indian Heritage: Acharya J.C. Bose & Semiconductor Diodes",
    "subtitle": "Pioneering Indian Science — Millimetre Waves, Galena Crystal Detectors & The Ancestor of the LED",
    "content": "India has a proud, pioneering heritage at the forefront of electrical and semiconductor physics! Long before modern silicon microchips and Light Emitting Diodes (LEDs) were commercialized, the great Indian polymath and physicist <strong>Acharya Jagadish Chandra Bose</strong> (1858–1937) conducted revolutionary electrical research in Kolkata.<br><br>In 1895, J.C. Bose publicly demonstrated the generation and wireless transmission of millimetre-wavelength electromagnetic waves (60 GHz, wavelength ≈ 5 mm), ringing a bell and detonating gunpowder through closed walls at Kolkata Town Hall—predating Marconi's commercial demonstrations.<br><br>To detect these high-frequency electrical signals, Bose invented the world's first solid-state semiconductor point-contact diode using a crystal of <strong>galena</strong> (lead sulfide, PbS). He was granted US Patent No. 755,840 in 1904 for this crystal detector—making him the recognized grandfather of modern semiconductor diodes, microwave engineering, and the solid-state physics that powers modern LEDs!",
    "formula": "J.C. Bose (1904): Galena Semiconductor Crystal Detector ➔ Modern Solid-State Diodes & LEDs",
    "key_takeaways": [
      "Acharya Jagadish Chandra Bose was a legendary Indian scientist who pioneered wireless microwave communication.",
      "In 1895, Bose generated 5 mm electromagnetic waves and transmitted them through walls in Kolkata.",
      "Bose invented the galena crystal detector in 1904, the first solid-state semiconductor diode in history.",
      "His semiconductor research laid the foundational physics that eventually gave rise to modern transistors and LEDs."
    ],
    "checkpoints": [
      {
        "question": "What historic semiconductor device did Acharya Jagadish Chandra Bose invent and patent in 1904?",
        "options": [
          "The steam engine turbine",
          "The galena crystal point-contact detector, the earliest solid-state semiconductor diode",
          "The rechargeable lithium-ion battery",
          "The mercury thermometer"
        ],
        "correct": 1,
        "explanation": "Acharya J.C. Bose patented the galena crystal detector (US Patent 755,840 in 1904), which was the first solid-state semiconductor diode used to detect radio waves."
      },
      {
        "question": "What groundbreaking scientific demonstration did Acharya J.C. Bose perform at Kolkata Town Hall in 1895?",
        "options": [
          "He split water into hydrogen and oxygen using an electric cell",
          "He generated 5 mm microwave electromagnetic waves that passed through walls to ring a bell wirelessly",
          "He invented the incandescent light bulb before Edison",
          "He mapped the human nervous system using an optical microscope"
        ],
        "correct": 1,
        "explanation": "In 1895, Bose generated millimetre microwave radiation, transmitting signals wirelessly through walls to ring a bell and ignite gunpowder remotely."
      }
    ],
    "simulator_type": "jc_bose_heritage_sim"
  },
  {
    "id": 17,
    "type": "quiz_slide",
    "title": "Mastery Assessment: Cells, Torches & Safety Fundamentals",
    "subtitle": "Challenge Inquiries 1 to 10 — Terminals, Potential Difference, Batteries & Lab Safety",
    "questions": [
      {
        "question": "1. What is the primary reason classroom science experiments must strictly use dry cells rather than domestic wall sockets?",
        "options": [
          "Wall socket electricity is too weak to light small bulbs",
          "Domestic sockets supply 230 V AC mains voltage, which poses severe risks of lethal shock and burns",
          "Wall sockets produce direct current that destroys copper wires",
          "Dry cells produce brighter light than mains electricity"
        ],
        "correct": 1,
        "solution": "Domestic electricity operates at 230 V AC, which can drive lethal currents through human tissue, causing severe muscle paralysis, burns, and cardiac arrest. Dry cells supply safe low-voltage direct current (1.5 V to 9 V)."
      },
      {
        "question": "2. Which metal forms the cylindrical outer casing and flat negative (-) terminal of a standard dry cell?",
        "options": [
          "Copper",
          "Zinc",
          "Iron",
          "Aluminum"
        ],
        "correct": 1,
        "solution": "In a standard Leclanché dry cell, the outer can is made of zinc metal, which serves as the negative electrode (anode) where oxidation takes place. The flat metal disc at the bottom connects to this zinc can."
      },
      {
        "question": "3. The positive terminal of a standard cylindrical dry cell is identified by:",
        "options": [
          "A raised metal cap at the top",
          "A flat circular metal disc at the bottom",
          "A plastic seal around the side wall",
          "A green stripe on the label"
        ],
        "correct": 0,
        "solution": "The raised metal cap at the top connects directly to the internal central carbon (graphite) rod, forming the positive (+) terminal of the dry cell."
      },
      {
        "question": "4. How must two 1.5 V cells be connected to construct a working 3.0 V battery in series?",
        "options": [
          "Positive terminal of the first cell connected to positive terminal of the second cell (+ to +)",
          "Positive terminal of the first cell connected to negative terminal of the second cell (+ to -)",
          "Negative terminal of the first cell connected to negative terminal of the second cell (- to -)",
          "By placing both cells in a glass of water"
        ],
        "correct": 1,
        "solution": "In a series battery, the positive terminal of one cell must connect to the negative terminal of the next cell (+ to -). This allows their individual potential differences to add constructively: V_total = 1.5 V + 1.5 V = 3.0 V."
      },
      {
        "question": "5. What total voltage is produced if four 1.5 V cells are correctly connected in series?",
        "options": [
          "1.5 V",
          "3.0 V",
          "4.5 V",
          "6.0 V"
        ],
        "correct": 3,
        "solution": "In series combination, voltages sum directly: V_total = 1.5 V + 1.5 V + 1.5 V + 1.5 V = 6.0 V."
      },
      {
        "question": "6. If two identical 1.5 V cells are connected with their positive terminals touching (+ to +), what is the resulting net voltage across the outer terminals?",
        "options": [
          "3.0 V",
          "0.0 V",
          "1.5 V",
          "4.5 V"
        ],
        "correct": 1,
        "solution": "Opposing like terminals (+ to +) create equal and opposite electromotive forces that cancel each other out: V_net = 1.5 V − 1.5 V = 0.0 V. No current flows through the external circuit."
      },
      {
        "question": "7. What provides the mechanical force in a torchlight to keep the electric cells in continuous electrical contact?",
        "options": [
          "A compressed air cushion",
          "A coiled metal spring at the base cap",
          "A layer of sticky glue",
          "A magnetic latch"
        ],
        "correct": 1,
        "solution": "The helical metal spring at the screw-on base cap is compressed when closed, exerting continuous elastic pressure that holds the cells firmly against each other and against the bulb base."
      },
      {
        "question": "8. What transformation of energy occurs when an electric cell operates in a closed circuit with a bulb?",
        "options": [
          "Nuclear energy converts directly into sound energy",
          "Chemical energy converts into electrical energy, which converts into heat and light energy",
          "Mechanical energy converts into gravitational energy",
          "Light energy converts into chemical potential energy"
        ],
        "correct": 1,
        "solution": "Chemical reactions in the electrolyte paste generate electrical potential energy (voltage). When current flows through the filament, electrical energy transforms into thermal energy and visible light radiation."
      },
      {
        "question": "9. Why does a standard primary dry cell eventually stop working permanently?",
        "options": [
          "The glass bulb absorbs all the electrons",
          "The chemical reactants inside the cell are completely consumed and exhausted",
          "The copper wires turn into rubber",
          "The atmospheric pressure pushes the terminals apart"
        ],
        "correct": 1,
        "solution": "A primary cell functions by consuming internal chemical reactants (zinc, manganese dioxide). Once these chemical reserves are fully converted to products, the reaction stops and cannot generate further electricity."
      },
      {
        "question": "10. Which of the following power sources is safe for Grade 7 students to use for classroom tabletop circuit experiments?",
        "options": [
          "A domestic 230 V wall socket",
          "A diesel-powered home backup generator",
          "A standard 1.5 V AA dry cell or 9 V transistor battery",
          "An overhead electric train high-tension wire"
        ],
        "correct": 2,
        "solution": "A 1.5 V AA cell or 9 V battery supplies safe, low-voltage direct current that cannot penetrate the electrical resistance of human skin or cause hazardous shocks."
      }
    ]
  },
  {
    "id": 18,
    "type": "quiz_slide",
    "title": "Mastery Assessment: Bulb Anatomy, LEDs & Closed Circuits",
    "subtitle": "Challenge Inquiries 11 to 20 — Tungsten Filaments, LED Polarity & Fused Bulbs",
    "questions": [
      {
        "question": "11. Why is tungsten metal exclusively chosen for the filament of traditional incandescent light bulbs?",
        "options": [
          "It has the lowest electrical resistance of all metals",
          "It has an extraordinarily high melting point (3422°C) and can glow white-hot without melting",
          "It is a liquid at room temperature",
          "It attracts magnetic lines of force"
        ],
        "correct": 1,
        "solution": "Incandescent lighting requires heating a filament wire to over 2500°C. Tungsten's ultra-high melting point (3422°C) allows it to maintain structural integrity and incandesce brightly without melting."
      },
      {
        "question": "12. In an incandescent bulb, where are the two electrical terminals located?",
        "options": [
          "Both terminals are located on top of the glass dome",
          "One terminal is at the metallic base tip, and the other is the metal threaded casing",
          "Inside the vacuum sealed chamber",
          "On the plastic support stem"
        ],
        "correct": 1,
        "solution": "One lead from the filament connects to the center metal contact point at the bottom tip, while the other lead connects to the outer metal cylindrical casing. The two are separated by an insulating ceramic barrier."
      },
      {
        "question": "13. What physical feature identifies the positive Anode terminal of a light-emitting diode (LED)?",
        "options": [
          "The shorter wire lead",
          "The longer wire lead",
          "The flat cut on the plastic rim",
          "The colored lens"
        ],
        "correct": 1,
        "solution": "By international convention, the longer external metal lead of an LED is the positive Anode (+), while the shorter lead (often next to a flat rim edge) is the negative Cathode (-)."
      },
      {
        "question": "14. What occurs when an LED is connected in reverse bias (cell positive connected to the shorter lead)?",
        "options": [
          "The LED emits ultraviolet light",
          "The LED conducts zero current and produces no light",
          "The LED shines ten times brighter",
          "The LED becomes an electric cell"
        ],
        "correct": 1,
        "solution": "An LED is a semiconductor diode. In reverse bias, the internal depletion zone widens, creating an enormous barrier that completely blocks electric current, so no photons are emitted."
      },
      {
        "question": "15. What is the fundamental cause of an incandescent light bulb becoming 'fused'?",
        "options": [
          "The glass envelope turns into solid carbon",
          "The thin tungsten filament has snapped or melted, creating an open air gap in the circuit",
          "The cell's voltage has doubled",
          "The copper wires have evaporated"
        ],
        "correct": 1,
        "solution": "A bulb fuses when its tungsten filament breaks due to thermal stress, mechanical vibration, or metal evaporation. The break introduces an open air gap inside the bulb, stopping current."
      },
      {
        "question": "16. By international scientific convention, what is the direction of electric current in an external circuit?",
        "options": [
          "From negative (-) terminal to positive (+) terminal",
          "From positive (+) terminal to negative (-) terminal",
          "From the center of the wire outward to the insulation",
          "Current only moves back and forth without traveling"
        ],
        "correct": 1,
        "solution": "Conventional current is defined as flowing from the positive (+) terminal through the external circuit components to the negative (-) terminal of the cell."
      },
      {
        "question": "17. Why do LEDs consume far less electrical energy than incandescent bulbs for the same amount of visible light?",
        "options": [
          "LEDs convert electricity directly into light via electron-hole recombination, wasting very little energy as heat",
          "LEDs use invisible light that does not require energy",
          "LEDs create electricity out of thin air",
          "LEDs only work in cold weather"
        ],
        "correct": 0,
        "solution": "Incandescent bulbs waste over 90% of electrical energy as thermal infrared heat before glowing. LEDs emit light directly via quantum semiconductor recombination, achieving up to 90% luminous efficiency."
      },
      {
        "question": "18. A student connects a circuit with a cell, wire, and bulb, but the bulb does not glow. Which of the following is NOT a plausible reason?",
        "options": [
          "The bulb filament is broken (fused)",
          "The cell is completely discharged",
          "The copper wire is a good conductor of electricity",
          "There is a loose connection or gap in the wire loop"
        ],
        "correct": 2,
        "solution": "Copper being a good conductor is precisely the condition required for current to flow. A broken filament, dead cell, or loose connection would each cause the circuit to fail."
      },
      {
        "question": "19. What is the state of an electrical circuit when all connections are tight, intact, and continuous?",
        "options": [
          "Open circuit",
          "Closed circuit",
          "Short circuit",
          "Gapped circuit"
        ],
        "correct": 1,
        "solution": "A complete, unbroken conducting path from one terminal of the source to the other is defined as a closed circuit. Current flows freely and loads operate."
      },
      {
        "question": "20. What happens if you connect both terminals of a light bulb to the negative (-) terminal of a cell simultaneously with two wires?",
        "options": [
          "The bulb glows normally",
          "The bulb does not glow because there is zero electrical potential difference between identical terminals",
          "The bulb explodes",
          "The bulb turns into a magnet"
        ],
        "correct": 1,
        "solution": "Electric current requires a potential difference (voltage) between two points (V_A − V_B > 0). Connecting to the same terminal provides 0 V potential difference, so no current flows."
      }
    ]
  },
  {
    "id": 19,
    "type": "quiz_slide",
    "title": "Mastery Assessment: Switches, Circuit Symbols & Schematics",
    "subtitle": "Challenge Inquiries 21 to 30 — Schematic Diagrams, Universal Symbols & Circuit Control",
    "questions": [
      {
        "question": "21. What mechanical action occurs inside a switch when it is moved to the 'ON' position?",
        "options": [
          "An insulating air gap is introduced between terminals",
          "A metallic conducting bridge closes the gap between terminals, completing the circuit loop",
          "The voltage of the battery is doubled",
          "The wires are physically cut"
        ],
        "correct": 1,
        "solution": "In the ON position, the internal metallic contact moves to touch both terminal contacts, bridging the gap with a low-resistance conductor and closing the circuit."
      },
      {
        "question": "22. In the standard circuit symbol for an electric cell, how is the negative (-) terminal drawn?",
        "options": [
          "As a long, thin vertical line",
          "As a short, thick vertical line",
          "As a circle with an arrow",
          "As a wavy zigzag line"
        ],
        "correct": 1,
        "solution": "By international schematic convention, the negative (-) terminal is depicted as a short, thick line, while the positive (+) terminal is a longer, thinner parallel line."
      },
      {
        "question": "23. How is an electric switch in the 'OFF' (open) position represented in a circuit diagram?",
        "options": [
          "As a line resting horizontally between two terminal dots",
          "As a straight line tilted upward away from one of the terminal dots, showing an open gap",
          "As a closed square",
          "As a circle with a cross inside"
        ],
        "correct": 1,
        "solution": "A tilted line showing an air gap between terminal dots represents an open switch in the OFF position, indicating that current flow is interrupted."
      },
      {
        "question": "24. In a circuit schematic, what does a continuous straight horizontal or vertical line represent?",
        "options": [
          "A high-resistance heating coil",
          "A conducting connecting wire with negligible electrical resistance",
          "An insulating plastic strip",
          "A glass tube"
        ],
        "correct": 1,
        "solution": "Straight lines represent conducting wires (typically copper) that connect components together with virtually zero electrical resistance."
      },
      {
        "question": "25. Which schematic symbol represents an electric bulb in standard circuit diagrams?",
        "options": [
          "A rectangle with a diagonal stripe",
          "A circle containing an internal curved filament loop or a cross",
          "Two parallel vertical lines of equal length",
          "A triangle pointing to a vertical bar"
        ],
        "correct": 1,
        "solution": "An incandescent lamp is universally symbolized by a circle enclosing an internal filament loop or a cross."
      },
      {
        "question": "26. What happens if a switch is placed on the negative (-) return side of a circuit instead of the positive (+) side?",
        "options": [
          "The switch will fail to work and the bulb will stay on permanently",
          "The circuit functions perfectly; opening the switch breaks the loop regardless of where it is positioned",
          "The battery will short-circuit",
          "The bulb will flicker with alternating current"
        ],
        "correct": 1,
        "solution": "In a single series loop, current is continuous throughout. A break anywhere in the loop—whether near the positive terminal, negative terminal, or bulb—opens the circuit and halts current completely."
      },
      {
        "question": "27. In a series circuit containing three bulbs, what happens if one bulb is unscrewed from its socket?",
        "options": [
          "The other two bulbs become twice as bright",
          "The other two bulbs go out immediately because the single continuous loop is broken",
          "Only the first bulb stays lit",
          "The battery instantly catches fire"
        ],
        "correct": 1,
        "solution": "In a series circuit, there is only one path for current. Removing any bulb breaks the loop (open circuit), causing all current to stop and turning off every bulb in the series."
      },
      {
        "question": "28. Why are electrical lights and appliances in our homes connected in parallel circuits rather than series circuits?",
        "options": [
          "Parallel circuits use less copper wire",
          "Each appliance can be operated independently without affecting the others, and each receives full mains voltage",
          "Parallel circuits do not require switches",
          "Series circuits cannot carry electric current"
        ],
        "correct": 1,
        "solution": "Parallel wiring gives each device its own independent circuit branch. Switching off a bedroom light does not turn off the refrigerator, and each device receives the full 230 V supply."
      },
      {
        "question": "29. What is the standard schematic symbol for a battery consisting of two cells in series?",
        "options": [
          "A single circle with two plus signs",
          "Two pairs of alternating long thin and short thick parallel lines connected in series",
          "A single long line without any short line",
          "A triangle pointing at a resistor"
        ],
        "correct": 1,
        "solution": "A battery symbol consists of multiple cell symbols arranged in series: long thin line (+), short thick line (-), connected to the next long thin line (+), and short thick line (-)."
      },
      {
        "question": "30. Why must corners in circuit schematic diagrams be drawn as clean 90° right angles?",
        "options": [
          "Because electricity only flows around 90-degree corners",
          "To maintain standardized engineering clarity, neatness, and prevent visual confusion",
          "Because curved wires slow down the speed of light",
          "Because circular diagrams drain batteries faster"
        ],
        "correct": 1,
        "solution": "Standard drafting conventions mandate straight lines and 90° corners to make complex electrical schematics orderly, readable, and unambiguously traceable for engineers and technicians."
      }
    ]
  },
  {
    "id": 20,
    "type": "quiz_slide",
    "title": "Mastery Assessment: Conductors, Insulators & Indian Heritage",
    "subtitle": "Challenge Inquiries 31 to 40 — Conduction Testing, Human Safety, PPE & J.C. Bose",
    "questions": [
      {
        "question": "31. When using a conduction tester, which of the following materials will cause the bulb to illuminate?",
        "options": [
          "A plastic button",
          "A wooden matchstick",
          "A brass key",
          "A glass bead"
        ],
        "correct": 2,
        "solution": "Brass is a metallic alloy of copper and zinc. Like all metals, it contains free delocalized electrons that conduct electricity easily, completing the conduction tester's circuit."
      },
      {
        "question": "32. Why is pure distilled water an electrical insulator, whereas common tap water conducts electricity?",
        "options": [
          "Distilled water is colder than tap water",
          "Tap water contains dissolved mineral salts that dissociate into mobile charge-carrying ions",
          "Distilled water is made of plastic molecules",
          "Tap water contains dissolved copper wire fragments"
        ],
        "correct": 1,
        "solution": "Pure water (H₂O) contains virtually no free ions. Tap water contains dissolved mineral salts (calcium, magnesium, chloride, sodium) that dissociate into mobile ions, allowing electrical conduction."
      },
      {
        "question": "33. Which non-metallic substance is a remarkable electrical conductor commonly found in school classrooms?",
        "options": [
          "Chalk",
          "Graphite (pencil lead)",
          "Rubber eraser",
          "Cotton string"
        ],
        "correct": 1,
        "solution": "Graphite is a crystalline allotrope of carbon arranged in hexagonal planar sheets with free delocalized pi-electrons, making it a good conductor despite being a non-metal."
      },
      {
        "question": "34. Why do professional electricians wear thick rubber-soled boots and rubber gloves when working on live electrical lines?",
        "options": [
          "Rubber keeps their feet warm during winter",
          "Rubber is an electrical insulator that prevents current from passing through their body to the ground",
          "Rubber generates static electricity that powers their tools",
          "Rubber repels magnetic fields"
        ],
        "correct": 1,
        "solution": "Rubber has extremely high electrical resistance (insulator). It creates an impenetrable barrier between the technician and the ground, preventing electric current from finding a path through their body."
      },
      {
        "question": "35. Why does touching an electrical appliance with wet hands dramatically increase the risk of severe electric shock?",
        "options": [
          "Water makes the copper wires inside the appliance heavier",
          "Moisture and dissolved skin salts reduce human skin resistance from 100,000 Ω down to less than 1,000 Ω",
          "Water turns direct current into static sparks",
          "Water changes the color of the plastic casing"
        ],
        "correct": 1,
        "solution": "Dry skin has high resistance (around 100,000 Ω). Water containing dissolved salts lowers skin resistance to under 1,000 Ω. By Ohm's law (I = V / R), lower resistance causes a hundred-fold surge in current through the body."
      },
      {
        "question": "36. What is the primary purpose of the colorful plastic (PVC) coating surrounding household electrical wires?",
        "options": [
          "To prevent electric shock to humans and prevent bare copper cores from touching and causing short circuits",
          "To make the cables smell pleasant",
          "To speed up the flow of electrons inside the copper",
          "To make the wire magnetic"
        ],
        "correct": 0,
        "solution": "PVC plastic is a durable, flexible electrical insulator. It protects users from fatal shocks and prevents adjacent conductors from coming into direct contact (which would cause massive short circuits and fires)."
      },
      {
        "question": "37. What revolutionary solid-state semiconductor device did Acharya Jagadish Chandra Bose invent in Kolkata in the late 1890s?",
        "options": [
          "The modern lithium-ion polymer battery",
          "The galena (lead sulfide) crystal detector, the world's first semiconductor diode",
          "The fluorescent neon tube",
          "The solar-powered calculator"
        ],
        "correct": 1,
        "solution": "Acharya J.C. Bose used a galena (PbS) crystal point-contact to detect microwave electromagnetic signals, creating the first semiconductor diode in history (patented in 1904)."
      },
      {
        "question": "38. What pioneering achievement did Acharya J.C. Bose demonstrate at Kolkata Town Hall in 1895?",
        "options": [
          "He generated 5 mm electromagnetic waves and transmitted them wirelessly through solid walls to ring a bell",
          "He discovered the element uranium in mineral ore",
          "He built India's first hydroelectric power dam",
          "He invented plastic insulation for copper cables"
        ],
        "correct": 0,
        "solution": "In 1895, Bose demonstrated wireless transmission of 5 mm millimetre microwaves through walls and the body of the Lieutenant Governor, successfully triggering a relay that rang a bell and detonated gunpowder."
      },
      {
        "question": "39. Why must a student scrape away the plastic insulation from the ends of a connecting wire before securing it under a terminal screw?",
        "options": [
          "Because plastic is an electrical insulator that would block electrical contact between the metal screw and the copper core",
          "To make the wire lighter",
          "Because bare copper wires absorb oxygen from the air to make electricity",
          "To change the color of the circuit"
        ],
        "correct": 0,
        "solution": "Plastic is an insulator. If it is not removed from the tips, it prevents physical metallic contact between the copper wire and the terminal, leaving the circuit open."
      },
      {
        "question": "40. Which of the following material pairs correctly identifies a good electrical conductor and a good electrical insulator?",
        "options": [
          "Conductor: Copper; Insulator: Rubber",
          "Conductor: Glass; Insulator: Aluminum",
          "Conductor: Plastic; Insulator: Iron",
          "Conductor: Wood; Insulator: Gold"
        ],
        "correct": 0,
        "solution": "Copper is a metal with free mobile electrons (conductor), while rubber is an elastic polymer with tightly bound electrons (insulator). The other options pair them incorrectly."
      }
    ]
  }
]

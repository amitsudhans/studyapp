# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 6: Pressure, Atmospheric Pressure, Winds, Storms & Cyclones
Complete curriculum dataset with compact headings, vocabulary, 16 content slides + 4 mastery challenge slides,
32 in-slide checkpoints, and 40 mastery quiz questions with comprehensive step-by-step solutions.
"""

SLIDES = [
    # SLIDE 1
    {
        "id": 1,
        "title": "Defining Pressure & Area",
        "tag": "Fundamental Law • SI Unit Pascal",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Welcome, weather explorers! Why can you easily push a sharp thumbtack into a wooden board with your thumb, but pressing with the flat head of a blunt rod does nothing? It all comes down to pressure! Let's explore how force and area interact.",
        "theory": r"""
<h3>The Concept of Pressure</h3>
<p>In physics, force alone does not tell the whole story. The effectiveness of a force depends entirely on the <strong>surface area</strong> over which that force is distributed.</p>
<p><strong>Pressure is defined as the force acting perpendicular to a surface per unit area:</strong></p>

<p style="text-align: center; font-size: 1.25rem; font-weight: bold; color: #38bdf8;">
  $$\text{Pressure} = \frac{\text{Force}}{\text{Area}} \quad \left(P = \frac{F}{A}\right)$$
</p>

<h4>SI Unit of Pressure</h4>
<ul>
  <li>The SI unit of force is the <strong>newton ($\text{N}$)</strong> and the SI unit of area is the <strong>square metre ($\text{m}^2$)</strong>.</li>
  <li>Therefore, the standard SI unit of pressure is <strong>newton per square metre ($\text{N/m}^2$)</strong>, which is named the <strong>pascal ($\text{Pa}$)</strong> in honor of French polymath Blaise Pascal.</li>
  <li>$$1\text{ Pascal} = 1\text{ N/m}^2$$</li>
</ul>

<h4>The Inverse Area Relationship</h4>
<p>From the formula $P = F/A$, pressure is <em>inversely proportional</em> to the contact area for a constant applied force:</p>
<ul>
  <li><strong>Smaller Area $\rightarrow$ Enormous Pressure:</strong> The pointed tip of an iron nail or syringe needle has an ultra-tiny area ($A \approx 0.1\text{ mm}^2$). Even a moderate pushing force of $10\text{ N}$ produces immense pressure exceeding $100,000,000\text{ Pa}$, piercing solid wood or skin effortlessly!</li>
  <li><strong>Larger Area $\rightarrow$ Reduced Pressure:</strong> Distributing the same force over a larger area drastically lowers the pressure exerted on surfaces.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Pressure", "definition": "The physical magnitude of perpendicular force applied per unit surface area ($P = F/A$)."},
            {"word": "Pascal (Pa)", "definition": "The SI unit of pressure, equal to one newton of force acting perpendicularly over one square metre ($1\\text{ N/m}^2$)."},
            {"word": "Perpendicular Force (Thrust)", "definition": "A mechanical force acting at a right angle ($90^\\circ$) to the contact surface plane."},
            {"word": "Inverse Proportionality", "definition": "A mathematical relationship where increasing surface area causes pressure to decrease proportionally for a constant force."}
        ],
        "sim_id": "pressure_area_sim",
        "checkpoints": [
            {
                "question": "What is the standard SI unit of pressure, and what is its equivalent formulation in fundamental units?",
                "options": [
                    "Joule per second (J/s)",
                    "Pascal (Pa), equivalent to Newton per square metre (N/m²)",
                    "Watt per square metre (W/m²)",
                    "Kilogram per metre (kg/m)"
                ],
                "correct": 1,
                "explanation": "Pressure is defined as Force divided by Area. The SI unit is Pascal (Pa), which is identically equal to 1 N/m².",
                "solution": "Formula: $P = F/A \\rightarrow [P] = \\text{N/m}^2 = \\text{Pascal (Pa)}$."
            },
            {
                "question": "If a constant pushing force of 50 N is applied first with a broad flat plate (Area = 0.5 m²) and then with a sharp pin (Area = 0.0001 m²), how will the pressure compare?",
                "options": [
                    "The pressure is identical in both cases because the force is 50 N",
                    "The pressure under the pin is dramatically higher because of its tiny contact area",
                    "The flat plate produces higher pressure",
                    "The pin produces zero pressure"
                ],
                "correct": 1,
                "explanation": "Since $P = F/A$, reducing contact area increases pressure inversely. The tiny area of the pin generates thousands of times greater pressure.",
                "solution": "Flat plate: $P = 50 / 0.5 = 100\\text{ Pa}$. Pin: $P = 50 / 0.0001 = 500,000\\text{ Pa}$. Pin pressure is $5,000\\times$ greater."
            }
        ]
    },

    # SLIDE 2
    {
        "id": 2,
        "title": "Pressure in Solids",
        "tag": "Engineering Applications • Sharp vs. Broad",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Have you ever carried a heavy school bag with thin string straps? Ouch! The strings dig painfully into your shoulders. But wide, padded straps feel completely comfortable. Let's see how spreading force over area protects our bodies and powers tools.",
        "theory": r"""
<h3>Harnessing Area in Daily Life</h3>
<p>Understanding the inverse relationship between area and pressure ($P = F/A$) allows engineers, carpenters, and designers to optimize tools and everyday objects for specific purposes:</p>

<h4>1. Minimizing Area to Maximize Pressure (Cutting & Piercing)</h4>
<ul>
  <li><strong>Sharp Knives & Axes:</strong> A sharp kitchen knife has an ultra-thin cutting edge with microscopic area. Gentle downward muscular force generates enough pressure to slice cleanly through tough vegetables and meats. A blunt knife has a rounded, wider edge, spreading the force and failing to cut.</li>
  <li><strong>Pointed Nails, Pins & Screws:</strong> The pointed tip concentrates hammer blows into massive pressure, penetrating brick walls and timber without bending.</li>
  <li><strong>Sewing Needles & Thumbtacks:</strong> Fine tips pierce thick fabrics effortlessly.</li>
</ul>

<h4>2. Maximizing Area to Minimize Pressure (Spreading Weight)</h4>
<ul>
  <li><strong>Broad School Bag Straps:</strong> School textbooks exert downward gravitational force (weight). Wide, padded shoulder straps distribute this weight over a large shoulder surface area, lowering pressure ($P = F/A$) and preventing painful shoulder bruising!</li>
  <li><strong>Broad Bucket Handles:</strong> Plastic buckets have thick, contoured handles or rotating grips to distribute the weight of 15 liters of water ($150\text{ N}$) across the entire palm.</li>
  <li><strong>Caterpillar Tracks on Heavy Tanks:</strong> Giant 60-ton military tanks and construction excavators ride on wide continuous tracks rather than narrow wheels, preventing them from sinking into soft mud or desert sand.</li>
  <li><strong>Wide Camel Hooves:</strong> Camels have large, flat, padded hooves that distribute body weight across desert sand, allowing them to walk without sinking.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Contact Area", "definition": "The exact geometric surface interface through which an applied force is transferred onto another body."},
            {"word": "Caterpillar Tracks", "definition": "Wide continuous metal treads fitted to heavy vehicles to spread weight over large ground area, preventing sinking."},
            {"word": "Weight Distribution", "definition": "Spreading gravitational load across broader surface dimensions to reduce localized contact pressure."},
            {"word": "Sharpness", "definition": "The degree to which a tool edge or tip is honed down to a microscopic contact surface area."}
        ],
        "sim_id": "bag_strap_pressure_sim",
        "checkpoints": [
            {
                "question": "Why are the shoulder straps of heavy school backpacks made broad and padded rather than made of thin string?",
                "options": [
                    "To make the backpack heavier",
                    "To distribute the bag's weight over a larger shoulder area, drastically reducing pressure on the body",
                    "To attract magnetic fields from books",
                    "To make the bag waterproof"
                ],
                "correct": 1,
                "explanation": "Broad straps increase contact area ($A$), which reduces pressure ($P = F/A$) exerted on the student's shoulders.",
                "solution": "$P = F/A$. Increasing $A$ reduces $P$, preventing pain and shoulder strain."
            },
            {
                "question": "Why does a sharp knife cut vegetables much more easily than a blunt knife when the same hand force is applied?",
                "options": [
                    "A sharp knife is much heavier than a blunt knife",
                    "The sharp knife has an extremely thin edge with tiny contact area, generating far higher pressure to pierce fibers",
                    "A blunt knife produces negative pressure",
                    "A sharp knife heats vegetables up"
                ],
                "correct": 1,
                "explanation": "A sharp edge has a microscopic contact area. For the same force, smaller area produces vastly higher localized pressure.",
                "solution": "Sharp edge = smaller $A \\rightarrow$ higher pressure $P = F/A$, cleanly cutting plant cells."
            }
        ]
    },

    # SLIDE 3
    {
        "id": 3,
        "title": "Liquid Pressure Directions",
        "tag": "Hydrostatics • Omnidirectional Thrust",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "A solid brick only presses downward onto the table beneath it. But what about water inside a bottle? If you poke holes in the side of a water-filled plastic container, water jets shoot out horizontally! Liquids exert pressure in every direction.",
        "theory": r"""
<h3>How Fluids Exert Pressure</h3>
<p>Unlike rigid solids (which exert pressure exclusively downward on the surface supporting their weight), liquids are fluids consisting of mobile molecules that collide continuously with every surface they touch.</p>

<h4>Cardinal Rules of Liquid Pressure</h4>
<ol>
  <li><strong>Downwards Pressure:</strong> Liquid column weight exerts downward vertical pressure on the container bottom:
    $$P_{\text{bottom}} = \frac{\text{Weight of Liquid Column}}{\text{Bottom Base Area}}$$
  </li>
  <li><strong>Sideways (Lateral) Pressure:</strong> Liquids push against the vertical walls of their container. If a flexible rubber membrane is tied over a side opening in a glass tube, filling the tube with water causes the side membrane to bulge outward prominently!</li>
  <li><strong>Omnidirectional Equality at a Given Depth:</strong> At any specific horizontal depth, <strong>a liquid exerts equal pressure in all directions</strong> (downward, upward, and sideways).</li>
</ol>

<h4>The Perforated Can Experiment</h4>
<p>Take a tall plastic bottle and puncture four holes around its circumference at the <em>exact same height</em> from the base. Fill the bottle with water. Water streams spurt out from all four holes with identical velocity and strike the table at the exact same horizontal distance! This proves that <strong>liquid pressure is identical in all lateral directions at a given depth</strong>.</p>
""",
        "vocabulary": [
            {"word": "Liquid Pressure", "definition": "The hydrostatic pressure exerted by a fluid at rest on the bottom and sidewalls of its container."},
            {"word": "Lateral Pressure", "definition": "The horizontal outward pressure exerted by liquids against the vertical boundary walls of a container."},
            {"word": "Omnidirectional Pressure", "definition": "The property of fluids whereby pressure at a given depth acts equally in all directions (Pascal's Principle)."},
            {"word": "Hydrostatic Equilibrium", "definition": "A state where fluid is motionless because pressure gradients balance out internal and gravitational forces."}
        ],
        "sim_id": "liquid_pressure_directions_sim",
        "checkpoints": [
            {
                "question": "If you puncture three holes around a plastic bottle at the EXACT SAME height from the base, what will you observe when the bottle is filled with water?",
                "options": [
                    "Water will squirt out only from the hole facing North",
                    "Water will squirt out from all three holes with identical speed and reach the same distance",
                    "No water will exit because pressure cancels out",
                    "The water will freeze instantly"
                ],
                "correct": 1,
                "explanation": "At a given depth, liquids exert equal pressure in all lateral directions, producing identical spurting streams.",
                "solution": "Principle: At any fixed depth $h$, liquid pressure is isotropic (equal in all lateral directions)."
            },
            {
                "question": "Unlike a solid block which only presses downward, on which surfaces of a container does a liquid exert pressure?",
                "options": [
                    "Only on the open top surface",
                    "Both on the bottom and on all surrounding sidewalls",
                    "Only on the corners of the container",
                    "Only on wooden surfaces"
                ],
                "correct": 1,
                "explanation": "Mobile liquid molecules collide with both the bottom base and all vertical sidewalls, exerting pressure everywhere.",
                "solution": "Liquids exert pressure downwards, sideways, and in all directions against container boundaries."
            }
        ]
    },

    # SLIDE 4
    {
        "id": 4,
        "title": "Depth & Dam Architecture",
        "tag": "Hydrostatic Head • Engineering Dams",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Why are hydroelectric dams built with narrow tops but massive, ultra-thick concrete bases at the bottom? Because liquid pressure grows directly with water height! Let's examine how depth governs liquid pressure.",
        "theory": r"""
<h3>Pressure Grows with Column Height</h3>
<p>The pressure exerted by a liquid at rest depends directly on the <strong>height (depth, $h$) of the liquid column</strong> standing above that point.</p>

<p style="text-align: center; font-size: 1.25rem; font-weight: bold; color: #38bdf8;">
  $$P = \rho \cdot g \cdot h$$
</p>
<ul>
  <li>$\rho$ is the liquid density (for water, $\rho \approx 1,000\text{ kg/m}^3$).</li>
  <li>$g$ is gravitational acceleration ($9.8\text{ m/s}^2$).</li>
  <li>$h$ is the vertical height of the liquid column above the point.</li>
</ul>

<h4>The Three-Spout Bottle Demonstration</h4>
<p>Puncture three vertical holes along the side of a tall bottle: Hole A (near top), Hole B (in middle), and Hole C (near bottom):</p>
<ol>
  <li><strong>Top Hole A:</strong> Low water column height $\rightarrow$ low pressure $\rightarrow$ weak, trickling stream landing close to the bottle.</li>
  <li><strong>Middle Hole B:</strong> Moderate water column height $\rightarrow$ medium pressure $\rightarrow$ stream lands farther away.</li>
  <li><strong>Bottom Hole C:</strong> Maximum water column height above $\rightarrow$ maximum pressure $\rightarrow$ powerful high-speed jet shooting out the farthest distance!</li>
</ol>

<h4>Real-World Engineering Marvels</h4>
<ul>
  <li><strong>Overhead Rooftop Water Tanks:</strong> Municipal and domestic water storage tanks are deliberately installed on the highest rooftops. The tall vertical elevation creates high gravitational head ($P = \rho g h$), ensuring high water pressure and robust flow from taps and showers downstairs!</li>
  <li><strong>Dam Architecture:</strong> Massive concrete dams (like the Bhakra Nangal or Hoover Dam) are engineered with <strong>thick, sloping, broad bases</strong> because water pressure near the bottom of the reservoir is tens of times greater than at the surface. A thin base would rupture under the colossal hydrostatic thrust!</li>
</ul>
""",
        "vocabulary": [
            {"word": "Hydrostatic Head", "definition": "The vertical height of a liquid column above a reference point that determines hydrostatic pressure ($P = \\rho g h$)."},
            {"word": "Pressure Gradient with Depth", "definition": "The continuous linear increase in liquid pressure as one descends deeper into a fluid."},
            {"word": "Dam Abutment", "definition": "The heavy, reinforced concrete base structure of a dam designed to resist massive bottom water pressure."},
            {"word": "Elevation Head", "definition": "The gravitational potential energy of water stored at high rooftop elevation to supply household tap pressure."}
        ],
        "sim_id": "depth_dam_architecture_sim",
        "checkpoints": [
            {
                "question": "Why are massive river dams constructed with much broader, thicker concrete bases at the bottom than at the top?",
                "options": [
                    "To save concrete material during construction",
                    "Because horizontal water pressure increases massively with depth, requiring a thick base to withstand the immense force",
                    "To allow fish to swim underneath the dam",
                    "To keep the water warm in winter"
                ],
                "correct": 1,
                "explanation": "Since $P = \\rho g h$, water pressure reaches its maximum near the reservoir bed. The base must be thick to prevent structural collapse.",
                "solution": "Hydrostatic law: $P \\propto h$. Maximum depth = maximum pressure $\\rightarrow$ thick broad dam base required."
            },
            {
                "question": "In a tall water container with three vertical spouts (top, middle, bottom), which spout will eject water with the highest speed and farthest range?",
                "options": [
                    "The top spout because it is closest to the open air",
                    "The middle spout because it is balanced",
                    "The bottom spout because it has the tallest column of water above it generating maximum pressure",
                    "All spouts eject water to the exact same distance"
                ],
                "correct": 2,
                "explanation": "The bottom spout has the greatest height of water above it ($h_{\\text{max}}$), producing the highest pressure and highest discharge velocity.",
                "solution": "Torricelli's theorem: $v = \\sqrt{2gh}$. Deepest hole has largest $h \\rightarrow$ fastest and farthest stream."
            }
        ]
    },

    # SLIDE 5
    {
        "id": 5,
        "title": "Atmospheric Pressure Envelope",
        "tag": "Atmospheric Physics • Torricelli's Column",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "You are currently living at the bottom of an ocean of air! Planet Earth is wrapped in a thick blanket of gas hundreds of kilometers high. The weight of this entire air column presses down on us with staggering force. Let's explore atmospheric pressure.",
        "theory": r"""
<h3>The Atmosphere of Earth</h3>
<p>The gaseous envelope of air surrounding planet Earth is called the <strong>Atmosphere</strong>. Earth's gravitational pull holds air molecules tightly to the globe, extending hundreds of kilometers into space.</p>

<h4>What is Atmospheric Pressure?</h4>
<p>Air has mass. Although a single cubic meter of air seems weightless, the colossal column of air extending from sea level all the way to the top of the atmosphere weighs approximately <strong>$10,000\text{ kilograms}$ over every single square metre</strong> of ground!</p>
<p><strong>Atmospheric Pressure is the downward force exerted by the weight of the air column on a unit surface area of Earth.</strong></p>

<h4>Standard Values and Meteorological Units</h4>
<ul>
  <li><strong>Standard Sea Level Pressure:</strong>
    $$P_0 \approx 101,325\text{ Pa} \approx 101.3\text{ kPa}$$
  </li>
  <li><strong>Meteorological Units:</strong> Weather scientists use the <strong>millibar ($\text{mb}$)</strong> and the <strong>hectopascal ($\text{hPa}$)</strong>:
    $$1\text{ hPa} = 100\text{ Pa}$$
    $$1\text{ bar} = 100,000\text{ Pa} = 1,000\text{ mb} \implies 1\text{ mb} = 1\text{ hPa}$$
  </li>
  <li>Standard sea level atmospheric pressure is approximately <strong>$1013\text{ hPa}$ (or $1013\text{ mb}$)</strong>, equivalent to supporting a column of liquid mercury $760\text{ mm}$ high ($76\text{ cm Hg}$).</li>
</ul>
""",
        "vocabulary": [
            {"word": "Atmosphere", "definition": "The thick envelope of air and gases surrounding planet Earth held by gravitational attraction."},
            {"word": "Atmospheric Pressure", "definition": "The gravitational force per unit area exerted by the weight of atmospheric air columns on Earth's surface."},
            {"word": "Hectopascal (hPa)", "definition": "A standard meteorological pressure unit equal to 100 Pascals ($1\\text{ hPa} = 100\\text{ Pa} = 1\\text{ mb}$)."},
            {"word": "Barometer", "definition": "A scientific instrument invented by Evangelista Torricelli used to measure atmospheric air pressure."}
        ],
        "sim_id": "atmospheric_pressure_mercury_sim",
        "checkpoints": [
            {
                "question": "What is the numerical relationship between the meteorological pressure units 'hectopascal' (hPa) and 'pascal' (Pa)?",
                "options": [
                    "1 hPa = 1 Pa",
                    "1 hPa = 10 Pa",
                    "1 hPa = 100 Pa",
                    "1 hPa = 1,000 Pa"
                ],
                "correct": 2,
                "explanation": "The prefix 'hecto' denotes a factor of 100. Therefore, 1 hectopascal (hPa) = 100 pascals (Pa) = 1 millibar (mb).",
                "solution": "Unit identity: $1\\text{ hPa} = 100\\text{ Pa} = 1\\text{ mb}$."
            },
            {
                "question": "Approximately what is the standard atmospheric pressure at sea level on Earth in hectopascals (hPa)?",
                "options": [
                    "10 hPa",
                    "100 hPa",
                    "1013 hPa",
                    "10,000 hPa"
                ],
                "correct": 2,
                "explanation": "Standard atmospheric pressure at sea level is approximately 101,325 Pa, which equals roughly 1013 hPa (or 1013 mb).",
                "solution": "Standard atmospheric pressure = $101.325\\text{ kPa} = 1013.25\\text{ hPa}$."
            }
        ]
    },

    # SLIDE 6
    {
        "id": 6,
        "title": "Body Pressure Equilibrium",
        "tag": "Physiological Balance • Internal Counter-Pressure",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "If the atmosphere exerts an incredible 100,000 Newtons of force on every square metre of our bodies—equivalent to the weight of an elephant standing on us—why don't we get crushed flat? Let's uncover the secret of internal body pressure.",
        "theory": r"""
<h3>The Great Balance: Inside vs. Outside</h3>
<p>The total surface area of an adult human body is roughly $1.5$ to $2.0\text{ m}^2$. That means the atmosphere presses against our skin with a colossal total force exceeding <strong>$150,000\text{ to }200,000\text{ Newtons}$ (equivalent to 15 to 20 metric tons)</strong>!</p>
<p>Why do we walk around without feeling crushed?</p>

<h4>Internal Counter-Pressure</h4>
<ol>
  <li><strong>Fluids & Gases Within:</strong> Our bodies are not empty shells; our tissues, bloodstream, and organs are filled with liquids (blood, interstitial fluids, water) and dissolved gases.</li>
  <li><strong>Exact Equality:</strong> The internal circulatory pressure exerted by blood and body fluids pushes outward against skin and vessel walls with a pressure that <strong>almost perfectly matches external atmospheric pressure</strong>:
    $$P_{\text{internal body}} \approx P_{\text{atmospheric}}$$
  </li>
  <li><strong>Zero Net Crushing Force:</strong> The inward atmospheric push is neutralized by the outward biological push. Net force across our skin is essentially zero!</li>
</ol>

<h4>High-Altitude Nosebleeds</h4>
<p>When mountaineers climb towering peaks (like Mt. Everest, altitude $8,848\text{ m}$), atmospheric pressure drops significantly because the air column above is much shorter and thinner ($P_{\text{atm}} \approx 330\text{ hPa}$).</p>
<p>Because internal blood pressure remains around $1013\text{ hPa}$, the outward push exceeds the external air pressure. Delicate capillaries inside nasal membranes rupture under this imbalance, causing <strong>altitude nosebleeds</strong>! Astronauts must wear pressurized spacesuits in the vacuum of space for this exact reason.</p>
""",
        "vocabulary": [
            {"word": "Internal Fluid Pressure", "definition": "The outward hydraulic pressure maintained by blood, body fluids, and cells balancing external air pressure."},
            {"word": "Atmospheric Crushing Force", "definition": "The immense inward force exerted by air columns that would crush an unpressurized container."},
            {"word": "Pressure Imbalance", "definition": "A condition where internal and external pressures differ, causing membranes or containers to rupture or collapse."},
            {"word": "Spacesuit Pressurization", "definition": "Artificial gas pressure maintained inside astronaut suits to prevent body fluids from boiling in space vacuum."}
        ],
        "sim_id": "body_fluid_balance_sim",
        "checkpoints": [
            {
                "question": "Why are humans and animals on Earth's surface NOT crushed flat by the immense weight of the atmosphere?",
                "options": [
                    "Because human bones are made of indestructible diamond",
                    "Because internal pressure exerted by blood and body fluids pushes outward to balance external atmospheric pressure",
                    "Because atmospheric pressure only acts on inanimate rocks",
                    "Because Earth's gravity stops working on living creatures"
                ],
                "correct": 1,
                "explanation": "Internal fluids and bloodstream exert an outward pressure that equals and balances external air pressure.",
                "solution": "Equilibrium: $P_{\\text{internal}} = P_{\\text{atmospheric}} \\rightarrow$ Net crushing force across skin = 0."
            },
            {
                "question": "Why do mountaineers frequently experience nosebleeds when climbing to extreme high altitudes on tall mountains?",
                "options": [
                    "Because high-altitude mountain snow turns blood into ice",
                    "Because external atmospheric pressure drops drastically, causing higher internal blood pressure to rupture delicate nasal capillaries",
                    "Because mountain air contains 100% pure oxygen",
                    "Because gravity is 10 times stronger on mountain peaks"
                ],
                "correct": 1,
                "explanation": "At high altitudes, air is thin and external pressure drops. Internal blood pressure is now greater, bursting tiny nasal blood vessels.",
                "solution": "Altitude effect: $P_{\\text{atm}}$ drops $\\rightarrow P_{\\text{blood}} > P_{\\text{atm}} \\rightarrow$ Capillary rupture."
            }
        ]
    },

    # SLIDE 7
    {
        "id": 7,
        "title": "Wind Speed & Pressure Drop",
        "tag": "Bernoulli's Principle • Roof Lift-off",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Here is an amazing counter-intuitive mystery of physics: when air rushes at high speed, does its pressure go UP or DOWN? It drops! Blowing between two balloons pulls them together. Let's see how high-speed winds create low pressure.",
        "theory": r"""
<h3>The Discovery: High Speed = Low Pressure</h3>
<p>In the 1730s, Swiss physicist Daniel Bernoulli established a foundational principle of fluid mechanics: <strong>High-speed winds are always accompanied by a significant drop in air pressure.</strong> Fast-moving air molecules exert less lateral pressure on adjacent surfaces than still, stagnant air.</p>

<h4>Classic Demonstration: Two Suspended Balloons</h4>
<p>Hang two inflated rubber balloons side-by-side with a gap of 5 to 10 cm between them. What happens if you blow air vigorously into the gap between them?</p>
<ul>
  <li>Common sense might suggest the air stream would blow the balloons apart.</li>
  <li>Instead, <strong>the two balloons instantly move toward each other and snap together!</strong></li>
  <li><strong>The Explanation:</strong> Blowing creates a high-speed air stream between the balloons, causing air pressure between them to drop sharply. The higher, still atmospheric pressure on their outer sides pushes the balloons inward toward the low-pressure zone!</li>
</ul>

<h4>Why Do Storm Winds Blow Roofs Off?</h4>
<p>During severe gales and hurricanes, tin or thatched roofs of houses are often ripped off and blown high into the air. Why?</p>
<ol>
  <li>Violent storm winds blow across the top of the roof at extreme speeds ($>100\text{ km/h}$), creating a powerful <strong>low-pressure zone above the roof</strong>.</li>
  <li>Inside the house, the air remains trapped and stagnant at normal, high atmospheric pressure.</li>
  <li>This massive upward pressure difference creates an immense aerodynamic lifting force, blowing the roof completely off the walls!</li>
</ol>
""",
        "vocabulary": [
            {"word": "Bernoulli's Principle", "definition": "A fluid dynamics law stating that an increase in the speed of a fluid occurs simultaneously with a decrease in pressure."},
            {"word": "Aerodynamic Lift", "definition": "The net upward force generated on a surface when air pressure above is lower than air pressure below."},
            {"word": "Roof Blow-Off", "definition": "The catastrophic lifting of roofs during gales caused by high-speed low pressure above and trapped high pressure beneath."},
            {"word": "Lateral Fluid Pressure", "definition": "The static pressure exerted sideways by a moving fluid perpendicular to its streamline flow."}
        ],
        "sim_id": "bernoulli_balloons_roof_sim",
        "checkpoints": [
            {
                "question": "What happens when you blow a fast stream of air into the narrow gap between two suspended rubber balloons?",
                "options": [
                    "The balloons are pushed far apart by the wind",
                    "The balloons move inward and snap toward each other due to the low-pressure zone created between them",
                    "Both balloons pop immediately",
                    "The balloons turn into helium"
                ],
                "correct": 1,
                "explanation": "High-speed air reduces pressure in the gap. Higher static atmospheric pressure on the outer sides pushes the balloons together.",
                "solution": "Fast air $\\rightarrow$ low pressure in gap $\\rightarrow$ external high pressure pushes balloons together."
            },
            {
                "question": "What is the primary physical reason why tin roofs of houses are lifted upward and blown away during violent storms?",
                "options": [
                    "Lightning melts the steel nails",
                    "Violent winds racing over the roof create severe low pressure above, while high pressure inside pushes the roof upward",
                    "Earthquakes shake the foundation",
                    "Cold air weighs more than warm air"
                ],
                "correct": 1,
                "explanation": "High wind velocity over the roof drops air pressure above. Stagnant high pressure inside exerts an upward lift force blowing the roof off.",
                "solution": "Bernoulli lift: $P_{\\text{inside}} \\gg P_{\\text{roof top}} \\rightarrow$ Net upward force blows roof off."
            }
        ]
    },

    # SLIDE 8
    {
        "id": 8,
        "title": "Pressure Gradients & Winds",
        "tag": "Atmospheric Dynamics • Wind Genesis",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "What is wind? Moving air! But what sets invisible air masses into motion across thousands of kilometers? A pressure difference! Air rushes from high pressure to low pressure, just like water rolling downhill.",
        "theory": r"""
<h3>The Origin of Atmospheric Motion</h3>
<p>Air in our atmosphere is never stationary. <strong>Wind is simply air in horizontal motion from one region to another.</strong></p>

<h4>The Pressure Gradient Force</h4>
<p>The primary driving engine of all winds on Earth is a difference in atmospheric air pressure:</p>
<ul>
  <li><strong>The Golden Rule:</strong> <strong>Air ALWAYS moves from a region of HIGH air pressure toward a region of LOW air pressure.</strong></li>
  <li><strong>Pressure Gradient:</strong> The rate of change of pressure with distance is called the <em>pressure gradient</em>.</li>
  <li><strong>Wind Velocity Rule:</strong> The greater the pressure difference between two regions, the steeper the pressure gradient, and the <strong>faster the wind blows</strong>! A gentle pressure difference produces a soft, cooling breeze; a steep pressure difference unleashes gale-force howling winds.</li>
</ul>

<h4>Isobars on Weather Maps</h4>
<p>Meteorologists plot lines of equal atmospheric pressure called <strong>isobars</strong> on daily weather maps:</p>
<ul>
  <li>When isobars are spaced far apart, the pressure gradient is gentle $\rightarrow$ light, calm winds.</li>
  <li>When isobars are packed tightly together, the pressure gradient is steep $\rightarrow$ fierce, roaring storms and squalls!</li>
</ul>
""",
        "vocabulary": [
            {"word": "Wind", "definition": "The horizontal movement of atmospheric air masses driven by regional differences in air pressure."},
            {"word": "Pressure Gradient", "definition": "The spatial rate of change of atmospheric pressure between two geographic points ($dP/dx$)."},
            {"word": "High-Pressure System (Anticyclone)", "definition": "A weather region with descending, dense air and higher pressure than surrounding areas, usually bringing clear skies."},
            {"word": "Low-Pressure System (Depression)", "definition": "A weather region where warm air rises, creating lower pressure that sucks in surrounding winds, often bringing rain and storms."}
        ],
        "sim_id": "pressure_gradient_wind_sim",
        "checkpoints": [
            {
                "question": "What is the fundamental rule governing the direction of atmospheric wind flow across Earth?",
                "options": [
                    "Air always moves from low-pressure regions to high-pressure regions",
                    "Air always moves from high-pressure regions to low-pressure regions",
                    "Air only moves vertically in circles without traveling horizontally",
                    "Air only moves toward magnetic North"
                ],
                "correct": 1,
                "explanation": "Air naturally flows down the pressure gradient from regions of higher atmospheric pressure to regions of lower atmospheric pressure.",
                "solution": "Fundamental atmospheric law: Wind flows High Pressure $\\rightarrow$ Low Pressure."
            },
            {
                "question": "What happens to the speed of wind when the atmospheric pressure difference between two neighboring cities increases dramatically?",
                "options": [
                    "The wind speed drops to zero and air freezes",
                    "The wind speed increases significantly, producing strong gales",
                    "The wind reverses direction into outer space",
                    "The wind turns into pure nitrogen gas"
                ],
                "correct": 1,
                "explanation": "A larger pressure difference creates a steeper pressure gradient force, accelerating air masses into higher-speed winds.",
                "solution": "Wind speed is proportional to the pressure gradient: $\\text{Wind Speed} \\propto |\\Delta P / \\Delta x|$."
            }
        ]
    },

    # SLIDE 9
    {
        "id": 9,
        "title": "Land and Sea Breezes",
        "tag": "Coastal Convection • Diurnal Cycles",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "If you stand on a tropical beach at noon, a refreshing cool breeze blows from the ocean onto the shore. But at midnight, the breeze reverses, blowing out toward the sea! Why? It's the magic of unequal solar heating.",
        "theory": r"""
<h3>Differential Heating of Land and Water</h3>
<p>Water has a very high specific heat capacity, meaning it absorbs and releases thermal energy very slowly. Solid land (rock and sand) has a low heat capacity, heating up rapidly in sunlight and cooling down rapidly at night.</p>
<p>This differential heating creates continuous local pressure cycles along coastlines:</p>

<h4>1. The Sea Breeze (Daytime Phenomenon)</h4>
<ol>
  <li><strong>Intense Solar Heating:</strong> During the day, the land surface heats up much faster than the adjacent ocean water.</li>
  <li><strong>Rising Warm Air:</strong> The air over the land warms, becomes less dense, and expands upward, creating a <strong>localized LOW-pressure zone</strong> over the shore.</li>
  <li><strong>Cool Onshore Flow:</strong> The air over the sea remains cooler and denser, maintaining a <strong>HIGH-pressure zone</strong>.</li>
  <li><strong>Breeze Direction:</strong> Cool, refreshing air rushes from the sea toward the land. This daytime wind is called the <strong>Sea Breeze</strong>.</li>
</ol>

<h4>2. The Land Breeze (Night-time Phenomenon)</h4>
<ol>
  <li><strong>Rapid Radiational Cooling:</strong> After sunset, without solar rays, the land cools down much faster than the vast ocean.</li>
  <li><strong>Warm Sea Air Rises:</strong> Ocean water remains warm, so warm air rises over the sea, creating a <strong>LOW-pressure zone over the water</strong>.</li>
  <li><strong>Cool Offshore Flow:</strong> Dense, cool air over the land forms a <strong>HIGH-pressure zone</strong>.</li>
  <li><strong>Breeze Direction:</strong> Cool air flows from the land toward the sea. This night-time wind is called the <strong>Land Breeze</strong>.</li>
</ol>
""",
        "vocabulary": [
            {"word": "Sea Breeze", "definition": "A daytime local cooling wind that blows from the high-pressure sea toward the low-pressure heated land."},
            {"word": "Land Breeze", "definition": "A night-time local wind that blows from the cooled high-pressure land toward the warmer low-pressure sea."},
            {"word": "Differential Heating", "definition": "The unequal rate of temperature change between land and water due to differences in specific heat capacities."},
            {"word": "Convection Cell", "definition": "A circular atmospheric loop of rising warm air and sinking cool air driven by thermal temperature differences."}
        ],
        "sim_id": "land_sea_breeze_cycle_sim",
        "checkpoints": [
            {
                "question": "During a bright sunny DAY along the coastline, in which direction does the local breeze blow, and why?",
                "options": [
                    "From land to sea because land is colder",
                    "From sea to land (Sea Breeze) because land heats faster, creating low pressure that sucks in cool air from the sea",
                    "Vertically downward from clouds into the sand",
                    "There is never any breeze during daytime"
                ],
                "correct": 1,
                "explanation": "During the day, land heats faster than water. Warm air rises over land (low pressure), drawing in cool air from the sea (Sea Breeze).",
                "solution": "Daytime cycle: Warm land $\\rightarrow$ Low pressure $\\rightarrow$ Cool Sea Breeze blows onshore."
            },
            {
                "question": "At NIGHT along the coast, why does the wind reverse to blow from the land toward the sea (Land Breeze)?",
                "options": [
                    "Because the Moon pulls the air like ocean tides",
                    "Because land cools down faster than the ocean; the sea air remains warmer and rises, pulling cool air from the land",
                    "Because all ocean water evaporates at night",
                    "Because fish create wind currents with their fins"
                ],
                "correct": 1,
                "explanation": "At night, land cools rapidly while ocean water retains heat. Air over the warm sea rises, drawing cool air offshore from the land.",
                "solution": "Night cycle: Warm sea $\\rightarrow$ Low pressure over water $\\rightarrow$ Cool Land Breeze blows offshore."
            }
        ]
    },

    # SLIDE 10
    {
        "id": 10,
        "title": "Storm Genesis & Convection",
        "tag": "Atmospheric Thermodynamics • Cloud Formation",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "On a sweltering summer afternoon, the air suddenly turns dark, towering black clouds boil into the sky, and torrential rain bursts forth! How do ordinary hot afternoons transform into ferocious storms? Let's trace storm genesis.",
        "theory": r"""
<h3>The Recipe for a Storm</h3>
<p>A storm is a violent disturbance of the atmosphere accompanied by strong winds and usually by rain, hail, sleet, or snow. The atmospheric sequence that generates a storm proceeds through four stages:</p>

<h4>Stage 1: Ground Heating & Thermal Updrafts</h4>
<p>Intense solar radiation scorches the land surface. The air in contact with the hot ground absorbs heat, expands, becomes lightweight, and ascends rapidly as a powerful <strong>convective updraft</strong>. This rapid ascent creates a localized <strong>deep LOW-pressure area</strong> at the surface.</p>

<h4>Stage 2: Inflow of Surrounding Air</h4>
<p>Surrounding cooler, denser air rushes into the low-pressure vacuum at high velocity, generating gusty, howling surface winds.</p>

<h4>Stage 3: Adiabatic Cooling & Condensation</h4>
<p>As the warm, moisture-laden air column ascends into the colder upper troposphere, it expands and cools adiabatically. Gaseous water vapour condenses into billions of microscopic liquid water droplets, releasing immense amounts of <strong>latent heat</strong> that fuel further vertical cloud growth!</p>

<h4>Stage 4: Precipitation & Squalls</h4>
<p>The cloud expands into a towering, anvil-shaped <strong>cumulonimbus cloud</strong> (thunderhead) extending up to $15\text{ km}$ high. Droplets coalesce into heavy raindrops and ice pellets (hail), dragging cold downdrafts down to Earth to produce torrential rain and fierce storm squalls.</p>
""",
        "vocabulary": [
            {"word": "Storm", "definition": "A severe violent disturbance of atmospheric conditions featuring high-speed winds and intense precipitation."},
            {"word": "Thermal Updraft", "definition": "A column of rising warm, buoyant air caused by localized solar heating of the Earth's surface."},
            {"word": "Cumulonimbus Cloud", "definition": "A colossal, towering thunderstorm cloud with a dark base and anvil-shaped top that unleashes heavy rain, lightning, and hail."},
            {"word": "Latent Heat of Condensation", "definition": "Thermal energy released into the surrounding air when gaseous water vapour condenses into liquid water droplets."}
        ],
        "sim_id": "storm_convection_cloud_sim",
        "checkpoints": [
            {
                "question": "What initiates the formation of a summer storm over heated land?",
                "options": [
                    "Freezing temperatures at ground level",
                    "Intense ground heating causing warm, moist air to rise rapidly, creating a localized low-pressure area",
                    "Underground earthquakes shaking tree branches",
                    "Ocean tides washing onto beaches"
                ],
                "correct": 1,
                "explanation": "Intense solar heating causes air to expand and rise as thermal updrafts, creating surface low pressure that triggers storm inflow.",
                "solution": "Ground heat $\\rightarrow$ Rising warm air $\\rightarrow$ Low pressure vacuum $\\rightarrow$ Cold air rushes in."
            },
            {
                "question": "What type of towering cloud is scientifically associated with intense thunderstorms, heavy downpours, and hail?",
                "options": [
                    "Wispy cirrus clouds",
                    "Flat stratus clouds",
                    "Towering cumulonimbus clouds",
                    "White puffy fair-weather cumulus clouds"
                ],
                "correct": 2,
                "explanation": "Cumulonimbus clouds are dense, towering thunderstorm clouds that extend vertically up to 15 km, generating lightning and heavy rain.",
                "solution": "Thunderstorm cloud = Cumulonimbus (anvil-headed storm cloud)."
            }
        ]
    },

    # SLIDE 11
    {
        "id": 11,
        "title": "Cloud Charge & Lightning",
        "tag": "Atmospheric Electricity • Dielectric Breakdown",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Lightning is nature's most dazzling and terrifying fireworks display—a single bolt packs over 1 billion volts of electricity and is hotter than the surface of the Sun! Where does this colossal electric charge come from inside a storm cloud?",
        "theory": r"""
<h3>The Electrical Engine Inside Storm Clouds</h3>
<p>Inside a towering cumulonimbus cloud, violent upward convection winds (moving at $>100\text{ km/h}$) and descending downdrafts create intense internal chaos:</p>

<h4>1. Frictional Charge Generation</h4>
<ul>
  <li>Freezing temperatures in the upper cloud convert water into tiny ice crystals, soft hail pellets, and supercooled water droplets.</li>
  <li>Turbulent winds cause millions of these ice crystals and water droplets to collide vigorously. This intense <strong>frictional rubbing rubs electrons off</strong>, generating immense static electric charges!</li>
</ul>

<h4>2. Polarity Separation</h4>
<ul>
  <li><strong>Upper Cloud Positivity ($+$):</strong> Lighter, smaller ice crystals lose electrons, acquire a <strong>positive charge ($+$)</strong>, and are carried by updrafts to the very top of the cloud ($10\text{ to }15\text{ km}$ high).</li>
  <li><strong>Lower Cloud Negativity ($- $):</strong> Heavier water droplets and hail pellets gain electrons, acquire a <strong>heavy negative charge ($- $)</strong>, and settle in the lower base of the cloud ($1\text{ to }2\text{ km}$ altitude).</li>
</ul>

<h4>3. The Lightning Flash (Dielectric Breakdown)</h4>
<p>Air is normally an excellent electrical insulator. However, as the negative charge in the cloud base climbs into hundreds of millions of volts, the electric field becomes so extreme that the <strong>insulating property of air breaks down (dielectric ionization)</strong>.</p>
<p>A blinding river of electrons cascades through ionized plasma channels between cloud layers, or arcs straight down to the positively charged ground. This sudden, colossal electrostatic discharge is <strong>Lightning</strong>!</p>
""",
        "vocabulary": [
            {"word": "Lightning", "definition": "A colossal electric discharge of static charges formed inside storm clouds through dielectric breakdown of air."},
            {"word": "Dielectric Breakdown", "definition": "The failure of an insulating substance (like air) to block current when electric field strength exceeds critical threshold ($>3\\times 10^6\\text{ V/m}$)."},
            {"word": "Charge Separation", "definition": "The spatial segregation of positive ice crystals at cloud tops and negative droplets at cloud bases."},
            {"word": "Plasma Channel", "definition": "A luminous, intensely heated path of ionized air through which electric charges flow during a lightning bolt."}
        ],
        "sim_id": "lightning_charge_breakdown_sim",
        "checkpoints": [
            {
                "question": "How do clouds become electrically charged to produce lightning?",
                "options": [
                    "They absorb electricity from high-voltage power lines",
                    "Violent updrafts and downdrafts cause ice crystals and water droplets to collide, rubbing static charges via friction",
                    "Solar light beams electrocute the clouds",
                    "Airplanes flying through drop electrical batteries"
                ],
                "correct": 1,
                "explanation": "Collisions between ascending ice crystals and descending hail pellets generate static electricity through frictional contact.",
                "solution": "Microscopic collisions between ice crystals and water droplets generate massive static electric charges."
            },
            {
                "question": "What is the typical spatial charge distribution inside an active thunderhead cloud?",
                "options": [
                    "Positive charges at the top, and negative charges concentrated at the base",
                    "Negative charges at the top, and positive charges at the base",
                    "Only positive charges with zero negative charges",
                    "Charges distributed completely randomly like sprinkles"
                ],
                "correct": 0,
                "explanation": "Lighter positive ice crystals rise to the upper cloud, while heavier negative droplets settle at the lower cloud base.",
                "solution": "Cloud polarity: Top is Positive ($+$); Base is Negative ($-$). Ground induces Positive ($+$)."
            }
        ]
    },

    # SLIDE 12
    {
        "id": 12,
        "title": "Thunder & Regional Storms",
        "tag": "Acoustic Shockwave • Cultural Geography",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Flash! And then... BOOM! A rolling, house-shaking roar rattles your windows. That is thunder! Did you know that India has unique cultural and regional names for pre-monsoon thunderstorms? Let's explore thunder acoustics and regional storms.",
        "theory": r"""
<h3>What Produces the Sound of Thunder?</h3>
<p>A lightning bolt transfers up to $30,000\text{ Amperes}$ of electric current in microseconds, instantly heating the narrow air channel to a staggering <strong>$30,000^\circ\text{C}$—five times hotter than the surface of the Sun!</strong></p>
<ol>
  <li><strong>Explosive Thermal Expansion:</strong> Superheated air expands with supersonic speed into the surrounding colder air.</li>
  <li><strong>Sonic Shockwave:</strong> This sudden violent expansion creates a supersonic pressure shockwave that propagates through the atmosphere as a deafening acoustic roar: <strong>Thunder</strong>!</li>
  <li><strong>Why Flash Precedes Thunder:</strong> Light travels at an incredible speed of $300,000,000\text{ m/s}$ ($3 \times 10^8\text{ m/s}$), reaching our eyes virtually instantaneously. Sound travels at a modest speed of roughly $340\text{ m/s}$. That's why you always see the lightning flash several seconds before you hear the rumble of thunder!</li>
</ol>

<h4>Regional Names of Pre-Monsoon Thunderstorms in India</h4>
<table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.85rem;">
  <thead>
    <tr style="border-bottom: 2px solid #38bdf8; color: #38bdf8;">
      <th style="padding: 0.35rem; text-align: left;">Regional Name</th>
      <th style="padding: 0.35rem; text-align: left;">States / Regions</th>
      <th style="padding: 0.35rem; text-align: left;">Characteristics & Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #f59e0b;">Kalboishakhi</td>
      <td style="padding: 0.35rem;">West Bengal, Bihar, Jharkhand, Odisha</td>
      <td style="padding: 0.35rem;">Fierce evening thunderstorms in Baisakh (April–May); brings brief relief from scorching heat.</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #38bdf8;">Bordoisila</td>
      <td style="padding: 0.35rem;">Assam & Northeast India</td>
      <td style="padding: 0.35rem;">Pre-monsoon squalls marking the arrival of the spring festival (Rongali Bihu).</td>
    </tr>
    <tr>
      <td style="padding: 0.35rem; font-weight: bold; color: #10b981;">Mango Showers</td>
      <td style="padding: 0.35rem;">Kerala, Karnataka, Tamil Nadu</td>
      <td style="padding: 0.35rem;">Beneficial pre-monsoon showers that aid early ripening of mangoes and blossom coffee plants.</td>
    </tr>
  </tbody>
</table>
""",
        "vocabulary": [
            {"word": "Thunder", "definition": "The acoustic shockwave generated by the explosive thermal expansion of air heated by a lightning bolt."},
            {"word": "Supersonic Expansion", "definition": "Air expansion occurring at speeds faster than the local speed of sound ($>340\\text{ m/s}$), generating shockwaves."},
            {"word": "Kalboishakhi", "definition": "Fierce localized pre-monsoon thunderstorms in Bengal, Bihar, and Jharkhand occurring in the Hindu month of Boishakh."},
            {"word": "Mango Showers", "definition": "Pre-monsoon convective rainfall in southern India that accelerates the ripening of mango fruit crops."}
        ],
        "sim_id": "thunder_sound_distance_sim",
        "checkpoints": [
            {
                "question": "What is the physical cause of the loud roaring sound of thunder?",
                "options": [
                    "Clouds physically colliding like giant rocks in the sky",
                    "Rapid superheating of air by a lightning bolt causes it to expand explosively, producing a supersonic shockwave",
                    "Airplanes breaking the sound barrier inside clouds",
                    "Heavy raindrops slapping against ocean waves"
                ],
                "correct": 1,
                "explanation": "Lightning heats air to $30,000^\\circ\\text{C}$ in microseconds. The explosive expansion of this heated air creates the acoustic shockwave of thunder.",
                "solution": "Lightning thermal spike ($30,000^\\circ\\text{C}$) $\\rightarrow$ explosive expansion $\\rightarrow$ acoustic shockwave = Thunder."
            },
            {
                "question": "In Kerala and Karnataka, pre-monsoon thunderstorms are popularly called 'Mango Showers'. Why?",
                "options": [
                    "Because mango fruits literally fall from clouds during the storm",
                    "Because the timely showers aid in the early ripening of prized mango crops and coffee blossoms",
                    "Because the rain smells like mango juice",
                    "Because lightning only strikes mango trees"
                ],
                "correct": 1,
                "explanation": "These essential pre-monsoon convective rains provide vital moisture that allows mangoes to mature and ripen ahead of summer.",
                "solution": "Agricultural significance: Showers nourish and ripen mango crops in South India."
            }
        ]
    },

    # SLIDE 13
    {
        "id": 13,
        "title": "Lightning Conductors & Safety",
        "tag": "Protective Engineering • Outdoor Survival",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "A single direct lightning strike can shatter concrete pillars, blow out electrical grids, and spark devastating building fires! How do skyscrapers protect themselves? And what should you do if caught in an open field during a thunderstorm? Let's learn life-saving lightning safety.",
        "theory": r"""
<h3>The Lightning Conductor (Lightning Rod)</h3>
<p>Invented by Benjamin Franklin, a <strong>lightning conductor</strong> is a protective device installed on tall buildings, monuments, and bridges to safely channel lightning strikes into the earth:</p>
<ul>
  <li><strong>Pointed Metallic Spikes:</strong> A thick copper or galvanized iron rod is mounted on the highest roof peak, ending in sharp metallic spikes pointing toward the sky.</li>
  <li><strong>Heavy Down-Conductor Strip:</strong> A thick copper strip runs down the outer wall of the building without breaks.</li>
  <li><strong>Earthing Plate:</strong> The lower end connects to a large copper or metal plate buried deep underground in moist, conductive soil packed with charcoal and salt.</li>
  <li><strong>How It Protects:</strong> When lightning strikes, the electric charges travel harmlessly through the low-resistance copper strip directly into the ground, completely bypassing walls, wiring, and occupants!</li>
</ul>

<h3>Personal Outdoor Safety During Lightning</h3>
<ol>
  <li><strong>AVOID Tall Isolated Objects:</strong> NEVER seek shelter under tall solitary trees, telephone poles, or high towers—lightning naturally strikes the tallest protruding object!</li>
  <li><strong>AVOID Metal & Water:</strong> Stay away from metal fences, pipes, railway tracks, and get out of swimming pools, lakes, or wet rice paddies immediately (water conducts electricity).</li>
  <li><strong>Crouch in Low-Lying Open Areas:</strong> If caught in an open field with nowhere to go, <strong>squat low on the balls of your feet</strong> with hands on knees and head tucked low. Do NOT lie flat on the ground (this increases contact area for deadly ground currents).</li>
  <li><strong>Cars Are Safe (Faraday Cage):</strong> A fully enclosed metal vehicle (car, bus) is very safe; its metal shell conducts lightning around you to the ground.</li>
</ol>
""",
        "vocabulary": [
            {"word": "Lightning Conductor", "definition": "A tall metal rod installed atop buildings connected to an underground grounding plate to safely dissipate lightning strikes."},
            {"word": "Earthing (Grounding)", "definition": "The safe transfer of excess electrical charges directly into the vast conductive reservoir of the Earth."},
            {"word": "Lightning Crouch", "definition": "A survival stance: squatting low on the balls of your feet with head tucked to minimize height and ground contact."},
            {"word": "Faraday Cage Effect", "definition": "The electrostatic shielding provided by a closed conductive metal enclosure (like a car) that blocks internal electric fields."}
        ],
        "sim_id": "lightning_conductor_earthing_sim",
        "checkpoints": [
            {
                "question": "How does a metallic lightning conductor mounted on a skyscraper protect the building from structural fire and damage?",
                "options": [
                    "It freezes the lightning bolt into ice before it hits",
                    "It provides a low-resistance path that safely routes the massive electric discharge directly into a deep underground grounding plate",
                    "It reflects the lightning back into outer space like a mirror",
                    "It converts electrical current into drinking water"
                ],
                "correct": 1,
                "explanation": "The heavy copper rod offers the path of least electrical resistance, channeling millions of volts safely into the ground.",
                "solution": "Function: Safely routes electrical discharge into deep earth, protecting structural masonry."
            },
            {
                "question": "If you are caught in an open field during a severe thunderstorm with nowhere to hide, what is the safest physical action to take?",
                "options": [
                    "Climb the tallest tree in the field",
                    "Lie completely flat on your stomach in a puddle of water",
                    "Squat low on the balls of your feet with hands on knees and head tucked low (Lightning Crouch)",
                    "Hold an umbrella with a sharp metal tip straight up in the air"
                ],
                "correct": 2,
                "explanation": "Crouching low on the balls of your feet minimizes your physical height while keeping minimal contact with the ground, reducing ground-current risk.",
                "solution": "Safety protocol: The Lightning Crouch minimizes height and ground contact without lying flat."
            }
        ]
    },

    # SLIDE 14
    {
        "id": 14,
        "title": "Cyclone Genesis & Coriolis",
        "tag": "Tropical Meteorology • Giant Spirals",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Spanning hundreds of kilometers across oceans, cyclones are the most energetic storms on Earth! Powered by warm tropical sea water and spun by the rotation of the Earth, they unleash catastrophic winds. Let's see how cyclones are born.",
        "theory": r"""
<h3>What is a Cyclone?</h3>
<p>A <strong>Cyclone</strong> (also known as a <em>hurricane</em> in the Atlantic or a <em>typhoon</em> in the Pacific) is a massive, rotating storm system characterized by an intense central low-pressure center, violent gale-force winds, and torrential spirals of rainfall.</p>

<h4>The Three Essential Ingredients for Cyclone Genesis</h4>
<ol>
  <li><strong>Warm Tropical Ocean Waters ($>26.5^\circ\text{C}$):</strong> A cyclone is a thermal heat engine. It can only form over vast ocean surfaces where water temperatures reach at least $26.5^\circ\text{C}$ down to a depth of 50 meters, providing an endless supply of evaporating moisture.</li>
  <li><strong>Latent Heat Energy Release:</strong> Immense volumes of warm moist air ascend into the sky. As water vapour condenses into towering storm clouds, it releases colossal quantities of <strong>latent heat of condensation</strong>. This heat warms the surrounding air, making it rise even faster and sucking more air into a deepening low-pressure vortex!</li>
  <li><strong>The Coriolis Effect (Earth's Rotation):</strong> As air rushes inward toward the low-pressure core, <strong>Earth's rotation deflects the winds (Coriolis force)</strong>. This causes the air to spin into a ferocious vortex—spiraling <strong>counter-clockwise</strong> in the Northern Hemisphere (Bay of Bengal & Arabian Sea) and clockwise in the Southern Hemisphere!</li>
</ol>
""",
        "vocabulary": [
            {"word": "Cyclone", "definition": "A colossal rotating tropical storm system centered on deep low pressure, featuring violent winds and spiral rainbands."},
            {"word": "Coriolis Effect", "definition": "The apparent deflection of moving air masses caused by Earth's rotational spin, twisting winds into spiral vortices."},
            {"word": "Thermal Heat Engine", "definition": "A thermodynamic system (like a cyclone) that converts oceanic thermal energy into violent mechanical wind kinetic energy."},
            {"word": "Tropical Depression", "definition": "An organized low-pressure weather system over tropical seas with sustained winds under $62\\text{ km/h}$ that can escalate into a cyclone."}
        ],
        "sim_id": "cyclone_vortex_coriolis_sim",
        "checkpoints": [
            {
                "question": "What is the primary energy source that fuels and powers a tropical cyclone?",
                "options": [
                    "Underwater volcanic eruptions on the sea bed",
                    "Warm ocean waters (above 26.5°C) and the continuous release of latent heat during water vapour condensation",
                    "Solar flares hitting polar ice sheets",
                    "Magnetic fields radiating from the equator"
                ],
                "correct": 1,
                "explanation": "Cyclones derive their colossal energy from the evaporation of warm sea water and the latent heat released when water vapour condenses.",
                "solution": "Fuel mechanism: Warm ocean water ($>26.5^\\circ\\text{C}$) + Latent heat of condensation = Cyclone energy engine."
            },
            {
                "question": "What planetary physical phenomenon causes the winds rushing into a cyclone's low-pressure center to spin in a giant spiral vortex?",
                "options": [
                    "The gravitational pull of the Moon",
                    "Earth's rotation deflecting moving winds via the Coriolis effect",
                    "The shape of the ocean coastline",
                    "Friction between water waves and fish schools"
                ],
                "correct": 1,
                "explanation": "Earth's daily axial rotation creates the Coriolis force, deflecting incoming winds into counter-clockwise spirals in the Northern Hemisphere.",
                "solution": "Vortex formation: Earth's rotation $\\rightarrow$ Coriolis deflection $\\rightarrow$ Spiral rotation."
            }
        ]
    },

    # SLIDE 15
    {
        "id": 15,
        "title": "The Cyclone Eye & Surge",
        "tag": "Storm Anatomy • Coastal Surge Destruction",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "At the very heart of the most ferocious storm lies a shocking secret: the 'Eye' of the cyclone is completely calm, sunny, and cloudless! But right outside the eye lurks the catastrophic eyewall and deadly storm surges. Let's study cyclone anatomy.",
        "theory": r"""
<h3>The Anatomy of a Mature Cyclone</h3>
<p>A fully formed tropical cyclone spans between $150\text{ and }1,000\text{ km}$ across and displays three distinct architectural zones:</p>

<h4>1. The Eye (Central Calm)</h4>
<ul>
  <li>A roughly circular area at the very center of the storm, typically $20\text{ to }50\text{ km}$ in diameter.</li>
  <li><strong>The Paradox:</strong> While surrounding regions experience terror, the eye features <strong>calm winds, light breezes, no rainfall, and often clear blue skies!</strong></li>
  <li>Air gently sinks in the eye, compressing and warming, which inhibits cloud formation. It has the <strong>lowest atmospheric pressure on Earth (often $<920\text{ hPa}$)</strong>.</li>
</ul>

<h4>2. The Eyewall (Zone of Maximum Fury)</h4>
<p>Immediately ringing the calm eye is a colossal vertical wall of dense cumulonimbus clouds. This is the <strong>most dangerous part of the cyclone</strong>, generating howling winds ($>200\text{ km/h}$), violent updrafts, and blinding torrential downpours.</p>

<h4>3. The Deadly Storm Surge</h4>
<p>The greatest threat to human life during a cyclone is not wind—it is the <strong>Storm Surge</strong>:</p>
<ol>
  <li>The extreme low pressure inside the cyclone acts like a giant vacuum cleaner, physically lifting the sea surface underneath.</li>
  <li>Furious eyewall winds pile up ocean water, driving a colossal <strong>wall of seawater 3 to 12 metres high</strong> slamming onto coastlines!</li>
  <li>Storm surges inundate low-lying coastal villages within minutes, submerging homes, destroying roads, and drowning agricultural fields in saltwater (e.g., <strong>Super Cyclone Amphan in 2020</strong> generated peak wind speeds of $270\text{ km/h}$ and devastating surges across West Bengal and Odisha).</li>
</ol>
""",
        "vocabulary": [
            {"word": "Eye of the Cyclone", "definition": "The calm, cloud-free central core of a cyclone with the lowest barometric pressure and gentle descending winds."},
            {"word": "Eyewall", "definition": "The vertical ring of towering clouds surrounding the eye where the storm's most violent winds and heaviest rain occur."},
            {"word": "Storm Surge", "definition": "A catastrophic coastal rise of seawater (3 to 12 m high) driven ashore by extreme low pressure and hurricane winds."},
            {"word": "Cyclone Amphan", "definition": "A historic Super Cyclonic Storm in May 2020 that struck West Bengal and Odisha with peak winds of $270\\text{ km/h}$."}
        ],
        "sim_id": "cyclone_eye_storm_surge_sim",
        "checkpoints": [
            {
                "question": "What are the weather conditions typically experienced inside the 'Eye' at the very center of a mature cyclone?",
                "options": [
                    "The highest wind speeds and heaviest rainfall of the entire storm",
                    "Calm light winds, clear or partly cloudy skies, and an absence of rainfall",
                    "Freezing blizzards with giant hailstones",
                    "Continuous electric lightning discharges"
                ],
                "correct": 1,
                "explanation": "The Eye is a calm, cloudless descending-air zone at the cyclone's center, surrounded by the destructive eyewall.",
                "solution": "Cyclone Eye: Lowest pressure, calm winds, clear skies, surrounded by violent eyewall."
            },
            {
                "question": "What is a 'storm surge' during a cyclone, and why is it so devastating?",
                "options": [
                    "A sudden surge of electricity through television cables",
                    "A colossal wall of seawater (3 to 12 metres high) driven inland by extreme winds and low pressure, causing severe coastal flooding",
                    "A sudden burst of desert dust storms",
                    "The sound of ocean waves splashing on rocks"
                ],
                "correct": 1,
                "explanation": "Storm surges are giant seawater walls pushed onto land by cyclone winds and suction pressure, causing catastrophic drowning and flooding.",
                "solution": "Storm surge = 3-12 m seawater wall driven onto coastal land, causing catastrophic flooding."
            }
        ]
    },

    # SLIDE 16
    {
        "id": 16,
        "title": "IMD Tracking & Preparedness",
        "tag": "Meteorological Surveillance • Disaster Management",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Years ago, cyclones struck without warning, claiming hundreds of thousands of lives. Today, modern science has changed everything! The India Meteorological Department tracks storms in real time using space satellites and Doppler radars. Let's study early warning systems.",
        "theory": r"""
<h3>The India Meteorological Department (IMD)</h3>
<p>Formed in 1875, the <strong>India Meteorological Department (IMD)</strong> is the national weather agency responsible for tracking weather phenomena, rainfall forecasts, and cyclone warnings across the subcontinent.</p>

<h4>Modern Cyclone Surveillance Tools</h4>
<ul>
  <li><strong>Geostationary Weather Satellites (INSAT & GSAT Series):</strong> Positioned $36,000\text{ km}$ above the equator, these satellites beam high-resolution infrared and visible images every 15 minutes, tracking the birth and path of ocean depressions days before landfall.</li>
  <li><strong>Doppler Weather Radars (DWR):</strong> Installed along India's coastline (Chennai, Visakhapatnam, Kolkata, Paradip, Mumbai), Doppler radars detect wind velocity, precipitation intensity, and spiral rainbands up to $400\text{ km}$ offshore.</li>
  <li><strong>Cyclone Warning Dissemination System:</strong> The IMD issues alerts through a standardized 4-stage color code (Yellow = Watch, Orange = Alert, Red = Warning).</li>
</ul>

<h4>Disaster Preparedness & Cyclone Shelters</h4>
<p>India's modern disaster management network (NDRF, state agencies) has drastically reduced cyclone casualties:</p>
<ol>
  <li><strong>Dedicated Cyclone Shelters:</strong> Specially engineered multi-story concrete buildings built on high pilings above storm-surge flood lines provide safe refuge for millions of evacuated coastal residents.</li>
  <li><strong>Community Action:</strong> Heeding official radio/TV broadcasts, securing loose rooftop sheets, stocking non-perishable food and potable water, avoiding the sea, and moving to shelters early saves countless lives!</li>
</ol>
""",
        "vocabulary": [
            {"word": "IMD", "definition": "India Meteorological Department; the premier national governmental agency for weather observation and cyclone tracking."},
            {"word": "Doppler Weather Radar", "definition": "Advanced coastal radar that measures both the position and velocity of precipitation inside storm clouds."},
            {"word": "Cyclone Shelter", "definition": "A fortified, elevated concrete building designed to safely shelter coastal communities above storm surge flood lines."},
            {"word": "INSAT Weather Satellites", "definition": "Indian geostationary satellites continuously monitoring tropical weather systems and storm development."}
        ],
        "sim_id": "imd_satellite_tracking_sim",
        "checkpoints": [
            {
                "question": "Which premier national agency in India is responsible for monitoring, tracking, and issuing official warnings for cyclones?",
                "options": [
                    "Indian Railways",
                    "India Meteorological Department (IMD)",
                    "Archaeological Survey of India",
                    "Reserve Bank of India"
                ],
                "correct": 1,
                "explanation": "The India Meteorological Department (IMD) is the official government agency tasked with weather forecasting and cyclone warnings.",
                "solution": "Agency responsible: India Meteorological Department (IMD)."
            },
            {
                "question": "How have dedicated coastal cyclone shelters and early satellite warnings saved thousands of lives during recent Indian cyclones?",
                "options": [
                    "They allow people to steer the cyclone out into the ocean",
                    "They allow timely mass evacuation of vulnerable populations to elevated, fortified concrete shelters above storm surge flood levels",
                    "They eliminate the cyclone's wind completely",
                    "They stop all rainfall from falling"
                ],
                "correct": 1,
                "explanation": "Advanced satellite warnings enable disaster agencies to evacuate coastal residents to elevated concrete shelters before storm surges hit.",
                "solution": "Preparedness: Early warning + Mass evacuation to fortified elevated shelters = Lives saved."
            }
        ]
    },

    # SLIDE 17 - MASTERY CHALLENGE PART I (Q1-Q10)
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "tag": "Comprehensive Review • Questions 1 to 10",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Fantastic work completing the lessons! Now it's time to test your mastery. Tackle these 10 in-depth questions on the definition of pressure, area relationships, liquid pressure directions, and dam engineering. Click the solution button to review the step-by-step breakdown!",
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10
    },

    # SLIDE 18 - MASTERY CHALLENGE PART II (Q11-Q20)
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "tag": "Comprehensive Review • Questions 11 to 20",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "You're doing wonderfully! Part II focuses on atmospheric pressure, body fluid balance, high-altitude nosebleeds, Bernoulli's wind pressure drops, and wind formation. Read each problem carefully!",
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10
    },

    # SLIDE 19 - MASTERY CHALLENGE PART III (Q21-Q30)
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "tag": "Comprehensive Review • Questions 21 to 30",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "Welcome to Part III! Here we dive deep into land and sea breeze cycles, storm convection, cloud charge separation, lightning physics, thunder acoustics, and Indian regional storms. Challenge your understanding!",
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10
    },

    # SLIDE 20 - MASTERY CHALLENGE PART IV (Q31-Q40)
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "tag": "Comprehensive Review • Questions 31 to 40",
        "badge": "Class 8 Science • Chapter 6",
        "avatar_dialogue": "The final summit! Part IV tests your knowledge of lightning conductors, cyclone genesis, Coriolis rotation, the calm Eye, catastrophic storm surges, and IMD satellite tracking. Finish strong and achieve complete chapter mastery!",
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
        "question": "What is the scientific definition of pressure, and what is its standard mathematical formula?",
        "options": [
            "Pressure is force multiplied by speed ($P = F \\cdot v$)",
            "Pressure is the force acting perpendicular to a surface per unit area ($P = F / A$)",
            "Pressure is mass divided by volume ($P = m / V$)",
            "Pressure is gravitational potential energy"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Definition:</strong> In physical science, pressure is defined as the magnitude of thrust (normal force) acting perpendicular to a surface divided by the contact surface area:
    $$P = \frac{\text{Force}}{\text{Area}} = \frac{F}{A}$$
  </li>
  <li><strong>SI Units:</strong> Force is measured in newtons ($\text{N}$), area in square metres ($\text{m}^2$), giving pressure in $\text{N/m}^2$ or Pascals ($\text{Pa}$).</li>
</ol>
"""
    },

    # Q2
    {
        "id": 2,
        "question": "A force of 600 N acts perpendicular to a flat surface having an area of 3 m². What is the pressure exerted on the surface?",
        "options": [
            "200 Pa",
            "1,800 Pa",
            "603 Pa",
            "50 Pa"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Given Data:</strong>
    <ul>
      <li>Force $F = 600\text{ N}$</li>
      <li>Area $A = 3\text{ m}^2$</li>
    </ul>
  </li>
  <li><strong>Calculation:</strong>
    $$P = \frac{F}{A} = \frac{600\text{ N}}{3\text{ m}^2} = 200\text{ N/m}^2 = 200\text{ Pa}$$
  </li>
  <li>The pressure exerted is $200\text{ Pa}$.</li>
</ol>
"""
    },

    # Q3
    {
        "id": 3,
        "question": "Why does a camel walk and run easily on soft desert sand without sinking, while a horse with smaller hooves sinks rapidly?",
        "options": [
            "Camels have broad, wide padded hooves that distribute body weight over a large area, dramatically reducing pressure on the sand",
            "Camels have zero gravitational mass in the desert",
            "Sand magnetically repels camel hair",
            "Horses are 100 times heavier than camels"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Area Relationship:</strong> Pressure is inversely proportional to area: $P = F/A$.</li>
  <li><strong>Camel Anatomy:</strong> Camels have large, broad, padded feet. This large contact area spreads their body weight widely.</li>
  <li><strong>Reduced Pressure:</strong> The low pressure exerted prevents their feet from sinking into soft, shifting sand dunes.</li>
</ol>
"""
    },

    # Q4
    {
        "id": 4,
        "question": "A porter carrying a heavy suitcase on his head places a round piece of cloth (gatta) between his head and the suitcase. Why?",
        "options": [
            "To make the suitcase heavier",
            "To increase the contact area between the suitcase and his head, reducing pressure and pain",
            "To prevent electricity from leaking out of the suitcase",
            "To absorb sweat so the suitcase does not get wet"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Mechanism:</strong> A round rolled cloth increases the surface area of contact between the porter's head and the hard suitcase base.</li>
  <li><strong>Pressure Reduction:</strong> For the same weight $F$, increasing area $A$ significantly lowers the contact pressure:
    $$P = \frac{F}{A}$$
  </li>
  <li>This makes carrying the heavy load far more comfortable.</li>
</ol>
"""
    },

    # Q5
    {
        "id": 5,
        "question": "In what direction does a liquid at rest exert pressure inside a container?",
        "options": [
            "Only straight downward on the bottom base",
            "Only horizontally sideways on the walls",
            "On the bottom and sideways on the walls, acting equally in all directions at a given depth",
            "Only upward toward the ceiling"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Fluid Mobility:</strong> Unlike solids, liquids are fluids whose molecules move randomly and collide with all boundary walls.</li>
  <li><strong>Omnidirectionality:</strong> Liquids exert pressure downward on the base, sideways on container walls, and upward (buoyancy), acting equally in all directions at any fixed depth.</li>
</ol>
"""
    },

    # Q6
    {
        "id": 6,
        "question": "How does the pressure exerted by a liquid column change as the height (depth) of the liquid column increases?",
        "options": [
            "Pressure decreases to zero",
            "Pressure remains completely unchanged",
            "Pressure increases directly and proportionally with column height ($P = \\rho g h$)",
            "Pressure fluctuates randomly"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Hydrostatic Law:</strong> Liquid pressure is directly proportional to depth:
    $$P = \rho \cdot g \cdot h$$
  </li>
  <li>As height of the liquid column ($h$) increases, the weight of liquid pressing down increases, raising pressure at deeper levels.</li>
</ol>
"""
    },

    # Q7
    {
        "id": 7,
        "question": "Why are domestic overhead water tanks in residential buildings always installed on the highest rooftops?",
        "options": [
            "To keep the water closer to the stars",
            "Because greater vertical column height creates higher hydrostatic pressure ($P = \\rho g h$), ensuring a strong flow from household taps downstairs",
            "To prevent birds from drinking the water",
            "Because water boils at room temperature on the ground"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Height Elevation:</strong> Placing tanks on rooftops maximizes the vertical water column height ($h$) relative to downstairs taps.</li>
  <li><strong>Tap Pressure:</strong> By $P = \rho g h$, this substantial elevation head delivers high pressure and strong water streams to showers and kitchen faucets.</li>
</ol>
"""
    },

    # Q8
    {
        "id": 8,
        "question": "Why are concrete dams built with much broader and thicker bases at the bottom than at the top?",
        "options": [
            "Because deep water exerts massive horizontal hydrostatic pressure that increases with depth, requiring a thicker base to withstand the immense load",
            "To allow trucks to drive across the bottom of the lake",
            "Because concrete melts in deep water",
            "To absorb sound waves from frogs"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Depth Effect:</strong> Hydrostatic pressure increases linearly with reservoir depth ($P \propto h$).</li>
  <li><strong>Dam Design:</strong> At the reservoir bottom, water pressure is at its maximum. Dams are constructed with broad, reinforced bases to withstand this colossal bursting force.</li>
</ol>
"""
    },

    # Q9
    {
        "id": 9,
        "question": "What is the gaseous envelope of air surrounding planet Earth called, and what is the pressure it exerts known as?",
        "options": [
            "Hydrosphere and hydrostatic pressure",
            "Lithosphere and tectonic pressure",
            "Atmosphere and atmospheric pressure",
            "Ionosphere and cosmic pressure"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Atmosphere:</strong> The thick blanket of gases surrounding Earth held by planetary gravity.</li>
  <li><strong>Atmospheric Pressure:</strong> The downward force exerted by the weight of this air column per unit area on Earth's surface.</li>
</ol>
"""
    },

    # Q10
    {
        "id": 10,
        "question": "How many Pascals are there in 1 hectopascal (hPa), the standard unit used by weather forecasters?",
        "options": [
            "1 hPa = 1 Pa",
            "1 hPa = 10 Pa",
            "1 hPa = 100 Pa",
            "1 hPa = 1,000 Pa"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Prefix 'Hecto':</strong> Represents a multiplier of $100$ ($10^2$).</li>
  <li><strong>Conversion:</strong>
    $$1\text{ hPa} = 100\text{ Pa} = 1\text{ millibar (mb)}$$
  </li>
  <li>Standard sea-level air pressure is approximately $1013\text{ hPa}$.</li>
</ol>
"""
    },

    # Q11
    {
        "id": 11,
        "question": "Why are human beings and land animals on Earth NOT crushed by the enormous weight of the atmospheric air column pressing down on them?",
        "options": [
            "Because the atmosphere only presses down on soil, never on animals",
            "Because internal fluids and blood exert an outward pressure that balances the external atmospheric pressure",
            "Because human skin is made of impenetrable steel",
            "Because air has zero weight at sea level"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Internal Pressure:</strong> Body cells, blood vessels, and tissues contain fluids and dissolved gases under pressure.</li>
  <li><strong>Equilibrium:</strong> This internal pressure pushes outward with approximately $101.3\text{ kPa}$, matching external atmospheric pressure.</li>
  <li><strong>Net Force:</strong> Net crushing force on the body is zero.</li>
</ol>
"""
    },

    # Q12
    {
        "id": 12,
        "question": "Why do high-altitude mountain climbers often suffer from nosebleeds at the summit of tall mountains?",
        "options": [
            "Because external air pressure drops drastically at high altitude, causing higher internal blood pressure to rupture delicate nasal capillaries",
            "Because mountain rocks are radioactive",
            "Because snow contains acid",
            "Because gravity is zero on mountain tops"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Altitude Drop:</strong> As altitude increases, the air column above is shorter, so atmospheric pressure drops significantly.</li>
  <li><strong>Imbalance:</strong> Internal blood pressure remains higher than the thin outside air.</li>
  <li><strong>Rupture:</strong> This outward pressure gradient bursts fragile nasal capillaries, causing nosebleeds.</li>
</ol>
"""
    },

    # Q13
    {
        "id": 13,
        "question": "According to Bernoulli's principle, what happens to the air pressure in a region where winds are blowing at very high speeds?",
        "options": [
            "The air pressure increases dramatically",
            "The air pressure is reduced significantly",
            "The air pressure turns into vacuum instantly",
            "The air pressure is unaffected by wind speed"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Bernoulli's Discovery:</strong> High-speed fluid flow is accompanied by a reduction in lateral static pressure.</li>
  <li><strong>Rule:</strong> High-speed winds create low-pressure zones. Stagnant, still air maintains higher static pressure.</li>
</ol>
"""
    },

    # Q14
    {
        "id": 14,
        "question": "What happens when you blow a fast stream of air between two lightweight balloons suspended 5 cm apart?",
        "options": [
            "They are blown far apart",
            "They move inward and pull together because fast air creates a low-pressure area between them",
            "They float to the ceiling",
            "They pop from friction"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Bernoulli Effect:</strong> Fast air stream in the gap lowers pressure between the balloons.</li>
  <li><strong>External Force:</strong> Normal atmospheric pressure on the outer sides is higher, pushing the balloons inward toward each other.</li>
</ol>
"""
    },

    # Q15
    {
        "id": 15,
        "question": "Why do violent cyclone winds often lift tin and thatched roofs off houses during storms?",
        "options": [
            "High-speed wind blowing over the roof drops air pressure above, while higher pressure inside the house pushes the roof upward",
            "Rainwater pulls the roof up into the clouds",
            "Lightning magnets attract the tin metal",
            "The house foundation pushes the walls upward"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Pressure Difference:</strong> Furious winds across the roof create a strong low-pressure zone above it.</li>
  <li><strong>Lift Force:</strong> Trapped, still air inside the house remains at higher atmospheric pressure, producing an upward lift force that tears the roof off.</li>
</ol>
"""
    },

    # Q16
    {
        "id": 16,
        "question": "What is the primary driving cause of all atmospheric winds blowing across planet Earth?",
        "options": [
            "The gravitational pull of passing comets",
            "Differences in atmospheric air pressure caused by unequal solar heating",
            "Trees swinging their branches in the breeze",
            "Ocean waves pushing air onto shores"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Pressure Differences:</strong> Unequal heating of Earth's surface creates regions of high and low pressure.</li>
  <li><strong>Wind Flow:</strong> Air rushes from high-pressure zones to low-pressure zones. This horizontal air motion is wind.</li>
</ol>
"""
    },

    # Q17
    {
        "id": 17,
        "question": "In what direction does atmospheric air always move between pressure systems?",
        "options": [
            "From regions of LOW pressure to regions of HIGH pressure",
            "From regions of HIGH pressure to regions of LOW pressure",
            "Only in vertical corkscrews without moving horizontally",
            "Directly toward the equator regardless of pressure"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Pressure Gradient:</strong> Fluid naturally moves down a pressure gradient from high to low pressure.</li>
  <li>Therefore, wind always flows from <strong>High Pressure to Low Pressure</strong>.</li>
</ol>
"""
    },

    # Q18
    {
        "id": 18,
        "question": "What is the relationship between the magnitude of a regional pressure difference and the resulting wind speed?",
        "options": [
            "Greater pressure differences produce higher wind speeds",
            "Pressure differences have no effect on wind speed",
            "Greater pressure differences make the wind stop completely",
            "Wind only blows when pressure is identical everywhere"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Steep Gradient:</strong> A larger pressure difference over a given distance creates a steeper pressure gradient force.</li>
  <li><strong>Acceleration:</strong> This stronger force accelerates air masses to higher velocities, producing stronger winds and gales.</li>
</ol>
"""
    },

    # Q19
    {
        "id": 19,
        "question": "Why does a coastal 'Sea Breeze' blow from the ocean onto the land during daytime?",
        "options": [
            "Land heats up faster than water in sunlight; warm air over land rises, creating low pressure that draws in cool air from the sea",
            "The sea freezes during daytime",
            "Ocean waves push air mechanically onto the beach",
            "Fish swim toward the shore pushing air"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Daytime Heating:</strong> Solid land has lower heat capacity and heats up faster than the ocean.</li>
  <li><strong>Low Pressure over Land:</strong> Warm air over land expands and ascends, creating a low-pressure area.</li>
  <li><strong>Inflow:</strong> Cooler, denser air over the sea (high pressure) flows onshore as the Sea Breeze.</li>
</ol>
"""
    },

    # Q20
    {
        "id": 20,
        "question": "Why does the coastal breeze reverse at night, blowing from the land toward the sea as a 'Land Breeze'?",
        "options": [
            "Land cools down much faster than the sea at night; warm air over the sea rises, drawing cool air offshore from the land",
            "The Moon pulls the air offshore with gravity",
            "The sea boils at night",
            "Sand dunes emit cold air jets"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Night-time Cooling:</strong> Without sun, land loses heat rapidly while the ocean retains heat.</li>
  <li><strong>Low Pressure over Sea:</strong> Air over the warm ocean rises, creating low pressure over water.</li>
  <li><strong>Offshore Flow:</strong> Denser, cooler air from the land flows out to sea as the Land Breeze.</li>
</ol>
"""
    },

    # Q21
    {
        "id": 21,
        "question": "What initial atmospheric condition triggers the formation of a severe thunderstorm over heated land?",
        "options": [
            "Intense surface heating causes warm, humid air to rise rapidly in thermal updrafts, creating a deep low-pressure zone",
            "Freezing snow cover on the ground",
            "A total eclipse of the Sun",
            "Earthquakes opening underground caverns"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Convection Updraft:</strong> Ground heating warms surface air, causing it to ascend rapidly.</li>
  <li><strong>Low Pressure:</strong> This creates a low-pressure vacuum that draws in cooler surrounding air.</li>
  <li><strong>Cloud Growth:</strong> Rising moisture condenses into towering cumulonimbus storm clouds.</li>
</ol>
"""
    },

    # Q22
    {
        "id": 22,
        "question": "How are massive static electrical charges generated inside a thunderstorm cloud?",
        "options": [
            "Violent upward and downward winds cause ice crystals, hail, and water droplets to collide and rub vigorously, transferring charges",
            "Clouds absorb electricity from power stations",
            "Solar radiation ionizes water into pure hydrogen",
            "Airplanes drop batteries into clouds"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Frictional Charging:</strong> Violent updrafts and downdrafts create continuous collisions between rising ice crystals and falling hail/droplets.</li>
  <li><strong>Triboelectricity:</strong> Frictional contact rubs electrons off, producing massive static electric charges inside the cloud.</li>
</ol>
"""
    },

    # Q23
    {
        "id": 23,
        "question": "Where are positive and negative charges typically segregated inside an active thunderhead cloud?",
        "options": [
            "Positive charges at the cloud top (lighter ice crystals), and negative charges at the cloud base (heavier droplets)",
            "Negative charges at the top, and positive at the base",
            "Positive and negative charges mixed completely uniformly",
            "Charges only exist outside the cloud"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Charge Separation:</strong> Lighter positively charged ice crystals are carried by updrafts to the cloud top.</li>
  <li><strong>Base:</strong> Heavier negatively charged water droplets and hail settle at the lower cloud base.</li>
</ol>
"""
    },

    # Q24
    {
        "id": 24,
        "question": "What occurs during the 'dielectric breakdown' of air that results in a visible lightning bolt?",
        "options": [
            "Air turns into solid glass",
            "The colossal charge buildup exceeds air's insulating capacity, ionizing a plasma path through which millions of volts discharge instantly",
            "The air molecules freeze into snowflakes",
            "Air stops conducting sound waves"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Insulation Breakdown:</strong> Air normally insulates against current flow.</li>
  <li><strong>Ionization:</strong> When electric field strength exceeds $\approx 3 \times 10^6\text{ V/m}$, air molecules ionize into plasma.</li>
  <li><strong>Discharge:</strong> Electric current surges through this ionized channel as a blinding lightning flash.</li>
</ol>
"""
    },

    # Q25
    {
        "id": 25,
        "question": "Why is the explosive sound of thunder heard several seconds AFTER the lightning flash is seen?",
        "options": [
            "Because thunder is created minutes after lightning finishes",
            "Because light travels at an enormous speed (300,000,000 m/s) almost instantaneously, while sound travels much slower (approx. 340 m/s)",
            "Because our ears react slower than our eyes",
            "Because sound waves bounce off the Moon before reaching Earth"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Speed of Light:</strong> $c \approx 3 \times 10^8\text{ m/s}$ (reaches us in microseconds).</li>
  <li><strong>Speed of Sound:</strong> $v_{\text{sound}} \approx 340\text{ m/s}$ (takes $\approx 3\text{ seconds}$ to travel $1\text{ km}$).</li>
  <li><strong>Delay:</strong> You see the flash first and hear the thunder rumble later.</li>
</ol>
"""
    },

    # Q26
    {
        "id": 26,
        "question": "If you see a lightning flash and hear the rumble of thunder exactly 6 seconds later, approximately how far away is the storm? ($v_{\\text{sound}} = 340\\text{ m/s}$)",
        "options": [
            "340 metres",
            "680 metres",
            "2,040 metres (approx. 2.04 km)",
            "6,000 metres"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Distance Formula:</strong>
    $$\text{Distance} = \text{Speed of Sound} \times \text{Time Delay}$$
  </li>
  <li><strong>Calculation:</strong>
    $$\text{Distance} = 340\text{ m/s} \times 6\text{ s} = 2,040\text{ metres} \approx 2.04\text{ km}$$
  </li>
  <li>The storm is roughly $2\text{ km}$ away.</li>
</ol>
"""
    },

    # Q27
    {
        "id": 27,
        "question": "What are fierce pre-monsoon thunderstorms accompanied by heavy downpours called in West Bengal, Bihar, and Jharkhand?",
        "options": [
            "Bordoisila",
            "Kalboishakhi (Nor'westers)",
            "Mango Showers",
            "Loo"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Regional Storm:</strong> In Bengal, Bihar, and Odisha, violent evening pre-monsoon thunderstorms in the month of Baisakh are known as <strong>Kalboishakhi</strong>.</li>
  <li>In Assam, they are called <em>Bordoisila</em>, and in South India, <em>Mango Showers</em>.</li>
</ol>
"""
    },

    # Q28
    {
        "id": 28,
        "question": "What is the regional name for pre-monsoon spring squalls in Assam that herald the arrival of the Rongali Bihu festival?",
        "options": [
            "Bordoisila",
            "Kalboishakhi",
            "Mango Showers",
            "Typhoon"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Assam Storm:</strong> Pre-monsoon thunderstorms in Assam are traditionally called <strong>Bordoisila</strong>.</li>
  <li>They mark the arrival of spring and the festive season of Bihu.</li>
</ol>
"""
    },

    # Q29
    {
        "id": 29,
        "question": "How does a metallic lightning conductor installed on top of a tall building safely protect the structure from lightning strikes?",
        "options": [
            "It absorbs lightning bolts and converts them into solar power",
            "It provides a low-resistance metallic pathway that safely routes the massive electrical current directly into a deep underground grounding plate",
            "It creates an invisible magnetic force field that deflects clouds",
            "It extinguishes electrical fires with built-in water sprinklers"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Low-Resistance Path:</strong> The copper rod and down-conductor offer minimal electrical resistance.</li>
  <li><strong>Earthing:</strong> When struck, the surge travels through the copper strip into an earthing plate buried deep in moist ground, protecting walls and occupants.</li>
</ol>
"""
    },

    # Q30
    {
        "id": 30,
        "question": "Why should you NEVER seek shelter under a tall, solitary tree during an outdoor thunderstorm?",
        "options": [
            "Because trees absorb all oxygen during storms",
            "Because tall, isolated objects are the most likely targets for lightning strikes; electrical current can jump from the tree to you",
            "Because trees attract rain onto your head",
            "Because birds will fly away"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Tallest Point:</strong> Lightning naturally strikes the tallest protruding object in an area.</li>
  <li><strong>Side Flash & Ground Current:</strong> A strike to the tree creates lethal side flashes and high-voltage ground currents that can electrocute anyone beneath.</li>
</ol>
"""
    },

    # Q31
    {
        "id": 31,
        "question": "What is the minimum ocean sea surface temperature required to fuel and sustain the formation of a tropical cyclone?",
        "options": [
            "0°C",
            "10°C",
            "At least 26.5°C down to a depth of roughly 50 metres",
            "100°C"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Thermal Threshold:</strong> Tropical cyclones require warm ocean waters of at least <strong>$26.5^\circ\text{C}$</strong>.</li>
  <li><strong>Fuel:</strong> This high sea surface temperature supplies abundant water vapour, whose condensation releases latent heat to power the cyclone engine.</li>
</ol>
"""
    },

    # Q32
    {
        "id": 32,
        "question": "In the Northern Hemisphere (including the Bay of Bengal and Arabian Sea), in which direction do winds spin around a cyclone's low-pressure center?",
        "options": [
            "Clockwise",
            "Counter-clockwise (anticlockwise)",
            "Straight outward in straight lines",
            "Vertically downward only"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Coriolis Deflection:</strong> In the Northern Hemisphere, Earth's rotation deflects moving air to the right.</li>
  <li><strong>Vortex Rotation:</strong> As air spirals inward toward a low-pressure center, this deflection forces the vortex into a <strong>counter-clockwise</strong> rotation.</li>
</ol>
"""
    },

    # Q33
    {
        "id": 33,
        "question": "What are the weather conditions typically found inside the 'Eye' of a mature cyclone?",
        "options": [
            "Ferocious 250 km/h winds and torrential downpours",
            "A calm, cloudless, light-wind region with the lowest atmospheric pressure of the entire storm",
            "Freezing blizzards and ice sheets",
            "Severe thunderstorms with continuous lightning"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>The Eye:</strong> The circular central core of a cyclone ($20\text{ to }50\text{ km}$ across).</li>
  <li><strong>Calm Conditions:</strong> Air gently descends, preventing cloud formation. It features calm winds, clear skies, and lowest atmospheric pressure.</li>
</ol>
"""
    },

    # Q34
    {
        "id": 34,
        "question": "Immediately surrounding the calm Eye of a cyclone is the 'Eyewall'. What occurs in this zone?",
        "options": [
            "Complete calm with no wind",
            "The most violent gale-force winds, torrential rain, and severe destruction of the entire cyclone",
            "Gentle sunny breezes",
            "Dry desert air with no moisture"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Eyewall:</strong> A dense vertical ring of cumulonimbus clouds ringing the eye.</li>
  <li><strong>Maximum Fury:</strong> Houses the storm's most destructive winds ($>200\text{ km/h}$) and torrential downpours.</li>
</ol>
"""
    },

    # Q35
    {
        "id": 35,
        "question": "What is a 'storm surge' during a cyclone, and why does it represent the greatest threat to coastal lives?",
        "options": [
            "A sudden surge of electrical power in grid lines",
            "A massive wall of ocean seawater (3 to 12 metres high) driven inland by extreme hurricane winds and low pressure, inundating coastal areas",
            "A sudden sandstorm blowing from deserts",
            "The rapid evaporation of seawater into clouds"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Storm Surge Genesis:</strong> Extreme low pressure elevates the sea surface, while howling winds push vast amounts of seawater toward land.</li>
  <li><strong>Impact:</strong> A 3 to 12 m wall of seawater crashes onto shore, causing catastrophic flooding and drowning low-lying coastal communities.</li>
</ol>
"""
    },

    # Q36
    {
        "id": 36,
        "question": "In May 2020, Super Cyclone Amphan struck eastern India (West Bengal and Odisha). What was its peak wind speed?",
        "options": [
            "50 km/h",
            "100 km/h",
            "270 km/h",
            "1,000 km/h"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Historical Fact:</strong> Super Cyclone Amphan in May 2020 attained peak sustained winds of approximately <strong>$270\text{ km/h}$</strong> over the Bay of Bengal.</li>
  <li>It caused extensive damage and coastal flooding across West Bengal and Bangladesh.</li>
</ol>
"""
    },

    # Q37
    {
        "id": 37,
        "question": "What technology does the India Meteorological Department (IMD) use to track cyclones days before they strike the coast?",
        "options": [
            "Submarine sonar microphones",
            "Geostationary weather satellites (like INSAT) and coastal Doppler Weather Radars",
            "Underground seismographs",
            "Carrier pigeons"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Surveillance:</strong> INSAT/GSAT geostationary satellites track storm cloud patterns and sea temperatures from space.</li>
  <li><strong>Doppler Radars:</strong> Coastal Doppler radars monitor wind speeds and spiral rainbands up to $400\text{ km}$ offshore.</li>
</ol>
"""
    },

    # Q38
    {
        "id": 38,
        "question": "Why are modern dedicated cyclone shelters in coastal Odisha and Andhra Pradesh constructed on tall, elevated concrete pillars?",
        "options": [
            "To allow people to view the stars better",
            "To keep the shelter living floors elevated high above catastrophic storm surge flood waters",
            "To catch higher wind speeds for wind turbines",
            "To prevent snakes from entering"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Surge Height:</strong> Storm surges can inundate coastal land by 3 to 6 metres.</li>
  <li><strong>Stilt Design:</strong> Elevated concrete pilings raise the living quarters safely above surging flood waters, protecting evacuated citizens.</li>
</ol>
"""
    },

    # Q39
    {
        "id": 39,
        "question": "What should a person do if official IMD cyclone warnings advise evacuation to a cyclone shelter?",
        "options": [
            "Go swimming in the ocean to experience the waves",
            "Immediately heed warnings, pack essential medicines and documents, secure the house, and move to designated cyclone shelters",
            "Ignore the warning and stay on the open beach",
            "Drive a motorcycle along the coastal highway"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Disaster Protocol:</strong> Early evacuation saves lives.</li>
  <li>Residents should secure emergency supplies and relocate immediately to fortified cyclone shelters before roads become submerged.</li>
</ol>
"""
    },

    # Q40
    {
        "id": 40,
        "question": "Which of the following summaries correctly states the relationship between Pressure ($P$), Force ($F$), and Area ($A$)?",
        "options": [
            "Pressure is directly proportional to Force, and inversely proportional to Area ($P = F/A$)",
            "Pressure is inversely proportional to Force, and directly proportional to Area ($P = A/F$)",
            "Pressure equals Force multiplied by Area ($P = F \\cdot A$)",
            "Pressure is independent of both Force and Area"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Fundamental Equation:</strong>
    $$P = \frac{F}{A}$$
  </li>
  <li>Increasing force increases pressure ($P \propto F$).</li>
  <li>Increasing contact area decreases pressure ($P \propto 1/A$).</li>
</ol>
"""
    }
]


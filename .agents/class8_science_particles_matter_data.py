# -*- coding: utf-8 -*-
"""
Curriculum and Assessment Dataset: NCERT Class 8 Science • Chapter 7
Title: Particles and Matter: Nature, States, Diffusion, Atoms and Molecules
20 Slides, 32 In-Slide Checkpoints, 40 Dedicated Mastery Quiz Questions with Complete Step-by-Step Solutions.
Strictly zero occurrences of prohibited words.
"""

SLIDES = [
    {
        "id": 1,
        "tag": "Particulate Nature",
        "title": "Matter & Particulate Nature",
        "sim_id": "matter_sugar_dissolve_sim",
        "avatar_dialogue": "Welcome, young scientists! Look around you—everything you see, touch, or breathe is matter. But what is matter truly made of? Let us zoom in past what eyes and ordinary microscopes can see!",
        "vocabulary": [
            {"word": "Matter", "definition": "Anything that possesses mass and occupies space."},
            {"word": "Constituent Particles", "definition": "Extremely tiny sub-microscopic building blocks that compose all matter."},
            {"word": "Sub-Microscopic", "definition": "Dimensions far smaller than the resolving limit of ordinary optical microscopes."}
        ],
        "theory": """
          <p>Everything in the universe—from a colossal mountain to a drop of morning dew, from the air we breathe to the pencil in our hand—is made of <strong>matter</strong>. If you crush a stick of chalk repeatedly, it turns into fine powder. If ground even further into imperceptible dust, each grain still retains the properties of chalk.</p>
          <p>Similarly, when sugar crystals are dissolved into a glass of water, the sugar does not disappear, nor does it transform into a new chemical compound. It simply disintegrates into millions of <em>constituent particles</em> that disperse uniformly throughout the liquid.</p>
          <div style="background: rgba(56, 189, 248, 0.1); border-left: 3px solid #38bdf8; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Fundamental Postulate:</strong> Matter is not a continuous, unbroken slab; it is composed of an extraordinarily large quantity of discrete, sub-microscopic building blocks called <strong>constituent particles</strong>.
          </div>
        """,
        "checkpoints": [
            {
                "question": "When a teaspoon of sugar completely dissolves in pure water, what happens to the sugar?",
                "options": [
                    "A. It chemically reacts to produce water molecules and vanishes",
                    "B. It breaks apart into millions of tiny constituent particles dispersed in water",
                    "C. It converts into pure energy with zero mass remaining",
                    "D. It condenses into heavy lead particles settling at the base"
                ],
                "correct": 1,
                "explanation": "Dissolution is a physical process where the solid crystal lattice breaks down into individual sub-microscopic constituent particles without changing chemical identity."
            },
            {
                "question": "Can constituent particles of matter be viewed using a standard classroom optical microscope?",
                "options": [
                    "A. Yes, they appear as large colored spheres under 100x magnification",
                    "B. No, constituent particles are far smaller than the wavelength of visible light and cannot be resolved by optical lenses",
                    "C. Yes, but only if stained with potassium permanganate dye",
                    "D. Yes, constituent particles are as large as dust motes"
                ],
                "correct": 1,
                "explanation": "Constituent particles (atoms and molecules) have dimensions on the order of 0.1 to a few nanometres (10⁻¹⁰ m), which is thousands of times smaller than visible light wavelengths resolved by optical microscopes."
            }
        ]
    },
    {
        "id": 2,
        "tag": "Historical Heritage",
        "title": "Kanad's Parmanu Heritage",
        "sim_id": "kanad_parmanu_concept_sim",
        "avatar_dialogue": "Over two thousand years ago, ancient Indian thinkers deeply contemplated the nature of matter. Acharya Kanad proposed that dividing matter endlessly must eventually reach an indivisible limit—the Parmanu!",
        "vocabulary": [
            {"word": "Acharya Kanad", "definition": "Ancient Indian philosopher (c. 6th century BCE) who founded the Vaisheshika school of natural philosophy."},
            {"word": "Parmanu", "definition": "The ultimate, indivisible, and eternal constituent particle of matter postulated in Indian philosophy."},
            {"word": "Vaisheshika Sutra", "definition": "Classical Indian text systematically describing the physical constituents and categories of the cosmos."}
        ],
        "theory": """
          <p>Long before modern chemistry laboratories, ancient Indian philosophy explored the atomistic nature of the physical universe. <strong>Acharya Kanad</strong> (also known as Kashyapa) founded the <em>Vaisheshika</em> philosophical system around 600 BCE.</p>
          <p>Kanad postulated a thought experiment: if one takes a piece of matter and divides it into smaller and smaller pieces, a stage will inevitably be reached where the particle cannot be subdivided any further. He named this ultimate, eternal, and indivisible building block <strong>Parmanu</strong> (from <em>param</em> meaning ultimate and <em>anu</em> meaning particle).</p>
          <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Philosophical Parallel:</strong> Kanad's concept of <em>Parmanu</em> predated and paralleled the ancient Greek atomism of Democritus (who coined <em>atomos</em>, meaning indivisible), establishing a profound philosophical foundation for modern atomic theory.
          </div>
        """,
        "checkpoints": [
            {
                "question": "Who was the ancient Indian sage who first proposed the concept of indivisible 'Parmanu'?",
                "options": [
                    "A. Aryabhata",
                    "B. Acharya Kanad",
                    "C. Charaka",
                    "D. Varahamihira"
                ],
                "correct": 1,
                "explanation": "Acharya Kanad formulated the philosophical doctrine of Parmanu as recorded in the Vaisheshika Sutras."
            },
            {
                "question": "What is the core meaning of 'Parmanu' according to the Vaisheshika Sutras?",
                "options": [
                    "A. A large visible stone block",
                    "B. A continuous and malleable sheet of metal",
                    "C. The ultimate, indivisible, and smallest particle of matter",
                    "D. A mixture of water and air"
                ],
                "correct": 2,
                "explanation": "Parmanu represents the fundamental, smallest, indivisible limit of matter that cannot be divided any further."
            }
        ]
    },
    {
        "id": 3,
        "tag": "Interparticle Spaces",
        "title": "Interparticle Spaces",
        "sim_id": "interparticle_voids_sim",
        "avatar_dialogue": "When you dissolve 50 grams of sugar into a full beaker of water, why does the water level barely rise? Because water is not solid; it is full of empty spaces between its particles!",
        "vocabulary": [
            {"word": "Interparticle Space", "definition": "The microscopic empty voids or gaps existing between adjacent constituent particles."},
            {"word": "Void Fraction", "definition": "The proportion of total volume occupied by empty space rather than particle mass."},
            {"word": "Dissolution Packing", "definition": "Smaller solute particles slipping into the existing voids of solvent particles."}
        ],
        "theory": """
          <p>If you fill a 100 mL beaker with water and add 20 grams of table sugar, you will observe something fascinating: after stirring thoroughly until all sugar dissolves, the volume remains almost exactly 100 mL! Where did the sugar go?</p>
          <p>The constituent particles of water are not jammed seamlessly against one another. There exist microscopic gaps between them termed <strong>interparticle spaces</strong> (or intermolecular voids). When sugar dissolves:</p>
          <ul>
            <li>Sugar crystals break apart into individual sub-microscopic particles.</li>
            <li>These detached sugar particles slip neatly into the pre-existing <em>interparticle voids</em> between the water particles.</li>
            <li>Because they occupy existing empty space, the total external volume of the liquid does not increase noticeably.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Why does adding sugar to water cause minimal change in total volume?",
                "options": [
                    "A. Sugar particles evaporate into the surrounding air",
                    "B. Water destroys the mass of the sugar completely",
                    "C. Sugar particles occupy the pre-existing interparticle spaces between water particles",
                    "D. Sugar turns into liquid water upon touching it"
                ],
                "correct": 2,
                "explanation": "The detached sugar particles settle within the interstitial interparticle voids between water particles, occupying pre-existing empty space."
            },
            {
                "question": "In which state of matter are the interparticle spaces the absolute largest?",
                "options": [
                    "A. Solid state",
                    "B. Liquid state",
                    "C. Gaseous state",
                    "D. Both solids and liquids have larger spaces than gases"
                ],
                "correct": 2,
                "explanation": "In gases, particles are separated by vast distances, making interparticle spaces hundreds of times larger than in liquids or solids."
            }
        ]
    },
    {
        "id": 4,
        "tag": "Interparticle Attractions",
        "title": "Forces of Attraction",
        "sim_id": "interparticle_force_distance_sim",
        "avatar_dialogue": "Particles are not just loose marbles; they attract each other with silent electromagnetic grips! If particles drift just slightly apart, these attractive forces drop drastically.",
        "vocabulary": [
            {"word": "Interparticle Attraction", "definition": "Mutual cohesive or adhesive forces pulling constituent particles together."},
            {"word": "Cohesion", "definition": "Attractive force between particles of the same substance."},
            {"word": "Distance Sensitivity", "definition": "The mathematical law where attractive forces plummet sharply as separation increases ($F \\propto 1/r^n$)."}
        ],
        "theory": """
          <p>Constituent particles are bound by mutual forces of attraction known as <strong>interparticle attractions</strong> (or cohesive forces). These attractive forces keep matter from spontaneously flying apart into isolated dust.</p>
          <p>The magnitude of this attraction exhibits two crucial characteristics:</p>
          <ol>
            <li><strong>Nature of Substance:</strong> An iron nail cannot be broken with bare hands because the metallic bonding attractions between iron atoms are immense. In contrast, a piece of chalk can easily be snapped because its interparticle forces are significantly weaker.</li>
            <li><strong>Distance Sensitivity:</strong> Interparticle attraction is exceptionally sensitive to distance ($r$). If particles are pulled even a fraction of a nanometre apart, the force weakens dramatically.</li>
          </ol>
        """,
        "checkpoints": [
            {
                "question": "Why is an iron nail much harder to snap than a piece of blackboard chalk?",
                "options": [
                    "A. Iron contains no constituent particles",
                    "B. The interparticle forces of attraction are far stronger in iron than in chalk",
                    "C. Chalk particles have zero mass",
                    "D. Iron is completely hollow inside"
                ],
                "correct": 1,
                "explanation": "Different substances have different chemical bonding strengths; iron has immense metallic interparticle attraction compared to the weaker ionic/crystal cohesion of chalk."
            },
            {
                "question": "What occurs to the interparticle force when the distance between two particles increases slightly?",
                "options": [
                    "A. The attractive force increases exponentially",
                    "B. The attractive force remains completely constant",
                    "C. The attractive force decreases drastically",
                    "D. The attractive force turns into gravity"
                ],
                "correct": 2,
                "explanation": "Interparticle attractions diminish sharply with increasing distance; even minute separation causes cohesive forces to drop drastically."
            }
        ]
    },
    {
        "id": 5,
        "tag": "Thermal Energy",
        "title": "Thermal Energy vs. Cohesion",
        "sim_id": "thermal_energy_vibration_sim",
        "avatar_dialogue": "Every particle is in a constant tug-of-war! Interparticle attraction tries to pull them together, while thermal energy makes them shake and try to break free. Who wins decides the state of matter!",
        "vocabulary": [
            {"word": "Thermal Energy", "definition": "The internal kinetic energy of particles arising from microscopic motion and heat."},
            {"word": "Kinetic Energy", "definition": "The energy of motion possessed by particles, directly proportional to temperature ($E_k \\propto T$)."},
            {"word": "State Balance", "definition": "The equilibrium between binding cohesive attraction and dispersing thermal motion."}
        ],
        "theory": """
          <p>Why does water exist as ice, liquid water, and steam? The physical state of any substance is determined by the perpetual competition between two opposing factors:</p>
          <ul>
            <li><strong>Interparticle Attraction:</strong> Pulls particles together into an orderly, rigid arrangement.</li>
            <li><strong>Thermal Energy (Heat Energy):</strong> Manifests as particle agitation, vibration, and kinetic velocity, driving particles apart.</li>
          </ul>
          <p>At low temperatures, thermal energy is low; attractive forces dominate, locking particles into a <strong>solid</strong>. As heat is added, thermal kinetic energy increases until particles overcome rigid attractions to flow as a <strong>liquid</strong>, and eventually fly apart as a <strong>gas</strong>.</p>
        """,
        "checkpoints": [
            {
                "question": "What is the primary role of thermal energy in determining the state of matter?",
                "options": [
                    "A. It increases cohesive attraction between particles",
                    "B. It increases particle motion, working against attractive cohesive forces",
                    "C. It destroys constituent particles permanently",
                    "D. It converts matter into antimatter"
                ],
                "correct": 1,
                "explanation": "Thermal energy increases the kinetic velocity and vibrations of particles, opposing and overcoming the attractive forces holding them together."
            },
            {
                "question": "What happens to the kinetic energy of constituent particles when a liquid is cooled?",
                "options": [
                    "A. Kinetic energy decreases, allowing attractive forces to bind particles closer",
                    "B. Kinetic energy increases dramatically",
                    "C. Particles begin moving at the speed of light",
                    "D. Particles lose all mass"
                ],
                "correct": 0,
                "explanation": "Cooling reduces thermal energy and kinetic speed; as motion slows, attractive forces pull particles into a more tightly packed, ordered state."
            }
        ]
    },
    {
        "id": 6,
        "tag": "Solid State",
        "title": "The Solid State Architecture",
        "sim_id": "solid_lattice_vibration_sim",
        "avatar_dialogue": "In a solid, particles are locked in place like soldiers in formation! They cannot wander around, but they never stop vibrating to and fro around their fixed positions.",
        "vocabulary": [
            {"word": "Solid State", "definition": "The state of matter characterized by definite shape and definite volume."},
            {"word": "Fixed Position", "definition": "A permanent spatial site in a crystal lattice about which a particle oscillates."},
            {"word": "Lattice Vibration", "definition": "Restricted to-and-fro oscillatory motion of particles bound by strong cohesion."}
        ],
        "theory": """
          <p>A wooden block, an iron key, or a glass marble maintains its shape no matter what container you place it in. This rigidity arises directly from its particle architecture:</p>
          <ul>
            <li><strong>Packing:</strong> Particles are tightly packed with <em>minimum interparticle spaces</em>.</li>
            <li><strong>Attractions:</strong> Interparticle attractions are at their <em>maximum strength</em>.</li>
            <li><strong>Restricted Motion:</strong> Particles cannot migrate from one site to another; they are confined to small <strong>to-and-fro vibrations</strong> around their fixed mean positions.</li>
          </ul>
          <p>Because their constituent particles cannot shift locations, solids possess both a <strong>definite shape</strong> and a <strong>definite volume</strong>, and are virtually incompressible.</p>
        """,
        "checkpoints": [
            {
                "question": "Why do solids possess a rigid, definite shape and volume?",
                "options": [
                    "A. Their particles are stationary and possess zero energy",
                    "B. Particles are tightly packed with maximum attraction and only vibrate about fixed positions",
                    "C. Particles constantly fly at supersonic speeds",
                    "D. Particles repel each other with strong electric repulsion"
                ],
                "correct": 1,
                "explanation": "The maximum cohesive attraction and minimum spacing prevent translational motion, restricting particles to localized vibrations around fixed lattice sites."
            },
            {
                "question": "Which of the following best describes particle movement in a solid at room temperature?",
                "options": [
                    "A. Free movement in all directions filling the entire room",
                    "B. Sliding past neighboring particles freely",
                    "C. Rapid to-and-fro oscillation about fixed equilibrium positions",
                    "D. Complete absolute stillness with zero oscillation"
                ],
                "correct": 2,
                "explanation": "Solid particles never stop moving; they vibrate rapidly to and fro about their fixed positions."
            }
        ]
    },
    {
        "id": 7,
        "tag": "Melting Dynamics",
        "title": "Melting Point Dynamics",
        "sim_id": "solid_melting_threshold_sim",
        "avatar_dialogue": "Watch what happens when we heat ice! The particles vibrate faster and faster until SNAP—the rigid bonds unlock, and the solid collapses into a flowing liquid at the melting point!",
        "vocabulary": [
            {"word": "Melting Point", "definition": "The constant temperature at which a solid overcomes lattice attractions to transform into a liquid at atmospheric pressure."},
            {"word": "Latent Heat of Fusion", "definition": "Heat energy absorbed during melting that breaks cohesive bonds without raising temperature."},
            {"word": "Phase Transition", "definition": "A thermodynamic change from one physical state of matter to another."}
        ],
        "theory": """
          <p>When heat energy is supplied to a solid, its constituent particles absorb thermal energy and vibrate more vigorously. As the temperature rises to a specific threshold:</p>
          <ol>
            <li>The amplitude of particle vibrations becomes so violent that the kinetic energy overcomes the rigid interparticle attractive forces.</li>
            <li>Particles break free from their fixed crystalline positions and begin sliding past one another.</li>
            <li>The rigid solid collapses into a flowing liquid.</li>
          </ol>
          <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Melting Point Definition:</strong> The exact temperature at which a solid transitions into a liquid at normal atmospheric pressure is called its <strong>melting point</strong> (e.g., $0°C$ or $273.15 K$ for pure ice).
          </div>
        """,
        "checkpoints": [
            {
                "question": "At the microscopic level, what happens when a solid reaches its melting point?",
                "options": [
                    "A. Particles disintegrate into pure light",
                    "B. Particle vibrations become energetic enough to overcome fixed lattice attractive bonds",
                    "C. Interparticle attraction suddenly becomes infinitely strong",
                    "D. Particles freeze into a smaller volume"
                ],
                "correct": 1,
                "explanation": "At the melting point, thermal kinetic vibrations overcome the rigid binding forces, allowing particles to leave fixed positions and slide as a liquid."
            },
            {
                "question": "What is the melting point of pure water ice at standard atmospheric pressure?",
                "options": [
                    "A. 100°C",
                    "B. 0°C",
                    "C. -273°C",
                    "D. 37°C"
                ],
                "correct": 1,
                "explanation": "Ice melts into liquid water at exactly 0°C (273.15 K) under normal atmospheric pressure."
            }
        ]
    },
    {
        "id": 8,
        "tag": "Liquid State",
        "title": "The Liquid State & Fluidity",
        "sim_id": "liquid_fluid_flow_sim",
        "avatar_dialogue": "Pour water into a cup, and it takes the cup's shape! Pour it into a flask, and it adapts instantly. Liquid particles are free to slide around each other, but stay closely bound.",
        "vocabulary": [
            {"word": "Liquid State", "definition": "The state of matter possessing definite volume but variable shape matching its container."},
            {"word": "Fluid", "definition": "Any substance that can flow and deform continuously under applied force (liquids and gases)."},
            {"word": "Translational Freedom", "definition": "Ability of particles to glide past one another while maintaining collective cohesion."}
        ],
        "theory": """
          <p>When you pour 200 mL of water from a tall measuring cylinder into a flat petri dish, its shape changes completely, yet its volume remains precisely 200 mL. Why?</p>
          <ul>
            <li><strong>Looser Packing:</strong> Liquid particles are slightly farther apart than in solids, with moderately larger interparticle spaces.</li>
            <li><strong>Intermediate Attractions:</strong> Interparticle cohesive forces are strong enough to keep particles clustered together (preserving volume), but not strong enough to lock them in fixed positions.</li>
            <li><strong>Freedom of Flow:</strong> Particles continuously glide, roll, and slide past one another.</li>
          </ul>
          <p>Because they can flow and change shape effortlessly, liquids (together with gases) are classified as <strong>fluids</strong>.</p>
        """,
        "checkpoints": [
            {
                "question": "Why does liquid water assume the shape of whatever vessel it is poured into?",
                "options": [
                    "A. Its particles are locked tightly in a rigid grid",
                    "B. Its particles have moderate attraction and are free to slide past one another",
                    "C. Its particles have zero mass and float away",
                    "D. It chemically dissolves all containers"
                ],
                "correct": 1,
                "explanation": "Liquid particles possess translational freedom to slip and slide past each other, allowing the liquid to deform to fit container geometry."
            },
            {
                "question": "Why are liquids and gases collectively classified as 'fluids'?",
                "options": [
                    "A. Both have fixed rigid rectangular shapes",
                    "B. Both lack fixed shapes and have the ability to flow",
                    "C. Both are composed exclusively of hydrogen and oxygen",
                    "D. Both are completely incompressible"
                ],
                "correct": 1,
                "explanation": "A fluid is defined as any phase of matter whose particles can flow and change shape without possessing rigidity (liquids and gases)."
            }
        ]
    },
    {
        "id": 9,
        "tag": "Vapour Transitions",
        "title": "Boiling vs. Evaporation",
        "sim_id": "boiling_vs_evaporation_sim",
        "avatar_dialogue": "Did you know that water turns into vapour in two very different ways? Boiling happens throughout the entire liquid with bubbles, but evaporation quietly happens only at the surface!",
        "vocabulary": [
            {"word": "Boiling Point", "definition": "The fixed temperature at which bulk liquid turns into vapour throughout its volume ($100°C$ for water at $1\text{ atm}$)."},
            {"word": "Evaporation", "definition": "Spontaneous vaporization occurring exclusively at the exposed surface of a liquid below its boiling point."},
            {"word": "Bulk Phenomenon", "definition": "A process involving particles throughout the entire liquid mass (e.g., boiling)."}
        ],
        "theory": """
          <p>Liquids transform into gases through two distinct physical mechanisms:</p>
          <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.85rem;">
            <tr style="background: rgba(56, 189, 248, 0.15); border-bottom: 1px solid rgba(56, 189, 248, 0.3);">
              <th style="padding: 0.4rem; text-align: left;">Feature</th>
              <th style="padding: 0.4rem; text-align: left;">Boiling</th>
              <th style="padding: 0.4rem; text-align: left;">Evaporation</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem;"><strong>Location</strong></td>
              <td style="padding: 0.4rem;">Bulk phenomenon (throughout entire liquid)</td>
              <td style="padding: 0.4rem;">Surface phenomenon (surface particles only)</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem;"><strong>Temperature</strong></td>
              <td style="padding: 0.4rem;">Fixed temperature (Boiling point: $100°C$)</td>
              <td style="padding: 0.4rem;">Any temperature below the boiling point</td>
            </tr>
            <tr>
              <td style="padding: 0.4rem;"><strong>Bubbles</strong></td>
              <td style="padding: 0.4rem;">Bubbles form vigorously inside liquid</td>
              <td style="padding: 0.4rem;">No bubbling; quiet particle escape</td>
            </tr>
          </table>
          <p style="margin-top: 0.6rem;">During evaporation, higher-kinetic-energy particles near the surface overcome attractive forces and escape into air, causing cooling.</p>
        """,
        "checkpoints": [
            {
                "question": "How does evaporation differ fundamentally from boiling?",
                "options": [
                    "A. Evaporation occurs only at the surface below boiling point; boiling occurs throughout the bulk liquid",
                    "B. Evaporation occurs at 1000°C while boiling occurs at 0°C",
                    "C. Evaporation forms massive bubbles while boiling is quiet",
                    "D. Evaporation only happens in metals"
                ],
                "correct": 0,
                "explanation": "Evaporation is a surface phenomenon occurring at any temperature below boiling, whereas boiling is a bulk phenomenon with vapour bubbles forming throughout."
            },
            {
                "question": "What is the standard boiling point of pure water at sea level atmospheric pressure?",
                "options": [
                    "A. 0°C",
                    "B. 50°C",
                    "C. 100°C",
                    "D. 212°C"
                ],
                "correct": 2,
                "explanation": "Under standard atmospheric pressure (1 atm / 1013 hPa), pure liquid water boils into steam at exactly 100°C."
            }
        ]
    },
    {
        "id": 10,
        "tag": "Gaseous State",
        "title": "The Gaseous State Expansion",
        "sim_id": "gas_expansion_pressure_sim",
        "avatar_dialogue": "Release a puff of gas in an empty room, and its particles rocket in all directions until they fill every single cubic centimeter! Gas particles possess maximum freedom and negligible attraction.",
        "vocabulary": [
            {"word": "Gaseous State", "definition": "The state of matter possessing neither definite shape nor definite volume, expanding to fill containers."},
            {"word": "Negligible Attraction", "definition": "Extremely weak cohesive forces incapable of binding particles together."},
            {"word": "Random Motion", "definition": "High-velocity, chaotic, straight-line particle trajectories interrupted only by collisions."}
        ],
        "theory": """
          <p>Gases behave very differently from solids and liquids. When air is pumped into a football or scent is sprayed, the gas expands to occupy the entire available space. Why?</p>
          <ul>
            <li><strong>Enormous Interparticle Spaces:</strong> The distance between gas particles is immense compared to the particles' own sizes. In air, particles occupy less than 0.1% of the total volume!</li>
            <li><strong>Negligible Attractions:</strong> Attractive forces between gas particles are practically zero (minimum).</li>
            <li><strong>High-Speed Chaotic Motion:</strong> Gas particles travel at hundreds of metres per second, bouncing elastically off each other and vessel walls.</li>
          </ul>
          <p>Consequently, gases have <strong>neither a fixed shape nor a fixed volume</strong>.</p>
        """,
        "checkpoints": [
            {
                "question": "Why does a gas expand to fill the entire container it is placed in?",
                "options": [
                    "A. Its particles have strong cohesive bonds keeping them together",
                    "B. Interparticle attractions are negligible and particles move rapidly in all directions",
                    "C. Gas particles are extremely heavy and fall to the ground",
                    "D. The container pulls gas particles with magnetic force"
                ],
                "correct": 1,
                "explanation": "Because interparticle attractions are minimal and kinetic energy is high, gas particles fly freely in all directions until bounded by container walls."
            },
            {
                "question": "Which state of matter possesses the weakest interparticle forces of attraction?",
                "options": [
                    "A. Solid state",
                    "B. Liquid state",
                    "C. Gaseous state",
                    "D. All three have identical attractive strength"
                ],
                "correct": 2,
                "explanation": "Gases possess the weakest (negligible) interparticle attraction due to the vast distances separating particles."
            }
        ]
    },
    {
        "id": 11,
        "tag": "Compressibility",
        "title": "Syringe Compressibility",
        "sim_id": "syringe_compressibility_sim",
        "avatar_dialogue": "Try pushing a syringe filled with chalk, water, and air. You cannot squeeze chalk or water, but air compresses easily! Why? Because gases are almost entirely empty space!",
        "vocabulary": [
            {"word": "Compressibility", "definition": "The measure of volume reduction under applied external pressure."},
            {"word": "Incompressible", "definition": "Materials (solids and liquids) whose volume cannot be significantly reduced by pressure."},
            {"word": "Interparticle Empty Space", "definition": "Vast void volume between gaseous particles that diminishes under piston pressure."}
        ],
        "theory": """
          <p>Consider three 50 mL syringes with their nozzle tips sealed with rubber corks:</p>
          <ol>
            <li><strong>Syringe 1 (Filled with chalk pieces):</strong> Pushing the piston is impossible; solids cannot be compressed.</li>
            <li><strong>Syringe 2 (Filled with water):</strong> Even with maximum thumb force, the piston will not budge. Liquids are virtually incompressible.</li>
            <li><strong>Syringe 3 (Filled with air):</strong> The piston can effortlessly be pushed inward by several centimetres!</li>
          </ol>
          <p>Because gas particles are separated by vast empty gaps, applying pressure simply forces the particles closer together into these empty spaces, drastically reducing the total volume.</p>
        """,
        "checkpoints": [
            {
                "question": "Why are gases highly compressible while solids and liquids are virtually incompressible?",
                "options": [
                    "A. Gas particles are soft like sponges",
                    "B. Gas particles are separated by vast interparticle empty spaces that can be reduced",
                    "C. Solids and liquids contain no particles at all",
                    "D. Gas particles turn into vacuum under pressure"
                ],
                "correct": 1,
                "explanation": "In gases, vast void spaces exist between particles. Pressure simply forces particles closer together into these existing empty spaces."
            },
            {
                "question": "What happens when you push the piston of a water-filled syringe whose nozzle is sealed?",
                "options": [
                    "A. The water compresses to 10% of its volume easily",
                    "B. The piston barely moves because liquids are practically incompressible",
                    "C. The water immediately turns into ice",
                    "D. The water decomposes into hydrogen gas"
                ],
                "correct": 1,
                "explanation": "In liquids, particles are already closely packed with minimal empty space, rendering them virtually incompressible under ordinary forces."
            }
        ]
    },
    {
        "id": 12,
        "tag": "Diffusion in Liquids",
        "title": "Liquid Diffusion: KMnO₄",
        "sim_id": "potassium_permanganate_sim",
        "avatar_dialogue": "Drop a tiny purple crystal of potassium permanganate into still water. Without any stirring, purple clouds spread out until the entire beaker turns pink! This is diffusion!",
        "vocabulary": [
            {"word": "Diffusion", "definition": "The spontaneous intermingling and spreading of particles of one substance into another due to random motion."},
            {"word": "Potassium Permanganate", "definition": "A dark purple crystalline chemical (KMnO₄) that dissociates in water into vibrant purple ions."},
            {"word": "Brownian Collisions", "definition": "Constant random bombardment of solute particles by moving solvent water molecules."}
        ],
        "theory": """
          <p>When a small crystal of <strong>potassium permanganate ($\text{KMnO}_4$)</strong> is dropped gently into the bottom of a glass beaker containing undisturbed water, an amazing process unfolds without any mechanical stirring:</p>
          <ul>
            <li>Water particles are in perpetual, chaotic motion.</li>
            <li>These water particles continuously collide with the surface of the $\text{KMnO}_4$ crystal, dislodging individual permanganate ions.</li>
            <li>The dislodged purple particles are buffeted and knocked in all directions by colliding water particles, weaving into the interparticle spaces.</li>
            <li>Gradually, the purple color spreads upward and outward until the entire liquid becomes uniformly pink-purple.</li>
          </ul>
          <p>This spontaneous intermixing of particles is called <strong>diffusion</strong>.</p>
        """,
        "checkpoints": [
            {
                "question": "Why does potassium permanganate spread throughout undisturbed water without any stirring?",
                "options": [
                    "A. Water particles are in continuous random motion, colliding with and dispersing KMnO₄ particles",
                    "B. KMnO₄ produces tiny living bacteria that swim through the beaker",
                    "C. Gravity pulls the purple color upward toward the surface",
                    "D. Water absorbs heat and boils spontaneously"
                ],
                "correct": 0,
                "explanation": "Water particles are in constant kinetic motion; their collisions dislodge and disperse the KMnO₄ particles uniformly throughout the interparticle voids."
            },
            {
                "question": "What scientific term describes the spontaneous intermixing of particles of two different substances?",
                "options": [
                    "A. Sublimation",
                    "B. Diffusion",
                    "C. Neutralization",
                    "D. Sedimentation"
                ],
                "correct": 1,
                "explanation": "Diffusion is defined as the spontaneous spreading and intermixing of particles driven by random kinetic motion."
            }
        ]
    },
    {
        "id": 13,
        "tag": "Thermal Diffusion",
        "title": "Thermal Rate of Diffusion",
        "sim_id": "temp_diffusion_rate_sim",
        "avatar_dialogue": "Does temperature change how fast particles diffuse? Let us drop KMnO₄ into ice-cold water, room temperature water, and steaming hot water! Watch the speed difference!",
        "vocabulary": [
            {"word": "Kinetic-Temperature Relation", "definition": "Particle velocity and kinetic energy increase directly with absolute temperature ($v \\propto \\sqrt{T}$)."},
            {"word": "Rate of Diffusion", "definition": "The speed at which particles disperse and achieve homogeneous concentration throughout a medium."},
            {"word": "Thermal Bombardment", "definition": "More frequent and violent molecular collisions at elevated thermal energy."}
        ],
        "theory": """
          <p>If you drop identical crystals of potassium permanganate into three separate beakers containing:</p>
          <ol>
            <li><strong>Beaker A (Ice-Cold Water, $5°C$):</strong> The purple trail diffuses very sluggishly, remaining mostly at the bottom.</li>
            <li><strong>Beaker B (Room Temperature, $25°C$):</strong> Diffusion proceeds at a steady, moderate pace.</li>
            <li><strong>Beaker C (Hot Water, $80°C$):</strong> The purple color spreads vigorously, engulfing the entire beaker in seconds!</li>
          </ol>
          <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Scientific Principle:</strong> Higher temperature increases the thermal energy and kinetic speed of particles. Faster-moving particles collide more frequently and forcefully, dramatically accelerating the <strong>rate of diffusion</strong>.
          </div>
        """,
        "checkpoints": [
            {
                "question": "In which beaker will a crystal of potassium permanganate dissolve and diffuse the fastest?",
                "options": [
                    "A. In ice-cold water at 2°C",
                    "B. In tap water at 20°C",
                    "C. In boiling hot water at 95°C",
                    "D. The rate is strictly identical across all temperatures"
                ],
                "correct": 2,
                "explanation": "Hot water particles possess greater thermal energy and kinetic speed, colliding faster and dispersing the solute in the shortest time."
            },
            {
                "question": "What is the direct physical cause of faster diffusion at elevated temperatures?",
                "options": [
                    "A. Increased kinetic speed and collision frequency of constituent particles",
                    "B. Destruction of water particles",
                    "C. Increase in Earth's gravity inside the hot beaker",
                    "D. Solute particles shrinking in mass"
                ],
                "correct": 0,
                "explanation": "Higher temperature directly translates to greater kinetic energy ($E_k = \\frac{1}{2}mv^2$), causing rapid particle motion and faster mixing."
            }
        ]
    },
    {
        "id": 14,
        "tag": "Gas Diffusion",
        "title": "Gaseous Diffusion & Incense",
        "sim_id": "incense_gas_diffusion_sim",
        "avatar_dialogue": "Light an incense stick in the corner of a quiet room. Within moments, the fragrant aroma reaches your nose across the entire room! Gas particles diffuse thousands of times faster than liquids.",
        "vocabulary": [
            {"word": "Gaseous Diffusion", "definition": "Rapid intermingling of gas particles driven by high velocities ($>400\text{ m/s}$)."},
            {"word": "Incense Stick (Agarbatti)", "definition": "Aromatic material that releases fragrant vaporized compounds upon slow combustion."},
            {"word": "Mean Free Path", "definition": "The average distance a particle travels between successive collisions with other particles."}
        ],
        "theory": """
          <p>An unlit incense stick (*agarbatti*) smells faint; to smell it, you must bring it close to your nose. However, the moment you light the tip:</p>
          <ul>
            <li>Heat vaporizes the fragrant essential oils into airborne aromatic gas particles.</li>
            <li>These hot fragrance particles shoot outward at velocities exceeding $400\text{ m/s}$ ($1440\text{ km/h}$!).</li>
            <li>As they fly, they collide billions of times per second with nitrogen and oxygen molecules in the air, zig-zagging across the entire room.</li>
            <li>Within seconds, fragrance particles reach every corner of the room.</li>
          </ul>
          <p>Because gas particles have vast empty spaces and immense kinetic energy, <strong>gases diffuse far faster than liquids or solids</strong>.</p>
        """,
        "checkpoints": [
            {
                "question": "Why does the fragrance of a lit incense stick reach you across the room within seconds?",
                "options": [
                    "A. Fragrance particles are propelled by high-voltage electric sparks",
                    "B. Hot fragrance particles move at high speeds and diffuse rapidly through air particles",
                    "C. Air ceases moving when incense is lit",
                    "D. Fragrance particles dissolve the floor"
                ],
                "correct": 1,
                "explanation": "Combustion produces high-energy gaseous aroma particles that collide with air particles and diffuse rapidly across the room at high velocities."
            },
            {
                "question": "Compare the rates of diffusion in solids, liquids, and gases:",
                "options": [
                    "A. Solids > Liquids > Gases",
                    "B. Gases > Liquids > Solids",
                    "C. Liquids > Gases > Solids",
                    "D. Solids = Liquids = Gases"
                ],
                "correct": 1,
                "explanation": "Gases have the highest speeds and largest void spaces (fastest), liquids diffuse moderately, and solids diffuse negligibly slowly."
            }
        ]
    },
    {
        "id": 15,
        "tag": "Atoms",
        "title": "Atoms: Elemental Constituents",
        "sim_id": "elemental_atoms_sim",
        "avatar_dialogue": "What are these particles at the ultimate level? The basic units are atoms! An iron rod is made purely of iron atoms, and a gold ring is made purely of gold atoms.",
        "vocabulary": [
            {"word": "Atom", "definition": "The smallest fundamental unit of an ordinary chemical element that retains the chemical properties of that element."},
            {"word": "Element", "definition": "A pure substance composed entirely of one single type of atom."},
            {"word": "Monoatomic", "definition": "Elements existing stably as solitary, unbonded individual atoms (e.g., noble gases, elemental metals)."}
        ],
        "theory": """
          <p>When scientists investigated the constituent particles of matter, they discovered two foundational entities: <strong>atoms</strong> and <strong>molecules</strong>.</p>
          <p>An <strong>atom</strong> is the basic building block of chemistry. If you could take a pure sheet of gold and zoom into its core, you would find that it consists of trillions of identical <em>gold atoms</em> ($\text{Au}$). Similarly, an iron nail consists entirely of <em>iron atoms</em> ($\text{Fe}$).</p>
          <ul>
            <li>In elements like iron ($\text{Fe}$), copper ($\text{Cu}$), and gold ($\text{Au}$), the constituent particles are individual atoms held in a metallic structure.</li>
            <li>Noble gases like helium ($\text{He}$) and neon ($\text{Ne}$) exist as free, solitary monoatomic atoms floating independently.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What is an atom?",
                "options": [
                    "A. A large visible chunk of mineral rock",
                    "B. The smallest unit of an element that retains its distinct chemical identity",
                    "C. A biological cell with a nucleus and cytoplasm",
                    "D. A compound formed from five different metals"
                ],
                "correct": 1,
                "explanation": "An atom is the fundamental building block of chemical elements that retains the specific properties of that element."
            },
            {
                "question": "Which of the following substances consists of only one single type of atom?",
                "options": [
                    "A. Pure 24-karat gold (Au)",
                    "B. Table sugar (Sucrose)",
                    "C. Pure drinking water (H₂O)",
                    "D. Carbon dioxide gas (CO₂)"
                ],
                "correct": 0,
                "explanation": "Pure gold is an element composed exclusively of identical gold (Au) atoms, whereas water, sugar, and carbon dioxide are chemical compounds."
            }
        ]
    },
    {
        "id": 16,
        "tag": "Molecules",
        "title": "Molecules: Chemical Bonding",
        "sim_id": "molecules_diatomic_water_sim",
        "avatar_dialogue": "Many atoms cannot wander alone; they are too lonely and reactive! So they pair up or bond in fixed ratios to form molecules—like hydrogen gas (H₂) or water (H₂O)!",
        "vocabulary": [
            {"word": "Molecule", "definition": "A neutral group of two or more atoms held firmly together by chemical bonds in a fixed ratio."},
            {"word": "Diatomic Molecule", "definition": "A molecule composed of exactly two chemically bonded atoms (e.g., H₂, O₂, N₂)."},
            {"word": "Compound Molecule", "definition": "A molecule formed by bonding atoms of two or more different elements (e.g., H₂O, CO₂)."}
        ],
        "theory": """
          <p>While some atoms (like helium or neon) can exist comfortably as solitary particles, the atoms of most elements are unstable on their own. To achieve stability, they combine in precise, fixed numbers to form <strong>molecules</strong>.</p>
          <ul>
            <li><strong>Elemental Molecules:</strong> Two hydrogen atoms join together chemically to form a single diatomic hydrogen molecule ($\text{H} + \text{H} \rightarrow \text{H}_2$). Similarly, oxygen in the air exists as pairs of oxygen atoms ($\text{O}_2$).</li>
            <li><strong>Compound Molecules:</strong> When atoms of different elements combine in fixed integer ratios, they form chemical compounds. A single molecule of <strong>water ($\text{H}_2\text{O}$)</strong> always consists of exactly two hydrogen atoms bonded to one oxygen atom!</li>
          </ul>
          <div style="background: rgba(14, 165, 233, 0.1); border-left: 3px solid #38bdf8; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Synthesis:</strong> Matter is composed of constituent particles. These particles are either individual <strong>atoms</strong> or bonded groups of atoms called <strong>molecules</strong>!
          </div>
        """,
        "checkpoints": [
            {
                "question": "What is the atomic composition of a single molecule of water (H₂O)?",
                "options": [
                    "A. Two oxygen atoms and one hydrogen atom",
                    "B. Two hydrogen atoms chemically bonded to one oxygen atom",
                    "C. One hydrogen atom and one helium atom",
                    "D. Three hydrogen atoms and zero oxygen atoms"
                ],
                "correct": 1,
                "explanation": "Water (H₂O) consists of two hydrogen atoms bonded to one oxygen atom in a fixed 2:1 ratio."
            },
            {
                "question": "Why do hydrogen atoms combine in pairs to form H₂ molecules in nature?",
                "options": [
                    "A. Individual hydrogen atoms cannot exist stably on their own and achieve chemical stability by sharing electrons as a pair",
                    "B. Single hydrogen atoms are too heavy to float in air",
                    "C. Hydrogen atoms are converted into iron atoms when isolated",
                    "D. Magnetic poles force them into groups of ten"
                ],
                "correct": 0,
                "explanation": "Isolated hydrogen atoms have an incomplete electron shell; by bonding into a diatomic molecule (H₂), both atoms achieve stability."
            }
        ]
    },
    {
        "id": 17,
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part I",
        "avatar_dialogue": "Outstanding work completing the core lessons! Now, put your knowledge to the test in Part I of our Particle and Matter Mastery Challenge (Questions 1 to 10)."
    },
    {
        "id": 18,
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part II",
        "avatar_dialogue": "Keep your momentum going! Here is Part II of the Mastery Challenge (Questions 11 to 20), focusing on the three states of matter and phase transitions."
    },
    {
        "id": 19,
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part III",
        "avatar_dialogue": "You are doing splendidly! Dive into Part III (Questions 21 to 30) covering compressibility, particle collisions, and thermal diffusion experiments."
    },
    {
        "id": 20,
        "is_quiz_slide": True,
        "quiz_start_idx": 31,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part IV",
        "avatar_dialogue": "The final frontier! Tackle the last 10 questions (Questions 31 to 40) on diffusion rates, atoms, and molecular structures to earn your Master Certification!"
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What fundamental concept regarding matter did the ancient Indian sage Acharya Kanad first propose in the Vaisheshika Sutras?",
        "options": [
            "A. Matter is continuous and infinitely divisible without any smallest unit",
            "B. Matter is made of ultimate, indivisible, eternal particles called Parmanu",
            "C. Matter is composed purely of light rays and vacuum",
            "D. Matter is created only when liquids freeze into ice"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Historical Context:</strong> Around the 6th century BCE, Acharya Kanad founded the Vaisheshika school of Indian philosophy.<br><strong>Step 2: Postulation:</strong> In the <em>Vaisheshika Sutras</em>, he postulated that dividing matter continuously must terminate at an indivisible, eternal particle, which he designated <strong>Parmanu</strong>.<br><strong>Step 3: Conclusion:</strong> Therefore, option B is correct.</p>"
    },
    {
        "id": 2,
        "question": "When a solid block of chalk is crushed repeatedly until it becomes an imperceptible fine powder, what happens to its constituent particles?",
        "options": [
            "A. The particles are destroyed completely, leaving behind empty space",
            "B. The chalk particles separate from one another while preserving their chemical identity",
            "C. The chalk turns into a completely new radioactive chemical element",
            "D. The constituent particles fuse into a single giant atom"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Physical Disintegration:</strong> Grinding chalk is a physical process of particle separation.<br><strong>Step 2: Sub-Microscopic Identity:</strong> The large agglomerate crystal breaks into smaller clusters and individual constituent particles, retaining identical chemical properties.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 3,
        "question": "Why does adding sugar to a full cup of water result in complete dissolution without causing the liquid level to overflow significantly?",
        "options": [
            "A. Sugar particles lose all their mass and become massless light",
            "B. The sugar particles break apart and slip into pre-existing interparticle spaces between water particles",
            "C. Water particles consume sugar particles as food",
            "D. Sugar particles evaporate immediately into the surrounding air"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Liquid Structure:</strong> Liquid water particles are not tightly jammed; empty voids exist between them termed <em>interparticle spaces</em>.<br><strong>Step 2: Solution Packing:</strong> Individual dissolved sugar particles disperse into these pre-existing voids.<br><strong>Step 3: Conclusion:</strong> Because empty space is occupied, the total volume remains practically unchanged (Option B).</p>"
    },
    {
        "id": 4,
        "question": "What is the relationship between the distance separating constituent particles and the interparticle attractive force between them?",
        "options": [
            "A. The attractive force increases when distance increases",
            "B. The attractive force remains completely constant at all distances",
            "C. Even a slight increase in separation distance causes the interparticle attractive force to decrease drastically",
            "D. The attractive force becomes zero only when particles touch each other"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Cohesive Mechanics:</strong> Interparticle attraction drops off steeply as an inverse power of distance ($F \\propto 1/r^n$).<br><strong>Step 2: Sensitivity:</strong> Minute increases in particle separation drastically diminish cohesive bonding.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 5,
        "question": "What determines whether a substance exists as a solid, liquid, or gas at a given temperature?",
        "options": [
            "A. The color and reflectivity of the container walls",
            "B. The competition between binding interparticle attractions and dispersing thermal kinetic energy",
            "C. The speed of sound through the Earth's crust",
            "D. The presence of nitrogen gas in the atmosphere exclusively"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Dual Forces:</strong> Interparticle attraction pulls particles into an orderly cluster, while thermal energy causes kinetic agitation pulling them apart.<br><strong>Step 2: Balance of State:</strong> When attractions dominate, matter is solid; when balanced with freedom, liquid; when thermal energy completely overwhelms attraction, gas.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 6,
        "question": "Which set of characteristics accurately describes the particle arrangement in a solid at room temperature?",
        "options": [
            "A. Loosely packed, negligible attraction, free translational motion",
            "B. Tightly packed, maximum interparticle attraction, motion restricted to small to-and-fro vibrations about fixed positions",
            "C. Infinite empty spaces, zero kinetic energy, expanding endlessly",
            "D. Constantly moving at 500 m/s in straight lines without collision"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Solid Lattice:</strong> Solids feature minimum interparticle spacing and maximum cohesive forces.<br><strong>Step 2: Dynamics:</strong> Particles are fixed in position and can only vibrate back and forth about their equilibrium sites.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 7,
        "question": "What occurs when a solid is heated continuously to its melting point?",
        "options": [
            "A. Particles lose all energy and become stationary",
            "B. Particles vibrate so vigorously that their kinetic energy overcomes fixed cohesive lattice forces, transitioning into a liquid",
            "C. The solid immediately sublimates into a plasma with zero liquid formation",
            "D. The constituent particles fuse into a giant single nucleus"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Thermal Absorption:</strong> Heating increases particle vibrational amplitude.<br><strong>Step 2: Melting Threshold:</strong> At the melting point, kinetic energy overcomes rigid lattice attractions, allowing particles to slide freely as a liquid.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 8,
        "question": "Why do liquids possess a definite volume but no fixed shape?",
        "options": [
            "A. Interparticle attraction holds particles together to preserve volume, but particles are free to slide past one another to conform to the container",
            "B. Liquid particles are completely rigid and break upon touching glass",
            "C. Liquids have zero interparticle attraction and expand to fill all rooms",
            "D. Liquid particles are connected by rigid steel springs"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Volume Cohesion:</strong> Moderate interparticle attraction prevents particles from separating infinitely, preserving fixed volume.<br><strong>Step 2: Shape Flexibility:</strong> Lack of fixed lattice sites enables particles to glide past each other, taking the container's shape.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 9,
        "question": "Why are liquids and gases collectively classified by scientists as 'fluids'?",
        "options": [
            "A. Because both consist exclusively of water and air",
            "B. Because both lack a fixed shape and possess the ability to flow under applied shear force",
            "C. Because both are completely impossible to compress",
            "D. Because both have identical boiling points"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Fluid Definition:</strong> A fluid is any substance that continually deforms (flows) under an applied shear stress.<br><strong>Step 2: Applicability:</strong> Both liquids and gases flow and lack fixed shapes, making both fluids.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 10,
        "question": "How does the process of evaporation differ from boiling in liquid water?",
        "options": [
            "A. Boiling happens only at 0°C; evaporation happens at 100°C",
            "B. Boiling is a bulk phenomenon with vapour bubbles forming throughout; evaporation is a surface phenomenon occurring below the boiling point",
            "C. Boiling is quiet without any bubbles; evaporation produces violent explosive bubbles",
            "D. Evaporation requires a Bunsen burner flame while boiling happens in a refrigerator"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Boiling:</strong> Occurs at the boiling point ($100°C$ at $1\text{ atm}$) throughout the bulk liquid.<br><strong>Step 2: Evaporation:</strong> Occurs at the surface at any temperature below boiling as energetic surface particles escape.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 11,
        "question": "What is the primary reason why gases expand to fill the entire volume of any container they are placed in?",
        "options": [
            "A. Gas particles are magnetically attracted to container lids",
            "B. Interparticle attractions are negligible and particles move rapidly in all directions",
            "C. Gas particles are heavier than solid particles",
            "D. Gas particles melt into vacuum"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Negligible Cohesion:</strong> In gases, interparticle attractive forces are near zero.<br><strong>Step 2: High Velocity:</strong> Particles move rapidly in random directions, dispersing until bounded by physical container walls.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 12,
        "question": "If you fill three identical syringes with chalk pieces, water, and air respectively, which syringe piston will compress significantly when pushed by hand?",
        "options": [
            "A. Only the syringe filled with chalk",
            "B. Only the syringe filled with water",
            "C. Only the syringe filled with air",
            "D. All three syringes compress equally easily"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Interparticle Spacing:</strong> In chalk (solid) and water (liquid), particles are tightly packed with minimal void space.<br><strong>Step 2: Gas Compressibility:</strong> In air (gas), particles are separated by vast empty spaces, allowing easy compression.<br><strong>Step 3: Conclusion:</strong> Only the air syringe compresses (Option C).</p>"
    },
    {
        "id": 13,
        "question": "What occurs when a single crystal of potassium permanganate (KMnO₄) is placed in undisturbed water at room temperature?",
        "options": [
            "A. The water particles freeze into purple ice crystals instantly",
            "B. Moving water particles collide with the crystal, dislodging and diffusing purple particles throughout the beaker",
            "C. The crystal remains an intact rock forever unless physically stirred with a spoon",
            "D. The crystal floats to the ceiling of the room"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Constant Particle Motion:</strong> Water particles are in continuous random motion.<br><strong>Step 2: Collisional Dissolution:</strong> Water particles strike the crystal surface, dislodging $\text{KMnO}_4$ particles and dispersing them via diffusion.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 14,
        "question": "How does the temperature of water influence the rate at which potassium permanganate diffuses?",
        "options": [
            "A. It diffuses fastest in ice-cold water and slowest in hot water",
            "B. It diffuses fastest in hot water, moderately at room temperature, and slowest in ice-cold water",
            "C. Temperature has zero effect on the diffusion rate",
            "D. Hot water prevents diffusion completely by destroying particles"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Kinetic-Temperature Relation:</strong> Thermal energy directly increases particle velocity ($E_k \\propto T$).<br><strong>Step 2: Collision Rate:</strong> In hot water, water particles move faster and strike the solute more vigorously, speeding diffusion.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 15,
        "question": "Why does the fragrance of a burning incense stick (agarbatti) spread rapidly to the opposite side of a room?",
        "options": [
            "A. Air particles are static, but fragrance particles possess wings",
            "B. Rapidly moving air particles constantly collide with and disperse the fragrance vapor particles",
            "C. The room becomes a total vacuum when incense is lit",
            "D. Fragrance particles only travel through solid walls"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Gaseous Diffusion:</strong> Burning releases high-velocity vaporized aroma particles.<br><strong>Step 2: Air Collisions:</strong> Air molecules collide with aroma particles, scattering them across the room via gaseous diffusion.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 16,
        "question": "Which of the following substances consists of individual, unbonded atoms as its fundamental constituent particles?",
        "options": [
            "A. Solid Iron (Fe)",
            "B. Liquid Water (H₂O)",
            "C. Carbon dioxide gas (CO₂)",
            "D. Table salt (NaCl)"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Elemental Metals:</strong> Metals like iron ($\text{Fe}$), copper ($\text{Cu}$), and gold ($\text{Au}$) consist of individual atoms arranged in a metallic lattice.<br><strong>Step 2: Contrast:</strong> Water, $\text{CO}_2$, and salt are chemical compounds consisting of molecules or ionic networks.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 17,
        "question": "Why do many non-metallic elements, such as hydrogen and oxygen, exist naturally as diatomic molecules (H₂ and O₂) rather than isolated single atoms?",
        "options": [
            "A. Single atoms are too small to be weighed by laboratory balances",
            "B. Isolated atoms of these elements are chemically unstable and achieve electronic stability by sharing electrons in pairs",
            "C. Magnetic gravity glues all atoms into pairs",
            "D. Single atoms disintegrate immediately into sunlight"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Stability:</strong> An isolated hydrogen or oxygen atom has an incomplete valence shell.<br><strong>Step 2: Molecule Formation:</strong> By bonding into $\text{H}_2$ or $\text{O}_2$, the atoms share electrons to achieve a stable electronic configuration.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 18,
        "question": "What is the exact atomic composition of one single molecule of pure water?",
        "options": [
            "A. One hydrogen atom and one oxygen atom (HO)",
            "B. Two hydrogen atoms chemically bonded to one oxygen atom (H₂O)",
            "C. Two oxygen atoms and one hydrogen atom (HO₂)",
            "D. Two hydrogen atoms and two oxygen atoms (H₂O₂)"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Chemical Formula:</strong> Water is represented chemically as $\text{H}_2\text{O}$.<br><strong>Step 2: Stoichiometry:</strong> Every individual water molecule consists of 2 hydrogen atoms bonded to 1 oxygen atom.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 19,
        "question": "In which state of matter are the interparticle spaces the smallest?",
        "options": [
            "A. Gaseous state",
            "B. Liquid state",
            "C. Solid state",
            "D. Plasma state"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Particle Packing:</strong> In solids, strong cohesive forces pack constituent particles as closely as possible.<br><strong>Step 2: Void Comparison:</strong> Solids have the minimum interparticle spacing, followed by liquids, and lastly gases.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 20,
        "question": "What happens to the kinetic energy of constituent particles when a substance is heated?",
        "options": [
            "A. The kinetic energy decreases and particles slow down",
            "B. The kinetic energy increases and particles move or vibrate faster",
            "C. The kinetic energy drops to zero at 100°C",
            "D. The kinetic energy converts into static electricity"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Thermodynamic Principle:</strong> Temperature is a direct macroscopic measure of the average kinetic energy of constituent particles ($E_k \\propto T$).<br><strong>Step 2: Effect:</strong> Heating increases kinetic energy, causing faster vibrations in solids and faster translational speeds in fluids.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 21,
        "question": "Why does ice float on liquid water despite being a solid?",
        "options": [
            "A. Ice particles lose all their mass when freezing",
            "B. Water molecules form an open cage-like crystalline structure upon freezing, making ice less dense than liquid water",
            "C. Ice is composed of helium gas bubbles exclusively",
            "D. Liquid water repels ice with electrostatic repulsion"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Hydrogen Bonding:</strong> As water freezes below $4°C$, hydrogen bonds arrange molecules into an open hexagonal cage-like lattice.<br><strong>Step 2: Density Effect:</strong> This cage structure creates larger voids, resulting in lower density than liquid water ($\rho_{\text{ice}} \\approx 0.92\text{ g/cm}^3 < 1.0\text{ g/cm}^3$).<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 22,
        "question": "What is the physical term for the temperature at which a liquid turns into vapour throughout its bulk at standard atmospheric pressure?",
        "options": [
            "A. Melting point",
            "B. Boiling point",
            "C. Condensation point",
            "D. Critical point"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Phase Definition:</strong> The temperature at which liquid vapour pressure equals atmospheric pressure and vaporizes throughout is the <strong>boiling point</strong>.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 23,
        "question": "Which of the following processes represents diffusion occurring in the gaseous state?",
        "options": [
            "A. Sugar dissolving in a cup of coffee",
            "B. A drop of ink spreading through a glass of still water",
            "C. The aroma of baked cookies spreading from the kitchen to the bedroom",
            "D. Copper sulphate crystals growing in a beaker"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Medium Analysis:</strong> Cookie aroma spreading through air involves gaseous fragrance particles intermixing with gaseous air molecules.<br><strong>Step 2: Liquid vs Gas:</strong> Sugar in coffee and ink in water are liquid diffusion examples.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 24,
        "question": "If you keep a drop of blue ink at the bottom of a water glass without stirring, what will you observe after 24 hours?",
        "options": [
            "A. The ink remains a tight drop at the bottom forever",
            "B. The ink floats to the top and forms a hard rock",
            "C. The ink particles diffuse uniformly, coloring the entire volume of water light blue",
            "D. The water completely evaporates within 10 seconds"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Random Particle Motion:</strong> Water particles continuously collide with ink particles.<br><strong>Step 2: Equilibrium:</strong> Over hours, diffusion ensures complete homogeneous distribution throughout the beaker.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 25,
        "question": "Why does wet clothing dry faster on a hot, sunny day compared to a cold, overcast day?",
        "options": [
            "A. Solar heat increases the kinetic energy of water particles, accelerating the rate of evaporation",
            "B. Sunlight destroys the hydrogen atoms in water",
            "C. Cold air has zero space for water particles",
            "D. Hot air freezes water into steam"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Evaporation Rate:</strong> Higher ambient temperature supplies thermal energy to surface water molecules.<br><strong>Step 2: Escaping Velocity:</strong> More particles achieve sufficient kinetic energy to escape cohesive liquid forces into air.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 26,
        "question": "What is the Greek philosophical equivalent of Acharya Kanad's concept of 'Parmanu'?",
        "options": [
            "A. Atomos (proposed by Democritus and Leucippus)",
            "B. Ether (proposed by Aristotle)",
            "C. Phlogiston",
            "D. Humors"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Comparative History:</strong> Around 400 BCE, Democritus proposed that all matter is composed of indivisible particles called <em>atomos</em> (meaning uncuttable).<br><strong>Step 2: Parallel:</strong> This closely parallels Kanad's earlier concept of <em>Parmanu</em>.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 27,
        "question": "In a gas cylinder under high pressure, what happens to the distance between gas particles?",
        "options": [
            "A. The distance between particles increases tenfold",
            "B. The particles are forced closer together, drastically decreasing interparticle spaces",
            "C. The gas particles turn into lead bricks",
            "D. The particles stop moving entirely"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Compression Mechanism:</strong> Increasing external pressure forces gas particles into the existing void spaces.<br><strong>Step 2: Proximity:</strong> Consequently, interparticle distances diminish, increasing collision frequency.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 28,
        "question": "Why can an diver easily cut through water in a swimming pool, but cannot walk through a solid concrete wall?",
        "options": [
            "A. Water particles have no mass",
            "B. Concrete particles have zero attraction",
            "C. Interparticle attractions in liquid water are relatively weak and can be overcome by muscular force, whereas concrete has immense lattice cohesion",
            "D. Water is composed purely of empty vacuum"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Cohesive Comparison:</strong> Liquids have moderate attractive forces and particles that slide freely, allowing external objects to displace them.<br><strong>Step 2: Rigid Solids:</strong> Concrete particles are bound in a rigid interlocking crystalline lattice that resists displacement.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 29,
        "question": "What is the difference between an element and a compound at the molecular level?",
        "options": [
            "A. An element consists of only one kind of atom; a compound consists of two or more different kinds of atoms chemically combined in fixed ratios",
            "B. Elements are always liquids; compounds are always gases",
            "C. Elements can be seen with the eye; compounds are completely invisible",
            "D. Elements contain no particles"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Chemical Definitions:</strong> An element is composed of one type of atom (e.g., $\text{O}_2$, $\text{Fe}$).<br><strong>Step 2: Compounds:</strong> A compound contains atoms of different elements bonded chemically in fixed ratios (e.g., $\text{H}_2\text{O}$, $\text{CO}_2$).<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 30,
        "question": "When solid camphor or naphthalene balls disappear over time without leaving any liquid residue, what process has occurred?",
        "options": [
            "A. Melting into clear water",
            "B. Sublimation (direct transition from solid to gaseous state)",
            "C. Nuclear fission",
            "D. Dissolution into floor tiles"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Sublimation:</strong> Certain solids possess weak intermolecular forces that allow particles to transition directly from solid to vapour without entering the liquid state.<br><strong>Step 2: Examples:</strong> Camphor, naphthalene, and dry ice ($\text{CO}_2$) undergo sublimation.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 31,
        "question": "Which of the following statements regarding the movement of particles in liquids is TRUE?",
        "options": [
            "A. Liquid particles are completely stationary at room temperature",
            "B. Liquid particles are in constant, random motion, sliding past one another within a confined volume",
            "C. Liquid particles can only move when stirred with a glass rod",
            "D. Liquid particles escape into space immediately upon melting"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Liquid Dynamics:</strong> Thermal energy keeps liquid particles in continuous chaotic motion.<br><strong>Step 2: Confinement:</strong> Attractive forces keep them confined to the liquid volume while allowing them to slide past neighbors.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 32,
        "question": "What is the approximate size of a typical atom in metres?",
        "options": [
            "A. About 1 millimetre (10⁻³ m)",
            "B. About 1 micrometre (10⁻⁶ m)",
            "C. About 0.1 nanometre (10⁻¹⁰ m)",
            "D. About 1 metre (10⁰ m)"
        ],
        "correct": 2,
        "solution": "<p><strong>Step 1: Atomic Scale:</strong> The diameter of typical atoms ranges around $1$ to $3$ angstroms, which is approximately $10^{-10}\text{ m}$ ($0.1\text{ nm}$).<br><strong>Step 2: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 33,
        "question": "Why does a gas exert pressure on the inner walls of its container?",
        "options": [
            "A. Gas particles are magnetically attracted to the container walls",
            "B. Billions of rapidly moving gas particles continuously collide elastically with the container walls, exerting force per unit area",
            "C. Gas particles freeze onto the walls and pull inward",
            "D. Gas particles create gravity inside the cylinder"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Kinetic Theory:</strong> Gas particles travel at high speeds in random directions.<br><strong>Step 2: Pressure Genesis:</strong> Continuous collisions of particles against the container wall transfer momentum, generating a net perpendicular force per unit area ($P = F/A$).<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 34,
        "question": "A balloon filled with air shrinks slightly when placed in a freezer. Why?",
        "options": [
            "A. The freezer eats the rubber of the balloon",
            "B. Cooling reduces the kinetic speed of gas particles; they collide less frequently and forcefully, lowering internal pressure",
            "C. Air particles leak through the rubber only when cold",
            "D. Air turns into solid rock at 0°C"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Temperature-Kinetic Effect:</strong> Lower temperature reduces particle kinetic energy and velocity ($E_k \\propto T$).<br><strong>Step 2: Pressure & Volume:</strong> Particles hit the inner balloon walls with reduced momentum, allowing outside atmospheric pressure to compress the balloon.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 35,
        "question": "Which of the following represents a chemical compound composed of three atoms per molecule?",
        "options": [
            "A. Carbon dioxide (CO₂)",
            "B. Hydrogen gas (H₂)",
            "C. Oxygen gas (O₂)",
            "D. Helium gas (He)"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Atom Count:</strong> $\text{CO}_2$ consists of 1 carbon atom and 2 oxygen atoms, totaling 3 atoms per molecule (triatomic).<br><strong>Step 2: Contrast:</strong> $\text{H}_2$ and $\text{O}_2$ have 2 atoms; $\text{He}$ has 1 atom.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 36,
        "question": "Why does a piece of chalk absorb ink when dipped into an ink bottle?",
        "options": [
            "A. Chalk is a living organism that drinks ink",
            "B. The ink particles diffuse into the fine pores and interparticle spaces of the porous chalk",
            "C. Chalk dissolves completely in ink within 1 second",
            "D. Ink evaporates and vanishes instantly"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Capillarity & Porosity:</strong> Chalk is an aggregate of microscopic particles separated by tiny pores.<br><strong>Step 2: Infiltration:</strong> Liquid ink particles are drawn into and diffuse through these interparticle voids by capillary action.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 37,
        "question": "What is the state of matter of a substance whose melting point is 80°C and boiling point is 218°C at room temperature (25°C)?",
        "options": [
            "A. Solid",
            "B. Liquid",
            "C. Gas",
            "D. Plasma"
        ],
        "correct": 0,
        "solution": "<p><strong>Step 1: Temperature Comparison:</strong> At $25°C$, the temperature is strictly below the melting point ($80°C$).<br><strong>Step 2: State Rule:</strong> When ambient temperature is below the melting point, the substance has not yet melted and remains a solid.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 38,
        "question": "What did Robert Brown observe in 1827 that provided empirical evidence for the continuous random motion of particles in fluids?",
        "options": [
            "A. Polished metal mirrors reflecting light rays",
            "B. Pollen grains suspended in water executing constant, erratic zig-zag motion (Brownian Motion)",
            "C. Planets revolving around the Sun",
            "D. Lightning striking a church steeple"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Discovery:</strong> Botanist Robert Brown observed microscopic pollen grains dancing erratically in water.<br><strong>Step 2: Explanation:</strong> Albert Einstein later proved in 1905 that this <em>Brownian motion</em> is caused by relentless sub-microscopic collisions of water particles hitting the grain from all sides.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 39,
        "question": "Which of the following pairs represents two different states of the EXACT same chemical constituent particle (H₂O)?",
        "options": [
            "A. Liquid water and hydrogen peroxide",
            "B. Solid ice and water vapour (steam)",
            "C. Oxygen gas and ozone gas",
            "D. Carbon monoxide and carbon dioxide"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Chemical Identity:</strong> Both ice and steam are composed of identical $\text{H}_2\text{O}$ molecules.<br><strong>Step 2: Phase Difference:</strong> Ice is the solid crystalline state, while steam is the gaseous state of $\text{H}_2\text{O}$.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 40,
        "question": "Which of the following summaries accurately synthesizes the core principles of the particulate nature of matter?",
        "options": [
            "A. Matter is continuous and stationary; particles are only created when liquids are heated to boiling",
            "B. Matter is composed of tiny constituent particles (atoms and molecules) separated by interparticle spaces, bound by attractive forces, and in perpetual thermal motion",
            "C. Matter is made of four mystical elements: earth, fire, air, and ether, with zero particles",
            "D. Only gases possess constituent particles; solids and liquids are single indivisible blocks"
        ],
        "correct": 1,
        "solution": "<p><strong>Step 1: Grand Synthesis:</strong> All matter consists of constituent particles (atoms/molecules).<br><strong>Step 2: Triad of Properties:</strong> (1) They have empty interparticle spaces between them; (2) They exert mutual interparticle attractions; (3) They possess thermal energy and are in constant motion.<br><strong>Step 3: Conclusion:</strong> Option B is the complete and accurate scientific synthesis.</p>"
    }
]

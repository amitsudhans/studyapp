# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 5: Force, Types of Forces, Weight, and Buoyancy
Complete curriculum dataset with compact headings, vocabulary, 16 content slides + 4 mastery challenge slides,
32 in-slide checkpoints, and 40 mastery quiz questions with comprehensive step-by-step solutions.
"""

SLIDES = [
    # SLIDE 1
    {
        "id": 1,
        "title": "Defining Force & Interaction",
        "tag": "Definition • SI Unit • Two-Body Interaction",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Welcome, explorers of physics! What happens when you kick a football, open a drawer, or lift a school bag? You apply a push or a pull! In science, every push or pull is called a force. Let's see how forces require an interaction between at least two bodies.",
        "theory": r"""
<h3>What is a Force?</h3>
<p>In everyday life, we perform countless actions like kicking, hitting, lifting, pushing, pulling, twisting, and dragging. In science, all these diverse actions can be grouped into two fundamental physical operations: a <strong>push</strong> or a <strong>pull</strong> applied to an object.</p>
<p>Therefore, <strong>Force is defined as a push or a pull acting upon an object as a result of its interaction with another object.</strong></p>

<h4>The SI Unit of Force</h4>
<ul>
  <li>The International System of Units (SI) unit of force is the <strong>newton</strong>, represented by the capital symbol <strong>N</strong>.</li>
  <li>It is named in honor of Sir Isaac Newton for his pioneering work on classical mechanics and the laws of motion.</li>
  <li>To give you a real-world intuition: the gravitational force pulling downward on a standard medium apple (mass of about $100\text{ grams}$) resting in your palm is approximately equal to <strong>$1\text{ newton}$ ($1\text{ N}$)</strong>!</li>
</ul>

<h4>The Interaction Requirement</h4>
<p>A force does not exist in isolation. <strong>A force comes into play only when at least two objects interact with each other.</strong></p>
<ul>
  <li>If a car stalls on a flat road, a person simply standing behind the stationary car exerts <em>no force</em> upon it. The car remains at rest.</li>
  <li>Only when the person physically makes contact and begins <em>pushing</em> against the car's bumper does an interaction occur. The person exerts a forward force on the car, causing it to begin rolling forward.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Force", "definition": "A push or a pull exerted on an object resulting from its physical or field interaction with another object."},
            {"word": "Newton (N)", "definition": "The standard SI unit of force; approximately equal to the downward gravitational force on a 100g apple ($1\\text{ N} \\approx 0.1\\text{ kg} \\times 9.8\\text{ m/s}^2$)."},
            {"word": "Interaction", "definition": "A mutual reciprocal action or influence where at least two objects exert forces on each other."},
            {"word": "State of Rest", "definition": "The physical condition of an object when its position does not change with time relative to its surroundings."}
        ],
        "sim_id": "force_interaction_sim",
        "checkpoints": [
            {
                "question": "In scientific terminology, what is a force fundamentally defined as?",
                "options": [
                    "A form of thermal energy stored inside atoms",
                    "A push or a pull applied on an object resulting from an interaction",
                    "The chemical mass of a stationary substance",
                    "The time it takes for an object to freeze"
                ],
                "correct": 1,
                "explanation": "Force is defined in physics as any push or pull exerted on an object through interaction with another object.",
                "solution": "Definition: Force = a push or a pull resulting from interaction between two objects. SI unit: Newton (N)."
            },
            {
                "question": "A person stands perfectly still 1 meter behind a stalled automobile without touching it. What force is the person exerting on the car?",
                "options": [
                    "A forward pushing force of 50 Newtons",
                    "Zero force, because force requires an interaction between at least two objects",
                    "A gravitational pulling force of 500 Newtons",
                    "A frictional stopping force"
                ],
                "correct": 1,
                "explanation": "Forces come into play only when objects interact. Without physical contact or significant field interaction, zero pushing force is exerted.",
                "solution": "Interaction requirement: Forces arise only when two entities interact. Standing apart without touching exerts 0 contact force."
            }
        ]
    },

    # SLIDE 2
    {
        "id": 2,
        "title": "Four Effects of Force",
        "tag": "Motion Dynamics • Direction & Shape Changes",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "We cannot directly see a force with our eyes, but we can easily see what a force DOES! A force can start motion, accelerate or brake a moving body, bend its path, or squeeze its shape. Let's observe the four core effects of force.",
        "theory": r"""
<h3>Recognizing Force by Its Effects</h3>
<p>Although force is an invisible physical vector, its presence is recognized instantly through the observable physical changes it produces on matter. The application of a force on an object can produce <strong>four fundamental effects</strong>:</p>

<h4>1. Make an Object Move from a State of Rest</h4>
<p>An object at rest cannot begin moving on its own. Applying a push or pull starts its motion. For example: kicking a stationary football, pulling a wagon, or pushing a toy cart across the floor.</p>

<h4>2. Change the Speed of a Moving Object</h4>
<ul>
  <li><strong>Accelerating (Speeding Up):</strong> If a force is applied in the <em>same direction</em> as the object's motion (e.g., pedaling harder on a bicycle or pushing a child's swing from behind), the object's speed increases.</li>
  <li><strong>Decelerating (Slowing Down / Stopping):</strong> If a force is applied in the <em>opposite direction</em> to motion (e.g., applying bicycle brakes, catching a cricket ball, or friction from grass), the speed decreases until the object comes to rest.</li>
</ul>

<h4>3. Change the Direction of Motion</h4>
<p>When a batsman strikes a cricket ball pitched toward him, the cricket bat exerts a force that alters the trajectory and direction of the ball across the boundary without stopping it completely.</p>

<h4>4. Change the Shape or Size of an Object (Deformation)</h4>
<p>A force can alter the physical dimensions of an object even if the object remains stationary:</p>
<ul>
  <li>Pressing a soft rubber foam sponge with your fingers.</li>
  <li>Kneading wheat flour dough into a round chapati.</li>
  <li>Stretching a rubber band or coiled steel spring.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Acceleration", "definition": "The rate of increase in speed of a moving object caused by an unbalanced force in the direction of motion."},
            {"word": "Deceleration", "definition": "The reduction in speed of a moving object when a force acts opposite to the direction of motion (braking)."},
            {"word": "Trajectory", "definition": "The curved or straight path followed by a projectile or moving object through space."},
            {"word": "Deformation", "definition": "A temporary or permanent change in the shape or dimensions of a body caused by an applied mechanical force."}
        ],
        "sim_id": "effects_of_force_sim",
        "checkpoints": [
            {
                "question": "What happens to the speed of a rolling skateboard when you push it in the exact same direction it is already moving?",
                "options": [
                    "Its speed increases (it accelerates)",
                    "Its speed decreases immediately",
                    "It turns around 180 degrees backward",
                    "Its mass doubles"
                ],
                "correct": 0,
                "explanation": "Applying a force in the direction of an object's motion accelerates it, increasing its speed.",
                "solution": "When force vector $\\vec{F}$ is parallel to velocity vector $\\vec{v}$, speed increases."
            },
            {
                "question": "Which of the following actions demonstrates a force changing the SHAPE of an object rather than its speed?",
                "options": [
                    "A goalkeeper catching a flying soccer ball",
                    "A batsman hitting a cricket ball toward the boundary",
                    "Kneading moist dough into flat chapatis with a rolling pin",
                    "A hockey player passing a puck across ice"
                ],
                "correct": 2,
                "explanation": "Kneading dough changes its physical shape and geometric form, which is an example of mechanical deformation.",
                "solution": "Kneading dough alters molecular configuration, demonstrating shape change (deformation)."
            }
        ]
    },

    # SLIDE 3
    {
        "id": 3,
        "title": "Contact vs. Non-Contact",
        "tag": "Broad Classification • Touch vs. Field",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Do objects always have to physically touch to exert a force? If you kick a ball, yes! But what about a magnet snapping a nail, or Earth pulling a dropped mango from the tree? Let's classify forces into Contact and Non-Contact categories.",
        "theory": r"""
<h3>The Two Grand Families of Forces</h3>
<p>In physics, all forces in nature are broadly classified into two major categories based on whether <strong>physical contact</strong> between the interacting bodies is necessary:</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.88rem;">
  <thead>
    <tr style="border-bottom: 2px solid #38bdf8; color: #38bdf8;">
      <th style="padding: 0.4rem; text-align: left;">Category</th>
      <th style="padding: 0.4rem; text-align: left;">Physical Contact?</th>
      <th style="padding: 0.4rem; text-align: left;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
      <td style="padding: 0.4rem; font-weight: bold; color: #f59e0b;">Contact Forces</td>
      <td style="padding: 0.4rem;"><strong>Yes</strong> (Direct or via stick/rope)</td>
      <td style="padding: 0.4rem;">Muscular force, Frictional force, Tension</td>
    </tr>
    <tr>
      <td style="padding: 0.4rem; font-weight: bold; color: #a855f7;">Non-Contact Forces</td>
      <td style="padding: 0.4rem;"><strong>No</strong> (Acts across empty space)</td>
      <td style="padding: 0.4rem;">Magnetic force, Electrostatic force, Gravitational force</td>
    </tr>
  </tbody>
</table>

<h4>Understanding Contact Forces</h4>
<p>Contact forces act <em>only</em> when there is physical contact between the interacting bodies. This contact can be direct (your hand lifting a mug) or indirect through an intermediary object (tugging a cart with a rope, hitting a tennis ball with a racquet).</p>

<h4>Understanding Non-Contact Forces (Action-at-a-Distance)</h4>
<p>Non-contact forces act through invisible <strong>force fields</strong> (magnetic, electric, gravitational fields) permeating space. The interacting bodies do not need to touch each other; their effects are felt across significant distances—even across the vast vacuum of outer space!</p>
""",
        "vocabulary": [
            {"word": "Contact Force", "definition": "A force that can only be exerted between objects when their physical surfaces are touching each other directly or via a connector."},
            {"word": "Non-Contact Force", "definition": "A force that acts across intervening space or vacuum without requiring physical contact between the interacting bodies."},
            {"word": "Action-at-a-Distance", "definition": "The physical concept where an object exerts a force on another object across space without mechanical contact."},
            {"word": "Force Field", "definition": "A region of space around a body (mass, charge, magnet) in which other bodies experience a non-contact force."}
        ],
        "sim_id": "contact_noncontact_sorter_sim",
        "checkpoints": [
            {
                "question": "Which of the following is classified as a NON-CONTACT force?",
                "options": [
                    "Muscular force exerted by a bullock pulling a cart",
                    "Friction between a rolling tire and asphalt road",
                    "Magnetic attraction between a bar magnet and iron filings from a distance",
                    "Force exerted by your fingers typing on a keyboard"
                ],
                "correct": 2,
                "explanation": "Magnetic force acts through space via magnetic fields without needing physical contact, making it a non-contact force.",
                "solution": "Non-contact forces act across space. Muscular and frictional forces require physical contact."
            },
            {
                "question": "Pulling a bucket of water from a well using a long nylon rope is an example of what type of force?",
                "options": [
                    "A non-contact electrostatic force",
                    "A contact force transmitted through the rope",
                    "A nuclear force",
                    "A magnetic levitation force"
                ],
                "correct": 1,
                "explanation": "The pulling force is a contact force transmitted mechanically through the tension of the rope connecting the bucket to your hands.",
                "solution": "Tension in a rope represents a contact force acting via mechanical linkage."
            }
        ]
    },

    # SLIDE 4
    {
        "id": 4,
        "title": "Muscular Force & Body",
        "tag": "Contact Force • Physiological Muscles",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Did you know that you are using muscular force right now to breathe and blink? Muscular force is produced by the contraction and relaxation of muscle fibers. It powers human labor and drives internal biological organs! Let's explore.",
        "theory": r"""
<h3>What is Muscular Force?</h3>
<p>The force resulting from the action of muscles in the body is called <strong>Muscular Force</strong>. Muscles contain specialized protein filaments (actin and myosin) that slide past one another, contracting or expanding to exert mechanical pushes and pulls.</p>

<h4>External Activities Powered by Muscular Force</h4>
<ul>
  <li><strong>Locomotion & Play:</strong> Walking, running, swimming, lifting weights, kicking a ball, and cycling.</li>
  <li><strong>Animal Labor:</strong> Throughout human history, domesticated animals (bullocks, horses, camels, elephants) have used their formidable muscular force to plow agricultural fields, carry heavy freight, and pull transport carts.</li>
</ul>

<h4>Vital Internal Physiological Processes</h4>
<p>Muscular force is not limited to external athletics; it is indispensable for keeping living organisms alive through internal involuntary muscle contractions:</p>
<ol>
  <li><strong>Chewing & Ingestion:</strong> Jaw muscles (masseter muscles) apply hundreds of Newtons of force to crush and grind solid food into manageable bites.</li>
  <li><strong>Peristalsis in the Alimentary Canal:</strong> Smooth muscles in the walls of the esophagus, stomach, and intestines contract rhythmically in wave-like motions (peristalsis) to push food forward along the digestive tract.</li>
  <li><strong>Cardiac Circulation (Heart Pump):</strong> The human heart is a powerful muscular organ. Cardiac muscle contracts and relaxes continuously (approx. 72 times per minute), exerting hydraulic force to pump blood through thousands of kilometers of blood vessels!</li>
  <li><strong>Breathing (Diaphragm):</strong> The muscular diaphragm contracts downward to expand the chest cavity, drawing air into the lungs.</li>
</ol>
""",
        "vocabulary": [
            {"word": "Muscular Force", "definition": "The contact force exerted by the contraction and elongation of biological muscle fibers in humans and animals."},
            {"word": "Peristalsis", "definition": "Involuntary wave-like contractions of smooth muscular walls in the digestive tract that propel food forward."},
            {"word": "Cardiac Muscle", "definition": "The specialized, tirelessly contracting muscular tissue of the heart that pumps oxygenated blood throughout the body."},
            {"word": "Contractile Proteins", "definition": "Microscopic protein filaments (actin and myosin) whose sliding action generates mechanical muscle tension."}
        ],
        "sim_id": "muscular_force_sim",
        "checkpoints": [
            {
                "question": "Which internal physiological process in the human body relies directly on involuntary muscular force?",
                "options": [
                    "The expansion of fingernails over weeks",
                    "Peristalsis pushing food along the alimentary canal and cardiac blood pumping",
                    "The bleaching of hair in sunlight",
                    "The evaporation of sweat from skin pores"
                ],
                "correct": 1,
                "explanation": "Peristaltic movements in intestines and cardiac pumping by heart walls are both driven by internal muscular force.",
                "solution": "Smooth muscles produce peristalsis, and cardiac muscle pumps blood—both are vital internal muscular forces."
            },
            {
                "question": "Why is muscular force classified strictly as a CONTACT force?",
                "options": [
                    "Because muscles can push objects from 10 meters away without touching them",
                    "Because our body must make direct physical contact (or contact through a tool) to exert force on an object",
                    "Because muscles only operate in electric circuits",
                    "Because muscles only exist in cold water"
                ],
                "correct": 1,
                "explanation": "Muscular force cannot act across empty space; the body or its extensions must physically touch the object to push or pull it.",
                "solution": "Muscles require mechanical contact (direct or via tool) to transmit tensile or compressive force."
            }
        ]
    },

    # SLIDE 5
    {
        "id": 5,
        "title": "Friction & Surface Locking",
        "tag": "Contact Force • Microscopic Asperities",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Roll a marble across a smooth tile floor and then across a thick rug. Why does it stop much sooner on the rug? Friction! Even mirror-smooth surfaces have microscopic mountains and valleys that interlock like jigsaw puzzles.",
        "theory": r"""
<h3>The Nature of Friction</h3>
<p>Whenever an object moves or attempts to move over the surface of another body, an opposing contact force comes into play. This opposing force is known as the <strong>Force of Friction</strong> (or simply <em>friction</em>).</p>

<h4>Cardinal Rules of Friction</h4>
<ol>
  <li><strong>Always Opposes Relative Motion:</strong> Friction acts parallel to the contact surfaces and <em>always in a direction opposite to the direction of motion</em>. If an object moves forward (to the right), friction acts backward (to the left).</li>
  <li><strong>Autonomous Deceleration:</strong> When you stop pedaling a bicycle or rolling a ball, friction gradually decelerates the object until it comes to a complete halt.</li>
</ol>

<h4>Microscopic Cause: Surface Irregularities</h4>
<p>Even surfaces that appear mirror-smooth to the naked eye have countless microscopic irregularities, ridges, and pits called <strong>asperities</strong>.</p>
<ul>
  <li>When two surfaces are placed in contact, the microscopic peaks of one surface sink into the valleys of the other, <strong>interlocking mechanically</strong> like jagged teeth of gears.</li>
  <li>To slide one surface over another, an external force must be applied to break or overcome this mechanical interlocking.</li>
  <li><strong>Rough vs. Smooth:</strong> Rough surfaces (like sandpaper, rough wood, or asphalt) have deeper irregularities and greater interlocking, resulting in much higher friction. Smooth surfaces (like polished ice, glass, or lubricated metal) have shallower irregularities and lower friction.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Friction", "definition": "A contact force that opposes the relative motion or impending sliding between two solid surfaces in contact."},
            {"word": "Asperities", "definition": "Microscopic irregularities, peaks, and valleys present on all material surfaces that interlock to cause friction."},
            {"word": "Interlocking", "definition": "The mechanical fitting together of microscopic surface bumps that resists sliding motion."},
            {"word": "Relative Motion", "definition": "The movement of one body with respect to another body whose surface it touches."}
        ],
        "sim_id": "friction_microscopic_sim",
        "checkpoints": [
            {
                "question": "In what direction does the force of friction always act relative to a moving object?",
                "options": [
                    "In the exact same direction as the object's motion",
                    "Perpendicularly upward toward the sky",
                    "In the direction opposite to the direction of relative motion",
                    "In random circular swirling loops"
                ],
                "correct": 2,
                "explanation": "Friction always opposes the relative sliding between surfaces, so it acts in the direction opposite to motion.",
                "solution": "Fundamental law: Friction vector $\\vec{f}$ acts anti-parallel to relative velocity vector $\\vec{v}$."
            },
            {
                "question": "What is the microscopic cause of friction between two solid surfaces?",
                "options": [
                    "Nuclear magnetic resonance between atoms",
                    "Microscopic irregularities, peaks, and valleys on the surfaces interlocking with each other",
                    "Air pressure sucking the surfaces together like a vacuum",
                    "Chemical combustion between metal molecules"
                ],
                "correct": 1,
                "explanation": "Microscopic surface irregularities (asperities) interlock when pressed together, creating mechanical resistance to sliding.",
                "solution": "Cause: Interlocking of microscopic surface asperities."
            }
        ]
    },

    # SLIDE 6
    {
        "id": 6,
        "title": "Fluid Friction & Drag",
        "tag": "Contact Force • Streamlining Aerodynamics",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Did you know that air and water also exert friction? When a jet airliner or a fish cuts through fluid, molecules push back with frictional drag. That's why birds, airplanes, and bullet trains have sleek, streamlined shapes!",
        "theory": r"""
<h3>Friction in Liquids and Gases</h3>
<p>Friction is not confined to solid surfaces. In science, liquids and gases are collectively known as <strong>fluids</strong> because they can flow. When an object moves through a fluid, the fluid molecules collide with the moving object, exerting a frictional resistance known as <strong>Fluid Friction</strong> or <strong>Drag</strong>.</p>

<h4>Factors Affecting Fluid Drag</h4>
<ul>
  <li><strong>Speed of Object:</strong> Drag increases drastically with speed ($F_{\\text{drag}} \\propto v^2$). Doubling your speed quadruples the aerodynamic air resistance!</li>
  <li><strong>Fluid Viscosity & Density:</strong> Moving through dense water requires vastly more effort than moving through light air.</li>
  <li><strong>Shape of the Object:</strong> Blunt, flat objects push large volumes of fluid ahead of them, creating high turbulence and enormous drag. Sleek, curved shapes slice through with minimal resistance.</li>
</ul>

<h4>The Solution: Streamlining</h4>
<p>To reduce fluid drag and minimize wasted fuel energy, high-speed objects are designed with <strong>streamlined shapes</strong>—rounded and tapering smoothly toward the rear:</p>
<ol>
  <li><strong>Nature's Pioneers:</strong> Millions of years of evolution gave birds and fish streamlined bodies so they can glide through air and water effortlessly.</li>
  <li><strong>Human Engineering:</strong> Airplanes, bullet trains, high-speed sports cars, and submarines are deliberately modeled after the streamlined profiles of birds and aquatic predators like sharks and dolphins!</li>
</ol>
""",
        "vocabulary": [
            {"word": "Fluid Friction (Drag)", "definition": "The resistive force exerted by a fluid (liquid or gas) on an object moving through it."},
            {"word": "Fluids", "definition": "Substances that have no fixed shape and can flow freely, encompassing both liquids and gases."},
            {"word": "Streamlining", "definition": "Giving an object a sleek, tapered aerodynamic profile to minimize fluid drag and turbulence."},
            {"word": "Turbulence", "definition": "Chaotic, swirling fluid eddies formed behind a blunt moving object that sap mechanical energy."}
        ],
        "sim_id": "fluid_drag_streamlining_sim",
        "checkpoints": [
            {
                "question": "What is the specialized scientific term for the frictional resistance exerted by fluids (air or water) on moving bodies?",
                "options": [
                    "Magnetic flux",
                    "Fluid friction or Drag",
                    "Gravitational potential",
                    "Electrostatic induction"
                ],
                "correct": 1,
                "explanation": "Frictional resistance exerted by liquids and gases is scientifically termed fluid friction or drag.",
                "solution": "Fluid resistance = Fluid Friction or Drag."
            },
            {
                "question": "Why are airplanes, high-speed trains, and racing cars designed with sleek, streamlined shapes?",
                "options": [
                    "To make them look shiny in photographs",
                    "To reduce fluid drag (air resistance) and conserve fuel energy",
                    "To make them heavier so they stay on the ground",
                    "To absorb sunlight more efficiently"
                ],
                "correct": 1,
                "explanation": "Streamlining allows air to glide smoothly around the vehicle without turbulence, minimizing drag and saving fuel.",
                "solution": "Engineering purpose: Minimizing aerodynamic drag and turbulence."
            }
        ]
    },

    # SLIDE 7
    {
        "id": 7,
        "title": "Magnetic Force & Poles",
        "tag": "Non-Contact Force • Action-at-a-Distance",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Bring two magnets close together and you can feel an invisible, mysterious push or pull pushing against your hands without touching! That is magnetic force. Let's examine how like poles repel and unlike poles attract.",
        "theory": r"""
<h3>The Invisible Magnetic Reach</h3>
<p>A magnet can exert a force on another magnet or on ferromagnetic materials (such as iron, steel, nickel, and cobalt) without physically touching them. Because it acts across intervening space via an invisible magnetic field, <strong>Magnetic Force is a Non-Contact Force</strong>.</p>

<h4>The Fundamental Law of Magnetic Poles</h4>
<p>Every magnet possesses two distinct poles: a <strong>North Pole (N)</strong> and a <strong>South Pole (S)</strong>. Magnetic interactions strictly obey the Law of Poles:</p>
<ul>
  <li><strong>Like Poles Repel:</strong> When two identical poles are brought near each other (North facing North, or South facing South), they exert an invisible <em>repulsive force</em> pushing each other away.</li>
  <li><strong>Unlike Poles Attract:</strong> When opposite poles face each other (North facing South), they exert a powerful <em>attractive force</em> pulling each other together.</li>
  <li><strong>Unmagnetized Iron:</strong> A magnet always attracts unmagnetized ferromagnetic materials (like iron nails or paperclips) regardless of which pole is presented, because the magnet induces temporary opposite polarity in the iron!</li>
</ul>

<h4>Magnetic Fields in Nature</h4>
<p>Magnetic force is harnessed in compasses, high-speed Maglev (magnetic levitation) trains that float above tracks without friction, MRI machines in hospitals, and electric motors.</p>
""",
        "vocabulary": [
            {"word": "Magnetic Force", "definition": "A non-contact force of attraction or repulsion exerted by a magnet on other magnets or magnetic materials."},
            {"word": "Magnetic Poles", "definition": "The two opposite regions at the ends of a magnet (North and South) where the magnetic field is concentrated."},
            {"word": "Repulsion", "definition": "The mechanical pushing force that drives like poles or like electric charges away from each other."},
            {"word": "Magnetic Levitation (Maglev)", "definition": "Suspending an object in mid-air using repulsive magnetic forces, eliminating mechanical friction."}
        ],
        "sim_id": "magnetic_force_poles_sim",
        "checkpoints": [
            {
                "question": "What happens when the North pole of one bar magnet is brought near the North pole of another freely suspended bar magnet?",
                "options": [
                    "They attract and snap tightly together",
                    "They repel each other without touching",
                    "They turn into liquid copper",
                    "Their magnetic fields cancel out permanently"
                ],
                "correct": 1,
                "explanation": "Like poles (North-North or South-South) repel each other across space via repulsive non-contact magnetic forces.",
                "solution": "Law of magnetic poles: Like poles repel; unlike poles attract."
            },
            {
                "question": "Why is magnetic force classified as a NON-CONTACT force?",
                "options": [
                    "Because it only exists inside computer screens",
                    "Because a magnet can pull iron objects or push other magnets from a distance without touching them",
                    "Because magnets cannot be touched by human fingers",
                    "Because it requires high voltage to function"
                ],
                "correct": 1,
                "explanation": "Magnets exert force through their surrounding magnetic field across space without physical contact.",
                "solution": "Non-contact criterion: Force acts across distance via magnetic fields."
            }
        ]
    },

    # SLIDE 8
    {
        "id": 8,
        "title": "Electrostatic Force & Charge",
        "tag": "Non-Contact Force • Static Electricity",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Rub a plastic comb through dry hair and hold it near tiny bits of paper. The paper scraps fly upward like magic! What invisible force pulled them? Electrostatic force! Let's explore how friction generates electric charges.",
        "theory": r"""
<h3>The Power of Static Charges</h3>
<p>When you rub certain insulating materials together (such as a plastic comb through dry hair, a glass rod with silk, or an inflated rubber balloon against a woolen sweater), friction rubs electrons off one material and transfers them onto the other.</p>
<p>This accumulation of stationary electric charges on a surface is known as <strong>Static Electricity</strong>.</p>

<h4>What is Electrostatic Force?</h4>
<p>The force exerted by a charged body on another charged or uncharged body is called <strong>Electrostatic Force</strong>. Because this force can act across space without touching, it is a <strong>Non-Contact Force</strong>.</p>

<h4>The Fundamental Laws of Electrostatics</h4>
<ul>
  <li><strong>Two Kinds of Charges:</strong> Electric charges exist in two varieties: <strong>Positive ($+$)</strong> and <strong>Negative ($-$)</strong>.</li>
  <li><strong>Like Charges Repel:</strong> Two similarly charged objects (positive with positive, or negative with negative) push each other away.</li>
  <li><strong>Unlike Charges Attract:</strong> Oppositely charged objects (positive with negative) pull toward each other.</li>
  <li><strong>Attraction of Uncharged Objects:</strong> A charged body can attract neutral, uncharged objects! For example, a negatively charged balloon polarizes the molecules in paper scraps, creating a temporary attractive force that lifts the scraps into the air.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Electrostatic Force", "definition": "The non-contact force exerted by a charged body on another charged or uncharged body."},
            {"word": "Static Electricity", "definition": "An imbalance of electric charges trapped on the surface of an insulating material, typically produced by friction."},
            {"word": "Charge Polarization", "definition": "The temporary shifting of electrons within a neutral body when brought near a charged object, causing attraction."},
            {"word": "Electron Transfer", "definition": "The microscopic movement of negatively charged electrons from one material to another during frictional rubbing."}
        ],
        "sim_id": "electrostatic_charge_sim",
        "checkpoints": [
            {
                "question": "What happens when an inflated balloon rubbed against a wool sweater is brought near tiny, neutral bits of paper?",
                "options": [
                    "The paper scraps are repelled into the floor",
                    "The paper scraps are attracted and fly upward to stick to the balloon",
                    "The balloon pops instantly from sound waves",
                    "The paper scraps catch fire"
                ],
                "correct": 1,
                "explanation": "The charged balloon exerts a non-contact electrostatic force on the neutral paper scraps by inducing opposite charges on their near surface, pulling them up.",
                "solution": "Static electric charges on balloon polarize neutral paper scraps $\\rightarrow$ electrostatic attraction lifts them."
            },
            {
                "question": "Two plastic drinking straws are both rubbed vigorously with the same woolen cloth and then suspended near each other. What will happen?",
                "options": [
                    "They will attract and fuse together",
                    "They will repel each other because both carry identical like charges",
                    "They will spin like helicopter blades",
                    "Nothing, because plastic cannot hold charge"
                ],
                "correct": 1,
                "explanation": "Rubbing both straws with the same wool gives them identical negative charges. Like charges repel each other.",
                "solution": "Both acquire identical charge $\\rightarrow$ Like charges repel."
            }
        ]
    },

    # SLIDE 9
    {
        "id": 9,
        "title": "Gravitational Attraction",
        "tag": "Non-Contact Force • Planetary Gravity",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Drop a pencil, a coin, or an apple from your hand. What happens? It accelerates straight downward toward the floor! Why doesn't it float sideways or up into space? Earth's invisible gravitational pull is constantly at work.",
        "theory": r"""
<h3>The Universal Pull: Gravity</h3>
<p>The attractive force with which planet Earth pulls all physical objects toward its center is called <strong>Gravitational Force</strong> (or simply <em>gravity</em>).</p>
<p>Gravity is an invisible, non-contact force acting across vast distances of empty space. It keeps our atmosphere locked to the planet, causes ocean tides, keeps the Moon in orbit around Earth, and governs the trajectory of planets around the Sun.</p>

<h4>Crucial Features of Gravitational Force</h4>
<ol>
  <li><strong>Strictly Attractive:</strong> Unlike magnetic or electrostatic forces (which can either attract or repel depending on poles or charge signs), <strong>gravitational force is ALWAYS attractive</strong>. Matter never repels matter gravitationally!</li>
  <li><strong>Universal Property:</strong> Gravity is not unique to Earth. Every single object in the universe with mass exerts a gravitational pull on every other object. You exert a tiny gravitational pull on your textbook, but it is too weak to notice because human masses are small. Only colossal planetary masses (like Earth's $5.97 \times 10^{24}\text{ kg}$) produce strong, easily noticeable gravitational forces.</li>
  <li><strong>Vertical Motion:</strong> When you drop any object from a height, gravity accelerates it downward. When you toss a ball upward, gravity opposes its upward motion, slows it to a momentary halt at its peak, and accelerates it back down.</li>
</ol>
""",
        "vocabulary": [
            {"word": "Gravitational Force", "definition": "The universal non-contact attractive force exerted by any mass on all other masses; specifically Earth's downward pull."},
            {"word": "Free Fall", "definition": "The downward motion of a body falling solely under the influence of gravitational force without other significant forces."},
            {"word": "Gravitational Acceleration (g)", "definition": "The acceleration gained by an object due to Earth's gravity, approximately $9.8\\text{ m/s}^2$ near the surface."},
            {"word": "Planetary Mass", "definition": "The colossal physical mass of a planet that creates a strong localized gravitational field in space."}
        ],
        "sim_id": "gravitational_pull_sim",
        "checkpoints": [
            {
                "question": "How does gravitational force fundamentally differ from magnetic and electrostatic forces?",
                "options": [
                    "Gravitational force is only active inside water",
                    "Gravitational force is ALWAYS attractive and never repulsive",
                    "Gravitational force only acts when objects physically touch",
                    "Gravitational force can be switched off with a battery"
                ],
                "correct": 1,
                "explanation": "Magnetic and electrostatic forces can attract or repel, but gravitational force is purely attractive across all matter.",
                "solution": "Distinctive property: Gravity is strictly an attractive force in nature."
            },
            {
                "question": "What force causes water to flow downward in rivers and raindrops to fall to Earth from clouds?",
                "options": [
                    "Muscular force of clouds",
                    "Earth's gravitational force",
                    "Magnetic force from the North Pole",
                    "Frictional drag from trees"
                ],
                "correct": 1,
                "explanation": "Earth's gravitational force pulls water droplets and river flows downward toward the planetary center of mass.",
                "solution": "Natural downward motion is driven by Earth's gravitational pull."
            }
        ]
    },

    # SLIDE 10
    {
        "id": 10,
        "title": "Mass vs. Weight",
        "tag": "Invariance vs. Force • Units (kg vs. N)",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Many people use 'mass' and 'weight' as if they mean the exact same thing, but in science, they are vastly different! Mass is the amount of matter in your body, while weight is Earth's gravitational pull on that matter. Let's compare them.",
        "theory": r"""
<h3>The Critical Distinction: Mass vs. Weight</h3>
<p>In everyday casual conversation, people often say "my weight is $50\text{ kg}$." In science, however, <strong>mass and weight are two fundamentally different physical quantities</strong>:</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.88rem;">
  <thead>
    <tr style="border-bottom: 2px solid #38bdf8; color: #38bdf8;">
      <th style="padding: 0.4rem; text-align: left;">Property</th>
      <th style="padding: 0.4rem; text-align: left;">Mass ($m$)</th>
      <th style="padding: 0.4rem; text-align: left;">Weight ($W$)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
      <td style="padding: 0.4rem; font-weight: bold; color: #38bdf8;">Definition</td>
      <td style="padding: 0.4rem;">Amount of matter contained in an object</td>
      <td style="padding: 0.4rem;">Gravitational force pulling on the object</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
      <td style="padding: 0.4rem; font-weight: bold; color: #f59e0b;">Physical Nature</td>
      <td style="padding: 0.4rem;">Scalar quantity (magnitude only)</td>
      <td style="padding: 0.4rem;"><strong>Vector Force</strong> (directed downward toward Earth)</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
      <td style="padding: 0.4rem; font-weight: bold; color: #10b981;">SI Unit</td>
      <td style="padding: 0.4rem;"><strong>Kilogram ($\text{kg}$)</strong> or gram ($\text{g}$)</td>
      <td style="padding: 0.4rem;"><strong>Newton ($\text{N}$)</strong></td>
    </tr>
    <tr>
      <td style="padding: 0.4rem; font-weight: bold; color: #a855f7;">Constancy</td>
      <td style="padding: 0.4rem;"><strong>Constant everywhere</strong> in the universe</td>
      <td style="padding: 0.4rem;"><strong>Varies</strong> depending on local gravitational field ($g$)</td>
    </tr>
  </tbody>
</table>

<h4>The Mathematical Relationship</h4>
<p style="text-align: center; font-size: 1.25rem; font-weight: bold; color: #38bdf8;">
  $$W = m \cdot g$$
</p>
<p>Where $m$ is mass in $\text{kg}$, and $g$ is the local acceleration due to gravity ($\approx 9.8\text{ N/kg}$ or $\text{m/s}^2$ on Earth).</p>
<p><em>Example:</em> An astronaut with a mass of $60\text{ kg}$ weighs about <strong>$588\text{ N}$ on Earth</strong>. On the Moon, where gravity is one-sixth ($g_{\\text{moon}} \\approx 1.63\\text{ m/s}^2$), her mass is still exactly <strong>$60\text{ kg}$</strong>, but her weight drops to only <strong>$98\text{ N}$</strong>!</p>
""",
        "vocabulary": [
            {"word": "Mass", "definition": "The measure of the amount of matter contained in a body; an invariant scalar measured in kilograms (kg)."},
            {"word": "Weight", "definition": "The gravitational force exerted on an object by Earth or another celestial body; a vector measured in newtons (N)."},
            {"word": "Scalar vs. Vector", "definition": "A scalar has magnitude only (mass); a vector has both magnitude and direction (weight acting downward)."},
            {"word": "Lunar Gravity", "definition": "The Moon's gravitational pull, which is approximately one-sixth ($\\approx 16.6\\%$) of Earth's surface gravity."}
        ],
        "sim_id": "mass_vs_weight_sim",
        "checkpoints": [
            {
                "question": "If an object has a mass of 10 kg on Earth, what will its mass be on the Moon where gravity is 1/6th as strong?",
                "options": [
                    "1.67 kg",
                    "Exactly 10 kg, because mass remains constant everywhere",
                    "60 kg",
                    "0 kg"
                ],
                "correct": 1,
                "explanation": "Mass is the amount of matter in an object and never changes with location, whereas weight varies with gravity.",
                "solution": "Mass invariance: $m = 10\\text{ kg}$ everywhere in the universe."
            },
            {
                "question": "What is the correct SI unit of weight in physics?",
                "options": [
                    "Kilogram (kg)",
                    "Newton (N)",
                    "Liter (L)",
                    "Meter per second (m/s)"
                ],
                "correct": 1,
                "explanation": "Because weight is a gravitational force, its standard SI unit is the newton (N).",
                "solution": "Weight is a force; therefore its SI unit is the Newton (N)."
            }
        ]
    },

    # SLIDE 11
    {
        "id": 11,
        "title": "Spring Balance Mechanics",
        "tag": "Measurement Instrument • Hooke's Elasticity",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "How do scientists and market vendors measure weight accurately? With a spring balance! When you hang a load, Earth's gravity stretches a calibrated steel spring inside. Let's see how spring balance mechanics work.",
        "theory": r"""
<h3>The Working of a Spring Balance</h3>
<p>A <strong>spring balance</strong> is a simple yet precise mechanical instrument used to measure the gravitational pull (weight or force) exerted on an object.</p>

<h4>Core Construction</h4>
<ul>
  <li><strong>Helical Steel Spring:</strong> Inside a metal or plastic protective case is a coiled steel spring attached at the top to a fixed ring.</li>
  <li><strong>Pointer and Hook:</strong> The lower end of the spring is attached to a pointer that slides along a vertical graduated scale, terminating in a load hook at the bottom.</li>
  <li><strong>Protective Enclosure:</strong> Prevents the spring from getting snagged, damaged, or overstretched past its elastic limit.</li>
</ul>

<h4>The Principle: Hooke's Law of Elasticity</h4>
<p>The operation of a spring balance is based on <strong>Hooke's Law</strong>: <em>The stretching (extension, $\Delta x$) of a coiled spring is directly proportional to the downward pulling force ($F$) applied to it, as long as its elastic limit is not exceeded:</em></p>
<p style="text-align: center; font-weight: bold; color: #f59e0b;">
  $$F = k \cdot \Delta x$$
</p>
<p>Where $k$ is the spring stiffness constant. If hanging $1\text{ N}$ stretches the spring by $1\text{ cm}$, then hanging $2\text{ N}$ will stretch it by exactly $2\text{ cm}$, and $5\text{ N}$ by $5\text{ cm}$!</p>

<h4>Dual Scale Calibration</h4>
<p>Most commercial spring balances feature two adjacent scales: one calibrated directly in <strong>Newtons (N)</strong> for measuring force/weight, and another calibrated in <strong>grams (g)</strong> or <strong>kilograms (kg)</strong> representing the corresponding mass under Earth's standard gravity ($100\text{g} \approx 1\text{N}$).</p>
""",
        "vocabulary": [
            {"word": "Spring Balance", "definition": "A device used to measure force or weight by observing the stretching extension of a calibrated coiled spring."},
            {"word": "Hooke's Law", "definition": "A physical principle stating that the extension of an elastic spring is directly proportional to the applied tensile force ($F = k \\Delta x$)."},
            {"word": "Elastic Limit", "definition": "The maximum force a spring can withstand without suffering permanent mechanical deformation."},
            {"word": "Graduated Scale", "definition": "A calibrated ruler with marked unit intervals (Newtons and grams) indicating pointer displacement."}
        ],
        "sim_id": "spring_balance_sim",
        "checkpoints": [
            {
                "question": "On what fundamental physical principle does a spring balance operate to measure force?",
                "options": [
                    "The electrical resistance of copper wires",
                    "The extension of a coiled spring is directly proportional to the applied gravitational pulling force",
                    "The chemical evaporation of liquid mercury",
                    "The magnetic repulsion of iron filings"
                ],
                "correct": 1,
                "explanation": "A spring balance works on Hooke's Law: the elongation of its internal spring is directly proportional to the applied force (weight).",
                "solution": "Operation principle: $F = k \\Delta x$ (Hooke's Law of spring extension)."
            },
            {
                "question": "If a weight of 2 N stretches a spring balance by 1.5 cm, how much will a weight of 6 N stretch the same spring within its elastic limit?",
                "options": [
                    "1.5 cm",
                    "3.0 cm",
                    "4.5 cm",
                    "12.0 cm"
                ],
                "correct": 2,
                "explanation": "Since force triples ($2\\text{ N} \\times 3 = 6\\text{ N}$), the spring extension also triples: $1.5\\text{ cm} \\times 3 = 4.5\\text{ cm}$.",
                "solution": "Extension ratio: $\\Delta x_2 = \\frac{6}{2} \\times 1.5\\text{ cm} = 3 \\times 1.5 = 4.5\\text{ cm}$."
            }
        ]
    },

    # SLIDE 12
    {
        "id": 12,
        "title": "Upthrust & Buoyant Force",
        "tag": "Fluid Mechanics • Upward Hydrostatic Push",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Try pushing an empty plastic bottle or a football down into a bucket of water. You can feel a powerful upward force resisting your push and popping the bottle straight up! That upward fluid force is called upthrust or buoyant force.",
        "theory": r"""
<h3>The Upward Force in Liquids: Upthrust</h3>
<p>When you submerge an object in a liquid, the liquid exerts an upward mechanical push on the object. This upward force exerted by any liquid or fluid on an object placed or immersed in it is called the <strong>Upthrust</strong> or <strong>Buoyant Force ($F_b$)</strong>.</p>

<h4>Why Do Liquids Push Upward? (Hydrostatic Pressure Cause)</h4>
<ol>
  <li><strong>Pressure Increases with Depth:</strong> In any fluid at rest, hydrostatic pressure increases with depth ($P = \rho g h$) due to the weight of the liquid columns above.</li>
  <li><strong>Pressure Differential:</strong> Consider a submerged solid cylinder. The bottom surface of the cylinder is deeper in the water than the top surface.</li>
  <li><strong>Net Upward Resultant:</strong> Consequently, the upward liquid pressure pushing on the bottom of the cylinder is <em>greater</em> than the downward pressure pushing on the top! This vertical pressure imbalance results in a net upward force: the <strong>buoyant force</strong>.</li>
</ol>

<h4>Apparent Loss of Weight</h4>
<p>Because the upward buoyant force actively opposes downward gravity, any object immersed in a liquid feels noticeably lighter than in air:</p>
<p style="text-align: center; font-weight: bold; color: #38bdf8;">
  $$\text{Apparent Weight in Liquid} = \text{True Weight in Air} - \text{Buoyant Force ($F_b$)}$$
</p>
<p>This is why lifting a heavy rock submerged in a bucket of water feels remarkably effortless until the rock breaks the water surface into the air!</p>
""",
        "vocabulary": [
            {"word": "Buoyant Force (Upthrust)", "definition": "The net upward force exerted by a fluid on any object placed or submerged in it."},
            {"word": "Hydrostatic Pressure", "definition": "The pressure exerted by a fluid at rest, which increases linearly with liquid depth ($P = \\rho g h$)."},
            {"word": "Apparent Weight", "definition": "The perceived reduced weight of a submerged body equal to its true weight minus the upward buoyant force."},
            {"word": "Pressure Differential", "definition": "The difference between higher pressure at the submerged bottom and lower pressure at the top, generating upthrust."}
        ],
        "sim_id": "liquid_upthrust_sim",
        "checkpoints": [
            {
                "question": "What is the scientific term for the upward force exerted by a liquid on a submerged object?",
                "options": [
                    "Centripetal force",
                    "Upthrust or Buoyant Force",
                    "Frictional drag",
                    "Electrostatic induction"
                ],
                "correct": 1,
                "explanation": "The upward force exerted by a liquid on an object immersed in it is called upthrust or buoyant force.",
                "solution": "Upward fluid force = Upthrust / Buoyant Force ($F_b$)."
            },
            {
                "question": "Why does a heavy stone feel significantly lighter while submerged inside a bucket of water compared to holding it in air?",
                "options": [
                    "The stone loses some of its atoms to the water",
                    "The upward buoyant force of the water supports a portion of the stone's weight",
                    "Earth's gravity stops working under water",
                    "The water cools the stone down"
                ],
                "correct": 1,
                "explanation": "The upward buoyant force counteracts a portion of the downward gravitational force, reducing the stone's apparent weight.",
                "solution": "Apparent weight = True weight - Buoyant force."
            }
        ]
    },

    # SLIDE 13
    {
        "id": 13,
        "title": "Floating & Sinking Laws",
        "tag": "Equilibrium Conditions • Weight vs. Upthrust",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Drop an iron nail in water and it plunges to the bottom like a stone. Drop an identical-mass piece of cork or wood, and it bobs happily on the surface! Why does an object float or sink? It's a tug-of-war between downward weight and upward buoyancy.",
        "theory": r"""
<h3>The Tug-of-War: Weight vs. Buoyant Force</h3>
<p>When an object is immersed in a liquid, two opposing vertical forces act upon it simultaneously:</p>
<ol>
  <li>The <strong>Downward Gravitational Force (Weight, $W$)</strong> pulling the object toward the bottom.</li>
  <li>The <strong>Upward Buoyant Force (Upthrust, $F_b$)</strong> pushing the object toward the surface.</li>
</ol>

<h4>The Three Conditions for Floating and Sinking</h4>
<ul>
  <li><strong>Condition 1: Sinking ($W > F_b$)</strong><br>
    If the downward gravitational force (weight) is <em>greater</em> than the maximum upward buoyant force the liquid can provide, the net force is directed downward. The object accelerates downward and <strong>sinks to the bottom</strong> (e.g., an iron nail, a pebble, or a gold ring in water).</li>
  <li><strong>Condition 2: Floating ($W = F_b$)</strong><br>
    If the upward buoyant force <em>equals</em> the object's downward weight, the forces are in perfect equilibrium ($\sum F_y = 0$). The object <strong>floats partially submerged</strong> at the surface (e.g., a wooden log, an ice cube, or a hollow plastic ball).</li>
  <li><strong>Condition 3: Neutral Buoyancy</strong><br>
    If the average density of the object exactly matches the density of the liquid, the buoyant force equals weight when completely submerged. The object remains suspended at any depth without sinking or bobbing up (like a scuba diver or a submarine).</li>
</ul>

<h4>The Role of Density ($\rho$)</h4>
<p>An object sinks if its density is greater than the liquid's density ($\rho_{\\text{object}} > \rho_{\\text{liquid}}$). An object floats if its density is less than the liquid's density ($\rho_{\\text{object}} < \rho_{\\text{liquid}}$)!</p>
""",
        "vocabulary": [
            {"word": "Condition for Sinking", "definition": "Occurs when an object's downward weight exceeds the maximum upward buoyant force ($W > F_b$) or $\\rho_{\\text{object}} > \\rho_{\\text{liquid}}$."},
            {"word": "Condition for Floating", "definition": "Occurs when upward buoyant force balances the object's weight ($F_b = W$) or $\\rho_{\\text{object}} < \\rho_{\\text{liquid}}$."},
            {"word": "Neutral Buoyancy", "definition": "A state of hydrostatic equilibrium where an object neither sinks nor floats, remaining suspended at a fixed depth."},
            {"word": "Density ($\\rho$)", "definition": "Mass per unit volume ($\\rho = m/V$); determines whether a substance floats or sinks in a given fluid."}
        ],
        "sim_id": "floating_sinking_sim",
        "checkpoints": [
            {
                "question": "Under what physical condition will an object sink to the bottom when placed in a liquid?",
                "options": [
                    "When the upward buoyant force is equal to the object's weight",
                    "When the downward gravitational force (weight) is greater than the upward buoyant force",
                    "When the object has zero mass",
                    "When the liquid is boiling"
                ],
                "correct": 1,
                "explanation": "An object sinks when its downward weight exceeds the upward buoyant force ($W > F_b$), producing a net downward force.",
                "solution": "Sinking condition: Downward Weight ($W$) > Upward Buoyant Force ($F_b$)."
            },
            {
                "question": "A piece of pine wood has a density of $0.5\\text{ g/cm}^3$ and pure water has a density of $1.0\\text{ g/cm}^3$. Will the wood float or sink in water?",
                "options": [
                    "It will sink to the very bottom immediately",
                    "It will float with approximately half of its volume submerged",
                    "It will turn into liquid water",
                    "It will bounce completely out of the container"
                ],
                "correct": 1,
                "explanation": "Because the wood's density ($0.5\\text{ g/cm}^3$) is less than water's density ($1.0\\text{ g/cm}^3$), it floats with $0.5/1.0 = 50\\%$ of its volume submerged.",
                "solution": "Density comparison: $\\rho_{\\text{wood}} < \\rho_{\\text{water}} \\rightarrow$ Floats with fraction $\\rho_{\\text{wood}}/\\rho_{\\text{water}} = 50\\%$ submerged."
            }
        ]
    },

    # SLIDE 14
    {
        "id": 14,
        "title": "Archimedes' Principle",
        "tag": "Historic Discovery • Displaced Liquid Law",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "'Eureka! Eureka!' shouted the ancient Greek scientist Archimedes as he stepped into a full bathtub and watched water overflow. He realized that the water displaced equals the volume of his submerged body and reveals the buoyant force!",
        "theory": r"""
<h3>The Eureka Discovery</h3>
<p>In the 3rd century BCE in Syracuse (Sicily), the Greek mathematician and scientist <strong>Archimedes</strong> was tasked by King Hiero II to determine whether a royal crown was made of pure gold or adulterated with cheaper silver—without melting the crown.</p>
<p>While stepping into a public bath filled to the brim, Archimedes observed that water overflowed onto the floor, and simultaneously felt his body become lighter. He realized that the volume of water displaced was equal to the volume of his submerged body, famously shouting <em>'Eureka!'</em> ('I have found it!').</p>

<h3>Archimedes' Principle Stated</h3>
<p><strong>When an object is wholly or partially immersed in a fluid, it experiences an upward buoyant force that is equal to the weight of the fluid displaced by the object.</strong></p>

<h4>Mathematical Formulation</h4>
<p style="text-align: center; font-size: 1.25rem; font-weight: bold; color: #38bdf8;">
  $$F_b = W_{\text{fluid displaced}} = m_{\text{fluid}} \cdot g = \rho_{\text{fluid}} \cdot V_{\text{submerged}} \cdot g$$
</p>
<ul>
  <li>$\rho_{\text{fluid}}$ is the density of the liquid (e.g., $1,000\text{ kg/m}^3$ for water).</li>
  <li>$V_{\text{submerged}}$ is the volume of the immersed portion of the object.</li>
  <li>$g$ is the acceleration due to gravity ($9.8\text{ m/s}^2$).</li>
</ul>
<p><em>Key Takeaway:</em> The buoyant force depends <strong>strictly on the volume of displaced liquid and the liquid's density</strong>—it does NOT depend on the mass, density, or material of the submerged object itself!</p>
""",
        "vocabulary": [
            {"word": "Archimedes' Principle", "definition": "A physical law stating that the upward buoyant force on a submerged body equals the weight of the fluid it displaces."},
            {"word": "Displaced Liquid", "definition": "The exact volume of liquid pushed aside or overflowing when an object is immersed into a full vessel."},
            {"word": "Submerged Volume ($V$)", "definition": "The three-dimensional volume of the portion of an object positioned below the liquid surface line."},
            {"word": "Eureka", "definition": "The Greek exclamation meaning 'I have found it!', shouted by Archimedes upon discovering his buoyancy principle."}
        ],
        "sim_id": "archimedes_principle_sim",
        "checkpoints": [
            {
                "question": "According to Archimedes' Principle, the upward buoyant force experienced by an immersed object is exactly equal to what quantity?",
                "options": [
                    "The total atmospheric air pressure above the container",
                    "The weight of the fluid displaced by the object",
                    "The total depth of the ocean floor",
                    "The surface area of the container walls"
                ],
                "correct": 1,
                "explanation": "Archimedes' Principle states that the buoyant force equals the weight of the fluid displaced by the immersed body.",
                "solution": "Archimedes' Principle: $F_b = W_{\\text{displaced fluid}} = \\rho_{\\text{fluid}} V_{\\text{submerged}} g$."
            },
            {
                "question": "A solid steel cube displaces 200 mL of water when fully submerged. If 200 mL of water weighs 1.96 N, what is the buoyant force acting on the steel cube?",
                "options": [
                    "0 N",
                    "1.96 N upward",
                    "19.6 N downward",
                    "200 N"
                ],
                "correct": 1,
                "explanation": "By Archimedes' Principle, buoyant force equals the weight of the displaced liquid, which is $1.96\\text{ N}$ upward.",
                "solution": "$F_b = W_{\\text{displaced water}} = 1.96\\text{ N}$ directed vertically upward."
            }
        ]
    },

    # SLIDE 15
    {
        "id": 15,
        "title": "Ships, Submarines & Density",
        "tag": "Engineering Applications • Hollow Hulls & Ballast",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "A tiny solid iron nail weighs only 5 grams and sinks instantly, yet a colossal 100,000-ton aircraft carrier made of solid steel floats effortlessly across oceans! How is this possible? Archimedes' Principle and hollow hull design hold the answer.",
        "theory": r"""
<h3>The Paradox of Iron Ships</h3>
<p>The density of solid iron/steel is roughly <strong>$7.8\text{ g/cm}^3$</strong>, which is nearly eight times denser than water ($1.0\text{ g/cm}^3$). A solid iron block sinks immediately. Why, then, do giant steel ships float?</p>

<h4>Hollow Hull Architecture</h4>
<ul>
  <li><strong>Trapped Air Volume:</strong> A ship is not a solid block of iron. It is built as a gigantic <strong>hollow shell</strong> containing vast volumes of empty air in cargo holds, passenger cabins, and engine bays.</li>
  <li><strong>Average Density:</strong> The overall average density of the ship (total mass of steel + air divided by total volume) is <strong>far less than the density of water ($1.0\text{ g/cm}^3$)</strong>!</li>
  <li><strong>Massive Displaced Water:</strong> The wide, curved hull displaces an enormous volume of water. The weight of this displaced water creates a tremendous upward buoyant force that easily balances the massive 100,000-ton weight of the ship!</li>
</ul>

<h4>How Submarines Dive and Surface</h4>
<p>Submarines use specialized <strong>ballast tanks</strong> to deliberately alter their average density:</p>
<ol>
  <li><strong>To Dive:</strong> Vents open, allowing seawater to flood into the ballast tanks while air escapes. The submarine's average density becomes greater than seawater, and it sinks smoothly to desired depths.</li>
  <li><strong>To Surface:</strong> High-pressure compressed air is pumped into the ballast tanks, blowing seawater out through bottom valves. The submarine's average density drops below seawater, and buoyant force pushes it back to the ocean surface!</li>
</ol>
""",
        "vocabulary": [
            {"word": "Average Density", "definition": "The total mass of an object (including internal air cavities) divided by its total exterior volume."},
            {"word": "Hollow Hull", "definition": "The wide, air-filled outer shell of a ship designed to displace a large volume of water while keeping average density low."},
            {"word": "Ballast Tanks", "definition": "Internal compartments in submarines that can be flooded with water to dive or filled with air to surface."},
            {"word": "Plimsoll Line", "definition": "A reference mark on a ship's hull indicating the maximum legal depth to which it may be safely loaded in various water densities."}
        ],
        "sim_id": "ship_submarine_density_sim",
        "checkpoints": [
            {
                "question": "Why does a 100,000-ton steel ocean liner float on seawater while a small solid steel nail sinks?",
                "options": [
                    "The ocean liner is painted with anti-gravity paint",
                    "The ocean liner has a hollow hull containing air, making its overall average density much less than water",
                    "Seawater only attracts small objects",
                    "The ship's engines push it out of the water"
                ],
                "correct": 1,
                "explanation": "A ship's hollow hull encloses vast amounts of air, reducing its average density below that of water and displacing sufficient water to float.",
                "solution": "Hollow architecture: $\\rho_{\\text{average}} = \\frac{m_{\\text{steel}} + m_{\\text{air}}}{V_{\\text{total}}} < \\rho_{\\text{water}} \\rightarrow$ Ship floats."
            },
            {
                "question": "How does a submarine submerge underwater from the ocean surface?",
                "options": [
                    "By turning its propellers backward",
                    "By flooding its ballast tanks with seawater, making its average density greater than the surrounding water",
                    "By dropping anchor weights to the sea floor",
                    "By turning off its internal lighting"
                ],
                "correct": 1,
                "explanation": "Flooding ballast tanks with seawater increases the submarine's total mass and average density, allowing downward weight to exceed upthrust.",
                "solution": "Submarine diving mechanism: Flooding ballast tanks with water increases average density above surrounding seawater."
            }
        ]
    },

    # SLIDE 16
    {
        "id": 16,
        "title": "Master Force Matrix",
        "tag": "Synthesis • Grand Classification Matrix",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Brilliant progress! You have explored the entire universe of forces—from muscular pulls and microscopic friction to magnetic fields, gravity, mass vs. weight, and Archimedes' buoyancy. Let's synthesize everything into a master reference matrix.",
        "theory": r"""
<h3>The Comprehensive Force Synthesis Matrix</h3>
<p>Below is the complete conceptual summary of Chapter 5 for your review:</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.82rem;">
  <thead>
    <tr style="border-bottom: 2px solid #38bdf8; color: #38bdf8;">
      <th style="padding: 0.35rem; text-align: left;">Force Type</th>
      <th style="padding: 0.35rem; text-align: left;">Category</th>
      <th style="padding: 0.35rem; text-align: left;">Origin / Mechanism</th>
      <th style="padding: 0.35rem; text-align: left;">Key Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #f59e0b;">Muscular Force</td>
      <td style="padding: 0.35rem;">Contact</td>
      <td style="padding: 0.35rem;">Actin/myosin muscle contraction</td>
      <td style="padding: 0.35rem;">Skeletal labor, peristalsis, heart blood pump</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #f59e0b;">Frictional Force</td>
      <td style="padding: 0.35rem;">Contact</td>
      <td style="padding: 0.35rem;">Interlocking microscopic asperities</td>
      <td style="padding: 0.35rem;">Always opposes relative motion; fluid drag</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #a855f7;">Magnetic Force</td>
      <td style="padding: 0.35rem;">Non-Contact</td>
      <td style="padding: 0.35rem;">Magnetic fields around poles</td>
      <td style="padding: 0.35rem;">Like poles repel, unlike attract; acts at distance</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #a855f7;">Electrostatic Force</td>
      <td style="padding: 0.35rem;">Non-Contact</td>
      <td style="padding: 0.35rem;">Frictional static charge transfer</td>
      <td style="padding: 0.35rem;">Like charges repel, unlike attract; polarizes neutral</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
      <td style="padding: 0.35rem; font-weight: bold; color: #a855f7;">Gravitational Force</td>
      <td style="padding: 0.35rem;">Non-Contact</td>
      <td style="padding: 0.35rem;">Planetary mass attraction</td>
      <td style="padding: 0.35rem;">Strictly attractive; weight $W = mg$</td>
    </tr>
    <tr>
      <td style="padding: 0.35rem; font-weight: bold; color: #38bdf8;">Buoyant Force ($F_b$)</td>
      <td style="padding: 0.35rem;">Contact (Fluid)</td>
      <td style="padding: 0.35rem;">Hydrostatic depth pressure differential</td>
      <td style="padding: 0.35rem;">Archimedes: $F_b = \text{weight of displaced fluid}$</td>
    </tr>
  </tbody>
</table>

<h4>Core Scientific Invariances</h4>
<ul>
  <li><strong>SI Unit of Force & Weight:</strong> Newton ($\text{N}$).</li>
  <li><strong>Mass:</strong> Invariant scalar ($\text{kg}$), independent of gravity.</li>
  <li><strong>Floating Condition:</strong> Upward Buoyant Force = Downward Weight ($F_b = W$) or $\rho_{\text{object}} \le \rho_{\text{liquid}}$.</li>
</ul>
""",
        "vocabulary": [
            {"word": "Synthesis Matrix", "definition": "A unified comparative overview integrating all classifications, mechanisms, and formulas of forces."},
            {"word": "Hydrostatic Equilibrium", "definition": "The stable balance between downward gravitational weight and upward fluid buoyant force."},
            {"word": "Universal Invariant", "definition": "A physical quantity (such as mass) whose numerical value remains constant across all environments."},
            {"word": "Force Polygon", "definition": r"A graphical vector representation demonstrating how balanced forces sum to zero ($\sum \vec{F} = 0$)."}
        ],
        "sim_id": "force_matrix_synthesis_sim",
        "checkpoints": [
            {
                "question": "Which of the following pairs of forces are BOTH classified as NON-CONTACT forces?",
                "options": [
                    "Muscular force and friction",
                    "Gravitational force and magnetic force",
                    "Tension in a rope and air drag",
                    "Friction and upthrust"
                ],
                "correct": 1,
                "explanation": "Gravitational force and magnetic force both act across space without requiring physical contact.",
                "solution": "Non-contact pair: Gravitational and Magnetic forces."
            },
            {
                "question": "Under Earth's standard gravity, approximately what mass experiences a gravitational force (weight) of 1 Newton?",
                "options": [
                    "1,000 kilograms (a car)",
                    "100 grams (about one medium apple)",
                    "1 milligram (a dust grain)",
                    "10 kilograms (a heavy bowling ball)"
                ],
                "correct": 1,
                "explanation": r"Since $W = m \cdot g$, $1\text{ N} \approx 0.102\text{ kg} \approx 100\text{ grams}$, roughly the weight of an apple.",
                "solution": "$m = W / g = 1\\text{ N} / 9.8\\text{ m/s}^2 \\approx 0.102\\text{ kg} = 102\\text{ g}$."
            }
        ]
    },

    # SLIDE 17 - MASTERY CHALLENGE PART I (Q1-Q10)
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "tag": "Comprehensive Review • Questions 1 to 10",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Congratulations on completing the core lessons! Now, test your scientific understanding. Tackle these 10 in-depth questions on the definition of force, its four effects, and contact forces like muscular force and friction. Click the solution button to review the full step-by-step breakdown!",
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10
    },

    # SLIDE 18 - MASTERY CHALLENGE PART II (Q11-Q20)
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "tag": "Comprehensive Review • Questions 11 to 20",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Keep up the great momentum! Part II focuses on fluid drag, streamlining, magnetic poles, electrostatic charges, and universal gravitational attraction. Analyze each problem carefully!",
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10
    },

    # SLIDE 19 - MASTERY CHALLENGE PART III (Q21-Q30)
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "tag": "Comprehensive Review • Questions 21 to 30",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "Welcome to Part III! Here we examine the crucial distinction between mass and weight, Hooke's law in spring balances, and the origin of upthrust in fluids. Think through the physics!",
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10
    },

    # SLIDE 20 - MASTERY CHALLENGE PART IV (Q31-Q40)
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "tag": "Comprehensive Review • Questions 31 to 40",
        "badge": "Class 8 Science • Chapter 5",
        "avatar_dialogue": "The final frontier! Part IV challenges your mastery of floating and sinking conditions, Archimedes' Principle, ship design, and submarine ballast systems. Solve these last 10 inquiries to achieve complete chapter mastery!",
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
        "question": "Which of the following statements provides the most accurate scientific definition of a force?",
        "options": [
            "A form of thermal energy contained inside an atom",
            "A push or a pull applied on an object resulting from its interaction with another object",
            "The physical volume occupied by a solid object",
            "The speed at which an object travels across a flat surface"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Definition:</strong> In physics, a force is fundamentally defined as a push or a pull exerted upon an object.</li>
  <li><strong>Interaction:</strong> Forces do not exist in isolation; they arise strictly from an interaction between at least two bodies.</li>
  <li><strong>SI Unit:</strong> The standard unit of force is the newton ($\text{N}$).</li>
  <li><strong>Conclusion:</strong> Option 2 accurately captures both the push/pull nature and the mutual interaction requirement.</li>
</ol>
"""
    },

    # Q2
    {
        "id": 2,
        "question": "What is the standard SI unit of force, and what symbol represents it?",
        "options": [
            "Joule, represented by J",
            "Newton, represented by N",
            "Pascal, represented by Pa",
            "Watt, represented by W"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>SI Standard:</strong> The International System of Units (SI) designates the <strong>newton</strong> as the coherent derived unit of force.</li>
  <li><strong>Symbol:</strong> It is symbolized by a capital <strong>N</strong> in honor of Sir Isaac Newton.</li>
  <li><strong>Equivalence:</strong> $1\text{ N} = 1\text{ kg}\cdot\text{m/s}^2$.</li>
</ol>
"""
    },

    # Q3
    {
        "id": 3,
        "question": "A force can produce several distinct effects on an object. Which of the following is NOT an effect produced by a force?",
        "options": [
            "Make an object move from a state of rest",
            "Change the speed or direction of motion of a moving body",
            "Change the chemical atomic number of the elements inside the object",
            "Bring about a change in the physical shape of an object"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Mechanical Effects of Force:</strong>
    <ul>
      <li>Change state of rest to motion.</li>
      <li>Change magnitude of speed (acceleration or deceleration).</li>
      <li>Change direction of motion.</li>
      <li>Deform or alter physical shape.</li>
    </ul>
  </li>
  <li><strong>Chemical Identity:</strong> Changing the atomic number requires nuclear reactions (fission/fusion), which is not a standard mechanical effect of an applied force.</li>
</ol>
"""
    },

    # Q4
    {
        "id": 4,
        "question": "A heavy wooden crate rests motionless on a level warehouse floor. Why does it not begin moving on its own?",
        "options": [
            "Because an object at rest requires an external unbalanced force to initiate motion",
            "Because Earth's gravity has disappeared inside the warehouse",
            "Because air molecules are pushing it down with infinite pressure",
            "Because wooden objects cannot move"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Newton's First Law / Inertia:</strong> A stationary body possesses inertia of rest.</li>
  <li><strong>Equilibrium:</strong> Downward gravity is balanced by the upward normal reaction force from the floor.</li>
  <li><strong>Motion Requirement:</strong> An object cannot change its state of rest without the application of an external, unbalanced force (a push or pull).</li>
</ol>
"""
    },

    # Q5
    {
        "id": 5,
        "question": "When a tennis player hits an incoming tennis ball with a racquet, what effect does the racquet's force produce on the ball?",
        "options": [
            "It turns the ball into liquid rubber",
            "It changes both the speed and the direction of motion of the ball",
            "It eliminates the ball's mass completely",
            "It only changes the color of the ball"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Incoming Ball:</strong> The ball approaches with a velocity vector pointing toward the player.</li>
  <li><strong>Racquet Impact:</strong> The racquet applies a large impulse force over a fraction of a second.</li>
  <li><strong>Outcome:</strong> The ball reverses direction and accelerates back across the net, demonstrating a combined change in speed and direction.</li>
</ol>
"""
    },

    # Q6
    {
        "id": 6,
        "question": "Which of the following scenarios illustrates a force causing a change in the SHAPE of an object?",
        "options": [
            "Squeezing an inflated rubber balloon between your two palms",
            "A goalkeeper catching a penalty kick",
            "A stone accelerating downward when dropped from a bridge",
            "A cricket ball rolling across grass until it stops"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Catching / Falling / Rolling:</strong> All involve changes in velocity or state of motion.</li>
  <li><strong>Squeezing Balloon:</strong> The opposing forces exerted by the palms compress the elastic rubber walls, altering its geometric shape from spherical to flattened (deformation).</li>
</ol>
"""
    },

    # Q7
    {
        "id": 7,
        "question": "Why is muscular force strictly classified as a CONTACT force?",
        "options": [
            "Because muscles can exert magnetic fields across empty rooms",
            "Because physical contact between the body (or a tool held by the body) and the object is required to apply the force",
            "Because muscular force only operates under electric lights",
            "Because muscles only work inside water"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Contact Force Definition:</strong> A force that requires physical contact between the interacting bodies.</li>
  <li><strong>Muscular Action:</strong> Muscles contract internally, pulling on tendons and bones, which must make mechanical contact (directly or via a stick/rope) with an external load to push or pull it.</li>
</ol>
"""
    },

    # Q8
    {
        "id": 8,
        "question": "How does muscular force contribute to the internal functioning of the human digestive system?",
        "options": [
            "By cooling the stomach with cold air",
            "Through peristalsis—wave-like muscular contractions of the alimentary canal pushing food forward",
            "By magnetizing nutrients so they stick to bones",
            "By freezing stomach acid into crystals"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Peristalsis:</strong> The walls of the esophagus, stomach, and intestines are lined with layers of smooth involuntary muscle.</li>
  <li><strong>Rhythmic Contraction:</strong> These muscles contract and relax in coordinated waves, exerting mechanical muscular force that propels digested food along the alimentary canal.</li>
</ol>
"""
    },

    # Q9
    {
        "id": 9,
        "question": "What is the primary microscopic cause of the force of friction between two sliding surfaces?",
        "options": [
            "Chemical bonding that permanently welds the two bodies together",
            "The mechanical interlocking of microscopic ridges, peaks, and valleys (asperities) on the contacting surfaces",
            "Gravitational attraction between individual atomic nuclei",
            "Air molecules being squeezed into a vacuum"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Surface Topography:</strong> No solid surface is perfectly flat at the microscopic scale; all exhibit microscopic asperities (hills and valleys).</li>
  <li><strong>Interlocking:</strong> When two surfaces touch, these asperities nest into one another.</li>
  <li><strong>Frictional Resistance:</strong> Sliding requires shearing or overcoming these interlocked microscopic peaks, creating friction.</li>
</ol>
"""
    },

    # Q10
    {
        "id": 10,
        "question": "A hockey puck slides across rough concrete and across smooth, polished ice. Why does the puck travel much farther on ice?",
        "options": [
            "Ice has no gravitational pull",
            "Polished ice has far fewer and smaller surface irregularities, resulting in significantly lower frictional resistance",
            "Concrete attracts the rubber in the puck with magnetic force",
            "Ice generates a forward pushing force on the puck"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Roughness Factor:</strong> Concrete has coarse, deep microscopic irregularities that interlock aggressively with the puck.</li>
  <li><strong>Ice Properties:</strong> Polished ice is exceptionally smooth and forms a microscopic lubricating water film, minimizing asperity interlocking.</li>
  <li><strong>Result:</strong> Much lower friction allows the puck to glide much farther before coming to rest.</li>
</ol>
"""
    },

    # Q11
    {
        "id": 11,
        "question": "What is the specialized scientific term for the frictional resistance exerted by fluids (liquids and gases) on objects moving through them?",
        "options": [
            "Centrifugal push",
            "Fluid friction or Drag",
            "Magnetic hysteresis",
            "Static electricity"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Fluid Resistance:</strong> As an object travels through air or water, fluid molecules collide with its surface and must be accelerated out of the way.</li>
  <li><strong>Terminology:</strong> This opposing frictional force is called <strong>fluid friction</strong> or <strong>drag</strong>.</li>
</ol>
"""
    },

    # Q12
    {
        "id": 12,
        "question": "Why are commercial jet airplanes, high-speed bullet trains, and racing cars designed with streamlined bodies?",
        "options": [
            "To make them look stylish in advertisements",
            "To allow air to flow smoothly around them with minimal turbulence, drastically reducing fluid drag and saving fuel",
            "To increase the weight of the vehicle so it clings to the ground",
            "To prevent lightning from striking the vehicle"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Blunt vs. Streamlined:</strong> A flat, blunt vehicle creates chaotic swirling eddies and high air pressure in front, creating massive drag.</li>
  <li><strong>Streamlined Geometry:</strong> Tapered, curved profiles guide airflow smoothly along the contours, minimizing wake turbulence.</li>
  <li><strong>Efficiency:</strong> Reduced drag lowers engine workload and significantly cuts fuel consumption.</li>
</ol>
"""
    },

    # Q13
    {
        "id": 13,
        "question": "Which of the following is an example of an organism in nature whose body shape inspired human engineers to design streamlined vehicles?",
        "options": [
            "Birds (like falcons) and aquatic predators (like sharks and dolphins)",
            "Jellyfish and sea anemones",
            "Cactus plants in deserts",
            "Earthworms crawling in soil"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Biomimicry:</strong> Millions of years of natural selection evolved birds for fast flight through air and fish/dolphins for rapid swimming through water.</li>
  <li><strong>Human Design:</strong> Aircraft fuselages, submarine hulls, and bullet train noses are directly modeled on these natural streamlined shapes.</li>
</ol>
"""
    },

    # Q14
    {
        "id": 14,
        "question": "What fundamental law governs the interaction between magnetic poles?",
        "options": [
            "Like poles attract, and unlike poles repel",
            "Like poles repel, and unlike poles attract",
            "All magnetic poles attract all other poles regardless of type",
            "Magnetic poles only interact when heated to red heat"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Poles:</strong> Every magnet has a North (N) and a South (S) pole.</li>
  <li><strong>Like Poles:</strong> $N-N$ or $S-S$ repel each other with an invisible pushing force.</li>
  <li><strong>Unlike Poles:</strong> $N-S$ attract each other with an invisible pulling force.</li>
</ol>
"""
    },

    # Q15
    {
        "id": 15,
        "question": "Why is magnetic force classified as a NON-CONTACT force?",
        "options": [
            "Because a magnet can pull iron objects or push other magnets from a distance without touching them",
            "Because magnets are made of non-conductive plastic",
            "Because magnets cannot be held with bare hands",
            "Because magnetic forces only exist inside vacuum tubes"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Non-Contact Criterion:</strong> Forces that can act across intervening empty space without physical contact.</li>
  <li><strong>Magnetic Field:</strong> A magnet establishes a magnetic field around itself. Another magnetic material placed within this field experiences a force across distance.</li>
</ol>
"""
    },

    # Q16
    {
        "id": 16,
        "question": "What causes an electric charge to build up on a plastic comb when it is run through dry hair?",
        "options": [
            "Friction between the comb and hair transfers microscopic electrons from one material to the other",
            "The comb absorbs liquid moisture from the hair",
            "The hair generates magnetic fields",
            "Chemical acid leaks from the plastic"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Triboelectric Effect:</strong> Frictional rubbing between two different insulating materials causes mechanical contact between surface atoms.</li>
  <li><strong>Electron Transfer:</strong> Electrons are transferred from hair to the comb, giving the comb an excess negative static electric charge.</li>
</ol>
"""
    },

    # Q17
    {
        "id": 17,
        "question": "What happens when two negatively charged rubber balloons are brought near each other without touching?",
        "options": [
            "They attract and snap tightly together",
            "They repel each other because like charges push each other away",
            "They neutralize each other and become water",
            "They emit bright green laser light"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Law of Electrostatics:</strong> Like electric charges (negative-negative or positive-positive) repel each other.</li>
  <li><strong>Result:</strong> The two negatively charged balloons push away from each other across the air gap via non-contact electrostatic repulsion.</li>
</ol>
"""
    },

    # Q18
    {
        "id": 18,
        "question": "Why does a negatively charged comb attract NEUTRAL, uncharged scraps of paper?",
        "options": [
            "Because the comb's electric field polarizes the paper scraps, attracting the near positive charges",
            "Because paper is made of solid iron",
            "Because air pressure blows the paper toward the comb",
            "Because the comb becomes a permanent magnet"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Induction / Polarization:</strong> The negatively charged comb repels electrons in the paper atoms away, leaving the near side with an induced positive charge.</li>
  <li><strong>Net Attraction:</strong> Since the attractive positive charges are closer to the comb than the repelled negative charges, a net electrostatic attraction pulls the paper upward.</li>
</ol>
"""
    },

    # Q19
    {
        "id": 19,
        "question": "What unique characteristic distinguishes gravitational force from both magnetic and electrostatic forces?",
        "options": [
            "Gravitational force is ALWAYS attractive and never repulsive",
            "Gravitational force only acts through direct physical contact",
            "Gravitational force only exists inside clouds",
            "Gravitational force can be shielded with aluminum foil"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Magnetic & Electrostatic:</strong> Both exhibit dual polarity (like poles/charges repel, unlike attract).</li>
  <li><strong>Gravity:</strong> Mass possesses only one gravitational "charge" (positive mass). Therefore, gravitational force in the universe is strictly attractive.</li>
</ol>
"""
    },

    # Q20
    {
        "id": 20,
        "question": "What keeps the Earth's atmosphere from drifting off into the vacuum of space and holds the Moon in orbit around the Earth?",
        "options": [
            "Earth's gravitational force",
            "Electrostatic attraction from polar ice caps",
            "The physical friction of clouds",
            "Solar wind pushing from the Sun"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Planetary Mass:</strong> Earth's immense mass ($5.97 \times 10^{24}\text{ kg}$) produces a powerful gravitational field.</li>
  <li><strong>Atmospheric Retention:</strong> Gravity pulls atmospheric gas molecules toward Earth, preventing their thermal escape into space.</li>
  <li><strong>Orbital Mechanics:</strong> Earth's gravitational pull provides the centripetal force holding the Moon in stable elliptical orbit.</li>
</ol>
"""
    },

    # Q21
    {
        "id": 21,
        "question": "What is the fundamental scientific difference between MASS and WEIGHT?",
        "options": [
            "Mass is a force, while weight is a measure of volume",
            "Mass is the amount of matter in an object and is constant everywhere; weight is the gravitational force acting on that matter and varies with gravity",
            "Mass is measured in Newtons, while weight is measured in kilograms",
            "There is no difference; they are identical quantities in physics"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Mass ($m$):</strong> Invariant scalar quantity representing the quantity of matter contained within an object (SI unit: $\text{kg}$).</li>
  <li><strong>Weight ($W$):</strong> Vector force representing the gravitational pull on that mass ($W = mg$, SI unit: $\text{N}$).</li>
  <li><strong>Location:</strong> Mass remains constant across the universe; weight varies directly with local gravitational acceleration $g$.</li>
</ol>
"""
    },

    # Q22
    {
        "id": 22,
        "question": "An astronaut has a mass of 72 kg on Earth. What will his MASS and WEIGHT be on the Moon, where $g_{\\text{moon}} \\approx 1.63\\text{ m/s}^2$ ($g_{\\text{earth}} \\approx 9.8\\text{ m/s}^2$)?",
        "options": [
            "Mass = 12 kg, Weight = 705.6 N",
            "Mass = 72 kg, Weight ≈ 117.4 N",
            "Mass = 72 kg, Weight = 705.6 N",
            "Mass = 0 kg, Weight = 0 N"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Mass Calculation:</strong> Mass is an invariant quantity. Therefore, mass on the Moon is still exactly <strong>$72\text{ kg}$</strong>.</li>
  <li><strong>Weight Calculation:</strong>
    $$W_{\text{moon}} = m \cdot g_{\text{moon}} = 72\text{ kg} \times 1.63\text{ m/s}^2 \approx 117.4\text{ N}$$
  </li>
  <li>On Earth, his weight was $72 \times 9.8 \approx 705.6\text{ N}$. On the Moon, it drops to $\approx 117.4\text{ N}$.</li>
</ol>
"""
    },

    # Q23
    {
        "id": 23,
        "question": "What physical instrument is commonly used to measure force or weight by observing the elongation of a calibrated steel spring?",
        "options": [
            "Beam balance",
            "Spring balance",
            "Barometer",
            "Thermometer"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Spring Balance:</strong> Contains an internal coiled steel spring that extends when a downward force (weight) is applied to its hook.</li>
  <li><strong>Scale:</strong> The extension is measured against a graduated scale calibrated in Newtons (and equivalent grams).</li>
</ol>
"""
    },

    # Q24
    {
        "id": 24,
        "question": "According to Hooke's Law, what is the relationship between the force applied to an elastic spring and its extension within the elastic limit?",
        "options": [
            "The extension is inversely proportional to the force",
            "The extension is directly proportional to the applied force ($F = k \\Delta x$)",
            "The extension is independent of the force",
            "The extension decreases as more force is applied"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Hooke's Law:</strong> Within the elastic limit of a spring, tensile force is directly proportional to displacement:
    $$F = k \cdot \Delta x$$
  </li>
  <li>Doubling the applied force doubles the extension of the spring.</li>
</ol>
"""
    },

    # Q25
    {
        "id": 25,
        "question": "If a spring balance stretches by 2.0 cm under a 5.0 N load, what extension will it exhibit under a 15.0 N load (assuming it remains within its elastic limit)?",
        "options": [
            "2.0 cm",
            "4.0 cm",
            "6.0 cm",
            "10.0 cm"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Proportionality:</strong> $\Delta x \propto F$.</li>
  <li><strong>Ratio:</strong>
    $$\frac{\Delta x_2}{\Delta x_1} = \frac{F_2}{F_1} = \frac{15.0\text{ N}}{5.0\text{ N}} = 3$$
  </li>
  <li><strong>New Extension:</strong>
    $$\Delta x_2 = 3 \times 2.0\text{ cm} = 6.0\text{ cm}$$
  </li>
</ol>
"""
    },

    # Q26
    {
        "id": 26,
        "question": "What is the physical cause of the upward buoyant force (upthrust) experienced by an object submerged in a liquid?",
        "options": [
            "Liquid pressure increases with depth, causing the upward pressure on the bottom of the object to exceed the downward pressure on the top",
            "Liquid molecules magnetically repel solid atoms",
            "The liquid evaporates into gas beneath the object",
            "The object loses its gravitational pull inside water"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Hydrostatic Law:</strong> Fluid pressure increases linearly with depth: $P = \rho g h$.</li>
  <li><strong>Immersed Body:</strong> The bottom surface of the object is located at a greater depth ($h_2 > h_1$) than the top surface.</li>
  <li><strong>Pressure Difference:</strong> Upward force on the bottom ($F_2 = P_2 A$) exceeds downward force on the top ($F_1 = P_1 A$).</li>
  <li><strong>Net Force:</strong> $\Delta F = F_2 - F_1 = \text{Upthrust } (F_b)$.</li>
</ol>
"""
    },

    # Q27
    {
        "id": 27,
        "question": "A metal cylinder weighs 25 N in air. When completely immersed in a beaker of water, it weighs 18 N on a spring balance. What is the magnitude of the buoyant force?",
        "options": [
            "43 N",
            "25 N",
            "7 N",
            "0 N"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Apparent Weight Formula:</strong>
    $$\text{Apparent Weight} = \text{True Weight in Air} - \text{Buoyant Force ($F_b$)}$$
  </li>
  <li><strong>Solving for $F_b$:</strong>
    $$F_b = \text{True Weight} - \text{Apparent Weight} = 25\text{ N} - 18\text{ N} = 7\text{ N}$$
  </li>
  <li>The water exerts an upward buoyant force of $7\text{ N}$.</li>
</ol>
"""
    },

    # Q28
    {
        "id": 28,
        "question": "What must be true about the forces acting on an object that is floating peacefully at the surface of a pond?",
        "options": [
            "The downward gravitational force (weight) is equal to the upward buoyant force",
            "The downward gravitational force is much greater than the buoyant force",
            "There are no forces acting on the object whatsoever",
            "The buoyant force is zero"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Equilibrium:</strong> For an object at rest on the water surface, the net vertical force must be zero: $\sum F_y = 0$.</li>
  <li><strong>Forces:</strong> Downward weight ($W$) is exactly balanced by the upward buoyant force ($F_b$).</li>
  <li>Therefore, $F_b = W$.</li>
</ol>
"""
    },

    # Q29
    {
        "id": 29,
        "question": "Why does a solid iron nail sink in water while a wooden block of the exact same size floats?",
        "options": [
            "The iron nail is heavier than the entire ocean",
            "Iron has a density greater than water ($7.8 > 1.0\\text{ g/cm}^3$), while wood has a density less than water ($0.6 < 1.0\\text{ g/cm}^3$)",
            "Water molecules dissolve iron immediately",
            "Wood contains magnetic repulsion poles"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Density Rule for Sinking:</strong> When $\rho_{\text{object}} > \rho_{\text{liquid}}$, the object's weight exceeds the maximum buoyant force of the displaced volume, and it sinks.</li>
  <li><strong>Density Rule for Floating:</strong> When $\rho_{\text{object}} < \rho_{\text{liquid}}$, the buoyant force equals weight before full immersion, and it floats.</li>
  <li>$\rho_{\text{iron}} \approx 7.8\text{ g/cm}^3 > 1.0\text{ g/cm}^3$ (sinks); $\rho_{\text{wood}} \approx 0.6\text{ g/cm}^3 < 1.0\text{ g/cm}^3$ (floats).</li>
</ol>
"""
    },

    # Q30
    {
        "id": 30,
        "question": "What is Archimedes' Principle?",
        "options": [
            "All moving objects eventually come to rest due to friction",
            "An object wholly or partially immersed in a fluid experiences an upward buoyant force equal to the weight of the fluid displaced by it",
            "Like electric charges repel, and unlike electric charges attract",
            "The pressure of a gas is directly proportional to its temperature"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Historical Statement:</strong> Discovered by Greek scientist Archimedes in the 3rd century BCE.</li>
  <li><strong>Principle:</strong> The upward buoyant force ($F_b$) exerted by a fluid on an immersed body equals the weight of the fluid pushed aside (displaced) by the immersed volume:
    $$F_b = W_{\text{displaced fluid}} = \rho_{\text{fluid}} V_{\text{submerged}} g$$
  </li>
</ol>
"""
    },

    # Q31
    {
        "id": 31,
        "question": "A heavy stone is submerged into a completely full overflow can of water. It causes 350 mL of water to spill into a measuring beaker. What is the VOLUME of the stone?",
        "options": [
            "35 mL",
            "350 mL (or 350 cm³)",
            "3,500 mL",
            "0 mL"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Archimedes' Displacement Insight:</strong> A completely submerged solid object displaces a volume of fluid exactly equal to its own physical volume:
    $$V_{\text{object}} = V_{\text{displaced fluid}}$$
  </li>
  <li>Since $350\text{ mL}$ of water overflowed, the stone's volume is exactly $350\text{ mL}$ (or $350\text{ cm}^3$).</li>
</ol>
"""
    },

    # Q32
    {
        "id": 32,
        "question": "If the 350 mL of displaced water in the previous question has a mass of 0.35 kg, what is the upward buoyant force acting on the stone? ($g = 9.8\\text{ m/s}^2$)",
        "options": [
            "0.35 N",
            "3.43 N",
            "34.3 N",
            "350 N"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Archimedes' Formula:</strong>
    $$F_b = W_{\text{displaced fluid}} = m_{\text{fluid}} \cdot g$$
  </li>
  <li><strong>Calculation:</strong>
    $$F_b = 0.35\text{ kg} \times 9.8\text{ m/s}^2 = 3.43\text{ N}$$
  </li>
  <li>The upward buoyant force acting on the stone is $3.43\text{ N}$.</li>
</ol>
"""
    },

    # Q33
    {
        "id": 33,
        "question": "Why does a 50,000-tonne cargo ship constructed from dense steel float easily in ocean water?",
        "options": [
            "The ship is filled with helium gas tanks",
            "The ship's hollow hull encloses vast volumes of air, making the average density of the entire ship less than the density of seawater",
            "Steel becomes lighter than water when shaped into sheets",
            "Ocean waves push the ship upward mechanically"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Average Density:</strong> $\rho_{\text{average}} = \frac{\text{Total Mass}}{\text{Total Exterior Volume}}$.</li>
  <li><strong>Air Inclusion:</strong> The ship's hollow hull encloses massive air spaces (cargo bays, engine rooms, passenger cabins).</li>
  <li><strong>Result:</strong> Despite the heavy steel, the combined average density is well below $1.025\text{ g/cm}^3$ (seawater density).</li>
  <li>The ship displaces an enormous volume of seawater whose weight balances the ship's 50,000-tonne weight.</li>
</ol>
"""
    },

    # Q34
    {
        "id": 34,
        "question": "How do submarines control their depth to dive beneath the surface and later return to the ocean surface?",
        "options": [
            "By extending and retracting mechanical metal legs",
            "By flooding internal ballast tanks with seawater to dive, and using compressed air to blow water out to surface",
            "By changing the temperature of the ocean water around them",
            "By spinning rapidly in circles"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Diving:</strong> Flooding ballast tanks with seawater increases the submarine's mass, raising average density above seawater ($\rho_{\text{sub}} > \rho_{\text{water}}$) $\rightarrow$ submarine dives.</li>
  <li><strong>Surfacing:</strong> Compressed air forces the seawater out through bottom vents, reducing mass and average density below seawater ($\rho_{\text{sub}} < \rho_{\text{water}}$) $\rightarrow$ buoyant force pushes submarine to the surface.</li>
</ol>
"""
    },

    # Q35
    {
        "id": 35,
        "question": "Does Archimedes' Principle apply ONLY to liquids like water, or does it also apply to gases like air?",
        "options": [
            "It applies only to fresh water in bathtubs",
            "It applies to all fluids, including both liquids and gases (such as air)",
            "It applies only to molten metals in furnaces",
            "It applies only inside vacuum chambers"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Fluids:</strong> Both liquids and gases are fluids with mass and hydrostatic pressure.</li>
  <li><strong>Buoyancy in Air:</strong> An object submerged in air experiences an upward buoyant force equal to the weight of displaced air.</li>
  <li><strong>Application:</strong> This is the exact principle that allows hot air balloons and helium blimps to rise in the atmosphere!</li>
</ol>
"""
    },

    # Q36
    {
        "id": 36,
        "question": "Why does a hot air balloon rise upward into the sky?",
        "options": [
            "Because hot air inside the balloon expands and becomes less dense than the cooler surrounding air, so upward buoyant force exceeds its weight",
            "Because fire has no gravitational mass",
            "Because the fabric of the balloon is repelled by Earth's gravity",
            "Because the wind blows it upward like a kite"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Thermal Expansion:</strong> Heating air inside the balloon causes air molecules to move faster and spread out.</li>
  <li><strong>Density Reduction:</strong> The density of hot air is less than the cold ambient atmospheric air outside.</li>
  <li><strong>Buoyant Equilibrium:</strong> The weight of the large volume of cold air displaced exceeds the total weight of the balloon + hot air, driving it upward.</li>
</ol>
"""
    },

    # Q37
    {
        "id": 37,
        "question": "What happens when an uncharged plastic rod is rubbed with dry wool?",
        "options": [
            "It becomes radioactive",
            "Electrons transfer between the materials, giving the plastic rod a net static electric charge",
            "The rod turns into a permanent magnet with North and South poles",
            "The rod's gravitational mass decreases to zero"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Triboelectricity:</strong> Frictional rubbing causes outer orbital electrons to transfer from wool to the plastic rod.</li>
  <li><strong>Charge Imbalance:</strong> The plastic rod acquires an excess of electrons, becoming negatively charged with static electricity.</li>
</ol>
"""
    },

    # Q38
    {
        "id": 38,
        "question": "A person pushes a 40 kg block across a rough carpet with a forward force of 150 N. The frictional force opposing the block is 100 N. What is the NET forward force acting on the block?",
        "options": [
            "250 N",
            "150 N",
            "50 N",
            "0 N"
        ],
        "correct": 2,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Vector Addition:</strong>
    $$F_{\text{net}} = F_{\text{applied}} - F_{\text{friction}}$$
  </li>
  <li><strong>Calculation:</strong>
    $$F_{\text{net}} = 150\text{ N} - 100\text{ N} = 50\text{ N forward}$$
  </li>
  <li>The block accelerates forward under an unbalanced net force of $50\text{ N}$.</li>
</ol>
"""
    },

    # Q39
    {
        "id": 39,
        "question": "Why does a swimmer float more easily in the salty water of the Dead Sea than in a freshwater swimming pool?",
        "options": [
            "The Dead Sea has no gravity",
            "Salty water has a much higher density than fresh water, generating a greater upward buoyant force for the same submerged volume",
            "Salt water pushes swimmers upward with magnetic force",
            "The Dead Sea is warmer than swimming pools"
        ],
        "correct": 1,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Buoyancy Formula:</strong> $F_b = \rho_{\text{liquid}} V g$.</li>
  <li><strong>Density:</strong> Dissolved salts raise the water density from $1.0\text{ g/cm}^3$ to approx. $1.24\text{ g/cm}^3$.</li>
  <li><strong>Effect:</strong> Displacing a smaller volume of dense saltwater provides enough upthrust to balance human body weight, causing swimmers to float high on the surface.</li>
</ol>
"""
    },

    # Q40
    {
        "id": 40,
        "question": "Which of the following summaries correctly states the three conditions of flotation based on density comparison ($\rho_{\\text{object}}$ vs $\rho_{\\text{fluid}}$)?",
        "options": [
            "If $\rho_{\\text{obj}} > \rho_{\\text{fluid}}$, it sinks; if $\rho_{\\text{obj}} < \rho_{\\text{fluid}}$, it floats; if $\rho_{\\text{obj}} = \rho_{\\text{fluid}}$, it remains neutrally buoyant",
            "All objects sink regardless of density",
            "If $\rho_{\\text{obj}} > \rho_{\\text{fluid}}$, it floats; if $\rho_{\\text{obj}} < \rho_{\\text{fluid}}$, it sinks",
            "Density has no effect on floating or sinking"
        ],
        "correct": 0,
        "solution": r"""
<strong>Step-by-Step Explanation:</strong>
<ol>
  <li><strong>Sinking:</strong> $\rho_{\text{obj}} > \rho_{\text{fluid}} \rightarrow$ Downward weight exceeds maximum buoyant force ($W > F_b$) $\rightarrow$ Sinks.</li>
  <li><strong>Floating:</strong> $\rho_{\text{obj}} < \rho_{\text{fluid}} \rightarrow$ Upthrust balances weight before full immersion $\rightarrow$ Floats.</li>
  <li><strong>Neutral Buoyancy:</strong> $\rho_{\text{obj}} = \rho_{\text{fluid}} \rightarrow$ Stable suspension at any submerged depth.</li>
</ol>
"""
    }
]

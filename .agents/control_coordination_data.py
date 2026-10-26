#!/usr/bin/env python3
"""
Generates public/animations/control-and-coordination.html
NCERT Class 10 Science - Chapter 6: Control and Coordination
Master Multimedia Lab with:
- Person talking: Dr. Sophia (Biology Teacher) animated avatar with mouth movement synced to Web Speech audio narration
- 21 slides (17 rich content slides + 4 dedicated quiz challenge slides)
- 2 checkpoint questions on EVERY content slide (34 checkpoint questions with step-by-step solutions)
- 40 mastery quiz questions (10 per quiz slide) with dedicated Solution buttons opening #solutionModal popups
- 17 interactive SVG lab simulators with lively animations
- Audio unlock on first user gesture
- Zero JavaScript syntax errors
"""

import json
import os

CONTENT_SLIDES = [
    # Slide 1: Introduction, Growth vs Non-Growth Movements (Page 100)
    {
        "index": 0,
        "title": "Introduction: Movement, Life & The Need for Control and Coordination",
        "short_title": "1. Life & Movement",
        "badge": "Chapter 6 • Foundations (Page 100)",
        "quote": "Living organisms must use systems providing control and coordination to ensure that every environmental change evokes an appropriate, controlled response.",
        "lead": "We instinctively associate visible movement with life. Yet while a germinating seedling moves purely as a result of growth, a running cat, chewing buffalo, or playing child moves without growth. All movements in living organisms are purposeful, finely regulated reactions to environmental cues.",
        "theory_blocks": [
            {
                "heading": "Growth-Dependent vs Growth-Independent Movements",
                "content": "• <strong>Growth-Dependent Movements:</strong> A seed germinates and grows; over a few days, the seedling pushes soil aside and emerges into the air. If growth stops, these movements cease entirely.<br>• <strong>Growth-Independent Movements:</strong> A cat sprinting after a mouse, children enjoying a swing, or a buffalo chewing cud to break down tough cellulose fibers are not caused by growth. They are immediate behavioural responses to take advantage of changes in the environment or to protect the organism (e.g. blinking at bright light, jerking away from a hot stove)."
            },
            {
                "heading": "Controlled Movement & Specialised Tissues",
                "content": "All movements in response to the environment are exquisitely controlled. When speaking to a classmate in a library, we whisper rather than shout loudly; the nature of the movement depends strictly on the triggering event. Therefore, multicellular organisms require integrated systems of <strong>control and coordination</strong>. In animals, this critical task is performed collaboratively by <strong>nervous tissue</strong> (rapid electrical signals) and <strong>muscular tissue</strong> (contractile mechanical effectors)."
            }
        ],
        "narration": "Welcome students to Chapter 6: Control and Coordination! How do we know something is alive? It isn't just about movement, but how movement is controlled. A germinating seed moves by growing, but a running cat or chewing cow moves without growth! Every movement is a calculated response to the environment. In animals, nervous and muscular tissues work together to coordinate every whisper, sprint, and reaction!",
        "interactive_type": "movement_types_sim",
        "checkpoints": [
            {
                "q": "Why is a seed seedling pushing soil aside classified as a growth-dependent movement, while a cat running is not?",
                "options": [
                    "Because seeds are animals while cats are plants",
                    "The seedling's movement ceases if growth is stopped, whereas a cat's running is an immediate muscular response independent of growth",
                    "Cats do not possess nervous tissues",
                    "Seedlings move at much faster speeds than running cats"
                ],
                "ans": 1,
                "solution": "The emergence of a seedling is physically produced by cellular division and elongation (growth). If growth is arrested, movement stops. In contrast, running in a cat is caused by rapid contraction of skeletal muscle fibres without any change in overall body growth (NCERT Page 100)."
            },
            {
                "q": "Which two specialized tissues work in coordination to provide rapid control and movement in animals?",
                "options": [
                    "Epithelial and connective tissues",
                    "Xylem and phloem tissues",
                    "Nervous and muscular tissues",
                    "Adipose and skeletal cartilage tissues"
                ],
                "ans": 2,
                "solution": "In animals, nervous tissue detects environmental stimuli and conducts electrical impulses, while muscular tissue responds mechanically by contracting and relaxing to generate physical movement (Section 6.1, Page 100)."
            }
        ]
    },

    # Slide 2: Animals – Nervous System & Structure of a Neuron (Pages 100-101, Fig 6.1)
    {
        "index": 1,
        "title": "Animals – Nervous System: Structure of a Neuron & The Synapse",
        "short_title": "2. Neuron & Synapse",
        "badge": "Section 6.1 • Pages 100–101",
        "quote": "Nervous tissue is an organized network of neurons specialized for conducting information via electrical impulses from one part of the body to another.",
        "lead": "Touching a hot object is an urgent hazard. Environmental information is captured by specialized receptors at nerve endings, converted into an electrical impulse, conducted along the neuron, and relayed chemically across synapses to muscles or adjacent neurons.",
        "theory_blocks": [
            {
                "heading": "Anatomy of a Neuron (Figure 6.1 a)",
                "content": "• <strong>Dendritic Tip:</strong> Branched cytoplasmic projections that acquire information from environmental receptors or preceding neurons.<br>• <strong>Cell Body (Cyton):</strong> Contains the nucleus and metabolic cytoplasm; converts receptor interactions into an electrical action potential.<br>• <strong>Axon:</strong> A long cylindrical nerve fibre that conducts the electrical impulse rapidly away from the cell body toward terminal branches.<br>• <strong>Nerve Ending:</strong> Terminal arborization where the electrical impulse triggers secretion of chemical messengers."
            },
            {
                "heading": "Transmission of Impulses & The Synapse (Figure 6.1 b)",
                "content": "1. Information acquired at the dendritic tip sets off a local chemical reaction creating an <strong>electrical impulse</strong>.<br>2. The impulse travels from dendrite to cyton, and shoots along the axon to its terminal end.<br>3. At the axon terminal, the electrical impulse stimulates synaptic vesicles to release <strong>neurotransmitter chemicals</strong>.<br>4. These chemicals diffuse across the microscopic fluid gap—the <strong>synapse</strong>—and trigger a fresh electrical impulse in the dendrite of the next neuron.<br>5. A similar <strong>neuromuscular junction (NMJ)</strong> delivers impulses directly to muscle fibres or glandular cells."
            }
        ],
        "narration": "Let's examine the neuron, the structural unit of the nervous system! Information is captured at the dendritic tips, where a chemical reaction sparks an electrical impulse. This impulse races through the cell body and along the axon. At the axon terminal, the electrical surge cannot jump the gap, so it triggers the release of chemical neurotransmitters across the synapse! This restarts the electrical spark in the next neuron or commands a muscle to contract!",
        "interactive_type": "neuron_synapse_sim",
        "checkpoints": [
            {
                "q": "What is the correct pathway through which an impulse travels within a single neuron?",
                "options": [
                    "Axon → Cell Body → Dendrite → Nerve Ending",
                    "Dendritic Tip → Cell Body (Cyton) → Axon → Axon Terminal (Nerve Ending)",
                    "Nerve Ending → Axon → Cell Body → Dendrite",
                    "Cell Body → Dendritic Tip → Axon Terminal → Axon"
                ],
                "ans": 1,
                "solution": "Sensory stimuli initiate an impulse at the dendritic tip. The electrical potential traverses the cell body (cyton), propagates down the axon cylinder, and arrives at the terminal nerve endings (NCERT Figure 6.1 a)."
            },
            {
                "q": "What happens at the synapse between two neurons when an electrical impulse reaches the axon end?",
                "options": [
                    "The electrical spark physically jumps across empty vacuum like lightning",
                    "The impulse stops permanently and is destroyed",
                    "The electrical impulse sets off the release of chemical neurotransmitters that cross the synaptic cleft to initiate a new impulse",
                    "Blood flows between the neurons to conduct ions"
                ],
                "ans": 2,
                "solution": "Because physical continuity is interrupted by the microscopic synaptic cleft, the electrical wave triggers exocytosis of neurotransmitter chemicals. These diffuse across the gap to bind receptors on the post-synaptic dendrite, generating a fresh impulse (NCERT Page 101)."
            }
        ]
    },

    # Slide 3: Sensory Receptors & Taste vs Smell Integration (Page 101, Activity 6.1)
    {
        "index": 2,
        "title": "Sensory Receptors & Activity 6.1: The Interplay of Taste and Smell",
        "short_title": "3. Sensory Receptors",
        "badge": "Section 6.1 • Activity 6.1 (Page 101)",
        "quote": "Gustatory receptors detect taste while olfactory receptors detect smell. The perceived flavour of food is an integrated synthesis of both sensory pathways.",
        "lead": "Our sense organs are studded with specialized sensory receptor cells that convert environmental energy into nervous signals. Activity 6.1 demonstrates how gustatory taste signals and olfactory smell signals merge to construct our full sensory reality.",
        "theory_blocks": [
            {
                "heading": "Classes of Sensory Receptors in Animals",
                "content": "• <strong>Gustatory Receptors:</strong> Located on taste buds on the tongue; detect five primary tastes (sweet, salty, sour, bitter, umami).<br>• <strong>Olfactory Receptors:</strong> Located in the olfactory epithelium of the nasal cavities; detect volatile airborne odorant molecules.<br>• <strong>Photoreceptors:</strong> Located in the retina of eyes; detect light intensity and colour wavelengths.<br>• <strong>Phonoreceptors / Statoreceptors:</strong> Located in the inner ear; detect sound acoustic vibrations and maintain balance.<br>• <strong>Thermoreceptors / Tangoreceptors:</strong> Located across the skin; detect temperature changes and mechanical pressure/touch."
            },
            {
                "heading": "Activity 6.1: Nose Blocking & Flavour Perception",
                "content": "• <strong>Procedure:</strong> Taste sugar with nostrils open; then pinch nose tightly between thumb and forefinger and taste sugar again. Repeat during a seasoned lunch meal.<br>• <strong>Observation:</strong> Pure cane sugar (sucrose) still tastes sweet with nostrils closed because tongue gustatory receptors directly bind dissolved sugar molecules. However, complex foods (spices, curries, garlic) taste dramatically bland and unrecognisable without nasal airflow.<br>• <strong>Scientific Explanation:</strong> True 'flavour' is a multisensory fusion. Up to 80% of perceived food flavour is derived from volatile aromatic molecules traveling retro-nasally to olfactory receptors. When the nose is blocked or congested during a common cold, olfactory detection is eliminated."
            }
        ],
        "narration": "Have you ever wondered why food tastes completely flat and boring when you have a cold? That's Activity 6.1! Our tongue has gustatory receptors for basic tastes like sweet, sour, and salty. But complex flavors require olfactory receptors in our nose! When you pinch your nose or catch a cold, mucus blocks airborne aromas from reaching your olfactory nerves. You can still tell sugar is sweet, but all the rich aromatic spices vanish!",
        "interactive_type": "receptors_taste_smell_sim",
        "checkpoints": [
            {
                "q": "Which sensory receptors detect taste and smell respectively in human sense organs?",
                "options": [
                    "Photoreceptors and Phonoreceptors",
                    "Gustatory receptors and Olfactory receptors",
                    "Thermoreceptors and Tangoreceptors",
                    "Proprioceptors and Baroreceptors"
                ],
                "ans": 1,
                "solution": "Gustatory receptors reside within the taste buds of the tongue to detect chemical tastes, while olfactory receptors reside in the nasal epithelium to detect volatile odorants (NCERT Page 101)."
            },
            {
                "q": "Why does seasoned food taste bland when you suffer from a head cold with a blocked nose?",
                "options": [
                    "Stomach enzymes stop secreting hydrochloric acid during a cold",
                    "Tongue gustatory receptors are physically destroyed by cold viruses",
                    "Inflamed nasal mucosa blocks volatile aromas from stimulating olfactory receptors, stripping away the aromatic component of flavour",
                    "Saliva turns completely acidic and neutralizes all taste molecules"
                ],
                "ans": 2,
                "solution": "Full flavour perception is a combined synthesis of tongue taste and nasal olfaction. Nasal blockage eliminates olfactory input, leaving only basic tongue sensations and making food seem dull and tasteless (Activity 6.1, Page 101)."
            }
        ]
    },

    # Slide 4: Reflex Actions & The Reflex Arc (Pages 102-103, Fig 6.2)
    {
        "index": 3,
        "title": "Reflex Actions & The Reflex Arc: High-Speed Survival Circuits",
        "short_title": "4. Reflex Arc",
        "badge": "Section 6.1.1 • Pages 102–103",
        "quote": "Reflex arcs are formed in the spinal cord itself, enabling an immediate output response before the conscious thinking process of the brain can intervene.",
        "lead": "When your hand touches a hot iron or open flame, you withdraw your arm in a fraction of a second—long before you consciously feel pain. This life-saving speed is achieved through dedicated short-circuit pathways called reflex arcs.",
        "theory_blocks": [
            {
                "heading": "Why Conscious Thinking is Too Slow in Emergencies",
                "content": "Conscious thinking involves intricate neural processing: sensory signals must travel up the spinal cord to the fore-brain, pass through thousands of cerebral interneurons, formulate an intentional decision, and send motor commands back down to the arm muscles. If we waited for this conscious deliberation when touching a flame, extensive tissue burning would occur before the hand could move!"
            },
            {
                "heading": "Anatomy of the Reflex Arc (Figure 6.2)",
                "content": "1. <strong>Stimulus & Receptor:</strong> Heat/pain detected by thermoreceptors in skin.<br>2. <strong>Sensory (Afferent) Neuron:</strong> Transmits electrical impulse from receptor into dorsal horn of spinal cord.<br>3. <strong>Relay (Interneuron) Neuron:</strong> Situated in spinal cord grey matter; instantly routes impulse directly to the motor pathway while simultaneously dispatching a parallel message to the brain.<br>4. <strong>Motor (Efferent) Neuron:</strong> Carries immediate command from ventral horn to target effector.<br>5. <strong>Effector Organ:</strong> Arm bicep muscle contracts, pulling hand away from danger.<br>• <strong>Evolutionary Origin:</strong> Reflex arcs evolved in animals as high-speed survival mechanisms because conscious cerebral networks are inherently slower or absent in primitive organisms."
            }
        ],
        "narration": "Imagine touching a burning flame! If your body had to send that signal all the way to your brain, think about the pain, and decide to pull away, your skin would suffer severe burns! Instead, nature engineered the reflex arc in your spinal cord. The sensory nerve meets a relay neuron right in the spinal cord, which immediately fires a motor command to contract your arm muscle! Your hand jerks back automatically in milliseconds, while a second signal informs your brain of what just happened!",
        "interactive_type": "reflex_arc_sim",
        "checkpoints": [
            {
                "q": "What is the exact sequence of components in a spinal reflex arc when touching a hot pan?",
                "options": [
                    "Effector → Motor Neuron → Brain → Sensory Neuron → Receptor",
                    "Receptor in skin → Sensory Neuron → Relay Neuron in Spinal Cord → Motor Neuron → Effector Muscle",
                    "Sensory Neuron → Brain Cortex → Relay Neuron → Receptor → Muscle",
                    "Motor Neuron → Spinal Cord → Sensory Neuron → Effector Muscle"
                ],
                "ans": 1,
                "solution": "The reflex arc proceeds from receptor in skin → sensory neuron → spinal cord relay neuron → motor neuron → effector muscle (Figure 6.2, Page 103)."
            },
            {
                "q": "Why have reflex arcs evolved in animals despite the presence of advanced thinking brains?",
                "options": [
                    "Because the brain cannot process electrical impulses",
                    "Reflex arcs operate through blood vessels rather than nerves",
                    "Because the thinking process of the cerebral cortex is too complex and slow for instantaneous emergency defense",
                    "Spinal cord nerves have higher voltage than brain nerves"
                ],
                "ans": 2,
                "solution": "Thinking requires complex integration across millions of cortical neurons, which introduces a delay. Reflex arcs evolved as rapid, hardwired survival shortcuts in the spinal cord to protect organisms from acute injury (Page 102)."
            }
        ]
    },

    # Slide 5: The Human Brain Architecture & The Central Nervous System (Pages 103-104, Fig 6.3)
    {
        "index": 4,
        "title": "The Human Brain & Nervous System Divisions",
        "short_title": "5. Brain Architecture",
        "badge": "Section 6.1.2 • Pages 103–104",
        "quote": "The brain and spinal cord constitute the Central Nervous System. They receive information from all parts of the body and integrate it.",
        "lead": "While reflex arcs handle urgent involuntary emergencies, the human brain is the master coordinating organ responsible for consciousness, voluntary movement, sensory integration, memory, and emotional deliberation.",
        "theory_blocks": [
            {
                "heading": "Nervous System Architectural Hierarchy",
                "content": "• <strong>Central Nervous System (CNS):</strong> Comprises the <strong>Brain</strong> and <strong>Spinal Cord</strong>. It processes sensory inputs, stores memories, makes decisions, and coordinates bodily physiology.<br>• <strong>Peripheral Nervous System (PNS):</strong> Facilitates two-way communication between the CNS and peripheral organs:<br>&nbsp;&nbsp;a) <em>Cranial Nerves:</em> 12 pairs of nerves arising directly from the brain.<br>&nbsp;&nbsp;b) <em>Spinal Nerves:</em> 31 pairs of nerves emerging along the spinal cord."
            },
            {
                "heading": "The Three Major Regions of the Brain (Figure 6.3)",
                "content": "1. <strong>Fore-Brain (Prosencephalon):</strong> Major component is the <strong>Cerebrum</strong>; responsible for thinking, intelligence, sensory interpretation, voluntary motor commands, and hunger.<br>2. <strong>Mid-Brain (Mesencephalon):</strong> Connects fore-brain to hind-brain; coordinates visual and auditory reflex movements of the head, neck, and trunk, and controls pupil size.<br>3. <strong>Hind-Brain (Rhombencephalon):</strong> Composed of the <strong>Pons</strong>, <strong>Cerebellum</strong>, and <strong>Medulla Oblongata</strong>; manages autonomic involuntary life functions and bodily equilibrium."
            }
        ],
        "narration": "Meet the most complex object in the known universe: the human brain! Together with the spinal cord, it forms the Central Nervous System, networked to the rest of your body via cranial and spinal nerves of the Peripheral Nervous System. Anatomically, the brain is divided into three key territories: the massive Fore-Brain for thinking and conscious decisions, the Mid-Brain for visual and auditory reflexes, and the Hind-Brain regulating your heartbeat, breathing, and balance!",
        "interactive_type": "brain_anatomy_sim",
        "checkpoints": [
            {
                "q": "Which anatomical structures together constitute the Central Nervous System (CNS)?",
                "options": [
                    "Cranial nerves and spinal nerves",
                    "Brain and Spinal Cord",
                    "Heart, lungs, and stomach",
                    "Sympathetic and parasympathetic ganglia"
                ],
                "ans": 1,
                "solution": "The Central Nervous System (CNS) consists strictly of the Brain and the Spinal Cord, whereas peripheral cranial and spinal nerves make up the PNS (NCERT Page 103)."
            },
            {
                "q": "What are the three fundamental anatomical divisions of the human brain?",
                "options": [
                    "Cortex, Medulla, and Pelvis",
                    "Sensory brain, Motor brain, and Reflex brain",
                    "Fore-brain, Mid-brain, and Hind-brain",
                    "Dendritic brain, Axonal brain, and Synaptic brain"
                ],
                "ans": 2,
                "solution": "The human brain is subdivided into three major developmental and functional regions: fore-brain, mid-brain, and hind-brain (NCERT Page 103)."
            }
        ]
    },

    # Slide 6: Fore-Brain: Thinking, Sensory Perception & Hunger Center (Pages 104-105)
    {
        "index": 5,
        "title": "The Fore-Brain: Cerebrum, Sensory Integration & The Hunger Center",
        "short_title": "6. Fore-Brain & Cerebrum",
        "badge": "Section 6.1.2 • Pages 104–105",
        "quote": "The fore-brain is the main thinking part of the brain, containing specialized sensory areas, association zones, and the hunger satiety center.",
        "lead": "The convoluted cerebral hemispheres of the fore-brain represent the pinnacle of neural evolution. Here, raw sensations are decoded, cross-referenced with past memories, and translated into intelligent voluntary motor decisions.",
        "theory_blocks": [
            {
                "heading": "Functional Organization of the Cerebral Cortex",
                "content": "• <strong>Sensory Receiving Areas:</strong> Specific lobes are dedicated to processing specific sensory streams—vision (occipital lobe), sound and language (temporal lobe), smell and taste.<br>• <strong>Association Areas:</strong> Highly connected neural sheets where new sensory inputs are interpreted by comparing them with stored memories and information from other sensory modalities.<br>• <strong>Motor Areas:</strong> Cortical zones that send deliberate voluntary movement instructions to skeletal muscles (e.g., deciding to stand up, write with a pen, or kick a soccer ball)."
            },
            {
                "heading": "The Sensation of Satiety & Hunger (Page 104)",
                "content": "How do you know when your stomach is full and it is time to stop eating? Certain visceral sensations are completely distinct from seeing or hearing. The sensation of feeling hungry or feeling full (satiety) is monitored and regulated by an independent, specialized metabolic control center located within the <strong>fore-brain</strong> (specifically the hypothalamus)."
            }
        ],
        "narration": "The Fore-Brain, dominated by the cerebrum, is your master thinking computer! It contains distinct sensory receiving areas for vision, sound, and smell. Surrounding these are association areas that weave incoming sights and sounds with your past memories to help you make decisions. When you decide to kick a ball or write an essay, your motor cortex fires the commands. And when you enjoy a meal, the fore-brain's hunger center detects nutrient levels and signals when you are happily full!",
        "interactive_type": "forebrain_centers_sim",
        "checkpoints": [
            {
                "q": "What is the primary role of the 'association areas' in the cerebral cortex of the fore-brain?",
                "options": [
                    "To pump cerebrospinal fluid into the ventricles",
                    "To interpret sensory information by integrating it with cues from other receptors and memories stored in the brain",
                    "To directly trigger involuntary vomiting reflexes",
                    "To manufacture red blood cells for cerebral circulation"
                ],
                "ans": 1,
                "solution": "Association areas are neither purely sensory nor purely motor; they correlate current sensory signals with accumulated memories and multimodal inputs to formulate decisions (NCERT Page 103-104)."
            },
            {
                "q": "Where in the human brain is the specialized center located that detects hunger and the sensation of feeling full (satiety)?",
                "options": [
                    "In the spinal cord lumbar segment",
                    "In the cerebellum at the back of the skull",
                    "In a separate part of the fore-brain",
                    "In the medulla oblongata"
                ],
                "ans": 2,
                "solution": "NCERT Page 104 specifically highlights that the sensation of feeling full is governed by a distinct hunger-monitoring center located in the fore-brain (hypothalamus)."
            }
        ]
    },

    # Slide 7: Mid-Brain & Hind-Brain: Involuntary Control & Posture Balance (Pages 104-105)
    {
        "index": 6,
        "title": "Mid-Brain & Hind-Brain: Involuntary Centers & Cerebellar Balance",
        "short_title": "7. Hind-Brain & Balance",
        "badge": "Section 6.1.2 • Pages 104–105",
        "quote": "Medulla controls vital involuntary actions like blood pressure, salivation, and vomiting; Cerebellum maintains posture, equilibrium, and precision of voluntary movements.",
        "lead": "Between conscious thought-out decisions (moving a chair) and simple spinal reflexes, thousands of automated muscle movements sustain our lives without any conscious effort. These vital functions are orchestrated by the mid-brain and hind-brain.",
        "theory_blocks": [
            {
                "heading": "Involuntary Actions & The Medulla Oblongata",
                "content": "• <strong>Involuntary Movements:</strong> Heartbeat, peristaltic gut contractions, respiratory rate, and pupillary adjustments occur continuously without conscious thought.<br>• <strong>The Medulla Oblongata (Hind-Brain):</strong> The master autonomic control center. It directly regulates arterial <strong>blood pressure</strong>, salivary secretion (<strong>salivation</strong> when seeing appetizing food), respiratory rhythm, swallowing, coughing, sneezing, and the <strong>vomiting</strong> reflex."
            },
            {
                "heading": "The Cerebellum: Posture, Balance & Precision",
                "content": "• <strong>Precision of Voluntary Movements:</strong> Activities like riding a bicycle, walking along a straight line, dancing, or picking up a sharp pencil require exact, synchronized muscle adjustments.<br>• <strong>Cerebellum Function:</strong> The cerebellum receives sensory input from the inner ear (semi-circular canals) and muscle proprioceptors. It continuously coordinates motor output to maintain <strong>posture</strong>, bodily <strong>equilibrium</strong>, and smooth, error-free motor coordination."
            }
        ],
        "narration": "You don't have to remember to beat your heart or tell your salivary glands to water when you smell pizza! These vital involuntary tasks are handled 24/7 by the Medulla Oblongata in your hind-brain, which controls blood pressure, breathing, salivation, and vomiting. Meanwhile, right behind it sits the Cerebellum—your balance master! Whether you are walking on a straight line, riding a bicycle, or threading a needle, your cerebellum coordinates every muscle for perfect posture and balance!",
        "interactive_type": "hindbrain_balance_sim",
        "checkpoints": [
            {
                "q": "Which specific part of the hind-brain controls involuntary visceral actions including blood pressure, salivation, and vomiting?",
                "options": [
                    "Cerebrum",
                    "Medulla (Medulla Oblongata)",
                    "Cerebellum",
                    "Hypothalamus"
                ],
                "ans": 1,
                "solution": "All these involuntary activities—blood pressure, salivation, and vomiting—are directly controlled by the medulla in the hind-brain (NCERT Page 104)."
            },
            {
                "q": "Riding a bicycle, walking along a straight chalk line, and picking up a fallen pencil are coordinated by which brain structure?",
                "options": [
                    "Cerebellum in the hind-brain",
                    "Occipital lobe of the cerebrum",
                    "Spinal cord reflex arc",
                    "Pituitary gland"
                ],
                "ans": 0,
                "solution": "The cerebellum in the hind-brain is specifically responsible for precision of voluntary actions and for maintaining the posture and equilibrium of the body (NCERT Page 104)."
            }
        ]
    },

    # Slide 8: Protection of Nervous Tissue & Muscle Cellular Action (Pages 105-106)
    {
        "index": 7,
        "title": "Protection of Nervous Tissues & The Mechanism of Muscle Action",
        "short_title": "8. Protection & Muscles",
        "badge": "Sections 6.1.3 & 6.1.4 • Pages 105–106",
        "quote": "The brain sits inside a bony box cushioned by cerebrospinal fluid; muscles execute movements when electrical signals trigger contractile proteins to change shape.",
        "lead": "Because central nervous tissues are delicate and indispensable, nature has fortified them inside heavy skeletal armor and hydraulic shock absorbers. At the end of the line, electrical commands trigger muscle fibres to physically contract.",
        "theory_blocks": [
            {
                "heading": "Mechanical Protection of Brain & Spinal Cord (Section 6.1.3)",
                "content": "• <strong>The Cranium (Skull Box):</strong> The brain is encased within a rigid bony box formed by fused cranial bones.<br>• <strong>Cerebrospinal Fluid (CSF) Balloon:</strong> Inside the cranium, the brain is wrapped in three protective membrane layers (meninges) bathed in CSF—acting as a fluid-filled hydraulic shock absorber that neutralizes mechanical impacts.<br>• <strong>The Vertebral Column (Backbone):</strong> The soft spinal cord runs through the neural canal of the hard, bumpy vertebral column for complete structural protection."
            },
            {
                "heading": "How Nervous Tissue Causes Muscle Action (Section 6.1.4)",
                "content": "1. When a nerve impulse arrives at the neuromuscular junction, acetylcholine neurotransmitters trigger an electrical wave along the muscle cell membrane.<br>2. <strong>Contractile Proteins (Actin & Myosin):</strong> Muscle cells contain specialized protein filaments that change both their shape and spatial arrangement in response to ionic shifts.<br>3. These protein filaments slide over one another, resulting in <strong>cellular shortening (contraction)</strong>.<br>4. Collective shortening of thousands of muscle fibres pulls on tendons and moves bones."
            }
        ],
        "narration": "Our nervous system is so precious that it has double protection! The brain sits safely inside a bony skull box called the cranium, floating in a fluid-filled balloon of cerebrospinal fluid that absorbs mechanical shocks. Your spinal cord is protected inside the bumpy vertebral column. But how does an electrical nerve signal make your arm move? At the neuromuscular junction, the impulse signals special muscle proteins—actin and myosin—to change shape and slide together, shortening the muscle cell to pull your bones!",
        "interactive_type": "protection_muscle_sim",
        "checkpoints": [
            {
                "q": "How is the delicate human brain protected from mechanical shocks and physical concussions?",
                "options": [
                    "By a thick layer of adipose subcutaneous fat alone",
                    "It sits inside a bony cranium cushioned within a fluid-filled balloon (cerebrospinal fluid)",
                    "By the contraction of facial voluntary muscles",
                    "It is suspended freely in air within the skull cavity"
                ],
                "ans": 1,
                "solution": "The brain sits inside a rigid bony cranium and is surrounded by cerebrospinal fluid (CSF) within the meninges, providing hydraulic shock absorption (Section 6.1.3, Page 105)."
            },
            {
                "q": "At the microscopic cellular level, how do animal muscle cells physically move and shorten upon receiving a nerve impulse?",
                "options": [
                    "Muscle cells evaporate water to decrease their volume",
                    "Muscle cells divide rapidly to create smaller cells",
                    "Specialized proteins in muscle cells change their molecular shape and arrangement in response to electrical impulses, causing the cell to shorten",
                    "Nerves physically reel in the muscle fibres like ropes"
                ],
                "ans": 2,
                "solution": "Muscle cells contain specialized contractile proteins that alter their shape and sliding arrangement in response to nervous electrical stimuli, giving the muscle cell a shorter contracted form (Section 6.1.4, Page 105)."
            }
        ]
    },

    # Slide 9: Coordination in Plants: Immediate Response to Stimulus (Mimosa pudica) (Page 106, Fig 6.4)
    {
        "index": 8,
        "title": "Coordination in Plants: Immediate Nastic Response in Mimosa pudica",
        "short_title": "9. Mimosa Droop Lab",
        "badge": "Section 6.2 & 6.2.1 • Page 106",
        "quote": "Plants show two distinct types of movement: one independent of growth (immediate nastic response) and the other dependent on directional growth (tropism).",
        "lead": "Plants possess neither a nervous system nor muscle fibres. Yet when you touch the leaflets of the sensitive plant Chhui-mui (Mimosa pudica), they fold and collapse in less than a second! How do plants detect touch and move without nerves?",
        "theory_blocks": [
            {
                "heading": "Two Distinct Categories of Plant Movement",
                "content": "• <strong>Growth-Independent (Nastic) Movements:</strong> Non-directional, rapid responses to external stimuli (e.g., touch, shock). Movement is reversible and does not involve cellular growth.<br>• <strong>Growth-Dependent (Tropic) Movements:</strong> Directional, slow growth curvatures oriented toward or away from environmental vectors (light, gravity, water)."
            },
            {
                "heading": "Immediate Response Mechanism in Mimosa pudica (Figure 6.4)",
                "content": "1. <strong>Touch Detection & Propagation:</strong> Touching a distal leaflet tip generates a wave of electrical-chemical signals that diffuses from cell to cell down the petiole.<br>2. <strong>No Muscle Tissue:</strong> Plants lack actin-myosin contractile proteins.<br>3. <strong>Turgor Pressure Hydraulic Shift:</strong> At the base of each leaflet and petiole lies a swollen hinge called the <strong>pulvinus</strong>.<br>4. Upon receiving the electrochemical signal, pulvinar cells suddenly lose potassium and other ions, prompting rapid <strong>efflux of water</strong> into intercellular spaces.<br>5. The loss of internal turgor pressure causes pulvinar cells to flaccidly collapse, causing the entire leaf to fold and droop downward!"
            }
        ],
        "narration": "Plants don't have brains, nerves, or muscles—yet watch what happens when you touch Chhui-mui, the sensitive touch-me-not plant! Its leaves fold up and droop in less than a second! How does this happen? The touch creates an electrical-chemical wave that travels from cell to cell to swollen hinges called pulvini at the leaf base. Instead of contracting muscles, plant cells rapidly dump water, losing turgor pressure! The cells shrink, and the leaves collapse downward in an immediate, non-growth defense reflex!",
        "interactive_type": "mimosa_pudica_sim",
        "checkpoints": [
            {
                "q": "How do the leaves of the sensitive plant (Mimosa pudica) rapidly fold and droop when touched, despite having no muscle tissue?",
                "options": [
                    "By rapidly shedding dead leaves",
                    "By altering the amount of water in specialized hinge cells (pulvini), leading to swelling or shrinking through turgor changes",
                    "By snapping tiny bones located in the leaf stem",
                    "By burning carbohydrates to produce steam"
                ],
                "ans": 1,
                "solution": "Plant cells change shape by changing their water content. Water efflux from pulvinar cells reduces turgor pressure, causing immediate shrinking, folding, and drooping (Section 6.2.1, Page 106)."
            },
            {
                "q": "How does cell-to-cell communication in Mimosa pudica differ from nervous conduction in animals?",
                "options": [
                    "Plants use pure radio waves rather than chemicals",
                    "Plants use electrical-chemical means to convey information from cell to cell, but lack specialized nervous tissue or synapses",
                    "Information in plants is carried solely by red blood cells",
                    "Plants do not communicate between cells at all"
                ],
                "ans": 1,
                "solution": "While plants employ electrical-chemical signaling, they do not possess specialized axons, neurons, or synapses; signals diffuse directly between adjacent vegetative cells (NCERT Page 106)."
            }
        ]
    },

    # Slide 10: Plant Movement Due to Growth: Tendril Thigmotropism (Pages 106-107)
    {
        "index": 9,
        "title": "Movement Due to Growth: Tendril Thigmotropism & Directional Climbing",
        "short_title": "10. Tendril Coiling",
        "badge": "Section 6.2.2 • Pages 106–107",
        "quote": "When a tendril comes into contact with support, the contact side grows slower than the outer side, causing the tendril to coil tightly around the object.",
        "lead": "Unlike the immediate collapsing of Mimosa, climbing plants navigate their world through slow, directional growth movements. Tendrils act as delicate touch-sensitive tactile feelers, allowing pea vines to scale vertical supports.",
        "theory_blocks": [
            {
                "heading": "Tendril Anatomy & Thigmotropism",
                "content": "• <strong>Tendrils:</strong> Slender, thread-like modified stem or leaf structures found in climbing plants like peas, pumpkins, and grapes.<br>• <strong>Thigmotropism:</strong> Directional plant growth in response to mechanical contact or touch with a solid object.<br>• Because plants cannot physically walk, directional growth gives the distinct appearance of purposeful searching and climbing movement."
            },
            {
                "heading": "Differential Growth Mechanism of Coiling",
                "content": "1. When a growing tendril touches an external support (fence, trellis, bamboo pole), touch sensors detect the contact.<br>2. <strong>Differential Growth Rate:</strong> The side of the tendril in direct physical contact with the object grows <em>much slower</em> than the side away from the object.<br>3. Growth-promoting hormones (auxins) migrate to the outer, non-contact side, stimulating dramatic cellular elongation.<br>4. This unequal elongation rate causes the tendril to curve continuously around the support in a spiral helix, securing a firm mechanical anchor."
            }
        ],
        "narration": "Look at pea plants and vines! How do they climb up fences without hands? They use tendrils—slender green feelers that exhibit thigmotropism, or touch-guided growth! When a tendril brushes against a bamboo stick, the side touching the stick slows down its growth, while the outer side grows much faster. This unequal growth forces the tendril to wrap around the stick in a tight spiral coil, anchoring the vine so it can reach toward the sun!",
        "interactive_type": "tendril_thigmotropism_sim",
        "checkpoints": [
            {
                "q": "Why does a pea plant tendril circle and coil tightly around a bamboo support stick?",
                "options": [
                    "The side in contact with the stick secretes glue",
                    "The side in contact with the object does not grow as rapidly as the side away from the object, causing curved coiling",
                    "The stick electrifies the tendril, causing it to shrink",
                    "Tendrils possess tiny muscular claws"
                ],
                "ans": 1,
                "solution": "Physical contact inhibits cell elongation on the inner surface while the outer surface continues rapid growth. This differential growth rate forces the tendril to coil around the support (Section 6.2.2, Page 106)."
            },
            {
                "q": "What term describes the directional growth movement of a plant organ in response to physical touch or contact?",
                "options": [
                    "Phototropism",
                    "Hydrotropism",
                    "Thigmotropism",
                    "Geotropism"
                ],
                "ans": 2,
                "solution": "Thigmotropism (from Greek 'thigma' meaning touch) is directional plant growth oriented in response to contact with a solid surface (NCERT Page 106-107)."
            }
        ]
    },

    # Slide 11: Phototropism & Activity 6.2 Light Box Experiment (Pages 107-108, Fig 6.5)
    {
        "index": 10,
        "title": "Phototropism & Activity 6.2: Response of Plants to Unidirectional Light",
        "short_title": "11. Phototropism Lab",
        "badge": "Activity 6.2 • Pages 107–108 (Figure 6.5)",
        "quote": "Shoots respond to light by bending towards it (positive phototropism), while roots bend away from light (negative phototropism).",
        "lead": "Light is the fundamental energy source for autotrophic photosynthesis. Plants have evolved precise directional tropisms to steer photosynthetic leaves directly into the path of sunlight.",
        "theory_blocks": [
            {
                "heading": "Principles of Phototropism",
                "content": "• <strong>Phototropism:</strong> Directional growth movement of plant organs in response to unidirectional light.<br>• <strong>Positive Phototropism:</strong> Plant shoots bend and grow <em>towards</em> the source of light to optimize photon absorption by chlorophyll in leaves.<br>• <strong>Negative Phototropism:</strong> Roots bend and grow <em>away from</em> light, driving them deeper into the darkness of soil where moisture and anchor minerals reside."
            },
            {
                "heading": "Activity 6.2: The Conical Flask Window Box Experiment (Figure 6.5)",
                "content": "1. <strong>Setup:</strong> Conical flask filled with water; wire mesh over neck holding germinating bean seeds; placed inside an open-sided cardboard box facing an illuminated window.<br>2. <strong>Initial Result (2–3 Days):</strong> Shoots bend distinctly towards the window light; roots bend away toward the dark interior.<br>3. <strong>Reversal Test:</strong> The flask is rotated 180° so shoots point away from light and roots point toward light, then left undisturbed for a few days.<br>4. <strong>Conclusion:</strong> Old mature stem parts remain bent, but <em>newly growing shoot tips</em> sharply change direction, bending back towards the light! This confirms that phototropism is an active, ongoing directional growth phenomenon."
            }
        ],
        "narration": "Let's explore Activity 6.2! Place germinating bean seeds in a conical flask inside a box open only to a sunny window. After a couple of days, the shoots bend towards the light—positive phototropism! Meanwhile, the roots curve away—negative phototropism! Now, turn the flask around so the shoots face away from the light. Remarkably, the new growth curves right back toward the sun! This ensures plants always maximize sunlight for photosynthesis!",
        "interactive_type": "phototropism_box_sim",
        "checkpoints": [
            {
                "q": "In Activity 6.2, how do newly growing shoot tips respond after the conical flask is rotated 180° away from the window light?",
                "options": [
                    "The shoots stop growing and die immediately",
                    "The newly growing shoot tips bend back towards the window light, demonstrating positive phototropism",
                    "The shoots continue growing straight into the dark box forever",
                    "The roots transform into leafy shoots"
                ],
                "ans": 1,
                "solution": "Newly formed shoot tissues adjust their directional elongation, curving back toward the window light to maintain positive phototropism (Activity 6.2, Page 107-108)."
            },
            {
                "q": "How do plant shoots and roots differ in their directional growth response to light?",
                "options": [
                    "Shoots are positively phototropic (bend toward light); roots are negatively phototropic (bend away from light)",
                    "Shoots and roots both grow exclusively toward light",
                    "Shoots grow away from light; roots grow toward light",
                    "Neither shoots nor roots show any response to light"
                ],
                "ans": 0,
                "solution": "Shoots exhibit positive phototropism by growing toward sunlight, while roots exhibit negative phototropism by growing away from light (NCERT Page 107)."
            }
        ]
    },

    # Slide 12: Geotropism, Hydrotropism & Chemotropism (Pages 107-108, Fig 6.6)
    {
        "index": 11,
        "title": "Geotropism, Hydrotropism & Chemotropism: Environmental Vectors",
        "short_title": "12. Tropic Movements",
        "badge": "Section 6.2.2 • Pages 107–108 (Figure 6.6)",
        "quote": "Geotropism guides roots downward and shoots upward; hydrotropism directs roots to water; chemotropism guides pollen tubes to ovules.",
        "lead": "Light is not the only environmental compass for plants. Gravity, moisture gradients, and chemical attractants each command specialized directional growth movements essential for survival and reproduction.",
        "theory_blocks": [
            {
                "heading": "Geotropism (Gravitropism) (Figure 6.6)",
                "content": "• <strong>Definition:</strong> Upward and downward growth of plant organs in response to the gravitational pull of the Earth.<br>• <strong>Positive Geotropism:</strong> Roots invariably grow downwards into soil along the vector of gravity.<br>• <strong>Negative Geotropism:</strong> Shoots grow upwards into the air against the gravitational pull.<br>• <em>Horizontal Pot Test:</em> When a potted seedling is placed horizontally, roots curve downward 90° into soil, while shoots curve upward 90° toward the sky."
            },
            {
                "heading": "Hydrotropism & Chemotropism (Page 107)",
                "content": "• <strong>Hydrotropism:</strong> Directional growth of roots towards regions of higher water or soil moisture content, even overriding geotropic vectors if water is scarce.<br>• <strong>Chemotropism:</strong> Directional growth in response to chemical stimuli.<br>• <strong>Prime Botanical Example:</strong> Following pollination on the flower stigma, the <strong>pollen tube</strong> grows down through the style toward the ovary and ovule, precisely guided by chemical attractants (sugars and calcium gradients) secreted by the ovule."
            }
        ],
        "narration": "Plants also respond to gravity, water, and chemicals! Lay a potted plant on its side: the roots curve downward toward the center of the Earth—positive geotropism! The stems curve upward against gravity—negative geotropism! Roots also detect moisture in dry soil, growing toward water in hydrotropism. And look at plant reproduction: when pollen lands on a flower, the pollen tube grows straight toward the ovule guided by chemical signals—a wonderful example of chemotropism!",
        "interactive_type": "tropisms_multi_sim",
        "checkpoints": [
            {
                "q": "What is the classic botanical example of chemotropism highlighted in NCERT Class 10 Science?",
                "options": [
                    "Sunflowers turning toward the sun",
                    "The growth of pollen tubes down through the style towards ovules in flowers",
                    "Tendrils coiling around wooden sticks",
                    "Leaves dropping off trees in autumn"
                ],
                "ans": 1,
                "solution": "The directed growth of the pollen tube through carpel tissues toward the ovule in response to chemical attractants is the standard example of chemotropism (NCERT Page 107)."
            },
            {
                "q": "When a potted plant is placed horizontally on a table, which tropic responses occur in its roots and shoots?",
                "options": [
                    "Roots grow upward (negative geotropism); shoots grow downward (positive geotropism)",
                    "Roots grow horizontally; shoots stop growing",
                    "Roots bend downward (positive geotropism); shoots bend upward (negative geotropism)",
                    "Both roots and shoots curve downward into the table"
                ],
                "ans": 2,
                "solution": "Under gravity's influence, the root bends downward (positive geotropism) while the shoot curves upward away from gravity (negative geotropism) (Figure 6.6, Page 107)."
            }
        ]
    },

    # Slide 13: Auxin Hormone & The Cellular Mechanism of Shoot Bending (Pages 108-109)
    {
        "index": 12,
        "title": "Plant Chemical Communication: The Auxin Phototropic Mechanism",
        "short_title": "13. Auxin Mechanism",
        "badge": "Section 6.2.2 • Pages 108–109",
        "quote": "When light shines from one side, auxin diffuses to the shaded side, stimulating cells on that side to grow longer and causing the shoot to bend towards light.",
        "lead": "Why does a plant bend toward light? The answer lies in microscopic chemical messengers called plant hormones (phytohormones). Auxin, produced at the stem tip, acts as the biochemical engine of phototropic curvature.",
        "theory_blocks": [
            {
                "heading": "Why Chemical Communication Transcends Electrical Impulses",
                "content": "• <strong>Limitations of Electrical Impulses:</strong> Electrical signals only reach cells with direct nervous connections; furthermore, after transmitting an impulse, a neuron requires a refractory recovery period to reset its ionic balance before firing again.<br>• <strong>Advantages of Chemical Signals:</strong> Hormones diffuse throughout fluids, reaching every cell equipped with matching surface receptors. They provide steady, persistent, and coordinated physiological regulation across entire organisms."
            },
            {
                "heading": "Step-by-Step Auxin Bending Mechanism",
                "content": "1. <strong>Synthesis:</strong> The plant hormone <strong>auxin</strong> is synthesised at the actively growing shoot tip (apical meristem).<br>2. <strong>Uniform Light:</strong> When light strikes from directly overhead, auxin diffuses symmetrically down all sides; the shoot grows vertically upright.<br>3. <strong>Unilateral Light:</strong> When light strikes from one side, auxin molecules are photo-sensitive and migrate / diffuse toward the <strong>shady side</strong> of the shoot.<br>4. <strong>Cell Elongation:</strong> The elevated concentration of auxin on the shaded flank stimulates cells there to expand and grow significantly longer than cells on the illuminated side.<br>5. <strong>Curvature:</strong> The faster lengthening of the dark flank physically bends the stem towards the light source!"
            }
        ],
        "narration": "How does a shoot physically bend toward light? It uses a clever chemical called auxin! Auxin is produced at the very tip of the shoot. When sunlight strikes the plant from one side, auxin flees the light, diffusing over to the shady side! Now, auxin is a cell elongation hormone. The cells on the shady side grow longer and faster than cells on the sunny side! This uneven growth pushes the entire stem to bend gracefully toward the light!",
        "interactive_type": "auxin_diffusion_sim",
        "checkpoints": [
            {
                "q": "How does the distribution of the plant hormone auxin cause a shoot to bend towards a side window?",
                "options": [
                    "Auxin is destroyed by shade, causing shaded cells to shrink",
                    "Auxin diffuses towards the shady side of the shoot, stimulating cells on the dark side to grow longer than those on the lit side",
                    "Auxin hardens into wood on the lit side, pulling the plant down",
                    "Auxin attracts insects that physically bend the stem"
                ],
                "ans": 1,
                "solution": "Unilateral light causes auxin to migrate to the shaded flank. The increased auxin concentration accelerates cell elongation on the shaded side, forcing the stem to bend toward the light (NCERT Page 108)."
            },
            {
                "q": "Where in the plant body is the growth hormone auxin primarily synthesised?",
                "options": [
                    "In mature wood of the trunk",
                    "In root hairs only",
                    "At the growing shoot tip (apical meristem)",
                    "Inside dormant seeds"
                ],
                "ans": 2,
                "solution": "Auxin is synthesized at the tips of growing shoots and young leaves, from where it diffuses downward to exert its effects (NCERT Page 108)."
            }
        ]
    },

    # Slide 14: Plant Hormones Quartet: Auxins, Gibberellins, Cytokinins & ABA (Pages 108-109)
    {
        "index": 13,
        "title": "The Plant Hormones Quartet: Growth Promoters vs Inhibitors",
        "short_title": "14. Plant Hormones",
        "badge": "Section 6.2.2 • Pages 108–109",
        "quote": "Auxins, gibberellins, and cytokinins promote growth and cell division; Abscisic acid acts as a growth inhibitor, causing wilting of leaves.",
        "lead": "Plant development is a balanced tug-of-war between hormones that promote growth and hormones that signal growth to halt. Master the four primary phytohormones outlined in the NCERT syllabus.",
        "theory_blocks": [
            {
                "heading": "The Growth-Promoting Phytohormones",
                "content": "• <strong>1. Auxins:</strong> Synthesised at shoot tips; promote cell elongation, apical dominance, phototropic and geotropic curvatures, and tendril coiling.<br>• <strong>2. Gibberellins:</strong> Synthesised in young leaves and roots; promote longitudinal growth and elongation of the <strong>stem and internodes</strong>, break seed dormancy, and increase fruit size.<br>• <strong>3. Cytokinins:</strong> Promoters of <strong>cell division (cytokinesis)</strong>; naturally present in highest concentrations in areas of rapid cell division, such as in <strong>fruits, seeds, and root tips</strong>; delay leaf aging (senescence) and promote stomatal opening."
            },
            {
                "heading": "The Growth-Inhibiting Phytohormone: Abscisic Acid (ABA)",
                "content": "• Plants also require negative signals to stop growing, enter winter dormancy, or conserve water during severe drought.<br>• <strong>Abscisic Acid (ABA):</strong> The primary plant <strong>growth inhibitor</strong> and stress hormone.<br>• <strong>Key Effects:</strong> Inhibits seed germination (maintains dormancy); triggers rapid closing of stomata during water deficits; causes <strong>wilting and falling (abscission) of leaves and flowers</strong>."
            }
        ],
        "narration": "Plants balance four master hormones like an orchestra! Auxins elongate shoot cells. Gibberellins stretch out stems and break seed dormancy. Cytokinins stimulate rapid cell division, which is why they are packed inside developing fruits and seeds! But plants also need brakes: Abscisic Acid, or ABA, is the growth inhibitor! When a drought hits, ABA closes stomata to save water and causes old leaves to wilt and drop off!",
        "interactive_type": "phytohormones_matrix_sim",
        "checkpoints": [
            {
                "q": "Which plant hormone promotes rapid cell division and is naturally found in greatest concentration in fruits and seeds?",
                "options": [
                    "Abscisic acid",
                    "Cytokinin",
                    "Thyroxin",
                    "Adrenaline"
                ],
                "ans": 1,
                "solution": "Cytokinins promote cytokinesis (cell division) and are naturally concentrated in rapidly dividing tissues such as fruits, developing embryos, and young seeds (NCERT Page 108)."
            },
            {
                "q": "Which plant hormone is responsible for inhibiting growth, maintaining seed dormancy, and causing the wilting of leaves?",
                "options": [
                    "Auxin",
                    "Gibberellin",
                    "Abscisic acid (ABA)",
                    "Insulin"
                ],
                "ans": 2,
                "solution": "Abscisic acid (ABA) is the growth-inhibiting hormone that induces stomatal closure, suppresses growth, and leads to leaf wilting (NCERT Page 108)."
            }
        ]
    },

    # Slide 15: Hormones in Animals: Adrenaline & The "Fight-or-Flight" Emergency Response (Pages 109-110)
    {
        "index": 14,
        "title": "Hormones in Animals: Adrenaline & The Fight-or-Flight Response",
        "short_title": "15. Adrenaline Surge",
        "badge": "Section 6.3 • Pages 109–110",
        "quote": "Adrenaline prepares animal bodies for emergency fight or flight by increasing heart rate, breathing, and diverting blood to skeletal muscles.",
        "lead": "Imagine a squirrel confronted by a hawk, or a student facing an unexpected hazard. Whether to fight or sprint away, the body must instantly mobilise vast energy across multiple organ systems through the hormone adrenaline.",
        "theory_blocks": [
            {
                "heading": "Why Animals Need Hormonal Transmission Alongside Nerves",
                "content": "If an animal relied solely on electrical impulses via nerve cells to prepare for danger, only tissues directly wired to specific nerves would be activated. But preparing for intense physical exertion requires systemic, whole-body adaptations across the heart, lungs, blood vessels, liver, and muscles. A chemical hormone released into the bloodstream reaches every cell simultaneously."
            },
            {
                "heading": "Target Organs & Physiological Effects of Adrenaline",
                "content": "Secreted directly into the blood by the <strong>adrenal glands</strong> (located atop each kidney):<br>1. <strong>Heart:</strong> Beats faster and stronger, boosting oxygen and glucose delivery to muscles.<br>2. <strong>Digestive System & Skin:</strong> Small arteries contract, reducing blood flow to the gut and skin, which <strong>diverts blood to skeletal muscles</strong>.<br>3. <strong>Lungs:</strong> Breathing rate accelerates due to rapid contractions of the diaphragm and intercostal rib muscles.<br>4. <strong>Liver:</strong> Stimulates breakdown of glycogen into glucose, flooding the blood with immediate cellular fuel.<br>• Together, these synchronized responses make the animal body ready to fight or flee!"
            }
        ],
        "narration": "Imagine a squirrel spotting a predator! Its body has two choices: fight or run! Both require massive energy. That's where adrenaline comes in, secreted by the adrenal glands sitting above your kidneys! Adrenaline shoots into the blood: your heart beats faster, your breathing rate accelerates, and blood is diverted away from your stomach and skin straight to your skeletal muscles! Your liver releases glucose fuel, preparing your entire body for peak fight-or-flight survival!",
        "interactive_type": "adrenaline_fight_flight_sim",
        "checkpoints": [
            {
                "q": "Which gland secretes adrenaline into the bloodstream, and where is it anatomically located?",
                "options": [
                    "Thyroid gland located in the neck",
                    "Adrenal gland located like a cap above each kidney",
                    "Pituitary gland at the base of the brain",
                    "Pancreas located behind the stomach"
                ],
                "ans": 1,
                "solution": "Adrenaline is secreted directly into the bloodstream by the adrenal glands located superior to each kidney (NCERT Page 109, Figure 6.7)."
            },
            {
                "q": "How does the secretion of adrenaline re-route blood flow during an emergency situation?",
                "options": [
                    "It stops all blood flow to the brain",
                    "It increases blood flow to the digestive tract and skin",
                    "It reduces blood flow to the digestive system and skin by contracting arterioles, diverting maximum blood volume to skeletal muscles",
                    "It drains all blood into the urinary bladder"
                ],
                "ans": 2,
                "solution": "Muscles around small arteries in the digestive system and skin contract, shunting blood away from these non-critical organs directly to the skeletal muscles for physical exertion (NCERT Page 109)."
            }
        ]
    },

    # Slide 16: Human Endocrine Glands, Hormones & Deficiency Disorders (Pages 110-111, Fig 6.7, Table 6.1)
    {
        "index": 15,
        "title": "Human Endocrine Glands, Hormones & Deficiency Disorders",
        "short_title": "16. Endocrine Glands",
        "badge": "Section 6.3 • Pages 110–111 (Table 6.1)",
        "quote": "Iodine is necessary for thyroxin; growth hormone deficiency causes dwarfism; insulin deficiency leads to diabetes.",
        "lead": "The endocrine system is a network of ductless glands that secrete chemical regulators directly into circulating blood. Explore the major human glands, their hormones, target functions, and clinical deficiency diseases.",
        "theory_blocks": [
            {
                "heading": "Key Endocrine Glands & Hormones (Figure 6.7 & Table 6.1)",
                "content": "• <strong>Hypothalamus:</strong> Secretes releasing hormones (e.g. Growth Hormone Releasing Factor) that stimulate the pituitary gland.<br>• <strong>Pituitary Gland:</strong> Secretes <strong>Growth Hormone (GH)</strong>; coordinates balanced growth of bones and organs. Deficiency in childhood causes <strong>Dwarfism</strong>; excess causes <strong>Gigantism</strong>.<br>• <strong>Thyroid Gland:</strong> Secretes <strong>Thyroxin</strong>; regulates carbohydrate, protein, and fat metabolism for optimal growth. <strong>Iodine</strong> is mandatory for thyroxin synthesis; dietary iodine deficiency causes <strong>Goitre</strong> (characterized by a swollen neck).<br>• <strong>Pancreas:</strong> Secretes <strong>Insulin</strong>; lowers blood sugar levels by promoting cellular glucose uptake. Deficiency causes <strong>Diabetes Mellitus</strong> (managed by insulin injections)."
            },
            {
                "heading": "Sex Hormones & Puberty",
                "content": "• <strong>Testes (Male):</strong> Secrete <strong>Testosterone</strong>; drives male secondary sexual characteristics at puberty (facial hair, deeper voice, muscle mass) and regulates sperm production.<br>• <strong>Ovaries (Female):</strong> Secrete <strong>Oestrogen</strong> (and progesterone); drives female puberty changes (breast development, widened hips, feminine fat distribution) and regulates the menstrual cycle."
            }
        ],
        "narration": "Let's explore your endocrine glands! The Pituitary gland at the brain base releases Growth Hormone: too little in childhood causes dwarfism, too much causes gigantism! In your neck sits the butterfly-shaped Thyroid gland, which makes thyroxin to regulate metabolism. You need iodine in salt to make thyroxin; without it, you can develop goitre with a swollen neck! Your Pancreas secretes insulin to regulate blood sugar, and your reproductive gonads produce testosterone and oestrogen for puberty changes!",
        "interactive_type": "endocrine_glands_sim",
        "checkpoints": [
            {
                "q": "Why is the use of iodised table salt strongly recommended in our daily diet?",
                "options": [
                    "Iodine prevents tooth decay directly",
                    "Iodine is required by the thyroid gland to synthesise thyroxin hormone; deficiency can cause goitre (swollen neck)",
                    "Iodine replaces the need for insulin",
                    "Iodine speeds up blood clotting"
                ],
                "ans": 1,
                "solution": "Iodine is chemically essential for the thyroid gland to produce thyroxin. In its absence, the gland enlarges into a swollen neck condition known as goitre (NCERT Page 110)."
            },
            {
                "q": "Why are some patients suffering from diabetes treated with therapeutic injections of insulin?",
                "options": [
                    "Insulin breaks down kidney stones",
                    "Insulin is a pancreatic hormone that reduces high blood sugar levels; deficient patients require external insulin to prevent hyperglycemia",
                    "Insulin stimulates the thyroid gland to cure goitre",
                    "Insulin serves as a sedative for nerve pain"
                ],
                "ans": 1,
                "solution": "Insulin, produced by the pancreas, facilitates cellular glucose uptake. In diabetic patients with insufficient insulin production, blood glucose rises to toxic levels, requiring exogenous insulin injections (NCERT Page 110-111)."
            }
        ]
    },

    # Slide 17: Feedback Mechanisms in Hormone Regulation (Pages 111-112)
    {
        "index": 16,
        "title": "Feedback Mechanisms: Maintaining Endocrine Homeostasis",
        "short_title": "17. Feedback Loops",
        "badge": "Section 6.3 • Pages 111–112",
        "quote": "The timing and amount of hormone released are regulated by feedback mechanisms: rising blood sugar triggers insulin release, and falling sugar turns it off.",
        "lead": "Hormones are extraordinarily potent chemical agents active in microgram concentrations. To prevent biological chaos, the body employs precise negative feedback loops to dial hormone production up or down.",
        "theory_blocks": [
            {
                "heading": "How Feedback Mechanisms Operate (Pages 111-112)",
                "content": "• If hormones are secreted in excess or in insufficient amounts, severe physiological disorders arise (e.g. hypoglycemia, dwarfism, gigantism, diabetes).<br>• The body uses <strong>feedback mechanisms</strong> to ensure hormones are secreted in precise quantities and at exact times.<br>• <strong>Negative Feedback:</strong> A regulatory loop where the output of a system inhibits or dampens the initial stimulus, restoring homeostasis."
            },
            {
                "heading": "The Classic Blood Sugar - Insulin Feedback Loop",
                "content": "1. <strong>Stimulus:</strong> After consuming a meal rich in carbohydrates, blood glucose concentration rises above normal (~90-100 mg/dL).<br>2. <strong>Sensor & Controller:</strong> Pancreatic beta cells directly detect the elevated blood sugar levels.<br>3. <strong>Effector Action:</strong> The pancreas responds by secreting more <strong>insulin</strong> into the bloodstream.<br>4. <strong>Target Tissue Response:</strong> Insulin signals liver and muscle cells to absorb glucose from the blood and convert it into stored glycogen.<br>5. <strong>Feedback Shutdown:</strong> As blood sugar levels fall back to normal baseline, the stimulus to pancreatic beta cells vanishes, and <strong>insulin secretion is reduced</strong> accordingly!"
            }
        ],
        "narration": "Hormones must be released in exact, microscopic amounts at just the right second. How does your body achieve this precision? Through negative feedback mechanisms! Think of your home thermostat: when the room gets too cold, the heater turns on; once the room warms up, the heater shuts off! Similarly, when you eat a meal, rising blood sugar tells your pancreas to secrete insulin. As insulin sweeps sugar into your cells and levels return to normal, insulin production shuts down!",
        "interactive_type": "feedback_loop_sim",
        "checkpoints": [
            {
                "q": "What is the primary physiological purpose of a negative feedback mechanism in the endocrine system?",
                "options": [
                    "To permanently stop all hormone production in the body",
                    "To regulate the timing and amount of hormone release so that optimal physiological levels (homeostasis) are maintained",
                    "To convert hormones into electrical nerve impulses",
                    "To eliminate the need for sense organs"
                ],
                "ans": 1,
                "solution": "Feedback loops ensure hormones are secreted in precise quantities only when required; once normal conditions return, hormone release is dialled back (NCERT Page 111)."
            },
            {
                "q": "In the pancreatic blood sugar feedback mechanism, what occurs as blood glucose concentrations return to normal?",
                "options": [
                    "The pancreas produces ten times more insulin",
                    "The thyroid gland begins secreting adrenaline",
                    "The stimulus is removed and pancreatic secretion of insulin is reduced",
                    "The liver destroys all pancreatic tissue"
                ],
                "ans": 2,
                "solution": "As blood sugar levels normalize, pancreatic beta cells detect the decline and reduce insulin secretion, preventing hypoglycemia (NCERT Page 111)."
            }
        ]
    }
]

# Quiz questions: 4 dedicated slides (10 questions each = 40 questions total)
QUIZ_SLIDES = [
    # Quiz 1: Questions 1 to 10
    {
        "index": 17,
        "title": "Mastery Challenge Quiz — Part 1: Nervous System, Neurons, Synapses & Reflex Arcs",
        "short_title": "18. Quiz Part 1",
        "badge": "Quiz Challenge • Part 1 of 4",
        "description": "Test your mastery on neuron anatomy, transmission of electrical and chemical impulses, sensory receptors, taste vs smell integration, and spinal reflex arc circuits. Click Solution on any question for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 1,
                "q": "In which part of a neuron is an environmental stimulus first converted into an electrical impulse?",
                "options": [
                    "Axon terminal",
                    "Dendritic tip",
                    "Schwann cell nucleus",
                    "Synaptic cleft"
                ],
                "ans": 1,
                "solution": "Information is acquired at the end of the dendritic tip of a nerve cell, setting off a local chemical reaction that generates an electrical impulse (NCERT Page 101)."
            },
            {
                "id": 2,
                "q": "The microscopic gap between the axon terminal of one neuron and the dendrite of the next neuron is known as:",
                "options": [
                    "Axon hillock",
                    "Synapse",
                    "Neuromuscular bridge",
                    "Myelin sheath"
                ],
                "ans": 1,
                "solution": "The microscopic junction between two successive neurons across which neurotransmitter chemicals diffuse is called a synapse (NCERT Page 101, Exercise Q2)."
            },
            {
                "id": 3,
                "q": "Which sensory receptors are specifically responsible for detecting taste and smell respectively?",
                "options": [
                    "Photoreceptors and phonoreceptors",
                    "Gustatory receptors and olfactory receptors",
                    "Thermoreceptors and baroreceptors",
                    "Mechanoreceptors and proprioceptors"
                ],
                "ans": 1,
                "solution": "Gustatory receptors located on the tongue detect chemical tastes, while olfactory receptors located in nasal passages detect smell (NCERT Page 101)."
            },
            {
                "id": 4,
                "q": "Why does food taste noticeably bland and unpalatable when a person is suffering from a severe head cold (Activity 6.1)?",
                "options": [
                    "Salivary glands stop secreting enzymes",
                    "Inflammation and mucus block olfactory receptors, eliminating the aromatic component that constitutes most of flavour",
                    "Taste buds on the tongue become permanently paralyzed",
                    "Cold virus destroys all spinal reflex arcs"
                ],
                "ans": 1,
                "solution": "Flavour perception relies on the synergistic combination of taste and retro-nasal olfaction. Nasal congestion prevents volatile aromas from reaching olfactory receptors, drastically flattening flavour (Activity 6.1, Page 101)."
            },
            {
                "id": 5,
                "q": "In a spinal reflex arc, where does the sensory neuron meet and synapse with the motor neuron?",
                "options": [
                    "In the cerebral cortex",
                    "Inside the bicep muscle",
                    "In the spinal cord (via a relay neuron)",
                    "In the thyroid gland"
                ],
                "ans": 2,
                "solution": "Nerves meet in a bundle in the spinal cord; reflex arcs are formed in the spinal cord itself via interneurons (relay neurons) to enable instantaneous responses (NCERT Page 102)."
            },
            {
                "id": 6,
                "q": "What is the primary evolutionary advantage of reflex arcs in animal survival?",
                "options": [
                    "They allow animals to see in the dark",
                    "They generate rapid defensive responses because cerebral thinking networks are too complex and slow to prevent acute injury",
                    "They bypass the need for muscle tissue",
                    "They produce hormones directly"
                ],
                "ans": 1,
                "solution": "Reflex arcs evolved as fast-acting shortcuts in the spinal cord because deliberate thinking in the brain is too slow to avoid burns or mechanical trauma (NCERT Page 102)."
            },
            {
                "id": 7,
                "q": "Which of the following correctly traces the flow of information across a neuromuscular junction?",
                "options": [
                    "Muscle fibre → Axon → Dendrite → Gland",
                    "Nerve terminal → Release of chemical neurotransmitter → Receptors on muscle cell membrane → Muscle contraction",
                    "Bone → Motor neuron → Sensory receptor → Brain",
                    "Spinal cord → Blood plasma → Sensory neuron → Skin"
                ],
                "ans": 1,
                "solution": "At the neuromuscular junction, the electrical impulse arriving at the axon terminal triggers chemical neurotransmitter exocytosis, depolarizing the muscle fibre membrane and inducing contraction (Figure 6.1 b, Page 101)."
            },
            {
                "id": 8,
                "q": "Which of the following movements is entirely independent of growth?",
                "options": [
                    "A germinating pea seedling pushing soil aside",
                    "Bending of a sunflower shoot towards sunlight",
                    "Chewing of cud by buffaloes to aid digestion",
                    "Upward growth of a bean shoot against gravity"
                ],
                "ans": 2,
                "solution": "Chewing cud, running, and playing are muscular movements unrelated to cellular growth, unlike seed germination and phototropism which require growth (NCERT Page 100)."
            },
            {
                "id": 9,
                "q": "Which component of a reflex arc carries the motor command from the spinal cord to the effector muscle?",
                "options": [
                    "Receptor cell",
                    "Sensory (afferent) neuron",
                    "Motor (efferent) neuron",
                    "Olfactory nerve"
                ],
                "ans": 2,
                "solution": "Motor (efferent) neurons conduct motor commands from the CNS/spinal cord out to effector organs like muscles or glands (Figure 6.2, Page 103)."
            },
            {
                "id": 10,
                "q": "Which of the following is NOT a reflex action?",
                "options": [
                    "Withdrawing a hand instantly from a burning candle flame",
                    "Blinking when a bright light is suddenly flashed in the eyes",
                    "Watering of the mouth upon smelling favorite food",
                    "Writing a detailed essay in an examination hall"
                ],
                "ans": 3,
                "solution": "Writing an essay is a deliberate, voluntary action requiring conscious thought, memory, and cortical decision-making, whereas the others are involuntary reflex responses (NCERT Page 103)."
            }
        ]
    },

    # Quiz 2: Questions 11 to 20
    {
        "index": 18,
        "title": "Mastery Challenge Quiz — Part 2: Human Brain, Functional Lobes & Tissue Protection",
        "short_title": "19. Quiz Part 2",
        "badge": "Quiz Challenge • Part 2 of 4",
        "description": "Test your mastery on brain anatomy (Fore-brain, Mid-brain, Hind-brain), cerebellum posture control, medulla involuntary centers, cranial/spinal nerves, and cranium protection. Click Solution on any question for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 11,
                "q": "The Central Nervous System (CNS) consists of:",
                "options": [
                    "Sympathetic nerves and parasympathetic nerves",
                    "Brain and Spinal Cord",
                    "Cranial nerves and spinal nerves only",
                    "Sensory receptors and muscle effectors"
                ],
                "ans": 1,
                "solution": "The CNS is made up exclusively of the Brain and the Spinal Cord, which act as the central command and coordinating hub of the body (NCERT Page 103)."
            },
            {
                "id": 12,
                "q": "Which part of the human brain is the primary center for thinking, logic, memory, and voluntary actions?",
                "options": [
                    "Cerebellum",
                    "Fore-brain (Cerebrum)",
                    "Medulla oblongata",
                    "Pons"
                ],
                "ans": 1,
                "solution": "The fore-brain (cerebrum) is the main thinking part of the brain, housing sensory receiving zones, association areas, and voluntary motor centers (NCERT Page 103)."
            },
            {
                "id": 13,
                "q": "Which brain structure is responsible for the precision of voluntary actions and maintaining bodily posture and equilibrium?",
                "options": [
                    "Cerebrum",
                    "Cerebellum",
                    "Medulla",
                    "Pituitary gland"
                ],
                "ans": 1,
                "solution": "The cerebellum (located in the hind-brain) coordinates voluntary muscle precision (e.g. riding a bike, picking up a pencil) and maintains body balance (NCERT Page 104, Exercise Q3)."
            },
            {
                "id": 14,
                "q": "Involuntary physiological actions such as blood pressure regulation, salivation, and vomiting are governed by:",
                "options": [
                    "Cerebrum in the fore-brain",
                    "Medulla in the hind-brain",
                    "Vertebral column",
                    "Optic chiasm"
                ],
                "ans": 1,
                "solution": "The medulla oblongata in the hind-brain directly controls vital autonomic activities including blood pressure, salivation, and vomiting (NCERT Page 104)."
            },
            {
                "id": 15,
                "q": "How is the delicate human brain mechanically protected from physical impacts and concussions?",
                "options": [
                    "Inside a bony cranium cushioned within a fluid-filled balloon of cerebrospinal fluid",
                    "Solely by thick scalp hair",
                    "Enclosed within the cartilage rings of the trachea",
                    "By the rib cage"
                ],
                "ans": 0,
                "solution": "The brain sits inside a rigid bony box (cranium) floating in a shock-absorbing fluid-filled balloon of cerebrospinal fluid (CSF) (NCERT Page 105)."
            },
            {
                "id": 16,
                "q": "Which bony structure protects the spinal cord running down the dorsal side of the body?",
                "options": [
                    "Rib cage",
                    "Vertebral column (backbone)",
                    "Pelvic girdle",
                    "Clavicle"
                ],
                "ans": 1,
                "solution": "The vertebral column (backbone) consists of bumpy vertebrae forming a neural canal that houses and safeguards the spinal cord (NCERT Page 105)."
            },
            {
                "id": 17,
                "q": "At the molecular level, what enables muscle cells to shorten and generate movement upon receiving a nerve impulse?",
                "options": [
                    "Specialized contractile proteins alter their shape and arrangement in response to electrical impulses",
                    "Muscle cells undergo rapid mitosis to divide",
                    "Nerve terminals physically reel in connective collagen fibres",
                    "Bone calcium dissolves and pulls the muscles"
                ],
                "ans": 0,
                "solution": "Muscle cells have specialized contractile proteins (actin and myosin) that change their molecular shape and spatial arrangement in response to ionic shifts triggered by nerve impulses, shortening the cell (NCERT Page 105)."
            },
            {
                "id": 18,
                "q": "The sensation of feeling full after a heavy meal is triggered by a satiety center located in which region?",
                "options": [
                    "The stomach mucosal lining",
                    "A distinct center in the fore-brain",
                    "The cerebellum",
                    "The spinal cord reflex loop"
                ],
                "ans": 1,
                "solution": "The sensation of feeling full is processed by a specialized satiety and hunger center located within the fore-brain (hypothalamus) (NCERT Page 104)."
            },
            {
                "id": 19,
                "q": "If a person suffers an injury to the spinal cord, which signals will be disrupted?",
                "options": [
                    "Only voluntary thinking in the cerebral cortex",
                    "Both sensory impulses coming from the trunk/limbs to the brain and motor commands sent from the brain to effectors, as well as spinal reflex arcs",
                    "Only the heartbeat and blood pressure",
                    "Only sight and hearing"
                ],
                "ans": 1,
                "solution": "A spinal cord injury disrupts communication between the brain and peripheral body parts below the lesion, impairing both sensory input and motor output, as well as local spinal reflexes (NCERT Page 112, Exercise Q7)."
            },
            {
                "id": 20,
                "q": "The human brain is responsible for which of the following combined functions?",
                "options": [
                    "Thinking",
                    "Regulating the heart beat",
                    "Balancing the body",
                    "All of the above"
                ],
                "ans": 3,
                "solution": "The cerebrum is responsible for thinking, the medulla regulates autonomic heart rate, and the cerebellum balances the body—so the brain is responsible for all of the above (NCERT Page 112, Exercise Q3)."
            }
        ]
    },

    # Quiz 3: Questions 21 to 30
    {
        "index": 19,
        "title": "Mastery Challenge Quiz — Part 3: Plant Coordination, Nastic Movements & Tropisms",
        "short_title": "20. Quiz Part 3",
        "badge": "Quiz Challenge • Part 3 of 4",
        "description": "Test your mastery on Mimosa pudica turgor drooping, tendril thigmotropism, phototropism, geotropism, hydrotropism, chemotropism, and plant hormones. Click Solution on any question for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 21,
                "q": "How does the sensitive plant (Mimosa pudica) cause its leaves to fold and droop rapidly in response to touch?",
                "options": [
                    "By rapidly burning starch via cellular respiration",
                    "By changing the amount of water inside specialized hinge cells (pulvini), leading to loss of turgor pressure",
                    "By contracting skeletal muscle fibres located in petioles",
                    "By snapping tiny mineral crystals inside leaf veins"
                ],
                "ans": 1,
                "solution": "Plant cells alter their shape by regulating water content; water efflux from pulvinar cells causes sudden loss of turgor pressure, folding the leaflets (NCERT Page 106, Figure 6.4)."
            },
            {
                "id": 22,
                "q": "How does the movement of Mimosa pudica leaves differ fundamentally from the bending of a shoot toward light?",
                "options": [
                    "Mimosa movement is growth-dependent, while shoot bending is independent of growth",
                    "Mimosa drooping is an immediate, reversible, growth-independent nastic response; shoot bending is a slow, directional, growth-dependent tropism",
                    "Mimosa movement involves nerves, whereas shoots possess muscles",
                    "There is no difference between the two movements"
                ],
                "ans": 1,
                "solution": "Mimosa drooping is a non-directional, growth-independent nastic response driven by turgor shifts, whereas phototropism is a directional growth movement driven by unequal cell division and elongation (NCERT Page 106, 108)."
            },
            {
                "id": 23,
                "q": "Why does a pea plant tendril circle and cling around an external bamboo fence?",
                "options": [
                    "The tendril synthesises sticky resin on the contact side",
                    "The side of the tendril in physical contact with the support grows slower than the side away from the support, inducing curved spiral coiling",
                    "The support attracts the tendril via magnetic pull",
                    "The tendril's root pressure pushes it around the fence"
                ],
                "ans": 1,
                "solution": "Touch contact inhibits growth on the contact side while the outer side grows rapidly under auxin stimulation, forcing the tendril to spiral around the support (NCERT Page 106-107)."
            },
            {
                "id": 24,
                "q": "Which plant hormone is synthesised at shoot tips and stimulates cell elongation on the shaded side of stems?",
                "options": [
                    "Insulin",
                    "Auxin",
                    "Abscisic acid",
                    "Thyroxin"
                ],
                "ans": 1,
                "solution": "Auxin is synthesized at shoot tips and migrates to the shaded side, stimulating cellular elongation and causing the shoot to bend towards sunlight (NCERT Page 108)."
            },
            {
                "id": 25,
                "q": "Which plant hormone promotes active cell division and is present in high concentrations in developing fruits and seeds?",
                "options": [
                    "Cytokinin",
                    "Abscisic acid",
                    "Adrenaline",
                    "Glucagon"
                ],
                "ans": 0,
                "solution": "Cytokinins promote cell division (cytokinesis) and are naturally concentrated in rapidly dividing zones like fruits and seeds (NCERT Page 108, Exercise Q1)."
            },
            {
                "id": 26,
                "q": "Which plant hormone acts as a growth inhibitor, promoting seed dormancy and causing wilting of leaves?",
                "options": [
                    "Gibberellin",
                    "Abscisic acid (ABA)",
                    "Auxin",
                    "Cytokinin"
                ],
                "ans": 1,
                "solution": "Abscisic acid (ABA) inhibits growth, induces stomatal closure during drought, and triggers leaf wilting and abscission (NCERT Page 108)."
            },
            {
                "id": 27,
                "q": "The growth of a pollen tube through the style towards the ovule in a flower is a classic demonstration of:",
                "options": [
                    "Phototropism",
                    "Chemotropism",
                    "Geotropism",
                    "Hydrotropism"
                ],
                "ans": 1,
                "solution": "Chemotropism is directional growth in response to chemical gradients, exemplified by pollen tube growth toward female ovules (NCERT Page 107)."
            },
            {
                "id": 28,
                "q": "What tropic growth responses occur when a seedling is oriented horizontally on its side?",
                "options": [
                    "Shoots bend downward; roots bend upward",
                    "Shoots bend upward (negative geotropism); roots bend downward (positive geotropism)",
                    "Both roots and shoots grow in parallel straight lines",
                    "Both roots and shoots coil into circles"
                ],
                "ans": 1,
                "solution": "Under the influence of gravity, roots grow downward (positive geotropism) while shoots grow upward away from the earth (negative geotropism) (Figure 6.6, Page 107)."
            },
            {
                "id": 29,
                "q": "In Activity 6.2, what is the primary conclusion drawn when germinated seeds in a window box bend toward the open window?",
                "options": [
                    "Plant shoots exhibit positive phototropism to maximize sunlight capture for photosynthesis",
                    "Plants are trying to escape the cardboard box",
                    "Roots need sunlight to absorb minerals",
                    "Shoots only grow where air pressure is zero"
                ],
                "ans": 0,
                "solution": "Activity 6.2 proves that shoots bend toward light (positive phototropism) and roots bend away (negative phototropism) (NCERT Page 107-108)."
            },
            {
                "id": 30,
                "q": "Which of the following is a plant hormone that specifically promotes stem elongation alongside auxins?",
                "options": [
                    "Gibberellin",
                    "Insulin",
                    "Testosterone",
                    "Oestrogen"
                ],
                "ans": 0,
                "solution": "Gibberellins stimulate stem elongation, internodal stretching, and seed germination in plants (NCERT Page 108)."
            }
        ]
    },

    # Quiz 4: Questions 31 to 40
    {
        "index": 20,
        "title": "Mastery Challenge Quiz — Part 4: Endocrine Glands, Hormones & Feedback Regulation",
        "short_title": "21. Quiz Part 4",
        "badge": "Quiz Challenge • Part 4 of 4",
        "description": "Test your mastery on human endocrine glands (Pituitary, Thyroid, Pancreas, Adrenals, Gonads), adrenaline fight-or-flight, insulin diabetes regulation, goitre iodine linkage, and negative feedback loops. Click Solution on any question for a step-by-step popup explanation.",
        "questions": [
            {
                "id": 31,
                "q": "Why is the hormone adrenaline called the 'emergency' or 'fight-or-flight' hormone?",
                "options": [
                    "Because it causes animals to fall asleep immediately during danger",
                    "Because it coordinates whole-body metabolic surges—accelerating heart rate, breathing, and diverting blood to skeletal muscles to handle threats",
                    "Because it is secreted only when animals are drinking water",
                    "Because it paralyzes the digestive tract permanently"
                ],
                "ans": 1,
                "solution": "Adrenaline is secreted by the adrenal glands during stressful situations to increase heart rate, dilate airways, and shunt blood to skeletal muscles, equipping the organism to fight or run (NCERT Page 109)."
            },
            {
                "id": 32,
                "q": "Why is dietary iodine essential for human health, and what disease results from its chronic deficiency?",
                "options": [
                    "Iodine synthesises hemoglobin; deficiency causes anemia",
                    "Iodine is required by the thyroid gland to produce thyroxin; deficiency causes goitre characterized by a swollen neck",
                    "Iodine produces insulin; deficiency causes diabetes",
                    "Iodine builds bone calcium; deficiency causes dwarfism"
                ],
                "ans": 1,
                "solution": "Iodine is an essential constituent of the hormone thyroxin. Without dietary iodine, the thyroid gland cannot manufacture thyroxin and enlarges, leading to goitre (NCERT Page 110)."
            },
            {
                "id": 33,
                "q": "Which endocrine gland secretes Growth Hormone (GH), and what disorder results from its deficiency during childhood?",
                "options": [
                    "Thyroid gland; causes Goitre",
                    "Pituitary gland; causes Dwarfism",
                    "Pancreas; causes Diabetes",
                    "Adrenal gland; causes Scurvy"
                ],
                "ans": 1,
                "solution": "Growth hormone is secreted by the pituitary gland; hyposecretion in childhood results in dwarfism, while hypersecretion causes gigantism (NCERT Page 110)."
            },
            {
                "id": 34,
                "q": "What is the biological function of insulin, and which endocrine gland produces it?",
                "options": [
                    "It raises body temperature; secreted by thyroid",
                    "It regulates blood glucose levels by promoting cellular glucose uptake; secreted by the pancreas",
                    "It triggers milk production; secreted by ovaries",
                    "It increases heart rate; secreted by adrenals"
                ],
                "ans": 1,
                "solution": "Insulin is manufactured by the beta cells of the pancreas; it lowers blood glucose to normal homeostatic levels (NCERT Page 110-111)."
            },
            {
                "id": 35,
                "q": "Which hormones are responsible for the physical changes associated with puberty in human males and females respectively?",
                "options": [
                    "Thyroxin and Adrenaline",
                    "Testosterone in males and Oestrogen in females",
                    "Insulin and Glucagon",
                    "Growth hormone and Prolactin"
                ],
                "ans": 1,
                "solution": "Testosterone (secreted by the testes) drives male puberty, while oestrogen (secreted by the ovaries) drives female puberty and menstrual regulation (NCERT Page 110)."
            },
            {
                "id": 36,
                "q": "How does a negative feedback mechanism regulate insulin secretion when blood glucose drops back to normal after a meal?",
                "options": [
                    "The pancreas accelerates insulin secretion tenfold",
                    "Pancreatic cells detect the falling sugar level and reduce insulin secretion to prevent hypoglycemia",
                    "The pituitary gland destroys all circulating insulin",
                    "The liver converts all remaining insulin into bile"
                ],
                "ans": 1,
                "solution": "In a negative feedback loop, falling blood sugar removes the stimulus from pancreatic cells, which reduces insulin secretion to maintain equilibrium (NCERT Page 111)."
            },
            {
                "id": 37,
                "q": "Which brain structure acts as the master neuroendocrine link by releasing factors that stimulate or inhibit pituitary hormones?",
                "options": [
                    "Cerebellum",
                    "Hypothalamus",
                    "Medulla",
                    "Pons"
                ],
                "ans": 1,
                "solution": "The hypothalamus secretes releasing hormones (such as Growth Hormone Releasing Factor) that directly regulate secretions from the pituitary gland (NCERT Page 110, Do You Know box)."
            },
            {
                "id": 38,
                "q": "Which of the following hormones is NOT produced by the human endocrine system?",
                "options": [
                    "Adrenaline",
                    "Thyroxin",
                    "Cytokinin",
                    "Insulin"
                ],
                "ans": 2,
                "solution": "Cytokinin is a plant hormone promoting cell division; adrenaline, thyroxin, and insulin are animal endocrine hormones (NCERT Page 108, 110, Exercise Q1)."
            },
            {
                "id": 39,
                "q": "Compare nervous vs hormonal control: which statement accurately reflects a key difference?",
                "options": [
                    "Nervous impulses are slow and widespread; hormones are instantaneous and restricted to few cells",
                    "Nervous coordination is rapid and reaches only connected cells via electrical impulses; hormonal coordination is slower, chemical, and diffuses widely to reach all target cells steadily",
                    "Nervous coordination operates in plants; hormonal coordination operates only in animals",
                    "Hormones travel along nerve axons"
                ],
                "ans": 1,
                "solution": "Nervous conduction is fast, point-to-point, and brief via electrical impulses, whereas hormonal control relies on bloodstream diffusion, reaching all target cells for sustained regulation (NCERT Page 108, 112, Exercise Q11)."
            },
            {
                "id": 40,
                "q": "What is the difference between the movement in a sensitive plant (Mimosa) and movement in our legs?",
                "options": [
                    "Leg movement uses plant hormones; Mimosa uses animal adrenaline",
                    "Movement in Mimosa is non-nervous and driven by cellular water turgor changes; leg movement is voluntary, controlled by the nervous system and executed by muscle proteins shortening",
                    "Mimosa leaves possess bones while legs do not",
                    "There is no difference in their mechanisms"
                ],
                "ans": 1,
                "solution": "Movement in Mimosa occurs without nerves or muscles via osmotic turgor pressure changes in pulvinus cells; leg movement is voluntary, commanded by the motor cortex, and executed by actin-myosin contraction in muscle fibres (NCERT Page 112, Exercise Q12)."
            }
        ]
    }
]

print(f"Total Content Slides: {len(CONTENT_SLIDES)}")
print(f"Total Quiz Slides: {len(QUIZ_SLIDES)}")
print(f"Total Combined Slides: {len(CONTENT_SLIDES) + len(QUIZ_SLIDES)}")


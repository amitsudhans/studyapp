#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 for NCERT Class 10 Science Chapter 6: Control and Coordination.
Strict requirements:
- Titles: 1-3 words
- Silent: speech = ""
- 10 challenge questions per slide (total 40 questions)
- Each question has 4 options, hint, explanation, and 3 solution steps
- Zero persona titles (Dr, Sir, Madam, Mr, Mrs, Prof) and zero fictional character names
"""

import json

slides_part3 = [
    {
        "id": 17,
        "title": "Neural Reflex Review",
        "subtitle": "Sensory Receptors, Synapses & Spinal Reflex Arcs",
        "speech": "",
        "questions": [
            {
                "question": "Which sense organs contain gustatory and olfactory receptors respectively in the human body?",
                "options": [
                    "Tongue for taste and nasal cavity for smell",
                    "Retina for vision and cochlea for hearing",
                    "Skin for temperature and semicircular canals for balance",
                    "Coronary arteries for blood pressure and lungs for respiration"
                ],
                "answer": 0,
                "hint": "Gustation relates to tasting food; olfaction relates to detecting aromas.",
                "explanation": "Gustatory receptors are situated in the taste buds of the tongue; olfactory receptors line the nasal cavity.",
                "solution_steps": [
                    "Step 1: Identify that gustatory receptors detect dissolved chemical tastants on the tongue.",
                    "Step 2: Identify that olfactory receptors detect volatile airborne odorants in the olfactory epithelium of the nose.",
                    "Step 3: Conclude that the tongue and nasal cavity house gustatory and olfactory receptors respectively."
                ]
            },
            {
                "question": "What is the sequence of events when an electrical impulse reaches the axonal tip of a neuron?",
                "options": [
                    "Chemical neurotransmitters are released across the synapse to start an electrical impulse in the next dendrite",
                    "The electrical impulse immediately jumps across the bone to the spinal cord without chemical release",
                    "The cell body converts the electrical impulse into insoluble calcium phosphate crystals",
                    "The axon terminal permanently fuses with the adjacent neuron's nucleus"
                ],
                "answer": 0,
                "hint": "The electrical signal triggers chemical release across the microscopic synaptic cleft.",
                "explanation": "At the axon terminal, the electrical impulse releases neurotransmitters that diffuse across the synapse to trigger an impulse in the next neuron.",
                "solution_steps": [
                    "Step 1: Note that neurons are separated by microscopic fluid-filled gaps called synapses.",
                    "Step 2: Understand that an electrical impulse arriving at an axon tip causes synaptic vesicles to release neurotransmitter chemicals.",
                    "Step 3: Conclude that these chemicals diffuse across the cleft, binding to receptors on the next dendrite to generate a new electrical signal."
                ]
            },
            {
                "question": "In Activity 6.1, why does blocking your nose while eating a sugar cube impair the full appreciation of its flavor?",
                "options": [
                    "Flavor perception combines both gustatory taste and olfactory aroma signals",
                    "Blocking the nose stops all salivary amylase production in the buccal cavity",
                    "Nasal blockage prevents oxygen from diffusing into tongue muscle fibers",
                    "Sugar crystals can only dissolve when air flows through the trachea"
                ],
                "answer": 0,
                "hint": "Flavors are complex sensations integrating both smell and taste.",
                "explanation": "Complete flavor perception requires simultaneous olfactory and gustatory inputs; blocking the nose eliminates the olfactory contribution.",
                "solution_steps": [
                    "Step 1: Recognize that the tongue detects simple taste modalities: sweet, sour, salty, bitter, and umami.",
                    "Step 2: Note that complex food flavors rely heavily on volatile aromatic molecules reaching olfactory receptors via the nasopharynx.",
                    "Step 3: Conclude that occluding nasal airflow blocks olfactory inputs, dulling the sensory richness of food."
                ]
            },
            {
                "question": "What is the evolutionary significance of spinal reflex arcs in animal physiology?",
                "options": [
                    "They provide immediate, involuntary protective responses before slow conscious brain processing can occur",
                    "They allow animals to digest cellulose without requiring a long small intestine",
                    "They eliminate the need for red blood cells and haemoglobin during physical sprinting",
                    "They convert sensory nerve endings into photosynthetic chloroplast thylakoids"
                ],
                "answer": 0,
                "hint": "Processing through conscious cerebral neural networks takes too long to prevent sudden injury.",
                "explanation": "Reflex arcs evolved as rapid emergency circuits that bypass slow cognitive brain processing to protect the body from trauma.",
                "solution_steps": [
                    "Step 1: Recognize that conscious decision-making involves millions of synaptic relays across cerebral networks.",
                    "Step 2: Understand that in emergency hazards (like touching fire), cerebral latency would result in severe tissue damage.",
                    "Step 3: Conclude that direct spinal sensory-to-motor relay circuits evolved to execute instantaneous protective withdrawals."
                ]
            },
            {
                "question": "Which of the following correctly traces the complete path of a spinal reflex arc when touching a hot flame?",
                "options": [
                    "Heat receptor in skin -> Sensory neuron -> Relay neuron in spinal cord -> Motor neuron -> Biceps muscle (Effector)",
                    "Effector muscle -> Motor neuron -> Spinal cord -> Sensory neuron -> Heat receptor in skin",
                    "Sensory neuron -> Brain cerebrum -> Olfactory lobe -> Motor neuron -> Trachea",
                    "Skin receptor -> Cranium -> Cerebrospinal fluid -> Spinal nerve -> Optic nerve"
                ],
                "answer": 0,
                "hint": "Trace the unidirectional flow from stimulus detection to effector muscle contraction.",
                "explanation": "The pathway proceeds from receptor to sensory neuron, relay neuron in the spinal cord, motor neuron, and effector muscle.",
                "solution_steps": [
                    "Step 1: Identify that thermal pain receptors in the skin detect the noxious heat stimulus.",
                    "Step 2: Follow the action potential along the afferent sensory neuron into the dorsal horn of the spinal cord.",
                    "Step 3: Note the synapse with an interneuron (relay neuron) that activates an efferent motor neuron to contract the effector biceps."
                ]
            },
            {
                "question": "What happens if the spinal cord is physically injured in an accident?",
                "options": [
                    "Signals for reflex actions and communication between the brain and peripheral body parts are disrupted",
                    "The heart stops beating immediately because the heart muscle is innervated exclusively by the spinal cord",
                    "The liver loses its ability to store glucose as glycogen entirely",
                    "The kidneys cannot filter blood because nephrons are located inside the vertebral column"
                ],
                "answer": 0,
                "hint": "The spinal cord is the main neural trunk relaying sensory input up to the brain and motor commands down.",
                "explanation": "Spinal cord transection impairs both local reflex arcs and the transmission of sensory/motor signals between brain and body.",
                "solution_steps": [
                    "Step 1: Identify the spinal cord as the central nervous trunk housing reflex arcs and ascending/descending tracts.",
                    "Step 2: Recognize that damage interrupts both incoming sensory inputs from limbs and descending motor commands from the brain.",
                    "Step 3: Conclude that sensation, voluntary movement, and spinal reflexes below the lesion level are severely impaired."
                ]
            },
            {
                "question": "How does an electrical impulse travel within a single neuron from reception to transmission?",
                "options": [
                    "Dendritic tip -> Cell body -> Axon -> Axon terminal endings",
                    "Axon terminal -> Axon -> Cell body -> Dendritic tip",
                    "Cell body -> Synapse -> Dendrite -> Myelin sheath",
                    "Nucleus -> Neuromuscular junction -> Axon -> Cell body"
                ],
                "answer": 0,
                "hint": "Signals are received at the branched dendritic tips and conducted down the axon.",
                "explanation": "Electrical signals move unidirectionally from the dendritic tip to the cell body, then propagate along the axon to its terminals.",
                "solution_steps": [
                    "Step 1: Note that dendrites acquire sensory stimuli or neurotransmitters from adjacent neurons.",
                    "Step 2: Follow the graded potential across the soma (cell body) where action potentials are generated at the axon hillock.",
                    "Step 3: Conclude that the wave of depolarization propagates down the axon to the terminal arborization."
                ]
            },
            {
                "question": "What is the specialized junction between the terminal endings of a motor neuron and a skeletal muscle fiber termed?",
                "options": [
                    "Neuromuscular junction (NMJ)",
                    "Bowman capsule",
                    "Alveolar capillary plexus",
                    "Pulvinus hinge"
                ],
                "answer": 0,
                "hint": "The synapse specifically connecting a nerve to a muscle.",
                "explanation": "The neuromuscular junction is the chemical synapse where a motor neuron transmits acetylcholine signals to a muscle fiber.",
                "solution_steps": [
                    "Step 1: Recall Figure 6.1b showing axon terminals terminating on skeletal muscle fibers.",
                    "Step 2: Identify this specialized synaptic interface as the neuromuscular junction.",
                    "Step 3: Recognize that acetylcholine release here depolarizes the sarcolemma to initiate muscular contraction."
                ]
            },
            {
                "question": "Which of the following is an involuntary reflex response rather than a conscious voluntary action?",
                "options": [
                    "Instantaneous withdrawal of the hand upon touching an unexpected hot iron",
                    "Writing answers deliberately in a biology examination booklet",
                    "Pedaling a bicycle down a steep hill while avoiding obstacles",
                    "Raising your hand in a classroom to ask a teacher a question"
                ],
                "answer": 0,
                "hint": "Look for the automatic emergency response executed without prior conscious deliberation.",
                "explanation": "Hand withdrawal from a hot object is an instantaneous, involuntary spinal reflex; writing, cycling, and raising hands are voluntary.",
                "solution_steps": [
                    "Step 1: Define a reflex action as an immediate, involuntary motor response to a sensory stimulus.",
                    "Step 2: Recognize that touching a hot iron triggers hand withdrawal before conscious perception occurs in the cerebrum.",
                    "Step 3: Contrast this with writing, cycling, and asking questions, which require conscious cerebral intention."
                ]
            },
            {
                "question": "Why do electrical impulses need chemical neurotransmitters to transmit signals between adjacent neurons?",
                "options": [
                    "Adjacent neurons do not touch physically; a microscopic fluid-filled synaptic cleft separates them",
                    "Electrical currents would permanently burn and fuse the myelin sheaths of adjacent cells",
                    "Chemical neurotransmitters contain glucose required for mitochondrial cellular respiration",
                    "Electric charges can only flow through solid crystalline bone structures like the cranium"
                ],
                "answer": 0,
                "hint": "There is a physical structural gap (synapse) between neurons that electrical sparks cannot jump.",
                "explanation": "The physical gap of the synapse prevents direct electrical current flow, requiring chemical diffusion to bridge the gap.",
                "solution_steps": [
                    "Step 1: Understand that individual neurons are discrete cellular units separated by synaptic clefts (~20 nm).",
                    "Step 2: Note that action potentials cannot physically jump across this non-conducting extracellular fluid gap.",
                    "Step 3: Conclude that neurotransmitter release converts electrical signals into chemical signals that cross the gap."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Brain Muscle Review",
        "subtitle": "Human Encephalon Regions, CSF Protection & Muscle Filaments",
        "speech": "",
        "questions": [
            {
                "question": "What is the primary function of the cerebrum within the human Central Nervous System?",
                "options": [
                    "It serves as the main thinking center, integrating sensory inputs, stored memory, and voluntary motor acts",
                    "It controls involuntary vital reflexes like blood pressure, cardiac rhythm, and vomiting",
                    "It coordinates opposing muscle groups to maintain physical balance and posture",
                    "It secretes thyroxin hormone directly into the cervical lymphatic capillaries"
                ],
                "answer": 0,
                "hint": "The largest cerebral part of the fore-brain responsible for consciousness, cognition, and voluntary decisions.",
                "explanation": "The cerebrum is the fore-brain's primary center for conscious thought, intelligence, memory, sensory processing, and voluntary action.",
                "solution_steps": [
                    "Step 1: Identify the cerebrum as the major constituent of the fore-brain.",
                    "Step 2: Note that it contains sensory areas (vision, hearing, smell), association areas (memory/logic), and motor areas.",
                    "Step 3: Conclude that conscious perception, deliberate voluntary movements, and intellectual cognition reside in the cerebrum."
                ]
            },
            {
                "question": "Which specific area of the human brain regulates the sensation of feeling full (the hunger satiety center)?",
                "options": [
                    "A specialized separate center in the fore-brain",
                    "The cerebellar peduncles in the hind-brain",
                    "The cartilaginous rings of the larynx",
                    "The adrenal medulla above the kidneys"
                ],
                "answer": 0,
                "hint": "NCERT identifies this appetite satiety center as part of the fore-brain.",
                "explanation": "The fore-brain contains a dedicated center that monitors blood nutrient levels and signals satiety when full.",
                "solution_steps": [
                    "Step 1: Recall the functional divisions of the human fore-brain described in Section 6.1.2.",
                    "Step 2: Identify that appetite regulation and the sensation of fullness are governed by the fore-brain (hypothalamus).",
                    "Step 3: Confirm that the hunger center is an integral component of the fore-brain."
                ]
            },
            {
                "question": "What distinct role does the cerebellum play in voluntary motor actions like riding a bicycle or walking straight?",
                "options": [
                    "It coordinates muscle precision, body equilibrium, and physical balance, though it does not initiate the action",
                    "It decides consciously when to begin riding the bicycle and chooses the navigation route",
                    "It secretes adrenaline into skeletal muscles to increase anaerobic glycolysis",
                    "It detects gustatory taste modalities through the cranial olfactory nerves"
                ],
                "answer": 0,
                "hint": "The cerebrum decides to walk; the cerebellum ensures you do not stumble or fall.",
                "explanation": "The cerebellum coordinates voluntary motor activities, ensuring smooth muscular precision, balance, and posture.",
                "solution_steps": [
                    "Step 1: Differentiate between motor initiation (cerebrum) and motor coordination (cerebellum).",
                    "Step 2: Note that riding a bicycle requires continuous micro-adjustments of balance and posture.",
                    "Step 3: Conclude that the cerebellum fine-tunes muscular timing, maintaining equilibrium and preventing stumbling."
                ]
            },
            {
                "question": "Which parts of the human Central Nervous System are responsible for controlling involuntary actions like blood pressure, salivation, and vomiting?",
                "options": [
                    "The medulla oblongata and mid-brain",
                    "The cerebrum and olfactory lobes",
                    "The peripheral spinal nerves alone",
                    "The bony cranium and vertebral column"
                ],
                "answer": 0,
                "hint": "Visceral autonomic functions are governed by the brainstem (medulla and mid-brain).",
                "explanation": "Involuntary autonomic processes like blood pressure, peristalsis, salivation, and vomiting are governed by the medulla and mid-brain.",
                "solution_steps": [
                    "Step 1: Identify that involuntary actions occur without conscious cerebral intervention.",
                    "Step 2: Recall that the brainstem—specifically the medulla in the hind-brain and parts of the mid-brain—manages visceral reflexes.",
                    "Step 3: Conclude that blood pressure, salivation, and vomiting reflexes are controlled by the medulla and mid-brain."
                ]
            },
            {
                "question": "How is the delicate human brain protected against mechanical shocks, violent concussions, and sudden physical trauma?",
                "options": [
                    "It is encased in a bony skull (cranium) and cushioned inside a fluid-filled balloon of cerebrospinal fluid (CSF)",
                    "It is surrounded by a thick waxy cuticle layer and interlocking cartilaginous rings",
                    "It floats freely in a bath of concentrated gastric hydrochloric acid",
                    "It is embedded directly within the contractile actin-myosin proteins of the neck"
                ],
                "answer": 0,
                "hint": "A hard bony container outside and a liquid shock absorber inside.",
                "explanation": "The brain is protected by the bony cranium and cushioned against mechanical shocks by shock-absorbing cerebrospinal fluid.",
                "solution_steps": [
                    "Step 1: Identify the hard outer armor: the bony cranium (skull).",
                    "Step 2: Identify the inner hydraulic cushion: cerebrospinal fluid (CSF) filling the subarachnoid space and ventricles.",
                    "Step 3: Conclude that CSF acts as a hydraulic shock-absorbing balloon, dampening sudden mechanical impacts."
                ]
            },
            {
                "question": "What anatomical structure protects the spinal cord from compression, crushing, and physical trauma?",
                "options": [
                    "The bony vertebral column (backbone)",
                    "The pleural membrane of the lungs",
                    "The peritoneal lining of the abdomen",
                    "The rings of cartilage around the oesophagus"
                ],
                "answer": 0,
                "hint": "The segmented bumpy bony column running down the middle of the back.",
                "explanation": "The spinal cord is housed within the neural canal of the bony vertebral column (backbone).",
                "solution_steps": [
                    "Step 1: Recall that the spinal cord is a delicate cylinder of nervous tissue extending down the back.",
                    "Step 2: Identify that it is enclosed inside the spinal canal formed by interlocking vertebrae.",
                    "Step 3: Conclude that the vertebral column (backbone) provides flexible, sturdy bony protection."
                ]
            },
            {
                "question": "What biochemical mechanism allows a muscle cell to change shape and execute movement upon receiving a nerve impulse?",
                "options": [
                    "Specialized contractile proteins change shape and spatial arrangement, causing the cell to shorten",
                    "Cellular water evaporates completely through microscopic stomatal pores",
                    "Mitochondria convert into rigid calcium carbonate bone crystals",
                    "The cell membrane dissolves completely into surrounding interstitial lymph"
                ],
                "answer": 0,
                "hint": "Actin and myosin protein filaments slide past each other in response to calcium and ATP.",
                "explanation": "Arriving nerve impulses trigger contractile proteins (actin and myosin) to alter conformation and slide, shortening the muscle cell.",
                "solution_steps": [
                    "Step 1: Note that muscle cells contain specialized contractile proteins: actin and myosin.",
                    "Step 2: Understand that electrical depolarization at the neuromuscular junction releases intracellular calcium ions.",
                    "Step 3: Conclude that protein filaments change their molecular arrangement and slide, physically shortening the cell to exert force."
                ]
            },
            {
                "question": "How do cranial nerves differ from spinal nerves in the human Peripheral Nervous System?",
                "options": [
                    "Cranial nerves arise directly from the brain; spinal nerves originate from the spinal cord",
                    "Cranial nerves only operate in plants; spinal nerves only operate in aquatic fishes",
                    "Cranial nerves carry only blood; spinal nerves carry digestive enzymes",
                    "Cranial nerves are surrounded by bone; spinal nerves lack all protective tissue"
                ],
                "answer": 0,
                "hint": "Consider their anatomical points of origin within the Central Nervous System.",
                "explanation": "Cranial nerves (12 pairs) arise from the brain; spinal nerves (31 pairs) originate from the spinal cord.",
                "solution_steps": [
                    "Step 1: Define the Peripheral Nervous System as nerves connecting the CNS to body parts.",
                    "Step 2: Identify that cranial nerves originate directly from the brainstem and innervate the head and viscera.",
                    "Step 3: Identify that spinal nerves branch segmental from the spinal cord to innervate the trunk and limbs."
                ]
            },
            {
                "question": "What is the primary difference between a reflex action (like hand withdrawal) and a voluntary motor action (like walking)?",
                "options": [
                    "Reflex actions are involuntary spinal responses bypassing conscious thought; walking is a deliberate cerebral decision",
                    "Reflex actions require twenty minutes of cognitive processing; walking happens without any nerve cells",
                    "Reflex actions are executed by smooth visceral muscles; walking is executed by cardiac muscle",
                    "Reflex actions do not involve sensory receptors; walking is controlled exclusively by the cerebellum"
                ],
                "answer": 0,
                "hint": "Conscious cerebral initiation versus automatic spinal emergency circuitry.",
                "explanation": "Reflex actions are rapid, involuntary, and mediated by spinal circuits; walking is a conscious voluntary movement directed by the cerebrum.",
                "solution_steps": [
                    "Step 1: Note that walking involves conscious intention generated in the cerebral cortex motor strip.",
                    "Step 2: Note that hand withdrawal is an involuntary, stereotyped response coordinated by spinal relay circuits.",
                    "Step 3: Conclude that reflex actions prioritize speed over cognitive deliberation to prevent immediate physical trauma."
                ]
            },
            {
                "question": "How do you detect the pleasant scent of an incense stick burning in a distant corner of a room?",
                "options": [
                    "Olfactory receptors in the nose detect airborne molecules, sending impulses to the olfactory area of the fore-brain",
                    "Gustatory receptors on the tongue detect airborne dust and stimulate salivary amylase secretion",
                    "The cerebellum computes the acoustic sound waves created by the glowing incense ember",
                    "Spinal reflex arcs directly contract the diaphragm to absorb the smoke through skin capillaries"
                ],
                "answer": 0,
                "hint": "Volatile odorants stimulate olfactory receptors that signal the fore-brain's smell center.",
                "explanation": "Volatile molecules bind to olfactory receptors in the nasal cavity, generating impulses sent to the fore-brain's olfactory cortex.",
                "solution_steps": [
                    "Step 1: Recognize that burning incense releases volatile organic molecules into ambient air.",
                    "Step 2: Note that inhaled molecules dissolve in nasal mucus and bind to specialized olfactory sensory receptors.",
                    "Step 3: Follow the electrical impulses along the olfactory tract into the fore-brain where conscious smell perception occurs."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Plant Hormones Review",
        "subtitle": "Tropisms, Auxin Curvature & Phytohormone Roles",
        "speech": "",
        "questions": [
            {
                "question": "What is the fundamental difference between the movement of leaves in a sensitive plant and the phototropic movement of a seedling shoot?",
                "options": [
                    "Sensitive plant leaf movement is non-directional and independent of growth; phototropism is directional growth curvature",
                    "Sensitive plant leaf movement takes three weeks; phototropism happens within fractions of a millisecond",
                    "Sensitive plant leaves use animal-like muscular nerves; phototropic shoots have no chemical signals",
                    "Sensitive plant leaves grow exclusively toward gravity; phototropic shoots bend away from all light"
                ],
                "answer": 0,
                "hint": "Immediate hydraulic nastic folding versus slow directional growth tropism.",
                "explanation": "Sensitive plant movement is a fast, non-directional nastic response caused by turgor shifts; phototropism is slow directional growth.",
                "solution_steps": [
                    "Step 1: Identify that Mimosa pudica leaf drooping is an immediate, reversible turgor-driven nastic movement independent of growth.",
                    "Step 2: Identify that phototropism involves irreversible differential cellular elongation guided directionally by light.",
                    "Step 3: Conclude that the former is growth-independent and non-directional, while the latter is growth-dependent and directional."
                ]
            },
            {
                "question": "How does the plant hormone auxin cause a growing shoot tip to bend towards a unilateral light source?",
                "options": [
                    "Auxin diffuses to the shaded flank, stimulating those cells to elongate faster than cells on the illuminated flank",
                    "Auxin destroys the cell walls on the illuminated side, causing the stem to collapse toward the window",
                    "Auxin converts all chloroplasts on the shaded flank into heavy starch crystals that pull the shoot down",
                    "Auxin attracts insect pollinators that mechanically pull the stem tip towards the daylight source"
                ],
                "answer": 0,
                "hint": "Auxin stimulates cell elongation and accumulates on the darker side of the stem.",
                "explanation": "Auxin moves away from light to the shaded side, where higher concentrations cause greater cell elongation, bending the stem toward light.",
                "solution_steps": [
                    "Step 1: Understand that auxin is synthesized at the shoot apex.",
                    "Step 2: Observe that unilateral illumination induces lateral transport of auxin toward the shaded flank.",
                    "Step 3: Conclude that higher auxin on the shaded flank promotes greater cell elongation, curving the stem tip toward the light."
                ]
            },
            {
                "question": "Which of the following plant hormones is specifically responsible for promoting rapid cellular division in developing fruits and seeds?",
                "options": [
                    "Cytokinin",
                    "Abscisic acid (ABA)",
                    "Adrenaline",
                    "Thyroxin"
                ],
                "answer": 0,
                "hint": "The hormone name shares the root of 'cytokinesis', meaning cell division.",
                "explanation": "Cytokinins stimulate cell division and are concentrated in rapidly growing plant organs such as developing seeds and young fruits.",
                "solution_steps": [
                    "Step 1: Match phytohormones with their primary physiological roles.",
                    "Step 2: Note that cytokinins are potent stimulators of mitotic cell division (cytokinesis).",
                    "Step 3: Confirm that developing seeds and fruits have the highest endogenous cytokinin concentrations to support growth."
                ]
            },
            {
                "question": "What is the primary physiological function of abscisic acid (ABA) in plant growth and stress adaptation?",
                "options": [
                    "It acts as a growth inhibitor, causing leaf wilting, stomatal closure, and seed dormancy during stress",
                    "It stimulates the rapid germination of seeds and excessive stem elongation in darkness",
                    "It secretes sweet floral nectar to attract flying pollinators during bright sunlight",
                    "It breaks down starch into glucose inside developing root nodule bacteroids"
                ],
                "answer": 0,
                "hint": "ABA inhibits growth and induces dormancy to protect plants against desiccation.",
                "explanation": "Abscisic acid is a plant growth inhibitor that induces stomatal closure during water stress, leaf senescence, and dormancy.",
                "solution_steps": [
                    "Step 1: Contrast growth promoters (auxins, gibberellins, cytokinins) with growth inhibitors.",
                    "Step 2: Identify abscisic acid (ABA) as the primary phytohormone mediating growth inhibition and stress signaling.",
                    "Step 3: Recognize that ABA triggers stomatal closure during drought, induces seed dormancy, and causes leaf wilting and drop."
                ]
            },
            {
                "question": "What experimental observation proves positive geotropism in roots and negative geotropism in plant shoots (Figure 6.6)?",
                "options": [
                    "When a potted plant is placed horizontally, roots bend downward into the soil while shoots bend upward toward the air",
                    "When a plant is placed in the dark, both roots and shoots dissolve completely into water vapor",
                    "Roots always bend toward loud acoustic sounds while shoots coil around plastic support stakes",
                    "Shoots absorb soil minerals through their cuticle while roots release oxygen through stomata"
                ],
                "answer": 0,
                "hint": "Consider the directional growth of roots (downward) versus shoots (upward) in a horizontal pot.",
                "explanation": "In a horizontal seedling, roots grow downward with gravity (positive geotropism) while shoots grow upward against gravity (negative geotropism).",
                "solution_steps": [
                    "Step 1: Define geotropism as directional growth in response to the Earth's gravitational pull.",
                    "Step 2: Place a potted seedling horizontally: observe roots curving downwards toward the center of gravity.",
                    "Step 3: Observe shoots curving upwards away from gravity, demonstrating positive geotropism in roots and negative in shoots."
                ]
            },
            {
                "question": "How do pea plant tendrils exhibit thigmotropism when contacting a wooden trellis or bamboo stake?",
                "options": [
                    "Cells on the side away from the support grow much faster than cells in contact, coiling the tendril tightly around the stake",
                    "Cells in direct contact with the stake divide rapidly while outer cells collapse from lack of water",
                    "The tendril secretes adhesive bile salts that permanently glue the leaf to the wooden support",
                    "Electrical nerve impulses from the root hairs contract specialized pulvinus hinge cells"
                ],
                "answer": 0,
                "hint": "Touch inhibits growth at the contact point while stimulating elongation on the opposite side.",
                "explanation": "Contact with a support slows growth on the inner side, while the outer side elongates rapidly, causing the tendril to spiral around the support.",
                "solution_steps": [
                    "Step 1: Define thigmotropism as directional growth response to physical mechanical contact.",
                    "Step 2: Note that contact with a support alters auxin distribution, slowing cell elongation on the contact flank.",
                    "Step 3: Observe that the opposite flank elongates rapidly, generating a mechanical torque that coils the tendril securely."
                ]
            },
            {
                "question": "Why do plants rely extensively on chemical phytohormones rather than an animal-like nervous system for whole-body coordination?",
                "options": [
                    "Plants lack nervous tissue; hormones diffuse widely to coordinate slow, developmental growth responses across all cells",
                    "Electrical impulses cannot travel through plant cell walls under any circumstances",
                    "Plants do not possess living cells and therefore cannot generate action potentials",
                    "Plant roots require digestive enzymes to break down soil minerals prior to absorption"
                ],
                "answer": 0,
                "hint": "Plants are non-motile and coordinate long-term growth and branching rather than rapid locomotion.",
                "explanation": "Plants lack nerves and muscles; chemical phytohormones diffuse to all cells to coordinate growth, tropisms, and stress responses.",
                "solution_steps": [
                    "Step 1: Recognize that plants are sessile organisms whose adaptations are manifested through growth and morphological changes.",
                    "Step 2: Note that electrical impulses have limited reach and require specialized neural infrastructure that plants lack.",
                    "Step 3: Conclude that chemical phytohormones provide an energy-efficient, systemic medium to coordinate developmental growth."
                ]
            },
            {
                "question": "Which plant hormone promotes internodal stem elongation and is used agriculturally to increase sugarcane yield?",
                "options": [
                    "Gibberellin",
                    "Abscisic acid",
                    "Insulin",
                    "Adrenaline"
                ],
                "answer": 0,
                "hint": "Promotes stem elongation and longitudinal growth along with auxins.",
                "explanation": "Gibberellins stimulate stem elongation and cell expansion, increasing stem length in plants like sugarcane.",
                "solution_steps": [
                    "Step 1: Recall the function of gibberellins as described in Section 6.2.2.",
                    "Step 2: Identify that gibberellins specifically promote internode elongation and stem height.",
                    "Step 3: Confirm that gibberellins are the growth-promoting phytohormones responsible for stem elongation."
                ]
            },
            {
                "question": "What is hydrotropism and how can it be demonstrated in a laboratory experiment?",
                "options": [
                    "Directional growth of roots towards moisture; demonstrated by roots bending toward a porous water pot in dry soil",
                    "Directional growth of shoots toward humid clouds during thunderstorm lightning",
                    "Rapid folding of leaflets when submerged under hot water baths",
                    "The ascent of sap through xylem tracheids driven by daytime transpiration pull"
                ],
                "answer": 0,
                "hint": "Roots bend toward moisture, even growing horizontally or against gravity if water is nearby.",
                "explanation": "Hydrotropism is directional root growth toward moisture, overriding gravity when water is unevenly distributed in soil.",
                "solution_steps": [
                    "Step 1: Define hydrotropism as directional growth in response to a water potential gradient.",
                    "Step 2: Set up a porous clay pot with water in dry soil with germinating seeds nearby.",
                    "Step 3: Observe the seedling roots curving laterally toward the moist pot, proving positive hydrotropism."
                ]
            },
            {
                "question": "What two major biological limitations restrict electrical communication in living plant and animal systems?",
                "options": [
                    "Impulses only reach cells connected by specialized tissue, and cells require recovery time to reset before the next impulse",
                    "Electrical impulses consume all cellular carbohydrates within two seconds, causing immediate necrosis",
                    "Electrical impulses permanently destroy all ribosomes inside nuclear membranes",
                    "Impulses only travel when atmospheric humidity exceeds ninety-five percent"
                ],
                "answer": 0,
                "hint": "Limited physical connectivity and the physiological refractory recovery period.",
                "explanation": "Electrical signals reach only innervated cells and require a refractory resetting period; chemical hormones overcome both.",
                "solution_steps": [
                    "Step 1: Identify that electrical impulses require physical anatomical connections (neurons or plasmodesmata).",
                    "Step 2: Note that cells undergo membrane depolarization and must expend metabolic energy to reset ionic gradients (refractory phase).",
                    "Step 3: Conclude that these two limitations necessitate chemical hormonal communication for widespread, continuous coordination."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Endocrine Feedback Review",
        "subtitle": "Human Endocrine Glands, Diabetes & Hormone Control",
        "speech": "",
        "questions": [
            {
                "question": "Which endocrine gland is located at the base of the brain and secretes Growth Hormone under hypothalamic regulation?",
                "options": [
                    "The pituitary gland",
                    "The thyroid gland",
                    "The pancreas",
                    "The adrenal gland"
                ],
                "answer": 0,
                "hint": "Often called the master endocrine gland, resting in the sella turcica of the sphenoid bone.",
                "explanation": "The pituitary gland, located at the base of the brain, secretes Growth Hormone and is regulated by hypothalamic releasing factors.",
                "solution_steps": [
                    "Step 1: Identify the endocrine gland situated at the base of the brain.",
                    "Step 2: Note that the hypothalamus secretes releasing hormones (like GHRF) into the hypophyseal portal system.",
                    "Step 3: Confirm that the pituitary gland secretes Growth Hormone to regulate overall somatic growth."
                ]
            },
            {
                "question": "What medical condition is caused by a dietary deficiency of iodine, and what is its visible physical manifestation?",
                "options": [
                    "Goitre, characterized by an abnormally enlarged, swollen thyroid gland in the neck",
                    "Dwarfism, characterized by severely stunted limb bones during infancy",
                    "Gigantism, characterized by excessive bone elongation exceeding eight feet",
                    "Diabetes mellitus, characterized by excessive glucose in circulating blood"
                ],
                "answer": 0,
                "hint": "Iodine is needed to make thyroxin; lack of it causes a swollen neck.",
                "explanation": "Iodine deficiency prevents thyroxin synthesis; the thyroid gland hypertrophies in compensation, causing goitre (swollen neck).",
                "solution_steps": [
                    "Step 1: Recall that the thyroid gland requires dietary iodine to synthesize thyroxin.",
                    "Step 2: Note that when iodine is deficient, pituitary TSH overstimulates the thyroid gland to grow larger.",
                    "Step 3: Conclude that this enlargement results in goitre, presenting as a conspicuous swelling in the neck."
                ]
            },
            {
                "question": "How does the hormone insulin, secreted by the endocrine pancreas, regulate blood glucose levels in humans?",
                "options": [
                    "It stimulates body cells to take up glucose and directs the liver to convert excess glucose into stored glycogen",
                    "It converts dietary proteins into concentrated hydrochloric acid inside the gastric lumen",
                    "It breaks down red blood cells to release extra haemoglobin into pulmonary alveoli",
                    "It increases blood pressure by constricting arterioles supplying the skeletal muscles"
                ],
                "answer": 0,
                "hint": "Insulin lowers elevated blood sugar by promoting cellular uptake and glycogen storage.",
                "explanation": "Insulin promotes glucose uptake by cells and stimulates glycogen synthesis in the liver and muscles, lowering blood sugar.",
                "solution_steps": [
                    "Step 1: Identify that beta cells in the pancreatic islets of Langerhans secrete insulin in response to hyperglycemia.",
                    "Step 2: Understand that insulin facilitates cellular glucose transport and activates glycogenesis in hepatocytes.",
                    "Step 3: Conclude that this biological action removes glucose from the bloodstream, returning blood sugar to normal homeostatic levels."
                ]
            },
            {
                "question": "What is the biological mechanism of closed-loop negative feedback regulating insulin secretion by the pancreas?",
                "options": [
                    "High blood sugar triggers insulin release; as sugar levels fall back to normal, insulin secretion automatically slows down",
                    "Insulin secretion increases exponentially throughout the day without ever shutting off",
                    "Blood glucose is converted into adrenaline whenever pancreatic beta cells detect high insulin",
                    "Cerebrospinal fluid destroys pancreatic cells when blood sugar drops below baseline"
                ],
                "answer": 0,
                "hint": "The response (lowered blood sugar) eliminates the stimulus, shutting off further hormone release.",
                "explanation": "High blood glucose stimulates insulin release; once glucose levels fall, the stimulus ceases, turning off insulin secretion.",
                "solution_steps": [
                    "Step 1: Note that pancreatic endocrine cells directly sense blood glucose concentration.",
                    "Step 2: When glucose rises after eating, insulin is secreted to lower it.",
                    "Step 3: As blood glucose returns to normal, the triggering stimulus disappears, naturally reducing insulin secretion."
                ]
            },
            {
                "question": "Which of the following hormones is matched correctly with its endocrine gland and primary biological function?",
                "options": [
                    "Adrenaline -> Adrenal glands -> Prepares body for fight-or-flight emergencies by increasing heart and breathing rates",
                    "Insulin -> Thyroid gland -> Regulates carbohydrate metabolism to prevent neck goitre",
                    "Thyroxin -> Pancreas -> Lowers blood glucose levels following a carbohydrate meal",
                    "Testosterone -> Pituitary gland -> Stimulates leaf wilting and stomatal pore closure"
                ],
                "answer": 0,
                "hint": "Adrenal glands sit above kidneys and secrete adrenaline for emergency fight-or-flight.",
                "explanation": "Adrenal glands secrete adrenaline, which accelerates heart and breathing rates to prepare the body for emergency action.",
                "solution_steps": [
                    "Step 1: Check hormone-gland-function pairs against Table 6.1 in the NCERT text.",
                    "Step 2: Notice that insulin is from the pancreas (not thyroid), thyroxin is from the thyroid (not pancreas), and testosterone is from testes.",
                    "Step 3: Confirm that adrenaline is correctly matched to adrenal glands and the fight-or-flight emergency response."
                ]
            },
            {
                "question": "What puberty changes are triggered in adolescent human females by the secretion of oestrogen from the ovaries?",
                "options": [
                    "Development of breast tissue, feminine subcutaneous fat distribution, and onset of the menstrual cycle",
                    "Deepening of the vocal pitch due to massive enlargement of the thyroid cartilage",
                    "Rapid growth of facial beard hair and broad muscular shoulder expansion",
                    "Complete cessation of all cellular respiration inside liver mitochondria"
                ],
                "answer": 0,
                "hint": "Oestrogen directs female secondary sexual characteristics and reproductive cyclicity.",
                "explanation": "Oestrogen drives female puberty changes: mammary gland development, feminine fat deposition, and menstrual cycle initiation.",
                "solution_steps": [
                    "Step 1: Identify oestrogen as the primary feminizing steroid hormone produced by ovarian follicles.",
                    "Step 2: Note its targets: breast tissue, hips, reproductive tract, and hypothalamic-pituitary-ovarian axis.",
                    "Step 3: Conclude that oestrogen establishes female secondary sexual characteristics and the 28-day menstrual cycle."
                ]
            },
            {
                "question": "What is the endocrine function of the hypothalamus in regulating the human endocrine system?",
                "options": [
                    "It secretes neurohormonal releasing factors that stimulate or inhibit hormone release from the pituitary gland",
                    "It synthesizes insulin to lower blood sugar levels during intense physical exercise",
                    "It filters blood plasma to produce one hundred eighty liters of initial filtrate daily",
                    "It secretes bile salts directly into the duodenum to emulsify large lipid droplets"
                ],
                "answer": 0,
                "hint": "The hypothalamus connects the nervous system to the endocrine system via the pituitary gland.",
                "explanation": "The hypothalamus secretes releasing hormones (e.g., GHRH, TRH) that control anterior pituitary hormone secretion.",
                "solution_steps": [
                    "Step 1: Locate the hypothalamus in the basal fore-brain, acting as the neuroendocrine bridge.",
                    "Step 2: Note that it secretes peptide releasing factors (e.g., Growth Hormone Releasing Factor).",
                    "Step 3: Conclude that these factors direct the pituitary gland to release or withhold specific tropic hormones."
                ]
            },
            {
                "question": "Why is the emergency hormone adrenaline called the 'fight-or-flight' hormone?",
                "options": [
                    "It rapidly mobilizes energy, diverting oxygen and glucose to skeletal muscles so the animal can fight or flee",
                    "It causes the animal to fall into deep hibernation during sudden predator encounters",
                    "It permanently converts red blood cells into white blood cells to resist bacterial infections",
                    "It freezes all muscular contraction so the animal appears completely dead to predators"
                ],
                "answer": 0,
                "hint": "It primes the entire body for intense physical exertion: running or battling.",
                "explanation": "Adrenaline increases heart rate, dilates bronchioles, and diverts blood to skeletal muscles to power fighting or rapid flight.",
                "solution_steps": [
                    "Step 1: Recognize that survival threats demand immediate, maximum physical exertion.",
                    "Step 2: Note that adrenaline coordinates cardiovascular acceleration, blood diversion to muscles, and glycogen breakdown.",
                    "Step 3: Conclude that these synergistic changes prepare the animal to either confront the threat (fight) or escape (flight)."
                ]
            },
            {
                "question": "What happens in a human body when the pancreas secretes an insufficient quantity of insulin?",
                "options": [
                    "Blood glucose levels rise abnormally high, resulting in the chronic disorder diabetes mellitus",
                    "The thyroid gland in the neck swells into a conspicuous goitre tumor",
                    "The skeleton experiences abnormal gigantism exceeding nine feet in height",
                    "Body temperature drops to zero because cellular respiration stops completely"
                ],
                "answer": 0,
                "hint": "Without insulin, glucose cannot enter cells and accumulates in circulating blood.",
                "explanation": "Insulin deficiency impairs cellular glucose uptake, causing high blood sugar (hyperglycemia) and diabetes mellitus.",
                "solution_steps": [
                    "Step 1: Recall that insulin is required for cellular glucose uptake and storage.",
                    "Step 2: Understand that insulin insufficiency causes glucose to accumulate in blood plasma rather than entering cells.",
                    "Step 3: Conclude that this chronic hyperglycemia defines diabetes mellitus, requiring dietary control and insulin therapy."
                ]
            },
            {
                "question": "How does the mechanism of chemical hormonal coordination differ fundamentally from electrical nervous communication?",
                "options": [
                    "Hormones travel via blood to reach all target cells with sustained effects; nervous signals are rapid, targeted, and brief",
                    "Hormones travel only along the myelin sheaths of sensory neurons; nervous signals diffuse across leaf stomata",
                    "Hormones act within one millisecond and disappear; nervous signals take three weeks to cross a single synapse",
                    "Hormones operate exclusively in plants; the nervous system operates in both plants and animals"
                ],
                "answer": 0,
                "hint": "Circulatory systemic distribution and duration versus hardwired localized speed.",
                "explanation": "Hormones travel via the bloodstream, producing widespread and sustained effects; nervous signals are rapid, point-to-point, and brief.",
                "solution_steps": [
                    "Step 1: Compare transmission medium: blood circulation (endocrine) versus axons/synapses (nervous).",
                    "Step 2: Compare speed and duration: electrical impulses are millisecond-fast and brief; hormones take minutes/hours and persist.",
                    "Step 3: Compare target scope: nervous is point-to-point (innervated cells); endocrine reaches all cells expressing the receptor."
                ]
            }
        ]
    }
]

with open('.agents/c10s_ch6_part3.json', 'w', encoding='utf-8') as f:
    json.dump(slides_part3, f, indent=2)

print("Slide part 3 (Slides 17-20) successfully written!")
for s in slides_part3:
    print(f"Slide {s['id']}: '{s['title']}' - {len(s['questions'])} questions, speech length: {len(s['speech'])}")
    assert s['speech'] == "", f"Slide {s['id']} must be silent!"
    assert len(s['questions']) == 10, f"Slide {s['id']} must have 10 challenge questions!"
    for q in s['questions']:
        assert len(q['options']) == 4
        assert 'hint' in q
        assert 'explanation' in q
        assert len(q['solution_steps']) == 3

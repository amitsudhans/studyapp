#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for NCERT Class 10 Science Chapter 6: Control and Coordination.
Strict requirements:
- Titles: 1-3 words
- Speech: strictly 195-215 words per slide
- Zero persona titles (Dr, Sir, Madam, Mr, Mrs, Prof) and zero fictional character names
- 2 checkpoints per slide with 4 options, hint, and detailed explanation
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Movement Environmental Response",
        "subtitle": "Growth-Linked vs Non-Growth Biological Actions",
        "speech": (
            "Welcome students to our laboratory exploration of biological control and coordination. When we observe the living world around us, "
            "movement is one of the most obvious signs of life. However, living movements fall into two fundamentally distinct biological categories: "
            "growth-related movements and non-growth movements. Consider a germinating seed pushing soil particles aside as its tender hypocotyl emerges; this is "
            "a directional growth movement, and if growth were stopped, the movement would cease entirely. In contrast, consider a running cat, "
            "children playfully swinging, or cows peacefully chewing their cud. These rapid physical actions are completely independent of growth. Why do "
            "organisms perform these energetic movements? Biological movements are precise responses to changes occurring in the surrounding environment. A cat runs "
            "vigorously because it detects a mouse; cows chew cud systematically to break down tough fibrous grass for efficient internal digestion; "
            "and we quickly whisper when talking in class rather than shouting loudly. An organism's response must be carefully controlled, recognizing "
            "environmental cues and executing appropriate motor responses. In complex multicellular organisms, specialized nervous and muscular tissues work together, coordinating "
            "incoming environmental stimuli with precise physical actions to secure ecological advantages, avoid physical trauma, and maintain internal biological survival."
        ),
        "checkpoints": [
            {
                "question": "Which of the following is an example of a biological movement completely independent of growth?",
                "options": [
                    "A cat sprinting rapidly to capture prey in an open field",
                    "A pea seedling pushing soil particles aside during germination",
                    "A pollen tube growing chemotropically through the style towards an ovule",
                    "A sunflower seedling bending phototropically toward morning sunlight"
                ],
                "answer": 0,
                "hint": "Identify the rapid physical locomotion that does not involve cellular growth or tissue enlargement.",
                "explanation": "A running cat executes rapid muscular movement independent of developmental growth, unlike plant seedling germination."
            },
            {
                "question": "Why must movements in multicellular organisms be controlled and coordinated rather than random?",
                "options": [
                    "To match specific environmental triggers with appropriate and advantageous motor responses",
                    "To prevent all internal chemical reactions from consuming cellular glucose",
                    "Because uncontrolled random movements convert soft tissues directly into bone minerals",
                    "To eliminate the need for specialized sensory receptors in sense organs"
                ],
                "answer": 0,
                "hint": "Coordinated responses ensure protective or beneficial actions suited to the situation.",
                "explanation": "Controlled coordination ensures that an organism responds correctly to environmental cues for protection, nutrition, or survival."
            }
        ]
    },
    {
        "id": 2,
        "title": "Neuron Synaptic Transmission",
        "subtitle": "Dendritic Receptors, Axonal Impulses & Synapses",
        "speech": (
            "Let us examine the structural and functional unit of the animal nervous system, the neuron. Environmental information is detected by "
            "specialized tips of nerve cells located within our sense organs, known as sensory receptors. For instance, gustatory receptors located on "
            "the tongue detect taste, while olfactory receptors located in nasal passages detect smell. In Activity 6.1, blocking the nose while "
            "tasting sugar impairs our ability to appreciate complex food flavors, demonstrating that normal taste perception combines both gustatory and olfactory "
            "inputs. Structurally, a neuron consists of three main components: dendritic tips, a cell body, and an elongated axon. Information "
            "is initially acquired at the dendritic tip, where environmental chemicals trigger a localized reaction that initiates an electrical impulse. This "
            "electrical impulse travels rapidly across the cell body and along the axon to its terminal endings. Because individual neurons are "
            "not physically fused together, a microscopic gap called a synapse separates the axon terminal of one neuron from the dendrite "
            "of the next. When the electrical signal reaches the axonal end, it causes the release of specialized chemical neurotransmitters across "
            "the synapse. These chemicals cross the synaptic cleft, starting an identical electrical impulse in the adjacent neuron or stimulating muscle fibers."
        ),
        "checkpoints": [
            {
                "question": "What is the microscopic gap across which chemical neurotransmitters diffuse between adjacent neurons called?",
                "options": [
                    "The synapse",
                    "The myelin sheath",
                    "The neuromuscular junction",
                    "The Bowman capsule"
                ],
                "answer": 0,
                "hint": "It is the tiny functional junction separating an axon tip from the next dendrite.",
                "explanation": "A synapse is the microscopic gap between neurons where electrical impulses are converted into chemical signals for transmission."
            },
            {
                "question": "Which specific sensory receptors detect taste sensations on the human tongue?",
                "options": [
                    "Gustatory receptors",
                    "Olfactory receptors",
                    "Auditory hair cells",
                    "Photoreceptor rod cells"
                ],
                "answer": 0,
                "hint": "Gustation refers to the sense of taste, whereas olfaction refers to smell.",
                "explanation": "Gustatory receptors located in taste buds on the tongue detect chemical taste modalities."
            }
        ]
    },
    {
        "id": 3,
        "title": "Spinal Reflex Arc",
        "subtitle": "Involuntary Emergency Circuits & Sensory-Motor Pathways",
        "speech": (
            "We now explore reflex actions, our body's rapid, involuntary emergency defense mechanisms. Imagine touching a boiling hot pan or stepping "
            "barefoot onto a sharp nail. If your body relied on conscious thinking, sensory nerves would have to transmit information up "
            "the spinal cord to the brain; the brain's complex neural networks would have to process the data, formulate a conscious "
            "decision, and send motor commands back down to the arm muscles. By the time that multi-step processing completed, severe tissue "
            "burns or lacerations would have already occurred. To prevent catastrophic injury, animals evolved reflex arcs, which connect sensory input nerves "
            "directly to motor output nerves in the spinal cord. In a typical spinal reflex arc, thermal heat is detected by "
            "pain and temperature receptors in the skin. A sensory neuron immediately conducts the electrical signal into the spinal cord, where "
            "it synapses with an intermediate relay neuron. The relay neuron instantly transmits the impulse directly to a motor neuron, which "
            "signals effector biceps muscles to contract powerfully, jerking the hand away in milliseconds. Although information simultaneously travels upward to the "
            "brain, the physical motor response is executed locally and automatically by the spinal cord, ensuring immediate survival without hazardous cognitive delays."
        ),
        "checkpoints": [
            {
                "question": "Where in the human body are the neural circuits for reflex arcs primarily formed?",
                "options": [
                    "In the spinal cord where incoming sensory and outgoing motor nerves meet",
                    "Exclusively within the cerebral cortex association areas",
                    "Inside the fluid-filled cochlea of the inner ear",
                    "Within the glandular medulla of the adrenal glands"
                ],
                "answer": 0,
                "hint": "Emergency reflex arcs form along the nerve highway before signals reach the conscious brain.",
                "explanation": "Reflex arcs form in the spinal cord, allowing immediate motor responses before cognitive brain processing."
            },
            {
                "question": "What is the correct sequence of components in a spinal reflex arc pathway?",
                "options": [
                    "Receptor -> Sensory neuron -> Relay neuron in spinal cord -> Motor neuron -> Effector muscle",
                    "Effector muscle -> Motor neuron -> Spinal cord -> Sensory neuron -> Skin receptor",
                    "Brain cerebrum -> Cranium -> Spinal cord -> Olfactory receptor -> Synapse",
                    "Dendrite -> Axon -> Cerebrospinal fluid -> Gustatory receptor -> Motor neuron"
                ],
                "answer": 0,
                "hint": "Follow the signal from stimulus detection in skin to muscular contraction.",
                "explanation": "The reflex arc moves from receptor to sensory neuron, relay neuron in the spinal cord, motor neuron, and effector muscle."
            }
        ]
    },
    {
        "id": 4,
        "title": "Human Brain Anatomy",
        "subtitle": "Cerebrum, Mid-Brain & Involuntary Hind-Brain Centers",
        "speech": (
            "Let us investigate the command center of our body, the human brain. Together with the spinal cord, the brain forms "
            "the Central Nervous System, which integrates sensory input from all body regions and coordinates responses. Communication between the central system "
            "and peripheral organs is mediated by the Peripheral Nervous System, comprising twelve pairs of cranial nerves arising from the brain "
            "and thirty-one pairs of spinal nerves originating from the spinal cord. Anatomically, the brain is divided into three major structural "
            "regions: the fore-brain, mid-brain, and hind-brain. The fore-brain consists primarily of the massive, highly folded cerebrum, which serves as the "
            "main thinking and cognitive center. The cerebrum contains specialized sensory areas that receive sensory signals for vision, hearing, and smell; "
            "association areas that compare incoming sensations with stored memories to make conscious decisions; and motor areas that command voluntary muscles. "
            "A dedicated hunger center in the fore-brain signals when our stomach is full. Beneath lies the mid-brain, which controls visual "
            "and auditory reflexes such as pupil constriction. The hind-brain consists of the pons, medulla, and cerebellum. The medulla controls vital "
            "involuntary actions including blood pressure, salivation, and vomiting, while the cerebellum maintains body posture, equilibrium, and precision of complex movements."
        ),
        "checkpoints": [
            {
                "question": "Which major part of the human brain functions as the primary center for conscious thinking and stored memory?",
                "options": [
                    "The cerebrum of the fore-brain",
                    "The medulla oblongata of the hind-brain",
                    "The arborization of the spinal cord",
                    "The cartilaginous rings of the trachea"
                ],
                "answer": 0,
                "hint": "The largest, most folded portion of the human brain responsible for cognitive logic.",
                "explanation": "The cerebrum is the fore-brain's main thinking center, integrating sensory inputs with memories to make voluntary decisions."
            },
            {
                "question": "Which region of the hind-brain regulates vital involuntary functions such as blood pressure, salivation, and vomiting?",
                "options": [
                    "The medulla oblongata",
                    "The olfactory lobe of the cerebrum",
                    "The optic chiasm of the mid-brain",
                    "The temporal cranial bone"
                ],
                "answer": 0,
                "hint": "Located at the base of the brainstem, controlling autonomic visceral reflexes.",
                "explanation": "The medulla controls involuntary autonomic activities like blood pressure, cardiac rhythm, salivation, and vomiting."
            }
        ]
    },
    {
        "id": 5,
        "title": "Voluntary Involuntary Coordination",
        "subtitle": "Cerebellar Balance, Motor Precision & Visceral Control",
        "speech": (
            "We now contrast voluntary and involuntary actions within the human body. Voluntary actions are conscious, decision-based movements that you actively "
            "choose to perform, such as writing an examination, speaking aloud, or moving a chair across the room. These deliberate actions "
            "are initiated by the motor areas of the cerebral cortex and executed by skeletal muscles. In stark contrast, involuntary actions "
            "occur automatically without conscious awareness or cognitive effort. You do not consciously instruct your heart to beat, your stomach to "
            "churn food, your salivary glands to secrete saliva, or your pupils to constrict when stepping into bright sunlight. These autonomic "
            "visceral functions are continuously governed by the mid-brain and hind-brain, particularly the medulla. Within the hind-brain, the cerebellum plays a "
            "specialized and indispensable role. While the cerebellum does not initiate voluntary movement, it is responsible for precision, coordination, and muscular "
            "equilibrium. When you walk in a straight line, ride a bicycle on a narrow road, or pick up a fallen "
            "pencil with your fingers, your cerebellum fine-tunes motor commands, coordinating opposing muscle groups to maintain physical balance and steady posture, "
            "preventing stumbling and demonstrating how distinct neural centers harmoniously manage conscious goals alongside automatic homeostatic regulation across the living body."
        ),
        "checkpoints": [
            {
                "question": "Which specific part of the human hind-brain maintains body posture, equilibrium, and the precision of voluntary motor acts?",
                "options": [
                    "The cerebellum",
                    "The cerebrum",
                    "The hypothalamus",
                    "The pituitary gland"
                ],
                "answer": 0,
                "hint": "It coordinates muscle groups to allow walking straight, cycling, and picking up small objects.",
                "explanation": "The cerebellum coordinates voluntary motor activities, ensuring smooth muscular precision, balance, and posture."
            },
            {
                "question": "How does a voluntary action like writing differ fundamentally from an involuntary action like salivation?",
                "options": [
                    "Voluntary actions involve conscious cerebral decisions; involuntary actions are automatic hind-brain responses",
                    "Voluntary actions do not require motor nerves; involuntary actions use skeletal muscles exclusively",
                    "Voluntary actions are controlled by the spinal cord alone; involuntary actions require conscious thought",
                    "Voluntary actions happen instantaneously in reflex arcs without involving muscular proteins"
                ],
                "answer": 0,
                "hint": "Think about conscious awareness and cerebral control versus autonomic regulation.",
                "explanation": "Voluntary actions are conscious decisions directed by the cerebrum, whereas involuntary actions run automatically via the brainstem."
            }
        ]
    },
    {
        "id": 6,
        "title": "Nervous Tissue Protection",
        "subtitle": "Cranial Bony Vault, CSF Cushion & Muscle Proteins",
        "speech": (
            "Because the brain and spinal cord are delicate, critical organs, the human body provides elaborate anatomical armor to protect them "
            "against mechanical trauma. The brain is housed securely within a tough, bony box called the cranium or skull. Inside this "
            "bony vault, the brain floats inside a protective balloon filled with cerebrospinal fluid, which serves as a hydraulic shock absorber, "
            "cushioning the brain against violent sudden impacts, concussions, and pressure variations. Similarly, the spinal cord extends downward within the vertebral "
            "column or backbone, a flexible, bumpy column of interlocking vertebrae that shields spinal nerves from twisting and crushing injuries. Now, "
            "how does nervous tissue translate electrical impulses into physical muscular movement? When a motor nerve impulse arrives at a neuromuscular junction, "
            "neurotransmitters trigger specialized biochemical events inside the muscle fibers. Muscle cells contain specialized contractile proteins, primarily actin and myosin. In "
            "response to the arriving electrical-chemical signal, these protein filaments change both their molecular shape and their spatial arrangement within the "
            "sarcomere. The filaments slide across one another, causing the muscle cell to shorten physically. This synchronized shortening of thousands of "
            "muscle fibers exerts mechanical tension on attached tendons and bones, executing precise physical motion across our skeletal joints during daily activities."
        ),
        "checkpoints": [
            {
                "question": "What two anatomical structures protect the delicate human brain from external mechanical shocks and physical trauma?",
                "options": [
                    "The bony cranium and shock-absorbing cerebrospinal fluid (CSF)",
                    "The vertebral column and salivary glands",
                    "The tracheal cartilaginous rings and alveolar capillaries",
                    "The waxy cuticle layer and stomatal guard cells"
                ],
                "answer": 0,
                "hint": "A hard bone helmet enclosing a fluid-filled shock-absorbing cushion.",
                "explanation": "The brain is protected by the bony skull (cranium) and cushioned by a fluid-filled balloon of cerebrospinal fluid."
            },
            {
                "question": "What happens at the cellular level when a nerve impulse reaches a muscle fiber at a neuromuscular junction?",
                "options": [
                    "Specialized contractile proteins change shape and slide, causing the muscle cell to shorten",
                    "The muscle cell permanently dissolves into cerebrospinal fluid",
                    "Contractile proteins convert into gaseous carbon dioxide to open stomatal pores",
                    "The cell membrane hardens into rigid crystalline bone tissue"
                ],
                "answer": 0,
                "hint": "Contractile actin and myosin filaments alter their arrangement to contract the cell.",
                "explanation": "Arriving nerve impulses cause muscle proteins to change shape and slide, shortening the muscle cell to produce movement."
            }
        ]
    },
    {
        "id": 7,
        "title": "Plant Nastic Movements",
        "subtitle": "Touch-Me-Not Electrical Signals & Pulvinus Turgor",
        "speech": (
            "We now turn our attention to plants, which lack specialized nervous systems and muscular tissues entirely. Despite having no nerves, "
            "plants exhibit sophisticated, highly controlled movements categorized into two broad types: movements independent of growth and movements dependent on growth. "
            "An outstanding example of movement independent of growth is the immediate response to touch shown by Mimosa pudica, commonly known "
            "as the touch-me-not or Chhui-mui plant. When you gently touch a single leaflet, the entire leaf rapidly folds inward and "
            "droops downwards in seconds. Because plants have no nerves, how is this touch information transmitted across the plant body? Plant "
            "cells communicate touch stimuli from cell to cell using electrical-chemical signals, analogous to animal impulses. Furthermore, because plants have no "
            "contractile muscle proteins, how do plant leaves physically move? Plant cells change their shape not through sliding proteins, but by "
            "altering their internal water content. Specialized swollen structures called pulvini located at the bases of leaves and petioles act as "
            "hydraulic hinges. When the electrical-chemical signal arrives at the pulvinus, cells rapidly lose water to surrounding intercellular spaces. The resulting "
            "sudden loss of turgor pressure causes pulvinar cells to shrink and collapse, causing the entire leaf to droop dramatically and protectively."
        ),
        "checkpoints": [
            {
                "question": "How do cells of the sensitive plant Mimosa pudica change shape to execute rapid leaf folding?",
                "options": [
                    "By rapidly changing their internal water content, causing swelling or shrinking",
                    "By contracting specialized animal-like actin and myosin protein filaments",
                    "By shedding outer dead bark tissues into surrounding garden soil",
                    "By secreting concentrated hydrochloric acid from salivary glands"
                ],
                "answer": 0,
                "hint": "Water movement changes cell turgor pressure in specialized pulvinus leaf bases.",
                "explanation": "Plant cells change shape by shifting water content; sudden water loss in pulvinus cells causes them to shrink and fold."
            },
            {
                "question": "What type of plant movement is exemplified by the rapid drooping of Mimosa pudica leaves upon touch?",
                "options": [
                    "A non-directional nastic movement completely independent of growth",
                    "A positive phototropic growth movement toward ambient sunlight",
                    "A negative geotropic growth response directed away from gravity",
                    "A chemotropic growth response guided by floral pollen tubes"
                ],
                "answer": 0,
                "hint": "It happens immediately and does not require cellular growth or elongation.",
                "explanation": "The rapid folding of touch-me-not leaves is a nastic movement—an immediate, reversible response independent of growth."
            }
        ]
    },
    {
        "id": 8,
        "title": "Plant Directional Tropisms",
        "subtitle": "Thigmotropism, Geotropism, Hydrotropism & Chemotropism",
        "speech": (
            "Unlike immediate nastic folding, tropic movements are directional growth movements occurring slowly in response to external environmental stimuli. If the "
            "plant organ grows toward the stimulus, it is positive tropism; if it grows away, it is negative tropism. First, "
            "consider thigmotropism, directional growth in response to physical touch. Climbing plants like peas possess delicate, wiry tendrils. When a tendril "
            "touches an external support such as a fence or bamboo stake, the tendril cells in direct physical contact with the "
            "support grow slowly, while cells on the opposite side away from contact elongate rapidly. This unequal growth rate forces the "
            "tendril to coil tightly around the support, anchoring the climbing plant. Second, consider geotropism, growth in response to gravity. In "
            "a horizontal potted seedling, roots exhibit positive geotropism, growing downwards into soil to secure water and anchorage, while shoots display "
            "negative geotropism, growing upwards into air towards light. Third, hydrotropism directs root tips to bend towards moist soil zones. Fourth, "
            "chemotropism is directional growth in response to chemical stimuli, illustrated by the growth of the pollen tube through the female "
            "flower style towards the ovarian ovule, demonstrating how environmental stimuli guide plant growth architecture with remarkable evolutionary precision."
        ),
        "checkpoints": [
            {
                "question": "What differential growth mechanism causes pea plant climbing tendrils to coil tightly around a wooden support?",
                "options": [
                    "Tendril cells away from the support elongate faster than cells in direct contact",
                    "Tendril cells in direct contact with the support divide ten times faster",
                    "The support secretes toxic hydrochloric acid that burns outer tendril hairs",
                    "Turgor pressure permanently bursts all cells touching the bamboo stake"
                ],
                "answer": 0,
                "hint": "Unequal growth rates on opposite flanks of the tendril cause circular curving.",
                "explanation": "Cells on the outer side away from the support grow faster than contact cells, causing the tendril to coil around the support."
            },
            {
                "question": "Which of the following is a classic example of chemotropism in angiosperm flowering plants?",
                "options": [
                    "Growth of the pollen tube through the style towards the ovary ovule",
                    "Upward bending of a green stem seedling towards blue daylight",
                    "Rapid hydraulic drooping of Mimosa pudica leaflets when touched",
                    "Downward growth of primary taproots into underground soil"
                ],
                "answer": 0,
                "hint": "A chemical attractant released by the ovule directs the pollen tube's path.",
                "explanation": "Pollen tube growth toward the ovule is driven by chemical attractants, exemplifying positive chemotropism."
            }
        ]
    }
]

with open('.agents/c10s_ch6_part1.json', 'w', encoding='utf-8') as f:
    json.dump(slides_part1, f, indent=2)

print("Slide part 1 (Slides 1-8) successfully written!")
for s in slides_part1:
    wc = len(s['speech'].split())
    print(f"Slide {s['id']}: '{s['title']}' - {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} speech word count {wc} out of range!"

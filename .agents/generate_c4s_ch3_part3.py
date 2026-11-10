# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 3: Nature Trail
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (replaced with generic roles).
Zero lecturer personas.
Clean Unicode throughout.
"""

def make_sol_html(steps, note=None):
    items = "".join(f"<li class='mb-2 text-slate-700 leading-relaxed'>{s}</li>" for s in steps)
    html = f"<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside space-y-1.5 text-sm'>{items}</ol></div>"
    if note:
        html += f"<div class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> {note}</div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "slide_num": 17,
        "title": "Challenge 1",
        "section": "Pachmarhi, Forest Rules & Mammal Traits",
        "speech": "",
        "quizzes": [
            {
                "question": "In which Indian mountain range and state is the Pachmarhi Biosphere Reserve located?",
                "options": [
                    "Aravalli Hills in Rajasthan",
                    "Satpura Range in Madhya Pradesh",
                    "Western Ghats in Goa",
                    "Himalayan Range in Uttarakhand"
                ],
                "correct": 1,
                "hint": "Think of the central Indian state known for its teak forests and Satpura hills.",
                "explanation": "Pachmarhi Biosphere Reserve is located in the Satpura mountain range of Madhya Pradesh.",
                "sol": make_sol_html([
                    "Pachmarhi is situated in Hoshangabad district of Madhya Pradesh.",
                    "It encompasses diverse ecosystems within the Satpura hill range.",
                    "It is internationally recognized as a UNESCO Biosphere Reserve."
                ], "Pachmarhi protects rich Satpura biodiversity in central Madhya Pradesh.")
            },
            {
                "question": "Why is keeping quiet and walking softly an essential safety rule during a forest nature trail?",
                "options": [
                    "To prevent trees from falling asleep",
                    "To avoid startling wild animals so they remain calm and behave naturally in their habitats",
                    "Because talking is illegal in all parks",
                    "To help sound waves turn into rocks"
                ],
                "correct": 1,
                "explanation": "Quiet walking avoids alarming wildlife, allowing observers to watch natural animal behaviors safely.",
                "sol": make_sol_html([
                    "Wild animals have acute hearing and perceive loud human noises as threats.",
                    "Sudden noises cause animals to flee or trigger defensive aggressive reactions.",
                    "Walking quietly ensures safe observation without disrupting forest life."
                ], "Quiet movement preserves natural wildlife behavior and ensures trail safety.")
            },
            {
                "question": "What grave hazard do discarded polythene bags pose to forest herbivores like deer and cows?",
                "options": [
                    "Plastic bags make deer run too fast",
                    "Animals may ingest plastic bags while foraging, causing fatal digestive blockages",
                    "Plastic bags turn into flowers",
                    "Plastic bags melt into honey"
                ],
                "correct": 1,
                "explanation": "Herbivores accidentally ingest plastic bags smelling of food, leading to severe intestinal impaction and death.",
                "sol": make_sol_html([
                    "Plastic bags do not decompose and cannot be digested by animal stomachs.",
                    "Ingested plastic creates permanent physical obstructions in the intestines.",
                    "This leads to starvation, internal toxicity, and painful death for wildlife."
                ], "Polythene litter is a lethal hazard to grazing wildlife in protected areas.")
            },
            {
                "question": "Which physical trait allows an Asian elephant's trunk to perform both heavy lifting and delicate picking?",
                "options": [
                    "It contains hundreds of hard bones",
                    "It is a boneless muscular hydrostat composed of over 40,000 flexible muscle bundles",
                    "It is filled with wooden cartilage",
                    "It is controlled by metal wires"
                ],
                "correct": 1,
                "explanation": "The elephant's trunk has over 40,000 muscle units and zero bones, providing unmatched strength and dexterity.",
                "sol": make_sol_html([
                    "The trunk unites the upper lip and nose into an elongated muscular hydrostat.",
                    "The absence of rigid bones permits movement in any direction.",
                    "A finger-like projection at the tip can grasp objects as tiny as a blade of grass."
                ], "The elephant trunk combines immense muscular power with microscopic dexterity.")
            },
            {
                "question": "What is the key functional role of the exceptionally long, bushy tail of the Indian Giant Squirrel in Pachmarhi?",
                "options": [
                    "It acts as a digging shovel in soil",
                    "It serves as a stabilizing counterweight during daring leaps between high tree branches",
                    "It is used to store drinking water",
                    "It frightens away predatory tigers"
                ],
                "correct": 1,
                "explanation": "The long bushy tail acts like a tightrope walker's balance pole, stabilizing leaps of up to six meters in canopies.",
                "sol": make_sol_html([
                    "The Indian Giant Squirrel is an entirely arboreal rodent.",
                    "Its tail can measure up to two feet in length, matching its body size.",
                    "Shifting the tail counterbalances its center of mass during high-velocity canopy leaps."
                ], "The bushy tail provides critical aerodynamic balance in high forest canopies.")
            },
            {
                "question": "The Spectacled Monkey (Phayre's leaf monkey) is the celebrated official state animal of which Indian state?",
                "options": [
                    "Gujarat",
                    "Tripura",
                    "Punjab",
                    "Maharashtra"
                ],
                "correct": 1,
                "explanation": "The Spectacled Monkey is the official state animal of Tripura in northeastern India.",
                "sol": make_sol_html([
                    "Phayre's leaf monkey is native to the primary forests of Tripura.",
                    "It is distinguished by prominent white ocular rings resembling spectacles.",
                    "Tripura designated this endangered primate as its state symbol to boost conservation."
                ], "The Spectacled Monkey represents Tripura's lush rainforest biodiversity.")
            },
            {
                "question": "How does the specialized multi-chambered stomach of the Spectacled Monkey assist its survival?",
                "options": [
                    "It allows it to swallow small rocks for weight",
                    "It uses symbiotic bacteria to ferment and digest tough, cellulose-rich leaves",
                    "It stores meat for winter months",
                    "It turns river water into milk"
                ],
                "correct": 1,
                "explanation": "The complex stomach hosts specialized microbes that ferment tough cellulose fibers found in tree leaves.",
                "sol": make_sol_html([
                    "Leaves contain structural cellulose that simple stomachs cannot break down.",
                    "The monkey's multi-chambered stomach functions similarly to a cow's rumen.",
                    "Bacterial fermentation extracts nutrients while neutralizing plant toxins."
                ], "Specialized leaf-eating stomachs allow folivores to extract energy from tough canopy foliage.")
            },
            {
                "question": "Why should hikers wear earth-toned clothing (greens, khakis, browns) rather than bright fluorescent colors on a nature trail?",
                "options": [
                    "Bright clothes make clothes heavier to wear",
                    "Earth tones blend into the forest foliage, reducing visual disturbance to watchful wildlife",
                    "Forest trees absorb bright clothes",
                    "Fluorescent clothes attract rainstorms"
                ],
                "correct": 1,
                "explanation": "Earth tones mimic natural forest colors, helping observers blend in without alarming wild animals.",
                "sol": make_sol_html([
                    "Animals rely heavily on vision to detect unnatural intrusions into their territory.",
                    "Fluorescent colors stand out starkly against green and brown foliage.",
                    "Earth tones provide camouflage, allowing closer, safer wildlife observation."
                ], "Earth-toned attire minimizes visual disturbance to sensitive forest fauna.")
            },
            {
                "question": "Which of the following describes an arboreal animal correctly?",
                "options": [
                    "An animal that burrows deep underground in darkness",
                    "An animal that spends the majority of its life climbing and living among tree canopies",
                    "An animal that lives exclusively in open ocean waters",
                    "An animal that lives only on glaciers"
                ],
                "correct": 1,
                "explanation": "Arboreal animals, like monkeys and tree squirrels, are adapted for life among tree branches.",
                "sol": make_sol_html([
                    "Arboreal refers specifically to tree-dwelling organisms.",
                    "These species feature gripping hands, claws, prehensile tails, or strong leaping legs.",
                    "Canopies provide them with fruits, tender leaves, insects, and safety from ground predators."
                ], "Arboreal adaptations specialize creatures for three-dimensional canopy living.")
            },
            {
                "question": "What is the primary conservation ethic summarized by the phrase: 'Leave only footprints, take only memories'?",
                "options": [
                    "Visitors should collect wild orchids to plant in pots at home",
                    "Visitors must preserve the forest untouched, removing no natural items and leaving no litter behind",
                    "Visitors should carve their names into tree bark",
                    "Visitors should paint rocks with bright colors"
                ],
                "correct": 1,
                "explanation": "This golden rule reminds hikers to protect wilderness areas by taking no specimens and leaving zero trash.",
                "sol": make_sol_html([
                    "Every rock, leaf, and shell plays a role in the forest ecosystem.",
                    "Removing natural items deprives organisms of food, minerals, or shelters.",
                    "Leaving zero waste ensures habitats remain pure and pristine for future generations."
                ], "True nature explorers respect the forest by disturbing nothing and leaving no trace.")
            }
        ]
    },
    {
        "slide_num": 18,
        "title": "Challenge 2",
        "section": "Tracking, Lookalikes, Birds & Adaptation",
        "speech": "",
        "quizzes": [
            {
                "question": "What are animal footprints pressed into soft, damp mud or sand called by wildlife trackers?",
                "options": [
                    "Pugmarks",
                    "Fossils",
                    "Petroglyphs",
                    "Burrows"
                ],
                "correct": 0,
                "explanation": "Footprints left by wild animals in soil, sand, or mud are known as pugmarks.",
                "sol": make_sol_html([
                    "Trackers study footprint contours, pad shapes, and step lengths.",
                    "Pugmarks identify the animal's species, sex, age, and health condition.",
                    "Forest departments use pugmark tracking censuses to monitor big cat populations."
                ], "Pugmarks provide vital biometric clues for monitoring wildlife populations.")
            },
            {
                "question": "Why do footprints of wild canines (dogs, jackals, wolves) always show claw marks, while cat prints do not?",
                "options": [
                    "Cats do not possess any claws",
                    "Canines have non-retractable claws, whereas big cats keep their sharp claws retracted while walking",
                    "Dogs walk on their toes while cats walk on their heels",
                    "Cats file their claws flat every morning"
                ],
                "correct": 1,
                "explanation": "Canine claws cannot retract, leaving marks in mud; feline claws retract into sheaths to stay razor sharp.",
                "sol": make_sol_html([
                    "Big cats retract their claws to protect them from blunting against hard rocks.",
                    "When walking, only soft fleshy digital pads touch the substrate.",
                    "Canine claws remain permanently extended to provide traction during high-speed chases."
                ], "Retractable claws keep cat footprints clawless and maintain razor-sharp hunting edges.")
            },
            {
                "question": "Which morphological trait distinguishes a crocodile's head from an alligator's head?",
                "options": [
                    "Crocodiles have feathers on their eyelids",
                    "Crocodiles have a pointed, V-shaped snout, while alligators possess a broader, U-shaped snout",
                    "Alligators have bright green beaks",
                    "Crocodiles have three eyes"
                ],
                "correct": 1,
                "explanation": "Crocodiles have narrower V-shaped snouts with visible lower teeth; alligators have broad U-shaped snouts.",
                "sol": make_sol_html([
                    "Snout shape directly reflects specialized feeding adaptations.",
                    "The crocodile's pointed V-snout cuts through water to seize fish.",
                    "The alligator's broad U-snout crushes hard-shelled prey like freshwater turtles."
                ], "Snout geometry easily differentiates crocodiles (V-shaped) from alligators (U-shaped).")
            },
            {
                "question": "How does a female hornbill protect her eggs and chicks from predators during nesting?",
                "options": [
                    "She buries them under sand like a sea turtle",
                    "She walls herself inside a tree cavity using mud, leaving only a tiny feeding slit",
                    "She leaves them in a crocodile's nest",
                    "She carries eggs in a pouch like a kangaroo"
                ],
                "correct": 1,
                "explanation": "The mother hornbill seals the entrance of a tree hollow with mud and feces, leaving a narrow slit for the male to deliver food.",
                "sol": make_sol_html([
                    "Sealing the nest hole prevents predatory snakes and civets from entering.",
                    "The male hornbill forages tirelessly, delivering berries and insects through the slit.",
                    "Once the chicks are half-grown, the mother breaks out to help gather food."
                ], "Hornbill nesting cavities offer secure protection against canopy predators.")
            },
            {
                "question": "What are the glittering eye-like circular spots on a male peacock's tail feathers called?",
                "options": [
                    "Casques",
                    "Ocelli",
                    "Lamellae",
                    "Talons"
                ],
                "correct": 1,
                "explanation": "The iridescent, circular spots on a peacock's ornamental train feathers are scientifically called ocelli.",
                "sol": make_sol_html([
                    "Ocelli produce shimmering structural colors through microscopic feather barbules.",
                    "The arrangement and symmetry of ocelli signal physical vigor to peahens.",
                    "Courtship displays involve shivering these feathers to produce rhythmic acoustic rustling."
                ], "Ocelli are iridescent circular eye-spots used in courtship visual displays.")
            },
            {
                "question": "How do facial feather discs and asymmetric ears assist nocturnal barn owls in total darkness?",
                "options": [
                    "They produce electric lights",
                    "They funnel faint rustling sounds directly to the ears to pinpoint prey location with sound",
                    "They help owls smell flowers",
                    "They keep rain off the owl's beak"
                ],
                "correct": 1,
                "explanation": "The heart-shaped facial disc acts like a satellite dish, funneling sound waves directly into acoustic ear canals.",
                "sol": make_sol_html([
                    "Asymmetric ear placement allows the owl to compare arrival times of sound waves.",
                    "This acoustic triangulation pinpoints prey location down to a fraction of an inch.",
                    "An owl can successfully capture a mouse in pitch-black darkness relying purely on hearing."
                ], "Facial discs and acoustic asymmetry give owls three-dimensional hearing in the dark.")
            },
            {
                "question": "What type of beak and claws does a raptor like an eagle possess?",
                "options": [
                    "A flat strainer beak and webbed swimming feet",
                    "A hooked tearing beak and sharp, curved grasping talons",
                    "A slender drinking tube and two backward-pointing toes",
                    "A soft rubbery bill and paddle feet"
                ],
                "correct": 1,
                "explanation": "Eagles have razor-sharp, hooked beaks for tearing meat and curved talons for seizing prey.",
                "sol": make_sol_html([
                    "Raptors hunt live vertebrates including rodents, snakes, and fish.",
                    "Muscular talons lock onto prey with tremendous crushing grip pressure.",
                    "The sharply curved upper mandible acts like a hook to tear portions of meat."
                ], "Hooked beaks and sharp talons are classic anatomical tools of birds of prey.")
            },
            {
                "question": "What is the function of the comb-like 'lamellae' lining the edges of a duck's broad, flat bill?",
                "options": [
                    "To chew tough meat bones",
                    "To filter tiny aquatic plants, seeds, and insects from muddy water",
                    "To polish feathers like a comb",
                    "To whistle songs to other ducks"
                ],
                "correct": 1,
                "explanation": "Lamellae act as strainers, allowing water and mud to squirt out while retaining edible seeds and larvae inside.",
                "sol": make_sol_html([
                    "Ducks scoop mouthfuls of muddy pond water from shallows.",
                    "Pumping the tongue forces water out through the comb-like lamellae.",
                    "Nutritious seeds, duckweed, and aquatic larvae remain trapped behind to be swallowed."
                ], "Lamellae serve as biological micro-filters for dabbling ducks in murky wetlands.")
            },
            {
                "question": "How does the zygodactyl foot arrangement (two toes forward, two backward) benefit woodpeckers?",
                "options": [
                    "It allows them to swim across broad rivers",
                    "It enables them to clamp securely onto vertical tree bark while chiseling wood",
                    "It lets them walk on lily pads",
                    "It helps them dig deep rabbit burrows"
                ],
                "correct": 1,
                "explanation": "Two forward toes and two backward toes provide an opposing pincer grip, anchoring the bird firmly to vertical trunks.",
                "sol": make_sol_html([
                    "Most birds have three toes forward and one backward (anisodactyl).",
                    "Woodpeckers adapt two toes forward and two toes backward (zygodactyl).",
                    "Combined with stiff tail feathers, this creates a sturdy tripod support for hammering."
                ], "Zygodactyl feet provide rock-solid vertical clamping power on tree bark.")
            },
            {
                "question": "What vital information should a student naturalist record when maintaining a field 'Bird Diary'?",
                "options": [
                    "Fictional fairy tale adventures",
                    "Date, time, weather, plumage field marks, habitat, vocalizations, and observed behaviors",
                    "Names of television characters",
                    "Prices of cinema tickets"
                ],
                "correct": 1,
                "explanation": "A scientific bird diary logs date, weather, location, plumage markings, calls, and feeding behaviors.",
                "sol": make_sol_html([
                    "Standardized records allow comparison across seasons and habitats.",
                    "Field marks like wing-bars, eye-stripes, and beaks identify species accurately.",
                    "Noting behaviors reveals ecological roles like foraging, courting, or nesting."
                ], "Systematic field notes turn casual bird observation into rigorous science.")
            }
        ]
    },
    {
        "slide_num": 19,
        "title": "Challenge 3",
        "section": "Aquatic Wildlife & Insect Anatomy",
        "speech": "",
        "quizzes": [
            {
                "question": "Why do swimming fish possess a spindle-shaped, streamlined body profile?",
                "options": [
                    "To make them look like submarines",
                    "To minimize hydrodynamic drag and slice smoothly through water currents",
                    "To allow them to walk across land",
                    "To absorb sunlight directly into bones"
                ],
                "correct": 1,
                "explanation": "Streamlined spindle bodies taper at both ends, drastically reducing water friction and drag while swimming.",
                "sol": make_sol_html([
                    "Water is roughly 800 times denser than air, creating high resistance.",
                    "A tapered, teardrop profile allows water to flow smoothly along the sides.",
                    "This hydrodynamic shape conserves muscular energy during propulsion."
                ], "Streamlining minimizes water resistance, enabling rapid and efficient swimming.")
            },
            {
                "question": "What is the critical biological function of a fish's gills?",
                "options": [
                    "To chew food like teeth",
                    "To extract dissolved oxygen gas directly from water flowing over them",
                    "To generate electricity",
                    "To fly into air"
                ],
                "correct": 1,
                "explanation": "Gills possess thin, blood-rich filaments that absorb dissolved oxygen from water and expel carbon dioxide.",
                "sol": make_sol_html([
                    "Water enters through the mouth and is pumped across gill arches.",
                    "Microscopic capillaries in gill lamellae facilitate gas exchange.",
                    "Oxygen diffuses into red blood cells, while carbon dioxide diffuses into the water."
                ], "Gills extract dissolved oxygen directly from water through countercurrent exchange.")
            },
            {
                "question": "What is the hard, protective upper shell of a freshwater turtle called scientifically?",
                "options": [
                    "Plastron",
                    "Carapace",
                    "Casque",
                    "Elytra"
                ],
                "correct": 1,
                "explanation": "The upper domed shell of a turtle is the carapace, fused directly to its backbone and rib cage.",
                "sol": make_sol_html([
                    "The turtle shell is a living structure made of modified rib and vertebral bones.",
                    "The upper arched dorsal shield is called the carapace.",
                    "The flat lower ventral belly plate is called the plastron."
                ], "The bony carapace provides armor plating that shields internal organs from predators.")
            },
            {
                "question": "How do tadpoles differ from adult frogs in terms of respiration and locomotion?",
                "options": [
                    "Tadpoles breathe with lungs and have walking legs",
                    "Tadpoles breathe using gills and swim with tails, whereas adult frogs use lungs, skin, and hopping legs",
                    "Tadpoles fly in the air with feathered wings",
                    "Tadpoles never live in water"
                ],
                "correct": 1,
                "explanation": "Tadpoles are fully aquatic gill-breathers with swimming tails; adult frogs develop lungs, skin breathing, and jumping legs.",
                "sol": make_sol_html([
                    "Amphibian metamorphosis transforms body architecture completely.",
                    "Aquatic tadpoles absorb oxygen through external and internal gills.",
                    "Adult frogs reabsorb their tail, grow powerful legs, and breathe via lungs and skin."
                ], "Metamorphosis transitions frogs from gill-breathing tadpoles to amphibious adults.")
            },
            {
                "question": "What are the three distinct anatomical body segments shared by all true adult insects?",
                "options": [
                    "Beak, wings, and tail",
                    "Head, thorax, and abdomen",
                    "Carapace, plastron, and flippers",
                    "Root, stem, and leaf"
                ],
                "correct": 1,
                "explanation": "All insects have bodies divided into three tagmata: head, thorax, and abdomen.",
                "sol": make_sol_html([
                    "The head bears mouthparts, eyes, and sensory antennae.",
                    "The middle thorax anchors three pairs of jointed legs and flight wings.",
                    "The posterior abdomen houses digestive, excretory, and reproductive organs."
                ], "Head, thorax, and abdomen form the universal three-part insect body plan.")
            },
            {
                "question": "How many total jointed walking legs do all true adult insects possess?",
                "options": [
                    "Four legs (two pairs)",
                    "Six legs (three pairs)",
                    "Eight legs (four pairs)",
                    "Ten legs (five pairs)"
                ],
                "correct": 1,
                "explanation": "All true insects belong to the subphylum Hexapoda, meaning six legs (three pairs attached to the thorax).",
                "sol": make_sol_html([
                    "Insects are distinguished from eight-legged arachnids (spiders).",
                    "All six legs are attached exclusively to the thoracic segments.",
                    "Jointed legs enable running, jumping, swimming, or digging."
                ], "Six jointed thoracic legs define all true adult insects.")
            },
            {
                "question": "What vital sensory roles do an insect's antennae perform?",
                "options": [
                    "They digest wood chips",
                    "They smell airborne pheromones, detect tactile vibrations, and monitor air currents",
                    "They shoot poison arrows",
                    "They store drinking water"
                ],
                "correct": 1,
                "explanation": "Insect antennae are covered in microscopic sensory sensilla that detect scents, humidity, vibrations, and wind.",
                "sol": make_sol_html([
                    "Antennae function simultaneously as noses and tactile feelers.",
                    "Moths detect female scent molecules from miles away using feathery antennae.",
                    "Ants tap antennae to exchange chemical messages along marching trails."
                ], "Antennae are multisensory instruments for smell, touch, and chemical communication.")
            },
            {
                "question": "What are the hardened, protective outer wing covers of beetles called?",
                "options": [
                    "Ocelli",
                    "Elytra",
                    "Lamellae",
                    "Talons"
                ],
                "correct": 1,
                "explanation": "A beetle's hardened, armor-like forewings are called elytra; they shield the delicate membranous flight wings beneath.",
                "sol": make_sol_html([
                    "Beetles belong to the order Coleoptera, meaning 'sheathed wings'.",
                    "The front pair of wings is heavily sclerotized into rigid protective plates (elytra).",
                    "During flight, elytra open up to allow the transparent hindwings to beat."
                ], "Elytra form protective armor covers that shield a beetle's flight wings.")
            },
            {
                "question": "How does the praying mantis utilize its unique anatomical adaptations to capture insect prey?",
                "options": [
                    "By swimming after fish in deep rivers",
                    "By camouflaging as green foliage and snapping spiny raptorial forelegs in milliseconds",
                    "By spinning huge sticky spider webs",
                    "By singing loud songs"
                ],
                "correct": 1,
                "explanation": "The mantis blends into vegetation and strikes with spiny, folding raptorial front legs with incredible speed.",
                "sol": make_sol_html([
                    "Cryptic coloration matches leaves, twigs, or blossoms perfectly.",
                    "A highly mobile triangular head swivels 180 degrees to track moving prey.",
                    "Spiny forelegs snap shut like a switchblade, trapping prey securely."
                ], "Raptorial front legs and cryptic camouflage make the praying mantis an ambush predator.")
            },
            {
                "question": "What crucial ecological services do worker bees and ants provide to forest ecosystems?",
                "options": [
                    "They build concrete highways",
                    "Bees pollinate flowering trees while ants aerate soil, disperse seeds, and clean organic waste",
                    "They dry up forest rivers",
                    "They cut down mature oak trees"
                ],
                "correct": 1,
                "explanation": "Bees are indispensable pollinators of flowering plants, while ants aerate soil, distribute seeds, and scavenge waste.",
                "sol": make_sol_html([
                    "Pollination by bees ensures fruit setting, seed creation, and forest regeneration.",
                    "Ant tunneling loosens dense soil, allowing air and rainwater to reach roots.",
                    "Ant scavenging cleans decomposing animal and plant debris from the forest floor."
                ], "Bees and ants are foundational ecosystem engineers maintaining forest vitality.")
            }
        ]
    },
    {
        "slide_num": 20,
        "title": "Challenge 4",
        "section": "Leaves, Venation, Web of Life & Conservation",
        "speech": "",
        "quizzes": [
            {
                "question": "What is the primary function of the central 'midrib' running down the middle of a leaf?",
                "options": [
                    "To generate loud musical tones",
                    "To provide structural support to the leaf blade and house main xylem and phloem transport tubes",
                    "To attract harmful beetles",
                    "To store heavy rocks"
                ],
                "correct": 1,
                "explanation": "The midrib provides structural rigidity and contains primary vascular bundles (xylem and phloem) for fluid transport.",
                "sol": make_sol_html([
                    "The midrib acts like the central spine of the leaf blade.",
                    "It anchors branching lateral veins across the green lamina.",
                    "It delivers water from the petiole and exports synthesized sugars."
                ], "The midrib provides skeletal rigidity and acts as the central vascular pipeline of a leaf.")
            },
            {
                "question": "Which of the following plants displays classic 'reticulate' (net-like) leaf venation?",
                "options": [
                    "Maize and wild grasses",
                    "Peepal, banyan, and mango trees",
                    "Bamboo plants",
                    "Banana leaves"
                ],
                "correct": 1,
                "explanation": "Dicot trees like peepal, banyan, and mango have branching veins that form an interconnected net (reticulate venation).",
                "sol": make_sol_html([
                    "Reticulate venation features lateral veins repeatedly dividing into veinlets.",
                    "This forms a complex interlocking mesh across the leaf blade.",
                    "In contrast, monocots like grasses and bamboo feature parallel venation."
                ], "Peepal and mango leaves exhibit net-like reticulate venation.")
            },
            {
                "question": "Why does a leaf autograph (crayon rubbing) require the rough underside of the leaf to face upward?",
                "options": [
                    "Because the upper side is made of wood",
                    "Because leaf veins protrude raised ridges on the underside that catch crayon wax to create a detailed impression",
                    "Because the underside is completely flat like glass",
                    "Because crayon wax only sticks to dirt"
                ],
                "correct": 1,
                "explanation": "Veins protrude prominently on the lower leaf surface, creating raised texture that transfers onto paper under crayon pressure.",
                "sol": make_sol_html([
                    "The upper leaf surface is relatively smooth and waxy.",
                    "The lower leaf surface has raised vascular ridges.",
                    "Rubbing sideways across these ridges transfers the structural skeleton to paper."
                ], "Raised vein ridges on the leaf underside produce crisp botanical crayon impressions.")
            },
            {
                "question": "What do the interconnected strings represent in the 'Web of Life' simulation game?",
                "options": [
                    "Telegraph cables connecting schools",
                    "The intricate network of feeding dependencies, energy pathways, and mutual ecological connections in nature",
                    "Fences dividing private farms",
                    "String instruments playing songs"
                ],
                "correct": 1,
                "explanation": "The yarn represents feeding links, nutrient cycles, and energy flows that bind all forest species together.",
                "sol": make_sol_html([
                    "Every strand symbolizes a direct or indirect ecological relationship.",
                    "Sunlight feeds plants, plants feed herbivores, herbivores nourish carnivores.",
                    "Decomposers close the loop by returning nutrients to soil and plants."
                ], "Yarn strings illustrate the invisible web of interdependence that supports all life.")
            },
            {
                "question": "What happens across an ecosystem when a key element like trees is removed by widespread deforestation?",
                "options": [
                    "Animals thrive and double in population",
                    "The entire web slacks: herbivores lose food, soil erodes into rivers, and interconnected species face starvation",
                    "Rivers turn into sweet syrup",
                    "Nothing changes for forest animals"
                ],
                "correct": 1,
                "explanation": "Removing trees collapses food chains, destroys wildlife shelters, and causes severe soil erosion and river silting.",
                "sol": make_sol_html([
                    "Trees are primary autotrophic producers and foundational habitat anchors.",
                    "Without canopy shade, forest soils dry out and wash away during rains.",
                    "Herbivores starve, causing secondary collapse among carnivores and pollinators."
                ], "Deforestation unravels ecological links, triggering systemic habitat collapse.")
            },
            {
                "question": "Why does eliminating top apex predators (like tigers) trigger ecological imbalance in forest ecosystems?",
                "options": [
                    "Deer populations grow unchecked, leading to overgrazing that destroys tree saplings and causes soil degradation",
                    "Tigers are the only animals that plant grass",
                    "Forest trees stop producing oxygen without tigers",
                    "Rivers stop flowing without tigers"
                ],
                "correct": 0,
                "explanation": "Without apex carnivores, herbivore numbers surge uncontrollably, leading to destructive overgrazing and forest decline.",
                "sol": make_sol_html([
                    "Apex predators regulate herbivore populations through natural predation.",
                    "Unregulated deer herds overgraze forest understory and eat tender saplings.",
                    "Without young trees maturing, the forest loses its ability to regenerate."
                ], "Apex predators maintain trophic balance, preventing overgrazing and preserving forests.")
            },
            {
                "question": "What is the official state bird of Madhya Pradesh, celebrated for its long, streaming white tail feathers?",
                "options": [
                    "The common house crow",
                    "The Asian Paradise Flycatcher (Dudhraj)",
                    "The blue rock pigeon",
                    "The barn owl"
                ],
                "correct": 1,
                "explanation": "The Asian Paradise Flycatcher (locally called Dudhraj) is the official state bird of Madhya Pradesh.",
                "sol": make_sol_html([
                    "Adult male Paradise Flycatchers display dazzling white plumage.",
                    "They possess two elongated ribbon-like central tail feathers.",
                    "They catch flying insects acrobatically in mid-air beneath forest canopies."
                ], "The Asian Paradise Flycatcher (Dudhraj) is the graceful state bird of Madhya Pradesh.")
            },
            {
                "question": "Which magnificent deer with twelve-tined antlers is designated as the state animal of Madhya Pradesh?",
                "options": [
                    "The blackbuck",
                    "The Barasingha (swamp deer)",
                    "The spotted chital",
                    "The musk deer"
                ],
                "correct": 1,
                "explanation": "The Barasingha (Rucervus duvaucelii), or swamp deer, is the state animal of Madhya Pradesh.",
                "sol": make_sol_html([
                    "Barasingha means 'twelve-horned' in Hindi, referring to its multi-tined antlers.",
                    "Kanha National Park saved the hard-ground swamp deer from near extinction.",
                    "It stands as a shining triumph of modern Indian wildlife conservation."
                ], "The Barasingha is the iconic twelve-antlered state animal of Madhya Pradesh.")
            },
            {
                "question": "How does creating paper origami wildlife models (like turtles) help students connect with nature conservation?",
                "options": [
                    "By teaching students how to make plastic garbage",
                    "By combining hands-on craft with learning about animal anatomy, habitats, and endangered species protection",
                    "By replacing living wild animals with paper toys in forests",
                    "By encouraging students to collect wild turtle eggs"
                ],
                "correct": 1,
                "explanation": "Origami crafts foster emotional empathy, reinforce anatomical knowledge, and encourage conservation commitments.",
                "sol": make_sol_html([
                    "Folding paper models demands focus on structural features like shells and flippers.",
                    "Students write personal environmental pledges onto their paper models.",
                    "This links artistic creativity with meaningful conservation stewardship."
                ], "Creative nature crafts build empathy and reinforce scientific wildlife understanding.")
            },
            {
                "question": "What is the most meaningful action young citizens can take to support biodiversity conservation in daily life?",
                "options": [
                    "Buying wild caged birds from pet markets",
                    "Planting native shade trees, avoiding single-use plastics, and treating all living creatures with respect",
                    "Throwing plastic bottles into forest streams",
                    "Chasing and teasing birds in community parks"
                ],
                "correct": 1,
                "explanation": "Planting native trees, refusing single-use plastics, and protecting local habitats are powerful daily conservation actions.",
                "sol": make_sol_html([
                    "Native trees support local birds, butterflies, and pollinating bees.",
                    "Eliminating plastic waste prevents toxic pollution in water bodies and soils.",
                    "Respecting all living things fosters an enduring culture of environmental stewardship."
                ], "Individual environmental habits collectively safeguard planetary biodiversity.")
            }
        ]
    }
]

if __name__ == "__main__":
    total_q = sum(len(s["quizzes"]) for s in slides_part3)
    print(f"Total quiz questions across Slides 17-20: {total_q}")
    assert total_q == 40, f"Expected 40 quiz questions, got {total_q}"
    for s in slides_part3:
        print(f"Slide {s['slide_num']}: '{s['title']}' -> {len(s['quizzes'])} questions")
        assert len(s["quizzes"]) == 10
        for i, q in enumerate(s["quizzes"]):
            assert len(q["options"]) == 4, f"Slide {s['slide_num']} Q{i+1} does not have 4 options"
            assert 0 <= q["correct"] <= 3, f"Slide {s['slide_num']} Q{i+1} correct index out of range"
            assert "sol" in q, f"Slide {s['slide_num']} Q{i+1} missing sol"
    print("All slides 17-20 validated successfully!")


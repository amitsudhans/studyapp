#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 5: Plants and Animals Live Together
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- No human character names, no lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Underground Soil Inhabitants",
        "subtitle": "Subterranean Life: Earthworms, Millipedes, and Natural Aeration",
        "speech": (
            "Step into the subterranean realm just beneath the soil surface, where miraculous creatures perform quiet engineering miracles! "
            "Among all underground dwellers, the humble earthworm stands out as nature's ultimate farmer. Earthworms possess moist, segmented, "
            "tubular bodies that glide smoothly through damp ground. As they move, earthworms ingest soil particles mixed with decaying organic leaves. "
            "Their digestive systems extract nutrients and excrete fine, nutrient-dense pellets known as earthworm castings. These castings are rich in bioavailable "
            "nitrogen, potassium, and phosphorus, enriching garden earth with superior natural fertilizer. Even more remarkably, as earthworms burrow tirelessly, "
            "they carve an extensive subterranean network of hollow micro-tunnels. These subterranean pathways allow oxygen to circulate deep down to suffocating "
            "plant roots and permit monsoon rainwater to percolate freely instead of running off and causing erosion. Alongside earthworms, long millipedes "
            "with dozens of delicate walking legs scurry through leaf litter, shredding tough fibrous plant stems into tiny fragments. When disturbed, millipedes "
            "curl protectively into tight, armored spirals. Without these subterranean soil inhabitants tirelessly aerating, breaking down debris, and enriching "
            "the earth, soil would become compacted, hard, and infertile. Earthworms and millipedes prove that life beneath our footsteps actively powers the growth "
            "of entire plant worlds above."
        ),
        "checkpoints": [
            {
                "question": "Why are earthworms often described by farmers as 'nature's plow'?",
                "options": [
                    "They cut down tall forest trees with sharp claws",
                    "Their burrowing aerates compacted soil and their castings provide rich natural fertilizer",
                    "They fly above fields scattering artificial chemical sprays",
                    "They store grain inside stone barns"
                ],
                "answer": 1,
                "hint": "Think about how their subterranean tunnels let air and water reach deep plant roots.",
                "explanation": "Earthworms dig burrows that loosen and aerate the soil while excreting organic castings that nourish surrounding plant roots."
            },
            {
                "question": "What defense mechanism does a millipede display when suddenly touched or threatened?",
                "options": [
                    "It flies up into the clouds",
                    "It curls tightly into an armored spiral to protect its soft underside",
                    "It changes its skin into bright blue water",
                    "It digs an underground diamond mine"
                ],
                "answer": 1,
                "hint": "Notice how the segmented body rolls into a compact circular coil.",
                "explanation": "When threatened, a millipede rolls its multi-segmented body into a tight spiral, protecting its vulnerable legs and soft underside."
            }
        ]
    },
    {
        "id": 10,
        "title": "Creeping Soil Insects",
        "subtitle": "Ants, Beetles, Termites, and Grasshoppers in the Litter Layer",
        "speech": (
            "Kneel down gently near the garden border and observe the bustling surface traffic of creeping soil insects! The upper soil horizon "
            "and leaf litter layer teem with organized insect communities working in continuous cooperation throughout every season. Watch a disciplined "
            "column of worker ants marching purposefully across crumbly soil particles. Ants communicate through invisible chemical scent trails called "
            "pheromones, guiding sisters toward fallen seeds, sweet nectar droplets, or dead insects. They carry these food morsels deep into underground "
            "labyrinth nests, aerating soil and burying seeds that later germinate into healthy green seedlings. Meanwhile, subterranean termites break "
            "down tough wooden cellulose from fallen tree branches using specialized gut microbes, rapidly cycling woody carbon back into fertile topsoil. "
            "Heavy-shelled ground beetles scurry across damp leaves, hunting destructive garden slugs and insect pests beneath dark stones. Nearby, camouflaged "
            "grasshoppers nibble on low blades of grass, using their powerful hind legs to launch into sudden escape leaps when threatened by predators. "
            "Each creeping insect plays an essential ecological role: shredding organic debris, dispersing dormant seeds, preying on garden pests, and recycling "
            "vital plant nutrients. This bustling insect community proves that even the tiniest creatures actively sustain the living soil fabric upon which entire "
            "forests and lush meadows depend."
        ),
        "checkpoints": [
            {
                "question": "How do foraging ants guide other colony members toward food sources on the soil surface?",
                "options": [
                    "By shouting loudly with vocal cords",
                    "By laying down invisible chemical scent trails called pheromones",
                    "By flashing bright colored lights from their antennae",
                    "By drawing arrows in the soil with wooden twigs"
                ],
                "answer": 1,
                "hint": "Ants use special scents that other ants can detect with their sensitive antennae.",
                "explanation": "Worker ants deposit chemical scent trails (pheromones) along the ground that guide fellow colony members directly to discovered food."
            },
            {
                "question": "What vital environmental role do subterranean termites perform in forest soil?",
                "options": [
                    "They manufacture plastic toys beneath the ground",
                    "They decompose tough dead wood and cellulose, returning essential nutrients back to the earth",
                    "They prevent rain from ever reaching tree roots",
                    "They turn garden flowers into solid ice"
                ],
                "answer": 1,
                "hint": "Termites digest fallen logs and dead branches that would otherwise clutter the forest floor.",
                "explanation": "Termites break down cellulose in fallen dead wood, recycling vital organic carbon and minerals back into the soil for living plants."
            }
        ]
    },
    {
        "id": 11,
        "title": "Herbivore Plant Foragers",
        "subtitle": "Diverse Feeding Habits of Camels, Monkeys, and Herbivores",
        "speech": (
            "Across diverse geographical habitats, herbivorous animals have developed remarkable anatomical adaptations to feed on specialized plant foods! "
            "In arid desert regions of Rajasthan, the hardy dromedary camel thrives where few other creatures can survive. Camels possess thick, leathery lips "
            "and heavily padded mouths that effortlessly chew thorny acacia branches, prickly cactus pads, and coarse scrub foliage without suffering painful "
            "wounds. Their long necks enable them to browse high tree foliage while storing metabolized energy in fatty humps during long treks. In lush deciduous "
            "woodlands, agile langurs and rhesus macaque monkeys leap energetically through the upper canopy. Monkeys use their nimble five-fingered hands to pluck "
            "ripe wild figs, succulent jamun berries, sweet mangoes, and tender leaf shoots. As monkeys feast high above, they often drop half-eaten fruits and "
            "fresh seeds onto the forest floor. This sloppy eating habit is not wasteful; it generously feeds ground-dwelling spotted deer, wild boars, and tortoises "
            "waiting patiently below, while scattering intact seeds far away from parent trees. From thorny desert scrubs to towering tropical canopies, "
            "herbivorous foragers have adapted distinct mouthparts, physical agility, and specialized digestive systems to harvest plant energy, illustrating "
            "the deep evolutionary partnership between animals and their botanical food supplies in nature."
        ),
        "checkpoints": [
            {
                "question": "What specialized adaptation allows desert camels to feed on prickly, thorny bushes without injury?",
                "options": [
                    "Sharp iron teeth replaced every week",
                    "Thick, leathery lips and toughened mouth linings that withstand sharp thorns",
                    "Chemical sprays that melt thorns into water",
                    "Eating only boiled thorns prepared by humans"
                ],
                "answer": 1,
                "hint": "Notice how thick skin on their lips and tongue prevents thorny punctures.",
                "explanation": "Camels possess dense, leathery mouth linings and thick prehensile lips that enable them to chew thorny desert foliage without injury."
            },
            {
                "question": "How does fruit-eating by canopy monkeys benefit other woodland creatures on the forest floor?",
                "options": [
                    "It blocks all rain from falling to the ground",
                    "Dropped fruits and scattered seeds provide nourishment for ground-dwelling animals and disperse new plants",
                    "It makes the forest completely silent at night",
                    "It removes all leaves from every tree"
                ],
                "answer": 1,
                "hint": "Monkeys drop partially eaten fruits and seeds that ground animals eagerly consume.",
                "explanation": "Fruit dropped by monkeys feeds ground animals such as deer and wild boars, while discarded seeds take root across the forest."
            }
        ]
    },
    {
        "id": 12,
        "title": "Nectar Sipping Pollinators",
        "subtitle": "Mutualistic Partnerships: Sunbirds, Butterflies, and Floral Nectar",
        "speech": (
            "Behold the radiant blossoms of flowering shrubs, where an exquisite biological dance called mutualistic pollination unfolds daily! "
            "Plants produce vibrant flower petals, sweet perfumes, and sugary liquid called nectar as an irresistible invitation for flying visitors. "
            "Watch a tiny purple sunbird hovering gracefully before an elongated red hibiscus bloom in the morning breeze. The sunbird possesses a slender, "
            "downward-curving beak perfectly shaped to slide deep into tubular blossoms, accompanied by a specialized tubular tongue that sips up rich nectar droplets. "
            "Fluttering alongside, colorful swallowtail butterflies uncoil their long, straw-like mouthparts—known as a proboscis—to drink sweet floral nectar from "
            "open marigold and zinnia flowers. But this partnership is never one-sided! As the sunbird and butterfly feed, their heads, feathers, and fuzzy "
            "legs brush against floral anthers, dusting them in golden pollen grains. When they fly to the next flower of the same species, some of this "
            "sticky pollen rubs off onto the receptive stigma. This crucial pollen transfer enables flowers to fertilize, develop sweet fruits, and produce "
            "viable seeds for the future. Without nectar-sipping pollinators, countless flowering plants and agricultural food crops could never reproduce, "
            "demonstrating how the mutual survival of plants and pollinators remains inextricably intertwined across our living planet."
        ),
        "checkpoints": [
            {
                "question": "What specialized anatomical tool do butterflies uncoil to drink sugary nectar from deep flower centers?",
                "options": [
                    "A broad wooden chisel beak",
                    "A long, slender tubular mouthpart called a proboscis",
                    "Sharp chewing pincers like a beetle",
                    "A pair of feathered wings"
                ],
                "answer": 1,
                "hint": "Think of a flexible biological drinking straw that curls up when not in use.",
                "explanation": "Butterflies use a coiled, straw-like tube called a proboscis to reach and sip sweet nectar deep inside flower petals."
            },
            {
                "question": "What vital service do pollinators provide to flowering plants while drinking nectar?",
                "options": [
                    "They prune dead branches with scissors",
                    "They transfer pollen grains between blossoms, enabling fertilization and seed production",
                    "They dig deep underground water wells",
                    "They paint the petals with artificial colors"
                ],
                "answer": 1,
                "hint": "Pollen grains stick to the pollinator's body and get transferred to the next blossom.",
                "explanation": "Pollinators transfer pollen from anther to stigma between flowers, allowing plants to fertilize, develop fruits, and produce seeds."
            }
        ]
    },
    {
        "id": 13,
        "title": "Canopy Resting Creatures",
        "subtitle": "Tree Branches as Sanctuaries for Leopards, Bats, and Wildlife",
        "speech": (
            "Look up into the dense, spreading canopy of ancient forest trees to discover how high branches serve as elevated sanctuaries! "
            "In Indian forests, the elusive leopard frequently utilizes horizontal tree limbs as strategic resting perches and predator-free safe zones. "
            "With powerful muscles and sharp retractable claws, a leopard easily hauls its heavy prey high up into the leafy fork of a banyan or mango tree, "
            "safely out of reach from prowling hyenas and wild dogs on the ground. Up among cool leafy shadows, the spotted big cat drapes its muscular limbs over "
            "a sturdy bough and sleeps soundly through hot afternoon hours. High above in the uppermost branches, colonies of Indian flying foxes—large "
            "fruit-eating bats—hang upside-down wrapped inside leathery wings. Their specialized curved claws hook effortlessly onto twigs without expending "
            "any muscle energy, allowing thousands of bats to roost quietly through the day. When twilight arrives, bats take flight to feast on wild figs, "
            "pollinating nighttime blossoms and scattering seeds across vast forest distances. High tree canopies provide reliable safety from ground predators, "
            "protection from muddy monsoon deluges, and refreshing cooling breezes. Forest trees prove to be elevated multistory hotels, housing powerful carnivores "
            "and gentle nocturnal flyers alike in peaceful harmony."
        ),
        "checkpoints": [
            {
                "question": "Why do leopards often haul their food and rest on high horizontal tree branches?",
                "options": [
                    "To hide food from underwater sharks",
                    "To protect their meals from ground scavengers and rest safely in cool, shaded canopy perches",
                    "Because they cannot walk on horizontal ground",
                    "To build woven nests out of Kapok cotton"
                ],
                "answer": 1,
                "hint": "Ground scavengers like hyenas cannot easily climb high vertical tree trunks.",
                "explanation": "Leopards hoist food and sleep on high tree branches to safeguard meals from scavengers and rest undisturbed in cool canopy shade."
            },
            {
                "question": "How do fruit-eating bats hang upside-down from tree twigs without falling while sleeping?",
                "options": [
                    "They use chemical tape on their wings",
                    "Their curved toe claws lock naturally around twigs under their own body weight",
                    "They hold on with their teeth throughout the day",
                    "They spin silk webs like spiders"
                ],
                "answer": 1,
                "hint": "Their curved claws have specialized tendons that lock automatically under body weight.",
                "explanation": "Bats have specialized locking tendon mechanisms in their feet, allowing their curved claws to grip twigs securely without muscle strain."
            }
        ]
    },
    {
        "id": 14,
        "title": "Listening Bird Calls",
        "subtitle": "Acoustic Identification, Sound Cupping, and Avian Communication",
        "speech": (
            "Close your eyes, stand quietly beneath a leafy canopy, and tune your senses to the rich acoustic symphony of bird calls! "
            "Birds use an astonishing variety of vocalizations to communicate territory, sound alarm warnings, and maintain contact with family flocks. "
            "Listen to the familiar, deep rhythmic cooing of the blue rock pigeon echoing from rooftop ledges: Gutru-Gu, Gutru-Gu! High in the branches, "
            "the Asian koel sings its melodious rising Ku-oo, Ku-oo, while the coppersmith barbet sounds like a tiny blacksmith striking a metal anvil: "
            "tuk-tuk-tuk! To experience an amazing biological acoustic technique, cup both hands firmly behind your ears with palms facing forward. "
            "Notice how this simple action instantly amplifies faint, distant chirps! Cupping your hands mimics the large external ear flaps, or pinnae, "
            "of mammals like deer, funneling more sound waves directly into your ear canals. You can discern whether a sharp chirp is a joyful mating song "
            "or a frantic alarm whistle warning of a lurking cat or hawk nearby. Bird sounds reveal the hidden life of creatures perched high within leafy foliage, "
            "teaching young scientists that listening attentively is just as powerful as looking when investigating the living natural world all around us."
        ),
        "checkpoints": [
            {
                "question": "What familiar vocalization does the common blue rock pigeon make when calling from ledges and branches?",
                "options": [
                    "Roar-roar like a lion",
                    "Rhythmic, deep cooing sound: 'Gutru-Gu, Gutru-Gu'",
                    "Hiss-hiss like a snake",
                    "Quack-quack like a pond duck"
                ],
                "answer": 1,
                "hint": "Recall the textbook description of the common city and village pigeon.",
                "explanation": "Blue rock pigeons produce a rhythmic, throaty cooing call transcribed in Indian nature lore as 'Gutru-Gu, Gutru-Gu'."
            },
            {
                "question": "How does cupping your hands behind your ears enhance your ability to hear distant bird calls?",
                "options": [
                    "It changes your eye vision to infrared",
                    "It acts like large external ear flaps, funneling more sound waves directly into your ear canals",
                    "It creates electricity in your eardrums",
                    "It makes the birds fly directly into your hands"
                ],
                "answer": 1,
                "hint": "Think about how animal ear flaps gather and direct sound vibrations.",
                "explanation": "Cupping hands behind the ears enlarges the sound-collecting surface area, directing more acoustic vibrations into the ear canal."
            }
        ]
    },
    {
        "id": 15,
        "title": "Dawn Dusk Melodies",
        "subtitle": "Temporal Rhythms: Morning Chorus, Midday Slumber, and Twilight Calls",
        "speech": (
            "If you record bird vocalizations throughout the day, you will discover fascinating temporal patterns synchronized with the sun! "
            "Just before sunrise, as the eastern horizon glows pale pink, the forest erupts in a deafening, joyful symphony known as the dawn chorus. "
            "Magpie robins, bulbuls, mynas, and sunbirds sing their most vigorous songs at daybreak because the morning air is calm and cool, allowing sound "
            "waves to travel much farther with minimal atmospheric distortion. Singing at dawn announces territorial boundaries and confirms survival through "
            "the night before daily foraging begins. By midday, when the blazing sun climbs high and temperatures peak, the woodland falls remarkably silent. "
            "Birds retreat deep into thick, shaded foliage to conserve bodily moisture and avoid dangerous overheating. Then, as twilight paints the evening sky, "
            "a secondary surge of acoustic activity awakens. Flocks of green parakeets and white egrets call noisily as they fly in formation toward communal roosting trees. "
            "As complete darkness descends, nocturnal birds take over: spotted owlets screech softly from tree hollows and nightjars call across open clearings. "
            "Observing these rhythmic shifts across morning, afternoon, and evening reveals how wild creatures synchronize their daily lives with solar cycles, "
            "ambient temperatures, and changing light levels."
        ),
        "checkpoints": [
            {
                "question": "Why do forest birds sing their most energetic songs during the early morning 'dawn chorus'?",
                "options": [
                    "Because they are afraid of the morning sunlight",
                    "Cool, calm morning air carries sound waves farther, and singing establishes territory before daily feeding",
                    "Because all trees are completely asleep at dawn",
                    "To scare away all plant leaves"
                ],
                "answer": 1,
                "hint": "Think about how quiet, still, and cool the air is at first light.",
                "explanation": "At dawn, calm atmospheric conditions enable acoustic signals to travel greater distances, helping birds mark territory and find mates."
            },
            {
                "question": "What do woodland birds typically do during the blazing heat of midday hours?",
                "options": [
                    "They swim to the bottom of the deep ocean",
                    "They retreat into thick, shaded foliage to rest, stay cool, and conserve energy",
                    "They fly up to the moon",
                    "They sing ten times louder than at dawn"
                ],
                "answer": 1,
                "hint": "During the hottest hours, animals seek shaded branches to avoid overheating.",
                "explanation": "During midday heat, birds rest quietly within dense leafy tree canopies to conserve bodily moisture and avoid thermal stress."
            }
        ]
    },
    {
        "id": 16,
        "title": "Caterpillar Butterfly Cycle",
        "subtitle": "Four Stages of Metamorphosis: Egg, Larva, Pupa, and Imago",
        "speech": (
            "Now let us examine one of nature's most enchanting life transformations: the four-stage metamorphosis connecting plants and butterflies! "
            "The journey begins when an adult butterfly deposits tiny, gem-like eggs on the underside of a specific host plant's leaf, such as a lemon "
            "or calotropis bush. Within a few days, the egg hatches into a voracious caterpillar, or larva. Equipped with strong chewing jaws, the caterpillar "
            "munches hungrily on green leaves day and night, molting its skin several times as its body expands rapidly in size. When fully grown, the caterpillar "
            "fastens itself upside-down to a sturdy twig using a silk button and molts into a smooth, stationary shell called a pupa or chrysalis. Inside this "
            "miraculous cocoon-like chamber, dramatic biological remodeling occurs: crawling larval tissues dissolve and reorganize into delicate wings, slender legs, "
            "and compound eyes! Finally, the pupal casing splits open, and a radiant adult butterfly emerges. It pumps vital fluid into its soft, crumpled wings, "
            "dries them in warm sunlight, and flutters away to pollinate flowers and drink sweet nectar. This breathtaking life cycle shows how insects depend "
            "completely on host plants for nursery leaves as caterpillars and floral nectar as butterflies, embodying nature's perpetual renewal across seasons."
        ),
        "checkpoints": [
            {
                "question": "What is the correct sequential order of the four stages in a butterfly's complete metamorphosis?",
                "options": [
                    "Butterfly → Chrysalis → Egg → Caterpillar",
                    "Egg → Caterpillar (Larva) → Chrysalis (Pupa) → Adult Butterfly (Imago)",
                    "Pupa → Egg → Butterfly → Larva",
                    "Caterpillar → Egg → Butterfly → Pupa"
                ],
                "answer": 1,
                "hint": "Start with the tiny egg on the leaf, followed by the hungry crawler, the pupal shell, and the winged adult.",
                "explanation": "The four stages of complete metamorphosis proceed in order: Egg, Larva (Caterpillar), Pupa (Chrysalis), and Adult Butterfly (Imago)."
            },
            {
                "question": "What transformative biological process occurs while the creature rests inside the stationary pupa or chrysalis?",
                "options": [
                    "The caterpillar turns into a stone fossil",
                    "Tissues reorganize, developing wings, antennae, long legs, and compound eyes of the adult butterfly",
                    "The insect shrinks into a tiny mineral rock",
                    "The creature divides into twenty different bees"
                ],
                "answer": 1,
                "hint": "Inside the chrysalis, larval body parts are reorganized into the adult butterfly's body.",
                "explanation": "Inside the chrysalis, complete cellular metamorphosis occurs, transforming caterpillar anatomy into a fully formed winged butterfly."
            }
        ]
    }
]

if __name__ == "__main__":
    import json
    print(f"Part 2 slides count: {len(slides_part2)}")
    assert len(slides_part2) == 8, "Expected exactly 8 slides in Part 2"
    for s in slides_part2:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({tw} words) - Speech: {wc} words")
        assert 1 <= tw <= 3, f"Title length violation on slide {s['id']}: '{s['title']}'"
        assert 195 <= wc <= 215, f"Speech word count violation on slide {s['id']}: {wc} words"
        assert len(s["checkpoints"]) == 2, f"Checkpoints count violation on slide {s['id']}"
    print("Part 2 validation successful!")

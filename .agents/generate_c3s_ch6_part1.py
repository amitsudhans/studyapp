#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 6: Living in Harmony
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- No human character names, no lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Shared Human Homes",
        "subtitle": "Distinguishing Cared Pets from Uninvited Household Visitors",
        "speech": (
            "Welcome, young nature explorers, to our interactive laboratory exploring how humans, plants, and animals live together in peaceful harmony! "
            "When we look around our everyday homes, courtyards, and school buildings, we quickly realize that we do not dwell alone. "
            "Many diverse creatures share our domestic spaces! We can categorize these animal cohabitants into two distinct groups: animals we "
            "intentionally invite and care for, and uninvited wild visitors who make their own homes near us. Domestic pets and farm animals—such "
            "as affectionate dogs, gentle cats, milking cows, and loyal goats—receive daily meals, fresh water, and cozy shelters because humans "
            "care deeply for their welfare. Meanwhile, fascinating uninvited visitors enter our dwellings without any formal invitation! Tiny geckos "
            "scurry across white walls hunting nocturnal moths, house sparrows nest tucked beneath ceiling rafters, industrious black ants march along "
            "kitchen tiles looking for bread crumbs, and colorful pigeons rest on breezy balcony ledges. Understanding these cohabitants teaches us "
            "that our houses form shared mini-ecosystems where diverse creatures seek food, warmth, and shelter. By learning to peacefully share space "
            "with gentle uninvited visitors while caring responsibly for our pets, we cultivate an everyday attitude of respectful coexistence and harmony "
            "right inside our home environments."
        ),
        "checkpoints": [
            {
                "question": "Which of these animals is typically an invited, cared-for domestic companion in human homes?",
                "options": [
                    "A wild wall gecko hunting moths",
                    "A domestic pet dog receiving food and shelter",
                    "A column of black ants marching on tiles",
                    "A mosquito buzzing around the light"
                ],
                "answer": 1,
                "hint": "Think about which animal humans invite into their homes and feed with love.",
                "explanation": "Domestic pets like dogs and cats are cared for intentionally by humans with food, affection, and clean shelter."
            },
            {
                "question": "Why do uninvited creatures like house geckos and sparrows enter human houses?",
                "options": [
                    "To read books in the study room",
                    "To seek shelter, warmth, and food sources like moths and crumbs",
                    "To drive cars along the hallway",
                    "To paint the walls with colors"
                ],
                "answer": 1,
                "hint": "Uninvited animals seek natural resources: insects to eat, warm corners, and safety.",
                "explanation": "Uninvited house visitors seek biological necessities including warmth, roof shelter, and food such as indoor insects and food crumbs."
            }
        ]
    },
    {
        "id": 2,
        "title": "Kindness Toward Creatures",
        "subtitle": "Practicing Everyday Empathy, Care, and Non-Cruelty Ethics",
        "speech": (
            "Now let us examine one of the noblest scientific and human values: extending empathy, gentle care, and kindness to every living organism! "
            "All animals, from tiny crawling beetles to majestic street animals, possess feelings, feel pain when injured, and experience hunger "
            "and thirst during hot summer days. True harmony means treating all living beings with deep compassion, never harming, teasing, "
            "or frightening them unnecessarily. When we spot a stray dog resting quietly in the courtyard shade, we must never throw stones or chase it away in fear; "
            "instead, we can speak gently and provide a clean bowl of fresh drinking water. During scorching summer months, placing an earthen water bowl "
            "on your terrace, balcony, or garden sill saves dozens of dehydrated pigeons, mynas, and honeybees from dangerous heat exhaustion. If an uninvited insect—such as "
            "a wandering beetle or fluttering moth—enters your bedroom, gently guide it into a cardboard cup and release it safely outdoors into the garden "
            "rather than crushing it. Unless a dangerous creature poses an immediate threat, non-violence, mindful patience, and respectful care are our best guides. "
            "Practicing everyday kindness fosters emotional empathy, strengthens civic responsibility, and connects us intimately to the vast living family "
            "of nature that surrounds us all across our shared planet."
        ),
        "checkpoints": [
            {
                "question": "What is the most compassionate action when finding a dehydrated bird on a hot summer terrace?",
                "options": [
                    "Chasing the bird away with a broomstick",
                    "Providing a shallow earthen bowl of clean drinking water in the shade",
                    "Trapping the bird inside a dark metal box",
                    "Sprinkling hot salt on its wings"
                ],
                "answer": 1,
                "hint": "Birds need safe hydration and cool shade when temperatures soar in summer.",
                "explanation": "Placing shallow earthen water bowls in shaded outdoor spaces provides vital life-saving hydration for birds and urban wildlife."
            },
            {
                "question": "How should a young nature explorer handle a wandering moth or beetle trapped inside a room?",
                "options": [
                    "Gently capture it in a cup and release it safely outdoors in the garden",
                    "Crush it immediately with a heavy shoe",
                    "Spray it with harmful toxic chemicals",
                    "Lock the door and run away forever"
                ],
                "answer": 0,
                "hint": "Gentle catch-and-release allows the harmless creature to return to its outdoor habitat safely.",
                "explanation": "Using a cup and card to safely transport wandering insects outdoors preserves living creatures without resorting to unnecessary cruelty."
            }
        ]
    },
    {
        "id": 3,
        "title": "Mango Tree Secrets",
        "subtitle": "Observing Nature's Wisdom Beneath a Shady Orchard Canopy",
        "speech": (
            "Imagine resting beneath the cool, leafy boughs of a grand old mango tree during a warm golden afternoon in the peaceful countryside! "
            "As an observant child sits peacefully with an elder in the orchard shade, the canopy above buzzes with vibrant ecological activity. "
            "High among the thick foliage, an agile monkey plucks a luscious, ripe golden mango. The monkey carefully peels the sweet skin, savors "
            "the succulent yellow pulp, and then casually drops the large, fibrous seed core onto the fertile soil below. Looking at the discarded seed "
            "resting in the dust, the curious child wonders: has the monkey wasted the fruit, or is something wonderful about to happen? The wise elder "
            "explains that this simple everyday act represents nature's brilliant mutual partnership between animals and trees! The mango tree cannot walk "
            "across open fields to plant its own children; instead, it sweetens its fruit to entice hungry monkeys, birds, and fruit bats. By feeding the monkey, "
            "the tree ensures its seed travels away from its parent canopy, where it will receive fresh sunlight, soil nutrients, and rain to sprout into a brand-new "
            "mango sapling. Observing this living interaction reveals how natural partnerships keep wild forests continuously thriving without any artificial machinery."
        ),
        "checkpoints": [
            {
                "question": "Why does a mango tree produce sweet, succulent fruits for animals to eat?",
                "options": [
                    "To poison forest creatures so they cannot climb branches",
                    "To entice animals to eat the pulp and transport seeds away to sprout in new locations",
                    "Because mango trees cannot absorb rainwater without monkeys",
                    "To make the forest floor slippery"
                ],
                "answer": 1,
                "hint": "Trees reward fruit-eaters with tasty food so animals carry seeds to distant sunny soil.",
                "explanation": "Plants produce nutritious, sweet fruits as an evolutionary strategy to reward animals that disperse their seeds far from the parent tree."
            },
            {
                "question": "What happens to the discarded mango seed when it lands on moist, fertile soil?",
                "options": [
                    "It turns into hard solid gold",
                    "It absorbs moisture and germinates into a brand-new mango sapling",
                    "It dissolves completely into air within one second",
                    "It prevents all other plants from ever growing"
                ],
                "answer": 1,
                "hint": "Under the right conditions of water, soil, and warmth, the seed embryo wakes up.",
                "explanation": "A discarded seed absorbs soil moisture and nutrients, germinating into roots and a green shoot to become a new mango tree."
            }
        ]
    },
    {
        "id": 4,
        "title": "Seed Germination Cycles",
        "subtitle": "How Embryonic Seeds Transform into Mighty Woodland Trees",
        "speech": (
            "Let us investigate the botanical marvel hidden inside every single plant seed: the wondrous developmental process of seed germination! "
            "A seed may appear dry, hard, and inactive like a tiny pebble, but inside lies a sleeping baby plant called an embryo, accompanied by a pantry "
            "of stored food called cotyledons. For this sleeping seed to awaken, nature must provide three essential triggers: moisture from rain, "
            "warmth from gentle sunlight, and oxygen from aerated soil pores. When a discarded mango or neem seed absorbs groundwater, its tough protective "
            "outer coat softens and cracks open. First, a tiny white embryonic root called a radicle emerges, anchoring deep into the subterranean soil "
            "to absorb dissolved minerals and fresh water. Shortly after, a tender green shoot called a plumule pushes upward toward the sky, unfolding its first "
            "pair of baby leaves. As soon as these green leaves catch golden sunlight, they begin photosynthesis, producing energy independently and vigorously. "
            "Over years of seasonal monsoon rains, this fragile seedling grows a sturdy wooden trunk, spreads thick branches, and produces fragrant blossoms "
            "of its own. Every towering banyan, mango, or peepal tree began its journey as a humble seed nurtured by soil, rain, and animal dispersal."
        ),
        "checkpoints": [
            {
                "question": "What three environmental conditions are essential for a dormant seed to germinate?",
                "options": [
                    "Plastic wrapping, darkness, and ice cubes",
                    "Moisture (water), gentle warmth (sunlight), and oxygen (air)",
                    "Chemical paint, gasoline, and loud music",
                    "Solid concrete, salt, and fire"
                ],
                "answer": 1,
                "hint": "Think about what a farmer gives to seeds planted in a vegetable bed.",
                "explanation": "Seeds require moisture to soften the coat, warmth to activate enzymes, and oxygen for cellular respiration to germinate successfully."
            },
            {
                "question": "Which plant part emerges first from a germinating seed to anchor into the soil?",
                "options": [
                    "A broad wooden branch",
                    "The embryonic root (radicle) that grows downward to absorb water",
                    "A cluster of red ripe fruits",
                    "A flock of flying birds"
                ],
                "answer": 1,
                "hint": "The downward-growing root establishes a stable anchor and absorbs soil moisture first.",
                "explanation": "The radicle (embryonic root) is the first organ to push out, anchoring the seedling and absorbing vital soil moisture and minerals."
            }
        ]
    },
    {
        "id": 5,
        "title": "Bountiful Plant Gifts",
        "subtitle": "Vital Human and Animal Reliance on Botanical Resources",
        "speech": (
            "Take a deep breath of fresh morning air and look around you to appreciate the endless, generous bounties we receive from plants! "
            "Without plants, complex animal and human life could not survive on Earth for even a single day. First and foremost, green plants generate "
            "the very oxygen gas we inhale with every breath through the magic of photosynthesis, while purifying the atmosphere by absorbing carbon dioxide. "
            "Every meal on our family dining table traces back directly to plants: wholesome grains like wheat and rice, protein-rich lentils, succulent "
            "vegetables, crunchy nuts, and sweet seasonal fruits. Beyond nourishing our bodies, plants furnish sturdy timber for building cozy houses, "
            "wooden tables, chairs, and school desks. Plant fibers provide soft cotton for our summer clothes and strong jute for sturdy shopping bags. "
            "Ancient healing traditions and modern pharmacies depend on medicinal plants like tulsi, neem, and ginger to cure stubborn coughs, heal skin "
            "wounds, and soothe fevers. Furthermore, dense tree roots bind topsoil tightly, preventing monsoon floods from washing away fertile agricultural "
            "land into rivers. From the clean air filling our lungs to the clothes on our backs, plants provide the indispensable foundation of all life on Earth."
        ),
        "checkpoints": [
            {
                "question": "What vital gas do green plants release into the atmosphere during photosynthesis?",
                "options": [
                    "Poisonous smoke",
                    "Life-sustaining oxygen gas inhaled by humans and animals",
                    "Pure liquid iron",
                    "Heavy mineral oil"
                ],
                "answer": 1,
                "hint": "This invisible gas is what our lungs take in with every refreshing breath.",
                "explanation": "Through photosynthesis, green plants convert sunlight and carbon dioxide into sugars, releasing vital oxygen gas into the atmosphere."
            },
            {
                "question": "Which of these everyday household items is made directly from botanical plant fibers?",
                "options": [
                    "A glass drinking tumbler",
                    "A soft cotton shirt and sturdy woven jute shopping bag",
                    "An iron kitchen frying pan",
                    "A clay cooking pot"
                ],
                "answer": 1,
                "hint": "Cotton comes from cotton plant seed bolls and jute comes from the stems of jute plants.",
                "explanation": "Cotton garments and jute bags are crafted from plant fibers harvested directly from agricultural crops."
            }
        ]
    },
    {
        "id": 6,
        "title": "Tree Canopy Shelter",
        "subtitle": "Living Multistory Sanctuaries for Birds, Bats, and Forest Mammals",
        "speech": (
            "Beyond providing timber, sweet fruit, and fresh air, living trees serve as expansive, elevated multistory apartment buildings for wildlife! "
            "When you gaze up into a sprawling neem, peepal, or banyan tree, you are looking at dozens of distinct animal residences stacked safely "
            "above the ground. Dense canopy foliage creates an insulating umbrella of cool green shade, dropping temperatures beneath the branches "
            "by several degrees during blistering summer afternoons. Small songbirds—such as bulbuls, tailorbirds, and sunbirds—weave intricate nests "
            "among fork branches, keeping fragile eggs and defenseless hatchlings out of reach from prowling ground predators like snakes and stray cats. "
            "Tree hollows in older trunks offer snug, dry wooden bedrooms for striped palm squirrels, roosting spotted owlets, and coppersmith barbets. "
            "High horizontal branches serve as comfortable resting lounges for leopards in dense forests, while colonies of fruit bats hang upside-down "
            "wrapped in leathery wings during bright daylight hours. Even the rough bark provides safe crevices where geckos, spiders, and beetles sleep securely "
            "away from harm. When fierce monsoon downpours arrive, interlocking leaves act like thatched roofs, sheltering tired birds from driving raindrops. "
            "A single mature forest tree proves to be a bustling, life-protecting sanctuary that shelters countless wild creatures in enduring safety."
        ),
        "checkpoints": [
            {
                "question": "How do tree canopies protect nesting birds and small mammals during scorching summer weather?",
                "options": [
                    "By turning branches into solid blocks of ice",
                    "By creating a broad umbrella of cool shade that significantly lowers ambient temperature",
                    "By blowing electric air conditioning through the leaves",
                    "By making the tree invisible to the sun"
                ],
                "answer": 1,
                "hint": "The thick leaf canopy blocks direct solar rays, creating a cooler microclimate beneath.",
                "explanation": "Dense tree canopies block harsh solar radiation and transpire moisture, significantly cooling the surrounding air for roosting wildlife."
            },
            {
                "question": "Why do birds prefer building nests high up in branch forks rather than on the flat ground?",
                "options": [
                    "Because birds cannot walk on the ground",
                    "To safeguard vulnerable eggs and hatchlings from ground-dwelling predators like snakes and dogs",
                    "To catch flying clouds with their beaks",
                    "Because tree branches are made of sweet sugar"
                ],
                "answer": 1,
                "hint": "Elevated branches keep fragile nests out of reach of animals walking along the forest floor.",
                "explanation": "Elevated nesting provides critical defense against ground predators, keeping eggs and defenseless baby chicks secure."
            }
        ]
    },
    {
        "id": 7,
        "title": "Forest Tree Planters",
        "subtitle": "Unintentional Arborists: How Squirrels and Birds Regenerate Forests",
        "speech": (
            "Did you know that many of the magnificent woodlands and fruit orchards around us were planted unintentionally by busy little animals? "
            "Among all woodland creatures, the energetic striped squirrel is one of nature's most prolific and successful tree planters! When autumn arrives, "
            "squirrels scurry through gardens gathering thousands of acorns, walnuts, and wild seeds to store for winter when food becomes scarce. The agile squirrel "
            "digs small holes in moist soil, buries the seeds safely underground, and pats the crumbly earth down. But here is the miraculous biological twist: "
            "squirrels have so many secret hiding spots that they forget the exact location of thousands of buried nuts! Come springtime, soaking rain filters "
            "into the forgotten seeds, and they sprout into vigorous green saplings. Birds are equally talented and tireless forest planters! Frugivorous birds "
            "like hornbills, bulbuls, and parakeets feast on wild figs, berries, and neem fruits. Because the internal seeds are tough and indigestible, they "
            "pass unharmed through avian digestive systems, landing miles away encased in natural fertilizer droppings. Without human gardeners planting saplings, "
            "wild animals quietly plant millions of new trees every year, ensuring the eternal regeneration of our planet's green forests across generations."
        ),
        "checkpoints": [
            {
                "question": "How do forgetful squirrels accidentally help plant thousands of new trees every year?",
                "options": [
                    "They buy seeds from farmers using money",
                    "They bury nuts and seeds in moist soil as winter stores and forget where many are hidden, allowing them to sprout",
                    "They carry watering cans to irrigate flower beds",
                    "They dig up living trees and move them to new forests"
                ],
                "answer": 1,
                "hint": "Seeds buried underground and forgotten by squirrels find ideal conditions to sprout in spring.",
                "explanation": "Squirrels cache seeds in subterranean holes for winter; forgotten seeds germinate with spring rains, regenerating woodland canopies."
            },
            {
                "question": "How do fruit-eating birds like bulbuls and hornbills disperse plant seeds across distant landscapes?",
                "options": [
                    "They mail seeds in paper envelopes",
                    "They swallow wild fruits and excrete viable seeds in fertilizer droppings miles away from parent trees",
                    "They bury seeds in deep ocean trenches",
                    "They burn the seeds with fire"
                ],
                "answer": 1,
                "hint": "The flesh is digested, but the hard seed passes through and lands far away with natural manure.",
                "explanation": "Hard seeds pass undamaged through bird digestive systems, falling in nutrient-rich droppings across wide landscapes to sprout."
            }
        ]
    },
    {
        "id": 8,
        "title": "Fertilizing Organic Waste",
        "subtitle": "Natural Nutrient Recycling: Dung, Droppings, and Vermicompost",
        "speech": (
            "In nature's marvelous zero-waste economy, what one organism discards becomes the life-giving treasure of another living creature! "
            "When domestic cows, wild elephants, or grazing goats drop organic manure onto the earth, they are not creating useless filth; they are returning "
            "vital minerals back to the living soil. Herbivore manure is exceptionally rich in organic plant fibers, nitrogen, potassium, and phosphorus that "
            "neighboring plants eagerly absorb through their roots to grow lush green leaves. Immediately after manure lands on the ground, industrious dung "
            "beetles arrive to roll the waste into neat spheres, burying it beneath the surface as food for their larvae. This burying behavior naturally aerates "
            "compacted earth and injects nutrients deep into root zones. Meanwhile, millions of subterranean earthworms feast on decaying plant litter and dung, "
            "processing organic waste into exquisite, nutrient-packed vermicompost castings. In traditional Indian farming, cow dung and dried neem leaves have "
            "been used for thousands of years as natural, chemical-free fertilizers that keep agricultural soils healthy, moist, dark, and fertile across generations. "
            "By recycling natural animal waste back into bioavailable plant nutrients, nature maintains an unbroken circular cycle of renewed life without "
            "generating any harmful environmental pollution, toxic residue, or wasteful discarded byproducts."
        ),
        "checkpoints": [
            {
                "question": "What happens to animal dung when it is broken down naturally in garden soil?",
                "options": [
                    "It turns into poisonous plastic that kills earthworms",
                    "It enriches soil with nitrogen, phosphorus, and organic humus that nourish growing plant roots",
                    "It dissolves all water out of the ground",
                    "It turns the surrounding air into solid ice"
                ],
                "answer": 1,
                "hint": "Manure contains essential plant nutrients that restore soil fertility naturally.",
                "explanation": "Animal waste decomposes into organic humus rich in nitrogen and minerals, functioning as natural fertilizer for thriving vegetation."
            },
            {
                "question": "How do dung beetles assist both soil health and plant growth on the forest floor?",
                "options": [
                    "They cut down green trees with their horns",
                    "They roll and bury dung underground, aerating soil and delivering organic nutrients directly to root zones",
                    "They steal seeds from bird nests",
                    "They freeze the soil during summer"
                ],
                "answer": 1,
                "hint": "Burying dung moves organic nutrients beneath the surface where plant roots can reach them.",
                "explanation": "Dung beetles bury organic manure underground to feed their larvae, which aerates the soil and deposits nutrients directly near plant roots."
            }
        ]
    }
]

if __name__ == "__main__":
    import json
    print(f"Part 1 slides count: {len(slides_part1)}")
    assert len(slides_part1) == 8, "Expected exactly 8 slides in Part 1"
    for s in slides_part1:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({tw} words) - Speech: {wc} words")
        assert 1 <= tw <= 3, f"Title length violation on slide {s['id']}: '{s['title']}'"
        assert 195 <= wc <= 215, f"Speech word count violation on slide {s['id']}: {wc} words"
        assert len(s["checkpoints"]) == 2, f"Checkpoints count violation on slide {s['id']}"
    print("Part 1 validation successful!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 11: Making Things
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- No human character names (Appooppan, Ammu, Khushi, Moyna, Dadu, Harpreet, Raghav, Shirin, etc.), no lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Preparing Potter Clay",
        "subtitle": "Wetting, Pounding, and Kneading Smooth Earth Soil Like Soft Dough",
        "speech": (
            "Welcome, curious young builders, to our fascinating journey into how skilled human hands transform simple raw earth into beautiful pots, "
            "bricks, and lasting homes! Visit a peaceful countryside pottery workshop where an elder grandfather potter and a skilled mother potter work "
            "side by side like dedicated material scientists! Can a potter scoop up dry crumbly garden dirt and instantaneously spin a tall sturdy matka "
            "pot? Never! Great pottery starts slowly with patient clay preparation! First, the elder potter gathers fine, silky soil from calm riverbeds "
            "and clears out tiny pebbles, dry twigs, and hard root fragments cleanly. Next comes careful wetting and pounding: pouring measured clean "
            "water onto dry dusty clay and pounding lumps gently using wooden mallets until every stubborn clump softens thoroughly! Then comes the most "
            "important step—kneading wet clay vigorously with strong rhythmic palms exactly like preparing smooth wheat chapati dough! Why does kneading "
            "matter so much scientifically? Thorough kneading squeezes out sneaky hidden air bubbles inside clay lumps—because trapped air pockets expand "
            "violently inside blazing brick kilns later and crack finished soft pots apart! Preparing silky, uniform, bubble-free clay dough turns ordinary damp earth into a magical elastic "
            "sculpting medium ready for fast spinning potter wheels!"
        ),
        "checkpoints": [
            {
                "question": "Why must a potter carefully remove tiny stones and vigorously knead wet clay like soft bread dough before shaping pots?",
                "options": [
                    "Kneading squeezes out trapped air bubbles and stones that would crack pots open when baked inside hot kilns",
                    "Because kneading turns brown clay into transparent glass windows immediately",
                    "So pots dissolve cleanly when touched by raindrops",
                    "Because pebbles make clay float upward into sky clouds"
                ],
                "answer": 0,
                "hint": "Think about what trapped air pockets inside hot ovens do to clay walls!",
                "explanation": "Thorough pounding, stone removal, and kneading create uniform, air-bubble-free clay so vessels shape evenly and survive intense kiln heat."
            },
            {
                "question": "Which kitchen preparation step closely resembles how potters press and fold wet clay with their palms?",
                "options": [
                    "Boiling dry pasta inside salted water",
                    "Kneading soft wheat flour dough smoothly before rolling chapatis",
                    "Slicing fresh watermelon wedges with knives",
                    "Freezing sweet milk into cold ice pops"
                ],
                "answer": 1,
                "hint": "Think of soft sticky flour mixed with water and pressed smoothly by hands!",
                "explanation": "Potters knead moist clay systematically with heel-of-hand pressure just like bakers knead chapati dough to achieve smooth elasticity."
            }
        ]
    },
    {
        "id": 2,
        "title": "Spinning Stone Wheel",
        "subtitle": "Shaping Balanced Circular Earthen Vessels on a Potter's Wheel",
        "speech": (
            "Step closer beside the heavy flat circular stone disc resting evenly above a shallow courtyard pit—watch the spinning magic of a traditional "
            "Indian potter's wheel! First, the elder potter drops a smooth, moist ball of kneaded clay squarely onto the exact dead center of the round "
            "stone disc. Next, inserting a strong wooden stick inside a rim notch, the potter spins the heavy stone wheel briskly until smooth rotational "
            "momentum keeps it gliding effortlessly round and round like a giant spinning top! Now watch gentle wet hands perform astonishing circular "
            "physics! Pressing moistened thumbs softly down into the rotating center opens a smooth hollow cavity, while steady outer palms guide soft "
            "spinning clay walls gently upward and outward—transforming one shapeless mound within minutes into a graceful cooling water matka, tiny "
            "tea kulhad, festive earthen diya lamp, or tall curved surahi! Keeping hands freshly dampened with cool water prevents friction from tearing "
            "spinning soft clay walls! Finally, a taut thin wire string slices cleanly beneath the pot's flat base, lifting the finished green vessel gently onto "
            "clean sun-drenched wooden drying planks gently and safely without ever squishing, stretching, or distorting its flawless smooth symmetrical round circle even slightly!"
        ),
        "checkpoints": [
            {
                "question": "Why does a traditional potter insert a wooden stick to spin a heavy stone wheel briskly before shaping wet clay?",
                "options": [
                    "Steady circular rotation helps wet hands shape perfectly round, even, symmetrical pot walls swiftly",
                    "Because spinning wheels freeze wet mud into blue ice",
                    "To launch finished clay bowls thirty feet upward into tree branches",
                    "Because clay refuses to stick onto stone unless vibrating randomly"
                ],
                "answer": 0,
                "hint": "Notice how every point around a spinning pot moves evenly past steady palms!",
                "explanation": "Uniform rotational momentum on a heavy stone wheel allows artisans to draw symmetrical hollow circular vessels smoothly."
            },
            {
                "question": "What clever simple tool slices cleanly underneath a newly shaped wet pot to lift it gently off the potter's wheel?",
                "options": [
                    "A heavy steel axe",
                    "A taut thin cotton or metal wire string slid flat across the wheel surface",
                    "A big wooden hammer struck from above",
                    "Boiling hot cooking oil poured over top"
                ],
                "answer": 1,
                "hint": "Pulling a thin tight thread straight across the base releases soft pots without squishing sides!",
                "explanation": "Sliding a taut thin wire/string flat under the base separates wet clay cleanly from the stone wheel without deforming soft rims."
            }
        ]
    },
    {
        "id": 3,
        "title": "Drying And Kilns",
        "subtitle": "Sun-Drying Shaped Clay and Baking Strong Pots Inside Hot Kilns",
        "speech": (
            "Suppose a freshly shaped wet clay cup sits softly atop a sunlit veranda shelf—what happens if someone immediately fills that unbaked raw "
            "cup with fresh drinking water? Within minutes, raw dried mud softens right back into squishy mud puddles and collapses! To turn fragile "
            "molded earth into strong, lasting, water-holding vessels, two vital drying and firing steps remain! First, neatly arranged newly spun pots "
            "rest calmly outdoors beneath warm golden sunshine and gentle breezes for several days until remaining moisture evaporates cleanly, turning "
            "soft damp clay firm and chalky 'bone-dry'! Second, the skilled mother potter stacks dozens of sun-dried vessels carefully inside a specialized "
            "domed high-heat oven called a KILN! Packed around dried firewood, rice husks, or fuel embers and sealed snugly beneath insulating ash layers, "
            "blazing kiln temperatures soar beyond eight hundred degrees Celsius! Intense radiant fire permanently fuses microscopic clay minerals together—"
            "converting soft dry mud chemically into tough, resonant reddish-orange terracotta ceramic! Once cooled slowly inside the closed kiln, finished pots "
            "ring clearly with resonant chime notes when tapped lightly, never dissolve back into soft mud when washed thoroughly with fresh water, and faithfully chill cool drinking water through entire scorching Indian summers!"
        ),
        "checkpoints": [
            {
                "question": "What happens if someone fills an unbaked, sun-dried clay cup directly with drinking water before baking it in a kiln?",
                "options": [
                    "The unbaked clay softens swiftly back into squishy wet mud and crumbles apart",
                    "Unbaked dry clay immediately glows bright neon purple",
                    "Water turns automatically into sweet solid jaggery",
                    "The raw clay cup rings louder than brass temple bells"
                ],
                "answer": 0,
                "hint": "Only intense kiln heat permanently fuses mineral clay grains waterproof against softening!",
                "explanation": "Sun-dried raw clay merely loses water temporarily; firing in a kiln chemically bonds clay particles into durable ceramic."
            },
            {
                "question": "What special high-temperature oven do potters use to bake sun-dried clay vessels hard and lasting?",
                "options": [
                    "An electric ice refrigerator",
                    "A kiln",
                    "A wooden wheat flour sieve",
                    "A plastic rainwater bucket"
                ],
                "answer": 1,
                "hint": "It rhymes with 'milk'—almost! Starts with K: K _ _ _.",
                "explanation": "A kiln is an insulated high-heat oven reaching 800°C+ to harden molded clay pots and bricks into permanent ceramic."
            }
        ]
    },
    {
        "id": 4,
        "title": "Sieving Clay Craft",
        "subtitle": "Purifying Garden Soil With Water Sedimentation for Classroom Sculpting",
        "speech": (
            "Ready to craft your very own custom miniature earthen bowls, tiny play animals, and festive diyas during Activity 1 and Activity 2? Even "
            "without living beside a river clay pit, clever third-grade young potters can purify ordinary garden soil cleanly using simple separation "
            "science! Gather two handfuls of dry crumbly garden soil, a wide metal mesh strainer sieve, a tall clear glass jar of clean water, and flat "
            "sunlit drying boards! Step one: shake dry crushed soil gently through your wire kitchen sieve to separate out large gravel stones, dry twig "
            "splinters, and hard leaves cleanly. Step two: stir the sifted fine powder thoroughly inside a clear jar filled with water! Watch carefully "
            "what gravity accomplishes over twenty calm minutes: coarse gritty sand drops rapidly to the bottom first, floating leaf chaff skims cleanly "
            "off the top, and ultra-fine silky clay settles slowly as a velvety top mud layer! Pour off excess clear water carefully, scoop out that "
            "silky settled clay paste onto soft cotton cloth to blot excess dampness, knead smoothly with palms until completely non-sticky, sculpt imaginative bowls, cups, or tiny playful animal figurines "
            "with damp fingertips, and dry them cleanly inside warm afternoon sunshine!"
        ),
        "checkpoints": [
            {
                "question": "Why do students pass dry garden soil through a wire mesh sieve before mixing water for clay craft in Activity 2?",
                "options": [
                    "To filter out sharp gravel pebbles, hard roots, and dry twigs so sculpted clay stays smooth and crack-free",
                    "Because metal sieves turn mud bright rainbow pink instantly",
                    "To make clay evaporate completely into invisible sky gas",
                    "So heavy gravel stones float atop pure water"
                ],
                "answer": 0,
                "hint": "Think about sharp stones scratching your fingertips or spoiling smooth models!",
                "explanation": "Sieving separates coarse pebbles and plant debris cleanly, leaving fine powder ideal for velvety sculpting clay."
            },
            {
                "question": "When sifted soil rests undisturbed inside a jar of clean water, which particles settle rapidly to the very bottom first?",
                "options": [
                    "Lightweight floating dry leaf pieces",
                    "Heavier coarse gritty sand grains, leaving fine smooth clay settling atop them",
                    "Clear drinking water bubbles",
                    "Tiny colorful flower petals"
                ],
                "answer": 1,
                "hint": "Gravity pulls heavier, larger gritty particles downward fastest!",
                "explanation": "Heavier sand sinks first (sedimentation), allowing silky ultra-fine clay particles to settle cleanly as a smooth workable top sediment layer."
            }
        ]
    },
    {
        "id": 5,
        "title": "Visiting Local Potters",
        "subtitle": "Observing Artisan Tools, Diverse Earthen Items, and Respecting Craftsmanship",
        "speech": (
            "Stepping politely inside a local village potter's courtyard during Activity 1 opens young eyes to extraordinary living heritage and tireless "
            "skilled artistry! Look attentively around rows of freshly baked terracotta treasures gleaming warmly under shaded bamboo awnings! Notice how "
            "many everyday useful objects spring gracefully from clever clay wheels: wide-bellied cooling water matkas, graceful spouted tea kulhads "
            "saving forests from disposable plastic foam cups, tiny shallow oil diyas illuminating joyful festivals, sturdy terracotta flowerpots breathing "
            "moisture cleanly around plant roots, slotted money-saving earthen piggy banks (gullaks), and sizzling baked tandoor cooking tandoors! Watch "
            "the potter wield humble yet ingenious hand tools too—wooden shaping paddles tapping pot curves thin and uniform, round river pebbles held "
            "steady inside as anvils, thin cutting wires, and soft damp cloth strips smoothing spinning lips cleanly! Always greet artisans warmly with "
            "respect, ask thoughtful curious questions about how many careful hours preparing clay, spinning wheels, and firing hot kilns require daily, and never touch or squeeze delicate unbaked sun-drying "
            "greenware clay pots carelessly before final brick kiln baking—discovering deep warm personal gratitude for tireless traditional handmade Indian village pottery crafts sustaining rural artisan families, creative cultural heritage, and healthy Earth soil everywhere cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Why is drinking warm tea or lassi out of disposable earthen clay kulhads friendlier to Earth than single-use plastic foam cups?",
                "options": [
                    "Clay kulhads come from pure natural soil and crush harmlessly back into earth without polluting rivers for centuries",
                    "Because plastic foam cups grow mango orchards automatically",
                    "Because clay cups fly away smoothly on windy afternoons",
                    "Because plastic cups chill boiling water instantaneously"
                ],
                "answer": 0,
                "hint": "Think about landfill pollution and biodegradable natural clay earth!",
                "explanation": "Fired unglazed clay kulhads break back down harmlessly into mineral soil particles, preventing stubborn toxic plastic waste."
            },
            {
                "question": "Why must visitors at a potter's drying yard avoid touching unbaked 'greenware' pots resting in sunshine before kiln firing?",
                "options": [
                    "Unbaked bone-dry clay is super fragile and brittle, snapping or chipping easily before baking hardens it",
                    "Because unbaked green clay burns fingers at 900 degrees",
                    "Because greenware pots ring too loudly when touched",
                    "Because touching raw pots turns sunlight permanently dark blue"
                ],
                "answer": 0,
                "hint": "Remember dry unbaked mud has zero ceramic strength yet!",
                "explanation": "Before high-temperature kiln firing fuses mineral particles, dry clay objects are exceedingly brittle and easily damaged."
            }
        ]
    },
    {
        "id": 6,
        "title": "Neem Branch Patterns",
        "subtitle": "Spotting Repeating Rhythmic Geometry Along Leaves and Natural Forms",
        "speech": (
            "Step away gently from pottery workshops into a breezy sunlit green garden—and examine one simple plucked neem twig closely like both "
            "a sharp scientist AND an imaginative artist! Look along the slender green central midrib stem of a compound neem leaf: notice how curved, "
            "serrated emerald leaflets sprout cleanly in neat, balanced, repeating pairs marching smoothly upward from base to tip? That pleasing, "
            "organized repetition of shapes, lines, curves, or angles is what scientists and designers celebrate as a PATTERN! Gaze closer across the "
            "garden to uncover natural patterns hiding right before your eyes everywhere! Hold a wide hibiscus or peepal leaf upward toward sunshine: "
            "branching thin veins fork repeatedly outward like miniature river maps carrying clean water to every cell! Look downward inside golden "
            "sunflower centers to spot spiraling seed rows curling mathematically outward, examine symmetrical five-petal floral stars, inspect stacked "
            "woody pinecones, and trace neat concentric annual growth rings inside fallen wooden tree trunks! Discovering repeating rhythm, order, and mathematical symmetry inside living green "
            "neem branches sparks deep joyful visual inspiration for traditional human painting art, woven cotton textiles, hand-carved wooden temple doors, embroidered scarves, and colorful decorated household pottery across every village!"
        ),
        "checkpoints": [
            {
                "question": "What pleasing repeating feature makes a neem twig an inspiring example of a natural pattern?",
                "options": [
                    "Curved serrated green leaflets grow neatly in balanced matching pairs along both sides of the central twig stem",
                    "Neem twigs sprout random square bricks and metal screws",
                    "Every single neem leaf grows strictly upside down in circles",
                    "Because neem twigs have zero leaves during sunny months"
                ],
                "answer": 0,
                "hint": "Trace left and right along a compound neem stem from bottom to top!",
                "explanation": "Repeated symmetrical pairs of serrated leaflets marching rhythmically along the twig form a classic botanical pattern."
            },
            {
                "question": "Which other plant structure displays clear mathematical repeating natural patterns?",
                "options": [
                    "Spiral seed rows inside sunflowers, branching leaf veins, and concentric wooden tree rings",
                    "Broken shards of plastic soda bottles dumped in trenches",
                    "Random piles of torn grey cardboard boxes",
                    "Crushed spilled salt piles on asphalt roads"
                ],
                "answer": 0,
                "hint": "Look for spirals, branching networks, and symmetric petals crafted by growing plants!",
                "explanation": "Sunflowers, tree rings, pinecones, and branching leaf veins exhibit orderly self-repeating botanical geometry."
            }
        ]
    },
    {
        "id": 7,
        "title": "Wildlife Body Patterns",
        "subtitle": "Exploring Stripes, Rosettes, Eye-Spots, and Wing Symmetry on Animals",
        "speech": (
            "Plant twigs are only half of nature's breathtaking art studio—now look carefully at wild creatures roaming grasslands, forests, and sunny "
            "flower gardens! Animals carry astonishing geometric body patterns painted cleanly upon fur coats, shimmering plumes, and delicate wings! "
            "Inspect five famous patterned wildlife marvels highlighted right inside Chapter 11! Marvel one: tall African zebras display crisp bold "
            "black-and-white vertical stripes—confusing chasing predators when herds gallop swiftly together! Marvel two: majestic royal Bengal tigers "
            "wear dramatic dark vertical stripes across fiery golden fur, blending invisibly amid tall dappled bamboo grass shadows! Marvel three: agile "
            "leopards showcase clustered ring-like dark blotches called rosettes helping them vanish high upon leafy tree branches! Marvel four: India's "
            "radiant national bird, the dancing peacock, fans colossal emerald tail plumes adorned with iridescent sapphire eye-spots! Finally, inspect "
            "colorful garden butterflies resting gently atop bright red marigolds: their left and right painted wings mirror each other in flawless exact bilateral mirror "
            "symmetry! Nature brilliantly crafts repeating vertical stripes, clustered fur spots, vivid bright plumage rings, and balanced mirror patterns across living wild animals both to camouflage gentle creatures safely from dangerous predators and to attract amazed admiring human eyes everywhere across open nature!"
        ),
        "checkpoints": [
            {
                "question": "How do dramatic dark stripes across a tiger's golden coat or leopard's spotted rosettes help wild big cats survive safely?",
                "options": [
                    "They provide natural camouflage breaking up body outlines amid tall grass and speckled forest shadows",
                    "Because stripes turn big cats bright neon invisible at noon sky",
                    "So tigers can shine brighter than fire engines in open plains",
                    "Spots allow leopards to float underwater like balloons"
                ],
                "answer": 0,
                "hint": "When sunlight filters through tall bamboo stalks and leaves, shadows form striped and dappled patches!",
                "explanation": "Stripes and rosettes mimic dappled sunlight and tall grass shadows, camouflaging predators effectively while hunting."
            },
            {
                "question": "Which natural pattern accurately matches each Chapter 11 wild animal?",
                "options": [
                    "Tiger & Zebra = Bold Stripes; Leopard = Rosette Spots; Peacock = Iridescent Eye-Spots; Butterfly = Symmetrical Wings",
                    "Zebra = Solid Blue Scales; Peacock = Muddy Grey Fur; Butterfly = Four-Legged Claws",
                    "Leopard = Green Bark Leaves; Tiger = Red Brick Squares",
                    "Peacock = Transparent Plastic Feathers; Zebra = Spiral Shell"
                ],
                "answer": 0,
                "hint": "Check each creature's signature coat, feather, or wing markings carefully!",
                "explanation": "Tigers and zebras feature stripes, leopards wear rosette spots, peacocks boast iridescent eye-spots, and butterflies display mirror-symmetric wings."
            }
        ]
    },
    {
        "id": 8,
        "title": "Decorating Indian Pottery",
        "subtitle": "Painting Botanical Leaf Motifs and Geometric Bands on Traditional Pots",
        "speech": (
            "Now bring nature's wondrous neem twigs, peacock eye-spots, and rippling river waves straight back into the cozy village pottery studio during "
            "Activity 4! Across every Indian state for thousands of years—from ancient Harappan painted jars to vibrant Rajasthani, Gujarati, Bengali, "
            "and Manipuri pottery—artists have decorated rounded earthen water pots with nature-inspired repeating patterns! Look closely at how a potter "
            "transforms a plain terracotta pot into a prized work of cultural art! Before firing inside the kiln, skilled artisans spin the leather-hard "
            "pot slowly upon the wheel while touching natural mineral-clay paint brushes cleanly against spinning curves—instantly sweeping flawless "
            "crisp horizontal bands right around pot shoulders! Next, slender bamboo brushes dip gently into chalky white, charcoal black, and warm red "
            "ochre earth pigments to sketch repeating wavy river ripples, marching neem leaf garlands, blossoming lotus petals, dancing peacocks, and "
            "dotted golden sun rings! Grab your own colorful wax crayons, neat rulers, or blank drawing sketchbooks during classroom Activity 4 to carefully design bold repeating geometric borders, bright flower loops, and crisp nature leaf patterns upon drawn curved round pot "
            "outlines—joyfully uniting steady earthen pottery science craft with rich traditional regional Indian folk artistic heritage across loving generations!"
        ),
        "checkpoints": [
            {
                "question": "What natural inspiration do Indian potters commonly paint along curved clay jars using mineral red, white, and black earth colors?",
                "options": [
                    "Repeating geometric horizontal rings, wavy river ripples, neem leaf garlands, lotus petals, and peacock motifs",
                    "Bright glowing neon television barcodes only",
                    "Digital computer circuit chips melted into plastic",
                    "Blank invisible stripes seen only in pitch darkness"
                ],
                "answer": 0,
                "hint": "Artisans borrow rhythms from nearby rivers, leaves, birds, and geometry!",
                "explanation": "Traditional Indian pottery draws upon natural forms—wave bands, leaves, fish scales, flowers, and birds—painted in earthy mineral slips."
            },
            {
                "question": "How does holding a paint brush steadily against a gently spinning potter's wheel help an artisan decorate round pots easily?",
                "options": [
                    "Spinning the pot effortlessly draws perfectly crisp, even circular rings all the way around curved pot shoulders",
                    "Because spinning wheels turn red clay pigments into clear glass",
                    "So vertical crooked triangles form automatically without moving hands",
                    "Spinning dries finished paint into heavy metal wires"
                ],
                "answer": 0,
                "hint": "Think of keeping a steady finger on a rotating turntable or spinning wheel!",
                "explanation": "Rotation turns a single steady brush touch into an unbroken symmetrical horizontal ring around the vessel."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        twc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} title words) | Speech: {wc} words")
        assert 1 <= twc <= 3, f"Slide {s['id']} title word count {twc} not in 1-3"
        assert 195 <= wc <= 215, f"Slide {s['id']} speech word count {wc} not in 195-215"
    print("All Part 1 assertions passed!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 10: This World of Things
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- No human character names (Khushi, Moyna, Dadu, Harpreet, Raghav, Shirin, etc.), no lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Sunlit Classroom Objects",
        "subtitle": "Observing Materials Inside a Bright Sunlit Learning Room",
        "speech": (
            "Welcome, observant young scientists, to an exciting scientific adventure exploring the fascinating physical world of everyday things all "
            "around us! Picture a bright morning sketch drawn thoughtfully by a third-grade student sitting inside a sunlit school classroom! Warm "
            "golden morning sunlight streams cleanly straight through tall glass windowpanes, illuminating wooden desks, sturdy school benches, stacked "
            "paper notebooks, gleaming steel water bottles, rubber erasers, and brass door latches! Pause for one curious moment and examine that classroom "
            "scene like a sharp detective! Why does morning sunshine pass cleanly straight through windowpanes to warm indoor desks, yet stop cold at "
            "thick brick walls and wooden classroom doors? Why do sturdy school desks stand solidly upon heavy wooden legs instead of soft flowing cloth, "
            "while window curtains sway gracefully inside morning breezes? Every single object inside homes, gardens, and classrooms is carefully crafted "
            "out of specific chosen materials possessing special physical properties—some hard and heavy, some smooth and shiny, some soft and flexible, "
            "and some brilliantly clear! Learning why clever humans carefully match particular materials to distinct everyday useful tasks unlocks wonderful scientific curiosity, sharp observation skills, and smart design thinking right "
            "inside our everyday school and home surroundings!"
        ),
        "checkpoints": [
            {
                "question": "Why does bright morning sunshine pour cleanly into the classroom through window glass rather than wooden door panels?",
                "options": [
                    "Window glass is clear and lets light pass straight through, whereas thick wood blocks light completely",
                    "Because sunlight dislikes touching brown wooden doors",
                    "Because glass generates its own electric daylight bulbs inside",
                    "Because wooden walls fly upward when sunshine hits them"
                ],
                "answer": 0,
                "hint": "Look through clear window glass versus solid wooden panels—which one transmits light?",
                "explanation": "Clear window glass transmits visible light rays cleanly indoors while solid opaque wood blocks light rays."
            },
            {
                "question": "Why are sturdy classroom benches and desks built from hard wood or metal instead of soft cotton cloth?",
                "options": [
                    "Rigid wood and metal hold their firm shape safely to support heavy books and sitting students without collapsing",
                    "Because wooden trees grow inside classroom corners automatically",
                    "Because cotton cloth turns into liquid whenever sunlight touches it",
                    "Because cloth weighs ten tons per shirt"
                ],
                "answer": 0,
                "hint": "Think about what happens if you try setting heavy books atop a hanging cloth bedsheet!",
                "explanation": "Tables and benches require rigid, strong materials capable of bearing weight without bending or tearing."
            }
        ]
    },
    {
        "id": 2,
        "title": "Wood And Metals",
        "subtitle": "Tracing Wooden Furniture and Underground Earth Metal Ores",
        "speech": (
            "Look closely around your room during Activity 1 and Activity 2 to uncover the hidden geological story behind sturdy wooden furniture and "
            "gleaming metallic hardware! Touch the smooth grain of a classroom wooden desk, pencil shaft, or heavy wooden door—where did that solid, "
            "dependable material originally begin growing? Years earlier inside quiet forest groves or managed timber farms, tall leafy trees steadily "
            "built thick, durable trunks out of woody plant fibers! Skilled carpenters then sawed cured timber planks carefully into chairs, shelves, "
            "and rulers. Now look right beside wooden door edges at sturdy metal hinges, shiny steel screws, heavy iron nails, and strong sliding door "
            "latches! Do iron, brass, aluminum, or copper ever sprout upon leafy tree branches? Never! Metals originate deep underground inside ancient "
            "Earth rocks! Miners dig deep down into rocky hillsides to extract special mineral-packed rocks and sediments known scientifically as ores! "
            "Inside intense hot furnaces, skilled metal engineers carefully smelt melted rock ores to extract pure strong metals like iron, aluminum, brass, and copper—molding "
            "glowing hot liquid metal smoothly into sturdy iron nails, unbreakable metal door hinges, shiny stainless steel kitchen spoons, ringing school bells, strong window grilles, and tough long-lasting everyday metallic bicycle frames!"
        ),
        "checkpoints": [
            {
                "question": "Where do strong metals used to craft door hinges, nails, steel spoons, and sliding latches originally come from?",
                "options": [
                    "Mineral-bearing rocks and sediments called ores dug from deep inside the Earth",
                    "Green leaves plucked off mango and guava trees",
                    "Clouds floating high inside rainy monsoon skies",
                    "Soft butter churned from warm cow milk"
                ],
                "answer": 0,
                "hint": "Miners excavate special mineral rocks underground and heat them inside furnaces!",
                "explanation": "Metals such as iron, copper, and aluminum are extracted from natural rock mineral deposits called ores inside Earth's crust."
            },
            {
                "question": "Why are door hinges, nails, and window latches crafted from strong metals rather than soft dry chalk?",
                "options": [
                    "Metals possess high strength and hardness, resisting snapping or crumbling under constant heavy door swinging",
                    "Because chalk melts into sweet honey inside doors",
                    "Because metal nails grow taller every summer morning",
                    "Chalk attracts thunderbolts into school classrooms"
                ],
                "answer": 0,
                "hint": "Imagine hammering brittle chalk into wood versus strong forged steel nails!",
                "explanation": "Metals endure heavy pressure, friction, and pounding without shattering, making them ideal for hinges, nails, and fasteners."
            }
        ]
    },
    {
        "id": 3,
        "title": "Light Passing Through",
        "subtitle": "Testing Torch Beams Through Clear, Frosted, and Solid Objects",
        "speech": (
            "Switch off bright classroom lamps momentarily and pull out a glowing pocket flashlight for Activity 3 and Activity 4—our exciting Light "
            "Transmission Lab! Shine a crisp bright beam straight through three very different household objects resting upright upon your study table, "
            "watching carefully what lands upon the white wall behind them! First, hold up a sparkling clean glass tumbler or clear plastic water bottle: "
            "almost ALL torchlight beams pass right through uninterrupted, illuminating a bright round circle upon the back wall! Second, hold up a thick "
            "wooden cutting board, metal steel tiffin box, or thick hardcover science textbook: ZERO light squeezes past! Instead, a sharp dark shadow "
            "falls directly onto the wall behind because solid dense wood and metal block light rays completely! Third, hold up an oiled butter-paper sheet, "
            "frosted glass pane, or thin creamy paper lampshade: notice something fascinating halfway between clear and dark? Partial soft glowing light "
            "filters gently through in softly scattered directions—allowing fuzzy dim glowing shapes to appear without clear sharp readable details! Observing crisp or blurry torch shadows closely reveals "
            "just how differently everyday materials welcome light clearly, softly scatter glowing beams, or completely stop traveling bright rays of light inside dark quiet science rooms!"
        ),
        "checkpoints": [
            {
                "question": "When a bright flashlight beam hits a thick wooden board or closed hardcover book, what lands on the wall behind it?",
                "options": [
                    "A crisp dark shadow, because solid wood and cardboard block light completely from passing through",
                    "A bright green glowing laser rainbow circle",
                    "Water starts pouring straight out of the flashlight glass",
                    "All light rays bounce straight through unchanged"
                ],
                "answer": 0,
                "hint": "Can sunlight or flashlight beams pass straight through thick solid books?",
                "explanation": "Opaque materials like wood and thick books absorb or reflect light completely, casting crisp shadows behind them."
            },
            {
                "question": "What happens when you shine a torch behind a thin paper lampshade or frosted bathroom glass pane?",
                "options": [
                    "Partial scattered light filters softly through, creating a cozy dim glow without letting sharp details show clearly",
                    "Zero light escapes—just pure pitch darkness",
                    "Paper transforms instantaneously into clear unbreakable crystal",
                    "Light bends backwards 180 degrees underground"
                ],
                "answer": 0,
                "hint": "Does a paper lampshade block all light like brick, or glow softly in bedrooms?",
                "explanation": "Translucent materials transmit partial light while scattering rays, allowing blurred brightness rather than clear sharp images."
            }
        ]
    },
    {
        "id": 4,
        "title": "See Through Glasses",
        "subtitle": "Classifying Materials as Transparent, Translucent, or Opaque",
        "speech": (
            "Now let us give exact scientific names to the three marvelous light behaviors we observed during our flashlight tests! Whenever a clean "
            "material lets light pass cleanly straight through so our eyes distinguish sharp details right on the other side, scientists call it "
            "Transparent! Think about sparkling transparent examples surrounding us daily: clear glass windowpanes, empty spectacles lenses, clean glass "
            "aquariums, crisp pure water inside tumblers, and invisible classroom air! Second, whenever an object allows ONLY partial scattered light "
            "through—letting you see fuzzy silhouettes without crisp sharp reading—scientists classify it as Translucent! Memorable translucent companions "
            "include oiled butter paper, thin tissue paper lampshades, frosted bathroom windows, foggy mist, and thin milky wax! Third, whenever solid "
            "matter stops ALL light rays completely so nothing behind can ever be seen, scientists term it Opaque! Solid brick walls, sturdy wooden "
            "cupboards, metal steel dinner plates, ceramic coffee mugs, thick notebooks, and heavy stone boulders are strictly opaque! Choosing wisely among transparent, translucent, "
            "and opaque materials thoughtfully helps clever architects and house builders daily design sunny bright clear glass windows, cozy soft glowing bedroom paper lampshades, sparkling protective fish aquariums, and completely private solid wooden bathroom doors everywhere safely!"
        ),
        "checkpoints": [
            {
                "question": "Which group contains ONLY 'Transparent' items that allow clear, sharp vision straight through them?",
                "options": [
                    "Clear window glass, sparkling aquarium glass, clean still water, and clear spectacle lenses",
                    "Wooden cupboard doors, brick walls, and steel lunchboxes",
                    "Oiled butter paper, frosted glass, and paper lampshades",
                    "Thick cardboard boxes and iron frying pans"
                ],
                "answer": 0,
                "hint": "Can you read book letters clearly right through clear aquarium glass?",
                "explanation": "Transparent materials transmit light rays cleanly without scattering, permitting sharp see-through visibility."
            },
            {
                "question": "Why are frosted bathroom windows and paper lampshades intentionally crafted from 'Translucent' materials?",
                "options": [
                    "They let soft welcoming daylight or lamp glow filter through gently while blurring sharp shapes to protect privacy and comfort eyes",
                    "Because translucent glass lets zero light rays pass inside ever",
                    "So harsh blinding sunbeams burn wooden desks quickly",
                    "Because paper lampshades turn opaque stone into transparent air"
                ],
                "answer": 0,
                "hint": "Think about wanting cozy soft brightness WITHOUT glaring bulbs or clear outside viewing!",
                "explanation": "Translucent materials scatter incoming light softly—providing illumination while shielding privacy or softening harsh bulb glare."
            }
        ]
    },
    {
        "id": 5,
        "title": "Colored Filter Magic",
        "subtitle": "Exploring How Tinted Transparent Plastics and Bottles Shift Perceived Colors",
        "speech": (
            "Have you ever held a clean, transparent green polythene wrapper or a bright red glass bottle gently in front of your eyes and gazed "
            "around a sunny garden? Suddenly crisp white paper looks rosy red or emerald green, yellow marigolds transform darkly, and friends' faces "
            "glow inside colorful filters! Let us explore the joyful physics behind Chapter 10's Color Experiments! Regular white sunshine actually blends "
            "all seven sparkling rainbow colors mixed effortlessly together! Whenever white light passes through clear colorless glass, every single "
            "rainbow shade travels smoothly onward together—leaving objects appearing completely natural! However, when transparent thin plastic bags, "
            "cellophane wrappers, or tinted soda bottles are dyed bright red, blue, or green, they act like strict colorful gates! A transparent green "
            "bottle lets primarily green light pass straight into your eyes while absorbing or blocking most red and blue wavelengths! Similarly, looking "
            "through transparent yellow tinted goggles fills the whole bright room with a warm golden hue! Remember one crucial optical science rule: colored wrappers remain clearly transparent "
            "as long as crisp object outlines still show cleanly through them—teaching curious young observers how color tint and transparency create dazzling stage spotlights, traffic signals, and sunny sunglasses!"
        ),
        "checkpoints": [
            {
                "question": "Why does a white sheet of paper appear bright red when you look at it closely through a clear red transparent plastic sheet?",
                "options": [
                    "The red transparent plastic acts as a filter letting mostly red light wavelengths pass through into your eyes",
                    "Because red plastic shoots permanent red ink paint onto paper miles away",
                    "Because white paper instantly turns into solid wood",
                    "Red cellophane blocks ALL light completely like a black brick"
                ],
                "answer": 0,
                "hint": "White light contains all rainbow colors; colored filters allow matching light waves past!",
                "explanation": "A transparent red filter transmits red wavelengths cleanly while absorbing most other rainbow colors from white sunlight."
            },
            {
                "question": "If you hold a clean transparent blue bottle right up to your eye, can you still recognize chairs and windows behind it?",
                "options": [
                    "Yes—sharp object shapes remain recognizable inside blue tints because colored transparent plastic still transmits light cleanly",
                    "No—because colored glass immediately becomes completely opaque like brick walls",
                    "No—chairs turn completely upside down inside blue light",
                    "Yes—only when rooms have zero lights turned on"
                ],
                "answer": 0,
                "hint": "Tinted transparency changes hue, yet preserves see-through transmission!",
                "explanation": "Colored transparent plastics or glasses alter perceived color hue while maintaining clear object outline visibility."
            }
        ]
    },
    {
        "id": 6,
        "title": "Six Everyday Materials",
        "subtitle": "Sorting Home and School Objects Into Wood, Metal, Glass, Plastic, Clay, and Rubber",
        "speech": (
            "Walk carefully through your study desk, school backpack, and kitchen shelf carrying a sorting notebook—and try sorting objects by what "
            "primary substance builds them! Almost every helpful everyday item belongs inside six familiar material families: Wood, Metal, Glass, Plastic, "
            "Clay, and Rubber! Let us examine sparkling real examples from each category! Wood shapes warm pencils, cricket bats, wooden spoons, and "
            "study desks. Strong Metals craft gleaming steel spoons, brass bells, aluminum tiffin boxes, and heavy iron locks. Clear brittle Glass "
            "constructs laboratory test tubes, transparent windowpanes, marbles, and crisp drinking jars. Featherlight waterproof Plastic forms colorful "
            "geometry scales, raincoats, school lunchboxes, and squeeze bottles. Baked earthy Clay molds cooling summer water matkas, flowerpots, red "
            "house bricks, and ceramic tea cups! Finally, bouncy stretchy Rubber crafts pencil erasers, bicycle tires, hair bands, and waterproof boots! "
            "Notice one awesome material engineering secret too: one single helpful everyday object—like a hinged classroom wooden door with metal locks or a writing wooden pencil sporting a metal crimp ferrule and soft pink rubber eraser tip—"
            "can cleverly combine MULTIPLE helpful contrasting raw materials working together smoothly side by side like strong engineering teammates across schools, kitchens, and joyful playgrounds every day!"
        ),
        "checkpoints": [
            {
                "question": "Which everyday school tool cleverly combines THREE different materials—Wood, Metal, and Rubber—working together in one object?",
                "options": [
                    "An eraser-tipped wooden pencil (wood shaft + metal crimp ferrule + rubber eraser tip)",
                    "A single plain river pebble",
                    "An empty glass of clean tap water",
                    "A pure sheet of folded white paper"
                ],
                "answer": 0,
                "hint": "Examine both ends of a classic yellow school pencil carefully!",
                "explanation": "An eraser-topped wooden pencil pairs lightweight carvable wood, a strong metal ferrule ring, and soft frictional rubber."
            },
            {
                "question": "Which trio lists items crafted specifically out of bouncy, elastic RUBBER?",
                "options": [
                    "Pencil erasers, bicycle tires, and stretchy hair bands",
                    "Window glass panes, bricks, and clay matkas",
                    "Steel spoons, iron hinges, and copper coins",
                    "Wooden benches, storybooks, and cotton towels"
                ],
                "answer": 0,
                "hint": "Think about materials prized for flexibility, grip friction, and erasing pencil graphite.",
                "explanation": "Erasers, gripping bicycle tires, and stretchy elastic bands exploit rubber's flexible, high-friction elasticity."
            }
        ]
    },
    {
        "id": 7,
        "title": "Natural Source Chains",
        "subtitle": "Tracing Finished Objects Back Through Chain Games to Nature's Ingredients",
        "speech": (
            "Play our exciting Chapter 10 Material Chain Game—tracing gleaming finished human objects backward step by step until we discover their "
            "original earthly source hiding inside nature! Ready to follow four surprising detective chains? Chain one: hold a crisp transparent Glass "
            "tumbler or windowpane! Where did crystal glass begin before shining inside factories? Incredibly, glass is made mostly by melting fine white "
            "river and desert SILICA SAND inside roaring hot furnaces alongside soda ash and limestone until liquid sand cools crystal-clear! Chain two: "
            "lift a bouncy pink Rubber eraser! Natural rubber begins as milky white liquid sap called latex tapped gently from incisions on tropical rubber "
            "tree bark! Chain three: tap an earthen terracotta flowerpot or matka! It began as wet river bank CLAY kneaded upon spinning wooden potter's "
            "wheels and baked solidly inside kilns! Chain four: check colorful Plastic bottles and crisp Wooden rulers—plastic derives chemically from ancient "
            "deep underground petroleum oil, while crisp writing paper and wooden rulers trace right back to lush tree wood cellulose! Tracing daily material source chains backward teaches curious young explorers profound lasting gratitude and wise "
            "respect for preserving Earth's limited precious natural water, sand, forests, and rock resources everywhere!"
        ),
        "checkpoints": [
            {
                "question": "Which surprising everyday transparent material is manufactured mostly by melting clean white SAND at extremely high temperatures?",
                "options": [
                    "Clear glass (windows, spectacles, and glass tumblers)",
                    "Soft woven cotton shirts",
                    "Stretchable rubber bicycle tires",
                    "Strong iron railway rails"
                ],
                "answer": 0,
                "hint": "Beach and river silica sand melts under fiery heat to cool into transparent sheets!",
                "explanation": "Silica sand heated above 1,500°C melts and cools cleanly into transparent glass."
            },
            {
                "question": "Which natural raw source matches cleanly to Rubber erasers and Clay flowerpots?",
                "options": [
                    "Milky latex sap tapped from rubber trees -> Rubber; Wet river soil earth -> Clay pots",
                    "Melted white sea salt -> Rubber; Chopped tree leaves -> Clay pots",
                    "Underground iron ores -> Rubber; Clear ocean water -> Clay pots",
                    "Dry desert sand -> Rubber; Fluffy sky clouds -> Clay pots"
                ],
                "answer": 0,
                "hint": "Natural rubber flows as white liquid sap from tree trunks!",
                "explanation": "Tree latex sap processes into elastic rubber, while fine wet mineral soil forms moldable earthen clay vessels."
            }
        ]
    },
    {
        "id": 8,
        "title": "Feel And Shine",
        "subtitle": "Inspecting Sensory Properties: Shiny, Dull, Smooth, Rough, and Thermal Feel",
        "speech": (
            "Close your eyes softly for a thrilling sensory science game during Activity 5—identifying mysterious mystery objects solely through attentive "
            "fingertips and keen eyes! Every material greets our five senses with distinctive physical signatures called Sensory Properties! First observe "
            "visual Lustre or Shine: polished stainless steel bowls, golden brass bells, and clean glass tumblers gleam with sparkling metallic or glassy "
            "shine bouncing room light back brightly—whereas dry blackboard chalk sticks, muddy clay bricks, and rough jute sacks appear completely Dull! "
            "Second glide fingertips smoothly across surfaces to compare Texture: polished marble tiles and window glass feel effortlessly Smooth like "
            "ice, whereas ancient neem tree bark, sandpaper sheets, and sandy river stones feel noticeably Rough with tiny bumps! Third notice Temperature "
            "Touch right away inside cool rooms: touch a stainless steel spoon alongside a wooden block sitting on the exact same table! Why does steel "
            "feel noticeably Colder than warm wood? Polished metals pull natural finger warmth away swiftly like rapid heat rivers, whereas wood holds warmth gently close—teaching clever cooks why safe kitchen frying "
            "pots always use insulated cool sturdy wooden handles safely protecting cooks' hands while keeping shiny rapid-heating stainless steel metal cooking pot bases underneath!"
        ),
        "checkpoints": [
            {
                "question": "Even when sitting side by side in the same cool room, why does a shiny steel spoon feel colder to your fingers than a wooden spoon?",
                "options": [
                    "Metal conducts heat swiftly away from warm fingertips, making steel feel cold while wood holds heat gently",
                    "Because steel spoons secretly contain frozen ice cubes inside",
                    "Because wood burns at 90°C indoors",
                    "Because steel absorbs green light from lamps"
                ],
                "answer": 0,
                "hint": "Think about why frying pans have metal bottoms yet wooden or plastic handles!",
                "explanation": "Metals are rapid thermal conductors that draw warmth quickly off skin, creating a cold sensation compared to insulating wood."
            },
            {
                "question": "Which pair properly matches physical items to their exact sensory texture and luster?",
                "options": [
                    "Polished steel spoon = Shiny & Smooth; Dry tree bark or sandpaper = Dull & Rough",
                    "Dry blackboard chalk = Gleaming mirror shine; Glass marble = Rough sandy bark",
                    "Jute gunny sack = Mirror glassy smoothness; Brass temple bell = Soft fuzzy cotton",
                    "Mud brick = Transparent shiny diamond"
                ],
                "answer": 0,
                "hint": "Notice which surface reflects light brightly vs feels bumpy under fingertips.",
                "explanation": "Polished metals display smooth lustrous shine, while dry bark and abrasive sandpapers exhibit matte dullness and rough texture."
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

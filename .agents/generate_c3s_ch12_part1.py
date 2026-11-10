#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 12: Taking Charge of Waste
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero human character names (Raghav, Khushi, Moyna, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Everyday Waste",
        "subtitle": "Where Do Peels, Wrappers, Shavings, Old Bottles, and Batteries Come From?",
        "speech": (
            "Welcome, attentive young eco-detectives, to Chapter Twelve: Taking Charge of Waste! Have you ever paused at dusk to inspect everything our families "
            "and bustling classrooms toss aside across a single ordinary day? Think carefully through our busy morning-to-night routines: early kitchen preparations drop fresh banana "
            "peels, potato skins, tea leaves, and crushed eggshells; crisp classroom sharpening sprinkles curly wooden pencil shavings onto desks; lunch snack breaks leave shiny "
            "crinkled plastic biscuit wrappers and empty juice cartons; evening household repairs turn up cracked glass bottles, rusty metal tins, torn exercise paper, "
            "faded outgrown cotton clothes, and worn-out dead torch batteries! Individually, tossing away one lone sweet wrapper or one dried apple core appears tiny and harmless. "
            "However, when hundreds of nearby households toss every scrap carelessly outdoors without thinking twice, tiny discarded items combine swiftly into mountainous, smelly "
            "garbage heaps near bus stops, school gates, and street corners! Recognizing all varied sources of everyday household trash—from wet organic kitchen leftovers "
            "and scrap paper to long-lasting plastics, sharp metals, and chemical dead batteries—marks our very first scientific detective clue toward keeping clean neighborhoods. "
            "Once observant learners notice exactly how daily choices generate rubbish piles, they hold real power to shrink waste right at home!"
        ),
        "checkpoints": [
            {
                "question": "Which group lists common everyday waste items created regularly across normal home and school routines?",
                "options": [
                    "Fruit peels, plastic wrappers, pencil shavings, scrap paper, old tins, worn clothes, and dead batteries",
                    "Fresh mountain snowfall and clean ocean currents",
                    "Living oak trees and fluttering garden butterflies",
                    "Warm afternoon sunlight and gentle evening breezes"
                ],
                "answer": 0,
                "hint": "Think about kitchen cooking scraps, study leftovers, snack covers, and worn gadgets!",
                "explanation": "Daily cooking, writing, snacking, and wearing items out generate varied wastes like peels, wrappers, shavings, paper, tins, old cloth, and used batteries."
            },
            {
                "question": "Why do huge unsightly garbage mounds form quickly around neighborhoods even when each person drops just one wrapper?",
                "options": [
                    "Hundreds of daily small discards multiply together into overflowing piles across street corners and open drains",
                    "Because sunlight magically swells single wrappers into giant rocks",
                    "Because plastic wrappers sprout roots and grow taller overnight",
                    "Because street brooms blow paper skyward every noon"
                ],
                "answer": 0,
                "hint": "Count what happens when dozens or hundreds of neighbors drop 'just one' scrap!",
                "explanation": "Small individual discards across large communities combine rapidly into huge foul garbage heaps if not collected and managed responsibly."
            }
        ]
    },
    {
        "id": 2,
        "title": "Garbage Heaps",
        "subtitle": "Tracing How Unmanaged Rubbish Piles Hurt Streets, Drains, and Community Beauty",
        "speech": (
            "Now imagine walking slowly past an unguarded empty plot right beside a lively school playground where careless neighbors dump overflowing mixed sacks day after day! "
            "Notice immediately what transforms a bright sunlit corner into a troubled wasteland: swirling afternoon breezes scatter lightweight plastic carry bags into "
            "green hedges and roadside drain grilles, rotting kitchen food emits sour smells attracting noisy buzzing swarms of houseflies, and jagged broken glass shards hide dangerously "
            "under soft damp dust! Unlike fallen dry forest leaves that rot swiftly back into rich fertile dark garden soil within a few warm weeks, synthetic plastic wrappers, metallic "
            "food tins, and heavy glass bottles linger stubbornly unchanged year after year without rotting away! Worse still, hungry stray animals sniff tempting vegetable scraps buried "
            "deep inside tangled knots of plastic bags, while leaking black paste from dead worn batteries drips toxic heavy-metal chemicals straight into garden soil and underground drinking water! Clean civic "
            "spaces belong equally to tiny crawling ants, tall leafy shade trees, playful schoolchildren, and walking elders. Understanding why unmanaged mixed "
            "garbage piles choke rainwater drains, spoil street beauty, spread foul germs, and injure creatures inspires caring young citizens to stop littering and keep communities clean!"
        ),
        "checkpoints": [
            {
                "question": "How do carelessly dumped roadside garbage piles affect neighborhood stormwater drains during rainy weeks?",
                "options": [
                    "Windblown plastic bags and mixed trash clog drain grilles, blocking rainwater flow and causing dirty street puddles",
                    "Mixed plastic piles filter cloudy rainwater into sparkling mountain springs",
                    "Floating garbage makes paved village streets stay bone-dry",
                    "Rusty tins sweep mud away faster than clean brooms"
                ],
                "answer": 0,
                "hint": "What happens when light plastic sheets wash straight into narrow storm drain mouths?",
                "explanation": "Loose wrappers and plastic carry bags wash into roadside drains, choking outlets and backing up foul dirty water across streets."
            },
            {
                "question": "Why is tossing dead dry-cell batteries casually into garden soil or open rubbish dumps unsafe?",
                "options": [
                    "Old batteries leak harmful toxic chemicals into soil and underground water rather than rotting safely like leaves",
                    "Because old batteries sprout sour weeds overnight",
                    "Because batteries cool afternoon sunshine below freezing",
                    "Batteries turn dry soil into transparent glass dust"
                ],
                "answer": 0,
                "hint": "Recall that batteries hold heavy metals and acidic paste inside!",
                "explanation": "Unlike organic peels or leaves, worn batteries contain hazardous chemicals that poison earth soil and groundwater if carelessly dumped."
            }
        ]
    },
    {
        "id": 3,
        "title": "Danger To Animals",
        "subtitle": "Protecting Grazing Cows, Dogs, and Wildlife From Swallowing Plastic Carry Bags",
        "speech": (
            "Observe closely what unfolds along busy neighborhood vegetable lanes whenever thoughtful care disappears! Many rushed evening shoppers tie leftover potato skins, stale bread "
            "crusts, cabbage leaves, or sweet mango peels tightly inside thin plastic carry bags before tossing those knotted bundles beside overflowing roadside corners. "
            "Soon afterward, wandering hungry cows, gentle goats, and street dogs follow tempting warm vegetable smells straight into the messy rubbish mound! "
            "Unable to untie tight plastic knots with clumsy hooves or paws, starving animals rip hastily through thin sheets and swallow dangerous plastic scraps straight alongside "
            "soft kitchen leftovers! Inside a friendly cow's stomach, natural vegetable peels digest swiftly and safely, yet indigestible plastic sheets tangle slowly week after week "
            "into dense rocky balls that block food passages completely! Sadly, countless innocent stray cows, bulls, deer, dogs, and hungry seabirds suffer terrible stomach pain or even "
            "lose their lives needlessly after ingesting discarded plastic bags! Even tiny garden hedgehogs and furry squirrels get stuck painfully inside discarded plastic cups and tight rings. "
            "Putting loose food scraps strictly inside compost bins—never trapped inside plastic bags—and carrying washable cloth shopping bags instead protects beloved innocent beloved street animals cleanly—keeping busy fruit markets, village pastures, and neighborhood parks safe and peaceful every single day!"
        ),
        "checkpoints": [
            {
                "question": "Why do stray cows and goats sadly swallow dangerous plastic bags at open street garbage piles?",
                "options": [
                    "People toss kitchen food peels tied inside plastic bags, so hungry animals eat plastic alongside food smells",
                    "Because cows prefer chewing crinkly plastic over sweet green grass",
                    "Because thin plastic turns into clover leaves in moonlight",
                    "Because cows use plastic bags to build warm nests"
                ],
                "answer": 0,
                "hint": "Animals smell leftover peels inside tied bags and cannot unwrap knots with hooves!",
                "explanation": "Tying vegetable scraps inside plastic bags lures hungry stray animals to swallow indigestible plastic sheets that block their stomachs fatally."
            },
            {
                "question": "Which everyday habit protects street cows, goats, and wildlife immediately from plastic bag ingestion?",
                "options": [
                    "Never throw food scraps inside plastic bags; put loose organic peels into green compost bins and shop with cloth bags",
                    "Toss two knotted plastic bags around leftover chapatis instead of one",
                    "Leave torn snack wrappers scattered across grazing meadows",
                    "Paint colorful designs on empty plastic wrappers before littering"
                ],
                "answer": 0,
                "hint": "Separate natural food scraps from plastic completely!",
                "explanation": "Composting loose food scraps separately and using reusable cloth bags prevents dangerous plastic bags from entering stray animal diets."
            }
        ]
    },
    {
        "id": 4,
        "title": "Burning Plastic Smoke",
        "subtitle": "Why Burning Rubbish Releases Toxic Gases and Damages Clean Breathing Air",
        "speech": (
            "Sometimes impatient sweepers rake dry fallen garden leaves mixed alongside plastic snack wrappers, torn polythene bags, old foam cups, and rubber scraps into an evening street pile "
            "and strike a quick match just to make unsightly heaps vanish from sight! Wait right there—let clear science reveal the hidden danger swirling upward inside thick dark smoke! "
            "Does lighting plastic rubbish on fire truly erase waste harmlessly from Earth? Never! Plastic is manufactured chemically from deep fossil oils, so fierce orange flames break "
            "plastic chains apart into clouds of invisible toxic gases, heavy black soot particles, and sharp irritating fumes! Breathing acrid plastic smoke makes playing children cough heavily, "
            "stings delicate eyes watery and red, worsens painful breathing illnesses such as asthma, and weakens singing bird lungs perched high inside neighborhood neem branches. "
            "Meanwhile, melted sticky plastic crusts still stay behind baked permanently across scarred soil below! Even burning dry crisp garden leaves carelessly clouds clean neighborhood sky air "
            "with thick choking haze instead of letting earthworms turn dry leaves peacefully into rich fertile garden compost! True Eco-Champions forbid open trash fires everywhere—protecting children's lungs, cheerful singing birds, buzzing honeybees, and crisp sparkling blue neighborhood skies all year long!"
        ),
        "checkpoints": [
            {
                "question": "What happens to neighborhood air quality and lungs whenever plastic waste heaps are burned openly?",
                "options": [
                    "Burning plastic releases poisonous toxic gases and dense soot smoke that harm human lungs, eyes, and birds",
                    "Burning plastic releases cool fresh oxygen like tall green banyan trees",
                    "Plastic smoke washes street pavements sparkling white",
                    "Fire turns burnt plastic smoothly into sweet drinking water"
                ],
                "answer": 0,
                "hint": "Think about the sharp black acrid fumes rising off melted plastic!",
                "explanation": "Combusting plastic releases hazardous chemical fumes and toxic smoke particles that injure respiratory health and pollute local air."
            },
            {
                "question": "Instead of setting crisp dry garden leaves on fire every autumn, what eco-friendly method manages leaf piles cleanly?",
                "options": [
                    "Burying or piling leaves in a compost pit where microbes rot them safely into rich garden fertilizer",
                    "Mixing dry leaves with old batteries and lighting tall bonfires",
                    "Stuffing dry leaves tightly inside street rainwater drains",
                    "Wrapping crisp leaves inside shiny plastic gift paper"
                ],
                "answer": 0,
                "hint": "Nature turns fallen leaves into dark black plant soil food without smoke!",
                "explanation": "Composting dry garden leaves naturally yields nutritious dark soil manure while keeping neighborhood breathing air fresh and smoke-free."
            }
        ]
    },
    {
        "id": 5,
        "title": "Stagnant Water Danger",
        "subtitle": "How Puddles in Old Tires, Pots, and Garbage Breed Disease Mosquitoes",
        "speech": (
            "Search carefully around shady backyard corners and damp alleys right after heavy monsoon rain showers! Besides making streets look messy, abandoned open rubbish containers—such as cracked "
            "plastic yogurt cups, empty coconut shells, punctured old bicycle tires, rusty paint cans, and choked open gutters—trap quiet bowls of still, stagnant rainwater! Why "
            "must watchful young science detectives inspect immediately for any quiet trapped water? Because calm, stagnant rainwater serves as the favorite warm nursery cradle for buzzing "
            "female mosquitoes! A mother mosquito never lays delicate floating egg clusters across swift rushing river rapids; instead, she lays hundreds of tiny eggs softly across calm "
            "unmoving water puddles hiding peacefully inside thrown cans, pot saucers, and clogged drains! Within a few warm days, wriggling aquatic larvae hatch out, grow wings swiftly, "
            "and fly straight indoors at dusk to bite sleeping family members—spreading dangerous fevers including painful malaria and dengue! Notice how closely neat waste control guards human "
            "health: tipping water dry out of plant saucers weekly, clearing loose wrappers off street gutters, covering rooftop storage tanks tightly, and recycling stray containers removes mosquito nurseries safely without needing harsh toxic chemical sprays—keeping every playful child and family protected safely from dangerous mosquito-borne fevers!"
        ),
        "checkpoints": [
            {
                "question": "Why are empty open tins, discarded tires, and blocked drains full of still rainwater dangerous to human health?",
                "options": [
                    "Stagnant standing rainwater creates breeding nurseries for mosquitoes that carry dengue and malaria fevers",
                    "Because calm puddles inside tires sprout sharp metallic thorns",
                    "Because open cans freeze solid under hot midday sunshine",
                    "Still rainwater cools house walls too quickly"
                ],
                "answer": 0,
                "hint": "Which buzzing biting insect hatches larvae in calm standing water?",
                "explanation": "Mosquitoes breed rapidly in stagnant water trapped inside discarded cans, tires, and blocked drains, transmitting diseases like malaria and dengue."
            },
            {
                "question": "Which simple weekly habit stops mosquito breeding immediately around school courtyards and homes?",
                "options": [
                    "Emptying trapped water from unused pots, clearing open trash containers, and keeping drains unblocked and tanks covered",
                    "Collecting extra open plastic bowls of rain across rooftops",
                    "Tossing banana peels into puddles along driveways",
                    "Covering wet gutters with thick torn newspapers"
                ],
                "answer": 0,
                "hint": "Remove calm trapped standing water before mosquito larvae grow wings!",
                "explanation": "Clearing junk water-holding containers, keeping drains clear, and sealing tanks deprive mosquitoes of standing breeding water."
            }
        ]
    },
    {
        "id": 6,
        "title": "First Rule Reduce",
        "subtitle": "Avoiding Packaged Snacks, Saying No to Plastic Bags, and Smart Consumption",
        "speech": (
            "Now let us unlock the two golden superpowers of spotless eco-friendly living: **Reduce** and **Reuse**! Meet our very first champion rule—**Reduce**—meaning shrink garbage right at its "
            "source before needless trash even crosses your family kitchen doorway! Pause beside a bright neighborhood grocery shelf and compare two snack choices: picking loose fresh roasted peanuts, "
            "golden bananas, or crisp apples placed neatly inside your own woven cotton tote bag versus grabbing five shiny plastic-wrapped mini chip packets sealed inside yet another thin "
            "disposable polythene carry bag! Which shopping basket generates a mountain of crinkly shiny plastic rubbish just ten minutes after finishing snack time? Choosing fresh unpackaged wholesome "
            "foods and saying a cheerful firm 'No thank you!' to extra thin plastic carry bags prevents dozens of persistent wrappers from ever entering street dumps! Tuck lightweight folded cloth "
            "or jute bags neatly inside school backpacks and parent baskets everywhere! Reducing also means serving wise lunch portions you finish completely cleanly, turning off idle room lights, shutting running taps promptly, "
            "repairing pencil cases cleanly, and buying sturdy long-lasting supplies rather than fragile trinkets. Remember every single day: the cleanest garbage anywhere on Earth is needless waste that smart mindful families never even created!"
        ),
        "checkpoints": [
            {
                "question": "What does practicing the First Rule — 'Reduce' — mean when shopping for daily groceries or snacks?",
                "options": [
                    "Choosing unpackaged fresh items, saying no to plastic carry bags, and taking only quantities we truly use cleanly",
                    "Buying tiny snacks wrapped in three shiny plastic layers each",
                    "Always collecting two new plastic bags at every shop counter",
                    "Heaping full plates with food to throw half inside bins"
                ],
                "answer": 0,
                "hint": "Think about preventing rubbish before it enters your shopping bag!",
                "explanation": "Reducing waste avoids excess single-use packaging, carries reusable cloth shopping bags, and prevents food or material over-buying."
            },
            {
                "question": "Which practical pocket habit stops shoppers from bringing dozens of thin plastic bags home each month?",
                "options": [
                    "Keeping a lightweight folded cloth or jute bag handy inside school backpacks or shopping baskets",
                    "Asking shopkeepers for doubled plastic handles every morning",
                    "Leaving old plastic bags flying along windy sidewalks",
                    "Buying packaged bottled water for every five-minute walk"
                ],
                "answer": 0,
                "hint": "Bring your own washable fabric bag from home before leaving!",
                "explanation": "Carrying a sturdy reusable cloth or jute bag eliminates the need for single-use disposable shop plastic bags completely."
            }
        ]
    },
    {
        "id": 7,
        "title": "Sharing Old Things",
        "subtitle": "Passing Outgrown Books, Toys, and Uniforms Joyfully to Others Who Need Them",
        "speech": (
            "Look gently inside tidy bedroom closets, toy baskets, and bright study bookshelves today! Nearly every growing third-grade learner keeps cheerful picture storybooks already enjoyed five times, "
            "wooden jigsaw puzzles solved swiftly months ago, warm knitted winter sweaters whose sleeves now feel snug across growing wrists, or sturdy outgrown school satchels resting quietly in dark cupboard "
            "corners! Before letting crisp outgrown belongings land anywhere near rubbish bins, pause thoughtfully and ask: could a younger neighbor, cousin, or cheerful community library treasure these items right away? "
            "Sharing clean storybooks, coloring pencils, neat winter coats, and unbreakable wooden toys launches joyful second chapters for loved treasures while keeping heaps of useful goods far away from crowded "
            "landfills! Many caring Indian schools host lively Share-and-Care book banks every spring where advancing pupils happily hand clean, well-kept textbooks onto incoming younger classes. Sharing multiplies joy doubly—brightening "
            "younger neighbors' sunny afternoons with helpful learning gifts while freeing calm, open, uncluttered study shelves indoors! Remember thoughtfully every season: true community richness lies never in hoarding forgotten dusty clutter, "
            "but in passing good useful treasures kindly onward generously to welcoming community hands so beloved books and toys continue sparking joyful learning inside caring new classrooms everywhere!"
        ),
        "checkpoints": [
            {
                "question": "What is the wisest eco-friendly action for neat storybooks, toys, and uniforms you have outgrown cleanly?",
                "options": [
                    "Share or donate them cleanly to younger learners, community centers, or needy neighbors so they serve happily again",
                    "Shred old storybooks and toss pieces into roadside drains",
                    "Throw neat toys straight into black roadside garbage piles",
                    "Burn old clean clothes behind open backyard walls"
                ],
                "answer": 0,
                "hint": "Outgrown clean items are still wonderfully useful to younger kids!",
                "explanation": "Passing clean outgrown books, toys, and clothes onward reduces waste piles while joyfully helping community members."
            },
            {
                "question": "How do school Share-and-Care book banks benefit both local families and our natural environment?",
                "options": [
                    "They extend textbook lifespans across multiple student classes, saving trees, money, and paper waste together",
                    "They encourage throwing crisp books away every Friday",
                    "They wrap every workbook inside five plastic sheets",
                    "They fill classroom desks with dusty broken batteries"
                ],
                "answer": 0,
                "hint": "Fewer newly printed books mean fewer cut trees and fewer discarded paper piles!",
                "explanation": "Reusing shared books across consecutive student classes conserves forest trees, family budgets, and paper landfill space."
            }
        ]
    },
    {
        "id": 8,
        "title": "Second Rule Reuse",
        "subtitle": "Giving Everyday Household Items Creative New Jobs Instead of Throwing Them Away",
        "speech": (
            "Meet our second mighty waste-fighting champion—**Reuse**! Once an everyday household item enters your home safely, reusing means spotting clever practical ways to keep using it repeatedly "
            "before ever letting it slide toward a garbage bin! Peek curiously inside bright home kitchens and craft corners: washed clear glass jam jars shine neatly along spice racks holding shiny green "
            "cardamom pods, colorful crayon stubs, or spare coat buttons; sturdy painted metal biscuit boxes turn swiftly into neat treasure chests for shiny marbles or sewing threads; chipped clay flowerpots "
            "bloom cheerfully again holding fragrant kitchen mint sprigs after quick bright brush strokes! Even washed wide plastic curd tubs or trimmed bottle bases serve nicely as sunny windowsill seed-starting cups "
            "when kept cleanly out of sun decay! Why does creative reusing shield our green Earth far better than tossing items away after single use? Every reused clear glass jar, repaired wooden classroom stool, "
            "or stout strong metal tin spares underground mineral ores from heavy mining, spares green forest trees from sharp axes, and saves smoky factory furnace energy! Observant young inventors discover bright new helpful daily futures hiding quietly inside simple everyday kitchen jars, stout tins, and colorful sturdy cardboard boxes!"
        ),
        "checkpoints": [
            {
                "question": "What does practicing the Second Rule — 'Reuse' — encourage children and families to do with finished jars or boxes?",
                "options": [
                    "Wash and repurpose sturdy jars, tins, and cartons repeatedly for storage, crafts, or seedling planters cleanly",
                    "Smash every finished glass bottle along park footpaths",
                    "Discard sturdy biscuit tins immediately after eating the last cookie",
                    "Burn cardboard gift boxes inside dark garden corners"
                ],
                "answer": 0,
                "hint": "Find a second helpful job for durable clean containers before tossing!",
                "explanation": "Reusing clean glass jars, tin boxes, and sturdy containers shrinks garbage volume and reduces demand for newly manufactured packaging."
            },
            {
                "question": "Why does repairing a loose wooden chair leg or reusing a jam jar protect Earth's resources cleanly?",
                "options": [
                    "Because extending item life saves fresh trees, mined ores, factory energy, and keeps waste out of dumps",
                    "Because old jars magically generate extra rainwater inside",
                    "Because broken chair legs dissolve into fertile compost overnight",
                    "Repairing furniture increases black burning plastic smoke"
                ],
                "answer": 0,
                "hint": "If we reuse or repair what we own, factories need not cut new timber or mine new metal!",
                "explanation": "Repairing and reusing goods prevents wasteful resource extraction, factory pollution, and premature landfill accumulation."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch12 Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 7: Water - A Precious Gift
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
        "title": "Watching Rain Clouds",
        "subtitle": "Observing Sky Clues to Forecast Rainy Weather",
        "speech": (
            "Welcome, young weather watchers, to our exciting scientific exploration of water—one of Earth's most precious gifts! "
            "Every monsoon season begins with captivating signals painted right across the open sky above our rooftops and fields. "
            "Have you ever noticed how the atmosphere changes right before a refreshing rainstorm arrives? By stepping outside and "
            "carefully examining sky clues, curious learners can forecast upcoming rainfall just like skilled meteorologists! First, look upward "
            "at the shifting clouds. Bright, fluffy white cumulus clouds drifting gently across a vivid blue sky normally indicate pleasant, "
            "sunny, and dry conditions. However, when towering, heavy, charcoal-gray nimbus clouds gather together and block warm sunlight, "
            "they carry millions of condensed water droplets ready to pour downward. Next, feel the blowing breeze against your skin. A sudden "
            "cool, damp, earthy gust often heralds approaching rain clouds, bringing along the wonderful scent of wet soil called petrichor! "
            "Even neighborhood animals sense dropping air pressure—dragonflies and swallows fly closer to the ground, frogs croak loudly near "
            "ditches, and ants hurry back into high ground nests. By carefully combining cloud colors, wind shifts, temperature drops, and "
            "creature behavior, students gain reliable tools to accurately predict when the clouds will finally open up to water our thirsty planet."
        ),
        "checkpoints": [
            {
                "question": "Which type of cloud signal usually indicates that heavy rain is about to fall soon?",
                "options": [
                    "Thin wispy white streaks high in a bright blue sky",
                    "Tall, dark charcoal-gray heavy clouds blocking the sun",
                    "Completely cloudless clear golden afternoon skies",
                    "Tiny isolated cotton-ball puffs floating high up"
                ],
                "answer": 1,
                "hint": "Dark clouds are packed thick with heavy condensed water droplets.",
                "explanation": "Dark charcoal-gray clouds (nimbus clouds) hold dense moisture and block sunlight, signaling impending rainfall."
            },
            {
                "question": "What environmental clue do we feel on our skin right before a rainstorm starts?",
                "options": [
                    "A dry scorching desert heatwave",
                    "A sudden cool, damp, humid breeze",
                    "Zero wind and freezing snow",
                    "Salty sea spray inside inland classrooms"
                ],
                "answer": 1,
                "hint": "Rain clouds push cool moisture-rich air ahead of the storm.",
                "explanation": "Approaching rain systems drive cool, humid breezes ahead of the downpour, lowering outdoor air temperature."
            }
        ]
    },
    {
        "id": 2,
        "title": "Weekly Weather Logs",
        "subtitle": "Tracking Daily Sky Observations and Rain Patterns Across Seven Days",
        "speech": (
            "Keeping systematic records turns casual nature glances into genuine scientific discovery! Over a full seven-day week, student "
            "observers can monitor sky transformations every morning and afternoon from their schoolyard or home balcony. In a structured "
            "weather log table, learners note the date, cloud cover color, wind speed, sunshine intensity, and their personal rainfall "
            "prediction before checking whether rain actually occurred! Some days start crisp and sunlit with bright golden warmth, leading "
            "to accurate predictions of dry weather where wet laundry dries briskly on clotheslines. Other humid mornings begin with hazy, "
            "still air and gray overcast skies rolling in from the horizon by midday, signaling high humidity and probable afternoon showers. "
            "Recording both accurate forecasts and surprising misses builds critical thinking skills! Why did thick gray clouds drift past "
            "without dropping rain on Tuesday? Perhaps high-altitude winds blew the moist clouds toward nearby hills before droplets grew heavy "
            "enough to fall! Tracking weekly patterns reveals that weather is never random; it follows physical cycles driven by solar heat, "
            "evaporating water vapor, and swirling winds. Maintaining neat seven-day weather calendars helps communities prepare for monsoon "
            "planting, protect harvested grains outdoors, and appreciate the dynamic atmosphere nourishing every farm, forest, and river valley."
        ),
        "checkpoints": [
            {
                "question": "Why should students record weather observations across an entire seven-day week instead of just one hour?",
                "options": [
                    "To decorate notebooks with random stickers",
                    "To discover recurring sky patterns and test whether weather predictions succeed",
                    "Because clouds only appear on Sundays",
                    "To measure how fast paint dries indoors"
                ],
                "answer": 1,
                "hint": "Science relies on comparing repeated observations over time.",
                "explanation": "Seven-day tracking reveals clear links between sky clues, humidity, wind shifts, and actual rainfall outcomes."
            },
            {
                "question": "What happens if heavy gray clouds appear overhead, but strong winds push them away quickly?",
                "options": [
                    "Rain might fall in a neighboring valley or hill instead of your home",
                    "The clouds instantly freeze into solid ice blocks",
                    "Sunlight disappears for an entire month",
                    "Rivers immediately flow backward uphill"
                ],
                "answer": 0,
                "hint": "Wind carries clouds horizontally across landscapes.",
                "explanation": "High-altitude winds transport rain-bearing clouds away before droplets release, depositing rain elsewhere."
            }
        ]
    },
    {
        "id": 3,
        "title": "Studying Raindrops Closely",
        "subtitle": "Comparing Rain Intensity, Droplet Size, Speed, and Wind Angles",
        "speech": (
            "Once rain finally begins tapping against windowpanes and metal roofs, let us closely investigate the fascinating physical behavior "
            "of falling rainwater! Not all rainfall looks, sounds, or behaves identically. By watching safely from a covered wooden verandah or porch, "
            "curious student scientists can compare light drizzles against roaring monsoon downpours. Notice droplet size and spacing first! "
            "During a gentle drizzle, misty micro-droplets float slowly downward, producing soft whispers on green mango leaves and leaving tiny "
            "widely spaced dots on dusty stone courtyards. Contrast this with a heavy tropical downpour, where giant, heavy raindrops plunge "
            "rapidly through the air, drumming thunderously on rooftops, churning mud puddles into dancing bubbles, and splashing brightly off "
            "wet pavements! Look carefully at the falling angle of raindrops as well. On calm, windless afternoons, gravity pulls every raindrop "
            "straight downward in crisp vertical lines. However, whenever gusty winds sweep sideways across the yard, falling droplets slant "
            "dramatically at diagonal angles—forcing pedestrians to tilt umbrellas firmly into the blowing wind! Listening to changing rain rhythms on metal "
            "sheets versus leafy trees, timing how fast puddles fill, and measuring slant angles turn every rainy afternoon into an astonishing, "
            "hands-on physics laboratory right outside our front doors."
        ),
        "checkpoints": [
            {
                "question": "Why do falling raindrops often travel at slanted diagonal angles instead of straight vertical lines?",
                "options": [
                    "Clouds tilt sideways to empty their buckets",
                    "Strong horizontal winds blow the falling raindrops sideways",
                    "Gravity stops pulling downward during storms",
                    "Trees push raindrops away with their branches"
                ],
                "answer": 1,
                "hint": "Think about what force pushes against droplets from the side.",
                "explanation": "Gravity pulls droplets straight down while sideways wind pushes them horizontally, resulting in a slanted diagonal path."
            },
            {
                "question": "How does a heavy downpour differ visibly from a light gentle drizzle?",
                "options": [
                    "Downpours feature larger droplets falling rapidly with noisy splashes and puddles",
                    "Drizzles break tree branches with huge water volumes",
                    "Downpours happen only when the sun is shining brightly",
                    "Drizzles create roaring floods within two seconds"
                ],
                "answer": 0,
                "hint": "Compare droplet size, falling speed, and sound intensity.",
                "explanation": "Heavy downpours drop large, fast-moving raindrops that splash vigorously and quickly fill ground puddles."
            }
        ]
    },
    {
        "id": 4,
        "title": "Testing Rainwater Purity",
        "subtitle": "Collecting Open Sky Rainwater Versus Roof Runoff Samples",
        "speech": (
            "Have you ever wondered whether falling rainwater is naturally clean or carries hidden specks? Let us conduct an illuminating "
            "collection experiment right in the open courtyard! Take two sparkling clean glass jars or wide steel bowls outdoors during a "
            "steady rainstorm. Place the first jar on an open wooden stool directly beneath clear skies, safely away from overhanging tree "
            "branches or house roofs. Place the second jar directly underneath a rooftop drainpipe or sloping tiled roof eaves. Wait twenty "
            "minutes, bring both containers inside into bright light, and inspect them closely! Look at the first jar filled directly from "
            "open clouds: the water appears remarkably crystal-clear, colorless, and odorless, though early drops may rinse tiny floating dust "
            "particles out of city air. Now observe the second jar collected from roof runoff: it often looks slightly muddy, brownish, or "
            "speckled with fallen leaf bits, bird droppings, soot, and roof dust! This simple comparison teaches an essential public health "
            "lesson about rainwater harvesting. Rainwater formed high inside clouds is naturally fresh and pure, yet it picks up surface dirt "
            "whenever it washes across dusty roofs, polluted streets, or dirty gutters—reminding us always to filter and boil harvested "
            "water before drinking it safely."
        ),
        "checkpoints": [
            {
                "question": "Why does rainwater collected directly from a rooftop drainpipe look dirtier than water caught in an open field jar?",
                "options": [
                    "Roof water picks up settled dust, dry leaf fragments, and soot off the roof surface",
                    "Raindrops change color when passing near metal pipes",
                    "Sky rain falls brown in cities and clear in villages",
                    "Open field jars magically boil water inside"
                ],
                "answer": 0,
                "hint": "Think about what settles on house roofs during dry sunny weeks.",
                "explanation": "Water running down roofs washes along accumulated dust, dried leaves, and surface dirt into the drainpipe."
            },
            {
                "question": "What should communities do with harvested rainwater stored from rooftops before using it for drinking?",
                "options": [
                    "Add colorful paint to mask any dirt",
                    "Discard the first dirty flush, then properly filter and boil or purify the water",
                    "Drink it immediately without checking clarity",
                    "Pour soap inside the drinking storage tank"
                ],
                "answer": 1,
                "hint": "Safe drinking water must be free from surface germs and particles.",
                "explanation": "Discarding first roof-wash runoff and filtering plus boiling removes particulate dirt and harmful microbes."
            }
        ]
    },
    {
        "id": 5,
        "title": "Soil Soaking Rainwater",
        "subtitle": "How Porous Earth Absorbs Rain to Recharge Wells and Groundwater",
        "speech": (
            "Once millions of sparkling raindrops strike the ground below, where does all that abundant water vanish? The answer depends "
            "entirely on the surface beneath our feet! Let us compare soft, porous garden soil against hard, sealed concrete pavements. "
            "When rain lands on natural meadows, forest mulch, sandy riverbanks, or plowed farm fields, water slowly seeps downward through "
            "tiny microscopic gaps between sand, silt, and soil grains. This wonderful downward soaking process is called percolation! Deeper "
            "and deeper the clean rainwater trickles, passing naturally through layers of gravel and sand that filter out impurities, until it "
            "collects in vast hidden underground rock sponges known as aquifers. This precious underground water table feeds village open wells, "
            "deep tube wells, stepwells, and hillside springs throughout dry scorching summer months! Conversely, what occurs when rain strikes "
            "tarred roads, tiled courtyards, and solid concrete cities? Sealed surfaces completely block water from soaking into the earth! "
            "Instead, rainwater rushes furiously across hard concrete into clogged storm drains and floods low streets while leaving underground aquifers "
            "thirsty. By preserving grassy parks, sandy walkways, and rainwater recharge pits around school buildings, thoughtful humans help rainwater "
            "soak gently underground—replenishing Earth's hidden freshwater bank account for future generations."
        ),
        "checkpoints": [
            {
                "question": "What happens when rainwater falls onto soft soil, garden beds, and sandy earth?",
                "options": [
                    "It bounces back upward into the clouds immediately",
                    "It seeps downward through soil gaps to recharge underground groundwater and wells",
                    "It freezes into solid stone boulders",
                    "It turns soil into waterproof concrete"
                ],
                "answer": 1,
                "hint": "Soil acts like a giant natural sponge allowing percolation.",
                "explanation": "Porous soil allows rainwater to percolate downward, naturally filtering it and replenishing groundwater tables and wells."
            },
            {
                "question": "Why do modern cities paved heavily with concrete and tar experience flash flooding and dry wells?",
                "options": [
                    "Concrete clouds produce zero rain",
                    "Hard paved surfaces block rainwater from soaking into the ground, forcing rapid runoff",
                    "Underground soil drinks ocean salt water instead",
                    "Trees absorb all street concrete"
                ],
                "answer": 1,
                "hint": "Can water pass easily through sealed concrete floors?",
                "explanation": "Waterproof tar and concrete prevent soil absorption, causing surface flooding above while starving underground water reserves."
            }
        ]
    },
    {
        "id": 6,
        "title": "Streams To Oceans",
        "subtitle": "Tracing Surface Runoff Through Puddles, Streams, Rivers, and Seas",
        "speech": (
            "Not every raindrop slips vertically underground; vast quantities flow triumphantly across the surface of our planet in an "
            "unforgettable geographical journey! Right after heavy downpours finish, watch how miniature streams form along sloping hills "
            "and roadside slopes. First, tiny rain trickles fill shallow stone hollows and dusty indentations to form shimmering puddles where "
            "sparrows splash happily and children float delicate paper boats. As overflow spills out of brimming puddles and hillside gullies, "
            "water merges into bubbling, rapid mountain brooks and narrow streams winding down rocky valleys. Downstream, dozens of lively "
            "tributary streams unite into broad, mighty, shimmering rivers—like the sacred Ganga, Godavari, Narmada, or Kaveri—carrying fresh "
            "water across fertile agricultural plains toward thirsty cities and forests! Along the way, depressions in the landscape trap "
            "flowing runoff into tranquil village ponds and expansive freshwater lakes supporting lotus flowers, fish, and wading herons. "
            "Ultimately, after traveling hundreds or thousands of kilometers across rocky plateaus and broad deltas, rivers empty their accumulated fresh "
            "waters into immense salty seas and sprawling oceans covering most of Earth. Under bright golden sunshine, open ocean surfaces warm gently and "
            "evaporate skyward again as invisible water vapor that cools into towering clouds—completing the timeless, magnificent circular water cycle for every creature on land!"
        ),
        "checkpoints": [
            {
                "question": "Which sequence correctly traces the natural downhill surface path of flowing rainwater?",
                "options": [
                    "Oceans -> Rivers -> Puddles -> Streams",
                    "Puddles -> Small Streams -> Broad Rivers -> Seas and Oceans",
                    "Wells -> Clouds -> Oceans -> Leaves",
                    "Seas -> Lakes -> Raindrops -> Soil"
                ],
                "answer": 1,
                "hint": "Water always flows from tiny collection spots downhill into larger bodies.",
                "explanation": "Rainwater collects in small puddles, merges into downhill streams, joins major rivers, and finally empties into seas and oceans."
            },
            {
                "question": "How does water in ponds, rivers, and vast oceans eventually return upward into the sky to form new rain clouds?",
                "options": [
                    "Birds carry droplets upward in buckets",
                    "Sun's heat warms surface water, evaporating it into invisible water vapor rising skyward",
                    "Trees pump ocean water through their branches into space",
                    "Fish splash water upward ten kilometers high"
                ],
                "answer": 1,
                "hint": "Think about what causes wet clothes or puddles to vanish under warm sunshine.",
                "explanation": "Solar warmth turns liquid surface water into rising invisible water vapor (evaporation), which cools high up to condense into rain clouds."
            }
        ]
    },
    {
        "id": 7,
        "title": "Home Water Pipes",
        "subtitle": "Tracing Water Flow From Overhead Tanks Through Plumbing Pipes to Taps",
        "speech": (
            "Turning a shining kitchen faucet brings cool, clean water flowing out effortlessly within a fraction of a second—yet an ingenious "
            "engineering network delivers every single drop! Let us trace how municipal water travels into urban homes and bustling schools. "
            "Large pumps at regional water treatment stations first purify raw river or reservoir water, removing mud, floating debris, and "
            "harmful microbes before propelling clean water through thick underground main pipelines beneath neighborhood roads. Branch pipes "
            "climb upward along house walls to fill sturdy overhead storage tanks perched high atop building rooftops! Why do architects and "
            "plumbers always place storage tanks high on the roof instead of under the ground floor? The answer lies in simple gravity! "
            "Because water sitting high above rooms possesses downward gravitational pressure, opening any tap downstairs allows water to rush "
            "downward naturally through vertical supply pipes into bathroom showers, kitchen sinks, school drinking fountains, and garden hoses "
            "without needing continuous noisy motors. Check the joints and taps inside your home too: sealed metal or PVC pipelines ensure "
            "precious purified water never mixes with dirty outside drains, reminding us how modern plumbing keeps drinking water safe, crisp, "
            "and conveniently accessible right inside every family household."
        ),
        "checkpoints": [
            {
                "question": "Why are municipal and household water storage tanks usually placed high atop building rooftops?",
                "options": [
                    "So birds can swim inside them",
                    "Gravity pushes stored water downward through pipes smoothly whenever taps open below",
                    "Rainwater only lands on high plastic tanks",
                    "Because ground floors have zero space for pipes"
                ],
                "answer": 1,
                "hint": "Water naturally flows from higher elevation to lower elevation.",
                "explanation": "Elevated rooftop tanks utilize downward gravity pressure to push water swiftly through plumbing pipes to all lower-floor taps."
            },
            {
                "question": "What crucial process happens at a water treatment plant before river water enters city home pipelines?",
                "options": [
                    "Sugar and salt are stirred into the water",
                    "Water is thoroughly filtered and purified to remove mud and disease-causing germs",
                    "Water is frozen into giant solid icebergs",
                    "Pipes are filled with rainwater directly from muddy puddles"
                ],
                "answer": 1,
                "hint": "Water straight from open rivers contains mud and bacteria.",
                "explanation": "Treatment plants filter away sediments and disinfect harmful microbes so safe, clean water reaches household drinking taps."
            }
        ]
    },
    {
        "id": 8,
        "title": "Village Water Sources",
        "subtitle": "Drawing Water via Wells, Pulleys, Hand Pumps, Motors, and Tankers",
        "speech": (
            "While overhead pipe networks serve many neighborhoods, millions of families across India gather daily drinking water from "
            "diverse, resourceful local sources! Venture out into rural villages, hilly hamlets, and outer towns to witness amazing traditional "
            "and modern water-lifting engineering. Deep stone-lined open wells tap directly into cool underground aquifers. To lift heavy "
            "buckets filled with water upward effortlessly, people mount grooved circular wheels called pulleys above the well rim, smoothly "
            "changing downward pulling effort into upward lifting motion! Nearby, sturdy iron hand pumps dot village squares and rural "
            "schoolyards. Moving the long iron lever handle up and down operates internal suction valves, pulling clean, filtered groundwater "
            "upward through narrow deep pipes straight out of the spout—completely free of electricity! In deeper wells or modern farms, "
            "electric submersible pumps spin rapidly underground to lift water briskly to crops and village tanks. Meanwhile, in arid desert "
            "regions or steep mountain neighborhoods lacking local wells during parched summer months, bright yellow municipal water tankers roll down dusty roads "
            "carrying emergency drinking supplies, while hardworking families sometimes walk rocky miles carrying gleaming brass or clay pots balanced gracefully "
            "atop their heads to bring every precious liter safely back home."
        ),
        "checkpoints": [
            {
                "question": "How does a grooved pulley wheel mounted over an open well help people draw heavy water buckets?",
                "options": [
                    "It makes the water inside the bucket evaporate faster",
                    "It redirects your downward pull smoothly into an upward lift, reducing strain",
                    "It converts groundwater into salty sea water",
                    "It runs on solar electricity stored inside stones"
                ],
                "answer": 1,
                "hint": "Pulling downward with your body weight is much easier than hauling straight upward.",
                "explanation": "A pulley wheel changes pull direction so a person can pull downward comfortably to raise a heavy water bucket upward."
            },
            {
                "question": "Which water-drawing machine lifts clean underground water purely by muscle power without requiring electricity?",
                "options": [
                    "An electric submersible motor",
                    "An iron lever hand pump",
                    "A rooftop diesel generator",
                    "A municipal tanker truck"
                ],
                "answer": 1,
                "hint": "Think of the iron lever found in rural courtyards and village schools.",
                "explanation": "Manual hand pumps use a lever and internal suction valves to draw clean groundwater purely through human muscle force."
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

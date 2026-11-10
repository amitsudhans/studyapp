# generate_c4s_ch7_part2.py
# Generates Slides 9 to 16 for Class 4 Science Chapter 7: How Things Work
# Target speech word count: strictly 195 to 215 words

slides_part2 = [
    {
        "id": 9,
        "title": "Shape Affects Flotation",
        "badge": "Structural Buoyancy",
        "description": "Perform the classic aluminium foil experiment, discovering how changing an object's geometry alters overall density and buoyant upthrust.",
        "sim_id": "sim-9",
        "sim_title": "Aluminium Foil Geometry & Buoyancy Chamber",
        "speech": (
            "One of the most remarkable discoveries in physical science is that whether an object floats or sinks is not permanently locked into the material "
            "itself, but can be radically transformed simply by re-engineering its geometric shape. Consider a standard sheet of metallic aluminium foil. If we take "
            "this thin sheet and gently lay it flat across the water's surface, it floats effortlessly like a miniature raft. If we fold the foil edges upward "
            "into the shape of a hollow cup or rectangular canoe, it floats even higher, capable of carrying small pebble passengers. However, if we take that exact "
            "same piece of foil and crumple it tightly between our palms, hammering and rolling it into a solid, compact metal pellet, something astonishing happens: "
            "when dropped into water, it plunges straight to the bottom and sinks. The mass of aluminium remained completely identical throughout the experiment, "
            "yet its behavior reversed. Why? When spread out or shaped into a hollow bowl, the foil encompasses a large volume filled with light air, dramatically "
            "lowering its overall average density below that of water while displacing substantial fluid. When compressed into a dense pellet, all buoyant air pockets are expelled, "
            "causing its density to exceed water's density and sink immediately."
        ),
        "checkpoints": [
            {
                "q": "Why does a flat or bowl-shaped piece of aluminium foil float, while the same foil crushed into a tight ball sinks?",
                "options": [
                    "The hollow bowl shape encloses air and has high volume, lowering its average density below water",
                    "The crushed ball absorbs water like a sponge",
                    "Aluminium chemically changes into lead when crushed",
                    "Water pushes sideways instead of upwards"
                ],
                "ans": "The hollow bowl shape encloses air and has high volume, lowering its average density below water",
                "explanation": "Shaping the foil into a hollow hull creates large volume with trapped air, lowering average density and maximizing buoyant upthrust."
            },
            {
                "q": "What happens to the total mass of the aluminium foil when it is crushed from a sheet into a tight ball?",
                "options": [
                    "The total mass remains exactly the same, but its volume decreases sharply",
                    "The mass multiplies by ten times",
                    "The mass disappears into heat energy",
                    "The foil becomes completely weightless"
                ],
                "ans": "The total mass remains exactly the same, but its volume decreases sharply",
                "explanation": "Mass is conserved; only the volume decreases, which increases density (mass/volume) and causes the compressed pellet to sink."
            }
        ]
    },
    {
        "id": 10,
        "title": "Displacement And Buoyancy",
        "badge": "Water Displacement",
        "description": "Investigate how submerged objects push water aside, discovering that the weight of displaced water generates the upward buoyant force.",
        "sim_id": "sim-10",
        "sim_title": "Archimedes Displacement Beaker Lab",
        "speech": (
            "To understand how massive steel ships weighing thousands of tons sail safely across oceans while tiny iron nails sink to the seabed, we must explore "
            "the scientific principle of fluid displacement. When any solid object enters a full container of water, it pushes aside an amount of water exactly equal "
            "to the volume of the object submerged beneath the surface. This pushed-aside fluid is called displaced water. In response, the surrounding water pushes back upward "
            "against the object with a powerful lifting force known as buoyant upthrust. The magnitude of this upward buoyant force is exactly equal to the weight of the "
            "displaced water. A tiny solid iron nail has a very small volume, so it displaces only a few droplets of water. The weight of those few displaced droplets "
            "is far too weak to support the heavy weight of the nail, causing it to sink rapidly. In contrast, an ocean liner or a wide hollow steel bowl has a vast "
            "internal air cavity. As it rests in water, its broad hull pushes aside an enormous volume of water. The weight of this displaced water easily equals the "
            "total weight of the ship, allowing it to float serenely and securely with towering confidence."
        ),
        "checkpoints": [
            {
                "q": "What determines the strength of the upward buoyant force acting on an object placed in water?",
                "options": [
                    "The weight of the water displaced by the submerged part of the object",
                    "The color of the paint applied to the outside of the object",
                    "The atmospheric temperature of the clouds overhead",
                    "The speed of the wind blowing across the surface"
                ],
                "ans": "The weight of the water displaced by the submerged part of the object",
                "explanation": "Archimedes' principle states that the upward buoyant force exerted on an immersed body equals the weight of fluid displaced by the body."
            },
            {
                "q": "How can a heavy steel bowl float on water when a small solid steel ball sinks?",
                "options": [
                    "The hollow bowl shape displaces a large volume of water whose upward buoyant weight supports the bowl",
                    "The bowl is made of magical anti-gravity metal",
                    "The steel ball is attracted to underwater magnets",
                    "Water prefers curved objects over spherical objects"
                ],
                "ans": "The hollow bowl shape displaces a large volume of water whose upward buoyant weight supports the bowl",
                "explanation": "A wide bowl pushes aside a large mass of water, creating an upward buoyant force greater than or equal to its own weight."
            }
        ]
    },
    {
        "id": 11,
        "title": "Crafting Model Boats",
        "badge": "Design Challenge",
        "description": "Engage in Activity 5 hands-on boat engineering, selecting lightweight materials like cardboard, popsicle sticks, and waterproof wax barriers.",
        "sim_id": "sim-11",
        "sim_title": "Hands-On Model Boat Workshop",
        "speech": (
            "Class 4 Science Activity 5 invites enthusiastic young engineers into the creative boat-making challenge, directly applying foundational scientific principles "
            "of buoyancy, waterproofing, and structural balance. Students work collaboratively in busy classroom teams using a vibrant assortment of everyday craft materials—including stiff cardboard cartons, "
            "wooden ice-cream popsicle sticks, lightweight thermocol blocks, malleable modeling clay, and colorful origami paper. Each material presents unique mechanical advantages and scientific challenges. "
            "Traditional folded paper boats are quick and easy to construct, yet untreated cellulose paper rapidly absorbs water through microscopic capillary action, becoming soggy, "
            "waterlogged, and prone to capsizing within minutes. To engineer a truly seaworthy model boat, students learn to coat paper and cardboard hulls with protective waterproof barriers, "
            "such as rubbing colored wax crayons across the exterior or applying thin layers of edible oil. Wooden popsicle sticks provide rigid structural ribs, and because dry wood has an "
            "intrinsic density lower than liquid water, it adds reliable natural buoyancy to the vessel. By designing wide, flat-bottomed rectangular rafts or pointed canoe hulls, children discover "
            "how geometry and material science cooperate to create sturdy floating craft that resist tipping over, demonstrating that real engineering begins with deeply understanding the physical properties of matter."
        ),
        "checkpoints": [
            {
                "q": "Why does an ordinary paper boat eventually become waterlogged, tip over, and sink in a puddle?",
                "options": [
                    "Paper fibers absorb water through capillary action, increasing overall weight and weakening structural stiffness",
                    "Water eats the paper like hungry acid",
                    "The sun melts the paper into vapor",
                    "The paper transforms into heavy stone after five minutes"
                ],
                "ans": "Paper fibers absorb water through capillary action, increasing overall weight and weakening structural stiffness",
                "explanation": "Porous cellulose fibers in untreated paper soak up water, adding mass and causing the hull to sag, leak, and capsize."
            },
            {
                "q": "How can students waterproof a homemade paper or cardboard model boat to extend its floating time?",
                "options": [
                    "Coating the exterior surface with wax crayons or a light film of oil to repel water molecules",
                    "Punching dozens of tiny holes through the bottom hull with pins",
                    "Soaking the boat in hot water before placing it in the pond",
                    "Adding five heavy iron nails to the bow"
                ],
                "ans": "Coating the exterior surface with wax crayons or a light film of oil to repel water molecules",
                "explanation": "Wax is hydrophobic (water-repelling), preventing water from penetrating porous cardboard and keeping the boat lightweight and buoyant."
            }
        ]
    },
    {
        "id": 12,
        "title": "Natural Shell Vessels",
        "badge": "Bio-Inspired Hulls",
        "description": "Explore nature's readymade boats by testing walnut half-shells, coconut shells, and hollow seed pods for natural buoyancy and balance.",
        "sim_id": "sim-12",
        "sim_title": "Botanical Shell Vessel Flotation Basin",
        "speech": (
            "Nature is the supreme master architect of floating structures, offering ingenious designs that inspire modern maritime engineering. When curious students explore natural organic materials "
            "in Class 4 Science, they test nature's ingenious readymade boats: halved walnut shells, dried coconut husks, and seed pods. A halved walnut shell is truly an exquisite marvel of botanical architecture "
            "and design. Its tough outer shell is made of dense cellulose, yet its hollow hemispherical bowl encompasses a generous pocket of air. When placed gently in water, the walnut shell floats "
            "buoyantly like a miniature fairy boat, rocking gracefully without capsizing. By attaching a tiny paper sail to a toothpick mast with a dab of natural clay at the center bottom, "
            "children create a fully functional sailboat that catches gentle breezes. Similarly, a halved coconut shell, with its thick fibrous air-trapping coir husk and wide circular bowl, can support "
            "substantial cargo weight before sinking. Remarkable plants evolved these buoyant, waterproof seed vessels over millions of years to disperse their precious seeds across winding rivers and oceans "
            "to distant shores. By studying botanical shells, young learners discover biomimicry—the practice of learning from nature's brilliant evolutionary designs to solve real-world human engineering challenges with sustainability and grace."
        ),
        "checkpoints": [
            {
                "q": "Why does a halved walnut shell float so effortlessly and stably on the surface of water?",
                "options": [
                    "Its curved, hollow bowl encloses buoyant air while its lightweight fibrous hull displaces sufficient water",
                    "Walnut shells are filled with helium gas inside the wood",
                    "The water surface acts like a solid magnet pushing the nut upwards",
                    "Walnuts are lighter than air itself"
                ],
                "ans": "Its curved, hollow bowl encloses buoyant air while its lightweight fibrous hull displaces sufficient water",
                "explanation": "The hollow hemispherical structure provides high internal volume with low weight, achieving excellent buoyancy and water displacement."
            },
            {
                "q": "Why did plants like coconuts and water lilies naturally evolve buoyant, waterproof floating fruits and shells?",
                "options": [
                    "To travel across rivers and ocean currents, dispersing seeds to colonize new shorelines",
                    "To hide underground away from direct sunlight",
                    "To feed underwater deep-sea sharks exclusively",
                    "To freeze water into solid ice blocks"
                ],
                "ans": "To travel across rivers and ocean currents, dispersing seeds to colonize new shorelines",
                "explanation": "Hydrochory is the botanical adaptation where seeds use buoyant, water-resistant hulls to travel across water bodies to germinate elsewhere."
            }
        ]
    },
    {
        "id": 13,
        "title": "Boat Stability Dynamics",
        "badge": "Naval Architecture",
        "description": "Investigate why boats tip or stay upright, exploring hull width, center of gravity, and bottom ballasting to prevent dangerous capsizing.",
        "sim_id": "sim-13",
        "sim_title": "Hull Stability & Metacentric Angle Rig",
        "speech": (
            "Building a model boat that floats is only the first step in naval engineering; the greater scientific triumph is designing a vessel that remains upright, balanced, "
            "and resistant to capsizing when buffeted by waves or wind. In our classroom testing basin, students quickly observe that narrow, tall boats tip sideways and flip over "
            "at the slightest disturbance. This stability puzzle is governed by the relative positions of two critical physical points: the center of gravity and the center of buoyancy. "
            "The center of gravity is the point where the entire downward weight of the boat is concentrated, while the center of buoyancy is the focal point of the upward water push. "
            "If a boat has heavy cargo mounted high up on deck, its center of gravity rises precariously. When tilted by a small wave, the high center of gravity creates a tipping torque "
            "that flips the hull upside down. Conversely, wide-bottomed boats with heavy ballast placed firmly at the lowest point of the hull have an exceptionally low center of gravity. "
            "When tilted, the water exerts an immediate restoring torque that pops the boat back upright, demonstrating how naval architects ensure the safety of sea vessels."
        ),
        "checkpoints": [
            {
                "q": "What design modification makes a model boat most resistant to tipping over and capsizing in rough water?",
                "options": [
                    "A wide, flat-bottomed hull with heavy ballast placed at the lowest point inside the keel",
                    "Making the boat extremely narrow and stacking all heavy cargo on the top deck",
                    "Removing all air from inside the boat hull",
                    "Painting the boat with fluorescent red stripes"
                ],
                "ans": "A wide, flat-bottomed hull with heavy ballast placed at the lowest point inside the keel",
                "explanation": "A wide beam and low ballast keep the center of gravity near the bottom, creating a strong righting torque that prevents capsizing."
            },
            {
                "q": "What dangerous mechanical effect occurs when heavy cargo is loaded high above the deck of a boat?",
                "options": [
                    "The center of gravity rises dangerously, making the boat unstable and prone to flipping over",
                    "The boat flies straight up into the clouds",
                    "The water underneath the boat turns into stone",
                    "The boat travels ten times faster automatically"
                ],
                "ans": "The center of gravity rises dangerously, making the boat unstable and prone to flipping over",
                "explanation": "High center of gravity creates an unstable equilibrium where slight tilting generates roll momentum that capsizes the vessel."
            }
        ]
    },
    {
        "id": 14,
        "title": "Load Capacity Testing",
        "badge": "Payload Physics",
        "description": "Conduct Activity 5 load tests by systematically placing metal coins or marbles inside model boats to measure maximum carrying capacity.",
        "sim_id": "sim-14",
        "sim_title": "Load Capacity & Plimsoll Waterline Tank",
        "speech": (
            "During the classroom model boat exhibition, students engage in one of the most exciting scientific challenges: testing the maximum cargo capacity of their floating designs. "
            "Using uniform calibrated weights, such as heavy five-rupee metallic coins or identical glass marbles, students carefully load one item at a time into their floating vessels, "
            "observing the hull closely. As each coin is added, the total downward gravitational weight of the boat increases. To remain afloat, the boat must sink slightly deeper into the water, "
            "pushing aside an additional volume of liquid to generate an equal increase in upward buoyant force. The boundary line where the water surface meets the boat's hull is called the waterline. "
            "With every additional coin or marble added, the waterline steadily creeps higher and higher up the exterior walls. If cargo is loaded unevenly on one side, the boat tilts dangerously, "
            "taking in water over the lowered gunwale. Finally, when the total loaded weight exceeds the maximum buoyant force the hull can displace before water spills over the rim, the vessel "
            "inevitably submerges. Real cargo ships feature painted Plimsoll marks on their steel hulls to indicate safe loading limits, connecting simple classroom coin trials directly to modern "
            "international maritime safety engineering."
        ),
        "checkpoints": [
            {
                "q": "What happens to a floating model boat as students add coins one by one into its cargo hold?",
                "options": [
                    "The boat sinks deeper into the water, displacing more liquid to generate greater upward buoyant force",
                    "The boat rises higher out of the water like a flying hovercraft",
                    "The coins dissolve into liquid water",
                    "The water level inside the bucket drops to zero"
                ],
                "ans": "The boat sinks deeper into the water, displacing more liquid to generate greater upward buoyant force",
                "explanation": "Added weight requires additional upward buoyancy to stay afloat, so the hull sinks deeper to displace a greater volume of water."
            },
            {
                "q": "What is the purpose of the historical Plimsoll line painted on the hulls of full-scale commercial cargo ships?",
                "options": [
                    "To show the maximum safe legal waterline depth to prevent overloading and sinking in open seas",
                    "To mark the spot where sailors should paint colorful flowers",
                    "To measure how warm the ocean water is",
                    "To frighten away sea turtles and whales"
                ],
                "ans": "To show the maximum safe legal waterline depth to prevent overloading and sinking in open seas",
                "explanation": "Plimsoll marks indicate the maximum safe depth a vessel can be loaded to in various water densities without risking swamping."
            }
        ]
    },
    {
        "id": 15,
        "title": "Modifying Object Buoyancy",
        "badge": "Buoyancy Control",
        "description": "Discover methods to make sinking objects float and floating objects sink, exploring air chambers, ballast weights, and submarine ballast tanks.",
        "sim_id": "sim-15",
        "sim_title": "Submarine Ballast & Buoyancy Inverter",
        "speech": (
            "In the concluding reflection activities of Chapter 7, students explore how human ingenuity can reverse the natural buoyancy of everyday objects, transforming "
            "sinkers into floaters and floaters into sinkers. Consider a solid lump of dense modeling clay. Dropped as a solid spherical ball, it sinks like a stone immediately. "
            "Yet if we press our thumbs into the clay, kneading and stretching it into a broad, hollow, thin-walled bowl with high rims, it floats triumphantly, supporting several metallic coins. "
            "By deliberately trapping a large volume of air inside its hollow contour, we drastically reduce its overall average density below water's liquid density. Conversely, how can we make "
            "a naturally buoyant object sink? A light plastic bottle floats effortlessly when completely empty, bobbing gently on the surface. But if we open the cap, fill it completely with water "
            "and heavy sand, and cap it again, the displaced air is replaced by dense material, causing the bottle to sink to the bottom. This exact scientific mechanism powers modern submarines. "
            "To dive beneath the ocean, submarines flood their ballast tanks with sea water; to resurface, powerful high-pressure pumps blast compressed air into the tanks, blowing the water out "
            "to restore positive buoyancy."
        ),
        "checkpoints": [
            {
                "q": "How can a ball of modeling clay that naturally sinks be transformed into a floating object?",
                "options": [
                    "By reshaping the solid ball into a wide, hollow bowl that encloses air and increases volume",
                    "By painting the clay ball bright yellow",
                    "By leaving the clay ball in a freezer for twenty minutes",
                    "By cutting the clay ball into two smaller solid balls"
                ],
                "ans": "By reshaping the solid ball into a wide, hollow bowl that encloses air and increases volume",
                "explanation": "Reshaping into a hollow bowl increases the volume and trapped air, dramatically lowering the overall density below that of water."
            },
            {
                "q": "How does a modern submarine dive underwater and later rise back to the ocean surface?",
                "options": [
                    "It floods ballast tanks with water to sink, and blows compressed air into tanks to float",
                    "It uses giant underwater tractor wheels that roll on the seabed",
                    "It turns off its engine and falls asleep",
                    "It changes its hull from steel into rubber"
                ],
                "ans": "It floods ballast tanks with water to sink, and blows compressed air into tanks to float",
                "explanation": "Controlling water and air in ballast tanks alters the submarine's average density, allowing precise control over sinking and rising."
            }
        ]
    },
    {
        "id": 16,
        "title": "Balanced Mobile Structures",
        "badge": "Center of Gravity",
        "description": "Synthesize chapter principles by analyzing balance toys, hanging mobiles, and equilibrium where the center of gravity hangs beneath the pivot.",
        "sim_id": "sim-16",
        "sim_title": "Equilibrium Mobile & Balancing Bird Rig",
        "speech": (
            "We conclude our rich scientific exploration of how things work by synthesizing rotational stability, center of mass, and equilibrium through balancing toys and hanging mobiles. "
            "A beloved traditional Indian toy is the balancing bird: a colorful plastic bird that perches precariously by the very tip of its beak upon a pencil tip or your outstretched fingertip, "
            "swaying gently in the breeze without ever falling off. How does this seeming magic work? The secret lies in deliberate weight distribution. Inside the bird's forward wingtips "
            "are hidden dense metallic weights. These heavy wingtips curve forward and downward, shifting the bird's entire center of gravity to a position directly beneath the tip of its beak. "
            "In physical mechanics, when an object's center of gravity is located below its support pivot point, the system is in stable equilibrium. If a gentle breeze tilts the bird, gravity "
            "pulls the low weights downward, creating an automatic restoring torque that returns the bird upright. The exact same mechanical principle governs spinning ceiling fans, hanging kinetic art mobiles, "
            "and acrobatic tightrope walkers using long curved balance poles. When human curiosity investigates the physical world, we discover that harmony, balance, and motion operate through universal, dependable scientific laws."
        ),
        "checkpoints": [
            {
                "q": "Why can a toy balancing bird perch upon the very tip of its beak without falling over?",
                "options": [
                    "Heavy weights in its downward-curved wingtips pull the center of gravity below the beak pivot point",
                    "The bird's beak is coated with sticky industrial glue",
                    "Invisible magnets hidden in the ceiling pull the tail upward",
                    "The bird flaps its wings at ultrasonic speeds"
                ],
                "ans": "Heavy weights in its downward-curved wingtips pull the center of gravity below the beak pivot point",
                "explanation": "When an object's center of gravity lies below its pivot support, it is in stable equilibrium; any tilt creates an automatic restoring force."
            },
            {
                "q": "Why do circus tightrope walkers carry long, heavy, downward-curving poles when walking across high wires?",
                "options": [
                    "The heavy curved pole lowers their overall center of gravity and increases rotational inertia against tipping",
                    "The pole acts as an umbrella to keep off rain",
                    "The pole is used to catch birds in the sky",
                    "The pole makes them weigh ten times less"
                ],
                "ans": "The heavy curved pole lowers their overall center of gravity and increases rotational inertia against tipping",
                "explanation": "A long drooping pole lowers the acrobat's center of mass closer to the wire and increases rotational inertia, making balancing much easier."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part2:
        wc = len(s['speech'].split())
        print(f"Slide {s['id']}: '{s['title']}' - Speech words: {wc}")
        assert 195 <= wc <= 215, f"Slide {s['id']} out of bounds: {wc}"
        assert len(s['title'].split()) <= 3, f"Slide {s['id']} title too long: {s['title']}"
        assert len(s['checkpoints']) == 2, f"Slide {s['id']} needs 2 checkpoints"
    print("All slides 9-16 passed checks successfully!")

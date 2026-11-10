# generate_c4s_ch7_part1.py
# Generates Slides 1 to 8 for Class 4 Science Chapter 7: How Things Work
# Target speech word count: strictly 195 to 215 words

slides_part1 = [
    {
        "id": 1,
        "title": "Spinning Objects Motion",
        "badge": "Rotational Mechanics",
        "description": "Observe how everyday objects rotate around a central point, exploring rotational speed, wobble dynamics, and gradual deceleration.",
        "sim_id": "sim-1",
        "sim_title": "Rotational Motion & Wobble Laboratory",
        "speech": (
            "When we spin everyday objects on a flat classroom table—such as a round metallic coin, a plastic bangle, a circular bottle cap, "
            "or a solid wooden top—we observe one of the most fascinating physical phenomena in nature: rotational motion. As long as an object rotates "
            "rapidly, it appears remarkably stable, balanced, and upright, maintaining its orientation in space like a spinning planet. A flat five-rupee coin standing "
            "on its edge would immediately tumble over when stationary, yet when given a brisk twist between our fingers, it spins vigorously, creating "
            "the visual illusion of a three-dimensional translucent sphere. However, this mesmerizing spinning motion does not continue forever. As the object spins, "
            "two relentless opposing physical forces begin acting upon it: contact friction from the tabletop surface beneath its point of contact, and aerodynamic drag from "
            "the surrounding air particles. As rotational energy gradually dissipates into heat and sound, the spinning speed steadily decreases. The upright axis begins to tilt "
            "and trace circular loops in a rhythmic wobbling dance known scientifically as precession. Finally, as momentum vanishes completely, the object makes "
            "a distinctive rattling sound against the desk surface, slows to a gentle halt, and rests flat, demonstrating clearly how physical energy transforms continuously."
        ),
        "checkpoints": [
            {
                "q": "Why does a five-rupee coin stay balanced upright while spinning, but falls flat when stationary?",
                "options": [
                    "Rapid rotational motion generates rotational stability that resists tilting over",
                    "The coin becomes completely weightless when rotating",
                    "Magnetic pull from the ceiling holds the coin upwards",
                    "The air inside the room turns into solid glass"
                ],
                "ans": "Rapid rotational motion generates rotational stability that resists tilting over",
                "explanation": "Spinning objects possess rotational momentum, which creates gyroscopic stability that keeps them upright until friction slows them down."
            },
            {
                "q": "What two physical forces gradually cause a spinning object on a desk to lose speed and stop?",
                "options": [
                    "Surface contact friction and surrounding air resistance",
                    "Electric voltage and direct solar radiation",
                    "Chemical oxidation and magnetic repulsion",
                    "Sound vibrations and atmospheric pressure increase"
                ],
                "ans": "Surface contact friction and surrounding air resistance",
                "explanation": "Contact friction at the pivot point and aerodynamic drag continuously strip away kinetic energy until motion ceases."
            }
        ]
    },
    {
        "id": 2,
        "title": "Rotational Pivot Center",
        "badge": "Center of Mass",
        "description": "Investigate the role of the central pivot axis, discovering why centering a toothpick yields balanced spinning while an off-center pivot wobbles wildly.",
        "sim_id": "sim-2",
        "sim_title": "Pivot Axis Placement Chamber",
        "speech": (
            "Constructing a handmade cardboard spinner teaches children a fundamental scientific truth regarding mechanical balance and the center of mass. If we cut "
            "a neat circle out of thick cardboard and punch a slender toothpick straight through the exact geometric center, the spinner whirls smoothly, quietly, "
            "and effortlessly for an extended duration. This happens because the mass of the cardboard disc is distributed symmetrically in every direction around the central "
            "rotational axis. The centrifugal forces pulling outward balance each other perfectly, allowing the toy to spin with minimal vibration or wobble. In sharp contrast, "
            "if we punch the toothpick even a few millimeters off-center, an immediate physical imbalance occurs. When spun, the unevenly distributed weight creates lopsided "
            "gravitational torque. The heavier side yanks the central spindle sideways with every single revolution, causing violent shaking, extreme wobbling, and sudden tipping. "
            "The uneven contact point grinds fiercely against the tabletop, generating excessive friction that drains kinetic energy within seconds. Through systematic experimentation, young scientists "
            "discover that mechanical stability in all rotating machines—from tiny toy tops to giant industrial wind turbines and jet aircraft engines—depends entirely on aligning "
            "the spinning pivot directly through the object's precise center of mass."
        ),
        "checkpoints": [
            {
                "q": "Why does a cardboard disc spinner with a central toothpick spin smoothly, while an off-center toothpick wobbles rapidly?",
                "options": [
                    "A central pivot ensures symmetrical mass distribution, balancing rotational forces evenly",
                    "The off-center toothpick becomes three times heavier when spinning",
                    "Cardboard only rotates if colored blue",
                    "Air molecules refuse to touch an off-center spindle"
                ],
                "ans": "A central pivot ensures symmetrical mass distribution, balancing rotational forces evenly",
                "explanation": "When the pivot is placed at the exact center of mass, centrifugal forces are equal in all directions, eliminating wobbling."
            },
            {
                "q": "What happens to the rotational energy when a spinner has an off-center pivot axis?",
                "options": [
                    "Violent wobbling increases ground friction, rapidly stopping the spin",
                    "The spinner accelerates indefinitely without stopping",
                    "The spinner floats into the upper atmosphere",
                    "The toothpick turns into liquid water"
                ],
                "ans": "Violent wobbling increases ground friction, rapidly stopping the spin",
                "explanation": "Uneven weight distribution causes the spindle to grind against the table, converting kinetic energy into heat and noise rapidly."
            }
        ]
    },
    {
        "id": 3,
        "title": "Spinner Optical Illusions",
        "badge": "Visual Perception",
        "description": "Explore the persistence of vision, observing how rotating square cards appear circular and how colored patterns blend into unified shades.",
        "sim_id": "sim-3",
        "sim_title": "Persistence of Vision & Color Disc Lab",
        "speech": (
            "Spinning toys do not merely demonstrate mechanical motion; they also unlock astonishing secrets regarding how the human eye and brain process visual information. "
            "When we spin a brightly colored square piece of cardboard rapidly on a toothpick spindle, our eyes no longer perceive distinct sharp corners. Instead, "
            "the square appears miraculously transformed into a smooth, translucent circle before our very eyes. This mesmerizing visual phenomenon is caused by persistence of vision. When light enters "
            "the human eye, the retina retains the visual impression for approximately one-sixteenth of a second after the light stimulus disappears. When an object rotates faster "
            "than this temporal processing threshold, our neural pathways overlap the sequential positions into a single, continuous, blended image. We observe the exact same "
            "fascinating optical principle in historic scientific instruments like physicist Isaac Newton's color disc. When a disc painted with sectors of violet, indigo, blue, green, yellow, "
            "orange, and red spins at high velocity, the individual hues fuse together on our retinas, making the disc appear grayish-white. Whether observing bicycle wheel "
            "spokes blurring into a solid transparent film or cinematic animation frames coming to life on screen, rapid rotational motion reveals how our human sensory perception synthesizes dynamic reality."
        ),
        "checkpoints": [
            {
                "q": "Why does a spinning square cardboard card appear completely circular to our eyes?",
                "options": [
                    "Persistence of vision blends rapidly moving corners into a continuous visual circle",
                    "The cardboard corners physically melt off during spinning",
                    "Spinning causes the cardboard to shrink into a sphere",
                    "The eyes stop seeing light completely"
                ],
                "ans": "Persistence of vision blends rapidly moving corners into a continuous visual circle",
                "explanation": "The human retina retains images for roughly 1/16th of a second, overlapping high-speed rotating corners into a solid blur."
            },
            {
                "q": "What happens when a disc painted with all seven rainbow colors is spun at high speed?",
                "options": [
                    "The individual colors blend together on the retina to appear white or off-white",
                    "The disc turns completely jet black",
                    "All the paint flies off into the air",
                    "The disc produces musical notes automatically"
                ],
                "ans": "The individual colors blend together on the retina to appear white or off-white",
                "explanation": "Newton's color disc proves that white light is a combination of all spectral colors, which fuse visually when spun rapidly."
            }
        ]
    },
    {
        "id": 4,
        "title": "Traditional Indian Lattu",
        "badge": "Cultural Mechanics",
        "description": "Examine the traditional Indian wooden spinning top (lattu), investigating string winding mechanics, pointed metal pivots, and gyroscopic balance.",
        "sim_id": "sim-4",
        "sim_title": "Traditional Lattu String Torque Engine",
        "speech": (
            "For centuries across Indian villages, towns, and school playgrounds, children have celebrated the physics of rotation through the beloved traditional spinning top, known locally "
            "as the lattu. Hand-carved from seasoned hardwood or molded from dense clay, the lattu features a pear-shaped symmetrical body tapering down gracefully to a sharp, hardened "
            "steel nail or brass pivot tip. Operating a lattu requires skillful mechanical coordination and practice. The player winds a sturdy cotton cord tightly around the grooved lower cone, "
            "holds the top inverted with the nail pointing outward, and casts it forcefully toward the ground while firmly pulling the cord backward. This rapid unwinding action "
            "transfers immense rotational torque to the wooden body, launching it into a blazing spin exceeding several hundred revolutions per minute. The sharp metal nail provides "
            "a microscopic point of contact with the ground, drastically minimizing frictional drag. Thanks to its heavy upper rim and concentrated angular momentum, the spinning lattu "
            "remains steadfastly upright, defying gravity like a precision gyroscope. Skilled children can even scoop the spinning lattu onto the open palm of their hand or along a tight string, "
            "demonstrating how traditional indigenous games embody sophisticated principles of rotational physics, momentum conservation, and timeless mechanical craftsmanship."
        ),
        "checkpoints": [
            {
                "q": "How does pulling the wrapped cotton string launch a traditional wooden lattu into a high-speed spin?",
                "options": [
                    "The unwinding cord exerts rapid rotational torque, converting pulling force into rotational energy",
                    "The string magically magnetizes the wooden body",
                    "The string heats the wood until it catches fire",
                    "The string blows wind beneath the top like a fan"
                ],
                "ans": "The unwinding cord exerts rapid rotational torque, converting pulling force into rotational energy",
                "explanation": "Pulling the cord unwinds it from the grooved body, imparting strong rotational torque that spins the lattu at high speed."
            },
            {
                "q": "Why does a traditional lattu feature a sharp, pointed metal tip at its base?",
                "options": [
                    "To minimize the contact surface area with the ground, reducing energy loss from friction",
                    "To dig deep holes in the earth for planting seeds",
                    "To make the top heavier than a brick",
                    "To prevent the top from ever moving"
                ],
                "ans": "To minimize the contact surface area with the ground, reducing energy loss from friction",
                "explanation": "A tiny contact point has minimal surface contact, sharply reducing friction so the lattu spins longer without slowing down."
            }
        ]
    },
    {
        "id": 5,
        "title": "The Historic Charkha",
        "badge": "Mechanical Heritage",
        "description": "Discover the mechanical engineering of the traditional Indian charkha, exploring pulley ratios, rotational drive belts, and fiber twisting physics.",
        "sim_id": "sim-5",
        "sim_title": "Charkha Pulley Ratio & Yarn Spindle",
        "speech": (
            "Beyond playground games, rotational physics holds a deeply revered place in Indian history, cultural pride, and industrial self-reliance through the iconic spinning wheel, known "
            "as the charkha. Championed by Mahatma Gandhi during the Indian independence movement, the charkha is an ingenious manual machine designed to transform loose raw cotton fibers into strong, "
            "continuous thread for weaving authentic khadi cloth. At its mechanical core, the charkha operates on an elegant two-stage belt-driven pulley system. The artisan turns a large hand-cranked "
            "wooden drive wheel smoothly. A continuous cotton drive cord connects this wide wheel to a vastly smaller spindle pulley called the takli. Because the primary drive wheel has a much larger circumference than the spindle, "
            "a single slow rotation of the main wheel causes the slender spindle to spin dozens of times at breathtaking speed. As the artisan carefully feeds raw carded cotton wisps toward the humming "
            "spindle tip, the rapid rotation twists the overlapping short cotton fibers together. This continuous twisting action locks the fibers through microscopic surface friction, forming durable, "
            "unbreakable yarn. The charkha stands as a magnificent historical testament to how simple rotational mechanics, velocity ratios, and creative human ingenuity empowered an entire nation."
        ),
        "checkpoints": [
            {
                "q": "What mechanical principle allows a charkha to spin the yarn spindle extremely fast with slow hand turning?",
                "options": [
                    "A large drive wheel connected to a tiny spindle pulley multiplies rotational speed through pulley ratios",
                    "An electric battery hidden inside the wooden base powers the spindle",
                    "The cotton thread pulls the wheel automatically",
                    "Steam pressure drives the spinning axle"
                ],
                "ans": "A large drive wheel connected to a tiny spindle pulley multiplies rotational speed through pulley ratios",
                "explanation": "The large drive wheel turns a much smaller spindle pulley via a belt, multiplying the rotational revolutions per turn."
            },
            {
                "q": "How does the rapid rotation of the charkha spindle transform fluffy cotton fibers into strong yarn?",
                "options": [
                    "The high-speed spinning twists adjacent fibers tightly together, locking them via friction into durable thread",
                    "The spindle melts the cotton into a liquid plastic glue",
                    "The spindle paints the cotton with synthetic white dye",
                    "The spindle cuts the cotton into microscopic dust grains"
                ],
                "ans": "The high-speed spinning twists adjacent fibers tightly together, locking them via friction into durable thread",
                "explanation": "Twisting short cotton staples aligns them and binds them together using natural fiber friction, creating resilient yarn."
            }
        ]
    },
    {
        "id": 6,
        "title": "Friction Slows Spinners",
        "badge": "Force & Energy",
        "description": "Analyze why spinning objects eventually stop, measuring the impact of smooth vs rough contact surfaces and aerodynamic drag.",
        "sim_id": "sim-6",
        "sim_title": "Surface Friction & Spin Duration Lab",
        "speech": (
            "A question that naturally sparks scientific inquiry in every classroom is: why does a spinning top or coin always slow down and stop instead of spinning indefinitely? "
            "The answer lies in physicist Isaac Newton's foundational laws of motion and the universal presence of dissipative forces, primarily friction. In an ideal scientific vacuum "
            "devoid of resistance, an object set into rotation would spin perpetually. However, in our everyday classroom environment, two forces constantly steal "
            "kinetic energy. First, contact friction occurs at the microscopic point where the tip of the spinner touches the tabletop. If we spin a top on a rough "
            "sandpaper sheet or woollen carpet, the coarse surface irregularities grind aggressively against the tip, converting rotational energy into thermal heat within seconds. "
            "Conversely, spinning the exact same top on a polished glass mirror or smooth ceramic tile allows it to spin significantly longer, because the micro-contact area experiences "
            "greatly diminished friction. Second, aerodynamic drag acts relentlessly on the spinning body. As the wide disc slices through the air, it collides with air molecules, creating "
            "invisible air resistance that steadily saps energy. Understanding friction empowers engineers to design low-friction ball bearings, lubricating oils, and streamlined aerodynamic shapes."
        ),
        "checkpoints": [
            {
                "q": "On which of the following surfaces will a toy top spin for the longest duration?",
                "options": [
                    "A smooth, polished glass plate",
                    "A coarse sheet of rough sandpaper",
                    "A thick, fluffy woollen carpet",
                    "A loose layer of outdoor garden soil"
                ],
                "ans": "A smooth, polished glass plate",
                "explanation": "A polished glass surface has minimal microscopic roughness, producing the least frictional resistance to rotation."
            },
            {
                "q": "Where does the kinetic energy of a spinning top go as it slows down and comes to a halt?",
                "options": [
                    "It transforms into microscopic heat, sound vibrations, and air movement",
                    "It vanishes completely from the universe without a trace",
                    "It turns into pure gravitational mass",
                    "It turns the top into solid ice"
                ],
                "ans": "It transforms into microscopic heat, sound vibrations, and air movement",
                "explanation": "According to the Law of Conservation of Energy, kinetic energy is converted into friction heat, acoustic sound, and air drag."
            }
        ]
    },
    {
        "id": 7,
        "title": "Floating Versus Sinking",
        "badge": "Buoyancy Foundations",
        "description": "Investigate why some materials float effortlessly on water while others sink to the bottom, introducing density and upward buoyant force.",
        "sim_id": "sim-7",
        "sim_title": "Density Tower & Float-Sink Tank",
        "speech": (
            "When raindrops gather into puddles outside or when we fill a transparent water bucket in the science laboratory, we encounter a timeless scientific inquiry: "
            "why do some objects float effortlessly on the surface, while others plunge straight to the bottom? If we drop a dry tree leaf, a cork stopper, or a light plastic "
            "bottle into the water, they bob gently on the surface, staying afloat without sinking. However, if we drop a small iron nail, a glass marble, or a dense pebble "
            "of the exact same size, they immediately sink and rest quietly on the container floor. This occurs because of a fundamental physical property called density—the amount "
            "of mass packed tightly inside a given volume of space—combined with the upward push of water, known as buoyant force. Water has a specific density of roughly one gram "
            "per cubic centimeter. Objects made of materials with lower density than water, such as dry wood and cork, experience an upward buoyant push greater than their downward "
            "weight, causing them to float securely. Conversely, dense materials like iron and stone have closely packed molecules, making them heavier than an equal volume of water, pulling "
            "them downward to the container floor."
        ),
        "checkpoints": [
            {
                "q": "Why does a dry tree leaf float on water while a small iron nail of similar size sinks immediately?",
                "options": [
                    "The leaf has a lower density than water, while the iron nail has a much higher density than water",
                    "The leaf is afraid of water, so it jumps to the top",
                    "Iron nails are attracted to the center of the earth by magnets",
                    "Water only likes green objects"
                ],
                "ans": "The leaf has a lower density than water, while the iron nail has a much higher density than water",
                "explanation": "Objects less dense than water float because their weight is less than the buoyant force; denser objects sink."
            },
            {
                "q": "What is the scientific term for the upward lifting force that water exerts on any submerged object?",
                "options": [
                    "Buoyant force (or upthrust)",
                    "Frictional drag",
                    "Magnetic pull",
                    "Chemical oxidation"
                ],
                "ans": "Buoyant force (or upthrust)",
                "explanation": "Buoyant force is the upward force exerted by fluids that opposes the weight of an immersed object."
            }
        ]
    },
    {
        "id": 8,
        "title": "Investigating Water Buoyancy",
        "badge": "Empirical Testing",
        "description": "Conduct Activity 4 prediction vs observation trials, classifying everyday objects into floaters and sinkers with a structured empirical table.",
        "sim_id": "sim-8",
        "sim_title": "Classroom Float & Sink Test Basin",
        "speech": (
            "In Class 4 Science Activity 4, curious young investigators explore the scientific method through hands-on empirical testing and systematic observation. Before placing any item into a bucket of water, "
            "students create a structured two-column record table labeled 'Prediction' and 'Observation'. Scientists never rely solely on hasty guesses; they hypothesize first, test "
            "carefully, and record empirical facts with honesty. When testing items like an eraser, a steel spoon, a hollow plastic ball, a wax candle, an empty glass tumbler, and an orange, "
            "surprises often occur that challenge common assumptions. For example, many students instinctively predict that a large, heavy wooden log will sink because it feels heavy, "
            "yet it floats gracefully on the surface. Conversely, a tiny steel sewing needle, which weighs almost nothing in your hand, sinks like a stone the instant it touches water. "
            "This critical experiment proves that whether an object floats or sinks does not depend simply on its total heaviness, but on its density and the volume of water it displaces. "
            "Testing wax reveals that its molecules are spaced so that solid wax is less dense than liquid water, floating calmly, while a dense plastic bead sinks, illustrating the profound joy of scientific empirical discovery."
        ),
        "checkpoints": [
            {
                "q": "Why is it incorrect to assume that all heavy objects sink and all light objects float?",
                "options": [
                    "Flotation depends on density and water displacement, not total weight alone (a huge wooden log floats, a tiny needle sinks)",
                    "Heavy objects always become lighter when they get wet",
                    "Water can tell how much money an object costs",
                    "Light objects always absorb air bubbles that make them fly"
                ],
                "ans": "Flotation depends on density and water displacement, not total weight alone (a huge wooden log floats, a tiny needle sinks)",
                "explanation": "Density (mass divided by volume) and water displacement govern buoyancy; heavy ships float while tiny dense needles sink."
            },
            {
                "q": "What does a wax candle do when placed in a bucket of freshwater, and why?",
                "options": [
                    "It floats, because wax has a lower density than water",
                    "It sinks instantly, because wax is made of stone",
                    "It dissolves into thin air in two seconds",
                    "It catches fire under water spontaneously"
                ],
                "ans": "It floats, because wax has a lower density than water",
                "explanation": "Paraffin wax has a density of roughly 0.9 g/cm³, which is less than water (1.0 g/cm³), allowing it to float buoyantly."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part1:
        wc = len(s['speech'].split())
        print(f"Slide {s['id']}: '{s['title']}' - Speech words: {wc}")
        assert 195 <= wc <= 215, f"Slide {s['id']} out of bounds: {wc}"
        assert len(s['title'].split()) <= 3, f"Slide {s['id']} title too long: {s['title']}"
        assert len(s['checkpoints']) == 2, f"Slide {s['id']} needs 2 checkpoints"
    print("All slides 1-8 passed checks successfully!")

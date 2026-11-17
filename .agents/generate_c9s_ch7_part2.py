#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part2 = [
    {
        "id": 9,
        "title": "Simple Machines",
        "subtitle": "Sections 7.6 & 7.6.1: Mechanical Advantage & Pulley Systems",
        "speech": (
            "How did ancient builders lift massive temple stones without electric motors, and how do modern cranes "
            "hoist steel girders? They use simple machines! A simple machine is a device that changes either the "
            "magnitude or the direction of an applied force to make a task easier—remembering that it NEVER "
            "reduces the total work required! We measure a machine's force-multiplying ability by its Mechanical "
            "Advantage, or MA, defined as Load divided by Effort. When MA is greater than one, a small effort "
            "lifts a heavy load! Start with our first simple machine in Section 7.6.1: the pulley, a grooved "
            "wheel with a rope running over it. A single fixed pulley mounted to a ceiling beam simply redirects "
            "your pull—you pull downward using your body weight to lift a bucket upward, giving an ideal Mechanical "
            "Advantage of one. By contrast, movable pulley systems—where one pulley moves along with the load "
            "supported by multiple rope segments—split the load across those ropes, giving a Mechanical Advantage "
            "greater than one! That is why construction cranes and building elevators rely on multi-pulley block "
            "and tackle systems every day. Remember, smaller effort always comes with pulling a longer length of rope "
            "to conserve total mechanical work."
        ),
        "checkpoints": [
            {
                "question": "What does a simple machine alter to make tasks easier, and what does it NEVER reduce?",
                "options": [
                    "It alters force magnitude or direction, but never reduces total work required",
                    "It reduces total work to zero",
                    "It eliminates gravity",
                    "It always multiplies speed by 100"
                ],
                "answer": 0,
                "hint": "Energy conservation applies to every machine: smaller force means pulling over a longer distance.",
                "explanation": "Simple machines change force magnitude or direction, while ideal work input equals work output."
            },
            {
                "question": "Compare a single fixed pulley with a movable pulley system in terms of Mechanical Advantage (MA = Load / Effort):",
                "options": [
                    "Fixed pulley has MA = 1 (changes direction); movable pulley has MA > 1 (reduces effort)",
                    "Fixed pulley has MA = 5; movable pulley has MA = 0",
                    "Both always have MA = 0.5",
                    "Neither can lift loads"
                ],
                "answer": 0,
                "hint": "A fixed pulley only redirects effort; movable pulleys share the load across rope segments.",
                "explanation": "A fixed pulley gives MA = 1 by changing pull direction, whereas movable pulleys give MA > 1."
            }
        ]
    },
    {
        "id": 10,
        "title": "Inclined Plane",
        "subtitle": "Section 7.6.2, Activity 7.3 & Example 7.12: Ramps & MA = L / h",
        "speech": (
            "Imagine rolling a heavy oil drum onto the back of a truck. Lifting it straight up vertically demands "
            "enormous force, yet pushing it up a slanted wooden plank feels surprisingly manageable! That slanted "
            "ramp is an inclined plane—a flat surface tilted at an angle to raise heavy loads using a smaller "
            "force applied over a longer distance. In Activity 7.3, pull a toy cart up wooden planks set at "
            "different steepness angles using a spring balance. As the slope angle becomes gentler, the required "
            "pulling force drops steadily, while the ramp length you must pull along grows longer! Because ideal "
            "work along the ramp equals work lifting vertically—Effort times ramp length L equals Load times "
            "vertical height h—we derive the ideal Mechanical Advantage of an inclined plane cleanly: MA equals "
            "Load divided by Effort, which equals ramp length L divided by vertical height h! Look at Example "
            "7.12: a wooden ramp fifty centimetres long rises to a vertical height of thirty centimetres. Dividing "
            "length fifty by height thirty gives a Mechanical Advantage of one point six seven—cutting your "
            "required lifting effort significantly! Try changing the ramp length and height in our simulator to see "
            "how force and distance trade off."
        ),
        "checkpoints": [
            {
                "question": "In Activity 7.3, what happens to the required pulling force as the slope angle of an inclined plane decreases?",
                "options": [
                    "Required force increases",
                    "Required force decreases, while pulling distance L increases",
                    "Required force stays equal to Load",
                    "Total work becomes negative"
                ],
                "answer": 1,
                "hint": "Gentler ramps have larger L/h ratio.",
                "explanation": "A gentler slope lowers the effort needed by spreading the same vertical lift over a longer ramp L."
            },
            {
                "question": "In Example 7.12, what is the ideal Mechanical Advantage of a ramp 50 cm long rising to a height of 30 cm?",
                "options": [
                    "0.60",
                    "1.67",
                    "2.00",
                    "15.0"
                ],
                "answer": 1,
                "hint": "Use MA = L / h = 50 / 30.",
                "explanation": "MA = L / h = 50 cm / 30 cm = 5/3 ≈ 1.67."
            }
        ]
    },
    {
        "id": 11,
        "title": "Principle of Levers",
        "subtitle": "Section 7.6.3, Activities 7.4–7.5 & Example 7.13: Moments & Seesaws",
        "speech": (
            "Give me a place to stand, and I shall move the Earth—so spoke ancient Greek thinker Archimedes about "
            "the lever! A lever is a rigid bar free to pivot about a fixed turning point called the fulcrum. "
            "In Activities 7.4 and 7.5, balance a wooden ruler over a pencil fulcrum to lift a heavy stapler or "
            "stack of coins using just a light finger tap! Every lever has three key features: the Fulcrum, the "
            "Load sitting at distance Load Arm from the fulcrum, and the Effort applied at distance Effort Arm "
            "from the fulcrum. When balanced horizontally, the lever obeys the Principle of Moments: Effort times "
            "Effort Arm equals Load times Load Arm, written as F1 times d1 equals F2 times d2! Rearranging this "
            "gives the Mechanical Advantage of a lever: MA equals Effort Arm L1 divided by Load Arm L2. Look at "
            "Example 7.13 on a playground seesaw: if a thirty-kilogram child sits one metre from the central "
            "fulcrum, where must a fifteen-kilogram child sit to balance? Half the weight needs double the arm—"
            "so fifteen times two equals thirty times one, placing the lighter child two metres out from the centre "
            "pivot to achieve perfect rotational balance!"
        ),
        "checkpoints": [
            {
                "question": "What does the Principle of Moments state for a balanced lever?",
                "options": [
                    "Effort + Effort Arm = Load + Load Arm",
                    "Effort × Effort Arm = Load × Load Arm (F₁d₁ = F₂d₂)",
                    "Effort × Load = Effort Arm × Load Arm",
                    "Fulcrum must always be at the end"
                ],
                "answer": 1,
                "hint": "Turning moments on opposite sides of the fulcrum must be equal.",
                "explanation": "For rotational balance, Effort × Effort Arm = Load × Load Arm."
            },
            {
                "question": "In Example 7.13, a 30 kg child sits 1 m from a seesaw fulcrum. How far from the fulcrum must a 15 kg child sit to balance?",
                "options": [
                    "0.5 m",
                    "1.0 m",
                    "2.0 m",
                    "3.0 m"
                ],
                "answer": 2,
                "hint": "Use 15 × d₁ = 30 × 1.",
                "explanation": "15 kg × 2.0 m = 30 kg × 1 m, so the 15 kg child sits 2.0 m away."
            }
        ]
    },
    {
        "id": 12,
        "title": "Classes of Levers",
        "subtitle": "Section 7.6.3 & Table 7.2: Class I, Class II & Class III Levers",
        "speech": (
            "Look around your home, toolbox, and kitchen—almost every hand tool is a lever! Scientists sort all "
            "levers into three neat classes in Table 7.2 based on one simple rule: which component sits IN THE "
            "MIDDLE between the other two? Remember the mnemonic F-L-E for Classes one, two, and three! In a "
            "Class I lever, the Fulcrum is in the middle, with Load on one side and Effort on the other—examples "
            "include a playground seesaw, a crowbar prying a rock, scissors, and pliers. Depending on where the "
            "fulcrum sits, Class I can multiply force or speed. In a Class II lever, the Load sits in the middle "
            "between the Fulcrum at one end and the Effort at the far end! Think of a gardener's wheelbarrow, a "
            "lemon squeezer, or a bottle opener: because the Effort Arm is always longer than the Load Arm, "
            "Class II levers ALWAYS give Mechanical Advantage greater than one! Finally, in a Class III lever, "
            "Effort is applied in the middle—like kitchen tongs, tweezers, a broom, or a boat oar—giving MA less "
            "than one to gain precision and speed! Use our interactive lever classifier to inspect every everyday tool "
            "and verify its fulcrum, load, and effort."
        ),
        "checkpoints": [
            {
                "question": "Which set lists ONLY Class II levers (where Load sits between Fulcrum and Effort)?",
                "options": [
                    "Scissors, pliers, seesaw",
                    "Wheelbarrow, lemon squeezer, bottle opener",
                    "Tongs, tweezers, broom",
                    "Crowbar, oar, scissors"
                ],
                "answer": 1,
                "hint": "Remember F-L-E: Class I = Fulcrum middle, Class II = Load middle, Class III = Effort middle.",
                "explanation": "Wheelbarrows, lemon squeezers, and bottle openers place the Load in the middle (Class II)."
            },
            {
                "question": "Why do Class III levers like kitchen tongs and tweezers have Mechanical Advantage less than 1?",
                "options": [
                    "Effort is applied closer to the fulcrum than the load (Effort Arm < Load Arm), trading force for speed and precision",
                    "They have no fulcrum",
                    "Their load arm is zero",
                    "They violate conservation of energy"
                ],
                "answer": 0,
                "hint": "Since MA = Effort Arm / Load Arm, having Effort in the middle makes Effort Arm shorter.",
                "explanation": "In Class III levers, Effort sits between Fulcrum and Load, so Effort Arm < Load Arm (MA < 1)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Gharat & Hydropower",
        "subtitle": "Bridging Science and Society: Himalayan Water Mills & Hydroelectric Dams",
        "speech": (
            "Long before modern electrical grids reached high mountain valleys, communities across the Himalayas "
            "engineered an ingenious clean-energy machine: the traditional gharat, also called a panchakki or "
            "water mill! In Bridging Science and Society, see how the exact same physics powers both ancient "
            "gharats and giant modern hydroelectric dams. Mountain streams flowing down steep slopes carry huge "
            "gravitational potential energy at higher elevations. Channeled through a wooden chute called a flume, "
            "the falling water accelerates, converting potential energy into rapid kinetic energy! When that "
            "fast water jet strikes the angled wooden blades of a horizontal water wheel below the millhouse, it "
            "does positive work, spinning a vertical shaft connected directly to a heavy circular grinding stone "
            "above—milling wheat, maize, and spices with zero smoke or fossil fuel! Modern hydroelectric power "
            "stations scale up this exact chain: high dams store vast reservoirs of gravitational potential "
            "energy, penstock pipes rush water onto steel turbines to create rotational kinetic energy, and "
            "generators convert that motion into clean electricity lighting millions of homes across India! Both "
            "traditional gharats and modern dams prove how timeless physics principles power sustainable communities "
            "while protecting mountain rivers and clean air for future generations across India."
        ),
        "checkpoints": [
            {
                "question": "What energy conversion sequence powers a traditional Himalayan gharat (panchakki) water mill?",
                "options": [
                    "Nuclear energy → light energy → chemical energy",
                    "Stream gravitational potential energy → kinetic energy of rushing water → rotational mechanical grinding",
                    "Electrical energy → sound energy",
                    "Thermal coal burning → steam"
                ],
                "answer": 1,
                "hint": "Elevated mountain water flows downhill onto turbine blades connected to millstones.",
                "explanation": "Elevated water's potential energy converts to kinetic energy, spinning the wheel and grinding stones."
            },
            {
                "question": "How do modern hydroelectric dams mirror the working principle of a traditional gharat?",
                "options": [
                    "Both burn diesel fuel",
                    "Both convert stored gravitational potential energy of elevated water into kinetic energy to spin turbines",
                    "Both use solar panels only",
                    "Both rely on chemical batteries"
                ],
                "answer": 1,
                "hint": "Compare a dam's reservoir + turbine with a gharat's elevated stream + water wheel.",
                "explanation": "Both harness elevated water's gravitational potential energy to drive rotating blades."
            }
        ]
    },
    {
        "id": 14,
        "title": "Journey Beyond",
        "subtitle": "The Journey Beyond & Quest Continues: DIY Machines, PhET & Dark Energy",
        "speech": (
            "Ready to take physics beyond the classroom? In The Journey Beyond, you can build simple machines "
            "and elastic launchers right at your desk! A spring-loaded pen-refill launcher demonstrates elastic "
            "potential energy transforming cleanly into projectile kinetic energy, while homemade pulley and "
            "inclined-plane kits let you test Mechanical Advantage directly with a small spring balance. Online, "
            "interactive PhET simulations like Energy Skate Park let you watch bar graphs of kinetic, potential, "
            "and thermal friction energy dance in real time as a skater swoops down curved ramps! And now look "
            "to the cosmos in The Quest Continues: we saw how gravity slows down a ball thrown upward on Earth. "
            "Astronomers once expected gravity to slow down the expansion of the entire universe after the Big "
            "Bang too. Instead, telescope observations revealed a stunning cosmic mystery: galaxies are racing "
            "apart faster and faster! Scientists attribute this accelerating expansion to an unknown cosmic "
            "phenomenon called dark energy—reminding us that even after mastering earthly work and energy, "
            "vast frontiers still await curious young scientists like you! Keep questioning, experimenting with "
            "everyday materials, and exploring how energy shapes everything from tiny springs to distant galaxies "
            "across the entire observable universe today."
        ),
        "checkpoints": [
            {
                "question": "In a DIY pen-refill launcher, what energy conversion launches the projectile?",
                "options": [
                    "Nuclear energy to thermal energy",
                    "Stored elastic potential energy of the compressed spring to kinetic energy",
                    "Gravitational energy to chemical energy",
                    "Sound energy to electrical energy"
                ],
                "answer": 1,
                "hint": "Compressing the spring deforms it, storing elastic energy.",
                "explanation": "Elastic potential energy stored in the compressed spring converts into kinetic energy of the refill."
            },
            {
                "question": "What cosmic mystery is attributed to 'dark energy' in The Quest Continues?",
                "options": [
                    "Why pendulums stop due to air drag",
                    "The observed accelerating expansion of the universe",
                    "How gharats grind wheat",
                    "Why Class II levers have MA > 1"
                ],
                "answer": 1,
                "hint": "Galaxies are moving apart faster rather than slowing down.",
                "explanation": "Dark energy is the name given to the mysterious driver accelerating the universe's expansion."
            }
        ]
    },
    {
        "id": 15,
        "title": "Applied Review",
        "subtitle": "Revise, Reflect, Refine: Path Independence, F–s & U–s Curves",
        "speech": (
            "Before you enter the four silent quizzes, let us sharpen three subtle ideas from Revise, Reflect, "
            "Refine! First, gravitational work is path-independent: whether you carry a ten-kilogram suitcase "
            "up a straight ladder, a winding staircase, or a long ramp to a three-metre balcony, the work done "
            "against gravity depends ONLY on vertical height h—always m g h! Second, on a Force-Displacement "
            "graph, even if the force changes linearly like a stretched spring forming a triangle, simply "
            "compute the geometric area under the graph—half times base times height—to find exact work done in "
            "joules! Third, read Potential Energy-Displacement curves like a roller-coaster track: at any "
            "position, subtracting U from total mechanical energy ME immediately gives kinetic energy K! Check "
            "your units every single time: convert grams to kilograms, centimetres to metres, and kilometres per "
            "hour to metres per second by multiplying by five over eighteen. Also double-check the angle between "
            "force and displacement before assigning a positive, negative, or zero sign. Always draw a quick sketch "
            "showing direction arrows for force and motion. With clean unit conversions, clear free-body thinking, "
            "and energy conservation, you can crack any physics numerical problem in just a few seconds with complete confidence!"
        ),
        "checkpoints": [
            {
                "question": "A 5 kg bag is carried to a 4 m high roof via a winding 12 m staircase instead of a vertical 4 m ladder (g = 10 m/s²). Work done against gravity is:",
                "options": [
                    "600 J",
                    "200 J (depends only on vertical height h = 4 m)",
                    "480 J",
                    "0 J"
                ],
                "answer": 1,
                "hint": "Gravitational work depends only on vertical height change, not path length.",
                "explanation": "W = mgh = 5 × 10 × 4 = 200 J regardless of staircase length."
            },
            {
                "question": "A Force–Displacement graph rises linearly from F = 0 N at s = 0 m to F = 20 N at s = 6 m. What is the total work done?",
                "options": [
                    "120 J",
                    "60 J",
                    "26 J",
                    "3.33 J"
                ],
                "answer": 1,
                "hint": "Area under the graph is a triangle: ½ × base × height.",
                "explanation": "Area = ½ × 6 m × 20 N = 60 J."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary",
        "subtitle": "At a Glance: Complete Work, Energy, Power & Simple Machines Map",
        "speech": (
            "Let us wrap up Chapter 7 with our complete At a Glance toolkit! First, work W equals F times s "
            "measured in joules—positive when force aligns with displacement, negative when opposite, and zero "
            "when F is zero, s is zero, or force is perpendicular at ninety degrees. Second, by the Work-Energy "
            "Theorem, net work equals change in energy. Third, mechanical energy combines kinetic energy K equals "
            "half m v squared and gravitational potential energy U equals m g h; under conservative forces, total "
            "mechanical energy K plus U stays conserved, as seen in free fall and pendulums. Fourth, power P "
            "equals W over t in watts, with one horsepower equal to seven hundred and forty-six watts. Fifth, "
            "simple machines alter force magnitude or direction with Mechanical Advantage equal to Load over Effort: "
            "fixed pulleys give MA one while movable pulleys exceed one; inclined planes give MA equal to L over "
            "h; and levers obey Effort times Effort Arm equals Load times Load Arm across Classes I, II, and III. "
            "From Himalayan water mills to cosmic dark energy, energy principles unify the entire physical world. "
            "You are now ready for the four silent mastery quizzes ahead!"
        ),
        "checkpoints": [
            {
                "question": "Which formula pairing across Chapter 7 is completely accurate?",
                "options": [
                    "W = F/s; K = mv; U = mgh²; P = W×t",
                    "W = F×s; K = ½mv²; U = mgh; P = W/t; MA = Load/Effort",
                    "W = ma; K = mgh; U = ½mv²; P = F/t",
                    "W = F×t; K = ½mv; U = mg/h; MA = Effort/Load"
                ],
                "answer": 1,
                "hint": "Verify every single formula against Sections 7.1 to 7.6.",
                "explanation": "W = Fs, K = ½mv², U = mgh, P = W/t, and MA = Load/Effort."
            },
            {
                "question": "Which simple machine always has Mechanical Advantage less than 1 because Effort is between Fulcrum and Load?",
                "options": [
                    "Class I lever (crowbar)",
                    "Class II lever (wheelbarrow)",
                    "Class III lever (tongs/tweezers)",
                    "Inclined plane"
                ],
                "answer": 2,
                "hint": "Remember F-L-E for Classes I, II, and III.",
                "explanation": "Class III levers place Effort in the middle, making Effort Arm < Load Arm (MA < 1)."
            }
        ]
    }
]

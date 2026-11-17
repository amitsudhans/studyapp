#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part2 = [
    {
        "id": 9,
        "title": "Second Law Problems",
        "subtitle": "Section 6.5 Worked Examples 6.4, 6.5 & 6.6: Barbell, Box & Sports Car",
        "speech": (
            "Let us apply F equals m a to solve three classic textbook problems: Examples 6.4, 6.5, and 6.6. "
            "In Example 6.4, a weightlifter holds a thirty-kilogram barbell steady above their head. Since it is "
            "stationary, net force is zero, so the upward force equals the downward weight: thirty times nine "
            "point eight, which is two hundred and ninety-four newtons! In Example 6.5, a twenty-five-kilogram "
            "box on a floor experiences a fifty-five-newton forward push and fifty newtons of backward friction. "
            "Net force is fifty-five minus fifty, or five newtons. Dividing five newtons by twenty-five "
            "kilograms gives acceleration a equals zero point two metres per second squared. Starting from rest "
            "for two seconds, displacement s equals half times zero point two times two squared, giving zero "
            "point four metres! Finally, in Example 6.6, a fifteen-hundred-kilogram sports car accelerates east "
            "at two metres per second squared, cruises steadily, then brakes at minus two metres per second "
            "squared. Multiplying mass by each slope gives three thousand newtons east, zero newtons during "
            "cruising, and minus three thousand newtons west during braking! Always read the velocity-time slope first "
            "to find acceleration, then multiply by total mass to get the exact net force in each phase."
        ),
        "checkpoints": [
            {
                "question": "In Example 6.5, a 25 kg box is pushed with 55 N against 50 N friction starting from rest. What is its acceleration?",
                "options": [
                    "0.2 m/s²",
                    "2.2 m/s²",
                    "5.0 m/s²",
                    "0.4 m/s²"
                ],
                "answer": 0,
                "hint": "Net force = 55 N - 50 N = 5 N; then use a = F_net / m.",
                "explanation": "F_net = 5 N, so a = 5 / 25 = 0.2 m/s² (giving s = ½(0.2)(2²) = 0.4 m in 2 s)."
            },
            {
                "question": "In Example 6.6, what net force acts on the 1500 kg sports car during its constant-velocity cruising phase?",
                "options": [
                    "3000 N east",
                    "-3000 N west",
                    "0 N",
                    "1500 N"
                ],
                "answer": 2,
                "hint": "Constant velocity means zero acceleration.",
                "explanation": "During constant speed, a = 0 m/s², so F = m × 0 = 0 N."
            }
        ]
    },
    {
        "id": 10,
        "title": "Newton's Third Law",
        "subtitle": "Section 6.6, Activities 6.5 & 6.6: Action-Reaction Pairs",
        "speech": (
            "Have you noticed that whenever you push against something, it pushes right back at you? That "
            "universal symmetry is Newton's Third Law of Motion: whenever one object exerts a force on a second "
            "object, the second object simultaneously exerts an equal and opposite force on the first object! "
            "Try Activity 6.5: sit on a smooth wheeled office chair and push forward against a heavy fixed "
            "table. Instantly, your chair rolls backward! Your hands pushed the table forward, and the table "
            "pushed you backward with equal force. Pull the table toward yourself, and the table pulls your "
            "chair forward! Next, verify the exact numbers in Activity 6.6: hook two spring balances together "
            "and pull in opposite directions. No matter how gently or strongly you pull, both spring balances "
            "display identical newton readings at the exact same instant! Here is a crucial exam tip: why do "
            "action and reaction forces NEVER cancel each other out? Because they always act on TWO DIFFERENT "
            "objects! Your foot pushes the ground, while the ground pushes your body—different objects, so both "
            "forces remain real and uncancelled. Keep that key distinction crystal clear whenever you draw action-reaction force pairs in physics problems!"
        ),
        "checkpoints": [
            {
                "question": "In Activity 6.6, when two interlocked spring balances are pulled apart and one reads 18 N, what does the other read?",
                "options": [
                    "0 N",
                    "9 N",
                    "18 N (equal in magnitude, opposite in direction)",
                    "36 N"
                ],
                "answer": 2,
                "hint": "Newton's Third Law states action and reaction are equal and opposite.",
                "explanation": "Both spring balances show identical readings (18 N) in opposite directions."
            },
            {
                "question": "Why do action and reaction forces never cancel each other to give zero net force?",
                "options": [
                    "Because they act at different times",
                    "Because they always act on two different objects",
                    "Because reaction is always smaller",
                    "Because friction destroys reaction"
                ],
                "answer": 1,
                "hint": "You only add forces acting on the SAME object to find its net force.",
                "explanation": "Action acts on object B and reaction acts on object A, so they never cancel on a single object."
            }
        ]
    },
    {
        "id": 11,
        "title": "Rockets & Propulsion",
        "subtitle": "Section 6.6 & Activity 6.7: Walking, Canoeing, Balloons & Chandrayaan-3",
        "speech": (
            "Newton's Third Law powers everything from a morning walk to lunar landings! When you walk or run, "
            "your foot pushes backward against the ground, and static friction from the ground pushes your body "
            "forward. When a farmer climbs a tall coconut tree, their hands and feet push downward on the trunk, "
            "and the trunk pushes them upward. When rowing a canoe, the paddle pushes water backward, so the "
            "water propels the canoe forward! Watch Activity 6.7 for a thrilling miniature rocket: thread a "
            "drinking straw taped to an inflated balloon onto a taut horizontal string, then release the neck. "
            "As air rushes backward out of the balloon, the escaping gas pushes the balloon forward along the "
            "string! Real space rockets work identically even in the airless vacuum of outer space—they do NOT "
            "need air to push against! Hot exhaust gases shoot downward at huge speed, propelling the rocket "
            "upward. And during India's historic Chandrayaan-3 mission, the Vikram lander fired its retro-thrusters "
            "downward toward the Moon's surface, using upward reaction thrust to brake gently for a soft lunar landing! "
            "Even far beyond Earth's atmosphere, Newton's Third Law remains our most reliable engine for deep space travel."
        ),
        "checkpoints": [
            {
                "question": "In Activity 6.7, what propels the balloon rocket forward along the taut string?",
                "options": [
                    "Surrounding room air pushing the string",
                    "Escaping air shooting backward exerts an equal and opposite forward reaction force on the balloon",
                    "Static electricity from the straw",
                    "Gravity pulling horizontally"
                ],
                "answer": 1,
                "hint": "Action: balloon pushes air backward; Reaction: escaping air pushes balloon forward.",
                "explanation": "The balloon expels air backward, and the reaction force of the escaping air drives the balloon forward."
            },
            {
                "question": "How did Chandrayaan-3's Vikram lander slow down for a soft landing on the airless Moon?",
                "options": [
                    "By opening a giant parachute",
                    "By retro-firing thrusters downward to generate upward reaction thrust",
                    "By using air friction",
                    "By turning off gravity"
                ],
                "answer": 1,
                "hint": "Rockets and landers work in vacuum using Third Law exhaust reaction.",
                "explanation": "Retro-firing exhaust gases toward the lunar surface produced an upward reaction force that slowed Vikram safely."
            }
        ]
    },
    {
        "id": 12,
        "title": "Non-Contact Action-Reaction",
        "subtitle": "Section 6.6, Examples 6.7 & 6.8: Gravity, Magnets & Gun Recoil",
        "speech": (
            "Does Newton's Third Law apply only when objects touch? Not at all! Action-reaction pairs operate "
            "across empty space for non-contact forces too—including magnetic, electrostatic, and gravitational "
            "forces. Hold two bar magnets near each other: Magnet A pulls Magnet B with the exact same force "
            "that Magnet B pulls Magnet A! Now look at Example 6.7: when a ripe mango falls from a tree, Earth "
            "pulls the mango downward with a gravitational force F, and the mango simultaneously pulls Earth "
            "upward with the exact same force F! Why do we see the mango race downward while Earth seems "
            "completely motionless? Because acceleration equals F divided by mass! The mango's tiny mass gets a "
            "large acceleration of nine point eight metres per second squared, whereas Earth's colossal mass "
            "receives an unimaginably tiny acceleration! Example 6.8 shows the same mass contrast in a rifle "
            "recoil: a two-newton firing force pushes a zero-point-one-kilogram bullet forward at twenty metres "
            "per second squared, while kicking the five-kilogram gun backward at just zero point four metres per "
            "second squared! Equal action-reaction forces always produce much larger accelerations on lighter masses and much smaller accelerations on heavier masses in every real physical interaction."
        ),
        "checkpoints": [
            {
                "question": "In Example 6.7, a falling fruit and Earth pull each other with equal gravitational force F. Why does only the fruit noticeably move?",
                "options": [
                    "Earth has no acceleration at all",
                    "Because a = F/m, Earth's colossal mass makes its upward acceleration negligibly tiny",
                    "The fruit exerts zero force on Earth",
                    "Gravity is a contact force"
                ],
                "answer": 1,
                "hint": "Equal forces produce vastly different accelerations when masses differ enormously.",
                "explanation": "Although F is identical on both, Earth's huge mass m makes a = F/m unnoticeably small."
            },
            {
                "question": "In Example 6.8, a 2 N force fires a 0.1 kg bullet from a 5 kg gun. What are the bullet and gun accelerations?",
                "options": [
                    "Bullet 2 m/s², gun 2 m/s²",
                    "Bullet 20 m/s², gun 0.4 m/s²",
                    "Bullet 0.4 m/s², gun 20 m/s²",
                    "Bullet 10 m/s², gun 5 m/s²"
                ],
                "answer": 1,
                "hint": "Compute a = F/m for each: 2 / 0.1 and 2 / 5.",
                "explanation": "Bullet a = 2 / 0.1 = 20 m/s² forward; Gun recoil a = 2 / 5 = 0.4 m/s² backward."
            }
        ]
    },
    {
        "id": 13,
        "title": "Multi-Body Systems",
        "subtitle": "Section 6.7: Connected Masses, Internal Tension & System Acceleration",
        "speech": (
            "What if two or more objects are linked together, such as two train coaches coupled together, or two "
            "boxes of masses m1 and m2 joined by a taut string and pulled forward by an external force F? Let "
            "us see a brilliant problem-solving shortcut from Section 6.7! On the front box m1, the external "
            "force F pulls forward while the connecting string pulls backward with tension T. Meanwhile, on the "
            "rear box m2, that exact same string pulls forward with equal and opposite tension T! Inside the "
            "combined two-box system, those two tension forces are internal action-reaction pairs—equal in "
            "magnitude and opposite in direction—so when we treat both boxes and the string as a single "
            "combined system, the internal tension T cancels out completely! Only the external pulling force F "
            "accelerates the total mass m1 plus m2. Therefore, the system's common acceleration is simply a "
            "equals F divided by m1 plus m2! Once you find a, you can immediately compute the string tension "
            "T if needed by multiplying rear mass m2 times acceleration a. Grouping connected objects simplifies "
            "complex multi-body problems in seconds! You can apply this exact same system trick to three or more "
            "linked blocks or train coaches."
        ),
        "checkpoints": [
            {
                "question": "Two boxes of masses m₁ = 4 kg and m₂ = 6 kg are joined by a string on a smooth floor and pulled by F = 30 N. What is the system's acceleration?",
                "options": [
                    "7.5 m/s²",
                    "5.0 m/s²",
                    "3.0 m/s²",
                    "1.5 m/s²"
                ],
                "answer": 2,
                "hint": "Treat both boxes as one system: a = F / (m₁ + m₂).",
                "explanation": "Internal tension cancels, so a = 30 / (4 + 6) = 30 / 10 = 3.0 m/s²."
            },
            {
                "question": "Why does internal string tension T vanish when calculating acceleration of a connected two-box system?",
                "options": [
                    "The string has infinite length",
                    "The string pulls m₁ backward and m₂ forward with equal and opposite internal forces that cancel for the whole system",
                    "Tension is always zero in moving strings",
                    "Gravity turns tension off"
                ],
                "answer": 1,
                "hint": "Internal action-reaction forces cancel when summed over the combined system.",
                "explanation": "Within the combined system, the opposite tensions on m₁ and m₂ cancel, leaving only external force F."
            }
        ]
    },
    {
        "id": 14,
        "title": "Friction Engineering",
        "subtitle": "The Journey Beyond: Maglev, Capstan Effect & Newton's Principia",
        "speech": (
            "Engineers constantly balance friction—sometimes boosting it for safe tyres and brakes, and other "
            "times slashing it to save energy! In The Journey Beyond, explore how modern transport minimizes "
            "sliding friction. Ball bearings replace sliding friction with much smaller rolling friction inside "
            "bicycle hubs and electric motors, while thin oil lubricants separate metal engine parts. Even more "
            "futuristic, magnetic levitation—or Maglev—trains use powerful electromagnets to lift the entire "
            "train slightly above the track, eliminating wheel-rail contact friction so trains glide past four "
            "hundred kilometres per hour! On the other hand, sailors and mountaineers exploit the amazing capstan "
            "effect: wrapping a rope just a few turns around a smooth cylindrical post multiplies rope friction "
            "exponentially, allowing one person to hold back a massive ship! You can test this safely with a "
            "broomstick and string, or use two toy cars with repelling magnets to witness non-contact Third Law "
            "pairs. For deeper inspiration, read translated excerpts from Isaac Newton's 1687 masterpiece, "
            "Principia Mathematica, where these three universal laws were first united. Understanding when to "
            "boost friction for safety and when to eliminate it for energy efficiency lies at the very heart of modern mechanical, aerospace, and high-speed transport engineering."
        ),
        "checkpoints": [
            {
                "question": "How do Maglev (magnetic levitation) trains achieve ultra-high speeds with minimal energy loss?",
                "options": [
                    "They glue rubber tyres to steel rails",
                    "Electromagnets lift the train off the track, eliminating wheel-rail contact friction",
                    "They burn coal inside the wheels",
                    "They increase normal force on the rails"
                ],
                "answer": 1,
                "hint": "No physical contact with the track means no rolling or sliding track friction.",
                "explanation": "Magnetic levitation suspends the train above the rails, removing track contact friction."
            },
            {
                "question": "What does the capstan effect demonstrate when a rope is wrapped multiple turns around a post?",
                "options": [
                    "Friction vanishes completely",
                    "Wrapping multiplies frictional grip exponentially so a small hold force balances a huge load",
                    "The rope loses all tension",
                    "Gravity reverses direction"
                ],
                "answer": 1,
                "hint": "Sailors use bollards on docks to moor heavy ships with one rope.",
                "explanation": "Each wrap around a cylinder multiplies frictional resistance, letting a small pull hold a heavy load."
            }
        ]
    },
    {
        "id": 15,
        "title": "Applied Review",
        "subtitle": "Revise, Reflect, Refine: Boats, Sailors, Footballs & Compass Needles",
        "speech": (
            "Let us sharpen our problem-solving instincts on key Revise, Reflect, Refine scenarios before you "
            "tackle the silent quizzes! First, consider a boat rowed by two oarsmen: if each pushes water "
            "backward, the water pushes the boat forward, and you find net acceleration by subtracting water "
            "drag from total forward thrust. Second, why does a small wooden boat drift backward when a sailor "
            "jumps forward onto a pier? By Newton's Third Law, the sailor pushes the boat backward to launch "
            "forward! Third, when a football player kicks a stationary ball, a brief contact time delta t "
            "transfers huge momentum—so force equals mass times final speed divided by contact time. Fourth, "
            "when a bullet penetrates a thick wooden plank, wood exerts a steady backward resistive force that "
            "decelerates the bullet over the penetration depth. Fifth, even a tiny magnetic compass needle "
            "swings toward north because Earth's magnetic field exerts a non-contact torque on it—and the "
            "needle exerts an equal opposite magnetic force on Earth! Always draw a clear force diagram first, "
            "separate horizontal from vertical forces, and check every single SI unit carefully before calculating your final numerical answer cleanly on paper or your digital screen today."
        ),
        "checkpoints": [
            {
                "question": "When a sailor jumps forward from a small unanchored boat onto a dock, why does the boat move backward?",
                "options": [
                    "Water pushes the boat forward",
                    "The sailor's feet push the boat backward as the boat pushes the sailor forward (Third Law)",
                    "The boat's mass increases",
                    "Air resistance pulls the boat backward"
                ],
                "answer": 1,
                "hint": "Identify the action-reaction pair between the sailor and the boat.",
                "explanation": "To propel forward, the sailor exerts a backward force on the boat, causing the boat to recoil backward."
            },
            {
                "question": "A 0.4 kg football at rest is kicked to 15 m/s in a contact time of 0.02 s. What average force did the boot exert?",
                "options": [
                    "6 N",
                    "60 N",
                    "300 N",
                    "30 N"
                ],
                "answer": 2,
                "hint": "Use F = Δp / Δt = (m × v - 0) / Δt.",
                "explanation": "F = (0.4 × 15) / 0.02 = 6 / 0.02 = 300 N."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary",
        "subtitle": "At a Glance: Friction, Inertia & Newton's Three Laws",
        "speech": (
            "Let us bring all of Chapter 6 together in one crisp At a Glance summary! First, force is a vector "
            "push or pull measured in newtons with a spring balance; balanced forces give zero net force and "
            "zero acceleration, while unbalanced forces change velocity. Second, friction opposes relative motion "
            "between surfaces, depends on surface smoothness, and led Galileo to discover that frictionless "
            "motion continues forever. Third, Newton's First Law defines inertia: objects resist changes to "
            "rest or uniform velocity unless acted on by a net external force. Fourth, Newton's Second Law "
            "gives F equals m a and F equals delta p over delta t, explaining weight F equals m g, cricket "
            "catches, airbags, and vehicle braking. Fifth, Newton's Third Law states that every action has an "
            "equal and opposite reaction acting simultaneously on two DIFFERENT bodies—governing walking, "
            "swimming, balloon rockets, Chandrayaan-3 retro-firing, magnets, and gun recoil. Finally, for "
            "connected multi-body systems, internal tensions cancel so acceleration equals external force "
            "divided by total mass. You are now ready for the four silent mastery quizzes! Take your time, "
            "use the hints whenever needed, and carefully review every three-step solution pop-up to master force and motion completely today."
        ),
        "checkpoints": [
            {
                "question": "Which summary statement correctly pairs all three of Newton's Laws?",
                "options": [
                    "1st: Inertia (zero net F ⇒ constant v); 2nd: F = ma = Δp/Δt; 3rd: Equal & opposite forces on two different bodies",
                    "1st: F = ma; 2nd: Action-reaction; 3rd: Inertia",
                    "1st: Friction = 0; 2nd: v = u + at; 3rd: Single-body cancellation",
                    "1st: Gravity only; 2nd: Circular motion; 3rd: Mass = weight"
                ],
                "answer": 0,
                "hint": "Match First = Inertia, Second = F=ma, Third = Action-Reaction.",
                "explanation": "First Law covers inertia, Second Law quantifies F = ma = Δp/Δt, and Third Law covers action-reaction pairs."
            },
            {
                "question": "Which quantity measures an object's inertia (its resistance to changes in velocity)?",
                "options": [
                    "Volume",
                    "Mass",
                    "Colour",
                    "Surface area"
                ],
                "answer": 1,
                "hint": "In Activity 6.4, doubling this quantity halved the acceleration for the same force.",
                "explanation": "Mass is the quantitative measure of inertia: greater mass requires greater force for the same acceleration."
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part1 = [
    {
        "id": 1,
        "title": "Forces & Motion",
        "subtitle": "Introduction & Section 6.1: Concept, Effects, Vector Nature & Units",
        "speech": (
            "Welcome, students, to Chapter 6, How Forces Affect Motion. In Chapter 4, we learned how to "
            "describe motion using position, velocity, acceleration, and graphs. Now we ask a deeper question: "
            "what actually causes motion to start, speed up, slow down, or turn? The answer is force, and "
            "studying how forces act brings us to Isaac Newton's three laws of motion. From everyday experience, "
            "a push or pull can set a stationary football rolling, change a cricket ball's speed and direction "
            "when struck by a bat, or squeeze a lemon to change its shape. Notice that a force never acts "
            "without direction: pushing a heavy door inward is completely different from pulling it outward! "
            "Therefore, force is a vector quantity requiring both magnitude and direction. Its SI unit is the "
            "newton, written with capital N, named in honour of Isaac Newton. Whether a tiny raindrop falls "
            "under Earth's pull or a massive rocket blasts upward from a launchpad, every change in velocity "
            "traces back to forces acting on an object. Let us explore how forces are measured, combined, and "
            "connected to every movement in our universe with complete scientific clarity, everyday examples, and clear mathematical precision."
        ),
        "checkpoints": [
            {
                "question": "Which statement best describes the effects a force can produce on an object?",
                "options": [
                    "It can only increase speed",
                    "It can set a stationary object in motion, change speed or direction, or change shape",
                    "It can only change temperature",
                    "It acts without any direction"
                ],
                "answer": 1,
                "hint": "Think of kicking a football, hitting a cricket ball, and squeezing a lemon.",
                "explanation": "A force can start motion from rest, alter speed or direction, or deform an object's shape."
            },
            {
                "question": "Why is force classified as a vector quantity, and what is its SI unit?",
                "options": [
                    "It needs only magnitude; SI unit is metre",
                    "It needs both magnitude and direction; SI unit is newton (N)",
                    "It needs only time; SI unit is second",
                    "It has no unit in SI"
                ],
                "answer": 1,
                "hint": "Pushing left vs pushing right produces opposite results.",
                "explanation": "Force requires both magnitude and direction, and its SI unit is the newton (N)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Measuring Force",
        "subtitle": "Section 6.1.1: Spring Balance, Weight & Yoctonewton Precision",
        "speech": (
            "How do scientists measure the exact magnitude of a force? In the school laboratory, the classic "
            "instrument is a spring balance! Inside a spring balance sits a coiled steel spring attached to a "
            "pointer moving along a calibrated newton scale. When you pull the hook—or hang an object from "
            "it—the spring stretches in proportion to the applied pull. Hanging a mango or a metal block from "
            "the hook measures its weight, which is the downward gravitational pull of the Earth on that object. "
            "Notice the difference: mass stays the same everywhere, whereas weight is a force measured in "
            "newtons! Now look at Threads of Curiosity to see how sensitive force measurements can get. On "
            "your fingertips, human perception can barely feel a tiny feather-light tap around one millinewton, "
            "or ten to the minus three newtons. Yet modern physics laboratories using trapped ions and optical "
            "tweezers can detect astonishingly tiny forces down to yoctonewtons—around ten to the minus "
            "twenty-four newtons! From bridge-testing hydraulic presses to single-atom sensors, measuring force "
            "accurately lets engineers and scientists test materials, weigh payloads, and probe nature at every scale, "
            "from tiny atomic traps up to heavy suspension bridges carrying daily traffic."
        ),
        "checkpoints": [
            {
                "question": "What does a spring balance measure when an object hangs vertically from its hook?",
                "options": [
                    "The object's temperature",
                    "The gravitational pull (weight) acting on the object in newtons",
                    "The object's volume in litres",
                    "The atmospheric pressure"
                ],
                "answer": 1,
                "hint": "Weight is the downward force exerted by Earth's gravity.",
                "explanation": "A spring balance stretches in proportion to the applied force, measuring weight in newtons."
            },
            {
                "question": "In Threads of Curiosity, how do human touch thresholds compare with extreme lab sensors?",
                "options": [
                    "Humans feel ~10⁻³ N, while labs can measure down to ~10⁻²⁴ N (yoctonewtons)",
                    "Humans feel 10⁻²⁴ N, while labs only measure 100 N",
                    "Both stop at 1 N",
                    "Labs cannot measure forces below 1 N"
                ],
                "answer": 0,
                "hint": "Yocto- stands for 10⁻²⁴.",
                "explanation": "Human perception starts around 10⁻³ N, whereas ultra-sensitive lab setups detect ~10⁻²⁴ N."
            }
        ]
    },
    {
        "id": 3,
        "title": "Balanced & Unbalanced",
        "subtitle": "Section 6.2 & Example 6.1: Net Force, Tug-of-War & Couples",
        "speech": (
            "In real life, an object almost never experiences just one lonely force. When you push a heavy "
            "wooden crate across the floor, friction pushes backward against your push; when a plastic ball "
            "floats on a pond, Earth's gravity pulls downward while water's buoyant force pushes upward! To "
            "predict motion, we must find the net force—the vector sum of all forces acting on the object. "
            "Imagine a tug-of-war: if both teams pull with equal and opposite forces, the rope stays still "
            "because the net force is zero. These are balanced forces, and they cause zero change in motion. "
            "If one team pulls harder, the forces become unbalanced, producing a non-zero net force in the "
            "direction of the larger pull! Look at Example 6.1 with two forces of ten newtons and six newtons "
            "on a block. If both push right, they add to sixteen newtons right. If ten newtons pushes right "
            "and six newtons pushes left, they subtract to four newtons right; reverse them and you get four "
            "newtons left! In Ready to Go Beyond, notice what happens when two equal opposite forces act at "
            "different points—like turning a bicycle handlebar or a water tap: they form a couple causing rotation."
        ),
        "checkpoints": [
            {
                "question": "In Example 6.1, forces of 10 N right and 6 N left act along the same line on a block. What is the net force?",
                "options": [
                    "16 N right",
                    "4 N right",
                    "4 N left",
                    "0 N"
                ],
                "answer": 1,
                "hint": "Opposite forces subtract, and the net force points along the larger force.",
                "explanation": "10 N right - 6 N left = 4 N to the right (unbalanced net force)."
            },
            {
                "question": "What happens when two equal and opposite forces act along the same line (like a tied tug-of-war)?",
                "options": [
                    "They are balanced forces giving zero net force and no change in motion",
                    "The object accelerates rapidly",
                    "They always create a spinning couple",
                    "They double the object's mass"
                ],
                "answer": 0,
                "hint": "Equal magnitudes in opposite directions cancel out along the same line.",
                "explanation": "Balanced forces sum to zero net force, producing no change in the state of motion."
            }
        ]
    },
    {
        "id": 4,
        "title": "Force of Friction",
        "subtitle": "Section 6.3, Activities 6.1–6.2 & Galileo's Thought Experiment",
        "speech": (
            "Why does a rolling cricket ball eventually stop on grass even after you stop kicking it? Because "
            "of friction—a contact force that always opposes relative motion between touching surfaces! On a "
            "level floor, gravity pulls a box downward while the floor pushes straight upward with a perpendicular "
            "normal force, keeping vertical forces balanced. Horizontally, your push must exceed friction before "
            "sliding begins, and air drag also resists fast objects. Let us test surfaces in Activities 6.1 and "
            "6.2. In Activity 6.1, shoot a taped stack of coins with a stretched rubber band across a rough "
            "wooden table, a smoother laminated table, and a polished marble floor. On the smooth marble, velocity "
            "drops much more slowly and the coins glide farthest! In Activity 6.2, pull a wooden block with a "
            "spring balance: the threshold reading needed to start sliding is lowest on polished marble, proving "
            "smoother surfaces have lower friction. Long ago, people wrongly believed a continuous push was "
            "needed to keep anything moving. In Meet a Scientist, Galileo Galilei imagined removing all friction "
            "and air drag—proving that an object moving horizontally would glide forever at constant velocity! "
            "This brilliant realization overturned centuries of confusion and paved the way for Newton's laws."
        ),
        "checkpoints": [
            {
                "question": "What do Activities 6.1 and 6.2 demonstrate about smoother surfaces like polished marble?",
                "options": [
                    "They exert greater friction and stop coins sooner",
                    "They exert lower frictional force, letting coins glide farther with smaller threshold pull",
                    "They eliminate gravity completely",
                    "They require infinite force to start motion"
                ],
                "answer": 1,
                "hint": "Compare the rubber-band coin travel distance and spring-balance reading across surfaces.",
                "explanation": "Smoother surfaces produce less friction, so the spring balance threshold is smaller and coins travel farther."
            },
            {
                "question": "What did Galileo Galilei's thought experiment establish?",
                "options": [
                    "A continuous push is always required to maintain constant velocity",
                    "If all friction and impediments are removed, a moving object continues at constant velocity indefinitely",
                    "Heavier objects always stop faster on ice",
                    "Normal force points horizontally"
                ],
                "answer": 1,
                "hint": "Galileo overturned the ancient idea that rest is the only natural state.",
                "explanation": "Galileo showed that objects slow down because of friction; without friction, uniform motion continues forever."
            }
        ]
    },
    {
        "id": 5,
        "title": "Newton's First Law",
        "subtitle": "Section 6.4, Examples 6.2–6.3: Inertia & Zero Net Force Graphs",
        "speech": (
            "Building directly on Galileo's insight, Isaac Newton formulated his First Law of Motion: an object "
            "at rest remains at rest, and an object in motion continues moving with constant velocity—same speed "
            "and same straight-line direction—unless acted upon by a net external force! This natural tendency of "
            "every object to resist any change in its state of rest or uniform motion is called inertia. That is "
            "why passengers lurch forward when a bus brakes suddenly, and why shaking a tree branch drops ripe "
            "fruits. Let us check Example 6.2: suppose you push a heavy box across a floor with a forward force "
            "exactly equal and opposite to the backward friction force. Because the forward push and backward "
            "friction cancel out, the net force is zero, so the box glides forward at a steady constant velocity! "
            "Now look at Example 6.3, which draws motion graphs for zero net force. For a stationary object, "
            "the position-time graph is a flat horizontal line and the velocity-time graph sits along zero. For "
            "an object in uniform motion under zero net force, the position-time graph is a straight inclined "
            "line and the velocity-time graph is a flat horizontal line above zero!"
        ),
        "checkpoints": [
            {
                "question": "In Example 6.2, a box is pushed with a 40 N forward force while friction exerts 40 N backward. How does it move?",
                "options": [
                    "It accelerates continuously",
                    "It moves with constant velocity because net force is zero",
                    "It stops instantaneously",
                    "It moves backward"
                ],
                "answer": 1,
                "hint": "40 N forward + 40 N backward = 0 N net force.",
                "explanation": "By Newton's First Law, zero net force means zero acceleration, so a moving box maintains constant velocity."
            },
            {
                "question": "In Example 6.3, what do the s-t and v-t graphs look like for an object in uniform motion with zero net force?",
                "options": [
                    "Inclined straight s-t line and horizontal non-zero v-t line",
                    "Curved s-t line and sloped v-t line",
                    "Horizontal s-t line and zero v-t line",
                    "Vertical s-t line and curved v-t line"
                ],
                "answer": 0,
                "hint": "Constant non-zero velocity means steady slope on s-t and flat height on v-t.",
                "explanation": "Uniform motion produces a straight sloped s-t graph and a flat horizontal non-zero v-t graph."
            }
        ]
    },
    {
        "id": 6,
        "title": "Second Law Experiments",
        "subtitle": "Section 6.5, Activities 6.3 & 6.4: Force, Mass & Acceleration",
        "speech": (
            "What happens when forces on an object are NOT balanced? A non-zero net force produces acceleration! "
            "Let us see how scientists measure this relationship cleanly in Activities 6.3 and 6.4 using a low-friction "
            "lab cart connected by a string over a pulley to a small hanging mass cup. Using slow-motion video, "
            "students measure the exact time T taken for the cart to travel a fixed track distance s from rest, "
            "computing acceleration via s equals half a T squared. First, in Activity 6.3, keep the cart's mass "
            "unchanged and double the hanging mass in the cup, which doubles the pulling force! The travel time "
            "drops sharply, showing that acceleration increases in direct proportion to the net applied force: "
            "double the force, double the acceleration! Second, in Activity 6.4, keep the hanging pulling force "
            "constant, but double the total mass on the cart by adding extra blocks. Now the cart speeds up much "
            "more sluggishly, taking longer to cover distance s. Acceleration drops to half—proving acceleration "
            "is inversely proportional to mass! Larger mass means greater inertia, making it harder for the same "
            "force to change the object's velocity. Keep these two clear trends in mind as we write the law!"
        ),
        "checkpoints": [
            {
                "question": "In Activity 6.3, when the cart mass is fixed and the net pulling force is doubled, what happens to acceleration?",
                "options": [
                    "Acceleration drops to zero",
                    "Acceleration doubles (directly proportional to net force)",
                    "Acceleration halves",
                    "Acceleration stays unchanged"
                ],
                "answer": 1,
                "hint": "a is directly proportional to F when m is constant.",
                "explanation": "Doubling the net applied force on a constant mass doubles its acceleration."
            },
            {
                "question": "In Activity 6.4, when the pulling force is kept constant and the cart's mass is doubled, what happens to acceleration?",
                "options": [
                    "Acceleration doubles",
                    "Acceleration halves (inversely proportional to mass)",
                    "Acceleration quadruples",
                    "Acceleration stays unchanged"
                ],
                "answer": 1,
                "hint": "Greater mass means greater inertia resisting velocity change.",
                "explanation": "For a constant net force, acceleration is inversely proportional to mass, so doubling mass halves a."
            }
        ]
    },
    {
        "id": 7,
        "title": "Force & Momentum",
        "subtitle": "Section 6.5: F = ma, 1 Newton, Weight F = mg & Momentum p = mv",
        "speech": (
            "Combining Activities 6.3 and 6.4 gives us Newton's Second Law of Motion in crisp mathematical "
            "form: acceleration a equals net force F divided by mass m, or F equals m times a! From this "
            "equation, we define the SI unit newton cleanly: one newton is the force that gives a one-kilogram "
            "mass an acceleration of one metre per second squared. We can also calculate an object's weight "
            "instantly: since gravity accelerates falling objects at g equals nine point eight metres per second "
            "squared, Earth's gravitational pull is F equals m times g. A ten-kilogram backpack weighs ninety-eight "
            "newtons! Now look at Ready to Go Beyond for an even deeper view using momentum. Momentum, denoted "
            "by p, equals mass times velocity: p equals m v. A heavy truck moving slowly and a light bullet "
            "moving fast can both carry huge momentum! Because a equals v minus u over t, multiplying by m shows "
            "that F equals m v minus m u divided by t—meaning net force equals the rate of change of momentum "
            "delta p divided by delta t! This momentum viewpoint explains collisions and safety engineering "
            "across cars, sports equipment, and protective helmets used in everyday life."
        ),
        "checkpoints": [
            {
                "question": "How is 1 newton (1 N) defined from Newton's Second Law F = ma?",
                "options": [
                    "1 kg moving at 1 m/s",
                    "The force that accelerates a 1 kg mass at 1 m/s² (1 kg m s⁻²)",
                    "The force of 1 gram falling for 1 second",
                    "10 kg resting on a table"
                ],
                "answer": 1,
                "hint": "Substitute m = 1 kg and a = 1 m/s² into F = ma.",
                "explanation": "1 N = 1 kg × 1 m/s² = 1 kg m s⁻²."
            },
            {
                "question": "Using momentum p = mv, how does Newton's Second Law express net force?",
                "options": [
                    "Net force equals mass plus velocity",
                    "Net force equals the rate of change of momentum (Δp / Δt)",
                    "Net force equals momentum multiplied by time",
                    "Net force is always zero when momentum changes"
                ],
                "answer": 1,
                "hint": "Rewrite m(v - u)/t as Δ(mv)/Δt.",
                "explanation": "F = m(v - u)/t = Δp / Δt: net force equals the rate of change of momentum."
            }
        ]
    },
    {
        "id": 8,
        "title": "Impulse & Safety",
        "subtitle": "Section 6.5 Real-World Applications: Cricket Catch, Airbags & Coconuts",
        "speech": (
            "The momentum form of Newton's Second Law—force equals change in momentum divided by time—explains "
            "clever tricks in sports, road safety, and everyday life! Watch a skilled cricket fielder catching a "
            "fast-moving ball: instead of holding their hands rigid, the fielder pulls their hands backward "
            "smoothly as the ball lands. Why? Stopping the ball requires the exact same change in momentum "
            "delta p, but pulling the hands back increases the stopping time delta t! Since delta t sits in the "
            "denominator, a longer impact time drastically reduces the stinging force on the palms! Automotive "
            "airbags use the exact same physics during a car crash: inflating in milliseconds, the soft cushion "
            "extends the driver's stopping time, lowering peak impact force on the chest and head to prevent "
            "fatal injuries. Now flip the idea around: what if you want a HUGE force to crack open a hard "
            "coconut shell? You strike it with a rapid, high-velocity blow against a hard rock so the stopping "
            "time delta t is tiny—producing a massive peak force that shatters the shell instantly! Always remember "
            "this golden rule: longer stopping time cuts force, while shorter stopping time boosts peak impact force dramatically during collisions."
        ),
        "checkpoints": [
            {
                "question": "Why does a cricket fielder pull their hands backward while catching a fast ball?",
                "options": [
                    "To decrease the ball's mass",
                    "To increase stopping time Δt, thereby reducing the impact force F = Δp/Δt on their hands",
                    "To make the ball bounce higher",
                    "To eliminate momentum completely before touching it"
                ],
                "answer": 1,
                "hint": "With fixed Δp, larger Δt in the denominator gives smaller F.",
                "explanation": "Extending the catch duration Δt lowers the average impact force F = Δp / Δt."
            },
            {
                "question": "How do automotive airbags protect passengers during a collision?",
                "options": [
                    "They increase the car's mass",
                    "They extend stopping time during impact to reduce peak force on the body",
                    "They eliminate friction between tyres and road",
                    "They accelerate the passenger forward"
                ],
                "answer": 1,
                "hint": "Compare a soft airbag cushion with a hard steering wheel.",
                "explanation": "Airbags lengthen the deceleration time Δt, greatly reducing the force F = Δp/Δt on passengers."
            }
        ]
    }
]

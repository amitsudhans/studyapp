#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part3 = [
    {
        "id": 17,
        "title": "Forces & Inertia",
        "subtitle": "Silent Mastery Quiz 1: Forces, Spring Balance, Friction & First Law (10 Questions)",
        "questions": [
            {
                "question": "What is the SI unit of force, and is force a scalar or vector quantity?",
                "options": [
                    "Kilogram; scalar",
                    "Newton (N); vector (has both magnitude and direction)",
                    "Metre per second; scalar",
                    "Joule; vector"
                ],
                "answer": 1,
                "hint": "Force depends on both how hard and which way you push.",
                "explanation": "Force is a vector quantity measured in newtons (N).",
                "solution_steps": [
                    "Force requires both magnitude and direction, making it a vector.",
                    "Its SI unit is the newton (N), equal to 1 kg m s⁻².",
                    "Spring balances measure force magnitudes in newtons."
                ]
            },
            {
                "question": "In Example 6.1, two forces of 10 N and 6 N act in the SAME direction (right) on a block. What is the net force?",
                "options": [
                    "4 N right",
                    "4 N left",
                    "16 N right",
                    "0 N"
                ],
                "answer": 2,
                "hint": "Forces in the same direction add together.",
                "explanation": "10 N right + 6 N right = 16 N right.",
                "solution_steps": [
                    "Both forces point to the right.",
                    "Add magnitudes: 10 N + 6 N = 16 N.",
                    "Net force = 16 N to the right."
                ]
            },
            {
                "question": "What does a pair of equal, opposite, non-collinear forces (like turning a bicycle handlebar or tap) produce?",
                "options": [
                    "Zero motion of any kind",
                    "A couple that causes rotation",
                    "Pure linear acceleration",
                    "Increase in mass"
                ],
                "answer": 1,
                "hint": "Covered in Ready to Go Beyond under Section 6.2.",
                "explanation": "Two equal and opposite forces acting along parallel separated lines form a couple causing rotation.",
                "solution_steps": [
                    "Forces act in opposite directions at opposite ends of the handlebar.",
                    "They cancel translationally but create a turning effect.",
                    "This pair is called a couple, producing rotation."
                ]
            },
            {
                "question": "In Activity 6.1, a stack of coins shot with a rubber band glides farthest on which surface?",
                "options": [
                    "Rough wooden table top",
                    "Laminated table top",
                    "Polished marble/tile floor",
                    "Sandpaper"
                ],
                "answer": 2,
                "hint": "Smoother surfaces exert lower opposing friction.",
                "explanation": "Polished marble/tile has the lowest friction, so velocity decreases slowest and coins travel farthest.",
                "solution_steps": [
                    "Friction opposes relative sliding motion.",
                    "Polished marble/tile is smoother than wood or laminate.",
                    "Lower friction allows the coins to glide a longer distance."
                ]
            },
            {
                "question": "Which vertical forces balance each other for a heavy wooden box resting on a level floor?",
                "options": [
                    "Friction and air drag",
                    "Downward gravitational force (weight) and upward perpendicular normal force",
                    "Magnetic force and tension",
                    "Applied push and buoyancy"
                ],
                "answer": 1,
                "hint": "The floor pushes straight up perpendicular to the surface.",
                "explanation": "Downward weight is balanced by the upward normal force from the floor.",
                "solution_steps": [
                    "Earth pulls the box downward (gravitational force).",
                    "The floor exerts an equal upward normal force perpendicular to the surface.",
                    "Vertical net force is zero, so the box does not sink or lift."
                ]
            },
            {
                "question": "What did Galileo Galilei's thought experiment disprove?",
                "options": [
                    "That gravity pulls downward",
                    "The ancient misconception that a continuous force is needed to sustain uniform horizontal motion",
                    "That smoother surfaces have less friction",
                    "That mass has inertia"
                ],
                "answer": 1,
                "hint": "Think about what happens if friction is completely removed.",
                "explanation": "Galileo showed uniform motion continues indefinitely without force once friction is removed.",
                "solution_steps": [
                    "Ancient thinkers believed objects naturally stop unless pushed.",
                    "Galileo showed friction is what slows objects down.",
                    "Without friction, an object glides at constant velocity forever."
                ]
            },
            {
                "question": "In Example 6.2, a moving box is pushed forward with 35 N while friction opposes with 35 N. What happens?",
                "options": [
                    "The box speeds up steadily",
                    "The box continues moving at constant velocity",
                    "The box reverses direction",
                    "The box stops immediately"
                ],
                "answer": 1,
                "hint": "Net force = 35 N - 35 N = 0 N.",
                "explanation": "Zero net force means zero acceleration, so the already-moving box keeps constant velocity.",
                "solution_steps": [
                    "Forward applied force = 35 N; backward friction = 35 N.",
                    "Net force = 0 N.",
                    "By Newton's First Law, an object in motion stays at constant velocity."
                ]
            },
            {
                "question": "In Example 6.3, which graph pair represents a STATIONARY object under zero net force?",
                "options": [
                    "Sloped s-t line and horizontal non-zero v-t line",
                    "Horizontal s-t line at constant s, and v-t line along v = 0",
                    "Curved s-t line and sloped v-t line",
                    "Vertical s-t line and v-t line at 10 m/s"
                ],
                "answer": 1,
                "hint": "Stationary means position s never changes and velocity v is zero.",
                "explanation": "A stationary object has constant s (horizontal s-t line) and v = 0 (v-t line on the time axis).",
                "solution_steps": [
                    "At rest, position s remains constant over time (horizontal s-t line).",
                    "Velocity v equals zero at all times.",
                    "Hence the v-t graph lies along the horizontal axis (v = 0)."
                ]
            },
            {
                "question": "Why do standing bus passengers lurch backward when a stationary bus suddenly accelerates forward?",
                "options": [
                    "A backward force pushes their heads",
                    "Because of inertia of rest, their upper bodies tend to remain stationary while feet move forward with the floor",
                    "Gravity reverses",
                    "Air pressure pushes them"
                ],
                "answer": 1,
                "hint": "Recall Newton's First Law and inertia.",
                "explanation": "Their feet move forward with the bus floor, while their upper body resists velocity change due to inertia.",
                "solution_steps": [
                    "Before starting, the passenger's body is at rest.",
                    "When the bus jerks forward, friction moves the feet forward.",
                    "By inertia, the upper body tends to stay at rest, appearing to lurch backward."
                ]
            },
            {
                "question": "What is the approximate threshold of human force perception compared with extreme yoctonewton lab sensitivity?",
                "options": [
                    "10 N vs 10⁻³ N",
                    "10⁻³ N vs 10⁻²⁴ N",
                    "10⁻²⁴ N vs 10⁻³ N",
                    "100 N vs 1 N"
                ],
                "answer": 1,
                "hint": "Yoctonewton = 10⁻²⁴ N.",
                "explanation": "Human touch senses down to ~10⁻³ N, while labs detect forces down to ~10⁻²⁴ N.",
                "solution_steps": [
                    "Human perception threshold is roughly 1 millinewton (~10⁻³ N).",
                    "Precision physics experiments measure forces down to yoctonewtons (~10⁻²⁴ N).",
                    "This spans 21 orders of magnitude."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Force & Momentum",
        "subtitle": "Silent Mastery Quiz 2: F = ma, Activities 6.3–6.4, Momentum & Examples 6.4–6.6 (10 Questions)",
        "questions": [
            {
                "question": "In Activity 6.3, doubling the hanging mass pulling a constant-mass cart doubles the cart's acceleration. What law does this confirm?",
                "options": [
                    "a is directly proportional to net force F",
                    "a is inversely proportional to net force F",
                    "a is independent of F",
                    "a equals mass squared"
                ],
                "answer": 0,
                "hint": "Look at the numerator of a = F/m.",
                "explanation": "For fixed mass, doubling net force doubles acceleration (a ∝ F).",
                "solution_steps": [
                    "Cart mass m is held constant.",
                    "Doubling hanging force F halves T²/2? Actually T drops by √2 so a = 2s/T² doubles.",
                    "Thus acceleration is directly proportional to net force."
                ]
            },
            {
                "question": "In Activity 6.4, keeping the pulling force constant while doubling the cart's mass causes acceleration to:",
                "options": [
                    "Double",
                    "Halve",
                    "Quadruple",
                    "Stay the same"
                ],
                "answer": 1,
                "hint": "a = F / m with F constant.",
                "explanation": "Acceleration is inversely proportional to mass (a ∝ 1/m), so doubling m halves a.",
                "solution_steps": [
                    "Net pulling force F is held constant.",
                    "Total mass m is doubled to 2m.",
                    "New acceleration a' = F/(2m) = a/2."
                ]
            },
            {
                "question": "In Example 6.4, what upward force must a weightlifter apply to hold a 30 kg barbell steady against gravity (g = 9.8 m/s²)?",
                "options": [
                    "30 N",
                    "98 N",
                    "294 N",
                    "3000 N"
                ],
                "answer": 2,
                "hint": "Weight = m × g.",
                "explanation": "F = mg = 30 kg × 9.8 m/s² = 294 N.",
                "solution_steps": [
                    "Mass m = 30 kg, g = 9.8 m/s².",
                    "Downward weight = 30 × 9.8 = 294 N.",
                    "To hold it steady (net force 0), upward force = 294 N."
                ]
            },
            {
                "question": "In Example 6.5, a 25 kg block is pushed with 55 N against 50 N of friction for 2 s from rest. Find its displacement.",
                "options": [
                    "0.2 m",
                    "0.4 m",
                    "1.0 m",
                    "2.0 m"
                ],
                "answer": 1,
                "hint": "First find F_net = 5 N, then a = 5/25 = 0.2 m/s², then s = ½at².",
                "explanation": "a = 0.2 m/s², so s = ½ × 0.2 × 2² = 0.4 m.",
                "solution_steps": [
                    "Net force = 55 N - 50 N = 5 N.",
                    "Acceleration a = 5 / 25 = 0.2 m/s².",
                    "Displacement s = 0 + ½(0.2)(2²) = 0.4 m."
                ]
            },
            {
                "question": "In Example 6.6, a 1500 kg sports car brakes with deceleration a = -2 m/s² (west). What net force acts on it?",
                "options": [
                    "750 N",
                    "1500 N",
                    "-3000 N (3000 N west)",
                    "0 N"
                ],
                "answer": 2,
                "hint": "Use F = m × a.",
                "explanation": "F = 1500 kg × (-2 m/s²) = -3000 N (3000 N west).",
                "solution_steps": [
                    "Mass m = 1500 kg; acceleration a = -2 m/s².",
                    "F = ma = 1500 × (-2) = -3000 N.",
                    "The negative sign indicates 3000 N opposing eastward motion (west)."
                ]
            },
            {
                "question": "What is the momentum of a 60 kg sprinter running at 8 m/s?",
                "options": [
                    "7.5 kg m/s",
                    "68 kg m/s",
                    "480 kg m/s",
                    "960 kg m/s"
                ],
                "answer": 2,
                "hint": "Momentum p = m × v.",
                "explanation": "p = 60 kg × 8 m/s = 480 kg m/s.",
                "solution_steps": [
                    "Mass m = 60 kg, velocity v = 8 m/s.",
                    "Use p = mv.",
                    "p = 60 × 8 = 480 kg m/s."
                ]
            },
            {
                "question": "A 0.15 kg cricket ball moving at 20 m/s is stopped by a fielder in 0.25 s. What average force acts on the fielder's hands?",
                "options": [
                    "3 N",
                    "12 N",
                    "30 N",
                    "60 N"
                ],
                "answer": 1,
                "hint": "Calculate Δp = 0.15 × 20 = 3 kg m/s, then divide by Δt = 0.25 s.",
                "explanation": "F = Δp / Δt = (0.15 × 20) / 0.25 = 3 / 0.25 = 12 N.",
                "solution_steps": [
                    "Initial momentum = 0.15 × 20 = 3.0 kg m/s; final momentum = 0.",
                    "Magnitude of momentum change Δp = 3.0 kg m/s.",
                    "Average force F = 3.0 / 0.25 = 12 N."
                ]
            },
            {
                "question": "Why does cracking a coconut require a rapid high-velocity strike against a hard surface?",
                "options": [
                    "To make stopping time Δt very small, creating a huge peak impact force F = Δp/Δt",
                    "To make stopping time very long",
                    "To reduce momentum to zero slowly",
                    "To lower the coconut's mass"
                ],
                "answer": 0,
                "hint": "A tiny Δt in F = Δp/Δt produces a very large force.",
                "explanation": "A fast impact over a tiny stopping time Δt generates a massive force capable of cracking the shell.",
                "solution_steps": [
                    "Rapid speed gives high initial momentum.",
                    "Hitting a hard surface stops the shell in a tiny time Δt.",
                    "By F = Δp/Δt, tiny Δt produces a huge shattering force."
                ]
            },
            {
                "question": "A net force of 24 N acts on a 6 kg object initially at rest for 3 s. What final velocity does it reach?",
                "options": [
                    "4 m/s",
                    "8 m/s",
                    "12 m/s",
                    "18 m/s"
                ],
                "answer": 2,
                "hint": "Find a = F/m = 24/6 = 4 m/s², then v = u + at.",
                "explanation": "a = 4 m/s², so v = 0 + 4 × 3 = 12 m/s.",
                "solution_steps": [
                    "Acceleration a = F / m = 24 / 6 = 4 m/s².",
                    "Initial velocity u = 0 m/s, time t = 3 s.",
                    "v = u + at = 0 + 4 × 3 = 12 m/s."
                ]
            },
            {
                "question": "Which unit expression is strictly equivalent to 1 newton (1 N)?",
                "options": [
                    "1 kg m s⁻¹",
                    "1 kg m s⁻²",
                    "1 g cm s⁻¹",
                    "1 kg m² s⁻²"
                ],
                "answer": 1,
                "hint": "Check the SI units of mass × acceleration.",
                "explanation": "From F = ma, 1 N = 1 kg × 1 m s⁻² = 1 kg m s⁻².",
                "solution_steps": [
                    "Mass is in kg; acceleration is in m s⁻².",
                    "F = ma gives kg × m s⁻².",
                    "Therefore 1 N = 1 kg m s⁻²."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Action-Reaction Systems",
        "subtitle": "Silent Mastery Quiz 3: Action-Reaction, Rockets, Gun Recoil & Multi-Body Systems (10 Questions)",
        "questions": [
            {
                "question": "In Activity 6.5, sitting on a wheeled chair and pushing a heavy table forward causes you to roll:",
                "options": [
                    "Forward into the table",
                    "Backward, because the table pushes you backward with equal and opposite force",
                    "Sideways only",
                    "Not at all"
                ],
                "answer": 1,
                "hint": "Action on table is forward; reaction on you is backward.",
                "explanation": "The table exerts an equal backward reaction force on your hands, rolling your wheeled chair backward.",
                "solution_steps": [
                    "You exert a forward force on the heavy table.",
                    "By Newton's Third Law, the table exerts an equal backward force on you.",
                    "Since the chair has wheels, you accelerate backward."
                ]
            },
            {
                "question": "How does a canoe oar propel a canoe forward through water?",
                "options": [
                    "The paddle pushes water forward, and water pushes the canoe backward",
                    "The paddle pushes water backward, and water pushes the canoe forward",
                    "Gravity pulls the canoe horizontally",
                    "Air resistance pulls the paddle"
                ],
                "answer": 1,
                "hint": "Action on water vs reaction on paddle/canoe.",
                "explanation": "Pushing water backward creates an equal forward reaction force from the water onto the canoe.",
                "solution_steps": [
                    "The oarsman uses the paddle to push water backward.",
                    "Water exerts an equal and opposite forward force on the paddle and canoe.",
                    "This forward reaction propels the canoe."
                ]
            },
            {
                "question": "Why can a rocket accelerate in the airless vacuum of outer space?",
                "options": [
                    "It pushes against moon dust",
                    "It expels hot exhaust gases backward, and the gases push the rocket forward (Third Law)",
                    "Outer space is full of dense air",
                    "Gravity pushes rockets upward"
                ],
                "answer": 1,
                "hint": "A rocket pushes against its own escaping exhaust, not external air.",
                "explanation": "Action-reaction between the rocket and its high-speed exhaust works equally well in vacuum.",
                "solution_steps": [
                    "Rocket engines push hot exhaust gases backward at high speed.",
                    "By Newton's Third Law, the exhaust gases exert an equal forward force on the rocket.",
                    "No external air is needed for this internal action-reaction."
                ]
            },
            {
                "question": "In Example 6.8, a 2 N force fires a 0.1 kg bullet from a 5 kg gun. Why is the bullet's acceleration 50 times larger than the gun's?",
                "options": [
                    "The bullet experiences 50 times more force",
                    "Both feel 2 N, and a = F/m is inversely proportional to mass (5 kg / 0.1 kg = 50)",
                    "The gun has no inertia",
                    "Friction doubles the bullet's mass"
                ],
                "answer": 1,
                "hint": "Compare m_gun = 5 kg and m_bullet = 0.1 kg under the same 2 N force.",
                "explanation": "Equal 2 N forces produce a_bullet = 2/0.1 = 20 m/s² and a_gun = 2/5 = 0.4 m/s² (ratio 50:1).",
                "solution_steps": [
                    "Third Law gives equal 2 N forces on bullet and gun.",
                    "Bullet acceleration = 2 / 0.1 = 20 m/s².",
                    "Gun acceleration = 2 / 5 = 0.4 m/s² (20 / 0.4 = 50×)."
                ]
            },
            {
                "question": "Two blocks of masses m₁ = 3 kg and m₂ = 7 kg are joined by a taut string on a frictionless surface and pulled by F = 40 N. Find the acceleration.",
                "options": [
                    "2 m/s²",
                    "4 m/s²",
                    "5.7 m/s²",
                    "13.3 m/s²"
                ],
                "answer": 1,
                "hint": "Use a = F / (m₁ + m₂).",
                "explanation": "a = 40 / (3 + 7) = 40 / 10 = 4 m/s².",
                "solution_steps": [
                    "Total system mass = 3 kg + 7 kg = 10 kg.",
                    "Internal string tension T cancels for the combined system.",
                    "a = 40 N / 10 kg = 4 m/s²."
                ]
            },
            {
                "question": "In the previous two-block system (m₁ = 3 kg front, m₂ = 7 kg rear, a = 4 m/s²), what is the tension T in the connecting string?",
                "options": [
                    "12 N",
                    "28 N",
                    "40 N",
                    "10 N"
                ],
                "answer": 1,
                "hint": "Only tension T pulls the rear 7 kg block forward: T = m₂ × a.",
                "explanation": "T = m₂ × a = 7 kg × 4 m/s² = 28 N.",
                "solution_steps": [
                    "Isolate the rear block m₂ = 7 kg.",
                    "The only horizontal force pulling m₂ is tension T.",
                    "T = m₂a = 7 × 4 = 28 N."
                ]
            },
            {
                "question": "Do Newton's Third Law action-reaction pairs apply to non-contact forces like magnetism and gravity?",
                "options": [
                    "No, only when objects touch",
                    "Yes, magnets and gravitating bodies exert equal and opposite forces on each other across space",
                    "Only for electric charges, not magnets",
                    "Only on Earth's surface"
                ],
                "answer": 1,
                "hint": "Think of Example 6.7 (falling fruit and Earth) and two bar magnets.",
                "explanation": "Third Law holds universally for both contact and non-contact forces.",
                "solution_steps": [
                    "Magnet A exerts force F on Magnet B; Magnet B exerts -F on Magnet A.",
                    "Earth pulls a falling fruit with F; the fruit pulls Earth with -F.",
                    "Thus Third Law applies to all contact and non-contact forces."
                ]
            },
            {
                "question": "When a person climbs a coconut tree, what is the action-reaction pair that moves them upward?",
                "options": [
                    "Climber pushes trunk downward; trunk pushes climber upward",
                    "Climber pulls air upward; air pushes trunk downward",
                    "Gravity pushes climber upward",
                    "Leaves pull climber upward"
                ],
                "answer": 0,
                "hint": "Think of hands and feet pressing down against the tree trunk.",
                "explanation": "Hands and feet push downward on the trunk, and the trunk's upward reaction lifts the climber.",
                "solution_steps": [
                    "The climber grips and pushes downward on the tree trunk.",
                    "The trunk exerts an equal upward reaction force on the climber.",
                    "This upward force overcomes gravity to lift the climber."
                ]
            },
            {
                "question": "If a boat's two oarsmen produce 120 N forward thrust while water drag opposes with 40 N, what is the net force on the boat?",
                "options": [
                    "160 N forward",
                    "80 N forward",
                    "40 N backward",
                    "0 N"
                ],
                "answer": 1,
                "hint": "Subtract opposing drag from forward thrust.",
                "explanation": "Net force = 120 N forward - 40 N backward = 80 N forward.",
                "solution_steps": [
                    "Forward thrust = 120 N; opposing water drag = 40 N.",
                    "F_net = 120 - 40 = 80 N.",
                    "The boat accelerates forward under 80 N net force."
                ]
            },
            {
                "question": "Why does a compass needle rotate to align north-south when placed on a table?",
                "options": [
                    "Because of air wind",
                    "Earth's magnetic field exerts a non-contact magnetic force/torque on the needle",
                    "Gravity pulls it sideways",
                    "Friction spins it continuously"
                ],
                "answer": 1,
                "hint": "From Revise, Reflect, Refine: non-contact magnetic interaction.",
                "explanation": "Earth's magnetic field exerts a non-contact magnetic force on the magnetized needle.",
                "solution_steps": [
                    "A compass needle is a small pivoted magnet.",
                    "Earth's magnetic field acts on it without physical contact.",
                    "This magnetic torque rotates the needle toward magnetic north."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Mastery",
        "subtitle": "Silent Mastery Quiz 4: Integrated Force, Graph, Bullet & Capstan Problems (10 Questions)",
        "questions": [
            {
                "question": "A 0.02 kg bullet travelling at 200 m/s embeds 0.1 m into a wooden block before stopping. What average resistive force did the wood exert?",
                "options": [
                    "400 N",
                    "2000 N",
                    "4000 N",
                    "8000 N"
                ],
                "answer": 2,
                "hint": "Use v² = u² + 2as to find deceleration a, then F = ma.",
                "explanation": "0 = 200² + 2a(0.1) ⇒ a = -40000 / 0.2 = -200,000 m/s²; F = 0.02 × 200,000 = 4000 N.",
                "solution_steps": [
                    "Use v² = u² + 2as: 0 = 40,000 + 0.2a ⇒ a = -200,000 m/s².",
                    "Apply F = ma = 0.02 kg × 200,000 m/s².",
                    "Average resistive force = 4000 N opposing motion."
                ]
            },
            {
                "question": "A 1000 kg car accelerates from rest to 20 m/s in 10 s, then cruises at 20 m/s for 5 s. What are the net forces in the two phases?",
                "options": [
                    "2000 N, then 2000 N",
                    "2000 N, then 0 N",
                    "200 N, then 0 N",
                    "0 N, then 2000 N"
                ],
                "answer": 1,
                "hint": "Phase 1: a = 20/10 = 2 m/s²; Phase 2: constant velocity ⇒ a = 0.",
                "explanation": "Phase 1: F = 1000 × 2 = 2000 N; Phase 2: F = 1000 × 0 = 0 N.",
                "solution_steps": [
                    "Phase 1 acceleration a₁ = (20 - 0)/10 = 2 m/s² ⇒ F₁ = 1000 × 2 = 2000 N.",
                    "Phase 2 constant speed ⇒ a₂ = 0 m/s².",
                    "F₂ = 1000 × 0 = 0 N."
                ]
            },
            {
                "question": "Three blocks (2 kg, 3 kg, 5 kg) are tied in a line on a smooth floor and pulled by 50 N. Find the acceleration.",
                "options": [
                    "2 m/s²",
                    "5 m/s²",
                    "10 m/s²",
                    "25 m/s²"
                ],
                "answer": 1,
                "hint": "Treat all three blocks as one system of total mass 10 kg.",
                "explanation": "Total mass = 2 + 3 + 5 = 10 kg; a = 50 / 10 = 5 m/s².",
                "solution_steps": [
                    "Combine all three masses: m_total = 2 + 3 + 5 = 10 kg.",
                    "All internal string tensions cancel within the system.",
                    "a = F / m_total = 50 / 10 = 5 m/s²."
                ]
            },
            {
                "question": "A 50 kg skater stands on frictionless ice and throws a 2 kg medicine ball forward at 10 m/s. At what speed does the skater recoil?",
                "options": [
                    "0.2 m/s",
                    "0.4 m/s",
                    "2.0 m/s",
                    "5.0 m/s"
                ],
                "answer": 1,
                "hint": "Action-reaction gives equal opposite momentum impulses: m_skater × v_skater = m_ball × v_ball.",
                "explanation": "50 × v = 2 × 10 = 20 ⇒ v = 20 / 50 = 0.4 m/s backward.",
                "solution_steps": [
                    "Equal and opposite forces over the same throw time give equal momentum magnitudes.",
                    "Ball momentum = 2 kg × 10 m/s = 20 kg m/s.",
                    "Skater recoil speed = 20 / 50 = 0.4 m/s."
                ]
            },
            {
                "question": "Which engineering technique minimizes friction by replacing sliding contact with magnetic suspension?",
                "options": [
                    "Capstan rope wrapping",
                    "Maglev (magnetic levitation) trains",
                    "Increasing normal force",
                    "Rough rubber braking"
                ],
                "answer": 1,
                "hint": "Electromagnets lift the train above the rails.",
                "explanation": "Maglev eliminates track contact friction using magnetic levitation.",
                "solution_steps": [
                    "Sliding and rolling contact both create friction.",
                    "Maglev trains float slightly above the guideway via electromagnets.",
                    "Zero track contact eliminates rail friction."
                ]
            },
            {
                "question": "Why does wrapping a mooring rope 4 times around a dock bollard (capstan effect) let one sailor hold a giant ship?",
                "options": [
                    "Each wrap multiplies frictional grip exponentially",
                    "Water turns into solid ice",
                    "The ship's mass becomes zero",
                    "Normal force disappears"
                ],
                "answer": 0,
                "hint": "Covered in The Journey Beyond.",
                "explanation": "Multiple wraps around a cylinder multiply friction exponentially, holding huge loads with a small pull.",
                "solution_steps": [
                    "Rope presses inward against the cylindrical post around each turn.",
                    "Frictional resistance compounds exponentially with wrap angle.",
                    "A small holding force on the free end balances enormous ship tension."
                ]
            },
            {
                "question": "If a box of mass 12 kg is pulled by 40 N right and 16 N left on a frictionless surface, what is its acceleration?",
                "options": [
                    "2 m/s² right",
                    "2 m/s² left",
                    "4.67 m/s² right",
                    "0 m/s²"
                ],
                "answer": 0,
                "hint": "Find net force first: 40 - 16 = 24 N right.",
                "explanation": "F_net = 24 N right; a = 24 / 12 = 2 m/s² right.",
                "solution_steps": [
                    "Net force = 40 N right - 16 N left = 24 N right.",
                    "Mass m = 12 kg.",
                    "a = F_net / m = 24 / 12 = 2 m/s² right."
                ]
            },
            {
                "question": "A car's velocity-time graph is a flat horizontal line at v = 25 m/s. What is the net force acting on the car?",
                "options": [
                    "Equal to its weight",
                    "0 N (balanced forces)",
                    "25 N",
                    "Increasing steadily"
                ],
                "answer": 1,
                "hint": "Horizontal v-t line means zero slope (zero acceleration).",
                "explanation": "Zero acceleration implies zero net force (forward engine thrust balances friction and air drag).",
                "solution_steps": [
                    "Horizontal v-t line ⇒ velocity is constant at 25 m/s.",
                    "Acceleration a = slope = 0 m/s².",
                    "By F = ma, net force = 0 N."
                ]
            },
            {
                "question": "Which statement about an action-reaction pair is ALWAYS true?",
                "options": [
                    "They act on the same object",
                    "They are equal in magnitude, opposite in direction, simultaneous, and act on two different objects",
                    "Reaction occurs 1 second after action",
                    "Action is larger than reaction for heavier objects"
                ],
                "answer": 1,
                "hint": "Review Section 6.6 carefully.",
                "explanation": "Action and reaction are always simultaneous, equal, opposite, and act on two distinct objects.",
                "solution_steps": [
                    "Both forces arise at the exact same instant.",
                    "Magnitudes are strictly equal regardless of mass.",
                    "They act on two different interacting bodies."
                ]
            },
            {
                "question": "Which historic 1687 book by Isaac Newton first presented the three laws of motion?",
                "options": [
                    "Aryabhatiya",
                    "Principia Mathematica",
                    "Ganitakaumudi",
                    "Origin of Species"
                ],
                "answer": 1,
                "hint": "Mentioned in The Journey Beyond historical readings.",
                "explanation": "Isaac Newton published his three laws of motion in Principia Mathematica (1687).",
                "solution_steps": [
                    "Isaac Newton unified mechanics and gravitation in 1687.",
                    "The work is titled Philosophiæ Naturalis Principia Mathematica.",
                    "It remains the foundation of classical physics."
                ]
            }
        ]
    }
]

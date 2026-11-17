#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part3 = [
    {
        "id": 17,
        "title": "Work & Energy",
        "subtitle": "Silent Mastery Quiz 1: Work Sign, Zero Work, Graphs & Work-Energy Theorem (10 Questions)",
        "questions": [
            {
                "question": "A porter lifts a 20 kg suitcase vertically by 1.5 m (g = 10 m/s²). How much work does the porter do?",
                "options": [
                    "30 J",
                    "200 J",
                    "300 J",
                    "0 J"
                ],
                "answer": 2,
                "hint": "Force needed = mg = 20 × 10 = 200 N; W = F × s.",
                "explanation": "W = 200 N × 1.5 m = 300 J.",
                "solution_steps": [
                    "Upward lifting force F = mg = 20 × 10 = 200 N.",
                    "Vertical displacement s = 1.5 m in the same upward direction.",
                    "W = F × s = 200 × 1.5 = 300 J."
                ]
            },
            {
                "question": "A boy pushes a rigid brick wall with 150 N for 30 seconds, and the wall does not move. How much scientific work is done on the wall?",
                "options": [
                    "4500 J",
                    "150 J",
                    "5 J",
                    "0 J"
                ],
                "answer": 3,
                "hint": "Check displacement s of the wall.",
                "explanation": "Since displacement s = 0 m, W = F × 0 = 0 J.",
                "solution_steps": [
                    "Applied force F = 150 N.",
                    "The rigid wall does not move, so displacement s = 0 m.",
                    "Work done W = 150 × 0 = 0 J."
                ]
            },
            {
                "question": "In Example 7.1, when you lower a heavy dumbbell slowly from chest height to the floor, the work done by your upward holding force is:",
                "options": [
                    "Positive",
                    "Negative",
                    "Zero",
                    "Infinite"
                ],
                "answer": 1,
                "hint": "Holding force points upward while displacement is downward.",
                "explanation": "Because holding force (up) opposes displacement (down), work done is negative.",
                "solution_steps": [
                    "Your hands exert an upward supporting force to control the descent.",
                    "The dumbbell's displacement is downward.",
                    "Opposite directions of force and displacement yield negative work."
                ]
            },
            {
                "question": "In Example 7.2, a goalkeeper stops a moving football by applying 200 N opposite to a 0.15 m displacement. Calculate the work done.",
                "options": [
                    "+30 J",
                    "-30 J",
                    "-200 J",
                    "+15 J"
                ],
                "answer": 1,
                "hint": "W = F × (-s).",
                "explanation": "W = 200 N × (-0.15 m) = -30 J.",
                "solution_steps": [
                    "Retarding force = 200 N opposite to motion.",
                    "Displacement = 0.15 m.",
                    "W = -200 × 0.15 = -30 J."
                ]
            },
            {
                "question": "A satellite orbits Earth in a circular path under Earth's inward gravitational pull. How much work does gravity do during this circular motion?",
                "options": [
                    "Positive work",
                    "Negative work",
                    "Zero work (force is perpendicular at 90° to tangential displacement)",
                    "Infinite work"
                ],
                "answer": 2,
                "hint": "Gravity points radially inward while instantaneous motion is along the tangent.",
                "explanation": "Because centripetal gravity is always at 90° to tangential displacement, it does zero work.",
                "solution_steps": [
                    "Gravitational force points toward Earth's centre (radial).",
                    "Satellite displacement at any instant is along the tangent.",
                    "Angle between force and displacement is 90°, so W = 0 J."
                ]
            },
            {
                "question": "A Force–Displacement graph is a horizontal line at F = 12 N from s = 0 m to s = 5 m, then drops linearly to F = 0 N at s = 9 m. Find total work done.",
                "options": [
                    "60 J",
                    "84 J",
                    "108 J",
                    "48 J"
                ],
                "answer": 1,
                "hint": "Add the rectangle area (5 × 12) and the triangle area (½ × 4 × 12).",
                "explanation": "Rectangle = 60 J; Triangle = ½ × 4 × 12 = 24 J; Total = 60 + 24 = 84 J.",
                "solution_steps": [
                    "Area from 0 to 5 m (rectangle) = 5 × 12 = 60 J.",
                    "Area from 5 to 9 m (triangle) = ½ × (9 - 5) × 12 = 24 J.",
                    "Total work = 60 + 24 = 84 J."
                ]
            },
            {
                "question": "In Example 7.3 (carrom shot), when the fast striker hits a stationary white coin and sets it moving, the striker does:",
                "options": [
                    "Negative work on the white coin",
                    "Positive work on the white coin, transferring energy to it",
                    "Zero work on the white coin",
                    "Only thermal work"
                ],
                "answer": 1,
                "hint": "The white coin gains kinetic energy in the direction of the push.",
                "explanation": "The striker exerts forward force causing forward displacement, doing positive work and transferring energy.",
                "solution_steps": [
                    "Striker pushes the white coin forward.",
                    "White coin moves forward in the same direction.",
                    "Positive work transfers kinetic energy from striker to coin."
                ]
            },
            {
                "question": "Which scientist experimentally established the quantitative link between mechanical work and heat energy?",
                "options": [
                    "James Watt",
                    "James Prescott Joule",
                    "Isaac Newton",
                    "Archimedes"
                ],
                "answer": 1,
                "hint": "1 J is named in his honour.",
                "explanation": "James Prescott Joule demonstrated the mechanical equivalent of heat.",
                "solution_steps": [
                    "James Prescott Joule used falling weights to turn paddles in water.",
                    "He measured the exact temperature rise produced by mechanical work.",
                    "The SI unit of energy/work, the joule (J), is named after him."
                ]
            },
            {
                "question": "Which energy interconversion occurs inside an electric water heater (geyser)?",
                "options": [
                    "Thermal energy → electrical energy",
                    "Electrical energy → thermal energy",
                    "Chemical energy → nuclear energy",
                    "Light energy → potential energy"
                ],
                "answer": 1,
                "hint": "Electric current heats the water.",
                "explanation": "A water heater converts electrical energy into thermal (heat) energy.",
                "solution_steps": [
                    "Current flows through a high-resistance heating coil.",
                    "Electrical energy is converted into thermal energy.",
                    "Thermal energy warms the surrounding water."
                ]
            },
            {
                "question": "Is work a scalar or a vector quantity, and why can it be negative?",
                "options": [
                    "Vector; because it points north",
                    "Scalar; it has magnitude and sign (+ or -) indicating energy added or removed, without spatial direction",
                    "Vector; measured in newtons",
                    "Scalar; it can never be negative"
                ],
                "answer": 1,
                "hint": "Work transfers scalar energy into (+) or out of (-) a system.",
                "explanation": "Work is a scalar quantity; its + or - sign shows whether energy is added to or removed from the object.",
                "solution_steps": [
                    "Work has no directional arrow in space, so it is a scalar.",
                    "Positive sign means energy flows into the object.",
                    "Negative sign means opposing force removes energy from the object."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Kinetic & Potential",
        "subtitle": "Silent Mastery Quiz 2: K = ½mv², U = mgh & Conservation of ME (10 Questions)",
        "questions": [
            {
                "question": "A 4 kg object moves at 5 m/s. What is its kinetic energy?",
                "options": [
                    "20 J",
                    "50 J",
                    "100 J",
                    "10 J"
                ],
                "answer": 1,
                "hint": "Use K = ½mv².",
                "explanation": "K = ½ × 4 × 5² = 2 × 25 = 50 J.",
                "solution_steps": [
                    "Mass m = 4 kg, speed v = 5 m/s.",
                    "Apply K = ½mv² = ½ × 4 × 25.",
                    "Kinetic energy K = 50 J."
                ]
            },
            {
                "question": "If the speed of a car triples from v to 3v, by what factor does its kinetic energy increase?",
                "options": [
                    "3 times",
                    "6 times",
                    "9 times",
                    "12 times"
                ],
                "answer": 2,
                "hint": "K is proportional to v².",
                "explanation": "(3v)² = 9v², so kinetic energy becomes 9 times larger.",
                "solution_steps": [
                    "K = ½mv².",
                    "New speed = 3v ⇒ K_new = ½m(3v)² = 9(½mv²).",
                    "Kinetic energy increases by a factor of 9."
                ]
            },
            {
                "question": "In Example 7.6, a 15,000 kg jet lands and is stopped in 100 m by a 367,500 N tail-hook retarding force. What was its landing speed?",
                "options": [
                    "35 m/s",
                    "50 m/s",
                    "70 m/s (252 km/h)",
                    "100 m/s"
                ],
                "answer": 2,
                "hint": "Work done by retarding force = ½mv²: 367,500 × 100 = ½ × 15,000 × v².",
                "explanation": "36,750,000 = 7500 v² ⇒ v² = 4900 ⇒ v = 70 m/s.",
                "solution_steps": [
                    "Magnitude of retarding work = 367,500 × 100 = 36,750,000 J.",
                    "Set equal to initial KE: 36,750,000 = ½(15,000)v² = 7500v².",
                    "v² = 4900 ⇒ v = 70 m/s (252 km/h)."
                ]
            },
            {
                "question": "Which object stores ELASTIC potential energy?",
                "options": [
                    "A stretched slingshot or bent archer's bow",
                    "A ball rolling on a flat floor",
                    "A bulb glowing brightly",
                    "Hot water in a kettle"
                ],
                "answer": 0,
                "hint": "Elastic potential energy comes from reversible deformation.",
                "explanation": "Deforming a slingshot, bow, or spring stores elastic potential energy.",
                "solution_steps": [
                    "Stretching or bending deforms an elastic material.",
                    "Work done in deforming it is stored as elastic potential energy.",
                    "Releasing it converts that stored U into kinetic energy."
                ]
            },
            {
                "question": "A 2 kg stone is lifted 5 m above the ground (g = 9.8 m/s²). How much gravitational potential energy does it gain?",
                "options": [
                    "10 J",
                    "49 J",
                    "98 J",
                    "196 J"
                ],
                "answer": 2,
                "hint": "Use U = mgh.",
                "explanation": "U = 2 × 9.8 × 5 = 98 J.",
                "solution_steps": [
                    "Mass m = 2 kg, g = 9.8 m/s², height h = 5 m.",
                    "Use U = mgh.",
                    "U = 2 × 9.8 × 5 = 98 J."
                ]
            },
            {
                "question": "A 1 kg ball is dropped from rest at height 20 m (g = 10 m/s²). What is its kinetic energy after falling 12 m (at height 8 m)?",
                "options": [
                    "80 J",
                    "120 J",
                    "200 J",
                    "0 J"
                ],
                "answer": 1,
                "hint": "Total ME = 200 J; at height 8 m, U = 80 J, so K = ME - U.",
                "explanation": "Total ME = 1×10×20 = 200 J; at 8 m, U = 80 J ⇒ K = 200 - 80 = 120 J.",
                "solution_steps": [
                    "Initial total mechanical energy = mgh = 1 × 10 × 20 = 200 J.",
                    "At height 8 m, potential energy U = 1 × 10 × 8 = 80 J.",
                    "By conservation, K = 200 - 80 = 120 J."
                ]
            },
            {
                "question": "In Activity 7.2 (simple pendulum), at extreme positions P and R, what are the values of K and U?",
                "options": [
                    "K is maximum, U is zero",
                    "K is zero (bob pauses momentarily), U is maximum",
                    "Both K and U are zero",
                    "K equals U"
                ],
                "answer": 1,
                "hint": "The bob stops for an instant at the highest points of its swing.",
                "explanation": "At extremes P and R, speed is zero (K = 0) and height is maximum (maximum U).",
                "solution_steps": [
                    "At turning points P and R, the bob's velocity is instantaneously 0 m/s.",
                    "Thus kinetic energy K = 0.",
                    "All mechanical energy is stored as gravitational potential energy U."
                ]
            },
            {
                "question": "In Example 7.8, a child slides down a frictionless slide of vertical height h = 5 m (g = 10 m/s²). What is the child's speed at the bottom?",
                "options": [
                    "5 m/s",
                    "10 m/s",
                    "15 m/s",
                    "50 m/s"
                ],
                "answer": 1,
                "hint": "Use v = √(2gh).",
                "explanation": "v = √(2 × 10 × 5) = √100 = 10 m/s.",
                "solution_steps": [
                    "Equate top PE to bottom KE: mgh = ½mv².",
                    "Cancel m: v = √(2gh).",
                    "v = √(2 × 10 × 5) = √100 = 10 m/s."
                ]
            },
            {
                "question": "Why does a runaway truck escape ramp in Example 7.9 use both an upward slope AND loose sand?",
                "options": [
                    "Upward slope converts KE into gravitational PE, while sand drag dissipates remaining KE safely",
                    "Sand makes the truck go faster",
                    "Upward slope reduces truck mass",
                    "Both increase kinetic energy"
                ],
                "answer": 0,
                "hint": "Two mechanisms drain the truck's kinetic energy together.",
                "explanation": "Climbing stores energy as mgh while sand friction does negative work, stopping the truck in 20 m.",
                "solution_steps": [
                    "Initial KE must be reduced to zero.",
                    "Climbing the 30° incline converts KE into gravitational PE.",
                    "Loose sand exerts 50,000 N drag, dissipating remaining energy."
                ]
            },
            {
                "question": "If total mechanical energy of a roller coaster is 5000 J and at a hill crest its potential energy is 3200 J, what is its kinetic energy?",
                "options": [
                    "8200 J",
                    "1800 J",
                    "3200 J",
                    "0 J"
                ],
                "answer": 1,
                "hint": "ME = K + U.",
                "explanation": "K = ME - U = 5000 - 3200 = 1800 J.",
                "solution_steps": [
                    "Total mechanical energy ME = K + U = 5000 J.",
                    "At the crest, U = 3200 J.",
                    "K = 5000 - 3200 = 1800 J."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Power & Machines",
        "subtitle": "Silent Mastery Quiz 3: Power, Pulleys, Inclined Planes & Levers (10 Questions)",
        "questions": [
            {
                "question": "In Example 7.11, a 1000 kg car accelerates from rest to 72 km/h (20 m/s) in 10 s. What is the average engine power?",
                "options": [
                    "2000 W",
                    "10,000 W",
                    "20,000 W",
                    "200,000 W"
                ],
                "answer": 2,
                "hint": "First find KE = ½mv² = 200,000 J, then divide by t = 10 s.",
                "explanation": "KE = ½(1000)(20²) = 200,000 J; P = 200,000 / 10 = 20,000 W.",
                "solution_steps": [
                    "Convert 72 km/h = 20 m/s.",
                    "Work/KE gained = ½ × 1000 × 20² = 200,000 J.",
                    "Power P = 200,000 / 10 = 20,000 W (20 kW)."
                ]
            },
            {
                "question": "A water pump rated at 2 horsepower (1 hp = 746 W) runs for 10 seconds. How much work does it do?",
                "options": [
                    "1492 J",
                    "7460 J",
                    "14,920 J",
                    "746 J"
                ],
                "answer": 2,
                "hint": "Power = 2 × 746 = 1492 W; Work = Power × time.",
                "explanation": "P = 1492 W; W = 1492 × 10 = 14,920 J.",
                "solution_steps": [
                    "Convert 2 hp to watts: 2 × 746 = 1492 W.",
                    "Use W = P × t.",
                    "W = 1492 × 10 = 14,920 J."
                ]
            },
            {
                "question": "How is Mechanical Advantage (MA) of a simple machine defined?",
                "options": [
                    "Effort / Load",
                    "Load / Effort",
                    "Load × Effort",
                    "Work / Time"
                ],
                "answer": 1,
                "hint": "MA > 1 means a small effort lifts a large load.",
                "explanation": "Mechanical Advantage = Load / Effort.",
                "solution_steps": [
                    "Load is the resistive force/weight to be overcome.",
                    "Effort is the force you apply.",
                    "MA = Load / Effort."
                ]
            },
            {
                "question": "An ideal movable pulley system has Mechanical Advantage = 4. What effort is needed to lift a 600 N crate?",
                "options": [
                    "2400 N",
                    "600 N",
                    "150 N",
                    "100 N"
                ],
                "answer": 2,
                "hint": "Effort = Load / MA.",
                "explanation": "Effort = 600 N / 4 = 150 N.",
                "solution_steps": [
                    "Given Load = 600 N and MA = 4.",
                    "Use MA = Load / Effort ⇒ Effort = Load / MA.",
                    "Effort = 600 / 4 = 150 N."
                ]
            },
            {
                "question": "A wooden ramp 6 m long raises crates to a truck bed 1.5 m high. What is the ideal Mechanical Advantage of this inclined plane?",
                "options": [
                    "0.25",
                    "4.0",
                    "4.5",
                    "9.0"
                ],
                "answer": 1,
                "hint": "Use MA = L / h.",
                "explanation": "MA = 6 m / 1.5 m = 4.0.",
                "solution_steps": [
                    "Ramp length L = 6 m; vertical height h = 1.5 m.",
                    "For an ideal inclined plane, MA = L / h.",
                    "MA = 6 / 1.5 = 4.0."
                ]
            },
            {
                "question": "Using the Principle of Moments, a 400 N load sits 0.5 m from a lever's fulcrum. What effort applied 2.0 m from the fulcrum balances it?",
                "options": [
                    "100 N",
                    "200 N",
                    "800 N",
                    "1600 N"
                ],
                "answer": 0,
                "hint": "Effort × Effort Arm = Load × Load Arm.",
                "explanation": "Effort × 2.0 = 400 × 0.5 = 200 ⇒ Effort = 100 N.",
                "solution_steps": [
                    "Apply F₁d₁ = F₂d₂: Effort × 2.0 = 400 × 0.5.",
                    "Effort × 2.0 = 200.",
                    "Effort = 200 / 2.0 = 100 N."
                ]
            },
            {
                "question": "Which class of lever has the Load located in the middle (between Fulcrum and Effort)?",
                "options": [
                    "Class I (e.g., scissors)",
                    "Class II (e.g., wheelbarrow, bottle opener)",
                    "Class III (e.g., tweezers)",
                    "Fixed pulley"
                ],
                "answer": 1,
                "hint": "F-L-E: Class I = F, Class II = L, Class III = E.",
                "explanation": "Class II levers place Load between Fulcrum and Effort.",
                "solution_steps": [
                    "Class I: Fulcrum in middle (seesaw, crowbar).",
                    "Class II: Load in middle (wheelbarrow, lemon squeezer).",
                    "Class III: Effort in middle (tongs, tweezers)."
                ]
            },
            {
                "question": "Which tool is a Class III lever?",
                "options": [
                    "Bottle opener",
                    "Crowbar",
                    "Kitchen tongs / tweezers",
                    "Wheelbarrow"
                ],
                "answer": 2,
                "hint": "Your hand squeezes in the middle while the tip holds the food/object.",
                "explanation": "Tongs, tweezers, brooms, and oars apply Effort between Fulcrum and Load (Class III).",
                "solution_steps": [
                    "In tongs, the hinge at the back is the fulcrum.",
                    "The food held at the front tip is the load.",
                    "Your fingers squeeze in the middle (Effort), making it Class III."
                ]
            },
            {
                "question": "What is the Mechanical Advantage of a single fixed pulley used to lift a bucket from a well?",
                "options": [
                    "MA = 1 (changes direction of pull only)",
                    "MA = 2",
                    "MA = 0.5",
                    "MA = 10"
                ],
                "answer": 0,
                "hint": "With one fixed pulley, Effort equals Load ideally.",
                "explanation": "A single fixed pulley has ideal MA = 1 and makes lifting convenient by letting you pull downward.",
                "solution_steps": [
                    "Effort equals Load in an ideal single fixed pulley.",
                    "MA = Load / Effort = 1.",
                    "It helps by changing the direction of effort."
                ]
            },
            {
                "question": "Why does an inclined plane NOT violate the conservation of energy even though it cuts the required force?",
                "options": [
                    "Because you must push the load over a proportionally longer distance L along the slope",
                    "Because gravity turns off on ramps",
                    "Because friction creates energy",
                    "Because mass shrinks on ramps"
                ],
                "answer": 0,
                "hint": "Work = Force × Distance; smaller force × longer distance = same work.",
                "explanation": "Reducing force by factor L/h increases distance by L/h, keeping ideal work mgh unchanged.",
                "solution_steps": [
                    "Ideal work along ramp = Effort × L.",
                    "Ideal vertical work = Load × h.",
                    "Smaller Effort is compensated by longer distance L, conserving work."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Mastery",
        "subtitle": "Silent Mastery Quiz 4: Integrated Energy, Gharat, Levers & Cosmology (10 Questions)",
        "questions": [
            {
                "question": "A 2 kg block slides down a curved frictionless track from height 1.8 m onto a rough horizontal floor where 6 N friction stops it. How far does it slide on the floor (g = 10 m/s²)?",
                "options": [
                    "3 m",
                    "6 m",
                    "9 m",
                    "12 m"
                ],
                "answer": 1,
                "hint": "Initial PE = mgh = 2 × 10 × 1.8 = 36 J; friction work = 6 N × d.",
                "explanation": "36 J = 6 N × d ⇒ d = 6 m.",
                "solution_steps": [
                    "Initial potential energy = mgh = 2 × 10 × 1.8 = 36 J.",
                    "All 36 J is dissipated by 6 N friction on the floor.",
                    "Distance d = 36 / 6 = 6 m."
                ]
            },
            {
                "question": "How does a traditional Himalayan gharat (panchakki) mill grain without electricity or fossil fuels?",
                "options": [
                    "Channeled stream water converts PE to KE and spins blades coupled to a grinding stone",
                    "Wind turns a solar panel",
                    "Magnets levitate the wheat",
                    "Sublimation of ice turns the wheel"
                ],
                "answer": 0,
                "hint": "Covered in Bridging Science and Society.",
                "explanation": "Falling stream water converts gravitational PE to KE, spinning the wooden water wheel and millstone.",
                "solution_steps": [
                    "Mountain stream at height holds gravitational potential energy.",
                    "Water rushing down a chute converts PE into kinetic energy.",
                    "Water jet spins the wheel shaft and circular grinding stone."
                ]
            },
            {
                "question": "A child of mass 20 kg sits 1.5 m from a seesaw fulcrum. Where should a 30 kg child sit on the opposite side to balance?",
                "options": [
                    "0.5 m",
                    "1.0 m",
                    "1.5 m",
                    "2.25 m"
                ],
                "answer": 1,
                "hint": "20 × 1.5 = 30 × d₂.",
                "explanation": "30 = 30 × d₂ ⇒ d₂ = 1.0 m.",
                "solution_steps": [
                    "Apply Principle of Moments: 20 × 1.5 = 30 × d₂.",
                    "30 = 30 × d₂.",
                    "d₂ = 1.0 m from the fulcrum."
                ]
            },
            {
                "question": "Two machines A and B lift identical 500 N loads by 4 m. Machine A takes 10 s; Machine B takes 20 s. Compare their work and power.",
                "options": [
                    "Same work (2000 J); Machine A has double the power (200 W vs 100 W)",
                    "Machine A does double the work",
                    "Machine B has double the power",
                    "Both have 200 W power"
                ],
                "answer": 0,
                "hint": "Work = 500 × 4 = 2000 J for both; Power = Work / time.",
                "explanation": "Both do 2000 J of work, while Machine A delivers 2000/10 = 200 W vs 2000/20 = 100 W.",
                "solution_steps": [
                    "Work W = 500 N × 4 m = 2000 J for both.",
                    "Power of A = 2000 / 10 = 200 W.",
                    "Power of B = 2000 / 20 = 100 W (A is twice as powerful)."
                ]
            },
            {
                "question": "In Revise, Reflect, Refine, if a Potential Energy–Displacement (U–x) curve has a valley at U = 10 J and total mechanical energy is ME = 25 J, what is K at the valley?",
                "options": [
                    "10 J",
                    "15 J",
                    "25 J",
                    "35 J"
                ],
                "answer": 1,
                "hint": "K = ME - U.",
                "explanation": "K = 25 J - 10 J = 15 J.",
                "solution_steps": [
                    "Total mechanical energy ME = K + U = 25 J.",
                    "At the valley, U = 10 J.",
                    "Kinetic energy K = 25 - 10 = 15 J."
                ]
            },
            {
                "question": "Which statement about Mechanical Advantage of an ideal lever is TRUE when Effort Arm is 60 cm and Load Arm is 15 cm?",
                "options": [
                    "MA = 0.25",
                    "MA = 4",
                    "MA = 45",
                    "MA = 75"
                ],
                "answer": 1,
                "hint": "MA = Effort Arm / Load Arm.",
                "explanation": "MA = 60 cm / 15 cm = 4.",
                "solution_steps": [
                    "Effort Arm L₁ = 60 cm; Load Arm L₂ = 15 cm.",
                    "MA = L₁ / L₂ = 60 / 15.",
                    "MA = 4."
                ]
            },
            {
                "question": "A 60 kg student runs up a flight of stairs rising 5 m vertically in 6 s (g = 10 m/s²). What is the student's power output?",
                "options": [
                    "300 W",
                    "500 W",
                    "600 W",
                    "3000 W"
                ],
                "answer": 1,
                "hint": "Work = mgh = 60 × 10 × 5 = 3000 J; divide by 6 s.",
                "explanation": "W = 3000 J; P = 3000 / 6 = 500 W.",
                "solution_steps": [
                    "Work against gravity = mgh = 60 × 10 × 5 = 3000 J.",
                    "Time t = 6 s.",
                    "Power P = 3000 / 6 = 500 W."
                ]
            },
            {
                "question": "Which everyday pair consists of one Class I lever and one Class II lever respectively?",
                "options": [
                    "Scissors (Class I) and Wheelbarrow (Class II)",
                    "Tongs (Class I) and Tweezers (Class II)",
                    "Broom (Class I) and Oar (Class II)",
                    "Bottle opener (Class I) and Crowbar (Class II)"
                ],
                "answer": 0,
                "hint": "Scissors have Fulcrum in middle; Wheelbarrow has Load in middle.",
                "explanation": "Scissors (Fulcrum middle) = Class I; Wheelbarrow (Load middle) = Class II.",
                "solution_steps": [
                    "Scissors pivot at central screw (Fulcrum middle) ⇒ Class I.",
                    "Wheelbarrow holds Load between wheel (Fulcrum) and handles (Effort) ⇒ Class II.",
                    "Hence Scissors & Wheelbarrow is the correct pair."
                ]
            },
            {
                "question": "Why does dark energy appear in The Quest Continues at the end of this energy chapter?",
                "options": [
                    "It powers household water heaters",
                    "It is the unknown cosmic phenomenon accelerating the expansion of the universe",
                    "It is stored in compressed springs",
                    "It increases friction in simple machines"
                ],
                "answer": 1,
                "hint": "Distant galaxies are accelerating apart rather than slowing under gravity.",
                "explanation": "Dark energy is the mysterious driver causing the universe's expansion to accelerate.",
                "solution_steps": [
                    "Gravity pulls matter together, expected to slow cosmic expansion.",
                    "Observations show cosmic expansion is actually accelerating.",
                    "Scientists attribute this acceleration to dark energy."
                ]
            },
            {
                "question": "A Force–Displacement graph shows a constant force of 15 N acting from s = 2 m to s = 8 m. How much work is done?",
                "options": [
                    "30 J",
                    "90 J",
                    "120 J",
                    "150 J"
                ],
                "answer": 1,
                "hint": "Displacement Δs = 8 - 2 = 6 m.",
                "explanation": "W = 15 N × (8 - 2) m = 15 × 6 = 90 J.",
                "solution_steps": [
                    "Displacement interval Δs = 8 m - 2 m = 6 m.",
                    "Constant force F = 15 N.",
                    "Work = rectangle area = 15 × 6 = 90 J."
                ]
            }
        ]
    }
]

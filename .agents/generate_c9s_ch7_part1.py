#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part1 = [
    {
        "id": 1,
        "title": "Work & Energy",
        "subtitle": "Introduction & Section 7.1: Constant Force, Joule & Force-Displacement Graph",
        "speech": (
            "Welcome, students, to Chapter 7, Work, Energy, and Simple Machines. In Chapters 4 and 6, we studied "
            "kinematics and Newton's laws, but analyzing complex or time-varying forces directly can become tricky. "
            "Work, energy, and power give us a remarkably simpler framework! Notice first how everyday words differ "
            "from physics: in daily life, energy powers walking from food, spinning fans from electricity, and "
            "driving cars from fuel, while studying for exams feels like hard work. Scientifically, work has a "
            "strict definition. Imagine lifting five-kilogram wheat bags onto a shelf. Lifting three bags by one "
            "metre takes three times the force, and lifting one bag by three metres takes force over three times "
            "the distance! Therefore, work done by a constant force equals force multiplied by displacement in the "
            "direction of the force: W equals F times s. Its SI unit is the joule, where one joule equals one "
            "newton times one metre. Work is a scalar quantity—it has magnitude and sign, but no direction. Even "
            "Even when force varies along a path, the total area under a Force-Displacement graph equals total work "
            "done! Let us master these foundational ideas carefully, step by step, using our interactive graph and "
            "calculator right here."
        ),
        "checkpoints": [
            {
                "question": "How is work done by a constant force mathematically defined, and what is its SI unit?",
                "options": [
                    "W = F / s; unit is watt",
                    "W = F × s (in the direction of force); unit is joule (J = N·m)",
                    "W = m × v; unit is newton",
                    "W = F × t; unit is kilogram"
                ],
                "answer": 1,
                "hint": "Work combines force magnitude and displacement along the force.",
                "explanation": "W = F × s, measured in joules (1 J = 1 N · 1 m = 1 kg m² s⁻²)."
            },
            {
                "question": "What does the area enclosed under a Force–Displacement graph represent?",
                "options": [
                    "Average velocity",
                    "Total work done (even for non-constant forces)",
                    "Instantaneous power",
                    "Mass of the object"
                ],
                "answer": 1,
                "hint": "Area multiplies vertical Force (N) by horizontal Displacement (m).",
                "explanation": "Force × displacement equals work, so the area under an F–s graph gives total work done."
            }
        ]
    },
    {
        "id": 2,
        "title": "Zero, Positive, Negative",
        "subtitle": "Sections 7.1.1 & 7.1.2: Zero Work, Examples 7.1 & 7.2",
        "speech": (
            "In physics, pushing with all your might does not guarantee positive work! Let us check when scientific "
            "work equals zero, positive, or negative. Work is strictly zero in three situations: first, when net "
            "applied force is zero; second, when displacement is zero, such as pushing a rigid concrete wall until "
            "you are exhausted without moving it an inch; and third, when force acts perpendicular—at ninety "
            "degrees—to displacement! For example, when you carry a heavy box horizontally across a room, your "
            "upward support force is at ninety degrees to horizontal motion, so your support force does zero work! "
            "Now compare positive and negative work. Positive work occurs when force and displacement point in the "
            "same direction, like pushing a wheelchair forward. Negative work occurs when force opposes displacement. "
            "Look at Example 7.1 with a dumbbell: lifting it upward means upward force and upward displacement, "
            "giving positive work; lowering it slowly means your upward holding force opposes downward displacement, "
            "giving negative work! In Example 7.2, a goalkeeper applies a two-hundred-newton backward force over "
            "zero point one five metres to stop a football, doing minus thirty joules of work on the ball! Remember, "
            "negative work removes kinetic energy from a moving object."
        ),
        "checkpoints": [
            {
                "question": "A person carries a 15 kg box horizontally at constant height across a 10 m room. How much work does the upward support force do?",
                "options": [
                    "150 J",
                    "1470 J",
                    "0 J (because upward force is at 90° to horizontal displacement)",
                    "-150 J"
                ],
                "answer": 2,
                "hint": "Check the angle between upward holding force and horizontal displacement.",
                "explanation": "Force perpendicular (90°) to displacement performs zero work."
            },
            {
                "question": "In Example 7.2, a goalkeeper stops a football by applying 200 N opposite to a 0.15 m forward displacement. What is the work done?",
                "options": [
                    "+30 J",
                    "-30 J",
                    "+1333 J",
                    "0 J"
                ],
                "answer": 1,
                "hint": "Force and displacement are in opposite directions, so work is negative.",
                "explanation": "W = 200 N × (-0.15 m) = -30 J (negative work)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Work-Energy Theorem",
        "subtitle": "Sections 7.2 & 7.3: Energy Capacity, Joule, Example 7.3 & Forms",
        "speech": (
            "What exactly is energy? Scientists define energy as the capacity to do work! A fast cricket ball "
            "carries energy because it can knock down wooden wickets on impact; a flowerpot perched on a high "
            "balcony stores energy because it can dent the ground if it falls. This brings us to one of physics' "
            "greatest bridges—the Work-Energy Theorem: the net work done on an object or system equals the change "
            "in its energy! In Meet a Scientist, James Prescott Joule proved that mechanical work and thermal "
            "energy are directly interchangeable, earning his name for the SI unit of both work and energy. Watch "
            "Example 7.3 on a carrom board: your hand does positive work accelerating the striker, transferring "
            "energy to it; the striker hits a white coin, doing positive work on it; and the white coin strikes "
            "a black coin, passing energy onward! Beyond motion, Section 7.3 reminds us that energy takes many "
            "forms—mechanical, thermal, light, sound, electrical, nuclear, and chemical—and constantly converts "
            "between them, such as electrical energy heating water in a geyser or chemical food energy powering "
            "muscular movement during sports, walking, and everyday household chores. Energy is never created out of "
            "nothing; it simply transfers and transforms."
        ),
        "checkpoints": [
            {
                "question": "What does the Work-Energy Theorem state?",
                "options": [
                    "Energy is always destroyed when work is done",
                    "Net work done on an object or system equals the change in its energy (W = ΔE)",
                    "Power equals force times distance",
                    "Work is independent of energy"
                ],
                "answer": 1,
                "hint": "Doing positive work increases a system's energy; negative work decreases it.",
                "explanation": "The Work-Energy Theorem states that Work Done = ΔEnergy."
            },
            {
                "question": "Who famously demonstrated the mechanical equivalence connecting mechanical work and thermal energy?",
                "options": [
                    "James Prescott Joule",
                    "Galileo Galilei",
                    "John Tyndall",
                    "Aryabhata"
                ],
                "answer": 0,
                "hint": "The SI unit of energy and work is named after him.",
                "explanation": "James Prescott Joule established that mechanical work converts quantitatively into thermal energy."
            }
        ]
    },
    {
        "id": 4,
        "title": "Kinetic Energy",
        "subtitle": "Section 7.4.1 & Examples 7.4–7.6: K = ½mv² & Jet Landing",
        "speech": (
            "Let us examine Mechanical Energy—energy possessed due to motion or position—starting with Kinetic "
            "Energy, denoted by K, the energy of motion! Let us derive its exact formula cleanly. Suppose a force "
            "F accelerates mass m from initial velocity u to final velocity v over displacement s. From Chapter 4, "
            "v squared equals u squared plus two a s, so s equals v squared minus u squared over two a. Multiply "
            "by Newton's second law, F equals m a: work W equals m a times s, which simplifies to half m times "
            "v squared minus u squared! Starting from rest at u equals zero, kinetic energy becomes K equals half "
            "m v squared! Notice Example 7.4: because speed is squared, doubling a car's speed quadruples its "
            "kinetic energy fourfold! In Example 7.5, a zero-point-two-kilogram cricket ball bowled at forty-three "
            "metres per second carries half times zero point two times forty-three squared, or one hundred and "
            "eighty-four point nine joules. And in Example 7.6, an aircraft carrier's tail-hook exerts a retarding "
            "force of three hundred sixty-seven thousand five hundred newtons over one hundred metres to stop a "
            "fifteen-thousand-kilogram jet, revealing an initial landing speed of seventy metres per second!"
        ),
        "checkpoints": [
            {
                "question": "In Example 7.4, if a vehicle's speed doubles from v to 2v, what happens to its kinetic energy?",
                "options": [
                    "It doubles",
                    "It quadruples (becomes 4 times)",
                    "It halves",
                    "It stays unchanged"
                ],
                "answer": 1,
                "hint": "K = ½mv² depends on the square of velocity.",
                "explanation": "Replacing v with 2v gives ½m(2v)² = 4(½mv²), so kinetic energy quadruples."
            },
            {
                "question": "In Example 7.5, what is the kinetic energy of a 0.2 kg cricket ball moving at 43 m/s?",
                "options": [
                    "8.6 J",
                    "43.0 J",
                    "184.9 J",
                    "369.8 J"
                ],
                "answer": 2,
                "hint": "Compute ½ × 0.2 × 43².",
                "explanation": "K = 0.1 × 1849 = 184.9 J."
            }
        ]
    },
    {
        "id": 5,
        "title": "Potential Energy",
        "subtitle": "Section 7.4.2, Activity 7.1 & Example 7.7: Stored Energy U = mgh",
        "speech": (
            "Can a stationary object still hold energy? Yes! Potential energy, denoted by U, is energy stored "
            "due to deformation, configuration, or relative position. Stretch a rubber slingshot, bend an archer's "
            "wooden bow, or compress a coiled spring—you store elastic potential energy ready to launch a projectile! "
            "Similarly, two repelling magnets pushed close together, electric charges, or a stone lifted above "
            "Earth store potential energy in their system. Let us focus on gravitational potential energy. In "
            "Activity 7.1, drop an iron ball into a tray of soft sand from a height of one metre, then drop it "
            "from two metres. The higher drop carves a noticeably deeper crater in the sand, proving greater height "
            "stores greater energy! How much energy? Raising mass m steadily to height h requires lifting force "
            "equal to weight m g over vertical distance h, so work done—and stored gravitational potential energy—is "
            "U equals m g h! Look at Example 7.7: throwing a two-hundred-gram, or zero-point-two-kilogram, ball "
            "ten metres high using g equals ten metres per second squared stores zero point two times ten times "
            "ten, or twenty joules of gravitational potential energy at its peak! Test different masses and drop "
            "heights in the interactive sand-tray simulator beside this slide."
        ),
        "checkpoints": [
            {
                "question": "In Activity 7.1, why does dropping a ball from 2 m create a deeper dent in sand than dropping it from 1 m?",
                "options": [
                    "Gravity is twice as strong at 2 m",
                    "Greater height stores more gravitational potential energy (U = mgh), which converts to more kinetic energy on impact",
                    "The ball's mass doubles at 2 m",
                    "Sand becomes softer at 2 m"
                ],
                "answer": 1,
                "hint": "Compare U = mgh at h = 2 m versus h = 1 m.",
                "explanation": "Doubling height doubles stored gravitational potential energy U = mgh, doing more work on the sand."
            },
            {
                "question": "In Example 7.7, what is the gravitational potential energy of a 200 g (0.2 kg) ball at height 10 m (g = 10 m/s²)?",
                "options": [
                    "2 J",
                    "20 J",
                    "200 J",
                    "2000 J"
                ],
                "answer": 1,
                "hint": "Convert 200 g to 0.2 kg first, then use U = mgh.",
                "explanation": "U = 0.2 kg × 10 m/s² × 10 m = 20 J."
            }
        ]
    },
    {
        "id": 6,
        "title": "Energy Conservation",
        "subtitle": "Section 7.4.3 & Activity 7.2: Free Fall & Pendulum ME = K + U",
        "speech": (
            "Now comes one of the most elegant laws in all of science: the Conservation of Mechanical Energy! "
            "In a closed system with only conservative forces like gravity and zero friction, total mechanical "
            "energy—the sum of kinetic energy K and potential energy U—remains strictly constant! Let us prove "
            "this for free fall from height h. At the top before release, velocity is zero, so K is zero and U "
            "equals m g h, giving total energy m g h. After falling for time t, the object drops distance half "
            "g t squared, so it loses potential energy equal to half m g squared t squared. Meanwhile, its speed "
            "grows to v equals g t, giving kinetic energy half m times g t squared, which is half m g squared t "
            "squared! Loss in potential energy equals gain in kinetic energy, keeping K plus U equal to m g h "
            "every single instant! Watch Activity 7.2 with a swinging simple pendulum: at the high extreme points "
            "P and R, the bob pauses momentarily with maximum potential energy and zero kinetic energy; swinging "
            "through the lowest point Q, all that stored potential energy transforms smoothly into maximum kinetic energy!"
        ),
        "checkpoints": [
            {
                "question": "During free fall without air resistance, what happens to potential energy U, kinetic energy K, and total ME = K + U?",
                "options": [
                    "U increases, K decreases, ME increases",
                    "U decreases, K increases by the same amount, and total ME remains constant at mgh",
                    "Both U and K drop to zero",
                    "ME doubles halfway down"
                ],
                "answer": 1,
                "hint": "Energy converts from position-based U into motion-based K.",
                "explanation": "Loss in potential energy equals gain in kinetic energy, conserving total mechanical energy mgh."
            },
            {
                "question": "In Activity 7.2 (simple pendulum), where is kinetic energy maximum and potential energy minimum?",
                "options": [
                    "At extreme point P",
                    "At extreme point R",
                    "At the lowest mean point Q",
                    "Nowhere during the swing"
                ],
                "answer": 2,
                "hint": "The bob moves fastest at the bottom of its arc.",
                "explanation": "At lowest point Q, height is minimum (minimum U) and speed is maximum (maximum K)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Slides & Ramps",
        "subtitle": "Examples 7.8 & 7.9: Frictionless Slide Speed & Runaway Truck Escape Ramp",
        "speech": (
            "Conservation of mechanical energy solves tricky real-world engineering problems effortlessly! Look "
            "at Example 7.8: a child slides down a curved, frictionless playground slide of vertical height h. "
            "Setting potential energy at the top, m g h, equal to kinetic energy at the bottom, half m v squared, "
            "mass m cancels out completely—yielding v equals square root of two g h! Amazingly, the child's exit "
            "speed depends only on vertical height h, NOT on the slide's curve shape or the child's mass! Now "
            "what when friction IS present, like a braking vehicle? Look at Example 7.9: a ten-thousand-kilogram "
            "runaway truck barrels down a mountain road at seventy-two kilometres per hour, or twenty metres per "
            "second, and enters a thirty-degree upward sand escape ramp! Its initial kinetic energy is half times "
            "ten thousand times twenty squared, which equals two million joules. As the truck climbs distance L "
            "up the thirty-degree ramp, vertical height rises by L sine thirty degrees, or half L, storing "
            "potential energy, while fifty-thousand-newton sand drag removes energy. Solving the complete energy balance "
            "shows a minimum ramp length of twenty metres stops the heavy truck safely! Try adjusting the truck "
            "speed and ramp angle in our simulator to verify the exact stopping distance."
        ),
        "checkpoints": [
            {
                "question": "In Example 7.8, what does a child's speed at the bottom of a frictionless slide of height h depend on?",
                "options": [
                    "The child's mass and the slide's curve shape",
                    "Only vertical height h and gravity g (v = √(2gh)), independent of mass or curve shape",
                    "Only the child's mass",
                    "Only the length of the ladder"
                ],
                "answer": 1,
                "hint": "In mgh = ½mv², m cancels out on both sides.",
                "explanation": "Energy conservation gives v = √(2gh), independent of mass or slide curvature."
            },
            {
                "question": "In Example 7.9, a 10,000 kg runaway truck at 20 m/s climbs a 30° sand escape ramp (sand drag = 50,000 N). What minimum ramp length L stops it?",
                "options": [
                    "5 m",
                    "10 m",
                    "20 m",
                    "40 m"
                ],
                "answer": 2,
                "hint": "Initial KE (2,000,000 J) = sand friction work (50,000 L) + gravity PE (10,000 × 10 × 0.5 L).",
                "explanation": "2,000,000 = 50,000 L + 50,000 L = 100,000 L ⇒ L = 20 m."
            }
        ]
    },
    {
        "id": 8,
        "title": "Power & Watt",
        "subtitle": "Section 7.5 & Examples 7.10–7.11: Rate of Work, Watt & Horsepower",
        "speech": (
            "Suppose two cranes lift identical steel beams to the same roof: Crane A finishes in ten seconds, "
            "while Crane B takes fifty seconds. Both do the exact same work, yet Crane A is far more powerful! "
            "Power, denoted by P, measures the rate of doing work—or energy transferred per unit time: P equals "
            "W divided by t. Its SI unit is the watt, named after James Watt, where one watt equals one joule "
            "per second. In Meet a Scientist, James Watt dramatically improved steam engine efficiency, and "
            "introduced the practical unit horsepower to compare engines against workhorses—where one horsepower "
            "equals seven hundred and forty-six watts! Let us solve Examples 7.10 and 7.11. In Example 7.10, a "
            "weightlifter raises a seventy-five-kilogram barbell by two metres in five seconds using g equals ten "
            "metres per second squared. Work done is seventy-five times ten times two, or fifteen hundred joules; "
            "dividing by five seconds gives three hundred watts! In Example 7.11, a one-thousand-kilogram car "
            "accelerates from rest to twenty metres per second in ten seconds, gaining two hundred thousand joules "
            "of kinetic energy—giving an average engine power output of twenty thousand watts, or twenty kilowatts! "
            "Always remember that power tells us how fast energy is transferred."
        ),
        "checkpoints": [
            {
                "question": "In Example 7.10, a weightlifter raises 75 kg by 2 m in 5 s (take g = 10 m/s²). What is the power output?",
                "options": [
                    "150 W",
                    "300 W",
                    "750 W",
                    "1500 W"
                ],
                "answer": 1,
                "hint": "Work = mgh = 75 × 10 × 2 = 1500 J; then divide by t = 5 s.",
                "explanation": "P = W / t = 1500 J / 5 s = 300 W."
            },
            {
                "question": "What is the relationship between the SI unit watt (W) and the historical unit horsepower (hp)?",
                "options": [
                    "1 hp = 100 W",
                    "1 hp = 746 W",
                    "1 W = 746 hp",
                    "1 hp = 1000 W"
                ],
                "answer": 1,
                "hint": "James Watt defined horsepower for comparing steam engines to draft horses.",
                "explanation": "1 horsepower (hp) equals 746 watts (746 J/s)."
            }
        ]
    }
]

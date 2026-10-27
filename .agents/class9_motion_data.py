# -*- coding: utf-8 -*-
"""
Class 9 Science - Chapter 9: Motion
Curriculum Data with 20 Slides:
- Slides 1-16: Core Content with 32 In-Slide Checkpoints (2 per slide) and 16 Bespoke Simulators
- Slides 17-20: 4 Dedicated Quiz Challenge Slides (40 Questions Total, 10 per slide) with Step-by-Step Pop-up Solutions
- Full alignment with competencies: C-2.1, C-8.1, C-8.2
"""

SLIDES_DATA = [
    {
        "id": 1,
        "badge": "Slide 01 • Competency C-2.1",
        "title": "Describing Motion, Reference Points & Relative Frames",
        "subtitle": "Why an object can be at rest and in motion at the same time",
        "teacher": "Welcome to our Motion Master Lab! In everyday life, we see birds flying, fish swimming, blood rushing through veins, and planets orbiting stars. But what is motion? An object is in motion when its position changes continuously with time relative to a chosen reference point. Notice that motion is always relative—a passenger sitting next to you on a moving train appears at rest to you, but to someone standing on the platform, both of you are hurtling forward at full speed!",
        "theory": [
            "<strong>Definition of Motion:</strong> An object is said to be in <strong>motion</strong> if its position changes continuously with respect to a stationary reference frame or origin as time passes.",
            "<strong>Reference Point (Origin):</strong> To describe the position of an object, we must specify a reference point called the <strong>origin</strong>. For example, stating that 'a school is 2 km north of the railway station' uses the railway station as the reference point.",
            "<strong>The Relativity of Rest and Motion:</strong>",
            "• Rest and motion are not absolute; they are <strong>relative concepts</strong> dependent entirely on the observer's frame of reference.",
            "• <em>Example:</em> For passengers inside a moving bus, their fellow passengers are at rest (their relative distance remains unchanged). However, to an observer standing by the roadside, the bus, its passengers, and their luggage are all moving forward. Concurrently, the roadside trees appear to move backwards to the passengers!",
            "<strong>Rectilinear Motion (Motion in a Straight Line):</strong> The simplest type of motion is motion along a straight-line path in one dimension. We represent this on a one-dimensional coordinate axis with an origin \\(O\\)."
        ],
        "key_points": [
            "Motion is the change in position of an object over time relative to a reference point.",
            "Rest and motion are relative terms; no absolute frame of rest exists in the universe.",
            "Rectilinear motion is one-dimensional motion along a straight line.",
            "A chosen reference point is known as the origin."
        ],
        "checkpoints": [
            {
                "num": 1,
                "q": "A person sitting inside a moving metro train is:",
                "options": [
                    "In motion relative to a fellow seated passenger",
                    "At rest relative to a fellow seated passenger, but in motion relative to a person standing on the platform",
                    "At absolute rest in the universe",
                    "In motion relative to their own seat"
                ],
                "ans": 1,
                "exp": "Motion is relative. The distance between two seated passengers does not change over time (at rest relative to each other), but their positions change continuously relative to an observer on the platform."
            },
            {
                "num": 2,
                "q": "What is the physical reference point called from which the position of an object is measured?",
                "options": ["Coordinate limit", "Origin (Reference Point)", "Terminal node", "Absolute zero"],
                "ans": 1,
                "exp": "To locate the position of an object unambiguously, a reference point called the origin is chosen, from which distances and directions are measured."
            }
        ]
    },
    {
        "id": 2,
        "badge": "Slide 02 • Competency C-2.1",
        "title": "Distance vs Displacement: Scalar Path vs Vector Shortcut",
        "subtitle": "Why total distance is never negative, but displacement can be zero or negative",
        "teacher": "Distance and displacement sound similar in everyday talk, but in physics they are fundamentally different! Distance is the total length of the actual path an object travels—it is a scalar quantity with only magnitude. Displacement is the shortest straight-line vector connecting the initial position directly to the final position. If you run one complete lap around a 400-metre circular track, your distance is 400 metres, but your displacement is zero!",
        "theory": [
            "<strong>Distance (Scalar Quantity):</strong>",
            "• The <strong>actual length of the path</strong> traversed by a moving body irrespective of its direction of motion.",
            "• Distance depends on the path taken, possesses only magnitude (scalar), is always positive or zero, and never decreases over time for a moving object.",
            "• SI unit: <strong>metre (m)</strong>.",
            "<strong>Displacement (Vector Quantity):</strong>",
            "• The <strong>shortest straight-line distance</strong> measured from the initial position to the final position of an object, along with the direction.",
            "• Displacement possesses both <strong>magnitude and direction</strong> (vector). It can be positive, negative, or zero.",
            "• SI unit: <strong>metre (m)</strong>.",
            "<strong>Crucial Comparative Relationships:</strong>",
            "1. $$\\text{Magnitude of Displacement} \\le \\text{Distance Travelled}$$ Equality holds strictly when an object moves continuously along a straight line in one unchanging direction.",
            "2. <strong>Zero Displacement with Non-Zero Distance:</strong>",
            "• When an object returns to its initial starting point (round trip), final position = initial position, so \\(\\text{Displacement} = 0\\), while \\(\\text{Distance} > 0\\).",
            "• <em>Example:</em> An athlete runs around a circular track of radius \\(r\\). After one complete revolution:",
            "$$\\text{Distance} = 2\\pi r \\quad \\text{and} \\quad \\text{Displacement} = 0$$",
            "After half a revolution:",
            "$$\\text{Distance} = \\pi r \\quad \\text{and} \\quad \\text{Displacement} = 2r\\text{ (the diameter)}$$"
        ],
        "key_points": [
            "Distance is total actual path length (scalar); displacement is the shortest direct straight-line vector.",
            "Magnitude of displacement is always less than or equal to distance (Displacement ≤ Distance).",
            "Displacement equals zero whenever an object returns to its starting point.",
            "Both distance and displacement share the SI unit metre (m)."
        ],
        "checkpoints": [
            {
                "num": 3,
                "q": "An athlete completes one round of a circular track of diameter 200 m in 40 seconds. What will be the distance covered and the magnitude of displacement after 2 minutes and 20 seconds (140 s)?",
                "options": [
                    "Distance = 2200 m, Displacement = 200 m",
                    "Distance = 1400 m, Displacement = 0 m",
                    "Distance = 2200 m, Displacement = 0 m",
                    "Distance = 440 m, Displacement = 100 m"
                ],
                "ans": 0,
                "exp": "Total time = 140 s. Number of rounds = 140 / 40 = 3.5 rounds. Distance = 3.5 × (2πr) = 3.5 × (π × 200) = 3.5 × 628.3 = 2200 m. After 3.5 rounds, the athlete is diametrically opposite to the start, so Displacement = Diameter = 200 m."
            },
            {
                "num": 4,
                "q": "Can the magnitude of displacement ever be greater than the distance travelled by an object?",
                "options": [
                    "Yes, when the body travels in a circular path",
                    "Yes, when the body is decelerating",
                    "No, because the shortest distance between two points is a straight line, so Displacement ≤ Distance always",
                    "Yes, in three-dimensional motion"
                ],
                "ans": 2,
                "exp": "Because a straight line is geometrically the shortest possible path connecting any two points in space, the straight-line displacement can never exceed the total path distance travelled."
            }
        ]
    },
    {
        "id": 3,
        "badge": "Slide 03 • Competency C-2.1",
        "title": "Speed, Velocity & Average Velocity",
        "subtitle": "Distinguishing the rate of distance from directed displacement rates",
        "teacher": "Speed tells you how fast an object moves, while velocity tells you how fast AND in what direction! If a car travels at 60 km/h, that is its speed. If it travels at 60 km/h due North, that is its velocity. Because velocity is a vector, a car moving at a constant speed of 40 km/h around a roundabout has a constantly changing velocity. Let's master the formulas for speed, velocity, and average velocity.",
        "theory": [
            "<strong>Speed (Scalar):</strong>",
            "• The rate at which an object covers distance: $$\\text{Speed } (v) = \\frac{\\text{Distance } (s)}{\\text{Time } (t)}$$",
            "• Scalar quantity (magnitude only, always positive). SI unit: <strong>metre per second (m/s or m·s⁻¹)</strong>.",
            "• <strong>Average Speed:</strong> $$\\text{Average Speed} = \\frac{\\text{Total Distance Travelled}}{\\text{Total Time Taken}}$$",
            "<strong>Velocity (Vector):</strong>",
            "• The rate of change of displacement of an object with time, or speed in a specified direction:",
            "$$\\vec{v} = \\frac{\\text{Displacement } (\\Delta \\vec{x})}{\\text{Time taken } (\\Delta t)}$$",
            "• Vector quantity (magnitude + direction). Can be positive, negative, or zero. SI unit: <strong>m/s</strong>.",
            "• <strong>How Velocity Can Change:</strong> Velocity changes if:",
            "  1. Speed changes,",
            "  2. Direction of motion changes, OR",
            "  3. Both speed and direction change simultaneously.",
            "<strong>Average Velocity (\\(v_{\\text{avg}}\\)):</strong>",
            "• General definition: $$v_{\\text{avg}} = \\frac{\\text{Total Net Displacement}}{\\text{Total Time Taken}}$$",
            "• For motion in a straight line with <em>uniform acceleration</em>, average velocity is the arithmetic mean of initial velocity (\\(u\\)) and final velocity (\\(v\\)):",
            "$$v_{\\text{avg}} = \\frac{u + v}{2}$$",
            "<strong>Unit Conversion Shortcut:</strong> To convert from \\(\\text{km/h}\\) to \\(\\text{m/s}\\), multiply by \\(\\frac{5}{18}\\):",
            "$$72\\text{ km/h} = 72 \\times \\frac{5}{18} = 20\\text{ m/s}$$"
        ],
        "key_points": [
            "Speed = Distance / Time (scalar); Velocity = Displacement / Time (vector).",
            "Velocity changes when speed changes, direction changes, or both change.",
            "Average speed = Total distance / Total time; Average velocity = Net displacement / Total time.",
            "For uniformly accelerated motion: v_avg = (u + v) / 2."
        ],
        "checkpoints": [
            {
                "num": 5,
                "q": "A car travels 30 km at a uniform speed of 60 km/h and the next 30 km at a uniform speed of 30 km/h. What is the average speed of the car for the entire 60 km journey?",
                "options": ["45 km/h", "40 km/h", "50 km/h", "35 km/h"],
                "ans": 1,
                "exp": "Time t₁ = 30 / 60 = 0.5 h. Time t₂ = 30 / 30 = 1.0 h. Total time = 0.5 + 1.0 = 1.5 h. Total distance = 60 km. Average speed = Total distance / Total time = 60 / 1.5 = 40 km/h (Note: not the simple average 45!)."
            },
            {
                "num": 6,
                "q": "Usha swims in a 90 m long pool. She covers 180 m in one minute by swimming from one end to the other and back along the same straight path. Find her average speed and average velocity.",
                "options": [
                    "Average speed = 3 m/s, Average velocity = 0 m/s",
                    "Average speed = 3 m/s, Average velocity = 3 m/s",
                    "Average speed = 1.5 m/s, Average velocity = 0 m/s",
                    "Average speed = 180 m/s, Average velocity = 90 m/s"
                ],
                "ans": 0,
                "exp": "Total distance = 180 m, time = 60 s. Average speed = 180 / 60 = 3 m/s. Because she returns to the starting point, net displacement = 0. Average velocity = 0 / 60 = 0 m/s."
            }
        ]
    },
    {
        "id": 4,
        "badge": "Slide 04 • Competency C-2.1",
        "title": "Acceleration & Retardation: Rate of Velocity Change",
        "subtitle": "Speeding up, slowing down, and motion under uniform acceleration",
        "teacher": "When you step on the accelerator pedal of a car, your velocity increases. When you slam on the brakes, your velocity decreases. In physics, acceleration is the rate of change of velocity with time. If velocity increases, acceleration is positive. If velocity decreases, acceleration is negative—often called retardation or deceleration. Let's master the mathematical formula and units of acceleration.",
        "theory": [
            "<strong>Definition of Acceleration:</strong> <strong>Acceleration</strong> is defined as the rate of change of velocity of an object with time:",
            "$$\\text{Acceleration } (a) = \\frac{\\text{Change in Velocity}}{\\text{Time taken}} = \\frac{\\text{Final Velocity } (v) - \\text{Initial Velocity } (u)}{\\text{Time } (t)}$$",
            "$$\\mathbf{a = \\frac{v - u}{t}}$$",
            "• Acceleration is a <strong>vector quantity</strong>.",
            "• SI unit: <strong>metre per second squared (m/s² or m·s⁻²)</strong>.",
            "<strong>Types of Acceleration:</strong>",
            "1. <strong>Positive Acceleration:</strong> When the velocity of an object increases with time (\\(v > u\\)). Direction of acceleration is in the direction of motion.",
            "2. <strong>Negative Acceleration (Retardation / Deceleration):</strong> When the velocity decreases with time (\\(v < u\\)). Acceleration acts opposite to the direction of motion. (e.g. brakes applied to a vehicle).",
            "3. <strong>Zero Acceleration:</strong> When an object moves with <strong>constant/uniform velocity</strong> (\\(v = u \\implies a = 0\\)).",
            "4. <strong>Uniform Acceleration:</strong> If an object travels in a straight line and its velocity increases or decreases by <strong>equal amounts in equal intervals of time</strong>. (e.g. A ball falling freely under gravity where \\(a = g \\approx 9.8\\text{ m/s}^2\\)).",
            "5. <strong>Non-Uniform Acceleration:</strong> If velocity changes at an irregular, unequal rate over time (e.g. driving in congested city traffic)."
        ],
        "key_points": [
            "Acceleration a = (v - u) / t. SI unit: m/s².",
            "Positive acceleration means velocity is increasing; negative acceleration (retardation) means slowing down.",
            "Uniform velocity implies zero acceleration (a = 0).",
            "Freely falling bodies under gravity experience uniform acceleration (g ≈ 9.8 m/s²)."
        ],
        "checkpoints": [
            {
                "num": 7,
                "q": "Starting from a stationary position, Rahul paddles his bicycle to attain a velocity of 6 m/s in 30 seconds. What is the acceleration of the bicycle?",
                "options": ["0.1 m/s²", "0.2 m/s²", "0.5 m/s²", "2.0 m/s²"],
                "ans": 1,
                "exp": "Initial velocity u = 0, final velocity v = 6 m/s, time t = 30 s. a = (v - u) / t = (6 - 0) / 30 = 0.2 m/s²."
            },
            {
                "num": 8,
                "q": "A bus travelling at 20 m/s applies brakes and is brought to rest in 5 seconds. What is the acceleration (retardation) of the bus?",
                "options": ["+4 m/s²", "-4 m/s² (Retardation of 4 m/s²)", "-2 m/s²", "+10 m/s²"],
                "ans": 1,
                "exp": "Initial velocity u = 20 m/s, final velocity v = 0 (rest), time t = 5 s. a = (v - u) / t = (0 - 20) / 5 = -4 m/s². The negative sign indicates retardation (deceleration)."
            }
        ]
    },
    {
        "id": 5,
        "badge": "Slide 05 • Competency C-2.1",
        "title": "Distance-Time (s-t) Graphs: Slope Equals Speed",
        "subtitle": "Visualizing rest, uniform velocity, and acceleration on coordinate axes",
        "teacher": "Graphs give us an intuitive visual summary of motion! On a distance-time (s-t) graph, time is plotted on the horizontal x-axis and distance on the vertical y-axis. For an object at rest, the graph is a flat horizontal line. For uniform speed, it is a straight line sloping upwards. Most importantly, the slope of a distance-time graph directly equals the speed of the object! Let's see how slope tells us who is moving faster.",
        "theory": [
            "<strong>Structure of a Distance-Time Graph:</strong>",
            "• Horizontal axis (\\(x\\)-axis) = Time (\\(t\\)).",
            "• Vertical axis (\\(y\\)-axis) = Distance (\\(s\\)).",
            "<strong>Interpreting Three Fundamental Cases:</strong>",
            "1. <strong>Object at Rest (Stationary):</strong>",
            "• Position does not change as time advances.",
            "• Graph is a <strong>horizontal straight line parallel to the time axis</strong>.",
            "• \\(\\text{Slope} = 0 \\implies \\text{Speed} = 0\\).",
            "2. <strong>Uniform Motion (Constant Speed):</strong>",
            "• The object covers equal distances in equal intervals of time.",
            "• Graph is a <strong>straight line inclined to the time axis</strong> passing through the origin.",
            "• <strong>Slope Calculation:</strong> Select two points \\(A(t_1, s_1)\\) and \\(B(t_2, s_2)\\) on the line:",
            "$$\\text{Slope} = \\frac{\\Delta s}{\\Delta t} = \\frac{s_2 - s_1}{t_2 - t_1} = \\mathbf{v\\text{ (Speed)}}$$",
            "• <em>The steeper the slope, the greater the speed of the object!</em>",
            "3. <strong>Non-Uniform Motion (Accelerating/Decelerating):</strong>",
            "• Covers unequal distances in equal time intervals.",
            "• Graph is a <strong>curved line</strong>. An upward-bending curve (concave up) represents acceleration; a curve flattening out represents deceleration."
        ],
        "key_points": [
            "Distance-time graph: Slope = Speed = Δs / Δt.",
            "Horizontal line parallel to time axis represents an object at rest (speed = 0).",
            "Straight inclined line represents uniform speed.",
            "Steeper slope indicates higher speed; curved line indicates accelerated motion."
        ],
        "checkpoints": [
            {
                "num": 9,
                "q": "What physical quantity does the slope of a distance-time graph represent?",
                "options": ["Acceleration", "Speed (or Velocity)", "Total distance", "Force"],
                "ans": 1,
                "exp": "The slope of a distance-time graph is the ratio of vertical change (distance Δs) to horizontal change (time Δt): Δs / Δt = Speed."
            },
            {
                "num": 10,
                "q": "On a distance-time graph, line A has a slope of 30° while line B has a slope of 60° relative to the time axis. Which object is moving faster?",
                "options": [
                    "Object A moves faster",
                    "Object B moves faster because its steeper slope indicates higher speed",
                    "Both move at identical speeds",
                    "Neither is moving"
                ],
                "ans": 1,
                "exp": "Speed is directly proportional to the slope (tan θ). Since tan(60°) = √3 ≈ 1.732 is greater than tan(30°) = 1/√3 ≈ 0.577, Object B is moving significantly faster than Object A."
            }
        ]
    },
    {
        "id": 6,
        "badge": "Slide 06 • Competency C-2.1",
        "title": "Velocity-Time (v-t) Graphs: Slope Equals Acceleration",
        "subtitle": "Analyzing uniform velocity, uniform acceleration, and retardation",
        "teacher": "A velocity-time (v-t) graph is a physics powerhouse! When we plot velocity on the vertical axis and time on the horizontal axis, the slope of the line gives us acceleration. A flat line means zero acceleration (constant speed). A straight line sloping upward means uniform acceleration. A line sloping downward means uniform retardation. Let's see how slope translates into acceleration.",
        "theory": [
            "<strong>Structure of a Velocity-Time Graph:</strong>",
            "• Horizontal axis = Time (\\(t\\)).",
            "• Vertical axis = Velocity (\\(v\\)).",
            "<strong>Key Graphical Profiles:</strong>",
            "1. <strong>Uniform Velocity (Zero Acceleration):</strong>",
            "• Velocity remains constant at all times (\\(v = u\\)).",
            "• Graph is a <strong>horizontal straight line parallel to the time axis</strong>.",
            "• \\(\\text{Slope} = \\frac{\\Delta v}{\\Delta t} = 0 \\implies a = 0\\).",
            "2. <strong>Uniform Acceleration (Speeding Up):</strong>",
            "• Velocity increases by equal amounts in equal time intervals.",
            "• Graph is a <strong>straight line sloping upwards</strong>.",
            "• <strong>Slope Calculation:</strong> Select two points \\(A(t_1, v_1)\\) and \\(B(t_2, v_2)\\):",
            "$$\\text{Slope} = \\frac{\\Delta v}{\\Delta t} = \\frac{v_2 - v_1}{t_2 - t_1} = \\mathbf{a\\text{ (Acceleration)}}$$",
            "3. <strong>Uniform Retardation (Slowing Down):</strong>",
            "• Velocity decreases linearly to zero.",
            "• Graph is a <strong>straight line sloping downwards</strong> with negative slope (\\(a < 0\\)).",
            "4. <strong>Non-Uniform Acceleration:</strong>",
            "• Graph is a non-linear curve indicating changing rates of acceleration."
        ],
        "key_points": [
            "Velocity-time graph: Slope = Acceleration = Δv / Δt.",
            "Horizontal line represents uniform velocity (zero acceleration).",
            "Upward sloping line represents uniform positive acceleration.",
            "Downward sloping line represents uniform retardation (deceleration)."
        ],
        "checkpoints": [
            {
                "num": 11,
                "q": "What physical quantity is determined from the slope of a velocity-time graph?",
                "options": ["Distance", "Acceleration", "Speed", "Force"],
                "ans": 1,
                "exp": "Slope = Change in velocity / Change in time = Δv / Δt = Acceleration."
            },
            {
                "num": 12,
                "q": "If the velocity-time graph of an object is a horizontal line parallel to the time axis at v = 15 m/s, what is its acceleration?",
                "options": ["15 m/s²", "9.8 m/s²", "0 m/s²", "1.5 m/s²"],
                "ans": 2,
                "exp": "A horizontal line has zero slope, meaning the velocity is constant over time (no change in velocity, Δv = 0). Therefore, acceleration a = 0 m/s²."
            }
        ]
    },
    {
        "id": 7,
        "badge": "Slide 07 • Competency C-2.1",
        "title": "Area Under Velocity-Time Graph Represents Displacement",
        "subtitle": "The powerful geometric integration principle of kinematics",
        "teacher": "Here is one of the most elegant discoveries in mechanics: the area enclosed under a velocity-time graph represents the total displacement travelled by the object! Why? Because velocity is metres divided by seconds, and time is seconds. Multiplying height (velocity) by width (time) cancels the seconds, leaving metres! Let's see how calculating areas of rectangles and triangles gives exact distances.",
        "theory": [
            "<strong>Dimensional Proof:</strong>",
            "$$\\text{Area} = \\text{Height } (v) \\times \\text{Base } (t) = \\left(\\frac{\\text{metres}}{\\text{second}}\\right) \\times \\text{seconds} = \\mathbf{\\text{metres (Displacement } s)}$$",
            "<strong>Two Geometric Scenarios:</strong>",
            "1. <strong>Uniform Velocity (Rectangular Area):</strong>",
            "For an object moving at constant velocity \\(v\\) from time \\(t_1\\) to \\(t_2\\):",
            "$$\\text{Displacement } s = \\text{Area of rectangle } ABCD = AB \\times AD = v \\times (t_2 - t_1)$$",
            "2. <strong>Uniformly Accelerated Motion (Trapezium Area):</strong>",
            "For an object with initial velocity \\(u\\) accelerating uniformly to final velocity \\(v\\) in time \\(t\\):",
            "The total area enclosed under line \\(AB\\) is a <strong>trapezium</strong> \\(OABC\\), which splits cleanly into:",
            "$$\\text{Total Area} = \\text{Area of Rectangle } OADC + \\text{Area of Triangle } ABD$$",
            "$$\\text{Area of Rectangle } OADC = OA \\times OC = u \\times t$$",
            "$$\\text{Area of Triangle } ABD = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times AD \\times BD = \\frac{1}{2} \\times t \\times (v - u)$$",
            "$$\\mathbf{s = ut + \\frac{1}{2}(v - u)t}$$",
            "This geometric area will serve as the exact foundation to derive the kinematic equations!"
        ],
        "key_points": [
            "The area under a velocity-time graph equals the displacement (or distance) travelled.",
            "Rectangle area = u × t represents displacement due to initial velocity.",
            "Triangle area = 1/2 × (v - u) × t represents additional displacement due to acceleration.",
            "Total displacement = Area of trapezium = Sum of rectangle and triangle areas."
        ],
        "checkpoints": [
            {
                "num": 13,
                "q": "A car moves at a constant velocity of 25 m/s for 12 seconds. What is the area under its velocity-time graph and the displacement?",
                "options": ["150 m", "300 m", "25 m", "12 m"],
                "ans": 1,
                "exp": "For constant velocity, the area is a rectangle: Area = height × base = 25 m/s × 12 s = 300 m. Thus, displacement = 300 m."
            },
            {
                "num": 14,
                "q": "The velocity-time graph of an object is a triangle with base 8 s and peak height 20 m/s starting from rest (u = 0). What is the total distance covered?",
                "options": ["160 m", "80 m", "40 m", "20 m"],
                "ans": 1,
                "exp": "Distance = Area of triangle = 1/2 × base × height = 1/2 × 8 s × 20 m/s = 80 m."
            }
        ]
    },
    {
        "id": 8,
        "badge": "Slide 08 • Competency C-2.1",
        "title": "Graphical Derivation: 1st Kinematic Equation (v = u + at)",
        "subtitle": "Deriving the velocity-time relation using the slope of the v-t graph",
        "teacher": "Now, let us derive the famous three equations of motion by the graphical method as required by the NCERT curriculum. First is the velocity-time relation: v = u + at. Consider a body moving with initial velocity u at time t = 0 that undergoes uniform acceleration a for time t, reaching final velocity v. By calculating the slope of the velocity-time line, the equation emerges effortlessly. Let's trace every step.",
        "theory": [
            "<strong>The Physical Setup:</strong>",
            "• An object moves with initial velocity \\(u\\) at time \\(t = 0\\) (represented by point \\(A\\) on the \\(y\\)-axis, where \\(OA = u\\)).",
            "• It accelerates uniformly at rate \\(a\\) for time \\(t\\) (represented by \\(OC = t\\)), reaching final velocity \\(v\\) at point \\(B\\) (where \\(BC = v\\)).",
            "<strong>Geometric Construction:</strong>",
            "• Draw perpendicular \\(BC\\) from point \\(B\\) down to the time axis.",
            "• Draw horizontal line \\(AD\\) parallel to \\(OC\\) intersecting \\(BC\\) at \\(D\\).",
            "From the graph:",
            "$$OA = CD = u, \\quad BC = v, \\quad OC = AD = t$$",
            "$$BD = BC - CD = v - u$$",
            "<strong>Derivation Step-by-Step:</strong>",
            "1. By definition, <strong>acceleration is the slope</strong> of the velocity-time graph line \\(AB\\):",
            "$$a = \\text{Slope of } AB = \\frac{\\text{Change in Velocity}}{\\text{Time}} = \\frac{BD}{AD}$$",
            "2. Substitute \\(BD = v - u\\) and \\(AD = t\\):",
            "$$a = \\frac{v - u}{t}$$",
            "3. Multiply both sides by \\(t\\):",
            "$$at = v - u$$",
            "4. Rearrange to isolate final velocity \\(v\\):",
            "$$\\mathbf{v = u + at}$$",
            "This is the <strong>First Equation of Motion</strong>, connecting initial velocity, final velocity, acceleration, and time."
        ],
        "key_points": [
            "1st equation: v = u + at represents the velocity-time relation.",
            "Derived directly from the slope of the v-t graph: a = BD / AD = (v - u) / t.",
            "u = initial velocity, v = final velocity, a = uniform acceleration, t = time.",
            "Applies strictly to motion in a straight line with constant acceleration."
        ],
        "checkpoints": [
            {
                "num": 15,
                "q": "In the graphical derivation of v = u + at from a velocity-time graph, what geometric segment represents the change in velocity (v - u)?",
                "options": ["Segment OA", "Segment OC", "Segment BD (where BD = BC - CD)", "Segment AD"],
                "ans": 2,
                "exp": "BC represents final velocity v and CD represents initial velocity u. Therefore, the vertical segment BD = BC - CD = v - u represents the change in velocity."
            },
            {
                "num": 16,
                "q": "A car accelerates uniformly from 10 m/s to 25 m/s in 5 seconds. Using the 1st equation of motion, what is its acceleration?",
                "options": ["2 m/s²", "3 m/s²", "5 m/s²", "15 m/s²"],
                "ans": 1,
                "exp": "v = u + at ➔ 25 = 10 + a(5) ➔ 5a = 15 ➔ a = 3 m/s²."
            }
        ]
    },
    {
        "id": 9,
        "badge": "Slide 09 • Competency C-2.1",
        "title": "Graphical Derivation: 2nd Kinematic Equation (s = ut + ½at²)",
        "subtitle": "Deriving the position-time relation by summing rectangular and triangular areas",
        "teacher": "Next, let us derive the second equation of motion: s = ut + 1/2 at², which relates distance to time. As established earlier, the distance travelled is the total area enclosed under the velocity-time graph. By splitting the trapezium under line AB into a rectangle (representing initial velocity) and a triangle (representing acceleration), the formula unfolds with complete mathematical clarity.",
        "theory": [
            "<strong>The Geometric Setup:</strong>",
            "Consider the same \\(v-t\\) graph where the body travels distance \\(s\\) in time \\(t\\) under uniform acceleration \\(a\\).",
            "The distance \\(s\\) travelled is equal to the <strong>area of trapezium \\(OABC\\)</strong> enclosed under the line \\(AB\\):",
            "$$s = \\text{Area of trapezium } OABC$$",
            "Split the trapezium into two distinct geometric figures:",
            "$$s = \\text{Area of rectangle } OADC + \\text{Area of triangle } ABD$$",
            "<strong>Step-by-Step Area Evaluation:</strong>",
            "1. <strong>Area of Rectangle \\(OADC\\):</strong>",
            "$$\\text{Area}(OADC) = \\text{Length} \\times \\text{Breadth} = OA \\times OC = u \\times t = \\mathbf{ut}$$",
            "2. <strong>Area of Triangle \\(ABD\\):</strong>",
            "$$\\text{Area}(ABD) = \\frac{1}{2} \\times \\text{Base} \\times \\text{Height} = \\frac{1}{2} \\times AD \\times BD$$",
            "Since \\(AD = t\\) and \\(BD = v - u\\):",
            "$$\\text{Area}(ABD) = \\frac{1}{2} \\times t \\times (v - u)$$",
            "3. From the 1st equation of motion, \\(v - u = at\\). Substituting this for \\(BD\\):",
            "$$\\text{Area}(ABD) = \\frac{1}{2} \\times t \\times (at) = \\mathbf{\\frac{1}{2}at^2}$$",
            "4. Summing the two areas:",
            "$$\\mathbf{s = ut + \\frac{1}{2}at^2}$$",
            "This is the <strong>Second Equation of Motion</strong> (the position-time relation)."
        ],
        "key_points": [
            "2nd equation: s = ut + 1/2 at² represents the position-time relation.",
            "Distance s equals the total area under the v-t graph.",
            "Area splits into: Rectangle OADC (ut) + Triangle ABD (1/2 at²).",
            "If an object starts from rest (u = 0), distance simplifies to s = 1/2 at²."
        ],
        "checkpoints": [
            {
                "num": 17,
                "q": "In the derivation of s = ut + 1/2 at², what does the term 'ut' physically represent?",
                "options": [
                    "The distance the object would cover if it continued moving at constant initial speed u without accelerating",
                    "The acceleration after time t",
                    "The final kinetic energy",
                    "The time taken to come to rest"
                ],
                "ans": 0,
                "exp": "The term 'ut' is the area of the rectangle, representing the displacement covered purely due to the initial velocity u. The term '1/2 at²' represents the additional displacement gained due to acceleration."
            },
            {
                "num": 18,
                "q": "A racing car starts from rest (u = 0) and accelerates uniformly at 4 m/s² for 8 seconds. What distance does it cover?",
                "options": ["32 m", "64 m", "128 m", "256 m"],
                "ans": 2,
                "exp": "u = 0, a = 4 m/s², t = 8 s. s = ut + 1/2 at² = 0 + 1/2 × 4 × (8)² = 2 × 64 = 128 m."
            }
        ]
    },
    {
        "id": 10,
        "badge": "Slide 10 • Competency C-2.1",
        "title": "Graphical Derivation: 3rd Kinematic Equation (v² = u² + 2as)",
        "subtitle": "Deriving the position-velocity relation eliminating the time variable",
        "teacher": "Now let us derive the third equation of motion: v² = u² + 2as. Notice that this equation does NOT contain time (t)! It connects initial velocity, final velocity, acceleration, and distance. We derive it using the direct geometric formula for the area of a trapezium, and then eliminate time using the first equation of motion. Let's see how the algebra unfolds.",
        "theory": [
            "<strong>The Direct Trapezium Formula:</strong>",
            "From the velocity-time graph, the distance \\(s\\) travelled by the object in time \\(t\\) is the area of trapezium \\(OABC\\):",
            "$$\\text{Area of a Trapezium} = \\frac{\\text{Sum of parallel sides} \\times \\text{Perpendicular distance between them}}{2}$$",
            "Here, the parallel sides are \\(OA = u\\) and \\(BC = v\\), and the perpendicular distance is \\(OC = t\\):",
            "$$s = \\frac{(OA + BC) \\times OC}{2} = \\frac{(u + v) \\times t}{2}$$",
            "$$s = \\frac{(v + u) \\cdot t}{2} \\quad \\text{--- (Equation 1)}$$",
            "<strong>Eliminating Time (\\(t\\)):</strong>",
            "From the First Equation of Motion:",
            "$$v = u + at \\implies v - u = at \\implies \\mathbf{t = \\frac{v - u}{a}} \\quad \\text{--- (Equation 2)}$$",
            "<strong>Substituting Equation 2 into Equation 1:</strong>",
            "$$s = \\frac{(v + u)}{2} \\times \\left(\\frac{v - u}{a}\\right)$$",
            "Using the algebraic identity \\((v + u)(v - u) = v^2 - u^2\\):",
            "$$s = \\frac{v^2 - u^2}{2a}$$",
            "Multiplying both sides by \\(2a\\):",
            "$$2as = v^2 - u^2$$",
            "Rearranging gives:",
            "$$\\mathbf{v^2 = u^2 + 2as}$$",
            "This is the <strong>Third Equation of Motion</strong> (the position-velocity relation)."
        ],
        "key_points": [
            "3rd equation: v² = u² + 2as (or 2as = v² - u²) represents the position-velocity relation.",
            "It is completely independent of time t.",
            "Derived by calculating the area of trapezium OABC and substituting t = (v - u) / a.",
            "Indispensable when distance and velocities are known, but time duration is not given."
        ],
        "checkpoints": [
            {
                "num": 19,
                "q": "Which equation of motion would you select to calculate the stopping distance of a car if initial velocity, final velocity, and deceleration are known, but time is unknown?",
                "options": ["v = u + at", "s = ut + 1/2 at²", "v² = u² + 2as (3rd Equation)", "s = v / t"],
                "ans": 2,
                "exp": "Because the 3rd equation (v² = u² + 2as) connects u, v, a, and s without requiring time t, it is the ideal formula to determine stopping distance directly: s = (v² - u²) / (2a)."
            },
            {
                "num": 20,
                "q": "A bullet travelling at 100 m/s penetrates a wooden block and comes to rest (v = 0) after traversing 0.5 m. What is the retardation experienced by the bullet?",
                "options": ["-5,000 m/s²", "-10,000 m/s²", "-20,000 m/s²", "-1,000 m/s²"],
                "ans": 1,
                "exp": "u = 100 m/s, v = 0, s = 0.5 m. Using v² = u² + 2as: 0 = (100)² + 2a(0.5) ➔ 0 = 10000 + 1a ➔ a = -10,000 m/s² (retardation of 10,000 m/s²)."
            }
        ]
    },
    {
        "id": 11,
        "badge": "Slide 11 • Competency C-2.1",
        "title": "Kinematic Problem Solving: Horizontal Motion Masterclass",
        "subtitle": "Step-by-step 4-step protocol for solving rectilinear kinematics problems",
        "teacher": "Solving physics word problems becomes effortless when you follow a structured method! Step 1: List the given known variables with proper SI units. Step 2: Identify the target unknown. Step 3: Pick the matching kinematic equation containing those exact variables. Step 4: Substitute and compute. Let's solve standard NCERT textbook problems together.",
        "theory": [
            "<strong>The Universal 4-Step Kinematics Protocol:</strong>",
            "1. <strong>Extract Variables:</strong> Read carefully and list knowns: \\(u, v, a, s, t\\).",
            "   • 'Starts from rest' \\(\\implies u = 0\\).",
            "   • 'Comes to a stop / brakes applied' \\(\\implies v = 0\\).",
            "   • 'Uniform speed / constant velocity' \\(\\implies a = 0\\).",
            "2. <strong>Unit Check:</strong> Convert all speeds from \\(\\text{km/h}\\) to \\(\\text{m/s}\\) (\\(\\times \\frac{5}{18}\\)).",
            "3. <strong>Equation Matching:</strong>",
            "   • If no \\(s\\): use \\(v = u + at\\)",
            "   • If no \\(v\\): use \\(s = ut + \\frac{1}{2}at^2\\)",
            "   • If no \\(t\\): use \\(v^2 = u^2 + 2as\\)",
            "<strong>Worked Problem: The Train Acceleration Problem:</strong>",
            "<em>A train starting from a railway station and moving with uniform acceleration attains a speed of 40 km/h in 10 minutes. Find its acceleration.</em>",
            "• \\(u = 0\\) (starts from rest).",
            "• \\(v = 40\\text{ km/h} = 40 \\times \\frac{5}{18} = \\frac{100}{9}\\text{ m/s} \\approx 11.11\\text{ m/s}\\).",
            "• \\(t = 10\\text{ min} = 10 \\times 60\\text{ s} = 600\\text{ s}\\).",
            "• Target: \\(a\\). Equation: \\(v = u + at\\):",
            "$$a = \\frac{v - u}{t} = \\frac{11.11 - 0}{600} \\approx \\mathbf{0.0185\\text{ m/s}^2}$$"
        ],
        "key_points": [
            "Always convert km/h to m/s by multiplying by 5/18 before computing.",
            "'From rest' means u = 0; 'brakes applied to a stop' means v = 0.",
            "Select equation based on the missing variable: no s (eq 1), no v (eq 2), no t (eq 3).",
            "Always state final answers with correct SI units."
        ],
        "checkpoints": [
            {
                "num": 21,
                "q": "A bus starting from rest moves with a uniform acceleration of 0.1 m/s² for 2 minutes. Find (a) the speed acquired, and (b) the distance travelled.",
                "options": [
                    "Speed = 12 m/s, Distance = 720 m",
                    "Speed = 24 m/s, Distance = 1440 m",
                    "Speed = 12 m/s, Distance = 360 m",
                    "Speed = 6 m/s, Distance = 720 m"
                ],
                "ans": 0,
                "exp": "u = 0, a = 0.1 m/s², t = 2 min = 120 s. (a) v = u + at = 0 + (0.1)(120) = 12 m/s. (b) s = ut + 1/2 at² = 0 + 1/2 (0.1)(120)² = 0.05 × 14400 = 720 m."
            },
            {
                "num": 22,
                "q": "A train is travelling at a speed of 90 km/h. Brakes are applied so as to produce a uniform acceleration of -0.5 m/s². How far will the train go before it is brought to rest?",
                "options": ["225 m", "450 m", "625 m", "900 m"],
                "ans": 2,
                "exp": "u = 90 km/h = 90 × (5/18) = 25 m/s. v = 0 (rest), a = -0.5 m/s². Using v² = u² + 2as: 0 = (25)² + 2(-0.5)s ➔ 0 = 625 - s ➔ s = 625 m."
            }
        ]
    },
    {
        "id": 12,
        "badge": "Slide 12 • Competency C-2.1",
        "title": "Vertical Motion & Free Fall Under Gravity",
        "subtitle": "Kinematics in Earth's gravitational field with a = ±g",
        "teacher": "What happens when an object drops freely from a tower or is thrown straight up into the sky? It moves under the influence of Earth's gravity alone! In vacuum (ignoring air resistance), all objects accelerate downward at the exact same rate: g ≈ 9.8 m/s². When an object falls downward, acceleration is positive (+g); when thrown upward, gravity slows it down, so acceleration is negative (-g). Let's master vertical kinematics.",
        "theory": [
            "<strong>Free Fall Fundamentals:</strong>",
            "• An object falling toward Earth under the pull of gravity alone, with air resistance neglected, is said to be in <strong>free fall</strong>.",
            "• <strong>Acceleration Due to Gravity (\\(g\\)):</strong>",
            "Near Earth's surface: $$g \\approx 9.8\\text{ m/s}^2 \\quad (\\text{often approximated as } 10\\text{ m/s}^2)$$",
            "• In free fall, acceleration is independent of the mass of the object! Galileo proved that a heavy cannonball and a light ball hit the ground simultaneously from the Leaning Tower of Pisa.",
            "<strong>Sign Conventions for Vertical Motion:</strong>",
            "1. <strong>Case A: Dropped Freely Downward (Falling Body):</strong>",
            "• Initial velocity \\(u = 0\\), acceleration \\(a = +g\\), displacement \\(s = +h\\).",
            "$$v = gt, \\quad h = \\frac{1}{2}gt^2, \\quad v^2 = 2gh$$",
            "2. <strong>Case B: Thrown Vertically Upward:</strong>",
            "• Initial velocity \\(u > 0\\), acceleration \\(a = -g\\).",
            "• At the maximum height (highest point), the instantaneous final velocity is zero: \\(\\mathbf{v = 0}\\).",
            "• Time to reach highest point: $$t_{\\text{ascent}} = \\frac{u}{g}$$",
            "• Maximum height attained: $$h_{\\text{max}} = \\frac{u^2}{2g}$$",
            "• Total time of flight (up and down): $$T = 2 \\times t_{\\text{ascent}} = \\frac{2u}{g}$$"
        ],
        "key_points": [
            "Free fall acceleration: g ≈ 9.8 m/s² directed downward toward Earth's center.",
            "For upward throws: a = -g; at maximum peak height, instantaneous velocity v = 0.",
            "Maximum height h_max = u² / 2g; Time of ascent = u / g.",
            "Time of ascent equals time of descent (symmetric trajectory in vacuum)."
        ],
        "checkpoints": [
            {
                "num": 23,
                "q": "A stone is thrown vertically upward with an initial velocity of 19.6 m/s. Taking g = 9.8 m/s², what is the maximum height attained by the stone?",
                "options": ["9.8 m", "19.6 m", "39.2 m", "4.9 m"],
                "ans": 1,
                "exp": "At max height v = 0, a = -9.8 m/s². Using v² = u² + 2as: 0 = (19.6)² + 2(-9.8)h ➔ 0 = 384.16 - 19.6h ➔ h = 384.16 / 19.6 = 19.6 m."
            },
            {
                "num": 24,
                "q": "A ball dropped from the roof of a building takes 3 seconds to strike the ground. Taking g = 9.8 m/s², what is the height of the building?",
                "options": ["29.4 m", "44.1 m", "58.8 m", "88.2 m"],
                "ans": 1,
                "exp": "Dropped from rest: u = 0, t = 3 s, a = +9.8 m/s². h = ut + 1/2 gt² = 0 + 1/2 × 9.8 × (3)² = 4.9 × 9 = 44.1 m."
            }
        ]
    },
    {
        "id": 13,
        "badge": "Slide 13 • Competency C-2.1",
        "title": "Uniform Circular Motion (UCM) & Tangential Speed",
        "subtitle": "Constant speed with continuously changing direction: an accelerated motion",
        "teacher": "Can an object have constant speed but still be accelerating? Absolutely! When an athlete runs along a circular track at a steady 5 m/s, their speed is constant, but their direction of motion changes every single millisecond. Because velocity is a vector, this continuous directional change means velocity is continuously changing. Therefore, Uniform Circular Motion is an accelerated motion! Let's derive its speed formula.",
        "theory": [
            "<strong>Definition of Uniform Circular Motion (UCM):</strong>",
            "When an object moves in a circular path with a <strong>constant (uniform) speed</strong>, its motion is called <strong>Uniform Circular Motion</strong>.",
            "<strong>Why is UCM an Accelerated Motion?</strong>",
            "• Velocity is a vector with magnitude (speed) and direction.",
            "• In circular motion, although the magnitude of velocity (speed) remains constant, the <strong>direction of motion changes continuously at every point</strong> along the circle.",
            "• Since velocity changes with time, uniform circular motion is <strong>accelerated motion</strong>.",
            "<strong>Tangential Direction of Velocity:</strong>",
            "• At any instant, the velocity vector of the moving body points along the <strong>tangent to the circle</strong> at that position.",
            "• <em>The Whirling Stone Experiment:</em> Tie a stone to a thread and whirl it in a horizontal circle. If the thread suddenly snaps, the stone flies off in a straight line along the <strong>tangent</strong> to the circle at that instant!",
            "<strong>Derivation of Speed Formula for UCM:</strong>",
            "Let a body move along a circular path of radius \\(r\\) and take time \\(T\\) for one complete revolution.",
            "• Distance covered in 1 complete revolution = Circumference of the circle = \\(2\\pi r\\).",
            "• Time taken = Periodic time \\(T\\).",
            "$$\\mathbf{v = \\frac{2\\pi r}{T}}$$"
        ],
        "key_points": [
            "Uniform Circular Motion has constant speed but continuously changing velocity.",
            "UCM is an accelerated motion because direction of motion changes constantly.",
            "Instantaneous velocity is always directed along the tangent to the circle.",
            "Speed formula: v = (2πr) / T, where r is radius and T is time for one revolution."
        ],
        "checkpoints": [
            {
                "num": 25,
                "q": "Why is uniform circular motion classified as an accelerated motion even when speed is constant?",
                "options": [
                    "Because the radius of the circle expands continuously",
                    "Because the direction of the velocity vector changes continuously at every point along the path",
                    "Because air friction increases speed",
                    "Because gravity is zero in circles"
                ],
                "ans": 1,
                "exp": "Acceleration is defined as the rate of change of velocity. Even though speed (magnitude) is constant, the direction of motion changes at every point on the circle, making velocity non-constant and the motion accelerated."
            },
            {
                "num": 26,
                "q": "An artificial satellite orbits Earth in a circular orbit of radius 42,250 km. It takes 24 hours to complete one revolution. What is its orbital speed?",
                "options": ["1.54 km/s", "3.07 km/s", "6.14 km/s", "11.2 km/s"],
                "ans": 1,
                "exp": "Radius r = 42,250 km. Time T = 24 h = 24 × 3600 s = 86,400 s. Circumference = 2 × π × 42250 = 265,464.5 km. Speed v = 2πr / T = 265464.5 / 86400 ≈ 3.07 km/s."
            }
        ]
    },
    {
        "id": 14,
        "badge": "Slide 14 • Competency C-2.1, C-8.1",
        "title": "Centripetal Acceleration & Circular Motion Dynamics",
        "subtitle": "The inward pull that bends straight-line inertia into a circular orbit",
        "teacher": "According to Newton's First Law, every moving body naturally wants to travel in a straight line forever! To force an object into a curved circle, an inward radial force must continuously pull it toward the centre. This produces centripetal acceleration. Without this centripetal pull, the Moon would fly off into deep space, and cars would skid off sharp highway bends! Let's explore centripetal dynamics.",
        "theory": [
            "<strong>Centripetal Acceleration (\\(a_c\\)):</strong>",
            "• In uniform circular motion, the acceleration is directed radially <strong>inward toward the center of the circular path</strong>.",
            "• The word 'centripetal' originates from Latin, meaning <em>'center-seeking'</em>.",
            "• Magnitude of centripetal acceleration: $$\\mathbf{a_c = \\frac{v^2}{r} = \\omega^2 r}$$",
            "where \\(v\\) is linear speed, \\(r\\) is radius, and \\(\\omega = \\frac{2\\pi}{T}\\) is angular velocity.",
            "<strong>Sources of Centripetal Force in Real Life:</strong>",
            "1. <strong>Whirling Stone on a String:</strong> Tension in the string pulls the stone inward.",
            "2. <strong>Planets and Satellites:</strong> Earth's gravitational force pulls the Moon and satellites toward Earth's centre, maintaining stable orbits.",
            "3. <strong>Car on a Circular Curve:</strong> Lateral frictional force between the car's rubber tyres and the road surface provides the needed inward centripetal force. If the road is icy, friction drops, the required centripetal force is lost, and the car skids tangentially!",
            "4. <strong>Banking of Roads:</strong> Highway engineers tilt curved roads inward so the normal reaction force provides centripetal support without relying solely on tyre friction."
        ],
        "key_points": [
            "Centripetal acceleration a_c = v² / r is always directed toward the center of curvature.",
            "Gravity provides centripetal acceleration for orbiting satellites.",
            "Tyre-road friction provides centripetal force for turning cars.",
            "Snapping the centripetal connection causes the object to move tangentially in a straight line."
        ],
        "checkpoints": [
            {
                "num": 27,
                "q": "In which direction is centripetal acceleration oriented for an object in uniform circular motion?",
                "options": [
                    "Tangential to the circle in the direction of motion",
                    "Radially inward toward the centre of the circle",
                    "Radially outward away from the circle",
                    "Perpendicular to the plane of rotation"
                ],
                "ans": 1,
                "exp": "Centripetal acceleration is strictly 'center-seeking'—it points radially inward toward the center of the circular orbit at every point, perpendicular to the tangential velocity vector."
            },
            {
                "num": 28,
                "q": "What provides the necessary centripetal force to keep the Moon in its circular orbit around the Earth?",
                "options": [
                    "Atmospheric air pressure from Earth",
                    "Earth's gravitational force of attraction",
                    "Solar radiation wind pressure",
                    "The magnetic field of the Moon"
                ],
                "ans": 1,
                "exp": "Earth's gravitational attraction pulls the Moon radially inward toward Earth's center, continuously bending the Moon's velocity vector into a stable circular orbit."
            }
        ]
    },
    {
        "id": 15,
        "badge": "Slide 15 • Competency C-8.1, C-8.2",
        "title": "Road Safety Physics: Reaction Time & Braking Distance",
        "subtitle": "Applying kinematics to saving lives: why doubling speed quadruples braking distance",
        "teacher": "Physics is directly tied to life and death on the highway! When a driver spots an obstacle, the vehicle does not stop instantly. Total stopping distance consists of two distinct phases: thinking distance (during human reaction time) and braking distance (while the brakes decelerate the car). Because braking distance is proportional to velocity squared (v²), doubling your speed from 40 to 80 km/h doesn't double your braking distance—it quadruples it! Let's examine the kinematics.",
        "theory": [
            "<strong>Total Stopping Distance Architecture:</strong>",
            "$$\\mathbf{\\text{Total Stopping Distance} = \\text{Thinking Distance} + \\text{Braking Distance}}$$",
            "1. <strong>Thinking Distance (Reaction Phase):</strong>",
            "• The distance traversed while the driver detects a hazard, makes a decision, and moves their foot to press the brake pedal.",
            "• Average human reaction time: \\(t_r \\approx 0.7\\text{ s to } 1.0\\text{ s}\\) (longer if fatigued or distracted by mobile phones).",
            "$$\\text{Thinking Distance } (s_{\\text{think}}) = v \\times t_r$$ (Directly linear with velocity: \\(s_{\\text{think}} \\propto v\\)).",
            "2. <strong>Braking Distance (Deceleration Phase):</strong>",
            "• The distance traversed from the moment brakes are depressed until the car stops (\\(v = 0\\)) under maximum retardation \\(a\\).",
            "• From the 3rd equation of motion: \\(v^2 = u^2 - 2as_{\\text{brake}} \\implies 0 = u^2 - 2as_{\\text{brake}}\\):",
            "$$\\mathbf{s_{\\text{brake}} = \\frac{u^2}{2a}}$$",
            "• <strong>The Quadratic Velocity Trap (\\(s_{\\text{brake}} \\propto u^2\\)):</strong>",
            "  - At \\(40\\text{ km/h}\\): \\(s_{\\text{brake}} = 10\\text{ m}\\).",
            "  - At \\(80\\text{ km/h}\\) (double speed): \\(s_{\\text{brake}} = 2^2 \\times 10 = \\mathbf{40\\text{ m}}\\text{ (four times longer!)}\\).",
            "  - At \\(120\\text{ km/h}\\) (triple speed): \\(s_{\\text{brake}} = 3^2 \\times 10 = \\mathbf{90\\text{ m}}\\text{ (nine times longer!)}\\)."
        ],
        "key_points": [
            "Stopping Distance = Thinking Distance (v × t_r) + Braking Distance (u² / 2a).",
            "Thinking distance is proportional to velocity (linear); braking distance is proportional to velocity squared (quadratic).",
            "Doubling vehicle speed quadruples (4×) the physical braking distance.",
            "Distractions or alcohol lengthen reaction time, drastically extending stopping distance."
        ],
        "checkpoints": [
            {
                "num": 29,
                "q": "If a car's speed is doubled from 50 km/h to 100 km/h, by what factor does its physical braking distance increase under identical road conditions?",
                "options": ["2 times (doubles)", "4 times (quadruples)", "8 times", "Remains unchanged"],
                "ans": 1,
                "exp": "From the 3rd equation of motion, s_braking = u² / 2a. Because braking distance is proportional to the square of initial speed (s ∝ u²), doubling speed (2u) increases braking distance by 2² = 4 times."
            },
            {
                "num": 30,
                "q": "A driver with a reaction time of 0.8 seconds is cruising at 20 m/s (72 km/h). How far does the car travel during the driver's reaction time before the brakes are even touched?",
                "options": ["8 m", "16 m", "20 m", "25 m"],
                "ans": 1,
                "exp": "Thinking distance = speed × reaction time = 20 m/s × 0.8 s = 16 metres. The car travels 16 m before the brake pads even contact the wheels!"
            }
        ]
    },
    {
        "id": 16,
        "badge": "Slide 16 • Competency C-7.2, C-8.2",
        "title": "Scientific Frontiers: The Cosmic Speed Limit & Special Relativity",
        "subtitle": "Where classical kinematics breaks down: Einstein's universal speed limit",
        "teacher": "Classical kinematics assumes that if you run at 10 km/h inside a train moving at 100 km/h, your speed relative to the ground is simply 110 km/h. But what happens if you shine a flashlight from a rocket moving at half the speed of light? Does light travel at 1.5 times the speed of light? Albert Einstein proved: NO! The speed of light (c ≈ 300,000 km/s) is the absolute cosmic speed limit. Let's explore the revolutionary boundary of modern kinematics.",
        "theory": [
            "<strong>The Classical Galilean Assumption:</strong>",
            "Classical Newtonian mechanics assumes that time is absolute and velocities add linearly: $$v' = v_1 + v_2$$ Under this assumption, an object could theoretically be accelerated to infinite speeds given sufficient time and force.",
            "<strong>Einstein's Special Theory of Relativity (1905):</strong>",
            "1. <strong>Postulate 1:</strong> The laws of physics are identical in all inertial reference frames.",
            "2. <strong>Postulate 2 (The Cosmic Speed Limit):</strong> The speed of light in a vacuum (\\(c = 2.998 \\times 10^8\\text{ m/s}\\)) is constant for all observers, regardless of the motion of the light source or observer.",
            "<strong>Relativistic Velocity Addition Formula:</strong>",
            "$$v_{\\text{combined}} = \\frac{v_1 + v_2}{1 + \\frac{v_1 v_2}{c^2}}$$",
            "If a rocket moves at \\(0.8c\\) and fires a laser forward (\\(c\\)):",
            "$$v = \\frac{0.8c + c}{1 + \\frac{0.8c \\cdot c}{c^2}} = \\frac{1.8c}{1 + 0.8} = \\frac{1.8c}{1.8} = \\mathbf{c}$$ Light never travels faster than \\(c\\)!",
            "<strong>Consequences as \\(v \\to c\\):</strong>",
            "• <strong>Time Dilation:</strong> Moving clocks tick slower: $$t' = \\frac{t}{\\sqrt{1 - v^2/c^2}}$$",
            "• <strong>Relativistic Mass:</strong> An object's inertia increases, requiring infinite energy to reach \\(c\\).",
            "• <strong>Conclusion:</strong> Class 9 kinematics (\\(v = u + at\\)) is an exceptionally accurate low-speed approximation (\\(v \\ll c\\)) of Einstein's universal physics!"
        ],
        "key_points": [
            "The speed of light in vacuum (c ≈ 3.0 × 10⁸ m/s) is the absolute cosmic speed limit.",
            "At speeds near c, classical velocity addition fails; relativistic kinematics governs motion.",
            "No object possessing rest mass can reach or exceed the speed of light.",
            "NCERT kinematics equations are the valid low-speed limit (v ≪ c) of Special Relativity."
        ],
        "checkpoints": [
            {
                "num": 31,
                "q": "Why can no particle possessing mass ever be accelerated to or beyond the speed of light in vacuum (c)?",
                "options": [
                    "Because friction in empty space stops it",
                    "Because as speed approaches c, the relativistic inertia/mass increases toward infinity, requiring infinite energy to accelerate further",
                    "Because light carries negative electrical charge",
                    "Because gravity turns off at high speeds"
                ],
                "ans": 1,
                "exp": "According to Einstein's Special Relativity, as an object's speed approaches c, its relativistic mass/inertia increases asymptotically toward infinity. Accelerating it to c would require an infinite amount of energy, making it physically impossible."
            },
            {
                "num": 32,
                "q": "Under what condition are the classical kinematic equations of motion (v = u + at, s = ut + 1/2 at²) extraordinarily accurate and valid?",
                "options": [
                    "Only when objects travel at speeds very close to the speed of light",
                    "When speeds are much less than the speed of light (v ≪ c), as in all everyday engineering and planetary motions",
                    "Only inside nuclear reactors",
                    "Only in deep intergalactic space"
                ],
                "ans": 1,
                "exp": "For all everyday motions (cars, trains, airplanes, rockets, and orbiting planets), v is far less than c (v/c ≈ 0). In this limit, relativistic corrections are negligible (less than 10⁻¹⁰%), making classical kinematics virtually exact."
            }
        ]
    },
    # Slides 17-20: Dedicated Mastery Quiz Challenge (40 Questions)
    {
        "id": 17,
        "badge": "Slide 17 • Dedicated Quiz Challenge (Part 1/4)",
        "title": "Mastery Quiz: Distance, Displacement, Speed & Velocity",
        "subtitle": "Test your mastery on kinematics scalars, vectors, and rates of motion",
        "teacher": "Welcome to Part 1 of our Motion Mastery Quiz Challenge! Here are 10 rigorous questions testing your grasp of distance, displacement, speed, and velocity. Solve each question and click 'View Solution' for detailed step-by-step guidance.",
        "quiz": [
            {
                "id": "q1",
                "q": "1. What is the SI unit of displacement and speed respectively?",
                "options": ["km and km/h", "m and m/s", "cm and cm/s", "m and m/s²"],
                "ans": 1,
                "sol": "The SI unit of displacement is the metre (m), and the SI unit of speed is metre per second (m/s or m·s⁻¹)."
            },
            {
                "id": "q2",
                "q": "2. An object moves through a distance. Can it have zero displacement?",
                "options": [
                    "No, because distance and displacement are always identical",
                    "Yes, if the object returns to its original starting position (initial position = final position)",
                    "Yes, only if the speed was zero throughout",
                    "No, displacement must always exceed distance"
                ],
                "ans": 1,
                "sol": "Displacement is the vector connecting the initial point to the final point. If an object takes a circular or round-trip path and returns to where it started, its displacement is exactly zero, even though it covered a non-zero distance."
            },
            {
                "id": "q3",
                "q": "3. A farmer moves along the boundary of a square field of side 10 m in 40 s. What will be the magnitude of displacement of the farmer at the end of 2 minutes 20 seconds from his initial position?",
                "options": ["10 m", "14.14 m (10√2 m)", "20 m", "35 m"],
                "ans": 1,
                "sol": "Perimeter = 4 × 10 = 40 m. Speed = 40 m / 40 s = 1 m/s. Total time = 2 min 20 s = 140 s. Distance = 140 m. Number of rounds = 140 / 40 = 3.5 rounds. After 3.5 rounds, the farmer is at the diagonally opposite corner of the square field. Magnitude of displacement = Diagonal of square = √(10² + 10²) = √200 = 10√2 ≈ 14.14 m."
            },
            {
                "id": "q4",
                "q": "4. Convert 54 km/h into m/s:",
                "options": ["10 m/s", "15 m/s", "20 m/s", "25 m/s"],
                "ans": 1,
                "sol": "To convert from km/h to m/s, multiply by 5/18: 54 × (5/18) = 3 × 5 = 15 m/s."
            },
            {
                "id": "q5",
                "q": "5. Which statement is true regarding distance and displacement?",
                "options": [
                    "Displacement is always greater than distance",
                    "Distance is a vector while displacement is a scalar",
                    "Magnitude of displacement is less than or equal to distance travelled (|Displacement| ≤ Distance)",
                    "Distance can be negative"
                ],
                "ans": 2,
                "sol": "Because a straight line is the shortest distance between two points, the magnitude of displacement is always less than or equal to the actual path distance travelled."
            },
            {
                "id": "q6",
                "q": "6. An odometer in an automobile measures which physical quantity?",
                "options": ["Instantaneous speed", "Acceleration", "Distance covered", "Average velocity"],
                "ans": 2,
                "sol": "An odometer records the total physical path distance covered by a vehicle in kilometres, while a speedometer indicates instantaneous speed."
            },
            {
                "id": "q7",
                "q": "7. A car travels the first half of a distance at 40 km/h and the second half at 60 km/h. What is the average speed of the car for the entire journey?",
                "options": ["50 km/h", "48 km/h", "45 km/h", "52 km/h"],
                "ans": 1,
                "sol": "Let total distance be 2d. Time for first half t₁ = d/40. Time for second half t₂ = d/60. Total time = d(1/40 + 1/60) = d(5/120) = d/24. Average speed = Total distance / Total time = 2d / (d/24) = 48 km/h (The harmonic mean, not the arithmetic mean!)."
            },
            {
                "id": "q8",
                "q": "8. Under what condition is the magnitude of average velocity equal to the average speed of an object?",
                "options": [
                    "When the object moves along a straight line in a single unchanging direction",
                    "When the object travels in a circle at constant speed",
                    "When the object accelerates and then reverses direction",
                    "It is never equal"
                ],
                "ans": 0,
                "sol": "Average speed equals the magnitude of average velocity if and only if the total distance travelled equals the magnitude of displacement, which occurs strictly when motion is in a straight line without reversing direction."
            },
            {
                "id": "q9",
                "q": "9. A particle travels 4 m East and then 3 m North. What are its distance and displacement respectively?",
                "options": [
                    "Distance = 7 m, Displacement = 5 m at 36.9° North of East",
                    "Distance = 5 m, Displacement = 7 m",
                    "Distance = 7 m, Displacement = 7 m",
                    "Distance = 1 m, Displacement = 5 m"
                ],
                "ans": 0,
                "sol": "Distance = 4 + 3 = 7 m. Displacement = Hypotenuse of right triangle = √(4² + 3²) = √(16 + 9) = √25 = 5 m."
            },
            {
                "id": "q10",
                "q": "10. In which of the following cases of motion are the distance moved and the magnitude of displacement equal?",
                "options": [
                    "If the car is moving on a circular road",
                    "If the car is moving on a straight road",
                    "The pendulum is moving to and fro",
                    "The earth is revolving around the Sun"
                ],
                "ans": 1,
                "sol": "When an object moves along a straight path without reversing direction, distance and displacement are strictly equal in magnitude."
            }
        ]
    },
    {
        "id": 18,
        "badge": "Slide 18 • Dedicated Quiz Challenge (Part 2/4)",
        "title": "Mastery Quiz: Acceleration & Graphical Representations",
        "subtitle": "Test your mastery on slopes, areas, and graphical kinematics",
        "teacher": "Part 2 tests your command of acceleration calculations and graphical analysis of distance-time and velocity-time curves. Solve each question and examine the pop-up solutions.",
        "quiz": [
            {
                "id": "q11",
                "q": "11. What is the SI unit of acceleration?",
                "options": ["m/s", "m·s", "m/s² (or m·s⁻²)", "km/h²"],
                "ans": 2,
                "sol": "Acceleration is rate of change of velocity: (m/s) / s = m/s² (or m·s⁻²)."
            },
            {
                "id": "q12",
                "q": "12. What does a horizontal line parallel to the time axis on a distance-time graph indicate?",
                "options": [
                    "The object is moving with high uniform speed",
                    "The object is at rest (stationary)",
                    "The object is accelerating uniformly",
                    "The object is moving backwards"
                ],
                "ans": 1,
                "sol": "On a distance-time graph, a horizontal line has zero slope, meaning distance does not change as time advances—the object is stationary (at rest)."
            },
            {
                "id": "q13",
                "q": "13. What physical quantity is given by the area under a velocity-time graph?",
                "options": ["Acceleration", "Displacement (Distance travelled)", "Speed", "Force"],
                "ans": 1,
                "sol": "The area enclosed beneath a velocity-time graph represents the total displacement (or distance) covered by the object."
            },
            {
                "id": "q14",
                "q": "14. A velocity-time graph has a constant negative slope. What type of motion does this represent?",
                "options": ["Uniform acceleration", "Uniform retardation (deceleration)", "Non-uniform motion", "Motion with zero speed"],
                "ans": 1,
                "sol": "The slope of a v-t graph represents acceleration. A constant negative slope indicates that velocity is decreasing uniformly with time—uniform retardation."
            },
            {
                "id": "q15",
                "q": "15. A train starts from rest and attains a velocity of 72 km/h in 5 minutes. Assuming acceleration is uniform, what is the acceleration?",
                "options": ["0.067 m/s² (1/15 m/s²)", "0.24 m/s²", "1.44 m/s²", "4.0 m/s²"],
                "ans": 0,
                "sol": "u = 0, v = 72 km/h = 72 × (5/18) = 20 m/s. t = 5 min = 300 s. a = (v - u) / t = (20 - 0) / 300 = 20 / 300 = 1/15 ≈ 0.067 m/s²."
            },
            {
                "id": "q16",
                "q": "16. In the problem above, what is the distance travelled by the train in attaining this velocity?",
                "options": ["1000 m", "3000 m (3 km)", "6000 m", "1500 m"],
                "ans": 1,
                "sol": "s = ut + 1/2 at² = 0 + 1/2 × (1/15) × (300)² = (1/30) × 90000 = 3000 m = 3 km."
            },
            {
                "id": "q17",
                "q": "17. On a distance-time graph, a curve whose slope increases with time indicates:",
                "options": ["Uniform motion", "Accelerated motion", "Decelerated motion", "State of rest"],
                "ans": 1,
                "exp": "Because the slope of an s-t graph represents instantaneous speed, an increasing slope indicates that the object is speeding up (accelerated motion)."
            },
            {
                "id": "q18",
                "q": "18. A car's velocity decreases from 80 km/h to 60 km/h in 5 seconds. What is its acceleration?",
                "options": ["-1.11 m/s²", "-4.0 m/s²", "-2.22 m/s²", "-0.5 m/s²"],
                "ans": 0,
                "sol": "u = 80 × (5/18) = 22.22 m/s. v = 60 × (5/18) = 16.67 m/s. t = 5 s. a = (16.67 - 22.22) / 5 = -5.55 / 5 = -1.11 m/s²."
            },
            {
                "id": "q19",
                "q": "19. The velocity-time graph of an object moving with constant velocity v₀ is:",
                "options": [
                    "A parabola curving upwards",
                    "A horizontal straight line parallel to the time axis at height v₀",
                    "A line passing through the origin at 45°",
                    "A vertical line parallel to the velocity axis"
                ],
                "ans": 1,
                "sol": "When velocity is constant, its value does not change as time elapses, producing a straight horizontal line parallel to the time axis."
            },
            {
                "id": "q20",
                "q": "20. What is the area under the v-t graph of an object moving at 10 m/s for 15 seconds?",
                "options": ["25 m", "150 m", "75 m", "1.5 m"],
                "ans": 1,
                "sol": "Area of rectangle = height × base = 10 m/s × 15 s = 150 m."
            }
        ]
    },
    {
        "id": 19,
        "badge": "Slide 19 • Dedicated Quiz Challenge (Part 3/4)",
        "title": "Mastery Quiz: Kinematic Equations & Derivations",
        "subtitle": "Test your mastery on graphical derivations and 3 equations of motion",
        "teacher": "Part 3 is the ultimate trial on the three equations of motion: v = u + at, s = ut + 1/2 at², and v² = u² + 2as. Apply the graphical method and solve rigorous numerical challenges.",
        "quiz": [
            {
                "id": "q21",
                "q": "21. Which equation represents the position-time relation for motion under uniform acceleration?",
                "options": ["v = u + at", "s = ut + 1/2 at²", "v² = u² + 2as", "v = s / t"],
                "ans": 1,
                "sol": "The second equation of motion, s = ut + 1/2 at², connects position/distance (s) with time (t), known as the position-time relation."
            },
            {
                "id": "q22",
                "q": "22. In the graphical derivation of s = ut + 1/2 at², the term 1/2 at² represents:",
                "options": [
                    "The area of the lower rectangle OADC",
                    "The area of the upper triangle ABD",
                    "The slope of the line AB",
                    "The total perimeter of the trapezium"
                ],
                "ans": 1,
                "sol": "The area of the upper right triangle ABD is 1/2 × base × height = 1/2 × t × (v - u). Since v - u = at, this becomes 1/2 at²."
            },
            {
                "id": "q23",
                "q": "23. A bus starts from rest and moves with uniform acceleration of 0.2 m/s² for 3 minutes. What is the distance travelled?",
                "options": ["18 m", "648 m", "1620 m", "3240 m"],
                "ans": 3,
                "sol": "u = 0, a = 0.2 m/s², t = 3 min = 180 s. s = ut + 1/2 at² = 0 + 1/2 × 0.2 × (180)² = 0.1 × 32400 = 3240 m."
            },
            {
                "id": "q24",
                "q": "24. An electron moving with a velocity of 5 × 10⁴ m/s enters a uniform electric field and acquires an acceleration of 10⁴ m/s² in the direction of motion. How long will it take to acquire a velocity of double its initial velocity?",
                "options": ["1 s", "2.5 s", "5 s", "10 s"],
                "ans": 2,
                "sol": "u = 5 × 10⁴ m/s, v = 2u = 10 × 10⁴ m/s, a = 10⁴ m/s². v = u + at ➔ 10 × 10⁴ = 5 × 10⁴ + (10⁴)t ➔ 5 × 10⁴ = (10⁴)t ➔ t = 5 s."
            },
            {
                "id": "q25",
                "q": "25. In the derivation of the 3rd equation of motion (v² = u² + 2as), what expression is substituted for time t?",
                "options": ["t = (v - u) / a", "t = s / v", "t = (u + v) / a", "t = 2s / a"],
                "ans": 0,
                "sol": "From the first equation v = u + at, we isolate t = (v - u) / a and substitute it into the area of the trapezium s = (v + u)t / 2, yielding s = (v² - u²) / 2a."
            },
            {
                "id": "q26",
                "q": "26. A ball is gently dropped from a height of 20 m. If its velocity increases uniformly at the rate of 10 m/s², with what velocity will it strike the ground?",
                "options": ["10 m/s", "20 m/s", "30 m/s", "40 m/s"],
                "ans": 1,
                "sol": "u = 0, s = 20 m, a = 10 m/s². v² = u² + 2as = 0 + 2(10)(20) = 400 ➔ v = √400 = 20 m/s."
            },
            {
                "id": "q27",
                "q": "27. In the question above, after what time will the ball strike the ground?",
                "options": ["1 s", "2 s", "3 s", "4 s"],
                "ans": 1,
                "sol": "v = u + at ➔ 20 = 0 + 10t ➔ t = 20 / 10 = 2 s."
            },
            {
                "id": "q28",
                "q": "28. The brakes applied to a car produce an acceleration of 6 m/s² in the opposite direction to the motion. If the car takes 2 s to stop after the application of brakes, calculate the distance it travels during this time.",
                "options": ["6 m", "12 m", "24 m", "36 m"],
                "ans": 1,
                "sol": "v = 0, a = -6 m/s², t = 2 s. v = u + at ➔ 0 = u - 6(2) ➔ u = 12 m/s. s = ut + 1/2 at² = 12(2) + 1/2 (-6)(2)² = 24 - 12 = 12 m."
            },
            {
                "id": "q29",
                "q": "29. What is the ratio of distances travelled by a body falling freely from rest in the 1st, 2nd, and 3rd seconds of its motion?",
                "options": ["1 : 2 : 3", "1 : 4 : 9", "1 : 3 : 5 (Galileo's odd-number rule)", "1 : 1 : 1"],
                "ans": 2,
                "sol": "Distance in nth second: s_n = u + a/2(2n - 1). For u = 0: s₁ = g/2(1), s₂ = g/2(3), s₃ = g/2(5). The ratio is 1 : 3 : 5 (Galileo's Law of Odd Numbers)."
            },
            {
                "id": "q30",
                "q": "30. A stone thrown vertically upwards reaches a maximum height of 5 m. What was its initial projection velocity? (g = 9.8 m/s²)",
                "options": ["4.9 m/s", "7.0 m/s", "9.9 m/s", "14.0 m/s"],
                "ans": 2,
                "sol": "At max height v = 0, a = -9.8 m/s², s = 5 m. v² = u² + 2as ➔ 0 = u² + 2(-9.8)(5) ➔ u² = 98 ➔ u = √98 ≈ 9.9 m/s."
            }
        ]
    },
    {
        "id": 20,
        "badge": "Slide 20 • Dedicated Quiz Challenge (Part 4/4)",
        "title": "Mastery Quiz: Circular Motion, Road Safety & Frontiers",
        "subtitle": "Test your mastery on uniform circular motion, stopping distance, and relativistic limits",
        "teacher": "Congratulations on reaching the final slide of our Motion Master Lab! This closing challenge covers uniform circular motion, centripetal dynamics, road safety physics, and Einstein's cosmic speed limit. Once completed, your chapter mastery will be complete!",
        "quiz": [
            {
                "id": "q31",
                "q": "31. A cyclist goes around a circular track of diameter 140 m in 44 seconds. What is the speed of the cyclist?",
                "options": ["5 m/s", "10 m/s", "15 m/s", "20 m/s"],
                "ans": 1,
                "sol": "Diameter = 140 m ➔ radius r = 70 m. Circumference = 2πr = 2 × (22/7) × 70 = 440 m. Speed v = 440 / 44 = 10 m/s."
            },
            {
                "id": "q32",
                "q": "32. In uniform circular motion, the angle between the instantaneous velocity vector and the centripetal acceleration vector is:",
                "options": ["0° (parallel)", "45°", "90° (perpendicular)", "180° (anti-parallel)"],
                "ans": 2,
                "sol": "Instantaneous velocity is directed along the tangent, while centripetal acceleration is directed along the radius toward the center. Tangent and radius are strictly perpendicular (90°)."
            },
            {
                "id": "q33",
                "q": "33. What happens to the centripetal acceleration of a vehicle if its speed around a circular curve is doubled while keeping the curve radius constant?",
                "options": ["It doubles (2×)", "It quadruples (4×)", "It is halved (0.5×)", "It remains the same"],
                "ans": 1,
                "sol": "Centripetal acceleration is a_c = v² / r. Because a_c is proportional to velocity squared (v²), doubling speed (2v) increases centripetal acceleration by 2² = 4 times."
            },
            {
                "id": "q34",
                "q": "34. What physical quantity remains constant for an object executing uniform circular motion?",
                "options": ["Velocity vector", "Linear speed (magnitude of velocity)", "Direction of motion", "Displacement from center"],
                "ans": 1,
                "sol": "In uniform circular motion, the speed (magnitude of velocity) remains constant, while velocity, acceleration direction, and displacement from the starting point change continuously."
            },
            {
                "id": "q35",
                "q": "35. If a stone tied to a string being whirled in a circle suddenly breaks, in which direction does the stone fly?",
                "options": [
                    "Directly toward the center of the circle",
                    "Directly away from the center along the radius",
                    "Along a straight line tangential to the circular path at that instant",
                    "It stops dead in mid-air"
                ],
                "ans": 2,
                "sol": "According to Newton's First Law, when the inward centripetal string tension vanishes, the stone's inertia carries it along a straight line in the direction of its instantaneous tangential velocity."
            },
            {
                "id": "q36",
                "q": "36. Why does doubling driving speed from 50 km/h to 100 km/h increase braking distance by 4 times rather than 2 times?",
                "options": [
                    "Because kinetic energy and braking distance depend on velocity squared: s = u² / 2a",
                    "Because tires melt at 100 km/h",
                    "Because gravity is reduced at higher speeds",
                    "Because brake pads expand linearly"
                ],
                "ans": 0,
                "sol": "From the 3rd equation of motion (v² = u² - 2as), stopping distance s = u² / 2a. Work done by friction must dissipate kinetic energy (1/2 mv²), which scales with velocity squared."
            },
            {
                "id": "q37",
                "q": "37. What is the tip speed of the minute hand of a clock if its length is 7 cm?",
                "options": ["1.22 × 10⁻⁴ m/s", "1.22 × 10⁻³ m/s", "0.7 cm/s", "7 mm/s"],
                "ans": 0,
                "sol": "r = 7 cm = 0.07 m. Time for 1 complete revolution of minute hand = 60 min = 3600 s. Circumference = 2 × (22/7) × 0.07 = 0.44 m. Speed v = 0.44 / 3600 ≈ 1.22 × 10⁻⁴ m/s."
            },
            {
                "id": "q38",
                "q": "38. What is the value of the speed of light in vacuum (the cosmic speed limit c)?",
                "options": ["3.0 × 10⁶ m/s", "3.0 × 10⁸ m/s (~300,000 km/s)", "3.0 × 10¹⁰ km/h", "343 m/s"],
                "ans": 1,
                "sol": "The speed of light in vacuum is c = 299,792,458 m/s ≈ 3.0 × 10⁸ m/s, representing the absolute cosmic speed limit in Special Relativity."
            },
            {
                "id": "q39",
                "q": "39. Why are the classical kinematic equations of motion valid for designing everyday cars and airplanes?",
                "options": [
                    "Because cars travel at the speed of light",
                    "Because vehicle speeds (v) are millions of times smaller than the speed of light (v ≪ c), where relativistic corrections are negligible",
                    "Because Einstein's theory does not apply on Earth",
                    "Because air cancels relativity"
                ],
                "ans": 1,
                "sol": "When v ≪ c, terms like v²/c² approach zero. Classical Galilean kinematics is the exact low-velocity limiting case of relativistic mechanics."
            },
            {
                "id": "q40",
                "q": "40. Total stopping distance of a vehicle equals:",
                "options": [
                    "Thinking distance minus braking distance",
                    "Thinking distance (v × t_reaction) plus Braking distance (u² / 2a)",
                    "Braking distance only",
                    "Reaction time divided by speed"
                ],
                "ans": 1,
                "sol": "Total stopping distance is the sum of thinking distance (travelled during driver reaction time) and braking distance (travelled while decelerating under brakes)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Total Slides: {len(SLIDES_DATA)}")
    checkpoints_count = sum(len(s.get("checkpoints", [])) for s in SLIDES_DATA)
    quiz_count = sum(len(s.get("quiz", [])) for s in SLIDES_DATA)
    print(f"Total In-Slide Checkpoints: {checkpoints_count}")
    print(f"Total Quiz Questions: {quiz_count}")
    assert len(SLIDES_DATA) == 20, "Must be exactly 20 slides"
    assert checkpoints_count == 32, "Must be exactly 32 checkpoints (2 per content slide)"
    assert quiz_count == 40, "Must be exactly 40 quiz questions across slides 17-20"
    print("All curriculum data validations passed!")


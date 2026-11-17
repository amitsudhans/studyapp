#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part2 = [
    {
        "id": 9,
        "title": "Velocity-Time Graphs",
        "subtitle": "Section 4.2.3: Acceleration from Slope & Displacement from Area",
        "speech": (
            "Let us now turn to velocity-time graphs, which pack even more information into a single picture. "
            "Here, time remains on the horizontal X-axis, while velocity is plotted on the vertical Y-axis. "
            "First, how do we interpret the shape? A horizontal straight line means velocity does not change "
            "over time: the object moves with constant velocity and zero acceleration. An inclined straight line "
            "sloping upward indicates constant positive acceleration, while a straight line sloping downward "
            "indicates constant deceleration. Just as before, let us check the geometric slope between two points "
            "on a velocity-time graph: vertical rise v minus u divided by horizontal run t2 minus t1. That ratio "
            "is change in velocity over time, so the slope of a velocity-time graph gives acceleration! Even more "
            "remarkably, look at the region trapped under the velocity-time line and above the time axis. For "
            "constant velocity, the area of that rectangle is height v times width t, which equals displacement! "
            "This rule holds for inclined lines too: the total area enclosed under the velocity-time graph with "
            "the time axis always equals the object's net displacement. For an accelerating vehicle starting from "
            "u and reaching v, that enclosed shape is a trapezium or triangle whose area you can compute in seconds."
        ),
        "checkpoints": [
            {
                "question": "What two physical quantities can be obtained from a velocity-time graph?",
                "options": [
                    "Mass from slope and force from area",
                    "Acceleration from slope and displacement from area under the curve",
                    "Displacement from slope and acceleration from area",
                    "Time from slope and temperature from area"
                ],
                "answer": 1,
                "hint": "Slope is (v - u)/t, while area multiplies velocity (m/s) by time (s).",
                "explanation": "The slope of a v-t graph gives acceleration, and the area enclosed with the time axis gives displacement."
            },
            {
                "question": "What does a horizontal straight line above zero on a velocity-time graph represent?",
                "options": [
                    "The object is at rest",
                    "Constant velocity with zero acceleration",
                    "Constantly increasing acceleration",
                    "Zero displacement at all times"
                ],
                "answer": 1,
                "hint": "Velocity stays at the same non-zero value as time advances.",
                "explanation": "A horizontal v-t line means velocity is unchanging, so acceleration is zero and motion is uniform."
            }
        ]
    },
    {
        "id": 10,
        "title": "First Kinematic Equation",
        "subtitle": "Section 4.3: Deriving v = u + at Under Constant Acceleration",
        "speech": (
            "Now that we understand velocity-time graphs, we can derive the famous kinematic equations for motion "
            "in a straight line with constant acceleration. Let an object start at time t equals zero with initial "
            "velocity u, and accelerate uniformly at rate a until time t, reaching final velocity v. On a "
            "velocity-time graph, this motion forms a straight line rising steadily from height u at time zero "
            "to height v at time t. Recall that the slope of a velocity-time line equals acceleration a. Looking "
            "at the triangle formed above height u, the vertical rise is v minus u, and the horizontal run is "
            "time t. Therefore, acceleration a equals v minus u divided by t. Multiply both sides by t to get "
            "a times t equals v minus u. Adding u to both sides gives the first equation of motion: v equals u "
            "plus a t. Let us appreciate its power: if you know how fast an object started, its steady "
            "acceleration, and how long it accelerated, you can predict its exact velocity at any future second "
            "without redrawing the graph every time. You can also rearrange it to find how long steady braking takes."
        ),
        "checkpoints": [
            {
                "question": "In the first equation of motion v = u + at, what condition must hold?",
                "options": [
                    "The object must remain at rest",
                    "Acceleration a must be constant",
                    "Initial velocity u must be zero",
                    "Time t must be negative"
                ],
                "answer": 1,
                "hint": "A straight-line v-t graph corresponds to uniform velocity change per second.",
                "explanation": "The kinematic equations apply specifically to straight-line motion under constant acceleration."
            },
            {
                "question": "A train starts at u = 5 m/s and accelerates steadily at a = 2 m/s² for t = 6 s. What is v?",
                "options": [
                    "12 m/s",
                    "17 m/s",
                    "22 m/s",
                    "30 m/s"
                ],
                "answer": 1,
                "hint": "Substitute u = 5, a = 2, and t = 6 into v = u + at.",
                "explanation": "v = 5 + (2 × 6) = 5 + 12 = 17 m/s."
            }
        ]
    },
    {
        "id": 11,
        "title": "Kinematic Equations",
        "subtitle": "Section 4.3: Deriving s = ut + ½at² and v² = u² + 2as",
        "speech": (
            "Let us derive the second and third kinematic equations from the exact same velocity-time trapezium! "
            "Remember that displacement s equals the total area enclosed under the velocity-time line from zero "
            "to t. Split this trapezium into two clean shapes: a bottom rectangle of height u and width t, plus "
            "a top right triangle of base t and height v minus u. The rectangle's area is u times t. The "
            "triangle's area is half times base t times height v minus u. From our first equation, v minus u "
            "equals a times t. Substituting a t in place of v minus u gives the triangle's area as half a t "
            "squared! Adding both areas yields the second equation of motion: s equals u t plus half a t squared. "
            "Now, what if a problem does not give you time t? We eliminate t! Write the trapezium area as "
            "average velocity, u plus v over two, multiplied by t. From the first equation, t equals v minus u "
            "over a. Multiplying them gives s equals v squared minus u squared over two a, which rearranges "
            "neatly into our third equation: v squared equals u squared plus two a s."
        ),
        "checkpoints": [
            {
                "question": "In the graphical derivation of s = ut + ½at², what does the ½at² term represent?",
                "options": [
                    "The area of the bottom rectangle on the v-t graph",
                    "The area of the upper right triangle on the v-t graph",
                    "The slope of the position-time graph",
                    "The initial velocity divided by time"
                ],
                "answer": 1,
                "hint": "The trapezium under the v-t line splits into a rectangle (ut) and a triangle above it.",
                "explanation": "The upper triangle has base t and height (v - u) = at, giving area = ½ × t × at = ½at²."
            },
            {
                "question": "Which kinematic equation is best when time t is unknown, given u, a, and s?",
                "options": [
                    "v = u + at",
                    "s = ut + ½at²",
                    "v² = u² + 2as",
                    "v_av = 2πR / T"
                ],
                "answer": 2,
                "hint": "Look for the equation formed by eliminating time t.",
                "explanation": "v² = u² + 2as relates velocities, acceleration, and displacement directly without requiring time t."
            }
        ]
    },
    {
        "id": 12,
        "title": "Braking & Safety",
        "subtitle": "Section 4.3, Example 4.8 & Safe Driving: Stopping Distance & V2V",
        "speech": (
            "Physics equations save lives on real roads! Let us examine Example 4.8 to see why speeding is so "
            "dangerous. Suppose a car brakes with a constant deceleration of four metres per second squared, so "
            "a equals minus four metres per second squared, until it stops at v equals zero. First, convert "
            "highway speeds into SI units. At fifty-four kilometres per hour, which equals fifteen metres per "
            "second, using v squared equals u squared plus two a s gives zero equals fifteen squared minus eight "
            "s, so stopping distance s is twenty-eight point one metres. Now double the car's speed to one "
            "hundred and eight kilometres per hour, or thirty metres per second. Because stopping distance "
            "depends on u squared, doubling speed multiplies stopping distance by four—jumping to one hundred "
            "and twelve point five metres! Add to that the distance travelled during the driver's reaction time "
            "before the brake pedal is even touched. Modern Bridging Science and Society innovations tackle this "
            "with Vehicle-to-Vehicle, or V2V, wireless communication, where cars broadcast braking alerts "
            "instantly to warn following drivers before a collision can occur. Keeping safe following gaps always saves precious lives on busy Indian highways every day."
        ),
        "checkpoints": [
            {
                "question": "In Example 4.8, when braking deceleration is fixed at -4 m/s², doubling speed from 54 km/h to 108 km/h changes stopping distance from 28.1 m to:",
                "options": [
                    "56.2 m (2 times)",
                    "84.3 m (3 times)",
                    "112.5 m (4 times)",
                    "14.0 m (half)"
                ],
                "answer": 2,
                "hint": "Since s = u² / (2|a|), stopping distance scales with the square of initial speed.",
                "explanation": "Doubling speed quadruples u², increasing stopping distance 4× from 28.1 m to 112.5 m."
            },
            {
                "question": "How does Vehicle-to-Vehicle (V2V) communication improve road safety?",
                "options": [
                    "It eliminates friction between tyres and asphalt",
                    "It broadcasts sudden braking alerts instantly to nearby vehicles to cut reaction lag",
                    "It doubles the mass of passenger cars",
                    "It disables brakes during rain"
                ],
                "answer": 1,
                "hint": "Think about reducing the delay before a following driver responds.",
                "explanation": "V2V communication warns nearby drivers immediately about sudden braking or hazards ahead."
            }
        ]
    },
    {
        "id": 13,
        "title": "Motion in Plane",
        "subtitle": "Section 4.4 & 3D Extension: 2D Trajectories & 3D Space",
        "speech": (
            "So far, our objects moved strictly forward or backward along a single straight line, which is "
            "one-dimensional motion. However, most motion around us unfolds across a flat surface or through open "
            "space! When an object changes position along two independent directions simultaneously, we call it "
            "motion in a plane, or two-dimensional motion. Picture a car overtaking another vehicle on a wide "
            "highway: it moves forward along the lane while shifting sideways into the passing lane. Or think "
            "of a kicked soccer ball arcing gracefully through the air: it travels horizontally across the field "
            "while rising and falling vertically under gravity, tracing a curved projectile path. A Ferris wheel "
            "cabin or a ceiling fan blade also moves in a plane, tracing a circle. Can motion go even beyond "
            "two dimensions? Yes! In Ready to Go Beyond, consider three-dimensional motion in space. A car "
            "climbing a winding mountain road changes its forward, sideways, and upward coordinates all at once, "
            "while an aircraft banking through clouds navigates freely along all three spatial axes: length, "
            "width, and altitude. Recognizing whether motion is 1D, 2D, or 3D helps us pick the right coordinate axes and physics model right away today."
        ),
        "checkpoints": [
            {
                "question": "Which example best illustrates motion in a plane (two-dimensional motion)?",
                "options": [
                    "An apple falling straight down to the ground",
                    "A kicked soccer ball arcing across a field",
                    "A swimmer racing in a straight lane",
                    "A parked bicycle at rest"
                ],
                "answer": 1,
                "hint": "Look for simultaneous horizontal and vertical (or two-axis) movement.",
                "explanation": "A kicked soccer ball moves horizontally and vertically at once, making it 2D projectile motion in a plane."
            },
            {
                "question": "Why is an aircraft flying through clouds classified as 3D motion?",
                "options": [
                    "It moves only along a straight runway",
                    "It changes position along three independent spatial axes (length, width, and altitude)",
                    "It never changes velocity",
                    "It has zero displacement"
                ],
                "answer": 1,
                "hint": "Think of forward/back, left/right, and up/down.",
                "explanation": "Aircraft and cars on winding mountain roads move across all three spatial dimensions simultaneously."
            }
        ]
    },
    {
        "id": 14,
        "title": "Uniform Circular Motion",
        "subtitle": "Section 4.4.1 & Activity 4.5: Constant Speed, Changing Velocity",
        "speech": (
            "One of the most important two-dimensional motions in nature and technology is circular motion, from "
            "a spinning bicycle wheel to satellites orbiting Earth. In one complete revolution along a circle of "
            "radius R, the total distance travelled is the circumference, two pi R, while the net displacement "
            "is zero because the object returns to its starting point. If one full lap takes time T, the average "
            "speed is two pi R divided by T. Now, suppose an object moves along a circular path at a strictly "
            "constant speed. We call this uniform circular motion. Here is a classic physics surprise: is uniform "
            "circular motion accelerated, even though speed never changes? Yes! Remember that velocity has both "
            "speed and direction. At every point on the circle, velocity points along the tangent to the circle, "
            "so its direction changes continuously! Changing velocity means non-zero acceleration. Activity 4.5 "
            "proves this beautifully: spin a marble inside a circular adhesive tape ring, then lift the ring "
            "suddenly. The marble flies off in a straight line directly along the tangent at the point of release, "
            "confirming that its instantaneous velocity always points strictly tangentially around the circle at every single moment!"
        ),
        "checkpoints": [
            {
                "question": "Why is uniform circular motion considered accelerated motion even though speed is constant?",
                "options": [
                    "Because the radius grows every second",
                    "Because the direction of velocity changes continuously along the circle",
                    "Because average speed is zero",
                    "Because time stops during rotation"
                ],
                "answer": 1,
                "hint": "Velocity is a vector, so changing direction alone changes velocity.",
                "explanation": "Velocity points along the tangent and changes direction continuously, producing acceleration."
            },
            {
                "question": "In Activity 4.5, when the adhesive tape ring is lifted off a spinning marble, which path does the marble follow?",
                "options": [
                    "It continues in a smaller circle",
                    "It stops immediately in place",
                    "It flies off in a straight line along the tangent at the release point",
                    "It moves straight toward the centre"
                ],
                "answer": 2,
                "hint": "Without the ring pushing it inward, the marble keeps its instantaneous tangential velocity.",
                "explanation": "Once released, the marble moves in a straight line along the tangent to the circle."
            }
        ]
    },
    {
        "id": 15,
        "title": "Phyphox & Extensions",
        "subtitle": "The Journey Beyond: Smartphone Accelerometers & Alternate Equations",
        "speech": (
            "Your own smartphone is actually a pocket physics laboratory! In The Journey Beyond, students use "
            "free apps like Phyphox to access the tiny MEMS accelerometer sensor built inside modern phones. "
            "When you ride an elevator or a school bus and record acceleration versus time, the app plots live "
            "peaks as the elevator starts upward, drops to zero during steady cruising, and dips negative as it "
            "slows to stop at your floor. By connecting real sensor graphs to what we learned, you can see "
            "kinematic concepts come alive outside the textbook. We can also derive helpful alternate kinematic "
            "forms from our three core equations! For instance, replacing initial velocity u with v minus a t "
            "inside s equals u t plus half a t squared yields s equals v t minus half a t squared, useful when "
            "you know final velocity v instead of u. Likewise, combining v equals u plus a t with s equals u t "
            "plus half a t squared gives s equals the average of u and v multiplied by t, showing that under "
            "constant acceleration, displacement equals average velocity times time. Try recording your own gentle elevator or school bus ride!"
        ),
        "checkpoints": [
            {
                "question": "What does a smartphone Phyphox accelerometer record during steady constant-velocity cruising between elevator floors?",
                "options": [
                    "Maximum positive acceleration",
                    "Zero net acceleration change",
                    "Infinite speed",
                    "Circular tangent velocity"
                ],
                "answer": 1,
                "hint": "Constant velocity means velocity is not changing.",
                "explanation": "During steady cruising at constant velocity, acceleration drops to zero."
            },
            {
                "question": "Which alternate equation gives displacement under constant acceleration using initial velocity u, final velocity v, and time t?",
                "options": [
                    "s = [(u + v) / 2] × t",
                    "s = v² - u²",
                    "s = 2πR / T",
                    "s = (v - u) / t"
                ],
                "answer": 0,
                "hint": "For uniform acceleration, average velocity is simply (u + v) / 2.",
                "explanation": "Multiplying average velocity (u + v)/2 by time t gives s = [(u + v)/2] × t."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary",
        "subtitle": "At a Glance: Complete Kinematics Toolkit & Synthesis",
        "speech": (
            "Let us bring the entire chapter together in one crystal-clear mental map. First, describing "
            "position requires an origin O, distance, and direction, with plus to the right and minus to the "
            "left. Second, distance is the scalar total path length, whereas displacement is the vector net "
            "change in position, never exceeding distance. Third, average speed equals total distance over time, "
            "while average velocity equals displacement over time—so a round trip has zero average velocity even "
            "when average speed is high. Fourth, average acceleration equals v minus u over t in metres per "
            "second squared, matching gravity g equals nine point eight metres per second squared in free fall. "
            "Fifth, on position-time graphs, slope gives average velocity and horizontal lines mean rest; on "
            "velocity-time graphs, slope gives acceleration and enclosed area gives displacement. Sixth, for "
            "constant acceleration, our three kinematic equations—v equals u plus a t, s equals u t plus half "
            "a t squared, and v squared equals u squared plus two a s—explain everything from free fall to "
            "vehicle braking distances. Finally, uniform circular motion has speed two pi R over T yet remains "
            "accelerated because tangential velocity direction changes continuously. Great job completing the lectures!"
        ),
        "checkpoints": [
            {
                "question": "Which summary pairing of graph feature and physical meaning is completely correct?",
                "options": [
                    "s-t slope = acceleration; v-t area = velocity",
                    "s-t slope = average velocity; v-t slope = acceleration; v-t area = displacement",
                    "s-t area = acceleration; v-t slope = displacement",
                    "s-t horizontal line = constant acceleration"
                ],
                "answer": 1,
                "hint": "Check the units of vertical/horizontal (slope) and vertical × horizontal (area) for both graphs.",
                "explanation": "s-t slope is velocity (m/s), v-t slope is acceleration (m/s²), and v-t area is displacement (m)."
            },
            {
                "question": "For one complete lap around a circular track of radius R in time T, what are the displacement and average speed?",
                "options": [
                    "Displacement = 2πR; average speed = 0",
                    "Displacement = 0; average speed = 2πR / T",
                    "Displacement = πR²; average speed = R / T",
                    "Displacement = 2R; average speed = 2R / T"
                ],
                "answer": 1,
                "hint": "Start and finish points coincide after one full lap, while path length is the circumference.",
                "explanation": "After one full revolution, net displacement is 0, while distance 2πR divided by T gives average speed 2πR/T."
            }
        ]
    }
]

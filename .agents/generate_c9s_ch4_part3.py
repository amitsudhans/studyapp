#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part3 = [
    {
        "id": 17,
        "title": "Exercise: Core Kinematics",
        "subtitle": "Silent Mastery Quiz 1: Position, Distance, Displacement & Acceleration (10 Questions)",
        "questions": [
            {
                "question": "Which three pieces of information are strictly required to specify an object's position?",
                "options": [
                    "Origin O, distance from O, and direction",
                    "Speed, mass, and time",
                    "Acceleration, force, and volume",
                    "Temperature, distance, and shape"
                ],
                "answer": 0,
                "hint": "Think of how you locate a house on a straight street.",
                "explanation": "Position requires a fixed reference point (origin O), distance, and direction.",
                "solution_steps": [
                    "Choose a fixed reference point called the origin O.",
                    "Measure the distance of the object from O.",
                    "Specify the direction (+ right or - left along a straight line)."
                ]
            },
            {
                "question": "A cyclist rides 30 m east from O, then turns and rides 12 m west. What are total distance and net displacement?",
                "options": [
                    "Distance = 42 m, displacement = +18 m (east)",
                    "Distance = 18 m, displacement = +42 m (east)",
                    "Distance = 42 m, displacement = -18 m (west)",
                    "Distance = 30 m, displacement = +12 m (east)"
                ],
                "answer": 0,
                "hint": "Add path segments for distance; subtract opposite segments for net displacement.",
                "explanation": "Distance = 30 + 12 = 42 m; displacement = +30 - 12 = +18 m east.",
                "solution_steps": [
                    "Total distance = 30 m + 12 m = 42 m.",
                    "Take east as positive (+): net position = +30 m + (-12 m) = +18 m.",
                    "Hence distance is 42 m and displacement is 18 m east."
                ]
            },
            {
                "question": "In Activity 4.1, a ball thrown straight up reaches 12 m and falls back to the thrower's hand. What is its net displacement?",
                "options": [
                    "24 m",
                    "12 m",
                    "0 m",
                    "-12 m"
                ],
                "answer": 2,
                "hint": "Compare the starting position and final position.",
                "explanation": "Since the ball returns to origin O, initial and final positions coincide, giving 0 m displacement.",
                "solution_steps": [
                    "Distance travelled = 12 m up + 12 m down = 24 m.",
                    "Final position equals initial position (origin O).",
                    "Net displacement = final position - initial position = 0 m."
                ]
            },
            {
                "question": "In Example 4.1 (Aryabhatiya / Ganitakaumudi style), two walkers 210 yojanas apart walk toward each other at 9 and 5 yojanas/day. How many days until they meet?",
                "options": [
                    "12 days",
                    "15 days",
                    "18 days",
                    "21 days"
                ],
                "answer": 1,
                "hint": "Add their daily distances because they walk toward each other.",
                "explanation": "Combined rate = 9 + 5 = 14 yojanas/day; time = 210 / 14 = 15 days.",
                "solution_steps": [
                    "Combined closing speed = 9 + 5 = 14 yojanas/day.",
                    "Total initial separation = 210 yojanas.",
                    "Days to meet = 210 / 14 = 15 days."
                ]
            },
            {
                "question": "A swimmer swims 50 m across a pool and back in 100 s. What are average speed and average velocity?",
                "options": [
                    "Average speed = 1 m/s; average velocity = 1 m/s",
                    "Average speed = 0.5 m/s; average velocity = 0 m/s",
                    "Average speed = 1 m/s; average velocity = 0 m/s",
                    "Average speed = 0 m/s; average velocity = 1 m/s"
                ],
                "answer": 2,
                "hint": "Total distance is 100 m, while net displacement is 0 m.",
                "explanation": "Average speed = 100 m / 100 s = 1 m/s; average velocity = 0 m / 100 s = 0 m/s.",
                "solution_steps": [
                    "Total distance = 50 m + 50 m = 100 m, so average speed = 100 / 100 = 1 m/s.",
                    "Net displacement = 0 m because the swimmer returns to the start.",
                    "Average velocity = 0 / 100 = 0 m/s."
                ]
            },
            {
                "question": "Which instrument in a car measures instantaneous speed?",
                "options": [
                    "Odometer",
                    "Speedometer",
                    "Thermometer",
                    "Barometer"
                ],
                "answer": 1,
                "hint": "The odometer logs total distance; look for the dial showing current speed.",
                "explanation": "A speedometer displays instantaneous speed at each moment.",
                "solution_steps": [
                    "Instantaneous speed is speed over an infinitesimally small time interval.",
                    "An odometer records total distance travelled.",
                    "A speedometer displays the vehicle's instantaneous speed."
                ]
            },
            {
                "question": "A highway bus accelerates uniformly from 10 m/s to 20 m/s in 20 s (Example 4.3). What is its average acceleration?",
                "options": [
                    "0.25 m/s²",
                    "0.5 m/s²",
                    "1.0 m/s²",
                    "2.0 m/s²"
                ],
                "answer": 1,
                "hint": "Use a = (v - u) / t.",
                "explanation": "a = (20 - 10) / 20 = 10 / 20 = 0.5 m/s².",
                "solution_steps": [
                    "Initial velocity u = 10 m/s, final velocity v = 20 m/s, time t = 20 s.",
                    "Change in velocity = v - u = 20 - 10 = 10 m/s.",
                    "Average acceleration a = 10 / 20 = 0.5 m/s²."
                ]
            },
            {
                "question": "A car moving at 15 m/s brakes to a complete stop in 5 s. What is its acceleration?",
                "options": [
                    "+3 m/s²",
                    "-3 m/s²",
                    "-5 m/s²",
                    "+0.33 m/s²"
                ],
                "answer": 1,
                "hint": "Final velocity v is 0 m/s.",
                "explanation": "a = (0 - 15) / 5 = -3 m/s².",
                "solution_steps": [
                    "Initial velocity u = 15 m/s, final velocity v = 0 m/s, time t = 5 s.",
                    "a = (v - u) / t = (0 - 15) / 5.",
                    "Acceleration = -3 m/s² (negative sign indicates deceleration)."
                ]
            },
            {
                "question": "An object is dropped from rest and falls freely near Earth's surface (g = 9.8 m/s²). What is its speed after 3 s?",
                "options": [
                    "9.8 m/s",
                    "19.6 m/s",
                    "29.4 m/s",
                    "39.2 m/s"
                ],
                "answer": 2,
                "hint": "Velocity increases by 9.8 m/s every second.",
                "explanation": "v = u + gt = 0 + 9.8 × 3 = 29.4 m/s.",
                "solution_steps": [
                    "Initial velocity u = 0 m/s and g = 9.8 m/s².",
                    "Use v = u + gt.",
                    "v = 0 + 9.8 × 3 = 29.4 m/s."
                ]
            },
            {
                "question": "When is the magnitude of displacement strictly equal to the distance travelled?",
                "options": [
                    "During circular motion",
                    "During straight-line motion in a single direction without reversing",
                    "During a round trip",
                    "Whenever acceleration is negative"
                ],
                "answer": 1,
                "hint": "Any turn or curve makes the path longer than the straight-line shift.",
                "explanation": "Only straight-line motion in one fixed direction has |displacement| = distance.",
                "solution_steps": [
                    "Displacement is the shortest straight-line segment from start to finish.",
                    "If the object never turns or curves, actual path = straight segment.",
                    "Thus |displacement| = distance only in unidirectional straight-line motion."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Exercise: Motion Graphs",
        "subtitle": "Silent Mastery Quiz 2: Position-Time & Velocity-Time Graphs (10 Questions)",
        "questions": [
            {
                "question": "In a standard motion graph, which variable is placed along the horizontal X-axis?",
                "options": [
                    "Distance",
                    "Time",
                    "Acceleration",
                    "Force"
                ],
                "answer": 1,
                "hint": "The independent variable goes on the horizontal axis.",
                "explanation": "Time is plotted along the X-axis, while position or velocity is plotted on the Y-axis.",
                "solution_steps": [
                    "Time progresses independently during motion.",
                    "Conventionally, the independent variable sits on the horizontal X-axis.",
                    "Position or velocity is plotted vertically on the Y-axis."
                ]
            },
            {
                "question": "What does a horizontal straight line at s = 40 m on a position-time graph indicate?",
                "options": [
                    "Constant non-zero velocity",
                    "Constant acceleration",
                    "The object is at rest at s = 40 m",
                    "Increasing speed"
                ],
                "answer": 2,
                "hint": "Check whether position changes as time increases.",
                "explanation": "Position remains 40 m for all values of time t, so the object is stationary (at rest).",
                "solution_steps": [
                    "At every time t, position s stays fixed at 40 m.",
                    "Slope = Δs / Δt = 0 / Δt = 0 m/s.",
                    "Zero velocity means the object is at rest."
                ]
            },
            {
                "question": "On a position-time graph, a line segment goes from A(2 s, 10 m) to B(6 s, 30 m). What is the average velocity?",
                "options": [
                    "2 m/s",
                    "5 m/s",
                    "10 m/s",
                    "20 m/s"
                ],
                "answer": 1,
                "hint": "Compute the slope (s2 - s1) / (t2 - t1).",
                "explanation": "Slope = (30 - 10) / (6 - 2) = 20 / 4 = 5 m/s.",
                "solution_steps": [
                    "Change in position Δs = 30 m - 10 m = 20 m.",
                    "Time interval Δt = 6 s - 2 s = 4 s.",
                    "Average velocity = slope = 20 / 4 = 5 m/s."
                ]
            },
            {
                "question": "Two straight lines A and B appear on the same position-time axes. Line A is steeper than Line B. Which is true?",
                "options": [
                    "Object A is slower than Object B",
                    "Object A has higher velocity than Object B",
                    "Object B has higher acceleration",
                    "Both objects are at rest"
                ],
                "answer": 1,
                "hint": "Steeper slope on an s-t graph means larger Δs/Δt.",
                "explanation": "Greater steepness means greater slope, which corresponds to higher velocity.",
                "solution_steps": [
                    "Slope of a position-time graph equals velocity.",
                    "Line A is steeper, so slope(A) > slope(B).",
                    "Therefore Object A moves with higher velocity than Object B."
                ]
            },
            {
                "question": "What does an upward-curving position-time graph represent?",
                "options": [
                    "Uniform velocity",
                    "Object at rest",
                    "Increasing velocity (positive acceleration)",
                    "Zero displacement"
                ],
                "answer": 2,
                "hint": "Notice that the slope becomes steeper as time increases.",
                "explanation": "Increasing steepness means velocity increases over time, indicating positive acceleration.",
                "solution_steps": [
                    "The instantaneous slope of an s-t graph represents velocity.",
                    "An upward curve grows steeper with increasing time.",
                    "Growing velocity indicates accelerated motion."
                ]
            },
            {
                "question": "What does the slope of a velocity-time graph represent?",
                "options": [
                    "Displacement",
                    "Average speed",
                    "Acceleration",
                    "Total distance"
                ],
                "answer": 2,
                "hint": "Divide vertical change (Δv) by horizontal change (Δt).",
                "explanation": "Slope = (v - u) / Δt, which is the definition of acceleration.",
                "solution_steps": [
                    "Vertical axis is velocity v (m/s), horizontal axis is time t (s).",
                    "Slope = Δv / Δt.",
                    "Change in velocity per unit time is acceleration (m/s²)."
                ]
            },
            {
                "question": "What does the area enclosed between a velocity-time graph and the time axis represent?",
                "options": [
                    "Acceleration",
                    "Displacement",
                    "Instantaneous speed",
                    "Mass"
                ],
                "answer": 1,
                "hint": "Multiply height (m/s) by base (s).",
                "explanation": "Area under a v-t graph has units (m/s) × s = m and represents displacement.",
                "solution_steps": [
                    "Area is calculated as velocity × time.",
                    "Multiplying m/s by s yields metres (m).",
                    "Thus, the area under a v-t graph equals net displacement."
                ]
            },
            {
                "question": "A car moves at a constant velocity of 12 m/s for 8 s. On its v-t graph, what is the area under the line?",
                "options": [
                    "1.5 m",
                    "20 m",
                    "96 m",
                    "192 m"
                ],
                "answer": 2,
                "hint": "The shape is a rectangle of height 12 m/s and width 8 s.",
                "explanation": "Area = 12 m/s × 8 s = 96 m displacement.",
                "solution_steps": [
                    "Constant velocity gives a horizontal line at v = 12 m/s from t = 0 to t = 8 s.",
                    "Area of rectangle = height × width = 12 × 8.",
                    "Displacement = 96 m."
                ]
            },
            {
                "question": "A velocity-time line rises linearly from u = 0 m/s at t = 0 s to v = 20 m/s at t = 5 s. Find acceleration and displacement.",
                "options": [
                    "a = 4 m/s², s = 50 m",
                    "a = 4 m/s², s = 100 m",
                    "a = 5 m/s², s = 50 m",
                    "a = 20 m/s², s = 25 m"
                ],
                "answer": 0,
                "hint": "Slope = 20/5; area is a triangle of base 5 and height 20.",
                "explanation": "a = 20 / 5 = 4 m/s², and triangle area s = ½ × 5 × 20 = 50 m.",
                "solution_steps": [
                    "Acceleration a = slope = (20 - 0) / (5 - 0) = 4 m/s².",
                    "Shape under the v-t line is a right triangle of base 5 s and height 20 m/s.",
                    "Displacement s = ½ × 5 × 20 = 50 m."
                ]
            },
            {
                "question": "A velocity-time line slopes downward linearly from 18 m/s to 0 m/s in 6 s. What is the acceleration?",
                "options": [
                    "+3 m/s²",
                    "-3 m/s²",
                    "-6 m/s²",
                    "0 m/s²"
                ],
                "answer": 1,
                "hint": "Downward slope on a v-t graph means negative acceleration.",
                "explanation": "a = (0 - 18) / 6 = -3 m/s².",
                "solution_steps": [
                    "Initial velocity u = 18 m/s, final velocity v = 0 m/s, time t = 6 s.",
                    "Slope = (0 - 18) / 6 = -18 / 6.",
                    "Acceleration = -3 m/s²."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Equations & Braking",
        "subtitle": "Silent Mastery Quiz 3: Kinematic Equations, Stopping Distance & V2V (10 Questions)",
        "questions": [
            {
                "question": "An object starts with u = 4 m/s and accelerates at a = 3 m/s² for t = 5 s. Find final velocity v.",
                "options": [
                    "15 m/s",
                    "19 m/s",
                    "23 m/s",
                    "12 m/s"
                ],
                "answer": 1,
                "hint": "Use v = u + at.",
                "explanation": "v = 4 + (3 × 5) = 4 + 15 = 19 m/s.",
                "solution_steps": [
                    "Given u = 4 m/s, a = 3 m/s², t = 5 s.",
                    "Apply v = u + at.",
                    "v = 4 + 3(5) = 19 m/s."
                ]
            },
            {
                "question": "A scooter starts from rest (u = 0) with constant acceleration a = 2 m/s². How far does it travel in 6 s?",
                "options": [
                    "12 m",
                    "24 m",
                    "36 m",
                    "72 m"
                ],
                "answer": 2,
                "hint": "Use s = ut + ½at² with u = 0.",
                "explanation": "s = 0 + ½(2)(6²) = 36 m.",
                "solution_steps": [
                    "Given u = 0 m/s, a = 2 m/s², t = 6 s.",
                    "Apply s = ut + ½at².",
                    "s = 0 + ½ × 2 × 36 = 36 m."
                ]
            },
            {
                "question": "Convert 54 km/h and 108 km/h into m/s (Example 4.8).",
                "options": [
                    "10 m/s and 20 m/s",
                    "15 m/s and 30 m/s",
                    "20 m/s and 40 m/s",
                    "5.4 m/s and 10.8 m/s"
                ],
                "answer": 1,
                "hint": "Multiply km/h by 5/18.",
                "explanation": "54 × 5/18 = 15 m/s, and 108 × 5/18 = 30 m/s.",
                "solution_steps": [
                    "1 km/h = 1000 m / 3600 s = 5/18 m/s.",
                    "54 × (5/18) = 15 m/s.",
                    "108 × (5/18) = 30 m/s."
                ]
            },
            {
                "question": "A car travelling at 15 m/s brakes at a = -4 m/s² until it stops (Example 4.8). What is its braking distance?",
                "options": [
                    "15.0 m",
                    "28.1 m",
                    "56.2 m",
                    "112.5 m"
                ],
                "answer": 1,
                "hint": "Use v² = u² + 2as with v = 0.",
                "explanation": "0 = 15² + 2(-4)s ⇒ 8s = 225 ⇒ s = 28.125 ≈ 28.1 m.",
                "solution_steps": [
                    "Given u = 15 m/s, v = 0 m/s, a = -4 m/s².",
                    "Apply v² = u² + 2as: 0 = 225 - 8s.",
                    "s = 225 / 8 = 28.125 m ≈ 28.1 m."
                ]
            },
            {
                "question": "If the same car in Example 4.8 travels at 30 m/s (108 km/h) and brakes at -4 m/s², what is its braking distance?",
                "options": [
                    "28.1 m",
                    "56.2 m",
                    "112.5 m",
                    "225.0 m"
                ],
                "answer": 2,
                "hint": "Doubling speed quadruples u² in s = u² / (2|a|).",
                "explanation": "0 = 30² - 8s ⇒ s = 900 / 8 = 112.5 m.",
                "solution_steps": [
                    "Given u = 30 m/s, v = 0 m/s, a = -4 m/s².",
                    "Apply v² = u² + 2as: 0 = 900 - 8s.",
                    "s = 900 / 8 = 112.5 m (4× the distance at 15 m/s)."
                ]
            },
            {
                "question": "If a driver moving at 20 m/s has a reaction time of 0.5 s before pressing the brakes, how far does the car move during reaction time?",
                "options": [
                    "5 m",
                    "10 m",
                    "20 m",
                    "40 m"
                ],
                "answer": 1,
                "hint": "During reaction time, the car still moves at constant speed u.",
                "explanation": "Reaction distance = speed × reaction time = 20 m/s × 0.5 s = 10 m.",
                "solution_steps": [
                    "Before braking starts, velocity remains constant at 20 m/s.",
                    "Reaction time = 0.5 s.",
                    "Reaction distance = 20 × 0.5 = 10 m."
                ]
            },
            {
                "question": "Which equation of motion is derived by combining s = [(u + v)/2]t and t = (v - u)/a?",
                "options": [
                    "v = u + at",
                    "s = ut + ½at²",
                    "v² = u² + 2as",
                    "v_av = 2πR / T"
                ],
                "answer": 2,
                "hint": "Notice that (u + v)(v - u) = v² - u².",
                "explanation": "Multiplying gives s = (v² - u²)/(2a), which rearranges to v² = u² + 2as.",
                "solution_steps": [
                    "Write s = [(u + v)/2] × [(v - u)/a].",
                    "Expand numerator: (v + u)(v - u) = v² - u².",
                    "Multiply both sides by 2a: v² - u² = 2as ⇒ v² = u² + 2as."
                ]
            },
            {
                "question": "A stone is thrown straight up at u = 19.6 m/s (g = 9.8 m/s² downward, so a = -9.8 m/s²). How long does it take to reach maximum height?",
                "options": [
                    "1 s",
                    "2 s",
                    "4 s",
                    "9.8 s"
                ],
                "answer": 1,
                "hint": "At maximum height, final velocity v = 0.",
                "explanation": "0 = 19.6 - 9.8t ⇒ t = 19.6 / 9.8 = 2 s.",
                "solution_steps": [
                    "At the highest point, v = 0 m/s.",
                    "Use v = u + at with u = 19.6 m/s and a = -9.8 m/s².",
                    "0 = 19.6 - 9.8t ⇒ t = 2 s."
                ]
            },
            {
                "question": "An object accelerates uniformly from u = 10 m/s to v = 20 m/s in 4 s. Using s = [(u + v)/2]t, find its displacement.",
                "options": [
                    "40 m",
                    "60 m",
                    "80 m",
                    "120 m"
                ],
                "answer": 1,
                "hint": "Average velocity is (10 + 20)/2 = 15 m/s.",
                "explanation": "s = [(10 + 20)/2] × 4 = 15 × 4 = 60 m.",
                "solution_steps": [
                    "Compute average velocity = (10 + 20) / 2 = 15 m/s.",
                    "Multiply by time interval t = 4 s.",
                    "Displacement s = 15 × 4 = 60 m."
                ]
            },
            {
                "question": "Why does V2V (Vehicle-to-Vehicle) communication help prevent highway pile-ups?",
                "options": [
                    "It increases braking distance",
                    "It transmits immediate braking warnings to trailing cars, reducing human reaction delay",
                    "It turns curved roads into straight lines",
                    "It removes gravity from highways"
                ],
                "answer": 1,
                "hint": "Earlier warning gives following drivers or automated brakes extra time.",
                "explanation": "V2V wireless alerts warn trailing vehicles instantly when a car ahead brakes hard.",
                "solution_steps": [
                    "Total stopping distance = reaction distance + braking distance.",
                    "V2V alerts notify trailing vehicles immediately when a lead car brakes.",
                    "Earlier warning cuts reaction delay and lowers collision risk."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Mastery",
        "subtitle": "Silent Mastery Quiz 4: Circular Motion, 2D/3D, Phyphox & Chapter Review (10 Questions)",
        "questions": [
            {
                "question": "An athlete completes one full lap around a circular track of radius R = 70 m in 44 s (take π = 22/7). What is the average speed?",
                "options": [
                    "5 m/s",
                    "10 m/s",
                    "20 m/s",
                    "0 m/s"
                ],
                "answer": 1,
                "hint": "Use v_av = 2πR / T.",
                "explanation": "Circumference = 2 × (22/7) × 70 = 440 m; v_av = 440 / 44 = 10 m/s.",
                "solution_steps": [
                    "Compute circumference: 2πR = 2 × (22/7) × 70 = 440 m.",
                    "Time for one revolution T = 44 s.",
                    "Average speed = 440 / 44 = 10 m/s."
                ]
            },
            {
                "question": "In the previous question, what is the athlete's net displacement after completing 1 full circular lap?",
                "options": [
                    "440 m",
                    "140 m",
                    "70 m",
                    "0 m"
                ],
                "answer": 3,
                "hint": "Where does the athlete finish relative to the start?",
                "explanation": "After one full lap, the athlete returns to the exact starting point, so displacement = 0 m.",
                "solution_steps": [
                    "One full revolution brings the athlete back to the starting point.",
                    "Initial position equals final position.",
                    "Net displacement = 0 m."
                ]
            },
            {
                "question": "At any instant during uniform circular motion, in which direction does the object's velocity vector point?",
                "options": [
                    "Directly toward the centre",
                    "Directly away from the centre",
                    "Along the tangent to the circular path",
                    "Perpendicular to the plane of the circle"
                ],
                "answer": 2,
                "hint": "Remember Activity 4.5 with the marble inside a tape ring.",
                "explanation": "Instantaneous velocity in circular motion always points along the tangent to the circle.",
                "solution_steps": [
                    "In circular motion, the object moves along the circumference.",
                    "At any point, its instantaneous direction of motion is the tangent.",
                    "Activity 4.5 confirms the marble flies off along the tangent when released."
                ]
            },
            {
                "question": "Why is uniform circular motion classified as accelerated motion?",
                "options": [
                    "Speed keeps increasing every lap",
                    "Velocity direction changes continuously even at constant speed",
                    "Radius changes every second",
                    "Net distance is zero"
                ],
                "answer": 1,
                "hint": "Acceleration occurs whenever velocity (magnitude OR direction) changes.",
                "explanation": "Continuous change in the tangential direction of velocity means velocity is changing, so acceleration is non-zero.",
                "solution_steps": [
                    "Velocity is a vector with both speed and direction.",
                    "In uniform circular motion, speed is constant, but direction changes at every point.",
                    "Changing velocity implies non-zero acceleration."
                ]
            },
            {
                "question": "The minute hand of a clock is 14 cm long. How far does its tip travel in 30 minutes (half a revolution, π = 22/7)?",
                "options": [
                    "22 cm",
                    "44 cm",
                    "88 cm",
                    "28 cm"
                ],
                "answer": 1,
                "hint": "In 30 minutes, the tip traces a semicircle of length πR.",
                "explanation": "Distance = πR = (22/7) × 14 = 44 cm (while displacement is diameter 2R = 28 cm).",
                "solution_steps": [
                    "30 minutes is half of a full 60-minute revolution.",
                    "Distance = ½ × 2πR = πR = (22/7) × 14.",
                    "Tip travels 44 cm."
                ]
            },
            {
                "question": "For the same 14 cm minute hand over 30 minutes, what is the magnitude of the tip's net displacement?",
                "options": [
                    "0 cm",
                    "14 cm",
                    "28 cm",
                    "44 cm"
                ],
                "answer": 2,
                "hint": "After half a circle, the tip is directly opposite its start across the diameter.",
                "explanation": "Net displacement equals the diameter 2R = 2 × 14 = 28 cm.",
                "solution_steps": [
                    "Half a revolution places the tip diametrically opposite the start.",
                    "Shortest straight-line distance across the circle is the diameter 2R.",
                    "Displacement magnitude = 2 × 14 = 28 cm."
                ]
            },
            {
                "question": "Which motion is an example of 3D motion rather than 1D or 2D motion?",
                "options": [
                    "A train on a straight track",
                    "A coin sliding on a flat carrom board",
                    "A car climbing a winding mountain road",
                    "A marble rolling inside a flat tape ring"
                ],
                "answer": 2,
                "hint": "Look for simultaneous changes in horizontal X, Y, and vertical Z coordinates.",
                "explanation": "A car on a winding mountain road changes forward, sideways, and vertical elevation simultaneously (3D).",
                "solution_steps": [
                    "Straight train = 1D; flat carrom coin and flat tape ring = 2D.",
                    "Winding mountain road changes X, Y, and altitude Z.",
                    "Therefore it is 3D motion."
                ]
            },
            {
                "question": "In The Journey Beyond, what sensor inside a smartphone does the Phyphox app use to measure acceleration in elevators?",
                "options": [
                    "Microphone",
                    "Accelerometer",
                    "GPS compass only",
                    "Ambient light sensor"
                ],
                "answer": 1,
                "hint": "Its name matches the physical quantity a = Δv/Δt.",
                "explanation": "Phyphox reads the smartphone's built-in accelerometer to log acceleration over time.",
                "solution_steps": [
                    "Smartphones contain tiny MEMS accelerometers.",
                    "Phyphox records live acceleration data as the elevator starts, cruises, and stops.",
                    "Students can directly observe positive, zero, and negative acceleration peaks."
                ]
            },
            {
                "question": "Which alternate equation correctly expresses displacement s in terms of final velocity v, acceleration a, and time t?",
                "options": [
                    "s = vt - ½at²",
                    "s = vt + ½at²",
                    "s = v - at",
                    "s = 2vt"
                ],
                "answer": 0,
                "hint": "Substitute u = v - at into s = ut + ½at².",
                "explanation": "s = (v - at)t + ½at² = vt - at² + ½at² = vt - ½at².",
                "solution_steps": [
                    "From v = u + at, write u = v - at.",
                    "Substitute into s = ut + ½at²: s = (v - at)t + ½at².",
                    "Simplify: s = vt - ½at²."
                ]
            },
            {
                "question": "A car accelerates from 5 m/s to 15 m/s over a distance of 50 m. What is its constant acceleration?",
                "options": [
                    "1 m/s²",
                    "2 m/s²",
                    "4 m/s²",
                    "10 m/s²"
                ],
                "answer": 1,
                "hint": "Use v² = u² + 2as since time is not given.",
                "explanation": "15² = 5² + 2a(50) ⇒ 225 = 25 + 100a ⇒ 100a = 200 ⇒ a = 2 m/s².",
                "solution_steps": [
                    "Given u = 5 m/s, v = 15 m/s, s = 50 m.",
                    "Use v² = u² + 2as: 225 = 25 + 100a.",
                    "Solve: 100a = 200 ⇒ a = 2 m/s²."
                ]
            }
        ]
    }
]

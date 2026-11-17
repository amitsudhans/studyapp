#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part1 = [
    {
        "id": 1,
        "title": "Motion Around Us",
        "subtitle": "Natural Variety, Idealized Motion & New Physical Quantities",
        "speech": (
            "Welcome, students, to Chapter 4, Describing Motion Around Us. Look closely at nature around you. "
            "Butterflies flit from flower to flower, horses gallop across fields, ocean tides rise and fall, "
            "tiny dust particles dance in a sunbeam, and climber tendrils coil slowly upward. Every living and "
            "non-living thing exhibits motion, yet real-world motion is often complex, combining twists, gusts, "
            "and uneven speeds. How do physicists study such intricate movement? They begin with idealized motion, "
            "stripping away minor disturbances like air drag to examine pure linear, circular, and oscillatory "
            "forms. Once we master these clean models, we can understand real vehicles, planets, and athletes. "
            "In earlier classes, you learned basic distance and speed. In this chapter, we upgrade our toolkit "
            "with vector quantities that care about direction. We will distinguish distance from displacement, "
            "average speed from average velocity, and introduce average acceleration. We will also read and plot "
            "velocity-time graphs, derive three powerful kinematic equations for constant acceleration, and explore "
            "two-dimensional uniform circular motion. Let us observe, measure, and predict motion using the clear, "
            "universal language of physics. By the end of this chapter, you will read real-world motion graphs "
            "effortlessly and solve everyday speed, braking, and circular-path problems with confidence."
        ),
        "checkpoints": [
            {
                "question": "Why do scientists study idealized linear, circular, and oscillatory motions first?",
                "options": [
                    "To simplify complex real-world motion into clear, analyzable models",
                    "Because air resistance does not exist anywhere on Earth",
                    "Because real objects never move in curves or straight lines",
                    "To avoid measuring time intervals in experiments"
                ],
                "answer": 0,
                "hint": "Think about how models help isolate core patterns before adding real-world complications.",
                "explanation": "Scientists use idealized motion to strip away minor disturbances and uncover fundamental relationships cleanly."
            },
            {
                "question": "Which set lists the three new directional or rate quantities introduced in this chapter?",
                "options": [
                    "Mass, volume, and density",
                    "Displacement, average velocity, and average acceleration",
                    "Temperature, pressure, and heat",
                    "Force, work, and electrical charge"
                ],
                "answer": 1,
                "hint": "These quantities extend basic distance and speed by including direction and velocity change.",
                "explanation": "This chapter introduces displacement, average velocity, and average acceleration alongside graphs and kinematic equations."
            }
        ]
    },
    {
        "id": 2,
        "title": "Position & Reference",
        "subtitle": "Section 4.1 & 4.1.1: Reference Point O & Sign Convention",
        "speech": (
            "Let us begin with the simplest kind of movement: motion in a straight line, also called linear "
            "motion. Think of swimmers racing in straight lanes, an apple falling straight down, or a train "
            "gliding along a straight track. To describe where an object is at any moment, stating a number alone "
            "is never enough. Saying a bus stop is five hundred metres away leaves us wondering: in which "
            "direction? Therefore, describing position requires three ingredients: a fixed reference point called "
            "the origin O, a distance from O, and a direction. Relative to this chosen origin O, an object is in "
            "motion if its position changes over time, and at rest if its position stays unchanged over time. "
            "Along a straight line, there are only two possible directions from the origin O: forward and backward, "
            "or right and left. By standard sign convention, positions to the right of origin O are assigned a "
            "plus sign, while positions to the left of origin O are assigned a minus sign. For instance, plus "
            "forty metres means forty metres right of O, whereas minus twenty metres means twenty metres left of O. "
            "Notice that changing your chosen origin O changes the position numbers, even though the object stays right there."
        ),
        "checkpoints": [
            {
                "question": "What three pieces of information are needed to specify an object's position?",
                "options": [
                    "Mass, speed, and colour",
                    "Origin (reference point), distance, and direction",
                    "Time, acceleration, and area",
                    "Temperature, length, and volume"
                ],
                "answer": 1,
                "hint": "Saying '500 m' alone is incomplete without knowing from where and which way.",
                "explanation": "Position requires a fixed reference point (origin O), the distance from O, and the direction."
            },
            {
                "question": "Using standard straight-line sign convention from origin O, what does -35 m represent?",
                "options": [
                    "35 m to the right of origin O",
                    "35 m to the left of origin O",
                    "An impossible negative length",
                    "35 seconds before starting"
                ],
                "answer": 1,
                "hint": "Plus is to the right of O, and minus is to the opposite side.",
                "explanation": "By convention, positions to the right of O are positive (+) and positions to the left of O are negative (-)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Distance vs Displacement",
        "subtitle": "Section 4.1.2 & Activity 4.1: Scalar Path vs Vector Net Change",
        "speech": (
            "Now let us carefully separate two terms that sound similar in daily speech but mean very different "
            "things in physics: distance travelled and displacement. Total distance travelled is the entire length "
            "of the actual path covered by a moving object. It is a scalar quantity, meaning it needs only a "
            "numerical value with units, and it never decreases as long as the object keeps moving. Displacement, "
            "by contrast, is the shortest straight-line change in position from the starting point to the final "
            "point. Because displacement depends on direction as well as size, it is a vector quantity. Both "
            "distance and displacement share the SI unit metre. Let us examine Activity 4.1: a ball is thrown "
            "vertically upward from origin O to height ten metres at point A, falls past point B at six metres, "
            "and returns to O at point C. At A, distance is ten metres and displacement is plus ten metres. At B "
            "on the way down, distance grows to fourteen metres, while displacement drops to plus six metres. At C, "
            "distance reaches twenty metres, but net displacement becomes zero! Thus, magnitude of displacement is "
            "always less than or equal to total distance."
        ),
        "checkpoints": [
            {
                "question": "In Activity 4.1, a ball goes vertically up 10 m to A and falls back 4 m to B (height 6 m). What are its distance and displacement?",
                "options": [
                    "Distance 14 m, displacement +6 m",
                    "Distance 6 m, displacement +14 m",
                    "Distance 10 m, displacement 0 m",
                    "Distance 14 m, displacement +14 m"
                ],
                "answer": 0,
                "hint": "Add the upward and downward path lengths for distance; measure net height from O for displacement.",
                "explanation": "Total path = 10 m + 4 m = 14 m, while net change in position from O is +6 m."
            },
            {
                "question": "Which inequality is always true for any moving object?",
                "options": [
                    "Magnitude of displacement > distance travelled",
                    "Magnitude of displacement <= distance travelled",
                    "Distance travelled is always zero",
                    "Displacement is always a scalar"
                ],
                "answer": 1,
                "hint": "The straight line between start and finish is never longer than the actual path.",
                "explanation": "Displacement magnitude equals distance only along a single-direction straight line; otherwise it is strictly smaller."
            }
        ]
    },
    {
        "id": 4,
        "title": "Average Speed",
        "subtitle": "Section 4.1.3 & Example 4.1: Uniform Motion & Ancient Indian Problems",
        "speech": (
            "How fast does an object cover its path? Average speed is defined as total distance travelled divided "
            "by the total time interval. If an object covers equal distances in equal intervals of time, no matter "
            "how small those intervals are, it is in uniform motion and its speed stays constant. If it covers "
            "unequal distances in equal time intervals, like a bus weaving through city traffic, it is in "
            "non-uniform motion. Speed-time reasoning has deep roots in India's scientific heritage. Ancient "
            "mathematical treatises such as Aryabhata's Aryabhatiya from the fifth century CE and Narayana "
            "Pandita's Ganitakaumudi from the fourteenth century CE posed clever motion problems using traditional "
            "distance units like the yojana. Look at Example 4.1: two postmen start two hundred and ten yojanas "
            "apart and walk directly toward each other. One covers nine yojanas per day, and the other covers "
            "five yojanas per day. Together, each day they close the gap by nine plus five, which equals fourteen "
            "yojanas per day. Dividing the total distance of two hundred and ten yojanas by their combined daily "
            "rate of fourteen yojanas per day gives exactly fifteen days until they meet. This elegant reasoning "
            "shows how breaking a motion problem into relative daily progress makes complex journeys simple to solve."
        ),
        "checkpoints": [
            {
                "question": "What defines uniform motion along a straight line?",
                "options": [
                    "Covering equal distances in equal intervals of time",
                    "Changing direction every second",
                    "Stopping at regular traffic signals",
                    "Covering larger distances each successive second"
                ],
                "answer": 0,
                "hint": "Think of steady cruise control on a straight, empty highway.",
                "explanation": "Uniform motion means equal distances are covered in all equal time intervals."
            },
            {
                "question": "In Example 4.1, two postmen 210 yojanas apart walk toward each other at 9 and 5 yojanas/day. When do they meet?",
                "options": [
                    "10 days",
                    "15 days",
                    "21 days",
                    "30 days"
                ],
                "answer": 1,
                "hint": "Their combined closing speed is 9 + 5 = 14 yojanas per day.",
                "explanation": "Time = 210 yojanas / (9 + 5) yojanas per day = 210 / 14 = 15 days."
            }
        ]
    },
    {
        "id": 5,
        "title": "Average Velocity",
        "subtitle": "Section 4.1.3 & Example 4.2: Directional Rate & Instantaneous Speed",
        "speech": (
            "While average speed tracks total path length over time, physics also needs to track how quickly "
            "position changes in a specific direction. Average velocity is defined as net displacement divided by "
            "the time interval, measured in metres per second. Because displacement is a vector, average velocity "
            "also carries both magnitude and direction! Consider Example 4.2: a swimmer swims across a "
            "twenty-five-metre pool and immediately swims back to the starting wall in fifty seconds. What is "
            "the total distance travelled? Twenty-five metres out plus twenty-five metres back equals fifty "
            "metres, so the average speed is fifty divided by fifty, or one metre per second. However, the swimmer "
            "returns to the exact starting point, making net displacement zero metres! Consequently, the average "
            "velocity is zero divided by fifty, which is zero metres per second. Now, what if we want to know a "
            "car's speed at one exact instant rather than averaged over a whole trip? Look at the dashboard "
            "speedometer: it shows instantaneous speed. Taking the limiting value of average velocity over an "
            "infinitesimally small time interval gives instantaneous velocity, bridging averages to exact moments. "
            "Whenever an object moves along a straight line at constant velocity, instantaneous velocity equals average velocity."
        ),
        "checkpoints": [
            {
                "question": "In Example 4.2, a swimmer swims 25 m across a pool and back in 50 s. What is the average velocity?",
                "options": [
                    "1 m/s",
                    "0.5 m/s",
                    "0 m/s",
                    "2 m/s"
                ],
                "answer": 2,
                "hint": "Average velocity uses net displacement, and the swimmer returned to the start.",
                "explanation": "Net displacement is 0 m for a round trip, so average velocity = 0 / 50 = 0 m/s (even though average speed is 1 m/s)."
            },
            {
                "question": "What does a car's speedometer directly display?",
                "options": [
                    "Average velocity over the whole trip",
                    "Instantaneous speed at that moment",
                    "Total displacement from home",
                    "Average acceleration since start"
                ],
                "answer": 1,
                "hint": "It updates immediately as you press the accelerator or brake.",
                "explanation": "A speedometer reads instantaneous speed, the magnitude of motion over an infinitesimally small time interval."
            }
        ]
    },
    {
        "id": 6,
        "title": "Average Acceleration",
        "subtitle": "Section 4.1.4, Activity 4.2 & Examples 4.3–4.4: Velocity Change",
        "speech": (
            "In everyday life, vehicles rarely stay at constant velocity; they speed up at green lights and slow "
            "down at stops. To measure how rapidly velocity changes, we define average acceleration as the change "
            "in velocity divided by the time interval, written as final velocity v minus initial velocity u, all "
            "divided by time t. Its SI unit is metre per second squared. When speed increases in the direction of "
            "motion, acceleration is positive and points with velocity. When an object slows down, acceleration "
            "points opposite to velocity and is negative. In Activity 4.2, comparing cars accelerating from zero "
            "to one hundred kilometres per hour shows that shorter times mean higher acceleration. Look at Example "
            "4.3: a highway bus speeds up from ten to twenty metres per second in twenty seconds, giving a change "
            "of plus ten divided by twenty, or plus zero point five metres per second squared. When it brakes from "
            "fifteen metres per second to rest in five seconds, acceleration is zero minus fifteen over five, "
            "giving minus three metres per second squared. In Example 4.4, a freely falling object gains nine point "
            "eight metres per second every second, giving constant acceleration due to gravity g."
        ),
        "checkpoints": [
            {
                "question": "A bus slows down from 15 m/s to rest (0 m/s) in 5 s (Example 4.3). What is its average acceleration?",
                "options": [
                    "+3 m/s²",
                    "-3 m/s²",
                    "+15 m/s²",
                    "-0.5 m/s²"
                ],
                "answer": 1,
                "hint": "Use a = (v - u) / t with v = 0 m/s and u = 15 m/s.",
                "explanation": "a = (0 - 15) / 5 = -3 m/s². The negative sign shows acceleration opposes the motion."
            },
            {
                "question": "In Example 4.4, what is the constant acceleration due to gravity (g) of a dropped object near Earth's surface?",
                "options": [
                    "0.5 m/s²",
                    "3.0 m/s²",
                    "9.8 m/s²",
                    "15.0 m/s²"
                ],
                "answer": 2,
                "hint": "Every second of free fall increases downward velocity by this standard value.",
                "explanation": "Near Earth's surface, freely falling objects accelerate downward at g = 9.8 m/s²."
            }
        ]
    },
    {
        "id": 7,
        "title": "Plotting Motion Graphs",
        "subtitle": "Section 4.2, Activity 4.3 & Example 4.5: Axes, Scales & Curves",
        "speech": (
            "Tables of numbers tell us where an object was at each second, but line graphs turn raw data into "
            "an instant visual story of motion. With a graph, we can spot uniform motion, speeding up, stopping, "
            "and compare two moving objects at a glance. Let us follow Activity 4.3 to construct a position-time "
            "graph cleanly on grid paper. First, draw two perpendicular axes meeting at origin O. Plot the "
            "independent variable, time, along the horizontal X-axis, and the dependent variable, position, along "
            "the vertical Y-axis. Second, choose convenient uniform scales so the data fills most of the grid "
            "without cramping, such as one centimetre equals ten seconds on the X-axis and one centimetre equals "
            "twenty metres on the Y-axis. Mark each ordered pair from Table 4.3 carefully as a crisp dot. When "
            "the points align along a ruler, draw a straight line; that signals uniform velocity. Now look at "
            "Example 4.5 with Table 4.4: a vehicle starts from rest and covers larger distances in each equal "
            "time interval. When we plot and join those points smoothly, we obtain an upward-curving graph, "
            "visually revealing non-uniform, accelerated motion. Always label both axes with physical quantities "
            "and their SI units, and record your chosen scale clearly at the top right corner of the graph sheet."
        ),
        "checkpoints": [
            {
                "question": "Which quantity is conventionally plotted on the horizontal X-axis in motion graphs?",
                "options": [
                    "Position",
                    "Velocity",
                    "Time",
                    "Acceleration"
                ],
                "answer": 2,
                "hint": "Time is the independent variable against which position or velocity changes.",
                "explanation": "Time is plotted along the horizontal X-axis, while position or velocity is plotted along the vertical Y-axis."
            },
            {
                "question": "In Example 4.5 (Table 4.4), a vehicle starting from rest and speeding up produces what shape on a position-time graph?",
                "options": [
                    "A horizontal flat line",
                    "An upward-curving line",
                    "A vertical straight line",
                    "A downward straight line"
                ],
                "answer": 1,
                "hint": "Because speed increases, position grows faster in later seconds than in earlier seconds.",
                "explanation": "Increasing speed means unequal distances in equal time intervals, producing an upward curve."
            }
        ]
    },
    {
        "id": 8,
        "title": "Position-Time Graphs",
        "subtitle": "Section 4.2.2, Activity 4.4 & Examples 4.6–4.7: Slopes & Steepness",
        "speech": (
            "Now let us learn how to read position-time graphs like a physicist. First, examine the shape of the "
            "graph. A straight inclined line tells us the object is moving at constant velocity, because position "
            "changes steadily with time. A curved line tells us velocity is changing, meaning the object is "
            "accelerating. What about Example 4.6, where the position-time graph is a flat horizontal line? Since "
            "position stays fixed as time ticks forward, the object is completely at rest, with zero velocity! "
            "Next, in Activity 4.4, we extract a number from a straight line segment AB by computing its geometric "
            "slope. Drop vertical and horizontal lines from A and B to form a right triangle ABC. The slope "
            "equals vertical rise BC divided by horizontal run CA, which is s2 minus s1 divided by t2 minus t1. "
            "That ratio is literally displacement divided by time interval—meaning the slope of a position-time "
            "graph equals average velocity! In Example 4.7, we compare two objects A and B on the same axes: the "
            "steeper line has a larger slope and therefore moves faster than the gentler line. Even without "
            "doing long arithmetic, the steepness of a position-time line immediately reveals which runner is ahead."
        ),
        "checkpoints": [
            {
                "question": "What does the slope of a position-time graph represent?",
                "options": [
                    "Total distance travelled",
                    "Average acceleration",
                    "Average velocity",
                    "Total time interval"
                ],
                "answer": 2,
                "hint": "Slope is vertical change (s2 - s1) divided by horizontal change (t2 - t1).",
                "explanation": "Since (s2 - s1)/(t2 - t1) is displacement over time, the slope of an s-t graph equals average velocity."
            },
            {
                "question": "In Example 4.7, if object A has a steeper straight position-time line than object B, what can we conclude?",
                "options": [
                    "Object A is at rest",
                    "Object A has a higher velocity than object B",
                    "Object B is accelerating faster",
                    "Both objects have the same speed"
                ],
                "answer": 1,
                "hint": "Steeper slope means more displacement per unit time.",
                "explanation": "A steeper position-time line has a greater slope, indicating a greater velocity."
            }
        ]
    }
]

#!/usr/bin/env python3
"""
Generate Slides 1 to 8 data for NCERT Class 5 Mathematics - Chapter 5: Far and Near
"""

slides_1_to_8 = [
    {
        "id": 1,
        "heading": "Choosing Units",
        "tagline": "Selecting the Appropriate Unit: Millimetres, Centimetres, Metres, or Kilometres",
        "color": "from-amber-500 to-orange-600",
        "badge": "Class 5 Maths • Chapter 5",
        "audio_text": (
            "Welcome, young explorers and mathematicians! Today we journey into the world of spatial distance with Far and Near. "
            "In our daily lives, we measure lengths of all kinds: from the tiny thickness of an eraser to the towering height of monument gates and the vast highway distances between cities. "
            "To measure effectively, our very first task is to choose the most sensible unit of measurement! "
            "If you measure a small object like a pencil, a handkerchief, or the width of your notebook, centimetres provide the ideal scale. "
            "If you measure a taller structure like the historic India Gate in New Delhi, the depth of a village drinking well, or the length of a cricket pitch, metres are the natural choice! "
            "Using centimetres to describe a highway between Delhi and Jaipur would require hundreds of thousands of tiny numbers, which is clumsy and confusing. "
            "Instead, we use kilometres for long travel distances. "
            "By choosing the appropriate metric unit, we make measurements simple, readable, and practical."
        ),
        "theory_blocks": [
            {
                "title": "The Metric Hierarchy",
                "content": "Millimetre (mm) for tiny thicknesses; Centimetre (cm) for hand-held objects; Metre (m) for rooms, sports pitches, and monuments; Kilometre (km) for road and rail travel.",
                "icon": "📏"
            },
            {
                "title": "Real-World Matching",
                "content": "Handkerchief = ~25 cm; India Gate Height = ~42 m; Well Depth = ~15 m; Highway between cities = ~250 km.",
                "icon": "🏛️"
            },
            {
                "title": "Sensible Units Principle",
                "content": "Choose the unit whose numerical value is easy to read, write, and communicate without excessively huge or awkward fractions.",
                "icon": "🎯"
            }
        ],
        "checkpoints": [
            {
                "question": "Which unit is best suited to measure the height of the historic India Gate in New Delhi?",
                "options": [
                    "Metres (m)",
                    "Centimetres (cm)",
                    "Millimetres (mm)",
                    "Kilometres (km)"
                ],
                "correct": 0,
                "feedback": "Correct! India Gate stands approximately 42 metres tall, making metres the most practical unit."
            },
            {
                "question": "Which unit should you use to measure the length of a cotton handkerchief?",
                "options": [
                    "Centimetres (cm)",
                    "Kilometres (km)",
                    "Metres (m)",
                    "Miles"
                ],
                "correct": 0,
                "feedback": "Spot on! A handkerchief is around 25 to 30 centimetres long, ideal for a standard ruler."
            }
        ]
    },
    {
        "id": 2,
        "heading": "Unit Equivalence",
        "tagline": "Connecting Centimetres and Metres Using Double Number Lines",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Equivalence on Double Lines",
        "audio_text": (
            "Lengths can be expressed in different units while representing the exact same physical distance! "
            "The golden conversion bridge between centimetres and metres is: 100 centimetres equals 1 metre! "
            "Therefore, 200 centimetres equals 2 metres, 300 centimetres equals 3 metres, and 500 centimetres equals 5 metres. "
            "What if a fabric stole or sari measures 240 centimetres? "
            "Let us partition 240 centimetres into hundreds and remaining tens: 240 is 200 centimetres plus 40 centimetres. "
            "Since 200 centimetres equals 2 metres, 240 centimetres is exactly 2 metres and 40 centimetres! "
            "Our textbook visualizes this relationship using double number lines: a top scale graduated in metres and a bottom scale graduated in centimetres. "
            "Every mark on the metre line aligns perfectly with its hundredfold value on the centimetre line below it! "
            "Double number lines allow you to translate seamlessly between single-unit and mixed-unit descriptions."
        ),
        "theory_blocks": [
            {
                "title": "The Golden Rule: 1 m = 100 cm",
                "content": "To convert metres to centimetres, multiply by 100. To convert centimetres to metres, divide by 100 (or separate into hundreds).",
                "icon": "⚖️"
            },
            {
                "title": "Double Number Line Alignment",
                "content": "0 m = 0 cm; 1 m = 100 cm; 2 m = 200 cm; 2.4 m = 240 cm; 5 m = 500 cm. Dual scales make equivalence visually intuitive.",
                "icon": "📊"
            },
            {
                "title": "Sari & Fabric Measures",
                "content": "Traditional Indian saris measure 550 cm (5 m 50 cm), and dupattas or stoles measure 240 cm (2 m 40 cm).",
                "icon": "🧵"
            }
        ],
        "checkpoints": [
            {
                "question": "How is 240 centimetres expressed in mixed metres and centimetres?",
                "options": [
                    "2 metres 40 centimetres",
                    "24 metres",
                    "20 metres 4 centimetres",
                    "2 metres 4 centimetres"
                ],
                "correct": 0,
                "feedback": "Correct! 240 cm = 200 cm + 40 cm = 2 m 40 cm."
            },
            {
                "question": "A silk sari is 5 metres and 50 centimetres long. What is its length in centimetres alone?",
                "options": [
                    "550 cm",
                    "5,500 cm",
                    "505 cm",
                    "55 cm"
                ],
                "correct": 0,
                "feedback": "Spot on! 5 m = 500 cm, so 500 cm + 50 cm = 550 cm."
            }
        ]
    },
    {
        "id": 3,
        "heading": "Comparing Lengths",
        "tagline": "Standardizing to a Single Unit Before Applying Inequalities",
        "color": "from-teal-600 to-cyan-700",
        "badge": "Comparative Analysis",
        "audio_text": (
            "When comparing two lengths expressed in different units, we must never compare the numbers blindly! "
            "For example, if you compare 456 centimetres with 5 metres, you might be tempted to think 456 is larger than 5 because 456 is a bigger number. "
            "However, you must remember that each metre contains 100 centimetres! "
            "To compare correctly, first convert both quantities into the exact same common unit. "
            "Let us convert 5 metres into centimetres: 5 times 100 gives 500 centimetres! "
            "Now compare: 456 centimetres is strictly less than 500 centimetres. Therefore, 456 centimetres is less than 5 metres! "
            "We write: 456 cm is less than 5 m, using the opening-to-the-larger-value inequality symbol. "
            "Always equalize units before comparing, ordering, adding, or subtracting lengths."
        ),
        "theory_blocks": [
            {
                "title": "The Golden Rule of Comparison",
                "content": "Never compare raw numbers of different units! Always convert all quantities into the same unit (usually the smaller unit, such as cm) first.",
                "icon": "🔍"
            },
            {
                "title": "Inequality Signs (<, =, >)",
                "content": "The wide open mouth always faces the greater value: 456 cm < 500 cm (5 m); 300 cm = 3 m; 6 m 20 cm > 600 cm.",
                "icon": "⚖️"
            },
            {
                "title": "Bridge Calculation",
                "content": "To compare 3 m 25 cm with 350 cm: 3 m 25 cm = 325 cm. Since 325 < 350, 3 m 25 cm < 350 cm.",
                "icon": "🌉"
            }
        ],
        "checkpoints": [
            {
                "question": "Which symbol correctly completes the comparison: 456 cm ___ 5 m?",
                "options": [
                    "< (Less than)",
                    "> (Greater than)",
                    "= (Equal to)",
                    "≈ (Approximately)"
                ],
                "correct": 0,
                "feedback": "Correct! 5 m = 500 cm. Since 456 cm < 500 cm, 456 cm < 5 m."
            },
            {
                "question": "Which length is the greatest: 2 m 80 cm, 300 cm, or 295 cm?",
                "options": [
                    "300 cm (3 m)",
                    "2 m 80 cm (280 cm)",
                    "295 cm",
                    "They are all equal"
                ],
                "correct": 0,
                "feedback": "Spot on! Converting to cm: 280 cm, 300 cm, 295 cm. 300 cm is the greatest."
            }
        ]
    },
    {
        "id": 4,
        "heading": "Tallest Statues",
        "tagline": "Height Data and Proportional Analysis of World Monuments",
        "color": "from-emerald-600 to-green-700",
        "badge": "Architectural Heights",
        "audio_text": (
            "Our textbook features an inspiring architectural study: the tallest statues in the world! "
            "Standing proudly on the banks of the Narmada River in Gujarat, India, is the magnificent Statue of Unity, depicting Sardar Vallabhbhai Patel. "
            "It is the tallest statue in the world, soaring to an astonishing height of 182 metres! "
            "Notice how significant this number is: 182 matches the total number of constituencies in the Gujarat Legislative Assembly. "
            "The second tallest statue is the Spring Temple Buddha in China, standing at 128 metres. "
            "And the famous Statue of Liberty in New York, USA, stands at 93 metres including its pedestal. "
            "Let us compare their heights using subtraction! "
            "How much taller is the Statue of Unity than the Spring Temple Buddha? "
            "We subtract: 182 metres minus 128 metres equals 54 metres! "
            "And how does the Statue of Unity compare to the Statue of Liberty? 182 minus 93 equals 89 metres taller: nearly double the height of the Statue of Liberty! "
            "Height comparisons allow us to appreciate the grand scale of monumental engineering."
        ),
        "theory_blocks": [
            {
                "title": "Statue of Unity (India)",
                "content": "Height: 182 metres (597 feet). Located in Kevadia (Ekta Nagar), Gujarat. The tallest statue on Earth, built to withstand earthquakes and high wind speeds.",
                "icon": "🇮🇳"
            },
            {
                "title": "Spring Temple Buddha (China)",
                "content": "Height: 128 metres (420 feet). The second tallest statue in the world, surpassed by the Statue of Unity by 54 metres.",
                "icon": "🏯"
            },
            {
                "title": "Statue of Liberty (USA)",
                "content": "Height: 93 metres (305 feet) from ground to torch tip. The Statue of Unity is nearly twice as tall (182 m vs 93 m).",
                "icon": "🗽"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the height of India's Statue of Unity?",
                "options": [
                    "182 metres",
                    "128 metres",
                    "93 metres",
                    "200 metres"
                ],
                "correct": 0,
                "feedback": "Correct! The Statue of Unity stands at 182 metres tall."
            },
            {
                "question": "How much taller is the Statue of Unity (182 m) than the Spring Temple Buddha (128 m)?",
                "options": [
                    "54 metres",
                    "64 metres",
                    "44 metres",
                    "50 metres"
                ],
                "correct": 0,
                "feedback": "Spot on! 182 - 128 = 54 metres."
            }
        ]
    },
    {
        "id": 5,
        "heading": "Measuring Tools",
        "tagline": "Instruments for Measuring Long Distances on Earth",
        "color": "from-purple-600 to-indigo-700",
        "badge": "Surveying Instruments",
        "audio_text": (
            "How do engineers, surveyors, and sports officials measure long outdoor distances accurately? "
            "A standard 30-centimetre ruler is wonderful for school notebooks, but measuring a whole football field or a newly paved road with a small ruler would take forever! "
            "Instead, specialized long-distance instruments are employed: "
            "First, the long surveyor tape: sturdy flexible tapes made of fiberglass or steel that extend 30, 50, or 100 metres! "
            "Second, the rodometer, commonly called a measuring wheel: as a surveyor pushes this single wheel along the ground, a mechanical or digital counter tracks each revolution, measuring the road distance smoothly in metres. "
            "Third, the laser distance meter: an electronic device that emits a safe laser beam to a distant wall and calculates the exact distance in fractions of a second based on the light's reflection time! "
            "And fourth, optical rangefinders used by sports coaches and navigators. "
            "Each instrument is designed for precision across different terrains."
        ),
        "theory_blocks": [
            {
                "title": "Measuring Wheel (Rodometer)",
                "content": "A rolling wheel with a calibrated circumference (often exactly 1 metre). Each full rotation records 1 metre on the attached counter.",
                "icon": "🎡"
            },
            {
                "title": "Laser Distance Meter",
                "content": "Uses laser reflection to measure distances up to 200 metres with millimeter precision in a fraction of a second.",
                "icon": "🔦"
            },
            {
                "title": "Surveyor Long Tape",
                "content": "Reinforced steel or fiberglass ribbon tape extending 30 m, 50 m, or 100 m, used on athletics tracks and construction foundations.",
                "icon": "📏"
            }
        ],
        "checkpoints": [
            {
                "question": "Which tool is commonly rolled along the road by highway surveyors to measure long road lengths?",
                "options": [
                    "A measuring wheel (rodometer)",
                    "A 15 cm school ruler",
                    "A sewing needle",
                    "A compass divider"
                ],
                "correct": 0,
                "feedback": "Correct! A measuring wheel (rodometer) records revolutions as it rolls, measuring long distances conveniently."
            },
            {
                "question": "How does a laser distance meter calculate distance?",
                "options": [
                    "By measuring the time taken for a laser beam to reflect back from a target",
                    "By rolling along the ground",
                    "By weighing the air between two points",
                    "By counting the footsteps of the operator"
                ],
                "correct": 0,
                "feedback": "Spot on! It uses the speed of light and the reflection time to calculate distance with extreme accuracy."
            }
        ]
    },
    {
        "id": 6,
        "heading": "The Kilometre",
        "tagline": "Unveiling the Kilometre: 1,000 Metres of Ground Distance",
        "color": "from-rose-600 to-pink-700",
        "badge": "1 km = 1,000 m",
        "audio_text": (
            "Now let us step outside onto the school playground to discover the kilometre! "
            "The prefix 'kilo' comes from an ancient Greek word meaning one thousand. "
            "Therefore, 1 kilometre represents exactly 1,000 metres! "
            "How far is 1,000 metres in human terms? "
            "If your school athletics running track is 200 metres long, you would need to run around it five complete times to complete 1 kilometre: 5 times 200 equals 1,000 metres! "
            "If an average Grade 5 student's walking pace spans approximately 50 centimetres (half a metre), it takes about 2,000 footsteps to walk one single kilometre! "
            "Walking a kilometre at a brisk pace takes about 12 to 15 minutes. "
            "When we travel between towns and states, highway milestones show distances in kilometres because metres would be too cumbersome to write on road signs. "
            "Always remember: 1 kilometre equals 1,000 metres, and half a kilometre equals 500 metres!"
        ),
        "theory_blocks": [
            {
                "title": "The 1 km = 1,000 m Rule",
                "content": "'Kilo' means 1,000. 1 km = 1,000 m; 1/2 km = 500 m; 1/4 km = 250 m; 3/4 km = 750 m.",
                "icon": "🛣️"
            },
            {
                "title": "Footsteps & Time",
                "content": "Average step = ~50 cm (0.5 m). 1 km = 2,000 footsteps. Brisk walking time for 1 km = 12 to 15 minutes.",
                "icon": "👟"
            },
            {
                "title": "Highway Milestones",
                "content": "Yellow and white stones mark National Highways; green and white mark State Highways, showing distances in kilometres.",
                "icon": "🪨"
            }
        ],
        "checkpoints": [
            {
                "question": "How many metres are there in 1 kilometre?",
                "options": [
                    "1,000 metres",
                    "100 metres",
                    "10 metres",
                    "10,000 metres"
                ],
                "correct": 0,
                "feedback": "Correct! 'Kilo' means thousand, so 1 km = 1,000 m."
            },
            {
                "question": "If a running track is 250 metres long, how many full laps equal 1 kilometre?",
                "options": [
                    "4 laps (4 × 250 = 1,000 m)",
                    "2 laps",
                    "5 laps",
                    "10 laps"
                ],
                "correct": 0,
                "feedback": "Spot on! 4 laps × 250 m = 1,000 m = 1 km."
            }
        ]
    },
    {
        "id": 7,
        "heading": "Race Track",
        "tagline": "Planning Logistics for a 3-Kilometre School Marathon",
        "color": "from-amber-600 to-yellow-600",
        "badge": "Event Planning Logistics",
        "audio_text": (
            "Let us apply kilometre arithmetic to organize a community 3-kilometre mini-marathon from our textbook! "
            "A 3-kilometre race covers a total distance of: 3 times 1,000 metres, which is 3,000 metres! "
            "To keep runners hydrated and safe, race organizers place water stations, medical tents, and directional flag marshals at equal intervals along the course. "
            "Suppose the organizers decide to place a water station every 500 metres starting after the start line. "
            "How many water stations will there be? "
            "Let us calculate the points along the course: "
            "Station 1 at 500 metres; Station 2 at 1,000 metres (which is 1 km); Station 3 at 1,500 metres (1.5 km); Station 4 at 2,000 metres (2 km); Station 5 at 2,500 metres (2.5 km); and the final celebration at the 3,000-metre finish line! "
            "That gives five intermediate refreshment stations along the course. "
            "Breaking long race distances into metric intervals ensures perfect event logistics."
        ),
        "theory_blocks": [
            {
                "title": "3 km in Metres",
                "content": "3 km = 3 × 1,000 m = 3,000 metres. A 5-km race = 5,000 m; a 10-km race = 10,000 m.",
                "icon": "🏃‍♂️"
            },
            {
                "title": "Water Station Intervals",
                "content": "Dividing total distance by interval length: 3,000 m / 500 m = 6 segments, giving 5 intermediate refreshment stations.",
                "icon": "💧"
            },
            {
                "title": "Safety & Marshal Points",
                "content": "Marshals placed every 250 m ensure complete visual safety and correct navigation around race turns.",
                "icon": "🚩"
            }
        ],
        "checkpoints": [
            {
                "question": "How many metres are in a 3-kilometre race course?",
                "options": [
                    "3,000 metres",
                    "300 metres",
                    "30,000 metres",
                    "1,500 metres"
                ],
                "correct": 0,
                "feedback": "Correct! 3 km = 3 × 1,000 m = 3,000 m."
            },
            {
                "question": "If a water station is placed every 500 metres, at what distance mark is the second water station?",
                "options": [
                    "1,000 metres (1 km)",
                    "500 metres",
                    "1,500 metres",
                    "2,000 metres"
                ],
                "correct": 0,
                "feedback": "Spot on! Station 1 is at 500 m, Station 2 is at 500 + 500 = 1,000 m (1 km)."
            }
        ]
    },
    {
        "id": 8,
        "heading": "Train Journey",
        "tagline": "The Vivek Express: 4,189 Kilometres Across 9 Indian States",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Rail Route Arithmetic",
        "audio_text": (
            "Did you know that the longest train journey in India is operated by the historic Vivek Express? "
            "Introduced to commemorate the 150th birth anniversary of Swami Vivekananda, this extraordinary train runs all the way from Dibrugarh in Assam in the northeast, down to Kanniyakumari in Tamil Nadu at the southernmost tip of peninsular India! "
            "The total route covers a staggering distance of 4,189 kilometres! "
            "The train passes through 9 Indian states and takes around 75 hours to complete the journey, making over 55 major scheduled stops. "
            "Let us examine intermediate station distances: "
            "From Dibrugarh to Guwahati is approximately 560 kilometres. "
            "From Guwahati onward to Malda Town in West Bengal is about 640 kilometres. "
            "By calculating distances between consecutive railway junctions, railway dispatchers create timetable schedules, plan locomotive refuelling, and ensure passenger safety across thousands of kilometres! "
            "Indian Railways unites our diverse nation through precision mathematics."
        ),
        "theory_blocks": [
            {
                "title": "Vivek Express Record",
                "content": "Route: Dibrugarh (Assam) to Kanniyakumari (Tamil Nadu). Distance: 4,189 km. Duration: ~75 hours. 9 Indian states traversed.",
                "icon": "🚆"
            },
            {
                "title": "Station Intervals",
                "content": "Distance between stations = Milestone(Station B) - Milestone(Station A). Analyzing route segments teaches multi-digit subtraction.",
                "icon": "🚉"
            },
            {
                "title": "Time and Speed",
                "content": "Average speed = Total Distance / Total Time. 4,189 km / 75 hours ≈ 56 km/h (including stops across varied terrain).",
                "icon": "⏱️"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the total route length of the Vivek Express, India's longest train journey?",
                "options": [
                    "4,189 kilometres",
                    "1,820 kilometres",
                    "2,500 kilometres",
                    "6,000 kilometres"
                ],
                "correct": 0,
                "feedback": "Correct! The Vivek Express travels 4,189 km from Dibrugarh to Kanniyakumari."
            },
            {
                "question": "If a train travels 560 km in Segment 1 and 640 km in Segment 2, what is the combined distance of both segments?",
                "options": [
                    "1,200 km",
                    "1,100 km",
                    "1,300 km",
                    "1,190 km"
                ],
                "correct": 0,
                "feedback": "Spot on! 560 + 640 = 1,200 km."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 1 to 8. Count: {len(slides_1_to_8)}")


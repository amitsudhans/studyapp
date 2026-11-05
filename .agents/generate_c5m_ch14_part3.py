# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 14: Maps and Locations - Part 3 (Slides 17 to 20)
Syllabus: Joyful Mathematics (NEP 2020)
40 Comprehensive Quiz Questions (10 per challenge slide)
- Zero human names
- Zero raw LaTeX
- Full solution_html with step-by-step derivation
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Avian Migration, Cardinal Directions & Campsite Legends",
        "questions": [
            {
                "question": "Which Indian state is home to the Bharatpur Bird Sanctuary where Siberian cranes migrate?",
                "options": ["Gujarat", "Rajasthan", "Madhya Pradesh", "Uttarakhand"],
                "answer": 1,
                "explanation": "The famous Keoladeo National Park (Bharatpur Bird Sanctuary) is located in Rajasthan.",
                "hint": "Recall the historic bird sanctuary of Rajasthan.",
                "solution_html": "<div class='space-y-2'><p>1. Bharatpur Bird Sanctuary is located in <strong>Rajasthan</strong>.</p></div>"
            },
            {
                "question": "When standing outdoors facing the rising Sun in the morning, which direction are you facing?",
                "options": ["North", "South", "East", "West"],
                "answer": 2,
                "explanation": "The Sun always rises in the East.",
                "hint": "The Sun rises in the East and sets in the West.",
                "solution_html": "<div class='space-y-2'><p>1. The rising Sun marks the <strong>East</strong> direction.</p></div>"
            },
            {
                "question": "If you are facing East, which cardinal direction does your left hand point toward?",
                "options": ["North", "South", "East", "West"],
                "answer": 0,
                "explanation": "When facing East, stretching your arms puts your left hand pointing North and right hand pointing South.",
                "hint": "Left is North when facing the morning Sun.",
                "solution_html": "<div class='space-y-2'><p>1. Facing East ➔ Left hand points <strong>North</strong>.</p></div>"
            },
            {
                "question": "Which direction is directly behind you when you face the rising Sun?",
                "options": ["North", "South", "West", "North-East"],
                "answer": 2,
                "explanation": "West is directly opposite to East (behind your back).",
                "hint": "The direction where the Sun sets.",
                "solution_html": "<div class='space-y-2'><p>1. Opposite of East = <strong>West</strong>.</p></div>"
            },
            {
                "question": "Which cardinal direction lies directly opposite to North along the vertical axis?",
                "options": ["East", "West", "South", "North-West"],
                "answer": 2,
                "explanation": "North and South form the vertical axis of the compass and are directly opposite.",
                "hint": "Opposite of top (North) is bottom (South).",
                "solution_html": "<div class='space-y-2'><p>1. Opposite of North = <strong>South</strong>.</p></div>"
            },
            {
                "question": "What is the angle between North and East on a standard compass rose?",
                "options": ["45 degrees", "90 degrees", "180 degrees", "360 degrees"],
                "answer": 1,
                "explanation": "Adjacent cardinal directions are perpendicular, forming a 90° right angle.",
                "hint": "A quarter turn is 90 degrees.",
                "solution_html": "<div class='space-y-2'><p>1. North and East form a perpendicular quarter turn = <strong>90°</strong>.</p></div>"
            },
            {
                "question": "According to the bird watching campsite map legend, which tent is located west of the central road?",
                "options": ["Green tent", "Blue tent", "Purple tent", "Yellow tent"],
                "answer": 1,
                "explanation": "The map clue states that the tent west (left) of the road is blue.",
                "hint": "West is to the left of the road.",
                "solution_html": "<div class='space-y-2'><p>1. West of road = <strong>Blue Tent</strong>.</p></div>"
            },
            {
                "question": "Which tent is positioned closest to the freshwater lake on the campsite map?",
                "options": ["Blue tent", "Green tent", "Purple tent", "Yellow tent"],
                "answer": 1,
                "explanation": "The green tent is located closest to the lake edge.",
                "hint": "Check the clue: closest to the lake.",
                "solution_html": "<div class='space-y-2'><p>1. Closest to lake = <strong>Green Tent</strong>.</p></div>"
            },
            {
                "question": "Where is the purple tent situated relative to the green tent?",
                "options": ["Directly South", "Directly North", "Directly East", "Directly West"],
                "answer": 1,
                "explanation": "The clue specifies: 'The tent directly north of the green tent is purple.'",
                "hint": "Look northward (upward) from the green tent.",
                "solution_html": "<div class='space-y-2'><p>1. North of green tent = <strong>Purple Tent</strong>.</p></div>"
            },
            {
                "question": "If park rangers ask you to draw a new tent to the EAST of the lake, where should you draw it?",
                "options": [
                    "Above the lake (North)",
                    "Below the lake (South)",
                    "To the right of the lake (East)",
                    "To the left of the lake (West)"
                ],
                "answer": 2,
                "explanation": "East is to the right on a standard map layout.",
                "hint": "East is always to the right side on paper.",
                "solution_html": "<div class='space-y-2'><p>1. East on a map = <strong>To the right</strong>.</p></div>"
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Room Layouts, Relative Perspectives & Shortest Street Paths",
        "lecture": "",
        "questions": [
            {
                "question": "Standing at the center of a room facing North (window), which wall has the entry door?",
                "options": ["Northern wall", "Southern wall", "Eastern wall", "Western wall"],
                "answer": 1,
                "explanation": "Directly behind an observer facing North is South, where the door is located.",
                "hint": "Behind is South.",
                "solution_html": "<div class='space-y-2'><p>1. Opposite of North = <strong>South</strong> (Door).</p></div>"
            },
            {
                "question": "Standing at the room center facing North, which furniture item is to your right (East)?",
                "options": ["Cupboard", "Bed", "Window", "Door"],
                "answer": 1,
                "explanation": "When facing North, your right hand points East toward the bed.",
                "hint": "Right hand is East when facing North.",
                "solution_html": "<div class='space-y-2'><p>1. Facing North ➔ Right hand points East (<strong>Bed</strong>).</p></div>"
            },
            {
                "question": "What is the key difference between cardinal directions and relative directions?",
                "options": [
                    "Cardinal directions change when a person turns, relative do not",
                    "Cardinal directions are fixed to Earth; relative directions change with body orientation",
                    "There is no difference between them",
                    "Relative directions only exist in space"
                ],
                "answer": 1,
                "explanation": "Cardinal directions (N, S, E, W) are permanently fixed; relative directions (left, right, front, back) depend on heading.",
                "hint": "The North Pole does not rotate when you turn.",
                "solution_html": "<div class='space-y-2'><p>1. Cardinal directions are <strong>fixed to Earth</strong>.</p><p>2. Relative directions change with observer heading.</p></div>"
            },
            {
                "question": "If you are walking South and make a 90° right turn, which direction are you now walking?",
                "options": ["East", "West", "North", "South-East"],
                "answer": 1,
                "explanation": "Facing South, your right hand points toward West.",
                "hint": "Imagine facing downward on a map; your right side is to the left (West).",
                "solution_html": "<div class='space-y-2'><p>1. Facing South ➔ Right turn = <strong>West</strong>.</p></div>"
            },
            {
                "question": "A school bus traveling East makes a 90° left turn. Which direction is it now heading?",
                "options": ["North", "South", "East", "West"],
                "answer": 0,
                "explanation": "From East (heading right), a left turn points upward toward North.",
                "hint": "Left turn from East points towards the top of the map.",
                "solution_html": "<div class='space-y-2'><p>1. East ➔ Left turn = <strong>North</strong>.</p></div>"
            },
            {
                "question": "If a bus travels 2 blocks East, 3 blocks North, and then 2 blocks South, what is its vertical distance from the start?",
                "options": ["1 block North", "5 blocks North", "1 block South", "0 blocks"],
                "answer": 0,
                "explanation": "3 blocks North minus 2 blocks South = 1 block North.",
                "hint": "3 - 2 = 1 block North.",
                "solution_html": "<div class='space-y-2'><p>1. 3 North − 2 South = <strong>1 block North</strong>.</p></div>"
            },
            {
                "question": "On a city grid, what is the shortest walking distance between two points differing by 3 blocks East and 4 blocks North?",
                "options": ["5 blocks", "7 blocks", "12 blocks", "1 block"],
                "answer": 1,
                "explanation": "On a grid without diagonals, distance = horizontal blocks + vertical blocks = 3 + 4 = 7 blocks.",
                "hint": "Add the East and North blocks together.",
                "solution_html": "<div class='space-y-2'><p>1. Grid distance = 3 + 4 = <strong>7 blocks</strong>.</p></div>"
            },
            {
                "question": "A zig-zag path walks 1E + 1N + 1E + 2N + 1E + 1N without backtracking. What is its total distance?",
                "options": ["5 blocks", "6 blocks", "7 blocks", "8 blocks"],
                "answer": 2,
                "explanation": "Total East = 1 + 1 + 1 = 3; Total North = 1 + 2 + 1 = 4. Total distance = 3 + 4 = 7 blocks.",
                "hint": "Sum all individual segments.",
                "solution_html": "<div class='space-y-2'><p>1. Sum of segments = 1+1+1+2+1+1 = <strong>7 blocks</strong>.</p></div>"
            },
            {
                "question": "Why does a route with backtracking take longer than a direct non-backtracking route on a grid?",
                "options": [
                    "Because roads get narrower",
                    "Because moving backwards requires walking extra blocks to make up the lost distance",
                    "Because traffic lights turn red",
                    "Because compasses stop working"
                ],
                "answer": 1,
                "explanation": "Every block walked backwards requires another block forward to undo the detour, adding distance.",
                "hint": "Backtracking adds double the detour distance.",
                "solution_html": "<div class='space-y-2'><p>1. Backtracking wastes travel by moving away from the goal.</p></div>"
            },
            {
                "question": "What is the mathematical term for distance measured strictly along horizontal and vertical grid lines?",
                "options": ["Diagonal distance", "Circular distance", "Manhattan grid distance", "Curved distance"],
                "answer": 2,
                "explanation": "Manhattan (or taxicab) grid distance measures path lengths along perpendicular street axes.",
                "hint": "Named after the grid street layout of Manhattan.",
                "solution_html": "<div class='space-y-2'><p>1. Grid street distance = <strong>Manhattan grid distance</strong>.</p></div>"
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • Metro Rail Networks, Route Optimization & Campus Mapping",
        "questions": [
            {
                "question": "Why do transit maps (like the Delhi Metro map) use simplified straight lines instead of true road curves?",
                "options": [
                    "To save ink",
                    "To make lines, stations, and transfer junctions clear and easy to read at a glance",
                    "Because trains cannot turn",
                    "Because stations are only in straight lines"
                ],
                "answer": 1,
                "explanation": "Schematic transit maps prioritize rapid visual clarity for commuters over geographical terrain realism.",
                "hint": "Commuters need to see lines and stops clearly.",
                "solution_html": "<div class='space-y-2'><p>1. Schematic maps maximize <strong>clarity and readability</strong>.</p></div>"
            },
            {
                "question": "What does a double-circle or interlocking ring symbol represent on a transit rail map?",
                "options": [
                    "A railway bridge",
                    "An interchange station where passengers can switch lines",
                    "An emergency exit",
                    "A ticket counter"
                ],
                "answer": 1,
                "explanation": "Double circles designate interchange stations connecting two or more transit lines.",
                "hint": "Where lines meet and passengers transfer.",
                "solution_html": "<div class='space-y-2'><p>1. Interlocking rings = <strong>Interchange station</strong>.</p></div>"
            },
            {
                "question": "At which major interchange hub can a passenger transfer directly between the Yellow Line and Blue Line in Delhi?",
                "options": ["Rajiv Chowk", "Hauz Khas", "Kashmere Gate", "Botanical Garden"],
                "answer": 0,
                "explanation": "Rajiv Chowk is the premier central interchange between the Yellow Line and Blue Line.",
                "hint": "The central crossroads of Connaught Place.",
                "solution_html": "<div class='space-y-2'><p>1. Yellow & Blue line transfer = <strong>Rajiv Chowk</strong>.</p></div>"
            },
            {
                "question": "When comparing two transit routes, what is a primary advantage of having fewer line transfers?",
                "options": [
                    "Trains travel at double speed",
                    "Less walking between platforms and shorter waiting times",
                    "The train tickets become free",
                    "You get extra seats"
                ],
                "answer": 1,
                "explanation": "Each transfer involves walking corridors, staircases, and waiting for the next train, so fewer transfers save time.",
                "hint": "Transferring lines takes time and physical effort.",
                "solution_html": "<div class='space-y-2'><p>1. Fewer transfers = <strong>Less walking and less waiting time</strong>.</p></div>"
            },
            {
                "question": "What is the primary function of a map key or legend on a campus map?",
                "options": [
                    "To unlock the school gates",
                    "To explain the meaning of symbols, icons, and colors used across the map",
                    "To tell the current time",
                    "To list student grades"
                ],
                "answer": 1,
                "explanation": "A map key explains what each symbol, boundary, and icon represents.",
                "hint": "A legend translates symbols into real-world meanings.",
                "solution_html": "<div class='space-y-2'><p>1. A map key <strong>explains the meaning of symbols</strong>.</p></div>"
            },
            {
                "question": "On the standardized school map, what geometric symbol represents the main school building?",
                "options": ["A tree canopy", "A solid rectangle", "A double circle", "A wavy line"],
                "answer": 1,
                "explanation": "Solid rectangles represent architectural buildings on standard campus maps.",
                "hint": "A rectangular block represents the building.",
                "solution_html": "<div class='space-y-2'><p>1. School building = <strong>Solid rectangle</strong>.</p></div>"
            },
            {
                "question": "What icon is used in the campus map legend to indicate the drinking water tank?",
                "options": ["A garden flower", "A water tank / circle with plumbing cross", "A bench symbol", "A fence line"],
                "answer": 1,
                "explanation": "Water tanks are represented by a distinctive tank or tap symbol.",
                "hint": "Look for the water plumbing marker.",
                "solution_html": "<div class='space-y-2'><p>1. Drinking water tank = <strong>Water tank icon</strong>.</p></div>"
            },
            {
                "question": "What three elements are essential to define a step in a treasure hunt navigation clue?",
                "options": [
                    "Origin point, cardinal direction, and distance/pace count",
                    "Color of clothes, temperature, and pencil length",
                    "Student name, shoe size, and lunch menu",
                    "Day of the week, school bell, and book weight"
                ],
                "answer": 0,
                "explanation": "Every navigation instruction needs where you start, which direction to walk, and how far to go.",
                "hint": "Start point, heading, and distance.",
                "solution_html": "<div class='space-y-2'><p>1. Essential triad: <strong>Origin, Direction, and Distance</strong>.</p></div>"
            },
            {
                "question": "If you are at the Water Tank and walk 25 paces West, which way are you moving on the map?",
                "options": ["Upward (North)", "Downward (South)", "To the right (East)", "To the left (West)"],
                "answer": 3,
                "explanation": "West is to the left on a standard map layout.",
                "hint": "West is always to the left.",
                "solution_html": "<div class='space-y-2'><p>1. West = <strong>To the left</strong>.</p></div>"
            },
            {
                "question": "Why is a compass rose with North marked at the top placed on school maps?",
                "options": [
                    "For decoration only",
                    "To establish fixed cardinal orientation for all readers",
                    "To show where the wind blows",
                    "To show where the sun sets"
                ],
                "answer": 1,
                "explanation": "The compass rose ensures all readers interpret directions consistently regardless of how they hold the map.",
                "hint": "Orientation reference for all viewers.",
                "solution_html": "<div class='space-y-2'><p>1. Compass rose establishes <strong>fixed cardinal orientation</strong>.</p></div>"
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Anthill Grids, Coordinate Geometry & Zoo Animal Plotting",
        "questions": [
            {
                "question": "An ant starts at origin (0, 0) and crawls 2 cm East and 3 cm North. How many total cm did it crawl?",
                "options": ["4 cm", "5 cm", "6 cm", "1 cm"],
                "answer": 1,
                "explanation": "2 cm East + 3 cm North = 5 cm total path length.",
                "hint": "Add 2 and 3.",
                "solution_html": "<div class='space-y-2'><p>1. Distance = 2 + 3 = <strong>5 cm</strong>.</p></div>"
            },
            {
                "question": "What is the coordinate pair of a laddoo located 2 cm East and 3 cm North of origin (0, 0)?",
                "options": ["(3, 2)", "(2, 3)", "(5, 0)", "(0, 5)"],
                "answer": 1,
                "explanation": "East is x = 2 and North is y = 3, giving coordinate pair (2, 3).",
                "hint": "Horizontal x first, vertical y second.",
                "solution_html": "<div class='space-y-2'><p>1. x = 2, y = 3 ➔ <strong>(2, 3)</strong>.</p></div>"
            },
            {
                "question": "From the laddoo at (2, 3), which movement reaches sugar crystals located at (6, 5)?",
                "options": [
                    "4 cm East and 2 cm North",
                    "2 cm West and 4 cm South",
                    "6 cm East and 5 cm North",
                    "3 cm North and 2 cm East"
                ],
                "answer": 0,
                "explanation": "East change = 6 - 2 = 4 cm; North change = 5 - 3 = 2 cm.",
                "hint": "Subtract starting coordinates from target coordinates.",
                "solution_html": "<div class='space-y-2'><p>1. Δx = 6 − 2 = 4 cm East.</p><p>2. Δy = 5 − 3 = 2 cm North.</p></div>"
            },
            {
                "question": "What is the shortest grid distance from origin (0, 0) to bread located at coordinate (5, 4)?",
                "options": ["7 cm", "9 cm", "11 cm", "20 cm"],
                "answer": 1,
                "explanation": "Distance = 5 cm East + 4 cm North = 9 cm.",
                "hint": "Add 5 and 4.",
                "solution_html": "<div class='space-y-2'><p>1. Shortest grid distance = 5 + 4 = <strong>9 cm</strong>.</p></div>"
            },
            {
                "question": "Why did Path C (3E + 2N + 2W + 2N + 4E = 13 cm) take 4 cm longer than the optimal 9 cm path?",
                "options": [
                    "Because crawling 2 cm West required an extra 2 cm East to reach x = 5 (2 + 2 = 4 cm wasted)",
                    "Because the grid squares expanded",
                    "Because the bread moved",
                    "Because the ant took a lunch break"
                ],
                "answer": 0,
                "explanation": "Crawling 2 cm West moved away from the target, requiring an additional 2 cm East to recover the lost distance.",
                "hint": "2 cm backwards + 2 cm to make up for it = 4 cm wasted.",
                "solution_html": "<div class='space-y-2'><p>1. Backtracking 2 cm West adds 2 + 2 = <strong>4 cm extra travel</strong>.</p></div>"
            },
            {
                "question": "In the standard coordinate system (x, y), what is the universal rule for ordering movements?",
                "options": [
                    "Vertical y first, horizontal x second",
                    "Horizontal x (East along columns) first, vertical y (North along rows) second",
                    "Diagonal movement first",
                    "Random choice"
                ],
                "answer": 1,
                "explanation": "Standard convention always places horizontal x-coordinate first and vertical y-coordinate second: (x, y).",
                "hint": "x before y in the alphabet, horizontal before vertical.",
                "solution_html": "<div class='space-y-2'><p>1. Universal rule: <strong>Horizontal x first, Vertical y second</strong>.</p></div>"
            },
            {
                "question": "Why is coordinate (4, 1) completely different from coordinate (1, 4)?",
                "options": [
                    "They are the same location",
                    "(4, 1) is 4 units East and 1 North; (1, 4) is 1 unit East and 4 North",
                    "(4, 1) does not exist on a grid",
                    "Only (1, 4) is a valid coordinate"
                ],
                "answer": 1,
                "explanation": "The order of coordinates matters: (4, 1) has x=4, y=1; while (1, 4) has x=1, y=4.",
                "hint": "Order matters in ordered pairs.",
                "solution_html": "<div class='space-y-2'><p>1. (4, 1) = 4 East, 1 North.</p><p>2. (1, 4) = 1 East, 4 North (different locations!).</p></div>"
            },
            {
                "question": "On the 12x12 zoo grid, which animal enclosure is located at coordinate (1, 1)?",
                "options": ["Giant Panda", "Lion", "Asian Elephant", "Saltwater Crocodile"],
                "answer": 0,
                "explanation": "The Giant Panda is located at coordinate (1, 1).",
                "hint": "Bottom-left enclosure near entrance.",
                "solution_html": "<div class='space-y-2'><p>1. (1, 1) = <strong>Giant Panda</strong>.</p></div>"
            },
            {
                "question": "On the zoo grid, which animal enclosure is located at coordinate (4, 1)?",
                "options": ["Giant Panda", "Giant Tortoise", "Spotted Deer", "Asian Elephant"],
                "answer": 1,
                "explanation": "At x = 4, y = 1 lies the Giant Tortoise enclosure.",
                "hint": "4 units East and 1 unit North.",
                "solution_html": "<div class='space-y-2'><p>1. (4, 1) = <strong>Giant Tortoise</strong>.</p></div>"
            },
            {
                "question": "What are the exact coordinates of the Asian Elephant enclosure near the top-right sanctuary border?",
                "options": ["(1, 1)", "(7, 6)", "(3, 10)", "(11, 11)"],
                "answer": 3,
                "explanation": "The Asian Elephant enclosure is located at column 11, row 11, written as (11, 11).",
                "hint": "Both horizontal and vertical coordinates are 11.",
                "solution_html": "<div class='space-y-2'><p>1. Top-right elephant enclosure = <strong>(11, 11)</strong>.</p></div>"
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part3:
        print(f"Slide {s['id']} ({s['title']}): {len(s['questions'])} questions")

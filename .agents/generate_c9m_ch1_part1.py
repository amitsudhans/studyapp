#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 1: Orienting Yourself: The Use of Coordinates
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 1.1 Introduction, 1.2 Settling In, and 1.3 The 2-D Cartesian Coordinate System
with 1-3 word headings, 195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Ancient Grid Roots",
        "subtitle": "Section 1.1 Introduction: Sindhu-Sarasvatī Urban Planning (~10 m Grid Streets) & Baudhāyana's Orthogonal Constructions",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter One: Orienting Yourself, The Use of Coordinates! "
            "Whenever you guide a friend to a specific house, track an airplane on radar, or place a button cleanly on a digital screen, you rely on a shared system of numbers that locks down exact position. "
            "In Section One Point One, trace this coordinate thinking back thousands of years to ancient India! "
            "Archaeological excavations across cities of the Sindhu-Sarasvatī Civilisation—such as Mohenjo-daro, Kalibangan, and Dholavira—reveal remarkably planned street networks laid out on perpendicular north-south and east-west grids! "
            "Major avenues roughly ten metres wide met side lanes cleanly at right angles, dividing residential neighbourhoods into neat rectangular blocks so any courtyard or granary could be located by avenue and cross-street! "
            "Around eight hundred BCE, Baudhāyana recorded systematic geometric constructions in the Śulba-Sūtras using taut cords and wooden pegs along an east-west central spine called the prācī line. "
            "By generating exact perpendiculars with measured cord ratios, builders oriented altars, bricks, and gateways with mathematical precision. "
            "Grid streets and orthogonal reference lines prove that coordinate orientation began as practical geometry long before modern graph paper existed! Every planned avenue and cross-lane acted like a living pair of coordinates guiding daily civic life."
        ),
        "checkpoints": [
            {
                "question": "What key geometric layout characterized cities of the Sindhu-Sarasvatī Civilisation?",
                "options": [
                    "Perpendicular north-south and east-west grid streets dividing neighbourhoods into rectangular blocks",
                    "Random winding footpaths radiating from a single circular well",
                    "Curved spiral alleys with no right-angle intersections",
                    "Single-line ribbon villages without cross-streets"
                ],
                "answer": 0,
                "hint": "Think about how orthogonal (~10 m wide) main roads intersected side streets in planned Harappan cities!",
                "explanation": "Excavations show perpendicular north-south and east-west avenues (~10 m wide) intersecting at right angles to organize urban blocks cleanly."
            },
            {
                "question": "How did Baudhāyana's Śulba-Sūtras orient geometric constructions accurately on flat ground?",
                "options": [
                    "Using taut cords and pegs along a reference axis to construct exact perpendiculars",
                    "Estimating angles visually without ropes or measurements",
                    "Using magnetic compasses attached to floating bowls",
                    "Plotting ordered pairs directly on printed coordinate graph paper"
                ],
                "answer": 0,
                "hint": "Recall the rope-stretcher ('śulba') method anchored to an east-west spine!",
                "explanation": "Baudhāyana used stretched cords (śulba) and pegs to lay down a central reference line and construct exact orthogonal (90-degree) lines."
            }
        ]
    },
    {
        "id": 2,
        "title": "Ujjayini Prime Meridian",
        "subtitle": "Section 1.1 Introduction: Ujjayinī as the Central Zero-Longitude Meridian in Ancient Indian Astronomy",
        "speech": (
            "Now move from street grids on earth to mapping cities and stars across continents! "
            "When ancient scholars measured locations across a wide kingdom or tracked celestial motions overhead, they needed a universally agreed zero line from which east and west distances could be counted consistently. "
            "In ancient Indian mathematical astronomy, the historic city of Ujjayinī served for centuries as the central zero-longitude prime meridian! "
            "Astronomical treatises—the Siddhāntas—treated the north-south meridian line passing directly through Ujjayinī as longitude zero, extending from the equator through Lanka and Ujjayinī toward the northern pole. "
            "By measuring how far east or west a town lay from the Ujjayinī meridian, and combining that measure with its northward latitude determined from solar shadow lengths at equinox or the Pole Star's altitude, scholars assigned each city a clear pair of directional numbers! "
            "Why does choosing a central meridian matter so deeply? Because without an agreed origin line, two observers measuring from different towns would publish conflicting numbers for the exact same location! "
            "Ujjayinī established a shared zero reference long before modern Greenwich longitude, demonstrating the power of a common origin line! Once every astronomer measured east or west from that single city, eclipses, calendars, and terrestrial maps aligned across kingdoms."
        ),
        "checkpoints": [
            {
                "question": "What role did the ancient city of Ujjayinī play in classical Indian astronomy and geography?",
                "options": [
                    "It served as the central zero-longitude prime meridian reference line",
                    "It served only as a coastal port with no astronomical significance",
                    "It marked the southernmost point of the Earth's equator",
                    "It replaced latitude completely so only one number was needed"
                ],
                "answer": 0,
                "hint": "Recall which meridian Indian Siddhānta astronomers chose as longitude 0°!",
                "explanation": "Indian astronomical texts treated the north-south line passing through Ujjayinī as the zero-longitude prime meridian for measuring east-west positions."
            },
            {
                "question": "Why must any coordinate system agree upon a fixed reference origin or prime meridian?",
                "options": [
                    "So different observers assign the exact same coordinates to the same position",
                    "Because Earth stops rotating along the prime meridian",
                    "To eliminate the need for north-south measurements",
                    "So positive and negative numbers always stay equal"
                ],
                "answer": 0,
                "hint": "Think about what happens if two mapmakers measure east-west distance from two different starting cities!",
                "explanation": "A shared zero reference guarantees consistency so every observer calculates unambiguous coordinates for identical points."
            }
        ]
    },
    {
        "id": 3,
        "title": "Global Coordinate Pioneers",
        "subtitle": "Section 1.1 Global Mathematical Contributions: Hipparchus, Ptolemy, Āryabhaṭa, Al-Bīrūnī & Omar Khayyām",
        "speech": (
            "Coordinate geometry grew through centuries of shared discovery across civilisations! "
            "Let us trace key global contributors who turned sky-watching and geometry into numerical coordinates. "
            "In the second century BCE, Greek astronomer Hipparchus pioneered organizing stars and terrestrial places using systematic grids of latitude and longitude angles. "
            "Later, around one hundred fifty CE, Ptolemy compiled his monumental Geographia, tabulating thousands of cities by latitude and longitude coordinates on gridded world maps! "
            "In fifth-century India, Āryabhaṭa revolutionized mathematical astronomy in the Āryabhaṭīya, calculating celestial coordinates using sine tables, spherical projections, and precise planetary positions anchored to Earth's rotation and reference meridians. "
            "Around the eleventh century, polymath Al-Bīrūnī refined geographical coordinate determinations across Central Asia and India, famously measuring Earth's radius from mountain elevation angles and coordinating cities between Ghazni and Nandana! "
            "Meanwhile, mathematician Omar Khayyām geometrically solved cubic equations by intersecting curves such as parabolas and circles along orthogonal reference lines, bridging algebra and geometry! "
            "Notice how every single mathematical advance—from Hipparchus and Ptolemy's star charts to Āryabhaṭa's trigonometry, Al-Bīrūnī's geodesy, and Khayyām's intersecting curves—moved human inquiry steadily closer to describing geometric shapes, celestial orbits, and terrestrial locations effortlessly with ordered pairs of signed numbers across ancient world cultures!"
        ),
        "checkpoints": [
            {
                "question": "Which scholar compiled extensive geographical tables assigning latitude and longitude coordinates to cities in Geographia?",
                "options": [
                    "Ptolemy (building on Hipparchus's grid concepts)",
                    "René Descartes in 1637",
                    "Baudhāyana in 800 BCE",
                    "Brahmagupta in 628 CE"
                ],
                "answer": 0,
                "hint": "Recall the second-century CE author of the world atlas 'Geographia'!",
                "explanation": "Ptolemy extended Hipparchus's angular grid ideas into Geographia, systematically listing places with latitude and longitude."
            },
            {
                "question": "How did Omar Khayyām connect algebra with geometric reference lines?",
                "options": [
                    "By solving cubic equations as intersections of geometric curves like parabolas and circles",
                    "By outlawing negative distances on number lines",
                    "By inventing modern digital pixels",
                    "By restricting geometry strictly to positive integers"
                ],
                "answer": 0,
                "hint": "Think about finding roots of equations through intersecting curves!",
                "explanation": "Omar Khayyām represented algebraic equations geometrically, locating solutions where conic curves intersected."
            }
        ]
    },
    {
        "id": 4,
        "title": "Brahmagupta to Descartes",
        "subtitle": "Section 1.1 Formalizing Zero, Negative Numbers (Brahmagupta) & the 2D Cartesian Plane (Fermat & Descartes)",
        "speech": (
            "A crucial mathematical bridge was still missing before a complete four-quadrant coordinate plane could exist: formal rules for zero and negative numbers! "
            "Early Greek geometry measured only positive lengths, keeping coordinate thinking trapped in a single region. "
            "In six hundred twenty-eight CE, Indian mathematician Brahmagupta transformed mathematics in his Brāhmasphuṭasiddhānta by treating zero as an operational number alongside explicit arithmetic rules for negative numbers—which he described as debts versus fortunes! "
            "Once zero marked a true origin point and negative numbers extended seamlessly left and downward on number lines, all four quadrants became mathematically possible! "
            "Centuries later in seventeenth-century France, Pierre de Fermat and René Descartes independently unified algebra and geometry into one analytic language! "
            "Descartes—after whom the Cartesian system is named—introduced two intersecting perpendicular number lines meeting at zero, allowing any point in the flat plane to be encoded uniquely as an ordered number pair, and any geometric curve to become an algebraic equation! "
            "Imagine turning geometric circles, straight lines, and triangles into clean algebraic equations you can solve systematically with signed numbers! "
            "Thus Brahmagupta's pioneering arithmetic of zero and negatives combined directly with Fermat and Descartes's perpendicular intersecting axes to create our modern Cartesian coordinate system!"
        ),
        "checkpoints": [
            {
                "question": "Why was Brahmagupta's formalization of zero and negative numbers essential for the full Cartesian coordinate plane?",
                "options": [
                    "It allowed coordinate axes to extend seamlessly on both sides of the origin (0, 0) into all four quadrants",
                    "It restricted all geometric points to Quadrant I only",
                    "It removed the vertical y-axis completely",
                    "It turned curved circles into straight lines"
                ],
                "answer": 0,
                "hint": "How could you write coordinates like (-3, -4) without zero and negative number arithmetic?",
                "explanation": "Brahmagupta's rules for zero and negative numbers established signed directions on axes, making Quadrants II, III, and IV possible."
            },
            {
                "question": "Which two seventeenth-century French mathematicians independently developed algebraic coordinate geometry on perpendicular axes?",
                "options": [
                    "Pierre de Fermat and René Descartes",
                    "Hipparchus and Ptolemy",
                    "Baudhāyana and Āryabhaṭa",
                    "Al-Bīrūnī and Omar Khayyām"
                ],
                "answer": 0,
                "hint": "One of them gave his Latinized name ('Cartesius') to the 'Cartesian' plane!",
                "explanation": "Fermat and René Descartes independently connected algebraic equations with points and curves on perpendicular coordinate axes."
            }
        ]
    },
    {
        "id": 5,
        "title": "Tactile Home Map",
        "subtitle": "Section 1.2 Settling In: Navigating a New Home Layout via Tactile Pin-and-Thread Grids (Scale 1 cm : 1 foot)",
        "speech": (
            "Now explore Section One Point Two: Settling In, where coordinate geometry solves a deeply practical everyday challenge! "
            "Imagine two siblings moving into an unfamiliar new house together: one sibling is visually impaired and needs to memorize the exact layout of rooms, doors, bedrooms, bathrooms, and wardrobes safely and independently. "
            "Rather than relying only on vague spoken phrases like 'somewhere near the back wall', the guiding sibling builds a raised tactile coordinate map on a sturdy board! "
            "Pins mark key corners along a crisp rectangular grid, and stretched threads form evenly spaced horizontal and vertical reference lines that fingertips can trace effortlessly! "
            "They pick a crystal-clear scale: one centimetre on the tactile pin-and-thread board equals exactly one foot inside the actual house! "
            "Using the bottom-left corner of the floor plan as zero-zero, every doorway, wardrobe edge, bathroom corner, and bedroom centre receives two exact numbers measured eastward along the bottom edge and northward along the side edge! "
            "With fingertips reading the tactile thread intersections, the visually impaired learner builds a complete, accurate mental blueprint of the entire home! Notice how the scale one centimetre per foot transforms abstract grid counts straight into exact walking steps across every single room!"
        ),
        "checkpoints": [
            {
                "question": "On a tactile pin-and-thread home map using a scale of 1 cm : 1 foot, if a bedroom is 12 cm wide and 10 cm long on the board, what are its actual room dimensions?",
                "options": [
                    "12 feet wide by 10 feet long",
                    "1.2 feet wide by 1.0 foot long",
                    "120 feet wide by 100 feet long",
                    "24 feet wide by 20 feet long"
                ],
                "answer": 0,
                "hint": "Each 1 cm step on the tactile thread grid represents exactly 1 foot in the real room!",
                "explanation": "At a 1 cm : 1 foot scale, multiplying board centimetres by 1 gives actual feet: 12 cm → 12 ft and 10 cm → 10 ft."
            },
            {
                "question": "Why does a rectangular pin-and-thread grid help a visually impaired learner orient inside a new home?",
                "options": [
                    "Stretched threads and pins convert spatial layouts into touchable horizontal and vertical coordinates",
                    "It hides doorways and wardrobes so rooms feel smaller",
                    "It replaces scale ratios with random unmeasured knots",
                    "It works only outdoors and cannot model floor plans"
                ],
                "answer": 0,
                "hint": "Think about tracing two perpendicular directions with fingertips from a corner reference!",
                "explanation": "Tactile grids allow fingertips to count evenly spaced horizontal and vertical threads to locate rooms, doors, and furniture accurately."
            }
        ]
    },
    {
        "id": 6,
        "title": "Axes and Origin",
        "subtitle": "Section 1.3 The 2-D Cartesian Coordinate System: Horizontal x-axis, Vertical y-axis, Origin O(0,0) & Ordered Pair (x,y)",
        "speech": (
            "Let us formalize the tactile grid into Section One Point Three: The Two-D Cartesian Coordinate System! "
            "Take two mutually perpendicular number lines intersecting right at their zero marks. "
            "The horizontal line X'OX is called the x-axis: moving right of zero gives positive x values, while moving left gives negative x values. "
            "The vertical line Y'OY is called the y-axis: moving upward from zero gives positive y values, while moving downward gives negative y values. "
            "Their unique intersection point O is called the Origin, having coordinates zero comma zero! "
            "Together, both axes form the Cartesian coordinate plane. "
            "To specify any point P in this plane, we write an ordered pair inside parentheses as open-parenthesis x comma y close-parenthesis! "
            "Always read the order strictly from left to right: the FIRST number x—called the abscissa—tells how far right or left to travel from the origin parallel to the x-axis. "
            "The SECOND number y—called the ordinate—tells how far up or down to travel parallel to the y-axis. "
            "Because order controls position strictly, ordered pair three comma five lands in a completely different spot than five comma three! "
            "Practice sliding the interactive horizontal and vertical guides below to watch each ordered pair snap cleanly onto its exact grid intersection!"
        ),
        "checkpoints": [
            {
                "question": "In the 2-D Cartesian plane, what are the coordinates of the Origin O where the x-axis and y-axis intersect?",
                "options": [
                    "(0, 0)",
                    "(1, 1)",
                    "(0, 1)",
                    "(1, 0)"
                ],
                "answer": 0,
                "hint": "Both perpendicular number lines cross directly at their zero marks!",
                "explanation": "The Origin O is the intersection of the zero mark of the x-axis and the zero mark of the y-axis, so its coordinates are (0, 0)."
            },
            {
                "question": "To plot the ordered pair P(4, -3) starting from the Origin O(0, 0), how do you move?",
                "options": [
                    "4 units right along the x-axis, then 3 units down parallel to the y-axis",
                    "4 units up along the y-axis, then 3 units left parallel to the x-axis",
                    "3 units right along the x-axis, then 4 units down parallel to the y-axis",
                    "4 units left along the x-axis, then 3 units up parallel to the y-axis"
                ],
                "answer": 0,
                "hint": "First coordinate x = +4 (horizontal), second coordinate y = -3 (vertical)!",
                "explanation": "Since x = +4 (right 4 units) and y = -3 (down 3 units), P(4, -3) sits 4 units right and 3 units below the Origin."
            }
        ]
    },
    {
        "id": 7,
        "title": "The Four Quadrants",
        "subtitle": "Section 1.3 Quadrants & Signs: Quadrant I (+,+), Quadrant II (-,+), Quadrant III (-,-), Quadrant IV (+,-) & Axis Points",
        "speech": (
            "Look closely at how the perpendicular x-axis and y-axis slice the entire flat plane into four open regions called Quadrants! "
            "By universal mathematical convention, we number the four quadrants counter-clockwise starting from the upper-right region! "
            "In Quadrant One, both x and y are positive, written plus comma plus—for example, point two comma four. "
            "Stepping left across the y-axis enters Quadrant Two, where x is negative and y is positive, written minus comma plus—such as negative three comma five. "
            "Dropping below the x-axis enters Quadrant Three, where both x and y are negative, written minus comma minus—such as negative four comma negative two. "
            "Finally, crossing right back over the y-axis enters Quadrant Four, where x is positive and y is negative, written plus comma minus—such as six comma negative one. "
            "Wait—what about points sitting directly ON an axis, like five comma zero or zero comma negative three? "
            "Crucial coordinate rule: points with zero as either coordinate lie directly ON the horizontal x-axis or vertical y-axis, NOT inside any open quadrant! Checking the plus and minus signs immediately reveals every point's exact quadrant home or axis boundary—practice identifying all four signed regions and axis boundaries in the interactive explorer below!"
        ),
        "checkpoints": [
            {
                "question": "In which quadrant does the point (-7, -2) lie?",
                "options": [
                    "Quadrant III, because both x < 0 and y < 0 (-, -)",
                    "Quadrant II, because x < 0 and y > 0 (-, +)",
                    "Quadrant IV, because x > 0 and y < 0 (+, -)",
                    "On the x-axis"
                ],
                "answer": 0,
                "hint": "Check the signs of x = -7 (left) and y = -2 (down)!",
                "explanation": "Points with negative x-coordinate and negative y-coordinate (-, -) lie in Quadrant III (bottom-left region)."
            },
            {
                "question": "Where does the point (0, -6) lie in the Cartesian plane?",
                "options": [
                    "On the negative y-axis (not inside any quadrant)",
                    "Inside Quadrant III",
                    "Inside Quadrant IV",
                    "On the positive x-axis"
                ],
                "answer": 0,
                "hint": "Since x = 0, there is zero horizontal displacement left or right from the vertical axis!",
                "explanation": "Every point of form (0, y) with y ≠ 0 lies directly on the y-axis; with y = -6 it lies 6 units below O on the negative y-axis."
            }
        ]
    },
    {
        "id": 8,
        "title": "Distance From Axes",
        "subtitle": "Section 1.3 Coordinate Rules: x = Distance from y-axis, y = Distance from x-axis & Symmetry Rule (x,y) = (y,x) ⇔ x = y",
        "speech": (
            "Now master the most common trap in Section One Point Three: perpendicular distances from the axes versus swaps of ordered pairs! "
            "Suppose a point P has coordinates five comma negative three. How far is P perpendicularly from the y-axis, and how far is it from the x-axis? "
            "Careful—never confuse the axis names! Moving horizontally from the vertical y-axis changes x, so the perpendicular distance of any point open-parenthesis x comma y close-parenthesis from the y-axis equals the absolute value of x! "
            "Similarly, moving vertically away from the horizontal x-axis changes y, so the perpendicular distance of P from the x-axis equals the absolute value of y! "
            "Wait: why absolute value? Because physical geometric distance is always non-negative! So negative five comma negative three sits five units away from the y-axis and three units away from the x-axis! "
            "Second golden rule: when do two reversed ordered pairs open-parenthesis x comma y close-parenthesis and open-parenthesis y comma x close-parenthesis represent the exact same point? "
            "Two ordered pairs are equal if and only if x equals y, meaning the point lies squarely on the diagonal mirror line y equals x! Otherwise, swapping coordinates reflects the point across that diagonal!"
        ),
        "checkpoints": [
            {
                "question": "What is the perpendicular distance of the point P(-4, 7) from the x-axis?",
                "options": [
                    "7 units (equal to |y|, the magnitude of its ordinate)",
                    "4 units (equal to |x|)",
                    "-4 units",
                    "11 units"
                ],
                "answer": 0,
                "hint": "Distance from the horizontal x-axis is vertical height, which is measured by |y|!",
                "explanation": "Moving vertically from the x-axis to (-4, 7) spans 7 units upward; hence perpendicular distance from the x-axis is |y| = 7 units."
            },
            {
                "question": "Under what exact condition does the ordered pair (x, y) equal (y, x)?",
                "options": [
                    "If and only if x = y",
                    "Always, for every pair of numbers x and y",
                    "Whenever x + y = 0",
                    "Only when x = 0 and y = 1"
                ],
                "answer": 0,
                "hint": "Two ordered pairs (a, b) and (c, d) match only when a = c and b = d!",
                "explanation": "Equality (x, y) = (y, x) requires first components to match (x = y) and second components to match (y = x), so x = y."
            }
        ]
    }
]

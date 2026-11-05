#!/usr/bin/env python3
"""
Generate Slides 9 to 16 data for NCERT Class 5 Mathematics - Chapter 3: Angles as Turns
"""

slides_9_to_16 = [
    {
        "id": 9,
        "heading": "Angles Around",
        "tagline": "Discovering Angles in Daily Objects, Structures, and Sports",
        "color": "from-teal-600 to-cyan-700",
        "badge": "Real-World Geometry",
        "audio_text": (
            "Angles are not confined to geometry textbooks; they structure the entire world around us! "
            "Consider two hardcover books stood on end to form an A-frame tent roof: the peak where the covers touch creates an acute or obtuse angle depending on how far apart the bases are spread. "
            "Look at the door to your room: when shut, the angle between the door and wall is zero; when opened slightly, it forms an acute angle; when swung perpendicular to the doorway, it locks into a crisp right angle; and when pushed wide against the wall, it swings through an obtuse angle! "
            "Your laptop screen can tilt from an acute angle when half-closed, to an upright right angle, to a reclining obtuse angle for comfortable reading. "
            "In sports, gymnasts and yoga practitioners showcase angles dynamically: a gymnast performing a side split opens their legs into an impressive 180-degree straight angle, while a high hurdle jump demands an acute angle between the torso and thighs. "
            "By identifying angles in our surroundings, we recognize how architects, engineers, and athletes master geometry every day."
        ),
        "theory_blocks": [
            {
                "title": "Hinges and Openings",
                "content": "Doors, windows, laptop screens, and book covers all pivot along a hinge vertex. Changing the opening width dynamically transitions the angle from acute to right to obtuse.",
                "icon": "🚪"
            },
            {
                "title": "Architectural Roof Trusses",
                "content": "Steep alpine roofs form sharp acute angles to shed snow, while wide residential carports and warehouse roofs form obtuse angles to cover maximum ground span.",
                "icon": "🏠"
            },
            {
                "title": "Athletic Angles in Gymnastics",
                "content": "Gymnastic floor routines, high kicks, and splits demonstrate human biomechanics as dynamic angle turns from acute tucks to straight 180° splits.",
                "icon": "🤸"
            }
        ],
        "checkpoints": [
            {
                "question": "When a room door is opened halfway so that it stands perpendicular to the doorframe, what angle does it form?",
                "options": [
                    "Right angle",
                    "Acute angle",
                    "Obtuse angle",
                    "Straight angle"
                ],
                "correct": 0,
                "feedback": "Correct! A door perpendicular to its frame forms a 1/4 turn, or right angle."
            },
            {
                "question": "What angle is formed between the legs of a gymnast performing a complete flat floor split?",
                "options": [
                    "Straight angle (180°)",
                    "Right angle (90°)",
                    "Acute angle (< 90°)",
                    "Full turn (360°)"
                ],
                "correct": 0,
                "feedback": "Spot on! In a full floor split, both legs stretch in opposite directions along a straight 180° line."
            }
        ]
    },
    {
        "id": 10,
        "heading": "Folded Tester",
        "tagline": "Building an 8-Part Circular Angle Measuring Tool",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Laboratory Craft 1",
        "audio_text": (
            "To measure angles accurately without an expensive protractor, we can construct our own precision angle-measuring tool using a circular sheet of tracing paper! "
            "Follow these simple steps from our textbook. "
            "First, cut out a neat circle of paper. Fold it exactly in half to create a semicircle: this fold line represents a 1/2 turn, or straight angle. "
            "Next, fold the semicircle in half once more: this creates a quarter-circle quadrant, representing a 1/4 turn, or right angle! "
            "Now fold this quadrant in half a third time: you divide the quarter turn into two equal halves. "
            "When you unfold the circle completely, the crease marks partition the whole circle into 8 identical wedges! "
            "Each individual wedge represents exactly 1/8 of a full turn. "
            "Because a full circle contains 360 degrees, each 1/8 turn equals 360 divided by 8, which is precisely 45 degrees. "
            "By placing this 8-part folded tester over any corner or shape, you can instantly test whether an angle is 1/8 turn, 1/4 turn, 3/8 turn, or a half turn!"
        ),
        "theory_blocks": [
            {
                "title": "3-Fold Construction Process",
                "content": "Fold 1: Circle in half = 2 halves (1/2 turn). Fold 2: Semicircle in half = 4 quarters (1/4 turn). Fold 3: Quadrant in half = 8 equal wedges (1/8 turn).",
                "icon": "✂️"
            },
            {
                "title": "The 1/8 Turn Unit",
                "content": "Each sector is 1/8 of a full turn (45°). Two 1/8 sectors combine to form a 1/4 turn right angle (2/8 = 1/4 = 90°).",
                "icon": "🍕"
            },
            {
                "title": "Practical Field Testing",
                "content": "Lay the tester flat on scissors, corners, drawings, or pattern blocks. Count the sectors spanned between the arms to read the angle directly.",
                "icon": "📐"
            }
        ],
        "checkpoints": [
            {
                "question": "How many equal sectors are created when a circular paper is folded in half three times?",
                "options": [
                    "8 equal sectors",
                    "4 equal sectors",
                    "6 equal sectors",
                    "16 equal sectors"
                ],
                "correct": 0,
                "feedback": "Correct! Each fold doubles the sections: 2, then 4, then 8 equal sectors."
            },
            {
                "question": "How many 1/8 sectors of the folded tester make up a right angle?",
                "options": [
                    "2 sectors (2/8 = 1/4)",
                    "1 sector (1/8)",
                    "3 sectors (3/8)",
                    "4 sectors (4/8)"
                ],
                "correct": 0,
                "feedback": "Spot on! Two 1/8 sectors equal 2/8 = 1/4 of a turn, which is a right angle (45° + 45° = 90°)."
            }
        ]
    },
    {
        "id": 11,
        "heading": "Six-Part Tester",
        "tagline": "Folding 6 Equal Sectors with an Attached Straw Pointer",
        "color": "from-violet-600 to-purple-700",
        "badge": "Laboratory Craft 2",
        "audio_text": (
            "Our textbook introduces a second ingenious angle tool: the six-part tester equipped with an attached straw pointer! "
            "To build this tool, we divide a circular disc into 6 equal sectors rather than 8. "
            "Each sector of a six-part tester represents 1/6 of a full turn. "
            "Since a full turn is 360 degrees, 360 divided by 6 gives exactly 60 degrees for each sector! "
            "Notice that two of these sectors combine to make 2/6, which simplifies to 1/3 of a full turn, or 120 degrees: a prominent obtuse angle found in regular hexagons. "
            "Three sectors make 3/6, which simplifies to 1/2 of a full turn: a straight angle of 180 degrees. "
            "By pushing a split pin through the centre and attaching a plastic drinking straw, you create a rotating pointer. "
            "You can align the baseline of the disc with one arm of any drawn figure, and spin the straw pointer until it aligns with the second arm. "
            "The numbered or colored sectors underneath immediately reveal the exact turn fraction: 1/6 turn, 2/6 turn, 3/6 turn, or more!"
        ),
        "theory_blocks": [
            {
                "title": "The 1/6 Turn Sector",
                "content": "Dividing the circle into 6 equal parts creates 1/6 turn sectors (60° each). This matches the interior angles of equilateral triangles.",
                "icon": "📐"
            },
            {
                "title": "Attached Straw Pointer",
                "content": "A split pin holds a movable straw pointer at the pivot. Turning the pointer lets students simulate dynamic angles and read sector counts.",
                "icon": "🥤"
            },
            {
                "title": "Fraction Reductions",
                "content": "1 sector = 1/6 turn (60°); 2 sectors = 2/6 = 1/3 turn (120°); 3 sectors = 3/6 = 1/2 turn (180°); 6 sectors = 6/6 = 1 full turn (360°).",
                "icon": "🔢"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the angle measure of each sector in a circular tester divided into 6 equal parts?",
                "options": [
                    "1/6 of a turn (60°)",
                    "1/4 of a turn (90°)",
                    "1/8 of a turn (45°)",
                    "1/2 of a turn (180°)"
                ],
                "correct": 0,
                "feedback": "Correct! 360° divided by 6 equals 60°, which is 1/6 of a full turn."
            },
            {
                "question": "How many sectors of the six-part tester combine to form a straight angle (1/2 turn)?",
                "options": [
                    "3 sectors (3/6 = 1/2)",
                    "2 sectors (2/6 = 1/3)",
                    "4 sectors (4/6 = 2/3)",
                    "6 sectors (6/6 = 1)"
                ],
                "correct": 0,
                "feedback": "Spot on! 3 sectors make 3/6, which simplifies to 1/2 of a full turn (3 × 60° = 180°)."
            }
        ]
    },
    {
        "id": 12,
        "heading": "Combining Turns",
        "tagline": "Adding and Subtracting Fractional Turn Angles",
        "color": "from-indigo-600 to-blue-700",
        "badge": "Fractional Turn Arithmetic",
        "audio_text": (
            "Just as we add and subtract numbers, turns can be combined sequentially to create larger or smaller angles! "
            "Suppose you perform a quarter turn, which is 1/4 of a turn, and then immediately turn an additional 1/8 of a turn in the same direction. "
            "How much total turning have you executed? "
            "Let us convert 1/4 into eighths: 1/4 is equivalent to 2/8. "
            "Now add: 2/8 plus 1/8 equals 3/8 of a full turn! "
            "Because 3/8 is greater than 2/8 (which is 1/4) but less than 4/8 (which is 1/2), a 3/8 turn produces an obtuse angle of 135 degrees. "
            "What if you perform a half turn, which is 1/2 or 4/8, and then turn back by 1/8 turn in the opposite direction? "
            "4/8 minus 1/8 leaves 3/8 turn remaining! "
            "Mastering the addition and subtraction of rotational fractions enables us to navigate complex courses, solve geometric riddles, and understand how compound gears operate in machinery."
        ),
        "theory_blocks": [
            {
                "title": "Adding Fractional Turns",
                "content": "To add turns, find a common denominator. Example: 1/4 turn + 1/8 turn = 2/8 + 1/8 = 3/8 turn (135° obtuse angle).",
                "icon": "➕"
            },
            {
                "title": "Subtracting Counter Turns",
                "content": "Turning in the opposite direction subtracts rotation. Example: 1/2 turn - 1/8 turn = 4/8 - 1/8 = 3/8 turn.",
                "icon": "➖"
            },
            {
                "title": "Equivalence Benchmarks",
                "content": "1/8 turn = 45°; 2/8 = 1/4 turn = 90°; 3/8 turn = 135°; 4/8 = 1/2 turn = 180°; 8/8 turn = 1 whole turn = 360°.",
                "icon": "🧭"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the total turn when you combine a 1/4 turn and a 1/8 turn in the same direction?",
                "options": [
                    "3/8 turn",
                    "2/8 turn",
                    "1/2 turn",
                    "5/8 turn"
                ],
                "correct": 0,
                "feedback": "Correct! 1/4 = 2/8, and 2/8 + 1/8 = 3/8 of a full turn (135°)."
            },
            {
                "question": "If you make a 1/2 turn and then turn backwards by 1/4 turn, what turn fraction remains?",
                "options": [
                    "1/4 turn",
                    "1/8 turn",
                    "3/8 turn",
                    "1/2 turn"
                ],
                "correct": 0,
                "feedback": "Spot on! 1/2 - 1/4 = 2/4 - 1/4 = 1/4 turn (a right angle)."
            }
        ]
    },
    {
        "id": 13,
        "heading": "Clock Turns",
        "tagline": "Tracking Minute-Hand Rotations Over 15, 30, 45, and 60 Minutes",
        "color": "from-amber-600 to-orange-700",
        "badge": "Time & Angle Rotations",
        "audio_text": (
            "A standard analogue clock dial is divided into 12 equal hour marks, making it a wonderful real-world angle calculator! "
            "A full hour consists of 60 minutes, during which the minute hand completes one whole turn of 360 degrees. "
            "Therefore, each single hour number represents 360 divided by 12, which is 30 degrees of rotation. "
            "When the minute hand advances by 15 minutes, it moves from 12 to 3. 15 minutes out of 60 minutes is 15/60, which simplifies to 1/4 of a turn: a 90-degree right angle! "
            "When it travels for 30 minutes, moving from 12 to 6, 30/60 equals 1/2 of a turn: a 180-degree straight angle. "
            "When it advances for 45 minutes, from 12 to 9, 45/60 simplifies to 3/4 of a turn, or 270 degrees. "
            "And what about a short 5-minute interval? 5 minutes is 5/60, which simplifies to 1/12 of a turn, or exactly 30 degrees. "
            "Every passing minute is a precise geometrical turn in action!"
        ),
        "theory_blocks": [
            {
                "title": "15 Minutes = 1/4 Turn",
                "content": "15 out of 60 minutes = 15/60 = 1/4 turn (90° right angle). The minute hand travels from 12 to 3.",
                "icon": "🕒"
            },
            {
                "title": "30 Minutes = 1/2 Turn",
                "content": "30 out of 60 minutes = 30/60 = 1/2 turn (180° straight angle). The minute hand travels from 12 to 6.",
                "icon": "🕕"
            },
            {
                "title": "45 Minutes = 3/4 Turn",
                "content": "45 out of 60 minutes = 45/60 = 3/4 turn (270° reflex angle). The minute hand travels from 12 to 9.",
                "icon": "🕘"
            }
        ],
        "checkpoints": [
            {
                "question": "What fraction of a turn does the minute hand make as it moves from 12 to 3?",
                "options": [
                    "1/4 turn (15 minutes)",
                    "1/2 turn (30 minutes)",
                    "3/4 turn (45 minutes)",
                    "1/12 turn (5 minutes)"
                ],
                "correct": 0,
                "feedback": "Correct! Moving from 12 to 3 is 15 minutes, which is 15/60 = 1/4 turn (90°)."
            },
            {
                "question": "How many degrees does the minute hand turn in 30 minutes?",
                "options": [
                    "180° (1/2 turn)",
                    "90° (1/4 turn)",
                    "270° (3/4 turn)",
                    "360° (1 full turn)"
                ],
                "correct": 0,
                "feedback": "Spot on! 30 minutes represents half the dial, which is 1/2 turn = 180°."
            }
        ]
    },
    {
        "id": 14,
        "heading": "Clockwise Motion",
        "tagline": "Following the Traditional Forward Path of Clock Hands",
        "color": "from-emerald-600 to-teal-700",
        "badge": "Directional Rotation",
        "audio_text": (
            "When talking about turns, describing the amount of turning is only half the story; we must also specify the direction of turning! "
            "Clockwise movement is defined as rotation in the same direction that the hands of a clock naturally move around the dial: from the top towards the right, then down to the bottom, and back up through the left. "
            "Think of tightening a screw into wood, or turning a water tap to close it tightly shut: both follow the clockwise path! "
            "In our homes and schools, the classic mnemonic rule is 'righty-tighty': rotating an object towards the right (clockwise) screws it in and seals it closed. "
            "When runners race around an outdoor athletics track in many international events, or when mechanical gears mesh to drive a vehicle forward, clockwise rotation directs the momentum. "
            "Whenever an arrow sweeps from 12 towards 1, 2, and 3, it is travelling clockwise."
        ),
        "theory_blocks": [
            {
                "title": "Definition of Clockwise",
                "content": "Rotation that moves in the same direction as clock hands: Top → Right → Bottom → Left (12 → 3 → 6 → 9 → 12).",
                "icon": "🔄"
            },
            {
                "title": "Everyday Clockwise Actions",
                "content": "Tightening a screw, screwing on a jar lid, turning off a water tap ('righty-tighty'), and winding a mechanical wristwatch.",
                "icon": "🔩"
            },
            {
                "title": "Geometric Representation",
                "content": "Clockwise angles are drawn with circular arrows curving towards the right around the pivot point.",
                "icon": "🏹"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the direction of movement that follows the natural path of clock hands called?",
                "options": [
                    "Clockwise",
                    "Anti-clockwise",
                    "Linear",
                    "Perpendicular"
                ],
                "correct": 0,
                "feedback": "Correct! Movement following the path of clock hands is termed clockwise."
            },
            {
                "question": "Which household action typically requires a clockwise turn?",
                "options": [
                    "Tightening a water tap to stop water flow",
                    "Opening a sealed jam jar lid",
                    "Loosening a tight bolt",
                    "Unwinding a garden hose reel in reverse"
                ],
                "correct": 0,
                "feedback": "Spot on! Turning a tap clockwise tightens the internal valve and stops the water flow."
            }
        ]
    },
    {
        "id": 15,
        "heading": "Anti-Clockwise",
        "tagline": "Reversing the Turn: Opening Taps, Lids, and Counter-Rotations",
        "color": "from-rose-600 to-pink-700",
        "badge": "Counter Rotation",
        "audio_text": (
            "Now let us examine the opposite rotational path: anti-clockwise movement! "
            "Anti-clockwise rotation, also known in some regions as counter-clockwise, is movement in the direction opposite to that of clock hands: from the top towards the left, then down to the bottom, and back up through the right. "
            "Think of opening a tight water tap to let cool water pour out: you turn the handle anti-clockwise! "
            "When you unscrew the cap of a water bottle or twist open a jar of delicious mango pickle, your hand turns anti-clockwise to release the lid. "
            "The popular memory phrase is 'lefty-loosey': turning towards the left (anti-clockwise) loosens threads and opens seals. "
            "In mathematics and trigonometry, positive angles are traditionally measured in the anti-clockwise direction starting from the positive horizontal axis. "
            "Understanding both clockwise and anti-clockwise turns gives you complete navigational control over any rotational puzzle."
        ),
        "theory_blocks": [
            {
                "title": "Definition of Anti-Clockwise",
                "content": "Rotation in the direction opposite to clock hands: Top → Left → Bottom → Right (12 → 9 → 6 → 3 → 12).",
                "icon": "🔁"
            },
            {
                "title": "Everyday Anti-Clockwise Actions",
                "content": "Unscrewing bottle caps, loosening bolts, opening water taps ('lefty-loosey'), and spinning revolving doors in reverse.",
                "icon": "🚰"
            },
            {
                "title": "Mathematical Convention",
                "content": "In higher mathematics, the anti-clockwise direction is chosen as the standard positive rotational direction.",
                "icon": "📐"
            }
        ],
        "checkpoints": [
            {
                "question": "In which direction do you turn a bottle cap to open and unscrew it?",
                "options": [
                    "Anti-clockwise ('lefty-loosey')",
                    "Clockwise ('righty-tighty')",
                    "Straight downward without turning",
                    "Side-to-side horizontally"
                ],
                "correct": 0,
                "feedback": "Correct! Unscrewing a bottle cap requires an anti-clockwise turn ('lefty-loosey')."
            },
            {
                "question": "If an arrow at 12 on a clock turns anti-clockwise by a 1/4 turn, which number does it point to?",
                "options": [
                    "9",
                    "3",
                    "6",
                    "12"
                ],
                "correct": 0,
                "feedback": "Spot on! Turning anti-clockwise from 12 by 1/4 turn sweeps to the left, pointing to 9."
            }
        ]
    },
    {
        "id": 16,
        "heading": "Compass Turns",
        "tagline": "Navigating Cardinal Directions with Clockwise and Anti-Clockwise Turns",
        "color": "from-blue-600 to-teal-700",
        "badge": "Cardinal Navigation Game",
        "audio_text": (
            "Let us put all our knowledge together with the classic textbook directional game table! "
            "Imagine standing at the centre of a large compass rose with four cardinal directions: North pointing forward, South pointing straight behind you, East pointing to your right, and West pointing to your left. "
            "Between any two adjacent cardinal directions, such as North and East, there is exactly one quarter turn, or 90 degrees. "
            "If you are facing North and make a 1/4 turn clockwise, you end up facing East! "
            "If you are facing North and make a 1/4 turn anti-clockwise, you end up facing West. "
            "What if you face East and make a 1/2 turn? A 1/2 turn always reverses your heading, so you end up facing West! "
            "What if you start facing South and make a 3/4 turn clockwise? One quarter turn takes you to West, two takes you to North, and three brings you to East! "
            "By mapping turn fractions and directions onto cardinal compass points, you master both spatial orientation and geometric angle rotation."
        ),
        "theory_blocks": [
            {
                "title": "The 4 Cardinal Directions",
                "content": "North (N), East (E), South (S), West (W). Each adjacent pair is separated by a 1/4 turn (90° right angle).",
                "icon": "🧭"
            },
            {
                "title": "Clockwise Compass Sequence",
                "content": "N → (1/4 turn CW) → E → (1/4 turn CW) → S → (1/4 turn CW) → W → (1/4 turn CW) → N.",
                "icon": "➡️"
            },
            {
                "title": "Anti-Clockwise Compass Sequence",
                "content": "N → (1/4 turn ACW) → W → (1/4 turn ACW) → S → (1/4 turn ACW) → E → (1/4 turn ACW) → N.",
                "icon": "⬅️"
            }
        ],
        "checkpoints": [
            {
                "question": "If you are facing North and make a 1/4 turn clockwise, which direction do you face?",
                "options": [
                    "East",
                    "West",
                    "South",
                    "North"
                ],
                "correct": 0,
                "feedback": "Correct! Turning 1/4 turn clockwise from North brings you directly to East."
            },
            {
                "question": "Starting at West, you make a 1/2 turn. Which direction do you face?",
                "options": [
                    "East",
                    "North",
                    "South",
                    "West"
                ],
                "correct": 0,
                "feedback": "Spot on! A 1/2 turn always points in the exact opposite direction: opposite of West is East."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 9 to 16. Count: {len(slides_9_to_16)}")


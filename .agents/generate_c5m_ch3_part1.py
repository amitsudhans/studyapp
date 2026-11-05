#!/usr/bin/env python3
"""
Generate Slides 1 to 8 data for NCERT Class 5 Mathematics - Chapter 3: Angles as Turns
"""

slides_1_to_8 = [
    {
        "id": 1,
        "heading": "Turning Around",
        "tagline": "Movement, Rotation, and the Spark of Geometry",
        "color": "from-amber-500 to-orange-600",
        "badge": "Class 5 Maths • Chapter 3",
        "audio_text": (
            "Welcome, young mathematicians! Today we step into an exciting world where every physical turn creates a mathematical angle. "
            "Think of a spinning giant wheel at an amusement park, a turning doorknob, or standing in the playground and pivoting on your heels to face your friend. "
            "When an object or person rotates around a fixed point, it is not moving straight forward; rather, it is executing a turn. "
            "In mathematics, we measure this circular movement to understand direction, orientation, and shape. "
            "Whenever an arm or ray pivots around a stationary centre, it sweeps out a portion of circular space. "
            "Notice how the blades of a ceiling fan continuously rotate around the central motor, or how the hands of a clock journey smoothly across the numbered dial. "
            "All geometric shapes, from triangular road signs to rectangular book covers, are formed by lines that meet after turning by precise amounts. "
            "By observing turns in our daily life, we uncover the very foundation of geometry. "
            "Let us explore how rotation turns everyday action into mathematical wonder!"
        ),
        "theory_blocks": [
            {
                "title": "What Is a Turn?",
                "content": "A turn is a circular rotational movement around a stationary fixed point called the centre or pivot. Rather than travelling along a straight line, an object changes its heading or facing direction by rotating.",
                "icon": "🔄"
            },
            {
                "title": "Everyday Turns",
                "content": "We encounter turns everywhere: giant wheel cabins sweeping through the sky, clock hands ticking around the dial, revolving doors, bicycle pedals, and gymnasts spinning on the mat.",
                "icon": "🎡"
            },
            {
                "title": "The Geometric Connection",
                "content": "Geometry is not just frozen lines on paper. Angles are dynamic measurements of how much one line has rotated away from another line from a shared starting position.",
                "icon": "📐"
            }
        ],
        "checkpoints": [
            {
                "question": "What kind of motion takes place when a giant wheel rotates around its central axle?",
                "options": [
                    "Rotational turning motion around a fixed pivot",
                    "Straight-line linear motion across the ground",
                    "Random zigzag drifting without a fixed centre",
                    "Periodic vertical bounce without angle change"
                ],
                "correct": 0,
                "feedback": "Correct! A giant wheel rotates around its fixed central axle, sweeping out turns that form geometric angles."
            },
            {
                "question": "Which of the following is the best real-world example of turning movement?",
                "options": [
                    "A minute hand sweeping around a clock dial",
                    "A train moving along a perfectly straight track",
                    "An apple falling straight down from a tree branch",
                    "A ruler lying flat and stationary on a desk"
                ],
                "correct": 0,
                "feedback": "Spot on! The minute hand continuously pivots around the dial centre, illustrating rotational turning."
            }
        ]
    },
    {
        "id": 2,
        "heading": "Turn Types",
        "tagline": "Full Turns, Half Turns, and Quarter Turns",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Core Fractions of Rotation",
        "audio_text": (
            "Now let us classify turns by looking at how much circular distance has been completed. "
            "Imagine standing in the schoolyard facing North. If you turn all the way around until you face North once again, you have executed one full turn. "
            "A full turn completes a whole circle of rotation. "
            "What if you turn halfway around so that you now face directly South, the opposite direction? That is a half turn, representing exactly 1/2 of a full rotation. "
            "If you start facing North and turn just enough to face East, you have made a quarter turn, which is exactly 1/4 of a full circle. "
            "If you make two quarter turns in the same direction, 1/4 plus 1/4 equals 2/4, which simplifies to 1/2, a half turn! "
            "And if you make four quarter turns, you complete 4/4, which brings you right back to your starting direction as a complete whole turn. "
            "Straw models, clock hands, and compass pointers help us clearly observe and verify these fundamental rotational fractions."
        ),
        "theory_blocks": [
            {
                "title": "1 Full Turn (Whole Circle)",
                "content": "Rotating completely around a pivot back to the exact initial facing direction. Represented as 1 whole turn or 4 quarter turns.",
                "icon": "⭕"
            },
            {
                "title": "1/2 Turn (Half Turn)",
                "content": "Rotating halfway across the circle, facing the exact opposite direction. Exactly equal to 2 quarter turns (1/4 + 1/4 = 1/2).",
                "icon": "↔️"
            },
            {
                "title": "1/4 Turn (Quarter Turn)",
                "content": "Rotating one-fourth of a circle. Transforms facing direction from North to East, or East to South, producing a classic square corner.",
                "icon": "↗️"
            }
        ],
        "checkpoints": [
            {
                "question": "How many quarter (1/4) turns are required to complete one full turn?",
                "options": [
                    "4 quarter turns",
                    "2 quarter turns",
                    "3 quarter turns",
                    "8 quarter turns"
                ],
                "correct": 0,
                "feedback": "Exactly! 4 quarter turns combine to make 4/4 = 1 complete whole turn."
            },
            {
                "question": "If you are facing North and perform a 1/2 turn, which direction will you face?",
                "options": [
                    "South",
                    "East",
                    "West",
                    "North"
                ],
                "correct": 0,
                "feedback": "Correct! A 1/2 turn rotates you halfway around the circle to face the exact opposite direction, South."
            }
        ]
    },
    {
        "id": 3,
        "heading": "What Is Angle",
        "tagline": "The Amount of Turning Between Two Arms at a Vertex",
        "color": "from-teal-600 to-emerald-700",
        "badge": "Geometric Definition",
        "audio_text": (
            "We are now ready to formalize what an angle truly is in mathematics. "
            "Take two straight rays or arms connected together at a single common endpoint. This shared meeting point is known as the vertex. "
            "When both arms lie directly on top of each other, there is zero opening. "
            "As we keep one arm fixed and rotate the second arm outward around the vertex, a gap or opening is created between them. "
            "An angle is defined as the measure of the amount of turning required to rotate one arm from the position of the other arm around their shared vertex! "
            "Notice that the size of an angle depends purely on the degree or fraction of turning, not on how long the drawn arms are. "
            "Even if you draw two short pencil lines or two kilometer-long laser beams, if the amount of turning between them is the same, the angle is identical. "
            "Straw strips fastened with a split pin provide the ideal tool to demonstrate angles of every conceivable opening."
        ),
        "theory_blocks": [
            {
                "title": "Anatomy of an Angle",
                "content": "An angle consists of two straight arms (rays) meeting at a single common corner called the vertex. The measure of the angle is the amount of turning between these arms.",
                "icon": "📐"
            },
            {
                "title": "Arm Length vs Angle Size",
                "content": "The size of an angle is determined solely by the amount of rotation between its arms. Extending or shortening the drawn arms does not alter the angle measure in any way.",
                "icon": "📏"
            },
            {
                "title": "The Dynamic Ray Model",
                "content": "Think of one arm as a stationary baseline and the other arm as a rotating pointer. The gap swept open between them is the angle.",
                "icon": "🧭"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the common meeting point of the two arms of an angle called?",
                "options": [
                    "Vertex",
                    "Circumference",
                    "Perimeter",
                    "Radius"
                ],
                "correct": 0,
                "feedback": "Spot on! The vertex is the shared endpoint where the two rays or arms meet."
            },
            {
                "question": "If you lengthen the drawn lines of an angle without rotating them, what happens to the angle?",
                "options": [
                    "The angle remains exactly the same",
                    "The angle becomes twice as large",
                    "The angle shrinks into an acute angle",
                    "The angle turns into a straight line"
                ],
                "correct": 0,
                "feedback": "Correct! Angle size depends solely on the amount of turning between the arms, not on arm length."
            }
        ]
    },
    {
        "id": 4,
        "heading": "Right Angle",
        "tagline": "The Benchmark Quarter Turn and Perfect L-Corner",
        "color": "from-emerald-600 to-green-700",
        "badge": "1/4 Turn Benchmark",
        "audio_text": (
            "The most important benchmark in practical geometry is the right angle. "
            "A right angle is created by exactly a quarter turn, which is 1/4 of a full rotation. "
            "When two arms meet at a right angle, they form a crisp, perpendicular L-shape, like the corner of your textbook, the edge of a doorframe, or the tiles on your classroom floor. "
            "In angular units, a full turn contains 360 degrees, so one quarter of 360 degrees equals precisely 90 degrees. "
            "Whenever we see a 90-degree right angle in geometry drawings, we indicate it with a distinctive square corner symbol rather than a rounded arc. "
            "Look at the hands of a clock at 3 o'clock or 9 o'clock: the hour hand and minute hand are separated by exactly a quarter turn, forming a pristine right angle. "
            "Architects and builders rely on right angles to ensure that walls stand straight, floors remain level, and buildings stand upright securely."
        ),
        "theory_blocks": [
            {
                "title": "1/4 Turn = Right Angle",
                "content": "A quarter turn sweeps out exactly 1/4 of a circle (90°). The two arms are perpendicular to each other, forming an upright L-corner.",
                "icon": "📐"
            },
            {
                "title": "Square Symbol Marking",
                "content": "Unlike other angles that use curved arcs, right angles are marked with a distinct square symbol at the vertex to signify exact perpendicularity.",
                "icon": "⏹️"
            },
            {
                "title": "Everyday Right Angles",
                "content": "Textbook corners, mobile phone screens, windows, doors, chessboards, and clock hands at 3:00 and 9:00 all display perfect right angles.",
                "icon": "🪟"
            }
        ],
        "checkpoints": [
            {
                "question": "What fraction of a full turn forms a right angle?",
                "options": [
                    "1/4 turn (quarter turn)",
                    "1/2 turn (half turn)",
                    "3/4 turn (three-quarter turn)",
                    "1/8 turn (eighth turn)"
                ],
                "correct": 0,
                "feedback": "Excellent! A quarter turn (1/4 turn = 90°) creates a perfect right angle."
            },
            {
                "question": "Which clock time displays a perfect right angle between the hour and minute hands?",
                "options": [
                    "3:00",
                    "6:00",
                    "12:00",
                    "1:30"
                ],
                "correct": 0,
                "feedback": "Correct! At 3:00, the minute hand points to 12 and the hour hand points to 3, forming a 1/4 turn (90°)."
            }
        ]
    },
    {
        "id": 5,
        "heading": "Acute Angle",
        "tagline": "Sharp Turns Less Than a Quarter Turn",
        "color": "from-cyan-600 to-blue-700",
        "badge": "Less Than 1/4 Turn",
        "audio_text": (
            "Now let us examine angles that are smaller than a right angle. "
            "An acute angle is created by a turn that is less than a quarter turn. "
            "Because a quarter turn equals 90 degrees, an acute angle measures greater than 0 degrees but strictly less than 90 degrees. "
            "The word acute comes from a Latin word meaning sharp or pointed. "
            "Think of the sharp tip of a sharpened pencil, the partially opened blades of a pair of scissors, a slice of pizza cut into 8 pieces, or the beak of a sparrow picking seeds. "
            "When the hands of a clock show 1 o'clock or 2 o'clock, the opening between the hands is distinctly less than a quarter turn, making it an acute angle. "
            "Whenever you see an angle whose opening is narrow and sharp, narrower than the square corner of a sheet of paper, you are observing an acute angle!"
        ),
        "theory_blocks": [
            {
                "title": "Definition of Acute Angle",
                "content": "An angle produced by a turn strictly less than 1/4 turn (between 0° and 90°). The opening is narrower than a right angle.",
                "icon": "🔺"
            },
            {
                "title": "Visual Characteristics",
                "content": "Acute angles appear sharp, pointed, and narrow. If you slide a right-angled paper corner into an acute angle, the angle's arm falls inside the paper.",
                "icon": "✂️"
            },
            {
                "title": "Real-World Examples",
                "content": "Partially opened scissors, alligator jaws opening slightly, clock hands at 2:00 (60°), pencil tips, and slices of watermelon.",
                "icon": "🐊"
            }
        ],
        "checkpoints": [
            {
                "question": "How is an acute angle defined in terms of turns?",
                "options": [
                    "A turn less than a quarter (1/4) turn",
                    "A turn exactly equal to a quarter turn",
                    "A turn greater than a quarter turn but less than half turn",
                    "A turn equal to two quarter turns"
                ],
                "correct": 0,
                "feedback": "Correct! Any angle formed by a turn less than a quarter turn (< 90°) is acute."
            },
            {
                "question": "At 2:00, what type of angle is formed between the clock hands?",
                "options": [
                    "Acute angle",
                    "Right angle",
                    "Obtuse angle",
                    "Straight angle"
                ],
                "correct": 0,
                "feedback": "Spot on! At 2:00, the hands span 2 clock numbers (60°), which is less than a 1/4 turn, forming an acute angle."
            }
        ]
    },
    {
        "id": 6,
        "heading": "Obtuse Angle",
        "tagline": "Wide Turns Greater Than a Quarter Turn but Less Than a Half Turn",
        "color": "from-purple-600 to-indigo-700",
        "badge": "Between 1/4 and 1/2 Turn",
        "audio_text": (
            "Let us continue rotating past the right angle! "
            "When a turn is greater than a quarter turn, but less than a half turn, it produces an obtuse angle. "
            "In degrees, an obtuse angle measures strictly between 90 degrees and 180 degrees. "
            "The word obtuse means blunt or wide. An obtuse angle looks wide open, spread apart much broader than a standard square corner. "
            "Think of a reclining deck chair pushed back for sunbathing, a roof with a wide slope, a book opened wide flat across a lectern, or the blades of a windmill sweeping wide apart. "
            "Look at a clock dial at 4 o'clock or 5 o'clock: the separation between the hands is noticeably wider than a right angle, but has not yet formed a single straight line. "
            "Whenever an angle's arms spread out wider than the corner of a paper tester without lying in a straight line, it is an obtuse angle."
        ),
        "theory_blocks": [
            {
                "title": "Definition of Obtuse Angle",
                "content": "An angle formed by a turn greater than 1/4 turn (90°) and strictly less than 1/2 turn (180°). It is open wider than a right angle.",
                "icon": "📐"
            },
            {
                "title": "Visual Characteristics",
                "content": "Obtuse angles look broad, blunt, and sprawling. A square paper tester placed inside an obtuse angle will leave extra empty space visible.",
                "icon": "🛋️"
            },
            {
                "title": "Everyday Obtuse Angles",
                "content": "Reclining beach chairs, open laptop screens pushed past 90°, clock hands at 4:00 (120°) and 5:00 (150°), and wide residential roof gables.",
                "icon": "💻"
            }
        ],
        "checkpoints": [
            {
                "question": "An obtuse angle is created by a turn that is:",
                "options": [
                    "Greater than a 1/4 turn but less than a 1/2 turn",
                    "Strictly less than a 1/4 turn",
                    "Exactly equal to a 1/4 turn",
                    "Equal to one complete full turn"
                ],
                "correct": 0,
                "feedback": "Correct! An obtuse angle spans between 1/4 turn (90°) and 1/2 turn (180°)."
            },
            {
                "question": "What type of angle do the clock hands form at 4:00?",
                "options": [
                    "Obtuse angle",
                    "Acute angle",
                    "Right angle",
                    "Straight angle"
                ],
                "correct": 0,
                "feedback": "Spot on! At 4:00, the hands span 4 clock numbers (120°), which is wider than 90° but less than 180°, making it obtuse."
            }
        ]
    },
    {
        "id": 7,
        "heading": "Straight Angle",
        "tagline": "Two Quarter Turns Forming a Perfectly Flat Line",
        "color": "from-rose-600 to-red-700",
        "badge": "1/2 Turn = 2 Quarter Turns",
        "audio_text": (
            "What happens if we rotate an arm through two full quarter turns in sequence? "
            "1/4 turn plus another 1/4 turn equals 2/4, which simplifies to exactly 1/2 of a full turn. "
            "When an arm executes a half turn, it points in the direction exactly opposite to the starting arm. "
            "The two arms now form a single, unbroken straight line across the shared vertex! "
            "This special geometric configuration is called a straight angle. "
            "A straight angle measures exactly 180 degrees, which is the sum of two 90-degree right angles: 90 degrees plus 90 degrees equals 180 degrees. "
            "Observe a clock at exactly 6 o'clock: the hour hand points straight down to 6 while the minute hand points straight up to 12. "
            "Together, the hands form a vertical line passing through the centre, creating an unmistakable straight angle. "
            "A gymnast performing a full split, or an opened ruler spread flat on a table, perfectly demonstrates a straight angle."
        ),
        "theory_blocks": [
            {
                "title": "Two Quarter Turns = Half Turn",
                "content": "Combining two consecutive 1/4 turns yields 1/2 turn (180°). The two arms lie in opposite directions along a single straight line.",
                "icon": "📏"
            },
            {
                "title": "180° Flat Angle",
                "content": "A straight angle equals two right angles combined (90° + 90° = 180°). The angle arc looks like a perfect semicircle.",
                "icon": "🌗"
            },
            {
                "title": "Classic Clock Example",
                "content": "At 6:00, the minute hand pointing to 12 and the hour hand pointing to 6 form a straight line, showcasing a straight angle.",
                "icon": "🕕"
            }
        ],
        "checkpoints": [
            {
                "question": "A straight angle is created by what fraction of a full turn?",
                "options": [
                    "1/2 turn (two quarter turns)",
                    "1/4 turn (one quarter turn)",
                    "3/4 turn (three quarter turns)",
                    "1 full turn (four quarter turns)"
                ],
                "correct": 0,
                "feedback": "Correct! A straight angle is formed by a 1/2 turn, which equals two 1/4 turns (180°)."
            },
            {
                "question": "Which clock time shows the hour hand and minute hand forming a straight angle?",
                "options": [
                    "6:00",
                    "3:00",
                    "9:00",
                    "12:00"
                ],
                "correct": 0,
                "feedback": "Spot on! At 6:00, the hands point in opposite directions to form a straight 180° line."
            }
        ]
    },
    {
        "id": 8,
        "heading": "Paper Fan",
        "tagline": "Folding and Unfolding Angles with Pleated Paper",
        "color": "from-amber-600 to-yellow-600",
        "badge": "Hands-On Activity 1",
        "audio_text": (
            "Let us explore our first hands-on laboratory activity from the textbook: making a paper fan to visualize every type of angle! "
            "Take a rectangular sheet of craft paper and fold it back and forth into accordion pleats, about one centimetre wide. "
            "Pinch one end tightly with a rubber band or thread to create the pivot vertex, while leaving the other end free to open. "
            "When the fan is held almost closed, the opening between the two outer edges is narrow, forming a sharp acute angle. "
            "Open the fan wider until the outer ribs form an upright L-shape: you have just modeled a crisp right angle! "
            "Spread the fan wider still, so it spans past the square corner: now the ribs display an obtuse angle. "
            "If you pull the outer edges completely flat across from each other, the fan creates a semicircular straight angle. "
            "And if you glue two fans back-to-back and open them fully into a complete wheel, you demonstrate a full turn! "
            "Through this simple craft, every family of angles comes alive in your hands."
        ),
        "theory_blocks": [
            {
                "title": "Accordion Paper Folding",
                "content": "Folding paper into uniform accordion pleats creates an adjustable geometric model that smoothly expands from 0° to 180° and beyond.",
                "icon": "🪭"
            },
            {
                "title": "Dynamic Angle Progression",
                "content": "Closed = Acute angle; Quarter spread = Right angle; Wide spread = Obtuse angle; Flat spread = Straight angle; Full circle = Complete turn.",
                "icon": "🔄"
            },
            {
                "title": "Pedagogical Value",
                "content": "Tactile manipulation helps internalize that angles are continuous spreads of turning rather than static disconnected drawings.",
                "icon": "✨"
            }
        ],
        "checkpoints": [
            {
                "question": "When a folded paper fan is opened halfway into an upright L-shape, what angle does it represent?",
                "options": [
                    "Right angle",
                    "Acute angle",
                    "Straight angle",
                    "Full turn"
                ],
                "correct": 0,
                "feedback": "Correct! An upright L-shape opening represents a 1/4 turn, or right angle."
            },
            {
                "question": "What happens to the angle between the fan edges as the fan is opened wider from a right angle towards a straight line?",
                "options": [
                    "It becomes an obtuse angle",
                    "It becomes an acute angle",
                    "It shrinks to zero degrees",
                    "It turns into a square corner"
                ],
                "correct": 0,
                "feedback": "Spot on! Opening wider than 1/4 turn but less than 1/2 turn forms an obtuse angle."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 1 to 8. Count: {len(slides_1_to_8)}")


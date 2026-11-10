#!/usr/bin/env python3
"""
Generate NCERT Class 3 Mathematics - Chapter 11: Filling and Lifting
Part 3: Slides 17 to 20 (Mastery Challenge Quizzes)
4 Slides × 10 Questions = 40 Questions
Each question has: id, question, options (4), answer (0-3), hint, explanation, solution_steps (3 steps).
Titles: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human character names. Zero teacher personas.
"""

slides_part3 = [
    # Slide 17: Challenge 1 (Liquid Capacity & Informal Measuring)
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Liquid capacity, glass sizes, equal container pouring, and lemonade stall word problems",
        "questions": [
            {
                "question": "A customer drinks 2 large tumblers of juice. If each tumbler holds the same as 3 small glasses, how many small glasses did they drink?",
                "options": ["6 small glasses (2 × 3)", "5 small glasses", "3 small glasses", "9 small glasses"],
                "answer": 0,
                "hint": "Multiply 2 tumblers by 3 small glasses each.",
                "explanation": "2 large tumblers × 3 small glasses per tumbler = 6 small glasses in total volume.",
                "solution_steps": [
                    "Identify the conversion ratio: 1 large tumbler = 3 small glasses.",
                    "Multiply the number of large tumblers by the ratio: 2 × 3.",
                    "Calculate 2 × 3 = 6 small glasses."
                ]
            },
            {
                "question": "Why is capacity measured by internal volume rather than just counting the number of cups?",
                "options": [
                    "Different cups have different holding sizes, so cup count alone does not determine volume",
                    "All cups in the world are exactly the same size",
                    "Liquids shrink when poured into cups",
                    "Counting cups takes too much time"
                ],
                "answer": 0,
                "hint": "Think about whether a tiny espresso cup holds the same as a giant mug.",
                "explanation": "Cups vary widely in dimensions; true capacity depends on the physical volume of liquid held inside.",
                "solution_steps": [
                    "Recognize that physical vessels differ in height, width, and shape.",
                    "Understand that counting containers ignores individual holding space.",
                    "Conclude that internal volume (capacity) is the true metric for liquid measurement."
                ]
            },
            {
                "question": "Three differently shaped glasses of milk are poured into three identical transparent jars. What tells us which glass held the most?",
                "options": [
                    "The jar with the highest liquid level",
                    "The jar with the lowest liquid level",
                    "The jar that feels the warmest",
                    "The jar with the most bubbles"
                ],
                "answer": 0,
                "hint": "In identical jars, a higher liquid line means greater volume.",
                "explanation": "Because identical jars have equal cross-sectional area, liquid height is directly proportional to volume.",
                "solution_steps": [
                    "Note that identical jars have equal width and base shape.",
                    "Recall that volume = base area × liquid height.",
                    "Conclude that the jar with the highest liquid level contained the greatest volume."
                ]
            },
            {
                "question": "It takes 3 small bowls of water to fill 1 drinking glass. How many bowls will it take to fill 4 drinking glasses?",
                "options": ["12 bowls (4 × 3)", "7 bowls (4 + 3)", "10 bowls", "1 bowl"],
                "answer": 0,
                "hint": "Multiply 4 glasses by 3 bowls per glass.",
                "explanation": "4 glasses × 3 bowls per glass = 12 small bowls.",
                "solution_steps": [
                    "Identify the unit rate: 1 glass = 3 bowls.",
                    "Multiply by 4 glasses: 4 × 3 bowls.",
                    "Calculate 4 × 3 = 12 bowls."
                ]
            },
            {
                "question": "A lemonade jug can fill exactly 8 glasses. If 24 glasses of lemonade are needed for a party, how many jugs must be prepared?",
                "options": ["3 jugs (24 ÷ 8)", "2 jugs", "4 jugs", "8 jugs"],
                "answer": 0,
                "hint": "Divide 24 total glasses by 8 glasses per jug.",
                "explanation": "24 glasses ÷ 8 glasses per jug = 3 full jugs.",
                "solution_steps": [
                    "State total glasses required: 24 glasses.",
                    "Divide by the capacity of 1 jug: 24 ÷ 8.",
                    "Calculate 3 jugs."
                ]
            },
            {
                "question": "At a refreshment stall, 1 glass of lemonade requires 2 full ladles. How many ladles are needed for 7 glasses?",
                "options": ["14 ladles (7 × 2)", "9 ladles", "12 ladles", "5 ladles"],
                "answer": 0,
                "hint": "Multiply 7 glasses by 2 ladles each.",
                "explanation": "7 glasses × 2 ladles per glass = 14 ladles.",
                "solution_steps": [
                    "Identify the ladle rate per glass: 2 ladles/glass.",
                    "Multiply by 7 glasses: 7 × 2.",
                    "Calculate 14 ladles in total."
                ]
            },
            {
                "question": "A large mixing bowl holds 18 ladles of fruit punch. If each serving glass takes 3 ladles, how many glasses can be served from the bowl?",
                "options": ["6 glasses (18 ÷ 3)", "15 glasses", "21 glasses", "3 glasses"],
                "answer": 0,
                "hint": "Divide 18 ladles by 3 ladles per glass.",
                "explanation": "18 ladles ÷ 3 ladles per glass = 6 glasses.",
                "solution_steps": [
                    "Identify total volume: 18 ladles.",
                    "Divide by portion size: 18 ÷ 3.",
                    "Calculate 6 glasses."
                ]
            },
            {
                "question": "Which of these everyday containers usually has the SMALLEST liquid capacity?",
                "options": ["A medicine dropper", "A soup bowl", "A water jug", "A kitchen cooking pot"],
                "answer": 0,
                "hint": "Think about which vessel delivers tiny drops of liquid.",
                "explanation": "A medicine dropper holds only a few millilitres, much less than a bowl, jug, or cooking pot.",
                "solution_steps": [
                    "Compare typical capacities: dropper (~2 mL), bowl (~250 mL), jug (~1 L), pot (~3 L).",
                    "Identify the vessel with the smallest volume.",
                    "Conclude that the medicine dropper has the smallest capacity."
                ]
            },
            {
                "question": "If 5 glasses of water fill 1 bottle, and 4 bottles fill 1 bucket, how many glasses fill the bucket?",
                "options": ["20 glasses (5 × 4)", "9 glasses (5 + 4)", "15 glasses", "25 glasses"],
                "answer": 0,
                "hint": "Multiply glasses per bottle by bottles per bucket.",
                "explanation": "1 bucket = 4 bottles = 4 × 5 glasses = 20 glasses.",
                "solution_steps": [
                    "Express 1 bottle in glasses: 1 bottle = 5 glasses.",
                    "Express 1 bucket in bottles: 1 bucket = 4 bottles.",
                    "Multiply: 4 × 5 = 20 glasses to fill the bucket."
                ]
            },
            {
                "question": "A short, wide mug and a tall, narrow glass both hold 300 mL of water. How does their capacity compare?",
                "options": [
                    "They have identical capacity despite their different shapes",
                    "The tall glass has greater capacity",
                    "The short mug has greater capacity",
                    "Neither container has capacity"
                ],
                "answer": 0,
                "hint": "Compare the numerical volume: 300 mL vs 300 mL.",
                "explanation": "Both hold 300 mL, so their liquid capacity is exactly equal regardless of their physical dimensions.",
                "solution_steps": [
                    "Read the capacity of each container: both hold 300 mL.",
                    "Understand that shape does not alter numerical liquid volume.",
                    "Conclude that their capacities are completely identical."
                ]
            }
        ]
    },

    # Slide 18: Challenge 2 (Standard Litres & Fractional Volumes)
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "The standard metric litre, everyday container classification, and fractional litre arithmetic",
        "questions": [
            {
                "question": "What is the standard base unit of liquid capacity in the international metric system?",
                "options": ["Litre (L)", "Kilogram (kg)", "Metre (m)", "Handspan"],
                "answer": 0,
                "hint": "It is abbreviated as capital L.",
                "explanation": "The litre (L) is the metric standard unit for measuring liquid volume and capacity.",
                "solution_steps": [
                    "Identify metric measurement categories: capacity, mass, length.",
                    "Recall that litre is specifically designed for liquids.",
                    "Conclude that the litre (L) is the standard base unit."
                ]
            },
            {
                "question": "How many millilitres (mL) are contained in exactly 1 standard litre?",
                "options": ["1,000 mL", "100 mL", "10 mL", "500 mL"],
                "answer": 0,
                "hint": "The prefix 'milli' means one-thousandth.",
                "explanation": "1 litre is defined as 1,000 millilitres (1 L = 1,000 mL).",
                "solution_steps": [
                    "Recall the metric prefix: milli- = 1/1,000.",
                    "Therefore, 1,000 millilitres make up 1 full litre.",
                    "Confirm the identity: 1 L = 1,000 mL."
                ]
            },
            {
                "question": "Which of the following household vessels typically holds MORE than 1 litre of water?",
                "options": ["A bathroom bathing bucket", "A medicine spoon", "An inkpot", "A coffee teacup"],
                "answer": 0,
                "hint": "Think of a heavy container used for bathing or cleaning.",
                "explanation": "A bathing bucket typically holds 15 to 20 litres, which is far greater than 1 litre.",
                "solution_steps": [
                    "Estimate volumes: spoon (~5 mL), inkpot (~50 mL), teacup (~150 mL), bucket (~15,000 mL).",
                    "Compare each to 1 litre (1,000 mL).",
                    "Conclude that the bathing bucket holds substantially more than 1 litre."
                ]
            },
            {
                "question": "A dairy shop sells milk in half-litre pouches. How many pouches must you buy to get 2 full litres?",
                "options": ["4 pouches (2 litres × 2 pouches/litre)", "2 pouches", "6 pouches", "8 pouches"],
                "answer": 0,
                "hint": "Each litre requires 2 half-litre pouches.",
                "explanation": "Each litre takes 2 pouches, so 2 litres require 2 × 2 = 4 pouches.",
                "solution_steps": [
                    "Recall that 1 litre = 2 half-litre pouches.",
                    "Multiply by 2 litres: 2 × 2.",
                    "Calculate 4 pouches in total."
                ]
            },
            {
                "question": "What is the volume of one-quarter of a litre (1/4 L) in millilitres?",
                "options": ["250 mL", "500 mL", "750 mL", "100 mL"],
                "answer": 0,
                "hint": "Divide 1,000 mL by 4 equal parts.",
                "explanation": "1,000 mL ÷ 4 = 250 mL, which equals 1/4 of a litre.",
                "solution_steps": [
                    "Start with 1 full litre: 1,000 mL.",
                    "Divide into 4 equal quarters: 1,000 ÷ 4.",
                    "Calculate 250 mL."
                ]
            },
            {
                "question": "How many quarter-litre glasses (250 mL) are needed to fill a 1-litre bottle?",
                "options": ["4 glasses", "2 glasses", "8 glasses", "1 glass"],
                "answer": 0,
                "hint": "Four quarters combine to make one whole.",
                "explanation": "4 × 250 mL = 1,000 mL = 1 litre, so 4 glasses are required.",
                "solution_steps": [
                    "Identify the fraction: each glass is 1/4 of a litre.",
                    "To reach 1 whole litre, you need 4/4.",
                    "Conclude that exactly 4 glasses are needed."
                ]
            },
            {
                "question": "If you combine two 250 mL juice boxes and one 500 mL water bottle, what is the total volume?",
                "options": ["1,000 mL (1 litre)", "750 mL", "500 mL", "1,500 mL"],
                "answer": 0,
                "hint": "Add: 250 + 250 + 500.",
                "explanation": "250 mL + 250 mL + 500 mL = 500 mL + 500 mL = 1,000 mL = 1 litre.",
                "solution_steps": [
                    "Add the two juice boxes: 250 + 250 = 500 mL.",
                    "Add the water bottle: 500 + 500 = 1,000 mL.",
                    "Convert to litres: 1,000 mL = 1 litre."
                ]
            },
            {
                "question": "A recipe calls for 3/4 litre of milk. How many millilitres is this?",
                "options": ["750 mL", "250 mL", "500 mL", "300 mL"],
                "answer": 0,
                "hint": "Three quarters of 1,000 mL is 3 × 250 mL.",
                "explanation": "3/4 of 1,000 mL = 3 × 250 mL = 750 mL.",
                "solution_steps": [
                    "Identify 1/4 litre = 250 mL.",
                    "Multiply by 3: 3 × 250 mL.",
                    "Calculate 750 mL."
                ]
            },
            {
                "question": "A water bottle has a capacity of 1.5 litres. How many millilitres does it hold?",
                "options": ["1,500 mL (1,000 + 500)", "150 mL", "15,000 mL", "1,050 mL"],
                "answer": 0,
                "hint": "1 litre is 1,000 mL, and half a litre is 500 mL.",
                "explanation": "1.5 litres = 1 litre + 0.5 litre = 1,000 mL + 500 mL = 1,500 mL.",
                "solution_steps": [
                    "Convert 1 whole litre: 1,000 mL.",
                    "Convert 0.5 (half) litre: 500 mL.",
                    "Add together: 1,000 + 500 = 1,500 mL."
                ]
            },
            {
                "question": "A milk vendor measures milk using a 1-litre can. If they fill a customer's container 5 times, how much milk was delivered?",
                "options": ["5 litres", "50 litres", "2.5 litres", "10 litres"],
                "answer": 0,
                "hint": "Multiply 5 fillings by 1 litre each.",
                "explanation": "5 × 1 litre = 5 litres of milk delivered.",
                "solution_steps": [
                    "Unit measure = 1 litre.",
                    "Count of measures = 5.",
                    "Calculate 5 × 1 = 5 litres."
                ]
            }
        ]
    },

    # Slide 19: Challenge 3 (Physical Weight & Balance Investigations)
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Muscular weight sensing, pan-balance principles, non-standard weights, and weight ordering",
        "questions": [
            {
                "question": "What invisible natural force pulls heavier objects downward with greater force?",
                "options": ["Earth's gravitational force", "Wind pressure", "Magnetic attraction", "Sunlight rays"],
                "answer": 0,
                "hint": "It is the downward pull that gives objects weight on Earth.",
                "explanation": "Gravity is the natural force of attraction pulling masses downward toward the center of the Earth.",
                "solution_steps": [
                    "Identify the physical cause of weight.",
                    "Recall that Earth attracts all mass downward via gravity.",
                    "Conclude that gravity creates the sensation of heaviness."
                ]
            },
            {
                "question": "On a two-pan balance, the left pan sinks downward while the right pan rises. What does this show?",
                "options": [
                    "The object in the left pan is heavier than the object in the right pan",
                    "The object in the right pan is heavier",
                    "Both objects have identical weight",
                    "The scale is broken"
                ],
                "answer": 0,
                "hint": "The heavier side always tilts downward.",
                "explanation": "Greater weight pulls the pan down, so the sinking left pan contains the heavier object.",
                "solution_steps": [
                    "Observe pan movements: left pan moves down, right pan moves up.",
                    "Recall balance rule: downward tilt corresponds to greater gravitational pull.",
                    "Conclude that the left pan holds the heavier item."
                ]
            },
            {
                "question": "A pencil box balances with 15 identical five-rupee coins. A pair of scissors balances with 9 identical coins. Which item is lighter?",
                "options": ["The pair of scissors (by 6 coins)", "The pencil box", "Both weigh the same", "Cannot be determined"],
                "answer": 0,
                "hint": "Fewer balancing coins mean the object is lighter.",
                "explanation": "9 coins < 15 coins, so the scissors are lighter than the pencil box by 15 - 9 = 6 coins.",
                "solution_steps": [
                    "Compare the coin counts: scissors = 9 coins, pencil box = 15 coins.",
                    "Identify that a lower coin count means less weight.",
                    "Calculate the difference: 15 - 9 = 6 coins lighter."
                ]
            },
            {
                "question": "Why must all units (like coins or erasers) used on a balance be identical in weight?",
                "options": [
                    "To ensure that each counted unit represents an exact, uniform amount of weight",
                    "To make the balance look neat and tidy",
                    "Because coins change color when weighed",
                    "Because different coins make the table shake"
                ],
                "answer": 0,
                "hint": "Consistent units are the foundation of accurate measurement.",
                "explanation": "Standardized, identical units guarantee that each count represents an unvarying, reproducible quantity.",
                "solution_steps": [
                    "Consider what happens if units vary in weight: counts become meaningless.",
                    "Recognize that valid measurement requires uniform, reproducible units.",
                    "Conclude that identical units ensure fair, trusted comparisons."
                ]
            },
            {
                "question": "On a pan balance: Apple > Orange, and Orange > Plum. What is the order from lightest to heaviest?",
                "options": [
                    "Plum (lightest), Orange, Apple (heaviest)",
                    "Apple (lightest), Orange, Plum (heaviest)",
                    "Orange, Apple, Plum",
                    "All three fruits weigh the same"
                ],
                "answer": 0,
                "hint": "Plum is lighter than Orange, which is lighter than Apple.",
                "explanation": "By transitive ordering: Plum < Orange < Apple.",
                "solution_steps": [
                    "Note the first relation: Apple > Orange (Orange is lighter than Apple).",
                    "Note the second relation: Orange > Plum (Plum is lighter than Orange).",
                    "Combine in ascending order: Plum < Orange < Apple."
                ]
            },
            {
                "question": "A matchbox filled with dry sand balances with 5 metal paperclips. If a toy car balances with 3 sand matchboxes, how many paperclips equal the car?",
                "options": ["15 paperclips (3 × 5)", "8 paperclips (3 + 5)", "10 paperclips", "2 paperclips"],
                "answer": 0,
                "hint": "Multiply 3 matchboxes by 5 paperclips per matchbox.",
                "explanation": "3 matchboxes × 5 paperclips/matchbox = 15 paperclips.",
                "solution_steps": [
                    "Unit conversion: 1 sand matchbox = 5 paperclips.",
                    "Multiply by 3 matchboxes: 3 × 5.",
                    "Calculate 15 paperclips."
                ]
            },
            {
                "question": "When both pans of a balance are loaded and the central beam is completely level, what is this state called?",
                "options": ["Equilibrium (equal weight)", "Overload", "Deflection", "Friction"],
                "answer": 0,
                "hint": "Level beam indicates balanced, equal forces.",
                "explanation": "When downward forces on both sides match, the beam rests horizontal in a state of equilibrium.",
                "solution_steps": [
                    "Recall the definition of a balanced scale.",
                    "Recognize that equal downward gravitational force creates a level beam.",
                    "Identify this state as physical equilibrium."
                ]
            },
            {
                "question": "Which of these pairs of objects can be most easily compared by hand without a mechanical scale?",
                "options": [
                    "A heavy metal bowling ball and a lightweight feather",
                    "Two identical pencils from the same pack",
                    "Two identical coins of the same denomination",
                    "Two identical sheets of blank paper"
                ],
                "answer": 0,
                "hint": "Look for the pair with the most dramatic, obvious weight contrast.",
                "explanation": "The huge weight contrast between a heavy bowling ball and a feather is immediately obvious to human muscles.",
                "solution_steps": [
                    "Evaluate contrast: bowling ball vs feather has massive weight disparity.",
                    "Other pairs have near-zero difference, requiring sensitive balance scales.",
                    "Conclude bowling ball and feather are effortlessly distinguished by hand."
                ]
            },
            {
                "question": "A student places 4 marbles in the left pan and 6 marbles in the right pan. All marbles are identical. What happens?",
                "options": [
                    "The right pan tilts downward because 6 marbles are heavier than 4",
                    "The left pan tilts downward",
                    "The beam remains perfectly level",
                    "The marbles roll off simultaneously"
                ],
                "answer": 0,
                "hint": "More identical marbles mean more weight on that side.",
                "explanation": "6 marbles weigh more than 4 marbles, so the right pan experiences more gravitational force and tilts down.",
                "solution_steps": [
                    "Compare quantities: 6 marbles > 4 marbles.",
                    "Identify that identical units mean greater count = greater weight.",
                    "Conclude the right pan tilts downward."
                ]
            },
            {
                "question": "If an empty plastic cup is placed in the left pan and a cup full of sand is placed in the right pan, which side sinks?",
                "options": ["The right pan (full of sand)", "The left pan (empty cup)", "Neither sinks", "Both sink to the table"],
                "answer": 0,
                "hint": "Sand adds substantial mass and weight to the cup.",
                "explanation": "The sand adds significant mass, making the right cup much heavier than the empty left cup.",
                "solution_steps": [
                    "Compare contents: cup + sand > empty cup.",
                    "Recognize that sand has substantial mass.",
                    "Conclude the right pan sinks downward."
                ]
            }
        ]
    },

    # Slide 20: Challenge 4 (Standard Kilograms, Packs & Logic Riddles)
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Standard kilograms, packet equalization, fractional weights, and the 3-ball balance logic riddle",
        "questions": [
            {
                "question": "What is the standard metric base unit for measuring mass and weight in science and commerce?",
                "options": ["Kilogram (kg)", "Litre (L)", "Metre (m)", "Gram (g)"],
                "answer": 0,
                "hint": "It is abbreviated as small letters kg.",
                "explanation": "The kilogram (kg) is the international standard base unit of mass in the metric SI system.",
                "solution_steps": [
                    "Identify the standard SI base unit for mass.",
                    "Recognize that the kilogram (kg) is the official base unit.",
                    "Distinguish it from the litre (capacity) and metre (length)."
                ]
            },
            {
                "question": "How many grams (g) equal exactly 1 standard kilogram (kg)?",
                "options": ["1,000 g", "100 g", "10 g", "500 g"],
                "answer": 0,
                "hint": "The prefix 'kilo' means one thousand.",
                "explanation": "1 kilogram equals 1,000 grams (1 kg = 1,000 g).",
                "solution_steps": [
                    "Recall the metric prefix definition: kilo = 1,000.",
                    "Apply to grams: 1 kilogram = 1,000 grams.",
                    "Confirm the fundamental equality: 1 kg = 1,000 g."
                ]
            },
            {
                "question": "A packet of yellow lentils weighs 500 grams. What fraction of a kilogram is this packet?",
                "options": ["1/2 kg (half a kilogram)", "1/4 kg", "3/4 kg", "2 kg"],
                "answer": 0,
                "hint": "500 grams is half of 1,000 grams.",
                "explanation": "500 g out of 1,000 g is 500/1,000 = 1/2 of a kilogram.",
                "solution_steps": [
                    "Express as a fraction: 500 g / 1,000 g.",
                    "Simplify: divide numerator and denominator by 500.",
                    "Obtain 1/2 kg."
                ]
            },
            {
                "question": "How many 250-gram tea boxes are required to counterbalance a 1 kg iron weight on a pan balance?",
                "options": ["4 boxes (4 × 250 g = 1,000 g)", "2 boxes", "8 boxes", "1 box"],
                "answer": 0,
                "hint": "Divide 1,000 grams by 250 grams per box.",
                "explanation": "1,000 g ÷ 250 g/box = 4 boxes.",
                "solution_steps": [
                    "Convert 1 kg to grams: 1 kg = 1,000 g.",
                    "Divide by the weight of 1 box: 1,000 ÷ 250.",
                    "Calculate 4 boxes."
                ]
            },
            {
                "question": "Backpack A weighs 6 kg and Backpack B weighs 2 kg. How many kg should be moved from A to B to balance them equally?",
                "options": ["2 kg (both become 4 kg)", "4 kg", "1 kg", "3 kg"],
                "answer": 0,
                "hint": "Total weight = 8 kg. Each bag should weigh 4 kg.",
                "explanation": "Total weight = 6 + 2 = 8 kg. Half is 4 kg each. 6 - 2 = 4 kg, and 2 + 2 = 4 kg. Moving 2 kg equalizes them.",
                "solution_steps": [
                    "Calculate total weight: 6 kg + 2 kg = 8 kg.",
                    "Find the equal share for each bag: 8 kg ÷ 2 = 4 kg.",
                    "Determine amount to shift from Bag A: 6 kg - 4 kg = 2 kg."
                ]
            },
            {
                "question": "You have three identical-looking balls (A, B, C). One ball is heavier. You weigh A against B and the scale stays LEVEL. Which ball is heavy?",
                "options": [
                    "Ball C (the one left on the table)",
                    "Ball A",
                    "Ball B",
                    "None of the balls is heavy"
                ],
                "answer": 0,
                "hint": "If the two balls on the pans balance evenly, neither is the heavier one.",
                "explanation": "Because A and B balance evenly, they have equal weight. Therefore, the unweighed Ball C must be the heavy one.",
                "solution_steps": [
                    "Analyze the weighing: Left pan (Ball A) = Right pan (Ball B).",
                    "Deduce that neither A nor B is the odd heavy ball.",
                    "Conclude with certainty that Ball C is the heavier ball."
                ]
            },
            {
                "question": "In the same 3-ball puzzle, you weigh A against B and the LEFT pan sinks down. Which ball is the heavy one?",
                "options": ["Ball A (on the left pan)", "Ball B", "Ball C", "Cannot be determined"],
                "answer": 0,
                "hint": "The pan containing the heavier ball sinks downward.",
                "explanation": "Because the left pan sank, Ball A is heavier than Ball B, directly identifying Ball A as the heavy one.",
                "solution_steps": [
                    "Observe the scale: the left pan containing Ball A tilts downward.",
                    "Recall that downward tilt indicates greater gravitational weight.",
                    "Conclude directly that Ball A is the heavy ball."
                ]
            },
            {
                "question": "If you buy three 1/2 kg packets of flour and two 1/4 kg packets of sugar, what is the total weight in kilograms?",
                "options": ["2 kg (1.5 kg + 0.5 kg)", "1 kg", "3 kg", "2.5 kg"],
                "answer": 0,
                "hint": "Three 1/2 kg = 1.5 kg. Two 1/4 kg = 0.5 kg.",
                "explanation": "Flour = 3 × 1/2 kg = 1.5 kg. Sugar = 2 × 1/4 kg = 0.5 kg. Total = 1.5 + 0.5 = 2.0 kg.",
                "solution_steps": [
                    "Calculate flour weight: 3 × 500 g = 1,500 g (1.5 kg).",
                    "Calculate sugar weight: 2 × 250 g = 500 g (0.5 kg).",
                    "Add weights together: 1,500 g + 500 g = 2,000 g = 2 kg."
                ]
            },
            {
                "question": "Which of these everyday objects weighs approximately 1 kilogram?",
                "options": [
                    "A standard 1 kg sealed packet of cooking salt",
                    "A single metal paperclip",
                    "A full-sized family motorcar",
                    "A feather from a bird"
                ],
                "answer": 0,
                "hint": "Look for the grocery item explicitly manufactured to 1 kg standard.",
                "explanation": "A sealed cooking salt packet is manufactured to exactly 1 kg, serving as an ideal benchmark.",
                "solution_steps": [
                    "Compare weights: paperclip (~1 g), feather (<1 g), car (~1,500 kg), salt packet (1,000 g = 1 kg).",
                    "Identify the object manufactured to match the kilogram standard.",
                    "Conclude that the salt packet weighs approximately 1 kg."
                ]
            },
            {
                "question": "On a balance, 1 watermelon balances with 4 identical pineapples. If 1 pineapple balances with 3 apples, how many apples balance the watermelon?",
                "options": ["12 apples (4 × 3)", "7 apples (4 + 3)", "10 apples", "1 apple"],
                "answer": 0,
                "hint": "Multiply 4 pineapples by 3 apples per pineapple.",
                "explanation": "1 watermelon = 4 pineapples = 4 × 3 apples = 12 apples.",
                "solution_steps": [
                    "Identify relationship 1: 1 watermelon = 4 pineapples.",
                    "Identify relationship 2: 1 pineapple = 3 apples.",
                    "Substitute: 1 watermelon = 4 × (3 apples) = 12 apples."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    for s in slides_part3:
        title_wc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_wc} words) -> {len(s['questions'])} questions")
        assert 1 <= title_wc <= 3, f"Title {s['title']} not 1-3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} must have 10 questions"
        for q in s["questions"]:
            assert len(q["options"]) == 4, f"Question must have 4 options"
            assert len(q["solution_steps"]) == 3, f"Question must have 3 solution steps"
    print("All slides in Part 3 passed strict validation!")

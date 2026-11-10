# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 (4 Challenges x 10 Questions = 40 Questions)
Class 3 Mathematics - Chapter 3: Double Century
Strict requirements:
- Titles: 'Challenge 1', 'Challenge 2', 'Challenge 3', 'Challenge 4' (all 2 words)
- Zero human character names (no Raghav, Meera, Dhruv, Teji, Jojo, Deba, Deep, Pihu, etc.)
- Zero lecturer personas (no Dr, Sir, Madam, Mr, Mrs, Miss)
- Each question has id, q, 4 options, ans, hint, explanation, and 3-step solution_steps
"""

slides_part3 = [
    # Slide 17: Challenge 1 (Origins, Base-10, Zero & Marketplace Estimation)
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Origins & Base-10",
        "description": "Test your mastery of ancient counting tallies, the Indian decimal system, the power of zero, and marketplace grouping.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "How did prehistoric humans record counts tens of thousands of years ago?",
                "options": [
                    "Carving notches on bones, cave walls, and tree barks",
                    "Typing on electronic tablets and smartphones",
                    "Printing colored currency banknotes",
                    "Using mechanical pocket calculators"
                ],
                "ans": "Carving notches on bones, cave walls, and tree barks",
                "hint": "Think about tools and materials available before paper and pens existed.",
                "explanation": "Early humans carved notches into animal bones and stone cave walls to track days, seasons, and animal herds.",
                "solution_steps": {
                    "step1": "Recall prehistoric counting methods discussed in the chapter.",
                    "step2": "Identify natural materials used by early humans (bones, stone, bark).",
                    "step3": "Conclude that carving notches on bones and cave walls was the original method."
                }
            },
            {
                "id": "c1_q2",
                "q": "Why did early humans invent the grouping of tally marks into sets of 5, 10, or 20?",
                "options": [
                    "Counting hundreds of single marks one by one was slow and prone to errors",
                    "Because cave walls were too small to hold more than 5 marks",
                    "Ancient rulers strictly banned counting by ones",
                    "To hide numbers from neighboring villages"
                ],
                "ans": "Counting hundreds of single marks one by one was slow and prone to errors",
                "hint": "Grouping into bundles makes large quantities much faster and easier to count.",
                "explanation": "Grouping tally marks by 5, 10, or 20 enabled faster skip-counting and prevented counting errors.",
                "solution_steps": {
                    "step1": "Consider the difficulty of counting 100 individual single scratches.",
                    "step2": "Grouping organizes large quantities into manageable, recognizable bundles.",
                    "step3": "Select 'Counting hundreds of single marks one by one was slow and prone to errors'."
                }
            },
            {
                "id": "c1_q3",
                "q": "Which major mathematical milestone was created in ancient India?",
                "options": [
                    "Writing any number using only ten symbols (0 to 9) with place value",
                    "Inventing Roman numeral letters like X and C",
                    "Using tally sticks with sixty notches for all numbers",
                    "Creating a number system without any zeros"
                ],
                "ans": "Writing any number using only ten symbols (0 to 9) with place value",
                "hint": "Think about the decimal base-10 system used worldwide today.",
                "explanation": "Ancient Indian mathematicians created the decimal base-10 system using digits 0 to 9 with place value.",
                "solution_steps": {
                    "step1": "Identify the historical mathematical achievement highlighted in Chapter 3.",
                    "step2": "Recall that ancient India introduced the 10-digit decimal place-value system.",
                    "step3": "Select 'Writing any number using only ten symbols (0 to 9) with place value'."
                }
            },
            {
                "id": "c1_q4",
                "q": "What happens to the value of a digit when it shifts one column to the left in a decimal number?",
                "options": [
                    "Its value multiplies by 10",
                    "Its value decreases by 10",
                    "Its value stays exactly unchanged",
                    "Its value doubles"
                ],
                "ans": "Its value multiplies by 10",
                "hint": "Each place value column is ten times greater than the column to its right.",
                "explanation": "In our base-10 system, moving one column left multiplies the digit's positional worth by 10 (ones to tens, tens to hundreds).",
                "solution_steps": {
                    "step1": "Compare the columns: ones, tens, hundreds.",
                    "step2": "Observe that 1 ten = 10 ones, and 1 hundred = 10 tens.",
                    "step3": "Conclude that moving left multiplies value by 10."
                }
            },
            {
                "id": "c1_q5",
                "q": "What does the digit 0 represent when counting items in a fruit basket?",
                "options": [
                    "The complete absence of items (empty/nothing)",
                    "A basket with exactly 10 fruits",
                    "A basket with unlimited fruits",
                    "A broken fruit basket"
                ],
                "ans": "The complete absence of items (empty/nothing)",
                "hint": "Zero signifies void, emptiness, or having no objects.",
                "explanation": "As a count, zero represents an absence of objects, meaning there are no items present.",
                "solution_steps": {
                    "step1": "Recall the meaning of zero as a quantity.",
                    "step2": "If all fruits are taken away, none remain.",
                    "step3": "Select 'The complete absence of items (empty/nothing)'."
                }
            },
            {
                "id": "c1_q6",
                "q": "Why is the digit 0 essential in writing the number 105?",
                "options": [
                    "It acts as a placeholder for the empty tens column",
                    "It adds five more units to the hundreds column",
                    "It makes the number easier to pronounce in English",
                    "It indicates that 105 is smaller than 15"
                ],
                "ans": "It acts as a placeholder for the empty tens column",
                "hint": "Without 0, writing 1 and 5 would produce 15 instead of 105.",
                "explanation": "Zero holds the tens place so the digit 1 remains in the hundreds place, distinguishing 105 from 15.",
                "solution_steps": {
                    "step1": "Decompose 105 into hundreds, tens, and ones: 1 hundred, 0 tens, 5 ones.",
                    "step2": "Note that without 0 in the tens place, the number would read as 15.",
                    "step3": "Conclude that 0 acts as an indispensable column placeholder."
                }
            },
            {
                "id": "c1_q7",
                "q": "A market vendor packs bangles into 4 boxes of 10 bangles each and has 7 loose bangles. How many bangles are there in total?",
                "options": [
                    "47 bangles (40 + 7)",
                    "74 bangles",
                    "40 bangles",
                    "11 bangles"
                ],
                "ans": "47 bangles (40 + 7)",
                "hint": "Multiply 4 by 10, then add 7.",
                "explanation": "4 boxes of 10 equal 40 bangles; adding 7 loose bangles yields 40 + 7 = 47.",
                "solution_steps": {
                    "step1": "Calculate the tens: 4 boxes x 10 = 40.",
                    "step2": "Add the loose ones: 40 + 7 = 47.",
                    "step3": "Select 47 bangles."
                }
            },
            {
                "id": "c1_q8",
                "q": "If a fruit stall has 8 bunches of 10 bananas each, how many bananas are there in total?",
                "options": [
                    "80 bananas",
                    "18 bananas",
                    "88 bananas",
                    "800 bananas"
                ],
                "ans": "80 bananas",
                "hint": "Skip-count by tens eight times: 10, 20, 30...",
                "explanation": "8 bunches of 10 equal 8 x 10 = 80 bananas.",
                "solution_steps": {
                    "step1": "Identify the number of groups (8) and items per group (10).",
                    "step2": "Multiply 8 by 10 = 80.",
                    "step3": "Select 80 bananas."
                }
            },
            {
                "id": "c1_q9",
                "q": "What ancient Sanskrit word meaning 'empty' or 'void' was originally given to zero in India?",
                "options": [
                    "Shunya",
                    "Gana",
                    "Rupa",
                    "Kendra"
                ],
                "ans": "Shunya",
                "hint": "It literally translates to emptiness or void.",
                "explanation": "Ancient Indian mathematicians used the word 'shunya' (void/empty) to name zero.",
                "solution_steps": {
                    "step1": "Recall the historical terminology for zero from the curriculum.",
                    "step2": "Identify 'shunya' as the classical Sanskrit term.",
                    "step3": "Select 'Shunya'."
                }
            },
            {
                "id": "c1_q10",
                "q": "If you estimate a bowl holds about 50 sweets, and upon grouping by tens you find 5 full groups of 10 and 2 singles, what was the exact count?",
                "options": [
                    "52 sweets",
                    "50 sweets",
                    "25 sweets",
                    "520 sweets"
                ],
                "ans": "52 sweets",
                "hint": "5 groups of 10 equal 50. Add 2 singles.",
                "explanation": "5 tens (50) plus 2 ones (2) equals 52 sweets.",
                "solution_steps": {
                    "step1": "Calculate 5 groups of 10 = 50.",
                    "step2": "Add the 2 loose sweets: 50 + 2 = 52.",
                    "step3": "The exact count is 52 sweets."
                }
            }
        ]
    },

    # Slide 18: Challenge 2 (Snakes & Ladders, Talking Pot, Defining & Making 100)
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Century Century Grid",
        "description": "Test your navigation of the 100-grid board, successor rules of the Talking Pot, and complementary pairs that total 100.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "On a 1 to 100 Snakes and Ladders board, what happens to your number when you move one square directly upwards?",
                "options": [
                    "The number increases by 10",
                    "The number increases by 1",
                    "The number is doubled",
                    "The number decreases by 10"
                ],
                "ans": "The number increases by 10",
                "hint": "Each row on the hundred-grid contains exactly 10 tiles.",
                "explanation": "Each horizontal row contains 10 numbers, so moving directly up one row adds 10 to the value.",
                "solution_steps": {
                    "step1": "Recall the 10x10 layout of the 1-100 board.",
                    "step2": "Moving up one row moves ahead by one full row of 10.",
                    "step3": "Conclude that the number increases by 10."
                }
            },
            {
                "id": "c2_q2",
                "q": "If your game token is on tile 37 and you land on a ladder that carries you up 20 spaces, what tile do you reach?",
                "options": [
                    "Tile 57 (37 + 20)",
                    "Tile 47",
                    "Tile 67",
                    "Tile 50"
                ],
                "ans": "Tile 57 (37 + 20)",
                "hint": "Add 20 to 37: 37 + 10 + 10.",
                "explanation": "37 + 20 = 57. The ladder carries the token to tile 57.",
                "solution_steps": {
                    "step1": "Identify the starting position (37).",
                    "step2": "Add the ladder advance: 37 + 20 = 57.",
                    "step3": "Select Tile 57."
                }
            },
            {
                "id": "c2_q3",
                "q": "What rule does the enchanted Talking Pot use to produce its output number?",
                "options": [
                    "It speaks the immediate successor (adds 1 to the input)",
                    "It multiplies the input by 2",
                    "It subtracts 10 from the input",
                    "It repeats the input backwards"
                ],
                "ans": "It speaks the immediate successor (adds 1 to the input)",
                "hint": "The Talking Pot always gives the next consecutive counting number.",
                "explanation": "The Talking Pot's rule is to state the immediate successor: input + 1.",
                "solution_steps": {
                    "step1": "Recall the Talking Pot activity rule from the chapter.",
                    "step2": "The pot always outputs the number that comes immediately next (n + 1).",
                    "step3": "Select 'It speaks the immediate successor (adds 1 to the input)'."
                }
            },
            {
                "id": "c2_q4",
                "q": "If the number 79 is dropped into the Talking Pot, what number will it announce?",
                "options": [
                    "80",
                    "78",
                    "89",
                    "70"
                ],
                "ans": "80",
                "hint": "What number comes immediately after 79?",
                "explanation": "79 + 1 = 80. The Talking Pot announces 80.",
                "solution_steps": {
                    "step1": "Input number = 79.",
                    "step2": "Apply the rule: 79 + 1 = 80.",
                    "step3": "The Talking Pot outputs 80."
                }
            },
            {
                "id": "c2_q5",
                "q": "What number must be added to 99 to make exactly 100?",
                "options": [
                    "1",
                    "10",
                    "0",
                    "2"
                ],
                "ans": "1",
                "hint": "100 is the immediate successor of 99.",
                "explanation": "99 + 1 = 100. Adding 1 to 99 completes the century.",
                "solution_steps": {
                    "step1": "Examine the equation: 99 + ___ = 100.",
                    "step2": "Subtract 99 from 100: 100 - 99 = 1.",
                    "step3": "The missing number is 1."
                }
            },
            {
                "id": "c2_q6",
                "q": "In sports terminology, especially cricket, what does scoring a 'century' mean?",
                "options": [
                    "Scoring 100 runs",
                    "Scoring 50 runs",
                    "Playing for 100 minutes",
                    "Hitting 10 sixes"
                ],
                "ans": "Scoring 100 runs",
                "hint": "Century comes from the Latin word 'centum', meaning 100.",
                "explanation": "In cricket, scoring a century means scoring exactly 100 runs in an innings.",
                "solution_steps": {
                    "step1": "Recall the cultural definition of a century.",
                    "step2": "A cricket century = 100 runs.",
                    "step3": "Select 'Scoring 100 runs'."
                }
            },
            {
                "id": "c2_q7",
                "q": "How many packets of 10 forehead bindis each are required to make 100 bindis?",
                "options": [
                    "10 packets",
                    "5 packets",
                    "20 packets",
                    "100 packets"
                ],
                "ans": "10 packets",
                "hint": "Count by tens: 10, 20, 30... up to 100.",
                "explanation": "10 packets x 10 bindis per packet = 100 bindis.",
                "solution_steps": {
                    "step1": "Divide 100 by 10.",
                    "step2": "100 / 10 = 10.",
                    "step3": "10 packets are required."
                }
            },
            {
                "id": "c2_q8",
                "q": "Which number completes the addition sentence: 75 + ___ = 100?",
                "options": [
                    "25",
                    "35",
                    "15",
                    "30"
                ],
                "ans": "25",
                "hint": "75 + 5 = 80, and 80 + 20 = 100.",
                "explanation": "75 + 25 = 100. Adding 25 to 75 yields exactly 100.",
                "solution_steps": {
                    "step1": "Start at 75 and jump 5 to reach 80.",
                    "step2": "Jump 20 from 80 to reach 100.",
                    "step3": "Combine the jumps: 20 + 5 = 25."
                }
            },
            {
                "id": "c2_q9",
                "q": "On a 100-bead string (ginladi), if 40 beads are on the left, how many beads are on the right?",
                "options": [
                    "60 beads (100 - 40)",
                    "50 beads",
                    "40 beads",
                    "70 beads"
                ],
                "ans": "60 beads (100 - 40)",
                "hint": "Subtract 40 from the total of 100 beads.",
                "explanation": "100 - 40 = 60 beads remaining on the right side.",
                "solution_steps": {
                    "step1": "Total beads on the ginladi = 100.",
                    "step2": "Subtract the left side beads: 100 - 40 = 60.",
                    "step3": "Select 60 beads."
                }
            },
            {
                "id": "c2_q10",
                "q": "If you take a number line jump from 0 to 65, how much further must you jump to reach 100?",
                "options": [
                    "35 units",
                    "45 units",
                    "25 units",
                    "30 units"
                ],
                "ans": "35 units",
                "hint": "Jump 5 to 70, then 30 to 100.",
                "explanation": "65 + 35 = 100. The remaining forward jump is 35 units.",
                "solution_steps": {
                    "step1": "Calculate distance from 65 to 70 (5 units).",
                    "step2": "Calculate distance from 70 to 100 (30 units).",
                    "step3": "Total forward distance: 5 + 30 = 35 units."
                }
            }
        ]
    },

    # Slide 19: Challenge 3 (Flower Petals, 101-124, Matchstick Bundles & Up to 150)
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Bundles & Beyond",
        "description": "Master flower petal sums, three-digit counting to 124, matchstick bundle hierarchies, and midpoints up to 150.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "In a flower petal puzzle with 100 at the center, one petal has 30. What number must be on its partner petal?",
                "options": [
                    "70 (30 + 70 = 100)",
                    "60",
                    "80",
                    "50"
                ],
                "ans": "70 (30 + 70 = 100)",
                "hint": "What number added to 30 makes 100?",
                "explanation": "30 + 70 = 100. The partner petal must contain 70.",
                "solution_steps": {
                    "step1": "Target center sum = 100.",
                    "step2": "Subtract known petal: 100 - 30 = 70.",
                    "step3": "The partner petal is 70."
                }
            },
            {
                "id": "c3_q2",
                "q": "In another flower puzzle with 100 at the center, a petal shows 50. What number belongs on its opposite petal?",
                "options": [
                    "50 (50 + 50 = 100)",
                    "40",
                    "60",
                    "100"
                ],
                "ans": "50 (50 + 50 = 100)",
                "hint": "What is half of 100?",
                "explanation": "50 + 50 = 100. Two equal petals of 50 total 100.",
                "solution_steps": {
                    "step1": "Target = 100.",
                    "step2": "100 - 50 = 50.",
                    "step3": "The opposite petal must hold 50."
                }
            },
            {
                "id": "c3_q3",
                "q": "How is 'one hundred and four' written in standard digits?",
                "options": [
                    "104",
                    "140",
                    "14",
                    "1004"
                ],
                "ans": "104",
                "hint": "1 hundred, 0 tens, and 4 ones.",
                "explanation": "One hundred and four has 1 in the hundreds place, 0 in the tens place, and 4 in the ones place: 104.",
                "solution_steps": {
                    "step1": "Identify hundreds digit = 1.",
                    "step2": "Identify tens digit = 0 (no tens mentioned).",
                    "step3": "Identify ones digit = 4. Number is 104."
                }
            },
            {
                "id": "c3_q4",
                "q": "What number is 'one hundred and ten' written in digits?",
                "options": [
                    "110",
                    "101",
                    "10010",
                    "11"
                ],
                "ans": "110",
                "hint": "100 + 10 = 110.",
                "explanation": "1 hundred and 1 ten with 0 ones is written as 110.",
                "solution_steps": {
                    "step1": "Add 100 + 10.",
                    "step2": "The sum is 110.",
                    "step3": "Select 110."
                }
            },
            {
                "id": "c3_q5",
                "q": "What number is formed by 1 master bundle of 100, 2 bundles of 10, and 3 loose matchsticks?",
                "options": [
                    "123",
                    "132",
                    "231",
                    "120"
                ],
                "ans": "123",
                "hint": "100 + 20 + 3.",
                "explanation": "1 hundred (100) + 2 tens (20) + 3 ones (3) = 123.",
                "solution_steps": {
                    "step1": "Hundreds: 1 x 100 = 100.",
                    "step2": "Tens: 2 x 10 = 20; Ones: 3 x 1 = 3.",
                    "step3": "Total = 100 + 20 + 3 = 123."
                }
            },
            {
                "id": "c3_q6",
                "q": "How many bundles of 10 matchsticks are inside 1 large master bundle of 100 matchsticks?",
                "options": [
                    "10 bundles of 10",
                    "5 bundles",
                    "20 bundles",
                    "100 bundles"
                ],
                "ans": "10 bundles of 10",
                "hint": "10 x 10 = 100.",
                "explanation": "10 bundles of 10 sticks each make up 1 large hundred-bundle.",
                "solution_steps": {
                    "step1": "Recall that 100 is composed of ten groups of ten.",
                    "step2": "Therefore, 10 bundles of 10 are tied together.",
                    "step3": "Select '10 bundles of 10'."
                }
            },
            {
                "id": "c3_q7",
                "q": "What number comes immediately after 139 in consecutive counting?",
                "options": [
                    "140",
                    "138",
                    "149",
                    "130"
                ],
                "ans": "140",
                "hint": "39 + 1 = 40, so 139 + 1 = 140.",
                "explanation": "The successor of 139 is 139 + 1 = 140.",
                "solution_steps": {
                    "step1": "Identify the number: 139.",
                    "step2": "Add 1: 139 + 1 = 140.",
                    "step3": "Select 140."
                }
            },
            {
                "id": "c3_q8",
                "q": "On a number line from 100 to 150, what number marks the exact halfway point?",
                "options": [
                    "125",
                    "120",
                    "130",
                    "135"
                ],
                "ans": "125",
                "hint": "Halfway between 0 and 50 is 25, so halfway between 100 and 150 is 100 + 25.",
                "explanation": "The span is 50 units; half is 25 units. 100 + 25 = 125.",
                "solution_steps": {
                    "step1": "Distance from 100 to 150 = 50.",
                    "step2": "Half of 50 = 25.",
                    "step3": "100 + 25 = 125."
                }
            },
            {
                "id": "c3_q9",
                "q": "What number is represented by 1 hundred-bundle, 4 ten-bundles, and 9 loose matchsticks?",
                "options": [
                    "149",
                    "194",
                    "140",
                    "159"
                ],
                "ans": "149",
                "hint": "100 + 40 + 9.",
                "explanation": "100 + 40 + 9 = 149.",
                "solution_steps": {
                    "step1": "1 hundred = 100.",
                    "step2": "4 tens = 40; 9 ones = 9.",
                    "step3": "Sum = 100 + 40 + 9 = 149."
                }
            },
            {
                "id": "c3_q10",
                "q": "If the Talking Pot is fed the number 123, what number will it speak?",
                "options": [
                    "124",
                    "122",
                    "133",
                    "125"
                ],
                "ans": "124",
                "hint": "Add 1 to 123.",
                "explanation": "123 + 1 = 124. The Talking Pot outputs the successor 124.",
                "solution_steps": {
                    "step1": "Input = 123.",
                    "step2": "Add 1: 123 + 1 = 124.",
                    "step3": "Select 124."
                }
            }
        ]
    },

    # Slide 20: Challenge 4 (Clap-Snap-Pat, Expanded Forms, Skips & Double Century)
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Double Century Summit",
        "description": "Solve auditory place-value codes, expanded notation, skip-counting leaps, and double-century multi-way models.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "In the Clap, Snap, and Pat game, what place value does one hand CLAP represent?",
                "options": [
                    "One hundred (100)",
                    "Ten (10)",
                    "One (1)",
                    "Zero (0)"
                ],
                "ans": "One hundred (100)",
                "hint": "The loudest sound represents the largest place value.",
                "explanation": "Clap = 100 (hundreds), Snap = 10 (tens), and Pat = 1 (ones).",
                "solution_steps": {
                    "step1": "Recall the game rules from Chapter 3.",
                    "step2": "Clap is assigned to the hundreds column (100).",
                    "step3": "Select 'One hundred (100)'."
                }
            },
            {
                "id": "c4_q2",
                "q": "A team performs 1 Clap, 5 Snaps, and 6 Pats. What number did they communicate?",
                "options": [
                    "156",
                    "165",
                    "516",
                    "150"
                ],
                "ans": "156",
                "hint": "1 Clap = 100, 5 Snaps = 50, 6 Pats = 6.",
                "explanation": "100 + 50 + 6 = 156 (one hundred fifty-six).",
                "solution_steps": {
                    "step1": "1 Clap = 100.",
                    "step2": "5 Snaps = 50; 6 Pats = 6.",
                    "step3": "Combine: 100 + 50 + 6 = 156."
                }
            },
            {
                "id": "c4_q3",
                "q": "What is the expanded form of the number 157?",
                "options": [
                    "100 + 50 + 7",
                    "10 + 50 + 7",
                    "150 + 70",
                    "1 + 5 + 7"
                ],
                "ans": "100 + 50 + 7",
                "hint": "Write the value of each digit separately: hundreds + tens + ones.",
                "explanation": "157 has 1 hundred (100), 5 tens (50), and 7 ones (7): 100 + 50 + 7.",
                "solution_steps": {
                    "step1": "Value of 1 in hundreds place = 100.",
                    "step2": "Value of 5 in tens place = 50; value of 7 in ones place = 7.",
                    "step3": "Expanded form = 100 + 50 + 7."
                }
            },
            {
                "id": "c4_q4",
                "q": "In the number 159, what is the place value of the digit 5?",
                "options": [
                    "50 (5 tens)",
                    "5 (5 ones)",
                    "500 (5 hundreds)",
                    "15"
                ],
                "ans": "50 (5 tens)",
                "hint": "The digit 5 is in the middle tens column.",
                "explanation": "The digit 5 in the tens column has a value of 5 x 10 = 50.",
                "solution_steps": {
                    "step1": "Identify the column of digit 5 (tens).",
                    "step2": "Multiply digit by its place value: 5 x 10 = 50.",
                    "step3": "Select 50 (5 tens)."
                }
            },
            {
                "id": "c4_q5",
                "q": "Starting at 100, if you take three consecutive forward jumps of 5 on a number line, what number do you reach?",
                "options": [
                    "115 (100 + 5 + 5 + 5)",
                    "110",
                    "120",
                    "105"
                ],
                "ans": "115 (100 + 5 + 5 + 5)",
                "hint": "100 -> 105 -> 110 -> 115.",
                "explanation": "Three jumps of 5 equal 3 x 5 = 15. 100 + 15 = 115.",
                "solution_steps": {
                    "step1": "Jump 1: 100 + 5 = 105.",
                    "step2": "Jump 2: 105 + 5 = 110; Jump 3: 110 + 5 = 115.",
                    "step3": "The landing number is 115."
                }
            },
            {
                "id": "c4_q6",
                "q": "If you start at 140 and leap forward by 20 on a number line, which milestone number do you land on?",
                "options": [
                    "160 (140 + 20)",
                    "150",
                    "170",
                    "180"
                ],
                "ans": "160 (140 + 20)",
                "hint": "14 tens + 2 tens = 16 tens.",
                "explanation": "140 + 20 = 160.",
                "solution_steps": {
                    "step1": "Start at 140.",
                    "step2": "Add 20: 140 + 20 = 160.",
                    "step3": "Select 160."
                }
            },
            {
                "id": "c4_q7",
                "q": "What numerical value corresponds to a 'Double Century'?",
                "options": [
                    "200 (Two Hundred)",
                    "100",
                    "150",
                    "300"
                ],
                "ans": "200 (Two Hundred)",
                "hint": "A single century is 100. Double means twice that amount.",
                "explanation": "A century is 100; a double century is 2 x 100 = 200.",
                "solution_steps": {
                    "step1": "Identify 1 century = 100.",
                    "step2": "Double century = 100 + 100 = 200.",
                    "step3": "Select 200 (Two Hundred)."
                }
            },
            {
                "id": "c4_q8",
                "q": "How many bundles of 10 matchsticks are needed to build the complete number 200?",
                "options": [
                    "20 bundles of 10",
                    "10 bundles of 10",
                    "2 bundles of 10",
                    "200 bundles of 10"
                ],
                "ans": "20 bundles of 10",
                "hint": "Divide 200 by 10.",
                "explanation": "20 bundles x 10 sticks per bundle = 200 matchsticks.",
                "solution_steps": {
                    "step1": "200 / 10 = 20.",
                    "step2": "Each bundle holds 10 sticks.",
                    "step3": "20 bundles of 10 are required."
                }
            },
            {
                "id": "c4_q9",
                "q": "How many large master hundred-bundles are needed to represent 200?",
                "options": [
                    "2 hundred-bundles",
                    "1 hundred-bundle",
                    "20 hundred-bundles",
                    "4 hundred-bundles"
                ],
                "ans": "2 hundred-bundles",
                "hint": "100 + 100 = 200.",
                "explanation": "Two bundles of 100 make 200.",
                "solution_steps": {
                    "step1": "1 master bundle = 100.",
                    "step2": "2 master bundles = 100 + 100 = 200.",
                    "step3": "Select 2 hundred-bundles."
                }
            },
            {
                "id": "c4_q10",
                "q": "Which action in Clap, Snap, and Pat would you perform to represent the hundreds in 200?",
                "options": [
                    "2 loud CLAPS (2 x 100)",
                    "2 finger SNAPS",
                    "2 thigh PATS",
                    "2 foot STOMPS"
                ],
                "ans": "2 loud CLAPS (2 x 100)",
                "hint": "Each Clap represents 100.",
                "explanation": "Each Clap represents 100. For 200, you perform 2 Claps with 0 Snaps and 0 Pats.",
                "solution_steps": {
                    "step1": "Identify the hundreds digit of 200 (2).",
                    "step2": "Recall that 1 Clap = 100.",
                    "step3": "To represent 200, perform 2 Claps."
                }
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 17 TO 20 (CHALLENGES) ===")
    assert len(slides_part3) == 4, f"Expected 4 challenge slides, got {len(slides_part3)}"
    
    total_q = 0
    for s in slides_part3:
        sid = s["id"]
        title = s["title"]
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        questions = s["questions"]
        assert len(questions) == 10, f"Slide {sid} must have exactly 10 questions, got {len(questions)}"
        total_q += len(questions)
        
        for q in questions:
            qid = q["id"]
            assert len(q["options"]) == 4, f"Question {qid} options != 4"
            assert q["ans"] in q["options"], f"Question {qid} ans '{q['ans']}' not in options!"
            assert "hint" in q and len(q["hint"]) > 5, f"Question {qid} missing hint!"
            assert "explanation" in q and len(q["explanation"]) > 5, f"Question {qid} missing explanation!"
            assert "solution_steps" in q, f"Question {qid} missing solution_steps!"
            steps = q["solution_steps"]
            assert "step1" in steps and "step2" in steps and "step3" in steps, f"Question {qid} missing steps 1-3!"
            
    print(f"Verified {len(slides_part3)} challenge slides with {total_q} questions successfully!")


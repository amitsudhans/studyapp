#!/usr/bin/env python3
"""
Generate NCERT Class 3 Mathematics - Chapter 12: Give and Take
Part 3: Slides 17 to 20 (Mastery Challenge Quizzes)
4 Slides × 10 Questions = 40 Questions
Each question has: id, question, options (4), answer (0-3), hint, explanation, solution_steps (3 steps).
Titles: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human character names. Zero teacher personas.
"""

slides_part3 = [
    # Slide 17: Challenge 1 (Tracks, Box Diagrams & HTO Addition)
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Animal track jumps, part-part-whole box diagrams, and HTO addition with regrouping",
        "questions": [
            {
                "question": "Starting at 48 on a segmented animal track, what number do you reach after taking a '+9' jump?",
                "options": ["57 (48 + 10 - 1)", "58", "56", "59"],
                "answer": 0,
                "hint": "Jump forward by 10 to reach 58, then step back by 1.",
                "explanation": "Adding 9 is the same as adding 10 and subtracting 1: 48 + 9 = 57.",
                "solution_steps": [
                    "Use the mental shortcut for adding 9: +9 = +10 - 1.",
                    "Add 10 to 48: 48 + 10 = 58.",
                    "Subtract 1: 58 - 1 = 57."
                ]
            },
            {
                "question": "Starting at 73, what number do you reach after making a '-9' jump?",
                "options": ["64 (73 - 10 + 1)", "63", "65", "62"],
                "answer": 0,
                "hint": "Step back by 10 to 63, then step forward by 1.",
                "explanation": "Subtracting 9 is equivalent to subtracting 10 and adding 1: 73 - 9 = 64.",
                "solution_steps": [
                    "Use the mental shortcut for subtracting 9: -9 = -10 + 1.",
                    "Subtract 10 from 73: 73 - 10 = 63.",
                    "Add 1: 63 + 1 = 64."
                ]
            },
            {
                "question": "A botanical nursery has 364 saplings and receives 52 more. What is the total count?",
                "options": ["416 saplings", "406 saplings", "426 saplings", "316 saplings"],
                "answer": 0,
                "hint": "Add 364 + 52 using column addition.",
                "explanation": "4 + 2 = 6 ones, 6 + 5 = 11 tens (1 ten, carry 100), 3 + 1 = 4 hundreds. Total = 416.",
                "solution_steps": [
                    "Add ones: 4 + 2 = 6 ones.",
                    "Add tens: 6 tens + 5 tens = 11 tens = 1 ten and carry over 1 hundred.",
                    "Add hundreds: 3 hundreds + 1 carried hundred = 4 hundreds. Total = 416."
                ]
            },
            {
                "question": "In a part-part-whole box diagram, the two parts are 245 and 130. What is the whole?",
                "options": ["375 (245 + 130)", "115", "370", "475"],
                "answer": 0,
                "hint": "Combine the two parts: Part 1 + Part 2 = Whole.",
                "explanation": "245 + 130 = 375.",
                "solution_steps": [
                    "Identify that the whole is the sum of both parts.",
                    "Add 245 and 130.",
                    "Calculate 245 + 130 = 375."
                ]
            },
            {
                "question": "When adding 10 tens in column addition, what do they regroup into?",
                "options": ["1 hundred", "10 hundreds", "1 ten", "1,000 ones"],
                "answer": 0,
                "hint": "10 × 10 = 100.",
                "explanation": "Ten tens equal 100, so they are bundled and carried over as 1 hundred.",
                "solution_steps": [
                    "Recall that place value groups in powers of 10.",
                    "Multiply 10 by 10: 10 × 10 = 100.",
                    "Conclude that 10 tens equal exactly 1 hundred."
                ]
            },
            {
                "question": "Starting at 215 on a number line, you take three +10 leaps and two +1 leaps. Where do you land?",
                "options": ["247 (215 + 30 + 2)", "237", "245", "257"],
                "answer": 0,
                "hint": "Add 30, then add 2.",
                "explanation": "215 + 30 = 245, then 245 + 2 = 247.",
                "solution_steps": [
                    "Calculate the tens leaps: 3 × 10 = 30.",
                    "Add tens to starting point: 215 + 30 = 245.",
                    "Add the two ones: 245 + 2 = 247."
                ]
            },
            {
                "question": "What is 478 + 6? (Solve by bridging through ten)",
                "options": ["484 (478 + 2 + 4)", "482", "486", "474"],
                "answer": 0,
                "hint": "Add 2 to reach 480, then add the remaining 4.",
                "explanation": "478 + 2 = 480, and 480 + 4 = 484.",
                "solution_steps": [
                    "Split 6 into 2 + 4 to bridge to the nearest multiple of ten.",
                    "Add 2 to 478: 478 + 2 = 480.",
                    "Add remaining 4: 480 + 4 = 484."
                ]
            },
            {
                "question": "A library has 185 Hindi books and 235 English books. What is the total number of books?",
                "options": ["420 books", "410 books", "430 books", "320 books"],
                "answer": 0,
                "hint": "Add 185 + 235.",
                "explanation": "5 + 5 = 10 (carry 1), 8 + 3 + 1 = 12 tens (carry 1), 1 + 2 + 1 = 4 hundreds. Total = 420.",
                "solution_steps": [
                    "Add ones: 5 + 5 = 10 (write 0, carry 1 ten).",
                    "Add tens: 8 + 3 + 1 = 12 tens (write 2, carry 1 hundred).",
                    "Add hundreds: 1 + 2 + 1 = 4 hundreds. Total = 420."
                ]
            },
            {
                "question": "What is the sum of 529 + 171?",
                "options": ["700 (529 + 171)", "690", "710", "600"],
                "answer": 0,
                "hint": "Notice that 29 + 71 = 100.",
                "explanation": "500 + 100 = 600, and 29 + 71 = 100. 600 + 100 = 700.",
                "solution_steps": [
                    "Group hundreds: 500 + 100 = 600.",
                    "Group remaining parts: 29 + 71 = 100.",
                    "Add components: 600 + 100 = 700."
                ]
            },
            {
                "question": "A nursery worker packs 140 rose saplings and 85 jasmine saplings. How many saplings in total?",
                "options": ["225 saplings", "215 saplings", "235 saplings", "125 saplings"],
                "answer": 0,
                "hint": "Add 140 + 85.",
                "explanation": "140 + 85 = 225 saplings.",
                "solution_steps": [
                    "Add ones: 0 + 5 = 5 ones.",
                    "Add tens: 4 tens + 8 tens = 12 tens = 2 tens and carry 1 hundred.",
                    "Add hundreds: 1 hundred + 1 carried hundred = 2 hundreds. Total = 225."
                ]
            }
        ]
    },

    # Slide 18: Challenge 2 (Subtraction with Regrouping & Grid Math)
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Borrowing across place values, missing-part word problems, and 500-range grid navigation",
        "questions": [
            {
                "question": "An order requires 230 saplings and 75 are already packed. How many more must be packed?",
                "options": ["155 saplings (230 - 75)", "165 saplings", "145 saplings", "175 saplings"],
                "answer": 0,
                "hint": "Subtract 75 from 230 with regrouping.",
                "explanation": "Borrowing: 10 - 5 = 5 ones; 12 tens - 7 tens = 5 tens; 1 hundred remaining. Total = 155.",
                "solution_steps": [
                    "Regroup 1 ten to ones: 10 - 5 = 5 ones.",
                    "Regroup 1 hundred to tens: 12 tens - 7 tens = 5 tens.",
                    "Bring down remaining 1 hundred: 155 saplings."
                ]
            },
            {
                "question": "What is 450 - 65?",
                "options": ["385", "375", "395", "415"],
                "answer": 0,
                "hint": "450 - 50 = 400, then 400 - 15 = 385.",
                "explanation": "450 - 65 = 385.",
                "solution_steps": [
                    "Subtract 50 first: 450 - 50 = 400.",
                    "Subtract remaining 15: 400 - 15 = 385.",
                    "Confirm: 385 + 65 = 450."
                ]
            },
            {
                "question": "In a school of 540 children, 315 are girls. How many boys are enrolled?",
                "options": ["225 boys (540 - 315)", "235 boys", "215 boys", "325 boys"],
                "answer": 0,
                "hint": "Total children (540) - girls (315) = boys.",
                "explanation": "540 - 315 = 225 boys.",
                "solution_steps": [
                    "Regroup: 10 - 5 = 5 ones.",
                    "Tens: 3 tens - 1 ten = 2 tens.",
                    "Hundreds: 5 hundreds - 3 hundreds = 2 hundreds. Total = 225."
                ]
            },
            {
                "question": "On a number grid with rows of 10, what operation corresponds to moving down 2 rows?",
                "options": ["Adding 20 (+20)", "Adding 2 (+2)", "Subtracting 20 (-20)", "Multiplying by 2"],
                "answer": 0,
                "hint": "Each row down adds 10.",
                "explanation": "Moving down 1 row adds 10, so moving down 2 rows adds 2 × 10 = 20.",
                "solution_steps": [
                    "Recall that each row consists of 10 numbers.",
                    "Moving down 1 row = +10.",
                    "Moving down 2 rows = +10 + 10 = +20."
                ]
            },
            {
                "question": "Using the number grid strategy, solve 481 + 19: move down 2 rows (+20) and step left 1 cell (-1). What is the answer?",
                "options": ["500 (481 + 20 - 1)", "499", "501", "510"],
                "answer": 0,
                "hint": "481 + 20 = 501, then 501 - 1 = 500.",
                "explanation": "481 + 19 = 481 + 20 - 1 = 501 - 1 = 500.",
                "solution_steps": [
                    "Decompose 19 as 20 - 1.",
                    "Add 20 to 481: 481 + 20 = 501.",
                    "Subtract 1: 501 - 1 = 500."
                ]
            },
            {
                "question": "What is 519 - 40 on a number grid?",
                "options": ["479 (jump up 4 rows)", "469", "489", "459"],
                "answer": 0,
                "hint": "Subtract 40 from 519.",
                "explanation": "Jumping up 4 rows subtracts 40: 519 - 40 = 479.",
                "solution_steps": [
                    "Moving up 1 row subtracts 10.",
                    "Moving up 4 rows subtracts 4 × 10 = 40.",
                    "Calculate 519 - 40 = 479."
                ]
            },
            {
                "question": "A warehouse holds 350 rice sacks. If 180 sacks are loaded onto a truck, how many sacks remain?",
                "options": ["170 sacks (350 - 180)", "180 sacks", "160 sacks", "270 sacks"],
                "answer": 0,
                "hint": "350 - 180 = 170.",
                "explanation": "350 - 180 = 170 sacks remaining in the warehouse.",
                "solution_steps": [
                    "Subtract 100: 350 - 100 = 250.",
                    "Subtract 80: 250 - 80 = 170.",
                    "Verify: 170 + 180 = 350."
                ]
            },
            {
                "question": "When borrowing 1 ten in place value subtraction, how many ones does it become?",
                "options": ["10 ones", "1 one", "100 ones", "5 ones"],
                "answer": 0,
                "hint": "1 ten equals 10 single units.",
                "explanation": "One ten unbundles into exactly 10 ones.",
                "solution_steps": [
                    "Recall the definition of a ten bundle.",
                    "Unbundling 1 ten yields 10 individual ones.",
                    "Conclude that 1 ten = 10 ones."
                ]
            },
            {
                "question": "What is 602 - 198? (Solve using mental compensation: subtract 200, then add 2)",
                "options": ["404 (602 - 200 + 2)", "402", "406", "394"],
                "answer": 0,
                "hint": "198 is 200 - 2.",
                "explanation": "602 - 200 = 402, then add 2 back = 404.",
                "solution_steps": [
                    "Round 198 to 200: compensation is +2.",
                    "Subtract 200: 602 - 200 = 402.",
                    "Add back 2: 402 + 2 = 404."
                ]
            },
            {
                "question": "In a subtraction box diagram, Whole = 400, Known Part = 125. What is the Missing Part?",
                "options": ["275 (400 - 125)", "285", "265", "525"],
                "answer": 0,
                "hint": "Subtract 125 from 400.",
                "explanation": "400 - 125 = 275.",
                "solution_steps": [
                    "Set up equation: Whole - Known Part = Missing Part.",
                    "Calculate 400 - 125.",
                    "Result = 275."
                ]
            }
        ]
    },

    # Slide 19: Challenge 3 (Barter, Currency & Shop Calculations)
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Economic barter history, currency note combinations, and shop earnings arithmetic",
        "questions": [
            {
                "question": "What problem occurred in the barter system when two traders did not desire each other's goods?",
                "options": [
                    "Lack of double coincidence of wants",
                    "Coins melting in the sun",
                    "Banknotes tearing easily",
                    "Taxes becoming too high"
                ],
                "answer": 0,
                "hint": "Both people had to want what the other person offered.",
                "explanation": "Trade could only happen if both parties happened to want what the other produced (double coincidence of wants).",
                "solution_steps": [
                    "Define barter: direct goods exchange.",
                    "Identify failure condition: when trader A has rice but wants pots, and trader B has cloth.",
                    "Name this classic limitation: lack of double coincidence of wants."
                ]
            },
            {
                "question": "Which combination of currency notes pays an exact bill of ₹180?",
                "options": [
                    "One ₹100 note + One ₹50 note + One ₹20 note + One ₹10 note",
                    "One ₹100 note + Two ₹50 notes",
                    "Two ₹100 notes",
                    "Three ₹50 notes"
                ],
                "answer": 0,
                "hint": "100 + 50 + 20 + 10 = 180.",
                "explanation": "₹100 + ₹50 + ₹20 + ₹10 = ₹180.",
                "solution_steps": [
                    "Add 100 + 50 = 150.",
                    "Add 20 = 170.",
                    "Add 10 = 180 exact."
                ]
            },
            {
                "question": "A village store opens with ₹465 cash in the drawer and closes with ₹756. What were the day's earnings?",
                "options": ["₹291 (756 - 465)", "₹281", "₹301", "₹1,221"],
                "answer": 0,
                "hint": "Subtract 465 from 756.",
                "explanation": "756 - 465 = 291 rupees earned from sales.",
                "solution_steps": [
                    "Ones: 6 - 5 = 1.",
                    "Tens: borrow 100 -> 15 tens - 6 tens = 9 tens.",
                    "Hundreds: 6 hundreds - 4 hundreds = 2 hundreds. Result = ₹291."
                ]
            },
            {
                "question": "How many ₹50 notes equal the value of a ₹500 banknote?",
                "options": ["10 notes (10 × 50 = 500)", "5 notes", "20 notes", "50 notes"],
                "answer": 0,
                "hint": "Divide 500 by 50.",
                "explanation": "500 ÷ 50 = 10 notes.",
                "solution_steps": [
                    "Recall value: 1 note = ₹50.",
                    "Calculate 10 notes: 10 × 50 = 500.",
                    "Conclude that 10 notes of ₹50 equal ₹500."
                ]
            },
            {
                "question": "You buy goods worth ₹340 and hand over a ₹500 note. How much change should you receive?",
                "options": ["₹160 (500 - 340)", "₹140", "₹260", "₹60"],
                "answer": 0,
                "hint": "Subtract 340 from 500.",
                "explanation": "500 - 340 = 160 rupees in change.",
                "solution_steps": [
                    "Set up change calculation: Paid amount - Cost = Change.",
                    "500 - 300 = 200.",
                    "200 - 40 = ₹160."
                ]
            },
            {
                "question": "A piggy bank contains three ₹100 notes, four ₹50 notes, and five ₹10 coins. What is the total savings?",
                "options": ["₹550 (300 + 200 + 50)", "₹500", "₹450", "₹600"],
                "answer": 0,
                "hint": "3 × 100 = 300; 4 × 50 = 200; 5 × 10 = 50.",
                "explanation": "300 + 200 + 50 = 550 rupees.",
                "solution_steps": [
                    "Value of ₹100 notes: 3 × 100 = 300.",
                    "Value of ₹50 notes: 4 × 50 = 200.",
                    "Value of ₹10 coins: 5 × 10 = 50. Total = 300 + 200 + 50 = ₹550."
                ]
            },
            {
                "question": "If an item costs ₹250, which combination pays the bill with the FEWEST number of notes?",
                "options": [
                    "One ₹200 note + One ₹50 note (2 notes)",
                    "Two ₹100 notes + One ₹50 note (3 notes)",
                    "Five ₹50 notes (5 notes)",
                    "Twenty-five ₹10 notes (25 notes)"
                ],
                "answer": 0,
                "hint": "Use the largest denomination notes available: ₹200 + ₹50.",
                "explanation": "₹200 + ₹50 uses only 2 notes, which is the minimum possible.",
                "solution_steps": [
                    "Identify available denominations: ₹200, ₹100, ₹50, etc.",
                    "Use largest note: ₹200.",
                    "Pay remaining ₹50 with one ₹50 note. Total = 2 notes."
                ]
            },
            {
                "question": "A merchant sells ₹320 of sugar in the morning and ₹280 of rice in the afternoon. What were total daily sales?",
                "options": ["₹600 (320 + 280)", "₹500", "₹700", "₹590"],
                "answer": 0,
                "hint": "320 + 280 = 600.",
                "explanation": "320 + 280 = 600 rupees.",
                "solution_steps": [
                    "Add hundreds: 300 + 200 = 500.",
                    "Add tens: 20 + 80 = 100.",
                    "Combine: 500 + 100 = ₹600."
                ]
            },
            {
                "question": "How many ₹20 notes are needed to make ₹100?",
                "options": ["5 notes (5 × 20 = 100)", "4 notes", "10 notes", "2 notes"],
                "answer": 0,
                "hint": "Count by twenties: 20, 40, 60, 80, 100.",
                "explanation": "5 × 20 = 100.",
                "solution_steps": [
                    "Count multiples of 20: 20, 40, 60, 80, 100.",
                    "Count the steps: 5 steps.",
                    "Conclude that 5 notes of ₹20 make ₹100."
                ]
            },
            {
                "question": "A shopper has one ₹500 note. Can they buy a shirt for ₹280 and trousers for ₹240?",
                "options": [
                    "No, because total is ₹520 (280 + 240 = 520 > 500)",
                    "Yes, with ₹20 change",
                    "Yes, with exactly ₹0 change",
                    "Cannot be determined"
                ],
                "answer": 0,
                "hint": "Add 280 + 240 and compare with 500.",
                "explanation": "280 + 240 = 520 rupees, which exceeds the available 500 rupees.",
                "solution_steps": [
                    "Calculate total purchase cost: 280 + 240 = 520.",
                    "Compare with available funds: 520 > 500.",
                    "Conclude the shopper is short by ₹20 and cannot buy both."
                ]
            }
        ]
    },

    # Slide 20: Challenge 4 (Estimation, Mental Logic & Digit Card Strategy)
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Rounding to nearest hundred, conceptual comparison, and digit card puzzle optimization",
        "questions": [
            {
                "question": "What is 468 rounded to the nearest hundred?",
                "options": ["500 (68 is greater than 50)", "400", "470", "450"],
                "answer": 0,
                "hint": "Look at the tens: 68 is 50 or greater, so round up.",
                "explanation": "Since 68 ≥ 50, 468 rounds up to the nearest hundred, 500.",
                "solution_steps": [
                    "Examine the tens and ones digits: 68.",
                    "Compare to the benchmark: 68 ≥ 50.",
                    "Round up to 500."
                ]
            },
            {
                "question": "Estimate 512 - 289 by rounding each number to the nearest hundred.",
                "options": ["200 (500 - 300)", "300", "100", "250"],
                "answer": 0,
                "hint": "512 rounds to 500; 289 rounds to 300.",
                "explanation": "500 - 300 = 200.",
                "solution_steps": [
                    "Round 512 to nearest hundred: 500.",
                    "Round 289 to nearest hundred: 300.",
                    "Subtract estimates: 500 - 300 = 200."
                ]
            },
            {
                "question": "Without calculating, which sum is GREATER: (420 + 260) or (420 + 290)?",
                "options": [
                    "420 + 290 (adding a larger addend to the same base produces a greater sum)",
                    "420 + 260",
                    "Both are equal",
                    "Cannot be determined without calculating"
                ],
                "answer": 0,
                "hint": "Both share the base 420. Compare 290 vs 260.",
                "explanation": "Since 290 > 260, 420 + 290 is greater.",
                "solution_steps": [
                    "Notice the common term: 420 in both expressions.",
                    "Compare the second terms: 290 > 260.",
                    "Conclude that 420 + 290 is greater."
                ]
            },
            {
                "question": "Without calculating, which difference is GREATER: (600 - 75) or (600 - 95)?",
                "options": [
                    "600 - 75 (taking away less leaves more remaining)",
                    "600 - 95",
                    "Both are equal",
                    "600 - 95 is greater"
                ],
                "answer": 0,
                "hint": "Subtracting a smaller number leaves a larger remainder.",
                "explanation": "75 < 95, so taking away 75 leaves more than taking away 95: 600 - 75 > 600 - 95.",
                "solution_steps": [
                    "Notice the common starting value: 600.",
                    "Compare the subtrahends: 75 < 95.",
                    "Conclude that subtracting the smaller amount leaves a greater result."
                ]
            },
            {
                "question": "Using digit cards 0, 1, 2, 3, 4, 5 once each, what is the MAXIMUM possible sum of two 3-digit numbers?",
                "options": ["951 (e.g. 531 + 420)", "941", "851", "960"],
                "answer": 0,
                "hint": "Put 5 and 4 in hundreds, 3 and 2 in tens, 1 and 0 in ones.",
                "explanation": "Hundreds: 5 + 4 = 900. Tens: 3 + 2 = 50. Ones: 1 + 0 = 1. Total = 951.",
                "solution_steps": [
                    "Place largest digits in hundreds: 5 and 4 (sum = 900).",
                    "Place next largest in tens: 3 and 2 (sum = 50).",
                    "Place smallest in ones: 1 and 0 (sum = 1). Grand total = 951."
                ]
            },
            {
                "question": "Starting at 269, what number results from adding 10?",
                "options": ["279 (only the tens digit increases)", "260", "369", "270"],
                "answer": 0,
                "hint": "Add 1 to the tens place (6 becomes 7).",
                "explanation": "Adding 10 increases only the tens place by 1: 269 + 10 = 279.",
                "solution_steps": [
                    "Identify the place value of 10: 1 ten.",
                    "Add 1 ten to the 6 tens in 269: 6 + 1 = 7 tens.",
                    "Keep ones (9) and hundreds (2) unchanged: 279."
                ]
            },
            {
                "question": "What is 454 + 100?",
                "options": ["554 (only the hundreds digit increases)", "464", "455", "544"],
                "answer": 0,
                "hint": "Add 1 to the hundreds place of 454.",
                "explanation": "4 hundreds + 1 hundred = 5 hundreds: 454 + 100 = 554.",
                "solution_steps": [
                    "Identify the place value: 100 operates on hundreds.",
                    "Add 1 to 4 in hundreds: 4 + 1 = 5 hundreds.",
                    "Keep tens and ones identical: 554."
                ]
            },
            {
                "question": "Which pair of expressions has the EXACT same value?",
                "options": [
                    "250 + 150 and 500 - 100 (both equal 400)",
                    "200 + 50 and 300 - 100",
                    "450 + 50 and 600 - 50",
                    "100 + 100 and 300 - 50"
                ],
                "answer": 0,
                "hint": "Check the value of both: 250 + 150 = 400, and 500 - 100 = 400.",
                "explanation": "250 + 150 = 400, and 500 - 100 = 400. Both equal 400.",
                "solution_steps": [
                    "Evaluate first expression: 250 + 150 = 400.",
                    "Evaluate second expression: 500 - 100 = 400.",
                    "Confirm both equal 400."
                ]
            },
            {
                "question": "Using digit cards 1, 2, 3, 4, 5, 6 once each, which two numbers yield the SMALLEST difference?",
                "options": [
                    "412 and 365 (consecutive hundreds: 4 and 3)",
                    "654 and 123",
                    "500 and 100",
                    "612 and 134"
                ],
                "answer": 0,
                "hint": "Choose consecutive digits for the hundreds place (like 4 and 3) to minimize difference.",
                "explanation": "Placing consecutive digits (4 and 3) in the hundreds place minimizes the gap between the two 3-digit numbers.",
                "solution_steps": [
                    "To minimize difference, the hundreds digits must be as close as possible (difference of 1).",
                    "Make the larger number have the smallest remaining digits (412).",
                    "Make the smaller number have the largest remaining digits (365): 412 - 365 = 47."
                ]
            },
            {
                "question": "What is the result of 700 - 350?",
                "options": ["350 (half of 700)", "450", "250", "300"],
                "answer": 0,
                "hint": "350 + 350 = 700.",
                "explanation": "700 - 350 = 350.",
                "solution_steps": [
                    "Notice that 350 is half of 700.",
                    "Subtracting half leaves the other half.",
                    "Calculate 700 - 350 = 350."
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

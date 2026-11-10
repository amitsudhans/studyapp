#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 7: Raksha Bandhan
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4)
Each Challenge contains 10 rigorous, curriculum-aligned questions (40 questions total).
Zero human character names.
Includes options, hint, explanation, and 3-step structured solutions.
"""

challenges = [
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Mastery Challenge on Grouping, Repeated Addition & Craft Calculations",
        "questions": [
            {
                "question": "A craftsperson needs 1 flower, 2 threads, and 4 beads for 1 wristband. How many beads are needed for 6 wristbands?",
                "options": ["20 beads", "24 beads", "28 beads", "32 beads"],
                "answer": 1,
                "hint": "Multiply 6 wristbands by 4 beads per wristband.",
                "explanation": "6 × 4 = 24 beads are needed for 6 wristbands.",
                "solution_steps": [
                    "Step 1: Identify beads needed per wristband = 4.",
                    "Step 2: Multiply by total wristbands to make = 6 × 4.",
                    "Step 3: 6 × 4 = 24. Therefore, 24 beads are required."
                ]
            },
            {
                "question": "Which repeated addition sentence matches the multiplication equation 4 × 5 = 20?",
                "options": ["4 + 4 + 4 + 4", "5 + 5 + 5 + 5", "4 + 5 + 4 + 5", "5 + 5 + 5 + 5 + 5"],
                "answer": 1,
                "hint": "4 × 5 means 4 groups of 5 added together.",
                "explanation": "Four groups of 5 added together is 5 + 5 + 5 + 5 = 20.",
                "solution_steps": [
                    "Step 1: Understand that 4 × 5 means 4 groups of 5.",
                    "Step 2: Write 5 added 4 times: 5 + 5 + 5 + 5.",
                    "Step 3: 5 + 5 + 5 + 5 = 20. Option B is correct."
                ]
            },
            {
                "question": "If 1 decorative garland requires 8 marigold flowers, how many flowers are needed to craft 5 identical garlands?",
                "options": ["35 flowers", "40 flowers", "45 flowers", "48 flowers"],
                "answer": 1,
                "hint": "Calculate 5 groups of 8: 5 × 8.",
                "explanation": "5 × 8 = 40 flowers are required.",
                "solution_steps": [
                    "Step 1: Flowers per garland = 8.",
                    "Step 2: Number of garlands = 5.",
                    "Step 3: Total flowers = 5 × 8 = 40."
                ]
            },
            {
                "question": "A box has 36 beads. If each wristband takes 4 beads, how many complete wristbands can be made?",
                "options": ["7 wristbands", "8 wristbands", "9 wristbands", "10 wristbands"],
                "answer": 2,
                "hint": "Divide 36 by 4: 36 ÷ 4.",
                "explanation": "36 ÷ 4 = 9 complete wristbands can be assembled.",
                "solution_steps": [
                    "Step 1: Total beads available = 36.",
                    "Step 2: Beads needed per wristband = 4.",
                    "Step 3: Compute 36 ÷ 4 = 9 wristbands."
                ]
            },
            {
                "question": "What is the total number of satin threads needed for 9 wristbands if each wristband requires 2 threads?",
                "options": ["14 threads", "16 threads", "18 threads", "20 threads"],
                "answer": 2,
                "hint": "Multiply 9 by 2: 9 × 2.",
                "explanation": "9 × 2 = 18 satin threads in total.",
                "solution_steps": [
                    "Step 1: Threads per wristband = 2.",
                    "Step 2: Multiply by 9 wristbands = 9 × 2.",
                    "Step 3: 9 × 2 = 18 threads."
                ]
            },
            {
                "question": "Which multiplication expression represents adding seven 6s together (6 + 6 + 6 + 6 + 6 + 6 + 6)?",
                "options": ["6 × 6", "7 × 6", "7 + 6", "6 × 8"],
                "answer": 1,
                "hint": "Count how many times 6 is added: 7 times.",
                "explanation": "Adding 6 seven times is written as 7 × 6 = 42.",
                "solution_steps": [
                    "Step 1: Identify the repeated number = 6.",
                    "Step 2: Count the number of terms = 7.",
                    "Step 3: Write as multiplication: 7 × 6 = 42."
                ]
            },
            {
                "question": "If 8 gift packets each hold 3 sweets, how many sweets are there in total?",
                "options": ["21 sweets", "24 sweets", "27 sweets", "30 sweets"],
                "answer": 1,
                "hint": "Compute 8 × 3.",
                "explanation": "8 packets × 3 sweets each = 24 sweets.",
                "solution_steps": [
                    "Step 1: Number of packets = 8.",
                    "Step 2: Sweets per packet = 3.",
                    "Step 3: Total sweets = 8 × 3 = 24."
                ]
            },
            {
                "question": "A craft kit contains 50 beads. If you make 10 wristbands using 4 beads each, how many beads remain?",
                "options": ["8 beads", "10 beads", "12 beads", "14 beads"],
                "answer": 1,
                "hint": "Find beads used (10 × 4 = 40), then subtract from 50.",
                "explanation": "10 × 4 = 40 beads used. 50 - 40 = 10 beads left.",
                "solution_steps": [
                    "Step 1: Total beads used = 10 × 4 = 40 beads.",
                    "Step 2: Subtract used beads from initial total: 50 - 40.",
                    "Step 3: 50 - 40 = 10 beads remaining."
                ]
            },
            {
                "question": "Which of the following equals 3 × 8?",
                "options": ["8 + 8 + 8", "3 + 3 + 3", "8 + 3", "3 × 3 × 3"],
                "answer": 0,
                "hint": "3 groups of 8 means adding 8 three times.",
                "explanation": "3 × 8 means 3 groups of 8, which is 8 + 8 + 8 = 24.",
                "solution_steps": [
                    "Step 1: Understand 3 × 8 as 3 groups of 8.",
                    "Step 2: Write as repeated addition: 8 + 8 + 8.",
                    "Step 3: 8 + 8 + 8 = 24, which matches 3 × 8."
                ]
            },
            {
                "question": "To make 7 wristbands, each needing 1 flower, 2 threads, and 4 beads, how many total items must be gathered?",
                "options": ["42 items", "49 items", "56 items", "63 items"],
                "answer": 1,
                "hint": "Each wristband uses 1 + 2 + 4 = 7 items. Multiply 7 by 7.",
                "explanation": "7 items per wristband × 7 wristbands = 49 items.",
                "solution_steps": [
                    "Step 1: Items per wristband = 1 + 2 + 4 = 7 items.",
                    "Step 2: Number of wristbands = 7.",
                    "Step 3: Total items = 7 × 7 = 49 items."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Mastery Challenge on Rectangular Arrays, Sweet Box Grids & Equal Sharing",
        "questions": [
            {
                "question": "A sweet box contains 5 rows of laddoos with 4 laddoos in each row. How many laddoos are in the box?",
                "options": ["16 laddoos", "20 laddoos", "24 laddoos", "25 laddoos"],
                "answer": 1,
                "hint": "Multiply rows by columns: 5 × 4.",
                "explanation": "5 rows × 4 laddoos per row = 20 laddoos.",
                "solution_steps": [
                    "Step 1: Number of rows = 5.",
                    "Step 2: Laddoos in each row = 4.",
                    "Step 3: Total laddoos = 5 × 4 = 20."
                ]
            },
            {
                "question": "Which of these arrays does NOT contain exactly 24 sweets?",
                "options": ["3 rows of 8", "4 rows of 6", "2 rows of 12", "5 rows of 5"],
                "answer": 3,
                "hint": "Check the products: 3×8=24, 4×6=24, 2×12=24, 5×5=25.",
                "explanation": "5 × 5 = 25, not 24.",
                "solution_steps": [
                    "Step 1: Evaluate 3 × 8 = 24, 4 × 6 = 24, 2 × 12 = 24.",
                    "Step 2: Evaluate 5 × 5 = 25.",
                    "Step 3: 5 rows of 5 equals 25 sweets, which is not 24."
                ]
            },
            {
                "question": "24 pedas are shared equally among 6 children. How many pedas does each child receive?",
                "options": ["3 pedas", "4 pedas", "5 pedas", "6 pedas"],
                "answer": 1,
                "hint": "Divide 24 by 6: 24 ÷ 6.",
                "explanation": "24 ÷ 6 = 4 pedas per child.",
                "solution_steps": [
                    "Step 1: Total pedas = 24.",
                    "Step 2: Number of children = 6.",
                    "Step 3: Calculate 24 ÷ 6 = 4 pedas."
                ]
            },
            {
                "question": "In the division statement 35 ÷ 7 = 5, what is the number 7 called?",
                "options": ["Dividend", "Divisor", "Quotient", "Product"],
                "answer": 1,
                "hint": "The number doing the dividing is the divisor.",
                "explanation": "In 35 ÷ 7 = 5, 35 is the dividend, 7 is the divisor, and 5 is the quotient.",
                "solution_steps": [
                    "Step 1: Identify the roles: [Dividend] ÷ [Divisor] = [Quotient].",
                    "Step 2: The number 7 is the dividing number.",
                    "Step 3: Therefore, 7 is the divisor."
                ]
            },
            {
                "question": "A baker packs 30 pastries into boxes holding 6 pastries each. How many boxes are completely filled?",
                "options": ["4 boxes", "5 boxes", "6 boxes", "7 boxes"],
                "answer": 1,
                "hint": "Divide 30 by 6: 30 ÷ 6.",
                "explanation": "30 ÷ 6 = 5 boxes.",
                "solution_steps": [
                    "Step 1: Total pastries = 30.",
                    "Step 2: Capacity per box = 6.",
                    "Step 3: Compute 30 ÷ 6 = 5 boxes."
                ]
            },
            {
                "question": "How many 2-wheeled bicycles can be equipped with 18 wheels?",
                "options": ["8 bicycles", "9 bicycles", "10 bicycles", "11 bicycles"],
                "answer": 1,
                "hint": "Divide 18 wheels by 2 wheels per bicycle.",
                "explanation": "18 ÷ 2 = 9 bicycles.",
                "solution_steps": [
                    "Step 1: Total wheels = 18.",
                    "Step 2: Wheels per bicycle = 2.",
                    "Step 3: 18 ÷ 2 = 9 complete bicycles."
                ]
            },
            {
                "question": "If 32 spiral jalebis are packed in plates of 4, how many plates are needed?",
                "options": ["6 plates", "7 plates", "8 plates", "9 plates"],
                "answer": 2,
                "hint": "Calculate 32 ÷ 4.",
                "explanation": "32 ÷ 4 = 8 plates.",
                "solution_steps": [
                    "Step 1: Total jalebis = 32.",
                    "Step 2: Jalebis per plate = 4.",
                    "Step 3: 32 ÷ 4 = 8 plates."
                ]
            },
            {
                "question": "A farmer plants 7 rows of cabbage with 6 cabbages in each row. How many cabbages are planted in total?",
                "options": ["36 cabbages", "40 cabbages", "42 cabbages", "48 cabbages"],
                "answer": 2,
                "hint": "Multiply rows by count per row: 7 × 6.",
                "explanation": "7 × 6 = 42 cabbages.",
                "solution_steps": [
                    "Step 1: Rows = 7.",
                    "Step 2: Cabbages per row = 6.",
                    "Step 3: Total = 7 × 6 = 42 cabbages."
                ]
            },
            {
                "question": "If 45 sweets are distributed equally among 9 plates, how many sweets are on each plate?",
                "options": ["4 sweets", "5 sweets", "6 sweets", "7 sweets"],
                "answer": 1,
                "hint": "Divide 45 by 9: 45 ÷ 9.",
                "explanation": "45 ÷ 9 = 5 sweets per plate.",
                "solution_steps": [
                    "Step 1: Total sweets = 45.",
                    "Step 2: Plates = 9.",
                    "Step 3: 45 ÷ 9 = 5 sweets."
                ]
            },
            {
                "question": "Which equation verifies that 36 divided by 4 equals 9?",
                "options": ["36 + 4 = 40", "4 × 9 = 36", "36 - 9 = 27", "9 + 4 = 13"],
                "answer": 1,
                "hint": "Multiplication is the inverse of division: divisor × quotient = dividend.",
                "explanation": "Because 4 × 9 = 36, it directly verifies that 36 ÷ 4 = 9.",
                "solution_steps": [
                    "Step 1: Recall inverse operations: if a ÷ b = c, then b × c = a.",
                    "Step 2: For 36 ÷ 4 = 9, the inverse is 4 × 9 = 36.",
                    "Step 3: Option B correctly confirms the division."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Mastery Challenge on Commutative Law, Tables Construction & Number Tracks",
        "questions": [
            {
                "question": "Which property states that 6 × 8 is always equal to 8 × 6?",
                "options": ["Additive property", "Commutative property", "Division property", "Zero property"],
                "answer": 1,
                "hint": "The property where changing factor order preserves the product.",
                "explanation": "The commutative property of multiplication states that changing the order of factors does not change the product.",
                "solution_steps": [
                    "Step 1: Note that 6 × 8 = 48 and 8 × 6 = 48.",
                    "Step 2: The order of factors has swapped without changing the result.",
                    "Step 3: This is the commutative property of multiplication."
                ]
            },
            {
                "question": "A jumper starts at 0 and takes 8 jumps of 3 steps each on a number track. What number does the jumper land on?",
                "options": ["21", "24", "27", "30"],
                "answer": 1,
                "hint": "Multiply 8 jumps by 3 steps: 8 × 3.",
                "explanation": "8 × 3 = 24.",
                "solution_steps": [
                    "Step 1: Number of jumps = 8.",
                    "Step 2: Size of each jump = 3.",
                    "Step 3: Landing point = 8 × 3 = 24."
                ]
            },
            {
                "question": "Starting at 0 on a number track, how many jumps of 4 steps are required to reach 36?",
                "options": ["7 jumps", "8 jumps", "9 jumps", "10 jumps"],
                "answer": 2,
                "hint": "Divide 36 by 4: 36 ÷ 4.",
                "explanation": "36 ÷ 4 = 9 jumps.",
                "solution_steps": [
                    "Step 1: Target stone = 36.",
                    "Step 2: Step length = 4.",
                    "Step 3: 36 ÷ 4 = 9 jumps."
                ]
            },
            {
                "question": "What is the common multiple of 4 and 6 between 10 and 20?",
                "options": ["12", "14", "16", "18"],
                "answer": 0,
                "hint": "Find a number in that range divisible by both 4 and 6.",
                "explanation": "12 is 4 × 3 and 6 × 2, so 12 is a common multiple.",
                "solution_steps": [
                    "Step 1: Multiples of 4 between 10 and 20: 12, 16.",
                    "Step 2: Multiples of 6 between 10 and 20: 12, 18.",
                    "Step 3: The common number is 12."
                ]
            },
            {
                "question": "If 6 horizontal sticks are crossed by 5 vertical sticks, how many intersection dots are formed?",
                "options": ["25 dots", "30 dots", "35 dots", "36 dots"],
                "answer": 1,
                "hint": "Multiply horizontal sticks by vertical sticks: 6 × 5.",
                "explanation": "6 × 5 = 30 intersection dots.",
                "solution_steps": [
                    "Step 1: Number of horizontal sticks = 6.",
                    "Step 2: Number of vertical sticks = 5.",
                    "Step 3: Total intersections = 6 × 5 = 30."
                ]
            },
            {
                "question": "What is the units digit of any product in the 5-times table when multiplied by an even number?",
                "options": ["5", "0", "2", "4"],
                "answer": 1,
                "hint": "Check 5×2=10, 5×4=20, 5×6=30, 5×8=40.",
                "explanation": "5 multiplied by any even number always ends in 0.",
                "solution_steps": [
                    "Step 1: Test products: 5 × 2 = 10, 5 × 4 = 20, 5 × 6 = 30.",
                    "Step 2: Observe the last digit in each product.",
                    "Step 3: The units digit is always 0."
                ]
            },
            {
                "question": "If you add the 2-times table and the 5-times table together, which table do you produce?",
                "options": ["The 6-times table", "The 7-times table", "The 10-times table", "The 8-times table"],
                "answer": 1,
                "hint": "Add the base table values: 2 + 5 = 7.",
                "explanation": "Because 2 + 5 = 7, adding the 2-times and 5-times tables gives the 7-times table.",
                "solution_steps": [
                    "Step 1: Recall the additive property of tables: (a × n) + (b × n) = (a + b) × n.",
                    "Step 2: Here a = 2 and b = 5, so a + b = 7.",
                    "Step 3: This produces the 7-times table."
                ]
            },
            {
                "question": "What is the value of 9 × 6?",
                "options": ["48", "52", "54", "56"],
                "answer": 2,
                "hint": "Compute (9 × 5) + 9 = 45 + 9 = 54.",
                "explanation": "9 × 6 = 54.",
                "solution_steps": [
                    "Step 1: Compute 9 × 5 = 45.",
                    "Step 2: Add one more 9: 45 + 9 = 54.",
                    "Step 3: 9 × 6 = 54."
                ]
            },
            {
                "question": "A frog leaps 4 meters per jump. How many meters has it traveled after 7 jumps?",
                "options": ["24 meters", "28 meters", "32 meters", "36 meters"],
                "answer": 1,
                "hint": "Multiply 7 jumps by 4 meters: 7 × 4.",
                "explanation": "7 × 4 = 28 meters.",
                "solution_steps": [
                    "Step 1: Distance per leap = 4 meters.",
                    "Step 2: Number of leaps = 7.",
                    "Step 3: Total distance = 7 × 4 = 28 meters."
                ]
            },
            {
                "question": "Which number is missing in the sequence: 6, 12, 18, __, 30, 36?",
                "options": ["20", "22", "24", "26"],
                "answer": 2,
                "hint": "This is skip-counting by 6: 18 + 6 = ?",
                "explanation": "The sequence increments by 6. 18 + 6 = 24.",
                "solution_steps": [
                    "Step 1: Find step difference: 12 - 6 = 6, 18 - 12 = 6.",
                    "Step 2: Add 6 to 18: 18 + 6 = 24.",
                    "Step 3: Check next: 24 + 6 = 30. The missing number is 24."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Mastery Challenge on Repeated Subtraction, Real-World Problems & Mystery Cards",
        "questions": [
            {
                "question": "A crafter has 140 sea-shells and uses 28 shells for each necklace. How many necklaces can be made?",
                "options": ["4 necklaces", "5 necklaces", "6 necklaces", "7 necklaces"],
                "answer": 1,
                "hint": "Calculate 140 ÷ 28 or subtract 28 repeatedly.",
                "explanation": "140 ÷ 28 = 5 necklaces.",
                "solution_steps": [
                    "Step 1: Total shells = 140.",
                    "Step 2: Shells per necklace = 28.",
                    "Step 3: 28 × 5 = 140, so exactly 5 necklaces can be crafted."
                ]
            },
            {
                "question": "How many 20-rupee notes are needed to make a total of 100 rupees?",
                "options": ["4 notes", "5 notes", "6 notes", "10 notes"],
                "answer": 1,
                "hint": "Divide 100 by 20: 100 ÷ 20.",
                "explanation": "100 ÷ 20 = 5 notes.",
                "solution_steps": [
                    "Step 1: Total amount = 100 rupees.",
                    "Step 2: Value per note = 20 rupees.",
                    "Step 3: 100 ÷ 20 = 5 notes."
                ]
            },
            {
                "question": "An envelope has a target product of 28. Which two number cards from 1 to 10 multiply to unlock it?",
                "options": ["3 and 9", "4 and 7", "5 and 6", "2 and 12"],
                "answer": 1,
                "hint": "Find which numbers from 1 to 10 give 28 when multiplied.",
                "explanation": "4 × 7 = 28, and both 4 and 7 are within 1 to 10.",
                "solution_steps": [
                    "Step 1: Target product = 28.",
                    "Step 2: Factor pairs: 1 × 28, 2 × 14, 4 × 7.",
                    "Step 3: Only 4 and 7 are both in the deck 1 to 10. Thus, cards 4 and 7 unlock it."
                ]
            },
            {
                "question": "If you buy 4 wall-hangings at 25 rupees each, what is the total cost?",
                "options": ["75 rupees", "90 rupees", "100 rupees", "125 rupees"],
                "answer": 2,
                "hint": "Multiply 4 by 25: 4 × 25.",
                "explanation": "4 × 25 = 100 rupees.",
                "solution_steps": [
                    "Step 1: Cost per wall-hanging = 25 rupees.",
                    "Step 2: Number of wall-hangings = 4.",
                    "Step 3: Total cost = 4 × 25 = 100 rupees."
                ]
            },
            {
                "question": "A mystery envelope has the target product 56. Which two cards from 1 to 10 unlock it?",
                "options": ["6 and 9", "7 and 8", "6 and 8", "5 and 11"],
                "answer": 1,
                "hint": "7 times 8 equals 56.",
                "explanation": "Cards 7 and 8 multiply to 7 × 8 = 56.",
                "solution_steps": [
                    "Step 1: Target product = 56.",
                    "Step 2: Find two cards between 1 and 10: 7 × 8 = 56.",
                    "Step 3: Cards 7 and 8 unlock the envelope."
                ]
            },
            {
                "question": "If 72 shiny pebbles are divided equally among 8 friends, how many pebbles does each friend receive?",
                "options": ["7 pebbles", "8 pebbles", "9 pebbles", "10 pebbles"],
                "answer": 2,
                "hint": "Divide 72 by 8: 72 ÷ 8.",
                "explanation": "72 ÷ 8 = 9 pebbles per friend.",
                "solution_steps": [
                    "Step 1: Total pebbles = 72.",
                    "Step 2: Number of friends = 8.",
                    "Step 3: 72 ÷ 8 = 9 pebbles."
                ]
            },
            {
                "question": "How many cups of sweet rabdi costing 15 rupees each can be bought with 60 rupees?",
                "options": ["3 cups", "4 cups", "5 cups", "6 cups"],
                "answer": 1,
                "hint": "Divide 60 by 15: 60 ÷ 15.",
                "explanation": "60 ÷ 15 = 4 cups.",
                "solution_steps": [
                    "Step 1: Total money available = 60 rupees.",
                    "Step 2: Price per cup = 15 rupees.",
                    "Step 3: 60 ÷ 15 = 4 cups."
                ]
            },
            {
                "question": "Which two cards from 1 to 10 unlock an envelope stamped with 63?",
                "options": ["6 and 9", "7 and 9", "8 and 8", "7 and 8"],
                "answer": 1,
                "hint": "7 times 9 equals 63.",
                "explanation": "7 × 9 = 63, unlocking the envelope.",
                "solution_steps": [
                    "Step 1: Target product = 63.",
                    "Step 2: Check factor pairs: 7 × 9 = 63.",
                    "Step 3: Cards 7 and 9 are both valid deck cards."
                ]
            },
            {
                "question": "A cookie jar has 48 cookies. If each child receives 6 cookies, how many children receive cookies?",
                "options": ["6 children", "7 children", "8 children", "9 children"],
                "answer": 2,
                "hint": "Divide 48 by 6: 48 ÷ 6.",
                "explanation": "48 ÷ 6 = 8 children.",
                "solution_steps": [
                    "Step 1: Total cookies = 48.",
                    "Step 2: Cookies per child = 6.",
                    "Step 3: 48 ÷ 6 = 8 children."
                ]
            },
            {
                "question": "If you save 10 rupees every day for 8 days, how much money have you saved in total?",
                "options": ["70 rupees", "80 rupees", "90 rupees", "100 rupees"],
                "answer": 1,
                "hint": "Multiply 8 days by 10 rupees per day: 8 × 10.",
                "explanation": "8 × 10 = 80 rupees saved.",
                "solution_steps": [
                    "Step 1: Daily savings = 10 rupees.",
                    "Step 2: Number of days = 8.",
                    "Step 3: Total saved = 8 × 10 = 80 rupees."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    for c in challenges:
        print(f"Slide {c['id']}: '{c['title']}' ({len(c['title'].split())} words) -> Questions: {len(c['questions'])}")
        assert len(c["title"].split()) <= 3
        assert len(c["questions"]) == 10
        for i, q in enumerate(c["questions"]):
            assert len(q["options"]) == 4, f"Slide {c['id']} Q{i+1} options count != 4"
            assert 0 <= q["answer"] <= 3, f"Slide {c['id']} Q{i+1} answer out of range"
            assert "hint" in q and len(q["hint"]) > 0
            assert "explanation" in q and len(q["explanation"]) > 0
            assert "solution_steps" in q and len(q["solution_steps"]) == 3
    print("Part 3 (Challenges 1-4) verified successfully!")

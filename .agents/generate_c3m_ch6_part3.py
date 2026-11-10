# -*- coding: utf-8 -*-
"""Part 3 (Slides 17-20: 4 Challenges × 10 Questions = 40 Questions) for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""

import json
import re

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Mastery Quiz 1",
        "description": "Test your mastery of counting torans in tens, crossing 300, and tiled number paths.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "How many groups of 10 triangular torans are required to count up to 250 torans?",
                "options": ["25 groups of 10", "20 groups of 10", "15 groups of 10", "30 groups of 10"],
                "ans": "25 groups of 10",
                "hint": "Divide 250 by 10 to find how many tens it contains.",
                "explanation": "250 divided by 10 equals 25 groups of 10.",
                "solution_steps": [
                    "Step 1: Recognize that each decorative string holds 10 triangular torans.",
                    "Step 2: Calculate how many tens are in 250: 250 ÷ 10 = 25.",
                    "Step 3: Conclude that 25 groups of 10 equal 250 torans."
                ]
            },
            {
                "id": "c1_q2",
                "q": "What number is reached when 1 single toffee is added to a box holding 299 toffees?",
                "options": ["300", "2910", "298", "301"],
                "ans": "300",
                "hint": "Add 1 to 299 to reach the third century milestone.",
                "explanation": "299 + 1 = 300.",
                "solution_steps": [
                    "Step 1: Start with the baseline count of 299.",
                    "Step 2: Add 1 unit: 9 ones + 1 one = 10 ones (regroups to 1 ten), 9 tens + 1 ten = 10 tens (regroups to 1 hundred).",
                    "Step 3: Combine with existing 2 hundreds: 200 + 100 = 300."
                ]
            },
            {
                "id": "c1_q3",
                "q": "Which missing number completes the consecutive stone path: 212, 213, ____, 215?",
                "options": ["214", "216", "224", "204"],
                "ans": "214",
                "hint": "Find the consecutive integer between 213 and 215.",
                "explanation": "213 + 1 = 214, which directly precedes 215.",
                "solution_steps": [
                    "Step 1: Observe that the sequence increases by 1 at each stepping stone.",
                    "Step 2: Add 1 to 213: 213 + 1 = 214.",
                    "Step 3: Verify that 214 + 1 = 215, confirming 214 is the missing stone."
                ]
            },
            {
                "id": "c1_q4",
                "q": "What total number is represented by 28 display rods holding 10 glass bangles each?",
                "options": ["280 bangles", "208 bangles", "288 bangles", "300 bangles"],
                "ans": "280 bangles",
                "hint": "Multiply 28 by 10.",
                "explanation": "28 × 10 = 280 bangles.",
                "solution_steps": [
                    "Step 1: Identify the number of rods: 28.",
                    "Step 2: Multiply by 10 bangles per rod: 28 × 10 = 280.",
                    "Step 3: Conclude that 28 rods hold 280 bangles."
                ]
            },
            {
                "id": "c1_q5",
                "q": "Which number is described by the verbal sentence '15 less than 250'?",
                "options": ["235", "245", "265", "225"],
                "ans": "235",
                "hint": "Subtract 15 from 250.",
                "explanation": "250 - 15 = 235.",
                "solution_steps": [
                    "Step 1: Start with 250.",
                    "Step 2: Subtract 10 first: 250 - 10 = 240.",
                    "Step 3: Subtract remaining 5: 240 - 5 = 235."
                ]
            },
            {
                "id": "c1_q6",
                "q": "What number comes immediately before 300 on a number line?",
                "options": ["299", "298", "290", "200"],
                "ans": "299",
                "hint": "Subtract 1 from 300.",
                "explanation": "The predecessor of 300 is 300 - 1 = 299.",
                "solution_steps": [
                    "Step 1: Locate 300 on the number line.",
                    "Step 2: Step backward by 1 unit: 300 - 1 = 299.",
                    "Step 3: Confirm that 299 is the number immediately preceding 300."
                ]
            },
            {
                "id": "c1_q7",
                "q": "If you are on stone 295 and take 5 forward steps, which stone do you reach?",
                "options": ["300", "299", "305", "290"],
                "ans": "300",
                "hint": "Add 5 to 295.",
                "explanation": "295 + 5 = 300.",
                "solution_steps": [
                    "Step 1: Start at stone 295.",
                    "Step 2: Add 5: 295 + 5 = 300.",
                    "Step 3: You land exactly on milestone stone 300."
                ]
            },
            {
                "id": "c1_q8",
                "q": "How many tens are in the number 240?",
                "options": ["24 tens", "4 tens", "20 tens", "2 tens"],
                "ans": "24 tens",
                "hint": "Divide 240 by 10.",
                "explanation": "240 consists of 24 groups of 10.",
                "solution_steps": [
                    "Step 1: Break 240 into hundreds and tens: 2 hundreds (20 tens) + 4 tens.",
                    "Step 2: Add the tens together: 20 + 4 = 24 tens.",
                    "Step 3: Verify: 24 × 10 = 240."
                ]
            },
            {
                "id": "c1_q9",
                "q": "Which sequence correctly counts forward by tens starting from 210?",
                "options": ["210, 220, 230, 240, 250", "210, 211, 212, 213, 214", "210, 230, 250, 270, 290", "210, 310, 410, 510, 610"],
                "ans": "210, 220, 230, 240, 250",
                "hint": "Add 10 at each step.",
                "explanation": "Adding 10 successively gives 210, 220, 230, 240, 250.",
                "solution_steps": [
                    "Step 1: Start at 210.",
                    "Step 2: Add 10 repeatedly: 210+10=220, 220+10=230, 230+10=240, 240+10=250.",
                    "Step 3: Identify the matching option: 210, 220, 230, 240, 250."
                ]
            },
            {
                "id": "c1_q10",
                "q": "What number is '20 more than 280'?",
                "options": ["300", "290", "310", "282"],
                "ans": "300",
                "hint": "Add 20 to 280.",
                "explanation": "280 + 20 = 300.",
                "solution_steps": [
                    "Step 1: Start with 280.",
                    "Step 2: Add 20: 280 + 20 = 300.",
                    "Step 3: Conclude that 20 more than 280 is 300."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Mastery Quiz 2",
        "description": "Assess your skills with matchstick bundle notation, number line navigation, and The Flag Game.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "What number is represented by 2 bundles of 100, 4 bundles of 10, and 7 loose sticks?",
                "options": ["247", "274", "427", "240"],
                "ans": "247",
                "hint": "Combine 200 + 40 + 7.",
                "explanation": "200 + 40 + 7 = 247.",
                "solution_steps": [
                    "Step 1: Evaluate hundreds: 2 × 100 = 200.",
                    "Step 2: Evaluate tens: 4 × 10 = 40.",
                    "Step 3: Add ones: 200 + 40 + 7 = 247."
                ]
            },
            {
                "id": "c2_q2",
                "q": "Which number sits exactly halfway between 200 and 300 on an extended number line?",
                "options": ["250", "225", "275", "260"],
                "ans": "250",
                "hint": "Add half of 100 (50) to 200.",
                "explanation": "The midpoint is 200 + (100 / 2) = 250.",
                "solution_steps": [
                    "Step 1: The total distance between 200 and 300 is 100 units.",
                    "Step 2: Half of 100 is 50 units.",
                    "Step 3: 200 + 50 = 250."
                ]
            },
            {
                "id": "c2_q3",
                "q": "Starting at 240, what is the resulting number after jumping forward by 20 on a number slider?",
                "options": ["260", "250", "270", "220"],
                "ans": "260",
                "hint": "Add 20 to 240.",
                "explanation": "240 + 20 = 260.",
                "solution_steps": [
                    "Step 1: Start at baseline 240.",
                    "Step 2: Add 20: 240 + 20 = 260.",
                    "Step 3: Confirm the landing point is 260."
                ]
            },
            {
                "id": "c2_q4",
                "q": "In The Flag Game, if a guess of 205 receives a 'Higher' clue, what is known about the mystery number?",
                "options": ["It is strictly greater than 205", "It is smaller than 205", "It must be 205", "It is smaller than 200"],
                "ans": "It is strictly greater than 205",
                "hint": "'Higher' means you need to guess a larger number.",
                "explanation": "A 'Higher' clue indicates the secret target lies above 205.",
                "solution_steps": [
                    "Step 1: Analyze the feedback clue 'Higher'.",
                    "Step 2: Recognize that all numbers less than or equal to 205 are ruled out.",
                    "Step 3: Conclude that the target is strictly greater than 205."
                ]
            },
            {
                "id": "c2_q5",
                "q": "How many letters are in the English word 'FOUR'?",
                "options": ["4 letters", "5 letters", "3 letters", "6 letters"],
                "ans": "4 letters",
                "hint": "Count F-O-U-R.",
                "explanation": "F-O-U-R has exactly 4 letters.",
                "solution_steps": [
                    "Step 1: Write down the letters: F, O, U, R.",
                    "Step 2: Count them: 1, 2, 3, 4.",
                    "Step 3: The letter count is 4."
                ]
            },
            {
                "id": "c2_q6",
                "q": "Starting at the word 'SIXTEEN' (7 letters), what is the next word in the convergence chain?",
                "options": ["SEVEN", "FIVE", "FOUR", "SIX"],
                "ans": "SEVEN",
                "hint": "Write the number name for the letter count 7.",
                "explanation": "SIXTEEN has 7 letters, so the next word is SEVEN.",
                "solution_steps": [
                    "Step 1: Count letters in S-I-X-T-E-E-N: 7 letters.",
                    "Step 2: Spell out the number 7: S-E-V-E-N.",
                    "Step 3: Confirm the next word in the chain is SEVEN."
                ]
            },
            {
                "id": "c2_q7",
                "q": "What number is reached if you jump backward by 10 from 275?",
                "options": ["265", "285", "255", "270"],
                "ans": "265",
                "hint": "Subtract 10 from 275.",
                "explanation": "275 - 10 = 265.",
                "solution_steps": [
                    "Step 1: Start at 275.",
                    "Step 2: Subtract 10: 275 - 10 = 265.",
                    "Step 3: The resulting number is 265."
                ]
            },
            {
                "id": "c2_q8",
                "q": "Which number is described as '200 and 35 more'?",
                "options": ["235", "253", "2035", "230"],
                "ans": "235",
                "hint": "Add 35 to 200.",
                "explanation": "200 + 35 = 235.",
                "solution_steps": [
                    "Step 1: Start with 200.",
                    "Step 2: Add 35: 200 + 35 = 235.",
                    "Step 3: Confirm the number is 235."
                ]
            },
            {
                "id": "c2_q9",
                "q": "On a number line from 0 to 350, is 320 closer to 300 or to 350?",
                "options": ["Closer to 300", "Closer to 350", "Exactly halfway", "Cannot be determined"],
                "ans": "Closer to 300",
                "hint": "Compare distances: |320 - 300| = 20 vs |350 - 320| = 30.",
                "explanation": "Distance to 300 is 20 units; distance to 350 is 30 units. 20 < 30, so 320 is closer to 300.",
                "solution_steps": [
                    "Step 1: Calculate distance to 300: 320 - 300 = 20 units.",
                    "Step 2: Calculate distance to 350: 350 - 320 = 30 units.",
                    "Step 3: Conclude that 320 is closer to 300."
                ]
            },
            {
                "id": "c2_q10",
                "q": "If a mystery number between 200 and 210 receives clues 'Higher than 205' and 'Lower than 208', what are the possible values?",
                "options": ["206 and 207", "205 and 206", "207 and 208", "208 and 209"],
                "ans": "206 and 207",
                "hint": "List integers strictly between 205 and 208.",
                "explanation": "Integers greater than 205 and less than 208 are 206 and 207.",
                "solution_steps": [
                    "Step 1: Apply 'Higher than 205': numbers must be > 205.",
                    "Step 2: Apply 'Lower than 208': numbers must be < 208.",
                    "Step 3: The only integers satisfying both conditions are 206 and 207."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Mastery Quiz 3",
        "description": "Evaluate understanding of advancing to 400, bakery sweet inventories, and apartment building grid coordinates.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "How far is the number 387 from the next hundred milestone of 400?",
                "options": ["13 units", "23 units", "17 units", "3 units"],
                "ans": "13 units",
                "hint": "Find what must be added to 387 to reach 400.",
                "explanation": "400 - 387 = 13 units.",
                "solution_steps": [
                    "Step 1: Jump from 387 to 390: 3 units.",
                    "Step 2: Jump from 390 to 400: 10 units.",
                    "Step 3: Sum the jumps: 3 + 10 = 13 units."
                ]
            },
            {
                "id": "c3_q2",
                "q": "What total number of sweets is represented by 4 trays of 100, 8 boxes of 10, and 7 singles?",
                "options": ["487 sweets", "478 sweets", "480 sweets", "587 sweets"],
                "ans": "487 sweets",
                "hint": "Calculate 400 + 80 + 7.",
                "explanation": "400 + 80 + 7 = 487 sweets.",
                "solution_steps": [
                    "Step 1: 4 trays of 100 = 400.",
                    "Step 2: 8 boxes of 10 = 80.",
                    "Step 3: Add 7 loose sweets: 400 + 80 + 7 = 487 sweets."
                ]
            },
            {
                "id": "c3_q3",
                "q": "In a 10-column apartment grid, which apartment is located directly one floor above apartment 105?",
                "options": ["115", "106", "125", "104"],
                "ans": "115",
                "hint": "Moving one floor up adds 10.",
                "explanation": "105 + 10 = 115.",
                "solution_steps": [
                    "Step 1: Identify that each floor holds 10 apartments.",
                    "Step 2: Moving up one floor adds 10 to the apartment number.",
                    "Step 3: 105 + 10 = 115."
                ]
            },
            {
                "id": "c3_q4",
                "q": "If you are at apartment 242 on a building grid, what apartment is directly below you?",
                "options": ["232", "252", "241", "243"],
                "ans": "232",
                "hint": "Moving one floor down subtracts 10.",
                "explanation": "242 - 10 = 232.",
                "solution_steps": [
                    "Step 1: Moving downward by one floor subtracts 10.",
                    "Step 2: Calculate: 242 - 10 = 232.",
                    "Step 3: Apartment 232 lies directly below 242."
                ]
            },
            {
                "id": "c3_q5",
                "q": "How many full trays of 100 sweets are needed to make 500 sweets in total?",
                "options": ["5 trays", "4 trays", "50 trays", "10 trays"],
                "ans": "5 trays",
                "hint": "Divide 500 by 100.",
                "explanation": "500 ÷ 100 = 5 trays.",
                "solution_steps": [
                    "Step 1: Each tray holds 100 sweets.",
                    "Step 2: Calculate 500 ÷ 100 = 5.",
                    "Step 3: Exactly 5 trays make 500 sweets."
                ]
            },
            {
                "id": "c3_q6",
                "q": "Which apartment is located directly between 231 and 233 on the same residential floor?",
                "options": ["232", "230", "242", "222"],
                "ans": "232",
                "hint": "Find the consecutive integer between 231 and 233.",
                "explanation": "The integer between 231 and 233 is 232.",
                "solution_steps": [
                    "Step 1: Note that doors on the same floor are numbered consecutively.",
                    "Step 2: The number between 231 and 233 is 231 + 1 = 232.",
                    "Step 3: Conclude that apartment 232 is situated between them."
                ]
            },
            {
                "id": "c3_q7",
                "q": "What number is represented by 3 hundred flats, 4 ten rods, and 2 unit cubes in Dienes blocks?",
                "options": ["342", "324", "432", "340"],
                "ans": "342",
                "hint": "3 flats = 300, 4 rods = 40, 2 cubes = 2.",
                "explanation": "300 + 40 + 2 = 342.",
                "solution_steps": [
                    "Step 1: Calculate flats: 3 × 100 = 300.",
                    "Step 2: Calculate rods: 4 × 10 = 40.",
                    "Step 3: Add cubes: 300 + 40 + 2 = 342."
                ]
            },
            {
                "id": "c3_q8",
                "q": "How many ten rods are needed to construct one hundred flat?",
                "options": ["10 rods", "5 rods", "100 rods", "20 rods"],
                "ans": "10 rods",
                "hint": "10 tens make 100.",
                "explanation": "10 rods of 10 equal 100.",
                "solution_steps": [
                    "Step 1: Each rod equals 10 units.",
                    "Step 2: One flat equals 100 units.",
                    "Step 3: 100 ÷ 10 = 10 rods."
                ]
            },
            {
                "id": "c3_q9",
                "q": "In the number 258, which digit is in the tens place?",
                "options": ["5", "2", "8", "0"],
                "ans": "5",
                "hint": "The middle digit represents the tens column.",
                "explanation": "In H-T-O representation of 258, the tens digit is 5 (value 50).",
                "solution_steps": [
                    "Step 1: Label columns: Hundreds = 2, Tens = 5, Ones = 8.",
                    "Step 2: Locate the tens column digit.",
                    "Step 3: The digit in the tens place is 5."
                ]
            },
            {
                "id": "c3_q10",
                "q": "What distance separates 329 from the next hundred milestone of 400?",
                "options": ["71 units", "81 units", "61 units", "79 units"],
                "ans": "71 units",
                "hint": "400 - 329 = ?",
                "explanation": "329 + 71 = 400.",
                "solution_steps": [
                    "Step 1: Jump from 329 to 330: 1 unit.",
                    "Step 2: Jump from 330 to 400: 70 units.",
                    "Step 3: Total distance: 1 + 70 = 71 units."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Mastery Quiz 4",
        "description": "Master digit hunting, place value comparisons using > and <, and 3-digit permutations and ordering.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "Which comparison statement is mathematically correct?",
                "options": ["487 > 423", "487 < 423", "487 = 423", "423 > 487"],
                "ans": "487 > 423",
                "hint": "Compare tens: 8 tens is greater than 2 tens.",
                "explanation": "Both have 4 hundreds, but 487 has 8 tens while 423 has 2 tens, so 487 > 423.",
                "solution_steps": [
                    "Step 1: Compare hundreds digits: 4 = 4.",
                    "Step 2: Compare tens digits: 8 > 2.",
                    "Step 3: Conclude that 487 > 423."
                ]
            },
            {
                "id": "c4_q2",
                "q": "Compare 209 and 290 using the correct inequality symbol:",
                "options": ["209 < 290", "209 > 290", "209 = 290", "290 < 209"],
                "ans": "209 < 290",
                "hint": "209 has 0 tens, while 290 has 9 tens.",
                "explanation": "209 has 0 tens while 290 has 9 tens, so 209 < 290.",
                "solution_steps": [
                    "Step 1: Compare hundreds digits: 2 = 2.",
                    "Step 2: Compare tens digits: 0 < 9.",
                    "Step 3: Conclude that 209 < 290."
                ]
            },
            {
                "id": "c4_q3",
                "q": "Using the digits 3, 7, and 5 once each, what is the greatest 3-digit number you can create?",
                "options": ["753", "735", "573", "375"],
                "ans": "753",
                "hint": "Place the largest digit in hundreds, then the next largest in tens.",
                "explanation": "Placing 7 in hundreds, 5 in tens, and 3 in ones gives 753.",
                "solution_steps": [
                    "Step 1: Identify the largest digit: 7 (place in hundreds).",
                    "Step 2: Identify the next largest digit: 5 (place in tens).",
                    "Step 3: Place remaining digit 3 in ones: 753."
                ]
            },
            {
                "id": "c4_q4",
                "q": "Using the digits 3, 7, and 5 once each, what is the smallest 3-digit number you can form?",
                "options": ["357", "375", "537", "735"],
                "ans": "357",
                "hint": "Place the smallest digit in hundreds, then the next smallest in tens.",
                "explanation": "Placing 3 in hundreds, 5 in tens, and 7 in ones gives 357.",
                "solution_steps": [
                    "Step 1: Identify the smallest digit: 3 (place in hundreds).",
                    "Step 2: Identify the next smallest digit: 5 (place in tens).",
                    "Step 3: Place remaining digit 7 in ones: 357."
                ]
            },
            {
                "id": "c4_q5",
                "q": "Which number between 200 and 300 has the digit 5 in both its tens and ones places?",
                "options": ["255", "250", "205", "215"],
                "ans": "255",
                "hint": "Look for 5 in the middle and 5 at the end.",
                "explanation": "255 has 5 tens (50) and 5 ones (5).",
                "solution_steps": [
                    "Step 1: Check tens column: needs to be 5.",
                    "Step 2: Check ones column: needs to be 5.",
                    "Step 3: Identify 255 as the matching number."
                ]
            },
            {
                "id": "c4_q6",
                "q": "How many distinct 3-digit numbers can be formed using the non-zero digits 3, 7, and 5 without repetition?",
                "options": ["6 numbers", "3 numbers", "9 numbers", "4 numbers"],
                "ans": "6 numbers",
                "hint": "Calculate 3 × 2 × 1.",
                "explanation": "There are 3! = 3 × 2 × 1 = 6 distinct permutations: 357, 375, 537, 573, 735, 753.",
                "solution_steps": [
                    "Step 1: Choices for hundreds place: 3 options.",
                    "Step 2: Choices for tens place: 2 options remaining.",
                    "Step 3: Choices for ones place: 1 option. Total = 3 × 2 × 1 = 6 numbers."
                ]
            },
            {
                "id": "c4_q7",
                "q": "Which set of numbers is arranged in correct ascending order (smallest to biggest)?",
                "options": ["215, 235, 255, 275", "275, 255, 235, 215", "255, 215, 275, 235", "235, 215, 255, 275"],
                "ans": "215, 235, 255, 275",
                "hint": "Ascending order means each number is larger than the previous one.",
                "explanation": "215 < 235 < 255 < 275 is correctly ordered from smallest to largest.",
                "solution_steps": [
                    "Step 1: Check 215 < 235: True.",
                    "Step 2: Check 235 < 255: True.",
                    "Step 3: Check 255 < 275: True. The set is in ascending order."
                ]
            },
            {
                "id": "c4_q8",
                "q": "What is the value of the digit 4 in the number 487?",
                "options": ["400", "40", "4", "48"],
                "ans": "400",
                "hint": "The digit 4 sits in the hundreds place.",
                "explanation": "Since 4 is in the hundreds column, its value is 4 × 100 = 400.",
                "solution_steps": [
                    "Step 1: Identify the position of digit 4: hundreds column.",
                    "Step 2: Multiply by place value: 4 × 100 = 400.",
                    "Step 3: Conclude that the value is 400."
                ]
            },
            {
                "id": "c4_q9",
                "q": "Between 438 and 476, which number is smaller?",
                "options": ["438 is smaller", "476 is smaller", "They are equal", "Cannot be compared"],
                "ans": "438 is smaller",
                "hint": "Compare tens digits: 3 tens is less than 7 tens.",
                "explanation": "Both have 4 hundreds, but 438 has 3 tens while 476 has 7 tens, so 438 < 476.",
                "solution_steps": [
                    "Step 1: Compare hundreds: 4 = 4.",
                    "Step 2: Compare tens: 3 < 7.",
                    "Step 3: Conclude that 438 is smaller than 476."
                ]
            },
            {
                "id": "c4_q10",
                "q": "Which set of numbers is arranged in correct descending order (biggest to smallest)?",
                "options": ["487, 450, 423, 405", "405, 423, 450, 487", "450, 487, 423, 405", "423, 450, 405, 487"],
                "ans": "487, 450, 423, 405",
                "hint": "Descending order means each number is smaller than the previous one.",
                "explanation": "487 > 450 > 423 > 405 is strictly ordered from largest to smallest.",
                "solution_steps": [
                    "Step 1: Check 487 > 450: True.",
                    "Step 2: Check 450 > 423: True.",
                    "Step 3: Check 423 > 405: True. The set is in descending order."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    FORBIDDEN_CHARACTERS = ['Ajji', 'Teji', 'Jojo', 'Farooq', 'Arvind', 'Raghav', 'Amma', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Deba', 'Deep', 'Meera', 'Dhruv', 'Pihu']
    FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']
    
    print("Validating Part 3 (Slides 17-20 Challenges)...")
    assert len(slides_part3) == 4, "Must have 4 challenge slides"
    total_q = 0
    for s in slides_part3:
        sid = s["id"]
        title = s["title"]
        words = len(title.split())
        assert 1 <= words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {words})"
        
        slide_str = json.dumps(s)
        for name in FORBIDDEN_CHARACTERS:
            if name.lower() == 'deep':
                assert not re.search(r'\bDeep\b', slide_str), f"Slide {sid} contains character name '{name}'"
            else:
                assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
        
        qs = s["questions"]
        assert len(qs) == 10, f"Slide {sid} must have 10 questions, found {len(qs)}"
        total_q += len(qs)
        for q in qs:
            qid = q["id"]
            assert 'hint' in q, f"Question {qid} missing hint!"
            assert len(q["options"]) == 4, f"Question {qid} must have 4 options"
            assert q["ans"] in q["options"], f"Question {qid} answer '{q['ans']}' not in options"
            assert len(q["solution_steps"]) == 3, f"Question {qid} must have 3 solution steps"
    print(f"Part 3 validation successful! Total questions: {total_q}")

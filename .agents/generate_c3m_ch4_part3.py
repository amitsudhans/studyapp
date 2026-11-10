# -*- coding: utf-8 -*-
"""Part 3 (Slides 17-20: Challenges 1-4) for Class 3 Mathematics Chapter 4: Vacation with My Nani Maa."""

import json
import re

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Mastery Quiz 1",
        "sim_id": "quiz_challenge_1",
        "description": "Test your mastery on missing-part subtraction, sweet counts, and ten-frame addition strategies.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "There are 15 marbles on a table. If 8 marbles are visible, how many are hidden under the cloth?",
                "options": ["7 marbles", "8 marbles", "6 marbles", "9 marbles"],
                "ans": "7 marbles",
                "hint": "Subtract the visible marbles from the total: 15 - 8.",
                "explanation": "15 - 8 = 7 hidden marbles.",
                "solution_steps": {
                    "step1": "Given total marbles = 15, visible marbles = 8.",
                    "step2": "Calculate missing part: 15 - 8 = 7.",
                    "step3": "Verify: 8 visible + 7 hidden = 15 total marbles."
                }
            },
            {
                "id": "c4_q2",
                "q": "A cloth covers some tamarind seeds. If the total is 19 and 12 are visible, how many are hidden?",
                "options": ["7 seeds", "8 seeds", "6 seeds", "9 seeds"],
                "ans": "7 seeds",
                "hint": "Calculate 19 - 12.",
                "explanation": "19 - 12 = 7 hidden seeds.",
                "solution_steps": {
                    "step1": "Total seeds = 19, visible seeds = 12.",
                    "step2": "Subtract visible from total: 19 - 12 = 7.",
                    "step3": "Check: 12 + 7 = 19 seeds."
                }
            },
            {
                "id": "c4_q3",
                "q": "Out of 23 river pebbles, 14 are on the ground. How many pebbles are inside a closed fist?",
                "options": ["9 pebbles", "8 pebbles", "10 pebbles", "7 pebbles"],
                "ans": "9 pebbles",
                "hint": "Find the difference: 23 - 14.",
                "explanation": "23 - 14 = 9 pebbles hidden in the fist.",
                "solution_steps": {
                    "step1": "Total pebbles = 23, visible = 14.",
                    "step2": "Subtract: 23 - 14 = 9.",
                    "step3": "Check: 14 + 9 = 23 pebbles."
                }
            },
            {
                "id": "c4_q4",
                "q": "One plate holds 7 fresh balushahis and another plate holds 5. What is the total sweet count?",
                "options": ["12 sweets", "11 sweets", "13 sweets", "14 sweets"],
                "ans": "12 sweets",
                "hint": "Add the two groups: 7 + 5.",
                "explanation": "7 + 5 = 12 balushahis altogether.",
                "solution_steps": {
                    "step1": "First plate = 7 sweets, second plate = 5 sweets.",
                    "step2": "Combine: 7 + 5 = 12.",
                    "step3": "Verify by counting forward 5 from 7: 8, 9, 10, 11, 12."
                }
            },
            {
                "id": "c4_q5",
                "q": "If there are 12 sweets and 4 are eaten during teatime, how many remain on the platter?",
                "options": ["8 sweets", "7 sweets", "9 sweets", "6 sweets"],
                "ans": "8 sweets",
                "hint": "Eating decreases the count: calculate 12 - 4.",
                "explanation": "12 - 4 = 8 sweets remain.",
                "solution_steps": {
                    "step1": "Starting sweets = 12, eaten sweets = 4.",
                    "step2": "Subtract: 12 - 4 = 8.",
                    "step3": "Check: 8 + 4 = 12 sweets."
                }
            },
            {
                "id": "c4_q6",
                "q": "A reader packs 9 storybooks and 7 puzzle books. How many books are there in total?",
                "options": ["16 books", "15 books", "17 books", "14 books"],
                "ans": "16 books",
                "hint": "Use make-a-ten: 9 + 1 = 10, then add the remaining 6.",
                "explanation": "9 + 7 = 16 books.",
                "solution_steps": {
                    "step1": "Storybooks = 9, puzzle books = 7.",
                    "step2": "Decompose 7 into 1 and 6: 9 + 1 = 10, and 10 + 6 = 16.",
                    "step3": "Verify total books = 16."
                }
            },
            {
                "id": "c4_q7",
                "q": "On a ten-frame, what is the fastest way to compute 8 + 5?",
                "options": [
                    "Give 2 from 5 to 8 to make 10, then 10 + 3 = 13",
                    "Count all 13 on fingers by ones",
                    "Subtract 5 from 8 to get 3",
                    "Multiply 8 by 5"
                ],
                "ans": "Give 2 from 5 to 8 to make 10, then 10 + 3 = 13",
                "hint": "8 needs 2 to fill a ten-frame.",
                "explanation": "Making a ten (8 + 2 = 10, then 10 + 3 = 13) is the benchmark ten strategy.",
                "solution_steps": {
                    "step1": "Identify that 8 needs 2 to make 10.",
                    "step2": "Split 5 into 2 and 3. Combine 8 + 2 = 10.",
                    "step3": "Add remainder: 10 + 3 = 13."
                }
            },
            {
                "id": "c4_q8",
                "q": "If 27 seeds are tracked and 18 are visible, how many seeds are hidden?",
                "options": ["9 seeds", "8 seeds", "11 seeds", "7 seeds"],
                "ans": "9 seeds",
                "hint": "Subtract 18 from 27.",
                "explanation": "27 - 18 = 9 hidden seeds.",
                "solution_steps": {
                    "step1": "Total seeds = 27, visible = 18.",
                    "step2": "27 - 18 = 9.",
                    "step3": "Verify: 18 + 9 = 27 seeds."
                }
            },
            {
                "id": "c4_q9",
                "q": "Which addition sentence verifies that 14 - 6 = 8?",
                "options": ["8 + 6 = 14", "14 + 6 = 20", "8 - 6 = 2", "14 + 8 = 22"],
                "ans": "8 + 6 = 14",
                "hint": "Addition reverses subtraction.",
                "explanation": "Because 8 + 6 = 14, it directly verifies that 14 - 6 = 8.",
                "solution_steps": {
                    "step1": "Given subtraction: 14 - 6 = 8.",
                    "step2": "The inverse addition adds the difference (8) and subtrahend (6).",
                    "step3": "8 + 6 = 14 verifies the result."
                }
            },
            {
                "id": "c4_q10",
                "q": "A basket had 16 guavas. After some were given to neighbors, 9 remained. How many were given away?",
                "options": ["7 guavas", "8 guavas", "6 guavas", "9 guavas"],
                "ans": "7 guavas",
                "hint": "Calculate 16 - 9.",
                "explanation": "16 - 9 = 7 guavas were shared.",
                "solution_steps": {
                    "step1": "Original count = 16, remaining count = 9.",
                    "step2": "Subtract: 16 - 9 = 7.",
                    "step3": "Check: 9 remaining + 7 given away = 16 guavas."
                }
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Mastery Quiz 2",
        "sim_id": "quiz_challenge_2",
        "description": "Test your reasoning on card fact families, ginladi bead strings, and decade bundle additions.",
        "questions": [
            {
                "id": "c4_q11",
                "q": "Which three numbers form a valid fact family triplet?",
                "options": [
                    "6, 8, and 14",
                    "5, 6, and 12",
                    "7, 9, and 15",
                    "4, 8, and 13"
                ],
                "ans": "6, 8, and 14",
                "hint": "Look for two numbers whose sum equals the third.",
                "explanation": "6 + 8 = 14, so 6, 8, and 14 form a valid fact family triplet.",
                "solution_steps": {
                    "step1": "Test 6 + 8: 6 + 8 = 14.",
                    "step2": "Verify subtraction: 14 - 6 = 8 and 14 - 8 = 6.",
                    "step3": "Conclude 6, 8, and 14 form a true fact family."
                }
            },
            {
                "id": "c4_q12",
                "q": "If 7 + 8 = 15, which subtraction equation is also true?",
                "options": ["15 - 7 = 8", "15 - 6 = 9", "8 - 7 = 1", "15 - 5 = 10"],
                "ans": "15 - 7 = 8",
                "hint": "Total minus one addend gives the other addend.",
                "explanation": "15 - 7 = 8 is a member of the same fact family.",
                "solution_steps": {
                    "step1": "Given addition: 7 + 8 = 15.",
                    "step2": "Inverse relation gives: 15 - 7 = 8.",
                    "step3": "Both belong to the {7, 8, 15} triplet family."
                }
            },
            {
                "id": "c4_q13",
                "q": "On a ginladi bead string, how can you solve 15 + 7 using friendly bridging to 20?",
                "options": [
                    "15 + 5 = 20, then 20 + 2 = 22",
                    "15 + 10 = 25, then 25 - 5 = 20",
                    "15 + 7 = 21",
                    "15 + 1 = 16, then 16 + 7 = 23"
                ],
                "ans": "15 + 5 = 20, then 20 + 2 = 22",
                "hint": "Split 7 into 5 and 2 to reach the decade 20 first.",
                "explanation": "15 + 5 = 20, and 20 + 2 = 22.",
                "solution_steps": {
                    "step1": "Identify that 15 needs 5 to reach decade 20.",
                    "step2": "Decompose 7 into 5 and 2.",
                    "step3": "Calculate: 15 + 5 = 20, then 20 + 2 = 22."
                }
            },
            {
                "id": "c4_q14",
                "q": "Using the compensation strategy to add 7 to 15, you add 10 first to reach 25. What is the next step?",
                "options": [
                    "Subtract 3 (25 - 3 = 22)",
                    "Add 3 (25 + 3 = 28)",
                    "Subtract 2 (25 - 2 = 23)",
                    "Add 7 (25 + 7 = 32)"
                ],
                "ans": "Subtract 3 (25 - 3 = 22)",
                "hint": "Adding 10 overshot by 3 (10 - 7 = 3).",
                "explanation": "Because 10 is 3 more than 7, subtract 3 from 25 to get 22.",
                "solution_steps": {
                    "step1": "Add 10: 15 + 10 = 25.",
                    "step2": "Notice overshoot: 10 - 7 = 3.",
                    "step3": "Compensate: 25 - 3 = 22."
                }
            },
            {
                "id": "c4_q15",
                "q": "A collection has 22 stamps. A gift of 30 stamps is added. What is the new total?",
                "options": ["52 stamps", "42 stamps", "62 stamps", "55 stamps"],
                "ans": "52 stamps",
                "hint": "Add 3 tens to 2 tens: 20 + 30 = 50, plus 2 ones.",
                "explanation": "22 + 30 = 52 stamps.",
                "solution_steps": {
                    "step1": "Start at 22.",
                    "step2": "Jump three tens: 22 + 10 = 32, 32 + 10 = 42, 42 + 10 = 52.",
                    "step3": "Total stamps = 52."
                }
            },
            {
                "id": "c4_q16",
                "q": "What is 34 + 20 calculated using tens jumps?",
                "options": ["54", "44", "64", "50"],
                "ans": "54",
                "hint": "Jump two tens from 34: 44, 54.",
                "explanation": "34 + 20 = 54.",
                "solution_steps": {
                    "step1": "Start at 34.",
                    "step2": "Add 2 tens (20): 34 + 10 = 44, 44 + 10 = 54.",
                    "step3": "Conclude 34 + 20 = 54."
                }
            },
            {
                "id": "c4_q17",
                "q": "If 45 + 30 = 75, what is 75 - 30?",
                "options": ["45", "35", "55", "40"],
                "ans": "45",
                "hint": "Subtraction undoes addition.",
                "explanation": "75 - 30 = 45.",
                "solution_steps": {
                    "step1": "Given 45 + 30 = 75.",
                    "step2": "Inverse subtraction: 75 - 30 = 45.",
                    "step3": "Verify: 45 + 30 = 75."
                }
            },
            {
                "id": "c4_q18",
                "q": "Which number card makes this equation true: 9 + ___ = 17?",
                "options": ["8", "7", "9", "6"],
                "ans": "8",
                "hint": "Calculate 17 - 9.",
                "explanation": "17 - 9 = 8, so 9 + 8 = 17.",
                "solution_steps": {
                    "step1": "Unknown addend: 9 + ? = 17.",
                    "step2": "Calculate 17 - 9 = 8.",
                    "step3": "Check: 9 + 8 = 17."
                }
            },
            {
                "id": "c4_q19",
                "q": "A runner has completed 28 laps and aims for 50 laps. How many laps remain?",
                "options": ["22 laps", "32 laps", "18 laps", "24 laps"],
                "ans": "22 laps",
                "hint": "Jump 2 to reach 30, then 20 to reach 50.",
                "explanation": "50 - 28 = 22 laps.",
                "solution_steps": {
                    "step1": "Goal = 50, completed = 28.",
                    "step2": "From 28, jump +2 to 30, then +20 to 50. Total jump = 2 + 20 = 22.",
                    "step3": "Verify: 28 + 22 = 50 laps."
                }
            },
            {
                "id": "c4_q20",
                "q": "On a ginladi, starting at bead 18 and jumping forward 10 lands on which bead?",
                "options": ["28", "27", "29", "38"],
                "ans": "28",
                "hint": "A leap of 10 increases the tens digit by 1.",
                "explanation": "18 + 10 = 28.",
                "solution_steps": {
                    "step1": "Start = 18.",
                    "step2": "Add 10: 18 + 10 = 28.",
                    "step3": "Bead 28 is the landing point."
                }
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Mastery Quiz 3",
        "sim_id": "quiz_challenge_3",
        "description": "Test your competence on backward line jumps, decade leaps, estimation, and 100-grid arrow navigation.",
        "questions": [
            {
                "id": "c4_q21",
                "q": "Out of 52 total stamps, 37 are portrait stamps and the rest are monument stamps. How many monument stamps are there?",
                "options": ["15 stamps", "17 stamps", "25 stamps", "14 stamps"],
                "ans": "15 stamps",
                "hint": "Subtract 37 from 52 using backward jumps.",
                "explanation": "52 - 37 = 15 monument stamps.",
                "solution_steps": {
                    "step1": "Total stamps = 52, portraits = 37.",
                    "step2": "Jump back 30 from 52 to 22. Then jump back 7 from 22 to 15.",
                    "step3": "Total monument stamps = 15."
                }
            },
            {
                "id": "c4_q22",
                "q": "How many more stamps are needed to reach a target of 75 if you currently have 52 stamps?",
                "options": ["23 stamps", "25 stamps", "22 stamps", "33 stamps"],
                "ans": "23 stamps",
                "hint": "Find 75 - 52.",
                "explanation": "75 - 52 = 23 stamps needed.",
                "solution_steps": {
                    "step1": "Target = 75, current = 52.",
                    "step2": "Jump from 52 to 72 (+20), then from 72 to 75 (+3).",
                    "step3": "Total stamps needed = 20 + 3 = 23."
                }
            },
            {
                "id": "c4_q23",
                "q": "A grasshopper hops backward from 67 by two jumps of 10. Where does it land?",
                "options": ["47", "57", "37", "45"],
                "ans": "47",
                "hint": "67 - 10 = 57, and 57 - 10 = 47.",
                "explanation": "67 - 20 = 47.",
                "solution_steps": {
                    "step1": "Start at 67.",
                    "step2": "First backward leap of 10: 67 - 10 = 57.",
                    "step3": "Second backward leap of 10: 57 - 10 = 47."
                }
            },
            {
                "id": "c4_q24",
                "q": "A foraging team has 60 ants in total. If 42 are marching outside, how many are hidden under the leaf?",
                "options": ["18 ants", "28 ants", "16 ants", "22 ants"],
                "ans": "18 ants",
                "hint": "Calculate 60 - 42.",
                "explanation": "60 - 42 = 18 ants.",
                "solution_steps": {
                    "step1": "Total ants = 60, visible = 42.",
                    "step2": "Subtract: 60 - 40 = 20, and 20 - 2 = 18.",
                    "step3": "Hidden ants = 18."
                }
            },
            {
                "id": "c4_q25",
                "q": "On a 100-grid, what does moving one step straight UP represent?",
                "options": ["Subtract 10 (-10)", "Add 10 (+10)", "Subtract 1 (-1)", "Divide by 10"],
                "ans": "Subtract 10 (-10)",
                "hint": "The row above contains numbers 10 less.",
                "explanation": "Moving one cell up on a 100-grid subtracts 10.",
                "solution_steps": {
                    "step1": "Each row in a 100-grid represents a decade of 10 numbers.",
                    "step2": "Moving up shifts to the previous row.",
                    "step3": "Conclude moving up is equivalent to subtracting 10."
                }
            },
            {
                "id": "c4_q26",
                "q": "Starting at 38 on a 100-grid, follow the path [Down, Down, Right]. On which number do you land?",
                "options": ["59", "58", "68", "49"],
                "ans": "59",
                "hint": "Down adds 10, Down adds 10, Right adds 1.",
                "explanation": "38 + 10 = 48, 48 + 10 = 58, 58 + 1 = 59.",
                "solution_steps": {
                    "step1": "Start at 38.",
                    "step2": "First Down: 38 + 10 = 48. Second Down: 48 + 10 = 58.",
                    "step3": "Right: 58 + 1 = 59."
                }
            },
            {
                "id": "c4_q27",
                "q": "Starting at 73 on a 100-grid, follow [Up, Left, Left]. What is your final position?",
                "options": ["61", "62", "63", "51"],
                "ans": "61",
                "hint": "Up is -10 (63), then Left is -1 (62), Left is -1 (61).",
                "explanation": "73 - 10 = 63, 63 - 1 = 62, 62 - 1 = 61.",
                "solution_steps": {
                    "step1": "Start at 73.",
                    "step2": "Up: 73 - 10 = 63.",
                    "step3": "Left, Left: 63 - 2 = 61."
                }
            },
            {
                "id": "c4_q28",
                "q": "In the Grid Race Game, if a player on cell 58 rolls digits 1 and 4, which forward move is possible without exceeding 100?",
                "options": [
                    "Both adding 14 (to 72) and adding 41 (to 99)",
                    "Only adding 14, because 41 goes over 100",
                    "Only adding 41",
                    "Neither move is allowed"
                ],
                "ans": "Both adding 14 (to 72) and adding 41 (to 99)",
                "hint": "Check 58 + 14 and 58 + 41.",
                "explanation": "58 + 14 = 72 and 58 + 41 = 99; both are within the 1-100 board.",
                "solution_steps": {
                    "step1": "Option A: 58 + 14 = 72 (valid).",
                    "step2": "Option B: 58 + 41 = 99 (valid, enters 91-100 winning zone).",
                    "step3": "Both moves are valid."
                }
            },
            {
                "id": "c4_q29",
                "q": "Before calculating 89 - 31, which is the best quick mental estimate?",
                "options": [
                    "Around 60 (since 90 - 30 = 60)",
                    "Around 20",
                    "Around 100",
                    "Around 40"
                ],
                "ans": "Around 60 (since 90 - 30 = 60)",
                "hint": "Round 89 to 90 and 31 to 30.",
                "explanation": "Rounding to nearest tens gives 90 - 30 = 60 (exact is 58).",
                "solution_steps": {
                    "step1": "Round 89 to nearest ten = 90.",
                    "step2": "Round 31 to nearest ten = 30.",
                    "step3": "Estimated difference: 90 - 30 = 60."
                }
            },
            {
                "id": "c4_q30",
                "q": "What is 64 - 28 calculated using open number line jumps?",
                "options": ["36", "38", "34", "46"],
                "ans": "36",
                "hint": "64 - 20 = 44, then 44 - 8 = 36.",
                "explanation": "64 - 28 = 36.",
                "solution_steps": {
                    "step1": "Start at 64.",
                    "step2": "Jump back 20: 64 - 20 = 44.",
                    "step3": "Jump back 8: 44 - 4 = 40, and 40 - 4 = 36."
                }
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Mastery Quiz 4",
        "sim_id": "quiz_challenge_4",
        "description": "Test your mastery on magic squares, harvest additions with regrouping, and 100-complements.",
        "questions": [
            {
                "id": "c4_q31",
                "q": "In a 3x3 magic square with sum 15, the top row has 8 and 1. What is the missing third number?",
                "options": ["6", "5", "7", "4"],
                "ans": "6",
                "hint": "8 + 1 + ? = 15.",
                "explanation": "8 + 1 = 9, and 15 - 9 = 6.",
                "solution_steps": {
                    "step1": "Top row sum must be 15.",
                    "step2": "Known numbers: 8 + 1 = 9.",
                    "step3": "Missing number: 15 - 9 = 6."
                }
            },
            {
                "id": "c4_q32",
                "q": "In the same magic square, if the middle row has 3 and 7, which central number completes the sum of 15?",
                "options": ["5", "4", "6", "8"],
                "ans": "5",
                "hint": "3 + ? + 7 = 15.",
                "explanation": "3 + 7 = 10, and 15 - 10 = 5.",
                "solution_steps": {
                    "step1": "Middle row numbers: 3, center, 7.",
                    "step2": "3 + 7 = 10.",
                    "step3": "15 - 10 = 5 is the central anchor."
                }
            },
            {
                "id": "c4_q33",
                "q": "A farmer harvests 25 red radishes and 36 white radishes. What is the total harvest count?",
                "options": ["61 radishes", "51 radishes", "60 radishes", "71 radishes"],
                "ans": "61 radishes",
                "hint": "Add tens: 20 + 30 = 50. Add ones: 5 + 6 = 11. Combine 50 + 11.",
                "explanation": "25 + 36 = 61 radishes.",
                "solution_steps": {
                    "step1": "Tens: 20 + 30 = 50.",
                    "step2": "Ones: 5 + 6 = 11 (1 ten and 1 one).",
                    "step3": "Total = 50 + 11 = 61 radishes."
                }
            },
            {
                "id": "c4_q34",
                "q": "A wooden crate holds 100 vegetables. If 65 are tomatoes, how many carrots fill the crate completely?",
                "options": ["35 carrots", "45 carrots", "25 carrots", "30 carrots"],
                "ans": "35 carrots",
                "hint": "Find the complement: 100 - 65.",
                "explanation": "100 - 65 = 35 carrots.",
                "solution_steps": {
                    "step1": "Total capacity = 100, tomatoes = 65.",
                    "step2": "From 65, jump +5 to 70, then +30 to 100.",
                    "step3": "Carrots needed = 5 + 30 = 35."
                }
            },
            {
                "id": "c4_q35",
                "q": "Two orchard baskets contain 85 apples and 67 apples. What is the grand combined total?",
                "options": ["152 apples", "142 apples", "162 apples", "150 apples"],
                "ans": "152 apples",
                "hint": "Add tens: 80 + 60 = 140. Add ones: 5 + 7 = 12.",
                "explanation": "85 + 67 = 152 apples.",
                "solution_steps": {
                    "step1": "80 + 60 = 140.",
                    "step2": "5 + 7 = 12.",
                    "step3": "140 + 12 = 152 apples."
                }
            },
            {
                "id": "c4_q36",
                "q": "By how many apples does the first basket of 85 exceed the second basket of 67?",
                "options": ["18 apples", "16 apples", "22 apples", "12 apples"],
                "ans": "18 apples",
                "hint": "Find the margin difference: 85 - 67.",
                "explanation": "85 - 67 = 18 apples.",
                "solution_steps": {
                    "step1": "Basket 1 = 85, Basket 2 = 67.",
                    "step2": "Subtract: 85 - 60 = 25, and 25 - 7 = 18.",
                    "step3": "Difference margin = 18 apples."
                }
            },
            {
                "id": "c4_q37",
                "q": "In a school book sale, 48 science books and 37 storybooks were sold. What was the total books sold?",
                "options": ["85 books", "75 books", "84 books", "95 books"],
                "ans": "85 books",
                "hint": "48 + 37: 40 + 30 = 70, 8 + 7 = 15.",
                "explanation": "48 + 37 = 85 books.",
                "solution_steps": {
                    "step1": "Tens sum: 40 + 30 = 70.",
                    "step2": "Ones sum: 8 + 7 = 15.",
                    "step3": "Combined total = 70 + 15 = 85 books."
                }
            },
            {
                "id": "c4_q38",
                "q": "In a friendly cricket match, the opening team scored 76 runs in the first innings and 58 in the second. What was their total score?",
                "options": ["134 runs", "124 runs", "144 runs", "132 runs"],
                "ans": "134 runs",
                "hint": "76 + 58: 70 + 50 = 120, 6 + 8 = 14.",
                "explanation": "76 + 58 = 134 runs.",
                "solution_steps": {
                    "step1": "Innings 1 = 76, Innings 2 = 58.",
                    "step2": "70 + 50 = 120, and 6 + 8 = 14.",
                    "step3": "Total score = 120 + 14 = 134 runs."
                }
            },
            {
                "id": "c4_q39",
                "q": "A school canteen prepared 90 hot vadas. During recess, 64 vadas were bought. How many vadas remained?",
                "options": ["26 vadas", "36 vadas", "24 vadas", "34 vadas"],
                "ans": "26 vadas",
                "hint": "Calculate 90 - 64.",
                "explanation": "90 - 64 = 26 vadas.",
                "solution_steps": {
                    "step1": "Total vadas = 90, sold = 64.",
                    "step2": "90 - 60 = 30, and 30 - 4 = 26.",
                    "step3": "Remaining vadas = 26."
                }
            },
            {
                "id": "c4_q40",
                "q": "A terrace garden has 43 flowering pots and 29 herbal pots. What is the total pot count?",
                "options": ["72 pots", "62 pots", "71 pots", "74 pots"],
                "ans": "72 pots",
                "hint": "43 + 29 = 43 + 30 - 1.",
                "explanation": "43 + 29 = 72 pots.",
                "solution_steps": {
                    "step1": "Flowering = 43, herbal = 29.",
                    "step2": "Use compensation: 43 + 30 = 73, then 73 - 1 = 72.",
                    "step3": "Total garden pots = 72."
                }
            }
        ]
    }
]

FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani']
FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 17 TO 20 (CHALLENGES) ===")
    assert len(slides_part3) == 4, f"Expected 4 challenge slides, got {len(slides_part3)}"
    total_q = 0
    for s in slides_part3:
        sid = s['id']
        title = s['title']
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        assert len(s['questions']) == 10, f"Slide {sid} must have 10 questions"
        total_q += len(s['questions'])
        
        for q in s['questions']:
            assert len(q['options']) == 4, f"Question {q['id']} must have 4 options"
            assert q['ans'] in q['options'], f"Question {q['id']} ans '{q['ans']}' not in options"
            assert 'step1' in q['solution_steps'] and 'step2' in q['solution_steps'] and 'step3' in q['solution_steps'], f"Question {q['id']} missing 3-step solution"

        s_str = json.dumps(s)
        for name in FORBIDDEN_CHARACTERS:
            if name.lower() == 'deep':
                assert not re.search(r'\bDeep\b', s_str), f"Slide {sid} contains character name '{name}'"
            else:
                assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", s_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"

    print(f"Verified {len(slides_part3)} challenge slides with {total_q} questions successfully!")


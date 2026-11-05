# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 (Challenge 1, 2, 3, 4) with 40 mastery questions,
hints, explanations, and popup step-by-step solutions for Class 4 Maths Chapter 3.
Zero human names, clean Unicode math throughout.
"""

def make_sol_html(steps):
    step_items = "".join([f"<li class='mb-2 text-slate-700 dark:text-slate-300'>{s}</li>" for s in steps])
    return f"<div class='p-3 bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 rounded-lg text-sm'><div class='font-bold text-amber-800 dark:text-amber-300 mb-2 flex items-center gap-1.5'><svg class='w-4 h-4' fill='none' stroke='currentColor' viewBox='0 0 24 24'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z'></path></svg>Step-by-Step Solution</div><ol class='list-decimal list-inside space-y-1'>{step_items}</ol></div>"

def get_part3_slides():
    return [
        {
            "id": 17,
            "title": "Challenge 1",
            "section": "Mastery Challenges",
            "speech": "",
            "quiz": [
                {
                    "id": 1,
                    "q": "An orchard has 6 rows of coconut trees with 8 trees in each row. How many coconut trees are planted in total?",
                    "options": ["42 trees", "46 trees", "48 trees", "54 trees"],
                    "ans": 2,
                    "hint": "Multiply the number of rows by the number of trees in each column.",
                    "explanation": "6 rows × 8 trees per row = 48 coconut trees in total.",
                    "sol": make_sol_html([
                        "Identify the grid dimensions: 6 horizontal rows and 8 vertical columns.",
                        "Apply rectangular array multiplication: Total = Rows × Columns.",
                        "Calculate: 6 × 8 = 48 trees."
                    ])
                },
                {
                    "id": 2,
                    "q": "If 5 coconuts are plucked from each of the 48 trees, what is the total number of coconuts harvested?",
                    "options": ["200 coconuts", "220 coconuts", "240 coconuts", "250 coconuts"],
                    "ans": 2,
                    "hint": "Multiply 48 by 5 by splitting 48 into 40 + 8.",
                    "explanation": "(40 × 5) + (8 × 5) = 200 + 40 = 240 coconuts.",
                    "sol": make_sol_html([
                        "Total trees = 48. Plucked coconuts per tree = 5.",
                        "Multiply 48 × 5.",
                        "Break down: 40 × 5 = 200, and 8 × 5 = 40.",
                        "Sum: 200 + 40 = 240 coconuts."
                    ])
                },
                {
                    "id": 3,
                    "q": "A potter arranges 7 vertical stacks of clay cups. Each stack has 6 cups. How many cups are on the bench?",
                    "options": ["36 cups", "42 cups", "48 cups", "49 cups"],
                    "ans": 1,
                    "hint": "Calculate 7 groups of 6 items.",
                    "explanation": "7 stacks × 6 cups per stack = 42 cups in total.",
                    "sol": make_sol_html([
                        "Identify the number of stacks: 7 vertical columns.",
                        "Count items per column: 6 cups.",
                        "Calculate: 7 × 6 = 42 cups."
                    ])
                },
                {
                    "id": 4,
                    "q": "On another table, there are 5 stacks of plates with 8 plates in each stack. If 6 plates are sold, how many plates remain?",
                    "options": ["32 plates", "34 plates", "36 plates", "40 plates"],
                    "ans": 1,
                    "hint": "Find the total number of plates first, then subtract the 6 sold plates.",
                    "explanation": "Total plates = 5 × 8 = 40. Remaining = 40 - 6 = 34 plates.",
                    "sol": make_sol_html([
                        "Calculate initial plates: 5 stacks × 8 plates = 40 plates.",
                        "Subtract the 6 sold plates: 40 - 6 = 34 plates remaining."
                    ])
                },
                {
                    "id": 5,
                    "q": "A sweet tray has 9 coconut laddoos and 16 milk pedas. How many total sweets are arranged in 3 such identical trays?",
                    "options": ["65 sweets", "70 sweets", "75 sweets", "80 sweets"],
                    "ans": 2,
                    "hint": "Find the total sweets in one tray, then multiply by 3.",
                    "explanation": "One tray = 9 + 16 = 25 sweets. 3 trays = 3 × 25 = 75 sweets.",
                    "sol": make_sol_html([
                        "Count sweets per tray: 9 laddoos + 16 pedas = 25 sweets.",
                        "Multiply by 3 trays: 3 × 25 = 75 total sweets."
                    ])
                },
                {
                    "id": 6,
                    "q": "How many more milk pedas than coconut laddoos are there across 4 identical sweet trays?",
                    "options": ["24 more pedas", "28 more pedas", "32 more pedas", "36 more pedas"],
                    "ans": 1,
                    "hint": "In one tray, pedas exceed laddoos by 16 - 9 = 7 sweets.",
                    "explanation": "Difference per tray = 16 - 9 = 7 pedas. Across 4 trays: 4 × 7 = 28 more pedas.",
                    "sol": make_sol_html([
                        "Difference in one tray = 16 pedas - 9 laddoos = 7 pedas.",
                        "Scale for 4 trays: 4 × 7 = 28 more pedas."
                    ])
                },
                {
                    "id": 7,
                    "q": "A money pattern has 6 ten-rupee notes, 4 five-rupee coins, and 8 two-rupee coins. What is the total monetary value?",
                    "options": ["₹88", "₹92", "₹96", "₹100"],
                    "ans": 2,
                    "hint": "Group and multiply: 6 × 10, 4 × 5, and 8 × 2, then add all values.",
                    "explanation": "(6 × 10) + (4 × 5) + (8 × 2) = 60 + 20 + 16 = ₹96.",
                    "sol": make_sol_html([
                        "Value of ten-rupee notes: 6 × ₹10 = ₹60.",
                        "Value of five-rupee coins: 4 × ₹5 = ₹20.",
                        "Value of two-rupee coins: 8 × ₹2 = ₹16.",
                        "Total monetary value = 60 + 20 + 16 = ₹96."
                    ])
                },
                {
                    "id": 8,
                    "q": "Which collection has the highest value: 12 five-rupee coins, 28 two-rupee coins, or 7 ten-rupee notes?",
                    "options": ["12 five-rupee coins", "28 two-rupee coins", "7 ten-rupee notes", "All are equal"],
                    "ans": 2,
                    "hint": "Calculate each value: 12 × 5, 28 × 2, and 7 × 10.",
                    "explanation": "12 × 5 = ₹60; 28 × 2 = ₹56; 7 × 10 = ₹70. ₹70 is the highest.",
                    "sol": make_sol_html([
                        "Calculate value 1: 12 × ₹5 = ₹60.",
                        "Calculate value 2: 28 × ₹2 = ₹56.",
                        "Calculate value 3: 7 × ₹10 = ₹70.",
                        "Comparing: ₹70 > ₹60 > ₹56. 7 ten-rupee notes has the highest value."
                    ])
                },
                {
                    "id": 9,
                    "q": "An orchard has 35 coconut trees arranged in 5 equal rows. How many trees are in each row?",
                    "options": ["6 trees", "7 trees", "8 trees", "9 trees"],
                    "ans": 1,
                    "hint": "Divide the total count of 35 trees by 5 rows.",
                    "explanation": "35 ÷ 5 = 7 trees in each row.",
                    "sol": make_sol_html([
                        "Total trees = 35, organized in 5 equal rows.",
                        "Divide: 35 ÷ 5 = 7 trees per row."
                    ])
                },
                {
                    "id": 10,
                    "q": "If 10 ten-rupee notes and 8 five-rupee coins are used to pay a bill of ₹135, how much change is returned?",
                    "options": ["₹0 (exact)", "₹5", "₹10", "₹15"],
                    "ans": 1,
                    "hint": "Total paid = (10 × 10) + (8 × 5) = 100 + 40 = 140 rupees. Change = 140 - 135.",
                    "explanation": "Total paid = ₹140. Change returned = 140 - 135 = ₹5.",
                    "sol": make_sol_html([
                        "Total money paid = (10 × ₹10) + (8 × ₹5) = ₹100 + ₹40 = ₹140.",
                        "Bill amount = ₹135.",
                        "Change returned = ₹140 - ₹135 = ₹5."
                    ])
                }
            ]
        },
        {
            "id": 18,
            "title": "Challenge 2",
            "section": "Mastery Challenges",
            "speech": "",
            "quiz": [
                {
                    "id": 11,
                    "q": "What is the minimum number of notes and coins needed to form ₹68 using ₹50, ₹10, ₹5, ₹2, and ₹1 denominations?",
                    "options": ["4 items", "5 items", "6 items", "7 items"],
                    "ans": 1,
                    "hint": "Use the largest denominations first: 1 × ₹50, 1 × ₹10, 1 × ₹5, 1 × ₹2, 1 × ₹1.",
                    "explanation": "1 × ₹50 + 1 × ₹10 + 1 × ₹5 + 1 × ₹2 + 1 × ₹1 = ₹68. Total = 5 items.",
                    "sol": make_sol_html([
                        "Start with largest denomination: 1 × ₹50 = ₹50 (remaining ₹18).",
                        "Next denomination: 1 × ₹10 = ₹10 (remaining ₹8).",
                        "Next denomination: 1 × ₹5 = ₹5 (remaining ₹3).",
                        "Next denomination: 1 × ₹2 = ₹2 (remaining ₹1).",
                        "Final denomination: 1 × ₹1 = ₹1 (remaining ₹0).",
                        "Total count of items = 1 + 1 + 1 + 1 + 1 = 5 items."
                    ])
                },
                {
                    "id": 12,
                    "q": "Can ₹125 be formed using exactly 1 hundred-rupee note, 1 twenty-rupee note, and 1 five-rupee coin?",
                    "options": ["No, it falls short by ₹5", "No, it exceeds by ₹5", "Yes, exactly 100 + 20 + 5 = ₹125", "Only if ₹2 coins are added"],
                    "ans": 2,
                    "hint": "Add the denominations: 100 + 20 + 5.",
                    "explanation": "100 + 20 + 5 = ₹125 exactly.",
                    "sol": make_sol_html([
                        "1 hundred-rupee note = ₹100.",
                        "1 twenty-rupee note = ₹20.",
                        "1 five-rupee coin = ₹5.",
                        "Sum: 100 + 20 + 5 = ₹125. Exactly matching."
                    ])
                },
                {
                    "id": 13,
                    "q": "Which of the following numbers of coins CAN be grouped into 2 equal rows without any leftover?",
                    "options": ["15 coins", "18 coins", "21 coins", "25 coins"],
                    "ans": 1,
                    "exp": "18 ÷ 2 = 9 coins per row with zero remainder. 18 is an even number.",
                    "hint": "Check which number is an even number divisible by 2.",
                    "explanation": "18 is even (18 = 2 × 9), so it splits into 2 equal rows of 9 coins.",
                    "sol": make_sol_html([
                        "To divide into 2 equal rows with no leftovers, the quantity must be even.",
                        "Test each: 15 (odd, leaves 1), 18 (even, 18 ÷ 2 = 9), 21 (odd), 25 (odd).",
                        "18 coins forms 2 equal rows of 9 coins."
                    ])
                },
                {
                    "id": 14,
                    "q": "If 24 coins are arranged into 4 equal columns, how many coins are in each column?",
                    "options": ["5 coins", "6 coins", "7 coins", "8 coins"],
                    "ans": 1,
                    "hint": "Divide 24 coins by 4 columns.",
                    "explanation": "24 ÷ 4 = 6 coins per column.",
                    "sol": make_sol_html([
                        "Total coins = 24. Number of columns = 4.",
                        "Divide: 24 ÷ 4 = 6 coins in each column."
                    ])
                },
                {
                    "id": 15,
                    "q": "How many individual shoes are there in 9 complete pairs of shoes?",
                    "options": ["16 shoes", "18 shoes", "20 shoes", "22 shoes"],
                    "ans": 1,
                    "hint": "Each pair consists of 2 shoes.",
                    "explanation": "9 pairs × 2 shoes per pair = 18 shoes.",
                    "sol": make_sol_html([
                        "1 pair = 2 items.",
                        "9 pairs = 9 × 2 = 18 shoes."
                    ])
                },
                {
                    "id": 16,
                    "q": "When 19 pencils are grouped into pairs of two, how many pencils remain unpaired?",
                    "options": ["0 pencils", "1 pencil", "2 pencils", "3 pencils"],
                    "ans": 1,
                    "hint": "19 is an odd number. Dividing by 2 always leaves a remainder.",
                    "explanation": "19 = (9 × 2) + 1. There are 9 pairs and exactly 1 unpaired pencil.",
                    "sol": make_sol_html([
                        "Divide 19 by 2: 19 ÷ 2 = 9 complete pairs with a remainder of 1.",
                        "Exactly 1 pencil remains unpaired."
                    ])
                },
                {
                    "id": 17,
                    "q": "Which of these numbers is an even number: 13, 17, 20, 23?",
                    "options": ["13", "17", "20", "23"],
                    "ans": 2,
                    "hint": "Even numbers end in 0, 2, 4, 6, or 8 and divide by 2 with no remainder.",
                    "explanation": "20 ends in 0 and divides evenly by 2 (20 ÷ 2 = 10).",
                    "sol": make_sol_html([
                        "Check divisibility by 2 or ending digit.",
                        "13, 17, and 23 end in 3, 7, and 3 (all odd).",
                        "20 ends in 0, so 20 is an even number."
                    ])
                },
                {
                    "id": 18,
                    "q": "If an even number is divided into two equal halves, what kind of numbers are the two halves?",
                    "options": ["Always fractions", "Always equal whole numbers", "Always odd numbers", "Always unequal numbers"],
                    "ans": 1,
                    "hint": "Think of 8 ÷ 2 = 4 and 4, or 10 ÷ 2 = 5 and 5.",
                    "explanation": "An even number divides into two identical whole numbers.",
                    "sol": make_sol_html([
                        "By definition, an even number 2n divides by 2 to yield two identical whole numbers n and n."
                    ])
                },
                {
                    "id": 19,
                    "q": "How can ₹183 be assembled with the fewest notes and coins using standard denominations?",
                    "options": [
                        "18 ten-rupee notes and 3 one-rupee coins",
                        "1 hundred, 1 fifty, 3 tens, 1 two-rupee, and 1 one-rupee",
                        "3 fifty-rupee notes and 33 one-rupee coins",
                        "2 fifty-rupee notes and 83 one-rupee coins"
                    ],
                    "ans": 1,
                    "hint": "Combine ₹100 + ₹50 + ₹30 + ₹2 + ₹1.",
                    "explanation": "1 × 100 + 1 × 50 + 3 × 10 + 1 × 2 + 1 × 1 = ₹183 (7 items total).",
                    "sol": make_sol_html([
                        "100 + 50 = 150.",
                        "150 + 30 (three ₹10 notes) = 180.",
                        "180 + 2 + 1 = 183.",
                        "This uses only 7 items and is the standard minimal denomination set."
                    ])
                },
                {
                    "id": 20,
                    "q": "Which statement about zero is mathematically correct?",
                    "options": ["Zero is an odd number", "Zero is an even number", "Zero is neither even nor odd", "Zero cannot be tested"],
                    "ans": 1,
                    "hint": "Zero divided by 2 gives 0 with remainder 0.",
                    "explanation": "0 ÷ 2 = 0 remainder 0. Since the remainder is 0, zero is an even number.",
                    "sol": make_sol_html([
                        "Dividing 0 by 2 yields a quotient of 0 with 0 remainder.",
                        "Because there is zero remainder, 0 satisfies the definition of an even number."
                    ])
                }
            ]
        },
        {
            "id": 19,
            "title": "Challenge 3",
            "section": "Mastery Challenges",
            "speech": "",
            "quiz": [
                {
                    "id": 21,
                    "q": "What is the remainder when the odd number 37 is divided by 2?",
                    "options": ["0", "1", "2", "7"],
                    "ans": 1,
                    "hint": "All odd numbers leave the same remainder when divided by 2.",
                    "explanation": "37 = (18 × 2) + 1. The remainder is always 1.",
                    "sol": make_sol_html([
                        "37 ÷ 2 = 18 with 1 remainder.",
                        "Every odd number leaves a remainder of 1 when divided by 2."
                    ])
                },
                {
                    "id": 22,
                    "q": "Which of the following is NOT an odd number: 11, 15, 18, 23?",
                    "options": ["11", "15", "18", "23"],
                    "ans": 2,
                    "hint": "Look for the number ending in an even digit (0, 2, 4, 6, 8).",
                    "explanation": "18 ends in 8, which is an even digit, making 18 an even number.",
                    "sol": make_sol_html([
                        "11 ends in 1 (odd).",
                        "15 ends in 5 (odd).",
                        "18 ends in 8 (even).",
                        "23 ends in 3 (odd).",
                        "18 is the only even number in the list."
                    ])
                },
                {
                    "id": 23,
                    "q": "How many odd numbers are there in the sequence from 1 to 10 inclusive?",
                    "options": ["4", "5", "6", "7"],
                    "ans": 1,
                    "hint": "List them: 1, 3, 5, 7, 9.",
                    "explanation": "There are 5 odd numbers (1, 3, 5, 7, 9) and 5 even numbers (2, 4, 6, 8, 10).",
                    "sol": make_sol_html([
                        "Odd numbers in 1 to 10: 1, 3, 5, 7, 9.",
                        "Count = 5 odd numbers."
                    ])
                },
                {
                    "id": 24,
                    "q": "If you multiply any whole number by 2, what will always be the parity of the product?",
                    "options": ["Always odd", "Always even", "Sometimes odd, sometimes even", "Depends on the number"],
                    "ans": 1,
                    "hint": "Any number multiplied by 2 consists of complete pairs of 2.",
                    "explanation": "Multiplying by 2 ensures complete pairing with zero remainder, so the product is always even.",
                    "sol": make_sol_html([
                        "Let n be any integer. 2 × n = 2n, which is divisible by 2 with 0 remainder.",
                        "Therefore, multiplying any whole number by 2 always yields an even number."
                    ])
                },
                {
                    "id": 25,
                    "q": "In a 1–50 crayon chart, in which column would you find the number 29?",
                    "options": ["Column ending in 2", "Column ending in 5", "Column ending in 7", "Column ending in 9"],
                    "ans": 3,
                    "hint": "The ones digit indicates the column in a 10-column grid.",
                    "explanation": "29 ends in 9, so it is in the 9th column (the column of numbers ending in 9).",
                    "sol": make_sol_html([
                        "In a standard 10-column grid, column index matches the ones digit.",
                        "29 ends in 9, placing it in column 9 (which contains only circled odd numbers)."
                    ])
                },
                {
                    "id": 26,
                    "q": "What marker would be placed on number 44 in the crayon grid: circle or square?",
                    "options": ["Circle because 44 is odd", "Square box because 44 is even", "Both circle and square", "Neither"],
                    "ans": 1,
                    "hint": "44 ends in 4, so test if it is even or odd.",
                    "explanation": "44 ends in 4 (an even digit), so 44 is even and receives a square box marker.",
                    "sol": make_sol_html([
                        "Check the ones digit of 44: it is 4.",
                        "Since 4 is even, 44 is an even number.",
                        "According to the rule, even numbers are marked with square boxes."
                    ])
                },
                {
                    "id": 27,
                    "q": "If you open a textbook to a spread and the left page is page 56, what is the right page number?",
                    "options": ["Page 55", "Page 57", "Page 58", "Page 60"],
                    "ans": 1,
                    "hint": "The right page directly follows the left page in reading sequence.",
                    "explanation": "56 + 1 = 57. The right page is page 57.",
                    "sol": make_sol_html([
                        "Left page = 56 (an even page).",
                        "Right page = Left page + 1 = 56 + 1 = 57 (an odd page)."
                    ])
                },
                {
                    "id": 28,
                    "q": "What is the sum of facing pages 28 and 29, and what is its parity?",
                    "options": ["56, which is even", "57, which is odd", "58, which is even", "59, which is odd"],
                    "ans": 1,
                    "hint": "Add 28 + 29, then check the ones digit of the sum.",
                    "explanation": "28 + 29 = 57. Since 57 ends in 7, the sum is odd.",
                    "sol": make_sol_html([
                        "Calculate: 28 + 29 = 57.",
                        "Check parity: 57 ends in 7, which is an odd digit.",
                        "An even number + an odd number always produces an odd sum: 57 is odd."
                    ])
                },
                {
                    "id": 29,
                    "q": "Why is the left page of a printed book always an even number in standard publishing?",
                    "options": [
                        "Because books always start with page 0",
                        "Because page 1 starts on the right side of the first leaf, making its reverse page 2 on the left",
                        "Publishers choose page numbers at random",
                        "Because odd numbers cannot be printed on the left"
                    ],
                    "ans": 1,
                    "hint": "Consider the very first page (page 1) on the right side of the first sheet.",
                    "explanation": "Page 1 is on the recto (right). Its reverse side is page 2 (left), so all left pages are even.",
                    "sol": make_sol_html([
                        "Leaf 1 front = Page 1 (Right side).",
                        "Leaf 1 back = Page 2 (Left side).",
                        "Each subsequent sheet advances by 2 pages, keeping left pages even (2, 4, 6...) and right pages odd (1, 3, 5...)."
                    ])
                },
                {
                    "id": 30,
                    "q": "Which pair of numbers represents two facing pages in an open book?",
                    "options": ["Page 31 and Page 32", "Page 34 and Page 35", "Page 40 and Page 42", "Page 25 and Page 27"],
                    "ans": 1,
                    "hint": "Facing pages are consecutive: left page must be EVEN, right page must be ODD.",
                    "explanation": "Page 34 is even (left) and Page 35 is odd (right). Page 31 on left is impossible.",
                    "sol": make_sol_html([
                        "A facing spread requires: Left page = Even, Right page = Even + 1 (Odd).",
                        "In Option 1: 31 is odd, so it cannot be on the left of a spread.",
                        "In Option 2: 34 is even (left) and 35 is odd (right), which matches standard book format."
                    ])
                }
            ]
        },
        {
            "id": 20,
            "title": "Challenge 4",
            "section": "Mastery Challenges",
            "speech": "",
            "quiz": [
                {
                    "id": 31,
                    "q": "What is the single most important rule to determine if a multi-digit number like 4,785 is even or odd?",
                    "options": [
                        "Add all the digits together",
                        "Look only at the first digit on the left",
                        "Look only at the ones digit on the far right",
                        "Divide the whole number by 10"
                    ],
                    "ans": 2,
                    "hint": "All tens, hundreds, and thousands are multiples of 10, which are already even.",
                    "explanation": "Only the ones digit determines parity. Since 4,785 ends in 5, it is odd.",
                    "sol": make_sol_html([
                        "Multiples of 10, 100, and 1,000 are always even.",
                        "Parity is determined solely by the ones digit.",
                        "4,785 ends in 5, so it is odd."
                    ])
                },
                {
                    "id": 32,
                    "q": "Classify these four numbers: 30, 46, 78, 67. How many are even?",
                    "options": ["1 is even", "2 are even", "3 are even", "All 4 are even"],
                    "ans": 2,
                    "hint": "Check the ending digit of each: 0, 6, 8 are even; 7 is odd.",
                    "explanation": "30, 46, and 78 end in 0, 6, and 8 (even). 67 ends in 7 (odd). Thus, 3 are even.",
                    "sol": make_sol_html([
                        "30 ends in 0 -> Even.",
                        "46 ends in 6 -> Even.",
                        "78 ends in 8 -> Even.",
                        "67 ends in 7 -> Odd.",
                        "Total even numbers = 3."
                    ])
                },
                {
                    "id": 33,
                    "q": "Using the digits 3 and 8 without repetition, which 2-digit numbers can you form, and what is their parity?",
                    "options": [
                        "38 is odd, 83 is even",
                        "38 is even, 83 is odd",
                        "Both 38 and 83 are even",
                        "Both 38 and 83 are odd"
                    ],
                    "ans": 1,
                    "hint": "38 ends in 8; 83 ends in 3.",
                    "explanation": "38 ends in 8 (even), so 38 is even. 83 ends in 3 (odd), so 83 is odd.",
                    "sol": make_sol_html([
                        "Formed numbers: 38 and 83.",
                        "38 has ones digit 8 -> Even.",
                        "83 has ones digit 3 -> Odd."
                    ])
                },
                {
                    "id": 34,
                    "q": "If you are given two even digits (such as 4 and 6), can you form any odd 2-digit number using both?",
                    "options": ["Yes, by placing 4 first", "Yes, by placing 6 first", "No, impossible because both digits are even", "Only if you add 1"],
                    "ans": 2,
                    "hint": "Whichever digit is in the ones place will be an even digit.",
                    "explanation": "The formed numbers 46 and 64 both end in even digits, so both are always even.",
                    "sol": make_sol_html([
                        "Possible numbers: 46 and 64.",
                        "Both ones digits (6 and 4) are even.",
                        "Therefore, it is impossible to form an odd number using only even digits."
                    ])
                },
                {
                    "id": 35,
                    "q": "What are the immediate predecessor (number before) and successor (number after) of the odd number 75?",
                    "options": ["73 and 77 (both odd)", "74 and 76 (both even)", "74 and 77 (one even, one odd)", "75 has no neighbors"],
                    "ans": 1,
                    "hint": "75 - 1 = 74, and 75 + 1 = 76.",
                    "explanation": "The predecessor is 74 and successor is 76. Both end in even digits (4 and 6), so both are even.",
                    "sol": make_sol_html([
                        "Number before 75 = 75 - 1 = 74 (Even).",
                        "Number after 75 = 75 + 1 = 76 (Even).",
                        "Any odd number is always sandwiched between two even neighbors."
                    ])
                },
                {
                    "id": 36,
                    "q": "In a sequence of 6 consecutive whole numbers (for example 11, 12, 13, 14, 15, 16), how many are even and how many are odd?",
                    "options": ["2 even, 4 odd", "3 even, 3 odd", "4 even, 2 odd", "Depends on the starting number"],
                    "ans": 1,
                    "hint": "Consecutive numbers alternate strictly: odd, even, odd, even, odd, even.",
                    "explanation": "In any 6 consecutive numbers, there are exactly 3 pairs of (odd, even), yielding 3 odd and 3 even numbers.",
                    "sol": make_sol_html([
                        "Consecutive numbers alternate: O, E, O, E, O, E.",
                        "Count of Odd = 3.",
                        "Count of Even = 3.",
                        "They are perfectly balanced."
                    ])
                },
                {
                    "id": 37,
                    "q": "How many even numbers are there between 1 and 100 inclusive?",
                    "options": ["40", "45", "50", "55"],
                    "ans": 2,
                    "hint": "Exactly half of the 100 numbers are even.",
                    "explanation": "100 ÷ 2 = 50 even numbers (and 50 odd numbers).",
                    "sol": make_sol_html([
                        "The numbers 1 to 100 form 50 pairs of consecutive numbers (1,2), (3,4)... (99,100).",
                        "Each pair has 1 even number.",
                        "Total even numbers = 50 × 1 = 50."
                    ])
                },
                {
                    "id": 38,
                    "q": "What is the parity of the sum of two even numbers (such as 14 + 22 = 36)?",
                    "options": ["Always odd", "Always even", "Sometimes odd, sometimes even", "Always ends in 0"],
                    "ans": 1,
                    "hint": "Even numbers have zero remainder. Adding two zero remainders leaves zero remainder.",
                    "explanation": "Even + Even = Even. 14 + 22 = 36, which is even.",
                    "sol": make_sol_html([
                        "First even number: complete pairs with 0 remainder.",
                        "Second even number: complete pairs with 0 remainder.",
                        "Combined sum: all items pair up with 0 remainder -> Always Even."
                    ])
                },
                {
                    "id": 39,
                    "q": "What is the parity of the sum of two odd numbers (such as 9 + 13 = 22)?",
                    "options": ["Always odd", "Always even", "Sometimes odd, sometimes even", "Cannot be determined"],
                    "ans": 1,
                    "hint": "Each odd number has 1 leftover item. When added, the two leftovers pair up: 1 + 1 = 2.",
                    "explanation": "Odd + Odd = Even. The two remainders of 1 combine to form a complete pair.",
                    "sol": make_sol_html([
                        "First odd number leaves 1 remainder.",
                        "Second odd number leaves 1 remainder.",
                        "Combine remainders: 1 + 1 = 2, which forms a complete new pair.",
                        "Therefore, Odd + Odd is ALWAYS Even."
                    ])
                },
                {
                    "id": 40,
                    "q": "What is the parity of the sum of an even number and an odd number (such as 16 + 7 = 23)?",
                    "options": ["Always even", "Always odd", "Always zero", "Depends on which number is larger"],
                    "ans": 1,
                    "hint": "The even number has 0 remainder, while the odd number has 1 remainder: 0 + 1 = 1.",
                    "explanation": "Even + Odd = Odd. 16 + 7 = 23, which is odd.",
                    "sol": make_sol_html([
                        "Even number leaves 0 remainder.",
                        "Odd number leaves 1 remainder.",
                        "Total remainder = 0 + 1 = 1.",
                        "Since 1 leftover remains, Even + Odd is ALWAYS Odd."
                    ])
                }
            ]
        }
    ]

if __name__ == '__main__':
    slides = get_part3_slides()
    total_q = sum(len(s['quiz']) for s in slides)
    print(f"Total quiz questions: {total_q}")
    assert total_q == 40, f"Expected 40 questions, got {total_q}"
    print("All 40 questions verified successfully!")

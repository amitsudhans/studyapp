# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 (Challenge 1, 2, 3, 4) with 40 mastery questions,
hints, explanations, and popup step-by-step solutions for Class 4 Maths Chapter 4.
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
                    "q": "A community pantry receives 3 bags of flour (50 kg each) and 4 bags of rice (25 kg each). What is the total donation weight?",
                    "options": ["200 kg", "225 kg", "250 kg", "275 kg"],
                    "ans": 2,
                    "hint": "Calculate the flour weight (3 × 50) and rice weight (4 × 25), then add them together.",
                    "explanation": "Flour = 3 × 50 = 150 kg. Rice = 4 × 25 = 100 kg. Total = 150 + 100 = 250 kg.",
                    "sol": make_sol_html([
                        "Flour donation: 3 bags × 50 kg = 150 kg.",
                        "Rice donation: 4 bags × 25 kg = 100 kg.",
                        "Total weight = 150 kg + 100 kg = 250 kg."
                    ])
                },
                {
                    "id": 2,
                    "q": "In the number 325, what is the place value of the digit 2?",
                    "options": ["2 Ones (2)", "2 Tens (20)", "2 Hundreds (200)", "2 Thousands (2000)"],
                    "ans": 1,
                    "hint": "Identify the column: 3 is in Hundreds, 2 is in Tens, 5 is in Ones.",
                    "explanation": "The digit 2 is in the Tens place, representing 2 Tens = 20.",
                    "sol": make_sol_html([
                        "Place value analysis of 325:",
                        "3 is in Hundreds place -> 300.",
                        "2 is in Tens place -> 20.",
                        "5 is in Ones place -> 5.",
                        "The place value of 2 is 2 Tens or 20."
                    ])
                },
                {
                    "id": 3,
                    "q": "Why does the number 508 have 3 digits even though there are zero tens?",
                    "options": [
                        "Because zero can be ignored",
                        "Because zero acts as an essential placeholder holding the tens position",
                        "Because 508 is smaller than 100",
                        "Because 8 is in the tens place"
                    ],
                    "ans": 1,
                    "hint": "Without zero, 508 would be written as 58, which is only fifty-eight.",
                    "explanation": "Zero preserves the position of the 5 in the Hundreds column, representing 508 rather than 58.",
                    "sol": make_sol_html([
                        "508 represents 5 Hundreds, 0 Tens, and 8 Ones.",
                        "If zero were omitted, the numeral would become 58 (5 Tens and 8 Ones).",
                        "Therefore, zero acts as an active placeholder."
                    ])
                },
                {
                    "id": 4,
                    "q": "Using the digits 3, 7, and 0 without repetition, what is the SMALLEST valid 3-digit number you can form?",
                    "options": ["037", "073", "307", "370"],
                    "ans": 2,
                    "exp": "Zero cannot occupy the Hundreds place for a 3-digit number. Placing 3 in Hundreds, 0 in Tens, and 7 in Ones gives 307.",
                    "hint": "A 3-digit number cannot begin with 0. Pick the smallest non-zero digit first.",
                    "explanation": "307 is the smallest valid 3-digit number because 037 is a 2-digit number.",
                    "sol": make_sol_html([
                        "To form a valid 3-digit number, the Hundreds digit cannot be 0.",
                        "Smallest non-zero digit is 3 (Hundreds place).",
                        "Next smallest available digit is 0 (Tens place).",
                        "Final digit is 7 (Ones place).",
                        "Result: 307."
                    ])
                },
                {
                    "id": 5,
                    "q": "What is the LARGEST 3-digit number that can be formed using digits 5, 8, and 2 without repetition?",
                    "options": ["582", "825", "852", "285"],
                    "ans": 2,
                    "hint": "Place the digits in decreasing order from left to right.",
                    "explanation": "Arranging digits from largest to smallest: 8 in Hundreds, 5 in Tens, and 2 in Ones gives 852.",
                    "sol": make_sol_html([
                        "Available digits: 5, 8, 2.",
                        "Highest digit: 8 -> Hundreds place.",
                        "Next highest digit: 5 -> Tens place.",
                        "Smallest digit: 2 -> Ones place.",
                        "Largest number = 852."
                    ])
                },
                {
                    "id": 6,
                    "q": "What number is 10 less than 405?",
                    "options": ["305", "385", "395", "415"],
                    "ans": 2,
                    "hint": "Subtract 10 from 405: 400 - 10 = 390, then add 5.",
                    "explanation": "405 - 10 = 395.",
                    "sol": make_sol_html([
                        "Calculate: 405 - 10.",
                        "405 - 5 = 400.",
                        "400 - 5 = 395.",
                        "Result: 395."
                    ])
                },
                {
                    "id": 7,
                    "q": "What is the next number in this skip-counting sequence: 320, 310, 300, ___?",
                    "options": ["280", "290", "299", "309"],
                    "ans": 1,
                    "hint": "The sequence is counting backward by 10s: 300 - 10 = ___.",
                    "explanation": "Subtracting 10 from 300 gives 290.",
                    "sol": make_sol_html([
                        "Identify the rule: counting backward by 10.",
                        "320 - 10 = 310.",
                        "310 - 10 = 300.",
                        "300 - 10 = 290."
                    ])
                },
                {
                    "id": 8,
                    "q": "On a number line from 200 to 600, where does the number 400 sit?",
                    "options": [
                        "At the very beginning",
                        "At the exact center midpoint",
                        "Near the 600 mark",
                        "Between 200 and 300"
                    ],
                    "ans": 1,
                    "hint": "Calculate the midpoint between 200 and 600: (200 + 600) ÷ 2.",
                    "explanation": "The distance from 200 to 400 is 200, and from 400 to 600 is 200. Thus, 400 is the exact midpoint.",
                    "sol": make_sol_html([
                        "Range length = 600 - 200 = 400 units.",
                        "Half distance = 400 ÷ 2 = 200 units.",
                        "Midpoint position = 200 + 200 = 400.",
                        "400 sits at the exact center."
                    ])
                },
                {
                    "id": 9,
                    "q": "Which of these 3-digit numbers is strictly less than 550 and greater than 500?",
                    "options": ["495", "537", "555", "573"],
                    "ans": 1,
                    "hint": "Check which number satisfies 500 < number < 550.",
                    "explanation": "537 is greater than 500 and less than 550.",
                    "sol": make_sol_html([
                        "Test 495: less than 500 (No).",
                        "Test 555: greater than 550 (No).",
                        "Test 573: greater than 550 (No).",
                        "Test 537: between 500 and 550 (Yes!)."
                    ])
                },
                {
                    "id": 10,
                    "q": "If 145 diners are served lunch at 12:00 and 325 diners are served at 1:00, how many diners were served in total?",
                    "options": ["450 diners", "460 diners", "470 diners", "480 diners"],
                    "ans": 2,
                    "hint": "Add 145 + 325: (100 + 300) + (40 + 20) + (5 + 5).",
                    "explanation": "145 + 325 = 470 diners.",
                    "sol": make_sol_html([
                        "Hundreds: 100 + 300 = 400.",
                        "Tens: 40 + 20 = 60.",
                        "Ones: 5 + 5 = 10.",
                        "Total = 400 + 60 + 10 = 470 diners."
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
                    "q": "What happens when 1 unit is added to the number 999?",
                    "options": ["It becomes 9991", "It becomes 1000 (one thousand)", "It becomes 9100", "It becomes 1009"],
                    "ans": 1,
                    "hint": "999 + 1 bundles through Ones, Tens, and Hundreds into Thousands.",
                    "explanation": "999 + 1 = 1000, creating the smallest 4-digit number.",
                    "sol": make_sol_html([
                        "9 Ones + 1 = 10 Ones -> bundles into 1 Ten.",
                        "9 Tens + 1 Ten = 10 Tens -> bundles into 1 Hundred.",
                        "9 Hundreds + 1 Hundred = 10 Hundreds -> bundles into 1 Thousand.",
                        "Result = 1000."
                    ])
                },
                {
                    "id": 12,
                    "q": "How many flat hundred-blocks are needed to assemble a 1-thousand base-ten cube?",
                    "options": ["5 flats", "10 flats", "50 flats", "100 flats"],
                    "ans": 1,
                    "hint": "1000 ÷ 100 = ___.",
                    "explanation": "10 flat hundred-blocks stacked vertically equal 1000 (10 × 100 = 1000).",
                    "sol": make_sol_html([
                        "Each flat block represents 100 unit cubes.",
                        "Stacking 10 flats: 10 × 100 = 1000 unit cubes.",
                        "Exactly 10 hundred-flats are needed."
                    ])
                },
                {
                    "id": 13,
                    "q": "The ancient Indian place-value system was created approximately how many years ago?",
                    "options": ["100 years ago", "500 years ago", "2000 years ago", "10,000 years ago"],
                    "ans": 2,
                    "hint": "Indian scholars developed the base-10 positional notation around two millennia ago.",
                    "explanation": "The base-10 system was developed in India around 2,000 years ago.",
                    "sol": make_sol_html([
                        "Historical records show the Indian base-10 positional decimal system with zero emerged over 2000 years ago."
                    ])
                },
                {
                    "id": 14,
                    "q": "An adult male Indian rhinoceros weighs approximately 2,200 kg. How many thousands are in 2,200?",
                    "options": ["1 Thousand", "2 Thousands", "20 Thousands", "200 Thousands"],
                    "ans": 1,
                    "hint": "Check the Thousands place digit in 2200.",
                    "explanation": "In 2200, the digit in the Thousands place is 2 (2 Thousands = 2000).",
                    "sol": make_sol_html([
                        "Place value breakdown of 2200:",
                        "Thousands: 2 (2000).",
                        "Hundreds: 2 (200).",
                        "Tens: 0.",
                        "Ones: 0.",
                        "There are 2 Thousands."
                    ])
                },
                {
                    "id": 15,
                    "q": "Which of the following numbers is the greatest 3-digit whole number?",
                    "options": ["900", "990", "999", "1000"],
                    "ans": 2,
                    "hint": "1000 has 4 digits. Look for the largest number with 3 digits.",
                    "explanation": "999 is the largest 3-digit number. 1000 is a 4-digit number.",
                    "sol": make_sol_html([
                        "3-digit numbers end at 999.",
                        "The very next number, 1000, has 4 digits.",
                        "Therefore, 999 is the greatest 3-digit number."
                    ])
                },
                {
                    "id": 16,
                    "q": "How many ten-rods are equivalent to 1 thousand-cube?",
                    "options": ["10 ten-rods", "50 ten-rods", "100 ten-rods", "1000 ten-rods"],
                    "ans": 2,
                    "hint": "1 thousand has 10 hundreds, and each hundred has 10 ten-rods.",
                    "explanation": "10 × 10 = 100 ten-rods (100 × 10 = 1000).",
                    "sol": make_sol_html([
                        "1 ten-rod = 10 units.",
                        "1 hundred = 10 ten-rods.",
                        "1 thousand = 10 hundreds = 10 × 10 = 100 ten-rods."
                    ])
                },
                {
                    "id": 17,
                    "q": "Which of these real-world quantities would normally fall in the range '500 to 1000'?",
                    "options": [
                        "Students in a small classroom",
                        "Pages in a large comprehensive encyclopedia",
                        "Fingers on one human hand",
                        "Wheels on a bicycle"
                    ],
                    "ans": 1,
                    "hint": "Classroom students are in tens; human fingers are 5; bicycle wheels are 2.",
                    "explanation": "A thick book or encyclopedia commonly contains between 500 and 1000 pages.",
                    "sol": make_sol_html([
                        "Students in classroom: 20–40 (Tens scale).",
                        "Fingers: 5 (Units scale).",
                        "Bicycle wheels: 2 (Units scale).",
                        "Encyclopedia pages: 500–1000 (Hundreds scale)."
                    ])
                },
                {
                    "id": 18,
                    "q": "India has approximately 7,500 km of coastline. What is the value of the digit 7 in 7,500?",
                    "options": ["70", "700", "7,000", "70,000"],
                    "ans": 2,
                    "hint": "7 is in the leftmost column of a 4-digit number: the Thousands place.",
                    "explanation": "7 is in the Thousands place, so its value is 7,000.",
                    "sol": make_sol_html([
                        "In 7,500:",
                        "7 is in Thousands place -> 7,000.",
                        "5 is in Hundreds place -> 500.",
                        "0 is in Tens place -> 0.",
                        "0 is in Ones place -> 0."
                    ])
                },
                {
                    "id": 19,
                    "q": "What number is obtained by adding 10 to 995?",
                    "options": ["996", "1000", "1005", "1015"],
                    "ans": 2,
                    "hint": "995 + 5 = 1000, then add the remaining 5.",
                    "explanation": "995 + 10 = 1005.",
                    "sol": make_sol_html([
                        "995 + 5 = 1000.",
                        "1000 + 5 = 1005.",
                        "Result = 1005."
                    ])
                },
                {
                    "id": 20,
                    "q": "Why is the base-10 number system called 'positional'?",
                    "options": [
                        "Because digits can only be placed on paper",
                        "Because a digit's value changes based on the column or position it occupies",
                        "Because every number has exactly 10 digits",
                        "Because numbers cannot change position"
                    ],
                    "ans": 1,
                    "hint": "Consider the digit 5: in Ones it means 5, in Tens it means 50, in Hundreds it means 500.",
                    "explanation": "A positional system assigns value based on where a symbol sits within the numeral.",
                    "sol": make_sol_html([
                        "In a positional system, the place of a digit determines its multiplier.",
                        "Moving left increases the multiplier by 10× at each step."
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
                    "q": "What is the missing addend in the equation: 670 + ___ = 1000?",
                    "options": ["230", "330", "370", "430"],
                    "ans": 1,
                    "hint": "Subtract 670 from 1000: 1000 - 600 = 400, then 400 - 70 = ___.",
                    "explanation": "1000 - 670 = 330. Therefore, 670 + 330 = 1000.",
                    "sol": make_sol_html([
                        "1000 - 670 = ?",
                        "1000 - 600 = 400.",
                        "400 - 70 = 330.",
                        "Missing complement = 330."
                    ])
                },
                {
                    "id": 22,
                    "q": "What is the equivalent standard number for: 11 Tens + 14 Ones?",
                    "options": ["25", "114", "124", "1114"],
                    "ans": 2,
                    "hint": "11 Tens = 110, and 14 Ones = 14. Add 110 + 14.",
                    "explanation": "11 Tens = 110. 14 Ones = 14. 110 + 14 = 124.",
                    "sol": make_sol_html([
                        "11 Tens = 11 × 10 = 110.",
                        "14 Ones = 14.",
                        "Total = 110 + 14 = 124.",
                        "(Alternatively: 14 ones = 1 ten + 4 ones; 11 tens + 1 ten = 12 tens = 120; 120 + 4 = 124)."
                    ])
                },
                {
                    "id": 23,
                    "q": "Convert 2 Hundreds + 13 Tens + 7 Ones into a standard number:",
                    "options": ["2137", "337", "237", "347"],
                    "ans": 1,
                    "hint": "2 Hundreds = 200. 13 Tens = 130. 7 Ones = 7. Sum them up.",
                    "explanation": "200 + 130 + 7 = 337.",
                    "sol": make_sol_html([
                        "2 Hundreds = 200.",
                        "13 Tens = 130 (1 Hundred + 3 Tens).",
                        "7 Ones = 7.",
                        "Combine Hundreds: 200 + 100 = 300.",
                        "Total = 300 + 30 + 7 = 337."
                    ])
                },
                {
                    "id": 24,
                    "q": "Which number is represented by 4 blue thousand-tokens, 5 red hundred-tokens, 0 yellow ten-tokens, and 8 green one-tokens?",
                    "options": ["458", "4508", "4580", "4058"],
                    "ans": 1,
                    "hint": "Write the digits in order: Thousands (4), Hundreds (5), Tens (0), Ones (8).",
                    "explanation": "4 Thousands + 5 Hundreds + 0 Tens + 8 Ones = 4508.",
                    "sol": make_sol_html([
                        "Thousands place: 4.",
                        "Hundreds place: 5.",
                        "Tens place: 0.",
                        "Ones place: 8.",
                        "Standard number = 4508."
                    ])
                },
                {
                    "id": 25,
                    "q": "If you have 1000 and subtract 350, what is the remaining value?",
                    "options": ["550", "650", "750", "850"],
                    "ans": 1,
                    "hint": "1000 - 300 = 700, then 700 - 50 = ___.",
                    "explanation": "1000 - 350 = 650.",
                    "sol": make_sol_html([
                        "1000 - 300 = 700.",
                        "700 - 50 = 650.",
                        "Result = 650."
                    ])
                },
                {
                    "id": 26,
                    "q": "A student incorrectly wrote '4 Thousands 0 Hundreds 3 Tens 2 Ones' as 432. What is the correct 4-digit number?",
                    "options": ["4032", "4302", "4320", "40032"],
                    "ans": 0,
                    "hint": "Zero must hold the Hundreds place: 4 in Thousands, 0 in Hundreds, 3 in Tens, 2 in Ones.",
                    "explanation": "4032 is the correct 4-digit number. 432 is a 3-digit number where the Hundreds zero was omitted.",
                    "sol": make_sol_html([
                        "Thousands: 4.",
                        "Hundreds: 0 (must be included as a placeholder!).",
                        "Tens: 3.",
                        "Ones: 2.",
                        "Correct number = 4032."
                    ])
                },
                {
                    "id": 27,
                    "q": "What is the number name for 3019?",
                    "options": [
                        "Three hundred nineteen",
                        "Three thousand nineteen",
                        "Thirty thousand nineteen",
                        "Three thousand one hundred nine"
                    ],
                    "ans": 1,
                    "hint": "There are 3 thousands, 0 hundreds, and nineteen (19).",
                    "explanation": "3019 is read as 'Three thousand nineteen'.",
                    "sol": make_sol_html([
                        "3000 = Three thousand.",
                        "19 = Nineteen.",
                        "Combined: Three thousand nineteen."
                    ])
                },
                {
                    "id": 28,
                    "q": "What is the value of 1895 increased by 1?",
                    "options": ["1894", "1896", "1900", "1995"],
                    "ans": 1,
                    "hint": "Add 1 to the ones digit: 5 + 1 = 6.",
                    "explanation": "1895 + 1 = 1896.",
                    "sol": make_sol_html([
                        "1895 + 1 = 1896."
                    ])
                },
                {
                    "id": 29,
                    "q": "What number completes the addition fact: 830 + ___ = 1000?",
                    "options": ["130", "150", "170", "270"],
                    "ans": 2,
                    "hint": "1000 - 830: 830 + 70 = 900, 900 + 100 = 1000.",
                    "explanation": "830 + 170 = 1000.",
                    "sol": make_sol_html([
                        "830 + 70 = 900.",
                        "900 + 100 = 1000.",
                        "70 + 100 = 170."
                    ])
                },
                {
                    "id": 30,
                    "q": "How many tens are there in 500?",
                    "options": ["5 tens", "10 tens", "50 tens", "500 tens"],
                    "ans": 2,
                    "hint": "Divide 500 by 10: 500 ÷ 10 = ___.",
                    "explanation": "500 = 50 × 10, so there are 50 tens in 500.",
                    "sol": make_sol_html([
                        "1 hundred = 10 tens.",
                        "5 hundreds = 5 × 10 = 50 tens."
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
                    "q": "Which arrow cards are overlapped to form the number 5,648?",
                    "options": [
                        "5000, 600, 40, 8",
                        "500, 60, 4, 8",
                        "5000, 60, 48",
                        "5000, 640, 8"
                    ],
                    "ans": 0,
                    "hint": "Break down by place values: 5000 + 600 + 40 + 8.",
                    "explanation": "5000 + 600 + 40 + 8 = 5648.",
                    "sol": make_sol_html([
                        "Thousands card: 5000.",
                        "Hundreds card: 600.",
                        "Tens card: 40.",
                        "Ones card: 8.",
                        "Layered together, they show 5648."
                    ])
                },
                {
                    "id": 32,
                    "q": "Which symbol correctly compares these two numbers: 3,425 ___ 3,452?",
                    "options": [">", "<", "=", "+"],
                    "ans": 1,
                    "hint": "Thousands match (3), Hundreds match (4). Now compare Tens: 2 Tens vs 5 Tens.",
                    "explanation": "2 Tens is less than 5 Tens, so 3425 < 3452.",
                    "sol": make_sol_html([
                        "Compare Thousands: 3 = 3 (match).",
                        "Compare Hundreds: 4 = 4 (match).",
                        "Compare Tens: 2 < 5.",
                        "Therefore, 3425 < 3452."
                    ])
                },
                {
                    "id": 33,
                    "q": "Arrange these three mountain peak heights in DECREASING order (highest to lowest): Nanda Devi (7816 m), Kangchenjunga (8586 m), Chaukhamba (7138 m).",
                    "options": [
                        "7138 m, 7816 m, 8586 m",
                        "8586 m, 7816 m, 7138 m",
                        "8586 m, 7138 m, 7816 m",
                        "7816 m, 8586 m, 7138 m"
                    ],
                    "ans": 1,
                    "hint": "Start with the highest thousands digit: 8586 m is tallest.",
                    "explanation": "8586 m (Kangchenjunga) > 7816 m (Nanda Devi) > 7138 m (Chaukhamba).",
                    "sol": make_sol_html([
                        "Compare Thousands: 8000 > 7000.",
                        "Highest is 8586 m.",
                        "Next, compare 7816 m and 7138 m: 8 Hundreds > 1 Hundred.",
                        "Second highest is 7816 m, and lowest is 7138 m.",
                        "Decreasing order: 8586 m, 7816 m, 7138 m."
                    ])
                },
                {
                    "id": 34,
                    "q": "How many whole numbers exist strictly between 7000 and 8000?",
                    "options": ["998 numbers", "999 numbers", "1000 numbers", "1001 numbers"],
                    "ans": 1,
                    "hint": "The numbers run from 7001 to 7999 inclusive.",
                    "explanation": "Count = 7999 - 7001 + 1 = 999 numbers.",
                    "sol": make_sol_html([
                        "First number after 7000 is 7001.",
                        "Last number before 8000 is 7999.",
                        "Total count = 7999 - 7001 + 1 = 998 + 1 = 999 numbers."
                    ])
                },
                {
                    "id": 35,
                    "q": "Using the 4 digits 2, 3, 4, and 7 without repetition, how many unique 4-digit numbers can be formed?",
                    "options": ["12 numbers", "16 numbers", "20 numbers", "24 numbers"],
                    "ans": 3,
                    "hint": "There are 4 choices for Thousands, 3 for Hundreds, 2 for Tens, and 1 for Ones: 4 × 3 × 2 × 1.",
                    "explanation": "4 × 3 × 2 × 1 = 24 unique 4-digit numbers.",
                    "sol": make_sol_html([
                        "Thousands position: 4 choices (2, 3, 4, 7).",
                        "Hundreds position: 3 choices remaining.",
                        "Tens position: 2 choices remaining.",
                        "Ones position: 1 choice remaining.",
                        "Total combinations = 4 × 3 × 2 × 1 = 24 numbers."
                    ])
                },
                {
                    "id": 36,
                    "q": "Which of the following numbers lies strictly between 5,500 and 5,700?",
                    "options": ["5490", "5595", "5720", "5800"],
                    "ans": 1,
                    "hint": "5595 is greater than 5500 and less than 5700.",
                    "explanation": "5500 < 5595 < 5700.",
                    "sol": make_sol_html([
                        "5490 < 5500 (too small).",
                        "5720 > 5700 (too large).",
                        "5800 > 5700 (too large).",
                        "5595 lies strictly between 5500 and 5700."
                    ])
                },
                {
                    "id": 37,
                    "q": "What is the smallest 4-digit number that can be formed using digits 2, 3, 4, and 7 without repetition?",
                    "options": ["2347", "2374", "2437", "7432"],
                    "ans": 0,
                    "hint": "Place the digits in increasing order: 2, 3, 4, 7.",
                    "explanation": "2347 is the smallest 4-digit combination.",
                    "sol": make_sol_html([
                        "Smallest digit in Thousands: 2.",
                        "Next smallest in Hundreds: 3.",
                        "Next smallest in Tens: 4.",
                        "Largest in Ones: 7.",
                        "Result = 2347."
                    ])
                },
                {
                    "id": 38,
                    "q": "A legendary cricketer scored 7,805 career runs. An international captain scored 5,114 runs. How many more runs did the legendary cricketer score?",
                    "options": ["2,691 runs", "2,709 runs", "2,791 runs", "2,811 runs"],
                    "ans": 0,
                    "hint": "Subtract: 7805 - 5114.",
                    "explanation": "7805 - 5114 = 2691 runs.",
                    "sol": make_sol_html([
                        "7805 - 5114:",
                        "Ones: 5 - 4 = 1.",
                        "Tens: 0 - 1 -> borrow 1 from 8 Hundreds -> 10 - 1 = 9.",
                        "Hundreds: 7 - 1 = 6.",
                        "Thousands: 7 - 5 = 2.",
                        "Difference = 2,691 runs."
                    ])
                },
                {
                    "id": 39,
                    "q": "Which appliance price is the CHEAPEST among ₹1986, ₹1099, and ₹1899?",
                    "options": ["₹1986", "₹1899", "₹1099", "All are the same"],
                    "ans": 2,
                    "hint": "Compare the hundreds place: 0 Hundreds vs 8 Hundreds vs 9 Hundreds.",
                    "explanation": "₹1099 has 0 Hundreds, making it the least expensive appliance.",
                    "sol": make_sol_html([
                        "Thousands digit is 1 for all three.",
                        "Hundreds: 0 (1099) < 8 (1899) < 9 (1986).",
                        "Therefore, ₹1099 is the cheapest."
                    ])
                },
                {
                    "id": 40,
                    "q": "If you compare 8,000 and 7,999, which statement correctly applies the left-to-right comparison rule?",
                    "options": [
                        "7999 is larger because 9 is larger than 0",
                        "8000 is larger because 8 Thousands is greater than 7 Thousands",
                        "They are equal because 7999 is close to 8000",
                        "Comparison depends on the ones digit"
                    ],
                    "ans": 1,
                    "hint": "Always compare the highest place value (Thousands) first.",
                    "explanation": "8 Thousands > 7 Thousands, so 8000 > 7999 regardless of lower digits.",
                    "sol": make_sol_html([
                        "Start at the leftmost column: Thousands place.",
                        "8000 has 8 Thousands.",
                        "7999 has 7 Thousands.",
                        "Since 8 > 7, 8000 is greater immediately."
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

#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4)
Each Challenge contains 10 rigorous, curriculum-aligned questions (40 questions total).
Zero human character names.
Includes options, hint, explanation, and 3-step structured solutions.
"""

challenges = [
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Mastery Challenge on Large 3-Digit Place Values, Rice Sack Tiles & Number Lines",
        "questions": [
            {
                "question": "What is the expanded form of the number 947?",
                "options": ["900 + 40 + 7", "90 + 40 + 7", "900 + 4 + 7", "900 + 70 + 4"],
                "answer": 0,
                "hint": "Break down 947 into hundreds, tens, and ones.",
                "explanation": "947 consists of 9 hundreds (900), 4 tens (40), and 7 ones (7): 900 + 40 + 7.",
                "solution_steps": [
                    "Step 1: Identify the hundreds digit = 9, value = 900.",
                    "Step 2: Identify the tens digit = 4, value = 40; ones digit = 7, value = 7.",
                    "Step 3: Combine in expanded form: 900 + 40 + 7."
                ]
            },
            {
                "question": "A warehouse holds 832 rice sacks. How many ten-rods are needed to represent this in tiles?",
                "options": ["8 rods", "3 rods", "2 rods", "30 rods"],
                "answer": 1,
                "hint": "Look at the digit in the tens column of 832.",
                "explanation": "In 832, the digit in the tens place is 3, which requires 3 ten-rods.",
                "solution_steps": [
                    "Step 1: In the number 832, 8 is hundreds, 3 is tens, and 2 is ones.",
                    "Step 2: Each ten-rod represents 10 units (1 ten).",
                    "Step 3: Therefore, 3 ten-rods are needed."
                ]
            },
            {
                "question": "Which number lies on the number line between 600 and 700, and is closer to 600?",
                "options": ["685", "650", "628", "710"],
                "answer": 2,
                "hint": "A number closer to 600 must be less than 650.",
                "explanation": "628 is between 600 and 700, and because 628 < 650, it is closer to 600.",
                "solution_steps": [
                    "Step 1: The midpoint of 600 and 700 is 650.",
                    "Step 2: Numbers less than 650 lie closer to 600.",
                    "Step 3: 628 < 650, so 628 is closer to 600."
                ]
            },
            {
                "question": "What number is formed by 6 hundred tiles, 2 ten rods, and 0 unit tiles?",
                "options": ["602", "620", "260", "622"],
                "answer": 1,
                "hint": "6 hundreds = 600, 2 tens = 20, 0 units = 0.",
                "explanation": "600 + 20 + 0 = 620.",
                "solution_steps": [
                    "Step 1: 6 hundred tiles = 6 × 100 = 600.",
                    "Step 2: 2 ten rods = 2 × 10 = 20.",
                    "Step 3: 600 + 20 = 620."
                ]
            },
            {
                "question": "What are the neighboring tens for the number 726?",
                "options": ["710 and 720", "720 and 730", "700 and 800", "725 and 727"],
                "answer": 1,
                "hint": "Find the multiples of 10 just below and above 726.",
                "explanation": "726 is bounded by 720 and 730.",
                "solution_steps": [
                    "Step 1: The multiple of 10 below 726 is 720.",
                    "Step 2: The multiple of 10 above 726 is 730.",
                    "Step 3: The neighboring tens are 720 and 730."
                ]
            },
            {
                "question": "A crane hops in strides of 10 from 750. After 3 hops, where does it land?",
                "options": ["770", "780", "790", "800"],
                "answer": 1,
                "hint": "Add 3 × 10 = 30 to 750.",
                "explanation": "750 + (3 × 10) = 750 + 30 = 780.",
                "solution_steps": [
                    "Step 1: Each hop is 10 units. 3 hops = 3 × 10 = 30 units.",
                    "Step 2: Start point = 750.",
                    "Step 3: 750 + 30 = 780."
                ]
            },
            {
                "question": "What is the place value of 0 in the number 504?",
                "options": ["0", "10", "100", "50"],
                "answer": 0,
                "hint": "Zero multiplied by any place value is zero.",
                "explanation": "The digit 0 in the tens place has a place value of 0 × 10 = 0.",
                "solution_steps": [
                    "Step 1: The digit 0 occupies the tens column.",
                    "Step 2: Its value is 0 × 10.",
                    "Step 3: 0 × 10 = 0."
                ]
            },
            {
                "question": "Which of these numbers is closest to 900 on a number line?",
                "options": ["840", "870", "895", "920"],
                "answer": 2,
                "hint": "Calculate the difference from 900: |895 - 900| = 5.",
                "explanation": "895 is only 5 units away from 900, which is closer than any other option.",
                "solution_steps": [
                    "Step 1: Compare differences: |840-900|=60, |870-900|=30, |895-900|=5, |920-900|=20.",
                    "Step 2: The smallest difference is 5.",
                    "Step 3: 895 is closest to 900."
                ]
            },
            {
                "question": "What number is 10 more than 590?",
                "options": ["595", "600", "605", "610"],
                "answer": 1,
                "hint": "Add 10 to 590: 590 + 10.",
                "explanation": "590 + 10 = 600.",
                "solution_steps": [
                    "Step 1: Start at 590.",
                    "Step 2: Add 1 ten: 590 + 10.",
                    "Step 3: 590 + 10 = 600."
                ]
            },
            {
                "question": "In the number 855, what is the value of the 5 in the tens place compared to the 5 in the ones place?",
                "options": ["Equal value", "10 times greater", "10 times smaller", "100 times greater"],
                "answer": 1,
                "hint": "Tens place is 50; ones place is 5. Compare 50 to 5.",
                "explanation": "The 5 in the tens place is 50, which is 10 times greater than the 5 in the ones place (5).",
                "solution_steps": [
                    "Step 1: Value of 5 in tens place = 50.",
                    "Step 2: Value of 5 in ones place = 5.",
                    "Step 3: 50 ÷ 5 = 10. It is 10 times greater."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Mastery Challenge on Bounding Fifties, Tambola Clues & Number Expressions",
        "questions": [
            {
                "question": "What are the neighboring fifties for the number 672?",
                "options": ["600 and 650", "650 and 700", "670 and 680", "600 and 700"],
                "answer": 1,
                "hint": "Multiples of 50 just below and above 672.",
                "explanation": "672 lies between the multiples of fifty: 650 and 700.",
                "solution_steps": [
                    "Step 1: Multiple of 50 below 672 is 650.",
                    "Step 2: Multiple of 50 above 672 is 700.",
                    "Step 3: The neighboring fifties are 650 and 700."
                ]
            },
            {
                "question": "A Tambola clue says: 'I have 7 hundreds, 3 tens, and 6 ones.' What number is it?",
                "options": ["763", "736", "673", "376"],
                "answer": 1,
                "hint": "Write hundreds, tens, and ones: 7, 3, 6.",
                "explanation": "7 hundreds + 3 tens + 6 ones = 736.",
                "solution_steps": [
                    "Step 1: Hundreds = 7.",
                    "Step 2: Tens = 3, Ones = 6.",
                    "Step 3: Number = 736."
                ]
            },
            {
                "question": "Which of these expressions does NOT equal 400?",
                "options": ["350 + 50", "500 - 100", "250 + 150", "300 + 90"],
                "answer": 3,
                "hint": "Check the sums: 300 + 90 = 390.",
                "explanation": "300 + 90 = 390, which does not equal 400.",
                "solution_steps": [
                    "Step 1: 350 + 50 = 400.",
                    "Step 2: 500 - 100 = 400; 250 + 150 = 400.",
                    "Step 3: 300 + 90 = 390 != 400. Option D is correct."
                ]
            },
            {
                "question": "What is the missing number in the sequence: 510, 520, 530, __, 550?",
                "options": ["535", "540", "545", "560"],
                "answer": 1,
                "hint": "The sequence skips by 10.",
                "explanation": "530 + 10 = 540.",
                "solution_steps": [
                    "Step 1: Find rule: 520 - 510 = 10.",
                    "Step 2: Add 10 to 530: 530 + 10 = 540.",
                    "Step 3: The missing number is 540."
                ]
            },
            {
                "question": "Which expression represents 555?",
                "options": ["500 + 50 + 5", "500 + 55", "600 - 45", "All of the above"],
                "answer": 3,
                "hint": "Check each expression: all equal 555.",
                "explanation": "500 + 50 + 5 = 555; 500 + 55 = 555; 600 - 45 = 555. All are valid.",
                "solution_steps": [
                    "Step 1: 500 + 50 + 5 = 555.",
                    "Step 2: 500 + 55 = 555; 600 - 45 = 555.",
                    "Step 3: Therefore, all of the above are correct."
                ]
            },
            {
                "question": "A Tambola clue asks for: '20 less than 610'. What is the number?",
                "options": ["580", "590", "600", "630"],
                "answer": 1,
                "hint": "Subtract 20 from 610: 610 - 20.",
                "explanation": "610 - 20 = 590.",
                "solution_steps": [
                    "Step 1: Start with 610.",
                    "Step 2: Subtract 20: 610 - 10 = 600, 600 - 10 = 590.",
                    "Step 3: The number is 590."
                ]
            },
            {
                "question": "What is the step size in the sequence: 400, 425, 450, 475, 500?",
                "options": ["10", "15", "20", "25"],
                "answer": 3,
                "hint": "Subtract consecutive terms: 425 - 400.",
                "explanation": "Each term increases by 25 (425 - 400 = 25).",
                "solution_steps": [
                    "Step 1: Subtract first term from second: 425 - 400 = 25.",
                    "Step 2: Check next: 450 - 425 = 25.",
                    "Step 3: The step size is 25."
                ]
            },
            {
                "question": "Which number is bounded between 800 and 900, and has 0 in the tens place?",
                "options": ["850", "805", "905", "855"],
                "answer": 1,
                "hint": "Hundreds digit is 8, tens digit is 0.",
                "explanation": "805 is between 800 and 900, and its tens digit is 0.",
                "solution_steps": [
                    "Step 1: Check range 800 to 900: 805, 850, 855 qualify.",
                    "Step 2: Check tens place: in 805, tens digit is 0.",
                    "Step 3: The correct number is 805."
                ]
            },
            {
                "question": "How can 775 be written using addition and subtraction?",
                "options": ["800 - 25", "700 + 75", "750 + 25", "All of the above"],
                "answer": 3,
                "hint": "All three expressions calculate to 775.",
                "explanation": "800 - 25 = 775; 700 + 75 = 775; 750 + 25 = 775.",
                "solution_steps": [
                    "Step 1: 800 - 25 = 775.",
                    "Step 2: 700 + 75 = 775; 750 + 25 = 775.",
                    "Step 3: All expressions are valid representations of 775."
                ]
            },
            {
                "question": "What is the next number in the pattern: 810, 840, 870, __?",
                "options": ["890", "900", "910", "920"],
                "answer": 1,
                "hint": "The sequence skips by 30: 870 + 30.",
                "explanation": "The step size is +30. 870 + 30 = 900.",
                "solution_steps": [
                    "Step 1: Find step: 840 - 810 = 30.",
                    "Step 2: Add 30 to 870: 870 + 30.",
                    "Step 3: 870 + 30 = 900."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Mastery Challenge on Magnitude Ranges, Number Riddles & Pattern Detective",
        "questions": [
            {
                "question": "Which magnitude range best fits the number of pages in a typical school textbook?",
                "options": ["0 to 10", "10 to 100", "100 to 1,000", "Over 10,000"],
                "answer": 2,
                "hint": "A textbook usually has between 100 and 300 pages.",
                "explanation": "Textbooks typically have around 150 to 300 pages, falling in the 100 to 1,000 range.",
                "solution_steps": [
                    "Step 1: Estimate textbook thickness: about 150-250 pages.",
                    "Step 2: Match to ranges: greater than 100, less than 1,000.",
                    "Step 3: The correct range is 100 to 1,000."
                ]
            },
            {
                "question": "Which of these numbers is a step-up sequence where digits increase consecutively?",
                "options": ["876", "345", "555", "353"],
                "answer": 1,
                "hint": "Look for digits that count up: 3, 4, 5.",
                "explanation": "In 345, each digit increases by 1 (3 -> 4 -> 5), forming a step-up sequence.",
                "solution_steps": [
                    "Step 1: Check 876: decreasing (step-down).",
                    "Step 2: Check 345: 3, 4, 5 are increasing consecutively.",
                    "Step 3: 345 is a step-up sequence."
                ]
            },
            {
                "question": "What is the number described by: 'One century plus 3 tens'?",
                "options": ["103", "130", "133", "301"],
                "answer": 1,
                "hint": "One century = 100; 3 tens = 30.",
                "explanation": "100 + 30 = 130.",
                "solution_steps": [
                    "Step 1: One century = 100.",
                    "Step 2: 3 tens = 30.",
                    "Step 3: 100 + 30 = 130."
                ]
            },
            {
                "question": "Which of the following is a palindromic number?",
                "options": ["474", "475", "574", "744"],
                "answer": 0,
                "hint": "A palindrome reads the same backwards and forwards.",
                "explanation": "474 reads as 4-7-4 in both directions, making it a palindrome.",
                "solution_steps": [
                    "Step 1: Reverse the digits of 474: 4-7-4.",
                    "Step 2: Since original equals reversed, it is a palindrome.",
                    "Step 3: Option A is correct."
                ]
            },
            {
                "question": "What kind of number is 888?",
                "options": ["A twin number", "A triplet number", "A step-down number", "A prime number"],
                "answer": 1,
                "hint": "All three digits are identical.",
                "explanation": "888 has three identical digits, so it is classified as a triplet number.",
                "solution_steps": [
                    "Step 1: Examine digits: 8, 8, 8.",
                    "Step 2: Three identical digits form a triplet.",
                    "Step 3: 888 is a triplet number."
                ]
            },
            {
                "question": "Which number matches the riddle: 'Two centuries minus one half century'?",
                "options": ["100", "150", "200", "250"],
                "answer": 1,
                "hint": "Two centuries = 200; half century = 50. Subtract: 200 - 50.",
                "explanation": "200 - 50 = 150.",
                "solution_steps": [
                    "Step 1: Two centuries = 2 × 100 = 200.",
                    "Step 2: Half century = 50.",
                    "Step 3: 200 - 50 = 150."
                ]
            },
            {
                "question": "Which of these is a step-down number sequence?",
                "options": ["123", "654", "456", "789"],
                "answer": 1,
                "hint": "Digits decrease consecutively from left to right: 6, 5, 4.",
                "explanation": "In 654, digits decrease by 1 consecutively (6 -> 5 -> 4).",
                "solution_steps": [
                    "Step 1: Inspect digit progression: 6, 5, 4.",
                    "Step 2: Each digit is 1 less than the previous.",
                    "Step 3: 654 is a step-down sequence."
                ]
            },
            {
                "question": "Which magnitude range best fits the population of a large city?",
                "options": ["0 to 10", "10 to 100", "100 to 1,000", "Over 1,000"],
                "answer": 3,
                "hint": "A city has tens of thousands or millions of residents.",
                "explanation": "City populations are in the hundreds of thousands or millions, far exceeding 1,000.",
                "solution_steps": [
                    "Step 1: A city has many thousands of inhabitants.",
                    "Step 2: Compare against ranges: exceeds 1,000.",
                    "Step 3: The correct range is 'Over 1,000'."
                ]
            },
            {
                "question": "Which number is 'one step before one century'?",
                "options": ["90", "98", "99", "101"],
                "answer": 2,
                "hint": "One century is 100. 100 - 1 = ?",
                "explanation": "One step before 100 is 99.",
                "solution_steps": [
                    "Step 1: One century = 100.",
                    "Step 2: One step before = 100 - 1.",
                    "Step 3: 100 - 1 = 99."
                ]
            },
            {
                "question": "How many palindromic numbers exist between 100 and 120?",
                "options": ["0", "1 (only 101)", "2 (101 and 111)", "3 (101, 111, 121)"],
                "answer": 2,
                "hint": "Check numbers between 100 and 120: 101 and 111.",
                "explanation": "Between 100 and 120, the palindromes are 101 and 111 (121 is not strictly between 100 and 120).",
                "solution_steps": [
                    "Step 1: Test numbers: 101 is a palindrome (1-0-1).",
                    "Step 2: 111 is a palindrome (1-1-1).",
                    "Step 3: Exactly 2 palindromic numbers exist in this interval."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Mastery Challenge on Paper Slips, Permutations & Bhutasankhya Word Numerals",
        "questions": [
            {
                "question": "Using 6 paper slips labeled 100, 10, or 1, what is the value of 3 slips of 100, 2 slips of 10, and 1 slip of 1?",
                "options": ["321", "312", "231", "320"],
                "answer": 0,
                "hint": "(3 × 100) + (2 × 10) + (1 × 1) = 300 + 20 + 1.",
                "explanation": "300 + 20 + 1 = 321.",
                "solution_steps": [
                    "Step 1: 3 slips of 100 = 300.",
                    "Step 2: 2 slips of 10 = 20; 1 slip of 1 = 1.",
                    "Step 3: Total = 300 + 20 + 1 = 321."
                ]
            },
            {
                "question": "How many 3-digit numbers can be formed using ONLY the digits 3 and 8 with repetition allowed?",
                "options": ["4 numbers", "6 numbers", "8 numbers", "9 numbers"],
                "answer": 2,
                "hint": "2 choices for hundreds × 2 for tens × 2 for ones = 2 × 2 × 2.",
                "explanation": "2 × 2 × 2 = 8 distinct three-digit numbers.",
                "solution_steps": [
                    "Step 1: Hundreds place has 2 options (3 or 8).",
                    "Step 2: Tens place has 2 options, Ones place has 2 options.",
                    "Step 3: 2 × 2 × 2 = 8 numbers."
                ]
            },
            {
                "question": "What is the largest 3-digit number formed using only the digits 3 and 8?",
                "options": ["838", "883", "888", "388"],
                "answer": 2,
                "hint": "Place the largest digit (8) in all three places.",
                "explanation": "888 has the maximum digit 8 in all three place value positions.",
                "solution_steps": [
                    "Step 1: To maximize, pick the largest digit 8 for the hundreds place.",
                    "Step 2: Pick 8 for the tens place and 8 for the ones place.",
                    "Step 3: The maximum number is 888."
                ]
            },
            {
                "question": "In the ancient Bhutasankhya tradition, which number is represented by 'Eyes'?",
                "options": ["1", "2", "3", "4"],
                "answer": 1,
                "hint": "Humans have a pair of 2 eyes.",
                "explanation": "'Eyes' symbolizes the numeral 2 because of the natural pair of eyes.",
                "solution_steps": [
                    "Step 1: In Bhutasankhya, paired body parts symbolize 2.",
                    "Step 2: 'Eyes' represents 2.",
                    "Step 3: Option B is correct."
                ]
            },
            {
                "question": "In Bhutasankhya, which number does 'Palm' represent?",
                "options": ["2", "5", "7", "10"],
                "answer": 1,
                "hint": "A palm has 5 fingers.",
                "explanation": "'Palm' represents the number 5 because a hand palm has 5 fingers.",
                "solution_steps": [
                    "Step 1: Count fingers on a human palm = 5.",
                    "Step 2: 'Palm' symbolizes 5.",
                    "Step 3: Option B is correct."
                ]
            },
            {
                "question": "What number does 'Trikala' represent in the Bhutasankhya system?",
                "options": ["2", "3", "4", "6"],
                "answer": 1,
                "hint": "'Tri' means three (past, present, future).",
                "explanation": "'Trikala' refers to the three aspects of time, representing 3.",
                "solution_steps": [
                    "Step 1: Trikala refers to 3 times (past, present, future).",
                    "Step 2: Prefix 'Tri' means 3.",
                    "Step 3: Therefore, it represents 3."
                ]
            },
            {
                "question": "If 'Moon' represents 1 and 'Palm' represents 5, what number is represented by 1 ten and 5 ones?",
                "options": ["15", "51", "105", "501"],
                "answer": 0,
                "hint": "1 ten (10) + 5 ones (5) = 15.",
                "explanation": "1 ten and 5 ones forms the number 15.",
                "solution_steps": [
                    "Step 1: Tens digit = 1.",
                    "Step 2: Ones digit = 5.",
                    "Step 3: The number is 15."
                ]
            },
            {
                "question": "Which of these is the correct ascending order for 3-digit numbers made from digits 3 and 8?",
                "options": ["333, 338, 383, 388", "388, 383, 338, 333", "888, 883, 838, 833", "338, 333, 388, 383"],
                "answer": 0,
                "hint": "Ascending order means from smallest to largest.",
                "explanation": "333 < 338 < 383 < 388 is strictly ascending.",
                "solution_steps": [
                    "Step 1: Compare hundreds: all start with 3.",
                    "Step 2: Compare tens: 333 and 338 have 3 tens, followed by 383 and 388 with 8 tens.",
                    "Step 3: Ascending order: 333, 338, 383, 388."
                ]
            },
            {
                "question": "What is the minimum number that can be made using 6 paper slips labeled 100, 10, or 1?",
                "options": ["1", "6", "10", "60"],
                "answer": 1,
                "hint": "Use 6 slips of 1: 6 × 1 = 6.",
                "explanation": "Choosing the smallest value (1) for all 6 slips gives 6 × 1 = 6.",
                "solution_steps": [
                    "Step 1: To minimize total, choose the smallest available value (1).",
                    "Step 2: 6 slips of 1 = 6 × 1.",
                    "Step 3: 6 × 1 = 6."
                ]
            },
            {
                "question": "What is the rule 'ankanam vamato gatih' in the ancient Indian numeral tradition?",
                "options": ["Numbers move from left to right", "Numbers move from right to left (units first, then tens, then hundreds)", "Numbers must always be even", "Numbers cannot exceed 100"],
                "answer": 1,
                "hint": "'Vamato gatih' means moving towards the left (units on right, tens on left).",
                "explanation": "'Ankanam vamato gatih' states that numerals proceed from right to left, placing units first, then tens, then hundreds.",
                "solution_steps": [
                    "Step 1: Translate the Sanskrit principle: ankanam (of numbers) vamato (towards the left) gatih (is the motion).",
                    "Step 2: In verse reading, units are named first, then tens to the left.",
                    "Step 3: Option B correctly defines the principle."
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

# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 9: Coconut Farm
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4: 40 Questions total)
"""

challenge_slides = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Foundations, Fact Triangles, Zero Patterns & Splitting",
        "lecture": "Welcome to Mastery Challenge 1. In this interactive session, you will test your understanding of division as the inverse of multiplication, number fact triangles, zero cancellation shortcuts, and mental dividend splitting.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Test your mastery of foundational division facts, place value patterns, and mental splitting strategies. Answer all 10 questions to unlock detailed step-by-step solutions!</p>",
        "questions": [
            {
                "id": "q1",
                "question": "In the mathematical equation 96 ÷ 8 = 12, what is the specific mathematical term for the number 8?",
                "options": [
                    "Dividend",
                    "Divisor",
                    "Quotient",
                    "Remainder"
                ],
                "answer": 1,
                "hint": "8 is the number of equal groups into which the total is being partitioned.",
                "explanation": "In 96 ÷ 8 = 12, 96 is the Dividend (N), 8 is the Divisor (D), and 12 is the Quotient (Q).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        <strong>Division Terminology Breakdown:</strong>
                        <ul class='list-disc list-inside mt-1 space-y-1 text-slate-300'>
                            <li><strong>96 (Dividend, N):</strong> The total quantity to be divided.</li>
                            <li><strong>8 (Divisor, D):</strong> The number of equal groups dividing the total.</li>
                            <li><strong>12 (Quotient, Q):</strong> The size or result of each equal part.</li>
                        </ul>
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Divisor</p>
                </div>
                """
            },
            {
                "id": "q2",
                "question": "From the multiplication fact 40 × 50 = 2,000, which of the following is an authentic derived division fact?",
                "options": [
                    "2,000 ÷ 40 = 50",
                    "2,000 ÷ 20 = 100",
                    "2,000 ÷ 5 = 40",
                    "40 ÷ 2,000 = 50"
                ],
                "answer": 0,
                "hint": "Divide the product (2,000) by one factor (40) to obtain the other factor (50).",
                "explanation": "Since 40 × 50 = 2,000, dividing 2,000 by 40 yields 50, and dividing 2,000 by 50 yields 40.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Multiplication: 40 × 50 = 2,000<br>
                        Derived Fact 1: 2,000 ÷ 40 = 50<br>
                        Derived Fact 2: 2,000 ÷ 50 = 40
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 2,000 ÷ 40 = 50</p>
                </div>
                """
            },
            {
                "id": "q3",
                "question": "In a number fact triangle, the top product box is 540, and the bottom-right node is 60. What number belongs in the bottom-left node?",
                "options": [
                    "9",
                    "90",
                    "8",
                    "6"
                ],
                "answer": 0,
                "hint": "Divide 540 by 60 by canceling one zero.",
                "explanation": "540 ÷ 60 = 54 ÷ 6 = 9. So the missing factor is 9.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Peak = 540<br>
                        Known Factor = 60<br>
                        Missing Factor = 540 ÷ 60 = 54 ÷ 6 = 9
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 9</p>
                </div>
                """
            },
            {
                "id": "q4",
                "question": "Evaluate 64,000 ÷ 80 using the trailing zero cancellation shortcut:",
                "options": [
                    "80",
                    "800",
                    "8,000",
                    "8"
                ],
                "answer": 1,
                "hint": "Cancel 1 zero from both 64,000 and 80: 6,400 ÷ 8.",
                "explanation": "64,000 ÷ 80: Cancel one zero from each side to get 6,400 ÷ 8. Since 64 ÷ 8 = 8, 6,400 ÷ 8 = 800.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        64,000 ÷ 80<br>
                        = (64,000 ÷ 10) ÷ (80 ÷ 10)<br>
                        = 6,400 ÷ 8 = 800
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 800</p>
                </div>
                """
            },
            {
                "id": "q5",
                "question": "A fruit trader packs 3,600 oranges equally into crates of 90 oranges each. How many crates are filled?",
                "options": [
                    "4 crates",
                    "40 crates",
                    "400 crates",
                    "45 crates"
                ],
                "answer": 1,
                "hint": "Cancel one zero: 360 ÷ 9 = 40.",
                "explanation": "3,600 ÷ 90 = 360 ÷ 9 = 40 crates.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Oranges = 3,600<br>
                        Per Crate = 90<br>
                        Crates = 3,600 ÷ 90 = 360 ÷ 9 = 40 crates
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 40 crates</p>
                </div>
                """
            },
            {
                "id": "q6",
                "question": "Using convenient additive splitting, what is the best mental decomposition to solve 1,854 ÷ 6?",
                "options": [
                    "(1,800 ÷ 6) + (54 ÷ 6) = 300 + 9 = 309",
                    "(1,000 ÷ 6) + (854 ÷ 6) = 166 + 143",
                    "(1,800 ÷ 6) + (54 ÷ 6) = 30 + 9 = 39",
                    "(1,200 ÷ 6) + (654 ÷ 6) = 200 + 109 = 309"
                ],
                "answer": 0,
                "hint": "1,854 splits into 1,800 and 54, both clean multiples of 6.",
                "explanation": "1,854 = 1,800 + 54. 1,800 ÷ 6 = 300, and 54 ÷ 6 = 9. Combining gives 300 + 9 = 309.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1,854 ÷ 6 = (1,800 ÷ 6) + (54 ÷ 6)<br>
                        = 300 + 9 = 309
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: (1,800 ÷ 6) + (54 ÷ 6) = 300 + 9 = 309</p>
                </div>
                """
            },
            {
                "id": "q7",
                "question": "Use subtractive convenient splitting to calculate 3,984 ÷ 4 mentally:",
                "options": [
                    "(4,000 ÷ 4) - (16 ÷ 4) = 1,000 - 4 = 996",
                    "(4,000 ÷ 4) - (14 ÷ 4) = 1,000 - 3.5 = 996.5",
                    "(3,600 ÷ 4) + (384 ÷ 4) = 900 + 96 = 996",
                    "(4,000 ÷ 4) - (16 ÷ 4) = 100 - 4 = 96"
                ],
                "answer": 0,
                "hint": "3,984 is 16 less than 4,000. Write as (4,000 - 16) ÷ 4.",
                "explanation": "3,984 = 4,000 - 16. (4,000 ÷ 4) - (16 ÷ 4) = 1,000 - 4 = 996.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        3,984 = 4,000 - 16<br>
                        3,984 ÷ 4 = (4,000 ÷ 4) - (16 ÷ 4)<br>
                        = 1,000 - 4 = 996
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: (4,000 ÷ 4) - (16 ÷ 4) = 1,000 - 4 = 996</p>
                </div>
                """
            },
            {
                "id": "q8",
                "question": "A courier delivery driver travels 240 km in 6 hours at a constant speed. What is the driver's speed per hour?",
                "options": [
                    "40 km/h",
                    "30 km/h",
                    "50 km/h",
                    "45 km/h"
                ],
                "answer": 0,
                "hint": "Speed = Distance ÷ Time = 240 ÷ 6.",
                "explanation": "240 ÷ 6 = 40 km/h.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Speed = Distance ÷ Time<br>
                        = 240 km ÷ 6 h = 40 km/h
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 40 km/h</p>
                </div>
                """
            },
            {
                "id": "q9",
                "question": "Which of the following is equivalent to 8,100 ÷ 90?",
                "options": [
                    "9",
                    "90",
                    "900",
                    "810"
                ],
                "answer": 1,
                "hint": "Cancel one zero: 810 ÷ 9 = 90.",
                "explanation": "8,100 ÷ 90 = 810 ÷ 9 = 90.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        8,100 ÷ 90 = 810 ÷ 9 = 90
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 90</p>
                </div>
                """
            },
            {
                "id": "q10",
                "question": "A dairy cooperative packs 1,200 litres of milk into 20-litre cans. How many cans are filled?",
                "options": [
                    "60 cans",
                    "6 cans",
                    "600 cans",
                    "50 cans"
                ],
                "answer": 0,
                "hint": "Cancel 1 zero: 120 ÷ 2 = 60.",
                "explanation": "1,200 ÷ 20 = 120 ÷ 2 = 60 cans.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1,200 ÷ 20 = 120 ÷ 2 = 60 cans
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 60 cans</p>
                </div>
                """
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Halving, Partial Quotients & The Remainder Algorithm",
        "lecture": "Welcome to Mastery Challenge 2. In this module, you will practice repeated halving, multi-step partial quotient algorithms, and the Fundamental Division Algorithm with remainders.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Test your mastery of powers-of-two halving, partial quotient leaps, and remainder constraints. Answer all 10 questions to unlock detailed solutions!</p>",
        "questions": [
            {
                "id": "q11",
                "question": "Use repeated halving to divide 672 by 4:",
                "options": [
                    "168",
                    "164",
                    "172",
                    "336"
                ],
                "answer": 0,
                "hint": "Half of 672 is 336. Half of 336 is 168.",
                "explanation": "672 ÷ 2 = 336. 336 ÷ 2 = 168. So 672 ÷ 4 = 168.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        First Half: 672 ÷ 2 = 336<br>
                        Second Half: 336 ÷ 2 = 168<br>
                        Result: 672 ÷ 4 = 168
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 168</p>
                </div>
                """
            },
            {
                "id": "q12",
                "question": "What is 1,536 ÷ 8 using three successive halves?",
                "options": [
                    "192",
                    "182",
                    "384",
                    "768"
                ],
                "answer": 0,
                "hint": "1,536 ÷ 2 = 768. 768 ÷ 2 = 384. 384 ÷ 2 = 192.",
                "explanation": "First half: 768. Second half: 384. Third half: 192. So 1,536 ÷ 8 = 192.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Half 1: 1,536 ÷ 2 = 768<br>
                        Half 2: 768 ÷ 2 = 384<br>
                        Half 3: 384 ÷ 2 = 192<br>
                        Result: 1,536 ÷ 8 = 192
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 192</p>
                </div>
                """
            },
            {
                "id": "q13",
                "question": "In Sunitha's partial quotient method for 738 ÷ 6, she first subtracts 100 × 6 = 600. After this first leap, what is the remaining quantity to divide?",
                "options": [
                    "138",
                    "128",
                    "238",
                    "38"
                ],
                "answer": 0,
                "hint": "Subtract 600 from 738.",
                "explanation": "738 - 600 = 138. 138 remains to be divided by 6.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        738 - (100 × 6) = 738 - 600 = 138<br>
                        Next Leap: 20 × 6 = 120 (leaves 18)<br>
                        Final Leap: 3 × 6 = 18 (leaves 0)<br>
                        Total Q = 100 + 20 + 3 = 123
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 138</p>
                </div>
                """
            },
            {
                "id": "q14",
                "question": "What is the complete quotient of 738 ÷ 6?",
                "options": [
                    "123",
                    "124",
                    "113",
                    "133"
                ],
                "answer": 0,
                "hint": "100 + 20 + 3 = 123.",
                "explanation": "738 ÷ 6 = 123. Verification: 123 × 6 = 738.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        738 ÷ 6 = 123<br>
                        Check: 123 × 6 = 738
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 123</p>
                </div>
                """
            },
            {
                "id": "q15",
                "question": "If Divisor = 7, Quotient = 24, and Remainder = 5, what is the Dividend (N)?",
                "options": [
                    "173",
                    "168",
                    "175",
                    "163"
                ],
                "answer": 0,
                "hint": "N = (D × Q) + R = (7 × 24) + 5.",
                "explanation": "7 × 24 = 168. 168 + 5 = 173. So N = 173.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        N = (D × Q) + R<br>
                        = (7 × 24) + 5<br>
                        = 168 + 5 = 173
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 173</p>
                </div>
                """
            },
            {
                "id": "q16",
                "question": "Which of the following could BE a remainder when dividing an integer by 9?",
                "options": [
                    "8",
                    "9",
                    "10",
                    "12"
                ],
                "answer": 0,
                "hint": "The remainder must satisfy 0 ≤ R < 9.",
                "explanation": "Because 0 ≤ R < D, dividing by 9 can only give remainders 0 through 8. 8 is valid; 9, 10, and 12 are impossible.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        Condition: 0 ≤ R < Divisor<br>
                        For Divisor = 9, possible remainders are {0, 1, 2, 3, 4, 5, 6, 7, 8}.<br>
                        Therefore, 8 is the only valid option.
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 8</p>
                </div>
                """
            },
            {
                "id": "q17",
                "question": "A school has 312 students going on a zoo trip. Each bus seats 45 students. How many buses must be booked so no student is left behind?",
                "options": [
                    "6 buses",
                    "7 buses",
                    "8 buses",
                    "5 buses"
                ],
                "answer": 1,
                "hint": "312 ÷ 45 = 6 with a remainder of 42 students.",
                "explanation": "312 ÷ 45 = 6 R 42. 6 buses only hold 270 students, leaving 42 students behind. A 7th bus must be booked for the remainder.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        312 ÷ 45 = 6 with remainder 42<br>
                        6 buses × 45 = 270 seats (42 students left out!)<br>
                        Must round UP: 6 + 1 = 7 buses
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 7 buses</p>
                </div>
                """
            },
            {
                "id": "q18",
                "question": "A baker bakes 250 muffins and packs them into boxes holding 6 muffins each. How many boxes are completely filled, and how many muffins are left over?",
                "options": [
                    "41 boxes filled, 4 muffins left over",
                    "40 boxes filled, 10 muffins left over",
                    "42 boxes filled, 2 muffins left over",
                    "39 boxes filled, 16 muffins left over"
                ],
                "answer": 0,
                "hint": "250 ÷ 6 = 41 with a remainder of 4.",
                "explanation": "250 ÷ 6 = 41 with remainder 4. (41 × 6 = 246; 250 - 246 = 4).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        250 ÷ 6 = 41 R 4<br>
                        Verification: (41 × 6) + 4 = 246 + 4 = 250
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 41 boxes filled, 4 muffins left over</p>
                </div>
                """
            },
            {
                "id": "q19",
                "question": "A farmer has 195 eggs. Egg cartons hold 12 eggs each. How many cartons can be completely filled?",
                "options": [
                    "16 cartons",
                    "15 cartons",
                    "17 cartons",
                    "14 cartons"
                ],
                "answer": 0,
                "hint": "195 ÷ 12 = 16 R 3.",
                "explanation": "195 ÷ 12 = 16 with a remainder of 3 eggs. Exactly 16 cartons are completely filled.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        195 ÷ 12 = 16 R 3<br>
                        16 × 12 = 192 eggs in full cartons.<br>
                        3 eggs remain in an incomplete carton.
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 16 cartons</p>
                </div>
                """
            },
            {
                "id": "q20",
                "question": "If a number is divided by 11, the quotient is 18 and the remainder is 7. What is the number?",
                "options": [
                    "205",
                    "198",
                    "208",
                    "195"
                ],
                "answer": 0,
                "hint": "N = (11 × 18) + 7.",
                "explanation": "11 × 18 = 198. 198 + 7 = 205.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        N = (D × Q) + R<br>
                        = (11 × 18) + 7<br>
                        = 198 + 7 = 205
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 205</p>
                </div>
                """
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • Bulk Calculations, Multi-Digit Divisors & Zero Traps",
        "lecture": "Welcome to Mastery Challenge 3. In this assessment, you will master multi-digit vertical division, identify and eliminate internal zero quotient traps, and calculate bulk farm oil extraction yields.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Test your mastery of multi-digit divisors, quotient placeholders, and agricultural processing mathematics. Answer all 10 questions to unlock detailed solutions!</p>",
        "questions": [
            {
                "id": "q21",
                "question": "An oil mill extracts 1 litre of coconut oil from every 8 coconuts. How many litres of oil are produced from 5,128 coconuts?",
                "options": [
                    "641 Litres",
                    "640 Litres",
                    "651 Litres",
                    "631 Litres"
                ],
                "answer": 0,
                "hint": "51 ÷ 8 = 6 R 3; 32 ÷ 8 = 4 R 0; 8 ÷ 8 = 1.",
                "explanation": "5,128 ÷ 8 = 641 litres of oil.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        5,128 ÷ 8<br>
                        • 51 ÷ 8 = 6 (R 3)<br>
                        • 32 ÷ 8 = 4 (R 0)<br>
                        • 8 ÷ 8 = 1 (R 0)<br>
                        = 641 Litres
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 641 Litres</p>
                </div>
                """
            },
            {
                "id": "q22",
                "question": "If 641 litres of coconut oil is sold at ₹250 per litre, what is the total revenue?",
                "options": [
                    "₹1,60,250",
                    "₹1,60,000",
                    "₹1,58,250",
                    "₹1,62,500"
                ],
                "answer": 0,
                "hint": "641 × 250 = (641 × 1,000) ÷ 4 = 641,000 ÷ 4.",
                "explanation": "641 × ₹250 = ₹1,60,250.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Revenue = 641 × ₹250<br>
                        = 641 × (1,000 ÷ 4)<br>
                        = 641,000 ÷ 4 = ₹1,60,250
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: ₹1,60,250</p>
                </div>
                """
            },
            {
                "id": "q23",
                "question": "What is the quotient of 9,805 ÷ 32?",
                "options": [
                    "306 with remainder 13",
                    "36 with remainder 13",
                    "360 with remainder 13",
                    "305 with remainder 15"
                ],
                "answer": 0,
                "hint": "98 ÷ 32 = 3 R 2; bring down 0 ➔ 20 ÷ 32 = 0; bring down 5 ➔ 205 ÷ 32 = 6 R 13.",
                "explanation": "98 ÷ 32 = 3 R 2. Bring down 0: 20 ÷ 32 = 0 R 20. Bring down 5: 205 ÷ 32 = 6 R 13. Quotient = 306, Remainder = 13.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        9,805 ÷ 32<br>
                        • 98 ÷ 32 = 3 (3 × 32 = 96; Rem = 2)<br>
                        • Bring down 0 ➔ 20 ÷ 32 = 0 (MUST WRITE 0!)<br>
                        • Bring down 5 ➔ 205 ÷ 32 = 6 (6 × 32 = 192; Rem = 13)<br>
                        Result = 306 R 13
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 306 with remainder 13</p>
                </div>
                """
            },
            {
                "id": "q24",
                "question": "Calculate 6,018 ÷ 6. Beware of the zero quotient trap!",
                "options": [
                    "1,003",
                    "103",
                    "1,030",
                    "13"
                ],
                "answer": 0,
                "hint": "6 ÷ 6 = 1; 0 ÷ 6 = 0; 1 ÷ 6 = 0; 18 ÷ 6 = 3.",
                "explanation": "6 ÷ 6 = 1. Bring down 0: 0 ÷ 6 = 0. Bring down 1: 1 ÷ 6 = 0. Bring down 8: 18 ÷ 6 = 3. Quotient = 1,003.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        6,018 ÷ 6<br>
                        6 ÷ 6 = 1 (Thousands)<br>
                        0 ÷ 6 = 0 (Hundreds)<br>
                        1 ÷ 6 = 0 (Tens)<br>
                        18 ÷ 6 = 3 (Ones)<br>
                        Quotient = 1,003
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 1,003</p>
                </div>
                """
            },
            {
                "id": "q25",
                "question": "A worker presses 8,625 kg of coir fiber into bales of 25 kg each. How many bales are pressed?",
                "options": [
                    "345 bales",
                    "335 bales",
                    "355 bales",
                    "325 bales"
                ],
                "answer": 0,
                "hint": "86 ÷ 25 = 3 R 11; 112 ÷ 25 = 4 R 12; 125 ÷ 25 = 5.",
                "explanation": "8,625 ÷ 25 = 345 bales.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        8,625 ÷ 25<br>
                        • 86 ÷ 25 = 3 (3 × 25 = 75; Rem = 11)<br>
                        • 112 ÷ 25 = 4 (4 × 25 = 100; Rem = 12)<br>
                        • 125 ÷ 25 = 5 (5 × 25 = 125; Rem = 0)<br>
                        Total = 345 Bales
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 345 bales</p>
                </div>
                """
            },
            {
                "id": "q26",
                "question": "Evaluate 2,874 ÷ 14:",
                "options": [
                    "205 with remainder 4",
                    "25 with remainder 4",
                    "204 with remainder 18",
                    "215 with remainder 4"
                ],
                "answer": 0,
                "hint": "28 ÷ 14 = 2; bring down 7 ➔ 7 ÷ 14 = 0; bring down 4 ➔ 74 ÷ 14 = 5 R 4.",
                "explanation": "28 ÷ 14 = 2. Bring down 7: 7 ÷ 14 = 0. Bring down 4: 74 ÷ 14 = 5 R 4. Result = 205 R 4.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        2,874 ÷ 14<br>
                        • 28 ÷ 14 = 2 (Rem = 0)<br>
                        • Bring down 7 ➔ 7 ÷ 14 = 0 (Rem = 7)<br>
                        • Bring down 4 ➔ 74 ÷ 14 = 5 (5 × 14 = 70; Rem = 4)<br>
                        Result = 205 R 4
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 205 with remainder 4</p>
                </div>
                """
            },
            {
                "id": "q27",
                "question": "A theater hall has 576 seats arranged in 18 equal rows. How many seats are in each row?",
                "options": [
                    "32 seats",
                    "34 seats",
                    "28 seats",
                    "36 seats"
                ],
                "answer": 0,
                "hint": "57 ÷ 18 = 3 R 3; 36 ÷ 18 = 2.",
                "explanation": "576 ÷ 18 = 32 seats per row.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        576 ÷ 18<br>
                        57 ÷ 18 = 3 (3 × 18 = 54; Rem = 3)<br>
                        36 ÷ 18 = 2 (2 × 18 = 36; Rem = 0)<br>
                        = 32 seats
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 32 seats</p>
                </div>
                """
            },
            {
                "id": "q28",
                "question": "What is 7,248 ÷ 12?",
                "options": [
                    "604",
                    "64",
                    "640",
                    "608"
                ],
                "answer": 0,
                "hint": "72 ÷ 12 = 6; 4 ÷ 12 = 0; 48 ÷ 12 = 4.",
                "explanation": "72 ÷ 12 = 6. Bring down 4: 4 ÷ 12 = 0. Bring down 8: 48 ÷ 12 = 4. Quotient = 604.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        7,248 ÷ 12 = 604<br>
                        Check: 604 × 12 = 7,248
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 604</p>
                </div>
                """
            },
            {
                "id": "q29",
                "question": "A warehouse receives 3,750 bags of sugar and distributes them equally among 15 supermarkets. How many bags does each supermarket receive?",
                "options": [
                    "250 bags",
                    "25 bags",
                    "205 bags",
                    "260 bags"
                ],
                "answer": 0,
                "hint": "37 ÷ 15 = 2 R 7; 75 ÷ 15 = 5; 0 ÷ 15 = 0.",
                "explanation": "3,750 ÷ 15 = 250 bags.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        3,750 ÷ 15 = 250 bags
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 250 bags</p>
                </div>
                """
            },
            {
                "id": "q30",
                "question": "If 8,000 ÷ 16 = 500, what is 8,000 ÷ 32?",
                "options": [
                    "250",
                    "1,000",
                    "125",
                    "500"
                ],
                "answer": 0,
                "hint": "Doubling the divisor cuts the quotient in half!",
                "explanation": "Since 32 is twice 16, dividing by 32 yields half of 500, which is 250.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Divisor doubles: 16 × 2 = 32<br>
                        Quotient halves: 500 ÷ 2 = 250<br>
                        Result: 8,000 ÷ 32 = 250
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 250</p>
                </div>
                """
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Invoices, Bottlenecks, Tour Planning & Mathematical Truth",
        "lecture": "Welcome to the final Mastery Challenge of Chapter 9. This concluding assessment challenges you with sabzi mandi invoices, workshop bottleneck optimization, cycle rally route planning, and truth value classification.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Congratulations on reaching the final mastery challenge! Solve these 10 multi-step optimization and truth-value problems to complete the Coconut Farm chapter.</p>",
        "questions": [
            {
                "id": "q31",
                "question": "A sabzi mandi invoice records that 65 kg of onions were sold for ₹1,625. What was the unit price per kilogram?",
                "options": [
                    "₹25 / kg",
                    "₹24 / kg",
                    "₹26 / kg",
                    "₹28 / kg"
                ],
                "answer": 0,
                "hint": "Rate = Total ÷ Weight = 1,625 ÷ 65.",
                "explanation": "1,625 ÷ 65 = 25 rupees per kg.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Rate = Total Cost ÷ Weight<br>
                        = ₹1,625 ÷ 65 kg = ₹25 / kg
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: ₹25 / kg</p>
                </div>
                """
            },
            {
                "id": "q32",
                "question": "Tomatoes sell at ₹32 per kg. A restaurant chef purchases ₹1,440 worth of tomatoes. How many kilograms were purchased?",
                "options": [
                    "45 kg",
                    "42 kg",
                    "40 kg",
                    "48 kg"
                ],
                "answer": 0,
                "hint": "Weight = Total ÷ Rate = 1,440 ÷ 32.",
                "explanation": "1,440 ÷ 32 = 45 kg.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Weight = Total Cost ÷ Rate<br>
                        = ₹1,440 ÷ ₹32 = 45 kg
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 45 kg</p>
                </div>
                """
            },
            {
                "id": "q33",
                "question": "A bicycle assembly workshop has 75 frames, 160 wheels, and 90 handlebars. Each bicycle requires 1 frame, 2 wheels, and 1 handlebar. What is the maximum number of bicycles that can be assembled?",
                "options": [
                    "75 bicycles",
                    "80 bicycles",
                    "90 bicycles",
                    "70 bicycles"
                ],
                "answer": 0,
                "hint": "Frames allow: 75. Wheels allow: 160 ÷ 2 = 80. Handlebars allow: 90. Find the minimum limit.",
                "explanation": "Frames allow 75 bikes. Wheels allow 80 bikes. Handlebars allow 90 bikes. The bottleneck is the frames (75), which caps production at 75 bicycles.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        • Frames: 75 ÷ 1 = 75 bikes (Bottleneck!)<br>
                        • Wheels: 160 ÷ 2 = 80 bikes<br>
                        • Handlebars: 90 ÷ 1 = 90 bikes<br>
                        Max Complete Bikes = 75
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 75 bicycles</p>
                </div>
                """
            },
            {
                "id": "q34",
                "question": "A coastal cycling expedition covers 702 km from Mumbai to Goa across 9 equal daily stages. What distance must the cyclists ride each day?",
                "options": [
                    "78 km",
                    "76 km",
                    "74 km",
                    "82 km"
                ],
                "answer": 0,
                "hint": "70 ÷ 9 = 7 R 7; 72 ÷ 9 = 8.",
                "explanation": "702 ÷ 9 = 78 km per day.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Daily Stage = 702 km ÷ 9 days = 78 km/day
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 78 km</p>
                </div>
                """
            },
            {
                "id": "q35",
                "question": "Which of the following equations represents a TRUE mathematical statement?",
                "options": [
                    "7 × 8 = 50 + 6",
                    "9 × 7 = 60 + 5",
                    "8 × 6 = 40 + 7",
                    "6 × 6 = 30 + 5"
                ],
                "answer": 0,
                "hint": "7 × 8 = 56, and 50 + 6 = 56.",
                "explanation": "7 × 8 = 56, and 50 + 6 = 56. 56 = 56, which is True.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        LHS = 7 × 8 = 56<br>
                        RHS = 50 + 6 = 56<br>
                        LHS = RHS ➔ TRUE!
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 7 × 8 = 50 + 6</p>
                </div>
                """
            },
            {
                "id": "q36",
                "question": "Classify the statement: 'When an odd number is divided by 2, the remainder is 1.'",
                "options": [
                    "Always True",
                    "Sometimes True",
                    "Never True",
                    "Cannot be determined"
                ],
                "answer": 0,
                "hint": "Test odd numbers: 3 ÷ 2 = 1 R 1; 5 ÷ 2 = 2 R 1; 7 ÷ 2 = 3 R 1.",
                "explanation": "By definition, an odd number is of the form 2k + 1. Dividing any odd number by 2 always leaves a remainder of exactly 1. It is Always True.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        All odd numbers leave remainder 1 when divided by 2.<br>
                        Examples: 3 = (2 × 1) + 1, 15 = (2 × 7) + 1, 99 = (2 × 49) + 1.<br>
                        This is the universal definition of odd integers.
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Always True</p>
                </div>
                """
            },
            {
                "id": "q37",
                "question": "Classify the statement: 'Dividing a number by 4 gives an even quotient.'",
                "options": [
                    "Sometimes True",
                    "Always True",
                    "Never True",
                    "Cannot be determined"
                ],
                "answer": 0,
                "hint": "Try 16 ÷ 4 = 4 (Even), but 12 ÷ 4 = 3 (Odd!).",
                "explanation": "16 ÷ 4 = 4 (even quotient), but 12 ÷ 4 = 3 (odd quotient). Because it is true for some numbers and false for others, it is Sometimes True.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        • Case 1: 16 ÷ 4 = 4 (Even ➔ True)<br>
                        • Case 2: 12 ÷ 4 = 3 (Odd ➔ False)<br>
                        Since it depends on the dividend, the statement is <strong>Sometimes True</strong>.
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Sometimes True</p>
                </div>
                """
            },
            {
                "id": "q38",
                "question": "Classify the statement: 'A number divided by 10 has a remainder of 15.'",
                "options": [
                    "Never True",
                    "Always True",
                    "Sometimes True",
                    "Cannot be determined"
                ],
                "answer": 0,
                "hint": "The remainder must be strictly smaller than the divisor (R < 10).",
                "explanation": "In division by 10, the remainder can only be 0 through 9. A remainder of 15 is mathematically impossible under the division algorithm. It is Never True.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        Condition: 0 ≤ R < Divisor<br>
                        When Divisor = 10, remainder must be < 10.<br>
                        A remainder of 15 violates the fundamental division algorithm.
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Never True</p>
                </div>
                """
            },
            {
                "id": "q39",
                "question": "A school buys 450 ice cream cups for sports day. If they are packed in cartons of 24 cups each, how many full cartons are bought, and how many extra loose cups remain?",
                "options": [
                    "18 cartons with 18 cups remaining",
                    "18 cartons with 12 cups remaining",
                    "19 cartons with 6 cups remaining",
                    "17 cartons with 24 cups remaining"
                ],
                "answer": 0,
                "hint": "450 ÷ 24 = 18 with a remainder of 18.",
                "explanation": "450 ÷ 24 = 18 with remainder 18. (18 × 24 = 432; 450 - 432 = 18).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        450 ÷ 24<br>
                        45 ÷ 24 = 1 R 21<br>
                        210 ÷ 24 = 8 R 18<br>
                        = 18 cartons and 18 extra cups
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 18 cartons with 18 cups remaining</p>
                </div>
                """
            },
            {
                "id": "q40",
                "question": "In a factory warehouse, 5,000 biscuit packets are loaded equally into 25 shipping crates. How many packets are in each crate?",
                "options": [
                    "200 packets",
                    "20 packets",
                    "250 packets",
                    "500 packets"
                ],
                "answer": 0,
                "hint": "50 ÷ 25 = 2. Append two zeros.",
                "explanation": "5,000 ÷ 25 = 200 packets.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        5,000 ÷ 25 = 200 packets<br>
                        Check: 200 × 25 = 5,000
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 200 packets</p>
                </div>
                """
            }
        ]
    }
]


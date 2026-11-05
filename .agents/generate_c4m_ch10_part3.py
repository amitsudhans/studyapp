# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 10: Elephants, Tigers, and Leopards
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names replaced with generic roles.
Clean Unicode throughout (₹, ×, ÷, +, -, =).
"""

def make_sol_html(steps, note=None):
    items = "".join(f"<li class='mb-2 text-slate-700 leading-relaxed'>{s}</li>" for s in steps)
    html = f"<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside space-y-1.5 text-sm'>{items}</ol></div>"
    if note:
        html += f"<div class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> {note}</div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "section": "Nim Strategies & Addition Chart Puzzles",
        "speech": "",
        "quizzes": [
            {
                "q": "In the 2-player Nim Game to 10 starting at 0 (adding 1 or 2), if the first player says 1, what numbers can the second player choose?",
                "options": ["2 or 3", "3 or 4", "4 or 5", "0 or 1"],
                "ans": 0,
                "hint": "The second player adds either 1 or 2 to the running total 1.",
                "exp": "1 + 1 = 2, and 1 + 2 = 3.",
                "sol": make_sol_html([
                    "The running total is currently 1.",
                    "The rules allow adding either 1 or 2.",
                    "If the second player adds 1: 1 + 1 = 2.",
                    "If the second player adds 2: 1 + 2 = 3."
                ], "Each turn advances the running total by 1 or 2.")
            },
            {
                "q": "To guarantee reaching the winning number 10, which key target number should you secure on your turn before?",
                "options": ["9", "7", "8", "6"],
                "ans": 1,
                "hint": "From 7, the opponent can only say 8 or 9.",
                "exp": "From 7, opponent can only reach 8 or 9; you immediately reach 10 on the next move.",
                "sol": make_sol_html([
                    "Target is 10. To prevent opponent from reaching 10, determine the threshold before 10.",
                    "If you claim 7, the opponent can only add 1 (reaching 8) or 2 (reaching 9).",
                    "From 8, you add 2 to reach 10! From 9, you add 1 to reach 10!",
                    "Therefore, securing 7 guarantees a win."
                ], "Backward induction reveals winning milestones: 10, 7, 4, 1.")
            },
            {
                "q": "What is the complete sequence of winning milestone numbers for Nim Game to 10?",
                "options": ["1, 4, 7, 10", "2, 4, 6, 8, 10", "3, 6, 9", "1, 3, 5, 7, 9"],
                "ans": 0,
                "hint": "Subtract 3 from 10 repeatedly.",
                "exp": "10 - 3 = 7; 7 - 3 = 4; 4 - 3 = 1.",
                "sol": make_sol_html([
                    "Working backwards from target 10: 10 - 3 = 7.",
                    "From 7: 7 - 3 = 4.",
                    "From 4: 4 - 3 = 1.",
                    "The first player who says 1 can secure 4, then 7, and finally 10!"
                ], "Controlling milestones differing by (max move + 1 = 3) guarantees victory.")
            },
            {
                "q": "If extending the Nim addition game to target 21 (adding 1 or 2), what is the first winning number?",
                "options": ["0", "1", "2", "3"],
                "ans": 0,
                "hint": "Find the remainder when 21 is divided by (1 + 2 = 3).",
                "exp": "21 ÷ 3 = 7 with remainder 0. The second player controls multiples of 3!",
                "sol": make_sol_html([
                    "Step size is 1 or 2, so the cycle period is 1 + 2 = 3.",
                    "Dividing target by cycle length: 21 ÷ 3 = 7 remainder 0.",
                    "Because 21 is a multiple of 3, the second player can always complete a sum of 3.",
                    "Winning targets for player 2 are: 3, 6, 9, 12, 15, 18, 21."
                ], "When the target is a multiple of 3, the second player has the winning strategy.")
            },
            {
                "q": "In a 13 × 13 addition chart (numbers 0 to 12 along rows and columns), what is the maximum sum?",
                "options": ["22", "24", "25", "26"],
                "ans": 1,
                "hint": "Add the largest row header and largest column header.",
                "exp": "The maximum entry is 12 + 12 = 24.",
                "sol": make_sol_html([
                    "Row headers range from 0 to 12.",
                    "Column headers range from 0 to 12.",
                    "The largest cell is at row 12, column 12: 12 + 12 = 24."
                ], "The extreme bottom-right cell holds the maximum sum.")
            },
            {
                "q": "In the addition chart, along which lines do identical sums always appear?",
                "options": ["Horizontal rows", "Vertical columns", "Top-right to bottom-left diagonals", "Top-left to bottom-right diagonals"],
                "ans": 2,
                "hint": "If row increases by 1 and column decreases by 1, the sum remains constant.",
                "exp": "Anti-diagonals (slanted /) connect cells where (r + 1) + (c - 1) = r + c.",
                "sol": make_sol_html([
                    "Consider cells with sum 5: (0,5), (1,4), (2,3), (3,2), (4,1), (5,0).",
                    "Moving down 1 row increases the row by 1.",
                    "Moving left 1 column decreases the column by 1.",
                    "The net change in sum is +1 - 1 = 0, creating a top-right to bottom-left diagonal of identical values."
                ], "Anti-diagonals in addition tables represent constant-sum contours.")
            },
            {
                "q": "How many times does the number 9 appear in the 13 × 13 addition table (0 to 12)?",
                "options": ["8 times", "9 times", "10 times", "11 times"],
                "ans": 2,
                "hint": "Count pairs (a, b) such that a + b = 9 where 0 ≤ a, b ≤ 12.",
                "exp": "The pairs are (0,9), (1,8), (2,7), (3,6), (4,5), (5,4), (6,3), (7,2), (8,1), (9,0) = 10 times.",
                "sol": make_sol_html([
                    "Any sum 9 is formed by a + b = 9.",
                    "Possible values of a are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.",
                    "For each value of a, b = 9 - a is between 0 and 9 (which is ≤ 12).",
                    "Counting from a = 0 to a = 9 gives exactly 10 pairs."
                ], "For any sum S ≤ max header, S appears S + 1 times in a 0-indexed table.")
            },
            {
                "q": "A 3 × 3 window frame placed over an addition grid has center cell 10. What is the sum of its horizontal row (9 + 10 + 11)?",
                "options": ["20", "25", "30", "35"],
                "ans": 2,
                "hint": "The numbers are 9, 10, and 11.",
                "exp": "9 + 10 + 11 = 30.",
                "sol": make_sol_html([
                    "Row contains: 9, 10, 11.",
                    "Notice 9 = 10 - 1 and 11 = 10 + 1.",
                    "(10 - 1) + 10 + (10 + 1) = 3 × 10 = 30."
                ], "Symmetrical entries balance around the central centroid.")
            },
            {
                "q": "What is the total sum of all 9 numbers inside a 3 × 3 window frame with center number 10?",
                "options": ["80", "90", "100", "110"],
                "ans": 1,
                "hint": "Multiply the central number by the total number of cells (9).",
                "exp": "9 cells × 10 = 90.",
                "sol": make_sol_html([
                    "In an addition table, each of the 4 symmetric pairs around center C sums to 2 × C.",
                    "4 pairs × (2 × 10) = 80.",
                    "Adding the central cell: 80 + 10 = 90.",
                    "Alternatively, average of the 9 cells is 10: 9 × 10 = 90."
                ], "Total sum of a 3 × 3 window on an addition table is always 9 × Center.")
            },
            {
                "q": "In a 3 × 3 addition grid window with center 10, the top-left cell is 8 and bottom-right is 12. What is their sum?",
                "options": ["18", "20", "22", "24"],
                "ans": 1,
                "hint": "The two cells form a diagonal passing through center 10.",
                "exp": "8 + 12 = 20 = 2 × 10.",
                "sol": make_sol_html([
                    "Top-left cell = 8.",
                    "Bottom-right cell = 12.",
                    "8 + 12 = 20.",
                    "Notice that 20 = 2 × 10 (twice the central value)."
                ], "Every opposite pair passing through the center sums to 2 × Center.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Reverse Additions & Wildlife Population Math",
        "speech": "",
        "quizzes": [
            {
                "q": "Take the 2-digit number 27, reverse its digits to 72, and add them. What is the result?",
                "options": ["89", "99", "109", "119"],
                "ans": 1,
                "hint": "Add 27 + 72.",
                "exp": "27 + 72 = 99.",
                "sol": make_sol_html([
                    "Original number = 27.",
                    "Reversed digits = 72.",
                    "Units: 7 + 2 = 9.",
                    "Tens: 2 + 7 = 9.",
                    "27 + 72 = 99."
                ], "Reversing and adding a 2-digit number always yields a multiple of 11.")
            },
            {
                "q": "For any 2-digit number with tens digit a and ones digit b, why is the sum of the number and its reverse always a multiple of 11?",
                "options": ["Because (10a + b) + (10b + a) = 11(a + b)", "Because 10 + 1 = 11", "Because numbers are even", "Because 9 + 2 = 11"],
                "ans": 0,
                "hint": "Write the place values: original is 10a + b, reverse is 10b + a.",
                "exp": "(10a + b) + (10b + a) = 11a + 11b = 11(a + b).",
                "sol": make_sol_html([
                    "Original 2-digit number = 10 × a + b.",
                    "Reversed 2-digit number = 10 × b + a.",
                    "Adding both: (10a + a) + (b + 10b) = 11a + 11b.",
                    "Factoring out 11: 11 × (a + b).",
                    "Hence, the result is always an exact multiple of 11!"
                ], "Algebraic structure proves why reverse-and-add patterns hold universally.")
            },
            {
                "q": "Which of the following 2-digit numbers produces 55 when added to its reverse?",
                "options": ["14", "23", "32", "All of these"],
                "ans": 3,
                "hint": "Check if the sum of the digits (a + b) equals 5.",
                "exp": "14 + 41 = 55; 23 + 32 = 55; 32 + 23 = 55. All yield 55!",
                "sol": make_sol_html([
                    "We need 11 × (a + b) = 55, which means a + b = 5.",
                    "For 14: 1 + 4 = 5 (14 + 41 = 55).",
                    "For 23: 2 + 3 = 5 (23 + 32 = 55).",
                    "For 32: 3 + 2 = 5 (32 + 23 = 55).",
                    "All of these numbers satisfy the condition!"
                ], "Any 2-digit number whose digits sum to 5 produces 55 upon reversal and addition.")
            },
            {
                "q": "Which 2-digit number yields a 3-digit sum when added to its reverse?",
                "options": ["25", "34", "56", "43"],
                "ans": 2,
                "hint": "A 3-digit sum requires digit sum (a + b) ≥ 10.",
                "exp": "56 + 65 = 121 (since 5 + 6 = 11 ≥ 10).",
                "sol": make_sol_html([
                    "To reach 100 or greater, 11 × (a + b) must exceed 99.",
                    "This requires a + b ≥ 10.",
                    "Check options:",
                    "25: 2 + 5 = 7 (25 + 52 = 77).",
                    "34: 3 + 4 = 7 (34 + 43 = 77).",
                    "56: 5 + 6 = 11 (56 + 65 = 121).",
                    "121 is a 3-digit palindromic number!"
                ], "When digits sum to 10 or more, the reversed sum enters the hundreds place.")
            },
            {
                "q": "What is the sum when 48 is added to its reverse 84?",
                "options": ["122", "132", "142", "152"],
                "ans": 1,
                "hint": "48 + 84 = 11 × (4 + 8).",
                "exp": "11 × 12 = 132.",
                "sol": make_sol_html([
                    "Original: 48, Reversed: 84.",
                    "Digit sum = 4 + 8 = 12.",
                    "Reversed sum = 11 × 12 = 132.",
                    "Direct addition: 48 + 84 = 132."
                ], "Multiples of 11: 11 × 12 = 132.")
            },
            {
                "q": "Karnataka shelters 6,049 wild elephants and Kerala shelters 3,054 elephants. What is their combined elephant population?",
                "options": ["9,093", "9,103", "9,113", "9,203"],
                "ans": 1,
                "hint": "Add 6,049 + 3,054 using place value columns.",
                "exp": "6,049 + 3,054 = 9,103.",
                "sol": make_sol_html([
                    "Ones: 9 + 4 = 13 (write 3, carry 1).",
                    "Tens: 1 (carry) + 4 + 5 = 10 (write 0, carry 1).",
                    "Hundreds: 1 (carry) + 0 + 0 = 1.",
                    "Thousands: 6 + 3 = 9.",
                    "Total = 9,103 elephants."
                ], "Meticulous column carrying yields the exact combined population.")
            },
            {
                "q": "Madhya Pradesh records 785 tigers while Karnataka records 563 tigers. How many more tigers reside in Madhya Pradesh?",
                "options": ["212", "222", "232", "242"],
                "ans": 1,
                "hint": "Subtract 563 from 785.",
                "exp": "785 - 563 = 222.",
                "sol": make_sol_html([
                    "Ones: 5 - 3 = 2.",
                    "Tens: 8 - 6 = 2.",
                    "Hundreds: 7 - 5 = 2.",
                    "Difference = 222 tigers."
                ], "Standard subtraction without borrowing yields 222.")
            },
            {
                "q": "According to census reports, Maharashtra has 444 tigers, Uttarakhand has 560 tigers, and Madhya Pradesh has 785 tigers. What is the total tiger count in these three states?",
                "options": ["1,689", "1,779", "1,789", "1,799"],
                "ans": 2,
                "hint": "Add 444 + 560 + 785.",
                "exp": "444 + 560 + 785 = 1,789.",
                "sol": make_sol_html([
                    "Add the first two: 444 + 560 = 1,004.",
                    "Add the third: 1,004 + 785 = 1,789.",
                    "Check column addition: Ones 4+0+5=9; Tens 4+6+8=18 (write 8, carry 1); Hundreds 1+4+5+7=17.",
                    "Total = 1,789 tigers."
                ], "Multi-addend addition requires carrying across tens and hundreds.")
            },
            {
                "q": "State A reports 1,842 leopards and State B reports 2,365 leopards. What is their combined leopard population?",
                "options": ["4,107", "4,207", "4,217", "4,307"],
                "ans": 1,
                "hint": "Add 1,842 + 2,365.",
                "exp": "1,842 + 2,365 = 4,207.",
                "sol": make_sol_html([
                    "Ones: 2 + 5 = 7.",
                    "Tens: 4 + 6 = 10 (write 0, carry 1).",
                    "Hundreds: 1 (carry) + 8 + 3 = 12 (write 2, carry 1).",
                    "Thousands: 1 (carry) + 1 + 2 = 4.",
                    "Total = 4,207 leopards."
                ], "Double carrying across tens and hundreds yields 4,207.")
            },
            {
                "q": "When adding 6,049 + 3,054, why does the hundreds place contain a 1 although both addends have 0 in the hundreds place?",
                "options": ["It is a typo", "A carry-over of 1 ten came from the ones", "The sum of tens (1 carry + 4 + 5 = 10) generated a carried hundred", "Addends always round up"],
                "ans": 2,
                "hint": "Look at the tens place sum: 4 tens + 5 tens plus 1 carry from ones.",
                "exp": "9 + 4 = 13 ones carries 1 ten; 1 + 4 + 5 = 10 tens bundles into 1 hundred.",
                "sol": make_sol_html([
                    "In the ones column: 9 + 4 = 13 ones = 1 ten and 3 ones.",
                    "The 1 ten carries to the tens column.",
                    "In the tens column: 1 (carry) + 4 + 5 = 10 tens.",
                    "10 tens bundle together into exactly 1 hundred and 0 tens.",
                    "This 1 hundred is placed in the hundreds column!"
                ], "Place value bundling cascades carries smoothly into adjacent columns.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Regrouping Subtraction & Production Records",
        "speech": "",
        "quizzes": [
            {
                "q": "Assam shelters 5,719 wild elephants while Meghalaya shelters 1,754 elephants. How many more elephants inhabit Assam?",
                "options": ["3,865", "3,955", "3,965", "4,065"],
                "ans": 2,
                "hint": "Subtract 1,754 from 5,719.",
                "exp": "5,719 - 1,754 = 3,965.",
                "sol": make_sol_html([
                    "Ones: 9 - 4 = 5.",
                    "Tens: 1 - 5 requires unbundling 1 hundred from 7 hundreds (leaving 6 hundreds). 11 - 5 = 6 tens.",
                    "Hundreds: 6 - 7 requires unbundling 1 thousand from 5 thousands (leaving 4 thousands). 16 - 7 = 9 hundreds.",
                    "Thousands: 4 - 1 = 3 thousands.",
                    "Difference = 3,965 elephants."
                ], "Successive unbundling ensures accurate multi-digit subtraction.")
            },
            {
                "q": "In subtraction, what does unbundling 1 hundred provide to the tens column?",
                "options": ["1 ten", "10 tens", "100 tens", "5 tens"],
                "ans": 1,
                "hint": "How many tens are in one hundred?",
                "exp": "1 hundred = 10 tens.",
                "sol": make_sol_html([
                    "The base-ten number system is built on powers of 10.",
                    "1 hundred is composed of 10 tens.",
                    "Unbundling 1 hundred adds 10 to the tens digit."
                ], "1 Hundred = 10 Tens in our base-ten positional system.")
            },
            {
                "q": "In 2022, Kaziranga National Park welcomed 9,115 visitors, compared to 8,426 visitors in 2021. What was the increase in visitors?",
                "options": ["679", "689", "699", "711"],
                "ans": 1,
                "hint": "Subtract 8,426 from 9,115.",
                "exp": "9,115 - 8,426 = 689.",
                "sol": make_sol_html([
                    "Ones: 5 - 6 (unbundle 1 ten -> 0 tens left; 15 - 6 = 9).",
                    "Tens: 0 - 2 (unbundle 1 hundred -> 0 hundreds left; 10 - 2 = 8).",
                    "Hundreds: 0 - 4 (unbundle 1 thousand -> 8 thousands left; 10 - 4 = 6).",
                    "Thousands: 8 - 8 = 0.",
                    "Increase = 689 visitors."
                ], "Triple unbundling across ones, tens, and hundreds yields 689.")
            },
            {
                "q": "A vehicle assembly plant produced 4,320 electric scooters in March and 3,895 in April. How many scooters were produced altogether?",
                "options": ["8,115", "8,205", "8,215", "8,315"],
                "ans": 2,
                "hint": "Add 4,320 + 3,895.",
                "exp": "4,320 + 3,895 = 8,215.",
                "sol": make_sol_html([
                    "Ones: 0 + 5 = 5.",
                    "Tens: 2 + 9 = 11 (write 1, carry 1).",
                    "Hundreds: 1 (carry) + 3 + 8 = 12 (write 2, carry 1).",
                    "Thousands: 1 (carry) + 4 + 3 = 8.",
                    "Total = 8,215 scooters."
                ], "Carrying across tens and hundreds produces 8,215.")
            },
            {
                "q": "How many more electric scooters were produced in March than in April (4,320 - 3,895)?",
                "options": ["415", "425", "435", "525"],
                "ans": 1,
                "hint": "Subtract 3,895 from 4,320.",
                "exp": "4,320 - 3,895 = 425.",
                "sol": make_sol_html([
                    "Ones: 0 - 5 (unbundle 1 ten from 2 tens -> 1 ten left; 10 - 5 = 5).",
                    "Tens: 1 - 9 (unbundle 1 hundred from 3 hundreds -> 2 hundreds left; 11 - 9 = 2).",
                    "Hundreds: 2 - 8 (unbundle 1 thousand from 4 thousands -> 3 thousands left; 12 - 8 = 4).",
                    "Thousands: 3 - 3 = 0.",
                    "Difference = 425 scooters."
                ], "Difference calculation verifies month-over-month factory trends.")
            },
            {
                "q": "A juice distribution center shipped 3,450 mango crates, 2,870 apple crates, and 1,680 orange crates. What was the total crate count?",
                "options": ["7,900", "8,000", "8,100", "8,200"],
                "ans": 1,
                "hint": "Add 3,450 + 2,870 + 1,680.",
                "exp": "3,450 + 2,870 + 1,680 = 8,000 crates.",
                "sol": make_sol_html([
                    "Ones: 0 + 0 + 0 = 0.",
                    "Tens: 5 + 7 + 8 = 20 (write 0, carry 2).",
                    "Hundreds: 2 (carry) + 4 + 8 + 6 = 20 (write 0, carry 2).",
                    "Thousands: 2 (carry) + 3 + 2 + 1 = 8.",
                    "Total = 8,000 crates."
                ], "Carries of 2 across consecutive columns yield an even 8,000.")
            },
            {
                "q": "What is the difference when subtracting across zeros: 7,000 - 3,456?",
                "options": ["3,534", "3,544", "3,644", "4,544"],
                "ans": 1,
                "hint": "Unbundle 1 thousand into 9 hundreds, 9 tens, and 10 ones.",
                "exp": "7,000 - 3,456 = 3,544.",
                "sol": make_sol_html([
                    "7,000 = 6 thousands + 9 hundreds + 9 tens + 10 ones.",
                    "Ones: 10 - 6 = 4.",
                    "Tens: 9 - 5 = 4.",
                    "Hundreds: 9 - 4 = 5.",
                    "Thousands: 6 - 3 = 3.",
                    "Difference = 3,544."
                ], "Subtracting across multiple zeros converts intermediate zeros into 9s.")
            },
            {
                "q": "If 5,420 - 2,185 = 3,235, which addition equation verifies this subtraction?",
                "options": ["3,235 + 2,185 = 5,420", "5,420 + 2,185 = 7,605", "3,235 + 5,420 = 8,655", "5,420 - 3,235 = 2,185"],
                "ans": 0,
                "hint": "Difference + Subtrahend = Minuend.",
                "exp": "3,235 + 2,185 = 5,420.",
                "sol": make_sol_html([
                    "In subtraction: Minuend - Subtrahend = Difference.",
                    "Inverse operation states: Difference + Subtrahend = Minuend.",
                    "3,235 + 2,185 = 5,420.",
                    "Adding the difference to the subtracted amount restores the original total."
                ], "Addition serves as the universal verification tool for subtraction.")
            },
            {
                "q": "A wildlife sanctuary counted 6,240 migratory birds in December and 4,580 in February. How many birds departed during this period?",
                "options": ["1,650", "1,660", "1,740", "1,760"],
                "ans": 1,
                "hint": "Subtract 4,580 from 6,240.",
                "exp": "6,240 - 4,580 = 1,660.",
                "sol": make_sol_html([
                    "Ones: 0 - 0 = 0.",
                    "Tens: 4 - 8 (unbundle 1 hundred -> 1 hundred left; 14 - 8 = 6).",
                    "Hundreds: 1 - 5 (unbundle 1 thousand -> 5 thousands left; 11 - 5 = 6).",
                    "Thousands: 5 - 4 = 1.",
                    "Departed birds = 1,660."
                ], "Accurate subtraction quantifies seasonal bird migration.")
            },
            {
                "q": "Calculate 8,215 - 4,786 using column algorithm.",
                "options": ["3,419", "3,429", "3,439", "3,529"],
                "ans": 1,
                "hint": "Carefully trace each borrow across all four columns.",
                "exp": "8,215 - 4,786 = 3,429.",
                "sol": make_sol_html([
                    "Ones: 5 - 6 (unbundle 1 ten -> 0 tens left; 15 - 6 = 9).",
                    "Tens: 0 - 8 (unbundle 1 hundred -> 1 hundred left; 10 - 8 = 2).",
                    "Hundreds: 1 - 7 (unbundle 1 thousand -> 7 thousands left; 11 - 7 = 4).",
                    "Thousands: 7 - 4 = 3.",
                    "Result = 3,429."
                ], "Systematic unbundling gives 3,429.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Financial Slips, Mental Math & Logic Puzzles",
        "speech": "",
        "quizzes": [
            {
                "q": "A student deposits ₹3,650 into the school savings bank. Which breakdown of currency notes equals exactly ₹3,650?",
                "options": ["7 × ₹500 + 1 × ₹100 + 1 × ₹50", "6 × ₹500 + 6 × ₹100 + 1 × ₹50", "5 × ₹500 + 11 × ₹100 + 1 × ₹50", "All of these"],
                "ans": 3,
                "hint": "Calculate the monetary value of each combination.",
                "exp": "All three combinations equal ₹3,650.",
                "sol": make_sol_html([
                    "Option A: (7 × 500 = 3,500) + 100 + 50 = ₹3,650.",
                    "Option B: (6 × 500 = 3,000) + (6 × 100 = 600) + 50 = ₹3,650.",
                    "Option C: (5 × 500 = 2,500) + (11 × 100 = 1,100) + 50 = ₹3,650.",
                    "All combinations represent valid breakdowns of ₹3,650!"
                ], "A target currency sum can be composed using multiple denomination combinations.")
            },
            {
                "q": "What is the total value of 4 notes of ₹500, 8 notes of ₹100, and 7 notes of ₹10?",
                "options": ["₹2,860", "₹2,870", "₹2,880", "₹2,970"],
                "ans": 1,
                "hint": "4 × 500 = 2,000; 8 × 100 = 800; 7 × 10 = 70.",
                "exp": "2,000 + 800 + 70 = ₹2,870.",
                "sol": make_sol_html([
                    "500-rupee notes: 4 × ₹500 = ₹2,000.",
                    "100-rupee notes: 8 × ₹100 = ₹800.",
                    "10-rupee notes: 7 × ₹10 = ₹70.",
                    "Sum: 2,000 + 800 + 70 = ₹2,870."
                ], "Multiply each note count by its face value and sum the products.")
            },
            {
                "q": "Using mental compensation, how do you quickly calculate 683 - 99?",
                "options": ["Subtract 100 then subtract 1 (582)", "Subtract 100 then add 1 (584)", "Add 100 then subtract 1 (782)", "Subtract 90 then 9 (584)"],
                "ans": 1,
                "hint": "99 is 1 less than 100, so subtracting 100 removes 1 too many.",
                "exp": "683 - 100 + 1 = 584.",
                "sol": make_sol_html([
                    "Landmark number near 99 is 100.",
                    "683 - 100 = 583.",
                    "Because 99 was to be subtracted and we subtracted 100 (1 too many), add 1 back.",
                    "583 + 1 = 584."
                ], "Subtracting 99 is equivalent to subtracting 100 and adding 1.")
            },
            {
                "q": "Using mental compensation, how do you quickly calculate 458 + 99?",
                "options": ["Add 100 then add 1 (559)", "Add 100 then subtract 1 (557)", "Subtract 100 then add 1 (359)", "Multiply by 2"],
                "ans": 1,
                "hint": "Adding 100 adds 1 too many, so subtract 1.",
                "exp": "458 + 100 - 1 = 557.",
                "sol": make_sol_html([
                    "Landmark number near 99 is 100.",
                    "458 + 100 = 558.",
                    "Because we added 100 instead of 99, we added 1 extra unit.",
                    "Subtract 1: 558 - 1 = 557."
                ], "Adding 99 is equivalent to adding 100 and subtracting 1.")
            },
            {
                "q": "Using mental compensation, what is 2,740 - 999?",
                "options": ["1,739", "1,740", "1,741", "1,841"],
                "ans": 2,
                "hint": "Subtract 1,000 then add 1.",
                "exp": "2,740 - 1,000 + 1 = 1,741.",
                "sol": make_sol_html([
                    "999 is 1 less than 1,000.",
                    "2,740 - 1,000 = 1,740.",
                    "Add 1 back to compensate for the extra 1 subtracted.",
                    "1,740 + 1 = 1,741."
                ], "Friendly milestone numbers make 4-digit mental math instantaneous.")
            },
            {
                "q": "Without calculating, which symbol correctly compares: (3,800 + 450) ___ (3,800 + 475)?",
                "options": [">", "<", "=", "Cannot tell"],
                "ans": 1,
                "hint": "Both share 3,800. Compare 450 and 475.",
                "exp": "Since 450 < 475, the left side is less than (<) the right side.",
                "sol": make_sol_html([
                    "Both expressions contain the common term 3,800.",
                    "Compare the remaining addends: 450 vs 475.",
                    "Since 450 < 475, (3,800 + 450) < (3,800 + 475)."
                ], "Relational thinking compares terms directly without tedious addition.")
            },
            {
                "q": "Without calculating, which symbol correctly compares: (5,000 - 320) ___ (5,000 - 350)?",
                "options": [">", "<", "=", "Cannot tell"],
                "ans": 0,
                "hint": "Subtracting a smaller number leaves a larger remainder.",
                "exp": "Since 320 < 350, subtracting 320 leaves more behind (>).",
                "sol": make_sol_html([
                    "Both expressions start from the identical base 5,000.",
                    "Comparing subtrahends: 320 is smaller than 350.",
                    "Removing a smaller amount leaves a greater remainder.",
                    "Therefore, (5,000 - 320) > (5,000 - 350)."
                ], "In subtraction from equal amounts, smaller subtrahend yields larger difference.")
            },
            {
                "q": "Compare the two expressions: (2,500 + 1,200) ___ (2,400 + 1,300).",
                "options": [">", "<", "=", "Cannot tell"],
                "ans": 2,
                "hint": "Notice that 2,500 decreased by 100 to 2,400 while 1,200 increased by 100 to 1,300.",
                "exp": "Both expressions equal 3,700.",
                "sol": make_sol_html([
                    "First expression: 2,500 + 1,200 = 3,700.",
                    "Second expression: 2,400 + 1,300 = 3,700.",
                    "Notice the balance: transferring 100 from 2,500 to 1,200 yields 2,400 + 1,300 without changing the sum.",
                    "The expressions are equal (=)."
                ], "Compensation preserves equality when equal amounts are transferred between addends.")
            },
            {
                "q": "In the 3 × 3 Neighbouring Square puzzle, numbers 1 to 9 are placed so no two even numbers share a side. What structural pattern is required?",
                "options": ["All even numbers in the first row", "Even numbers placed in the 4 edge positions, odd numbers in 4 corners and center", "All odd numbers in the diagonal", "Random assignment"],
                "ans": 1,
                "hint": "There are 4 even numbers (2, 4, 6, 8) and 5 odd numbers (1, 3, 5, 7, 9).",
                "exp": "Odd numbers occupy the 4 corners and center; even numbers occupy the 4 edge cells.",
                "sol": make_sol_html([
                    "Numbers 1 to 9 contain 4 even numbers (2, 4, 6, 8) and 5 odd numbers (1, 3, 5, 7, 9).",
                    "A 3 × 3 grid behaves like a chessboard with 5 light squares (corners and center) and 4 dark squares (edge centers).",
                    "Dark squares do not touch each other horizontally or vertically.",
                    "Placing even numbers in the 4 edge positions ensures no two even numbers share an edge!"
                ], "Bipartite chessboard graph coloring solves adjacency parity constraints.")
            },
            {
                "q": "What is the sum of all nine digits from 1 to 9 placed inside the Neighbouring Square grid?",
                "options": ["40", "45", "50", "55"],
                "ans": 1,
                "hint": "Sum the digits: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9.",
                "exp": "The sum of integers from 1 to 9 is (9 × 10) ÷ 2 = 45.",
                "sol": make_sol_html([
                    "Sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9.",
                    "Pairing from ends: (1+9) + (2+8) + (3+7) + (4+6) + 5.",
                    "10 + 10 + 10 + 10 + 5 = 45.",
                    "Alternatively: n(n+1)/2 = 9 × 10 / 2 = 45."
                ], "The total sum of numbers 1 through 9 is always 45.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} challenge slides.")
    total_q = sum(len(s['quizzes']) for s in slides_part3)
    print(f"Total quiz questions: {total_q}")
    assert len(slides_part3) == 4, "Must have exactly 4 slides"
    assert total_q == 40, "Must have exactly 40 quiz questions"
    for s in slides_part3:
        assert len(s["title"].split()) <= 3, f"Title {s['title']} has too many words"
        assert len(s["quizzes"]) == 10, f"Slide {s['id']} must have 10 questions"
        for q in s["quizzes"]:
            assert 0 <= q["ans"] < len(q["options"]), f"Invalid answer index in {q['q']}"
    print("All Part 3 challenge assertions passed successfully!")

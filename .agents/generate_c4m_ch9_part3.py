# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 9: Equal Groups
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (Gulabo, Anvi, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, +, -, =).
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
        "section": "Animal Leaps, Common Multiples & Grid Hunts",
        "speech": "",
        "quizzes": [
            {
                "q": "If a frog jumps 3 steps at a time, where will it land on its 7th jump?",
                "options": ["18", "21", "24", "27"],
                "ans": 1,
                "hint": "Multiply the number of jumps by the step size.",
                "exp": "7 jumps × 3 steps = 21.",
                "sol": make_sol_html([
                    "Each jump covers 3 steps.",
                    "For 7 jumps, total distance = 7 × 3.",
                    "7 × 3 = 21."
                ], "Multiplication is fast repeated addition.")
            },
            {
                "q": "How many 4-step jumps does a squirrel take to reach milestone 48?",
                "options": ["10 jumps", "11 jumps", "12 jumps", "14 jumps"],
                "ans": 2,
                "hint": "Divide 48 by 4.",
                "exp": "48 ÷ 4 = 12 jumps.",
                "sol": make_sol_html([
                    "Target milestone = 48.",
                    "Step size per jump = 4.",
                    "Number of jumps = 48 ÷ 4 = 12."
                ], "Divide target by jump size to find number of jumps.")
            },
            {
                "q": "Does the 6-step rabbit land on milestone 54?",
                "options": ["Yes, on its 9th jump", "No, it skips it", "Only if it runs backward", "It stops at 50"],
                "ans": 0,
                "exp": "54 ÷ 6 = 9, so the rabbit lands on 54 on its 9th jump.",
                "sol": make_sol_html([
                    "Check divisibility: 54 ÷ 6 = 9.",
                    "Since 54 is an exact multiple of 6, the rabbit lands on 54.",
                    "The landing occurs on jump 9."
                ], "A target is reached if it is an exact multiple.")
            },
            {
                "q": "Which milestone is the smallest shared landing point (LCM) for the 3-step frog and 4-step squirrel?",
                "options": ["6", "8", "12", "16"],
                "ans": 2,
                "exp": "12 is the smallest positive number divisible by both 3 and 4.",
                "sol": make_sol_html([
                    "Frog landings: 3, 6, 9, 12, 15...",
                    "Squirrel landings: 4, 8, 12, 16...",
                    "The first number appearing in both lists is 12."
                ], "Least Common Multiple of 3 and 4 is 12.")
            },
            {
                "q": "What is the first shared landing stone for the 6-step rabbit and the 8-step kangaroo?",
                "options": ["12", "18", "24", "48"],
                "ans": 2,
                "exp": "6 × 4 = 24 and 8 × 3 = 24.",
                "sol": make_sol_html([
                    "Rabbit landings: 6, 12, 18, 24, 30...",
                    "Kangaroo landings: 8, 16, 24, 32...",
                    "First common number is 24."
                ], "24 is the least common multiple of 6 and 8.")
            },
            {
                "q": "A mouse starts at step 24 (moves 2 steps/jump) and a cat starts at step 12 (moves 3 steps/jump). Where is the cat when the mouse reaches step 36?",
                "options": ["Step 28", "Step 30", "Step 33", "Step 36"],
                "ans": 1,
                "hint": "Find how many jumps the mouse took to reach 36 from 24, then advance the cat by that many jumps.",
                "exp": "Mouse jumps = (36 - 24) ÷ 2 = 6 jumps. Cat position = 12 + (6 × 3) = 12 + 18 = step 30.",
                "sol": make_sol_html([
                    "Step 1: Distance moved by mouse = 36 - 24 = 12 steps.",
                    "Step 2: Jumps taken by mouse = 12 ÷ 2 = 6 jumps.",
                    "Step 3: Distance moved by cat in 6 leaps = 6 × 3 = 18 steps.",
                    "Step 4: Cat position = 12 + 18 = step 30."
                ], "Track simultaneous steps using jump count.")
            },
            {
                "q": "In a number hunt grid, which three consecutive numbers form a valid multiplication sentence?",
                "options": ["7, 8, 56", "5, 6, 32", "4, 9, 38", "3, 7, 24"],
                "ans": 0,
                "exp": "7 × 8 = 56 is an exact multiplication sentence.",
                "sol": make_sol_html([
                    "Evaluate each option:",
                    "7 × 8 = 56 (True)",
                    "5 × 6 = 30 ≠ 32",
                    "4 × 9 = 36 ≠ 38",
                    "3 × 7 = 21 ≠ 24"
                ], "7 × 8 = 56.")
            },
            {
                "q": "If 72 ÷ 8 = 9, what is the inverse multiplication sentence?",
                "options": ["9 × 8 = 72", "72 × 8 = 576", "9 + 8 = 17", "72 - 8 = 64"],
                "ans": 0,
                "exp": "Division and multiplication are inverses: 9 × 8 = 72.",
                "sol": make_sol_html([
                    "Dividend = 72, Divisor = 8, Quotient = 9.",
                    "Inverse relationship: Quotient × Divisor = Dividend.",
                    "Therefore, 9 × 8 = 72."
                ], "Multiplication and division are reciprocal operations.")
            },
            {
                "q": "Which of these numbers CANNOT be landed on by the 8-step kangaroo?",
                "options": ["32", "48", "60", "72"],
                "ans": 2,
                "exp": "60 is not divisible by 8 (60 ÷ 8 = 7 remainder 4).",
                "sol": make_sol_html([
                    "Check multiples of 8: 32 = 8 × 4, 48 = 8 × 6, 72 = 8 × 9.",
                    "60 ÷ 8 = 7 with remainder 4.",
                    "Therefore, 60 is not on the kangaroo's path."
                ], "Only exact multiples of 8 can be landed on.")
            },
            {
                "q": "If an animal leaps 5 steps per bound, how many jumps are needed to travel from 25 to 75?",
                "options": ["8 jumps", "10 jumps", "12 jumps", "15 jumps"],
                "ans": 1,
                "hint": "Find the difference between 75 and 25, then divide by 5.",
                "exp": "(75 - 25) ÷ 5 = 50 ÷ 5 = 10 jumps.",
                "sol": make_sol_html([
                    "Total distance = 75 - 25 = 50 steps.",
                    "Step size = 5 steps per jump.",
                    "Number of jumps = 50 ÷ 5 = 10 jumps."
                ], "Distance ÷ Step size = Number of jumps.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Floral Geometry, Arrays & Doubling Magic",
        "speech": "",
        "quizzes": [
            {
                "q": "A flowerbed has 12 lily blossoms, each with 6 petals. How many total petals are there?",
                "options": ["60 petals", "66 petals", "72 petals", "84 petals"],
                "ans": 2,
                "hint": "Multiply 12 by 6.",
                "exp": "12 × 6 = 72 petals.",
                "sol": make_sol_html([
                    "Number of flowers = 12.",
                    "Petals per flower = 6.",
                    "Total petals = 12 × 6 = 72."
                ], "12 × 6 = 72.")
            },
            {
                "q": "In the multiplication equation 9 × 7 = 63, what is the term '63' called?",
                "options": ["Multiplier", "Multiplicand", "Product", "Quotient"],
                "ans": 2,
                "exp": "The result of multiplying two numbers is called the product.",
                "sol": make_sol_html([
                    "Multiplier = 9 (number of groups).",
                    "Multiplicand = 7 (size of each group).",
                    "Product = 63 (the total resulting amount)."
                ], "Product is the result of multiplication.")
            },
            {
                "q": "A gardener has 45 hibiscus petals. If each flower has 5 petals, how many flowers were picked?",
                "options": ["7 flowers", "8 flowers", "9 flowers", "10 flowers"],
                "ans": 2,
                "hint": "Divide 45 by 5.",
                "exp": "45 ÷ 5 = 9 flowers.",
                "sol": make_sol_html([
                    "Total petals = 45.",
                    "Petals per flower = 5.",
                    "Number of flowers = 45 ÷ 5 = 9 flowers."
                ], "Division finds the number of equal groups.")
            },
            {
                "q": "A seedling tray has 4 rows of marigold saplings with 6 saplings in each row. What property shows this equals 6 rows of 4?",
                "options": ["Associative property", "Commutative property", "Distributive property", "Zero property"],
                "ans": 1,
                "exp": "The commutative property states that changing factor order does not change the product (4 × 6 = 6 × 4 = 24).",
                "sol": make_sol_html([
                    "4 rows of 6 = 24.",
                    "6 rows of 4 = 24.",
                    "Order does not alter the product in multiplication."
                ], "Commutative property: a × b = b × a.")
            },
            {
                "q": "A supermarket tray holds strawberries in 5 rows with 8 strawberries in each row. How many strawberries are in the tray?",
                "options": ["35", "40", "45", "48"],
                "ans": 1,
                "hint": "Multiply 5 by 8.",
                "exp": "5 rows × 8 strawberries = 40 strawberries.",
                "sol": make_sol_html([
                    "Rows = 5.",
                    "Items per row = 8.",
                    "Total items = 5 × 8 = 40."
                ], "5 × 8 = 40.")
            },
            {
                "q": "What is the result when 36 is doubled?",
                "options": ["68", "70", "72", "74"],
                "ans": 2,
                "hint": "Multiply 36 by 2.",
                "exp": "36 × 2 = 72.",
                "sol": make_sol_html([
                    "Doubling means multiplying by 2.",
                    "36 × 2 = (30 × 2) + (6 × 2) = 60 + 12 = 72."
                ], "Doubling 36 gives 72.")
            },
            {
                "q": "Which of the following can NEVER be the ones digit of a doubled whole number?",
                "options": ["0", "4", "7", "8"],
                "ans": 2,
                "hint": "Doubling any whole number always produces an even product.",
                "exp": "Doubled numbers are always even, so their ones digit must be 0, 2, 4, 6, or 8. It can never be an odd digit like 7.",
                "sol": make_sol_html([
                    "Any number multiplied by 2 is an even number.",
                    "Even numbers only end in 0, 2, 4, 6, or 8.",
                    "Therefore, 7 can never appear in the ones place of a doubled whole number."
                ], "Doubled products always have even ones digits.")
            },
            {
                "q": "If you double the number 15, and then double the result again, what is the final number?",
                "options": ["45", "50", "60", "75"],
                "ans": 2,
                "hint": "First double 15 (15 × 2 = 30), then double 30.",
                "exp": "15 × 2 = 30, and 30 × 2 = 60 (which is 15 × 4).",
                "sol": make_sol_html([
                    "First doubling: 15 × 2 = 30.",
                    "Second doubling: 30 × 2 = 60.",
                    "Notice that doubling twice is equivalent to multiplying by 4 (15 × 4 = 60)."
                ], "Doubling twice equals multiplying by 4.")
            },
            {
                "q": "A bakery bakes cupcakes in trays of 4 rows and 6 columns. If they bake 3 identical trays, how many cupcakes are baked?",
                "options": ["60 cupcakes", "72 cupcakes", "80 cupcakes", "96 cupcakes"],
                "ans": 1,
                "hint": "Find cupcakes per tray (4 × 6 = 24), then multiply by 3.",
                "exp": "Each tray = 4 × 6 = 24 cupcakes. Three trays = 24 × 3 = 72 cupcakes.",
                "sol": make_sol_html([
                    "Cupcakes per tray = 4 × 6 = 24.",
                    "Total cupcakes for 3 trays = 24 × 3.",
                    "24 × 3 = 72 cupcakes."
                ], "24 × 3 = 72.")
            },
            {
                "q": "What is half of 96?",
                "options": ["44", "46", "48", "52"],
                "ans": 2,
                "hint": "Divide 96 by 2.",
                "exp": "96 ÷ 2 = 48.",
                "sol": make_sol_html([
                    "Halving is the reverse of doubling.",
                    "96 ÷ 2 = (90 ÷ 2) + (6 ÷ 2) = 45 + 3 = 48."
                ], "Half of 96 is 48.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Grid Symmetry, Scaling Tens & Breakdown Multiplication",
        "speech": "",
        "quizzes": [
            {
                "q": "In a 10×10 multiplication table, what property causes Row 4, Col 9 to equal Row 9, Col 4 (36)?",
                "options": ["Diagonal symmetry via commutative property", "Distributive law", "Inverse operation", "Rounding convention"],
                "ans": 0,
                "exp": "Commutativity (4 × 9 = 9 × 4 = 36) creates reflectional symmetry across the main diagonal.",
                "sol": make_sol_html([
                    "The main diagonal contains square numbers (1, 4, 9, 16, 25...).",
                    "Off-diagonal cells mirror each other because a × b = b × a.",
                    "Row 4 Col 9 = 36 = Row 9 Col 4."
                ], "Multiplication tables are symmetrical across the diagonal.")
            },
            {
                "q": "What is the ones digit of 8 × 7?",
                "options": ["2", "4", "6", "8"],
                "ans": 2,
                "hint": "8 × 7 = 56. Look at the ones digit.",
                "exp": "8 × 7 = 56, so the ones digit is 6.",
                "sol": make_sol_html([
                    "8 × 7 = 56.",
                    "The tens digit is 5 and the ones digit is 6."
                ], "Ones digit of 56 is 6.")
            },
            {
                "q": "If 6 × 9 = 54, what is 60 × 9?",
                "options": ["54", "540", "5,400", "630"],
                "ans": 1,
                "hint": "Multiply 54 by 10 (affix a zero).",
                "exp": "60 × 9 = 54 tens = 540.",
                "sol": make_sol_html([
                    "60 is 6 tens.",
                    "6 tens × 9 = 54 tens.",
                    "54 tens = 540."
                ], "60 × 9 = 540.")
            },
            {
                "q": "How many wheels are there on 70 four-wheeled cars?",
                "options": ["240 wheels", "280 wheels", "320 wheels", "350 wheels"],
                "ans": 1,
                "hint": "Multiply 70 by 4.",
                "exp": "70 × 4 = (7 × 4) tens = 28 tens = 280 wheels.",
                "sol": make_sol_html([
                    "Number of cars = 70.",
                    "Wheels per car = 4.",
                    "Total wheels = 70 × 4 = 280."
                ], "70 × 4 = 280 wheels.")
            },
            {
                "q": "Using the tens breakdown method to calculate 18 × 5, how do you split 18?",
                "options": ["10 + 8", "12 + 6", "15 + 3", "9 + 9"],
                "ans": 0,
                "exp": "Split 18 into tens and ones: 10 + 8. Then (10 × 5) + (8 × 5) = 50 + 40 = 90.",
                "sol": make_sol_html([
                    "18 = 10 + 8.",
                    "Multiply each by 5: 10 × 5 = 50, and 8 × 5 = 40.",
                    "Add partial products: 50 + 40 = 90."
                ], "18 × 5 = 90.")
            },
            {
                "q": "An artisan needs 23 bamboo poles for each of 8 carts. How many poles are needed in total?",
                "options": ["164", "176", "184", "192"],
                "ans": 2,
                "hint": "Calculate (20 × 8) + (3 × 8).",
                "exp": "(20 × 8) + (3 × 8) = 160 + 24 = 184 poles.",
                "sol": make_sol_html([
                    "Decompose 23: 20 + 3.",
                    "20 × 8 = 160.",
                    "3 × 8 = 24.",
                    "Total = 160 + 24 = 184 poles."
                ], "23 × 8 = 184.")
            },
            {
                "q": "A school field trip has 25 two-legged ducks and 12 four-legged goats. How many animal legs are there in total?",
                "options": ["88 legs", "94 legs", "98 legs", "108 legs"],
                "ans": 2,
                "hint": "(25 × 2) + (12 × 4).",
                "exp": "(25 × 2) + (12 × 4) = 50 + 48 = 98 legs.",
                "sol": make_sol_html([
                    "Duck legs = 25 × 2 = 50 legs.",
                    "Goat legs = 12 × 4 = 48 legs.",
                    "Total legs = 50 + 48 = 98 legs."
                ], "50 + 48 = 98 legs.")
            },
            {
                "q": "An assembly hall has 14 rows with 15 chairs in each row. What is the total seating capacity?",
                "options": ["190", "200", "210", "225"],
                "ans": 2,
                "hint": "14 × 15 = (10 × 15) + (4 × 15).",
                "exp": "(10 × 15) + (4 × 15) = 150 + 60 = 210 chairs.",
                "sol": make_sol_html([
                    "Decompose 14: 10 + 4.",
                    "10 × 15 = 150.",
                    "4 × 15 = 60.",
                    "Total = 150 + 60 = 210 chairs."
                ], "14 × 15 = 210.")
            },
            {
                "q": "What is 40 × 60?",
                "options": ["240", "2,400", "24,000", "240,000"],
                "ans": 1,
                "hint": "Multiply 4 × 6 = 24, then append two zeros.",
                "exp": "4 × 6 = 24; affix two zeros gives 2,400.",
                "sol": make_sol_html([
                    "4 tens × 6 tens = 24 hundreds.",
                    "24 hundreds = 2,400."
                ], "40 × 60 = 2,400.")
            },
            {
                "q": "If 9 × 8 = 72, what is 9 × 800?",
                "options": ["720", "7,200", "72,000", "720,000"],
                "ans": 1,
                "hint": "Multiply 72 by 100.",
                "exp": "9 × 800 = 7,200.",
                "sol": make_sol_html([
                    "800 is 8 hundreds.",
                    "9 × 8 hundreds = 72 hundreds.",
                    "72 hundreds = 7,200."
                ], "9 × 800 = 7,200.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Partial Quotients, Scaling Hundreds & Reasoning",
        "speech": "",
        "quizzes": [
            {
                "q": "Using partial quotients to solve 54 ÷ 3, if you first take away 10 groups of 3 (30), how many are left to divide?",
                "options": ["14", "20", "24", "30"],
                "ans": 2,
                "hint": "Subtract 30 from 54.",
                "exp": "54 - 30 = 24.",
                "sol": make_sol_html([
                    "Total = 54.",
                    "10 groups of 3 = 30.",
                    "Remaining to divide = 54 - 30 = 24.",
                    "Next, 24 ÷ 3 = 8 groups. Total = 10 + 8 = 18."
                ], "54 ÷ 3 = 18.")
            },
            {
                "q": "How many 3-wheeled passenger tempos can be fitted using 57 wheels?",
                "options": ["17 tempos", "18 tempos", "19 tempos", "21 tempos"],
                "ans": 2,
                "hint": "Divide 57 by 3.",
                "exp": "57 ÷ 3 = (30 ÷ 3) + (27 ÷ 3) = 10 + 9 = 19 tempos.",
                "sol": make_sol_html([
                    "57 = 30 + 27.",
                    "30 ÷ 3 = 10.",
                    "27 ÷ 3 = 9.",
                    "Total tempos = 10 + 9 = 19."
                ], "57 ÷ 3 = 19 tempos.")
            },
            {
                "q": "A city fleet has 8 electric shuttle buses, each carrying 125 passengers. How many total passengers are transported?",
                "options": ["850", "960", "1,000", "1,050"],
                "ans": 2,
                "hint": "Multiply (100 × 8) + (20 × 8) + (5 × 8).",
                "exp": "800 + 160 + 40 = 1,000 passengers.",
                "sol": make_sol_html([
                    "Decompose 125 into 100 + 20 + 5.",
                    "100 × 8 = 800.",
                    "20 × 8 = 160.",
                    "5 × 8 = 40.",
                    "Sum = 800 + 160 + 40 = 1,000."
                ], "125 × 8 = 1,000 passengers.")
            },
            {
                "q": "A potter packs 174 clay tea cups (kulhads) into 6 crates. How many cups are packed in total?",
                "options": ["1,024", "1,034", "1,044", "1,054"],
                "ans": 2,
                "hint": "174 × 6 = (100 × 6) + (70 × 6) + (4 × 6).",
                "exp": "600 + 420 + 24 = 1,044 cups.",
                "sol": make_sol_html([
                    "Decompose 174 into 100 + 70 + 4.",
                    "100 × 6 = 600.",
                    "70 × 6 = 420.",
                    "4 × 6 = 24.",
                    "Total = 600 + 420 + 24 = 1,044 cups."
                ], "174 × 6 = 1,044 cups.")
            },
            {
                "q": "A mountain toy train travels 88 km each day. How many kilometres does it travel in 1 full week (7 days)?",
                "options": ["586 km", "606 km", "616 km", "626 km"],
                "ans": 2,
                "hint": "Multiply 88 by 7: (80 × 7) + (8 × 7).",
                "exp": "560 + 56 = 616 km.",
                "sol": make_sol_html([
                    "Daily distance = 88 km.",
                    "88 × 7 = (80 × 7) + (8 × 7).",
                    "560 + 56 = 616 km."
                ], "88 × 7 = 616 km.")
            },
            {
                "q": "96 adventurers go whitewater rafting in rafts holding 6 people each. How many rafts are launched?",
                "options": ["14 rafts", "15 rafts", "16 rafts", "18 rafts"],
                "ans": 2,
                "hint": "96 ÷ 6 = (60 ÷ 6) + (36 ÷ 6).",
                "exp": "10 + 6 = 16 rafts.",
                "sol": make_sol_html([
                    "96 = 60 + 36.",
                    "60 ÷ 6 = 10.",
                    "36 ÷ 6 = 6.",
                    "Total rafts = 10 + 6 = 16 rafts."
                ], "96 ÷ 6 = 16 rafts.")
            },
            {
                "q": "Is the statement 'A number divided by 1 is always equal to the number itself' Always, Sometimes, or Never True?",
                "options": ["Always True", "Sometimes True", "Never True", "Only for even numbers"],
                "ans": 0,
                "exp": "Any number divided by 1 equals itself (Identity property of division).",
                "sol": make_sol_html([
                    "Identity property: n ÷ 1 = n for any number.",
                    "Examples: 5 ÷ 1 = 5, 48 ÷ 1 = 48, 1000 ÷ 1 = 1000.",
                    "This is Always True without exception."
                ], "Always True.")
            },
            {
                "q": "Is the statement 'The product of two odd numbers is always even' Always, Sometimes, or Never True?",
                "options": ["Always True", "Sometimes True", "Never True", "True on Tuesdays"],
                "ans": 2,
                "exp": "Odd × Odd is ALWAYS Odd (e.g., 3 × 5 = 15, 7 × 9 = 63). It is Never True that it is even.",
                "sol": make_sol_html([
                    "Test odd pairs: 3 × 5 = 15 (odd), 7 × 7 = 49 (odd).",
                    "An odd number has no factor of 2.",
                    "Multiplying two odd numbers can never introduce a factor of 2.",
                    "Therefore, the statement is Never True."
                ], "Never True.")
            },
            {
                "q": "A warehouse has 72 truck tires. If each truck requires 6 tires, what type of division problem is this?",
                "options": ["Measurement division (group size is known, finding number of groups)", "Sharing division (number of groups is known)", "Repeated addition", "Doubling magic"],
                "ans": 0,
                "exp": "The group size (6 tires/truck) is known; we are measuring how many trucks can be served.",
                "sol": make_sol_html([
                    "In measurement division, the group size is given (6 tires per truck).",
                    "We divide 72 by 6 to measure the number of groups formed (12 trucks).",
                    "This is measurement division."
                ], "Measurement division finds the number of groups.")
            },
            {
                "q": "Sharing ₹750 equally among 5 children gives how many rupees to each child?",
                "options": ["₹125", "₹140", "₹150", "₹175"],
                "ans": 2,
                "hint": "Divide 750 by 5.",
                "exp": "750 ÷ 5 = 150 rupees per child.",
                "sol": make_sol_html([
                    "Total money = ₹750.",
                    "Children = 5.",
                    "Share per child = 750 ÷ 5 = ₹150."
                ], "₹750 ÷ 5 = ₹150.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    total_q = 0
    for s in slides_part3:
        n_q = len(s.get("quizzes", []))
        total_q += n_q
        print(f"Slide {s['id']}: {s['title']} -> {n_q} questions (Title: {len(s['title'].split())} words)")
        assert 1 <= len(s['title'].split()) <= 3, f"Title length out of bounds for slide {s['id']}!"
        assert n_q == 10, f"Expected 10 questions in slide {s['id']}, found {n_q}!"
    print(f"Total quizzes in Part 3: {total_q}")
    assert total_q == 40, f"Expected 40 questions total, found {total_q}!"

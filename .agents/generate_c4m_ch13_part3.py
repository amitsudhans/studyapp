# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 13: The Transport Museum
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (Chinnu, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, ₹, etc.).
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
        "section": "Mystery Matrix, Tables & Halving-Doubling",
        "speech": "",
        "quizzes": [
            {
                "q": "In a mystery matrix, a row contains products 24 and 32. What single-digit row multiplier divides both numbers evenly?",
                "options": ["6", "7", "8", "9"],
                "ans": 2,
                "hint": "Find the highest common single-digit factor of 24 and 32.",
                "exp": "8 × 3 = 24 and 8 × 4 = 32. 8 is the common single-digit factor.",
                "sol": make_sol_html([
                    "Factors of 24 include 1, 2, 3, 4, 6, 8, 12, 24.",
                    "Factors of 32 include 1, 2, 4, 8, 16, 32.",
                    "The common single-digit factors are 1, 2, 4, and 8.",
                    "Choosing 8 gives column multipliers 3 and 4, which are valid single digits."
                ], "Common row multipliers represent shared factors across row products.")
            },
            {
                "q": "How can 7 × 15 be computed by decomposing 15 into tens and ones?",
                "options": ["(7 × 10) + (7 × 5)", "(7 × 10) - (7 × 5)", "(7 × 20) - 15", "(7 × 5) + 10"],
                "ans": 0,
                "hint": "Split 15 into 10 + 5 and apply the distributive property.",
                "exp": "(7 × 10) + (7 × 5) = 70 + 35 = 105.",
                "sol": make_sol_html([
                    "Decompose 15 into 10 and 5.",
                    "Multiply 7 by 10: 7 × 10 = 70.",
                    "Multiply 7 by 5: 7 × 5 = 35.",
                    "Sum the two partial products: 70 + 35 = 105."
                ], "Breaking numbers into tens and ones simplifies multi-digit multiplication.")
            },
            {
                "q": "Using the halving and doubling strategy, how can you calculate 4 × 14?",
                "options": ["Halve 14 to 7, calculate 4 × 7 = 28, then double 28 to get 56", "Multiply 4 × 10 and subtract 4", "Double 4 to 8 and add 14", "Divide 14 by 4"],
                "ans": 0,
                "hint": "Split 14 in half, multiply by 4, and double the result.",
                "exp": "Half of 14 is 7; 4 × 7 = 28, and doubling 28 gives 56.",
                "sol": make_sol_html([
                    "Halve the factor 14: 14 ÷ 2 = 7.",
                    "Compute the simpler multiplication: 4 × 7 = 28.",
                    "Double the intermediate result: 28 × 2 = 56.",
                    "Therefore, 4 × 14 = 56."
                ], "Halving one factor and doubling the product preserves the total quantity.")
            },
            {
                "q": "How many times greater is each multiple in the times-15 table compared to the times-5 table?",
                "options": ["2 times", "3 times", "5 times", "10 times"],
                "ans": 1,
                "exp": "Since 15 = 3 × 5, every multiple of 15 is 3 times the corresponding multiple of 5.",
                "hint": "Divide 15 by 5 to find the scaling factor.",
                "sol": make_sol_html([
                    "Compare 1 × 15 = 15 with 1 × 5 = 5 (15 ÷ 5 = 3).",
                    "Compare 2 × 15 = 30 with 2 × 5 = 10 (30 ÷ 10 = 3).",
                    "Every multiple of 15 is exactly 3 times larger than the multiple of 5."
                ], "Table scaling follows the ratio between the base factors.")
            },
            {
                "q": "If 6 × 8 = 48, what is 6 × 16 using doubling?",
                "options": ["84", "96", "106", "112"],
                "ans": 1,
                "hint": "16 is double 8, so double the product 48.",
                "exp": "Double 48 is 96. Therefore, 6 × 16 = 96.",
                "sol": make_sol_html([
                    "Notice that 16 is twice 8.",
                    "Since 6 × 8 = 48, 6 × 16 must equal 2 × 48.",
                    "48 + 48 = 96.",
                    "Therefore, 6 × 16 = 96."
                ], "Doubling one factor doubles the final product.")
            },
            {
                "q": "What is the product of 9 × 12 using the tens-and-ones split?",
                "options": ["98", "102", "108", "118"],
                "ans": 2,
                "hint": "(9 × 10) + (9 × 2).",
                "exp": "(9 × 10 = 90) + (9 × 2 = 18) = 108.",
                "sol": make_sol_html([
                    "Split 12 into 10 + 2.",
                    "9 × 10 = 90.",
                    "9 × 2 = 18.",
                    "90 + 18 = 108."
                ], "Distributive breakdown works for all numbers 11 to 20.")
            },
            {
                "q": "In a 3×3 multiplication matrix, if row headers are 3, 5, 7 and column headers are 2, 4, 6, what is the center cell value (row 5, column 4)?",
                "options": ["10", "15", "20", "24"],
                "ans": 2,
                "hint": "Multiply row header 5 by column header 4.",
                "exp": "5 × 4 = 20.",
                "sol": make_sol_html([
                    "Locate row 2 header: 5.",
                    "Locate column 2 header: 4.",
                    "Compute cell product: 5 × 4 = 20."
                ], "Each matrix cell is the product of its row and column headers.")
            },
            {
                "q": "What digit do all products in the times-10 table end with?",
                "options": ["0", "1", "5", "Even numbers only"],
                "ans": 0,
                "hint": "Think of 10, 20, 30, 40...",
                "exp": "Multiplying any whole number by 10 shifts it one place left, placing 0 in the ones column.",
                "sol": make_sol_html([
                    "Multiples of 10 are 10, 20, 30, 40, 50, etc.",
                    "The ones digit is always 0 because each product consists of whole tens."
                ], "Multiplication by 10 always produces a ones digit of zero.")
            },
            {
                "q": "How can 5 × 18 be calculated using halving and doubling?",
                "options": ["Halve 18 to 9, compute 5 × 9 = 45, double to 90", "Add 18 five times", "Multiply 5 × 10 and add 8", "Double 5 to 10 and double 18"],
                "ans": 0,
                "hint": "Half of 18 is 9; 5 × 9 = 45.",
                "exp": "Half of 18 is 9; 5 × 9 = 45; doubling 45 gives 90.",
                "sol": make_sol_html([
                    "Half of 18 is 9.",
                    "5 × 9 = 45.",
                    "Double 45: 45 × 2 = 90.",
                    "Therefore, 5 × 18 = 90."
                ], "Halving and doubling turns unfamiliar facts into simple single-digit calculations.")
            },
            {
                "q": "Which of the following equals 8 × 15?",
                "options": ["(8 × 10) + (8 × 5) = 120", "(8 × 10) + 5 = 85", "(8 × 5) + 10 = 50", "(8 × 20) - 10 = 150"],
                "ans": 0,
                "hint": "Multiply 8 by both 10 and 5, then add.",
                "exp": "8 × 10 = 80; 8 × 5 = 40; 80 + 40 = 120.",
                "sol": make_sol_html([
                    "8 × 10 = 80.",
                    "8 × 5 = 40.",
                    "80 + 40 = 120.",
                    "Thus, 8 × 15 = 120."
                ], "Distributive area decomposition guarantees quick, accurate table generation.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Decade Scaling, Box Method & Products",
        "speech": "",
        "quizzes": [
            {
                "q": "What is the product of 14 × 20?",
                "options": ["140", "240", "280", "320"],
                "ans": 2,
                "hint": "Multiply 14 by 2, then multiply by 10.",
                "exp": "14 × 2 = 28; 28 × 10 = 280.",
                "sol": make_sol_html([
                    "Decompose 20 into 2 × 10.",
                    "14 × 2 = 28.",
                    "28 × 10 = 280."
                ], "Scaling by decades decomposes the multiple of 10 into single-digit × 10.")
            },
            {
                "q": "In the box grid method for 16 × 13, what are the four chamber products?",
                "options": ["(10×10=100), (6×10=60), (10×3=30), (6×3=18)", "(16×10=160), (16×3=48), (10×3=30), (6×1=6)", "(10×10=100), (6×3=18), (10×1=10), (6×1=6)", "(100, 60, 40, 18)"],
                "ans": 0,
                "hint": "Split 16 into 10 + 6 and 13 into 10 + 3.",
                "exp": "The 4 chambers are 10×10=100, 6×10=60, 10×3=30, and 6×3=18. Sum = 208.",
                "sol": make_sol_html([
                    "Partition factors: 16 = 10 + 6, and 13 = 10 + 3.",
                    "Chamber 1: 10 × 10 = 100.",
                    "Chamber 2: 6 × 10 = 60.",
                    "Chamber 3: 10 × 3 = 30.",
                    "Chamber 4: 6 × 3 = 18.",
                    "Sum: 100 + 60 + 30 + 18 = 208."
                ], "The box method organizes all 4 partial products without carrying confusion.")
            },
            {
                "q": "A museum miniature railway has 12 coaches, each seating 15 visitors. What is the total capacity?",
                "options": ["150 visitors", "165 visitors", "180 visitors", "195 visitors"],
                "ans": 2,
                "hint": "Calculate 12 × 15 using (12 × 10) + (12 × 5).",
                "exp": "12 × 10 = 120; 12 × 5 = 60; 120 + 60 = 180 visitors.",
                "sol": make_sol_html([
                    "Number of coaches = 12.",
                    "Seats per coach = 15.",
                    "Total seats = 12 × 15.",
                    "12 × 10 = 120, and 12 × 5 = 60.",
                    "120 + 60 = 180 seats."
                ], "Vehicle fleet capacity equals number of vehicles × capacity per vehicle.")
            },
            {
                "q": "What is 25 × 30 calculated by decade multiplication?",
                "options": ["650", "700", "750", "800"],
                "ans": 2,
                "hint": "Multiply 25 by 3, then multiply by 10.",
                "exp": "25 × 3 = 75; 75 × 10 = 750.",
                "sol": make_sol_html([
                    "Decompose 30 into 3 × 10.",
                    "Compute 25 × 3 = 75.",
                    "Apply the decade shift: 75 × 10 = 750."
                ], "Decade multiplication shifts the single-digit product one place left.")
            },
            {
                "q": "What is the product of 40 × 60?",
                "options": ["240", "2,400", "24,000", "460"],
                "ans": 1,
                "hint": "4 × 6 = 24, with two decade zeroes.",
                "exp": "4 × 6 = 24; 24 × 100 = 2,400.",
                "sol": make_sol_html([
                    "40 = 4 × 10, and 60 = 6 × 10.",
                    "4 × 6 = 24.",
                    "10 × 10 = 100.",
                    "24 × 100 = 2,400."
                ], "Multiplying two decade numbers produces two trailing zeroes.")
            },
            {
                "q": "Using the box grid method, what is the product of 18 × 14?",
                "options": ["242", "252", "262", "272"],
                "ans": 1,
                "hint": "(10×10=100) + (8×10=80) + (10×4=40) + (8×4=32).",
                "exp": "100 + 80 + 40 + 32 = 252.",
                "sol": make_sol_html([
                    "18 = 10 + 8, and 14 = 10 + 4.",
                    "Partial products: 100 + 80 + 40 + 32.",
                    "100 + 80 = 180.",
                    "180 + 40 = 220.",
                    "220 + 32 = 252."
                ], "Box grid method breaks multi-digit multiplication into 4 clean additions.")
            },
            {
                "q": "If 1 vintage bus carries 35 passengers, how many passengers can 4 such buses transport?",
                "options": ["120", "130", "140", "150"],
                "ans": 2,
                "hint": "4 × 35 = 4 × 30 + 4 × 5.",
                "exp": "4 × 30 = 120; 4 × 5 = 20; 120 + 20 = 140 passengers.",
                "sol": make_sol_html([
                    "Number of buses = 4.",
                    "Passengers per bus = 35.",
                    "4 × 30 = 120.",
                    "4 × 5 = 20.",
                    "120 + 20 = 140 passengers."
                ], "Multiplying decade and unit components gives quick fleet calculations.")
            },
            {
                "q": "What is 16 × 10 expressed in place-value terminology?",
                "options": ["16 Ones", "16 Tens (160)", "16 Hundreds", "106 Units"],
                "ans": 1,
                "exp": "16 × 10 represents 16 Tens, which equals 160.",
                "hint": "Think of 16 rods of ten units each.",
                "sol": make_sol_html([
                    "16 × 10 means 16 groups of 10.",
                    "16 groups of 10 = 16 Tens.",
                    "16 Tens = 160."
                ], "Multiplying by 10 bundles the number directly into tens.")
            },
            {
                "q": "What is the product of 15 × 15 (a square array)?",
                "options": ["215", "225", "235", "245"],
                "ans": 1,
                "hint": "(10×10=100) + (5×10=50) + (10×5=50) + (5×5=25).",
                "exp": "100 + 50 + 50 + 25 = 225.",
                "sol": make_sol_html([
                    "Split both factors into 10 + 5.",
                    "10 × 10 = 100.",
                    "5 × 10 = 50.",
                    "10 × 5 = 50.",
                    "5 × 5 = 25.",
                    "100 + 50 + 50 + 25 = 225."
                ], "Square numbers can be verified through four-quadrant area decomposition.")
            },
            {
                "q": "A tour guide orders 20 souvenir caps at ₹45 each. What is the total cost?",
                "options": ["₹800", "₹850", "₹900", "₹950"],
                "ans": 2,
                "hint": "45 × 2 = 90; 90 × 10 = 900.",
                "exp": "45 × 2 = 90; 90 × 10 = ₹900.",
                "sol": make_sol_html([
                    "Unit price = ₹45.",
                    "Quantity = 20.",
                    "Total = 45 × 20.",
                    "45 × 2 = 90.",
                    "90 × 10 = ₹900."
                ], "Financial procurement uses decade factoring for rapid mental calculation.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Long Division, Remainders & Scaling",
        "speech": "",
        "quizzes": [
            {
                "q": "A school group of 250 students boards museum shuttle vans seating 12 students each. How many vans are needed to carry all students?",
                "options": ["20 vans", "21 vans", "22 vans", "25 vans"],
                "ans": 1,
                "hint": "250 ÷ 12 = 20 remainder 10. The 10 remaining students still need a van!",
                "exp": "250 = (20 × 12) + 10. 20 vans leave 10 students behind, so 21 vans are needed.",
                "sol": make_sol_html([
                    "Divide total students by van capacity: 250 ÷ 12.",
                    "12 × 20 = 240 students.",
                    "250 - 240 = 10 students remaining.",
                    "Quotient = 20, Remainder = 10.",
                    "Since 10 students cannot be abandoned, 20 + 1 = 21 vans are required."
                ], "In passenger transit, any remainder requires an additional vehicle.")
            },
            {
                "q": "What is the quotient and remainder of 185 ÷ 8?",
                "options": ["22 remainder 9", "23 remainder 1", "24 remainder 1", "23 remainder 5"],
                "ans": 1,
                "hint": "8 × 23 = 184.",
                "exp": "8 × 23 = 184; 185 - 184 = 1 remainder.",
                "sol": make_sol_html([
                    "Divide 18 by 8: 8 × 2 = 16 (remainder 2).",
                    "Bring down 5 to make 25.",
                    "Divide 25 by 8: 8 × 3 = 24 (remainder 1).",
                    "Quotient = 23, Remainder = 1."
                ], "Long division processes digits from left to right systematically.")
            },
            {
                "q": "What is the product of 70 × 60?",
                "options": ["420", "4,200", "42,000", "760"],
                "ans": 1,
                "hint": "7 × 6 = 42, then attach two zeroes.",
                "exp": "7 × 6 = 42; 42 × 100 = 4,200.",
                "sol": make_sol_html([
                    "70 = 7 × 10, and 60 = 6 × 10.",
                    "7 × 6 = 42.",
                    "10 × 10 = 100.",
                    "42 × 100 = 4,200."
                ], "Multiplying two multiples of 10 creates a product in hundreds or thousands.")
            },
            {
                "q": "What is 900 ÷ 10?",
                "options": ["9", "90", "900", "9,000"],
                "ans": 1,
                "hint": "Dividing by 10 shifts digits one place right (removes one zero).",
                "exp": "900 ÷ 10 = 90.",
                "sol": make_sol_html([
                    "900 consists of 90 tens.",
                    "Dividing by 10 removes one factor of 10.",
                    "900 ÷ 10 = 90."
                ], "Dividing by 10 shifts the decimal point one position to the left.")
            },
            {
                "q": "What is 3,500 ÷ 100?",
                "options": ["35", "350", "3,500", "35,000"],
                "ans": 0,
                "hint": "Dividing by 100 shifts digits two places right (removes two zeroes).",
                "exp": "3,500 ÷ 100 = 35.",
                "sol": make_sol_html([
                    "3,500 contains 35 hundreds.",
                    "Dividing by 100 removes both trailing zeroes.",
                    "3,500 ÷ 100 = 35."
                ], "Dividing by 100 determines how many hundreds are in the dividend.")
            },
            {
                "q": "A warehouse has 645 kg of wheat. How many 10 kg bags can be filled completely, and how many kg remain?",
                "options": ["64 bags, 5 kg remaining", "60 bags, 45 kg remaining", "65 bags, 0 kg remaining", "640 bags, 5 kg remaining"],
                "ans": 0,
                "hint": "645 ÷ 10 = 64 remainder 5.",
                "exp": "645 = (64 × 10) + 5. 64 full bags, 5 kg remaining.",
                "sol": make_sol_html([
                    "Divide total wheat by bag size: 645 ÷ 10.",
                    "64 × 10 = 640 kg.",
                    "645 - 640 = 5 kg left over.",
                    "Quotient = 64 bags, Remainder = 5 kg."
                ], "Real-world packaging problems map directly to quotient and remainder.")
            },
            {
                "q": "What is the product of 12 × 300?",
                "options": ["360", "3,600", "36,000", "1,230"],
                "ans": 1,
                "hint": "12 × 3 = 36; then multiply by 100.",
                "exp": "12 × 3 = 36; 36 × 100 = 3,600.",
                "sol": make_sol_html([
                    "Decompose 300 into 3 × 100.",
                    "12 × 3 = 36.",
                    "36 × 100 = 3,600."
                ], "Factoring hundreds scales the single-digit product by two decimal places.")
            },
            {
                "q": "If a divisor is 7, the quotient is 14, and the remainder is 3, what is the dividend?",
                "options": ["95", "98", "101", "105"],
                "ans": 2,
                "hint": "Dividend = (Divisor × Quotient) + Remainder.",
                "exp": "(7 × 14) + 3 = 98 + 3 = 101.",
                "sol": make_sol_html([
                    "Apply formula: Dividend = (Divisor × Quotient) + Remainder.",
                    "7 × 14 = 98.",
                    "98 + 3 = 101.",
                    "Dividend = 101."
                ], "The division formula is the universal proof check for long division.")
            },
            {
                "q": "Why is the remainder in any division problem always strictly less than the divisor?",
                "options": ["By random rule", "Because if the remainder were equal to or greater than the divisor, another group could be formed", "To save paper", "Because division only works on even numbers"],
                "ans": 1,
                "hint": "If you have 8 items left and groups are size 8, you can make 1 more group!",
                "exp": "If remainder ≥ divisor, another full group can be subtracted into the quotient.",
                "sol": make_sol_html([
                    "Division groups items into equal sets of size Divisor.",
                    "If leftover items ≥ Divisor, at least one more full set can be formed.",
                    "Therefore, the final remainder must always be strictly less than the divisor."
                ], "Remainder < Divisor is an inviolable law of integer arithmetic.")
            },
            {
                "q": "What is 500 × 40?",
                "options": ["2,000", "20,000", "200,000", "4,500"],
                "ans": 1,
                "hint": "5 × 4 = 20, then attach three zeroes (two from 500, one from 40).",
                "exp": "5 × 4 = 20; 20 × 1,000 = 20,000.",
                "sol": make_sol_html([
                    "5 × 4 = 20.",
                    "500 has two zeroes; 40 has one zero (total 3 trailing zeroes).",
                    "Append 3 zeroes to 20: 20,000.",
                    "Therefore, 500 × 40 = 20,000."
                ], "Do not confuse the zero in 20 with the attached place-holding zeroes!")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Denominations, Patterns & Fleet Matching",
        "speech": "",
        "quizzes": [
            {
                "q": "A museum ticket buyer needs to pay ₹485. Which combination uses the fewest notes and coins?",
                "options": [
                    "2 notes of ₹200 + 1 note of ₹50 + 1 note of ₹20 + 1 note of ₹10 + 1 coin of ₹5",
                    "4 notes of ₹100 + 8 notes of ₹10 + 5 coins of ₹1",
                    "9 notes of ₹50 + 3 notes of ₹10 + 1 coin of ₹5",
                    "1 note of ₹500 - ₹15 change"
                ],
                "ans": 0,
                "hint": "Start with the largest denomination: ₹200 × 2 = ₹400.",
                "exp": "400 + 50 + 20 + 10 + 5 = ₹485 using 5 notes/coins.",
                "sol": make_sol_html([
                    "Highest denomination: 2 × ₹200 = ₹400 (leaves ₹85).",
                    "Next denomination: 1 × ₹50 = ₹50 (leaves ₹35).",
                    "Next denomination: 1 × ₹20 = ₹20 (leaves ₹15).",
                    "Next denomination: 1 × ₹10 = ₹10 (leaves ₹5).",
                    "Final coin: 1 × ₹5 = ₹5 (balance zero).",
                    "Total = ₹485 with only 5 currency units."
                ], "Greedy denomination selection minimizes the physical count of notes and coins.")
            },
            {
                "q": "What is the product of 45 × 11 using the two-digit multiplication pattern?",
                "options": ["455", "485", "495", "505"],
                "ans": 2,
                "hint": "Split 4 and 5, insert (4 + 5 = 9) in the middle.",
                "exp": "4 _ 5 with 4 + 5 = 9 gives 495.",
                "sol": make_sol_html([
                    "To multiply a two-digit number by 11:",
                    "Keep the hundreds digit as 4.",
                    "Keep the ones digit as 5.",
                    "The middle tens digit is the sum of the digits: 4 + 5 = 9.",
                    "Result: 495."
                ], "Multiplying by 11 inserts the sum of digits between the original digits.")
            },
            {
                "q": "What is the total passenger capacity of a fleet of 6 auto-rickshaws (3 passengers each) and 4 cars (5 passengers each)?",
                "options": ["32 passengers", "36 passengers", "38 passengers", "42 passengers"],
                "ans": 2,
                "hint": "(6 × 3) + (4 × 5).",
                "exp": "6 × 3 = 18; 4 × 5 = 20; 18 + 20 = 38 passengers.",
                "sol": make_sol_html([
                    "Auto-rickshaws capacity = 6 × 3 = 18 passengers.",
                    "Passenger cars capacity = 4 × 5 = 20 passengers.",
                    "Total combined capacity = 18 + 20 = 38 passengers."
                ], "Mixed fleet calculations sum the individual sub-fleet products.")
            },
            {
                "q": "If 1 train sleeper coach accommodates 72 passengers, how many passengers do 5 sleeper coaches accommodate?",
                "options": ["340 passengers", "350 passengers", "360 passengers", "370 passengers"],
                "ans": 2,
                "hint": "5 × 72 = (5 × 70) + (5 × 2).",
                "exp": "5 × 70 = 350; 5 × 2 = 10; 350 + 10 = 360 passengers.",
                "sol": make_sol_html([
                    "5 × 70 = 350.",
                    "5 × 2 = 10.",
                    "350 + 10 = 360 passengers."
                ], "Long-distance train coaches offer massive passenger capacities per coach.")
            },
            {
                "q": "What is the total value of 5 notes of ₹200 and 6 notes of ₹50?",
                "options": ["₹1,200", "₹1,250", "₹1,300", "₹1,350"],
                "ans": 2,
                "hint": "(5 × 200) + (6 × 50).",
                "exp": "(5 × 200 = 1,000) + (6 × 50 = 300) = ₹1,300.",
                "sol": make_sol_html([
                    "5 × ₹200 = ₹1,000.",
                    "6 × ₹50 = ₹300.",
                    "₹1,000 + ₹300 = ₹1,300."
                ], "Combining note bundles requires evaluating each denomination group before adding.")
            },
            {
                "q": "Which number has a digital root (sum of digits) equal to 9?",
                "options": ["73", "81", "92", "100"],
                "ans": 1,
                "hint": "8 + 1 = 9.",
                "exp": "8 + 1 = 9. 81 is a multiple of 9 (9 × 9).",
                "sol": make_sol_html([
                    "Compute digit sums:",
                    "7 + 3 = 10 (1 + 0 = 1).",
                    "8 + 1 = 9 (Multiple of 9!).",
                    "9 + 2 = 11 (1 + 1 = 2).",
                    "1 + 0 + 0 = 1."
                ], "All multiples of 9 reduce to a digital root of 9.")
            },
            {
                "q": "How many bicycles (carrying 1 person each) and auto-rickshaws (carrying 3 persons each) are needed to carry 15 people if exactly 3 auto-rickshaws are used?",
                "options": ["4 bicycles", "5 bicycles", "6 bicycles", "7 bicycles"],
                "ans": 2,
                "hint": "3 auto-rickshaws carry 3 × 3 = 9 people. Remaining = 15 - 9.",
                "exp": "3 autos carry 9 people. 15 - 9 = 6 people, requiring 6 bicycles.",
                "sol": make_sol_html([
                    "Auto capacity = 3 × 3 = 9 people.",
                    "Remaining people = 15 - 9 = 6 people.",
                    "Bicycle capacity = 1 person per bicycle.",
                    "Bicycles needed = 6 ÷ 1 = 6 bicycles."
                ], "Multi-modal vehicle matching uses subtraction and division to balance fleets.")
            },
            {
                "q": "What is 72 ÷ 10 expressed as a mixed quotient and remainder?",
                "options": ["6 remainder 12", "7 remainder 2", "7 remainder 0", "8 remainder 2"],
                "ans": 1,
                "hint": "7 × 10 = 70 with 2 left over.",
                "exp": "72 = (7 × 10) + 2. Quotient 7, remainder 2.",
                "sol": make_sol_html([
                    "70 contains exactly 7 tens.",
                    "72 - 70 = 2 units remainder.",
                    "Quotient = 7, Remainder = 2."
                ], "Dividing by 10 separates the tens digit from the ones remainder digit.")
            },
            {
                "q": "What is the product of 52 × 11?",
                "options": ["562", "572", "582", "592"],
                "ans": 1,
                "hint": "Split 5 and 2, insert (5 + 2 = 7) in the center.",
                "exp": "5 _ 2 with 5 + 2 = 7 gives 572.",
                "sol": make_sol_html([
                    "First digit: 5.",
                    "Last digit: 2.",
                    "Middle digit: 5 + 2 = 7.",
                    "Combined product: 572."
                ], "The 11s pattern enables rapid mental multiplication without carrying when sum < 10.")
            },
            {
                "q": "A museum hangar holds 3 transport aeroplanes seating 180 passengers each. What is the total fleet capacity?",
                "options": ["480 passengers", "520 passengers", "540 passengers", "560 passengers"],
                "ans": 2,
                "hint": "3 × 180 = 3 × 18 × 10.",
                "exp": "3 × 18 = 54; 54 × 10 = 540 passengers.",
                "sol": make_sol_html([
                    "Number of aeroplanes = 3.",
                    "Seats per aeroplane = 180.",
                    "Total capacity = 3 × 180.",
                    "3 × 18 = 54.",
                    "54 × 10 = 540 passengers."
                ], "Scaling aeroplane fleets demonstrates how commercial transit moves hundreds of citizens.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} challenge slides.")
    total_q = sum(len(s.get("quizzes", [])) for s in slides_part3)
    print(f"Total quiz questions: {total_q}")
    assert len(slides_part3) == 4, "Must have exactly 4 challenge slides"
    assert total_q == 40, "Must have exactly 40 quiz questions"
    for s in slides_part3:
        tw = len(s["title"].split())
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert len(s["quizzes"]) == 10, f"Slide {s['id']} must have 10 questions"
        for qz in s["quizzes"]:
            assert "hint" in qz, f"Question missing hint: {qz['q']}"
            assert "sol" in qz, f"Question missing sol: {qz['q']}"
            assert len(qz["options"]) == 4, f"Question must have 4 options: {qz['q']}"
    print("All Part 3 challenge assertions passed successfully!")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 8: Fractions in Disguise
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Percent Foundations Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Etymology, Fractions-to-Percent, Base-10 System, History & Track Comparisons",
        "questions": [
            {
                "question": "The term 'per cent' originates from the Latin phrase 'per centum', meaning 'out of hundred'. Accordingly, what fraction equals 37%?",
                "options": [
                    "37 / 100",
                    "37 / 10",
                    "37 / 1000",
                    "100 / 37"
                ],
                "answer": 0,
                "hint": "Every z% means z parts out of 100 equal parts!",
                "explanation": "By definition, z% = z/100, so 37% = 37/100.",
                "solution_steps": [
                    "Recall etymology: Latin 'per centum' literally translates to 'out of hundred'.",
                    "Write percentage symbol % as denominator 100: z% = z / 100.",
                    "Substitute z = 37 directly to get fraction 37/100."
                ]
            },
            {
                "question": "Convert the fraction 9/20 to a percentage by finding an equivalent fraction with denominator 100:",
                "options": [
                    "45%   (9/20 = 45/100)",
                    "9%   (9/100)",
                    "90%   (90/100)",
                    "4.5%   (4.5/100)"
                ],
                "answer": 0,
                "hint": "Multiply both numerator 9 and denominator 20 by 5 so the denominator becomes 100!",
                "explanation": "(9 × 5) / (20 × 5) = 45/100 = 45%.",
                "solution_steps": [
                    "Find factor turning 20 into 100: 100 ÷ 20 = 5.",
                    "Scale fraction equivalently: (9 × 5) / (20 × 5) = 45/100.",
                    "Express parts per hundred directly as 45%."
                ]
            },
            {
                "question": "Which calculation converts the fraction 5/8 accurately into a percentage?",
                "options": [
                    "(5/8) × 100% = 500/8% = 62.5%",
                    "(5/8) × 10% = 6.25%",
                    "(8/5) × 100% = 160%",
                    "65% directly"
                ],
                "answer": 0,
                "hint": "Multiply 5/8 directly by 100 (since 8 × 12.5 = 100)!",
                "explanation": "(5/8) × 100 = 500/8 = 62.5%.",
                "solution_steps": [
                    "Recognize denominator 8 does not scale to 100 by an integer.",
                    "Apply universal method: multiply fraction by 100 → (5/8) × 100 = 500/8.",
                    "Divide 500 ÷ 8 = 62.5 to conclude 62.5%."
                ]
            },
            {
                "question": "Why does a base-10 number system strongly favor 100 ('per cent') over bases like 60 or 80 for expressing proportions?",
                "options": [
                    "100 = 10², so percentages shift directly by 2 decimal places for effortless mental decimal math",
                    "Because 100 is odd and easy to split into thirds",
                    "Because calculators only understand numbers up to 100",
                    "Because base-10 fractions never simplify"
                ],
                "answer": 0,
                "hint": "Notice how quickly 38% becomes 0.38 by shifting two places!",
                "explanation": "In base-10, denominator 100 = 10² maps seamlessly onto two decimal places (e.g., 38/100 = 0.38).",
                "solution_steps": [
                    "Connect base-10 place values: hundredths occupy the second decimal column.",
                    "Dividing by 100 = 10² requires moving the decimal point only 2 places left.",
                    "This gives fine 1/100 precision with zero messy arithmetic."
                ]
            },
            {
                "question": "Which 4th-century BCE Indian text recorded rules for monthly interest rates per hundred panas?",
                "options": [
                    "Kautilya's Arthashastra",
                    "Aryabhatiya",
                    "Brahmasphutasiddhanta",
                    "Lilavati"
                ],
                "answer": 0,
                "hint": "Look back at the 4th century BCE Indian economic treatise noted in Section 1.1!",
                "explanation": "Kautilya's Arthashastra (4th century BCE) documented monthly interest rates stated per hundred.",
                "solution_steps": [
                    "Identify 4th century BCE Indian statecraft and economics treatise.",
                    "Recall Kautilya's Arthashastra detailing credit rates per hundred per month.",
                    "Contrast with 15th-century Italian manuscripts that later shaped the % sign."
                ]
            },
            {
                "question": "Roughly what percentage of the total mass of the entire Solar System resides inside the Sun alone?",
                "options": [
                    "Over 99.8% (leaving < 0.2% for all planets and moons)",
                    "About 50%",
                    "About 75%",
                    "About 60%"
                ],
                "answer": 0,
                "hint": "The Sun dwarfs Jupiter and every planet combined by almost everything!",
                "explanation": "Astronomical measurements show the Sun holds over 99.8% of Solar System mass.",
                "solution_steps": [
                    "Recall NCERT Section 1.1 'Percentages Around Us' statistics.",
                    "Adult human body water is ~60%, while Solar System mass is >99.8% in the Sun.",
                    "Select > 99.8% accurately."
                ]
            },
            {
                "question": "Along a 0% to 100% running track, Runner A is at 3/5 and Runner B is at 13/20. Which runner is farther along and why?",
                "options": [
                    "Runner B (65%) leads Runner A (60%) by 5 percentage points",
                    "Runner A (65%) leads Runner B (60%)",
                    "Runner A (60%) leads Runner B (55%)",
                    "Both are at equal track markers"
                ],
                "answer": 0,
                "hint": "Scale 3/5 = 60/100 and 13/20 = 65/100!",
                "explanation": "3/5 = 60% and 13/20 = 65%, putting Runner B ahead by 5 percentage points.",
                "solution_steps": [
                    "Convert Runner A: (3/5) × 100 = 60%.",
                    "Convert Runner B: (13/20) × 100 = 65%.",
                    "Compare: 65% > 60%, so Runner B leads by 5 points."
                ]
            },
            {
                "question": "Arrange the following values in strictly ascending order: 3/4, 72%, 4/5, 0.78:",
                "options": [
                    "72% < 3/4 < 0.78 < 4/5",
                    "3/4 < 72% < 4/5 < 0.78",
                    "72% < 0.78 < 3/4 < 4/5",
                    "4/5 < 0.78 < 3/4 < 72%"
                ],
                "answer": 0,
                "hint": "Rewrite all four quantities as percentages first: 75%, 72%, 80%, 78%!",
                "explanation": "72% < 75% (3/4) < 78% (0.78) < 80% (4/5).",
                "solution_steps": [
                    "Convert each quantity to percent: 3/4 = 75%, 72% = 72%, 4/5 = 80%, 0.78 = 78%.",
                    "Sort numerically: 72% < 75% < 78% < 80%.",
                    "Substitute back original symbols: 72% < 3/4 < 0.78 < 4/5."
                ]
            },
            {
                "question": "In a 10 × 10 square grid (100 unit cells), 3 full rows and 7 extra squares remain UNSHADED. What percentage of the grid IS shaded?",
                "options": [
                    "63%",
                    "37%",
                    "73%",
                    "30%"
                ],
                "answer": 0,
                "hint": "Unshaded squares = 37 out of 100! Subtract 37% from 100%!",
                "explanation": "37 unshaded squares leave 100 − 37 = 63 shaded squares = 63%.",
                "solution_steps": [
                    "Count unshaded cells: 3 rows × 10 + 7 = 37 squares.",
                    "Subtract from total 100 squares: 100 − 37 = 63 shaded squares.",
                    "Write 63/100 cleanly as 63%."
                ]
            },
            {
                "question": "Express 7/40 cleanly as an exact percentage:",
                "options": [
                    "17.5%",
                    "14%",
                    "28%",
                    "1.75%"
                ],
                "answer": 0,
                "hint": "Compute (7/40) × 100 = 700/40 = 70/4!",
                "explanation": "(7/40) × 100 = 70/4 = 17.5%.",
                "solution_steps": [
                    "Multiply fraction by 100: (7/40) × 100.",
                    "Cancel factor 20: (7/2) × 5 = 35/2.",
                    "Divide 35 ÷ 2 = 17.5%."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Quantity Mental Quiz",
        "subtitle": "Challenge Arena 2 (10 MCQs): Contextual Whole, Bar Models, Mental Benchmarks, FDP Trio & Above 100%",
        "questions": [
            {
                "question": "School X reports 80% attendance out of 50 enrolled students, while School Y reports 40% attendance out of 300 students. Which school has more students present today?",
                "options": [
                    "School Y (120 present) beats School X (40 present) — percentages depend on their contextual whole!",
                    "School X (120 present) beats School Y (40 present)",
                    "School X automatically has more because 80% > 40%",
                    "Both schools have equal attendance"
                ],
                "answer": 0,
                "hint": "Calculate 80% of 50 and 40% of 300 individually!",
                "explanation": "School X: 0.80 × 50 = 40 students; School Y: 0.40 × 300 = 120 students.",
                "solution_steps": [
                    "Compute School X attendance: (80/100) × 50 = 40 students.",
                    "Compute School Y attendance: (40/100) × 300 = 120 students.",
                    "Notice School Y's larger base (300 vs 50) yields 3× as many students despite lower percentage."
                ]
            },
            {
                "question": "Using the proportional equation a/100 = s/total, solve for total library size if 30% equals 75 science books:",
                "options": [
                    "250 total books",
                    "225 total books",
                    "150 total books",
                    "300 total books"
                ],
                "answer": 0,
                "hint": "Set 30/100 = 75/total! Note 10% = 75 ÷ 3 = 25 books!",
                "explanation": "30% = 75 → 10% = 25 → 100% = 25 × 10 = 250 books.",
                "solution_steps": [
                    "Write proportion 30/100 = 75/total.",
                    "Solve unit block: 10% = 75 ÷ 3 = 25 books (or 30 × total = 7,500).",
                    "Scale to 100%: total = 7,500 ÷ 30 = 250 books."
                ]
            },
            {
                "question": "Find 15% of ₹840 mentally using benchmark decomposition (10% + 5%):",
                "options": [
                    "₹126   (84 + 42)",
                    "₹116",
                    "₹134",
                    "₹84"
                ],
                "answer": 0,
                "hint": "First take 10% of 840 (= 84), then halve 84 for 5%!",
                "explanation": "10% of 840 = 84; 5% = 42; 84 + 42 = ₹126.",
                "solution_steps": [
                    "Take 10% of ₹840 by shifting decimal: 840 ÷ 10 = ₹84.",
                    "Take 5% as half of 10%: 84 ÷ 2 = ₹42.",
                    "Add benchmark blocks: 84 + 42 = ₹126."
                ]
            },
            {
                "question": "Find 25% of 480 minutes using the benchmark fraction equivalent:",
                "options": [
                    "120 minutes   (480 ÷ 4)",
                    "96 minutes",
                    "240 minutes",
                    "60 minutes"
                ],
                "answer": 0,
                "hint": "Remember 25% equals exactly 1/4 of a whole!",
                "explanation": "25% = 1/4, and 480 ÷ 4 = 120 minutes (2 hours).",
                "solution_steps": [
                    "Convert benchmark 25% = 25/100 = 1/4.",
                    "Divide base quantity by 4: 480 ÷ 4 = 120.",
                    "Result is 120 minutes."
                ]
            },
            {
                "question": "A workshop sets a daily quota of 60 ceramic mugs. Today artisans craft 90 mugs. What percentage of the daily quota was achieved?",
                "options": [
                    "150%",
                    "66.7%",
                    "90%",
                    "130%"
                ],
                "answer": 0,
                "hint": "90 is 1.5 times the 60-mug baseline target!",
                "explanation": "(90/60) × 100% = 1.5 × 100% = 150%.",
                "solution_steps": [
                    "Set quota whole = 60 mugs (100%).",
                    "Form ratio actual/quota = 90/60 = 3/2 = 1.5.",
                    "Multiply by 100% → 150% (50% above target)."
                ]
            },
            {
                "question": "Which FDP Trio row is completely consistent across Fraction, Decimal, and Percentage?",
                "options": [
                    "3/8  |  0.375  |  37.5%",
                    "3/8  |  0.38   |  38%",
                    "7/5  |  1.4    |  14%",
                    "1/20 |  0.5    |  5%"
                ],
                "answer": 0,
                "hint": "Check 3 ÷ 8 = 0.375 and 0.375 × 100% = 37.5%!",
                "explanation": "3/8 = 0.375 = 37.5%, while the other options have decimal-place errors.",
                "solution_steps": [
                    "Verify 3 ÷ 8 = 0.375 cleanly.",
                    "Multiply 0.375 × 100% = 37.5%.",
                    "Eliminate 7/5 = 140% (not 14%) and 1/20 = 0.05 (not 0.5)."
                ]
            },
            {
                "question": "In the estimation game 'How Close Can You Get?', which benchmark best estimates 49% of 398?",
                "options": [
                    "~200   (using 50% of 400)",
                    "~100",
                    "~40",
                    "~350"
                ],
                "answer": 0,
                "hint": "Round 49% to 50% (1/2) and 398 to 400!",
                "explanation": "50% of 400 = 200 (exact 49% × 398 = 195.02).",
                "solution_steps": [
                    "Round 49% closely to anchor 50% (= 1/2).",
                    "Round 398 closely to friendly number 400.",
                    "Compute 1/2 × 400 = 200 immediately."
                ]
            },
            {
                "question": "A pancake recipe weighing 500 g uses 60% flour, 25% sugar, and the remainder milk powder. How many grams of milk powder are needed for a doubled 1,000 g batch?",
                "options": [
                    "150 g",
                    "75 g",
                    "250 g",
                    "300 g"
                ],
                "answer": 0,
                "hint": "Milk powder share = 100% − 60% − 25% = 15%! Compute 15% of 1,000 g!",
                "explanation": "Milk powder is 15% of batch; 15% of 1,000 g = 150 g.",
                "solution_steps": [
                    "Find milk powder %: 100% − (60% + 25%) = 15%.",
                    "Use doubled batch total = 1,000 g.",
                    "Compute 15% of 1,000 g = (15/100) × 1,000 = 150 g."
                ]
            },
            {
                "question": "Suppose 12% of a number equals 36. What is 100% of that number?",
                "options": [
                    "300",
                    "432",
                    "250",
                    "360"
                ],
                "answer": 0,
                "hint": "Divide 36 by 12 to find 1% (= 3), then multiply by 100!",
                "explanation": "1% = 36 ÷ 12 = 3, so 100% = 3 × 100 = 300.",
                "solution_steps": [
                    "Apply unit-rate scaling: 12% = 36.",
                    "Find 1%: 36 ÷ 12 = 3.",
                    "Scale to 100%: 3 × 100 = 300."
                ]
            },
            {
                "question": "What percentage equals 2.45 when expressed via the FDP Trio?",
                "options": [
                    "245%",
                    "24.5%",
                    "2.45%",
                    "2450%"
                ],
                "answer": 0,
                "hint": "Multiply any decimal cleanly by 100 (shift decimal point 2 spots right)!",
                "explanation": "2.45 × 100% = 245% (greater than 100% because 2.45 > 1).",
                "solution_steps": [
                    "Take decimal value 2.45.",
                    "Multiply by 100 (shift two places right): 2.45 → 245.",
                    "Attach % symbol → 245%."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Commerce Growth Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Comparing Proportions, % Change, Profit/Loss, Gross vs Net, GST & Compounding/Decay",
        "questions": [
            {
                "question": "Compare two food bars in 'Know Your Contents': Bar A (80 g) has 12 g fiber; Bar B (125 g) has 15 g fiber. Which bar has a higher fiber percentage?",
                "options": [
                    "Bar A (15% fiber) beats Bar B (12% fiber)",
                    "Bar B (15% fiber) beats Bar A (12% fiber)",
                    "Bar B wins because 15 g > 12 g",
                    "Both contain 12% fiber"
                ],
                "answer": 0,
                "hint": "Calculate (12/80) × 100 and (15/125) × 100!",
                "explanation": "Bar A: 12/80 = 3/20 = 15%; Bar B: 15/125 = 3/25 = 12%.",
                "solution_steps": [
                    "Compute Bar A fiber %: (12/80) × 100 = (3/20) × 100 = 15%.",
                    "Compute Bar B fiber %: (15/125) × 100 = (3/25) × 100 = 12%.",
                    "Bar A has higher proportional fiber content (15% > 12%)."
                ]
            },
            {
                "question": "A bicycle's price dropped from ₹5,000 to ₹4,250 during a seasonal sale. What was the percentage decrease?",
                "options": [
                    "15% decrease",
                    "17.6% decrease",
                    "85% decrease",
                    "20% decrease"
                ],
                "answer": 0,
                "hint": "Divide the ₹750 drop by ORIGINAL ₹5,000, not ₹4,250!",
                "explanation": "Decrease = ₹750; (750 / 5,000) × 100 = 15%.",
                "solution_steps": [
                    "Find Amount of Change: 5,000 − 4,250 = ₹750.",
                    "Divide by Original Base (₹5,000): 750 / 5,000 = 0.15.",
                    "Multiply by 100 → 15% decrease (new price is 85% of original)."
                ]
            },
            {
                "question": "A retailer buys stationery at Cost Price ₹1,200, sets Marked Price at ₹1,800, and sells after discount for Selling Price ₹1,500. Find Profit%:",
                "options": [
                    "25% profit   (based on CP ₹1,200)",
                    "20% profit",
                    "16.67% loss",
                    "30% profit"
                ],
                "answer": 0,
                "hint": "Profit = SP − CP = ₹300, divided over Cost Price ₹1,200!",
                "explanation": "Profit = ₹1,500 − ₹1,200 = ₹300; Profit% = (300/1,200) × 100 = 25%.",
                "solution_steps": [
                    "Identify CP = ₹1,200 and SP = ₹1,500 (SP > CP → Profit).",
                    "Compute Profit = 1,500 − 1,200 = ₹300.",
                    "Compute Profit% on CP: (300 / 1,200) × 100 = 25%."
                ]
            },
            {
                "question": "A shop achieves Sales of ₹80,000, Cost of Goods Sold ₹52,000, and Operating Expenses (rent/utilities) ₹12,000. What is its Net Profit?",
                "options": [
                    "₹16,000   (Gross ₹28,000 − Expenses ₹12,000)",
                    "₹28,000",
                    "₹68,000",
                    "₹40,000"
                ],
                "answer": 0,
                "hint": "Gross Profit = Sales − COGS; then subtract Operating Expenses for Net Profit!",
                "explanation": "Gross Profit = 80,000 − 52,000 = ₹28,000; Net Profit = 28,000 − 12,000 = ₹16,000.",
                "solution_steps": [
                    "Compute Gross Profit = Sales − Cost of Goods = 80,000 − 52,000 = ₹28,000.",
                    "Subtract Operating Expenses = ₹12,000.",
                    "Net Profit = 28,000 − 12,000 = ₹16,000."
                ]
            },
            {
                "question": "An electronics bill has a Selling Price of ₹10,000 with 18% intra-state GST (split equally into CGST and SGST). What is the SGST amount and final payable bill?",
                "options": [
                    "SGST = ₹900 (9%); Total Bill = ₹11,800",
                    "SGST = ₹1,800 (18%); Total Bill = ₹13,600",
                    "SGST = ₹900; Total Bill = ₹10,900",
                    "SGST = ₹1,000; Total Bill = ₹11,800"
                ],
                "answer": 0,
                "hint": "18% GST splits equally into 9% CGST + 9% SGST on ₹10,000!",
                "explanation": "9% CGST = ₹900, 9% SGST = ₹900; total tax = ₹1,800; final bill = ₹11,800.",
                "solution_steps": [
                    "Split 18% GST equally: CGST = 9%, SGST = 9%.",
                    "Compute 9% of ₹10,000 = ₹900 each (₹1,800 combined GST).",
                    "Add tax to SP: 10,000 + 1,800 = ₹11,800."
                ]
            },
            {
                "question": "Compute the final amount on ₹10,000 at 10% annual rate after 2 years using COMPOUNDING growth p(1 + r)^t:",
                "options": [
                    "₹12,100",
                    "₹12,000   (non-compounding)",
                    "₹11,000",
                    "₹12,200"
                ],
                "answer": 0,
                "hint": "Compute 10,000 × (1.10)² = 10,000 × 1.21!",
                "explanation": "p(1 + r)^t = 10,000 × (1.10)² = ₹12,100 (₹100 more than simple growth ₹12,000).",
                "solution_steps": [
                    "Substitute p = 10,000, r = 0.10, t = 2 into A = p(1 + r)^t.",
                    "Calculate (1 + 0.10)² = 1.1² = 1.21.",
                    "Multiply 10,000 × 1.21 = ₹12,100."
                ]
            },
            {
                "question": "How much EXTRA amount does ₹5,000 earn in 2 years at 20% compound growth compared with 20% non-compounding simple growth?",
                "options": [
                    "₹200 extra   (₹7,200 vs ₹7,000)",
                    "₹0 difference",
                    "₹400 extra",
                    "₹1,000 extra"
                ],
                "answer": 0,
                "hint": "Simple: 5000(1 + 0.4) = 7,000; Compound: 5000(1.2)² = 5000 × 1.44!",
                "explanation": "Compound reaches 5,000 × 1.44 = ₹7,200 vs Simple ₹7,000 → ₹200 extra.",
                "solution_steps": [
                    "Compute simple linear growth: 5,000 × (1 + 0.20 × 2) = 5,000 × 1.40 = ₹7,000.",
                    "Compute compounding growth: 5,000 × (1.20)² = 5,000 × 1.44 = ₹7,200.",
                    "Find difference: 7,200 − 7,000 = ₹200."
                ]
            },
            {
                "question": "A town's population starts at 40,000 and grows at 5% compounded annually. Which expression predicts population after 3 years?",
                "options": [
                    "40,000 × (1.05)³ = 46,305",
                    "40,000 × (1 + 0.15) = 46,000",
                    "40,000 × (0.95)³ = 34,295",
                    "40,000 × 1.5³ = 135,000"
                ],
                "answer": 0,
                "hint": "Convert 5% to decimal r = 0.05 and use p(1 + r)^3!",
                "explanation": "40,000 × 1.05³ = 40,000 × 1.157625 = 46,305.",
                "solution_steps": [
                    "Set p = 40,000, r = 0.05, t = 3 in A = p(1 + r)^t.",
                    "Compute (1.05)³ = 1.157625.",
                    "Multiply 40,000 × 1.157625 = 46,305."
                ]
            },
            {
                "question": "A delivery scooter bought for ₹60,000 depreciates at 20% annually under p(1 − r)^t. Find its worth after 2 years:",
                "options": [
                    "₹38,400",
                    "₹36,000",
                    "₹48,000",
                    "₹24,000"
                ],
                "answer": 0,
                "hint": "Remaining multiplier each year is 1 − 0.20 = 0.80; compute 60,000 × 0.80²!",
                "explanation": "60,000 × 0.80 × 0.80 = 60,000 × 0.64 = ₹38,400.",
                "solution_steps": [
                    "Compute retention factor per year: 1 − 0.20 = 0.80.",
                    "After Year 1: 60,000 × 0.80 = ₹48,000.",
                    "After Year 2: 48,000 × 0.80 = ₹38,400."
                ]
            },
            {
                "question": "If the final price after an item rises by 25% is ₹500, what was its ORIGINAL price before the increase?",
                "options": [
                    "₹400",
                    "₹375",
                    "₹425",
                    "₹625"
                ],
                "answer": 0,
                "hint": "Remember ₹500 represents 125% OF original (never subtract 25% of 500)!",
                "explanation": "1.25 × Original = ₹500 → Original = 500 ÷ 1.25 = ₹400.",
                "solution_steps": [
                    "Recognize +25% increase means new price = 125% = 1.25 × Original.",
                    "Set up equation: 1.25 × Original = 500.",
                    "Divide carefully: Original = 500 ÷ 1.25 = ₹400."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Traps Knights Quiz",
        "subtitle": "Challenge Arena 4 (10 MCQs): Successive Discounts, Asymmetry, Deals, Area % Change, Summary & Peaceful Knights",
        "questions": [
            {
                "question": "A clothing store advertises '30% off + an extra 20% off!'. What single equivalent discount does this give?",
                "options": [
                    "44% effective discount",
                    "50% effective discount",
                    "40% effective discount",
                    "48% effective discount"
                ],
                "answer": 0,
                "hint": "Multiply remaining factors cleanly: 0.70 × 0.80 = 0.56 paid → discount is 1 − 0.56!",
                "explanation": "Paying 70% then 80% leaves 0.70 × 0.80 = 0.56 (56% paid), giving a 44% discount.",
                "solution_steps": [
                    "Start with marked price ₹100; 30% off drops price to ₹70 (× 0.70).",
                    "Apply extra 20% off ₹70: 70 × 0.80 = ₹56 paid.",
                    "Net saved = 100 − 56 = ₹44 → 44% effective discount."
                ]
            },
            {
                "question": "A shopkeeper first marks goods UP by +40% and then gives a −40% discount on the marked price. What is the overall percentage profit or loss?",
                "options": [
                    "16% net loss   (1.40 × 0.60 = 0.84)",
                    "0% no profit no loss",
                    "16% net profit",
                    "8% net loss"
                ],
                "answer": 0,
                "hint": "Test ₹100: +40% makes ₹140; now take 60% remaining of ₹140!",
                "explanation": "100 × 1.40 = 140; 140 × 0.60 = ₹84 → ₹16 loss per ₹100 = 16% net loss.",
                "solution_steps": [
                    "Start at ₹100; +40% markup sets Marked Price = ₹140.",
                    "Apply −40% discount on ₹140: SP = 140 × 0.60 = ₹84.",
                    "Compare SP ₹84 to CP ₹100 → 16% net loss."
                ]
            },
            {
                "question": "Journalists hype Village A ('fastest growing library' — jumped from 10 to 30 books, +200%) over Town B (jumped from 1,000 to 1,400 books, +40%). What fallacy occurs here?",
                "options": [
                    "Base-size fallacy: Village A added only 20 books while Town B added 400 books (20× more!)",
                    "Arithmetic addition fallacy",
                    "Compound interest fallacy",
                    "No fallacy — Village A literally added more books"
                ],
                "answer": 0,
                "hint": "Compare absolute book additions alongside starting base sizes (10 vs 1,000)!",
                "explanation": "Tiny initial base 10 makes just +20 books look like +200%, whereas Town B added 400 books.",
                "solution_steps": [
                    "Compute absolute gains: Village A = +20 books; Town B = +400 books.",
                    "Observe Village A started tiny (10 books), inflating relative % to +200%.",
                    "Conclude relative % headlines without base sizes cause base-size fallacy."
                ]
            },
            {
                "question": "Which supermarket promotion gives a HIGHER true percentage discount: Deal P ('Buy 3 Get 1 Free') or Deal Q ('Buy 4 Get 2 Free')?",
                "options": [
                    "Deal Q (33.33% off) beats Deal P (25% off)",
                    "Deal P (33.33% off) beats Deal Q (25% off)",
                    "Both equal 25% off",
                    "Deal P (40% off) beats Deal Q (30% off)"
                ],
                "answer": 0,
                "hint": "Compute Free ÷ Total Items Received: Deal P = 1/4, Deal Q = 2/6!",
                "explanation": "Deal P = 1/4 = 25% discount; Deal Q = 2/6 = 1/3 = 33.33% discount.",
                "solution_steps": [
                    "Deal P: take 4 items, 1 free → (1/4) × 100 = 25% off.",
                    "Deal Q: take 6 items, 2 free → (2/6) × 100 = 33.33% off.",
                    "Deal Q gives the better effective discount."
                ]
            },
            {
                "question": "A rectangular garden increases its length by 30% and decreases its width by 10%. What is the net percentage change in area?",
                "options": [
                    "+17% increase in area   (1.30 × 0.90 = 1.17)",
                    "+20% increase in area",
                    "−17% decrease in area",
                    "+3% increase in area"
                ],
                "answer": 0,
                "hint": "Multiply scale factors directly: 1.30 × 0.90!",
                "explanation": "New area = 1.30 L × 0.90 W = 1.17 LW, which is a +17% net area increase.",
                "solution_steps": [
                    "Convert changes to multipliers: Length × 1.30, Width × 0.90.",
                    "Multiply factors for area: 1.30 × 0.90 = 1.17.",
                    "Interpret 1.17 − 1.00 = +0.17 → +17% area increase."
                ]
            },
            {
                "question": "Which statement summarizes Chapter 8's rule for combining successive percentage changes of r₁ and r₂?",
                "options": [
                    "Multiply factors (1 ± r₁)(1 ± r₂) — never add percentages directly",
                    "Always add r₁ + r₂ regardless of direction",
                    "Multiply r₁ × r₂ directly",
                    "Take the arithmetic mean (r₁ + r₂)/2"
                ],
                "answer": 0,
                "hint": "Each consecutive percentage operates on the newly updated intermediate amount!",
                "explanation": "Successive changes compound multiplicatively as (1 ± r₁)(1 ± r₂).",
                "solution_steps": [
                    "First change maps base p to p(1 ± r₁).",
                    "Second change acts on that updated value: p(1 ± r₁)(1 ± r₂).",
                    "Net multiplier equals (1 ± r₁)(1 ± r₂)."
                ]
            },
            {
                "question": "If every side of a square increases by 10%, by what percentage does its area increase?",
                "options": [
                    "21% increase   (1.10 × 1.10 = 1.21)",
                    "20% increase",
                    "10% increase",
                    "100% increase"
                ],
                "answer": 0,
                "hint": "Square Area = side × side scales by 1.10 × 1.10!",
                "explanation": "New area = (1.1 s)² = 1.21 s², an increase of 21%.",
                "solution_steps": [
                    "Multiply both length and breadth by 1.10.",
                    "Compute area factor: 1.10 × 1.10 = 1.21.",
                    "Subtract original 1.00 → 0.21 = 21% area increase."
                ]
            },
            {
                "question": "In the 'Peaceful Knights' puzzle on an 8 × 8 chessboard, from square d4 (row 4, column 4), which square CANNOT be reached in one valid L-shaped knight move?",
                "options": [
                    "f6   (diagonal 2+2, not 2+1!)",
                    "f5   (+2, +1)",
                    "e6   (+1, +2)",
                    "b3   (−2, −1)"
                ],
                "answer": 0,
                "hint": "A knight moves strictly 2 squares along one axis and 1 along the perpendicular axis!",
                "explanation": "d4 → f6 moves (+2, +2), which is a bishop diagonal, not an L-shaped knight jump.",
                "solution_steps": [
                    "Test coordinate offsets from (4, 4).",
                    "f5 is (+2, +1), e6 is (+1, +2), b3 is (−2, −1) — all valid L-moves.",
                    "f6 is (+2, +2), so it is unreachable in one knight move."
                ]
            },
            {
                "question": "If you place 8 Peaceful Knights safely along edge column 'a' (a1 through a8) of an 8 × 8 chessboard, do ANY two attack each other? What is the true bipartite reason knights on ONLY dark squares never attack each other?",
                "options": [
                    "No two attack along column 'a'; every L-jump switches square color (dark ↔ light), so same-color knights never meet!",
                    "Column 'a' knights attack adjacent neighbors; knights move same-color to same-color",
                    "Knights along column 'a' attack diagonally 1 step; dark-square knights attack dark squares",
                    "Only corners can be peaceful"
                ],
                "answer": 0,
                "hint": "Check whether any pair in the same column differs by (±2, ±1), AND remember L-moves always invert parity!",
                "explanation": "Column 'a' shares zero perpendicular offset (±1), and every (2+1) L-move flips dark ↔ light parity.",
                "solution_steps": [
                    "Check pairs in column 'a': column change = 0, never ±1 or ±2, so zero attacks!",
                    "Check general parity: ±2 keeps color, ±1 flips color.",
                    "Hence dark-square knights only attack light squares — allowing up to 32 peaceful knights (50% of board)."
                ]
            },
            {
                "question": "What is the MAXIMUM number of Peaceful Knights that can be placed on an 8 × 8 chessboard using the dark-squares strategy, and what percentage of the 64 squares does this cover?",
                "options": [
                    "32 knights covering 50% of the board",
                    "16 knights covering 25% of the board",
                    "8 knights covering 12.5% of the board",
                    "48 knights covering 75% of the board"
                ],
                "answer": 0,
                "hint": "Half of an 8 × 8 chessboard's 64 squares share the dark color!",
                "explanation": "64 ÷ 2 = 32 same-color squares; 32/64 = 50% coverage with zero attacks.",
                "solution_steps": [
                    "Count dark squares on standard 8 × 8 chessboard: 64 ÷ 2 = 32.",
                    "Verify parity: knights on dark squares threaten only light squares.",
                    "Compute % coverage: (32/64) × 100 = 50%."
                ]
            }
        ]
    }
]

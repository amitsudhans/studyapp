#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 13: Algebra Play
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Tricks Birthday Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Sections 6.1–6.2 Variable Modeling, Cancellation Tricks & 100M + 165 + D",
        "questions": [
            {
                "question": "In Section 6.1, why do mathematicians replace specific test numbers with variables like x or a?",
                "options": [
                    "To prove a pattern works universally for EVERY number at once rather than just lucky examples",
                    "Because calculators prefer letters over numbers",
                    "Because arithmetic works only for odd numbers",
                    "To hide mistakes"
                ],
                "answer": 0,
                "hint": "Compare checking 3 test numbers vs proving for ALL numbers!",
                "explanation": "Variables represent arbitrary numbers, turning specific arithmetic tricks into general proofs.",
                "solution_steps": [
                    "Observe numeric examples only confirm individual cases.",
                    "Assign variable x to an arbitrary starting value.",
                    "Simplify algebraic steps to verify universal truth."
                ]
            },
            {
                "question": "Trace this trick algebraically: Think of x → Multiply by 3 → Add 15 → Divide by 3 → Subtract original x. What constant always remains?",
                "options": [
                    "5",
                    "15",
                    "3",
                    "x + 5"
                ],
                "answer": 0,
                "hint": "Simplify (3x + 15) ÷ 3 first, then subtract x!",
                "explanation": "(3x + 15) ÷ 3 = x + 5; subtracting x cancels x cleanly to leave 5.",
                "solution_steps": [
                    "Express steps 1–3 algebraically: 3x + 15.",
                    "Divide evenly by 3: (3x + 15) ÷ 3 = x + 5.",
                    "Subtract original x: (x + 5) − x = 5."
                ]
            },
            {
                "question": "Simplify the 'Think of a Number' expression: ((2n − 8) ÷ 2) + 4:",
                "options": [
                    "n   (always returns the original starting number!)",
                    "n + 4",
                    "n − 4",
                    "2n"
                ],
                "answer": 0,
                "hint": "Divide BOTH 2n and −8 by 2 before adding +4!",
                "explanation": "(2n − 8) ÷ 2 = n − 4; adding 4 leaves exact original n.",
                "solution_steps": [
                    "Divide both terms inside parentheses by 2: 2n÷2 − 8÷2 = n − 4.",
                    "Add 4: (n − 4) + 4 = n.",
                    "Every starting number returns unchanged."
                ]
            },
            {
                "question": "If someone claims 'Take x, multiply by 4, add 8, divide by 2, and subtract x — your answer is always 4!', test x = 10 to see what went WRONG:",
                "options": [
                    "The result equals x + 4 (for x = 10, gives 14!), because 4x ÷ 2 = 2x and 2x − x leaves x instead of cancelling",
                    "The trick actually gives 4 for every x",
                    "8 ÷ 2 equals 2, not 4",
                    "Dividing by 2 leaves 4x"
                ],
                "answer": 0,
                "hint": "Compute (4x + 8) ÷ 2 − x carefully!",
                "explanation": "(4x + 8) ÷ 2 = 2x + 4; subtracting x leaves x + 4, failing to cancel x completely.",
                "solution_steps": [
                    "Divide 4x + 8 by 2 → 2x + 4.",
                    "Subtract x → 2x + 4 − x = x + 4.",
                    "Since x stays inside x + 4, the output depends on x (not constant!)."
                ]
            },
            {
                "question": "In the birthday prediction formula 100M + 165 + D, someone born on August 9 (M = 8, D = 9) reports what raw number BEFORE subtracting 165?",
                "options": [
                    "974   (100(8) + 165 + 9)",
                    "809",
                    "965",
                    "874"
                ],
                "answer": 0,
                "hint": "Compute 800 + 165 + 9!",
                "explanation": "800 + 165 + 9 = 974 (subtracting 165 recovers 809 → Month 8, Day 9).",
                "solution_steps": [
                    "Substitute M = 8 and D = 9 into 100M + 165 + D.",
                    "Calculate 100(8) = 800.",
                    "Sum 800 + 165 + 9 = 974."
                ]
            },
            {
                "question": "Using the 100M + 165 + D birthday decoder, a participant announces final sum 1,392. What is their exact birthday?",
                "options": [
                    "December 27   (1,392 − 165 = 1,227 → Month 12, Day 27)",
                    "November 27",
                    "December 17",
                    "October 27"
                ],
                "answer": 0,
                "hint": "Compute 1,392 − 165, then separate the last two digits (Day) from the leading digits (Month)!",
                "explanation": "Subtracting the constant offset: 1,392 − 165 = 1,227. In 100M + D, the leading digits 12 give Month 12 (December) and the last two digits 27 give Day 27.",
                "solution_steps": [
                    "Step 1: Recall the trick formula evaluates to 100M + 165 + D.",
                    "Step 2: Subtract 165 from the announced total: 1,392 − 165 = 1,227.",
                    "Step 3: Read Month M = 12 (December) from hundreds/thousands and Day D = 27 from the last two digits."
                ]
            },
            {
                "question": "Verify why ((5M + 6) × 4 + 9) × 5 + D ALWAYS simplifies to 100M + 165 + D:",
                "options": [
                    "(20M + 33) × 5 + D = 100M + 165 + D",
                    "(20M + 15) × 5 + D = 100M + 75 + D",
                    "(5M + 15) × 20 + D = 100M + 300 + D",
                    "(20M + 24) × 5 + D = 100M + 120 + D"
                ],
                "answer": 0,
                "hint": "Expand (5M + 6) × 4 = 20M + 24 first, add 9 to get 20M + 33, then multiply by 5!",
                "explanation": "4(5M + 6) + 9 = 20M + 33; multiplying by 5 yields 100M + 165, plus D.",
                "solution_steps": [
                    "Distribute 4: 4(5M + 6) = 20M + 24.",
                    "Add 9: 20M + 33.",
                    "Multiply by 5 and add D: 5(20M + 33) + D = 100M + 165 + D."
                ]
            },
            {
                "question": "Why does subtracting 165 fail to mix Month M and Day D digits together (say for M = 11 and D = 30)?",
                "options": [
                    "Because every calendar day D ≤ 31 takes at most 2 digits (01–31), fitting completely below the 100s place occupied by 100M",
                    "Because months only go up to 9",
                    "Because 165 divides every day D evenly",
                    "Because D gets multiplied by 10"
                ],
                "answer": 0,
                "hint": "Note 100(11) + 30 = 1,130 — D never carries into the 100s place because D < 100!",
                "explanation": "Since 1 ≤ D ≤ 31 < 100, D occupies strictly the units and tens digits while M stays cleanly in hundreds/thousands.",
                "solution_steps": [
                    "After subtracting 165, expression becomes 100M + D.",
                    "Notice 100M ends in two zeros (..M00).",
                    "Since D ≤ 31 < 100, adding D never overflows into M's place."
                ]
            },
            {
                "question": "Suppose you invent a new trick: 'Pick x, add 7, triple it, subtract 6, divide by 3, subtract x'. What fixed number should you announce?",
                "options": [
                    "5   ((3x + 21 − 6)/3 − x = (3x + 15)/3 − x = 5)",
                    "7",
                    "15",
                    "1"
                ],
                "answer": 0,
                "hint": "Expand 3(x + 7) = 3x + 21, subtract 6 → 3x + 15, divide by 3, then subtract x!",
                "explanation": "(3x + 15) ÷ 3 = x + 5; subtracting x always yields 5.",
                "solution_steps": [
                    "Compute 3(x + 7) − 6 = 3x + 21 − 6 = 3x + 15.",
                    "Divide by 3: (3x + 15) ÷ 3 = x + 5.",
                    "Subtract x → constant 5."
                ]
            },
            {
                "question": "How would you modify the 100M + 165 + D trick if you wanted to decode Day FIRST in thousands/hundreds and Month LAST in the two rightmost digits (100D + M)?",
                "options": [
                    "Start with Day D (instead of Month M), compute 100D + 165 + M, and subtract 165!",
                    "Start with M and multiply by 1,000",
                    "Subtract 100 instead of 165",
                    "Divide M by 100"
                ],
                "answer": 0,
                "hint": "Notice any starting variable x ends up multiplied by 100 while the final added variable stays in the last two digits!",
                "explanation": "Swapping inputs puts Day D in 100D and Month M (1–12 < 100) cleanly in the final two digits.",
                "solution_steps": [
                    "Identify which variable enters the machine first (gets ×100).",
                    "Feed Day D first and add Month M last → 100D + 165 + M.",
                    "Subtract 165 → 100D + M (since M ≤ 12 < 100)."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Pyramids Grids Quiz",
        "subtitle": "Challenge Arena 2 (10 MCQs): Sections 6.3–6.4 Number Pyramids, Virahāṅka-Fibonacci, Calendar & Shape Grids",
        "questions": [
            {
                "question": "In a 3-row addition pyramid, the bottom row holds 9, 4, 11. What sits at the TOP peak brick?",
                "options": [
                    "28   (9 + 2×4 + 11 = 28)",
                    "24   (9 + 4 + 11)",
                    "32",
                    "26"
                ],
                "answer": 0,
                "hint": "Middle row is 9+4 = 13 and 4+11 = 15 → sum = 13 + 15!",
                "explanation": "Using a + 2b + c: 9 + 2(4) + 11 = 28.",
                "solution_steps": [
                    "Row 2 left = 9 + 4 = 13; Row 2 right = 4 + 11 = 15.",
                    "Top peak = 13 + 15 = 28.",
                    "Verify with formula a + 2b + c: 9 + 8 + 11 = 28."
                ]
            },
            {
                "question": "A 3-row pyramid has bottom bricks 7, x, 13 and Top peak 44. Solve 7 + 2x + 13 = 44 for missing middle base brick x:",
                "options": [
                    "x = 12",
                    "x = 24",
                    "x = 10",
                    "x = 14"
                ],
                "answer": 0,
                "hint": "Combine 7 + 13 = 20 → 2x + 20 = 44!",
                "explanation": "2x = 44 − 20 = 24 → x = 12.",
                "solution_steps": [
                    "Apply 3-row peak equation: 7 + 2x + 13 = 44.",
                    "Combine constants: 2x + 20 = 44 → 2x = 24.",
                    "Divide by 2 → x = 12."
                ]
            },
            {
                "question": "What algebraic expression represents the TOP brick of a 4-row addition pyramid with bottom base a, b, c, d?",
                "options": [
                    "a + 3b + 3c + d",
                    "a + 2b + 2c + d",
                    "a + 4b + 4c + d",
                    "3a + b + c + 3d"
                ],
                "answer": 0,
                "hint": "Row 3 has (a+2b+c) and (b+2c+d) — add them together!",
                "explanation": "(a + 2b + c) + (b + 2c + d) = a + 3b + 3c + d.",
                "solution_steps": [
                    "Row 2: a+b, b+c, c+d.",
                    "Row 3: a+2b+c and b+2c+d.",
                    "Top brick sums Row 3 → a + 3b + 3c + d."
                ]
            },
            {
                "question": "Using the 4-row pyramid peak equation a + 3b + 3c + d = Top, if bottom bricks are 3, x, x, 5 and Top = 38, find x:",
                "options": [
                    "x = 5   (8 + 6x = 38 → 6x = 30)",
                    "x = 6",
                    "x = 4",
                    "x = 10"
                ],
                "answer": 0,
                "hint": "Plug b = x and c = x into 3 + 3x + 3x + 5 = 38!",
                "explanation": "3 + 5 + 6x = 38 → 6x = 30 → x = 5.",
                "solution_steps": [
                    "Substitute a=3, b=x, c=x, d=5: 3 + 3x + 3x + 5 = 38.",
                    "Combine like terms: 6x + 8 = 38 → 6x = 30.",
                    "Solve x = 5."
                ]
            },
            {
                "question": "Place consecutive Virahāṅka-Fibonacci numbers 3, 5, 8, 13 along the bottom row of a 4-row addition pyramid. What exact number reaches the TOP peak?",
                "options": [
                    "55",
                    "34",
                    "89",
                    "42"
                ],
                "answer": 0,
                "hint": "Row 2 is 8, 13, 21; Row 3 is 21, 34 → Top = 21 + 34!",
                "explanation": "8, 13, 21 → 21, 34 → 55 (advancing cleanly along the Virahāṅka-Fibonacci sequence!).",
                "solution_steps": [
                    "Row 2 sums: 3+5=8, 5+8=13, 8+13=21.",
                    "Row 3 sums: 8+13=21, 13+21=34.",
                    "Top sum: 21 + 34 = 55."
                ]
            },
            {
                "question": "In a 2 × 2 monthly calendar block (a, a+1, a+7, a+8), the four dates sum to S = 84. Find the top-left date a and bottom-right date (a + 8):",
                "options": [
                    "Top-left = 17; Bottom-right = 25   (dates 17, 18, 24, 25)",
                    "Top-left = 16; Bottom-right = 24",
                    "Top-left = 18; Bottom-right = 26",
                    "Top-left = 15; Bottom-right = 23"
                ],
                "answer": 0,
                "hint": "Solve 4a + 16 = 84 → 4a = 68!",
                "explanation": "4a = 84 − 16 = 68 → a = 17; bottom-right = 17 + 8 = 25.",
                "solution_steps": [
                    "Apply calendar box formula: 4a + 16 = 84.",
                    "Subtract 16: 4a = 68 → top-left a = 17.",
                    "Bottom-right corner = 17 + 8 = 25."
                ]
            },
            {
                "question": "A friend claims they circled a valid 2 × 2 square box on a regular monthly calendar whose 4 dates add up to 74. How can you prove IMMEDIATELY they misadded?",
                "options": [
                    "Because 74 − 16 = 58 is NOT divisible by 4 (all valid 2 × 2 calendar sums satisfy 4a + 16 = 4(a + 4))",
                    "Because 74 exceeds 31",
                    "Because calendar rows only hold 5 days",
                    "Because 74 is odd"
                ],
                "answer": 0,
                "hint": "Test 4a + 16 = 74 — does integer a exist?!",
                "explanation": "74 is not a multiple of 4 (4a = 58 gives 14.5, impossible for calendar dates!).",
                "solution_steps": [
                    "Set up 4a + 16 = 74.",
                    "Subtract 16 → 4a = 58 → a = 14.5.",
                    "Since dates must be whole integers, 74 is impossible."
                ]
            },
            {
                "question": "In ANY 2 × 2 monthly calendar block, compare the two cross-diagonal sums (top-left + bottom-right) vs (top-right + bottom-left):",
                "options": [
                    "Always equal: (a) + (a + 8) = 2a + 8 = (a + 1) + (a + 7)",
                    "Top-left + bottom-right is always larger by 7",
                    "Top-right + bottom-left is always larger by 1",
                    "They match only on Mondays"
                ],
                "answer": 0,
                "hint": "Expand both sums using variable a!",
                "explanation": "Both diagonals evaluate to 2a + 8 for any starting date a.",
                "solution_steps": [
                    "Compute main diagonal: a + (a + 8) = 2a + 8.",
                    "Compute anti-diagonal: (a + 1) + (a + 7) = 2a + 8.",
                    "Identical algebraic expressions prove universal equality."
                ]
            },
            {
                "question": "In an Algebra Grid, Row 1 = [Star, Star, Star] = 36, and Row 2 = [Star, Moon, Moon] = 28. What value does ONE Moon hold?",
                "options": [
                    "Moon = 8",
                    "Moon = 12",
                    "Moon = 16",
                    "Moon = 6"
                ],
                "answer": 0,
                "hint": "First divide 36 ÷ 3 = 12 for Star, then solve 12 + 2×Moon = 28!",
                "explanation": "Star = 12; 12 + 2×Moon = 28 → 2×Moon = 16 → Moon = 8.",
                "solution_steps": [
                    "Solve Row 1: 3 × Star = 36 → Star = 12.",
                    "Substitute into Row 2: 12 + 2 × Moon = 28.",
                    "2 × Moon = 16 → Moon = 8."
                ]
            },
            {
                "question": "In an Algebra Grid where Hexagon = 5 and Diamond = 14, a column holds [Hexagon, Hexagon, Diamond]. What total belongs beneath that column?",
                "options": [
                    "24   (5 + 5 + 14)",
                    "19",
                    "33",
                    "28"
                ],
                "answer": 0,
                "hint": "Add two Hexagons plus one Diamond: 5 + 5 + 14!",
                "explanation": "5 + 5 + 14 = 24.",
                "solution_steps": [
                    "Write column sum expression: 2 × Hexagon + Diamond.",
                    "Substitute values: 2(5) + 14.",
                    "Calculate 10 + 14 = 24."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Products Divisibility Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Sections 6.5–6.6 Largest Product Proof & Divisibility Tricks (9, 11, 37, 1001)",
        "questions": [
            {
                "question": "Arrange distinct digits 4, 6, and 8 into (□□ × □) to yield the ABSOLUTE MAXIMUM possible product:",
                "options": [
                    "64 × 8 = 512",
                    "86 × 4 = 344",
                    "84 × 6 = 504",
                    "46 × 8 = 368"
                ],
                "answer": 0,
                "hint": "Place largest digit 8 outside, and descending remaining digits (64) inside!",
                "explanation": "64 × 8 = 512 beats 84 × 6 = 504 by 4 × (8 − 6) = 8.",
                "solution_steps": [
                    "Apply qp × r optimality rule with p=4, q=6, r=8.",
                    "Form 64 × 8 = 512.",
                    "Verify 512 > 504 (84×6) > 344 (86×4)."
                ]
            },
            {
                "question": "Why does qp × r ALWAYS beat rp × q for distinct digits p < q < r?",
                "options": [
                    "Because (10qr + pr) − (10rq + pq) = p(r − q) > 0 strictly",
                    "Because r must always sit in the tens place",
                    "Because q × p is always negative",
                    "Because 10qr > 10rq"
                ],
                "answer": 0,
                "hint": "Expand (10q + p)r and (10r + p)q to compare!",
                "explanation": "10qr cancels 10rq cleanly, leaving pr − pq = p(r − q) > 0.",
                "solution_steps": [
                    "Expand qp × r = 10qr + pr.",
                    "Expand rp × q = 10rq + pq.",
                    "Subtract: pr − pq = p(r − q) > 0 since p > 0 and r > q."
                ]
            },
            {
                "question": "Without full multiplication, compute the EXACT difference (52 × 9) − (92 × 5) using the formula p(r − q):",
                "options": [
                    "8   (2 × (9 − 5))",
                    "4",
                    "20",
                    "40"
                ],
                "answer": 0,
                "hint": "Here p = 2, q = 5, r = 9 → calculate 2 × (9 − 5)!",
                "explanation": "2 × (9 − 5) = 8 (check: 468 − 460 = 8!).",
                "solution_steps": [
                    "Match digits p = 2, q = 5, r = 9.",
                    "Evaluate p(r − q) = 2(9 − 5) = 2 × 4 = 8.",
                    "Verify directly: 468 − 460 = 8."
                ]
            },
            {
                "question": "When reversing ANY two-digit number 'ab' (b > a) to form 'ba', what algebraic identity proves (ba − ab) is ALWAYS divisible by 9?",
                "options": [
                    "(10b + a) − (10a + b) = 9(b − a)",
                    "(10b + a) + (10a + b) = 11(a + b)",
                    "10b − 10a = 10(b − a)",
                    "ab − ba = 0"
                ],
                "answer": 0,
                "hint": "Expand 10b + a minus 10a + b!",
                "explanation": "10b − b + a − 10a = 9b − 9a = 9(b − a), always a multiple of 9.",
                "solution_steps": [
                    "Write ba = 10b + a and ab = 10a + b.",
                    "Subtract: (10b + a) − (10a + b) = 9b − 9a.",
                    "Factor 9 → 9(b − a)."
                ]
            },
            {
                "question": "Add a two-digit number 'ab' and its digit reversal 'ba' together. Which factor ALWAYS divides (ab + ba)?",
                "options": [
                    "11   (since ab + ba = 11(a + b))",
                    "9",
                    "7",
                    "37"
                ],
                "answer": 0,
                "hint": "Add (10a + b) + (10b + a)!",
                "explanation": "(10a + b) + (10b + a) = 11a + 11b = 11(a + b).",
                "solution_steps": [
                    "Expand ab + ba = (10a + b) + (10b + a).",
                    "Combine like terms: 11a + 11b.",
                    "Factor 11 → 11(a + b)."
                ]
            },
            {
                "question": "If ab + ba = 154, what must the sum of digits (a + b) equal?",
                "options": [
                    "14",
                    "11",
                    "15",
                    "7"
                ],
                "answer": 0,
                "hint": "Solve 11(a + b) = 154!",
                "explanation": "154 ÷ 11 = 14 (e.g., 68 + 86 = 154).",
                "solution_steps": [
                    "Equate 11(a + b) = 154.",
                    "Divide both sides by 11.",
                    "a + b = 154 ÷ 11 = 14."
                ]
            },
            {
                "question": "Take 3-digit number 417, form cyclic shifts 174 and 741, and compute S = 417 + 174 + 741 = 1,332. What equals 1,332 ÷ 37?",
                "options": [
                    "36   (3 × (4 + 1 + 7) = 3 × 12)",
                    "12",
                    "111",
                    "41"
                ],
                "answer": 0,
                "hint": "Recall abc + bca + cab = 37 × 3(a + b + c)!",
                "explanation": "Dividing by 37 leaves 3(a + b + c) = 3(4 + 1 + 7) = 3 × 12 = 36.",
                "solution_steps": [
                    "Use cyclic identity: S = 111(a + b + c) = 37 × 3(a + b + c).",
                    "Compute a + b + c = 4 + 1 + 7 = 12.",
                    "S ÷ 37 = 3 × 12 = 36."
                ]
            },
            {
                "question": "Why does ANY repeated 6-digit number 'abcabc' (such as 285,285) ALWAYS divide evenly by 7, 11, AND 13?",
                "options": [
                    "Because abcabc = 1001 × abc, and 1001 factors cleanly into 7 × 11 × 13",
                    "Because a + b + c always equals 7 + 11 + 13",
                    "Because 1000 = 7 × 11 × 13",
                    "Because 6-digit numbers are always prime"
                ],
                "answer": 0,
                "hint": "Write abcabc = 1000·abc + abc = 1001·abc!",
                "explanation": "1001 = 7 × 11 × 13 guarantees every 6-digit repeat abcabc is a multiple of 7, 11, and 13.",
                "solution_steps": [
                    "Expand place value: abcabc = 1000 × abc + 1 × abc = 1001 × abc.",
                    "Prime factorize 1001 = 7 × 11 × 13.",
                    "Hence 7, 11, and 13 divide abcabc with zero remainder."
                ]
            },
            {
                "question": "Solve quickly without long division: what is 624,624 ÷ (7 × 11 × 13)?",
                "options": [
                    "624",
                    "1001",
                    "1248",
                    "62"
                ],
                "answer": 0,
                "hint": "Remember 7 × 11 × 13 = 1001, and 624,624 = 1001 × 624!",
                "explanation": "(1001 × 624) ÷ 1001 = 624 instantaneously.",
                "solution_steps": [
                    "Recognize 7 × 11 × 13 = 1001.",
                    "Factor 624,624 = 1001 × 624.",
                    "Cancel 1001 → exact quotient 624."
                ]
            },
            {
                "question": "If the cyclic sum abc + bca + cab equals 1,998, what is the sum of the three digits (a + b + c)?",
                "options": [
                    "18   (1,998 ÷ 111 = 18)",
                    "9",
                    "27",
                    "54"
                ],
                "answer": 0,
                "hint": "Divide 1,998 by 111 since abc + bca + cab = 111(a + b + c)!",
                "explanation": "1,998 ÷ 111 = 18 → a + b + c = 18 (e.g., 5 + 6 + 7 = 18).",
                "solution_steps": [
                    "Apply identity 111(a + b + c) = 1,998.",
                    "Divide: 1,998 ÷ 111 = 18.",
                    "Digit sum a + b + c = 18."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Word Puzzles Summary",
        "subtitle": "Challenge Arena 4 (10 MCQs): Shrine/Genie Double-Deduct, Legs/Ages/Cowherd, Dosa Break-Even & Summary",
        "questions": [
            {
                "question": "In the 3-shrine puzzle, a pond doubles flowers before each shrine and 8 flowers are offered inside each shrine, finishing with 0 flowers after Shrine 3. How many flowers x did the pilgrim start with?",
                "options": [
                    "7 flowers   (8x − 56 = 0 → x = 7)",
                    "8 flowers",
                    "14 flowers",
                    "6 flowers"
                ],
                "answer": 0,
                "hint": "Work forward: 7 → 14−8=6 → 12−8=4 → 8−8=0!",
                "explanation": "2(2(2x − 8) − 8) − 8 = 8x − 56 = 0 → x = 7.",
                "solution_steps": [
                    "After Shrine 1: 2x − 8; After Shrine 2: 2(2x − 8) − 8 = 4x − 24.",
                    "After Shrine 3: 2(4x − 24) − 8 = 8x − 56 = 0.",
                    "Solve 8x = 56 → x = 7 flowers."
                ]
            },
            {
                "question": "In the Traveler and the Genie puzzle, the genie doubles pouch coins and takes 16 coins fee in EACH of 2 rounds, leaving 0 coins at the end. How many coins did the traveler start with?",
                "options": [
                    "12 coins   (4x − 48 = 0 → x = 12)",
                    "16 coins",
                    "8 coins",
                    "14 coins"
                ],
                "answer": 0,
                "hint": "Check Round 1: 2(12)−16 = 8; Round 2: 2(8)−16 = 0!",
                "explanation": "2(2x − 16) − 16 = 4x − 48 = 0 → x = 12 coins.",
                "solution_steps": [
                    "After Round 1: 2x − 16 coins remain.",
                    "After Round 2: 2(2x − 16) − 16 = 4x − 48 = 0.",
                    "Solve 4x = 48 → x = 12 coins."
                ]
            },
            {
                "question": "A barnyard contains horses (4 legs) and hens (2 legs) with 30 heads and 84 total legs. How many horses and hens are there?",
                "options": [
                    "12 horses and 18 hens",
                    "18 horses and 12 hens",
                    "14 horses and 16 hens",
                    "10 horses and 20 hens"
                ],
                "answer": 0,
                "hint": "Solve 4x + 2(30 − x) = 84 → 2x + 60 = 84!",
                "explanation": "2x = 24 → 12 horses and 30 − 12 = 18 hens (check: 48 + 36 = 84 legs).",
                "solution_steps": [
                    "Let horses = x, so hens = 30 − x.",
                    "Equate legs: 4x + 2(30 − x) = 84 → 2x + 60 = 84.",
                    "2x = 24 → 12 horses, 18 hens."
                ]
            },
            {
                "question": "A mother is 3 times her daughter's age right now. Twelve years from now, the mother will be ONLY twice as old. How old is the daughter today?",
                "options": [
                    "12 years old   (check: 12 & 36 → +12 yrs: 24 & 48)",
                    "10 years old",
                    "14 years old",
                    "18 years old"
                ],
                "answer": 0,
                "hint": "Solve 3x + 12 = 2(x + 12) = 2x + 24!",
                "explanation": "3x + 12 = 2x + 24 → x = 12 years.",
                "solution_steps": [
                    "Present ages: daughter x, mother 3x.",
                    "Add 12 years: 3x + 12 = 2(x + 12) = 2x + 24.",
                    "Subtract 2x and 12 → x = 12 years."
                ]
            },
            {
                "question": "A cowherd tends x cows: half graze in the pasture, one-third drink at the river, and 15 rest under a banyan tree. Solve x/2 + x/3 + 15 = x:",
                "options": [
                    "90 cows",
                    "60 cows",
                    "75 cows",
                    "45 cows"
                ],
                "answer": 0,
                "hint": "Add 1/2 + 1/3 = 5/6 of x, leaving 1/6 of x = 15!",
                "explanation": "(1 − 5/6)x = 15 → (1/6)x = 15 → x = 90 cows.",
                "solution_steps": [
                    "Add fractions: 1/2 + 1/3 = 3/6 + 2/6 = 5/6.",
                    "Remaining fraction: x − (5/6)x = (1/6)x = 15.",
                    "Multiply 15 × 6 = 90 cows."
                ]
            },
            {
                "question": "A dosa cart pays ₹800 fixed daily expenses plus ₹12 per dosa made, and sells each dosa for ₹32. How many dosas n hit the break-even point?",
                "options": [
                    "40 dosas",
                    "25 dosas",
                    "66 dosas",
                    "50 dosas"
                ],
                "answer": 0,
                "hint": "Solve 32n = 800 + 12n → 20n = 800!",
                "explanation": "Profit per dosa = 32 − 12 = ₹20; 800 ÷ 20 = 40 dosas.",
                "solution_steps": [
                    "Write Total Cost = 800 + 12n and Revenue = 32n.",
                    "Equate 32n = 800 + 12n → 20n = 800.",
                    "Solve n = 800 ÷ 20 = 40 dosas."
                ]
            },
            {
                "question": "In that same dosa cart problem (₹800 fixed + ₹12/dosa, selling at ₹32), how much pure PROFIT does selling 55 dosas earn?",
                "options": [
                    "₹300 profit   (15 extra dosas past 40 × ₹20 margin)",
                    "₹1,100 profit",
                    "₹160 profit",
                    "₹550 profit"
                ],
                "answer": 0,
                "hint": "Revenue = 55 × 32 = ₹1,760; Cost = 800 + 55 × 12 = ₹1,460!",
                "explanation": "1,760 − 1,460 = ₹300 profit (or (55 − 40) × ₹20 = ₹300).",
                "solution_steps": [
                    "Compute Revenue = 55 × ₹32 = ₹1,760.",
                    "Compute Cost = ₹800 + (55 × ₹12) = ₹800 + ₹660 = ₹1,460.",
                    "Profit = 1,760 − 1,460 = ₹300."
                ]
            },
            {
                "question": "Solve the nested fraction series equation: x/2 + x/4 + x/8 + x/16 + 7 = x:",
                "options": [
                    "x = 112",
                    "x = 64",
                    "x = 56",
                    "x = 128"
                ],
                "answer": 0,
                "hint": "Sum fractions 8/16 + 4/16 + 2/16 + 1/16 = 15/16 of x, leaving (1/16)x = 7!",
                "explanation": "(1/16)x = 7 → x = 7 × 16 = 112.",
                "solution_steps": [
                    "Add fractions over 16: (8 + 4 + 2 + 1)/16 = 15/16.",
                    "Subtract from 1: (1/16)x = 7.",
                    "Multiply 7 × 16 = 112."
                ]
            },
            {
                "question": "A 4-row addition pyramid starts with Virahāṅka-Fibonacci numbers 1, 2, 3, 5, while another puzzle multiplies digits 1, 4, 9 into (□□ × □). What are the top pyramid value AND max digit product?",
                "options": [
                    "Top Pyramid = 21; Max Product = 41 × 9 = 369",
                    "Top Pyramid = 13; Max Product = 94 × 1 = 94",
                    "Top Pyramid = 21; Max Product = 91 × 4 = 364",
                    "Top Pyramid = 11; Max Product = 49 × 1 = 49"
                ],
                "answer": 0,
                "hint": "Check 1 + 3(2) + 3(3) + 5 = 21 and qp × r = 41 × 9!",
                "explanation": "4-row pyramid gives 21, and qp × r gives 41 × 9 = 369 (> 91 × 4 = 364).",
                "solution_steps": [
                    "Compute 4-row pyramid: 1 + 3(2) + 3(3) + 5 = 21.",
                    "Arrange digits 1 < 4 < 9 as qp × r = 41 × 9 = 369.",
                    "Select 21 and 369."
                ]
            },
            {
                "question": "Which summary takeaway best captures why Algebra Play is central to Chapter 13?",
                "options": [
                    "Variables turn hidden number tricks, birthdays, pyramids, calendar grids, digit optimality, divisibility rules, and word puzzles into clear equations and formal proofs",
                    "Algebra only works for guessing birthdays",
                    "Place value ignores 10a + b when reversing digits",
                    "Trial-and-error guessing is always stronger than algebraic equations"
                ],
                "answer": 0,
                "hint": "Match the Chapter 13 Summary: algebraic modeling, problem-solving & formal proof!",
                "explanation": "Algebra turns patterns, puzzles, and word problems into unified general models and proofs.",
                "solution_steps": [
                    "Review Section 6.1–6.6 scope: tricks, pyramids, grids, largest product, divisibility & word problems.",
                    "Recognize variable equations solve AND prove rules universally.",
                    "Select Option 1."
                ]
            }
        ]
    }
]

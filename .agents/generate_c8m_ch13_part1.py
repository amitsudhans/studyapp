#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 13: Algebra Play
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 13 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Variable Algebra Modeling",
        "subtitle": "Section 6.1 Algebra Play: Using Letter Variables to Analyze, Solve & Decode Mathematical Patterns",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Thirteen: Algebra Play! Throughout earlier arithmetic classes, you often tested one specific concrete number at a time—like checking 3 + 5 = 8 or 10 × 4 = 40! Here in Section Six Point One, Algebra transforms you cleanly from a passive arithmetic calculator into an insightful, analytical mathematical codebreaker who uncovers the exact hidden machinery operating behind every puzzle rule! "
            "Instead of locking onto one fixed number, replace unknown or changing quantities with crisp LETTER VARIABLES such as x, y, a, M, or D! Why are letter variables so astonishingly powerful? Because a single algebraic expression captures EVERY possible number simultaneously inside one compact universal blueprint! "
            "Watch what happens when someone performs a mysterious parlor trick, constructs a tall number pyramid, reads monthly calendar patterns, arranges digits for maximum products, or discovers hidden divisibility laws for multiples of 9, 11, 37, and 1001! Arithmetic guesses examples one by one and still wonders 'Does this ALWAYS work without any exceptions?' ALGEBRA models the entire machine cleanly using letter expressions, simplifies hidden steps automatically, solves puzzles systematically, and delivers rock-solid mathematical proofs covering INFINITELY MANY numbers in just two crisp lines!"
        ),
        "checkpoints": [
            {
                "question": "Why does algebraic modeling with letter variables outperform testing individual arithmetic examples one by one?",
                "options": [
                    "A single variable expression represents ALL numbers simultaneously, proving whether a rule works universally",
                    "Because letters are faster to draw than digits",
                    "Because variables work only for single-digit numbers",
                    "Because arithmetic works only on Fridays"
                ],
                "answer": 0,
                "hint": "Notice how testing x = 3 and x = 10 shows examples, while using x proves the rule for EVERY number!",
                "explanation": "Letter variables model general numerical structures, turning pattern observations into universal proofs."
            },
            {
                "question": "Which algebraic expression models 'take any unknown number n, triple it, and subtract 7' cleanly?",
                "options": [
                    "3n − 7",
                    "3(n − 7)",
                    "n + 3 − 7",
                    "7 − 3n"
                ],
                "answer": 0,
                "hint": "'Triple it' translates to 3n, followed cleanly by '− 7'!",
                "explanation": "Multiplying variable n by 3 gives 3n, and subtracting 7 produces 3n − 7."
            }
        ]
    },
    {
        "id": 2,
        "title": "Mind Reading Proofs",
        "subtitle": "Section 6.2 Think of a Number: Algebraic Variable Cancellation Always Landing on Constant Output (x + 2 − x = 2)",
        "speech": (
            "Unmask the logical mystery behind classic 'Think of a Number' party tricks inside Section Six Point Two! Follow these four mysterious instructions aloud right now: Step One—think secretly of ANY whole number inside your head without telling anyone! Step Two—double your secret number! Step Three—add 4 to that doubled total! Step Four—divide everything evenly by 2, and finally subtract your exact original secret starting number! Without knowing what number you picked—whether 7, 50, or 1,947—the magician announces triumphantly: 'Your final answer is ALWAYS TWO!' "
            "How on earth did your secret number vanish completely from the final answer? Represent your unknown secret choice with letter x and trace every single step algebraically! Step One starts cleanly at x! Step Two doubles it to 2x! Step Three adds 4 cleanly, yielding 2x + 4! Step Four applies the distributive law and divides BOTH terms inside 2x + 4 evenly by 2: (2x + 4) ÷ 2 simplifies cleanly to x + 2! Finally, subtracting your original starting number x leaves (x + 2) − x! Notice +x and −x are exact additive inverses that cancel cleanly to zero—leaving exact constant 2 EVERY single time regardless of starting choice!"
        ),
        "checkpoints": [
            {
                "question": "In the classic trick: 'Think of x, double it, add 10, divide by 2, then subtract x', what algebraic expression proves why the constant 5 ALWAYS results?",
                "options": [
                    "(2x + 10)/2 − x = (x + 5) − x = 5",
                    "2(x + 10) − x = x + 20",
                    "(2x + 10) − x = x + 10",
                    "x/2 + 5 − x = 5"
                ],
                "answer": 0,
                "hint": "Track (2x + 10) divided evenly by 2 first before subtracting x!",
                "explanation": "Dividing 2x + 10 by 2 yields x + 5; subtracting x cancels x cleanly, guaranteeing constant 5."
            },
            {
                "question": "What happens in 'Think of n, add 3, multiply by 4, subtract 12, divide by 4'?",
                "options": [
                    "You always recover your exact original starting number n!   ((4n + 12 − 12)/4 = n)",
                    "You always get constant 12",
                    "You always get 4n",
                    "You always get 0"
                ],
                "answer": 0,
                "hint": "Expand 4(n + 3) = 4n + 12, subtract 12 → 4n, then divide by 4!",
                "explanation": "Adding 3 then multiplying by 4 yields 4n + 12; subtracting 12 leaves 4n, and dividing by 4 returns original n."
            }
        ]
    },
    {
        "id": 3,
        "title": "Birthday Date Trick",
        "subtitle": "Section 6.2 Date & Birthday Prediction: 100M + 165 + D Isolating Month M and Day D cleanly",
        "speech": (
            "Now level up to predicting an entire secret calendar birthday—BOTH Month (M, from 1 to 12) AND Day (D, from 1 to 31)—in ONE single multi-step trick from Section Six Point Two! Instruct someone silently to execute these steps starting with their birth Month number M: First multiply M by 5! Second, add 6! Third, multiply that new sum by 4! Fourth, add 9! Fifth, multiply everything by 5! Sixth, add their exact birth Day number D! "
            "Suppose someone born on October 24 (M = 10, D = 24) reports the grand final output 1,189! Subtract 165 mentally in one quick second: 1,189 − 165 = 1,024! Split off the last two digits: 24 gives the exact Day, and leading 10 gives October! "
            "Why does subtracting 165 ALWAYS work without fail? Expand every operation step by step algebraically! ((5M + 6) × 4 + 9) × 5 + D = (20M + 24 + 9) × 5 + D = (20M + 33) × 5 + D = 100M + 165 + D! Multiplying Month M by 100 pushes M safely into the hundreds column, isolating two-digit Day D cleanly in the tens and units columns!"
        ),
        "checkpoints": [
            {
                "question": "Following the birthday algorithm resulting in 100M + 165 + D, a student announces final number 779. Subtract 165 to decode their Month M and Day D:",
                "options": [
                    "June 14   (779 − 165 = 614 → Month 6, Day 14)",
                    "July 19   (719)",
                    "May 14   (514)",
                    "June 24   (624)"
                ],
                "answer": 0,
                "hint": "Compute 779 − 165 first, then read the last two digits as Day D and leading digit(s) as Month M!",
                "explanation": "779 − 165 = 614; 100(6) + 14 decodes cleanly to Month 6 (June), Day 14."
            },
            {
                "question": "In the expression 100M + 165 + D, why does subtracting 165 cleanly separate Month M from Day D?",
                "options": [
                    "Because 100M shifts M left by two place-value columns, keeping every two-digit day D (01–31) strictly in the last two digits",
                    "Because 165 equals total days in 6 months",
                    "Because D is always multiplied by 100",
                    "Because M + D always equals 165"
                ],
                "answer": 0,
                "hint": "Think what multiplying any number M by 100 does to its decimal digits when 1 ≤ D ≤ 31!",
                "explanation": "100M leaves 00 in the ones and tens places, so adding D ≤ 31 preserves M in the hundreds/thousands and D in the last two digits."
            }
        ]
    },
    {
        "id": 4,
        "title": "Number Pyramid Sums",
        "subtitle": "Section 6.3 Number Pyramids: Bottom-Up Addition Rule & Expanding 3-Row / 4-Row Algebraic Weights",
        "speech": (
            "Enter Section Six Point Three: NUMBER PYRAMIDS! Imagine stacking rectangular number bricks neatly into tiered rows so EVERY brick above rests squarely on two bricks directly below it! Follow ONE clean summation rule: every cell value equals the exact SUM of the two cells touching directly beneath it! "
            "Test a simple 3-row pyramid numerically first: place 4, 7, and 2 across the bottom base! Middle row builds 4 + 7 = 11 on the left and 7 + 2 = 9 on the right! Top peak sums 11 + 9 = 20! "
            "Now unlock the hidden algebraic power using variables a, b, and c along the bottom row! Middle row becomes (a + b) on the left and (b + c) on the right! Add them carefully to reveal the top peak: (a + b) + (b + c) = a + 2b + c! Look at middle brick b's coefficient: 2! Because central brick b feeds into BOTH middle bricks simultaneously, b gets counted TWICE! Expand onward to a 4-row pyramid with bottom base a, b, c, d: algebra reveals top peak a + 3b + 3c + d—mirroring symmetric Pascal weights 1, 3, 3, 1!"
        ),
        "checkpoints": [
            {
                "question": "In a 3-row addition pyramid with bottom base numbers a, b, c (left to right), what exact algebraic expression gives the TOP brick?",
                "options": [
                    "a + 2b + c",
                    "a + b + c",
                    "2a + b + 2c",
                    "a × b × c"
                ],
                "answer": 0,
                "hint": "Middle row is (a + b) and (b + c); add those two middle expressions together!",
                "explanation": "(a + b) + (b + c) = a + 2b + c — middle base brick b contributes twice."
            },
            {
                "question": "Using the 4-row pyramid peak formula (a + 3b + 3c + d), what is the top brick value when the bottom base row holds 2, 5, 1, 4?",
                "options": [
                    "24   (2 + 3×5 + 3×1 + 4 = 2 + 15 + 3 + 4)",
                    "12   (2 + 5 + 1 + 4)",
                    "20",
                    "32"
                ],
                "answer": 0,
                "hint": "Substitute a = 2, b = 5, c = 1, d = 4 directly into a + 3b + 3c + d!",
                "explanation": "2 + 3(5) + 3(1) + 4 = 2 + 15 + 3 + 4 = 24."
            }
        ]
    },
    {
        "id": 5,
        "title": "Solving Missing Pyramids",
        "subtitle": "Section 6.3 Algebraic Solvers: Linear Equations Solving Missing Internal Cells & Base Unknowns",
        "speech": (
            "What happens when a number pyramid hides bricks right inside the bottom or middle layers instead of nicely handing you the complete bottom row? Never guess blindly by slow, tedious trial and error—instead set up clean LINEAR EQUATIONS inside Section Six Point Three to solve directly! "
            "Solve a classic missing-cell 3-row puzzle right now! Suppose bottom-left is 5, bottom-middle is unknown x, and bottom-right is 9, while the very TOP peak equals 34! Plug directly into our 3-row algebraic law a + 2b + c = Top Peak! Substitute a = 5, b = x, c = 9, and Top = 34 cleanly: 5 + 2x + 9 = 34 → combine constants: 2x + 14 = 34 → subtract 14 from both sides: 2x = 20 → divide by 2 → bottom-middle x = 10 instantly! Fill back upward to verify: middle bricks 5 + 10 = 15 and 10 + 9 = 19, summing cleanly to 15 + 19 = 34! "
            "Even trickier puzzles—where one middle brick, one base corner, and the top peak are given—backtrack cleanly step by step using subtraction and one variable letter until every single hidden cell locks right into place!"
        ),
        "checkpoints": [
            {
                "question": "A 3-row addition pyramid has bottom bricks 6, x, 8 and Top brick equal to 30. Using a + 2b + c = Top, find missing center brick x:",
                "options": [
                    "x = 8",
                    "x = 16",
                    "x = 7",
                    "x = 10"
                ],
                "answer": 0,
                "hint": "Solve 6 + 2x + 8 = 30 → 2x + 14 = 30!",
                "explanation": "2x + 14 = 30 gives 2x = 16, so center base brick x = 8."
            },
            {
                "question": "In a 3-row pyramid, top peak is 45, left middle brick is 21, and bottom-left brick is 9. Find the bottom-right brick c:",
                "options": [
                    "12   (right middle = 45 − 21 = 24; center base = 21 − 9 = 12 → c = 24 − 12 = 12)",
                    "15",
                    "9",
                    "24"
                ],
                "answer": 0,
                "hint": "Work down one step at a time: right middle = 45 − 21 = 24, and center base = 21 − 9 = 12!",
                "explanation": "Center base = 21 − 9 = 12; right middle = 45 − 21 = 24; hence bottom-right c = 24 − 12 = 12."
            }
        ]
    },
    {
        "id": 6,
        "title": "Virahanka Fibonacci Pyramids",
        "subtitle": "Section 6.3 Virahāṅka-Fibonacci Connections: Sequence Terms (1, 2, 3, 5, 8...) Forming Pyramid Base Rows",
        "speech": (
            "Discover an enchanting mathematical link uniting number pyramids with India's ancient Virahāṅka-Fibonacci sequence (1, 2, 3, 5, 8, 13, 21, 34, ...) inside Section Six Point Three! Centuries before Fibonacci wrote in Europe, Indian prosody scholar Virahāṅka analyzed poetic meter rhythms and described these exact numbers where each new term equals the exact sum of the two immediately previous terms! "
            "Watch the dazzling magic unfold whenever you place consecutive Virahāṅka-Fibonacci numbers along the BOTTOM ROW of an addition pyramid! Start a 3-row pyramid with bottom base 1, 2, 3! Middle row builds 1 + 2 = 3 and 2 + 3 = 5—the VERY NEXT TWO sequence terms! Top peak sums 3 + 5 = 8—the NEXT Virahāṅka-Fibonacci term! Notice why: pairwise pyramid addition MIRRORS the Virahāṅka recurrence step for step! "
            "Now build a 4-row pyramid starting with base 1, 2, 3, 5: Row 2 generates 3, 5, 8; Row 3 generates 8, 13; Top Peak reaches 21! Notice why our algebraic formula matches cleanly too: 1 + 3(2) + 3(3) + 5 = 21! In general, along an n-row pyramid built upon consecutive terms, EVERY upward layer shifts forward smoothly along the sequence—revealing deep algebraic harmony!"
        ),
        "checkpoints": [
            {
                "question": "Place consecutive Virahāṅka-Fibonacci terms 2, 3, 5 along the bottom row of a 3-row addition pyramid. What exact number crowns the TOP brick?",
                "options": [
                    "13   (middle row 5, 8 → top 5 + 8 = 13, next Virahāṅka term!)",
                    "10",
                    "8",
                    "21"
                ],
                "answer": 0,
                "hint": "Compute 2 + 3 = 5 and 3 + 5 = 8 on row 2, then add row 2!",
                "explanation": "Since 2, 3, 5 satisfy the Virahāṅka rule, middle row gives 5, 8 and top reaches 13."
            },
            {
                "question": "In a 4-row addition pyramid built on bottom base 1, 2, 3, 5 (consecutive Virahāṅka-Fibonacci numbers), what appears at the very TOP brick?",
                "options": [
                    "21   (Row 2: 3, 5, 8 → Row 3: 8, 13 → Top: 21)",
                    "13",
                    "34",
                    "11"
                ],
                "answer": 0,
                "hint": "Check a + 3b + 3c + d = 1 + 3(2) + 3(3) + 5 = 1 + 6 + 9 + 5!",
                "explanation": "1 + 6 + 9 + 5 = 21, advancing smoothly to the 7th Virahāṅka-Fibonacci term."
            }
        ]
    },
    {
        "id": 7,
        "title": "Calendar Grid Magic",
        "subtitle": "Section 6.4 Fun with Grids: Monthly 2×2 Calendar Blocks (a, a+1, a+7, a+8) & Linear Equation 4a + 16 = S",
        "speech": (
            "Pull down any standard monthly wall calendar for Section Six Point Four: Fun with Grids! Draw ANY compact 2 by 2 square box enclosing four neighboring dates inside a month! Ask a classmate to tell you ONLY the total sum S of all four dates hidden inside their secret box—and amaze them by naming ALL FOUR exact calendar dates in under two seconds flat! "
            "Decode the secret effortlessly using one single letter variable a for the top-left corner date! Moving one box right advances by +1 day, giving top-right date (a + 1)! Moving one full week straight down in the same column adds +7 days, giving bottom-left (a + 7) and bottom-right (a + 8)! Sum all four corner dates algebraically right now: a + (a + 1) + (a + 7) + (a + 8) = 4a + 16! "
            "Given ANY valid sum S, isolate top-left date a cleanly in two quick inverse steps: subtract 16, then divide by 4 (a = (S − 16) ÷ 4)! Notice also why opposite diagonal pairs match identically: a + (a + 8) = 2a + 8 EQUALS (a + 1) + (a + 7) = 2a + 8!"
        ),
        "checkpoints": [
            {
                "question": "The sum S of four dates inside a 2 × 2 calendar box is S = 52. Using 4a + 16 = S, what are the four exact dates inside that box?",
                "options": [
                    "9, 10, 16, 17   (since 4a = 36 → a = 9)",
                    "8, 9, 15, 16",
                    "10, 11, 17, 18",
                    "13, 14, 20, 21"
                ],
                "answer": 0,
                "hint": "Solve 4a + 16 = 52 → 4a = 36 → a = 9, then add +1, +7, +8!",
                "explanation": "a = (52 − 16) ÷ 4 = 9, giving box dates 9, 10 (top) and 16, 17 (bottom)."
            },
            {
                "question": "Why must every valid 2 × 2 monthly calendar block ALWAYS produce a total sum S that leaves remainder 0 when divided by 4?",
                "options": [
                    "Because S = 4a + 16 = 4(a + 4) is ALWAYS a multiple of 4 for any integer date a",
                    "Because every month has 28 days",
                    "Because adding 7 and 8 makes an odd sum",
                    "Only in leap years"
                ],
                "answer": 0,
                "hint": "Factor 4 cleanly out of 4a + 16!",
                "explanation": "4a + 16 = 4(a + 4) guarantees S is always evenly divisible by 4 (so S = 50 cannot be a valid 2 × 2 calendar sum!)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Picture Shape Grids",
        "subtitle": "Section 6.4 Algebra Grids: Solving Picture-Symbol Row & Column Equations for Unknown Shapes",
        "speech": (
            "Now inspect playful picture-symbol puzzles called ALGEBRA GRIDS inside Section Six Point Four! Imagine a square 3 by 3 grid filled neatly with geometric icons—such as Circles, Triangles, and Squares—instead of plain digits! Alongside every horizontal row and beneath every vertical column sits the exact numerical sum of the three shapes inside that row or column! Your mathematical detective mission: uncover the secret number value hidden behind EACH geometric shape! "
            "Treat every icon cleanly as an algebraic letter variable! Spot the easiest starting line first—scan the totals carefully to locate a row or column holding THREE IDENTICAL SHAPES! Suppose Row One displays three Triangles totaling 24! Write the crisp equation 3△ = 24 → divide evenly by 3 → Triangle = 8 instantly! "
            "Now substitute △ = 8 cleanly into Row Two: suppose Row Two displays Triangle + Square + Square = 20! That equation turns directly into 8 + 2□ = 20 → subtract 8 from both sides to obtain 2□ = 12 → divide by 2 → Square = 6! Finally plug those two known values cleanly into any column containing Circle to unlock the third unknown shape cleanly by subtraction, verifying every remaining row and column total simultaneously!"
        ),
        "checkpoints": [
            {
                "question": "In an Algebra Grid, Row 1 contains [Circle, Circle, Circle] = 27. Column 1 contains [Circle, Square, Square] = 21. Find the exact values of Circle and Square:",
                "options": [
                    "Circle = 9; Square = 6",
                    "Circle = 9; Square = 12",
                    "Circle = 7; Square = 7",
                    "Circle = 8; Square = 6.5"
                ],
                "answer": 0,
                "hint": "First divide 27 ÷ 3 for Circle, then solve 9 + 2×Square = 21!",
                "explanation": "3○ = 27 → ○ = 9. Then 9 + 2□ = 21 → 2□ = 12 → □ = 6."
            },
            {
                "question": "If Triangle = 7 and Star = 11 in an Algebra Grid, what total sum belongs at the end of a row showing [Triangle, Star, Star]?",
                "options": [
                    "29   (7 + 11 + 11)",
                    "25   (7 + 7 + 11)",
                    "18",
                    "33"
                ],
                "answer": 0,
                "hint": "Add one Triangle plus two Stars: 7 + 11 + 11!",
                "explanation": "7 + 11 + 11 = 29."
            }
        ]
    }
]

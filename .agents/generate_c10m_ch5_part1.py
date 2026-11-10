#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 5: Arithmetic Progressions
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (Subba Rao, Ramkali, John, Raghav, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Patterns Around Us",
        "subtitle": "Spotting Number Sequences in Nature, Savings, Ladder Rungs, Unit Squares & Rabbit Populations",
        "speech": (
            "Welcome, curious Class Ten mathematicians, to Chapter Five on Arithmetic Progressions! Open your eyes wide and spot numerical patterns marching quietly all around nature and everyday human routines! "
            "Observe four contrasting sequences side by side. First, an office starter salary of 8,000 rupees climbs steadily by a fixed annual raise of 500 rupees, forming 8,000, 8,500, 9,000, and 9,500. "
            "Second, a wooden ladder whose bottom rung spans 45 centimeters shrinks evenly by 2 centimeters every step upward, giving 45, 43, 41, all the way down to 25 centimeters at the top. "
            "Third, consider unit squares tiling larger square grids, producing 1, 4, 9, 16, and 25. Fourth, look at bank compound interest balances or famous branching rabbit population models called the Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13! "
            "Pause and compare all four patterns carefully. While unit squares grow by changing odd jumps and Fibonacci adds the previous two terms together, salary increments, piggy bank savings, and ladder rungs follow one remarkably clean rule. "
            "Every succeeding term arrives simply by adding a fixed constant number to its immediately preceding term! This constant step growth rule launches our entire exciting journey into arithmetic progressions, nth terms, and sums!"
        ),
        "checkpoints": [
            {
                "question": "Which everyday sequence below adds (or subtracts) a FIXED constant number at every single step?",
                "options": [
                    "Ladder rung lengths shrinking smoothly by 2 cm each rung: 45, 43, 41, 39, ...",
                    "Rabbit population (Fibonacci): 1, 1, 2, 3, 5, 8, 13, ...",
                    "Unit square area counts: 1, 4, 9, 16, 25, ...",
                    "Compound interest doubling balances yearly: 100, 200, 400, 800"
                ],
                "answer": 0,
                "hint": "Check consecutive differences between neighboring numbers to see which stays constant!",
                "explanation": "43 − 45 = −2, 41 − 43 = −2, 39 − 41 = −2 (constant step), whereas Fibonacci, squares, and doubling vary in consecutive differences."
            },
            {
                "question": "A young saver starts putting ₹100 in a piggy bank in Month 1 and adds ₹50 MORE than the previous month each new month (₹100, ₹150, ₹200...). What fixed number separates consecutive deposits?",
                "options": [
                    "+₹50",
                    "+₹100",
                    "×1.5",
                    "−₹50"
                ],
                "answer": 0,
                "hint": "Subtract ₹100 from ₹150 and ₹150 from ₹200!",
                "explanation": "150 − 100 = 50 and 200 − 150 = 50, showing constant addition +₹50."
            }
        ]
    },
    {
        "id": 2,
        "title": "Common Difference d",
        "subtitle": "Defining Arithmetic Progressions, General Form a, a+d, a+2d... & Finite vs Infinite APs",
        "speech": (
            "Now lock down the crisp formal definition from Section Five Point Two! An Arithmetic Progression, abbreviated as AP, is a list of numbers in which each term is obtained by adding a fixed number d "
            "to its immediately preceding term, except for the very first term a! That fixed step d wears the title common difference. Look closely: can the common difference d only be a positive number? Never fall for that common myth! "
            "Common difference d can comfortably be positive, like 1, 2, 3, 4 where d equals plus 1; negative, like 100, 70, 40, 10 where d equals minus 30; or even zero, like 3, 3, 3, 3 where d equals zero! "
            "Writing the general form algebraically gives first term a, second term a plus d, third term a plus 2 d, fourth term a plus 3 d, and onward! Furthermore, if an AP stops cleanly at a clear last term, like 11 wooden ladder rungs, it is called a finite AP. "
            "However, if dots trail endlessly onward forever without a final term, it is called an infinite AP! Always verify any candidate sequence carefully by checking whether each term minus its preceding term stays strictly identical across every single consecutive pair!"
        ),
        "checkpoints": [
            {
                "question": "Check whether the sequence 3, 3, 3, 3, ... is an Arithmetic Progression, and state its first term a and common difference d:",
                "options": [
                    "Yes! It is a valid AP with a = 3 and d = 0",
                    "No—common difference d can never equal zero",
                    "Yes, with a = 3 and d = 3",
                    "No—finite terms only can have d = 0"
                ],
                "answer": 0,
                "hint": "Common difference d is allowed to be positive, negative, or zero!",
                "explanation": "Every consecutive difference 3 − 3 = 0 remains strictly constant, so 3, 3, 3, ... is a valid AP with a = 3, d = 0."
            },
            {
                "question": "Verify whether the sequence −1.2, −3.2, −5.2, −7.2, ... (Exercise 5.1) forms an AP, and identify d:",
                "options": [
                    "Yes, forms an AP with d = −2.0 (next term −9.2)",
                    "Yes, forms an AP with d = +2.0",
                    "No—negative decimals never form APs",
                    "Yes, forms an AP with d = −1.2"
                ],
                "answer": 0,
                "hint": "Carefully subtract a₁ from a₂: (−3.2) − (−1.2) = −3.2 + 1.2!",
                "explanation": "−3.2 − (−1.2) = −2, −5.2 − (−3.2) = −2, −7.2 − (−5.2) = −2; constant d = −2 confirms an AP."
            }
        ]
    },
    {
        "id": 3,
        "title": "Testing Real Situations",
        "subtitle": "Exercise 5.1 Verification: Taxi Fares, Well Digging, Air Pump Cylinders & Compound Growth",
        "speech": (
            "Test your detective instincts right across all four real-world stories inside Exercise Five Point One, Question One! Can every gradual cost or volume change produce an Arithmetic Progression? Watch closely! "
            "Scenario One: A city taxi fare charges 15 rupees for the first kilometer and adds 8 rupees for each additional kilometer. List consecutive bills: 15, 23, 31, and 39 rupees. The step stays constant at plus 8, so yes, it forms an AP! "
            "Scenario Two: Digging a village well costs 150 rupees for the very first meter and rises by 50 rupees per deeper meter. List cumulative bills: 150, 200, 250, and 300 rupees. That constant difference of plus 50 confirms an AP! "
            "Scenario Three is a classic trap! A vacuum pump removes one-fourth of the air remaining inside a glass cylinder at each stroke. Starting with volume V leaves three-fourths V after stroke one, and nine-sixteenths V after stroke two. "
            "Subtracting consecutive terms shows the first drop is minus one-fourth V, while the second drop shrinks to minus three-sixteenths V. Since the step shrinks, it is not an AP! Scenario Four: 10,000 rupees at 8 percent compound interest multiplies by 1.08 yearly, so also not an AP!"
        ),
        "checkpoints": [
            {
                "question": "Why does removing 1/4 of the remaining air inside a cylinder on each pump stroke NOT form an Arithmetic Progression (Ex 5.1 Q1 ii)?",
                "options": [
                    "Each stroke removes 1/4 of a smaller remaining volume (−V/4, then −3V/16, then −9V/64), so consecutive differences are NOT constant",
                    "Because air volume increases after pumping",
                    "Because fractions can never appear inside any AP",
                    "Because only 3 strokes are allowed"
                ],
                "answer": 0,
                "hint": "Compare a₂ − a₁ = −V/4 against a₃ − a₂ = −3V/16!",
                "explanation": "Multiplicative scaling by (3/4) shrinks the absolute amount removed every stroke, making consecutive differences unequal (geometric progression, not AP)."
            },
            {
                "question": "Which situation from Exercise 5.1 DOES form a true Arithmetic Progression?",
                "options": [
                    "Cost of digging a well: ₹150 for first meter + ₹50 extra per additional meter (150, 200, 250, 300...)",
                    "Bank account growing at 8% per annum compound interest",
                    "Vacuum pump extracting 1/4 remaining air repeatedly",
                    "Square areas 1², 2², 3², 4²"
                ],
                "answer": 0,
                "hint": "Look for constant additive increments at every step!",
                "explanation": "Each additional meter adds an identical +₹50 constant difference, forming AP 150, 200, 250, 300... cleanly."
            }
        ]
    },
    {
        "id": 4,
        "title": "General nth Term",
        "subtitle": "Deriving Formula aₙ = a + (n − 1)d and Finding Specific Terms (30th, 11th, etc.)",
        "speech": (
            "Suppose a sequence starts at 2 with constant step 5, giving 2, 7, 12, 17, 22, and someone demands the 30th or 100th term instantly without writing 99 additions by hand! Look closely at the counting pattern built by "
            "adding d repeatedly starting from first term a. Term 1 equals a plus zero steps of d. Term 2 equals a plus one step of d. Term 3 equals a plus two steps of d. Notice the exact offset every single time: "
            "to reach Term Number n, how many forward jumps of common difference d do you take starting from Term 1? Always one less than n, meaning precisely n minus 1 steps! That insight gives our golden nth Term Formula: a sub n equals a plus n minus 1 times d! "
            "Test it immediately on Exercise Five Point Two to find the 30th term of the AP 10, 7, 4, and so on! Identify first term a equals 10 and common difference d equals 7 minus 10 equals minus 3. "
            "Plug n equals 30 cleanly into the formula: Term 30 equals 10 plus 30 minus 1 times minus 3, which is 10 plus 29 times minus 3, giving 10 minus 87 equals minus 77 with instant precision!"
        ),
        "checkpoints": [
            {
                "question": "In the nth term formula aₙ = a + (n − 1)d, why is common difference d multiplied by (n − 1) rather than n?",
                "options": [
                    "Because a₁ = a already sits at step 0, so reaching the nth term requires strictly (n − 1) forward steps of size d",
                    "Because first term a is always zero",
                    "Because every AP ends at n − 1 terms",
                    "Because d is subtracted on the first term"
                ],
                "answer": 0,
                "hint": "Count gaps between n terms placed in a line: 2 terms have 1 gap, 3 terms have 2 gaps, n terms have...",
                "explanation": "Counting from Term 1 (0·d) to Term 2 (1·d) to Term n uses exactly (n − 1) common-difference additions."
            },
            {
                "question": "Find the 11th term of the AP: −3, −1/2, 2, ... (Exercise 5.2 Q2 ii):",
                "options": [
                    "22",
                    "28",
                    "−38",
                    "−48.5"
                ],
                "answer": 0,
                "hint": "Compute d = (−1/2) − (−3) = +2.5 (= 5/2), then find a₁₁ = −3 + 10 × (5/2)!",
                "explanation": "d = 5/2; a₁₁ = −3 + (11 − 1)(5/2) = −3 + 25 = 22."
            }
        ]
    },
    {
        "id": 5,
        "title": "Term Position Check",
        "subtitle": "Finding Index n for Known Values (78 or 0) and Testing Non-Integer Membership (−150)",
        "speech": (
            "Our trusty formula a_n equals a plus (n minus 1)d also works smoothly IN REVERSE: given ANY target value inside an AP, we can solve for its exact term index n—OR prove whether a suspect number actually belongs to the AP at all! "
            "Remember one ironclad rule about term position n: term indices (1st, 2nd, 3rd, ...) MUST strictly be POSITIVE WHOLE INTEGERS (n ∈ {1, 2, 3, ...})! You can NEVER visit a 54.67th seat inside a theater! "
            "Test Two Textbook Cases! Case One (Exercise 5.2 Q4): Which term of AP 3, 8, 13, 18, ... equals 78? Plug a equals 3, d equals 5, and a_n equals 78 into formula: 78 equals 3 plus (n minus 1) times 5! Subtracting 3 gives 75 equals 5(n minus 1), "
            "so n minus 1 equals 15 -> n equals 16 (clean positive integer—78 is the 16th term)! Case Two (Exercise 5.2 Q6): Check whether minus 150 is a term of AP 11, 8, 5, 2, ...! Setting minus 150 equals 11 plus (n minus 1)(minus 3) gives minus 161 equals minus 3(n minus 1), "
            "yielding n equals 164 over 3 equals 54 and 2/3! Since n is NOT an integer, minus 150 does NOT belong anywhere in this AP!"
        ),
        "checkpoints": [
            {
                "question": "Check whether −150 is a term of the AP: 11, 8, 5, 2, ... (Exercise 5.2 Q6):",
                "options": [
                    "No—solving 11 + (n − 1)(−3) = −150 gives n = 164/3 ≈ 54.67, which is NOT a positive integer",
                    "Yes—it is the 54th term",
                    "Yes—it is the 55th term",
                    "No—solely because APs cannot contain negative numbers"
                ],
                "answer": 0,
                "hint": "Term index n must belong strictly to positive integers {1, 2, 3, ...}!",
                "explanation": "Since 164 is not divisible by 3, n = 54⅔ fails the positive-integer requirement, proving −150 never occurs in this sequence."
            },
            {
                "question": "Which term of the decreasing AP: 21, 18, 15, ... equals 0 (Textbook Example 4)?",
                "options": [
                    "8th term",
                    "7th term",
                    "9th term",
                    "0 does not appear"
                ],
                "answer": 0,
                "hint": "Set 21 + (n − 1)(−3) = 0 -> 3(n − 1) = 21!",
                "explanation": "21 − 3(n − 1) = 0 ⟹ n − 1 = 7 ⟹ n = 8 (8th term = 0)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Terms From End",
        "subtitle": "Finding kth Term From the End of a Finite AP by Reversing Progression Order",
        "speech": (
            "Watch this super sleek shortcut for solving Textbook Example Eight and Exercise Five Point Two Question Seventeen: Find the 11th term FROM THE LAST TERM (towards the first term) of finite AP: 10, 7, 4, ..., minus 62! "
            "Notice TWO distinct clean ways to solve this! Method One (Traditional): First solve minus 62 equals 10 plus (n minus 1)(minus 3) to discover total length n equals 25 terms, then figure out that 11th from the end equals (25 minus 11 plus 1) equals 15th term from the start! "
            "Careful—students often forget that '+1' in (25 − 11 + 1) and accidentally grab the 14th term instead! Now discover Method Two—a gorgeous mistake-proof trick! Simply FLIP THE FINITE AP BACKWARDS! Starting right at last term minus 62 and walking backwards towards 10 reverses the common difference "
            "sign automatically from d equals minus 3 into NEW common difference minus d equals PLUS 3! Now simply ask for the ordinary 11th term from the front of the reversed AP (a_new equals minus 62, d_new equals +3): "
            "minus 62 plus (11 minus 1) times 3 equals minus 62 plus 30 equals minus 32! Clean, direct, and zero index mistakes!"
        ),
        "checkpoints": [
            {
                "question": "Using the reversal shortcut (new first term = l, new step = −d) on finite AP 3, 8, 13, ..., 253 (Ex 5.2 Q17), find the 20th term FROM THE LAST TERM:",
                "options": [
                    "158  [compute 253 + (20 − 1)(−5) = 253 − 95]",
                    "163",
                    "103",
                    "98"
                ],
                "answer": 0,
                "hint": "Forward d = +5, so moving backwards from l = 253 uses step −5!",
                "explanation": "Reversing starts at 253 with difference −5: 20th term from end = 253 + 19(−5) = 253 − 95 = 158."
            },
            {
                "question": "If a finite AP has 25 terms total, which forward position matches the 11th term from the last term?",
                "options": [
                    "15th term  (via 25 − 11 + 1)",
                    "14th term",
                    "16th term",
                    "11th term"
                ],
                "answer": 0,
                "hint": "Count inclusively: 1st from end = 25th; 2nd from end = 24th; 11th from end = ?",
                "explanation": "Inclusive counting from the end gives position n − k + 1 = 25 − 11 + 1 = 15th term."
            }
        ]
    },
    {
        "id": 7,
        "title": "Two Term Systems",
        "subtitle": "Determining a & d From Linear Term Relations and Salary/Savings Word Models (Ex 5.2)",
        "speech": (
            "Whenever an Arithmetic Progression hides both its first term a and its common difference d, how do two clues unlock the entire progression? Think straight back to Chapter Three and its Elimination Method! Because every term formula a sub n equals a plus n minus 1 times d is simply linear in a and d, "
            "any two given terms build two simultaneous linear equations, and subtracting one from the other always cancels first term a immediately! Test Textbook Example Five: Determine the AP whose 3rd term is 5 and 7th term is 9. Write a plus 2 d equals 5 and a plus 6 d equals 9. "
            "Subtract Equation One from Equation Two to get 4 d equals 4, giving common difference d equals 1 and first term a equals 3, forming 3, 4, 5, 6, 7! "
            "Next check Exercise Five Point Two salary and savings applications. Suppose a new office worker begins work in 1995 at 5,000 rupees yearly salary and receives a fixed 200 rupee raise each year. When does income reach 7,000 rupees? "
            "Solve 7,000 equals 5,000 plus n minus 1 times 200 to find the 11th year, 2005! Likewise, saving 5 rupees in Week 1 and adding 1.75 rupees weekly reaches 20.75 rupees cleanly in Week 10!"
        ),
        "checkpoints": [
            {
                "question": "If the 17th term of an AP exceeds its 10th term by 7 (Exercise 5.2 Q10), find its common difference d immediately:",
                "options": [
                    "d = 1  (since a₁₇ − a₁₀ = 7d = 7)",
                    "d = 7",
                    "d = 10",
                    "Cannot be determined without knowing a"
                ],
                "answer": 0,
                "hint": "Compute (a + 16d) − (a + 9d) = 7d cleanly!",
                "explanation": "a cancels out immediately: 16d − 9d = 7d = 7 ⟹ d = 1 regardless of a!"
            },
            {
                "question": "An employee starts at ₹5,000/yr and receives ₹200 annual raise (Ex 5.2 Q19). In which nth year of service does annual salary reach ₹7,000?",
                "options": [
                    "11th year",
                    "10th year",
                    "12th year",
                    "20th year"
                ],
                "answer": 0,
                "hint": "Solve 5000 + (n − 1)(200) = 7000 -> (n − 1) = 2000 ÷ 200 = 10!",
                "explanation": "(n − 1) = 10 gives n = 11th year (1995 + 10 = year 2005)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Gauss Summation Trick",
        "subtitle": "Carl Friedrich Gauss's Pairing Symmetry for Adding Consecutive Numbers Instantly",
        "speech": (
            "Now enter Section Five Point Four on the Sum of First n Terms of an AP, starting with one of mathematics most delightful childhood classroom stories! Around age ten, young schoolboy Carl Friedrich Gauss sat inside an arithmetic class when his teacher "
            "asked pupils to add every whole integer smoothly from 1 all the way up to 100: 1 plus 2 plus 3 all the way up to 100! Expecting quiet pencil work for half an hour, the teacher gasped in total amazement when young Gauss raised his slate mere seconds later carrying "
            "the exact correct total 5,050! How did young Gauss compute that massive sum faster than anyone else in the room? Look closely at the pure symmetry he spotted: write Sum S forward from 1 up to 100, and write the exact same Sum S directly underneath backwards from 100 down to 1! "
            "Now add vertically column by column! First column: 1 plus 100 equals 101! Second column: 2 plus 99 equals 101! Every single column across all 100 pairs equals the exact same constant 101! Thus twice S equals 100 times 101. Dividing both sides by 2 yields "
            "50 times 101 equals 5,050, giving birth directly to our general AP Sum Formula!"
        ),
        "checkpoints": [
            {
                "question": "In Carl Friedrich Gauss's pairing method for S = 1 + 2 + ... + 100, what did adding forward and reversed lists column-by-column produce?",
                "options": [
                    "100 identical column sums each equal to 101, so 2S = 100 × 101 ⟹ S = 5,050",
                    "50 different uneven remainders",
                    "100 columns each summing to 100",
                    "2S = 100 + 101"
                ],
                "answer": 0,
                "hint": "1 + 100 = 101, 2 + 99 = 101, ..., 100 + 1 = 101!",
                "explanation": "Reversing S pairs smallest with largest so every column sums identically to (a + l) = 101, giving n(a + l)/2 = 50 × 101 = 5,050."
            },
            {
                "question": "Using Gauss's general natural-number sum formula Sₙ = n(n + 1)/2, what is the sum of the first 50 positive integers?",
                "options": [
                    "1,275",
                    "2,550",
                    "1,250",
                    "2,500"
                ],
                "answer": 0,
                "hint": "Compute (50 × 51) ÷ 2 = 25 × 51 cleanly!",
                "explanation": "25 × 51 = 25 × 50 + 25 = 1,250 + 25 = 1,275."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch5 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

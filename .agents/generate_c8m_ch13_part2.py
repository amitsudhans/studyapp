#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 13: Algebra Play
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 13 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Largest Digit Product",
        "subtitle": "Section 6.5 The Largest Product: Maximizing (□□ × □) Using Three Distinct Digits p < q < r",
        "speech": (
            "Enter an exciting optimization puzzle in Section Six Point Five: THE LARGEST PRODUCT! Suppose you hold three distinct non-zero digit tiles—ordered strictly p < q < r, such as digits 2, 5, and 8! You must slot all three tiles once each into a two-digit by one-digit multiplication box template: (□□ × □)! Which arrangement produces the LARGEST POSSIBLE PRODUCT? "
            "Test digits 2, 5, and 8 systematically right now! Most students immediately guess by quick instinct: 'Make the two-digit number as huge as possible—put 85 × 2!' Compute 85 × 2 = 170! Next, try putting the middle digit 5 or largest digit 8 outside as the single-digit multiplier instead! Try 82 × 5 = 410—already more than double 170! Now try placing largest digit 8 OUTSIDE and arranging remaining digits 5 and 2 in descending order INSIDE: 52 × 8! Compute 52 × 8 = 416! Look closely at the complete scoreboard: 52 × 8 (416) beats 82 × 5 (410) and crushes 85 × 2 (170)! Try digits 3, 6, 9 too: 63 × 9 = 567 beats 93 × 6 = 558! Why does qp × r ALWAYS beat every rival like rq × p?"
        ),
        "checkpoints": [
            {
                "question": "Given digits 3, 7, and 9 placed into the 2-digit × 1-digit template (□□ × □), which arrangement produces the STRICT MAXIMUM product?",
                "options": [
                    "73 × 9 = 657",
                    "97 × 3 = 291",
                    "93 × 7 = 651",
                    "37 × 9 = 333"
                ],
                "answer": 0,
                "hint": "Put largest digit r = 9 in the single-digit box, and put remaining 7, 3 descending inside (73)!",
                "explanation": "73 × 9 = 657 beats 93 × 7 = 651 and 97 × 3 = 291."
            },
            {
                "question": "When placing digits p < q < r into (□□ × □), which digit ALWAYS belongs inside the TENS place vs the UNITS place of the 2-digit factor once largest digit r sits outside?",
                "options": [
                    "Put q (larger remaining) in the TENS place and p (smallest) in the UNITS place: qp × r",
                    "Put p in the TENS place and q in the UNITS place: pq × r",
                    "Put r in the UNITS place",
                    "Order of digits inside □□ never changes the product"
                ],
                "answer": 0,
                "hint": "Compare 10q + p vs 10p + q when q > p!",
                "explanation": "Since q > p, 10q + p > 10p + q, so multiplying by r achieves maximum with qp × r."
            }
        ]
    },
    {
        "id": 10,
        "title": "Expanded Place Proof",
        "subtitle": "Section 6.5 Algebraic Proof: Comparing 10qr + pr vs 10rq + pq to Prove qp × r Always Wins",
        "speech": (
            "Earlier we SAW 52 × 8 = 416 beat 82 × 5 = 410—now PROVE with rock-solid algebra why qp × r ALWAYS defeats EVERY competitor for ALL distinct digits p < q < r! "
            "Recall place value carefully: a two-digit number 'ab' stands for 10a + b, NEVER a × b! Now compare the two sharpest contenders cleanly: Candidate One places largest digit r outside as qp × r, expanding cleanly to (10q + p) × r = 10qr + pr! Candidate Two places middle digit q outside as rp × q, expanding cleanly to (10r + p) × q = 10rq + pq! Similarly, placing p outside gives rq × p = 10rp + qp, which loses heavily in its hundreds term because r > q > p! Look closely at Candidate One versus Candidate Two! Notice BOTH expressions share the IDENTICAL hundreds-place term 10qr (= 10rq)! Cancel 10qr off both sides to compare what remains: pr versus pq! "
            "Since r is STRICTLY GREATER than q (r > q) and digit p is positive, pr is GUARANTEED strictly greater than pq (by exact difference p(r − q) > 0)! That proves why 52 × 8 beats 82 × 5 by exactly 2 × (8 − 5) = 6!"
        ),
        "checkpoints": [
            {
                "question": "Compare the expanded algebraic products of qp × r (= 10qr + pr) and rp × q (= 10rq + pq) where p < q < r. What exact difference separates them?",
                "options": [
                    "qp × r exceeds rp × q by EXACTLY p(r − q) > 0",
                    "rp × q is always larger by 10qr",
                    "Both products are always identical",
                    "qp × r exceeds rp × q by 10(r − q)"
                ],
                "answer": 0,
                "hint": "Cancel identical term 10qr = 10rq and subtract pq from pr!",
                "explanation": "(10qr + pr) − (10rq + pq) = pr − pq = p(r − q) > 0 since p > 0 and r > q."
            },
            {
                "question": "Using your difference formula p(r − q), by how much does 64 × 9 beat 94 × 6 WITHOUT multiplying both completely out?",
                "options": [
                    "12   (p = 4, r = 9, q = 6 → 4 × (9 − 6) = 12)",
                    "3",
                    "30",
                    "18"
                ],
                "answer": 0,
                "hint": "Identify p = 4, q = 6, r = 9 in p(r − q)!",
                "explanation": "4 × (9 − 6) = 4 × 3 = 12 (check: 64×9 = 576 and 94×6 = 564; 576 − 564 = 12!)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Two Digit Reversals",
        "subtitle": "Section 6.6 Reversed Two-Digit Tricks: Algebraic Proofs of ba − ab = 9(b − a) & ab + ba = 11(a + b)",
        "speech": (
            "Enter Section Six Point Six: DECODING DIVISIBILITY TRICKS! Watch how elementary place-value algebra exposes centuries-old numerical magic tricks instantly! Start with ANY two-digit number 'ab' having tens digit a and units digit b—written cleanly in expanded base-ten form as 10a + b! Next, reverse its two digits cleanly to build 'ba', written in expanded place-value form as 10b + a! "
            "Trick One: REVERSE AND SUBTRACT! Pick 72, reverse to 27, subtract: 72 − 27 = 45 (an exact multiple of 9)! Pick 38, reverse to 83, subtract: 83 − 38 = 45 (also an exact multiple of 9)! Prove why this holds permanently: subtract (10b + a) − (10a + b) = (10b − b) − (10a − a) = 9b − 9a = 9(b − a)! Every reversed two-digit difference is GUARANTEED divisible by 9, with quotient equal to the exact digit difference! "
            "Trick Two: REVERSE AND ADD! Add (10a + b) + (10b + a) cleanly side by side: collect like terms carefully to reach 11a + 11b = 11(a + b)! Therefore, every reversed two-digit sum is ALWAYS an exact multiple of 11, with exact quotient equal to digit sum a + b!"
        ),
        "checkpoints": [
            {
                "question": "A secret two-digit number 'ab' (a > b) has its digits reversed to form 'ba'. Dividing the positive difference (ab − ba) by 9 gives 5. What must (a − b) equal?",
                "options": [
                    "a − b = 5",
                    "a − b = 9",
                    "a + b = 5",
                    "a − b = 45"
                ],
                "answer": 0,
                "hint": "Recall ab − ba = 9(a − b)!",
                "explanation": "Since ab − ba = 9(a − b), dividing by 9 directly leaves exact digit difference a − b = 5."
            },
            {
                "question": "If you add a two-digit number 'ab' and its reverse 'ba' together and obtain 143, what is the sum of its digits (a + b)?",
                "options": [
                    "13   (since 11(a + b) = 143 → 143 ÷ 11 = 13)",
                    "11",
                    "9",
                    "15"
                ],
                "answer": 0,
                "hint": "Use ab + ba = 11(a + b) and divide 143 by 11!",
                "explanation": "11(a + b) = 143 → a + b = 143 ÷ 11 = 13 (e.g., 58 + 85 = 143)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Cyclic Six Digit",
        "subtitle": "Section 6.6 Cyclic 3-Digit & 6-Digit Proofs: 111(a+b+c) = 37×3(a+b+c) & abcabc = 1001×abc = 7×11×13×abc",
        "speech": (
            "Amaze friends with two jaw-dropping divisibility tricks for larger multi-digit numbers decoded inside Section Six Point Six! "
            "Trick One: THREE-DIGIT CYCLIC SUMS! Choose ANY three-digit number 'abc' (such as 254), cycle its digits forward cleanly to form 'bca' (542) and 'cab' (425), and add all three numbers: 254 + 542 + 425 = 1,221! Divide 1,221 by 37—it divides EVENLY to exact 33 with ZERO remainder! Why does 37 always work?! Write all three cyclic numbers in expanded place value: (100a + 10b + c) + (100b + 10c + a) + (100c + 10a + b)! Notice each digit appears ONCE in hundreds, tens, and ones → 111a + 111b + 111c = 111(a + b + c)! Since 111 factors cleanly as 37 × 3, the cyclic sum ALWAYS equals 37 × 3(a + b + c)—guaranteed divisible by BOTH 3 and 37! "
            "Trick Two: SIX-DIGIT REPEATS! Write ANY 3-digit number twice in a row—like 382,382! Notice abcabc expands cleanly into thousands plus units as 1000 × abc + abc = 1001 × abc! Since 1001 factors cleanly into primes 7 × 11 × 13, ANY repeated six-digit abcabc divides cleanly by 7, 11, AND 13!"
        ),
        "checkpoints": [
            {
                "question": "Take any 3-digit number 'abc' and compute the cyclic sum S = abc + bca + cab. Which numbers are ALWAYS guaranteed divisors of S?",
                "options": [
                    "111, 37, and 3   (since S = 111(a + b + c) = 37 × 3(a + b + c))",
                    "7 and 13",
                    "10 and 100",
                    "2 and 5"
                ],
                "answer": 0,
                "hint": "Factor 111 = 37 × 3 out of 111(a + b + c)!",
                "explanation": "Cyclic shifts place each digit in 100s, 10s, and 1s once → 111(a + b + c) = 37 × 3 × (a + b + c)."
            },
            {
                "question": "A mysterious six-digit number formed by repeating 3 digits twice is 479,479. Without long division, which factor triplet is GUARANTEED to divide 479,479 evenly?",
                "options": [
                    "7, 11, and 13   (since 479,479 = 1001 × 479 and 1001 = 7 × 11 × 13)",
                    "37, 9, and 5",
                    "2, 4, and 8",
                    "17, 19, and 23"
                ],
                "answer": 0,
                "hint": "Factor abcabc = 1001 × abc and remember 1001 = 7 × 11 × 13!",
                "explanation": "479479 = 1001 × 479 = 7 × 11 × 13 × 479, dividing cleanly by 7, 11, and 13."
            }
        ]
    },
    {
        "id": 13,
        "title": "Shrine Flower Puzzle",
        "subtitle": "Section 6.6 Double-and-Deduct Puzzles: Shrine Flower Offerings & Traveler-and-Genie Coin-Doubling",
        "speech": (
            "Now put algebraic linear equations to work solving classical 'double-and-deduct' puzzles from Section Six Point Six! Puzzle One: SHRINE FLOWER OFFERINGS! Suppose a pilgrim visits three sacred shrines carrying x fresh flowers in a basket! Before entering EACH shrine, a magical temple pond DOUBLES all remaining flowers (×2), and inside the shrine the pilgrim offers exact number f flowers (say f = 8), finishing with ZERO flowers right after exiting the third shrine! "
            "Model it cleanly using algebra or reverse backtracking! Starting with x before Shrine 1 leaves (2x − 8) after Shrine 1! Before and after Shrine 2 leaves 2(2x − 8) − 8 = 4x − 24! Before and after Shrine 3 leaves 2(4x − 24) − 8 = 8x − 56 = 0 → solve 8x = 56 → x = 7 flowers! Check forward smoothly step by step: 7 → 14 − 8 = 6 → 12 − 8 = 4 → 8 − 8 = 0! "
            "Notice the identical algebraic structure inside the famous TRAVELER AND THE GENIE COIN-DOUBLING PUZZLE: a genie repeatedly doubles coins inside a traveler's pouch in exchange for a fixed fee paid back—solved effortlessly by backtracking from zero or solving one linear equation!"
        ),
        "checkpoints": [
            {
                "question": "In the 3-shrine puzzle, a pond doubles flowers before each shrine and 16 flowers are offered inside each shrine, leaving 0 flowers after Shrine 3. Solve 8x − 112 = 0 (or backtrack) for starting flowers x:",
                "options": [
                    "14 flowers   (8x − 112 = 0)",
                    "16 flowers",
                    "12 flowers",
                    "8 flowers"
                ],
                "answer": 0,
                "hint": "Work backward from 0: after Shrine 3 add 16 (16), halve (8), add 16 (24), halve (12), add 16 (28), halve!",
                "explanation": "Forward equation: 2(2(2x − 16) − 16) − 16 = 8x − 112 = 0, which gives x = 112 / 8 = 14 flowers."
            },
            {
                "question": "A genie doubles a traveler's coins and charges 16 coins fee at the end of EACH of 2 magic rounds, leaving 0 coins after Round 2. How many coins did the traveler start with?",
                "options": [
                    "12 coins   (4x − 48 = 0)",
                    "16 coins",
                    "8 coins",
                    "10 coins"
                ],
                "answer": 0,
                "hint": "Set up 2(2x − 16) − 16 = 0 and solve 4x − 48 = 0!",
                "explanation": "Round 1 leaves (2x − 16); Round 2 leaves 2(2x − 16) − 16 = 4x − 48 = 0, so x = 12 coins."
            }
        ]
    },
    {
        "id": 14,
        "title": "Legs Ages Equations",
        "subtitle": "Section 6.6 Word Problems: Horse-and-Hen Head/Leg Counts, Mother-Daughter Ages & Cowherd Counts",
        "speech": (
            "Master three famous linear equation word puzzles from Section Six Point Six! Puzzle One: HORSE AND HEN BARNYARD COUNTS! Suppose a farmyard encloses horses (4 legs each) and hens (2 legs each), totaling 20 heads and 56 legs! Let x equal number of horses—so number of hens equals (20 − x)! Equate total legs immediately: 4x + 2(20 − x) = 56! Expand cleanly: 4x + 40 − 2x = 56 → 2x = 16 → x = 8 horses and 12 hens (verify: 32 + 24 = 56 legs)! "
            "Puzzle Two: MOTHER-DAUGHTER AGE RATIOS! Today a mother is 4 times as old as her daughter (daughter = x, mother = 4x)! In 6 years, she will be ONLY 3 times as old! Equate ages 6 years ahead cleanly: 4x + 6 = 3(x + 6) = 3x + 18 → subtract 3x and 6 → x = 12 years (daughter 12, mother 48; in 6 years, 18 and 54 = 3 × 18)! "
            "Puzzle Three: ANCIENT COWHERD FRACTION COUNTS! Setting total herd size = x converts one-half grazing nearby, one-quarter drinking water by the river, plus remaining grazing cows cleanly into one single-variable linear equation!"
        ),
        "checkpoints": [
            {
                "question": "A stable encloses horses (4 legs) and hens (2 legs). Counting 15 total heads and 42 total legs, how many horses are inside?",
                "options": [
                    "6 horses   (and 9 hens: 24 + 18 = 42 legs)",
                    "9 horses",
                    "8 horses",
                    "5 horses"
                ],
                "answer": 0,
                "hint": "Set 4x + 2(15 − x) = 42 and simplify 2x + 30 = 42!",
                "explanation": "2x + 30 = 42 gives 2x = 12 → x = 6 horses (leaving 15 − 6 = 9 hens)."
            },
            {
                "question": "Today a mother is 5 times her daughter's age. After 8 years, the mother will be 3 times her daughter's age. Find their present ages:",
                "options": [
                    "Daughter 8 years, Mother 40 years   (check: in 8 yrs → 16 and 48)",
                    "Daughter 6 years, Mother 30 years",
                    "Daughter 10 years, Mother 50 years",
                    "Daughter 4 years, Mother 20 years"
                ],
                "answer": 0,
                "hint": "Solve 5x + 8 = 3(x + 8) = 3x + 24!",
                "explanation": "5x + 8 = 3x + 24 → 2x = 16 → daughter x = 8, mother = 40."
            }
        ]
    },
    {
        "id": 15,
        "title": "Dosa Cart Series",
        "subtitle": "Section 6.6 Business & Series Equations: Dosa Cart Break-Even Points & Nested Fraction Sum Series",
        "speech": (
            "Finish Section Six Point Six's real-world toolkit with business break-even algebra and clever nested fraction series! Puzzle One: THE DOSA CART BREAK-EVEN PROFIT POINT! Suppose a street dosa cart invests ₹600 daily for fixed cart rent and stove fuel, plus ₹15 ingredient cost per dosa, while selling each crisp dosa for ₹35! How many dosas n must be sold to reach BREAK-EVEN—the exact sales count where total revenue covers total cost with zero loss? "
            "Write BOTH algebraic expressions cleanly using variable n! Total Cost = 600 + 15n! Total Revenue = 35n! Set Revenue equal to Cost: 35n = 600 + 15n! Subtract 15n from both sides cleanly: 20n = 600 → divide by 20 → n = 30 dosas! Every single dosa sold BEYOND 30 generates ₹20 pure profit! "
            "Puzzle Two: NESTED FRACTION SUM SERIES! What happens when an unknown total x equals x/2 + x/4 + x/8 + 12 (such as splitting treasure or herds in shrinking halves)? Combine all fractional coefficients cleanly using common denominator 8: (4 + 2 + 1)x/8 + 12 = (7/8)x + 12 = x → remaining 1/8 x = 12 → multiply by 8 to find x = 96 effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "A snack stall spends ₹450 fixed daily setup cost plus ₹10 per plate, selling plates for ₹25 each. How many plates must sell to break even (Revenue = Cost)?",
                "options": [
                    "30 plates",
                    "18 plates",
                    "45 plates",
                    "25 plates"
                ],
                "answer": 0,
                "hint": "Solve 25n = 450 + 10n → subtract 10n from both sides!",
                "explanation": "Profit margin per plate = 25 − 10 = ₹15; 450 ÷ 15 = 30 plates to break even."
            },
            {
                "question": "A traveler divides a bag of x mangoes: half go to travelers, a quarter to guards, an eighth to temple priests, and 5 remain left over. Solve x/2 + x/4 + x/8 + 5 = x:",
                "options": [
                    "40 mangoes",
                    "32 mangoes",
                    "48 mangoes",
                    "20 mangoes"
                ],
                "answer": 0,
                "hint": "Notice 1/2 + 1/4 + 1/8 = 7/8 of x, leaving 1/8 of x equal to 5!",
                "explanation": "x − (7/8)x = (1/8)x = 5 → x = 5 × 8 = 40 mangoes."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Algebra Summary",
        "subtitle": "Summary Consolidation: Algebra as Indispensable Tool for Modeling, Problem-Solving & Formal Proof",
        "speech": (
            "Step back cleanly to appreciate the grand architecture of Chapter Thirteen: Algebra Play! Across six rich playgrounds, letter variables proved themselves an indispensable tool for mathematical MODELING, SYSTEMATIC PROBLEM-SOLVING, and FORMAL PROOF! "
            "First, NUMBER AND BIRTHDAY TRICKS: expanding linear steps proves instant variable cancellation (x + 2 − x = 2) and shows how 100M + 165 + D isolates Month M and Day D cleanly! "
            "Second, PYRAMIDS AND GRIDS: bottom-up addition generates symmetric polynomial weights (a + 2b + c and a + 3b + 3c + d), connects to Virahāṅka-Fibonacci sequences (1, 2, 3, 5, 8...), decodes 2 × 2 calendar magic (4a + 16 = S), and solves picture-shape grids! "
            "Third, DIGIT OPTIMIZATION: place-value expansion 10qr + pr > 10rq + pq formally proves why qp × r maximizes digit products for p < q < r! "
            "Fourth, DIVISIBILITY AND WORD PUZZLES: ba − ab = 9(b − a), ab + ba = 11(a + b), cyclic 111(a + b + c) = 37 × 3(a + b + c), abcabc = 7 × 11 × 13 × abc, shrine flowers, horse-hen legs, age ratios, dosa break-even, and fraction series all yield seamlessly to algebra!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement accurately collects four key algebraic proofs from Chapter 13?",
                "options": [
                    "3-row pyramid top = a+2b+c; 2×2 calendar S = 4a+16; reversed diff ba−ab = 9(b−a); cyclic sum = 37×3(a+b+c)",
                    "3-row pyramid top = a+b+c; calendar S = 4a+8; reversed diff = 11(b−a)",
                    "Max digit product for p<q<r is rq × p; cyclic sum = 1001(a+b+c)",
                    "Birthday trick isolates Month using 10M + D"
                ],
                "answer": 0,
                "hint": "Verify every algebraic identity carefully against Sections 6.3–6.6!",
                "explanation": "Option 1 matches every core algebraic identity proved across Chapter 13."
            },
            {
                "question": "What transforms a clever arithmetic parlor trick or puzzle into a permanent mathematical theorem?",
                "options": [
                    "Replacing specific digits with variables and simplifying algebraically to prove the property holds for ALL valid inputs",
                    "Testing three lucky single-digit numbers",
                    "Hiding the numbers inside a calendar",
                    "Dividing every equation by zero"
                ],
                "answer": 0,
                "hint": "Examples illustrate; variable algebra proves universally!",
                "explanation": "Algebraic modeling generalizes across arbitrary inputs, yielding airtight deductive proofs."
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 7: The Mathematics of Maybe: Introduction to Probability
Slides Data Generator - Part 3 (Slides 17 to 20 - Silent Mastery Quizzes, 40 Questions Total)
Strictly 1-3 word titles, zero spoken audio, zero human names, hints + 3-step solutions.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Foundations Scale Quiz",
        "subtitle": "Sections 7.1–7.1.2 Practice Set (10 Questions): Randomness, Certainty vs Impossibility, 0–1 Probability Scale & 6-Card Deck",
        "questions": [
            {
                "question": "Which statement accurately describes a mathematical RANDOM EXPERIMENT?",
                "options": [
                    "All possible outcomes are known beforehand, yet the exact result of a single trial cannot be predicted in advance",
                    "Possible outcomes are completely unknown even after repeating the test",
                    "Every repetition must produce the exact same number",
                    "Results can be calculated deterministically with a ruler"
                ],
                "answer": 0,
                "hint": "Recall tossing a coin or rolling a die: S is known, next single outcome is uncertain!",
                "explanation": "A random experiment has a known pool of possible outcomes while single-trial outcomes stay unpredictable.",
                "solution_steps": [
                    "Identify whether the possible outcomes can be listed beforehand (e.g., {H, T} or {1..6}).",
                    "Check whether individual single-trial outcomes remain uncertain despite repeatable conditions.",
                    "Conclude that known sample pool + unpredictable individual outcome defines a random experiment."
                ]
            },
            {
                "question": "Why do atmospheric weather systems produce mathematically random rainfall events?",
                "options": [
                    "Tiny variations across complex physical factors (air pressure, temperature, wind, moisture) cascade unpredictably",
                    "Rain gauges intentionally choose random numbers",
                    "Physics equations fail inside Earth's atmosphere",
                    "Clouds hold only impossible outcomes"
                ],
                "answer": 0,
                "hint": "Check Section 7.1.1: weather involves vast coupled physical variables!",
                "explanation": "Rainfall depends sensitively on countless interacting atmospheric variables, creating genuine forecast uncertainty.",
                "solution_steps": [
                    "Identify atmospheric inputs: pressure gradients, humidity, air currents, and surface heating.",
                    "Recognize extreme sensitivity where tiny unobserved shifts alter storm paths rapidly.",
                    "Conclude rainfall carries genuine uncertainty modeled via objective probability."
                ]
            },
            {
                "question": "In the 6-card model containing 4 purple cards and 2 green cards, what is the probability of drawing a PURPLE card on one blind pick?",
                "options": ["2/3 (4/6)", "1/3 (2/6)", "1/2", "4/2"],
                "answer": 0,
                "hint": "Divide favourable purple cards (4) by total cards (6) and simplify!",
                "explanation": "P(purple) = 4/6 = 2/3.",
                "solution_steps": [
                    "Count favourable purple cards = 4.",
                    "Count total equally likely cards = 4 + 2 = 6.",
                    "Compute ratio and simplify: 4/6 = 2/3."
                ]
            },
            {
                "question": "If the 6-card deck contains 3 purple cards and 3 green cards, where does P(purple) sit on the probability scale?",
                "options": ["Exactly 0.5 (Even chance)", "0 (Impossible)", "1 (Certain)", "0.25"],
                "answer": 0,
                "hint": "Equal counts (3 out of 6) sit right in the middle of [0, 1]!",
                "explanation": "P(purple) = 3/6 = 0.5, representing an exact 50-50 even chance.",
                "solution_steps": [
                    "Count 3 purple cards out of 6 total cards.",
                    "Divide: P(purple) = 3 / 6 = 1 / 2 = 0.5.",
                    "Locate 0.5 at the exact midpoint of [0, 1], marking an even chance."
                ]
            },
            {
                "question": "What numerical value represents an IMPOSSIBLE event on the probability scale, such as picking Tuesday directly after Wednesday?",
                "options": ["0", "0.5", "1", "−1"],
                "answer": 0,
                "hint": "Impossibility always sits at the left boundary of 0 ≤ P(E) ≤ 1!",
                "explanation": "Impossible events never occur across any trial, giving P = 0.",
                "solution_steps": [
                    "Recognize Tuesday can never follow Wednesday directly.",
                    "Count favourable outcomes = 0.",
                    "Apply probability scale lower boundary: P(impossible) = 0."
                ]
            },
            {
                "question": "What numerical value represents a CERTAIN event on the probability scale, such as getting an integer from 1 to 6 on a standard die?",
                "options": ["1", "0", "0.5", "100"],
                "answer": 0,
                "hint": "On the standard probability scale (not percentage scale), certainty equals 1!",
                "explanation": "Guaranteed events occur on every single trial, holding probability P = 1.",
                "solution_steps": [
                    "Check all 6 faces of a standard die lie in {1, 2, 3, 4, 5, 6}.",
                    "Divide favourable (6) by total (6).",
                    "Conclude guaranteed occurrence gives probability P = 6/6 = 1."
                ]
            },
            {
                "question": "Which candidate number CANNOT possibly represent the probability of any event?",
                "options": ["−0.15", "0.001", "0.999", "0"],
                "answer": 0,
                "hint": "Check whether the value violates 0 ≤ P(E) ≤ 1!",
                "explanation": "Probability can never be negative or exceed 1; −0.15 is invalid.",
                "solution_steps": [
                    "State fundamental bounds: 0 ≤ P(E) ≤ 1 for all events E.",
                    "Test each candidate: 0.001, 0.999, and 0 satisfy 0 ≤ p ≤ 1.",
                    "Reject −0.15 because probabilities can never be negative."
                ]
            },
            {
                "question": "A card deck holds 6 purple cards and 0 green cards. Compare drawing a purple card vs drawing a green card.",
                "options": [
                    "Purple is Certain (P = 1); Green is Impossible (P = 0)",
                    "Both have P = 0.5",
                    "Purple has P = 6; Green has P = 0",
                    "Purple has P = 5/6; Green has P = 1/6"
                ],
                "answer": 0,
                "hint": "6/6 = 1 and 0/6 = 0!",
                "explanation": "All 6 cards are purple ⇒ P(purple) = 1 (certain) and P(green) = 0 (impossible).",
                "solution_steps": [
                    "Calculate P(purple) = 6 / 6 = 1 (Certain event).",
                    "Calculate P(green) = 0 / 6 = 0 (Impossible event).",
                    "Confirm P(purple) + P(green) = 1 + 0 = 1."
                ]
            },
            {
                "question": "Arrange these likelihood fractions from LEAST likely to MOST likely: A = 1/5, B = 0.05, C = 3/4, D = 0.5.",
                "options": [
                    "B (0.05) < A (0.20) < D (0.50) < C (0.75)",
                    "A < B < C < D",
                    "D < B < A < C",
                    "B < D < A < C"
                ],
                "answer": 0,
                "hint": "Convert fractions cleanly into decimals: 1/5 = 0.20 and 3/4 = 0.75!",
                "explanation": "0.05 < 0.20 < 0.50 < 0.75 orders the events cleanly from unlikely to very likely.",
                "solution_steps": [
                    "Convert all probabilities into decimals: A = 0.20, B = 0.05, C = 0.75, D = 0.50.",
                    "Sort ascending from 0 toward 1: 0.05 < 0.20 < 0.50 < 0.75.",
                    "Map back to labels: B < A < D < C."
                ]
            },
            {
                "question": "What happens to the sum of probabilities of 'rain occurring' and 'rain NOT occurring' tomorrow?",
                "options": [
                    "It always equals exactly 1",
                    "It equals 0",
                    "It equals 0.5",
                    "It depends on temperature"
                ],
                "answer": 0,
                "hint": "One of the two mutually exclusive outcomes must happen!",
                "explanation": "An event and its opposite cover 100% of possibilities, summing strictly to 1.",
                "solution_steps": [
                    "Notice 'rain' (E) and 'no rain' (not E) cover every possible day outcome cleanly.",
                    "Recall P(E) + P(not E) = 1.",
                    "Conclude their combined probability always equals 1."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Empirical Theoretical Quiz",
        "subtitle": "Sections 7.2–7.2.3 Practice Set (10 Questions): Experimental Trials, Jñān-Chaupad, 'PROBABILITY', Sampling & Gambler's Fallacy",
        "questions": [
            {
                "question": "In 120 tosses of an irregular bottle cap, it landed open-up 72 times. What is the experimental probability of landing open-up?",
                "options": ["0.6 (3/5)", "0.4 (2/5)", "0.5", "0.72"],
                "answer": 0,
                "hint": "Divide observed occurrences (72) by total trials (120)!",
                "explanation": "Experimental P = 72 / 120 = 3 / 5 = 0.6.",
                "solution_steps": [
                    "Identify observed occurrences = 72 and total trials = 120.",
                    "Apply relative frequency formula: P(open-up) = 72 / 120.",
                    "Divide top and bottom by 24: 3/5 = 0.6."
                ]
            },
            {
                "question": "Why is Jñān-Chaupad highlighted in the history of probability?",
                "options": [
                    "It is the ancient Indian board game combining dice/cowrie chance throws with moral ladders and snakes, predating Snakes and Ladders",
                    "It invented continuous calculus",
                    "It banned all dice games worldwide",
                    "It proved √2 is irrational"
                ],
                "answer": 0,
                "hint": "Section 7.2.1 connects modern dice board games back to India's Jñān-Chaupad!",
                "explanation": "Jñān-Chaupad used chance rolls to teach ethics, serving as the historical ancestor of Snakes and Ladders.",
                "solution_steps": [
                    "Recall historical note in Section 7.2.1 on Snakes and Ladders.",
                    "Identify ancient Indian origin Jñān-Chaupad ('Board of Knowledge').",
                    "Connect cowrie/dice experimental rolls to upward ladders and downward snakes."
                ]
            },
            {
                "question": "One letter card is picked blindly from the 11 letters of 'P R O B A B I L I T Y'. What is P(picking letter B or letter I)?",
                "options": ["4/11", "2/11", "3/11", "1/11"],
                "answer": 0,
                "hint": "Count 'B' (appears twice) + 'I' (appears twice) out of 11 total letters!",
                "explanation": "There are 2 B's and 2 I's ⇒ 4 favourable cards out of 11 ⇒ 4/11.",
                "solution_steps": [
                    "Count total letter cards in P-R-O-B-A-B-I-L-I-T-Y: n(S) = 11.",
                    "Count favourable cards: B appears 2 times and I appears 2 times (total = 4).",
                    "Divide equally likely outcomes: 4 / 11."
                ]
            },
            {
                "question": "What is the theoretical probability of rolling a number LESS THAN 5 on a single fair 6-sided die?",
                "options": ["2/3 (4/6)", "1/2 (3/6)", "5/6", "1/3"],
                "answer": 0,
                "hint": "'Less than 5' includes {1, 2, 3, 4}, NOT 5 itself!",
                "explanation": "Four outcomes {1, 2, 3, 4} out of 6 give 4/6 = 2/3.",
                "solution_steps": [
                    "List die outcomes strictly less than 5: E = {1, 2, 3, 4} (count = 4).",
                    "Identify total equally likely outcomes n(S) = 6.",
                    "Compute and simplify: P = 4/6 = 2/3."
                ]
            },
            {
                "question": "A spinner has 4 regions labeled A, B, C, D with central angles 180°, 60°, 60°, 60°. What is the true theoretical probability of landing on A?",
                "options": ["1/2", "1/4", "1/3", "180"],
                "answer": 0,
                "hint": "Compare A's sector angle (180°) against full circle 360°—don't treat unequal regions as 1/4 each!",
                "explanation": "Sectors are unequally likely; A covers 180°/360° = 1/2 of the wheel.",
                "solution_steps": [
                    "Notice the 4 regions have unequal central angles, so 1/4 is INVALID.",
                    "Use proportional angular fraction: angle(A) / 360° = 180° / 360°.",
                    "Simplify: 180° / 360° = 1/2."
                ]
            },
            {
                "question": "A school cafeteria surveys a representative sample of 50 students and finds 18 prefer bananas. Estimate total banana servings needed for all 1,500 students.",
                "options": ["540 bananas", "360 bananas", "180 bananas", "720 bananas"],
                "answer": 0,
                "hint": "Multiply experimental proportion (18/50) by population size 1,500!",
                "explanation": "(18 / 50) × 1,500 = 18 × 30 = 540 bananas.",
                "solution_steps": [
                    "Compute sample relative frequency: 18 / 50 = 0.36.",
                    "Scale to entire population of 1,500 students: 0.36 × 1,500.",
                    "Calculate: (18/50) × 1,500 = 18 × 30 = 540 bananas."
                ]
            },
            {
                "question": "A balanced coin lands Heads 8 times in a row. Why is believing 'the 9th toss has a higher chance of being Tails' called the Gambler's Fallacy?",
                "options": [
                    "Because independent random trials have no memory—the 9th toss STILL has P(Tail) = 1/2",
                    "Because the coin bends permanently toward Tails",
                    "Because 8 Heads prove the coin is certain to stay Heads",
                    "Because 1/2 turns into 8/9"
                ],
                "answer": 0,
                "hint": "Fair coins do not keep scoreboards to 'even out' short streaks!",
                "explanation": "Independent events carry zero memory of past results; P(Tail) remains 1/2 on toss 9.",
                "solution_steps": [
                    "Identify coin flips as physically independent random trials.",
                    "Recognize coins retain zero memory of earlier Heads/Tails streaks.",
                    "Conclude P(Tail on toss 9) stays identically 1/2; expecting Tails 'due' is the Gambler's Fallacy."
                ]
            },
            {
                "question": "Which phenomenon explains why flipping a fair coin 10,000 times yields relative frequency very close to 0.500, even if 10 flips gave 0.700?",
                "options": [
                    "Law of Large Numbers",
                    "Gambler's Fallacy",
                    "Baudhāyana's Theorem",
                    "Circular Segment Rule"
                ],
                "answer": 0,
                "hint": "Large sample sizes N pull empirical frequency steadily toward theoretical probability!",
                "explanation": "The Law of Large Numbers guarantees long-run relative frequencies converge near theoretical values.",
                "solution_steps": [
                    "Contrast noisy small samples (N = 10 ⇒ 0.700) vs massive trials (N = 10,000 ⇒ ~0.500).",
                    "Recall that random fluctuations cancel relatively as trial count grows large.",
                    "Identify this fundamental convergence theorem as the Law of Large Numbers."
                ]
            },
            {
                "question": "Out of the 11 letters in 'PROBABILITY', what is the theoretical probability of picking a CONSONANT?",
                "options": ["7/11", "4/11", "6/11", "5/11"],
                "answer": 0,
                "hint": "Count vowels (O, A, I, I = 4) and use complement 1 − 4/11!",
                "explanation": "Consonants are P, R, B, B, L, T, Y (7 letters) out of 11 ⇒ 7/11.",
                "solution_steps": [
                    "Count vowels in PROBABILITY: O, A, I, I (4 vowels out of 11).",
                    "Subtract from 11: 11 − 4 = 7 consonants (P, R, B, B, L, T, Y).",
                    "Divide favourable consonants by total letters: 7 / 11."
                ]
            },
            {
                "question": "When MUST experimental probability be used instead of simple theoretical counting?",
                "options": [
                    "When symmetry/equal likelihood fails—such as predicting customer preferences, biased objects, or weather frequencies",
                    "Only when tossing a perfect fair coin",
                    "Whenever sample space S has fewer than 6 items",
                    "Never—theoretical counting works for everything"
                ],
                "answer": 0,
                "hint": "Check Section 7.2: irregular shapes, human habits, and real-world data lack built-in symmetry!",
                "explanation": "Experimental data frequencies are essential whenever outcomes lack ideal physical symmetry.",
                "solution_steps": [
                    "Check prerequisite for theoretical counting: all elementary outcomes must be equally likely.",
                    "Identify real-world data (canteen taste, irregular bottle cap, rainfall) as non-symmetric.",
                    "Conclude empirical trials and relative frequency data are required."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Sample Spaces Quiz",
        "subtitle": "Sections 7.3–7.3.2 Practice Set (10 Questions): Sample Space S, n(S), Subsets E, Complements & Multi-Coin/Dice Pairs",
        "questions": [
            {
                "question": "In set notation for an experiment, what do symbols S and n(S) denote?",
                "options": [
                    "S is the set of all distinct possible outcomes (Sample Space), and n(S) is the total count of those outcomes",
                    "S is one desired outcome, and n(S) is its percentage",
                    "S is always 6, and n(S) is always 1",
                    "S is only for dice and n(S) is only for coins"
                ],
                "answer": 0,
                "hint": "Check Section 7.3.1 Sample Space definitions!",
                "explanation": "S collects all non-duplicate elementary outcomes; n(S) counts how many outcomes belong to S.",
                "solution_steps": [
                    "Define S as the complete set of all distinct non-duplicate outcomes of an experiment.",
                    "Define n(S) as the cardinality (count of elements) inside set S.",
                    "Confirm both match Section 7.3.1 notation."
                ]
            },
            {
                "question": "Two fair coins are tossed together. Which sample space S is strictly accurate?",
                "options": [
                    "S = {HH, HT, TH, TT} with n(S) = 4",
                    "S = {HH, HT, TT} with n(S) = 3",
                    "S = {H, T} with n(S) = 2",
                    "S = {2H, 2T} with n(S) = 2"
                ],
                "answer": 0,
                "hint": "First-coin Head + Second-coin Tail (HT) and Tail + Head (TH) are distinct outcomes!",
                "explanation": "There are 2 × 2 = 4 equally likely ordered outcomes: HH, HT, TH, TT.",
                "solution_steps": [
                    "List outcomes of Coin 1: {H, T} and Coin 2: {H, T}.",
                    "Distinguish HT (H then T) from TH (T then H).",
                    "Form complete set S = {HH, HT, TH, TT} with n(S) = 4."
                ]
            },
            {
                "question": "Three fair coins are tossed simultaneously. What is the sample size n(S) and P(getting all 3 Heads)?",
                "options": [
                    "n(S) = 8, P(HHH) = 1/8",
                    "n(S) = 6, P(HHH) = 1/6",
                    "n(S) = 4, P(HHH) = 1/4",
                    "n(S) = 9, P(HHH) = 1/9"
                ],
                "answer": 0,
                "hint": "Multiply choices across 3 coins: 2 × 2 × 2 = 8!",
                "explanation": "n(S) = 2³ = 8 outcomes, and {HHH} is 1 of those 8 ⇒ P(HHH) = 1/8.",
                "solution_steps": [
                    "Multiply outcome choices across 3 independent coins: n(S) = 2 × 2 × 2 = 8.",
                    "Identify favourable outcome E = {HHH}, so n(E) = 1.",
                    "Compute probability P(E) = n(E) / n(S) = 1/8."
                ]
            },
            {
                "question": "On rolling ONE fair die, let Event E = 'rolling an odd number greater than 1'. List E as a subset of S and find P(E).",
                "options": [
                    "E = {3, 5}, P(E) = 2/6 = 1/3",
                    "E = {1, 3, 5}, P(E) = 1/2",
                    "E = {2, 3, 5}, P(E) = 1/2",
                    "E = {5}, P(E) = 1/6"
                ],
                "answer": 0,
                "hint": "1 is odd, yet NOT strictly greater than 1!",
                "explanation": "Inside S = {1,2,3,4,5,6}, odd numbers > 1 are {3, 5}, giving 2/6 = 1/3.",
                "solution_steps": [
                    "Write sample space S = {1, 2, 3, 4, 5, 6} (n(S) = 6).",
                    "Select odd numbers strictly > 1: E = {3, 5} (n(E) = 2).",
                    "Divide: P(E) = 2/6 = 1/3."
                ]
            },
            {
                "question": "If Event E has probability P(E) = 5/13, what is P(complement not-E)?",
                "options": ["8/13", "5/13", "13/5", "1/13"],
                "answer": 0,
                "hint": "Apply P(not E) = 1 − P(E)!",
                "explanation": "P(not E) = 1 − 5/13 = 8/13.",
                "solution_steps": [
                    "Use complementary event identity P(E) + P(not E) = 1.",
                    "Substitute P(E) = 5/13: P(not E) = 1 − 5/13.",
                    "Compute 13/13 − 5/13 = 8/13."
                ]
            },
            {
                "question": "When rolling two standard 6-sided dice (n(S) = 36), what is the probability of rolling a DOUBLET (same number on both dice, like (3,3))?",
                "options": ["1/6 (6/36)", "1/36", "1/12", "5/36"],
                "answer": 0,
                "hint": "Count pairs (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) out of 36!",
                "explanation": "There are 6 doublets out of 36 pairs ⇒ 6/36 = 1/6.",
                "solution_steps": [
                    "Determine total ordered pairs n(S) = 6 × 6 = 36.",
                    "List doublets: {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)} ⇒ n(E) = 6.",
                    "Compute ratio: 6 / 36 = 1 / 6."
                ]
            },
            {
                "question": "When rolling two fair dice, what is the probability that the sum of the two numbers equals 9?",
                "options": ["1/9 (4/36)", "1/6 (6/36)", "1/12 (3/36)", "5/36"],
                "answer": 0,
                "hint": "List ordered pairs adding to 9: (3,6), (4,5), (5,4), (6,3)!",
                "explanation": "Four pairs sum to 9 out of 36 total outcomes ⇒ 4/36 = 1/9.",
                "solution_steps": [
                    "Enumerate all ordered pairs (a, b) with a + b = 9: (3,6), (4,5), (5,4), (6,3).",
                    "Count n(E) = 4 out of n(S) = 36.",
                    "Simplify: 4 / 36 = 1 / 9."
                ]
            },
            {
                "question": "In tossing two fair coins, what is P(getting AT MOST ONE Tail)?",
                "options": ["3/4", "1/4", "1/2", "1"],
                "answer": 0,
                "hint": "'At most 1 Tail' means 0 Tails (HH) or 1 Tail (HT, TH)—only TT (2 Tails) is excluded!",
                "explanation": "E = {HH, HT, TH} gives 3/4 (or complement 1 − P(TT) = 1 − 1/4 = 3/4).",
                "solution_steps": [
                    "Inspect sample space S = {HH, HT, TH, TT}.",
                    "Identify outcomes with 0 or 1 Tail: E = {HH, HT, TH} (count = 3).",
                    "Compute P(E) = 3/4 (matching 1 − P(TT) = 1 − 1/4)."
                ]
            },
            {
                "question": "How is any Event E mathematically defined relative to Sample Space S?",
                "options": [
                    "Any subset of the Sample Space S (E ⊆ S)",
                    "Only a single element not inside S",
                    "Always larger than S",
                    "The average of all outcomes in S"
                ],
                "answer": 0,
                "hint": "Check Section 7.3.2 Events!",
                "explanation": "Every event E is a subset of outcomes selected from sample space S, including ∅ and S.",
                "solution_steps": [
                    "Define sample space S as the universal outcome pool.",
                    "Specify a condition selecting zero, some, or all outcomes from S.",
                    "Conclude every event E is formally a subset E ⊆ S."
                ]
            },
            {
                "question": "A card is drawn randomly from a well-shuffled standard deck of 52 playing cards. What is the probability of NOT drawing an Ace?",
                "options": ["12/13 (48/52)", "1/13", "4/52", "1/4"],
                "answer": 0,
                "hint": "There are 4 Aces in 52 cards; use P(not Ace) = 1 − 4/52!",
                "explanation": "P(Ace) = 4/52 = 1/13 ⇒ P(not Ace) = 1 − 1/13 = 12/13.",
                "solution_steps": [
                    "Count 4 Aces in a 52-card deck: P(Ace) = 4/52 = 1/13.",
                    "Apply complement rule: P(not Ace) = 1 − P(Ace).",
                    "Evaluate: 1 − 1/13 = 12/13."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Trees Applications Quiz",
        "subtitle": "Section 7.4 & End-of-Chapter Practice Set (10 Questions): Tree Diagrams, Multi-Step Paths, Spinners & Geometric Drop Probabilities",
        "questions": [
            {
                "question": "Bag 1 has 1 Red and 2 Blue marbles; Bag 2 has 3 Red and 1 Blue marble. One marble is drawn from each bag. Use a tree diagram to find P(BOTH marbles are Red).",
                "options": ["1/4 (from 1/3 × 3/4 = 3/12)", "1/2", "4/7", "2/3"],
                "answer": 0,
                "hint": "Multiply P(Red in Bag 1) = 1/3 by P(Red in Bag 2) = 3/4!",
                "explanation": "Tree path Red→Red multiplies branch fractions: (1/3) × (3/4) = 3/12 = 1/4.",
                "solution_steps": [
                    "Assign Stage 1 branch weight: P(Red₁) = 1 / (1 + 2) = 1/3.",
                    "Assign Stage 2 branch weight: P(Red₂) = 3 / (3 + 1) = 3/4.",
                    "Multiply along Red→Red path: (1/3) × (3/4) = 3/12 = 1/4."
                ]
            },
            {
                "question": "Using the same two bags (Bag 1: 1R, 2B; Bag 2: 3R, 1B), what is the probability of drawing ONE Red and ONE Blue marble (in either order)?",
                "options": ["7/12 (1/12 + 6/12)", "1/4", "1/6", "5/12"],
                "answer": 0,
                "hint": "Add the two valid paths: P(Red then Blue) = (1/3)(1/4) PLUS P(Blue then Red) = (2/3)(3/4)!",
                "explanation": "Path RB = (1/3)(1/4) = 1/12; Path BR = (2/3)(3/4) = 6/12; Sum = 7/12.",
                "solution_steps": [
                    "Compute path Red→Blue: (1/3) × (1/4) = 1/12.",
                    "Compute path Blue→Red: (2/3) × (3/4) = 6/12.",
                    "Add mutually exclusive leaf paths: 1/12 + 6/12 = 7/12."
                ]
            },
            {
                "question": "Fruit Basket X holds {Apple, Banana, Pear}; Basket Y holds {Grape, Mango}. Picking 1 item from X and 1 from Y, how many branches/paths exist and what is P(Apple & Mango)?",
                "options": [
                    "6 paths total; P(Apple & Mango) = 1/6",
                    "5 paths total; P(Apple & Mango) = 1/5",
                    "6 paths total; P(Apple & Mango) = 2/6",
                    "9 paths total; P(Apple & Mango) = 1/9"
                ],
                "answer": 0,
                "hint": "Tree has 3 × 2 = 6 equally likely leaf tips!",
                "explanation": "Basket X (3) × Basket Y (2) creates 6 equal leaf outcomes; (Apple, Mango) is 1 of 6.",
                "solution_steps": [
                    "Count Stage 1 branches from Basket X = 3.",
                    "Split each into Stage 2 branches from Basket Y = 2 ⇒ 3 × 2 = 6 total paths.",
                    "Locate single leaf (Apple, Mango) ⇒ P = 1/6."
                ]
            },
            {
                "question": "A pouch holds 3 Blue pens and 2 Green pens. Two pens are drawn ONE AFTER ANOTHER WITHOUT replacement. What is P(both pens are Blue)?",
                "options": ["3/10 (3/5 × 2/4)", "9/25 (3/5 × 3/5)", "1/5", "3/20"],
                "answer": 0,
                "hint": "On the 2nd pick, only 2 Blue pens and 4 total pens remain!",
                "explanation": "Branch 1: P(Blue₁) = 3/5. Branch 2 (without replacement): P(Blue₂) = 2/4. Product = 6/20 = 3/10.",
                "solution_steps": [
                    "Stage 1 pick: 3 Blue out of 5 total ⇒ P(Blue₁) = 3/5.",
                    "Stage 2 without replacement: 2 Blue remain out of 4 pens ⇒ P(Blue₂) = 2/4 = 1/2.",
                    "Multiply path fractions: (3/5) × (1/2) = 3/10."
                ]
            },
            {
                "question": "A circular dartboard of radius 10 cm contains a tiny central bullseye circle of radius 2 cm. Assuming every dart hits randomly across the board, what is P(bullseye)?",
                "options": [
                    "1/25 (0.04, from area ratio π·2² / π·10² = 4/100)",
                    "1/5 (radius ratio 2/10)",
                    "1/10",
                    "2/25"
                ],
                "answer": 0,
                "hint": "Geometric probability divides AREAS (πr²), NOT radii!",
                "explanation": "P(bullseye) = Area(bullseye) / Area(board) = (π × 2²) / (π × 10²) = 4 / 100 = 1/25.",
                "solution_steps": [
                    "Compute bullseye circle area = π × 2² = 4π cm².",
                    "Compute whole board area = π × 10² = 100π cm².",
                    "Take geometric area ratio: 4π / 100π = 1/25 = 0.04."
                ]
            },
            {
                "question": "A square garden of side 12 m contains an L-shaped paved patio of area 36 m² and grass covering the rest. What is the probability a random raindrop inside the garden hits GRASS?",
                "options": ["3/4 (108 / 144)", "1/4 (36 / 144)", "1/3", "2/3"],
                "answer": 0,
                "hint": "Total square area = 12² = 144 m²; Grass area = 144 − 36 = 108 m²!",
                "explanation": "Grass covers 144 − 36 = 108 m² out of 144 m² ⇒ P(grass) = 108/144 = 3/4.",
                "solution_steps": [
                    "Calculate total square garden area = 12 × 12 = 144 m².",
                    "Subtract patio area to find grass area = 144 − 36 = 108 m².",
                    "Divide favourable grass area by total area: 108/144 = 3/4."
                ]
            },
            {
                "question": "A coin is flipped AND a 6-sided fair die is rolled in a 2-step tree. What is P(Head AND a number divisible by 3)?",
                "options": ["1/6 (1/2 × 2/6)", "1/3", "1/12", "5/6"],
                "answer": 0,
                "hint": "Multiples of 3 on a die are {3, 6} (2/6 = 1/3); multiply by P(Head) = 1/2!",
                "explanation": "P(Head and {3,6}) = (1/2) × (2/6) = 1/6 (2 favourable paths out of 12).",
                "solution_steps": [
                    "Find coin branch: P(Head) = 1/2.",
                    "Find die multiples of 3: {3, 6} out of 6 faces ⇒ P = 2/6 = 1/3.",
                    "Multiply independent branch probabilities: (1/2) × (1/3) = 1/6."
                ]
            },
            {
                "question": "On a circular spinner divided into sectors of 90° (Gold), 120° (Silver), and 150° (Bronze), what is P(Silver or Gold)?",
                "options": ["7/12 (210° / 360°)", "2/3", "1/2", "5/12"],
                "answer": 0,
                "hint": "Add Silver (120°) + Gold (90°) = 210° out of full 360° circle!",
                "explanation": "Combined central angle = 90° + 120° = 210° ⇒ P = 210° / 360° = 7/12.",
                "solution_steps": [
                    "Add central angles of favourable sectors: 90° (Gold) + 120° (Silver) = 210°.",
                    "Divide by total 360° circle: 210° / 360°.",
                    "Simplify by 30°: 7 / 12."
                ]
            },
            {
                "question": "Look at the probability tree rule: at every branching node, what must the sum of outgoing sister branch probabilities equal?",
                "options": ["Exactly 1", "0.5", "0", "Equal to the number of branches"],
                "answer": 0,
                "hint": "One of the sister branches must happen at that step!",
                "explanation": "Sister branches at any node partition all possibilities at that stage, so their probabilities always sum to 1.",
                "solution_steps": [
                    "Observe sister branches list every mutually exclusive choice at that stage.",
                    "One branch must occur on any trial passing that node.",
                    "Conclude outgoing branch probabilities always sum strictly to 1."
                ]
            },
            {
                "question": "A 2-step tree tracks two independent weather days where P(Rain) = 0.3 and P(Clear) = 0.7 each day. What is the probability of AT LEAST ONE Rainy day across the 2 days?",
                "options": ["0.51 (1 − 0.7 × 0.7)", "0.60 (0.3 + 0.3)", "0.09 (0.3 × 0.3)", "0.49"],
                "answer": 0,
                "hint": "Use the complement shortcut: 1 − P(Clear on BOTH days) = 1 − (0.7 × 0.7)!",
                "explanation": "Only (Clear, Clear) has 0 rainy days: P = 0.7 × 0.7 = 0.49 ⇒ P(at least 1 Rain) = 1 − 0.49 = 0.51.",
                "solution_steps": [
                    "Identify complement event: '0 rainy days' = (Clear on Day 1 AND Clear on Day 2).",
                    "Multiply along Clear→Clear branch: 0.7 × 0.7 = 0.49.",
                    "Subtract from 1: P(at least 1 Rain) = 1 − 0.49 = 0.51."
                ]
            }
        ]
    }
]

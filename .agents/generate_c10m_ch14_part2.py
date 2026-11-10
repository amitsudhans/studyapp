#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 14: Probability
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Cards Without Replacement",
        "subtitle": "Exercise 14.1 Q15: Five Diamond Cards Shuffled & Queen Put Aside (Total Shrinks From 5 to 4!)",
        "speech": (
            "Inspect Exercise Fourteen Point One Question Fifteen carefully—a brilliant mini-problem where students get tricked by a SHRINKING SAMPLE SPACE when drawing without replacement! "
            "Read every word cleanly: FIVE cards—specifically the Ten, Jack, Queen, King, and Ace of DIAMONDS—are well-shuffled face downward on a table! ONLY those five diamond cards are present (NEVER divide by 52 here!)! "
            "Part One: One card is picked up at random! What is the probability that this picked card is the QUEEN? Since there is 1 Queen among 5 cards total, P(Queen) equals ONE FIFTH (1/5)! "
            "Now read Part Two WITH LASER FOCUS: If the Queen IS drawn AND PUT ASIDE (not put back!), and a second card is picked up from what remains, find probabilities (a) that the second card is an ACE, and (b) that it is a QUEEN! "
            "Because the Queen was removed permanently aside onto the table edge, ONLY FOUR diamond cards remain inside the face-down pile: {Ten, Jack, King, Ace of Diamonds}! Therefore: (a) P(Ace) equals exact ONE FOURTH (1/4), and (b) since ZERO Queens remain anywhere in that remaining four-card pile, drawing a second Queen now is completely IMPOSSIBLE—its exact probability equals exact zero always!"
        ),
        "checkpoints": [
            {
                "question": "Five cards (10, J, Q, K, A of diamonds) are shuffled face down (Ex 14.1 Q15). If the Queen is drawn and PUT ASIDE, find probabilities that a second card drawn is (a) an Ace, (b) a Queen:",
                "options": [
                    "(a) 1 / 4,     (b) 0   (Total shrinks from 5 to 4 with no Queen left!)",
                    "(a) 1 / 5,     (b) 1 / 5",
                    "(a) 1 / 4,     (b) 1 / 4",
                    "(a) 4 / 52,     (b) 0"
                ],
                "answer": 0,
                "hint": "After removing the Queen aside, remaining deck is strictly {10, J, K, A} (count = 4)!",
                "explanation": "With Queen put aside, 4 cards remain including 1 Ace (1/4) and 0 Queens (impossible = 0)."
            },
            {
                "question": "Before the Queen is put aside in Ex 14.1 Q15, what was the probability of picking the Queen out of those 5 Diamond cards?",
                "options": [
                    "1 / 5",
                    "1 / 52",
                    "1 / 4",
                    "1 / 13"
                ],
                "answer": 0,
                "hint": "Denominator is 5 (not 52!), because ONLY those 5 Diamond cards are on the table!",
                "explanation": "1 Queen out of 5 diamond cards gives 1/5."
            }
        ]
    },
    {
        "id": 10,
        "title": "Marbles And Piggybank",
        "subtitle": "Exercise 14.1 Q8, Q9, Q10 & Q19: Urn Balls, Piggy Bank Coins (180 Coins) & Lettered Die {A,B,C,D,E,A}",
        "speech": (
            "Now conquer FOUR fast counting classics from Exercise Fourteen Point One: Urn Balls, Piggy Bank Coins, Aquarium Fish, and Lettered Dice! "
            "Check Q8 & Q9 (Ball & Marble Urns): Q8 has 3 red and 5 black balls (Total = 8): P(red) = 3/8, P(not red) = 5/8! Q9 box holds 5 red, 8 white, and 4 green marbles (Total = 17): P(red) = 5/17, P(white) = 8/17, and P(NOT green) adds 5 + 8 = THIRTEEN over 17! "
            "Next crack open Q10's Piggy Bank! It contains ONE HUNDRED 50-paise coins, FIFTY ₹1 coins, TWENTY ₹2 coins, and TEN ₹5 coins! Step One: Always sum TOTAL coins first carefully: 100 + 50 + 20 + 10 equals ONE HUNDRED EIGHTY total coins! When one coin drops out upside down randomly: P(50-paise coin) = 100/180 = 5/9, and P(will NOT be a ₹5 coin) = (180 − 10)/180 = 170/180 = 17/18! "
            "Check Q19 Lettered Die showing six printed faces {A, B, C, D, E, A}: notice letter A appears TWICE across all six total faces! So P(A) equals 2/6 equals 1/3, while P(D) equals 1/6 cleanly! Always count repeating letter faces on special dice with extreme care!"
        ),
        "checkpoints": [
            {
                "question": "A piggy bank holds 100 fifty-paise coins, 50 ₹1 coins, 20 ₹2 coins, and 10 ₹5 coins (Ex 14.1 Q10). Probability a falling coin is (i) 50p coin, (ii) NOT a ₹5 coin:",
                "options": [
                    "(i) 5 / 9,     (ii) 17 / 18",
                    "(i) 1 / 2,     (ii) 17 / 18",
                    "(i) 5 / 9,     (ii) 1 / 18",
                    "(i) 10 / 18,     (ii) 8 / 9"
                ],
                "answer": 0,
                "hint": "Total coins = 180! Simplify 100/180 = 5/9 and (180 − 10)/180 = 170/180 = 17/18!",
                "explanation": "100/180 = 5/9 for 50p; (180−10)/180 = 17/18 for not ₹5."
            },
            {
                "question": "A box holds 5 red, 8 white, and 4 green marbles (Ex 14.1 Q9). What is the probability of drawing a marble that is NOT green?",
                "options": [
                    "13 / 17",
                    "4 / 17",
                    "8 / 17",
                    "5 / 17"
                ],
                "answer": 0,
                "hint": "Total = 17; favourable 'not green' = Red (5) + White (8) = 13 (or 1 − 4/17)!",
                "explanation": "P(not green) = (5 + 8)/17 = 13/17."
            }
        ]
    },
    {
        "id": 11,
        "title": "Spinner And Defective",
        "subtitle": "Exercise 14.1 Q12 (Spinner 1–8), Q16 (144 Pens) & Q17 (20 Bulbs Without Replacement → 15/19)",
        "speech": (
            "Now inspect Industrial Quality Control & Spinning Wheels inside Exercise Fourteen Point One Questions Twelve, Sixteen, and Seventeen! "
            "Check Q12 Game of Chance: a spinning arrow stops cleanly on equally likely numbers {1, 2, 3, 4, 5, 6, 7, 8} (Total = 8)! Quickly calculate all four parts: P(points at 8) = 1/8; P(odd number {1,3,5,7}) = 4/8 = 1/2; P(greater than 2: {3..8}) = 6/8 = 3/4; and P(less than 9: all eight numbers!) = 8/8 = ONE (Sure Event)! "
            "Check Q16 Defective Pens: 12 defective pens get accidentally mixed with 132 good ones! Careful: ALWAYS add BEFORE dividing! Total pens = 132 + 12 = ONE HUNDRED FORTY FOUR (NOT 132!)! So P(good pen) = 132 / 144 = 11 / 12! "
            "Check Q17 Two-Step Defective Bulbs: A carton lot of 20 electric bulbs contains 4 defective ones (leaving 16 good working bulbs inside)! Part (i): P(defective bulb) equals 4/20 equals ONE FIFTH! Part (ii): Suppose the very first electric bulb drawn IS good and is NOT replaced back inside the carton! Remaining lot shrinks cleanly down to 19 bulbs total with 15 good ones left, so P(not defective now) equals exact 15/19!"
        ),
        "checkpoints": [
            {
                "question": "12 defective pens are accidentally mixed with 132 good ones (Ex 14.1 Q16). Find probability that one pen taken at random is GOOD:",
                "options": [
                    "11 / 12   (= 132 / 144)",
                    "12 / 132",
                    "1 / 11",
                    "11 / 13"
                ],
                "answer": 0,
                "hint": "Total pens = 132 + 12 = 144! Simplify 132 / 144 by dividing top & bottom by 12!",
                "explanation": "Total = 144 pens; Good = 132 ⟹ P(Good) = 132/144 = 11/12."
            },
            {
                "question": "A lot of 20 bulbs contains 4 defective ones. Suppose the 1st bulb drawn is NOT defective and is NOT put back (Ex 14.1 Q17 ii). Probability the next bulb drawn is NOT defective:",
                "options": [
                    "15 / 19",
                    "16 / 20",
                    "15 / 20",
                    "4 / 19"
                ],
                "answer": 0,
                "hint": "19 bulbs remain in total, and good bulbs dropped from 16 down to 15!",
                "explanation": "After removing 1 good bulb, 15 good bulbs remain out of 19 total ⟹ 15/19."
            }
        ]
    },
    {
        "id": 12,
        "title": "Box Discs Calendar",
        "subtitle": "Exercise 14.1 Q18 (90 Numbered Discs) & Board Favorite Calendar Problems (53 Sundays in Leap vs Non-Leap Year)",
        "speech": (
            "Now master Numbered Discs (Exercise Fourteen Point One Question Eighteen) and Board Exam Calendar Puzzles (53 Sundays in a Year)! "
            "Look at Q18: A box contains 90 discs numbered strictly from 1 to 90 (Total = 90)! Part (i) asks: probability of a TWO-DIGIT number! Watch carefully: single-digit numbers {1, 2, ..., 9} count NINE discs! Subtracting from 90 leaves EIGHTY ONE two-digit numbers (10 to 90), so probability equals 81/90 = 9/10! Part (ii): Perfect square numbers {1, 4, 9, 16, 25, 36, 49, 64, 81} count NINE discs = 9/90 = 1/10! Part (iii): Divisible by 5 gives 90 ÷ 5 = 18 discs = 18/90 = 1/5! "
            "Now solve the classic Calendar problem: probability of getting exact 53 Sundays across a whole calendar year! Every ordinary non-leap year has 365 days equal to 52 full weeks PLUS ONE EXTRA DAY! That 1 extra day can land uniformly on any of the 7 weekday names, giving 53 Sundays equals exact 1/7! Every LEAP year has 366 days equal to 52 full weeks PLUS TWO CONSECUTIVE EXTRA DAYS {(Sun,Mon), (Mon,Tue), ..., (Sat,Sun)}—exact TWO out of all seven weekday pairs contain Sunday, giving exact 2/7!"
        ),
        "checkpoints": [
            {
                "question": "A box contains 90 discs numbered 1 to 90 (Ex 14.1 Q18). Find probabilities of drawing (i) a two-digit number, and (ii) a perfect square:",
                "options": [
                    "(i) 9 / 10   (81/90),     (ii) 1 / 10   (9/90)",
                    "(i) 8 / 9,     (ii) 9 / 90",
                    "(i) 9 / 10,     (ii) 1 / 9",
                    "(i) 80 / 90,     (ii) 8 / 90"
                ],
                "answer": 0,
                "hint": "Single-digit discs = 1..9 (9 discs), leaving 81 two-digit discs; perfect squares ≤ 90 are 1²..9² (9 discs)!",
                "explanation": "Two-digit = 81/90 = 9/10; Perfect squares {1,4,9,16,25,36,49,64,81} = 9/90 = 1/10."
            },
            {
                "question": "Compare the probability of having 53 Sundays in a randomly selected LEAP year vs an ORDINARY (non-leap) year:",
                "options": [
                    "Leap year = 2 / 7,     Ordinary year = 1 / 7",
                    "Leap year = 1 / 7,     Ordinary year = 2 / 7",
                    "Both equal 1 / 7",
                    "Both equal 53 / 365"
                ],
                "answer": 0,
                "hint": "365 = 52×7 + 1 extra day (1/7); 366 = 52×7 + 2 consecutive days {(Sat,Sun), (Sun,Mon)}!",
                "explanation": "Leap year has 2 extra consecutive days out of 7 pairs containing Sunday (2/7); non-leap has 1 extra day (1/7)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Continuous Geometric Models",
        "subtitle": "Section 14.1 Geometric Probability: Lost Helicopter (Ex 11 = 5/18) & Die Circle Target (Ex 14.1 Q20 = π/24)",
        "speech": (
            "What happens when possible outcomes are NOT discrete integer dots like coin tosses, but INFINITE points spread continuously across a geometric line or flat 2D area? Welcome to Geometric Probability! Here, replace counting outcomes cleanly with LENGTH ratio or AREA ratio! "
            "Check Example Ten (Musical Chairs): Suppose the music stops uniformly inside a 2-minute interval! Probability it stops within the first half-minute (0 to 0.5) equals 0.5 / 2 = ONE FOURTH (1/4)! "
            "Check Example Eleven (Lost Helicopter inside Rectangular Forest): Forest rectangle measures 9 km long × 4.5 km wide (Total Area = 40.5 km²)! A lake spans top-right corner width (9 − 6 = 3 km) by height (4.5 − 2 = 2.5 km), giving Lake Area = 3 × 2.5 = 7.5 km²! Probability helicopter crashed in the lake equals 7.5 / 40.5 = FIVE OVER TWENTY SEVEN (5/27)! "
            "And test Ex 14.1 Q20 carefully (A fair die dropped randomly inside a 3 m × 2 m rectangle containing a central circular hole of diameter 1 m → radius r = 0.5 m): P(inside circle) equals Circle Area (π × 0.5²) divided by Rectangle Area (3 × 2) equals exact π / 24!"
        ),
        "checkpoints": [
            {
                "question": "Suppose you drop a die at random on a rectangular region 3 m × 2 m containing a central circle of diameter 1 m (Ex 14.1 Q20). Probability it lands inside the circle:",
                "options": [
                    "π / 24   [= π(0.5)² / 6]",
                    "π / 6",
                    "π / 12",
                    "π / 48"
                ],
                "answer": 0,
                "hint": "Diameter 1 m ⟹ radius r = 1/2 m, so Circle Area = π(1/4); divide by Rectangle Area 3 × 2 = 6!",
                "explanation": "Area(Circle) / Area(Rectangle) = (π/4) / 6 = π/24."
            },
            {
                "question": "A missing helicopter is reported crashed somewhere in a 9 km × 4.5 km forest rectangle containing a 3 km × 2.5 km rectangular lake (Example 11). Probability it crashed in the lake:",
                "options": [
                    "5 / 27   (= 7.5 / 40.5)",
                    "5 / 18",
                    "7.5 / 13.5",
                    "1 / 6"
                ],
                "answer": 0,
                "hint": "Lake Area = 3 × 2.5 = 7.5 km²; Total Forest Area = 9 × 4.5 = 40.5 km²; simplify 75 / 405 by dividing by 15!",
                "explanation": "7.5 / 40.5 = 75 / 405 = 5 / 27."
            }
        ]
    },
    {
        "id": 14,
        "title": "Algebraic Missing Balls",
        "subtitle": "Exercise 14.1 Q21 (144 Pens → 31/36) & Unknown Ball Count Solving (x Black Balls in 12 & Jar Ratios)",
        "speech": (
            "Now solve Algebraic Unknowns inside Probability—one of CBSE's favorite 3-mark problem types combining linear equations cleanly with Laplace's ratio! "
            "First confirm Exercise Fourteen Point One Question Twenty One: A lot consists of 144 ball pens, of which 20 are defective and the others (144 − 20 = 124) are good! A customer buys a pen ONLY if it is good! Probability customer buys = 124 / 144 = THIRTY ONE OVER THIRTY SIX (31/36), while probability customer does NOT buy = 20/144 = 5/36! "
            "Now solve a classic unknown-count puzzle cleanly: A wooden box contains TWELVE colored balls total, out of which x balls are black! (i) Probability of drawing a black ball equals x / 12! (ii) Suppose SIX MORE black balls are added straight into that exact same wooden box! New black balls = x + 6, and NEW total balls = 12 + 6 = EIGHTEEN! Since the new probability DOUBLES what it was earlier, solve this simple equation cleanly: (x + 6) / 18 = 2 × (x / 12) = x / 6 ⟹ x + 6 = 3x ⟹ 2x = 6 ⟹ x = THREE black balls were present originally!"
        ),
        "checkpoints": [
            {
                "question": "A box contains 12 balls, x of which are black. If 6 MORE black balls are added, the probability of drawing a black ball DOUBLES compared to before. Find initial x:",
                "options": [
                    "x = 3",
                    "x = 4",
                    "x = 6",
                    "x = 2"
                ],
                "answer": 0,
                "hint": "Remember total balls ALSO increases from 12 to 18! Solve (x + 6)/18 = 2(x/12)!",
                "explanation": "(x+6)/18 = x/6 ⟹ x + 6 = 3x ⟹ 2x = 6 ⟹ x = 3."
            },
            {
                "question": "A lot consists of 144 ball pens of which 20 are defective (Ex 14.1 Q21). A shopkeeper draws one pen; the customer buys it only if good. Probability customer will buy:",
                "options": [
                    "31 / 36   (= 124 / 144)",
                    "5 / 36",
                    "31 / 41",
                    "124 / 20"
                ],
                "answer": 0,
                "hint": "Good pens = 144 − 20 = 124; divide 124 / 144 cleanly by 4!",
                "explanation": "Good = 124; P(buy) = 124/144 = 31/36."
            }
        ]
    },
    {
        "id": 15,
        "title": "Fallacies And Proofs",
        "subtitle": "Exercise 14.1 Q25 Argument Audit & Ex 14.1 Q11 Fish Tank (Refuting Equally-Likely Traps & Gambler's Fallacy)",
        "speech": (
            "Be a sharp mathematical detective inside Exercise Fourteen Point One Question Twenty Five! Audit BOTH arguments below carefully to judge which is TRUE and which hides a classic fallacy! "
            "Argument One: 'If two coins are tossed simultaneously, there are three possible outcomes—two heads, two tails, or one of each—therefore, each outcome has probability one third!' Verdict: COMPLETELY INCORRECT! As seen earlier, 'one of each' actually consists of TWO separate elementary outcomes (HT and TH) out of FOUR total, making P(one of each) = 2/4 = 1/2, while P(HH) = 1/4 and P(TT) = 1/4! "
            "Argument Two: 'If a fair die is thrown, there are two possible outcomes—an odd number or an even number—therefore, the probability of getting an odd number is one half!' Verdict: 100% CORRECT! Because odds {1, 3, 5} and evens {2, 4, 6} partition 6 equally likely faces cleanly into 3 and 3! "
            "Also check Q11 Fish Tank (5 male fish + 8 female fish = 13 total fish inside aquarium): P(male fish drawn) = 5/13! And remember Gambler's Fallacy cleanly: unbiased coins and fair cubical dice have ZERO memory—tossing five consecutive Heads never increases or forces a Tail on toss number six!"
        ),
        "checkpoints": [
            {
                "question": "Audit Exercise 14.1 Q25 statements: (I) 'Two coins give 3 outcomes (2H, 2T, 1 of each) so each has P = 1/3'; (II) 'One die throw gives odd or even so P(odd) = 1/2'. Which verdict holds?",
                "options": [
                    "(I) is INCORRECT (P(one each) = 2/4 = 1/2), whereas (II) is CORRECT",
                    "Both (I) and (II) are CORRECT",
                    "(I) is CORRECT and (II) is INCORRECT",
                    "Both (I) and (II) are INCORRECT"
                ],
                "answer": 0,
                "hint": "Notice {HH, HT, TH, TT} splits 'one of each' across HT and TH!",
                "explanation": "Statement I violates equally-likely counting (P(HH)=1/4, P(HT/TH)=1/2, P(TT)=1/4); Statement II is true (3/6 = 1/2)."
            },
            {
                "question": "A fair coin lands Heads 6 times in a row. On the 7th toss, what is the probability of landing Tails?",
                "options": [
                    "1 / 2   (Coins have zero memory of past tosses!)",
                    "More than 1 / 2 because Tails is 'due'",
                    "1 / 64",
                    "6 / 7"
                ],
                "answer": 0,
                "hint": "Independent trials never remember past flips—avoid the Gambler's Fallacy!",
                "explanation": "Independent fair coin flips always keep P(Tail) = 1/2 regardless of prior streak."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Fourteen Summary",
        "subtitle": "Section 14.2 Synthesis: Classical Formula, Bounds, Complements & Experimental-Theoretical Convergence",
        "speech": (
            "Congratulations, probability strategists! You have mastered EVERY concept, card deck, dice grid, urn problem, geometric target, and fallacy trap inside NCERT Class Ten Chapter Fourteen: Probability! Lock in your complete Section Fourteen Point Two checklist before solving forty Interactive Board Quizzes! "
            "One, Theoretical Probability Formula: Assuming all outcomes are equally likely, P(E) equals Number of Outcomes Favourable to E divided by Number of All Possible Outcomes! "
            "Two, Probability Bounds & Extremes: Every probability stays strictly inside 0 ≤ P(E) ≤ 1! Impossible events ALWAYS have probability ZERO, while Sure or Certain events ALWAYS have probability ONE! "
            "Three, Elementary & Complementary Events: The sum of probabilities of ALL elementary events of any experiment equals ONE! And for any event E, its complement satisfies P(E) + P(not E) = 1, giving P(not E) = 1 − P(E)! "
            "Four, Watch Hidden Shrinking Totals & Continuity: Put-aside diamond cards (5 shrinking down to 4) and unreplaced defective bulbs (20 shrinking down to 19) shrink denominators! Also recall continuous geometric area ratios cleanly! Finally, always remember the great convergence law: as empirical trial counts grow huge toward infinity, observed relative frequency steadily converges toward theoretical Laplace probability! Good luck solving!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement across NCERT Chapter 14 is 100% mathematically accurate?",
                "options": [
                    "0 ≤ P(E) ≤ 1; Sum of elementary probabilities = 1; P(not E) = 1 − P(E); Impossible P = 0; Sure P = 1",
                    "P(E) can equal 1.2 if an event is very likely",
                    "Removing a drawn card without replacement leaves the sample space total unchanged",
                    "In two coin tosses, getting 1 head and 1 tail has probability 1/3"
                ],
                "answer": 0,
                "hint": "Review bounds, sum of elementary events, complement formula, and extreme event values!",
                "explanation": "Option 1 summarizes all core Section 14.2 theoretical probability laws accurately."
            },
            {
                "question": "A card is drawn from 52 cards. Match BOTH Sure Event and Impossible Event examples cleanly:",
                "options": [
                    "Sure (P=1): Drawing a Red OR Black card;   Impossible (P=0): Drawing a card with number 15",
                    "Sure: Drawing an Ace;   Impossible: Drawing a Black King",
                    "Sure: Drawing a Face Card;   Impossible: Drawing a Red Queen",
                    "Both have probability 1/2"
                ],
                "answer": 0,
                "hint": "Every standard card is Red or Black (52/52 = 1), whereas rank 15 does not exist (0/52 = 0)!",
                "explanation": "Every card is red or black (P = 1), while no card is numbered 15 (P = 0)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch14 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

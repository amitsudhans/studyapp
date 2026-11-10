#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 14: Probability
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Experimental vs Theoretical",
        "subtitle": "Section 14.1 Introduction: Empirical Experiments vs Pierre Simon Laplace's Classical Probability (1795)",
        "speech": (
            "Welcome to NCERT Class Ten Chapter Fourteen: Probability! In Class Nine, you computed EXPERIMENTAL or empirical probability by actually tossing physical coins hundreds of times and dividing observed heads by total actual trials! "
            "Recall famous historical experiments: Comte de Buffon tossed a coin 4,040 times getting 2,048 heads (ratio 0.507); J. E. Kerrich tossed 10,000 times getting 5,067 heads (0.5067); and Karl Pearson tossed 24,000 times getting 12,012 heads (ratio 0.5005)! Notice a thrilling pattern: as the number of trials grows huge, empirical relative frequency steadily stabilizes toward ONE HALF (0.5)! "
            "However, scientists cannot always roll millions of dice, draw ten thousand blood samples, or crash thousands of machines just to measure odds! In 1795, French mathematician Pierre Simon Laplace formulated THEORETICAL or Classical Probability—predicting chances logically BEFORE doing any experiment, assuming fair physical symmetry! "
            "Whenever a coin, spinner, or cubical die is completely unbiased, theoretical probability equals Favourable Outcomes divided by All Possible Equally Likely Outcomes! Watch experimental outcomes dance around dynamically inside our live animated coin toss simulators and converge smoothly right onto Pierre Simon Laplace's theoretical probability benchmark as random coin trial counts climb much higher across our entire interactive probability laboratory today!"
        ),
        "checkpoints": [
            {
                "question": "What happens to the Experimental (empirical) probability of getting Heads on a fair coin as total number of tosses increases toward thousands?",
                "options": [
                    "It fluctuates less and converges steadily closer to the Theoretical Probability 0.5",
                    "It always reaches 1.0",
                    "It steadily decreases toward 0",
                    "It becomes completely independent of 0.5"
                ],
                "answer": 0,
                "hint": "Recall Karl Pearson's 24,000 coin tosses yielding 12,012/24,000 = 0.5005!",
                "explanation": "With large trials, empirical relative frequency converges toward theoretical probability 0.5."
            },
            {
                "question": "Who formulated the foundational Classical (Theoretical) definition of probability assuming equally likely outcomes?",
                "options": [
                    "Pierre Simon Laplace (1795)",
                    "Euclid of Alexandria",
                    "Pythagoras",
                    "Brahmagupta"
                ],
                "answer": 0,
                "hint": "Named in Section 14.1 Introduction!",
                "explanation": "Pierre Simon Laplace presented the classical theoretical probability definition in 1795."
            }
        ]
    },
    {
        "id": 2,
        "title": "Equally Likely Formula",
        "subtitle": "Section 14.1 Foundations: Unbiased Equally Likely Outcomes & P(E) = Favourable / Total",
        "speech": (
            "Before plugging numbers straight into Laplace's classical probability formula P(E) equals Number of Favourable Outcomes divided by Number of All Possible Outcomes, always verify ONE golden precondition FIRST: are all possible outcomes physically EQUALLY LIKELY? "
            "Examine Exercise Fourteen Point One Question Two carefully to sharpen your instinct! Case One: a driver attempts to start a car—it starts cleanly or does not start! Are those two outcomes equally likely? NO! A brand new car almost certainly starts while a broken engine stalls repeatedly, so probability is NOT one half! "
            "Case Two: a basketball player attempts to shoot a basket—scores or misses! Again NOT equally likely, because shooting success depends heavily on player training, court distance, and defense! "
            "Now contrast Case Three: a trial made purely by guessing to answer a true-false exam question blindly, a newborn baby being either a boy or a girl, or tossing an unbiased symmetric two-sided coin! Every outcome holds identical physical symmetry with zero hidden bias, making them genuinely EQUALLY LIKELY! Never apply simple counting ratios Favourable Outcomes divided by Total Possible Outcomes unless symmetric physics genuinely guarantees every single elementary outcome shares identical mathematical likelihood before conducting any random trial!"
        ),
        "checkpoints": [
            {
                "question": "Which experiment below does NOT have equally likely outcomes (Exercise 14.1 Q2)?",
                "options": [
                    "A driver attempts to start a car (car starts or does not start)",
                    "Tossing a fair unbiased coin (Head or Tail)",
                    "A trial made to answer a pure True-False question blindly (Right or Wrong)",
                    "Throwing a fair symmetric six-faced cubical die (1, 2, 3, 4, 5, or 6)"
                ],
                "answer": 0,
                "hint": "Whether a car starts depends on battery, fuel, and engine health—not 50-50 symmetry!",
                "explanation": "Car starting depends on mechanical condition, whereas unbiased coins, dice, and blind guesses have equally likely outcomes."
            },
            {
                "question": "In Classical Probability, what is the formula for P(E) when all elementary outcomes are equally likely?",
                "options": [
                    "P(E) = (Number of outcomes favourable to E) / (Total number of possible outcomes)",
                    "P(E) = Total outcomes / Favourable outcomes",
                    "P(E) = Favourable outcomes − Total outcomes",
                    "P(E) = Favourable outcomes × Total outcomes"
                ],
                "answer": 0,
                "hint": "Part divided by Whole always produces a fraction between 0 and 1!",
                "explanation": "P(E) equals favourable outcomes divided by total equally likely outcomes."
            }
        ]
    },
    {
        "id": 3,
        "title": "Probability Axioms Bounds",
        "subtitle": "Section 14.1 Rules: 0 ≤ P(E) ≤ 1, Sure Event (1), Impossible Event (0) & Sum of Elementary Events = 1",
        "speech": (
            "Lock in FOUR unbreakable laws governing every single probability number in the universe inside Section Fourteen Point One! "
            "Law One, Universal Bounds: Since favourable counts ALWAYS sit cleanly between zero and total possible outcomes, EVERY valid probability P(E) satisfies ZERO less than or equal to P(E) less than or equal to ONE! That means negative numbers like minus 1.5, fractions bigger than one like five over four, and percentages above 100 percent like 105 percent can NEVER represent any probability! "
            "Law Two, Impossible Event: An event completely impossible to occur has ZERO favourable outcomes, so P(E) equals ZERO! Example (Ex 14.1 Q6): picking an orange-flavored candy blindly from a bag containing ONLY lemon candies has probability ZERO! "
            "Law Three, Sure or Certain Event: An event guaranteed to happen EVERY single trial equals ONE! Picking a lemon candy from that lemon-only bag has probability ONE! "
            "Law Four, Elementary Events: An event having only a SINGLE simple outcome is called an elementary event, and adding together the probabilities of ALL possible elementary events of any random experiment (such as drawing red, blue, or yellow balls inside Textbook Example Two) ALWAYS equals EXACTLY ONE every single time cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Which value CANNOT possibly be the probability of any event (Exercise 14.1 Q4)?",
                "options": [
                    "−1.5   (probabilities can never be negative or greater than 1!)",
                    "2 / 3",
                    "15%",
                    "0.7"
                ],
                "answer": 0,
                "hint": "Check universal rule 0 ≤ P(E) ≤ 1 (remember 15% = 0.15)!",
                "explanation": "Since 0 ≤ P(E) ≤ 1 always holds, negative −1.5 cannot be a probability."
            },
            {
                "question": "A bag contains 1 red, 1 blue, and 1 yellow ball of identical size (Example 2). What is the sum P(Red) + P(Blue) + P(Yellow)?",
                "options": [
                    "1   (= ⅓ + ⅓ + ⅓, sum of all elementary event probabilities!)",
                    "3",
                    "⅓",
                    "0"
                ],
                "answer": 0,
                "hint": "Every experiment's elementary events always sum cleanly to 1!",
                "explanation": "Sum of probabilities of all elementary events of any experiment ALWAYS equals 1."
            }
        ]
    },
    {
        "id": 4,
        "title": "Complementary Event Law",
        "subtitle": "Section 14.1: P(E) + P(Ē) = 1, Complementary Shortcut P(not E) = 1 − P(E) & Birthday Problems",
        "speech": (
            "Meet the fastest subtraction shortcut in all of Probability inside Section Fourteen Point One: Complementary Events! "
            "For any event E, the exact opposite event 'not E' (written E-bar, Ē) consists of EVERY outcome inside the sample space where E does NOT happen! Since on every trial either E happens or E does not happen with zero overlap, together they cover one hundred percent of all possible outcomes: P(E) plus P(not E) ALWAYS equals EXACTLY ONE! Rearranging gives the golden Complementary Formula: P(not E) equals ONE MINUS P(E)! "
            "Test Exercise Fourteen Point One Question Five instantly! If P(E) equals 0.05, what is P(not E)? Align your decimal places carefully from 1.00: 1.00 minus 0.05 equals exact ZERO POINT NINE FIVE (careful—never mistakenly write 0.5 or 0.995)! "
            "Now inspect Question Seven, the classic Same Birthday problem! In a small group of just two students, the probability they do NOT share the exact same birthday is 0.992! What is the probability BOTH share the EXACT same birthday? Apply the Complement Law immediately: 1.000 minus 0.992 equals exact 0.008! Likewise in Example Four tennis match, winning match probability 0.62 leaves losing match probability exact 0.38 cleanly every single time!"
        ),
        "checkpoints": [
            {
                "question": "If P(E) = 0.05, what is the probability of 'not E' (Exercise 14.1 Q5)?",
                "options": [
                    "0.95   (= 1.00 − 0.05)",
                    "0.05",
                    "0.995",
                    "0.50"
                ],
                "answer": 0,
                "hint": "Align decimals cleanly: 1.00 − 0.05!",
                "explanation": "P(not E) = 1 − P(E) = 1.00 − 0.05 = 0.95."
            },
            {
                "question": "In a group of 2 students, the probability of NOT having the same birthday is 0.992 (Ex 14.1 Q7). Probability that both have the SAME birthday:",
                "options": [
                    "0.008",
                    "0.08",
                    "0.992",
                    "0.0008"
                ],
                "answer": 0,
                "hint": "Subtract 1.000 − 0.992 carefully!",
                "explanation": "Same Birthday + Not Same Birthday are complementary: 1 − 0.992 = 0.008."
            }
        ]
    },
    {
        "id": 5,
        "title": "Single Die Problems",
        "subtitle": "Example 3 & Ex 14.1 Q13: Unbiased Die {1,2,3,4,5,6}, Prime Number Trap {2,3,5} & Composites",
        "speech": (
            "Now roll a fair six-faced cubical die once (Example Three & Exercise Fourteen Point One Question Thirteen)! Write down all six equally likely elementary outcomes right away: {1, 2, 3, 4, 5, 6}, Total = 6! "
            "Watch out for the NUMBER ONE BOARD EXAM TRAP in the entire chapter: finding the probability of getting a PRIME NUMBER on a single die throw! Students repeatedly miscount number ONE as prime and answer 4/6! STOP right there! Recall Chapter One Number Theory: number ONE has only ONE divisor, so ONE IS NEITHER PRIME NOR COMPOSITE! "
            "List the ONLY prime faces on a standard die: {2, 3, 5}—exact count THREE primes! So P(Prime) equals 3 over 6 equals ONE HALF! And the ONLY composite faces on a die are {4, 6}—exact count TWO composites, so P(Composite) equals 2/6 equals ONE THIRD! "
            "Also check Q13(ii): finding a face number lying strictly BETWEEN 2 and 6 excludes both endpoints 2 and 6 cleanly, leaving exact outcomes {3, 4, 5} equals 3/6 equals ONE HALF! Notice P(> 4) gives {5, 6} equals 2/6 equals 1/3, while its exact complement P(≤ 4) gives {1, 2, 3, 4} equals exact 4/6 equals 2/3 cleanly!"
        ),
        "checkpoints": [
            {
                "question": "A fair die is thrown once (Ex 14.1 Q13). Find the probability of getting (i) a prime number, and (ii) a number lying strictly between 2 and 6:",
                "options": [
                    "(i) 1/2   [{2,3,5}],     (ii) 1/2   [{3,4,5}]",
                    "(i) 2/3   [{1,2,3,5}],     (ii) 5/6",
                    "(i) 1/3   [{3,5}],     (ii) 1/3",
                    "(i) 1/2,     (ii) 2/3"
                ],
                "answer": 0,
                "hint": "Remember 1 is NOT prime! Primes = {2, 3, 5}; strictly between 2 and 6 = {3, 4, 5}!",
                "explanation": "Primes = {2,3,5} (3/6 = 1/2); numbers between 2 and 6 = {3,4,5} (3/6 = 1/2)."
            },
            {
                "question": "In one throw of a fair die (Example 3), what is the probability of getting a number GREATER than 4, and LESS than or equal to 4?",
                "options": [
                    "P(> 4) = 1/3   [{5,6}],     P(≤ 4) = 2/3   [{1,2,3,4}]",
                    "P(> 4) = 1/2,     P(≤ 4) = 1/2",
                    "P(> 4) = 1/6,     P(≤ 4) = 5/6",
                    "P(> 4) = 2/3,     P(≤ 4) = 1/3"
                ],
                "answer": 0,
                "hint": "Favourable for > 4 are ONLY 5 and 6 (2 of 6); ≤ 4 is its exact complement!",
                "explanation": "P(> 4) = 2/6 = 1/3; complement P(≤ 4) = 1 − 1/3 = 2/3."
            }
        ]
    },
    {
        "id": 6,
        "title": "Two Three Coins",
        "subtitle": "Example 7 & Ex 14.1 Q23: 2-Coin Sample Space (4 Outcomes, No 1/3 Fallacy) & 3-Coin Game (1/4 vs 3/4)",
        "speech": (
            "Never fall for the classic Two-Coin 1/3 Fallacy! Many students wrongly claim: tossing two coins gives 'two heads', 'two tails', or 'one of each', so each probability must be 1/3! WRONG! Why? Because Coin One landing Head and Coin Two landing Tail (HT) is a COMPLETELY DIFFERENT physical outcome from Coin One landing Tail and Coin Two landing Head (TH)! "
            "Two distinct unbiased coins tossed simultaneously produce FOUR equally likely ordered outcomes: {HH, HT, TH, TT}! Check Example Seven right away: Probability of AT LEAST ONE HEAD covers {HH, HT, TH} = 3 over 4! Probability of AT MOST ONE HEAD covers {HT, TH, TT} = 3 over 4! Probability of EXACTLY ONE HEAD covers {HT, TH} = 2/4 = ONE HALF! "
            "Now level up cleanly to THREE Coins tossed together in Exercise Fourteen Point One Question Twenty Three! Tossing three fair coins yields 2 × 2 × 2 equals EIGHT equally likely ordered outcomes: {HHH, HHT, HTH, THH, TTT, TTH, THT, HTT}! A player wins the coin game ONLY if ALL three tosses match ({HHH, TTT} = 2/8 = 1/4), so the probability of LOSING the game equals 1 minus 1/4 equals exact THREE FOURTHS!"
        ),
        "checkpoints": [
            {
                "question": "Two coins of ₹1 and ₹2 are tossed simultaneously (Example 7). Find the probability of getting AT LEAST ONE head:",
                "options": [
                    "3 / 4   [outcomes {HH, HT, TH} out of {HH, HT, TH, TT}]",
                    "1 / 3",
                    "1 / 2",
                    "1 / 4"
                ],
                "answer": 0,
                "hint": "HT and TH are TWO distinct outcomes! Only TT has zero heads!",
                "explanation": "Out of 4 outcomes {HH, HT, TH, TT}, 3 have at least one head (1 − 1/4 = 3/4)."
            },
            {
                "question": "A player tosses a ₹1 coin THREE times and wins ONLY if all tosses give the same result (3 heads or 3 tails, Ex 14.1 Q23). Find probability of LOSING:",
                "options": [
                    "3 / 4   (= 6 / 8 remaining mixed outcomes)",
                    "1 / 4",
                    "1 / 2",
                    "7 / 8"
                ],
                "answer": 0,
                "hint": "Total 8 outcomes; winning outcomes = {HHH, TTT} (2/8 = 1/4); subtract from 1!",
                "explanation": "P(Win) = 2/8 = 1/4; therefore P(Lose) = 1 − 1/4 = 3/4."
            }
        ]
    },
    {
        "id": 7,
        "title": "Two Dice Grid",
        "subtitle": "Example 13 & Ex 14.1 Q22, Q24: 36 Ordered Pairs Grid, Symmetric Sum-7 Peak & Sum Probabilities",
        "speech": (
            "Master rolling TWO dice (blue die and grey die) simultaneously—Section Fourteen Point One Example Thirteen and Exercise Fourteen Point One Questions Twenty Two and Twenty Four! "
            "Draw the famous 6 × 6 coordinate grid! Six faces on Die One paired with six faces on Die Two create SIX TIMES SIX equals THIRTY SIX equally likely ordered pairs, where pair (1, 4) is strictly DIFFERENT from pair (4, 1)! Only matching doublets {(1,1), (2,2), ..., (6,6)} appear ONCE each (total 6 doublets, probability 6/36 = 1/6)! "
            "Watch the gorgeous Sum Pyramid across Sums Two through Twelve! Sum 2 has only 1 pair (1,1) = 1/36; Sum 3 has 2/36; rising step by step cleanly up to the tallest peak SUM SEVEN with SIX pairs {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)} = 6/36 = 1/6; then descending symmetrically down to Sum 12 = 1/36! Notice P(Sum ≤ 12) = 1 (Sure Event) and P(Sum = 13) = 0 (Impossible Event)! "
            "Also check Q24 thoroughly: probability that number 5 will NOT come up on EITHER dice throw leaves five times five equals 25 out of 36 outcomes (25/36), while number 5 coming up AT LEAST once equals its complement 1 minus 25/36 equals 11/36!"
        ),
        "checkpoints": [
            {
                "question": "Two dice are thrown at the same time (Ex 14.1 Q22 & Q24). What is the probability that (i) SUM is 8, and (ii) 5 will NOT come up either time?",
                "options": [
                    "(i) 5 / 36,     (ii) 25 / 36",
                    "(i) 1 / 6,     (ii) 11 / 36",
                    "(i) 5 / 36,     (ii) 30 / 36",
                    "(i) 4 / 36,     (ii) 25 / 36"
                ],
                "answer": 0,
                "hint": "Sum 8 = {(2,6),(3,5),(4,4),(5,3),(6,2)} (5 pairs); avoiding 5 on BOTH dice leaves 5 choices × 5 choices!",
                "explanation": "Sum 8 has 5 outcomes (5/36); avoiding 5 on either die leaves 5×5 = 25 outcomes (25/36)."
            },
            {
                "question": "When two fair dice are rolled simultaneously, which sum of the two numbers has the HIGHEST probability (6/36 = 1/6)?",
                "options": [
                    "Sum = 7   [{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)}]",
                    "Sum = 6",
                    "Sum = 12",
                    "Sum = 2"
                ],
                "answer": 0,
                "hint": "Look at the longest main anti-diagonal of the 6 × 6 grid!",
                "explanation": "Sum = 7 forms the full 6-entry diagonal of the 6×6 grid, giving peak probability 6/36 = 1/6."
            }
        ]
    },
    {
        "id": 8,
        "title": "Playing Card Deck",
        "subtitle": "Example 4 & Ex 14.1 Q14: Complete 52-Card Deck Breakdown (4 Suits, 2 Colors, 12 Face Cards)",
        "speech": (
            "Know every single card inside a standard well-shuffled deck of FIFTY TWO playing cards cleanly, because card problems appear in EVERY Class Ten board paper! "
            "Divide 52 cards first by COLOR: exact TWENTY SIX RED cards and TWENTY SIX BLACK cards! "
            "Next divide cleanly into FOUR SUITS of THIRTEEN cards each: TWO Red suits—HEARTS and DIAMONDS (13 each)—and TWO Black suits—SPADES and CLUBS (13 each)! Notice EVERY suit contains identical 13 ranks: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King! "
            "Watch TWO super common card traps carefully! Trap One: Which cards are FACE CARDS (picture cards)? ONLY Kings, Queens, and Jacks—THREE per suit × FOUR suits equals TWELVE FACE CARDS TOTAL (6 Red Face Cards, 6 Black Face Cards)! Remember: ACES ARE NOT FACE CARDS! There are 4 Aces total! "
            "Test ALL SIX parts of Exercise 14.1 Question 14 immediately: P(King of red color) = 2/52 = 1/26! P(Face card) = 12/52 = 3/13! P(Red face card) = 6/52 = 3/26! P(Jack of hearts) = 1/52! P(any Spade card) = 13/52 = 1/4! And finally P(Queen of diamonds) equals exact 1 out of all 52 well-shuffled playing cards cleanly!"
        ),
        "checkpoints": [
            {
                "question": "From a well-shuffled deck of 52 cards (Ex 14.1 Q14), find the probability of drawing (i) a FACE card, and (ii) a RED King:",
                "options": [
                    "(i) 3 / 13   (= 12/52),     (ii) 1 / 26   (= 2/52)",
                    "(i) 4 / 13   (= 16/52),     (ii) 1 / 13   (= 4/52)",
                    "(i) 3 / 26   (= 6/52),     (ii) 1 / 52",
                    "(i) 1 / 4,     (ii) 1 / 26"
                ],
                "answer": 0,
                "hint": "Face cards are ONLY J, Q, K (4×3 = 12 total; NOT Aces!); Red Kings = King♥ + King♦ (2 total)!",
                "explanation": "12/52 = 3/13 for face card; 2/52 = 1/26 for red King."
            },
            {
                "question": "One card is drawn from a well-shuffled deck of 52 cards (Example 4). What is the probability that the card is NOT an Ace?",
                "options": [
                    "12 / 13   (= 1 − 4/52 = 48/52)",
                    "1 / 13",
                    "11 / 13",
                    "3 / 4"
                ],
                "answer": 0,
                "hint": "There are 4 Aces in 52 cards (4/52 = 1/13); subtract cleanly from 1!",
                "explanation": "P(Ace) = 4/52 = 1/13, so complement P(not Ace) = 1 − 1/13 = 12/13."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch14 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 7: The Mathematics of Maybe: Introduction to Probability
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 7.2.3 (LLN & Gambler's Fallacy) through 7.4, Exercises & Summary, 1-3 word titles, 195-215 words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Large Numbers Fallacy",
        "subtitle": "Section 7.2.3 Law of Large Numbers & Misconceptions: Long-Run Convergence vs The Gambler's Fallacy",
        "speech": (
            "Uncover two of the deepest lessons across all of probability science inside Section Seven Point Two Point Three: THE LAW OF LARGE NUMBERS versus THE GAMBLER'S FALLACY! "
            "First, inspect what happens when you flip a fair coin just TEN consecutive times! Getting seven heads and three tails—experimental relative frequency zero point seven zero—happens frequently inside short noisy runs! Now flip that same balanced coin ONE HUNDRED, ONE THOUSAND, even TEN THOUSAND times! Watch experimental relative frequency settle steadily closer and closer toward exact theoretical probability ZERO POINT FIVE! That fundamental long-run stabilization as trial count N grows vast is called THE LAW OF LARGE NUMBERS! "
            "Second, smash the famous misleading trap known as THE GAMBLER'S FALLACY! Suppose a strictly fair unbiased coin lands Heads FIVE consecutive times in a row! Many onlookers whisper excitedly: Tails MUST be overdue next to balance out the streak! "
            "COMPLETELY FALSE! Does an ordinary metal coin possess memory of previous tosses or keep score? NO! Each independent coin flip starts completely fresh with zero awareness of earlier toss history—so the sixth single toss STILL carries the EXACT SAME fifty percent chance of landing Heads and fifty percent chance of landing Tails!"
        ),
        "checkpoints": [
            {
                "question": "A fair coin has landed Tails 6 consecutive times in a row. What is the exact probability that the 7th toss lands HEADS?",
                "options": [
                    "Still exactly 0.5 (1/2), because independent coin tosses have no memory of past outcomes",
                    "Much greater than 0.5 because Heads is 'due' to catch up",
                    "Close to 0 because Tails is on a hot streak",
                    "6/7"
                ],
                "answer": 0,
                "hint": "Remember: believing Tails makes Heads more likely next is the Gambler's Fallacy!",
                "explanation": "Coins have zero memory; every independent fair toss maintains P(Head) = 1/2 regardless of preceding streaks."
            },
            {
                "question": "What does the Law of Large Numbers formally describe?",
                "options": [
                    "As the number of repeated independent trials grows very large, experimental relative frequency converges closely toward theoretical probability",
                    "Large coins land Heads more often than small coins",
                    "10 flips always show exactly 5 Heads and 5 Tails",
                    "Theoretical probability doubles after 1,000 trials"
                ],
                "answer": 0,
                "hint": "Compare noisy short runs (10 flips) against smooth huge runs (10,000 flips)!",
                "explanation": "Law of Large Numbers states long-run relative frequencies stabilize near theoretical probabilities as sample size N → ∞."
            }
        ]
    },
    {
        "id": 10,
        "title": "Sample Space Sets",
        "subtitle": "Section 7.3.1 Sample Space: Definition (S), Sample Size n(S) & Single/Double Coin and Single Die Examples",
        "speech": (
            "Now organize every random experiment systematically using crisp mathematical set notation in Section Seven Point Three Point One: SAMPLE SPACE! "
            "Imagine writing out a complete, master reference checklist listing EVERY possible non-duplicate basic outcome an experiment could ever produce! In probability theory, that master set of all distinct elementary outcomes is named the SAMPLE SPACE and denoted neatly by capital letter S! And the total count of distinct elements inside S is written cleanly as n of S! "
            "Examine three foundational sample spaces effortlessly! Experiment One—Tossing ONE fair coin: only two distinct upward faces exist, so sample space S equals curly brace H comma T close, giving sample size n of S equals TWO! Experiment Two—Rolling ONE six-sided die: sample space S equals curly brace one, two, three, four, five, six close, giving size n of S equals SIX! "
            "Experiment Three—Tossing TWO distinct fair coins simultaneously (or tossing one single coin twice sequentially): NEVER fall for the careless three-outcome trap! Distinguish Coin One from Coin Two carefully: Head-Head, Head-Tail, Tail-Head, and Tail-Tail yield FOUR distinct equally likely elementary outcomes inside complete sample space S—making exact total sample size n of S strictly equal to FOUR!"
        ),
        "checkpoints": [
            {
                "question": "What is the complete sample space S and sample size n(S) when tossing two distinct coins together?",
                "options": [
                    "S = {HH, HT, TH, TT}, n(S) = 4",
                    "S = {HH, HT, TT}, n(S) = 3",
                    "S = {H, T}, n(S) = 2",
                    "S = {1, 2, 3, 4, 5, 6}, n(S) = 6"
                ],
                "answer": 0,
                "hint": "Getting Head on Coin 1 + Tail on Coin 2 (HT) differs from Tail on Coin 1 + Head on Coin 2 (TH)!",
                "explanation": "Order/coin identity matters: {HH, HT, TH, TT} yields 4 distinct equally likely outcomes."
            },
            {
                "question": "Why are duplicate entries strictly excluded when writing any Sample Space set S?",
                "options": [
                    "Because S is a mathematical set listing each distinct unique possible outcome exactly once",
                    "Because computers forbid curly braces with repeated digits",
                    "Because sample spaces always have only 2 elements",
                    "Because outcomes with duplicates become impossible"
                ],
                "answer": 0,
                "hint": "Remember set theory: every unique outcome occupies one entry inside S!",
                "explanation": "A sample space S lists all distinct, non-overlapping elementary outcomes of an experiment without repetition."
            }
        ]
    },
    {
        "id": 11,
        "title": "Compound Outcome Counting",
        "subtitle": "Section 7.3.1 Multi-Step Sample Spaces: Two-Dice Ordered Pairs Grid (n(S) = 36) & Spinner-Coin Combinations",
        "speech": (
            "Now scale sample space mastery up cleanly from two coins to multi-object compound experiments inside Section Seven Point Three Point One! "
            "What happens when you roll TWO distinguishable dice—say one bright blue die alongside one bright amber die—and record ordered pairs cleanly? The first die alone displays six faces, and for EACH blue face, the amber die independently displays six faces! Multiplying six times six yields THIRTY-SIX crisp ordered pairs inside Sample Space S—spanning systematically from one-comma-one clear down to six-comma-six! Notice why ordering stays essential: rolling blue-two plus amber-five is genuinely a separate physical outcome from rolling blue-five plus amber-two! "
            "Inspect dice sums carefully across that thirty-six-square outcome grid! Does rolling a combined sum equal to seven happen with the exact same frequency as rolling a combined sum equal to twelve? NO! Sum twelve occurs ONLY once at six-comma-six (probability one thirty-sixth), whereas sum seven stretches diagonally across SIX distinct pairs—yielding six thirty-sixths equals ONE-SIXTH! "
            "Whenever two independent experimental stages offer m distinct choices followed sequentially by n distinct choices, total combined sample size ALWAYS equals m TIMES n—a crisp, reliable, universal counting rule working smoothly across card decks, colorful spinners, coins, and dice!"
        ),
        "checkpoints": [
            {
                "question": "When rolling two fair 6-sided dice simultaneously, what is total sample size n(S) and what is P(sum = 7)?",
                "options": [
                    "n(S) = 36, and P(sum = 7) = 6/36 = 1/6",
                    "n(S) = 12, and P(sum = 7) = 1/12",
                    "n(S) = 36, and P(sum = 7) = 1/36",
                    "n(S) = 11, and P(sum = 7) = 1/11"
                ],
                "answer": 0,
                "hint": "List the pairs adding to 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) out of 6 × 6 = 36 pairs!",
                "explanation": "With 36 equally likely ordered pairs, 6 pairs sum to 7 ⇒ P(sum = 7) = 6/36 = 1/6."
            },
            {
                "question": "A fair coin (2 outcomes) and a 4-color uniform spinner (4 sectors) are used together. How many outcomes are in combined sample space S?",
                "options": [
                    "8 outcomes (2 × 4)",
                    "6 outcomes (2 + 4)",
                    "16 outcomes",
                    "4 outcomes"
                ],
                "answer": 0,
                "hint": "Apply the multiplication principle across Stage 1 (m = 2) and Stage 2 (n = 4)!",
                "explanation": "Each of the 2 coin results pairs with 4 spinner sectors ⇒ n(S) = 2 × 4 = 8 outcomes."
            }
        ]
    },
    {
        "id": 12,
        "title": "Events As Subsets",
        "subtitle": "Section 7.3.2 Events: Event E as Subset of S, Complementary Rule P(not E) = 1 − P(E), Impossible & Sure Events",
        "speech": (
            "Now connect Sample Space S cleanly to real probability questions inside Section Seven Point Three Point Two: EVENTS! "
            "Suppose rolling a fair die creates sample space S equals one, two, three, four, five, six, and someone asks specifically about rolling a number STRICTLY GREATER THAN FOUR! Only outcomes five and six satisfy that criterion! Notice five-and-six forms a neat smaller collection inside S—a SUBSET! Formally, ANY subset E contained inside sample space S is called an EVENT! Calculating equally likely probability simply divides subset sizes: P of E equals n of E DIVIDED BY n of S! "
            "Spot THREE rock-star special subsets immediately! Subset One—the EMPTY SET (zero elements inside S, such as rolling seven on a standard six-sided die) represents an IMPOSSIBLE EVENT with probability zero! Subset Two—the ENTIRE SAMPLE SPACE S itself (such as rolling a whole number from one through six) forms a SURE EVENT with probability one! "
            "Subset Three—THE COMPLEMENTARY EVENT NOT-E gathers every elementary outcome inside S lying strictly OUTSIDE subset E! Adding both probabilities always equals one, unlocking the golden shortcut: P OF NOT-E EQUALS ONE MINUS P OF E—ideal for solving tricky 'at least one' probability calculations effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "If the probability of winning a raffle ticket is 0.08, what is the exact probability of NOT winning?",
                "options": [
                    "0.92 (using complement rule 1 − 0.08)",
                    "0.08",
                    "1.08",
                    "0.80"
                ],
                "answer": 0,
                "hint": "Every trial either belongs to E or to its complement 'not E', so P(E) + P(not E) = 1!",
                "explanation": "P(not winning) = 1 − P(winning) = 1 − 0.08 = 0.92."
            },
            {
                "question": "In double coin toss S = {HH, HT, TH, TT}, which subset represents event E = 'getting AT LEAST ONE head' and what is P(E)?",
                "options": [
                    "E = {HH, HT, TH}, so P(E) = 3/4",
                    "E = {HT, TH}, so P(E) = 1/2",
                    "E = {HH}, so P(E) = 1/4",
                    "E = {TT}, so P(E) = 1/4"
                ],
                "answer": 0,
                "hint": "'At least one head' includes 1 head (HT, TH) OR 2 heads (HH) — only TT fails!",
                "explanation": "E = {HH, HT, TH} has 3 outcomes out of 4 (or via complement 1 − P(TT) = 1 − 1/4 = 3/4)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Multi-Step Tree Diagrams",
        "subtitle": "Section 7.4 Tree Diagrams: Visualizing Multi-Step Trials (Double Coin, Fruit Baskets & Colored Pens)",
        "speech": (
            "Whenever a random experiment unfolds sequentially across TWO OR THREE distinct stages, writing plain flat lists becomes messy and error-prone fast! Section Seven Point Four introduces our visual superpower: TREE DIAGRAMS! "
            "Picture growing an organized branching tree sideways from one single root dot on the left margin! Draw Stage One branches fanning out cleanly for every possible first-step choice! Then from the outer tip of EACH Stage One branch, sprout fresh Stage Two sub-branches representing every subsequent second-step outcome! Following any single continuous trail smoothly from root straight to final leaf tip traces ONE exact complete outcome inside the compound sample space! "
            "Explore two classic textbook tree models! Model One—FRUIT BASKETS: Basket A holds an Apple or Banana; Basket B holds an Orange, Mango, or Guava! Two branches splitting from the root immediately fork into three branches each—visibly displaying all two times three equals SIX complete fruit-basket pairs cleanly with zero forgotten or duplicated combinations! "
            "Model Two—DRAWING COLORED PENS: pulling pens sequentially from a pouch containing Red and Blue pens maps every distinct ordered draw clearly along separate branching paths—never confusing Red-then-Blue with Blue-then-Red, and clearly updating remaining pen counts whenever draws happen without replacement!"
        ),
        "checkpoints": [
            {
                "question": "Basket 1 offers 3 fruits (Apple, Mango, Pear) and Basket 2 offers 2 snacks (Date, Walnut). How many final leaf tips appear at the right end of a complete 2-stage tree diagram?",
                "options": [
                    "6 leaf tips (3 branches × 2 sub-branches each)",
                    "5 leaf tips (3 + 2)",
                    "9 leaf tips",
                    "2 leaf tips"
                ],
                "answer": 0,
                "hint": "Every single one of the 3 initial branches splits into 2 child branches!",
                "explanation": "Tree branching multiplies stage counts: 3 × 2 = 6 total complete paths from root to leaves."
            },
            {
                "question": "Why are tree diagrams particularly valuable in multi-step probability problems?",
                "options": [
                    "They visually guarantee every sequential outcome path is systematically listed once without missing or duplicating combinations",
                    "They make all unequal probabilities become equal automatically",
                    "They eliminate all need for sample spaces",
                    "They only apply to botanical tree leaves"
                ],
                "answer": 0,
                "hint": "Tracing from root to tip enumerates n(S) visually step by step!",
                "explanation": "Tree diagrams structure multi-step experiments cleanly so no compound path is overlooked or repeated."
            }
        ]
    },
    {
        "id": 14,
        "title": "Path Branch Probabilities",
        "subtitle": "Section 7.4 Path Probabilities: Assigning Branch Fractions, Multiplying Independent Paths & Verifying Total Sum = 1",
        "speech": (
            "Now supercharge visual tree diagrams with quantitative fractional weights inside Section Seven Point Four: PATH PROBABILITIES! "
            "Remember that not every branch option starts equally likely! Suppose Pencil Box One holds TWO Red pens alongside ONE Blue pen (three pens total), so upper branch Red carries fractional weight two-thirds while lower branch Blue carries fractional weight one-third! Observe immediately that sister branches sprouting from ANY single split node ALWAYS sum neatly to EXACTLY ONE! "
            "Now extend cleanly onward into Stage Two: suppose Pencil Box Two holds ONE Red pen alongside THREE Blue pens (four pens total), yielding one-fourth Red and three-fourths Blue! How do we evaluate the exact theoretical probability of traversing one COMPLETE route from leftmost root to rightmost leaf—for example Red from Box One followed by Blue from Box Two? "
            "Apply the fundamental TREE MULTIPLICATION RULE: multiply the fractional branch probabilities written along EVERY connected segment along that individual trail! So P of Red-then-Blue equals two-thirds TIMES three-fourths equals six-twelfths equals ONE-HALF! To compute composite events matching MULTIPLE separate leaf paths—like picking mismatched pen colors from two different boxes—simply SUM those leaf path probabilities cleanly! Always verify the complete total leaf sum equals exactly ONE!"
        ),
        "checkpoints": [
            {
                "question": "Box A has 2 Red and 1 Blue pen; Box B has 1 Red and 3 Blue pens. One pen is drawn from each. Along a weighted tree diagram, what is P(Red from A AND Blue from B)?",
                "options": [
                    "1/2 (from 2/3 × 3/4 = 6/12)",
                    "1/4",
                    "2/7",
                    "17/12"
                ],
                "answer": 0,
                "hint": "Multiply P(Red in A) = 2/3 along the first branch by P(Blue in B) = 3/4 along the second branch!",
                "explanation": "Multiplying along the path gives (2/3) × (3/4) = 6/12 = 1/2."
            },
            {
                "question": "What check ALWAYS confirms your weighted tree diagram probabilities have zero arithmetic errors?",
                "options": [
                    "Branches from every node sum to 1, and ALL final leaf-tip path probabilities sum cleanly to 1",
                    "Each branch probability must exceed 1",
                    "Every leaf probability must equal 0.5",
                    "The bottom branch always equals zero"
                ],
                "answer": 0,
                "hint": "Total probability across all exhaustive mutually exclusive outcomes must equal certainty (1)!",
                "explanation": "Both local child-branch sums at each split and the global sum of all complete root-to-leaf paths equal 1."
            }
        ]
    },
    {
        "id": 15,
        "title": "Geometric Drop Applications",
        "subtitle": "End-of-Chapter Exercises: Geometric Area Drop Probabilities, Unequal Spinners, Sampling & Compound Event Strategies",
        "speech": (
            "Conquer high-scoring END-OF-CHAPTER EXERCISES by blending probability reasoning seamlessly with Chapter Six spatial measurement skills: GEOMETRIC AREA PROBABILITY! "
            "Imagine dropping a tiny marble, pinpoint dart, or raindrop completely at random inside a flat rectangular courtyard measuring ten metres by six metres—yielding total flat area sixty square metres! Nested inside that rectangle sits one decorative circular water fountain enclosing area fifteen square metres! Assuming every point inside the rectangle holds equal chance of being hit, what is the probability your randomly dropped marble lands inside the fountain? "
            "Upgrade finite counting ratios smoothly into continuous spatial geometry: GEOMETRIC PROBABILITY EQUALS FAVOURABLE TARGET AREA DIVIDED BY TOTAL ENCLOSING REGION AREA! Dividing fifteen square metres by sixty square metres immediately gives one-fourth or zero point two five! "
            "Master three extra high-yield end-of-chapter problem strategies too! On circular spinners, ALWAYS divide central sector degree angles by the full circle three hundred sixty degrees—never assume uneven wedges share equal probabilities! On sequential multi-step draws, distinguish carefully between 'WITH replacement' versus 'WITHOUT replacement' so Stage Two denominators shrink accurately! And solve 'at least one' problems effortlessly via complement rule one minus P(none) whenever direct leaf path listing feels overly long and tedious!"
        ),
        "checkpoints": [
            {
                "question": "A dart lands randomly somewhere inside a 10 m × 8 m rectangular target holding an inner painted circle of area 16 m². What is the probability it lands inside the inner circle?",
                "options": [
                    "1/5 (0.20, since 16 / 80 = 1/5)",
                    "1/4",
                    "1/10",
                    "16/18"
                ],
                "answer": 0,
                "hint": "Compute total rectangle area 10 × 8 = 80 m², then divide favourable circle area 16 m² by 80 m²!",
                "explanation": "Geometric P = Favourable Area / Total Area = 16 / 80 = 1/5 = 0.20."
            },
            {
                "question": "If two pens are drawn WITHOUT replacement from a pouch holding 3 Red and 2 Blue pens, how many total pens remain in the denominator for Stage 2 of the tree diagram?",
                "options": [
                    "4 pens remaining (since the 1st drawn pen was NOT put back)",
                    "5 pens remaining",
                    "3 pens remaining",
                    "6 pens remaining"
                ],
                "answer": 0,
                "hint": "'Without replacement' permanently removes 1 pen before the second pick!",
                "explanation": "Removing 1 pen without replacing drops the total available count from 5 to 4 for Stage 2."
            }
        ]
    },
    {
        "id": 16,
        "title": "Probability Synthesis Matrix",
        "subtitle": "Chapter Summary: Probability Range [0,1], Experimental vs Theoretical, Sample Spaces, Subsets, Complements & Trees",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your master Chapter Seven synthesis uniting every concept, formula, and pitfall in elementary probability! "
            "Lock down all four core pillars permanently! Pillar One—THE PROBABILITY SCALE AND RANDOMNESS: random experiments reveal their entire possible outcome set beforehand while keeping individual trial results uncertain; every valid probability obeys zero less than or equal to P of E less than or equal to one, spanning impossible zero, even-chance zero point five, and certain one! "
            "Pillar Two—EXPERIMENTAL VERSUS THEORETICAL: experimental relative frequency divides observed occurrences by total physical trials (honoring ancient Jñān-Chaupad heritage), whereas theoretical probability divides favourable counts by total outcomes STRICTLY under equally likely fairness! Remember the Law of Large Numbers stabilizes long-run frequencies toward theory, while the Gambler's Fallacy wrongly claims independent coins remember previous streaks! "
            "Pillar Three—SAMPLE SPACES AND SUBSET EVENTS: sample space S lists all distinct elementary outcomes cleanly (with total size n of S), event E is any subset inside S, and complement P of not-E equals one minus P of E! Pillar Four—TREE DIAGRAMS organize sequential multi-step random experiments cleanly via branch multiplication and leaf summation! Now challenge yourself confidently across all four silent mastery quiz slides right below!"
        ),
        "checkpoints": [
            {
                "question": "Which summary table accurately connects all four core probability formulas from Chapter 7?",
                "options": [
                    "Range: 0 ≤ P(E) ≤ 1; Exp P = occurrences / trials; Theo P = favourable / total (equally likely); Complement P(not E) = 1 − P(E)",
                    "Range: −1 ≤ P(E) ≤ 1; Complement P(not E) = 1 + P(E)",
                    "Theo P applies even when spinner angles differ widely",
                    "Gambler's Fallacy proves coins balance themselves after 5 Heads"
                ],
                "answer": 0,
                "hint": "Check bounds [0, 1], complementary sum = 1, and equal-likelihood requirement!",
                "explanation": "All four formulas—bounds [0,1], empirical relative frequency, fair theoretical ratio, and complement 1 − P(E)—are strictly accurate."
            },
            {
                "question": "A fair spinner has 5 equal 72° sectors numbered 1 to 5. What is P(rolling/spinning a number ≤ 5) and P(number > 5)?",
                "options": [
                    "P(≤ 5) = 1 (Certain event) and P(> 5) = 0 (Impossible event)",
                    "P(≤ 5) = 4/5 and P(> 5) = 1/5",
                    "Both equal 0.5",
                    "P(≤ 5) = 5 and P(> 5) = 0"
                ],
                "answer": 0,
                "hint": "Every sector in S = {1,2,3,4,5} satisfies ≤ 5, and zero sectors satisfy > 5!",
                "explanation": "E₁ = S gives certainty P = 5/5 = 1; E₂ = ∅ gives impossibility P = 0/5 = 0."
            }
        ]
    }
]

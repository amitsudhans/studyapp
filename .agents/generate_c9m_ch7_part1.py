#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 7: The Mathematics of Maybe: Introduction to Probability
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 7.1 to 7.2.2 with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Probability Likelihood Basics",
        "subtitle": "Section 7.1 What is Probability?: Objective Measurement of Likelihood & Everyday Random Events (Weather, Sports & Draws)",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Seven: The Mathematics of Maybe—Introduction to Probability! "
            "Every single day, people look up at dark monsoon clouds wondering whether heavy rain will interrupt evening cricket, or wait anxiously as a referee flips a shiny brass coin before a tournament match, or draw sealed numbered coupons from a raffle bowl during a community fair! Notice how words like probably, likely, fifty-fifty chance, and almost certain appear naturally across daily conversation! "
            "Yet in Section Seven Point One, mathematics transforms vague guesswork into exact quantitative precision! PROBABILITY is an objective numerical measurement expressing how confident or likely it is that a specific uncertain random event will occur! Instead of shrugging and guessing wildly on intuition alone, probability assigns a crisp clear fraction or decimal comparing competing possibilities cleanly and fairly! "
            "Inspect everyday random events carefully! Why can analysts NOT guarantee tomorrow afternoon's exact winning cricket score, lottery ticket winner, or sudden evening cloudburst? Because real-world situations combine countless shifting physical factors and genuine chance! Mathematics does not predict individual coin flips magically—rather, probability empowers meteorologists, doctors, engineers, and planners to measure likelihood accurately and make smarter evidence-based decisions even under deep uncertainty!"
        ),
        "checkpoints": [
            {
                "question": "In mathematics, what does probability primarily provide for an uncertain event?",
                "options": [
                    "An objective numerical measure of how likely or confident we are that the event will occur",
                    "A guaranteed prediction of the exact single future outcome",
                    "A way to change physical weather or force a coin to land heads",
                    "Only a list of past historical dates with no numbers"
                ],
                "answer": 0,
                "hint": "Probability replaces vague guesses like 'maybe' with an exact numerical degree of likelihood!",
                "explanation": "Probability objectively quantifies the likelihood of an uncertain event occurring using clear numbers."
            },
            {
                "question": "Which everyday situation directly involves an uncertain random outcome measured by probability?",
                "options": [
                    "Forecasting whether rain will fall tomorrow or drawing a random coupon from a shuffled box",
                    "Adding 15 + 25 on a standard calculator",
                    "Counting how many minutes make one hour",
                    "Finding the perimeter of a 5 cm × 5 cm square"
                ],
                "answer": 0,
                "hint": "Pick the scenario whose result cannot be known for certain beforehand!",
                "explanation": "Weather rain chances and lucky draws depend on chance and are genuinely uncertain before occurring."
            }
        ]
    },
    {
        "id": 2,
        "title": "Randomness Unknown Outcomes",
        "subtitle": "Section 7.1.1 What is Randomness?: Random Experiments, Known Outcome Pools & Complex Physical Sensitivity in Rainfall",
        "speech": (
            "Explore what the word RANDOM actually means mathematically inside Section Seven Point One Point One! "
            "In casual conversation, people often call weird unexpected surprises random—yet probability science gives randomness a crystal-sharp formal definition! Consider tossing one balanced metallic coin or rolling one six-sided numbered die cleanly across a smooth wooden desk! Before rolling, do we already know the COMPLETE list of all possible results? YES! A standard coin MUST land Heads or Tails; a standard cubic die MUST display one, two, three, four, five, or six! "
            "Yet can anyone predict with certainty BEFOREHAND which exact upward face will appear on the very next toss? NO! An action is called a RANDOM EXPERIMENT whenever all possible outcomes are completely known in advance, the action can be repeated endlessly under matching conditions, yet each individual trial's exact single outcome stays unpredictable! "
            "Now apply this concept to nature! Why is tomorrow's afternoon rainfall mathematically random even with weather satellites orbiting overhead? Because atmospheric systems depend exquisitely on millions of shifting air currents, microscopic dust particles, ocean surface temperatures, and barometric pressure gradients! Tiny invisible nudges cascade rapidly into rain or clear sunshine—making exact deterministic single-moment forecasting practically impossible!"
        ),
        "checkpoints": [
            {
                "question": "What two essential features define a RANDOM EXPERIMENT in probability?",
                "options": [
                    "All possible outcomes are known beforehand, yet the exact result of an individual trial cannot be predicted in advance",
                    "Nobody knows any possible outcomes and the experiment can never be repeated",
                    "Every trial produces the exact same forced outcome",
                    "Outcomes can only be words, never numbers"
                ],
                "answer": 0,
                "hint": "Think about rolling a 6-sided die: you know {1,2,3,4,5,6}, yet not what the next roll shows!",
                "explanation": "Random experiments have a known set of possible outcomes while individual trial results remain unpredictable."
            },
            {
                "question": "Why are atmospheric events like rainfall treated mathematically as random events?",
                "options": [
                    "They depend sensitively on vast interacting physical factors like temperature, pressure, wind currents, and humidity",
                    "Because weather instruments always switch numbers randomly on purpose",
                    "Because rain never follows any scientific laws of physics",
                    "Because clouds only appear on weekends"
                ],
                "answer": 0,
                "hint": "Recall Section 7.1.1: extreme sensitivity to many complex physical factors creates unpredictability!",
                "explanation": "Atmospheric complexity makes rainfall acutely sensitive to tiny initial changes, preventing deterministic long-range certainty."
            }
        ]
    },
    {
        "id": 3,
        "title": "Zero One Scale",
        "subtitle": "Section 7.1.2 The Probability Scale: Impossible (0), Even Chance (0.5), Certain (1) & 6-Card Purple/Green Visual Model",
        "speech": (
            "Where on the number line do ALL valid probability values live? Discover Section Seven Point One Point Two: THE PROBABILITY SCALE! "
            "Every probability value sits strictly between ZERO and ONE inclusive—written neatly as ZERO LESS THAN OR EQUAL TO P OF E LESS THAN OR EQUAL TO ONE! Zero sits at the far left endpoint marking an IMPOSSIBLE EVENT that can NEVER occur under any trial whatsoever! One sits at the far right endpoint marking a CERTAIN EVENT completely guaranteed to happen on EVERY single trial! Sitting strictly halfway at zero point five (or fifty percent) marks an EVEN CHANCE—equally likely to occur or fail! "
            "Test this continuous scale vividly using a SIX-CARD DECK MODEL holding changing mixes of purple and green cards! If ALL six cards are solid green and ZERO are purple, blindly drawing one purple card holds probability zero over six equals ZERO—completely IMPOSSIBLE! Swap one green card for one purple card: probability climbs to one-sixth! With THREE purple and THREE green cards, probability lands cleanly at three-sixths equals ZERO POINT FIVE—perfect even chance! Swap ALL six cards into purple: probability reaches six-sixths equals ONE—one hundred percent CERTAIN on every single draw!"
        ),
        "checkpoints": [
            {
                "question": "A sealed pouch contains 6 green cards and 0 purple cards. What is the probability of drawing a purple card on one blind pick?",
                "options": [
                    "0 (Impossible event)",
                    "1/6",
                    "0.5 (Even chance)",
                    "1 (Certain event)"
                ],
                "answer": 0,
                "hint": "Count how many purple cards exist inside the 6-card pouch!",
                "explanation": "Zero favourable cards out of 6 gives probability 0/6 = 0, an impossible event."
            },
            {
                "question": "Which number can NEVER represent a valid probability of any event E?",
                "options": [
                    "1.25 (or any value greater than 1 or less than 0)",
                    "0.0",
                    "0.5",
                    "1.0"
                ],
                "answer": 0,
                "hint": "Check the strict boundary rule 0 ≤ P(E) ≤ 1!",
                "explanation": "Probabilities must always stay inside [0, 1]; values above 1 (like 1.25) or negative numbers are invalid."
            }
        ]
    },
    {
        "id": 4,
        "title": "Two Probability Approaches",
        "subtitle": "Section 7.2 Measuring Probability Objectively: Dual Framework Comparing Experimental Trials vs Theoretical Symmetry",
        "speech": (
            "How do mathematicians, scientists, and data engineers actually CALCULATE reliable probability numbers instead of guessing loosely by gut feeling? Section Seven Point Two unveils TWO COMPLEMENTARY OBJECTIVE APPROACHES! "
            "Approach One is EXPERIMENTAL PROBABILITY (frequently called Empirical Probability)—grounded directly in hands-on physical observation, repeated practical testing, and real recorded data! Imagine testing whether an unevenly weighted wooden spinning top or an irregular plastic bottle cap lands upright more often than resting sideways! No ideal geometric symmetry formula works reliably on an odd-shaped plastic bottle cap—you MUST physically toss it dozens or hundreds of times, tally every observed result honestly, and measure relative frequency! "
            "Approach Two is THEORETICAL PROBABILITY—powered purely by logical structure, ideal fairness, and symmetrical reasoning BEFORE running even a single physical trial! When inspecting a flat symmetric coin, a balanced six-faced cubic die, or a thoroughly shuffled standard card deck, geometric symmetry guarantees every elementary outcome stands an equal fair chance! Without tossing anything, pure counting calculates exact theoretical probability effortlessly! "
            "Throughout Chapter Seven, discover how repeated physical trials and pure symmetrical mathematical theory reinforce each other seamlessly across scientific experiments—real empirical testing uncovers physical fairness or hidden bias, while theoretical reasoning delivers exact benchmarks before any experiment even starts!"
        ),
        "checkpoints": [
            {
                "question": "Which approach is most appropriate for estimating the chance that an irregularly shaped plastic bottle cap lands open-side UP?",
                "options": [
                    "Experimental (empirical) probability by tossing it repeatedly and recording observed outcomes",
                    "Theoretical probability assuming 50-50 symmetry automatically",
                    "Assuming probability is always 1",
                    "Measuring its outer perimeter"
                ],
                "answer": 0,
                "hint": "An asymmetric bottle cap does NOT have physically symmetric equally likely faces!",
                "explanation": "Because faces of a bottle cap lack symmetry, experimental relative frequency over many trials is required."
            },
            {
                "question": "Why can theoretical probability evaluate a balanced six-sided die directly without performing physical rolls first?",
                "options": [
                    "Because geometric symmetry guarantees all 6 faces are fair and equally likely under ideal conditions",
                    "Because dice always land on 6 first",
                    "Because theoretical probability ignores sample sizes",
                    "Because experimental probability only works for weather"
                ],
                "answer": 0,
                "hint": "Compare symmetry on a perfect cube versus asymmetric real objects!",
                "explanation": "Ideal cube symmetry makes each face equally likely (1/6), allowing direct theoretical counting."
            }
        ]
    },
    {
        "id": 5,
        "title": "Experimental Frequency Trials",
        "subtitle": "Section 7.2.1 Experimental Probability: Relative Frequency Formula & Historical Origins of Jñān-Chaupad (Snakes & Ladders)",
        "speech": (
            "Now master the exact calculation engine inside Section Seven Point Two Point One: EXPERIMENTAL PROBABILITY! "
            "Whenever a scientist, sports analyst, or researcher executes a repeatable experiment N total times and observes desired event E occurring f distinct times, its experimental probability equals: NUMBER OF TIMES EVENT OCCURRED DIVIDED BY TOTAL NUMBER OF TRIALS! Mathematicians name this observed data fraction RELATIVE FREQUENCY! "
            "Test an immediate quick calculation cleanly! Suppose an automated classroom spinner completes sixty independent spins, and twenty-four spins stop cleanly inside prime-numbered sectors! Experimental probability equals twenty-four divided by sixty—simplifying neatly to two-fifths or zero point four zero! Notice experimental probability always depends strictly upon the actual data recorded inside THAT particular test run: repeat another sixty spins, and observed relative frequency might wobble naturally to zero point four three or zero point three seven! "
            "Celebrate a remarkable Indian historical heritage spotlight inside this section too! Long centuries before modern commercial Snakes and Ladders boards spread worldwide, ancient Indian scholars taught ethics, karma, and probability concepts through JÑĀN-CHAUPAD (the traditional Indian Board of Knowledge)! Players rolled cowrie shells or cubical dice—turning random experimental throws into memorable life lessons about rising ladders and descending snakes!"
        ),
        "checkpoints": [
            {
                "question": "A spinning pointer is spun 80 times in an experiment and stops in the gold sector 28 times. What is the experimental probability of landing on gold?",
                "options": [
                    "7/20 (0.35, from 28/80)",
                    "28/52",
                    "1/4",
                    "80/28"
                ],
                "answer": 0,
                "hint": "Divide favourable observed occurrences (28) by total trials (80) and simplify by 4!",
                "explanation": "Experimental P(gold) = 28 / 80 = 7 / 20 = 0.35."
            },
            {
                "question": "Which ancient Indian board game used dice/shell rolls to teach moral cause-and-chance lessons and inspired modern Snakes and Ladders?",
                "options": [
                    "Jñān-Chaupad",
                    "Sulbasūtra Grid",
                    "Ptolemy Chords",
                    "Pascal Triangle"
                ],
                "answer": 0,
                "hint": "Meaning 'Board of Knowledge' (Jñān = knowledge, Chaupad = dice game board)!",
                "explanation": "Jñān-Chaupad originated in ancient India, combining chance throws with upward virtue ladders and downward snake slips."
            }
        ]
    },
    {
        "id": 6,
        "title": "Theoretical Probability Formula",
        "subtitle": "Section 7.2.2 Theoretical Probability: Equally Likely Outcomes Ratio, Fair Dice & Picking Letters from 'PROBABILITY'",
        "speech": (
            "Step directly into crystal-clear counting logic inside Section Seven Point Two Point Two: THEORETICAL PROBABILITY! "
            "Whenever a random experiment occurs under ideal, fair, unbiased conditions—so EVERY possible basic outcome shares the exact same likelihood—theoretical probability requires ZERO tedious repeated trials! Simply count two clear finite sets: THEORETICAL PROBABILITY OF EVENT E EQUALS NUMBER OF FAVOURABLE OUTCOMES DIVIDED BY TOTAL NUMBER OF POSSIBLE OUTCOMES! "
            "Apply this golden formula immediately across two classic textbook examples! Example One—Fair Die Throws: rolling a balanced cubic die displays six equally likely faces numbered one through six! Want the probability of rolling an even face (two, four, or six)? Three favourable faces over six total gives three-sixths equals ONE-HALF! Want a multiple of three (three or six)? Two over six equals ONE-THIRD! Want an odd face greater than one (three or five)? Two over six equals ONE-THIRD! "
            "Example Two—Picking Letter Cards from the eleven-letter word P-R-O-B-A-B-I-L-I-T-Y flipped face-down across a wooden classroom table! Count carefully: out of eleven letter slips total, how many carry letter B? TWO distinct slips! How many carry vowels (O, A, I, I)? FOUR slips total! So theoretical probability of picking letter B equals two-elevenths, and vowels equal four-elevenths!"
        ),
        "checkpoints": [
            {
                "question": "All 11 letters of the word PROBABILITY are written on identical slips and placed in a hat. What is the theoretical probability of picking the letter 'I'?",
                "options": [
                    "2/11",
                    "1/11",
                    "4/11",
                    "1/9"
                ],
                "answer": 0,
                "hint": "Count total letters in P-R-O-B-A-B-I-L-I-T-Y (11) and count how many are 'I'!",
                "explanation": "Out of 11 total letter slips, 'I' appears twice ⇒ P(I) = 2/11."
            },
            {
                "question": "On a single throw of a fair 6-sided die, what is the theoretical probability of getting a prime number?",
                "options": [
                    "1/2 (primes 2, 3, 5 give 3/6)",
                    "1/3 (only 3 and 5)",
                    "2/3 (1, 2, 3, 5)",
                    "1/6"
                ],
                "answer": 0,
                "hint": "Remember 1 is neither prime nor composite; the primes on {1..6} are 2, 3, and 5!",
                "explanation": "Primes on a standard die are {2, 3, 5} (3 outcomes out of 6) ⇒ P(prime) = 3/6 = 1/2."
            }
        ]
    },
    {
        "id": 7,
        "title": "Equally Likely Fairness",
        "subtitle": "Section 7.2.2 Crucial Condition Check: Recognizing Equally Likely Outcomes vs Unfairly Weighted or Unequal Sectors",
        "speech": (
            "Hold on right there! Pause carefully before dividing favourable outcome counts blindly by total outcome counts—always inspect the GOLDEN GUARDRAIL inside Section Seven Point Two Point Two! "
            "Theoretical formula Favourable Divided By Total ONLY remains mathematically valid when all elementary outcomes are genuinely EQUALLY LIKELY! Wait—what guarantees outcomes are equally likely, and how can sneaky diagrams fool hasty calculators? "
            "Compare TWO circular spinners side by side! Spinner A slices a circular disc cleanly into FOUR congruent ninety-degree sectors painted Red, Blue, Green, and Yellow! Every color commands identical twenty-five percent angular space—truly EQUALLY LIKELY at one-fourth each! "
            "Now inspect sneaky Spinner B: it ALSO displays Red, Blue, Green, and Yellow sectors—four distinct named colors! Yet Red spans a massive ONE HUNDRED EIGHTY degree semicircle, Blue spans ninety degrees, while Green and Yellow squeeze into narrow forty-five degree wedges! If anyone ignores sector geometry and claims Red holds probability one-fourth, that answer is COMPLETELY WRONG! Red covers HALF the circle—exact probability ONE-HALF, while Green claims just one-eighth! "
            "Similarly, biased weighted dice, bent metal coins rolled sideways, uneven lottery tickets, or unbalanced drawing pins violate symmetry completely—never count unequal labels blindly; ALWAYS verify physical symmetry and equal likelihood across elementary outcomes FIRST!"
        ),
        "checkpoints": [
            {
                "question": "A spinner has 3 regions: Red (180° half-circle), Blue (90° quarter), and Green (90° quarter). Why is P(Red) NOT equal to 1/3?",
                "options": [
                    "Because the sectors have unequal areas/angles, so the 3 outcomes are NOT equally likely (P(Red) = 180/360 = 1/2)",
                    "Because Red is always skipped on spinners",
                    "Because 1/3 is greater than 1",
                    "Because spinners only measure experimental probability"
                ],
                "answer": 0,
                "hint": "Compare the central angles (180°, 90°, 90°): equal outcomes require equal area fractions!",
                "explanation": "Outcome Red occupies half the circle (180°/360° = 1/2), whereas Blue and Green occupy 1/4 each."
            },
            {
                "question": "Which scenario strictly satisfies the 'equally likely elementary outcomes' condition?",
                "options": [
                    "Drawing one ball blindly from a thoroughly mixed bag of 5 identical-sized numbered balls",
                    "A basketball player shooting a free throw from half-court (make vs rebound)",
                    "Tossing a drawing pin to see whether it lands point-up or flat",
                    "Predicting whether an earthquake occurs tomorrow"
                ],
                "answer": 0,
                "hint": "Physical uniformity and symmetry among balls ensure no single ball is favored!",
                "explanation": "Identical mixed numbered balls have equal physical symmetry (1/5 each); shots, pins, and quakes do not."
            }
        ]
    },
    {
        "id": 8,
        "title": "Sampling Statistical Data",
        "subtitle": "Section 7.2.3 Analysing Statistical Data: Market Research, Population Forecasting (50-Student Sample to 1,500) & Fairness",
        "speech": (
            "Now step straight into real-world business forecasting, market research, and campus logistics inside Section Seven Point Two Point Three: ANALYSING STATISTICAL DATA USING PROBABILITY! "
            "Why do supermarket chains, factory planners, and school cafeterias depend daily upon experimental probability? Because polling every single customer across an entire mega-city or large campus demands excessive time, labor, and money! Instead, data analysts survey a carefully chosen REPRESENTATIVE RANDOM SAMPLE and scale experimental probabilities proportionally to forecast the full population accurately! "
            "Trace a crisp campus fruit-planning example step by step! Suppose a large school cafeteria feeds ONE THOUSAND FIVE HUNDRED total students daily, yet surveys a clean random sample of FIFTY students regarding favorite afternoon snacks! Inside that fifty-student sample, TWENTY select bananas, FIFTEEN pick crisp apples, TEN choose sweet mangoes, and FIVE want fresh oranges! "
            "Convert each preference cleanly into observed experimental relative frequency: bananas earn twenty divided by fifty equals zero point four zero (forty percent)! Now scale intelligently across ALL fifteen hundred students: zero point four zero times fifteen hundred equals SIX HUNDRED BANANAS ordered smartly each school day—preventing wasteful canteen fruit spoilage while satisfying daily student nutritional demand accurately, economically, and reliably without sampling bias!"
        ),
        "checkpoints": [
            {
                "question": "In a random sample survey of 50 students out of a school of 1,500 students, 15 preferred apples. Approximately how many apples should the canteen plan for all 1,500 students?",
                "options": [
                    "450 apples (since 15/50 = 0.30 and 0.30 × 1,500 = 450)",
                    "150 apples",
                    "300 apples",
                    "750 apples"
                ],
                "answer": 0,
                "hint": "Compute experimental probability 15/50 = 3/10, then multiply by full school population 1,500!",
                "explanation": "Sample proportion = 15/50 = 30%. Applying 30% to 1,500 gives 0.30 × 1,500 = 450 students."
            },
            {
                "question": "Why must the 50-student sample be chosen RANDOMLY across all grades rather than asking only one sports team?",
                "options": [
                    "To ensure the sample stays unbiased and fairly represents the entire 1,500-student population",
                    "Because sports teams eat zero fruit",
                    "To force every fruit probability to equal 1/4",
                    "To reduce total school population to 50"
                ],
                "answer": 0,
                "hint": "Sampling one narrow group introduces systematic bias!",
                "explanation": "Random representative sampling prevents bias so sample frequencies accurately mirror population preferences."
            }
        ]
    }
]

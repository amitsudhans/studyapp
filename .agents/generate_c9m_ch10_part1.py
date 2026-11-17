#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 10: How Quantities Combine: Understanding Data
Part 1: Slides 1 to 8 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Combining Quantities Framework",
        "subtitle": "Section 10.1 Combining Things: Extending Arithmetic Mean to Weighted Averages",
        "speech": (
            "Welcome to Chapter Ten: How Quantities Combine: Understanding Data! Every day, scientists, economists, teachers, and engineers combine separate datasets into one meaningful summary number! "
            "Recall how you already compute a simple arithmetic mean: add all individual values together and divide by the total count! That works cleanly when every single observation carries equal importance or comes from a single uniform group! "
            "However, real-world data rarely arrives in equal-sized boxes! Suppose you want to combine two cricket teams' batting averages, blend two sugar-water solutions of different volumes, or compute a final course grade where exams count twice as much as class projects! Simply adding two summary numbers and dividing by two often produces a completely wrong answer! "
            "Inside Section Ten Point One, we generalize the ordinary average into a powerful, universal mathematical framework called the WEIGHTED AVERAGE! Each value x sub i gets multiplied by its own non-negative weight W sub i—representing group size, physical mass, volume, or relative importance—before dividing by the sum of all weights! Whenever all weights are equal, this formula shrinks right back into the familiar ordinary average! Understanding weights prevents misleading statistics across science, finance, sports analytics, and public policy decisions every single day!"
        ),
        "checkpoints": [
            {
                "question": "When does a weighted average reduce to the exact same value as a simple arithmetic mean?",
                "options": [
                    "Whenever all weights W₁, W₂, ..., Wₙ are strictly equal to one another",
                    "Whenever all data values xᵢ are negative",
                    "Whenever there are more than 10 data points",
                    "Never — weighted averages always differ from simple means"
                ],
                "answer": 0,
                "hint": "Plug W₁ = W₂ = ... = Wₙ = W into (W·x₁ + ... + W·xₙ) / (n·W)!",
                "explanation": "Factoring out equal weight W gives W(x₁ + ... + xₙ) / (nW) = (x₁ + ... + xₙ)/n, the ordinary arithmetic mean."
            },
            {
                "question": "What can a 'weight' Wᵢ represent in a weighted average calculation?",
                "options": [
                    "Group size, physical quantity (mass/volume), or relative importance (such as exam percentage weight)",
                    "Only physical mass measured in kilograms",
                    "Only the largest number in the dataset",
                    "Only negative integers"
                ],
                "answer": 0,
                "hint": "Think across Sections 10.1.1 (group size), 10.1.2 (mixtures), and 10.1.3 (custom importance weights)!",
                "explanation": "Weights can represent sample counts, physical quantities in mixtures, or abstract importance scores."
            }
        ]
    },
    {
        "id": 2,
        "title": "Average Of Averages",
        "subtitle": "Section 10.1.1 Average of Averages: Why Unequal Group Sizes Break Simple Averaging",
        "speech": (
            "Uncover one of the most common statistical blunders in everyday life inside Section Ten Point One Point One: TAKING THE AVERAGE OF AVERAGES! "
            "Test this through a sports academy height example! Suppose Group A has four basketball players with an average height of one hundred eighty centimetres, while Group B has sixteen junior gymnasts with an average height of one hundred forty centimetres! "
            "If someone carelessly averages the two group averages—one hundred eighty plus one hundred forty divided by two—they get ONE HUNDRED SIXTY centimetres! Wait a second! Does that make sense when Group B has FOUR TIMES as many athletes pulling the combined height downward? "
            "Check the true combined average! Total height of Group A equals four times one hundred eighty equals seven hundred twenty centimetres! Total height of Group B equals sixteen times one hundred forty equals two thousand two hundred forty centimetres! Combine all twenty athletes: two thousand nine hundred sixty divided by twenty equals ONE HUNDRED FORTY-EIGHT centimetres—twelve centimetres lower than the naive guess! "
            "The exact same trap strikes cycling duration averages across unequal ride days: the larger group ALWAYS pulls the combined average closer toward itself in exact proportion to its group size!"
        ),
        "checkpoints": [
            {
                "question": "Group A (4 players) averages 180 cm and Group B (16 players) averages 140 cm. Why is the true combined average (148 cm) much closer to 140 cm than to 160 cm?",
                "options": [
                    "Because Group B has 16 players versus only 4 in Group A, so Group B's larger size gives its average 4× more weight",
                    "Because 140 is an even number",
                    "Because 180 cm players are ignored",
                    "Because averages always round down"
                ],
                "answer": 0,
                "hint": "Compare total sum: 4(180) + 16(140) divided by 20!",
                "explanation": "Group B contributes 16/20 = 80% of the total count, pulling the combined mean 80% of the way from 180 toward 140 (148 cm)."
            },
            {
                "question": "A cyclist rides 3 hours/day for 2 days, then 1 hour/day for 6 days. What is the true average daily cycling duration?",
                "options": [
                    "1.5 hours/day ((3×2 + 1×6) / 8 = 12 / 8)",
                    "2.0 hours/day ((3 + 1) / 2)",
                    "4.0 hours/day",
                    "1.0 hour/day"
                ],
                "answer": 0,
                "hint": "Divide total cycling hours (6 + 6 = 12) by total days (2 + 6 = 8)!",
                "explanation": "Total hours = 3(2) + 1(6) = 12 hours across 2 + 6 = 8 days, giving 12/8 = 1.5 hours/day."
            }
        ]
    },
    {
        "id": 3,
        "title": "Combined Average Formula",
        "subtitle": "Section 10.1.1 General Formulation: (an + bm)/(n + m) & When Simple Averaging Holds",
        "speech": (
            "Now formalize Section Ten Point One Point One into an exact algebraic theorem! "
            "Suppose Collection One contains n items with arithmetic average a, and Collection Two contains m items with arithmetic average b! What is the sum of all items inside Collection One? Since average equals sum divided by count, Sum One equals a TIMES n! Similarly, Sum Two equals b TIMES m! "
            "Now merge both collections into one big pool of n plus m items! The combined sum equals a n plus b m, so the true COMBINED AVERAGE is EXACTLY a n plus b m, ALL DIVIDED BY n plus m! "
            "Now ask an essential algebraic question: WHEN does this true combined average equal the naive simple average open a plus b close divided by two? Set the two fractions equal and cross-multiply! Two a n plus two b m equals a n plus a m plus b n plus b m! Rearranging terms cleanly gives open a minus b close TIMES open n minus m close EQUALS ZERO! "
            "Therefore, taking the simple average of two averages works ONLY in two situations: either both collections have the EXACT SAME SIZE (n equals m), OR both collections already have the EXACT SAME AVERAGE (a equals b)!"
        ),
        "checkpoints": [
            {
                "question": "If Section A has n = 20 students averaging a = 75% and Section B has m = 30 students averaging b = 85%, what is the combined average?",
                "options": [
                    "81% ((75×20 + 85×30) / 50 = 4050 / 50)",
                    "80% ((75 + 85) / 2)",
                    "82%",
                    "79%"
                ],
                "answer": 0,
                "hint": "Use the combined average formula (an + bm) / (n + m)!",
                "explanation": "(75×20 + 85×30)/(20 + 30) = (1500 + 2550)/50 = 4050/50 = 81%."
            },
            {
                "question": "Under what exact condition does (an + bm)/(n + m) equal (a + b)/2?",
                "options": [
                    "When n = m (equal group sizes) OR a = b (equal group averages)",
                    "Whenever a + b is even",
                    "Whenever n > m",
                    "Whenever a > 0 and b > 0"
                ],
                "answer": 0,
                "hint": "Cross-multiplying simplifies to (a − b)(n − m) = 0!",
                "explanation": "(a − b)(n − m) = 0 holds if and only if a = b or n = m."
            }
        ]
    },
    {
        "id": 4,
        "title": "Mixtures Concentration Law",
        "subtitle": "Section 10.1.2 Mixtures: Blending Lemonade, Fertilizers & Solutions by Weighted Mean",
        "speech": (
            "See weighted averages come alive inside chemistry, farming, and kitchens in Section Ten Point One Point Two: MIXTURES AND CONCENTRATION CALCULATIONS! "
            "Suppose you mix two jugs of lemon-sugar drink! Jug One holds two litres at ten percent sugar concentration, and Jug Two holds three litres at twenty percent sugar concentration! What is the sugar percentage of the combined five-litre pitcher? "
            "Never average ten percent and twenty percent to guess fifteen percent—the volumes differ! Compute total pure sugar first! Jug One supplies ten percent of two litres equals zero point two litres of sugar! Jug Two supplies twenty percent of three litres equals zero point six litres of sugar! Total sugar equals zero point eight litres inside five total litres, yielding SIXTEEN PERCENT concentration! "
            "Notice that exact same formula—open two times ten plus three times twenty close divided by open two plus three close—is the COMBINED WEIGHTED AVERAGE where the physical volumes act as weights! Whether blending two fertilizers with different nitrogen percentages or mixing two milk-water batches of unequal litres, concentration ALWAYS obeys the weighted average by volume or mass! Even diluting with pure water works cleanly by treating water as zero percent concentration weighted by its poured volume!"
        ),
        "checkpoints": [
            {
                "question": "You mix 4 kg of fertilizer containing 15% nitrogen with 6 kg of fertilizer containing 25% nitrogen. What is the nitrogen percentage of the 10 kg mixture?",
                "options": [
                    "21% ((4×15 + 6×25) / 10 = 210 / 10)",
                    "20% ((15 + 25) / 2)",
                    "22%",
                    "19%"
                ],
                "answer": 0,
                "hint": "Weight each concentration by its mass in kilograms: (4×15 + 6×25) / (4 + 6)!",
                "explanation": "Total nitrogen = 0.60 + 1.50 = 2.10 kg out of 10 kg total, giving 21% nitrogen."
            },
            {
                "question": "If 3 L of pure water (0% salt) is poured into 2 L of 25% salt solution, what is the resulting salt concentration?",
                "options": [
                    "10% ((3×0 + 2×25) / 5 = 50 / 5)",
                    "12.5%",
                    "15%",
                    "25%"
                ],
                "answer": 0,
                "hint": "Pure water has 0% salt concentration and weight 3 L!",
                "explanation": "Total salt = 0 + 0.5 L in 5 L total = 10%."
            }
        ]
    },
    {
        "id": 5,
        "title": "Gold Alloy Purity",
        "subtitle": "Section 10.1.2 Historical Contributions: Brahmagupta & Śrīdharācārya Varna/Karat Alloy Formulas",
        "speech": (
            "Celebrate India's ancient mathematical mastery of weighted averages inside Section Ten Point One Point Two: GOLD ALLOY PURITY! "
            "Over a thousand years ago, classical Indian mathematicians BRAHMAGUPTA in his seventh-century masterpiece Brāhmasphuṭasiddhānta and ŚRĪDHARĀCĀRYA in his tenth-century treatise Pātīganita solved practical goldsmithing problems! When merchants melted together several gold bars of different weights and purities—measured in VARNA (modern KARATS, where twenty-four karat is pure gold)—how could they compute the exact purity of the melted ingot without re-assaying it? "
            "They stated the exact weighted average rule in verse! Multiply each gold piece's weight W sub i by its varna or karat purity k sub i, sum all those products together, and divide by the sum of all piece weights! "
            "Test Brahmagupta's formula right now! Melt ten grams of eighteen-karat gold together with twenty grams of twenty-four-karat pure gold! Compute: ten times eighteen equals one hundred eighty, plus twenty times twenty-four equals four hundred eighty! Total six hundred sixty divided by thirty total grams equals TWENTY-TWO KARATS! Ancient Indian commerce ran on this exact weighted mean law! Whether combining two ingots or five different gold ornaments, dividing total pure gold content by total alloy mass always yields the exact resulting karat!"
        ),
        "checkpoints": [
            {
                "question": "A goldsmith melts 10 g of 18-karat gold with 20 g of 24-karat gold. Using Brahmagupta's / Śrīdharācārya's rule, what is the purity of the combined 30 g alloy?",
                "options": [
                    "22 karats ((10×18 + 20×24) / 30 = 660 / 30)",
                    "21 karats ((18 + 24) / 2)",
                    "23 karats",
                    "20 karats"
                ],
                "answer": 0,
                "hint": "Compute (W₁k₁ + W₂k₂) / (W₁ + W₂)!",
                "explanation": "(10×18 + 20×24) / (10 + 20) = (180 + 480) / 30 = 660 / 30 = 22 karats."
            },
            {
                "question": "Which two classical Indian mathematical texts presented systematic alloy purity (varna/karat) weighted-average rules?",
                "options": [
                    "Brahmagupta's Brāhmasphuṭasiddhānta and Śrīdharācārya's Pātīganita",
                    "Euclid's Elements and Fibonacci's Liber Abaci",
                    "Newton's Principia and Euler's Introductio",
                    "Only 20th-century statistics textbooks"
                ],
                "answer": 0,
                "hint": "Both works come from classical Indian mathematics (7th and 10th centuries CE)!",
                "explanation": "Brahmagupta (Brāhmasphuṭasiddhānta) and Śrīdharācārya (Pātīganita) formulated varna/karat alloy weighted means."
            }
        ]
    },
    {
        "id": 6,
        "title": "Weighted Mean Formula",
        "subtitle": "Section 10.1.2 General Weighted Mean: x̄ = (W₁x₁ + W₂x₂ + ... + Wₙxₙ) / (W₁ + W₂ + ... + Wₙ)",
        "speech": (
            "Now unite all previous cases—group averages, liquid mixtures, and gold alloys—into ONE single master equation in Section Ten Point One Point Two: THE GENERAL WEIGHTED MEAN FORMULA! "
            "Whenever you have n values x one, x two, up to x sub n, carrying corresponding non-negative weights W one, W two, up to W sub n (with total weight positive), the weighted mean x-bar equals W one x one plus W two x two plus dot-dot-dot plus W sub n x sub n, ALL DIVIDED BY W one plus W two plus dot-dot-dot plus W sub n! "
            "Notice two super-handy properties of this formula! First, if you multiply EVERY weight by the same positive scaling factor—say converting all weights from grams to kilograms, or turning ratios three-to-two into percentages sixty percent and forty percent—the weighted mean stays COMPLETELY UNCHANGED because the common factor cancels cleanly from numerator and denominator! "
            "Second, the weighted mean ALWAYS lies strictly between the smallest data value and the largest data value! If every value in a mixture lies between ten and thirty, no combination of positive weights can ever push the weighted average below ten or above thirty—it always stays strictly bounded inside the data range!"
        ),
        "checkpoints": [
            {
                "question": "Compute the weighted mean of values x = (10, 20, 30) with weights W = (2, 3, 5).",
                "options": [
                    "23 ((2×10 + 3×20 + 5×30) / (2 + 3 + 5) = 230 / 10)",
                    "20 ((10 + 20 + 30) / 3)",
                    "25",
                    "18"
                ],
                "answer": 0,
                "hint": "Multiply each xᵢ by its weight Wᵢ, sum them, and divide by 2 + 3 + 5 = 10!",
                "explanation": "(20 + 60 + 150) / 10 = 230 / 10 = 23."
            },
            {
                "question": "If all weights (2, 3, 5) are doubled to (4, 6, 10) while keeping values (10, 20, 30) unchanged, what happens to the weighted mean?",
                "options": [
                    "It remains exactly 23 (scaling all weights by a positive constant cancels out)",
                    "It doubles to 46",
                    "It halves to 11.5",
                    "It increases by 2"
                ],
                "answer": 0,
                "hint": "Factor 2 out of both the numerator and denominator!",
                "explanation": "(4×10 + 6×20 + 10×30)/(4+6+10) = 460/20 = 23 — only relative proportions of weights matter."
            }
        ]
    },
    {
        "id": 7,
        "title": "Custom Academic Weights",
        "subtitle": "Section 10.1.3 Custom Weights: Grading Ratios (Internals, Projects, Final Exams)",
        "speech": (
            "Now step beyond physical counts and masses into Section Ten Point One Point Three: CUSTOM WEIGHTS FOR RELATIVE IMPORTANCE! "
            "In schools, universities, sports rankings, and business scorecards, weights often represent CHOSEN IMPORTANCE rather than physical quantity! "
            "Take a realistic school assessment system! Suppose a mathematics course evaluates three components out of one hundred marks each: Internal Tests weighted twenty percent, Class Projects weighted thirty percent, and the Final Examination weighted fifty percent! Notice how the total weights add neatly to one hundred percent! "
            "Compare two students! Student One scores ninety on Internals, eighty on Projects, and sixty on the Final Exam! Simple average would give seventy-six point seven! Yet weighted average computes: zero point two times ninety (eighteen) plus zero point three times eighty (twenty-four) plus zero point five times sixty (thirty), totaling SEVENTY-TWO percent! "
            "Meanwhile, Student Two scores sixty on Internals, seventy on Projects, and ninety on the Final Exam: zero point two times sixty (twelve) plus zero point three times seventy (twenty-one) plus zero point five times ninety (forty-five) equals SEVENTY-EIGHT percent! Because the Final Exam carries half the total weight, strong final performance boosts the weighted score dramatically compared to giving every small quiz equal weight!"
        ),
        "checkpoints": [
            {
                "question": "A course weights Homework 20%, Project 30%, and Final Exam 50%. If a student scores 80, 90, and 70 respectively, what is the weighted final score?",
                "options": [
                    "78% (0.20×80 + 0.30×90 + 0.50×70 = 16 + 27 + 35)",
                    "80% ((80 + 90 + 70) / 3)",
                    "75%",
                    "82%"
                ],
                "answer": 0,
                "hint": "Multiply each score by 0.20, 0.30, and 0.50 and add!",
                "explanation": "16 + 27 + 35 = 78%."
            },
            {
                "question": "Why might a school assign weight 50% to the Final Exam and 20% to Homework instead of equal 33.3% weights?",
                "options": [
                    "To reflect the higher relative importance of comprehensive supervised exam mastery over short homework tasks",
                    "Because percentages must always equal 50",
                    "Because simple averages cannot be calculated for three numbers",
                    "To make every student's score lower"
                ],
                "answer": 0,
                "hint": "Think about Section 10.1.3: weights encode relative importance!",
                "explanation": "Custom weights let educators prioritize high-stakes cumulative assessments over smaller assignments."
            }
        ]
    },
    {
        "id": 8,
        "title": "Ratings Recency Weights",
        "subtitle": "Section 10.1.3 Custom Weights: Hotel/Restaurant Ratings & Product Review Recency Weighting",
        "speech": (
            "Custom weights also power the apps and websites you use daily inside Section Ten Point One Point Three: HOTEL RATINGS AND PRODUCT REVIEW RECENCY! "
            "Suppose a restaurant review platform scores Food Quality out of five, Service out of five, and Ambience out of five! Most diners care far more about delicious food than fancy wall lighting—so a rating engine assigns custom weights: Food five, Service three, Ambience two! If a restaurant earns four point eight for Food, four point zero for Service, and three point zero for Ambience, its weighted rating equals open five times four point eight plus three times four point zero plus two times three point zero close divided by ten, giving FOUR POINT TWO stars! "
            "Now think about online product reviews over time! Suppose a phone had software bugs two years ago earning two-star reviews, yet after major updates this month it earns five-star reviews! If a store gives equal weight to old and new reviews, the outdated complaints drag down the rating! By assigning HIGHER RECENCY WEIGHTS to newer reviews (for example, weight three for this month, weight two for last quarter, weight one for older years), the weighted score reflects current quality accurately!"
        ),
        "checkpoints": [
            {
                "question": "A hotel scores Food = 4.5 (weight 5), Service = 4.0 (weight 3), Ambience = 3.5 (weight 2). What is its weighted rating?",
                "options": [
                    "4.15 ((5×4.5 + 3×4.0 + 2×3.5) / 10 = 41.5 / 10)",
                    "4.00 ((4.5 + 4.0 + 3.5) / 3)",
                    "4.30",
                    "3.95"
                ],
                "answer": 0,
                "hint": "Sum (5×4.5 + 3×4.0 + 2×3.5) and divide by total weight 5 + 3 + 2 = 10!",
                "explanation": "(22.5 + 12.0 + 7.0) / 10 = 41.5 / 10 = 4.15."
            },
            {
                "question": "Why do e-commerce platforms often apply RECENCY WEIGHTING to product reviews?",
                "options": [
                    "To give newer reviews more influence so the rating reflects the product's current quality and recent updates",
                    "To delete all old reviews completely",
                    "Because older reviews always have 5 stars",
                    "To make all products average 3.0"
                ],
                "answer": 0,
                "hint": "Products change over time via software updates or manufacturing revisions!",
                "explanation": "Recency weights prioritize fresh customer feedback while still retaining historical context."
            }
        ]
    }
]

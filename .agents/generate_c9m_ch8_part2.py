#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 8.5 to 8.6.2, Exercises & Summary with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Natural Sum Gauss",
        "subtitle": "Section 8.5 Sum of First n Natural Numbers: Gauss Reversal Pairing Method Deriving Sₙ = n(n + 1) / 2",
        "speech": (
            "Discover one of the most celebrated clever shortcuts in mathematical history inside Section Eight Point Five: SUMMING THE FIRST n NATURAL NUMBERS! "
            "Legend tells how young Carl Friedrich Gauss stunned his schoolteacher in seconds when asked to add EVERY whole number from one straight up to one hundred! Instead of plodding laboriously one plus two plus three, watch Gauss's ingenious REVERSAL PAIRING trick! "
            "Write sum S sub n twice—once going forward from one up to n, and directly underneath going backward from n down to one! Now add EVERY vertical column straight down! Column one adds one plus n equals n plus one! Column two adds two plus open n minus one close—ALSO equals n plus one! Every single one of the n columns sums identically to n PLUS ONE! "
            "Therefore, adding BOTH rows gives TWO TIMES S sub n equals n TIMES open n plus one close! Dividing cleanly by two unlocks our famous universal formula: S sub n EQUALS n TIMES open n plus one close DIVIDED BY TWO! For n equals one hundred: one hundred times one hundred one divided by two equals FIFTY TIMES ONE HUNDRED ONE equals FIVE THOUSAND FIFTY!"
        ),
        "checkpoints": [
            {
                "question": "Using Gauss's formula Sₙ = n(n + 1)/2, what is the exact sum 1 + 2 + 3 + ... + 100?",
                "options": ["5,050", "5,000", "10,100", "4,950"],
                "answer": 0,
                "hint": "Evaluate 100 × 101 / 2!",
                "explanation": "S₁₀₀ = 100 × (100 + 1) / 2 = 50 × 101 = 5,050."
            },
            {
                "question": "Why does pairing Sₙ forward with Sₙ backward divide by 2 at the final step?",
                "options": [
                    "Because adding the sequence forward plus backward counts the desired sum Sₙ TWICE (giving 2·Sₙ = n(n+1))",
                    "Because half the numbers are negative",
                    "Because only even numbers are counted",
                    "Because n is always even"
                ],
                "answer": 0,
                "hint": "Two identical copies of Sₙ were added vertically!",
                "explanation": "Sₙ + Sₙ = 2Sₙ = n(n + 1), so dividing by 2 isolates a single copy Sₙ = n(n + 1)/2."
            }
        ]
    },
    {
        "id": 10,
        "title": "Āryabhaṭa Grid Sums",
        "subtitle": "Section 8.5 Historical Context & Visual Proof: Āryabhaṭīya (499 CE), Pictorial Grid Proof & Arbitrary Range Sums",
        "speech": (
            "Long before European schoolrooms heard of Gauss, fifth-century Indian astronomer-mathematician ĀRYABHAṬA recorded this exact triangular sum rule inside his masterpiece the ĀRYABHAṬĪYA in four hundred ninety-nine CE! Moreover, Section Eight Point Five reveals a dazzling PICTORIAL GRID PROOF showing WHY S sub n equals n times open n plus one close divided by two visually! "
            "Stack dots forming the nth triangular staircase—one dot on row one, two on row two, up to n dots on row n! Now clone an identical upside-down staircase of dots and snap BOTH staircases smoothly together! Look at the combined grid: it forms an exact solid RECTANGLE measuring height n rows by width n plus one columns, holding n times open n plus one close total dots! Since one staircase equals HALF that rectangle, S sub n equals half of n times open n plus one close! "
            "Need an ARBITRARY consecutive integer range like twenty-one plus twenty-two straight up to sixty? Simply subtract! Compute S sixty minus S twenty: sixty times sixty-one over two minus twenty times twenty-one over two equals eighteen hundred thirty minus two hundred ten equals ONE THOUSAND SIX HUNDRED TWENTY effortlessly in just two clean subtraction steps!"
        ),
        "checkpoints": [
            {
                "question": "In the pictorial grid proof of Sₙ = n(n + 1)/2, what exact rectangle dimensions form when two congruent n-staircases interlock?",
                "options": [
                    "Height n rows by width (n + 1) columns, holding n(n + 1) total dots",
                    "Height n by width n (n² dots)",
                    "Height 2n by width n",
                    "Height (n − 1) by width (n + 1)"
                ],
                "answer": 0,
                "hint": "Top row combines 1 dot + n dots = (n + 1) dots across n rows!",
                "explanation": "Two identical staircases fit together cleanly into an n × (n + 1) dot rectangle, so each staircase holds ½ n(n + 1) dots."
            },
            {
                "question": "Calculate the sum of consecutive integers 11 + 12 + 13 + ... + 30 using S₃₀ − S₁₀.",
                "options": ["410", "465", "355", "520"],
                "answer": 0,
                "hint": "Compute S₃₀ = 30×31/2 = 465 and subtract S₁₀ = 10×11/2 = 55!",
                "explanation": "S₃₀ − S₁₀ = 465 − 55 = 410."
            }
        ]
    },
    {
        "id": 11,
        "title": "Geometric Progression Basics",
        "subtitle": "Section 8.6 Geometric Progressions: Constant Multiplier Common Ratio (r) & General Form a, ar, ar², ...",
        "speech": (
            "Now shift smoothly from constant ADDITION to constant MULTIPLICATION inside Section Eight Point Six: GEOMETRIC PROGRESSIONS, abbreviated cleanly as GPs! "
            "Imagine bacteria inside a dish doubling every hour—one, two, four, eight, sixteen—or folding a paper sheet repeatedly so thickness multiplies by two each fold, or a savings fund multiplying by one point zero five annually! Subtracting consecutive terms here does NOT stay constant—instead, DIVIDING each term by its preceding term stays CONSTANT! "
            "A GEOMETRIC PROGRESSION is a sequence where every term after the first non-zero term a is produced by MULTIPLYING the previous term by a fixed constant factor called the COMMON RATIO r! Writing it out gives the classic general GP form: a, a r, a r squared, a r cubed, onward! "
            "Check all three faces of ratio r! When r exceeds one (like r equals three), terms explode upward rapidly! When r sits strictly between zero and one (like r equals one-half in sixty-four, thirty-two, sixteen, eight), terms decay smoothly toward zero! And when r is negative (like r equals negative two), consecutive terms alternate cleanly between positive and negative signs on every single multiplication step, swinging above and below zero across the number line!"
        ),
        "checkpoints": [
            {
                "question": "Identify the common ratio r of the Geometric Progression 81, 27, 9, 3, ...",
                "options": ["r = 1/3", "r = 3", "r = −54", "r = 1/9"],
                "answer": 0,
                "hint": "Divide any term by its immediately preceding term: t₂ / t₁ = 27 / 81!",
                "explanation": "27 / 81 = 9 / 27 = 3 / 9 = 1 / 3."
            },
            {
                "question": "What happens to a Geometric Progression with positive first term a > 0 when common ratio r is NEGATIVE (for example, a = 5, r = −2)?",
                "options": [
                    "The terms alternate signs between positive and negative (5, −10, 20, −40, ...)",
                    "All terms become zero immediately",
                    "It becomes an Arithmetic Progression",
                    "All terms stay strictly positive"
                ],
                "answer": 0,
                "hint": "Multiply 5 by −2 repeatedly and track the + / − signs!",
                "explanation": "Multiplying by a negative ratio flips the sign on every consecutive step."
            }
        ]
    },
    {
        "id": 12,
        "title": "GP Nth Term",
        "subtitle": "Section 8.6 GP Explicit Formula: tₙ = a·rⁿ⁻¹ & Recursive Formulation t₁ = a, tₙ = r · tₙ₋₁",
        "speech": (
            "Now lock down the exact algebraic formula for ANY term inside a Geometric Progression in Section Eight Point Six! "
            "Count carefully how many times first term a gets multiplied by common ratio r to reach position n! Term one multiplies ZERO factors of r: a times r to the zero equals a! Term two multiplies ONE factor: a r to the one! Term three multiplies TWO factors: a r squared! Term ten multiplies NINE factors: a r to the ninth! "
            "Spot the crystal-clear universal rule: the exponent on ratio r is ALWAYS ONE LESS than position n! That proves the GP explicit nth-term formula: t sub n EQUALS a TIMES r TO THE POWER open n minus one close! Meanwhile, its twin recursive form reads t one equals a and t sub n equals r TIMES t sub n minus one! "
            "Test it immediately! Suppose a viral educational video doubles views hourly starting at three views at hour one: first term a equals three, common ratio r equals two! How many views arrive at hour eight? Compute t eight equals three times two to the seventh equals three times one hundred twenty-eight equals THREE HUNDRED EIGHTY-FOUR views!"
        ),
        "checkpoints": [
            {
                "question": "Find the 6th term t₆ of the Geometric Progression 5, 10, 20, 40, ...",
                "options": ["160", "320", "80", "25"],
                "answer": 0,
                "hint": "Here a = 5, r = 2, and n = 6; remember exponent is n − 1 = 5!",
                "explanation": "t₆ = 5 × 2⁶⁻¹ = 5 × 2⁵ = 5 × 32 = 160."
            },
            {
                "question": "Why is the exponent in tₙ = a·rⁿ⁻¹ equal to (n − 1) rather than n?",
                "options": [
                    "Because the first term t₁ = a uses 0 multiplications by r, so the nth term uses (n − 1) multiplications",
                    "Because r is always negative",
                    "Because n starts at 0 instead of 1",
                    "Because Geometric Progressions skip the 1st term"
                ],
                "answer": 0,
                "hint": "Check n = 1: r¹⁻¹ = r⁰ = 1 leaves t₁ = a!",
                "explanation": "Starting at t₁ = a (zero factors of r) means reaching tₙ requires (n − 1) steps of multiplying by r."
            }
        ]
    },
    {
        "id": 13,
        "title": "Fractals Sierpiński Geometry",
        "subtitle": "Section 8.6.1 Fun with Fractals: Sierpiński Triangle & Carpet Exponential Counts (3ⁿ) & Shrinking Areas ((3/4)ⁿ)",
        "speech": (
            "Witness Geometric Progressions painting breathtaking infinite geometry inside Section Eight Point Six Point One: FUN WITH FRACTALS! "
            "Start with one solid black equilateral triangle at Stage Zero (area one unit squared)! At Stage One, connect midpoints of all three sides and cut out the central upside-down white triangle! How many smaller black triangles remain? THREE triangles, each carrying one-fourth area—leaving total remaining black area THREE-FOURTHS! "
            "Now repeat inside EVERY remaining black triangle at Stage Two: each of the three splits into three, creating THREE SQUARED equals NINE tiny black triangles, while remaining area shrinks cleanly to open three-fourths close SQUARED equals nine-sixteenths! At Stage n of the SIERPIŃSKI TRIANGLE, count explodes upward as a growing GP THREE TO THE POWER n, while total black area shrinks smoothly as a decaying GP open THREE-FOURTHS close TO THE POWER n! "
            "Even better, build the SIERPIŃSKI CARPET from a square divided into nine equal sub-squares with the center removed: remaining shaded sub-squares multiply rapidly by EIGHT to the power n while remaining shaded area shrinks cleanly toward zero as open EIGHT-NINTHS close to the power n—revealing the astonishing mathematical paradox of an infinitely long fractal boundary enclosing an area that shrinks steadily toward zero!"
        ),
        "checkpoints": [
            {
                "question": "At Stage 3 of the Sierpiński Triangle (starting from 1 unit² triangle at Stage 0), how many shaded sub-triangles exist and what total shaded area remains?",
                "options": [
                    "27 shaded triangles (3³), remaining area (3/4)³ = 27/64 unit²",
                    "9 shaded triangles, remaining area 9/16 unit²",
                    "81 shaded triangles, remaining area 1/64 unit²",
                    "12 shaded triangles, remaining area 1/4 unit²"
                ],
                "answer": 0,
                "hint": "Plug n = 3 into count GP = 3ⁿ and area GP = (3/4)ⁿ!",
                "explanation": "At Stage 3, 3³ = 27 sub-triangles remain, each of area (1/4)³, giving total shaded area (3/4)³ = 27/64."
            },
            {
                "question": "In the Sierpiński Carpet, a square is split into a 3×3 grid (9 equal sub-squares) and the central 1 sub-square is removed at each stage. What GP models remaining area at Stage n?",
                "options": [
                    "(8/9)ⁿ",
                    "(3/4)ⁿ",
                    "(1/9)ⁿ",
                    "8ⁿ"
                ],
                "answer": 0,
                "hint": "Removing 1 out of 9 sub-squares leaves 8/9 of the previous area at every stage!",
                "explanation": "Each stage multiplies remaining area by r = 8/9, yielding (8/9)ⁿ."
            }
        ]
    },
    {
        "id": 14,
        "title": "Exponential GP Curves",
        "subtitle": "Section 8.6.2 Visualising a GP: Non-Linear Exponential Graphs & Bouncing Ball Physics Decay Model",
        "speech": (
            "Compare graphs of Arithmetic versus Geometric Progressions side by side inside Section Eight Point Six Point Two: VISUALISING A GP! "
            "Remember how plotting open n comma t sub n close for any AP traced a crisp ruler-straight line? Now plot open n comma t sub n close for GP two, four, eight, sixteen, thirty-two! At first, jumps look gentle (two, then four), yet quickly rocket skyward (eight, sixteen, thirty-two, sixty-four)! Connecting those plotted dots forms a sweeping NON-LINEAR EXPONENTIAL CURVE bending dramatically upward (for r greater than one) or curving smoothly downward toward zero (for r between zero and one)! "
            "Apply decaying GPs straight to real-world physics with the classic BOUNCING BALL PROBLEM! Drop an elastic rubber ball from initial height H zero equals sixteen metres onto a hard concrete floor! Suppose on every single bounce it rebounds strictly to THREE-FOURTHS of its immediately previous height (common ratio r equals zero point seven five)! "
            "Bounce one rises to twelve metres; bounce two rises to nine metres; bounce three reaches six point seven five metres! Notice consecutive rebound heights follow an exact decaying GP: sixteen times open three-fourths close to the power n—gradually shrinking steadily toward rest!"
        ),
        "checkpoints": [
            {
                "question": "How does the coordinate graph (n, tₙ) of a Geometric Progression with r = 2 fundamentally differ from an Arithmetic Progression with d = 2?",
                "options": [
                    "The GP traces a rapidly curving non-linear exponential curve, whereas the AP lies on a straight line",
                    "The GP lies on a horizontal flat line",
                    "Both AP and GP trace identical straight lines",
                    "The GP curves straight downward below zero"
                ],
                "answer": 0,
                "hint": "Multiplying by 2 causes vertical steps to double each turn rather than stay equal!",
                "explanation": "Constant multiplication creates exponential curvature, unlike constant addition which creates linear slope."
            },
            {
                "question": "A ball is dropped from 80 cm and rebounds to 1/2 of its previous height on each bounce. What height does it reach after the 4th bounce?",
                "options": [
                    "5 cm (80 × (1/2)⁴)",
                    "10 cm",
                    "20 cm",
                    "2.5 cm"
                ],
                "answer": 0,
                "hint": "Track bounces: Bounce 1 = 40, Bounce 2 = 20, Bounce 3 = 10, Bounce 4 = ...!",
                "explanation": "After n bounces, height = 80 × (1/2)ⁿ; at n = 4, 80 / 16 = 5 cm."
            }
        ]
    },
    {
        "id": 15,
        "title": "Progression Problem Strategies",
        "subtitle": "Exercise Sets 8.1–8.3 & End-of-Chapter Strategies: Explicit/Recursive Conversions, Growth, Wages & Linear Systems",
        "speech": (
            "Master four high-scoring problem-solving strategies across Exercise Sets Eight Point One, Eight Point Two, Eight Point Three, and End-of-Chapter Challenges! "
            "Strategy One—EXPLICIT-TO-RECURSIVE CONVERSION: given explicit AP t sub n equals five n minus two, compute t one equals three and inspect coefficient five as common difference d—instantly writing recursive rule t one equals three, t sub n equals t sub n minus one plus five! "
            "Strategy Two—SOLVING AP LINEAR SYSTEMS: told t three equals eleven and t seven equals twenty-three? Write BOTH equations cleanly: a plus two d equals eleven and a plus six d equals twenty-three! Subtracting cancels a immediately: four d equals twelve gives d equals three, and substituting back unlocks a equals five! "
            "Strategy Three—WAGE INCREMENTS AND POPULATION GROWTH: fixed constant annual raises (like plus five hundred rupees every year) model APs cleanly, whereas compound percentage growth (like plus ten percent annually, common ratio r equals one point one zero) or bacterial cell doubling models GPs! Strategy Four—always verify whether consecutive ratios t two over t one equal t three over t two before assuming a sequence is a GP—and remember that any non-zero constant sequence satisfies BOTH AP with d equals zero AND GP with r equals one simultaneously!"
        ),
        "checkpoints": [
            {
                "question": "In an Arithmetic Progression, t₃ = 14 and t₇ = 30. What are the first term a and common difference d?",
                "options": [
                    "a = 6 and d = 4",
                    "a = 4 and d = 6",
                    "a = 10 and d = 4",
                    "a = 2 and d = 6"
                ],
                "answer": 0,
                "hint": "Subtract (a + 6d) − (a + 2d) = 30 − 14 ⇒ 4d = 16!",
                "explanation": "4d = 16 ⇒ d = 4; substituting into a + 2(4) = 14 gives a = 6."
            },
            {
                "question": "A bacterium colony starts with 200 cells and triples every hour. Which formula gives cell count after n hours (t₀ = 200, or 1st hour = 600)?",
                "options": [
                    "GP with ratio r = 3: tₙ = 200 × 3ⁿ (after n hours)",
                    "AP with d = 3: tₙ = 200 + 3n",
                    "AP with d = 600",
                    "Triangular sum n(n+1)/2"
                ],
                "answer": 0,
                "hint": "'Triples every hour' means multiplying by 3 repeatedly (constant ratio r = 3)!",
                "explanation": "Repeated multiplication by 3 defines a Geometric Progression with common ratio r = 3."
            }
        ]
    },
    {
        "id": 16,
        "title": "Sequences Synthesis Matrix",
        "subtitle": "Chapter Summary: Sequences, Explicit & Recursive Rules, Triangular Sums, AP (a, d), GP (a, r) & Fractals",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your complete Chapter Eight synthesis unifying every sequence, progression, and fractal formula! "
            "Review all four grand pillars clearly! Pillar One—SEQUENCES AND RULES: ordered term lists t one, t two, t three can be finite or infinite; EXPLICIT formulas compute t sub n directly from position n (enabling instant jumps to t three hundred and membership checks), while RECURSIVE rules build from preceding terms using anchor values—celebrating India's seventh-century Virahānka-Fibonacci sequence! "
            "Pillar Two—ARITHMETIC PROGRESSIONS AND SUMS: adding constant difference d creates AP t sub n equals a plus open n minus one close d whose graph open n comma t sub n close is strictly LINEAR! Gauss's pairing and Āryabhaṭa's rectangular dot grid prove sum of first n naturals equals n times open n plus one close over two! "
            "Pillar Three—GEOMETRIC PROGRESSIONS AND SELF-SIMILAR FRACTALS: multiplying by constant common ratio r yields GP explicit formula t sub n equals a r to the power n minus one, tracing EXPONENTIAL curves, modeling bouncing ball physics, and powering Sierpiński fractals (three to the n shaded count, three-fourths to the n remaining area)! Now challenge yourself confidently across all four silent mastery quiz slides right below!"
        ),
        "checkpoints": [
            {
                "question": "Which comparison table accurately summarizes Arithmetic vs Geometric Progressions?",
                "options": [
                    "AP: constant difference d, tₙ = a + (n−1)d, linear graph | GP: constant ratio r, tₙ = a·rⁿ⁻¹, exponential graph",
                    "AP: constant ratio r, exponential graph | GP: constant difference d, linear graph",
                    "Both AP and GP have linear graphs (n, tₙ)",
                    "AP sum of first n naturals = n²; GP nth term = a + rⁿ"
                ],
                "answer": 0,
                "hint": "Check operation (add d vs multiply r), formula, and graph shape!",
                "explanation": "AP uses constant addition d (linear), whereas GP uses constant multiplication r (exponential)."
            },
            {
                "question": "Match these historical Indian breakthroughs from Chapter 8 cleanly: Virahānka (7th c. CE) and Āryabhaṭa (499 CE).",
                "options": [
                    "Virahānka: Vₙ = Vₙ₋₁ + Vₙ₋₂ from poetic meters; Āryabhaṭa: Sₙ = n(n + 1)/2 in the Āryabhaṭīya",
                    "Virahānka: Sierpiński carpet; Āryabhaṭa: bouncing ball GP",
                    "Both invented only negative numbers",
                    "Virahānka: tₙ = a + (n−1)d; Āryabhaṭa: common ratio r"
                ],
                "answer": 0,
                "hint": "Check Sections 8.3 and 8.5!",
                "explanation": "Virahānka formulated Vₙ = Vₙ₋₁ + Vₙ₋₂ in prosody, and Āryabhaṭa stated the natural number sum formula in 499 CE."
            }
        ]
    }
]

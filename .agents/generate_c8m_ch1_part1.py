#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 1: A Square and A Cube
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
        "title": "Hundred Lockers Puzzle",
        "subtitle": "Introductory Puzzle: 100 Lockers Toggled by 100 Visitors — Why Only Square Numbers Stay Open!",
        "speech": (
            "Welcome to NCERT Class Eight Chapter One: A Square and A Cube! Begin with our thrilling Introductory Lockers Puzzle! "
            "Imagine one hundred closed treasure lockers numbered one to one hundred along a grand palace corridor! Visitor One walks past and toggles EVERY locker (1, 2, 3, ..., 100) open! Visitor Two toggles multiples of TWO (2, 4, 6, ...), closing them! Visitor Three toggles multiples of THREE! This alternating pattern continues all the way until Visitor One Hundred toggles ONLY locker 100! "
            "Which exact locker numbers remain OPEN at the very end? Notice every locker starts CLOSED! Toggling it an EVEN number of times brings it right back CLOSED! Only lockers toggled an ODD number of times end OPEN! "
            "When does a number have an ODD number of factors? Normally factors come in neat pairs, like twelve having (1,12), (2,6), (3,4) equals 6 factors! Prime lockers like seven have ONLY two factors (1 and 7), toggled strictly twice, ending CLOSED! Only PERFECT SQUARES like thirty six hold a self-partnered factor (6 × 6 = 36), giving an ODD total count of factors! Exact open lockers: 1, 4, 9, 16, 25, 36, 49, 64, 81, and 100!"
        ),
        "checkpoints": [
            {
                "question": "In the 100 Lockers puzzle (all starting CLOSED), which locker numbers remain OPEN after all 100 people toggle their multiples?",
                "options": [
                    "Only Perfect Square numbers {1, 4, 9, 16, 25, 36, 49, 64, 81, 100} because they have an ODD number of factors",
                    "Only Prime numbers {2, 3, 5, 7, ...}",
                    "Only Even numbers {2, 4, 6, ...}",
                    "Only Multiples of 10"
                ],
                "answer": 0,
                "hint": "Closed → Open requires an ODD number of toggles, meaning an ODD count of factors (due to self-partnered √n)!",
                "explanation": "Factors normally pair up evenly except when n = k², leaving k self-partnered and an odd factor count."
            },
            {
                "question": "Exactly how many times is a PRIME locker number (like Locker 29 or 53) toggled during the 100-visitor walk, and what is its final state?",
                "options": [
                    "Toggled exactly 2 times (by Visitor 1 and itself) → Ends CLOSED",
                    "Toggled 1 time → Ends OPEN",
                    "Toggled 3 times → Ends OPEN",
                    "Toggled 4 times → Ends CLOSED"
                ],
                "answer": 0,
                "hint": "A prime number p has exactly two positive factors: 1 and p!",
                "explanation": "Visitor 1 opens prime locker p, and Visitor p closes it (2 toggles = CLOSED)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Square Number Meaning",
        "subtitle": "Section 1.1 Foundations: Geometric Area Model (n² = n × n), Perfect Squares & Fraction/Decimal Squares",
        "speech": (
            "Now step directly into Section One Point One: Square Numbers! Why do mathematicians across the entire world call n multiplied by n a SQUARE number? "
            "Picture laying tiny unit square floor tiles side by side cleanly! Arrange a neat grid 3 tiles wide and 3 tiles tall: 3 × 3 = 9 tiles form a crisp geometric square! Arrange 4 rows of 4 tiles: 4 × 4 = 16 tiles! Geometrically, n squared (written n²) literally measures the planar AREA of a square of side length n! "
            "Whenever n is a NATURAL counting number (1, 2, 3, 4, 5, ...), its square n² equals 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 and onward, and is called a PERFECT SQUARE! Memorize all perfect squares cleanly up to 20² = 400! "
            "Notice you can ALSO square fractional and decimal side lengths cleanly! A square tile of side three fourths (3/4) has exact area (3/4) × (3/4) = 9/16! A square tile of side 1.5 cm has area 1.5 × 1.5 = 2.25 cm²! Always count decimal places very carefully when squaring 0.4: 0.4 × 0.4 equals exact 0.16 (TWO decimal places, never mistakenly 1.6)!"
        ),
        "checkpoints": [
            {
                "question": "If a square paper sheet has side length 0.7 cm, what is its exact area (0.7)²?",
                "options": [
                    "0.49 cm²",
                    "4.9 cm²",
                    "1.4 cm²",
                    "0.049 cm²"
                ],
                "answer": 0,
                "hint": "7 × 7 = 49, and squaring one decimal place creates TWO decimal places!",
                "explanation": "0.7 × 0.7 = 0.49 cm²."
            },
            {
                "question": "Which list shows ONLY the first five Perfect Squares (squares of natural numbers 1 to 5)?",
                "options": [
                    "1, 4, 9, 16, 25",
                    "2, 4, 6, 8, 10",
                    "1, 8, 27, 64, 125",
                    "1, 3, 6, 10, 15"
                ],
                "answer": 0,
                "hint": "Compute 1², 2², 3², 4², 5²!",
                "explanation": "1² = 1, 2² = 4, 3² = 9, 4² = 16, 5² = 25."
            }
        ]
    },
    {
        "id": 3,
        "title": "Units Digit Rules",
        "subtitle": "Section 1.1 Patterns: Allowed Endings {0,1,4,5,6,9} vs Instant Rejection Digits {2,3,7,8}",
        "speech": (
            "Discover ONE super-fast detective trick in Section One Point One to reject fake squares in LESS THAN ONE SECOND without any long multiplication! Inspect the UNITS DIGIT (rightmost digit) of every integer square from 0² through 9²! "
            "Check each digit pair carefully: 0² ends in 0; 1² and 9² BOTH end in 1; 2² and 8² BOTH end in 4; 3² and 7² BOTH end in 9; 4² and 6² BOTH end in 6; and 5² ends in 5! "
            "Pause and marvel at the missing digits! Which units digits appear at the end of squares? ONLY SIX digits: 0, 1, 4, 5, 6, and 9! Which FOUR digits NEVER EVER appear at the end of ANY perfect square? Digits TWO, THREE, SEVEN, and EIGHT! "
            "Memorize that rejection code immediately: 2, 3, 7, 8! Whenever a huge integer like 7,928 or 1,057 or 453 ends in 2, 3, 7, or 8, decide immediately: NOT a perfect square! Remember this crucial exam caution: ending in 0, 1, 4, 5, 6, or 9 is NECESSARY yet never alone guarantees a true perfect square (for instance check 26 or 19)—and odd² stays always odd while even² stays always even!"
        ),
        "checkpoints": [
            {
                "question": "Which set lists ALL four units digits that can NEVER end ANY perfect square number?",
                "options": [
                    "{2, 3, 7, 8}",
                    "{1, 4, 6, 9}",
                    "{0, 1, 5, 6}",
                    "{2, 4, 6, 8}"
                ],
                "answer": 0,
                "hint": "Check endings of 0² through 9²: only 0, 1, 4, 5, 6, 9 appear!",
                "explanation": "No integer square can end in 2, 3, 7, or 8."
            },
            {
                "question": "If a natural number ends in the digit 6 (like 14² or 26²), or ends in 7 (like 37²), what units digits will their SQUARES end in respectively?",
                "options": [
                    "6 and 9   (since 6² = 36 and 7² = 49)",
                    "6 and 7",
                    "4 and 9",
                    "1 and 7"
                ],
                "answer": 0,
                "hint": "Square only the units digits cleanly: 6×6 = 36, 7×7 = 49!",
                "explanation": "Units digit of n² depends purely on units digit of n: 6² → 6, 7² → 9."
            }
        ]
    },
    {
        "id": 4,
        "title": "Trailing Zero Doubling",
        "subtitle": "Section 1.1 Zero Laws: Why Squares Always End in an EVEN Number of Zeros (e.g., 400 vs 4,000)",
        "speech": (
            "Now inspect trailing zeros at the end of square numbers! Watch closely what happens whenever you square natural numbers ending in zeros! "
            "Check single zero first: 10² equals 10 × 10 equals 100 (ONE trailing zero DOUBLES into TWO zeros)! Check 30² equals 900 (TWO zeros)! Next check TWO trailing zeros: 100² equals 100 × 100 equals 10,000 (TWO trailing zeros DOUBLE cleanly into FOUR zeros)! Check THREE trailing zeros: 2,000² equals 4,000,000 (THREE trailing zeros DOUBLE cleanly into SIX zeros)! "
            "Spot the ironclad mathematical law right away: squaring ANY integer ALWAYS DOUBLES its count of trailing zeros! Because 2 times any whole number is ALWAYS EVEN, EVERY perfect square ending in zeros MUST carry an EVEN number of trailing zeros (2, 4, 6, ...)! "
            "Therefore, whole numbers ending in ONE zero (such as 250), THREE zeros (such as 64,000), or FIVE zeros (such as 900,000) can NEVER be perfect squares! Also watch ONE subtle bonus board exam trap very carefully: inspect 1,200! Although 1,200 ends in TWO trailing zeros (which is even!), its remaining front digits 12 are NOT a perfect square, so BOTH even zeros AND a square front are always strictly needed!"
        ),
        "checkpoints": [
            {
                "question": "Why can NO perfect square ever end with exactly 3 trailing zeros (like 8,000 or 9,000)?",
                "options": [
                    "Because squaring always DOUBLES the count of trailing zeros, forcing perfect squares to have an EVEN count of trailing zeros",
                    "Because 10² equals 1,000",
                    "Because perfect squares never end in zeros at all",
                    "Because 3 divides 10"
                ],
                "answer": 0,
                "hint": "Count zeros when multiplying (a × 10ᵏ) × (a × 10ᵏ) = a² × 10^(2k)!",
                "explanation": "Every trailing zero in the root creates 2 trailing zeros in the square, making the count strictly even."
            },
            {
                "question": "Which number below IS a genuine Perfect Square?",
                "options": [
                    "19,600   [= 140², even 2 zeros AND front 196 = 14²!]",
                    "1,96,000",
                    "1,200",
                    "64,000"
                ],
                "answer": 0,
                "hint": "Check BOTH requirements: EVEN trailing zeros AND remaining front digits form a perfect square!",
                "explanation": "19,600 = 196 × 100 = 14² × 10² = 140², whereas 1,200 (12 not square) and 64,000 / 1,96,000 (odd 3 zeros) fail."
            }
        ]
    },
    {
        "id": 5,
        "title": "Consecutive Odd Sums",
        "subtitle": "Section 1.1 Odd-Sum Property: 1+3+5+... = n² (Gnomon Layers) & Successive Odd Subtraction Test",
        "speech": (
            "Witness one of the cleanest visual miracles in arithmetic inside Section One Point One: building squares directly out of CONSECUTIVE ODD NUMBERS! "
            "Start with 1 dot (1 = 1²)! Wrap an L-shaped corner layer of 3 dots around it: 1 + 3 = 4 = 2²! Wrap the next L-shaped corner of 5 dots around that 2×2 square: 1 + 3 + 5 = 9 = 3²! Wrap 7 dots: 1 + 3 + 5 + 7 = 16 = 4²! Always starting strictly from ONE, the sum of the FIRST n consecutive odd numbers ALWAYS equals EXACTLY n²! Test mentally: sum of first ten odd numbers equals 10² = 100! "
            "Now flip that exact miracle backward into the SUCCESSIVE SUBTRACTION METHOD to test whether a number (like 49 or 50) is a perfect square AND find its square root! Start at 49 and subtract odd numbers 1, 3, 5, ... step by step: 49 − 1 = 48, 48 − 3 = 45, −5 = 40, −7 = 33, −9 = 24, −11 = 13, 13 − 13 = ZERO cleanly in SEVEN steps! Since we hit EXACT ZERO, √49 = 7! Skipping past 0 (like 50 reaching −14) proves NOT a square!"
        ),
        "checkpoints": [
            {
                "question": "Without adding term by term, find the exact sum of the first 12 consecutive odd natural numbers: 1 + 3 + 5 + ... + 23:",
                "options": [
                    "144   (= 12²)",
                    "120",
                    "169",
                    "24"
                ],
                "answer": 0,
                "hint": "Sum of the first n odd numbers starting from 1 ALWAYS equals n²!",
                "explanation": "1 + 3 + 5 + ... + 23 has 12 odd terms, so Sum = 12² = 144."
            },
            {
                "question": "When testing whether 81 is a perfect square via Successive Subtraction (81 − 1, − 3, − 5, ...), at which step do you hit exact 0?",
                "options": [
                    "Step 9 (after subtracting 17 cleanly to reach 0 ⟹ √81 = 9)",
                    "Step 8 (after subtracting 15)",
                    "Step 10",
                    "Never hits exact zero"
                ],
                "answer": 0,
                "hint": "How many odd numbers starting from 1 sum to 81 = 9²?",
                "explanation": "Subtracting the 9 consecutive odd numbers 1,3,5,7,9,11,13,15,17 reduces 81 cleanly to 0, proving √81 = 9."
            }
        ]
    },
    {
        "id": 6,
        "title": "Triangular Number Sums",
        "subtitle": "Section 1.1: Adding Consecutive Triangular Numbers (Tₙ₋₁ + Tₙ = n²) & 2n Non-Squares Interval",
        "speech": (
            "Now uncover TWO gorgeous dot-geometry patterns inside Section One Point One: Triangular Number Sums and Non-Square Intervals! "
            "Recall Triangular Numbers formed by stacking rows of 1, 2, 3, 4 dots into neat staircases: T₁ = 1, T₂ = 1 + 2 = 3, T₃ = 1 + 2 + 3 = 6, T₄ = 10, T₅ = 15, T₆ = 21! Look closely what happens when you fit ANY two CONSECUTIVE triangular dot triangles diagonally edge to edge: T₁ + T₂ = 1 + 3 = 4 = 2²! T₂ + T₃ = 3 + 6 = 9 = 3²! T₃ + T₄ = 6 + 10 = 16 = 4²! T₄ + T₅ = 10 + 15 = 25 = 5²! Generally, Tₙ₋₁ + Tₙ ALWAYS equals n² cleanly! "
            "Also spot exactly how many non-square natural numbers sit strictly BETWEEN two consecutive squares n² and (n + 1)²! Expand (n + 1)² − n² = 2n + 1, then exclude upper endpoint square (n + 1)², leaving EXACTLY TWO n (2n) non-square natural integers cleanly! Example: between 9² (81) and 10² (100), count exact 2 × 9 equals EIGHTEEN non-square natural numbers (82 through 99)!"
        ),
        "checkpoints": [
            {
                "question": "Which two consecutive Triangular Numbers (from 1, 3, 6, 10, 15, 21, 28, ...) add together to form the square number 6² = 36?",
                "options": [
                    "15 + 21   (= T₅ + T₆)",
                    "10 + 26",
                    "12 + 24",
                    "10 + 15"
                ],
                "answer": 0,
                "hint": "Check T₅ = 1+2+3+4+5 = 15 and T₆ = 15 + 6 = 21!",
                "explanation": "T₅ + T₆ = 15 + 21 = 36 = 6²."
            },
            {
                "question": "How many natural (non-square) numbers lie strictly between 12² (144) and 13² (169)?",
                "options": [
                    "24   (= 2 × 12)",
                    "25",
                    "12",
                    "26"
                ],
                "answer": 0,
                "hint": "Between n² and (n+1)² lie exact 2n non-square natural numbers!",
                "explanation": "With n = 12, count = 2n = 2 × 12 = 24 numbers (145 to 168)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Square Roots Intro",
        "subtitle": "Section 1.1: Inverse Radical Notation (√y = x), Dual Roots (±x) vs Principal Root & Bounding Estimation",
        "speech": (
            "Now reverse the square operation! Finding the SQUARE ROOT is the inverse operation of squaring—just as subtraction undoes addition and division undoes multiplication cleanly! "
            "If x² equals y, then x is called a square root of y! Notice ONE subtle sign fact every Class Eight student must know: both (+5)² = 25 AND (−5)² = 25! So every positive perfect square mathematically possesses TWO integer roots: +x and −x! However, in Class Eight this principal radical symbol √y denotes ONLY the positive square root (for instance √25 = 5, √144 = 12, √169 = 13)! "
            "Watch how easily you can ESTIMATE square roots of unfamiliar four-digit squares using smart interval bounds BEFORE prime factoring! Suppose you suspect 529 is a perfect square! Check friendly tens landmarks first cleanly: 20² equals 400 and 30² equals 900! Since 529 sits cleanly right between 400 and 900, √529 MUST sit strictly between 20 and 30! Next check last digit 9: ONLY units digits 3 (meaning 23) or 7 (meaning 27) square cleanly to end in 9! Test 23 × 23 equals exact 529! Quick landmark bracketing plus last-digit filtering nails mental square roots fast, smoothly, accurately, and reliably every single time!"
        ),
        "checkpoints": [
            {
                "question": "Which statement correctly distinguishes all integer square roots of 49 versus the principal symbol √49?",
                "options": [
                    "49 has two integer roots (+7 and −7), while principal radical √49 denotes strictly +7",
                    "√49 equals both +7 and −7 simultaneously",
                    "Only −7 squared gives 49",
                    "√49 equals 24.5"
                ],
                "answer": 0,
                "hint": "(+7)² = 49 and (−7)² = 49, whereas √y signifies the positive square root in NCERT!",
                "explanation": "Every positive square has two roots (±x), while the symbol √y specifically denotes the non-negative root +x."
            },
            {
                "question": "Using interval estimation (tens landmarks + units digit filter), what is the exact value of √784?",
                "options": [
                    "28   (between 20²=400 and 30²=900; ends in 4 so 22 or 28; 28² = 784!)",
                    "22",
                    "26",
                    "32"
                ],
                "answer": 0,
                "hint": "25² = 625 < 784 < 900, so root > 25 and ends in 2 or 8!",
                "explanation": "784 > 25² (625) and ends in 4 (from 8² = 64), giving √784 = 28."
            }
        ]
    },
    {
        "id": 8,
        "title": "Prime Factor Pairing",
        "subtitle": "Section 1.1 Algorithm: Grouping Prime Factors in Pairs to Find √y & Smallest Multiplier/Divisor",
        "speech": (
            "When a square number grows too large for mental guessing, Prime Factorization gives an unbreakable 100 percent exact square-root machine! Why does this work every time? Because in any perfect square n², EVERY prime factor of n gets DOUBLED cleanly into balanced PAIRS! "
            "Follow THREE crisp steps on any square, say 324 or 1,764! Step One: Factorize completely down into primes: 324 = 2 × 2 × 3 × 3 × 3 × 3! Step Two: Group identical prime factors neatly into PAIRS: (2 × 2) × (3 × 3) × (3 × 3)! Step Three: Pull ONE prime out from each pair and multiply: √324 = 2 × 3 × 3 = EIGHTEEN! Test 1,764 = (2×2) × (3×3) × (7×7) ⟹ √1764 = 2 × 3 × 7 = FORTY TWO! "
            "Bonus Board Exam Classic! What if ONE prime factor gets left completely UNPAIRED without a partner inside the factorization, like 180 = (2×2) × (3×3) × 5? Notice lonely prime factor 5 lacks any partner! To repair 180 cleanly into a perfect square, either MULTIPLY by lonely factor 5 (giving 900 = 30²) OR DIVIDE away lonely factor 5 (giving 36 = 6²)!"
        ),
        "checkpoints": [
            {
                "question": "Given prime factorization 1,764 = 2 × 2 × 3 × 3 × 7 × 7, compute √1764 by grouping factors into pairs:",
                "options": [
                    "42   (= 2 × 3 × 7)",
                    "21",
                    "84",
                    "14"
                ],
                "answer": 0,
                "hint": "Take ONE prime factor from each pair: (2×2) → 2, (3×3) → 3, (7×7) → 7!",
                "explanation": "√1764 = 2 × 3 × 7 = 42."
            },
            {
                "question": "Factorize 252 = (2 × 2) × (3 × 3) × 7. What is the SMALLEST natural number by which 252 must be MULTIPLIED (or DIVIDED) to make it a perfect square?",
                "options": [
                    "7   (the lonely unpaired prime factor!)",
                    "2",
                    "3",
                    "6"
                ],
                "answer": 0,
                "hint": "Spot which prime factor has NO partner inside 252!",
                "explanation": "7 is unpaired: 252 × 7 = 1,764 (42²) and 252 ÷ 7 = 36 (6²)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch1 Class 8 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

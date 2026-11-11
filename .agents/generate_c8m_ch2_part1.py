#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 2: Power Play
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
        "title": "Paper Folding Power",
        "subtitle": "Section 2.1: Experiencing Multiplicative Growth (0.001 cm Paper Reaching Past the Moon in 46 Folds!)",
        "speech": (
            "Welcome to NCERT Class Eight Chapter Two: Power Play! Let us begin Section Two Point One with a mind-bending thought experiment: folding an ordinary thin sheet of paper! "
            "Imagine a large paper sheet just 0.001 centimeters thick—one hundredth of a millimeter! Fold it cleanly in half once: thickness DOUBLES to 0.002 cm! Fold twice: 0.004 cm! Fold ten times: multiplying 0.001 by two raised to ten (2¹⁰ = 1,024) turns thin paper into 1.024 centimeters—roughly a thick notebook! Remember that golden scaling law right away: EVERY ten additional folds multiplies paper thickness by factor ONE THOUSAND TWENTY FOUR (2¹⁰ = 1024)! "
            "Watch what happens as folding continues step by step! After TWENTY SIX folds, paper shoots up to 670 METERS tall—nearly matching the height of the world-famous Burj Khalifa skyscraper in Dubai! After THIRTY folds, thickness rockets to 10.7 KILOMETERS high—cruising right at passenger airplane cruising altitude! After FORTY SIX folds, paper surpasses SEVEN LAKH KILOMETERS—soaring completely PAST THE MOON at roughly 3,84,000 kilometers away! Repeated multiplicative growth explodes astonishingly faster than human intuition ever expects, proving clearly why exponential mathematics shapes modern astronomy, biology, computer science, modern banking finance, rocket physics, and vast cosmic space distances!"
        ),
        "checkpoints": [
            {
                "question": "If a sheet of paper is 0.001 cm thick and doubles with each fold, by what factor does thickness multiply after EVERY 10 folds?",
                "options": [
                    "1,024   (= 2¹⁰)",
                    "20",
                    "100",
                    "512"
                ],
                "answer": 0,
                "hint": "Multiply 2 by itself ten times: 2¹⁰!",
                "explanation": "2¹⁰ = 1,024, so every 10 folds scales thickness 1,024× (0.001 cm → 1.024 cm)."
            },
            {
                "question": "Approximately how many halving folds transform a 0.001 cm sheet of paper past airplane altitude (10.7 km) and past Moon distance (> 7,00,000 km)?",
                "options": [
                    "30 folds (10.7 km)   and   46 folds (> 7,00,000 km)",
                    "10 folds (10.7 km)   and   20 folds (Moon)",
                    "100 folds (10.7 km)   and   1,000 folds (Moon)",
                    "26 folds (Moon)"
                ],
                "answer": 0,
                "hint": "Recall 26 folds ≈ 670 m (Burj Khalifa), 30 folds ≈ 10.7 km, 46 folds > 7,00,000 km!",
                "explanation": "At 30 folds (2³⁰ × 0.001 cm) it reaches ~10.7 km; at 46 folds it exceeds 7,00,000 km (past the Moon)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Base And Exponent",
        "subtitle": "Section 2.2: Exponential Notation (nᵃ), Comparing nᵃ vs aⁿ & Prime Factorization Power Form",
        "speech": (
            "Now enter Section Two Point Two: Exponential Notation and Operations! Instead of writing exhausted multiplication chains like 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2, mathematicians invent crisp shorthand notation called EXPONENTIAL FORM: nᵃ (read carefully as 'n raised to the power a' or 'n to the exponent a')! "
            "Decode BOTH pieces cleanly right away! The bottom repeated factor n is called the BASE, and the small raised superscript a counting HOW MANY TIMES to multiply base n by itself is called the EXPONENT (or POWER)! Example: in 3⁵ = 3 × 3 × 3 × 3 × 3 = 243, base equals THREE and exponent equals FIVE! Be careful: NEVER swap base and exponent blindly—note 2⁵ equals 32, whereas 5² equals only 25! Only rare special pairs like 2⁴ = 4² = 16 ever tie! "
            "Exponential notation also packs giant prime factorizations cleanly into tiny compact labels! Factorize 32,400 smoothly into primes: four 2s, four 3s, and two 5s collapse directly into 2⁴ × 3⁴ × 5² cleanly! Likewise factor 1,000 easily into 2³ × 5³, or rewrite 729 neatly as 3⁶ in seconds!"
        ),
        "checkpoints": [
            {
                "question": "In the exponential expression 7⁴, identify the Base and Exponent, and compare 2⁵ vs 5²:",
                "options": [
                    "Base = 7, Exponent = 4;   and 2⁵ (32) > 5² (25)",
                    "Base = 4, Exponent = 7;   and 2⁵ = 5²",
                    "Base = 7, Exponent = 4;   and 2⁵ (10) = 5² (10)",
                    "Base = 28, Exponent = 1"
                ],
                "answer": 0,
                "hint": "Base is the bottom multiplied factor; exponent counts repetitions (never multiply base × exponent!).",
                "explanation": "7⁴ multiplies base 7 four times; 2⁵ = 32 is strictly larger than 5² = 25."
            },
            {
                "question": "Express 32,400 as a product of powers of its prime factors:",
                "options": [
                    "2⁴ × 3⁴ × 5²",
                    "2³ × 3⁴ × 5³",
                    "2² × 3⁵ × 5²",
                    "2⁴ × 3³ × 5²"
                ],
                "answer": 0,
                "hint": "Notice 32,400 = 324 × 100 = (18²) × (10²) = (2×3²)² × (2×5)²!",
                "explanation": "324 = 2² × 3⁴ and 100 = 2² × 5², multiplying together to exact 2⁴ × 3⁴ × 5²."
            }
        ]
    },
    {
        "id": 3,
        "title": "Product Base Rule",
        "subtitle": "Section 2.2 Puzzle ('The Stones That Shine') & Product Law With Same Base: nᵃ × nᵇ = nᵃ⁺ᵇ",
        "speech": (
            "Unlock our FIRST fundamental law of exponents from Section Two Point Two's luminous story puzzle, 'The Stones that Shine'—where glowing crystals double or triple brightness cleanly every single hour! Suppose glowing power multiplies by 3ᵃ during morning hours and multiplies again by 3ᵇ during afternoon hours! How many total 3s get multiplied altogether? "
            "Test concrete factor counts first: multiply 3² (= 3 × 3) by 3⁴ (= 3 × 3 × 3 × 3)! Count ALL repeated 3s lined up side by side cleanly: (3 × 3) × (3 × 3 × 3 × 3) equals SIX threes multiplied cleanly together = 3⁶! Notice two plus four equals six! "
            "Behold Law One, the Product Rule with Same Base: for ANY non-zero base n, multiplying powers KEEPS THE SAME BASE AND ADDS EXPONENTS cleanly: nᵃ × nᵇ equals n^(a+b)! "
            "Watch ONE classic exam mistake students repeatedly fall into! Product Rule works strictly ONLY for MULTIPLICATION, NEVER ADDITION! Check 2³ + 2⁴ equals 8 + 16 = 24 (NEVER 2⁷ = 128)! Always keep bases identical and operations strictly multiplicative whenever adding exponents together cleanly across multiple matching factors like 5³ × 5⁷ × 5² equals 5¹²!"
        ),
        "checkpoints": [
            {
                "question": "Simplify cleanly using the Product Rule with Same Base: 5³ × 5⁷ × 5²:",
                "options": [
                    "5¹²",
                    "5⁴²",
                    "15¹²",
                    "5¹⁰"
                ],
                "answer": 0,
                "hint": "Keep base 5 unchanged and ADD exponents 3 + 7 + 2!",
                "explanation": "5³ × 5⁷ × 5² = 5^(3+7+2) = 5¹² (never multiply the bases!)."
            },
            {
                "question": "Spot the common student trap: Which statement comparing multiplication vs addition of powers is TRUE?",
                "options": [
                    "2³ × 2⁴ = 2⁷ (128),   whereas 2³ + 2⁴ = 8 + 16 = 24 (NOT 2⁷!)",
                    "2³ + 2⁴ = 2⁷",
                    "2³ × 2⁴ = 4⁷",
                    "2³ × 2⁴ = 2¹²"
                ],
                "answer": 0,
                "hint": "Laws of exponents govern multiplication and division, NEVER direct addition!",
                "explanation": "Multiplication adds exponents cleanly (2³ × 2⁴ = 2⁷ = 128), while addition adds actual numeric values (8 + 16 = 24)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Power Of Power",
        "subtitle": "Section 2.2 Puzzle ('Magical Pond') & Nested Exponent Rule: (nᵃ)ᵇ = (nᵇ)ᵃ = nᵃᵇ",
        "speech": (
            "Now solve Section Two Point Two's famous 'Magical Pond' puzzle where glowing water lilies double rapidly across repeating weekly cycles, revealing Law Two: the POWER OF A POWER RULE! "
            "Suppose a magical pond doubles its glowing lily area 3 times per week (multiplying by 2³ each week), and we watch for FOUR full weeks! Total growth multiplies four identical copies of (2³): (2³)⁴ = 2³ × 2³ × 2³ × 2³! By Law One, add four exponents of 3: 3 + 3 + 3 + 3 = 3 × 4 = TWELVE! Thus (2³)⁴ equals 2¹²! Check symmetrically too: (2⁴)³ equals 2^(4×3) equals exact 2¹² identically! "
            "Behold Law Two cleanly: (nᵃ)ᵇ equals (nᵇ)ᵃ equals n^(a×b)! When raising a power INSIDE parentheses to ANOTHER power OUTSIDE parentheses, simply MULTIPLY BOTH EXPONENTS! "
            "Compare carefully against stacked power towers WITHOUT parentheses! Notice (2³)² equals 2^(3×2) = 2⁶ = SIXTY FOUR, whereas stacked 2^(3²) evaluates top exponent first 3² = 9, giving 2⁹ = FIVE HUNDRED TWELVE! Parentheses completely govern exponent evaluation order every single time without fail, and notice (10²)³ equals 10⁶ equals exactly one million cleanly without ever needing to count or write individual trailing zeros manually on paper!"
        ),
        "checkpoints": [
            {
                "question": "Simplify [(7²)³] cleanly using the Power of a Power rule:",
                "options": [
                    "7⁶",
                    "7⁵",
                    "7⁸",
                    "49³ = 7⁵"
                ],
                "answer": 0,
                "hint": "Multiply inside exponent 2 by outside exponent 3: 2 × 3!",
                "explanation": "(7²)³ = 7^(2×3) = 7⁶ (note (7³)² also equals 7⁶)."
            },
            {
                "question": "Compare (2³)² against 2^(3²) carefully:",
                "options": [
                    "(2³)² = 2⁶ = 64,   whereas 2^(3²) = 2⁹ = 512 (NOT equal!)",
                    "Both equal 64",
                    "Both equal 512",
                    "(2³)² = 512 and 2^(3²) = 64"
                ],
                "answer": 0,
                "hint": "With parentheses, multiply 3×2 = 6; without inner parentheses, compute 3² = 9 first!",
                "explanation": "(2³)² = 2^(3×2) = 2⁶ = 64; 2^(3²) = 2⁹ = 512."
            }
        ]
    },
    {
        "id": 5,
        "title": "Same Exponent Laws",
        "subtitle": "Section 2.2 Combinations & Laws Three & Four: mᵃ × nᵃ = (mn)ᵃ and mᵃ / nᵃ = (m/n)ᵃ",
        "speech": (
            "Now inspect what happens whenever BASES are DIFFERENT yet EXPONENTS match identically—as discovered in Section Two Point Two's 'How Many Combinations' outfit and meal puzzles! Suppose a school traveler selects between 2 shirts and 3 caps across 4 independent days cleanly! Multiplying 2⁴ × 3⁴ pairs one 2 with every matching 3 cleanly: (2×3) × (2×3) × (2×3) × (2×3) equals exact 6⁴! "
            "Behold Law Three, Product Rule with Same Exponent: mᵃ × nᵃ ALWAYS equals (m × n)ᵃ! Look closely at the superpower mental shortcut this unlocks for rapid arithmetic: 2ᵃ × 5ᵃ ALWAYS packs cleanly into (2 × 5)ᵃ = 10ᵃ! Test instantly: 2⁴ × 5⁴ equals (2×5)⁴ = 10⁴ = TEN THOUSAND in one glance! And 2⁷ × 5⁵ splits neatly as 2² × (2⁵ × 5⁵) = 4 × 10⁵ = FOUR LAKH (4,00,000) in two seconds! "
            "Similarly apply Law Four, Quotient Rule with Same Exponent: mᵃ divided by nᵃ equals (m divided by n)ᵃ (for any n ≠ 0)! Thus 15⁴ ÷ 3⁴ = (15/3)⁴ = 5⁴ = 625 effortlessly! Try also finding locker codes: choosing 5 independent digits per slot across 4 slots equals 5⁴ = 625 total codes!"
        ),
        "checkpoints": [
            {
                "question": "Use the Same-Exponent Product Rule (mᵃ × nᵃ = (mn)ᵃ) to evaluate 2⁶ × 5⁶ instantly without multiplying 64 × 15625:",
                "options": [
                    "10⁶   (= 10,00,000 / 1 Million)",
                    "7⁶",
                    "10¹²",
                    "25⁶"
                ],
                "answer": 0,
                "hint": "Combine matching exponents 6 over bases 2 × 5!",
                "explanation": "2⁶ × 5⁶ = (2 × 5)⁶ = 10⁶ = 10,00,000."
            },
            {
                "question": "Simplify (18⁵ ÷ 6⁵) cleanly using Law Four (Quotient with Same Exponent):",
                "options": [
                    "3⁵   (= 243)",
                    "12⁵",
                    "3⁰ = 1",
                    "18 / 6 = 3"
                ],
                "answer": 0,
                "hint": "Factor common exponent 5 outside fraction (18 / 6)⁵!",
                "explanation": "18⁵ / 6⁵ = (18 / 6)⁵ = 3⁵ = 243."
            }
        ]
    },
    {
        "id": 6,
        "title": "Division Base Rule",
        "subtitle": "Section 2.3: Dividing Same-Base Powers & Quotient Rule nᵃ ÷ nᵇ = nᵃ⁻ᵇ (n ≠ 0)",
        "speech": (
            "Enter Section Two Point Three: The Other Side of Powers! Earlier when multiplying identical bases nᵃ × nᵇ, we cleanly ADDED exponents together! Now what happens when DIVIDING identical bases nᵃ ÷ nᵇ (where n ≠ 0)? "
            "Cancel shared factors directly top to bottom! Compute 5⁷ ÷ 5³: write seven factors of 5 across the numerator and three factors of 5 across the denominator! Canceling THREE matching 5s cleanly from top and bottom leaves 7 − 3 = FOUR fives remaining cleanly on top = 5⁴ = 625! "
            "Behold Law Five, Quotient Rule with Same Base: for ANY non-zero number n, dividing powers simply subtracts bottom exponent from top exponent: nᵃ ÷ nᵇ equals n^(a−b)! "
            "Watch how smoothly ALL exponent laws team up together on multi-step NCERT Figure It Out simplification problems! Simplify (2⁸ × 3⁵) ÷ (2⁵ × 3²): group identical bases side by side cleanly—2^(8−5) × 3^(5−2) = 2³ × 3³! Next spot matching exponent 3 and invoke Law Three: (2 × 3)³ = 6³ = TWO HUNDRED SIXTEEN in three crisp lines! Remember always: NEVER blindly cancel exponents across DIFFERENT prime bases directly without carefully prime factoring every composite base completely first!"
        ),
        "checkpoints": [
            {
                "question": "Simplify (9⁶ ÷ 9²) cleanly using the Quotient Rule with Same Base:",
                "options": [
                    "9⁴",
                    "9³",
                    "9⁸",
                    "1⁴ = 1"
                ],
                "answer": 0,
                "hint": "Keep base 9 and SUBTRACT exponents: 6 − 2!",
                "explanation": "9⁶ ÷ 9² = 9^(6−2) = 9⁴."
            },
            {
                "question": "Simplify [(2⁸ × 3⁵) ÷ (2⁵ × 3²)] cleanly into one integer value:",
                "options": [
                    "216   (= 2³ × 3³ = 6³)",
                    "72",
                    "108",
                    "36"
                ],
                "answer": 0,
                "hint": "Subtract exponents per base: 2^(8−5) × 3^(5−2) = 2³ × 3³!",
                "explanation": "2³ × 3³ = (2 × 3)³ = 6³ = 216."
            }
        ]
    },
    {
        "id": 7,
        "title": "Zero Power Law",
        "subtitle": "Section 2.3 ('When Zero is in Power!'): Why x⁰ = 1 Always Holds for Every Non-Zero x ≠ 0",
        "speech": (
            "Conquer one of algebra's biggest mind-openers inside Section Two Point Three—'When Zero is in Power!': WHY does 5⁰, 100⁰, and even (−7)⁰ equal ONE instead of ZERO? Let us PROVE it rigorously in two crystal-clear ways! "
            "Proof One, Quotient Rule Consistency: Divide 5³ cleanly by 5³! Remember—any non-zero number divided by itself equals EXACT ONE (125 ÷ 125 = 1)! Yet apply Quotient Rule nᵃ ÷ nᵇ = n^(a−b): 5³ ÷ 5³ equals 5^(3−3) = FIVE TO THE POWER ZERO (5⁰)! Since both expressions evaluate the exact same division problem, 5⁰ MUST equal ONE! "
            "Proof Two, Stepping Down Pattern: Watch powers of 2 shrink cleanly by dividing by 2 at every single step: 2³ = 8, ÷2 gives 2² = 4, ÷2 gives 2¹ = 2, ÷2 gives 2⁰ = ONE! "
            "Watch the classic board exam trap carefully! Evaluate (5⁰ + 7⁰) × 9⁰: NEVER blindly write (0 + 0) × 0 = 0! Plug exact ONE cleanly for EVERY non-zero base raised to zero power: (1 + 1) × 1 = 2 × 1 = EXACT TWO! Note strictly x ≠ 0 because zero raised to zero (0⁰) stays left undefined in elementary arithmetic!"
        ),
        "checkpoints": [
            {
                "question": "Why does x⁰ ALWAYS equal 1 for every non-zero base x ≠ 0?",
                "options": [
                    "Because xᵃ ÷ xᵃ equals 1 by basic division AND equals x^(a−a) = x⁰ by the Quotient Rule!",
                    "Because multiplying x by 0 gives 1",
                    "Because zero equals one in exponent rules",
                    "Only when x = 10"
                ],
                "answer": 0,
                "hint": "Compare x³ / x³ directly (= 1) against Law Five x^(3−3) (= x⁰)!",
                "explanation": "xᵃ / xᵃ = 1 and xᵃ / xᵃ = x^(a−a) = x⁰ together prove x⁰ = 1 for all x ≠ 0."
            },
            {
                "question": "Evaluate cleanly: (3⁰ + 5⁰) × (11⁰ + 13⁰) − 2⁰:",
                "options": [
                    "3   [= (1 + 1) × (1 + 1) − 1 = 4 − 1]",
                    "0",
                    "4",
                    "1"
                ],
                "answer": 0,
                "hint": "Replace EVERY non-zero base raised to power 0 with 1 cleanly first!",
                "explanation": "(1 + 1) × (1 + 1) − 1 = 2 × 2 − 1 = 3."
            }
        ]
    },
    {
        "id": 8,
        "title": "Negative Exponent Reciprocals",
        "subtitle": "Section 2.3: Multiplicative Inverse Rule n⁻ᵃ = 1 / nᵃ & Extending Laws to Negative Powers",
        "speech": (
            "Now keep stepping LEFT past x⁰ = 1 inside Section Two Point Three! Watch what pops up cleanly on the negative side of zero: NEGATIVE EXPONENTS! "
            "Continue dividing powers of 10 cleanly by 10 at every single step: 10² = 100, 10¹ = 10, 10⁰ = 1, divide by 10 again: 10⁻¹ = ONE OVER TEN (1/10 = 0.1)! Divide by 10 again: 10⁻² = ONE OVER HUNDRED (1/10² = 0.01)! Divide again: 10⁻³ = 1/10³ = 0.001! "
            "Notice ONE crucial fact: a negative exponent NEVER turns a positive base negative! Instead, NEGATIVE POWER MEANS MULTIPLICATIVE RECIPROCAL (flip top and bottom cleanly)! Memorize the golden reciprocal pair: n⁻ᵃ equals 1 / nᵃ, and conversely 1 / n⁻ᵃ equals nᵃ! For any fraction (p/q)⁻ᵃ, simply flip numerator and denominator upside down to (q/p)ᵃ! "
            "And best news of all: ALL five exponent laws work 100 percent identically for negative exponents too! Check 2⁻³ × 2⁻² = 2^(−3 + (−2)) = 2⁻⁵ = 1/32, and check 3² ÷ 3⁻⁴ = 3^(2 − (−4)) = 3^(2 + 4) = 3⁶! Watch double minus signs very carefully whenever dividing identical bases or subtracting any negative exponent cleanly during algebra problem solving!"
        ),
        "checkpoints": [
            {
                "question": "What is the exact fraction value of 2⁻⁴ and also of (3/5)⁻²?",
                "options": [
                    "2⁻⁴ = 1 / 16   and   (3/5)⁻² = 25 / 9",
                    "2⁻⁴ = −16   and   (3/5)⁻² = −9 / 25",
                    "2⁻⁴ = 1 / 8   and   (3/5)⁻² = 9 / 25",
                    "2⁻⁴ = −8   and   (3/5)⁻² = 5 / 3"
                ],
                "answer": 0,
                "hint": "Negative exponents take the RECIPROCAL (never negate the number!): 1/2⁴ and (5/3)²!",
                "explanation": "2⁻⁴ = 1/2⁴ = 1/16; flipping fraction (3/5)⁻² gives (5/3)² = 25/9."
            },
            {
                "question": "Simplify carefully watching double minus signs: (5³ ÷ 5⁻²) × 5⁻⁴:",
                "options": [
                    "5¹   (= 5)",
                    "5⁻³",
                    "5⁹",
                    "5⁻⁹"
                ],
                "answer": 0,
                "hint": "In 5³ ÷ 5⁻², subtract negative exponent: 3 − (−2) = +5! Then add (−4)!",
                "explanation": "5^(3 − (−2)) × 5⁻⁴ = 5⁵ × 5⁻⁴ = 5^(5−4) = 5¹ = 5."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch2 Class 8 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

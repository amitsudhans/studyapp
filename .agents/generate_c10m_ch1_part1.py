#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 1: Real Numbers
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing for Indian male teacher voice)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (Raghav, Sonia, Ravi, Khushi, etc.), zero lecturer personas
- Note: Historical mathematician Carl Friedrich Gauss is permitted by curriculum.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Real Numbers Intro",
        "subtitle": "Continuing Positive Integer Study: Euclid's Algorithm and Fundamental Arithmetic Pillars",
        "speech": (
            "Welcome, enthusiastic Class Ten mathematicians, to Chapter One: Real Numbers! Back in Class Nine, you mapped out rational numbers alongside puzzling "
            "irrational numbers across the entire continuous real number line! This year, we zoom cleanly inward onto the fascinating secret patterns hidden right inside positive "
            "whole integers! Two colossal pillars guide our mathematical expedition from start to finish. Our very first pillar is Euclid's division algorithm, a timeless "
            "step-by-step remainder method crafted chiefly to compute the Highest Common Factor, or H C F, of any two positive integers swiftly through exact divisibility! "
            "Our second grand pillar is the Fundamental Theorem of Arithmetic, declaring that every composite whole number breaks apart into one completely unique recipe "
            "of prime numbers multiplied together! Wait until you witness how powerfully this single prime factorization pillar unlocks three astonishing mathematical "
            "feats: proving beyond any shadow of doubt why square root of 2, square root of 3, and square root of 5 are truly irrational numbers, AND predicting effortlessly "
            "whether any rational fraction p over q yields a cleanly stopping terminating decimal expansion or keeps repeating forever simply by inspecting denominator q! "
            "Ready to step inside the logical workshop of pure integers? Let us sharpen our reasoning and explore!"
        ),
        "checkpoints": [
            {
                "question": "Which two foundational pillars guide the study of positive integers in Class 10 Chapter 1: Real Numbers?",
                "options": [
                    "Euclid's division algorithm (divisibility & remainders) and the Fundamental Theorem of Arithmetic (unique prime factorization)",
                    "Only measuring circle areas with wooden protractors",
                    "Adding imaginary fractions onto negative decimal lines only",
                    "Memorizing multiplication tables up to five"
                ],
                "answer": 0,
                "hint": "Check Section 1.1: one uses remainders for HCF, while the other factors integers into primes!",
                "explanation": "Class 10 Chapter 1 builds on Class 9 Real Numbers by studying positive integer properties using Euclid's division algorithm and the Fundamental Theorem of Arithmetic."
            },
            {
                "question": "Besides computing unique prime products, what two key questions does prime factorization help resolve for rational and irrational numbers?",
                "options": [
                    "Proving irrationality of √2, √3, √5 and testing whether p/q has a terminating or repeating decimal expansion",
                    "Converting negative numbers into prime whole shapes",
                    "Solving quadratic parabolas without any coefficients",
                    "Drawing straight tangent chords on circle borders"
                ],
                "answer": 0,
                "hint": "Look at how prime factors of denominator q and squared primes determine decimal endings and irrationality!",
                "explanation": "The Fundamental Theorem of Arithmetic underpins contradiction proofs of irrationality and tests whether q has only factors 2 and 5 for terminating decimals."
            }
        ]
    },
    {
        "id": 2,
        "title": "Euclid Division Method",
        "subtitle": "Finding the HCF of Two Positive Integers Through Repeated Divisibility and Remainders",
        "speech": (
            "Let us examine our first integer engine closely: Euclid's division algorithm! Suppose two positive whole numbers stand before you—say 455 and 42—and you wish "
            "to uncover the largest possible integer that divides both numbers completely with zero remainder, called their Highest Common Factor or H C F! Rather than guessing divisors blindly, "
            "Euclid's clean remainder principle states that dividing a larger positive integer a by a smaller positive integer b always gives a unique quotient q plus a remainder r satisfying "
            "a equals b times q plus r, where remainder r sits from zero up to strictly less than b! Now watch how beautifully the chain runs step by step: divide 455 by 42, obtaining quotient 10 and "
            "remainder 35, because 42 times 10 is 420 plus 35 equals 455. Next, slide divisor 42 down as the new dividend and remainder 35 as the new divisor! Divide 42 by 35 cleanly: quotient 1, "
            "remainder 7! Slide once more: divide 35 by 7 to achieve quotient 5 and crisp remainder ZERO! The exact moment remainder reaches zero, the final non-zero divisor—here 7—locks in as the "
            "exact H C F of 455 and 42! Simple repeated remainders solve even giant multi-digit H C F puzzles reliably!"
        ),
        "checkpoints": [
            {
                "question": "In Euclid's division step a = bq + r for positive integers a and b, what strict range must remainder r always satisfy?",
                "options": [
                    "0 ≤ r < b",
                    "r > a always",
                    "b < r < a",
                    "r must always be negative"
                ],
                "answer": 0,
                "hint": "A remainder can be zero when divisibility is exact, and must stay strictly smaller than divisor b!",
                "explanation": "By Euclid's division lemma/algorithm, dividing a by b leaves a non-negative remainder r strictly less than divisor b (0 ≤ r < b)."
            },
            {
                "question": "Using Euclid's algorithm on 455 and 42 (455 = 42×10 + 35; 42 = 35×1 + 7; 35 = 7×5 + 0), which number equals HCF(455, 42)?",
                "options": [
                    "7",
                    "35",
                    "10",
                    "42"
                ],
                "answer": 0,
                "hint": "When remainder turns zero, look at the final divisor used in that last division step!",
                "explanation": "Since 7 divides 35 cleanly leaving remainder 0, the final non-zero divisor 7 is HCF(455, 42)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Decimal Expansion Test",
        "subtitle": "Determining Terminating vs. Non-Terminating Repeating Decimals via Denominator Prime Factors",
        "speech": (
            "Can you look straight at a reduced fraction p over q—without even performing tedious long division—and immediately predict whether its decimal expansion stops cleanly "
            "or keeps repeating forever? Prime factorization unlocks this exact shortcut cleanly! Remember rational numbers in lowest simplest form p over q where p and q share zero common "
            "factors besides 1. Now inspect only the prime factorization of bottom denominator q! When does decimal division terminate cleanly after finite steps? Only when denominator q "
            "splits cleanly into powers of 2 and powers of 5 alone—meaning q equals 2 to the power n times 5 to the power m! Why strictly 2 and 5? Because our base-ten number system builds "
            "tens strictly from 2 times 5! Take 3 divided by 8: denominator 8 equals 2 cubed, so multiplying numerator and denominator by 5 cubed turns the fraction into 375 over 1000, giving "
            "terminating decimal 0.375! Conversely, look at 1 over 7 or 7 divided by 30: even in reduced form, denominator 30 contains prime factor 3 besides 2 and 5! Any sneaky prime factor other "
            "than 2 or 5 inside simplified denominator q guarantees the decimal repeats periodically forever as a non-terminating recurring decimal!"
        ),
        "checkpoints": [
            {
                "question": "If rational number p/q (in lowest coprime form) has a terminating decimal expansion, what can be said about prime factors of denominator q?",
                "options": [
                    "Denominator q contains only prime factors 2 and/or 5 (form 2ⁿ × 5ᵐ)",
                    "Denominator q must contain prime factor 3 or 7",
                    "Numerator p must be strictly prime while q = 9",
                    "Denominator q must always be an odd prime greater than 5"
                ],
                "answer": 0,
                "hint": "Every terminating decimal writes cleanly over a power of 10 = 2 × 5!",
                "explanation": "A simplified rational p/q terminates if and only if the prime factorization of q is of the form 2ⁿ 5ᵐ for non-negative integers n, m."
            },
            {
                "question": "Without long division, classify the decimal expansion of 7/80 (note 80 = 2⁴ × 5¹) versus 13/21 (note 21 = 3 × 7):",
                "options": [
                    "7/80 is terminating; 13/21 is non-terminating repeating",
                    "Both 7/80 and 13/21 are irrational",
                    "7/80 is non-terminating; 13/21 terminates cleanly",
                    "Both decimal expansions end after exactly two digits"
                ],
                "answer": 0,
                "hint": "Check whether any prime besides 2 or 5 divides the simplified denominator!",
                "explanation": "80 factors purely into 2⁴ × 5¹, making 7/80 terminating (0.0875), whereas denominator 21 carries primes 3 and 7, forcing 13/21 to repeat forever."
            }
        ]
    },
    {
        "id": 4,
        "title": "Factor Tree Explorer",
        "subtitle": "Splitting Composite Numbers Into Primes With Trees and Meeting Carl Friedrich Gauss",
        "speech": (
            "Now let us build bright Prime Factor Trees just like master builders dismantling huge stone castles down into single unbreakable bricks! Every prime number—such as "
            "2, 3, 5, 7, 11, or 13—acts like an indivisible numerical atom carrying exactly two factors: 1 and itself! Pick a large composite integer like 32,760 and factor it "
            "step by step along branching limbs! Split 32,760 first into 2 times 16,380; split 16,380 into 2 times 8,190; split 8,190 into 2 times 4,095! Notice odd 4,095 splits cleanly into "
            "3 times 1,365, then 3 times 455, then 5 times 91, and finally prime 7 times prime 13! Multiply every leaf hanging along the bottom branches: 2 cubed times 3 squared times 5 times 7 times 13 "
            "equals 32,760! Notice a legendary historical genius standing behind this number law: Carl Friedrich Gauss, honored globally alongside Archimedes and Newton as the 'Prince of Mathematicians'! "
            "Writing his celebrated masterpiece Disquisitiones Arithmeticae at just twenty-one years old, Carl Friedrich Gauss first stated and proved this exact prime uniqueness theorem rigorously, transforming pure number theory forever! Today, you can split every composite integer cleanly down step by step until every single tiny bottom prime leaf shines unmistakably clear!"
        ),
        "checkpoints": [
            {
                "question": "Which historic scholar known as the 'Prince of Mathematicians' first stated and proved the Fundamental Theorem of Arithmetic in Disquisitiones Arithmeticae?",
                "options": [
                    "Carl Friedrich Gauss",
                    "Isaac Asimov",
                    "Blaise Pascal",
                    "René Descartes"
                ],
                "answer": 0,
                "hint": "He belongs to the legendary trio alongside Archimedes and Newton!",
                "explanation": "Carl Friedrich Gauss (1777–1855), often called the 'Prince of Mathematicians', gave the first complete proof of unique prime factorization."
            },
            {
                "question": "What are the prime power factors obtained at the bottom leaves of the Factor Tree for 32,760?",
                "options": [
                    "2³ × 3² × 5 × 7 × 13",
                    "2² × 3³ × 5² × 11",
                    "2⁴ × 5² × 7 × 17",
                    "3² × 5 × 11 × 19"
                ],
                "answer": 0,
                "hint": "Count how many 2s divide 32,760 cleanly: 32760 ÷ 8 = 4095, then 4095 = 9 × 5 × 91!",
                "explanation": "32,760 = 2 × 2 × 2 × 3 × 3 × 5 × 7 × 13 = 2³ × 3² × 5 × 7 × 13."
            }
        ]
    },
    {
        "id": 5,
        "title": "Fundamental Arithmetic Theorem",
        "subtitle": "Formulating Theorem 1.1: Every Composite Integer Has a Unique Prime Factorization",
        "speech": (
            "Now read carefully and lock Theorem One Point One—the Fundamental Theorem of Arithmetic—right into your mathematical toolkit! Theorem One Point One proclaims: "
            "Every composite number can be expressed, or factorized, as a product of primes, and this factorization is UNIQUE, apart from the order in which the prime factors occur! "
            "Pause and marvel at what 'unique apart from order' means! Suppose one student draws a factor tree for 60 starting with 2 times 30, ending with primes 2, 2, 3, and 5! "
            "Meanwhile, another student starts splitting 60 from 5 times 12, ending with primes 5, 3, 2, 2! Even though they branched along completely different routes, both trees terminate "
            "with the exact same collection of prime atoms: two 2s, one 3, and one 5! If we arrange prime factors neatly in non-decreasing ascending order—writing 2 squared times 3 times 5—then "
            "even the order becomes completely identical! Nobody anywhere in the universe can ever invent a secret collection of primes whose product equals 60 while sneaking in a 7! "
            "Prime factors truly serve as nature's permanent, tamper-proof numerical fingerprints for every single composite whole integer—letting mathematicians crack divisibility, remainders, and common multiples everywhere with complete logical confidence!"
        ),
        "checkpoints": [
            {
                "question": "According to Theorem 1.1 (Fundamental Theorem of Arithmetic), what holds true for any two prime factorizations of 210?",
                "options": [
                    "They must contain the exact same primes (2, 3, 5, 7) with exact same powers, differing only in factor order",
                    "One tree might contain prime 11 while the other contains prime 13",
                    "Composite numbers cannot be split into primes at all",
                    "Ordering factors from smallest to largest changes the actual product value"
                ],
                "answer": 0,
                "hint": "Every composite number has a single unique prime fingerprint apart from factor ordering!",
                "explanation": "Theorem 1.1 guarantees uniqueness of prime factors and exponents for every composite integer, regardless of factoring path order."
            },
            {
                "question": "Why must we require 'apart from the order in which prime factors occur' in Theorem 1.1?",
                "options": [
                    "Because 2 × 3 × 5 and 5 × 2 × 3 are both valid prime factorizations of 30 using identical prime factors",
                    "Because 2 × 3 × 5 gives a different sum than 5 × 2 × 3",
                    "Because prime numbers change value depending on sequence",
                    "Because composite numbers only allow 1 factor each"
                ],
                "answer": 0,
                "hint": "Multiplication is commutative, so rearranging the order writes the same prime collection differently!",
                "explanation": "Whether written as 2 × 3 × 5 or 3 × 5 × 2, multiplication order can vary while the underlying multiset of primes remains unique."
            }
        ]
    },
    {
        "id": 6,
        "title": "Zero Ending Check",
        "subtitle": "Applying Uniqueness to Prove Why Powers Like 4ⁿ and 6ⁿ Never End With Zero",
        "speech": (
            "Now put Theorem One Point One straight to work solving a classic reasoning puzzle! Consider: for any natural number n, can 4 raised to power n, or 6 raised "
            "to power n, ever end with the final units digit ZERO? Testing tiny powers gives 4, 16, 64, 256—notice only digits 4 and 6 alternate! Yet testing finite examples cannot check infinitely many integers n! Let uniqueness prove it decisively "
            "for ALL n! Suppose 4 to power n ends with zero for some n. Then 4 to power n must divide cleanly by 10, meaning prime factor 5 MUST divide 4 to power n! Yet 4 equals 2 squared, so "
            "4 to power n equals 2 to power 2n—containing ONLY prime 2! Similarly, 6 to power n factors strictly into 2 to power n times 3 to power n—holding strictly primes 2 and 3! "
            "By uniqueness in Theorem One Point One, prime 5 can NEVER appear anywhere inside either prime list—meaning neither 4 to power n nor 6 to power n can ever divide by 10 or end with units digit zero for any natural number n whatsoever! Checking prime factors beats checking endlessly many digits effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "For a natural number expression to end with the units digit 0, which two prime factors MUST appear in its prime factorization?",
                "options": [
                    "Both 2 and 5 (since 10 = 2 × 5)",
                    "Only 2 and 3",
                    "Only 3 and 7",
                    "Only prime factor 2 alone"
                ],
                "answer": 0,
                "hint": "Any number ending in 0 is divisible by 10!",
                "explanation": "A whole number ends with digit 0 if and only if it is a multiple of 10 = 2 × 5, requiring both primes 2 and 5."
            },
            {
                "question": "Why does Theorem 1.1 prove decisively that 6ⁿ (6ⁿ = 2ⁿ × 3ⁿ) cannot end with digit 0 for any natural number n?",
                "options": [
                    "Uniqueness guarantees 2 and 3 are the only primes in 6ⁿ, so required prime 5 can never exist in its factorization",
                    "Because 6 is an odd prime integer greater than 5",
                    "Because multiplying by 3 adds digit 0 at the front",
                    "Because n must be negative whenever 6ⁿ ends in 6"
                ],
                "answer": 0,
                "hint": "Inspect the primes present in 6ⁿ = (2 × 3)ⁿ and apply uniqueness!",
                "explanation": "6ⁿ = 2ⁿ × 3ⁿ contains solely primes 2 and 3. By unique prime factorization, prime 5 is absent, so 6ⁿ is never divisible by 10 or 5."
            }
        ]
    },
    {
        "id": 7,
        "title": "HCF And LCM",
        "subtitle": "Computing HCF and LCM Using Primes & Verifying HCF(a, b) × LCM(a, b) = a × b",
        "speech": (
            "Now master the cleanest method for computing both H C F and L C M for any two integers using prime powers! Take 96 and 404 from Textbook Example Seven. "
            "Factor 96 completely into primes: 96 equals 2 to power 5 times 3 to power 1. Next factor 404 completely: 404 equals 2 squared times 101 to power 1. How do we grab "
            "H C F instantly? Take the PRODUCT of the SMALLEST power of each COMMON prime factor present in both integers! Only prime 2 sits inside both 96 and 404, and its smallest power is "
            "2 squared, giving H C F equal to 4! Now how do we grab L C M? Take the PRODUCT of the GREATEST power of EVERY prime factor involved across either integer! Gather prime "
            "2 to power 5 times 3 to power 1 times 101 to power 1, giving L C M equal to 9,696! Wait—notice the golden symmetry identity linking any two positive integers a and b: "
            "H C F of a and b multiplied by L C M of a and b ALWAYS equals a times b! Multiply 4 times 9,696 to get 38,784—matching 96 times 404 identically! Given H C F, finding L C M "
            "takes one single division step!"
        ),
        "checkpoints": [
            {
                "question": "When using prime factorization for two integers a and b, how is HCF(a, b) vs LCM(a, b) chosen from prime powers?",
                "options": [
                    "HCF takes smallest powers of common primes; LCM takes greatest powers of every prime appearing in either number",
                    "HCF takes greatest powers of all primes; LCM takes smallest common powers",
                    "Both HCF and LCM sum all prime exponents together",
                    "LCM uses only odd primes while HCF uses only prime 2"
                ],
                "answer": 0,
                "hint": "HCF must divide inside BOTH (so stay small/common); LCM must hold BOTH inside it (so take all/greatest powers)!",
                "explanation": "HCF = product of smallest powers of common primes; LCM = product of greatest powers of all prime factors involved."
            },
            {
                "question": "If HCF(306, 657) = 9, use the identity HCF(a, b) × LCM(a, b) = a × b to find LCM(306, 657):",
                "options": [
                    "22,338",
                    "9,696",
                    "20,104",
                    "3,400"
                ],
                "answer": 0,
                "hint": "Compute (306 × 657) ÷ 9 cleanly by noticing 306 ÷ 9 = 34!",
                "explanation": "LCM(306, 657) = (306 × 657) / 9 = 34 × 657 = 22,338."
            }
        ]
    },
    {
        "id": 8,
        "title": "Composite Number Proof",
        "subtitle": "Identifying Composite Numbers Using Factor Extraction From Exercise 1.1 Sums & Products",
        "speech": (
            "Here is a wonderfully clever puzzle straight out of Exercise One Point One: Explain why expressions such as 7 times 11 times 13 plus 13, and 7 times 6 times 5 times 4 times 3 times 2 times 1 plus 5, "
            "are composite numbers! Many beginners rush to multiply out gigantic products just to test divisibility slowly! Stop and think cleanly like Carl Friedrich Gauss using elementary "
            "factoring instead! Recall the exact mathematical definition: a prime number admits ONLY two factors (1 and itself), whereas a composite number owns AT LEAST ONE extra factor besides "
            "1 and itself—meaning it factors cleanly as a product of two whole numbers greater than 1! Look closely at the first expression: 7 times 11 times 13 plus 13! Notice 13 appears cleanly in BOTH "
            "terms around the plus sign! Pull common factor 13 neatly outside brackets: 13 times (7 times 11 plus 1), which simplifies cleanly to 13 times 78, or 13 times 2 times 3 times 13! "
            "Clearly it possesses factors 13, 2, and 3—far more than two factors! Same magic solves the second expression: pull common factor 5 outside brackets to obtain 5 times (1,008 plus 1) equals 5 times 1,009! "
            "Since both expressions factor cleanly into products of primes besides 1, both are undeniably composite!"
        ),
        "checkpoints": [
            {
                "question": "Without multiplying everything out slowly, why is 7 × 11 × 13 + 13 guaranteed to be a composite number?",
                "options": [
                    "Factoring out 13 gives 13 × (7 × 11 + 1) = 13 × 78, proving it has factors 13, 2, 3 besides 1 and itself",
                    "Because every number ending in 3 is automatically composite",
                    "Because adding 13 to any product always creates an even prime",
                    "Because 7 × 11 × 13 equals zero"
                ],
                "answer": 0,
                "hint": "Spot the common factor shared by both added terms and pull it outside brackets!",
                "explanation": "Factoring out 13 reveals 13 × 78, which explicitly exhibits multiple factors (13, 2, 3, 6, etc.) other than 1 and the number itself."
            },
            {
                "question": "Pulling common factor 5 out of 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 expresses it as 5 × 1009. What proves this is composite?",
                "options": [
                    "It is expressed cleanly as the product of two integers both greater than 1 (5 and 1009)",
                    "Because 1009 ends with the digit 9",
                    "Because every factorial expression plus 5 equals 50",
                    "Because 5 divides 1009 evenly"
                ],
                "answer": 0,
                "hint": "Any positive integer equal to a × b with a > 1 and b > 1 has more than two factors!",
                "explanation": "Since both 5 > 1 and 1009 > 1 divide the total evenly, it has at least factors 1, 5, 1009, and the whole number—making it composite."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch1 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

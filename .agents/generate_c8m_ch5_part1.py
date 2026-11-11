#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 5: Number Play
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 5 syllabus with short 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Consecutive Number Sums",
        "subtitle": "Section 5.1: Representing Natural Numbers as Sums of Consecutive Integers & Powers of 2 Parity Rule",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Five: Number Play! Open Section Five Point One with a captivating detective math puzzle question: which natural counting numbers can be built smoothly by adding consecutive positive numbers together in straight unbroken sequences? "
            "Test odd number seven cleanly: seven equals three plus four (one way)! Now test fifteen right beside it: fifteen equals seven plus eight (two terms), ALSO equals four plus five plus six (three terms), AND equals one plus two plus three plus four plus five (five terms)! Why do some natural numbers admit multiple consecutive sums, others just one single sum, and a special few NONE AT ALL? "
            "Reveal the secret parity law right now! Any sum of two consecutive integers combines ONE EVEN plus ONE ODD, ALWAYS equaling an ODD number! Three consecutive numbers centered cleanly around middle integer m ALWAYS sum cleanly to three times m! Even-length consecutive spans follow neat symmetric half-integer pairing! Remarkably, EVERY odd number greater than one writes smoothly as two consecutive terms, while EVERY multiple of an odd prime splits cleanly—leaving ONLY pure POWERS OF TWO (2, 4, 8, 16, 32, ...) completely impossible to write as consecutive positive integer sums anywhere!"
        ),
        "checkpoints": [
            {
                "question": "Which set of numbers CANNOT be written as the sum of two or more consecutive natural numbers?",
                "options": [
                    "Pure powers of 2   (e.g. 2, 4, 8, 16, 32)",
                    "All odd numbers greater than 1   (e.g. 7, 15, 21)",
                    "Multiples of 3   (e.g. 6, 9, 15)",
                    "Multiples of 5   (e.g. 10, 15, 25)"
                ],
                "answer": 0,
                "hint": "Notice 6 = 1+2+3 and 10 = 1+2+3+4 work cleanly because they hold odd factors (3 and 5), whereas powers of 2 hold zero odd prime factors!",
                "explanation": "A natural number equals a consecutive sum if and only if it is NOT a pure power of 2."
            },
            {
                "question": "In how many distinct ways can 15 be written as a sum of two or more consecutive positive integers?",
                "options": [
                    "Three ways:  7+8,   4+5+6,   and   1+2+3+4+5",
                    "Only one way: 7+8",
                    "Two ways: 7+8 and 4+5+6",
                    "Zero ways"
                ],
                "answer": 0,
                "hint": "Count odd divisors of 15 greater than 1 (divisors 3 and 5 plus 2-term split 7+8)!",
                "explanation": "15 = 7+8 = 4+5+6 = 1+2+3+4+5 (exactly three distinct consecutive representations)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Four Consecutive Signs",
        "subtitle": "Section 5.1: Combining 4 Consecutive Integers (±a ± b ± c ± d) & Always-Even Constant Parity",
        "speech": (
            "Now investigate one of NCERT Section Five Point One's sharpest puzzles: COMBINING FOUR CONSECUTIVE NUMBERS! Take ANY four integers marching cleanly in a row—say 5, 6, 7, and 8 (or generally any a, a+1, a+2, a+3)—and place EITHER a PLUS sign or a MINUS sign freely right before each of those four integers! "
            "Count total choices systematically: choosing '+' or '−' across four slots produces 2 × 2 × 2 × 2 = SIXTEEN algebraic combinations (forming eight positive/negative magnitude pairs)! For example, +5 − 6 + 7 − 8 = −2, while −5 − 6 + 7 + 8 = +4, and +5 + 6 + 7 + 8 = +26! "
            "Test EVERY SINGLE ONE of all sixteen outcomes carefully: DID YOU EVER SPOT A SINGLE ODD RESULT LIKE 1, 3, 5, OR −7? NEVER! Why MUST ±a ± b ± c ± d ALWAYS evaluate cleanly to an EVEN NUMBER regardless whether a starts odd or even? "
            "Look directly inside ANY four consecutive numbers: TWO are ALWAYS ODD, and TWO are ALWAYS EVEN! Ignoring plus/minus direction for parity, combining TWO odd numbers ALWAYS yields EVEN (odd ± odd = even), while combining TWO even numbers ALWAYS stays EVEN—guaranteeing even + even = ALWAYS EVEN every single time!"
        ),
        "checkpoints": [
            {
                "question": "When placing '+' or '−' before each of any 4 consecutive integers (±a ± b ± c ± d), how many total sign combinations exist and what parity do ALL results share?",
                "options": [
                    "2⁴ = 16 sign combinations (8 distinct magnitude values), and ALL 16 always evaluate to an EVEN integer!",
                    "8 combinations, always ODD",
                    "16 combinations, half even and half odd",
                    "4 combinations, always multiples of 4"
                ],
                "answer": 0,
                "hint": "Every group of 4 consecutive integers contains exactly 2 odd numbers and 2 even numbers!",
                "explanation": "Two odds combine into an even integer, and two evens stay even; thus all 16 combinations stay strictly EVEN."
            },
            {
                "question": "Test consecutive integers 11, 12, 13, 14. Evaluate (11 − 12 − 13 + 14) AND state whether ANY sign flip can produce 15:",
                "options": [
                    "Evaluates to 0 (even); NO sign flip can produce odd 15 because all 16 outcomes stay even!",
                    "Evaluates to −2; flipping 11 creates odd 15",
                    "Evaluates to +2; flipping 13 gives 15",
                    "Evaluates to 14"
                ],
                "answer": 0,
                "hint": "11−12 = −1; −1−13 = −14; −14+14 = 0! And odd targets remain permanently unreachable!",
                "explanation": "11 − 12 − 13 + 14 = 0, and constant even parity makes odd sums impossible."
            }
        ]
    },
    {
        "id": 3,
        "title": "Parity Invariance Proof",
        "subtitle": "Section 5.1: Why Sign Flips Shift Totals by 2b & 'Breaking Even' Algebraic Parity Expressions",
        "speech": (
            "Discover the razor-sharp algebraic proof behind PARITY INVARIANCE and Section Five Point One's 'Breaking Even' expressions! Suppose ANY sum contains a positive term (+b), and suddenly you flip its sign from PLUS (+b) to MINUS (−b)! By how exact an amount did your overall total drop? "
            "Do the algebra cleanly: dropping from (+b) across zero down to (−b) changes the total by (+b) − (−b) = TWO TIMES b (2b)! Look closely at 2b: for ANY integer b whatsoever, multiplying by TWO ALWAYS produces an EVEN SHIFT (2b)! Adding or subtracting ANY even shift NEVER changes odd into even OR even into odd—so parity stays 100 percent INVARIANT across EVERY sign swap! "
            "Now master 'BREAKING EVEN' arithmetic laws cleanly: EVEN ± EVEN = EVEN; ODD ± ODD = EVEN; ONLY MIXED ODD ± EVEN = ODD! Test algebraic formulas confidently for arbitrary integers m, n, u, v, x: Look at 4m + 2q = 2(2m + q): ALWAYS EVEN! Look at 2u − 4v = 2(u − 2v): ALWAYS EVEN! Look at x² + 2: whenever x is EVEN, x² + 2 is EVEN; whenever x is ODD, x² stays odd so x² + 2 stays ODD—meaning parity tracks variable x directly!"
        ),
        "checkpoints": [
            {
                "question": "In any sum of integers, changing ONE sign from (+b) to (−b) alters the overall value by exactly how much, proving parity invariance?",
                "options": [
                    "Subtracts 2b (an ALWAYS-EVEN change!), leaving odd/even parity completely unchanged!",
                    "Subtracts 1b (sometimes odd)",
                    "Multiplies total by 2",
                    "Changes parity every single flip"
                ],
                "answer": 0,
                "hint": "Compute the exact difference (+b) − (−b) cleanly!",
                "explanation": "(+b) − (−b) = 2b is always even, so flipping any sign never changes the parity of the total."
            },
            {
                "question": "For arbitrary integers m, q, u, v, and x, classify the parity of (4m + 2q) and (x² + 3):",
                "options": [
                    "(4m + 2q) is ALWAYS EVEN;   (x² + 3) is EVEN when x is odd, and ODD when x is even!",
                    "Both are ALWAYS EVEN for all integers",
                    "(4m + 2q) is always ODD",
                    "(x² + 3) is ALWAYS ODD for every x"
                ],
                "answer": 0,
                "hint": "Factor 2 out of 4m+2q = 2(2m+q)! For x²+3, test x=2 (2²+3 = 7 odd) vs x=3 (3²+3 = 12 even)!",
                "explanation": "4m+2q = 2(2m+q) is always even; x² shares x's parity, so adding odd 3 flips parity cleanly."
            }
        ]
    },
    {
        "id": 4,
        "title": "Pairs Make Fours",
        "subtitle": "Section 5.1: Classifying Evens (4p vs 4p + 2 Modulo 4) & When Two Evens Sum to a Multiple of 4",
        "speech": (
            "Now zoom inside EVEN NUMBERS one level sharper in Section Five Point One: PAIRS TO MAKE FOURS! Wait—if you add ANY two even numbers together, you obviously get an even sum! Yet check carefully: does adding TWO even numbers ALWAYS produce a MULTIPLE OF FOUR? Test 6 + 4 = TEN! Oops—neither 6 nor 10 divides cleanly by 4! "
            "Classify ALL even integers cleanly modulo four into TWO distinct buckets! Bucket One: multiples of 4 written algebraically as 4p (for example 4, 8, 12, 16, 20—remainder ZERO when divided by 4)! Bucket Two: even numbers leaving REMAINDER TWO when divided by 4, written algebraically as 4p + 2 (for example 2, 6, 10, 14, 18)! "
            "Check BOTH pairing rules cleanly right now! Pair One: adding TWO numbers from Bucket One gives 4a + 4b = 4(a + b)—ALWAYS a multiple of 4! Pair Two: adding TWO numbers from Bucket Two gives (4a + 2) + (4b + 2) = 4(a + b) + 4 = 4(a + b + 1)—ALSO ALWAYS A MULTIPLE OF 4! Only MIXED pairing (one 4a plus one 4b + 2) equals 4(a + b) + 2, MISSING divisibility by 4 every single time!"
        ),
        "checkpoints": [
            {
                "question": "If x is of the form (4a + 2) and y is of the form (4b + 2) (both even numbers NOT divisible by 4), what is TRUE about (x + y)?",
                "options": [
                    "(x + y) is ALWAYS divisible by 4, because (4a+2) + (4b+2) = 4(a + b + 1)!",
                    "(x + y) is NEVER divisible by 4",
                    "(x + y) is always an odd integer",
                    "(x + y) leaves remainder 2 upon dividing by 4"
                ],
                "answer": 0,
                "hint": "Add remainders 2 + 2 = 4 cleanly, then factor out 4!",
                "explanation": "(4a + 2) + (4b + 2) = 4(a + b + 1), proving two remainder-2 evens ALWAYS combine into an exact multiple of 4."
            },
            {
                "question": "When does the sum of TWO even numbers FAIL to be a multiple of 4?",
                "options": [
                    "Whenever ONE even number is a multiple of 4 (4p) and the OTHER leaves remainder 2 (4q + 2)!",
                    "Whenever both are multiples of 4",
                    "Whenever both leave remainder 2",
                    "Never — all sums of two evens divide by 4"
                ],
                "answer": 0,
                "hint": "Compute 4p + (4q + 2) = 4(p + q) + 2 cleanly!",
                "explanation": "Mixing a multiple of 4 (4p) with a non-multiple (4q+2) always leaves remainder 2 modulo 4."
            }
        ]
    },
    {
        "id": 5,
        "title": "Divisibility By Eight",
        "subtitle": "Section 5.1 'Always, Sometimes, Never': Proving 8a + 8b = 8(a+b) & Counterexamples for Sum Splits",
        "speech": (
            "Sharpen your mathematical proof instincts right now inside Section Five Point One's famous 'ALWAYS, SOMETIMES, OR NEVER' laboratory! Let us inspect TWO deceptively similar statements about divisibility by eight—one holds ALWAYS, while the other holds ONLY SOMETIMES! "
            "Statement One: 'If two whole numbers are EACH divisible by 8, then their sum MUST ALSO be divisible by 8!' Prove this ALWAYS TRUE cleanly using algebra: call the first multiple 8a and the second multiple 8b (where a and b are whole numbers)! Add them together and pull common factor 8 outside via the distributive property: 8a + 8b = 8 × (a + b)! Since (a + b) stays a whole number, 8(a + b) is GUARANTEED to be divisible by 8 EVERY SINGLE TIME! "
            "Now flip it around carefully into Statement Two: 'If the SUM of two whole numbers is divisible by 8, MUST BOTH original numbers individually be multiples of 8?' Test clean numbers right now: yes, 16 + 24 = 40 uses two multiples of 8—YET look at 5 + 3 = EIGHT, or 11 + 13 = TWENTY FOUR! Neither 5 nor 3 divides by 8, proving Statement Two holds ONLY SOMETIMES in mathematics!"
        ),
        "checkpoints": [
            {
                "question": "Classify BOTH claims strictly as Always, Sometimes, or Never True:\n(i) If 8 divides x and 8 divides y, then 8 divides (x + y).\n(ii) If 8 divides (x + y), then 8 divides BOTH x and y.",
                "options": [
                    "(i) ALWAYS TRUE (8a+8b = 8(a+b));   (ii) SOMETIMES TRUE (counterexample: 5+3 = 8 divides by 8 yet 8 divides neither 5 nor 3!)",
                    "(i) ALWAYS TRUE;   (ii) ALWAYS TRUE",
                    "(i) SOMETIMES TRUE;   (ii) ALWAYS TRUE",
                    "(i) NEVER TRUE;   (ii) SOMETIMES TRUE"
                ],
                "answer": 0,
                "hint": "Check algebraic proof 8(a+b) for (i) vs splitting 24 = 11 + 13 cleanly for (ii)!",
                "explanation": "Multiples of 8 always sum to a multiple of 8, whereas sums totaling 8k only sometimes split into individual multiples of 8."
            },
            {
                "question": "Suppose x leaves remainder 3 when divided by 8 (x = 8a + 3). What remainder must y leave modulo 8 so that (x + y) is divisible by 8?",
                "options": [
                    "y must leave remainder 5   (since 3 + 5 = 8!)",
                    "y must leave remainder 3",
                    "y must leave remainder 0",
                    "y must leave remainder 7"
                ],
                "answer": 0,
                "hint": "Combine (8a + 3) + (8b + r) = 8(a + b) + (3 + r) so 3 + r hits 8!",
                "explanation": "(8a + 3) + (8b + 5) = 8(a + b + 1), cleanly divisible by 8."
            }
        ]
    },
    {
        "id": 6,
        "title": "Factors And LCM",
        "subtitle": "Section 5.1 Divisibility Theorems: Factor Inheritance (f|k|n), Multiples & The LCM(k, m) Rule",
        "speech": (
            "Unlock TWO rock-solid algebraic theorems powering divisibility proofs across Section Five Point One! "
            "Theorem One, Multiples of Factors: Suppose whole number n is cleanly divisible by divisor k (meaning n = k × q for some integer q)! First, what happens to ANY multiple of n, say m × n? Substitute n = kq: m × n = k × (m × q)—proving EVERY multiple of n ALSO stays cleanly divisible by k! Second, pick ANY smaller factor f of k (so k = f × r)! Substitute directly: n = (f × r) × q = f × (r × q)! Immediately prove: IF A NUMBER IS DIVISIBLE BY k, IT IS AUTOMATICALLY DIVISIBLE BY EVERY SINGLE FACTOR OF k! For example, every multiple of 12 automatically divides cleanly by 1, 2, 3, 4, 6, and 12! "
            "Theorem Two, The LCM Rule: What if a single number n divides cleanly by BOTH k AND m simultaneously? Then n MUST contain every prime factor power inside k AND every prime factor power inside m—proving n IS ALWAYS DIVISIBLE BY LCM(k, m)! Care alert: dividing by BOTH 4 and 6 guarantees divisibility by LCM(4, 6) = TWELVE (not necessarily 4 × 6 = 24—test number 12 itself!)!"
        ),
        "checkpoints": [
            {
                "question": "If an integer n is divisible by BOTH 6 and 9 simultaneously, what is the LARGEST divisor GUARANTEED to divide n every time?",
                "options": [
                    "18   (= LCM(6, 9); note n = 18 fails divisibility by 6 × 9 = 54!)",
                    "54   (= 6 × 9)",
                    "3   (= HCF(6, 9))",
                    "15   (= 6 + 9)"
                ],
                "answer": 0,
                "hint": "Apply the LCM Rule cleanly: calculate LCM(6, 9) and test n = 18 against 54!",
                "explanation": "n divisible by k and m is guaranteed divisible by LCM(k, m); LCM(6, 9) = 18."
            },
            {
                "question": "If a mystery number n is divisible by 36, which statement is ALWAYS TRUE by the Multiples-of-Factors rule?",
                "options": [
                    "n is automatically divisible by every factor of 36 (1, 2, 3, 4, 6, 9, 12, 18, 36), and 7n is also divisible by 36!",
                    "n is automatically divisible by 72",
                    "n can only be divisible by 36 and 1",
                    "n is never divisible by 4"
                ],
                "answer": 0,
                "hint": "Since 36 = f × r divides n = 36q = f(rq), ALL factors of 36 divide n automatically!",
                "explanation": "Every factor of divisor k divides n, and every multiple of n preserves divisibility by k."
            }
        ]
    },
    {
        "id": 7,
        "title": "What Remains Modulo",
        "subtitle": "Section 5.1 'What Remains?': Expressing Remainders Algebraically (5k + 3 = 5m − 2) & Remainder Problems",
        "speech": (
            "Solve Section Five Point One's clever 'WHAT REMAINS?' remainder puzzles cleanly using dual algebraic forms! Suppose you count marbles in groups of five, and EVERY single time THREE loose marbles remain left over! How can you write EVERY possible such marble count cleanly with ONE universal formula? "
            "Method One, Forward Remainder Form: write 5k + 3 (for any whole number k = 0, 1, 2, ...), giving exact values 3, 8, 13, 18, 23, 28, ...! Yet notice something astonishingly handy right beside it! Reaching the NEXT group of five (like 5, 10, 15, 20, ...) sits JUST TWO MARBLES SHORT! Method Two, Deficit Remainder Form writes those IDENTICAL numbers cleanly as 5m − 2 (for counting integer m = 1, 2, 3, ...: 5−2=3, 10−2=8, 15−2=13)! Both 5k + 3 and 5m − 2 capture the EXACT SAME remainder family modulo 5! "
            "Watch what superpower this algebra unlocks on remainder equations! Suppose a number leaves remainder 3 when divided by 5 (n = 5k + 3). Add 7: (5k + 3) + 7 = 5k + 10 = 5(k + 2)—suddenly divisible by 5 with ZERO remainder! And multiply two such numbers or square 5k + 3 to spot modulo shifts cleanly in one glance!"
        ),
        "checkpoints": [
            {
                "question": "Which two algebraic expressions represent the EXACT SAME family of positive integers leaving remainder 3 when divided by 5 (3, 8, 13, 18, 23...)?",
                "options": [
                    "5k + 3 (for k ≥ 0)   and   5m − 2 (for m ≥ 1)",
                    "5k + 3   and   5m − 3",
                    "3k + 5   and   3m − 2",
                    "5k + 2   and   5m − 3"
                ],
                "answer": 0,
                "hint": "Notice being 3 ABOVE a multiple of 5 equals being 2 BELOW the next multiple of 5 (since 3 + 2 = 5)!",
                "explanation": "5k + 3 = 5(k+1) − 2 = 5m − 2 generates the identical sequence 3, 8, 13, 18, 23, ..."
            },
            {
                "question": "If N leaves remainder 4 when divided by 7 (N = 7k + 4), what remainder does (N + 12) leave when divided by 7?",
                "options": [
                    "2   (since (7k + 4) + 12 = 7k + 16 = 7(k + 2) + 2)",
                    "4",
                    "6",
                    "0"
                ],
                "answer": 0,
                "hint": "Add 4 + 12 = 16, then take remainder of 16 ÷ 7 cleanly!",
                "explanation": "7k + 4 + 12 = 7k + 14 + 2 = 7(k + 2) + 2, leaving remainder 2."
            }
        ]
    },
    {
        "id": 8,
        "title": "Last Digits Shortcuts",
        "subtitle": "Section 5.2 Standard Shortcuts: Place-Value Proof (1000d + 100c + 10b + a) for 10, 5, 2, 4 & 8",
        "speech": (
            "Enter Section Five Point Two: Checking Divisibility Quickly! Have you ever wondered WHY checking only the LAST DIGIT instantly decides divisibility by ten, five, and two, while checking TWO digits solves four, and checking THREE digits solves eight—even for a hundred-digit integer? Prove ALL FIVE shortcuts algebraically from ONE place-value identity! "
            "Expand ANY integer N = ...dcba cleanly: N equals 1000d + 100c + 10b + a! First factor out 10 from every digit left of units digit a: N = 10 × (100d + 10c + b) + a! Notice that giant bracket term is ALREADY divisible by 10, 5, AND 2! Therefore divisibility by 10, 5, or 2 depends STRICTLY upon units digit 'a' alone: a = 0 gives divisibility by 10; a ∈ {0, 5} gives divisibility by 5; and a ∈ {0, 2, 4, 6, 8} gives divisibility by 2! "
            "Now shift ONE column left cleanly: rewrite N = 100 × (10d + c) + (10b + a)! Since 100 = 4 × 25 divides cleanly by 4, divisibility by FOUR depends strictly on last two digits (ba)! Similarly 1000 = 8 × 125 makes divisibility by EIGHT depend strictly on last three digits (cba)!"
        ),
        "checkpoints": [
            {
                "question": "Algebraically expanding N = 100(10d + c) + (10b + a) directly proves the divisibility rule for 4 because:",
                "options": [
                    "100 (= 4 × 25) makes EVERY higher place-value term automatically divisible by 4, leaving ONLY the last two digits (10b + a) to check!",
                    "4 divides 10 evenly",
                    "Only units digit a matters for 4",
                    "Digits must add up to 4"
                ],
                "answer": 0,
                "hint": "Check 100 ÷ 4 = 25 (zero remainder!), whereas 10 ÷ 4 leaves remainder 2!",
                "explanation": "Since 4 | 100, 100(10d + c) is always divisible by 4, so 4 | N depends solely on last two digits (10b + a)."
            },
            {
                "question": "Which digit combination cleanly checks divisibility by 8 for 7,354,912 without dividing the whole 7-digit number?",
                "options": [
                    "Check only the last 3 digits: 912 ÷ 8 = 114 (exact, so 8 divides 7,354,912!)",
                    "Check only last digit 2",
                    "Check last 2 digits 12",
                    "Sum all digits 7+3+5+4+9+1+2 = 31"
                ],
                "answer": 0,
                "hint": "Because 1000 = 8 × 125 divides cleanly by 8, test only 100c + 10b + a = 912!",
                "explanation": "912 = 8 × 114 divides cleanly by 8 (whereas 100 ≠ multiple of 8), proving 8 | 7,354,912."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch5 Class 8 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

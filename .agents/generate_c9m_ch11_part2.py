#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 11: The World of Algorithms
Part 2: Slides 9 to 16 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Algorithm Efficiency Scaling",
        "subtitle": "Section 11.3.2 Analysing these Algorithms: Numerical Value vs Digit Count Scaling",
        "speech": (
            "Stage Three eliminated all intermediate lists—so is our one-to-min-of-m-and-n GCD algorithm truly FAST on giant numbers? Test it critically inside Section Eleven Point Three Point Two: EFFICIENCY ANALYSIS! "
            "Suppose m and n are ten-digit integers—around five billion! How many loop iterations does scanning from one up to min(m, n) perform? FIVE BILLION remainder checks! Even at one billion operations per second, a twenty-digit number would take centuries! "
            "Why is linear scanning so slow compared to column addition? Look at the crucial difference in INPUT SCALING! Adding two d-digit numbers takes roughly d steps—increasing the number from ten digits to twenty digits only DOUBLES the work! By contrast, a linear scan up to min(m, n) scales with the NUMERICAL VALUE ten to the power d! Adding just ONE extra digit multiplies the runtime by TEN! "
            "In computer science, algorithms scaling linearly with numerical magnitude (ten to the d) are exponentially slower than algorithms scaling with digit count (d)! To achieve true efficiency for cryptography and big-number math, we MUST discover an algorithm whose steps depend on DIGITS, not numerical value! Otherwise, even modern supercomputers stall completely whenever input numbers grow beyond ten, fifteen, or twenty decimal digits!"
        ),
        "checkpoints": [
            {
                "question": "If a GCD algorithm scans 1 to min(m, n), what happens to its runtime when m and n gain 2 extra decimal digits (e.g., 10⁴ → 10⁶)?",
                "options": [
                    "The number of steps multiplies by roughly 100× (scaling with numerical magnitude, not digit count)",
                    "It only adds 2 extra steps",
                    "It runs faster",
                    "It stays constant"
                ],
                "answer": 0,
                "hint": "Adding 2 decimal digits multiplies a number's value by 10² = 100!",
                "explanation": "Value-linear algorithms scale as O(10^d) in digit count d, growing 10× per added digit."
            },
            {
                "question": "Why is column addition considered vastly more efficient in scaling than 1-to-min(m, n) GCD scanning?",
                "options": [
                    "Column addition takes steps proportional to the number of digits d, whereas 1-to-min(m, n) takes steps proportional to numerical value 10^d",
                    "Because addition never uses loops",
                    "Because addition only works on 2-digit numbers",
                    "Because GCD cannot be computed for 10-digit numbers"
                ],
                "answer": 0,
                "hint": "Compare d steps vs 10^d steps for d = 12 digits!",
                "explanation": "Algorithms proportional to digit length d remain fast even on 100-digit integers."
            }
        ]
    },
    {
        "id": 10,
        "title": "Euclid Subtraction Algorithm",
        "subtitle": "Section 11.3.3 Euclid's Subtraction Algorithm: gcd(m, n) = gcd(n, m − n) & Block Tiling",
        "speech": (
            "Discover our first huge algorithmic breakthrough inside Section Eleven Point Three Point Three: EUCLID'S SUBTRACTION ALGORITHM from Euclid's Elements! "
            "Imagine tiling an m-by-n rectangular floor (say eighteen by twelve) using identical square tiles of the largest possible side length d! Because d tiles both width m and height n evenly, d must divide BOTH m and n! Now place one twelve-by-twelve square inside the eighteen-by-twelve rectangle! What remains untiled? A smaller six-by-twelve rectangle—dimensions n by open m minus n close! "
            "Any square tile that fits both m and n MUST also fit the remaining difference m minus n! Therefore, for m greater than n, GCD OF m AND n EQUALS GCD OF n AND m MINUS n! "
            "Repeat subtracting the smaller from the larger until both become EQUAL—that shared value IS the GCD! Trace twenty-four and nine: (24, 9) → (15, 9) → (6, 9) → (6, 3) → (3, 3) → GCD equals THREE! Watch the one edge-case limitation though: for gcd(2k + 1, 2)—say one million and one vs two—subtracting two repeatedly takes k = five hundred thousand subtractions—revealing why we still need one much sharper algorithmic idea for truly large real-world inputs!"
        ),
        "checkpoints": [
            {
                "question": "Trace Euclid's subtraction algorithm on (21, 9). Which sequence of pairs appears?",
                "options": [
                    "(21, 9) → (12, 9) → (3, 9) → (6, 3) → (3, 3) ⇒ GCD = 3",
                    "(21, 9) → (12, 9) → (9, 9) ⇒ GCD = 9",
                    "(21, 9) → (10, 9) → (1, 1) ⇒ GCD = 1",
                    "(21, 9) → (7, 3) ⇒ GCD = 3"
                ],
                "answer": 0,
                "hint": "Repeatedly replace the larger number with (larger − smaller) until both equal!",
                "explanation": "21−9=12, 12−9=3, 9−3=6, 6−3=3, giving (3, 3) and GCD = 3."
            },
            {
                "question": "Why can Euclid's subtraction algorithm still be slow on an extreme pair like gcd(2,000,001, 2)?",
                "options": [
                    "Because subtracting 2 repeatedly from 2,000,001 requires 1,000,000 subtraction steps!",
                    "Because 2 has no divisors",
                    "Because subtraction gives negative numbers",
                    "Because the answer is 2"
                ],
                "answer": 0,
                "hint": "How many times must you subtract 2 from 2k + 1 before reaching 1?",
                "explanation": "Repeatedly subtracting a tiny number from a huge number takes k steps — motivating modulo division!"
            }
        ]
    },
    {
        "id": 11,
        "title": "Āryabhaṭa Division Algorithm",
        "subtitle": "Section 11.3.4 Āryabhaṭa's Division Algorithm: Remainder Reduction gcd(n, m mod n) (499 CE)",
        "speech": (
            "Now witness the ultimate GCD leap inside Section Eleven Point Three Point Four: ĀRYABHAṬA'S DIVISION ALGORITHM from his four hundred ninety-nine CE treatise Āryabhaṭīya! "
            "Notice why Euclid's subtraction crawled on gcd(two million one, two): subtracting two a million times in a row is literally JUST REPEATED SUBTRACTION—which is DIVISION! Instead of subtracting n one step at a time, divide m by n once and jump straight to the REMAINDER r equals m modulo n! "
            "Because subtracting n q times leaves remainder r equals m minus q n, the exact same block-tiling logic proves: GCD OF m AND n EQUALS GCD OF n AND m MODULO n! Repeat replacing (m, n) with (n, m mod n) until the remainder hits ZERO—the last non-zero divisor IS the GCD! "
            "Watch how fast it runs on (2,000,001, 2): ONE single division gives remainder ONE, next division gives remainder ZERO—finished in TWO STEPS instead of one million! Even for arbitrary ten-digit numbers, remainder shrinks by at least half every two steps, completing in roughly five times the DIGIT COUNT! Even huge hundred-digit cryptographic keys finish smoothly in under five hundred fast remainder divisions every single time without any fail whatsoever!"
        ),
        "checkpoints": [
            {
                "question": "Trace Āryabhaṭa's division algorithm on (48, 18): what are the remainder steps?",
                "options": [
                    "(48, 18) → 48 mod 18 = 12 → (18, 12) → 18 mod 12 = 6 → (12, 6) → 12 mod 6 = 0 ⇒ GCD = 6",
                    "(48, 18) → 48 mod 18 = 8 → (18, 8) ⇒ GCD = 2",
                    "(48, 18) → (30, 18) → (12, 18) ⇒ GCD = 6",
                    "Takes 18 steps"
                ],
                "answer": 0,
                "hint": "Replace (m, n) with (n, m mod n) until the second number becomes 0!",
                "explanation": "48 = 2(18)+12, 18 = 1(12)+6, 12 = 2(6)+0; last non-zero remainder is 6."
            },
            {
                "question": "Why does Āryabhaṭa's division algorithm scale with the NUMBER OF DIGITS rather than the numerical value?",
                "options": [
                    "Every 2 remainder steps shrink the numbers by at least a factor of 2, so total steps grow logarithmically (proportional to digit count)",
                    "Because modulo always equals 0 on the first step",
                    "Because it skips odd numbers",
                    "Because it adds the digits instead of dividing"
                ],
                "answer": 0,
                "hint": "Exponential halving means 10^d shrinks to 1 in O(d) steps!",
                "explanation": "Since m mod n < m/2 whenever n ≤ m/2 (and next step if n > m/2), values drop exponentially fast in O(d) steps."
            }
        ]
    },
    {
        "id": 12,
        "title": "Al-Khwārizmī Algorithm Origins",
        "subtitle": "A Pinch of History: From Al-Khwārizmī (Liber Algorismi) & Indian Numerals to 'Algorithm'",
        "speech": (
            "Pause for a fascinating Pinch of History behind the very word ALGORITHM! "
            "Where did the English word 'algorithm' come from? In the ninth century CE, the brilliant Persian scholar MUḤAMMAD IBN MŪSĀ AL-KHWĀRIZMĪ worked at the House of Wisdom in Baghdad! Around eight hundred twenty-five CE, he wrote a landmark Arabic treatise explaining India's revolutionary base-ten decimal place-value system—zero and the digits one through nine—along with step-by-step procedures for addition, subtraction, multiplication, and division! "
            "When European scholars translated Al-Khwārizmī's book into Latin in the twelfth century under titles like Liber Algorismi (literally 'Book of Al-Khwārizmī'), his Latinized name 'Algorismi' evolved into 'algorism', meaning Indian place-value arithmetic! Over time, that word broadened into 'ALGORITHM' for ANY systematic computational procedure! "
            "Think about that unbroken global thread: Indian decimal place-value and Āryabhaṭa's division method traveled through Baghdad via Al-Khwārizmī into Europe, laying the foundation for modern computer science and every digital device on Earth today! Whenever you hear computer scientists speak of algorithms, remember that this very word honors Al-Khwārizmī's clear step-by-step exposition of Indian decimal place-value calculation across centuries of global mathematical history, inspiring every modern programming language, software engineering textbook, and automated modern digital calculation system!"
        ),
        "checkpoints": [
            {
                "question": "From whose name and Latinized book title did the English word 'algorithm' originate?",
                "options": [
                    "9th-century scholar Al-Khwārizmī, via the Latin translation 'Liber Algorismi'",
                    "Euclid's Elements",
                    "Isaac Newton's Principia",
                    "Pierre de Fermat's Margin Notes"
                ],
                "answer": 0,
                "hint": "Notice the sound similarity between 'Algorismi' and 'algorithm'!",
                "explanation": "Al-Khwārizmī's name was Latinized as Algorismi in translations of his treatise on Indian decimal arithmetic."
            },
            {
                "question": "Which mathematical innovation did Al-Khwārizmī's treatise popularize across the Islamic world and Europe?",
                "options": [
                    "Indian base-10 decimal numerals (including zero) and place-value arithmetic algorithms",
                    "Roman numeral dot counting",
                    "Only geometric compass constructions",
                    "Binary computer chips"
                ],
                "answer": 0,
                "hint": "Remember Section 11.1's efficiency leap from dots to place-value digits!",
                "explanation": "Al-Khwārizmī explained Indian decimal place-value numerals and step-by-step arithmetic rules."
            }
        ]
    },
    {
        "id": 13,
        "title": "Tracing Addition Reverse",
        "subtitle": "Exercises 11.1–11.2: Multi-Digit Addition Traces, Reverse List Scans & LCM via GCD",
        "speech": (
            "Now apply your algorithmic skills to Exercise Sets Eleven Point One and Eleven Point Two: ADDITION TRACES, REVERSE SCANS, AND LCM ALGORITHMS! "
            "First, trace column addition on seven hundred eighty-six plus four hundred fifty-nine! Column one (ones): six plus nine equals fifteen—write five, carry one! Column two (tens): eight plus five plus carry one equals fourteen—write four, carry one! Column three (hundreds): seven plus four plus carry one equals twelve—write two, carry one! Final carry one writes leading one, giving ONE THOUSAND TWO HUNDRED FORTY-FIVE! "
            "Second, optimize GCD scanning via a REVERSE LOOP! Instead of scanning i upward from one to min(m, n), scan downward from i equals min(m, n) down to one! The VERY FIRST i that divides both m and n IS the GCD—allowing immediate early exit! "
            "Third, design an ultra-fast LCM ALGORITHM! Never list multiples endlessly—use the identity LCM(m, n) EQUALS m TIMES n DIVIDED BY GCD(m, n) (dividing m by gcd first to avoid huge intermediate products)! Remember also: reverse scanning from min(m, n) down to one shines when common factors are large, yet coprime integer pairs still force scanning all the way down to one every single time without shortcuts!"
        ),
        "checkpoints": [
            {
                "question": "Using the efficient identity lcm(m, n) = (m / gcd(m, n)) × n, what is lcm(24, 36)?",
                "options": [
                    "72 (since gcd(24, 36) = 12, and (24 / 12) × 36 = 2 × 36 = 72)",
                    "864",
                    "12",
                    "144"
                ],
                "answer": 0,
                "hint": "First find gcd(24, 36) = 12, then compute (24 ÷ 12) × 36!",
                "explanation": "Using Āryabhaṭa's GCD gives lcm(24, 36) = (24/12)×36 = 72 in just a few operations."
            },
            {
                "question": "When scanning i downward from min(m, n) down to 1 to find gcd(m, n), what happens when m and n are coprime (gcd = 1), such as (1000, 999)?",
                "options": [
                    "Worst case! It still scans all the way down from 999 to 1 (999 checks), showing why Āryabhaṭa's algorithm is still far superior",
                    "It finishes in 1 step",
                    "It returns 999",
                    "It enters an infinite loop"
                ],
                "answer": 0,
                "hint": "How many steps from 999 down to 1 before finding the first common divisor 1?",
                "explanation": "Reverse scanning helps when GCD is large, but coprime pairs still require min(m, n) steps."
            }
        ]
    },
    {
        "id": 14,
        "title": "Prime Testing Algorithms",
        "subtitle": "Exercise 11.3: Prime Testing Algorithm prime(n) Up to √n & Prime Factorization",
        "speech": (
            "Now design and optimize a classic number-theory algorithm from Exercise Eleven Point Three: TESTING WHETHER AN INTEGER n IS PRIME (prime(n)) AND PRIME FACTORIZATION! "
            "First handle base cases cleanly: if n is less than or equal to one, return FALSE (one is neither prime nor composite)! Next, naive testing checks every integer d from two up to n minus one: if n modulo d equals zero, return FALSE immediately; if the loop finishes, return TRUE! "
            "Wait—can we slash the loop length dramatically just like we optimized GCD? YES! Suppose n is composite, so n equals a times b with both factors greater than one! Could BOTH a AND b exceed the SQUARE ROOT OF n? Impossible—if a exceeded square root n AND b exceeded square root n, their product a times b would exceed n! Therefore, EVERY composite number n MUST have at least one factor d less than or equal to SQUARE ROOT OF n! "
            "So prime(n) only needs to check d from two up to floor(square root of n)! For n equals one million, checking drops from one million steps down to just ONE THOUSAND steps—a thousand-fold speedup from one simple mathematical inequality!"
        ),
        "checkpoints": [
            {
                "question": "To test whether n = 197 is prime using the optimized prime(n) algorithm, up to which integer d do we need to check divisibility?",
                "options": [
                    "Up to d = 14 (since 14² = 196 ≤ 197 < 15² = 225, so ⌊√197⌋ = 14)",
                    "Up to d = 196",
                    "Up to d = 98",
                    "Up to d = 100"
                ],
                "answer": 0,
                "hint": "Find the largest integer d such that d² ≤ 197!",
                "explanation": "Any composite factor pair {a, b} of 197 must have min(a, b) ≤ √197 ≈ 14.03, so checking d = 2..14 suffices."
            },
            {
                "question": "Why must every composite number n have at least one factor d ≤ √n?",
                "options": [
                    "If both factors in n = a × b exceeded √n, their product a × b would strictly exceed √n × √n = n (contradiction)",
                    "Because all prime numbers are less than 10",
                    "Because √n is always a factor of n",
                    "Because composite numbers are always even"
                ],
                "answer": 0,
                "hint": "Use a quick proof by contradiction assuming a > √n and b > √n!",
                "explanation": "a > √n and b > √n ⇒ a·b > n, contradicting a·b = n."
            }
        ]
    },
    {
        "id": 15,
        "title": "Computational Algorithm Traces",
        "subtitle": "End-of-Chapter Exercises: Tracing Āryabhaṭa's Division, Loop Invariants & Correctness Proofs",
        "speech": (
            "Practice end-of-chapter computational execution traces on Āryabhaṭa's division algorithm and verify WHY we know it ALWAYS terminates with the exact right answer! "
            "Trace gcd(1071, 462) step by step! Step One: divide one thousand seventy-one by four hundred sixty-two—quotient two, remainder ONE HUNDRED FORTY-SEVEN! New pair: (462, 147)! Step Two: divide four hundred sixty-two by one hundred forty-seven—quotient three, remainder TWENTY-ONE! New pair: (147, 21)! Step Three: divide one hundred forty-seven by twenty-one—quotient seven, remainder ZERO! Stop and return TWENTY-ONE! Just THREE divisions! "
            "Now inspect the TWO-PART PROOF OF CORRECTNESS every great algorithm needs! First, TERMINATION: each remainder r satisfies zero less than or equal to r strictly less than n! Because remainders are non-negative integers that strictly shrink on every step, the loop CANNOT run forever—it MUST eventually hit zero! Second, LOOP INVARIANT: at every step, gcd(m, n) equals gcd(n, m mod n)! Since gcd(d, 0) equals d when remainder hits zero, the final non-zero divisor MUST equal the original gcd! Combining termination with an unchanging loop invariant gives rock-solid mathematical certainty that our algorithm works reliably on every positive integer pair without a single exception anywhere across all positive integer inputs in number theory and mathematics!"
        ),
        "checkpoints": [
            {
                "question": "Trace Āryabhaṭa's division algorithm on gcd(252, 105). How many modulo steps until remainder 0, and what is the GCD?",
                "options": [
                    "3 steps: (252, 105) → (105, 42) → (42, 21) → (21, 0) ⇒ GCD = 21",
                    "2 steps ⇒ GCD = 42",
                    "4 steps ⇒ GCD = 7",
                    "105 steps ⇒ GCD = 21"
                ],
                "answer": 0,
                "hint": "Compute 252 mod 105 = 42, then 105 mod 42 = 21, then 42 mod 21 = 0!",
                "explanation": "252 = 2(105)+42, 105 = 2(42)+21, 42 = 2(21)+0 ⇒ GCD = 21 in 3 division steps."
            },
            {
                "question": "What guarantees that Āryabhaṭa's division algorithm ALWAYS terminates (never loops infinitely)?",
                "options": [
                    "The remainder r satisfies 0 ≤ r < n, so the second argument strictly decreases through non-negative integers until hitting 0",
                    "Because m and n are always even",
                    "Because we stop after 10 steps automatically",
                    "Because division always gives remainder 1"
                ],
                "answer": 0,
                "hint": "Can a strictly decreasing sequence of non-negative integers continue forever?",
                "explanation": "Strictly decreasing non-negative integers must reach 0 in finitely many steps."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Algorithm Summary",
        "subtitle": "Chapter 11 Synthesis: Loops, Data Structures, Correctness Proofs, Efficiency & Input Scaling",
        "speech": (
            "Congratulations on completing Chapter Eleven: The World of Algorithms! Let us bring together the six core pillars of algorithmic thinking you mastered! "
            "Pillar One: STEP-BY-STEP EXECUTION LOGIC—every algorithm breaks tasks into unambiguous, finite operations, like five-step column addition! "
            "Pillar Two: CONDITIONAL LOOPS—repeating bounded tests until a stopping condition fires, like scanning divisors or reducing remainders to zero! "
            "Pillar Three: DATA STRUCTURES—choosing between ordered lists (D sub m, D sub n, C) and single variables (best_gcd) to balance clarity against memory cost! "
            "Pillar Four: PROOF OF CORRECTNESS—proving BOTH termination (strictly shrinking non-negative remainders) AND invariant preservation (gcd(m, n) equals gcd(n, m mod n))! "
            "Pillar Five: EFFICIENCY AND INPUT SCALING—distinguishing algorithms that scale exponentially slowly with numerical value ten to the d (dot counting, linear GCD scan) from blazingly fast algorithms scaling with digit count d (place-value addition, Āryabhaṭa's division algorithm)! "
            "Pillar Six: GLOBAL HERITAGE—from Āryabhaṭa's Āryabhaṭīya and Euclid's Elements to Al-Khwārizmī's Liber Algorismi! Now test yourself on the forty silent quiz challenges ahead—tracing multi-digit column additions, comparing divisor lists, counting subtraction versus modulo steps, computing LCMs quickly, and verifying prime-testing square-root bounds accurately on every single silent challenge question ahead in this chapter—let us begin right now!"
        ),
        "checkpoints": [
            {
                "question": "Which two properties together form a complete Proof of Correctness for an iterative algorithm like Āryabhaṭa's GCD?",
                "options": [
                    "Termination (proving the loop must stop) and Loop Invariant / Partial Correctness (proving the answer stays preserved at every step)",
                    "Only testing 3 small examples",
                    "Using 3 separate lists",
                    "Adding leading zeros"
                ],
                "answer": 0,
                "hint": "An algorithm must BOTH finish in finite time AND return the exact right value when it stops!",
                "explanation": "Termination + invariant preservation mathematically guarantee correctness for all valid inputs."
            },
            {
                "question": "Rank these three GCD methods from SLOWEST to FASTEST for huge 12-digit numbers:",
                "options": [
                    "1-to-min(m,n) linear scan (slowest) → Euclid subtraction (faster, slow on 2k+1, 2) → Āryabhaṭa division (fastest, digit-count scaling)",
                    "Āryabhaṭa division → Euclid subtraction → 1-to-min(m,n) linear scan",
                    "All three take the exact same time",
                    "Euclid subtraction → 1-to-min(m,n) → Āryabhaṭa"
                ],
                "answer": 0,
                "hint": "Linear value scan takes ~10¹² steps, whereas Āryabhaṭa's modulo takes ~20–60 steps!",
                "explanation": "Āryabhaṭa's remainder algorithm scales with digit length d, vastly outperforming value-linear scans."
            }
        ]
    }
]

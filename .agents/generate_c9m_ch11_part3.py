#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 11: The World of Algorithms
Part 3: Slides 17 to 20 (Silent Mastery Quiz Slides - 40 Questions with 3-Step Solutions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Addition Divisor Challenge",
        "subtitle": "Mastery Quiz 1 (Silent Exercise): Place-Value Addition, 5-Step Algorithm & Divisor Listing",
        "is_quiz": True,
        "questions": [
            {
                "question": "Why does base-10 column addition scale far better than dot counting for 8-digit numbers?",
                "options": [
                    "Column addition performs 8 digit-column steps (proportional to digit count), whereas dot counting requires tens of millions of steps (proportional to numerical magnitude)",
                    "Because dot counting only works for prime numbers",
                    "Because column addition skips carries",
                    "Because 8-digit numbers have only 1 column"
                ],
                "answer": 0,
                "solution_steps": [
                    "Dot counting creates one mark per unit, scaling as ~10^d for d-digit numbers.",
                    "Place-value column addition processes one column per digit, taking ~d steps.",
                    "Hence column addition is exponentially faster in digit count."
                ]
            },
            {
                "question": "In the 5-step column addition algorithm, what is the MAXIMUM carry c that can ever pass from one column to the next when adding two numbers?",
                "options": ["1", "2", "9", "10"],
                "answer": 0,
                "solution_steps": [
                    "Each column adds two base-10 digits (each ≤ 9) plus incoming carry c (≤ 1).",
                    "Maximum column sum = 9 + 9 + 1 = 19.",
                    "Since 19 < 20, the outgoing carry is always either 0 or 1."
                ]
            },
            {
                "question": "Trace Step 3–4 of adding 879 + 456 at the TENS column (after ones column 9 + 6 = 15 leaves carry c = 1). What is written in the tens column and what is the new carry?",
                "options": [
                    "7 + 5 + 1 = 13 → write 3, new carry c = 1",
                    "7 + 5 = 12 → write 2, new carry c = 1",
                    "7 + 5 + 1 = 13 → write 1, new carry c = 3",
                    "Write 13 in the tens place"
                ],
                "answer": 0,
                "solution_steps": [
                    "Ones column: 9 + 6 = 15 → write 5, carry c = 1.",
                    "Tens column: 7 + 5 + 1 = 13.",
                    "Write 13 mod 10 = 3, and set new carry c = 1."
                ]
            },
            {
                "question": "Which step ensures two numbers of different lengths (like 4789 + 56) align properly in the column addition algorithm?",
                "options": [
                    "Aligning rightmost ones digits and padding the shorter number on the left with leading zeros (0056)",
                    "Aligning leftmost digits",
                    "Reversing both numbers",
                    "Removing zeros"
                ],
                "answer": 0,
                "solution_steps": [
                    "Place values (1s, 10s, 100s, ...) align from right to left.",
                    "Left-padding 56 as 0056 keeps its value unchanged while matching 4-digit length.",
                    "This lets the loop iterate cleanly across d = 4 columns."
                ]
            },
            {
                "question": "What ordered list D is produced by the 1-to-n divisor algorithm for n = 20?",
                "options": [
                    "[1, 2, 4, 5, 10, 20]",
                    "[1, 2, 5, 10]",
                    "[2, 4, 5, 10, 20]",
                    "[1, 2, 4, 5, 8, 10, 20]"
                ],
                "answer": 0,
                "solution_steps": [
                    "Test i = 1 to 20 for 20 mod i = 0.",
                    "Divisors found in ascending order: 1, 2, 4, 5, 10, 20.",
                    "Output D = [1, 2, 4, 5, 10, 20]."
                ]
            },
            {
                "question": "Given divisor lists D_24 = [1, 2, 3, 4, 6, 8, 12, 24] and D_30 = [1, 2, 3, 5, 6, 10, 15, 30], what is the common list C and gcd(24, 30)?",
                "options": [
                    "C = [1, 2, 3, 6], gcd = 6",
                    "C = [1, 2, 3], gcd = 3",
                    "C = [1, 2, 6, 12], gcd = 12",
                    "C = [1, 3, 5, 6], gcd = 6"
                ],
                "answer": 0,
                "solution_steps": [
                    "Compare D_24 and D_30 to keep elements present in both.",
                    "Common elements: 1, 2, 3, 6.",
                    "Largest common element = 6."
                ]
            },
            {
                "question": "Why is the common divisor list C never empty for any two positive integers m and n?",
                "options": [
                    "1 divides every positive integer, so 1 is always in both D_m and D_n",
                    "2 always divides m and n",
                    "m always divides n",
                    "0 is always in C"
                ],
                "answer": 0,
                "solution_steps": [
                    "For any positive integer k, k mod 1 = 0.",
                    "Thus 1 ∈ D_m and 1 ∈ D_n always.",
                    "Therefore 1 ∈ C, guaranteeing gcd(m, n) ≥ 1."
                ]
            },
            {
                "question": "In the naive two-list GCD algorithm, how many total remainder checks (m mod i and n mod i) are run to build D_36 and D_48?",
                "options": [
                    "84 checks (36 + 48)",
                    "36 checks",
                    "48 checks",
                    "12 checks"
                ],
                "answer": 0,
                "solution_steps": [
                    "Building D_36 checks i = 1..36 (36 checks).",
                    "Building D_48 checks i = 1..48 (48 checks).",
                    "Total = 36 + 48 = 84 remainder checks."
                ]
            },
            {
                "question": "Which optimization cuts memory usage of the 1-to-min(m, n) GCD scan down to a single integer variable?",
                "options": [
                    "Maintaining 'best_gcd' (initialized to 1) and updating best_gcd = i whenever i divides both m and n",
                    "Storing three sorted lists",
                    "Doubling the loop limit to max(m, n)",
                    "Converting m and n to fractions"
                ],
                "answer": 0,
                "solution_steps": [
                    "Since i scans upward 1..min(m, n), each new common divisor is larger than all earlier ones.",
                    "Overwriting best_gcd = i avoids storing any list.",
                    "Memory drops to O(1) constant space."
                ]
            },
            {
                "question": "What is the maximum possible value of gcd(m, n) for two positive integers m and n?",
                "options": [
                    "min(m, n) (achieved when the smaller number divides the larger)",
                    "max(m, n)",
                    "m × n",
                    "m + n"
                ],
                "answer": 0,
                "solution_steps": [
                    "Any common divisor d must divide min(m, n), so d ≤ min(m, n).",
                    "When min(m, n) divides max(m, n) (e.g., gcd(12, 36) = 12), d = min(m, n).",
                    "Thus gcd(m, n) ≤ min(m, n) always."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Optimization Scaling Challenge",
        "subtitle": "Mastery Quiz 2 (Silent Exercise): Data Structures, 3 Optimization Stages & Value vs Digit Scaling",
        "is_quiz": True,
        "questions": [
            {
                "question": "Order the three GCD optimizations from Section 11.3.1 from FIRST to THIRD:",
                "options": [
                    "(1) Scan 1..max(m,n) for both lists → (2) Scan 1..min(m,n) for one common list → (3) Eliminate all lists with one 'best_gcd' variable",
                    "(1) Eliminate lists → (2) Scan to max(m,n) → (3) Scan to min(m,n)",
                    "(1) Scan to min(m,n) → (2) Scan to max(m,n) → (3) Use 3 lists",
                    "All three are identical"
                ],
                "answer": 0,
                "solution_steps": [
                    "Stage 1 merges the two loops into one pass up to max(m, n).",
                    "Stage 2 shrinks the bound to min(m, n) and uses a single common list.",
                    "Stage 3 replaces the list with a single variable best_gcd."
                ]
            },
            {
                "question": "For m = 1,000,000,000 and n = 2,000,000,000, why is Stage 3 (1 to min(m, n) with 'best_gcd') STILL terribly slow?",
                "options": [
                    "Because it still performs 1,000,000,000 loop iterations — scaling with numerical value rather than digit count",
                    "Because it uses too many lists",
                    "Because best_gcd cannot store 10-digit numbers",
                    "Because 1,000,000,000 has no divisors"
                ],
                "answer": 0,
                "solution_steps": [
                    "Stage 3 saves memory (O(1)), not loop iterations.",
                    "A 1-to-min(m, n) scan takes 10⁹ iterations for 10-digit inputs.",
                    "True speed requires scaling with digit count d, not value 10^d."
                ]
            },
            {
                "question": "If an algorithm takes steps proportional to the numerical value N, what happens when you add 3 more decimal digits to N?",
                "options": [
                    "The number of steps multiplies by 1,000×",
                    "The number of steps increases by 3",
                    "The number of steps triples",
                    "The runtime stays unchanged"
                ],
                "answer": 0,
                "solution_steps": [
                    "Adding 3 decimal digits multiplies N by 10³ = 1,000.",
                    "An algorithm proportional to N therefore takes 1,000× as many steps.",
                    "By contrast, a digit-count algorithm only adds a small constant number of steps."
                ]
            },
            {
                "question": "If we reverse the Stage 3 scan to go DOWNWARD from min(m, n) to 1, when does it finish fastest?",
                "options": [
                    "When gcd(m, n) is large (e.g., gcd(1000, 500) = 500 finishes on the very first check!)",
                    "When m and n are coprime (gcd = 1)",
                    "When m = 1000 and n = 999",
                    "Never faster than upward scan"
                ],
                "answer": 0,
                "solution_steps": [
                    "Scanning downward exits at the first common divisor i.",
                    "For (1000, 500), i = 500 matches immediately in 1 step!",
                    "For coprime (1000, 999), it still scans all 999 steps down to 1."
                ]
            },
            {
                "question": "What is a 'data structure' in algorithm design?",
                "options": [
                    "An organized way to store and manage intermediate data (like ordered lists or single variables) during computation",
                    "A physical computer monitor",
                    "Only a prime number",
                    "A graph drawn on paper without numbers"
                ],
                "answer": 0,
                "solution_steps": [
                    "Ordered lists D_m, D_n, C are data structures storing collections of divisors.",
                    "Choosing a single variable best_gcd instead of a list is a data-structure optimization.",
                    "Right data structures simplify logic and save memory."
                ]
            },
            {
                "question": "In Stage 1 (scanning i = 1 to max(m, n)), why must we check 'i divides m' and 'i divides n' separately inside the loop?",
                "options": [
                    "Because a divisor of m might not divide n (so it belongs in D_m only), and vice versa",
                    "Because i cannot divide both",
                    "Because max(m, n) is always odd",
                    "To make the list unsorted"
                ],
                "answer": 0,
                "solution_steps": [
                    "Stage 1 still builds both full divisor lists D_m and D_n.",
                    "Some i divide only m, some only n, and some both.",
                    "Stage 2 avoids this by testing 'm mod i == 0 AND n mod i == 0' up to min(m, n)."
                ]
            },
            {
                "question": "Which input pair represents the WORST CASE for the downward 1-to-min(m, n) GCD scan?",
                "options": [
                    "Consecutive integers like (10000, 9999), whose GCD is 1",
                    "(10000, 5000), whose GCD is 5000",
                    "(10000, 10000), whose GCD is 10000",
                    "(10000, 2500), whose GCD is 2500"
                ],
                "answer": 0,
                "solution_steps": [
                    "Consecutive integers are always coprime: gcd(n, n−1) = 1.",
                    "Downward scan must test every integer from 9999 down to 1.",
                    "Total checks = 9,999!"
                ]
            },
            {
                "question": "How many steps does adding two 50-digit numbers take using the 5-step digit-by-digit algorithm?",
                "options": [
                    "50 column additions (plus at most 1 final carry write)",
                    "10⁵⁰ steps",
                    "2500 steps",
                    "1 step"
                ],
                "answer": 0,
                "solution_steps": [
                    "Each of the 50 aligned columns requires 1 small addition + carry update.",
                    "Steps = 50 (linear in digit count d = 50).",
                    "Completely independent of the 10⁵⁰ numerical magnitude!"
                ]
            },
            {
                "question": "What happens if an algorithm has a loop condition that never becomes false?",
                "options": [
                    "It enters an infinite loop and fails the 'Termination' requirement of a valid algorithm",
                    "It becomes twice as fast",
                    "It automatically returns 0",
                    "It scales with digit count"
                ],
                "answer": 0,
                "solution_steps": [
                    "Every valid algorithm must terminate in a finite number of steps.",
                    "A non-terminating loop hangs forever.",
                    "Termination proofs verify that a loop counter or remainder reaches the stop condition."
                ]
            },
            {
                "question": "Which statement best captures Section 11.3.2's main lesson on efficiency?",
                "options": [
                    "True efficiency for large-number arithmetic means scaling with the number of digits d, not with the numerical magnitude 10^d",
                    "Eliminating lists always makes an algorithm run in 1 step",
                    "1-to-min(m, n) is fast for 100-digit numbers",
                    "Only addition can scale with digit count"
                ],
                "answer": 0,
                "solution_steps": [
                    "1-to-min(m, n) scales with N ≈ 10^d (exponential in digits d).",
                    "Digit-scaling algorithms (like column addition and Āryabhaṭa's GCD) take O(d) steps.",
                    "This exponential gap separates impractical algorithms from fast ones."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Euclid Āryabhaṭa Challenge",
        "subtitle": "Mastery Quiz 3 (Silent Exercise): Euclid Subtraction, Āryabhaṭa Division & Al-Khwārizmī History",
        "is_quiz": True,
        "questions": [
            {
                "question": "What geometric idea justifies Euclid's subtraction identity gcd(m, n) = gcd(n, m − n) for m > n?",
                "options": [
                    "Any square tile of side d that tiles an m × n rectangle also tiles the remaining n × (m − n) rectangle after removing one n × n square",
                    "Every rectangle is a square",
                    "Subtracting n always halves m",
                    "Area equals perimeter"
                ],
                "answer": 0,
                "solution_steps": [
                    "If d divides both m and n, then d divides m − n.",
                    "Conversely, if d divides both n and m − n, then d divides n + (m − n) = m.",
                    "So (m, n) and (n, m − n) share the exact same common divisors and GCD."
                ]
            },
            {
                "question": "Trace Euclid's subtraction algorithm on (35, 14). How many subtractions occur before both numbers become equal?",
                "options": [
                    "3 subtractions: (35, 14) → (21, 14) → (7, 14) → (7, 7) ⇒ GCD = 7",
                    "2 subtractions ⇒ GCD = 14",
                    "5 subtractions ⇒ GCD = 7",
                    "1 subtraction ⇒ GCD = 21"
                ],
                "answer": 0,
                "solution_steps": [
                    "Step 1: 35 − 14 = 21 → (21, 14).",
                    "Step 2: 21 − 14 = 7 → (7, 14).",
                    "Step 3: 14 − 7 = 7 → (7, 7) ⇒ GCD = 7."
                ]
            },
            {
                "question": "How many subtraction steps does Euclid's subtraction algorithm take on gcd(201, 2)?",
                "options": [
                    "100 subtractions (201 → 199 → ... → 1, then 2 − 1 = 1)",
                    "2 subtractions",
                    "10 subtractions",
                    "1 subtraction"
                ],
                "answer": 0,
                "solution_steps": [
                    "For gcd(2k + 1, 2) with k = 100, subtracting 2 takes 100 steps to reach (1, 2).",
                    "One final subtraction 2 − 1 = 1 gives (1, 1) (101 total steps, ~k subtractions).",
                    "This demonstrates why repeated subtraction is slow for unbalanced pairs."
                ]
            },
            {
                "question": "How does Āryabhaṭa's division algorithm compute gcd(201, 2) in contrast?",
                "options": [
                    "In 2 modulo steps: (201, 2) → (2, 1) → (1, 0) ⇒ GCD = 1",
                    "In 100 steps",
                    "In 201 steps",
                    "In 50 steps"
                ],
                "answer": 0,
                "solution_steps": [
                    "Step 1: 201 mod 2 = 1 → new pair (2, 1).",
                    "Step 2: 2 mod 1 = 0 → new pair (1, 0).",
                    "Stop at remainder 0 and return 1!"
                ]
            },
            {
                "question": "Trace Āryabhaṭa's division algorithm on gcd(391, 299).",
                "options": [
                    "(391, 299) → (299, 92) → (92, 23) → (23, 0) ⇒ GCD = 23",
                    "(391, 299) → (299, 92) → (92, 13) ⇒ GCD = 13",
                    "(391, 299) → (299, 102) ⇒ GCD = 1",
                    "GCD = 29"
                ],
                "answer": 0,
                "solution_steps": [
                    "391 mod 299 = 92 → (299, 92).",
                    "299 mod 92 = 23 (since 3×92 = 276, 299−276 = 23) → (92, 23).",
                    "92 mod 23 = 0 → GCD = 23."
                ]
            },
            {
                "question": "In which classical Indian text (499 CE) does Āryabhaṭa's remainder-based GCD / kuttaka division method appear?",
                "options": ["Āryabhaṭīya", "Brāhmasphuṭasiddhānta", "Pātīganita", "Elements"],
                "answer": 0,
                "solution_steps": [
                    "Āryabhaṭa composed the Āryabhaṭīya in 499 CE.",
                    "It presents the remainder-based division reduction for GCD and linear congruences.",
                    "Hence Āryabhaṭīya is correct."
                ]
            },
            {
                "question": "Why does Āryabhaṭa's division algorithm finish in O(d) steps for d-digit numbers?",
                "options": [
                    "Every two modulo steps reduce the larger number by at least half, shrinking 10^d to 0 in steps proportional to d",
                    "Because remainders are always 1",
                    "Because it only checks even numbers",
                    "Because it adds the digits"
                ],
                "answer": 0,
                "solution_steps": [
                    "In two consecutive steps (m, n) → (n, r₁) → (r₁, r₂), it is guaranteed that r₁ < m/2 or r₂ < n/2.",
                    "Halving repeatedly takes at most ~2·log₂(n) ≈ 6.6·d steps for d-digit numbers.",
                    "Thus runtime scales linearly with digit count d!"
                ]
            },
            {
                "question": "Who was Al-Khwārizmī, and how is his name connected to 'algorithm'?",
                "options": [
                    "A 9th-century Persian scholar whose treatise on Indian decimal arithmetic was Latinized as 'Liber Algorismi', giving us 'algorithm'",
                    "A Greek geometer who wrote Elements",
                    "A 19th-century computer programmer",
                    "A Roman emperor"
                ],
                "answer": 0,
                "solution_steps": [
                    "Al-Khwārizmī (c. 825 CE) wrote a foundational book explaining Indian base-10 numerals and arithmetic.",
                    "12th-century Latin translations titled 'Liber Algorismi' turned his name into 'algorism'.",
                    "This evolved into the modern word 'algorithm'."
                ]
            },
            {
                "question": "In Āryabhaṭa's algorithm, what is the base-case stopping rule?",
                "options": [
                    "When the second argument (remainder) reaches 0, stop and return the first argument: gcd(d, 0) = d",
                    "When both arguments equal 1",
                    "When the first argument becomes negative",
                    "After 10 divisions"
                ],
                "answer": 0,
                "solution_steps": [
                    "Every integer d divides 0 evenly (0 = 0 × d).",
                    "Therefore the greatest common divisor of d and 0 is d itself.",
                    "So (d, 0) triggers immediate return of d."
                ]
            },
            {
                "question": "What happens if we accidentally call Āryabhaṭa's gcd(m, n) with m < n (e.g., gcd(18, 48))?",
                "options": [
                    "The very first step computes 18 mod 48 = 18 and swaps them cleanly into gcd(48, 18)!",
                    "It crashes with a negative remainder",
                    "It enters an infinite loop",
                    "It returns 0"
                ],
                "answer": 0,
                "solution_steps": [
                    "When m < n, quotient is 0 and remainder is m mod n = m.",
                    "So (m, n) becomes (n, m), automatically putting the larger number first!",
                    "One extra step handles m < n effortlessly."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Primes Proofs Mastery",
        "subtitle": "Mastery Quiz 4 (Silent Exercise): LCM via GCD, prime(n) Up to √n, Factorization & Correctness",
        "is_quiz": True,
        "questions": [
            {
                "question": "Compute lcm(45, 60) using Āryabhaṭa's GCD and the identity lcm(m, n) = (m / gcd(m, n)) × n.",
                "options": ["180", "2700", "90", "360"],
                "answer": 0,
                "solution_steps": [
                    "Find gcd(60, 45): (60, 45) → (45, 15) → (15, 0) ⇒ gcd = 15.",
                    "Compute (45 / 15) × 60 = 3 × 60.",
                    "lcm(45, 60) = 180."
                ]
            },
            {
                "question": "To test if n = 251 is prime using the optimized prime(n) algorithm, which integers d must be checked?",
                "options": [
                    "Integers from d = 2 up to 15 (since 15² = 225 ≤ 251 < 16² = 256)",
                    "Integers from 2 up to 250",
                    "Integers from 2 up to 125",
                    "Only d = 2 and d = 3"
                ],
                "answer": 0,
                "solution_steps": [
                    "Any composite factor pair {a, b} of 251 must have min(a, b) ≤ √251.",
                    "Since 15² = 225 and 16² = 256, ⌊√251⌋ = 15.",
                    "Testing d = 2..15 (none divide 251) proves 251 is prime in 14 checks!"
                ]
            },
            {
                "question": "In prime(n), why MUST the algorithm return FALSE for n = 1?",
                "options": [
                    "By definition, a prime number has exactly two distinct positive factors (1 and itself); 1 has only one factor",
                    "Because 1 is even",
                    "Because 1 is divisible by 2",
                    "Because √1 = 1"
                ],
                "answer": 0,
                "solution_steps": [
                    "Primes require exactly 2 positive divisors: 1 and n.",
                    "n = 1 has only 1 positive divisor {1}.",
                    "Hence n ≤ 1 must return False immediately."
                ]
            },
            {
                "question": "For n = 10,000,000, approximately how many trial divisions does the √n prime(n) algorithm save compared to checking 2..n−1?",
                "options": [
                    "It checks only up to ~3,162 instead of ~10,000,000 (over 3,000× fewer checks!)",
                    "It saves only 10 checks",
                    "It checks 5,000,000 numbers",
                    "It takes the same number of checks"
                ],
                "answer": 0,
                "solution_steps": [
                    "√10,000,000 ≈ 3,162.27.",
                    "Naive 2..n−1 runs nearly 10⁷ checks.",
                    "Optimized 2..⌊√n⌋ runs at most 3,161 checks."
                ]
            },
            {
                "question": "What are the two essential parts of a formal Proof of Correctness for an algorithm?",
                "options": [
                    "Termination (proving it always stops in finite steps) and Invariant / Partial Correctness (proving it returns the exact right output)",
                    "Testing on 2 inputs and formatting the output",
                    "Using a list and a loop",
                    "Naming variables x and y"
                ],
                "answer": 0,
                "solution_steps": [
                    "An algorithm is correct only if it (1) finishes in finite steps for every valid input,",
                    "and (2) produces the mathematically guaranteed answer upon stopping.",
                    "Termination + loop invariant establish both."
                ]
            },
            {
                "question": "In prime factorization by trial division (dividing n repeatedly by d = 2, 3, ... while d² ≤ n), why do we divide out ALL copies of d before incrementing d?",
                "options": [
                    "So that any later divisor d that divides the reduced n is guaranteed to be prime (since all smaller prime factors were already removed)",
                    "To make n larger",
                    "Because primes only occur once",
                    "To skip 2"
                ],
                "answer": 0,
                "solution_steps": [
                    "Dividing out all factors of 2 removes every multiple of 2 (like 4, 6, 8) as future divisors.",
                    "In general, removing all smaller prime factors ensures the next d dividing n cannot be composite.",
                    "And if remaining n > 1 after d² > n, that leftover n itself is prime!"
                ]
            },
            {
                "question": "Trace Āryabhaṭa's division algorithm on gcd(377, 233) (consecutive Fibonacci numbers!). How many modulo steps does it take?",
                "options": [
                    "12 steps (consecutive Fibonacci numbers are the worst-case input for Āryabhaṭa's GCD, yet still take only ~12 steps for 3-digit numbers!)",
                    "1 step",
                    "233 steps",
                    "377 steps"
                ],
                "answer": 0,
                "solution_steps": [
                    "377 mod 233 = 144 → 233 mod 144 = 89 → 144 mod 89 = 55 → 89 mod 55 = 34 → 55 mod 34 = 21 → 34 mod 21 = 13 → 21 mod 13 = 8 → 13 mod 8 = 5 → 8 mod 5 = 3 → 5 mod 3 = 2 → 3 mod 2 = 1 → 2 mod 1 = 0.",
                    "Total: 12 steps, yielding GCD = 1.",
                    "Even the worst case for Āryabhaṭa's algorithm scales linearly with digit count!"
                ]
            },
            {
                "question": "Why is dividing m by gcd(m, n) BEFORE multiplying by n in lcm(m, n) = (m / gcd(m, n)) × n good engineering practice?",
                "options": [
                    "It keeps the intermediate number smaller, preventing unnecessary integer overflow on large inputs",
                    "Because m × n is always odd",
                    "Because division is always approximate",
                    "Because gcd(m, n) never divides m"
                ],
                "answer": 0,
                "solution_steps": [
                    "Since gcd(m, n) divides m evenly, m / gcd(m, n) is an exact integer.",
                    "Dividing first shrinks the factor before multiplying by n.",
                    "This avoids oversized intermediate products m × n."
                ]
            },
            {
                "question": "Which algorithm from Chapter 11 inspired the very word 'algorithm' via Al-Khwārizmī's Latinized book?",
                "options": [
                    "Indian base-10 place-value arithmetic (digit-by-digit addition, subtraction, multiplication, division)",
                    "Dot counting",
                    "1-to-min(m, n) GCD scanning",
                    "Trial division up to n − 1"
                ],
                "answer": 0,
                "solution_steps": [
                    "Al-Khwārizmī's 9th-century treatise taught Indian decimal numerals and place-value operations.",
                    "12th-century Latin translations ('Liber Algorismi') coined 'algorism' for decimal calculation.",
                    "This evolved into 'algorithm'."
                ]
            },
            {
                "question": "Which summary statement best captures Chapter 11 (The World of Algorithms)?",
                "options": [
                    "Great algorithms combine clean problem decomposition, smart data structures, formal correctness proofs (termination + invariant), and efficiency scaling with digit count rather than numerical magnitude",
                    "Any algorithm that gets the right answer on 1-digit numbers is fast enough for 50-digit numbers",
                    "Dot counting and 1-to-min(m,n) scanning scale with digit count",
                    "Correctness means never using loops"
                ],
                "answer": 0,
                "solution_steps": [
                    "Decomposition (Section 11.2), data structures (11.3), and optimization (11.3.1) build clean solutions.",
                    "Efficiency analysis (11.3.2–11.3.4) shows why digit-scaling (column addition, Āryabhaṭa's GCD) beats value-scaling.",
                    "Termination + loop invariants prove correctness."
                ]
            }
        ]
    }
]

for _s in slides_part3:
    for _q in _s["questions"]:
        _q.setdefault("hint", _q["solution_steps"][0])
        _q.setdefault("explanation", _q["solution_steps"][-1])

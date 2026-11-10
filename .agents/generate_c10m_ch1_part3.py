#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 1: Real Numbers
Data Generator - Part 3 (Slides 17 to 20: Exercises 1.1, 1.2 & Challenges)
Strict constraints:
- Titles: Strictly 1 to 3 words each ('Exercise 1.1 Quiz', 'Exercise 1.2 Quiz', 'Challenge Quiz 1', 'Challenge Quiz 2')
- Questions: Exactly 10 questions per slide (40 questions total)
- Zero spoken lecture on Exercise/Quiz slides ("except exercises")
- Zero fictional human character names (Raghav, Sonia, Ravi, etc.), zero lecturer personas
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Exercise 1.1 Quiz",
        "subtitle": "Exercise 1.1 Practice: Prime Factorizations, HCF × LCM Verification, 6ⁿ & Circular Path",
        "questions": [
            {
                "question": "Express the composite number 140 cleanly as a product of its prime factors (Exercise 1.1 Q1):",
                "options": [
                    "2² × 5 × 7",
                    "2 × 5² × 7",
                    "2³ × 3 × 7",
                    "4 × 35"
                ],
                "answer": 0,
                "hint": "140 = 2 × 70 = 2 × 2 × 35, and remember 4 is composite, not prime!",
                "explanation": "Factoring 140 down completely to primes gives 2 × 2 × 5 × 7 = 2² × 5 × 7.",
                "solution_steps": [
                    "Divide 140 repeatedly by smallest prime 2: 140 ÷ 2 = 70, 70 ÷ 2 = 35.",
                    "Factor odd quotient 35 cleanly into primes: 35 = 5 × 7.",
                    "Write in exponential prime form: 2² × 5 × 7."
                ]
            },
            {
                "question": "Express the composite integer 156 as a product of its prime factors:",
                "options": [
                    "2² × 3 × 13",
                    "2 × 3² × 13",
                    "2² × 39",
                    "3 × 4 × 13"
                ],
                "answer": 0,
                "hint": "Divide 156 twice by 2 to get 39, then split 39 into primes!",
                "explanation": "156 = 2 × 78 = 2 × 2 × 39 = 2² × 3 × 13.",
                "solution_steps": [
                    "Halve 156 twice: 156 ÷ 2 = 78; 78 ÷ 2 = 39.",
                    "Divide 39 by prime 3: 39 = 3 × 13 (13 is prime).",
                    "Combine prime powers: 2² × 3 × 13."
                ]
            },
            {
                "question": "What is the unique prime factorization of 3825 (Exercise 1.1 Q1)?",
                "options": [
                    "3² × 5² × 17",
                    "3 × 5³ × 11",
                    "3² × 5 × 19",
                    "5² × 9 × 17"
                ],
                "answer": 0,
                "hint": "Test divisibility by 3 (sum of digits = 18), then 3 again, then 5!",
                "explanation": "3825 ÷ 3 = 1275; 1275 ÷ 3 = 425; 425 ÷ 5 = 85; 85 ÷ 5 = 17, giving 3² × 5² × 17.",
                "solution_steps": [
                    "Divide twice by 3: 3825 = 9 × 425.",
                    "Divide 425 twice by 5: 425 = 25 × 17.",
                    "Verify 17 is prime -> 3² × 5² × 17."
                ]
            },
            {
                "question": "Find the prime factorization of 5005 (Exercise 1.1 Q1):",
                "options": [
                    "5 × 7 × 11 × 13",
                    "5 × 1001",
                    "5² × 7 × 13",
                    "3 × 5 × 11 × 17"
                ],
                "answer": 0,
                "hint": "5005 = 5 × 1001; recall 1001 = 7 × 143!",
                "explanation": "5005 ÷ 5 = 1001; 1001 ÷ 7 = 143; 143 ÷ 11 = 13, yielding four distinct primes 5 × 7 × 11 × 13.",
                "solution_steps": [
                    "Divide by 5 -> quotient 1001.",
                    "Test prime 7: 1001 = 7 × 143.",
                    "Factor 143 = 11 × 13 -> 5 × 7 × 11 × 13."
                ]
            },
            {
                "question": "Find the LCM and HCF of 26 and 91, and check their product (Exercise 1.1 Q2):",
                "options": [
                    "HCF = 13, LCM = 182 (both 13 × 182 and 26 × 91 equal 2,366)",
                    "HCF = 7, LCM = 260 (product 1,820)",
                    "HCF = 2, LCM = 1,183",
                    "HCF = 13, LCM = 91"
                ],
                "answer": 0,
                "hint": "Factor 26 = 2 × 13 and 91 = 7 × 13!",
                "explanation": "Common prime is 13¹ (HCF = 13); LCM = 2 × 7 × 13 = 182. Product: 13 × 182 = 2366 = 26 × 91.",
                "solution_steps": [
                    "Factor both integers: 26 = 2 × 13, 91 = 7 × 13.",
                    "HCF (smallest common prime) = 13; LCM (all primes greatest powers) = 2 × 7 × 13 = 182.",
                    "Verify 13 × 182 = 2,366 = 26 × 91."
                ]
            },
            {
                "question": "Compute HCF(12, 15, 21) and LCM(12, 15, 21) by prime factorization (Exercise 1.1 Q3):",
                "options": [
                    "HCF = 3, LCM = 420",
                    "HCF = 1, LCM = 180",
                    "HCF = 3, LCM = 210",
                    "HCF = 6, LCM = 420"
                ],
                "answer": 0,
                "hint": "12 = 2² × 3, 15 = 3 × 5, 21 = 3 × 7!",
                "explanation": "Common prime across all three is 3¹ = 3; LCM uses highest powers 2² × 3 × 5 × 7 = 420.",
                "solution_steps": [
                    "Prime factorize: 12 = 2² × 3, 15 = 3 × 5, 21 = 3 × 7.",
                    "HCF = smallest power of common prime 3 = 3.",
                    "LCM = 2² × 3 × 5 × 7 = 4 × 105 = 420."
                ]
            },
            {
                "question": "Given HCF(306, 657) = 9, find LCM(306, 657) (Exercise 1.1 Q4):",
                "options": [
                    "22,338",
                    "20,104",
                    "24,516",
                    "18,927"
                ],
                "answer": 0,
                "hint": "Use LCM = (306 × 657) ÷ 9 = 34 × 657!",
                "explanation": "Using HCF(a, b) × LCM(a, b) = a × b gives LCM = (306 ÷ 9) × 657 = 34 × 657 = 22,338.",
                "solution_steps": [
                    "Apply identity: 9 × LCM = 306 × 657.",
                    "Divide 306 by 9 to simplify cleanly -> 34.",
                    "Multiply 34 × 657 = 22,338."
                ]
            },
            {
                "question": "Can 6ⁿ end with the digit 0 for any natural number n (Exercise 1.1 Q5)?",
                "options": [
                    "No; 6ⁿ = 2ⁿ × 3ⁿ lacks prime factor 5, which is strictly required to end in 0",
                    "Yes, whenever n = 5",
                    "Yes, whenever n is an even multiple of 10",
                    "No, solely because 6 is greater than 5"
                ],
                "answer": 0,
                "hint": "Ending in digit 0 means divisibility by 10 = 2 × 5!",
                "explanation": "By uniqueness of Theorem 1.1, the only primes dividing 6ⁿ = 2ⁿ × 3ⁿ are 2 and 3; since 5 is absent, 6ⁿ cannot end with 0.",
                "solution_steps": [
                    "Recognize numbers ending in 0 must contain prime factors 2 and 5.",
                    "Factor 6ⁿ = (2 × 3)ⁿ = 2ⁿ × 3ⁿ.",
                    "Invoke Fundamental Theorem of Arithmetic uniqueness: 5 never appears."
                ]
            },
            {
                "question": "Which explanation correctly proves 7 × 11 × 13 + 13 is a composite number (Exercise 1.1 Q6)?",
                "options": [
                    "Factoring out 13 gives 13 × (7 × 11 + 1) = 13 × 78, exhibiting factors other than 1 and itself",
                    "Because every number containing prime 7 is automatically composite",
                    "Because multiplying two odd primes always yields zero",
                    "Because adding 13 turns every composite number prime"
                ],
                "answer": 0,
                "hint": "Factor out common 13 using the distributive property!",
                "explanation": "7 × 11 × 13 + 13 = 13 × 78 = 2 × 3 × 13², having multiple prime factors other than 1 and itself.",
                "solution_steps": [
                    "Identify common factor 13 in both additive terms.",
                    "Rewrite cleanly as 13 × (7 × 11 + 1) = 13 × 78.",
                    "Conclude more than two positive divisors prove it is composite."
                ]
            },
            {
                "question": "Two runners start together around a circular track in the same direction; Runner A takes 18 min and Runner B takes 12 min per lap. When do they reunite at the starting point (Exercise 1.1 Q7)?",
                "options": [
                    "After 36 minutes",
                    "After 6 minutes",
                    "After 30 minutes",
                    "After 54 minutes"
                ],
                "answer": 0,
                "hint": "They reunite at the least common multiple LCM(18, 12)!",
                "explanation": "18 = 2 × 3² and 12 = 2² × 3, so LCM(18, 12) = 2² × 3² = 36 minutes.",
                "solution_steps": [
                    "Recognize simultaneous starting-line reunion equals LCM(18, 12).",
                    "Factor 18 = 2 × 3² and 12 = 2² × 3.",
                    "Compute LCM = 2² × 3² = 4 × 9 = 36 minutes."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Exercise 1.2 Quiz",
        "subtitle": "Exercise 1.2 & Section 1.3 Practice: Proving √5, 3+2√5, 1/√2, 7√5 & 6+√2 Irrational",
        "questions": [
            {
                "question": "State the exact hypothesis and conclusion of Theorem 1.2 used across all irrational root proofs:",
                "options": [
                    "If prime p divides a² (for positive integer a), then prime p divides a",
                    "If composite c divides a², then c always divides a",
                    "If prime p divides a + b, then p divides a",
                    "If p divides a, then a must be odd"
                ],
                "answer": 0,
                "hint": "Remember primality of p is mandatory for p | a² ⟹ p | a!",
                "explanation": "Theorem 1.2 proves via unique prime factorization that whenever prime p divides a², p must divide a.",
                "solution_steps": [
                    "Recall Theorem 1.2 states prime p divides a² implies p divides a.",
                    "Rule out composite divisors using counterexample 4 | 6² yet 4 ∤ 6.",
                    "Confirm positive integer condition for a."
                ]
            },
            {
                "question": "In proving √5 is irrational by contradiction (Exercise 1.2 Q1), suppose √5 = a/b with coprime integers a, b ≠ 0. What follows squaring 5b² = a²?",
                "options": [
                    "5 divides a², so 5 divides a by Theorem 1.2; setting a = 5c gives b² = 5c², forcing 5 to divide b too",
                    "5 divides b immediately without dividing a",
                    "a must equal 1 and b must equal 5",
                    "5b = a² proves a and b are even"
                ],
                "answer": 0,
                "hint": "Follow the exact two-step Theorem 1.2 chain used in √2, swapping 2 with 5!",
                "explanation": "5 | a² ⟹ 5 | a ⟹ a = 5c ⟹ 5b² = 25c² ⟹ b² = 5c² ⟹ 5 | b, contradicting coprimality of a and b.",
                "solution_steps": [
                    "From 5b² = a², note prime 5 divides a², hence 5 divides a.",
                    "Substitute a = 5c -> 5b² = 25c² -> b² = 5c².",
                    "Deduce 5 divides b, contradicting coprime a, b."
                ]
            },
            {
                "question": "When proving 3 + 2√5 is irrational (Exercise 1.2 Q2), assume 3 + 2√5 = a/b (a, b integers, b ≠ 0). Which isolation produces the contradiction?",
                "options": [
                    "√5 = (a − 3b) / (2b), claiming irrational √5 equals a rational quotient of integers",
                    "√5 = (a + 3b) / b",
                    "√5 = 2a − 3b",
                    "√5 = 3a / (2b)"
                ],
                "answer": 0,
                "hint": "Subtract 3 from a/b first, then divide both sides by 2!",
                "explanation": "2√5 = a/b − 3 = (a − 3b)/b, so √5 = (a − 3b)/(2b), contradicting that √5 is irrational.",
                "solution_steps": [
                    "Move integer 3 to right: 2√5 = (a − 3b)/b.",
                    "Divide both sides by nonzero integer 2: √5 = (a − 3b)/(2b).",
                    "Spot integer ratio on right contradicting irrational √5 on left."
                ]
            },
            {
                "question": "In Exercise 1.2 Q3(i), how is 1/√2 cleanly proved irrational after assuming 1/√2 = a/b (coprime integers a, b ≠ 0)?",
                "options": [
                    "Flip reciprocals to get √2 = b/a (rational), contradicting Theorem 1.3 that √2 is irrational",
                    "Add 1 to both sides getting 1 + 1/√2 = 2",
                    "Claim a = 0 immediately",
                    "Multiply both sides by zero"
                ],
                "answer": 0,
                "hint": "Taking reciprocals turns 1/√2 directly into √2!",
                "explanation": "Taking reciprocals (note a ≠ 0 since 1/√2 ≠ 0) gives √2 = b/a, an integer ratio contradicting irrationality of √2.",
                "solution_steps": [
                    "Verify a ≠ 0 since 1/√2 ≠ 0.",
                    "Invert both sides cleanly: √2 = b/a.",
                    "Contradict Theorem 1.3 (√2 is irrational)."
                ]
            },
            {
                "question": "Alternatively, rationalizing the denominator of 1/√2 expresses it as:",
                "options": [
                    "√2 / 2, which would make √2 = 2a/b if 1/√2 = a/b",
                    "2 / √2 = 1",
                    "√2 / 4",
                    "1 / 2"
                ],
                "answer": 0,
                "hint": "Multiply top and bottom of 1/√2 by √2!",
                "explanation": "1/√2 = √2/2; assuming √2/2 = a/b implies √2 = 2a/b (rational), creating the same contradiction.",
                "solution_steps": [
                    "Multiply numerator and denominator by √2: √2 / (√2 × √2) = √2 / 2.",
                    "Equate √2 / 2 = a/b -> √2 = 2a/b.",
                    "Notice rational right side contradicts irrational √2."
                ]
            },
            {
                "question": "In Exercise 1.2 Q3(ii), assuming 7√5 = a/b (a, b integers, b ≠ 0), what step proves 7√5 is irrational?",
                "options": [
                    "√5 = a / (7b), forcing irrational √5 to equal rational fraction a/(7b)",
                    "√5 = 7a / b",
                    "7 = a / (5b)",
                    "√7 = a / (5b)"
                ],
                "answer": 0,
                "hint": "Divide both sides by 7 cleanly!",
                "explanation": "Dividing by 7 yields √5 = a/(7b); since a and 7b (≠ 0) are integers, a/(7b) is rational, contradicting √5 irrationality.",
                "solution_steps": [
                    "Assume 7√5 = a/b with integers a, b ≠ 0.",
                    "Divide both sides by 7: √5 = a/(7b).",
                    "Contradict known irrationality of √5."
                ]
            },
            {
                "question": "In Exercise 1.2 Q3(iii), assuming 6 + √2 = a/b (integers a, b ≠ 0), which isolation completes the contradiction proof?",
                "options": [
                    "√2 = (a − 6b) / b, asserting irrational √2 equals rational integer ratio (a − 6b)/b",
                    "√2 = 6b / a",
                    "√2 = (a + 6b) / b",
                    "6 = √2 − a/b"
                ],
                "answer": 0,
                "hint": "Subtract 6 from both sides and combine over denominator b!",
                "explanation": "√2 = a/b − 6 = (a − 6b)/b is rational because a − 6b and b ≠ 0 are integers, contradicting Theorem 1.3.",
                "solution_steps": [
                    "Subtract 6 cleanly from both sides: √2 = a/b − 6.",
                    "Combine fraction: √2 = (a − 6b)/b.",
                    "Contradict Theorem 1.3 (√2 is irrational)."
                ]
            },
            {
                "question": "Which general property allows quick 4-line contradiction proofs for 5 − √3 and 3 + 2√5 once √3 and √5 are known irrational?",
                "options": [
                    "Closure of rational numbers under addition, subtraction, multiplication, and non-zero division",
                    "Because rational numbers are never closed under subtraction",
                    "Because adding integers turns √3 into 3",
                    "Because every negative root equals zero"
                ],
                "answer": 0,
                "hint": "Combining any rational with integers (+, −, ×, ÷ nonzero) stays rational!",
                "explanation": "Since rationals are closed under arithmetic (+, −, ×, ÷ nonzero), isolating the irrational root on one side traps it equal to a rational.",
                "solution_steps": [
                    "Note integers/rationals combine under +, −, ×, ÷(≠0) to give rationals.",
                    "Isolate √p alone by inverse arithmetic moves.",
                    "Clash between rational value and proven irrational √p ends proof."
                ]
            },
            {
                "question": "In Example 9 of the textbook (proving √3 irrational), after 3b² = a², why are we guaranteed a and b CANNOT both be multiples of 3?",
                "options": [
                    "We explicitly canceled common factors beforehand so a and b are chosen COPRIME (HCF = 1)",
                    "Because multiples of 3 are always negative",
                    "Because 3 never divides square numbers",
                    "Because b was chosen equal to 0"
                ],
                "answer": 0,
                "hint": "Look at the reduced rational fraction step at the start of the proof!",
                "explanation": "Reducing initial r/s by HCF gives coprime integers a, b; proving 3 divides both a and b yields HCF ≥ 3, creating the contradiction.",
                "solution_steps": [
                    "Start with √3 = r/s and divide by common factors to get coprime a/b.",
                    "Coprime means HCF(a, b) = 1.",
                    "Algebra proving 3 | a and 3 | b forces HCF ≥ 3 (contradiction)."
                ]
            },
            {
                "question": "If integer p is PRIME, which statement holds universally across all Real Numbers?",
                "options": [
                    "√p is strictly an irrational number",
                    "√p is always a terminating decimal",
                    "√p equals p/2",
                    "√p is an even integer whenever p ≥ 3"
                ],
                "answer": 0,
                "hint": "Theorem 1.3 for p = 2 generalizes seamlessly to every prime integer p!",
                "explanation": "Applying Theorem 1.2 with any prime p proves √p = a/b forces p | a and p | b, making √p irrational for every prime p.",
                "solution_steps": [
                    "Substitute generic prime p into Theorem 1.3 proof: pb² = a².",
                    "Theorem 1.2 gives p | a ⟹ a = pc ⟹ b² = pc² ⟹ p | b.",
                    "Coprime contradiction proves √p irrational for all primes p."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge Quiz 1",
        "subtitle": "Mastery Challenge: Euclid's Algorithm, Decimal Expansions, Factor Trees & Gauss Theorem 1.1",
        "questions": [
            {
                "question": "Use Euclid's division steps to find HCF(135, 225):",
                "options": [
                    "45",
                    "15",
                    "90",
                    "5"
                ],
                "answer": 0,
                "hint": "225 = 135×1 + 90; next 135 = 90×1 + 45; next 90 = 45×2 + 0!",
                "explanation": "Remainder becomes 0 when dividing 90 by 45, making final divisor 45 = HCF(135, 225).",
                "solution_steps": [
                    "225 = 135 × 1 + 90.",
                    "135 = 90 × 1 + 45.",
                    "90 = 45 × 2 + 0 -> HCF = 45."
                ]
            },
            {
                "question": "Use Euclid's division steps to find HCF(196, 38220):",
                "options": [
                    "196",
                    "98",
                    "14",
                    "195"
                ],
                "answer": 0,
                "hint": "Test 196 × 195 carefully!",
                "explanation": "38,220 = 196 × 195 + 0 directly on the first division step, so divisor 196 itself is the HCF!",
                "solution_steps": [
                    "Divide 38,220 by 196 -> quotient 195.",
                    "Check remainder: 196 × 195 = 38,220 -> remainder 0.",
                    "Zero remainder on Step 1 yields HCF = 196."
                ]
            },
            {
                "question": "Without performing long division, which rational number yields a TERMINATING decimal expansion?",
                "options": [
                    "17 / 8",
                    "64 / 455",
                    "29 / 343",
                    "77 / 210"
                ],
                "answer": 0,
                "hint": "Check simplified denominator prime factors: only 2 and 5 allow termination!",
                "explanation": "In 17/8, q = 8 = 2³ (pure power of 2 -> 2.125). Note 455 = 5×7×13, 343 = 7³, and 77/210 = 11/30 (30 = 2×3×5) all contain non-2/5 primes.",
                "solution_steps": [
                    "Simplify fractions completely first: 77/210 = 11/30.",
                    "Factor denominators: 8 = 2³; 455 = 5×7×13; 343 = 7³; 30 = 2×3×5.",
                    "Only 17/8 has purely 2ⁿ5ᵐ denominator."
                ]
            },
            {
                "question": "Watch out for simplification! Does 6 / 15 have a terminating or repeating decimal expansion?",
                "options": [
                    "Terminating (0.4), because simplifying 6/15 first gives 2/5 where q = 5¹",
                    "Non-terminating repeating, because 15 = 3 × 5 has a 3",
                    "Irrational number",
                    "Cannot be expressed as a decimal"
                ],
                "answer": 0,
                "hint": "ALWAYS cancel common numerator-denominator factors first before testing q!",
                "explanation": "6/15 is NOT in coprime form! Dividing top and bottom by 3 reduces 6/15 to 2/5, whose denominator 5 = 2⁰ × 5¹ yields terminating decimal 0.4.",
                "solution_steps": [
                    "Check HCF(6, 15) = 3 and simplify: 6/15 = 2/5.",
                    "Inspect simplified denominator q = 5 = 2⁰ × 5¹.",
                    "Verify pure 2ⁿ5ᵐ form gives terminating 0.4."
                ]
            },
            {
                "question": "How many decimal places will the terminating decimal expansion of 23 / (2³ × 5²) terminate after?",
                "options": [
                    "3 decimal places (0.115)",
                    "2 decimal places",
                    "5 decimal places",
                    "It repeats infinitely"
                ],
                "answer": 0,
                "hint": "Multiply top and bottom by 5¹ so 2³ × 5³ = 10³ = 1,000!",
                "explanation": "The higher exponent between 2³ and 5² is 3: (23 × 5)/(2³ × 5³) = 115/1000 = 0.115 (3 places).",
                "solution_steps": [
                    "Match powers of 2 and 5: max(3, 2) = 3.",
                    "Multiply numerator/denominator by 5¹: 115 / 1000.",
                    "Read 3 decimal places cleanly: 0.115."
                ]
            },
            {
                "question": "If a prime factor tree decomposes integer X into 2² × 3 × 5², what is X?",
                "options": [
                    "300",
                    "150",
                    "600",
                    "120"
                ],
                "answer": 0,
                "hint": "Compute 4 × 3 × 25 carefully!",
                "explanation": "2² × 3 × 5² = 4 × 3 × 25 = 12 × 25 = 300.",
                "solution_steps": [
                    "Evaluate prime powers: 2² = 4 and 5² = 25.",
                    "Group 4 × 25 = 100 cleanly.",
                    "Multiply 100 × 3 = 300."
                ]
            },
            {
                "question": "What is the HCF of the smallest prime number and the smallest composite number?",
                "options": [
                    "2",
                    "1",
                    "4",
                    "6"
                ],
                "answer": 0,
                "hint": "Smallest prime is 2, and smallest composite integer is 4!",
                "explanation": "Smallest prime = 2; smallest composite = 4 = 2². Their common prime smallest power is 2¹ = 2.",
                "solution_steps": [
                    "Identify smallest prime (1 is neither prime nor composite -> 2).",
                    "Identify smallest composite integer -> 4.",
                    "Compute HCF(2, 4) = 2."
                ]
            },
            {
                "question": "What is the LCM of two distinct prime numbers p and q?",
                "options": [
                    "p × q",
                    "1",
                    "p + q",
                    "p / q"
                ],
                "answer": 0,
                "hint": "Distinct primes share no common prime factor besides 1!",
                "explanation": "HCF(p, q) = 1 for distinct primes p, q, so LCM(p, q) = (p × q) / 1 = p × q.",
                "solution_steps": [
                    "Write prime powers: p¹ and q¹.",
                    "HCF (common prime factors) = 1.",
                    "LCM (all primes highest powers) = p × q."
                ]
            },
            {
                "question": "Using 10 = 2 × 5 reasoning, how many trailing zeroes will 2⁴ × 5³ × 7² end with?",
                "options": [
                    "3 trailing zeroes",
                    "4 trailing zeroes",
                    "2 trailing zeroes",
                    "7 trailing zeroes"
                ],
                "answer": 0,
                "hint": "Count how many complete pairs of (2 × 5) can be formed!",
                "explanation": "min(exponent of 2, exponent of 5) = min(4, 3) = 3 pairs of (2×5) = 10³ = 1000, giving 3 trailing zeroes (98,000).",
                "solution_steps": [
                    "Group powers of 10: 2⁴ × 5³ = 2 × (2×5)³ = 2 × 1000.",
                    "Remaining factors 2 × 49 = 98 do not end in 0.",
                    "Conclude 98 × 1000 = 98,000 has 3 trailing zeroes."
                ]
            },
            {
                "question": "For natural number n ≥ 1, which units digit(s) can 4ⁿ end with?",
                "options": [
                    "Only 4 (when n is odd) or 6 (when n is even), never 0",
                    "0 whenever n is a multiple of 5",
                    "Only 2 and 8",
                    "Any digit from 0 to 9"
                ],
                "answer": 0,
                "hint": "Compute 4¹ = 4, 4² = 16, 4³ = 64, 4⁴ = 256 and recall 4ⁿ = 2²ⁿ lacks factor 5!",
                "explanation": "4¹=4, 4²=16, 4³=64 cycle cleanly between 4 and 6; prime 5 never divides 2²ⁿ so 0 is impossible.",
                "solution_steps": [
                    "Check small powers: 4¹ = 4, 4² = 16, 4³ = 64.",
                    "Recognize alternating units cycle {4, 6}.",
                    "Confirm prime 5 never appears in 4ⁿ = 2²ⁿ."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Quiz 2",
        "subtitle": "Final Mastery: 3-Number HCF/LCM Formulas, Composite Traps, Euclid Proofs & Chapter Synthesis",
        "questions": [
            {
                "question": "Find HCF and LCM of the three numbers 6, 72, and 120 cleanly using primes (Example 8 & Note):",
                "options": [
                    "HCF = 6, LCM = 360",
                    "HCF = 12, LCM = 720",
                    "HCF = 6, LCM = 51,840",
                    "HCF = 3, LCM = 180"
                ],
                "answer": 0,
                "hint": "6 = 2×3, 72 = 2³×3², 120 = 2³×3×5!",
                "explanation": "Smallest common powers: 2¹×3¹ = 6 (HCF); Greatest powers across all primes: 2³×3²×5¹ = 8×9×5 = 360 (LCM).",
                "solution_steps": [
                    "Factor: 6 = 2¹·3¹, 72 = 2³·3², 120 = 2³·3¹·5¹.",
                    "HCF = smallest common prime powers = 2¹·3¹ = 6.",
                    "LCM = greatest powers across all primes = 2³·3²·5 = 360."
                ]
            },
            {
                "question": "Why does NCERT's 'Note to the Reader' warn that HCF(p, q, r) × LCM(p, q, r) ≠ p × q × r in general?",
                "options": [
                    "Because shared primes across all three numbers are over-counted/under-counted; e.g., 6 × 360 = 2,160 ≠ 6 × 72 × 120 = 51,840",
                    "Because three integers cannot have a common multiple",
                    "Because prime 5 disappears when multiplying three numbers",
                    "Because LCM is always smaller than HCF for three numbers"
                ],
                "answer": 0,
                "hint": "Test p = 6, q = 72, r = 120 directly!",
                "explanation": "For 3 numbers, intermediate pairwise common prime exponents are omitted by HCF(p,q,r)×LCM(p,q,r), so pairwise HCFs/LCMs are needed.",
                "solution_steps": [
                    "Compare HCF(6,72,120)×LCM(6,72,120) = 6 × 360 = 2,160.",
                    "Compute direct product 6 × 72 × 120 = 51,840.",
                    "Conclude 2,160 ≠ 51,840, disproving naive generalization."
                ]
            },
            {
                "question": "In the exact 3-number formula LCM(p, q, r) = [p·q·r · HCF(p, q, r)] / D, what equals denominator D?",
                "options": [
                    "HCF(p, q) · HCF(q, r) · HCF(p, r)",
                    "LCM(p, q) · LCM(q, r) · LCM(p, r)",
                    "p + q + r",
                    "HCF(p, q, r)²"
                ],
                "answer": 0,
                "hint": "Check the Note to the Reader in Section 1.4: divide by the product of all three pairwise HCFs!",
                "explanation": "LCM(p, q, r) divides p·q·r·HCF(p,q,r) by the product of pairwise HCFs: HCF(p,q)·HCF(q,r)·HCF(p,r).",
                "solution_steps": [
                    "Recall Section 1.4 Note formula for three positive integers.",
                    "Verify on 6, 72, 120: HCF(6,72)=6, HCF(72,120)=24, HCF(6,120)=6.",
                    "Compute (6×72×120 × 6) / (6×24×6) = 360 = LCM."
                ]
            },
            {
                "question": "Symmetrically, in the Note to the Reader's formula HCF(p, q, r) = [p·q·r · LCM(p, q, r)] / E, what is E?",
                "options": [
                    "LCM(p, q) · LCM(q, r) · LCM(p, r)",
                    "HCF(p, q) · HCF(q, r) · HCF(p, r)",
                    "(p · q · r)²",
                    "LCM(p, q, r)"
                ],
                "answer": 0,
                "hint": "Swap every HCF and LCM cleanly in the previous 3-number formula!",
                "explanation": "HCF(p,q,r) = [p·q·r·LCM(p,q,r)] / [LCM(p,q)·LCM(q,r)·LCM(p,r)], symmetric dual of the LCM formula.",
                "solution_steps": [
                    "Swap HCF ↔ LCM across the Section 1.4 Note identity.",
                    "Check on 6, 72, 120: LCM(6,72)=72, LCM(72,120)=360, LCM(6,120)=120.",
                    "(6×72×120 × 360) / (72×360×120) = 6 = HCF."
                ]
            },
            {
                "question": "If positive integers a and b are written in prime form as a = x³ y² and b = x y³ (where x, y are distinct primes), find HCF(a, b) and LCM(a, b):",
                "options": [
                    "HCF = x y² and LCM = x³ y³",
                    "HCF = x³ y³ and LCM = x y²",
                    "HCF = x y and LCM = x⁴ y⁵",
                    "HCF = x² y² and LCM = x³ y²"
                ],
                "answer": 0,
                "hint": "HCF chooses minimum exponent of each prime; LCM chooses maximum exponent!",
                "explanation": "min(3,1)=1 for x and min(2,3)=2 for y -> HCF = xy². max(3,1)=3 and max(2,3)=3 -> LCM = x³y³.",
                "solution_steps": [
                    "Compare prime exponents of x: min(3,1)=1, max(3,1)=3.",
                    "Compare prime exponents of y: min(2,3)=2, max(2,3)=3.",
                    "Conclude HCF = xy², LCM = x³y³ (notice HCF × LCM = x⁴y⁵ = a × b!)."
                ]
            },
            {
                "question": "Notice a subtle trap in Theorem 1.2: 4 divides 6² (4 | 36), yet 4 does NOT divide 6. Why does this NOT break Theorem 1.2?",
                "options": [
                    "Because 4 is COMPOSITE (4 = 2²), whereas Theorem 1.2 holds strictly for PRIME divisors p",
                    "Because 36 is not a square number",
                    "Because 6 is irrational",
                    "Because Euclid's algorithm forbids number 4"
                ],
                "answer": 0,
                "hint": "Can prime 2 split into 2 × 2, taking one 2 from the first 6 and the second 2 from the other 6?",
                "explanation": "Composite 4 = 2×2 grabs one factor 2 from each copy of 6 in 6 × 6 = 36 without dividing 6 individually.",
                "solution_steps": [
                    "Observe 6 = 2 × 3, so 6² = (2 × 3) × (2 × 3) = 4 × 9.",
                    "Note composite 4 splits across both factors of 6.",
                    "Confirm Theorem 1.2 explicitly requires prime p."
                ]
            },
            {
                "question": "If the HCF of 65 and 117 is expressible in the linear form 65m − 117, find the value of integer m:",
                "options": [
                    "m = 2",
                    "m = 1",
                    "m = 4",
                    "m = 3"
                ],
                "answer": 0,
                "hint": "First find HCF(65, 117) cleanly (note 65 = 5×13, 117 = 9×13), then solve 65m − 117 = 13!",
                "explanation": "HCF(65, 117) = 13. Solving 65m − 117 = 13 gives 65m = 130 ⟹ m = 2.",
                "solution_steps": [
                    "Factor 65 = 5 × 13 and 117 = 3² × 13 -> HCF = 13.",
                    "Set up equation: 65m − 117 = 13.",
                    "Solve 65m = 130 -> m = 2."
                ]
            },
            {
                "question": "Why can two positive numbers NEVER have HCF = 18 and LCM = 380?",
                "options": [
                    "Because HCF must ALWAYS divide LCM evenly, whereas 380 ÷ 18 leaves non-zero remainder 2",
                    "Because 380 is an even number",
                    "Because LCM must always be smaller than HCF",
                    "Because 18 contains prime factor 5"
                ],
                "answer": 0,
                "hint": "Divide 380 by 18 and recall that every factor in HCF is also inside both numbers and thus inside LCM!",
                "explanation": "Since HCF divides a and a divides LCM, HCF must divide LCM with zero remainder; 380 = 18×21 + 2 (remainder 2 ≠ 0) is impossible.",
                "solution_steps": [
                    "Recall divisibility chain: HCF(a, b) | a | LCM(a, b).",
                    "Test whether 18 divides 380 cleanly: 380 = 18 × 21 + 2.",
                    "Non-zero remainder proves no integer pair has HCF 18 and LCM 380."
                ]
            },
            {
                "question": "Which number below is GUARANTEED irrational?",
                "options": [
                    "√2 + √3 (and any √p + √q for distinct primes, or 5 − √3)",
                    "√4 × √9 (= 6)",
                    "(3 − √5)(3 + √5) (= 4)",
                    "22 / 7"
                ],
                "answer": 0,
                "hint": "Evaluate algebraic simplifications first! Watch out for conjugates and 22/7 (which is rational p/q)!",
                "explanation": "√4×√9 = 2×3 = 6, (3−√5)(3+√5) = 9−5 = 4, and 22/7 are all rational; only √2 + √3 stays irrational.",
                "solution_steps": [
                    "Check √4×√9 = 2×3 = 6 (rational).",
                    "Check difference of squares (3−√5)(3+√5) = 9 − 5 = 4 (rational) and 22/7 (p/q rational).",
                    "Confirm √2 + √3 cannot be written as p/q (squaring leaves 2√6 irrational)."
                ]
            },
            {
                "question": "What is the largest positive integer that divides 70 and 125 leaving remainders 5 and 8 respectively?",
                "options": [
                    "13",
                    "15",
                    "9",
                    "65"
                ],
                "answer": 0,
                "hint": "Subtract the remainders first (70 − 5 = 65 and 125 − 8 = 117), then take their HCF!",
                "explanation": "Exact multiples of the divisor are 70−5 = 65 and 125−8 = 117; HCF(65, 117) = 13 (check: 70 = 13×5 + 5, 125 = 13×9 + 8).",
                "solution_steps": [
                    "Subtract remainders to get exact multiples: 70 − 5 = 65 and 125 − 8 = 117.",
                    "Factor: 65 = 5 × 13 and 117 = 3² × 13.",
                    "Largest divisor is HCF(65, 117) = 13 (> 8 so remainders valid!)."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch1 Class 10 Maths Part 3.")
    for s in slides_part3:
        twc = len(s["title"].split())
        q_count = len(s["questions"])
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Questions: {q_count}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert q_count == 10, f"Slide {s['id']} has {q_count} questions, expected 10"
        for qidx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4
            assert 0 <= q["answer"] <= 3
            assert len(q["solution_steps"]) == 3
            assert len(q["hint"]) > 5
            assert len(q["explanation"]) > 10
    print("All 40 exercise & challenge questions verified successfully!")

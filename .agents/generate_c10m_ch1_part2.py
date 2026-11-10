#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 1: Real Numbers
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (Raghav, Sonia, Ravi, Khushi, etc.), zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Circular Track Meeting",
        "subtitle": "Solving Real-World Circular Path Meeting Problems Using Prime LCM",
        "speech": (
            "Now watch prime L C M shine cleanly on an exciting athletic circular running track from Exercise One Point One! Imagine a circular sports field path where two "
            "runners—Runner A and Runner B—start running simultaneously from the exact same chalk starting line and head in the exact same circular direction! Runner A completes "
            "one full lap smoothly in 18 minutes, while slightly faster Runner B finishes one complete lap in 12 minutes! After how many minutes will both runners reunite side by "
            "side right back at that starting line? Notice immediately why H C F would fail here: their reunion time cannot be shorter than 12 or 18 minutes, because both runners must "
            "complete exact whole numbers of full laps simultaneously! Therefore, reunion time must be a common MULTIPLE of both 18 and 12—specifically the SMALLEST common multiple, "
            "or L C M of 18 and 12! Let us compute swiftly with primes: 18 factors into 2 times 3 squared, while 12 factors into 2 squared times 3! Taking greatest powers across all primes "
            "gives 2 squared times 3 squared, equaling 4 times 9, or 36 minutes! At 36 minutes, Runner A finishes 2 full laps while Runner B completes 3 full laps—crossing the starting line together!"
        ),
        "checkpoints": [
            {
                "question": "If Runner A takes 18 minutes and Runner B takes 12 minutes per circular track lap starting together in the same direction, when do they reunite at the starting point?",
                "options": [
                    "After 36 minutes (LCM of 18 and 12)",
                    "After 6 minutes (HCF of 18 and 12)",
                    "After 30 minutes (sum of 18 and 12)",
                    "After 216 minutes only"
                ],
                "answer": 0,
                "hint": "Find the least common multiple (LCM) of 18 = 2 × 3² and 12 = 2² × 3!",
                "explanation": "Reuniting at the starting point requires complete whole laps for both runners, which happens first at LCM(18, 12) = 2² × 3² = 36 minutes."
            },
            {
                "question": "At the first reunion time of 36 minutes, how many full laps has each runner completed?",
                "options": [
                    "Runner A completes 2 laps and Runner B completes 3 laps",
                    "Both runners complete 6 laps each",
                    "Runner A completes 3 laps and Runner B completes 2 laps",
                    "Runner A completes 1 lap and Runner B completes 4 laps"
                ],
                "answer": 0,
                "hint": "Divide total time (36 minutes) by each runner's single-lap time (18 and 12)!",
                "explanation": "36 ÷ 18 = 2 laps for Runner A, and 36 ÷ 12 = 3 laps for Runner B, bringing both back to the start together."
            }
        ]
    },
    {
        "id": 10,
        "title": "Theorem One Two",
        "subtitle": "Prime Divisibility Lemma: If a Prime Number p Divides a², Then p Divides a",
        "speech": (
            "Now step boldly into Section One Point Three: Revisiting Irrational Numbers! Before dismantling square root of 2 cleanly with contradiction, mathematicians craft "
            "one razor-sharp helper tool called Theorem One Point Two! Read every word slowly: Let p be a prime number. If p divides a squared, then p MUST divide a, where a is a positive integer! "
            "Wait—does that hold for composite numbers too? Careful trap check! Suppose 4 divides 6 squared (4 divides 36 cleanly!), yet 4 does NOT divide 6! So primality of p is truly essential! "
            "How does the Fundamental Theorem of Arithmetic prove Theorem One Point Two effortlessly? Write out the unique prime factorization of integer a as p1 times p2 up to pn, where some primes "
            "may repeat. Now square both sides cleanly: a squared equals p1 squared times p2 squared up to pn squared! Look carefully at the primes sitting inside a squared—there are NO brand-new "
            "primes created by squaring! Only the exact original primes p1 through pn appear doubled! Since prime p divides a squared cleanly, by uniqueness in Theorem One Point One, p MUST "
            "be one of the prime factors of a squared—meaning p belongs strictly among p1 through pn, proving p divides a! That single golden lemma unlocks every root proof ahead!"
        ),
        "checkpoints": [
            {
                "question": "Why does Theorem 1.2 require that p specifically be a PRIME number when concluding 'if p divides a², then p divides a'?",
                "options": [
                    "Because composite divisors can split factors across a×a (e.g., 4 divides 6² = 36, yet 4 does not divide 6)",
                    "Because composite numbers never divide square integers",
                    "Because prime numbers are always even integers",
                    "Because squaring removes all prime factors from integers"
                ],
                "answer": 0,
                "hint": "Test p = 4 and a = 6: 4 divides 36, yet does 4 divide 6?",
                "explanation": "A composite number's prime factors can come partly from one copy of a and partly from the other copy, whereas an indivisible prime p must divide at least one (hence every) copy of a."
            },
            {
                "question": "If integer a has prime factorization a = p₁ × p₂ × ... × pₙ, which theorem proves prime factor p of a² must appear among p₁, p₂, ..., pₙ?",
                "options": [
                    "Uniqueness part of Theorem 1.1 (Fundamental Theorem of Arithmetic)",
                    "Pythagorean circular track theorem",
                    "Adding remainder r > b in Euclid's lemma",
                    "Only decimal expansion rounding"
                ],
                "answer": 0,
                "hint": "Squaring doubles exponents of existing primes; uniqueness forbids new primes from appearing!",
                "explanation": "By uniqueness in the Fundamental Theorem of Arithmetic, the prime factors of a² = p₁²p₂²...pₙ² are precisely p₁, ..., pₙ, so any prime dividing a² must divide a."
            }
        ]
    },
    {
        "id": 11,
        "title": "Proving Root Two",
        "subtitle": "Theorem 1.3: Step-by-Step Proof by Contradiction That √2 Is Irrational",
        "speech": (
            "Witness one of human civilization's finest jewels of pure logic—Theorem One Point Three: proving strictly by contradiction that square root of 2 is IRRATIONAL! "
            "Rather than searching infinitely many decimal digits forever, how can twenty short lines of algebra prove something impossible for eternity? Watch closely! Step One: Assume "
            "the exact opposite—suppose square root of 2 IS rational! Then we can write square root of 2 equal to r over s, cancel out common factors cleanly, and arrive at square root of 2 "
            "equals a over b, where integers a and b are COPRIME (sharing NO common factor other than 1, and b not zero)! Step Two: Multiply by b and square both sides cleanly to banish "
            "the radical sign: 2 times b squared equals a squared! Look straight at that equation: 2 divides a squared! Now apply Theorem One Point Two immediately: since 2 is prime, "
            "2 MUST divide a! Step Three: Write a equals 2 times c for some integer c, substitute back inside 2 b squared equals 4 c squared, and cancel 2 cleanly to obtain b squared equals 2 c squared! "
            "Apply Theorem One Point Two again: 2 divides b! Contradiction! Both a and b share common factor 2, shattering our coprime assumption—proving square root of 2 CANNOT be rational!"
        ),
        "checkpoints": [
            {
                "question": "What crucial assumption made at the start of the contradiction proof of Theorem 1.3 (√2 is irrational) gets violated at the end?",
                "options": [
                    "Assuming a and b are coprime (sharing no common factor > 1), whereas algebra forces 2 to divide both a and b",
                    "Assuming 2 is a composite number greater than 5",
                    "Assuming denominator b equals zero from the start",
                    "Assuming √2 equals an odd integer"
                ],
                "answer": 0,
                "hint": "After writing √2 = a/b in lowest coprime form, both a and b turn out divisible by 2!",
                "explanation": "Showing 2 divides both a and b directly contradicts the initial assumption that a/b was reduced to coprime integers."
            },
            {
                "question": "In proving √2 irrational, once we substitute a = 2c into 2b² = a², what simplified relation proves 2 divides b?",
                "options": [
                    "b² = 2c², showing 2 divides b² and hence prime 2 divides b by Theorem 1.2",
                    "b² = 4c², showing 4 divides c only",
                    "b = 2a, showing a divides 1",
                    "2b = c², showing b is odd"
                ],
                "answer": 0,
                "hint": "2b² = (2c)² = 4c² simplifies upon dividing both sides by 2!",
                "explanation": "Dividing 2b² = 4c² by 2 yields b² = 2c², proving 2 | b² and thus 2 | b by Theorem 1.2."
            }
        ]
    },
    {
        "id": 12,
        "title": "Roots Three Five",
        "subtitle": "Extending Prime Contradiction Cleanly to √3, √5, and General Prime Roots √p",
        "speech": (
            "Now marvel at how effortlessly the exact blueprint of Theorem One Point Three generalizes from square root of 2 to square root of 3, square root of 5, and in fact square root of ANY "
            "prime integer p! Test the blueprint live on square root of 3 and square root of 5! Step One: Assume for contradiction that square root of 3 equals a over b where integers a and b are "
            "strictly coprime and b is nonzero! Square both sides cleanly to get 3 b squared equals a squared! Because prime 3 divides a squared, Theorem One Point Two guarantees prime 3 divides a! "
            "Substitute a equal to 3 times c directly inside 3 b squared equals (3 c) squared, yielding 3 b squared equals 9 c squared! Divide both sides cleanly by 3: b squared equals 3 c squared! "
            "Immediately Theorem One Point Two ensures prime 3 divides b too—yielding a blazing contradiction because coprime a and b cannot share common factor 3! Now replace number 3 with prime 5 for Exercise "
            "One Point Two Question One: 5 b squared equals a squared gives a equals 5 c, yielding b squared equals 5 c squared—forcing common factor 5! In general, for EVERY prime p, square root of p is irrational!"
        ),
        "checkpoints": [
            {
                "question": "When adapting Theorem 1.3 to prove √5 is irrational via √5 = a/b (coprime), what substitution follows showing 5 divides a?",
                "options": [
                    "Set a = 5c, then 5b² = 25c² simplifies to b² = 5c², forcing prime 5 to divide b as well",
                    "Set a = 2c, then 5b² = 4c² shows 2 divides 5",
                    "Set b = 5c immediately before squaring",
                    "Set a = 25c, giving b = 5c²"
                ],
                "answer": 0,
                "hint": "Replace 2 with 5 across the substitution a = pc!",
                "explanation": "Since 5 | a², Theorem 1.2 yields 5 | a so a = 5c; substituting into 5b² = a² gives b² = 5c², proving 5 | b and contradicting coprimality."
            },
            {
                "question": "Does the √p contradiction argument prove √9 is irrational? Why or why not?",
                "options": [
                    "No! 9 is NOT prime (9 = 3²), so √9 = 3 is rational; Theorem 1.2 fails when p is composite like 9",
                    "Yes, √9 is irrational because 9 is odd",
                    "No, because 9 ends in digit 9 instead of 0",
                    "Yes, all square roots of odd integers are irrational"
                ],
                "answer": 0,
                "hint": "What does √9 actually equal? Check whether 9 satisfies 'p is prime'!",
                "explanation": "9 = 3² is composite, so √9 = 3 = 3/1 is completely rational! Theorem 1.2 strictly requires prime p, and irrationality √p holds for prime p (or non-square integers)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Combined Irrational Proofs",
        "subtitle": "Proving 5 − √3 and 3√2 Irrational Quickly via Rational Closure Algebra",
        "speech": (
            "Suppose a textbook example challenges you to prove that 5 minus square root of 3, or 3 times square root of 2, is irrational! Do you need to repeat squaring with coprime "
            "denominators all over again? Not at all—once you already know square root of 3 or square root of 2 is irrational, elementary arithmetic solves these in FOUR brisk lines! "
            "Watch carefully on Example Ten: Prove 5 minus square root of 3 is irrational! First assume the opposite: suppose 5 minus square root of 3 equals rational fraction a over b! "
            "Next isolate square root of 3 completely alone on one side: subtract a over b from 5, writing 5 minus a over b equals square root of 3, or (5b minus a) over b equals square root of 3! "
            "Since a and b are integers with nonzero denominator b, (5b minus a) over b is strictly RATIONAL! Yet the right side equals square root of 3, already proven IRRATIONAL! Contradiction! Similarly, setting 3 times square root of 2 equal to rational a over b gives square root of 2 equal to a over (3b)—proving both combined numbers strictly irrational every single time with zero tedious squaring!"
        ),
        "checkpoints": [
            {
                "question": "To prove 5 − √3 is irrational using proof by contradiction (given √3 is irrational), what is the key algebraic move after setting 5 − √3 = a/b?",
                "options": [
                    "Isolate √3 alone: √3 = 5 − a/b = (5b − a)/b, equating irrational √3 with a rational fraction of integers",
                    "Square both sides infinitely many times without isolating √3",
                    "Multiply both sides by zero",
                    "Assume √3 = 3 from the beginning"
                ],
                "answer": 0,
                "hint": "Keep the irrational radical isolated cleanly on one side and rational integers on the other!",
                "explanation": "Isolating √3 = (5b − a)/b creates an immediate contradiction between the irrationality of √3 and the closure of rationals under subtraction."
            },
            {
                "question": "If we assume 3√2 = a/b (a, b integers, b ≠ 0), how do we obtain a contradiction in one division step?",
                "options": [
                    "Divide by 3 to write √2 = a/(3b), asserting irrational √2 equals a rational ratio of integers",
                    "Write 3 = a/b + √2 without dividing",
                    "Set b = 0 so the denominator vanishes",
                    "Add 3 to both sides giving 3 + 3√2 = 6"
                ],
                "answer": 0,
                "hint": "Move coefficient 3 into the denominator of a/b!",
                "explanation": "Since a and 3b (≠ 0) are integers, a/(3b) is rational, contradicting the proven irrationality of √2."
            }
        ]
    },
    {
        "id": 14,
        "title": "Mixed Exercise Proofs",
        "subtitle": "Walking Through Exercise 1.2 Proofs: 3+2√5, 1/√2, 7√5, and 6+√2",
        "speech": (
            "Let us examine all four famous problems in Exercise One Point Two so you recognize the exact isolation template for EVERY combination! Look closely at Question Two: Prove 3 plus 2 square root of 5 "
            "is irrational! Assume 3 plus 2 square root of 5 equals rational a over b! First subtract 3 across: 2 square root of 5 equals (a minus 3b) over b! Next divide cleanly by 2: square root of 5 equals "
            "(a minus 3b) over (2b)! Since a, b, 3, and 2 are integers with 2b nonzero, the right fraction is purely rational—contradicting the known irrationality of square root of 5! Now inspect Question Three Part One: "
            "1 divided by square root of 2! Assume 1 over square root of 2 equals rational a over b (a not zero). Simply flip reciprocals cleanly on both sides—obtaining square root of 2 equals b over a! Instant "
            "contradiction because b over a is rational while square root of 2 is irrational! Part Two checks 7 square root of 5 cleanly via dividing by 7 into a over (7b), while Part Three isolates 6 plus square root of 2 "
            "into square root of 2 equals (a minus 6b) over b! Four distinct-looking Exercise One Point Two problems, one unified algebraic isolation crystal!"
        ),
        "checkpoints": [
            {
                "question": "In proving 1/√2 is irrational by setting 1/√2 = a/b (coprime integers, a ≠ 0, b ≠ 0), what cleanest one-step move contradicts Theorem 1.3?",
                "options": [
                    "Take reciprocals on both sides to write √2 = b/a, forcing irrational √2 to equal rational fraction b/a",
                    "Multiply by √3 on both sides",
                    "Conclude a = 0 immediately",
                    "Add 1/2 to both sides"
                ],
                "answer": 0,
                "hint": "Flip numerator and denominator on both sides!",
                "explanation": "Taking reciprocals (or rationalizing √2/2 = a/b -> √2 = 2a/b) expresses irrational √2 as a quotient of integers, contradicting Theorem 1.3."
            },
            {
                "question": "After assuming 3 + 2√5 = a/b (integers a, b ≠ 0), which rational expression correctly isolates √5 on the right?",
                "options": [
                    "√5 = (a − 3b) / (2b)",
                    "√5 = (a + 3b) / 2",
                    "√5 = (2a − 3) / b",
                    "√5 = (3b − 2a) / b"
                ],
                "answer": 0,
                "hint": "First subtract 3 = 3b/b from a/b, then divide everything by 2!",
                "explanation": "3 + 2√5 = a/b ⟹ 2√5 = (a − 3b)/b ⟹ √5 = (a − 3b)/(2b), contradicting that √5 is irrational."
            }
        ]
    },
    {
        "id": 15,
        "title": "Three Number Formulas",
        "subtitle": "Note to the Reader: Why HCF×LCM ≠ p·q·r and True 3-Integer Formulas",
        "speech": (
            "Now unlock the fascinating 'Note to the Reader' inside Section One Point Four—a subtle rule catching hasty students off guard! For two positive integers a and b, "
            "H C F times L C M always equals a times b! Wait: does that neat shortcut hold when THREE integers p, q, and r step in? Test 6, 72, and 120 right now! "
            "Factor all three carefully: 6 equals 2 times 3; 72 equals 2 cubed times 3 squared; 120 equals 2 cubed times 3 times 5! Compute H C F (smallest common powers) equaling 2 times 3 equals 6, and L C M "
            "(greatest powers across all primes) equaling 2 cubed times 3 squared times 5 equals 360! Multiply H C F times L C M: 6 times 360 equals 2,160! Meanwhile multiply p times q times r: 6 times 72 times 120 equals 51,840! "
            "NOT EQUAL! Pairwise prime overlaps fail to cancel cleanly! Instead, NCERT provides exact three-integer formulas: L C M(p, q, r) equals (p times q times r times H C F(p, q, r)) divided by the product of all three "
            "pairwise H C Fs! Swapping H C F and L C M computes three-number H C F!"
        ),
        "checkpoints": [
            {
                "question": "For three integers p = 6, q = 72, r = 120, what does comparing HCF(p, q, r) × LCM(p, q, r) against p × q × r reveal?",
                "options": [
                    "They are NOT equal (6 × 360 = 2,160 ≠ 51,840); the two-number product identity does NOT generalize directly to 3 integers",
                    "They are always identical for every triple of numbers",
                    "Their difference always equals 10",
                    "Three integers never possess an LCM"
                ],
                "answer": 0,
                "hint": "Check the Note to the Reader in Section 1.4 carefully!",
                "explanation": "HCF(6, 72, 120) × LCM(6, 72, 120) = 6 × 360 = 2,160, whereas 6 × 72 × 120 = 51,840, proving the 2-number rule does not apply directly to 3 numbers."
            },
            {
                "question": "In the Note to the Reader's exact formula for 3 positive integers, LCM(p, q, r) equals [p·q·r·HCF(p, q, r)] divided by what product?",
                "options": [
                    "HCF(p, q) · HCF(q, r) · HCF(p, r) — the product of all three pairwise HCFs",
                    "p + q + r",
                    "LCM(p, q) + LCM(r, p)",
                    "HCF(p, q, r) cubed"
                ],
                "answer": 0,
                "hint": "Think of inclusion-exclusion with prime exponents across pairs (p,q), (q,r), and (p,r)!",
                "explanation": "Dividing p·q·r·HCF(p,q,r) by the three pairwise HCFs [HCF(p,q)·HCF(q,r)·HCF(p,r)] properly restores the maximum prime exponents for LCM(p,q,r)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter One Summary",
        "subtitle": "Synthesizing Real Numbers: Divisibility, Uniqueness, Irrationality & Multi-Number Rules",
        "speech": (
            "Congratulations, bright mathematicians, on mastering every big concept inside NCERT Class Ten Chapter One: Real Numbers! Let us snap all four monumental pillars firmly together into one clear mental map! "
            "First, Euclid's division algorithm computes H C F smoothly via positive remainders a equals b q plus r until zero remainder arrives, while simplified fraction denominator primes 2 and 5 decide instantly "
            "whether rational p over q gives a terminating or repeating decimal! Second, Theorem One Point One—the Fundamental Theorem of Arithmetic proved by Carl Friedrich Gauss—guarantees unique prime factorization "
            "for every composite integer, allowing instant factor trees, proving why 4 to power n and 6 to power n never end with digit zero, proving composite expressions swiftly, solving circular track L C M meetings, "
            "and confirming H C F times L C M equals a times b for any TWO integers! Third, prime divisibility Theorem One Point Two anchors contradiction proofs showing square root of p—for primes like 2, 3, 5—and algebraic "
            "combinations like 5 minus root 3 or 3 root 2 are strictly irrational! Fourth, always remember the Note to the Reader: three-integer H C F and L C M require pairwise formulas! Ready for Exercises and Challenges!"
        ),
        "checkpoints": [
            {
                "question": "Which single summary statement accurately connects the Fundamental Theorem of Arithmetic to decimal expansions and irrational proofs?",
                "options": [
                    "Unique prime factorization underpins Theorem 1.2 (p | a² ⟹ p | a) for irrationality proofs and checks denominator q = 2ⁿ5ᵐ for terminating decimals",
                    "It states only even numbers possess prime factor trees",
                    "It proves HCF(p, q, r) × LCM(p, q, r) = p × q × r for all triples",
                    "It claims 4ⁿ always ends with zero when n ≥ 5"
                ],
                "answer": 0,
                "hint": "Combine Sections 1.1, 1.2, 1.3, and 1.4 accurately!",
                "explanation": "Theorem 1.1 governs unique prime factorization, powering divisibility Lemma 1.2, contradiction proofs of √p, HCF/LCM, and decimal tests."
            },
            {
                "question": "Suppose an integer N = p·q with distinct primes p and q. Which statement MUST be false?",
                "options": [
                    "N has another prime factor besides p and q in some special factor tree",
                    "√p is an irrational number",
                    "HCF(N, p) equals p and LCM(N, p) equals N",
                    "If p and q are 2 and 5, 1/N terminates as 0.1"
                ],
                "answer": 0,
                "hint": "Can a composite integer EVER produce a brand-new prime factor by using a different factor tree?",
                "explanation": "By uniqueness in Theorem 1.1, no alternate factor tree can ever uncover prime factors outside {p, q}."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch1 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

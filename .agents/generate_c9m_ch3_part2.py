#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 3: The World of Numbers
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 3.5.3 to 3.7, Exercises & Chapter Summary with 1-3 word headings, 195-215 words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Pi and Madhava",
        "subtitle": "Section 3.5.3 Story of π: Lambert's 1761 Irrationality Proof, Āryabhaṭa's 3927/1250 = 3.1416 & Mādhava's Infinite Series",
        "speech": (
            "Now meet the most celebrated irrational constant in all of mathematics and science: PI, defined as the constant ratio of every circle's circumference to its exact diameter! "
            "Open Section Three Point Five Point Three! Because no whole-number ruler division ever seemed to capture Pi cleanly, ancient mathematicians across civilizations chased sharper rational approximations for millennia! "
            "In four hundred ninety-nine CE, Indian astronomer-mathematician Āryabhaṭa inscribed regular polygons inside a circle of diameter twenty thousand in his Āryabhaṭīya, famously deriving perimeter sixty-two thousand eight hundred thirty-two! Dividing yields Āryabhaṭa's crisp rational approximation three thousand nine hundred twenty-seven divided by one thousand two hundred fifty, equal to three point one four one six—remarkably accurate to four decimal places! "
            "Yet around the fourteenth century in Kerala, visionary mathematician Mādhava of Saṅgamagrāma discovered something far deeper: instead of a static fraction approximation, Pi equals an EXACT INFINITE ALTERNATING SERIES! "
            "Mādhava proved that Pi equals four times the infinite alternating sum: one minus one-third plus one-fifth minus one-seventh plus one-ninth, continuing forever! "
            "Finally in seventeen hundred sixty-one, Swiss mathematician Johann Heinrich Lambert rigorously proved using continued fractions that Pi itself is genuinely IRRATIONAL—completely impossible to express as any finite integer fraction!"
        ),
        "checkpoints": [
            {
                "question": "Which famous rational approximation for π did Āryabhaṭa report in 499 CE, and to how many decimal places is it accurate?",
                "options": [
                    "3927/1250 = 3.1416 (accurate to 4 decimal places)",
                    "22/7 = 3.142857... (exact value of π)",
                    "3.0000 exactly",
                    "10/3 = 3.3333..."
                ],
                "answer": 0,
                "hint": "Remember circumference 62,832 divided by diameter 20,000!",
                "explanation": "62,832 / 20,000 reduces by 16 to 3927/1250 = 3.1416, matching π ≈ 3.14159... cleanly to 4 decimals."
            },
            {
                "question": "Which 14th-century Kerala School mathematician discovered the exact infinite alternating series π = 4 × (1 − 1/3 + 1/5 − 1/7 + ...)?",
                "options": [
                    "Mādhava of Saṅgamagrāma",
                    "Hippasus",
                    "Johann Lambert",
                    "Baudhāyana"
                ],
                "answer": 0,
                "hint": "Recall the founder of the Kerala School of Astronomy and Mathematics!",
                "explanation": "Mādhava of Saṅgamagrāma (14th century) derived the alternating odd-reciprocal series for π (later rediscovered in Europe by Gregory and Leibniz)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Terminating Rational Decimals",
        "subtitle": "Sections 3.6 & 3.6.1 (Part A): Real Line ℝ & Prime-Factor Rule (q = 2ᵐ5ⁿ) for Terminating Rational Decimals",
        "speech": (
            "Now bridge fractions and irrationals seamlessly onto one unbroken geometric canvas in Section Three Point Six: REAL NUMBERS, DECIMALS AND CYCLIC PATTERNS! "
            "When we unite ALL rational fractions Q together with ALL irrational numbers like root two and Pi, every microscopic pinhole vanishes—forming the continuous REAL NUMBER LINE denoted capital R! Every single point on that line matches one real number, and every real number matches one unique point! "
            "Now inspect rational decimals cleanly in Section Three Point Six Point One! Divide any fraction p divided by q: why does three-eighths stop cleanly at zero point three seven five, while one-third loops endlessly as zero point three three three forever? "
            "Uncover the Prime Factor Secret! First reduce fraction p over q completely to co-prime lowest terms! A reduced rational fraction produces a TERMINATING DECIMAL if and only if the prime factorization of its denominator q contains STRICTLY twos and or fives—never threes, never sevens, never any other primes! "
            "Why does this work? Because only powers of two and five combine cleanly to build powers of ten like one hundred or one thousand! Any extra prime factor like three or seven lingering inside denominator q forces endless division!"
        ),
        "checkpoints": [
            {
                "question": "Without performing long division, which reduced rational fraction has a TERMINATING decimal expansion?",
                "options": [
                    "13/40 (denominator 40 = 2³ × 5¹ has strictly prime factors 2 and 5)",
                    "7/30 (denominator 30 = 2 × 3 × 5 includes prime factor 3)",
                    "5/21 (denominator 21 = 3 × 7)",
                    "11/14 (denominator 14 = 2 × 7)"
                ],
                "answer": 0,
                "hint": "Factor each denominator into primes after checking HCF(p, q) = 1!",
                "explanation": "40 = 2³ × 5 contains ONLY prime factors 2 and 5, giving 13/40 = (13 × 25)/1000 = 0.325 (terminating)."
            },
            {
                "question": "What does the Real Number Set ℝ represent geometrically?",
                "options": [
                    "The continuous union of all rational numbers ℚ and all irrational numbers, filling every point on the number line",
                    "Only positive terminating decimals",
                    "Only integer points excluding fractions",
                    "Only prime numbers and zero"
                ],
                "answer": 0,
                "hint": "Combining fractions with irrationals eliminates every gap on the line!",
                "explanation": "ℝ = ℚ ∪ Irrationals establishes a complete one-to-one correspondence with every point on the continuous number line."
            }
        ]
    },
    {
        "id": 11,
        "title": "Repeating Decimal Fractions",
        "subtitle": "Section 3.6.1 (Part B): Algebraic 10ᵏ Shift Algorithm Converting Pure (0.6̄) & Mixed (0.16̄, 2.357̄) Decimals into p/q Form",
        "speech": (
            "Can every non-terminating decimal with a repeating loop STILL be converted back into an exact integer fraction p over q? YES! Every repeating decimal is one hundred percent RATIONAL! "
            "Master BOTH pure and mixed repeating conversions in Section Three Point Six Point One using the crisp ten-to-the-k shift trick! "
            "Case One: PURE repeating decimal, such as x equals zero point six-bar (zero point six six six forever)! Since ONE digit repeats right after the decimal point, multiply both sides by ten: ten x equals six point six six six forever! "
            "Now subtract original x cleanly from ten x: the infinite decimal tail vanishes completely! Nine x equals six, giving x equals six-ninths, reducing neatly to TWO-THIRDS! "
            "Case Two: MIXED repeating decimals having non-repeating digits first, such as zero point one six-bar or two point three five seven-bar! "
            "Follow a clean two-step shift! For x equals two point three five seven-bar: multiply by one hundred to pull the two non-repeating digits left, giving one hundred x equals two hundred thirty-five point seven-bar! Next multiply by one thousand so one repeating digit shifts past: one thousand x equals two thousand three hundred fifty-seven point seven-bar! Subtracting cancels the bar tail: nine hundred x equals two thousand one hundred twenty-two!"
        ),
        "checkpoints": [
            {
                "question": "Convert the pure repeating decimal x = 0.6̄ (0.666...) into reduced p/q fraction form.",
                "options": [
                    "2/3",
                    "6/10 = 3/5",
                    "5/9",
                    "3/4"
                ],
                "answer": 0,
                "hint": "Set 10x = 6.666... and subtract x = 0.666...!",
                "explanation": "10x - x = 6 ⇒ 9x = 6 ⇒ x = 6/9 = 2/3."
            },
            {
                "question": "Convert the mixed repeating decimal x = 0.16̄ (0.1666...) into reduced p/q fraction form.",
                "options": [
                    "1/6",
                    "16/99",
                    "4/25",
                    "2/15"
                ],
                "answer": 0,
                "hint": "Compute 100x - 10x = 16.6̄ - 1.6̄ = 15, so 90x = 15!",
                "explanation": "10x = 1.666... and 100x = 16.666...; subtracting yields 90x = 15 ⇒ x = 15/90 = 1/6."
            }
        ]
    },
    {
        "id": 12,
        "title": "Magic Cyclic Numbers",
        "subtitle": "Section 3.6.2 Magic of Cyclic Numbers: Repeating Block 1/7 = 0.142857̄ & Cyclic Digit Rotations Under Multiplication (1 to 6)",
        "speech": (
            "Now marvel at one of arithmetic's most astonishing jewels in Section Three Point Six Point Two: THE MAGIC OF CYCLIC NUMBERS! "
            "Take the humble unit fraction ONE-SEVENTH! Perform step-by-step long division carefully: dividing one by seven reveals a crisp six-digit repeating loop—zero point ONE-FOUR-TWO-EIGHT-FIVE-SEVEN bar! "
            "Notice immediately why exactly six digits repeat: when dividing by prime number seven, only six non-zero remainders—one, three, two, six, four, five—can ever appear before the remainder sequence MUST loop right back to the start! "
            "Now watch pure mathematical magic happen when you multiply that exact six-digit integer block ONE-FOUR-TWO-EIGHT-FIVE-SEVEN by two, three, four, five, and six! "
            "Multiply by two: two hundred eighty-five thousand seven hundred fourteen! "
            "Multiply by three: four hundred twenty-eight thousand five hundred seventy-one! "
            "Multiply by four: five hundred seventy-one thousand four hundred twenty-eight! "
            "Multiply by five: seven hundred fourteen thousand two hundred eighty-five! "
            "Multiply by six: eight hundred fifty-seven thousand one hundred forty-two! "
            "Look closely at every single product—NOT ONE NEW DIGIT EVER APPEARED! All six digits stay locked inside the exact same circular necklace order, merely rotating cleanly like hands around a dial! And what happens when you multiply by seven? Nine hundred ninety-nine thousand nine hundred ninety-nine—matching point nine-bar equal to ONE!"
        ),
        "checkpoints": [
            {
                "question": "Knowing that 1/7 = 0.142857̄, without doing full multiplication, what are the repeating digits of 3/7 = 3 × 0.142857̄?",
                "options": [
                    "0.428571̄ (a cyclic rotation starting from digit 4)",
                    "0.333333̄",
                    "0.491234̄",
                    "0.571428̄"
                ],
                "answer": 0,
                "hint": "3 × 14 = 42, and cyclic order keeps the same circular ring 1 → 4 → 2 → 8 → 5 → 7 → 1!",
                "explanation": "Multiplying 142857 by 3 rotates the exact cycle cleanly to 428571, so 3/7 = 0.428571̄."
            },
            {
                "question": "What remarkable result occurs when you multiply the cyclic number 142857 by 7 (corresponding to 7 × 1/7)?",
                "options": [
                    "999,999 (matching 0.999999̄ = 1)",
                    "1,000,000",
                    "714,285",
                    "142,857"
                ],
                "answer": 0,
                "hint": "Divide 1 by 7 in decimal 0.142857̄ and multiply by 7!",
                "explanation": "142857 × 7 = 999,999, and similarly 7 × 0.142857̄ = 0.999999̄ = 1."
            }
        ]
    },
    {
        "id": 13,
        "title": "Irrational Decimal Chaos",
        "subtitle": "Section 3.6.3 Irrational Decimals: Non-Terminating, Non-Repeating Infinite Expansions (√2, π, & Constructed Chaos)",
        "speech": (
            "Compare the orderly repeating clockwork of one-seventh against Section Three Point Six Point Three: IRRATIONAL DECIMALS—CHAOS AND INFINITY! "
            "Whenever you compute the infinite decimal expansion of any irrational number such as root two, root three, or Pi, you enter a boundless stream of digits with ZERO termination and ZERO repeating loop! "
            "Look closely at root two: one point four one four two one three five six two three seven three zero nine five... Compute ten decimal places, ten thousand places, or ten billion decimal places—no block of digits EVER locks into permanent periodic repetition! "
            "Look closely at Pi: three point one four one five nine two six five three five eight nine seven nine three... Modern supercomputers calculate trillions of digits of Pi without ever discovering a single repeating cycle! "
            "Wait—can YOU effortlessly invent brand-new irrational decimals right on the spot? YES! Watch this crisp deterministic non-repeating pattern rule: zero point one zero one zero zero one zero zero zero one zero zero zero zero one... Each consecutive block deliberately inserts ONE extra zero digit right before the next digit one! Because zero-gaps keep stretching wider and wider forever, no fixed-length block can ever repeat identically!"
        ),
        "checkpoints": [
            {
                "question": "Which decimal expansion rule guarantees that a number is IRRATIONAL?",
                "options": [
                    "Non-terminating AND non-repeating (no fixed block ever repeats forever)",
                    "Terminating after 4 decimal places",
                    "Non-terminating with a repeating 6-digit cycle",
                    "Ending with repeated zeros"
                ],
                "answer": 0,
                "hint": "Remember terminating and repeating decimals are ALWAYS rational p/q!",
                "explanation": "A real number is irrational if and only if its decimal expansion neither terminates nor becomes periodically repeating."
            },
            {
                "question": "Why is the decimal 0.202002000200002... definitely an IRRATIONAL number?",
                "options": [
                    "The count of zeros between consecutive 2s increases by 1 each time, preventing any periodic cycle from ever repeating",
                    "Because it contains only digits 0 and 2",
                    "Because it stops after the fifth digit",
                    "Because 2 is a prime number"
                ],
                "answer": 0,
                "hint": "For a decimal to repeat with period k, the exact same block of length k must repeat endlessly!",
                "explanation": "Growing zero-runs (1, 2, 3, 4... zeros) prevent any fixed block of digits from ever repeating identically forever."
            }
        ]
    },
    {
        "id": 14,
        "title": "Set Hierarchy Journey",
        "subtitle": "Section 3.7 Conclusion: Nested Number Universe (ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ) & Frontier of Imaginary Numbers (i = √−1)",
        "speech": (
            "Step back in Section Three Point Seven to admire the breathtaking mathematical architecture you have explored—from simple clay pebbles all the way to infinite series! "
            "Examine the nested HIERARCHICAL SET SUMMARY: every single expansion kept all earlier numbers completely intact while solving a brand-new mathematical barrier! "
            "Begin at the innermost core with Natural Numbers N (one, two, three...) born from counting objects! Solving subtraction equations like x plus five equals two forced zero and negative debts into existence, expanding N cleanly into Integers Z! "
            "Next, solving linear division equations like three x equals two demanded ratios, expanding Z cleanly into Rational Numbers Q! "
            "Then solving geometric equations like x squared equals two unveiled irrational lengths like root two and Pi, uniting rationals and irrationals seamlessly into the continuous Real Number Line R! So N is a subset of Z, subset of Q, subset of R! "
            "Wait—does mathematics stop at R? Test one innocent-looking quadratic equation: x squared plus one equals zero, meaning x equals SQUARE ROOT OF MINUS ONE! "
            "Since every real number squares to a non-negative value, solving x squared equals minus one launches the frontier of IMAGINARY NUMBERS using i equals root minus one!"
        ),
        "checkpoints": [
            {
                "question": "Which nested subset chain accurately orders our number systems from innermost to outermost?",
                "options": [
                    "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ",
                    "ℝ ⊂ ℚ ⊂ ℤ ⊂ ℕ",
                    "ℚ ⊂ ℕ ⊂ ℝ ⊂ ℤ",
                    "ℤ ⊂ ℕ ⊂ ℝ ⊂ ℚ"
                ],
                "answer": 0,
                "hint": "Every natural is an integer, every integer is rational (n/1), and every rational is real!",
                "explanation": "Natural numbers ℕ lie inside integers ℤ, inside rationals ℚ, inside the complete real number line ℝ."
            },
            {
                "question": "Which algebraic equation cannot be solved inside Real Numbers ℝ and motivates the imaginary unit i = √(−1)?",
                "options": [
                    "x² + 1 = 0 (requiring x² = −1)",
                    "x² − 2 = 0 (solved by ±√2 ∈ ℝ)",
                    "3x − 2 = 0 (solved by 2/3 ∈ ℚ)",
                    "x + 5 = 2 (solved by −3 ∈ ℤ)"
                ],
                "answer": 0,
                "hint": "Any real number squared satisfies r² ≥ 0, never negative!",
                "explanation": "No real number has a negative square, so solving x² = −1 launches the imaginary unit i = √(−1)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Algebraic Identity Previews",
        "subtitle": "End-of-Chapter Exercises Preview: Proving √5 Irrational, Density Insertions, Radical Identities & Square Root Spiral",
        "speech": (
            "Preview essential analytical techniques from the End-of-Chapter Exercises uniting formal proofs, fraction operations, radical identities, and geometric spirals! "
            "First, generalize Hippasus's contradiction argument carefully to prove ROOT FIVE IS IRRATIONAL! Assume root five equals completely reduced fraction p over q! Squaring both sides gives five q squared equals p squared, forcing prime factor five to divide p squared and hence prime five MUST divide p! Setting p equals five k yields q squared equals five k squared, forcing five to also divide q—contradicting co-prime lowest terms! "
            "Second, apply RATIONAL DENSITY swiftly! To insert multiple evenly spaced rationals between a and b, or average midpoints, scale both to common denominators: between one-third and one-half, scaling denominators to thirty turns them into ten-thirtieths and fifteen-thirtieths, immediately exposing four crisp fractions strictly in between! "
            "Third, master RADICAL IDENTITIES! Expanding open root a plus root b close times open root a minus root b close cancels cross terms cleanly to exact rational integer difference a minus b! "
            "Fourth, trace the recursive SQUARE ROOT SPIRAL: adding perpendicular unit legs step by step unfolds root two, root three, root four, and root five cleanly outward like a radiant geometric spiral shell!"
        ),
        "checkpoints": [
            {
                "question": "Using the prime divisibility step from the √5 irrationality proof, if p² = 5q², what must follow immediately about integer p?",
                "options": [
                    "Since prime 5 divides p², 5 must divide p itself (allowing p = 5k)",
                    "p must be an even number",
                    "p must equal q",
                    "q must equal 1"
                ],
                "answer": 0,
                "hint": "By prime factorization, a prime p' dividing n² must divide n!",
                "explanation": "Because 5 is prime and divides p², 5 divides p, letting us substitute p = 5k to show 5 also divides q."
            },
            {
                "question": "Simplify the radical product (√7 + √3)(√7 − √3) using algebraic identities.",
                "options": [
                    "4 (since (√7)² − (√3)² = 7 − 3)",
                    "10",
                    "√4 = 2",
                    "4√21"
                ],
                "answer": 0,
                "hint": "Apply difference of squares: (x + y)(x − y) = x² − y²!",
                "explanation": "(√7 + √3)(√7 − √3) = (√7)² − (√3)² = 7 − 3 = 4 (a rational integer!)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary Matrix",
        "subtitle": "Chapter Summary: Natural Numbers, Śhūnya, Dhana/Riṇa Integers, ℚ Density, Irrational Proofs, ℝ Decimals, Cyclic 1/7 & Imaginary i",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your complete Chapter Summary Matrix mastering The World of Numbers! "
            "Review every chapter milestone cleanly from start to finish! First, ORIGINS OF COUNTING: clay pebbles built one-to-one correspondence N, Lebombo Bone tallied twenty-nine lunar notches, Ishango Bone recorded primes eleven, thirteen, seventeen, nineteen, Harappan cubical weights balanced maritime trade, and ancient Indian texts named decimal powers up to parārdha ten to the twelve and tallakṣaṇa ten to the fifty-three! "
            "Second, SHŪNYA AND INTEGERS: philosophical Śhūnyatā and Bakhśhālī's birch-bark bindu dot led directly to Brahmagupta's zero rules and Dhana-fortune versus Riṇa-debt integers Z, proving negative times negative removes debt into positive! "
            "Third, RATIONALS AND DENSITY: p over q with q non-zero fills spaces smoothly via equivalence a d equals b c, distance modulus a minus b, and midpoint density! "
            "Fourth, IRRATIONALS AND PI: Baudhāyana's unit square diagonal, Hippasus's root-two proof, compass root-n constructions, Āryabhaṭa's three point one four one six, and Mādhava's alternating infinite Pi series! "
            "Fifth, REAL LINE AND IMAGINARY FRONTIER: terminating denominators two-to-the-m five-to-the-n, repeating algebraic conversions, cyclic one-seventh, chaotic irrationals, nested N in Z in Q in R, and imaginary unit root minus one! Now test yourself and conquer all four silent mastery quizzes!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement accurately pairs a mathematical test with its exact number property?",
                "options": [
                    "Reduced fraction p/q terminates ⇔ q = 2ᵐ5ⁿ; cyclic 1/7 rotates 142857; irrational decimals neither terminate nor repeat",
                    "All square roots √n are irrational (even √4); all repeating decimals are irrational",
                    "Negative × negative gives negative under Dhana/Riṇa commerce",
                    "Zero has no arithmetic operations outside decimal placeholders"
                ],
                "answer": 0,
                "hint": "Check every clause against Sections 3.2, 3.3, 3.5, and 3.6!",
                "explanation": "Only reduced fractions with denominator primes strictly 2 and/or 5 terminate; 1/7 = 0.142857̄ is cyclic; irrationals never terminate or repeat."
            },
            {
                "question": "Which historical match across Indian and global number history is completely accurate?",
                "options": [
                    "Brahmagupta (628 CE): zero & negative rules; Baudhāyana (~800 BCE): √2 diagonal; Āryabhaṭa: 3927/1250; Mādhava: infinite π series",
                    "Hippasus: Lalitavistara powers up to 10⁵³; Lambert: Ishango Bone",
                    "Patanjali: square-root spiral; Bakhśhālī Manuscript: imaginary i",
                    "Lothal weights: irrational decimals of √5"
                ],
                "answer": 0,
                "hint": "Verify each scholar's exact century and signature contribution!",
                "explanation": "Brahmagupta codified zero/integers, Baudhāyana explored √2, Āryabhaṭa gave 3927/1250 = 3.1416, and Mādhava discovered the alternating infinite series for π."
            }
        ]
    }
]

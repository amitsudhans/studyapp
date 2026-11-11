#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 5: Number Play
Slides Data Generator - Part 2 (Slides 9 to 16)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Divisibility By Nine",
        "subtitle": "Section 5.2 Shortcut for 9: Remainder 1 Powers Proof (10 = 9+1, 100 = 99+1, 1000 = 999+1)",
        "speech": (
            "Uncover WHY summing digits solves DIVISIBILITY BY NINE cleanly across EVERY digit in the universe inside Section Five Point Two! Why don't we just inspect the units digit like 2, 5, or 10? Because dividing 10 by 9 leaves remainder ONE instead of zero! Watch what magic happens across EVERY higher power of ten! "
            "Decompose powers of ten beside multiples of nine cleanly: 10 = 9 + 1! 100 = 99 + 1! 1,000 = 999 + 1! 10,000 = 9,999 + 1! Notice EVERY single power of ten equals a chain of pure nines (ALWAYS cleanly divisible by 9) PLUS EXACTLY ONE leftover unit! "
            "Plug directly into ANY 4-digit integer N = 1000d + 100c + 10b + a! Rewrite smoothly: N equals (999d + 99c + 9b) + (d + c + b + a)! Factor nine cleanly outside that giant first bracket: 9 × (111d + 11c + b) + DIGIT SUM (d + c + b + a)! Immediately conclude TWO extraordinary laws: First, N is divisible by 9 IF AND ONLY IF its digit sum divides cleanly by 9! Second, N ALWAYS leaves the EXACT SAME REMAINDER modulo 9 as its digit sum!"
        ),
        "checkpoints": [
            {
                "question": "Why does expanding 1000d + 100c + 10b + a as 9(111d + 11c + b) + (d + c + b + a) prove the Divisibility-by-9 rule?",
                "options": [
                    "Every power 10ⁿ leaves remainder 1 modulo 9 (9, 99, 999... are divisible by 9), leaving ONLY the plain sum of digits to determine remainder modulo 9!",
                    "Because 9 divides 10 evenly",
                    "Because leading digit d must equal 9",
                    "Because units digit a determines divisibility by 9"
                ],
                "answer": 0,
                "hint": "Look at 10 = 9+1, 100 = 99+1, 1000 = 999+1 inside the algebraic identity!",
                "explanation": "Since 9 divides (999d + 99c + 9b), N and its digit sum share the exact same remainder upon division by 9."
            },
            {
                "question": "What single digit 'd' makes 74d58 cleanly divisible by 9, and what remainder does 74158 leave when divided by 9?",
                "options": [
                    "d = 3   (7+4+3+5+8 = 27 = 9×3);   remainder of 74158 ÷ 9 is 7",
                    "d = 6   (sum = 30);   remainder is 4",
                    "d = 9;   remainder is 1",
                    "d = 0;   remainder is 8"
                ],
                "answer": 0,
                "hint": "Sum known digits 7 + 4 + 5 + 8 = 24; next multiple of 9 is 27 (24 + d = 27)!",
                "explanation": "24 + 3 = 27 (multiple of 9); for 74158, digit sum = 25 = 2×9 + 7 → remainder 7."
            }
        ]
    },
    {
        "id": 10,
        "title": "Divisibility By Three",
        "subtitle": "Section 5.2 Shortcut for 3: Extending 10ⁿ = 3k + 1 & Comparing Divisibility by 3 vs 9",
        "speech": (
            "Now extend that exact remainder-one engine seamlessly to DIVISIBILITY BY THREE inside Section Five Point Two! Why does the exact same digit-sum rule also diagnose divisibility by THREE with 100 percent accuracy? "
            "Check EVERY multiple of nine (9, 99, 999, 9999, ...): since 9 = 3 × 3, THREE is a clean factor of NINE! Automatically EVERY power of ten ALSO writes cleanly as 10ⁿ = (a chain of nines) + 1 = 3k + 1! Plug directly into N = 1000d + 100c + 10b + a: N equals 3 × (333d + 33c + 3b) + DIGIT SUM (d + c + b + a)! "
            "Hence an integer N is divisible by 3 IF AND ONLY IF its digit sum divides cleanly by 3 (AND leaves identical remainder modulo 3)! "
            "Watch one vital comparison rule sharply right now! Is EVERY multiple of 9 ALSO automatically a multiple of 3? YES—ALWAYS! Is EVERY multiple of 3 ALSO automatically a multiple of 9? NO—NEVER guaranteed! Test 15, 21, or 432? Notice 432 sums cleanly to 9 (divisible by BOTH 9 and 3), whereas 123 sums cleanly to 6 (divisible by 3 ONLY, NOT by 9)!"
        ),
        "checkpoints": [
            {
                "question": "Why are ALL multiples of 9 automatically divisible by 3, whereas multiples of 3 (like 123 or 516) are NOT always divisible by 9?",
                "options": [
                    "Because 3 is a factor of 9 (so 9 | sum implies 3 | sum), yet a digit sum like 6 or 12 divides by 3 without dividing by 9!",
                    "Because 10 = 3×3 + 2",
                    "Because 9 is a factor of 3",
                    "Because 3 only checks the last two digits"
                ],
                "answer": 0,
                "hint": "Check digit sum of 516: 5 + 1 + 6 = 12 (divides by 3, leaves remainder 3 mod 9)!",
                "explanation": "Multiples of 9 form a strict subset inside multiples of 3; digit sum 12 divides by 3 cleanly, not by 9."
            },
            {
                "question": "List ALL single digits 'x' from {0..9} that make the 5-digit number 52x64 divisible by 3 (even if NOT divisible by 9):",
                "options": [
                    "x ∈ {1, 4, 7}   (known sum 17; adding 1→18, 4→21, 7→24 all divide by 3!)",
                    "x ∈ {1} only",
                    "x ∈ {0, 3, 6, 9}",
                    "x ∈ {2, 5, 8}"
                ],
                "answer": 0,
                "hint": "Sum known digits 5 + 2 + 6 + 4 = 17, then check which 17 + x divides by 3!",
                "explanation": "17 + 1 = 18, 17 + 4 = 21, 17 + 7 = 24 give x ∈ {1, 4, 7} (note only x=1 yields divisibility by 9)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Divisibility By Eleven",
        "subtitle": "Section 5.2 Shortcut for 11: Alternating Place Signs (1, 10=11−1, 100=99+1, 1000=1001−1)",
        "speech": (
            "Now solve one of algebra's prettiest divisibility tricks inside Section Five Point Two: THE SHORTCUT FOR ELEVEN! Why do we ALTERNATE plus and minus signs across consecutive digits instead of simply adding all digits together? Test powers of ten modulo 11 right now! "
            "Inspect EVERY consecutive power of ten beside multiples of eleven cleanly: Ones place 1 = 0 + 1 (OVER by +1)! Tens place 10 = 11 − 1 (SHORT by −1)! Hundreds place 100 = 99 + 1 (OVER by +1)! Thousands place 1,000 = 1,001 − 1 (SHORT by −1, since 1001 = 11 × 91)! Ten-thousands place 10,000 = 9,999 + 1 (OVER by +1)! Look at that unbroken alternating pulse: +1, −1, +1, −1, +1! "
            "Plug directly into ANY 4-digit integer N = 1000d + 100c + 10b + a cleanly: N = (1001d + 99c + 11b) + (a − b + c − d)! Since 11 cleanly divides EVERY single term inside that giant first bracket (1001 = 11×91, 99 = 11×9, 11 = 11×1), checking divisibility by 11 inspects ONLY (sum of odd-position digits from right) MINUS (sum of even-position digits)—testing quickly if that difference equals 0, ±11, ±22, or higher!"
        ),
        "checkpoints": [
            {
                "question": "Why does the Divisibility-by-11 test SUBTRACT even-position digits from odd-position digits (instead of adding all digits)?",
                "options": [
                    "Because powers of 10 alternate modulo 11 cleanly between (+1) and (−1): 1 = 0+1, 10 = 11−1, 100 = 99+1, 1000 = 1001−1!",
                    "Because 11 is an even prime number",
                    "Because all even places equal zero",
                    "Because 1001 is divisible by 9"
                ],
                "answer": 0,
                "hint": "Check signs of 1, 10, 100, 1000 modulo 11: +1, −1, +1, −1!",
                "explanation": "Odd powers of 10 equal (multiple of 11) − 1 while even powers equal (multiple of 11) + 1, forcing alternating signs."
            },
            {
                "question": "Check divisibility by 11 for 91,806 AND find missing digit 'y' making 6y53 divisible by 11:",
                "options": [
                    "91,806 IS divisible by 11 (9+8+6 − (1+0) = 22 = 11×2);   missing y = 8   ((6+5) − (8+3) = 0!)",
                    "91,806 fails divisibility;   y = 2",
                    "91,806 divides by 11;   y = 5",
                    "Both leave remainder 1"
                ],
                "answer": 0,
                "hint": "Odd places (right-to-left) for 91,806: 6+8+9 = 23, even: 0+1 = 1 → 23−1 = 22! For 6y53: (3+y) − (5+6) = y − 8 = 0!",
                "explanation": "Alternating sum gives 22 (divisible by 11) for 91,806, and y − 8 = 0 → y = 8 for 6853 (= 11×623)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Coprime Factor Rules",
        "subtitle": "Section 5.2 More Shortcuts: Composite Divisibility via Coprime Pairs (6 = 2×3, 24 = 3×8 vs Trap 4×6)",
        "speech": (
            "Beware one of the sharpest student traps in ALL of Section Five Point Two: COMPOSITE DIVISIBILITY RULES! How do we build rapid shortcuts for composite numbers like 6, 12, 15, 18, 24, or 44? By splitting the divisor strictly into COPRIME FACTORS (sharing HCF = 1)! "
            "Test 6 cleanly: split 6 = 2 × 3! Since HCF(2, 3) = ONE, checking divisibility by BOTH 2 (even units digit) AND 3 (digit sum ÷ 3) guarantees divisibility by LCM(2, 3) = SIX every single time! Similarly check 18 via 2 × 9 (HCF = 1), 15 via 3 × 5 (HCF = 1), 12 via 3 × 4 (HCF = 1), and 44 via 4 × 11 (HCF = 1)! "
            "Now catch the DEADLY STUDENT TRAP on 24! Why can you NEVER test divisibility by 24 using non-coprime factors 4 AND 6 alone? Check HCF(4, 6) = TWO ≠ 1! Look closely at number THIRTY SIX: 36 divides cleanly by 4 (= 9) AND divides cleanly by 6 (= 6), yet 36 FAILS divisibility by 24 (because LCM(4, 6) = 12, NOT 24)! Always pick COPRIME factor pair 3 × 8 (HCF(3, 8) = 1 → LCM = 24)!"
        ),
        "checkpoints": [
            {
                "question": "To test if a giant number divides cleanly by 24, why MUST you check divisibility by (3 and 8) instead of (4 and 6)?",
                "options": [
                    "Because HCF(3, 8) = 1 gives LCM(3, 8) = 24, whereas HCF(4, 6) = 2 gives LCM(4, 6) = 12 (numbers like 12 and 36 pass 4 & 6 yet fail 24!)",
                    "Because 4 × 6 does not equal 24",
                    "Because 6 has no divisibility shortcut",
                    "Because 3 and 8 are both even numbers"
                ],
                "answer": 0,
                "hint": "Remember Theorem Two from Section 5.1: passing k and m guarantees divisibility by LCM(k, m)!",
                "explanation": "Only coprime pairs (HCF = 1) make LCM(a, b) = a × b; 12 passes 4 and 6 yet fails 24."
            },
            {
                "question": "Which coprime shortcut pair cleanly tests divisibility by 45 and 18 respectively?",
                "options": [
                    "For 45: check (5 and 9);   for 18: check (2 and 9)",
                    "For 45: check (3 and 15);   for 18: check (3 and 6)",
                    "For 45: check (9 and 10);   for 18: check (6 and 6)",
                    "For 45: check (5 and 15);   for 18: check (3 and 9)"
                ],
                "answer": 0,
                "hint": "Verify HCF(5, 9) = 1 (product 45) and HCF(2, 9) = 1 (product 18)!",
                "explanation": "HCF(3, 15)=3 and HCF(3, 6)=3 fail coprime rules; (5, 9) and (2, 9) are strictly coprime."
            }
        ]
    },
    {
        "id": 13,
        "title": "Digital Roots History",
        "subtitle": "Section 5.2 Digital Roots: Repeated Digit Sums Modulo 9 & Aryabhata II's Mahāsiddhānta (c. 950 CE)",
        "speech": (
            "Discover an ancient mental arithmetic checksum inside Section Five Point Two: DIGITAL ROOTS and historical checking by ARYABHATA II! What is the DIGITAL ROOT of a counting number? Keep adding a number's digits repeatedly until JUST ONE SINGLE DIGIT (1 through 9, or 0 for 0) remains! "
            "Test 8,795 step by step: first add 8 + 7 + 9 + 5 = TWENTY NINE; add again 2 + 9 = ELEVEN; add one final time 1 + 1 = TWO! That single surviving digit TWO is the digital root of 8,795! "
            "Connect immediately with modulo 9 remainder from Slide Nine! Since every digit-sum reduction step preserves exact remainder modulo 9, ANY positive number's digital root matches its exact REMAINDER WHEN DIVIDED BY NINE (with digital root 9 marking exact non-zero multiples of 9—remainder 0)! Test 8,795 ÷ 9 = 977 remainder 2! "
            "Nearly eleven hundred years ago in c. 950 Common Era, Indian astronomer-mathematician ARYABHATA II famously codified this 'casting out nines' arithmetic check inside his Sanskrit treatise Mahāsiddhānta! Checking giant manual multiplication 47 × 36 = 1,692 takes just one quick mental arithmetic glance: digital root(47)=2, digital root(36)=9, product root(2×9)=9 matches digital root(1692)=9 effortlessly every single time!"
        ),
        "checkpoints": [
            {
                "question": "Compute the exact Digital Root of 9,685 AND deduce the remainder of 9,685 ÷ 9 cleanly:",
                "options": [
                    "Digital Root = 1   (9+6+8+5 = 28 → 2+8 = 10 → 1+0 = 1),   so remainder ÷ 9 equals 1!",
                    "Digital Root = 9;   remainder = 0",
                    "Digital Root = 2;   remainder = 2",
                    "Digital Root = 8;   remainder = 8"
                ],
                "answer": 0,
                "hint": "Add digits repeatedly until 1 single digit survives, and remember casting out 9s ignores digit 9 directly (6+8+5 = 19 → 10 → 1)!",
                "explanation": "9+6+8+5 = 28 → 2+8 = 10 → 1+0 = 1 (check: 9685 = 9×1076 + 1)."
            },
            {
                "question": "Who codified this digital-root ('casting out nines') arithmetic verification check historically in Mahāsiddhānta around 950 CE?",
                "options": [
                    "Aryabhata II",
                    "Fibonacci",
                    "Hammurabi",
                    "Euler"
                ],
                "answer": 0,
                "hint": "Distinguish Aryabhata I (499 CE) from the c. 950 CE author of Mahāsiddhānta!",
                "explanation": "Aryabhata II (~950 CE) documented digital-root arithmetic verification checks in Mahāsiddhānta."
            }
        ]
    },
    {
        "id": 14,
        "title": "Cryptarithm Logic Puzzles",
        "subtitle": "Section 5.3 Digits in Disguise: Unique Digit Rules (0–9, Non-Zero Lead) & Solving UT×3=PUT, BYE×6=RAY, JK×6=KKK",
        "speech": (
            "Enter Section Five Point Three: Digits in Disguise—solving CRYPTARITHMS (letter arithmetic puzzles)! Obey TWO golden rules strictly: First, EACH distinct capital letter stands for ONE UNIQUE DIGIT from 0 to 9 (no two different letters share the same digit)! Second, NO multi-digit number's leftmost leading letter can EVER equal zero! "
            "Watch logical elimination crush THREE famous NCERT puzzles instantly without tedious guessing! Puzzle One: UT × 3 = PUT! Notice 2-digit UT appears identically at the right end of 3-digit PUT = 100P + UT! Subtract UT cleanly from BOTH sides: 2 × UT = 100P, dividing by 2 gives UT = 50 × P! Since UT stays 2 digits (< 100), P MUST equal 1, immediately snapping UT = 50 (check: 50 × 3 = 150)! "
            "Puzzle Two: JK × 6 = KKK! Rewrite KKK cleanly as 111 × K = 3 × 37 × K! Dividing BOTH sides by 6 gives JK = (37 × K) ÷ 2! Since JK is an even 2-digit whole number (< 100), try K = 2 (gives 37, mismatch!) or K = 4 (37 × 2 = 74 → J=7, K=4: check 74 × 6 = 444)! Puzzle Three: BYE × 6 = RAY solves uniquely cleanly as 105 × 6 = 630!"
        ),
        "checkpoints": [
            {
                "question": "In the cryptarithm UT × 3 = PUT (distinct letters, P ≠ 0, U ≠ 0), find the exact digit values of P, U, and T:",
                "options": [
                    "P = 1,   U = 5,   T = 0   (50 × 3 = 150)",
                    "P = 2,   U = 5,   T = 0   (50 × 3 = 250)",
                    "P = 1,   U = 2,   T = 5   (25 × 3 = 125)",
                    "P = 3,   U = 1,   T = 0   (10 × 3 = 310)"
                ],
                "answer": 0,
                "hint": "Rewrite UT × 3 = 100P + UT → 2 × UT = 100P → UT = 50P!",
                "explanation": "UT = 50P forces P = 1 (if P ≥ 2, UT ≥ 100 isn't 2-digit), yielding 50 × 3 = 150 cleanly."
            },
            {
                "question": "Solve cryptarithm JK × 6 = KKK (distinct letters, J ≠ 0, K ≠ 0) cleanly:",
                "options": [
                    "J = 7,   K = 4   (74 × 6 = 444)",
                    "J = 3,   K = 7   (37 × 6 = 222 — units digits 7 and 2 don't match K!)",
                    "J = 6,   K = 6   (66 × 6 = 396)",
                    "J = 5,   K = 2   (52 × 6 = 312)"
                ],
                "answer": 0,
                "hint": "Write KKK = 111K → JK = 111K / 6 = 37K / 2; plug even K ∈ {2, 4, 6, 8} so the resulting units digit equals K!",
                "explanation": "K=4 gives JK = 37 × 4 / 2 = 74, matching units digit 4 (74 × 6 = 444)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Multi Digit Constraints",
        "subtitle": "Section 5.3 Figure It Out: Solving 48a23b ÷ 18, 3p7q8 ÷ 44, Reverse-Digit Properties & Venn Sets",
        "speech": (
            "Master multi-constraint NCERT Figure It Out puzzles inside Section Five Point Three cleanly! First inspect reverse-digit integer pairs carefully: subtracting reversed 10b + a from 10a + b yields 9(a − b)—ALWAYS divisible by 9—while adding both gives 11(a + b)—ALWAYS divisible by 11! "
            "Now conquer multi-variable divisibility digit locks systematically step by step! Example One: make 48a23b divisible by EIGHTEEN (coprime factors 18 = 2 × 9)! Inspect units digit b FIRST: divisibility by 2 restricts b cleanly to {0, 2, 4, 6, 8}! Suppose b = 4: apply divisibility by 9: 4 + 8 + a + 2 + 3 + 4 = 21 + a → next multiple of 9 is 27, locking a = 6 (verify: 4,86,234 ÷ 18 = 27,013)! "
            "Example Two: make 3p7q8 divisible by FORTY FOUR (coprime 44 = 4 × 11)! Check 4 FIRST on last two digits (q8): q MUST be EVEN {0, 2, 4, 6, 8}! Next apply alternating 11-rule: (3 + 7 + 8) − (p + q) = 18 − (p + q)! Choosing q = 2 gives 16 − p = 11 → exact digit p = 5 (35,728 ÷ 44 = 812)!"
        ),
        "checkpoints": [
            {
                "question": "If the 6-digit number 48a23b must be divisible by 18 and units digit b = 6, what is the unique digit 'a'?",
                "options": [
                    "a = 4   (digit sum 4+8+a+2+3+6 = 23 + a = 27 → a = 4)",
                    "a = 2",
                    "a = 6",
                    "a = 8"
                ],
                "answer": 0,
                "hint": "With b = 6 (already even!), find digit 'a' making 4 + 8 + a + 2 + 3 + 6 divisible by 9!",
                "explanation": "23 + 4 = 27 is the sole 0–9 choice yielding a multiple of 9 (484,236 ÷ 18 = 26,902)."
            },
            {
                "question": "If the 5-digit number 3p7q8 is divisible by 44 (4 × 11) and tens digit q = 2, which unique digit 'p' works?",
                "options": [
                    "p = 5   (alternating check: (3+7+8) − (p+2) = 16 − p = 11 → p = 5; check 35,728 = 44 × 812!)",
                    "p = 2",
                    "p = 7",
                    "p = 9"
                ],
                "answer": 0,
                "hint": "Note 28 divides by 4 cleanly; solve 18 − (p + 2) ∈ {0, 11} keeping 0 ≤ p ≤ 9!",
                "explanation": "16 − p = 11 gives p = 5 (note 16 − p = 0 requires p = 16, invalid single digit)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Navakankari Chapter Summary",
        "subtitle": "Chapter Recap & Puzzle Time: Navakankari (Sālu Mane Aṭa / Nine Men's Morris) Rules & Strategy",
        "speech": (
            "Congratulations on completing NCERT Class Eight Chapter Five: Number Play completely! Snapshot ALL three big mathematical pillars right now before playing traditional Indian strategy game NAVAKANKARI and solving forty Challenge Questions! "
            "Checklist One: Consecutive sums skip powers of 2; flipping signs alters totals by even 2b keeping parity invariant; evens split modulo 4 into 4p and 4p+2; divisibility inherits downward to all factors and scales cleanly to LCM(k, m)! Checklist Two: Place-value remainders prove shortcuts for 2, 4, 8, 5, 10 (trailing digits), 3 & 9 (digit sums & digital roots), 11 (alternating sums), and coprime products! Checklist Three: Cryptarithms obey unique 0–9 mapping and non-zero leading digits! "
            "Now play IT'S PUZZLE TIME: NAVAKANKARI—known regionally across India as Sālu Mane Aṭa, Chār-Pār, or Navkakri (historically identical to Nine Men's Morris)! Two strategy players hold NINE pawns each on a three-concentric-squares 24-point grid! First take turns PLACING all 9 pawns onto empty vertex dots, then SLIDE pawns step by step along straight connecting lines! Whenever three friendly pawns align orthogonally in a straight three-point row (forming a MILL!), immediately CAPTURE one rival pawn off the board—winning cleanly once rival pieces drop down to just TWO surviving pawns!"
        ),
        "checkpoints": [
            {
                "question": "In the traditional Indian board game Navakankari (Sālu Mane Aṭa / Nine Men's Morris), how many pawns does each player start with and what earns an immediate capture?",
                "options": [
                    "9 pawns per player; forming a 3-in-a-row line (Mill) along grid lines captures 1 rival pawn!",
                    "4 pawns per player; jumping diagonally captures all pieces",
                    "16 pawns per player; forming a 4-corner square captures 2 pieces",
                    "6 pawns per player; rolling dice decides captures"
                ],
                "answer": 0,
                "hint": "Think of the Sanskrit/Kannada clues 'Nava' (Nine) and 'Sālu' (Row/Line of 3)!",
                "explanation": "Players begin with 9 pawns each and form 3-in-a-row mills to eliminate opponent pawns until a player drops below 3."
            },
            {
                "question": "Which grand Chapter 5 rule check is 100% ACCURATE?",
                "options": [
                    "4|N checks last 2 digits; 9|N checks digit sum; 11|N checks alternating sum; composite divisibility requires COPRIME factors (HCF = 1)!",
                    "Divisibility by 24 can safely be checked by testing 4 and 6 alone",
                    "Flipping '+' to '−' alters a sum by 1b (odd/even shift)",
                    "Every consecutive-integer sum fails for odd numbers"
                ],
                "answer": 0,
                "hint": "Verify each shortcut and recall why HCF(4, 6) = 2 fails 24!",
                "explanation": "Every shortcut in Option 1 holds universally across place-value algebra."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch5 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

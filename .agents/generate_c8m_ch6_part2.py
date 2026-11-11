#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 6: We Distribute, Yet Things Multiply
Slides Data Generator - Part 2 (Slides 9 to 16)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Sum Of Squares",
        "subtitle": "Section 6.2 Pattern 1: Identity 2(a² + b²) = (a+b)² + (a−b)² & Calendar Diagonal Products",
        "speech": (
            "Explore Section Six Point Two's dazzling Identity Patterns right now! Look what magical simplification snaps out when we ADD Identity 1A and Identity 1B side by side! "
            "Add (a + b)² = a² + 2ab + b² cleanly onto (a − b)² = a² − 2ab + b²! Watch the opposing middle terms (+2ab) and (−2ab) CANCEL OUT COMPLETELY TO ZERO! Leftover terms pair identically: a² + a² = 2a² and b² + b² = 2b²! Immediately capture PATTERN ONE: (a + b)² + (a − b)² ALWAYS equals 2(a² + b²)! Even subtract instead if curious: (a + b)² − (a − b)² equals exact 4ab! "
            "Test Pattern One rapidly on tough mental squares: evaluate 103² + 97² cleanly! Rewrite BOTH terms as (100 + 3)² + (100 − 3)² = 2(100² + 3²) = 2(10,000 + 9) = exact 20,018 in three quick seconds flat! "
            "Apply algebra ALSO to monthly calendar number grids: pick ANY 2 × 2 square block of calendar dates [n, n+1] above [n+7, n+8] on a standard weekly calendar! Diagonal cross-product differences cleanly stay invariant: (n+1)(n+7) − n(n+8) = (n² + 8n + 7) − (n² + 8n) = EXACT SEVEN ALWAYS!"
        ),
        "checkpoints": [
            {
                "question": "Evaluate (54² + 46²) instantly without expanding two squares individually, using Pattern 1: (a+b)² + (a−b)² = 2(a² + b²):",
                "options": [
                    "5,032   [= 2 × (50² + 4²) = 2 × 2,516]",
                    "2,516",
                    "5,016",
                    "4,968"
                ],
                "answer": 0,
                "hint": "Rewrite 54 = 50 + 4 and 46 = 50 − 4, so a = 50 and b = 4 inside 2(a² + b²)!",
                "explanation": "(50+4)² + (50−4)² = 2(50² + 4²) = 2(2500 + 16) = 5,032."
            },
            {
                "question": "In any monthly calendar's 2 × 2 date square [n, n+1; n+7, n+8], compute the constant diagonal product difference [(n+1)(n+7) − n(n+8)]:",
                "options": [
                    "Always 7   [since (n² + 8n + 7) − (n² + 8n) = 7 for EVERY date n!]",
                    "Always 1",
                    "Depends on date n",
                    "Always 14"
                ],
                "answer": 0,
                "hint": "Expand both products cleanly via Identity 1 and cancel n² + 8n!",
                "explanation": "(n² + 7n + n + 7) − (n² + 8n) = 7 unconditionally for every calendar square."
            }
        ]
    },
    {
        "id": 10,
        "title": "Difference Of Squares",
        "subtitle": "Section 6.2 Identity 1C: (a + b)(a − b) = a² − b² Algebraic & Cut-and-Move Geometric Proof",
        "speech": (
            "Now unlock IDENTITY 1C inside Section Six Point Two—arguably school algebra's sharpest mental calculation shortcut: THE DIFFERENCE OF TWO SQUARES! Multiply the sum of two numbers directly by their exact difference: (a + b)(a − b)! Distribute cleanly via Identity One: a² − ab + ba − b²! Notice both opposite middle terms (−ab) and (+ab) annihilate completely to zero, leaving ONLY exact identity: (a + b)(a − b) ALWAYS equals a² − b² across EVERY pair of numbers! "
            "Visualize Identity 1C geometrically by cutting and rearranging paper! Begin cleanly with a large square of side 'a' (area a²), and snip out ONE corner square of side 'b' (leaving remaining L-shaped region of area a² − b²)! Now slice cleanly along one horizontal dashed cut line to separate the leftover L-shape into two rectangles: height (a − b) × width a, plus height b × width (a − b)! Rotate that smaller b × (a − b) rectangle and attach it smoothly along the right end—forming ONE clean single solid rectangle measuring width (a + b) by height (a − b)! Test 104 × 96 instantly: (100 + 4)(100 − 4) = 10,000 − 16 = 9,984 effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "Multiply 107 × 93 mentally in one glance using Identity 1C: (a + b)(a − b) = a² − b²:",
                "options": [
                    "9,951   [= (100 + 7)(100 − 7) = 10,000 − 49]",
                    "10,049",
                    "9,949",
                    "9,851"
                ],
                "answer": 0,
                "hint": "Center halfway at a = 100 with b = 7, then subtract 7² = 49 from 10,000!",
                "explanation": "107 × 93 = (100+7)(100−7) = 100² − 7² = 10,000 − 49 = 9,951."
            },
            {
                "question": "Factorize and evaluate 85² − 15² cleanly using Identity 1C in reverse:",
                "options": [
                    "7,000   [= (85 + 15)(85 − 15) = 100 × 70]",
                    "4,900",
                    "7,225",
                    "6,800"
                ],
                "answer": 0,
                "hint": "Compute (85 + 15) × (85 − 15) without squaring 85!",
                "explanation": "a² − b² = (a+b)(a−b) gives 100 × 70 = 7,000 instantly."
            }
        ]
    },
    {
        "id": 11,
        "title": "Sridharacharya Squaring Trick",
        "subtitle": "Section 6.2 Modified Identity 1C: Śrīdharācārya's Method a² = (a+b)(a−b) + b² (e.g. 197² = 38,809)",
        "speech": (
            "Discover a brilliant squaring trick preserved by medieval Indian algebra master ŚRĪDHARĀCĀRYA inside Section Six Point Two! Look straight back at Identity 1C: (a + b)(a − b) = a² − b²! Simply add (+b²) cleanly onto BOTH sides of that equation simultaneously! "
            "Behold ŚRĪDHARĀCĀRYA'S SQUARING FORMULA: a² ALWAYS equals (a + b)(a − b) + b²! Why is moving (−b²) across the equals sign so wildly clever? Because to square ANY awkward integer 'a' sitting near a friendly round multiple of ten or hundred (just small distance b away!), you smoothly shift BOTH UP by b to hit that clean round multiple AND DOWN by equal b—turning hard multiplication into an effortless round-zero product PLUS tiny b²! "
            "Test directly on 197²! Sitting just distance b = 3 away from convenient round anchor 200, shift smoothly up by 3 (197 + 3 = 200) and symmetrically down by 3 (197 − 3 = 194)! Multiply cleanly: 200 × 194 = 38,800, then add tiny 3² = 9 → exact 38,809 instantly! Even works seamlessly across rational decimal fractions like (3.5)² = (4 × 3) + 0.25 = 12.25 and negative integers cleanly every single time!"
        ),
        "checkpoints": [
            {
                "question": "Compute 197² cleanly using Śrīdharācārya's modified Identity 1C formula: a² = (a + b)(a − b) + b² (with b = 3):",
                "options": [
                    "38,809   [= (200 × 194) + 3² = 38,800 + 9]",
                    "38,791   [= 38,800 − 9]",
                    "38,803",
                    "39,209"
                ],
                "answer": 0,
                "hint": "Remember moving −b² to the other side makes it +b² (+9)!",
                "explanation": "197² = (197+3)(197−3) + 3² = 200×194 + 9 = 38,809."
            },
            {
                "question": "Apply Śrīdharācārya's trick a² = (a+b)(a−b) + b² cleanly to find 94² (choosing round anchor 100, so b = 6):",
                "options": [
                    "8,836   [= (100 × 88) + 6² = 8,800 + 36]",
                    "8,764   [= 8,800 − 36]",
                    "8,936",
                    "9,436"
                ],
                "answer": 0,
                "hint": "Shift up 94+6 = 100 and down 94−6 = 88, then ADD 6² = 36!",
                "explanation": "94² = (100 × 88) + 36 = 8,836."
            }
        ]
    },
    {
        "id": 12,
        "title": "Mend Algebraic Mistakes",
        "subtitle": "Section 6.3 'Mind the Mistake, Mend the Mistake': Sign Drops, Partial Distribution & Missing 2ab",
        "speech": (
            "Enter Section Six Point Three: Mind the Mistake, Mend the Mistake! Even top mathematics students drop precious marks on algebra tests NOT from hard geometry theorems, but from subtle distribution slips! Let us inspect, catch, and mend the biggest classic student traps right now! "
            "Trap One, Incomplete Distribution: carelessly writing 4(x + 5) = 4x + 5! Why is that wrong? Outer multiplier 4 completely forgot to multiply the SECOND term +5 sitting inside parentheses! Fix cleanly: 4x + 4(5) = 4x + 20! "
            "Trap Two, Dropping Negative Signs: expanding −3(y − 7) carelessly as −3y − 21! Why is that wrong? Multiplying negative −3 by negative −7 MUST turn PLUS (+21)! Fix cleanly: −3y + 21! Similarly outer minus −(a − b + c) flips and distributes −1 across EVERY single interior term cleanly: −a + b − c! "
            "Trap Three, The Freshman's Dream: wrongly claiming (x + y)² = x² + y² or (x − 5)² = x² − 25! Never ignore middle algebraic cross-terms! Test concrete integer values x = 3, y = 4: (3+4)² = 49, whereas 3²+4² = 25! Always keep full Identity 1A (+2xy) and 1B (−10x + 25) cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Spot the exact algebraic error and repair:   5 − 2(3x − 4) = 3(3x − 4) = 9x − 12.",
                "options": [
                    "Error: subtracted 5 − 2 BEFORE multiplying −2(3x − 4)! Correct: 5 − 6x + 8 = 13 − 6x",
                    "Error: should multiply 5 × 2 first to get 10(3x − 4)",
                    "The original answer 9x − 12 is already correct",
                    "Correct answer is 5 − 6x − 8 = −6x − 3"
                ],
                "answer": 0,
                "hint": "Follow BODMAS & sign distribution strictly: multiply −2 across (3x − 4) FIRST (−6x + 8) before adding 5!",
                "explanation": "Multiplication precedes subtraction: 5 + (−2)(3x) + (−2)(−4) = 5 − 6x + 8 = 13 − 6x."
            },
            {
                "question": "Identify why the statement '(p + 6)² = p² + 36' fails, and write the correct expanded identity:",
                "options": [
                    "Fails because it skipped the middle cross-term 2(p)(6) = 12p;   Correct: p² + 12p + 36",
                    "Fails because 6² = 12;   Correct: p² + 12",
                    "Fails because +36 should be −36;   Correct: p² − 36",
                    "It is already an accurate identity for all p"
                ],
                "answer": 0,
                "hint": "Recall (p + 6)(p + 6) creates BOTH p×6 and 6×p inner strips = +12p!",
                "explanation": "Identity 1A gives p² + 2(p)(6) + 6² = p² + 12p + 36 (only holds at p = 0!)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Sign Like Terms",
        "subtitle": "Section 6.3 Error Repair Lab: Unlike Terms (3x+2y ≠ 5xy), Double Binomial Expansions & Bracket Order",
        "speech": (
            "Continue carefully mending Section Six Point Three's twelve notorious algebra traps so ZERO calculation bugs ever survive inside your exercise notebooks! "
            "Trap Four, Combining Unlike Terms: simplifying 3x + 2y carelessly into 5xy, OR adding 2x² + 5x straight into 7x³! Remember algebra's unbreakable golden rule: ONLY LIKE TERMS carrying identical letters raised to IDENTICAL EXPONENTS can ever add or subtract numerical coefficients! Notice 3x + 2y MUST stay 3x + 2y (3 apples + 2 bananas never merge into 5 apple-bananas!), while 2x² + 5x stays 2x² + 5x cleanly! "
            "Trap Five, Squaring Coefficients & Bracket Products Improperly: writing (3x)² as 3x² instead of exact 9x², OR expanding 2(x + 3)(x + 4) by pushing scalar 2 inside BOTH brackets to get (2x + 6)(2x + 8)! Why is that wrong? Multiplying BOTH bracket factors by 2 accidentally scales the entire algebraic product by FOUR instead of TWO! Distribute scalar 2 across ONLY ONE single bracket factor cleanly: 2(x² + 7x + 12) = 2x² + 14x + 24! "
            "Trap Six, Fractional & Binomial Cross-Term Sign Drops: ALWAYS double-check middle cross-terms and negative squares cleanly like (2a − 3b)² = 4a² − 12ab + 9b² without dropping a single negative sign!"
        ),
        "checkpoints": [
            {
                "question": "Fix ALL errors inside the student's incorrect line:   '3(x + 2) + (2x)² = 3x + 2 + 2x² = 5x³ + 2':",
                "options": [
                    "Fixed: 3x + 6 + 4x²   (distribute 3 to +2 = +6; square coefficient (2x)² = 4x²; never combine unlike terms 3x and 4x²!)",
                    "Fixed: 3x + 6 + 2x²",
                    "Fixed: 7x³ + 6",
                    "Fixed: 3x + 6 + 4x² = 7x³ + 6"
                ],
                "answer": 0,
                "hint": "Fix three distinct mistakes: 3×2 = 6, (2x)² = 2²x² = 4x², and 4x² + 3x cannot merge!",
                "explanation": "3(x + 2) + (2x)² simplifies properly to 4x² + 3x + 6."
            },
            {
                "question": "What goes wrong if someone simplifies 2(x + 1)(x + 5) as '(2x + 2)(2x + 10)'?",
                "options": [
                    "They multiplied by 2 TWICE (= ×4 instead of ×2!); scalar 2 multiplies ONLY ONE factor: 2(x² + 6x + 5) = 2x² + 12x + 10!",
                    "Scalar 2 should not multiply any term inside parentheses",
                    "(2x + 2)(2x + 10) is actually equal to 2(x + 1)(x + 5)",
                    "They should add 2 instead of multiplying"
                ],
                "answer": 0,
                "hint": "Test x = 0: 2(1)(5) = 10, whereas (2)(10) = 20!",
                "explanation": "Multiplication is associative, not distributive over multiplication itself: multiply by 2 ONCE to get 2x² + 12x + 10."
            }
        ]
    },
    {
        "id": 14,
        "title": "Four Pattern Perspectives",
        "subtitle": "Section 6.4 'This Way or That Way': Proving (k+1)²−1, k²+2k, k(k+1)+k & k(k+2) All Equal k² + 2k",
        "speech": (
            "Enter Section Six Point Four's joyful title topic: THIS WAY OR THAT WAY, ALL WAYS LEAD TO THE BAY! Imagine four students staring at the EXACT SAME growing tile L-frame bordering a k × k square core (think k = 1 gives 3 border dots, k = 2 gives 8 dots, k = 3 gives 15 dots)! Each viewer sees the picture through a DIFFERENT creative geometric slice—yet algebra proves ALL FOUR expressions equal the EXACT SAME polynomial! "
            "Compare all four viewpoints cleanly! Method One sees one giant (k + 1) × (k + 1) square with 1 missing corner tile: (k + 1)² − 1! Method Two sees one k × k inner square PLUS two outer arms of length k: k² + 2k! Method Three slices ONE tall k × (k + 1) rectangle PLUS one extra row of k: k(k + 1) + k! Method Four swings one side strip onto the end to form ONE flat rectangle: k × (k + 2)! "
            "Expand ALL FOUR cleanly: (k² + 2k + 1) − 1 = k² + 2k; k² + k + k = k² + 2k; k² + 2k! ALL FOUR paths simplify identically to k² + 2k!"
        ),
        "checkpoints": [
            {
                "question": "Expand and compare Method 1 [(k + 1)² − 1] and Method 4 [k(k + 2)] algebraically:",
                "options": [
                    "Both expand cleanly to the identical polynomial k² + 2k (proving all four counting methods are algebraically equivalent!)",
                    "Method 1 gives k² only while Method 4 gives k² + 2",
                    "Only Method 4 equals k² + 2k",
                    "They agree ONLY when k = 1"
                ],
                "answer": 0,
                "hint": "Expand (k+1)² = k² + 2k + 1, subtract 1; then distribute k(k + 2)!",
                "explanation": "(k+1)² − 1 = (k²+2k+1) − 1 = k² + 2k, and k(k+2) = k² + 2k identically."
            },
            {
                "question": "If tile step k = 10, how many tiles appear in the pattern under ALL FOUR methods (k² + 2k)?",
                "options": [
                    "120 tiles   [check: (11² − 1) = 120; 10² + 20 = 120; 10(11) + 10 = 120; 10 × 12 = 120!]",
                    "102 tiles",
                    "121 tiles",
                    "100 tiles"
                ],
                "answer": 0,
                "hint": "Substitute k = 10 cleanly into k² + 2k (or k(k + 2) = 10 × 12)!",
                "explanation": "All 4 formulas yield exact 120 tiles at step k = 10."
            }
        ]
    },
    {
        "id": 15,
        "title": "Border Walkway Areas",
        "subtitle": "Section 6.4 Multi-Method Areas: Park Borders, Frames, I-Beams & Figure It Out Equivalences",
        "speech": (
            "Apply Section Six Point Four's multi-perspective equivalence directly onto real geometric border walkways, wooden picture frames, steel I-beams, and park boundary area puzzles! "
            "Suppose a rectangular garden park measuring length L by breadth B gets surrounded completely outside by a flat paved walking path of uniform width w! Calculate the exact shaded WALKWAY BORDER AREA using TWO completely different geometric dissection paths and prove both match identically! "
            "Path One, Outer Minus Inner Rectangle Subtraction: outer rectangle full length equals (L + 2w) and outer full breadth equals (B + 2w)! Subtract inner rectangular garden park area (LB) cleanly: Border Area = (L + 2w)(B + 2w) − LB! Expand smoothly via Identity One: (LB + 2wL + 2wB + 4w²) − LB = 2wL + 2wB + 4w²! "
            "Path Two, Four Strips + Four Corners Addition: sum top/bottom long rectangular boundary strips (2 × wL), left/right side boundary strips (2 × wB), PLUS all four corner square tiles w × w (4w²): 2wL + 2wB + 4w²! EXACT IDENTICAL MATCH! Even slicing shaded structural I-beams or nested concentric square frames cleanly proves total shaded area = outer rectangle minus two symmetric cutout notches identically every single time!"
        ),
        "checkpoints": [
            {
                "question": "A rectangular park of dimensions L × B is surrounded outside by a uniform path of width w. Which expression simplifies BOTH [(L + 2w)(B + 2w) − LB] AND four-strip assembly?",
                "options": [
                    "2wL + 2wB + 4w²",
                    "2wL + 2wB + w²",
                    "LB + 4w²",
                    "2w(L + B) − 4w²"
                ],
                "answer": 0,
                "hint": "Expand (L + 2w)(B + 2w) carefully to see the four w×w corner squares (+4w²), then subtract LB!",
                "explanation": "LB + 2wL + 2wB + 4w² − LB = 2wL + 2wB + 4w²."
            },
            {
                "question": "For a 10 m × 6 m park surrounded by a 2 m uniform outer walkway (w = 2), compute the exact walkway area:",
                "options": [
                    "80 m²   [check: (14 × 10) − (10 × 6) = 140 − 60 = 80, AND 2(2)(10) + 2(2)(6) + 4(4) = 40 + 24 + 16 = 80!]",
                    "64 m²",
                    "140 m²",
                    "68 m²"
                ],
                "answer": 0,
                "hint": "Check BOTH outer−inner (14×10 − 60) AND formula (40 + 24 + 16)!",
                "explanation": "Both geometric pathways confirm 80 m²."
            }
        ]
    },
    {
        "id": 16,
        "title": "Coin Conjoin Summary",
        "subtitle": "Chapter Consolidation & Puzzle Time ('Coin Conjoin': Inverting 10-Coin Triangle in 3 Moves + Triangular Numbers)",
        "speech": (
            "Congratulations on conquering NCERT Class Eight Chapter Six: We Distribute, Yet Things Multiply! Lock ALL four pillars cleanly before solving forty Challenge Questions and playing 'COIN CONJOIN'! "
            "Master Recap: First, general binomial product (a + b)(c + d) = ac + ad + bc + bd (via Brahmagupta's khaṇḍa-guṇanam) powers mental multiplication (×11, ×101, ×99) and product increments! Second, three core algebraic identities hold forever: (a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², and (a + b)(a − b) = a² − b² (plus Śrīdharācārya's a² = (a+b)(a−b) + b²)! Third, avoid sign traps and skipped middle terms! Fourth, creative multiple slices ALWAYS simplify to ONE invariant algebraic expression! "
            "Now tackle IT'S PUZZLE TIME—Coin Conjoin! Arrange TEN flat circular coins cleanly as an upright equilateral triangle (rows 1, 2, 3, 4)! How can you flip the triangle completely UPSIDE DOWN (rows 4, 3, 2, 1) moving the STRICT MINIMUM number of coins? JUST THREE MOVES! Slide bottom-left and bottom-right corner coins neatly up beside row two, and slide the lone top apex coin straight down below row four—generalizing smoothly across larger 15-coin (five moves) triangular numbers!"
        ),
        "checkpoints": [
            {
                "question": "In the 'Coin Conjoin' puzzle with a 10-coin equilateral triangle (rows 1, 2, 3, 4), what is the MINIMUM number of coins you must move to invert the triangle upside down?",
                "options": [
                    "3 coins   (move 1 top apex coin down to bottom peak, and 2 bottom corner coins up to flanks of row 2!)",
                    "5 coins",
                    "6 coins",
                    "4 coins"
                ],
                "answer": 0,
                "hint": "Notice a central 6-coin upward triangle + 1 coin stays completely untouched (7 coins stay stationary out of 10: 10 − 7 = 3 moves)!",
                "explanation": "7 interior coins remain completely fixed as an overlapping inverted core, requiring ONLY 3 outer vertex moves!"
            },
            {
                "question": "What minimum number of coin moves inverts a larger 15-coin triangle (rows 1, 2, 3, 4, 5)?",
                "options": [
                    "5 coins   (floor(15 / 3) = 5; 10 interior coins stay stationary while 5 outer coins move!)",
                    "3 coins",
                    "7 coins",
                    "10 coins"
                ],
                "answer": 0,
                "hint": "Apply the general triangular inversion rule floor(Tₙ / 3) = floor(15 / 3)!",
                "explanation": "For T₅ = 15 coins, 10 overlapping core coins remain fixed and 15 − 10 = 5 outer coins move!"
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch6 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

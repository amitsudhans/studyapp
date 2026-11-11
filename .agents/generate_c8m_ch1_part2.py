#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 1: A Square and A Cube
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Cubic Numbers Intro",
        "subtitle": "Section 1.2 Foundations: 3D Unit-Cube Stacking (n³ = n × n × n), Perfect Cubes & Dimension Scaling",
        "speech": (
            "Now leap cleanly from flat two-dimensional squares straight into three-dimensional solid volume inside Section One Point Two: Cubic Numbers! "
            "Imagine stacking small 1 × 1 × 1 unit wooden cubes to assemble larger solid cubes! To build a solid cube of side 2 units, you need 2 layers each containing 2 × 2 = 4 blocks: 2 × 2 × 2 = EIGHT unit cubes! To build side 3 units, stack 3 × 3 × 3 = TWENTY SEVEN unit cubes! Generally, n cubed (written n³ = n × n × n) literally measures the solid 3D VOLUME of a cube of edge length n! "
            "Whenever n is a natural counting number (1, 2, 3, 4, 5, ...), n³ equals 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000 and onward, and is called a PERFECT CUBE (or cubic number)! Notice how rapidly cubes grow compared to squares, and remember doubling side length multiplies cube volume by 2³ = EIGHT TIMES! "
            "You can also cube fractions and decimals cleanly! A tiny cube of edge 0.2 cm has exact volume 0.2 × 0.2 × 0.2 = 0.008 cm³ (THREE decimal places!), and (2/3)³ = 8/27!"
        ),
        "checkpoints": [
            {
                "question": "How many small 1 × 1 × 1 unit cubes are required to build one solid 4 × 4 × 4 cube, and what happens to cube volume if side length triples (n → 3n)?",
                "options": [
                    "64 unit cubes (= 4³);   tripling side length multiplies volume by 27× (= 3³)",
                    "16 unit cubes;   tripling multiplies volume by 9×",
                    "12 unit cubes;   tripling multiplies volume by 3×",
                    "64 unit cubes;   tripling multiplies volume by 6×"
                ],
                "answer": 0,
                "hint": "Volume of a cube = side × side × side = n³!",
                "explanation": "4³ = 64 unit cubes; (3n)³ = 27n³ gives 27× volume scaling."
            },
            {
                "question": "Compute the exact cube of decimal 0.3 and fraction 3/5:",
                "options": [
                    "0.3³ = 0.027   and   (3/5)³ = 27/125",
                    "0.3³ = 0.27   and   (3/5)³ = 9/25",
                    "0.3³ = 0.9   and   (3/5)³ = 27/15",
                    "0.3³ = 0.0027   and   (3/5)³ = 27/125"
                ],
                "answer": 0,
                "hint": "3³ = 27; cubing 1 decimal place creates 3 decimal places (0.027)!",
                "explanation": "0.3 × 0.3 × 0.3 = 0.027; (3×3×3)/(5×5×5) = 27/125."
            }
        ]
    },
    {
        "id": 10,
        "title": "Cube Digit Patterns",
        "subtitle": "Section 1.2 Properties: Last Digits (All 0–9 Possible, 2↔8 & 3↔7 Swaps) & Trailing Zero Tripling",
        "speech": (
            "Now compare Perfect Cube properties sharply against Perfect Squares—countless board exam questions test whether students accidentally confuse squares with cubes! "
            "First inspect ALL UNITS DIGITS of cubes from 0³ through 9³: 0³ ends in 0, 1³ ends in 1, 2³ ends in 8, 3³ ends in 7, 4³ ends in 4, 5³ ends in 5, 6³ ends in 6, 7³ ends in 3, 8³ ends in 2, and 9³ ends in 9! Surprise! Unlike squares which banned digits 2, 3, 7, and 8 completely, a perfect CUBE can end in EVERY SINGLE DIGIT from zero through nine! Look closely at the unique 1-to-1 pattern: six digits {0, 1, 4, 5, 6, 9} stay UNCHANGED, while TWO golden pairs SWAP partners cleanly: 2 ↔ 8 and 3 ↔ 7 (notice 2+8=10, 3+7=10)! Also odd cubes stay always odd, and even cubes stay always even! "
            "Second check TRAILING ZEROS carefully! Cubing TRIPLES trailing zeros: 10³ = 1,000 (3 zeros!), 200³ = 8,000,000 (6 zeros!)! So a perfect cube ending in zeros MUST have zeros in MULTIPLES OF THREE (3, 6, 9, ...)! Numbers ending in 2 zeros like 400 or 4 zeros like 80,000 are NEVER perfect cubes!"
        ),
        "checkpoints": [
            {
                "question": "If a natural number ends in 8 (like 18) or ends in 3 (like 23), what exact units digits do their CUBES (18³ and 23³) end in?",
                "options": [
                    "18³ ends in 2,   and   23³ ends in 7   (remember 2 ↔ 8 and 3 ↔ 7 swaps!)",
                    "18³ ends in 4,   and   23³ ends in 9",
                    "18³ ends in 8,   and   23³ ends in 3",
                    "No cube can end in 2 or 7"
                ],
                "answer": 0,
                "hint": "8³ = 512 (ends in 2) and 3³ = 27 (ends in 7)!",
                "explanation": "Units digits of cubes preserve {0,1,4,5,6,9} and swap {2↔8} and {3↔7}."
            },
            {
                "question": "Why is 80,000 NOT a perfect cube even though 8 = 2³?",
                "options": [
                    "Because 80,000 ends in 4 trailing zeros, whereas perfect cubes MUST end in multiples of 3 zeros (3, 6, 9, ...)",
                    "Because cubes cannot end in zero",
                    "Because 8 is not a cube",
                    "Because 80,000 is even"
                ],
                "answer": 0,
                "hint": "Count zeros in 80,000 (4 zeros) — does 3 divide 4?",
                "explanation": "Cubing triples trailing zeros, so valid cube zero counts are strictly multiples of 3 (e.g. 8,000 or 8,000,000)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Ramanujan Taxicab Number",
        "subtitle": "Section 1.2 Story: Hardy-Ramanujan Taxicab Number 1729 = 1³ + 12³ = 9³ + 10³ & Sum of Two Cubes",
        "speech": (
            "Celebrate one of the most inspiring true stories in world mathematics inside Section One Point Two: the famous Hardy-Ramanujan Taxicab Number 1,729! "
            "While Indian mathematical genius Srinivasa Ramanujan lay recovering in a London hospital back in 1918, Cambridge professor G. H. Hardy visited him and remarked casually: 'I rode here in taxi number 1729—a rather dull number, I hope not an unfavorable omen!' Instantly, without pencil, paper, or hesitation, Ramanujan smiled warmly and replied: 'No, Hardy! 1729 is a VERY interesting number! It is the SMALLEST natural number expressible as the sum of two positive cubes in TWO DIFFERENT WAYS!' "
            "Verify Srinivasa Ramanujan's instant mental brilliance cleanly right now! Way One: one cubed plus twelve cubed equals 1 + 1,728 equals exact 1,729! Way Two: nine cubed plus ten cubed equals 729 + 1,000 equals exact 1,729! "
            "Natural numbers expressible cleanly as sums of two positive cubes in two distinct ways are now famously honored worldwide by mathematicians as TAXICAB NUMBERS! Notice the very next smallest Taxicab Number right after 1,729 is 4,104 (since 2³ + 16³ equals 9³ + 15³ equals exact 4,104), celebrated in modern number theory forever as Srinivasa Ramanujan's remarkable discovery!"
        ),
        "checkpoints": [
            {
                "question": "Verify BOTH distinct representations that make 1729 the smallest Hardy–Ramanujan Taxicab Number:",
                "options": [
                    "1³ + 12³   AND   9³ + 10³",
                    "1³ + 10³   AND   8³ + 11³",
                    "2³ + 12³   AND   7³ + 11³",
                    "3³ + 12³   AND   9³ + 10³"
                ],
                "answer": 0,
                "hint": "Calculate 1 + 1728 and 729 + 1000!",
                "explanation": "1³ + 12³ = 1 + 1728 = 1729, and 9³ + 10³ = 729 + 1000 = 1729."
            },
            {
                "question": "Check whether 4,104 is ALSO a Taxicab Number given 2³ + 16³ = 8 + 4096 = 4104 and 9³ + 15³ = 729 + 3375:",
                "options": [
                    "Yes! 729 + 3,375 = 4,104 as well (two distinct ways of summing two positive cubes!)",
                    "No, because 4104 is even",
                    "No, because 9³ + 15³ = 4004",
                    "No, 1729 is the only taxicab number in existence"
                ],
                "answer": 0,
                "hint": "Add 729 + 3,375 directly!",
                "explanation": "2³ + 16³ = 4,104 and 9³ + 15³ = 729 + 3,375 = 4,104 (second smallest Taxicab Number)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Cube Odd Partitions",
        "subtitle": "Section 1.2 Nicomachus Pattern: Consecutive Odd-Number Blocks Summing Cleanly to Cubes (n³)",
        "speech": (
            "Earlier you saw that adding odd numbers ALWAYS starting from 1 built SQUARES! Now watch how grouping CONSECUTIVE ODD NUMBERS into growing sequential blocks builds EVERY PERFECT CUBE cleanly! "
            "Read the breathtaking odd-number staircase row by row: Block One (1 term) equals 1 = ONE CUBED (1³)! Skip into the next TWO consecutive odd numbers for Block Two: 3 + 5 = EIGHT = 2³! Continue onward to the next THREE consecutive odd numbers for Block Three: 7 + 9 + 11 = TWENTY SEVEN = 3³! Next FOUR consecutive odd numbers: 13 + 15 + 17 + 19 = SIXTY FOUR = 4³! Next FIVE consecutive odd numbers: 21 + 23 + 25 + 27 + 29 = ONE HUNDRED TWENTY FIVE = 5³! "
            "Spot TWO crisp predictive rules immediately! First: Block row n ALWAYS adds together EXACTLY n consecutive odd terms to produce n³! Second: Check the middle average of Block n—in Block 3 (7, 9, 11), the middle average equals 9 = 3², and 3 terms × 3² equals 3³! In Block 5 (21 through 29), center is 25 = 5², and 5 terms × 5² equals exact 125 every single time!"
        ),
        "checkpoints": [
            {
                "question": "Which consecutive odd-number block sums cleanly to 4³ = 64?",
                "options": [
                    "13 + 15 + 17 + 19   (4 terms centered at 16 = 4²)",
                    "1 + 3 + 5 + 7",
                    "7 + 9 + 11 + 13",
                    "15 + 17 + 19 + 21"
                ],
                "answer": 0,
                "hint": "Row 3 ends at 11 (7+9+11=27), so Row 4 starts right at the next odd number 13!",
                "explanation": "13 + 15 + 17 + 19 = 64 = 4³."
            },
            {
                "question": "How many consecutive odd numbers are needed in the block that sums to 10³ = 1,000?",
                "options": [
                    "10 consecutive odd numbers   (centered around 10² = 100: 91 + 93 + ... + 109)",
                    "100 consecutive odd numbers",
                    "5 consecutive odd numbers",
                    "20 consecutive odd numbers"
                ],
                "answer": 0,
                "hint": "Block n ALWAYS contains exact n consecutive odd terms summing to n³!",
                "explanation": "For n³ = 10³, exact 10 consecutive odd numbers (91 through 109) sum to 1,000."
            }
        ]
    },
    {
        "id": 13,
        "title": "Cube Root Triplets",
        "subtitle": "Section 1.2 Algorithm: Radical ∛y = x, Grouping Prime Factors into Triplets & Smallest Multiplier/Divisor",
        "speech": (
            "Now unlock the inverse of cubing: extracting CUBE ROOTS inside Section One Point Two! If x³ equals y, then x is the CUBE ROOT of y, written clearly with radical index three: ∛y = x! Example: since 5³ = 125, we write ∛125 = 5; since 12³ = 1,728, we write ∛1,728 = 12! Notice even negative integers have real cube roots like (−2)³ = −8, though Class Eight focuses primarily on positive integers! "
            "How do we compute exact cube roots reliably? Replace prime factor PAIRS cleanly with PRIME FACTOR TRIPLETS (groups of three identical primes)! "
            "Test 3,375 immediately! Prime factorize cleanly: 3,375 = (3 × 3 × 3) × (5 × 5 × 5)! Pull ONE prime from each triplet: ∛3,375 = 3 × 5 = FIFTEEN! Test 13,824 = 2⁹ × 3³ = three triplets of 2 and one triplet of 3 ⟹ ∛13,824 = 2 × 2 × 2 × 3 = TWENTY FOUR! "
            "Incomplete Triplet Trap! Check 392 = (2×2×2) × 7 × 7! Notice 7 appears ONLY twice! To complete a triplet, MULTIPLY by 7 (392×7 = 2744 = 14³) OR DIVIDE by 49 (= 7×7, leaving 8 = 2³)!"
        ),
        "checkpoints": [
            {
                "question": "Given prime factorization 1,728 = 2 × 2 × 2 × 2 × 2 × 2 × 3 × 3 × 3, find ∛1,728 by grouping triplets:",
                "options": [
                    "12   (= 2 × 2 × 3)",
                    "6",
                    "24",
                    "18"
                ],
                "answer": 0,
                "hint": "Group into triplets: (2×2×2) × (2×2×2) × (3×3×3), then pick ONE per triplet!",
                "explanation": "∛1728 = 2 × 2 × 3 = 12."
            },
            {
                "question": "Factorize 675 = (3 × 3 × 3) × (5 × 5). Find the SMALLEST natural number to MULTIPLY 675 by, and to DIVIDE 675 by, to yield a perfect cube:",
                "options": [
                    "Multiply by 5 (completes triplet 5³);   Divide by 25 (= 5×5 removes incomplete group!)",
                    "Multiply by 25;   Divide by 5",
                    "Multiply by 3;   Divide by 9",
                    "Already a perfect cube"
                ],
                "answer": 0,
                "hint": "Look carefully: (5 × 5) needs ONE more 5 to multiply into 5³, OR dividing by BOTH 5s (= 25) leaves pure 3³!",
                "explanation": "675 × 5 = 3,375 (15³); 675 ÷ 25 = 27 (3³) — always notice multiplier ≠ divisor for cubes!"
            }
        ]
    },
    {
        "id": 14,
        "title": "Successive Differences Law",
        "subtitle": "Section 1.2 Discovery: Constant Difference at Level 2 (Squares = 2) vs Level 3 (Cubes = 6)",
        "speech": (
            "Uncover one of the coolest hidden calculus-preview patterns in NCERT Class Eight Section One Point Two: SUCCESSIVE DIFFERENCES! Watch closely what happens when you subtract adjacent terms cleanly level by level! "
            "Test SQUARES first: write down 1, 4, 9, 16, 25, 36! Level One differences (4−1, 9−4, 16−9, 25−16, 36−25) produce 3, 5, 7, 9, 11—pure consecutive odd numbers! Now take Level TWO differences (subtracting consecutive Level One terms): 5−3 = 2, 7−5 = 2, 9−7 = 2, 11−9 = 2! Every single square sequence stabilizes cleanly at CONSTANT TWO right at Level Two! "
            "Now climb up cleanly to CUBES: write down 1, 8, 27, 64, 125, 216! Level One differences give 7, 19, 37, 61, 91! Now take Level Two differences carefully: 19 minus 7 = 12, 37 minus 19 = 18, 61 minus 37 = 24, 91 minus 61 = 30 (rising steadily by six each single step)! Take Level THREE differences: 18−12 = SIX, 24−18 = SIX, 30−24 = SIX! Consecutive integer cubes always stabilize cleanly at CONSTANT SIX right at Level Three (because 3 × 2 × 1 equals 6, whereas squares always stabilize at 2 × 1 equals 2 right at Level Two)!"
        ),
        "checkpoints": [
            {
                "question": "At which level do successive differences stabilize for Perfect Squares vs Perfect Cubes, and to what exact constants?",
                "options": [
                    "Squares stabilize at Level 2 (constant 2);   Cubes stabilize at Level 3 (constant 6)",
                    "Squares stabilize at Level 1 (constant 3);   Cubes at Level 2 (constant 12)",
                    "Both stabilize at Level 2 with constant 4",
                    "Cubes never stabilize"
                ],
                "answer": 0,
                "hint": "Degree 2 squares reach constant 2×1 = 2 at Level 2; Degree 3 cubes reach 3×2×1 = 6 at Level 3!",
                "explanation": "Consecutive squares have constant 2nd difference = 2; consecutive cubes have constant 3rd difference = 6."
            },
            {
                "question": "Given Level-1 cube differences 7, 19, 37, 61, 91 (for 1³..6³), use Level-2 and Level-3 pattern (+6) to predict the NEXT Level-1 jump from 6³ (216) to 7³ (343):",
                "options": [
                    "127   (since Level 2 jumps 30 + 6 = 36, so 91 + 36 = 127, and 216 + 127 = 343!)",
                    "121",
                    "115",
                    "133"
                ],
                "answer": 0,
                "hint": "Level 2 runs 12, 18, 24, 30, next is 36; add 36 to 91!",
                "explanation": "Level 2 next = 30 + 6 = 36; Level 1 next = 91 + 36 = 127; check 216 + 127 = 343 = 7³!"
            }
        ]
    },
    {
        "id": 15,
        "title": "Ancient Square Roots",
        "subtitle": "Section 1.3 History: Babylonian Tablets (1700 BCE), Sanskrit Varga, Ghana, Varga-Mula & Aryabhata",
        "speech": (
            "Step back almost four thousand years into Section One Point Three: A Pinch of History! Why did ancient civilizations care deeply about finding squares, cubes, and roots long before modern calculators existed? "
            "On baked BABYLONIAN CLAY TABLETS dating back around 1700 BCE (such as the famous Yale tablet YBC 7289), scribes already engraved detailed tables of squares, cubes, and astonishingly accurate values of √2 to measure temple diagonal beams and rectangular land plots! "
            "Meanwhile in classical Indian mathematics, legendary Indian scholars including ARYABHATA (499 CE) and BRAHMAGUPTA (628 CE) gave us vivid Sanskrit terminology still embedded deeply inside our modern Indian mathematical vocabulary today! They named a square VARGA (meaning both 'a flat four-sided geometric square' AND 'a grid troop arranged in equal rows and columns'), and named a solid cube GHANA (meaning a 'solid 3D cubical block' or 'volume')! "
            "Look closely at their poetic Sanskrit root word: MULA—literally meaning a LIVING PLANT ROOT anchoring a tall banyan tree deeply down inside soil and earth! Thus square root naturally became VARGA-MULA (meaning the foundational side length growing the square) and cube root naturally became GHANA-MULA (meaning the foundational edge length growing the solid cube seamlessly)!"
        ),
        "checkpoints": [
            {
                "question": "In ancient Sanskrit mathematical texts (by Aryabhata & Brahmagupta), what do the terms Varga, Ghana, Varga-mula, and Ghana-mula mean?",
                "options": [
                    "Varga = Square, Ghana = Cube, Varga-mula = Square Root, Ghana-mula = Cube Root (mula = plant root/origin)",
                    "Varga = Triangle, Ghana = Circle, Mula = Diagonal",
                    "Varga = Cube, Ghana = Square, Mula = Area",
                    "Terms invented purely in 20th century Europe"
                ],
                "answer": 0,
                "hint": "Mula means root/foundation; Varga is 2D square rows, Ghana is 3D solid volume!",
                "explanation": "Ancient Indian scholars named square = Varga, cube = Ghana, square root = Varga-mula, cube root = Ghana-mula."
            },
            {
                "question": "How far back do the earliest surviving clay tablets displaying tables of squares, cubes, and √2 approximations trace?",
                "options": [
                    "Babylonian clay tablets around 1700 BCE",
                    "1900 CE",
                    "500 CE",
                    "1200 CE"
                ],
                "answer": 0,
                "hint": "Recall Mesopotamia / Babylonia around 1700 BCE!",
                "explanation": "Babylonian clay tablets from around 1700 BCE already tabulated squares, cubes, and accurate √2 estimates."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter One Summary",
        "subtitle": "Chapter Recap & Puzzle Time: Square Pairs Ordering (1 to 15 Adjacent Sums = Perfect Squares!)",
        "speech": (
            "Congratulations on conquering NCERT Class Eight Chapter One: A Square and A Cube! Lock in ALL core takeaways before tackling forty Quiz Questions and the famous SQUARE PAIRS challenge! "
            "Summary Card: One, Squares n² = n × n end ONLY in {0, 1, 4, 5, 6, 9} (never 2, 3, 7, 8), carry EVEN trailing zeros, equal sums of first n odd numbers, and equal consecutive triangular sums Tₙ₋₁ + Tₙ! Two, Square Roots (√x) group prime factors in PAIRS! Three, Cubes n³ = n × n × n can end in ANY digit 0–9 (with 2↔8 and 3↔7 swaps), carry zeros strictly in MULTIPLES OF THREE, sum consecutive odd blocks cleanly, include Taxicab 1729, and extract Cube Roots (∛x) via TRIPLETS! "
            "Now solve IT'S PUZZLE TIME—Square Pairs! Can you arrange all natural numbers 1 through 15 cleanly in ONE single horizontal sequence so EVERY two adjacent neighbors sum together to form a perfect square? Key insight: 8 and 9 each hold ONLY ONE distinct square partner inside 1..15 (since 8 + 1 = 9 and 9 + 7 = 16), forcing numbers 8 and 9 onto the two outer ends to chain all fifteen numbers cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In the 'Square Pairs' puzzle arranging integers 1 to 15 so adjacent pairs sum to a perfect square, why must 8 and 9 sit at the ENDS (endpoints) of the chain?",
                "options": [
                    "Each of 8 and 9 has ONLY ONE valid partner in {1..15} to sum to a square (8 + 1 = 9 = 3², and 9 + 7 = 16 = 4²; notice 8+8=16 repeats 8!)",
                    "Because 8 and 9 are prime numbers",
                    "Because 8 + 9 = 17 is a square",
                    "Because odd numbers cannot touch even numbers"
                ],
                "answer": 0,
                "hint": "Check what distinct integers in 1..15 add with 8 to give 4, 9, 16, or 25 (25−8 = 17 > 15!)!",
                "explanation": "Without repeating numbers, 8 pairs ONLY with 1 (=9), and 9 pairs ONLY with 7 (=16), forcing 8 and 9 to be chain endpoints!"
            },
            {
                "question": "Which summary comparison between Perfect Squares and Perfect Cubes is 100% accurate?",
                "options": [
                    "Squares use even trailing zeros, prime pairs (√), and never end in {2,3,7,8}; Cubes use multiples of 3 zeros, prime triplets (∛), and can end in any digit 0–9",
                    "Both squares and cubes ban ending digits 2, 3, 7, 8",
                    "Both squares and cubes require prime pairs",
                    "Squares have constant 3rd differences while cubes have constant 2nd differences"
                ],
                "answer": 0,
                "hint": "Contrast zero rules (even vs 3k), prime grouping (pairs vs triplets), and allowed endings!",
                "explanation": "Option 1 accurately summarizes every Section 1.1 and 1.2 law."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch1 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

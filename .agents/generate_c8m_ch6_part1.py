#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 6: We Distribute, Yet Things Multiply
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 6 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Letters And Distribution",
        "subtitle": "Introduction & 6.1: Algebra Letters for General Proofs & Rectangular Dot Arrays a(b + c) = ab + ac",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Six: We Distribute, Yet Things Multiply! Why does modern algebra replace concrete numbers with letter symbols like a, b, and c? Because checking separate arithmetic examples one by one never proves a general rule forever—whereas ONE crisp algebraic sentence captures INFINITELY MANY numerical facts at once! "
            "Master the foundational engine of this entire chapter inside Section Six Point One: THE DISTRIBUTIVE PROPERTY OF MULTIPLICATION OVER ADDITION! Suppose a gardener plants a rectangular orchard grid array having 'a' horizontal rows, divided cleanly into 'b' mango tree columns on the left plus 'c' guava tree columns on the right! "
            "Count total trees in TWO completely equivalent ways! Method One computes combined horizontal width first: a rows times (b + c) columns = a(b + c)! Method Two counts the left mango block (a × b) and adds the right guava block (a × c) = ab + ac! Both geometric methods count the EXACT SAME rectangular dot array, proving universally: a(b + c) ALWAYS equals ab + ac! Even subtraction follows identically by treating minus terms as added negative numbers: a(b − c) equals ab − ac cleanly across all real numbers!"
        ),
        "checkpoints": [
            {
                "question": "How does a rectangular dot array of 'a' rows split vertically into 'b' columns and 'c' columns prove the Distributive Property a(b + c) = ab + ac?",
                "options": [
                    "Total area a × (b + c) equals the sum of left block (ab) plus right block (ac) covering the exact same array!",
                    "Adding (a + b) equals multiplying (b × c)",
                    "Only works when a = b = c",
                    "Multiplying a × b automatically erases c"
                ],
                "answer": 0,
                "hint": "Compare counting the full rectangle as ONE grid vs TWO side-by-side sub-grids!",
                "explanation": "Counting the undivided array a(b + c) matches the combined left grid (ab) and right grid (ac) identically."
            },
            {
                "question": "Evaluate 18 × 104 mentally in one line using the Distributive Property a(b + c) = ab + ac:",
                "options": [
                    "1,872   [= 18 × (100 + 4) = 1800 + 72]",
                    "1,804",
                    "1,972",
                    "2,172"
                ],
                "answer": 0,
                "hint": "Split 104 neatly into 100 + 4 and multiply 18 across BOTH terms!",
                "explanation": "18(100 + 4) = 18×100 + 18×4 = 1800 + 72 = 1,872."
            }
        ]
    },
    {
        "id": 2,
        "title": "Increments In Products",
        "subtitle": "Section 6.1 Increments: Single (+1), Dual (+1, +1 → a+b+1) & Opposing (+1, −1 → b−a−1) Changes",
        "speech": (
            "Now investigate Section Six Point One's clever 'Increments in Products' question: how exact does product a × b change whenever we nudge one OR both factors up or down by one? "
            "Test Single-Variable Increments first! Add one to factor b: a × (b + 1) distributes cleanly into ab + a—showing the product increases by exact 'a'! Conversely, add one to factor a: (a + 1) × b distributes cleanly into ab + b—increasing by exact 'b'! Never guess whether it grows by 'a' or 'b'—distribution tells instantly! "
            "Next nudge BOTH factors up by one: (a + 1)(b + 1)! Watch rectangle width widen by 1 strip (adding area b), height rise by 1 strip (adding area a), PLUS one tiny 1 × 1 corner tile (+1)! Total formula: (a + 1)(b + 1) equals ab + a + b + 1—growing cleanly by (a + b + 1)! "
            "Finally compare OPPOSING single-unit nudges cleanly: (a + 1)(b − 1)! Expand carefully term by term: ab − a + b − 1—so the exact net product change equals (b − a − 1)! Check cleanly: whenever b exceeds (a + 1), total product GROWS larger; whenever b ≤ (a + 1), product drops or stays equal!"
        ),
        "checkpoints": [
            {
                "question": "By exactly how much does product (a × b) increase when BOTH factors increase by 1 to (a + 1)(b + 1)?",
                "options": [
                    "Increases by (a + b + 1)   [since (a+1)(b+1) = ab + a + b + 1]",
                    "Increases by 1 only",
                    "Increases by (a + b) without +1",
                    "Increases by ab"
                ],
                "answer": 0,
                "hint": "Think geometrically: add a top strip (b), a side strip (a), PLUS the missing 1×1 corner!",
                "explanation": "(a + 1)(b + 1) = ab + a + b + 1, increasing the original product ab by exactly a + b + 1."
            },
            {
                "question": "Compute (25 + 1)(19 − 1) compared with 25 × 19 (= 475) using the opposing-increment formula (a+1)(b−1) = ab + b − a − 1:",
                "options": [
                    "468   [change = 19 − 25 − 1 = −7;   475 − 7 = 468]",
                    "475",
                    "482",
                    "469"
                ],
                "answer": 0,
                "hint": "Set a = 25 and b = 19 inside change (b − a − 1) = 19 − 25 − 1 = −7!",
                "explanation": "26 × 18 = 468 = 475 + 19 − 25 − 1 = 475 − 7."
            }
        ]
    },
    {
        "id": 3,
        "title": "Identity One Proofs",
        "subtitle": "Section 6.1 Identities vs Equations & Identity 1 Rectangular Grid: (a+m)(b+n) = ab + mb + an + mn",
        "speech": (
            "Learn one crucial distinction inside Section Six Point One right away: EQUATION versus IDENTITY! Equation x + 5 = 12 holds true ONLY for one solution x = 7! By contrast, an ALGEBRAIC IDENTITY states an equality between two expressions that stays 100 PERCENT TRUE FOR EVERY SINGLE NUMBER assigned to its letters! "
            "Behold IDENTITY ONE—the universal parent law of ALL polynomial multiplication: (a + m)(b + n) ALWAYS equals ab + mb + an + mn! Why? Picture dividing ONE giant floor rectangle of width (a + m) and height (b + n) cleanly into FOUR smaller floor tiles! "
            "Read all four tile areas carefully! Top-left tile: a rows × b columns = ab! Top-right tile: a rows × n columns = an! Bottom-left tile: m rows × b columns = mb! Bottom-right tile: m rows × n columns = mn! Summing all four non-overlapping rectangular regions gives: ab + an + mb + mn! Algebraically, EVERY single term inside the first bracket multiplies EVERY single term inside the second bracket cleanly with zero skipped cross-pairs—check quickly on mental arithmetic too: (10 + 3)(20 + 4) = 200 + 40 + 60 + 12 = 312 effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "What sets an algebraic IDENTITY cleanly apart from a conditional equation?",
                "options": [
                    "An identity holds TRUE for ALL numerical values substituted for its letter-variables, whereas an equation holds only for specific solutions!",
                    "An identity contains no equals sign",
                    "An equation holds for every number while an identity has only 1 solution",
                    "Identities never allow negative numbers"
                ],
                "answer": 0,
                "hint": "Compare (a+1)b = ab + b (true for ALL a, b!) against x + 2 = 9 (true ONLY for x = 7)!",
                "explanation": "Identities express universal structural equivalence true across all values."
            },
            {
                "question": "Expand (3x + 4)(2y + 5) completely using Identity 1: (a + m)(b + n) = ab + an + mb + mn:",
                "options": [
                    "6xy + 15x + 8y + 20",
                    "6xy + 20",
                    "5xy + 15x + 8y + 9",
                    "6xy + 8x + 15y + 20"
                ],
                "answer": 0,
                "hint": "Compute all four pairs: (3x)(2y), (3x)(5), (4)(2y), and (4)(5)!",
                "explanation": "3x(2y) + 3x(5) + 4(2y) + 4(5) = 6xy + 15x + 8y + 20."
            }
        ]
    },
    {
        "id": 4,
        "title": "Negative Binomial Adjustments",
        "subtitle": "Section 6.1 Negative Terms: (a+u)(b−v), (a−u)(b+v) & (a−u)(b−v) Sign Distribution Rules",
        "speech": (
            "Now extend Identity One cleanly to handle SUBTRACTION WITHOUT memorizing separate confusing tables inside Section Six Point One! How? Rewrite EVERY subtraction sign neatly as ADDING A NEGATIVE TERM—for example treating (b − v) identically as (b + (−v))—and apply integer sign multiplication laws: (+ × − = −) and (− × − = +)! "
            "Test ALL THREE signed combinations step by step right now! Case One, (a + u)(b − v): multiply a by b (+ab), a by (−v) (−av), u by b (+ub), and u by (−v) (−uv), giving exact result: ab + ub − av − uv! "
            "Case Two, (a − u)(b + v): multiply a across (+ab + av) and (−u) across (−ub − uv), yielding ab − ub + av − uv! "
            "Case Three—watch BOTH negative integers carefully in (a − u)(b − v)! Multiply negative (−u) × negative (−v) to earn PLUS (+uv), giving exact result: ab − ub − av + uv! Verify instantly with quick mental arithmetic: 18 × 17 = (20 − 2)(20 − 3) = 400 − 40 − 60 + 6 = 306—notice how restoring +6 fixes subtracting two overlapping edge strips neatly every single time!"
        ),
        "checkpoints": [
            {
                "question": "Expand (a − u)(b − v) accurately, watching the product of BOTH negative terms (−u) and (−v):",
                "options": [
                    "ab − ub − av + uv",
                    "ab − ub − av − uv",
                    "ab + ub − av − uv",
                    "ab − uv"
                ],
                "answer": 0,
                "hint": "Remember negative × negative = POSITIVE: (−u) × (−v) = +uv!",
                "explanation": "a(b) + a(−v) + (−u)(b) + (−u)(−v) = ab − av − ub + uv."
            },
            {
                "question": "Use negative distribution (20 − 3)(30 + 2) to evaluate 17 × 32 cleanly:",
                "options": [
                    "544   [= 600 + 40 − 90 − 6]",
                    "556   [= 600 + 40 − 90 + 6]",
                    "534",
                    "634"
                ],
                "answer": 0,
                "hint": "Compute 20×30 (+600), 20×2 (+40), (−3)×30 (−90), and (−3)×2 (−6)!",
                "explanation": "600 + 40 − 90 − 6 = 544."
            }
        ]
    },
    {
        "id": 5,
        "title": "Polynomial Distribution Proofs",
        "subtitle": "Section 6.1 Multi-Term Expansions (a+b)(a²+2ab+b²) & Brahmagupta's Khaṇḍa-Guṇanam (Verse 12.55)",
        "speech": (
            "Scale up cleanly from simple two-term binomials straight onto MULTI-TERM POLYNOMIAL EXPANSIONS inside Section Six Point One, and discover ancient India's remarkable historical mastery of algebraic distribution across centuries! "
            "Expand cubic product (a + b)(a² + 2ab + b²) cleanly step by step without dropping a single intermediate term! First multiply leading factor 'a' across ALL THREE second-bracket terms: a³ + 2a²b + ab²! Next multiply trailing factor '+b' across ALL THREE identical terms: +a²b + 2ab² + b³! Now carefully combine LIKE TERMS sharing identical letter-power signatures: 2a²b + a²b = 3a²b, and ab² + 2ab² = 3ab²—revealing the famous cubic expansion identity: a³ + 3a²b + 3ab² + b³! Also test constant-product increment conditions cleanly whenever balanced shifts keep (a + m)(b − n) completely equal to original ab! "
            "Celebrate A Pinch of History right here too: over fourteen centuries before modern algebraic letter symbols x and y were invented, classical Greek geometer Euclid and great Indian mathematician-astronomer Āryabhaṭa applied geometric distribution implicitly across mathematical proofs, and in 628 Common Era BRAHMAGUPTA explicitly formulated KHAṆḌA-GUṆANAM ('multiplication by breaking into convenient integer parts') in Verse 12.55 of Brahmasphuṭasiddhānta alongside ultra-fast IṢṬA-GUṆANA arithmetic calculation algorithms!"
        ),
        "checkpoints": [
            {
                "question": "Combine like terms cleanly after distributing (a + b)(a² + 2ab + b²):",
                "options": [
                    "a³ + 3a²b + 3ab² + b³",
                    "a³ + 2a²b + 2ab² + b³",
                    "a³ + b³",
                    "a³ + 3ab + b³"
                ],
                "answer": 0,
                "hint": "Add matching a²b terms (2a²b + 1a²b) and matching ab² terms (1ab² + 2ab²)!",
                "explanation": "(a³ + 2a²b + ab²) + (a²b + 2ab² + b³) = a³ + 3a²b + 3ab² + b³."
            },
            {
                "question": "Which classical Indian mathematician explicitly defined khaṇḍa-guṇanam ('multiplication by parts') in Brahmasphuṭasiddhānta (Verse 12.55)?",
                "options": [
                    "Brahmagupta (628 CE)",
                    "Fibonacci (1202 CE)",
                    "Descartes (1637 CE)",
                    "Hammurabi"
                ],
                "answer": 0,
                "hint": "Notice the treatise title Brahmasphuṭasiddhānta (Verse 12.55)!",
                "explanation": "Brahmagupta formulated khaṇḍa-guṇanam in Brahmasphuṭasiddhānta Verse 12.55, laying foundations for distributive mental arithmetic."
            }
        ]
    },
    {
        "id": 6,
        "title": "Fast Multiplication Shortcuts",
        "subtitle": "Section 6.1 Mental Tricks: ×11, ×101, ×99, ×999 via Distribution & Iṣṭa-Guṇana Heritage",
        "speech": (
            "Turn distributive algebra directly into blazing human mental calculator speed inside Section Six Point One: FAST MULTIPLICATIONS USING THE DISTRIBUTIVE PROPERTY! Historically celebrated as IṢṬA-GUṆANA by Indian masters Brahmagupta, Śrīdharācārya, and Bhāskarācārya inside Līlāvatī, breaking tough multipliers cleanly near convenient round powers of ten turns giant manual products into instant one-line mental addition or subtraction! "
            "Trick One, Multiplying cleanly by 11: expand dcba × 11 directly as dcba × (10 + 1) = dcba0 + dcba! Look what happens to adjacent digits instantaneously: copy units digit 'a', add neighboring digit pairs (a + b), (b + c), (c + d), carry tens smoothly leftward, and finish with top digit d! Test 432 × 11 right now: units 2, 2+3=5, 3+4=7, top 4 → exact 4,752 in two seconds! "
            "Trick Two, Multiplying by 101 or 1001: expand dcba × 101 = dcba00 + dcba—shifting TWO decimal places cleanly! Test 34 × 101 = 3,434 effortlessly! "
            "Trick Three, Multiplying by 99 or 999: apply SUBTRACTION distribution! N × 99 equals N × (100 − 1) = N00 − N, and N × 999 = N000 − N! Test 64 × 99 = 6,400 − 64 = 6,336 instantly without paper!"
        ),
        "checkpoints": [
            {
                "question": "Compute 58 × 99 mentally using subtractive distribution N × (100 − 1) = N00 − N:",
                "options": [
                    "5,742   [= 5,800 − 58]",
                    "5,858",
                    "5,752",
                    "5,642"
                ],
                "answer": 0,
                "hint": "Calculate 58 × 100 = 5,800, then subtract 58 cleanly!",
                "explanation": "58 × (100 − 1) = 5,800 − 58 = 5,742."
            },
            {
                "question": "Compute 2,314 × 11 AND 76 × 101 cleanly using additive powers-of-10 distribution:",
                "options": [
                    "25,454   and   7,676",
                    "23,454   and   7,606",
                    "25,354   and   7,776",
                    "24,454   and   7,676"
                ],
                "answer": 0,
                "hint": "23140 + 2314 = 25,454; and 7600 + 76 = 7,676!",
                "explanation": "2314(10+1) = 23140 + 2314 = 25,454; 76(100+1) = 7600 + 76 = 7,676."
            }
        ]
    },
    {
        "id": 7,
        "title": "Square Of Sum",
        "subtitle": "Section 6.2 Identity 1A: (a + b)² = a² + 2ab + b² Algebraic Proof & 4-Region Square Dissection",
        "speech": (
            "Enter Section Six Point Two: Special Cases of the Distributive Property! Meet the most famous identity in all of school algebra—IDENTITY 1A, THE SQUARE OF A SUM: (a + b)² ALWAYS equals a² + 2ab + b²! Never fall for the trap of skipping the middle 2ab term! "
            "Prove Identity 1A BOTH algebraically AND geometrically so you see WHY 2ab MUST exist! Algebraically: set m = b and n = b inside Identity One: (a + b)(a + b) = a² + ab + ba + b²! Combining BOTH identical middle rectangles (ab + ab = 2ab) immediately locks in: (a + b)² = a² + 2ab + b²! "
            "See WHY geometrically inside ONE giant square of side length (a + b)! Slice cleanly horizontally and vertically at split points a and b into FOUR colored rectangular regions: one large corner square of area a²; one smaller corner square of area b²; AND TWO congruent rectangular side strips EACH measuring exact area a × b! Total geometric area sums cleanly: a² + 2ab + b²! Verify rapidly on 105² mentally right now: (100 + 5)² = 10,000 + 2(500) + 25 = 11,025 in one single blink!"
        ),
        "checkpoints": [
            {
                "question": "In the geometric square dissection of side (a + b), what four sub-regions sum to prove (a + b)² = a² + 2ab + b²?",
                "options": [
                    "One square of area a², one square of area b², and TWO congruent rectangles of area ab each!",
                    "Two squares a² and b² ONLY",
                    "Four squares of area ab each",
                    "One square a² minus one square b²"
                ],
                "answer": 0,
                "hint": "Missing those two side rectangles ab creates the classic error (a+b)² = a²+b²!",
                "explanation": "Area(a+b)² = a² + ab + ab + b² = a² + 2ab + b²."
            },
            {
                "question": "Compute 53² cleanly using Identity 1A: (50 + 3)²:",
                "options": [
                    "2,809   [= 2,500 + 300 + 9]",
                    "2,509",
                    "2,659",
                    "2,806"
                ],
                "answer": 0,
                "hint": "Remember middle term 2ab = 2 × 50 × 3 = 300!",
                "explanation": "50² + 2(50)(3) + 3² = 2,500 + 300 + 9 = 2,809."
            }
        ]
    },
    {
        "id": 8,
        "title": "Square Of Difference",
        "subtitle": "Section 6.2 Identity 1B: (a − b)² = a² − 2ab + b² Algebraic Proof & Corner Strip Restoration",
        "speech": (
            "Now conquer IDENTITY 1B inside Section Six Point Two: THE SQUARE OF A DIFFERENCE—(a − b)² ALWAYS equals a² − 2ab + b²! Wait: why does the final b² carry a PLUS SIGN (+b²) instead of minus (−b²)? Both algebra AND geometry explain this crystal clearly! "
            "Algebraically distribute (a − b)(a − b): multiply a × a (+a²), a × (−b) (−ab), (−b) × a (−ab), and negative times negative (−b) × (−b) = PLUS b²! Combining (−ab) + (−ab) = −2ab yields cleanly: (a − b)² = a² − 2ab + b²! "
            "Now see WHY visually on a complete square of side length 'a' (total area a²)! To shrink side length cleanly from 'a' down to (a − b), slice off ONE right-side vertical strip of area (a × b) AND ONE bottom horizontal strip of area (a × b)! Look right at the bottom-right b × b corner square: you accidentally subtracted that small overlapping b² corner TWICE—once inside each rectangular strip! Adding ONE b² back (+b²) restores the exact leftover interior square area (a − b)² cleanly! Test 98² = (100 − 2)² = 10,000 − 400 + 4 = 9,604 effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "Geometrically, why does the formula (a − b)² = a² − 2ab + b² END with (+b²) when starting from square a² and removing two strips of area ab?",
                "options": [
                    "Because removing two perpendicular strips of area (a × b) doubly subtracts the overlapping corner square (b²), so we must ADD (+b²) once back!",
                    "Because (−b) times (+a) is positive",
                    "Because strips have area 2b²",
                    "Because b² is added to make a larger square"
                ],
                "answer": 0,
                "hint": "Count how many times the b × b bottom-right overlap gets removed when cutting BOTH vertical and horizontal strips of width b!",
                "explanation": "Removing two full a×b strips cuts the overlapping corner b² twice; restoring +b² leaves exact area (a − b)²."
            },
            {
                "question": "Calculate 97² cleanly using Identity 1B: (100 − 3)²:",
                "options": [
                    "9,409   [= 10,000 − 600 + 9]",
                    "9,391   [= 10,000 − 600 − 9]",
                    "9,991",
                    "9,709"
                ],
                "answer": 0,
                "hint": "Check signs carefully: a² − 2ab + b² = 100² − 2(100)(3) + 3²!",
                "explanation": "10,000 − 600 + 9 = 9,409."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch6 Class 8 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

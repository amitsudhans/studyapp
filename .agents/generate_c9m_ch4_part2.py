#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 4: Exploring Algebraic Identities
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 4.5 to 4.8, Exercises & Summary with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Splitting Linear Coefficients",
        "subtitle": "Sections 4.5 & 4.6: Connecting Tile Arrays to Algebraic Middle-Term Splitting x² + (a + b)x + ab",
        "speech": (
            "Now bridge hands-on Algebra Tiles straight into lightning-fast algebraic factoring in Sections Four Point Five and Four Point Six! "
            "Notice what happened inside our rectangle tile puzzle: arranging seven x-bars into three columns plus four rows visually executed COEFFICIENT SPLITTING! Even without physical tiles on an exam sheet, we replicate that exact geometry purely algebraically using identity x squared plus open a plus b close x plus a b equals open x plus a close times open x plus b close! "
            "Look carefully at BOTH targets you must hunt simultaneously when factoring x squared plus B x plus C! "
            "Step One: find two integer numbers a and b whose MULTIPLIED PRODUCT equals constant C (a times b equals C)! "
            "Step Two: check whose ADDED SUM equals middle linear coefficient B (a plus b equals B)! "
            "Try factoring x squared plus eleven x plus twenty-four! List factor pairs multiplying to twenty-four: one times twenty-four adds to twenty-five; two times twelve adds to fourteen; THREE times EIGHT adds cleanly to ELEVEN! "
            "Rewrite eleven x cleanly split as three x plus eight x, group pairs to pull out common factors x and eight, revealing crisp factored form open x plus three close times open x plus eight close!"
        ),
        "checkpoints": [
            {
                "question": "To factorize x² + 11x + 24 using middle-term splitting, which pair of numbers (a, b) satisfies a + b = 11 and ab = 24?",
                "options": [
                    "3 and 8",
                    "4 and 6",
                    "2 and 12",
                    "1 and 24"
                ],
                "answer": 0,
                "hint": "Check both sum = 11 AND product = 24!",
                "explanation": "3 × 8 = 24 and 3 + 8 = 11, so x² + 11x + 24 = x² + 3x + 8x + 24 = (x + 3)(x + 8)."
            },
            {
                "question": "How does splitting the middle term 9x in x² + 9x + 14 algebraically mirror Algebra Tiles?",
                "options": [
                    "Splitting 9x into 2x + 7x arranges 2 vertical x-tiles and 7 horizontal x-tiles to lock a 2 × 7 = 14 unit corner",
                    "Deleting the 9x term leaves x² + 14",
                    "Adding 9 and 14 creates 23x",
                    "Splitting x² into 9 pieces"
                ],
                "answer": 0,
                "hint": "Find a + b = 9 and ab = 14!",
                "explanation": "Since 2 + 7 = 9 and 2 × 7 = 14, splitting 9x → 2x + 7x directly matches tile dimensions (x + 2) and (x + 7)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Signed Middle Splitting",
        "subtitle": "Section 4.6 Factorisation Without Tiles: Handling Positive & Negative Coefficients in x² + bx + c",
        "speech": (
            "What if negative signs appear inside quadratic polynomials where wooden tiles can no longer sit positively? Master Section Four Point Six: COEFFICIENT SIGN RULES WITHOUT TILES! "
            "Use pure sign logic on product C equals a times b and sum B equals a plus b—zero guessing needed! "
            "Case One: POSITIVE product C and NEGATIVE sum B, such as x squared minus ten x plus twenty-one! Since product plus twenty-one is positive, BOTH factors must share the SAME sign; negative sum forces BOTH numbers NEGATIVE! Which negative pair sums to minus ten and multiplies to plus twenty-one? Minus three and minus seven! Factor form: open x minus three close times open x minus seven close! "
            "Case Two: NEGATIVE product C, such as x squared plus two x minus fifteen or x squared minus three x minus twenty-eight! Since product is NEGATIVE, one factor MUST be POSITIVE and one MUST be NEGATIVE—meaning their absolute difference equals B, and the LARGER magnitude steals the sign of middle term B! "
            "Test x squared plus two x minus fifteen: factors of fifteen differing by two are five and three; plus two gives plus five and minus three, yielding open x plus five close times open x minus three close!"
        ),
        "checkpoints": [
            {
                "question": "Factorize x² − 10x + 21 completely.",
                "options": [
                    "(x − 3)(x − 7)",
                    "(x + 3)(x + 7)",
                    "(x − 3)(x + 7)",
                    "(x − 21)(x + 1)"
                ],
                "answer": 0,
                "hint": "Positive constant +21 with negative middle −10x requires TWO negative numbers multiplying to +21!",
                "explanation": "(−3) + (−7) = −10 and (−3)(−7) = +21 ⇒ (x − 3)(x − 7)."
            },
            {
                "question": "Factorize x² − 3x − 28 completely.",
                "options": [
                    "(x − 7)(x + 4)",
                    "(x + 7)(x − 4)",
                    "(x − 7)(x − 4)",
                    "(x − 14)(x + 2)"
                ],
                "answer": 0,
                "hint": "Negative constant −28 means opposite signs; middle −3x gives the minus sign to the larger magnitude 7!",
                "explanation": "−7 + 4 = −3 and (−7)(4) = −28 ⇒ (x − 7)(x + 4)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Binomial Cube Volume",
        "subtitle": "Section 4.7 Finding New Identities: Derivation & 8-Solid 3D Decomposition of (a + b)³",
        "speech": (
            "Now leap cleanly from flat two-dimensional squares into full three-dimensional cubes in Section Four Point Seven: FINDING NEW IDENTITIES! "
            "What equals open-parenthesis a plus b close-parenthesis CUBED? Let us derive it BOTH algebraically and geometrically inside a cube of edge length a plus b! "
            "First, algebraic expansion: write open a plus b close cubed as open a plus b close times open a plus b close squared! Substitute a squared plus two a b plus b squared inside, then distribute a and b carefully across all three terms: a cubed plus two a squared b plus a b squared plus a squared b plus two a b squared plus b cubed! "
            "Combining like terms yields our famous CUBIC BINOMIAL IDENTITY: a cubed plus three a squared b plus three a b squared plus b cubed—also written compactly as a cubed plus b cubed plus three a b times open a plus b close! "
            "Now slice a wooden cube of side a plus b along all three coordinate axes! Exactly EIGHT non-overlapping blocks tumble apart: ONE big cube of volume a cubed, ONE small cube of volume b cubed, THREE flat slabs of volume a squared b, and THREE slender bars of volume a b squared!"
        ),
        "checkpoints": [
            {
                "question": "When slicing a solid cube of edge (a + b) along its height, width, and depth, what exact 8 pieces form the total volume?",
                "options": [
                    "Two cubes (volumes a³ and b³) and six cuboids (3 of volume a²b and 3 of volume ab²)",
                    "Only two cubes of volumes a³ and b³",
                    "Eight identical cubes of volume a²b",
                    "Six square tiles and two prisms"
                ],
                "answer": 0,
                "hint": "Expand (a + b)³ = a³ + 3a²b + 3ab² + b³ and count terms: 1 + 3 + 3 + 1 = 8!",
                "explanation": "Decomposing along 3 axes produces 2×2×2 = 8 solids: a³, 3 × (a²b), 3 × (ab²), and b³."
            },
            {
                "question": "Expand (2x + 3)³ cleanly using (a + b)³ = a³ + 3a²b + 3ab² + b³.",
                "options": [
                    "8x³ + 36x² + 54x + 27",
                    "8x³ + 27",
                    "2x³ + 18x² + 27x + 9",
                    "8x³ + 12x² + 18x + 27"
                ],
                "answer": 0,
                "hint": "Take a = 2x and b = 3: note 3a²b = 3(4x²)(3) = 36x² and 3ab² = 3(2x)(9) = 54x!",
                "explanation": "(2x)³ + 3(2x)²(3) + 3(2x)(3)² + 3³ = 8x³ + 36x² + 54x + 27."
            }
        ]
    },
    {
        "id": 12,
        "title": "Difference Cube Expansion",
        "subtitle": "Section 4.7 Derived Cubic Identities: (a − b)³ and Sum/Difference of Cubes Factorisation (x³ ± y³)",
        "speech": (
            "Watch one smart substitution unlock THREE brand-new cubic identities effortlessly in Section Four Point Seven! "
            "First, want open-parenthesis a minus b close-parenthesis cubed without doing painful multiplication again? Simply replace plus b everywhere inside our binomial cube formula with NEGATIVE b! Odd powers keep negative signs while even powers flip positive: open a minus b close cubed equals a cubed MINUS three a squared b PLUS three a b squared MINUS b cubed—or equivalently a cubed minus b cubed minus three a b times open a minus b close! "
            "Now rearrange both cubic expansions cleanly to isolate SUM AND DIFFERENCE OF TWO CUBES! "
            "For x cubed MINUS y cubed: pull out factor open x minus y close, leaving every sign positive inside the companion bracket: open x minus y close times open x squared plus x y plus y squared close! "
            "For x cubed PLUS y cubed: take open x plus y close, placing ONE minus sign on middle term x y: open x plus y close times open x squared MINUS x y plus y squared close! "
            "Factor twenty-seven m cubed minus sixty-four n cubed: open three m minus four n close times open nine m squared plus twelve m n plus sixteen n squared close!"
        ),
        "checkpoints": [
            {
                "question": "Which factored expression accurately equals the difference of cubes identity x³ − y³?",
                "options": [
                    "(x − y)(x² + xy + y²)",
                    "(x − y)(x² − xy + y²)",
                    "(x + y)(x² + xy + y²)",
                    "(x − y)³"
                ],
                "answer": 0,
                "hint": "Check how −x²y and −xy² cancel cleanly when multiplying (x − y) by (x² + xy + y²)!",
                "explanation": "x(x² + xy + y²) − y(x² + xy + y²) = x³ + x²y + xy² − x²y − xy² − y³ = x³ − y³."
            },
            {
                "question": "Factorize 8a³ + 125b³ using the sum of cubes identity x³ + y³ = (x + y)(x² − xy + y²).",
                "options": [
                    "(2a + 5b)(4a² − 10ab + 25b²)",
                    "(2a − 5b)(4a² + 10ab + 25b²)",
                    "(2a + 5b)(4a² + 10ab + 25b²)",
                    "(2a + 5b)³"
                ],
                "answer": 0,
                "hint": "Set x = 2a and y = 5b; notice the middle quadratic term carries −xy!",
                "explanation": "(2a)³ + (5b)³ = (2a + 5b)((2a)² − (2a)(5b) + (5b)²) = (2a + 5b)(4a² − 10ab + 25b²)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Three Variable Cubic",
        "subtitle": "Section 4.7 Master Cubic Identity: x³ + y³ + z³ − 3xyz & Conditional Zero Sum Corollary",
        "speech": (
            "Meet the grand crowning jewel of Section Four Point Seven: the THREE-VARIABLE MASTER CUBIC IDENTITY! "
            "Observe the symmetric polynomial expression x cubed plus y cubed plus z cubed minus three x y z! By grouping cubes cleanly via x cubed plus y cubed and factoring out open x plus y plus z close, this four-term cubic collapses cleanly into two famous factors: open x plus y plus z close MULTIPLIED BY open x squared plus y squared plus z squared minus x y minus y z minus z x close! "
            "Wait—check out TWO extraordinary consequences hiding inside that product! "
            "First, watch what happens whenever the three numbers sum to ZERO: x plus y plus z equals zero! Because the first bracket instantly becomes ZERO, the entire right-hand side vanishes to zero! Moving minus three x y z right proves the stunning conditional shortcut: IF x plus y plus z equals zero, THEN x cubed plus y cubed plus z cubed equals THREE x y z! "
            "Test that shortcut mentally right now! Compute negative twelve cubed plus seven cubed plus five cubed WITHOUT cubing anything! Since negative twelve plus seven plus five equals ZERO, the sum instantly equals three times negative twelve times seven times five equals negative one thousand two hundred sixty!"
        ),
        "checkpoints": [
            {
                "question": "Without computing individual cubes, evaluate (−12)³ + 7³ + 5³ using the conditional 3xyz corollary.",
                "options": [
                    "−1260",
                    "1260",
                    "0",
                    "−420"
                ],
                "answer": 0,
                "hint": "First verify x + y + z = −12 + 7 + 5 = 0, then compute 3xyz!",
                "explanation": "Since −12 + 7 + 5 = 0, (−12)³ + 7³ + 5³ = 3(−12)(7)(5) = −1260."
            },
            {
                "question": "In the master identity x³ + y³ + z³ − 3xyz = (x + y + z)(x² + y² + z² − xy − yz − zx), what happens if x = y = z?",
                "options": [
                    "The second bracket becomes 0, making x³ + y³ + z³ = 3xyz",
                    "The identity becomes undefined",
                    "The first bracket vanishes to 0",
                    "The product equals 9x³"
                ],
                "answer": 0,
                "hint": "Observe x² + y² + z² − xy − yz − zx = ½[(x − y)² + (y − z)² + (z − x)²]!",
                "explanation": "When x = y = z, x² + y² + z² − xy − yz − zx = 3x² − 3x² = 0, so x³ + y³ + z³ − 3xyz = 0."
            }
        ]
    },
    {
        "id": 14,
        "title": "Simplifying Rational Expressions",
        "subtitle": "Section 4.8 Simplifying Rational Expressions: Factoring P(x)/Q(x) & Canceling Non-Zero Common Factors",
        "speech": (
            "Now put every factorization tool you mastered to practical work in Section Four Point Eight: SIMPLIFYING RATIONAL ALGEBRAIC EXPRESSIONS! "
            "A rational algebraic expression writes as P of x divided by Q of x, where numerator P and denominator Q are polynomials and denominator Q does NOT equal zero! "
            "Golden Rule Number One—NEVER cancel individual added or subtracted terms directly! Crossing out x squared from x squared minus nine over x minus three without factoring is a fatal algebraic blunder! "
            "Instead, follow our clean THREE-STEP SIMPLIFICATION PIPELINE! "
            "Step One: completely FACTORIZE both numerator P and denominator Q using difference of squares, perfect squares, cubic identities, or middle-term splitting! For example, factor x squared minus nine over x squared plus seven x plus twelve into open x minus three close open x plus three close OVER open x plus three close open x plus four close! "
            "Step Two: check domain restrictions—exclude variable values making Q zero, here x cannot equal minus three or minus four! "
            "Step Three: safely cancel strictly non-zero common MULTIPLIED brackets like open x plus three close from numerator and denominator, yielding crisp simplified fraction open x minus three close over open x plus four close!"
        ),
        "checkpoints": [
            {
                "question": "Simplify the rational expression (x² − 16) / (x² + 9x + 20) where x ≠ −4, −5.",
                "options": [
                    "(x − 4) / (x + 5)",
                    "(x + 4) / (x + 5)",
                    "−16 / (9x + 20)",
                    "(x − 4) / (x − 5)"
                ],
                "answer": 0,
                "hint": "Factor numerator as (x − 4)(x + 4) and denominator as (x + 4)(x + 5), then cancel (x + 4)!",
                "explanation": "(x² − 16)/(x² + 9x + 20) = [(x − 4)(x + 4)] / [(x + 4)(x + 5)] = (x − 4)/(x + 5) for x ≠ −4, −5."
            },
            {
                "question": "Why is it mathematically invalid to 'cancel x²' directly in (x² − 9) / (x² − 3x) to get −9 / (−3x)?",
                "options": [
                    "Only common multiplied FACTORS can be canceled after complete factorisation, never individual added or subtracted terms",
                    "Because x² is always negative",
                    "Because numerator powers must exceed denominator powers",
                    "Because 9 is not divisible by 3"
                ],
                "answer": 0,
                "hint": "Proper factoring gives [(x − 3)(x + 3)] / [x(x − 3)], canceling (x − 3) instead!",
                "explanation": "Terms joined by + or − are not multiplicative factors. Factoring first reveals the true common factor (x − 3) → (x + 3)/x."
            }
        ]
    },
    {
        "id": 15,
        "title": "Geometry Area Problems",
        "subtitle": "Section 4.8 Real-World Word Problems: Finding Dimensions of Rectangular Pools, Gardens & Land Areas",
        "speech": (
            "See algebraic factorization and rational division solve real-world engineering and land measurement puzzles cleanly in Section Four Point Eight! "
            "Imagine a rectangular community park having total tiled surface area open x squared plus eleven x plus twenty-eight close square metres, and width open x plus four close metres! How do engineers find its unknown length instantly? "
            "Divide total area by known width: open x squared plus eleven x plus twenty-eight close divided by open x plus four close! Factor numerator using middle-term splitting: four plus seven equals eleven and four times seven equals twenty-eight, giving open x plus four close times open x plus seven close! Cancel non-zero factor open x plus four close—revealing exact pool length open x plus seven close metres, and perimeter two times open two x plus eleven close! "
            "Test a rectangular swimming pool upgrade too! Suppose an existing square pool of side x metres loses two metres along one border and gains three metres along the adjacent border, giving modified area x squared plus x minus six! Or compare land plot area x cubed minus twenty-seven divided by width x minus three: cubic identity instantly reveals quadratic land expression x squared plus three x plus nine!"
        ),
        "checkpoints": [
            {
                "question": "A rectangular community swimming pool has floor area (x² + 13x + 36) m² and width (x + 4) m. What are its exact length and perimeter?",
                "options": [
                    "Length = (x + 9) m and Perimeter = (4x + 26) m",
                    "Length = (x + 4) m and Perimeter = (4x + 16) m",
                    "Length = (x + 32) m and Perimeter = (4x + 72) m",
                    "Length = (x − 9) m and Perimeter = (4x − 10) m"
                ],
                "answer": 0,
                "hint": "Factor x² + 13x + 36 with 4 + 9 = 13 and 4 × 9 = 36, then compute 2(Length + Width)!",
                "explanation": "Area / Width = (x + 4)(x + 9)/(x + 4) = (x + 9) m. Perimeter = 2[(x + 9) + (x + 4)] = 2(2x + 13) = 4x + 26 m."
            },
            {
                "question": "A rectangular solar farm plot has area (x³ − 8) m² and side width (x − 2) m (x > 2). Find the expression for its other dimension.",
                "options": [
                    "(x² + 2x + 4) m",
                    "(x² − 2x + 4) m",
                    "(x − 2)² m",
                    "(x² + 4) m"
                ],
                "answer": 0,
                "hint": "Factor x³ − 2³ using the difference of cubes identity!",
                "explanation": "(x³ − 8)/(x − 2) = [(x − 2)(x² + 2x + 4)]/(x − 2) = (x² + 2x + 4) m."
            }
        ]
    },
    {
        "id": 16,
        "title": "Eleven Core Identities",
        "subtitle": "Chapter Summary: Complete Reference of All 11 Core Algebraic Identities, Visualization & Factoring Methods",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your master reference guide uniting ALL ELEVEN CORE ALGEBRAIC IDENTITIES and geometric tools from Chapter Four! "
            "Count through all eleven identities cleanly! Identity One and Two: binomial squares open a plus or minus b close squared equals a squared plus or minus two a b plus b squared! Identity Three: difference of squares a squared minus b squared equals open a plus b close open a minus b close! Identity Four: Śhrīdharāchārya's mental squaring rearrangement a squared equals open a plus b close open a minus b close plus b squared! "
            "Identity Five: general middle-term quadratic open x plus a close open x plus b close equals x squared plus open a plus b close x plus a b! Identity Six: trinomial square open a plus b plus c close squared equals a squared plus b squared plus c squared plus two a b plus two b c plus two c a! "
            "Identities Seven and Eight: binomial cubes open a plus or minus b close cubed! Identities Nine and Ten: sum and difference of cubes x cubed plus or minus y cubed! Identity Eleven: master cubic x cubed plus y cubed plus z cubed minus three x y z! Master tiles, splitting, and rational cancellation—now conquer all four silent mastery quizzes!"
        ),
        "checkpoints": [
            {
                "question": "Which summary pairing accurately matches all signs in BOTH (x³ + y³) and (a − b)³?",
                "options": [
                    "x³ + y³ = (x + y)(x² − xy + y²) AND (a − b)³ = a³ − 3a²b + 3ab² − b³",
                    "x³ + y³ = (x + y)(x² + xy + y²) AND (a − b)³ = a³ − 3a²b − 3ab² − b³",
                    "x³ + y³ = (x − y)(x² + xy + y²) AND (a − b)³ = a³ − b³",
                    "x³ + y³ = (x + y)³ AND (a − b)³ = a³ + 3a²b + 3ab² − b³"
                ],
                "answer": 0,
                "hint": "Keep (−b)² positive so +3ab² stays +, and keep −xy inside (x³ + y³) so cross terms cancel!",
                "explanation": "In (a − b)³, signs alternate +, −, +, −. In x³ + y³, quadratic factor carries −xy to cancel +x²y and −x²y."
            },
            {
                "question": "Which step sequence correctly solves rational simplification (2x² − 18) / (x² + 5x + 6)?",
                "options": [
                    "Factor numerator 2(x − 3)(x + 3) and denominator (x + 2)(x + 3), exclude x ≠ −2, −3, cancel (x + 3) → 2(x − 3)/(x + 2)",
                    "Cancel x² immediately to get −18/(5x + 6)",
                    "Divide 18 by 6 directly to get (2x² − 3)/(x² + 5x)",
                    "Substitute x = −3 to confirm both numerator and denominator vanish"
                ],
                "answer": 0,
                "hint": "Always pull out the GCF (here 2) first before applying a² − b²!",
                "explanation": "Factoring out GCF 2 gives 2(x² − 9) = 2(x − 3)(x + 3); dividing by (x + 2)(x + 3) simplifies cleanly to 2(x − 3)/(x + 2) for x ≠ −2, −3."
            }
        ]
    }
]

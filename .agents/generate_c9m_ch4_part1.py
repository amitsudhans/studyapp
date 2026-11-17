#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 4: Exploring Algebraic Identities
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 4.1 to 4.5 with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Numerical Square Patterns",
        "subtitle": "Section 4.1 Introduction: Consecutive Square Patterns & Role of General Algebraic Rules",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Four: Exploring Algebraic Identities! "
            "Have you ever noticed hidden mathematical magic inside ordinary consecutive whole numbers? Test this striking pattern from Section Four Point One right now! "
            "Pick ANY three consecutive integers—for example four, five, and six! Square all three numbers to get sixteen, twenty-five, and thirty-six. Now add the smallest square and the largest square: sixteen plus thirty-six equals fifty-two. Subtract twice the middle square, which is two times twenty-five equals fifty! What remains? Fifty-two minus fifty equals TWO! "
            "Try nine, ten, and eleven next! Eighty-one plus one hundred twenty-one equals two hundred two. Subtract twice one hundred, giving two hundred two minus two hundred equals TWO again! "
            "Wait—does this miraculous result hold for EVERY trio of consecutive integers up to infinity, or only small test numbers? Checking numbers one by one takes eternity! "
            "Instead, algebra steps forward with universal mathematical superpowers! By representing any three consecutive whole integers generally using single-letter variable expressions n minus one, n, and n plus one, general algebraic identities systematically transform endless numerical arithmetic guesswork into effortless, crystal-clear one-line mathematical certainty universally valid across every single integer, rational fraction, and real number!"
        ),
        "checkpoints": [
            {
                "question": "Pick three consecutive integers 7, 8, and 9. Compute 7² + 9² − 2(8²).",
                "options": [
                    "2",
                    "0",
                    "4",
                    "8"
                ],
                "answer": 0,
                "hint": "Calculate 49 + 81 − 2(64) = 130 − 128!",
                "explanation": "7² + 9² − 2(8²) = 49 + 81 − 128 = 2, obeying (n−1)² + (n+1)² − 2n² = 2."
            },
            {
                "question": "What primary mathematical advantage do algebraic identities offer over numerical trial and error?",
                "options": [
                    "They prove general mathematical rules hold true for infinitely many numbers at once and simplify calculations",
                    "They only check whether a single specific number fits an equation",
                    "They replace negative signs with positive constants",
                    "They forbid using letters in geometry"
                ],
                "answer": 0,
                "hint": "Think why testing n = 5, 10, 100 never proves something for ALL numbers!",
                "explanation": "Algebraic identities establish universal structural rules valid across all real and rational values simultaneously."
            }
        ]
    },
    {
        "id": 2,
        "title": "Binomial Square Model",
        "subtitle": "Section 4.2 Visualising Identities: Geometric Square Model of (a + b)² & Fast Mental Squaring",
        "speech": (
            "Open Section Four Point Two and see algebra turn vividly geometric! Why does open-parenthesis a plus b close-parenthesis squared equal a squared plus two a b plus b squared—and NEVER mistakenly just a squared plus b squared? "
            "Draw a big outer square whose side length equals a plus b! Now slice that side cleanly into two segments: length a and length b, both horizontally and vertically! "
            "Look at the four non-overlapping tiles inside your big square! The top-left corner forms a pure square of side a, holding area a squared! The bottom-right corner forms a smaller square of side b, holding area b squared! "
            "What fills the remaining two L-shaped corners? TWO identical rectangles, each measuring length a by width b—contributing area a b plus a b equals TWO a b! "
            "Summing all four geometric tiles proves visually beyond any doubt that open a plus b close squared equals a squared plus two a b plus b squared! "
            "Watch this unlock lightning-fast mental squaring! Need forty-three squared without pen and paper? Split forty-three into forty plus three: sixteen hundred plus twice forty times three which is two hundred forty plus nine equals one thousand eight hundred forty-nine!"
        ),
        "checkpoints": [
            {
                "question": "In the geometric square model of side (a + b), what four non-overlapping regions partition the total area?",
                "options": [
                    "One square of area a², one square of area b², and two rectangles each of area ab",
                    "Only two squares of areas a² and b²",
                    "Four identical rectangles of area ab",
                    "One cube of volume a³ and three rectangles of area b²"
                ],
                "answer": 0,
                "hint": "Remember why the middle term +2ab never disappears geometrically!",
                "explanation": "Partitioning side (a + b) creates squares a² and b² on the main diagonal plus two off-diagonal rectangles ab."
            },
            {
                "question": "Evaluate 52² mentally using the binomial square identity (50 + 2)² = a² + 2ab + b².",
                "options": [
                    "2704",
                    "2504",
                    "2604",
                    "2700"
                ],
                "answer": 0,
                "hint": "Compute 50² + 2(50)(2) + 2² = 2500 + 200 + 4!",
                "explanation": "(50 + 2)² = 2500 + 200 + 4 = 2704. Notice 2504 misses the crucial 2ab = 200 rectangle term."
            }
        ]
    },
    {
        "id": 3,
        "title": "Equation vs Identity",
        "subtitle": "Section 4.2 Core Distinction: Conditional Equations (x² − 1 = 24) vs Universal Algebraic Identities",
        "speech": (
            "Now master one crucial conceptual distinction in Section Four Point Two that separates sharp algebraists from careless guessers: EQUATION versus ALGEBRAIC IDENTITY! "
            "Look at an algebraic statement with an equals sign, such as x squared minus one equals twenty-four! Test different numbers for x! Plug in x equals zero: minus one does NOT equal twenty-four! Plug in x equals three: eight does NOT equal twenty-four! Plug in x equals five: twenty-five minus one equals twenty-four—TRUE! Plug in x equals minus five: also TRUE! "
            "Because x squared minus one equals twenty-four holds ONLY for specific values x equals plus five and minus five, we call it a CONDITIONAL EQUATION! "
            "Now compare open-parenthesis x plus three close-parenthesis squared equals x squared plus six x plus nine! Plug in x equals zero: nine equals nine! Plug in x equals minus two: one equals one! Plug in one-half, root five, or minus ten: BOTH sides remain identically equal EVERY SINGLE TIME! "
            "An ALGEBRAIC IDENTITY holds true universally across ALL valid real and rational values of its variables—without exception! Unlike conditional equations that wait to be solved for isolated roots, identities serve as trusted structural shortcuts empowering completely safe expression rewriting, fast mental arithmetic, and exact polynomial simplification anywhere in mathematics!"
        ),
        "checkpoints": [
            {
                "question": "Which mathematical statement is an ALGEBRAIC IDENTITY rather than a conditional equation?",
                "options": [
                    "(x + 4)² = x² + 8x + 16",
                    "x² − 1 = 24",
                    "3x + 5 = 17",
                    "x² = 9"
                ],
                "answer": 0,
                "hint": "Check which equality holds identically for x = 0, x = 1, x = −3, and every other real number!",
                "explanation": "(x + 4)² = x² + 8x + 16 is true for all real values of x; the others hold only for isolated roots."
            },
            {
                "question": "Why is x² − 1 = 24 classified strictly as an equation instead of an identity?",
                "options": [
                    "It is satisfied only by specific values x = 5 and x = −5, failing for other numbers like x = 2",
                    "It contains a square term x²",
                    "It contains negative subtraction on the left",
                    "It evaluates to an odd integer when x = 0"
                ],
                "answer": 0,
                "hint": "Test x = 1 in x² − 1 = 24: does 0 equal 24?",
                "explanation": "An identity must hold for all valid values; x² − 1 = 24 holds solely at x = ±5."
            }
        ]
    },
    {
        "id": 4,
        "title": "Perfect Square Factoring",
        "subtitle": "Section 4.3 Factorisation Using Identities: Perfect Squares (a ± b)² & Proof of Consecutive Squares Pattern",
        "speech": (
            "In Section Four Point Three, flip your identity lenses into REVERSE GEAR! Expanding multiplies brackets outward, while FACTORISATION folds long polynomial sums cleanly back into compact multiplied brackets! "
            "Suppose you spot three terms: nine x squared plus twenty-four x plus sixteen! How do we factor it cleanly? Check the outer square anchor terms! Nine x squared equals open three x close squared, and sixteen equals four squared! Now test the middle term against two a b: twice three x times four equals twenty-four x—EXACT MATCH! Immediately factor backward into open three x plus four close whole squared! "
            "Similarly, if the middle term carries a MINUS sign, check a squared minus two a b plus b squared factoring into open a minus b close squared! "
            "Now fulfill our Section Four Point One promise! Prove algebraically why consecutive squares ALWAYS satisfy open n minus one close squared plus open n plus one close squared minus two n squared equals two! "
            "Expand both brackets cleanly: n squared minus two n plus one, PLUS n squared plus two n plus one! Notice minus two n and plus two n cancel cleanly, leaving two n squared plus two! Subtracting two n squared leaves pure invariant TWO!"
        ),
        "checkpoints": [
            {
                "question": "Factorize the perfect-square trinomial 25x² − 30xy + 9y² using algebraic identities.",
                "options": [
                    "(5x − 3y)²",
                    "(5x + 3y)²",
                    "(25x − 9y)²",
                    "(5x − 3y)(5x + 3y)"
                ],
                "answer": 0,
                "hint": "Identify a = 5x, b = 3y, and check the minus middle term −2ab = −2(5x)(3y) = −30xy!",
                "explanation": "25x² − 30xy + 9y² = (5x)² − 2(5x)(3y) + (3y)² = (5x − 3y)²."
            },
            {
                "question": "In the algebraic proof of (n − 1)² + (n + 1)² − 2n² = 2, which terms cancel cleanly during expansion?",
                "options": [
                    "−2n and +2n cancel first, then +2n² and −2n² cancel, leaving 1 + 1 = 2",
                    "n² and 1 cancel completely",
                    "Only the +1 constants cancel",
                    "No terms cancel because consecutive squares grow randomly"
                ],
                "answer": 0,
                "hint": "Write out (n² − 2n + 1) + (n² + 2n + 1) − 2n² term by term!",
                "explanation": "(n² − 2n + 1) + (n² + 2n + 1) − 2n² simplifies to 2n² + 2 − 2n² = 2 for every number n."
            }
        ]
    },
    {
        "id": 5,
        "title": "Difference Square Geometry",
        "subtitle": "Section 4.3 Geometric Model for (a − b)²: Subtracting Areas ab and b(a − b) from Big Square a²",
        "speech": (
            "Now visualize open-parenthesis a minus b close-parenthesis squared geometrically in Section Four Point Three—avoiding the classic student trap of forgetting plus b squared! "
            "Begin with one solid large square of total side length a, giving full initial area a squared! "
            "Inside this big square, mark off a smaller top-left target square whose side length equals a minus b, leaving thin border strips of thickness b along the right side and bottom edge! Our mission: compute the area of that inner target square open a minus b close squared by slicing away borders! "
            "Method One—two clean border cuts! First slice away a full tall right rectangle of width b and full height a: subtracted area equals a b! What leftover bottom border remains below the target square? A shorter horizontal strip of height b and width ONLY a minus b! Subtract that second area b times open a minus b close, equal to a b minus b squared! "
            "Alternatively, think of subtracting BOTH full length-a strips (two a b), then noticing the tiny bottom-right overlap square b squared was subtracted TWICE—so add back plus b squared! Both routes prove visually: open a minus b close squared equals a squared minus two a b plus b squared!"
        ),
        "checkpoints": [
            {
                "question": "When removing two full strips of area ab from square a² to isolate (a − b)², why must we add +b² at the end?",
                "options": [
                    "Because the corner overlap square of area b² belongs to both strips and was subtracted twice",
                    "Because b² must always remain outside the big square",
                    "Because subtracting a − b doubles the perimeter",
                    "To convert a rectangle into a triangle"
                ],
                "answer": 0,
                "hint": "Check where the vertical b × a strip and horizontal a × b strip intersect at the corner!",
                "explanation": "Subtracting two a × b strips removes the intersecting b × b corner twice; adding +b² compensates once, giving a² − 2ab + b²."
            },
            {
                "question": "Compute 98² cleanly using the difference-square identity (100 − 2)² = a² − 2ab + b².",
                "options": [
                    "9604",
                    "9996",
                    "9804",
                    "9600"
                ],
                "answer": 0,
                "hint": "Evaluate 100² − 2(100)(2) + 2² = 10000 − 400 + 4!",
                "explanation": "(100 − 2)² = 10000 − 400 + 4 = 9604."
            }
        ]
    },
    {
        "id": 6,
        "title": "Trinomial Square Grid",
        "subtitle": "Section 4.4 More Identities: Expansion & 3 × 3 Partitioned Grid of (a + b + c)²",
        "speech": (
            "What happens when a square expands from TWO terms inside brackets to THREE terms? Welcome to Section Four Point Four: MORE IDENTITIES, starting with the TRINOMIAL SQUARE open a plus b plus c close whole squared! "
            "Derive it cleanly using BOTH algebraic substitution AND a vibrant three-by-three grid! "
            "Algebraic shortcut: group open a plus b close as one single bundle let u equals a plus b! Then open u plus c close squared expands cleanly using our binomial formula into u squared plus two u c plus c squared! Substitute back u equals a plus b: open a plus b close squared plus two c times open a plus b close plus c squared! "
            "Expanding produces SIX neat terms: three individual squares a squared plus b squared plus c squared, PLUS three doubled cross-products: two a b plus two b c plus two c a! "
            "Verify visually on a square of side a plus b plus c split into three segments along top and left! Nine crisp rectangular regions appear: three pure diagonal squares (a squared, b squared, c squared) flanked by three symmetric pairs of rectangles (two a b, two b c, two c a)—all nine pieces matching algebra!"
        ),
        "checkpoints": [
            {
                "question": "Which expansion accurately equals the trinomial square identity (a + b + c)²?",
                "options": [
                    "a² + b² + c² + 2ab + 2bc + 2ca",
                    "a² + b² + c² + ab + bc + ca",
                    "a² + b² + c²",
                    "a² + b² + c² + 3abc"
                ],
                "answer": 0,
                "hint": "Remember the 3 diagonal squares plus 6 symmetric off-diagonal rectangles (2ab, 2bc, 2ca) in the 3 × 3 grid!",
                "explanation": "(a + b + c)² sums the 3 squares and all 3 doubled pairwise products: a² + b² + c² + 2ab + 2bc + 2ca."
            },
            {
                "question": "Expand (x − 2y + 3z)² cleanly using the trinomial square identity.",
                "options": [
                    "x² + 4y² + 9z² − 4xy − 12yz + 6zx",
                    "x² − 4y² + 9z² − 4xy + 12yz − 6zx",
                    "x² + 4y² + 9z² − 2xy − 6yz + 3zx",
                    "x² + 4y² + 9z²"
                ],
                "answer": 0,
                "hint": "Substitute a = x, b = −2y, c = +3z! Remember (−2y)² = +4y²!",
                "explanation": "x² + (−2y)² + (3z)² + 2(x)(−2y) + 2(−2y)(3z) + 2(3z)(x) = x² + 4y² + 9z² − 4xy − 12yz + 6zx."
            }
        ]
    },
    {
        "id": 7,
        "title": "Sridharacharya Square Method",
        "subtitle": "Section 4.4 Difference of Squares a² − b² = (a + b)(a − b) & Śhrīdharāchārya's 750 CE Mental Squaring Method",
        "speech": (
            "Now inspect one of algebra's fastest calculation powerhouses in Section Four Point Four: DIFFERENCE OF TWO SQUARES and ŚHRĪDHARĀCHĀRYA'S ANCIENT SQUARING SECRET! "
            "Recall identity a squared minus b squared equals open a plus b close times open a minus b close! Why does it work geometrically? Take square a squared, remove corner square b squared, slice off the bottom rectangle, and rotate it cleanly onto the side—forming one sleek rectangle measuring width a plus b by height a minus b! "
            "Now witness how eighth-century Indian mathematician Śhrīdharāchārya around seven hundred fifty CE flipped this exact identity for lightning mental arithmetic! Simply add b squared to BOTH sides: a squared equals open a plus b close times open a minus b close PLUS b squared! "
            "Watch Śhrīdharāchārya square ninety-seven in two seconds! Pick shift b equals three so a plus b leaps to a round hundred! Multiply ninety-seven minus three equals ninety-four times one hundred to get nine thousand four hundred, then add three squared equals nine—instant answer NINE THOUSAND FOUR HUNDRED NINE! "
            "Or square sixty-six cleanly using b equals four: seventy times sixty-two equals four thousand three hundred forty, plus four squared sixteen equals four thousand three hundred fifty-six—instant mental precision!"
        ),
        "checkpoints": [
            {
                "question": "According to Śhrīdharāchārya's identity (750 CE), a² = (a + b)(a − b) + b². How does this compute 96² cleanly with b = 4?",
                "options": [
                    "(100)(92) + 4² = 9200 + 16 = 9216",
                    "(100)(96) + 16 = 9616",
                    "(92)(92) + 16 = 8480",
                    "(100)(92) − 16 = 9184"
                ],
                "answer": 0,
                "hint": "Compute (a + b) = 96 + 4 = 100 and (a − b) = 96 − 4 = 92, then add +b²!",
                "explanation": "96² = (96 + 4)(96 − 4) + 4² = 100 × 92 + 16 = 9216."
            },
            {
                "question": "Evaluate 105 × 95 swiftly using difference of squares (a + b)(a − b) = a² − b².",
                "options": [
                    "9975 (since 100² − 5² = 10000 − 25)",
                    "10025",
                    "9925",
                    "9950"
                ],
                "answer": 0,
                "hint": "Rewrite 105 × 95 as (100 + 5)(100 − 5)!",
                "explanation": "(100 + 5)(100 − 5) = 100² − 5² = 10000 − 25 = 9975."
            }
        ]
    },
    {
        "id": 8,
        "title": "Algebra Tile Rectangles",
        "subtitle": "Section 4.5 Factorisation Using Algebra Tiles: Concrete x², x, and Unit Tiles Forming (x + 3)(x + 4)",
        "speech": (
            "Can abstract quadratic polynomials literally be touched, slid around, and snapped together like jigsaw puzzle pieces? Welcome to Section Four Point Five: FACTORISATION USING ALGEBRA TILES! "
            "Meet three simple building tiles! First, a large square tile measuring x by x has area x squared! Second, a slender rectangular bar measuring x by one has area x! Third, a tiny one-by-one square has area one unit! "
            "Suppose you dump one x-squared tile, SEVEN rectangular x-tiles, and TWELVE tiny unit squares onto your desk—representing polynomial x squared plus seven x plus twelve! "
            "Can you arrange ALL twenty tiles seamlessly into one solid, unbroken rectangle with zero gaps and zero overhanging pieces? "
            "Place the x-squared tile top-left! Now split the seven x-bars into rows and columns around it! Try putting THREE x-bars vertically down the right edge and FOUR x-bars horizontally along the bottom edge! "
            "Check the empty bottom-right corner gap left neatly between them: THREE rows by FOUR columns demands exact space for THREE times FOUR equals TWELVE tiny unit squares! Every tile locks completely tight! Reading both outer rectangle dimensions immediately reveals crisp factored sides open x plus three close times open x plus four close!"
        ),
        "checkpoints": [
            {
                "question": "To arrange x² + 7x + 12 cleanly into an Algebra Tile rectangle, how are the 7 rectangular x-tiles placed along the right and bottom of the x² tile?",
                "options": [
                    "3 x-tiles on one side and 4 x-tiles on the adjacent side (since 3 + 4 = 7 and 3 × 4 = 12 unit tiles fit the corner)",
                    "1 x-tile on one side and 6 x-tiles on the other",
                    "2 x-tiles on one side and 5 x-tiles on the other",
                    "All 7 x-tiles stacked on top of one edge"
                ],
                "answer": 0,
                "hint": "Check which row × column rectangle holds all 12 unit square tiles in the corner!",
                "explanation": "A 3-by-4 array uses 3 + 4 = 7 x-tiles and creates an exact 3 × 4 = 12 unit-tile corner for (x + 3)(x + 4)."
            },
            {
                "question": "Which quadratic polynomial matches an Algebra Tile rectangle formed by 1 x²-tile, 2 x-tiles along top/right, 3 x-tiles along bottom, and 6 unit tiles?",
                "options": [
                    "x² + 5x + 6 = (x + 2)(x + 3)",
                    "x² + 6x + 5 = (x + 1)(x + 6)",
                    "x² + 5x + 5",
                    "x² + 6x + 6"
                ],
                "answer": 0,
                "hint": "Count total x-tiles (2 + 3) and total unit tiles (2 × 3)!",
                "explanation": "Total area = x² + (2 + 3)x + (2×3) = x² + 5x + 6, whose side dimensions are (x + 2) and (x + 3)."
            }
        ]
    }
]

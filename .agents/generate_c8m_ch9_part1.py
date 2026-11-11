#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 9: The Baudhāyana-Pythagoras Theorem
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 9 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Doubling A Square",
        "subtitle": "Section 2.1 Baudhāyana's Śulba-Sūtra Verse 1.9 (c. 800 BCE): Side Scaling vs Diagonal Square Proof",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Nine: The Baudhāyana-Pythagoras Theorem! Open Section Two Point One in ancient India around eight hundred BCE, where Baudhāyana posed a remarkably practical altar construction puzzle in Verse One Point Nine of the Śulba-Sūtra: given any square, how do you construct another square having EXACTLY DOUBLE its area? "
            "Watch carefully for the tempting trap! Many students immediately double the side length from s to 2s! What actually happens to the area? Doubling BOTH length and width multiplies area by 2 × 2 = FOUR times—making a square FOUR times bigger, NOT double! "
            "Now admire Baudhāyana's brilliant geometric solution: build your new square directly on the DIAGONAL of the original square! Prove why immediately using crisp grid lines! Slice one original square diagonally into TWO congruent isosceles right triangles! Next observe the larger tilted square constructed cleanly along that exact diagonal—drawing horizontal and vertical grid divisions reveals that this diagonal square encloses FOUR identical copies of those exact same triangles! Four triangles divided by two triangles equals EXACTLY DOUBLE THE AREA! Try the hands-on paper-cutting activity too: slice two identical squares diagonally into four right triangles and arrange all four hypotenuses outward to seamlessly assemble one double-area square!"
        ),
        "checkpoints": [
            {
                "question": "If you double the side length of a 5 cm × 5 cm square to 10 cm × 10 cm, what happens to its area?",
                "options": [
                    "Area quadruples (2 × 2 = 4 times bigger: 25 sq cm → 100 sq cm)",
                    "Area exactly doubles to 50 sq cm",
                    "Area increases by +25 sq cm",
                    "Area triples to 75 sq cm"
                ],
                "answer": 0,
                "hint": "Area scales multiplicatively across BOTH dimensions: (2s) × (2s) = 4s²!",
                "explanation": "Doubling side length multiplies area by 2 × 2 = 4, yielding four times the original area, not double."
            },
            {
                "question": "According to Verse 1.9 of Baudhāyana's Śulba-Sūtra, how do you build a square with EXACTLY DOUBLE the area of a given square?",
                "options": [
                    "Construct the new square on the DIAGONAL of the original square (4 congruent triangles vs 2)",
                    "Double every side length of the original square",
                    "Add 1 cm to both width and height",
                    "Use half of the original diagonal as the new side"
                ],
                "answer": 0,
                "hint": "Count the congruent right isosceles triangles formed by the diagonal!",
                "explanation": "One original square holds 2 congruent triangles, while the square built on its diagonal encloses 4 such triangles — exactly 2× area."
            }
        ]
    },
    {
        "id": 2,
        "title": "Halving A Square",
        "subtitle": "Section 2.2 Constructing Half-Area Squares: Inscribed Tilted Square PQRS & Midpoint Paper Folding",
        "speech": (
            "Can we reverse Baudhāyana's doubling miracle smoothly? Enter Section Two Point Two: Halving a Square! Suppose you hold a complete square sheet of paper of area A, and you wish to construct a smaller square whose area equals EXACTLY HALF of A without using any ruler measurements or decimal decimals! "
            "Follow the crisp hands-on paper-folding activity step by step! Start by finding the four exact side midpoints—simply fold opposite edges together cleanly along vertical and horizontal axes, or fold all four outer corners inward until their tips meet right at the dead center of the sheet! Mark those four side midpoints cleanly as P, Q, R, and S! When you connect P to Q, Q to R, R to S, and S back to P, you uncover an inscribed tilted inner square PQRS sitting symmetrically inside the outer square! "
            "Verify its exact area in two seconds using clean visual symmetry! The four folded triangular corner flaps lying outside PQRS fold inward snugly to cover EVERY single square centimeter of inner square PQRS—four triangles outside match four identical inner triangles inside! Therefore, inscribed midpoint square PQRS always holds EXACTLY ONE-HALF of the original outer square's total area cleanly!"
        ),
        "checkpoints": [
            {
                "question": "A square sheet of paper has area 64 sq cm. Four corners are folded inward along the midpoints P, Q, R, S to form an inscribed tilted square PQRS. What is the area of PQRS?",
                "options": [
                    "32 sq cm   (exactly half of 64 sq cm)",
                    "16 sq cm",
                    "48 sq cm",
                    "128 sq cm"
                ],
                "answer": 0,
                "hint": "The 4 folded outer triangles fit perfectly inside PQRS, dividing the sheet into 8 equal triangles (4 inside, 4 outside)!",
                "explanation": "Joining the side midpoints creates an inscribed square covering 4 out of 8 congruent triangles = 1/2 × 64 = 32 sq cm."
            },
            {
                "question": "Why does folding the four outer corner flaps inward onto the center prove that inscribed square PQRS equals half the original sheet?",
                "options": [
                    "The four outer flaps meet cleanly without overlap or gaps to cover the exact interior of PQRS",
                    "Because folding always cuts perimeter in half",
                    "Because each folded angle measures 60 degrees",
                    "Because midpoints sit 1/4 of the way along each edge"
                ],
                "answer": 0,
                "hint": "Think about comparing the combined area of the 4 outside corners directly against the inner square!",
                "explanation": "Since the 4 corner triangles completely tile PQRS with zero overlap, outer area = inner area = 50% each."
            }
        ]
    },
    {
        "id": 3,
        "title": "Isosceles Right Triangle",
        "subtitle": "Section 2.3 Hypotenuse of Isosceles Right Triangle: Unit Legs (1,1), c² = 2 & General c = a√2",
        "speech": (
            "Now link Baudhāyana's square doubling directly to triangle side lengths in Section Two Point Three! Slice a unit 1-by-1 square along its diagonal c to create an ISOSCELES RIGHT TRIANGLE whose two perpendicular legs both equal 1 unit! What exact length must that diagonal hypotenuse c measure? "
            "Recall Section Two Point One cleanly! The original unit square has area 1 × 1 = 1 square unit! The larger square built along hypotenuse c has DOUBLE that area—so its area c² equals 2! Wait: what positive number squared equals 2? Mathematicians name that exact length √2 (the positive square root of 2)! Thus, for legs 1 and 1, hypotenuse c equals √2! "
            "Now generalize smoothly from unit leg 1 to ANY isosceles right triangle having equal legs of length a! The original square has area a², so the diagonal square has double area c² = 2a²! Taking positive square roots on both sides establishes our general formula: c = a√2! Test immediately: if equal legs measure 5 cm, hypotenuse c = 5√2 cm! Conversely, if hypotenuse c measures 10 cm, solve 2a² = 100 → a² = 50 → leg length a = √50 cm effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "An isosceles right triangle has two equal legs measuring 7 cm each. What is the exact square of its hypotenuse (c²) and its hypotenuse c?",
                "options": [
                    "c² = 98 sq cm; c = 7√2 cm",
                    "c² = 49 sq cm; c = 7 cm",
                    "c² = 14 sq cm; c = √14 cm",
                    "c² = 196 sq cm; c = 14 cm"
                ],
                "answer": 0,
                "hint": "Apply c² = 2a² with a = 7: compute 2 × 7²!",
                "explanation": "c² = 2(7²) = 2 × 49 = 98, so c = √98 = 7√2 cm."
            },
            {
                "question": "If the hypotenuse of an isosceles right triangle measures 8 cm, what is the area of each square built on a single leg (a²)?",
                "options": [
                    "32 sq cm   (from 2a² = 64)",
                    "64 sq cm",
                    "16 sq cm",
                    "4 sq cm"
                ],
                "answer": 0,
                "hint": "Use c² = 2a² where c = 8, so 64 = 2a²!",
                "explanation": "Since c² = 8² = 64 and 2a² = c², each leg square has area a² = 64 ÷ 2 = 32 sq cm (so leg a = √32 cm)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Estimating Square Root",
        "subtitle": "Section 2.3 Decimal Representation of √2: Step-by-Step Bounds & Why √2 Cannot Terminate",
        "speech": (
            "How large is √2 as an ordinary decimal number? Squeeze it systematically between tighter upper and lower bounds in Section Two Point Three! First test whole integers: 1² = 1 (too small) and 2² = 4 (too large), proving 1 < √2 < 2! Next zoom into tenths: 1.4² = 1.96 (just under 2!) while 1.5² = 2.25 (clearly above 2!), narrowing to 1.4 < √2 < 1.5! Test hundredths next: 1.41² = 1.9881 while 1.42² = 2.0164! Finally test thousandths: 1.414² = 1.999396 whereas 1.415² = 2.002225, bounding 1.414 < √2 < 1.415! "
            "Wait—if we keep appending extra decimal digits far enough, will we EVER hit a finite terminating decimal whose square equals 2.000000 exactly? IMPOSSIBLE! Here is the crystal-clear last-digit mathematical proof! Pick ANY terminating decimal number ending in any non-zero final digit d (from 1 through 9)! Compute every single digit square d² carefully right now: 1²=1, 2²=4, 3²=9, 4²=16, 5²=25, 6²=36, 7²=49, 8²=64, 9²=81! Notice carefully that NO single-digit square ever ends in zero! Therefore, squaring ANY finite terminating decimal number always ends in a non-zero final digit, NEVER producing exact 2.000...! Thus √2 has a truly non-terminating decimal expansion continuing forever!"
        ),
        "checkpoints": [
            {
                "question": "Check the squares 1.41² = 1.9881 and 1.42² = 2.0164. Which tight interval bound for √2 do these two squares establish?",
                "options": [
                    "1.41 < √2 < 1.42",
                    "1.4 < √2 < 1.41",
                    "1.42 < √2 < 1.43",
                    "1.98 < √2 < 2.01"
                ],
                "answer": 0,
                "hint": "2 lies strictly between 1.9881 (= 1.41²) and 2.0164 (= 1.42²)!",
                "explanation": "Since 1.41² < 2 < 1.42², taking square roots gives 1.41 < √2 < 1.42."
            },
            {
                "question": "Why can NO terminating decimal number ever square to equal 2 exactly?",
                "options": [
                    "The square of its final non-zero digit (1..9) ends in 1, 4, 5, 6, or 9 — NEVER 0, so trailing zeros cannot form 2.000...",
                    "Because terminating decimals always become negative when squared",
                    "Because multiplying decimals halves the number of digits",
                    "Because 2 is an odd prime number"
                ],
                "answer": 0,
                "hint": "Check the units digit of d² for every non-zero digit d from 1 to 9!",
                "explanation": "No digit 1–9 squared ends in 0, so a terminating decimal squared always has a non-zero final decimal digit and can never equal 2."
            }
        ]
    },
    {
        "id": 5,
        "title": "Irrationality Proof Euclid",
        "subtitle": "Section 2.3 Euclid's Classic Proof (Elements c. 300 BCE): Odd vs Even Prime Factor 2s in 2n² = m²",
        "speech": (
            "We know √2 cannot end as a terminating decimal—could it perhaps equal a clean repeating fraction like m/n? Around three hundred BCE in his Elements, Euclid delivered one of history's most celebrated proofs showing √2 is completely IRRATIONAL—impossible to express as ANY integer ratio m/n! "
            "Follow Euclid's stunning prime-factor parity proof step by step! Suppose, just for argument, that positive integers m and n satisfy √2 = m/n! Square both sides cleanly to eliminate the root: 2 = m²/n², then multiply by n² to obtain the master integer equation: 2n² = m²! "
            "Now count how many times prime factor 2 divides each side! In ANY perfect square like m² or n², every prime factor of the base appears TWICE—meaning EVERY square holds an EVEN number of factor 2s (0, 2, 4, 6, and so on)! Look at the right-hand side m²: EVEN count of 2s! Now look at the left-hand side 2n²: n² has an EVEN count of 2s, PLUS ONE extra explicit factor of 2 in front! Even plus one equals ODD! One side has an ODD number of 2s while the identical number has an EVEN number—contradiction! Hence √2 can NEVER equal m/n!"
        ),
        "checkpoints": [
            {
                "question": "Suppose √2 = m/n for positive integers m, n, yielding 2n² = m². Why does prime factorization reveal a contradiction?",
                "options": [
                    "2n² contains an ODD number of prime factor 2s, while m² must contain an EVEN number of prime factor 2s",
                    "Because m² is always prime while 2n² is composite",
                    "Because n² cannot be multiplied by 2",
                    "Because m and n must both equal 1"
                ],
                "answer": 0,
                "hint": "Every prime factor in a square (m² or n²) appears an EVEN number of times!",
                "explanation": "Squaring doubles all prime exponents, so n² and m² have even powers of 2; multiplying n² by 2 makes LHS odd-powered, contradicting RHS."
            },
            {
                "question": "If integer k has prime factorization containing three factors of 2 (i.e., 2³), how many factors of 2 appear inside k²?",
                "options": [
                    "Six factors of 2   (always EVEN: 2 × 3 = 6)",
                    "Three factors of 2",
                    "Nine factors of 2",
                    "Five factors of 2"
                ],
                "answer": 0,
                "hint": "Compute (2³)² by doubling the exponent!",
                "explanation": "(2³)² = 2⁶ has 6 factors of 2 — squaring always guarantees an even count of every prime factor."
            }
        ]
    },
    {
        "id": 6,
        "title": "Combining Two Squares",
        "subtitle": "Section 2.4 Śulba-Sūtra Verse 1.12 & Theorem Statement (a² + b² = c²): Historical Precedence of Baudhāyana",
        "speech": (
            "Now leap forward into Section Two Point Four, uncovering the celebrated crown jewel of this entire geometric chapter! In Section Two Point One, Baudhāyana combined two IDENTICAL squares into one larger double-area square! What happens if you possess TWO DIFFERENT-SIZED SQUARES—say square A with side a (area a²) and smaller square B with side b (area b²)? Verse One Point Twelve of Baudhāyana's Śulba-Sūtra asks directly: how can we construct ONE single unified square whose combined area equals the EXACT SUM a² + b²? "
            "Here stands Baudhāyana's timeless theorem statement: in ANY right-angled triangle having perpendicular legs a and b and longest slanted side hypotenuse c, the area of the square constructed cleanly on hypotenuse c ALWAYS equals the exact sum of the areas of the two squares constructed on legs a and b—written algebraically as a² + b² = c²! "
            "Notice the important historical truth carefully emphasized by NCERT! Baudhāyana clearly formulated and proved this general mathematical theorem right inside his Śulba-Sūtra text centuries BEFORE the Greek philosopher and mathematician Pythagoras lived around five hundred BCE! To honor both ancient mathematical traditions accurately and fairly, our textbook introduces the balanced transitional title: THE BAUDHĀYANA-PYTHAGORAS THEOREM!"
        ),
        "checkpoints": [
            {
                "question": "A right-angled triangle has legs of lengths a = 6 cm and b = 8 cm. What is the area of the square built on its hypotenuse (c²) and hypotenuse length c?",
                "options": [
                    "c² = 100 sq cm; c = 10 cm",
                    "c² = 14 sq cm; c = √14 cm",
                    "c² = 28 sq cm; c = √28 cm",
                    "c² = 48 sq cm; c = √48 cm"
                ],
                "answer": 0,
                "hint": "Add the two leg-square areas cleanly: 6² + 8² = 36 + 64!",
                "explanation": "a² + b² = 36 + 64 = 100 = c², so c = √100 = 10 cm."
            },
            {
                "question": "Why does NCERT refer to a² + b² = c² as the 'Baudhāyana-Pythagoras Theorem'?",
                "options": [
                    "Baudhāyana stated the general theorem in his Śulba-Sūtra (~800 BCE), predating Pythagoras (~500 BCE) by centuries",
                    "Because Baudhāyana and Pythagoras co-wrote a book in 300 BCE",
                    "Because Baudhāyana studied only equilateral triangles while Pythagoras studied squares",
                    "Because it applies strictly to Indian architecture"
                ],
                "answer": 0,
                "hint": "Check the chronology between ~800 BCE and ~500 BCE!",
                "explanation": "Baudhāyana documented the general theorem in Verse 1.12 of the Śulba-Sūtra centuries before Pythagoras."
            }
        ]
    },
    {
        "id": 7,
        "title": "Baudhayana Dissection Proof",
        "subtitle": "Section 2.4 Geometric & Paper-Cutting Proof: Śulba-Sūtra Verse 2.1 Rectangle Dissection into c²",
        "speech": (
            "Words alone never satisfy true mathematicians—HOW did Baudhāyana visually PROVE that a² + b² equals c² for EVERY pair of squares? Inspect Verse Two Point One's stunning dissection and paper-cutting proof right now! "
            "Place your smaller square (side a, area a²) snug next to your larger square (side b, area b²) sitting flat along a shared baseline! Next follow Verse Two Point One cleanly: mark off width a inside the larger b × b square to slice out two identical right-angled triangles having legs a, b and diagonal hypotenuse c! Notice what remains of the original joined figure: an exact smaller piece that completes the inner geometry! "
            "Now perform the magical rigid paper-cutting motion! Slide and rotate those two sliced right-angled triangles cleanly outward onto the adjacent straight edges without losing a single square millimeter of paper area! Look at the brand-new outer boundary formed seamlessly around all four sides: every edge measures exact hypotenuse c, every corner forms an exact ninety-degree right angle (because the two acute angles of any right triangle always sum cleanly to ninety degrees!), enclosing ONE seamless unified square of area c²! Paper conservation proves a² + b² = c² visually!"
        ),
        "checkpoints": [
            {
                "question": "In Baudhāyana's Verse 2.1 paper-cutting proof combining squares of area a² and b², why must the rearranged shape have EXACTLY 90° corners to be a true square of area c²?",
                "options": [
                    "Because the two acute angles of each sliced right triangle sum to 90°, forming perfect right-angle corners when rotated",
                    "Because every side is trimmed after cutting",
                    "Because paper always stretches by 10%",
                    "Only when a equals b"
                ],
                "answer": 0,
                "hint": "In any right triangle, angles α + β + 90° = 180°, so α + β = 90°!",
                "explanation": "Rotating the two congruent right triangles places α + β = 90° cleanly at the corners, producing an exact c × c square."
            },
            {
                "question": "If you cut a 9 sq cm square and a 16 sq cm square using Baudhāyana's dissection method and rearrange all pieces without gaps or overlaps, what is the exact side length of the single resulting square?",
                "options": [
                    "5 cm   (since combined area = 9 + 16 = 25 sq cm)",
                    "7 cm   (3 + 4)",
                    "12.5 cm",
                    "25 cm"
                ],
                "answer": 0,
                "hint": "Total paper area never changes during cutting and rearranging!",
                "explanation": "Total area = 9 + 16 = 25 sq cm, so the rearranged single square has side √25 = 5 cm."
            }
        ]
    },
    {
        "id": 8,
        "title": "Baudhayana Integer Triples",
        "subtitle": "Section 2.5 Baudhāyana Triples (Verse 1.13: 3-4-5, 5-12-13, 8-15-17, 7-24-25), Scaling & Primitive Triples",
        "speech": (
            "Notice how most right triangles have messy roots like √2 or √50—yet certain magical right triangles possess ALL THREE SIDES AS CRISP WHOLE INTEGERS! Enter Section Two Point Five: Baudhāyana Triples! Any three positive integers (a, b, c) obeying a² + b² = c² form a Baudhāyana triple! Look back at Verse One Point Thirteen of the Śulba-Sūtra listing four timeless classics: (3, 4, 5) since 9 + 16 = 25; (5, 12, 13) since 25 + 144 = 169; (8, 15, 17) since 64 + 225 = 289; and (7, 24, 25) since 49 + 576 = 625! "
            "Watch what happens when you scale EVERY side of a valid triple by any whole multiplier k! Test k = 2 on (3, 4, 5): obtaining (6, 8, 10) gives 36 + 64 = 100 = 10²! Algebra confirms why permanently: (ka)² + (kb)² = k²(a² + b²) = k²c² = (kc)²! Thus infinite scaled triples exist! "
            "To avoid repeats, mathematicians define a PRIMITIVE BAUDHĀYANA TRIPLE as an integer triple whose three numbers share NO common factor greater than 1! So (3, 4, 5) is primitive, whereas (6, 8, 10) and (15, 36, 39) are scaled multiples!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following integer sets is a PRIMITIVE Baudhāyana triple (satisfies a² + b² = c² AND has HCF(a, b, c) = 1)?",
                "options": [
                    "(8, 15, 17)",
                    "(6, 8, 10)",
                    "(10, 24, 26)",
                    "(8, 15, 19)"
                ],
                "answer": 0,
                "hint": "Check both a² + b² = c² AND whether all three numbers share a common divisor > 1!",
                "explanation": "8² + 15² = 64 + 225 = 289 = 17², and HCF(8, 15, 17) = 1. Both (6,8,10) and (10,24,26) share common factor 2."
            },
            {
                "question": "Scaling the triple (5, 12, 13) by factor k = 3 creates (15, 36, 39). Why is (15, 36, 39) guaranteed to form a right-angled triangle?",
                "options": [
                    "Because (ka)² + (kb)² = k²(a² + b²) = k²c² = (kc)², preserving equality!",
                    "Because adding 10 to each side preserves right triangles",
                    "Because all multiples of 3 are prime",
                    "Because 15 + 36 = 39"
                ],
                "answer": 0,
                "hint": "Factor out k² = 3² = 9 from (15² + 36²)!",
                "explanation": "15² + 36² = 9(5² + 12²) = 9(13²) = 39², proving every positive scaling (ka, kb, kc) stays a right triple."
            }
        ]
    }
]

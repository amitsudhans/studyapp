#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 8: Introduction to Trigonometry
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (Aryabhata and Edmund Gunter are historical syllabus figures; zero fictional names like Raghav, Sonia, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Right Triangle Geometry",
        "subtitle": "Origins of Trigonometry (Egypt & Babylon) + Measuring Qutub Minar, Rivers & Hot-Air Balloons",
        "speech": (
            "Welcome, curious geometry explorers, to one of mathematics most exciting and practical branches: Chapter Eight, Introduction to Trigonometry! "
            "Decode the word trigonometry right from its three classic Greek roots: tri means three, gon means sides, and metron means measure! Thus trigonometry is the exact mathematical study of relationships linking all side lengths and interior angles of a triangle! "
            "Thousands of years ago, clever ancient astronomers across Egypt and Babylon used early trigonometry to measure immense celestial distances from planet Earth cleanly out to distant stars and planets! Today engineers, architects, physicists, and ocean surveyors still rely heavily on trigonometric ratios daily! "
            "Picture three vivid real world scenes straight from Section Eight Point One! Scene One: standing safely on flat ground looking up toward the top of the towering Qutub Minar forms an imaginary vertical right angled triangle connecting your eye line to the peak! "
            "Scene Two: standing on one balcony bank looking across a wide flowing river to a flowerpot sitting directly on the opposite lower bank measures the unreachable river width! Scene Three: tracking a steadily rising hot air balloon measures changing vertical altitude smoothly above flat ground using JUST ONE measured distance and angle!"
        ),
        "checkpoints": [
            {
                "question": "From its Greek roots 'tri + gon + metron', what does Trigonometry fundamentally study?",
                "options": [
                    "Relationships between the sides and angles of triangles (especially right-angled triangles)",
                    "Only areas of circles and ellipses",
                    "Only counting prime numbers",
                    "Volume of spheres in 3D space without angles"
                ],
                "answer": 0,
                "hint": "Break down tri (3), gon (sides/angles), and metron (measure)!",
                "explanation": "Trigonometry studies exact numerical ratios relating the side lengths and angles of right triangles."
            },
            {
                "question": "How does trigonometry allow surveyors to find the height of the Qutub Minar or width of a flowing river without directly climbing or crossing?",
                "options": [
                    "By forming an imaginary right-angled triangle using ground distance and line of sight angle, then solving the unknown vertical side",
                    "By guessing height visually from clouds",
                    "Because all rivers are 100 meters wide",
                    "Because right triangles have equal sides always"
                ],
                "answer": 0,
                "hint": "One measurable horizontal side plus one elevation/depression angle determines the missing vertical height!",
                "explanation": "Connecting the observer, object base, and top creates a right triangle whose trigonometric ratio finds the height."
            }
        ]
    },
    {
        "id": 2,
        "title": "Six Trig Ratios",
        "subtitle": "Defining sin, cos, tan, cosec, sec, cot + Historical Contributions of Aryabhata & Edmund Gunter",
        "speech": (
            "Step straight inside Section Eight Point Two and label all three sides of any right angled triangle ABC, right angled at vertex B, relative to acute interior angle A! "
            "First, side AC sitting directly across from the ninety degree right corner is ALWAYS the longest side, wearing the title Hypotenuse! Second, side BC facing straight across from acute angle A is the Side Opposite to angle A! Third, side AB touching angle A right alongside the hypotenuse is the Side Adjacent to angle A! "
            "From just these three clean triangle sides, build all SIX fundamental Trigonometric Ratios for acute interior angle A! Sine A equals Opposite over Hypotenuse! Cosine A equals Adjacent over Hypotenuse! Tangent A equals Opposite over Adjacent! "
            "Flip those three ratios cleanly upside down for their three reciprocal partners: Cosecant A equals Hypotenuse over Opposite! Secant A equals Hypotenuse over Adjacent! Cotangent A equals Adjacent over Opposite! "
            "Remember their fascinating mathematical history across centuries: the great Indian astronomer mathematician Aryabhata first introduced ardha jya inside his famous 500 CE treatise Aryabhatiyam, later evolving via Arabic into Latin sinus, while English astronomer Edmund Gunter later coined modern abbreviations sin, cos, and tan cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In right △ABC (∠B = 90°), how are sin A and cos A defined relative to acute angle A?",
                "options": [
                    "sin A = Opposite (BC) / Hypotenuse (AC),   and   cos A = Adjacent (AB) / Hypotenuse (AC)",
                    "sin A = Adjacent / Hypotenuse,   and   cos A = Opposite / Hypotenuse",
                    "sin A = Opposite / Adjacent,   and   cos A = Adjacent / Opposite",
                    "sin A = Hypotenuse / Opposite"
                ],
                "answer": 0,
                "hint": "Remember classic memory aid: Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse, Tangent = Opposite/Adjacent!",
                "explanation": "Relative to acute angle A, side BC is opposite, AB is adjacent, and AC is hypotenuse: sin A = BC/AC and cos A = AB/AC."
            },
            {
                "question": "Which Indian mathematician introduced the concept of 'ardha-jya' (half-chord) in Aryabhatiyam (500 CE), which eventually evolved into the word 'sine'?",
                "options": [
                    "Aryabhata",
                    "Edmund Gunter",
                    "Euclid",
                    "Gauss"
                ],
                "answer": 0,
                "hint": "Section 8.2 highlights this astronomer-mathematician's 500 CE treatise Aryabhatiyam!",
                "explanation": "Aryabhata used 'ardha-jya' (abbreviated jya), translated to Arabic jiba -> jaib -> Latin sinus -> sine."
            }
        ]
    },
    {
        "id": 3,
        "title": "Perspective Shift Rules",
        "subtitle": "Switching Reference Angle A ↔ C Plus Quotient & Reciprocal Laws (tan A = sin A / cos A)",
        "speech": (
            "Watch out for the number one beginner mistake across Chapter Eight! Inside ONE fixed right triangle ABC, right angled at B, hypotenuse AC stays permanently fixed forever, YET Side Opposite and Side Adjacent SWAP PLACES completely whenever you switch your gaze from angle A up to complementary angle C! "
            "Look carefully! Standing at bottom acute angle A, the opposite wall is side BC and adjacent floor is side AB, so sine A equals BC over AC! Now climb straight up to top acute angle C! Standing at angle C, opposite floor becomes AB and adjacent wall becomes BC! Therefore sine C equals AB over AC, matching cosine A identically! "
            "Notice that gorgeous reciprocal partnership across all six trigonometric ratios too! Cosecant A ALWAYS equals one divided by sine A! Secant A ALWAYS equals one divided by cosine A! Cotangent A ALWAYS equals one divided by tangent A! "
            "Even better, divide sine A cleanly by cosine A right now: (Opposite over Hypotenuse) divided by (Adjacent over Hypotenuse) cancels common Hypotenuse cleanly, yielding Opposite over Adjacent, proving our golden Quotient Laws: tangent A equals sine A divided by cosine A, while cotangent A equals cosine A divided by sine A!"
        ),
        "checkpoints": [
            {
                "question": "In right △ABC (∠B = 90°) with AB = 24 cm and BC = 7 cm (Hypotenuse AC = 25 cm, Ex 8.1 Q1), compare sin A vs sin C:",
                "options": [
                    "sin A = 7/25 (opp BC)  whereas  sin C = 24/25 (opp AB)",
                    "Both sin A and sin C equal 7/25",
                    "sin A = 24/25  and  sin C = 7/25",
                    "sin A = 7/24  and  sin C = 24/7"
                ],
                "answer": 0,
                "hint": "Side opposite ∠A is BC = 7, while side opposite ∠C is AB = 24!",
                "explanation": "Switching from ∠A to ∠C swaps opposite and adjacent sides: sin A = BC/AC = 7/25, while sin C = AB/AC = 24/25."
            },
            {
                "question": "Which pair of Quotient Identities accurately expresses tan A and cot A in terms of sin A and cos A?",
                "options": [
                    "tan A = sin A / cos A   and   cot A = cos A / sin A",
                    "tan A = cos A / sin A   and   cot A = sin A / cos A",
                    "tan A = sin A × cos A",
                    "tan A = 1 / sin A"
                ],
                "answer": 0,
                "hint": "Divide (Opposite / Hypotenuse) by (Adjacent / Hypotenuse) cleanly!",
                "explanation": "Hypotenuse cancels in (Opp/Hyp) ÷ (Adj/Hyp) = Opp/Adj = tan A, while cot A = 1/tan A = cos A / sin A."
            }
        ]
    },
    {
        "id": 4,
        "title": "Scale Invariance Proof",
        "subtitle": "Why Trig Ratios Are Independent of Triangle Size (AA Similarity) + Bounds (sin A ≤ 1, sec A ≥ 1)",
        "speech": (
            "Suppose two curious geometry students draw two completely different sized right triangles sharing the exact same acute angle A equal to thirty seven degrees: one tiny notebook triangle with hypotenuse five centimeters, and one massive outdoor courtyard triangle with hypotenuse fifty meters! "
            "Question: will sine of thirty seven degrees change when the triangle grows ten times larger? NEVER! Look back at Chapter Six to see WHY! "
            "Drop ANY vertical perpendicular line segment MN inside giant right triangle ABC along angle A! Immediately small right triangle AMN and giant right triangle ABC share common acute angle A AND ninety degree right corners, making triangle AMN strictly similar to triangle ABC by Chapter Six AA Similarity! "
            "By similarity proportionality, small vertical over small hypotenuse (MN over AM) equals giant vertical over giant hypotenuse (BC over AC)! Scale factor cancels out completely! "
            "Thus all six trigonometric ratios depend strictly on angle measure, NEVER on triangle side lengths! Also remember strict bounds in Exercise Eight Point One: because hypotenuse is ALWAYS the strictly longest triangle side, sine A and cosine A can NEVER exceed one, whereas cosecant A and secant A are ALWAYS greater than or equal to one!"
        ),
        "checkpoints": [
            {
                "question": "Why do the trigonometric ratios of an acute angle A remain invariant even when the right triangle scales up or down?",
                "options": [
                    "Because all right triangles sharing acute angle A are similar by AA Similarity, keeping corresponding side ratios constant",
                    "Because side lengths never change",
                    "Because tangent A always equals 1",
                    "Because all right triangles are congruent"
                ],
                "answer": 0,
                "hint": "Think directly of Chapter 6: matching 90° + shared ∠A creates what triangle relationship?",
                "explanation": "AA Similarity ensures any scaled right triangle with angle A preserves identical ratios Opp/Hyp, Adj/Hyp, and Opp/Adj."
            },
            {
                "question": "Which statement from Exercise 8.1 Q11 about trigonometric bounds for an acute angle A is MATHEMATICALLY TRUE?",
                "options": [
                    "sec A = 12/5 is possible (since sec A ≥ 1), whereas sin θ = 4/3 is IMPOSSIBLE (since opposite side can never exceed hypotenuse!)",
                    "The value of tan A is ALWAYS less than 1",
                    "sin θ = 4/3 is possible for wide triangles",
                    "cos A = 1 is an abbreviation for 'cosecant of angle A'"
                ],
                "answer": 0,
                "hint": "Check which side of a right triangle is STRICTLY longest — hypotenuse!",
                "explanation": "Because Opposite ≤ Hypotenuse, sin θ ≤ 1 always (4/3 > 1 is impossible); Hypotenuse ≥ Adjacent allows sec A = 12/5 = 2.4 ≥ 1!"
            }
        ]
    },
    {
        "id": 5,
        "title": "Pythagoras Ratio Solving",
        "subtitle": "Computing All 6 Ratios From One Fraction (k-Multiplier Method) + Ex 8.1 Triangle Proofs",
        "speech": (
            "Suppose Exercise Eight Point One tells you tangent A equals four over three, and challenges you to compute ALL five remaining trigonometric ratios cleanly! Never accidentally claim Opposite equals four centimeters and Adjacent equals three centimeters directly! Remember reduced fractions hide common factors! "
            "Always introduce a positive common scaling factor k: set Opposite BC equal to four k and Adjacent AB equal to three k! Then Pythagoras Theorem delivers Hypotenuse AC equal to square root of (four k whole squared plus three k whole squared), giving root of twenty five k squared equals five k! Dividing ratios cancels positive factor k completely, giving sine A equals four fifths and cosine A equals three fifths! "
            "Also check Exercise Eight Point One Question Ten and its famous triple riddle: in right triangle PQR right angled at vertex Q, given side PQ equals five centimeters and sum PR plus QR equals twenty five centimeters! "
            "Set QR equal to unknown leg length x centimeters and PR equal to (25 minus x) centimeters! Applying Pythagoras Theorem cleanly gives (25 minus x) squared equals 5 squared plus x squared, solving cleanly to x equals 12 and hypotenuse PR equals 13 centimeters!"
        ),
        "checkpoints": [
            {
                "question": "In right △PQR (∠Q = 90°), PQ = 5 cm and PR + QR = 25 cm (Exercise 8.1 Q10). Find sin P and cos P:",
                "options": [
                    "sin P = 12/13  and  cos P = 5/13",
                    "sin P = 5/13  and  cos P = 12/13",
                    "sin P = 12/5  and  cos P = 5/12",
                    "sin P = 5/25  and  cos P = 20/25"
                ],
                "answer": 0,
                "hint": "Solve (25 − x)² = 5² + x² ⟹ 625 − 50x + x² = 25 + x² ⟹ 50x = 600 ⟹ QR = 12, PR = 13!",
                "explanation": "Pythagoras gives sides 5, 12, 13; relative to ∠P, opposite QR = 12, adjacent PQ = 5, hypotenuse PR = 13 ⟹ sin P = 12/13, cos P = 5/13."
            },
            {
                "question": "Given 15 cot A = 8 (Exercise 8.1 Q4), find sin A and sec A cleanly using the k-multiplier method:",
                "options": [
                    "sin A = 15/17  and  sec A = 17/8",
                    "sin A = 8/17  and  sec A = 17/15",
                    "sin A = 15/8  and  sec A = 8/15",
                    "sin A = 7/17  and  sec A = 17/7"
                ],
                "answer": 0,
                "hint": "cot A = 8/15 sets Adjacent = 8k and Opposite = 15k ⟹ Hypotenuse = √(64 + 225)k = 17k!",
                "explanation": "Sides 8k, 15k, 17k give sin A = Opp/Hyp = 15/17 and sec A = Hyp/Adj = 17/8."
            }
        ]
    },
    {
        "id": 6,
        "title": "Angles 45 Degrees",
        "subtitle": "Geometric Derivation of Exact Trigonometric Ratios for 45° Using an Isosceles Right Triangle",
        "speech": (
            "Welcome to Section Eight Point Three: discovering exact geometric trigonometric ratio values for standard special angles without touching an electronic calculator! Start right at forty five degrees! "
            "Construct a right angled triangle ABC right angled at B, setting acute angle A strictly equal to forty five degrees! Immediately by Triangle Angle Sum one hundred eighty degrees, what MUST the remaining top acute angle C equal? One hundred eighty minus ninety minus forty five equals forty five degrees as well! "
            "Because interior angle A equals interior angle C inside triangle ABC, sides sitting opposite equal angles MUST be strictly equal! That makes triangle ABC a crisp ISOSCELES RIGHT TRIANGLE where side AB equals side BC! Let us call both equal legs length a! "
            "Now find slanted hypotenuse AC cleanly via Pythagoras Theorem: AC squared equals a squared plus a squared equals two a squared, yielding AC equals a root two! "
            "Compute every trigonometric ratio instantaneously: variable a cancels out completely! Sine forty five degrees equals a over a root two equals one over root two! Cosine forty five ALSO equals one over root two! And tangent forty five equals a over a equals exact crisp one!"
        ),
        "checkpoints": [
            {
                "question": "How does NCERT Section 8.3 derive exact trigonometric ratios for 45° geometrically?",
                "options": [
                    "Using an isosceles right triangle with legs a, a (because ∠A = ∠C = 45°) and hypotenuse a√2 by Pythagoras",
                    "Using an equilateral triangle of side 2a",
                    "By dividing 90° ratios by 2",
                    "Using a circle of radius 0"
                ],
                "answer": 0,
                "hint": "If ∠B = 90° and ∠A = 45°, then ∠C = 45° forces BC = AB = a!",
                "explanation": "Equal angles (45°) make legs equal (a, a) and hypotenuse a√2, canceling 'a' to yield sin 45° = cos 45° = 1/√2 and tan 45° = 1."
            },
            {
                "question": "Evaluate 2 tan² 45° + cos² 30° − sin² 60° (Exercise 8.2 Q1 ii) or check the value of sin² 45° + cos² 45°:",
                "options": [
                    "sin² 45° + cos² 45° = (1/√2)² + (1/√2)² = 1/2 + 1/2 = 1",
                    "0",
                    "2",
                    "1/√2"
                ],
                "answer": 0,
                "hint": "Square 1/√2 neatly to get 1/2!",
                "explanation": "(1/√2)² + (1/√2)² = 1/2 + 1/2 = 1."
            }
        ]
    },
    {
        "id": 7,
        "title": "Deriving 30° 60°",
        "subtitle": "Geometric Derivation of 30° and 60° Ratios by Splitting an Equilateral Triangle of Side 2a",
        "speech": (
            "Now derive BOTH thirty degrees and sixty degrees simultaneously from ONE single symmetric geometric shape: an equilateral triangle ABC whose every side spans length two a and every interior corner angle holds exact sixty degrees! "
            "Drop straight perpendicular altitude AD from top corner A squarely down onto bottom base BC! By geometric symmetry or RHS congruence, right triangles ADB and ADC are strictly congruent to one another! Therefore altitude AD cleanly bisects bottom base BC into equal halves BD equals DC equals a, AND cleanly bisects the top sixty degree corner into thirty degrees each! "
            "Inside left right triangle ABD: slanted hypotenuse AB equals two a, short base BD opposite thirty degrees equals a, and vertical altitude AD by Pythagoras equals square root of four a squared minus a squared equals a root three! "
            "Now read BOTH special angle sets cleanly straight off right triangle ABD! Standing at thirty degrees: sine thirty equals one half, cosine thirty equals root three over two, and tangent thirty equals one over root three! Standing at sixty degrees: sine sixty equals root three over two, cosine sixty equals exact one half, and tangent sixty equals pure square root of three!"
        ),
        "checkpoints": [
            {
                "question": "In deriving 30° and 60° ratios from an equilateral triangle of side 2a split by altitude AD, what are the three sides of right △ABD?",
                "options": [
                    "Hypotenuse AB = 2a,  Base BD (opp 30°) = a,  and Altitude AD (opp 60°) = a√3",
                    "AB = 2a, BD = a, AD = a",
                    "AB = a√2, BD = a, AD = a",
                    "AB = 2a, BD = a√3, AD = a"
                ],
                "answer": 0,
                "hint": "Compute AD = √[(2a)² − a²] = √(3a²) = a√3!",
                "explanation": "Half of base 2a gives BD = a, and Pythagoras gives altitude AD = a√3, yielding exact ratios for 30° and 60°."
            },
            {
                "question": "Evaluate (sin 60°)(cos 30°) + (sin 30°)(cos 60°) (Exercise 8.2 Q1 i):",
                "options": [
                    "1   [since (√3/2)(√3/2) + (1/2)(1/2) = 3/4 + 1/4]",
                    "1/2",
                    "√3/2",
                    "0"
                ],
                "answer": 0,
                "hint": "Multiply (√3/2) × (√3/2) = 3/4 and (1/2) × (1/2) = 1/4!",
                "explanation": "sin 60° cos 30° + sin 30° cos 60° = (√3/2)² + (1/2)² = 3/4 + 1/4 = 1."
            }
        ]
    },
    {
        "id": 8,
        "title": "Boundary Angles Limits",
        "subtitle": "Limit Observations for 0° and 90° & Why tan 90°, sec 90°, cosec 0°, cot 0° Are Not Defined",
        "speech": (
            "Can an ordinary right angled triangle actually hold a second ninety degree angle OR a flat zero degree angle? Strictly speaking, as acute angle A approaches zero degrees or ninety degrees, the right triangle flattens cleanly into a single straight line segment! Watch carefully what happens to all ratios at those two extreme angle limits! "
            "Limit One: Let acute angle A shrink smaller and smaller steadily toward ZERO degrees while keeping base AB fixed! Look closely at opposite vertical height BC: BC shrinks closer and closer to ZERO, while slanted hypotenuse AC drops flat straight down on top of AB, making AC approach AB! "
            "Hence at angle A equals zero degrees: sine zero equals zero over AC equals ZERO! Cosine zero equals AB over AB equals ONE! Tangent zero equals zero over AB equals ZERO! Meanwhile, cosecant zero (one over sine zero) and cotangent zero divide by zero, making them strictly NOT DEFINED! "
            "Limit Two: Swing acute angle A wide open toward NINETY degrees! Now base leg AB shrinks completely down to ZERO while slanted hypotenuse AC merges cleanly straight into vertical wall BC! Thus sine ninety equals ONE, cosine ninety equals ZERO, and tangent ninety becomes NOT DEFINED!"
        ),
        "checkpoints": [
            {
                "question": "As acute angle A approaches 90° in right △ABC (∠B = 90°), which geometric limits occur?",
                "options": [
                    "Adjacent side AB → 0 and Hypotenuse AC → BC, making sin 90° = 1, cos 90° = 0, and tan 90° NOT DEFINED",
                    "Opposite side BC → 0, making sin 90° = 0 and cos 90° = 1",
                    "Hypotenuse AC → 0",
                    "tan 90° equals 1"
                ],
                "answer": 0,
                "hint": "Push vertex A closer and closer to B so base AB vanishes and AC merges vertically into BC!",
                "explanation": "When A → 90°, AB → 0 and AC → BC, yielding cos 90° = 0, sin 90° = 1, and tan 90° = 1/0 (not defined)."
            },
            {
                "question": "Which four boundary values in Table 8.1 are STRICTLY 'Not Defined' (division by zero)?",
                "options": [
                    "cosec 0°,  cot 0°,  tan 90°,  and  sec 90°",
                    "sin 0°,  cos 90°,  tan 0°,  and  cot 90°",
                    "cosec 90°,  sec 0°,  tan 45°,  cot 45°",
                    "None—all trigonometric ratios are defined at 0° and 90°"
                ],
                "answer": 0,
                "hint": "Find where denominator sin 0° = 0 OR cos 90° = 0 lands in the bottom of a fraction!",
                "explanation": "Since sin 0° = 0, its reciprocals cosec 0° and cot 0° are not defined; since cos 90° = 0, tan 90° and sec 90° are not defined."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch8 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 8: Introduction to Trigonometry
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
        "title": "Master Ratio Table",
        "subtitle": "Compiling Table 8.1 Values (0°, 30°, 45°, 60°, 90°), Fast √n/2 Trick & Monotonic Trends",
        "speech": (
            "Now lock ALL thirty exact values of Standard Table Eight Point One permanently into your memory using ONE effortless numerical root pattern! "
            "Write the five standard angles in ascending order: zero degrees, thirty degrees, forty five degrees, sixty degrees, and ninety degrees! Underneath them write simple integers zero, one, two, three, four! Divide each by four and take positive square roots! "
            "Compute out loud right now: root zero over four equals ZERO! Root one over four equals ONE HALF! Root two over four equals ONE OVER ROOT TWO! Root three over four equals ROOT THREE OVER TWO! Root four over four equals ONE! "
            "Congratulations, you just reconstructed EVERY single sine value cleanly from zero degrees all the way up to ninety degrees! "
            "For COSINE values, simply reverse that exact sine row cleanly backwards from right to left: one, root three over two, one over root two, one half, and zero! Divide sine by cosine for tangent, and flip reciprocals cleanly for cosecant, secant, and cotangent! "
            "Notice one crystal clear trend tested repeatedly in Exercise Eight Point Two: as acute angle theta climbs upward from zero to ninety degrees, sine theta strictly INCREASES while cosine theta strictly DECREASES!"
        ),
        "checkpoints": [
            {
                "question": "As angle θ increases from 0° to 90° (Exercise 8.2 Q4), how do sin θ and cos θ behave?",
                "options": [
                    "sin θ INCREASES from 0 to 1, whereas cos θ DECREASES from 1 down to 0",
                    "Both sin θ and cos θ increase from 0 to 1",
                    "sin θ decreases while cos θ increases",
                    "sin θ = cos θ for ALL values of θ"
                ],
                "answer": 0,
                "hint": "Compare 0° (sin 0°=0, cos 0°=1) against 90° (sin 90°=1, cos 90°=0)!",
                "explanation": "sin θ rises monotonically 0 → 1/2 → 1/√2 → √3/2 → 1, while cos θ falls symmetrically 1 → √3/2 → 1/√2 → 1/2 → 0."
            },
            {
                "question": "For which acute angle θ between 0° and 90° does sin θ strictly equal cos θ?",
                "options": [
                    "45° only  (where both equal 1/√2)",
                    "30° only",
                    "60° only",
                    "Every angle θ"
                ],
                "answer": 0,
                "hint": "Check Table 8.1 to find the single column where sin and cos rows match!",
                "explanation": "In Table 8.1, sin θ = cos θ holds strictly at θ = 45° (= 1/√2)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Evaluating Standard Angles",
        "subtitle": "Solving Unknown Sides From Angle + Side (Ex 6) & Simultaneous Angle Equations tan(A±B) (Ex 8.2 Q3)",
        "speech": (
            "Now put Standard Table Eight Point One straight to work solving unknown right triangle side lengths AND simultaneous angle equations inside Exercise Eight Point Two! "
            "Watch Textbook Example Six: In right triangle ABC right angled at B, vertical wall AB spans five centimeters and ground elevation angle ACB equals thirty degrees! Find BOTH horizontal floor BC and slanted hypotenuse AC! "
            "Ask yourself smartly: which trig ratio links known Opposite side five centimeters cleanly to unknown Adjacent floor BC? Tangent! Write tangent thirty degrees equals AB over BC, so one over root three equals five over BC -> floor BC equals five root three centimeters! "
            "Next connect Opposite side five cleanly to unknown Hypotenuse AC via Sine: sine thirty degrees equals five over AC, so one half equals five over AC, giving AC equals ten centimeters! "
            "Now crush Exercise Eight Point Two Question Three: Given tan(A plus B) equals root three AND tan(A minus B) equals one over root three! Matching Table Eight Point One values instantly sets A plus B equals sixty degrees and A minus B equals thirty degrees! Adding both linear equations solves A equals forty five degrees and B equals fifteen degrees!"
        ),
        "checkpoints": [
            {
                "question": "If tan(A + B) = √3 and tan(A − B) = 1/√3 (0° < A + B ≤ 90°, A > B, Ex 8.2 Q3), find angles A and B:",
                "options": [
                    "A = 45°,  B = 15°",
                    "A = 60°,  B = 30°",
                    "A = 30°,  B = 15°",
                    "A = 45°,  B = 30°"
                ],
                "answer": 0,
                "hint": "Match Table 8.1: tan 60° = √3 and tan 30° = 1/√3 ⟹ A + B = 60° and A − B = 30°!",
                "explanation": "Adding A + B = 60° and A − B = 30° gives 2A = 90° ⟹ A = 45° and B = 15°."
            },
            {
                "question": "Evaluate (2 tan 30°) / (1 + tan² 30°) (Exercise 8.2 Q2 i) and identify which standard ratio matches its value:",
                "options": [
                    "sin 60°  (= √3/2)",
                    "cos 60°  (= 1/2)",
                    "tan 60°  (= √3)",
                    "sin 30°  (= 1/2)"
                ],
                "answer": 0,
                "hint": "Substitute tan 30° = 1/√3 cleanly: numerator = 2/√3, denominator = 1 + 1/3 = 4/3!",
                "explanation": "(2/√3) ÷ (4/3) = (2/√3) × (3/4) = √3 / 2 = sin 60°."
            }
        ]
    },
    {
        "id": 11,
        "title": "Primary Cosine Identity",
        "subtitle": "Identities vs Conditional Equations + Pythagorean Proof of cos² A + sin² A = 1 (Section 8.4)",
        "speech": (
            "Welcome straight into the crown jewel algebraic section of Chapter Eight: Section Eight Point Four on Fundamental Trigonometric Identities! First clarify clearly what makes an equation wear the noble title IDENTITY! "
            "An ordinary algebraic equation (like two x equals ten) holds true ONLY for specific variable values, whereas a mathematical trigonometric IDENTITY is an equation involving trigonometric ratios of an angle that holds true for ALL allowable values of that acute angle! "
            "Let us prove our FIRST and most fundamental Pythagorean Identity inside right triangle ABC (right angled at B) using ONE magical division step! "
            "Start cleanly with plain Pythagoras Theorem inside right triangle ABC: AB squared plus BC squared equals AC squared! Now divide EVERY single squared term cleanly through by squared hypotenuse AC squared! "
            "Look carefully at what lands immediately: (AB over AC) whole squared plus (BC over AC) whole squared equals (AC over AC) whole squared! Recognize each ratio inside parentheses right away! Ratio AB over AC is simply cosine A, while ratio BC over AC is simply sine A! "
            "That proves cosine squared A plus sine squared A equals ONE, which also holds completely true at boundary endpoints zero degrees and ninety degrees!"
        ),
        "checkpoints": [
            {
                "question": "How is the primary trigonometric identity cos² A + sin² A = 1 proved directly in NCERT Section 8.4?",
                "options": [
                    "By dividing Pythagoras Theorem (AB² + BC² = AC²) on both sides by AC²",
                    "By assuming A = 45° only",
                    "By dividing AB² + BC² = AC² by AB²",
                    "By multiplying sin A and cos A together"
                ],
                "answer": 0,
                "hint": "(AB/AC)² + (BC/AC)² equals which two squared ratios?",
                "explanation": "Dividing AB² + BC² = AC² by AC² gives (AB/AC)² + (BC/AC)² = 1 ⟹ cos² A + sin² A = 1 (valid for 0° ≤ A ≤ 90°)."
            },
            {
                "question": "Using cos² A + sin² A = 1, how can cos A be written purely in terms of sin A for an acute/right angle 0° ≤ A ≤ 90°?",
                "options": [
                    "cos A = √(1 − sin² A)   (positive root since cos A ≥ 0 for 0° ≤ A ≤ 90°)",
                    "cos A = 1 − sin A",
                    "cos A = √(1 + sin² A)",
                    "cos A = 1 / sin A"
                ],
                "answer": 0,
                "hint": "Subtract sin² A cleanly to get cos² A = 1 − sin² A, then take non-negative square root!",
                "explanation": "For 0° ≤ A ≤ 90°, cos A ≥ 0, so cos² A = 1 − sin² A yields cos A = +√(1 − sin² A)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Secondary Trig Identities",
        "subtitle": "Pythagorean Proofs of 1 + tan² A = sec² A & cot² A + 1 = cosec² A With Angle Domains",
        "speech": (
            "Now repeat that EXACT same Pythagoras division trick TWO MORE TIMES cleanly to unlock our second and third Fundamental Trigonometric Identities! "
            "Keep Pythagoras Theorem AB squared plus BC squared equals AC squared written right on top of your notebook page! "
            "For Identity Two, instead of dividing by hypotenuse AC squared, divide EVERY single term cleanly by adjacent horizontal leg AB squared! Immediately AB squared over AB squared becomes crisp ONE! Next, (BC over AB) whole squared equals tangent squared A! Finally, (AC over AB) whole squared equals secant squared A! "
            "Thus ONE plus tangent squared A equals secant squared A, valid strictly for angles between zero and strictly below ninety degrees so leg AB never vanishes! "
            "For Identity Three, divide Pythagoras AB squared plus BC squared equals AC squared cleanly by opposite leg BC squared, valid strictly above zero degrees up to ninety degrees! Immediately (AB over BC) whole squared becomes cotangent squared A, giving cotangent squared A plus ONE equals cosecant squared A! "
            "Bonus algebraic factoring weapon: rewrite secant squared A minus tangent squared A equals one smoothly into difference of squares (sec A + tan A)(sec A − tan A) equals exact ONE!"
        ),
        "checkpoints": [
            {
                "question": "Evaluate 9 sec² A − 9 tan² A (Exercise 8.3 Q3 i) immediately using Identity 2:",
                "options": [
                    "9   [since 9(sec² A − tan² A) = 9 × 1]",
                    "1",
                    "0",
                    "8"
                ],
                "answer": 0,
                "hint": "Factor out common 9 and rearrange 1 + tan² A = sec² A!",
                "explanation": "1 + tan² A = sec² A ⟹ sec² A − tan² A = 1 ⟹ 9(sec² A − tan² A) = 9(1) = 9."
            },
            {
                "question": "For which angles in [0°, 90°] is the identity 1 + tan² A = sec² A strictly valid (avoiding undefined division by zero)?",
                "options": [
                    "0° ≤ A < 90°  (excludes A = 90° where cos A = 0 makes tan A & sec A undefined)",
                    "0° < A ≤ 90°",
                    "A = 90° only",
                    "Only A = 45°"
                ],
                "answer": 0,
                "hint": "Recall dividing by AB² requires AB ≠ 0, and cos A = 0 happens at A = 90°!",
                "explanation": "Both tan 90° and sec 90° involve division by cos 90° = 0, so 1 + tan² A = sec² A holds for 0° ≤ A < 90°."
            }
        ]
    },
    {
        "id": 13,
        "title": "Converting Trig Ratios",
        "subtitle": "Expressing cos A, tan A, sec A, cosec A & cot A Cleanly in Terms of sin A (Example 9 & Ex 8.3)",
        "speech": (
            "Master Textbook Example Nine and Exercise Eight Point Three Question One: How do we express EVERY trigonometric ratio purely in terms of JUST ONE single chosen ratio, like expressing cosine A, tangent A, and secant A strictly in terms of sine A? "
            "Follow this clean three-step conversion chain without memorizing separate clutter! Step One: grab Identity One (cosine squared A plus sine squared A equals one) to convert cosine A directly into positive square root of (1 minus sine squared A) for acute angle A! "
            "Step Two: apply Quotient Law for tangent A equals sine A divided by cosine A! Substituting our root expression for cosine A gives tangent A equals sine A divided by square root of (1 minus sine squared A)! "
            "Step Three: flip reciprocal partners cleanly! Secant A equals one divided by cosine A equals one over square root of (1 minus sine squared A), while cosecant A is already simply one over sine A! "
            "The exact same systematic strategy crushes Exercise Eight Point Three Question One cleanly: convert secant A into cotangent A via sec A equals root of (1 + tan squared A), rewriting tan A as 1 over cot A to reach root of (cot squared A + 1) over cot A!"
        ),
        "checkpoints": [
            {
                "question": "Which expression expresses sec A purely in terms of sin A for an acute angle 0° ≤ A < 90°?",
                "options": [
                    "1 / √(1 − sin² A)",
                    "√(1 − sin² A)",
                    "sin A / √(1 − sin² A)",
                    "√(1 + sin² A)"
                ],
                "answer": 0,
                "hint": "Combine sec A = 1 / cos A with cos A = √(1 − sin² A)!",
                "explanation": "Since sec A = 1/cos A and cos A = √(1 − sin² A), sec A = 1 / √(1 − sin² A)."
            },
            {
                "question": "Express sin A strictly in terms of cot A (Exercise 8.3 Q1):",
                "options": [
                    "1 / √(1 + cot² A)   (since cosec² A = 1 + cot² A and sin A = 1 / cosec A)",
                    "√(1 + cot² A)",
                    "cot A / √(1 + cot² A)",
                    "√(cot² A − 1)"
                ],
                "answer": 0,
                "hint": "Use Identity 3 (1 + cot² A = cosec² A) and take the reciprocal of cosec A!",
                "explanation": "cosec A = √(1 + cot² A) for acute A, so sin A = 1 / cosec A = 1 / √(1 + cot² A)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Rationalizing Square Roots",
        "subtitle": "Identity Proof Strategy I: Removing Radicals With Conjugates & Sine-Cosine Conversion (Ex 8.3 Q4)",
        "speech": (
            "Every single time a board exam proof in Exercise Eight Point Three confronts you with square roots or tangled fractions, unlock BOTH Strategy One tools right away! "
            "Tool A (Conjugate Multiplication for Radicals, Exercise 8.3 Q4 part vi): Prove square root of (1 plus sine A) divided by (1 minus sine A) equals secant A plus tangent A! "
            "Inside the square root sign, multiply BOTH numerator and denominator cleanly by the denominator's positive algebraic CONJUGATE (1 plus sine A)! Look how smoothly algebra unfolds: top becomes (1 plus sine A) whole squared, while bottom becomes (1 minus sine squared A) equals cosine squared A! "
            "Taking positive square root wipes out the radical sign completely into (1 plus sine A) over cosine A, splitting smoothly into one over cosine A plus sine A over cosine A, which simplifies identically to secant A plus tangent A! "
            "Tool B, Convert Everything cleanly to Sine and Cosine: To evaluate (1 + tan theta + sec theta)(1 + cot theta − cosec theta) in Question Three part two, rewrite tangent, secant, cotangent, and cosecant as clean fractions over cosine and sine so difference of squares simplifies straight to crisp TWO!"
        ),
        "checkpoints": [
            {
                "question": "How is the radical √[(1 + sin A) / (1 − sin A)] simplified cleanly to prove it equals sec A + tan A (Ex 8.3 Q4 vi)?",
                "options": [
                    "Multiply numerator & denominator inside the root by conjugate (1 + sin A), turning denominator into 1 − sin² A = cos² A",
                    "Square root both 1 and sin A separately",
                    "Cancel sin A cleanly from top and bottom",
                    "Multiply only by cos A"
                ],
                "answer": 0,
                "hint": "Using (1 − sin A)(1 + sin A) = 1 − sin² A creates a perfect square cos² A under the root!",
                "explanation": "Multiplying by (1+sin A)/(1+sin A) gives √[(1+sin A)² / cos² A] = (1+sin A)/cos A = sec A + tan A."
            },
            {
                "question": "Evaluate (1 + tan θ + sec θ)(1 + cot θ − cosec θ) (Exercise 8.3 Q3 ii):",
                "options": [
                    "2",
                    "1",
                    "0",
                    "−1"
                ],
                "answer": 0,
                "hint": "Convert to sin/cos: [(cos θ + sin θ + 1)/cos θ] × [(sin θ + cos θ − 1)/sin θ], then apply (a+b)(a−b)!",
                "explanation": "Numerator = (sin θ + cos θ)² − 1 = (1 + 2 sin θ cos θ) − 1 = 2 sin θ cos θ; dividing by sin θ cos θ yields 2!"
            }
        ]
    },
    {
        "id": 15,
        "title": "Difference Squares Proofs",
        "subtitle": "Advanced Ex 8.3 Proofs: Substituting 1 = cosec² A − cot² A (Q4 v) & Quotient Powers (Q4 x)",
        "speech": (
            "Now conquer the trickiest algebraic proof across the entire Chapter Eight board syllabus—Exercise Eight Point Three Question Four part five (matching Textbook Example Twelve)! "
            "Prove cleanly that (cosine A minus sine A plus one) divided by (cosine A plus sine A minus one) equals cosecant A plus cotangent A, using identity cosecant squared A equals one plus cotangent squared A! "
            "Follow this unforgettable three step proof playbook! Step One: notice our target right hand side contains cosecant and cotangent, NOT sine and cosine! So immediately divide EVERY term inside BOTH numerator and denominator cleanly by sine A! That converts the fraction smoothly into (cot A minus 1 plus cosec A) divided by (cot A plus 1 minus cosec A)! "
            "Step Two: NEVER modify the denominator at all! Replace ONLY the number ONE sitting inside the NUMERATOR with (cosecant squared A minus cotangent squared A), factoring cleanly via difference of squares as (cosec A + cot A)(cosec A − cot A)! "
            "Step Three: factor out common multiplier (cosec A + cot A), leaving bracket (1 − cosec A + cot A) on top which cancels the bottom denominator identically, leaving pure cosec A + cot A!"
        ),
        "checkpoints": [
            {
                "question": "In proving (cos A − sin A + 1) / (cos A + sin A − 1) = cosec A + cot A (Ex 8.3 Q4 v), what is the CRITICAL Step 1 conversion?",
                "options": [
                    "Divide every term of BOTH numerator and denominator by sin A to switch into cot A and cosec A",
                    "Divide top and bottom by cos A",
                    "Multiply top and bottom by sin A",
                    "Replace 1 with sin² A − cos² A"
                ],
                "answer": 0,
                "hint": "cos A / sin A = cot A and 1 / sin A = cosec A match the target RHS!",
                "explanation": "Dividing top & bottom by sin A turns the fraction into (cot A − 1 + cosec A)/(cot A + 1 − cosec A)."
            },
            {
                "question": "Simplify (1 + tan² A) / (1 + cot² A) (Exercise 8.3 Q4 x):",
                "options": [
                    "tan² A   (since numerator = sec² A = 1/cos² A and denominator = cosec² A = 1/sin² A)",
                    "cot² A",
                    "1",
                    "sec² A"
                ],
                "answer": 0,
                "hint": "Replace 1 + tan² A with sec² A and 1 + cot² A with cosec² A, then convert to sin/cos!",
                "explanation": "sec² A / cosec² A = (1 / cos² A) ÷ (1 / sin² A) = sin² A / cos² A = tan² A."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Eight Summary",
        "subtitle": "Complete Synthesis: 6 Ratios, Scale Invariance, Table 8.1 Values, Bounds & 3 Identities",
        "speech": (
            "Congratulations, keen trigonometry scholars! You have now mastered every single definition, geometric angle value derivation, extreme boundary limit, and algebraic identity proof across NCERT Class Ten Chapter Eight! Snapshot all five golden takeaways onto one crystal clear summary sheet before tackling our Interactive Exercises! "
            "One: For acute angle A in right triangle ABC, define sine (Opposite over Hypotenuse), cosine (Adjacent over Hypotenuse), tangent (Opposite over Adjacent), plus their reciprocals cosecant, secant, and cotangent! Remember switching angle perspective A to C swaps Opposite and Adjacent! "
            "Two: By AA Similarity, trigonometric ratios depend strictly on angle measure, never triangle scale size, with strict bounds sine A at most one and cosine A at most one! Three: Always apply quotient law tangent A equals sine A divided by cosine A! "
            "Four: Reconstruct all thirty Table Eight Point One standard values across 0, 30, 45, 60, and 90 degrees instantly using square roots of 0, 1, 2, 3, and 4 divided by 2! "
            "Five: Lock down all three Pythagorean Identities cleanly: cosine squared plus sine squared equals one, one plus tangent squared equals secant squared, and cotangent squared plus one equals cosecant squared! Now solve Exercises 8.1 through 8.3 confidently!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement below is 100% mathematically accurate across NCERT Chapter 8?",
                "options": [
                    "cos² A + sin² A = 1 (0° ≤ A ≤ 90°); 1 + tan² A = sec² A (0° ≤ A < 90°); cot² A + 1 = cosec² A (0° < A ≤ 90°)",
                    "sin(A + B) always equals sin A + sin B",
                    "Value of tan A is always strictly less than 1",
                    "cos A increases from 0 to 1 as A goes from 0° to 90°"
                ],
                "answer": 0,
                "hint": "Verify domains of all 3 Pythagorean identities carefully against division by zero!",
                "explanation": "Option 1 states all three Pythagorean identities along with their exact valid angle domains."
            },
            {
                "question": "Simplify (sec A + tan A)(1 − sin A) (Exercise 8.3 Q3 iii):",
                "options": [
                    "cos A",
                    "sec A",
                    "sin A",
                    "cosec A"
                ],
                "answer": 0,
                "hint": "Rewrite sec A + tan A as (1 + sin A) / cos A, then multiply by (1 − sin A)!",
                "explanation": "[(1 + sin A)/cos A](1 − sin A) = (1 − sin² A)/cos A = cos² A / cos A = cos A."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch8 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

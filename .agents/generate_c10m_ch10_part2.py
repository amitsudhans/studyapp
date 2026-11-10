#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 10: Circles
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
        "title": "Tangent Chord Triangle",
        "subtitle": "Example 3: Solving TP = 20/3 cm Using Right Triangle Bisection & AA Similarity (△TPR ~ △PRO)",
        "speech": (
            "Now solve Textbook Example Three—blending Chapter Six AA Similarity seamlessly with Chapter Ten Tangents! Read carefully: PQ is a chord of length eight centimeters inside a circle of radius five centimeters! Tangents at P and Q intersect at external point T! Find tangent length TP! "
            "Join center O to T, intersecting chord PQ at point R! By Theorem Ten Point Two symmetry, line OT bisects angle PTQ and acts as the perpendicular bisector of chord PQ! Therefore PR equals half of eight equals FOUR centimeters with right angle ORP equals ninety degrees! "
            "Step One: Inside small inner right triangle ORP, hypotenuse OP equals five centimeters and leg PR equals four centimeters! Immediately Pythagoras gives inner segment OR equals three centimeters! "
            "Step Two: Compare right triangle TRP (angled at R) against large right triangle TPO (angled at P by Theorem Ten Point One)! Both triangles share acute angle PTR AND hold ninety degree corners, making triangle TRP strictly similar to triangle TPO by AA Similarity! "
            "Setting corresponding side ratio TP over PO equals RP over RO cleanly gives TP divided by five equals four divided by three, yielding exact tangent length TP equals twenty over three centimeters!"
        ),
        "checkpoints": [
            {
                "question": "In Textbook Example 3 (radius OP = 5 cm, chord PQ = 8 cm), find length TP cleanly:",
                "options": [
                    "20/3 cm",
                    "15/4 cm",
                    "4 cm",
                    "25/3 cm"
                ],
                "answer": 0,
                "hint": "Find OR = 3 cm first; then △TRP ~ △TPO (or △TRP ~ △PRO!) gives TP / OP = PR / OR = 4 / 3!",
                "explanation": "PR = 4 cm, OR = 3 cm; AA similarity TP/5 = 4/3 gives TP = 20/3 cm."
            },
            {
                "question": "Why does line OT bisect chord PQ perpendicularly at R in Example 3?",
                "options": [
                    "Because △TPQ is isosceles (TP = TQ) and OT bisects apex angle ∠PTQ (by Theorem 10.2), hence OT is perpendicular bisector of PQ",
                    "Because T always sits inside the circle",
                    "Because PQ equals diameter 10 cm",
                    "Because ∠OPT = 60°"
                ],
                "answer": 0,
                "hint": "An angle bisector from the apex of an isosceles triangle bisects the opposite base at 90°!",
                "explanation": "Theorem 10.2 makes △TPQ isosceles with OT bisecting ∠PTQ ⟹ OT ⊥ PQ and PR = RQ = 4 cm."
            }
        ]
    },
    {
        "id": 10,
        "title": "Tangent Angle Sums",
        "subtitle": "Kite Quadrilateral Supplementary Angles (∠AOB + ∠APB = 180°) Solving Ex 10.2 Q2, Q3 & Q10",
        "speech": (
            "Spot ONE lightning fast angle shortcut inside EVERY two tangent kite quadrilateral OAPB (with external tangents PA and PB meeting smoothly at external point P): inspect ALL FOUR interior corner angles carefully! "
            "Corner A, meaning angle OAP, equals exact ninety degrees by Theorem Ten Point One! Corner B, meaning angle OBP, ALSO equals exact ninety degrees! Since ALL four interior angles of ANY closed quadrilateral always sum to three hundred sixty degrees, subtracting ninety plus ninety equals one hundred eighty leaves the remaining opposite angle pair strictly SUPPLEMENTARY: central angle AOB plus external angle APB ALWAYS equals exact ONE HUNDRED EIGHTY DEGREES! "
            "That clean angle proof solves Exercise Ten Point Two Question Ten directly AND cracks Questions Two and Three effortlessly in just two quick seconds! "
            "Check Question Two cleanly: given central angle POQ equals one hundred ten degrees, opposite external angle PTQ equals 180 minus 110 equals exact SEVENTY DEGREES in total! "
            "Check Question Three carefully: given full external angle APB between the two tangents equals eighty degrees! Because line OP cleanly bisects angle APB into forty degrees each, inside right triangle OAP, half central angle POA equals ninety minus forty equals exact FIFTY DEGREES!"
        ),
        "checkpoints": [
            {
                "question": "If tangents PA and PB from point P to a circle with center O are inclined to each other at angle 80° (Ex 10.2 Q3), find ∠POA:",
                "options": [
                    "50°",
                    "80°",
                    "60°",
                    "40°"
                ],
                "answer": 0,
                "hint": "Full central angle ∠AOB = 180° − 80° = 100°, and OP bisects ∠AOB evenly in half!",
                "explanation": "∠AOB = 180° − 80° = 100°; by Theorem 10.2 OP bisects ∠AOB ⟹ ∠POA = 50°."
            },
            {
                "question": "If TP and TQ are tangents so that ∠POQ = 110° (Ex 10.2 Q2), find ∠PTQ:",
                "options": [
                    "70°",
                    "60°",
                    "80°",
                    "90°"
                ],
                "answer": 0,
                "hint": "Opposite angles ∠POQ and ∠PTQ in tangent kite OPTQ sum to 180°!",
                "explanation": "180° − 110° = 70° cleanly."
            }
        ]
    },
    {
        "id": 11,
        "title": "Parallel Diameter Tangents",
        "subtitle": "Ex 10.2 Q4 (Diameter Endpoint Tangents ∥) & Q5 (Normal at Contact Point Passes Through O)",
        "speech": (
            "Now solve two crystal clear board geometry proofs from Exercise Ten Point Two cleanly: Questions Four and Five! "
            "Proof One from Question Four: Prove strictly using Theorem Ten Point One that two tangents drawn at the TWO opposite ends of ANY circle diameter AB are strictly PARALLEL to each other! "
            "Label top tangent line PQ touching diameter top endpoint A, and bottom tangent line RS touching diameter bottom endpoint B! Since diameter AB passes straight through circle center O, BOTH OA and OB are circle radii! By Theorem Ten Point One, top angle OAP equals ninety degrees AND bottom angle OBS equals ninety degrees! "
            "Look closely at angles PAB and ABS formed along straight transversal AB: BOTH equal ninety degrees, making ALTERNATE INTERIOR ANGLES strictly EQUAL! Equal alternate interior angles guarantee top tangent PQ runs strictly PARALLEL to bottom tangent RS! "
            "Proof Two from Question Five: Prove cleanly by logical contradiction that any perpendicular line drawn straight to tangent AB at exact point of contact P MUST pass straight through center O! Assuming another ray O prime P perpendicular to AB creates two unequal ninety degree right angles on the exact same side—geometrically totally impossible!"
        ),
        "checkpoints": [
            {
                "question": "In Exercise 10.2 Q4, how do we prove that tangents PQ and RS drawn at opposite endpoints A and B of a diameter are parallel?",
                "options": [
                    "Theorem 10.1 makes ∠OAP = 90° and ∠OBS = 90°, so equal alternate interior angles along diameter transversal AB prove PQ ∥ RS",
                    "By assuming PQ ∥ RS beforehand",
                    "Using SSS Congruence",
                    "Because AB = 2r"
                ],
                "answer": 0,
                "hint": "Diameter AB serves as a straight transversal between PQ and RS with both Z-angles equal to 90°!",
                "explanation": "∠PAB = ∠ABS = 90° gives equal alternate interior angles, proving PQ ∥ RS."
            },
            {
                "question": "In proving Exercise 10.2 Q5 (perpendicular at contact P passes through center O), what contradiction finishes the proof?",
                "options": [
                    "If another perpendicular O'P ≠ OP existed, then ∠O'PB = ∠OPB = 90°, which is impossible unless O'P and OP coincide along the same line",
                    "Diameter would equal zero",
                    "Tangent would have length 0",
                    "Circle center would move outside"
                ],
                "answer": 0,
                "hint": "Two distinct rays at P cannot both make 90° with tangent AB on the same side!",
                "explanation": "Theorem 10.1 guarantees ∠OPB = 90°; assuming ∠O'PB = 90° on the same side forces O'P to coincide with OP."
            }
        ]
    },
    {
        "id": 12,
        "title": "Circumscribed Quadrilateral Law",
        "subtitle": "Exercise 10.2 Q8: Proving Opposite Sides of Circumscribed Quadrilateral Sum Equally (AB + CD = AD + BC)",
        "speech": (
            "Master one of NCERT Class Ten's most beloved theorems—Exercise Ten Point Two Question Eight! A quadrilateral ABCD is drawn carefully OUTSIDE a circle so ALL FOUR sides touch the circle cleanly at contact points P, Q, R, and S! Prove that opposite side sums match identically: AB plus CD equals AD plus BC! "
            "Pause and watch how effortlessly Theorem Ten Point Two solves this without writing a single angle equation! Look at ALL FOUR external corners A, B, C, and D! Each corner fires TWO equal tangent segments onto the circle! "
            "Pair them carefully so the LEFT side of EVERY equation cleanly builds segments lying along sides AB and CD: Corner A gives AP equals AS! Corner B gives BP equals BQ! Corner C gives CR equals CQ! Corner D gives DR equals DS! "
            "Now simply ADD all four tangent equations vertically together! On the LEFT hand side, (AP plus BP) glues smoothly into full edge AB, while (CR plus DR) glues smoothly into opposite edge CD! On the RIGHT hand side, (AS plus DS) equals side AD and (BQ plus CQ) equals side BC! Thus opposite sum AB plus CD equals AD plus BC cleanly!"
        ),
        "checkpoints": [
            {
                "question": "A quadrilateral ABCD is drawn to circumscribe a circle (Ex 10.2 Q8). If AB = 6 cm, BC = 7 cm, and CD = 4 cm, find AD:",
                "options": [
                    "3 cm",
                    "5 cm",
                    "7 cm",
                    "9 cm"
                ],
                "answer": 0,
                "hint": "Apply AB + CD = AD + BC ⟹ 6 + 4 = AD + 7!",
                "explanation": "Opposite sides sum equally: 6 + 4 = AD + 7 ⟹ 10 = AD + 7 ⟹ AD = 3 cm."
            },
            {
                "question": "Which critical alignment makes the proof of AB + CD = AD + BC work cleanly in Exercise 10.2 Q8?",
                "options": [
                    "Writing Theorem 10.2 equations with AB-pieces and CD-pieces ALL placed on the LHS (AP=AS, BP=BQ, CR=CQ, DR=DS) before adding vertically",
                    "Putting all segments randomly on either side",
                    "Assuming ABCD is a square first",
                    "Using area ratios"
                ],
                "answer": 0,
                "hint": "Keep segments that sum to AB and CD on the left, and segments that sum to AD and BC on the right!",
                "explanation": "(AP+BP) + (CR+DR) = AB + CD equals (AS+DS) + (BQ+CQ) = AD + BC directly by Theorem 10.2."
            }
        ]
    },
    {
        "id": 13,
        "title": "Parallelogram Becomes Rhombus",
        "subtitle": "Exercise 10.2 Q11 (Circumscribed Parallelogram = Rhombus) & Q9 (Parallel Tangents ∠AOB = 90°)",
        "speech": (
            "Now put Question Eight straight to work solving Exercise Ten Point Two Questions Eleven and Nine cleanly! "
            "First tackle Question Eleven carefully: Prove rigorously that ANY PARALLELOGRAM circumscribing a circle MUST be a RHOMBUS! Write down the exact two geometric facts we know instantly right away: Fact One, since ABCD is a parallelogram, opposite sides are strictly EQUAL in length, meaning AB equals CD AND AD equals BC! "
            "Fact Two, since ABCD circumscribes a circle cleanly, Question Eight already guarantees AB plus CD equals AD plus BC! Substitute CD equals AB and BC equals AD straight into that sum equation: TWICE AB equals TWICE AD, dividing both sides by two leaves AB equals AD! Having all four adjacent and opposite edges strictly equal forces parallelogram ABCD to be a true RHOMBUS! "
            "Next crack Question Nine smoothly! Parallel tangents XY at point P and X prime Y prime at point Q are cut cleanly by tangent AB touching at contact point C! Join center lines OA, OC, and OB! Theorem Ten Point Two makes OA bisect angle PAC and OB bisect angle QBC cleanly, giving half co-interior angle sum ninety degrees, forcing angle AOB equals ninety degrees!"
        ),
        "checkpoints": [
            {
                "question": "How does Question 8 (AB + CD = AD + BC) prove that a parallelogram circumscribing a circle MUST be a rhombus (Ex 10.2 Q11)?",
                "options": [
                    "Parallelogram opposite sides give AB = CD and BC = AD ⟹ substituting yields 2 AB = 2 AD ⟹ AB = AD (all 4 sides equal ⟹ Rhombus)",
                    "Because parallelogram angles all equal 90°",
                    "Because tangents bisect diagonals",
                    "Because circle diameter equals perimeter"
                ],
                "answer": 0,
                "hint": "Combine opposite-side equality (AB = CD, AD = BC) with circumscribed sum equality AB + CD = AD + BC!",
                "explanation": "AB + AB = AD + AD forces AB = AD, making all four sides equal ⟹ Rhombus."
            },
            {
                "question": "In Ex 10.2 Q9, parallel tangents XY (at P) and X'Y' (at Q) are cut by tangent AB touching circle at C. What MUST ∠AOB equal?",
                "options": [
                    "90°",
                    "60°",
                    "120°",
                    "180°"
                ],
                "answer": 0,
                "hint": "Co-interior angles ∠PAC + ∠QBC = 180°; OA & OB bisect them so ∠OAB + ∠OBA = 90° ⟹ ∠AOB = ?",
                "explanation": "By RHS congruence OA and OB bisect ∠PAC and ∠QBC: ½(180°) = 90° = ∠OAB + ∠OBA, leaving ∠AOB = 180° − 90° = 90°."
            }
        ]
    },
    {
        "id": 14,
        "title": "Opposite Sides Supplementary",
        "subtitle": "Exercise 10.2 Q13: Proving Opposite Sides Subtend Supplementary Central Angles (180°)",
        "speech": (
            "Conquer the final geometric theorem in Exercise Ten Point Two, Question Thirteen! Read cleanly: Prove that OPPOSITE sides of a quadrilateral circumscribing a circle subtend SUPPLEMENTARY angles at the center of the circle! "
            "Draw quadrilateral ABCD touching the circle cleanly at P, Q, R, and S! Connect center O straight to ALL four outer corners A, B, C, D AND to ALL four contact points P, Q, R, S! That divides the full 360 degree space around center O neatly into EIGHT small central angles numbered 1 through 8 clockwise! "
            "Look back straight at Theorem Ten Point Two! Earlier we noticed external tangents from corner A form right triangle OAP congruent to triangle OAS by SSS or RHS congruence! Therefore central angles sitting across adjacent tangent segments from the SAME corner are ALWAYS equal: angle 1 equals angle 8, angle 2 equals angle 3, angle 4 equals angle 5, and angle 6 equals angle 7! "
            "Add all eight numbered angles smoothly around center O: twice (angle 1 plus angle 2 plus angle 5 plus angle 6) equals 360 degrees, so dividing by two groups cleanly into angle AOB plus angle COD equals ONE HUNDRED EIGHTY DEGREES!"
        ),
        "checkpoints": [
            {
                "question": "In Exercise 10.2 Q13, if side AB of a circumscribed quadrilateral ABCD subtends ∠AOB = 115° at center O, what angle does opposite side CD subtend at O?",
                "options": [
                    "65°   (since opposite sides subtend supplementary 180° angles)",
                    "115°",
                    "90°",
                    "180°"
                ],
                "answer": 0,
                "hint": "Use ∠AOB + ∠COD = 180°!",
                "explanation": "180° − 115° = 65°."
            },
            {
                "question": "What congruence property around center O lets us pair the 8 central angles into 4 equal pairs in Question 13?",
                "options": [
                    "Each external corner (A, B, C, D) forms two congruent right triangles to adjacent contact points (e.g. △OAP ≅ △OAS), making ∠AOP = ∠AOS",
                    "All 8 central angles equal 45° each",
                    "Diagonals AC and BD are perpendicular",
                    "Opposite edges are parallel"
                ],
                "answer": 0,
                "hint": "Recall the angle-bisector bonus of Theorem 10.2 around center O!",
                "explanation": "Theorem 10.2 symmetry pairs adjacent central angles from each vertex cleanly, halving 360° into ∠AOB + ∠COD = 180°."
            }
        ]
    },
    {
        "id": 15,
        "title": "Triangle Circumscribing Circle",
        "subtitle": "Exercise 10.2 Q12 Flagship: Finding Sides AB = 15 cm & AC = 13 cm Given r = 4 cm, BD = 8, DC = 6",
        "speech": (
            "Now tackle NCERT Class Ten's most famous multi-concept masterpiece—Exercise Ten Point Two Question Twelve! "
            "A triangle ABC is drawn circumscribing a circle of radius four centimeters such that bottom contact point D splits side BC cleanly into segments BD equal to eight centimeters and DC equal to six centimeters! Find unknown side lengths AB and AC! "
            "Step One (Theorem 10.2 Tangents): Label touching points E on AC and F on AB! Immediately from corners B and C, BF equals BD equals eight centimeters AND CE equals DC equals six centimeters! Let top equal pair AF equals AE equal x centimeters! Thus sides are: a = 14, b = x + 6, and c = x + 8! "
            "Step Two (Dual Area Formula Link!): First compute semi perimeter s equals (14 + x + 6 + x + 8) divided by 2 equals x + 14! Write total Area of triangle ABC in TWO ways! Way One (Heron's Formula): square root of (x + 14)(x)(6)(8) equals root of 48x(x + 14)! Way Two (Three Radius-Base Triangles): s times r equals (x + 14) times 4! Squaring and matching solves x = 7 -> AC = 13 cm and AB = 15 cm!"
        ),
        "checkpoints": [
            {
                "question": "In Exercise 10.2 Q12 (circle radius r = 4 cm inscribed in △ABC with BD = 8 cm and DC = 6 cm), find unknown sides AC and AB:",
                "options": [
                    "AC = 13 cm  and  AB = 15 cm   (since top tangent segment x = 7 cm)",
                    "AC = 14 cm  and  AB = 16 cm",
                    "AC = 12 cm  and  AB = 14 cm",
                    "AC = 10 cm  and  AB = 12 cm"
                ],
                "answer": 0,
                "hint": "Equate Heron Area² = 48x(x+14) against [4(x+14)]² = 16(x+14)² ⟹ 3x = x + 14 ⟹ x = 7!",
                "explanation": "Solving 48x(x + 14) = 16(x + 14)² gives 3x = x + 14 ⟹ x = 7 cm; hence AC = 7+6 = 13 cm and AB = 7+8 = 15 cm."
            },
            {
                "question": "Why does dividing △ABC into three subtriangles △OBC, △OCA, and △OAB always produce Total Area = (1/2) × Perimeter × r = s · r?",
                "options": [
                    "Because by Theorem 10.1, ALL three inradii OD, OE, OF stand perpendicular (altitude = r) to bases a, b, c!",
                    "Because △ABC is equilateral",
                    "Because r equals half of BC",
                    "Because ∠A = 90° always"
                ],
                "answer": 0,
                "hint": "Compute ar(OBC) + ar(OCA) + ar(OAB) = ½ a·r + ½ b·r + ½ c·r!",
                "explanation": "Theorem 10.1 makes each radius r the exact altitude to each side, giving Total Area = ½(a + b + c)r = s · r."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Ten Summary",
        "subtitle": "Complete Section 10.4 Recap: Tangent Cases, Theorem 10.1, Theorem 10.2, Kite & Quadrilateral Laws",
        "speech": (
            "Bravo, master circle geometers! You have now mastered every single circle geometry definition, formal theorem proof, and challenging board rider inside NCERT Class Ten Chapter Ten on Circles! Snapshot all four golden chapter takeaways cleanly onto one concise revision card before attacking our forty Interactive Exercise Questions! "
            "One: A flat plane line intersects any circle cleanly in zero points (non-intersecting), two distinct points (secant), or one unique point (tangent at point of contact), with at most two parallel tangents pointing along any fixed compass direction. "
            "Two: Theorem Ten Point One guarantees rigorously that the tangent at any point of a circle stands strictly PERPENDICULAR to the radius drawn straight through the point of contact, defining the circle Normal line! "
            "Three: Zero tangents pass through an interior point, one passes smoothly through a boundary point, and exactly two equal tangent segments pass from any external point by Theorem Ten Point Two! "
            "Four: External tangent kite angles always sum cleanly to one hundred eighty degrees, external angle PTQ equals twice angle OPQ, and circumscribed quadrilaterals ALWAYS satisfy opposite edge sum AB + CD = AD + BC! Now go solve Exercises 10.1 and 10.2 with total confidence!"
        ),
        "checkpoints": [
            {
                "question": "Which Chapter 10 summary statement is 100% mathematically TRUE?",
                "options": [
                    "Tangent ⊥ radius at contact point (Theorem 10.1); external tangent segments are equal PQ = PR (Theorem 10.2); circumscribed quadrilateral satisfies AB + CD = AD + BC",
                    "Exactly two tangents can be drawn from a point INSIDE a circle",
                    "A tangent intersects a circle at two distinct points",
                    "Angles ∠AOB and ∠APB in a tangent kite are always complementary (sum 90°)"
                ],
                "answer": 0,
                "hint": "Check point-inside count (0), tangent intersection count (1), and kite sum (180°) carefully!",
                "explanation": "Option 1 combines Theorem 10.1, Theorem 10.2, and the circumscribed quadrilateral sum law without any errors."
            },
            {
                "question": "A right-angled triangle has legs a = 6 cm, b = 8 cm, and hypotenuse c = 10 cm with an inscribed circle of radius r. Using Area = s·r (or r = (a+b−c)/2), find r:",
                "options": [
                    "2 cm",
                    "3 cm",
                    "4 cm",
                    "1.5 cm"
                ],
                "answer": 0,
                "hint": "Area = ½ × 6 × 8 = 24 cm², semi-perimeter s = (6 + 8 + 10)/2 = 12 cm ⟹ r = 24 / 12!",
                "explanation": "r = Area / s = 24 / 12 = 2 cm (also matches tangent shortcut (6 + 8 − 10)/2 = 2 cm!)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch10 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

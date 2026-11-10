#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 10: Circles
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Lines And Circles",
        "subtitle": "Three Circle-Line Relationships (Non-Intersecting, Secant, Tangent) & Everyday Pulleys/Wheels (10.1)",
        "speech": (
            "Welcome, curious geometry explorers, to Class Ten Mathematics Chapter Ten on Circles! Begin right away by refreshing Class Nine's clean definition: a circle is the exact collection of ALL points inside a flat plane sitting at one exact fixed constant distance called radius r away from a fixed center point O! "
            "Now imagine drawing a circle alongside ANY straight line PQ in that same flat plane! Count how many ways they can meet! Look closely—strictly THREE distinct possibilities exist! "
            "Case One: A NON INTERSECTING LINE passes completely outside the circle rim with ZERO common shared points anywhere! Case Two: A SECANT slices straight across the circular interior, intersecting cleanly at TWO distinct boundary points A and B! Case Three: A TANGENT kisses the circle cleanly along its outer edge, intersecting at ONE AND ONLY ONE exact point! "
            "Spot real tangents moving quietly around everyday engineering machinery right now! Look at a circular pulley lifting heavy water buckets from a deep well: both taut straight rope strands glide smoothly as tangents touching the spinning circular pulley wheel! Or watch a rolling bicycle wheel meeting level flat road ground at exactly ONE contact point directly beneath its axle!"
        ),
        "checkpoints": [
            {
                "question": "In a flat plane, what are the THREE possible relationships between a circle and a straight line (Section 10.1)?",
                "options": [
                    "Non-intersecting (0 common points), Secant (2 common points), and Tangent (1 common point)",
                    "Only intersecting at 3 points or 0 points",
                    "Secant (1 point) and Chord (0 points)",
                    "Parallel (2 points) and Tangent (3 points)"
                ],
                "answer": 0,
                "hint": "Count the exact number of intersection points possible: 0, 2, or 1!",
                "explanation": "A line meets a circle in 0 points (non-intersecting), 2 points (secant), or exactly 1 point (tangent)."
            },
            {
                "question": "Which everyday physical object demonstrates a tangent touching a circle at a single point of contact?",
                "options": [
                    "A taut rope pulled over a circular pulley, or a bicycle wheel rolling on flat ground",
                    "Two concentric circular rings",
                    "Spokes radiating from hub to rim",
                    "A diameter slicing through the center"
                ],
                "answer": 0,
                "hint": "Notice where a flat level road or straight pulley belt grazes the outer rim cleanly!",
                "explanation": "The level road meets a rolling wheel at one single point of contact, acting as a geometric tangent."
            }
        ]
    },
    {
        "id": 2,
        "title": "Tangent Limiting Secant",
        "subtitle": "Point of Contact, Rotating Secant Activity & Two Parallel Tangents Limit (Section 10.2)",
        "speech": (
            "Zoom sharply onto the star concept of Section Ten Point Two: the TANGENT to a circle! Derived from the Latin word tangere meaning 'to touch', a tangent touches a circle at ONE single unique point called the POINT OF CONTACT! "
            "Perform a super visual mental activity to understand clearly WHY a tangent behaves like a close cousin of a secant! Picture a straight wire pivoted at point P on a circle, slicing across the rim as a secant PQ! Hold point P fixed and slowly rotate the wire clockwise! "
            "Watch carefully what happens to second intersection point Q: point Q glides steadily closer and closer along the curved circular rim toward fixed point P! At ONE magical instant, point Q lands right on top of P so both chord endpoints A and B COINCIDE completely into ONE single shared point! "
            "That beautiful geometry visualization proves our core NCERT insight cleanly: a tangent is simply a special limiting case of a secant whenever both distinct endpoints of its corresponding circular chord coincide completely! Plus remember cleanly from Exercise Ten Point One: any circle can hold AT MOST TWO parallel tangents pointing along any fixed straight direction!"
        ),
        "checkpoints": [
            {
                "question": "How is a tangent defined as a special limiting case of a secant (Section 10.2)?",
                "options": [
                    "When the two endpoints of the secant's corresponding chord COINCIDE into a single point of contact",
                    "When the secant passes directly through the center O",
                    "When the secant moves infinitely far outside the circle",
                    "When chord length equals diameter 2r"
                ],
                "answer": 0,
                "hint": "Rotate a secant about point P until second intersection Q merges smoothly into P!",
                "explanation": "As chord endpoints coalesce into one point, the secant turns into a tangent at that point of contact."
            },
            {
                "question": "How many parallel tangents can a circle have at most for a given fixed direction (Exercise 10.1 Q1)?",
                "options": [
                    "Two parallel tangents (sitting at opposite ends of one perpendicular diameter)",
                    "Only one tangent",
                    "Four parallel tangents",
                    "Infinitely many parallel tangents in the same direction"
                ],
                "answer": 0,
                "hint": "Slide a line smoothly across a circle keeping its slope fixed: where does it touch with only 1 point?",
                "explanation": "A circle has at most two parallel tangents in any single given direction (at opposite endpoints of a diameter)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Radius Perpendicular Tangent",
        "subtitle": "Theorem 10.1 Proof: Shortest Distance Forces Radius OP ⊥ Tangent XY at Contact Point P",
        "speech": (
            "Now master the very first pillar theorem of Chapter Ten: Theorem Ten Point One! Read its crisp statement carefully: The tangent at ANY point of a circle is STRICTLY PERPENDICULAR to the radius drawn through the point of contact! "
            "Consider a circle centered at O touched by tangent line XY at contact point P! We must prove radius OP is perpendicular to line XY! Watch how effortlessly this textbook proof works without needing heavy angle calculations! "
            "Pick ANY other point Q along tangent XY strictly different from P! Connect center O straight to Q! Now pause and ask: WHERE must point Q lie—inside the circle, on the circle, or strictly OUTSIDE? "
            "Because line XY is strictly a TANGENT touching the circle rim at ONLY ONE unique point P, point Q CANNOT touch or enter inside the circle (otherwise line XY would cut twice as a secant)! Thus every such point Q MUST lie strictly OUTSIDE the circle boundary! "
            "Therefore segment distance OQ MUST be strictly LONGER than circle radius OP for EVERY other point Q along line XY! Since the shortest distance from center O to line XY is always perpendicular, radius OP stands strictly perpendicular to XY!"
        ),
        "checkpoints": [
            {
                "question": "In proving Theorem 10.1 (OP ⊥ tangent XY), why is OQ > OP true for EVERY point Q ≠ P on tangent XY?",
                "options": [
                    "Because tangent XY meets the circle ONLY at P, so every other point Q lies strictly OUTSIDE the circle (distance > radius r)",
                    "Because Q lies inside the circle",
                    "Because ∠OPQ is assumed equal to 90° beforehand",
                    "Because PQ always equals radius OP"
                ],
                "answer": 0,
                "hint": "If Q lay inside the circle, tangent XY would have to intersect the rim twice as a secant!",
                "explanation": "Since Q ≠ P lies outside the circle, OQ > radius OP, making OP the shortest distance from O to XY (hence OP ⊥ XY)."
            },
            {
                "question": "A tangent PQ at point P of a circle of radius 5 cm meets a line through center O at Q so that OQ = 12 cm (Ex 10.1 Q3). Find length PQ:",
                "options": [
                    "√119 cm",
                    "13 cm",
                    "12 cm",
                    "8.5 cm"
                ],
                "answer": 0,
                "hint": "Theorem 10.1 makes ∠OPQ = 90°, so Hypotenuse is OQ = 12 cm (NOT PQ)!",
                "explanation": "By Pythagoras in right △OPQ (∠P = 90°), PQ = √(OQ² − OP²) = √(12² − 5²) = √(144 − 25) = √119 cm."
            }
        ]
    },
    {
        "id": 4,
        "title": "Normals And Uniqueness",
        "subtitle": "Uniqueness of Tangent at Point P, Normal Line Definition & Exercise 10.1 Numerical Applications",
        "speech": (
            "Lock in TWO super important geometry remarks flowing straight out of Theorem Ten Point One alongside classic Exercise Ten Point One tangent length calculations! "
            "Remark One covers Uniqueness of Tangent: at any single given point P ON a circle boundary, how many tangent lines can possibly exist? Only ONE AND EXACTLY ONE unique tangent! Why? Because through contact point P, Euclidean geometry allows strictly ONE straight line perpendicular to radius OP! Any slightly tilted line fails perpendicularity and slices back through the circle as a secant! "
            "Remark Two defines the circle NORMAL: the straight geometric line containing radius OP, passing strictly perpendicular to the tangent right through exact point of contact P, wears the classic mathematical title NORMAL to the circle at point P! "
            "Now solve Exercise Ten Point One tangent length calculations cleanly using Pythagoras Theorem! Remember strictly that the ninety degree right angle corner ALWAYS sits squarely at point of contact P, never at circle center O or external point Q! When tangent length PQ equals twenty four centimeters and distance OQ equals twenty five centimeters, hypotenuse OQ equals twenty five, giving exact circle radius square root of (625 minus 576) equals seven centimeters!"
        ),
        "checkpoints": [
            {
                "question": "What is the geometric definition of the 'Normal' to a circle at point of contact P (Section 10.2 Remark)?",
                "options": [
                    "The line passing through P perpendicular to the tangent (which always contains radius OP through center O)",
                    "A parallel chord not touching center O",
                    "Any line passing through an external point without touching the circle",
                    "The tangent itself"
                ],
                "answer": 0,
                "hint": "Theorem 10.1 proves the line containing radius OP stands strictly perpendicular to the tangent at P!",
                "explanation": "The line containing radius OP through contact point P is perpendicular to the tangent and is called the normal at P."
            },
            {
                "question": "From an external point Q, the tangent length to a circle is 24 cm and distance of Q from center O is 25 cm (Ex 10.2 Q1). Find radius r:",
                "options": [
                    "7 cm",
                    "12 cm",
                    "15 cm",
                    "24.5 cm"
                ],
                "answer": 0,
                "hint": "Right angle sits at tangent contact P, making OQ = 25 cm the Hypotenuse!",
                "explanation": "r = √(25² − 24²) = √(625 − 576) = √49 = 7 cm."
            }
        ]
    },
    {
        "id": 5,
        "title": "Tangents From Point",
        "subtitle": "Number of Tangents by Point Location (Inside=0, On=1, Outside=2) & Tangent Segment Length (10.3)",
        "speech": (
            "Now step boldly inside Section Ten Point Three! Pick ANY single point P anywhere inside the flat coordinate plane of a circle, and ask ONE crisp question: How many tangent lines can you draw passing straight through point P to touch the circle rim? Three completely different regions yield THREE exact geometric answers! "
            "Region One lies strictly INSIDE the circle boundary: draw ANY straight ray passing straight through interior point P in any compass direction you might choose! Every single line ALWAYS enters and exits the circular boundary at TWO separate spots as a cutting secant! Therefore ZERO tangents can ever pass through an interior point! "
            "Region Two sits directly ON the circle boundary: exactly ONE single unique tangent touches cleanly right at point P! "
            "Region Three sits strictly OUTSIDE the circle boundary: sketch both upper top and lower bottom tangent lines from external point P cleanly, giving EXACTLY TWO distinct tangents PT1 and PT2! "
            "Watch mathematical terminology very carefully! An entire tangent is an endless infinite straight line extending both ways forever, whereas LENGTH OF THE TANGENT specifically measures ONLY the finite segment PT measured straight from external point P cleanly to contact point T!"
        ),
        "checkpoints": [
            {
                "question": "How many tangents can be drawn to a circle passing through a point P depending on P's location (Section 10.3)?",
                "options": [
                    "Inside circle: 0 tangents  |  On circle: 1 tangent  |  Outside circle: exactly 2 tangents",
                    "Inside: 1  |  On: 2  |  Outside: infinite",
                    "Inside: 0  |  On: 2  |  Outside: 1",
                    "Always 2 regardless of location"
                ],
                "answer": 0,
                "hint": "Every line through an interior point hits the circle twice as a secant!",
                "explanation": "Interior points allow 0 tangents; boundary points allow 1 unique tangent; external points allow exactly 2 tangents."
            },
            {
                "question": "In Theorem 10.2, what does 'Length of a tangent from external point P' specifically denote?",
                "options": [
                    "The length of the finite segment PT from external point P to the point of contact T",
                    "The length of the infinite tangent line",
                    "The distance PO to the circle center",
                    "The arc length along the circle"
                ],
                "answer": 0,
                "hint": "Infinite lines have infinite length; 'length of tangent' measures between which two specific points?",
                "explanation": "Tangent length refers to segment PT connecting external point P to contact point T."
            }
        ]
    },
    {
        "id": 6,
        "title": "Equal Tangent Segments",
        "subtitle": "Theorem 10.2 RHS Congruence Proof: Tangents PQ = PR + Bisector ∠OPQ = ∠OPR",
        "speech": (
            "Now conquer the second grand pillar proof of Class Ten Chapter Ten: Theorem Ten Point Two! State this famous theorem loudly and cleanly right away: The lengths of TWO tangent segments drawn from an external point P to a circle are ALWAYS STRICTLY EQUAL! "
            "Consider external point P drawing two tangent rays PQ and PR touching a circle centered at O neatly at exact contact points Q and R! How do mathematicians prove segment PQ equals segment PR with complete certainty? "
            "Join circle radii OQ and OR smoothly, plus draw central connecting line segment OP! Look closely at the two resulting right angled triangles OQP and ORP inside our diagram! "
            "First, Theorem Ten Point One guarantees BOTH corner angles OQP and ORP equal ninety degree right angles! Second, hypotenuse OP is identically SHARED common to both right triangles! Third, radii OQ and OR hold identical fixed circle radius r! "
            "Therefore, by Class Nine RHS Congruence, right triangle OQP is strictly congruent to right triangle ORP! Instantly by corresponding parts CPCT, equal tangent segments PQ equals PR AND central connecting line OP bisects BOTH external angle QPR AND central angle QOR evenly right down the middle!"
        ),
        "checkpoints": [
            {
                "question": "Which Class 9 congruence criterion proves Theorem 10.2 (PQ = PR for two tangents from external point P)?",
                "options": [
                    "RHS Congruence (∠OQP = ∠ORP = 90°, shared Hypotenuse OP, equal radii OQ = OR)",
                    "AAA Congruence only",
                    "ASS Congruence without right angles",
                    "ASA without knowing radii"
                ],
                "answer": 0,
                "hint": "Right angle (90°) + shared Hypotenuse OP + equal Radii Side OQ = OR spells...",
                "explanation": "Right angles at Q & R (Theorem 10.1), common hypotenuse OP, and equal radii OQ = OR establish △OQP ≅ △ORP by RHS."
            },
            {
                "question": "What useful angle bonus follows immediately from △OQP ≅ △ORP by CPCT in Theorem 10.2?",
                "options": [
                    "Center line OP bisects BOTH the external angle ∠QPR and the central angle ∠QOR equally",
                    "∠QPR must always equal 90°",
                    "PQ + PR = OP always",
                    "QR always equals diameter 2r"
                ],
                "answer": 0,
                "hint": "Check corresponding angles ∠OPQ vs ∠OPR and ∠POQ vs ∠POR!",
                "explanation": "Congruence gives ∠OPQ = ∠OPR and ∠POQ = ∠POR, so OP lies right along the angle bisector of ∠QPR and ∠QOR."
            }
        ]
    },
    {
        "id": 7,
        "title": "Concentric Circles Chord",
        "subtitle": "Example 1 & Ex 10.2 Q7: Proving Outer Chord Touching Inner Circle Is Bisected at Contact Point P",
        "speech": (
            "Apply Theorem Ten Point One smoothly to TWO different circles sharing one identical common center O, known as Concentric Circles! Look closely at Textbook Example One alongside Exercise Ten Point Two Question Seven! "
            "Example One states carefully: Two concentric circles share common center point O! A straight chord AB of the LARGER outer circle touches the SMALLER inner circle tangentially at single contact point P! Prove cleanly that contact point P BISECTS outer chord AB into equal halves AP equals BP! "
            "This elegant geometric proof takes JUST TWO lines combining Class Ten with Class Nine geometry! Line One: Since AB touches the smaller circle strictly as a tangent at P, Theorem Ten Point One guarantees inner radius OP stands strictly PERPENDICULAR to chord AB! "
            "Line Two: Step back and view outer chord AB inside the LARGER outer circle! Class Nine's golden chord theorem states that a perpendicular drawn straight down from center O onto ANY chord ALWAYS bisects that chord cleanly! Hence AP equals BP! "
            "Test Exercise Question Seven numerically right now: outer circle radius five centimeters and inner circle radius three centimeters gives half chord root (25 minus 9) equals four, so full chord length equals eight centimeters!"
        ),
        "checkpoints": [
            {
                "question": "Two concentric circles have radii 5 cm and 3 cm (Exercise 10.2 Q7). Find the length of the chord of the larger circle which touches the smaller circle:",
                "options": [
                    "8 cm",
                    "4 cm",
                    "10 cm",
                    "6 cm"
                ],
                "answer": 0,
                "hint": "OP = 3 cm ⊥ AB with OA = 5 cm gives half-chord AP = √(5² − 3²) = 4 cm; double for full AB!",
                "explanation": "OP ⊥ AB bisects chord AB: AP = √(25 − 9) = 4 cm ⟹ full chord AB = 2 × 4 = 8 cm."
            },
            {
                "question": "Which two theorems combine cleanly in Textbook Example 1 to prove chord AB is bisected at tangent point P?",
                "options": [
                    "Theorem 10.1 (radius OP ⊥ tangent AB) + Class 9 Chord Theorem (perpendicular from center to chord bisects chord)",
                    "Theorem 10.2 + AAS Congruence",
                    "Only Angle Sum Property",
                    "Parallel lines alternate angles"
                ],
                "answer": 0,
                "hint": "First establish OP ⊥ AB on the inner circle, then apply the center-to-chord theorem on the outer circle!",
                "explanation": "Theorem 10.1 proves OP ⊥ AB, and perpendicular from center O bisects outer chord AB at P."
            }
        ]
    },
    {
        "id": 8,
        "title": "Double Angle Tangents",
        "subtitle": "Textbook Example 2 Algebraic Angle Proof: Proving ∠PTQ = 2 ∠OPQ Between Tangents & Chord",
        "speech": (
            "Now conquer Textbook Example Two, one of NCERT Class Ten Chapter Ten's cleanest angle chasing proofs! Two tangents TP and TQ are drawn cleanly to a circle centered at O from external point T! Join chord PQ and radius OP! Prove smoothly that external angle PTQ equals TWICE inner angle OPQ! "
            "Follow this sleek three step algebraic proof carefully! Step One: Set unknown external angle PTQ equal to theta! By Theorem Ten Point Two, tangent segments TP and TQ are STRICTLY EQUAL in length, turning triangle TPQ directly into an ISOSCELES TRIANGLE! "
            "Step Two: Inside isosceles triangle TPQ, the two opposite base angles TPQ and TQP MUST be strictly equal! Subtract theta from one hundred eighty degrees and divide cleanly by two: BOTH base angles equal (ninety degrees minus theta divided by two)! "
            "Step Three: Look closely at right corner angle OPT! By Theorem Ten Point One, radius OP perpendicular to tangent TP sets FULL corner angle OPT equal to exact ninety degrees! "
            "Subtract inner part angle TPQ cleanly away: remaining inner angle OPQ equals ninety minus bracket ninety minus theta divided by two bracket, leaving theta over two, proving angle PTQ equals exact twice angle OPQ!"
        ),
        "checkpoints": [
            {
                "question": "In Example 2 (tangents TP & TQ to circle centered at O), if ∠PTQ = 70°, what MUST ∠OPQ equal?",
                "options": [
                    "35°   (since ∠PTQ = 2 ∠OPQ)",
                    "70°",
                    "55°",
                    "20°"
                ],
                "answer": 0,
                "hint": "Halve ∠PTQ cleanly using ∠PTQ = 2 ∠OPQ!",
                "explanation": "By Example 2's identity ∠PTQ = 2 ∠OPQ, ∠OPQ = 70° / 2 = 35°."
            },
            {
                "question": "In proving ∠PTQ = 2 ∠OPQ, why does ∠TPQ equal (90° − ½ ∠PTQ)?",
                "options": [
                    "Because TP = TQ (Theorem 10.2) makes △TPQ isosceles, so ∠TPQ = ∠TQP = (180° − ∠PTQ) / 2 = 90° − ½ ∠PTQ",
                    "Because △TPQ is equilateral",
                    "Because ∠OPT = 45°",
                    "Because TQ = OQ"
                ],
                "answer": 0,
                "hint": "Equal tangent lengths make base angles of △TPQ equal!",
                "explanation": "Isosceles base angles share (180° − θ)/2 = 90° − θ/2; subtracting from 90° (Theorem 10.1) leaves θ/2."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch10 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

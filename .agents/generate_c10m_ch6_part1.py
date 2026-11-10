#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 6: Triangles
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (no Raghav, Sonia, Girish, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Congruence Versus Similarity",
        "subtitle": "Same Shape & Size (Congruent) vs Same Shape Across Scales (Similar) + Indirect Measurement",
        "speech": (
            "Welcome, keen geometry explorers, to Class Ten Chapter Six on Triangles! In Class Nine you mastered congruent geometric figures, which share both the exact same shape and the exact same size, fitting completely over one another without turning or stretching. "
            "Today we unlock a broader, super powerful geometry idea called similar figures! Two geometric figures sharing the exact same overall shape, yet not necessarily having the exact same physical size, are called similar figures! "
            "Think about printing three different passport and wall poster photographs from one single camera image. Every enlarged or reduced photograph looks identically shaped with matching angles, yet side lengths scale proportionally larger or smaller! "
            "Why do engineers, astronomers, and land surveyors treasure triangle similarity so deeply? Because smart indirect measurement lets us calculate enormous unreachable distances without ever carrying a giant measuring tape! "
            "Using small similar triangles measured safely on flat ground alongside light rays or ground shadows, ancient Greek thinkers measured tall mountain heights, wide river banks, and even distant celestial distances to the Moon and planets! "
            "Remember one golden rule right away: every pair of congruent shapes is automatically similar with scale factor one, whereas two similar shapes do not have to be congruent!"
        ),
        "checkpoints": [
            {
                "question": "How do similar geometric figures differ from congruent geometric figures?",
                "options": [
                    "Similar figures MUST have the same shape, but their sizes may be scaled differently (equal shape, not necessarily equal size)",
                    "Similar figures have identical areas while congruent figures do not",
                    "Congruent figures must have different angles",
                    "Similar figures only exist for circles and never triangles"
                ],
                "answer": 0,
                "hint": "Think of small and large prints of the exact same photograph!",
                "explanation": "Congruence requires equal shape AND equal size; similarity requires equal shape regardless of scale size."
            },
            {
                "question": "Why does triangle similarity enable indirect measurement of tall mountains or distant celestial objects?",
                "options": [
                    "Because a small measurable ground triangle with identical angles shares the EXACT same side ratios as the giant unreachable triangle",
                    "Because light rays bend into curved circles near mountains",
                    "Because congruent triangles can stretch across space",
                    "Because all mountains are equilateral triangles"
                ],
                "answer": 0,
                "hint": "Same angles guarantee identical proportions between small models and towering real objects!",
                "explanation": "Indirect measurement creates a small scale-model triangle whose angles match the towering object, preserving exact side ratios."
            }
        ]
    },
    {
        "id": 2,
        "title": "Always Similar Shapes",
        "subtitle": "Why All Circles, All Squares & All Equilateral Triangles Are Inherently Similar",
        "speech": (
            "Suppose a friend picks any two circles drawn anywhere on Earth, one tiny coin just two centimeters wide and one giant circular Ferris wheel twenty meters across. Are those two circles ALWAYS similar to each other? "
            "Yes, every single circle in plane geometry is strictly similar to every other circle! Look carefully at why: one single measurement, radius r, completely determines a circle, so scaling radius evenly produces the exact same round shape without ever bending or distorting angles! "
            "Now apply the exact same test to squares! Draw a tiny notebook square of side two centimeters and a huge playground square of side fifty meters. Every corner angle stays permanently locked at ninety degrees, and all four equal sides carry identical scale ratio two over five thousand! Therefore, all squares are ALWAYS similar! "
            "Next check ordinary triangles! Are all isosceles triangles always similar? Watch out carefully, no! One isosceles triangle could stand tall and skinny with a sharp twenty degree apex angle, while another sits short and wide with a wide hundred degree apex angle! "
            "Only EQUILATERAL triangles lock every interior angle permanently at sixty degrees and equalize all three sides, making ALL equilateral triangles strictly similar!"
        ),
        "checkpoints": [
            {
                "question": "Which family of triangles is ALWAYS similar regardless of side length (Exercise 6.1 Q1)?",
                "options": [
                    "Equilateral triangles  (all angles permanently 60° and equal side ratios)",
                    "Isosceles triangles",
                    "Right-angled triangles",
                    "Scalene triangles"
                ],
                "answer": 0,
                "hint": "Check which triangle family guarantees ALL three angles remain identical no matter the size!",
                "explanation": "Every equilateral triangle has three 60° angles and three equal sides, ensuring identical corresponding angles and constant side ratio."
            },
            {
                "question": "Evaluate the statement: 'Every congruent polygon is similar, and every similar polygon is congruent.'",
                "options": [
                    "First half TRUE (congruent ⟹ similar with scale factor 1), second half FALSE (e.g., 2 cm square vs 5 cm square)",
                    "Both halves are completely true",
                    "First half FALSE, second half TRUE",
                    "Both halves are false"
                ],
                "answer": 0,
                "hint": "Compare a tiny circle with radius 1 cm and a large circle with radius 10 cm!",
                "explanation": "All congruent shapes match both shape and size (hence similar), whereas similar shapes may differ in size and thus fail congruence."
            }
        ]
    },
    {
        "id": 3,
        "title": "Polygon Similarity Rules",
        "subtitle": "Formal Conditions (Equal Angles & Proportional Sides) + Exercise 6.1 Counterexamples",
        "speech": (
            "Now lock down the exact formal definition from Section Six Point Two for ANY two polygons having the exact same number of sides! Two polygons with equal side counts are similar if AND ONLY IF TWO strict geometric conditions hold together simultaneously: "
            "Condition One, all corresponding interior angles are strictly equal in measure! Condition Two, all corresponding side lengths stay in the exact same fixed constant ratio, commonly called the scale factor! "
            "Warning, never check only ONE condition all by itself! Inspect Exercise Six Point One and its famous counterexample pair: place a crisp square of side three centimeters alongside a tilted rhombus also having all four sides equal to three centimeters! "
            "Compare their side ratios first: every corresponding side ratio equals three over three, which equals one, totally proportional! Yet look closely at their four corner angles: the square holds crisp ninety degree right angles, while the tilted rhombus displays acute sixty degree and obtuse one hundred twenty degree angles! Angles fail equality, so NOT similar! "
            "Conversely, compare a square against a wide rectangle: all angles match ninety degrees cleanly, yet side ratios differ! BOTH equal angles AND proportional sides are strictly mandatory for polygons!"
        ),
        "checkpoints": [
            {
                "question": "Are a square (side 3 cm, all angles 90°) and a rhombus (side 3 cm, angles 60° & 120°) similar polygons (Ex 6.1 Q3)?",
                "options": [
                    "No—even though corresponding sides are in equal ratio 1:1, corresponding angles are NOT equal",
                    "Yes—because all corresponding sides have ratio 3:3 = 1:1",
                    "Yes—because all quadrilaterals with equal sides are congruent",
                    "Cannot be decided without diagonals"
                ],
                "answer": 0,
                "hint": "Both equal corresponding angles AND proportional sides must hold simultaneously!",
                "explanation": "Sides have ratio 1:1, but 90° ≠ 60°/120°, breaking Condition 1 (equal corresponding angles)."
            },
            {
                "question": "Two quadrilaterals ABCD and PQRS have equal corresponding angles of 90°, with sides ABCD = 4, 4, 4, 4 and PQRS = 4, 8, 4, 8. Are they similar?",
                "options": [
                    "No—the ratio of adjacent sides fails consistency (4/4 = 1 ≠ 4/8 = 1/2)",
                    "Yes—because all four angles equal 90°",
                    "Yes—because perimeters are proportional",
                    "Yes—because rectangles and squares share two equal opposite sides"
                ],
                "answer": 0,
                "hint": "Check if EVERY pair of corresponding sides shares the exact same scale factor!",
                "explanation": "Condition 1 passes (all 90°), yet Condition 2 fails because 4:4 ≠ 4:8, proving equal angles alone are insufficient for polygons with 4+ sides."
            }
        ]
    },
    {
        "id": 4,
        "title": "Similar Triangles Basics",
        "subtitle": "Triangles as a Special Polygon Case, Vertex Ordering (△ABC ~ △PQR) & Equiangular Ratios",
        "speech": (
            "Now zoom inside Section Six Point Three onto the true star shape of school geometry: triangles! Since every triangle is a three sided polygon, triangle similarity begins cleanly with the exact same two polygon rules: two triangles are similar whenever their corresponding interior angles are strictly equal AND their corresponding side lengths remain in the exact same constant ratio! "
            "Pay razor sharp attention to symbolic notation and proper vertex order! When writing Triangle ABC is similar to Triangle PQR using the squiggle wave symbol, exact vertex alignment matters critically: "
            "vertex A matches vertex P, vertex B matches vertex Q, and vertex C matches vertex R! That exact ordered correspondence guarantees angle A equals angle P, angle B equals angle Q, angle C equals angle R, AND corresponding ratio side AB over PQ equals BC over QR equals AC over PR! "
            "Swapping letters carelessly breaks matching pairs immediately! Centuries ago, the famous Greek mathematician Thales observed a brilliant truth about equiangular triangles, meaning pairs of triangles having all three corresponding angles equal: "
            "whenever two triangles share identical corresponding angles, the ratio between ANY two corresponding sides stays constant everywhere in plane geometry, launching Thales celebrated Basic Proportionality Theorem!"
        ),
        "checkpoints": [
            {
                "question": "If △ABC ~ △DEF cleanly in that exact vertex order, which side ratio equation MUST be true?",
                "options": [
                    "AB / DE = BC / EF = AC / DF",
                    "AB / DF = BC / DE = AC / EF",
                    "AB / EF = BC / DF = AC / DE",
                    "AB + DE = BC + EF = AC + DF"
                ],
                "answer": 0,
                "hint": "Match 1st-2nd with 1st-2nd, 2nd-3rd with 2nd-3rd, and 1st-3rd with 1st-3rd!",
                "explanation": "Preserving vertex correspondence (A↔D, B↔E, C↔F) gives AB/DE = BC/EF = AC/DF."
            },
            {
                "question": "What does 'equiangular triangles' mean, as studied by Greek mathematician Thales?",
                "options": [
                    "Two triangles whose corresponding interior angles are strictly equal (∠A=∠P, ∠B=∠Q, ∠C=∠R)",
                    "Triangles whose angles are all 90°",
                    "Triangles having all sides strictly equal in length",
                    "Triangles sharing zero equal angles"
                ],
                "answer": 0,
                "hint": "Notice the roots: 'equi' (equal) + 'angular' (angles)!",
                "explanation": "Equiangular triangles have pairwise equal corresponding angles; Thales noted their corresponding side ratios remain constant."
            }
        ]
    },
    {
        "id": 5,
        "title": "Basic Proportionality Theorem",
        "subtitle": "Statement & Area-Ratio Proof of Theorem 6.1 (Thales Theorem): DE ∥ BC ⟹ AD/DB = AE/EC",
        "speech": (
            "Master one of Class Ten mathematics most celebrated proofs: Theorem Six Point One, the Basic Proportionality Theorem, famously honored as Thales Theorem! "
            "Listen carefully to the exact theorem statement: If a line is drawn parallel to one side of a triangle intersecting the other two sides in distinct points, then the other two sides are divided in the exact same ratio! "
            "Consider triangle ABC where line DE runs parallel to side BC, cutting side AB at D and side AC at E! We must prove AD over DB equals AE over EC! "
            "Follow this crystal clear four-step area proof! Step One: join B to E and C to D, plus draw altitudes EN perpendicular to AB and DM perpendicular to AC! "
            "Step Two: Compare triangles ADE and BDE sharing equal altitude EN: area ADE over area BDE simplifies cleanly to AD over DB! "
            "Step Three: Compare triangles ADE and CDE sharing equal altitude DM: area ADE over area CDE simplifies cleanly to AE over EC! "
            "Step Four: Notice triangles BDE and CDE stand on the same base DE between the same parallels DE and BC, making their areas strictly EQUAL, proving AD over DB equals AE over EC!"
        ),
        "checkpoints": [
            {
                "question": "In the proof of Theorem 6.1 (BPT, with DE ∥ BC), why does ar(△BDE) equal ar(△CDE)?",
                "options": [
                    "Because △BDE and △CDE stand on the SAME base DE and lie between the SAME parallel lines DE and BC",
                    "Because D and E are strictly midpoints of AB and AC",
                    "Because △BDE and △CDE are right-angled isosceles triangles",
                    "Because BD always equals CE in every triangle"
                ],
                "answer": 0,
                "hint": "Recall the Class 9 Area Theorem for triangles sharing a base between parallels!",
                "explanation": "Triangles on the same base DE and between the same parallels DE ∥ BC have equal altitude, hence equal area: ar(BDE) = ar(CDE)."
            },
            {
                "question": "In △ABC with DE ∥ BC, if AD = 1.5 cm, DB = 3 cm, and AE = 1 cm (Ex 6.2 Q1 i), what is EC?",
                "options": [
                    "2 cm",
                    "1.5 cm",
                    "3 cm",
                    "4.5 cm"
                ],
                "answer": 0,
                "hint": "Set up BPT: 1.5 / 3 = 1 / EC!",
                "explanation": "By BPT, AD/DB = AE/EC ⟹ 1.5/3 = 1/EC ⟹ 1/2 = 1/EC ⟹ EC = 2 cm."
            }
        ]
    },
    {
        "id": 6,
        "title": "BPT Proof Extensions",
        "subtitle": "Whole-Side Ratios (AD/AB = AE/AC) & Proving Trapezium Diagonals Cut Proportionally",
        "speech": (
            "Once Thales Basic Proportionality Theorem locks down upper ratio AD over DB equals AE over EC inside triangle ABC with line DE parallel to side BC, two super useful algebraic ratio siblings follow instantaneously! "
            "First, add one neatly to both sides of AD over DB equals AE over EC! Writing one as DB over DB on the left side and EC over EC on the right side yields AD plus DB all over DB equals AE plus EC all over EC, which simplifies smoothly to whole side AB over DB equals whole side AC over EC! "
            "Even better, flip BPT completely upside down into DB over AD equals EC over AE, then add one cleanly to BOTH sides! That gives full ratio AB over AD equals AC over AE, or inverted directly as part AD over whole side AB equals part AE over whole side AC! "
            "Watch how these ratios crush Exercise Six Point Two Question Nine immediately: prove that diagonals AC and BD of trapezium ABCD with AB parallel to DC intersect at point O satisfying AO over BO equals CO over DO! "
            "Simply draw auxiliary parallel line EO parallel to AB and DC, apply BPT twice inside triangles ADC and DAB, and equate AE over ED cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Given DE ∥ BC in △ABC, which THREE ratio equations are ALL valid consequences of BPT?",
                "options": [
                    "AD/DB = AE/EC,   AD/AB = AE/AC,   and   DB/AB = EC/AC",
                    "AD/DB = EC/AE,   AD/AB = AC/AE,   and   DE/BC = AD/DB",
                    "Only AD/DB = AE/EC (full side AB can never appear)",
                    "AD/BC = AE/BC"
                ],
                "answer": 0,
                "hint": "Notice DE/BC equals AD/AB (whole side), NOT AD/DB (upper part over lower part)!",
                "explanation": "Adding 1 to BPT and its reciprocal yields both part-to-whole ratios AD/AB = AE/AC and DB/AB = EC/AC."
            },
            {
                "question": "In trapezium ABCD (AB ∥ DC) with diagonals intersecting at O (Ex 6.2 Q9), if AO = 3x−1, OC = 5x−3, BO = 2x+1, OD = 6x−5, what ratio equation always holds?",
                "options": [
                    "AO / OC = BO / OD  (equivalently AO / BO = CO / DO)",
                    "AO / OC = OD / BO",
                    "AO + OC = BO + OD",
                    "AO × CO = BO × DO"
                ],
                "answer": 0,
                "hint": "Draw EO ∥ AB ∥ DC and match AE/ED from △ADC and △DAB!",
                "explanation": "Applying BPT in △ADC gives AE/ED = AO/OC, and in △DAB gives AE/ED = BO/OD, hence AO/OC = BO/OD."
            }
        ]
    },
    {
        "id": 7,
        "title": "Converse Of BPT",
        "subtitle": "Theorem 6.2 Statement & Contradiction Proof: AD/DB = AE/EC ⟹ Line DE ∥ BC",
        "speech": (
            "In geometry, whenever a forward theorem shines bright, immediately flip the logical arrow backwards and test its CONVERSE! Welcome to Theorem Six Point Two, the Converse of Basic Proportionality Theorem! "
            "Here is its crystal clear theorem statement: If a line divides any two sides of a triangle in the exact same ratio, then that dividing line MUST run strictly parallel to the third side! "
            "Suppose inside triangle ABC we are GIVEN AD over DB equals AE over EC, and we must prove DE is parallel to BC! How do mathematicians prove this backwards result cleanly without guessing? By using a sleek Proof by Contradiction! "
            "Assume temporarily for argument sake that DE is NOT parallel to BC! Then through point D, Euclidean geometry lets us draw ONE true parallel line DE prime parallel to side BC, meeting side AC at some distinct point E prime! "
            "By forward BPT on DE prime parallel to BC, AD over DB equals AE prime over E prime C! Comparing against our given AD over DB equals AE over EC forces AE over EC to equal AE prime over E prime C! "
            "Adding one cleanly to both sides forces E and E prime to coincide completely, proving DE parallel to BC!"
        ),
        "checkpoints": [
            {
                "question": "In the contradiction proof of Theorem 6.2 (Converse of BPT), why does AE/EC = AE'/E'C force points E and E' to coincide?",
                "options": [
                    "Adding 1 gives AC/EC = AC/E'C ⟹ EC = E'C, so E and E' lie at the exact same distance from C on segment AC",
                    "Because △ABC is assumed equilateral",
                    "Because DE is perpendicular to AC",
                    "Because AD must equal AE"
                ],
                "answer": 0,
                "hint": "Add 1 cleanly to both sides: (AE + EC)/EC = (AE' + E'C)/E'C!",
                "explanation": "Since AE + EC = AC and AE' + E'C = AC, equality forces AC/EC = AC/E'C ⟹ EC = E'C, proving E and E' are identical!"
            },
            {
                "question": "In △PQR, points E and F lie on PQ and PR with PE = 3.9 cm, EQ = 3 cm, PF = 3.6 cm, and FR = 2.4 cm (Ex 6.2 Q2 i). Is EF ∥ QR?",
                "options": [
                    "No—because PE/EQ = 1.3 whereas PF/FR = 1.5 (unequal ratios)",
                    "Yes—because both PE > EQ and PF > FR",
                    "Yes—because 3.9 − 3 = 0.9",
                    "Cannot tell without knowing ∠P"
                ],
                "answer": 0,
                "hint": "Compute PE/EQ = 3.9/3 and compare carefully against PF/FR = 3.6/2.4!",
                "explanation": "PE/EQ = 3.9/3 = 1.3 while PF/FR = 3.6/2.4 = 1.5; since 1.3 ≠ 1.5, Converse of BPT shows EF is NOT parallel to QR."
            }
        ]
    },
    {
        "id": 8,
        "title": "BPT Geometric Proofs",
        "subtitle": "Double-Parallel Proofs (Ex 6.2 Q3-4) & Midpoint Theorem Derived via Converse of BPT",
        "speech": (
            "Now put BOTH Theorem Six Point One and Theorem Six Point Two directly to work side by side solving Exercise Six Point Two famous double parallel geometric proofs! "
            "Look closely at Exercise Six Point Two Question Three: a kite shaped diagram joins two adjacent triangles ABC and ADC smoothly along their shared central diagonal AC! Line segment LM runs strictly parallel to side CB inside upper triangle ABC, while segment LN runs parallel to CD inside lower triangle ADC! "
            "Watch how effortlessly BPT connects both ratios across the shared bridge AC! From upper triangle ABC with LM parallel to CB, BPT corollary gives AM over AB equals AL over AC! From lower triangle ADC with LN parallel to CD, BPT corollary gives AN over AD equals AL over AC! "
            "Because BOTH target fractions equal that exact same shared bridge AL over AC, equating them yields AM over AB equals AN over AD instantly! "
            "Finally check Question Seven, linking straight back to Class Nine and the famous Midpoint Theorem! If a segment connects the exact midpoints D of AB and E of AC, both AD over DB and AE over EC equal one, so Converse of BPT proves DE parallel to BC!"
        ),
        "checkpoints": [
            {
                "question": "In two back-to-back triangles sharing diagonal AC, LM ∥ CB in △ABC and LN ∥ CD in △ADC (Ex 6.2 Q3). Which shared bridge proves AM/AB = AN/AD?",
                "options": [
                    "Both AM/AB and AN/AD equal the shared ratio AL / AC on diagonal AC",
                    "Both equal LM / CB",
                    "Both equal MN / BD directly without AC",
                    "Both equal 1/2"
                ],
                "answer": 0,
                "hint": "Apply the BPT corollary AD/AB = AE/AC cleanly to BOTH upper and lower triangles!",
                "explanation": "LM ∥ CB gives AM/AB = AL/AC; LN ∥ CD gives AN/AD = AL/AC; equating them proves AM/AB = AN/AD."
            },
            {
                "question": "If D is the midpoint of AB and E is the midpoint of AC in △ABC (Ex 6.2 Q7), how does Converse of BPT prove DE ∥ BC?",
                "options": [
                    "Because AD/DB = 1 and AE/EC = 1, making AD/DB = AE/EC ⟹ DE ∥ BC",
                    "Because △ADE is congruent to △ABC",
                    "Because ∠D = 90°",
                    "Because DE = AB"
                ],
                "answer": 0,
                "hint": "Midpoints mean AD = DB and AE = EC — divide each pair!",
                "explanation": "Midpoints satisfy AD/DB = 1 and AE/EC = 1; equal ratios invoke Theorem 6.2 (Converse of BPT) to guarantee DE ∥ BC."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch6 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

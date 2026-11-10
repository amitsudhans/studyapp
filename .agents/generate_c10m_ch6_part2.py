#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 6: Triangles
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (no Raghav, Girish, Sonia, etc.), zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Why Three Criteria",
        "subtitle": "Minimum Shortcuts to Prove △ABC ~ △DEF Without Checking All Six Conditions",
        "speech": (
            "Pause carefully and ask a super smart foundational question right at the start of Section Six Point Four! By formal definition, two triangles are similar only when ALL six relationships hold together simultaneously: three equal corresponding interior angle pairs PLUS three proportional corresponding side ratios! "
            "Must geometry students verify ALL SIX separate relationships manually every single time they compare two triangles? Never worry! Just as Class Nine triangle congruence offered crisp shortcuts like SSS, SAS, and ASA instead of checking all six triangle parts, triangle similarity ALSO provides THREE golden minimum sufficient shortcuts! "
            "Meet our powerhouse trio of core theorems: Theorem Six Point Three is AAA Similarity along with its super fast two angle helper called AA! Theorem Six Point Four is SSS Similarity! Theorem Six Point Five is SAS Similarity! "
            "Before proving each similarity criterion rigorously step by step, guard yourself firmly against TWO classic student traps! Trap One: never confuse SSS congruence, which requires equal side lengths, with SSS similarity, which requires equal constant side ratios across all three pairs! "
            "Trap Two: inside SAS similarity, that single equal angle MUST sit strictly INCLUDED right between the two proportional sides! Always trace exact vertex correspondence order carefully!"
        ),
        "checkpoints": [
            {
                "question": "Why are minimum similarity criteria (AAA/AA, SSS, SAS) so valuable in geometry?",
                "options": [
                    "They prove ALL 6 similarity conditions hold automatically after verifying only 2 angles or 3 proportional parts",
                    "They eliminate the need for angles and sides altogether",
                    "They work exclusively for equilateral triangles",
                    "They let side ratios differ across edges"
                ],
                "answer": 0,
                "hint": "Just like Class 9 congruence criteria, checking fewer conditions guarantees the rest follow automatically!",
                "explanation": "Similarity criteria reduce the 6 required conditions down to 2 or 3 minimum checks, automatically implying the remaining parts match."
            },
            {
                "question": "If △ABC and △PQR satisfy AB/QR = BC/PR = CA/PQ (Ex 6.3 Q2 style), which exact similarity notation matches corresponding vertices?",
                "options": [
                    "△ABC ~ △QRP  (since A↔Q, B↔R, C↔P)",
                    "△ABC ~ △PQR",
                    "△ABC ~ △RPQ",
                    "△ABC ~ △PRQ"
                ],
                "answer": 0,
                "hint": "Find the vertex shared by AB and CA (vertex A), and match it to the vertex shared by QR and PQ (vertex Q)!",
                "explanation": "AB/QR and CA/PQ share A↔Q; AB/QR and BC/PR share B↔R; hence C↔P, giving △ABC ~ △QRP."
            }
        ]
    },
    {
        "id": 10,
        "title": "AAA Similarity Theorem",
        "subtitle": "Theorem 6.3 Cut-and-Place Proof + AA Similarity Corollary via Triangle Angle Sum 180°",
        "speech": (
            "Explore Theorem Six Point Three, the celebrated AAA Similarity Criterion, most frequently used across board geometry proofs and real world indirect shadow calculations! "
            "Read the theorem statement cleanly: If in two triangles, corresponding interior angles are strictly equal, then their corresponding sides automatically lie in the exact same ratio, and hence the two triangles are strictly similar! "
            "How do we prove that equal angles force proportional side ratios? Apply our classic Cut and Place construction inside larger triangle DEF! Suppose angle A equals angle D, angle B equals angle E, and angle C equals angle F. "
            "Cut points P along side DE and Q along side DF such that segment DP equals AB and segment DQ equals AC, then join segment PQ! Instantly small triangle ABC becomes congruent to triangle DPQ by SAS congruence! Therefore angle DPQ equals angle B, which equals angle E! "
            "Because equal corresponding angles make line PQ strictly parallel to side EF, Thales BPT corollary gives DP over DE equals DQ over DF, meaning AB over DE equals AC over DF! "
            "Even faster, by our AA Corollary, matching JUST TWO angle pairs forces the third pair equal via 180 degree triangle angle sum!"
        ),
        "checkpoints": [
            {
                "question": "In the proof of Theorem 6.3 (AAA Similarity, cutting DP = AB and DQ = AC on △DEF), what proves line PQ is parallel to EF?",
                "options": [
                    "△ABC ≅ △DPQ (SAS) makes ∠DPQ = ∠B = ∠E, so equal corresponding angles force PQ ∥ EF",
                    "Converse of Pythagoras theorem",
                    "Assumption that AB = DE",
                    "Because P and Q are midpoints of DE and DF"
                ],
                "answer": 0,
                "hint": "Compare corresponding angles ∠DPQ and ∠E on transversal DE!",
                "explanation": "By SAS congruence △ABC ≅ △DPQ, giving ∠DPQ = ∠B = ∠E; equal corresponding angles guarantee PQ ∥ EF."
            },
            {
                "question": "Why is the AA (Angle-Angle) Criterion logically identical to AAA Similarity?",
                "options": [
                    "Because Triangle Angle Sum equals 180°: if two pairs of angles match, the third pair (180° − sum) MUST match automatically!",
                    "Because every triangle has only two angles",
                    "Because all triangles are right-angled",
                    "Because the third side is always equal"
                ],
                "answer": 0,
                "hint": "Compute ∠C = 180° − (∠A + ∠B) and ∠F = 180° − (∠D + ∠E)!",
                "explanation": "Two equal angle pairs force the third angle pair equal by the 180° angle-sum property, fulfilling full AAA."
            }
        ]
    },
    {
        "id": 11,
        "title": "SSS Similarity Theorem",
        "subtitle": "Theorem 6.4 Statement & Proof: Proportional Sides Force PQ ∥ EF and Equal Angles",
        "speech": (
            "Now flip Theorem Six Point Three neatly around backwards to prove Theorem Six Point Four, the SSS Similarity Criterion! "
            "Read its exact textbook statement carefully: If in two triangles, sides of one triangle are strictly proportional to all three corresponding sides of the other triangle, then their corresponding angles MUST be equal, and hence the two triangles are strictly similar! "
            "Given AB over DE equals BC over EF equals CA over FD across triangles ABC and DEF, how do we prove angle A equals angle D, angle B equals angle E, and angle C equals angle F? "
            "Draw the exact same cut inside larger triangle DEF: mark DP equals AB along side DE and DQ equals AC along side DF, then join segment PQ! Notice DP over DE equals DQ over DF immediately! By Theorem Six Point Two, the Converse of BPT, line PQ runs strictly parallel to side EF! "
            "Because parallel lines always create equal corresponding angles cleanly, triangle DPQ becomes similar to triangle DEF by AA! Thus DP over DE equals PQ over EF! Comparing with given BC over EF forces PQ to equal BC, proving triangle ABC congruent to DPQ by SSS congruence!"
        ),
        "checkpoints": [
            {
                "question": "In proving Theorem 6.4 (SSS Similarity), after cutting DP = AB and DQ = AC, which theorem shows PQ ∥ EF?",
                "options": [
                    "Converse of BPT (Theorem 6.2), because AB/DE = AC/DF implies DP/DE = DQ/DF",
                    "AAA Similarity directly without BPT",
                    "SAS Congruence alone",
                    "Midpoint theorem directly"
                ],
                "answer": 0,
                "hint": "Side ratios DP/DE = DQ/DF hold FIRST, before knowing angles!",
                "explanation": "Proportional cuts DP/DE = DQ/DF establish PQ ∥ EF via Converse of BPT, leading to △DPQ ~ △DEF and PQ = BC."
            },
            {
                "question": "Given △ABC with sides 2, 3, 2.5 and △DEF with sides 4, 6, 5 (Ex 6.3 Q2 style), are the triangles similar, and by which criterion?",
                "options": [
                    "Yes, by SSS Similarity with constant ratio 1 : 2 across all three side pairs",
                    "Yes, by AAA Similarity",
                    "No—sides are not equal",
                    "Yes, by SAS Similarity"
                ],
                "answer": 0,
                "hint": "Divide each side of △ABC by the corresponding doubled side of △DEF!",
                "explanation": "2/4 = 3/6 = 2.5/5 = 1/2 across all three corresponding pairs, satisfying SSS Similarity (Theorem 6.4)."
            }
        ]
    },
    {
        "id": 12,
        "title": "SAS Similarity Theorem",
        "subtitle": "Theorem 6.5 Proof & Crucial Trap Check: Equal Angle MUST Sit Included Between Ratio Sides",
        "speech": (
            "Meet the third essential pillar inside Section Six Point Four: Theorem Six Point Five, the SAS Similarity Criterion! "
            "State Theorem Six Point Five with crystal precision: If one interior angle of a triangle equals one corresponding angle of another triangle AND the two pairs of sides including those equal angles are proportional, then the two triangles are strictly similar! "
            "Watch how smoothly its geometric proof combines the clever steps of our earlier proofs! Given angle A equals angle D together with proportional flanking sides AB over DE equals AC over DF, cut segment DP equals AB along DE and segment DQ equals AC along DF, then join line PQ! "
            "Immediately triangle ABC matches triangle DPQ cleanly by SAS Congruence! Next, because cut ratios satisfy DP over DE equals DQ over DF, Converse of BPT, Theorem Six Point Two, forces line PQ strictly parallel to side EF! "
            "Parallel lines make corresponding angles P equal E and Q equal F, guaranteeing angle A equals D, B equals E, and C equals F! "
            "Remember this crucial Exercise Six Point Three trap: given equal angle A equals D, always verify proportional included flanking sides AB over DE equals AC over DF!"
        ),
        "checkpoints": [
            {
                "question": "To prove △ABC ~ △DEF using SAS Similarity (Theorem 6.5) when given ∠B = ∠E, which two side pairs MUST be proportional?",
                "options": [
                    "AB / DE = BC / EF  (the two sides forming ∠B and ∠E)",
                    "AC / DF = BC / EF",
                    "AB / DE = AC / DF",
                    "Any two pairs regardless of angle position"
                ],
                "answer": 0,
                "hint": "Trace which two edges touch vertex B and vertex E!",
                "explanation": "∠B is included between sides AB and BC, while ∠E is included between DE and EF; hence AB/DE = BC/EF is required."
            },
            {
                "question": "In Ex 6.3 Q2 (iv), △MNL has MN=2.5, ML=5, ∠M=70° and △PQR has PQ=6, QR=10, ∠Q=70°. Check whether △MNL ~ △QPR!",
                "options": [
                    "No—around the 70° angle, side ratios MN/PQ = 2.5/6 and ML/QR = 5/10 = 1/2 are UNEQUAL, so SAS fails!",
                    "Yes—because both triangles contain a 70° angle",
                    "Yes—by AAA Similarity",
                    "Yes—they are congruent"
                ],
                "answer": 0,
                "hint": "Check included ratios: (shorter/shorter) vs (longer/longer) around the 70° angle!",
                "explanation": "SAS holds strictly when ratios around the 70° included angle match: 2.5/5 = 5/10 = 1/2 succeeds, whereas 2.5/6 ≠ 5/10 fails!"
            }
        ]
    },
    {
        "id": 13,
        "title": "Shadow Length Models",
        "subtitle": "Solving Lamp-Post Walker (Example 7) & Vertical Pole / Tower Sun Shadow Heights (Ex 6.3)",
        "speech": (
            "Now put AA Similarity directly to practical real world work on textbook shadow engineering problems, keeping every setup clean with zero fictional character names! "
            "Study Model One from Textbook Example Seven, walking directly away from a street lamp post! A bright lamp hangs at height three point six meters straight above flat ground. A student measuring ninety centimeters, or zero point nine meters tall, walks straight away from the lamp base at speed one point two meters per second! "
            "How long does the student's ground shadow stretch after four seconds? First multiply speed one point two meters per second by four seconds to find distance walked equals four point eight meters! "
            "Now trace the two overlapping right triangles formed vertically by tall lamp post AB of height three point six meters and shorter student CD of height zero point nine meters, meeting cleanly at ground shadow tip E! "
            "Both stand perpendicular at ninety degrees AND share common ground vertex angle E, making large triangle ABE similar to small triangle CDE by AA Similarity! Setting BE over DE equals AB over CD gives four point eight plus x all over x equals four, solving cleanly to shadow length one point six meters!"
        ),
        "checkpoints": [
            {
                "question": "A lamp is 3.6 m above the ground. A 0.9 m tall student walks away at 1.2 m/s for 4 seconds (distance 4.8 m). What is the shadow length x?",
                "options": [
                    "1.6 m  [solving (4.8 + x)/x = 3.6/0.9 = 4 ⟹ 3x = 4.8]",
                    "1.2 m",
                    "2.4 m",
                    "4.8 m"
                ],
                "answer": 0,
                "hint": "Shadow base of big triangle is (4.8 + x) while small triangle base is x!",
                "explanation": "By AA Similarity, (4.8 + x)/x = 3.6/0.9 = 4 ⟹ 4x = 4.8 + x ⟹ 3x = 4.8 ⟹ x = 1.6 m."
            },
            {
                "question": "A vertical pole 6 m tall casts a 4 m shadow on flat ground while a nearby tower casts a 28 m shadow (Ex 6.3 Q15). Find the tower height!",
                "options": [
                    "42 m",
                    "18.67 m",
                    "32 m",
                    "56 m"
                ],
                "answer": 0,
                "hint": "Sun's rays strike at equal elevation angles at the same moment ⟹ height / shadow stays constant!",
                "explanation": "By AA Similarity (90° ground + equal Sun angle), h / 28 = 6 / 4 ⟹ h = (6 × 28) / 4 = 42 m."
            }
        ]
    },
    {
        "id": 14,
        "title": "Median Overlapping Proofs",
        "subtitle": "Exercise 6.3 Proof Techniques: Medians Proportionality (Q12, Q14) & Angle-Chasing Riders",
        "speech": (
            "Master two high weightage Exercise Six Point Three geometric proof techniques tested repeatedly across Class Ten mathematics board exams! "
            "Technique One covers Proportionality of Triangle Medians in Question Twelve! Suppose two triangles ABC and PQR satisfy proportional ratio AB over PQ equals BC over QR equals median AD over median PM, where D bisects side BC and M bisects side QR! "
            "How do you prove entire triangle ABC is strictly similar to triangle PQR? Watch this sleek move carefully: rewrite full base lengths BC and QR cleanly as TWICE their half segments 2 BD and 2 QM! "
            "Canceling factor two gives AB over PQ equals BD over QM equals AD over PM! Instantly small left triangle ABD matches small triangle PQM by SSS Similarity, locking down corresponding angle B equal to angle Q! "
            "Now step back outside to full triangles ABC and PQR cleanly: having AB over PQ equals BC over QR PLUS included angle B equal to angle Q proves entire triangle ABC strictly similar to triangle PQR by SAS Similarity! "
            "Technique Two: remember always that whenever two triangles are similar, their overall perimeter ratio P1 over P2 equals their corresponding side scale ratio!"
        ),
        "checkpoints": [
            {
                "question": "Given AB/PQ = BC/QR = AD/PM where AD and PM are medians of △ABC and △PQR (Ex 6.3 Q12), what proves △ABC ~ △PQR?",
                "options": [
                    "First △ABD ~ △PQM by SSS (using BC/QR = 2BD/2QM = BD/QM) ⟹ ∠B = ∠Q, then △ABC ~ △PQR by SAS",
                    "Directly by AAA without checking sides",
                    "First △ADC ~ △PMR by RHS",
                    "Because medians always equal sides"
                ],
                "answer": 0,
                "hint": "Rewrite BC = 2 BD and QR = 2 QM to link the left half-triangles first!",
                "explanation": "Halving BC and QR gives △ABD ~ △PQM (SSS), securing ∠B = ∠Q so full triangles match by SAS."
            },
            {
                "question": "Sides AB and AC and median AD of △ABC are proportional to PQ, PR, and median PM of △PQR (Ex 6.3 Q14). What construction unlocks SAS inside Q14?",
                "options": [
                    "Extend AD to E (so AD = DE) and PM to N (so PM = MN), forming congruent triangles/parallelograms to link AC to BE",
                    "Bisect ∠B and ∠Q randomly",
                    "Draw altitudes only",
                    "Assume ∠A = 90°"
                ],
                "answer": 0,
                "hint": "Doubling the median creates △ABE and △PQN where BE = AC and QN = PR!",
                "explanation": "Extending AD = DE (producing ABEC parallelogram) makes BE = AC, turning AB/PQ = AC/PR = AD/PM into SSS on △ABE ~ △PQN!"
            }
        ]
    },
    {
        "id": 15,
        "title": "RHS Similarity Criterion",
        "subtitle": "Supplementary RHS Criterion & Right-Triangle Altitude Split Creating 3 Similar Triangles",
        "speech": (
            "Now inspect Section Six Point Five's valuable Supplementary Note alongside a classic right triangle altitude theorem! Meet the RHS Similarity Criterion standing neatly for Right Angle, Hypotenuse, and Side! "
            "Read its exact statement cleanly: If in two right angled triangles, the hypotenuse and one leg of one triangle are proportional to the hypotenuse and one corresponding leg of the other triangle, then the two triangles MUST be strictly similar! "
            "Pause and ask why RHS always works cleanly even though non included SSA fails for general non right triangles! Because Pythagoras Theorem locks down the third leg uniquely whenever one ninety degree right angle sits opposite the longest hypotenuse! "
            "Specifically, if hypotenuse AC over PR equals leg AB over PQ equals constant k inside right triangles angled at B and Q, Pythagoras automatically forces remaining leg BC over QR to equal that exact same ratio k, triggering SSS Similarity effortlessly! "
            "Also discover this gorgeous bonus theorem inside any right angled triangle ABC right angled at C: dropping altitude CD perpendicular onto hypotenuse AB divides triangle ABC neatly into TWO smaller right triangles ACD and CBD, making ALL THREE right triangles mutually similar cleanly to one another!"
        ),
        "checkpoints": [
            {
                "question": "Why does RHS (Right-Angle + proportional Hypotenuse + Leg) guarantee triangle similarity even though general non-included SSA fails?",
                "options": [
                    "Pythagoras fixes the third leg uniquely in right triangles, forcing all three side ratios equal (triggering SSS Similarity)",
                    "Because right triangles are always congruent",
                    "Because all right triangles are equilateral",
                    "Because hypotenuse ratio always equals 1"
                ],
                "answer": 0,
                "hint": "Use b₁ = √(h₁² − a₁²) and b₂ = √(h₂² − a₂²) when h₁ = k·h₂ and a₁ = k·a₂!",
                "explanation": "Since √((kh₂)² − (ka₂)²) = k√(h₂² − a₂²), the third leg shares exact ratio k, satisfying SSS Similarity."
            },
            {
                "question": "In right △ABC (∠C = 90°), altitude CD ⊥ AB meets hypotenuse AB at D. Which similarity statement is strictly correct?",
                "options": [
                    "△ABC ~ △ACD ~ △CBD  (all three right triangles match acute angles cleanly)",
                    "△ABC ~ △ADC ~ △BDC",
                    "Only △ACD ~ △CBD, never △ABC",
                    "They are congruent, not similar"
                ],
                "answer": 0,
                "hint": "Trace acute angle A: ∠ACD = 90° − ∠A = ∠B, matching vertex order A↔A↔C and C↔D↔B!",
                "explanation": "Matching right angles (∠C = ∠ADC = ∠CDB = 90°) and acute angle ∠A = ∠BCD gives △ABC ~ △ACD ~ △CBD."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Six Summary",
        "subtitle": "Master Recap: Congruence vs Similarity, BPT, Converse of BPT, AAA/AA, SSS, SAS & RHS",
        "speech": (
            "Congratulations, keen geometry champions! You have now mastered every key definition, geometric proof, and real world proportion trick inside NCERT Class Ten Chapter Six on Triangles! Snapshot all six golden takeaways cleanly before launching into our four Interactive Exercise Sets! "
            "One: Similar figures always share the exact same shape with equal corresponding angles AND proportional sides, while all congruent figures are automatically similar with scale factor one. Two: ALL circles, ALL squares, and ALL equilateral triangles of any dimensions are permanently similar to each other. "
            "Three: Thales Basic Proportionality Theorem, Theorem Six Point One, states that line DE parallel to BC gives AD over DB equals AE over EC alongside whole side ratios AD over AB equals AE over AC. "
            "Four: Converse of BPT, Theorem Six Point Two, proves that equal ratios AD over DB equals AE over EC force DE parallel to BC. Five: Proving two triangles similar requires checking only AAA or AA, SSS, SAS with equal INCLUDED angle, or Supplementary RHS for right triangles! "
            "Six: Always carefully align all matching vertex letters in exact corresponding order when writing triangle similarity equations! Now go solve Exercises 6.1 through 6.3 and our final Mastery Challenge confidently!"
        ),
        "checkpoints": [
            {
                "question": "If △ABC ~ △RPQ, AB = 3 cm, BC = 5 cm, AC = 6 cm, and RP = 6 cm, QR = 12 cm, what is side PQ?",
                "options": [
                    "10 cm  (since scale factor AB/RP = 3/6 = 1/2 ⟹ PQ = 2 × BC = 10 cm)",
                    "12 cm",
                    "5 cm",
                    "2.5 cm"
                ],
                "answer": 0,
                "hint": "Follow exact vertex correspondence: AB↔RP, BC↔PQ, AC↔RQ!",
                "explanation": "Vertex matching △ABC ~ △RPQ sets AB/RP = BC/PQ ⟹ 3/6 = 5/PQ ⟹ PQ = 10 cm."
            },
            {
                "question": "Which summary rule below contains ZERO mathematical errors?",
                "options": [
                    "All equilateral triangles are similar; DE ∥ BC ⟺ AD/DB = AE/EC; valid criteria are AAA/AA, SSS, SAS, and right-triangle RHS",
                    "All similar triangles must be congruent",
                    "A square and rhombus with equal sides are always similar",
                    "Non-included SSA guarantees similarity for acute triangles"
                ],
                "answer": 0,
                "hint": "Check counterexamples (rhombus vs square) and non-included SSA!",
                "explanation": "Option 1 accurately states shape similarity, BPT/Converse equivalence, and all valid similarity criteria."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch6 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

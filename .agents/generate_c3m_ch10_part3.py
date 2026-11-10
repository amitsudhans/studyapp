#!/usr/bin/env python3
"""
Generate NCERT Class 3 Mathematics - Chapter 10: Fun at Class Party!
Part 3: Slides 17 to 20 (Mastery Challenge Quizzes)
4 Slides × 10 Questions = 40 Questions
Each question has: id, question, options (4), answer (0-3), hint, explanation, solution_steps (3 steps).
Titles: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human character names. Zero teacher personas.
"""

slides_part3 = [
    # Slide 17: Challenge 1 (Foundations & Non-Standard Measuring)
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Informal measurements, handspans, perimeter strings, and bilateral symmetry",
        "questions": [
            {
                "question": "If a study desk edge measures 7 large handspans, how many smaller handspans are expected for the same edge?",
                "options": ["More than 7 handspans", "Fewer than 7 handspans", "Exactly 7 handspans", "Zero handspans"],
                "answer": 0,
                "hint": "Smaller units cover less physical distance with each step.",
                "explanation": "Because smaller hands have a shorter span, more spans must be counted to cover the same total edge length.",
                "solution_steps": [
                    "Identify the relationship: smaller measuring unit means a higher count for an identical length.",
                    "Compare hand sizes: smaller handspan covers less distance per span than a large handspan.",
                    "Conclude that more than 7 smaller handspans are needed to traverse the desk edge."
                ]
            },
            {
                "question": "A student measures a tabletop as 9 handspans and a friend measures it as 11 handspans. What explains this difference?",
                "options": [
                    "The friend has smaller hands than the first student",
                    "The tabletop shrank while being measured",
                    "The friend has larger hands than the first student",
                    "The table moved to another classroom"
                ],
                "answer": 0,
                "hint": "More spans mean each individual span is shorter.",
                "explanation": "A higher count of 11 spans indicates that the friend's individual handspan is shorter (smaller hands).",
                "solution_steps": [
                    "Notice that the table length remains fixed in both measurements.",
                    "Understand that count × unit size = total length.",
                    "Since 11 is greater than 9, the friend's unit size (handspan) must be smaller."
                ]
            },
            {
                "question": "A rectangular green board takes 8 decorative paper strings across the top and 5 along the side. What is its total perimeter?",
                "options": ["26 strings", "13 strings", "40 strings", "16 strings"],
                "answer": 0,
                "hint": "A rectangle has two equal horizontal sides and two equal vertical sides.",
                "explanation": "Perimeter = Top + Bottom + Left + Right = 8 + 8 + 5 + 5 = 26 paper strings.",
                "solution_steps": [
                    "Add the two horizontal borders: 8 + 8 = 16 strings.",
                    "Add the two vertical side borders: 5 + 5 = 10 strings.",
                    "Total perimeter = 16 + 10 = 26 paper strings."
                ]
            },
            {
                "question": "When measuring a table border with paper strings, which practice guarantees an accurate measurement?",
                "options": [
                    "Placing strings end-to-end with no gaps and no overlapping",
                    "Overlapping adjacent strings by half their length",
                    "Leaving random empty gaps between strings",
                    "Folding each string into a tiny triangle"
                ],
                "answer": 0,
                "hint": "Units must line up consecutively in a continuous line.",
                "explanation": "Accurate linear measurement requires units to meet end-to-end without overlapping or leaving empty gaps.",
                "solution_steps": [
                    "Recall the fundamental rule of unit iteration in measurement.",
                    "Any overlap underestimates the true length; any gap overestimates it.",
                    "Therefore, placing strings end-to-end with zero gaps and zero overlap gives the true perimeter."
                ]
            },
            {
                "question": "On a costume mask, the left curled moustache is 9 cm long. By mirror symmetry, what must be the length of the right curl?",
                "options": ["Exactly 9 cm", "18 cm", "4.5 cm", "12 cm"],
                "answer": 0,
                "hint": "Bilateral symmetry means the two opposite halves are identical in length.",
                "explanation": "Bilateral mirror symmetry requires matching parts on either side of the axis of symmetry to have identical lengths.",
                "solution_steps": [
                    "Identify the central line of symmetry running vertically down the nose of the mask.",
                    "Recognize that mirror reflection preserves segment length exactly.",
                    "Conclude that the right curl must measure exactly 9 cm to match the left curl."
                ]
            },
            {
                "question": "A string of festive party lights has 20 small bulbs spaced 5 cm apart. What is the distance from the 1st to the 2nd bulb?",
                "options": ["5 cm", "10 cm", "20 cm", "100 cm"],
                "answer": 0,
                "hint": "Look at the spacing given between consecutive bulbs.",
                "explanation": "The problem states that consecutive bulbs are spaced 5 cm apart, so the distance between bulb 1 and 2 is 5 cm.",
                "solution_steps": [
                    "Read the given spacing between adjacent bulbs: 5 cm.",
                    "Identify that the gap between the 1st and 2nd bulb is exactly one interval.",
                    "Conclude the distance is 1 interval × 5 cm = 5 cm."
                ]
            },
            {
                "question": "Why is a flexible cotton cord better than a wooden ruler for finding the distance around a round tree trunk?",
                "options": [
                    "It bends smoothly around curves to match the circular perimeter",
                    "It is heavier than wood",
                    "It changes length when pulled",
                    "It cannot be cut with scissors"
                ],
                "answer": 0,
                "hint": "Think about the shape of a curved surface.",
                "explanation": "A flexible cord can curve around cylindrical objects like tree trunks or round pillars where rigid rulers cannot bend.",
                "solution_steps": [
                    "Identify that a tree trunk has a curved circular boundary (perimeter).",
                    "Note that rigid wooden rulers only measure along straight lines.",
                    "Conclude that a flexible cord conforms to the curve, allowing direct circumference measurement."
                ]
            },
            {
                "question": "If 1 decorative paper ribbon measures 15 cm, how long is a border made of 4 identical ribbons placed end-to-end?",
                "options": ["60 cm", "45 cm", "50 cm", "30 cm"],
                "answer": 0,
                "hint": "Multiply the length of 1 ribbon by 4.",
                "explanation": "4 ribbons × 15 cm each = 60 cm total border length.",
                "solution_steps": [
                    "Identify the unit length: 1 ribbon = 15 cm.",
                    "Multiply by the number of ribbons: 4 × 15 cm.",
                    "Calculate 4 × 15 = 60 cm."
                ]
            },
            {
                "question": "Which of these is a non-standard unit of length?",
                "options": ["A child's footstep pace", "A centimetre", "A metre", "A kilometre"],
                "answer": 0,
                "hint": "Standard units have fixed, universal values defined by international agreement.",
                "explanation": "A footstep pace varies from person to person, making it an informal or non-standard unit.",
                "solution_steps": [
                    "Define standard units: units with fixed universal definitions (centimetre, metre, kilometre).",
                    "Define non-standard units: body-based or informal units that vary across people.",
                    "Identify footstep pace as a non-standard, variable unit."
                ]
            },
            {
                "question": "A bulletin board perimeter requires 18 paper strips. If the top and bottom need 6 strips each, how many strips does each side need?",
                "options": ["3 strips", "6 strips", "4 strips", "2 strips"],
                "answer": 0,
                "hint": "Total = 18. Subtract top and bottom, then divide the remainder by 2 sides.",
                "explanation": "Top + bottom = 6 + 6 = 12 strips. Remaining for 2 sides = 18 - 12 = 6 strips. Each side = 6 ÷ 2 = 3 strips.",
                "solution_steps": [
                    "Calculate horizontal borders: 6 + 6 = 12 strips.",
                    "Subtract from total perimeter: 18 - 12 = 6 strips for both vertical sides.",
                    "Divide equally between the two vertical sides: 6 ÷ 2 = 3 strips per side."
                ]
            }
        ]
    },

    # Slide 18: Challenge 2 (Spatial Clearance, Proportions & Standard Units)
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Doorway clearances, bridge heights, body ratios, and the international standard metre",
        "questions": [
            {
                "question": "A table is 110 cm long, 65 cm wide, and 75 cm high. An open door is 80 cm wide. How can the table pass through?",
                "options": [
                    "Turn it sideways so its 65 cm width or 75 cm height faces the 80 cm door",
                    "Push it harder flat so it breaks the doorposts",
                    "It is impossible for the table to pass",
                    "Cut the tabletop in half with a saw"
                ],
                "answer": 0,
                "hint": "Compare all three dimensions of the table to the door width.",
                "explanation": "While length (110 cm) exceeds 80 cm, breadth (65 cm) and height (75 cm) are both less than 80 cm, allowing passage when turned.",
                "solution_steps": [
                    "Compare table length (110 cm) with door width (80 cm): 110 > 80 (cannot pass flat).",
                    "Compare table width (65 cm) and height (75 cm) with door width: 65 < 80 and 75 < 80.",
                    "Conclude that rotating the table sideways allows it to pass through easily."
                ]
            },
            {
                "question": "A toy bridge has a vertical clearance of 14 cm. Which toy vehicle CANNOT pass underneath?",
                "options": [
                    "A toy giraffe wagon that is 16 cm tall",
                    "A toy sports car that is 4 cm tall",
                    "A toy delivery van that is 11 cm tall",
                    "A toy skateboard that is 3 cm tall"
                ],
                "answer": 0,
                "hint": "Any object taller than the 14 cm opening will collide with the bridge span.",
                "explanation": "At 16 cm tall, the giraffe wagon exceeds the 14 cm bridge clearance (16 cm > 14 cm) and gets stuck.",
                "solution_steps": [
                    "Check the bridge clearance limit: 14 cm maximum height.",
                    "Compare each toy's height against 14 cm: 4 < 14, 11 < 14, 3 < 14, but 16 > 14.",
                    "Conclude that the 16 cm giraffe wagon cannot pass underneath."
                ]
            },
            {
                "question": "According to typical human anatomical proportions, which body measurement is roughly equal to foot length?",
                "options": ["Forearm length (inner elbow to wrist)", "Neck circumference", "Hand thickness", "Ear height"],
                "answer": 0,
                "hint": "You can test this by placing the bottom of your shoe along your inner arm.",
                "explanation": "In human body proportions, the forearm length from the elbow crease to the wrist matches foot length.",
                "solution_steps": [
                    "Recall natural body proportions discovered in classical anatomy.",
                    "Note that forearm length (elbow to wrist) corresponds closely to foot length.",
                    "Conclude that forearm length is the matching measurement."
                ]
            },
            {
                "question": "If a person's outstretched arm span from fingertip to fingertip is 130 cm, what is their approximate standing height?",
                "options": ["Approximately 130 cm", "Exactly 65 cm", "Approximately 260 cm", "Approximately 30 cm"],
                "answer": 0,
                "hint": "Vitruvian proportions link arm span directly to standing height.",
                "explanation": "Human body proportions show that outstretched arm span is approximately equal to total standing height.",
                "solution_steps": [
                    "Recall the anatomical proportion: arm span ≈ standing height.",
                    "Substitute the given arm span: 130 cm.",
                    "Conclude that standing height is approximately 130 cm."
                ]
            },
            {
                "question": "What is the primary international metric standard unit of length?",
                "options": ["Metre (m)", "Handspan", "Cubit", "Footstep"],
                "answer": 0,
                "hint": "It is abbreviated as small letter m.",
                "explanation": "The metre (symbol: m) is the base unit of length in the International System of Units (SI).",
                "solution_steps": [
                    "Identify the international standard system for measurement (metric system).",
                    "Recognize that the metre (m) is the universal base unit of length.",
                    "Eliminate informal body-based units (handspan, cubit, footstep)."
                ]
            },
            {
                "question": "How many centimetres make up exactly 1 standard metre?",
                "options": ["100 cm", "10 cm", "50 cm", "1,000 cm"],
                "answer": 0,
                "hint": "The prefix 'centi' means one-hundredth.",
                "explanation": "By definition, 1 metre equals exactly 100 centimetres (1 m = 100 cm).",
                "solution_steps": [
                    "Recall the metric prefix definition: centi- means 1/100th of a metre.",
                    "Therefore, 100 centimetres are contained in 1 full metre.",
                    "State the fundamental relationship: 1 m = 100 cm."
                ]
            },
            {
                "question": "A cloth merchant uses a metal metre rod. Why is this better than measuring with an arm length?",
                "options": [
                    "The metal rod gives an identical, fair measurement regardless of who is measuring",
                    "The metal rod is heavier to carry",
                    "The metal rod changes length when it rains",
                    "Arm lengths are always the same for all humans"
                ],
                "answer": 0,
                "hint": "Standard tools provide consistency and eliminate personal size bias.",
                "explanation": "Standardized metal rods ensure fair, repeatable measurements that do not depend on the physical size of the merchant's arms.",
                "solution_steps": [
                    "Recognize that human arm lengths vary widely across different individuals.",
                    "Understand that buying from a merchant with short arms would yield less fabric.",
                    "Conclude that a rigid metal metre rod guarantees equal, fair, and reliable trade for everyone."
                ]
            },
            {
                "question": "A box tunnel has a width of 20 cm and height of 15 cm. A toy truck is 18 cm wide and 12 cm tall. Can it pass through?",
                "options": [
                    "Yes, because both width (18 < 20) and height (12 < 15) fit within the clearance",
                    "No, because the truck is too wide",
                    "No, because the truck is too tall",
                    "Only if the truck is turned upside down"
                ],
                "answer": 0,
                "hint": "Check both dimensions: truck width vs tunnel width, truck height vs tunnel height.",
                "explanation": "Truck width 18 cm < 20 cm tunnel width, and truck height 12 cm < 15 cm tunnel height. Both clearances are satisfied.",
                "solution_steps": [
                    "Compare horizontal clearance: 18 cm truck width < 20 cm tunnel width (fits with 2 cm spare).",
                    "Compare vertical clearance: 12 cm truck height < 15 cm tunnel height (fits with 3 cm spare).",
                    "Conclude that the toy truck passes through smoothly."
                ]
            },
            {
                "question": "A strip of paper wrapped around a child's head measures roughly how many handspans?",
                "options": ["Roughly 3 handspans", "Roughly 10 handspans", "Roughly 1 handspan", "Roughly 20 handspans"],
                "answer": 0,
                "hint": "This common body measurement rule connects head circumference to handspan.",
                "explanation": "In typical children's body proportions, head circumference is approximately 3 handspans.",
                "solution_steps": [
                    "Recall the costume-making classroom activity from the textbook.",
                    "Verify the body proportion rule: head circumference ≈ 3 handspans.",
                    "Confirm that roughly 3 handspans wraps around the forehead."
                ]
            },
            {
                "question": "A student paces a room and counts 12 paces. A teacher paces the same room and counts 8 paces. Why did the teacher count fewer paces?",
                "options": [
                    "The teacher has a longer stride than the student",
                    "The teacher walked in circles",
                    "The room shrank when the teacher walked",
                    "The teacher has a shorter stride than the student"
                ],
                "answer": 0,
                "hint": "Longer steps cover more ground per pace.",
                "explanation": "Because an adult teacher has longer legs and a longer stride, each step covers more distance, requiring fewer total paces.",
                "solution_steps": [
                    "Compare stride lengths: adult stride > child stride.",
                    "Recognize that total distance = number of paces × pace length.",
                    "Conclude that longer paces yield a smaller count of 8 compared to 12."
                ]
            }
        ]
    },

    # Slide 19: Challenge 3 (Metre Knots, Height Benchmarks & Object Sorting)
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Knotted ropes, wall height categorization, environmental estimation, and half-metre folding",
        "questions": [
            {
                "question": "To make a 1-metre measuring rope, how far apart should the inner edges of the two knots be tied?",
                "options": ["Exactly 100 cm apart", "Exactly 50 cm apart", "Exactly 10 cm apart", "Exactly 1,000 cm apart"],
                "answer": 0,
                "hint": "1 metre is defined as 100 centimetres.",
                "explanation": "A 1-metre measuring rope must have its knots placed exactly 100 cm apart to match standard metric length.",
                "solution_steps": [
                    "Identify the definition of 1 standard metre: 1 m = 100 cm.",
                    "Ensure the distance between the two knots represents this standard distance.",
                    "Conclude the knots must be tied exactly 100 cm apart."
                ]
            },
            {
                "question": "A child stands against the 1-metre wall line and the top of their head is at 112 cm. How much taller than 1 metre are they?",
                "options": ["12 cm taller", "2 cm taller", "112 cm taller", "10 cm taller"],
                "answer": 0,
                "hint": "Subtract 100 cm (1 metre) from 112 cm.",
                "explanation": "112 cm - 100 cm = 12 cm above the 1-metre mark.",
                "solution_steps": [
                    "Convert 1 metre to centimetres: 1 m = 100 cm.",
                    "Subtract the 1-metre benchmark from the standing height: 112 cm - 100 cm.",
                    "Calculate the difference: 12 cm taller than 1 metre."
                ]
            },
            {
                "question": "Another student stands at 94 cm against the 1-metre wall line. How many centimetres do they need to reach 1 metre?",
                "options": ["6 cm", "14 cm", "10 cm", "4 cm"],
                "answer": 0,
                "hint": "Calculate how much to add to 94 to make 100.",
                "explanation": "100 cm - 94 cm = 6 cm needed to reach the 1-metre line.",
                "solution_steps": [
                    "Identify the target benchmark: 1 metre = 100 cm.",
                    "Current height = 94 cm.",
                    "Calculate needed difference: 100 - 94 = 6 cm."
                ]
            },
            {
                "question": "Which of these classroom objects is typically LESS than 1 metre long?",
                "options": ["A student pencil box", "The classroom door height", "The main chalkboard length", "A full-size teacher table length"],
                "answer": 0,
                "hint": "Think about which item fits easily into a student backpack.",
                "explanation": "A pencil box is around 20 cm long, which is significantly less than 1 metre (100 cm).",
                "solution_steps": [
                    "Estimate the length of a pencil box: approximately 20 cm.",
                    "Compare with 1 metre (100 cm): 20 cm < 100 cm.",
                    "Conclude that the pencil box belongs to the 'less than 1 metre' category."
                ]
            },
            {
                "question": "Which everyday object has a length that is approximately EQUAL to 1 metre?",
                "options": ["The height of an ordinary school study desk", "A fingernail", "An eraser", "A railway train carriage"],
                "answer": 0,
                "hint": "Look for an object that reaches approximately waist height on an adult.",
                "explanation": "A school study desk or guitar is typically around 75 to 100 cm tall, closely approximating 1 metre.",
                "solution_steps": [
                    "Recall standard classroom benchmarks: fingernail is ~1 cm, train is ~25 m.",
                    "Consider a study desk: height is roughly 75 to 100 cm.",
                    "Conclude that a study desk serves as a reliable 1-metre benchmark."
                ]
            },
            {
                "question": "When a 1-metre rope is folded in half so its ends touch, what is the length of each half?",
                "options": ["50 cm (or 1/2 metre)", "25 cm", "75 cm", "10 cm"],
                "answer": 0,
                "hint": "Divide 100 cm by 2 equal parts.",
                "explanation": "Half of 1 metre (100 cm) is 100 ÷ 2 = 50 cm, or 1/2 metre.",
                "solution_steps": [
                    "Start with the whole length: 1 m = 100 cm.",
                    "Divide into 2 equal halves: 100 cm ÷ 2.",
                    "Calculate 50 cm, which represents one-half of a metre (1/2 m)."
                ]
            },
            {
                "question": "A tall glass storage jar measures 50 cm in height. What fraction of a metre is its height?",
                "options": ["1/2 metre", "1/4 metre", "3/4 metre", "1 whole metre"],
                "answer": 0,
                "hint": "50 cm out of 100 cm simplifies to what fraction?",
                "explanation": "50 cm out of 100 cm is 50/100 = 1/2 of a metre.",
                "solution_steps": [
                    "Express the height as a fraction of a metre: 50 cm / 100 cm.",
                    "Simplify the fraction by dividing numerator and denominator by 50.",
                    "Obtain 1/2 metre."
                ]
            },
            {
                "question": "How many half-metre cords placed end-to-end are needed to measure a 3-metre wall?",
                "options": ["6 half-metre cords", "3 half-metre cords", "2 half-metre cords", "12 half-metre cords"],
                "answer": 0,
                "hint": "Each metre contains 2 half-metres. Multiply 3 metres by 2.",
                "explanation": "Since each metre has 2 half-metres, 3 metres require 3 × 2 = 6 half-metre cords.",
                "solution_steps": [
                    "Recall that 1 metre = 2 half-metres.",
                    "Multiply by 3 metres: 3 × 2 half-metres.",
                    "Calculate 6 half-metre cords in total."
                ]
            },
            {
                "question": "If a ribbon is 2 metres and 50 cm long, how many total centimetres is that?",
                "options": ["250 cm", "205 cm", "520 cm", "70 cm"],
                "answer": 0,
                "hint": "2 metres = 200 cm. Add the extra 50 cm.",
                "explanation": "2 metres = 2 × 100 cm = 200 cm. Adding 50 cm gives 200 + 50 = 250 cm.",
                "solution_steps": [
                    "Convert 2 metres to centimetres: 2 × 100 cm = 200 cm.",
                    "Add the remaining 50 cm: 200 cm + 50 cm.",
                    "Total length = 250 cm."
                ]
            },
            {
                "question": "A student measures the classroom door and finds it is 200 cm tall. How many metres is this?",
                "options": ["2 metres", "20 metres", "1.5 metres", "4 metres"],
                "answer": 0,
                "hint": "Divide 200 cm by 100 cm per metre.",
                "explanation": "200 cm ÷ 100 cm/m = 2 metres.",
                "solution_steps": [
                    "Recall that 100 cm = 1 metre.",
                    "Divide total centimetres by 100: 200 ÷ 100.",
                    "Conclude that the door height is exactly 2 metres."
                ]
            }
        ]
    },

    # Slide 20: Challenge 4 (Quarter Metres, Practical Estimations & Rope Calculations)
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Quarter metres, three-quarters, jump distances, rope cuts, and perimeter problem solving",
        "questions": [
            {
                "question": "A 1-metre rope is folded in half, and then folded in half again. How long is each of the 4 equal parts?",
                "options": ["25 cm (1/4 metre)", "50 cm", "75 cm", "20 cm"],
                "answer": 0,
                "hint": "Divide 100 cm by 4 equal segments.",
                "explanation": "Folding in half gives 50 cm; folding in half again gives 50 ÷ 2 = 25 cm, which is 1/4 of a metre.",
                "solution_steps": [
                    "First fold: 100 cm ÷ 2 = 50 cm (half metre).",
                    "Second fold: 50 cm ÷ 2 = 25 cm (quarter metre).",
                    "Conclude each of the 4 equal segments is 25 cm (1/4 m)."
                ]
            },
            {
                "question": "What is the length of three-quarters of a metre (3/4 m) in centimetres?",
                "options": ["75 cm", "25 cm", "50 cm", "80 cm"],
                "answer": 0,
                "hint": "Multiply 25 cm (one quarter) by 3.",
                "explanation": "3 × 25 cm = 75 cm, which is three-quarters of a metre.",
                "solution_steps": [
                    "Identify that 1/4 m = 25 cm.",
                    "Calculate 3/4 m: 3 × 25 cm.",
                    "Calculate 3 × 25 = 75 cm."
                ]
            },
            {
                "question": "If you combine one quarter-metre (25 cm) and one half-metre (50 cm), what total length do you get?",
                "options": ["75 cm (or 3/4 metre)", "100 cm", "50 cm", "25 cm"],
                "answer": 0,
                "hint": "Add 25 cm and 50 cm.",
                "explanation": "25 cm + 50 cm = 75 cm, which is 3/4 of a metre.",
                "solution_steps": [
                    "Identify the lengths: quarter-metre = 25 cm, half-metre = 50 cm.",
                    "Add the two lengths together: 25 + 50.",
                    "Obtain 75 cm, which equals 3/4 metre."
                ]
            },
            {
                "question": "How many cuts with a pair of scissors are needed to divide a straight piece of wool into 4 equal pieces?",
                "options": ["3 cuts", "4 cuts", "2 cuts", "5 cuts"],
                "answer": 0,
                "hint": "Each cut increases the number of pieces by 1.",
                "explanation": "1 cut makes 2 pieces, 2 cuts make 3 pieces, and 3 cuts make 4 pieces.",
                "solution_steps": [
                    "Notice that n pieces of a single cord require n - 1 cuts.",
                    "For 4 pieces, calculate: 4 - 1 = 3 cuts.",
                    "Conclude that exactly 3 cuts divide the wool into 4 pieces."
                ]
            },
            {
                "question": "In a playground standing broad jump, a learner leaps 145 cm. Between which two benchmarks did they land?",
                "options": [
                    "Between 1 metre (100 cm) and 1.5 metres (150 cm)",
                    "Between 0.5 metres and 1 metre",
                    "Between 1.5 metres and 2 metres",
                    "Beyond 2 metres"
                ],
                "answer": 0,
                "hint": "Compare 145 cm with 100 cm and 150 cm.",
                "explanation": "145 cm is greater than 100 cm (1 m) and less than 150 cm (1.5 m).",
                "solution_steps": [
                    "Convert 1 m to 100 cm and 1.5 m to 150 cm.",
                    "Locate 145 cm on the number line: 100 < 145 < 150.",
                    "Conclude the learner landed between 1 metre and 1.5 metres."
                ]
            },
            {
                "question": "If one natural footstep covers 50 cm, how many footsteps are needed to walk a 6-metre hallway?",
                "options": ["12 footsteps", "6 footsteps", "3 footsteps", "24 footsteps"],
                "answer": 0,
                "hint": "Each metre takes 2 footsteps. Multiply 6 by 2.",
                "explanation": "Since 1 metre = 100 cm = 2 footsteps of 50 cm, 6 metres require 6 × 2 = 12 footsteps.",
                "solution_steps": [
                    "Find footsteps per metre: 100 cm ÷ 50 cm = 2 footsteps.",
                    "Multiply by total metres: 6 metres × 2 footsteps/metre.",
                    "Calculate 12 footsteps in total."
                ]
            },
            {
                "question": "A classroom has 2 long walls of 7 metres each and 2 short walls of 5 metres each. What is the total perimeter?",
                "options": ["24 metres", "12 metres", "35 metres", "14 metres"],
                "answer": 0,
                "hint": "Add all 4 walls: 7 + 7 + 5 + 5.",
                "explanation": "Perimeter = 7 + 7 + 5 + 5 = 14 + 10 = 24 metres.",
                "solution_steps": [
                    "Add the two long walls: 7 m + 7 m = 14 m.",
                    "Add the two short walls: 5 m + 5 m = 10 m.",
                    "Total perimeter = 14 m + 10 m = 24 metres."
                ]
            },
            {
                "question": "How many 25 cm gift ribbons can be cut from a single 1-metre long ribbon roll?",
                "options": ["4 ribbons", "2 ribbons", "5 ribbons", "10 ribbons"],
                "answer": 0,
                "hint": "How many 25s are in 100?",
                "explanation": "1 metre = 100 cm. 100 cm ÷ 25 cm = 4 ribbons.",
                "solution_steps": [
                    "Convert 1 metre to centimetres: 1 m = 100 cm.",
                    "Divide total length by ribbon size: 100 ÷ 25.",
                    "Calculate exactly 4 ribbons."
                ]
            },
            {
                "question": "A throw lands at 7 metres and 25 centimetres. How is this written in fractional metres?",
                "options": ["7 and 1/4 metres", "7 and 1/2 metres", "7 and 3/4 metres", "8 metres"],
                "answer": 0,
                "hint": "25 cm is what fraction of 1 metre?",
                "explanation": "Since 25 cm = 1/4 metre, 7 metres and 25 cm equals 7 and 1/4 metres.",
                "solution_steps": [
                    "Recall that 25 cm out of 100 cm is 1/4 of a metre.",
                    "Combine with the whole metres: 7 whole metres + 1/4 metre.",
                    "Express as mixed measurement: 7 and 1/4 metres."
                ]
            },
            {
                "question": "A piece of rope is 1 metre long. If you cut off 30 cm, how much rope remains?",
                "options": ["70 cm", "60 cm", "80 cm", "50 cm"],
                "answer": 0,
                "hint": "Subtract 30 cm from 100 cm.",
                "explanation": "1 metre = 100 cm. 100 cm - 30 cm = 70 cm remaining.",
                "solution_steps": [
                    "Convert 1 metre to centimetres: 1 m = 100 cm.",
                    "Subtract the cut piece: 100 cm - 30 cm.",
                    "Calculate 70 cm remaining."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    for s in slides_part3:
        title_wc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_wc} words) -> {len(s['questions'])} questions")
        assert 1 <= title_wc <= 3, f"Title {s['title']} not 1-3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} must have 10 questions"
        for q in s["questions"]:
            assert len(q["options"]) == 4, f"Question must have 4 options"
            assert len(q["solution_steps"]) == 3, f"Question must have 3 solution steps"
    print("All slides in Part 3 passed strict validation!")

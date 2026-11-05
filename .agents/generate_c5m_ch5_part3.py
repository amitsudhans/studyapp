#!/usr/bin/env python3
"""
Generate Slides 17 to 20 (4 Mastery Challenges = 40 Quiz Questions)
for NCERT Class 5 Mathematics - Chapter 5: Far and Near
"""

slides_17_to_20 = [
    {
        "id": 17,
        "heading": "Challenge 1",
        "tagline": "Mastery Quiz: Choosing Units, Equivalences, Comparisons, and Tallest Statues",
        "color": "from-indigo-600 to-purple-700",
        "badge": "Mastery Challenge • Part 1",
        "audio_text": (
            "Welcome to Challenge 1! Test your foundational mastery of selecting sensible metric units, converting centimetres to metres, applying inequalities, and analyzing monument height data. "
            "Examine each question carefully, choose the correct answer, and review the detailed step-by-step solution modal for complete mathematical clarity."
        ),
        "quizzes": [
            {
                "question": "Which unit is most appropriate to measure the depth of a village open water well?",
                "options": ["Metres (m)", "Centimetres (cm)", "Kilometres (km)", "Millimetres (mm)"],
                "correct": 0,
                "solution_html": "A typical open well is 10 to 20 metres deep, making metres the most sensible and practical unit."
            },
            {
                "question": "How many centimetres are there in 1 metre?",
                "options": ["100 cm", "10 cm", "1,000 cm", "50 cm"],
                "correct": 0,
                "solution_html": "1 metre is defined as exactly 100 centimetres (1 m = 100 cm)."
            },
            {
                "question": "How is 385 cm expressed in mixed metres and centimetres?",
                "options": ["3 m 85 cm", "38 m 5 cm", "30 m 85 cm", "3 m 8 cm"],
                "correct": 0,
                "solution_html": "385 cm = 300 cm + 85 cm = 3 m 85 cm."
            },
            {
                "question": "Which symbol correctly compares: 6 m 25 cm ___ 650 cm?",
                "options": ["< (Less than)", "> (Greater than)", "= (Equal to)", "≥ (Greater than or equal)"],
                "correct": 0,
                "solution_html": "6 m 25 cm = 625 cm. Since 625 cm < 650 cm, 6 m 25 cm < 650 cm."
            },
            {
                "question": "How tall is the Statue of Unity in Gujarat, India?",
                "options": ["182 metres", "128 metres", "93 metres", "210 metres"],
                "correct": 0,
                "solution_html": "The Statue of Unity stands at 182 metres, making it the tallest statue in the world."
            },
            {
                "question": "The Statue of Liberty is 93 m and Spring Temple Buddha is 128 m. What is their height difference?",
                "options": ["35 metres", "25 metres", "45 metres", "38 metres"],
                "correct": 0,
                "solution_html": "128 m - 93 m = 35 metres."
            },
            {
                "question": "A table cloth is 2 metres and 50 centimetres long. What is its length in centimetres?",
                "options": ["250 cm", "205 cm", "2,500 cm", "25 cm"],
                "correct": 0,
                "solution_html": "2 m = 200 cm. 200 cm + 50 cm = 250 cm."
            },
            {
                "question": "Which of these lengths is the longest: 4 m, 380 cm, or 4 m 15 cm?",
                "options": ["4 m 15 cm (415 cm)", "4 m (400 cm)", "380 cm", "They are all equal"],
                "correct": 0,
                "solution_html": "Converting all to cm: 4 m = 400 cm; 380 cm; 4 m 15 cm = 415 cm. 415 cm is the longest."
            },
            {
                "question": "Why is kilometres the preferred unit for inter-city highways instead of metres?",
                "options": ["Highway distances are vast; writing 250 km is simpler than writing 250,000 m", "Kilometres are cheaper to measure", "Metres cannot be measured outdoors", "Road signs only have space for two letters"],
                "correct": 0,
                "solution_html": "Using kilometres keeps numerical values manageable and easy to read on highway milestone signs."
            },
            {
                "question": "A cotton stole is 2 metres long. How many 50-centimetre handkerchiefs can be cut from it?",
                "options": ["4 handkerchiefs (200 / 50)", "2 handkerchiefs", "5 handkerchiefs", "10 handkerchiefs"],
                "correct": 0,
                "solution_html": "2 metres = 200 cm. 200 cm / 50 cm = 4 handkerchiefs."
            }
        ]
    },
    {
        "id": 18,
        "heading": "Challenge 2",
        "tagline": "Mastery Quiz: Measuring Instruments, Kilometres, Race Logistics, and Railway Records",
        "color": "from-teal-600 to-emerald-700",
        "badge": "Mastery Challenge • Part 2",
        "audio_text": (
            "Welcome to Challenge 2! Test your understanding of outdoor measuring wheels, laser distance meters, kilometre conversions, race planning, and the Vivek Express rail route. "
            "Calculate each step methodically and inspect the solution modal whenever you need guidance."
        ),
        "quizzes": [
            {
                "question": "What is a rolling wheel tool used by road surveyors to measure ground distances called?",
                "options": ["A measuring wheel (rodometer)", "A galvanometer", "A protractor", "A micrometer screw"],
                "correct": 0,
                "solution_html": "A measuring wheel (rodometer) tracks revolutions as it rolls along the ground to measure distance."
            },
            {
                "question": "How many metres are in 1 kilometre?",
                "options": ["1,000 metres", "100 metres", "10 metres", "10,000 metres"],
                "correct": 0,
                "solution_html": "1 kilometre equals 1,000 metres (1 km = 1,000 m)."
            },
            {
                "question": "In a 3-km race course, how many total metres must the participants run?",
                "options": ["3,000 metres", "300 metres", "30,000 metres", "1,500 metres"],
                "correct": 0,
                "solution_html": "3 km = 3 × 1,000 m = 3,000 metres."
            },
            {
                "question": "If water stations are placed every 500 metres on a 3-km course, at which mark is Station 3 located?",
                "options": ["1,500 metres (1.5 km)", "1,000 metres", "2,000 metres", "500 metres"],
                "correct": 0,
                "solution_html": "Station 1 = 500 m; Station 2 = 1,000 m; Station 3 = 1,500 m (1.5 km)."
            },
            {
                "question": "What is the total distance of the Vivek Express route from Dibrugarh to Kanniyakumari?",
                "options": ["4,189 km", "3,500 km", "2,850 km", "5,200 km"],
                "correct": 0,
                "solution_html": "The Vivek Express covers 4,189 km across 9 Indian states, making it India's longest train route."
            },
            {
                "question": "How many metres are in half a kilometre (1/2 km)?",
                "options": ["500 metres", "250 metres", "100 metres", "750 metres"],
                "correct": 0,
                "solution_html": "1/2 of 1,000 metres = 500 metres."
            },
            {
                "question": "A runner completes five 400-metre laps around an athletics track. How many kilometres did they run?",
                "options": ["2 km (5 × 400 m = 2,000 m = 2 km)", "1 km", "3 km", "4 km"],
                "correct": 0,
                "solution_html": "5 × 400 m = 2,000 m. Since 1,000 m = 1 km, 2,000 m = 2 km."
            },
            {
                "question": "A laser distance meter measures a hall to be 45.5 metres. How many centimetres is this?",
                "options": ["4,550 cm", "455 cm", "45,500 cm", "45 cm"],
                "correct": 0,
                "solution_html": "45.5 m × 100 = 4,550 cm."
            },
            {
                "question": "If a train travels 750 km on Day 1 and 825 km on Day 2, what is the combined distance?",
                "options": ["1,575 km", "1,550 km", "1,675 km", "1,475 km"],
                "correct": 0,
                "solution_html": "750 + 825 = 1,575 km."
            },
            {
                "question": "How many metres are in 2 km 350 m?",
                "options": ["2,350 metres", "235 metres", "23,500 metres", "2,035 metres"],
                "correct": 0,
                "solution_html": "2 km = 2,000 m. 2,000 m + 350 m = 2,350 metres."
            }
        ]
    },
    {
        "id": 19,
        "heading": "Challenge 3",
        "tagline": "Mastery Quiz: Millimetres, Sprout Tracking, Precision Lines, and Addition of Lengths",
        "color": "from-cyan-600 to-blue-700",
        "badge": "Mastery Challenge • Part 3",
        "audio_text": (
            "Welcome to Challenge 3! Dive into millimetre precision, sprout growth tracking, exact line segment drafting, and mixed-unit column additions. "
            "Solve each problem with speed and precision, and check your reasoning with the solution modal."
        ),
        "quizzes": [
            {
                "question": "How many millimetres are there in 1 centimetre?",
                "options": ["10 mm", "100 mm", "1,000 mm", "5 mm"],
                "correct": 0,
                "solution_html": "Each centimetre contains 10 equal millimetres (1 cm = 10 mm)."
            },
            {
                "question": "A sprouted moong seed measured 5 mm on Day 1 and 12 mm on Day 2. What was its daily growth?",
                "options": ["7 mm (12 - 5)", "17 mm", "6 mm", "8 mm"],
                "correct": 0,
                "solution_html": "Growth = 12 mm - 5 mm = 7 mm."
            },
            {
                "question": "A line segment is 68 millimetres long. Express this in centimetres and millimetres.",
                "options": ["6 cm 8 mm", "68 cm", "60 cm 8 mm", "6 cm 80 mm"],
                "correct": 0,
                "solution_html": "68 mm = 60 mm + 8 mm = 6 cm 8 mm."
            },
            {
                "question": "What is the sum of 3 m 45 cm and 2 m 75 cm?",
                "options": ["6 m 20 cm", "5 m 20 cm", "6 m 15 cm", "5 m 120 cm"],
                "correct": 0,
                "solution_html": "cm: 45 + 75 = 120 cm = 1 m 20 cm (write 20, carry 1 m). Metres: 3 + 2 + 1 = 6 m. Total = 6 m 20 cm."
            },
            {
                "question": "Add 4 km 500 m and 3 km 800 m.",
                "options": ["8 km 300 m", "7 km 300 m", "8 km 400 m", "7 km 1,300 m"],
                "correct": 0,
                "solution_html": "m: 500 + 800 = 1,300 m = 1 km 300 m. km: 4 + 3 + 1 = 8 km. Total = 8 km 300 m."
            },
            {
                "question": "How many millimetres are in 4 cm 5 mm?",
                "options": ["45 mm", "405 mm", "54 mm", "450 mm"],
                "correct": 0,
                "solution_html": "4 cm = 40 mm. 40 mm + 5 mm = 45 mm."
            },
            {
                "question": "A pencil is 14 cm 2 mm long. Express its length in millimetres alone.",
                "options": ["142 mm", "140 mm", "14.2 mm", "1,420 mm"],
                "correct": 0,
                "solution_html": "14 cm = 140 mm. 140 mm + 2 mm = 142 mm."
            },
            {
                "question": "Add 2 m 60 cm, 1 m 40 cm, and 3 m 25 cm.",
                "options": ["7 m 25 cm", "6 m 25 cm", "7 m 15 cm", "6 m 125 cm"],
                "correct": 0,
                "solution_html": "cm: 60 + 40 + 25 = 125 cm = 1 m 25 cm. Metres: 2 + 1 + 3 + 1 = 7 m. Total = 7 m 25 cm."
            },
            {
                "question": "What is the thickness of a typical 5-rupee coin in millimetres?",
                "options": ["About 2 mm", "About 2 cm", "About 20 mm", "About 0.1 mm"],
                "correct": 0,
                "solution_html": "A standard coin is roughly 2 millimetres thick."
            },
            {
                "question": "On a double number line connecting cm and mm, what value aligns directly with 8 cm?",
                "options": ["80 mm", "8 mm", "800 mm", "0.8 mm"],
                "correct": 0,
                "solution_html": "8 cm × 10 = 80 mm."
            }
        ]
    },
    {
        "id": 20,
        "heading": "Challenge 4",
        "tagline": "Mastery Quiz: Subtraction, Scaling, Height Estimation, and Imperial Units",
        "color": "from-emerald-600 to-teal-700",
        "badge": "Mastery Challenge • Part 4",
        "audio_text": (
            "Welcome to the final challenge! Test your advanced mathematical mastery of length subtraction with borrowing, proportional fabric scaling, real-world estimation, and feet-inch conversions. "
            "Solve each puzzle, verify your score, and celebrate your mastery of Far and Near!"
        ),
        "quizzes": [
            {
                "question": "What is 8 m 20 cm minus 3 m 65 cm?",
                "options": ["4 m 55 cm", "5 m 55 cm", "4 m 45 cm", "5 m 45 cm"],
                "correct": 0,
                "solution_html": "Borrow 1 m (100 cm): 120 cm - 65 cm = 55 cm. Metres: 7 - 3 = 4 m. Result = 4 m 55 cm."
            },
            {
                "question": "A 10-km marathon route has 4 km 350 m completed. How much distance remains?",
                "options": ["5 km 650 m", "6 km 650 m", "5 km 750 m", "6 km 350 m"],
                "correct": 0,
                "solution_html": "10 km 000 m - 4 km 350 m: Borrow 1 km (1,000 m): 1,000 - 350 = 650 m. km: 9 - 4 = 5 km. Result = 5 km 650 m."
            },
            {
                "question": "If 1 shirt requires 2 m 25 cm of cloth, how much cloth is needed for 4 shirts?",
                "options": ["9 metres (8 m + 100 cm = 9 m)", "8 m 50 cm", "8 m 25 cm", "10 metres"],
                "correct": 0,
                "solution_html": "4 × 2 m = 8 m. 4 × 25 cm = 100 cm = 1 m. 8 m + 1 m = 9 metres."
            },
            {
                "question": "A 20-metre rope is divided equally into 4 pieces. What is the length of each piece?",
                "options": ["5 metres", "4 metres", "6 metres", "2.5 metres"],
                "correct": 0,
                "solution_html": "20 m / 4 = 5 metres."
            },
            {
                "question": "What is the estimated height of a 3-storey school building (standard floor height ~3 m)?",
                "options": ["About 9 metres", "About 3 metres", "About 20 metres", "About 30 metres"],
                "correct": 0,
                "solution_html": "3 storeys × ~3 metres per storey ≈ 9 metres."
            },
            {
                "question": "How many inches are there in 1 foot?",
                "options": ["12 inches", "10 inches", "100 inches", "24 inches"],
                "correct": 0,
                "solution_html": "1 foot is defined as exactly 12 inches."
            },
            {
                "question": "Approximately how many centimetres are in 1 inch?",
                "options": ["About 2.5 cm (2 cm 5 mm)", "About 1 cm", "About 5 cm", "About 10 cm"],
                "correct": 0,
                "solution_html": "1 inch is approximately 2.54 cm, commonly rounded to 2.5 cm (2 cm 5 mm)."
            },
            {
                "question": "A student measures 4 feet tall. Approximately what is their height in centimetres (1 foot ≈ 30 cm)?",
                "options": ["About 120 cm (4 × 30 cm)", "About 100 cm", "About 140 cm", "About 90 cm"],
                "correct": 0,
                "solution_html": "4 feet × ~30 cm/foot ≈ 120 cm."
            },
            {
                "question": "A classroom door is approximately 2 metres tall. A mango tree outside is twice as tall. What is its estimated height?",
                "options": ["4 metres", "6 metres", "2 metres", "8 metres"],
                "correct": 0,
                "solution_html": "2 × 2 metres = 4 metres."
            },
            {
                "question": "If 1 metre of curtain fabric costs ₹ 150, what is the cost of 3 metres and 50 centimetres (3.5 m)?",
                "options": ["₹ 525 (3 × 150 + 75)", "₹ 450", "₹ 500", "₹ 600"],
                "correct": 0,
                "solution_html": "3 m costs 3 × 150 = ₹ 450. 50 cm (half metre) costs ₹ 75. ₹ 450 + ₹ 75 = ₹ 525."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 17 to 20. Count: {len(slides_17_to_20)}")
    total_q = sum(len(s.get("quizzes", [])) for s in slides_17_to_20)
    print(f"Total Quiz Questions: {total_q}")


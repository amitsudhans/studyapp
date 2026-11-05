# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 8: Weight and Capacity
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4: 40 Questions total)
"""

challenge_slides = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Weight Estimation, Scale Readings & Equivalences",
        "lecture": "Welcome to Mastery Challenge 1. In this interactive session, you will test your understanding of real-world mass estimations, reading analog and digital weighing scales, and converting between kilograms and grams.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Test your mastery of mass estimation, scale reading, and metric conversions. Answer all 10 questions to unlock the detailed solutions!</p>",
        "questions": [
            {
                "id": "q1",
                "question": "Which of the following household items would have an estimated mass closest to 30 to 40 kg?",
                "options": [
                    "A plastic lunchbox filled with food",
                    "A standard two-seater living room sofa",
                    "A steel kitchen fork",
                    "An empty 1-litre water bottle"
                ],
                "answer": 1,
                "hint": "Think about furniture that requires two adults to lift comfortably.",
                "explanation": "A standard two-seater sofa weighs around 35 kg. A lunchbox is ~500 g, a fork is ~40 g, and an empty water bottle is ~50 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        <strong>Analysis of Mass Benchmarks:</strong>
                        <ul class='list-disc list-inside mt-1 space-y-1 text-slate-300'>
                            <li>Steel kitchen fork: ~30 to 50 g (grams)</li>
                            <li>Plastic lunchbox with food: ~400 to 600 g</li>
                            <li>Empty water bottle: ~30 to 50 g</li>
                            <li>Two-seater sofa: <strong>~30 to 40 kg (kilograms)</strong></li>
                        </ul>
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: A standard two-seater living room sofa (~35 kg).</p>
                </div>
                """
            },
            {
                "id": "q2",
                "question": "An analog spring scale has a dial where the interval between 4 kg and 5 kg is subdivided into 4 equal spaces. If the dial pointer rests on the 3rd mark past 4 kg, what weight is displayed?",
                "options": [
                    "4 kg 300 g",
                    "4 kg 750 g",
                    "4 kg 250 g",
                    "4 kg 500 g"
                ],
                "answer": 1,
                "hint": "Each of the 4 subdivisions equals 1,000 g ÷ 4 = 250 g.",
                "explanation": "1 kg = 1,000 g. 4 equal spaces mean each mark represents 1,000 ÷ 4 = 250 g. 3 marks past 4 kg = 4 kg + (3 × 250 g) = 4 kg 750 g (or 4 3/4 kg).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <p><strong>Step 1:</strong> Determine the value of one dial division:</p>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>Interval = 5 kg - 4 kg = 1 kg = 1,000 g<br>1 subdivision = 1,000 g ÷ 4 = 250 g</div>
                    <p><strong>Step 2:</strong> Add 3 subdivisions to 4 kg:</p>
                    <div class='p-2 rounded bg-slate-800 font-mono text-emerald-300'>4 kg + (3 × 250 g) = 4 kg + 750 g = 4 kg 750 g</div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 4 kg 750 g</p>
                </div>
                """
            },
            {
                "id": "q3",
                "question": "On a double number line connecting kilograms and grams, what gram value aligns exactly with 3 1/2 kg?",
                "options": [
                    "3,050 g",
                    "3,250 g",
                    "3,500 g",
                    "3,750 g"
                ],
                "answer": 2,
                "hint": "3 1/2 kg = 3 kg + 1/2 kg. We know 1/2 kg = 500 g.",
                "explanation": "3 kg = 3,000 g. 1/2 kg = 500 g. Adding them gives 3,000 + 500 = 3,500 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        3 1/2 kg = 3 kg + 0.5 kg<br>
                        3 kg = 3 × 1,000 g = 3,000 g<br>
                        0.5 kg = 0.5 × 1,000 g = 500 g<br>
                        Total = 3,000 g + 500 g = 3,500 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 3,500 g</p>
                </div>
                """
            },
            {
                "id": "q4",
                "question": "A grocer weighs a bag of pulses as 5 kg 8 g. What is this mass expressed in total grams?",
                "options": [
                    "5,800 g",
                    "5,080 g",
                    "5,008 g",
                    "580 g"
                ],
                "answer": 2,
                "hint": "8 grams requires two leading zeros in the three-digit gram placeholder: 008.",
                "explanation": "5 kg = 5,000 g. 8 g has 0 hundreds and 0 tens, so it is 008 g. Total = 5,000 + 8 = 5,008 g. 5,800 g would be 5 kg 800 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <p><strong>Three-Digit Placeholder Rule:</strong></p>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        5 kg = 5,000 g<br>
                        8 g = 008 g<br>
                        5,000 g + 008 g = 5,008 g
                    </div>
                    <p class='text-amber-300'>Note: 5,800 g is 5 kg 800 g; 5,080 g is 5 kg 80 g.</p>
                    <p class='text-emerald-400 font-bold'>Correct Option: 5,008 g</p>
                </div>
                """
            },
            {
                "id": "q5",
                "question": "Which of the following mathematical inequalities is TRUE?",
                "options": [
                    "2 kg 70 g > 2,700 g",
                    "3 kg 450 g < 3,045 g",
                    "4 kg 500 g = 4,500 g",
                    "1 kg 900 g > 2 kg"
                ],
                "answer": 2,
                "hint": "Convert both sides to grams: 4 kg 500 g = 4,500 g.",
                "explanation": "4 kg 500 g = 4,000 + 500 = 4,500 g, which equals 4,500 g. In option A, 2,070 g is NOT > 2,700 g. In option B, 3,450 g is NOT < 3,045 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-slate-300 space-y-1'>
                        <div>• 2 kg 70 g = 2,070 g (< 2,700 g) ➔ False</div>
                        <div>• 3 kg 450 g = 3,450 g (> 3,045 g) ➔ False</div>
                        <div>• 4 kg 500 g = 4,500 g (= 4,500 g) ➔ <strong>TRUE</strong></div>
                        <div>• 1 kg 900 g = 1,900 g (< 2,000 g) ➔ False</div>
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 4 kg 500 g = 4,500 g</p>
                </div>
                """
            },
            {
                "id": "q6",
                "question": "Convert 7,060 grams into compound units of kilograms and grams:",
                "options": [
                    "70 kg 60 g",
                    "7 kg 600 g",
                    "7 kg 60 g",
                    "7 kg 6 g"
                ],
                "answer": 2,
                "hint": "The thousands digit (7) represents kilograms; the remaining 3 digits (060) represent grams.",
                "explanation": "7,060 ÷ 1,000 = 7 with remainder 60. So 7,060 g = 7 kg 60 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        7,060 g = 7,000 g + 60 g<br>
                        7,000 g = 7 kg<br>
                        60 g = 60 g<br>
                        Result = 7 kg 60 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 7 kg 60 g</p>
                </div>
                """
            },
            {
                "id": "q7",
                "question": "Four backpacks weigh: Bag 1 = 3 kg 250 g, Bag 2 = 3,050 g, Bag 3 = 3 kg 400 g, Bag 4 = 3,200 g. What is the correct descending order of their weights?",
                "options": [
                    "Bag 3 > Bag 1 > Bag 4 > Bag 2",
                    "Bag 3 > Bag 4 > Bag 1 > Bag 2",
                    "Bag 2 > Bag 4 > Bag 1 > Bag 3",
                    "Bag 1 > Bag 3 > Bag 4 > Bag 2"
                ],
                "answer": 0,
                "hint": "Convert all to grams: Bag 1 = 3,250 g, Bag 2 = 3,050 g, Bag 3 = 3,400 g, Bag 4 = 3,200 g.",
                "explanation": "In grams: Bag 3 (3,400 g) > Bag 1 (3,250 g) > Bag 4 (3,200 g) > Bag 2 (3,050 g).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Bag 1: 3,250 g<br>
                        Bag 2: 3,050 g<br>
                        Bag 3: 3,400 g (Heaviest)<br>
                        Bag 4: 3,200 g<br>
                        Descending Order: 3,400 g > 3,250 g > 3,200 g > 3,050 g<br>
                        ➔ Bag 3 > Bag 1 > Bag 4 > Bag 2
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Bag 3 > Bag 1 > Bag 4 > Bag 2</p>
                </div>
                """
            },
            {
                "id": "q8",
                "question": "A fruit seller uses standard iron weights on a two-pan balance. To balance a 2 kg 750 g pumpkin, which combination of weights should he place on the opposite pan?",
                "options": [
                    "One 2 kg weight and one 500 g weight",
                    "Two 1 kg weights, one 500 g weight, and one 250 g weight",
                    "One 2 kg weight and three 200 g weights",
                    "Five 500 g weights"
                ],
                "answer": 1,
                "hint": "Find the combination that sums to exactly 2 kg + 750 g = 2,750 g.",
                "explanation": "Two 1 kg weights = 2,000 g. One 500 g + one 250 g = 750 g. Total = 2,000 + 750 = 2,750 g = 2 kg 750 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-emerald-300'>
                        Target = 2 kg 750 g = 2,750 g<br>
                        Option B: (2 × 1,000 g) + 500 g + 250 g<br>
                        = 2,000 g + 750 g = 2,750 g (Exact Match!)
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Two 1 kg weights, one 500 g weight, and one 250 g weight</p>
                </div>
                """
            },
            {
                "id": "q9",
                "question": "How many 50-gram packets of black pepper can be prepared from a 1 kg container of pepper?",
                "options": [
                    "10 packets",
                    "20 packets",
                    "25 packets",
                    "50 packets"
                ],
                "answer": 1,
                "hint": "Convert 1 kg to grams: 1,000 g. Divide by 50 g.",
                "explanation": "1 kg = 1,000 g. Number of packets = 1,000 ÷ 50 = 20 packets.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Mass = 1 kg = 1,000 g<br>
                        Packet Mass = 50 g<br>
                        Number of Packets = 1,000 ÷ 50 = 20 packets
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 20 packets</p>
                </div>
                """
            },
            {
                "id": "q10",
                "question": "If 1/4 kg of green chillies costs ₹15, what is the cost of 2 kg of green chillies?",
                "options": [
                    "₹60",
                    "₹90",
                    "₹120",
                    "₹150"
                ],
                "answer": 2,
                "hint": "There are four 1/4 kg units in 1 kg. So 2 kg contains eight 1/4 kg units.",
                "explanation": "1 kg = 4 × (1/4 kg) = 4 × ₹15 = ₹60 per kg. For 2 kg, the cost is 2 × ₹60 = ₹120.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Rate for 1/4 kg = ₹15<br>
                        Rate for 1 kg = 4 × ₹15 = ₹60<br>
                        Cost of 2 kg = 2 × ₹60 = ₹120
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: ₹120</p>
                </div>
                """
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Milligrams, Quintals, Tonnes & Weight Arithmetic",
        "lecture": "Welcome to Mastery Challenge 2. This session focuses on tiny milligram measurements, heavy commercial units like quintals and metric tonnes, and vertical column addition and subtraction of weights with regrouping.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Test your mastery of micro-units, heavy metric units, and multi-column arithmetic. Answer all 10 questions to unlock the detailed solutions!</p>",
        "questions": [
            {
                "id": "q11",
                "question": "Which of the following objects is most appropriately weighed in milligrams (mg)?",
                "options": [
                    "A baby elephant",
                    "A grain of fine table salt",
                    "A bag of basmati rice",
                    "A cricket bat"
                ],
                "answer": 1,
                "hint": "Milligrams are used for extremely tiny and feather-light objects.",
                "explanation": "A single grain of salt weighs approximately 1 mg. An elephant is weighed in tonnes, rice in kg, and a cricket bat in kg and grams (~1.2 kg).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <p><strong>Appropriate Units Analysis:</strong></p>
                    <ul class='list-disc list-inside text-slate-300 space-y-1'>
                        <li>Baby elephant: ~100 kg (or tonnes)</li>
                        <li>Cricket bat: ~1 kg 200 g (kg/g)</li>
                        <li>Rice bag: 25 kg (kg)</li>
                        <li>Grain of salt: <strong>~1 mg (milligram)</strong></li>
                    </ul>
                    <p class='text-emerald-400 font-bold'>Correct Option: A grain of fine table salt</p>
                </div>
                """
            },
            {
                "id": "q12",
                "question": "A goldsmith crafts a necklace using 12 g 450 mg of 22-carat gold. What is the total mass of the necklace in milligrams?",
                "options": [
                    "1,245 mg",
                    "12,450 mg",
                    "124,500 mg",
                    "12.45 mg"
                ],
                "answer": 1,
                "hint": "1 g = 1,000 mg. Multiply 12 by 1,000 and add 450.",
                "explanation": "12 g = 12 × 1,000 mg = 12,000 mg. Adding 450 mg gives 12,000 + 450 = 12,450 mg.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1 g = 1,000 mg<br>
                        12 g = 12,000 mg<br>
                        Total = 12,000 mg + 450 mg = 12,450 mg
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 12,450 mg</p>
                </div>
                """
            },
            {
                "id": "q13",
                "question": "How many quintals of grain are equivalent to exactly 6 metric tonnes?",
                "options": [
                    "6 quintals",
                    "60 quintals",
                    "600 quintals",
                    "0.6 quintals"
                ],
                "answer": 1,
                "hint": "1 metric tonne = 10 quintals.",
                "explanation": "Since 1 metric tonne = 10 quintals, 6 metric tonnes = 6 × 10 = 60 quintals (which also equals 6,000 kg).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1 Metric Tonne = 10 Quintals = 1,000 kg<br>
                        6 Metric Tonnes = 6 × 10 = 60 Quintals<br>
                        (Check in kg: 60 × 100 kg = 6,000 kg = 6 tonnes)
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 60 quintals</p>
                </div>
                """
            },
            {
                "id": "q14",
                "question": "A cargo ship transports 45 metric tonnes of steel. How many kilograms of steel does this represent?",
                "options": [
                    "4,500 kg",
                    "45,000 kg",
                    "450,000 kg",
                    "450 kg"
                ],
                "answer": 1,
                "hint": "1 metric tonne = 1,000 kg. Multiply 45 by 1,000.",
                "explanation": "45 tonnes × 1,000 kg/tonne = 45,000 kg.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1 Metric Tonne = 1,000 kg<br>
                        45 Metric Tonnes = 45 × 1,000 kg = 45,000 kg
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 45,000 kg</p>
                </div>
                """
            },
            {
                "id": "q15",
                "question": "Add the following compound masses: 28 kg 650 g + 19 kg 780 g. What is the sum?",
                "options": [
                    "47 kg 430 g",
                    "48 kg 430 g",
                    "48 kg 1,430 g",
                    "47 kg 1,430 g"
                ],
                "answer": 1,
                "hint": "Add grams: 650 + 780 = 1,430 g. Carry 1 kg (1,000 g) to kilograms.",
                "explanation": "Grams: 650 + 780 = 1,430 g = 1 kg 430 g. Kilograms: 28 + 19 + 1 (carry) = 48 kg. Total = 48 kg 430 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Grams Column: 650 g + 780 g = 1,430 g<br>
                        Regroup: 1,430 g = 1 kg 430 g (Carry 1 kg)<br>
                        Kilograms Column: 28 kg + 19 kg + 1 kg = 48 kg<br>
                        Sum = 48 kg 430 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 48 kg 430 g</p>
                </div>
                """
            },
            {
                "id": "q16",
                "question": "A vegetable van carries 12 kg 300 g of cauliflower, 8 kg 750 g of carrots, and 15 kg 450 g of cabbage. What is the total mass of the vegetables?",
                "options": [
                    "35 kg 500 g",
                    "36 kg 500 g",
                    "36 kg 1,500 g",
                    "35 kg 1,500 g"
                ],
                "answer": 1,
                "hint": "Sum all grams: 300 + 750 + 450 = 1,500 g. Regroup 1,000 g as 1 kg.",
                "explanation": "Grams: 300 + 750 + 450 = 1,500 g = 1 kg 500 g. Kilograms: 12 + 8 + 15 + 1 (carry) = 36 kg. Total = 36 kg 500 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Grams: 300 + 750 + 450 = 1,500 g = 1 kg 500 g<br>
                        Kilograms: 12 + 8 + 15 + 1 (carry) = 36 kg<br>
                        Total = 36 kg 500 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 36 kg 500 g</p>
                </div>
                """
            },
            {
                "id": "q17",
                "question": "Subtract: 34 kg 250 g - 18 kg 680 g. What is the result?",
                "options": [
                    "16 kg 570 g",
                    "15 kg 570 g",
                    "15 kg 430 g",
                    "16 kg 430 g"
                ],
                "answer": 1,
                "hint": "Borrow 1 kg (1,000 g) from 34 kg to make 1,250 g. Subtract 680 g.",
                "explanation": "Borrow 1 kg from 34 kg, leaving 33 kg. Top grams become 250 + 1,000 = 1,250 g. Grams: 1,250 - 680 = 570 g. Kilograms: 33 - 18 = 15 kg. Result = 15 kg 570 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Borrow 1 kg from 34 kg ➔ 33 kg and (250 + 1,000) = 1,250 g<br>
                        Grams: 1,250 g - 680 g = 570 g<br>
                        Kilograms: 33 kg - 18 kg = 15 kg<br>
                        Difference = 15 kg 570 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 15 kg 570 g</p>
                </div>
                """
            },
            {
                "id": "q18",
                "question": "A 50 kg sack of wheat flour has a small leak. When inspected at the store, it weighs 46 kg 125 g. How much flour leaked out?",
                "options": [
                    "4 kg 875 g",
                    "3 kg 875 g",
                    "3 kg 125 g",
                    "4 kg 125 g"
                ],
                "answer": 1,
                "hint": "50 kg 000 g - 46 kg 125 g. Borrow 1 kg from 50 kg to get 49 kg 1,000 g.",
                "explanation": "50 kg 000 g - 46 kg 125 g: Borrow 1 kg ➔ 49 kg 1,000 g. Grams: 1,000 - 125 = 875 g. Kilograms: 49 - 46 = 3 kg. Leaked flour = 3 kg 875 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        50 kg 000 g ➔ 49 kg 1,000 g<br>
                        Grams: 1,000 g - 125 g = 875 g<br>
                        Kilograms: 49 kg - 46 kg = 3 kg<br>
                        Leaked mass = 3 kg 875 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 3 kg 875 g</p>
                </div>
                """
            },
            {
                "id": "q19",
                "question": "An elephant displaced an amount of river water equal to the weight of 80 bags of stones. If each bag of stones weighs 50 kg, what is the weight of the elephant in metric tonnes?",
                "options": [
                    "2 tonnes",
                    "4 tonnes",
                    "8 tonnes",
                    "40 tonnes"
                ],
                "answer": 1,
                "hint": "Total mass = 80 × 50 kg = 4,000 kg. 1 tonne = 1,000 kg.",
                "explanation": "Total weight of stones = 80 × 50 kg = 4,000 kg. Since 1 metric tonne = 1,000 kg, 4,000 kg = 4 metric tonnes.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Stones = 80 bags × 50 kg/bag = 4,000 kg<br>
                        Conversion to Tonnes: 4,000 kg ÷ 1,000 = 4 Metric Tonnes
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 4 tonnes</p>
                </div>
                """
            },
            {
                "id": "q20",
                "question": "A truck has a tare weight (empty weight) of 3 tonnes 500 kg. When fully loaded with bricks, it weighs 8 tonnes 200 kg. What is the weight of the bricks loaded on the truck?",
                "options": [
                    "4 tonnes 700 kg",
                    "5 tonnes 300 kg",
                    "4 tonnes 300 kg",
                    "5 tonnes 700 kg"
                ],
                "answer": 0,
                "hint": "8 tonnes 200 kg - 3 tonnes 500 kg. Borrow 1 tonne = 1,000 kg.",
                "explanation": "Borrow 1 tonne from 8 tonnes ➔ 7 tonnes 1,200 kg. Kilograms: 1,200 - 500 = 700 kg. Tonnes: 7 - 3 = 4 tonnes. Bricks weight = 4 tonnes 700 kg.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Loaded: 8 t 200 kg ➔ 7 t 1,200 kg<br>
                        Empty: - 3 t 500 kg<br>
                        Bricks = 4 t 700 kg (4,700 kg)
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 4 tonnes 700 kg</p>
                </div>
                """
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • Proportional Scaling, Capacity Basics & Equivalences",
        "lecture": "Welcome to Mastery Challenge 3. In this module, you will practice proportional multiplication and division of weights, understand liquid volume benchmarks, and master litre to millilitre conversions.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Test your mastery of proportional scaling, scrap pricing, liquid capacity benchmarks, and unit conversions. Answer all 10 questions to unlock the detailed solutions!</p>",
        "questions": [
            {
                "id": "q21",
                "question": "A caterer packs 5 hampers. Each hamper contains 2 kg 450 g of festive sweets. What is the total mass of sweets in all 5 hampers?",
                "options": [
                    "10 kg 250 g",
                    "12 kg 250 g",
                    "12 kg 450 g",
                    "11 kg 250 g"
                ],
                "answer": 1,
                "hint": "Multiply 2,450 g by 5, or multiply 2 kg × 5 and 450 g × 5.",
                "explanation": "5 × 2 kg = 10 kg. 5 × 450 g = 2,250 g = 2 kg 250 g. Total = 10 kg + 2 kg 250 g = 12 kg 250 g.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Method 1: 2,450 g × 5 = 12,250 g = 12 kg 250 g<br>
                        Method 2: (5 × 2 kg) + (5 × 450 g)<br>
                        = 10 kg + 2,250 g = 10 kg + 2 kg 250 g = 12 kg 250 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 12 kg 250 g</p>
                </div>
                """
            },
            {
                "id": "q22",
                "question": "A box containing 6 kg 300 g of mixed dry fruits is distributed equally among 7 children. How much dry fruit does each child receive?",
                "options": [
                    "850 g",
                    "900 g",
                    "950 g",
                    "1 kg"
                ],
                "answer": 1,
                "hint": "Convert 6 kg 300 g to 6,300 g. Divide 6,300 by 7.",
                "explanation": "6 kg 300 g = 6,300 g. 6,300 ÷ 7 = 900 g per child.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Dry Fruits = 6 kg 300 g = 6,300 g<br>
                        Per Child = 6,300 g ÷ 7 = 900 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 900 g</p>
                </div>
                """
            },
            {
                "id": "q23",
                "question": "A kabadiwala buys 16 kg of old iron pipes for ₹448. At this same rate per kg, how much will he pay for 25 kg of iron pipes?",
                "options": [
                    "₹650",
                    "₹700",
                    "₹725",
                    "₹750"
                ],
                "answer": 1,
                "hint": "Find the rate per kg first: ₹448 ÷ 16 kg. Then multiply by 25 kg.",
                "explanation": "Rate per kg = ₹448 ÷ 16 = ₹28 per kg. For 25 kg = 25 × ₹28 = ₹700.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Rate per kg = ₹448 ÷ 16 = ₹28 / kg<br>
                        Cost of 25 kg = 25 × ₹28 = ₹700
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: ₹700</p>
                </div>
                """
            },
            {
                "id": "q24",
                "question": "Which of the following capacities is equivalent to exactly 3/4 of a litre?",
                "options": [
                    "250 mL",
                    "500 mL",
                    "750 mL",
                    "1,750 mL"
                ],
                "answer": 2,
                "hint": "1 litre = 1,000 mL. Multiply 1,000 by 3/4.",
                "explanation": "3/4 of 1,000 mL = (1,000 ÷ 4) × 3 = 250 × 3 = 750 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1 Litre = 1,000 mL<br>
                        3/4 L = (3/4) × 1,000 mL = 3 × 250 mL = 750 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 750 mL</p>
                </div>
                """
            },
            {
                "id": "q25",
                "question": "How many 200 mL cups of tea can be served from a 3-litre tea kettle?",
                "options": [
                    "12 cups",
                    "15 cups",
                    "18 cups",
                    "20 cups"
                ],
                "answer": 1,
                "hint": "Convert 3 L to 3,000 mL. Divide by 200 mL.",
                "explanation": "3 L = 3,000 mL. Number of cups = 3,000 ÷ 200 = 15 cups.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Kettle Capacity = 3 L = 3,000 mL<br>
                        Cup Capacity = 200 mL<br>
                        Number of Cups = 3,000 ÷ 200 = 15 cups
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 15 cups</p>
                </div>
                """
            },
            {
                "id": "q26",
                "question": "When reading the water level in a laboratory graduated glass cylinder, at which position should your eye be aligned?",
                "options": [
                    "Looking down from above at the upper rim of the curved water surface",
                    "Horizontally level with the lowest bottom point of the concave meniscus",
                    "Looking up from below the cylinder bottom",
                    "At any angle because parallax does not affect graduated cylinders"
                ],
                "answer": 1,
                "hint": "Always align your eye horizontally with the lowest dip of the curved meniscus.",
                "explanation": "Scientific protocol requires aligning the eye horizontally with the bottom of the curved meniscus to eliminate optical parallax errors.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <p><strong>Scientific Meniscus Reading Convention:</strong></p>
                    <div class='p-2 rounded bg-slate-800 text-slate-200'>
                        Water adheres to glass walls, creating a curved concave surface. To prevent parallax distortion, your line of sight must be exactly horizontal with the <strong>lowest central point of the meniscus</strong>.
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: Horizontally level with the lowest bottom point of the concave meniscus</p>
                </div>
                """
            },
            {
                "id": "q27",
                "question": "A milk delivery can contains 5,025 mL of milk. Express this volume in litres and millilitres:",
                "options": [
                    "50 L 25 mL",
                    "5 L 250 mL",
                    "5 L 25 mL",
                    "5 L 2.5 mL"
                ],
                "answer": 2,
                "hint": "5,025 = 5,000 mL + 25 mL.",
                "explanation": "5,025 mL = 5,000 mL + 25 mL = 5 L 25 mL (with a leading zero in the hundreds place: 025).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        5,025 mL = 5,000 mL + 25 mL<br>
                        5,000 mL = 5 L<br>
                        25 mL = 25 mL<br>
                        Result = 5 L 25 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 5 L 25 mL</p>
                </div>
                """
            },
            {
                "id": "q28",
                "question": "A recipe for biryani calls for 2 L 60 mL of vegetable broth. Which numerical value in millilitres represents this exact quantity?",
                "options": [
                    "2,600 mL",
                    "2,060 mL",
                    "260 mL",
                    "20,060 mL"
                ],
                "answer": 1,
                "hint": "2 L = 2,000 mL. 60 mL is written as 060 in the 3-digit placeholder.",
                "explanation": "2 L = 2,000 mL. Adding 60 mL gives 2,000 + 60 = 2,060 mL. 2,600 mL would be 2 L 600 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        2 L = 2,000 mL<br>
                        60 mL = 060 mL<br>
                        2,000 mL + 060 mL = 2,060 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 2,060 mL</p>
                </div>
                """
            },
            {
                "id": "q29",
                "question": "An athlete tracks daily water intake. She drinks 400 mL at breakfast, 650 mL during morning training, 500 mL at lunch, and 750 mL after evening running. What is her total water intake in litres and millilitres?",
                "options": [
                    "2 L 100 mL",
                    "2 L 300 mL",
                    "2 L 200 mL",
                    "1 L 900 mL"
                ],
                "answer": 1,
                "hint": "Add all millilitres: 400 + 650 + 500 + 750.",
                "explanation": "Total = 400 + 650 + 500 + 750 = 2,300 mL = 2,000 mL + 300 mL = 2 L 300 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        400 + 650 = 1,050 mL<br>
                        1,050 + 500 = 1,550 mL<br>
                        1,550 + 750 = 2,300 mL<br>
                        2,300 mL = 2 L 300 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 2 L 300 mL</p>
                </div>
                """
            },
            {
                "id": "q30",
                "question": "Which volume is strictly GREATER than 1 litre 80 millilitres?",
                "options": [
                    "1,080 mL",
                    "1,008 mL",
                    "1,800 mL",
                    "1,079 mL"
                ],
                "answer": 2,
                "hint": "1 L 80 mL = 1,080 mL. Find which option exceeds 1,080 mL.",
                "explanation": "1 L 80 mL = 1,080 mL. 1,800 mL (which equals 1 L 800 mL) is much greater than 1,080 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1 L 80 mL = 1,080 mL<br>
                        • 1,080 mL = 1,080 mL (Equal)<br>
                        • 1,008 mL < 1,080 mL (Smaller)<br>
                        • 1,800 mL > 1,080 mL (GREATER by 720 mL!)<br>
                        • 1,079 mL < 1,080 mL (Smaller)
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 1,800 mL</p>
                </div>
                """
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Fuel Logistics, Oil Partitioning & Multi-Step Story Problems",
        "lecture": "Welcome to the final Mastery Challenge of Chapter 8. This concluding assessment challenges you with real-world fuel logistics, multi-stage commercial packaging, and multi-step reasoning problems.",
        "content_html": "<p class='text-xs text-slate-300 mb-4'>Congratulations on reaching the final mastery challenge! Solve these 10 multi-step problems to complete the Weight and Capacity chapter.</p>",
        "questions": [
            {
                "id": "q31",
                "question": "A family car has a fuel tank capacity of 48 litres. When arriving at a petrol pump, the fuel gauge shows 14 litres 350 millilitres remaining. How much fuel is needed to fill the tank completely?",
                "options": [
                    "34 L 650 mL",
                    "33 L 650 mL",
                    "33 L 350 mL",
                    "34 L 350 mL"
                ],
                "answer": 1,
                "hint": "Borrow 1 L (1,000 mL) from 48 L to make 47 L 1,000 mL. Subtract 14 L 350 mL.",
                "explanation": "48 L 000 mL - 14 L 350 mL: Borrow 1 L ➔ 47 L 1,000 mL. Millilitres: 1,000 - 350 = 650 mL. Litres: 47 - 14 = 33 L. Needed = 33 L 650 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Full Capacity: 48 L 000 mL ➔ 47 L 1,000 mL<br>
                        Current Fuel: - 14 L 350 mL<br>
                        Required = 33 L 650 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 33 L 650 mL</p>
                </div>
                """
            },
            {
                "id": "q32",
                "question": "An auto-rickshaw driver buys petrol three times in a week: 8 L 500 mL on Monday, 6 L 750 mL on Wednesday, and 9 L 250 mL on Friday. What is the total volume of petrol purchased?",
                "options": [
                    "23 L 500 mL",
                    "24 L 500 mL",
                    "24 L 250 mL",
                    "23 L 750 mL"
                ],
                "answer": 1,
                "hint": "Add millilitres: 500 + 750 + 250 = 1,500 mL = 1 L 500 mL. Add litres: 8 + 6 + 9 + 1.",
                "explanation": "Millilitres: 500 + 750 + 250 = 1,500 mL = 1 L 500 mL. Litres: 8 + 6 + 9 + 1 (carry) = 24 L. Total = 24 L 500 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Millilitres: 500 + 750 + 250 = 1,500 mL = 1 L 500 mL<br>
                        Litres: 8 + 6 + 9 + 1 (carry) = 24 L<br>
                        Total = 24 L 500 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 24 L 500 mL</p>
                </div>
                """
            },
            {
                "id": "q33",
                "question": "A juice stall owner prepares 16 litres of fresh orange juice. He fills 50 glasses holding 250 mL each. How much juice remains in his dispenser?",
                "options": [
                    "2 L 500 mL",
                    "3 L 500 mL",
                    "4 L 500 mL",
                    "1 L 500 mL"
                ],
                "answer": 1,
                "hint": "50 × 250 mL = 12,500 mL = 12 L 500 mL. Subtract from 16 L.",
                "explanation": "Poured juice = 50 × 250 mL = 12,500 mL = 12 L 500 mL. Remaining juice = 16 L 000 mL - 12 L 500 mL = 3 L 500 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Juice = 16 L = 16,000 mL<br>
                        Juice Served = 50 × 250 mL = 12,500 mL (12 L 500 mL)<br>
                        Remaining = 16,000 mL - 12,500 mL = 3,500 mL = 3 L 500 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 3 L 500 mL</p>
                </div>
                """
            },
            {
                "id": "q34",
                "question": "A wholesale oil dealer has an 18-litre drum of groundnut oil. He pours it entirely into bottles holding 600 mL each. How many bottles can he fill?",
                "options": [
                    "25 bottles",
                    "30 bottles",
                    "35 bottles",
                    "36 bottles"
                ],
                "answer": 1,
                "hint": "Convert 18 L to 18,000 mL. Divide 18,000 by 600.",
                "explanation": "18 L = 18,000 mL. Number of bottles = 18,000 ÷ 600 = 30 bottles.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Oil = 18 L = 18,000 mL<br>
                        Bottle Size = 600 mL<br>
                        Bottles Filled = 18,000 ÷ 600 = 30 bottles
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 30 bottles</p>
                </div>
                """
            },
            {
                "id": "q35",
                "question": "A vendor buys a 20-litre container of mango juice for ₹400. He serves the juice in 200 mL cups and sells each cup for ₹8. What is his total profit?",
                "options": [
                    "₹300",
                    "₹400",
                    "₹500",
                    "₹800"
                ],
                "answer": 1,
                "hint": "Find total cups: 20,000 mL ÷ 200 mL = 100 cups. Revenue = 100 × ₹8 = ₹800. Profit = Revenue - Cost.",
                "explanation": "Total cups = 20,000 ÷ 200 = 100 cups. Total revenue = 100 × ₹8 = ₹800. Profit = ₹800 - ₹400 = ₹400.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Volume = 20 L = 20,000 mL<br>
                        Cups Served = 20,000 ÷ 200 = 100 cups<br>
                        Total Revenue = 100 × ₹8 = ₹800<br>
                        Total Cost = ₹400<br>
                        Profit = ₹800 - ₹400 = ₹400
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: ₹400</p>
                </div>
                """
            },
            {
                "id": "q36",
                "question": "A dairy farmer has 45 L of milk. He sells 18 L 400 mL to a hotel and 14 L 850 mL to a restaurant. How much milk is left with the farmer?",
                "options": [
                    "11 L 750 mL",
                    "12 L 250 mL",
                    "11 L 250 mL",
                    "12 L 750 mL"
                ],
                "answer": 0,
                "hint": "Add milk sold: 18 L 400 mL + 14 L 850 mL = 33 L 250 mL. Subtract from 45 L.",
                "explanation": "Milk sold = 18 L 400 mL + 14 L 850 mL = 33 L 250 mL. Leftover = 45 L 000 mL - 33 L 250 mL = 11 L 750 mL.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Total Sold = 18 L 400 mL + 14 L 850 mL = 33 L 250 mL<br>
                        Remaining = 45 L 000 mL - 33 L 250 mL<br>
                        44 L 1,000 mL - 33 L 250 mL = 11 L 750 mL
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 11 L 750 mL</p>
                </div>
                """
            },
            {
                "id": "q37",
                "question": "A recipe for lemonade calls for 150 mL of lemon juice, 200 mL of sugar syrup, and 1 L 650 mL of chilled water. What is the total volume of lemonade prepared?",
                "options": [
                    "1 L 900 mL",
                    "2 L (2,000 mL)",
                    "2 L 100 mL",
                    "2 L 500 mL"
                ],
                "answer": 1,
                "hint": "Sum all components: 150 mL + 200 mL + 1,650 mL.",
                "explanation": "150 + 200 + 1,650 = 2,000 mL. Since 2,000 mL = 2 L, exactly 2 litres of lemonade is prepared.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Lemon Juice: 150 mL<br>
                        Sugar Syrup: 200 mL<br>
                        Water: 1 L 650 mL = 1,650 mL<br>
                        Total = 150 + 200 + 1,650 = 2,000 mL = 2 L
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 2 L (2,000 mL)</p>
                </div>
                """
            },
            {
                "id": "q38",
                "question": "A village water tanker carries 1,200 litres of water. It fills 4 community storage tanks, each having a capacity of 240 litres. How much water remains in the tanker?",
                "options": [
                    "240 L",
                    "260 L",
                    "300 L",
                    "960 L"
                ],
                "answer": 0,
                "hint": "Water dispensed = 4 × 240 L = 960 L. Subtract 960 L from 1,200 L.",
                "explanation": "Water filled = 4 × 240 = 960 L. Remaining water = 1,200 - 960 = 240 L.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Water Distributed = 4 × 240 L = 960 L<br>
                        Remaining in Tanker = 1,200 L - 960 L = 240 L
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 240 L</p>
                </div>
                """
            },
            {
                "id": "q39",
                "question": "A chemist dissolves 750 mg of salt in 250 mL of water. If she wants to make 1 litre of solution with the exact same concentration, how many milligrams of salt must she dissolve?",
                "options": [
                    "1,500 mg",
                    "2,250 mg",
                    "3,000 mg (3 g)",
                    "3,750 mg"
                ],
                "answer": 2,
                "hint": "1 litre is 4 times 250 mL. Multiply 750 mg by 4.",
                "explanation": "1 L = 1,000 mL = 4 × 250 mL. Salt required = 4 × 750 mg = 3,000 mg (or 3 g).",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        Volume Scaling Factor = 1,000 mL ÷ 250 mL = 4<br>
                        Salt Required = 4 × 750 mg = 3,000 mg = 3 g
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 3,000 mg (3 g)</p>
                </div>
                """
            },
            {
                "id": "q40",
                "question": "A school kitchen uses 35 kg of wheat flour each week. If they purchase a 1-quintal sack of flour, for how many full weeks will this single sack last, and how many kilograms will remain?",
                "options": [
                    "2 full weeks with 30 kg remaining",
                    "3 full weeks with 5 kg remaining",
                    "2 full weeks with 20 kg remaining",
                    "3 full weeks with 10 kg remaining"
                ],
                "answer": 0,
                "hint": "1 quintal = 100 kg. Divide 100 by 35.",
                "explanation": "1 quintal = 100 kg. 100 ÷ 35 = 2 with a remainder of 30 (since 2 × 35 = 70 kg, and 100 - 70 = 30 kg). It lasts 2 full weeks with 30 kg left.",
                "solution_html": """
                <div class='space-y-2 text-xs'>
                    <div class='p-2 rounded bg-slate-800 font-mono text-cyan-300'>
                        1 Quintal = 100 kg<br>
                        Weekly Usage = 35 kg<br>
                        Division: 100 ÷ 35 = 2 quotient with 30 remainder<br>
                        (2 weeks × 35 kg = 70 kg; 100 kg - 70 kg = 30 kg remaining)
                    </div>
                    <p class='text-emerald-400 font-bold'>Correct Option: 2 full weeks with 30 kg remaining</p>
                </div>
                """
            }
        ]
    }
]


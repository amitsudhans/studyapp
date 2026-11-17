#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 10: How Quantities Combine: Understanding Data
Part 3: Slides 17 to 20 (Silent Mastery Quiz Slides - 40 Questions with 3-Step Solutions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Combined Averages Challenge",
        "subtitle": "Mastery Quiz 1 (Silent Exercise): Average of Averages, (an+bm)/(n+m) & Weighted Mean Properties",
        "is_quiz": True,
        "questions": [
            {
                "question": "Class A (12 students) has an average height of 150 cm, and Class B (36 students) has an average height of 162 cm. What is the combined average height?",
                "options": ["159 cm", "156 cm", "158 cm", "160 cm"],
                "answer": 0,
                "solution_steps": [
                    "Use the combined average formula: (a·n + b·m) / (n + m).",
                    "Numerator = 150×12 + 162×36 = 1800 + 5832 = 7632 cm; Denominator = 12 + 36 = 48.",
                    "Combined average = 7632 / 48 = 159 cm."
                ]
            },
            {
                "question": "When is the simple average (a + b)/2 equal to the true combined average (an + bm)/(n + m)?",
                "options": [
                    "Only when n = m (equal group sizes) OR a = b (equal group averages)",
                    "Whenever n + m is even",
                    "Whenever a > b",
                    "Always for positive numbers"
                ],
                "answer": 0,
                "solution_steps": [
                    "Set (an + bm)/(n + m) = (a + b)/2 and cross-multiply.",
                    "2an + 2bm = an + am + bn + bm simplifies to (a − b)(n − m) = 0.",
                    "Hence either a = b or n = m."
                ]
            },
            {
                "question": "A cyclist rides at 18 km/h for 2 hours and 12 km/h for 4 hours. What is the average speed over the 6-hour trip?",
                "options": ["14 km/h", "15 km/h", "16 km/h", "13.5 km/h"],
                "answer": 0,
                "solution_steps": [
                    "Weight each speed by its duration in hours: Total distance = 18×2 + 12×4 = 36 + 48 = 84 km.",
                    "Total time = 2 + 4 = 6 hours.",
                    "Average speed = 84 / 6 = 14 km/h."
                ]
            },
            {
                "question": "Find the weighted mean of values (20, 40, 50) with weights (1, 2, 2).",
                "options": ["40", "36.7", "38", "42"],
                "answer": 0,
                "solution_steps": [
                    "Compute weighted sum: 1(20) + 2(40) + 2(50) = 20 + 80 + 100 = 200.",
                    "Sum of weights = 1 + 2 + 2 = 5.",
                    "Weighted mean = 200 / 5 = 40."
                ]
            },
            {
                "question": "If every weight in a weighted mean is multiplied by 5 while data values stay fixed, what happens to the weighted mean?",
                "options": [
                    "It stays completely unchanged",
                    "It becomes 5 times larger",
                    "It becomes 1/5 as large",
                    "It increases by 5"
                ],
                "answer": 0,
                "solution_steps": [
                    "Numerator becomes Σ(5Wᵢxᵢ) = 5·Σ(Wᵢxᵢ) and denominator becomes Σ(5Wᵢ) = 5·ΣWᵢ.",
                    "The factor 5 cancels cleanly from numerator and denominator.",
                    "Therefore the weighted mean is unchanged."
                ]
            },
            {
                "question": "Group 1 (n = 10) has mean 60 and Group 2 (m = 40) has mean 80. Which value is the combined mean closest to?",
                "options": [
                    "80 (specifically 76, since Group 2 has 4× the weight of Group 1)",
                    "60",
                    "70 (midpoint)",
                    "90"
                ],
                "answer": 0,
                "solution_steps": [
                    "Combined mean = (10×60 + 40×80) / 50 = (600 + 3200) / 50 = 3800 / 50 = 76.",
                    "76 is only 4 units from 80, versus 16 units from 60.",
                    "The larger group always pulls the combined mean toward itself."
                ]
            },
            {
                "question": "Can the weighted mean of {12, 18, 25} with positive weights ever equal 27?",
                "options": [
                    "No — a weighted mean always lies between the minimum (12) and maximum (25) values",
                    "Yes — if the weight on 25 is huge",
                    "Yes — if all weights exceed 100",
                    "Yes — if weights sum to 27"
                ],
                "answer": 0,
                "solution_steps": [
                    "Since 12 ≤ xᵢ ≤ 25 and Wᵢ > 0, multiplying gives 12Wᵢ ≤ Wᵢxᵢ ≤ 25Wᵢ.",
                    "Summing and dividing by ΣWᵢ gives 12 ≤ x̄_w ≤ 25.",
                    "Hence 27 is impossible."
                ]
            },
            {
                "question": "Three batches of 10, 20, and 30 boxes weigh an average of 4 kg, 6 kg, and 5 kg per box respectively. Find the overall average weight per box.",
                "options": ["5.17 kg (310 / 60)", "5.00 kg", "5.50 kg", "4.83 kg"],
                "answer": 0,
                "solution_steps": [
                    "Total weight = 10×4 + 20×6 + 30×5 = 40 + 120 + 150 = 310 kg.",
                    "Total boxes = 10 + 20 + 30 = 60.",
                    "Overall mean = 310 / 60 ≈ 5.17 kg."
                ]
            },
            {
                "question": "A combined group of 25 boys and 15 girls has a mean score of 74. If the boys' mean is 71, what is the girls' mean score?",
                "options": ["79", "77", "76", "80"],
                "answer": 0,
                "solution_steps": [
                    "Total score of all 40 students = 40 × 74 = 2960.",
                    "Boys' total score = 25 × 71 = 1775, leaving girls' total = 2960 − 1775 = 1185.",
                    "Girls' mean = 1185 / 15 = 79."
                ]
            },
            {
                "question": "In the combined average formula (an + bm)/(n + m), if n = m = 25, what does the formula simplify to?",
                "options": ["(a + b) / 2", "(a − b) / 2", "(ab) / 25", "25(a + b)"],
                "answer": 0,
                "solution_steps": [
                    "Substitute n = m = 25: (25a + 25b) / (25 + 25).",
                    "Factor 25: 25(a + b) / 50.",
                    "Simplify: (a + b) / 2."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Mixtures Custom Challenge",
        "subtitle": "Mastery Quiz 2 (Silent Exercise): Mixtures, Gold Karats (Brahmagupta), Academic & Rating Weights",
        "is_quiz": True,
        "questions": [
            {
                "question": "3 L of 12% sugar syrup is mixed with 5 L of 20% sugar syrup. What is the concentration of the 8 L mixture?",
                "options": ["17%", "16%", "18%", "15.5%"],
                "answer": 0,
                "solution_steps": [
                    "Sugar in batch 1 = 3 × 0.12 = 0.36 L; batch 2 = 5 × 0.20 = 1.00 L.",
                    "Total sugar = 1.36 L in 8 L total volume.",
                    "Concentration = (1.36 / 8) × 100% = 17%."
                ]
            },
            {
                "question": "A goldsmith melts 15 g of 20-karat gold with 5 g of 24-karat pure gold. Using Brahmagupta's alloy rule, what is the purity?",
                "options": ["21 karats", "22 karats", "21.5 karats", "20.5 karats"],
                "answer": 0,
                "solution_steps": [
                    "Apply weighted mean by mass: (15×20 + 5×24) / (15 + 5).",
                    "Numerator = 300 + 120 = 420; Denominator = 20.",
                    "Purity = 420 / 20 = 21 karats."
                ]
            },
            {
                "question": "How many grams of pure 24-karat gold must be melted with 20 g of 18-karat gold to obtain a 20-karat alloy?",
                "options": ["10 g", "15 g", "20 g", "5 g"],
                "answer": 0,
                "solution_steps": [
                    "Let w be grams of 24k gold: (20×18 + w×24) / (20 + w) = 20.",
                    "360 + 24w = 400 + 20w ⇒ 4w = 40.",
                    "Solving gives w = 10 g."
                ]
            },
            {
                "question": "In a fertilizer mix, 8 kg of 10% nitrogen mix is blended with 12 kg of 25% nitrogen mix. Find the resulting nitrogen percentage.",
                "options": ["19%", "17.5%", "20%", "18%"],
                "answer": 0,
                "solution_steps": [
                    "Weighted average: (8×10 + 12×25) / (8 + 12).",
                    "= (80 + 300) / 20 = 380 / 20.",
                    "= 19% nitrogen."
                ]
            },
            {
                "question": "A course assigns weights: Internals 25%, Lab 25%, Final Exam 50%. A student scores 84, 92, and 76 respectively. Find the final grade.",
                "options": ["82%", "84%", "80%", "83%"],
                "answer": 0,
                "solution_steps": [
                    "Compute 0.25(84) + 0.25(92) + 0.50(76).",
                    "= 21 + 23 + 38.",
                    "= 82%."
                ]
            },
            {
                "question": "A restaurant rating weights Food (×5), Service (×3), Ambience (×2). Scores are Food 4.6, Service 4.0, Ambience 3.5. Find the weighted rating.",
                "options": ["4.20", "4.03", "4.30", "4.15"],
                "answer": 0,
                "solution_steps": [
                    "Weighted sum = 5(4.6) + 3(4.0) + 2(3.5) = 23.0 + 12.0 + 7.0 = 42.0.",
                    "Total weight = 5 + 3 + 2 = 10.",
                    "Weighted rating = 42.0 / 10 = 4.20."
                ]
            },
            {
                "question": "Product reviews have 10 recent reviews (weight 3 each) averaging 4.8 stars and 10 old reviews (weight 1 each) averaging 3.2 stars. Find the recency-weighted score.",
                "options": ["4.40 stars", "4.00 stars", "4.20 stars", "4.50 stars"],
                "answer": 0,
                "solution_steps": [
                    "Recent weight = 10×3 = 30; Old weight = 10×1 = 10; Total weight = 40.",
                    "Weighted sum = 30(4.8) + 10(3.2) = 144 + 32 = 176.",
                    "Score = 176 / 40 = 4.40 stars."
                ]
            },
            {
                "question": "4 L of pure water (0% acid) is added to 6 L of 30% acid solution. What is the new acid percentage?",
                "options": ["18%", "15%", "20%", "12%"],
                "answer": 0,
                "solution_steps": [
                    "Pure acid = 6 × 0.30 + 4 × 0 = 1.8 L.",
                    "Total volume = 6 + 4 = 10 L.",
                    "Concentration = (1.8 / 10) × 100% = 18%."
                ]
            },
            {
                "question": "Which ancient Indian work by Śrīdharācārya contains weighted-average rules for gold alloy (varna) purity?",
                "options": ["Pātīganita", "Elements", "Principia", "Arithmetica"],
                "answer": 0,
                "solution_steps": [
                    "Śrīdharācārya authored the Pātīganita (c. 10th century CE).",
                    "Alongside Brahmagupta's Brāhmasphuṭasiddhānta, it gives exact varna/karat alloy rules.",
                    "Hence Pātīganita is correct."
                ]
            },
            {
                "question": "A student has 70% in Internals (weight 40%) and needs an 82% overall grade. What minimum score is needed in the Final Exam (weight 60%)?",
                "options": ["90%", "88%", "94%", "86%"],
                "answer": 0,
                "solution_steps": [
                    "Set 0.40(70) + 0.60(F) = 82.",
                    "28 + 0.60F = 82 ⇒ 0.60F = 54.",
                    "F = 54 / 0.60 = 90%."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Stacked Charts Challenge",
        "subtitle": "Mastery Quiz 3 (Silent Exercise): Cluster vs Stacked Columns, 100% Stacked Bars & Case Studies",
        "is_quiz": True,
        "questions": [
            {
                "question": "In a stacked column chart, Segment 1 runs from 0 to 25, Segment 2 from 25 to 68, and Segment 3 from 68 to 105. What is Segment 2's value?",
                "options": ["43 (68 − 25)", "68", "25", "37"],
                "answer": 0,
                "solution_steps": [
                    "Upper segments in stacked charts sit on top of lower segments.",
                    "Bottom boundary of Segment 2 = 25; Top boundary = 68.",
                    "Value = 68 − 25 = 43."
                ]
            },
            {
                "question": "Using the same stacked column (0–25, 25–68, 68–105), what is the overall total height and Segment 3's value?",
                "options": [
                    "Total = 105; Segment 3 = 37 (105 − 68)",
                    "Total = 105; Segment 3 = 105",
                    "Total = 198; Segment 3 = 68",
                    "Total = 68; Segment 3 = 37"
                ],
                "answer": 0,
                "solution_steps": [
                    "The top edge of the entire column is 105 (overall total).",
                    "Segment 3 spans from 68 to 105.",
                    "Segment 3 value = 105 − 68 = 37 (check: 25 + 43 + 37 = 105)."
                ]
            },
            {
                "question": "Why is a 100% stacked bar chart often better than 5 side-by-side pie charts?",
                "options": [
                    "Parallel aligned straight bars make comparing proportional segment lengths far easier and more accurate than judging circular angles",
                    "Pie charts cannot show 5 categories",
                    "100% stacked bars show raw totals without percentages",
                    "Pie charts always sum to 360%"
                ],
                "answer": 0,
                "solution_steps": [
                    "Comparing angles across multiple separate circles is visually error-prone.",
                    "Aligning bars on a common 0%–100% scale lets eyes compare lengths directly.",
                    "Thus 100% stacked bars excel at multi-group proportional comparisons."
                ]
            },
            {
                "question": "Which piece of information CANNOT be read from a 100% stacked bar chart alone?",
                "options": [
                    "Which group has the larger absolute total count or quantity",
                    "Which category has the largest percentage share within a group",
                    "How a category's percentage share changes across groups",
                    "Whether all components in a group sum to 100%"
                ],
                "answer": 0,
                "solution_steps": [
                    "Every bar in a 100% stacked chart is scaled to the exact same 100% length.",
                    "Therefore raw totals (e.g., 500 vs 50,000) are normalized away.",
                    "To compare absolute totals, pair it with a regular stacked chart."
                ]
            },
            {
                "question": "In a 100% stacked energy chart, Country X's solar share doubles from 10% to 20%, while total energy usage also doubles. How did absolute solar energy change?",
                "options": [
                    "It quadrupled (4×)! (10% of 100 = 10 units → 20% of 200 = 40 units)",
                    "It stayed the same",
                    "It only doubled (2×)",
                    "It halved"
                ],
                "answer": 0,
                "solution_steps": [
                    "Initial solar = 10% of T = 0.10T.",
                    "New solar = 20% of (2T) = 0.40T.",
                    "0.40T / 0.10T = 4× (quadrupled)."
                ]
            },
            {
                "question": "In India's National Time Use Survey (2024), why do all demographic bars have the exact same 24-hour (1,440-minute) total length?",
                "options": [
                    "Every person's daily activities across 24 hours form a fixed 100% daily time budget",
                    "Because everyone works 8 hours",
                    "Because sleep is excluded from the chart",
                    "Because time use is measured in kilograms"
                ],
                "answer": 0,
                "solution_steps": [
                    "A single day is strictly 24 hours = 1,440 minutes for every demographic.",
                    "Allocating time across sleep, paid work, unpaid work, learning, and leisure partitions 100% of 24 hours.",
                    "Hence fixed-length stacked bars represent time-use trade-offs cleanly."
                ]
            },
            {
                "question": "When comparing individual sub-category values across years (without needing overall totals), which chart gives every sub-category a zero baseline?",
                "options": [
                    "Cluster-column chart",
                    "Stacked column chart",
                    "100% stacked bar chart",
                    "Pie chart"
                ],
                "answer": 0,
                "solution_steps": [
                    "In a cluster-column chart, every bar rests directly on the y = 0 horizontal axis.",
                    "In a stacked chart, only the bottom segment starts at 0.",
                    "Hence cluster-column charts give all sub-categories a common zero baseline."
                ]
            },
            {
                "question": "In a 100% stacked chart of school playgrounds, State A shows 85% 'Yes' (out of 4,000 schools) and State B shows 70% 'Yes' (out of 60,000 schools). Which state has MORE schools with playgrounds?",
                "options": [
                    "State B (70% of 60,000 = 42,000 schools > 85% of 4,000 = 3,400 schools)",
                    "State A (because 85% > 70%)",
                    "Both have the same number",
                    "Cannot be computed"
                ],
                "answer": 0,
                "solution_steps": [
                    "State A absolute count = 0.85 × 4,000 = 3,400 schools.",
                    "State B absolute count = 0.70 × 60,000 = 42,000 schools.",
                    "A higher percentage of a much smaller base can be smaller in absolute count!"
                ]
            },
            {
                "question": "On a 24-hour body-state stacked bar, Sleep = 7.5 h, Sitting = 11 h, Light Activity = 4 h. How many hours are left for Vigorous Exercise?",
                "options": ["1.5 hours", "2.0 hours", "2.5 hours", "0.5 hours"],
                "answer": 0,
                "solution_steps": [
                    "Sum known states: 7.5 + 11 + 4 = 22.5 hours.",
                    "Subtract from 24-hour day: 24 − 22.5.",
                    "= 1.5 hours."
                ]
            },
            {
                "question": "Which chart type is best when you want BOTH to compare total monthly sales AND see how Electronics, Books, and Clothing contribute to each month's total?",
                "options": [
                    "Regular stacked column chart",
                    "100% stacked bar chart",
                    "Single pie chart",
                    "Scatter plot"
                ],
                "answer": 0,
                "solution_steps": [
                    "Regular stacked columns show the total monthly height at the top edge.",
                    "Each coloured band shows the contribution of Electronics, Books, and Clothing.",
                    "A 100% stacked chart would hide whether total sales grew or shrank."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Applied Data Mastery",
        "subtitle": "Mastery Quiz 4 (Silent Exercise): Cricket Run Rates, Share Pricing, Space Debris & Census Data",
        "is_quiz": True,
        "questions": [
            {
                "question": "A cricket team scores at 6.0 runs/over in overs 1–10, 8.0 runs/over in overs 11–15, and 11.0 runs/over in overs 16–20. What is the overall 20-over run rate?",
                "options": ["7.75 runs/over", "8.33 runs/over", "8.00 runs/over", "7.50 runs/over"],
                "answer": 0,
                "solution_steps": [
                    "Total runs = 10(6.0) + 5(8.0) + 5(11.0) = 60 + 40 + 55 = 155 runs.",
                    "Total overs = 10 + 5 + 5 = 20 overs.",
                    "Overall run rate = 155 / 20 = 7.75 runs/over."
                ]
            },
            {
                "question": "An investor buys 50 shares at ₹120 each and 150 shares at ₹160 each. What is the weighted average purchase price per share?",
                "options": ["₹150", "₹140", "₹145", "₹155"],
                "answer": 0,
                "solution_steps": [
                    "Total cost = 50(120) + 150(160) = 6,000 + 24,000 = ₹30,000.",
                    "Total shares = 50 + 150 = 200 shares.",
                    "Average price = 30,000 / 200 = ₹150 per share."
                ]
            },
            {
                "question": "In a space debris stacked chart, Active Satellites = 9,000, Dead Spacecraft = 3,500, Rocket Bodies = 2,500, and Total Objects = 35,000. How many Fragmentation Debris objects exist?",
                "options": ["20,000", "15,000", "25,000", "18,000"],
                "answer": 0,
                "solution_steps": [
                    "Sum the three known categories: 9,000 + 3,500 + 2,500 = 15,000.",
                    "Subtract from total stack height: 35,000 − 15,000.",
                    "Fragmentation Debris = 20,000 objects."
                ]
            },
            {
                "question": "In a disability census 100% stacked bar for Region P (total 10,000 persons), Locomotor is 40%, Visual is 20%, Hearing is 15%, and Speech/Other makes up the rest. How many persons are in Speech/Other?",
                "options": ["2,500 persons (25%)", "1,500 persons (15%)", "3,500 persons (35%)", "2,000 persons (20%)"],
                "answer": 0,
                "solution_steps": [
                    "Remaining percentage = 100% − (40% + 20% + 15%) = 25%.",
                    "Absolute count = 25% of 10,000.",
                    "= 2,500 persons."
                ]
            },
            {
                "question": "Two fertilizers A (12% N) and B (32% N) are mixed in a 3 : 2 mass ratio. What is the nitrogen percentage of the blend?",
                "options": ["20%", "22%", "18%", "24%"],
                "answer": 0,
                "solution_steps": [
                    "Use weights W₁ = 3, W₂ = 2: (3×12 + 2×32) / (3 + 2).",
                    "= (36 + 64) / 5 = 100 / 5.",
                    "= 20% nitrogen."
                ]
            },
            {
                "question": "A town's 300-km highway trip has 120 km driven at 60 km/h and 180 km driven at 90 km/h. What is the true average speed (total distance / total time)?",
                "options": ["75 km/h", "78 km/h", "72 km/h", "80 km/h"],
                "answer": 0,
                "solution_steps": [
                    "Time 1 = 120 / 60 = 2 hours; Time 2 = 180 / 90 = 2 hours.",
                    "Total time = 2 + 2 = 4 hours; Total distance = 300 km.",
                    "Average speed = 300 / 4 = 75 km/h (note: equal times happened to match (60+90)/2!)."
                ]
            },
            {
                "question": "Three classes of 20, 30, and 50 students have pass percentages of 90%, 80%, and 70%. What is the overall pass percentage?",
                "options": ["77%", "80%", "78%", "75%"],
                "answer": 0,
                "solution_steps": [
                    "Total passing students = 20(0.90) + 30(0.80) + 50(0.70) = 18 + 24 + 35 = 77.",
                    "Total students = 20 + 30 + 50 = 100.",
                    "Overall pass rate = 77 / 100 = 77%."
                ]
            },
            {
                "question": "In a garden blooming stacked chart, Month 1 has 12 roses, 8 marigolds, and 5 jasmines; Month 2 has 6 roses, 14 marigolds, and 10 jasmines. Which month has MORE total blooming species, and by how many?",
                "options": [
                    "Month 2 has 30 total vs Month 1's 25 (more by 5)",
                    "Month 1 has 30 total vs Month 2's 25",
                    "Both have 25",
                    "Month 2 has 28 total"
                ],
                "answer": 0,
                "solution_steps": [
                    "Month 1 stack height = 12 + 8 + 5 = 25.",
                    "Month 2 stack height = 6 + 14 + 10 = 30.",
                    "Month 2 exceeds Month 1 by 30 − 25 = 5."
                ]
            },
            {
                "question": "A custom project grading scheme uses Design (weight 3), Code (weight 4), Presentation (weight 3). Scores are 9, 8, and 7 out of 10. Find the weighted score out of 10.",
                "options": ["8.0", "8.2", "7.8", "8.5"],
                "answer": 0,
                "solution_steps": [
                    "Weighted sum = 3(9) + 4(8) + 3(7) = 27 + 32 + 21 = 80.",
                    "Total weight = 3 + 4 + 3 = 10.",
                    "Weighted score = 80 / 10 = 8.0 out of 10."
                ]
            },
            {
                "question": "Which principle best summarizes Chapter 10 (How Quantities Combine: Understanding Data)?",
                "options": [
                    "Weight every component by its true size, quantity, or importance (ΣWᵢxᵢ / ΣWᵢ), and choose stacked vs 100% stacked charts to match whether totals or proportions are being compared",
                    "Always average two averages by dividing their sum by 2",
                    "100% stacked bars always show larger absolute totals as longer bars",
                    "Upper segments in stacked charts can be read directly from the top axis tick without subtraction"
                ],
                "answer": 0,
                "solution_steps": [
                    "Weighted means prevent 'average of averages' errors across unequal groups, mixtures, alloys, and custom rubrics.",
                    "Regular stacked charts show totals + parts; 100% stacked charts show normalized proportions.",
                    "Upper stacked segments always require subtracting bottom boundary from top boundary."
                ]
            }
        ]
    }
]

for _s in slides_part3:
    for _q in _s["questions"]:
        _q.setdefault("hint", _q["solution_steps"][0])
        _q.setdefault("explanation", _q["solution_steps"][-1])

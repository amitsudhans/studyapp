#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 2: Introduction to Linear Polynomials
Slides Data Generator - Part 3 (Slides 17 to 20: 40 Mastery Quiz Questions)
Silent quiz/exercise slides with 3-step mathematical solutions, zero fictional human names.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Polynomials Basics Quiz",
        "subtitle": "Exercise Set 1 (Questions 1–10): Expressions, Terms, Coefficients, Degrees (0–3), Linear Models & Constant Differences",
        "questions": [
            {
                "question": "A stationary store sells pens in packs of 8 plus loose individual pens. Which expression represents 5 packs plus k loose pens?",
                "options": [
                    "40 + k",
                    "8k + 5",
                    "13k",
                    "5k + 8"
                ],
                "answer": 0,
                "hint": "Each of the 5 packs holds 8 pens (5 × 8 = 40), plus k single pens!",
                "explanation": "5 packs × 8 pens/pack = 40 pens, plus k loose pens yields 40 + k.",
                "solution_steps": [
                    "Identify fixed pack size: 8 pens per pack across 5 packs = 5 × 8 = 40 pens.",
                    "Add the variable number of loose pens represented by k.",
                    "Total pen count expression is 40 + k."
                ]
            },
            {
                "question": "In the cubic polynomial 5y³ + y² + 2y - 1, identify the coefficient of y², the coefficient of y, and the constant term.",
                "options": [
                    "Coeff of y² is 1, coeff of y is 2, constant term is -1",
                    "Coeff of y² is 0, coeff of y is 2, constant term is 1",
                    "Coeff of y² is 5, coeff of y is 1, constant term is -1",
                    "Coeff of y² is 2, coeff of y is 1, constant term is -1"
                ],
                "answer": 0,
                "hint": "Remember y² means 1·y², and keep the minus sign with -1!",
                "explanation": "1·y² gives coefficient 1, +2y gives coefficient 2, and standalone -1 is the constant term.",
                "solution_steps": [
                    "Split polynomial into terms: 5y³, +1y², +2y, and -1.",
                    "Read numeric multipliers: y² has invisible multiplier 1; y has multiplier 2.",
                    "The standalone constant term keeping its sign is -1."
                ]
            },
            {
                "question": "What is the degree of the constant polynomial 8 (written as 8x⁰)?",
                "options": [
                    "Degree 0",
                    "Degree 1",
                    "Degree 8",
                    "Degree 2"
                ],
                "answer": 0,
                "hint": "The exponent on x inside 8x⁰ is 0!",
                "explanation": "Every non-zero constant c = cx⁰ has highest variable exponent 0, so its degree is 0.",
                "solution_steps": [
                    "Degree of a univariate polynomial is the highest non-zero power of its variable.",
                    "Writing 8 as 8x⁰ shows exponent 0 explicitly.",
                    "Therefore constant non-zero polynomial 8 has degree 0."
                ]
            },
            {
                "question": "Which of the following is a LINEAR univariate polynomial?",
                "options": [
                    "3z + 7",
                    "x² + 5x + 1",
                    "5y³ + y² + 2y - 1",
                    "4/x + 9"
                ],
                "answer": 0,
                "hint": "A linear polynomial has highest variable exponent strictly equal to 1!",
                "explanation": "3z + 7 has single variable z with highest exponent 1 (degree 1), whereas x² is quadratic, y³ is cubic, and 4/x = 4x⁻¹ is not a polynomial.",
                "solution_steps": [
                    "Check each option: x² + 5x + 1 has degree 2 (quadratic); 5y³ + y² + 2y - 1 has degree 3 (cubic).",
                    "4/x + 9 contains negative exponent x⁻¹, so it is not a polynomial.",
                    "3z + 7 has whole-number exponent 1 and non-zero coefficient 3, making it linear."
                ]
            },
            {
                "question": "Evaluate the polynomial P(x) = 3x - 7 at x = -4.",
                "options": [
                    "-19",
                    "5",
                    "-5",
                    "19"
                ],
                "answer": 0,
                "hint": "Substitute x = -4 carefully: 3(-4) - 7!",
                "explanation": "P(-4) = 3(-4) - 7 = -12 - 7 = -19.",
                "solution_steps": [
                    "Start with P(x) = 3x - 7.",
                    "Substitute x = -4: P(-4) = 3(-4) - 7 = -12 - 7.",
                    "Combine negative numbers cleanly: P(-4) = -19."
                ]
            },
            {
                "question": "A fencing project surrounds a square field of side x metres at ₹45 per metre plus a fixed ₹250 gate installation cost. Which linear expression gives total cost?",
                "options": [
                    "180x + 250",
                    "45x + 250",
                    "4x + 250",
                    "250x + 180"
                ],
                "answer": 0,
                "hint": "Square perimeter is 4x metres, multiplied by ₹45 per metre, then add the ₹250 gate fee!",
                "explanation": "Perimeter = 4x m → wire cost = 45(4x) = 180x, plus ₹250 fixed cost = 180x + 250.",
                "solution_steps": [
                    "Compute perimeter of square of side x: P = 4x metres.",
                    "Multiply perimeter by rate ₹45/m: 45 × 4x = 180x.",
                    "Add fixed baseline gate cost ₹250: Total Cost = 180x + 250."
                ]
            },
            {
                "question": "If P(x) = ax + b yields P(1) = 9, P(2) = 14, P(3) = 19, P(4) = 24, what are the values of a and b?",
                "options": [
                    "a = 5 and b = 4",
                    "a = 4 and b = 5",
                    "a = 9 and b = 5",
                    "a = 5 and b = 9"
                ],
                "answer": 0,
                "hint": "Constant difference gives a = 14 - 9 = 5; then check 5(1) + b = 9!",
                "explanation": "Successive difference 14 - 9 = 5 gives a = 5; substituting x = 1 yields 5(1) + b = 9 ⇒ b = 4.",
                "solution_steps": [
                    "Compute constant successive difference: 14 - 9 = 5, 19 - 14 = 5, 24 - 19 = 5 ⇒ slope a = 5.",
                    "Substitute (1, 9) into y = 5x + b: 9 = 5(1) + b.",
                    "Solve b = 9 - 5 = 4, yielding P(x) = 5x + 4."
                ]
            },
            {
                "question": "Which sequence of consecutive outputs for x = 0, 1, 2, 3 does NOT come from a linear polynomial?",
                "options": [
                    "2, 5, 10, 17",
                    "4, 7, 10, 13",
                    "20, 15, 10, 5",
                    "-6, -2, 2, 6"
                ],
                "answer": 0,
                "hint": "Check first differences! Only one sequence has changing jumps instead of a constant step!",
                "explanation": "For 2, 5, 10, 17 the differences are +3, +5, +7 (not constant — that is x² + 1!), whereas all others have constant differences (+3, -5, +4).",
                "solution_steps": [
                    "Test differences: (B) +3, +3, +3; (C) -5, -5, -5; (D) +4, +4, +4.",
                    "Test (A) 2, 5, 10, 17: differences are 5-2 = 3, 10-5 = 5, 17-10 = 7.",
                    "Non-constant first differences prove 2, 5, 10, 17 is non-linear (specifically quadratic x² + 2x + 2 or x² + 1)."
                ]
            },
            {
                "question": "In the input-output model y = -3x + 12, what input x produces output y = 0?",
                "options": [
                    "x = 4",
                    "x = -4",
                    "x = 12",
                    "x = 9"
                ],
                "answer": 0,
                "hint": "Solve -3x + 12 = 0!",
                "explanation": "-3x + 12 = 0 ⇒ 3x = 12 ⇒ x = 4.",
                "solution_steps": [
                    "Set output y = 0 in y = -3x + 12: 0 = -3x + 12.",
                    "Add 3x to both sides: 3x = 12.",
                    "Divide by 3: x = 4."
                ]
            },
            {
                "question": "A rectangular garden plot has length (3w + 2) metres and width 4 metres. Which simplified linear polynomial expresses its area?",
                "options": [
                    "12w + 8 square metres",
                    "3w + 6 square metres",
                    "6w + 12 square metres",
                    "7w + 6 square metres"
                ],
                "answer": 0,
                "hint": "Area = length × width = 4 × (3w + 2) using the distributive property!",
                "explanation": "4(3w + 2) = 12w + 8 square metres (degree-1 linear expression in w).",
                "solution_steps": [
                    "Write Rectangle Area = width × length = 4(3w + 2).",
                    "Apply distributive property: 4 × 3w + 4 × 2 = 12w + 8.",
                    "Simplified area polynomial is 12w + 8 square metres."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Patterns Growth Quiz",
        "subtitle": "Exercise Set 2 (Questions 1–10): Tile Patterns (2n-1), Linear Sequences, Growth C(d) & Linear Decay h(t) Models",
        "questions": [
            {
                "question": "In the growing square tile sequence whose term rule is T(n) = 2n - 1, which step number n requires exactly 39 tiles?",
                "options": [
                    "n = 20",
                    "n = 19",
                    "n = 21",
                    "n = 77"
                ],
                "answer": 0,
                "hint": "Set 2n - 1 = 39 and solve for n!",
                "explanation": "2n - 1 = 39 ⇒ 2n = 40 ⇒ n = 20.",
                "solution_steps": [
                    "Set general term equal to 39: 2n - 1 = 39.",
                    "Add 1 to both sides: 2n = 40.",
                    "Divide by 2: Step n = 20."
                ]
            },
            {
                "question": "A daily allowance budget starts at ₹600 and spends ₹25 per day. After d days, which expression gives remaining allowance and on which day does it hit ₹0?",
                "options": [
                    "600 - 25d; reaches ₹0 after 24 days",
                    "600 + 25d; reaches ₹0 after 20 days",
                    "600 - 25d; reaches ₹0 after 15 days",
                    "25d - 600; reaches ₹0 after 24 days"
                ],
                "answer": 0,
                "hint": "Solve 600 - 25d = 0!",
                "explanation": "Balance is 600 - 25d; 25d = 600 ⇒ d = 600 / 25 = 24 days.",
                "solution_steps": [
                    "Model remaining money: initial ₹600 minus ₹25 × d days = 600 - 25d.",
                    "Set balance to zero: 600 - 25d = 0 ⇒ 25d = 600.",
                    "Solve d = 600 / 25 = 24 days."
                ]
            },
            {
                "question": "A tiered auto-rickshaw charges ₹30 for the first 2 km and ₹12 for every additional kilometre thereafter. What is the fare for a 10 km journey?",
                "options": [
                    "₹126",
                    "₹150",
                    "₹120",
                    "₹106"
                ],
                "answer": 0,
                "hint": "First 2 km cost ₹30 flat; remaining (10 - 2) = 8 km each cost ₹12!",
                "explanation": "Fare = 30 + 12(10 - 2) = 30 + 96 = ₹126.",
                "solution_steps": [
                    "Base fare covers first 2 km for ₹30.",
                    "Additional distance = 10 - 2 = 8 km billed at ₹12/km = 8 × 12 = ₹96.",
                    "Total fare = 30 + 96 = ₹126."
                ]
            },
            {
                "question": "A reading goal tracks unread pages of a 320-page book read at 16 pages per day. How many days are needed to finish the entire book?",
                "options": [
                    "20 days",
                    "16 days",
                    "18 days",
                    "24 days"
                ],
                "answer": 0,
                "hint": "Model unread pages U(d) = 320 - 16d and set U(d) = 0!",
                "explanation": "320 - 16d = 0 ⇒ 16d = 320 ⇒ d = 20 days.",
                "solution_steps": [
                    "Unread pages function: U(d) = 320 - 16d.",
                    "Completion means 0 pages remaining: 320 - 16d = 0.",
                    "Divide 320 by 16: d = 20 days."
                ]
            },
            {
                "question": "For the linear growth cost model C(d) = 100 + 60d, how much larger is C(10) than C(4)?",
                "options": [
                    "360 (since 6 days × 60 = 360)",
                    "460",
                    "600",
                    "240"
                ],
                "answer": 0,
                "hint": "Compute C(10) - C(4) = 60(10 - 4)!",
                "explanation": "C(10) = 700 and C(4) = 340; difference = 700 - 340 = 360 (baseline 100 cancels).",
                "solution_steps": [
                    "Evaluate C(10) = 100 + 60(10) = 700 and C(4) = 100 + 60(4) = 340.",
                    "Subtract: C(10) - C(4) = 700 - 340 = 360.",
                    "Notice shortcut: ΔC = rate × Δd = 60 × (10 - 4) = 360."
                ]
            },
            {
                "question": "For candle decay h(t) = 3 - 0.5t (in decimetres, t in hours), what is the candle's height at t = 3.5 hours?",
                "options": [
                    "1.25 decimetres",
                    "1.75 decimetres",
                    "1.5 decimetres",
                    "0.75 decimetres"
                ],
                "answer": 0,
                "hint": "Compute 3 - 0.5 × 3.5 = 3 - 1.75!",
                "explanation": "h(3.5) = 3 - 0.5(3.5) = 3 - 1.75 = 1.25 dm.",
                "solution_steps": [
                    "Substitute t = 3.5 into h(t) = 3 - 0.5t.",
                    "Multiply rate by time: 0.5 × 3.5 = 1.75 dm melted.",
                    "Subtract from initial height 3: h(3.5) = 3 - 1.75 = 1.25 dm."
                ]
            },
            {
                "question": "A delivery van purchased for ₹9,00,000 depreciates linearly by ₹75,000 each year. What is its value after 6 years?",
                "options": [
                    "₹4,50,000",
                    "₹5,25,000",
                    "₹3,75,000",
                    "₹6,00,000"
                ],
                "answer": 0,
                "hint": "Evaluate V(6) = 9,00,000 - 75,000 × 6!",
                "explanation": "Total depreciation over 6 years = 6 × 75,000 = ₹4,50,000; remaining value = 9,00,000 - 4,50,000 = ₹4,50,000.",
                "solution_steps": [
                    "Model vehicle depreciation: V(t) = 9,00,000 - 75,000t.",
                    "Substitute t = 6: V(6) = 9,00,000 - (75,000 × 6) = 9,00,000 - 4,50,000.",
                    "Remaining asset value is ₹4,50,000."
                ]
            },
            {
                "question": "A village has 3,200 people and declines linearly at 50 residents per year. What will its population be after 8 years?",
                "options": [
                    "2,800 residents",
                    "3,600 residents",
                    "2,400 residents",
                    "2,750 residents"
                ],
                "answer": 0,
                "hint": "Compute P(8) = 3200 - 50(8)!",
                "explanation": "P(8) = 3200 - 400 = 2,800 residents.",
                "solution_steps": [
                    "Write linear decay function: P(t) = 3200 - 50t.",
                    "Evaluate at t = 8: 50 × 8 = 400 residents decrease.",
                    "3200 - 400 = 2,800 residents."
                ]
            },
            {
                "question": "In a savings plan S(w) = 450 + 85w, which statement explains why it represents linear growth?",
                "options": [
                    "The coefficient of w is positive (+85), adding ₹85 consistently each week",
                    "The constant baseline 450 is positive",
                    "Savings double every single week",
                    "Because S(0) = 0"
                ],
                "answer": 0,
                "hint": "Growth vs decay is controlled strictly by the sign of rate parameter a, not baseline b!",
                "explanation": "Positive slope a = +85 > 0 ensures S(w + 1) - S(w) = +85 > 0, representing steady linear growth.",
                "solution_steps": [
                    "Compare S(w) = 450 + 85w against y = ax + b: rate a = +85 and baseline b = 450.",
                    "Positive rate a > 0 causes output to increase uniformly by ₹85 per week.",
                    "Hence sign of rate a (+85 > 0) establishes linear growth."
                ]
            },
            {
                "question": "A sunflower grows linearly from 14 cm to 44 cm over 6 weeks. What is its weekly growth rate and predicted height at week 10?",
                "options": [
                    "5 cm/week; 64 cm at week 10",
                    "6 cm/week; 74 cm at week 10",
                    "4 cm/week; 54 cm at week 10",
                    "5 cm/week; 50 cm at week 10"
                ],
                "answer": 0,
                "hint": "Growth rate = (44 - 14) / 6 = 30 / 6 cm/week; then evaluate 14 + rate × 10!",
                "explanation": "Rate a = 30/6 = 5 cm/week, baseline b = 14 cm → H(10) = 14 + 5(10) = 64 cm.",
                "solution_steps": [
                    "Compute constant growth rate: a = (44 - 14) / (6 - 0) = 30 / 6 = 5 cm/week.",
                    "Formulate H(w) = 5w + 14.",
                    "Substitute w = 10: H(10) = 5(10) + 14 = 64 cm."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Linear Systems Quiz",
        "subtitle": "Exercise Set 3 (Questions 1–10): Formulating (a,b) from Data, Telecom/Gym/Modules, °C↔°F, Origin Lines & Parallel Slopes",
        "questions": [
            {
                "question": "A linear equation passes through points (3, 10) and (7, 22). Find the equation in slope-intercept form y = ax + b.",
                "options": [
                    "y = 3x + 1",
                    "y = 3x - 1",
                    "y = 4x - 2",
                    "y = 2x + 4"
                ],
                "answer": 0,
                "hint": "Calculate slope a = (22 - 10)/(7 - 3), then substitute (3, 10) to find b!",
                "explanation": "a = 12/4 = 3; 10 = 3(3) + b ⇒ b = 1, giving y = 3x + 1.",
                "solution_steps": [
                    "Set up system: 3a + b = 10 and 7a + b = 22.",
                    "Subtract equations: 4a = 12 ⇒ a = 3.",
                    "Back-substitute: b = 10 - 3(3) = 1 ⇒ y = 3x + 1."
                ]
            },
            {
                "question": "A telecom carrier bills ₹380 for 6 GB of data and ₹540 for 10 GB under a flat monthly rental plus per-GB rate. Find the flat monthly fee and rate per GB.",
                "options": [
                    "Flat fee ₹140; rate ₹40 per GB",
                    "Flat fee ₹100; rate ₹45 per GB",
                    "Flat fee ₹160; rate ₹35 per GB",
                    "Flat fee ₹40; rate ₹140 per GB"
                ],
                "answer": 0,
                "hint": "4 extra GB cost 540 - 380 = ₹160!",
                "explanation": "Per-GB rate a = 160 / 4 = ₹40; flat rental b = 380 - 6(40) = ₹140.",
                "solution_steps": [
                    "Let C = ax + b: 6a + b = 380 and 10a + b = 540.",
                    "Subtract to eliminate b: 4a = 160 ⇒ a = ₹40 per GB.",
                    "Substitute back: b = 380 - 240 = ₹140 flat monthly fee."
                ]
            },
            {
                "question": "A gym charges a membership fee b plus hourly court rental a. A member pays ₹950 for 5 hours and ₹1,400 for 8 hours. What does 12 hours cost?",
                "options": [
                    "₹2,000",
                    "₹1,850",
                    "₹2,200",
                    "₹1,950"
                ],
                "answer": 0,
                "hint": "Find hourly rate a = (1400 - 950)/(8 - 5) = 150 and b = 200, then compute 150(12) + 200!",
                "explanation": "3 extra hours cost ₹450 ⇒ a = ₹150/hr and b = 950 - 750 = ₹200; for 12 hrs: 150(12) + 200 = ₹2,000.",
                "solution_steps": [
                    "Hourly rate: a = (1400 - 950) / (8 - 5) = 450 / 3 = ₹150/hr.",
                    "Membership baseline: b = 950 - 5(150) = ₹200.",
                    "Evaluate at 12 hours: C(12) = 150(12) + 200 = 1800 + 200 = ₹2,000."
                ]
            },
            {
                "question": "At what temperature do Celsius (°C) and Fahrenheit (°F) scales read the EXACT same numerical value?",
                "options": [
                    "-40° (i.e., -40 °C = -40 °F)",
                    "0°",
                    "32°",
                    "-273°"
                ],
                "answer": 0,
                "hint": "Set C = (9/5)C + 32 and solve for C!",
                "explanation": "C - (9/5)C = 32 ⇒ (-4/5)C = 32 ⇒ C = -40°.",
                "solution_steps": [
                    "Equate C and F in F = (9/5)C + 32: C = (9/5)C + 32.",
                    "Subtract (9/5)C: (-4/5)C = 32.",
                    "Multiply by -5/4: C = -40, so -40 °C = -40 °F."
                ]
            },
            {
                "question": "Which point ALWAYS lies on every straight line of form y = ax regardless of slope a?",
                "options": [
                    "The Origin (0, 0)",
                    "(1, 0)",
                    "(0, 1)",
                    "(1, 1)"
                ],
                "answer": 0,
                "hint": "Substitute x = 0 into y = ax!",
                "explanation": "When x = 0, y = a(0) = 0, so every line y = ax (b = 0) passes through Origin (0, 0).",
                "solution_steps": [
                    "Inspect y = ax (missing constant term means b = 0).",
                    "Substitute x = 0: y = a × 0 = 0.",
                    "Thus (0, 0) always satisfies y = ax for any real slope a."
                ]
            },
            {
                "question": "How does the graph of y = (1/4)x compare visually to y = x in Quadrant I?",
                "options": [
                    "y = (1/4)x is significantly flatter (closer to the x-axis) because |a| = 1/4 < 1",
                    "y = (1/4)x is steeper (closer to the y-axis)",
                    "y = (1/4)x shifts 1/4 unit upward",
                    "y = (1/4)x slopes downward into Quadrant IV"
                ],
                "answer": 0,
                "hint": "For Origin lines y = ax, slopes with 0 < a < 1 rise less vertically than y = x!",
                "explanation": "At x = 4, y = (1/4)(4) = 1 versus y = 4 on y = x, making y = (1/4)x much flatter.",
                "solution_steps": [
                    "Compare slopes: y = x has a = 1; y = (1/4)x has a = 0.25.",
                    "Since 0 < 0.25 < 1, each 1 unit right rises only 0.25 units instead of 1 unit.",
                    "Thus y = (1/4)x appears flatter and closer to the horizontal x-axis."
                ]
            },
            {
                "question": "Compare lines L₁: y = -2x + 5 and L₂: y = -2x - 3. Which geometric statement is true?",
                "options": [
                    "L₁ and L₂ are parallel lines with negative slope -2, crossing the y-axis at (0, 5) and (0, -3)",
                    "L₁ and L₂ intersect at (-2, 0)",
                    "L₁ is steeper than L₂",
                    "Both lines represent linear growth"
                ],
                "answer": 0,
                "hint": "Both equations have identical coefficient of x (-2) and different constants (+5 vs -3)!",
                "explanation": "Equal slope a = -2 with distinct y-intercepts (0, 5) and (0, -3) produces two parallel lines declining left-to-right.",
                "solution_steps": [
                    "Read slope-intercept parameters: L₁ has a = -2, b = 5; L₂ has a = -2, b = -3.",
                    "Equal slope a₁ = a₂ = -2 forces identical tilt (descending left-to-right).",
                    "Distinct intercepts (0, 5) ≠ (0, -3) mean L₁ and L₂ are parallel and never meet."
                ]
            },
            {
                "question": "If the graph of y = ax + b crosses the y-axis at (0, -6) and passes through (2, 4), find a and b.",
                "options": [
                    "a = 5 and b = -6",
                    "a = -6 and b = 5",
                    "a = 2 and b = -6",
                    "a = -1 and b = -6"
                ],
                "answer": 0,
                "hint": "The y-intercept directly gives b = -6; then plug (2, 4) into y = ax - 6!",
                "explanation": "y-intercept (0, -6) sets b = -6; 4 = 2a - 6 ⇒ 2a = 10 ⇒ a = 5.",
                "solution_steps": [
                    "From y-intercept (0, b) = (0, -6), read baseline b = -6 immediately.",
                    "Substitute point (2, 4) into y = ax - 6: 4 = a(2) - 6.",
                    "Solve 2a = 10 ⇒ a = 5, equation y = 5x - 6."
                ]
            },
            {
                "question": "Which equation produces a straight line PARALLEL to y = 4x - 9 and passing through (0, 3)?",
                "options": [
                    "y = 4x + 3",
                    "y = 3x - 9",
                    "y = -4x + 3",
                    "y = 3x + 4"
                ],
                "answer": 0,
                "hint": "Parallel requires keeping slope a = 4, and passing through (0, 3) fixes y-intercept b = 3!",
                "explanation": "Matching slope a = 4 ensures parallelism, and y-intercept (0, 3) sets b = 3 → y = 4x + 3.",
                "solution_steps": [
                    "Line parallel to y = 4x - 9 must share identical slope a = 4.",
                    "Line passing through (0, 3) has y-intercept b = 3.",
                    "Substitute a = 4, b = 3 into y = ax + b to get y = 4x + 3."
                ]
            },
            {
                "question": "Does the point (-3, -10) lie on the line y = 4x + 2?",
                "options": [
                    "Yes, because 4(-3) + 2 = -12 + 2 = -10",
                    "No, because 4(-3) + 2 = -14",
                    "No, because both coordinates are negative",
                    "Yes, because 4(2) - 3 = 5"
                ],
                "answer": 0,
                "hint": "Plug x = -3 into 4x + 2 and compare to y = -10!",
                "explanation": "Evaluating 4(-3) + 2 yields -12 + 2 = -10, matching the y-coordinate, so (-3, -10) lies on the line.",
                "solution_steps": [
                    "Take test point (-3, -10): x = -3, target y = -10.",
                    "Substitute x = -3 into right-hand side: 4(-3) + 2 = -12 + 2 = -10.",
                    "Since LHS = RHS (-10 = -10), (-3, -10) lies directly on the line."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Exercises Mastery Quiz",
        "subtitle": "Exercise Set 4 (Questions 1–10): Polynomial Values, Digit Reversals, Kelvin-Fahrenheit, Work-Distance, Hexagons & Chapter Summary",
        "questions": [
            {
                "question": "For a two-digit number with tens digit x and units digit y (where x > y), what linear polynomial represents (original number) minus (digit-reversed number)?",
                "options": [
                    "9(x - y) = 9x - 9y",
                    "11(x + y)",
                    "10x - y",
                    "9(x + y)"
                ],
                "answer": 0,
                "hint": "Compute (10x + y) - (10y + x)!",
                "explanation": "(10x + y) - (10y + x) = 9x - 9y = 9(x - y), always divisible by 9.",
                "solution_steps": [
                    "Express original two-digit value as 10x + y and reversed two-digit value as 10y + x.",
                    "Subtract: (10x + y) - (10y + x) = 10x - x + y - 10y.",
                    "Simplify cleanly to 9x - 9y = 9(x - y)."
                ]
            },
            {
                "question": "A chain of connected matchstick hexagons uses 6 sticks for 1 hexagon, 11 sticks for 2, and 16 sticks for 3. How many matchsticks are in n joined hexagons, and how many hexagons can 101 sticks form?",
                "options": [
                    "5n + 1 sticks; 20 hexagons from 101 sticks",
                    "6n sticks; 16 hexagons from 101 sticks",
                    "5n - 1 sticks; 20 hexagons from 101 sticks",
                    "5n + 6 sticks; 19 hexagons from 101 sticks"
                ],
                "answer": 0,
                "hint": "Check 5n + 1 = 101!",
                "explanation": "Formula is 5n + 1 (at n=1: 6, n=2: 11); solving 5n + 1 = 101 gives 5n = 100 ⇒ n = 20 hexagons.",
                "solution_steps": [
                    "First hexagon uses 6 sticks and each additional hexagon shares 1 edge, adding 5 sticks: 6 + 5(n - 1) = 5n + 1.",
                    "Set total matchsticks to 101: 5n + 1 = 101 ⇒ 5n = 100.",
                    "Divide by 5: n = 20 hexagons."
                ]
            },
            {
                "question": "If physical work W done by a constant force F of 15 N over displacement d metres follows W = 15d, what does the graph of W versus d look like?",
                "options": [
                    "A straight line passing through Origin (0, 0) with positive slope 15",
                    "A horizontal line at W = 15",
                    "A straight line crossing the vertical axis at (0, 15)",
                    "A downward-sloping line with slope -15"
                ],
                "answer": 0,
                "hint": "Compare W = 15d with Origin-passing linear relationship y = ax!",
                "explanation": "W = 15d has slope a = 15 > 0 and baseline b = 0, so its graph passes through (0, 0) and rises steeply at 15 J per metre.",
                "solution_steps": [
                    "Match W = 15d with y = ax + b: slope a = 15 and y-intercept b = 0.",
                    "When displacement d = 0, work W = 0, placing the line through Origin (0, 0).",
                    "Positive slope 15 yields an upward linear growth line."
                ]
            },
            {
                "question": "Convert a liquid's temperature of 303.15 Kelvin to Fahrenheit using C = K - 273.15 and F = (9/5)C + 32.",
                "options": [
                    "86 °F",
                    "62 °F",
                    "98.6 °F",
                    "76 °F"
                ],
                "answer": 0,
                "hint": "First find C = 303.15 - 273.15 = 30 °C, then plug C = 30 into (9/5)C + 32!",
                "explanation": "C = 303.15 - 273.15 = 30 °C; F = (9/5)(30) + 32 = 54 + 32 = 86 °F.",
                "solution_steps": [
                    "Convert Kelvin to Celsius: C = 303.15 - 273.15 = 30 °C.",
                    "Apply Celsius-to-Fahrenheit linear relation: F = (9/5)(30) + 32.",
                    "Compute 9 × 6 + 32 = 54 + 32 = 86 °F."
                ]
            },
            {
                "question": "Notice that K → F satisfies F = (9/5)(K - 273.15) + 32. What is the constant rate of change (slope) of °F with respect to Kelvin?",
                "options": [
                    "9/5 = 1.8 °F per Kelvin",
                    "5/9 °F per Kelvin",
                    "32 °F per Kelvin",
                    "-273.15 °F per Kelvin"
                ],
                "answer": 0,
                "hint": "Expand (9/5)K - (9/5)(273.15) + 32 and inspect the coefficient multiplying K!",
                "explanation": "Because Celsius and Kelvin step by identical 1-degree intervals (C = K - 273.15), every +1 K rise adds exactly 9/5 = 1.8 °F.",
                "solution_steps": [
                    "Expand F = (9/5)K - (9/5)(273.15) + 32 into slope-intercept form aK + b.",
                    "The coefficient multiplying variable K is a = 9/5 = 1.8.",
                    "Thus Fahrenheit rises linearly at 1.8 °F per 1 Kelvin increase."
                ]
            },
            {
                "question": "Find the intersection point of two competing delivery cost lines: Plan A (y = 20x + 120) and Plan B (y = 35x).",
                "options": [
                    "(8, 280)",
                    "(6, 210)",
                    "(10, 320)",
                    "(4, 140)"
                ],
                "answer": 0,
                "hint": "Set 35x = 20x + 120 to find break-even distance x, then compute 35x!",
                "explanation": "15x = 120 ⇒ x = 8; then y = 35(8) = 280, giving intersection (8, 280).",
                "solution_steps": [
                    "Equate y-values at intersection: 35x = 20x + 120.",
                    "Subtract 20x: 15x = 120 ⇒ x = 8.",
                    "Substitute x = 8 into Plan B: y = 35(8) = 280 ⇒ intersection (8, 280)."
                ]
            },
            {
                "question": "Evaluate the linear polynomial P(z) = 3z + 7 minus Q(z) = 5z - 2 when z = 3.",
                "options": [
                    "3 (since P(3) = 16 and Q(3) = 13)",
                    "29",
                    "-3",
                    "7"
                ],
                "answer": 0,
                "hint": "Compute P(3) = 3(3) + 7 and Q(3) = 5(3) - 2, then subtract P(3) - Q(3)!",
                "explanation": "P(3) = 16 and Q(3) = 13, so P(3) - Q(3) = 16 - 13 = 3 (or (-2z + 9) at z=3 → -6 + 9 = 3).",
                "solution_steps": [
                    "Evaluate P(3) = 3(3) + 7 = 9 + 7 = 16.",
                    "Evaluate Q(3) = 5(3) - 2 = 15 - 2 = 13.",
                    "Subtract: P(3) - Q(3) = 16 - 13 = 3."
                ]
            },
            {
                "question": "Two lines L₁: y = ax + 4 and L₂: y = -3x + b are parallel, and L₁ passes through (0, 4). What is the slope a of L₁?",
                "options": [
                    "a = -3",
                    "a = 4",
                    "a = 3",
                    "a = b"
                ],
                "answer": 0,
                "hint": "Parallel lines ALWAYS share the exact same slope coefficient multiplying x!",
                "explanation": "Since L₂ has slope -3, any line L₁ parallel to L₂ must also have slope a = -3.",
                "solution_steps": [
                    "Read slope of L₂ (y = -3x + b): slope = -3.",
                    "Recall that parallel straight lines have identical slopes: a₁ = a₂.",
                    "Hence slope a of L₁ must equal -3."
                ]
            },
            {
                "question": "How can you distinguish a linear polynomial from a quadratic or cubic polynomial both algebraically and from a value table?",
                "options": [
                    "Algebraically: highest variable exponent is 1; Table: consecutive integer inputs produce constant first differences",
                    "Algebraically: highest exponent is 2; Table: first differences double each step",
                    "Algebraically: constant term must be zero; Table: all outputs stay identical",
                    "Algebraically: contains x⁻¹; Table: ratios stay constant"
                ],
                "answer": 0,
                "hint": "Combine Section 2.1 degree classification with Section 2.2 constant differences!",
                "explanation": "Linear polynomials have degree 1 (ax + b, a ≠ 0) algebraically and yield constant successive difference a across integer inputs.",
                "solution_steps": [
                    "Algebraic test: highest non-zero whole-number exponent of the single variable equals 1.",
                    "Numerical table test: successive integer outputs satisfy P(x + 1) - P(x) = constant a ≠ 0.",
                    "Geometric test: plotted pairs (x, P(x)) align along a non-horizontal straight line."
                ]
            },
            {
                "question": "Which overarching statement best summarizes NCERT Class 9 Chapter 2: Introduction to Linear Polynomials?",
                "options": [
                    "Degree-1 polynomials y = ax + b (a ≠ 0) unite constant-difference patterns, linear growth/decay, simultaneous solvers, and straight-line slope-intercept graphs",
                    "Only cubic polynomials produce straight lines with constant slope",
                    "Changing baseline b in y = ax + b alters the steepness of a line",
                    "Linear equations can never convert between temperature scales or model depreciation"
                ],
                "answer": 0,
                "hint": "Synthesize Sections 2.1 through 2.6: degree 1, constant step a, growth/decay, solvers, and slope-intercept lines!",
                "explanation": "Linear polynomials y = ax + b link algebraic rate & baseline modeling with geometric slope a and y-intercept (0, b).",
                "solution_steps": [
                    "Degree-1 univariate expressions (ax + b, a ≠ 0) model bundled counts, perimeters, tile patterns, and fee rules.",
                    "Sign of rate a distinguishes steady linear growth (a > 0) from linear decay (a < 0), recoverable from two data points.",
                    "On the Cartesian plane, y = ax + b draws a straight line with slope a, y-intercept (0, b), and parallel shifts for fixed a."
                ]
            }
        ]
    }
]

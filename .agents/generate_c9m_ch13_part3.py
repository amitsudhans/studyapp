#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 13: Two Variables, One Line
Part 3: Slides 17 to 20 (Silent Mastery Quiz Slides - 40 Questions with 3-Step Solutions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Equations Graphs Quiz",
        "subtitle": "Mastery Quiz 1 (Silent Exercise): Standard Form, Ordered Pairs & Intercepts (13.1–13.2)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Which of the following is in standard form ax + by + c = 0 for the equation 3x = 7y − 11?",
                "options": [
                    "3x − 7y + 11 = 0",
                    "3x + 7y − 11 = 0",
                    "3x − 7y − 11 = 0",
                    "7y − 3x + 11 = 0",
                ],
                "answer": 0,
                "solution_steps": [
                    "Start with 3x = 7y − 11.",
                    "Subtract 7y and add 11 on both sides to move all terms to the left.",
                    "We obtain 3x − 7y + 11 = 0, so (a, b, c) = (3, −7, 11).",
                ],
            },
            {
                "question": "In the standard form ax + by + c = 0, why must a and b NOT both be zero?",
                "options": [
                    "If a = 0 and b = 0, both variables vanish and the equation is no longer linear in x, y",
                    "Because c must always be zero",
                    "Because a must equal b",
                    "Because x and y must be integers",
                ],
                "answer": 0,
                "solution_steps": [
                    "If a = 0 and b = 0, then ax + by + c = 0 reduces to c = 0.",
                    "Neither x nor y remains in the equation.",
                    "At least one of a or b must be non-zero to define a line.",
                ],
            },
            {
                "question": "How is the equation 5y = 20 written in two-variable standard form ax + by + c = 0?",
                "options": [
                    "0x + 5y − 20 = 0",
                    "5x + 0y − 20 = 0",
                    "x + 5y − 20 = 0",
                    "0x + 5y + 20 = 0",
                ],
                "answer": 0,
                "solution_steps": [
                    "The variable x does not appear, so its coefficient a = 0.",
                    "Move 20 to the left side: 5y − 20 = 0.",
                    "Insert 0x to get 0x + 5y − 20 = 0.",
                ],
            },
            {
                "question": "Clear fractions from (x/3) + (y/4) = 2 to write it in integer standard form.",
                "options": [
                    "4x + 3y − 24 = 0",
                    "3x + 4y − 24 = 0",
                    "4x + 3y − 2 = 0",
                    "x + y − 12 = 0",
                ],
                "answer": 0,
                "solution_steps": [
                    "Multiply every term by LCM(3, 4) = 12.",
                    "12(x/3) + 12(y/4) = 12(2) gives 4x + 3y = 24.",
                    "Subtract 24: 4x + 3y − 24 = 0.",
                ],
            },
            {
                "question": "Which ordered pair is a solution of 2x − 3y = 12?",
                "options": ["(3, −2)", "(−2, 3)", "(2, 3)", "(0, 4)"],
                "answer": 0,
                "solution_steps": [
                    "Test (3, −2): substitute x = 3 and y = −2.",
                    "2(3) − 3(−2) = 6 + 6 = 12.",
                    "Since LHS = RHS, (3, −2) is a solution.",
                ],
            },
            {
                "question": "How many solutions does the equation x − 4y = 9 have?",
                "options": [
                    "Infinitely many solutions",
                    "Exactly one solution",
                    "Exactly four solutions",
                    "No solution",
                ],
                "answer": 0,
                "solution_steps": [
                    "Rewrite as x = 4y + 9.",
                    "For each real number y, there is a corresponding real value x.",
                    "Hence there are infinitely many ordered-pair solutions.",
                ],
            },
            {
                "question": "Find the x-intercept and y-intercept of 3x + 4y = 24.",
                "options": [
                    "(8, 0) and (0, 6)",
                    "(6, 0) and (0, 8)",
                    "(3, 0) and (0, 4)",
                    "(24, 0) and (0, 24)",
                ],
                "answer": 0,
                "solution_steps": [
                    "Set y = 0: 3x = 24 ⇒ x = 8, giving x-intercept (8, 0).",
                    "Set x = 0: 4y = 24 ⇒ y = 6, giving y-intercept (0, 6).",
                    "Both intercepts plot the line immediately.",
                ],
            },
            {
                "question": "If (2, k) is a solution of 5x + 3y = 22, find k.",
                "options": ["4", "3", "5", "6"],
                "answer": 0,
                "solution_steps": [
                    "Substitute x = 2 and y = k into 5x + 3y = 22.",
                    "5(2) + 3k = 22 ⇒ 10 + 3k = 22.",
                    "3k = 12 ⇒ k = 4.",
                ],
            },
            {
                "question": "Which point lies on the line y = 3x − 2?",
                "options": ["(2, 4)", "(4, 2)", "(1, 3)", "(0, 2)"],
                "answer": 0,
                "solution_steps": [
                    "Substitute x = 2 into y = 3x − 2.",
                    "y = 3(2) − 2 = 6 − 2 = 4.",
                    "Therefore (2, 4) lies on the line.",
                ],
            },
            {
                "question": "Which real-world cost is modeled by 60x + 50y = 280?",
                "options": [
                    "Buying x kg of fruit at ₹60/kg and y kg at ₹50/kg for ₹280",
                    "Buying 60 kg of fruit for ₹280",
                    "Traveling 280 km in 60 hours",
                    "Adding 60 and 50 to get 280",
                ],
                "answer": 0,
                "solution_steps": [
                    "60x represents cost of x kg at ₹60/kg.",
                    "50y represents cost of y kg at ₹50/kg.",
                    "Their sum equals the total expenditure ₹280.",
                ],
            },
        ],
    },
    {
        "id": 18,
        "title": "Slope Intercept Quiz",
        "subtitle": "Mastery Quiz 2 (Silent Exercise): Rise/Run, Slope Types & y = mx + d (13.3)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Find the slope of the line passing through (1, 4) and (5, 16).",
                "options": ["3", "4", "1/3", "12"],
                "answer": 0,
                "solution_steps": [
                    "Use m = (y₂ − y₁) / (x₂ − x₁).",
                    "m = (16 − 4) / (5 − 1) = 12 / 4.",
                    "m = 3.",
                ],
            },
            {
                "question": "Find the slope of the line passing through (2, 9) and (6, 1).",
                "options": ["−2", "2", "−1/2", "8"],
                "answer": 0,
                "solution_steps": [
                    "m = (1 − 9) / (6 − 2) = −8 / 4.",
                    "m = −2.",
                    "Negative slope means the line falls from left to right.",
                ],
            },
            {
                "question": "What is the slope of the horizontal line y = −5?",
                "options": ["0", "−5", "1", "Undefined"],
                "answer": 0,
                "solution_steps": [
                    "On y = −5, every point has the same y-coordinate (−5).",
                    "Rise = y₂ − y₁ = 0 for any two points.",
                    "Slope m = 0 / Run = 0.",
                ],
            },
            {
                "question": "Why is the slope of a vertical line x = 7 undefined?",
                "options": [
                    "Its horizontal Run (x₂ − x₁) is 0, causing division by zero",
                    "Its Rise is 0",
                    "It passes through (0, 0)",
                    "It has two y-intercepts",
                ],
                "answer": 0,
                "solution_steps": [
                    "Every point on x = 7 has x = 7, so x₂ − x₁ = 0.",
                    "In Rise / Run = (y₂ − y₁) / 0, the denominator is zero.",
                    "Division by zero is undefined.",
                ],
            },
            {
                "question": "Rewrite 4x + 2y − 10 = 0 in slope-intercept form y = mx + d.",
                "options": [
                    "y = −2x + 5",
                    "y = 2x − 5",
                    "y = −4x + 10",
                    "y = 2x + 5",
                ],
                "answer": 0,
                "solution_steps": [
                    "Isolate 2y: 2y = −4x + 10.",
                    "Divide every term by 2: y = −2x + 5.",
                    "Here slope m = −2 and y-intercept d = 5.",
                ],
            },
            {
                "question": "Using m = −a/b and d = −c/b for 3x − 5y + 15 = 0, find (m, d).",
                "options": [
                    "m = 3/5, d = 3",
                    "m = −3/5, d = −3",
                    "m = 5/3, d = 5",
                    "m = 3/5, d = −3",
                ],
                "answer": 0,
                "solution_steps": [
                    "Here a = 3, b = −5, c = 15.",
                    "m = −a/b = −3/(−5) = 3/5.",
                    "d = −c/b = −15/(−5) = 3.",
                ],
            },
            {
                "question": "Which line is steeper: y = 5x + 1 or y = 2x + 9?",
                "options": [
                    "y = 5x + 1 (larger |m| = 5 > 2)",
                    "y = 2x + 9 (larger y-intercept 9 > 1)",
                    "Both have equal steepness",
                    "Cannot be compared",
                ],
                "answer": 0,
                "solution_steps": [
                    "Steepness depends solely on the magnitude of slope |m|, not on the y-intercept.",
                    "|5| = 5 > |2| = 2.",
                    "Therefore y = 5x + 1 climbs more steeply.",
                ],
            },
            {
                "question": "What is the y-intercept of the line y = −4x?",
                "options": ["0 (passes through origin)", "−4", "4", "1"],
                "answer": 0,
                "solution_steps": [
                    "Compare y = −4x with y = mx + d.",
                    "Here m = −4 and d = 0.",
                    "Setting x = 0 gives y = 0, so it crosses the y-axis at (0, 0).",
                ],
            },
            {
                "question": "Two lines have equations y = 3x + 2 and y = 3x − 7. How are they related?",
                "options": [
                    "They are parallel and never intersect",
                    "They intersect at (3, 0)",
                    "They are perpendicular",
                    "They are identical",
                ],
                "answer": 0,
                "solution_steps": [
                    "Both lines have the exact same slope m = 3.",
                    "Their y-intercepts differ (2 ≠ −7).",
                    "Same slope + different intercepts = parallel lines.",
                ],
            },
            {
                "question": "If a line has slope m = 4 and passes through (0, −3), what is its equation?",
                "options": [
                    "y = 4x − 3",
                    "y = −3x + 4",
                    "y = 4x + 3",
                    "4x + 3y = 0",
                ],
                "answer": 0,
                "solution_steps": [
                    "The point (0, −3) is the y-intercept, so d = −3.",
                    "Given slope m = 4.",
                    "Substitute into y = mx + d to get y = 4x − 3.",
                ],
            },
        ],
    },
    {
        "id": 19,
        "title": "Algebraic Systems Quiz",
        "subtitle": "Mastery Quiz 3 (Silent Exercise): Substitution, Elimination, Ratio Criteria & History (13.4–13.5)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Solve using Substitution: x − y = 4 and 2x + y = 17.",
                "options": ["(7, 3)", "(3, 7)", "(8, 4)", "(6, 2)"],
                "answer": 0,
                "solution_steps": [
                    "From x − y = 4, express x = y + 4.",
                    "Substitute into 2x + y = 17: 2(y + 4) + y = 17 ⇒ 3y + 8 = 17 ⇒ y = 3.",
                    "Back-substitute: x = 3 + 4 = 7, giving (7, 3).",
                ],
            },
            {
                "question": "Solve using Elimination: 3x + 4y = 18 and 3x − 2y = 6.",
                "options": ["(10/3, 2)", "(2, 3)", "(4, 3)", "(6, 0)"],
                "answer": 0,
                "solution_steps": [
                    "Subtract the second equation from the first to eliminate 3x: (3x + 4y) − (3x − 2y) = 18 − 6.",
                    "6y = 12 ⇒ y = 2.",
                    "Substitute y = 2 into 3x − 4 = 6 ⇒ 3x = 10 ⇒ x = 10/3.",
                ],
            },
            {
                "question": "How many solutions does the system 3x − 2y = 5 and 6x − 4y = 10 have?",
                "options": [
                    "Infinitely many solutions",
                    "Unique solution",
                    "No solution",
                    "Exactly two solutions",
                ],
                "answer": 0,
                "solution_steps": [
                    "Compare ratios: a₁/a₂ = 3/6 = 1/2, b₁/b₂ = (−2)/(−4) = 1/2, c₁/c₂ = 5/10 = 1/2.",
                    "All three ratios are equal: a₁/a₂ = b₁/b₂ = c₁/c₂.",
                    "Therefore the system has infinitely many solutions.",
                ],
            },
            {
                "question": "Classify the system 5x + 2y = 9 and 10x + 4y = 15 without solving.",
                "options": [
                    "No solution (parallel lines)",
                    "Unique solution",
                    "Infinitely many solutions",
                    "Coincident lines",
                ],
                "answer": 0,
                "solution_steps": [
                    "Compare ratios: a₁/a₂ = 5/10 = 1/2 and b₁/b₂ = 2/4 = 1/2.",
                    "Compare c₁/c₂ = 9/15 = 3/5 ≠ 1/2.",
                    "Since a₁/a₂ = b₁/b₂ ≠ c₁/c₂, there is no solution.",
                ],
            },
            {
                "question": "For what value of p will px + 3y = 7 and 4x + 6y = 14 have a UNIQUE solution?",
                "options": [
                    "Any p ≠ 2",
                    "Only p = 2",
                    "Only p = 0",
                    "Only p = 4",
                ],
                "answer": 0,
                "solution_steps": [
                    "Unique solution requires a₁/a₂ ≠ b₁/b₂.",
                    "Set p/4 ≠ 3/6 = 1/2.",
                    "Solving gives p ≠ 2.",
                ],
            },
            {
                "question": "3 chairs and 2 tables cost ₹1850; 5 chairs and 3 tables cost ₹2850. Find the cost of 1 chair and 1 table.",
                "options": [
                    "Chair ₹150, Table ₹700",
                    "Chair ₹200, Table ₹600",
                    "Chair ₹250, Table ₹550",
                    "Chair ₹100, Table ₹775",
                ],
                "answer": 0,
                "solution_steps": [
                    "Multiply 3c + 2t = 1850 by 3 → 9c + 6t = 5550; multiply 5c + 3t = 2850 by 2 → 10c + 6t = 5700.",
                    "Subtracting gives c = 150.",
                    "Then 3(150) + 2t = 1850 ⇒ 2t = 1400 ⇒ t = 700.",
                ],
            },
            {
                "question": "What historical Chinese text introduced 'fangcheng' counting-rod matrix elimination?",
                "options": [
                    "The Nine Chapters on the Mathematical Art",
                    "Elements",
                    "Principia Mathematica",
                    "Sulbasutras",
                ],
                "answer": 0,
                "solution_steps": [
                    "Han Dynasty mathematicians compiled 'The Nine Chapters on the Mathematical Art'.",
                    "Chapter 8 presented 'fangcheng' using counting rods in rectangular arrays.",
                    "It anticipated modern Gaussian elimination by ~1,800 years.",
                ],
            },
            {
                "question": "Which ancient civilisation recorded linear system word problems on clay tablets around 2000 BCE?",
                "options": ["Babylonian", "Roman", "Victorian", "Mayan"],
                "answer": 0,
                "solution_steps": [
                    "Old Babylonian clay tablets (c. 2000 BCE) preserve two-unknown field and silver problems.",
                    "They solved them using systematic verbal balancing steps.",
                    "These are among the earliest recorded linear systems in history.",
                ],
            },
            {
                "question": "If 2x + 3y = 15 and 5x − 3y = 6, what is x + y?",
                "options": ["6", "5", "7", "8"],
                "answer": 0,
                "solution_steps": [
                    "Add both equations: 7x = 21 ⇒ x = 3.",
                    "Substitute x = 3 into 2(3) + 3y = 15 ⇒ 3y = 9 ⇒ y = 3.",
                    "Therefore x + y = 3 + 3 = 6.",
                ],
            },
            {
                "question": "Solve: x + y = 10 and x − y = 2. What is the product xy?",
                "options": ["24", "20", "16", "12"],
                "answer": 0,
                "solution_steps": [
                    "Add the equations: 2x = 12 ⇒ x = 6.",
                    "Subtract to get y = 4.",
                    "Product xy = 6 × 4 = 24.",
                ],
            },
        ],
    },
    {
        "id": 20,
        "title": "Graphical Applications Quiz",
        "subtitle": "Mastery Quiz 4 (Silent Exercise): Graphical Intersection & Word Problems (13.6 & Exercises)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Two lines graphed on a Cartesian plane intersect at the single point (4, −1). What does this represent?",
                "options": [
                    "A unique solution x = 4, y = −1",
                    "No solution",
                    "Infinitely many solutions",
                    "Two separate solutions",
                ],
                "answer": 0,
                "solution_steps": [
                    "An intersection point lies on both lines simultaneously.",
                    "Its coordinates satisfy both linear equations.",
                    "Two distinct non-parallel lines meet at a single unique point (4, −1).",
                ],
            },
            {
                "question": "When plotting x + 2y = 6 and 2x + 4y = 10 on the same axes, what will the two lines look like?",
                "options": [
                    "Parallel lines that never intersect",
                    "Intersecting lines at (2, 2)",
                    "Coincident overlapping lines",
                    "Perpendicular lines",
                ],
                "answer": 0,
                "solution_steps": [
                    "Check ratios: 1/2 = 2/4 ≠ 6/10.",
                    "Equal slopes (−1/2) with different y-intercepts (3 vs 2.5).",
                    "Thus the lines are parallel and never intersect.",
                ],
            },
            {
                "question": "A wheelchair ramp must have slope ≤ 1/12. What is the maximum vertical height a 9.6 m horizontal ramp can safely climb?",
                "options": ["0.8 m", "1.2 m", "0.5 m", "1.5 m"],
                "answer": 0,
                "solution_steps": [
                    "Use Rise = Slope × Run.",
                    "Rise = (1/12) × 9.6 = 0.8 m.",
                    "Any higher rise would exceed the 1:12 gradient safety limit.",
                ],
            },
            {
                "question": "Convert 25°C to Fahrenheit using F = (9/5)C + 32.",
                "options": ["77°F", "68°F", "82°F", "57°F"],
                "answer": 0,
                "solution_steps": [
                    "Substitute C = 25 into F = (9/5)C + 32.",
                    "F = (9/5)(25) + 32 = 45 + 32.",
                    "F = 77°F.",
                ],
            },
            {
                "question": "Plan X costs ₹150 + ₹3/GB and Plan Y costs ₹50 + ₹5/GB. Above how many GB is Plan X cheaper than Plan Y?",
                "options": ["50 GB", "25 GB", "40 GB", "100 GB"],
                "answer": 0,
                "solution_steps": [
                    "Find the break-even point: 150 + 3x = 50 + 5x.",
                    "100 = 2x ⇒ x = 50 GB.",
                    "Because Plan X has a lower per-GB slope (3 < 5), it is cheaper for x > 50 GB.",
                ],
            },
            {
                "question": "In a cyclic quadrilateral, opposite angles are (3x + 10)° and (x + 50)°. Find x.",
                "options": ["30°", "40°", "20°", "45°"],
                "answer": 0,
                "solution_steps": [
                    "Opposite angles of a cyclic quadrilateral sum to 180°.",
                    "(3x + 10) + (x + 50) = 180 ⇒ 4x + 60 = 180.",
                    "4x = 120 ⇒ x = 30°.",
                ],
            },
            {
                "question": "Two cars 150 km apart meet in 1.5 hours moving toward each other (u + v = 100) and in 5 hours moving in the same direction (u − v = 30). Find u.",
                "options": ["65 km/h", "55 km/h", "70 km/h", "35 km/h"],
                "answer": 0,
                "solution_steps": [
                    "Add u + v = 100 and u − v = 30.",
                    "2u = 130.",
                    "u = 65 km/h (and v = 35 km/h).",
                ],
            },
            {
                "question": "In Mahāvīrāchārya's Gaṇita Sāra Saṅgraha puzzle (x + 100 = 2(y − 100) and y + 10 = 6(x − 10)), what are x and y?",
                "options": [
                    "x = 40, y = 170",
                    "x = 50, y = 150",
                    "x = 60, y = 180",
                    "x = 30, y = 160",
                ],
                "answer": 0,
                "solution_steps": [
                    "Simplify: x − 2y = −300 and 6x − y = 70.",
                    "Multiply second by 2: 12x − 2y = 140; subtract first: 11x = 440 ⇒ x = 40.",
                    "Then y = 6(40) − 70 = 170.",
                ],
            },
            {
                "question": "What is the area of the triangle bounded by the line 2x + 3y = 12 and the two coordinate axes?",
                "options": ["12 sq units", "24 sq units", "6 sq units", "10 sq units"],
                "answer": 0,
                "solution_steps": [
                    "x-intercept (y = 0): 2x = 12 ⇒ x = 6.",
                    "y-intercept (x = 0): 3y = 12 ⇒ y = 4.",
                    "Right triangle area = ½ × base × height = ½ × 6 × 4 = 12 sq units.",
                ],
            },
            {
                "question": "Which summary statement accurately captures Chapter 13 (Two Variables, One Line)?",
                "options": [
                    "Linear equations ax + by + c = 0 represent straight lines whose intersections, slopes, and ratios unify algebra and geometry",
                    "Every linear equation has only one solution",
                    "Parallel lines always intersect at (0, 0)",
                    "Vertical lines have slope 0",
                ],
                "answer": 0,
                "solution_steps": [
                    "Standard form ax + by + c = 0 maps to lines with slope −a/b and y-intercept −c/b.",
                    "Systems of two lines classify cleanly by coefficient ratios into unique, infinite, or no solution.",
                    "Substitution, elimination, and graphing solve real-world modeling problems.",
                ],
            },
        ],
    },
]

for _s in slides_part3:
    for _q in _s["questions"]:
        _q.setdefault("hint", _q["solution_steps"][0])
        _q.setdefault("explanation", _q["solution_steps"][-1])

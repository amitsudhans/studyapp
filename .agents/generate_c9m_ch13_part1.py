#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 13: Two Variables, One Line
Part 1: Slides 1 to 8 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Linear Equation Modeling",
        "subtitle": "Section 13.1 Linear Equations in Two Variables: Real-World Algebraic Modeling",
        "speech": (
            "Welcome to Chapter Thirteen: Two Variables, One Line! Until now, you solved equations with a single unknown "
            "like two x plus five equals eleven, which pins down one exact number! Yet real life constantly pairs two "
            "independent quantities together inside Section Thirteen Point One! "
            "Imagine visiting a fruit market with two hundred eighty rupees! Apples cost sixty rupees per kilogram and "
            "oranges cost fifty rupees per kilogram! If you buy x kilograms of apples and y kilograms of oranges, the "
            "total bill becomes sixty x plus fifty y equals two hundred eighty! Notice two distinct variables, x and y, "
            "each raised strictly to the first power with no x-squared, no y-cubed, and no x-times-y product! "
            "That makes sixty x plus fifty y equals two hundred eighty a LINEAR EQUATION IN TWO VARIABLES! Why is it "
            "called linear? Because when you plot every valid combination of apples and oranges—such as three kilograms "
            "of apples and two kilograms of oranges, or one kilogram of apples and four point four kilograms of oranges—all "
            "solution points align along one straight geometric line! Modeling budgets, speeds, mixtures, and temperatures "
            "with two unknowns opens the doorway to coordinate geometry and simultaneous systems!"
        ),
        "checkpoints": [
            {
                "question": "If notebooks cost ₹40 each and pens cost ₹15 each, which equation models spending ₹250 on x notebooks and y pens?",
                "options": [
                    "40x + 15y = 250",
                    "40x² + 15y = 250",
                    "40xy = 250",
                    "x + y = 250",
                ],
                "answer": 0,
                "hint": "Multiply each unit price by its quantity and add them to equal the total budget!",
                "explanation": "Cost of x notebooks is 40x and y pens is 15y, giving the linear equation 40x + 15y = 250.",
            },
            {
                "question": "Which of the following is a valid linear equation in two variables?",
                "options": [
                    "3x + 4y = 12",
                    "3x² + 4y = 12",
                    "3xy + 4 = 12",
                    "3/x + 4y = 12",
                ],
                "answer": 0,
                "hint": "Both variables must appear strictly to degree 1 with no products like xy!",
                "explanation": "In 3x + 4y = 12, both x and y have exponent 1 and are not multiplied together.",
            },
        ],
    },
    {
        "id": 2,
        "title": "Standard Equation Form",
        "subtitle": "Section 13.1.1 Standard Form of Linear Equations: ax + by + c = 0",
        "speech": (
            "Now master the universal blueprint inside Section Thirteen Point One Point One: THE STANDARD FORM OF A "
            "LINEAR EQUATION IN TWO VARIABLES! Every linear equation in x and y can be written cleanly as a x plus b y "
            "plus c equals zero, where a, b, and c are real numbers, AND a and b are NOT both zero simultaneously! "
            "Why must we forbid a and b both being zero? Because if a equals zero and b equals zero, both variables "
            "vanish, leaving a false or trivial statement like c equals zero! "
            "Watch two essential conversions! First, suppose you have fractional coefficients like x over two minus y "
            "over three equals five! Multiply the entire equation by the least common multiple six to clear fractions, "
            "then shift everything to the left: three x minus two y minus thirty equals zero, giving integers a equals "
            "three, b equals minus two, and c equals minus thirty! "
            "Second, what about a single-variable equation like x equals four? Write it in two-variable standard form by "
            "inserting zero times y: one x plus zero y minus four equals zero! Similarly, y equals minus seven becomes "
            "zero x plus one y plus seven equals zero—keeping our algebraic format completely uniform!"
        ),
        "checkpoints": [
            {
                "question": "In the standard form ax + by + c = 0 of the equation 2y = 5x − 9, what are (a, b, c)?",
                "options": [
                    "(5, −2, −9)",
                    "(2, 5, −9)",
                    "(5, 2, 9)",
                    "(−5, −2, 9)",
                ],
                "answer": 0,
                "hint": "Move 2y to the right side (or everything to the left) so all terms equal 0!",
                "explanation": "5x − 2y − 9 = 0 gives a = 5, b = −2, c = −9 (or equivalently −5x + 2y + 9 = 0).",
            },
            {
                "question": "How is the single-variable equation 3x = 12 written in standard two-variable form ax + by + c = 0?",
                "options": [
                    "3x + 0y − 12 = 0",
                    "3x + 1y − 12 = 0",
                    "0x + 3y − 12 = 0",
                    "3x + 12y = 0",
                ],
                "answer": 0,
                "hint": "The missing variable y gets a coefficient of 0!",
                "explanation": "3x = 12 becomes 3x + 0y − 12 = 0 with a = 3, b = 0, c = −12.",
            },
        ],
    },
    {
        "id": 3,
        "title": "Ordered Pair Solutions",
        "subtitle": "Section 13.2 & 13.2.1 Algebraic Meaning of Solution: Infinitely Many Ordered Pairs",
        "speech": (
            "Now turn to Section Thirteen Point Two: SOLUTIONS OF A LINEAR EQUATION IN TWO VARIABLES! Unlike a single-"
            "variable equation with just one answer, a two-variable equation like two x plus y equals eight has an "
            "INFINITE family of solutions! What does a solution look like? It is an ORDERED PAIR (x, y) whose x-value "
            "and y-value make the left-hand side equal the right-hand side simultaneously! "
            "Notice the word ORDERED! Swapping the two numbers matters! Test (2, 4) in two x plus y equals eight: two "
            "times two plus four equals eight—TRUE! Now swap them to (4, 2): two times four plus two equals ten, NOT "
            "eight—FALSE! "
            "How do we systematically generate as many solutions as we wish inside Section Thirteen Point Two Point One? "
            "Pick ANY real number you like for x, substitute it into the equation, and solve the remaining one-variable "
            "equation for y! Take x equals zero: y equals eight, giving (0, 8)! Take x equals one: y equals six, giving "
            "(1, 6)! Take x equals five: y equals minus two, giving (5, −2)! Since x can be chosen from infinitely many "
            "real numbers—integers, fractions, or decimals—EVERY linear equation in two variables possesses infinitely "
            "many ordered-pair solutions!"
        ),
        "checkpoints": [
            {
                "question": "Which ordered pair (x, y) is a solution of 3x − 2y = 7?",
                "options": ["(3, 1)", "(1, 3)", "(2, 1)", "(0, 7)"],
                "answer": 0,
                "hint": "Substitute x and y into 3x − 2y and check which pair equals 7!",
                "explanation": "For (3, 1): 3(3) − 2(1) = 9 − 2 = 7, which satisfies the equation.",
            },
            {
                "question": "How many solutions does the linear equation 5x + 2y = 10 have?",
                "options": [
                    "Infinitely many solutions",
                    "Exactly one solution",
                    "Exactly two solutions",
                    "No solution",
                ],
                "answer": 0,
                "hint": "Every real value chosen for x produces a corresponding real value for y!",
                "explanation": "Because y = (10 − 5x)/2 yields a unique y for every real x, there are infinitely many solutions.",
            },
        ],
    },
    {
        "id": 4,
        "title": "Graphing Linear Solutions",
        "subtitle": "Section 13.2.2 Geometric Visualisation: Plotting Lines & X/Y-Intercepts",
        "speech": (
            "Now bridge algebra to geometry inside Section Thirteen Point Two Point Two: GEOMETRIC VISUALISATION OF "
            "SOLUTIONS! Take three or four ordered-pair solutions of two x plus y equals six—say (0, 6), (1, 4), (2, 2), "
            "and (3, 0)—and plot them as points on the Cartesian coordinate plane! Lay a straightedge across those dots: "
            "EVERY SINGLE SOLUTION LIES ON ONE CONTINUOUS STRAIGHT LINE! "
            "Conversely, pick ANY arbitrary point sitting on that drawn line, read its coordinates (x, y)—even fractional "
            "points like (1.5, 3)—and substitute them back into two x plus y equals six: it satisfies the equation "
            "perfectly! Points OFF the line fail the equation! "
            "To sketch any line rapidly without tedious arithmetic, use the TWO-INTERCEPT SHORTCUT! First, set y equals "
            "zero to find the X-INTERCEPT—where the line crosses the horizontal x-axis! For two x plus three y equals "
            "twelve, setting y equals zero gives two x equals twelve, so x equals six, marking (6, 0)! Second, set x "
            "equals zero to find the Y-INTERCEPT—where the line crosses the vertical y-axis! Setting x equals zero "
            "gives three y equals twelve, so y equals four, marking (0, 4)! Connect (6, 0) and (0, 4) with a ruler—done!"
        ),
        "checkpoints": [
            {
                "question": "What are the x-intercept and y-intercept of the line 4x + 5y = 20?",
                "options": [
                    "x-intercept (5, 0) and y-intercept (0, 4)",
                    "x-intercept (4, 0) and y-intercept (0, 5)",
                    "x-intercept (20, 0) and y-intercept (0, 20)",
                    "x-intercept (0, 5) and y-intercept (4, 0)",
                ],
                "answer": 0,
                "hint": "Set y = 0 to get the x-intercept, and set x = 0 to get the y-intercept!",
                "explanation": "4x = 20 ⇒ x = 5 gives (5, 0); 5y = 20 ⇒ y = 4 gives (0, 4).",
            },
            {
                "question": "If the point (k, 5) lies on the line 2x + 3y = 19, what is the value of k?",
                "options": ["2", "3", "4", "7"],
                "answer": 0,
                "hint": "Any point on the line must satisfy the equation—substitute x = k and y = 5!",
                "explanation": "2k + 3(5) = 19 ⇒ 2k + 15 = 19 ⇒ 2k = 4 ⇒ k = 2.",
            },
        ],
    },
    {
        "id": 5,
        "title": "Rise Over Run",
        "subtitle": "Section 13.3.1 Understanding Slope: Rise/Run, Positive, Negative, Zero & Undefined",
        "speech": (
            "Welcome to Section Thirteen Point Three Point One: UNDERSTANDING SLOPE! Why do some lines climb steeply "
            "like a mountain trail while others glide gently or plunge downward? We measure steepness with a single "
            "number called SLOPE, denoted by the letter m! "
            "Pick ANY two distinct points (x one, y one) and (x two, y two) on a straight line! Slope m equals RISE "
            "divided by RUN: the vertical change (y two minus y one) divided by the horizontal change (x two minus x "
            "one)! Because similar right triangles along a straight line share the same ratio, slope m stays completely "
            "CONSTANT everywhere along that line! "
            "Classify all four slope types! First, POSITIVE SLOPE (m greater than zero): the line rises upward from "
            "left to right, and larger m means steeper climb! Second, NEGATIVE SLOPE (m less than zero): the line "
            "falls downward from left to right! Third, ZERO SLOPE (m equals zero): y two minus y one is zero, giving a "
            "perfectly HORIZONTAL line like y equals five! Fourth, UNDEFINED SLOPE: x two minus x one is zero—meaning "
            "division by zero—giving a perfectly VERTICAL line like x equals three, pointing straight up and down vertically!"
        ),
        "checkpoints": [
            {
                "question": "What is the slope m of the straight line passing through (2, 3) and (6, 11)?",
                "options": ["2", "½", "4", "8"],
                "answer": 0,
                "hint": "Compute Rise / Run = (y₂ − y₁) / (x₂ − x₁)!",
                "explanation": "m = (11 − 3) / (6 − 2) = 8 / 4 = 2.",
            },
            {
                "question": "What is the slope of a horizontal line (such as y = 7) and a vertical line (such as x = 4)?",
                "options": [
                    "Horizontal has slope 0; vertical has undefined slope",
                    "Horizontal has undefined slope; vertical has slope 0",
                    "Both have slope 1",
                    "Horizontal has slope 7; vertical has slope 4",
                ],
                "answer": 0,
                "hint": "Horizontal lines have Rise = 0; vertical lines have Run = 0 (division by zero)!",
                "explanation": "Rise = 0 gives m = 0 for horizontal lines; Run = 0 gives division by zero (undefined) for vertical lines.",
            },
        ],
    },
    {
        "id": 6,
        "title": "Slope Intercept Form",
        "subtitle": "Section 13.3.2 Slope-Intercept Form: Deriving y = mx + d from ax + by + c = 0",
        "speech": (
            "Now connect standard form directly to slope inside Section Thirteen Point Three Point Two: THE SLOPE-"
            "INTERCEPT FORM y equals m x plus d! Start with any non-vertical line in standard form: a x plus b y plus "
            "c equals zero, where b is not zero! Solve algebraically for y! Subtract a x and c from both sides: b y "
            "equals minus a x minus c! Now divide every term by b: y equals (minus a over b) times x plus (minus c "
            "over b)! "
            "Compare this directly with y equals m x plus d! Immediately we prove TWO golden formulas! First, the "
            "coefficient of x is the SLOPE m equals minus a over b! Second, the constant term is the Y-INTERCEPT d "
            "equals minus c over b—because setting x equals zero leaves y equals d! "
            "Test this on three x plus two y minus eight equals zero! Here a equals three, b equals two, c equals minus "
            "eight! Instantly, slope m equals minus three over two (falling downward), and y-intercept d equals minus "
            "of minus eight over two, which is positive four! Whenever two lines share the exact same slope m with "
            "different intercepts d, they are strictly PARALLEL!"
        ),
        "checkpoints": [
            {
                "question": "For the line 6x − 2y + 10 = 0, what are the slope m and y-intercept d when written as y = mx + d?",
                "options": [
                    "m = 3, d = 5",
                    "m = −3, d = −5",
                    "m = 6, d = 10",
                    "m = 1/3, d = 5",
                ],
                "answer": 0,
                "hint": "Solve 6x − 2y + 10 = 0 for y (or use m = −a/b and d = −c/b)!",
                "explanation": "2y = 6x + 10 ⇒ y = 3x + 5, so slope m = 3 and y-intercept d = 5.",
            },
            {
                "question": "What geometric relationship holds between the lines y = 4x − 1 and y = 4x + 7?",
                "options": [
                    "They are strictly parallel (same slope m = 4, different y-intercepts)",
                    "They are perpendicular",
                    "They intersect at (0, 4)",
                    "They are identical coincident lines",
                ],
                "answer": 0,
                "hint": "Compare their slopes m₁ and m₂ and their y-intercepts d₁ and d₂!",
                "explanation": "Equal slopes (4 = 4) with unequal y-intercepts (−1 ≠ 7) produce parallel lines that never meet.",
            },
        ],
    },
    {
        "id": 7,
        "title": "Simultaneous Linear Systems",
        "subtitle": "Section 13.4 Pair of Linear Equations in Two Variables: Formulating Systems",
        "speech": (
            "Until Slide Six, one equation in two variables gave infinitely many solutions along a line! What happens "
            "when TWO conditions apply to the SAME two unknowns simultaneously? Welcome to Section Thirteen Point Four: "
            "PAIR OF LINEAR EQUATIONS IN TWO VARIABLES! "
            "A system consists of two linear equations in x and y: a one x plus b one y plus c one equals zero, AND "
            "a two x plus b two y plus c two equals zero! Let us formulate three classic real-world systems! "
            "First, TICKET SALES: three adult tickets and two child tickets cost five hundred rupees, while two adult "
            "tickets and five child tickets cost four hundred eighty rupees! That yields three x plus two y equals five "
            "hundred, and two x plus five y equals four hundred eighty! "
            "Second, TAXI FARES: a fixed flag-down charge F plus r rupees per kilometre gives F plus ten r equals one "
            "hundred five, and F plus fifteen r equals one hundred fifty-five! "
            "Third, NUMBER PUZZLES: two numbers sum to thirty-six and their difference is twelve, giving x plus y equals "
            "thirty-six and x minus y equals twelve! Solving both equations together pins down the exact shared (x, y)!"
        ),
        "checkpoints": [
            {
                "question": "Two numbers sum to 50 and their difference is 14. Which pair of equations models this system (x > y)?",
                "options": [
                    "x + y = 50 and x − y = 14",
                    "x + y = 14 and x − y = 50",
                    "xy = 50 and x/y = 14",
                    "2x + y = 50 and x − 2y = 14",
                ],
                "answer": 0,
                "hint": "Translate 'sum' as x + y and 'difference' as x − y!",
                "explanation": "The two conditions directly give x + y = 50 and x − y = 14.",
            },
            {
                "question": "A taxi charges a fixed fee F plus ₹r per km. A 5 km ride costs ₹65 and an 8 km ride costs ₹95. Which system models this?",
                "options": [
                    "F + 5r = 65 and F + 8r = 95",
                    "5F + r = 65 and 8F + r = 95",
                    "F + r = 65 and F + r = 95",
                    "5F + 8r = 160",
                ],
                "answer": 0,
                "hint": "Total fare = fixed charge F + (distance × rate r)!",
                "explanation": "For 5 km: F + 5r = 65; for 8 km: F + 8r = 95.",
            },
        ],
    },
    {
        "id": 8,
        "title": "Substitution Solving Method",
        "subtitle": "Section 13.5.1 Algebraic Methods: Step-by-Step Substitution Method",
        "speech": (
            "Now solve simultaneous systems algebraically inside Section Thirteen Point Five Point One! Method One is "
            "THE SUBSTITUTION METHOD—ideal whenever one variable already has coefficient one or minus one! "
            "Follow our crisp four-step recipe on a real system: Equation One is x plus y equals fourteen, and Equation "
            "Two is three x minus two y equals twelve! "
            "Step One: Isolate one variable from the simpler equation! From Equation One, subtract y to express x in "
            "terms of y: x equals fourteen minus y! "
            "Step Two: SUBSTITUTE that expression (fourteen minus y) in place of x inside the OTHER equation! Equation "
            "Two transforms into three times (fourteen minus y) minus two y equals twelve! Notice x has vanished, "
            "leaving a single-variable equation in y! "
            "Step Three: Expand and solve for y! Forty-two minus three y minus two y equals twelve gives forty-two "
            "minus five y equals twelve, so five y equals thirty, yielding y equals six! "
            "Step Four: Back-substitute y equals six into x equals fourteen minus y to get x equals eight! Always "
            "verify (8, 6) in BOTH original equations: eight plus six is fourteen, and twenty-four minus twelve is twelve—confirming our exact unique solution pair!"
        ),
        "checkpoints": [
            {
                "question": "Solve by substitution: y = 2x and 3x + y = 25. What is the ordered pair (x, y)?",
                "options": ["(5, 10)", "(10, 5)", "(4, 8)", "(6, 12)"],
                "answer": 0,
                "hint": "Substitute y = 2x directly into 3x + y = 25!",
                "explanation": "3x + 2x = 25 ⇒ 5x = 25 ⇒ x = 5, and y = 2(5) = 10.",
            },
            {
                "question": "In Step 2 of the Substitution Method, why must you substitute into the OTHER equation rather than back into the same equation?",
                "options": [
                    "Substituting back into the same equation produces an identity (0 = 0) and eliminates nothing",
                    "Because the other equation has bigger numbers",
                    "To change the slope",
                    "Because y always equals 0",
                ],
                "answer": 0,
                "hint": "Try plugging x = 14 − y back into x + y = 14 to see what happens!",
                "explanation": "Substituting into the same equation gives 14 − y + y = 14 (14 = 14), using only one constraint instead of both.",
            },
        ],
    },
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 2: Introduction to Linear Polynomials
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 2.4 Linear Decay, 2.5 Linear Relationships, 2.6 Visualising Linear Relationships,
Exercises & Chapter Summary with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Linear Decay Models",
        "subtitle": "Section 2.4 Linear Decay: Negative Rate Parameters (h(t) = 3 - 0.5t), Depreciation, Population & Prepaid Balance",
        "speech": (
            "Now reverse the sign of the rate parameter to explore LINEAR DECAY in Section Two Point Four! "
            "Whenever a quantity drops by a fixed constant amount over equal intervals, the model carries a NEGATIVE rate a less than zero! "
            "Test four vivid real-world decay models! First, a tall candle measuring three decimetres melts uniformly at zero point five decimetres per hour: h of t equals three minus zero point five t! At t equals zero, height is three; after two hours, height drops to two; at t equals six hours, the candle reaches zero and finishes burning! "
            "Second, VEHICLE ASSET DEPRECIATION: a scooter bought for eighty thousand rupees loses six thousand rupees of value yearly, modeled as V of t equals eighty thousand minus six thousand t! "
            "Third, VILLAGE POPULATION CHANGE: a rural hamlet of four thousand residents losing forty residents annually follows P of t equals four thousand minus forty t! "
            "Fourth, PREPAID PHONE BALANCE: starting with two hundred rupees and deducting five rupees per call minute follows B of m equals two hundred minus five m! "
            "Always verify physical limits carefully: once height, asset value, population, or phone balance hits zero, negative outputs lose physical meaning in practical decay models!"
        ),
        "checkpoints": [
            {
                "question": "For candle height h(t) = 3 - 0.5t (in decimetres after t hours), after how many hours does the candle completely burn down (h = 0)?",
                "options": [
                    "6 hours",
                    "3 hours",
                    "1.5 hours",
                    "5 hours"
                ],
                "answer": 0,
                "hint": "Set 3 - 0.5t = 0 and solve for t!",
                "explanation": "0.5t = 3 ⇒ t = 3 / 0.5 = 6 hours."
            },
            {
                "question": "A prepaid SIM balance starts at ₹250 and drops by ₹4 per minute of talk time. What remains after 35 minutes?",
                "options": [
                    "₹110",
                    "₹140",
                    "₹90",
                    "₹190"
                ],
                "answer": 0,
                "hint": "Evaluate B(35) = 250 - 4(35)!",
                "explanation": "B(35) = 250 - 140 = ₹110."
            }
        ]
    },
    {
        "id": 10,
        "title": "Formulating Linear Equations",
        "subtitle": "Section 2.5 Linear Relationships: Formulating y = ax + b from Experimental Data Points & Algebraic Equation Solving",
        "speech": (
            "In real experiments and business plans, nobody hands you the formula y equals a x plus b up front—you recover the hidden rate a and baseline b directly from observed data pairs! "
            "Welcome to Section Two Point Five: Linear Relationships! Suppose you observe two clean measurements: open-parenthesis x-one comma y-one close-parenthesis and open-parenthesis x-two comma y-two close-parenthesis! "
            "Follow a foolproof two-stage algebraic solver! Stage One: plug BOTH data pairs into y equals a x plus b to create two simultaneous linear equations: y-one equals a x-one plus b, and y-two equals a x-two plus b! "
            "Notice that subtracting Equation One from Equation Two completely eliminates the unknown baseline b! Why? Because b minus b equals zero! "
            "That leaves y-two minus y-one equals a times open x-two minus x-one close, instantly yielding exact rate a equals open y-two minus y-one close divided by open x-two minus x-one close! "
            "Stage Two: substitute your newly solved rate a back into either original linear equation to unlock the exact fixed baseline value b cleanly! Always verify your completed linear equation against a third independent experimental data pair to confirm exact straight-line linear fit across the entire observed numerical dataset!"
        ),
        "checkpoints": [
            {
                "question": "A linear relationship passes through (2, 11) and (5, 23). What are the rate constant a and baseline b in y = ax + b?",
                "options": [
                    "a = 4 and b = 3 (equation y = 4x + 3)",
                    "a = 3 and b = 4",
                    "a = 12 and b = 1",
                    "a = 4 and b = -3"
                ],
                "answer": 0,
                "hint": "First compute a = (23 - 11)/(5 - 2), then solve 11 = a(2) + b!",
                "explanation": "a = 12 / 3 = 4; substituting (2, 11) gives 11 = 4(2) + b ⇒ b = 3 → y = 4x + 3."
            },
            {
                "question": "Why does subtracting y₁ = ax₁ + b from y₂ = ax₂ + b immediately isolate the unknown rate a?",
                "options": [
                    "Because the baseline constant b cancels out cleanly (b - b = 0)",
                    "Because x₁ and x₂ cancel out",
                    "Because y₁ becomes zero",
                    "Because a always equals 1"
                ],
                "answer": 0,
                "hint": "Look at what happens to +b when you subtract the two equations!",
                "explanation": "Subtracting (ax₁ + b) from (ax₂ + b) eliminates b, yielding y₂ - y₁ = a(x₂ - x₁)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Pricing and Temperature",
        "subtitle": "Section 2.5 Algebraic Solvers: Solving (a, b) in Telecom Plans, Learning Modules, Gym Rentals & °C to °F Conversions",
        "speech": (
            "Apply that exact simultaneous-equation solver to four classic scenarios in Section Two Point Five! "
            "First, TELECOM DATA PLANS: suppose a ten-gigabyte plan bills four hundred fifty rupees and an eighteen-gigabyte plan bills six hundred ninety rupees! Subtracting gives eight extra gigabytes costing two hundred forty rupees, so rate a equals thirty rupees per gigabyte, and fixed monthly base fee b equals one hundred fifty rupees! "
            "Second, ONLINE LEARNING MODULES & GYM COURT RENTALS: if three hours of badminton court rental costs six hundred rupees and seven hours costs twelve hundred rupees, subtracting isolates hourly rate a equals one hundred fifty rupees and flat booking deposit b equals one hundred fifty rupees! "
            "Third, TEMPERATURE SCALE CONVERSION between Celsius C and Fahrenheit F! Anchor two exact physical benchmarks: water freezes at zero Celsius equals thirty-two Fahrenheit, and boils at one hundred Celsius equals two hundred twelve Fahrenheit! "
            "Rate a equals two hundred twelve minus thirty-two divided by one hundred, which simplifies cleanly to exact fraction nine-fifths! Baseline b equals thirty-two! Thus the complete linear equation formula F equals nine-fifths C plus thirty-two solves every single temperature scale conversion instantaneously from freezing point right up to boiling point!"
        ),
        "checkpoints": [
            {
                "question": "An online learning platform charges a fixed registration fee b plus a per-module fee a. 4 modules cost ₹1,100 and 9 modules cost ₹2,100. Find (a, b).",
                "options": [
                    "Per-module fee a = ₹200, registration fee b = ₹300",
                    "Per-module fee a = ₹300, registration fee b = ₹200",
                    "Per-module fee a = ₹250, registration fee b = ₹100",
                    "Per-module fee a = ₹100, registration fee b = ₹700"
                ],
                "answer": 0,
                "hint": "5 extra modules cost 2100 - 1100 = ₹1000, so find a = 1000 / 5!",
                "explanation": "a = (2100 - 1100)/(9 - 4) = 1000/5 = ₹200; then b = 1100 - 4(200) = ₹300."
            },
            {
                "question": "Using the linear temperature formula F = (9/5)C + 32, what Fahrenheit temperature equals 35 °C?",
                "options": [
                    "95 °F",
                    "67 °F",
                    "85 °F",
                    "103 °F"
                ],
                "answer": 0,
                "hint": "Compute (9/5) × 35 = 9 × 7 = 63, then add 32!",
                "explanation": "F = (9/5)(35) + 32 = 63 + 32 = 95 °F."
            }
        ]
    },
    {
        "id": 12,
        "title": "Graphing Straight Lines",
        "subtitle": "Section 2.6 Visualising Linear Relationships: Plotting Coordinates (x, ax + b) as Straight Lines on the Cartesian Plane",
        "speech": (
            "Now bridge Chapter One coordinates directly into Section Two Point Six: Visualising Linear Relationships! "
            "Every ordered pair open-parenthesis x comma y close-parenthesis satisfying y equals a x plus b corresponds to an exact dot on the two-dimensional Cartesian plane! "
            "Take y equals two x minus one! Build a quick coordinate table by choosing three comfortable values of x, such as zero, two, and negative one! "
            "At x equals zero, y is minus one, giving zero comma negative one. At x equals two, y is three, giving two comma three. At x equals minus one, y is minus three, giving negative one comma negative three! "
            "Plot all three points on graph paper and lay a straight ruler across them: EVERY point satisfying y equals two x minus one aligns perfectly along ONE infinite straight line! That geometric fact explains why degree-one polynomials are called LINEAR! "
            "Crucial verification test: how do you check whether a candidate coordinate point like four comma seven lies on that line? Substitute x equals four into two x minus one—if output matches seven, the point sits squarely on the line! Otherwise it lies strictly above or strictly below the plotted straight line!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following points lies directly on the graph of the linear equation y = 3x - 4?",
                "options": [
                    "(2, 2)",
                    "(2, 10)",
                    "(0, 4)",
                    "(-1, -1)"
                ],
                "answer": 0,
                "hint": "Substitute x into 3x - 4 and check whether the result matches y!",
                "explanation": "At x = 2, y = 3(2) - 4 = 6 - 4 = 2, so (2, 2) satisfies the equation and lies on the line."
            },
            {
                "question": "Why are degree-1 polynomials (ax + b) called 'linear' polynomials?",
                "options": [
                    "Because plotting all solution pairs (x, ax + b) forms an exact straight line on the Cartesian plane",
                    "Because they always pass through (1, 1)",
                    "Because their graphs curve into parabolas",
                    "Because they can only accept positive integers"
                ],
                "answer": 0,
                "hint": "Look at the root word 'line' inside 'linear'!",
                "explanation": "Constant rate of change ensures every plotted pair (x, y) aligns collinearly along a straight line."
            }
        ]
    },
    {
        "id": 13,
        "title": "Origin Lines Steepness",
        "subtitle": "Section 2.6 Origin-Passing Lines (y = ax): Slope Magnitude |a| Controls Steepness & Sign Connects Growth vs Decay",
        "speech": (
            "Before exploring general shifts, examine the cleanest family of lines: Origin-passing lines of form y equals a x, where baseline b equals zero! "
            "Whenever b is zero, plugging in x equals zero yields y equals zero—forcing EVERY line y equals a x to pass straight through Origin O zero comma zero! "
            "Now compare how changing the slope parameter a tilts the line around the Origin! "
            "First, compare POSITIVE magnitudes! Plot y equals x (forty-five-degree diagonal), y equals three x, and y equals zero point two five x! Notice that when magnitude a exceeds one (like a equals three), every step right climbs steeply upward—steeper than y equals x! Conversely, when magnitude a lies between zero and one (like one-fourth), the line rises gently, looking much flatter! "
            "Second, reverse the SIGN of a! Negative slopes such as y equals minus two x drop steeply downward from left to right—directly illustrating LINEAR DECAY! Positive slopes climb upward from left to right—illustrating LINEAR GROWTH! What about rate a equals zero? That special case produces the completely flat horizontal x-axis! "
            "Thus slope a encodes BOTH direction (growth versus decay) and exact geometric visual steepness cleanly around the Origin point!"
        ),
        "checkpoints": [
            {
                "question": "Among the four Origin-passing lines y = 4x, y = x, y = 0.2x, and y = -3x, which positive-slope line is STEEPEST and which is FLATTEST?",
                "options": [
                    "y = 4x is steepest (|a| = 4 > 1); y = 0.2x is flattest (|a| = 0.2 < 1)",
                    "y = 0.2x is steepest; y = 4x is flattest",
                    "y = x is steeper than y = 4x",
                    "All Origin-passing lines share the exact same steepness"
                ],
                "answer": 0,
                "hint": "Larger absolute value |a| produces greater vertical rise per unit horizontal step!",
                "explanation": "Greater |a| means faster vertical rise per 1-unit run: 4 > 1 > 0.2, so y = 4x is steepest and y = 0.2x is flattest."
            },
            {
                "question": "Which visual behaviour on a Cartesian graph signals linear decay rather than linear growth?",
                "options": [
                    "A negative slope (a < 0), sloping downward from left to right",
                    "A positive slope (a > 0), sloping upward from left to right",
                    "Passing through (0, 0) with a = 2",
                    "Having a positive y-intercept b > 0 with a = 1"
                ],
                "answer": 0,
                "hint": "When y drops as x moves rightward, is rate a positive or negative?",
                "explanation": "Negative slope a < 0 means y decreases as x increases—moving downward left-to-right, representing linear decay."
            }
        ]
    },
    {
        "id": 14,
        "title": "Slope and Intercept",
        "subtitle": "Section 2.6 Slope-Intercept Form (y = ax + b): Slope a, Vertical Intercept (0, b) & Parallel Lines Sharing Equal Slope",
        "speech": (
            "Now put slope and vertical shift together to unlock the complete geometric anatomy of y equals a x plus b! "
            "In y equals a x plus b, the coefficient a defines the line's SLOPE—measuring exact vertical rise or drop per one-unit step rightward! "
            "Meanwhile, the constant b defines the Y-INTERCEPT—the exact point zero comma b where the straight line slices across the vertical y-axis! "
            "Watch what happens geometrically when you hold slope a fixed—say a equals two—while sliding intercept b from zero to plus three and minus four! "
            "Plot y equals two x, y equals two x plus three, and y equals two x minus four together! "
            "Because every line climbs at the identical rate of two units up per one unit right, all three lines tilt at the exact same angle! Adding constant b merely slides the entire straight line vertically upward or downward without tilting its angle by even a tiny fraction of a single degree! "
            "Consequently, any distinct straight lines having identical constant slope a and distinctly different vertical y-intercepts b NEVER intersect anywhere in the coordinate plane—they always form perfectly PARALLEL STRAIGHT LINES stretching infinitely rightward and leftward across all four rectangular coordinate quadrants!"
        ),
        "checkpoints": [
            {
                "question": "Where does the straight line y = -5x + 7 intersect the vertical y-axis, and what is its slope?",
                "options": [
                    "y-intercept is (0, 7) and slope is a = -5",
                    "y-intercept is (7, 0) and slope is 7",
                    "y-intercept is (0, -5) and slope is 7",
                    "y-intercept is (0, 0) and slope is -5"
                ],
                "answer": 0,
                "hint": "Match y = ax + b carefully and plug in x = 0 to locate the y-axis intersection!",
                "explanation": "In y = -5x + 7, coefficient of x gives slope a = -5, and setting x = 0 gives y-intercept (0, 7)."
            },
            {
                "question": "Which pair of linear equations represents two distinct PARALLEL straight lines?",
                "options": [
                    "y = 3x + 2 and y = 3x - 5 (same slope a = 3, different intercepts)",
                    "y = 3x + 2 and y = 2x + 3 (different slopes)",
                    "y = 3x + 2 and y = -3x + 2 (opposite slopes, intersecting at (0, 2))",
                    "y = x and y = 4x (intersecting at Origin (0, 0))"
                ],
                "answer": 0,
                "hint": "Parallel lines share identical steepness (slope a) while crossing the y-axis at different heights b!",
                "explanation": "Both y = 3x + 2 and y = 3x - 5 have identical slope a = 3 with distinct y-intercepts 2 ≠ -5, so they never meet."
            }
        ]
    },
    {
        "id": 15,
        "title": "Applied Linear Graphs",
        "subtitle": "End-of-Chapter Exercises Preview: Matchstick Hexagons (5n+1), Graph Intersections, Work-Distance & Kelvin-Fahrenheit",
        "speech": (
            "Preview four clever end-of-chapter problems uniting patterns, physics, temperature conversions, and intersecting lines! "
            "First, MATCHSTICK HEXAGON PATTERNS: one standalone regular hexagon uses six matchsticks. Attach a second hexagon sharing one edge—it only needs FIVE extra sticks! Each new joined hexagon adds five sticks, producing six, eleven, sixteen, twenty-one—modeled cleanly by five n plus one matchsticks! "
            "Second, DIGIT-REVERSAL WORD PROBLEMS: remember any two-digit number ten t plus u minus its reverse ten u plus t equals nine times open t minus u close—a linear expression in the digit difference! "
            "Third, GRAPH INTERSECTION POINTS: suppose two telecom plans or two motion lines cross at one shared point—at their intersection, BOTH equations share the exact same x and y values! Equate their expressions and solve! "
            "Fourth, WORK-DISTANCE GRAPHS AND KELVIN-TO-FAHRENHEIT: physical mechanical work W equals constant applied force F times linear displacement distance d plots cleanly on Cartesian graph paper as a straight origin-passing line with constant slope F, while liquid temperature measured accurately in Kelvin scales converts linearly via F equals nine-fifths times open K minus two hundred seventy-three point one five close plus thirty-two—adding exactly one point eight Fahrenheit degrees for every single one Kelvin degree rise!"
        ),
        "checkpoints": [
            {
                "question": "If 1 joined matchstick hexagon uses 6 sticks, 2 joined hexagons use 11 sticks, and 3 use 16 sticks, how many matchsticks are required for 12 joined hexagons?",
                "options": [
                    "61 matchsticks (via 5n + 1)",
                    "72 matchsticks",
                    "60 matchsticks",
                    "56 matchsticks"
                ],
                "answer": 0,
                "hint": "Evaluate 5(12) + 1!",
                "explanation": "First hexagon uses 6 and each of the remaining 11 adds 5 sticks: 6 + 5(11) = 61 (or 5(12) + 1 = 61)."
            },
            {
                "question": "At what exact coordinate point do the two lines y = 2x + 1 and y = 5x - 8 intersect?",
                "options": [
                    "(3, 7)",
                    "(2, 5)",
                    "(3, 5)",
                    "(1, 3)"
                ],
                "answer": 0,
                "hint": "Set 2x + 1 = 5x - 8 to solve x, then substitute back for y!",
                "explanation": "2x + 1 = 5x - 8 ⇒ 9 = 3x ⇒ x = 3; then y = 2(3) + 1 = 7, giving intersection (3, 7)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary Matrix",
        "subtitle": "Chapter Summary: Univariate Polynomial Degrees, Linear Growth/Decay, Pattern Rules & Slope-Intercept Geometry (y = ax + b)",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your complete Chapter Summary Matrix for Introduction to Linear Polynomials! "
            "Connect every concept together cleanly! First, ALGEBRAIC MODELING & TERMINOLOGY: variables, terms, coefficients, and constants build univariate polynomials classified by highest non-zero whole-number exponent into Constant degree zero, Linear degree one, Quadratic degree two, and Cubic degree three! "
            "Second, LINEAR POLYNOMIALS & PATTERNS: degree-one functions y equals a x plus b (with a non-zero) model perimeters, fees, tile sequences like two n minus one, and matchstick hexagons five n plus one—always exhibiting constant successive differences equal to a! "
            "Third, LINEAR GROWTH & DECAY: positive rate a greater than zero drives steady growth such as C of d equals one hundred plus sixty d, whereas negative rate a less than zero drives linear decay like candle melting three minus zero point five t or depreciation! "
            "Fourth, SOLVERS & VISUALISATION: solving simultaneous data points recovers exact rate a and fixed baseline b, while Cartesian graphs reveal crisp straight lines with constant slope a, vertical y-intercept zero comma b, Origin-passing lines y equals a x, and parallel lines sharing equal slopes! Now test every algebraic and graphical skill cleanly across the four silent challenge quizzes ahead!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement accurately links algebra and geometry for linear relationships y = ax + b (a ≠ 0)?",
                "options": [
                    "Constant first difference equals a; Cartesian graph is a straight line with slope a crossing the y-axis at (0, b)",
                    "First differences grow quadratically; graph always passes through Origin (0, 0) even if b ≠ 0",
                    "Lines with different slopes a₁ ≠ a₂ are parallel",
                    "Negative rate a < 0 always models exponential growth"
                ],
                "answer": 0,
                "hint": "Check every piece: constant step a, y-axis crossing at x = 0, and straight-line geometry!",
                "explanation": "In y = ax + b, every +1 step in x changes y by exact constant a (slope), and x = 0 gives y-intercept (0, b)."
            },
            {
                "question": "Given two points (x₁, y₁) and (x₂, y₂) on a linear graph, which property identifies two lines as parallel rather than intersecting?",
                "options": [
                    "Equal slopes (a₁ = a₂) combined with distinct y-intercepts (b₁ ≠ b₂)",
                    "Equal y-intercepts (b₁ = b₂) with different slopes (a₁ ≠ a₂)",
                    "Equal constant terms only when x = 1",
                    "Opposite signs on slope (a₁ = -a₂)"
                ],
                "answer": 0,
                "hint": "Parallel lines climb or fall at the exact same steepness without sharing points!",
                "explanation": "Identical slope a₁ = a₂ keeps lines equally tilted, and b₁ ≠ b₂ shifts them apart vertically so they stay parallel."
            }
        ]
    }
]

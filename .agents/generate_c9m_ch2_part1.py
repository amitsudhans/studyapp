#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 2: Introduction to Linear Polynomials
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 2.1 Introduction, 2.2 Linear Polynomials, 2.3 Exploring Linear Patterns, 2.4 Linear Growth
with 1-3 word headings, 195-215 spoken words per slide, zero fictional human names/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Real Algebraic Modeling",
        "subtitle": "Section 2.1 Introduction: Counting Bundled Stationery, Rectangular Garden Fencing & Seed Costs, and Variable Area Expressions",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Two: Introduction to Linear Polynomials! "
            "Why do mathematicians replace everyday spoken sentences with compact algebraic letters like x, y, or z? "
            "Begin in Section Two Point One with practical counting and measurement problems! "
            "Suppose a school store sells notebooks packed in sealed bundles of ten plus loose single pens and pencils! If each bundle holds p pens and a box holds q pencils, then three bundles plus four loose pens gives the tidy expression three p plus four! "
            "Now inspect a rectangular garden whose length measures l metres and width measures five metres. Its perimeter requiring wire fencing equals two times l plus ten metres! Suppose fencing wire costs forty rupees per metre and grass seed costs fifteen rupees per square metre of area five l! "
            "Adding perimeter fencing cost plus interior area seed cost combines two geometric quantities into one single algebraic formula depending purely on the variable length l! "
            "Even if someone changes the garden's length tomorrow from six metres to twelve metres, you never rewrite the rule—simply substitute the new number! Algebraic modeling turns changing real-world counts, perimeters, fencing quotes, and grass-seed costs into reusable mathematical blueprints!"
        ),
        "checkpoints": [
            {
                "question": "If a stationery box holds p pens per bundle and a student buys 4 full bundles plus 7 loose pens, which expression represents the total pens?",
                "options": [
                    "4p + 7",
                    "7p + 4",
                    "11p",
                    "4p × 7"
                ],
                "answer": 0,
                "hint": "Multiply bundles (4) by pens per bundle (p), then add the 7 single pens!",
                "explanation": "Four bundles contain 4 × p = 4p pens, plus 7 loose pens yields 4p + 7."
            },
            {
                "question": "A rectangular garden has fixed width 6 m and variable length l m. If fencing costs ₹25 per metre and seed costs ₹10 per m², which expression represents total cost?",
                "options": [
                    "25(2l + 12) + 10(6l) = 110l + 300",
                    "25(6l) + 10(2l + 12)",
                    "35l + 6",
                    "2l + 12 + 6l"
                ],
                "answer": 0,
                "hint": "Perimeter = 2(l + 6) = 2l + 12 metres, and Area = 6l square metres; multiply each by its unit rate!",
                "explanation": "Fencing cost = 25(2l + 12) = 50l + 300, and seed cost = 10(6l) = 60l; summing gives 110l + 300."
            }
        ]
    },
    {
        "id": 2,
        "title": "Expression Key Terms",
        "subtitle": "Section 2.1 Key Terminology: Defining Terms, Variables, Coefficients & Constants in Univariate Algebraic Expressions",
        "speech": (
            "Before classifying families of expressions, master the four essential building blocks of every single-variable—or univariate—algebraic expression! "
            "Look at an expression such as five y cubed plus y squared plus two y minus one, or simply three z plus seven! "
            "First, identify the VARIABLE: a letter symbol like x, y, or z that can stand for different numerical values across situations. Notice our expressions here are univariate because each uses strictly ONE variable letter! "
            "Second, break the expression apart at addition and subtraction signs into individual TERMS! For instance, three z plus seven contains two terms: three z and seven; while five y cubed plus y squared plus two y minus one splits cleanly into four terms, carefully keeping the negative sign attached to minus one! "
            "Third, inspect each term's COEFFICIENT—the numerical factor multiplying the variable power! In minus four x plus nine, the coefficient of x is minus four, while in y squared the hidden coefficient is positive one! "
            "Fourth, spot the CONSTANT TERM—the standalone number with no variable attached, such as plus seven or minus one, whose value remains fixed regardless of what number x takes! Recognizing variables, coefficients, terms, and constants accurately prevents sign errors throughout algebra!"
        ),
        "checkpoints": [
            {
                "question": "In the univariate algebraic expression 5y³ - 7y² + y - 4, what is the coefficient of y² and what is the constant term?",
                "options": [
                    "Coefficient of y² is -7; constant term is -4",
                    "Coefficient of y² is 7; constant term is 4",
                    "Coefficient of y² is 5; constant term is 1",
                    "Coefficient of y² is -4; constant term is -7"
                ],
                "answer": 0,
                "hint": "Always keep the minus sign immediately to the left attached to each term!",
                "explanation": "The term is -7y² (coefficient -7) and the standalone number term is -4."
            },
            {
                "question": "How many terms are in the expression 3x² + 8x - 11, and why is it called univariate?",
                "options": [
                    "3 terms (3x², 8x, -11); univariate because it uses only one variable (x)",
                    "2 terms; univariate because its leading coefficient is 3",
                    "4 terms; univariate because 11 is prime",
                    "1 term; univariate because x is raised to power 2"
                ],
                "answer": 0,
                "hint": "Count the parts separated by + and - signs, and count how many distinct variable letters appear!",
                "explanation": "There are 3 terms: 3x², 8x, and -11; only the single letter x appears, making it univariate."
            }
        ]
    },
    {
        "id": 3,
        "title": "Polynomial Degree Types",
        "subtitle": "Section 2.1 Classification by Degree: Constant (0), Linear (1), Quadratic (2) & Cubic (3) Univariate Polynomials",
        "speech": (
            "Now define a univariate POLYNOMIAL and classify it sharply by its degree! "
            "A univariate polynomial is an algebraic expression formed by combining constants and powers of a single variable using ONLY addition, subtraction, and multiplication—crucially requiring every variable exponent to be a whole number: zero, one, two, three, and so on! "
            "Expressions containing division by a variable like four over x, or fractional powers like root x, are NOT polynomials! "
            "What determines a polynomial's DEGREE? Simply locate the HIGHEST power of the variable whose coefficient is non-zero! "
            "Look at our four benchmark classes! First, CONSTANT POLYNOMIALS have degree zero, such as eight written as eight x to the power zero—just a non-zero number! "
            "Second, LINEAR POLYNOMIALS—the hero of this chapter—have degree ONE, such as three z plus seven, where the highest exponent is z to the power one! "
            "Third, QUADRATIC POLYNOMIALS have degree TWO, like x squared plus five x plus one! "
            "Fourth, CUBIC POLYNOMIALS have degree THREE, like five y cubed plus y squared plus two y minus one! Identifying the exact polynomial degree immediately predicts both the algebraic structure and the geometric shape of an expression's graph cleanly across the entire Cartesian coordinate plane!"
        ),
        "checkpoints": [
            {
                "question": "Classify each polynomial by degree: (i) 8x⁰, (ii) 3z + 7, (iii) x² + 5x + 1, (iv) 5y³ + y² + 2y - 1.",
                "options": [
                    "(i) Constant (deg 0), (ii) Linear (deg 1), (iii) Quadratic (deg 2), (iv) Cubic (deg 3)",
                    "(i) Linear (deg 1), (ii) Constant (deg 0), (iii) Cubic (deg 3), (iv) Quadratic (deg 2)",
                    "(i) Zero (deg 0), (ii) Quadratic (deg 2), (iii) Linear (deg 1), (iv) Cubic (deg 3)",
                    "All four are linear polynomials"
                ],
                "answer": 0,
                "hint": "Check the highest non-zero exponent of the variable in each expression: 0, 1, 2, 3!",
                "explanation": "Highest powers are 0 (constant), 1 (linear), 2 (quadratic), and 3 (cubic) respectively."
            },
            {
                "question": "Which of the following expressions is NOT a polynomial?",
                "options": [
                    "3x + 5/x (contains x⁻¹ in denominator)",
                    "8 (equals 8x⁰)",
                    "0.5x - 4",
                    "5y³ + y² + 2y - 1"
                ],
                "answer": 0,
                "hint": "Polynomials allow only whole-number exponents (0, 1, 2, 3...) — never negative or fractional variable exponents!",
                "explanation": "5/x equals 5x⁻¹, which has negative exponent -1, disqualifying it from being a polynomial."
            }
        ]
    },
    {
        "id": 4,
        "title": "Linear Polynomial Properties",
        "subtitle": "Section 2.2 Linear Polynomials: Perimeter (4x), Fixed-Plus-Variable Fees & Single-Variable Input-Output Functions (y = ax + b)",
        "speech": (
            "Zoom cleanly into Section Two Point Two: Linear Polynomials! "
            "Every univariate linear polynomial takes the crisp general algebraic blueprint a x plus b, where a and b are fixed numbers and critically a cannot equal zero! Why must a be non-zero? Because if a drops to zero, the x term vanishes and only a constant polynomial b remains! "
            "Test two everyday situations governed directly by linear polynomials! First, measure the perimeter of a square tile of variable side x centimetres: perimeter P equals four x! Here rate a is four and baseline b is zero! "
            "Second, join a local sports club charging a one-time registration fee of two hundred rupees plus fifty rupees for every match played! Let x represent matches played; total cost equals fifty x plus two hundred! Notice the exact fixed-plus-variable structure: a baseline constant b plus a steady rate a per unit! "
            "Now think like a mathematician or computer scientist: treat a linear polynomial as an INPUT-OUTPUT FUNCTION y equals a x plus b! Feed in any numerical input x, multiply by constant rate a, add fixed baseline b, and collect one exact output value y every single time you test it!"
        ),
        "checkpoints": [
            {
                "question": "A sports academy charges a ₹300 one-time joining fee plus ₹75 per match played. Which linear input-output function gives total cost y for x matches?",
                "options": [
                    "y = 75x + 300 (with rate a = 75, baseline b = 300)",
                    "y = 300x + 75",
                    "y = 375x",
                    "y = 75x² + 300"
                ],
                "answer": 0,
                "hint": "The match fee multiplies the number of matches x, while the one-time joining fee stays constant!",
                "explanation": "Variable cost for x matches is 75x plus fixed ₹300 joining fee gives y = 75x + 300."
            },
            {
                "question": "In the standard linear polynomial P(x) = ax + b, why is the condition a ≠ 0 strictly required?",
                "options": [
                    "If a = 0, ax vanishes leaving constant polynomial P(x) = b of degree 0 (not linear degree 1)",
                    "If a = 0, b becomes infinite",
                    "Because x cannot equal zero",
                    "Because b must always equal zero"
                ],
                "answer": 0,
                "hint": "What happens to the degree of ax + b when a is replaced by 0?",
                "explanation": "When a = 0, P(x) = 0·x + b = b, dropping the degree from 1 (linear) to 0 (constant)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Constant Successive Differences",
        "subtitle": "Section 2.2 Constant Differences: Why Linear Polynomials Yield Equal First Differences Across Successive Integer Inputs",
        "speech": (
            "Discover the most reliable fingerprint of a linear polynomial! "
            "Suppose you pick any linear polynomial y equals a x plus b—say y equals four x plus three—and evaluate it at consecutive integer inputs x equals zero, one, two, three, four, and five! "
            "Watch the outputs appear: three, seven, eleven, fifteen, nineteen, twenty-three! "
            "Now subtract each output from the very next output! Seven minus three equals four! Eleven minus seven equals four! Fifteen minus eleven equals four! Every consecutive jump adds EXACTLY positive four—the coefficient a! "
            "Prove why this ALWAYS works algebraically! Compare output at x plus one against output at x: open-parenthesis a times open x plus one close plus b close-parenthesis minus open-parenthesis a x plus b close-parenthesis! "
            "Expanding gives a x plus a plus b minus a x minus b; both a x and b cancel out completely, leaving strictly the constant a! "
            "Contrast that with a quadratic polynomial like x squared: outputs zero, one, four, nine, sixteen show ever-changing jumps of one, three, five, seven! Only degree-one linear polynomials guarantee perfectly equal, constant first differences across every single consecutive integer input step—giving mathematics students everywhere an instant, completely reliable algebraic linearity verification test!"
        ),
        "checkpoints": [
            {
                "question": "For the linear polynomial P(x) = 5x - 8, what is the constant difference P(x + 1) - P(x) between any two consecutive integer inputs?",
                "options": [
                    "+5 (always equal to coefficient a)",
                    "-8 (equal to constant b)",
                    "5x",
                    "Changes as x grows larger"
                ],
                "answer": 0,
                "hint": "Compute (5(x + 1) - 8) - (5x - 8)!",
                "explanation": "P(x + 1) - P(x) = (5x + 5 - 8) - (5x - 8) = 5, constant for every integer x."
            },
            {
                "question": "Which output table for consecutive inputs x = 1, 2, 3, 4 represents a linear polynomial?",
                "options": [
                    "y: 7, 10, 13, 16 (constant difference +3)",
                    "y: 1, 4, 9, 16 (differences 3, 5, 7)",
                    "y: 2, 4, 8, 16 (differences 2, 4, 8)",
                    "y: 1, 8, 27, 64 (differences 7, 19, 37)"
                ],
                "answer": 0,
                "hint": "Check consecutive differences y(x + 1) - y(x) — linear polynomials always show equal steps!",
                "explanation": "10 - 7 = 3, 13 - 10 = 3, and 16 - 13 = 3; constant differences verify y = 3x + 4."
            }
        ]
    },
    {
        "id": 6,
        "title": "Tile Pattern Rules",
        "subtitle": "Section 2.3 Exploring Linear Patterns: Geometric Square Tile Generalization (2n - 1) & Constant-Difference Linear Sequences",
        "speech": (
            "Move into Section Two Point Three: Exploring Linear Patterns, where visual geometry generates algebraic sequences! "
            "Look at a sequence of growing L-shaped square tile borders! "
            "Step one begins with one single corner tile! "
            "Step two places one tile to the right and one tile above, creating an L-shape of three tiles! "
            "Step three extends each arm by one more tile, creating five tiles! "
            "Step four creates seven tiles! Count them: one, three, five, seven, nine! "
            "Notice how every new stage simply attaches two extra square tiles—one at the top tip and one at the right tip! Because the jump stays fixed at plus two, the tile count forms a linear sequence! "
            "How do we derive the general term formula for Step n? Start with one central corner tile, plus open-parenthesis n minus one close-parenthesis pairs of two arm tiles: one plus two times open n minus one close simplifies cleanly to two n minus one! "
            "Check Step five: two times five minus one equals nine tiles! Notice the common difference plus two becomes the coefficient multiplying n! Visual geometric decomposition turns sequence pictures straight into exact linear polynomials you can verify cleanly for any positive integer stage!"
        ),
        "checkpoints": [
            {
                "question": "In the growing L-shaped tile pattern with counts 1, 3, 5, 7, ..., how many tiles are in Step 25 using general term 2n - 1?",
                "options": [
                    "49 tiles",
                    "50 tiles",
                    "51 tiles",
                    "25 tiles"
                ],
                "answer": 0,
                "hint": "Substitute n = 25 cleanly into 2n - 1!",
                "explanation": "At n = 25, T(25) = 2(25) - 1 = 50 - 1 = 49 tiles."
            },
            {
                "question": "A linear pattern starts at 5 and adds 4 tiles at each new step (5, 9, 13, 17, ...). What is its general formula for Step n?",
                "options": [
                    "4n + 1",
                    "5n + 4",
                    "4n + 5",
                    "5n - 1"
                ],
                "answer": 0,
                "hint": "Use Step 1 + (n - 1) × difference = 5 + 4(n - 1)!",
                "explanation": "5 + 4(n - 1) = 5 + 4n - 4 = 4n + 1 (check: at n=1, 4+1=5; at n=2, 8+1=9)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Applied Linear Sequences",
        "subtitle": "Section 2.3 Applied Sequence Problems: Daily Allowance, Tiered Taxi Fares, Savings Accumulations & Reading Rates",
        "speech": (
            "Linear sequences appear everywhere in daily budgeting, transportation, and study planning! Explore four signature NCERT-style applications! "
            "First, DAILY ALLOWANCE SPENDING: a student receives five hundred rupees at month-start and spends thirty rupees daily on bus fare! After d days, remaining balance equals five hundred minus thirty d—decreasing steadily by thirty each day! "
            "Second, TIERED TAXI FARE: a city cab charges thirty-five rupees flag-down fare for the first kilometre, then twelve rupees for each additional kilometre! For total distance d kilometres where d is at least one, fare equals thirty-five plus twelve times open d minus one close, simplifying neatly to twelve d plus twenty-three! "
            "Third, SAVINGS ACCUMULATION: starting with six hundred rupees in a bank account and depositing one hundred fifty rupees weekly creates balance six hundred plus one hundred fifty w after w weeks—a rising sequence adding one hundred fifty every week! "
            "Fourth, READING COMPLETION RATE: reading eighteen pages every evening from a two-hundred-seventy-page book leaves two hundred seventy minus eighteen n pages unread after n evenings—finishing cleanly in fifteen evenings! Notice how every single real-world sequence model above increases or decreases uniformly by an exact constant step across every single equal unit time period!"
        ),
        "checkpoints": [
            {
                "question": "A taxi charges ₹40 for the first kilometre and ₹15 for every extra kilometre thereafter. What is the fare for a 9 km ride?",
                "options": [
                    "₹160",
                    "₹175",
                    "₹135",
                    "₹120"
                ],
                "answer": 0,
                "hint": "First km costs ₹40; the remaining (9 - 1) = 8 km each cost ₹15!",
                "explanation": "Fare = 40 + 15(9 - 1) = 40 + 120 = ₹160 (or simplified linear rule 15d + 25 → 15(9) + 25 = 160)."
            },
            {
                "question": "A learner begins with ₹800 savings and adds ₹125 each week. After how many weeks will total savings reach ₹1,800?",
                "options": [
                    "8 weeks",
                    "6 weeks",
                    "10 weeks",
                    "12 weeks"
                ],
                "answer": 0,
                "hint": "Solve 800 + 125w = 1800!",
                "explanation": "125w = 1800 - 800 = 1000 ⇒ w = 1000 / 125 = 8 weeks."
            }
        ]
    },
    {
        "id": 8,
        "title": "Linear Growth Models",
        "subtitle": "Section 2.4 Linear Growth: Positive Constant Rate Parameters (a > 0), C(d) = 100 + 60d & Plant Growth Applications",
        "speech": (
            "Now inspect Section Two Point Four: Linear Growth versus Linear Decay! "
            "Whenever a quantity increases by the EXACT SAME positive amount over equal intervals of time or steps, we model it with LINEAR GROWTH: y equals a x plus b with positive rate parameter a greater than zero! "
            "Look at a classic example: C of d equals one hundred plus sixty d! Suppose a small digital workshop pays a baseline subscription of one hundred rupees plus sixty rupees per active day d, or a gardener tracks a sapling starting at height twelve centimetres that grows steadily at three centimetres per week! "
            "Wait—check how C of d equals one hundred plus sixty d behaves day by day! On day zero, baseline value is one hundred! Day one reaches one hundred sixty! Day two hits two hundred twenty! Day five reaches four hundred! "
            "Notice two vital properties of linear growth! First, rate a equal to positive sixty means every single unit increase in d pushes C upward by sixty, creating an upward-climbing trend without curves or acceleration! Second, doubling d does NOT double total C unless baseline b equals zero! Watch the growth graph rise steadily below!"
        ),
        "checkpoints": [
            {
                "question": "In the linear growth function C(d) = 100 + 60d, what do 100 and 60 represent?",
                "options": [
                    "100 is the initial baseline value at d = 0; 60 is the constant growth added per unit increase in d",
                    "100 is the growth rate; 60 is the initial baseline value",
                    "Both 100 and 60 are exponential multipliers",
                    "C(d) shrinks by 60 each day"
                ],
                "answer": 0,
                "hint": "Plug in d = 0 first to find the baseline, then check C(d + 1) - C(d)!",
                "explanation": "C(0) = 100 gives the starting value, and C(d + 1) - C(d) = 60 (> 0) gives constant daily growth."
            },
            {
                "question": "A sapling is 8 cm tall when planted and grows linearly at 2.5 cm per week. How tall will it be after 12 weeks?",
                "options": [
                    "38 cm",
                    "30 cm",
                    "32 cm",
                    "24 cm"
                ],
                "answer": 0,
                "hint": "Evaluate H(12) = 8 + 2.5 × 12!",
                "explanation": "H(12) = 8 + 2.5(12) = 8 + 30 = 38 cm."
            }
        ]
    }
]

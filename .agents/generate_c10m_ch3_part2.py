#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 3: Pair of Linear Equations in Two Variables
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero human character names (Akhila, Champa, Aftab, Meena, Nuri, Sonu, Raghav, etc.), zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Substitution Cost Problems",
        "subtitle": "Applying Substitution to Pencil-Eraser Coincidence, Bat-Ball Prices & Fraction Word Puzzles",
        "speech": (
            "Now solve exciting practical money and fraction problems using the Substitution Method—and watch closely for a remarkable twist! Look at our earlier pencil-eraser bill: 2 pencils plus 3 erasers cost 9 rupees "
            "(2x plus 3y equals 9), while 4 pencils plus 6 erasers cost 18 rupees (4x plus 6y equals 18)! Express x cleanly from Equation One: x equals (9 minus 3y) divided by 2! Substitute this fraction straight inside "
            "Equation Two: 4 times [(9 minus 3y)/2] plus 6y equals 18! Simplify 4 over 2 into 2 times (9 minus 3y), yielding 18 minus 6y plus 6y equals 18! Notice minus 6y and plus 6y CANCEL completely—leaving the pure true identity "
            "18 equals 18! Wait: does 18 equals 18 mean we made a mistake? NEVER! Whenever both variables cancel cleanly leaving a TRUE identity like 18 equals 18, BOTH equations share infinitely many common solutions (coincident)! "
            "Meanwhile, in sports equipment shopping (7 bats plus 6 balls equal 3,800 rupees; 3 bats plus 5 balls equal 1,750 rupees), clean substitution solves exact prices: 500 rupees per cricket bat and 50 rupees per cricket ball—proving how cleanly substitution cracks shopping bills and trickier fraction ratio word problems cleanly without errors!"
        ),
        "checkpoints": [
            {
                "question": "If substituting one equation into the second eliminates all variables and leaves a true statement like 18 = 18 (with no x or y left), what does this prove?",
                "options": [
                    "The pair has INFINITELY MANY solutions (coincident dependent equations)",
                    "There is strictly no solution (inconsistent)",
                    "Both x and y must equal 18",
                    "An arithmetic mistake occurred"
                ],
                "answer": 0,
                "hint": "Think about what 18 = 18 means—it holds true for EVERY choice of y along the first equation!",
                "explanation": "An identity like 18 = 18 holds universally, confirming the second equation carries no new constraint beyond the first—yielding infinitely many solutions."
            },
            {
                "question": "A fraction becomes 9/11 if 2 is added to both numerator x and denominator y; it becomes 5/6 if 3 is added to both (Ex 3.2 Q3 v). Find the fraction x/y:",
                "options": [
                    "7 / 9",
                    "5 / 7",
                    "9 / 11",
                    "3 / 5"
                ],
                "answer": 0,
                "hint": "Test (x+2)/(y+2) = 9/11 and (x+3)/(y+3) = 5/6: (7+2)/(9+2) = 9/11 and (7+3)/(9+3) = 10/12 = 5/6!",
                "explanation": "Cross-multiplying gives 11x − 9y = −4 and 6x − 5y = −3, whose substitution solves cleanly to x = 7, y = 9 (fraction 7/9)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Substitution Age Problems",
        "subtitle": "Solving Future and Past Age Comparison Word Problems Cleanly via Linear Algebra",
        "speech": (
            "Time-traveling word puzzles comparing parent and child ages across past decades and future years become super clear once you translate time shifts carefully! Try this classic Exercise Three Point Two puzzle with neutral characters: "
            "An elder parent and a younger child compare their ages today, calling parent's present age x years and child's present age y years! Clue One looks FIVE YEARS INTO THE FUTURE: five years hence, both grow older by 5 years, making "
            "parent age (x plus 5) and child age (y plus 5)! The riddle says parent's future age will be THREE TIMES child's future age: write x plus 5 equals 3 times (y plus 5), simplifying cleanly to x minus 3y equals 10! "
            "Clue Two steps FIVE YEARS BACKWARD INTO THE PAST: five years ago, parent was (x minus 5) and child was (y minus 5), and parent's past age was SEVEN TIMES child's past age: x minus 5 equals 7 times (y minus 5), giving x minus 7y "
            "equals minus 30! Substituting x equals 3y plus 10 into Equation Two yields minus 4y equals minus 40—pinning child age y equal to 10 years and parent age x equal to 40 years!"
        ),
        "checkpoints": [
            {
                "question": "When translating '5 years hence (in the future), an elder parent's age x will be 3 times a child's age y', why must 5 be added to BOTH x and y?",
                "options": [
                    "Because both individuals age forward by 5 years together: (x + 5) = 3(y + 5)",
                    "Only the child grows older over 5 years",
                    "Only the parent grows older while the child stays age y",
                    "Because 5 × 3 = 15 replaces x"
                ],
                "answer": 0,
                "hint": "Every living person ages at the exact same rate of 1 year per year!",
                "explanation": "Time passes equally for both people, so 5 years later their ages are (x + 5) and (y + 5), giving x + 5 = 3(y + 5) ⟹ x − 3y = 10."
            },
            {
                "question": "In the previous age system (x − 3y = 10 and x − 7y = −30), verify the present ages (x, y) found by substitution:",
                "options": [
                    "Parent = 40 years, Child = 10 years",
                    "Parent = 35 years, Child = 10 years",
                    "Parent = 45 years, Child = 15 years",
                    "Parent = 30 years, Child = 5 years"
                ],
                "answer": 0,
                "hint": "Plug 40 and 10 into both checks: 5 years later (45 vs 15 = 3×) and 5 years ago (35 vs 5 = 7×)!",
                "explanation": "Substituting x = 3y + 10 into x − 7y = −30 gives −4y = −40 ⟹ y = 10 and x = 40."
            }
        ]
    },
    {
        "id": 11,
        "title": "Elimination Method Steps",
        "subtitle": "Scaling Equations With Non-Zero Constants and Adding/Subtracting to Eliminate One Variable",
        "speech": (
            "Now meet the lightning-fast champion of simultaneous equations: the ELIMINATION METHOD! Rather than building messy fractions while isolating a variable in Substitution, Elimination knocks out one complete variable "
            "cleanly in two crisp moves! How does it work? Step One: Choose either x or y to eliminate, then multiply one or BOTH entire equations by clever non-zero constants so the numeric coefficient in front of your target variable "
            "matches identically in size! Step Two: Check the signs of those matched terms—if they carry OPPOSITE signs (+ and −), ADD both equations vertically; if they share the SAME sign (+ and +, or − and −), SUBTRACT cleanly! "
            "Immediately that matched variable drops straight down to ZERO—eliminated! Test immediately on Exercise Three Point Two Question One: x plus y equals 5 and 2x minus 3y equals 4! Multiply Equation One completely by 3 to match y's coefficient: "
            "3x plus 3y equals 15! Now spot opposite signs (+3y and −3y)—simply ADD vertically! 3x plus 2x gives 5x, y vanishes cleanly, 15 plus 4 gives 19, instantly unlocking x equals 19 over 5 and back substituting swiftly to uncover y equals 6 over 5 cleanly without messy early fractions!"
        ),
        "checkpoints": [
            {
                "question": "In the Elimination Method, after scaling two equations so variable y has coefficients +6y and +6y (SAME sign), which operation eliminates y cleanly?",
                "options": [
                    "SUBTRACT one equation from the other (so 6y − 6y = 0)",
                    "ADD both equations together (giving 12y)",
                    "Multiply both equations by zero",
                    "Divide x by y"
                ],
                "answer": 0,
                "hint": "Same signs cancel via subtraction (SSS: Same Sign Subtract); opposite signs cancel via addition!",
                "explanation": "When coefficients match with identical signs (+6y and +6y), subtracting eliminates the variable (6y − 6y = 0)."
            },
            {
                "question": "To eliminate x rapidly from 3x + 4y = 10 and 2x − 2y = 2 (Ex 3.2 Q1 ii), notice even simpler scaling on y: multiplying Eq 2 by what constant matches ±4y?",
                "options": [
                    "Multiply Equation 2 by 2 (giving 4x − 4y = 4), then ADD to get 7x = 14 ⟹ x = 2, y = 1!",
                    "Multiply Equation 2 by 5",
                    "Multiply Equation 1 by 0",
                    "Add directly without scaling"
                ],
                "answer": 0,
                "hint": "Notice −2y doubled becomes −4y—opposite to +4y in Equation 1!",
                "explanation": "Multiplying 2x − 2y = 2 by 2 produces 4x − 4y = 4; adding directly to 3x + 4y = 10 eliminates y cleanly -> 7x = 14 -> x = 2, y = 1."
            }
        ]
    },
    {
        "id": 12,
        "title": "Elimination Edge Cases",
        "subtitle": "Interpreting When Both Variables Disappear Under Elimination: True 0 = 0 vs False 0 = k",
        "speech": (
            "What mystery unfolds during Elimination whenever you scale Equation One cleanly to match x, subtract Equation Two, and BOTH x AND y disappear simultaneously at the exact same moment? Don't panic—algebra is "
            "sending you an unmistakable crystal-clear signal straight from Table Three Point One! Observe both possible leftovers carefully! Possibility A: Suppose you solve rails x plus 2y equals 4 and 2x plus 4y equals 12! "
            "Double Equation One cleanly to get 2x plus 4y equals 8, then subtract Equation Two: (2x minus 2x) plus (4y minus 4y) equals 8 minus 12—simplifying into the glaring FALSE mathematical statement ZERO equals MINUS FOUR! "
            "Because zero can NEVER equal minus four for any x or y anywhere, no solution exists—those lines are strictly PARALLEL and INCONSISTENT! Possibility B: Double pencil-eraser bill 2x plus 3y equals 9 into 4x plus 6y equals 18, "
            "then subtract 4x plus 6y equals 18—yielding the universally TRUE statement ZERO equals ZERO! A true identity 0 equals 0 proves COINCIDENT overlapping lines sharing infinitely many solutions! Notice how nicely clean algebra signals every geometric curve relationship automatically without drawing any axes! Both 0 equals 0 and 0 equals k stay completely reliable algebraic signals everywhere!"
        ),
        "checkpoints": [
            {
                "question": "During the Elimination Method, if BOTH variables x and y cancel cleanly leaving a FALSE equation such as 0 = −4, what does that prove?",
                "options": [
                    "The pair of equations is INCONSISTENT (parallel lines, NO solution)",
                    "There are infinitely many solutions",
                    "x = 0 and y = −4",
                    "You must multiply by 2 again"
                ],
                "answer": 0,
                "hint": "Can any values of x and y ever make 0 equal −4?",
                "explanation": "A false numerical contradiction (0 = −4) proves no ordered pair can satisfy both equations simultaneously (parallel inconsistent system)."
            },
            {
                "question": "Contrast the two variable-cancellation outcomes under Elimination (0 = 0 vs 0 = k for k ≠ 0):",
                "options": [
                    "0 = 0 means infinitely many solutions (coincident); 0 = k (k ≠ 0) means NO solution (parallel)",
                    "0 = 0 means unique solution at origin (0, 0)",
                    "0 = k (k ≠ 0) means infinitely many solutions",
                    "Both always mean no solution"
                ],
                "answer": 0,
                "hint": "True identity = dependent overlapping lines; false contradiction = separated parallel lines!",
                "explanation": "True 0 = 0 holds along every point of the shared line (∞ solutions); false 0 = k contradicts itself everywhere (0 solutions)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Income Ratio Problems",
        "subtitle": "Solving Ratio-Based Monthly Income & Expenditure Systems via Elimination (Textbook Ex 8)",
        "speech": (
            "Now put our Elimination engine onto a classic real-life ratio puzzle straight from Textbook Example Eight! Suppose two households earn monthly incomes in the exact ratio 9 is to 7, while their monthly expenditures "
            "stand in the ratio 4 is to 3! Remarkably, both families manage to save the exact same tidy amount of 2,000 rupees every single month! How do we find their exact monthly incomes without confusing ratios? Assign a separate scale factor "
            "to each ratio! Let monthly incomes equal 9x and 7x rupees, and let monthly expenditures equal 4y and 3y rupees! Remember Savings equals Income minus Expenditure! For Family One: 9x minus 4y equals 2,000! For Family Two: "
            "7x minus 3y equals 2,000! Watch Elimination work swiftly to wipe out y: multiply Equation One by 3 (getting 27x minus 12y equals 6,000) and multiply Equation Two by 4 (getting 28x minus 12y equals 8,000)! Subtract Equation One "
            "cleanly from Equation Two: (28x minus 27x) equals 8,000 minus 6,000, giving x equals 2,000 immediately! Multiply by 9 and 7 to uncover monthly incomes: 18,000 rupees and 14,000 rupees! Subtracting 2,000 savings confirms exact expenses 16,000 and 12,000 match ratio four to three!"
        ),
        "checkpoints": [
            {
                "question": "If incomes are in ratio 9 : 7 and expenditures are in ratio 4 : 3 with ₹2,000 saved by each, why do we use two DIFFERENT variables x and y (9x, 7x and 4y, 3y)?",
                "options": [
                    "Because income ratio multiplier x and expenditure ratio multiplier y are generally different quantities",
                    "Because 9 and 4 are odd and even numbers",
                    "Because savings must always be negative",
                    "To force parallel lines"
                ],
                "answer": 0,
                "hint": "A single multiplier k only scales ONE ratio, whereas two distinct ratios (income vs expenditure) need independent multipliers x and y!",
                "explanation": "Two separate ratios require two distinct proportionality variables x and y so incomes (9x, 7x) and expenses (4y, 3y) scale independently."
            },
            {
                "question": "In the system 9x − 4y = 2000 and 7x − 3y = 2000, solving gives x = 2000. What are the two monthly incomes and verified expenses?",
                "options": [
                    "Incomes ₹18,000 & ₹14,000; Expenses ₹16,000 & ₹12,000 (since y = 4,000, saving ₹2,000 each!)",
                    "Incomes ₹9,000 & ₹7,000",
                    "Incomes ₹20,000 & ₹16,000",
                    "Incomes ₹12,000 & ₹10,000"
                ],
                "answer": 0,
                "hint": "Multiply 9×2000 and 7×2000, and check 18,000 − 2,000 = 16,000!",
                "explanation": "Incomes = 9(2000) = ₹18,000 and 7(2000) = ₹14,000; subtracting ₹2,000 savings confirms expenses ₹16,000 : ₹12,000 = 4 : 3."
            }
        ]
    },
    {
        "id": 14,
        "title": "Digit Reversal Puzzles",
        "subtitle": "Solving Two-Digit Place-Value and Reversed-Digit Problems Using Elimination (Ex 10)",
        "speech": (
            "Two-digit reversed number riddles sit among students' favorite classic algebra puzzles—provided you write place value carefully! Suppose a two-digit number owns tens digit x and units digit y! Be careful: NEVER write the number "
            "as xy (which means x multiplied by y)! Because tens digit x stands in the tens place, the actual number equals 10x plus y! When you reverse its digits, y slides into the tens place and x moves to units—creating the reversed number 10y plus x! "
            "Now solve Textbook Example Ten using Elimination! Clue One: Adding the original number (10x plus y) and its reverse (10y plus x) totals 66! Combine cleanly: 11x plus 11y equals 66—dividing through by 11 gives crisp equation "
            "x plus y equals 6! Clue Two: The two digits differ by 2! Careful algebraic alertness! Because either x could exceed y (x minus y equals 2) OR y could exceed x (y minus x equals 2), TWO valid elimination pairs arise! Adding x plus y equals 6 "
            "with x minus y equals 2 gives 2x equals 8 -> x equals 4, y equals 2 (number 42); switching yields 24! Check cleanly: 42 plus 24 equals 66, and both digits clearly differ by two!"
        ),
        "checkpoints": [
            {
                "question": "If a two-digit number has tens digit x and units digit y, what algebraic expression equals the ORIGINAL number minus the REVERSED number?",
                "options": [
                    "(10x + y) − (10y + x) = 9x − 9y = 9(x − y)",
                    "xy − yx = 0",
                    "10x − 10y = 10(x − y)",
                    "11x + 11y"
                ],
                "answer": 0,
                "hint": "Subtract (10y + x) carefully from (10x + y)!",
                "explanation": "10x + y − 10y − x = 9(x − y), explaining why the difference between any 2-digit number and its reverse is always a multiple of 9!"
            },
            {
                "question": "Why does the riddle 'sum of a 2-digit number and its reverse is 66, and its digits differ by 2' produce TWO valid answers (42 and 24)?",
                "options": [
                    "Because 'digits differ by 2' allows either tens > units (x − y = 2 -> 42) OR units > tens (y − x = 2 -> 24)",
                    "Because 66 is divisible by 2",
                    "Because reversed numbers always halve themselves",
                    "Because x must always equal 0"
                ],
                "answer": 0,
                "hint": "Difference |x − y| = 2 splits into two symmetric linear equations!",
                "explanation": "Solving x + y = 6 alongside x − y = 2 yields 42, while solving alongside y − x = 2 yields 24; both satisfy 42 + 24 = 66."
            }
        ]
    },
    {
        "id": 15,
        "title": "Comparing Solution Methods",
        "subtitle": "Choosing Smartly Between Graphical, Substitution, and Elimination Workflows",
        "speech": (
            "Now think like a seasoned mathematical strategist! With three distinct solving tools resting inside your belt—Graphical Method, Substitution Method, and Elimination Method—which tool solves any given puzzle fastest and cleanest? "
            "Observe each scenario! First, choose the GRAPHICAL METHOD whenever a visual picture of lines (intersecting, parallel, or coincident) helps interpret trends OR when simple integer grid crossings appear easily—though remember graphs struggle "
            "with fractions like 19 over 29! Second, grab the SUBSTITUTION METHOD the very instant ONE equation displays a lonely variable carrying unit coefficient 1 or minus 1—such as x equals 14 minus y, or y equals 2x minus 2—making substitution clean "
            "with zero messy fractions! Third, fire up the ELIMINATION METHOD whenever coefficients appear large, equal, or nicely proportional—such as 9x minus 4y equals 2,000 alongside 7x minus 3y equals 2,000, OR symmetric sums 11x plus 11y equals 66! "
            "Every genuine pair yields the EXACT SAME unique solution regardless of method chosen—picking the smartest method simply saves busy algebra steps, prevents tricky fraction arithmetic mistakes, avoids imprecise rounding, and prevents annoying sign slips, preserves clean exactness, and builds tremendous mathematical accuracy and solving confidence across every single linear equation problem you ever tackle!"
        ),
        "checkpoints": [
            {
                "question": "Suppose you face the system 15x − 14y = 117 and 14x − 15y = 115. Why is Elimination/Add-Subtract far smarter than Substitution here?",
                "options": [
                    "Substitution creates ugly denominator-15 fractions immediately, whereas adding & subtracting swapped coefficients produces simple x+y and x−y!",
                    "Substitution does not work mathematically on numbers > 10",
                    "Because graphs cannot draw 15x",
                    "Elimination always gives 0 = 0 for large numbers"
                ],
                "answer": 0,
                "hint": "Look at what happens when you ADD and SUBTRACT two equations whose x and y coefficients are swapped!",
                "explanation": "Adding gives 29(x − y) or 29(x + y) cleanly without fractions, whereas isolating x creates /15 denominators immediately."
            },
            {
                "question": "If two equations represent intersecting lines, will solving the pair via Graphical, Substitution, and Elimination methods yield different answers?",
                "options": [
                    "No—all valid methods must return the exact same unique ordered pair (x, y)",
                    "Yes, Elimination flips x and y coordinates",
                    "Yes, Substitution gives only positive fractions",
                    "Only Graphical plotting finds the true answer"
                ],
                "answer": 0,
                "hint": "Intersection coordinates depend purely on the lines themselves, not the tool used to find them!",
                "explanation": "All algebraic and graphical methods solve the identical underlying linear pair and yield the exact same unique intersection point."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Three Summary",
        "subtitle": "Synthesizing Geometric Cases, Table 3.1 Consistency Ratios, Substitution & Elimination",
        "speech": (
            "Congratulations on conquering every pillar of NCERT Class Ten Chapter Three: Pair of Linear Equations in Two Variables! Let us snap all foundational tools neatly into place before diving into Exercise Three Point One, Exercise Three Point Two, "
            "and our final Mastery Challenges! Pillar One—Modeling: translate real-world fair rides, ages, costs, fractions, and two-digit reversed numbers (10x plus y) cleanly into two simultaneous equations a1 x plus b1 y plus c1 equals 0 and a2 x plus b2 y plus c2 equals 0! "
            "Pillar Two—Graphical Geometry & Table Three Point One: remember three outcomes! Unequal ratios a1 over a2 NOT equal to b1 over b2 give intersecting lines with ONE unique solution (Consistent); ALL THREE equal ratios produce overlapping COINCIDENT lines "
            "with infinitely many solutions (Dependent Consistent); matching a1 over a2 equals b1 over b2 NOT equal to c1 over c2 give PARALLEL lines with zero solutions (Inconsistent)! Pillar Three—Exact Algebra: isolate lonely unit-coefficient variables via Substitution, "
            "or scale coefficients cleanly to knock out one variable via Elimination! Remember also special flags zero equals zero and zero equals k! Practice cleanly on every exercise across Three Point One, Three Point Two, and our Challenge Quizzes ahead!"
        ),
        "checkpoints": [
            {
                "question": "For which value of k does the pair kx + 3y − (k − 3) = 0 and 12x + ky − k = 0 have INFINITELY MANY solutions?",
                "options": [
                    "k = 6  (check: 6/12 = 3/6 = (6−3)/6 = 1/2! Note k = −6 fails c₁/c₂)",
                    "k = −6",
                    "k = 3",
                    "k = 12"
                ],
                "answer": 0,
                "hint": "Require ALL THREE ratios equal: k/12 = 3/k = (k−3)/k -> k² = 36 gives ±6, then check c₁/c₂!",
                "explanation": "k² = 36 gives k = ±6. Testing k = 6 gives 6/12 = 3/6 = 3/6 = 1/2 (valid!), whereas k = −6 gives −1/2 ≠ (−9)/(−6) = +3/2."
            },
            {
                "question": "Which summary statement accurately links Table 3.1 ratios, geometry, and algebraic outcomes?",
                "options": [
                    "Intersecting (a₁/a₂≠b₁/b₂ -> 1 sol), Coincident (all equal -> ∞, 0=0), Parallel (slopes equal≠c ratio -> 0 sol, false 0=k)",
                    "Parallel lines always yield a unique intersection at (0, c)",
                    "Dependent coincident lines are classified as Inconsistent",
                    "Elimination can never detect parallel lines"
                ],
                "answer": 0,
                "hint": "Check all three columns: Ratio <-> Graph <-> Algebra!",
                "explanation": "Table 3.1 ratios correspond identically to line intersections/overlaps/parallelism and algebraic outcomes (unique, 0=0, 0=k)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch3 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

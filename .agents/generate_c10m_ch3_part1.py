#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 3: Pair of Linear Equations in Two Variables
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero human character names (Akhila, Champa, Aftab, Meena, Nuri, Sonu, Raghav, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Fair Equation Modeling",
        "subtitle": "Translating Real-World Stories Into Simultaneous Linear Equations in Two Variables",
        "speech": (
            "Welcome, keen Class Ten problem solvers, to Chapter Three: Pair of Linear Equations in Two Variables! Imagine a cheerful student visiting a bustling "
            "village carnival fair with twenty rupees safely inside a coin pocket, eager to enjoy rides on the towering Giant Wheel and play ring-tossing Hoopla! Notice two mathematical "
            "facts connecting her games together: the total number of times she played Hoopla, called y, equals EXACTLY half the number of Giant Wheel rides, called x! Furthermore, "
            "each Giant Wheel ride costs three rupees while each Hoopla round costs four rupees, totaling exactly twenty rupees spent completely! Look how naturally everyday clues "
            "turn into TWO algebraic equations carrying two matching unknowns x and y! From half of x equals y, rearranging gives x minus 2y equals zero; from the ticket bill comes "
            "3x plus 4y minus 20 equals zero! Because both statements must hold true simultaneously for the EXACT SAME fair visit, mathematicians call them a PAIR OF LINEAR EQUATIONS "
            "in two variables! In standard form, we write a1 x plus b1 y plus c1 equals zero and a2 x plus b2 y plus c2 equals zero, where coefficients a and b are never both zero together!"
        ),
        "checkpoints": [
            {
                "question": "If x represents Giant Wheel rides (₹3 each) and y represents Hoopla games (₹4 each = half of x), totaling ₹20 spent, which pair of equations models this situation?",
                "options": [
                    "x − 2y = 0   and   3x + 4y = 20",
                    "2x − y = 0   and   4x + 3y = 20",
                    "x + y = 20   and   3x − 4y = 0",
                    "x − y = 3   and   x + 4y = 20"
                ],
                "answer": 0,
                "hint": "y = (1/2)x multiplies cleanly by 2 into x = 2y (so x − 2y = 0), and total cost is 3x + 4y = 20!",
                "explanation": "Translating 'Hoopla = half of rides' gives y = x/2 ⟹ x − 2y = 0; summing costs gives 3x + 4y = 20 (solving cleanly to x = 4, y = 2)."
            },
            {
                "question": "In the general form a₁x + b₁y + c₁ = 0 for a linear equation in two variables x and y, what must hold for real numbers a₁ and b₁?",
                "options": [
                    "a₁ and b₁ cannot both be zero simultaneously (written compactly as a₁² + b₁² ≠ 0)",
                    "a₁ must equal 1 while b₁ must equal 0 always",
                    "c₁ can never equal 0",
                    "a₁ and b₁ must always be equal"
                ],
                "answer": 0,
                "hint": "If BOTH a₁ = 0 and b₁ = 0, both variables x and y vanish completely!",
                "explanation": "Requiring a₁ and b₁ not both zero (a₁² + b₁² ≠ 0) ensures at least one variable remains so the graph represents a genuine straight line."
            }
        ]
    },
    {
        "id": 2,
        "title": "Intersecting Unique Solution",
        "subtitle": "Graphical Case 1: Consistent Pair Intersecting at One Unique Common Point",
        "speech": (
            "Now step onto the glowing Cartesian grid and watch our two linear fair equations draw ruler-straight paths across space! Plot two neat solutions for x minus 2y equals zero: "
            "when x is 0, y equals 0; when x is 4, y equals 2! Joining them draws a bright upward line! Next plot two points for 3x plus 4y equals 20: when x is 0, y equals 5; when x is 4, "
            "y equals 2! Watch carefully right where BOTH straight lines cross paths at a single crisp glowing dot: (4, 2)! Why is (4, 2) so special? Because point (4, 2) lies simultaneously "
            "on Line One AND on Line Two—making it the ONLY ordered pair satisfying BOTH conditions together (4 rides at 3 rupees plus 2 games at 4 rupees equals 20 rupees, and 2 equals half of 4)! "
            "Test another textbook graph: x plus 3y equals 6 and 2x minus 3y equals 12 cross right on the x-axis at ONE unique point (6, 0)! Whenever two distinct lines intersect at one shared "
            "point, the system owns a UNIQUE SOLUTION and proudly earns the clean mathematical title CONSISTENT across linear algebra because lines can cross strictly once!"
        ),
        "checkpoints": [
            {
                "question": "When the graphs of two linear equations intersect cleanly at one single point (6, 0), what can we say about the system's solution and consistency?",
                "options": [
                    "The pair has a unique solution (x = 6, y = 0) and is CONSISTENT",
                    "The pair has infinitely many solutions",
                    "The pair has no solution and is INCONSISTENT",
                    "Only x = 0 satisfies both equations"
                ],
                "answer": 0,
                "hint": "Two distinct straight lines can cross each other at most ONCE, giving a single shared solution!",
                "explanation": "A unique intersection point (x, y) satisfies both equations simultaneously—defining an independent, CONSISTENT system."
            },
            {
                "question": "Verify graphically/algebraically where lines x + 3y = 6 and 2x − 3y = 12 intersect:",
                "options": [
                    "(6, 0)",
                    "(0, 6)",
                    "(3, 1)",
                    "(4, 2)"
                ],
                "answer": 0,
                "hint": "Substitute (x, y) into BOTH equations cleanly (note y = 0 makes 6 = 6 and 12 = 12)!",
                "explanation": "6 + 3(0) = 6 and 2(6) − 3(0) = 12 both hold true at (6, 0), their single intersection point."
            }
        ]
    },
    {
        "id": 3,
        "title": "Parallel No Solution",
        "subtitle": "Graphical Case 2: Inconsistent Parallel Lines Never Intersecting Anywhere",
        "speech": (
            "Can two straight railway rails running steadily side by side across flat plains EVER meet one another anywhere along the horizon? Never! Welcome to Graphical Case Two: Parallel Lines! "
            "Inspect the classic railway-track equation pair from Section Three Point Two: x plus 2y minus 4 equals zero, and 2x plus 4y minus 12 equals zero! Let us plot both straight tracks on coordinate paper! "
            "For Line One (x plus 2y equals 4): points (0, 2) and (4, 0) tilt gently downwards across Quadrant One! Now plot Line Two (2x plus 4y equals 12, which simplifies to x plus 2y equals 6): points (0, 3) and (6, 0) "
            "tilt downwards at the EXACT SAME steepness! Look across your coordinate grid: Line Two glides steadily parallel ONE unit above Line One forever without closing the gap by even a hair's breadth! "
            "Because x plus 2y can NEVER equal 4 and 6 at the very same instant, zero common points lie on BOTH rails! When parallel lines share zero intersection points, the system possesses NO SOLUTION and is "
            "officially classified across mathematics as INCONSISTENT! Notice identical slopes yet shifted vertical heights keep both straight railway tracks separated cleanly forever!"
        ),
        "checkpoints": [
            {
                "question": "If two linear equations graph as strictly parallel lines on the coordinate plane, how is the pair classified?",
                "options": [
                    "INCONSISTENT with NO solution (zero common intersection points)",
                    "CONSISTENT with infinitely many solutions",
                    "CONSISTENT with a unique solution",
                    "Dependent with two distinct solutions"
                ],
                "answer": 0,
                "hint": "Parallel tracks never cross paths anywhere on the coordinate grid!",
                "explanation": "Because parallel lines never intersect, no ordered pair (x, y) satisfies both equations simultaneously—making the system INCONSISTENT."
            },
            {
                "question": "Look algebraically at rails x + 2y = 4 and 2x + 4y = 12 (dividing the second by 2 gives x + 2y = 6). Why is no solution possible?",
                "options": [
                    "The identical quantity (x + 2y) cannot simultaneously equal both 4 and 6",
                    "Because x and y must both be negative",
                    "Because dividing by 2 changes line slope",
                    "Because 12 is greater than 4"
                ],
                "answer": 0,
                "hint": "Can a single sum equal 4 and 6 at the exact same moment?",
                "explanation": "2x + 4y = 12 simplifies to x + 2y = 6, contradicting x + 2y = 4 and proving parallel separation."
            }
        ]
    },
    {
        "id": 4,
        "title": "Coincident Infinite Solutions",
        "subtitle": "Graphical Case 3: Dependent Coincident Lines Sharing Infinitely Many Common Solutions",
        "speech": (
            "Now inspect a subtle shopping example where two separate clues actually describe the EXACT SAME hidden line! Suppose a shopper buys 2 pencils and 3 erasers for 9 rupees (written "
            "2x plus 3y equals 9), while a friend buys 4 pencils and 6 erasers of the exact same brand for 18 rupees (written 4x plus 6y equals 18)! Plot Line One cleanly using points (0, 3) and (4.5, 0)! "
            "Next plot Line Two (4x plus 6y equals 18) using points (0, 3) and (3, 1)! Watch carefully on screen as Line Two lands DIRECTLY ON TOP OF Line One point for point—completely overlapping "
            "from minus infinity right across to plus infinity! Why did both equations fuse into one single identical straight line? Simply divide the second equation 4x plus 6y equals 18 completely through by 2, "
            "revealing 2x plus 3y equals 9—an exact scaled twin of Line One! Lines overlapping completely everywhere are called COINCIDENT LINES! Because EVERY single point sitting along that shared line solves BOTH "
            "equations simultaneously, a coincident pair owns INFINITELY MANY SOLUTIONS and is called DEPENDENT yet CONSISTENT because shared solutions genuinely exist everywhere along the entire shared straight geometric line!"
        ),
        "checkpoints": [
            {
                "question": "When two linear equations produce completely overlapping COINCIDENT lines, how many solutions exist and how is the pair classified?",
                "options": [
                    "Infinitely many solutions; classified as a DEPENDENT (and Consistent) pair",
                    "Unique solution; independent consistent",
                    "No solution; inconsistent",
                    "Strictly 2 solutions at the axes"
                ],
                "answer": 0,
                "hint": "Does a straight line contain finite or infinitely many coordinate points?",
                "explanation": "Every single point along the shared coincident line satisfies both equations simultaneously, yielding infinitely many solutions (dependent consistent)."
            },
            {
                "question": "Why do 2x + 3y = 9 and 4x + 6y = 18 graph onto the exact same coincident line?",
                "options": [
                    "Multiplying every term of 2x + 3y = 9 by 2 yields 4x + 6y = 18—making them equivalent equations",
                    "Because 18 − 9 = 9 creates a perpendicular turn",
                    "Because their y-intercepts differ by 2 units",
                    "Because both lines pass vertically through x = 9"
                ],
                "answer": 0,
                "hint": "Check what happens when you double every coefficient AND the constant in 2x + 3y = 9!",
                "explanation": "Scaling an entire equation (a₁, b₁, c₁) by non-zero constant k = 2 leaves its solution set completely unchanged—creating coincident lines."
            }
        ]
    },
    {
        "id": 5,
        "title": "Coefficient Ratio Table",
        "subtitle": "Table 3.1 Rules: Predicting Line Behaviour From Ratios a₁/a₂, b₁/b₂, and c₁/c₂",
        "speech": (
            "Must you always plot points across graph paper just to tell whether two lines cross once, run parallel forever, or coincide completely? Not at all—Table Three Point One "
            "of your NCERT textbook unlocks an instant algebraic radar comparing simply the three coefficient ratios a1 over a2, b1 over b2, and c1 over c2! First make sure BOTH equations sit cleanly in standard form "
            "with zero on the right-hand side! Now read all three golden radar checks carefully! Check One: If a1 over a2 does NOT equal b1 over b2, STOP immediately—you don't even need c1 over c2! Different slopes force "
            "the lines to INTERSECT at ONE unique point (Consistent)! Check Two: Whenever a1 over a2 EQUALS b1 over b2, look straight at c1 over c2 to settle the tie! If ALL THREE ratios match—a1 over a2 equals b1 over b2 "
            "equals c1 over c2—one equation is merely a scaled twin of the other, yielding COINCIDENT lines with INFINITELY MANY solutions (Dependent)! Check Three: If a1 over a2 equals b1 over b2, YET differs from c1 over c2, "
            "parallel tracks run cleanly apart—strictly PARALLEL lines sharing NO common solution anywhere (Inconsistent)! Memorizing Table Three Point One makes every pair crystal clear!"
        ),
        "checkpoints": [
            {
                "question": "According to Table 3.1, if a₁/a₂ ≠ b₁/b₂ for a pair of linear equations, what must be true graphically and algebraically?",
                "options": [
                    "Intersecting lines, exactly one unique solution, CONSISTENT pair",
                    "Parallel lines, no solution, INCONSISTENT pair",
                    "Coincident lines, infinitely many solutions, DEPENDENT pair",
                    "Cannot be decided without checking c₁/c₂ first"
                ],
                "answer": 0,
                "hint": "Different x-to-y coefficient ratios mean different line slopes!",
                "explanation": "Unequal slopes (a₁/a₂ ≠ b₁/b₂) guarantee two distinct straight lines in a plane must cross at one unique point (consistent)."
            },
            {
                "question": "Distinguish carefully between COINCIDENT vs. PARALLEL lines using Table 3.1 ratios:",
                "options": [
                    "Coincident: a₁/a₂ = b₁/b₂ = c₁/c₂  |  Parallel: a₁/a₂ = b₁/b₂ ≠ c₁/c₂",
                    "Coincident: a₁/a₂ ≠ b₁/b₂  |  Parallel: a₁/a₂ = b₁/b₂ = c₁/c₂",
                    "Coincident: a₁/a₂ = c₁/c₂ ≠ b₁/b₂  |  Parallel: all unequal",
                    "Both have a₁/a₂ = b₁/b₂ = c₁/c₂"
                ],
                "answer": 0,
                "hint": "Equal slopes (a₁/a₂ = b₁/b₂) produce coincident lines if constant ratio c₁/c₂ matches, or parallel separation if it differs!",
                "explanation": "Coincident lines preserve the ratio across ALL three terms (a, b, c), whereas parallel lines preserve slopes (a, b) yet shift constants (≠ c₁/c₂)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Checking Consistency Live",
        "subtitle": "Testing Textbook Equation Pairs Using Ratios and Solving Exercise 3.1 Examples",
        "speech": (
            "Let us put Table Three Point One straight to work testing real equations from Exercise Three Point One—and watch out for sneaky sign traps! Test Pair One: 5x minus 4y plus 8 equals 0, "
            "and 7x plus 6y minus 9 equals 0! Compare x-ratio a1 over a2 equaling 5 over 7 against y-ratio b1 over b2 equaling minus 4 over 6 equals minus 2 over 3! Clearly 5 over 7 does NOT equal minus 2 over 3—so "
            "Pair One represents INTERSECTING lines with a unique solution (Consistent)! Test Pair Two: 9x plus 3y plus 12 equals 0, and 18x plus 6y plus 24 equals 0! Compute ratios: 9 over 18 equals 1 over 2; 3 over 6 equals 1 over 2; "
            "and 12 over 24 equals 1 over 2! All three ratios equal 1 half—COINCIDENT lines with infinitely many solutions (Consistent Dependent)! Test Pair Three carefully: 6x minus 3y plus 10 equals 0, and 2x minus y plus 9 equals 0! "
            "Notice 6 over 2 equals 3, minus 3 over minus 1 equals +3, YET 10 over 9 does NOT equal 3! Equal slopes yet unequal constants reveal PARALLEL lines—completely INCONSISTENT with zero common intersection points anywhere on the plane!"
        ),
        "checkpoints": [
            {
                "question": "Classify the pair 6x − 3y + 10 = 0 and 2x − y + 9 = 0 (Exercise 3.1 Q2 iii) by comparing ratios:",
                "options": [
                    "Parallel lines (no solution, Inconsistent), since a₁/a₂ = 3 = b₁/b₂ ≠ c₁/c₂ (10/9)",
                    "Intersecting lines (unique solution)",
                    "Coincident lines (infinitely many solutions)",
                    "Perpendicular crossing at origin"
                ],
                "answer": 0,
                "hint": "Check signs carefully: (−3)/(−1) = +3, matching 6/2 = 3, then compare 10/9!",
                "explanation": "6/2 = 3 and (−3)/(−1) = 3, yet 10/9 ≠ 3—satisfying a₁/a₂ = b₁/b₂ ≠ c₁/c₂ for parallel inconsistent lines."
            },
            {
                "question": "WATCH SIGN TRAP! Are 3x + 2y = 5 and 2x − 3y = 7 consistent or inconsistent? Check ratios!",
                "options": [
                    "Consistent (Intersecting), because a₁/a₂ = 3/2 ≠ b₁/b₂ = −2/3",
                    "Inconsistent (Parallel), because constants 5 and 7 differ",
                    "Dependent coincident lines",
                    "Not linear equations"
                ],
                "answer": 0,
                "hint": "Always bring c to the same side (both −5 and −7 OR both +5 and +7 on RHS), and compare a₁/a₂ vs b₁/b₂ FIRST!",
                "explanation": "Since a₁/a₂ = 3/2 and b₁/b₂ = 2/(−3) = −2/3 are unequal, the lines intersect uniquely—automatically consistent!"
            }
        ]
    },
    {
        "id": 7,
        "title": "Shopping Pants Skirts",
        "subtitle": "Solving Textbook Shopping & Garden Perimeter Word Problems Graphically (Exercise 3.1)",
        "speech": (
            "Now solve a classic NCERT graphical word problem without touching any algebraic elimination yet! Imagine a customer visiting a clothing boutique to buy new pants and skirts! When asked how many she bought, "
            "she offers two playful number riddles: First, the number of skirts y equals two less than TWICE the number of pants x purchased—giving Equation One: y equals 2x minus 2! Second, the number of skirts y also "
            "equals four less than FOUR TIMES the number of pants x—giving Equation Two: y equals 4x minus 4! How can graphs crack this shopping riddle immediately? Plot two tidy points on Line One (y equals 2x minus 2): "
            "(1, 0) and (2, 2)! Next plot two tidy points on Line Two (y equals 4x minus 4): (1, 0) and (0, minus 4)! Look right where both bright lines cross cleanly on the horizontal x-axis: exact point (1, 0)! "
            "Reading coordinates gives x equals 1 pant and y equals 0 skirts—she bought ONE pant and ZERO skirts! Notice similarly Exercise Three Point One's rectangular garden half-perimeter puzzle (x plus y equals 36, x minus y equals 4) "
            "crosses cleanly at width 16 meters and length 20 meters!"
        ),
        "checkpoints": [
            {
                "question": "For the shopping riddle y = 2x − 2 (skirts = 2×pants − 2) and y = 4x − 4 (skirts = 4×pants − 4), where do both lines intersect?",
                "options": [
                    "(1, 0) -> 1 pant and 0 skirts purchased",
                    "(0, 1) -> 0 pants and 1 skirt",
                    "(2, 2) -> 2 pants and 2 skirts",
                    "Parallel lines (no solution)"
                ],
                "answer": 0,
                "hint": "Test x = 1, y = 0 inside both y = 2x − 2 and y = 4x − 4!",
                "explanation": "At (1, 0), 0 = 2(1) − 2 and 0 = 4(1) − 4 both hold identically, meaning 1 pant and 0 skirts were bought."
            },
            {
                "question": "Half the perimeter of a rectangular garden (length x is 4m more than width y) equals 36m (Ex 3.1 Q5). Which system & solution fit?",
                "options": [
                    "x + y = 36 and x − y = 4, intersecting at length 20 m and width 16 m",
                    "2x + 2y = 36 and x − y = 4, giving 11 m and 7 m",
                    "x + y = 36 and x + y = 4 (inconsistent)",
                    "x − y = 36 and y − x = 4"
                ],
                "answer": 0,
                "hint": "Perimeter = 2(length + width), so HALF the perimeter equals simply length + width = x + y!",
                "explanation": "Half perimeter x + y = 36 combined with x − y = 4 gives 2x = 40 ⟹ length 20 m and width 16 m."
            }
        ]
    },
    {
        "id": 8,
        "title": "Substitution Method Steps",
        "subtitle": "Section 3.3 Algebra: Isolating One Variable and Substituting Into the Second Equation",
        "speech": (
            "What happens whenever two lines cross at a messy fractional coordinate like (49 over 29, 19 over 29) instead of tidy whole integers? Counting tiny millimeters off graph paper becomes imprecise and frustrating! "
            "To achieve 100% razor-sharp exactness regardless of ugly fractions, mathematicians unleash EXACT ALGEBRAIC METHODS—starting with the SUBSTITUTION METHOD! Master this reliable three-step recipe on Textbook Example Seven: "
            "7x minus 15y equals 2, alongside x plus 2y equals 3! Step One: Pick the simplest equation—spot lonely x with coefficient ONE inside Equation Two! Express x cleanly in terms of y: x equals 3 minus 2y! "
            "Step Two: SUBSTITUTE that entire block (3 minus 2y) right in place of x inside Equation One! Write 7 times (3 minus 2y) minus 15y equals 2! Expand brackets carefully: 21 minus 14y minus 15y equals 2, which combines into "
            "minus 29y equals minus 19, pinning down exact fraction y equals 19 over 29! Step Three: Back-substitute y equals 19 over 29 straight into Step One's formula x equals 3 minus 2 times (19 over 29), yielding exact x equals 49 over 29 cleanly without any visual graph guesswork or rounding mistakes! Notice how smoothly substitution solves ugly fractions!"
        ),
        "checkpoints": [
            {
                "question": "Why does the algebraic Substitution Method improve upon Graphical plotting for systems like 7x − 15y = 2 and x + 2y = 3?",
                "options": [
                    "Graph reading struggles to estimate non-integer fractional intersections like (49/29, 19/29), whereas substitution computes exact fractions cleanly",
                    "Substitution changes parallel lines into intersecting lines",
                    "Graphical lines cannot represent negative coefficients",
                    "Substitution avoids solving any equations"
                ],
                "answer": 0,
                "hint": "Can human eyes read exact 29ths cleanly off standard graph squares?",
                "explanation": "Algebraic substitution calculates exact rational fractions (49/29, 19/29) without graph-reading approximation errors."
            },
            {
                "question": "Using Substitution on x + y = 14 and x − y = 4 (Exercise 3.2 Q1 i), express x = 4 + y and solve for (x, y):",
                "options": [
                    "(9, 5)",
                    "(10, 4)",
                    "(8, 6)",
                    "(7, 7)"
                ],
                "answer": 0,
                "hint": "Substitute x = 4 + y into x + y = 14 giving (4 + y) + y = 14!",
                "explanation": "4 + 2y = 14 ⟹ 2y = 10 ⟹ y = 5, and back-substituting gives x = 4 + 5 = 9."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch3 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

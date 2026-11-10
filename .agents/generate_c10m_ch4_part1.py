#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 4: Quadratic Equations
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (John, Jivanti, Rohan, Raghav, etc.), zero lecturer personas
- Note: Historical mathematicians Babylonians, Euclid, Brahmagupta, Sridharacharya, Al-Khwarizmi are part of syllabus 4.1.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Prayer Hall Equations",
        "subtitle": "Translating Real-Life Carpet Area & Geometry Into Quadratic Equations (Section 4.1)",
        "speech": (
            "Welcome, keen Class Ten problem solvers, to Chapter Four: Quadratic Equations! Earlier in Chapter Two, you explored linear polynomials of degree one and quadratic polynomials "
            "of degree two; then in Chapter Three, you solved simultaneous straight lines! Today, look what happens whenever TWO perpendicular measurements—like length and breadth—multiply together! "
            "Imagine a community committee planning a peaceful prayer hall carrying an exact floor carpet area of 300 square meters! Notice the architectural rule linking length and breadth: "
            "its length must measure ONE meter more than TWICE its breadth! Let breadth equal unknown variable x meters! Immediately length becomes (2x plus 1) meters! Remember rectangle area equals "
            "length multiplied by breadth: write x times (2x plus 1) equals 300! Expand brackets carefully right away: 2x squared plus x equals 300, or moving 300 across gives 2x squared plus x minus 300 equals zero! "
            "Pause and inspect that clean degree-two equation! Can linear rules solve x squared terms? Never! Solving areas, parabolic flights, right triangles, and business profits trains, and engineering budgets unlocks the dynamic curved world of Quadratic Equations—powerful degree two equations shaped across real world architectural geometry, curved projectile rocket motion paths, and exciting practical engineering problem solving!"
        ),
        "checkpoints": [
            {
                "question": "A rectangular prayer hall of carpet area 300 m² has length 1 m more than twice its breadth x. Which equation models this situation?",
                "options": [
                    "2x² + x − 300 = 0",
                    "x² + 2x − 300 = 0",
                    "2x² − x − 300 = 0",
                    "3x + 1 = 300"
                ],
                "answer": 0,
                "hint": "Breadth = x, length = 2x + 1, and Area = x(2x + 1) = 300!",
                "explanation": "Expanding x(2x + 1) = 300 gives 2x² + x = 300 ⟹ 2x² + x − 300 = 0."
            },
            {
                "question": "Testing breadth x = 12 m inside 2x² + x − 300 = 0 confirms:",
                "options": [
                    "2(144) + 12 − 300 = 288 + 12 − 300 = 0 (so breadth = 12 m and length = 25 m!)",
                    "2(144) + 12 − 300 = 12 ≠ 0",
                    "Breadth = 25 m and length = 12 m",
                    "Area = 150 m²"
                ],
                "answer": 0,
                "hint": "Plug x = 12 into 2x + 1 and check 12 × 25!",
                "explanation": "At x = 12 m, length = 2(12) + 1 = 25 m, and carpet area = 12 × 25 = 300 m² cleanly."
            }
        ]
    },
    {
        "id": 2,
        "title": "Quadratic History Timeline",
        "subtitle": "From Ancient Babylonians & Euclid to Brahmagupta, Sridharacharya, Al-Khwarizmi & Europe",
        "speech": (
            "Before solving degree-two puzzles algebraically, travel swiftly across four thousand years of brilliant human discovery behind quadratic equations! Long before modern x and y symbols existed, "
            "ancient Babylonian scribes solved rectangular land-area riddles on baked clay tablets—even knowing two numbers given their sum and product! Centuries later, Greek mathematician Euclid crafted clever geometric "
            "square-cutting methods to find hidden lengths geometrically! Next came golden breakthroughs across India: great Indian mathematician Brahmagupta (around AD 598 to 665) stated an explicit algebraic rule "
            "solving quadratic equations of the form ax squared plus bx equals c! Later, Indian scholar Sridharacharya (AD 1025) perfected the celebrated method of completing the square, giving us the famous explicit Quadratic Formula "
            "still named in his honor across Indian classrooms today! Simultaneously, brilliant Arab mathematician Al-Khwarizmi studied six standard quadratic forms systematically in Baghdad, giving mathematics the very word ALGEBRA from his book! "
            "Finally, European scholars like Abraham bar Hiyya spread complete unified quadratic solutions across medieval Europe, linking spatial geometric square puzzles and sleek symbolic algebra together forever! Understanding this rich global history helps us appreciate every bright algebraic theorem and classic formula you master step by step across this entire fascinating Class Ten algebra chapter!"
        ),
        "checkpoints": [
            {
                "question": "Which ancient Indian mathematician derived the explicit formula solving quadratic equations (widely called Sridharacharya's Formula), building on earlier work by Brahmagupta?",
                "options": [
                    "Sridharacharya (following Brahmagupta's earlier explicit rule)",
                    "Euclid of Alexandria",
                    "Al-Khwarizmi only",
                    "Carl Friedrich Gauss"
                ],
                "answer": 0,
                "hint": "Recall Section 4.1 noting ancient Indian pioneers Brahmagupta and Sridharacharya!",
                "explanation": "Brahmagupta gave an early explicit quadratic solution, and Sridharacharya perfected the completing-the-square Quadratic Formula."
            },
            {
                "question": "How did ancient Greek scholar Euclid primarily solve quadratic problems compared to Arab mathematician Al-Khwarizmi?",
                "options": [
                    "Euclid used geometric length/area constructions, whereas Al-Khwarizmi classified algebraic equation types systematically",
                    "Euclid used decimal calculators",
                    "Babylonians copied formulas from European printed books",
                    "Al-Khwarizmi proved x² cannot have positive roots"
                ],
                "answer": 0,
                "hint": "Check the chronological progression in Section 4.1: Babylonians -> Greek Euclid (geometric) -> Indian Brahmagupta/Sridharacharya -> Arab Al-Khwarizmi -> European texts!",
                "explanation": "Babylonians & Euclid framed quadratics via areas/lengths, while Indian and Arab mathematicians advanced explicit algebraic formulas."
            }
        ]
    },
    {
        "id": 3,
        "title": "Standard Quadratic Form",
        "subtitle": "Defining ax² + bx + c = 0 (a ≠ 0) With Real Coefficients and Descending Power Order",
        "speech": (
            "Now lock in the official mathematical definition from Section Four Point Two! ANY equation expressible in the standard descending-power form a x squared plus b x plus c equals zero, "
            "where a, b, and c are real numbers and leading coefficient a is STRICTLY NONZERO (a not equal to zero), is called a QUADRATIC EQUATION in variable x! Why is that tiny warning "
            "condition 'a not equal to zero' so fiercely important? Watch what happens if leading coefficient a ever drops down to zero: 0 times x squared vanishes completely, collapsing the entire expression "
            "down into b x plus c equals zero—merely a degree-one LINEAR equation! Notice meanwhile that middle coefficient b OR constant term c CAN happily equal zero! For instance, 2x squared minus 3 equals zero "
            "(here b equals zero) and 5x squared plus 7x equals zero (here c equals zero) are BOTH valid authentic quadratic equations because a stays nonzero! Furthermore, whenever terms arrive jumbled—such as "
            "1 minus 3x plus 4x squared equals zero—always arrange descending powers neatly (4x squared minus 3x plus 1 equals zero) cleanly before reading exact numbers for a, b, and c every single time without falling into sneaky reversed algebraic sign errors!"
        ),
        "checkpoints": [
            {
                "question": "In the standard quadratic equation ax² + bx + c = 0 (a, b, c ∈ ℝ), which single condition is STRICTLY mandatory?",
                "options": [
                    "a ≠ 0  (while b or c are allowed to equal 0)",
                    "b ≠ 0 and c ≠ 0 always",
                    "a, b, and c must all be positive integers",
                    "c can never be negative"
                ],
                "answer": 0,
                "hint": "Only the x² term defines degree 2; missing x or constant terms stay degree 2!",
                "explanation": "If a = 0, the x² term disappears and degree drops to 1 or 0; hence a ≠ 0 is the strict requirement."
            },
            {
                "question": "Arrange 7 − 4x = −5x² into standard form ax² + bx + c = 0 (with a > 0) and identify a, b, and c:",
                "options": [
                    "5x² − 4x + 7 = 0  (a = 5, b = −4, c = 7)",
                    "−5x² + 4x + 7 = 0  (a = 5, b = 4, c = 7)",
                    "5x² + 4x − 7 = 0  (a = 5, b = 4, c = −7)",
                    "7x² − 4x + 5 = 0  (a = 7, b = −4, c = 5)"
                ],
                "answer": 0,
                "hint": "Move −5x² across to the left side as +5x² cleanly!",
                "explanation": "Adding 5x² to both sides yields 5x² − 4x + 7 = 0, giving a = 5, b = −4, c = 7."
            }
        ]
    },
    {
        "id": 4,
        "title": "Disguised Equation Detector",
        "subtitle": "Expanding & Simplifying Expressions to Spot True Quadratics vs Cancellation Traps (Ex 4.1)",
        "speech": (
            "Never judge a mystery algebraic equation merely by glancing quickly at its brackets before expanding BOTH sides completely! Welcome to Exercise Four Point One's Disguised Equation Detector! "
            "Test Trap One: Look at (x minus 2)(x plus 1) equals (x minus 1)(x plus 3)! Many beginners spot parentheses multiplying x times x and declare 'Quadratic!' instantly! STOP and multiply both sides carefully! "
            "Left side expands into x squared minus x minus 2; right side expands into x squared plus 2x minus 3! Watch closely when you subtract x squared from both sides: x squared CANCELS x squared completely, leaving "
            "minus 3x plus 1 equals zero—purely LINEAR, NOT quadratic! Now inspect Trap Two on the opposite side: x cubed minus 4x squared minus x plus 1 equals (x minus 2) whole cubed! Seeing x cubed on the left, beginners shout 'Cubic!'—yet "
            "expanding (x minus 2) whole cubed produces x cubed minus 6x squared plus 12x minus 8! Both x cubed terms cancel cleanly out, leaving 2x squared minus 13x plus 9 equals zero—a disguised TRUE QUADRATIC carrying degree two! Expanding every expression cleanly saves students from falling right into common visual parenthesis cancellation traps across math exams!"
        ),
        "checkpoints": [
            {
                "question": "Check whether (x − 2)(x + 1) = (x − 1)(x + 3) simplifies into a quadratic equation (Exercise 4.1 Q1 iii):",
                "options": [
                    "No—expanding gives x² − x − 2 = x² + 2x − 3, where x² cancels leaving linear −3x + 1 = 0",
                    "Yes—simplifies to 2x² + x − 5 = 0",
                    "Yes—simplifies to x² − 3x + 1 = 0",
                    "No—it becomes degree 3 cubic"
                ],
                "answer": 0,
                "hint": "Expand BOTH sides completely and gather all terms onto one side!",
                "explanation": "Because +x² appears on both left and right sides, subtracting x² leaves degree-1 equation 3x − 1 = 0 (not quadratic)."
            },
            {
                "question": "Does x³ − 4x² − x + 1 = (x − 2)³ represent a quadratic equation (Exercise 4.1 Q1 viii)?",
                "options": [
                    "Yes! Expanding (x − 2)³ cancels x³ on both sides, simplifying cleanly to quadratic 2x² − 13x + 9 = 0",
                    "No—highest visible power is x³, so it stays cubic",
                    "No—both x³ and x² cancel leaving 0 = 9",
                    "Yes—it simplifies to x² − 8 = 0"
                ],
                "answer": 0,
                "hint": "Use (a − b)³ = a³ − 3a²b + 3ab² − b³ on (x − 2)³!",
                "explanation": "(x−2)³ = x³ − 6x² + 12x − 8. Canceling x³ yields 2x² − 13x + 9 = 0, a genuine quadratic equation!"
            }
        ]
    },
    {
        "id": 5,
        "title": "Marbles And Toys",
        "subtitle": "Modeling Marbles, Toy Production Costs, Consecutive Integers & Speed Into Quadratics",
        "speech": (
            "Now practice translating rich real-world textbook stories into crisp quadratic equations—watch carefully how ONE single unknown variable x models TWO connected numbers! Look at Textbook Example One Part One: "
            "Two young collectors together own 45 shiny glass marbles! Let Student A keep x marbles; instantly Student B holds (45 minus x) marbles! Both accidentally drop 5 marbles each while playing—leaving Student A with "
            "(x minus 5) marbles and Student B with (40 minus x) marbles! Now the riddle states the product of their remaining marbles equals 124: multiply (x minus 5) times (40 minus x) equals 124! Expanding neatly yields "
            "x squared minus 45x plus 324 equals zero! Look next at Part Two—cottage industry wooden toys: producing x toys on a certain day costs (55 minus x) rupees per toy, with total daily production bill 750 rupees! "
            "Multiplying x times (55 minus x) equals 750 produces x squared minus 55x plus 750 equals zero! Notice how consecutive positive integers whose product is 306 simply write x times (x plus 1) equals 306 -> x squared plus x minus 306 equals zero! Notice how easily clear variable definitions convert word stories into clean degree two equations!"
        ),
        "checkpoints": [
            {
                "question": "Two students together own 45 marbles. After losing 5 marbles each, the product of their remaining marbles is 124. If Student A started with x marbles, which equation results?",
                "options": [
                    "x² − 45x + 324 = 0",
                    "x² + 45x − 324 = 0",
                    "x² − 40x + 124 = 0",
                    "x² − 55x + 324 = 0"
                ],
                "answer": 0,
                "hint": "Expand (x − 5)(45 − x − 5) = (x − 5)(40 − x) = 124!",
                "explanation": "40x − x² − 200 + 5x = 124 ⟹ −x² + 45x − 324 = 0 ⟹ x² − 45x + 324 = 0 (roots: 36 and 9)."
            },
            {
                "question": "The product of two consecutive positive integers is 306 (Exercise 4.1 Q2 ii). Letting the smaller integer be x, which quadratic finds x?",
                "options": [
                    "x² + x − 306 = 0  (solving to integers 17 and 18)",
                    "x² + 2x − 306 = 0",
                    "2x + 1 = 306",
                    "x² − x − 306 = 0  (smaller x = 18)"
                ],
                "answer": 0,
                "hint": "Two consecutive integers are x and x + 1, so x(x + 1) = 306!",
                "explanation": "x(x + 1) = 306 ⟹ x² + x − 306 = 0, factoring as (x + 18)(x − 17) = 0 ⟹ positive x = 17, x + 1 = 18."
            }
        ]
    },
    {
        "id": 6,
        "title": "Zeroes Equal Roots",
        "subtitle": "Connecting Polynomial Zeroes (p(α) = 0) Identically to Equation Roots (ax² + bx + c = 0)",
        "speech": (
            "Pause cleanly right here as we cross into Section Four Point Three: Solution of a Quadratic Equation by Factorisation! Notice two slightly different vocabulary words students hear across Chapter Two and Chapter Four: "
            "in Chapter Two, we searched for ZEROES of a quadratic POLYNOMIAL p(x) equal to a x squared plus b x plus c; now in Chapter Four, we solve for ROOTS (or SOLUTIONS) of the quadratic EQUATION a x squared plus b x plus c "
            "equals zero! Wait: are 'zeroes' and 'roots' completely different objects, or exact twin cousins? Let us test number x equals 1 inside 2x squared minus 3x plus 1! Plugging x equals 1 gives 2(1) minus 3(1) plus 1 equaling ZERO! "
            "Because output p(1) equals zero, x equals 1 is a ZERO of polynomial 2x squared minus 3x plus 1—AND simultaneously, because Left-Hand Side matches Right-Hand Side zero cleanly, x equals 1 is a ROOT (solution) of equation "
            "2x squared minus 3x plus 1 equals zero! Thus, for any real number alpha: alpha is a root of ax squared plus bx plus c equals zero IF AND ONLY IF alpha is a zero of polynomial ax squared plus bx plus c! Every quadratic equation owns at most TWO roots!"
        ),
        "checkpoints": [
            {
                "question": "How do the 'roots' of quadratic equation ax² + bx + c = 0 compare to the 'zeroes' of quadratic polynomial p(x) = ax² + bx + c?",
                "options": [
                    "They are the EXACT same real numbers α satisfying aα² + bα + c = 0",
                    "Roots are always negative while zeroes are positive",
                    "Zeroes are y-intercepts while roots are x² coefficients",
                    "A quadratic equation has 3 roots whereas the polynomial has 2 zeroes"
                ],
                "answer": 0,
                "hint": "Substituting x = α makes p(α) = 0—both terms refer to the identical values!",
                "explanation": "Real number α is a root/solution of ax² + bx + c = 0 if and only if α is a zero of p(x) = ax² + bx + c."
            },
            {
                "question": "Test which number below is a genuine root of the quadratic equation 2x² − 5x + 3 = 0:",
                "options": [
                    "x = 1  (check: 2(1)² − 5(1) + 3 = 0)  and  x = 3/2",
                    "x = −1  (check: 2 + 5 + 3 = 10)",
                    "x = 2",
                    "x = 0"
                ],
                "answer": 0,
                "hint": "Quick rule: whenever coefficients sum to zero (a + b + c = 2 − 5 + 3 = 0), x = 1 is automatically a root!",
                "explanation": "Plugging x = 1 yields 2 − 5 + 3 = 0, and plugging x = 3/2 yields 2(9/4) − 15/2 + 3 = 9/2 − 15/2 + 6/2 = 0."
            }
        ]
    },
    {
        "id": 7,
        "title": "Factoring Middle Term",
        "subtitle": "Finding Quadratic Roots via Middle-Term Splitting Into Linear Factors (Exercise 4.2)",
        "speech": (
            "Now put middle-term splitting straight to work cracking quadratic equations cleanly into two linear brackets! Examine Textbook Example Three: 2x squared minus 5x plus 3 equals zero! Multiply outer numbers a times c: 2 times 3 equals plus 6! "
            "Find two numbers multiplying to plus 6 whose sum matches middle b (minus 5): immediately minus 2 and minus 3 fit cleanly! Split minus 5x into minus 2x minus 3x, factor pairs cleanly into 2x(x minus 1) minus 3(x minus 1), giving factored form "
            "(2x minus 3)(x minus 1) equals zero! Remember the Zero-Product Principle: whenever two numbers multiply to zero, AT LEAST ONE factor MUST equal zero! Setting 2x minus 3 equal to zero yields root 3 over 2, while setting x minus 1 equal to zero "
            "yields root 1! Now inspect Textbook Example Five: 3x squared minus 2 root 6 x plus 2 equals zero, or Exercise Four Point Two's 100x squared minus 20x plus 1 equals zero! Notice 100x squared minus 20x plus 1 factors tightly into (10x minus 1)(10x minus 1) "
            "equals zero—yielding TWO EQUAL REPEATED ROOTS: 1 over 10 and 1 over 10 cleanly in just a few bright steps without confusion!"
        ),
        "checkpoints": [
            {
                "question": "Solve 6x² − x − 2 = 0 (Textbook Example 4) cleanly by splitting the middle term:",
                "options": [
                    "x = 2/3  and  x = −1/2  [factors: (3x − 2)(2x + 1) = 0]",
                    "x = −2/3  and  x = 1/2",
                    "x = 3/2  and  x = −2",
                    "x = 4  and  x = −3"
                ],
                "answer": 0,
                "hint": "a·c = 6 × (−2) = −12 and b = −1 -> split −x = −4x + 3x!",
                "explanation": "6x² + 3x − 4x − 2 = 3x(2x + 1) − 2(2x + 1) = (3x − 2)(2x + 1) = 0 ⟹ roots 2/3 and −1/2."
            },
            {
                "question": "Factor 100x² − 20x + 1 = 0 (Exercise 4.2 Q1 v). What are its exact roots?",
                "options": [
                    "Two equal repeated roots: x = 1/10 and x = 1/10  [(10x − 1)² = 0]",
                    "x = 10 and x = 10",
                    "x = 1/10 and x = −1/10",
                    "No real roots"
                ],
                "answer": 0,
                "hint": "Recognize perfect square (10x)² − 2(10x)(1) + 1² = 0!",
                "explanation": "(10x − 1)(10x − 1) = 0 sets 10x − 1 = 0 twice, yielding repeated roots 1/10 and 1/10."
            }
        ]
    },
    {
        "id": 8,
        "title": "Radical Quadratic Factoring",
        "subtitle": "Splitting Square-Root Middle Terms cleanly: 3x² − 2√6x + 2 = 0 and √2x² + 7x + 5√2 = 0",
        "speech": (
            "Square roots appearing inside middle-term splitting problems often intimidate students until one neat trick shines light everywhere! Inspect Textbook Example Five: 3x squared minus 2 root 6 x plus 2 equals zero! "
            "Multiply a times c first: 3 times 2 equals plus 6! Wait—which two identical-radical numbers multiply to positive 6 and add together cleanly to minus 2 root 6? Think: minus root 6 times minus root 6 equals PLUS 6, "
            "and minus root 6 plus (minus root 6) equals minus 2 root 6! Split cleanly: 3x squared minus root 6 x minus root 6 x plus 2 equals zero! Remember 3 equals root 3 times root 3, root 6 equals root 3 times root 2, "
            "and 2 equals root 2 times root 2! Pull root 3 x out of the first pair and minus root 2 out of the second pair: (root 3 x minus root 2) whole squared equals zero, gifting equal roots root(2/3) and root(2/3)! "
            "Similarly on Exercise Four Point Two's root 2 x squared plus 7x plus 5 root 2 equals zero: a times c equals root 2 times 5 root 2 equaling 10—splitting 7x cleanly into 2x plus 5x and factoring neatly!"
        ),
        "checkpoints": [
            {
                "question": "In solving 3x² − 2√6x + 2 = 0 by middle-term splitting, what two terms cleanly split −2√6x?",
                "options": [
                    "−√6x and −√6x  (since (−√6)(−√6) = +6 = a·c, giving (√3x − √2)² = 0 -> roots √(2/3), √(2/3))",
                    "−2x and −√6x",
                    "−3x and +2x",
                    "+√6x and −3√6x"
                ],
                "answer": 0,
                "hint": "Recall a·c = 3 × 2 = 6, and √6 × √6 = 6!",
                "explanation": "Splitting −2√6x = −√6x − √6x factors into (√3x − √2)(√3x − √2) = 0, yielding repeated root √(2/3)."
            },
            {
                "question": "Solve Exercise 4.2 Q1(iii) √2x² + 7x + 5√2 = 0 cleanly by splitting 7x (note √2 × 5√2 = 10):",
                "options": [
                    "x = −√2  and  x = −5/√2  [factors: (√2x + 5)(x + √2) = 0]",
                    "x = √2  and  x = 5/√2",
                    "x = −2  and  x = −5",
                    "x = −5√2  and  x = −1"
                ],
                "answer": 0,
                "hint": "Split 7x into 2x + 5x, and remember 2 = √2 × √2 when factoring!",
                "explanation": "√2x² + 2x + 5x + 5√2 = √2x(x + √2) + 5(x + √2) = (x + √2)(√2x + 5) = 0 ⟹ roots −√2 and −5/√2."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch4 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

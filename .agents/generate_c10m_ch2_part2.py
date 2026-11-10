#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 2: Polynomials
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Degree Zero Bound",
        "subtitle": "General Rule: A Polynomial of Degree n Intersects the x-Axis at Most n Times",
        "speech": (
            "Pause cleanly right here and collect all visual clues uncovered across linear lines, quadratic parabolas, and twisting cubic curves into one shining universal rule of Section Two Point Two! "
            "Linear degree ONE intersected the x-axis once; quadratic degree TWO intersected two, one, or zero times; cubic degree THREE intersected three, two, or one times! Look at the crisp universal pattern: "
            "In general, given a polynomial p(x) of degree n, the graph of y equals p(x) intersects the x-axis at AT MOST n points! Therefore, a polynomial p(x) of degree n has AT MOST n real zeroes! "
            "Let us also tackle Exercise Two Point One right visually! Imagine inspecting six mysterious curves on screen without even knowing their algebraic equations: counting simply how many sharp or smooth places each curve "
            "crosses or touches the horizontal x-axis—ignoring y-axis crossings completely!—tells you instantly the exact number of real zeroes! Wait: watch two classic traps! First, a flat horizontal line hovering parallel above "
            "the x-axis has ZERO zeroes! Second, a wavy W-shaped curve slicing down, up, down, and up across the x-axis four distinct times reveals FOUR zeroes, meaning its degree MUST be at least four—never linear, quadratic, or cubic! Always count horizontal x-axis intersections carefully!"
        ),
        "checkpoints": [
            {
                "question": "If the graph of y = p(x) intersects the x-axis at 3 points and crosses the vertical y-axis at 1 point, how many zeroes does p(x) have?",
                "options": [
                    "3 zeroes (only horizontal x-axis intersections count as zeroes of p(x))",
                    "4 zeroes (counting both x and y intercepts)",
                    "1 zero",
                    "0 zeroes"
                ],
                "answer": 0,
                "hint": "Remember zeroes occur where y = p(x) = 0, i.e., exclusively on the x-axis!",
                "explanation": "A y-axis intersection gives p(0), not p(x) = 0 (unless it passes through origin (0, 0)). Only x-axis crossings determine the count of zeroes: 3."
            },
            {
                "question": "By the general degree rule, what is the MAXIMUM number of real zeroes a polynomial of degree 5 can possibly have?",
                "options": [
                    "At most 5 real zeroes",
                    "Always 6 real zeroes",
                    "Infinite zeroes",
                    "At most 2 real zeroes"
                ],
                "answer": 0,
                "hint": "Degree n implies at most n zeroes!",
                "explanation": "A polynomial of degree n intersects the x-axis at at most n points, giving at most 5 zeroes when n = 5."
            }
        ]
    },
    {
        "id": 10,
        "title": "Quadratic Sum Product",
        "subtitle": "Deriving α + β = −b/a and αβ = c/a Directly From Factored Form k(x − α)(x − β)",
        "speech": (
            "Now step into Section Two Point Three: uncovering the stunning hidden algebra connecting the ZEROES of a polynomial right to its COEFFICIENTS! You already know linear polynomial a x plus b owns single zero minus b over a! "
            "What about quadratic polynomial p(x) equals a x squared plus b x plus c (where a is nonzero) possessing two zeroes alpha and beta? By the Factor Theorem from Class Nine, since alpha and beta make p(x) equal zero, "
            "(x minus alpha) and (x minus beta) MUST both be factors of p(x)! Therefore, we write p(x) equal to constant k times (x minus alpha) times (x minus beta)! Expand brackets neatly: k times [x squared minus (alpha plus beta)x plus alpha times beta], "
            "equaling k x squared minus k(alpha plus beta)x plus k alpha beta! Now match coefficients term by term directly against a x squared plus b x plus c! Comparing x squared terms gives a equals k; comparing x terms gives b equals minus a(alpha plus beta); "
            "and comparing constant terms gives c equals a alpha beta! Solving cleanly gifts us two golden formulas: sum of zeroes alpha plus beta equals minus b over a, and product alpha beta equals c over a!"
        ),
        "checkpoints": [
            {
                "question": "For quadratic polynomial p(x) = ax² + bx + c (a ≠ 0) with zeroes α and β, what are the exact formulas for sum (α + β) and product (αβ)?",
                "options": [
                    "α + β = −b/a   and   αβ = c/a",
                    "α + β = b/a   and   αβ = −c/a",
                    "α + β = −c/a   and   αβ = b/a",
                    "α + β = a/b   and   αβ = a/c"
                ],
                "answer": 0,
                "hint": "Remember the minus sign sits on the SUM (−b/a), while PRODUCT stays positive (+c/a)!",
                "explanation": "Equating ax² + bx + c = a[x² − (α+β)x + αβ] directly establishes α + β = −b/a and αβ = c/a."
            },
            {
                "question": "Without even finding individual roots of 3x² − 12x + 7 = 0, determine the exact sum and product of its zeroes α and β:",
                "options": [
                    "Sum = 4  and  Product = 7/3",
                    "Sum = −4  and  Product = 7/3",
                    "Sum = 12  and  Product = 7",
                    "Sum = −12/7  and  Product = 3/7"
                ],
                "answer": 0,
                "hint": "Identify a = 3, b = −12, c = 7 carefully—watch the double negative in −b/a!",
                "explanation": "α + β = −(−12)/3 = +4, and αβ = 7/3."
            }
        ]
    },
    {
        "id": 11,
        "title": "Middle Term Factoring",
        "subtitle": "Finding Zeroes by Splitting the Middle Term and Verifying Coefficients Step by Step",
        "speech": (
            "Now put those formulas into crisp action solving Textbook Example Two and Exercise Two Point Two problems using middle-term splitting! Look at p(x) equals x squared plus 7x plus 10! "
            "We hunt for two integers whose product equals a times c (here 1 times 10 equals 10) and whose sum equals middle coefficient b (here 7)! Instantly 5 and 2 shine brightly: 5 plus 2 equals 7 and 5 times 2 equals 10! "
            "Split 7x cleanly into 2x plus 5x, group pairs smoothly into (x plus 2) times (x plus 5), and set equal to zero to obtain exact zeroes alpha equals minus 2 and beta equals minus 5! Now perform the official verification step: "
            "compute sum directly: minus 2 plus (minus 5) equals minus 7—matching minus b over a equal to minus 7 over 1! Compute product directly: minus 2 times minus 5 equals plus 10—matching c over a equal to 10 over 1! "
            "Watch one classic trap from Exercise Two Point Two: 6x squared minus 3 minus 7x! Always rearrange terms cleanly in descending power order—6x squared minus 7x minus 3—BEFORE identifying a equals 6, b equals minus 7, c equals minus 3!"
        ),
        "checkpoints": [
            {
                "question": "In Exercise 2.2 Q1(iii), before identifying coefficients a, b, c of 6x² − 3 − 7x, why must you rearrange the polynomial first?",
                "options": [
                    "Writing standard order 6x² − 7x − 3 clearly assigns b = −7 (coeff of x) and c = −3 (constant), avoiding swapping b and c!",
                    "Because descending powers change actual roots of the polynomial",
                    "Because 3 must always be positive before factoring",
                    "Rearranging removes the x² term"
                ],
                "answer": 0,
                "hint": "Notice −3 sits in the middle position! Standard form places bx before c.",
                "explanation": "Standard form ax² + bx + c reveals a = 6, b = −7, c = −3 cleanly, factoring into (3x + 1)(2x − 3) with zeroes −1/3 and 3/2."
            },
            {
                "question": "Verify the zeroes of x² − 2x − 8 (Exercise 2.2 Q1): what are the zeroes and their verified sum/product?",
                "options": [
                    "Zeroes 4 and −2; Sum = 2 (= −(−2)/1) and Product = −8 (= −8/1)",
                    "Zeroes −4 and 2; Sum = −2 and Product = −8",
                    "Zeroes 4 and 2; Sum = 6 and Product = 8",
                    "Zeroes −4 and −2; Sum = −6 and Product = 8"
                ],
                "answer": 0,
                "hint": "Split −2x = −4x + 2x giving (x − 4)(x + 2)!",
                "explanation": "x² − 2x − 8 = (x − 4)(x + 2) yields zeroes 4 and −2; 4 + (−2) = 2 = −b/a and 4 × (−2) = −8 = c/a."
            }
        ]
    },
    {
        "id": 12,
        "title": "Missing Term Quadratics",
        "subtitle": "Finding Zeroes & Verifying Coefficients When Linear Term b = 0 or Constant c = 0",
        "speech": (
            "What happens whenever a quadratic polynomial arrives missing its middle x-term (meaning b equals zero), OR missing its constant number (meaning c equals zero)? Beginners often freeze wondering how to split "
            "missing middle terms—yet these turn out to be the FASTEST quadratics of all! Examine missing-b Example Three: x squared minus 3! Notice b equals zero and c equals minus 3! Do NOT split middle terms; simply recall "
            "algebraic difference of squares: write 3 cleanly as square root of 3 whole squared! Immediately x squared minus (root 3) squared factors into (x minus root 3) times (x plus root 3), gifting symmetrical zeroes plus root 3 and minus root 3! "
            "Check coefficients rapidly: sum equals root 3 plus (minus root 3) equals ZERO—matching minus 0 over 1! Product equals minus 3—matching minus 3 over 1! Next inspect missing-c Exercise Two Point Two: 4 u squared plus 8 u! "
            "Simply pull greatest common factor 4 u completely outside brackets: 4 u times (u plus 2) equal to zero! Immediately either u equals 0 or u equals minus 2—sum minus 2 matches minus 8 over 4, and product 0 matches 0 over 4! Never divide away variable u, or you accidentally hide zero root u equals 0!"
        ),
        "checkpoints": [
            {
                "question": "Find the zeroes of quadratic polynomial x² − 3 (Textbook Example 3) using a² − b² factorization:",
                "options": [
                    "√3 and −√3 (with sum 0 = −0/1 and product −3 = −3/1)",
                    "3 and −3",
                    "√3 and 0",
                    "1 and −3"
                ],
                "answer": 0,
                "hint": "Rewrite x² − 3 cleanly as x² − (√3)²!",
                "explanation": "x² − (√3)² = (x − √3)(x + √3) gives zeroes √3 and −√3, verifying α + β = 0 = −b/a and αβ = −3 = c/a."
            },
            {
                "question": "What is the quickest method to find the zeroes of 4u² + 8u (Exercise 2.2 Q1 iv) where constant term c = 0?",
                "options": [
                    "Factor out 4u cleanly: 4u(u + 2) = 0, yielding zeroes u = 0 and u = −2",
                    "Subtract 8 from both sides and divide by 4u",
                    "Use √8 and −√8 as zeroes",
                    "Because c = 0, there are no real zeroes"
                ],
                "answer": 0,
                "hint": "Never divide away variable u (which hides root u = 0); factor common 4u outside!",
                "explanation": "4u(u + 2) = 0 gives u = 0 and u = −2; sum = −2 = −8/4 and product = 0 = 0/4."
            }
        ]
    },
    {
        "id": 13,
        "title": "Building Quadratic Polynomials",
        "subtitle": "Constructing p(x) = k[x² − (Sum)x + Product] Directly From Given Zero Data",
        "speech": (
            "Suppose now we reverse the direction! Instead of breaking down an already-written quadratic polynomial to discover its zeroes, someone hands you ONLY the SUM S equal to alpha plus beta, and the PRODUCT P equal to alpha beta, "
            "asking you to construct the matching quadratic polynomial cleanly! Watch how smoothly our factored identity builds ANY quadratic backward! Recall every quadratic polynomial sharing zeroes alpha and beta writes neatly in scaled form "
            "k times [x squared minus (alpha plus beta)x plus alpha beta], where k is any nonzero real constant! Notice that crucial minus sign right in front of the sum S: x squared MINUS S x PLUS P! Test Textbook Example Four immediately: "
            "sum equals minus 3 and product equals 2! Plug S equals minus 3 and P equals 2 inside brackets: x squared minus (minus 3)x plus 2 equals x squared plus 3x plus 2 (taking k equals 1)! Now test fractional Exercise Two Point Two: sum equals 1 over 4, "
            "product equals minus 1! Plugging in gives x squared minus (1/4)x minus 1! Choosing smart multiplier k equals 4 clears ugly fraction denominators completely cleanly, gifting integer-coefficient beauty 4x squared minus x minus 4!"
        ),
        "checkpoints": [
            {
                "question": "Which general template constructs a quadratic polynomial whose sum of zeroes is S and product of zeroes is P?",
                "options": [
                    "k [ x² − Sx + P ]  (for any nonzero real constant k)",
                    "k [ x² + Sx + P ]",
                    "k [ x² − Px + S ]",
                    "k [ x² − Sx − P ]"
                ],
                "answer": 0,
                "hint": "Remember −b/a = S implies b/a = −S, putting a MINUS sign on the Sx term!",
                "explanation": "Expanding k(x − α)(x − β) gives k[x² − (α+β)x + αβ] = k[x² − Sx + P]."
            },
            {
                "question": "Construct a neat integer-coefficient quadratic polynomial whose sum of zeroes is 1/4 and product is −1 (Exercise 2.2 Q2 i):",
                "options": [
                    "4x² − x − 4",
                    "4x² + x − 4",
                    "x² − 4x − 1",
                    "4x² − x + 4"
                ],
                "answer": 0,
                "hint": "Plug S = 1/4 and P = −1 into k(x² − Sx + P), then pick k = 4 to clear fractions!",
                "explanation": "4(x² − (1/4)x − 1) = 4x² − x − 4 cleanly satisfies α + β = 1/4 and αβ = −4/4 = −1."
            }
        ]
    },
    {
        "id": 14,
        "title": "Cubic Zero Relations",
        "subtitle": "Extending Coefficient Relations to Cubic Polynomials: α+β+γ, αβ+βγ+γα & αβγ",
        "speech": (
            "Can this gorgeous dance between zeroes and polynomial coefficients step smoothly upwards into CUBIC polynomials of degree three? Watch how cleanly the exact same bracket expansion works for p(x) equals a x cubed plus b x squared plus c x plus d, "
            "where a is nonzero and zeroes are alpha, beta, and gamma! Write p(x) factored as k times (x minus alpha)(x minus beta)(x minus gamma), and multiply all three linear factors patiently! Gathering powers of x reveals three sparkling symmetric "
            "blocks: the x squared coefficient carries minus (alpha plus beta plus gamma); the x coefficient carries plus (alpha beta plus beta gamma plus gamma alpha); and the constant term carries minus (alpha beta gamma)! Look closely at the alternating "
            "signs reading left to right—MINUS, PLUS, MINUS! Thus matching coefficients yields all three cubic formulas cleanly: first, sum of single zeroes alpha plus beta plus gamma equals minus b over a; second, sum of pairwise products alpha beta plus beta gamma "
            "plus gamma alpha equals positive c over a; third, full triple product alpha beta gamma equals minus d over a! Notice how minus b over a, positive c over a, and minus d over a match linear and quadratic rules while extending smoothly!"
        ),
        "checkpoints": [
            {
                "question": "For cubic polynomial ax³ + bx² + cx + d (a ≠ 0) with zeroes α, β, γ, what equals the pairwise product sum (αβ + βγ + γα)?",
                "options": [
                    "+c / a",
                    "−b / a",
                    "−d / a",
                    "−c / a"
                ],
                "answer": 0,
                "hint": "Follow the alternating sign pattern from left to right: −b/a (singles), +c/a (pairs), −d/a (triple)!",
                "explanation": "Expanding a(x−α)(x−β)(x−γ) reveals the x coefficient equals +a(αβ+βγ+γα), so αβ+βγ+γα = c/a."
            },
            {
                "question": "For cubic p(x) = 2x³ + 6x² − 4x + 10, find α + β + γ and αβγ immediately without solving for α, β, γ:",
                "options": [
                    "α + β + γ = −3  and  αβγ = −5",
                    "α + β + γ = 3  and  αβγ = 5",
                    "α + β + γ = −2  and  αβγ = −10",
                    "α + β + γ = −3  and  αβγ = 5"
                ],
                "answer": 0,
                "hint": "Identify a = 2, b = 6, c = −4, d = 10 and apply −b/a and −d/a carefully!",
                "explanation": "α + β + γ = −6/2 = −3, and αβγ = −10/2 = −5."
            }
        ]
    },
    {
        "id": 15,
        "title": "Verifying Cubic Example",
        "subtitle": "Checking Zeroes 3, −1, −1/3 Inside 3x³ − 5x² − 11x − 3 and Verifying Coefficients",
        "speech": (
            "Let us test all three cubic formulas live step by step on Textbook Example Five! Here stands cubic polynomial p(x) equals 3x cubed minus 5x squared minus 11x minus 3, alongside three candidate numbers: 3, minus 1, and minus 1 over 3! "
            "Part One checks whether all three genuinely act as zeroes: evaluate p(3) equals 3(27) minus 5(9) minus 33 minus 3 equals 81 minus 45 minus 36 equals ZERO! Check p(minus 1) equals minus 3 minus 5 plus 11 minus 3 equals ZERO! "
            "Check p(minus 1/3) equals minus 1 over 9 minus 5 over 9 plus 11 over 3 minus 3 equals zero! Confirmed: alpha equals 3, beta equals minus 1, gamma equals minus 1 over 3! Part Two verifies every single cubic formula against a equals 3, b equals minus 5, "
            "c equals minus 11, d equals minus 3! Check Sum: 3 minus 1 minus 1/3 equals 5 over 3—matching minus b over a equals 5 over 3! Check Pairs: minus 3 plus 1/3 minus 1 equals minus 11 over 3—matching c over a! Check Triple Product: "
            "3 times (minus 1) times (minus 1/3) equals plus 1—matching minus d over a equals 3 over 3! Every relation balances cleanly!"
        ),
        "checkpoints": [
            {
                "question": "For p(x) = 3x³ − 5x² − 11x − 3 with zeroes 3, −1, −1/3, verify the triple product αβγ against −d/a:",
                "options": [
                    "3 × (−1) × (−1/3) = +1, matching −(−3)/3 = +1",
                    "3 × (−1) × (−1/3) = −1, matching d/a",
                    "Product equals −3",
                    "Product equals 5/3"
                ],
                "answer": 0,
                "hint": "Two negatives multiply to positive; check d = −3 and a = 3 in −d/a!",
                "explanation": "αβγ = 3 × (−1) × (−1/3) = +1, which equals −d/a = −(−3)/3 = +1."
            },
            {
                "question": "Verify the pairwise product sum (αβ + βγ + γα) for zeroes 3, −1, −1/3 against c/a of 3x³ − 5x² − 11x − 3:",
                "options": [
                    "−3 + 1/3 − 1 = −11/3, matching c/a = −11/3",
                    "−3 + 1/3 + 1 = −5/3",
                    "3 + 1 + 1/3 = 13/3",
                    "−11 only"
                ],
                "answer": 0,
                "hint": "Compute (3)(−1) + (−1)(−1/3) + (−1/3)(3) carefully!",
                "explanation": "−3 + 1/3 − 1 = −4 + 1/3 = −11/3 = c/a."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Two Summary",
        "subtitle": "Synthesizing Polynomial Degrees, Graphical Intercepts, Zero Bounds & Coefficient Laws",
        "speech": (
            "Bravo, young algebraists—you have unlocked every essential theorem and problem pattern across NCERT Class Ten Chapter Two: Polynomials! Let us crystallize four clear takeaways to carry smoothly into both Exercise quizzes ahead! "
            "First, Degree Classifications: linear (degree 1, ax plus b), quadratic (degree 2, ax squared plus bx plus c), and cubic (degree 3, ax cubed plus bx squared plus cx plus d) require whole-number exponents and nonzero leading coefficients! "
            "Second, Graphical Meaning: zeroes of y equals p(x) sit strictly along horizontal x-axis intersection coordinates! Linear lines cross once; quadratics trace upward (a positive) or downward (a negative) parabolas hitting the x-axis 2, 1, or 0 times; "
            "general degree-n curves cross at MOST n times! Third, Quadratic Coefficient Laws: sum alpha plus beta equals minus b over a, product alpha beta equals c over a, and constructing quadratics obeys k times [x squared minus S x plus P]! "
            "Fourth, Cubic Coefficient Laws follow alternating signs: minus b over a, positive c over a, and minus d over a! You are now completely prepared to solve graphs, factoring splits, coefficient checks, and cubic mysteries cleanly across every single exercise puzzle across Two Point One and Two Point Two calmly next!"
        ),
        "checkpoints": [
            {
                "question": "Suppose the sum of zeroes of quadratic kx² + 2x + 3k equals their product. What value must non-zero constant k take?",
                "options": [
                    "k = −2/3  (since −2/k = 3k/k = 3  ⟹  −2 = 3k)",
                    "k = 2/3",
                    "k = −3/2",
                    "k = 3"
                ],
                "answer": 0,
                "hint": "Set α + β = −b/a = −2/k equal to αβ = c/a = 3k/k = 3!",
                "explanation": "Equating −2/k = 3 yields k = −2/3 cleanly (nonzero, valid!)."
            },
            {
                "question": "Which statement correctly summarizes ALL key results of Chapter 2: Polynomials?",
                "options": [
                    "Degree n implies ≤ n real zeroes (x-intercepts); quadratic has α+β=−b/a, αβ=c/a; cubic has −b/a, +c/a, −d/a",
                    "A polynomial of degree n always has strictly n + 1 zeroes",
                    "Quadratic parabolas open upwards when a < 0",
                    "Cubic triple product αβγ equals +d/a without a minus sign"
                ],
                "answer": 0,
                "hint": "Verify degree bound, parabola sign, and alternating minus signs!",
                "explanation": "Degree n bounds real zeroes to ≤ n, parabolas cut x-axis at 0/1/2 points, and quadratic/cubic Vieta coefficient formulas follow exact signs."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch2 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

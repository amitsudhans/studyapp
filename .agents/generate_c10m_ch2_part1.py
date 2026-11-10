#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 2: Polynomials
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero human character names, zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Polynomial Degree Intro",
        "subtitle": "Recalling One-Variable Polynomials, Whole-Number Powers, and Linear/Quadratic/Cubic Degrees",
        "speech": (
            "Welcome, curious Class Ten mathematicians, to Chapter Two: Polynomials! Back in Class Nine, you discovered algebraic expressions built strictly from constants and whole-number powers "
            "of a single variable x! Remember the golden rule dividing genuine polynomials from imposter expressions: every exponent on variable x MUST be a non-negative whole integer—zero, one, two, "
            "three, and upward! Whenever x hides underneath a square root sign, inside a denominator like one over (x minus 1), or carries negative exponents, that expression is NOT a polynomial! "
            "Now inspect the DEGREE of a polynomial p(x): the highest power of x carrying a nonzero coefficient! Degree ONE defines a linear polynomial—such as 2x minus 3—where slope never equals zero! "
            "Degree TWO gives a quadratic polynomial a x squared plus b x plus c with nonzero a—like y squared minus 2! Degree THREE yields a cubic polynomial a x cubed plus b x squared plus c x plus d "
            "with nonzero leading coefficient a! Mastering degree classifications, coefficient identities, and polynomial division ideas opens the entire bridge linking pure algebra seamlessly to smooth curved coordinate geometry, coefficient laws, and polynomial division ideas throughout this exciting Class Ten mathematics chapter ahead cleanly and confidently!"
        ),
        "checkpoints": [
            {
                "question": "Which algebraic expression below is NOT a polynomial in one variable x?",
                "options": [
                    "x + 1/x  (or √x + 2, because exponents −1 and 1/2 are not whole numbers)",
                    "4x² − 3x + 7",
                    "√3 x² − 5x + 1",
                    "2x³ − x + 9"
                ],
                "answer": 0,
                "hint": "Check exponents on variable x: coefficients may be radicals (like √3), yet exponents on x MUST be whole numbers!",
                "explanation": "A polynomial allows irrational constant coefficients like √3, yet requires all variable exponents to be whole numbers {0, 1, 2, ...}."
            },
            {
                "question": "What is the exact degree of the polynomial p(x) = 3 − x² + 5x³ − 7x?",
                "options": [
                    "3 (making it a cubic polynomial)",
                    "2 (quadratic)",
                    "1 (linear)",
                    "5 (leading coefficient)"
                ],
                "answer": 0,
                "hint": "Find the HIGHEST exponent on x regardless of term order!",
                "explanation": "Arranging in descending powers gives 5x³ − x² − 7x + 3; highest exponent of x is 3 (cubic polynomial)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Value And Zeroes",
        "subtitle": "Evaluating p(k) and Connecting Linear Zero k = −b/a Directly to Coefficients",
        "speech": (
            "Suppose a friend hands you the polynomial p(x) equal to x squared minus 3x minus 4, and asks: what value does p(x) take when x equals 2? Simply substitute 2 everywhere x sits! "
            "We compute p(2) equals 2 squared minus 3 times 2 minus 4, equaling 4 minus 6 minus 4, giving minus 6! That resulting real number minus 6 is called the VALUE of p(x) at x equals 2! "
            "Now try plugging in x equals 4 or x equals minus 1 instead! Notice p(4) equals 16 minus 12 minus 4, collapsing right down to ZERO! Similarly, p(minus 1) equals 1 plus 3 minus 4, equaling ZERO! "
            "Any real number k such that p(k) equals zero is crowned a ZERO of the polynomial p(x)! Now spot a super neat algebraic link for ANY linear polynomial p(x) equals a x plus b (where a is nonzero): "
            "setting a k plus b equal to zero and solving directly yields k equals minus b divided by a—meaning minus (constant term) divided by (coefficient of x)! Thus EVERY linear polynomial a x plus b has ONE unique zero determined directly from its coefficients, laying our stepping-stone toward quadratic and cubic laws ahead!"
        ),
        "checkpoints": [
            {
                "question": "For polynomial p(x) = x² − 3x − 4, what is the value p(−1) and what does it tell us about −1?",
                "options": [
                    "p(−1) = (−1)² − 3(−1) − 4 = 0, so −1 is a ZERO of p(x)",
                    "p(−1) = −8, so −1 is not a zero",
                    "p(−1) = 4, making 4 the coefficient",
                    "p(−1) = −6"
                ],
                "answer": 0,
                "hint": "Evaluate (−1)² = +1 and −3(−1) = +3 carefully!",
                "explanation": "1 + 3 − 4 = 0! Whenever substituting x = k gives p(k) = 0, k is a zero of polynomial p(x)."
            },
            {
                "question": "Using the linear coefficient formula k = −b/a, what is the exact zero of p(x) = 3x + 7?",
                "options": [
                    "−7/3",
                    "7/3",
                    "−3/7",
                    "3/7"
                ],
                "answer": 0,
                "hint": "Set ax + b = 0 with a = 3 and b = 7!",
                "explanation": "Solving 3k + 7 = 0 gives k = −b/a = −7/3."
            }
        ]
    },
    {
        "id": 3,
        "title": "Linear Graph Zeroes",
        "subtitle": "Visualizing Straight Line y = ax + b Intersecting the x-Axis at (−b/a, 0)",
        "speech": (
            "Now step boldly from pure algebra onto our glowing coordinate plane to uncover what a 'zero' genuinely LOOKS like geometrically! Plot points for the linear polynomial y equals 2x plus 3! "
            "When x is minus 2, y equals minus 1; when x is 0, y sits at 3; when x is 2, y climbs to 7! Joining those points draws a ruler-straight continuous line slicing cleanly upwards across both grid axes! "
            "Watch carefully where that slanted line cuts right across the crisp horizontal x-axis anywhere across the entire endless real number line! Every single point resting flat on the x-axis owns y-coordinate ZERO! Setting y equal to zero inside y equals 2x plus 3 "
            "forces 2x plus 3 equal to zero, pinning the exact crossing point down to (minus 3 over 2, zero)—matching (minus b over a, zero) algebraically! Pause and verify the wonderful two-way bridge: "
            "algebraically, minus b over a makes p(x) equal zero; geometrically, minus b over a is the exact x-coordinate where the graph line intersects the x-axis! Therefore every non-horizontal linear polynomial y equals a x plus b "
            "intersects the x-axis at ONE and ONLY ONE unique crossing point—matching its exact single algebraic zero cleanly without ever curving back across!"
        ),
        "checkpoints": [
            {
                "question": "Geometrically, what do the zeroes of ANY polynomial y = p(x) correspond to on the Cartesian coordinate plane?",
                "options": [
                    "The x-coordinates of points where the graph y = p(x) intersects the x-axis",
                    "The y-intercept where the graph touches the vertical y-axis",
                    "The origin (0, 0) regardless of equation",
                    "Only points where x equals 1"
                ],
                "answer": 0,
                "hint": "Where on a graph does output height y = p(x) become equal to 0?",
                "explanation": "Since y = p(x), setting p(x) = 0 means y = 0—the exact points lying on the horizontal x-axis."
            },
            {
                "question": "At what exact coordinate point does the straight line y = 2x − 6 cross the x-axis?",
                "options": [
                    "(3, 0)",
                    "(−6, 0)",
                    "(0, 3)",
                    "(−3, 0)"
                ],
                "answer": 0,
                "hint": "Find −b/a where a = 2 and b = −6 (remember y = 0 on the x-axis)!",
                "explanation": "Solving 2x − 6 = 0 yields x = 6/2 = 3, so the line intersects the x-axis at (3, 0)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Up Down Parabolas",
        "subtitle": "Shaping Quadratic Curves y = ax² + bx + c: Upward (a > 0) vs Downward (a < 0) Parabolas",
        "speech": (
            "Now crank the polynomial degree up from one to TWO and watch straight lines bend smoothly into graceful U-shaped curves called PARABOLAS! Look at the general quadratic polynomial y equals a x squared plus b x plus c, "
            "where leading coefficient a is strictly nonzero! Try plotting points for y equals x squared minus 3x minus 4: far left at x equals minus 2, y climbs high to positive 6; sinking smoothly down through (minus 1, 0), "
            "(0, minus 4), and hitting bottom near x equals 1.5 before soaring back upwards symmetrically through (4, 0) and (5, 6)! Look carefully at that bright upward-opening U-cup! What controls whether a parabola opens UPWARDS "
            "like a smiling bowl or flips UPSIDE-DOWNWARDS like an umbrella roof? Strictly the algebraic sign of leading coefficient a! Whenever a is positive (greater than zero), positive squaring x squared pushes wings steeply upward forever, "
            "opening UPWARDS! Whenever a is negative (less than zero), say y equals minus x squared plus 4, negative coefficient flips wings downward—opening DOWNWARDS! Every quadratic graph shapes into an unmistakable graceful symmetric parabola curving cleanly upwards like a smiling valley or downwards like a tall arched rainbow bridge spanning smoothly across coordinates!"
        ),
        "checkpoints": [
            {
                "question": "What determines whether the parabola y = ax² + bx + c (a ≠ 0) opens upwards or downwards?",
                "options": [
                    "Leading coefficient a: opens upwards if a > 0, and opens downwards if a < 0",
                    "Constant term c alone",
                    "Middle coefficient b only",
                    "Every parabola opens sideways to the right"
                ],
                "answer": 0,
                "hint": "Think about what sign a·x² carries when |x| becomes very large!",
                "explanation": "For large |x|, the ax² term dominates y: when a > 0 both ends rise upward (∪); when a < 0 both ends drop downward (∩)."
            },
            {
                "question": "Which quadratic polynomial below draws a downward-opening parabola (∩)?",
                "options": [
                    "y = −2x² + 5x − 1",
                    "y = 3x² − 4x + 7",
                    "y = x² − 9",
                    "y = 0.5x² + 2"
                ],
                "answer": 0,
                "hint": "Look for a negative coefficient multiplying x²!",
                "explanation": "Only y = −2x² + 5x − 1 has a = −2 < 0, forcing its parabolic curve to open downwards."
            }
        ]
    },
    {
        "id": 5,
        "title": "Two Zero Parabolas",
        "subtitle": "Quadratic Case 1: Parabolas Cutting the x-Axis at Two Distinct Real Zeroes",
        "speech": (
            "Now examine all three possible geometric relationships between a quadratic parabola y equals a x squared plus b x plus c and the horizontal x-axis! Welcome to Case One: "
            "a parabola that slices cleanly across the x-axis at TWO DISTINCT points! Picture our earlier friend y equals x squared minus 3x minus 4! Because coefficient a equals plus 1, "
            "the parabola opens proudly upwards—yet its lowest bottom dip, called the vertex, drops below the x-axis down into negative y territory! Like a fearless submarine diving beneath the ocean surface "
            "and popping smoothly back up into sunlit air, a U-cup whose vertex sits below the x-axis MUST punch through y equals zero TWICE—once on the way down at A equals (minus 1, zero) and once rising back up at A prime "
            "equals (4, zero)! Notice how cleanly downwards-opening parabolas behave similarly: whenever a is negative and the peak crest rises above the x-axis—say y equals minus x squared plus 4—the arch crosses twice "
            "at (minus 2, zero) and (2, zero)! Therefore, in Quadratic Case One, the parabola slashes cleanly across two spots A and A prime, gifting polynomial p(x) EXACTLY TWO distinct real zeroes sitting symmetrically around the parabola axis!"
        ),
        "checkpoints": [
            {
                "question": "When a quadratic parabola y = ax² + bx + c cuts the x-axis at A(−1, 0) and A'(4, 0), how many distinct real zeroes does it have?",
                "options": [
                    "2 distinct zeroes (specifically x = −1 and x = 4)",
                    "1 zero only",
                    "0 zeroes",
                    "4 zeroes"
                ],
                "answer": 0,
                "hint": "Count the distinct x-intercepts where y = 0!",
                "explanation": "Each distinct intersection point with the x-axis corresponds to one distinct real zero—here two zeroes, −1 and 4."
            },
            {
                "question": "If an upward-opening parabola (a > 0) has its lowest vertex strictly BELOW the x-axis (y_vertex < 0), how many times does it cross the x-axis?",
                "options": [
                    "Twice (yielding 2 distinct real zeroes)",
                    "Never (0 zeroes)",
                    "Once only (1 coincident zero)",
                    "Three times"
                ],
                "answer": 0,
                "hint": "Starting below y = 0 and rising upward to +∞ on both left and right wings must pass y = 0 on each side!",
                "explanation": "Rising to +∞ on both wings from a vertex below y = 0 guarantees two distinct x-axis crossings (Case 1)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Touch Zero Parabolas",
        "subtitle": "Quadratic Case 2: Parabolas Grazing Tangent to the x-Axis at Exactly One Point",
        "speech": (
            "Now slide that dipping parabola smoothly upward until its bottom vertex rises right onto the x-axis itself—discovering Quadratic Case Two! Consider a classic square polynomial such as "
            "y equals x squared minus 4x plus 4, which factors neatly into (x minus 2) whole squared! Let us check heights carefully: at x equals 0, y equals 4; at x equals 1, y equals 1; at x equals 2, "
            "y kisses ZERO right on the x-axis; then at x equals 3, y rises immediately back to positive 1! Notice the curve descends gently down from above, barely touches the horizontal x-axis at ONE single point "
            "(2, zero) without ever crossing below into negative y values, and sweeps symmetrically back upwards! Think carefully: can two algebraic zeroes merge into ONE shared geometric point? YES! "
            "Two equal coincident points A and A prime coalesce smoothly into ONE point A! Even flipped upside down—say y equals minus (x plus 1) squared—an umbrella grazing y equals zero from underneath shares the exact same "
            "Case Two behavior: exactly ONE x-intercept, representing ONE single distinct repeated real zero! Notice how two separate intersection spots smoothly squeeze together into one exact shared tangent crossing!"
        ),
        "checkpoints": [
            {
                "question": "If a quadratic parabola gently touches the x-axis at exactly one point (2, 0) without crossing through, how many distinct x-intercepts does it have?",
                "options": [
                    "1 point (giving 1 zero, as in (x − 2)² = 0 where both algebraic roots coincide at x = 2)",
                    "2 distinct points",
                    "0 zeroes",
                    "3 zeroes"
                ],
                "answer": 0,
                "hint": "Two coincident roots merge geometrically into a single tangent touching point!",
                "explanation": "Case 2 occurs when the vertex sits right on the x-axis, cutting/touching the x-axis at exactly one point (one repeated real zero)."
            },
            {
                "question": "Which quadratic polynomial creates a Case 2 graph touching the x-axis at one single point?",
                "options": [
                    "y = x² − 6x + 9  [= (x − 3)²]",
                    "y = x² − 9",
                    "y = x² + 9",
                    "y = x² − 5x + 6"
                ],
                "answer": 0,
                "hint": "Look for a perfect square trinomial (x − k)²!",
                "explanation": "x² − 6x + 9 = (x − 3)² equals 0 solely at x = 3 and stays ≥ 0 everywhere else, grazing the x-axis at (3, 0) alone."
            }
        ]
    },
    {
        "id": 7,
        "title": "No Zero Parabolas",
        "subtitle": "Quadratic Case 3: Floating Parabolas Never Intersecting the x-Axis (Zero Real Zeroes)",
        "speech": (
            "Finally, lift that upward-opening parabola completely above the horizontal x-axis—or drop a downward-opening parabola completely underneath it—to observe Quadratic Case Three! Look at the crisp algebraic curve "
            "y equals x squared plus 1, or y equals minus x squared minus 4! Let us test plugging ANY real number anywhere from minus infinity to positive infinity into y equals x squared plus 1! Because squaring any real "
            "number never produces less than zero (x squared is always zero or positive), adding plus 1 guarantees y is ALWAYS at least positive 1—sitting strictly ABOVE the horizontal x-axis everywhere! No matter how wide "
            "left or right you trace that soaring bowl, the curve NEVER touches or cuts the x-axis anywhere! Similarly, an upside-down arch y equals minus x squared minus 2 stays strictly below minus 2—floating completely "
            "underneath the x-axis forever! Since zero intersection points exist along the horizontal x-axis, a Case Three quadratic polynomial has ZERO real zeroes! Gathering Cases One, Two, and Three together proves a quadratic "
            "polynomial has EITHER two, one, or zero real zeroes—meaning ALWAYS AT MOST two real zeroes—never three or more x-axis intersections anywhere anywhere along any single vertical quadratic parabola drawn vertically!"
        ),
        "checkpoints": [
            {
                "question": "Why does the parabola y = x² + 4 NEVER intersect the horizontal x-axis anywhere?",
                "options": [
                    "Because x² ≥ 0 for every real x, forcing y = x² + 4 ≥ 4 > 0 strictly above the x-axis (0 real zeroes)",
                    "Because its graph is a vertical straight line",
                    "Because x² becomes negative when x = −2",
                    "Because it crosses the x-axis at 3 hidden places"
                ],
                "answer": 0,
                "hint": "Can squaring a real number x ever yield −4 so that x² + 4 = 0?",
                "explanation": "With vertex at (0, 4) and a = +1 > 0 opening upward, the entire curve lies strictly above y = 0, yielding zero real zeroes."
            },
            {
                "question": "Across all three geometric cases (cutting twice, touching once, never touching), what is the exact range of possible real zeroes for any quadratic polynomial?",
                "options": [
                    "Either 2, 1, or 0 real zeroes (at most 2 zeroes)",
                    "Always strictly 2 zeroes without exception",
                    "Up to 3 zeroes",
                    "Infinitely many zeroes"
                ],
                "answer": 0,
                "hint": "Check Cases 1, 2, and 3 together!",
                "explanation": "A quadratic polynomial (degree 2) crosses the x-axis at 2, 1, or 0 points—never 3 or more—giving at most 2 real zeroes."
            }
        ]
    },
    {
        "id": 8,
        "title": "Cubic Curve Graphs",
        "subtitle": "Examining S-Shaped Cubic Curves y = x³ − 4x, y = x³, and y = x³ − x²",
        "speech": (
            "Now leap forward onto cubic curves of degree three and watch S-shaped roller coasters twist across our coordinate plane! Test three distinct textbook cubic curves side by side! "
            "First, plot y equals x cubed minus 4x! Factoring cleanly yields x times (x minus 2) times (x plus 2)—immediately predicting zero crossings at minus 2, zero, and plus 2! Visually, the graceful S-curve rises "
            "through (minus 2, zero), crests upward, dives cleanly through origin (0, zero), dips downward, and surges permanently upward through (2, zero)—intersecting the x-axis THREE distinct times! "
            "Second, inspect y equals x cubed itself: passing steeply through origin (0, zero) alone while hugging zero flatly at the middle—intersecting the x-axis at ONLY ONE single point (0, zero)! "
            "Third, examine y equals x cubed minus x squared equals x squared times (x minus 1): touching zero once at origin (0, zero) without crossing, then climbing through (1, zero)—intersecting at EXACTLY TWO points! "
            "Thus degree-three cubic curves possess 1, 2, or 3 real zeroes—meaning every cubic polynomial always has AT MOST 3 real zeroes! Notice the crystal-clear mathematical link connecting degree three strictly to at most three real zero crossings across the horizontal x-axis anywhere on screen!"
        ),
        "checkpoints": [
            {
                "question": "Look at the three textbook cubic curves: y = x³ − 4x, y = x³, and y = x³ − x². How many distinct x-intercepts does each have?",
                "options": [
                    "3 zeroes (at −2, 0, 2), 1 zero (at 0), and 2 zeroes (at 0, 1) respectively",
                    "All three cubic polynomials have strictly 3 distinct zeroes",
                    "None of them cross the x-axis (0 zeroes)",
                    "They have 4 zeroes each"
                ],
                "answer": 0,
                "hint": "Factor each expression cleanly: x(x−2)(x+2), x³, and x²(x−1)!",
                "explanation": "x(x−2)(x+2) cuts 3 times; x³ cuts 1 time; x²(x−1) touches at 0 and cuts at 1 (2 distinct x-intercepts)."
            },
            {
                "question": "Can a cubic polynomial y = ax³ + bx² + cx + d (a ≠ 0) EVER have 0 real zeroes across (−∞, +∞)?",
                "options": [
                    "No—odd-degree curves run from −∞ to +∞ (or reverse), crossing y = 0 at least once and at most 3 times",
                    "Yes, y = x³ + 5 never crosses the x-axis",
                    "Yes, cubic curves have up to 5 zeroes",
                    "Cubic graphs are always straight lines"
                ],
                "answer": 0,
                "hint": "Does x³ become huge positive for large +x and huge negative for large −x?",
                "explanation": "Every cubic curve sweeps from −∞ to +∞ (when a > 0), guaranteeing at least 1 real x-intercept and at most 3."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch2 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

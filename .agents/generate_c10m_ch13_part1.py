#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 13: Statistics
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Grouped Data Intro",
        "subtitle": "Section 13.1 Review: Ungrouped vs Grouped Distributions, Class IX Charts & Chapter Objectives",
        "speech": (
            "Welcome to NCERT Class Ten Chapter Thirteen: Statistics! In Class Nine, you organized raw numbers into ungrouped and grouped frequency distribution tables, drew bar graphs, histograms, and frequency polygons, and calculated Mean, Median, and Mode for small ungrouped lists of individual observations! "
            "In real world surveys covering thousands of school students, factory workers, or household electricity bills, listing every single number individually becomes impractical! Real world data arrives packed cleanly inside CLASS INTERVALS such as ten to twenty, twenty to thirty, and thirty to forty! "
            "So Chapter Thirteen extends all THREE central tendency measures—Mean, Median, and Mode—smoothly onto GROUPED frequency distributions! Plus, you will construct Less Than and More Than Cumulative Frequency distributions and plot cumulative curves called OGIVES to pinpoint medians visually! "
            "Remember what each statistical measure captures intuitively: MEAN equals the arithmetic balance average taking every single observation into account carefully; MODE identifies the single most popular peak repeating category; and MEDIAN pinpoints the exact positional middle score splitting ordered data cleanly into fifty percent below and fifty percent above! Explore every interactive table, ogive graph, and formula simulator ahead right now and let us master every single statistical calculation step by step!"
        ),
        "checkpoints": [
            {
                "question": "Which three core topics form the main extension in NCERT Class 10 Chapter 13 beyond Class IX ungrouped statistics?",
                "options": [
                    "Grouped Mean (Direct, Assumed, Step-Deviation), Grouped Mode, and Grouped Median via Cumulative Frequency",
                    "Only drawing pie charts and pictographs",
                    "Computing standard deviation and variance exclusively",
                    "Sorting single ungrouped lists without intervals"
                ],
                "answer": 0,
                "hint": "Recall Sections 13.2, 13.3, and 13.4!",
                "explanation": "Class 10 Chapter 13 extends Mean, Mode, and Median onto grouped class intervals along with Less Than / More Than cumulative distributions."
            },
            {
                "question": "Which measure of central tendency ALWAYS identifies the middlemost value when observations are sorted in ascending order?",
                "options": [
                    "Median",
                    "Mean",
                    "Mode",
                    "Class Mark"
                ],
                "answer": 0,
                "hint": "Splits ordered data into equal 50% lower and 50% upper halves!",
                "explanation": "Median represents the exact positional middle observation of ordered data."
            }
        ]
    },
    {
        "id": 2,
        "title": "Direct Mean Method",
        "subtitle": "Section 13.2: Class Marks (xᵢ = Midpoint) & Direct Method Formula x̄ = Σ(fᵢxᵢ) / Σfᵢ",
        "speech": (
            "Let us tackle Section Thirteen Point Two: Mean of Grouped Data, beginning cleanly with the Direct Method! "
            "Suppose a mathematics test scores table groups thirty students neatly into class intervals such as ten to twenty five, twenty five to forty, forty to fifty five, up to one hundred! Because individual test scores vanished once data got grouped, what single number stands in to represent ALL values inside each interval? "
            "We make ONE fundamental assumption: all frequencies inside a class interval behave as if centered strictly at its MIDPOINT, called the CLASS MARK! Compute Class Mark xᵢ cleanly as Upper Class Limit PLUS Lower Class Limit, divided by TWO! Check quickly: for interval 10 to 25, Class Mark xᵢ equals (10 + 25) / 2 equals 17.5! "
            "Now follow the Direct Method in THREE crisp tabular columns! Column One: compute every interval midpoint Class Mark xᵢ! Column Two: multiply each row frequency fᵢ by its midpoint xᵢ to form product fᵢ xᵢ! Column Three: add Σ fᵢ xᵢ completely and divide cleanly by Total Frequency Σ fᵢ! On NCERT Table 13.1 covering thirty students' marks, dividing 1,860 by 30 yields exact grouped Mean SIXTY TWO point zero cleanly!"
        ),
        "checkpoints": [
            {
                "question": "What is the Class Mark (xᵢ) of the grouped class interval 25 − 40?",
                "options": [
                    "32.5   [= (25 + 40) / 2]",
                    "15",
                    "30",
                    "65"
                ],
                "answer": 0,
                "hint": "Class Mark = (Lower Limit + Upper Limit) ÷ 2!",
                "explanation": "(25 + 40) / 2 = 65 / 2 = 32.5."
            },
            {
                "question": "In the Direct Method for grouped Mean x̄ = Σ(fᵢxᵢ) / Σfᵢ, if Σ(fᵢxᵢ) = 1,860 and total students Σfᵢ = 30, find the exact Mean:",
                "options": [
                    "62.0",
                    "59.3",
                    "60.5",
                    "64.0"
                ],
                "answer": 0,
                "hint": "Divide 1860 ÷ 30 cleanly!",
                "explanation": "1,860 / 30 = 62.0."
            }
        ]
    },
    {
        "id": 3,
        "title": "Assumed Mean Method",
        "subtitle": "Section 13.2 Time-Saver: Deviations dᵢ = xᵢ − a & x̄ = a + (Σfᵢdᵢ / Σfᵢ)",
        "speech": (
            "Notice ONE annoying arithmetic hurdle in the Direct Method whenever Class Marks xᵢ and frequencies fᵢ become large decimal numbers like 47.5, 92.5, or 1,250! Multiplying large fᵢ times xᵢ takes long error-prone vertical multiplication! "
            "Let us crush that arithmetic immediately with Method Two: the Assumed Mean Method! Pick ONE convenient central class mark near the middle of your frequency table and crown it as your Assumed Mean lowercase letter a! Check NCERT's exact same thirty student dataset: choosing a = 47.5 right near the middle shrinks every remaining number! "
            "Instead of multiplying large class marks xᵢ, compute small DEVIATIONS dᵢ = xᵢ minus a for every single row! Notice right at row a itself, deviation dᵢ equals ZERO! Rows above a give crisp negative numbers (−15, −30), while rows below give crisp positive numbers (+15, +30, +45)! "
            "Multiply each small frequency fᵢ times deviation dᵢ (almost always doable mentally in seconds!), add positive and negative terms cleanly to get Σ fᵢ dᵢ = +435, divide cleanly by Total Frequency Σ fᵢ = 30 to obtain +14.5, and finally add back your assumed baseline a = 47.5! Exact Mean equals 47.5 + 14.5 = SIXTY TWO—matching the Direct Method effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "Why does the Assumed Mean Method compute deviations dᵢ = xᵢ − a before multiplying by frequencies fᵢ?",
                "options": [
                    "To replace large class marks xᵢ with small centered numbers (plus a zero row) while preserving the exact Mean!",
                    "To change the final answer depending on which 'a' is picked",
                    "To eliminate the need for total frequency Σfᵢ",
                    "To convert grouped data into a mode"
                ],
                "answer": 0,
                "hint": "Notice adding 'a' at the end cancels subtracting 'a' inside dᵢ = xᵢ − a!",
                "explanation": "Centering around a near the middle makes fᵢdᵢ tiny; adding back a guarantees the exact same Mean."
            },
            {
                "question": "Using Assumed Mean a = 47.5, if Σ(fᵢdᵢ) = +435 and Σfᵢ = 30, find the exact Mean x̄:",
                "options": [
                    "62.0   (= 47.5 + 14.5)",
                    "47.5",
                    "33.0",
                    "59.3"
                ],
                "answer": 0,
                "hint": "First divide 435 ÷ 30 = 14.5, then add 47.5 + 14.5!",
                "explanation": "x̄ = 47.5 + (435/30) = 47.5 + 14.5 = 62.0."
            }
        ]
    },
    {
        "id": 4,
        "title": "Step Deviation Method",
        "subtitle": "Section 13.2 Super-Shortcut: uᵢ = (xᵢ − a)/h & x̄ = a + h × (Σfᵢuᵢ / Σfᵢ)",
        "speech": (
            "Can we shrink those deviations dᵢ even FURTHER whenever all class sizes share a clean common factor h? YES! Welcome to Method Three—the fastest board exam weapon in Section Thirteen Point Two: the Step Deviation Method! "
            "Examine NCERT Table 13.1 deviations dᵢ again: −30, −15, 0, +15, +30, +45! Notice EVERY single deviation divides cleanly by class size h = 15! "
            "So divide every dᵢ cleanly by h: define scaled step uᵢ = (xᵢ − a) divided by h! Watch what magic happens across the entire table: −30 becomes −2, −15 becomes −1, zero stays 0, +15 becomes +1, +30 becomes +2, and +45 becomes +3! "
            "Multiplying the table frequencies (2, 3, 7, 6, 6, 6) by tiny single-digit integers −2, −1, 0, 1, 2, 3 takes JUST FIVE SECONDS mentally with zero arithmetic mistakes! Sum Σ(fᵢuᵢ) = −4 − 3 + 0 + 6 + 12 + 18 = +29! Now plug smoothly into x̄ = a + h × (Σfᵢuᵢ / Σfᵢ): 47.5 + 15 × (29 / 30) = 47.5 + 14.5 = SIXTY TWO IDENTICALLY! Remember Step-Deviation shines brightest when all class intervals are equal in width—NEVER forget multiplying back by class size h!"
        ),
        "checkpoints": [
            {
                "question": "In Step-Deviation Method x̄ = a + h × (Σfᵢuᵢ / Σfᵢ), how is uᵢ defined and why must we multiply back by h?",
                "options": [
                    "uᵢ = (xᵢ − a)/h scales deviations down by factor h, so multiplying back by h restores original units!",
                    "uᵢ = (xᵢ + a) × h, and h subtracts outliers",
                    "h equals total frequency Σfᵢ",
                    "Multiplying by h is optional whenever h > 1"
                ],
                "answer": 0,
                "hint": "Division by h in defining uᵢ must be undone by multiplying by h in x̄!",
                "explanation": "Because uᵢ = (xᵢ − a)/h, x̄ = a + h(Σfᵢuᵢ / Σfᵢ) recovers exact unscaled deviations."
            },
            {
                "question": "Given Assumed Mean a = 150, common factor h = 20, Σfᵢ = 50, and Σ(fᵢuᵢ) = −12, compute the exact Mean:",
                "options": [
                    "145.2   [= 150 + 20×(−12/50)]",
                    "149.76",
                    "154.8",
                    "138.0"
                ],
                "answer": 0,
                "hint": "Compute 20 × (−12/50) = −240/50 = −4.8, then add to 150!",
                "explanation": "x̄ = 150 + 20×(−0.24) = 150 − 4.8 = 145.2."
            }
        ]
    },
    {
        "id": 5,
        "title": "Unequal Class Intervals",
        "subtitle": "Example 2 & Ex 13.1 Q7: Varying Class Widths & Choosing Common Divisor h Safely",
        "speech": (
            "Now inspect what happens when a grouped frequency table contains UNEQUAL class sizes, like Cricket Bowlers' wickets taken in Exercise Thirteen Point One Question Seven (20–60 width 40, 60–100 width 40, 100–150 width 50, 150–250 width 100, 250–350 width 100, and 350–450 width 100)! "
            "Student misconception alert! Many students panic thinking unequal class intervals break the grouped Mean formula! NOT AT ALL! First, Direct Method and Assumed Mean Method NEVER require equal class widths—simply compute each interval's OWN true midpoint xᵢ = (Lower Limit + Upper Limit) / 2 individually! "
            "Second, CAN you still apply Step-Deviation when class widths differ across rows? YES—as long as ALL deviations (xᵢ − a) share ANY convenient positive common factor h (or clean divisor like h = 20 or h = 5)! Check NCERT's Cricket Bowlers problem: class marks are 40, 80, 125, 200, 300, 400! Picking a = 200 gives deviations −160, −120, −75, 0, +100, +200! "
            "Using common divisor h = 20 gives clean step values −8, −6, −3.75, 0, 5, 10 (or choosing h = 5 keeps pure integers cleanly everywhere!), yielding the exact grouped Mean equal to 152.89 wickets identically across all three mean methods!"
        ),
        "checkpoints": [
            {
                "question": "If a grouped table has unequal class widths (e.g., width 40, 50, 100), how should you calculate class marks xᵢ and the Mean?",
                "options": [
                    "Calculate each row's exact own midpoint (L + U)/2, then apply Direct, Assumed Mean, or Step-Deviation with a common factor h",
                    "Force every row to have width 50 by changing frequencies",
                    "Unequal intervals cannot have a Mean",
                    "Only add the upper limits together"
                ],
                "answer": 0,
                "hint": "Every interval still has a valid midpoint regardless of width!",
                "explanation": "Each interval keeps its own midpoint (L+U)/2; Direct, Assumed, and common-factor Step-Deviation all yield the exact same Mean."
            },
            {
                "question": "In NCERT Example 2 (Rural School Teachers percentage with equal width h=10), if all three methods (Direct, Assumed, Step-Deviation) are run properly, how do their final Means compare?",
                "options": [
                    "All three methods produce the EXACT SAME Mean (39.71%)",
                    "Direct Method always gives a higher Mean",
                    "Step-Deviation divides the Mean by h",
                    "Assumed Mean changes depending on a"
                ],
                "answer": 0,
                "hint": "Step-Deviation and Assumed Mean are algebraic rewrites of the exact same Direct formula!",
                "explanation": "All three methods are algebraically equivalent and give the identical Mean 39.71%."
            }
        ]
    },
    {
        "id": 6,
        "title": "Missing Frequency Mean",
        "subtitle": "Exercise 13.1 Q3 Algebraic Solving: Daily Pocket Allowance With Mean = ₹18 (f = 20)",
        "speech": (
            "Now solve one of the top board exam classics in Exercise Thirteen Point One: Question Three, finding an UNKNOWN missing frequency when the grouped Mean is ALREADY given! "
            "Examine the daily pocket allowance survey: intervals 11–13 (f = 7), 13–15 (f = 6), 15–17 (f = 9), 17–19 (f = 13), 19–21 (unknown f!), 21–23 (f = 5), and 23–25 (f = 4)! The problem informs us: Mean daily pocket allowance equals EXACTLY EIGHTEEN RUPEES (₹18)! "
            "Step One: Compute every class mark xᵢ cleanly: 12, 14, 16, 18, 20, 22, 24! "
            "Step Two: Use Direct Method OR Assumed Mean centered right at a = 18 (watch why a = 18 is genius: at row 19–21, deviation dᵢ = 20 − 18 = 2, and Σfᵢ = 44 + f)! "
            "Let us verify Direct Method cleanly too: Sum of known frequencies equals 44, so Total Σfᵢ = 44 + f! Sum of known fᵢ xᵢ = 84 + 84 + 144 + 234 + 110 + 96 = 752, plus unknown 20f! Equate (752 + 20f) / (44 + f) = 18 ⟹ 752 + 20f = 792 + 18f ⟹ 2f = 40 ⟹ f = TWENTY!"
        ),
        "checkpoints": [
            {
                "question": "In the Daily Pocket Allowance problem (Ex 13.1 Q3), Mean = ₹18, known Σf = 44, known Σfx = 752, and unknown frequency f sits in class 19–21 (x = 20). Find f:",
                "options": [
                    "f = 20",
                    "f = 18",
                    "f = 16",
                    "f = 24"
                ],
                "answer": 0,
                "hint": "Solve (752 + 20f) / (44 + f) = 18!",
                "explanation": "752 + 20f = 792 + 18f ⟹ 2f = 40 ⟹ f = 20."
            },
            {
                "question": "Why is choosing Assumed Mean a = 18 even faster when solving Ex 13.1 Q3?",
                "options": [
                    "Because Mean x̄ = 18 equals a = 18, forcing Σ(fᵢdᵢ) directly equal to ZERO: −40 + 2f = 0 ⟹ f = 20!",
                    "Because a = 18 removes all frequencies",
                    "Because class width h becomes 10",
                    "Because 20 becomes zero"
                ],
                "answer": 0,
                "hint": "When Mean = a, (Σfᵢdᵢ / Σfᵢ) MUST equal 0!",
                "explanation": "If a = 18 equals given Mean 18, then Σ(fᵢdᵢ) = 0 directly gives −40 + 2f = 0 ⟹ f = 20."
            }
        ]
    },
    {
        "id": 7,
        "title": "Grouped Discontinuous Intervals",
        "subtitle": "Exercise 13.1 Q5: Inclusive Intervals (50–52, 53–55) — Continuous Gap Rule for Mean vs Mode/Median",
        "speech": (
            "Inspect Exercise Thirteen Point One Question Five—a tricky fruit market mango packing table with DISCONTINUOUS (inclusive) class intervals: 50–52, 53–55, 56–58, 59–61, and 62–64 mangoes per box! Notice a gap of ONE whole unit sits cleanly between upper limit 52 and the very next lower limit 53! "
            "Whenever you encounter boundary gaps between intervals, ALWAYS make classes continuous for Mode and Median calculations by subtracting HALF the gap (0.5) from every lower limit and adding HALF the gap (0.5) to every upper limit! That transforms 50–52 smoothly into continuous boundary 49.5–52.5 (giving true class width h = THREE, NEVER two!) and 53–55 into 52.5–55.5! "
            "Now inspect what happens to CLASS MARKS xᵢ for the grouped MEAN calculation! Compute midpoint BEFORE adjusting boundaries: (50 + 52) / 2 equals FIFTY ONE! Now compute midpoint AFTER adjusting boundaries: (49.5 + 52.5) / 2 equals 102 / 2 equals FIFTY ONE IDENTICALLY! "
            "Remember that golden board exam rule forever: Class Marks stay IDENTICAL with or without ±0.5 adjustment for MEAN, whereas adjusting boundaries IS strictly MANDATORY before computing Mode and Median! On Q5 mangoes, Step-Deviation delivers an exact grouped Mean equal to 57.19 mangoes per packed fruit box!"
        ),
        "checkpoints": [
            {
                "question": "Consider inclusive intervals 50–52, 53–55, 56–58 (Ex 13.1 Q5). What are the continuous boundaries and true class size (h) of 53–55?",
                "options": [
                    "52.5 − 55.5,   true class width h = 3",
                    "52.5 − 55.5,   true class width h = 2",
                    "53.0 − 55.0,   true class width h = 2",
                    "52.0 − 56.0,   true class width h = 4"
                ],
                "answer": 0,
                "hint": "Subtract 0.5 from 53 and add 0.5 to 55, then take Upper − Lower!",
                "explanation": "Continuous class is 52.5–55.5, so true class size h = 55.5 − 52.5 = 3."
            },
            {
                "question": "Why does adjusting discontinuous limits (50–52 → 49.5–52.5) leave grouped MEAN completely unchanged?",
                "options": [
                    "Because subtracting 0.5 and adding 0.5 cancels inside midpoint (L+U)/2, keeping every class mark xᵢ identical!",
                    "Because frequencies double cleanly",
                    "Because Mean ignores class marks",
                    "Because h changes from 2 to 3 inside Mean"
                ],
                "answer": 0,
                "hint": "Compare (50 + 52)/2 against (49.5 + 52.5)/2!",
                "explanation": "(49.5 + 52.5)/2 = 51 = (50 + 52)/2 identically."
            }
        ]
    },
    {
        "id": 8,
        "title": "Grouped Mode Formula",
        "subtitle": "Section 13.3: Modal Class (Maximum Frequency f₁) & Mode = l + [(f₁ − f₀)/(2f₁ − f₀ − f₂)] × h",
        "speech": (
            "Now conquer Section Thirteen Point Three: Mode of Grouped Data! In ungrouped data, Mode was simply the number appearing most frequently! Inside grouped data, we cannot see single values, so we first locate the MODAL CLASS—the interval holding the MAXIMUM FREQUENCY! "
            "How do we estimate the exact peak Mode inside that winning Modal Class? Memorize this crisp five-symbol formula with crystal precision: Mode equals l PLUS bracket open (f₁ minus f₀) divided by (2 f₁ minus f₀ minus f₂) bracket close, multiplied by class size h! "
            "Decode every single symbol cleanly: l equals Lower Limit of the modal class; h equals class size; f₁ equals frequency of the MODAL class (1 = winner!); f₀ equals frequency of the PRECEDING class just before it (0 comes before 1!); and f₂ equals frequency of the SUCCEEDING class right after it (2 comes after 1!)! "
            "Test NCERT Example Five (Family sizes survey): maximum frequency f₁ = 8 sits neatly in class 3–5 (lower limit l = 3, width h = 2), preceding class frequency f₀ = 7, succeeding class frequency f₂ = 2! Compute 3 + [(8 − 7) / (16 − 7 − 2)] × 2 = 3 + 2/7 = exact 3.286 family members!"
        ),
        "checkpoints": [
            {
                "question": "In the grouped Mode formula l + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h, what do f₀, f₁, and f₂ stand for?",
                "options": [
                    "f₁ = frequency of modal class (highest), f₀ = preceding class frequency, f₂ = succeeding class frequency",
                    "f₀ = lowest frequency overall, f₁ = total frequency, f₂ = cumulative frequency",
                    "f₁ = lower limit, f₀ = class width, f₂ = upper limit",
                    "f₀ = succeeding class, f₁ = preceding class, f₂ = modal class"
                ],
                "answer": 0,
                "hint": "Keep numeric order: 0 (before) → 1 (modal peak) → 2 (after)!",
                "explanation": "f₁ is the maximum frequency (modal class), flanked by f₀ before and f₂ after."
            },
            {
                "question": "For modal class 3 − 5 with f₁ = 8, preceding f₀ = 7, succeeding f₂ = 2, and h = 2 (NCERT Example 5), calculate the Mode:",
                "options": [
                    "3.286   [= 3 + (1/7)×2]",
                    "3.571",
                    "4.000",
                    "2.714"
                ],
                "answer": 0,
                "hint": "Substitute 3 + [(8−7) / (16−7−2)] × 2 = 3 + 2/7!",
                "explanation": "Mode = 3 + (1 / 7) × 2 = 3 + 0.286 = 3.286."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch13 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

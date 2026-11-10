#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 13: Statistics
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Applied Mode Problems",
        "subtitle": "Exercise 13.2 Applications: Comparing Mode vs Mean Meaning (Hospital Ages 36.8 vs 35.37 yr, Lifetimes 65.625 hr)",
        "speech": (
            "Now inspect real world Exercise Thirteen Point Two problems and understand NCERT's vital interpretive distinction comparing Mean against Mode! "
            "Check Question One: a hospital records ages of patients admitted during a year! Maximum frequency f₁ = 23 patients appears in interval 35–45 years (l = 35, h = 10), flanked by f₀ = 21 and f₂ = 14! Plugging straight into Mode formula gives 35 + [(23 − 21) / (46 − 21 − 14)] × 10 = 35 + 20/11 = THIRTY SIX POINT EIGHT YEARS! "
            "Meanwhile computing Mean gives THIRTY FIVE POINT THREE SEVEN YEARS! Look carefully at what BOTH numbers tell hospital doctors! The MODE 36.8 years shows that the maximum number of admitted patients belong near age 36.8 years (the modal peak age), whereas the MEAN 35.37 years states the average age across ALL admitted patients! "
            "Also note Question Two (225 Electrical Components lifetime survey): modal peak f₁ = 61 sits cleanly in 60–80 hours (preceding f₀ = 52, succeeding f₂ = 38, h = 20), yielding exact modal component lifetime SIXTY FIVE POINT SIX TWO FIVE HOURS! Watch one special edge case: if modal class sits in the VERY FIRST row, simply take f₀ = ZERO!"
        ),
        "checkpoints": [
            {
                "question": "In the hospital patient survey (Ex 13.2 Q1: Mode = 36.8 yrs, Mean = 35.37 yrs), how do you correctly interpret Mode vs Mean?",
                "options": [
                    "Maximum number of admitted patients are around age 36.8 yrs (Mode), whereas overall average age is 35.37 yrs (Mean)",
                    "Both always represent the exact same quantity",
                    "Mean gives maximum count while Mode averages extremes",
                    "Mode ignores frequencies"
                ],
                "answer": 0,
                "hint": "Mode highlights highest concentration/peak, Mean computes overall mathematical average!",
                "explanation": "Mode identifies the most common peak patient age (36.8 yr), while Mean reports overall average age (35.37 yr)."
            },
            {
                "question": "If the highest frequency f₁ happens to lie in the VERY FIRST class interval of a frequency table, what value should you take for f₀?",
                "options": [
                    "f₀ = 0",
                    "f₀ = f₁",
                    "f₀ = f₂",
                    "Mode cannot be defined"
                ],
                "answer": 0,
                "hint": "No class sits before the first row, so preceding frequency is zero!",
                "explanation": "When the first class is modal, its preceding class has frequency f₀ = 0 (similarly f₂ = 0 if last class is modal)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Less Than Cumulative",
        "subtitle": "Section 13.4 Foundations: Building 'Less Than' Cumulative Frequencies From Upper Class Limits & Reversing",
        "speech": (
            "Enter Section Thirteen Point Four: Median of Grouped Data! To pinpoint where the middle fifty percent score sits inside grouped classes, we first construct CUMULATIVE FREQUENCY DISTRIBUTIONS! Let us master Type One first: the LESS THAN type! "
            "How is a Less Than cumulative distribution built? Take EVERY UPPER CLASS LIMIT of your intervals as your boundary thresholds! Suppose intervals are 0–10 (5), 10–20 (3), 20–30 (4), 30–40 (3)! "
            "Ask steadily upward: How many students scored LESS THAN 10? Just 5! How many scored LESS THAN 20? Add both rows: 5 + 3 = 8! LESS THAN 30? Keep accumulating: 8 + 4 = 12! LESS THAN 40? 12 + 3 = 15 (matching total n)! Notice Less Than cumulative frequencies ALWAYS rise monotonically from bottom upward! "
            "Board Exam Alert! Frequently an exam question gives you ONLY the Less Than cumulative column directly (for example: below 20 years: 2, below 25 years: 6, below 30 years: 24 policy holders) and asks you to REVERSE smoothly back into normal class frequencies! Simply subtract consecutive cumulative counts carefully upward: f₂ = cf₂ − cf₁ = 6 − 2 = 4, and f₃ = 24 − 6 = 18!"
        ),
        "checkpoints": [
            {
                "question": "Which limits are always paired with a 'Less Than' cumulative frequency distribution table?",
                "options": [
                    "Upper Class Limits (accumulating frequencies upward to total n)",
                    "Lower Class Limits",
                    "Class Marks only",
                    "Modal differences"
                ],
                "answer": 0,
                "hint": "Saying 'less than 20' uses the upper limit of interval 10–20!",
                "explanation": "Less Than cumulative tables always pair Upper Class Limits with running cumulative totals."
            },
            {
                "question": "If a survey states: 'Below 20 years: 2 policy holders', 'Below 25 years: 6', and 'Below 30 years: 24' (Ex 13.3 Q3), what is the simple frequency (f) of class 25 − 30?",
                "options": [
                    "18   (= 24 − 6)",
                    "24",
                    "6",
                    "30"
                ],
                "answer": 0,
                "hint": "Subtract the cumulative count below 25 from the cumulative count below 30!",
                "explanation": "Those between 25 and 30 = (Below 30) − (Below 25) = 24 − 6 = 18."
            }
        ]
    },
    {
        "id": 11,
        "title": "More Than Cumulative",
        "subtitle": "Section 13.4 Foundations: Building 'More Than or Equal To' Cumulative Tables & Curve Intersection",
        "speech": (
            "Now flip direction cleanly to master Type Two: the MORE THAN OR EQUAL TO cumulative frequency distribution! "
            "Look carefully at which class boundary switches here! While Less Than used Upper Class Limits going upward, More Than or Equal To ALWAYS pairs with LOWER CLASS LIMITS going downward from Total Frequency n! "
            "Take the exact same intervals: 0–10 (5), 10–20 (3), 20–30 (4), 30–40 (3), total n = 15! Ask: How many students scored MORE THAN OR EQUAL TO 0? Every student—all 15! How many scored 10 or more? Subtract first class: 15 − 5 = 10! How many scored 20 or more? Subtract next class: 10 − 3 = 7! How many scored 30 or more? 7 − 4 = 3! Notice More Than cumulative counts ALWAYS decrease steadily from n down toward the final class frequency! "
            "Check one beautiful geometric property connecting BOTH cumulative frequency curves (commonly called OGIVES): if you plot BOTH the rising Less Than ogive and the falling More Than or Equal To ogive cleanly on the exact same graph axes, their SINGLE intersection point drops vertically straight down onto the horizontal x-axis right at the exact MEDIAN, at vertical height n/2!"
        ),
        "checkpoints": [
            {
                "question": "Which limits are used to construct a 'More Than or Equal To' cumulative frequency table, and how do its values progress?",
                "options": [
                    "Lower Class Limits; values decrease steadily downward starting from Total n",
                    "Upper Class Limits; values increase steadily",
                    "Midpoints; values stay constant",
                    "Upper Class Limits; values decrease to zero"
                ],
                "answer": 0,
                "hint": "Saying 'More than or equal to 10' starts right at the Lower Limit of class 10–20!",
                "explanation": "More Than tables use Lower Class Limits and step down from total n by subtracting each class frequency."
            },
            {
                "question": "If the 'Less Than' and 'More Than' cumulative frequency curves (ogives) of a distribution intersect at point (28.5, 30), what are the exact Median and Total Frequency (n)?",
                "options": [
                    "Median = 28.5,   Total Frequency n = 60",
                    "Median = 30,   Total Frequency n = 28.5",
                    "Median = 28.5,   Total Frequency n = 30",
                    "Median = 57,   Total Frequency n = 30"
                ],
                "answer": 0,
                "hint": "Intersection coordinates give (Median, n/2)!",
                "explanation": "x-coordinate = Median = 28.5; y-coordinate = n/2 = 30 ⟹ n = 60."
            }
        ]
    },
    {
        "id": 12,
        "title": "Grouped Median Formula",
        "subtitle": "Section 13.4: Finding Median Class (cf ≥ n/2) & Median = l + [((n/2) − cf) / f] × h",
        "speech": (
            "Now put cumulative frequency straight into action with Section Thirteen Point Four's core formula: the Median of Grouped Data! "
            "Follow these FOUR rock-solid steps on EVERY problem! Step One: Calculate the Less Than cumulative frequency column cf up to total n! Step Two: Compute n divided by TWO! Locate the MEDIAN CLASS—the VERY FIRST interval whose cumulative frequency cf is greater than or equal to n/2! "
            "Step Three: Read FOUR numbers carefully—avoid the #1 exam slip! l = lower limit of median class; h = class size; f = simple frequency OF that median class; and cf = cumulative frequency of the class PRECEDING (directly ABOVE) the median class! Never accidentally plug the median class's own cf into the numerator! "
            "Step Four: Plug cleanly into Median equals l PLUS [((n/2) − cf) / f] × h! Test right now on NCERT's fifty one girls' height distribution table (where half-count n/2 = 25.5 falls squarely inside median interval 145–150 with lower limit l = 145, median class frequency f = 18, preceding cumulative frequency cf = 11, and width h = 5): 145 + [(25.5 − 11) / 18] × 5 = 145 + 72.5/18 = exact 149.03 centimeters!"
        ),
        "checkpoints": [
            {
                "question": "In the grouped Median formula l + [((n/2) − cf) / f] × h, which row's cumulative frequency must be plugged in for 'cf'?",
                "options": [
                    "The cumulative frequency of the class PRECEDING (directly above) the median class",
                    "The cumulative frequency of the median class itself",
                    "Total frequency n",
                    "Frequency of the succeeding class"
                ],
                "answer": 0,
                "hint": "(n/2) − cf measures how far inside the median class you still need to climb past all previous classes!",
                "explanation": "cf is strictly the cumulative frequency of the class preceding the median class, while f is the median class frequency."
            },
            {
                "question": "For n = 51 girls' heights (n/2 = 25.5), median class is 145–150 with l = 145, h = 5, f = 18, and preceding cf = 11. Compute the Median:",
                "options": [
                    "149.03 cm",
                    "147.25 cm",
                    "151.03 cm",
                    "145.80 cm"
                ],
                "answer": 0,
                "hint": "Compute 145 + [(25.5 − 11) / 18] × 5 = 145 + (14.5 × 5)/18!",
                "explanation": "145 + (72.5 / 18) = 145 + 4.028 = 149.03 cm."
            }
        ]
    },
    {
        "id": 13,
        "title": "Dual Missing Frequencies",
        "subtitle": "Exercise 13.3 Q2 Classic Board HOTS (Median = 28.5, n = 60 → x = 8, y = 7) & Discontinuous Leaves Q4",
        "speech": (
            "Now conquer one of the highest-scoring board problems in NCERT Class Ten: Exercise Thirteen Point Three Question Two, solving TWO unknown frequencies x and y simultaneously from the Median! "
            "Examine the frequency table: 0–10 (5), 10–20 (x), 20–30 (20), 30–40 (15), 40–50 (y), 50–60 (5)! We are given TWO facts: Total frequency n = 60, and Median = 28.5! "
            "Equation One comes from summing all frequencies: 5 + x + 20 + 15 + y + 5 = 45 + x + y = 60 ⟹ x + y = 15! "
            "Equation Two comes straight from Median = 28.5! Since 28.5 lies neatly between 20 and 30, the MEDIAN CLASS MUST BE 20–30 (even before knowing x)! So l = 20, h = 10, f = 20, n/2 = 30, and preceding cf = 5 + x! "
            "Plug straight into the Median formula: 28.5 = 20 + [(30 − 5 − x) / 20] × 10 ⟹ 8.5 = (25 − x) / 2 ⟹ 17 = 25 − x ⟹ x = EIGHT! Substituting x = 8 into x + y = 15 gives y = SEVEN cleanly! Always verify continuous boundaries on leaves Q4 (117.5–171.5)!"
        ),
        "checkpoints": [
            {
                "question": "In Exercise 13.3 Q2, Median = 28.5, Total n = 60, with intervals 0–10 (5), 10–20 (x), 20–30 (20), 30–40 (15), 40–50 (y), 50–60 (5). Find (x, y):",
                "options": [
                    "x = 8,   y = 7",
                    "x = 7,   y = 8",
                    "x = 9,   y = 6",
                    "x = 10,   y = 5"
                ],
                "answer": 0,
                "hint": "28.5 in 20–30 gives 28.5 = 20 + [(30 − (5+x))/20]×10; combine with x + y = 15!",
                "explanation": "8.5 = (25−x)/2 ⟹ 17 = 25−x ⟹ x = 8; then y = 15 − 8 = 7."
            },
            {
                "question": "In the leaves length survey (Ex 13.3 Q4: 118–126, 127–135, 136–144, 145–153), why MUST you adjust limits ±0.5 BEFORE applying the Median formula?",
                "options": [
                    "Because discontinuous gaps hide 1 mm between classes, so true l = 144.5 and true class size h = 9 (NOT 8!)",
                    "Because leaves cannot be measured in mm",
                    "Because Median equals Mean only after adding 1",
                    "Adjusting limits changes only total n"
                ],
                "answer": 0,
                "hint": "Check true width: 153.5 − 144.5 = 9 vs unadjusted 153 − 145 = 8!",
                "explanation": "Making intervals continuous gives exact true boundary l = 144.5 and true width h = 9, yielding exact Median 146.75 mm."
            }
        ]
    },
    {
        "id": 14,
        "title": "Choosing Central Measure",
        "subtitle": "Section 13.4 Guidelines: Comparing Mean (Uses All Data), Median (Outlier-Proof) & Mode (Most Common)",
        "speech": (
            "Which statistical measure of central tendency should a professional data analyst choose in practical real life situations: Mean, Median, or Mode? Examine Section Thirteen Point Four's textbook decision guidelines carefully! "
            "Pick MEAN whenever numerical data values cluster fairly symmetrically around a center without extreme high or low outliers, because Mean incorporates EVERY single observation mathematically with balanced equal weight! However, watch one classic pitfall carefully: if ONE billionaire walks into a small meeting room of ten ordinary salaried workers, the arithmetic Mean salary skyrockets artificially upward while misrepresenting almost everyone present in the room! "
            "Pick MEDIAN whenever extreme outlier values heavily distort one tail of the dataset OR whenever grouped class intervals contain OPEN ENDS such as 'below 20' or '80 and above'! Because Median evaluates only cumulative fifty percent position around the middle class, extreme high or low tail values cannot pull it sideways! "
            "Pick MODE whenever you need the SINGLE MOST POPULAR repeating choice, such as manufacturing shoe sizes, readymade shirt collar sizes, or tracking peak customer vehicle traffic across busy intersections! Notice Mode even works effortlessly on non-numerical consumer preferences and qualitative surveys! Always examine dataset shape and practical purpose carefully first!"
        ),
        "checkpoints": [
            {
                "question": "A tech startup has 9 interns earning ₹20,000/month and 1 founder earning ₹50,00,000/month. Which measure BEST represents a typical employee salary?",
                "options": [
                    "Median (₹20,000), because Mean gets distorted heavily by the single extreme outlier!",
                    "Mean (₹5,18,000)",
                    "Sum total alone",
                    "Class width"
                ],
                "answer": 0,
                "hint": "Outliers drag Mean sharply toward extreme tails, whereas Median remains stable!",
                "explanation": "Median resists extreme salary outliers and accurately reflects the typical employee earning ₹20,000."
            },
            {
                "question": "A shoe factory must decide which single size to manufacture in largest bulk quantity. Which statistical measure guides production directly?",
                "options": [
                    "Mode (the most frequently bought shoe size!)",
                    "Mean (e.g., fractional size 7.38)",
                    "Cumulative Sum",
                    "Assumed Mean a"
                ],
                "answer": 0,
                "hint": "Factories cannot manufacture fractional 'average shoe size 7.38'—they produce the most demanded size!",
                "explanation": "Mode identifies the exact highest-demand category for retail/manufacturing sizing."
            }
        ]
    },
    {
        "id": 15,
        "title": "Empirical Relation Formula",
        "subtitle": "Section 13.4 Benchmark Law: 3 Median = Mode + 2 Mean (Connecting Ex 13.3 Q1 & Skewed Estimates)",
        "speech": (
            "Unlock Section Thirteen Point Four's celebrated Empirical Relationship linking all THREE central tendency measures together cleanly in one compact equation: THREE MEDIAN EQUALS MODE PLUS TWO MEAN! "
            "Repeat that golden rhyme out loud several times until it sticks forever: Three Median equals Mode plus Two Mean! Understand carefully what the word 'empirical' signals mathematically here: this equation is NOT a rigid exact algebraic identity for every possible artificial dataset, yet across countless real-world moderately skewed distributions, whenever ANY TWO measures are already known, this formula predicts the THIRD measure accurately! "
            "Master BOTH quick algebraic rearrangements right away so you solve ALL board exam directions fluently: Mode equals Three Median MINUS Two Mean! And Mean equals Three Median MINUS Mode, all divided cleanly by TWO! "
            "Test this right onto Exercise Thirteen Point Three Question One (covering 68 consumers' monthly electricity consumption units): calculating separately from the grouped frequency table gives Mean equal to 137.05 units, Mode equal to 135.76 units, and Median equal to 137 units! Plug cleanly to verify: three times 137 equals 411, while 135.76 plus two times 137.05 equals 409.86—closely confirming our empirical benchmark! Note also when data is perfectly symmetric, Mean equals Median equals Mode identically!"
        ),
        "checkpoints": [
            {
                "question": "Using the Empirical Formula (3 Median = Mode + 2 Mean), if a distribution has Mean = 24 and Median = 26, find its approximate Mode:",
                "options": [
                    "Mode = 30   [= 3(26) − 2(24) = 78 − 48]",
                    "Mode = 25",
                    "Mode = 28",
                    "Mode = 22"
                ],
                "answer": 0,
                "hint": "Rearrange: Mode = 3 Median − 2 Mean!",
                "explanation": "Mode = 3(26) − 2(24) = 78 − 48 = 30."
            },
            {
                "question": "If Mode = 12 and Mean = 18 in a moderately skewed distribution, compute Median using the empirical relation:",
                "options": [
                    "Median = 16   [= (12 + 2×18) / 3 = 48 / 3]",
                    "Median = 15",
                    "Median = 14",
                    "Median = 20"
                ],
                "answer": 0,
                "hint": "3 Median = 12 + 2(18) = 48 ⟹ divide by 3!",
                "explanation": "3 Median = 12 + 36 = 48 ⟹ Median = 48/3 = 16."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Thirteen Summary",
        "subtitle": "Section 13.5 Master Formula Card: 3 Mean Methods, Mode, Median, Cumulative Curves & Empirical Law",
        "speech": (
            "Congratulations, statistics masters! You have conquered every grouped frequency formula, cumulative curve, missing unknown puzzle, and conceptual interpretation inside NCERT Class Ten Chapter Thirteen: Statistics! Snapshot your complete Section Thirteen Point Five formula summary card onto memory before entering forty Interactive Board Quizzes! "
            "One, Three Grouped Mean Methods (all using midpoint Class Mark xᵢ = (Upper + Lower)/2): Direct Method Σfᵢxᵢ / Σfᵢ, Assumed Mean a + Σfᵢdᵢ / Σfᵢ (where deviations dᵢ = xᵢ − a), and Step-Deviation a + h(Σfᵢuᵢ / Σfᵢ) (where uᵢ = (xᵢ − a)/h)! "
            "Two, Grouped Mode Formula: locate Modal Class holding highest frequency f₁, then compute l + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h! "
            "Three, Grouped Median Formula: build Less Than cumulative cf using Upper Limits, locate very first class satisfying cf ≥ n/2, then compute l + [((n/2) − cf) / f] × h where cf comes STRICTLY from the preceding class! "
            "Four, Discontinuous Boundaries: ALWAYS convert inclusive limits ±0.5 BEFORE applying Mode or Median! "
            "Five, Empirical Law: 3 Median equals Mode plus 2 Mean, and plotting Less Than and More Than ogives intersects directly at point (Median, n/2)! Check whether every question asks for Mean, Mode, or Median before picking formulas!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement across NCERT Chapter 13 formulas is 100% mathematically accurate?",
                "options": [
                    "Mean = a + h(Σfᵢuᵢ/Σfᵢ); Mode = l + [(f₁−f₀)/(2f₁−f₀−f₂)]×h; Median = l + [((n/2)−cf)/f]×h; 3 Median = Mode + 2 Mean",
                    "3 Mean = Mode + 2 Median",
                    "Less Than cf uses Lower Class Limits",
                    "In Median, cf is taken from the median class itself"
                ],
                "answer": 0,
                "hint": "Check coefficient 3 on Median, cf from preceding class, and Upper Limits for Less Than!",
                "explanation": "Option 1 accurately states every Chapter 13 formula."
            },
            {
                "question": "In a symmetric distribution where Mean = Median = Mode = 50, verify what 3 Median − Mode − 2 Mean equals:",
                "options": [
                    "0   (satisfying 3(50) = 50 + 2(50) identically!)",
                    "50",
                    "100",
                    "−50"
                ],
                "answer": 0,
                "hint": "Substitute 50 for all three values into 3(50) − 50 − 2(50)!",
                "explanation": "150 − 50 − 100 = 0; in perfectly symmetric data, Mean = Median = Mode."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch13 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

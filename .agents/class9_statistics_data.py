# -*- coding: utf-8 -*-
"""
Data module for Class 9 Mathematics Chapter 14: Statistics
Syllabus Competencies: CG-6, C-6.1, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

SLIDES = [
    {
        "id": 1,
        "title": "The Statistical Inquiry Cycle: PPDAC Framework & Raw Data",
        "subtitle": "Problem, Plan, Data, Analysis, Conclusion — From Raw Observations to Grouped Tables",
        "category": "Data Collection & Organisation",
        "badge": "CG-6 • Statistical Investigation",
        "summary": "Statistics is the branch of mathematical science concerned with the collection, organisation, presentation, analysis, and interpretation of numerical data. A modern scientific investigation follows the 5-stage PPDAC inquiry cycle: (1) Problem: formulating precise questions (e.g., 'What is the average daily screen time of Grade 9 students?'); (2) Plan: designing sampling protocols, measurement tools, and identifying primary vs secondary data sources; (3) Data: collecting raw measurements without systematic bias; (4) Analysis: organising data into arrays and frequency distribution tables, computing summary metrics; and (5) Conclusion: interpreting patterns, answering the inquiry question, and noting limitations. Unorganized measurements are called Raw Data. Arranging data in ascending or descending order yields an Array. The Range of the dataset is the difference between the maximum and minimum observations: Range = Maximum Value - Minimum Value. Tally marks grouped in clusters of five (four vertical bars crossed by a diagonal strike) enable swift, error-free frequency compilation.",
        "key_points": [
            "PPDAC Inquiry Cycle: Problem → Plan → Data → Analysis → Conclusion guides scientific data investigation.",
            "Data Classifications: Primary data (collected firsthand by the investigator) vs Secondary data (sourced from records/censuses).",
            "Raw Data & Array: Unsorted measurements are Raw Data; arranged in ascending or descending order is an Arrayed Data set.",
            "Range of Data: Range = Maximum Observation - Minimum Observation; measures total dispersion spread.",
            "Frequency & Tally Marks: Frequency (f) denotes the number of times a value occurs; tally marks bundle into groups of 5."
        ],
        "narration": "Welcome to Statistics! In modern science and daily decision-making, we are constantly surrounded by facts and numbers. But numbers alone are not enough. We need the PPDAC framework—Problem, Plan, Data, Analysis, and Conclusion—to turn raw chaos into actionable knowledge. Notice how raw numbers become structured once we sort them into an array and group them with tally marks to discover their frequency and range. Explore our interactive tally counter to see raw measurements automatically bundle into structured frequencies!",
        "sim_title": "Interactive PPDAC Inquiry Pipeline & Live Tally Counter",
        "checkpoints": [
            {
                "q": "The marks obtained by 10 students in a math test are: 55, 36, 95, 73, 60, 42, 25, 78, 75, 62. What is the range of this dataset?",
                "options": ["65", "70", "75", "80"],
                "ans": 1,
                "exp": "Range = Maximum value - Minimum value. Here, Maximum = 95 and Minimum = 25. Therefore, Range = 95 - 25 = 70."
            },
            {
                "q": "In a statistical investigation, data collected directly by an investigator for a specific purpose is called:",
                "options": ["Secondary Data", "Primary Data", "Composite Data", "Continuous Data"],
                "ans": 1,
                "exp": "Data collected firsthand by the investigator with a specific objective in mind is called Primary Data. Data obtained from previously published or stored records is Secondary Data."
            }
        ]
    },
    {
        "id": 2,
        "title": "Bar Graphs: Discrete Categories & Uniform Widths",
        "subtitle": "Visualising Qualitative and Discrete Quantitative Variables with Spaced Rectangles",
        "category": "Graphical Representation",
        "badge": "C-6.1 • Discrete Visualisation",
        "summary": "A bar graph (or bar chart) is a pictorial representation of discrete or categorical data in which rectangular bars of uniform width are drawn with equal spaces between them. The height (or length) of each bar is directly proportional to the frequency of the corresponding category. Essential rules for constructing valid bar graphs: (1) Bar widths must remain identical across all categories—width has no mathematical value and only provides visual clarity; (2) The spaces (gaps) between consecutive bars must be equal and non-zero to signify discrete, separate categories; (3) The vertical axis (or horizontal axis) must start at 0, with a clearly calibrated uniform scale (e.g., 1 unit = 5 students); and (4) If the scale does not start at 0, a 'kink' or zig-zag break (zigzag axis) must be explicitly shown to prevent visual distortion. Bar graphs are universally applied to depict categorical frequencies such as favorite subjects, blood groups, monthly family expenditures, and vehicle types.",
        "key_points": [
            "Discrete Representation: Used for categorical or discrete quantitative data where no continuous transitions exist.",
            "Uniform Width & Equal Gaps: Bar widths must be equal, and spacing between bars must remain strictly uniform.",
            "Height Proportional to Frequency: The height of each bar directly reflects the numerical count or frequency.",
            "Scale Integrity: The frequency axis must start at zero or clearly mark an axis break (kink) to avoid misleading the viewer.",
            "Orientation: Can be drawn vertically (column bars) or horizontally (row bars) depending on category label length."
        ],
        "narration": "Bar graphs are our most trusted tools for categorical data! When comparing students' favorite sports or family budget allocations, each category stands independently. Notice the two cardinal rules: every bar must have the exact same width, and the gaps between bars must be uniform. That's because the width doesn't carry meaning—only the height tells the story! Try adjusting the category counts on our interactive chart to observe how the vertical scale balances automatically.",
        "sim_title": "Interactive Bar Chart Studio & Scale Balancer",
        "checkpoints": [
            {
                "q": "Which of the following is a mandatory rule when constructing a standard vertical bar graph?",
                "options": [
                    "The widths of bars must vary according to frequency",
                    "There must be no spaces between consecutive bars",
                    "The widths of the bars and the spaces between them must be uniform",
                    "The heights of all bars must be equal"
                ],
                "ans": 2,
                "exp": "In a standard bar graph, the bars must have uniform width and the spaces (gaps) separating consecutive bars must also be uniform to represent discrete categories accurately."
            },
            {
                "q": "If 1 cm on the vertical axis represents 15 vehicles, what height bar is required to represent a frequency of 75 vehicles?",
                "options": ["3 cm", "4 cm", "5 cm", "6 cm"],
                "ans": 2,
                "exp": "Height = Total Frequency / Scale Factor = 75 / 15 = 5 cm."
            }
        ]
    },
    {
        "id": 3,
        "title": "Stacked Bar Graphs: Decomposing Component Totals",
        "subtitle": "Segmented Bars for Comparing Overall Magnitudes and Internal Categorical Breakdowns",
        "category": "Graphical Representation",
        "badge": "CG-6 • Component Decomposition",
        "summary": "A Stacked Bar Graph (also known as a Segmented Bar Chart) divides each bar into multiple colored sub-segments stacked on top of one another. It allows simultaneous visual evaluation of two distinct dimensions: (1) The overall total height of the bar represents the aggregate sum of the primary category (e.g., total school enrollment per year); and (2) The individual heights of the colored segments depict the breakdown contributions of sub-categories (e.g., boys vs. girls, or science vs. humanities streams). To read an internal segment that does not start at the baseline zero, subtract the lower segment boundary from the upper segment boundary: Segment Value = Y_top - Y_bottom. Stacked bar graphs excel in demographic studies, energy source portfolios (solar, wind, thermal, hydro over successive decades), and corporate revenue streams across product divisions.",
        "key_points": [
            "Dual-Level Insight: Displays both the aggregate total (entire bar height) and constituent parts (segment lengths).",
            "Segment Stacking: Sub-categories are placed consecutively atop each other from baseline to bar summit.",
            "Segment Value Calculation: For floating segments, Value = Upper Boundary Coordinate - Lower Boundary Coordinate.",
            "Legend Necessity: A distinct color code and legend are essential to identify each component sub-segment.",
            "Best Application: Comparing total volume across categories while monitoring changes in sub-group composition."
        ],
        "narration": "What if you need to know both the total number of students in a grade AND how many are boys versus girls? Enter the Stacked Bar Graph! Instead of drawing separate bars side by side, we stack the girl count right on top of the boy count. The total height shows the entire grade strength, while each colored block reveals its internal composition. Use our simulator to change sub-group counts and see how the segments stack and expand!",
        "sim_title": "Interactive Stacked Bar Graph Explorer & Segment Ruler",
        "checkpoints": [
            {
                "q": "In a stacked bar graph, a bar has a total height of 120 units. The bottom segment (Science) ends at 50 units, and the middle segment (Commerce) ends at 90 units. What is the value of the top segment (Arts)?",
                "options": ["20 units", "30 units", "40 units", "50 units"],
                "ans": 1,
                "exp": "The top segment spans from 90 to 120 units. Value = 120 - 90 = 30 units."
            },
            {
                "q": "To determine the absolute magnitude of an intermediate (middle) segment in a stacked bar graph, one must:",
                "options": [
                    "Read the upper boundary directly on the vertical axis",
                    "Subtract the lower boundary value from the upper boundary value",
                    "Divide the total height by the number of segments",
                    "Measure the width of the bar"
                ],
                "ans": 1,
                "exp": "Since the middle segment does not start at zero, its magnitude equals Upper Boundary Value - Lower Boundary Value."
            }
        ]
    },
    {
        "id": 4,
        "title": "100% Stacked Bar Graphs: Relative Proportions & Percentage Shares",
        "subtitle": "Normalising Unequal Population Totals to Evaluate Pure Categorical Composition",
        "category": "Graphical Representation",
        "badge": "CG-9 • Relative Proportions",
        "summary": "While a standard stacked bar graph emphasizes absolute totals, a 100% Stacked Bar Graph normalizes every single bar to an identical total height of 100%. Each constituent segment represents the percentage relative share of that sub-category within its group: Percentage Share = (Component Value / Group Total) × 100%. This representation is indispensable when comparing the internal composition of groups that have vastly different total population sizes. For example, comparing the budget allocations of a small school (total budget ₹5 Lakhs) with a large university (total budget ₹50 Crores) using absolute bars makes the small school's bars invisible. In a 100% stacked bar chart, both institutions stand at 100%, allowing immediate, fair comparison of the proportion spent on teacher salaries, laboratory equipment, and sports.",
        "key_points": [
            "Fixed Total Height: Every bar extends to exactly 100% on the vertical percentage axis.",
            "Percentage Normalisation: Each segment length = (Sub-category Value / Total Category Value) × 100%.",
            "Eliminates Scale Bias: Enables fair comparison of internal structures across groups with vastly different sample sizes.",
            "Focus on Proportions: Prioritises relative share and ratio distributions rather than raw counts.",
            "Limitation: Does not display the absolute magnitude of totals; requires accompanying data tables or annotations."
        ],
        "narration": "Imagine comparing household budgets between two families—one earning 20,000 rupees and another earning 200,000 rupees. If we plotted absolute amounts, the smaller bar would be barely visible! But with a 100% Stacked Bar Graph, both bars are scaled to exactly 100 percent. Now you can instantly see that both families spend 40% on food and 20% on education. Toggle between absolute and normalized views in our simulator to see this transformation live!",
        "sim_title": "Absolute Stacked vs 100% Stacked Normalizer",
        "checkpoints": [
            {
                "q": "In a school of 400 students, 240 travel by bus, 100 walk, and 60 use bicycles. In a 100% stacked bar graph, what percentage height represents bus commuters?",
                "options": ["40%", "50%", "60%", "70%"],
                "ans": 2,
                "exp": "Percentage share = (240 / 400) × 100% = 0.60 × 100% = 60%."
            },
            {
                "q": "When is a 100% stacked bar graph preferred over a standard stacked bar graph?",
                "options": [
                    "When absolute counts across categories must be strictly highlighted",
                    "When comparing relative percentage compositions of groups with vastly different sample sizes",
                    "When there is only one category to display",
                    "When class intervals have unequal widths"
                ],
                "ans": 1,
                "exp": "A 100% stacked bar graph is ideal when comparing proportions and percentage shares across groups of disparate sample sizes, neutralizing total magnitude differences."
            }
        ]
    },
    {
        "id": 5,
        "title": "Histograms with Uniform Class Widths",
        "subtitle": "Continuous Interval Partitions Where Area Strictly Dictates Frequency",
        "category": "Graphical Representation",
        "badge": "C-6.1 • Continuous Histograms",
        "summary": "A Histogram is a 2D graphical representation of continuous frequency distribution where class intervals are marked on the horizontal axis and frequencies on the vertical axis. Unlike bar graphs, there are NO spaces or gaps between adjacent rectangles because the data variable is continuous. For uniform class widths (where class size h = Upper Limit - Lower Limit is constant for all intervals), the heights of the rectangles are directly proportional to the class frequencies. Key structural terms: (1) Class Limits: Lower limit (L) and Upper limit (U); (2) Class Size (Width): h = U - L; (3) Class Mark (Midpoint): x_i = (L + U) / 2. If data is recorded in inclusive form (e.g., 10-19, 20-29), it must first be converted into continuous exclusive form (e.g., 9.5-19.5, 19.5-29.5) by subtracting 0.5 from lower limits and adding 0.5 to upper limits before plotting.",
        "key_points": [
            "Continuous Data: Used for continuous variables (heights, weights, time, exam scores) with touching bars.",
            "Zero Gaps: Rectangles share vertical boundaries; no gaps exist between consecutive intervals.",
            "Area Proportionality: The area of each rectangle is strictly proportional to its class frequency.",
            "Class Mark (Midpoint): x_i = (Lower Limit + Upper Limit) / 2; represents the center of the interval.",
            "Continuity Correction: Convert inclusive intervals (gap 1) by subtracting and adding 0.5 to the boundaries."
        ],
        "narration": "Now we move from discrete categories to continuous data like student heights or travel times. Notice something revolutionary: there are no gaps between the bars! Because when one interval ends, say at 10 minutes, the next interval begins at that exact point. In a histogram, the area of each rectangle represents the frequency. When all widths are equal, height alone tells the story. Build your own continuous histogram in our interactive canvas!",
        "sim_title": "Continuous Interval Histogram Builder & Boundary Snapper",
        "checkpoints": [
            {
                "q": "What is the class mark (midpoint) of the class interval 35 - 45?",
                "options": ["38", "40", "42", "45"],
                "ans": 1,
                "exp": "Class mark = (Lower Limit + Upper Limit) / 2 = (35 + 45) / 2 = 80 / 2 = 40."
            },
            {
                "q": "If raw continuous data is given in inclusive intervals 1-5, 6-10, 11-15, what are the true continuous class boundaries for the second interval?",
                "options": ["6.0 to 10.0", "5.5 to 10.5", "5.0 to 10.0", "6.5 to 10.5"],
                "ans": 1,
                "exp": "Continuity correction factor = (6 - 5) / 2 = 0.5. Subtract 0.5 from lower limit (6 - 0.5 = 5.5) and add 0.5 to upper limit (10 + 0.5 = 10.5)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Histograms with Unequal Class Widths: Frequency Density",
        "subtitle": "The Fundamental Area Principle — Adjusting Heights to Prevent Visual Distortion",
        "category": "Graphical Representation",
        "badge": "CG-9 • Area Invariance",
        "summary": "In histograms, the foundational mathematical law is: Area of Rectangle ∝ Class Frequency. When all class intervals have equal width, height is directly proportional to frequency. However, when class intervals have unequal (varying) widths, plotting raw frequency as height creates massive visual deception—wider intervals appear disproportionately dominant because their area is artificially inflated! To maintain correct area proportionality, we must adjust the height of each rectangle using Frequency Density or Adjusted Frequency: Adjusted Frequency = (Minimum Class Width / Class Width of Interval) × Frequency; or Frequency Density = Frequency / Class Width. For example, if minimum width is 10, an interval of width 30 with frequency 60 must have an adjusted height of (10/30) × 60 = 20. Its drawn area is then 30 × 20 = 600, exactly preserving the correct visual weight relative to a width-10 interval of frequency 20 (area 10 × 20 = 200).",
        "key_points": [
            "Histogram Golden Rule: Area of the rectangle—NOT its height alone—must be proportional to frequency.",
            "Trap of Raw Frequencies: Using unadjusted heights with unequal widths inflates areas and misleads viewers.",
            "Adjusted Frequency Formula: Height = (Minimum Class Width / Class Width of Interval) × Frequency.",
            "Frequency Density Definition: Frequency Density = Frequency / Class Width; represents frequency per unit width.",
            "Total Histogram Area: The sum of all rectangular areas remains strictly proportional to total sample size N."
        ],
        "narration": "Pay close attention to this vital concept! In a histogram, the area of a bar represents frequency, not just its height. If an age bracket is three times wider than the others, drawing it with raw frequency makes its area three times too big! That distorts the truth. We fix this by calculating Frequency Density or Adjusted Frequency, compressing the height so the rectangular area stays true to the data. Toggle between raw and adjusted views in our simulator to witness the correction!",
        "sim_title": "Unequal Width Frequency Density Correcter & Area Verifier",
        "checkpoints": [
            {
                "q": "In a dataset with minimum class width 5, an interval 20 - 40 (width 20) has a frequency of 36. What is the adjusted frequency (height) for drawing the histogram?",
                "options": ["9", "18", "24", "36"],
                "ans": 0,
                "exp": "Adjusted Frequency = (Minimum Class Width / Class Width) × Frequency = (5 / 20) × 36 = (1 / 4) × 36 = 9."
            },
            {
                "q": "Why must the heights of rectangles in a histogram with varying class widths be adjusted?",
                "options": [
                    "To ensure all rectangles have identical heights",
                    "To satisfy the fundamental principle that area of each rectangle must be proportional to frequency",
                    "To convert continuous data into discrete categories",
                    "To make the frequency polygon symmetric"
                ],
                "ans": 1,
                "exp": "The fundamental mathematical principle of histograms is that Area ∝ Frequency. When widths vary, adjusting heights guarantees that area accurately reflects frequency."
            }
        ]
    },
    {
        "id": 7,
        "title": "Frequency Polygons: Continuous Trend Enclosures",
        "subtitle": "Connecting Class Marks and Enclosing Equal Area via Zero-Frequency Baseline Extensions",
        "category": "Graphical Representation",
        "badge": "C-6.1 • Trend Enclosures",
        "summary": "A Frequency Polygon is a piecewise linear line graph formed by joining the midpoints (class marks) of the upper horizontal edges of consecutive histogram rectangles with straight line segments. It can be constructed directly from a frequency table without drawing a histogram by plotting points (x_i, f_i), where x_i is the class mark and f_i is the frequency. To complete the polygon into a closed geometric figure of equal area: (1) Extend the polygon at both ends to the class marks of imaginary preceding and succeeding class intervals of the same width with frequency 0; (2) The baseline closure ensures that the total area enclosed between the frequency polygon and the horizontal axis is exactly equal to the total area of the corresponding histogram! The triangular areas excluded from the tops of rectangles are geometrically congruent to the triangular areas included outside the rectangles, proving area conservation through triangle congruence.",
        "key_points": [
            "Construction Points: Points plotted are (Class Mark, Frequency) = (x_i, f_i).",
            "Alternative to Histograms: Can be plotted directly with class marks without drawing histogram bars first.",
            "Multi-Dataset Comparison: Ideal for superimposing and comparing two or more distributions (e.g., Section A vs Section B).",
            "Baseline Closure Rule: Connect both ends to imaginary adjacent class marks with frequency 0.",
            "Area Equivalence Theorem: Total area enclosed by the frequency polygon equals the total area of the histogram."
        ],
        "narration": "A frequency polygon gives us the continuous rhythm and flow of a distribution! By connecting the midpoint of each bar's roof, we trace out a dynamic polygon. But notice how we close it: we anchor both tails down to zero frequency at the imaginary neighboring class marks. Why? Because the triangular pieces clipped off the bars exactly equal the empty triangles added outside! The total area under the polygon remains identical to the histogram. Watch this area equivalence in our simulator!",
        "sim_title": "Interactive Frequency Polygon & Area Equivalence Engine",
        "checkpoints": [
            {
                "q": "To construct a frequency polygon without a histogram, which values are plotted on the horizontal (X) axis?",
                "options": ["Lower class limits", "Upper class limits", "Class marks (midpoints)", "Class frequencies"],
                "ans": 2,
                "exp": "Points on a frequency polygon have coordinates (Class Mark, Frequency). Midpoints are plotted on the horizontal axis."
            },
            {
                "q": "Why are the tails of a frequency polygon extended to zero frequency at the midpoints of imaginary adjacent classes?",
                "options": [
                    "To make the line look continuous",
                    "To ensure the total area enclosed under the polygon equals the total area of the histogram",
                    "To calculate the median graphically",
                    "To prevent negative frequencies"
                ],
                "ans": 1,
                "exp": "Extending to zero frequency at the adjacent imaginary class marks closes the polygon such that the enclosed area matches the total area of the histogram."
            }
        ]
    },
    {
        "id": 8,
        "title": "Measures of Central Tendency Overview: Representative Centre Values",
        "subtitle": "The Big Three: Arithmetic Mean (Balance), Median (Middle Divider), Mode (Peak Frequency)",
        "category": "Measures of Central Tendency",
        "badge": "CG-6 • Representative Metrics",
        "summary": "A Measure of Central Tendency is a single representative summary metric that locates the central position or 'center of gravity' of a numerical data distribution. Rather than inspecting hundreds of raw values, central tendency condenses the dataset into one meaningful benchmark. The three primary classical measures of central tendency are: (1) Arithmetic Mean (x̄): The mathematical balance point obtained by dividing the sum of all values by total observation count; (2) Median: The positional middle value when observations are sorted in ascending order, partitioning the dataset into two equal halves (50% below, 50% above); and (3) Mode: The most frequently occurring observation or peak category. An ideal measure of central tendency should be rigidly defined, based on all observations, easily understandable, simple to calculate, and not unduly influenced by extreme outliers.",
        "key_points": [
            "Central Tendency Concept: A single representative value summarizing the location of the center of a data cluster.",
            "The Three Measures: Mean (arithmetic center), Median (positional 50th percentile), Mode (most common value).",
            "Mean as Fulcrum: The Mean is the mechanical center of mass; balancing all positive and negative deviations to zero.",
            "Median as Slicer: Divides sorted data into two groups of equal count regardless of extreme numerical magnitudes.",
            "Mode as Popularity Peak: Identifies the category or number with the highest frequency density."
        ],
        "narration": "When summarizing thousands of exam marks or nationwide temperatures, you can't hand someone a book of raw numbers. You need a single number that captures the essence of the group—a measure of central tendency. Think of the Mean as the physical balance point on a seesaw, the Median as the person standing exactly in the middle of a sorted line, and the Mode as the most popular item in the room. Step onto our balance fulcrum to see how moving data points shifts these three measures!",
        "sim_title": "The Central Balance Fulcrum & Dynamic Center of Gravity",
        "checkpoints": [
            {
                "q": "Which measure of central tendency acts as the physical center of gravity where the sum of deviations equals zero?",
                "options": ["Median", "Mode", "Arithmetic Mean", "Range"],
                "ans": 2,
                "exp": "The Arithmetic Mean is the mathematical center of gravity because the sum of deviations of all observations from the mean is always zero: Σ(x_i - x̄) = 0."
            },
            {
                "q": "Which measure of central tendency splits an ordered dataset into two groups containing equal numbers of observations?",
                "options": ["Mean", "Median", "Mode", "Weighted Mean"],
                "ans": 1,
                "exp": "The Median is the positional middle value that divides an ordered dataset into two equal halves (50% of values lie at or below, and 50% lie at or above)."
            }
        ]
    },
    {
        "id": 9,
        "title": "Arithmetic Mean: Ungrouped & Grouped Frequency Data",
        "subtitle": "Formulaic Derivations, the Zero-Deviation Invariant, and Linear Transformations",
        "category": "Measures of Central Tendency",
        "badge": "C-6.1 • Arithmetic Mean",
        "summary": "The Arithmetic Mean (denoted by x̄) is the sum of all observations divided by the total number of observations. (1) Ungrouped Data Formula: For n observations x_1, x_2, ..., x_n: x̄ = (∑_{i=1}^n x_i) / n. (2) Discrete Grouped Frequency Distribution: If values x_1, x_2, ..., x_k occur with frequencies f_1, f_2, ..., f_k: x̄ = (∑_{i=1}^k f_i x_i) / (∑_{i=1}^k f_i) = (∑ f_i x_i) / N, where N = ∑ f_i. Fundamental Mathematical Properties: (a) Zero Deviation Sum: The algebraic sum of deviations of all observations from their arithmetic mean is always identically zero: ∑ (x_i - x̄) = 0; (b) Shift Invariance: If every observation is shifted by constant c (x_i' = x_i + c), new mean is x̄' = x̄ + c; (c) Scale Invariance: If every observation is multiplied by constant a (x_i' = a x_i), new mean is x̄' = a x̄.",
        "key_points": [
            "Ungrouped Mean Formula: x̄ = (∑ x_i) / n; sums all values and divides by count n.",
            "Grouped Mean Formula: x̄ = (∑ f_i x_i) / (∑ f_i); weighs each value x_i by its frequency count f_i.",
            "Zero Deviation Property: ∑_{i=1}^n (x_i - x̄) = 0; positive deviations exactly cancel negative deviations.",
            "Linear Addition Shift: Adding or subtracting constant c shifts the mean by c: (x̄ + c).",
            "Linear Multiplication Scaling: Multiplying all values by constant a scales the mean by a: (a · x̄)."
        ],
        "narration": "The arithmetic mean is our everyday average. Add all the numbers up and divide by how many there are! When identical numbers repeat, we multiply each value by its frequency f_i before summing them up. But here is the most elegant property in all of statistics: if you measure how far each point sits above or below the mean, the sum of all those positive and negative distances is precisely zero! Try moving points on our dynamic number line and watch the deviations cancel out to zero.",
        "sim_title": "Dynamic Mean Calculator & Zero-Deviation Balancer",
        "checkpoints": [
            {
                "q": "The mean of five numbers is 30. If one number is excluded, their mean becomes 28. What is the excluded number?",
                "options": ["36", "38", "40", "42"],
                "ans": 1,
                "exp": "Sum of 5 numbers = 5 × 30 = 150. Sum of remaining 4 numbers = 4 × 28 = 112. Excluded number = 150 - 112 = 38."
            },
            {
                "q": "If the mean of 20 observations is 18 and each observation is multiplied by 3 and then increased by 5, what is the new mean?",
                "options": ["54", "59", "64", "69"],
                "ans": 1,
                "exp": "Linear transformation rule: x̄_new = a · x̄_old + c = 3(18) + 5 = 54 + 5 = 59."
            }
        ]
    },
    {
        "id": 10,
        "title": "Weighted Average: Prioritising Importance in Real-World Settings",
        "subtitle": "Overcoming Equal-Weight Bias in GPA, Consumer Price Indices & Multi-Criteria Decisions",
        "category": "Measures of Central Tendency",
        "badge": "CG-6 • Weighted Decisions",
        "summary": "In many practical scenarios, not all observations carry equal importance or significance. Computing a simple arithmetic mean naively assumes that every single data item has identical weight. To assign proportional importance, we compute the Weighted Average (x̄_w): x̄_w = (∑_{i=1}^k w_i x_i) / (∑_{i=1}^k w_i), where w_i represents the numerical weight (credit, percentage importance, or expenditure share) assigned to value x_i. Real-World Applications: (1) Academic GPA / Course Grades: Homework (weight 20%), Midterm (weight 30%), Final Exam (weight 50%). A student with 90 in homework, 70 in midterm, and 80 in final earns (20×90 + 30×70 + 50×80)/100 = (1800 + 2100 + 4000)/100 = 79. (2) Consumer Price Index (CPI): Price inflation of staple food (weight 45%) affects households far more severely than luxury jewelry (weight 2%). (3) Multi-Criteria Corporate Hiring: Interview, Technical Test, and Experience weighted by role requirements.",
        "key_points": [
            "Limitation of Simple Mean: Treats all data points as possessing identical significance and impact.",
            "Weighted Mean Formula: x̄_w = (∑ w_i x_i) / (∑ w_i); multiplies values by weights before normalising.",
            "Weight Normalisation: If weights are expressed as percentages summing to 100%, the denominator is simply 100.",
            "Academic Grade Portfolios: Final exams and major projects carry higher weights than minor weekly homework.",
            "Economic Inflation (CPI): Essential commodities (wheat, rice, fuel) carry higher weights than discretionary luxuries."
        ],
        "narration": "Should a five-minute quiz count the exact same as a three-hour final exam? Of course not! That is why real life uses the Weighted Average. Each component is multiplied by its importance weight, w_i, before dividing by the sum of all weights. Economists use this to calculate inflation with the Consumer Price Index, where food prices matter far more than luxury watches. Adjust the sliders in our GPA and CPI simulator to see how shifting weights alters your final score!",
        "sim_title": "Interactive Weighted GPA & CPI Portfolio Simulator",
        "checkpoints": [
            {
                "q": "A student scores 80 in Lab Work (weight 2), 70 in Midterm (weight 3), and 90 in Final Exam (weight 5). What is the student's weighted average score?",
                "options": ["80", "82", "84", "86"],
                "ans": 1,
                "exp": "x̄_w = (2×80 + 3×70 + 5×90) / (2 + 3 + 5) = (160 + 210 + 450) / 10 = 820 / 10 = 82."
            },
            {
                "q": "In computing the Consumer Price Index (CPI), why are price changes of food items assigned significantly larger weights than cinema tickets?",
                "options": [
                    "Food items have higher unit prices",
                    "Households spend a much larger percentage of their regular budget on essential food than on entertainment",
                    "Cinema tickets are purchased by fewer people",
                    "Food prices never change"
                ],
                "ans": 1,
                "exp": "Weights in index numbers reflect the relative economic importance and proportion of total household expenditure devoted to that commodity."
            }
        ]
    },
    {
        "id": 11,
        "title": "Median: Positional Middle of Ordered Data",
        "subtitle": "Step-by-Step Sorting, Odd vs Even Algorithms, and Cumulative Frequency Tables",
        "category": "Measures of Central Tendency",
        "badge": "C-6.1 • Positional Median",
        "summary": "The Median is the value of the middle observation when raw data is arranged in ascending (or descending) order of magnitude. It splits the distribution into two equal halves such that 50% of observations lie below or at the median, and 50% lie above or at the median. Median Computation Algorithm: (1) Step 1: Arrange all n raw observations in ascending order: x_1 ≤ x_2 ≤ ... ≤ x_n; (2) Step 2: Determine total count n; (3) Case A (When n is ODD): Median = value of the ((n + 1) / 2)-th observation; (4) Case B (When n is EVEN): There are two middle terms at positions (n / 2) and (n / 2 + 1). The median is the arithmetic mean of these two middle terms: Median = [Value at (n/2) + Value at (n/2 + 1)] / 2. For discrete frequency distributions, compute Cumulative Frequencies (cf) and locate the observation corresponding to N/2.",
        "key_points": [
            "Sorting Prerequisite: Data MUST be arranged in non-decreasing order before locating the median.",
            "Odd n Formula: Median = Observation at position ((n + 1) / 2).",
            "Even n Formula: Median = Average of observations at positions (n / 2) and ((n / 2) + 1).",
            "Positional Nature: Depends exclusively on ranked positions rather than the arithmetic sum of values.",
            "Cumulative Frequency (cf): Running total of frequencies used to swiftly identify the middle observation."
        ],
        "narration": "To find the median, rule number one is non-negotiable: you must sort your data in order! Once lined up from smallest to largest, the median is the person standing right in the center. If there are 7 numbers, the 4th number is the median. If there are 8 numbers, there are two people in the middle—so you take their average! Watch our interactive sorting engine arrange scrambled numbers and zoom into the exact middle position.",
        "sim_title": "Interactive Sorting & Median Squeeze Engine",
        "checkpoints": [
            {
                "q": "Find the median of the following dataset: 18, 13, 27, 25, 15, 31, 20.",
                "options": ["18", "20", "22", "25"],
                "ans": 1,
                "exp": "Step 1: Sort in ascending order: 13, 15, 18, 20, 25, 27, 31. Total n = 7 (odd). Position = (7 + 1) / 2 = 4th term. 4th term = 20."
            },
            {
                "q": "Find the median of the dataset: 8, 14, 6, 12, 19, 10, 15, 22.",
                "options": ["12", "13", "14", "15"],
                "ans": 1,
                "exp": "Sort in order: 6, 8, 10, 12, 14, 15, 19, 22. Total n = 8 (even). Middle terms are 4th (12) and 5th (14). Median = (12 + 14) / 2 = 26 / 2 = 13."
            }
        ]
    },
    {
        "id": 12,
        "title": "Mode: Most Frequent Observation & Category Peak",
        "subtitle": "Unimodal, Bimodal, Multimodal Classifications and Qualitative Data Supremacy",
        "category": "Measures of Central Tendency",
        "badge": "C-6.1 • Peak Frequency Mode",
        "summary": "The Mode is the observation that occurs with the greatest frequency in a dataset—it represents the point of maximum frequency concentration. Modal Classifications: (1) Unimodal: A distribution with a single distinct peak frequency (e.g., 2, 3, 3, 3, 5, 8 has mode = 3); (2) Bimodal: A distribution with two distinct values sharing the same maximum frequency (e.g., 1, 2, 2, 4, 5, 5, 7 has modes 2 and 5); (3) Multimodal: Having three or more peaks; (4) No Mode: When every observation appears with identical frequency (e.g., 4, 7, 9, 12 each appearing once). Qualitative Data Advantage: While Mean and Median require numerical values, Mode is the ONLY measure of central tendency that can be used for nominal (categorical non-numerical) data—such as finding the most popular shoe size sold in a retail store (size 8), the most requested car color (white), or the winning candidate in an election.",
        "key_points": [
            "Definition of Mode: The value that appears most often (highest frequency count) in the dataset.",
            "Modal Types: Distributions can be Unimodal (one peak), Bimodal (two peaks), Multimodal, or have No Mode.",
            "Nominal / Qualitative Applicability: The only central tendency measure applicable to non-numeric categorical data.",
            "Simplicity: Easily identified from a frequency table by finding the value with the highest f_i.",
            "Commercial Utility: Crucial for retail inventory restocking, fashion manufacturing, and production planning."
        ],
        "narration": "What is the most popular sneaker size in a shoe shop? You wouldn't calculate an average size of 8.37—nobody can buy size 8.37! You want the Mode: the single size that sells the most. Mode is the crowd favorite, the peak of the mountain. And unlike mean or median, mode is the only measure that works on non-numbers, like finding the favorite ice cream flavor. Test unimodal, bimodal, and no-mode distributions on our interactive frequency peak detector!",
        "sim_title": "Interactive Frequency Bar Peak & Mode Detector",
        "checkpoints": [
            {
                "q": "What is the mode of the numbers: 2, 4, 4, 6, 7, 4, 8, 9, 4, 7, 6?",
                "options": ["4", "6", "7", "9"],
                "ans": 0,
                "exp": "Count frequencies: 2 occurs once, 6 occurs twice, 7 occurs twice, 8 occurs once, 9 occurs once, and 4 occurs four times. Since 4 has the highest frequency (4), Mode = 4."
            },
            {
                "q": "A shirt manufacturer needs to decide which collar sizes to mass produce in the largest quantity. Which measure of central tendency should guide this decision?",
                "options": ["Mean", "Median", "Mode", "Range"],
                "ans": 2,
                "exp": "The Mode indicates the most popular or frequently purchased collar size, making it the decisive metric for manufacturing and inventory stocking."
            }
        ]
    },
    {
        "id": 13,
        "title": "Sensitivity to Outliers & Measure Robustness",
        "subtitle": "The 'Billionaire in the Diner' Phenomenon — Mean Distortion vs Median Invariance",
        "category": "Comparative Analysis",
        "badge": "CG-9 • Robustness Under Extremes",
        "summary": "An Outlier is an extreme observation that lies an abnormal distance away from the rest of the values in a dataset. The three measures of central tendency respond to outliers with fundamentally different levels of robustness: (1) Arithmetic Mean is Highly Sensitive (Non-Robust): Because every single value enters the summation ∑ x_i, a single massive outlier pulls the mean heavily toward itself, producing a misleading impression of the typical value; (2) Median is Extremely Robust (Resistant): Since median depends only on rank positions, replacing the highest value with an enormous number leaves the middle position completely unchanged; (3) Mode is Highly Resistant: An outlier does not alter the frequency peak unless the outlier itself repeats more times than the modal frequency. Classic Thought Experiment: 9 teachers earn ₹40,000/month. If a billionaire earning ₹10 Crores walks into the room, the Mean income jumps to over ₹1 Crore (falsely suggesting all are wealthy), while the Median stays at ₹40,000.",
        "key_points": [
            "Outlier Definition: An extreme data point far removed from the general cluster of observations.",
            "Mean Vulnerability: Highly distorted by extreme values because every observation directly affects ∑ x_i.",
            "Median Robustness: Resistant to outliers; rank ordering ensures the middle element remains stable.",
            "Mode Stability: Unaffected by extreme values unless the outlier frequency exceeds the original mode.",
            "Practical Rule: Always inspect for skewness and outliers before deciding between Mean and Median."
        ],
        "narration": "Here is one of the most famous traps in statistics! Imagine nine hardworking teachers sitting in a cafe, each earning 40,000 rupees a month. Suddenly, a billionaire earning 10 crore rupees walks in. If you calculate the average income, everyone suddenly looks like a multi-millionaire! That is the vulnerability of the Mean—it gets dragged away by extreme outliers. But the Median? It stays rock-solid at 40,000. Drag the billionaire slider in our experiment to see the Mean skyrocket while the Median stays calm!",
        "sim_title": "The Billionaire in the Room Outlier Experiment",
        "checkpoints": [
            {
                "q": "In a company, 9 employees earn ₹30,000 each and the managing director earns ₹5,00,000. Which measure of central tendency best represents the typical worker's salary?",
                "options": ["Mean", "Median", "Range", "Standard Deviation"],
                "ans": 1,
                "exp": "Because the director's ₹5,00,000 is an extreme outlier that artificially inflates the mean to ₹77,000, the Median (₹30,000) provides a far more accurate representation of typical salary."
            },
            {
                "q": "If the largest value in an ordered dataset of 25 numbers is multiplied by 1,000, what happens to the median?",
                "options": [
                    "It increases by 1,000 times",
                    "It increases slightly",
                    "It remains completely unchanged",
                    "It becomes zero"
                ],
                "ans": 2,
                "exp": "The median depends exclusively on the 13th ranked position (for n = 25). Changing the magnitude of the 25th (highest) observation does not alter the 13th observation; hence the median remains unchanged."
            }
        ]
    },
    {
        "id": 14,
        "title": "Empirical Relationship & Distribution Skewness",
        "subtitle": "Karl Pearson's Empirical Rule: Mode ≈ 3 Median - 2 Mean Across Asymmetric Distributions",
        "category": "Theoretical Relationships",
        "badge": "CG-9 • Distribution Geometry",
        "summary": "For moderately skewed (asymmetrical) continuous frequency distributions, the English statistician Karl Pearson established a celebrated empirical relationship connecting the three measures of central tendency: Mode ≈ 3 · Median - 2 · Mean; or equivalently, Mean - Mode ≈ 3 · (Mean - Median). Three Fundamental Distribution Shapes: (1) Symmetrical Distribution (Bell-Shaped / Normal): The left and right halves are mirror images. The mean, median, and mode coincide at the exact same central point: Mean = Median = Mode; (2) Positively Skewed (Right-Tailed): The tail stretches out to the right toward high positive values (e.g., household wealth). The extreme high values pull the mean rightward: Mean > Median > Mode; (3) Negatively Skewed (Left-Tailed): The tail stretches out to the left toward low values (e.g., age at death in developed countries). Extreme low values pull the mean leftward: Mode > Median > Mean.",
        "key_points": [
            "Empirical Formula: Mode ≈ 3 · Median - 2 · Mean (valid for unimodal, moderately skewed curves).",
            "Symmetrical Distribution: Symmetrical bell curve where Mean = Median = Mode at the central apex.",
            "Positively Skewed (Right-Tailed): Asymmetry with right tail; ordering is Mode < Median < Mean.",
            "Negatively Skewed (Left-Tailed): Asymmetry with left tail; ordering is Mean < Median < Mode.",
            "Algebraic Power: Allows estimation of an unknown measure when two of the three measures are given."
        ],
        "narration": "Can you guess the mode if you only know the mean and median? Yes! Karl Pearson discovered an empirical rule: Mode is approximately 3 times the Median minus 2 times the Mean. In a perfectly balanced bell curve, all three sit right at the peak together. But when data stretches out with a long tail to the right—like wealth or salaries—the Mean gets dragged furthest out into the tail, the Median follows halfway, and the Mode stays at the highest peak. Morph the distribution in our simulator to verify Pearson's rule!",
        "sim_title": "Interactive Skewness Curve & Karl Pearson Verifier",
        "checkpoints": [
            {
                "q": "In a moderately skewed distribution, the mean is 45 and the median is 48. What is the approximate value of the mode?",
                "options": ["51", "54", "57", "60"],
                "ans": 1,
                "exp": "Using Karl Pearson's empirical formula: Mode ≈ 3 · Median - 2 · Mean = 3(48) - 2(45) = 144 - 90 = 54."
            },
            {
                "q": "In a positively skewed (right-tailed) distribution, which of the following relationships holds true?",
                "options": [
                    "Mean = Median = Mode",
                    "Mean > Median > Mode",
                    "Mode > Median > Mean",
                    "Median > Mean > Mode"
                ],
                "ans": 1,
                "exp": "In a right-skewed distribution, extreme high values in the right tail pull the mean furthest to the right, followed by the median, with the mode remaining at the highest frequency peak: Mean > Median > Mode."
            }
        ]
    },
    {
        "id": 15,
        "title": "Decision-Making Framework: Choosing the Right Measure",
        "subtitle": "Navigating Real-World Scenarios in Economics, Public Health, Commerce & Education",
        "category": "Decision-Making Strategy",
        "badge": "C-6.1 • Applied Decision Science",
        "summary": "Data scientists, policy makers, and business leaders must choose the most honest and effective measure of central tendency based on the scale of measurement and data distribution characteristics. The Decision Matrix: (1) Choose Arithmetic Mean when: The data is continuous/interval, roughly symmetric, contains NO severe outliers, and every observation's magnitude contributes to an aggregate budget or inventory total (e.g., average monthly rainfall, overall exam grade point averages, machine part tolerance averages); (2) Choose Median when: The distribution is skewed, contains extreme outliers, or represents ordinal data where rank ordering matters (e.g., national household incomes, real estate house sale prices, hospital patient recovery times, website page load speeds); (3) Choose Mode when: Working with categorical (nominal) data, identifying the most popular commodity, or optimizing inventory supply chains (e.g., shoe sizing, bus timetable scheduling, election polls); (4) Choose Weighted Mean when items have unequal units of credit or economic shares.",
        "key_points": [
            "Context-Driven Choice: No single measure is universally best; choice depends on distribution shape and operational goals.",
            "Mean for Totals: Optimal when total sum (N · x̄) is meaningful, such as total electricity consumed or company payroll.",
            "Median for Typicality: Optimal when extreme outliers skew the picture, reflecting the genuine experience of the typical person.",
            "Mode for Supply Chains: Essential for discrete stock orders, shelf space allocation, and popular choice voting.",
            "Weighted Mean for Policy: Essential for CPI indices, academic honors rankings, and composite safety scores."
        ],
        "narration": "If a government announces that average household income is rising, does that mean ordinary families are better off? Not necessarily—if billionaires are getting richer, the mean climbs while ordinary wages stagnate! That is why real estate and income statistics always report the Median. Meanwhile, shoe retailers stock shelves using the Mode, and schools calculate honours using the Weighted Average. Test your statistical intuition against our interactive real-world decision matrix!",
        "sim_title": "Interactive Real-World Scenario Selector & Recommender",
        "checkpoints": [
            {
                "q": "A real estate analyst is reporting on housing affordability in a city where 5 luxury mansions sold for ₹50 Crores while 100 apartments sold for ₹40 Lakhs. Which measure of central tendency should be reported to prospective homebuyers?",
                "options": ["Mean", "Median", "Mode", "Standard Deviation"],
                "ans": 1,
                "exp": "The Median house price should be reported because the luxury mansions are massive outliers that distort the mean house price upward, misrepresenting genuine affordability."
            },
            {
                "q": "An airline needs to calculate the total fuel required for a fleet of 50 flights based on past fuel consumption. Which measure of central tendency is required?",
                "options": ["Mode", "Median", "Arithmetic Mean", "Range"],
                "ans": 2,
                "exp": "The Arithmetic Mean is required because Total Fuel = Number of Flights × Mean Fuel Consumption per flight (Total = N · x̄)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking in Statistics: Algorithms & Data Pipelines",
        "subtitle": "Sorting Complexities, Hash Map Frequency Counters, Accumulators & Live Visualizer",
        "category": "Computational Thinking",
        "badge": "CG-9 • Algorithmic Pipelines",
        "summary": "Computational thinking operationalizes statistical analysis through systematic algorithmic pipelines: (1) Mean Computation: An Accumulator Loop iterates through n elements in linear time O(n), summing values before dividing by n; (2) Median Computation: Requires a Sorting Algorithm (such as QuickSort or MergeSort) with time complexity O(n log n). Once sorted, array indexing allows O(1) instant retrieval of the middle element (or average of two middle elements); (3) Mode Computation: A Hash Map (or Dictionary) counts frequencies in O(n) time and finds the key with maximum count; (4) Floating-Point Rounding & Edge Cases: Managing rounding precision errors (e.g., 0.1 + 0.2 ≠ 0.3 in IEEE 754 float), zero denominators, and tie-breaking for multimodal distributions; (5) Data Cleaning Pipelines: Detecting missing values (null/NaN) and filtering extreme measurement artifacts. Modern data science libraries (Python Pandas, NumPy) execute these algorithms across billions of rows in parallel computing clusters.",
        "key_points": [
            "Mean Algorithm: Linear Accumulator loop running in O(n) time and O(1) auxiliary space.",
            "Median Algorithm: Comparison sorting pipeline running in O(n log n) time followed by O(1) index retrieval.",
            "Mode Algorithm: Hash Map frequency counter dictionary operating in O(n) time and O(k) space.",
            "Floating-Point Precision: Handling machine epsilon and rounding in floating-point statistical computations.",
            "Full Pipeline: Data Input → Cleaning/Validation → Sorting & Frequency Map → Central Tendency Outputs → Dynamic Plotting."
        ],
        "narration": "In the era of big data, computers process millions of data points every second using computational thinking! To find the mean, an accumulator loop sums values in O(n) time. To find the median, an efficient sorting algorithm like QuickSort arranges elements in O(n log n) time. And to find the mode, a hash map tracks frequencies instantly. Type any custom list of numbers into our live algorithmic laboratory to watch these algorithms execute and visualize the results simultaneously!",
        "sim_title": "Interactive Computational Statistics Engine & Live Visualizer",
        "checkpoints": [
            {
                "q": "What is the theoretical time complexity of finding the median of an unsorted array of n numbers using a standard comparison sorting algorithm (e.g., MergeSort)?",
                "options": ["O(1)", "O(n)", "O(n log n)", "O(n²)"],
                "ans": 2,
                "exp": "Sorting the array with MergeSort takes O(n log n) time. After sorting, accessing the middle element takes O(1) time; hence total time complexity is O(n log n)."
            },
            {
                "q": "Which computational data structure is optimal for determining the mode of a large discrete dataset in O(n) linear time?",
                "options": ["Binary Search Tree", "Hash Map (Frequency Dictionary)", "Linked List", "Stack"],
                "ans": 1,
                "exp": "A Hash Map (dictionary) allows insertion and frequency increments in average O(1) time per item, tallying all n elements in O(n) total time."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 1,
        "title": "Mastery Challenge 1: Data Collection, Bar Graphs & Stacked Charts",
        "badge": "Quiz 1 • Fundamentals & Charts",
        "questions": [
            {
                "q": "1. In the PPDAC statistical inquiry framework, which stage involves formulating the research hypothesis and defining precise investigative questions?",
                "options": ["Plan", "Problem", "Analysis", "Conclusion"],
                "ans": 1,
                "solution": "Step 1: The PPDAC cycle consists of Problem, Plan, Data, Analysis, and Conclusion.\nStep 2: The 'Problem' phase specifies the research objectives, target population, and precise questions to be answered.\nStep 3: Therefore, the correct stage is 'Problem'."
            },
            {
                "q": "2. Data extracted from the Census of India published report by a student researcher is classified as:",
                "options": ["Primary Data", "Secondary Data", "Raw Experimental Data", "Continuous Data"],
                "ans": 1,
                "solution": "Step 1: Primary data is collected firsthand by the investigator.\nStep 2: Secondary data is sourced from existing publications, government archives, or prior reports.\nStep 3: A published Census report is Secondary Data."
            },
            {
                "q": "3. The weights (in kg) of 8 students are: 45, 52, 38, 61, 49, 55, 34, 58. What is the range of this dataset?",
                "options": ["23 kg", "25 kg", "27 kg", "29 kg"],
                "ans": 2,
                "solution": "Step 1: Identify maximum observation: Max = 61 kg.\nStep 2: Identify minimum observation: Min = 34 kg.\nStep 3: Range = Max - Min = 61 - 34 = 27 kg."
            },
            {
                "q": "4. In a standard vertical bar graph, the widths of the bars:",
                "options": [
                    "Must be strictly equal for all categories",
                    "Must be proportional to the category frequency",
                    "Can be arbitrary and different for each bar",
                    "Must equal the space between bars"
                ],
                "ans": 0,
                "solution": "Step 1: In a bar graph, width carries no mathematical weight; it serves purely for visual clarity.\nStep 2: To avoid misleading visual prominence, all bars must have identical (uniform) width.\nStep 3: The correct option is that bar widths must be strictly equal."
            },
            {
                "q": "5. On a bar graph scale where 1 unit length = 200 trees, what height bar represents 1,400 trees?",
                "options": ["5 units", "6 units", "7 units", "8 units"],
                "ans": 2,
                "solution": "Step 1: Scale factor = 200 trees per unit.\nStep 2: Bar height = Total frequency / Scale factor = 1,400 / 200 = 7 units."
            },
            {
                "q": "6. A stacked bar graph shows total energy generation of 80 GW for a region. If Hydroelectric spans 0 to 25 GW, Thermal spans 25 to 65 GW, and Solar forms the remainder, what is Solar capacity?",
                "options": ["10 GW", "15 GW", "20 GW", "25 GW"],
                "ans": 1,
                "solution": "Step 1: Thermal ends at 65 GW, which is the lower boundary for Solar.\nStep 2: The total bar ends at 80 GW, which is the upper boundary for Solar.\nStep 3: Solar capacity = 80 - 65 = 15 GW."
            },
            {
                "q": "7. In a 100% stacked bar graph representing school transport, Grade 9 has 50 bus riders, 30 walkers, and 20 cyclists (total 100). Grade 10 has 120 bus riders, 50 walkers, and 30 cyclists (total 200). What are the percentage heights of bus riders for Grade 9 and Grade 10?",
                "options": ["50% and 60%", "50% and 50%", "40% and 60%", "30% and 50%"],
                "ans": 0,
                "solution": "Step 1: Grade 9 bus percentage = (50 / 100) × 100% = 50%.\nStep 2: Grade 10 bus percentage = (120 / 200) × 100% = 0.60 × 100% = 60%.\nStep 3: The respective heights are 50% and 60%."
            },
            {
                "q": "8. What is the key advantage of a 100% stacked bar chart compared to a standard stacked bar chart?",
                "options": [
                    "It displays the absolute magnitudes of populations directly",
                    "It allows direct comparison of percentage composition across groups of disparate sizes",
                    "It requires no vertical scale",
                    "It can only have two categories"
                ],
                "ans": 1,
                "solution": "Step 1: Standard stacked bars emphasize total absolute magnitude, which overshadows small cohorts.\nStep 2: A 100% stacked bar scales all bars to 100%, enabling fair visual comparison of relative proportions across unequal total sizes."
            },
            {
                "q": "9. A survey recorded tally marks for family vehicle ownership: '|||| |||| |||'. What is the frequency?",
                "options": ["11", "12", "13", "14"],
                "ans": 2,
                "solution": "Step 1: Each bundle of '||||' crossed represents 5.\nStep 2: Two bundles of 5 = 5 + 5 = 10.\nStep 3: Three single tallies '|||' = 3.\nStep 4: Total frequency = 10 + 3 = 13."
            },
            {
                "q": "10. Which visual element on an axis indicates that the scale has omitted numbers between 0 and the first marked value?",
                "options": ["Arrowhead", "Kink (zigzag / axis break)", "Gridline", "Legend"],
                "ans": 1,
                "solution": "Step 1: When an axis does not begin continuously from zero, plotting without indication creates false proportions.\nStep 2: A kink (zigzag break line) is drawn to alert viewers that a range of values near zero has been skipped."
            }
        ]
    },
    {
        "id": 2,
        "title": "Mastery Challenge 2: Histograms, Frequency Density & Polygons",
        "badge": "Quiz 2 • Histograms & Polygons",
        "questions": [
            {
                "q": "11. Why are there NO gaps between adjacent rectangles in a histogram?",
                "options": [
                    "To save horizontal page space",
                    "Because the data variable is continuous across adjacent intervals",
                    "Because all frequencies are greater than zero",
                    "Because bar widths are always equal"
                ],
                "ans": 1,
                "solution": "Step 1: Histograms represent continuous quantitative variables where one interval ends exactly where the next begins.\nStep 2: Therefore, adjacent rectangles touch each other with zero gaps."
            },
            {
                "q": "12. What is the class mark of the class interval 120 - 150?",
                "options": ["130", "135", "140", "145"],
                "ans": 1,
                "solution": "Step 1: Class mark = (Lower limit + Upper limit) / 2.\nStep 2: (120 + 150) / 2 = 270 / 2 = 135."
            },
            {
                "q": "13. The class intervals of a distribution are: 10-19, 20-29, 30-39. What is the true lower boundary of the second class (20-29)?",
                "options": ["19.0", "19.5", "20.0", "20.5"],
                "ans": 1,
                "solution": "Step 1: Gap between classes = 20 - 19 = 1.\nStep 2: Half-gap correction = 1 / 2 = 0.5.\nStep 3: True lower boundary = 20 - 0.5 = 19.5."
            },
            {
                "q": "14. In a histogram with unequal class widths, the minimum class width is 10. For an interval of width 25 having frequency 50, what is the adjusted frequency for drawing the rectangle?",
                "options": ["15", "20", "25", "30"],
                "ans": 1,
                "solution": "Step 1: Adjusted Frequency = (Minimum Class Width / Class Width of Interval) × Frequency.\nStep 2: Adjusted Frequency = (10 / 25) × 50 = 0.40 × 50 = 20."
            },
            {
                "q": "15. The fundamental mathematical principle governing all histograms is that the area of each rectangle is proportional to:",
                "options": ["Class width", "Class mark", "Frequency of the class", "Total number of classes"],
                "ans": 2,
                "solution": "Step 1: Unlike a bar graph where height reflects frequency, a histogram's fundamental law is Area ∝ Frequency.\nStep 2: Adjusting heights for varying widths ensures that the drawn area strictly reflects class frequency."
            },
            {
                "q": "16. To draw a frequency polygon directly without constructing a histogram, what coordinates are plotted for each class?",
                "options": ["(Lower Limit, Frequency)", "(Upper Limit, Frequency)", "(Class Mark, Frequency)", "(Class Width, Frequency)"],
                "ans": 2,
                "solution": "Step 1: A frequency polygon connects midpoints of class intervals at heights corresponding to frequency.\nStep 2: The plotted coordinates are (Class Mark, Frequency) = (x_i, f_i)."
            },
            {
                "q": "17. A histogram has first class interval 20 - 30 (width 10). To close the frequency polygon at the lower end, to which point on the baseline is the polygon connected?",
                "options": ["(20, 0)", "(15, 0)", "(10, 0)", "(25, 0)"],
                "ans": 1,
                "solution": "Step 1: The imaginary preceding class interval of the same width (10) is 10 - 20.\nStep 2: Midpoint of 10 - 20 is (10 + 20) / 2 = 15.\nStep 3: Connected at frequency 0, the point is (15, 0)."
            },
            {
                "q": "18. The total area enclosed by a properly closed frequency polygon and the horizontal axis is:",
                "options": [
                    "Half the area of the corresponding histogram",
                    "Exactly equal to the area of the corresponding histogram",
                    "Twice the area of the corresponding histogram",
                    "Dependent on the number of classes"
                ],
                "ans": 1,
                "solution": "Step 1: By the baseline closure rule, the triangular areas clipped off the histogram bars are congruent to the triangular areas added outside.\nStep 2: Hence, the total enclosed area remains exactly equal to the total area of the histogram."
            },
            {
                "q": "19. If class marks of a distribution are 15, 25, 35, 45, what is the class width and the first class interval?",
                "options": [
                    "Width = 10, Interval = 10 - 20",
                    "Width = 10, Interval = 5 - 15",
                    "Width = 5, Interval = 12.5 - 17.5",
                    "Width = 10, Interval = 15 - 25"
                ],
                "ans": 0,
                "solution": "Step 1: Difference between consecutive class marks = 25 - 15 = 10 (Class Width h = 10).\nStep 2: Half-width = 10 / 2 = 5.\nStep 3: First interval lower limit = 15 - 5 = 10; upper limit = 15 + 5 = 20. Interval is 10 - 20."
            },
            {
                "q": "20. Frequency density is defined as:",
                "options": [
                    "Frequency × Class Width",
                    "Frequency / Class Width",
                    "Class Width / Frequency",
                    "Cumulative Frequency / Total Frequency"
                ],
                "ans": 1,
                "solution": "Step 1: Frequency density represents frequency per unit width of the class interval.\nStep 2: Formula: Frequency Density = Frequency / Class Width."
            }
        ]
    },
    {
        "id": 3,
        "title": "Mastery Challenge 3: Measures of Central Tendency & Weighted Average",
        "badge": "Quiz 3 • Mean, Median & Weights",
        "questions": [
            {
                "q": "21. The mean of 6 numbers is 24. If one number is removed, the mean of the remaining 5 numbers is 22. What was the removed number?",
                "options": ["30", "32", "34", "36"],
                "ans": 2,
                "solution": "Step 1: Total sum of 6 numbers = 6 × 24 = 144.\nStep 2: Total sum of remaining 5 numbers = 5 × 22 = 110.\nStep 3: Removed number = 144 - 110 = 34."
            },
            {
                "q": "22. The algebraic sum of deviations of 15 observations from their arithmetic mean is:",
                "options": ["15", "1", "0", "-15"],
                "ans": 2,
                "solution": "Step 1: Property of arithmetic mean: ∑ (x_i - x̄) = ∑ x_i - ∑ x̄ = n x̄ - n x̄ = 0.\nStep 2: The algebraic sum of deviations from the mean is always identically 0."
            },
            {
                "q": "23. If the mean of numbers x, x+3, x+6, x+9, x+12 is 18, what is the value of x?",
                "options": ["10", "12", "14", "16"],
                "ans": 1,
                "solution": "Step 1: Sum = 5x + (3 + 6 + 9 + 12) = 5x + 30.\nStep 2: Mean = (5x + 30) / 5 = x + 6.\nStep 3: Set x + 6 = 18 ⇒ x = 18 - 6 = 12."
            },
            {
                "q": "24. In an exam evaluation, Theory (out of 100) carries weight 70% and Practical (out of 100) carries weight 30%. If a student scores 80 in Theory and 90 in Practical, what is their weighted average score?",
                "options": ["81", "83", "85", "87"],
                "ans": 1,
                "solution": "Step 1: x̄_w = (w_1 x_1 + w_2 x_2) / (w_1 + w_2).\nStep 2: x̄_w = (70 × 80 + 30 × 90) / 100 = (5600 + 2700) / 100 = 8300 / 100 = 83."
            },
            {
                "q": "25. What is the median of the following dataset: 41, 43, 127, 99, 61, 92, 71, 58, 57?",
                "options": ["58", "61", "71", "92"],
                "ans": 1,
                "solution": "Step 1: Sort in ascending order: 41, 43, 57, 58, 61, 71, 92, 99, 127.\nStep 2: Count n = 9 (odd).\nStep 3: Median position = (9 + 1) / 2 = 5th term.\nStep 4: 5th term = 61."
            },
            {
                "q": "26. What is the median of the first 10 even positive integers (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)?",
                "options": ["10", "11", "12", "13"],
                "ans": 1,
                "solution": "Step 1: The numbers are already sorted: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Count n = 10 (even).\nStep 2: Middle terms are (10/2) = 5th term (10) and (5+1) = 6th term (12).\nStep 3: Median = (10 + 12) / 2 = 22 / 2 = 11."
            },
            {
                "q": "27. For a discrete frequency distribution with total frequency N = 50, the median is the value corresponding to which cumulative frequency threshold?",
                "options": ["N = 50", "N/2 = 25", "N/4 = 12.5", "3N/4 = 37.5"],
                "ans": 1,
                "solution": "Step 1: In a cumulative frequency table, the median partitions the total frequency into two equal halves.\nStep 2: It is located at the class where cumulative frequency first equals or exceeds N/2 = 25."
            },
            {
                "q": "28. Find the mode of the dataset: 14, 25, 14, 28, 18, 17, 18, 14, 23, 22, 14, 18.",
                "options": ["14", "18", "22", "Bimodal (14 and 18)"],
                "ans": 0,
                "solution": "Step 1: Count occurrences: 14 occurs 4 times; 18 occurs 3 times; 17, 22, 23, 25, 28 occur once each.\nStep 2: Since 14 has the highest frequency (4), Mode = 14 (it is unimodal)."
            },
            {
                "q": "29. If every observation in a dataset is increased by 7, how do the Mean, Median, and Mode change?",
                "options": [
                    "Only Mean increases by 7",
                    "All three (Mean, Median, and Mode) increase by 7",
                    "Mean and Median increase by 7, but Mode remains constant",
                    "None of them change"
                ],
                "ans": 1,
                "solution": "Step 1: Shifting every data point x_i → x_i + c translates the entire distribution uniformly.\nStep 2: The center of gravity shifts by c (Mean + 7).\nStep 3: The rank ordering positions shift by c (Median + 7).\nStep 4: The peak frequency location shifts by c (Mode + 7).\nStep 5: All three increase by exactly 7."
            },
            {
                "q": "30. The only measure of central tendency that can be used to describe categorical/nominal qualitative data is:",
                "options": ["Arithmetic Mean", "Median", "Mode", "Weighted Mean"],
                "ans": 2,
                "solution": "Step 1: Mean and Weighted Mean require addition and division of numbers.\nStep 2: Median requires numerical ranking/sorting.\nStep 3: Mode identifies the most frequent category and therefore works on non-numerical labels (e.g., eye color, blood group)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Mastery Challenge 4: Outliers, Skewness & Decision-Making",
        "badge": "Quiz 4 • Advanced Synthesis",
        "questions": [
            {
                "q": "31. In a distribution of 50 values, the maximum value is 85. If an error is corrected and 85 is replaced by 185, what happens to the Median?",
                "options": [
                    "It increases by 100",
                    "It increases by 2",
                    "It remains unchanged",
                    "It cannot be determined"
                ],
                "ans": 2,
                "solution": "Step 1: The median is determined by the 25th and 26th ranked observations.\nStep 2: Replacing the 50th (highest) value with a still higher value does not change the identity or value of the 25th or 26th observation.\nStep 3: Hence, the median remains completely unchanged."
            },
            {
                "q": "32. In a moderately skewed distribution, if the Mean is 32 and the Median is 30, what is the approximate Mode according to Karl Pearson's empirical formula?",
                "options": ["24", "26", "28", "31"],
                "ans": 1,
                "solution": "Step 1: Empirical formula: Mode ≈ 3 · Median - 2 · Mean.\nStep 2: Substitute Median = 30 and Mean = 32: Mode ≈ 3(30) - 2(32) = 90 - 64 = 26."
            },
            {
                "q": "33. In a perfectly symmetric bell-shaped distribution:",
                "options": [
                    "Mean > Median > Mode",
                    "Mode > Median > Mean",
                    "Mean = Median = Mode",
                    "Mean + Mode = Median"
                ],
                "ans": 2,
                "solution": "Step 1: A symmetric distribution has identical left and right halves.\nStep 2: The peak frequency (Mode), the 50th percentile divider (Median), and the center of mass (Mean) all coincide at the exact center: Mean = Median = Mode."
            },
            {
                "q": "34. If the Mean of a distribution is 55, Median is 50, and Mode is 40, the distribution is:",
                "options": ["Symmetric", "Positively Skewed (Right-Tailed)", "Negatively Skewed (Left-Tailed)", "Bimodal"],
                "ans": 1,
                "solution": "Step 1: Check ordering: Mean (55) > Median (50) > Mode (40).\nStep 2: When Mean > Median > Mode, the long tail stretches to the right.\nStep 3: The distribution is Positively Skewed (Right-Tailed)."
            },
            {
                "q": "35. A government agency is reporting household income to evaluate poverty alleviation. Why is the Median income preferred over the Mean income?",
                "options": [
                    "Median is easier to compute on computers",
                    "A few multi-billionaires artificially drag the Mean upward, while the Median reflects the typical family",
                    "Mean cannot be calculated for large populations",
                    "Median is always larger than Mean"
                ],
                "ans": 1,
                "solution": "Step 1: Income distributions are severely positively skewed with extreme upper outliers.\nStep 2: The Mean is pulled up by extreme wealth, creating a false illusion of widespread prosperity.\nStep 3: The Median is resistant to outliers and honestly reflects the experience of the typical household."
            },
            {
                "q": "36. A ready-made garments retailer wants to determine which T-shirt sizes to keep in stock. Which measure of central tendency is most relevant?",
                "options": ["Mean", "Median", "Mode", "Weighted Mean"],
                "ans": 2,
                "solution": "Step 1: The retailer needs to know which specific sizes sell in the highest volume.\nStep 2: The Mode represents the most frequently purchased size (e.g., Size L).\nStep 3: Mode governs retail inventory decisions."
            },
            {
                "q": "37. An electricity board needs to determine the total power generation required next month for a town of 10,000 households. The board should base its projection on:",
                "options": ["The Mode of household consumption", "The Median of household consumption", "The Arithmetic Mean of household consumption", "The Range of household consumption"],
                "ans": 2,
                "solution": "Step 1: Total power needed = Number of households × Average consumption per household.\nStep 2: Since Total = N · x̄, the Arithmetic Mean is the mathematically required metric for computing aggregate sums."
            },
            {
                "q": "38. What is the time complexity of computing the Arithmetic Mean of an array of n numbers using an accumulator loop?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "ans": 2,
                "solution": "Step 1: An accumulator loop visits each of the n elements exactly once to add it to a running sum.\nStep 2: Dividing the final sum by n takes O(1) time.\nStep 3: Total time complexity is linear O(n)."
            },
            {
                "q": "39. For an array of numbers [7, 2, 9, 4, 9, 2, 9, 5], what does a hash map frequency counter return as the maximum frequency key (Mode)?",
                "options": ["2", "4", "5", "9"],
                "ans": 3,
                "solution": "Step 1: Build frequency map: {7: 1, 2: 2, 9: 3, 4: 1, 5: 1}.\nStep 2: The maximum frequency is 3, corresponding to key 9.\nStep 3: The mode is 9."
            },
            {
                "q": "40. If a distribution has Mean = 28 and Mode = 25, what is the estimated Median using Karl Pearson's empirical rule?",
                "options": ["26", "27", "28", "29"],
                "ans": 1,
                "solution": "Step 1: Pearson's formula: Mode ≈ 3 · Median - 2 · Mean.\nStep 2: 25 ≈ 3 · Median - 2(28) ⇒ 25 ≈ 3 · Median - 56.\nStep 3: 3 · Median ≈ 25 + 56 = 81 ⇒ Median ≈ 81 / 3 = 27."
            }
        ]
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(SLIDES)} slides, {len(QUIZZES)} quiz challenge slides.")
    total_cp = sum(len(s['checkpoints']) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    total_qz = sum(len(q['questions']) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, f"Expected 16 content slides, got {len(SLIDES)}"
    assert total_cp == 32, f"Expected 32 checkpoints, got {total_cp}"
    assert len(QUIZZES) == 4, f"Expected 4 quiz challenge slides, got {len(QUIZZES)}"
    assert total_qz == 40, f"Expected 40 quiz questions, got {total_qz}"
    print("All statistics data assertions passed cleanly!")


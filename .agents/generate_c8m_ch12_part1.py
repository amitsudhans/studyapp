#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 12: Tales by Dots and Lines
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 12 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Mean Fulcrum Balance",
        "subtitle": "Section 5.1 The Balancing Act: Arithmetic Mean as Physical Fulcrum Where LHS Distance = RHS Distance",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Twelve: Tales by Dots and Lines! Open Section Five Point One—The Balancing Act—by seeing the arithmetic mean not merely as a division formula, but as a living physical seesaw! Picture values plotted cleanly as dots resting upon a horizontal number line plank! Where must you place one triangular wooden fulcrum beneath that number line so the plank balances completely level without tipping left or right? RIGHT AT THE ARITHMETIC MEAN! "
            "Verify this distance-balance law immediately with a small dot set: suppose four scores sit at 2, 4, 8, and 10! First compute their arithmetic mean: (2 + 4 + 8 + 10) ÷ 4 = 24 ÷ 4 = 6! Place your fulcrum cleanly at position 6! Now measure every dot's exact horizontal distance away from fulcrum 6! On the left-hand side (LHS), dot 2 sits 4 units left and dot 4 sits 2 units left—summing LHS distances to 4 + 2 = 6 units! On the right-hand side (RHS), dot 8 sits 2 units right and dot 10 sits 4 units right—summing RHS distances to 2 + 4 = 6 units! Notice the magic: total LHS distance ALWAYS equals total RHS distance at the mean!"
        ),
        "checkpoints": [
            {
                "question": "Dots sit on a horizontal number line at 3, 5, 10, and 14. Where must the balance fulcrum (mean) be placed so total LHS distance equals total RHS distance?",
                "options": [
                    "At 8   (LHS distances 5+3=8 match RHS distances 2+6=8)",
                    "At 7.5   (midpoint between 5 and 10)",
                    "At 9   (middle of 3 and 14)",
                    "At 10"
                ],
                "answer": 0,
                "hint": "Add all 4 numbers and divide by 4, then check |3−8| + |5−8| vs |10−8| + |14−8|!",
                "explanation": "Mean = (3 + 5 + 10 + 14) ÷ 4 = 32 ÷ 4 = 8. LHS sum = (8−3)+(8−5) = 8; RHS sum = (10−8)+(14−8) = 8."
            },
            {
                "question": "If dots sit at 4, 6, and 11, where does the mean lie, and what happens if you place a fulcrum to the RIGHT of the mean?",
                "options": [
                    "Mean is 7; placing the fulcrum right of 7 makes the LHS heavier so the plank tips left",
                    "Mean is 6; placing the fulcrum right tips right",
                    "Mean is 8; both sides always stay level",
                    "Mean is 7.5; total LHS distance shrinks"
                ],
                "answer": 0,
                "hint": "(4 + 6 + 11) ÷ 3 = 7! Think which side gains extra distance weight when the fulcrum slides right!",
                "explanation": "Mean = 21 ÷ 3 = 7. Sliding the fulcrum right lengthens LHS distances and shortens RHS distances, tipping the beam left."
            }
        ]
    },
    {
        "id": 2,
        "title": "Inserting Removing Values",
        "subtitle": "Section 5.1 Behavior Under Data Changes: Inserting Values Above/Below Mean & Symmetric Balance Pairs",
        "speech": (
            "Now predict instantly how inserting or removing dots nudges our seesaw fulcrum! Suppose an archer's or basketball player's scores balance smoothly at an existing mean of 20 points! "
            "Rule One: INSERT A HIGHER VALUE! Add a fresh dot at 28 (strictly greater than 20)! Because 28 drops extra weight onto the RIGHT side of fulcrum 20, the seesaw tips right—forcing the balance fulcrum to slide UPWARD above 20! Rule Two: INSERT A LOWER VALUE! Add a dot at 12 (strictly smaller than 20), and the extra left-side weight pulls the mean DOWNWARD below 20! "
            "Rule Three: INSERT AT THE EXACT MEAN! Drop a brand-new dot right onto 20 itself: distance from fulcrum is ZERO, leaving the mean completely unchanged at 20! "
            "Rule Four: INSERT BALANCING SYMMETRIC PAIRS! Add two new dots standing EQUAL distances above and below 20—such as 14 (6 units left) together with 26 (6 units right)! Equal LHS and RHS lever torques cancel completely, locking the balance point completely unchanged right at 20! Conversely, removing an existing data value strictly higher than the mean pulls the fulcrum lower, whereas removing an existing value strictly lower than the mean shifts it upward cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Five quizzes have an arithmetic mean of 40. A student takes two extra quizzes and scores 33 and 47. What happens to the new 7-quiz mean?",
                "options": [
                    "Remains completely unchanged at 40   (33 is 7 below, 47 is 7 above!)",
                    "Increases above 40 because 47 > 40",
                    "Decreases below 40 because 33 < 40",
                    "Drops to 38"
                ],
                "answer": 0,
                "hint": "Compare how far 33 lies left of 40 vs how far 47 lies right of 40!",
                "explanation": "−7 and +7 balance symmetrically around mean 40 (sum adds 80 for 2 items → average 40), keeping the mean unchanged."
            },
            {
                "question": "A factory team averages 50 packages per hour across 6 days. If Day 7 produces 36 packages (below 50), what happens to the 7-day mean?",
                "options": [
                    "Decreases to 48   ((300 + 36) ÷ 7 = 336 ÷ 7)",
                    "Increases to 52",
                    "Remains unchanged at 50",
                    "Drops directly to 36"
                ],
                "answer": 0,
                "hint": "Inserting a score strictly below the current mean pulls the fulcrum leftward!",
                "explanation": "Old sum = 6 × 50 = 300; new sum = 300 + 36 = 336; new mean = 336 ÷ 7 = 48."
            }
        ]
    },
    {
        "id": 3,
        "title": "Linear Operations Mean",
        "subtitle": "Section 5.1 Linear Operations: Adding Constant c Shifts Mean by ±c; Scaling by k Multiplies Mean by k",
        "speech": (
            "Suppose a mathematics teacher awards every single student in a 30-pupil classroom +5 bonus marks—or scales every test score by multiplying by 2! Must we recompute every student's score from scratch just to find the new class mean? NOT AT ALL! Follow crisp LINEAR OPERATIONS on dot plots in Section Five Point One! "
            "Operation One: CONSTANT SHIFT (±c)! Picture sliding EVERY single dot on the number line plank together by exact distance +c to the right! Because every dot's spacing relative to its neighbors remains frozen identical, the entire dot constellation plus its balance fulcrum glide rigidly together by +c! Algebra proves why cleanly: adding c to n numbers increases their total sum by n·c, so dividing by n adds (n·c) ÷ n = +c directly to the old mean! Subtracting c shifts the mean down by −c! "
            "Operation Two: MULTIPLICATIVE SCALING (×k)! Multiply EVERY single data value cleanly by any positive scale factor k (such as doubling plant heights or converting metres to centimetres ×100)! Every individual numerical distance measured from zero and from the mean stretches equally by factor k—multiplying the entire arithmetic mean directly by EXACTLY k without ever altering relative proportional positions!"
        ),
        "checkpoints": [
            {
                "question": "A dataset of 12 measurements has mean 24. If you ADD +6 to every measurement and then MULTIPLY every result by 2, what is the new mean?",
                "options": [
                    "60   ((24 + 6) × 2 = 30 × 2)",
                    "54   (24 × 2 + 6)",
                    "30",
                    "48"
                ],
                "answer": 0,
                "hint": "Apply the operations to the mean in the exact order given: first +6, then ×2!",
                "explanation": "Adding +6 shifts mean from 24 to 30; multiplying every value by 2 scales mean 30 × 2 = 60."
            },
            {
                "question": "Why does subtracting 10 from every single value in a dataset shift the mean by −10 without changing how spread apart dots sit from the mean?",
                "options": [
                    "Every dot slides 10 units left together, preserving all pairwise spacings and fulcrum balance",
                    "Because 10 values drop out of the sum",
                    "Only values larger than 10 decrease",
                    "The fulcrum moves 10 units right while dots move left"
                ],
                "answer": 0,
                "hint": "Visualize sliding an entire dot plot 10 notches left on a rigid ruler!",
                "explanation": "Uniform translation shifts every point by −c, moving the balance point identically by −c while preserving distances."
            }
        ]
    },
    {
        "id": 4,
        "title": "Tinkering With Median",
        "subtitle": "Section 5.1 Tinkering with Median: Middle Position Shifts When Inserting or Removing Points",
        "speech": (
            "Unlike the mean—which pulls toward extreme giant or tiny numbers—meet the positional center in Section Five Point One: THE MEDIAN! Sort your data strictly from smallest to largest! For an odd count of values, the median sits cleanly on the middle value; for an even count, the median averages the two central values! "
            "Now tinker with the median carefully by inserting or removing single values! Take an ordered list of 5 numbers: 10, 12, 15, 20, 25—notice middle value Median = 15! What happens if you insert TWO numbers—one tiny number (2) below 15 AND one huge number (90) above 15—producing 2, 10, 12, 15, 20, 25, 90? Spot the magic: 15 STILL sits dead in the 4th middle slot! Adding balanced values on opposite sides leaves the median completely intact, even if 90 becomes 9,000! "
            "Wait—what happens if you insert just ONE single extra value strictly ABOVE 15 (say 18)? Now 6 ordered values give 10, 12, 15, 18, 20, 25, nudging the positional median gently upward to (15 + 18)/2 = 16.5! Removing values on one side only similarly shifts which ordered slot holds the median—whereas balanced removals from opposite ends protect the median!"
        ),
        "checkpoints": [
            {
                "question": "An ordered dataset is 8, 11, 14, 19, 23 (Median = 14). Which change keeps the median STRICTLY UNCHANGED at 14?",
                "options": [
                    "Inserting BOTH 3 (below 14) and 500 (above 14)",
                    "Inserting only 500 above 14",
                    "Removing 8 from the left end only",
                    "Replacing 14 with 18"
                ],
                "answer": 0,
                "hint": "Inserting one item on the left AND one item on the right keeps the middle rank anchored on 14!",
                "explanation": "In 3, 8, 11, 14, 19, 23, 500, 14 still occupies the 4th middle slot cleanly."
            },
            {
                "question": "Compare inserting an outlier 1,000 onto the ordered list 4, 6, 8, 10, 12: how much do the Mean vs Median shift?",
                "options": [
                    "Mean jumps dramatically from 8 to 173.3, whereas Median shifts slightly from 8 to 9 ((8+10)/2)",
                    "Both Mean and Median jump to 173.3",
                    "Mean stays at 8 while Median jumps to 500",
                    "Neither Mean nor Median changes"
                ],
                "answer": 0,
                "hint": "Compute new mean (40+1000)÷6 vs middle pair of 4, 6, 8, 10, 12, 1000!",
                "explanation": "Outlier 1,000 pulls the mean violently upward to 173.3, while the median depends only on middle positions 8 and 10 → 9."
            }
        ]
    },
    {
        "id": 5,
        "title": "Finding The Unknown",
        "subtitle": "Section 5.1 Finding the Unknown: Missing Wrestler Weight & Correcting Overstated Coconut Harvest Counts",
        "speech": (
            "Invert the mean formula algebraically inside Section Five Point One to solve real detective problems—FINDING THE UNKNOWN! Remember always that Mean = Total Sum ÷ Count, which rearranges instantly into Total Sum = Mean × Count! "
            "Test NCERT's classic MISSING WRESTLER WEIGHT problem! Suppose a team of 5 wrestlers has a mean weight of 72 kg! Immediately unlock their combined team sum: 5 × 72 = 360 kg! Four teammates weigh 68 kg, 70 kg, 74 kg, and 75 kg (partial sum = 287 kg)! Subtract cleanly to expose the missing fifth wrestler: 360 − 287 = 73 kg! Or verify via balance distances from 72: (−4 − 2 + 2 + 3 = −1) demands +1 right of 72 → 73 kg! "
            "Next fix NCERT's OVERSTATED COCONUT HARVEST recording error! Suppose 10 tall coconut palm trees averaged 42 coconuts (recorded sum = 420), before careful inspection discovered one tree's harvest count was miswritten as 65 instead of true 35! Simply subtract the overstated wrong entry and add back the true entry: Corrected Sum = 420 − 65 + 35 = 390 coconuts → Corrected Mean = 390 ÷ 10 = 39 true coconuts per tree!"
        ),
        "checkpoints": [
            {
                "question": "Six boxers in a training squad have an average weight of 65 kg. Five of them weigh 62, 64, 66, 68, and 63 kg. What is the weight of the 6th boxer?",
                "options": [
                    "67 kg",
                    "65 kg",
                    "70 kg",
                    "64 kg"
                ],
                "answer": 0,
                "hint": "Total team weight = 6 × 65 = 390 kg; subtract the sum of the five known boxers!",
                "explanation": "Sum of five known = 323 kg; missing boxer = 390 − 323 = 67 kg."
            },
            {
                "question": "A farmer calculated an average yield of 50 coconuts across 8 trees (sum = 400), then noticed one tree was overstated as 74 instead of its true 42 coconuts. What is the TRUE mean yield?",
                "options": [
                    "46 coconuts   ((400 − 74 + 42) ÷ 8 = 368 ÷ 8)",
                    "54 coconuts",
                    "48 coconuts",
                    "42 coconuts"
                ],
                "answer": 0,
                "hint": "Adjust total sum by −74 + 42 (= −32) before dividing by 8 trees!",
                "explanation": "Corrected sum = 400 − 32 = 368; true mean = 368 ÷ 8 = 46 coconuts per tree."
            }
        ]
    },
    {
        "id": 6,
        "title": "Weighted Frequency Tables",
        "subtitle": "Section 5.1 Frequency Tables: Weighted Mean (Σf_i x_i / Σf_i) & Cumulative Frequency Median in Family Sizes",
        "speech": (
            "Real classroom surveys collect dozens or hundreds of repeated responses—such as student family sizes—organized neatly into compact FREQUENCY TABLES! Look closely at Section Five Point One: how do we extract BOTH the Mean and the Median accurately from a frequency table? "
            "Beware the huge weighted-mean trap: NEVER average distinct values directly while ignoring frequencies! Instead, multiply each distinct value xᵢ by its count fᵢ (fᵢ · xᵢ), add those products together, and divide by TOTAL observations Σfᵢ: Mean = Σ(fᵢ xᵢ) ÷ Σfᵢ! Test 20 student families: suppose 4 families have size 3, 8 families have size 4, 6 families have size 5, and 2 families have size 6! Products sum to (4×3) + (8×4) + (6×5) + (2×6) = 12 + 32 + 30 + 12 = 86 people across 20 families → Mean = 86 ÷ 20 = 4.3 people! "
            "Now track the MEDIAN cleanly using CUMULATIVE FREQUENCIES! Build running observation totals row by row down the sorted table: size 3 reaches cumulative rank 4; size 4 reaches cumulative rank 4 + 8 = 12! For 20 student families, the middle ranks 10th and 11th BOTH sit cleanly inside size 4—making the true frequency-table Median equal 4 directly without writing out twenty separate numbers!"
        ),
        "checkpoints": [
            {
                "question": "In a frequency table of student family sizes: 3 people (freq 2), 4 people (freq 5), 5 people (freq 3). Compute the exact weighted mean (Σfᵢxᵢ / Σfᵢ):",
                "options": [
                    "4.1   ((6 + 20 + 15) ÷ 10 = 41 ÷ 10)",
                    "4.0   ((3 + 4 + 5) ÷ 3)",
                    "4.5",
                    "3.8"
                ],
                "answer": 0,
                "hint": "Multiply each family size by its frequency before summing and dividing by 2 + 5 + 3 = 10!",
                "explanation": "Weighted sum = 3(2) + 4(5) + 5(3) = 41; total frequency = 10; weighted mean = 41 ÷ 10 = 4.1."
            },
            {
                "question": "Using cumulative frequencies on those 10 sorted families (2 at size 3, 5 at size 4, 3 at size 5), which family size holds the 5th and 6th middle ranks for the Median?",
                "options": [
                    "Size 4   (cumulative count reaches 7 at size 4, covering ranks 3 through 7)",
                    "Size 3",
                    "Size 5",
                    "Size 4.5"
                ],
                "answer": 0,
                "hint": "Ranks 1–2 sit in size 3; ranks 3–7 sit inside size 4!",
                "explanation": "Since cumulative frequency jumps from 2 to 7 at size 4, both 5th and 6th positions lie cleanly at size 4."
            }
        ]
    },
    {
        "id": 7,
        "title": "Digital Spreadsheet Formulas",
        "subtitle": "Section 5.1 Spreadsheets: LibreOffice Calc, MS Excel, Google Sheets, Ranges (B3:G3), =SUM() & =AVERAGE()",
        "speech": (
            "When real classroom data grows to hundreds of rows, working statisticians switch smoothly from hand arithmetic to digital SPREADSHEET SOFTWARE—such as LibreOffice Calc, Microsoft Excel, or Google Sheets! Inside any spreadsheet worksheet, vertical lettered COLUMNS (A, B, C, D...) intersect horizontal numbered ROWS (1, 2, 3, 4...) to create unique addressable rectangular grid CELLS like B3 or G3! "
            "Suppose row 3 stores six consecutive weekly rainfall readings neatly across cells B3, C3, D3, E3, F3, and G3! Instead of typing all six individual cell names with plus signs, highlight the entire continuous horizontal range cleanly using a colon symbol: B3:G3! Every dynamic spreadsheet calculation MUST begin with an equals sign (=), clearly signaling the software to evaluate a live mathematical formula rather than store plain text! "
            "Type =SUM(B3:G3) directly inside output cell H3 to compute the exact sum of all six numbers instantaneously! Even better, type =AVERAGE(B3:G3) (or =MEDIAN(B3:G3)) right inside the adjacent output cell I3 to obtain the exact arithmetic mean automatically! Best of all: whenever you edit ONE single weekly rainfall measurement inside cell D3, BOTH live dynamic formulas =SUM() and =AVERAGE() automatically recalculate and display updated answers cleanly in mere milliseconds every time!"
        ),
        "checkpoints": [
            {
                "question": "Inside LibreOffice Calc, Excel, or Google Sheets, which exact formula correctly calculates the arithmetic mean of numbers stored in cells B3 through G3?",
                "options": [
                    "=AVERAGE(B3:G3)",
                    "AVERAGE(B3-G3)",
                    "=MEAN(B3;G3)",
                    "+SUM(B3:G3)"
                ],
                "answer": 0,
                "hint": "Formulas begin with '=', use ':' for continuous cell ranges, and call =AVERAGE(...)!",
                "explanation": "=AVERAGE(B3:G3) begins with '=' and applies the built-in AVERAGE function across range B3 through G3."
            },
            {
                "question": "If cell H3 holds =SUM(B3:G3) and you increase the number typed inside cell D3 by +18, what happens automatically in H3 and in =AVERAGE(B3:G3)?",
                "options": [
                    "H3 increases dynamically by +18 and =AVERAGE(B3:G3) increases automatically by +3 (18 ÷ 6)",
                    "You must retype both formulas from scratch",
                    "Only H3 changes while AVERAGE stays frozen",
                    "Spreadsheets erase cell D3"
                ],
                "answer": 0,
                "hint": "Dynamic formulas recalculate automatically whenever any cell in range B3:G3 updates!",
                "explanation": "Dynamic cell references immediately add +18 to =SUM(B3:G3) and +18/6 = +3 to =AVERAGE(B3:G3)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Time Series Graphs",
        "subtitle": "Section 5.2 Line Graphs: Continuous Tracking Over Time (Kerala vs Punjab Monthly Max Temperatures)",
        "speech": (
            "Enter Section Five Point Two: Visualising and Interpreting Data! While dot plots freeze single snapshots in time, how do we tell stories of change unfolding across months, years, or decades? Meet LINE GRAPHS—time series champions linking ordered data points from left to right along continuous time intervals! "
            "Compare monthly maximum daytime temperatures across twelve calendar months between southern coastal Kerala and northern inland Punjab! Put Months (January through December) evenly spaced along the horizontal x-axis, and Temperature (°C) scaled carefully along the vertical y-axis! Plot each city's twelve monthly points and connect consecutive months cleanly with straight line segments! "
            "Look instantly at the two sharp contrasting seasonal temperature stories emerging clearly side by side! Kerala's humid coastal ocean breeze holds monthly maximum daytime temperatures remarkably steady inside a gentle horizontal flat band near 29°C to 33°C throughout the entire calendar year! By sharp contrast, Punjab's inland line graph swoops dramatically across seasons—climbing steeply upward across dry spring months to scorching summer peaks soaring above 40°C in May and June before dropping steeply down to crisp cool winter troughs near 18°C in January! Steep line slopes immediately reveal fast climate shifts at one quick visual glance!"
        ),
        "checkpoints": [
            {
                "question": "On a dual line graph comparing monthly maximum temperatures of Kerala and Punjab from January to December, what visually indicates Punjab's larger seasonal temperature swing?",
                "options": [
                    "Steep upward and downward slopes reaching much higher summer peaks and lower winter troughs than Kerala's steady curve",
                    "Punjab having fewer months along the horizontal axis",
                    "Kerala sitting higher in every single month",
                    "Both lines remaining completely horizontal"
                ],
                "answer": 0,
                "hint": "In line graphs, steep slopes and wide vertical height differences reveal dramatic change over time!",
                "explanation": "Coastal Kerala remains relatively flat (29–33°C), while inland Punjab climbs steeply above 40°C in summer and drops below 20°C in winter."
            },
            {
                "question": "Why are line graphs preferred over unordered dot plots when tracking monthly temperatures or annual harvests across consecutive years?",
                "options": [
                    "Connecting sequential time points shows continuous upward/downward slopes, trends, and rates of change clearly",
                    "Because line graphs cannot show negative temperatures",
                    "Because line graphs eliminate the vertical y-axis scale",
                    "Because horizontal axes are always alphabetical"
                ],
                "answer": 0,
                "hint": "Joining chronological neighbors exposes rising slopes, flat plateaus, peaks, and troughs!",
                "explanation": "Time-ordered line segments visualize rates of rise/fall and seasonal cycles continuously across time."
            }
        ]
    }
]

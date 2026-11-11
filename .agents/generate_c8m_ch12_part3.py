#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 12: Tales by Dots and Lines
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Mean Median Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Section 5.1 Fulcrum Balance, Inserting/Removing Values, Linear Shifts & Median",
        "questions": [
            {
                "question": "Dots lie on a number line at 4, 7, 11, and 18. Where sits the physical balance fulcrum (arithmetic mean) so LHS distances equal RHS distances?",
                "options": [
                    "At 10   (LHS: 6+3=9; RHS: 1+8=9)",
                    "At 9",
                    "At 11",
                    "At 10.5"
                ],
                "answer": 0,
                "hint": "Compute (4 + 7 + 11 + 18) ÷ 4 and verify |4−10| + |7−10| = |11−10| + |18−10|!",
                "explanation": "Sum = 40 ÷ 4 = 10. LHS sum = 6 + 3 = 9; RHS sum = 1 + 8 = 9.",
                "solution_steps": [
                    "Sum all four positions: 4 + 7 + 11 + 18 = 40.",
                    "Divide by 4 dots: Mean = 40 ÷ 4 = 10.",
                    "Check balance distances: LHS = (10−4)+(10−7) = 9; RHS = (11−10)+(18−10) = 9."
                ]
            },
            {
                "question": "A balance fulcrum sits cleanly at Mean = 25 for a dot plot. If ONE dot currently at 20 moves right to 30, and ONE dot at 35 moves left to 25, what happens to the Mean?",
                "options": [
                    "Unchanged at 25   (+10 right and −10 left cancel to zero net change!)",
                    "Increases by +5",
                    "Decreases by −5",
                    "Doubles to 50"
                ],
                "answer": 0,
                "hint": "Track net change in total sum: (+10) + (−10) = 0!",
                "explanation": "Moving +10 and −10 leaves the total sum unchanged, so the balance point stays locked at 25.",
                "solution_steps": [
                    "Track dot 1 shift: 20 → 30 (+10).",
                    "Track dot 2 shift: 35 → 25 (−10).",
                    "Total sum change = +10 − 10 = 0 → Mean stays 25."
                ]
            },
            {
                "question": "Eight cricket scores average 35 runs. Two more innings score 28 and 42 runs. What is the new 10-innings mean?",
                "options": [
                    "35 runs   (28 is 7 below 35, 42 is 7 above 35)",
                    "36 runs",
                    "34 runs",
                    "37 runs"
                ],
                "answer": 0,
                "hint": "Symmetric pair (35 − 7) and (35 + 7) balances cleanly around 35!",
                "explanation": "28 + 42 = 70 = 2 × 35, leaving the mean completely unchanged at 35.",
                "solution_steps": [
                    "Old sum = 8 × 35 = 280.",
                    "Add new scores: 280 + 28 + 42 = 350.",
                    "Divide by 10 innings: 350 ÷ 10 = 35."
                ]
            },
            {
                "question": "Five consecutive test marks have mean 64. If a teacher removes ONE mark of 84 (above 64), what happens to the mean of the remaining 4 tests?",
                "options": [
                    "Decreases to 59   ((320 − 84) ÷ 4 = 236 ÷ 4)",
                    "Increases to 69",
                    "Stays at 64",
                    "Drops to 54"
                ],
                "answer": 0,
                "hint": "Removing a value greater than the current mean lowers the mean!",
                "explanation": "Total sum = 5 × 64 = 320; removing 84 leaves 236 ÷ 4 = 59.",
                "solution_steps": [
                    "Compute original sum = 5 × 64 = 320.",
                    "Subtract removed score: 320 − 84 = 236.",
                    "Divide by 4 remaining tests: 236 ÷ 4 = 59."
                ]
            },
            {
                "question": "A list of 15 temperatures has mean 22°C. Every temperature is increased by +3°C. What is the new mean?",
                "options": [
                    "25°C",
                    "22.2°C",
                    "66°C",
                    "27°C"
                ],
                "answer": 0,
                "hint": "Adding constant c to every entry shifts the mean directly by +c!",
                "explanation": "22°C + 3°C = 25°C (every dot glides 3 units right with its fulcrum).",
                "solution_steps": [
                    "Apply Linear Shift property: new Mean = old Mean + c.",
                    "Substitute old Mean = 22 and c = +3.",
                    "New Mean = 22 + 3 = 25°C."
                ]
            },
            {
                "question": "If every entry in a dataset with mean 18 and median 16 is multiplied by scaling factor k = 5, what are the new mean and new median?",
                "options": [
                    "New Mean = 90; New Median = 80",
                    "New Mean = 23; New Median = 21",
                    "New Mean = 90; New Median = 16 unchanged",
                    "New Mean = 18; New Median = 80"
                ],
                "answer": 0,
                "hint": "Multiplying every value by k scales BOTH the mean and median directly by ×k!",
                "explanation": "18 × 5 = 90 (Mean) and 16 × 5 = 80 (Median).",
                "solution_steps": [
                    "Apply Linear Scaling (×k) with k = 5.",
                    "New Mean = 18 × 5 = 90.",
                    "New Median = 16 × 5 = 80."
                ]
            },
            {
                "question": "Ordered dataset: 5, 9, 13, 17, 21 (Median = 13). Insert ONE new value 25 (strictly above 13). What is the new median?",
                "options": [
                    "15   (average of middle 13 and 17)",
                    "13   (unchanged)",
                    "17",
                    "16"
                ],
                "answer": 0,
                "hint": "The 6 ordered values are 5, 9, 13, 17, 21, 25 — average the 3rd and 4th!",
                "explanation": "Middle values of 6 numbers are 13 and 17 → (13 + 17)/2 = 15.",
                "solution_steps": [
                    "Write new sorted list of 6 values: 5, 9, 13, 17, 21, 25.",
                    "Locate 3rd (13) and 4th (17) middle positions.",
                    "Average them: (13 + 17) ÷ 2 = 15."
                ]
            },
            {
                "question": "Ordered list: 4, 8, 12, 16, 20, 24 (6 numbers, Median = 14). If BOTH 4 and 24 are removed together, what happens to the median?",
                "options": [
                    "Remains strictly unchanged at 14",
                    "Increases to 16",
                    "Decreases to 12",
                    "Drops to 10"
                ],
                "answer": 0,
                "hint": "Removing one smallest value and one largest value keeps the middle two entries 12 and 16 centered!",
                "explanation": "Remaining list 8, 12, 16, 20 still averages 12 and 16 → Median = 14.",
                "solution_steps": [
                    "Remove extreme endpoints 4 and 24 → 8, 12, 16, 20 remain.",
                    "Locate middle 2 entries: 12 and 16.",
                    "Compute (12 + 16) ÷ 2 = 14 (unchanged!)."
                ]
            },
            {
                "question": "Why does replacing the largest number 30 in the set {6, 8, 10, 14, 30} with 3,000 leave the Median untouched at 10 while skyrocketing the Mean?",
                "options": [
                    "Median depends only on sorted middle rank (3rd of 5), whereas Mean adds every value's full magnitude",
                    "Because 3,000 is divisible by 10",
                    "Because Median divides by 30",
                    "Because Mean always equals the largest number"
                ],
                "answer": 0,
                "hint": "Think positional rank stability vs distance-torque pull on a seesaw!",
                "explanation": "Changing the 5th rank from 30 to 3,000 does not move the 3rd middle item (10), whereas sum jumps by +2,970.",
                "solution_steps": [
                    "Identify middle position in {6, 8, 10, 14, 3000}: still 3rd item = 10.",
                    "Compute Mean jump: (6+8+10+14+3000)÷5 = 607.6 (up from 13.6).",
                    "Conclude Median resists extreme outliers."
                ]
            },
            {
                "question": "What algebraic transformation converts temperatures from Celsius (C) with mean 20°C into Fahrenheit via F = 1.8C + 32, and what is the resulting Fahrenheit mean?",
                "options": [
                    "Scale ×1.8 then shift +32 → Mean F = 68°F",
                    "Shift +32 only → Mean F = 52°F",
                    "Scale ×1.8 only → Mean F = 36°F",
                    "Mean stays 20°F"
                ],
                "answer": 0,
                "hint": "Apply BOTH linear operations cleanly directly to old mean C = 20: 1.8(20) + 32!",
                "explanation": "1.8 × 20 + 32 = 36 + 32 = 68°F.",
                "solution_steps": [
                    "Apply scaling k = 1.8 to mean: 20 × 1.8 = 36.",
                    "Apply constant shift c = +32: 36 + 32 = 68.",
                    "New Fahrenheit mean = 68°F."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Missing Frequency Calc",
        "subtitle": "Challenge Arena 2 (10 MCQs): Unknown Weight/Coconuts, Weighted Mean Σfᵢxᵢ/Σfᵢ, Cumulative Median & Spreadsheets",
        "questions": [
            {
                "question": "Four wrestlers average 80 kg. Three weigh 76 kg, 82 kg, and 85 kg. What does the missing fourth wrestler weigh?",
                "options": [
                    "77 kg",
                    "79 kg",
                    "80 kg",
                    "75 kg"
                ],
                "answer": 0,
                "hint": "Team total = 4 × 80 = 320 kg; subtract 76 + 82 + 85 = 243 kg!",
                "explanation": "320 − 243 = 77 kg.",
                "solution_steps": [
                    "Calculate total team weight: 4 × 80 = 320 kg.",
                    "Sum known three weights: 76 + 82 + 85 = 243 kg.",
                    "Subtract: 320 − 243 = 77 kg."
                ]
            },
            {
                "question": "A village orchard recorded an average harvest of 60 coconuts across 12 trees (total 720), before realizing one entry of 88 was mistakenly typed instead of 40. Find the corrected mean:",
                "options": [
                    "56 coconuts",
                    "64 coconuts",
                    "52 coconuts",
                    "58 coconuts"
                ],
                "answer": 0,
                "hint": "Subtract wrong 88 and add back true 40: 720 − 88 + 40 = 672, then divide by 12!",
                "explanation": "Corrected sum = 720 − 48 = 672; new mean = 672 ÷ 12 = 56 coconuts.",
                "solution_steps": [
                    "Compute recorded sum: 12 × 60 = 720.",
                    "Adjust error (−88 + 40 = −48): corrected sum = 720 − 48 = 672.",
                    "Divide by 12 trees: 672 ÷ 12 = 56."
                ]
            },
            {
                "question": "A student class records daily study hours: 1 hr (4 students), 2 hrs (10 students), 3 hrs (6 students). Compute the weighted mean (Σfᵢxᵢ / Σfᵢ):",
                "options": [
                    "2.1 hours",
                    "2.0 hours",
                    "2.5 hours",
                    "1.8 hours"
                ],
                "answer": 0,
                "hint": "Sum (1×4 + 2×10 + 3×6) = 42 hours across 20 total students!",
                "explanation": "42 ÷ 20 = 2.1 hours.",
                "solution_steps": [
                    "Multiply values by frequencies: 1(4) + 2(10) + 3(6) = 4 + 20 + 18 = 42.",
                    "Sum frequencies: 4 + 10 + 6 = 20 students.",
                    "Divide: 42 ÷ 20 = 2.1 hours."
                ]
            },
            {
                "question": "A survey of 25 student families shows sizes: size 3 (freq 5), size 4 (freq 11), size 5 (freq 6), size 6 (freq 3). Using cumulative frequencies, what is the MEDIAN family size?",
                "options": [
                    "Size 4   (13th rank lies in cumulative range 6..16)",
                    "Size 5",
                    "Size 3",
                    "Size 4.5"
                ],
                "answer": 0,
                "hint": "For N = 25, median sits at the (25+1)/2 = 13th ordered observation!",
                "explanation": "Cumulative frequency reaches 5 at size 3 and 16 at size 4, placing the 13th rank cleanly inside size 4.",
                "solution_steps": [
                    "Locate median rank for N = 25: (25 + 1) ÷ 2 = 13th observation.",
                    "Build cumulative frequencies: size 3 → 5; size 4 → 5 + 11 = 16.",
                    "Since 5 < 13 ≤ 16, median = 4."
                ]
            },
            {
                "question": "Why is taking the plain unweighted average (3 + 4 + 5 + 6) ÷ 4 = 4.5 WRONG for a family-size frequency table?",
                "options": [
                    "Different family sizes occur unequally often; frequencies fᵢ must weight each value xᵢ",
                    "Because frequency tables always have zero median",
                    "Because division by 4 only applies to even numbers",
                    "Because 4.5 exceeds 6"
                ],
                "answer": 0,
                "hint": "11 families had size 4 while only 3 families had size 6 — they cannot count equally!",
                "explanation": "Every distinct xᵢ must be weighted by how many times fᵢ it occurred via Σ(fᵢxᵢ) / Σfᵢ.",
                "solution_steps": [
                    "Notice frequency fᵢ represents how many families share value xᵢ.",
                    "Equal-weight averaging ignores unequal counts (11 vs 3).",
                    "Weighted formula Σ(fᵢxᵢ)/Σfᵢ counts all 25 observations properly."
                ]
            },
            {
                "question": "In LibreOffice Calc or Google Sheets, which symbol MUST start every mathematical formula inside a cell?",
                "options": [
                    "=",
                    "#",
                    "@",
                    "$"
                ],
                "answer": 0,
                "hint": "Think =SUM(B3:G3) and =AVERAGE(B3:G3)!",
                "explanation": "Every spreadsheet formula starts with an equals sign (=).",
                "solution_steps": [
                    "Inspect Section 5.1 Spreadsheets syntax.",
                    "Notice =SUM(...) and =AVERAGE(...) always lead with '='.",
                    "Select '='."
                ]
            },
            {
                "question": "In a spreadsheet, cells B3, C3, D3, E3, F3, and G3 hold numbers 10, 20, 30, 40, 50, and 60. What does =AVERAGE(B3:G3) output?",
                "options": [
                    "35",
                    "210",
                    "30",
                    "40"
                ],
                "answer": 0,
                "hint": "Sum 10+20+30+40+50+60 = 210, then divide by 6 cells!",
                "explanation": "210 ÷ 6 = 35.",
                "solution_steps": [
                    "Identify range B3:G3 covers 6 cells: 10, 20, 30, 40, 50, 60.",
                    "Compute SUM = 210.",
                    "Divide 210 ÷ 6 = 35."
                ]
            },
            {
                "question": "How is a continuous block of cells spanning from column B row 3 through column G row 3 written cleanly in spreadsheet range notation?",
                "options": [
                    "B3:G3",
                    "B3->G3",
                    "B3+G3",
                    "B3..G3"
                ],
                "answer": 0,
                "hint": "A colon separates the top-left and bottom-right cell addresses!",
                "explanation": "B3:G3 uses the standard colon separator to specify all cells from B3 through G3.",
                "solution_steps": [
                    "Identify starting cell B3 and ending cell G3.",
                    "Join with colon ':' → B3:G3.",
                    "Use inside =SUM(B3:G3) or =AVERAGE(B3:G3)."
                ]
            },
            {
                "question": "Five packages have mean weight 14 kg. If a 6th package weighing 26 kg is added, what is the new mean weight of all 6 packages?",
                "options": [
                    "16 kg",
                    "20 kg",
                    "15 kg",
                    "18 kg"
                ],
                "answer": 0,
                "hint": "Total sum = 5 × 14 = 70 kg; add 26 kg = 96 kg; divide by 6!",
                "explanation": "(70 + 26) ÷ 6 = 96 ÷ 6 = 16 kg.",
                "solution_steps": [
                    "Calculate sum of first 5 packages: 5 × 14 = 70 kg.",
                    "Add 6th package: 70 + 26 = 96 kg.",
                    "Divide across 6 packages: 96 ÷ 6 = 16 kg."
                ]
            },
            {
                "question": "In a frequency table of test scores out of 10: score 6 (freq x), score 8 (freq 4), score 10 (freq 2). If total weighted mean equals 8, find unknown frequency x:",
                "options": [
                    "x = 2",
                    "x = 4",
                    "x = 3",
                    "x = 6"
                ],
                "answer": 0,
                "hint": "Balance LHS/RHS around 8: score 6 is 2 below 8 (needs weight 2×x) to balance score 10 (2 above 8, weight 2×2 = 4)!",
                "explanation": "Balance distances around mean 8: x × (8−6) = 2 × (10−8) → 2x = 4 → x = 2 (sum = 6(2)+8(4)+10(2) = 64 ÷ 8 = 8).",
                "solution_steps": [
                    "Set up distance balance around mean 8: LHS = 2·x; RHS = 2·2 = 4.",
                    "Equate LHS = RHS: 2x = 4 → x = 2.",
                    "Verify weighted mean: (12 + 32 + 20) ÷ (2 + 4 + 2) = 64 ÷ 8 = 8."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Line Graphs Strips",
        "subtitle": "Challenge Arena 3 (10 MCQs): Kerala/Punjab Temps, 2-Step Reading, Space/Rain/Births, Rice/Wheat Maps & Strips",
        "questions": [
            {
                "question": "In NCERT's 2-Step Interpretation Process for line graphs, what belongs strictly to Step 1 vs Step 2?",
                "options": [
                    "Step 1: Axes, scales, markers, slopes; Step 2: Patterns, peaks, troughs, comparative trends",
                    "Step 1: Guess future trends; Step 2: Check axis labels last",
                    "Step 1: Remove slopes; Step 2: Redraw bars",
                    "Both steps ignore vertical scales"
                ],
                "answer": 0,
                "hint": "Read the physical chart setup (Step 1) before drawing analytical conclusions (Step 2)!",
                "explanation": "Step 1 verifies spatial scales, axes, markers, and slopes; Step 2 infers patterns, peaks, troughs, and trends.",
                "solution_steps": [
                    "Step 1 checks axes, tick intervals, markers, and slopes.",
                    "Step 2 identifies peaks, troughs, seasonal repeats, and stories.",
                    "Select Option 1."
                ]
            },
            {
                "question": "Comparing monthly maximum temperatures of Kerala and Punjab on a dual line graph, which state exhibits the MUCH WIDER temperature range between winter trough and summer peak?",
                "options": [
                    "Punjab (swings sharply from cool winter <20°C up to >40°C summer peak)",
                    "Kerala (swings from 5°C to 50°C)",
                    "Both exhibit identical 4°C annual swings",
                    "Neither state changes across months"
                ],
                "answer": 0,
                "hint": "Inland continental climates have extreme winter-summer swings compared to humid coastal Kerala!",
                "explanation": "Coastal Kerala stays relatively steady (~29–33°C), while inland Punjab spans wide seasonal extremes.",
                "solution_steps": [
                    "Inspect Kerala's curve: flat steady coastal band (~29–33°C).",
                    "Inspect Punjab's curve: steep spring rise (>40°C) and steep autumn drop (<20°C).",
                    "Conclude Punjab has the wider annual range."
                ]
            },
            {
                "question": "On a time-series line graph tracking monthly live births, Segment A slopes steeply upward while Segment B drops downward. What does Segment A represent?",
                "options": [
                    "A rapid monthly increase in live births across that interval",
                    "Zero change in live births",
                    "A sharp drop in live births",
                    "A missing month"
                ],
                "answer": 0,
                "hint": "Positive steep upward slope moving left-to-right shows rapid growth!",
                "explanation": "Upward left-to-right slope directly represents growth; steepness shows fast rate of increase.",
                "solution_steps": [
                    "Read slope direction from left to right.",
                    "Upward slope = positive growth; downward = decrease; flat = constant.",
                    "Select rapid monthly increase."
                ]
            },
            {
                "question": "Analyzing India's East Coast (Chennai) vs West Coast (Mumbai/Mangalore) monthly rainfall line graphs, during which months does Chennai experience its BIGGEST rainfall peak?",
                "options": [
                    "October–December   (Northeast Monsoon)",
                    "March–May   (Dry summer)",
                    "June–July exclusively",
                    "February only"
                ],
                "answer": 0,
                "hint": "Remember the Northeast Monsoon peaking late in the calendar year along Tamil Nadu's coast!",
                "explanation": "While India's West Coast peaks in June–September, Chennai peaks heavily in October–December.",
                "solution_steps": [
                    "Contrast coastal monsoon curves.",
                    "West Coast peaks June–September (Southwest Monsoon).",
                    "East Coast (Chennai) peaks October–December (Northeast Monsoon)."
                ]
            },
            {
                "question": "Looking at the UN Office for Outer Space Affairs line graph of annual global space object launches, what dramatic shift occurs in the modern satellite era?",
                "options": [
                    "Steep exponential upward surge jumping thousands of objects per year",
                    "Smooth decline down to fewer than 10 objects/year",
                    "Perfect straight horizontal line from 1957 to 2024",
                    "Zero launches after 1990"
                ],
                "answer": 0,
                "hint": "Small-satellite constellations caused launch counts to spike dramatically upward!",
                "explanation": "Annual launched space objects climbed sharply in recent years, creating a steep hockey-stick rise.",
                "solution_steps": [
                    "Read historical early plateau from 1960s–2010s.",
                    "Observe sharp vertical surge in 2018+.",
                    "Identify massive increase driven by satellite constellations."
                ]
            },
            {
                "question": "What pattern does an Infographic Map shading Indian states by Rice vs Wheat dietary preference highlight cleanly?",
                "options": [
                    "Rice dominates moist southern, eastern & coastal states; Wheat dominates northern & northwestern plains",
                    "Wheat dominates exclusively coastal southern states",
                    "Every Indian state reports identical 50-50 dietary shares",
                    "Only islands consume wheat"
                ],
                "answer": 0,
                "hint": "Match water-rich coastal/eastern states to rice and northern Indo-Gangetic plains to wheat!",
                "explanation": "Climate and agriculture produce strong geographic clustering: rice across South/East/Northeast vs wheat across North/Northwest.",
                "solution_steps": [
                    "Locate South & East coastal states on map → Rice shading.",
                    "Locate North & Northwest plains (Punjab, Haryana, UP, MP) → Wheat shading.",
                    "Confirm regional geographical correlation."
                ]
            },
            {
                "question": "In NCERT's 'What can a Strip Say?' activity, each 24-hour day is divided into uniform 30-minute blocks. If a student's Play strip covers 5 blocks, how much time is spent playing?",
                "options": [
                    "2 hours 30 minutes   (5 × 30 min)",
                    "5 hours",
                    "1 hour 15 minutes",
                    "3 hours"
                ],
                "answer": 0,
                "hint": "Multiply 5 blocks × 30 minutes per block!",
                "explanation": "5 × 30 minutes = 150 minutes = 2.5 hours (2 hours 30 minutes).",
                "solution_steps": [
                    "Note each strip block represents 30 minutes (0.5 hour).",
                    "Multiply block count by duration: 5 × 0.5 = 2.5 hours.",
                    "Convert 0.5 hr → 30 min: 2 hours 30 minutes."
                ]
            },
            {
                "question": "Comparing stacked 24-hour weekday vs weekend activity strips of a school student typically reveals which unmistakable visual change?",
                "options": [
                    "The long weekday School block disappears on weekends, replaced by longer Sleep and Play/Family blocks",
                    "Both weekday and weekend strips look 100% identical",
                    "Weekend strips contain only 24 blocks instead of 48",
                    "Sleep drops to zero on weekends"
                ],
                "answer": 0,
                "hint": "All 24 hours remain (48 blocks), while School time shifts into Rest and Recreation!",
                "explanation": "Total blocks remain 48 (24 hours), while weekend strips reallocate school blocks into extended sleep and leisure.",
                "solution_steps": [
                    "Verify both strips span 48 blocks (24 hours).",
                    "Spot absence of weekday School block on weekend.",
                    "Notice larger Sleep and Play segments on weekend."
                ]
            },
            {
                "question": "If an infographic uses tiny rice bowls where 1 bowl = 10% and a state shows 8 full bowls for Rice and 2 full bowls for Wheat, what ratio prefers Rice over Wheat?",
                "options": [
                    "4 : 1   (80% Rice to 20% Wheat)",
                    "8 : 1",
                    "2 : 1",
                    "1 : 4"
                ],
                "answer": 0,
                "hint": "Simplify 8 : 2 cleanly!",
                "explanation": "8 bowls (80%) to 2 bowls (20%) simplifies to 4 : 1.",
                "solution_steps": [
                    "Convert icons: 8 × 10% = 80% Rice; 2 × 10% = 20% Wheat.",
                    "Form ratio 80 : 20.",
                    "Simplify dividing by 20 → 4 : 1."
                ]
            },
            {
                "question": "Which mistake commonly leads students to misread two line graphs placed side by side?",
                "options": [
                    "Ignoring different vertical y-axis scales (e.g., one chart jumps by 10s while the other jumps by 100s)",
                    "Reading horizontal time labels from left to right",
                    "Checking where two curves cross",
                    "Reading the chart legend first"
                ],
                "answer": 0,
                "hint": "Always verify Step 1 vertical axis scale intervals before comparing curve steepness across separate graphs!",
                "explanation": "Differing vertical tick scales distort apparent visual steepness if Step 1 axis inspection is skipped.",
                "solution_steps": [
                    "Recall Step 1 of NCERT 2-Step Interpretation.",
                    "Compare y-axis step sizes across separate charts.",
                    "Never assume matching visual heights equal matching numbers without checking scales."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Curves Hex Summary",
        "subtitle": "Challenge Arena 4 (10 MCQs): Sleepy-Deepy Smooth Curves (Ages 6–75), 11×11 Game of Hex & Chapter Summary",
        "questions": [
            {
                "question": "In 'Data Story: Sleepy-Deepy', daily sleep hours are surveyed across 70 consecutive ages (6 to 75 years). Why does NCERT plot ONE smooth curve rather than a bar chart?",
                "options": [
                    "70 thin bars side-by-side create dense visual clutter, whereas a smooth curve cleanly tracks continuous rise/fall across ages",
                    "Because bar charts cannot display numbers near 8",
                    "Because smooth curves delete ages 20 through 50",
                    "Because bar charts only accept negative numbers"
                ],
                "answer": 0,
                "hint": "Think visually: 70 closely packed bars blur into stripes while a single curve shows smooth age progression!",
                "explanation": "Smooth multi-point curves cleanly reveal subtle multi-decade trends across dense numeric ages 6 to 75.",
                "solution_steps": [
                    "Count points: ages 6..75 = 70 distinct points.",
                    "Visualize 70 narrow vertical bars crowding together.",
                    "Smooth continuous curve shows clear long-term trend cleanly."
                ]
            },
            {
                "question": "What real-life human story appears directly along the Sleepy-Deepy curve from age 6 to age 75?",
                "options": [
                    "Children age 6 sleep longest (~9.5–10 hrs), decreasing gradually toward working adulthood (~7.5 hrs) and ticking gently up after age 65",
                    "Six-year-olds sleep only 4 hours while adults sleep 14 hours",
                    "Sleep declines strictly linearly to 0 hours by age 75",
                    "Sleep stays frozen flat at 8.00 hours across all ages"
                ],
                "answer": 0,
                "hint": "Compare school children, working adults, and older retirees!",
                "explanation": "Young children require maximum rest (~9.5–10 hrs), mid-adulthood dips lowest (~7.5 hrs), and senior ages rise modestly.",
                "solution_steps": [
                    "Locate leftmost start (age 6): peak ~9.5–10 hrs.",
                    "Track mid-life plateau (ages 25–55): lower trough ~7.5 hrs.",
                    "Observe gentle uptick past age 65."
                ]
            },
            {
                "question": "Why are ages on the horizontal axis of the Sleepy-Deepy curve NOT shuffled into random order?",
                "options": [
                    "Chronological ordering (6 → 75) is essential so slopes accurately portray progression across the human lifespan",
                    "Because numbers must always start at zero",
                    "Because alphabetical sorting works better for ages",
                    "Because shuffling leaves gaps on the vertical axis"
                ],
                "answer": 0,
                "hint": "Line graphs and smooth curves track changes across ordered sequential steps!",
                "explanation": "Ordered x-axis progression lets left-to-right curves display genuine age trajectories.",
                "solution_steps": [
                    "Connect adjacent years continuously in age order 6, 7, ..., 75.",
                    "Recognize shuffling destroys meaningful slope interpretation.",
                    "Conclude natural numeric ordering is vital."
                ]
            },
            {
                "question": "How many hexagonal cells build a standard 11 × 11 Game of Hex board?",
                "options": [
                    "121 hexagons",
                    "64 hexagons",
                    "100 hexagons",
                    "144 hexagons"
                ],
                "answer": 0,
                "hint": "Multiply 11 rows × 11 columns!",
                "explanation": "11 × 11 = 121 hexagonal spaces.",
                "solution_steps": [
                    "Read Grid Dimensions from Section 'It's Puzzle Time! Game of Hex': 11 × 11.",
                    "Multiply 11 × 11 = 121.",
                    "Select 121 hexagons."
                ]
            },
            {
                "question": "In the Game of Hex, how does Player 1 (Top–Bottom) win, and must the winning chain form a straight line?",
                "options": [
                    "By forming any unbroken chain of touching hexagons from Top edge to Bottom edge — bends and zigzags are completely valid!",
                    "Only by building a ruler-straight diagonal line",
                    "By surrounding 50% of the board's corners",
                    "By jumping over opponent pieces like chess knights"
                ],
                "answer": 0,
                "hint": "Hex allows winding, snaking paths as long as consecutive stones touch edge-to-edge!",
                "explanation": "Any continuous unbroken connected path linking opposite assigned edges wins immediately.",
                "solution_steps": [
                    "Check win criterion: topological connection between opposite borders.",
                    "Verify winding/zigzag chains still count as connected.",
                    "Confirm straight lines are unnecessary."
                ]
            },
            {
                "question": "What happens mathematically if two players take turns filling EVERY SINGLE one of the 121 cells on an 11 × 11 Hex board?",
                "options": [
                    "Impossible to draw — exactly ONE player MUST hold a complete unbroken opposite-side chain",
                    "The game always ends in a tie",
                    "Both players win simultaneously",
                    "The center hexagon belongs to both players"
                ],
                "answer": 0,
                "hint": "If one player's stones block the other completely from Left-to-Right, that blocking wall itself connects Top-to-Bottom!",
                "explanation": "Hex obeys a proven No-Tie Theorem: a full board guarantees a unique winner.",
                "solution_steps": [
                    "Note opposing borders sit perpendicularly (Top–Bottom vs Left–Right).",
                    "Observe any complete barrier blocking Left–Right connects Top–Bottom.",
                    "Conclude ties cannot exist in Hex."
                ]
            },
            {
                "question": "Which tactic in Hex is called a 'virtual connection / two-hexagon bridge'?",
                "options": [
                    "Placing two same-colored stones with TWO shared empty neighbor cells between them — whichever one the opponent takes, you take the other to connect!",
                    "Skipping your turn twice",
                    "Connecting only the four corners",
                    "Placing two stones in one turn"
                ],
                "answer": 0,
                "hint": "Think of two empty backup cells linking two nearby stones: blocking one leaves the other wide open!",
                "explanation": "A Hex bridge leaves two parallel linking cells so no single opponent move can sever the connection.",
                "solution_steps": [
                    "Picture two stones separated by a 2-cell shared diamond.",
                    "If opponent fills Cell A, immediately fill Cell B to connect.",
                    "This secures a guaranteed unbroken connection."
                ]
            },
            {
                "question": "A 24-hour weekend activity strip allocates 18 blocks (30 min each) to Sleep, 6 blocks to Meals/Chores, and 10 blocks to Study/Reading. How many hours remain for Play/Leisure?",
                "options": [
                    "7 hours   (14 remaining blocks out of 48)",
                    "14 hours",
                    "5 hours",
                    "6 hours"
                ],
                "answer": 0,
                "hint": "Total blocks = 48; used = 18 + 6 + 10 = 34 → remaining = 14 blocks × 0.5 hour!",
                "explanation": "48 − 34 = 14 blocks remaining; 14 × 0.5 hr = 7 hours.",
                "solution_steps": [
                    "Sum used blocks: 18 + 6 + 10 = 34 blocks.",
                    "Subtract from 48 total blocks: 48 − 34 = 14 blocks.",
                    "Multiply by 0.5 hr/block: 14 × 0.5 = 7 hours."
                ]
            },
            {
                "question": "If every entry of a dataset (mean 30, median 28) decreases by −4, AND then you multiply every result by 3, what are the final Mean and final Median?",
                "options": [
                    "Final Mean = 78; Final Median = 72",
                    "Final Mean = 86; Final Median = 80",
                    "Final Mean = 90; Final Median = 84",
                    "Final Mean = 26; Final Median = 24"
                ],
                "answer": 0,
                "hint": "First subtract 4 (30 → 26, 28 → 24), then multiply BOTH by 3!",
                "explanation": "Mean: (30 − 4) × 3 = 78; Median: (28 − 4) × 3 = 72.",
                "solution_steps": [
                    "Apply shift −4: Mean = 26, Median = 24.",
                    "Apply scale ×3: Mean = 26 × 3 = 78.",
                    "Apply scale ×3: Median = 24 × 3 = 72."
                ]
            },
            {
                "question": "Which summary option accurately consolidates ALL core lessons of Chapter 12: Tales by Dots and Lines?",
                "options": [
                    "Mean balances LHS=RHS distances; ±c & ×k transform mean cleanly; frequencies weight via Σfᵢxᵢ/Σfᵢ; 2-step line graphs, infographics, 48-block strips & 11×11 Hex tell data tales",
                    "Mean ignores extreme outliers while Median balances LHS=RHS distances",
                    "Spreadsheets omit '=' while Hex allows frequent draws on full boards",
                    "Bar charts always beat smooth curves for 70+ ages"
                ],
                "answer": 0,
                "hint": "Verify every single clause against Section 5.1, Section 5.2, Summary & Game of Hex!",
                "explanation": "Option 1 accurately recaps fulcrum mean, linear operations, weighted frequencies, spreadsheets, 2-step line graphs, strips, Sleepy-Deepy & 11×11 Hex.",
                "solution_steps": [
                    "Confirm Section 5.1: Fulcrum mean, median tinkering, weighted frequencies & spreadsheets.",
                    "Confirm Section 5.2: 2-step line graphs, infographics, 48-block strips & Sleepy-Deepy.",
                    "Confirm 11 × 11 Game of Hex no-tie connection rule."
                ]
            }
        ]
    }
]

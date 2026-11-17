#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 10: How Quantities Combine: Understanding Data
Part 2: Slides 9 to 16 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Cluster Stacked Columns",
        "subtitle": "Section 10.2.1 Stacking Columns: Comparing Cluster-Column Charts vs Stacked Bar & Column Charts",
        "speech": (
            "Now transition from numerical weighted averages into Section Ten Point Two: VISUALISING AND INTERPRETING DATA! Begin with Subsection Ten Point Two Point One: STACKING COLUMNS! "
            "Suppose a school tracks student enrollment across Arts, Commerce, and Science streams over three years! You already know how to draw a CLUSTER-COLUMN CHART, placing three separate vertical bars side by side for each year! Cluster charts make comparing individual stream heights easy, YET they hide one crucial question: what is the OVERALL TOTAL enrollment each year, and how did that total grow? "
            "Enter the STACKED COLUMN CHART (or horizontal STACKED BAR CHART)! Instead of placing the three bars side by side, we stack Arts on the bottom, Commerce directly on top of Arts, and Science directly on top of Commerce inside ONE unified column per year! "
            "Instantly, TWO insights jump off the page simultaneously! First, the top edge of each stacked column reveals the EXACT OVERALL TOTAL at a glance! Second, the coloured bands inside each column track how every individual component contributes to that combined whole! Remember though: cluster columns remain superior whenever you only need direct baseline-zero comparisons of individual sub-categories without needing total heights across separate categories!"
        ),
        "checkpoints": [
            {
                "question": "What is the primary advantage of a STACKED column chart over a CLUSTER-column chart?",
                "options": [
                    "A stacked chart directly displays the combined OVERALL TOTAL height while simultaneously showing each component's part",
                    "A stacked chart hides all component values",
                    "A cluster chart cannot display categories",
                    "Stacked charts only work for 2 numbers"
                ],
                "answer": 0,
                "hint": "Think about what the top edge of a stacked bar represents compared to side-by-side bars!",
                "explanation": "Stacking components end-to-end visually sums them into the total bar height while keeping parts visible."
            },
            {
                "question": "When is a CLUSTER-column chart actually MORE convenient than a stacked column chart?",
                "options": [
                    "When you want to compare the exact heights of individual sub-categories directly from a common zero baseline",
                    "When you want to see the combined sum of all sub-categories",
                    "When all values sum to 100%",
                    "Never — stacked charts are always better"
                ],
                "answer": 0,
                "hint": "In a stacked chart, upper segments don't start at y = 0!",
                "explanation": "Clustered bars all start at baseline 0, making side-by-side comparison of middle/top sub-categories easier."
            }
        ]
    },
    {
        "id": 10,
        "title": "Reading Stacked Totals",
        "subtitle": "Section 10.2.1 Reading Stacked Charts: Cumulative Boundaries vs Individual Segment Sizes",
        "speech": (
            "Watch out for the single biggest reading mistake students make on stacked bar charts inside Section Ten Point Two Point One! "
            "Suppose a stacked column for Year Twenty Twenty-Five shows three stacked bands: Band A (bottom, blue) running from zero up to forty; Band B (middle, amber) running from forty up to ninety-five; and Band C (top, emerald) running from ninety-five up to one hundred thirty! "
            "If a hurried reader glances at the top boundary of Band B at ninety-five and writes 'Band B equals ninety-five', that is WRONG! Ninety-five is the CUMULATIVE TOTAL of Band A PLUS Band B! To extract the true value of ANY middle or upper segment in a stacked chart, you MUST subtract its bottom boundary from its top boundary! "
            "Calculate carefully! Band A equals forty minus zero equals FORTY! Band B equals ninety-five minus forty equals FIFTY-FIVE! Band C equals one hundred thirty minus ninety-five equals THIRTY-FIVE! Check the sum: forty plus fifty-five plus thirty-five equals ONE HUNDRED THIRTY—matching the overall column height cleanly! Always subtract bottom from top before reading any upper stacked segment, and verify that all extracted segment values sum back cleanly to the top boundary!"
        ),
        "checkpoints": [
            {
                "question": "In a stacked bar chart, Segment 1 spans 0 to 30, Segment 2 spans 30 to 75, and Segment 3 spans 75 to 120. What is the true value of Segment 2?",
                "options": ["45 (75 − 30)", "75", "30", "120"],
                "answer": 0,
                "hint": "Subtract the bottom boundary (30) from the top boundary (75) of Segment 2!",
                "explanation": "75 is the cumulative height of Segment 1 + Segment 2, so Segment 2 alone = 75 − 30 = 45."
            },
            {
                "question": "What does the very top edge (120) of that entire stacked bar represent?",
                "options": [
                    "The combined total sum of all three segments (30 + 45 + 45 = 120)",
                    "Only Segment 3's value",
                    "The average of the three segments",
                    "The difference between Segment 3 and Segment 1"
                ],
                "answer": 0,
                "hint": "Stacking places segments end-to-end from 0 upward!",
                "explanation": "The top of the stack equals the total sum across all constituent segments."
            }
        ]
    },
    {
        "id": 11,
        "title": "Hundred Percent Bars",
        "subtitle": "Section 10.2.2 An Alternative to Pie Charts: 100% Stacked Bar Charts for Proportions",
        "speech": (
            "Now discover a sleek, modern alternative to pie charts inside Section Ten Point Two Point Two: THE HUNDRED-PERCENT STACKED BAR CHART! "
            "Recall how pie charts show percentage shares as circular slices adding up to one hundred percent! Pie charts work nicely for ONE single dataset—yet what happens if you want to compare proportional shares across FIVE different countries, SIX months, or TEN demographic groups side by side? Placing ten separate circles next to each other makes comparing tiny slice angles nearly impossible for human eyes! "
            "A HUNDRED-PERCENT STACKED BAR CHART solves this effortlessly! Every bar is scaled to the EXACT SAME FIXED LENGTH—representing ONE HUNDRED PERCENT—and each category segment stretches across a length proportional to its percentage share! "
            "Look closely at the crucial trade-off between regular stacked bars and hundred-percent stacked bars! Regular stacked bars preserve ABSOLUTE VALUES and OVERALL TOTALS (showing which city uses more total electricity), whereas hundred-percent stacked bars strip away total size differences to highlight RELATIVE PROPORTIONS (showing which city relies on a higher percentage of solar power)! Because human eyes compare aligned straight lengths far more accurately than circular pie slice angles, hundred-percent stacked bars shine brightly across multi-group proportional comparisons!"
        ),
        "checkpoints": [
            {
                "question": "Why are 100% stacked bar charts often preferred over multiple pie charts when comparing 5 or 6 groups?",
                "options": [
                    "Human eyes compare aligned straight segment lengths along parallel 0–100% bars much more accurately than angles across separate circles",
                    "Pie charts cannot display percentages",
                    "100% stacked bars show absolute totals without percentages",
                    "Pie charts can only have 2 slices"
                ],
                "answer": 0,
                "hint": "Compare judging 28% vs 31% as circular angles versus straight bars stacked to the same 100% line!",
                "explanation": "Aligned fixed-length bars allow rapid, accurate visual comparison of proportional shares across many groups."
            },
            {
                "question": "What information is LOST when switching from an absolute stacked bar chart to a 100% stacked bar chart?",
                "options": [
                    "The absolute magnitudes and overall group totals (since every bar is stretched/shrunk to equal length 100%)",
                    "The relative percentage shares of components",
                    "The category names",
                    "Nothing — both charts show identical absolute numbers"
                ],
                "answer": 0,
                "hint": "If Group A has total 50 and Group B has total 5,000, both bars have the exact same 100% length!",
                "explanation": "100% stacked bars normalize every total to 100%, hiding differences in raw total size."
            }
        ]
    },
    {
        "id": 12,
        "title": "Global Energy Trends",
        "subtitle": "Section 10.2.2 Data Case Study: Global Household Energy Consumption Trends",
        "speech": (
            "Apply hundred-percent stacked bar charts to real-world sustainability inside Section Ten Point Two Point Two: GLOBAL HOUSEHOLD ENERGY CONSUMPTION TRENDS! "
            "Across the world, households consume energy for cooking, heating, lighting, and appliances from diverse sources—electricity, natural gas, traditional biomass (firewood and crop residue), oil products, and modern renewables! Compare rural versus urban energy profiles, or track how a nation's household energy mix shifts across decades from nineteen ninety to today! "
            "Notice a classic data-literacy insight when reading household energy stacked charts! Suppose Country A's hundred-percent stacked bar shows biomass shrinking from sixty percent down to twenty-five percent while electricity grows from fifteen percent up to fifty-five percent! That clearly reveals a cleaner energy transition in PROPORTIONAL SHARE! "
            "However, remember: if total population and total household energy demand doubled during those same decades, twenty-five percent of a doubled total still consumes almost as much absolute biomass! Pairing BOTH an absolute stacked chart AND a hundred-percent stacked chart gives policy analysts the complete, honest energy picture! Never jump to conclusions about absolute fuel reduction from a shrinking percentage slice alone without checking whether the overall total energy pie itself grew much larger over the exact same period!"
        ),
        "checkpoints": [
            {
                "question": "In a 100% stacked bar chart of household energy, biomass drops from 60% in 1990 to 30% in 2020 while total energy doubles. What happened to absolute biomass usage?",
                "options": [
                    "It stayed the same! (60% of 100 units = 60 units; 30% of 200 units = 60 units)",
                    "It definitely dropped by half",
                    "It doubled",
                    "It became zero"
                ],
                "answer": 0,
                "hint": "Test with concrete totals: 100 units in 1990 vs 200 units in 2020!",
                "explanation": "A falling percentage share of a growing total can keep the absolute quantity constant (0.60×100 = 0.30×200 = 60)."
            },
            {
                "question": "Why is pairing an absolute stacked chart with a 100% stacked chart valuable for energy trend studies?",
                "options": [
                    "The absolute chart tracks total energy growth while the 100% chart isolates shifts in fuel-source proportions",
                    "Because one chart is always wrong",
                    "Because 100% charts cannot show electricity",
                    "To make the report twice as long"
                ],
                "answer": 0,
                "hint": "Each chart answers a different question: 'how much total?' vs 'what share of the mix?'",
                "explanation": "Together they distinguish proportional fuel-mix transitions from changes in total consumption."
            }
        ]
    },
    {
        "id": 13,
        "title": "Blooming Time Use",
        "subtitle": "Section 10.2.2 Data Case Studies: Flower Blooming Seasons, National Time Use Survey (2024) & Body States",
        "speech": (
            "Explore three more fascinating data case studies from Section Ten Point Two Point Two: FLOWER BLOOMING SEASONS, INDIA'S NATIONAL TIME USE SURVEY TWENTY TWENTY-FOUR, AND PHYSICAL BODY-STATE TRACKING! "
            "First, botanical gardens track flower blooming seasons across twelve months using stacked bars—showing peak spring diversity alongside winter lulls, helping gardeners plan year-round colour! "
            "Second, inspect INDIA'S NATIONAL TIME USE SURVEY TWENTY TWENTY-FOUR! Every human day contains a fixed budget of TWENTY-FOUR HOURS (one thousand four hundred forty minutes)—making a hundred-percent stacked bar (or twenty-four-hour fixed stacked bar) completely natural! Across demographics (rural versus urban, students versus working adults), bars divide into Sleep and Self-Care, Paid Employment, Unpaid Caregiving and Domestic Work, Learning, and Leisure! Immediately you spot how unpaid domestic hours and leisure hours shift starkly across groups! "
            "Third, physical body-state tracking across a day—dividing twenty-four hours into Deep Sleep, Light Sleep, Sedentary Sitting, Light Walking, and Vigorous Exercise—lets health scientists compare active versus sedentary lifestyles cleanly along identical twenty-four-hour bars! Notice how fixed-budget datasets—whether twelve calendar months, twenty-four daily hours, or one hundred percent—naturally invite stacked bar comparisons because every single bar across all demographic groups always shares the exact same fixed total daily time capacity!"
        ),
        "checkpoints": [
            {
                "question": "Why does the National Time Use Survey (2024) map naturally onto a fixed 24-hour (or 100%) stacked bar chart across demographics?",
                "options": [
                    "Because every person's daily activities must sum to the exact same fixed 24-hour (1,440-minute) total",
                    "Because everyone sleeps 12 hours",
                    "Because time cannot be measured in hours",
                    "Because rural and urban days have different lengths"
                ],
                "answer": 0,
                "hint": "Think about the total height of everyone's daily time budget!",
                "explanation": "A day is universally 24 hours (100% of daily time), so fixed-length stacked bars directly show how demographics trade off activities."
            },
            {
                "question": "In a 24-hour body-state stacked bar, if Sleep = 8 hrs, Sitting = 10 hrs, Light Walking = 4.5 hrs, how many hours remain for Vigorous Exercise?",
                "options": ["1.5 hours (24 − (8 + 10 + 4.5))", "2.5 hours", "3.0 hours", "0.5 hours"],
                "answer": 0,
                "hint": "Subtract 8 + 10 + 4.5 = 22.5 from 24 hours!",
                "explanation": "24 − 22.5 = 1.5 hours."
            }
        ]
    },
    {
        "id": 14,
        "title": "Cricket Share Averages",
        "subtitle": "Exercises 10.1–10.3: Cricket Run Rates, Share Portfolio Pricing & Fertilizer Mixtures",
        "speech": (
            "Now tackle high-yield applied problems from Exercise Sets Ten Point One through Ten Point Three: CRICKET RUN RATES, PORTFOLIO SHARE PRICING, AND FERTILIZER MIXTURES! "
            "First, CRICKET RUN RATES! Suppose a batting team scores at six runs per over during the first ten overs, then accelerates to nine runs per over during the next five overs, and finishes at twelve runs per over in the final five overs! What is their overall run rate across the twenty-over innings? Weight each run rate by the NUMBER OF OVERS bowled in that phase! Compute: ten times six (sixty) plus five times nine (forty-five) plus five times twelve (sixty) equals one hundred sixty-five total runs divided by twenty total overs equals EIGHT POINT TWO FIVE runs per over! "
            "Second, PORTFOLIO SHARE PRICING! Suppose an investor buys forty shares of a company at two hundred rupees per share, and later buys sixty more shares at two hundred fifty rupees per share! Average purchase price per share equals open forty times two hundred plus sixty times two hundred fifty close divided by one hundred shares, equaling TWO HUNDRED THIRTY RUPEES per share—showing how larger share purchases pull the weighted average cost!"
        ),
        "checkpoints": [
            {
                "question": "A cricket team scores at 5.5 runs/over for 20 overs, then 7.0 runs/over for the next 30 overs. What is the overall 50-over run rate?",
                "options": [
                    "6.4 runs/over ((20×5.5 + 30×7.0) / 50 = 320 / 50)",
                    "6.25 runs/over ((5.5 + 7.0) / 2)",
                    "6.0 runs/over",
                    "6.75 runs/over"
                ],
                "answer": 0,
                "hint": "Total runs = 20(5.5) + 30(7.0) = 110 + 210 = 320; divide by 50 overs!",
                "explanation": "Run rate is total runs divided by total overs: 320 / 50 = 6.4 runs/over."
            },
            {
                "question": "An investor buys 30 shares at ₹100 each and 20 shares at ₹150 each. What is the weighted average cost per share?",
                "options": [
                    "₹120 ((30×100 + 20×150) / 50 = 6000 / 50)",
                    "₹125 ((100 + 150) / 2)",
                    "₹115",
                    "₹130"
                ],
                "answer": 0,
                "hint": "Divide total money spent (₹3,000 + ₹3,000) by total shares (50)!",
                "explanation": "₹6,000 / 50 shares = ₹120 per share."
            }
        ]
    },
    {
        "id": 15,
        "title": "Space Infrastructure Data",
        "subtitle": "Exercises 10.4–10.5: Space Debris Growth, State School Playgrounds & Disability Census Data",
        "speech": (
            "Now examine rich real-world datasets from Exercise Sets Ten Point Four and Ten Point Five: SPACE DEBRIS GROWTH, SCHOOL PLAYGROUND INFRASTRUCTURE ACROSS INDIAN STATES, AND DISABILITY CENSUS DISTRIBUTIONS! "
            "In SPACE DEBRIS TRACKING, stacked column charts break orbital objects above Earth into active satellites, dead spacecraft, rocket bodies, and fragmentation debris across decades! Immediately you spot how fragmentation debris from collisions drives the dramatic vertical growth of total orbital clutter! "
            "In SCHOOL PLAYGROUND INFRASTRUCTURE MAPS across Indian states, hundred-percent stacked bars compare what percentage of primary, middle, and secondary schools in each state possess functional playgrounds versus no playground—allowing fair comparisons between populous states and smaller states without population size distorting the visual! "
            "Similarly, in DISABILITY CENSUS DISTRIBUTIONS across age brackets or regions, stacked charts reveal overall counts while hundred-percent stacked bars expose proportional shifts across visual, hearing, speech, and locomotor categories—empowering targeted public policy and inclusive school planning! Notice the key lesson uniting all three datasets: whenever groups differ wildly in population or total count, absolute stacked bars reveal raw scale and infrastructure gaps, whereas hundred-percent stacked bars expose proportional equity and composition shifts cleanly across all different Indian states, age groups, and diverse regional demographics!"
        ),
        "checkpoints": [
            {
                "question": "Why are 100% stacked bar charts ideal when comparing school playground availability between a large state (50,000 schools) and a small state (2,000 schools)?",
                "options": [
                    "Because scaling both states to 100% lets you directly compare the PROPORTION of schools with playgrounds without the 50,000-school bar dwarfing the 2,000-school bar",
                    "Because small states have no playgrounds",
                    "Because 100% charts hide percentages",
                    "Because absolute counts are always misleading"
                ],
                "answer": 0,
                "hint": "Think about comparing 80% of 50,000 vs 85% of 2,000 on an absolute bar chart!",
                "explanation": "Normalizing to 100% puts states of vastly different total school counts on an equal proportional footing."
            },
            {
                "question": "In a stacked chart of orbital space debris, if Active Satellites = 8,000 and Total Tracked Objects = 36,000, what do all non-active debris categories sum to?",
                "options": ["28,000 objects (36,000 − 8,000)", "44,000 objects", "8,000 objects", "18,000 objects"],
                "answer": 0,
                "hint": "Total stack height minus the Active Satellites band gives the remaining debris!",
                "explanation": "36,000 − 8,000 = 28,000 non-active debris objects."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Data Summary",
        "subtitle": "Chapter 10 Synthesis: Weighted Mean, Mixtures, Custom Weights & Stacked Data Visualisation",
        "speech": (
            "Congratulations on completing Chapter Ten: How Quantities Combine: Understanding Data! Let us review the four core statistical pillars you have mastered! "
            "Pillar One: NEVER blindly take the simple average of two averages! Whenever group sizes n and m differ, the true combined average is a n plus b m divided by n plus m—simple averaging works ONLY when n equals m or a equals b! "
            "Pillar Two: THE GENERAL WEIGHTED MEAN formula x-bar equals sum of W sub i x sub i divided by sum of W sub i handles liquid mixtures, fertilizer blends, Brahmagupta and Śrīdharācārya's gold alloy karat calculations, cricket run rates, share portfolio averages, AND custom importance weights like exam ratios and review recency! "
            "Pillar Three: STACKED COLUMN AND BAR CHARTS display overall totals alongside component breakdowns—always subtract the bottom boundary from the top boundary to read upper segments accurately! "
            "Pillar Four: HUNDRED-PERCENT STACKED BAR CHARTS replace multi-pie comparisons by aligning fixed-length proportional distributions cleanly—while pairing them with absolute charts ensures total scale is never forgotten! Now conquer the forty silent quiz questions ahead—checking weights, subtracting stacked boundaries carefully, and distinguishing relative proportions from raw absolute totals accurately on every single problem!"
        ),
        "checkpoints": [
            {
                "question": "Which statement accurately summarizes the difference between a regular stacked chart and a 100% stacked chart?",
                "options": [
                    "Regular stacked charts compare absolute totals and component sizes; 100% stacked charts compare relative percentage shares across equal-length bars",
                    "Both charts always look identical",
                    "100% stacked charts cannot show multiple groups",
                    "Regular stacked charts do not show totals"
                ],
                "answer": 0,
                "hint": "Ask: do the bars have different total heights (absolute) or identical 100% lengths (proportional)?",
                "explanation": "Regular stacked bars preserve absolute totals; 100% stacked bars normalize every bar to 100% to compare proportions."
            },
            {
                "question": "Which formula correctly computes ANY weighted mean across n components?",
                "options": [
                    "x̄ = (W₁x₁ + W₂x₂ + ... + Wₙxₙ) / (W₁ + W₂ + ... + Wₙ)",
                    "x̄ = (x₁ + x₂ + ... + xₙ) / (W₁ + W₂ + ... + Wₙ)",
                    "x̄ = (W₁x₁ + ... + Wₙxₙ) / n",
                    "x̄ = (x₁ + x₂ + ... + xₙ) / n"
                ],
                "answer": 0,
                "hint": "Sum the weighted products in the numerator and divide by the sum of all weights in the denominator!",
                "explanation": "Dividing Σ(Wᵢxᵢ) by ΣWᵢ ensures weights normalize properly regardless of scale."
            }
        ]
    }
]

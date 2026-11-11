#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 10: Proportional Reasoning-2
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 10 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Speed And Time",
        "subtitle": "Section 3.6 Travel Time vs Speed: Fixed Distance Product s₁ × t₁ = s₂ × t₂ (30 km/h for 3 h vs 60 km/h)",
        "speech": (
            "Observe inverse proportion cruising straight down an open highway! Whenever you travel between two fixed towns separated by constant Distance D, what exact relationship links average Speed (s) and travel Time (t)? Distance equals Speed multiplied by Time: s × t = D! Since Distance D remains locked constant across every trip between those identical towns, Speed and Time satisfy the classic constant-product law s₁ t₁ = s₂ t₂! "
            "Test NCERT's crisp travel example right now! Suppose a car drives from Town A to Town B at steady speed s₁ = 30 km/h and takes t₁ = 3 hours! First compute the constant distance invariant: D = 30 × 3 = 90 kilometres! Now double driving speed cleanly to s₂ = 60 km/h! Apply s₁ t₁ = s₂ t₂: 60 × t₂ = 90 → travel time halves directly to t₂ = 90 ÷ 60 = 1.5 hours! "
            "What if heavy rain forces driving speed down by factor 2/3 to 20 km/h? Travel time automatically scales inversely upward by reciprocal factor 3/2: 90 ÷ 20 = 4.5 hours! Remember carefully: ONLY when total journey distance remains fixed do driving speed and travel duration vary strictly inversely!"
        ),
        "checkpoints": [
            {
                "question": "A train covers a fixed distance at 30 km/h in 3 hours. At what steady speed must it run to cover that exact same journey in 1.5 hours?",
                "options": [
                    "60 km/h",
                    "15 km/h",
                    "45 km/h",
                    "90 km/h"
                ],
                "answer": 0,
                "hint": "Constant distance = 30 × 3 = 90 km; divide 90 by 1.5 hours!",
                "explanation": "Since s₁t₁ = s₂t₂, 30 × 3 = s₂ × 1.5 → 90 ÷ 1.5 = 60 km/h (halving time doubles speed)."
            },
            {
                "question": "A cyclist rides at 18 km/h and reaches school in 20 minutes. To arrive in 15 minutes along the identical route, what new speed is needed?",
                "options": [
                    "24 km/h   (18 × 20 = s₂ × 15)",
                    "13.5 km/h",
                    "22 km/h",
                    "25 km/h"
                ],
                "answer": 0,
                "hint": "Both times use minutes, so equate product 18 × 20 = s₂ × 15 directly!",
                "explanation": "Product = 360; 360 ÷ 15 = 24 km/h."
            }
        ]
    },
    {
        "id": 10,
        "title": "Workers Food Provisions",
        "subtitle": "Section 3.6 Inverse Workforce & Provisions: Headcount vs Job Completion Time & Hostel Food Duration",
        "speech": (
            "Now shift from highway speed to teams of builders and hostel kitchens! Suppose a community plans road construction or fence painting—where every equally skilled worker maintains identical steady pace! Here total workload equals constant Worker-Days (or Worker-Hours): Workers × Time = Constant Job Product w₁ t₁ = w₂ t₂! "
            "Test road construction cleanly! Suppose 12 workers pave a village road in 10 days! Total fixed workload equals 12 × 10 = 120 worker-days! How quickly could 15 workers finish that exact identical road? Equate constant products: 15 × t₂ = 120 → t₂ = 120 ÷ 15 = 8 days! Hiring extra workers shrinks project completion time proportionately! "
            "Apply the exact same constant-product reasoning to FOOD PROVISION DURATION! Suppose an expedition camp kitchen stocks enough rice for 40 hikers lasting 18 full days! Total daily meals equal 40 × 18 = 720 hiker-days! Suddenly 20 MORE hungry hikers join the camp (so the new total group size becomes 40 + 20 = 60 hikers—watch carefully NOT to plug in just 20!). Solve 60 × d₂ = 720 → existing food provisions finish much earlier in d₂ = 720 ÷ 60 = just 12 complete days!"
        ),
        "checkpoints": [
            {
                "question": "A hostel has food provisions stored for 40 students to last 15 days. If 10 MORE students join (making 50 total), how many days will the exact same provisions last?",
                "options": [
                    "12 days   (40 × 15 = 50 × d₂)",
                    "18.75 days",
                    "10 days",
                    "60 days"
                ],
                "answer": 0,
                "hint": "Total student-days = 40 × 15 = 600, shared now among 40 + 10 = 50 students!",
                "explanation": "600 student-days ÷ 50 students = 12 days."
            },
            {
                "question": "If 8 painters can paint a long school boundary fence in 9 days, how many painters working at the same pace are needed to finish it in 6 days?",
                "options": [
                    "12 painters",
                    "5 painters",
                    "14 painters",
                    "16 painters"
                ],
                "answer": 0,
                "hint": "Total workload = 8 × 9 = 72 painter-days; divide by 6 days!",
                "explanation": "w₂ × 6 = 8 × 9 = 72 → w₂ = 72 ÷ 6 = 12 painters."
            }
        ]
    },
    {
        "id": 11,
        "title": "Combined Work Rates",
        "subtitle": "Section 3.6 Combining Individual Output Rates: Adding Hourly/Daily Fractions for Shared Tasks",
        "speech": (
            "Careful—a brand-new twist enters Section Three Point Six when workers perform at DIFFERENT speeds! Suppose Painter A paints an entire fence alone in 6 hours, while Painter B paints that identical fence alone in 3 hours! A common trap tempts students to average 6 and 3 to guess 4.5 hours—wait: how could BOTH working together take LONGER than fast Painter B working alone?! Impossible! "
            "Solve combined shared work cleanly using UNIT WORK RATES per hour! Think fractionally inside just 1 hour: Painter A finishes 1/6 of the wooden fence per hour! Painter B finishes 1/3 of the wooden fence per hour! Working simultaneously side by side, their hourly work contributions ADD cleanly together: Combined Rate = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2 of the fence completed every single hour! "
            "Now invert that combined hourly rate cleanly to recover total shared working time: if 1/2 of the entire job finishes each passing hour, the full 1.0 job finishes cleanly in 1 ÷ (1/2) = EXACT 2 HOURS! Verify calmly: in 2 hours, Painter A paints 2/6 = 1/3, Painter B paints 2/3, and 1/3 + 2/3 equals one whole complete fence!"
        ),
        "checkpoints": [
            {
                "question": "Painter A paints a wall alone in 4 hours, and Painter B paints the same wall alone in 12 hours. Working together, how long do they take?",
                "options": [
                    "3 hours   (1/4 + 1/12 = 4/12 = 1/3 wall/hr → 3 hrs)",
                    "8 hours   (average of 4 and 12)",
                    "16 hours",
                    "2 hours"
                ],
                "answer": 0,
                "hint": "Add individual 1-hour work fractions: 1/4 + 1/12!",
                "explanation": "Combined hourly rate = 1/4 + 1/12 = 3/12 + 1/12 = 4/12 = 1/3 per hour → total time = 3 hours."
            },
            {
                "question": "Worker X finishes a carpentry job in 10 days, while Worker Y finishes it in 15 days. What fraction of the job do BOTH together complete in ONE day?",
                "options": [
                    "1/6 of the job per day   (taking 6 days total)",
                    "1/25 of the job per day",
                    "1/12 of the job per day",
                    "2/25 of the job per day"
                ],
                "answer": 0,
                "hint": "Add daily fractions 1/10 + 1/15 using common denominator 30!",
                "explanation": "1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6 per day, meaning the whole job takes 6 days together."
            }
        ]
    },
    {
        "id": 12,
        "title": "Pumps Tank Filling",
        "subtitle": "Section 3.6 Pump Flow Rates vs Tank Filling Durations: Single Pump Scaling & Multi-Pump Addition",
        "speech": (
            "Water tanks and pump flow rates unite BOTH constant-product inverse scaling AND combined rate addition! Look first at identical pumps or variable pump speeds filling ONE fixed water tank! Suppose a single pump delivers 20 litres per minute and fills an empty rooftop tank in 30 minutes! Total fixed tank capacity equals constant product 20 × 30 = 600 litres! Upgrade that pump's flow rate by factor 1.5 to 30 litres per minute: tank filling time drops inversely to 600 ÷ 30 = 20 minutes! Double flow rate to 40 litres per minute, and filling drops cleanly to 15 minutes! "
            "Similarly, if 4 identical taps fill a pool in 45 minutes (total = 4 × 45 = 180 tap-minutes), running 6 identical taps fills it in 180 ÷ 6 = 30 minutes! "
            "Now combine TWO DIFFERENT-SPEED PUMPS together! Pump One fills a rooftop cistern alone in 4 hours (hourly rate 1/4 per hour) and Pump Two fills it alone in 6 hours (hourly rate 1/6 per hour)! Opened together simultaneously, combined hourly rate = 1/4 + 1/6 = 3/12 + 2/12 = 5/12 of the tank per hour → total filling duration = 12/5 = 2.4 hours (2 hours 24 minutes)!"
        ),
        "checkpoints": [
            {
                "question": "Six identical water taps fill a school storage tank in 1 hour 20 minutes (80 minutes). How long will 5 such identical taps take to fill the same tank?",
                "options": [
                    "96 minutes (1 hour 36 minutes)",
                    "66.7 minutes",
                    "75 minutes",
                    "100 minutes"
                ],
                "answer": 0,
                "hint": "Constant tap-minutes = 6 × 80 = 480; divide 480 cleanly by 5 taps!",
                "explanation": "6 × 80 = 5 × t₂ → 480 ÷ 5 = 96 minutes (1 hr 36 min)."
            },
            {
                "question": "Pipe A fills a tank alone in 3 hours and Pipe B fills it alone in 6 hours. How long do both pipes take together?",
                "options": [
                    "2 hours",
                    "4.5 hours",
                    "9 hours",
                    "1.5 hours"
                ],
                "answer": 0,
                "hint": "Add hourly fill fractions: 1/3 + 1/6 = 3/6 = 1/2 per hour!",
                "explanation": "Combined rate = 1/3 + 1/6 = 1/2 tank/hour → full tank in 2 hours."
            }
        ]
    },
    {
        "id": 13,
        "title": "Tables Transport Charts",
        "subtitle": "Section 3.6 Figure it Out: Identifying Inverse Tables, Sleep Duration Charts & Transport Pie Charts",
        "speech": (
            "Practice Section Three Point Six's diagnostic data tables and visual pie charts! First: IDENTIFYING INVERSE PROPORTION PAIRS AND COMPLETING DATA TABLES! Suppose a numerical table lists x-values (2, 4, 8, ?) directly alongside y-values (18, 9, ?, 3)! Never guess wildly—multiply row products x · y immediately! Row 1: 2 × 18 = 36! Row 2: 4 × 9 = 36! Locked constant product k = 36 confirms INVERSE PROPORTION! Solve missing table slots instantly: when x = 8, y = 36 ÷ 8 = 4.5; when y = 3, x = 36 ÷ 3 = 12! "
            "Second: READING SLEEP DURATION AND SCHOOL TRANSPORTATION PIE CHARTS! On a 24-hour daily student sleep duration pie chart, an 8-hour nightly sleep sector spans exactly (8 ÷ 24) × 360° = 120° (one-third of a full day = 33.3%)! On a school transportation pie chart surveying 360 school pupils—notice how neatly 360 surveyed pupils makes 1 pupil equal EXACTLY 1° around the full circle! If 140° ride bicycles, 100° ride school buses, 80° walk on foot, and 40° carpool daily, you can immediately read every single exact student headcount directly straight off central sector degrees completely effortlessly every time!"
        ),
        "checkpoints": [
            {
                "question": "Inspect this table of (x, y) pairs: (3, 20), (6, 10), (12, 5), (15, ?). Are x and y inversely proportional, and what missing value completes y when x = 15?",
                "options": [
                    "Yes (product x·y = 60 constant); missing y = 4",
                    "Yes (quotient x/y = 6 constant); missing y = 2.5",
                    "No — product changes across rows",
                    "Yes (sum x + y = 16); missing y = 1"
                ],
                "answer": 0,
                "hint": "Multiply 3×20, 6×10, and 12×5 first to verify the invariant product!",
                "explanation": "Every pair multiplies to 60 (3×20 = 6×10 = 12×5 = 60), confirming inverse proportion with y = 60 ÷ 15 = 4."
            },
            {
                "question": "On a 24-hour daily sleep duration pie chart, a student sleeps 9 hours a night. What central angle represents sleep?",
                "options": [
                    "135°   ((9 / 24) × 360° = 135°)",
                    "90°",
                    "120°",
                    "150°"
                ],
                "answer": 0,
                "hint": "Simplify 9/24 = 3/8, then multiply 3/8 × 360°!",
                "explanation": "(9 / 24) × 360° = (3/8) × 360° = 135°."
            }
        ]
    },
    {
        "id": 14,
        "title": "Machines Production Schedules",
        "subtitle": "Section 3.6 Figure it Out: Combined Machine Production Schedules & Multi-Step Inverse Problems",
        "speech": (
            "Solve multi-step industrial production problems in Section Three Point Six's Figure it Out! Suppose a bottling workshop operates 5 identical packaging machines that seal 1,000 bottles in 6 hours! First challenge: keeping total output fixed at 1,000 bottles, how fast do 3 active machines finish? Apply constant inverse product: 5 × 6 = 3 × t₂ → 30 machine-hours ÷ 3 = 10 hours! "
            "Wait—what happens when BOTH machine count AND production target change simultaneously? Solve cleanly via machine-hours per batch! Five machines running 6 hours supply 30 machine-hours per 1,000 bottles (or 3 machine-hours per 100 bottles)! To seal 2,000 bottles (double total output!) using 10 active machines, calculate needed machine-hours = 30 × 2 = 60 machine-hours, divided cleanly by 10 machines = 6 hours! "
            "Now test COMBINED UNEQUAL MACHINES! Machine Alpha prints 1,200 school flyers in 4 hours (speed = 300 flyers per hour), while Machine Beta prints 1,200 flyers in 6 hours (speed = 200 flyers per hour)! Running simultaneously together, combined factory speed = 300 + 200 = 500 flyers per hour → 1,200 flyers finish printing cleanly in 1,200 ÷ 500 = exactly 2.4 hours (2 hours and 24 minutes)!"
        ),
        "checkpoints": [
            {
                "question": "Four identical printing machines produce a fixed batch of textbooks in 12 hours. If one machine breaks down leaving only 3 active machines, how long will the same batch take?",
                "options": [
                    "16 hours   (4 × 12 = 3 × 16)",
                    "9 hours",
                    "15 hours",
                    "18 hours"
                ],
                "answer": 0,
                "hint": "Fewer machines for the same batch → longer time! Compute 4 × 12 ÷ 3!",
                "explanation": "Total batch work = 4 × 12 = 48 machine-hours; 48 ÷ 3 = 16 hours."
            },
            {
                "question": "Machine M packs a crate order alone in 6 hours, and Machine N packs it alone in 12 hours. Running both machines together, how fast is the order completed?",
                "options": [
                    "4 hours   (1/6 + 1/12 = 3/12 = 1/4 per hr)",
                    "9 hours",
                    "3 hours",
                    "18 hours"
                ],
                "answer": 0,
                "hint": "Add hourly fractions 1/6 + 1/12!",
                "explanation": "1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4 order per hour → 4 hours total."
            }
        ]
    },
    {
        "id": 15,
        "title": "Direct Inverse Decision",
        "subtitle": "Diagnostic Decision Tool: Testing x/y vs x·y & Avoiding Non-Proportional Everyday Traps",
        "speech": (
            "Before finishing Chapter Ten, sharpen one crucial diagnostic skill: never assume EVERY table is either direct or inverse without testing! Real life holds THREE distinct cases: Direct Proportion, Inverse Proportion, or NEITHER! "
            "Apply our lightning two-step diagnostic test to any pair of variables (x, y)! Step One: check QUOTIENTS y/x across rows! If y/x stays completely equal—like fuel cost per litre (1 L = ₹100, 3 L = ₹300, 5 L = ₹500 → ₹100/L constant!)—you found DIRECT PROPORTION! "
            "Step Two: if row quotients vary, check row PRODUCTS x · y across entries! If x · y stays completely locked equal—like dividing a fixed ₹600 prize evenly among n winners (2 winners = ₹300 each, 3 = ₹200, 6 = ₹100 → product ₹600 constant!)—you discovered INVERSE PROPORTION! "
            "Step Three: what happens whenever NEITHER row quotient nor row product stays constant—such as tree height measured over consecutive years, or city taxi fare charging a fixed ₹30 minimum boarding base fee plus ₹15 per kilometre traveled? Because fixed base ₹30 breaks pure ratio scaling (1 km = ₹45, 2 km = ₹60 ≠ 2 × ₹45), that everyday taxi fare relationship is mathematically NEITHER direct nor inverse!"
        ),
        "checkpoints": [
            {
                "question": "An auto-rickshaw charges a fixed ₹25 minimum boarding fee PLUS ₹12 per kilometre traveled (1 km → ₹37; 2 km → ₹49). Which relationship links distance (x) and fare (y)?",
                "options": [
                    "Neither direct nor inverse   (37/1 ≠ 49/2 and 1×37 ≠ 2×49)",
                    "Direct proportion",
                    "Inverse proportion",
                    "Multi-term proportion"
                ],
                "answer": 0,
                "hint": "Test BOTH quotient y/x (37 vs 24.5) AND product x·y (37 vs 98)!",
                "explanation": "Adding a fixed ₹25 base prevents constant quotient (37 ≠ 24.5) and constant product (37 ≠ 98)."
            },
            {
                "question": "A fixed ₹1,200 scholarship fund is split equally among N prize winners. What type of proportion connects number of winners (N) and prize per winner (P)?",
                "options": [
                    "Inverse proportion   (since N × P = ₹1,200 constant product)",
                    "Direct proportion   (since P/N is constant)",
                    "Neither direct nor inverse",
                    "Multi-term spice ratio"
                ],
                "answer": 0,
                "hint": "Doubling winners cuts each winner's prize in half so N × P always stays ₹1,200!",
                "explanation": "N · P = 1,200 is a constant product, proving inverse proportion."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Formula Summary",
        "subtitle": "Summary Consolidation: Multi-Term Ratios, Partitioning, Pie Angles, Direct (x/y = k) & Inverse (x·y = k)",
        "speech": (
            "Consolidate the entire mathematical blueprint of Chapter Ten: Proportional Reasoning Part Two onto one unified reference guide! First, RECAP AND CROSS-MULTIPLICATION: two ratios a : b and c : d stand proportional whenever their cross-products match exactly: a × d = b × c! "
            "Second, REPRESENTATIVE FRACTIONS IN MAPS: RF compares map distance to ground distance in matching units, converting seamlessly between kilometres and 1 : 50 classroom floor plans! "
            "Third, MULTI-TERM RATIOS AND WHOLE PARTITIONING: extended ratios a : b : c : d scale uniformly (a/p = b/q = c/r = d/s), and partitioning whole x gives Component Share = x × (Term ÷ Sum of All Terms)—watching out carefully for coin value totals (denomination × count) and triangle side-length inequalities! "
            "Fourth, PIE CHARTS: simplify category counts via HCF and assign Central Angle = (Frequency ÷ Total) × 360°! "
            "Fifth, DIRECT VERSUS INVERSE PROPORTIONS: Direct variation keeps QUOTIENT completely constant (x/y = k), whereas Inverse variation keeps PRODUCT completely constant (x · y = k, scaling n ↔ 1/n reciprocally), while combined unequal workers or water pumps cleanly add individual 1-hour fractional work rates together to compute exact shared job completion durations cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Which equation pair accurately summarizes Direct Proportion vs Inverse Proportion from the Chapter 10 Summary?",
                "options": [
                    "Direct: x/y = k (constant quotient)   vs   Inverse: x · y = k (constant product)",
                    "Direct: x · y = k   vs   Inverse: x/y = k",
                    "Direct: x + y = k   vs   Inverse: x − y = k",
                    "Direct: x² = y   vs   Inverse: x = y²"
                ],
                "answer": 0,
                "hint": "Check which invariant stays equal when scaling variables together vs oppositely!",
                "explanation": "Direct proportion maintains x/y = k; inverse proportion maintains x · y = k (equivalently x₁y₁ = x₂y₂)."
            },
            {
                "question": "To divide a total quantity x across a three-term ratio a : b : c, what gives the share of component b?",
                "options": [
                    "x × b / (a + b + c)",
                    "x × (a + b + c) / b",
                    "x × b / (a + c)",
                    "x ÷ b"
                ],
                "answer": 0,
                "hint": "Component share equals total x times the component's fraction of the SUM of all terms!",
                "explanation": "Sum of all terms = a + b + c, so component b receives x × b / (a + b + c)."
            }
        ]
    }
]

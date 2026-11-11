#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 12: Tales by Dots and Lines
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 12 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Two Step Interpretation",
        "subtitle": "Section 5.2 Structured 2-Step Line Graph Reading: (1) Scales/Axes/Slopes & (2) Peaks/Troughs/Trends",
        "speech": (
            "Before jumping prematurely to quick conclusions from any chart or news figure, master NCERT's structured TWO-STEP INTERPRETATION PROCESS inside Section Five Point Two! Many statistical misreadings happen simply because hurried readers skip Step One completely! "
            "STEP ONE: CAREFULLY READ THE GRAPH'S STRUCTURAL SKELETON! Inspect both horizontal x-axis and vertical y-axis labels along with exact measurement units! Check carefully whether the vertical y-axis starts honestly at zero OR uses a compressed broken/truncated baseline scale! Verify grid tick step sizes (10s, 100s, or 1,000s), identify distinct line markers or color legends, and examine segment SLOPES: steep upward segments signal rapid growth, gentle upward slopes signal modest growth, completely flat horizontal segments mean ZERO change, and steep downward segments signal sharp sudden decline! "
            "STEP TWO: INFER DATA PATTERNS, PEAKS, TROUGHS, AND COMPARATIVE TRENDS! Locate exact global maximum PEAKS (the highest sharp upward spikes) and minimum TROUGHS (the lowest deep downward dips), measure exact total vertical numeric range separating both extremes cleanly, spot repeating seasonal annual cycles across multiple consecutive calendar years, compare multiple overlaid curves' crossover intersection points carefully, and explain thoughtfully WHY underlying real-world physical events drove each observed rise or dip across every single time interval!"
        ),
        "checkpoints": [
            {
                "question": "In NCERT's 2-Step Line Graph Interpretation methodology, what must you examine FIRST in Step 1 before inferring peaks or real-world stories?",
                "options": [
                    "Identify axis titles, scale intervals, starting zero/ticks, legend markers, and segment slopes",
                    "Guess which country produced the largest peak without reading numbers",
                    "Always connect the first and last point only",
                    "Ignore vertical y-axis units"
                ],
                "answer": 0,
                "hint": "Check whether the vertical axis starts at 0 and what units each grid box represents!",
                "explanation": "Step 1 reads scales, axes, units, markers, and slopes accurately so Step 2 inferences about peaks/troughs aren't misled."
            },
            {
                "question": "Along one segment of a time-series line graph from Month 4 to Month 5, the plotted line runs COMPLETELY HORIZONTAL (zero slope). What does that flat segment tell us?",
                "options": [
                    "The measured quantity stayed completely constant with zero change between Month 4 and Month 5",
                    "Data was deleted at Month 5",
                    "The value dropped down to zero",
                    "The value doubled at Month 5"
                ],
                "answer": 0,
                "hint": "Think of y-value at Month 4 equaling y-value at Month 5!",
                "explanation": "Zero slope on a time-series line graph signifies no change (constant value) across that interval."
            }
        ]
    },
    {
        "id": 10,
        "title": "Space Rain Births",
        "subtitle": "Section 5.2 Real-World Line Graphs: UN Space Launches, India Coastal Rainfall & Monthly Live Births",
        "speech": (
            "Apply your crisp two-step line-graph reading toolkit across three diverse real-world scientific datasets explicitly highlighted in Section Five Point Two! "
            "Dataset One: ANNUAL SPACE OBJECT LAUNCHES WORLDWIDE (monitored officially each year by the UN Office for Outer Space Affairs)! Follow the historical orbital launch trajectory curve carefully from early Space Age decades right through 2020 and beyond: a long modest steady horizontal plateau suddenly explodes vertically upward into a sky-high exponential hockey-stick climb driven largely by modern low-orbit commercial small-satellite mega-constellations! "
            "Dataset Two: MONTHLY RAINFALL PATTERNS ALONG INDIA'S WEST VERSUS EAST COASTS! Compare coastal cities such as Mangalore or Mumbai on India's West Coast directly against Chennai sitting along the East Coast! Notice the stunning opposite monsoon seasonal rhythm: the West Coast peaks sharply during the June–September Southwest Monsoon rains, whereas Chennai's East Coast stays much drier in June yet spikes dramatically during October–December Northeast Monsoon rains and storms! "
            "Dataset Three: MONTHLY LIVE BIRTH TRENDS! Plotting monthly hospital and regional live births across consecutive calendar years uncovers clear repeating annual biological seasonal waves, peak late-summer and autumn birth months, and lowest early-spring trough months clearly, consistently, and reliably across diverse Indian geographic states and regions!"
        ),
        "checkpoints": [
            {
                "question": "Comparing India's West Coast vs East Coast (Chennai) monthly rainfall line graphs reveals which clear seasonal peak difference?",
                "options": [
                    "West Coast peaks sharply in June–September (SW Monsoon), whereas East Coast (Chennai) peaks in October–December (NE Monsoon)",
                    "Both coasts receive identical maximum rainfall in January",
                    "West Coast stays completely dry in July",
                    "East Coast receives zero rain from October to December"
                ],
                "answer": 0,
                "hint": "Think of Southwest monsoon hitting western shores in summer vs returning Northeast monsoon hitting Chennai in late autumn!",
                "explanation": "West Coast peaks June–September while Chennai's East Coast peaks later during October–December."
            },
            {
                "question": "What major overall trend appears in the UN Office for Outer Space Affairs graph of annual space objects launched worldwide?",
                "options": [
                    "Modest steady counts for decades followed by a massive steep upward surge in recent years due to satellite constellations",
                    "A steady drop down to zero launches after 2000",
                    "Strictly horizontal flat counts every single year",
                    "A single peak only in 1960 followed by zero activity"
                ],
                "answer": 0,
                "hint": "Think of modern mega-constellations launching thousands of satellites compared to earlier decades!",
                "explanation": "Annual launched objects climbed dramatically in recent years with steep positive slopes."
            }
        ]
    },
    {
        "id": 11,
        "title": "Dietary Preference Maps",
        "subtitle": "Section 5.2 Infographics: Visual Spatial Data Maps of Rice vs Wheat Dietary Preferences Across India",
        "speech": (
            "Mathematical data stories do not live exclusively inside dry spreadsheets and x-y coordinate axes! Explore rich INFOGRAPHICS in Section Five Point Two—skillfully pairing geographic maps, crisp icons, proportions, and vivid color gradients so complex nationwide statistical patterns communicate clearly at a single visual glance! "
            "Examine NCERT's colorful dietary infographic map of India comparing everyday household staple food grain preferences between RICE and WHEAT across all Indian states and union territories! Instead of scanning thirty separate long rows of dense percentage numbers inside a multi-page printed statistical data report, shading every Indian state directly onto one crisp geographic map using its dominant staple color immediately reveals stark continental climate, water, and agricultural crop zones! "
            "Look closely across eastern, northeastern, and southern coastal states—Kerala, Tamil Nadu, Andhra Pradesh, Odisha, West Bengal, and Assam—glowing strongly inside the deep RICE-dominant color band thanks to heavy annual monsoon rains and fertile flooded river deltas! Now swing northwest across Punjab, Haryana, Rajasthan, Uttar Pradesh, and Madhya Pradesh, where bright golden WHEAT shading dominates fertile cool winter crop plains—while central transition states display balanced mixed rice-and-wheat regional household dietary habits very clearly together side by side at just one single quick visual glance!"
        ),
        "checkpoints": [
            {
                "question": "What unique advantage does a shaded spatial Infographic Map (like India's state-by-state Rice vs Wheat preference map) provide over a plain alphabetical state table?",
                "options": [
                    "It reveals geographic clusters, regional climate patterns, and neighbor transitions instantaneously at one glance",
                    "It deletes all numerical data permanently",
                    "It converts all states into identical percentages",
                    "It removes the need for a color key/legend"
                ],
                "answer": 0,
                "hint": "Notice how quickly your eye spots coastal/eastern rice belts vs northern wheat plains on a map!",
                "explanation": "Spatial infographics expose geographic clustering (monsoon rice regions vs northern wheat belts) far faster than raw alphabetical tables."
            },
            {
                "question": "According to Indian regional dietary infographic patterns, which pair contrasts typical Rice-dominant vs Wheat-dominant zones?",
                "options": [
                    "Southern/Eastern coastal states (e.g., Tamil Nadu, West Bengal) → Rice; Northwestern plains (e.g., Punjab, Haryana) → Wheat",
                    "Punjab & Haryana → Rice only; Kerala & Odisha → Wheat only",
                    "All states eat 100% identical staples",
                    "Rajasthan grows only deep-water rice"
                ],
                "answer": 0,
                "hint": "Link monsoon water abundance in South/East India with rice and northern winter plains with wheat!",
                "explanation": "Wet coastal/eastern regions predominantly favor rice, whereas northern/northwestern plains predominantly favor wheat."
            }
        ]
    },
    {
        "id": 12,
        "title": "Activity Time Strips",
        "subtitle": "Section 5.2 What can a Strip Say?: Color-Coded 24-Hour Strips in 30-Minute Blocks Across Weekdays, Weekends & Ages",
        "speech": (
            "Compare how different people spend one complete 24-hour day side by side using NCERT's intuitive visual comparison tool: WHAT CAN A STRIP SAY? Picture one sleek straight horizontal bar representing a full 24-hour clock sliced cleanly into exactly 48 tiny equal 30-minute (half-hour) unit blocks running from midnight to midnight! Color-code every single 30-minute block cleanly by daily activity: deep midnight blue for Sleep, warm amber for School or Work, fresh emerald for Meals and Chores, bright cyan for Sports and Play, and rose for Commute or Screen time! "
            "Now stack two or three aligned 24-hour horizontal time strips directly one above another and compare diverse daily lifestyles side by side in half a second! Compare a middle-school student's regular busy WEEKDAY strip against a relaxed WEEKEND strip: weekday reveals a solid continuous 6-hour school classroom study block, whereas weekend swaps morning classroom hours for extra morning sleep plus longer afternoon outdoor sports and play blocks! "
            "Finally stack daily 24-hour strips vertically across diverse AGE GROUPS—comparing a young primary school child, a busy working adult, and a retired senior grandparent—instantly spotting how daily sleep duration and active daily schedules shift cleanly across human life stages!"
        ),
        "checkpoints": [
            {
                "question": "A 24-hour color-coded activity strip is divided uniformly into 30-minute (0.5-hour) blocks. How many total blocks form the complete strip, and how many hours do 16 blue sleep blocks represent?",
                "options": [
                    "48 total blocks; 16 blocks = 8 hours of sleep",
                    "24 total blocks; 16 blocks = 16 hours of sleep",
                    "48 total blocks; 16 blocks = 4 hours of sleep",
                    "30 total blocks; 16 blocks = 8 hours of sleep"
                ],
                "answer": 0,
                "hint": "Each hour holds TWO 30-minute blocks (24 × 2 = 48 total; 16 × 0.5 hr)!",
                "explanation": "24 hours ÷ 0.5 hours = 48 equal blocks; 16 half-hour blocks = 16 × 0.5 = 8 hours."
            },
            {
                "question": "Why are stacked 24-hour horizontal activity strips superior to separate disconnected pie charts when comparing weekday vs weekend routines?",
                "options": [
                    "Aligned timelines let you directly match exact clock times (like waking, school, meals, bedtime) vertically across days",
                    "Because pie charts cannot display percentages",
                    "Because strips change the total number of hours in a weekend",
                    "Because strips ignore time duration completely"
                ],
                "answer": 0,
                "hint": "Look vertically down a stack of aligned 24-hour bars from midnight to midnight!",
                "explanation": "Stacked strips align identical clock intervals vertically, exposing BOTH total duration and exact timing shifts."
            }
        ]
    },
    {
        "id": 13,
        "title": "Sleep Age Curve",
        "subtitle": "Section 5.2 Data Story Sleepy-Deepy: Smooth Multi-Point Sleep Curve Across Ages 6–75 vs Cluttered Bars",
        "speech": (
            "Explore Section Five Point Two's engaging National Time Use Survey investigation—DATA STORY: SLEEPY-DEEPY! National survey data carefully measured average daily sleep duration across seventy consecutive human age points spanning young school children age 6 all the way up to senior adults age 75! "
            "First pause and ask an important visual-design question: WHY did NCERT choose ONE smooth multi-point LINE CURVE here instead of drawing a 70-bar vertical BAR CHART? Imagine squeezing 70 vertical rectangles tightly side by side onto one narrow textbook page: individual bars collapse into skinny overlapping stripes resembling a dense blurry picket fence, blinding the reader to subtle life-stage changes! By plotting clean points and connecting consecutive ages into ONE smooth trajectory, the entire 70-year human lifespan fits gracefully inside a single readable frame! "
            "Read the fascinating biological human life story straight off the Sleepy-Deepy age curve! Young six-year-olds clearly require longest daily nighttime rest—averaging around 9.5 to 10 full hours every single night! Daily sleep duration drops gently downward through active teenage school years and stays relatively steady near 7.5 to 8 hours across busy working middle adulthood, before ticking noticeably upward again during calm senior retirement years well past age 65 cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In the 'Sleepy-Deepy' National Time Use Survey (ages 6 to 75 years), why does a smooth multi-point line curve outperform a 70-column bar chart?",
                "options": [
                    "70 adjacent bars create heavy visual clutter, whereas one smooth line clearly reveals continuous age trends across the lifespan",
                    "Because bar charts cannot show decimals like 8.5 hours",
                    "Because line curves hide minimum and maximum ages",
                    "Because age 6 to 75 only has 5 categories"
                ],
                "answer": 0,
                "hint": "Picture 70 thick colored bars squeezed side-by-side onto a narrow screen!",
                "explanation": "Smooth multi-point curves cleanly track continuous progression across dense numeric variables like 70 yearly ages."
            },
            {
                "question": "What overall age-related pattern does the Sleepy-Deepy curve show across ages 6 to 75?",
                "options": [
                    "Highest sleep hours in young childhood (~9.5–10 hrs), dipping lower in mid-adulthood (~7.5 hrs), and rising slightly in senior years",
                    "Zero sleep at age 6 climbing to 18 hours at age 40",
                    "Identical 8.0 hours at every single age from 6 to 75",
                    "Steady drop all the way to 2 hours at age 75"
                ],
                "answer": 0,
                "hint": "Think about growing children, busy working adults, and older retirees!",
                "explanation": "Children sleep longest, working-age adults average fewer hours, and older adults recover slightly more rest."
            }
        ]
    },
    {
        "id": 14,
        "title": "Mean Median Tradeoffs",
        "subtitle": "Comparative Data Thinking: Balancing Mean Sensitivity Against Median Stability in Real Datasets",
        "speech": (
            "Step back now and compare our two core numeric summaries from Section Five Point One—ARITHMETIC MEAN versus POSITIONAL MEDIAN—side by side using realistic data situations! Knowing WHICH central summary tells the more honest story is a true hallmark of smart statistical reasoning! "
            "Notice closely how the ARITHMETIC MEAN behaves exactly like a sensitive physics seesaw fulcrum: EVERY single observation tugs the balance point according to BOTH its direction AND its exact distance away! Suppose five ordinary village households earn monthly incomes of ₹20,000, ₹22,000, ₹24,000, ₹25,000, and ₹29,000—clean symmetric numbers where Mean (₹24,000) and Median (₹24,000) agree beautifully! "
            "Now imagine one ultra-wealthy billionaire business tycoon suddenly moves onto that quiet ordinary residential street earning a massive ₹50,00,000 every single month! Immediately the Arithmetic Mean rockets absurdly upward well past ₹8,50,000—completely failing to describe ANY typical everyday working household living quietly along that entire street! Meanwhile, the POSITIONAL MEDIAN nudges gently upward from ₹24,000 to just ₹24,500—shielding the true typical resident household monthly income completely from wild extreme outlier distortion! Always choose Arithmetic Mean whenever exact combined totals, sums, and linear algebra truly matter; always choose Median whenever extreme outliers heavily skew your numerical dot plot!"
        ),
        "checkpoints": [
            {
                "question": "Six house prices in a neighborhood are ₹30L, ₹32L, ₹35L, ₹36L, ₹38L, and one luxury mansion at ₹300L. Which summary measure best represents a 'typical' house price here?",
                "options": [
                    "The Median (₹35.5L), because the ₹300L outlier pulls the Mean upward to ₹78.5L",
                    "The Mean (₹78.5L), because ₹300L should dominate every other home",
                    "The maximum value (₹300L)",
                    "The range (₹270L)"
                ],
                "answer": 0,
                "hint": "Notice five out of six homes cost ₹30L–₹38L, while ₹300L is an extreme outlier!",
                "explanation": "Extreme outlier ₹300L inflates the mean to ₹78.5L (higher than 5 of 6 houses), whereas median ₹35.5L stays faithful."
            },
            {
                "question": "When is the Arithmetic Mean indispensable and superior to the Median?",
                "options": [
                    "When total combined sum matters (e.g., total team weight, average crop yield per tree, or exact fair sharing)",
                    "When an extreme outlier must be ignored completely",
                    "Only when data contains zero repeated values",
                    "When data values are sorted backward"
                ],
                "answer": 0,
                "hint": "Recall Missing Wrestler Weight and Coconut Harvest problems: Sum = Mean × Count!",
                "explanation": "Mean ties directly to total sum (Sum = Mean × Count), making it essential for totals, rates, and linear operations."
            }
        ]
    },
    {
        "id": 15,
        "title": "Chapter Data Summary",
        "subtitle": "Summary Consolidation: Fulcrum Mean, Linear/Insertion Effects, Frequencies, Spreadsheets, Graphs & Strips",
        "speech": (
            "Consolidate every essential statistical insight of Chapter Twelve: Tales by Dots and Lines cleanly onto one master revision map! First, MEAN AS A FULCRUM: on any dot plot, the mean balances total left-hand distances equal to total right-hand distances! Inserting values higher than the mean pulls it upward; lower values pull it downward; symmetric equal-distance pairs keep the balance point completely fixed! "
            "Second, LINEAR OPERATIONS AND ALGEBRAIC PROBLEM SOLVING: adding ±c to all entries shifts the mean by ±c; multiplying every entry by scale factor k scales the mean directly by k! Finding missing weights or fixing harvest counting errors applies Total Sum = Mean × Count! "
            "Third, MEDIAN, FREQUENCY TABLES, AND SPREADSHEETS: medians remain stable when balanced points flank both sides; frequency tables demand weighted mean Σ(fᵢxᵢ) ÷ Σfᵢ and cumulative frequency ranks for medians; digital spreadsheets compute =SUM(B3:G3) and =AVERAGE(B3:G3) instantaneously! "
            "Fourth, VISUAL DATA STORIES: carefully execute the structured 2-step line-graph reading protocol (Step 1: check scales, axes, markers, slopes; Step 2: infer peaks, troughs, comparative trends) across state temperature curves, UN annual space launches, Indian coastal rainfall, live births, rice/wheat infographic maps, 48-block 24-hour activity strips, and smooth Sleepy-Deepy lifespan age curves!"
        ),
        "checkpoints": [
            {
                "question": "Which summary rule accurately links Mean operations, Frequency Tables, and Spreadsheets?",
                "options": [
                    "Adding +c shifts mean by +c; weighted mean = Σ(fᵢxᵢ)/Σfᵢ; spreadsheet formula =AVERAGE(B3:G3)",
                    "Adding +c leaves mean unchanged; weighted mean ignores frequencies fᵢ",
                    "Multiplying data by k keeps mean fixed; spreadsheets start formulas with '?'",
                    "LHS distance at mean is always double RHS distance"
                ],
                "answer": 0,
                "hint": "Check all three pillars: +c linear shift, Σ(fᵢxᵢ)/Σfᵢ weighted mean, and =AVERAGE(...) syntax!",
                "explanation": "Uniform +c shifts mean +c, frequency tables weight values by fᵢ, and spreadsheets evaluate =AVERAGE(B3:G3)."
            },
            {
                "question": "Which visual format is best suited for comparing continuous 70-age sleep averages vs comparing weekday/weekend 30-minute clock routines?",
                "options": [
                    "Smooth multi-point Line Curve for 70-age Sleepy-Deepy trends; stacked 48-block 24-Hour Strips for daily clock routines",
                    "A 70-bar chart for Sleepy-Deepy; an unweighted dot plot for daily clock routines",
                    "An infographic map for daily clock routines",
                    "Single numbers without any axes"
                ],
                "answer": 0,
                "hint": "Remember Sleepy-Deepy (Section 5.2) and 'What can a Strip Say?' (48 half-hour blocks)!",
                "explanation": "Smooth curves avoid 70-bar clutter across ages 6–75, while aligned 48-block 24-hour strips compare daily timings cleanly."
            }
        ]
    },
    {
        "id": 16,
        "title": "Game Of Hex",
        "subtitle": "It's Puzzle Time! Game of Hex: 11 × 11 Hexagonal Grid Strategy Connecting Opposite Colored Sides",
        "speech": (
            "Conclude Chapter Twelve with a thrilling mathematical strategy game: IT'S PUZZLE TIME—THE GAME OF HEX! Picture a crisp diamond-shaped board tiled neatly with 11 horizontal rows by 11 slanted columns of hexagonal honeycomb cells—121 distinct hexagons in total! Two opposing players take turns placing one colored stone per move onto any unoccupied empty hexagon: Player One (Red or Amber) aims to forge ONE unbroken connected chain of colored stones linking the TOP edge cleanly down to the BOTTOM edge! Player Two (Blue or Cyan) aims to bridge the LEFT edge completely across to the RIGHT edge! "
            "Notice two breathtaking topological properties hiding cleanly inside Hex! First, winning colored stone chains do NOT need ruler-straight lines—winding zigzags, bends, and clever two-cell diamond 'bridges' (leaving two separating empty hexagons so if your opponent blocks either connecting cell, you immediately capture the other!) link seamlessly across the entire board! Second, mathematicians proved a celebrated NO-TIE THEOREM for 11 × 11 Hex: it is MATHEMATICALLY IMPOSSIBLE for any completely filled Hex board to finish in a tied draw—ONE player MUST always complete an unbroken edge-to-edge winning path! Practice blocking and building chains on our interactive Hex board right now!"
        ),
        "checkpoints": [
            {
                "question": "On the standard 11 × 11 hexagonal Game of Hex board (121 cells), what is the exact winning objective of each player?",
                "options": [
                    "Form one unbroken continuous chain of your colored hexagons connecting your two assigned opposite borders",
                    "Capture and remove opponent stones off the board like checkers",
                    "Place 8 non-attacking pieces on dark hexagons only",
                    "Force both players into an equal draw"
                ],
                "answer": 0,
                "hint": "Think Red bridges Top-to-Bottom while Cyan bridges Left-to-Right without ever needing straight lines!",
                "explanation": "Hex is a pure connection game: Player 1 connects Top–Bottom borders, while Player 2 connects Left–Right borders."
            },
            {
                "question": "What remarkable mathematical guarantee holds once all 121 hexagons of an 11 × 11 Hex board are completely filled (no empty cells remaining)?",
                "options": [
                    "A tie/draw is IMPOSSIBLE — exactly one of the two players MUST hold an unbroken winning path",
                    "Every full board ends in a 50-50 draw",
                    "Both players simultaneously win 50% of the time",
                    "At least 10 hexagons always stay unconnected"
                ],
                "answer": 0,
                "hint": "If Red fails to bridge Top-to-Bottom, Red's unbridged wall acts as a continuous Cyan path Left-to-Right (and vice versa)!",
                "explanation": "By Hex's famous No-Tie Theorem, completely filling the grid guarantees one unbroken path blocks the perpendicular direction."
            }
        ]
    }
]

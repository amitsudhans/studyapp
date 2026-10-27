# Class 8 Mathematics Chapter 12: Data Handling (Tales by Dots and Lines)
SLIDES_DATA = [
  {
    "id": 1,
    "title": "Tales by Dots and Lines",
    "subtitle": "The Art & Science of Data Storytelling",
    "content": "<p>In our modern world, we are surrounded by a constant deluge of numbers—sports scores, weather forecasts, school attendance, and screen time. But raw lists of numbers are silent until we give them a voice. <strong>Data Handling</strong> is the art and science of organizing, summarizing, and presenting numbers so that meaningful stories emerge.</p><p class='mt-2'>A single dot on a number line marks an individual observation. Stacking multiple dots builds a <strong>dot plot</strong>, revealing frequency, spread, and clusters at a glance. Connecting sequential dots across time gives birth to a <strong>line graph</strong>, capturing continuous trends and trajectories.</p>",
    "key_takeaways": [
      "Data handling translates raw numerical records into clear, actionable visual stories.",
      "A dot plot displays individual frequencies along an ordered scale, highlighting clusters and gaps.",
      "Connecting consecutive data points with line segments reveals rates of change over time."
    ],
    "formula": "$$\\text{Data Handling: } \\text{Collect} \\to \\text{Organise (Tables)} \\to \\text{Analyse (Mean/Median)} \\to \\text{Visualise}$$",
    "simulator_type": "tales_dots_lines_intro",
    "checkpoints": [
      {
        "question": "What primary advantage does a dot plot offer over a simple unorganized list of raw test scores?",
        "options": [
          "It automatically multiplies all test scores by 10",
          "It immediately reveals the distribution, clusters, most frequent values (mode), and extreme gaps",
          "It hides the lowest scores so everyone feels successful",
          "It requires no axes or measurement scale"
        ],
        "correct": 1,
        "explanation": "A dot plot visualizes the distribution of data points along an ordered number line, making clusters, peaks (mode), and data spread instantly apparent."
      },
      {
        "question": "When is a line graph more appropriate to use than a static bar chart?",
        "options": [
          "When comparing completely unrelated categories like favorite fruit flavors",
          "When tracking continuous change over a continuous variable such as time, temperature, or age",
          "When the data contains only two numbers",
          "When no numbers are available"
        ],
        "correct": 1,
        "explanation": "Line graphs excel at showing continuous trends over time (e.g., hourly temperature, annual population, daily rainfall) because line segments represent continuous transitions."
      }
    ]
  },
  {
    "id": 2,
    "title": "The Balancing Act",
    "subtitle": "Arithmetic Mean as the Center of Mass & Fulcrum",
    "content": "<p>We often calculate the <strong>arithmetic mean</strong> (or average) by adding all values and dividing by the count: $\\bar{x} = \\frac{\\sum x_i}{N}$. But what does this number physically represent?</p><p class='mt-2'>Think of the data points as identical weights placed along a balanced physical seesaw (number line). The arithmetic mean $\\bar{x}$ is the exact <strong>fulcrum (balance point)</strong> where the seesaw rests in perfect horizontal equilibrium!</p><p class='mt-2'>At the mean, the sum of all positive deviations (weights to the right) exactly balances the sum of all negative deviations (weights to the left):</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\sum_{i=1}^N (x_i - \\bar{x}) = 0$$</div>",
    "key_takeaways": [
      "The arithmetic mean is the physical center of mass (balance fulcrum) of the dataset.",
      "The sum of algebraic deviations of all observations from their arithmetic mean is always strictly zero.",
      "Mean balances total numerical values, making it sensitive to every single observation."
    ],
    "formula": "$$\\bar{x} = \\frac{\\sum_{i=1}^N x_i}{N} \\iff \\sum_{i=1}^N (x_i - \\bar{x}) = 0$$",
    "simulator_type": "balancing_act_mean_fulcrum",
    "checkpoints": [
      {
        "question": "If the numbers $2, 4, 6, 8, 10$ have an arithmetic mean of $6$, what is the sum of their deviations $(x_i - 6)$?",
        "options": [
          "30",
          "12",
          "0",
          "-6"
        ],
        "correct": 2,
        "explanation": "Deviations are: $(2-6) + (4-6) + (6-6) + (8-6) + (10-6) = -4 + (-2) + 0 + 2 + 4 = 0$. The sum of deviations about the mean is always zero!"
      },
      {
        "question": "On a physical seesaw with unit weights placed at positions $3, 7, 8$, at which position must the fulcrum be placed for the seesaw to balance?",
        "options": [
          "Position 5",
          "Position 6",
          "Position 7",
          "Position 8"
        ],
        "correct": 1,
        "explanation": "The balance fulcrum is the arithmetic mean: $\\bar{x} = \\frac{3 + 7 + 8}{3} = \\frac{18}{3} = 6$."
      }
    ]
  },
  {
    "id": 3,
    "title": "Unchanging Mean",
    "subtitle": "Properties of Mean Under Shifts & Uniform Scaling",
    "content": "<p>How does the arithmetic mean behave when we modify every observation in a dataset? The mean follows elegant mathematical transformation laws:</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Addition / Subtraction Invariance:</strong> If a constant value $c$ is added to every data point ($x_i' = x_i + c$), the new mean shifts by exactly $c$: $\\bar{x}_{\\text{new}} = \\bar{x} + c$.</li><li><strong>Multiplication / Division Scaling:</strong> If every data point is multiplied by a factor $k$ ($x_i' = k \\cdot x_i$), the new mean is multiplied by the same factor: $\\bar{x}_{\\text{new}} = k \\cdot \\bar{x}$.</li><li><strong>Compensating Changes:</strong> If you increase one value by $+5$ and decrease another value by $-5$, the total sum remains unchanged, so the arithmetic mean remains <strong>strictly unchanged</strong>!</li></ul>",
    "key_takeaways": [
      "Adding constant $c$ to all values shifts the mean by $+c$: $\\overline{x+c} = \\bar{x} + c$.",
      "Multiplying all values by factor $k$ scales the mean by $k$: $\\overline{kx} = k\\bar{x}$.",
      "Internal transfers between observations that preserve the total sum leave the mean unchanged."
    ],
    "formula": "$$\\overline{a x + b} = a \\bar{x} + b, \\quad \\text{Sum Preservation: } \\Delta \\left(\\sum x_i\\right) = 0 \\implies \\Delta \\bar{x} = 0$$",
    "simulator_type": "unchanging_mean_properties",
    "checkpoints": [
      {
        "question": "The mean score of 20 students in a math test was 65. If the teacher awards 5 bonus grace marks to every student, what is the new mean score?",
        "options": [
          "65",
          "70",
          "75",
          "130"
        ],
        "correct": 1,
        "explanation": "When a constant $c = 5$ is added to every observation, the mean increases by exactly $c$: $\\bar{x}_{\\text{new}} = 65 + 5 = 70$."
      },
      {
        "question": "In a dataset of 5 numbers with mean 24, one number is increased by 8 and another is decreased by 8. What happens to the mean?",
        "options": [
          "The mean increases by 8",
          "The mean decreases by 8",
          "The mean remains unchanged at 24",
          "The mean cannot be determined"
        ],
        "correct": 2,
        "explanation": "The net change to the sum is $+8 - 8 = 0$. Since the total sum and count remain unchanged, the arithmetic mean remains exactly 24."
      }
    ]
  },
  {
    "id": 4,
    "title": "Outlier Impact",
    "subtitle": "Mean Sensitivity vs. Median Robustness to Outliers",
    "content": "<p>While the arithmetic mean is an excellent summary for symmetric data, it has a serious vulnerability: <strong>extreme outliers</strong>.</p><p class='mt-2'>Consider five friends earning monthly pocket money of $\\text{Rs } 100, 120, 130, 150, 1000$. The single wealthy friend pulls the mean up to $\\frac{1500}{5} = \\text{Rs } 300$, which is higher than what $80\\%$ of the group earns!</p><p class='mt-2'>In contrast, the <strong>Median</strong> (the middle value when arranged in order: $\\text{Rs } 130$) is <strong>robust</strong>. If the richest friend received $\\text{Rs } 10,000$ instead of $\\text{Rs } 1,000$, the mean would jump to $\\text{Rs } 2,100$, while the median would remain <strong>completely unchanged</strong> at $\\text{Rs } 130$!</p>",
    "key_takeaways": [
      "An outlier is an observation that lies an abnormal distance from other values in the data.",
      "The arithmetic mean is highly sensitive to extreme outliers because it incorporates every magnitude.",
      "The median is robust (resistant) to extreme values because it depends only on ordinal position."
    ],
    "formula": "$$\\text{Mean Sensitivity: } \\bar{x} \\propto x_{\\text{outlier}}, \\quad \\text{Median Robustness: } \\text{Median } = x_{\\left(\\frac{N+1}{2}\\right)} \\text{ (Unaffected by magnitude)}$$",
    "simulator_type": "outlier_robustness_comparator",
    "checkpoints": [
      {
        "question": "Which measure of central tendency is preferred when reporting household income in a city with both low earners and a few billionaires?",
        "options": [
          "Arithmetic Mean",
          "Median",
          "Highest score only",
          "Total sum only"
        ],
        "correct": 1,
        "explanation": "Billionaires create extreme positive outliers that heavily distort the arithmetic mean upwards. The median represents the true middle household, providing a far more realistic picture."
      },
      {
        "question": "For the dataset $5, 7, 8, 10, 100$, what are the median and mean respectively?",
        "options": [
          "Median = 8, Mean = 26",
          "Median = 26, Mean = 8",
          "Median = 8, Mean = 8",
          "Median = 10, Mean = 30"
        ],
        "correct": 0,
        "explanation": "Arranged in order: $5, 7, 8, 10, 100$. The middle value is $8$ (Median). The sum is $130$, so the Mean is $130 / 5 = 26$."
      }
    ]
  },
  {
    "id": 5,
    "title": "Finding Median",
    "subtitle": "Odd vs Even Counts, Ordered Ranks & Percentile Half",
    "content": "<p>The <strong>Median</strong> is the value of the middle observation when data are sorted in ascending or descending numerical order. It divides a distribution into two equal halves (50% below, 50% above):</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Odd Number of Observations ($N = 2k + 1$):</strong> There is a unique single middle element at rank position:</li></ul><div class='p-1 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Position} = \\frac{N + 1}{2}$$</div><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Even Number of Observations ($N = 2k$):</strong> There are two middle elements at positions $\\frac{N}{2}$ and $\\frac{N}{2} + 1$. The median is their arithmetic average:</li></ul><div class='p-1 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Median} = \\frac{x_{(N/2)} + x_{(N/2 + 1)}}{2}$$</div>",
    "key_takeaways": [
      "Data MUST always be sorted in order before determining the median.",
      "For odd $N$: Median is the unique middle value at position $\\frac{N+1}{2}$.",
      "For even $N$: Median is the average of the two middle values at $\\frac{N}{2}$ and $\\frac{N}{2}+1$."
    ],
    "formula": "$$\\text{Median} = \\begin{cases} x_{\\left(\\frac{N+1}{2}\\right)}, & N \\text{ odd} \\\\[6pt] \\frac{x_{(N/2)} + x_{(N/2 + 1)}}{2}, & N \\text{ even} \\end{cases}$$",
    "simulator_type": "median_ordered_ranker",
    "checkpoints": [
      {
        "question": "What is the median of the scores: $14, 6, 22, 9, 18, 30$?",
        "options": [
          "15",
          "16",
          "18",
          "20"
        ],
        "correct": 1,
        "explanation": "Step 1: Sort in ascending order: $6, 9, 14, 18, 22, 30$.<br>Step 2: Here $N = 6$ (even). The middle positions are $6/2 = 3$rd (value 14) and 4th (value 18).<br>Step 3: Average = $\\frac{14 + 18}{2} = \\frac{32}{2} = 16$."
      },
      {
        "question": "If an 11-student cricket squad has scores arranged in order, which player's score is the team median?",
        "options": [
          "The 5th player",
          "The 6th player",
          "The 7th player",
          "Average of 5th and 6th"
        ],
        "correct": 1,
        "explanation": "For odd $N = 11$, position $= \\frac{11 + 1}{2} = \\frac{12}{2} = 6$th player."
      }
    ]
  },
  {
    "id": 6,
    "title": "Finding the Unknown",
    "subtitle": "Inverse Statistical Reasoning & Algebraic Balancing",
    "content": "<p>In real-world testing and scientific analysis, we frequently know the overall mean or median and need to solve for a missing or unknown data entry $x$.</p><p class='mt-2'>Because the arithmetic mean relates to the total sum via:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Total Sum} = N \\times \\bar{x}$$</div><p class='mt-2'>We can set up a simple linear algebraic equation. For example, if a student scored $70, 75, 85, 90$ in four tests and needs an overall mean of $82$ across five tests, what must she score in the 5th test?</p><p class='mt-2'>$$\\text{Required Sum} = 5 \\times 82 = 410$$<br>$$\\text{Current Sum} = 70 + 75 + 85 + 90 = 320$$<br>$$x = 410 - 320 = 90\\text{ marks!}$$</p>",
    "key_takeaways": [
      "Use the total sum identity: $\\sum x_i = N \\times \\bar{x}$.",
      "The missing value is the difference between the required total and current partial sum.",
      "Inverse reasoning turns statistical averages into straightforward linear equations."
    ],
    "formula": "$$x_{\\text{missing}} = \\left(N \\times \\bar{x}\\right) - \\sum_{i=1}^{N-1} x_i$$",
    "simulator_type": "finding_unknown_equation_solver",
    "checkpoints": [
      {
        "question": "The mean of five numbers is 20. Four of the numbers are 15, 18, 22, and 25. What is the fifth number?",
        "options": [
          "18",
          "20",
          "22",
          "24"
        ],
        "correct": 1,
        "explanation": "Total sum required $= 5 \\times 20 = 100$.<br>Sum of known four numbers $= 15 + 18 + 22 + 25 = 80$.<br>Fifth number $= 100 - 80 = 20$."
      },
      {
        "question": "A bowler had a mean of 4 wickets per match across 6 matches. In the 7th match, how many wickets must he take to raise his overall mean to 5?",
        "options": [
          "7 wickets",
          "9 wickets",
          "11 wickets",
          "12 wickets"
        ],
        "correct": 2,
        "explanation": "Total wickets required across 7 matches $= 7 \\times 5 = 35$.<br>Current wickets in 6 matches $= 6 \\times 4 = 24$.<br>Wickets needed $= 35 - 24 = 11$ wickets."
      }
    ]
  },
  {
    "id": 7,
    "title": "Frequency Tables",
    "subtitle": "Grouped Counts, Weighted Totals & Cumulative Frequency",
    "content": "<p>When datasets contain hundreds of numbers with repeated values, listing each number individually is impractical. Instead, data are tabulated in a <strong>frequency table</strong> ($x_i$ with frequency $f_i$):</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Weighted Mean:</strong> Multiply each value $x_i$ by its frequency $f_i$ to find sub-totals, sum them up, and divide by total observations $N = \\sum f_i$:</li></ul><div class='p-1 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}$$</div><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Median via Cumulative Frequency ($cf$):</strong> Running cumulative sums pinpoint the exact category containing the $\\frac{N}{2}$-th or $\\frac{N+1}{2}$-th observation without needing to expand the list.</li></ul>",
    "key_takeaways": [
      "Frequency $f_i$ represents how many times value $x_i$ occurs in the dataset.",
      "Total observations $N = \\sum f_i$; total numerical sum is $\\sum f_i x_i$.",
      "Cumulative frequency tracks the running sum of frequencies to locate the median item."
    ],
    "formula": "$$\\bar{x} = \\frac{\\sum_{i=1}^k f_i x_i}{\\sum_{i=1}^k f_i}, \\quad N = \\sum f_i, \\quad \\text{Median} \\implies \\text{Value where } cf \\ge \\frac{N+1}{2}$$",
    "simulator_type": "frequency_table_mean_median",
    "checkpoints": [
      {
        "question": "In a class, 5 students scored 10 marks, and 15 students scored 20 marks. What is the weighted mean score?",
        "options": [
          "15 marks",
          "17.5 marks",
          "18 marks",
          "16.5 marks"
        ],
        "correct": 1,
        "explanation": "Total sum $= (5 \\times 10) + (15 \\times 20) = 50 + 300 = 350$.<br>Total students $= 5 + 15 = 20$.<br>Mean $= \\frac{350}{20} = 17.5$ marks."
      },
      {
        "question": "In a survey of 31 people, cumulative frequencies for family sizes 2, 3, 4, 5 are 6, 14, 25, 31. What is the median family size?",
        "options": [
          "Size 2",
          "Size 3",
          "Size 4",
          "Size 5"
        ],
        "correct": 2,
        "explanation": "With $N = 31$, the median observation is the $\\frac{31 + 1}{2} = 16$th person. Looking at cumulative frequencies: $cf(3) = 14$ and $cf(4) = 25$. Since 16 falls between 15 and 25, the median is 4."
      }
    ]
  },
  {
    "id": 8,
    "title": "Spreadsheets",
    "subtitle": "Formulas, Cell References & Digital Data Tables",
    "content": "<p>In modern digital workplaces and scientific research, computations are automated using computer <strong>spreadsheets</strong> (like Google Sheets, Microsoft Excel, or LibreOffice Calc):</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Grid Architecture:</strong> Data is organized into <strong>columns</strong> labeled with letters ($A, B, C, \\dots$) and <strong>rows</strong> labeled with numbers ($1, 2, 3, \\dots$). The intersection is a unique <strong>cell address</strong> (e.g., $B4$).</li><li><strong>Formula Syntax:</strong> Every mathematical formula begins with an equals sign ($=$).</li><li><strong>Standard Statistical Functions:</strong></li></ul><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'><code>=SUM(A1:A10)</code> &nbsp;|&nbsp; <code>=AVERAGE(B2:B20)</code> &nbsp;|&nbsp; <code>=MEDIAN(C1:C15)</code></div>",
    "key_takeaways": [
      "Cells are referenced by column letter followed by row number (e.g., A1, D12).",
      "Formulas always begin with an equals sign ($=$) to trigger calculation rather than text display.",
      "Dynamic recalculation updates all formulas automatically when raw cell values change."
    ],
    "formula": "$$\\text{Range Syntax: } \\text{Cell}_{\\text{start}} : \\text{Cell}_{\\text{end}} \\implies \\text{e.g., } =\\text{AVERAGE}(A1:A20)$$",
    "simulator_type": "spreadsheet_formula_studio",
    "checkpoints": [
      {
        "question": "What must precede every formula in a digital spreadsheet software?",
        "options": [
          "A dollar sign ($)",
          "An equals sign (=)",
          "A hashtag (#)",
          "An asterisk (*)"
        ],
        "correct": 1,
        "explanation": "In all spreadsheet programs, entering an equals sign ($=$) signals to the software that the cell contains an executable formula rather than plain text or a static number."
      },
      {
        "question": "If cell A1 contains 10, A2 contains 20, and A3 contains 30, what will the formula '=AVERAGE(A1:A3)' display?",
        "options": [
          "60",
          "20",
          "30",
          "10"
        ],
        "correct": 1,
        "explanation": "The AVERAGE function computes the arithmetic mean: $\\frac{10 + 20 + 30}{3} = \\frac{60}{3} = 20$."
      }
    ]
  },
  {
    "id": 9,
    "title": "Reading Data",
    "subtitle": "Misleading Baselines, Scaling & Critical Literacy",
    "content": "<p>A chart is worth a thousand words\u2014but only if drawn honestly! Graphical representations can unintentionally (or deliberately) mislead viewers if the visual scale is distorted.</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>The Truncated Graph (Broken Baseline):</strong> Starting a bar graph's vertical axis at $90$ instead of $0$ can make a tiny $2\\%$ difference look like a massive $300\\%$ increase! Always check if the vertical axis starts at zero.</li><li><strong>Proportional Area Principle:</strong> The visual area of a graphical symbol must be directly proportional to the numerical quantity it represents. Doubling both width and height quadruples area ($2 \\times 2 = 4$), visually exaggerating the data!</li><li><strong>Scale Consistency:</strong> Equal intervals on the axis must represent equal increments in quantity.</li></ul>",
    "key_takeaways": [
      "Always inspect the vertical scale: verify if it begins at zero or uses a break/kink (zigzag).",
      "Truncated axes visually exaggerate trivial differences between quantities.",
      "Area scaling must match linear proportions to avoid visual deception."
    ],
    "formula": "$$\\text{Visual Integrity Rule: } \\frac{\\text{Graphic Height / Area}}{\\text{Data Value}} = \\text{Constant Scale Factor}$$",
    "simulator_type": "data_visualization_scale_lab",
    "checkpoints": [
      {
        "question": "Why is a bar chart with a vertical axis starting at 95% instead of 0% potentially misleading?",
        "options": [
          "It makes differences between 96% and 98% appear enormous rather than slight",
          "It changes the math test scores of students",
          "It cannot be printed in black and white",
          "It is illegal under geometry rules"
        ],
        "correct": 0,
        "explanation": "Truncating the vertical axis exaggerates small variations, making a minor 2% difference appear visually four or five times larger than it actually is."
      },
      {
        "question": "What symbol is drawn on a coordinate axis when a large gap of unused values is omitted from zero to the first value?",
        "options": [
          "A circular ring",
          "A kink (zigzag / broken line symbol)",
          "A question mark",
          "An arrow pointing up"
        ],
        "correct": 1,
        "explanation": "A kink (zigzag or break mark) is standard convention indicating that the scale does not start from zero continuously, alerting readers to read values carefully."
      }
    ]
  },
  {
    "id": 10,
    "title": "Line Graphs",
    "subtitle": "Continuous Trajectories, Slopes & Interpolation",
    "content": "<p>A <strong>line graph</strong> displays information as a series of data points called 'markers' connected by straight line segments. It is the premier tool for displaying how a continuous variable changes over continuous intervals of time.</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Horizontal Axis ($X$):</strong> Represents the independent variable (usually time: hours, days, months, years).</li><li><strong>Vertical Axis ($Y$):</strong> Represents the dependent variable being measured (e.g., patient temperature, stock price, rainfall).</li><li><strong>Interpreting Slopes:</strong> A steep upward slope indicates rapid increase; a horizontal flat line indicates zero change (stability); a downward slope indicates decrease.</li><li><strong>Interpolation:</strong> Estimating intermediate values between recorded data points by reading along the connecting segment.</li></ul>",
    "key_takeaways": [
      "Line graphs track dynamic continuous trends over unbroken intervals of time.",
      "The steepness (slope) of a line segment directly reflects the rate of change.",
      "Horizontal line segments represent intervals of constancy (zero change)."
    ],
    "formula": "$$\\text{Rate of Change (Slope)} = \\frac{\\Delta y}{\\Delta x} = \\frac{y_2 - y_1}{x_2 - x_1}$$",
    "simulator_type": "line_graph_slope_navigator",
    "checkpoints": [
      {
        "question": "In a hospital patient's 24-hour temperature chart, what does a flat horizontal segment between 2 PM and 6 PM indicate?",
        "options": [
          "The patient's temperature increased rapidly",
          "The patient's temperature remained completely steady at the same degree",
          "The thermometer was broken",
          "The patient was not breathing"
        ],
        "correct": 1,
        "explanation": "A horizontal segment means $\\Delta y = 0$; the temperature value remained constant throughout that 4-hour time interval."
      },
      {
        "question": "Between 9 AM ($20^\\circ\\text{C}$) and 11 AM ($28^\\circ\\text{C}$), what was the average rate of temperature rise per hour?",
        "options": [
          "$4^\\circ\\text{C per hour}$",
          "$8^\\circ\\text{C per hour}$",
          "$2^\\circ\\text{C per hour}$",
          "$14^\\circ\\text{C per hour}$"
        ],
        "correct": 0,
        "explanation": "Rate of change $= \\frac{\\Delta y}{\\Delta t} = \\frac{28 - 20}{11 - 9} = \\frac{8}{2} = 4^\\circ\\text{C per hour}$."
      }
    ]
  },
  {
    "id": 11,
    "title": "Orbital Traffic",
    "subtitle": "Orbital Debris, Satellite Congestion & Exponential Growth",
    "content": "<p>Since the launch of Sputnik in 1957, thousands of artificial satellites have been launched into Low Earth Orbit (LEO). Today, over $10,000$ active satellites and millions of pieces of space debris travel at speeds exceeding $28,000\\text{ km/h}$!</p><p class='mt-2'>Statistical analysis reveals an alarming trend known as the <strong>Kessler Syndrome</strong>: as orbital density increases, the collision frequency rises non-linearly. A collision between two satellites generates thousands of high-speed fragments, triggering a cascading chain reaction of further collisions.</p><p class='mt-2'>Tracking orbital traffic via time-series line graphs allows space agencies like ISRO, NASA, and ESA to predict close encounters (conjunctions) and perform collision avoidance maneuvers in real time.</p>",
    "key_takeaways": [
      "Orbital traffic data exhibits steep exponential growth over recent decades.",
      "Kessler syndrome describes cascading space debris generation through collision feedback loops.",
      "Statistical tracking and conjunction analysis are vital for protecting space infrastructure."
    ],
    "formula": "$$\\text{Collision Probability } P \\propto \\text{Debris Density } \\rho^2 \\times \\text{Relative Velocity } v_{\\text{rel}}$$",
    "simulator_type": "space_jam_orbital_traffic",
    "checkpoints": [
      {
        "question": "Why does a cascading collision in low Earth orbit (Kessler Syndrome) represent a severe global crisis?",
        "options": [
          "It will cause satellites to fall into our drinking water reservoirs immediately",
          "It could create a dense debris belt that renders low Earth orbits unusable for communications, navigation, and weather forecasting for generations",
          "It changes the gravitational constant of the Earth",
          "It will make the Moon disappear"
        ],
        "correct": 1,
        "explanation": "Millions of fragments traveling at hyper-velocity could destroy communication satellites, GPS navigation, and weather observatories, effectively blinding modern civilization."
      },
      {
        "question": "If active satellites increased from 2,000 in 2019 to 10,000 in 2024, what was the average annual increase?",
        "options": [
          "800 per year",
          "1,600 per year",
          "2,000 per year",
          "4,000 per year"
        ],
        "correct": 1,
        "explanation": "Net increase $= 10,000 - 2,000 = 8,000$ satellites over 5 years. Rate $= \\frac{8,000}{5} = 1,600$ satellites per year."
      }
    ]
  },
  {
    "id": 12,
    "title": "Rain Patterns",
    "subtitle": "Seasonality, Monsoons & Moving Averages",
    "content": "<p>Rainfall is the lifeblood of agriculture, water supply, and ecology across the Indian subcontinent. Yet daily rainfall readings are notoriously erratic\u2014a torrential cloudburst one afternoon may be followed by three dry days.</p><p class='mt-2'>How do meteorologists extract clear trends from noisy data? They use two powerful tools:</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Seasonal Aggregation:</strong> Tabulating rainfall by month or season clearly reveals the Indian South-West Monsoon peak (June to September).</li><li><strong>Moving Averages:</strong> By replacing each day's reading with the average of the surrounding 7 days or 30 days, short-term noise is smoothed out, revealing the underlying seasonal tide.</li></ul>",
    "key_takeaways": [
      "Time series data frequently exhibits cyclical seasonal patterns alongside random noise.",
      "Moving averages smooth out short-term fluctuations to reveal underlying macro trends.",
      "Monsoon precipitation charts guide agricultural planning, dam storage, and disaster mitigation."
    ],
    "formula": "$$\\text{3-Period Moving Average: } M_t = \\frac{x_{t-1} + x_t + x_{t+1}}{3}$$",
    "simulator_type": "rain_pattern_time_series",
    "checkpoints": [
      {
        "question": "What is the primary mathematical purpose of computing a moving average on rainfall time-series data?",
        "options": [
          "To make the rainfall numbers look bigger for farmers",
          "To filter out short-term random daily noise and highlight true seasonal patterns and long-term trends",
          "To convert millimeters into liters",
          "To stop the rain from falling"
        ],
        "correct": 1,
        "explanation": "A moving average smooths out erratic daily spikes, allowing meteorologists and planners to track smooth seasonal trajectories and long-term climatic trends."
      },
      {
        "question": "For monthly rainfall of June ($150\\text{ mm}$), July ($300\\text{ mm}$), and August ($270\\text{ mm}$), what is the 3-month average?",
        "options": [
          "$220\\text{ mm}$",
          "$240\\text{ mm}$",
          "$250\\text{ mm}$",
          "$270\\text{ mm}$"
        ],
        "correct": 1,
        "explanation": "Average $= \\frac{150 + 300 + 270}{3} = \\frac{720}{3} = 240\\text{ mm}$."
      }
    ]
  },
  {
    "id": 13,
    "title": "Infographics",
    "subtitle": "Visual Storytelling, Proportional Icons & Cognitive Clarity",
    "content": "<p>An <strong>infographic</strong> (information graphic) is a visual representation of data designed to present complex statistical ideas quickly and clearly to a broad audience.</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Pictograms (Isotypes):</strong> Using repeated icons where each icon represents a fixed unit quantity (e.g., \ud83d\udeb9 = 1,000 citizens, \ud83d\udca7 = 50 liters). This makes abstract numbers immediately relatable.</li><li><strong>Hierarchy & Flow:</strong> Effective infographics guide the reader's eye from the core question to key findings and conclusions through color coding and visual callouts.</li><li><strong>Statistical Ethics:</strong> Good infographics never sacrifice numerical accuracy for artistic flashiness. All symbols must adhere to strict mathematical proportions!</li></ul>",
    "key_takeaways": [
      "Infographics combine graphic design with statistical data to convey information intuitively.",
      "In pictograms, each icon represents a standardized fixed numerical quantity.",
      "Proportionality must be strictly maintained to ensure visual honesty."
    ],
    "formula": "$$\\text{Icon Count} = \\frac{\\text{Total Quantity}}{\\text{Value per Icon}} \\implies N_{\\text{icons}} = \\frac{Q}{V_{\\text{icon}}}$$",
    "simulator_type": "infographics_visual_storyteller",
    "checkpoints": [
      {
        "question": "In a village water infographic, if 1 droplet symbol represents 250 liters of water, how many symbols represent 1,500 liters?",
        "options": [
          "4 symbols",
          "5 symbols",
          "6 symbols",
          "8 symbols"
        ],
        "correct": 2,
        "explanation": "Number of symbols $= \\frac{1,500}{250} = 6$ droplet symbols."
      },
      {
        "question": "What is the primary danger when an graphic designer doubles both the width and height of an icon to represent a doubled quantity?",
        "options": [
          "The icon turns upside down",
          "The area of the icon quadruples ($2 \\times 2 = 4$), visually exaggerating the quantity by 400% instead of 200%",
          "The ink becomes invisible",
          "The icon disappears"
        ],
        "correct": 1,
        "explanation": "Scaling both linear dimensions doubles area quadratically ($2^2 = 4$), giving the false visual impression of a four-fold increase rather than a two-fold increase."
      }
    ]
  },
  {
    "id": 14,
    "title": "Strip Charts",
    "subtitle": "Strip Charts, Segmented Proportions & 100% Stacks",
    "content": "<p>A <strong>segmented strip chart</strong> (or 100% stacked bar) is a powerful tool for displaying how a whole quantity is partitioned into categorical proportions:</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Single Bar Division:</strong> A single continuous rectangular strip represents $100\\%$ of the whole. The strip is sliced into colored segments whose lengths are exactly proportional to each component's percentage share.</li><li><strong>Direct Linear Comparison:</strong> Unlike circular pie charts where readers must gauge angles, human eyes are exceptionally skilled at comparing linear segment lengths along a straight strip!</li><li><strong>Side-by-Side Strips:</strong> Comparing two parallel strips (e.g., Household Budget in 2020 vs 2025) instantly highlights shifting priorities and percentage changes.</li></ul>",
    "key_takeaways": [
      "A 100% strip chart divides a single linear bar into proportional colored segments.",
      "The sum of all segment percentages along the strip must equal exactly $100\\%$.",
      "Linear lengths along a strip are easier for human eyes to compare accurately than circular angles in pie charts."
    ],
    "formula": "$$\\text{Segment Length } L_i = \\frac{P_i}{100} \\times L_{\\text{total}}, \\quad \\sum P_i = 100\\%$$",
    "simulator_type": "strip_chart_percentage_segmenter",
    "checkpoints": [
      {
        "question": "On a $20\\text{ cm}$ long percentage strip chart, what length should represent food expenditure that accounts for $35\\%$ of the budget?",
        "options": [
          "$5\\text{ cm}$",
          "$7\\text{ cm}$",
          "$8.5\\text{ cm}$",
          "$10\\text{ cm}$"
        ],
        "correct": 1,
        "explanation": "Segment length $= 35\\% \\times 20\\text{ cm} = \\frac{35}{100} \\times 20 = 7\\text{ cm}$."
      },
      {
        "question": "Why do many modern data analysts prefer stacked strip charts over circular pie charts?",
        "options": [
          "Rectangles are cheaper to draw than circles",
          "Human visual perception judges linear lengths far more accurately than angular sector wedges",
          "Pie charts can only show two categories",
          "Strip charts only work on computers"
        ],
        "correct": 1,
        "explanation": "Extensive cognitive science research demonstrates that human eyes judge one-dimensional lengths along a common scale with much higher precision than angles or areas of circular sectors."
      }
    ]
  },
  {
    "id": 15,
    "title": "Sleep & Focus Story",
    "subtitle": "Sleep Habits, Alertness & Bivariate Correlation",
    "content": "<p>In the engaging statistical case study <em>'Sleepy-Deepy'</em>, students surveyed classmates to investigate a critical question: <strong>Does sleep duration affect classroom alertness and academic focus?</strong></p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Bivariate Data:</strong> Each student contributed two paired measurements: hours of night sleep ($X$) and an alertness test score out of 100 ($Y$).</li><li><strong>Scatter Plot & Trend:</strong> Plotting pairs as points $(x_i, y_i)$ reveals a clear positive trend: students sleeping fewer than 6 hours consistently had lower alertness scores (mean 58), while those with 8 to 9 hours of sleep maintained top alertness (mean 88).</li><li><strong>Correlation vs Causation:</strong> While high sleep correlates with alertness, researchers must also consider confounding factors like late-night screen time and nutrition!</li></ul>",
    "key_takeaways": [
      "Bivariate data explores the relationship between two distinct numerical variables.",
      "Scatter plots reveal positive, negative, or zero correlation between paired variables.",
      "A strong statistical correlation suggests a relationship but requires scientific control to prove causation."
    ],
    "formula": "$$\\text{Paired Observations: } (x_i, y_i) \\implies \\text{Positive Correlation: As } X \\uparrow, Y \\uparrow$$",
    "simulator_type": "sleepy_deepy_data_story",
    "checkpoints": [
      {
        "question": "In the Sleepy-Deepy study, if students who slept more hours generally achieved higher alertness scores, what type of correlation exists?",
        "options": [
          "Negative correlation",
          "Positive correlation",
          "Zero correlation",
          "Inverse quadratic correlation"
        ],
        "correct": 1,
        "explanation": "When both variables increase together (more sleep hours $\\implies$ higher alertness), the relationship exhibits a positive correlation."
      },
      {
        "question": "Does a strong statistical correlation between sleep and grades prove that sleeping 15 hours a day will automatically make you score 100%?",
        "options": [
          "Yes, because correlation always equals direct linear causation",
          "No; correlation demonstrates an association, but extreme excessive sleep may indicate other health issues and beyond optimal sleep (8-9 hrs) returns plateau",
          "Yes, sleep is the only factor in learning",
          "No, because math does not apply to biology"
        ],
        "correct": 1,
        "explanation": "Correlation does not imply unlimited causation. Healthy sleep within optimal boundaries (8-9 hrs) supports cognitive performance, but excessive sleep yields diminishing returns."
      }
    ]
  },
  {
    "id": 16,
    "title": "Game of Hex",
    "subtitle": "Nash's Hex Theorem, No-Tie Topology & Master Matrix",
    "content": "<p><strong>It's Puzzle Time: The Game of Hex</strong> was invented independently by Danish mathematician Piet Hein (1942) and Nobel laureate John Nash (1948). Played on an $11 \\times 11$ (or $7 \\times 7$) grid of regular hexagons:</p><ul class='list-disc pl-5 mt-2 space-y-1'><li><strong>Rules:</strong> Two players (Red and Blue) take turns placing colored stones on empty hex cells. Red attempts to connect the North and South borders; Blue attempts to connect the East and West borders.</li><li><strong>The No-Tie Theorem:</strong> Nash proved using the Brouwer fixed-point theorem that <strong>Hex can NEVER end in a draw</strong>! Because a connected path for one player topologically blocks the other, exactly one player must win!</li><li><strong>Chapter Summary Matrix:</strong> Arithmetic Mean balances total values (center of mass); Median divides sorted ranks into equal halves; Line graphs track continuous change; Infographics communicate data ethically.</li></ul>",
    "key_takeaways": [
      "Hex is a pure strategy game played on a rhombus of regular hexagons with NO draws possible.",
      "John Nash's Hex Theorem proves that one player must always form an unbroken crossing path.",
      "Statistical summary: Mean $\\bar{x} = \\frac{\\sum x_i}{N}$; Median $= x_{\\left(\\frac{N+1}{2}\\right)}$; sum of deviations $\\sum (x_i - \\bar{x}) = 0$."
    ],
    "formula": "$$\\text{Hex Theorem: } P(\\text{Draw}) = 0 \\implies \\text{Winner } \\in \\{ \\text{Red}, \\text{Blue} \\} \\text{ (No Ties Possible)}$$",
    "simulator_type": "game_of_hex_puzzle_lab",
    "checkpoints": [
      {
        "question": "Why is the Game of Hex mathematically celebrated in game theory and topology?",
        "options": [
          "It has 100 different dice",
          "It is mathematically proven that the game can NEVER end in a draw; one player is guaranteed to win",
          "It can only be played on circular boards",
          "It was invented by ancient Roman gladiators"
        ],
        "correct": 1,
        "explanation": "John Nash proved that the topology of the hexagonal planar graph guarantees an unbroken path for one player inevitably blocks the other, making a draw mathematically impossible."
      },
      {
        "question": "What is the single most important summary equation defining the arithmetic mean as a balance point?",
        "options": [
          "$\\sum (x_i - \\bar{x}) = 0$",
          "$\\sum x_i = 0$",
          "$\\bar{x} = \\text{Median}$",
          "$\\bar{x}^2 = N$"
        ],
        "correct": 0,
        "explanation": "The defining balance condition of the arithmetic mean is that the sum of all signed deviations around it equals zero: $\\sum (x_i - \\bar{x}) = 0$."
      }
    ]
  },
  {
    "id": 17,
    "title": "Mastery Challenge \u2022 Part I",
    "subtitle": "Mean, Fulcrum Balance & Invariant Operations",
    "type": "quiz_slide",
    "questions": [
      {
        "id": "q1",
        "question": "What is the arithmetic mean of the numbers: 12, 15, 18, 21, 24?",
        "options": [
          "16",
          "18",
          "20",
          "21"
        ],
        "correct": 1,
        "solution": "Step 1: Calculate the sum of all numbers: $12 + 15 + 18 + 21 + 24 = 90$.<br>Step 2: Count of numbers $N = 5$.<br>Step 3: Mean $\\bar{x} = \\frac{90}{5} = 18$.<br>(Notice that for an evenly spaced arithmetic progression with odd count, the mean is simply the middle number, 18)."
      },
      {
        "id": "q2",
        "question": "What is the physical interpretation of the arithmetic mean on a number line?",
        "options": [
          "The leftmost point",
          "The rightmost point",
          "The center of mass (balance fulcrum) where net torque is zero",
          "The midpoint between the minimum and maximum"
        ],
        "correct": 2,
        "solution": "Step 1: Treat each data point as a unit mass along a beam.<br>Step 2: The fulcrum balance position is where clockwise moments equal counterclockwise moments.<br>Step 3: This occurs exactly at $\\bar{x}$, where $\\sum (x_i - \\bar{x}) = 0$."
      },
      {
        "id": "q3",
        "question": "If the mean of 6 numbers is 35, what is their total sum?",
        "options": [
          "180",
          "210",
          "240",
          "280"
        ],
        "correct": 1,
        "solution": "Step 1: Use the relationship $\\text{Total Sum} = N \\times \\bar{x}$.<br>Step 2: Total Sum $= 6 \\times 35 = 210$."
      },
      {
        "id": "q4",
        "question": "The mean weight of 8 students is 42 kg. If every student gains exactly 3 kg over the vacation, what is the new mean weight?",
        "options": [
          "42 kg",
          "45 kg",
          "48 kg",
          "50 kg"
        ],
        "correct": 1,
        "solution": "Step 1: By the linear shift property of arithmetic mean, adding a constant $c$ to every value shifts the mean by $+c$.<br>Step 2: New mean $= 42 + 3 = 45\\text{ kg}$."
      },
      {
        "id": "q5",
        "question": "A dataset of 10 numbers has a mean of 15. If each number is multiplied by 4, what is the new mean?",
        "options": [
          "15",
          "30",
          "60",
          "90"
        ],
        "correct": 2,
        "solution": "Step 1: Multiplying all observations by a constant factor $k$ multiplies the mean by $k$.<br>Step 2: New mean $= 15 \\times 4 = 60$."
      },
      {
        "id": "q6",
        "question": "In a dataset, the sum of deviations of 7 observations from the number 14 is +21. What is the actual arithmetic mean?",
        "options": [
          "14",
          "17",
          "21",
          "24"
        ],
        "correct": 1,
        "solution": "Step 1: Recall $\\sum (x_i - A) = \\sum x_i - N \\cdot A$.<br>Step 2: $\\sum x_i = 7 \\times 14 + 21 = 98 + 21 = 119$.<br>Step 3: Actual mean $\\bar{x} = \\frac{119}{7} = 17$ (or $\\bar{x} = A + \\frac{\\sum d_i}{N} = 14 + \\frac{21}{7} = 14 + 3 = 17$)."
      },
      {
        "id": "q7",
        "question": "If the mean of 5 observations $x, x+2, x+4, x+6, x+8$ is 15, what is the value of $x$?",
        "options": [
          "9",
          "11",
          "13",
          "15"
        ],
        "correct": 1,
        "solution": "Step 1: Sum $= x + (x+2) + (x+4) + (x+6) + (x+8) = 5x + 20$.<br>Step 2: Mean $= \\frac{5x + 20}{5} = x + 4$.<br>Step 3: Set $x + 4 = 15 \\implies x = 15 - 4 = 11$."
      },
      {
        "id": "q8",
        "question": "Five numbers have a mean of 28. If one number 40 is excluded from the dataset, what is the mean of the remaining 4 numbers?",
        "options": [
          "24",
          "25",
          "26",
          "27"
        ],
        "correct": 1,
        "solution": "Step 1: Original total sum $= 5 \\times 28 = 140$.<br>Step 2: Subtract the excluded number: $140 - 40 = 100$.<br>Step 3: New count $= 4$.<br>Step 4: New mean $= \\frac{100}{4} = 25$."
      },
      {
        "id": "q9",
        "question": "What is the sum of the deviations of observations: 3, 7, 11, 15 from their mean?",
        "options": [
          "0",
          "4",
          "9",
          "36"
        ],
        "correct": 0,
        "solution": "Step 1: Mean $= \\frac{3 + 7 + 11 + 15}{4} = \\frac{36}{4} = 9$.<br>Step 2: Deviations: $(3-9) + (7-9) + (11-9) + (15-9) = -6 + (-2) + 2 + 6 = 0$.<br>Step 3: The sum of deviations around the mean is universally zero."
      },
      {
        "id": "q10",
        "question": "The mean of 100 items was calculated as 50. It was later found that one observation was misread as 80 instead of the correct value 30. What is the corrected mean?",
        "options": [
          "49.5",
          "50.5",
          "48.0",
          "51.0"
        ],
        "correct": 0,
        "solution": "Step 1: Incorrect total sum $= 100 \\times 50 = 5000$.<br>Step 2: Subtract wrong value and add correct value: Correct sum $= 5000 - 80 + 30 = 4950$.<br>Step 3: Corrected mean $= \\frac{4950}{100} = 49.5$."
      }
    ]
  },
  {
    "id": 18,
    "title": "Mastery Challenge \u2022 Part II",
    "subtitle": "Median, Outliers & Missing Values",
    "type": "quiz_slide",
    "questions": [
      {
        "id": "q11",
        "question": "What is the median of the dataset: 8, 3, 14, 2, 9, 21, 6?",
        "options": [
          "6",
          "8",
          "9",
          "14"
        ],
        "correct": 1,
        "solution": "Step 1: Sort in ascending order: $2, 3, 6, 8, 9, 14, 21$.<br>Step 2: Count $N = 7$ (odd).<br>Step 3: Middle position is $\\frac{7+1}{2} = 4$th position.<br>Step 4: The 4th number is 8."
      },
      {
        "id": "q12",
        "question": "What is the median of the numbers: 15, 22, 9, 31, 18, 27?",
        "options": [
          "18",
          "20",
          "21",
          "22"
        ],
        "correct": 1,
        "solution": "Step 1: Sort in ascending order: $9, 15, 18, 22, 27, 31$.<br>Step 2: Count $N = 6$ (even).<br>Step 3: Middle elements are at positions $6/2 = 3$rd (value 18) and 4th (value 22).<br>Step 4: Median $= \\frac{18 + 22}{2} = \\frac{40}{2} = 20$."
      },
      {
        "id": "q13",
        "question": "Why is the median unaffected when an extreme outlier of 1,000,000 is appended to the numbers 2, 4, 6, 8, 10?",
        "options": [
          "Because math ignores big numbers",
          "Because the median depends on positional rank order, not the magnitude of the extreme tail values",
          "Because 1,000,000 divides by zero",
          "Because 6 is lucky"
        ],
        "correct": 1,
        "solution": "Step 1: The median is a positional measure of central tendency.<br>Step 2: Outliers change the magnitude of total sums, but only count as a single item in the rank order.<br>Step 3: Hence, the median is robust against extreme values."
      },
      {
        "id": "q14",
        "question": "The median of observations 11, 12, 14, x-2, x+4, 20, 22, 25 arranged in ascending order is 17. What is the value of x?",
        "options": [
          "14",
          "15",
          "16",
          "18"
        ],
        "correct": 2,
        "solution": "Step 1: $N = 8$ (even). The middle two terms are at positions 4th ($x-2$) and 5th ($x+4$).<br>Step 2: Median $= \\frac{(x-2) + (x+4)}{2} = \\frac{2x + 2}{2} = x + 1$.<br>Step 3: Set $x + 1 = 17 \\implies x = 16$."
      },
      {
        "id": "q15",
        "question": "A student has scores 78, 82, 86, and 90. What score must she obtain in the 5th test to achieve an overall average of 85?",
        "options": [
          "87",
          "89",
          "91",
          "93"
        ],
        "correct": 1,
        "solution": "Step 1: Total required sum $= 5 \\times 85 = 425$.<br>Step 2: Current sum $= 78 + 82 + 86 + 90 = 336$.<br>Step 3: Required 5th score $= 425 - 336 = 89$."
      },
      {
        "id": "q16",
        "question": "If the mean of 4 numbers is 12 and the mean of another 6 numbers is 17, what is the combined mean of all 10 numbers?",
        "options": [
          "14.5",
          "15.0",
          "15.2",
          "16.0"
        ],
        "correct": 1,
        "solution": "Step 1: Sum of first group $= 4 \\times 12 = 48$.<br>Step 2: Sum of second group $= 6 \\times 17 = 102$.<br>Step 3: Total combined sum $= 48 + 102 = 150$.<br>Step 4: Combined mean $= \\frac{150}{4 + 6} = \\frac{150}{10} = 15.0$."
      },
      {
        "id": "q17",
        "question": "In an ordered dataset of 9 integers, what is the rank position of the median?",
        "options": [
          "4th",
          "5th",
          "6th",
          "Between 4th and 5th"
        ],
        "correct": 1,
        "solution": "Step 1: For odd $N = 9$, position is $\\frac{9+1}{2} = \\frac{10}{2} = 5$th observation."
      },
      {
        "id": "q18",
        "question": "In a symmetric bell-shaped distribution, what is the relationship between the arithmetic mean, median, and mode?",
        "options": [
          "Mean > Median > Mode",
          "Mean < Median < Mode",
          "Mean = Median = Mode",
          "They have no relationship"
        ],
        "correct": 2,
        "solution": "Step 1: In a perfectly symmetric unimodal distribution, the balance point (mean), the middle rank (median), and the peak frequency (mode) coincide at the exact same central value: $\\text{Mean} = \\text{Median} = \\text{Mode}$."
      },
      {
        "id": "q19",
        "question": "If you replace the highest observation in a sorted dataset of 11 numbers with a number 50 units higher, what happens to the median?",
        "options": [
          "The median increases by 50",
          "The median decreases by 50",
          "The median remains strictly unchanged",
          "The median doubles"
        ],
        "correct": 2,
        "solution": "Step 1: The median of 11 sorted numbers is the 6th number.<br>Step 2: Replacing the 11th number with an even larger value leaves the 6th position and its value completely untouched.<br>Step 3: The median remains strictly unchanged."
      },
      {
        "id": "q20",
        "question": "The mean of $x, x+3, x+5, x+7, x+10$ is 15. What is the median?",
        "options": [
          "10",
          "14",
          "15",
          "17"
        ],
        "correct": 2,
        "solution": "Step 1: Sum $= 5x + 25$.<br>Step 2: Mean $= \\frac{5x + 25}{5} = x + 5 = 15 \\implies x = 10$.<br>Step 3: The numbers are $10, 13, 15, 17, 20$.<br>Step 4: The median is the 3rd number, which is 15."
      }
    ]
  },
  {
    "id": 19,
    "title": "Mastery Challenge \u2022 Part III",
    "subtitle": "Frequency Tables, Spreadsheets & Line Graphs",
    "type": "quiz_slide",
    "questions": [
      {
        "id": "q21",
        "question": "A table shows marks $x = [5, 10, 15]$ with frequencies $f = [2, 5, 3]$. What is the mean mark?",
        "options": [
          "10.0",
          "10.5",
          "11.0",
          "11.5"
        ],
        "correct": 1,
        "solution": "Step 1: Calculate $f_i x_i$:<br>$5 \\times 2 = 10$<br>$10 \\times 5 = 50$<br>$15 \\times 3 = 45$<br>Step 2: $\\sum f_i x_i = 10 + 50 + 45 = 105$.<br>Step 3: $\\sum f_i = 2 + 5 + 3 = 10$.<br>Step 4: $\\bar{x} = \\frac{105}{10} = 10.5$."
      },
      {
        "id": "q22",
        "question": "In a spreadsheet, what does the formula '=SUM(B2:B6)' compute?",
        "options": [
          "The average of cells B2 and B6 only",
          "The total sum of all numerical values in cells B2, B3, B4, B5, and B6",
          "The difference B2 - B6",
          "The number of cells in row 2"
        ],
        "correct": 1,
        "solution": "Step 1: The colon ($:$) denotes a contiguous range of cells.<br>Step 2: The SUM function adds every cell from starting cell B2 through ending cell B6 inclusive."
      },
      {
        "id": "q23",
        "question": "In a digital spreadsheet, which formula correctly computes the median of cells D1 through D25?",
        "options": [
          "=MID(D1:D25)",
          "=MEDIAN(D1:D25)",
          "=CENTER(D1:D25)",
          "=AVERAGE(D1:D25)"
        ],
        "correct": 1,
        "solution": "Step 1: The built-in standard statistical function for median is <code>=MEDIAN(range)</code>."
      },
      {
        "id": "q24",
        "question": "What is the slope (rate of change) on a line graph connecting point (2 hr, 60 km) to (5 hr, 210 km)?",
        "options": [
          "30 km/h",
          "40 km/h",
          "50 km/h",
          "60 km/h"
        ],
        "correct": 2,
        "solution": "Step 1: Rate of change $= \\frac{\\Delta y}{\\Delta x} = \\frac{210 - 60}{5 - 2} = \\frac{150}{3} = 50\\text{ km/h}$."
      },
      {
        "id": "q25",
        "question": "On a distance-time line graph, what does a horizontal line segment signify?",
        "options": [
          "Traveling at maximum speed",
          "Moving backward",
          "Stationary (stopped, speed = 0)",
          "Moving with constant acceleration"
        ],
        "correct": 2,
        "solution": "Step 1: A horizontal line has slope zero ($\\Delta y = 0$).<br>Step 2: Distance does not change as time elapses, meaning the object is stationary."
      },
      {
        "id": "q26",
        "question": "Why is a zigzag (kink) symbol used near the origin on an axis of a line graph?",
        "options": [
          "To show where the paper was torn",
          "To indicate that the scale between 0 and the first displayed value has been truncated or omitted",
          "To show that data is negative",
          "To mark a speed bump"
        ],
        "correct": 1,
        "explanation": "A kink (zigzag line) alerts readers that values from zero up to the start of the data range are omitted, preventing misinterpretation of spatial distances."
      },
      {
        "id": "q27",
        "question": "If daily temperatures recorded for 5 consecutive days are 28\u00b0C, 31\u00b0C, 29\u00b0C, 33\u00b0C, 34\u00b0C, what is the 3-day moving average centered on Day 3?",
        "options": [
          "29.0\u00b0C",
          "30.0\u00b0C",
          "31.0\u00b0C",
          "32.0\u00b0C"
        ],
        "correct": 2,
        "solution": "Step 1: A 3-day moving average centered on Day 3 averages Day 2, Day 3, and Day 4.<br>Step 2: Average $= \\frac{31 + 29 + 33}{3} = \\frac{93}{3} = 31.0^\\circ\\text{C}$."
      },
      {
        "id": "q28",
        "question": "In a discrete frequency distribution with 50 total items, in which cumulative frequency category does the median fall?",
        "options": [
          "Category containing cf = 10",
          "First category where cumulative frequency reaches or exceeds 25.5 (or 25/26)",
          "Category with the highest single frequency",
          "Category with the lowest frequency"
        ],
        "correct": 1,
        "solution": "Step 1: With $N = 50$, the median rank is between 25th and 26th.<br>Step 2: We locate the first category whose cumulative frequency is $\\ge 25$."
      },
      {
        "id": "q29",
        "question": "What is the primary role of independent variables in coordinate line plotting?",
        "options": [
          "They are plotted on the vertical y-axis and depend on the other variable",
          "They are plotted on the horizontal x-axis and represent the controlled input (like elapsed time)",
          "They are always multiplied by zero",
          "They can only take negative values"
        ],
        "correct": 1,
        "solution": "Step 1: By universal mathematical convention, independent variables (time, input stages) are assigned to the horizontal X-axis, while dependent observed responses are plotted along the vertical Y-axis."
      },
      {
        "id": "q30",
        "question": "If an astronaut's heart rate was 72 bpm at t = 0 min, 120 bpm at t = 4 min, and 120 bpm at t = 8 min, what was the average rate of increase during the first 4 minutes?",
        "options": [
          "10 bpm/min",
          "12 bpm/min",
          "15 bpm/min",
          "24 bpm/min"
        ],
        "correct": 1,
        "solution": "Step 1: $\\Delta y = 120 - 72 = 48\\text{ bpm}$.<br>Step 2: $\\Delta t = 4 - 0 = 4\\text{ min}$.<br>Step 3: Rate of increase $= \\frac{48}{4} = 12\\text{ bpm per minute}$."
      }
    ]
  },
  {
    "id": 20,
    "title": "Mastery Challenge \u2022 Part IV",
    "subtitle": "Infographics, Strip Charts & Game of Hex",
    "type": "quiz_slide",
    "questions": [
      {
        "id": "q31",
        "question": "In an infographic pictogram, 1 tree symbol represents planting 500 saplings. How many tree symbols represent 3,500 saplings?",
        "options": [
          "5 symbols",
          "6 symbols",
          "7 symbols",
          "8 symbols"
        ],
        "correct": 2,
        "solution": "Step 1: Number of symbols $= \\frac{\\text{Total}}{\\text{Value per symbol}} = \\frac{3,500}{500} = 7$ symbols."
      },
      {
        "id": "q32",
        "question": "On a 100% segmented strip chart of total length 25 cm, what length is assigned to an activity that takes 40% of the day?",
        "options": [
          "8 cm",
          "10 cm",
          "12 cm",
          "15 cm"
        ],
        "correct": 1,
        "solution": "Step 1: Segment length $= 40\\% \\times 25\\text{ cm} = \\frac{40}{100} \\times 25 = 10\\text{ cm}$."
      },
      {
        "id": "q33",
        "question": "What is the sum of all percentages represented in a complete segmented strip chart?",
        "options": [
          "50%",
          "90%",
          "100%",
          "360%"
        ],
        "correct": 2,
        "solution": "Step 1: A strip chart represents a complete whole partitioned into parts.<br>Step 2: The sum of all parts of a whole is always strictly $100\\%$ (unlike circular pie charts where angles sum to $360^\\circ$)."
      },
      {
        "id": "q34",
        "question": "In the Sleepy-Deepy study, what does a negative correlation between evening screen time and sleep duration indicate?",
        "options": [
          "More screen time is associated with fewer hours of sleep",
          "More screen time is associated with more hours of sleep",
          "Screen time has zero relationship with sleep",
          "Students never use screens"
        ],
        "correct": 0,
        "solution": "Step 1: Negative correlation means that as one variable increases, the other variable decreases.<br>Step 2: As evening screen time increases, hours of sleep decrease."
      },
      {
        "id": "q35",
        "question": "Who were the two mathematicians who independently invented the Game of Hex?",
        "options": [
          "Isaac Newton and Gottfried Leibniz",
          "Piet Hein and John Nash",
          "Euclid and Pythagoras",
          "Aryabhata and Bhaskara"
        ],
        "correct": 1,
        "solution": "Step 1: Piet Hein invented the game in 1942 at the Niels Bohr Institute.<br>Step 2: John Nash re-invented it independently in 1948 at Princeton University."
      },
      {
        "id": "q36",
        "question": "What profound mathematical theorem did John Nash prove about the Game of Hex?",
        "options": [
          "It can only be won by the player who moves second",
          "Hex can NEVER end in a tie (draw); exactly one player must win",
          "The game must always last more than 100 moves",
          "The game has no winning strategy"
        ],
        "correct": 1,
        "solution": "Step 1: Using the topology of the hexagonal planar graph and the Brouwer fixed-point theorem, Nash proved that Hex cannot end in a draw.<br>Step 2: An unbroken chain of hexagons connecting one player's sides automatically prevents the opponent from connecting theirs."
      },
      {
        "id": "q37",
        "question": "A student surveys 50 peers and finds that 30 walk to school, 15 cycle, and 5 take a bus. In a 10 cm strip chart, what length represents students who cycle?",
        "options": [
          "1.5 cm",
          "3.0 cm",
          "4.5 cm",
          "6.0 cm"
        ],
        "correct": 1,
        "solution": "Step 1: Fraction of cyclists $= \\frac{15}{50} = 0.30 = 30\\%$.<br>Step 2: Length on a $10\\text{ cm}$ strip $= 30\\% \\times 10\\text{ cm} = 3.0\\text{ cm}$."
      },
      {
        "id": "q38",
        "question": "If a line graph shows a downward sloping curve from left to right, what does it signify about the relationship?",
        "options": [
          "As time increases, the measured quantity decreases",
          "The measured quantity is accelerating upwards",
          "The slope is positive",
          "The rate of change is zero"
        ],
        "correct": 0,
        "solution": "Step 1: Downward slope means negative gradient ($\\Delta y < 0$ as $\\Delta x > 0$).<br>Step 2: The measured quantity decreases over time."
      },
      {
        "id": "q39",
        "question": "Why is the arithmetic mean called a 'measure of central tendency'?",
        "options": [
          "Because it is always located at the exact geographic center of India",
          "Because it identifies a single central value around which data points tend to cluster and balance",
          "Because it only works for circular shapes",
          "Because it ignores all numbers except the middle one"
        ],
        "correct": 1,
        "solution": "Step 1: Measures of central tendency summarize an entire distribution of numbers into a single representative value around which observations cluster and balance."
      },
      {
        "id": "q40",
        "question": "In a dataset where Mean = 25 and Median = 25, if the lowest number 5 is reduced to 1, what happens to the Mean and Median?",
        "options": [
          "Both Mean and Median decrease",
          "Mean decreases, while Median remains unchanged at 25",
          "Mean remains unchanged, while Median decreases",
          "Both Mean and Median remain unchanged"
        ],
        "correct": 1,
        "solution": "Step 1: Reducing an observation lowers the total sum, so the arithmetic mean decreases ($\\bar{x}_{\\text{new}} < 25$).<br>Step 2: The rank order of the middle value is unaffected because reducing the lowest value keeps it in the lowest position.<br>Step 3: Hence, the Median remains completely unchanged at 25."
      }
    ]
  }
]
